"""Apply targeted fixes for the GetZone() null-deref crash.

Disables LCs identified as crash-likely:
1. Sandbox_PromenadeToMines — malformed enum literal
   (EMorLayoutConnectionZoneRule::Shared instead of EConnectionZoneRule::Shared)
2. Sandbox_FloorD5_Internal — DestinationLandmark Chapter4.DurinsForge is
   ALSO hosted by DurinsCapital (ZoneSet=Moria), which is not present in the
   active SandboxSmall world; engine GetZone() may resolve to that zone and
   return null.

Backup: DT_Moria_LayoutConnections.before_endpoint_host_fix.json
"""
import json, os, shutil
ROOT = os.path.dirname(os.path.abspath(__file__))
os.chdir(ROOT)

SRC = 'DT_Moria_LayoutConnections.json'
BAK = 'DT_Moria_LayoutConnections.before_endpoint_host_fix.json'

DISABLE = {
    'Sandbox_PromenadeToMines': 'malformed enum literal EMorLayoutConnectionZoneRule::Shared (every other LC uses EConnectionZoneRule::*)',
    'Sandbox_FloorD5_Internal': 'DestLandmark Chapter4.DurinsForge anchored on DurinsCapital (Moria zoneset, not in active SS world) — GetZone may null',
}

if not os.path.exists(BAK):
    shutil.copy(SRC, BAK)
    print(f'Backup written: {BAK}')
else:
    print(f'Backup already exists: {BAK}')

doc = json.load(open(SRC, encoding='utf-8'))
rows = doc['Exports'][0]['Table']['Data']

def fp(v, n):
    for p in v or []:
        if isinstance(p, dict) and p.get('Name') == n: return p
    return None

changed = 0
for r in rows:
    if r['Name'] not in DISABLE: continue
    es = fp(r.get('Value', []), 'EnabledState')
    if not es:
        # add one
        r['Value'].append({'$type': '...', 'Name': 'EnabledState', 'Value': 'ERowEnabledState::Disabled'})
        changed += 1
        print(f'+ {r["Name"]}: added EnabledState=Disabled')
    else:
        cur = str(es.get('Value','')).split('::')[-1]
        if cur != 'Disabled':
            es['Value'] = 'ERowEnabledState::Disabled'
            changed += 1
            print(f'+ {r["Name"]}: EnabledState {cur} -> Disabled  ({DISABLE[r["Name"]]})')
        else:
            print(f'  {r["Name"]}: already Disabled')

with open(SRC, 'w', encoding='utf-8') as f:
    json.dump(doc, f, indent=2)
print(f'Wrote {SRC}.  Rows changed: {changed}')
