"""Prepare batch import directories for tiers 1, 2, and 3.

Tier 1+2: JSON assets -> batch-import-tier12/ for BatchImport commandlet
Tier 3: Mesh PSK references -> tier3-mesh-manifest.json for PSK->FBX->UE4 pipeline
"""
import subprocess
import os
import shutil
import json
from pathlib import Path
from collections import defaultdict

CLOUD_BT = Path("tools/cloud-exports-by-type")
CLOUD = Path("tools/cloud-exports")
CONTENT = Path("project/Content")
BATCH_DIR = Path("tools/batch-import-tier12")
TIER3_MANIFEST = Path("tools/tier3-mesh-manifest.json")

# Types for tier 1 (batch-importable via JsonAsAsset)
TIER1_TYPES = [
    "DataTable", "CurveFloat", "CurveLinearColor", "CurveVector", "CurveTable",
    "MaterialInstanceConstant", "Material", "MaterialFunction",
    "MaterialFunctionMaterialLayer", "MaterialFunctionMaterialLayerBlend",
    "MaterialParameterCollection",
    "PhysicalMaterial", "SubsurfaceProfile",
    "FoliageType_InstancedStaticMesh",
    "StringTable", "UserDefinedStruct", "UserDefinedEnum",
    "NiagaraEffectType", "NiagaraParameterCollection",
    "NiagaraDataInterfaceArrayFloat", "NiagaraDataInterfaceCurve",
    "NiagaraDataInterfaceCamera", "NiagaraDataInterfaceColorCurve",
    "NiagaraDataInterfaceCollisionQuery", "NiagaraDataInterfaceArrayInt32",
    "NiagaraDataInterfaceArrayColor", "NiagaraDataInterfaceArrayFloat3",
    "NiagaraDataInterfaceArrayFloat4",
    "Font", "FontFace",
    "ForceFeedbackEffect",
    "SoundCue",
    "PhysicsAsset",
    "SkeletalMeshLODSettings", "ClothConfigNv",
    "BlackboardData",
    "BodySetup",
    "DistributionFloatConstant",
    "MediaPlayer",
    "LightMapTexture2D", "RuntimeVirtualTexture",
]

# Types for tier 2 (game data assets)
TIER2_TYPES = [
    "MorPrefabData", "PrefabAsset", "InventoryLoadout", "InventoryLimit",
    "MorBubbleDefinition", "MorBubbleData", "MorBubbleCatalog",
    "MoriaMineralPropertyAsset", "MorRuneEffect", "MorItemTintEffect",
    "MorItemEffect", "MorItemEffectsConfig",
    "MorAISettings", "MorAIWaveEncounterSettings",
    "MorArchitectureDecorationConfig",
    "MorDistanceSongValidation", "MorSongCategoryDefinition",
    "MorBackgroundMusicAsset", "MorBackgroundMusicData",
    "MorCharacterFallSettings", "MorPlatformUiConfig", "MorUIConfig",
    "MorAttributeDisplaySettings", "MorDatabase", "MorEconomyTuningData",
    "MorIsoMapTuningData", "MorNpcTuningData", "MorSaveGameData",
    "MorMenuButtons", "MorBiomeLayerProperties",
    "MorShadowFogRepelItemEffect",
    "FGKCharacterData", "FGKCharacterMovementSettings",
    "FGKCharacterCombatSettings", "FGKCharacterAnimSettings",
    "FGKCharacterControlSettings", "FGKCharacterHealthSettings",
    "FGKCharacterInventorySettings", "FGKCharacterLocoSettings",
    "FGKCombatGridSettings", "FGKCharacterBodyStateSettings",
    "FGKAIAttackSettings", "FGKAISenseConfig_Ping",
    "PersonalityInfo", "SurvivalSettings",
    "BiomeDecoConfig", "BiomeAudioConfig", "BiomeRockConfig",
    "EnvQuery",
    "AISenseConfig_Sight", "AISenseConfig_Hearing",
    "VoxelBasicMaterialCollection", "VoxelDataAsset",
]

# Types for tier 3 (meshes)
TIER3_TYPES = ["DestructibleMesh", "SkeletalMesh"]


def get_content_set():
    """Get set of all asset paths already in project."""
    content_str = str(CONTENT.resolve())
    ps_cmd = (
        f"Get-ChildItem -Path '{content_str}' -Filter '*.uasset' "
        f"-Recurse -File | ForEach-Object {{ $_.FullName }}"
    )
    result = subprocess.run(
        ["powershell", "-NoProfile", "-Command", ps_cmd],
        capture_output=True, text=True, errors="replace", timeout=300
    )
    paths = set()
    for f in result.stdout.splitlines():
        f = f.strip()
        if f:
            rel = os.path.relpath(f, content_str).replace("\\", "/")
            paths.add(rel.rsplit(".", 1)[0])
    return paths


def find_missing_by_type(type_name, content_set):
    """Find JSON files in cloud-exports-by-type that aren't imported yet."""
    type_dir = CLOUD_BT / type_name
    if not type_dir.exists():
        return []

    missing = []
    for jp in type_dir.rglob("*.json"):
        rel = os.path.relpath(jp, type_dir).replace("\\", "/")
        game_path = rel.rsplit(".", 1)[0]
        if game_path not in content_set:
            missing.append((game_path, jp))
    return missing


def find_cloud_json(game_path):
    """Find the JSON file in cloud-exports for a game path."""
    direct = CLOUD / (game_path + ".json")
    if direct.exists():
        return direct
    return None


def main():
    print("Building content index...")
    content_set = get_content_set()
    print(f"  {len(content_set)} assets in project")

    # Clean batch dir
    if BATCH_DIR.exists():
        shutil.rmtree(BATCH_DIR)

    # --- TIER 1 + 2 ---
    tier12_count = 0
    tier12_by_type = defaultdict(int)

    for tier_label, type_list in [("Tier1", TIER1_TYPES), ("Tier2", TIER2_TYPES)]:
        for type_name in type_list:
            missing = find_missing_by_type(type_name, content_set)
            if not missing:
                continue

            for game_path, bt_json in missing:
                # Find source JSON - prefer cloud-exports (has proper path structure)
                src = find_cloud_json(game_path)
                if src is None:
                    src = bt_json

                dst = BATCH_DIR / "Moria" / "Content" / (game_path + ".json")
                dst.parent.mkdir(parents=True, exist_ok=True)
                try:
                    os.link(str(src), str(dst))
                except OSError:
                    shutil.copy2(str(src), str(dst))

                tier12_count += 1
                tier12_by_type[type_name] += 1

    print(f"\nTier 1+2: {tier12_count} JSONs staged in {BATCH_DIR}")
    for t, c in sorted(tier12_by_type.items(), key=lambda x: -x[1]):
        print(f"  {t}: {c}")

    # --- TIER 3: Meshes ---
    tier3_psk = []
    tier3_fbx_needed = []
    tier3_no_source = []

    for type_name in TIER3_TYPES:
        missing = find_missing_by_type(type_name, content_set)
        for game_path, bt_json in missing:
            # Check if cloud-exports has a PSK reference
            src = find_cloud_json(game_path)
            if src is None:
                tier3_no_source.append((game_path, type_name))
                continue

            with open(src) as f:
                data = json.load(f)

            if isinstance(data, dict) and "path" in data:
                psk_path = data["path"]
                if Path(psk_path).exists():
                    fbx_out = f"tools/umodel-meshes-fbx-tier3/Game/{game_path}.fbx"
                    tier3_psk.append([psk_path, fbx_out])
                else:
                    tier3_no_source.append((game_path, f"{type_name} (PSK missing)"))
            else:
                # JSON-based import (not PSK) - stage for batch import
                dst = BATCH_DIR / "Moria" / "Content" / (game_path + ".json")
                dst.parent.mkdir(parents=True, exist_ok=True)
                try:
                    os.link(str(src), str(dst))
                except OSError:
                    shutil.copy2(str(src), str(dst))
                tier12_count += 1
                tier12_by_type[type_name] += 1

    # Write tier 3 PSK manifest
    with open(TIER3_MANIFEST, "w") as f:
        json.dump(tier3_psk, f, indent=2)

    print(f"\nTier 3 meshes:")
    print(f"  PSK available (-> FBX -> UE4): {len(tier3_psk)}")
    print(f"  Added to JSON batch:           {tier12_by_type.get('DestructibleMesh', 0) + tier12_by_type.get('SkeletalMesh', 0)}")
    print(f"  No source found:               {len(tier3_no_source)}")

    if tier3_no_source:
        print(f"\n  Assets with no PSK or JSON source:")
        for gp, reason in tier3_no_source[:20]:
            print(f"    {reason} | {Path(gp).name}")
        if len(tier3_no_source) > 20:
            print(f"    ... and {len(tier3_no_source) - 20} more")

    # Final count
    total_batch = sum(1 for _ in BATCH_DIR.rglob("*.json")) if BATCH_DIR.exists() else 0
    print(f"\nTotal staged for BatchImport: {total_batch}")
    print(f"Total staged for PSK pipeline: {len(tier3_psk)}")


if __name__ == "__main__":
    main()
