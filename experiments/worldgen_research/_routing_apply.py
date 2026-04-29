"""Apply Tasks A-D for the SandboxSmall routing fix.

Task A: flip 2 ext flags on LandmarkHandles in DT_Moria_Zones.json
Task B: append 6 cross-elevator handoff LayoutConnection rows
Task C: add GuaranteedConnections (TagName entries) to 12 stair landmarks
Task D: append per-floor internal LayoutConnection rows where a non-stair landmark exists
"""
import json, os, copy
from collections import defaultdict

ROOT = os.path.dirname(os.path.abspath(__file__))
def load(n):
    with open(os.path.join(ROOT, n), 'r', encoding='utf-8') as f: return json.load(f)
def save(n, d):
    with open(os.path.join(ROOT, n), 'w', encoding='utf-8') as f: json.dump(d, f, indent=2)

zones = load('DT_Moria_Zones.json')
landmarks = load('DT_Moria_Landmarks.json')
connections = load('DT_Moria_LayoutConnections.json')

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

zone_rows = rows(zones); lm_rows = rows(landmarks); conn_rows = rows(connections)
zone_by = {r['Name']: r for r in zone_rows}
lm_by = {r['Name']: r for r in lm_rows}

# =================== TASK A ===================
print("=== TASK A: flip ext flags ===")
flips = [('Sandbox_Small_Elevator_G', 'Sandbox.SeventhStair'),
         ('Sandbox_Small_Elevator_E', 'Sandbox.LowerDescent')]
flipped = 0
for zname, target_lm in flips:
    z = zone_by[zname]
    arr = get_array(z, 'LandmarkHandles')
    for entry in arr:
        if not isinstance(entry, dict): continue
        sub = entry.get('Value', [])
        lm_ref = None
        for sp in sub:
            if isinstance(sp, dict) and sp.get('Name') == 'Landmark':
                for q in sp.get('Value', []):
                    if isinstance(q, dict) and q.get('Name') == 'RowName':
                        lm_ref = q.get('Value')
        if lm_ref == target_lm:
            for sp in sub:
                if isinstance(sp, dict) and sp.get('Name') == 'bExtendedConnectivityLandmark':
                    print(f"  {zname} :: {target_lm}  {sp.get('Value')} -> True")
                    sp['Value'] = True
                    flipped += 1
print(f"  Flipped {flipped} ext flags")

# =================== TASK B + D: append LayoutConnection rows ===================
# Use Sandbox_ElvenEntranceToPromenade as Live SS LandmarkInterface template

def find_template():
    for r in conn_rows:
        if r['Name'] == 'Sandbox_ElvenEntranceToPromenade':
            return r
    raise RuntimeError("Template not found")

template = find_template()

def make_row(name, origin_lm, dest_lm):
    new = copy.deepcopy(template)
    new['Name'] = name
    for p in new['Value']:
        nm = p.get('Name')
        if nm == 'OriginLandmark':
            for q in p.get('Value', []):
                if q.get('Name') == 'RowName':
                    q['Value'] = origin_lm
        elif nm == 'DestinationLandmark':
            for q in p.get('Value', []):
                if q.get('Name') == 'RowName':
                    q['Value'] = dest_lm
        elif nm == 'OriginZone':
            for q in p.get('Value', []):
                if q.get('Name') == 'RowName':
                    q['Value'] = 'None'
        elif nm == 'DestinationZone':
            for q in p.get('Value', []):
                if q.get('Name') == 'RowName':
                    q['Value'] = 'None'
        elif nm == 'ZoneSet':
            p['Value'] = 'EZoneSet::SandboxSmall'
        elif nm == 'EnabledState':
            p['Value'] = 'ERowEnabledState::Live'
    return new

# --- Task B rows ---
print("\n=== TASK B: cross-elevator handoff connections ===")
task_b_rows = [
    ('Sandbox_E_LowerDescent_to_F_CrystalDescent', 'Sandbox.LowerDescent',  'Sandbox.CrystalDescent'),
    ('Sandbox_F_CrystalDescent_to_G_SeventhStair', 'Sandbox.CrystalDescent', 'Sandbox.SeventhStair'),
    ('Sandbox_G_SeventhStair_to_C_SecondStair',    'Sandbox.SeventhStair',   'Sandbox.SecondStair'),
    ('Sandbox_C_SecondStair_to_H_NinthStair',      'Sandbox.SecondStair',    'Sandbox.NinthStair'),
    ('Sandbox_H_TenthStair_to_B_FirstStair',       'Sandbox.TenthStair',     'Sandbox.FirstStair'),
    ('Sandbox_B_FourthStair_to_D_ThirdStair',      'Sandbox.FourthStair',    'Sandbox.ThirdStair'),
]
existing_names = {r['Name'] for r in conn_rows}
new_conn_names = []
for name, ol, dl in task_b_rows:
    if name in existing_names:
        print(f"  SKIP existing: {name}")
        continue
    conn_rows.append(make_row(name, ol, dl))
    new_conn_names.append(name)
    print(f"  ADD {name}: {ol} -> {dl}")

# --- Task D rows ---
print("\n=== TASK D: floor-internal connections ===")
# Build per-Z non-stair landmark map
def lm_z(name):
    r = lm_by.get(name)
    if not r: return None
    bp = get_intvec(r, 'BasePosition')
    return bp[2] if bp else None

stair_lms_set = {'Sandbox.LowerDescent','Sandbox.CrystalDescent','Sandbox.SeventhStair',
                 'Sandbox.SecondStair','Sandbox.NinthStair','Sandbox.TenthStair',
                 'Sandbox.FirstStair','Sandbox.FourthStair','Sandbox.ThirdStair',
                 'Sandbox.SixthStair','Sandbox.EighthStair','Sandbox.EleventhStair'}

def is_live(row):
    p = props(row).get('EnabledState')
    e = p.get('Value') if p else None
    return e is None or 'Live' in str(e)

ss_zones_live = [z for z in zone_rows if z['Name'].startswith('Sandbox_Small_') and is_live(z)]

def lm_handles(z):
    arr = get_array(z, 'LandmarkHandles')
    out = []
    for entry in arr:
        if not isinstance(entry, dict): continue
        lm_ref = None
        for sp in entry.get('Value', []):
            if isinstance(sp, dict) and sp.get('Name') == 'Landmark':
                for q in sp.get('Value', []):
                    if isinstance(q, dict) and q.get('Name') == 'RowName':
                        lm_ref = q.get('Value')
        if lm_ref: out.append(lm_ref)
    return out

non_stair_by_z = defaultdict(list)
for z in ss_zones_live:
    if 'Elevator' in z['Name']: continue
    for lm in lm_handles(z):
        if lm in stair_lms_set or lm == 'None': continue
        zv = lm_z(lm)
        if zv is None: continue
        non_stair_by_z[zv].append(lm)

# Floor labels per anchor Z (post-fix Z anchors)
anchors = [
    ('Sandbox.LowerDescent', 0,  'D7'),
    ('Sandbox.CrystalDescent',1, 'D6'),
    ('Sandbox.SeventhStair',  4, 'D5'),
    ('Sandbox.SecondStair',  13, 'D2'),
    ('Sandbox.NinthStair',   14, 'D1'),
    ('Sandbox.TenthStair',   17, 'Lv1bot'),
    ('Sandbox.FirstStair',   18, 'Lv1'),
    ('Sandbox.FourthStair',  22, 'Lv4'),
    ('Sandbox.ThirdStair',   23, 'Lv5'),
    ('Sandbox.SixthStair',   27, 'Lv6'),
    ('Sandbox.EighthStair',  28, 'Lv7'),
    ('Sandbox.EleventhStair',29, 'Lv7top'),
]
task_d_added = []
task_d_skipped = []
for stair_lm, z, label in anchors:
    cands = non_stair_by_z.get(z, [])
    if not cands:
        task_d_skipped.append((stair_lm, z, label))
        print(f"  SKIP Z={z} ({label}) anchor={stair_lm}: no non-stair landmark")
        continue
    cand = cands[0]
    name = f"Sandbox_Floor{label}_Internal"
    if name in existing_names:
        print(f"  SKIP existing: {name}")
        continue
    conn_rows.append(make_row(name, stair_lm, cand))
    new_conn_names.append(name)
    task_d_added.append((name, stair_lm, cand, z))
    print(f"  ADD {name}: {stair_lm} -> {cand}  (Z={z})")

# Update connections NameMap with all new row Names
print("\n--- Updating LayoutConnections NameMap ---")
nm_conn = connections.get('NameMap', [])
nm_conn_set = set(nm_conn)
added_to_nm = 0
for n in new_conn_names:
    if n not in nm_conn_set:
        nm_conn.append(n); nm_conn_set.add(n); added_to_nm += 1
# Also add any landmark RowNames referenced that aren't already
for r in [make_row("dummy","x","y")]: pass  # noop
# Actually scan NEW rows for Name references not yet in NameMap
def collect_names_from_row(row):
    names = set()
    for p in row['Value']:
        nm = p.get('Name')
        if nm in ('OriginLandmark','DestinationLandmark','OriginZone','DestinationZone'):
            for q in p.get('Value', []):
                if q.get('Name') == 'RowName' and q.get('Value') and q['Value'] != 'None':
                    names.add(q['Value'])
    return names
new_rows_added = [r for r in conn_rows if r['Name'] in new_conn_names]
referenced = set()
for r in new_rows_added: referenced.update(collect_names_from_row(r))
for n in referenced:
    if n not in nm_conn_set:
        nm_conn.append(n); nm_conn_set.add(n); added_to_nm += 1
        print(f"   adding referenced name: {n}")
connections['NamesReferencedFromExportDataCount'] = max(connections.get('NamesReferencedFromExportDataCount', 0), len(nm_conn))
print(f"  Connections NameMap: +{added_to_nm} entries -> total {len(nm_conn)}")

# =================== TASK C: GuaranteedConnections ===================
print("\n=== TASK C: stair GuaranteedConnections ===")
gc_map = {
    'Sandbox.LowerDescent':   ['World.Landmark.Sandbox.CrystalDescent'],
    'Sandbox.CrystalDescent': ['World.Landmark.Sandbox.LowerDescent', 'World.Landmark.Sandbox.SeventhStair'],
    'Sandbox.SeventhStair':   ['World.Landmark.Sandbox.CrystalDescent', 'World.Landmark.Sandbox.SecondStair'],
    'Sandbox.SecondStair':    ['World.Landmark.Sandbox.SeventhStair',   'World.Landmark.Sandbox.NinthStair'],
    'Sandbox.NinthStair':     ['World.Landmark.Sandbox.SecondStair',    'World.Landmark.Sandbox.TenthStair'],
    'Sandbox.TenthStair':     ['World.Landmark.Sandbox.NinthStair',     'World.Landmark.Sandbox.FirstStair'],
    'Sandbox.FirstStair':     ['World.Landmark.Sandbox.TenthStair',     'World.Landmark.Sandbox.FourthStair'],
    'Sandbox.FourthStair':    ['World.Landmark.Sandbox.FirstStair',     'World.Landmark.Sandbox.ThirdStair'],
    'Sandbox.ThirdStair':     ['World.Landmark.Sandbox.FourthStair',    'World.Landmark.Sandbox.SixthStair'],
    'Sandbox.SixthStair':     ['World.Landmark.Sandbox.ThirdStair',     'World.Landmark.Sandbox.EighthStair'],
    'Sandbox.EighthStair':    ['World.Landmark.Sandbox.SixthStair',     'World.Landmark.Sandbox.EleventhStair'],
    'Sandbox.EleventhStair':  ['World.Landmark.Sandbox.EighthStair'],
}

def make_gc_entry(tag_name):
    return {
        "$type": "UAssetAPI.PropertyTypes.Structs.StructPropertyData, UAssetAPI",
        "StructType": "GameplayTag",
        "SerializeNone": True,
        "StructGUID": "{00000000-0000-0000-0000-000000000000}",
        "SerializationControl": "NoExtension",
        "Operation": "None",
        "Name": "GuaranteedConnections",
        "ArrayIndex": 0,
        "IsZero": False,
        "PropertyTagFlags": "None",
        "PropertyTagExtensions": "NoExtension",
        "Value": [
            {
                "$type": "UAssetAPI.PropertyTypes.Objects.NamePropertyData, UAssetAPI",
                "Name": "TagName",
                "ArrayIndex": 0,
                "IsZero": False,
                "PropertyTagFlags": "None",
                "PropertyTagExtensions": "NoExtension",
                "Value": tag_name
            }
        ]
    }

gc_added = 0
new_landmark_names = set()
for stair, tags in gc_map.items():
    r = lm_by.get(stair)
    if not r:
        print(f"  MISSING landmark {stair}"); continue
    p = props(r).get('GuaranteedConnections')
    if not p:
        print(f"  WARN {stair} has no GuaranteedConnections property to append to")
        continue
    arr = p.get('Value', [])
    existing_tags = set()
    for e in arr:
        for sp in e.get('Value', []):
            if sp.get('Name') == 'TagName': existing_tags.add(sp.get('Value'))
    for tag in tags:
        if tag in existing_tags:
            print(f"  SKIP existing: {stair} -> {tag}")
            continue
        arr.append(make_gc_entry(tag))
        gc_added += 1
        new_landmark_names.add(tag)
        print(f"  ADD {stair} GC: {tag}")

# Update Landmarks NameMap
print("\n--- Updating Landmarks NameMap ---")
nm_lm = landmarks.get('NameMap', [])
nm_lm_set = set(nm_lm)
lm_added = 0
for n in new_landmark_names:
    if n not in nm_lm_set:
        nm_lm.append(n); nm_lm_set.add(n); lm_added += 1
        print(f"   adding: {n}")
landmarks['NamesReferencedFromExportDataCount'] = max(landmarks.get('NamesReferencedFromExportDataCount', 0), len(nm_lm))
print(f"  Landmarks NameMap: +{lm_added} entries -> total {len(nm_lm)}")

# =================== Save ===================
save('DT_Moria_Zones.json', zones)
save('DT_Moria_Landmarks.json', landmarks)
save('DT_Moria_LayoutConnections.json', connections)

# Summary
summary = {
    'task_a_flipped': flipped,
    'task_b_added': [n for n,_,_ in task_b_rows if n in new_conn_names],
    'task_c_gc_entries_added': gc_added,
    'task_d_added': [{'name':n,'origin':o,'dest':d,'z':z} for n,o,d,z in task_d_added],
    'task_d_skipped_layers': [{'stair':s,'z':z,'label':l} for s,z,l in task_d_skipped],
}
with open(os.path.join(ROOT, '_routing_applied.json'), 'w', encoding='utf-8') as f:
    json.dump(summary, f, indent=2)

print("\n=== APPLY DONE ===")
print(f"  Task A: {flipped} ext flags flipped")
print(f"  Task B: {len(summary['task_b_added'])} cross-elevator rows added")
print(f"  Task C: {gc_added} GC tag entries added across stair landmarks")
print(f"  Task D: {len(task_d_added)} floor-internal rows added; {len(task_d_skipped)} skipped (no candidate)")
