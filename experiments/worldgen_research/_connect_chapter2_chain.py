"""
Wire the 3-way landmark chain for chapter 2:

    Suburban_C  ===  ElvenQuarter_B  ===  Sandbox_ElvenQuarter
       |                   |                       |
       |                   |                       |
       +-- SuburbanC_Link -+                       |
                           |                       |
                           +-- B_Link -------------+-- Promenade

Steps:
  1. Create new landmark `Sandbox.SuburbanC_Link` (anchors BB_UrbanCommunity,
     a sandbox Elven/Urban deck bubble)
  2. Attach it to Sandbox_Small_Suburban_C (currently has no landmarks)
  3. Wire connections:
        Sandbox.SuburbanC_Link   ->  [B_Link]
        Sandbox.ElvenQuarterB_Link   ->  [SuburbanC_Link, Promenade]   (BOTH sides)
        Sandbox.ElvenQuarterPromenade   ->  [B_Link]   (drop the dangling C_Link
                                                         since ElvenQuarter_C is disabled)
  4. NameMap patches on both DataTables
"""
import copy
import json
from pathlib import Path

HERE = Path(__file__).parent
LM_PATH = HERE / 'DT_Moria_Landmarks.json'
ZN_PATH = HERE / 'DT_Moria_Zones.json'


def find_prop(row_value, name):
    for p in row_value or []:
        if isinstance(p, dict) and p.get('Name') == name:
            return p
    return None


def set_rowname(prop, new_val):
    for it in prop.get('Value', []) or []:
        if isinstance(it, dict) and it.get('Name') == 'RowName':
            it['Value'] = new_val
            return


def set_enum(prop, new_val):
    cur = prop.get('Value', '')
    if isinstance(cur, str) and '::' in cur:
        prefix = cur.split('::', 1)[0]
        prop['Value'] = f'{prefix}::{new_val}'
    else:
        prop['Value'] = new_val


def clone_landmark_row(source_row, new_name, bubble, display_key):
    r = copy.deepcopy(source_row)
    r['Name'] = new_name
    for p in r.get('Value', []):
        if not isinstance(p, dict):
            continue
        n = p.get('Name')
        if n == 'BaseBubbleName':
            p['Value'] = bubble
        elif n == 'DisplayName':
            p['Value'] = display_key
        elif n == 'GuaranteedConnections':
            existing = p.get('Value', []) or []
            if existing and 'DummyStruct' not in p:
                p['DummyStruct'] = copy.deepcopy(existing[0])
            p['Value'] = []
    return r


def set_gc(row, tag_list):
    gc = find_prop(row['Value'], 'GuaranteedConnections')
    if gc is None: return
    existing = gc.get('Value', [])
    template = copy.deepcopy(existing[0]) if existing else copy.deepcopy(gc.get('DummyStruct')) if gc.get('DummyStruct') else None
    if template is None:
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
                'Value': '',
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
    if new_items:
        gc.pop('DummyStruct', None)


# ---- 1. Load ----
lm = json.loads(LM_PATH.read_text(encoding='utf-8'))
zn = json.loads(ZN_PATH.read_text(encoding='utf-8'))
lm_rows = lm['Exports'][0]['Table']['Data']
zn_rows = zn['Exports'][0]['Table']['Data']
lm_by_name = {r['Name']: r for r in lm_rows}
zn_by_name = {r['Name']: r for r in zn_rows}


# ---- 2. Create SuburbanC_Link landmark if it doesn't exist ----
NEW_LM = 'Sandbox.SuburbanC_Link'
NEW_BUBBLE = 'BB_UrbanCommunity'

if NEW_LM not in lm_by_name:
    tpl = lm_by_name['Sandbox.ElvenQuarterB_Link']  # similar shape
    new_row = clone_landmark_row(tpl, NEW_LM, NEW_BUBBLE,
                                  f'Landmarks.{NEW_LM}')
    # Force Fixed placement
    pl = find_prop(new_row['Value'], 'Placement')
    if pl is not None:
        set_enum(pl, 'Fixed')
    lm_rows.append(new_row)
    lm_by_name[NEW_LM] = new_row
    print(f'Created landmark {NEW_LM}  anchors {NEW_BUBBLE}')


# ---- 3. Wire all three landmark connections ----
set_gc(lm_by_name['Sandbox.SuburbanC_Link'],
       ['World.Landmark.Sandbox.ElvenQuarterB_Link'])
print('  Sandbox.SuburbanC_Link       -> [B_Link]')

set_gc(lm_by_name['Sandbox.ElvenQuarterB_Link'],
       ['World.Landmark.Sandbox.SuburbanC_Link',
        'World.Landmark.Sandbox.ElvenQuarterPromenade'])
print('  Sandbox.ElvenQuarterB_Link   -> [SuburbanC_Link, Promenade]')

set_gc(lm_by_name['Sandbox.ElvenQuarterPromenade'],
       ['World.Landmark.Sandbox.ElvenQuarterB_Link'])
print('  Sandbox.ElvenQuarterPromenade -> [B_Link]    (dropped dangling C_Link)')


# ---- 4. Attach SuburbanC_Link to Suburban_C ----
sub_c = zn_by_name['Sandbox_Small_Suburban_C']
lh = find_prop(sub_c['Value'], 'LandmarkHandles')
if lh is None:
    raise SystemExit('Sandbox_Small_Suburban_C has no LandmarkHandles prop')

# Build an entry — use a template from another zone's LandmarkHandles
template_zone = zn_by_name['Sandbox_ElvenQuarter']
template_lh = find_prop(template_zone['Value'], 'LandmarkHandles')
entry_template = copy.deepcopy(template_lh['Value'][0])

def build_entry(lm_rowname, placement='Fixed', extended=False):
    e = copy.deepcopy(entry_template)
    for sub in e.get('Value', []):
        if not isinstance(sub, dict): continue
        n = sub.get('Name')
        if n == 'Landmark':
            set_rowname(sub, lm_rowname)
        elif n == 'Placement':
            cur = sub.get('Value','')
            prefix = cur.split('::',1)[0] if '::' in cur else 'EZoneBubblePlacement'
            sub['Value'] = f'{prefix}::{placement}'
        elif n == 'bExtendedConnectivityLandmark':
            sub['Value'] = bool(extended)
    return e

lh['Value'] = [build_entry(NEW_LM, 'Fixed', False)]
lh.pop('DummyStruct', None)
print(f'  Attached {NEW_LM} to Sandbox_Small_Suburban_C')


# ---- 5. NameMap patches ----
# Landmarks NameMap
nm_lm = lm.get('NameMap', [])
nm_lm_set = set(nm_lm)
lm_added = []
for s in [NEW_LM, NEW_BUBBLE,
          f'World.Landmark.{NEW_LM}',
          f'Landmarks.{NEW_LM}',
          'World.Landmark.Sandbox.SuburbanC_Link']:
    if s not in nm_lm_set:
        nm_lm.append(s); nm_lm_set.add(s); lm_added.append(s)
lm['NameMap'] = nm_lm

# Zones NameMap
nm_zn = zn.get('NameMap', [])
nm_zn_set = set(nm_zn)
zn_added = []
for s in [NEW_LM]:
    if s not in nm_zn_set:
        nm_zn.append(s); nm_zn_set.add(s); zn_added.append(s)
zn['NameMap'] = nm_zn


# ---- Save ----
LM_PATH.write_text(json.dumps(lm, indent=2), encoding='utf-8')
ZN_PATH.write_text(json.dumps(zn, indent=2), encoding='utf-8')
print(f'\n  Landmarks NameMap added: {lm_added}')
print(f'  Zones NameMap added: {zn_added}')
print(f'\n  Landmarks total: {len(lm_rows)}')
print(f'  Zones total: {len(zn_rows)}')
