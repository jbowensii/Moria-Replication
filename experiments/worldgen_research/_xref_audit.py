"""Cross-reference audit covering 10 sub-checks beyond validator+deep_verify."""
import json
from pathlib import Path
from collections import defaultdict

WGR = Path(__file__).resolve().parent
LM = json.load(open(WGR / 'DT_Moria_Landmarks.json', encoding='utf-8'))
ZN = json.load(open(WGR / 'DT_Moria_Zones.json', encoding='utf-8'))
LC = json.load(open(WGR / 'DT_Moria_LayoutConnections.json', encoding='utf-8'))
CH = json.load(open(WGR / 'DT_Moria_Chapters.json', encoding='utf-8'))

NULL = {'None', 'Null', '', None}

def fp(v, n):
    for p in v or []:
        if isinstance(p, dict) and p.get('Name') == n:
            return p
    return None

def state(r):
    p = fp(r.get('Value', []), 'EnabledState')
    return str(p.get('Value', '')).split('::')[-1] if p else None

def get_rowname(prop):
    if not prop: return None
    v = prop.get('Value')
    if isinstance(v, list):
        for s in v:
            if isinstance(s, dict) and s.get('Name') == 'RowName':
                return s.get('Value')
    return None

def get_struct_field(struct_val_list, field):
    for p in struct_val_list or []:
        if isinstance(p, dict) and p.get('Name') == field:
            return p
    return None

def get_vec(prop):
    """Return (X,Y,Z) ints from a Vector/IntVector struct (handles both list-of-fields and dict {X,Y,Z} forms)."""
    if not prop: return None
    v = prop.get('Value')
    # Outer struct often wraps in a list with one IntVectorPropertyData entry whose Value is dict {X,Y,Z}
    if isinstance(v, list):
        # Try inner dict form
        for s in v:
            if isinstance(s, dict):
                inner = s.get('Value')
                if isinstance(inner, dict) and 'X' in inner and 'Y' in inner and 'Z' in inner:
                    return (int(inner['X']), int(inner['Y']), int(inner['Z']))
        # Fall back to flat list of named X/Y/Z properties
        x = y = z = None
        for s in v:
            if not isinstance(s, dict): continue
            n = s.get('Name'); val = s.get('Value')
            if n == 'X': x = val
            elif n == 'Y': y = val
            elif n == 'Z': z = val
        if x is not None and y is not None and z is not None:
            return (int(x), int(y), int(z))
        return None
    if isinstance(v, dict) and 'X' in v and 'Y' in v and 'Z' in v:
        return (int(v['X']), int(v['Y']), int(v['Z']))
    return None

def zoneset(r):
    p = fp(r.get('Value', []), 'ZoneSet')
    return str(p.get('Value', '')).split('::')[-1] if p else None

# Index landmarks
lm_rows = LM['Exports'][0]['Table']['Data']
lm_by_name = {r['Name']: r for r in lm_rows}

# Index zones
z_rows = ZN['Exports'][0]['Table']['Data']
z_by_name = {r['Name']: r for r in z_rows}

# Index chapters
ch_rows = CH['Exports'][0]['Table']['Data']
ch_by_name = {r['Name']: r for r in ch_rows}

# Index lc
lc_rows = LC['Exports'][0]['Table']['Data']
lc_by_name = {r['Name']: r for r in lc_rows}

print('='*70)
print('AUDIT 1 — Chain connection integrity')
print('='*70)
chain_lcs = [r for r in lc_rows if r.get('Name','').startswith('Sandbox_Small_Chain_')]
print(f'Found {len(chain_lcs)} Sandbox_Small_Chain_* connections')
issues_1 = []
for r in chain_lcs:
    name = r['Name']
    val = r.get('Value', [])
    oz = get_rowname(fp(val, 'OriginZone'))
    ol = get_rowname(fp(val, 'OriginLandmark'))
    dz = get_rowname(fp(val, 'DestinationZone'))
    dl = get_rowname(fp(val, 'DestinationLandmark'))
    req = fp(val, 'bRequired')
    req_v = req.get('Value') if req else None
    zs = zoneset(r)
    st = state(r)

    def check_ref(label, refname, table):
        if not refname or refname in NULL:
            issues_1.append(f'{name}: {label} is null')
            return
        row = table.get(refname)
        if not row:
            issues_1.append(f'{name}: {label}={refname} does not exist')
            return
        if state(row) != 'Live':
            issues_1.append(f'{name}: {label}={refname} is {state(row)}')
    check_ref('OriginZone', oz, z_by_name)
    check_ref('OriginLandmark', ol, lm_by_name)
    check_ref('DestinationZone', dz, z_by_name)
    check_ref('DestinationLandmark', dl, lm_by_name)
    if req_v is not True:
        issues_1.append(f'{name}: bRequired={req_v} (not True)')
    if zs != 'SandboxSmall':
        issues_1.append(f'{name}: ZoneSet={zs}')
    if st != 'Live':
        issues_1.append(f'{name}: EnabledState={st}')
if issues_1:
    print(f'  {len(issues_1)} issue(s):')
    for i in issues_1: print(f'   - {i}')
else:
    print('  OK — all chain LCs reference Live rows, bRequired=true, SS, Live')

print()
print('='*70)
print('AUDIT 2 — Stair zone catalog (SS Live, ext-conn LM with Size.Z >= 2)')
print('='*70)

# Resolve landmark base positions
def lm_basepos(lm_row):
    bp = fp(lm_row.get('Value', []), 'BasePosition')
    return get_vec(bp)

# Landmark TargetSize (only on Live landmarks; many landmarks don't have it)
def lm_targetsize(lm_row):
    ts = fp(lm_row.get('Value', []), 'TargetSize')
    return get_vec(ts)

# Iterate live SS zones, walk LandmarkHandles
stair_records = []  # zone_name, primary_chap, additional_chaps, lm_name, bp, sz_landmark
for r in z_rows:
    if state(r) != 'Live': continue
    if zoneset(r) != 'SandboxSmall': continue
    zname = r['Name']
    primary_p = fp(r.get('Value', []), 'Chapter')
    primary = get_rowname(primary_p)
    ac_p = fp(r.get('Value', []), 'AdditionalChapters')
    add_chs = []
    if ac_p:
        for entry in (ac_p.get('Value') or []):
            inner = entry.get('Value') if isinstance(entry, dict) else None
            if isinstance(inner, list):
                rn = None
                for s in inner:
                    if isinstance(s, dict) and s.get('Name') == 'RowName':
                        rn = s.get('Value'); break
                if rn and rn not in NULL: add_chs.append(rn)
    # Zone's TargetSize as stair-height proxy
    zsize = get_vec(fp(r.get('Value', []), 'TargetSize'))
    z_size_z = zsize[2] if zsize else None
    lh = fp(r.get('Value', []), 'LandmarkHandles')
    if not lh: continue
    for entry in (lh.get('Value') or []):
        inner = entry.get('Value') if isinstance(entry, dict) else None
        if not isinstance(inner, list): continue
        ext = fp(inner, 'bExtendedConnectivityLandmark')
        ext_v = ext.get('Value') if ext else None
        lm_p = fp(inner, 'Landmark')
        lname = get_rowname(lm_p)
        lm_row = lm_by_name.get(lname) if lname else None
        ts_z = z_size_z  # derive from host zone footprint
        if ext_v is True and ts_z is not None and ts_z >= 2:
            bp = lm_basepos(lm_row) if lm_row and state(lm_row)=='Live' else None
            stair_records.append({
                'zone': zname, 'primary': primary, 'add': add_chs,
                'landmark': lname, 'bp': bp, 'sz_z': ts_z,
            })

print(f'Found {len(stair_records)} stair landmark records:')
for s in stair_records:
    bp = s['bp']
    bp_str = f'BP=({bp[0]},{bp[1]},{bp[2]})' if bp else 'BP=?'
    print(f'  zone={s["zone"]}  primary={s["primary"]}  add={s["add"]}  Size.Z={s["sz_z"]}  LM={s["landmark"]} {bp_str}')

# chapter primary uniqueness
prim_count = defaultdict(int)
for s in stair_records: prim_count[s['primary']] += 1
print()
print('Chapter primary uniqueness:')
dups = [c for c,n in prim_count.items() if n > 1]
if dups:
    for c in dups: print(f'  WARN: chapter {c} has {prim_count[c]} stair zones primary')
else:
    print('  OK — each chapter has at most 1 stair zone primary')

# stair_xy_collision
xy_map = defaultdict(list)
for s in stair_records:
    if s['bp']: xy_map[(s['bp'][0], s['bp'][1])].append(s['landmark'])
collisions = {k:v for k,v in xy_map.items() if len(v) > 1}
print()
print('Stair X,Y collision check:')
if collisions:
    for k,v in collisions.items(): print(f'  COLLIDE at {k}: {v}')
else:
    print('  OK — all stair landmarks have unique X,Y')

print()
print('='*70)
print('AUDIT 3 — Floor connectivity matrix (14 floors)')
print('='*70)
# Build chapter -> Z band
def chap_band(name):
    r = ch_by_name.get(name)
    if not r: return None
    minz_p = fp(r.get('Value', []), 'MinZ')
    maxz_p = fp(r.get('Value', []), 'MaxZ')
    primez_p = fp(r.get('Value', []), 'PrimeZ')
    return (
        minz_p.get('Value') if minz_p else None,
        maxz_p.get('Value') if maxz_p else None,
        primez_p.get('Value') if primez_p else None,
    )

# Floor labels Lv-7..D-7 — derive from live SS chapters by Layer
ss_live_chaps = []
for r in ch_rows:
    if state(r) != 'Live': continue
    if zoneset(r) != 'SandboxSmall': continue
    layer_p = fp(r.get('Value', []), 'Layer')
    layer = layer_p.get('Value') if layer_p else None
    band = chap_band(r['Name'])
    ss_live_chaps.append((r['Name'], layer, band))
ss_live_chaps.sort(key=lambda x: -(x[1] if x[1] is not None else 0))
print(f'{len(ss_live_chaps)} Live SS chapters')

# Map chapter -> stairs that reach it (primary or additional)
chap_to_stairs = defaultdict(list)
for s in stair_records:
    chap_to_stairs[s['primary']].append((s['zone'], 'primary'))
    for ac in s['add']:
        chap_to_stairs[ac].append((s['zone'], 'add'))

floors_with_no_stair = []
for cname, layer, band in ss_live_chaps:
    stairs = chap_to_stairs.get(cname, [])
    print(f'  {cname} (Layer={layer}, Z={band}): {len(stairs)} stair(s)')
    for z, kind in stairs: print(f'    - {z} ({kind})')
    if not stairs:
        floors_with_no_stair.append(cname)

print()
if floors_with_no_stair:
    print(f'  WARN: floors with no stair access: {floors_with_no_stair}')
else:
    print('  OK — every floor has at least 1 stair anchored on or reaching it')

print()
print('='*70)
print('AUDIT 4 — Chapter Z band coverage & overlap')
print('='*70)
issues_4 = []
for cname, layer, band in ss_live_chaps:
    minz, maxz, primez = band if band else (None,None,None)
    if minz is None or maxz is None or primez is None:
        issues_4.append(f'{cname}: missing Z fields')
        continue
    if not (minz <= primez <= maxz):
        issues_4.append(f'{cname}: PrimeZ {primez} outside [{minz},{maxz}]')

# Pairwise overlap
ranges = [(c, b[0], b[1]) for c,_,b in ss_live_chaps if b]
for i in range(len(ranges)):
    for j in range(i+1, len(ranges)):
        a = ranges[i]; b = ranges[j]
        if a[1] is None or a[2] is None or b[1] is None or b[2] is None: continue
        if a[1] <= b[2] and b[1] <= a[2]:
            issues_4.append(f'OVERLAP: {a[0]} [{a[1]},{a[2]}] vs {b[0]} [{b[1]},{b[2]}]')
if issues_4:
    for i in issues_4: print(f'  - {i}')
else:
    print('  OK — every chapter has MinZ<=PrimeZ<=MaxZ; no Z range overlaps')

print()
print('='*70)
print('AUDIT 5 — Stair anchor Z within chapter band OR elevator footprint')
print('='*70)
issues_5 = []
for s in stair_records:
    if not s['bp']:
        issues_5.append(f'{s["landmark"]}: no BasePosition'); continue
    z = s['bp'][2]
    band = chap_band(s['primary']) or (None,None,None)
    minz, maxz, _ = band
    in_chap = minz is not None and maxz is not None and minz <= z <= maxz
    in_foot = z is not None and z + s['sz_z'] - 1 <= 29 and z >= 0  # softer footprint check
    # The "elevator footprint" rule: BP.Z .. BP.Z+Size.Z-1 must include lm Z (always true).
    # Real check: lm Z in [primary chap MinZ..MaxZ]
    if not in_chap:
        issues_5.append(f'{s["landmark"]} z={z} outside primary {s["primary"]} band [{minz},{maxz}] (zone={s["zone"]})')
if issues_5:
    for i in issues_5: print(f'  - {i}')
else:
    print('  OK — every stair anchor lm Z is inside primary chapter Z band')

print()
print('='*70)
print('AUDIT 6 — NameMap completeness (4 working DTs)')
print('='*70)
for tag, doc in [('Zones', ZN), ('Chapters', CH), ('Landmarks', LM), ('LayoutConnections', LC)]:
    nm = doc.get('NameMap', [])
    nrefed = doc.get('NamesReferencedFromExportDataCount')
    gens = doc.get('Generations') or []
    gen0 = gens[0].get('NameCount') if gens else None
    ok = (len(nm) == nrefed == gen0)
    print(f'  {tag}: NameMap={len(nm)} NRefED={nrefed} Gen[0].NameCount={gen0} {"OK" if ok else "MISMATCH"}')

print()
print('='*70)
print('AUDIT 7 — Engine bound check ([0..29] Z)')
print('='*70)
issues_7 = []
for r in z_rows:
    if state(r) != 'Live': continue
    if zoneset(r) != 'SandboxSmall': continue
    pos = get_vec(fp(r.get('Value', []), 'Position'))
    sz = get_vec(fp(r.get('Value', []), 'TargetSize'))
    if pos:
        if pos[2] < 0 or pos[2] > 29:
            issues_7.append(f'zone {r["Name"]} Position.Z={pos[2]}')
    if pos and sz:
        top = pos[2] + sz[2] - 1
        if top > 29:
            issues_7.append(f'zone {r["Name"]} footprint top={top} > 29')
for r in lm_rows:
    if state(r) != 'Live': continue
    bp = get_vec(fp(r.get('Value', []), 'BasePosition'))
    if bp:
        if bp[2] < 0 or bp[2] > 29:
            issues_7.append(f'landmark {r["Name"]} BP.Z={bp[2]}')
if issues_7:
    for i in issues_7: print(f'  - {i}')
else:
    print('  OK — all Live SS zone/landmark Z values within [0..29]')

print()
print('='*70)
print('AUDIT 8 — DarkestDeeps disabled & embedded_bottom rule')
print('='*70)
DD_ZONES = ['Sandbox_Small_DarkestDeeps_A','Sandbox_Small_DarkestDeeps_B','Sandbox_Small_DarkestDeeps_C','Sandbox_Small_DarkestDeeps_D','Sandbox_Small_DarkestDeeps_E']
issues_8 = []
for n in DD_ZONES:
    r = z_by_name.get(n)
    if not r:
        issues_8.append(f'{n}: missing'); continue
    s = state(r)
    if s != 'Disabled':
        issues_8.append(f'{n}: state={s} (expected Disabled)')
        # then check rule
        primary = get_rowname(fp(r.get('Value', []), 'PrimaryChapter'))
        band = chap_band(primary) or (None,None,None)
        minz, maxz, primez = band
        if minz is None or primez is None:
            issues_8.append(f'  {n}: chap {primary} missing Z')
        elif not (minz < primez):
            issues_8.append(f'  {n}: rule violation MinZ<PrimeZ ({minz}<{primez})')
if issues_8:
    for i in issues_8: print(f'  - {i}')
else:
    print('  OK — all 5 DarkestDeeps zones still Disabled')

print()
print('='*70)
print('AUDIT 9 — Disabled-zone reference scan')
print('='*70)
disabled_zones = {r['Name'] for r in z_rows if state(r) == 'Disabled'}
issues_9 = []
for r in lc_rows:
    if state(r) != 'Live': continue
    val = r.get('Value', [])
    oz = get_rowname(fp(val, 'OriginZone'))
    dz = get_rowname(fp(val, 'DestinationZone'))
    if oz in disabled_zones:
        issues_9.append(f'LC {r["Name"]}: OriginZone={oz} is Disabled')
    if dz in disabled_zones:
        issues_9.append(f'LC {r["Name"]}: DestinationZone={dz} is Disabled')
if issues_9:
    for i in issues_9: print(f'  - {i}')
else:
    print(f'  OK — {len(disabled_zones)} disabled zones, no Live LC refs them')

print()
print('='*70)
print('AUDIT 10 — Disabled-landmark reference scan')
print('='*70)
disabled_lms = {r['Name'] for r in lm_rows if state(r) == 'Disabled'}
issues_10 = []
# scan zones
for r in z_rows:
    if state(r) != 'Live': continue
    lh = fp(r.get('Value', []), 'LandmarkHandles')
    if not lh: continue
    for entry in (lh.get('Value') or []):
        inner = entry.get('Value') if isinstance(entry, dict) else None
        if not isinstance(inner, list): continue
        lname = get_rowname(fp(inner, 'Landmark'))
        if lname in disabled_lms:
            issues_10.append(f'Live zone {r["Name"]}: LandmarkHandle refs Disabled landmark {lname}')
# scan LCs
for r in lc_rows:
    if state(r) != 'Live': continue
    val = r.get('Value', [])
    for f in ('OriginLandmark', 'DestinationLandmark'):
        v = get_rowname(fp(val, f))
        if v in disabled_lms:
            issues_10.append(f'Live LC {r["Name"]}: {f}={v} is Disabled')
print(f'Disabled landmarks: {len(disabled_lms)}')
if issues_10:
    for i in issues_10: print(f'  - {i}')
else:
    print('  OK — no Live row refs any Disabled landmark')

print()
print('='*70)
print('AUDIT COMPLETE')
print('='*70)
