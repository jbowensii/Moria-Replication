"""Routing verify: post-fix Task E checklist."""
import json, os
from collections import defaultdict

ROOT = os.path.dirname(os.path.abspath(__file__))
def load(n):
    with open(os.path.join(ROOT, n), 'r', encoding='utf-8') as f: return json.load(f)

zones = load('DT_Moria_Zones.json')
landmarks = load('DT_Moria_Landmarks.json')
connections = load('DT_Moria_LayoutConnections.json')
chapters = load('DT_Moria_Chapters.json')

def rows(dt): return dt['Exports'][0]['Table']['Data']
def props(r): return {p.get('Name'): p for p in r.get('Value', []) if isinstance(p, dict)}
def get_array(row, name):
    p = props(row).get(name); return p.get('Value', []) if p else []
def get_intvec(row, name):
    p = props(row).get(name)
    if not p: return None
    for sp in p.get('Value', []):
        if isinstance(sp, dict) and sp.get('$type', '').endswith('IntVectorPropertyData, UAssetAPI'):
            v = sp.get('Value', {})
            return (v.get('X'), v.get('Y'), v.get('Z'))
    return None
def get_rowname(row, name):
    p = props(row).get(name)
    if not p: return None
    for sp in p.get('Value', []):
        if isinstance(sp, dict) and sp.get('Name') == 'RowName': return sp.get('Value')
    return None
def is_live(row):
    p = props(row).get('EnabledState')
    e = p.get('Value') if p else None
    return e is None or 'Live' in str(e)

zone_rows = rows(zones); lm_rows = rows(landmarks); conn_rows = rows(connections); chap_rows = rows(chapters)
zone_by = {r['Name']: r for r in zone_rows}
lm_by = {r['Name']: r for r in lm_rows}

def lm_handles(z):
    arr = get_array(z, 'LandmarkHandles')
    out = []
    for entry in arr:
        if not isinstance(entry, dict): continue
        lm_ref = ext = placement = None
        for sp in entry.get('Value', []):
            if not isinstance(sp, dict): continue
            nm = sp.get('Name')
            if nm == 'Landmark':
                for q in sp.get('Value', []):
                    if isinstance(q, dict) and q.get('Name') == 'RowName': lm_ref = q.get('Value')
            elif nm == 'bExtendedConnectivityLandmark':
                ext = sp.get('Value')
            elif nm == 'Placement':
                placement = sp.get('Value')
        out.append({'lm': lm_ref, 'ext': ext, 'placement': placement})
    return out

def lm_z(name):
    r = lm_by.get(name)
    if not r: return None
    bp = get_intvec(r, 'BasePosition')
    return bp[2] if bp else None

# Live SS connections
def is_live_ss(c):
    p = props(c).get('ZoneSet')
    zs = p.get('Value', '') if p else ''
    return 'SandboxSmall' in str(zs) and is_live(c)

ss_conns = [c for c in conn_rows if is_live_ss(c)]
print(f"Live SS connection rows: {len(ss_conns)}")

# === E1: coverage table ===
print("\n=== E1: LayoutConnection coverage table (endpoint Z hits) ===")
ep_count = defaultdict(int)
for c in ss_conns:
    o = get_rowname(c, 'OriginLandmark'); d = get_rowname(c, 'DestinationLandmark')
    oz = lm_z(o) if o and o != 'None' else None
    dz = lm_z(d) if d and d != 'None' else None
    if oz is not None: ep_count[oz] += 1
    if dz is not None: ep_count[dz] += 1
floors = [('Lv-7',29),('Lv-6_top',28),('Lv-6',27),('Lv-5',23),('Lv-4',22),('Lv-3',19),('Lv-2',18),
          ('Lv-1',17),('D-1',14),('D-2',13),('D-3',10),('D-4',9),('D-5',4),('D-6',1),('D-7',0)]
for fl, z in floors:
    print(f"  {fl:12s} (Z={z:2d}): {ep_count.get(z,0)} endpoints")

# === E2: 6 cross-elevator handoffs ===
print("\n=== E2: Cross-elevator handoff connections ===")
expected = ['Sandbox_E_LowerDescent_to_F_CrystalDescent','Sandbox_F_CrystalDescent_to_G_SeventhStair',
            'Sandbox_G_SeventhStair_to_C_SecondStair','Sandbox_C_SecondStair_to_H_NinthStair',
            'Sandbox_H_TenthStair_to_B_FirstStair','Sandbox_B_FourthStair_to_D_ThirdStair']
names = {r['Name'] for r in conn_rows}
e2_pass = all(n in names for n in expected)
for n in expected:
    print(f"  {'PASS' if n in names else 'FAIL'}  {n}")
print(f"  E2 OVERALL: {'PASS' if e2_pass else 'FAIL'}")

# === E3: ext flags ===
print("\n=== E3: ext flags True ===")
checks = [('Sandbox_Small_Elevator_G','Sandbox.SeventhStair'),
          ('Sandbox_Small_Elevator_E','Sandbox.LowerDescent')]
e3_pass = True
for zname, lm in checks:
    found = False
    for h in lm_handles(zone_by[zname]):
        if h['lm'] == lm:
            ok = bool(h['ext'])
            print(f"  {'PASS' if ok else 'FAIL'}  {zname} :: {lm}  ext={h['ext']}")
            if not ok: e3_pass = False
            found = True
    if not found:
        print(f"  FAIL  {zname} :: {lm}  not found"); e3_pass = False
print(f"  E3 OVERALL: {'PASS' if e3_pass else 'FAIL'}")

# === E4: every stair has GC >= 1 ===
print("\n=== E4: stair landmark GC >= 1 ===")
stairs = ['Sandbox.LowerDescent','Sandbox.CrystalDescent','Sandbox.SeventhStair','Sandbox.SecondStair',
          'Sandbox.NinthStair','Sandbox.TenthStair','Sandbox.FirstStair','Sandbox.FourthStair',
          'Sandbox.ThirdStair','Sandbox.SixthStair','Sandbox.EighthStair','Sandbox.EleventhStair']
e4_pass = True
for s in stairs:
    r = lm_by.get(s)
    gc = get_array(r, 'GuaranteedConnections') if r else []
    ok = len(gc) >= 1
    print(f"  {'PASS' if ok else 'FAIL'}  {s:35s} GC={len(gc)}")
    if not ok: e4_pass = False
print(f"  E4 OVERALL: {'PASS' if e4_pass else 'FAIL'}")

# === E5: NameMap counters synced ===
print("\n=== E5: NameMap counters synced ===")
e5_pass = True
for fn, dt in [('Zones',zones),('Chapters',chapters),('Landmarks',landmarks),('LayoutConnections',connections)]:
    nm = dt.get('NameMap', [])
    nrc = dt.get('NamesReferencedFromExportDataCount', 0)
    ok = nrc >= len(nm)
    print(f"  {'PASS' if ok else 'FAIL'}  {fn}: NameMap={len(nm)} NamesRef={nrc}")
    if not ok: e5_pass = False
print(f"  E5 OVERALL: {'PASS' if e5_pass else 'FAIL'}")

# === E6: no Origin/Dest landmark refs to missing landmarks ===
print("\n=== E6: connection landmark references valid ===")
e6_pass = True
miss = []
for c in conn_rows:
    o = get_rowname(c, 'OriginLandmark'); d = get_rowname(c, 'DestinationLandmark')
    for v in (o, d):
        if v and v != 'None' and v not in lm_by:
            miss.append((c['Name'], v))
            e6_pass = False
for n, v in miss: print(f"  FAIL  {n} references missing landmark: {v}")
print(f"  E6 OVERALL: {'PASS' if e6_pass else 'FAIL'} ({len(miss)} bad refs)")

# === E7: GC TagName references valid ===
print("\n=== E7: GC TagName references valid ===")
e7_pass = True
bad = []
for r in lm_rows:
    gc = get_array(r, 'GuaranteedConnections')
    for entry in gc:
        for sp in entry.get('Value', []):
            if sp.get('Name') == 'TagName':
                tag = sp.get('Value')
                if tag and tag.startswith('World.Landmark.'):
                    short = tag[len('World.Landmark.'):]
                    if short not in lm_by:
                        bad.append((r['Name'], tag))
                        e7_pass = False
for n, t in bad: print(f"  FAIL  landmark {n} GC tag missing target: {t}")
print(f"  E7 OVERALL: {'PASS' if e7_pass else 'FAIL'} ({len(bad)} bad)")

# === E8: zero out-of-range stair landmark BPs ===
print("\n=== E8: stair landmark BPs in zone footprints ===")
def zone_fp(z):
    pos = get_intvec(z,'Position'); sz = get_intvec(z,'TargetSize')
    if not pos or not sz or None in pos or None in sz: return None
    px,py,pz=pos; sx,sy,sz_=sz
    return {'xmin':px,'xmax':px+sx-1,'ymin':py,'ymax':py+sy-1,'zmin':pz,'zmax':pz+sz_-1}

ss_zones_live = [z for z in zone_rows if z['Name'].startswith('Sandbox_Small_') and is_live(z)]
e8_pass = True
oob = []
for z in ss_zones_live:
    fp = zone_fp(z)
    if not fp: continue
    for h in lm_handles(z):
        if not h['placement'] or 'Fixed' not in str(h['placement']): continue
        lm = h['lm']
        if not lm or lm == 'None': continue
        r = lm_by.get(lm)
        if not r: continue
        bp = get_intvec(r, 'BasePosition')
        if not bp or None in bp: continue
        bx,by,bz=bp
        if not (fp['xmin']<=bx<=fp['xmax'] and fp['ymin']<=by<=fp['ymax'] and fp['zmin']<=bz<=fp['zmax']):
            # only flag stairs
            if any(s in lm for s in ['Stair','Descent']):
                oob.append((z['Name'], lm, bp))
                e8_pass = False
for zn, lm, bp in oob: print(f"  FAIL  {zn} :: {lm} BP={bp} out of zone fp")
print(f"  E8 OVERALL: {'PASS' if e8_pass else 'FAIL'} ({len(oob)} stair OOB)")

# === E9: 14 level rows in chapters ===
print("\n=== E9: level rows in chapters ===")
level_rows = [r for r in chap_rows if r['Name'].startswith('SandboxSmall-Chapter')]
e9_pass = len(level_rows) == 14
print(f"  Level rows: {len(level_rows)}  -> {'PASS' if e9_pass else 'FAIL'}")

# Final
print("\n" + "="*60)
results = [('E1 coverage table','PRINTED'),('E2 cross-elevator',e2_pass),('E3 ext flags',e3_pass),
           ('E4 stair GC>=1',e4_pass),('E5 NameMap sync',e5_pass),('E6 conn LM refs',e6_pass),
           ('E7 GC tag refs',e7_pass),('E8 stair BP in fp',e8_pass),('E9 14 level rows',e9_pass)]
for k,v in results:
    print(f"  {k}: {v}")
