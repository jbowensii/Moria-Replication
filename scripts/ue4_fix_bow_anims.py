# UE4 Editor Python script: retry failed bow/crossbow animation imports.
#
# These 7 animations failed with the standard Dwa_FGK_Dwarf_Skeleton.
# Strategy: try import with bone track deletion disabled, and if that fails,
# try with the weapon-specific skeleton (ShortBow / Crossbow).
#
# Run from UE4 Python console:
#   exec(open("C:/Users/johnb/OneDrive/Documents/Projects/Moria-Replication/scripts/ue4_fix_bow_anims.py").read())
#
import unreal
import json
import os
from pathlib import Path

REPO_ROOT = Path("C:/Users/johnb/OneDrive/Documents/Projects/Moria-Replication")
LOG_PATH = REPO_ROOT / "tools" / "bow-anim-fix-results.json"

# The 7 failed animations and their FBX paths
FAILED_ANIMS = [
    {
        "fbx": str(REPO_ROOT / "tools/anim-fbx/Animations/Dwarf/Dwa_Bow_Combat_Aim_Fire_Bow.fbx"),
        "game_path": "/Game/Animations/Dwarf/Dwa_Bow_Combat_Aim_Fire_Bow",
        "dest_dir": "/Game/Animations/Dwarf",
        "asset_name": "Dwa_Bow_Combat_Aim_Fire_Bow",
    },
    {
        "fbx": str(REPO_ROOT / "tools/anim-fbx/Animations/Dwarf/Dwa_Bow_Combat_Aim_Loop_Bow.fbx"),
        "game_path": "/Game/Animations/Dwarf/Dwa_Bow_Combat_Aim_Loop_Bow",
        "dest_dir": "/Game/Animations/Dwarf",
        "asset_name": "Dwa_Bow_Combat_Aim_Loop_Bow",
    },
    {
        "fbx": str(REPO_ROOT / "tools/anim-fbx/Animations/Dwarf/Dwa_Bow_Combat_HipAim_Fire_Bow.fbx"),
        "game_path": "/Game/Animations/Dwarf/Dwa_Bow_Combat_HipAim_Fire_Bow",
        "dest_dir": "/Game/Animations/Dwarf",
        "asset_name": "Dwa_Bow_Combat_HipAim_Fire_Bow",
    },
    {
        "fbx": str(REPO_ROOT / "tools/anim-fbx/Animations/Dwarf/Dwa_Bow_Draw_Aim_Bow.fbx"),
        "game_path": "/Game/Animations/Dwarf/Dwa_Bow_Draw_Aim_Bow",
        "dest_dir": "/Game/Animations/Dwarf",
        "asset_name": "Dwa_Bow_Draw_Aim_Bow",
    },
    {
        "fbx": str(REPO_ROOT / "tools/anim-fbx/Animations/Dwarf/Dwa_Bow_Draw_HipAim_Bow.fbx"),
        "game_path": "/Game/Animations/Dwarf/Dwa_Bow_Draw_HipAim_Bow",
        "dest_dir": "/Game/Animations/Dwarf",
        "asset_name": "Dwa_Bow_Draw_HipAim_Bow",
    },
    {
        "fbx": str(REPO_ROOT / "tools/anim-fbx/Animations/Dwarf/Dwa_Xbow_Combat_Atk_Fire_BOW.fbx"),
        "game_path": "/Game/Animations/Dwarf/Dwa_Xbow_Combat_Atk_Fire_BOW",
        "dest_dir": "/Game/Animations/Dwarf",
        "asset_name": "Dwa_Xbow_Combat_Atk_Fire_BOW",
    },
    {
        "fbx": str(REPO_ROOT / "tools/anim-fbx/Animations/Dwarf/Dwa_Xbow_Combat_Atk_Reload_Bow.fbx"),
        "game_path": "/Game/Animations/Dwarf/Dwa_Xbow_Combat_Atk_Reload_Bow",
        "dest_dir": "/Game/Animations/Dwarf",
        "asset_name": "Dwa_Xbow_Combat_Atk_Reload_Bow",
    },
]

# Skeletons to try in order (dwarf first, then weapon-specific)
SKELETON_CANDIDATES = [
    "/Game/Character/Dwarf/Dwa_FGK_Dwarf_Skeleton",
    "/Game/Items/Weapons/Models/Dwarf_Weapons/D_Weapon_BlueMountains_ShortBow/D_Weapon_BlueMountains_ShortBow_Skeleton",
    "/Game/Items/Weapons/Models/Dwarf_Weapons/SM_Crossbow_2H/SM_Crossbow_2H_Skeleton",
    "/Game/Unshippable/DwarfPrepro/DwarfFGK_v1/Dwa_Dwarf_Skeleton",
]


def try_import(entry, skeleton, use_default_sample_rate=False, delete_existing_morph=True):
    """Attempt a single FBX animation import with given skeleton and settings."""
    task = unreal.AssetImportTask()
    task.set_editor_property("filename", entry["fbx"])
    task.set_editor_property("destination_path", entry["dest_dir"])
    task.set_editor_property("destination_name", entry["asset_name"])
    task.set_editor_property("replace_existing", True)
    task.set_editor_property("automated", True)
    task.set_editor_property("save", True)

    options = unreal.FbxImportUI()
    options.set_editor_property("import_mesh", False)
    options.set_editor_property("import_materials", False)
    options.set_editor_property("import_textures", False)
    options.set_editor_property("import_animations", True)
    options.set_editor_property("import_as_skeletal", True)
    options.set_editor_property("create_physics_asset", False)
    options.set_editor_property("skeleton", skeleton)

    anim_settings = options.get_editor_property("anim_sequence_import_data")
    if anim_settings:
        anim_settings.set_editor_property("import_bone_tracks", True)
        anim_settings.set_editor_property("remove_redundant_keys", False)
        if use_default_sample_rate:
            anim_settings.set_editor_property("use_default_sample_rate", True)
        if delete_existing_morph:
            anim_settings.set_editor_property("delete_existing_morph_target_curves", False)

    task.set_editor_property("options", options)
    unreal.AssetToolsHelpers.get_asset_tools().import_asset_tasks([task])

    return unreal.EditorAssetLibrary.does_asset_exist(entry["game_path"])


def main():
    results = []

    # Load all candidate skeletons
    skeleton_cache = {}
    for skel_path in SKELETON_CANDIDATES:
        skel = unreal.load_asset(skel_path)
        if skel:
            skeleton_cache[skel_path] = skel
            print(f"  Loaded skeleton: {skel_path}")
        else:
            print(f"  WARNING: Could not load skeleton: {skel_path}")

    for entry in FAILED_ANIMS:
        name = entry["asset_name"]
        game_path = entry["game_path"]

        # Skip if already imported (from a prior run)
        if unreal.EditorAssetLibrary.does_asset_exist(game_path):
            print(f"  SKIP (exists): {name}")
            results.append({"name": name, "status": "already_exists"})
            continue

        if not os.path.exists(entry["fbx"]):
            print(f"  MISSING FBX: {name}")
            results.append({"name": name, "status": "missing_fbx"})
            continue

        imported = False

        # Strategy 1: Try each skeleton with default settings
        for skel_path, skel_obj in skeleton_cache.items():
            print(f"  Trying {name} with {skel_path.split('/')[-1]}...", end="")
            if try_import(entry, skel_obj):
                print(" OK!")
                results.append({"name": name, "status": "ok", "skeleton": skel_path, "strategy": "default"})
                imported = True
                break
            else:
                print(" failed")

        if imported:
            continue

        # Strategy 2: Try with use_default_sample_rate=True
        for skel_path, skel_obj in skeleton_cache.items():
            print(f"  Trying {name} with {skel_path.split('/')[-1]} + default_sample_rate...", end="")
            if try_import(entry, skel_obj, use_default_sample_rate=True):
                print(" OK!")
                results.append({"name": name, "status": "ok", "skeleton": skel_path, "strategy": "default_sample_rate"})
                imported = True
                break
            else:
                print(" failed")

        if not imported:
            print(f"  FAILED all strategies: {name}")
            results.append({"name": name, "status": "all_failed"})

    # Summary
    ok = sum(1 for r in results if r["status"] == "ok")
    skip = sum(1 for r in results if r["status"] == "already_exists")
    fail = sum(1 for r in results if r["status"] in ("all_failed", "missing_fbx"))

    print(f"\nBow Animation Fix Results")
    print(f"  OK:      {ok}")
    print(f"  Skipped: {skip}")
    print(f"  Failed:  {fail}")

    with open(LOG_PATH, "w") as f:
        json.dump({"ok": ok, "skipped": skip, "failed": fail, "results": results}, f, indent=2)
    print(f"  Log: {LOG_PATH}")


if __name__ == "__main__":
    main()
