"""Verify: each elevator zone's bubble Z range fits within its primary chapter's [MinZ..MaxZ]
and within global SS world Z range. Print final table."""
import json, os

ROOT = os.path.dirname(os.path.abspath(__file__))

def find_rows(u):
    for e in u.get('Exports', []):
        t = e.get('Table')
        if t and 'Data' in t: return t['Data']
    return []

def rp(r): return r.get('Value',[]) or []

def pg(rd,n):
    for p in rd:
        if p.get('Name')==n: return p
    return None

def pi(rd,n,d=None):
    p = pg(rd,n); return p.get('Value',d) if p else d

def iv(rd,n):
    p = pg(rd,n)
    if not p: return None
    inner = p.get('Value')
    if isinstance(inner,list) and inner:
        v = inner[0].get('Value')
        if isinstance(v,dict): return (v.get('X'),v.get('Y'),v.get('Z'))
    return None

def lhs(rd):
    out=[]; p = pg(rd,'LandmarkHandles')
    if not p: return out
    for e in p.get('Value',[]) or []:
        ep = e.get('Value',[]) or []
        lh = pg(ep,'Landmark')
        if lh:
            rn = pg(lh.get('Value',[]) or [], 'RowName')
            if rn: out.append(rn.get('Value'))
    return out

def chapter_of(rd):
    ch = pg(rd,'Chapter')
    if not ch: return None
    rn = pg(ch.get('Value',[]) or [], 'RowName')
    return rn.get('Value') if rn else None

def load(p):
    with open(p,'r',encoding='utf-8') as f: return json.load(f)

zd = load(os.path.join(ROOT,'DT_Moria_Zones.json'))
ld = load(os.path.join(ROOT,'DT_Moria_Landmarks.json'))
cd = load(os.path.join(ROOT,'DT_Moria_Chapters.json'))

# Build chapter map
chapters = {}
ss_minz = []; ss_maxz = []
for r in find_rows(cd):
    nm = r.get('Name',''); rd = rp(r)
    zs = pg(rd,'ZoneSet'); zsv = zs.get('Value') if zs else None
    if zsv == 'EZoneSet::SandboxSmall':
        chapters[nm] = (pi(rd,'MinZ'), pi(rd,'MaxZ'), pi(rd,'PrimeZ'))
        ss_minz.append(pi(rd,'MinZ')); ss_maxz.append(pi(rd,'MaxZ'))
WORLD_MIN, WORLD_MAX = min(ss_minz), max(ss_maxz)

# Build landmark BP map
lm_bp = {}
for r in find_rows(ld):
    nm = r.get('Name','')
    bp = iv(rp(r),'BasePosition')
    lm_bp[nm] = bp

# Walk elevator zones
print(f"World SS Z bounds: [{WORLD_MIN}..{WORLD_MAX}]")
print()
header = f"{'Zone':38s} {'LM':24s} {'BP.Z':>4s} {'TS.Z':>4s} {'Bubble Z':>10s} {'Chap':28s} {'ChapZ':>8s} {'Status':10s}"
print(header)
print('-'*len(header))

errors = 0
for r in find_rows(zd):
    nm = r.get('Name',''); rd = rp(r)
    pos = iv(rd,'Position'); ts = iv(rd,'TargetSize')
    if not (ts and ts[0]==6 and ts[1]==6): continue
    L = lhs(rd)
    if not any('Stair' in x or 'Descent' in x for x in L): continue
    lm = L[0]
    # find BP — try variants
    bp = lm_bp.get(lm) or lm_bp.get('Sandbox.'+lm.split('.')[-1]) or None
    if bp is None:
        # try suffix match
        for k,v in lm_bp.items():
            if k.endswith('.'+lm.split('.')[-1]) or k==lm:
                bp = v; break
    bz = bp[2] if bp else None
    tz = ts[2]
    bubble = (bz, bz+tz-1) if bz is not None else None
    ch = chapter_of(rd)
    cmm = chapters.get(ch)
    status = 'OK'
    if bubble:
        if bubble[0] < WORLD_MIN or bubble[1] > WORLD_MAX:
            status = 'OOB-WORLD'; errors += 1
        elif cmm and (bubble[0] < cmm[0] or bubble[1] > cmm[1]):
            status = 'OOB-CHAP'  # warning only
    czstr = f"{cmm[0]}..{cmm[1]}" if cmm else '?'
    print(f"{nm:38s} {lm:24s} {bz!s:>4s} {tz:>4d} {str(bubble):>10s} {ch or '?':28s} {czstr:>8s} {status:10s}")

print()
print(f"World OOB errors: {errors}")
