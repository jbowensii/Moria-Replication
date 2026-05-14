#!/usr/bin/env python3
"""
CloneBellOfTheGoatBP.py - One-time authoring of BP_BellOfTheGoat.

Clones BP_EpicPack_AdventurersPack_Small (the smallest vanilla adventurer
pack) into a new EpicPack-style item at the path:

    /Game/Mods/PorterGoat/Items/BP_BellOfTheGoat

Rewrites:
  NameMap entries (package path, class name, CDO name, RowHandle target)
  FolderName
  Export ObjectNames
  CDO RowHandle.RowName: 'AdventurersPack_Small' -> 'BellOfTheGoat'

The grid spec for the bell (8x8) is defined separately in a DT_Storage row
added by BuildPorterGoatBell.py.  This script just produces the BP asset.

Run once.  Output lands in experiments/portergoat/bell_build/.
"""

import json
import shutil
import subprocess
import sys
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parent.parent
W = PROJECT_ROOT / 'experiments' / 'portergoat' / 'bell_build'
UAG = PROJECT_ROOT / 'tools' / 'UAssetGUI' / 'UAssetGUI.exe'

SRC_UASSET = (PROJECT_ROOT / 'tools' / 'legacy-assets' / 'Moria' / 'Content'
              / 'Items' / 'EpicPacks' / 'BP_EpicPack_AdventurersPack_Small.uasset')
SRC_UEXP = SRC_UASSET.with_suffix('.uexp')

# String rewrites
OLD_PKG_PATH    = '/Game/Items/EpicPacks/BP_EpicPack_AdventurersPack_Small'
NEW_PKG_PATH    = '/Game/Mods/PorterGoat/Items/BP_BellOfTheGoat'
OLD_CLASS_NAME  = 'BP_EpicPack_AdventurersPack_Small_C'
NEW_CLASS_NAME  = 'BP_BellOfTheGoat_C'
OLD_CDO_NAME    = 'Default__BP_EpicPack_AdventurersPack_Small_C'
NEW_CDO_NAME    = 'Default__BP_BellOfTheGoat_C'
OLD_ROWNAME     = 'AdventurersPack_Small'
NEW_ROWNAME     = 'BellOfTheGoat'


def run(cmd, label):
    r = subprocess.run(cmd, capture_output=True, text=True, timeout=60)
    if r.returncode != 0:
        print(f'  FAIL {label}: exit={r.returncode}\n{r.stderr[:600]}')
        return False
    return True


def main():
    if not SRC_UASSET.exists():
        print(f'ERROR: source missing: {SRC_UASSET}')
        sys.exit(1)

    W.mkdir(parents=True, exist_ok=True)

    # Step 1 - copy source to working dir
    print('[1/5] Copying source...')
    work_uasset = W / 'BP_Pack_template.uasset'
    work_uexp   = W / 'BP_Pack_template.uexp'
    shutil.copy2(SRC_UASSET, work_uasset)
    shutil.copy2(SRC_UEXP, work_uexp)

    # Step 2 - tojson
    print('[2/5] tojson...')
    template_json = W / 'BP_Pack_template.json'
    if not run([str(UAG), 'tojson', str(work_uasset), str(template_json), 'VER_UE4_27'],
               'tojson template'):
        sys.exit(1)

    # Step 3 - load, rewrite, save
    print('[3/5] Rewriting strings (NameMap, FolderName, exports, RowHandle)...')
    with open(template_json, 'r', encoding='utf-8') as f:
        d = json.load(f)

    # NameMap rewrites
    nm = d.get('NameMap', [])
    rewrites = {
        OLD_PKG_PATH:   NEW_PKG_PATH,
        OLD_CLASS_NAME: NEW_CLASS_NAME,
        OLD_CDO_NAME:   NEW_CDO_NAME,
        OLD_ROWNAME:    NEW_ROWNAME,
    }
    rewrite_count = 0
    for i, entry in enumerate(nm):
        if entry in rewrites:
            print(f'    NameMap[{i}]: {entry!r} -> {rewrites[entry]!r}')
            nm[i] = rewrites[entry]
            rewrite_count += 1
    print(f'  NameMap rewrites: {rewrite_count}')

    # FolderName
    if d.get('FolderName') == OLD_PKG_PATH:
        d['FolderName'] = NEW_PKG_PATH
        print(f'  FolderName: {OLD_PKG_PATH!r} -> {NEW_PKG_PATH!r}')

    # Export ObjectNames
    for exp in d.get('Exports', []):
        on = exp.get('ObjectName', '')
        if on == OLD_CLASS_NAME:
            exp['ObjectName'] = NEW_CLASS_NAME
            print(f'  Export.ObjectName: {OLD_CLASS_NAME!r} -> {NEW_CLASS_NAME!r}')
        elif on == OLD_CDO_NAME:
            exp['ObjectName'] = NEW_CDO_NAME
            print(f'  Export.ObjectName: {OLD_CDO_NAME!r} -> {NEW_CDO_NAME!r}')

    # CDO Data: find the RowHandle struct, change RowName Value
    cdo = next((e for e in d['Exports']
                if e.get('ObjectName') == NEW_CDO_NAME), None)
    if cdo is None:
        print('ERROR: CDO not found after rename')
        sys.exit(1)
    for prop in cdo.get('Data', []):
        if prop.get('Name') == 'RowHandle':
            for sub in prop.get('Value', []):
                if sub.get('Name') == 'RowName':
                    print(f'  CDO.RowHandle.RowName: {sub.get("Value")!r} -> {NEW_ROWNAME!r}')
                    sub['Value'] = NEW_ROWNAME

    # Save
    out_json = W / 'BP_BellOfTheGoat.json'
    with open(out_json, 'w', encoding='utf-8') as f:
        json.dump(d, f, indent=2)

    # Step 4 - fromjson
    print('[4/5] fromjson...')
    out_uasset = W / 'BP_BellOfTheGoat.uasset'
    if not run([str(UAG), 'fromjson', str(out_json), str(out_uasset), 'VER_UE4_27'],
               'fromjson bell'):
        sys.exit(1)
    out_uexp = out_uasset.with_suffix('.uexp')
    if not (out_uasset.exists() and out_uexp.exists()):
        print('ERROR: fromjson missing output')
        sys.exit(1)
    print(f'  Output: {out_uasset.stat().st_size} + {out_uexp.stat().st_size} bytes')

    # Step 5 - round-trip validate
    print('[5/5] Round-trip validate (tojson on output)...')
    validate_json = W / 'BP_BellOfTheGoat_validate.json'
    if not run([str(UAG), 'tojson', str(out_uasset), str(validate_json), 'VER_UE4_27'],
               'tojson validate'):
        print('ERROR: round-trip validation failed')
        sys.exit(2)

    with open(validate_json, 'r', encoding='utf-8') as f:
        v = json.load(f)
    assert v.get('FolderName') == NEW_PKG_PATH, f'FolderName drift: {v.get("FolderName")}'
    assert NEW_PKG_PATH in v.get('NameMap', []), 'New package path missing from NameMap'
    assert NEW_CLASS_NAME in v.get('NameMap', []), 'New class name missing from NameMap'
    assert NEW_ROWNAME in v.get('NameMap', []), 'New row name missing from NameMap'
    cdo_v = next((e for e in v['Exports']
                  if e.get('ObjectName') == NEW_CDO_NAME), None)
    assert cdo_v is not None, 'CDO not found in validated output'
    rh = next((p for p in cdo_v['Data'] if p.get('Name') == 'RowHandle'), None)
    assert rh is not None, 'RowHandle missing'
    rn = next((s for s in rh['Value'] if s.get('Name') == 'RowName'), None)
    assert rn is not None and rn['Value'] == NEW_ROWNAME, f'RowName drift: {rn}'
    print('  All key fields persisted through round-trip.')

    print()
    print(f'DONE. Cooked Bell of the Goat asset at:')
    print(f'  {out_uasset}')
    print(f'  {out_uexp}')


if __name__ == '__main__':
    main()
