"""Add 2 new stairs to bridge missing transitions in upper stack (ch1-ch7)."""
import json, copy
from pathlib import Path

HERE = Path(__file__).parent
ZP = HERE / 'DT_Moria_Zones.json'
LP = HERE / 'DT_Moria_Landmarks.json'
CP = HERE / 'DT_Moria_Chapters.json'

z = json.loads(ZP.read_text(encoding='utf-8'))
lm = json.loads(LP.read_text(encoding='utf-8'))
ch = json.loads(CP.read_text(encoding='utf-8'))


def fp(v, n):
    for p in v or []:
        if isinstance(p, dict) and p.get('Name') == n:
            return p
    return None


def set_rowname(prop, new):
    for it in prop.get('Value', []) or []:
        if isinstance(it, dict) and it.get('Name') == 'RowName':
            it['Value'] = new
            return


def setv(prop, x, y, zv):
    for it in (prop.get('Value') or []):
        if isinstance(it, dict):
            v = it.get('Value')
            if isinstance(v, dict) and 'X' in v:
                v['X'] = int(x); v['Y'] = int(y); v['Z'] = int(zv)
                return


def chap_minz(name):
    for r in ch['Exports'][0]['Table']['Data']:
        if r['Name'] == name:
            mz = fp(r['Value'], 'MinZ')
            return mz.get('Value') if mz else None
    return None


ch3_minz = chap_minz('SandboxSmall-chapter-3')
ch6_minz = chap_minz('SandboxSmall-chapter-6')
print(f'ch3 MinZ={ch3_minz}, ch6 MinZ={ch6_minz}')

elevator_B = next(r for r in z['Exports'][0]['Table']['Data']
                  if r['Name'] == 'Sandbox_Small_Elevator_B')
firstStair = next(r for r in lm['Exports'][0]['Table']['Data']
                   if r['Name'] == 'Sandbox.FirstStair')

NEW = [
    ('Sandbox_Small_Elevator_G', 'SandboxSmall-chapter-3',
     'Sandbox.SixthStair',     ch3_minz, 0, 12),
    ('Sandbox_Small_Elevator_H', 'SandboxSmall-chapter-6',
     'Sandbox.SeventhStair',   ch6_minz, 0, 12),
]

zone_rows = z['Exports'][0]['Table']['Data']
zone_by = {r['Name']: r for r in zone_rows}
lm_rows = lm['Exports'][0]['Table']['Data']
lm_by = {r['Name']: r for r in lm_rows}

for zone_name, chap_name, lm_name, minz, x, y in NEW:
    if zone_name in zone_by:
        print(f'  {zone_name} already exists, skipping zone create')
    else:
        new_zone = copy.deepcopy(elevator_B)
        new_zone['Name'] = zone_name
        set_rowname(fp(new_zone['Value'], 'Chapter'), chap_name)
        setv(fp(new_zone['Value'], 'Position'), x, y, minz)
        # Clear and rewrite LandmarkHandles
        lh = fp(new_zone['Value'], 'LandmarkHandles')
        if lh and lh.get('Value'):
            tpl = copy.deepcopy(lh['Value'][0])
            for sub in (tpl.get('Value') or []):
                if not isinstance(sub, dict):
                    continue
                n = sub.get('Name')
                if n == 'Landmark':
                    set_rowname(sub, lm_name)
                elif n == 'Placement':
                    cur = sub.get('Value', '')
                    pref = cur.split('::', 1)[0] if '::' in cur else 'EZoneBubblePlacement'
                    sub['Value'] = f'{pref}::Fixed'
                elif n == 'bExtendedConnectivityLandmark':
                    sub['Value'] = True
            lh['Value'] = [tpl]
            lh.pop('DummyStruct', None)
        zone_rows.append(new_zone)
        zone_by[zone_name] = new_zone
        print(f'  Created zone {zone_name}: chapter={chap_name}, Pos=({x},{y},{minz}), Size=(6,6,4)')

    if lm_name in lm_by:
        print(f'  Landmark {lm_name} already exists, skipping')
    else:
        new_lm = copy.deepcopy(firstStair)
        new_lm['Name'] = lm_name
        dp = fp(new_lm['Value'], 'DisplayName')
        if dp:
            dp['Value'] = f'Landmarks.{lm_name}'
        gc = fp(new_lm['Value'], 'GuaranteedConnections')
        if gc and gc.get('Value'):
            if 'DummyStruct' not in gc:
                gc['DummyStruct'] = copy.deepcopy(gc['Value'][0])
            gc['Value'] = []
        lm_rows.append(new_lm)
        lm_by[lm_name] = new_lm
        print(f'  Created landmark {lm_name}  (clone of FirstStair, GC cleared, BB_Sandbox_Elevator_Urban)')

# NameMap patches
znm = z.get('NameMap', [])
for zn, _, ln, _, _, _ in NEW:
    for s in (zn, ln):
        if s not in znm:
            znm.append(s)
z['NameMap'] = znm

lnm = lm.get('NameMap', [])
for _, _, ln, _, _, _ in NEW:
    for s in (ln, f'Landmarks.{ln}'):
        if s not in lnm:
            lnm.append(s)
lm['NameMap'] = lnm

ZP.write_text(json.dumps(z, indent=2), encoding='utf-8')
LP.write_text(json.dumps(lm, indent=2), encoding='utf-8')

print()
print('=== Updated bridge coverage ===')
print('  Lv-1 -- Lv-2:  Sandbox.FirstStair (ch1)            existing')
print('  Lv-2 -- Lv-3:  Sandbox.SixthStair (ch3)            NEW')
print('  Lv-3 -- Lv-4:  Sandbox.SixthStair (ch3) + ThirdStair (ch4)')
print('  Lv-4 -- Lv-5:  Sandbox.ThirdStair (ch4)            existing')
print('  Lv-5 -- Lv-6:  Sandbox.SeventhStair (ch6)          NEW')
print('  Lv-6 -- Lv-7:  Sandbox.SeventhStair (ch6)          NEW')
