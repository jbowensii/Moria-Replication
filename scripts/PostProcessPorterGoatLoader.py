#!/usr/bin/env python3
"""
PostProcessPorterGoatLoader.py - Retarget BP_PorterGoatLoader's hard class
reference from /Script/Engine.Pawn to /Game/Character/NpcGoat/BP_NpcGoat.BP_NpcGoat_C.

The cooked asset (authored in a blank UE4.27 scratch project) ships with
the variable LoadedNpcGoatClass defaulted to Pawn (engine built-in). That
hard reference is what makes the engine resolve the class at boot, but
Pawn is already always-loaded so it accomplishes nothing.

This script edits the cooked asset's import table to add a hard ref to
BP_NpcGoat_C, then repoints the CDO's LoadedNpcGoatClass value at it.
The MetaClass on the FClassProperty stays Pawn (BP_NpcGoat is a Pawn
subclass, so the constraint is satisfied).

Mechanics:
  1. UAssetGUI tojson on cooked BP_PorterGoatLoader.uasset
  2. Append 2 NameMap entries:
       /Game/Character/NpcGoat/BP_NpcGoat
       BP_NpcGoat_C
  3. Append 2 Imports:
       Package /Game/Character/NpcGoat/BP_NpcGoat (outer=0, Class=Package)
       Class BP_NpcGoat_C (outer=PackageImportIdx, Class=BlueprintGeneratedClass)
  4. Edit CDO export:
       Data[0].Value: -5 (Pawn) -> -<new BP class import idx>
       CreateBeforeSerializationDependencies: replace -5 with new idx
  5. UAssetGUI fromjson back
  6. Round-trip validate (tojson on output)

Output goes to experiments/portergoat/cooked/ as
BP_PorterGoatLoader_retargeted.uasset/.uexp.

The main BuildPorterGoat.py is then updated to stage these instead of
running this post-process inline.
"""

import json
import shutil
import subprocess
import sys
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parent.parent
COOKED_DIR = PROJECT_ROOT / 'experiments' / 'portergoat' / 'cooked'
UAG = PROJECT_ROOT / 'tools' / 'UAssetGUI' / 'UAssetGUI.exe'

SRC_UASSET = COOKED_DIR / 'BP_PorterGoatLoader.uasset'
SRC_UEXP   = COOKED_DIR / 'BP_PorterGoatLoader.uexp'
SRC_JSON   = COOKED_DIR / 'BP_PorterGoatLoader.json'

OUT_UASSET = COOKED_DIR / 'BP_PorterGoatLoader_retargeted.uasset'
OUT_UEXP   = COOKED_DIR / 'BP_PorterGoatLoader_retargeted.uexp'
EDITED_JSON = COOKED_DIR / 'BP_PorterGoatLoader_retargeted.json'
VALIDATE_JSON = COOKED_DIR / 'BP_PorterGoatLoader_retargeted_validate.json'

NPCGOAT_PACKAGE_NAME = '/Game/Character/NpcGoat/BP_NpcGoat'
NPCGOAT_CLASS_NAME = 'BP_NpcGoat_C'

PAWN_IMPORT_INDEX_NEG = -5  # Imports[4] (1-based negative)


def run_tojson(src_uasset, dst_json):
    cmd = [str(UAG), 'tojson', str(src_uasset), str(dst_json), 'VER_UE4_27']
    r = subprocess.run(cmd, capture_output=True, text=True, timeout=60)
    if r.returncode != 0:
        print(f'tojson FAILED: {r.stderr[:600]}')
        return False
    return True


def run_fromjson(src_json, dst_uasset):
    cmd = [str(UAG), 'fromjson', str(src_json), str(dst_uasset), 'VER_UE4_27']
    r = subprocess.run(cmd, capture_output=True, text=True, timeout=60)
    if r.returncode != 0:
        print(f'fromjson FAILED: {r.stderr[:600]}')
        return False
    return True


def main():
    if not SRC_UASSET.exists():
        print(f'ERROR: missing {SRC_UASSET}')
        sys.exit(1)

    # Step 1: tojson (already done in our recon, but redo to be safe)
    print('[1/6] Converting cooked uasset to JSON...')
    if not run_tojson(SRC_UASSET, SRC_JSON):
        sys.exit(1)

    with open(SRC_JSON, 'r', encoding='utf-8') as f:
        data = json.load(f)

    print(f'  NameMap entries before: {len(data["NameMap"])}')
    print(f'  Imports before: {len(data["Imports"])}')

    # Step 2: NameMap additions
    print('\n[2/6] Adding NameMap entries...')
    if NPCGOAT_PACKAGE_NAME not in data['NameMap']:
        data['NameMap'].append(NPCGOAT_PACKAGE_NAME)
        print(f'  + {NPCGOAT_PACKAGE_NAME}')
    if NPCGOAT_CLASS_NAME not in data['NameMap']:
        data['NameMap'].append(NPCGOAT_CLASS_NAME)
        print(f'  + {NPCGOAT_CLASS_NAME}')

    # Step 3: Append imports
    # Existing: -1..-8 (Default__BlueprintGeneratedClass, Class, Object,
    #   BlueprintGeneratedClass, Pawn, Default__Object, /Script/CoreUObject,
    #   /Script/Engine)
    # Append: -9 (BP_NpcGoat package), -10 (BP_NpcGoat_C class)
    print('\n[3/6] Appending imports...')

    pkg_import = {
        '$type': 'UAssetAPI.Import, UAssetAPI',
        'ObjectName': NPCGOAT_PACKAGE_NAME,
        'OuterIndex': 0,
        'ClassPackage': '/Script/CoreUObject',
        'ClassName': 'Package',
        'PackageName': None,
        'bImportOptional': False,
    }
    data['Imports'].append(pkg_import)
    pkg_idx_neg = -len(data['Imports'])
    print(f'  + Package import at {pkg_idx_neg}: {NPCGOAT_PACKAGE_NAME}')

    cls_import = {
        '$type': 'UAssetAPI.Import, UAssetAPI',
        'ObjectName': NPCGOAT_CLASS_NAME,
        'OuterIndex': pkg_idx_neg,
        'ClassPackage': '/Script/Engine',
        'ClassName': 'BlueprintGeneratedClass',
        'PackageName': None,
        'bImportOptional': False,
    }
    data['Imports'].append(cls_import)
    cls_idx_neg = -len(data['Imports'])
    print(f'  + Class import at {cls_idx_neg}: {NPCGOAT_CLASS_NAME} (outer={pkg_idx_neg})')

    # Step 4: Edit CDO export's LoadedNpcGoatClass property value
    print('\n[4/6] Retargeting CDO LoadedNpcGoatClass value...')
    cdo = None
    for exp in data['Exports']:
        if exp.get('ObjectName') == 'Default__BP_PorterGoatLoader_C':
            cdo = exp
            break
    if cdo is None:
        print('  ERROR: CDO export not found')
        sys.exit(1)

    found_value = False
    for prop in cdo.get('Data', []):
        if prop.get('Name') == 'LoadedNpcGoatClass':
            old_val = prop['Value']
            prop['Value'] = cls_idx_neg
            print(f'  CDO.Data[LoadedNpcGoatClass]: {old_val} -> {cls_idx_neg}')
            found_value = True
            break
    if not found_value:
        print('  ERROR: LoadedNpcGoatClass property not found on CDO')
        sys.exit(1)

    # Update CDO's CreateBeforeSerializationDependencies (was [-5])
    deps = cdo.get('CreateBeforeSerializationDependencies', [])
    new_deps = [cls_idx_neg if d == PAWN_IMPORT_INDEX_NEG else d for d in deps]
    if cls_idx_neg not in new_deps:
        new_deps.append(cls_idx_neg)
    cdo['CreateBeforeSerializationDependencies'] = new_deps
    print(f'  CDO.CreateBeforeSerializationDependencies: {deps} -> {new_deps}')

    # Step 4b: keep counts in sync
    new_name_count = len(data['NameMap'])
    if 'Generations' in data and data['Generations']:
        for gen in data['Generations']:
            gen['NameCount'] = new_name_count
    data['NamesReferencedFromExportDataCount'] = new_name_count
    print(f'  Generations[*].NameCount = {new_name_count}')

    # Save modified JSON
    with open(EDITED_JSON, 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=2)

    # Step 5: fromjson
    print('\n[5/6] Converting back to uasset/uexp...')
    if not run_fromjson(EDITED_JSON, OUT_UASSET):
        sys.exit(1)
    if not (OUT_UASSET.exists() and OUT_UEXP.exists()):
        print('  ERROR: fromjson did not produce expected outputs')
        sys.exit(1)
    print(f'  Output: {OUT_UASSET.stat().st_size} + {OUT_UEXP.stat().st_size} bytes')

    # Step 6: round-trip validation
    print('\n[6/6] Round-trip validation (tojson on output)...')
    if not run_tojson(OUT_UASSET, VALIDATE_JSON):
        print('  WARN: round-trip tojson failed - asset may be malformed')
        sys.exit(2)

    with open(VALIDATE_JSON, 'r', encoding='utf-8') as f:
        v = json.load(f)
    # Confirm the retargeted value persisted
    for exp in v['Exports']:
        if exp.get('ObjectName') == 'Default__BP_PorterGoatLoader_C':
            for prop in exp.get('Data', []):
                if prop.get('Name') == 'LoadedNpcGoatClass':
                    print(f'  Verified: CDO.LoadedNpcGoatClass = {prop["Value"]} (expected {cls_idx_neg})')
                    if prop['Value'] != cls_idx_neg:
                        print('  ERROR: value did not persist round-trip')
                        sys.exit(2)
                    break
            break
    # Confirm imports persisted
    for imp in v['Imports']:
        if imp.get('ObjectName') == NPCGOAT_CLASS_NAME:
            print(f'  Verified import: {NPCGOAT_CLASS_NAME} (ClassPackage={imp["ClassPackage"]}, Outer={imp["OuterIndex"]})')
            break

    print('\nDONE.')
    print(f'Retargeted asset: {OUT_UASSET}')


if __name__ == '__main__':
    main()
