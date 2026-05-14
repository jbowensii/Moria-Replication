#!/usr/bin/env python3
"""
CloneBellAndSaddlebagsBPs.py - One-time authoring of two new BPs for the
v1.1.0 porter-goat-bell architecture:

  BP_PorterGoatBell_C       - trigger item (right-clicked by player; runtime
                              intercepts -> spawn/despawn goat)
  BP_PorterGoatSaddlebags_C - container item with 8x8 storage backing
                              (lives in player inventory; click suppressed
                              by runtime; opened via goat E-menu)

Both inherit from BP_ContainerItem_Dwarf_BodyInventory shape (the proven
clone-and-rename template from v1.2.x's BP_ContainerItem_Goat_BodyInventory).
Each rewrites NameMap/FolderName/exports/RowHandle.RowName to target a new
asset path under /Game/Mods/PorterGoat/Items/.

Outputs land in experiments/portergoat/v110_build/.  The build pipeline
(BuildPorterGoatBell_v1_1_0.py) stages both .uasset+.uexp pairs into the pak.
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
              / 'Items' / 'ContainerItems' / 'BP_ContainerItem_Dwarf_BodyInventory.uasset')
SRC_UEXP = SRC_UASSET.with_suffix('.uexp')

OLD_PKG_PATH = '/Game/Items/ContainerItems/BP_ContainerItem_Dwarf_BodyInventory'
OLD_CLASS_NAME = 'BP_ContainerItem_Dwarf_BodyInventory_C'
OLD_CDO_NAME = 'Default__BP_ContainerItem_Dwarf_BodyInventory_C'
OLD_ROWNAME = 'Dwarf.BodyInventory'


def run(cmd, label):
    r = subprocess.run(cmd, capture_output=True, text=True, timeout=60)
    if r.returncode != 0:
        print(f'  FAIL {label}: exit={r.returncode}\n{r.stderr[:600]}')
        return False
    return True


def clone_one(new_basename, new_rowname):
    """Produce a single cloned BP at the given basename + retargeted to the
    given RowName. Returns the output .uasset Path."""
    print(f'\n=== Cloning -> {new_basename} (RowHandle.RowName={new_rowname!r}) ===')

    new_pkg_path   = f'/Game/Mods/PorterGoat/Items/{new_basename}'
    new_class_name = f'{new_basename}_C'
    new_cdo_name   = f'Default__{new_basename}_C'

    # Copy fresh template
    work_uasset = W / f'{new_basename}_template.uasset'
    work_uexp   = W / f'{new_basename}_template.uexp'
    shutil.copy2(SRC_UASSET, work_uasset)
    shutil.copy2(SRC_UEXP, work_uexp)

    # tojson
    template_json = W / f'{new_basename}_template.json'
    if not run([str(UAG), 'tojson', str(work_uasset), str(template_json), 'VER_UE4_27'],
               f'tojson {new_basename}'):
        sys.exit(1)

    # Rewrite
    with open(template_json, 'r', encoding='utf-8') as f:
        d = json.load(f)

    nm = d.get('NameMap', [])
    rewrites = {
        OLD_PKG_PATH:   new_pkg_path,
        OLD_CLASS_NAME: new_class_name,
        OLD_CDO_NAME:   new_cdo_name,
        OLD_ROWNAME:    new_rowname,
    }
    rewrite_count = 0
    for i, entry in enumerate(nm):
        if entry in rewrites:
            print(f'  NameMap[{i}]: {entry!r} -> {rewrites[entry]!r}')
            nm[i] = rewrites[entry]
            rewrite_count += 1

    if d.get('FolderName') == OLD_PKG_PATH:
        d['FolderName'] = new_pkg_path
        print(f'  FolderName: {OLD_PKG_PATH!r} -> {new_pkg_path!r}')

    for exp in d.get('Exports', []):
        on = exp.get('ObjectName', '')
        if on == OLD_CLASS_NAME:
            exp['ObjectName'] = new_class_name
        elif on == OLD_CDO_NAME:
            exp['ObjectName'] = new_cdo_name

    # CDO RowHandle.RowName
    cdo = next((e for e in d['Exports']
                if e.get('ObjectName') == new_cdo_name), None)
    if cdo is None:
        print('  ERROR: CDO not found after rename')
        sys.exit(1)
    for prop in cdo.get('Data', []):
        if prop.get('Name') == 'RowHandle':
            for sub in prop.get('Value', []):
                if sub.get('Name') == 'RowName':
                    print(f'  CDO.RowHandle.RowName: {sub.get("Value")!r} -> {new_rowname!r}')
                    sub['Value'] = new_rowname

    # Save modified JSON
    out_json = W / f'{new_basename}.json'
    with open(out_json, 'w', encoding='utf-8') as f:
        json.dump(d, f, indent=2)

    # fromjson
    out_uasset = W / f'{new_basename}.uasset'
    if not run([str(UAG), 'fromjson', str(out_json), str(out_uasset), 'VER_UE4_27'],
               f'fromjson {new_basename}'):
        sys.exit(1)
    out_uexp = out_uasset.with_suffix('.uexp')
    print(f'  Output: {out_uasset.stat().st_size} + {out_uexp.stat().st_size} bytes')

    # Round-trip validate
    validate_json = W / f'{new_basename}_validate.json'
    if not run([str(UAG), 'tojson', str(out_uasset), str(validate_json), 'VER_UE4_27'],
               f'tojson validate {new_basename}'):
        sys.exit(2)
    with open(validate_json, 'r', encoding='utf-8') as f:
        v = json.load(f)
    assert v.get('FolderName') == new_pkg_path, f'FolderName drift for {new_basename}'
    assert new_class_name in v.get('NameMap', []), f'Class name missing for {new_basename}'
    assert new_rowname in v.get('NameMap', []), f'Row name missing for {new_basename}'
    cdo_v = next((e for e in v['Exports']
                  if e.get('ObjectName') == new_cdo_name), None)
    assert cdo_v is not None, f'CDO missing in validated output for {new_basename}'
    rh = next((p for p in cdo_v['Data'] if p.get('Name') == 'RowHandle'), None)
    assert rh is not None, f'RowHandle missing for {new_basename}'
    rn = next((s for s in rh['Value'] if s.get('Name') == 'RowName'), None)
    assert rn is not None and rn['Value'] == new_rowname, f'RowName drift for {new_basename}'
    print(f'  Round-trip OK: {new_basename}')
    return out_uasset


def main():
    if not SRC_UASSET.exists():
        print(f'ERROR: source missing: {SRC_UASSET}')
        sys.exit(1)

    W.mkdir(parents=True, exist_ok=True)

    bell_out = clone_one('BP_PorterGoatBell',       'PorterGoatBell')
    sad_out  = clone_one('BP_PorterGoatSaddlebags', 'PorterGoatSaddlebags')

    print()
    print('DONE. Cooked assets at:')
    print(f'  {bell_out}')
    print(f'  {sad_out}')


if __name__ == '__main__':
    main()
