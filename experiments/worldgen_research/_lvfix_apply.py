"""Apply BP fixes for Fixed-placement landmarks whose BasePosition is outside their host zone."""
import json, os
from collections import defaultdict
ROOT = os.path.dirname(os.path.abspath(__file__))

def load(n):
    with open(os.path.join(ROOT,n),'r',encoding='utf-8') as f: return json.load(f)
def save(n, d):
    with open(os.path.join(ROOT,n),'w',encoding='utf-8') as f: json.dump(d,f,indent=2)

zones = load('DT_Moria_Zones.json')
lms = load('DT_Moria_Landmarks.json')

def rows(dt): return dt['Exports'][0]['Table']['Data']
def props(r): return {p.get('Name'):p for p in r.get('Value',[]) if isinstance(p,dict)}
def get_intvec(row, name):
    p = props(row).get(name)
    if not p: return None
    for sp in p.get('Value', []):
        if isinstance(sp,dict) and sp.get('$type','').endswith('IntVectorPropertyData, UAssetAPI'):
            v = sp.get('Value',{})
            return (v.get('X'), v.get('Y'), v.get('Z'))
    return None
def set_intvec(row, name, x, y, z):
    p = props(row).get(name)
    if not p: return False
    for sp in p.get('Value', []):
        if isinstance(sp,dict) and sp.get('$type','').endswith('IntVectorPropertyData, UAssetAPI'):
            sp['Value']['X'] = int(x)
            sp['Value']['Y'] = int(y)
            sp['Value']['Z'] = int(z)
            return True
    return False
def get_array(row, name):
    p = props(row).get(name)
    return p.get('Value',[]) if p else []
def get_enabled(row):
    p = props(row).get('EnabledState'); return p.get('Value') if p else None
def is_live(row):
    e = get_enabled(row); return e is None or 'Live' in str(e)

zone_rows = rows(zones); lm_rows = rows(lms)
lm_by_name = {r['Name']:r for r in lm_rows}
zone_by_name = {r['Name']:r for r in zone_rows}

def zone_footprint(z):
    pos = get_intvec(z,'Position'); sz = get_intvec(z,'TargetSize')
    if not pos or not sz or None in pos or None in sz: return None
    px,py,pz=pos; sx,sy,sz_=sz
    return {'pos':pos,'size':sz,'xmin':px,'xmax':px+sx-1,'ymin':py,'ymax':py+sy-1,'zmin':pz,'zmax':pz+sz_-1}

def lm_handles(z):
    arr = get_array(z, 'LandmarkHandles'); out = []
    for entry in arr:
        if not isinstance(entry, dict): continue
        lm_ref=None; ext=None; placement=None
        for sp in entry.get('Value', []):
            if not isinstance(sp,dict): continue
            nm = sp.get('Name')
            if nm == 'Landmark':
                for q in sp.get('Value',[]):
                    if isinstance(q,dict) and q.get('Name')=='RowName':
                        lm_ref = q.get('Value')
            elif nm == 'bExtendedConnectivityLandmark': ext = sp.get('Value')
            elif nm == 'Placement': placement = sp.get('Value')
        out.append({'lm':lm_ref,'ext':ext,'placement':placement})
    return out

# Find all violations (Fixed placement, BP outside zone)
violations = []  # list of dicts
zone_lm_handles_cache = {}
for z in zone_rows:
    if not z['Name'].startswith('Sandbox_Small_'): continue
    if not is_live(z): continue
    fp = zone_footprint(z)
    if not fp: continue
    handles = lm_handles(z)
    zone_lm_handles_cache[z['Name']] = (fp, handles)
    for h in handles:
        if not h['placement'] or 'Fixed' not in str(h['placement']): continue
        lname = h['lm']
        if not lname or lname == 'None': continue
        lr = lm_by_name.get(lname)
        if not lr: continue
        bp = get_intvec(lr, 'BasePosition')
        if not bp or None in bp: continue
        bx,by,bz=bp
        if not (fp['xmin']<=bx<=fp['xmax'] and fp['ymin']<=by<=fp['ymax'] and fp['zmin']<=bz<=fp['zmax']):
            violations.append({'zone':z['Name'],'fp':fp,'lm':lname,'bp':bp,'ext':h['ext']})

print(f"Violations to fix: {len(violations)}")

# Compute new BPs
def clamp(v, lo, hi): return max(lo, min(hi, v))
def center_xy(fp):
    cx = fp['xmin'] + (fp['xmax']-fp['xmin'])//2
    cy = fp['ymin'] + (fp['ymax']-fp['ymin'])//2
    return cx, cy

# Group by zone for multi-LM spreading
by_zone = defaultdict(list)
for v in violations:
    by_zone[v['zone']].append(v)

fixes = []  # (lm, old_bp, new_bp, zone)

# User-specified exact fixes (override defaults)
explicit = {
    'Sandbox.FirstStair': (12,21,18),
    'Sandbox.FourthStair': (12,21,22),
    'Sandbox.ThirdStair': (12,8,23),
}

for zname, vlist in by_zone.items():
    fp = zone_lm_handles_cache[zname][0]
    cx, cy = center_xy(fp)
    # Group by Z (use clamped Z first)
    by_clamped_z = defaultdict(list)
    for v in vlist:
        bx,by,bz = v['bp']
        new_z = clamp(bz, fp['zmin'], fp['zmax'])
        # If original BP looks placeholder (0,0,Z), set Z to zmin (typical floor for fixed lm)
        if bx == 0 and by == 0:
            new_z = fp['zmin']
        by_clamped_z[new_z].append(v)
    for z, group in by_clamped_z.items():
        # If multiple LMs land on same Z, spread X (and Y) inside zone
        n = len(group)
        for i, v in enumerate(group):
            if v['lm'] in explicit:
                nx, ny, nz = explicit[v['lm']]
            else:
                if n == 1:
                    nx, ny, nz = cx, cy, z
                else:
                    # spread X across zone interior
                    span_x = fp['xmax']-fp['xmin']
                    if span_x >= n-1:
                        nx = fp['xmin'] + 1 + (i*(span_x-1))//max(1,n-1) if span_x>=2 else fp['xmin']+i
                        nx = clamp(nx, fp['xmin'], fp['xmax'])
                    else:
                        nx = cx
                    ny, nz = cy, z
            fixes.append({'lm':v['lm'],'old':v['bp'],'new':(nx,ny,nz),'zone':zname})

# Write the fixes
for fx in fixes:
    lr = lm_by_name[fx['lm']]
    ok = set_intvec(lr, 'BasePosition', *fx['new'])
    print(f"  {fx['lm']:35s} {fx['old']} -> {fx['new']}  in {fx['zone']}  ok={ok}")

# Save
save('DT_Moria_Landmarks.json', lms)
print(f"\nWrote {len(fixes)} BP fixes to DT_Moria_Landmarks.json")

# Save fix log
with open(os.path.join(ROOT,'_lvfix_applied.json'),'w',encoding='utf-8') as f:
    json.dump([{'lm':fx['lm'],'old':list(fx['old']),'new':list(fx['new']),'zone':fx['zone']} for fx in fixes], f, indent=2)
