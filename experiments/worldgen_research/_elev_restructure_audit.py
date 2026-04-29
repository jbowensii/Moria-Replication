"""Audit pre-state of elevators, per-elevator chapter rows, and stair landmarks."""
import json
from pathlib import Path

WGR = Path(__file__).resolve().parent

def load(name):
    with open(WGR / name, 'r', encoding='utf-8') as f:
        return json.load(f)

def get_prop(values, name):
    for p in values or []:
        if isinstance(p, dict) and p.get('Name') == name:
            return p
    return None

def prop_value(values, name):
    p = get_prop(values, name)
    return p.get('Value') if p else None

zones = load('DT_Moria_Zones.json')
chaps = load('DT_Moria_Chapters.json')
lms = load('DT_Moria_Landmarks.json')

zdata = zones['Exports'][0]['Table']['Data']
cdata = chaps['Exports'][0]['Table']['Data']
ldata = lms['Exports'][0]['Table']['Data']

print('=== Section 1: Current Sandbox_Small_Elevator_* zones ===')
elev_zones = [r for r in zdata if r.get('Name','').startswith('Sandbox_Small_Elevator_')]
print(f'count: {len(elev_zones)}')
for e in elev_zones:
    name = e['Name']
    v = e['Value']
    chapter = prop_value(v, 'Chapter')
    chapter_rn = prop_value(chapter, 'RowName') if chapter else None
    addl = prop_value(v, 'AdditionalChapters') or []
    addl_rns = []
    for a in addl:
        rn = prop_value(a.get('Value'), 'RowName')
        addl_rns.append(rn)
    pos = prop_value(v, 'Position')
    tgt = prop_value(v, 'TargetSize')
    pfl = prop_value(v, 'bPositionFromLandmarks')
    pft = prop_value(v, 'bPositionFromZoneTable')
    state = prop_value(v, 'EnabledState')
    lhs = prop_value(v, 'LandmarkHandles') or []
    lh_info = []
    for lh in lhs:
        lhv = lh.get('Value', [])
        lm = prop_value(lhv, 'Landmark')
        lm_rn = prop_value(lm, 'RowName') if lm else None
        ext = prop_value(lhv, 'bExtendedConnectivityLandmark')
        lh_info.append((lm_rn, ext))
    print(f'  {name}')
    print(f'    Chapter={chapter_rn} Addl={addl_rns}')
    print(f'    State={state} Pos={pos} Tgt={tgt} pPFL={pfl} pPFZT={pft}')
    print(f'    LHs ({len(lhs)}): {lh_info}')

print()
print('=== Section 2: SandboxSmall-Chapter##.Elevator_* chapter rows ===')
elev_chap_rows = [r for r in cdata if 'Elevator' in r.get('Name','') and r.get('Name','').startswith('SandboxSmall-Chapter')]
print(f'count: {len(elev_chap_rows)}')
for r in elev_chap_rows:
    print(f'  {r["Name"]}')

# Also list all SandboxSmall-Chapter##.* rows so we can confirm what stays
print()
print('=== Section 2b: ALL SandboxSmall-Chapter##.* rows (anchored) ===')
ss_anchored = [r for r in cdata if r.get('Name','').startswith('SandboxSmall-Chapter')]
print(f'count: {len(ss_anchored)}')
for r in ss_anchored:
    n = r['Name']
    is_level = '.Level' in n or '.Deep' in n
    is_elev = '.Elevator' in n
    flag = 'LEVEL' if is_level else ('ELEV' if is_elev else 'ANCHOR')
    print(f'  [{flag}] {n}')

print()
print('=== Section 3: Stair landmarks ===')
stair_names = ['Sandbox.FirstStair','Sandbox.SecondStair','Sandbox.ThirdStair','Sandbox.FourthStair',
               'Sandbox.SixthStair','Sandbox.SeventhStair','Sandbox.EighthStair','Sandbox.NinthStair',
               'Sandbox.TenthStair','Sandbox.EleventhStair','Sandbox.CrystalDescent','Sandbox.LowerDescent']
for sn in stair_names:
    found = next((r for r in ldata if r.get('Name')==sn), None)
    if not found:
        print(f'  MISSING: {sn}')
        continue
    v = found['Value']
    bp = prop_value(v, 'BasePosition')
    state = prop_value(v, 'EnabledState')
    print(f'  {sn}  State={state} BasePos={bp}')

print()
print('=== Section 4: Counts ===')
print(f'  total zones: {len(zdata)}')
print(f'  SS zones (any state): {len([r for r in zdata if "ZoneSet" in str(r)])}')
ss_zones_live = []
for r in zdata:
    v = r.get('Value', [])
    zs = prop_value(v, 'ZoneSet')
    state = prop_value(v, 'EnabledState')
    if zs == 'EZoneSet::SandboxSmall' and state == 'ERowEnabledState::Live':
        ss_zones_live.append(r['Name'])
print(f'  Live SS zones: {len(ss_zones_live)}')
non_elev_live = [n for n in ss_zones_live if not n.startswith('Sandbox_Small_Elevator_')]
elev_live = [n for n in ss_zones_live if n.startswith('Sandbox_Small_Elevator_')]
print(f'    non-elev live SS: {len(non_elev_live)}')
print(f'    elev live SS: {len(elev_live)}: {elev_live}')

print(f'  total chapters: {len(cdata)}')
print(f'  total landmarks: {len(ldata)}')
