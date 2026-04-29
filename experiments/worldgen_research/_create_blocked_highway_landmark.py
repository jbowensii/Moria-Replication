"""
Clone Chapter2.BlockedHighwayWest.Town -> Sandbox.BlockedHighwayWestTown.

New landmark:
  - Anchors the same bubble BB_Chapter2_BlockedHighwayWestTown
  - Placement = Fixed (matches source)
  - GuaranteedConnections cleared (campaign refs would dangle in sandbox)
"""
import copy
import json
from pathlib import Path

HERE = Path(__file__).parent
LM_PATH = HERE / 'DT_Moria_Landmarks.json'

SOURCE = 'Chapter2.BlockedHighwayWest.Town'
TARGET = 'Sandbox.BlockedHighwayWestTown'


def main():
    data = json.loads(LM_PATH.read_text(encoding='utf-8'))
    rows = data['Exports'][0]['Table']['Data']
    by_name = {r['Name']: r for r in rows}

    if SOURCE not in by_name:
        raise SystemExit(f'Source landmark {SOURCE!r} not found.')
    if TARGET in by_name:
        raise SystemExit(f'Target landmark {TARGET!r} already exists.')

    # Clone row and rewrite fields
    new_row = copy.deepcopy(by_name[SOURCE])
    new_row['Name'] = TARGET

    bubble = ''
    for p in new_row.get('Value', []):
        if not isinstance(p, dict):
            continue
        n = p.get('Name')
        if n == 'BaseBubbleName':
            bubble = str(p.get('Value', ''))
        elif n == 'GuaranteedConnections':
            existing = p.get('Value', []) or []
            if existing and 'DummyStruct' not in p:
                p['DummyStruct'] = copy.deepcopy(existing[0])
            p['Value'] = []
        elif n == 'DisplayName':
            p['Value'] = f'Landmarks.{TARGET}'

    rows.append(new_row)

    # NameMap patches
    namemap = data.get('NameMap', [])
    namemap_set = set(namemap)
    added = []

    def nm_add(s):
        if s and s not in namemap_set:
            namemap.append(s)
            namemap_set.add(s)
            added.append(s)

    nm_add(TARGET)
    nm_add(bubble)
    nm_add(f'World.Landmark.{TARGET}')
    nm_add(f'Landmarks.{TARGET}')
    data['NameMap'] = namemap

    LM_PATH.write_text(json.dumps(data, indent=2), encoding='utf-8')

    print(f'Cloned {SOURCE}  ->  {TARGET}')
    print(f'  bubble: {bubble}')
    print(f'  placement: Fixed (inherited)')
    print(f'  connections: [] (cleared)')
    print(f'  total landmarks now: {len(rows)}')
    if added:
        print(f'  NameMap additions:')
        for s in added:
            print(f'    + {s}')


if __name__ == '__main__':
    main()
