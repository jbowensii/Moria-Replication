"""Verification after BP fixes."""
import json, os
ROOT = os.path.dirname(os.path.abspath(__file__))
def load(n):
    with open(os.path.join(ROOT,n),'r',encoding='utf-8') as f: return json.load(f)
def rows(d): return d['Exports'][0]['Table']['Data']
def props(r): return {p.get('Name'):p for p in r.get('Value',[]) if isinstance(p,dict)}
def get_intvec(row,name):
    p=props(row).get(name)
    if not p: return None
    for sp in p.get('Value',[]):
        if isinstance(sp,dict) and sp.get('$type','').endswith('IntVectorPropertyData, UAssetAPI'):
            v=sp.get('Value',{}); return (v.get('X'),v.get('Y'),v.get('Z'))
    return None
def get_array(row,name):
    p=props(row).get(name); return p.get('Value',[]) if p else []
def get_enabled(row):
    p=props(row).get('EnabledState'); return p.get('Value') if p else None
def is_live(row):
    e=get_enabled(row); return e is None or 'Live' in str(e)

zones=load('DT_Moria_Zones.json'); lms=load('DT_Moria_Landmarks.json')
chap=load('DT_Moria_Chapters.json'); conn=load('DT_Moria_LayoutConnections.json')

zr=rows(zones); lr=rows(lms); cr=rows(conn); chr_=rows(chap)
lm_by_name={r['Name']:r for r in lr}
zone_by_name={r['Name']:r for r in zr}
chap_by_name={r['Name']:r for r in chr_}

# 1. Re-audit BPs
def zone_fp(z):
    pos=get_intvec(z,'Position'); sz=get_intvec(z,'TargetSize')
    if not pos or not sz: return None
    px,py,pz=pos; sx,sy,sz_=sz
    return {'xmin':px,'xmax':px+sx-1,'ymin':py,'ymax':py+sy-1,'zmin':pz,'zmax':pz+sz_-1}

def lm_handles(z):
    arr=get_array(z,'LandmarkHandles'); out=[]
    for entry in arr:
        if not isinstance(entry,dict): continue
        lm_ref=None; placement=None
        for sp in entry.get('Value',[]):
            if not isinstance(sp,dict): continue
            nm=sp.get('Name')
            if nm=='Landmark':
                for q in sp.get('Value',[]):
                    if isinstance(q,dict) and q.get('Name')=='RowName':
                        lm_ref=q.get('Value')
            elif nm=='Placement': placement=sp.get('Value')
        out.append({'lm':lm_ref,'placement':placement})
    return out

bad=0
for z in zr:
    if not z['Name'].startswith('Sandbox_Small_'): continue
    if not is_live(z): continue
    fp=zone_fp(z)
    if not fp: continue
    for h in lm_handles(z):
        if not h['placement'] or 'Fixed' not in str(h['placement']): continue
        if not h['lm'] or h['lm']=='None': continue
        lr_=lm_by_name.get(h['lm'])
        if not lr_: continue
        bp=get_intvec(lr_,'BasePosition')
        if not bp: continue
        bx,by,bz=bp
        if not(fp['xmin']<=bx<=fp['xmax'] and fp['ymin']<=by<=fp['ymax'] and fp['zmin']<=bz<=fp['zmax']):
            print(f"  STILL BAD: {h['lm']} BP={bp} in {z['Name']}")
            bad+=1
print(f"VERIFY 1: out-of-range Fixed BPs = {bad}")

# 2. 14 level rows in Chapters
expected_levels=['Lv-1','Lv-2','Lv-3','Lv-4','Lv-5','Lv-6','Lv-7','D-1','D-2','D-3','D-4','D-5','D-6','D-7']
chap_names=set(chap_by_name.keys())
missing=[]
for lvl in expected_levels:
    found=any(lvl in n for n in chap_names)
    if not found: missing.append(lvl)
print(f"VERIFY 2: chapter level rows missing: {missing}")
matching = [n for n in chap_names if any(l in n for l in expected_levels)]
print(f"   level-related chapter rows: {len(matching)}")

# 3. NameMap consistency: NamesReferencedFromExportDataCount vs NameMap length
files = ['DT_Moria_Zones.json','DT_Moria_Chapters.json','DT_Moria_Landmarks.json','DT_Moria_LayoutConnections.json','World.json']
for fn in files:
    try:
        d = load(fn)
        nm = d.get('NameMap', [])
        nrc = d.get('NamesReferencedFromExportDataCount')
        print(f"VERIFY 3 {fn}: NameMap={len(nm)} NamesReferencedFromExportDataCount={nrc}")
    except Exception as e:
        print(f"  ERR {fn}: {e}")

# 4. Zone -> chapter row exists
def get_rowname(row,name):
    p=props(row).get(name)
    if not p: return None
    for sp in p.get('Value',[]):
        if isinstance(sp,dict) and sp.get('Name')=='RowName':
            return sp.get('Value')
    return None
miss_chap=[]
for z in zr:
    if not is_live(z): continue
    cn = get_rowname(z,'Chapter')
    if cn and cn != 'None' and cn not in chap_by_name:
        miss_chap.append((z['Name'],cn))
print(f"VERIFY 4: zones with missing chapter ref: {len(miss_chap)}")
for zn,cn in miss_chap[:10]:
    print(f"  {zn} -> {cn}")

# 5. LayoutConnection -> landmark exists
miss_lm=[]
for c in cr:
    if not is_live(c): continue
    for k in ('OriginLandmark','DestinationLandmark'):
        ln = get_rowname(c,k)
        if ln and ln != 'None' and ln not in lm_by_name:
            miss_lm.append((c['Name'],k,ln))
print(f"VERIFY 5: connections with missing landmark ref: {len(miss_lm)}")
for c,k,ln in miss_lm[:10]:
    print(f"  {c}.{k} -> {ln}")
