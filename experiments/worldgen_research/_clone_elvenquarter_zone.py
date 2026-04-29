"""
Clone the campaign zone `ElvenQuarter` into a new sandbox zone `Sandbox.ElvenQuarter`.

Transformations applied to the clone:
  - ZoneSet        : Moria                        -> SandboxSmall
  - Chapter        : Moria-chapter-2              -> SandboxSmall-chapter-2
  - DisplayName    : Zones.Names.ElvenQuarter     -> Zones.Names.sb_ElvenQuarter
  - LandmarkHandles:
      Chapter2.ElvenQuarterPromenade (void source in sandbox)
      -> Sandbox.ElvenQuarterPromenade  +  Sandbox.ElvenQuarterEntrance
         (paired, no dangling campaign refs)

BubbleDeck / PassageDeck kept as DefaultBubbles / DefaultPassages (generic);
the user can retarget them to sandbox decks via the editor.
"""
import copy
import json
from pathlib import Path

HERE = Path(__file__).parent
ZN_PATH = HERE / 'DT_Moria_Zones.json'
SOURCE_NAME = 'ElvenQuarter'
TARGET_NAME = 'Sandbox.ElvenQuarter'


def set_enum(prop, new_val):
    cur = prop.get('Value', '')
    if isinstance(cur, str) and '::' in cur:
        prefix = cur.split('::', 1)[0]
        prop['Value'] = f'{prefix}::{new_val}'
    else:
        prop['Value'] = new_val


def set_rowname(prop, new_val):
    for it in prop.get('Value', []) or []:
        if isinstance(it, dict) and it.get('Name') == 'RowName':
            it['Value'] = new_val
            return


def main():
    data = json.loads(ZN_PATH.read_text(encoding='utf-8'))
    rows = data['Exports'][0]['Table']['Data']
    by_name = {r['Name']: r for r in rows}

    if SOURCE_NAME not in by_name:
        raise SystemExit(f'Source zone {SOURCE_NAME!r} not found')
    if TARGET_NAME in by_name:
        raise SystemExit(f'Target zone {TARGET_NAME!r} already exists')

    src = by_name[SOURCE_NAME]
    new_row = copy.deepcopy(src)
    new_row['Name'] = TARGET_NAME

    # Walk top-level properties and retarget
    for p in new_row['Value']:
        if not isinstance(p, dict):
            continue
        n = p.get('Name')
        if n == 'ZoneSet':
            set_enum(p, 'SandboxSmall')
        elif n == 'Chapter':
            set_rowname(p, 'SandboxSmall-chapter-2')
        elif n == 'DisplayName':
            p['Value'] = 'Zones.Names.sb_ElvenQuarter'
        elif n == 'LandmarkHandles':
            # Rebuild entries: swap the campaign Promenade for the sandbox pair.
            existing = p.get('Value', []) or []
            if not existing:
                continue
            # Use the first existing entry as a struct template
            template = copy.deepcopy(existing[0])

            def make_entry(lm_rowname, placement='Fixed', extended=False):
                e = copy.deepcopy(template)
                for sub in e.get('Value', []):
                    if not isinstance(sub, dict):
                        continue
                    sn = sub.get('Name')
                    if sn == 'Landmark':
                        set_rowname(sub, lm_rowname)
                    elif sn == 'Placement':
                        cur = sub.get('Value', '')
                        prefix = cur.split('::', 1)[0] if '::' in cur else 'EZoneBubblePlacement'
                        sub['Value'] = f'{prefix}::{placement}'
                    elif sn == 'bExtendedConnectivityLandmark':
                        sub['Value'] = bool(extended)
                return e

            p['Value'] = [
                make_entry('Sandbox.ElvenQuarterEntrance',  'Fixed', False),
                make_entry('Sandbox.ElvenQuarterPromenade', 'Fixed', False),
            ]
            p.pop('DummyStruct', None)

    rows.append(new_row)

    # NameMap patches — every new FName reference must be in the map
    namemap = data.get('NameMap', [])
    namemap_set = set(namemap)
    added = []

    def nm_add(s):
        if s and s not in namemap_set:
            namemap.append(s); namemap_set.add(s); added.append(s)

    nm_add(TARGET_NAME)
    nm_add('SandboxSmall-chapter-2')       # should already be there, but safe
    nm_add('Zones.Names.sb_ElvenQuarter')  # display-name string table key
    nm_add('Sandbox.ElvenQuarterEntrance')
    nm_add('Sandbox.ElvenQuarterPromenade')
    data['NameMap'] = namemap

    ZN_PATH.write_text(json.dumps(data, indent=2), encoding='utf-8')

    print(f'Cloned {SOURCE_NAME}  ->  {TARGET_NAME}')
    print(f'  ZoneSet:    SandboxSmall')
    print(f'  Chapter:    SandboxSmall-chapter-2')
    print(f'  Biome:      World.Biome.ElvenQuarter (inherited)')
    print(f'  Landmarks:  Sandbox.ElvenQuarterEntrance + Sandbox.ElvenQuarterPromenade')
    print(f'  Size / Position / Decks / Tuning: inherited from campaign clone')
    if added:
        print(f'  NameMap additions:')
        for s in added:
            print(f'    + {s}')
    print(f'  Total zones now: {len(rows)}')


if __name__ == '__main__':
    main()
