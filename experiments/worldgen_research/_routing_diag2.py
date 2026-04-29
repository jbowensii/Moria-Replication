"""Endpoint-host audit for SandboxSmall LayoutConnections.

For every Live SS LayoutConnection, check whether each endpoint landmark
is hosted by a Live SS zone via LandmarkHandles. Report orphans —
the smoking-gun candidates for the GetZone() null-deref crash.
"""
import json, os, sys

ROOT = os.path.dirname(os.path.abspath(__file__))
os.chdir(ROOT)

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

# Index landmark rows
lm_index = {}  # name -> (zoneset, state)
for r in lrows:
    lm_index[r['Name']] = (zoneset(r), zstate(r) or 'Live')

# Build map landmark_name -> [(zone_name, zone_state, zone_zoneset, pos)]
hosted_by = {}
zone_info = {}  # zname -> dict
for r in zrows:
    zs = zoneset(r)
    st = zstate(r) or 'Live'
    pos = get_intvec(fp(r['Value'], 'Position'))
    zone_info[r['Name']] = {'zoneset': zs, 'state': st, 'pos': pos, 'chapter': get(r, 'Chapter')}
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
                            lname = it.get('Value','')
                            hosted_by.setdefault(lname, []).append(r['Name'])

# Audit Live SS LayoutConnections
print('=== Endpoint-host audit: Live SS LayoutConnections ===\n')
issues = []
ok_count = 0

for r in crows:
    zs = zoneset(r)
    st = zstate(r) or 'Live'
    if zs != 'SandboxSmall' or st == 'Disabled':
        continue
    name = r['Name']
    o_lm = get(r, 'OriginLandmark')
    d_lm = get(r, 'DestinationLandmark')

    row_issues = []
    for role, lm in (('Origin', o_lm), ('Destination', d_lm)):
        if not lm or lm == 'None':
            row_issues.append(f'{role}: NULL/empty landmark')
            continue
        if lm not in lm_index:
            row_issues.append(f'{role}={lm}: landmark row MISSING from DT_Moria_Landmarks')
            continue
        lm_zs, lm_state = lm_index[lm]
        if lm_state == 'Disabled':
            row_issues.append(f'{role}={lm}: landmark is DISABLED')
        hosts = hosted_by.get(lm, [])
        live_ss_hosts = [h for h in hosts if zone_info[h]['zoneset']=='SandboxSmall' and zone_info[h]['state']!='Disabled']
        live_other_hosts = [h for h in hosts if zone_info[h]['zoneset']!='SandboxSmall' and zone_info[h]['state']!='Disabled']
        disabled_hosts = [h for h in hosts if zone_info[h]['state']=='Disabled']
        if not live_ss_hosts:
            detail = f'{role}={lm}: NO Live SS host'
            if live_other_hosts:
                detail += f' (Live in other ZoneSet: {live_other_hosts[:3]})'
            if disabled_hosts:
                detail += f' (Disabled hosts: {disabled_hosts[:3]})'
            if not hosts:
                detail += ' (NOT in any zone LandmarkHandles)'
            row_issues.append(detail)
        else:
            # check sentinel positions
            for h in live_ss_hosts:
                pos = zone_info[h]['pos']
                if pos == (0,0,0) or pos == (None,None,None):
                    row_issues.append(f'{role}={lm}: host {h} has sentinel Position={pos}')

    if row_issues:
        issues.append((name, o_lm, d_lm, row_issues))
    else:
        ok_count += 1

print(f'Live SS LCs OK: {ok_count}')
print(f'Live SS LCs with issues: {len(issues)}\n')

print('=== Issues ===')
for name, o, d, ri in issues:
    print(f'[{name}]  Origin={o}  Dest={d}')
    for x in ri:
        print(f'    -> {x}')
    print()

# Persist for apply step
out = []
for name, o, d, ri in issues:
    # Mark cause-likely (no Live SS host) vs not (e.g. sentinel position only)
    fatal = any('NO Live SS host' in x or 'MISSING' in x or 'NULL/empty' in x or 'is DISABLED' in x for x in ri)
    out.append({'name': name, 'origin': o, 'dest': d, 'issues': ri, 'fatal': fatal})
json.dump(out, open('_routing_diag2_findings.json','w', encoding='utf-8'), indent=2)
print(f'\nFatal LCs (will be disabled): {sum(1 for x in out if x["fatal"])}')
print(f'Non-fatal warnings (sentinel pos): {sum(1 for x in out if not x["fatal"])}')
