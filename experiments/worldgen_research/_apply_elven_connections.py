"""Apply Interpretation B: mirror campaign ElvenQuarterEntrance/Promenade
connections as Sandbox-flavored.

  - Add 2 new Sandbox.* landmarks (Sandbox.ElvenQuarterEntrance,
    Sandbox.BlockedHighwayWestTown) with campaign DisplayName keys.
  - Re-enable Sandbox.ElvenQuarterPromenade (Disabled -> Live).
  - Update GuaranteedConnections on the 2 Sandbox landmarks.
  - Add 3 new Sandbox-flavored LayoutConnection rows.
  - Use Sandbox.Deep1MineNexus instead of creating Sandbox.MinesHeroShot.
"""
import json
import copy

LM_PATH = 'DT_Moria_Landmarks.json'
LC_PATH = 'DT_Moria_LayoutConnections.json'

def fp(v, n):
    for p in v or []:
        if isinstance(p, dict) and p.get('Name') == n:
            return p
    return None


def get_row(d, name):
    for r in d['Exports'][0]['Table']['Data']:
        if r['Name'] == name:
            return r
    return None


def set_text_key(prop, key, table_id='/Game/Tech/Data/StringTables/World.World'):
    if not prop:
        return
    prop['HistoryType'] = 'StringTableEntry'
    prop['TableId'] = table_id
    prop['Value'] = key
    prop['Namespace'] = None
    prop['CultureInvariantString'] = None


lm = json.load(open(LM_PATH, encoding='utf-8'))
lc = json.load(open(LC_PATH, encoding='utf-8'))

# ============================================================
# 1) Add 2 new landmarks: Sandbox.ElvenQuarterEntrance, Sandbox.BlockedHighwayWestTown
# ============================================================
template = get_row(lm, 'Sandbox.DoorsOfDurin')
assert template, 'Sandbox.DoorsOfDurin template not found'

NEW_LANDMARKS = [
    ('Sandbox.ElvenQuarterEntrance',   'BB_Chapter2_ElvenQuarterEntrance',  'Zones.Names.ElvenQuarter.Banner'),
    ('Sandbox.BlockedHighwayWestTown', 'BB_Chapter2_BlockedHighwayWestTown','Landmarks.Ch2.BlockedHighwayWestTown'),
]

existing_lm = {r['Name'] for r in lm['Exports'][0]['Table']['Data']}
for new_name, bub, dn_key in NEW_LANDMARKS:
    if new_name in existing_lm:
        print(f'  Landmark {new_name} already exists - skip')
        continue
    clone = copy.deepcopy(template)
    clone['Name'] = new_name

    # BaseBubbleName
    bp = fp(clone['Value'], 'BaseBubbleName')
    if bp:
        bp['Value'] = bub

    # DisplayName -> StringTable key
    dn = fp(clone['Value'], 'DisplayName')
    set_text_key(dn, dn_key)

    # BasePosition -> (0,0,0) (we don't pin it)
    bpos = fp(clone['Value'], 'BasePosition')
    if bpos:
        val = bpos.get('Value')
        if isinstance(val, list) and val and isinstance(val[0], dict) and isinstance(val[0].get('Value'), dict):
            val[0]['Value']['X'] = 0
            val[0]['Value']['Y'] = 0
            val[0]['Value']['Z'] = 0

    # Clear any inherited GuaranteedConnections
    gc = fp(clone['Value'], 'GuaranteedConnections')
    if gc:
        gc['Value'] = []

    # EnabledState = Live
    es = fp(clone['Value'], 'EnabledState')
    if es:
        es['Value'] = 'ERowEnabledState::Live'

    lm['Exports'][0]['Table']['Data'].append(clone)
    print(f'  +Landmark {new_name}  bubble={bub}  DisplayName={dn_key}')

# ============================================================
# 2) Re-enable Sandbox.ElvenQuarterPromenade
# ============================================================
prom = get_row(lm, 'Sandbox.ElvenQuarterPromenade')
if prom:
    es = fp(prom['Value'], 'EnabledState')
    if es:
        old = es.get('Value')
        es['Value'] = 'ERowEnabledState::Live'
        print(f'  Sandbox.ElvenQuarterPromenade EnabledState: {old} -> Live')

# ============================================================
# 3) Update GuaranteedConnections
# ============================================================

def add_gc(landmark_row, target_landmark_names):
    gc = fp(landmark_row['Value'], 'GuaranteedConnections')
    if not gc:
        return
    val = gc.get('Value') or []
    # GameplayTag struct shape: each entry is an Array of struct, with TagName=World.Landmark.<name>
    # Use template from another landmark that has GuaranteedConnections
    template_lm = None
    for r in lm['Exports'][0]['Table']['Data']:
        gtest = fp(r['Value'], 'GuaranteedConnections')
        if gtest and (gtest.get('Value') or []):
            template_lm = gtest.get('Value')[0]
            break
    if not template_lm:
        print('   ! Could not find a GuaranteedConnections template')
        return
    for tn in target_landmark_names:
        new_entry = copy.deepcopy(template_lm)
        # Walk and replace TagName
        def fix_tag(o):
            if isinstance(o, dict):
                if o.get('Name') == 'TagName':
                    o['Value'] = f'World.Landmark.{tn}'
                for v in o.values():
                    fix_tag(v)
            elif isinstance(o, list):
                for it in o:
                    fix_tag(it)
        fix_tag(new_entry)
        val.append(new_entry)
    gc['Value'] = val


# Sandbox.ElvenQuarterPromenade -> Sandbox.Deep1MineNexus, Sandbox.ElvenQuarterEntrance
prom = get_row(lm, 'Sandbox.ElvenQuarterPromenade')
if prom:
    # First clear
    gc = fp(prom['Value'], 'GuaranteedConnections')
    if gc:
        gc['Value'] = []
    add_gc(prom, ['Sandbox.Deep1MineNexus', 'Sandbox.ElvenQuarterEntrance'])
    print('  Sandbox.ElvenQuarterPromenade.GuaranteedConnections = '
          '[Sandbox.Deep1MineNexus, Sandbox.ElvenQuarterEntrance]')

# Sandbox.ElvenQuarterEntrance -> Sandbox.BlockedHighwayWestTown
ent = get_row(lm, 'Sandbox.ElvenQuarterEntrance')
if ent:
    add_gc(ent, ['Sandbox.BlockedHighwayWestTown'])
    print('  Sandbox.ElvenQuarterEntrance.GuaranteedConnections = '
          '[Sandbox.BlockedHighwayWestTown]')

# ============================================================
# 4) Add 3 new LayoutConnection rows (Sandbox-flavored)
# ============================================================
# Use a vanilla Sandbox-side template — find one with LandmarkInterface kind
template_conn = None
for r in lc['Exports'][0]['Table']['Data']:
    if r['Name'] == 'WesternTownToElvenQuarter':  # campaign one - same kind
        template_conn = r
        break
assert template_conn, 'WesternTownToElvenQuarter template not found'


def set_rowname(prop, value):
    if not prop:
        return
    val = prop.get('Value')
    if isinstance(val, list):
        for it in val:
            if isinstance(it, dict) and it.get('Name') == 'RowName':
                it['Value'] = value


def set_enum(prop, value):
    if prop:
        prop['Value'] = value


NEW_CONNS = [
    # (RowName, OriginLandmark, DestinationLandmark, OriginZone, DestinationZone)
    ('Sandbox_DoorsOfDurinToElvenEntrance',
     'Sandbox.DoorsOfDurin', 'Sandbox.ElvenQuarterEntrance',
     None, None),
    ('Sandbox_ElvenEntranceToPromenade',
     'Sandbox.ElvenQuarterEntrance', 'Sandbox.ElvenQuarterPromenade',
     None, None),
    ('Sandbox_PromenadeToMines',
     'Sandbox.ElvenQuarterPromenade', 'Sandbox.Deep1MineNexus',
     None, None),
]

existing_conn = {r['Name'] for r in lc['Exports'][0]['Table']['Data']}
for new_name, ol, dl, oz, dz in NEW_CONNS:
    if new_name in existing_conn:
        print(f'  Connection {new_name} already exists - skip')
        continue
    clone = copy.deepcopy(template_conn)
    clone['Name'] = new_name

    # ZoneSet
    zs = fp(clone['Value'], 'ZoneSet')
    if zs:
        zs['Value'] = 'EZoneSet::SandboxSmall'

    # OriginLandmark / DestinationLandmark
    set_rowname(fp(clone['Value'], 'OriginLandmark'), ol)
    set_rowname(fp(clone['Value'], 'DestinationLandmark'), dl)

    # Clear OriginZone/DestinationZone (None means landmark-only)
    if oz is None:
        oprop = fp(clone['Value'], 'OriginZone')
        if oprop:
            val = oprop.get('Value')
            if isinstance(val, list):
                for it in val:
                    if isinstance(it, dict) and it.get('Name') == 'RowName':
                        it['Value'] = None
    if dz is None:
        dprop = fp(clone['Value'], 'DestinationZone')
        if dprop:
            val = dprop.get('Value')
            if isinstance(val, list):
                for it in val:
                    if isinstance(it, dict) and it.get('Name') == 'RowName':
                        it['Value'] = None

    # OriginKind = LandmarkInterface, DestinationKind = LandmarkInterface
    set_enum(fp(clone['Value'], 'OriginKind'),
             'EMorLayoutConnectionEndpointKind::LandmarkInterface')
    set_enum(fp(clone['Value'], 'DestinationKind'),
             'EMorLayoutConnectionEndpointKind::LandmarkInterface')

    # ZoneRule = Shared, bRequired = True, bExclusive = False
    set_enum(fp(clone['Value'], 'ZoneRule'), 'EMorLayoutConnectionZoneRule::Shared')
    req = fp(clone['Value'], 'bRequired')
    if req:
        req['Value'] = True
    exc = fp(clone['Value'], 'bExclusive')
    if exc:
        exc['Value'] = False

    # EnabledState = Live
    es = fp(clone['Value'], 'EnabledState')
    if es:
        es['Value'] = 'ERowEnabledState::Live'

    lc['Exports'][0]['Table']['Data'].append(clone)
    print(f'  +Connection {new_name}: {ol} -> {dl}')

# ============================================================
# 5) Sync NameMaps
# ============================================================

def add_nm(d, names):
    nm = d.get('NameMap', [])
    existing = set(nm)
    added = 0
    for n in names:
        if n is None: continue
        if n not in existing:
            nm.append(n); existing.add(n); added += 1
    d['NameMap'] = nm
    if 'NamesReferencedFromExportDataCount' in d:
        d['NamesReferencedFromExportDataCount'] = len(nm)
    exp0 = d['Exports'][0]
    if 'Generations' in exp0 and exp0['Generations']:
        exp0['Generations'][0]['NameCount'] = len(nm)
    return added

lm_added = add_nm(lm, [
    'Sandbox.ElvenQuarterEntrance', 'Sandbox.BlockedHighwayWestTown',
    'BB_Chapter2_ElvenQuarterEntrance', 'BB_Chapter2_BlockedHighwayWestTown',
    'Zones.Names.ElvenQuarter.Banner', 'Landmarks.Ch2.BlockedHighwayWestTown',
])
lc_added = add_nm(lc, [
    'Sandbox_DoorsOfDurinToElvenEntrance',
    'Sandbox_ElvenEntranceToPromenade',
    'Sandbox_PromenadeToMines',
    'Sandbox.ElvenQuarterEntrance', 'Sandbox.BlockedHighwayWestTown',
    'Sandbox.ElvenQuarterPromenade', 'Sandbox.DoorsOfDurin',
    'Sandbox.Deep1MineNexus',
])
print(f'  Landmarks NameMap +{lm_added}')
print(f'  LayoutConnections NameMap +{lc_added}')

json.dump(lm, open(LM_PATH, 'w', encoding='utf-8'), indent=2)
json.dump(lc, open(LC_PATH, 'w', encoding='utf-8'), indent=2)
print('\nApplied.')
