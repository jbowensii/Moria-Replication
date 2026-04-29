"""
Create a sandbox-safe ElvenQuarter landmark pair that reference each other,
so both bubbles' connection slots resolve instead of opening into the void.
"""
import copy
import json
from pathlib import Path

HERE = Path(__file__).parent
LM_PATH = HERE / 'DT_Moria_Landmarks.json'
ZN_PATH = HERE / 'DT_Moria_Zones.json'


def set_guaranteed_connections(row, tag_list):
    gc = next((p for p in row['Value'] if p.get('Name') == 'GuaranteedConnections'), None)
    if gc is None:
        raise SystemExit('GuaranteedConnections prop missing')
    existing = gc.get('Value', [])
    if existing:
        template = copy.deepcopy(existing[0])
    else:
        template = {
            '$type': 'UAssetAPI.PropertyTypes.Structs.StructPropertyData, UAssetAPI',
            'StructType': 'GameplayTag',
            'SerializeNone': True,
            'StructGUID': '{00000000-0000-0000-0000-000000000000}',
            'SerializationControl': 'NoExtension',
            'Operation': 'None',
            'Name': 'GuaranteedConnections',
            'ArrayIndex': 0, 'IsZero': False,
            'PropertyTagFlags': 'None', 'PropertyTagExtensions': 'NoExtension',
            'Value': [{
                '$type': 'UAssetAPI.PropertyTypes.Objects.NamePropertyData, UAssetAPI',
                'Name': 'TagName',
                'ArrayIndex': 0, 'IsZero': False,
                'PropertyTagFlags': 'None', 'PropertyTagExtensions': 'NoExtension',
                'Value': ''
            }]
        }
    new_items = []
    for tag in tag_list:
        item = copy.deepcopy(template)
        for sub in item.get('Value', []) or []:
            if isinstance(sub, dict) and sub.get('Name') == 'TagName':
                sub['Value'] = tag
                break
        new_items.append(item)
    gc['Value'] = new_items
    gc.pop('DummyStruct', None)


# --- Landmarks ---
lm_data = json.loads(LM_PATH.read_text(encoding='utf-8'))
lm_rows = lm_data['Exports'][0]['Table']['Data']
lm_by_name = {r['Name']: r for r in lm_rows}

if 'Sandbox.ElvenQuarterEntrance' in lm_by_name:
    print('Sandbox.ElvenQuarterEntrance exists — updating in place.')
    new_entrance = lm_by_name['Sandbox.ElvenQuarterEntrance']
else:
    print('Cloning Chapter2.ElvenQuarterEntrance -> Sandbox.ElvenQuarterEntrance')
    new_entrance = copy.deepcopy(lm_by_name['Chapter2.ElvenQuarterEntrance'])
    new_entrance['Name'] = 'Sandbox.ElvenQuarterEntrance'
    lm_rows.append(new_entrance)

set_guaranteed_connections(new_entrance,
                            ['World.Landmark.Sandbox.ElvenQuarterPromenade'])
print('  Sandbox.ElvenQuarterEntrance conns -> [Sandbox.ElvenQuarterPromenade]')

existing_prom = lm_by_name['Sandbox.ElvenQuarterPromenade']
set_guaranteed_connections(existing_prom,
                            ['World.Landmark.Sandbox.ElvenQuarterEntrance'])
print('  Sandbox.ElvenQuarterPromenade conns -> [Sandbox.ElvenQuarterEntrance]')

LM_PATH.write_text(json.dumps(lm_data, indent=2), encoding='utf-8')
print(f'\nSaved {LM_PATH.name} ({len(lm_rows)} rows)')


# --- Zone rewire ---
zn_data = json.loads(ZN_PATH.read_text(encoding='utf-8'))
zn_rows = zn_data['Exports'][0]['Table']['Data']

target = next(r for r in zn_rows if r['Name'] == 'Sandbox_Small_ElvenQuarter_B')
lh = next(p for p in target['Value'] if p.get('Name') == 'LandmarkHandles')

source_zone = next(r for r in zn_rows if r['Name'] == 'Sandbox_Small_Suburban_A_Westgate')
src_lh = next(p for p in source_zone['Value'] if p.get('Name') == 'LandmarkHandles')
entry_template = copy.deepcopy(src_lh['Value'][0])


def build_entry(lm_rowname, placement='Fixed', extended=False):
    e = copy.deepcopy(entry_template)
    for sub in e.get('Value', []):
        if not isinstance(sub, dict):
            continue
        n = sub.get('Name')
        if n == 'Landmark':
            for it in sub.get('Value', []):
                if isinstance(it, dict) and it.get('Name') == 'RowName':
                    it['Value'] = lm_rowname
        elif n == 'Placement':
            cur = sub.get('Value', '')
            prefix = cur.split('::', 1)[0] if '::' in cur else 'EZoneBubblePlacement'
            sub['Value'] = f'{prefix}::{placement}'
        elif n == 'bExtendedConnectivityLandmark':
            sub['Value'] = bool(extended)
    return e


lh['Value'] = [
    build_entry('Sandbox.ElvenQuarterEntrance',  'Fixed', False),
    build_entry('Sandbox.ElvenQuarterPromenade', 'Fixed', False),
]
lh.pop('DummyStruct', None)

ZN_PATH.write_text(json.dumps(zn_data, indent=2), encoding='utf-8')
print(f'Saved {ZN_PATH.name}')


# --- Verify ---
print('\n=== Verification ===')
lm2 = json.loads(LM_PATH.read_text(encoding='utf-8'))
rows = lm2['Exports'][0]['Table']['Data']
for name in ['Sandbox.ElvenQuarterEntrance', 'Sandbox.ElvenQuarterPromenade']:
    r = next(x for x in rows if x['Name'] == name)
    gc = next(p for p in r['Value'] if p.get('Name') == 'GuaranteedConnections')
    conns = []
    for item in gc.get('Value', []) or []:
        for sub in item.get('Value', []) or []:
            if isinstance(sub, dict) and sub.get('Name') == 'TagName':
                conns.append(str(sub.get('Value', '')))
    print(f'  {name}  conns={conns}')

zn2 = json.loads(ZN_PATH.read_text(encoding='utf-8'))
zt = next(r for r in zn2['Exports'][0]['Table']['Data']
          if r['Name'] == 'Sandbox_Small_ElvenQuarter_B')
lhz = next(p for p in zt['Value'] if p.get('Name') == 'LandmarkHandles')
print('\n  Sandbox_Small_ElvenQuarter_B.LandmarkHandles:')
for e in lhz.get('Value', []):
    for sub in e.get('Value', []):
        if isinstance(sub, dict) and sub.get('Name') == 'Landmark':
            for it in sub.get('Value', []):
                if isinstance(it, dict) and it.get('Name') == 'RowName':
                    print(f'    -> {it.get("Value", "")}')
