"""Audit vanilla and current data; determine bubble Z placement direction."""
import json, os

ROOT = os.path.dirname(os.path.abspath(__file__))

def find_rows(uasset):
    for exp in uasset.get('Exports', []):
        t = exp.get('Table')
        if t and 'Data' in t:
            return t['Data']
    return []

def row_props(row): return row.get('Value', []) or []

def prop_get(rd, name):
    for p in rd:
        if p.get('Name') == name: return p
    return None

def prop_int(rd, name, default=None):
    p = prop_get(rd, name)
    return p.get('Value', default) if p else default

def prop_bool(rd, name, default=None):
    p = prop_get(rd, name)
    return p.get('Value', default) if p else default

def intvec(rd, name):
    """Read IntVector struct: outer struct's Value is list of one IntVectorPropertyData whose Value is dict X/Y/Z."""
    p = prop_get(rd, name)
    if not p: return None
    inner = p.get('Value')
    if isinstance(inner, list) and inner:
        v = inner[0].get('Value')
        if isinstance(v, dict) and all(k in v for k in 'XYZ'):
            return (v['X'], v['Y'], v['Z'])
    return None

def landmark_handles(rd):
    """Return list of landmark RowNames referenced by the zone."""
    out = []
    p = prop_get(rd, 'LandmarkHandles')
    if not p: return out
    arr = p.get('Value', []) or []
    for entry in arr:
        # entry is StructProperty MorZoneLandmarkEntry; its Value is list of properties
        entry_props = entry.get('Value', []) or []
        lh = prop_get(entry_props, 'Landmark')
        if lh:
            inner = lh.get('Value', []) or []
            rn = prop_get(inner, 'RowName')
            if rn: out.append(rn.get('Value'))
    return out

def load_rows(p):
    with open(p,'r',encoding='utf-8') as f: d=json.load(f)
    return find_rows(d)

# === VANILLA SS chapters ===
print("=== VANILLA SandboxSmall chapters ===")
v_chap = {}
for r in load_rows(os.path.join(ROOT,'DT_Moria_Chapters.original.json')):
    name = r.get('Name','')
    rd = row_props(r)
    zs = prop_get(rd,'ZoneSet'); zsv = zs.get('Value') if zs else None
    if zsv == 'EZoneSet::SandboxSmall':
        mn=prop_int(rd,'MinZ'); mx=prop_int(rd,'MaxZ'); pz=prop_int(rd,'PrimeZ')
        v_chap[name] = (mn,mx,pz)
        print(f"  {name:30s} MinZ={mn} MaxZ={mx} PrimeZ={pz}")
v_minZ = min(c[0] for c in v_chap.values())
v_maxZ = max(c[1] for c in v_chap.values())
print(f"  Vanilla SS world Z range: {v_minZ}..{v_maxZ}")

# === VANILLA stair landmarks ===
print()
print("=== VANILLA stair landmark BPs ===")
v_lm = {}
stair_kw = ['Stair','Descent']
for r in load_rows(os.path.join(ROOT,'DT_Moria_Landmarks.original.json')):
    nm = r.get('Name','')
    if any(k in nm for k in stair_kw):
        bp = intvec(row_props(r),'BasePosition')
        v_lm[nm] = bp
        print(f"  {nm:40s} BP={bp}")

# === VANILLA stair zones (TargetSize Z=4) ===
print()
print("=== VANILLA stair/elevator zones ===")
v_zones = {}
for r in load_rows(os.path.join(ROOT,'DT_Moria_Zones.original.json')):
    nm = r.get('Name','')
    rd = row_props(r)
    pos = intvec(rd,'Position'); ts = intvec(rd,'TargetSize')
    if ts and ts[2]==4 and ts[0]==6 and ts[1]==6:
        lh = landmark_handles(rd)
        bpfl = prop_bool(rd,'bPositionFromLandmarks')
        bpfz = prop_bool(rd,'bPositionFromZoneTable')
        # find chapter to get its PrimeZ
        ch = prop_get(rd,'Chapter')
        chrn = None
        if ch:
            iv = ch.get('Value',[]) or []
            rn = prop_get(iv,'RowName')
            chrn = rn.get('Value') if rn else None
        v_zones[nm]=(pos,ts,lh,bpfl,bpfz,chrn)
        print(f"  {nm:35s} Pos={pos} TS={ts} bPFL={bpfl} bPFZ={bpfz} Chapter={chrn} LMs={lh}")

# === Compute bubble Z range per direction hypothesis ===
print()
print("=== VANILLA bubble Z hypothesis test ===")
print("Formula UP:    bubble Z = [BP.Z .. BP.Z + TS.Z - 1]")
print("Formula DOWN:  bubble Z = [BP.Z - TS.Z + 1 .. BP.Z]")
print("Formula CENTER:bubble Z = [BP.Z - TS.Z//2 .. BP.Z + TS.Z//2 - 1] (or +TS.Z/2)")
print()
for zname,(pos,ts,lhs,bpfl,bpfz,chrn) in v_zones.items():
    # use first landmark
    if not lhs: continue
    lmname = lhs[0]
    # find by exact match
    bp = None
    for k,v in v_lm.items():
        if k == lmname or k.endswith('.'+lmname) or k == 'Sandbox.'+lmname:
            bp = v; break
    if bp is None:
        print(f"  {zname}: landmark {lmname} not found"); continue
    bz = bp[2]; tz = ts[2]
    up = (bz, bz+tz-1)
    dn = (bz-tz+1, bz)
    print(f"  {zname:30s} LM={lmname:20s} BP.Z={bz} TS.Z={tz}  UP={up}  DOWN={dn}")
print(f"  World bounds: [{v_minZ}..{v_maxZ}]")

# Conclude
def in_bounds(rng,lo,hi): return rng[0]>=lo and rng[1]<=hi

up_ok=True; dn_ok=True
for zname,(pos,ts,lhs,bpfl,bpfz,chrn) in v_zones.items():
    if not lhs: continue
    bp=None
    for k,v in v_lm.items():
        if k.endswith('.'+lhs[0]) or k==lhs[0] or k=='Sandbox.'+lhs[0]:
            bp=v; break
    if bp is None: continue
    bz=bp[2]; tz=ts[2]
    if not in_bounds((bz,bz+tz-1), v_minZ, v_maxZ): up_ok=False
    if not in_bounds((bz-tz+1,bz), v_minZ, v_maxZ): dn_ok=False
print(f"  All-vanilla-fits-UP={up_ok}  All-vanilla-fits-DOWN={dn_ok}")
