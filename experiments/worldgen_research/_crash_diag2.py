"""_crash_diag2.py — Drill into the real LC zone field and chapter Z-band."""
import json
from pathlib import Path

WGR = Path(__file__).resolve().parent

def load(name):
    with open(WGR / name, 'r', encoding='utf-8') as f:
        d = json.load(f)
    table = d['Exports'][0].get('Table', {})
    rows = table.get('Data', []) if 'Data' in table else (table.get('Value', []) or [])
    return d, rows

_, conns_rows = load('DT_Moria_LayoutConnections.json')
_, chapters_rows = load('DT_Moria_Chapters.json')
_, lm_rows = load('DT_Moria_Landmarks.json')

# Inspect the raw OriginZone field for the template AND a new row.
def find(rows, name):
    return next((r for r in rows if r.get('Name') == name), None)

for n in ('Sandbox_ElvenEntranceToPromenade',
          'Sandbox_E_LowerDescent_to_F_CrystalDescent'):
    r = find(conns_rows, n)
    if not r:
        print(n, '— NOT FOUND')
        continue
    print('\n===', n, '===')
    for fld in ('OriginZone', 'DestinationZone',
                'OriginLandmark', 'DestinationLandmark',
                'ZoneSet', 'EnabledState'):
        for p in r.get('Value', []):
            if isinstance(p, dict) and p.get('Name') == fld:
                print(f'  {fld}: {json.dumps(p, default=str)[:300]}')

# Check SeventhStair landmark for the bExtendedConnectivityLandmark flag
print('\n=== SeventhStair landmark properties ===')
for n in ('Sandbox.SeventhStair',):
    r = find(lm_rows, n)
    if r:
        for p in r.get('Value', []):
            if isinstance(p, dict):
                nm = p.get('Name')
                if nm in ('bExtendedConnectivityLandmark', 'BasePosition', 'GuaranteedConnections'):
                    short = json.dumps(p, default=str)[:400]
                    print(f'  {nm}: {short}')

# Check: does the SeventhStair landmark's row even contain bExtendedConnectivityLandmark?
print('\n=== All keys on Sandbox.SeventhStair ===')
r = find(lm_rows, 'Sandbox.SeventhStair')
if r:
    for p in r.get('Value', []):
        if isinstance(p, dict):
            print(' ', p.get('Name'), '=', repr(p.get('Value'))[:80])

# Chapter row name for Elevator_G
print('\n=== Chapter rows referenced as "Chapter10.Elevator_G" or related ===')
for r in chapters_rows:
    n = r.get('Name', '')
    if 'Elevator' in n or 'chap-10' in n.lower() or 'chapter10' in n.lower():
        # show MinZ/MaxZ + Layer
        kv = {}
        for p in r.get('Value', []):
            if isinstance(p, dict) and p.get('Name') in ('MinZ', 'MaxZ', 'Layer', 'PrimeZ', 'ChapterID'):
                kv[p['Name']] = p.get('Value')
        print(f'  {n}  {kv}')

# Check that the chapter naming style for "SandboxSmall-Chapter10.Elevator_G" matches what the validator expects
print('\n=== Chapter-name styles found in chapters DT (live SS only) ===')
import collections
styles = collections.Counter()
for r in chapters_rows:
    n = r.get('Name', '')
    if not n.startswith('SandboxSmall'): continue
    es = next((p for p in r.get('Value', []) if isinstance(p, dict) and p.get('Name') == 'EnabledState'), None)
    state = str(es.get('Value', '') if es else '').split('::')[-1]
    if state == 'Disabled': continue
    if '-chapter-' in n:
        styles['SandboxSmall-chapter-N'] += 1
    elif '-Chapter' in n:
        styles['SandboxSmall-ChapterNN.X'] += 1
    else:
        styles['other:' + n[:40]] += 1
print('  ', dict(styles))

# Also: list all SandboxSmall live chapters with their Z-band and Layer
print('\n=== All live SandboxSmall chapters MinZ/MaxZ/Layer ===')
for r in chapters_rows:
    n = r.get('Name', '')
    if not n.startswith('SandboxSmall'): continue
    es = next((p for p in r.get('Value', []) if isinstance(p, dict) and p.get('Name') == 'EnabledState'), None)
    state = str(es.get('Value', '') if es else '').split('::')[-1]
    if state == 'Disabled': continue
    kv = {}
    for p in r.get('Value', []):
        if isinstance(p, dict) and p.get('Name') in ('MinZ', 'MaxZ', 'Layer', 'PrimeZ'):
            kv[p['Name']] = p.get('Value')
    print(f'  {n:55s} {kv}')
