"""Deep audit of post-shift state — every cross-reference, every Z value,
every alignment between zone/landmark/connection data and chapter Z bands.
Make no assumptions. Find ANY mismatch."""
import json, sys, io
from collections import Counter, defaultdict
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

ch = json.load(open('DT_Moria_Chapters.json',encoding='utf-8'))
z = json.load(open('DT_Moria_Zones.json',encoding='utf-8'))
lm = json.load(open('DT_Moria_Landmarks.json',encoding='utf-8'))
lc = json.load(open('DT_Moria_LayoutConnections.json',encoding='utf-8'))
zt = json.load(open('DT_Moria_ZoneTemplates.json',encoding='utf-8'))
zd = json.load(open('DT_Moria_ZoneDeck.json',encoding='utf-8'))

def fp(v,n):
    for p in v or []:
        if isinstance(p,dict) and p.get('Name')==n: return p
    return None
def gv(p):
    v=p.get('Value') if p else None
    if isinstance(v,list) and v:
        d=v[0].get('Value') if isinstance(v[0],dict) else None
        if isinstance(d,dict): return (d.get('X'),d.get('Y'),d.get('Z'))
    return None
def gf(r,k):
    p=fp(r['Value'],k); v=p.get('Value') if p else None
    if isinstance(v,list):
        for it in v:
            if isinstance(it,dict) and it.get('Name')=='RowName': return it.get('Value','')
    return v
def st(r):
    p=fp(r.get('Value',[]),'EnabledState')
    return str(p.get('Value','')).split('::')[-1] if p else None
def zoneset(r):
    p=fp(r.get('Value',[]),'ZoneSet')
    return str(p.get('Value','')).split('::')[-1] if p else None

# Build chapter band map: chapter_name -> (MinZ, MaxZ, PrimeZ)
chap_bands = {}
for r in ch['Exports'][0]['Table']['Data']:
    n = r['Name']
    chap_bands[n] = (gf(r,'MinZ'), gf(r,'MaxZ'), gf(r,'PrimeZ'))

print('===== CHAPTER BAND MAP =====')
ss_chaps = [(n,b) for n,b in chap_bands.items()
            if n.startswith('SandboxSmall')]
for n, b in sorted(ss_chaps):
    if st(next(r for r in ch['Exports'][0]['Table']['Data'] if r['Name']==n)) != 'Disabled':
        print(f'  {n:<30} MinZ={b[0]} MaxZ={b[1]} PrimeZ={b[2]}')

# Check 1: every zone's Z extent inside its primary chapter's band?
print('\n===== CHECK 1: Zone Position+TargetSize inside chapter Z band =====')
violations = []
for r in z['Exports'][0]['Table']['Data']:
    if zoneset(r) != 'SandboxSmall' or st(r) == 'Disabled': continue
    pos = gv(fp(r['Value'],'Position'))
    sz = gv(fp(r['Value'],'TargetSize'))
    chap = gf(r,'Chapter')
    if not pos or not sz or pos == (0,0,0): continue
    band = chap_bands.get(chap)
    if not band: continue
    z0 = pos[2]; z1 = pos[2] + sz[2] - 1
    mn, mx = band[0], band[1]
    if z0 < mn or z1 > mx:
        violations.append((r['Name'], pos, sz, chap, band))
print(f'Zones outside their chapter Z band: {len(violations)}')
for n, pos, sz, chap, band in violations[:20]:
    print(f'  {n}: Pos.Z={pos[2]}..{pos[2]+sz[2]-1} but {chap} band={band[0]}..{band[1]}')

# Check 2: every landmark BP.Z (non-sentinel) inside ITS HOST ZONE's chapter band
print('\n===== CHECK 2: Landmark BP.Z inside host zone chapter band =====')
hosts = {}  # landmark name -> set of (zone_name, host_chapter)
for r in z['Exports'][0]['Table']['Data']:
    if zoneset(r) != 'SandboxSmall' or st(r) == 'Disabled': continue
    chap = gf(r,'Chapter')
    lh = fp(r['Value'],'LandmarkHandles')
    for entry in (lh.get('Value') or []) if lh else []:
        if not isinstance(entry,dict): continue
        ev = entry.get('Value')
        if not isinstance(ev,list): continue
        for sub in ev:
            if isinstance(sub,dict) and sub.get('Name')=='Landmark':
                lv = sub.get('Value')
                if isinstance(lv,list):
                    for it in lv:
                        if isinstance(it,dict) and it.get('Name')=='RowName':
                            ln = it.get('Value','')
                            if ln: hosts.setdefault(ln,set()).add((r['Name'],chap))

violations2 = []
for r in lm['Exports'][0]['Table']['Data']:
    if r['Name'] not in hosts: continue
    bp = gv(fp(r['Value'],'BasePosition'))
    if not bp or (bp[0] == 0 and bp[1] == 0): continue
    for zn, chap in hosts[r['Name']]:
        band = chap_bands.get(chap)
        if not band: continue
        if bp[2] < band[0] or bp[2] > band[1]:
            violations2.append((r['Name'], bp, zn, chap, band))
print(f'Landmark BPs outside host chapter band: {len(violations2)}')
for ln, bp, zn, chap, band in violations2[:20]:
    print(f'  {ln} BP.Z={bp[2]} hosted on {zn} (chap={chap}, band={band[0]}..{band[1]})')

# Check 3: LayoutConnections Subcell.Z inside SOME chapter band
print('\n===== CHECK 3: LayoutConnections Subcell.Z covered by some chapter =====')
ss_band_cells = set()
for n, b in ss_chaps:
    if st(next(r for r in ch['Exports'][0]['Table']['Data'] if r['Name']==n)) != 'Disabled':
        for zz in range(b[0], b[1]+1):
            ss_band_cells.add(zz)
print(f'  Live SS chapter Z cells: {sorted(ss_band_cells)}')
violations3 = []
for r in lc['Exports'][0]['Table']['Data']:
    if zoneset(r) != 'SandboxSmall' or st(r) == 'Disabled': continue
    sc = gv(fp(r['Value'],'Subcell'))
    if not sc: continue
    if sc[2] not in ss_band_cells:
        violations3.append((r['Name'], sc))
print(f'Subcell.Z values outside any Live SS chapter band: {len(violations3)}')
for n, sc in violations3[:20]:
    print(f'  {n} Subcell.Z={sc[2]}')

# Check 4: every Z value referenced in connection endpoints (via landmark/zone refs)
# Check 5: ZoneCoord values — are they used to compute absolute Z?
print('\n===== CHECK 4: ZoneTemplate ZoneCoord — does it tie to chapter Z anywhere? =====')
# For each ZoneTemplate, find all Z values
zt_zcoords = []
for r in zt['Exports'][0]['Table']['Data']:
    zc = gv(fp(r['Value'],'ZoneCoord'))
    if zc: zt_zcoords.append((r['Name'], zc))
print(f'  Total ZoneTemplate rows: {len(zt["Exports"][0]["Table"]["Data"])}')
print(f'  Rows with ZoneCoord: {len(zt_zcoords)}')
print(f'  ZoneCoord Z value distribution: {Counter(t[1][2] for t in zt_zcoords)}')

# Check 6: PositionVariance values — anything non-zero?
print('\n===== CHECK 6: Zone PositionVariance distribution =====')
for r in z['Exports'][0]['Table']['Data']:
    pv = gv(fp(r['Value'],'PositionVariance'))
    if pv and pv != (0,0,0):
        print(f'  {r["Name"]}: PositionVariance={pv}')
print('(silence above = all PositionVariance are (0,0,0))')

# Check 7: any Live SS connection endpoint whose target landmark's BP isn't matched?
print('\n===== CHECK 7: Connection endpoint landmarks vs their BPs =====')
lm_by_name = {r['Name']: r for r in lm['Exports'][0]['Table']['Data']}
problems = 0
for r in lc['Exports'][0]['Table']['Data']:
    if zoneset(r) != 'SandboxSmall' or st(r) == 'Disabled': continue
    for fld in ('OriginLandmark','DestinationLandmark'):
        ln = gf(r, fld)
        if not ln or ln == 'None': continue
        lm_row = lm_by_name.get(ln)
        if not lm_row:
            print(f'  {r["Name"]}.{fld} -> {ln} (NOT IN LANDMARKS TABLE)')
            problems += 1
            continue
        bp = gv(fp(lm_row['Value'],'BasePosition'))
        if not bp: continue
        # is BP.Z in any Live chapter band?
        if bp[0] != 0 or bp[1] != 0:  # skip sentinels
            if bp[2] not in ss_band_cells:
                print(f'  {r["Name"]}.{fld} -> {ln} BP.Z={bp[2]} OUTSIDE all Live SS bands')
                problems += 1
if problems == 0: print('(no issues found)')

# Check 8: is there ANY field with int Z values 1..14 (vanilla pre-shift Z range)
# that we might have missed?
print('\n===== CHECK 8: Any int field with values matching vanilla pre-shift Z range (1..14) =====')
def walk_check_z_range(obj, path, hits):
    if isinstance(obj, dict):
        nm = obj.get('Name')
        v = obj.get('Value')
        ptype = obj.get('$type','')
        if isinstance(nm, str) and isinstance(v, int) and 1 <= v <= 14:
            # Only flag if the field name suggests it could be Z
            if any(p in nm for p in ('Pos','Coord','Cell','Z','Height','Layer','Min','Max','Prime','Floor','Level')):
                hits.append((path[-3:], nm, v))
        for k, val in obj.items():
            if isinstance(val, (dict, list)):
                walk_check_z_range(val, path + [nm or k], hits)
    elif isinstance(obj, list):
        for i, it in enumerate(obj):
            walk_check_z_range(it, path + [f'[{i}]'], hits)

# Audit all 5 main files
all_hits = []
for label, doc in [('Zones',z),('Chapters',ch),('Landmarks',lm),('LayoutConnections',lc),('ZoneTemplates',zt)]:
    hits = []
    walk_check_z_range(doc, [label], hits)
    if hits:
        # Filter: skip ones we already know about
        known = {'MinZ','MaxZ','PrimeZ','Layer','EnemyScalingLevel','Z'}
        unknowns = [(p,n,v) for (p,n,v) in hits if n not in known]
        if unknowns:
            counter = Counter(n for _,n,_ in unknowns)
            print(f'\n  {label}:')
            for fname, cnt in counter.most_common():
                print(f'    {fname}: {cnt} instances with values 1..14')
