"""
X is vertical (level). Put 3 ElvenQuarter zones on X=5 (elven level) and
2 Suburban zones on X=10 (suburban level). Same chapter 2. No overlap.
Keep pristine sizes. Only Y and Z change (X held at the intended level).

Target layout:

  X=5  (elven level — 3 zones stacked by Y, all Z=12):
    ElvenQuarter_C        Pos (5,  6, 12)  Size (6, 6, 1)   Y=6..12
    Sandbox.ElvenQuarter  Pos (5, 12, 12)  Size (6, 6, 1)   Y=12..18    <-- Promenade center
    ElvenQuarter_B        Pos (5, 18, 12)  Size (6, 6, 1)   Y=18..24

  X=10  (suburban level — 2 zones stacked by Y, all Z=12):
    Suburban_C            Pos (10, 10, 12) Size (4, 4, 1)   Y=10..14   (pristine)
    Suburban_D            Pos (10, 14, 12) Size (4, 4, 1)   Y=14..18
"""
import copy
import json
from pathlib import Path

HERE = Path(__file__).parent
ZN_PATH = HERE / 'DT_Moria_Zones.json'


def find_prop(row_value, name):
    for p in row_value or []:
        if isinstance(p, dict) and p.get('Name') == name:
            return p
    return None


def set_intvec(prop, x, y, z):
    for it in prop.get('Value', []) or []:
        if isinstance(it, dict):
            v = it.get('Value')
            if isinstance(v, dict) and 'X' in v:
                v['X'] = int(x); v['Y'] = int(y); v['Z'] = int(z)
                return


TARGETS = [
    # (zone_name,                       X, Y, Z,  size_x, size_y, size_z)
    ('Sandbox_Small_ElvenQuarter_C',     5,  6, 12,   6, 6, 1),
    ('Sandbox.ElvenQuarter',             5, 12, 12,   6, 6, 1),
    ('Sandbox_Small_ElvenQuarter_B',     5, 18, 12,   6, 6, 1),
    ('Sandbox_Small_Suburban_C',        10, 10, 12,   4, 4, 1),  # pristine
    ('Sandbox_Small_Suburban_D',        10, 14, 12,   4, 4, 1),  # moved Y to avoid overlap
]


def main():
    data = json.loads(ZN_PATH.read_text(encoding='utf-8'))
    rows = data['Exports'][0]['Table']['Data']
    by_name = {r['Name']: r for r in rows}

    print(f'{"Zone":45s}  OldPos       OldSize      NewPos       NewSize')
    for name, x, y, z, sx, sy, sz in TARGETS:
        r = by_name.get(name)
        if r is None:
            print(f'  {name}: NOT FOUND'); continue
        pos_prop = find_prop(r['Value'], 'Position')
        sz_prop  = find_prop(r['Value'], 'TargetSize')

        def cur(prop):
            for it in prop.get('Value', []) or []:
                if isinstance(it, dict):
                    v = it.get('Value')
                    if isinstance(v, dict) and 'X' in v:
                        return (v['X'], v['Y'], v['Z'])
            return (0, 0, 0)

        old_pos = cur(pos_prop)
        old_sz = cur(sz_prop)

        set_intvec(pos_prop, x, y, z)
        set_intvec(sz_prop, sx, sy, sz)
        print(f'  {name:43s}  {str(old_pos):12s} {str(old_sz):12s} '
              f'({x},{y},{z})   ({sx},{sy},{sz})')

    ZN_PATH.write_text(json.dumps(data, indent=2), encoding='utf-8')
    print(f'\nSaved {ZN_PATH.name}')


if __name__ == '__main__':
    main()
