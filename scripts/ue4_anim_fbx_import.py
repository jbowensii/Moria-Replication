# UE4 Editor Python script: batch import FBX animation files.
#
# Run from UE4 Python console:
#   exec(open("C:/Users/johnb/OneDrive/Documents/Projects/Moria-Replication/scripts/ue4_anim_fbx_import.py").read())
#
import unreal
import json
import os
import gc
from pathlib import Path

REPO_ROOT = Path("C:/Users/johnb/OneDrive/Documents/Projects/Moria-Replication")
MANIFEST_PATH = REPO_ROOT / "tools" / "anim-fbx-import-manifest.json"
LOG_PATH = REPO_ROOT / "tools" / "anim-fbx-import-results.json"

# How many imports between GC + save-all flushes (prevents OOM)
BATCH_SIZE = 200

# Explicit skeleton mapping: animation path prefix -> skeleton game path
# Keys are matched against game_path segments after /Game/
SKELETON_MAP = {
    # --- Creatures (direct match already worked, but explicit is safer) ---
    "Animations/BadgerBoar":    "/Game/CharacterArt/Creatures/BadgerBoar/SK_BadgerBoar_Skeleton",
    "Animations/Warg":          "/Game/CharacterArt/Creatures/Warg/SK_Warg_Skeleton",
    "Animations/ShadowDragon":  "/Game/CharacterArt/Creatures/ShadowDragon/SK_ShadowDragon_Skeleton",
    "Animations/Goat":          "/Game/CharacterArt/Creatures/Goat/SK_Goat_Skeleton",
    "Animations/Drake":         "/Game/CharacterArt/Creatures/Drake/Drake_Skeleton",
    "Animations/Rat":           "/Game/CharacterArt/Creatures/Rat/Rat_Skeleton",
    "Animations/WhiteDeer":     "/Game/CharacterArt/Creatures/WhiteDeer/SK_WhiteDeer_Skeleton",
    "Animations/FellBeast":     "/Game/CharacterArt/Creatures/FellBeast/FellBeast_Skeleton",
    "Animations/Raven":         "/Game/CharacterArt/Creatures/Raven/Raven_Skeleton",

    # --- Creatures (name mismatch — these failed before) ---
    "Animations/Bear":          "/Game/CharacterArt/Creatures/CaveBear/SK_CaveBear_Skeleton",
    "Animations/Spider":        "/Game/Character/Creatures/Spider/Spider_Parent_Skeleton",
    "Animations/Worm":          "/Game/CharacterArt/Creatures/GreatWorm/GreatWorm_Skeleton",
    "Animations/Watcher":       "/Game/CharacterArt/Creatures/TheWatcher/TheWatcher_Skeleton",
    "Animations/Moth":          "/Game/CharacterArt/Creatures/GiantMoth/Moth_Skeleton",
    "Animations/Bat":           "/Game/Unshippable/ThirdParty/Medhue_Bat/Mesh/Bat_Skeleton",
    "Animations/Grendel":       "/Game/Character/Orcs/Orc_Parent_Skeleton",  # Grendel uses Orc rig

    # --- Humanoids ---
    "Animations/Dwarf":         "/Game/Character/Dwarf/Dwa_FGK_Dwarf_Skeleton",
    "Animations/Orc":           "/Game/Character/Orcs/Orc_Parent_Skeleton",
    "Animations/Goblin":        "/Game/Character/Orcs/Orc_Parent_Skeleton",
    "Animations/Uruk":          "/Game/Character/Orcs/Orc_Parent_Skeleton",
    "Animations/Troll":         "/Game/Character/Orcs/Trolls/Troll_Parent_Skeleton",

    # --- LipSync (facial animations, keyed by sub-character) ---
    "Animations/LipSync/Dwarfs":    "/Game/Character/Dwarf/Dwa_FGK_Dwarf_Skeleton",
    "Animations/LipSync/Orc":       "/Game/Character/Orcs/Orc_Parent_Skeleton",
    "Animations/LipSync/Goblin":    "/Game/Character/Orcs/Orc_Parent_Skeleton",
    "Animations/LipSync/Uruk":      "/Game/Character/Orcs/Orc_Parent_Skeleton",
    "Animations/LipSync/Dragon":    "/Game/CharacterArt/Creatures/ShadowDragon/SK_ShadowDragon_Skeleton",
    "Animations/LipSync/Raven":     "/Game/CharacterArt/Creatures/Raven/Raven_Skeleton",
    "Animations/LipSync/TrollKing": "/Game/Character/Orcs/Trolls/Troll_Parent_Skeleton",

    # --- Unshippable / Prepro ---
    "Unshippable/DwarfPrepro":  "/Game/Unshippable/DwarfPrepro/DwarfFGK_v1/Dwa_Dwarf_Skeleton",
    "Unshippable/OrcPrepro":    "/Game/Unshippable/OrcPrepro/Orc_Skeleton",
    "Unshippable/TrollPrepro":  "/Game/Character/Orcs/Trolls/Troll_Parent_Skeleton",

    # --- FX skeletons ---
    "FX/BlockageDestruction":   "/Game/FX/BlockageDestruction/blockDestruction_v004/blockageDestruction_v004_Skeleton",
    "FX/CeilingCollapse":       "/Game/FX/CeilingCollapse/ceilingCollapse_v004/ceilingCollapse_v004_Skeleton",
    "FX/Monument_FX":           "/Game/FX/Monument_FX/Animation/Monument_Tarp_Cover_Skeleton",
}

# ThirdParty animations need per-file matching
THIRDPARTY_SKELETON_MAP = {
    "Kubold":           "/Game/Character/Dwarf/Dwa_FGK_Dwarf_Skeleton",
    "Medhue_Bat":       "/Game/Unshippable/ThirdParty/Medhue_Bat/Mesh/Bat_Skeleton",
    "ReactionSystemBP": "/Game/Unshippable/ThirdParty/ReactionSystemBP/DemoContent/Characters/Mannequin/Character/Mesh/UE4_Mannequin_Skeleton",
}


def find_skeleton_for_anim(game_path):
    """Find the matching skeleton asset for an animation path using explicit mapping.

    Uses SKELETON_MAP for prefix-based lookup, with longest-prefix-first matching
    so LipSync/Dwarfs beats LipSync.
    """
    # Strip /Game/ prefix for matching
    rel_path = game_path[len("/Game/"):] if game_path.startswith("/Game/") else game_path

    # Try longest prefix first (so LipSync/Dwarfs matches before LipSync)
    sorted_keys = sorted(SKELETON_MAP.keys(), key=len, reverse=True)
    for prefix in sorted_keys:
        if rel_path.startswith(prefix):
            return SKELETON_MAP[prefix]

    # ThirdParty fallback: match by subfolder name
    if "ThirdParty" in game_path:
        for key, skel_path in THIRDPARTY_SKELETON_MAP.items():
            if key in game_path:
                return skel_path

    # Last resort: search asset registry (slow but catches edge cases)
    try:
        registry = unreal.AssetRegistryHelpers.get_asset_registry()
        parts = game_path.split("/")
        if len(parts) >= 4 and parts[2] == "Animations":
            creature_name = parts[3]
            search_paths = [
                f"/Game/CharacterArt/Creatures/{creature_name}",
                f"/Game/Character/Creatures/{creature_name}",
            ]
            for search_path in search_paths:
                assets = registry.get_assets_by_path(search_path, recursive=True)
                for asset_data in assets:
                    if "Skeleton" in str(asset_data.asset_name) and "Mesh" not in str(asset_data.asset_name):
                        return str(asset_data.object_path)
    except Exception:
        pass

    return None


def main():
    fbx_dir = REPO_ROOT / "tools" / "anim-fbx"

    if not MANIFEST_PATH.exists():
        entries = build_manifest(fbx_dir, MANIFEST_PATH)
    else:
        with open(MANIFEST_PATH) as f:
            data = json.load(f)
        # Support both formats: bare list or {entries: [...]}
        entries = data.get("entries", data) if isinstance(data, dict) else data
        print(f"Loaded manifest: {len(entries)} entries")

    # Pre-cache skeleton objects to avoid repeated load_asset calls
    skeleton_cache = {}

    results = []
    success = 0
    failed = 0
    skipped = 0
    no_skeleton = 0
    imports_this_batch = 0

    for entry in entries:
        fbx_path = entry["fbx"]
        dest_dir = entry["dest_dir"]
        asset_name = entry["asset_name"]
        game_path = entry["game_path"]

        # Skip if already imported
        if unreal.EditorAssetLibrary.does_asset_exist(game_path):
            skipped += 1
            continue

        if not os.path.exists(fbx_path):
            results.append({"path": game_path, "status": "missing_fbx"})
            failed += 1
            continue

        # Find skeleton — skip LipSync/RefPoses (no skeleton needed)
        if "/LipSync/RefPoses/" in game_path:
            results.append({"path": game_path, "status": "skipped_refpose"})
            skipped += 1
            continue

        skeleton_path = find_skeleton_for_anim(game_path)
        if not skeleton_path:
            results.append({"path": game_path, "status": "no_skeleton"})
            no_skeleton += 1
            failed += 1
            continue

        # Cache skeleton objects
        if skeleton_path not in skeleton_cache:
            skel_obj = unreal.load_asset(skeleton_path)
            if skel_obj:
                skeleton_cache[skeleton_path] = skel_obj
                print(f"  Loaded skeleton: {skeleton_path}")
            else:
                skeleton_cache[skeleton_path] = None
                print(f"  WARNING: Failed to load skeleton: {skeleton_path}")

        skeleton = skeleton_cache.get(skeleton_path)
        if not skeleton:
            results.append({"path": game_path, "status": "skeleton_load_failed",
                            "skeleton": skeleton_path})
            failed += 1
            continue

        try:
            task = unreal.AssetImportTask()
            task.set_editor_property("filename", fbx_path)
            task.set_editor_property("destination_path", dest_dir)
            task.set_editor_property("destination_name", asset_name)
            task.set_editor_property("replace_existing", False)
            task.set_editor_property("automated", True)
            task.set_editor_property("save", True)

            # FBX import options for animations
            options = unreal.FbxImportUI()
            options.set_editor_property("import_mesh", False)
            options.set_editor_property("import_materials", False)
            options.set_editor_property("import_textures", False)
            options.set_editor_property("import_animations", True)
            options.set_editor_property("import_as_skeletal", True)
            options.set_editor_property("create_physics_asset", False)
            options.set_editor_property("skeleton", skeleton)

            # Animation sequence import settings
            anim_settings = options.get_editor_property("anim_sequence_import_data")
            if anim_settings:
                anim_settings.set_editor_property("import_bone_tracks", True)
                anim_settings.set_editor_property("remove_redundant_keys", False)

            task.set_editor_property("options", options)

            unreal.AssetToolsHelpers.get_asset_tools().import_asset_tasks([task])

            if unreal.EditorAssetLibrary.does_asset_exist(game_path):
                success += 1
                results.append({"path": game_path, "status": "ok",
                                "skeleton": skeleton_path})
            else:
                failed += 1
                results.append({"path": game_path, "status": "import_failed",
                                "skeleton": skeleton_path})

        except Exception as e:
            failed += 1
            results.append({"path": game_path, "status": "error", "error": str(e),
                            "skeleton": skeleton_path})

        imports_this_batch += 1

        # Memory management: flush every BATCH_SIZE imports
        if imports_this_batch >= BATCH_SIZE:
            print(f"  Batch checkpoint ({success} ok, {failed} fail, {skipped} skip) — saving & collecting garbage...")
            # Save all dirty packages to free memory
            unreal.EditorLoadingAndSavingUtils.save_dirty_packages(
                True,   # save_map_packages
                True    # save_content_packages
            )
            gc.collect()
            # Write incremental results so progress isn't lost on crash
            _write_log(LOG_PATH, success, failed, no_skeleton, skipped, results)
            imports_this_batch = 0

    # Final flush
    print(f"\nFinal save...")
    unreal.EditorLoadingAndSavingUtils.save_dirty_packages(True, True)
    gc.collect()

    print(f"\nAnimation FBX Import Complete")
    print(f"  Success:     {success}")
    print(f"  Failed:      {failed}")
    print(f"  No skeleton: {no_skeleton}")
    print(f"  Skipped:     {skipped}")

    _write_log(LOG_PATH, success, failed, no_skeleton, skipped, results)
    print(f"  Log: {LOG_PATH}")


def _write_log(path, success, failed, no_skeleton, skipped, results):
    with open(path, "w") as f:
        json.dump({
            "success": success,
            "failed": failed,
            "no_skeleton": no_skeleton,
            "skipped": skipped,
            "results": results
        }, f, indent=2)


if __name__ == "__main__":
    main()
