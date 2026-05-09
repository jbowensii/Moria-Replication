#!/usr/bin/env python3
"""
CloneGoatBodyInventoryBP.py - One-time authoring of BP_ContainerItem_Goat_BodyInventory.

The slot wrapper BP is a thin container — only 4 CDO fields and 5 internal
exports. We clone BP_ContainerItem_Dwarf_BodyInventory and rewrite seven
strings (NameMap, FolderName, Export ObjectNames, RowHandle.RowName) to
produce a new BP at the path:

    /Game/Mods/PorterGoat/Items/BP_ContainerItem_Goat_BodyInventory

Run once. Output lands in experiments/portergoat/v110_build/.
The main build script (BuildPorterGoat.py) stages the produced uasset+uexp
into the pak.

This is the same clone-and-rename pattern used for v1.0.4's BP_PorterGoatLoader
and v1.0.5's modified BP_NpcGoat — proven safe with UAssetGUI tojson/fromjson
round-trips on minimal BPs.
"""

import json
import shutil
import subprocess
import sys
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parent.parent
W = PROJECT_ROOT / 'experiments' / 'portergoat' / 'v110_build'
UAG = PROJECT_ROOT / 'tools' / 'UAssetGUI' / 'UAssetGUI.exe'

SRC_UASSET = PROJECT_ROOT / 'tools' / 'legacy-assets' / 'Moria' / 'Content' / 'Items' / 'ContainerItems' / 'BP_ContainerItem_Dwarf_BodyInventory.uasset'
SRC_UEXP   = SRC_UASSET.with_suffix('.uexp')

# String rewrites
OLD_PKG_PATH    = '/Game/Items/ContainerItems/BP_ContainerItem_Dwarf_BodyInventory'
NEW_PKG_PATH    = '/Game/Mods/PorterGoat/Items/BP_ContainerItem_Goat_BodyInventory'
OLD_CLASS_NAME  = 'BP_ContainerItem_Dwarf_BodyInventory_C'
NEW_CLASS_NAME  = 'BP_ContainerItem_Goat_BodyInventory_C'
OLD_CDO_NAME    = 'Default__BP_ContainerItem_Dwarf_BodyInventory_C'
NEW_CDO_NAME    = 'Default__BP_ContainerItem_Goat_BodyInventory_C'
OLD_ROWNAME     = 'Dwarf.BodyInventory'
NEW_ROWNAME     = 'Goat.BodyInventory'


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

    # Step 1 — copy source to working dir
    print('[1/5] Copying source...')
    work_uasset = W / 'BP_Dwarf_template.uasset'
    work_uexp   = W / 'BP_Dwarf_template.uexp'
    shutil.copy2(SRC_UASSET, work_uasset)
    shutil.copy2(SRC_UEXP, work_uexp)

    # Step 2 — tojson
    print('[2/5] tojson...')
    template_json = W / 'BP_Dwarf_template.json'
    if not run([str(UAG), 'tojson', str(work_uasset), str(template_json), 'VER_UE4_27'],
               'tojson template'):
        sys.exit(1)

    # Step 3 — load, rewrite, save
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
                    sub['Value'] = NEW_ROWNAME
                    print(f'  CDO.RowHandle.RowName: -> {NEW_ROWNAME!r}')

    # Save
    out_json = W / 'BP_ContainerItem_Goat_BodyInventory.json'
    with open(out_json, 'w', encoding='utf-8') as f:
        json.dump(d, f, indent=2)

    # Step 4 — fromjson
    print('[4/5] fromjson...')
    out_uasset = W / 'BP_ContainerItem_Goat_BodyInventory.uasset'
    if not run([str(UAG), 'fromjson', str(out_json), str(out_uasset), 'VER_UE4_27'],
               'fromjson goat'):
        sys.exit(1)
    out_uexp = out_uasset.with_suffix('.uexp')
    if not (out_uasset.exists() and out_uexp.exists()):
        print('ERROR: fromjson missing output')
        sys.exit(1)
    print(f'  Output: {out_uasset.stat().st_size} + {out_uexp.stat().st_size} bytes')

    # Step 5 — round-trip validate
    print('[5/5] Round-trip validate (tojson on output)...')
    validate_json = W / 'BP_ContainerItem_Goat_BodyInventory_validate.json'
    if not run([str(UAG), 'tojson', str(out_uasset), str(validate_json), 'VER_UE4_27'],
               'tojson validate'):
        print('ERROR: round-trip validation failed')
        sys.exit(2)

    # Confirm key fields persist
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
    print(f'DONE. Cooked goat-bodyinventory wrapper at:')
    print(f'  {out_uasset}')
    print(f'  {out_uexp}')


if __name__ == '__main__':
    main()
