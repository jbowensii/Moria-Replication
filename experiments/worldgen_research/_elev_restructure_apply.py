"""Apply the elevator restructure: 7 multi-Z zones -> 12 single-stair zones.

Steps:
  - Load current Zones, Chapters JSONs.
  - Load template (Sandbox_Small_Elevator_C) from working backup.
  - For each of 12 stairs, clone template -> override Name, Chapter.RowName,
    AdditionalChapters, single LandmarkHandle (with Placement=Fixed,
    bExtendedConnectivityLandmark=true), DisplayName SourceValue, EnabledState=Live,
    keep Position=(0,0,0), TargetSize=(6,6,4), bPositionFromLandmarks=true,
    bPositionFromZoneTable=true.
  - Remove the 7 old elevator zones from Zones.
  - Append 12 new elevator zones to Zones.
  - Remove 7 SandboxSmall-Chapter##.Elevator_* rows from Chapters.
  - Sync NameMap: add new zone names, remove old elevator zone names from Zones NameMap;
    remove deleted chapter row names from Chapters NameMap.
  - Update NamesReferencedFromExportDataCount and Generations[0].NameCount per file.
"""
import copy
import json
from pathlib import Path

WGR = Path(__file__).resolve().parent
BACKUP = WGR / 'backups' / 'working with restored stair labels'

STAIR_MAP = [
    # (stair_name, primary_chapter_row, additional_chapter_row_or_None, ext_flag)
    # Primary must be an INTERIOR floor — must have both Layer+1 and Layer-1 neighbours live.
    # For edge stairs whose primary in the spec is at a stack edge (Lv-7 / Deep-7),
    # we swap primary<->addl. EleventhStair has no swap target -> clear ext flag.
    ('FirstStair',     'SandboxSmall-Chapter01.Level1', 'SandboxSmall-Chapter02.Level2', True),
    ('SecondStair',    'SandboxSmall-Chapter13.Deep2',  'SandboxSmall-Chapter12.Deep3',  True),
    ('ThirdStair',     'SandboxSmall-Chapter05.Level5', 'SandboxSmall-Chapter04.Level4', True),
    ('FourthStair',    'SandboxSmall-Chapter04.Level4', 'SandboxSmall-Chapter03.Level3', True),
    ('SixthStair',     'SandboxSmall-Chapter06.Level6', 'SandboxSmall-Chapter05.Level5', True),
    ('SeventhStair',   'SandboxSmall-Chapter10.Deep5',  'SandboxSmall-Chapter11.Deep4',  True),
    # EighthStair: spec says Lv-7 primary / Lv-6 addl. Lv-7 is stack edge (no Layer+1).
    # Swap so primary=Lv-6 (interior), addl=Lv-7. Stair landmark unchanged.
    ('EighthStair',    'SandboxSmall-Chapter06.Level6', 'SandboxSmall-Chapter07.Level7', True),
    ('NinthStair',     'SandboxSmall-Chapter14.Deep1',  'SandboxSmall-Chapter13.Deep2',  True),
    ('TenthStair',     'SandboxSmall-Chapter01.Level1', 'SandboxSmall-Chapter14.Deep1',  True),
    # EleventhStair: cap at Lv-7 (no neighbour above). Cannot satisfy ext-conn invariant.
    # Per validator + task spec, clear bExtendedConnectivityLandmark.
    ('EleventhStair',  'SandboxSmall-Chapter07.Level7', None,                            False),
    ('CrystalDescent', 'SandboxSmall-Chapter09.Deep6',  'SandboxSmall-Chapter10.Deep5',  True),
    # LowerDescent: spec says Deep7 primary / Deep6 addl. Deep7 is stack edge.
    # Swap so primary=Deep6 (interior), addl=Deep7. Stair landmark unchanged.
    ('LowerDescent',   'SandboxSmall-Chapter09.Deep6',  'SandboxSmall-Chapter08.Deep7',  True),
]

OLD_ELEV_ZONES = [
    'Sandbox_Small_Elevator_B',
    'Sandbox_Small_Elevator_C',
    'Sandbox_Small_Elevator_D',
    'Sandbox_Small_Elevator_E',
    'Sandbox_Small_Elevator_F',
    'Sandbox_Small_Elevator_G',
    'Sandbox_Small_Elevator_H',
]

OLD_ELEV_CHAP_ROWS = [
    'SandboxSmall-Chapter01.Elevator_B',
    'SandboxSmall-Chapter05.Elevator_D',
    'SandboxSmall-Chapter08.Elevator_E',
    'SandboxSmall-Chapter09.Elevator_F',
    'SandboxSmall-Chapter10.Elevator_G',
    'SandboxSmall-Chapter12.Elevator_C',
    'SandboxSmall-Chapter14.Elevator_H',
]


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

def make_chapter_handle_struct(row_name, prop_name='AdditionalChapters'):
    """Returns a struct entry suitable for AdditionalChapters array."""
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
        'Value': [
            {
                '$type': 'UAssetAPI.PropertyTypes.Objects.NamePropertyData, UAssetAPI',
                'Name': 'RowName',
                'ArrayIndex': 0,
                'IsZero': False,
                'PropertyTagFlags': 'None',
                'PropertyTagExtensions': 'NoExtension',
                'Value': row_name,
            }
        ],
    }


def make_dummy_chapter_struct():
    """DummyStruct used when an AdditionalChapters array is empty so the
    serializer knows the inner StructType."""
    return {
        '$type': 'UAssetAPI.PropertyTypes.Structs.StructPropertyData, UAssetAPI',
        'StructType': 'MorChapterRowHandle',
        'SerializeNone': True,
        'StructGUID': '{00000000-0000-0000-0000-000000000000}',
        'SerializationControl': 'NoExtension',
        'Operation': 'None',
        'Name': 'AdditionalChapters',
        'ArrayIndex': 0,
        'IsZero': False,
        'PropertyTagFlags': 'None',
        'PropertyTagExtensions': 'NoExtension',
        'Value': [],
    }


def build_zone(template, stair_name, chapter_rn, addl_rn, ext_flag=True):
    """Clone template and override key fields for this stair."""
    z = copy.deepcopy(template)
    new_name = f'Sandbox_Small_Elevator_{stair_name}'
    z['Name'] = new_name
    v = z['Value']

    # Chapter
    chap_struct = get_prop(v, 'Chapter')
    rn_prop = get_prop(chap_struct['Value'], 'RowName')
    rn_prop['Value'] = chapter_rn

    # AdditionalChapters: build fresh single-entry array (or empty for cap)
    addl_prop = get_prop(v, 'AdditionalChapters')
    if addl_rn is None:
        addl_prop['Value'] = []
        # Need DummyStruct so serializer knows inner StructType
        addl_prop['DummyStruct'] = make_dummy_chapter_struct()
    else:
        addl_prop['Value'] = [make_chapter_handle_struct(addl_rn, 'AdditionalChapters')]
        # Drop DummyStruct if present (template's AdditionalChapters had real entries)
        addl_prop.pop('DummyStruct', None)

    # Position = (0,0,0)
    pos_prop = get_prop(v, 'Position')
    pos_struct = pos_prop['Value'][0]   # the IntVectorPropertyData
    pos_struct['Value'] = {
        '$type': 'UAssetAPI.UnrealTypes.FIntVector, UAssetAPI',
        'X': 0, 'Y': 0, 'Z': 0,
    }
    # TargetSize = (6,6,4)
    tgt_prop = get_prop(v, 'TargetSize')
    tgt_struct = tgt_prop['Value'][0]
    tgt_struct['Value'] = {
        '$type': 'UAssetAPI.UnrealTypes.FIntVector, UAssetAPI',
        'X': 6, 'Y': 6, 'Z': 4,
    }
    # Flags
    set_prop_value(v, 'bPositionFromLandmarks', True)
    set_prop_value(v, 'bPositionFromZoneTable', True)
    set_prop_value(v, 'EnabledState', 'ERowEnabledState::Live')

    # LandmarkHandles - single entry
    lh_prop = get_prop(v, 'LandmarkHandles')
    # Replace the single existing entry's landmark RowName, keep struct shape
    if lh_prop['Value']:
        existing = lh_prop['Value'][0]
        # Update Landmark.RowName
        lm_struct = get_prop(existing['Value'], 'Landmark')
        lm_rn = get_prop(lm_struct['Value'], 'RowName')
        lm_rn['Value'] = f'Sandbox.{stair_name}'
        # Placement -> Fixed
        place = get_prop(existing['Value'], 'Placement')
        place['Value'] = 'EZoneBubblePlacement::Fixed'
        # bExtendedConnectivityLandmark -> true
        ext = get_prop(existing['Value'], 'bExtendedConnectivityLandmark')
        ext['Value'] = bool(ext_flag)
        # Trim to single entry
        lh_prop['Value'] = [existing]

    # DisplayName: keep TableId/HistoryType, change SourceValue -> stair-suffix
    dn_prop = get_prop(v, 'DisplayName')
    if dn_prop is not None:
        # Use the SourceValue field if present; else set Value
        # In the template it uses StringTable lookup via 'Value' = 'Zones.Names.SB_Elevator_C'.
        # Set to a generic stair display key; if unknown, use Sandbox_<Stair>
        dn_prop['Value'] = f'Zones.Names.SB_Elevator_{stair_name}'

    return z


def sync_namemap(doc, names_to_add, names_to_remove):
    nm = doc.get('NameMap', [])
    nm_set = set(nm)
    for n in names_to_remove:
        if n in nm_set:
            nm.remove(n)
            nm_set.discard(n)
    for n in names_to_add:
        if n not in nm_set:
            nm.append(n)
            nm_set.add(n)
    doc['NameMap'] = nm
    # Update counts
    if 'NamesReferencedFromExportDataCount' in doc:
        doc['NamesReferencedFromExportDataCount'] = len(nm)
    gens = doc.get('Generations')
    if isinstance(gens, list) and gens:
        if 'NameCount' in gens[0]:
            gens[0]['NameCount'] = len(nm)


def main():
    zones_doc = load_json(WGR / 'DT_Moria_Zones.json')
    chaps_doc = load_json(WGR / 'DT_Moria_Chapters.json')
    bk_zones = load_json(BACKUP / 'DT_Moria_Zones.json')

    # find template
    bk_data = bk_zones['Exports'][0]['Table']['Data']
    template = next(r for r in bk_data if r['Name'] == 'Sandbox_Small_Elevator_C')

    z_data = zones_doc['Exports'][0]['Table']['Data']
    c_data = chaps_doc['Exports'][0]['Table']['Data']

    # Remove old elevator zones
    before_z = len(z_data)
    z_data[:] = [r for r in z_data if r.get('Name') not in OLD_ELEV_ZONES]
    removed_z = before_z - len(z_data)
    print(f'removed old elev zones: {removed_z}')

    # Remove old elevator chapter rows
    missing = [n for n in OLD_ELEV_CHAP_ROWS if not any(r.get('Name') == n for r in c_data)]
    if missing:
        print(f'WARNING: chapter rows not found: {missing}')
    before_c = len(c_data)
    c_data[:] = [r for r in c_data if r.get('Name') not in OLD_ELEV_CHAP_ROWS]
    removed_c = before_c - len(c_data)
    print(f'removed old elev chapter rows: {removed_c}')

    # Build & append new zones
    new_zone_names = []
    for stair_name, chap_rn, addl_rn, ext_flag in STAIR_MAP:
        new_z = build_zone(template, stair_name, chap_rn, addl_rn, ext_flag)
        z_data.append(new_z)
        new_zone_names.append(new_z['Name'])
        print(f'  appended {new_z["Name"]} primary={chap_rn} addl={addl_rn} ext={ext_flag}')

    # Sync NameMaps
    # Zones doc: add new names, remove old elev names
    sync_namemap(zones_doc, names_to_add=new_zone_names, names_to_remove=OLD_ELEV_ZONES)

    # Need to ensure new chapter row names referenced by zones exist in Zones NameMap
    referenced_chap_rows = set()
    for stair_name, chap_rn, addl_rn, _ in STAIR_MAP:
        referenced_chap_rows.add(chap_rn)
        if addl_rn:
            referenced_chap_rows.add(addl_rn)
    # Add stair landmark names to Zones NameMap (already referenced by current elevators except stairs)
    referenced_lm = set(f'Sandbox.{sn}' for sn,_,_,_ in STAIR_MAP)
    sync_namemap(zones_doc, names_to_add=list(referenced_chap_rows) + list(referenced_lm),
                 names_to_remove=[])

    # DisplayName StringTable keys: add new ones
    new_st_keys = [f'Zones.Names.SB_Elevator_{sn}' for sn,_,_,_ in STAIR_MAP]
    sync_namemap(zones_doc, names_to_add=new_st_keys, names_to_remove=[])

    # Chapters doc: remove old elev chapter row names from NameMap
    sync_namemap(chaps_doc, names_to_add=[], names_to_remove=OLD_ELEV_CHAP_ROWS)

    save_json(zones_doc, WGR / 'DT_Moria_Zones.json')
    save_json(chaps_doc, WGR / 'DT_Moria_Chapters.json')
    print('saved.')


if __name__ == '__main__':
    main()
