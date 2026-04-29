import json
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

z = json.load(open('DT_Moria_Zones.json'))
ch = json.load(open('DT_Moria_Chapters.json'))
lm = json.load(open('DT_Moria_Landmarks.json'))
lc = json.load(open('DT_Moria_LayoutConnections.json'))

ss_chap_band = {}
for r in ch['Exports'][0]['Table']['Data']:
    if not r['Name'].startswith('SandboxSmall-chapter-'): continue
    if zstate(r) == 'Disabled': continue
    ss_chap_band[r['Name']] = (get(r,'MinZ'), get(r,'MaxZ'))

lm_pos = {}
lm_state = {}
for r in lm['Exports'][0]['Table']['Data']:
    bp = get_intvec(fp(r['Value'], 'BasePosition'))
    lm_pos[r['Name']] = bp
    lm_state[r['Name']] = zstate(r)

live_ss_zones = set()
disabled_ss_zones = set()
for r in z['Exports'][0]['Table']['Data']:
    if zoneset(r) != 'SandboxSmall': continue
    if zstate(r) == 'Disabled': disabled_ss_zones.add(r['Name'])
    else: live_ss_zones.add(r['Name'])

print('### Q1: Anything extending above Z=29? ###')
above29 = []
for r in z['Exports'][0]['Table']['Data']:
    if zoneset(r) != 'SandboxSmall' or zstate(r) == 'Disabled': continue
    pos = get_intvec(fp(r['Value'], 'Position'))
    sz = get_intvec(fp(r['Value'], 'TargetSize'))
    if None in pos or None in sz: continue
    px,py,pz = pos
    sx,sy,sz_ = sz
    extend = fp(r['Value'], 'bExtendFootprint')
    extend_v = bool(extend and extend.get('Value') is True)
    # stored Pos top
    if pz is not None and sz_ is not None and pos != (0,0,0):
        top = pz + sz_ - 1
        if top > 29:
            above29.append((r['Name'], 'stored', pz, sz_, top, extend_v))
    # if landmark-driven, check landmark Z
    pflp = fp(r['Value'], 'bPositionFromLandmarks')
    if pflp and pflp.get('Value') is True:
        lh = fp(r['Value'], 'LandmarkHandles')
        if lh:
            for e in (lh.get('Value') or []):
                if not isinstance(e, dict): continue
                inner = e.get('Value')
                if not isinstance(inner, list): continue
                lhprop = fp(inner, 'Landmark')
                if not lhprop: continue
                lv = lhprop.get('Value')
                if isinstance(lv, list):
                    for it in lv:
                        if isinstance(it, dict) and it.get('Name') == 'RowName':
                            ln = it.get('Value', '')
                            if ln and ln != 'None':
                                bp = lm_pos.get(ln, (None,None,None))
                                if bp[2] is not None:
                                    top = bp[2] + (sz_ or 1) - 1
                                    if top > 29:
                                        above29.append((r['Name'], 'landmark='+ln, bp[2], sz_, top, extend_v))

if above29:
    print('  HITS:')
    for n, src, p, s, top, ext in above29:
        flag = '  bExtendFootprint=TRUE' if ext else ''
        print('    ' + n + ': ' + src + ' Pos.Z=' + str(p) + ' Size.Z=' + str(s) + ' top=' + str(top) + flag)
else:
    print('  All Live zones top <= Z=29 (assuming Pos+Size only).')

# bExtendFootprint zones
print('\n  Zones with bExtendFootprint=TRUE (footprint may grow at runtime):')
for r in z['Exports'][0]['Table']['Data']:
    if zoneset(r) != 'SandboxSmall' or zstate(r) == 'Disabled': continue
    extend = fp(r['Value'], 'bExtendFootprint')
    if extend and extend.get('Value') is True:
        pos = get_intvec(fp(r['Value'], 'Position'))
        sz = get_intvec(fp(r['Value'], 'TargetSize'))
        print('    ' + r['Name'] + ' Pos=' + str(pos) + ' Size=' + str(sz))

print('\n### Q2: Cross-row dependency check ###')
problems = []
for r in z['Exports'][0]['Table']['Data']:
    if zoneset(r) != 'SandboxSmall' or zstate(r) == 'Disabled': continue
    name = r['Name']
    for fld in ('ParentZone', 'SlideToZone'):
        v = get(r, fld)
        if v and v != 'None':
            if v in disabled_ss_zones:
                problems.append((name, fld, v, 'TARGET DISABLED'))
    lh = fp(r['Value'], 'LandmarkHandles')
    if lh:
        for e in (lh.get('Value') or []):
            if not isinstance(e, dict): continue
            inner = e.get('Value')
            if not isinstance(inner, list): continue
            lhprop = fp(inner, 'Landmark')
            if not lhprop: continue
            lv = lhprop.get('Value')
            if isinstance(lv, list):
                for it in lv:
                    if isinstance(it, dict) and it.get('Name') == 'RowName':
                        ln = it.get('Value', '')
                        if ln and ln != 'None':
                            if lm_state.get(ln) == 'Disabled':
                                problems.append((name, 'Landmark', ln, 'TARGET DISABLED'))

if problems:
    print('  HITS:')
    for n, fld, v, why in problems:
        print('    ' + n + '.' + fld + ' -> ' + v + ' (' + why + ')')
else:
    print('  All Live zone cross-row refs resolve to Live targets.')

# LayoutConnections endpoint check
print('\n### LayoutConnections endpoints in Live zones? ###')
SS_RELEVANT = ('SandboxSmall', 'All')
issues_lc = []
for r in lc['Exports'][0]['Table']['Data']:
    if zstate(r) == 'Disabled': continue
    p = fp(r.get('Value', []), 'ZoneSet')
    zs_v = str(p.get('Value','')).split('::')[-1] if p else 'None'
    if zs_v not in SS_RELEVANT: continue
    for fld in ('OriginZone', 'DestinationZone'):
        v = get(r, fld)
        if v and v != 'None':
            if v in disabled_ss_zones:
                issues_lc.append((r['Name'], zs_v, fld, v))
print('  ' + str(len(issues_lc)) + ' connection endpoint refs to Disabled SS zones')
for x in issues_lc[:10]:
    print('    ' + str(x))
