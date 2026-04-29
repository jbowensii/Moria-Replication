"""Deeper inspection of the 17 Live SS LCs — full property dump including ZoneRule, OriginZone/DestZone, bRequired, bExclusive, OriginPriority, etc., plus check whether endpoint landmarks have bExtendedConnectivityLandmark set on the host LandmarkHandle."""
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
def zoneset(r):
    p = fp(r.get('Value', []), 'ZoneSet'); return str(p.get('Value','')).split('::')[-1] if p else None
def zstate(r):
    p = fp(r.get('Value', []), 'EnabledState'); return str(p.get('Value','')).split('::')[-1] if p else None

zones = json.load(open('DT_Moria_Zones.json', encoding='utf-8'))
lcs = json.load(open('DT_Moria_LayoutConnections.json', encoding='utf-8'))

# Build host info per landmark with extended-connectivity flag
zone_info = {}
host_of = {}  # lm -> [(zone, bExtended)]
for r in zones['Exports'][0]['Table']['Data']:
    zs = zoneset(r); st = zstate(r) or 'Live'
    zone_info[r['Name']] = {'zoneset': zs, 'state': st}
    lh = fp(r['Value'], 'LandmarkHandles')
    if not lh: continue
    for e in (lh.get('Value') or []):
        if not isinstance(e, dict): continue
        inner = e.get('Value', [])
        ext_p = fp(inner, 'bExtendedConnectivityLandmark')
        ext = bool(ext_p.get('Value')) if ext_p else False
        for sub in inner:
            if isinstance(sub, dict) and sub.get('Name') == 'Landmark':
                lv = sub.get('Value')
                if isinstance(lv, list):
                    for it in lv:
                        if isinstance(it, dict) and it.get('Name')=='RowName':
                            host_of.setdefault(it.get('Value',''), []).append((r['Name'], ext))

# Original SS LC names (pre-fix)
orig_lcs = json.load(open('DT_Moria_LayoutConnections.original.json', encoding='utf-8'))
orig_names = set()
for r in orig_lcs['Exports'][0]['Table']['Data']:
    if zoneset(r) == 'SandboxSmall' and (zstate(r) or 'Live') != 'Disabled':
        orig_names.add(r['Name'])

# Inspect all 17 Live SS LCs
print('=== Live SS LCs full inspection ===\n')
for r in lcs['Exports'][0]['Table']['Data']:
    if zoneset(r) != 'SandboxSmall' or (zstate(r) or 'Live') == 'Disabled': continue
    name = r['Name']
    new_marker = '[NEW]' if name not in orig_names else '[orig]'
    print(f'{new_marker} {name}')
    for k in ['OriginLandmark','DestinationLandmark','OriginZone','DestinationZone',
              'ZoneRule','bRequired','bExclusive','bAvoidLoops','OriginPriority','DestinationPriority','bRouteInternal','bAllowAcrossDifferentChapter']:
        p = fp(r['Value'], k)
        if p is not None:
            v = get(r, k) if k in ('OriginLandmark','DestinationLandmark','OriginZone','DestinationZone') else p.get('Value')
            print(f'   {k} = {v}')
    # Check ext flag for both endpoints
    for role in ('OriginLandmark','DestinationLandmark'):
        lm = get(r, role)
        if lm and lm in host_of:
            hosts = host_of[lm]
            print(f'   {role} hosts (zone, bExt): {hosts}')
    print()
