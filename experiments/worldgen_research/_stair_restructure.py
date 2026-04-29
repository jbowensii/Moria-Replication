"""Stair restructure per user's odd/even rule + plan A."""
import json, copy

LM_PATH = 'DT_Moria_Landmarks.json'
Z_PATH  = 'DT_Moria_Zones.json'
URBAN = 'BB_Sandbox_Elevator_Urban'
CRYSTAL = 'BB_Sandbox_CrystalDescent'

def fp(v, n):
    for p in v or []:
        if isinstance(p, dict) and p.get('Name') == n:
            return p
    return None

lm = json.load(open(LM_PATH, encoding='utf-8'))
z = json.load(open(Z_PATH, encoding='utf-8'))

# 1) FourthStair & FifthStair: crystal -> urban
for lr in lm['Exports'][0]['Table']['Data']:
    if lr['Name'] in ('Sandbox.FourthStair', 'Sandbox.FifthStair'):
        bp = fp(lr['Value'], 'BaseBubbleName')
        if bp:
            old = bp.get('Value')
            bp['Value'] = URBAN
            print(f'  Landmark {lr["Name"]} BaseBubbleName: {old} -> {URBAN}')

# 2) Add 3 new landmarks
def find_lm(name):
    for lr in lm['Exports'][0]['Table']['Data']:
        if lr['Name'] == name:
            return lr
    return None

template_urban = find_lm('Sandbox.FirstStair')
template_crystal = find_lm('Sandbox.CrystalDescent')

NEW_LANDMARKS = [
    ('Sandbox.EighthStair', template_urban, URBAN),
    ('Sandbox.TenthStair', template_urban, URBAN),
    ('Sandbox.LowerDescent', template_crystal, CRYSTAL),
]
existing_lm_names = {r['Name'] for r in lm['Exports'][0]['Table']['Data']}
for new_name, tmpl, bub in NEW_LANDMARKS:
    if new_name in existing_lm_names:
        print(f'  Landmark {new_name} already exists - skip')
        continue
    new_lm = copy.deepcopy(tmpl)
    new_lm['Name'] = new_name
    bp = fp(new_lm['Value'], 'BaseBubbleName')
    if bp:
        bp['Value'] = bub
    bpos = fp(new_lm['Value'], 'BasePosition')
    if bpos:
        val = bpos.get('Value')
        if isinstance(val, list) and val and isinstance(val[0], dict) and isinstance(val[0].get('Value'), dict):
            val[0]['Value']['X'] = 0
            val[0]['Value']['Y'] = 0
            val[0]['Value']['Z'] = 0
    lm['Exports'][0]['Table']['Data'].append(new_lm)
    print(f'  +Landmark {new_name}  bubble={bub}')

# 3) Reassign LandmarkHandles
REASSIGN = {
    'Sandbox_Small_Elevator_C': ('Sandbox.SecondStair', 'Sandbox.FourthStair'),
    'Sandbox_Small_Elevator_E': ('Sandbox.FourthStair', 'Sandbox.TenthStair'),
    'Sandbox_Small_Elevator_F': ('Sandbox.FifthStair', 'Sandbox.CrystalDescent'),
    'Sandbox_Small_Elevator_G': ('Sandbox.SeventhStair', 'Sandbox.FifthStair'),
    'Sandbox_Small_Elevator_H': ('Sandbox.NinthStair', 'Sandbox.SeventhStair'),
}
for zr in z['Exports'][0]['Table']['Data']:
    if zr['Name'] not in REASSIGN:
        continue
    old_lm, new_lm_name = REASSIGN[zr['Name']]
    lh = fp(zr['Value'], 'LandmarkHandles')
    if not lh:
        continue
    for e in lh.get('Value') or []:
        for sub in e.get('Value') or []:
            if isinstance(sub, dict) and sub.get('Name') == 'Landmark':
                lv = sub.get('Value')
                if isinstance(lv, list):
                    for it in lv:
                        if isinstance(it, dict) and it.get('Name') == 'RowName' and it.get('Value') == old_lm:
                            it['Value'] = new_lm_name
                            print(f'  Zone {zr["Name"]}: {old_lm} -> {new_lm_name}')

# 4) Disable Elevator_I
for zr in z['Exports'][0]['Table']['Data']:
    if zr['Name'] == 'Sandbox_Small_Elevator_I':
        es = fp(zr['Value'], 'EnabledState')
        if es:
            old = es.get('Value')
            es['Value'] = 'ERowEnabledState::Disabled'
            print(f'  Zone Elevator_I: {old} -> Disabled')

# 5) Add 4 new zones
def find_zone(name):
    for zr in z['Exports'][0]['Table']['Data']:
        if zr['Name'] == name:
            return zr
    return None

template_zone = find_zone('Sandbox_Small_Elevator_B')

NEW_ZONES = [
    ('Sandbox_Small_Elevator_J', 'SandboxSmall-chapter-14', 'Sandbox.SecondStair'),
    ('Sandbox_Small_Elevator_K', 'SandboxSmall-chapter-12', 'Sandbox.SixthStair'),
    ('Sandbox_Small_Elevator_L', 'SandboxSmall-chapter-11', 'Sandbox.EighthStair'),
    ('Sandbox_Small_Elevator_M', 'SandboxSmall-chapter-8', 'Sandbox.LowerDescent'),
]

existing_zone_names = {zr['Name'] for zr in z['Exports'][0]['Table']['Data']}
for new_name, chap, lm_name in NEW_ZONES:
    if new_name in existing_zone_names:
        print(f'  Zone {new_name} already exists - skip')
        continue
    new_z = copy.deepcopy(template_zone)
    new_z['Name'] = new_name
    cp = fp(new_z['Value'], 'Chapter')
    if cp:
        val = cp.get('Value')
        if isinstance(val, list):
            for it in val:
                if isinstance(it, dict) and it.get('Name') == 'RowName':
                    it['Value'] = chap
    lh = fp(new_z['Value'], 'LandmarkHandles')
    if lh:
        for e in lh.get('Value') or []:
            for sub in e.get('Value') or []:
                if isinstance(sub, dict) and sub.get('Name') == 'Landmark':
                    lv = sub.get('Value')
                    if isinstance(lv, list):
                        for it in lv:
                            if isinstance(it, dict) and it.get('Name') == 'RowName':
                                it['Value'] = lm_name
            break
    z['Exports'][0]['Table']['Data'].append(new_z)
    print(f'  +Zone {new_name}  chap={chap}  landmark={lm_name}')

# 6) Sync NameMaps
def add_to_namemap(d, names):
    nm = d.get('NameMap', [])
    existing = set(nm)
    added = 0
    for n in names:
        if n not in existing:
            nm.append(n)
            existing.add(n)
            added += 1
    d['NameMap'] = nm
    if 'NamesReferencedFromExportDataCount' in d:
        d['NamesReferencedFromExportDataCount'] = len(nm)
    exp0 = d['Exports'][0]
    if 'Generations' in exp0 and exp0['Generations']:
        exp0['Generations'][0]['NameCount'] = len(nm)
    return added

lm_added = add_to_namemap(lm, ['Sandbox.EighthStair', 'Sandbox.TenthStair', 'Sandbox.LowerDescent'])
z_added = add_to_namemap(z, [
    'Sandbox_Small_Elevator_J', 'Sandbox_Small_Elevator_K',
    'Sandbox_Small_Elevator_L', 'Sandbox_Small_Elevator_M',
    'Sandbox.EighthStair', 'Sandbox.TenthStair', 'Sandbox.LowerDescent',
])
print(f'  Landmarks NameMap +{lm_added} ({len(lm.get("NameMap", []))} total)')
print(f'  Zones NameMap +{z_added} ({len(z.get("NameMap", []))} total)')

json.dump(lm, open(LM_PATH, 'w', encoding='utf-8'), indent=2)
json.dump(z, open(Z_PATH, 'w', encoding='utf-8'), indent=2)
print('Applied.')
