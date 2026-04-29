"""Rebuild stairs as 5 SHORT stairs (TS.Z=1, bExtendFootprint=false).

Step 1: Backup 4 files to backups/before_5stair_rebuild/
Step 2: Remove the 8 stair zones (Sandbox_Small_Elevator_*Ascent/Descent/GroundStair) and 8 landmarks (Sandbox.*Ascent/*Descent/GroundStair)
Step 3: Read chapter PrimeZ from DT_Moria_Chapters.json
Step 4: Add 5 new stair zones+landmarks
Step 5: NameMap sync
"""
import json, sys, io, copy, shutil
from pathlib import Path
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

ROOT = Path(__file__).parent
BACKUP_DIR = ROOT / 'backups' / 'before_5stair_rebuild'

FILES = ['DT_Moria_Zones.json','DT_Moria_Landmarks.json','DT_Moria_LayoutConnections.json','World.json']

# === Step 1: backup ===
BACKUP_DIR.mkdir(parents=True, exist_ok=True)
for fn in FILES:
    src = ROOT / fn
    dst = BACKUP_DIR / fn
    shutil.copy2(src, dst)
print(f'[1] Backed up {len(FILES)} files to {BACKUP_DIR}')

# === Loaders ===
def load(fn): return json.load(open(ROOT/fn,encoding='utf-8'))
def save(fn,d):
    with open(ROOT/fn,'w',encoding='utf-8') as f:
        json.dump(d,f,indent=2,ensure_ascii=False)

z = load('DT_Moria_Zones.json')
lm = load('DT_Moria_Landmarks.json')
lc = load('DT_Moria_LayoutConnections.json')
ch = load('DT_Moria_Chapters.json')

# === Helpers ===
def fp(v,n):
    for p in v or []:
        if isinstance(p,dict) and p.get('Name')==n: return p
    return None
def gv_intvec(p):
    v=p.get('Value') if p else None
    if isinstance(v,list) and v:
        d=v[0].get('Value') if isinstance(v[0],dict) else None
        if isinstance(d,dict): return (d.get('X'),d.get('Y'),d.get('Z'))
    return None
def set_intvec(p, x, y, zz):
    p['Value'][0]['Value']['X']=x
    p['Value'][0]['Value']['Y']=y
    p['Value'][0]['Value']['Z']=zz
def gf_rowname(r,k):
    p=fp(r['Value'],k); v=p.get('Value') if p else None
    if isinstance(v,list):
        for it in v:
            if isinstance(it,dict) and it.get('Name')=='RowName': return it.get('Value','')
    return v
def st(r):
    p=fp(r.get('Value',[]),'EnabledState')
    return str(p.get('Value','')).split('::')[-1] if p else None

# === Step 2: remove old 8 stair zones/landmarks/connections ===
OLD_ZONES = {
    'Sandbox_Small_Elevator_TopAscent','Sandbox_Small_Elevator_UpperAscent',
    'Sandbox_Small_Elevator_HighAscent','Sandbox_Small_Elevator_MidAscent',
    'Sandbox_Small_Elevator_GroundStair','Sandbox_Small_Elevator_UpperDescent',
    'Sandbox_Small_Elevator_MidDescent','Sandbox_Small_Elevator_LowerDescent',
}
OLD_LMS = {
    'Sandbox.TopAscent','Sandbox.UpperAscent','Sandbox.HighAscent','Sandbox.MidAscent',
    'Sandbox.GroundStair','Sandbox.UpperDescent','Sandbox.MidDescent','Sandbox.LowerDescent',
}

z_data = z['Exports'][0]['Table']['Data']
z_before = len(z_data)
z['Exports'][0]['Table']['Data'] = [r for r in z_data if r['Name'] not in OLD_ZONES]
z_data = z['Exports'][0]['Table']['Data']
removed_zones = z_before - len(z_data)

lm_data = lm['Exports'][0]['Table']['Data']
lm_before = len(lm_data)
lm['Exports'][0]['Table']['Data'] = [r for r in lm_data if r['Name'] not in OLD_LMS]
lm_data = lm['Exports'][0]['Table']['Data']
removed_lms = lm_before - len(lm_data)

# Connections referencing old landmarks
lc_data = lc['Exports'][0]['Table']['Data']
lc_before = len(lc_data)
def conn_refs_old(r):
    o = gf_rowname(r,'OriginLandmark')
    d = gf_rowname(r,'DestinationLandmark')
    return o in OLD_LMS or d in OLD_LMS
removed_conns = [r['Name'] for r in lc_data if conn_refs_old(r)]
lc['Exports'][0]['Table']['Data'] = [r for r in lc_data if not conn_refs_old(r)]
lc_data = lc['Exports'][0]['Table']['Data']

print(f'[2] Removed: {removed_zones} zones, {removed_lms} landmarks, {len(removed_conns)} connections')
if removed_conns:
    print(f'    Removed conns: {removed_conns}')

# === Step 3: chapter PrimeZ map ===
chap_pz = {}
for r in ch['Exports'][0]['Table']['Data']:
    n = r['Name']
    if not n.startswith('SandboxSmall-chapter'): continue
    if st(r) == 'Disabled': continue
    chap_pz[n] = gf_rowname(r,'PrimeZ')
print('[3] Chapter PrimeZ map:')
for k,v in chap_pz.items(): print(f'    {k} = {v}')

# === Step 4: build 5 new stair zones+landmarks ===
# Find Elevator_C as zone template, Sandbox.FirstStair as landmark template
ZONE_TEMPLATE = None
for r in z_data:
    if r['Name'] == 'Sandbox_Small_Elevator_C':
        ZONE_TEMPLATE = r
        break
if ZONE_TEMPLATE is None:
    raise SystemExit('ERROR: cannot find Sandbox_Small_Elevator_C as template')

LM_TEMPLATE = None
for r in lm_data:
    if r['Name'] == 'Sandbox.FirstStair':
        LM_TEMPLATE = r
        break
if LM_TEMPLATE is None:
    raise SystemExit('ERROR: cannot find Sandbox.FirstStair as template')

# 5-stair plan
NEW_STAIRS = [
    # zone_name, lm_name, primary_chap, additional_chaps
    ('Sandbox_Small_TopStair',    'Sandbox.TopStair',    'SandboxSmall-chapter-11', ['SandboxSmall-chapter-10','SandboxSmall-chapter-9']),
    ('Sandbox_Small_UpperStair',  'Sandbox.UpperStair',  'SandboxSmall-chapter-3',  ['SandboxSmall-chapter-4','SandboxSmall-chapter-2']),
    ('Sandbox_Small_GroundStair', 'Sandbox.GroundStair', 'SandboxSmall-chapter-1',  ['SandboxSmall-chapter-2','SandboxSmall-chapter-5']),
    ('Sandbox_Small_MidDeepStair','Sandbox.MidDeepStair','SandboxSmall-chapter-7',  ['SandboxSmall-chapter-6','SandboxSmall-chapter-8','SandboxSmall-chapter-5']),
    ('Sandbox_Small_BottomStair', 'Sandbox.BottomStair', 'SandboxSmall-chapter-14', ['SandboxSmall-chapter-13','SandboxSmall-chapter-12']),
]

def make_chapter_struct(rowname, name='AdditionalChapters'):
    return {
        "$type": "UAssetAPI.PropertyTypes.Structs.StructPropertyData, UAssetAPI",
        "StructType": "MorChapterRowHandle",
        "SerializeNone": True,
        "StructGUID": "{00000000-0000-0000-0000-000000000000}",
        "SerializationControl": "NoExtension",
        "Operation": "None",
        "Name": name,
        "ArrayIndex": 0, "IsZero": False, "PropertyTagFlags": "None", "PropertyTagExtensions": "NoExtension",
        "Value": [{
            "$type": "UAssetAPI.PropertyTypes.Objects.NamePropertyData, UAssetAPI",
            "Name":"RowName","ArrayIndex":0,"IsZero":False,
            "PropertyTagFlags":"None","PropertyTagExtensions":"NoExtension",
            "Value":rowname
        }]
    }

def build_zone(zone_name, lm_name, primary_chap, addl_chaps, pz):
    new = copy.deepcopy(ZONE_TEMPLATE)
    new['Name'] = zone_name
    # Set Chapter
    chap_p = fp(new['Value'], 'Chapter')
    chap_p['Value'][0]['Value'] = primary_chap
    # Set AdditionalChapters
    addl_p = fp(new['Value'], 'AdditionalChapters')
    addl_p['Value'] = [make_chapter_struct(c) for c in addl_chaps]
    # TargetSize Z=1 (preserve X/Y from Elevator_C which is some value)
    ts_p = fp(new['Value'], 'TargetSize')
    cur = ts_p['Value'][0]['Value']
    set_intvec(ts_p, cur['X'], cur['Y'], 1)
    # Position (0,0,0)
    pos_p = fp(new['Value'], 'Position')
    set_intvec(pos_p, 0, 0, 0)
    # bExtendFootprint = false
    bef = fp(new['Value'], 'bExtendFootprint')
    if bef is None:
        new['Value'].append({"$type":"UAssetAPI.PropertyTypes.Objects.BoolPropertyData, UAssetAPI",
                             "Name":"bExtendFootprint","ArrayIndex":0,"IsZero":False,
                             "PropertyTagFlags":"None","PropertyTagExtensions":"NoExtension","Value":False})
    else:
        bef['Value'] = False
    # bPositionFromLandmarks = true
    bpfl = fp(new['Value'], 'bPositionFromLandmarks')
    if bpfl is None:
        new['Value'].append({"$type":"UAssetAPI.PropertyTypes.Objects.BoolPropertyData, UAssetAPI",
                             "Name":"bPositionFromLandmarks","ArrayIndex":0,"IsZero":False,
                             "PropertyTagFlags":"None","PropertyTagExtensions":"NoExtension","Value":True})
    else:
        bpfl['Value'] = True
    # LandmarkHandles → [ {Landmark: lm_name, Placement: Fixed, bExtendedConnectivityLandmark: true} ]
    lh_p = fp(new['Value'], 'LandmarkHandles')
    handle = {
        "$type":"UAssetAPI.PropertyTypes.Structs.StructPropertyData, UAssetAPI",
        "StructType":"MorZoneLandmarkEntry","SerializeNone":True,
        "StructGUID":"{00000000-0000-0000-0000-000000000000}","SerializationControl":"NoExtension","Operation":"None",
        "Name":"LandmarkHandles","ArrayIndex":0,"IsZero":False,
        "PropertyTagFlags":"None","PropertyTagExtensions":"NoExtension",
        "Value":[
            {"$type":"UAssetAPI.PropertyTypes.Structs.StructPropertyData, UAssetAPI",
             "StructType":"MorLandmarkRowHandle","SerializeNone":True,
             "StructGUID":"{00000000-0000-0000-0000-000000000000}","SerializationControl":"NoExtension","Operation":"None",
             "Name":"Landmark","ArrayIndex":0,"IsZero":False,
             "PropertyTagFlags":"None","PropertyTagExtensions":"NoExtension",
             "Value":[{"$type":"UAssetAPI.PropertyTypes.Objects.NamePropertyData, UAssetAPI",
                       "Name":"RowName","ArrayIndex":0,"IsZero":False,
                       "PropertyTagFlags":"None","PropertyTagExtensions":"NoExtension","Value":lm_name}]},
            {"$type":"UAssetAPI.PropertyTypes.Objects.EnumPropertyData, UAssetAPI",
             "EnumType":"EZoneBubblePlacement","InnerType":None,
             "Name":"Placement","ArrayIndex":0,"IsZero":False,
             "PropertyTagFlags":"None","PropertyTagExtensions":"NoExtension",
             "Value":"ELandmarkPlacement::Fixed"},
            {"$type":"UAssetAPI.PropertyTypes.Objects.BoolPropertyData, UAssetAPI",
             "Name":"bExtendedConnectivityLandmark","ArrayIndex":0,"IsZero":False,
             "PropertyTagFlags":"None","PropertyTagExtensions":"NoExtension","Value":True},
        ]
    }
    if lh_p is None:
        new['Value'].append({"$type":"UAssetAPI.PropertyTypes.Objects.ArrayPropertyData, UAssetAPI",
                             "ArrayType":"StructProperty","Name":"LandmarkHandles","ArrayIndex":0,"IsZero":False,
                             "PropertyTagFlags":"None","PropertyTagExtensions":"NoExtension",
                             "Value":[handle]})
    else:
        lh_p['Value'] = [handle]
    return new

def build_landmark(lm_name, base_z):
    new = copy.deepcopy(LM_TEMPLATE)
    new['Name'] = lm_name
    # BasePosition (0,0, base_z)
    bp_p = fp(new['Value'], 'BasePosition')
    set_intvec(bp_p, 0, 0, base_z)
    # InternalId tag = World.Landmark.<lm_name>
    iid_p = fp(new['Value'], 'InternalId')
    if iid_p:
        iid_p['Value'][0]['Value'] = f'World.Landmark.{lm_name}'
    # DisplayName -> Landmarks.<lm_name>
    dn_p = fp(new['Value'], 'DisplayName')
    if dn_p:
        dn_p['Value'] = f'Landmarks.{lm_name}'
    # Ensure EnabledState=Live
    es_p = fp(new['Value'], 'EnabledState')
    if es_p:
        es_p['Value'] = 'ERowEnabledState::Live'
    return new

added_zones = []
added_lms = []
for zname, lname, prim, addl in NEW_STAIRS:
    pz = chap_pz[prim]
    zr = build_zone(zname, lname, prim, addl, pz)
    lr = build_landmark(lname, pz)
    z_data.append(zr)
    lm_data.append(lr)
    added_zones.append((zname, prim, pz, addl))
    added_lms.append((lname, pz))

print(f'[4] Added {len(added_zones)} zones and {len(added_lms)} landmarks')
for n,p,pz,a in added_zones:
    print(f'    {n} chapter={p} BP.Z={pz} additional={a}')

# === Step 5: NameMap sync ===
def sync_namemap(d, fname):
    # Collect all string-like values that might be FNames
    needed = set()
    def walk(o):
        if isinstance(o,dict):
            for k,v in o.items():
                if isinstance(v,(dict,list)): walk(v)
                elif isinstance(v,str):
                    # FName-bearing keys
                    if k in ('Name','Value','RowName','TagName','EnumType','InnerType','StructType','EnumValue','ResourceName'):
                        needed.add(v)
        elif isinstance(o,list):
            for it in o: walk(it)
    walk(d.get('Exports',[]))
    walk(d.get('Imports',[]))
    nm = d.get('NameMap',[])
    nm_set = set(nm)
    added = 0
    for s in sorted(needed):
        if not isinstance(s,str): continue
        # Strip enum prefixes like ERowEnabledState::Live; both halves go to NameMap typically (just the suffix)
        # But UAssetGUI handles enums via separate NameMap entries; safest to add the raw values that appear as Name, RowName, TagName, ResourceName
        pass
    # More conservative: only add strings used as Name fields, RowName, TagName (these are the FName-typed ones)
    fname_strings = set()
    def walk2(o):
        if isinstance(o,dict):
            # Each property has a "Name" that is an FName
            n = o.get('Name')
            if isinstance(n,str): fname_strings.add(n)
            # Specific value-bearing FName fields
            for vk in ('Value',):
                v = o.get(vk)
                if isinstance(v,str):
                    nk = o.get('Name')
                    # NamePropertyData -> Value is FName
                    if o.get('$type','').endswith('NamePropertyData, UAssetAPI'):
                        fname_strings.add(v)
                    # Enums with :: -> the whole string and its halves often appear in NameMap
                    if '::' in v:
                        fname_strings.add(v)
                        a,b = v.split('::',1)
                        fname_strings.add(a); fname_strings.add(b)
            # Value can be list (handled in walk recursion)
            for k,v in o.items():
                if isinstance(v,(dict,list)): walk2(v)
        elif isinstance(o,list):
            for it in o: walk2(it)
    walk2(d.get('Exports',[]))
    new_entries = [s for s in fname_strings if s not in nm_set and s != '' and s is not None]
    nm.extend(new_entries)
    d['NameMap'] = nm
    nm_len = len(nm)
    d['NamesReferencedFromExportDataCount'] = nm_len
    g = d.get('Generations') or []
    if g and isinstance(g, list):
        g[0]['NameCount'] = nm_len
    print(f'    {fname}: NameMap len={nm_len}, added {len(new_entries)} new entries')

print('[5] Syncing NameMaps...')
sync_namemap(z, 'DT_Moria_Zones.json')
sync_namemap(lm, 'DT_Moria_Landmarks.json')
sync_namemap(lc, 'DT_Moria_LayoutConnections.json')

# === Save ===
save('DT_Moria_Zones.json', z)
save('DT_Moria_Landmarks.json', lm)
save('DT_Moria_LayoutConnections.json', lc)

print('\nDONE — files saved.')
print('Summary of additions:')
for (zname,p,pz,a),(lname,bz) in zip(added_zones, added_lms):
    print(f'  Zone {zname} (chapter={p}, addl={a}) + Landmark {lname} (BP.Z={bz})')
