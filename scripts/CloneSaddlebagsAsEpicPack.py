#!/usr/bin/env python3
"""
CloneSaddlebagsAsEpicPack.py - v1.4.0 re-clone of BP_PorterGoatSaddlebags.

REPLACES the v1.1.0 saddlebag clone (which inherited from
BP_ContainerItem_Dwarf_BodyInventory). The new clone inherits from
BP_EpicPack_AdventurersPack_Large -- making the saddlebag a player-
equippable EpicPack (back slot), surfacing a multi-slot grid when worn.

The bell continues to use the v1.1.0 clone path (BP_ContainerItem_Dwarf_
BodyInventory parent) -- bells are trigger items, not equippable packs.
Run CloneBellAndSaddlebagsBPs.py FIRST to produce the bell; then run THIS
script to overwrite the saddlebag with an EpicPack-shaped clone.

Source:  /Game/Items/EpicPacks/BP_EpicPack_AdventurersPack_Large
Target:  /Game/Mods/PorterGoat/Items/BP_PorterGoatSaddlebags
Row:     PorterGoatSaddlebags (will live in DT_EpicPacks, not DT_ContainerItems)
"""

import json
import shutil
import subprocess
import sys
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parent.parent
W = PROJECT_ROOT / 'experiments' / 'portergoat' / 'v110_build'
UAG = PROJECT_ROOT / 'tools' / 'UAssetGUI' / 'UAssetGUI.exe'

SRC_UASSET = (PROJECT_ROOT / 'tools' / 'legacy-assets' / 'Moria' / 'Content'
              / 'Items' / 'EpicPacks' / 'BP_EpicPack_AdventurersPack_Large.uasset')
SRC_UEXP = SRC_UASSET.with_suffix('.uexp')

OLD_PKG_PATH   = '/Game/Items/EpicPacks/BP_EpicPack_AdventurersPack_Large'
OLD_CLASS_NAME = 'BP_EpicPack_AdventurersPack_Large_C'
OLD_CDO_NAME   = 'Default__BP_EpicPack_AdventurersPack_Large_C'
OLD_ROWNAME    = 'AdventurersPack_Large'

NEW_BASENAME   = 'BP_PorterGoatSaddlebags'
NEW_PKG_PATH   = f'/Game/Mods/PorterGoat/Items/{NEW_BASENAME}'
NEW_CLASS_NAME = f'{NEW_BASENAME}_C'
NEW_CDO_NAME   = f'Default__{NEW_BASENAME}_C'
NEW_ROWNAME    = 'PorterGoatSaddlebags'


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
    print(f'\n=== Cloning EpicPack -> {NEW_BASENAME} (RowName={NEW_ROWNAME!r}) ===')

    # Copy fresh template
    work_uasset = W / f'{NEW_BASENAME}_epicpack_template.uasset'
    work_uexp   = W / f'{NEW_BASENAME}_epicpack_template.uexp'
    shutil.copy2(SRC_UASSET, work_uasset)
    shutil.copy2(SRC_UEXP, work_uexp)

    # tojson
    template_json = W / f'{NEW_BASENAME}_epicpack_template.json'
    if not run([str(UAG), 'tojson', str(work_uasset), str(template_json), 'VER_UE4_27'],
               f'tojson {NEW_BASENAME}'):
        sys.exit(1)

    # Rewrite
    with open(template_json, 'r', encoding='utf-8') as f:
        d = json.load(f)

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
            print(f'  NameMap[{i}]: {entry!r} -> {rewrites[entry]!r}')
            nm[i] = rewrites[entry]
            rewrite_count += 1

    if d.get('FolderName') == OLD_PKG_PATH:
        d['FolderName'] = NEW_PKG_PATH
        print(f'  FolderName: {OLD_PKG_PATH!r} -> {NEW_PKG_PATH!r}')

    for exp in d.get('Exports', []):
        on = exp.get('ObjectName', '')
        if on == OLD_CLASS_NAME:
            exp['ObjectName'] = NEW_CLASS_NAME
        elif on == OLD_CDO_NAME:
            exp['ObjectName'] = NEW_CDO_NAME

    # CDO RowHandle.RowName retarget
    cdo = next((e for e in d['Exports']
                if e.get('ObjectName') == NEW_CDO_NAME), None)
    if cdo is None:
        print('  ERROR: CDO not found after rename')
        sys.exit(1)
    for prop in cdo.get('Data', []):
        if prop.get('Name') == 'RowHandle':
            for sub in prop.get('Value', []):
                if sub.get('Name') == 'RowName':
                    print(f'  CDO.RowHandle.RowName: {sub.get("Value")!r} -> {NEW_ROWNAME!r}')
                    sub['Value'] = NEW_ROWNAME

    # Save modified JSON
    out_json = W / f'{NEW_BASENAME}.json'
    with open(out_json, 'w', encoding='utf-8') as f:
        json.dump(d, f, indent=2)

    # fromjson -- overwrites the v1.1.0 ContainerItem-based clone at the same path
    out_uasset = W / f'{NEW_BASENAME}.uasset'
    if not run([str(UAG), 'fromjson', str(out_json), str(out_uasset), 'VER_UE4_27'],
               f'fromjson {NEW_BASENAME}'):
        sys.exit(1)
    out_uexp = out_uasset.with_suffix('.uexp')
    print(f'  Output: {out_uasset.stat().st_size} + {out_uexp.stat().st_size} bytes')

    # Round-trip validate
    validate_json = W / f'{NEW_BASENAME}_validate.json'
    if not run([str(UAG), 'tojson', str(out_uasset), str(validate_json), 'VER_UE4_27'],
               f'tojson validate {NEW_BASENAME}'):
        sys.exit(2)
    with open(validate_json, 'r', encoding='utf-8') as f:
        v = json.load(f)
    assert v.get('FolderName') == NEW_PKG_PATH, 'FolderName drift'
    assert NEW_CLASS_NAME in v.get('NameMap', []), 'Class name missing'
    assert NEW_ROWNAME in v.get('NameMap', []), 'Row name missing'
    cdo_v = next((e for e in v['Exports']
                  if e.get('ObjectName') == NEW_CDO_NAME), None)
    assert cdo_v is not None, 'CDO missing in validated output'
    rh = next((p for p in cdo_v['Data'] if p.get('Name') == 'RowHandle'), None)
    assert rh is not None, 'RowHandle missing'
    rn = next((s for s in rh['Value'] if s.get('Name') == 'RowName'), None)
    assert rn is not None and rn['Value'] == NEW_ROWNAME, 'RowName drift'
    print(f'  Round-trip OK')
    print()
    print(f'DONE. {NEW_BASENAME} is now an EpicPack-class BP at {NEW_PKG_PATH}')
    print(f'  {out_uasset}')
    print(f'  {out_uexp}')


if __name__ == '__main__':
    main()
