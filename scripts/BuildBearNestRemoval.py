#!/usr/bin/env python3
"""
BuildBearNestRemoval.py — Build the BearNestRemoval mod pak.

Two-pronged approach to removing bear nest visuals:
  A) Replace 18 deco mesh files with per-target Debris replacements
     (each has correct internal package name + export ObjectName to
     avoid IoStore FNameEntry crashes during async loading)
  B) Strip deco mesh batches from PD_CPF_BearNest prefab data so the
     rubble, bones, dirt, and midden surrounding the nest aren't spawned

Bears still spawn — only the visual decoration is removed.

Pipeline:
  1. Convert Debris template to JSON, create per-target replacement
     meshes with correct internal names via tojson/fromjson
  2. UAssetGUI tojson on original PD_CPF_BearNest.uasset
  3. Strip unwanted InstancedMeshCatalog batches from the JSON
  4. UAssetGUI fromjson → modified PD_CPF_BearNest.uasset/.uexp
  5. Stage everything under correct Moria/Content/ paths
  6. Validate staged assets with UAssetGUI
  7. retoc to-zen → IoStore .pak/.ucas/.utoc
  8. Zip to ~/Downloads/BearNestRemoval_v{VERSION}.zip

Usage:
    python scripts/BuildBearNestRemoval.py
"""

import json
import os
import shutil
import stat
import subprocess
import sys
import time
import zipfile
from pathlib import Path

# ---------------------------------------------------------------------------
# Paths
# ---------------------------------------------------------------------------
SCRIPT_DIR = Path(__file__).resolve().parent
PROJECT_ROOT = SCRIPT_DIR.parent

EXPERIMENT_DIR = PROJECT_ROOT / 'experiments' / 'bearnest_empty'
STAGING_DECO = EXPERIMENT_DIR / 'staging_deco'    # deco mesh replacements
STAGING_PD = EXPERIMENT_DIR / 'staging_pd'        # modified prefab data
OUTPUT_DIR = EXPERIMENT_DIR / 'output'
WORK_DIR = EXPERIMENT_DIR / 'work'                # scratch for tojson/fromjson
DOWNLOADS_DIR = Path(os.path.expanduser('~/Downloads'))

# Source: cooked Debris mesh from UE4.27 project
COOKED_DEBRIS_DIR = Path(r'C:\Unreal Projects\Moria\Saved\Cooked\WindowsNoEditor\Moria\Content')
DEBRIS_UASSET = COOKED_DEBRIS_DIR / 'Debris.uasset'
DEBRIS_UEXP = COOKED_DEBRIS_DIR / 'Debris.uexp'

# Source: original PD_CPF_BearNest from legacy assets
LEGACY_PD = PROJECT_ROOT / 'tools' / 'legacy-assets' / 'Moria' / 'Content' / 'Tech' / 'Data' / 'Prefabs' / 'PD_CPF_BearNest.uasset'
LEGACY_PD_EXP = LEGACY_PD.with_suffix('.uexp')

# Tools
RETOC_EXE = PROJECT_ROOT / 'tools' / 'retoc' / 'bin' / 'retoc.exe'
UASSETGUI_EXE = PROJECT_ROOT / 'tools' / 'UAssetGUI' / 'UAssetGUI.exe'

UE_VERSION = 'VER_UE4_27'       # for UAssetGUI tojson/fromjson
RETOC_VERSION = 'UE4_27'        # for retoc to-zen (no VER_ prefix)

MOD_VERSION = '1.2.0'
PAK_NAME_DECO = 'BearNestDeco_P'      # Deco mesh replacements (invisible Debris)
PAK_NAME_PD = 'BearNestPrefab_P'      # Modified prefab data (stripped batches)

# ---------------------------------------------------------------------------
# Deco mesh replacements (invisible Debris swap)
# ---------------------------------------------------------------------------
DECO_MESH_REPLACEMENTS = [
    # (mesh_name, staging subpath under Moria/Content/)
    # --- Main nest meshes ---
    ('BearNest_Deco_PH',            'LevelDesign/Deco/Nests_Deco'),
    ('BearNest_Deco_PH_A',          'LevelDesign/Deco/Nests_Deco'),
    ('BearNest_Deco_PH_Collision',   'LevelDesign/Deco/Nests_Deco/Collision'),
    ('Merged_BearNest_Deco_PH',      'LevelDesign/Deco/Nests_Deco'),
    # --- Rubble piles ---
    ('Rubble_Masonry_Pile_A',        'Art/Assets/Kits/Deco/Rubble'),
    ('Rubble_Masonry_Pile_B',        'Art/Assets/Kits/Deco/Rubble'),
    ('Rubble_Masonry_Pile_C',        'Art/Assets/Kits/Deco/Rubble'),
    ('Rubble_Masonry_Pile_D',        'Art/Assets/Kits/Deco/Rubble'),
    # --- Orc midden ---
    ('Orc_Shanty_Midden_B_A',       'Art/Assets/Kits/Deco/Orc/Shanty'),
    # --- Bones ---
    ('Deep_Remains_Bones_Femur',     'Art/Assets/Kits/Deco/Warrens_Tomb'),
    ('Deep_Remains_Bones_Humerus',   'Art/Assets/Kits/Deco/Warrens_Tomb'),
    ('Deep_Remains_Bones_Pelvis',    'Art/Assets/Kits/Deco/Warrens_Tomb'),
    ('Remains_Bones_Assemblage_A',   'Art/Assets/Kits/Deco/Warrens_Tomb'),
    ('Remains_Bones_Assemblage_C',   'Art/Assets/Kits/Deco/Warrens_Tomb'),
    ('Remains_Bones_Assemblage_E',   'Art/Assets/Kits/Deco/Warrens_Tomb'),
    # --- Dirt mounds ---
    ('Dirt_Mound_I',                 'Art/Assets/Kits/Misc/Dirt_Mounds'),
    ('Suburbs_Dirt_Mound_A',         'Art/Assets/Kits/Misc/Dirt_Mounds'),
    # --- Warren nest (the actual visible mesh inside BP_PlaceholderNestCore) ---
    ('Warren_Nest_A',                'Art/Assets/Kits/Deco/Warrens_Tomb'),
]

# ---------------------------------------------------------------------------
# Mesh families to strip from PD_CPF_BearNest InstancedMeshCatalog
# These are the deco meshes embedded in the bear nest prefab itself.
# Matching is by substring — any batch whose mesh import name contains
# one of these strings will be removed.
# ---------------------------------------------------------------------------
PREFAB_MESH_STRIP_PATTERNS = [
    'BearNest_Deco_PH',
    'Rubble_Masonry_Pile',
    'Orc_Shanty_Midden',
    'Remains_Bones',
    'Deep_Remains_Bones',
    'Dirt_Mound',
    'Suburbs_Dirt_Mound',
]


# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------

def log(msg=''):
    print(msg)


def rmtree_safe(d):
    """Remove directory tree with OneDrive lock retry."""
    if not d.exists():
        return
    for attempt in range(3):
        try:
            shutil.rmtree(d, onerror=_rmtree_onerror)
            return
        except PermissionError:
            time.sleep(1)
    log(f"  WARN: Could not fully remove {d}, continuing anyway")


def _rmtree_onerror(func, path, exc_info):
    """Handle OneDrive / read-only locks during rmtree."""
    os.chmod(path, stat.S_IWRITE)
    time.sleep(0.2)
    func(path)


def run_uassetgui_tojson(uasset_path: Path, json_output: Path):
    """Convert .uasset to UAssetAPI JSON."""
    cmd = [str(UASSETGUI_EXE), 'tojson', str(uasset_path), str(json_output), UE_VERSION]
    result = subprocess.run(cmd, capture_output=True, text=True, timeout=60)
    if result.returncode != 0:
        log(f"    FAIL: UAssetGUI tojson exit={result.returncode}")
        if result.stderr:
            log(f"    stderr: {result.stderr[:500]}")
        return False
    return True


def run_uassetgui_fromjson(json_path: Path, uasset_output: Path):
    """Convert UAssetAPI JSON back to .uasset/.uexp."""
    cmd = [str(UASSETGUI_EXE), 'fromjson', str(json_path), str(uasset_output), UE_VERSION]
    result = subprocess.run(cmd, capture_output=True, text=True, timeout=60)
    if result.returncode != 0:
        log(f"    FAIL: UAssetGUI fromjson exit={result.returncode}")
        if result.stderr:
            log(f"    stderr: {result.stderr[:500]}")
        return False
    return True


def run_retoc_tozen(staging_dir: Path, output_dir: Path, pak_name: str):
    """Package staged files into IoStore pak.
    NEVER use --override-container-header-version (causes crash).
    """
    output_utoc = output_dir / f'{pak_name}.utoc'
    cmd = [str(RETOC_EXE), 'to-zen', '-v', '--version', RETOC_VERSION,
           str(staging_dir), str(output_utoc)]
    log(f"  retoc to-zen: {pak_name}")
    result = subprocess.run(cmd, capture_output=True, text=True, timeout=300)
    if result.stdout:
        for line in result.stdout.strip().split('\n')[-5:]:
            log(f"  [retoc] {line}")
    if result.stderr:
        for line in result.stderr.strip().split('\n')[-5:]:
            log(f"  [retoc] {line}")
    if result.returncode != 0:
        log(f"  ERROR: retoc to-zen failed (exit={result.returncode})")
        return False
    return True


def resolve_import_name(imports, import_index):
    """Resolve a negative import index to the import's ObjectName.

    UAssetAPI uses 1-based negative indices: -1 = imports[0], -2 = imports[1], etc.
    """
    if import_index >= 0 or not imports:
        return None
    idx = (-import_index) - 1
    if idx < len(imports):
        return imports[idx].get('ObjectName', '')
    return None


def should_strip_batch(mesh_name, strip_patterns):
    """Check if a mesh name matches any of the strip patterns."""
    if not mesh_name:
        return False
    for pattern in strip_patterns:
        if pattern in mesh_name:
            return True
    return False


def create_replacement_mesh(debris_json_template, mesh_name, subpath, work_dir):
    """Create a per-target Debris replacement with correct internal names.

    The Debris mesh has internal name "/Game/Debris" + export "Debris".
    IoStore requires the internal package name and export ObjectName to match
    what other packages expect when they import this asset.  Mismatched names
    cause ACCESS_VIOLATION in FNameEntry::AppendNameToString during loading.

    Returns (uasset_path, uexp_path) or None on failure.
    """
    import copy
    data = copy.deepcopy(debris_json_template)

    # Build the /Game/... package path from the staging subpath
    game_path = f'/Game/{subpath}/{mesh_name}'

    # --- Fix NameMap ---
    nm = data.get('NameMap', [])
    for i, entry in enumerate(nm):
        if entry == '/Game/Debris':
            nm[i] = game_path
        elif entry == 'Debris':
            nm[i] = mesh_name

    # --- Fix FolderName ---
    data['FolderName'] = game_path

    # --- Fix export ObjectName (export index 2 = the StaticMesh) ---
    for exp in data.get('Exports', []):
        if exp.get('ObjectName') == 'Debris':
            exp['ObjectName'] = mesh_name

    # --- Save modified JSON ---
    json_path = work_dir / f'{mesh_name}_replacement.json'
    with open(json_path, 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=2)

    # --- fromjson → .uasset/.uexp ---
    out_uasset = work_dir / f'{mesh_name}.uasset'
    if not run_uassetgui_fromjson(json_path, out_uasset):
        log(f"    FAIL: Could not build replacement for {mesh_name}")
        return None

    out_uexp = out_uasset.with_suffix('.uexp')
    if not out_uasset.exists() or not out_uexp.exists():
        log(f"    FAIL: fromjson missing output for {mesh_name}")
        return None

    return out_uasset, out_uexp


def strip_catalog_batches(properties, catalog_name, strip_patterns, imports):
    """Strip batches from InstancedMeshCatalog or InstancedBreakableCatalog.

    Returns (removed_count, kept_count).
    """
    removed = 0
    kept = 0

    for prop in properties:
        if prop.get('Name') != catalog_name:
            continue

        catalog_value = prop.get('Value', [])
        for catalog_entry in catalog_value:
            if catalog_entry.get('Name') != 'Batches':
                continue

            batches = catalog_entry.get('Value', [])
            filtered_batches = []

            for batch in batches:
                batch_props = batch.get('Value', [])

                # Find mesh name — in InstancedMeshCatalog it's Definition→Mesh,
                # in InstancedBreakableCatalog it's Definition→Mesh→Mesh (soft obj)
                mesh_name = None
                for bp in batch_props:
                    if bp.get('Name') == 'Definition':
                        def_props = bp.get('Value', [])
                        for dp in def_props:
                            if dp.get('Name') == 'Mesh':
                                # InstancedMeshCatalog: integer import index
                                val = dp.get('Value')
                                if isinstance(val, int):
                                    mesh_name = resolve_import_name(imports, val)
                                # InstancedBreakableCatalog: nested struct with soft obj
                                elif isinstance(val, list):
                                    for sv in val:
                                        if sv.get('Name') == 'Mesh':
                                            sov = sv.get('Value', {})
                                            ap = sov.get('AssetPath', {})
                                            asset = ap.get('AssetName', '')
                                            if asset:
                                                mesh_name = asset.split('/')[-1].split('.')[0]
                                            break
                                break
                        break

                    # Also check BreakableClass for breakable catalog
                    if bp.get('Name') == 'BreakableClass' and not mesh_name:
                        sov = bp.get('Value', {})
                        ap = sov.get('AssetPath', {})
                        asset = ap.get('AssetName', '')
                        if asset:
                            mesh_name = asset.split('/')[-1].split('.')[0]

                if should_strip_batch(mesh_name, strip_patterns):
                    # Count instances
                    inst_count = 0
                    for bp in batch_props:
                        if bp.get('Name') == 'Instances':
                            inst_count = len(bp.get('Value', []))
                            break
                    if inst_count == 0:
                        inst_count = 1  # breakable entries may not have Instances array
                    log(f"    [{catalog_name}] Removing: {mesh_name} ({inst_count} instance(s))")
                    removed += inst_count
                else:
                    filtered_batches.append(batch)
                    kept += 1

            # UAssetGUI crashes on empty struct arrays — keep 1 dummy batch
            # with 1 instance (mesh file is already replaced with Debris)
            if not filtered_batches and batches:
                dummy = json.loads(json.dumps(batches[0]))  # deep copy
                # Keep only 1 instance
                for bp in dummy.get('Value', []):
                    if bp.get('Name') == 'Instances':
                        if bp.get('Value') and len(bp['Value']) > 1:
                            bp['Value'] = bp['Value'][:1]
                        break
                filtered_batches = [dummy]
                log(f"    [{catalog_name}] (Kept 1 dummy batch - mesh replaced with Debris)")

            catalog_entry['Value'] = filtered_batches
            break
        break

    return removed, kept


def strip_prefab_deco_batches(json_data):
    """Remove unwanted batches from both InstancedMeshCatalog and
    InstancedBreakableCatalog in PD_CPF_BearNest JSON.

    Returns (modified_data, total_removed, total_kept).
    """
    imports = json_data.get('Imports', [])
    exports = json_data.get('Exports', [])

    if not exports:
        log("    WARN: No exports in PD_CPF_BearNest")
        return json_data, 0, 0

    export0 = exports[0]
    properties = export0.get('Data', [])

    total_removed = 0
    total_kept = 0

    # Strip InstancedMeshCatalog batches
    r, k = strip_catalog_batches(properties, 'InstancedMeshCatalog',
                                  PREFAB_MESH_STRIP_PATTERNS, imports)
    total_removed += r
    total_kept += k

    # Strip InstancedBreakableCatalog batches (nest core uses BearNest_Deco_PH)
    # Use same patterns — anything matching gets removed
    breakable_patterns = PREFAB_MESH_STRIP_PATTERNS + ['PlaceholderNestCore']
    r, k = strip_catalog_batches(properties, 'InstancedBreakableCatalog',
                                  breakable_patterns, imports)
    total_removed += r
    total_kept += k

    return json_data, total_removed, total_kept


# ---------------------------------------------------------------------------
# Main build
# ---------------------------------------------------------------------------

def main():
    log(f"=== BuildBearNestRemoval v{MOD_VERSION} ===\n")

    # -----------------------------------------------------------------------
    # Step 1: Pre-flight checks
    # -----------------------------------------------------------------------
    log("[1/8] Pre-flight checks...")

    errors = []
    for name, path in [
        ('Cooked Debris.uasset', DEBRIS_UASSET),
        ('Cooked Debris.uexp', DEBRIS_UEXP),
        ('Legacy PD_CPF_BearNest.uasset', LEGACY_PD),
        ('Legacy PD_CPF_BearNest.uexp', LEGACY_PD_EXP),
        ('retoc.exe', RETOC_EXE),
        ('UAssetGUI.exe', UASSETGUI_EXE),
    ]:
        if not path.exists():
            errors.append(f"  Missing {name} at: {path}")

    if errors:
        log("  ERRORS:")
        for e in errors:
            log(e)
        sys.exit(1)

    log(f"  Debris source: {DEBRIS_UASSET.stat().st_size} + {DEBRIS_UEXP.stat().st_size} bytes")
    log(f"  PrefabData source: {LEGACY_PD.stat().st_size} + {LEGACY_PD_EXP.stat().st_size} bytes")
    log(f"  Deco mesh replacements: {len(DECO_MESH_REPLACEMENTS)}")
    log(f"  Prefab strip patterns: {len(PREFAB_MESH_STRIP_PATTERNS)}")
    log("  All checks passed.\n")

    # -----------------------------------------------------------------------
    # Step 2: Clean work dirs
    # -----------------------------------------------------------------------
    log("[2/8] Cleaning work directories...")

    for d in [STAGING_DECO, STAGING_PD, OUTPUT_DIR, WORK_DIR]:
        rmtree_safe(d)
        d.mkdir(parents=True, exist_ok=True)

    log("  Done.\n")

    # -----------------------------------------------------------------------
    # Step 3: Build per-target Debris replacements with correct internal names
    # -----------------------------------------------------------------------
    log("[3/8] Building per-target Debris replacements...")

    # Load the Debris template JSON once
    debris_template_json = WORK_DIR / 'Debris_template.json'
    log("  Converting Debris template to JSON...")
    if not run_uassetgui_tojson(DEBRIS_UASSET, debris_template_json):
        log("  ERROR: Could not convert Debris.uasset to JSON template")
        sys.exit(1)
    with open(debris_template_json, 'r', encoding='utf-8') as f:
        debris_template = json.load(f)

    # Create a customised replacement for each target mesh
    replacement_work = WORK_DIR / 'replacements'
    replacement_work.mkdir(exist_ok=True)

    for mesh_name, subpath in DECO_MESH_REPLACEMENTS:
        result = create_replacement_mesh(debris_template, mesh_name, subpath, replacement_work)
        if result is None:
            log(f"  ERROR: Failed to create replacement for {mesh_name}")
            sys.exit(1)
        uasset_path, uexp_path = result

        # Stage under correct content path
        dest_dir = STAGING_DECO / 'Moria' / 'Content' / subpath
        dest_dir.mkdir(parents=True, exist_ok=True)
        shutil.copy2(uasset_path, dest_dir / f'{mesh_name}.uasset')
        shutil.copy2(uexp_path, dest_dir / f'{mesh_name}.uexp')
        log(f"  Staged: {subpath}/{mesh_name}")

    log()

    # -----------------------------------------------------------------------
    # Step 4: Modify PD_CPF_BearNest — strip deco batches
    # -----------------------------------------------------------------------
    log("[4/8] Modifying PD_CPF_BearNest prefab data...")

    # Copy original to work dir
    work_uasset = WORK_DIR / 'PD_CPF_BearNest.uasset'
    work_uexp = WORK_DIR / 'PD_CPF_BearNest.uexp'
    shutil.copy2(LEGACY_PD, work_uasset)
    shutil.copy2(LEGACY_PD_EXP, work_uexp)

    # tojson
    work_json = WORK_DIR / 'PD_CPF_BearNest.json'
    log("  Converting to JSON...")
    if not run_uassetgui_tojson(work_uasset, work_json):
        log("  ERROR: Could not convert PD_CPF_BearNest to JSON")
        sys.exit(1)

    # Load and strip batches
    with open(work_json, 'r', encoding='utf-8') as f:
        pd_data = json.load(f)

    pd_data, removed_count, kept_count = strip_prefab_deco_batches(pd_data)
    log(f"  Batches kept: {kept_count}, instances removed: {removed_count}")

    # Save modified JSON
    modified_json = WORK_DIR / 'PD_CPF_BearNest_modified.json'
    with open(modified_json, 'w', encoding='utf-8') as f:
        json.dump(pd_data, f, indent=2)

    # fromjson → modified uasset
    modified_uasset = WORK_DIR / 'PD_CPF_BearNest_out.uasset'
    log("  Converting back to uasset...")
    if not run_uassetgui_fromjson(modified_json, modified_uasset):
        log("  ERROR: Could not convert modified JSON back to uasset")
        sys.exit(1)

    modified_uexp = modified_uasset.with_suffix('.uexp')
    if not modified_uasset.exists() or not modified_uexp.exists():
        log("  ERROR: fromjson did not produce expected output files")
        sys.exit(1)

    log(f"  Modified: {modified_uasset.stat().st_size} + {modified_uexp.stat().st_size} bytes")

    # Stage modified PD under correct path (separate staging dir)
    pd_staging = STAGING_PD / 'Moria' / 'Content' / 'Tech' / 'Data' / 'Prefabs'
    pd_staging.mkdir(parents=True, exist_ok=True)
    shutil.copy2(modified_uasset, pd_staging / 'PD_CPF_BearNest.uasset')
    shutil.copy2(modified_uexp, pd_staging / 'PD_CPF_BearNest.uexp')
    log(f"  Staged: Tech/Data/Prefabs/PD_CPF_BearNest")
    log()

    # -----------------------------------------------------------------------
    # Step 5: Validate all staged assets
    # -----------------------------------------------------------------------
    log("[5/8] Validating staged assets with UAssetGUI...")

    validate_dir = WORK_DIR / 'validate'
    validate_dir.mkdir(exist_ok=True)

    all_valid = True

    # Validate deco replacements
    for mesh_name, subpath in DECO_MESH_REPLACEMENTS:
        uasset_path = STAGING_DECO / 'Moria' / 'Content' / subpath / f'{mesh_name}.uasset'
        json_path = validate_dir / f'{mesh_name}.json'
        log(f"  Validating {mesh_name}...")
        if not run_uassetgui_tojson(uasset_path, json_path):
            log(f"    FAIL: {mesh_name}")
            all_valid = False
        else:
            log(f"    OK")

    # Validate modified PD
    pd_path = pd_staging / 'PD_CPF_BearNest.uasset'
    pd_json = validate_dir / 'PD_CPF_BearNest_validate.json'
    log("  Validating PD_CPF_BearNest...")
    if not run_uassetgui_tojson(pd_path, pd_json):
        log("    FAIL: PD_CPF_BearNest")
        all_valid = False
    else:
        # Verify the batches were actually stripped
        with open(pd_json, 'r', encoding='utf-8') as f:
            vdata = json.load(f)
        exports = vdata.get('Exports', [])
        if exports:
            for prop in exports[0].get('Data', []):
                if prop.get('Name') == 'InstancedMeshCatalog':
                    for ce in prop.get('Value', []):
                        if ce.get('Name') == 'Batches':
                            remaining = len(ce.get('Value', []))
                            log(f"    OK: {remaining} batch(es) remaining in catalog")
                            break
                    break

    if not all_valid:
        log("\n  ERROR: Validation failed. Aborting.")
        sys.exit(1)

    log("  All assets validated.\n")

    # -----------------------------------------------------------------------
    # Step 6: Build IoStore paks (two separate paks to avoid cross-refs)
    # -----------------------------------------------------------------------
    log("[6/8] Building IoStore paks with retoc to-zen...")

    # Pak 1: Deco mesh replacements
    log("  --- Pak 1: Deco mesh replacements ---")
    if not run_retoc_tozen(STAGING_DECO, OUTPUT_DIR, PAK_NAME_DECO):
        log("  ERROR: retoc to-zen failed for deco pak. Aborting.")
        sys.exit(1)

    # Pak 2: Modified prefab data
    log("  --- Pak 2: Modified prefab data ---")
    if not run_retoc_tozen(STAGING_PD, OUTPUT_DIR, PAK_NAME_PD):
        log("  ERROR: retoc to-zen failed for prefab pak. Aborting.")
        sys.exit(1)

    all_pak_files = []
    for pak_name in [PAK_NAME_DECO, PAK_NAME_PD]:
        triplet = [
            OUTPUT_DIR / f'{pak_name}.pak',
            OUTPUT_DIR / f'{pak_name}.ucas',
            OUTPUT_DIR / f'{pak_name}.utoc',
        ]
        if not all(f.exists() for f in triplet):
            log(f"  ERROR: Missing files for {pak_name}!")
            sys.exit(1)
        for f in triplet:
            log(f"  {f.name}: {f.stat().st_size:,} bytes")
            all_pak_files.append(f)

    log()

    # -----------------------------------------------------------------------
    # Step 7: Validate IoStore paks
    # -----------------------------------------------------------------------
    log("[7/8] Validating IoStore paks...")

    for pak_name, expected_exports in [
        (PAK_NAME_DECO, len(DECO_MESH_REPLACEMENTS)),
        (PAK_NAME_PD, 1),
    ]:
        utoc_file = OUTPUT_DIR / f'{pak_name}.utoc'
        log(f"  --- {pak_name} ---")
        list_cmd = [str(RETOC_EXE), 'list', str(utoc_file)]
        list_result = subprocess.run(list_cmd, capture_output=True, text=True, timeout=60)

        if list_result.returncode != 0:
            log(f"  WARN: retoc list exit={list_result.returncode}")
        else:
            lines = [l for l in list_result.stdout.strip().split('\n') if l.strip()]
            for line in lines:
                log(f"    {line}")

            export_count = sum(1 for l in lines if 'ExportBundleData' in l)
            header_count = sum(1 for l in lines if 'ContainerHeader' in l)
            log(f"  ExportBundleData: {export_count} (expected {expected_exports})")

            if export_count == expected_exports and header_count == 1:
                log(f"  OK")
            else:
                log(f"  WARNING: Unexpected entry count")

    log()

    # -----------------------------------------------------------------------
    # Step 8: Zip for distribution
    # -----------------------------------------------------------------------
    log("[8/8] Creating distribution zip...")

    zip_name = f'BearNestRemoval_v{MOD_VERSION}.zip'
    zip_path = DOWNLOADS_DIR / zip_name

    with zipfile.ZipFile(zip_path, 'w', zipfile.ZIP_DEFLATED) as zf:
        for f in all_pak_files:
            zf.write(f, f.name)
            log(f"  Added: {f.name}")

    log(f"\n  Output: {zip_path} ({zip_path.stat().st_size:,} bytes)")

    # -----------------------------------------------------------------------
    # Summary
    # -----------------------------------------------------------------------
    log(f"\n{'='*60}")
    log(f"  BearNestRemoval v{MOD_VERSION} -- BUILD SUCCESSFUL")
    log(f"  Deco meshes replaced: {len(DECO_MESH_REPLACEMENTS)}")
    log(f"  Prefab instances stripped: {removed_count}")
    log(f"  Paks: {PAK_NAME_DECO} + {PAK_NAME_PD}")
    log(f"  Zip: {zip_path}")
    log(f"  Install: Extract all 6 files to game Paks folder")
    log(f"{'='*60}")


if __name__ == '__main__':
    main()
