"""
Final ElvenQuarter topology for chapter-2 sandbox:

   ┌────────┐      ┌─────────────────┐      ┌────────┐
   │   B    │◄────►│ Sandbox.ElvenQ  │◄────►│   C    │
   │ X5..13 │      │ Promenade only  │      │X19..27 │
   └────────┘      └─────────────────┘      └────────┘
    decks only      1 Promenade bubble       decks only
    + B_Link        w/ 2 guaranteed          + C_Link
                    cross-zone connections

Changes:
  1. Move Sandbox_Small_ElvenQuarter_C to Position (19, 12, 12)
  2. Empty LandmarkHandles on B and C (DummyStruct preserved)
  3. Sandbox.ElvenQuarter keeps Sandbox.ElvenQuarterPromenade (sole Promenade)
  4. Bump B and C GenerationPriority 120 -> 125 (ensure both spawn)
  5. Create two "connector" landmarks:
       Sandbox.ElvenQuarterB_Link  anchors BB_DwarfHall_Small  -> inside B
       Sandbox.ElvenQuarterC_Link  anchors BB_Sandbox_ElfHall  -> inside C
     Add them to B and C's LandmarkHandles respectively.
     Add cross-zone GuaranteedConnections:
       Sandbox.ElvenQuarterPromenade  ->  [B_Link, C_Link]
       B_Link                          ->  [Sandbox.ElvenQuarterPromenade]
       C_Link                          ->  [Sandbox.ElvenQuarterPromenade]
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


def set_intvec(prop, x, y, z):
    for it in prop.get('Value', []) or []:
        if isinstance(it, dict):
            v = it.get('Value')
            if isinstance(v, dict) and 'X' in v:
                v['X'] = int(x); v['Y'] = int(y); v['Z'] = int(z)
                return


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
    """Overwrite the GuaranteedConnections[] on a landmark row."""
    gc = find_prop(row['Value'], 'GuaranteedConnections')
    if gc is None:
        return
    existing = gc.get('Value', [])
    template = copy.deepcopy(existing[0]) if existing else gc.get('DummyStruct')
    if template is None:
        # minimal GameplayTag struct
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
    else:
        template = copy.deepcopy(template)

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


# -----------------------------------------------------------------------------
# LANDMARKS  — create B_Link and C_Link connector landmarks, rewire Promenade
# -----------------------------------------------------------------------------

lm_data = json.loads(LM_PATH.read_text(encoding='utf-8'))
lm_rows = lm_data['Exports'][0]['Table']['Data']
lm_by_name = {r['Name']: r for r in lm_rows}

# Use an existing Sandbox landmark as template (Sandbox.DwarfMainHall has
# simple structure with empty connections — perfect source)
tpl = lm_by_name.get('Sandbox.DwarfMainHall') or lm_by_name['Sandbox.ElvenQuarterPromenade']

connectors = [
    ('Sandbox.ElvenQuarterB_Link', 'BB_DwarfHall_Small',
     'Landmarks.Sandbox.ElvenQuarterB_Link'),
    ('Sandbox.ElvenQuarterC_Link', 'BB_Sandbox_ElfHall',
     'Landmarks.Sandbox.ElvenQuarterC_Link'),
]
for new_name, bubble, display in connectors:
    if new_name in lm_by_name:
        print(f'  {new_name} already exists — using in place')
    else:
        r = clone_landmark_row(tpl, new_name, bubble, display)
        # Force Placement=Fixed so they anchor reliably
        pl = find_prop(r['Value'], 'Placement')
        if pl is not None:
            cur = pl.get('Value', '')
            prefix = cur.split('::', 1)[0] if '::' in cur else 'ELandmarkPlacement'
            pl['Value'] = f'{prefix}::Fixed'
        lm_rows.append(r)
        lm_by_name[new_name] = r
        print(f'  created landmark {new_name} -> {bubble}')

# Cross-zone connections
#   Promenade <-> both connectors
set_gc(lm_by_name['Sandbox.ElvenQuarterPromenade'],
       ['World.Landmark.Sandbox.ElvenQuarterB_Link',
        'World.Landmark.Sandbox.ElvenQuarterC_Link'])
print('  Sandbox.ElvenQuarterPromenade  conns -> [B_Link, C_Link]')

set_gc(lm_by_name['Sandbox.ElvenQuarterB_Link'],
       ['World.Landmark.Sandbox.ElvenQuarterPromenade'])
print('  Sandbox.ElvenQuarterB_Link      conns -> [Promenade]')

set_gc(lm_by_name['Sandbox.ElvenQuarterC_Link'],
       ['World.Landmark.Sandbox.ElvenQuarterPromenade'])
print('  Sandbox.ElvenQuarterC_Link      conns -> [Promenade]')

# Landmarks NameMap
nm = lm_data.get('NameMap', [])
nm_set = set(nm)
added = []
for s in ['Sandbox.ElvenQuarterB_Link', 'BB_DwarfHall_Small',
         'World.Landmark.Sandbox.ElvenQuarterB_Link',
         'Landmarks.Sandbox.ElvenQuarterB_Link',
         'Sandbox.ElvenQuarterC_Link', 'BB_Sandbox_ElfHall',
         'World.Landmark.Sandbox.ElvenQuarterC_Link',
         'Landmarks.Sandbox.ElvenQuarterC_Link']:
    if s not in nm_set:
        nm.append(s); nm_set.add(s); added.append(s)
lm_data['NameMap'] = nm
LM_PATH.write_text(json.dumps(lm_data, indent=2), encoding='utf-8')
print(f'  Landmarks NameMap: added {len(added)} entries')


# -----------------------------------------------------------------------------
# ZONES  — move C, detach landmarks from B/C, bump priorities, attach B_Link/C_Link
# -----------------------------------------------------------------------------

zn_data = json.loads(ZN_PATH.read_text(encoding='utf-8'))
zn_rows = zn_data['Exports'][0]['Table']['Data']
zn_by_name = {r['Name']: r for r in zn_rows}


def attach_single_landmark(zone_row, lm_rowname, placement='Fixed', extended=False):
    """Replace LandmarkHandles with a single entry for the given landmark."""
    lh = find_prop(zone_row['Value'], 'LandmarkHandles')
    if lh is None:
        return
    existing = lh.get('Value', []) or []
    template = None
    if existing:
        template = copy.deepcopy(existing[0])
    elif 'DummyStruct' in lh:
        template = copy.deepcopy(lh['DummyStruct'])
    else:
        # Borrow a shape from another zone
        for r in zn_rows:
            other_lh = find_prop(r['Value'], 'LandmarkHandles')
            if other_lh and other_lh.get('Value'):
                template = copy.deepcopy(other_lh['Value'][0])
                break
    if template is None:
        return
    for sub in template.get('Value', []):
        if not isinstance(sub, dict):
            continue
        n = sub.get('Name')
        if n == 'Landmark':
            set_rowname(sub, lm_rowname)
        elif n == 'Placement':
            cur = sub.get('Value', '')
            prefix = cur.split('::', 1)[0] if '::' in cur else 'EZoneBubblePlacement'
            sub['Value'] = f'{prefix}::{placement}'
        elif n == 'bExtendedConnectivityLandmark':
            sub['Value'] = bool(extended)
    lh['Value'] = [template]
    lh.pop('DummyStruct', None)


# 1. Move C east
C = zn_by_name['Sandbox_Small_ElvenQuarter_C']
set_intvec(find_prop(C['Value'], 'Position'), 19, 12, 12)
set_intvec(find_prop(C['Value'], 'TargetSize'), 8, 6, 1)
print('  Sandbox_Small_ElvenQuarter_C position -> (19, 12, 12)  size -> (8, 6, 1)')

# 2/5. Attach B_Link to B, C_Link to C (replaces the Promenade landmarks)
attach_single_landmark(zn_by_name['Sandbox_Small_ElvenQuarter_B'],
                        'Sandbox.ElvenQuarterB_Link')
print('  Sandbox_Small_ElvenQuarter_B landmark -> Sandbox.ElvenQuarterB_Link')

attach_single_landmark(zn_by_name['Sandbox_Small_ElvenQuarter_C'],
                        'Sandbox.ElvenQuarterC_Link')
print('  Sandbox_Small_ElvenQuarter_C landmark -> Sandbox.ElvenQuarterC_Link')

# 4. Bump priority on B and C
for z_name in ['Sandbox_Small_ElvenQuarter_B', 'Sandbox_Small_ElvenQuarter_C']:
    z = zn_by_name[z_name]
    gp = find_prop(z['Value'], 'GenerationPriority')
    if gp:
        gp['Value'] = 125
        print(f'  {z_name} priority -> 125')

# Zones NameMap — ensure B_Link and C_Link names are present
zn_nm = zn_data.get('NameMap', [])
zn_nm_set = set(zn_nm)
zn_added = []
for s in ['Sandbox.ElvenQuarterB_Link', 'Sandbox.ElvenQuarterC_Link']:
    if s not in zn_nm_set:
        zn_nm.append(s); zn_nm_set.add(s); zn_added.append(s)
zn_data['NameMap'] = zn_nm
ZN_PATH.write_text(json.dumps(zn_data, indent=2), encoding='utf-8')
print(f'  Zones NameMap: added {len(zn_added)} entries')

print('\n=== Done ===')
