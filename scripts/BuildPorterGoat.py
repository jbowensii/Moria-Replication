#!/usr/bin/env python3
"""
BuildPorterGoat.py - Build the PorterGoat mod pak.

Two paths combined into one tiny IoStore mod:

  Path A: Re-enable the Porter NPC role
    DT_NPCRoles -> row "Porter" -> EnabledState: Disabled -> Live
    The dev team built the porter goat system but shipped it Disabled.
    Flipping it makes the role assignable. (Required tag: Fauna.Goat,
    which BP_NpcGoat already carries.)

  Path B: Register BP_NpcGoat in the AI spawn vocabulary
    DT_Moria_AI_Population -> add row "NpcGoat" -> BP_NpcGoat_C
    DT_AICharacterSettings -> add row "NpcGoat" cloned from "Goat"
    Does NOT add a distribution row, so the wildlife director will
    not randomly spawn it. UE4SS keypress remains the only trigger.

Pipeline (same as CleanSweep):
  1. UAssetGUI tojson on three source DTs
  2. Edit JSON in-place: flip Porter, add NpcGoat row x2
  3. UAssetGUI fromjson back to .uasset/.uexp
  4. Validate round-trip with another tojson
  5. Stage under correct content paths
  6. retoc to-zen -> IoStore .pak/.utoc/.ucas
  7. Zip to ~/Downloads/PorterGoat_v{VERSION}.zip

Usage:
    python scripts/BuildPorterGoat.py
"""

import copy
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
# Config
# ---------------------------------------------------------------------------
SCRIPT_DIR = Path(__file__).resolve().parent
PROJECT_ROOT = SCRIPT_DIR.parent

EXPERIMENT_DIR = PROJECT_ROOT / 'experiments' / 'portergoat'
WORK_DIR = EXPERIMENT_DIR / 'work'
STAGING_DIR = EXPERIMENT_DIR / 'staging'
OUTPUT_DIR = EXPERIMENT_DIR / 'output'
DOWNLOADS_DIR = Path(os.path.expanduser('~/Downloads'))

LEGACY_ROOT = PROJECT_ROOT / 'tools' / 'legacy-assets' / 'Moria' / 'Content'

RETOC_EXE = PROJECT_ROOT / 'tools' / 'retoc' / 'bin' / 'retoc.exe'
UASSETGUI_EXE = PROJECT_ROOT / 'tools' / 'UAssetGUI' / 'UAssetGUI.exe'

UE_VERSION = 'VER_UE4_27'
RETOC_VERSION = 'UE4_27'

MOD_VERSION = '1.0.5'
PAK_NAME = 'PorterGoat_P'
NPCGOAT_CLASS_PATH = '/Game/Character/NpcGoat/BP_NpcGoat.BP_NpcGoat_C'
NPCGOAT_PACKAGE_PATH = '/Game/Character/NpcGoat/BP_NpcGoat'

# v1.0.2 — drops the brand-new BP_PorterGoatLoader asset entirely.
# Theory A (IoStore rejecting brand-new mod-pak paths) was confirmed at
# runtime: the loader package returned 0x0 from every load API. Override
# paths (DT_NPCRoles, etc.) work fine.
#
# Replacement: embed a hard UClass* reference inside DT_NPCRoles by
# adding a dummy "_PorterGoatLoader" row whose WorkBehavior field
# (which is hard ObjectPropertyData, not soft) points at BP_NpcGoat_C.
# When the modified DT_NPCRoles loads at boot, that import is resolved,
# pulling /Game/Character/NpcGoat/BP_NpcGoat into memory.
# Type validation against TSubclassOf<UMorBehaviorState> happens AFTER
# import resolution, so the load fires regardless of type mismatch.
# v1.0.3: row is Live (was Disabled in v1.0.2). Theory was that Disabled
# rows skip eager import resolution; runtime probe confirmed v1.0.2 didn't
# trigger BP_NpcGoat load. To keep the role un-assignable while Live, we
# set RequiredTags to an impossible tag no entity carries.
LOADER_ROW_NAME = '_PorterGoatLoader'
LOADER_IMPOSSIBLE_TAG = '_DoesNotExist_PorterGoatLoader'

# All FName strings introduced by the NpcGoat row addition.
# UAssetGUI serialises FSoftObjectPath.AssetName as an FName, so the full
# class path AND the package path must exist in NameMap before fromjson.
NPCGOAT_NAMEMAP_ADDITIONS = [
    'NpcGoat',
    NPCGOAT_PACKAGE_PATH,
    NPCGOAT_CLASS_PATH,
]

# (legacy-assets relpath, staging relpath, friendly name)
# NOTE: in v1.0.4 the list includes a Blueprint asset (BP_MoriaGameMode_MainMenu)
# alongside the three DTs. The build pipeline is generic — it just round-trips
# each entry through tojson/edit/fromjson per its registered editor function.
DTS = [
    ('Character/NpcDwarf/DT_NPCRoles',
     'Character/NpcDwarf/DT_NPCRoles',
     'DT_NPCRoles'),
    ('Character/AI/Spawning/DT_Moria_AI_Population',
     'Character/AI/Spawning/DT_Moria_AI_Population',
     'DT_Moria_AI_Population'),
    ('Character/AI/Spawning/DT_AICharacterSettings',
     'Character/AI/Spawning/DT_AICharacterSettings',
     'DT_AICharacterSettings'),
    ('Tech/GameModes/BP_MoriaGameMode_MainMenu',
     'Tech/GameModes/BP_MoriaGameMode_MainMenu',
     'BP_MoriaGameMode_MainMenu'),
    ('Character/NpcGoat/BP_NpcGoat',
     'Character/NpcGoat/BP_NpcGoat',
     'BP_NpcGoat'),
]

# Pack class for v1.0.5 DummyEquipment override
PACK_CLASS_PATH    = '/Game/Items/EpicPacks/BP_EpicPack_AdventurersPack_Large.BP_EpicPack_AdventurersPack_Large_C'
PACK_PACKAGE_PATH  = '/Game/Items/EpicPacks/BP_EpicPack_AdventurersPack_Large'
PACK_CLASS_NAME    = 'BP_EpicPack_AdventurersPack_Large_C'


# ---------------------------------------------------------------------------
# Helpers (lifted from BuildBearNestRemoval / BuildCleanSweep style)
# ---------------------------------------------------------------------------

def log(msg=''):
    print(msg)


def _rmtree_onerror(func, path, exc_info):
    os.chmod(path, stat.S_IWRITE)
    time.sleep(0.2)
    func(path)


def rmtree_safe(d):
    if not d.exists():
        return
    for _ in range(3):
        try:
            shutil.rmtree(d, onerror=_rmtree_onerror)
            return
        except PermissionError:
            time.sleep(1)
    log(f"  WARN: Could not fully remove {d}")


def run_uassetgui_tojson(uasset_path, json_output):
    cmd = [str(UASSETGUI_EXE), 'tojson', str(uasset_path), str(json_output), UE_VERSION]
    r = subprocess.run(cmd, capture_output=True, text=True, timeout=60)
    if r.returncode != 0:
        log(f"    FAIL tojson exit={r.returncode}\n    {r.stderr[:500]}")
        return False
    return True


def run_uassetgui_fromjson(json_path, uasset_output):
    cmd = [str(UASSETGUI_EXE), 'fromjson', str(json_path), str(uasset_output), UE_VERSION]
    r = subprocess.run(cmd, capture_output=True, text=True, timeout=60)
    if r.returncode != 0:
        log(f"    FAIL fromjson exit={r.returncode}\n    {r.stderr[:500]}")
        return False
    return True


def run_retoc_tozen(staging_dir, output_dir, pak_name):
    output_utoc = output_dir / f'{pak_name}.utoc'
    cmd = [str(RETOC_EXE), 'to-zen', '-v', '--version', RETOC_VERSION,
           str(staging_dir), str(output_utoc)]
    log(f"  retoc to-zen -> {pak_name}")
    r = subprocess.run(cmd, capture_output=True, text=True, timeout=300)
    if r.stdout:
        for ln in r.stdout.strip().split('\n')[-5:]:
            log(f"  [retoc] {ln}")
    if r.stderr:
        for ln in r.stderr.strip().split('\n')[-5:]:
            log(f"  [retoc] {ln}")
    return r.returncode == 0


# ---------------------------------------------------------------------------
# Edits
# ---------------------------------------------------------------------------

def ensure_namemap_entry(data, name):
    """Add `name` to NameMap if it isn't already present.

    UAssetGUI usually handles new FNames automatically on fromjson, but we add
    explicitly to be safe. NameMap is a simple list of strings.
    """
    nm = data.get('NameMap', [])
    if name not in nm:
        nm.append(name)
        data['NameMap'] = nm
        return True
    return False


def _add_npcgoat_imports_to_asset(data, label='asset'):
    """Append package + class imports for /Game/Character/NpcGoat/BP_NpcGoat
    and BP_NpcGoat_C.  Returns the negative import index of BP_NpcGoat_C
    (i.e. the value to assign to the WorkBehavior field).

    Idempotent: if the imports already exist, returns the existing index.
    """
    imports = data['Imports']

    # Check if BP_NpcGoat_C class import already exists
    for i, imp in enumerate(imports):
        if (imp.get('ObjectName') == 'BP_NpcGoat_C'
                and imp.get('ClassPackage') == '/Script/Engine'
                and imp.get('ClassName') == 'BlueprintGeneratedClass'):
            log(f"    NOTE: BP_NpcGoat_C class import already at -{i+1}")
            return -(i + 1)

    # Add package import
    pkg_import = {
        '$type': 'UAssetAPI.Import, UAssetAPI',
        'ObjectName': NPCGOAT_PACKAGE_PATH,
        'OuterIndex': 0,
        'ClassPackage': '/Script/CoreUObject',
        'ClassName': 'Package',
        'PackageName': None,
        'bImportOptional': False,
    }
    imports.append(pkg_import)
    pkg_idx_neg = -len(imports)
    log(f"    + Package import at {pkg_idx_neg}: {NPCGOAT_PACKAGE_PATH}")

    # Add class import
    cls_import = {
        '$type': 'UAssetAPI.Import, UAssetAPI',
        'ObjectName': 'BP_NpcGoat_C',
        'OuterIndex': pkg_idx_neg,
        'ClassPackage': '/Script/Engine',
        'ClassName': 'BlueprintGeneratedClass',
        'PackageName': None,
        'bImportOptional': False,
    }
    imports.append(cls_import)
    cls_idx_neg = -len(imports)
    log(f"    + Class   import at {cls_idx_neg}: BP_NpcGoat_C (outer={pkg_idx_neg})")

    return cls_idx_neg


def edit_npcroles(data):
    """Flip Porter row EnabledState Disabled -> Live.

    v1.0.4: removed the _PorterGoatLoader sentinel row. v1.0.3 confirmed DT
    row hard imports don't fire eagerly regardless of EnabledState. The
    force-load anchor moved to BP_MoriaGameMode_MainMenu.DefaultPawnClass.
    """
    rows = data['Exports'][0]['Table']['Data']
    porter = next((r for r in rows if r.get('Name') == 'Porter'), None)
    if porter is None:
        log("    ERROR: Porter row not found")
        return False
    for prop in porter['Value']:
        if prop.get('Name') == 'EnabledState':
            old = prop.get('Value')
            prop['Value'] = 'ERowEnabledState::Live'
            log(f"    Porter.EnabledState: {old} -> {prop['Value']}")
            return True
    log("    ERROR: Porter row has no EnabledState property")
    return False


def edit_mainmenu_gamemode(data):
    """Override BP_MoriaGameMode_MainMenu's DefaultPawnClass CDO default
    from BP_CharSelectionPawn_C to BP_NpcGoat_C.

    Both classes are Pawn-derived, so the engine's TSubclassOf<APawn> type
    check accepts the override at validation time. The hard import is
    resolved eagerly during CDO deserialization at title-screen load,
    pulling /Game/Character/NpcGoat/BP_NpcGoat permanently into memory.

    Side effect: at the character-selection screen, the menu pawn appears
    as a goat instead of a dwarf. Acceptable tradeoff for the load anchor.
    """
    # Find the CDO export
    cdo = None
    for exp in data.get('Exports', []):
        on = exp.get('ObjectName', '')
        if on.startswith('Default__BP_MoriaGameMode_MainMenu'):
            cdo = exp
            break
    if cdo is None:
        log("    ERROR: Default__BP_MoriaGameMode_MainMenu CDO not found")
        return False

    # Find DefaultPawnClass property in CDO Data
    target_prop = None
    for prop in cdo.get('Data', []):
        if prop.get('Name') == 'DefaultPawnClass':
            target_prop = prop
            break
    if target_prop is None:
        log("    ERROR: DefaultPawnClass property not found on CDO")
        log("    (it may inherit the parent's value without an override entry)")
        return False

    # Add NameMap entries (FName strings the new imports will reference)
    for n in [NPCGOAT_PACKAGE_PATH, 'BP_NpcGoat_C']:
        ensure_namemap_entry(data, n)

    # Add hard imports for BP_NpcGoat_C (returns negative class import idx)
    bpgoat_class_idx = _add_npcgoat_imports_to_asset(data, 'MainMenuGameMode')

    # Retarget DefaultPawnClass value
    old = target_prop.get('Value')
    target_prop['Value'] = bpgoat_class_idx
    log(f"    Default__BP_MoriaGameMode_MainMenu.DefaultPawnClass: {old} -> {bpgoat_class_idx} (BP_NpcGoat_C)")

    # Update CDO's CreateBeforeSerializationDependencies to include our class
    deps = cdo.get('CreateBeforeSerializationDependencies', [])
    if isinstance(old, int) and old < 0 and old in deps:
        deps[deps.index(old)] = bpgoat_class_idx
    elif bpgoat_class_idx not in deps:
        deps.append(bpgoat_class_idx)
    cdo['CreateBeforeSerializationDependencies'] = deps
    log(f"    CDO.CreateBeforeSerializationDependencies updated: {deps}")
    return True


def edit_ai_population(data):
    """Add new row 'NpcGoat' cloned from 'Goat', repointed at BP_NpcGoat_C."""
    rows = data['Exports'][0]['Table']['Data']

    # Guard against double-add
    if any(r.get('Name') == 'NpcGoat' for r in rows):
        log("    NOTE: NpcGoat row already present (idempotent skip)")
        return True

    template = next((r for r in rows if r.get('Name') == 'Goat'), None)
    if template is None:
        log("    ERROR: Template row 'Goat' not found")
        return False

    new_row = copy.deepcopy(template)
    new_row['Name'] = 'NpcGoat'
    # Re-point CharacterClass
    for prop in new_row['Value']:
        if prop.get('Name') == 'CharacterClass':
            prop['Value']['AssetPath']['AssetName'] = NPCGOAT_CLASS_PATH

    rows.append(new_row)
    for n in NPCGOAT_NAMEMAP_ADDITIONS:
        ensure_namemap_entry(data, n)
    log(f"    Added row 'NpcGoat' -> {NPCGOAT_CLASS_PATH}")
    log(f"    Population row count: {len(rows)}")
    return True


def edit_aicharsettings(data):
    """Add new row 'NpcGoat' cloned from 'Goat', repointed at BP_NpcGoat_C."""
    rows = data['Exports'][0]['Table']['Data']

    if any(r.get('Name') == 'NpcGoat' for r in rows):
        log("    NOTE: NpcGoat row already present (idempotent skip)")
        return True

    template = next((r for r in rows if r.get('Name') == 'Goat'), None)
    if template is None:
        log("    ERROR: Template row 'Goat' not found")
        return False

    new_row = copy.deepcopy(template)
    new_row['Name'] = 'NpcGoat'
    for prop in new_row['Value']:
        if prop.get('Name') == 'CharacterClass':
            prop['Value']['AssetPath']['AssetName'] = NPCGOAT_CLASS_PATH

    rows.append(new_row)
    for n in NPCGOAT_NAMEMAP_ADDITIONS:
        ensure_namemap_entry(data, n)
    log(f"    Added row 'NpcGoat' -> {NPCGOAT_CLASS_PATH}")
    log(f"    AICharacterSettings row count: {len(rows)}")
    return True


def edit_bp_npcgoat(data):
    """Override BP_NpcGoat's EquipComp.DummyEquipment CDO field to point at
    BP_EpicPack_AdventurersPack_Large_C.

    EquipComp (a MorEquipComponent) currently has zero overridden defaults
    on BP_NpcGoat — inherits all from C++. We add ONE property entry to
    its export Data, naming the field 'DummyEquipment' as ObjectPropertyData
    with value = import index of BP_EpicPack_AdventurersPack_Large_C.

    Hypothesis (per runtime side schema dump): MorEquipComponent reads
    DummyEquipment at component init and auto-attaches its visual mesh
    to the appropriate epic-pack socket on the owning character. If true,
    every spawned BP_NpcGoat shows the AdventurersPack visually with no
    runtime intervention — bypasses the FWeakObjectPtr corruption that
    hit when calling ServerEquipDummyItem mid-spawn-tick.
    """
    # Find the EquipComp export
    equipcomp_export = None
    for exp in data.get('Exports', []):
        if exp.get('ObjectName') == 'EquipComp':
            equipcomp_export = exp
            break
    if equipcomp_export is None:
        log("    ERROR: EquipComp export not found")
        return False

    # Idempotency check
    for prop in equipcomp_export.get('Data', []):
        if prop.get('Name') == 'DummyEquipment':
            log("    NOTE: DummyEquipment already set on EquipComp (idempotent skip)")
            return True

    # Add NameMap entries for the new strings we'll reference
    for n in ['DummyEquipment', PACK_PACKAGE_PATH, PACK_CLASS_NAME]:
        ensure_namemap_entry(data, n)

    # Add Imports for BP_EpicPack_AdventurersPack_Large package + class
    imports = data['Imports']

    # Check if pack class import already exists (defensive)
    pack_class_idx = None
    for i, imp in enumerate(imports):
        if (imp.get('ObjectName') == PACK_CLASS_NAME
                and imp.get('ClassPackage') == '/Script/Engine'
                and imp.get('ClassName') == 'BlueprintGeneratedClass'):
            pack_class_idx = -(i + 1)
            log(f"    NOTE: Pack class import already at {pack_class_idx}")
            break

    if pack_class_idx is None:
        pkg_import = {
            '$type': 'UAssetAPI.Import, UAssetAPI',
            'ObjectName': PACK_PACKAGE_PATH,
            'OuterIndex': 0,
            'ClassPackage': '/Script/CoreUObject',
            'ClassName': 'Package',
            'PackageName': None,
            'bImportOptional': False,
        }
        imports.append(pkg_import)
        pkg_idx = -len(imports)
        log(f"    + Package import at {pkg_idx}: {PACK_PACKAGE_PATH}")

        cls_import = {
            '$type': 'UAssetAPI.Import, UAssetAPI',
            'ObjectName': PACK_CLASS_NAME,
            'OuterIndex': pkg_idx,
            'ClassPackage': '/Script/Engine',
            'ClassName': 'BlueprintGeneratedClass',
            'PackageName': None,
            'bImportOptional': False,
        }
        imports.append(cls_import)
        pack_class_idx = -len(imports)
        log(f"    + Class   import at {pack_class_idx}: {PACK_CLASS_NAME} (outer={pkg_idx})")

    # Add the DummyEquipment property entry to EquipComp's Data list
    new_prop = {
        '$type': 'UAssetAPI.PropertyTypes.Objects.ObjectPropertyData, UAssetAPI',
        'Name': 'DummyEquipment',
        'ArrayIndex': 0,
        'IsZero': False,
        'PropertyTagFlags': 'None',
        'PropertyTagExtensions': 'NoExtension',
        'Value': pack_class_idx,
    }
    equipcomp_export.setdefault('Data', []).append(new_prop)
    log(f"    EquipComp.DummyEquipment = {pack_class_idx} ({PACK_CLASS_NAME})")

    # Update CreateBeforeSerializationDependencies on EquipComp
    deps = equipcomp_export.get('CreateBeforeSerializationDependencies', [])
    if pack_class_idx not in deps:
        deps.append(pack_class_idx)
    equipcomp_export['CreateBeforeSerializationDependencies'] = deps
    log(f"    EquipComp.CreateBeforeSerializationDependencies updated: {deps}")

    return True


EDIT_FUNCS = {
    'DT_NPCRoles': edit_npcroles,
    'DT_Moria_AI_Population': edit_ai_population,
    'DT_AICharacterSettings': edit_aicharsettings,
    'BP_MoriaGameMode_MainMenu': edit_mainmenu_gamemode,
    'BP_NpcGoat': edit_bp_npcgoat,
}


# ---------------------------------------------------------------------------
# Main build
# ---------------------------------------------------------------------------

def main():
    log(f"=== BuildPorterGoat v{MOD_VERSION} ===\n")

    # ----------------------------------------------------------------- 1
    log("[1/7] Pre-flight checks...")
    errors = []
    for tool_name, tool_path in [('retoc.exe', RETOC_EXE),
                                 ('UAssetGUI.exe', UASSETGUI_EXE)]:
        if not tool_path.exists():
            errors.append(f"  Missing {tool_name}: {tool_path}")
    for src_rel, _, name in DTS:
        src_uasset = LEGACY_ROOT / f'{src_rel}.uasset'
        src_uexp = LEGACY_ROOT / f'{src_rel}.uexp'
        if not src_uasset.exists():
            errors.append(f"  Missing {src_uasset}")
        if not src_uexp.exists():
            errors.append(f"  Missing {src_uexp}")
    if errors:
        for e in errors:
            log(e)
        sys.exit(1)
    log(f"  Sources: {len(DTS)} DataTables\n")

    # ----------------------------------------------------------------- 2
    log("[2/7] Cleaning work dirs...")
    for d in [WORK_DIR, STAGING_DIR, OUTPUT_DIR]:
        rmtree_safe(d)
        d.mkdir(parents=True, exist_ok=True)
    log("  Done.\n")

    # ----------------------------------------------------------------- 3
    log("[3/7] tojson + edit + fromjson...")
    edited_outputs = []  # (modified_uasset, modified_uexp, staging_relpath)

    for src_rel, dst_rel, name in DTS:
        log(f"  --- {name} ---")

        src_uasset = LEGACY_ROOT / f'{src_rel}.uasset'
        src_uexp = LEGACY_ROOT / f'{src_rel}.uexp'

        work_uasset = WORK_DIR / f'{name}.uasset'
        work_uexp = WORK_DIR / f'{name}.uexp'
        shutil.copy2(src_uasset, work_uasset)
        shutil.copy2(src_uexp, work_uexp)

        work_json = WORK_DIR / f'{name}.json'
        if not run_uassetgui_tojson(work_uasset, work_json):
            log(f"  ERROR: tojson failed for {name}"); sys.exit(1)

        with open(work_json, 'r', encoding='utf-8') as f:
            data = json.load(f)

        edit_fn = EDIT_FUNCS[name]
        if not edit_fn(data):
            log(f"  ERROR: edit failed for {name}"); sys.exit(1)

        modified_json = WORK_DIR / f'{name}_modified.json'
        with open(modified_json, 'w', encoding='utf-8') as f:
            json.dump(data, f, indent=2)

        out_uasset = WORK_DIR / f'{name}_out.uasset'
        if not run_uassetgui_fromjson(modified_json, out_uasset):
            log(f"  ERROR: fromjson failed for {name}"); sys.exit(1)

        out_uexp = out_uasset.with_suffix('.uexp')
        if not (out_uasset.exists() and out_uexp.exists()):
            log(f"  ERROR: fromjson missing output for {name}"); sys.exit(1)

        log(f"    Output: {out_uasset.stat().st_size} + {out_uexp.stat().st_size} bytes")
        edited_outputs.append((out_uasset, out_uexp, dst_rel, name))

    log()

    # ----------------------------------------------------------------- 4
    log("[4/7] Validating round-trip (tojson on the modified output)...")
    for out_uasset, _, _, name in edited_outputs:
        validate_json = WORK_DIR / f'{name}_validate.json'
        if not run_uassetgui_tojson(out_uasset, validate_json):
            log(f"  ERROR: round-trip validation failed for {name}"); sys.exit(1)
        log(f"  OK: {name}")
    log()

    # ----------------------------------------------------------------- 5
    log("[5/7] Staging modified uassets...")
    for out_uasset, out_uexp, dst_rel, name in edited_outputs:
        dst_dir = STAGING_DIR / 'Moria' / 'Content' / Path(dst_rel).parent
        dst_dir.mkdir(parents=True, exist_ok=True)
        final_uasset = dst_dir / f'{Path(dst_rel).name}.uasset'
        final_uexp = dst_dir / f'{Path(dst_rel).name}.uexp'
        shutil.copy2(out_uasset, final_uasset)
        shutil.copy2(out_uexp, final_uexp)
        log(f"  Staged: Moria/Content/{dst_rel}")
    # v1.0.2 ships only override paths — no brand-new assets.  The hard
    # UClass* reference to BP_NpcGoat_C is now embedded inside DT_NPCRoles
    # via the _PorterGoatLoader sentinel row.
    log()

    # ----------------------------------------------------------------- 6
    log("[6/7] Building IoStore pak with retoc to-zen...")
    if not run_retoc_tozen(STAGING_DIR, OUTPUT_DIR, PAK_NAME):
        log("  ERROR: retoc to-zen failed"); sys.exit(1)

    triplet = [
        OUTPUT_DIR / f'{PAK_NAME}.pak',
        OUTPUT_DIR / f'{PAK_NAME}.ucas',
        OUTPUT_DIR / f'{PAK_NAME}.utoc',
    ]
    for f in triplet:
        if not f.exists():
            log(f"  ERROR: missing {f.name}"); sys.exit(1)
        log(f"  {f.name}: {f.stat().st_size:,} bytes")

    # retoc list sanity check
    list_cmd = [str(RETOC_EXE), 'list', str(triplet[2])]
    r = subprocess.run(list_cmd, capture_output=True, text=True, timeout=60)
    if r.returncode == 0:
        lines = [l for l in r.stdout.strip().split('\n') if l.strip()]
        export_count = sum(1 for l in lines if 'ExportBundleData' in l)
        log(f"  ExportBundleData entries: {export_count} (expected 5)")
    log()

    # ----------------------------------------------------------------- 7
    log("[7/7] Creating distribution zip...")
    DOWNLOADS_DIR.mkdir(parents=True, exist_ok=True)
    zip_path = DOWNLOADS_DIR / f'PorterGoat_v{MOD_VERSION}.zip'
    with zipfile.ZipFile(zip_path, 'w', zipfile.ZIP_DEFLATED) as zf:
        for f in triplet:
            zf.write(f, f.name)
            log(f"  Added: {f.name}")
    log(f"\n  Output: {zip_path} ({zip_path.stat().st_size:,} bytes)")

    # ------------------------------------------------------------- summary
    log(f"\n{'='*60}")
    log(f"  PorterGoat v{MOD_VERSION} -- BUILD SUCCESSFUL")
    log(f"  Assets modified: 4")
    log(f"    - DT_NPCRoles: Porter Disabled -> Live")
    log(f"    - DT_Moria_AI_Population: +1 row 'NpcGoat'")
    log(f"    - DT_AICharacterSettings: +1 row 'NpcGoat'")
    log(f"    - BP_MoriaGameMode_MainMenu (override):")
    log(f"        DefaultPawnClass: BP_CharSelectionPawn_C -> BP_NpcGoat_C")
    log(f"        (eager-load anchor; visual: goat at character selection)")
    log(f"    - BP_NpcGoat (override):")
    log(f"        EquipComp.DummyEquipment = BP_EpicPack_AdventurersPack_Large_C")
    log(f"        (visible pack on spawn, no runtime equip call needed)")
    log(f"  Pak: {PAK_NAME}")
    log(f"  Zip: {zip_path}")
    log(f"  Install: extract zip to <game>/Moria/Content/Paks/~mods/")
    log(f"{'='*60}")


if __name__ == '__main__':
    main()
