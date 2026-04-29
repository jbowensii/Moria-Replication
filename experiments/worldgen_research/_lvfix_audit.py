"""Comprehensive Lv-fix audit (Tasks 1 + 3)."""
import json, os
from collections import defaultdict

ROOT = os.path.dirname(os.path.abspath(__file__))
def load(n):
    with open(os.path.join(ROOT,n),'r',encoding='utf-8') as f: return json.load(f)

zones = load('DT_Moria_Zones.json')
landmarks = load('DT_Moria_Landmarks.json')
connections = load('DT_Moria_LayoutConnections.json')
chapters = load('DT_Moria_Chapters.json')

def rows(dt): return dt['Exports'][0]['Table']['Data']

zone_rows = rows(zones)
lm_rows = rows(landmarks)
conn_rows = rows(connections)
chap_rows = rows(chapters)

def props(row):
    return {p.get('Name'): p for p in row.get('Value',[]) if isinstance(p,dict)}

def get_intvec(row, name):
    """For Position/TargetSize/BasePosition struct -> child IntVectorPropertyData with Value{X,Y,Z}."""
    p = props(row).get(name)
    if not p: return None
    inner = p.get('Value',[])
    if isinstance(inner, list):
        for sp in inner:
            if isinstance(sp,dict) and sp.get('$type','').endswith('IntVectorPropertyData, UAssetAPI'):
                v = sp.get('Value',{})
                return (v.get('X'), v.get('Y'), v.get('Z'))
    return None

def get_rowname(row, prop_name):
    """For struct properties wrapping a MorXxxRowHandle -> RowName NameProperty."""
    p = props(row).get(prop_name)
    if not p: return None
    inner = p.get('Value',[])
    if isinstance(inner, list):
        for sp in inner:
            if isinstance(sp,dict) and sp.get('Name')=='RowName':
                return sp.get('Value')
    return None

def get_enabled(row):
    p = props(row).get('EnabledState')
    if not p: return None
    return p.get('Value')

def get_array(row, name):
    p = props(row).get(name)
    if not p: return []
    v = p.get('Value', [])
    return v if isinstance(v, list) else []

def is_live(row):
    e = get_enabled(row)
    return e is None or 'Live' in str(e)

# --- Build lookups ---
lm_by_name = {r['Name']:r for r in lm_rows}
zone_by_name = {r['Name']:r for r in zone_rows}
chap_by_name = {r['Name']:r for r in chap_rows}

def zone_footprint(z):
    pos = get_intvec(z,'Position')
    sz = get_intvec(z,'TargetSize')
    if not pos or not sz or None in pos or None in sz: return None
    px,py,pz=pos; sx,sy,sz_=sz
    return {'pos':pos,'size':sz,'xmin':px,'xmax':px+sx-1,'ymin':py,'ymax':py+sy-1,'zmin':pz,'zmax':pz+sz_-1}

def lm_handles(z):
    """Parse LandmarkHandles array. Each entry has Landmark (RowHandle), Placement (enum), bExtendedConnectivityLandmark (bool)."""
    arr = get_array(z, 'LandmarkHandles')
    out = []
    for entry in arr:
        if not isinstance(entry, dict): continue
        sub = entry.get('Value', [])
        lm_ref = None; ext = None; placement = None
        for sp in sub:
            if not isinstance(sp,dict): continue
            nm = sp.get('Name')
            if nm == 'Landmark':
                inner = sp.get('Value',[])
                if isinstance(inner,list):
                    for q in inner:
                        if isinstance(q,dict) and q.get('Name')=='RowName':
                            lm_ref = q.get('Value')
            elif nm == 'bExtendedConnectivityLandmark':
                ext = sp.get('Value')
            elif nm == 'Placement':
                placement = sp.get('Value')
        out.append({'lm':lm_ref,'ext':ext,'placement':placement})
    return out

# --- SS zones ---
def is_ss(z):
    p = props(z).get('ZoneSet')
    if p:
        v = p.get('Value','')
        if 'SandboxSmall' in str(v): return True
        if str(v).endswith('::All'): return True
    return z['Name'].startswith('Sandbox_Small_')

ss_zones = [z for z in zone_rows if z['Name'].startswith('Sandbox_Small_') and is_live(z)]
print(f"Live SS zones: {len(ss_zones)}")

# === Task 1 ===
print("\n=== TASK 1: BasePosition vs zone footprint ===")
out_of_range = []
zone_lm_info = {}

for z in ss_zones:
    zname = z['Name']
    fp = zone_footprint(z)
    if not fp: continue
    handles = lm_handles(z)
    if not handles: continue
    info = []
    for h in handles:
        lname = h['lm']
        if not lname or lname == 'None': continue
        lr = lm_by_name.get(lname)
        if not lr:
            info.append((lname, None, h['ext'], 'LM_MISSING'))
            continue
        bp = get_intvec(lr, 'BasePosition')
        if not bp or None in bp:
            info.append((lname, bp, h['ext'], 'NO_BP'))
            continue
        bx,by,bz=bp
        in_x = fp['xmin']<=bx<=fp['xmax']
        in_y = fp['ymin']<=by<=fp['ymax']
        in_z = fp['zmin']<=bz<=fp['zmax']
        ok = in_x and in_y and in_z
        placement = h.get('placement')
        is_fixed = placement and 'Fixed' in str(placement)
        status = 'OK' if ok else f"OUT(x={in_x} y={in_y} z={in_z})"
        if not ok and not is_fixed:
            status += f" [placement={placement} - not Fixed, may be intentional]"
        info.append((lname, bp, h['ext'], status))
        if not ok and is_fixed:
            out_of_range.append({'zone':zname,'lm':lname,'bp':bp,'ext':h['ext'],'fp':fp,'placement':placement})
    if info:
        zone_lm_info[zname] = (fp, info)

for zn,(fp,info) in zone_lm_info.items():
    print(f"\n{zn}  pos={fp['pos']} size={fp['size']}  X[{fp['xmin']}..{fp['xmax']}] Y[{fp['ymin']}..{fp['ymax']}] Z[{fp['zmin']}..{fp['zmax']}]")
    for lname, bp, ext, status in info:
        print(f"    {lname:35s} BP={bp} ext={ext}  {status}")

print(f"\n>>> OUT-OF-RANGE COUNT: {len(out_of_range)}")
for o in out_of_range:
    print(f"   {o['lm']} BP={o['bp']} not in {o['zone']} fp")

# === Task 3A: Layout connection landmark Z coverage ===
print("\n=== TASK 3A: LayoutConnection landmark Z coverage ===")

def conn_lms(c):
    o = get_rowname(c,'OriginLandmark')
    d = get_rowname(c,'DestinationLandmark')
    return o, d

def conn_zones(c):
    o = get_rowname(c,'OriginZone')
    d = get_rowname(c,'DestinationZone')
    return o, d

def lm_z(name):
    if not name or name=='None': return None
    r = lm_by_name.get(name)
    if not r: return None
    bp = get_intvec(r,'BasePosition')
    return bp[2] if bp else None

ss_conns = []
for c in conn_rows:
    p = props(c).get('ZoneSet',{})
    zs = p.get('Value','') if p else ''
    if 'SandboxSmall' in str(zs) or 'All' in str(zs):
        if is_live(c):
            ss_conns.append(c)
print(f"Live SS-applicable connections: {len(ss_conns)} of {len(conn_rows)} total")

z_endpoint_count = defaultdict(int)
z_pair_count = defaultdict(int)
above_lv3 = 0  # Lv-4+ -> BP Z>21 (Lv-1=18, Lv-2=19, Lv-3=20, Lv-4=21+)
# Actually re-examine: Elevator_B Z=18..25 covers Lv-1..Lv-7; Lv-1=18,Lv-2=19,Lv-3=20,Lv-4=21,Lv-5=22,Lv-6=23,Lv-7=24
# D-1=17,D-2=16,D-3=15,D-4=14...
below_d3 = 0
for c in ss_conns:
    o,d = conn_lms(c)
    oz = lm_z(o); dz = lm_z(d)
    if oz is not None: z_endpoint_count[oz]+=1
    if dz is not None: z_endpoint_count[dz]+=1
    if oz is not None and dz is not None:
        z_pair_count[(min(oz,dz),max(oz,dz))]+=1

print("Endpoint Z histogram (per SS connection endpoint):")
for z in sorted(z_endpoint_count):
    print(f"  Z={z}: {z_endpoint_count[z]}")
print("Z pair histogram (zmin,zmax):")
for k in sorted(z_pair_count):
    print(f"  {k}: {z_pair_count[k]}")

# Bucket vs floor mapping
floor_z = {'D-7':11,'D-6':12,'D-5':13,'D-4':14,'D-3':15,'D-2':16,'D-1':17,
           'Lv-1':18,'Lv-2':19,'Lv-3':20,'Lv-4':21,'Lv-5':22,'Lv-6':23,'Lv-7':24}
print("\nFloor coverage (endpoints touching exact floor Z):")
for fl, z in floor_z.items():
    print(f"  {fl} (Z={z}): {z_endpoint_count.get(z,0)} endpoints")

# === Task 3B: Stair GuaranteedConnections ===
print("\n=== TASK 3B: Stair GuaranteedConnections ===")
stair_keys = [k for k in lm_by_name if any(s in k for s in
    ['FirstStair','SecondStair','ThirdStair','FourthStair','FifthStair','SixthStair',
     'SeventhStair','EighthStair','NinthStair','TenthStair','EleventhStair',
     'CrystalDescent','LowerDescent'])]
for k in stair_keys:
    r = lm_by_name[k]
    bp = get_intvec(r,'BasePosition')
    gc = get_array(r,'GuaranteedConnections')
    print(f"  {k:40s} BP={bp} GC={len(gc)}")
    for tag in gc[:5]:
        # GuaranteedConnections is GameplayTag; print TagName
        if isinstance(tag,dict):
            sub = tag.get('Value',[])
            tn = None
            if isinstance(sub,list):
                for sp in sub:
                    if isinstance(sp,dict) and sp.get('Name')=='TagName':
                        tn = sp.get('Value')
            print(f"      tag: {tn}")

# === Task 3C: bExt flags on elevator zones ===
print("\n=== TASK 3C: Elevator ext flag review ===")
for zn,(fp,info) in zone_lm_info.items():
    if 'Elevator' not in zn: continue
    sorted_info = sorted([(bp[2] if bp else -999, lname, ext) for (lname,bp,ext,_) in info if bp])
    if not sorted_info: continue
    top_z = sorted_info[-1][0]
    print(f"  {zn}  fpZ[{fp['zmin']}..{fp['zmax']}]:")
    for z, lname, ext in sorted_info:
        marker = ' <-TOP' if z==top_z else ''
        # World top: assume Z_max==29 means no Layer+1 -> ext should be False on top
        # User said EleventhStair Z=29 ext=false - that's a top-of-world rule
        recommend = 'true' if z==top_z and z<29 else ('?' if z!=top_z else 'false')
        flag_warn = ''
        if z==top_z:
            if z>=29 and ext: flag_warn = '  WARN: top-of-world should be ext=false'
            elif z<29 and not ext: flag_warn = '  WARN: top anchor below world top should be ext=true'
        print(f"    Z={z} {lname:35s} ext={ext}{marker}{flag_warn}")

# === Task 3D: cross-elevator connection presence ===
print("\n=== TASK 3D: Cross-elevator handoff connections ===")
elev_lms = {}
for zn,(fp,info) in zone_lm_info.items():
    if 'Elevator' in zn:
        elev_lms[zn] = set(x[0] for x in info if x[0])
print("Elevator landmark sets:")
for zn, lms in elev_lms.items():
    print(f"  {zn}: {sorted(lms)}")

pairs = [('Elevator_E','Elevator_F'),('Elevator_F','Elevator_G'),
         ('Elevator_G','Elevator_C'),('Elevator_C','Elevator_H'),
         ('Elevator_H','Elevator_B'),('Elevator_B','Elevator_D')]
for a,b in pairs:
    aname=f'Sandbox_Small_{a}'; bname=f'Sandbox_Small_{b}'
    al = elev_lms.get(aname,set()); bl = elev_lms.get(bname,set())
    matches = []
    for c in ss_conns:
        o,d = conn_lms(c)
        if (o in al and d in bl) or (o in bl and d in al):
            matches.append((c['Name'], o, d))
    print(f"  {a}<->{b}: {len(matches)} conns; A_lms={sorted(al)} B_lms={sorted(bl)}")
    for nm,o,d in matches:
        print(f"    {nm}: {o} -> {d}")

# === Task 3E: Floor-internal coverage ===
print("\n=== TASK 3E: Floor-internal connection coverage ===")
internal_by_z = defaultdict(int)
inbound_by_z = defaultdict(int)
for c in ss_conns:
    o,d = conn_lms(c)
    oz = lm_z(o); dz = lm_z(d)
    if oz is not None and oz==dz:
        internal_by_z[oz] += 1
    elif oz is not None or dz is not None:
        if oz is not None: inbound_by_z[oz] += 1
        if dz is not None: inbound_by_z[dz] += 1

for fl, z in floor_z.items():
    print(f"  {fl} (Z={z}):  internal={internal_by_z.get(z,0)}  cross-floor touches={inbound_by_z.get(z,0)}")

# Save findings
findings = {
    'out_of_range':[{'zone':o['zone'],'lm':o['lm'],'bp':list(o['bp']),'ext':o['ext'],'fp':o['fp']} for o in out_of_range]
}
with open(os.path.join(ROOT,'_lvfix_findings.json'),'w',encoding='utf-8') as f:
    json.dump(findings,f,indent=2,default=str)
print("\nFindings saved to _lvfix_findings.json")
