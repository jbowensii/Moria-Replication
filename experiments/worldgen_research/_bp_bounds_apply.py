"""Diagnose current state and apply Strategy A: shrink TargetSize.Z 4->1 on all elevator zones.

Formula confirmed by audit (vanilla all fits): bubble Z = [BP.Z .. BP.Z + TS.Z - 1].
Therefore Lv-7 (PrimeZ=28, MaxZ=28) with TS.Z=4 → bubble (28..31) > world MaxZ=28: FAIL.
Lv-6 (27,28..31..30): also fails. Etc.

Strategy A: TS.Z=1 -> bubble Z = [BP.Z..BP.Z], single-cell, always inside any single-Z chapter.
Backup files first.
"""
import json, os, shutil

ROOT = os.path.dirname(os.path.abspath(__file__))
ZONES = os.path.join(ROOT,'DT_Moria_Zones.json')
LMS = os.path.join(ROOT,'DT_Moria_Landmarks.json')
ZONES_BAK = os.path.join(ROOT,'DT_Moria_Zones.before_bp_bounds_fix.json')
LMS_BAK = os.path.join(ROOT,'DT_Moria_Landmarks.before_bp_bounds_fix.json')

# Backup
if not os.path.exists(ZONES_BAK):
    shutil.copy2(ZONES, ZONES_BAK); print(f"Backed up zones -> {ZONES_BAK}")
else:
    print(f"Zones backup already exists: {ZONES_BAK}")
if not os.path.exists(LMS_BAK):
    shutil.copy2(LMS, LMS_BAK); print(f"Backed up landmarks -> {LMS_BAK}")
else:
    print(f"Landmarks backup already exists: {LMS_BAK}")

# Load zones
with open(ZONES,'r',encoding='utf-8') as f: zd = json.load(f)

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

def prop_bool(rd, name, default=None):
    p = prop_get(rd, name)
    return p.get('Value', default) if p else default

def intvec_struct(rd, name):
    p = prop_get(rd, name)
    if not p: return None, None
    inner = p.get('Value')
    if isinstance(inner, list) and inner:
        ivp = inner[0]
        v = ivp.get('Value')
        if isinstance(v, dict): return ivp, v
    return None, None

def landmark_handles(rd):
    out = []
    p = prop_get(rd, 'LandmarkHandles')
    if not p: return out
    for entry in p.get('Value', []) or []:
        ep = entry.get('Value', []) or []
        lh = prop_get(ep, 'Landmark')
        if lh:
            inner = lh.get('Value', []) or []
            rn = prop_get(inner, 'RowName')
            if rn: out.append(rn.get('Value'))
    return out

# Identify and modify
rows = find_rows(zd)
modified = []
for r in rows:
    nm = r.get('Name','')
    rd = row_props(r)
    _, ts = intvec_struct(rd, 'TargetSize')
    bpfl = prop_bool(rd,'bPositionFromLandmarks')
    if ts and ts.get('X')==6 and ts.get('Y')==6 and ts.get('Z')==4 and bpfl:
        # Stair/elevator zone candidate. Confirm it has a stair landmark.
        lhs = landmark_handles(rd)
        if any('Stair' in lh or 'Descent' in lh for lh in lhs):
            ts['Z'] = 1
            modified.append((nm, lhs))

# Write back
with open(ZONES,'w',encoding='utf-8') as f:
    json.dump(zd, f, indent=2)

print(f"\nModified {len(modified)} elevator/stair zones (TargetSize.Z 4 -> 1):")
for nm,lhs in modified:
    print(f"  {nm:35s} LMs={lhs}")
