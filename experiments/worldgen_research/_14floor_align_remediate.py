"""Second pass: collapse drift values to NEW PrimeZ of their owning chapter.

After _14floor_align_apply.py we have 4 prefZ + 1 subcell + 11 landmark BP errors —
all values that were inside an OLD chapter band but != old PrimeZ. To make the
build valid, collapse each to the NEW PrimeZ of the chapter whose old band
contained the value.

Special handling:
- DurinsTower BP.Z=23 (not in any active chapter old band actually — wait 23 IS
  in chapter-3 old band 21..24). Apply chapter-3 new PrimeZ = 21. (User can
  reposition later.)
- Values in chapter-1 old band (18..19) with Δ=0 but band narrowed (drops 19):
  collapse 19 -> 18.
- A value in old chapter-7 band lying at new chapter-8 cell (Z=8) is fine for
  validator, but to keep things in the right semantic chapter we collapse to
  chapter-7 new PrimeZ = 9.
"""
import json, sys, io
from collections import defaultdict
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

# Same TARGETS as apply
TARGETS = {
    'SandboxSmall-chapter-1': {'min':18,'max':18,'pz':18},
    'SandboxSmall-chapter-2': {'min':20,'max':20,'pz':20},
    'SandboxSmall-chapter-3': {'min':21,'max':21,'pz':21},
    'SandboxSmall-chapter-4': {'min':22,'max':22,'pz':22},
    'SandboxSmall-chapter-5': {'min':17,'max':17,'pz':17},
    'SandboxSmall-chapter-6': {'min':13,'max':13,'pz':13},
    'SandboxSmall-chapter-7': {'min':9, 'max':9, 'pz':9},
    'SandboxSmall-chapter-8': {'min':8, 'max':8, 'pz':8},
}
# OLD bands (from current state before migration)
OLD_BANDS = {
    'SandboxSmall-chapter-1': (18,19,18),
    'SandboxSmall-chapter-2': (20,20,20),
    'SandboxSmall-chapter-3': (21,24,22),
    'SandboxSmall-chapter-4': (22,22,22),
    'SandboxSmall-chapter-5': (16,17,16),
    'SandboxSmall-chapter-6': (14,15,15),
    'SandboxSmall-chapter-7': (11,13,12),
    'SandboxSmall-chapter-8': (8,8,8),
}

ZF='DT_Moria_Zones.json'; CF='DT_Moria_Chapters.json'
LF='DT_Moria_Landmarks.json'; KF='DT_Moria_LayoutConnections.json'
z = json.load(open(ZF,encoding='utf-8'))
ch = json.load(open(CF,encoding='utf-8'))
lm = json.load(open(LF,encoding='utf-8'))
lc = json.load(open(KF,encoding='utf-8'))

def fp(v,n):
    for p in v or []:
        if isinstance(p,dict) and p.get('Name')==n: return p
def gv_xyz(p):
    v=p.get('Value') if p else None
    if isinstance(v,list) and v:
        d=v[0].get('Value') if isinstance(v[0],dict) else None
        if isinstance(d,dict): return d
def gf(r,k):
    p=fp(r['Value'],k); v=p.get('Value') if p else None
    if isinstance(v,list):
        for it in v:
            if isinstance(it,dict) and it.get('Name')=='RowName': return it.get('Value','')
    return v
def st(r):
    p=fp(r.get('Value',[]),'EnabledState')
    return str(p.get('Value','')).split('::')[-1] if p else None
def zoneset(r):
    p=fp(r.get('Value',[]),'ZoneSet')
    return str(p.get('Value','')).split('::')[-1] if p else None

# Live SS cells (after migration)
ss_cells = set()
for n,t in TARGETS.items():
    for cz in range(t['min'], t['max']+1):
        ss_cells.add(cz)

# Map old Z -> chapter (any chapter whose old band contains z; pick by precedence)
def chapter_for_z(zv):
    # prefer one whose old band contains zv (could be multiple; pick deterministic)
    matches = [n for n,(omn,omx,opz) in OLD_BANDS.items() if omn<=zv<=omx]
    if not matches: return None
    # If one is exactly the OLD PrimeZ -> prefer that (semantic floor)
    pz_match = [n for n in matches if OLD_BANDS[n][2]==zv]
    if pz_match: return pz_match[0]
    # else prefer the chapter whose old MinZ == zv (semantic floor)
    mn_match = [n for n in matches if OLD_BANDS[n][0]==zv]
    if mn_match: return mn_match[0]
    return matches[0]

def remediate(zv):
    """Return new Z (collapsed to chapter's new PrimeZ) or None if uncovered."""
    if zv in ss_cells: return zv  # already valid
    chap = chapter_for_z(zv)
    if not chap: return None
    return TARGETS[chap]['pz']

remed = defaultdict(int)
log = []

# Zone PreferredZOverride
for r in z['Exports'][0]['Table']['Data']:
    if zoneset(r) != 'SandboxSmall' or st(r)=='Disabled': continue
    pp = fp(r['Value'],'PreferredZOverride')
    if pp is None: continue
    v = pp.get('Value')
    if not isinstance(v,int) or v < 0: continue
    if v in ss_cells: continue
    new_v = remediate(v)
    if new_v is None or new_v == v: continue
    pp['Value'] = new_v
    remed['zone_prefz']+=1
    log.append(('zone_prefz', r['Name'], v, new_v))

# Zone Position.Z (handles the Z=19 chapter-1 narrowing case)
for r in z['Exports'][0]['Table']['Data']:
    if zoneset(r) != 'SandboxSmall' or st(r)=='Disabled': continue
    pos_p = fp(r['Value'],'Position')
    pos_d = gv_xyz(pos_p)
    if pos_d is None: continue
    if pos_d.get('X')==0 and pos_d.get('Y')==0: continue
    zv = pos_d.get('Z')
    if not isinstance(zv,int): continue
    if zv in ss_cells: continue
    new_zv = remediate(zv)
    if new_zv is None or new_zv == zv: continue
    pos_d['Z'] = new_zv
    remed['zone_pos']+=1
    log.append(('zone_pos', r['Name'], zv, new_zv))

# Landmarks (all SS-namespaced + bridge names)
ss_namespaces=('Sandbox.',)
ss_bridge_names={'TradingPost','DurinsTower','DimrillDale','Sandbox_DurinsTower','Sandbox_TradingPost','Sandbox_DimrillDale'}
for r in lm['Exports'][0]['Table']['Data']:
    n=r['Name']
    if not (n.startswith(ss_namespaces) or n in ss_bridge_names): continue
    if st(r)=='Disabled': continue
    bp_p=fp(r['Value'],'BasePosition')
    bp_d=gv_xyz(bp_p)
    if bp_d is None: continue
    if bp_d.get('X')==0 and bp_d.get('Y')==0: continue
    zv=bp_d.get('Z')
    if not isinstance(zv,int): continue
    if zv in ss_cells: continue
    new_zv=remediate(zv)
    if new_zv is None or new_zv == zv: continue
    bp_d['Z']=new_zv
    remed['lm_bp']+=1
    log.append(('lm_bp', n, zv, new_zv))

# Subcell.Z in connections
for r in lc['Exports'][0]['Table']['Data']:
    if zoneset(r) != 'SandboxSmall' or st(r)=='Disabled': continue
    for fld in ('OriginInterface','DestinationInterface'):
        prop=fp(r['Value'], fld)
        if not prop: continue
        for inner in (prop.get('Value') or []):
            if isinstance(inner,dict) and inner.get('Name')=='Subcell':
                sc_v=inner.get('Value')
                if isinstance(sc_v,list) and sc_v:
                    d=sc_v[0].get('Value')
                    if not isinstance(d,dict): continue
                    zv=d.get('Z')
                    if not isinstance(zv,int) or zv==0: continue
                    if zv in ss_cells: continue
                    new_zv=remediate(zv)
                    if new_zv is None or new_zv == zv: continue
                    d['Z']=new_zv
                    remed['subcell']+=1
                    log.append(('subcell', r['Name']+'.'+fld, zv, new_zv))

print('=== Remediation counts ===')
for k,v in remed.items():
    print(f'  {k}: {v}')
print('\n=== Log ===')
for kind, ref, old, new in log:
    print(f'  [{kind}] {ref}: {old} -> {new}')

def save(path,obj):
    with open(path,'w',encoding='utf-8') as f:
        json.dump(obj, f, indent=2)
save(ZF,z); save(CF,ch); save(LF,lm); save(KF,lc)
print('\nFiles saved.')
