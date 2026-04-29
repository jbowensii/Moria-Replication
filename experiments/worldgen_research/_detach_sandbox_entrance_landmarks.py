"""
Detach every Sandbox.*Entrance landmark from every SandboxSmall zone.

  - Touches only SandboxSmall zones (campaign/Moria zones untouched — reference only)
  - Removes each matching entry from the zone's LandmarkHandles[] array
  - Preserves DummyStruct template when an array becomes empty (UAssetGUI quirk)
  - Leaves the landmark rows themselves alone in DT_Moria_Landmarks

Run from Moria-Replication root or with absolute paths.
"""
import copy
import json
from pathlib import Path

HERE = Path(__file__).parent
ZN_PATH = HERE / 'DT_Moria_Zones.json'
LM_PATH = HERE / 'DT_Moria_Landmarks.json'


def find_prop(row_value, name):
    for p in row_value or []:
        if isinstance(p, dict) and p.get('Name') == name:
            return p
    return None


def get_enum(prop):
    v = prop.get('Value', '') if prop else ''
    return v.split('::', 1)[1] if '::' in str(v) else str(v)


def get_rowname(prop):
    if prop is None:
        return ''
    for it in prop.get('Value', []) or []:
        if isinstance(it, dict) and it.get('Name') == 'RowName':
            return str(it.get('Value', ''))
    return ''


# 1. Enumerate Sandbox.*Entrance landmarks (defensive — handles both
#    "Entrance" and any typo variant "Enterance")
lm_rows = json.loads(LM_PATH.read_text(encoding='utf-8'))['Exports'][0]['Table']['Data']
entrance_landmarks = set()
for r in lm_rows:
    name = r.get('Name', '')
    if name.startswith('Sandbox.') and ('Entrance' in name or 'Enterance' in name):
        entrance_landmarks.add(name)
print('Sandbox entrance landmarks to detach:')
for n in sorted(entrance_landmarks):
    print(f'  {n}')
print()

# 2. Walk SandboxSmall zones and strip matching entries
zn_data = json.loads(ZN_PATH.read_text(encoding='utf-8'))
zn_rows = zn_data['Exports'][0]['Table']['Data']
total_detached = 0
report = []

for r in zn_rows:
    zs = get_enum(find_prop(r['Value'], 'ZoneSet'))
    if zs != 'SandboxSmall':
        continue
    lh = find_prop(r['Value'], 'LandmarkHandles')
    if lh is None:
        continue
    entries = lh.get('Value', []) or []
    kept, removed = [], []
    for e in entries:
        if not isinstance(e, dict):
            kept.append(e); continue
        lm_ref = ''
        for sub in e.get('Value', []) or []:
            if isinstance(sub, dict) and sub.get('Name') == 'Landmark':
                lm_ref = get_rowname(sub)
                break
        if lm_ref in entrance_landmarks:
            removed.append(lm_ref)
        else:
            kept.append(e)
    if removed:
        # Preserve DummyStruct if the array would now be empty AND we have
        # a removed entry to use as template shape.
        if not kept and 'DummyStruct' not in lh:
            lh['DummyStruct'] = copy.deepcopy(entries[0])
        lh['Value'] = kept
        report.append((r['Name'], removed, len(kept)))
        total_detached += len(removed)

for zone_name, removed, remaining in report:
    print(f'  {zone_name}')
    for lm in removed:
        print(f'    - detached {lm}')
    print(f'    ({remaining} landmarks remaining)')

print(f'\nTotal: {total_detached} entries detached across '
      f'{len(report)} sandbox zone(s)')

ZN_PATH.write_text(json.dumps(zn_data, indent=2), encoding='utf-8')
print(f'\nSaved {ZN_PATH.name}')
