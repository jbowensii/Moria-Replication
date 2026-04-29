"""Routing audit: pre-state for Tasks A-D before apply.

Reports:
  Task A: ext flag state on the two LandmarkHandles to flip
  Task B: which 6 cross-elevator handoff connections exist / missing
  Task C: GC counts on stair landmarks
  Task D: per-layer non-stair Live SS landmarks reachable from each elevator
"""
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
def get_intvec(row, name):
    p = props(row).get(name)
    if not p: return None
    for sp in p.get('Value', []):
        if isinstance(sp, dict) and sp.get('$type', '').endswith('IntVectorPropertyData, UAssetAPI'):
            v = sp.get('Value', {})
            return (v.get('X'), v.get('Y'), v.get('Z'))
    return None
def get_array(row, name):
    p = props(row).get(name)
    return p.get('Value', []) if p else []
def get_rowname(row, name):
    p = props(row).get(name)
    if not p: return None
    for sp in p.get('Value', []):
        if isinstance(sp, dict) and sp.get('Name') == 'RowName':
            return sp.get('Value')
    return None
def is_live(row):
    p = props(row).get('EnabledState')
    e = p.get('Value') if p else None
    return e is None or 'Live' in str(e)

zone_rows = rows(zones); lm_rows = rows(landmarks); conn_rows = rows(connections); chap_rows = rows(chapters)
lm_by = {r['Name']: r for r in lm_rows}
zone_by = {r['Name']: r for r in zone_rows}

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
                    if isinstance(q, dict) and q.get('Name') == 'RowName':
                        lm_ref = q.get('Value')
            elif nm == 'bExtendedConnectivityLandmark':
                ext = sp.get('Value')
            elif nm == 'Placement':
                placement = sp.get('Value')
        out.append({'lm': lm_ref, 'ext': ext, 'placement': placement})
    return out

def is_ss_zone(z):
    return z['Name'].startswith('Sandbox_Small_')

ss_zones = [z for z in zone_rows if is_ss_zone(z) and is_live(z)]

# --- Task A audit ---
print("=== TASK A: ext flag audit ===")
targets = [('Sandbox_Small_Elevator_G', 'Sandbox.SeventhStair'),
           ('Sandbox_Small_Elevator_E', 'Sandbox.LowerDescent')]
for zname, lm in targets:
    z = zone_by.get(zname)
    if not z: print(f"  MISSING zone {zname}"); continue
    for h in lm_handles(z):
        if h['lm'] == lm:
            print(f"  {zname} :: {lm}  ext={h['ext']}  placement={h['placement']}  -> SHOULD FLIP TO True")

# --- Task B audit ---
print("\n=== TASK B: cross-elevator handoff connection audit ===")
needed = [
    ('Sandbox_E_LowerDescent_to_F_CrystalDescent', 'Sandbox.LowerDescent', 'Sandbox.CrystalDescent'),
    ('Sandbox_F_CrystalDescent_to_G_SeventhStair', 'Sandbox.CrystalDescent', 'Sandbox.SeventhStair'),
    ('Sandbox_G_SeventhStair_to_C_SecondStair', 'Sandbox.SeventhStair', 'Sandbox.SecondStair'),
    ('Sandbox_C_SecondStair_to_H_NinthStair', 'Sandbox.SecondStair', 'Sandbox.NinthStair'),
    ('Sandbox_H_TenthStair_to_B_FirstStair', 'Sandbox.TenthStair', 'Sandbox.FirstStair'),
    ('Sandbox_B_FourthStair_to_D_ThirdStair', 'Sandbox.FourthStair', 'Sandbox.ThirdStair'),
]
existing_names = {r['Name'] for r in conn_rows}
for nm, ol, dl in needed:
    print(f"  {nm:50s} present={nm in existing_names}  origin={ol}  dest={dl}")
    # Check if any other connection already wires this pair
    for c in conn_rows:
        if not is_live(c): continue
        co = get_rowname(c, 'OriginLandmark'); cd = get_rowname(c, 'DestinationLandmark')
        if (co == ol and cd == dl) or (co == dl and cd == ol):
            print(f"     existing pair via: {c['Name']}")

# Verify all dest landmarks exist
print("\n  Landmark existence check:")
all_lm_refs = set();
for nm, ol, dl in needed:
    all_lm_refs.add(ol); all_lm_refs.add(dl)
for lm in sorted(all_lm_refs):
    print(f"    {lm}: present={lm in lm_by}")

# --- Task C audit ---
print("\n=== TASK C: stair GC counts ===")
stair_lms = ['Sandbox.LowerDescent','Sandbox.CrystalDescent','Sandbox.SeventhStair',
             'Sandbox.SecondStair','Sandbox.NinthStair','Sandbox.TenthStair',
             'Sandbox.FirstStair','Sandbox.FourthStair','Sandbox.ThirdStair',
             'Sandbox.SixthStair','Sandbox.EighthStair','Sandbox.EleventhStair']
for lm in stair_lms:
    r = lm_by.get(lm)
    if not r: print(f"  MISSING {lm}"); continue
    gc = get_array(r, 'GuaranteedConnections')
    print(f"  {lm:35s}  GC count={len(gc)}")

# --- Task D audit ---
print("\n=== TASK D: per-elevator/floor non-stair landmark candidates ===")
# Build map: lm -> Z (BasePosition Z)
def lm_z(name):
    r = lm_by.get(name)
    if not r: return None
    bp = get_intvec(r, 'BasePosition')
    return bp[2] if bp else None

# Stair anchors per elevator (anchor LM and Z)
elev_anchors = {
    'Sandbox_Small_Elevator_E': [('Sandbox.LowerDescent', 0)],
    'Sandbox_Small_Elevator_F': [('Sandbox.CrystalDescent', 1)],
    'Sandbox_Small_Elevator_G': [('Sandbox.SeventhStair', 4)],
    'Sandbox_Small_Elevator_C': [('Sandbox.SecondStair', 13)],
    'Sandbox_Small_Elevator_H': [('Sandbox.NinthStair', 14), ('Sandbox.TenthStair', 17)],
    'Sandbox_Small_Elevator_B': [('Sandbox.FirstStair', 18), ('Sandbox.FourthStair', 22)],
    'Sandbox_Small_Elevator_D': [('Sandbox.ThirdStair', 23), ('Sandbox.SixthStair', 27),
                                 ('Sandbox.EighthStair', 28), ('Sandbox.EleventhStair', 29)],
}

# Build per-Z list of non-stair Live SS landmarks that exist on each layer.
# Strategy: for each Live SS zone (non-elevator) and each LandmarkHandle on it, capture LM and its Z.
non_stair_by_z = defaultdict(list)  # z -> list of (lm_name, host_zone)
stair_set = set(stair_lms)

for z in ss_zones:
    if 'Elevator' in z['Name']: continue
    for h in lm_handles(z):
        lm = h['lm']
        if not lm or lm == 'None': continue
        if lm in stair_set: continue
        zv = lm_z(lm)
        if zv is None: continue
        non_stair_by_z[zv].append((lm, z['Name']))

print("\nNon-stair Live SS landmarks by Z-layer:")
for zv in sorted(non_stair_by_z):
    print(f"  Z={zv}: {non_stair_by_z[zv]}")

# For each elevator anchor Z, recommend Task D wire
print("\nProposed Task D internal connections per elevator anchor:")
proposals = []
for ez, anchors in elev_anchors.items():
    for anchor_lm, anchor_z in anchors:
        cands = non_stair_by_z.get(anchor_z, [])
        if cands:
            cand_lm, cand_zone = cands[0]
            label = f"Z{anchor_z}"
            new_name = f"Sandbox_Floor{label}_Internal_{anchor_lm.replace('Sandbox.','')}"
            print(f"  {ez} anchor {anchor_lm} (Z={anchor_z}) -> {cand_lm} (host {cand_zone})  name={new_name}")
            proposals.append({'name': new_name, 'origin': anchor_lm, 'dest': cand_lm, 'z': anchor_z})
        else:
            print(f"  {ez} anchor {anchor_lm} (Z={anchor_z}) -> NO non-stair candidate on this layer")

# Save proposals
with open(os.path.join(ROOT, '_routing_proposals.json'), 'w', encoding='utf-8') as f:
    json.dump({'task_d': proposals, 'task_b': needed}, f, indent=2)

# --- Coverage baseline ---
print("\n=== Coverage baseline (Live SS connections, endpoints touching each Z) ===")
def is_live_ss_conn(c):
    p = props(c).get('ZoneSet')
    zs = p.get('Value', '') if p else ''
    return 'SandboxSmall' in str(zs) and is_live(c)

ep_count = defaultdict(int)
for c in conn_rows:
    if not is_live_ss_conn(c): continue
    o = get_rowname(c, 'OriginLandmark'); d = get_rowname(c, 'DestinationLandmark')
    oz = lm_z(o) if o and o != 'None' else None
    dz = lm_z(d) if d and d != 'None' else None
    if oz is not None: ep_count[oz] += 1
    if dz is not None: ep_count[dz] += 1

floors = {'D-7':0,'D-6':1,'D-5':4,'D-4':9,'D-3':10,'D-2':13,'D-1':14,'Lv-1':17,'Lv-2':18,'Lv-3':19,'Lv-4':22,'Lv-5':23,'Lv-6':27,'Lv-7':29}
for fl, zv in floors.items():
    print(f"  {fl} (Z={zv}): {ep_count.get(zv,0)} endpoints")

print("\nAudit complete. Proposals written to _routing_proposals.json")
