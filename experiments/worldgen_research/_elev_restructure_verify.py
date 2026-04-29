"""Verify post-restructure: BuildValidator + topology summary."""
import importlib.util
import json
import sys
from pathlib import Path

WGR = Path(__file__).resolve().parent
SCRIPTS = WGR.parent.parent / 'scripts'

spec = importlib.util.spec_from_file_location(
    'sandbox_zone_editor', SCRIPTS / 'SandboxZoneEditor.py')
mod = importlib.util.module_from_spec(spec)
sys.modules['sandbox_zone_editor'] = mod
spec.loader.exec_module(mod)

DataTableDoc = mod.DataTableDoc
BuildValidator = mod.BuildValidator
DATATABLES = mod.DATATABLES

docs = {}
for key, (fname, stem, label) in DATATABLES.items():
    if key == 'strings':
        continue
    p = WGR / fname
    if not p.exists():
        continue
    d = DataTableDoc(key, p, stem, label)
    if d.load():
        docs[key] = d

print(f'loaded {len(docs)} docs')
bv = BuildValidator(docs)
issues = bv.run()
errors = [i for i in issues if i.severity == 'error']
warnings = [i for i in issues if i.severity == 'warning']
print(f'  total issues: {len(issues)}')
print(f'  errors:       {len(errors)}')
print(f'  warnings:     {len(warnings)}')
from collections import Counter
by_check = Counter(i.check for i in issues)
print('by check:')
for k, c in by_check.most_common():
    print(f'  {k}: {c}')
print()
print('=== sample issues (first 30) ===')
for i in issues[:30]:
    print(f'  [{i.severity}] {i.check}: {i.message}')

# === Topology summary ===
print()
print('=== Topology summary ===')
def gp(v, n):
    for p in v or []:
        if isinstance(p, dict) and p.get('Name') == n:
            return p
    return None
def gv(v, n):
    p = gp(v, n)
    return p.get('Value') if p else None

with open(WGR / 'DT_Moria_Zones.json','r',encoding='utf-8') as f:
    zd = json.load(f)
with open(WGR / 'DT_Moria_Chapters.json','r',encoding='utf-8') as f:
    cd = json.load(f)

z_data = zd['Exports'][0]['Table']['Data']
c_data = cd['Exports'][0]['Table']['Data']

elev_zones = [r for r in z_data if r.get('Name','').startswith('Sandbox_Small_Elevator_')]
print(f'elevator zones now: {len(elev_zones)}')
floor_to_zones = {}
for e in elev_zones:
    v = e['Value']
    chap_rn = gv(gv(v, 'Chapter'), 'RowName')
    addl = gv(v, 'AdditionalChapters') or []
    addl_rns = [gv(a.get('Value'), 'RowName') for a in addl]
    lhs = gv(v, 'LandmarkHandles') or []
    lh_info = []
    for lh in lhs:
        lhv = lh.get('Value', [])
        lm_rn = gv(gv(lhv, 'Landmark'), 'RowName')
        ext = gv(lhv, 'bExtendedConnectivityLandmark')
        place = gv(lhv, 'Placement')
        lh_info.append((lm_rn, place, ext))
    pos = gv(gv(v, 'Position') or [{}], 'X')
    state = gv(v, 'EnabledState')
    print(f'  {e["Name"]}  primary={chap_rn} addl={addl_rns} LH={lh_info} state={state}')
    floor_to_zones.setdefault(chap_rn, []).append(e['Name'] + ' (primary)')
    for a in addl_rns:
        floor_to_zones.setdefault(a, []).append(e['Name'] + ' (additional)')

# Chapter row counts
ss_anchored = [r for r in c_data if r.get('Name','').startswith('SandboxSmall-Chapter')]
levels = [r for r in ss_anchored if '.Level' in r['Name'] or '.Deep' in r['Name']]
elev_rows = [r for r in ss_anchored if '.Elevator' in r['Name']]
others = [r for r in ss_anchored if r not in levels and r not in elev_rows]
print(f'\n=== chapter row counts ===')
print(f'  level identity rows (.LevelN/.DeepN): {len(levels)}')
print(f'  elevator anchored rows (.Elevator_*): {len(elev_rows)}')
print(f'  other anchored rows: {len(others)}')

# Zone counts
ss_live = []
for r in z_data:
    v = r.get('Value', [])
    if gv(v, 'ZoneSet') == 'EZoneSet::SandboxSmall' and gv(v, 'EnabledState') == 'ERowEnabledState::Live':
        ss_live.append(r['Name'])
non_elev = [n for n in ss_live if not n.startswith('Sandbox_Small_Elevator_')]
elev = [n for n in ss_live if n.startswith('Sandbox_Small_Elevator_')]
print(f'\n=== zone counts ===')
print(f'  Live SS zones: {len(ss_live)}  (non-elev={len(non_elev)}, elev={len(elev)})')

# Per-floor topology
print(f'\n=== per-floor topology ===')
floor_order = ['SandboxSmall-Chapter01.Level1','SandboxSmall-Chapter02.Level2',
               'SandboxSmall-Chapter03.Level3','SandboxSmall-Chapter04.Level4',
               'SandboxSmall-Chapter05.Level5','SandboxSmall-Chapter06.Level6',
               'SandboxSmall-Chapter07.Level7','SandboxSmall-Chapter14.Deep1',
               'SandboxSmall-Chapter13.Deep2','SandboxSmall-Chapter12.Deep3',
               'SandboxSmall-Chapter11.Deep4','SandboxSmall-Chapter10.Deep5',
               'SandboxSmall-Chapter09.Deep6','SandboxSmall-Chapter08.Deep7']
for fl in floor_order:
    print(f'  {fl}:')
    for entry in floor_to_zones.get(fl, []):
        print(f'    - {entry}')
