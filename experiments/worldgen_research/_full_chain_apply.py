"""Build the full 14-floor elevator chain spanning D-7 to Lv-7.

Steps:
  1. Expand chapter MinZ for chapters 2,5,6,8,12.
  2. Verify Elevator_B is correct (chapter-1 + addl[2,3], size Z=4).
  3. Create 8 new zones + 8 new landmarks (one a relocation of CrystalDescent).
  4. Sync NameMaps on Zones, Chapters, Landmarks.
  5. Save all 4 DTs.

LayoutConnections is loaded only for backup; not modified.
"""
import copy
import json
from pathlib import Path

WGR = Path(__file__).resolve().parent

# -------- Chapter expansions --------
CHAP_MIN_Z = {
    'SandboxSmall-chapter-2':  19,
    'SandboxSmall-chapter-5':  14,
    'SandboxSmall-chapter-6':  10,
    'SandboxSmall-chapter-8':  5,
    'SandboxSmall-chapter-12': 2,
}

# -------- New zones --------
# (zone_name, primary_chap, addl_chaps, size_xyz, lm_name, ext_flag)
NEW_ZONES = [
    ('Sandbox_Small_TopElevator',     'SandboxSmall-chapter-4',
        ['SandboxSmall-chapter-9','SandboxSmall-chapter-10','SandboxSmall-chapter-11'],
        (6,6,4),  'Sandbox.TopElevator',     True),
    ('Sandbox_Small_Lv3Lv4Connector', 'SandboxSmall-chapter-3',
        ['SandboxSmall-chapter-4'],
        (4,4,2),  'Sandbox.Lv3Lv4Connector', True),
    ('Sandbox_Small_D1Lv1Connector',  'SandboxSmall-chapter-5',
        ['SandboxSmall-chapter-1'],
        (4,4,2),  'Sandbox.D1Lv1Connector',  True),
    ('Sandbox_Small_DeepUpperEl',     'SandboxSmall-chapter-6',
        ['SandboxSmall-chapter-5'],
        (6,6,5),  'Sandbox.DeepUpperEl',     True),
    ('Sandbox_Small_DeepMidEl',       'SandboxSmall-chapter-7',
        ['SandboxSmall-chapter-6'],
        (6,6,4),  'Sandbox.DeepMidEl',       True),
    ('Sandbox_Small_D4D3Connector',   'SandboxSmall-chapter-8',
        ['SandboxSmall-chapter-7'],
        (4,4,2),  'Sandbox.D4D3Connector',   True),
    ('Sandbox_Small_DeepBottomEl',    'SandboxSmall-chapter-12',
        ['SandboxSmall-chapter-8'],
        (6,6,5),  'Sandbox.DeepBottomEl',    True),
    ('Sandbox_Small_CrystalDescent',  'SandboxSmall-chapter-14',
        ['SandboxSmall-chapter-13','SandboxSmall-chapter-12'],
        (6,6,4),  'Chapter3.CrystalDescent', True),
    ('Sandbox_Small_D7D6Stair',       'SandboxSmall-chapter-13',
        ['SandboxSmall-chapter-14'],
        (4,4,2),  'Sandbox.D7D6Stair',       True),
]

# -------- New / updated landmark BasePositions --------
# lm_name -> (X, Y, Z)
LM_POS = {
    'Sandbox.TopElevator':     (4,  4,  25),
    'Sandbox.Lv3Lv4Connector': (8,  8,  21),
    'Sandbox.D1Lv1Connector':  (12, 12, 17),
    'Sandbox.DeepUpperEl':     (3,  14, 13),
    'Sandbox.DeepMidEl':       (15, 3,  9),
    'Sandbox.D4D3Connector':   (7,  15, 8),
    'Sandbox.DeepBottomEl':    (10, 6,  4),
    'Chapter3.CrystalDescent': (16, 14, 0),  # update existing
    'Sandbox.D7D6Stair':       (5,  11, 0),
}

# Landmarks to CREATE (skip Chapter3.CrystalDescent — exists already)
NEW_LM_NAMES = [
    'Sandbox.TopElevator', 'Sandbox.Lv3Lv4Connector', 'Sandbox.D1Lv1Connector',
    'Sandbox.DeepUpperEl', 'Sandbox.DeepMidEl', 'Sandbox.D4D3Connector',
    'Sandbox.DeepBottomEl', 'Sandbox.D7D6Stair',
]


# -------- Helpers --------
def load_json(p):
    with open(p, 'r', encoding='utf-8') as f:
        return json.load(f)

def save_json(obj, p):
    with open(p, 'w', encoding='utf-8') as f:
        json.dump(obj, f, indent=2, ensure_ascii=False)

def get_prop(values, name):
    for p in values or []:
        if isinstance(p, dict) and p.get('Name') == name:
            return p
    return None

def set_prop_value(values, name, new_value):
    p = get_prop(values, name)
    if p is None:
        raise KeyError(f'property {name} not found')
    p['Value'] = new_value
    return p

def vec_value(prop):
    """Return mutable inner FIntVector dict from a struct property like Position/BasePosition."""
    if not prop: return None
    vlst = prop.get('Value')
    if isinstance(vlst, list) and vlst:
        d = vlst[0].get('Value') if isinstance(vlst[0], dict) else None
        return d
    return None

def set_vec(prop, x, y, z):
    d = vec_value(prop)
    if d is None:
        raise RuntimeError(f'no inner vec on {prop.get("Name")}')
    d['X'] = x; d['Y'] = y; d['Z'] = z

def make_chapter_handle_struct(row_name, prop_name='AdditionalChapters'):
    return {
        '$type': 'UAssetAPI.PropertyTypes.Structs.StructPropertyData, UAssetAPI',
        'StructType': 'MorChapterRowHandle',
        'SerializeNone': True,
        'StructGUID': '{00000000-0000-0000-0000-000000000000}',
        'SerializationControl': 'NoExtension',
        'Operation': 'None',
        'Name': prop_name,
        'ArrayIndex': 0,
        'IsZero': False,
        'PropertyTagFlags': 'None',
        'PropertyTagExtensions': 'NoExtension',
        'Value': [{
            '$type': 'UAssetAPI.PropertyTypes.Objects.NamePropertyData, UAssetAPI',
            'Name': 'RowName',
            'ArrayIndex': 0,
            'IsZero': False,
            'PropertyTagFlags': 'None',
            'PropertyTagExtensions': 'NoExtension',
            'Value': row_name,
        }],
    }


def build_zone(template, name, primary_chap, addl_chaps, size_xyz, lm_name, ext_flag):
    z = copy.deepcopy(template)
    z['Name'] = name
    v = z['Value']

    # Chapter
    chap_struct = get_prop(v, 'Chapter')
    rn_prop = get_prop(chap_struct['Value'], 'RowName')
    rn_prop['Value'] = primary_chap

    # AdditionalChapters
    addl_prop = get_prop(v, 'AdditionalChapters')
    if addl_chaps:
        addl_prop['Value'] = [make_chapter_handle_struct(c, 'AdditionalChapters')
                              for c in addl_chaps]
        addl_prop.pop('DummyStruct', None)
    else:
        addl_prop['Value'] = []

    # Position = (0,0,0) sentinel
    pos_prop = get_prop(v, 'Position')
    set_vec(pos_prop, 0, 0, 0)

    # TargetSize
    tgt_prop = get_prop(v, 'TargetSize')
    set_vec(tgt_prop, *size_xyz)

    # Flags
    set_prop_value(v, 'bPositionFromLandmarks', True)
    set_prop_value(v, 'bPositionFromZoneTable', True)
    # bExtendFootprint -> false (per spec)
    bef = get_prop(v, 'bExtendFootprint')
    if bef is not None:
        bef['Value'] = False
    set_prop_value(v, 'EnabledState', 'ERowEnabledState::Live')

    # LandmarkHandles - single entry pointing at lm_name
    lh_prop = get_prop(v, 'LandmarkHandles')
    if lh_prop['Value']:
        existing = copy.deepcopy(lh_prop['Value'][0])
        lm_struct = get_prop(existing['Value'], 'Landmark')
        lm_rn = get_prop(lm_struct['Value'], 'RowName')
        lm_rn['Value'] = lm_name
        place = get_prop(existing['Value'], 'Placement')
        if place is not None:
            place['Value'] = 'EZoneBubblePlacement::Fixed'
        ext = get_prop(existing['Value'], 'bExtendedConnectivityLandmark')
        if ext is not None:
            ext['Value'] = bool(ext_flag)
        lh_prop['Value'] = [existing]

    # DisplayName
    dn_prop = get_prop(v, 'DisplayName')
    if dn_prop is not None:
        dn_prop['Value'] = f'Zones.Names.SB_{name.replace("Sandbox_Small_", "")}'

    return z


def build_landmark(template, name, x, y, z):
    lm = copy.deepcopy(template)
    lm['Name'] = name
    v = lm['Value']

    # BasePosition
    bp = get_prop(v, 'BasePosition')
    set_vec(bp, x, y, z)

    # Placement: ELandmarkPlacement::Fixed (already, but ensure)
    pl = get_prop(v, 'Placement')
    if pl is not None:
        pl['Value'] = 'ELandmarkPlacement::Fixed'

    # InternalId.TagName -> "World.Landmark.<name>"
    iid = get_prop(v, 'InternalId')
    if iid is not None:
        tn = get_prop(iid['Value'], 'TagName')
        if tn is not None:
            tn['Value'] = f'World.Landmark.{name}'

    # EnabledState -> Live
    es = get_prop(v, 'EnabledState')
    if es is not None:
        es['Value'] = 'ERowEnabledState::Live'

    return lm


def sync_namemap(doc, names_to_add, names_to_remove=()):
    nm = doc.get('NameMap', [])
    nm_set = set(nm)
    for n in names_to_remove:
        if n in nm_set:
            nm.remove(n)
            nm_set.discard(n)
    for n in names_to_add:
        if n and n not in nm_set:
            nm.append(n)
            nm_set.add(n)
    doc['NameMap'] = nm
    if 'NamesReferencedFromExportDataCount' in doc:
        doc['NamesReferencedFromExportDataCount'] = len(nm)
    gens = doc.get('Generations')
    if isinstance(gens, list) and gens:
        if 'NameCount' in gens[0]:
            gens[0]['NameCount'] = len(nm)


def main():
    print('=== Loading DTs ===')
    zones_doc = load_json(WGR / 'DT_Moria_Zones.json')
    chaps_doc = load_json(WGR / 'DT_Moria_Chapters.json')
    lmks_doc  = load_json(WGR / 'DT_Moria_Landmarks.json')

    z_data = zones_doc['Exports'][0]['Table']['Data']
    c_data = chaps_doc['Exports'][0]['Table']['Data']
    l_data = lmks_doc['Exports'][0]['Table']['Data']

    # ---- Step 1: Chapter MinZ expansion ----
    print('\n=== Chapter MinZ expansion ===')
    for r in c_data:
        n = r.get('Name')
        if n in CHAP_MIN_Z:
            mn_prop = get_prop(r['Value'], 'MinZ')
            old = mn_prop['Value']
            mn_prop['Value'] = CHAP_MIN_Z[n]
            print(f'  {n}: MinZ {old} -> {CHAP_MIN_Z[n]}')

    # ---- Step 2: verify Elevator_B unchanged ----
    eB = next((r for r in z_data if r['Name']=='Sandbox_Small_Elevator_B'), None)
    if eB:
        sz = vec_value(get_prop(eB['Value'],'TargetSize'))
        print(f'\nElevator_B verify: size={sz} — {"OK" if sz and sz["Z"]==4 else "WARN"}')

    # ---- Step 3: build new zones ----
    print('\n=== Building new zones ===')
    template = next(r for r in z_data if r['Name']=='Sandbox_Small_Elevator_B')
    new_zone_objs = []
    for spec in NEW_ZONES:
        zname, primary, addl, sz, lmname, ext = spec
        if any(r['Name']==zname for r in z_data):
            print(f'  WARNING: zone {zname} already exists; replacing')
            z_data[:] = [r for r in z_data if r['Name'] != zname]
        zo = build_zone(template, zname, primary, addl, sz, lmname, ext)
        z_data.append(zo)
        new_zone_objs.append(zo)
        print(f'  {zname}: primary={primary} addl={addl} size={sz} lm={lmname}')

    # ---- Step 4: build / update landmarks ----
    print('\n=== Building landmarks ===')
    # template = an existing simple landmark
    lm_template = next(r for r in l_data if r['Name']=='Sandbox.FirstStair')
    for lname in NEW_LM_NAMES:
        x,y,zv = LM_POS[lname]
        if any(r['Name']==lname for r in l_data):
            print(f'  WARNING: landmark {lname} already exists; replacing')
            l_data[:] = [r for r in l_data if r['Name'] != lname]
        lm = build_landmark(lm_template, lname, x, y, zv)
        l_data.append(lm)
        print(f'  + {lname}: ({x},{y},{zv})')

    # Update existing Chapter3.CrystalDescent BP and ensure Live
    cd = next((r for r in l_data if r['Name']=='Chapter3.CrystalDescent'), None)
    if cd:
        x,y,zv = LM_POS['Chapter3.CrystalDescent']
        bp = get_prop(cd['Value'],'BasePosition')
        set_vec(bp, x, y, zv)
        es = get_prop(cd['Value'],'EnabledState')
        if es and es['Value'] != 'ERowEnabledState::Live':
            es['Value'] = 'ERowEnabledState::Live'
        print(f'  ~ Chapter3.CrystalDescent: BP -> ({x},{y},{zv})')
    else:
        print('  WARNING: Chapter3.CrystalDescent not found')

    # ---- Step 5: NameMap sync ----
    print('\n=== NameMap sync ===')
    # Zones doc must reference: new zone names, primary/addl chapter rows, lm names,
    # and the StringTable display keys.
    new_zone_names = [s[0] for s in NEW_ZONES]
    referenced_chaps = set()
    for s in NEW_ZONES:
        referenced_chaps.add(s[1])
        for c in s[2]: referenced_chaps.add(c)
    referenced_lms = set(s[4] for s in NEW_ZONES)
    new_st_keys = [f'Zones.Names.SB_{n.replace("Sandbox_Small_","")}' for n in new_zone_names]

    sync_namemap(zones_doc,
        names_to_add=new_zone_names + list(referenced_chaps) + list(referenced_lms) + new_st_keys)
    print(f'  Zones NameMap len={len(zones_doc["NameMap"])}')

    # Chapters NameMap: nothing new added (all chap rows existed); but ensure consistency
    # No removals needed.
    sync_namemap(chaps_doc, names_to_add=[])
    print(f'  Chapters NameMap len={len(chaps_doc["NameMap"])}')

    # Landmarks doc must reference: new landmark row names + their TagName strings
    new_tag_names = [f'World.Landmark.{n}' for n in NEW_LM_NAMES]
    sync_namemap(lmks_doc,
        names_to_add=NEW_LM_NAMES + new_tag_names)
    print(f'  Landmarks NameMap len={len(lmks_doc["NameMap"])}')

    # ---- Save ----
    save_json(zones_doc, WGR / 'DT_Moria_Zones.json')
    save_json(chaps_doc, WGR / 'DT_Moria_Chapters.json')
    save_json(lmks_doc,  WGR / 'DT_Moria_Landmarks.json')
    print('\nSaved DT_Moria_Zones.json, DT_Moria_Chapters.json, DT_Moria_Landmarks.json')


if __name__ == '__main__':
    main()
