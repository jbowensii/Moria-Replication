"""
Chapter-2 sandbox 3-zone plan:

  Active zones (all priority 130, all Live, all on Z=12, X=10, Y-stacked):
    Sandbox_Small_Suburban_C       Pos (10, 10, 12)  Size (4, 4, 1)   Y=10..14
    Sandbox_Small_ElvenQuarter_B   Pos (10, 14, 12)  Size (6, 6, 1)   Y=14..20
    Sandbox_ElvenQuarter           Pos (10, 20, 12)  Size (6, 6, 1)   Y=20..26  (RENAMED from Sandbox.ElvenQuarter)

  Disabled zones (still in DataTable but EnabledState=Disabled):
    Sandbox_Small_Suburban_D
    Sandbox_Small_ElvenQuarter_C

Plus rename Sandbox.ElvenQuarter -> Sandbox_ElvenQuarter (underscore).
"""
import copy
import json
from pathlib import Path

HERE = Path(__file__).parent
ZN_PATH = HERE / 'DT_Moria_Zones.json'

OLD = 'Sandbox.ElvenQuarter'
NEW = 'Sandbox_ElvenQuarter'


def find_prop(row_value, name):
    for p in row_value or []:
        if isinstance(p, dict) and p.get('Name') == name:
            return p
    return None


def set_enum(prop, new_val):
    cur = prop.get('Value', '')
    if isinstance(cur, str) and '::' in cur:
        prefix = cur.split('::', 1)[0]
        prop['Value'] = f'{prefix}::{new_val}'
    else:
        prop['Value'] = new_val


def set_intvec(prop, x, y, z):
    for it in prop.get('Value', []) or []:
        if isinstance(it, dict):
            v = it.get('Value')
            if isinstance(v, dict) and 'X' in v:
                v['X'] = int(x); v['Y'] = int(y); v['Z'] = int(z)
                return


# ---- 1. Load ----
zn = json.loads(ZN_PATH.read_text(encoding='utf-8'))
rows = zn['Exports'][0]['Table']['Data']
by_name = {r['Name']: r for r in rows}


# ---- 2. Rename the row ----
if OLD in by_name and NEW not in by_name:
    r = by_name.pop(OLD)
    r['Name'] = NEW
    by_name[NEW] = r
    print(f'Renamed row {OLD}  ->  {NEW}')
elif NEW in by_name:
    print(f'{NEW} already exists — no rename needed')

# Update NameMap: replace old string, ensure new string present
namemap = zn.get('NameMap', [])
for i, s in enumerate(namemap):
    if s == OLD:
        namemap[i] = NEW
        print(f'NameMap[{i}] renamed {OLD} -> {NEW}')
if NEW not in namemap:
    namemap.append(NEW)
    print(f'NameMap: added {NEW}')

# Also ensure DisplayName key is appropriate
# (Was "Zones.Names.sb_ElvenQuarter" — keep as-is)


# ---- 3. Layout: all three on X=10, Z=12, Y-stacked with no overlap ----
TARGETS = [
    ('Sandbox_Small_Suburban_C',     10, 10, 12,  4, 4, 1),
    ('Sandbox_Small_ElvenQuarter_B', 10, 14, 12,  6, 6, 1),
    ('Sandbox_ElvenQuarter',         10, 20, 12,  6, 6, 1),
]

for name, px, py, pz, sx, sy, sz in TARGETS:
    r = by_name.get(name)
    if r is None:
        print(f'  {name}: NOT FOUND')
        continue
    set_intvec(find_prop(r['Value'], 'Position'), px, py, pz)
    set_intvec(find_prop(r['Value'], 'TargetSize'), sx, sy, sz)
    print(f'  {name}: Pos ({px},{py},{pz})  Size ({sx},{sy},{sz})')


# ---- 4. All three at priority 130, all Live ----
for name in ['Sandbox_Small_Suburban_C',
             'Sandbox_Small_ElvenQuarter_B',
             'Sandbox_ElvenQuarter']:
    r = by_name.get(name)
    if r is None: continue
    gp = find_prop(r['Value'], 'GenerationPriority')
    if gp is not None:
        gp['Value'] = 130
    es = find_prop(r['Value'], 'EnabledState')
    if es is not None:
        set_enum(es, 'Live')
    print(f'  {name}: priority=130, EnabledState=Live')


# ---- 5. Disable the other 2 chapter-2 zones ----
for name in ['Sandbox_Small_Suburban_D', 'Sandbox_Small_ElvenQuarter_C']:
    r = by_name.get(name)
    if r is None:
        print(f'  {name}: NOT FOUND'); continue
    es = find_prop(r['Value'], 'EnabledState')
    if es is not None:
        set_enum(es, 'Disabled')
    print(f'  {name}: EnabledState=Disabled')


# ---- Save ----
zn['NameMap'] = namemap
ZN_PATH.write_text(json.dumps(zn, indent=2), encoding='utf-8')


# ---- Verify ----
print('\n=== Final chapter-2 state ===')
for r in rows:
    chap = ''
    for p in r.get('Value', []):
        if p.get('Name') == 'Chapter':
            for it in p.get('Value', []) or []:
                if isinstance(it, dict) and it.get('Name')=='RowName':
                    chap = str(it.get('Value',''))
    if chap != 'SandboxSmall-chapter-2':
        continue
    pos = (0,0,0); sz = (0,0,0)
    for p in r['Value']:
        if p.get('Name') == 'Position':
            for it in p.get('Value', []) or []:
                if isinstance(it, dict):
                    v = it.get('Value')
                    if isinstance(v, dict) and 'X' in v:
                        pos = (v['X'], v['Y'], v['Z'])
        elif p.get('Name') == 'TargetSize':
            for it in p.get('Value', []) or []:
                if isinstance(it, dict):
                    v = it.get('Value')
                    if isinstance(v, dict) and 'X' in v:
                        sz = (v['X'], v['Y'], v['Z'])
    gp = find_prop(r['Value'], 'GenerationPriority')
    es = find_prop(r['Value'], 'EnabledState')
    pri = gp.get('Value') if gp else 0
    enabled_val = ''
    if es:
        v = str(es.get('Value',''))
        enabled_val = v.split('::')[-1] if '::' in v else v
    print(f'  {r["Name"]:45s}  pri={pri:>4d}  {enabled_val:10s}  Pos={pos} Size={sz}')
