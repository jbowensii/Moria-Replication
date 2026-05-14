#!/usr/bin/env python3
"""
ClonePorterGoatStringTable.py - One-time authoring of ST_PorterGoatStrings.

Clones the vanilla `UI.uasset` StringTable, strips its 1000+ entries, and
replaces them with our 12 PorterGoat localization strings. Outputs:

    /Game/Mods/PorterGoat/Strings/ST_PorterGoatStrings

DT_ContainerItems, DT_RecipeBundles, and DT_Storage TextPropertyData fields
reference this StringTable via their TableId field, so player sees real
text instead of raw key strings.

Rewrites:
  NameMap entries (package path + ObjectName for the asset rename)
  TableNamespace -> "PorterGoat"
  Table.Value -> our 12 [key, text] pairs

Run once. Output lands in experiments/portergoat/v110_build/.
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
              / 'Tech' / 'Data' / 'StringTables' / 'UI.uasset')
SRC_UEXP = SRC_UASSET.with_suffix('.uexp')

OLD_PKG_PATH    = '/Game/Tech/Data/StringTables/UI'
NEW_PKG_PATH    = '/Game/Mods/PorterGoat/Strings/ST_PorterGoatStrings'
OLD_ASSET_NAME  = 'UI'
NEW_ASSET_NAME  = 'ST_PorterGoatStrings'
NEW_NAMESPACE   = 'PorterGoat'

# Our localization entries: (key, text)
ENTRIES = [
    # DT_ContainerItems display
    ('Container.PorterGoatBell.Name',
     'Bell of the Goat'),
    ('Container.PorterGoatBell.Description',
     'A bronze bell that summons your porter goat companion. Right-click to ring.'),
    ('Container.PorterGoatSaddlebags.Name',
     'Goat Saddlebags'),
    ('Container.PorterGoatSaddlebags.Description',
     'Sturdy saddlebags carried by your porter goat. Access through the goat\'s menu.'),
    # DT_RecipeBundles display (Shire merchant offers)
    ('Economy.Recipe.Bundle.PorterGoatBell.Name',
     'Recipe: Bell of the Goat'),
    ('Economy.Recipe.Bundle.PorterGoatBell.Description',
     'A merchant\'s scroll teaching how to forge a bronze bell that summons '
     'a porter goat companion.'),
    ('Economy.Recipe.Bundle.PorterGoatSaddlebags.Name',
     'Recipe: Goat Saddlebags'),
    ('Economy.Recipe.Bundle.PorterGoatSaddlebags.Description',
     'A merchant\'s scroll teaching how to stitch sturdy saddlebags for a '
     'porter goat.'),
    # DT_Storage display
    ('Storage.PorterGoatBell.Name',
     'Bell'),
    ('Storage.PorterGoatBell.Description',
     ''),
    ('Storage.PorterGoatSaddlebags.Name',
     'Saddlebags'),
    ('Storage.PorterGoatSaddlebags.Description',
     '8x8 cargo space carried by your porter goat.'),
    # v1.3.9: Porter role display name (fixes the "Citizen" header in the menu)
    ('Goat.Role.Porter',
     'Porter Goat'),
]


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

    print('[1/5] Copying source...')
    work_uasset = W / 'ST_template.uasset'
    work_uexp = W / 'ST_template.uexp'
    shutil.copy2(SRC_UASSET, work_uasset)
    shutil.copy2(SRC_UEXP, work_uexp)

    print('[2/5] tojson...')
    template_json = W / 'ST_template.json'
    if not run([str(UAG), 'tojson', str(work_uasset), str(template_json), 'VER_UE4_27'],
               'tojson template'):
        sys.exit(1)

    print('[3/5] Rewriting StringTable...')
    with open(template_json, 'r', encoding='utf-8') as f:
        d = json.load(f)

    # NameMap rewrites
    nm = d.get('NameMap', [])
    rewrites = {
        OLD_PKG_PATH:   NEW_PKG_PATH,
        OLD_ASSET_NAME: NEW_ASSET_NAME,
    }
    for i, entry in enumerate(nm):
        if entry in rewrites:
            print(f'  NameMap[{i}]: {entry!r} -> {rewrites[entry]!r}')
            nm[i] = rewrites[entry]
    # The TableNamespace ("UserInterface") was in NameMap as part of original
    # asset metadata; replace it with our namespace if present, else add.
    if 'UserInterface' in nm:
        nm[nm.index('UserInterface')] = NEW_NAMESPACE
    elif NEW_NAMESPACE not in nm:
        nm.append(NEW_NAMESPACE)

    # ObjectName + Table replacement on the StringTableExport
    exp = next((e for e in d.get('Exports', [])
                if e.get('$type', '').endswith('StringTableExport, UAssetAPI')),
               None)
    if exp is None:
        print('  ERROR: StringTableExport not found')
        sys.exit(1)
    exp['ObjectName'] = NEW_ASSET_NAME
    table = exp.get('Table', {})
    print(f'  TableNamespace: {table.get("TableNamespace")!r} -> {NEW_NAMESPACE!r}')
    table['TableNamespace'] = NEW_NAMESPACE
    print(f'  Entries: {len(table.get("Value", []))} (vanilla) -> {len(ENTRIES)} (ours)')
    table['Value'] = [[k, v] for (k, v) in ENTRIES]

    # Save modified JSON
    out_json = W / 'ST_PorterGoatStrings.json'
    with open(out_json, 'w', encoding='utf-8') as f:
        json.dump(d, f, indent=2)

    print('[4/5] fromjson...')
    out_uasset = W / 'ST_PorterGoatStrings.uasset'
    if not run([str(UAG), 'fromjson', str(out_json), str(out_uasset), 'VER_UE4_27'],
               'fromjson string-table'):
        sys.exit(1)
    out_uexp = out_uasset.with_suffix('.uexp')
    if not (out_uasset.exists() and out_uexp.exists()):
        print('ERROR: fromjson missing output')
        sys.exit(1)
    print(f'  Output: {out_uasset.stat().st_size} + {out_uexp.stat().st_size} bytes')

    print('[5/5] Round-trip validate...')
    validate_json = W / 'ST_PorterGoatStrings_validate.json'
    if not run([str(UAG), 'tojson', str(out_uasset), str(validate_json), 'VER_UE4_27'],
               'tojson validate'):
        sys.exit(2)

    with open(validate_json, 'r', encoding='utf-8') as f:
        v = json.load(f)
    v_exp = next((e for e in v.get('Exports', [])
                  if e.get('$type', '').endswith('StringTableExport, UAssetAPI')),
                 None)
    if v_exp is None:
        print('  ERROR: StringTableExport missing in validated output')
        sys.exit(2)
    v_table = v_exp.get('Table', {})
    if v_table.get('TableNamespace') != NEW_NAMESPACE:
        print(f'  ERROR: TableNamespace drift: {v_table.get("TableNamespace")}')
        sys.exit(2)
    v_entries = v_table.get('Value', [])
    if len(v_entries) != len(ENTRIES):
        print(f'  ERROR: entry count drift: {len(v_entries)} vs {len(ENTRIES)}')
        sys.exit(2)
    # Sanity-check first entry
    if v_entries[0][0] != ENTRIES[0][0] or v_entries[0][1] != ENTRIES[0][1]:
        print(f'  ERROR: entry content drift: {v_entries[0]} vs {ENTRIES[0]}')
        sys.exit(2)
    print(f'  Round-trip OK: {len(v_entries)} entries preserved')

    print()
    print('DONE. Cooked ST_PorterGoatStrings at:')
    print(f'  {out_uasset}')
    print(f'  {out_uexp}')


if __name__ == '__main__':
    main()
