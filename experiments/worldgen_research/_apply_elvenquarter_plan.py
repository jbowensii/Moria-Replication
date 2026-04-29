"""
Apply user's chosen plan for chapter-2 ElvenQuarter zones:

  Layout A    Sandbox.ElvenQuarter positioned east of B/C at Z=12,
              contiguous so the generator auto-connects.

  Option 1    BubbleDeck=Sandbox_ElvenQuarterBubbles
              PassageDeck=Sandbox_ElvenQuarterPassages

  Unique landmarks per zone:
    Sandbox_Small_ElvenQuarter_B -> Sandbox.ElvenQuarterB_Entrance
                                    Sandbox.ElvenQuarterB_Promenade
    Sandbox_Small_ElvenQuarter_C -> Sandbox.ElvenQuarterC_Entrance
                                    Sandbox.ElvenQuarterC_Promenade
    Sandbox.ElvenQuarter         -> Sandbox.ElvenQuarterEntrance
                                    Sandbox.ElvenQuarterPromenade   (already there)

Each pair internally connects Entrance<->Promenade via GuaranteedConnections.
"""
import copy
import json
from pathlib import Path

HERE = Path(__file__).parent
LM_PATH = HERE / 'DT_Moria_Landmarks.json'
ZN_PATH = HERE / 'DT_Moria_Zones.json'


# -----------------------------------------------------------------------------
# helpers
# -----------------------------------------------------------------------------

def find_prop(row_value, name):
    for p in row_value or []:
        if isinstance(p, dict) and p.get('Name') == name:
            return p
    return None


def set_enum(prop, new_val):
    cur = prop.get('Value', '')
    if isinstance(cur, str) and '::' in cur:
        prefix = cur.split('::', 1)[0]
        prop['Value'] = f'{prefix}::{new_val}'
    else:
        prop['Value'] = new_val


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


def set_connections(landmark_row, tag_list):
    """Rewrite GuaranteedConnections on a landmark row."""
    gc = find_prop(landmark_row['Value'], 'GuaranteedConnections')
    if gc is None:
        return
    existing = gc.get('Value', [])
    if existing:
        template = copy.deepcopy(existing[0])
    else:
        template = gc.get('DummyStruct')
        if template is None:
            # Synthesise minimal GameplayTag struct
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
    # Preserve DummyStruct on an empty array; drop on non-empty to avoid bloat
    if new_items:
        gc.pop('DummyStruct', None)
    else:
        gc['DummyStruct'] = copy.deepcopy(template)
    gc['Value'] = new_items


def clone_landmark(source_row, new_name, bubble, display_key):
    """Return a deep-copied landmark row with name + bubble + display updated.
    Clears GuaranteedConnections (caller fills in)."""
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
            existing = p.get('Value', [])
            if existing and 'DummyStruct' not in p:
                p['DummyStruct'] = copy.deepcopy(existing[0])
            p['Value'] = []
    return r


# -----------------------------------------------------------------------------
# 1) Create the four new landmarks
# -----------------------------------------------------------------------------

lm_data = json.loads(LM_PATH.read_text(encoding='utf-8'))
lm_rows = lm_data['Exports'][0]['Table']['Data']
lm_by_name = {r['Name']: r for r in lm_rows}

# Use the existing sandbox pair as template — they're already sandbox-safe
tpl_entrance = lm_by_name['Sandbox.ElvenQuarterEntrance']
tpl_promenade = lm_by_name['Sandbox.ElvenQuarterPromenade']

BUBBLE_ENTRANCE = 'BB_Chapter2_ElvenQuarterEntrance'
BUBBLE_PROMENADE = 'BB_Chapter2_ElvenQuarterPromenade'

new_landmarks = [
    ('Sandbox.ElvenQuarterB_Entrance',  tpl_entrance,  BUBBLE_ENTRANCE,
     'Landmarks.Sandbox.ElvenQuarterB_Entrance'),
    ('Sandbox.ElvenQuarterB_Promenade', tpl_promenade, BUBBLE_PROMENADE,
     'Landmarks.Sandbox.ElvenQuarterB_Promenade'),
    ('Sandbox.ElvenQuarterC_Entrance',  tpl_entrance,  BUBBLE_ENTRANCE,
     'Landmarks.Sandbox.ElvenQuarterC_Entrance'),
    ('Sandbox.ElvenQuarterC_Promenade', tpl_promenade, BUBBLE_PROMENADE,
     'Landmarks.Sandbox.ElvenQuarterC_Promenade'),
]

for name, tpl, bubble, display in new_landmarks:
    if name in lm_by_name:
        print(f'  {name} already exists — skipping create')
        continue
    r = clone_landmark(tpl, name, bubble, display)
    lm_rows.append(r)
    lm_by_name[name] = r
    print(f'  created landmark {name}')

# Wire pair connections: Entrance <-> Promenade within each pair
pair_wires = [
    ('Sandbox.ElvenQuarterB_Entrance',  'Sandbox.ElvenQuarterB_Promenade'),
    ('Sandbox.ElvenQuarterB_Promenade', 'Sandbox.ElvenQuarterB_Entrance'),
    ('Sandbox.ElvenQuarterC_Entrance',  'Sandbox.ElvenQuarterC_Promenade'),
    ('Sandbox.ElvenQuarterC_Promenade', 'Sandbox.ElvenQuarterC_Entrance'),
]
for src, tgt in pair_wires:
    set_connections(lm_by_name[src], [f'World.Landmark.{tgt}'])
    print(f'  {src}  conns -> [{tgt}]')

# NameMap additions for Landmarks
lm_nm = lm_data.get('NameMap', [])
lm_nm_set = set(lm_nm)
lm_added = []
for name, _, bubble, display in new_landmarks:
    for s in (name, bubble, f'World.Landmark.{name}', display):
        if s and s not in lm_nm_set:
            lm_nm.append(s); lm_nm_set.add(s); lm_added.append(s)
lm_data['NameMap'] = lm_nm

LM_PATH.write_text(json.dumps(lm_data, indent=2), encoding='utf-8')
print(f'\nDT_Moria_Landmarks.json: saved, {len(lm_added)} NameMap entries added')


# -----------------------------------------------------------------------------
# 2) Update zones:
#    Sandbox.ElvenQuarter         -> decks + position/size
#    Sandbox_Small_ElvenQuarter_B -> LandmarkHandles rewritten to B pair
#    Sandbox_Small_ElvenQuarter_C -> LandmarkHandles rewritten to C pair
# -----------------------------------------------------------------------------

zn_data = json.loads(ZN_PATH.read_text(encoding='utf-8'))
zn_rows = zn_data['Exports'][0]['Table']['Data']
zn_by_name = {r['Name']: r for r in zn_rows}

# --- Sandbox.ElvenQuarter: decks + position + size
r = zn_by_name['Sandbox.ElvenQuarter']

bd = find_prop(r['Value'], 'BubbleDeck')
pd = find_prop(r['Value'], 'PassageDeck')
set_rowname(bd, 'Sandbox_ElvenQuarterBubbles')
set_rowname(pd, 'Sandbox_ElvenQuarterPassages')
print('\nSandbox.ElvenQuarter decks updated:')
print('  BubbleDeck  -> Sandbox_ElvenQuarterBubbles')
print('  PassageDeck -> Sandbox_ElvenQuarterPassages')

# Layout A: Position (14, 12, 12), Size (4, 6, 1)
pos = find_prop(r['Value'], 'Position')
sz = find_prop(r['Value'], 'TargetSize')
set_intvec(pos, 14, 12, 12)
set_intvec(sz, 4, 6, 1)
print('Sandbox.ElvenQuarter position: (14, 12, 12)  size: (4, 6, 1)  (Z=12, east of B/C)')


def rewire_zone_landmarks(zone_row, landmark_pair):
    """Replace LandmarkHandles[] with two entries pointing at a custom pair.
    landmark_pair = (entrance_rowname, promenade_rowname)"""
    lh = find_prop(zone_row['Value'], 'LandmarkHandles')
    if lh is None:
        return
    existing = lh.get('Value', []) or []
    if not existing:
        # Nothing to template from — synthesise
        return
    template = copy.deepcopy(existing[0])

    def build(lm):
        e = copy.deepcopy(template)
        for sub in e.get('Value', []):
            if not isinstance(sub, dict):
                continue
            n = sub.get('Name')
            if n == 'Landmark':
                set_rowname(sub, lm)
            elif n == 'Placement':
                cur = sub.get('Value', '')
                prefix = cur.split('::', 1)[0] if '::' in cur else 'EZoneBubblePlacement'
                sub['Value'] = f'{prefix}::Fixed'
            elif n == 'bExtendedConnectivityLandmark':
                sub['Value'] = False
        return e

    lh['Value'] = [build(landmark_pair[0]), build(landmark_pair[1])]
    lh.pop('DummyStruct', None)


rewire_zone_landmarks(zn_by_name['Sandbox_Small_ElvenQuarter_B'],
                      ('Sandbox.ElvenQuarterB_Entrance',
                       'Sandbox.ElvenQuarterB_Promenade'))
print('\nSandbox_Small_ElvenQuarter_B landmarks -> B pair')

rewire_zone_landmarks(zn_by_name['Sandbox_Small_ElvenQuarter_C'],
                      ('Sandbox.ElvenQuarterC_Entrance',
                       'Sandbox.ElvenQuarterC_Promenade'))
print('Sandbox_Small_ElvenQuarter_C landmarks -> C pair')

# Zones NameMap: add the new landmark row names so the zones can reference them
zn_nm = zn_data.get('NameMap', [])
zn_nm_set = set(zn_nm)
zn_added = []
for s in ('Sandbox.ElvenQuarterB_Entrance', 'Sandbox.ElvenQuarterB_Promenade',
          'Sandbox.ElvenQuarterC_Entrance', 'Sandbox.ElvenQuarterC_Promenade',
          'Sandbox_ElvenQuarterBubbles', 'Sandbox_ElvenQuarterPassages'):
    if s not in zn_nm_set:
        zn_nm.append(s); zn_nm_set.add(s); zn_added.append(s)
zn_data['NameMap'] = zn_nm

ZN_PATH.write_text(json.dumps(zn_data, indent=2), encoding='utf-8')
print(f'\nDT_Moria_Zones.json: saved, {len(zn_added)} NameMap entries added: {zn_added}')

print('\n=== Done. Summary ===')
print('  Sandbox.ElvenQuarter: decks swapped to ElvenQuarter variants, '
      'position (14,12,12), size (4,6,1), priority 130, landmarks intact')
print('  Sandbox_Small_ElvenQuarter_B: landmarks rewired to B pair')
print('  Sandbox_Small_ElvenQuarter_C: landmarks rewired to C pair')
print(f'  Landmarks total: {len(lm_rows)}')
print(f'  Zones total: {len(zn_rows)}')
