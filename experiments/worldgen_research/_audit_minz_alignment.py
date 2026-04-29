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

# Q1: 21st Hall details
print('### Q1: 21st Hall — every reference (zones + landmarks) ###\n')

# Find every landmark named *21stHall*
print('Landmarks containing "21stHall":')
for r in lm['Exports'][0]['Table']['Data']:
    if '21stHall' not in r['Name']: continue
    bp = get_intvec(fp(r['Value'], 'BasePosition'))
    bb = fp(r['Value'], 'BaseBubbleName')
    bb_v = bb.get('Value') if bb else None
    placement = fp(r['Value'], 'Placement')
    pl_v = str(placement.get('Value','')).split('::')[-1] if placement else None
    print('  ' + r['Name'] + ': BasePos=' + str(bp) + '  BubbleName=' + repr(bb_v) + '  Placement=' + str(pl_v))

# Find every zone whose LandmarkHandles points at *21stHall*
print('\nZones referencing a 21stHall landmark:')
for r in z['Exports'][0]['Table']['Data']:
    lh = fp(r['Value'], 'LandmarkHandles')
    if not lh: continue
    matched = []
    for e in (lh.get('Value') or []):
        if not isinstance(e, dict): continue
        inner = e.get('Value')
        if not isinstance(inner, list): continue
        lhprop = fp(inner, 'Landmark')
        if not lhprop: continue
        lv = lhprop.get('Value')
        if isinstance(lv, list):
            for it in lv:
                if isinstance(it, dict) and it.get('Name')=='RowName':
                    nm = it.get('Value','')
                    if '21stHall' in nm:
                        matched.append(nm)
    if matched:
        zs = zoneset(r)
        st = zstate(r)
        chap = get(r, 'Chapter')
        pos = get_intvec(fp(r['Value'], 'Position'))
        sz = get_intvec(fp(r['Value'], 'TargetSize'))
        print('  ' + r['Name'] + ' (' + str(zs) + ', ' + str(st) + ')')
        print('    Chapter=' + str(chap) + '  Pos=' + str(pos) + '  Size=' + str(sz))
        print('    Landmark refs: ' + str(matched))

# Q2: Live SS zones whose Pos.Z != chapter MinZ
print('\n### Q2: Live zones/landmarks NOT anchored at chapter MinZ ###\n')

# build chapter band (SS only — bridges have their own scheme)
ss_chap_band = {}
for r in ch['Exports'][0]['Table']['Data']:
    if not r['Name'].startswith('SandboxSmall-chapter-'): continue
    if zstate(r) == 'Disabled': continue
    ss_chap_band[r['Name']] = (get(r,'MinZ'), get(r,'MaxZ'))

print('--- Live SS ZONES (Pos.Z != chapter MinZ) ---')
print('  (Pos=(0,0,0) is the generator-placed sentinel, skipped)')
zones_off = []
for r in z['Exports'][0]['Table']['Data']:
    if zoneset(r) != 'SandboxSmall' or zstate(r) == 'Disabled': continue
    chap = get(r, 'Chapter')
    if chap not in ss_chap_band: continue   # skip bridge zones
    mn, mx = ss_chap_band[chap]
    pos = get_intvec(fp(r['Value'], 'Position'))
    if pos == (0, 0, 0): continue
    pz = pos[2]
    if pz != mn:
        in_band = '(in band)' if mn <= pz <= mx else '(OUT OF BAND)'
        zones_off.append((r['Name'], chap, mn, mx, pz, in_band))
print('  Total: ' + str(len(zones_off)))
for n, c, mn, mx, pz, ib in zones_off:
    print('    ' + n + '  chap=' + c + '  band=' + str(mn) + '..' + str(mx) + '  Pos.Z=' + str(pz) + '  ' + ib)

print('\n--- Landmarks attached to Live SS zones (BasePos.Z != host chapter MinZ) ---')
print('  (only landmarks attached to zones with bPositionFromLandmarks=true)')
lm_pos = {}
for r in lm['Exports'][0]['Table']['Data']:
    bp = get_intvec(fp(r['Value'], 'BasePosition'))
    lm_pos[r['Name']] = bp

lm_off = []
for r in z['Exports'][0]['Table']['Data']:
    if zoneset(r) != 'SandboxSmall' or zstate(r) == 'Disabled': continue
    chap = get(r, 'Chapter')
    if chap not in ss_chap_band: continue
    mn, mx = ss_chap_band[chap]
    pflp = fp(r['Value'], 'bPositionFromLandmarks')
    if not pflp or pflp.get('Value') is not True: continue
    lh = fp(r['Value'], 'LandmarkHandles')
    if not lh: continue
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
                    if not ln or ln == 'None': continue
                    bp = lm_pos.get(ln, (None,None,None))
                    if bp[2] is None: continue
                    if bp[2] != mn:
                        in_band = '(in band)' if mn <= bp[2] <= mx else '(OUT OF BAND)'
                        lm_off.append((r['Name'], chap, mn, mx, ln, bp[2], in_band))
print('  Total: ' + str(len(lm_off)))
for zn, c, mn, mx, ln, bz, ib in lm_off:
    print('    ' + zn + '  chap=' + c + '  band=' + str(mn) + '..' + str(mx) + '  landmark=' + ln + '  BasePos.Z=' + str(bz) + '  ' + ib)
