"""Broader audit — all Live LCs regardless of ZoneSet, plus inspect specific recent additions."""
import json, os
os.chdir(os.path.dirname(os.path.abspath(__file__)))

def fp(v, n):
    for p in v or []:
        if isinstance(p, dict) and p.get('Name') == n: return p
    return None

def get(r, k):
    p = fp(r['Value'], k)
    if not p: return None
    v = p.get('Value')
    if isinstance(v, list):
        for it in v:
            if isinstance(it, dict) and it.get('Name')=='RowName':
                return it.get('Value','')
    return v

def get_intvec(prop):
    v = prop.get('Value') if prop else None
    if isinstance(v, list) and v:
        inner = v[0]
        if isinstance(inner, dict) and isinstance(inner.get('Value'), dict):
            d = inner['Value']
            return (d.get('X'), d.get('Y'), d.get('Z'))
    return (None, None, None)

def zoneset(r):
    p = fp(r.get('Value', []), 'ZoneSet')
    return str(p.get('Value','')).split('::')[-1] if p else None

def zstate(r):
    p = fp(r.get('Value', []), 'EnabledState')
    return str(p.get('Value','')).split('::')[-1] if p else None

zones = json.load(open('DT_Moria_Zones.json', encoding='utf-8'))
lms = json.load(open('DT_Moria_Landmarks.json', encoding='utf-8'))
lcs = json.load(open('DT_Moria_LayoutConnections.json', encoding='utf-8'))

zrows = zones['Exports'][0]['Table']['Data']
lrows = lms['Exports'][0]['Table']['Data']
crows = lcs['Exports'][0]['Table']['Data']

lm_index = {r['Name']: (zoneset(r), zstate(r) or 'Live') for r in lrows}
zone_info = {}
hosted_by = {}
for r in zrows:
    zs = zoneset(r); st = zstate(r) or 'Live'
    pos = get_intvec(fp(r['Value'], 'Position'))
    zone_info[r['Name']] = {'zoneset': zs, 'state': st, 'pos': pos, 'chapter': get(r,'Chapter')}
    lh = fp(r['Value'], 'LandmarkHandles')
    if not lh: continue
    for e in (lh.get('Value') or []):
        if not isinstance(e, dict): continue
        for sub in e.get('Value', []):
            if isinstance(sub, dict) and sub.get('Name') == 'Landmark':
                lv = sub.get('Value')
                if isinstance(lv, list):
                    for it in lv:
                        if isinstance(it, dict) and it.get('Name')=='RowName':
                            hosted_by.setdefault(it.get('Value',''), []).append(r['Name'])

# Count Live LCs per ZoneSet
counts = {}
for r in crows:
    if (zstate(r) or 'Live') == 'Disabled': continue
    zs = zoneset(r) or '<none>'
    counts[zs] = counts.get(zs, 0) + 1
print('Live LC counts by ZoneSet:', counts)
print()

# All Live LCs with any endpoint-host problem
print('=== ALL Live LCs (any ZoneSet) — endpoint host audit ===\n')
issues = []
for r in crows:
    st = zstate(r) or 'Live'
    if st == 'Disabled': continue
    zs = zoneset(r)
    name = r['Name']
    o_lm = get(r, 'OriginLandmark'); d_lm = get(r, 'DestinationLandmark')

    ri = []
    for role, lm in (('Origin', o_lm), ('Destination', d_lm)):
        if not lm or lm == 'None':
            ri.append(f'{role}: NULL/empty landmark'); continue
        if lm not in lm_index:
            ri.append(f'{role}={lm}: landmark MISSING'); continue
        lm_zs, lm_state = lm_index[lm]
        if lm_state == 'Disabled':
            ri.append(f'{role}={lm}: landmark DISABLED')
        hosts = hosted_by.get(lm, [])
        live_in_lc_zs = [h for h in hosts if zone_info[h]['zoneset']==zs and zone_info[h]['state']!='Disabled']
        live_any = [h for h in hosts if zone_info[h]['state']!='Disabled']
        if not live_in_lc_zs:
            detail = f'{role}={lm}: no Live host in ZoneSet={zs}'
            other = [(h, zone_info[h]['zoneset']) for h in live_any]
            if other:
                detail += f'; Live elsewhere: {other[:3]}'
            else:
                detail += '; no Live host anywhere'
            ri.append(detail)

    if ri:
        issues.append((zs, name, o_lm, d_lm, ri))

print(f'Total problematic Live LCs: {len(issues)}\n')
for zs, name, o, d, ri in issues:
    print(f'[{zs}] {name}  Origin={o}  Dest={d}')
    for x in ri: print(f'    -> {x}')
    print()

# Inspect specific recent additions per the task
recent = ['Sandbox_FloorD2_Internal','Sandbox_FloorD5_Internal','Sandbox_FloorD6_Internal',
          'Sandbox_FloorLv1_Internal','Sandbox_FloorLv1bot_Internal','Sandbox_FloorLv5_Internal',
          'Sandbox_FloorLv6_Internal','Sandbox_ElvenEntranceToPromenade','Sandbox_PromenadeToMines']
print('=== Recent-addition inspection ===')
for r in crows:
    if r['Name'] not in recent: continue
    name = r['Name']; zs = zoneset(r); st = zstate(r) or 'Live'
    o = get(r,'OriginLandmark'); d = get(r,'DestinationLandmark')
    oz = get(r,'OriginZone'); dz = get(r,'DestinationZone')
    print(f'[{name}] state={st} zs={zs}')
    print(f'   OriginLandmark={o}  OriginZone={oz}')
    print(f'   DestLandmark={d}    DestZone={dz}')
    for role, lm in (('O',o),('D',d)):
        hosts = hosted_by.get(lm, [])
        states = [(h, zone_info[h]['state'], zone_info[h]['zoneset']) for h in hosts]
        print(f'   {role} hosts: {states}')
    print()

# Save findings
json.dump([{'zs':zs,'name':n,'origin':o,'dest':d,'issues':ri} for zs,n,o,d,ri in issues],
          open('_routing_diag2_findings.json','w', encoding='utf-8'), indent=2)
