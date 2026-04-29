"""Migrate 8 active SS chapters to 14-floor target Z layout.

Strategy (safe rule):
- Shift a reference value by Δ ONLY if value == OLD PrimeZ of its affected chapter.
- Values in OLD band but != OLD PrimeZ are flagged as needing user review (drift).
- Values outside any old band are untouched.

Targets (per spec):
  chapter-1  Lv-1  18..19/18 -> 18..18/18  Δ=0
  chapter-2  Lv-2  20..20/20 -> 20..20/20  Δ=0
  chapter-3  Lv-3  21..24/22 -> 21..21/21  Δ=-1
  chapter-4  Lv-4  22..22/22 -> 22..22/22  Δ=0
  chapter-5  D-1   16..17/16 -> 17..17/17  Δ=+1
  chapter-6  D-2   14..15/15 -> 13..13/13  Δ=-2
  chapter-7  D-3   11..13/12 -> 9..9/9     Δ=-3
  chapter-8  D-4   8..8/8    -> 8..8/8     Δ=0
"""
import json, sys, io
from collections import defaultdict, Counter
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

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

# ---- Load ----
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
        if isinstance(d,dict): return d  # mutable
    return None
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

# ---- Step 1: Build chapter delta map from CURRENT data ----
chap_old = {}  # name -> (mn, mx, pz)
for r in ch['Exports'][0]['Table']['Data']:
    n=r['Name']
    if n not in TARGETS: continue
    if st(r)=='Disabled': continue
    chap_old[n]=(gf(r,'MinZ'), gf(r,'MaxZ'), gf(r,'PrimeZ'))

deltas = {}  # name -> dict(old_pz, new_pz, delta, old_min, old_max)
for n, tgt in TARGETS.items():
    if n not in chap_old:
        print(f'  SKIP (chapter not present/disabled): {n}')
        continue
    omn, omx, opz = chap_old[n]
    deltas[n] = {
        'old_min':omn,'old_max':omx,'old_pz':opz,
        'new_min':tgt['min'],'new_max':tgt['max'],'new_pz':tgt['pz'],
        'delta': tgt['pz'] - opz,
    }

print('=== Delta map ===')
for n in sorted(deltas):
    d=deltas[n]
    print(f'  {n}: {d["old_min"]}..{d["old_max"]}/{d["old_pz"]} -> {d["new_min"]}..{d["new_max"]}/{d["new_pz"]}  Δ={d["delta"]:+d}')

# Map old PrimeZ -> chapter (for chapters with delta != 0 OR band narrowing)
# We need this for orphan landmarks and Subcell.Z that don't carry chapter affiliation.
old_pz_to_chap = {}
for n,d in deltas.items():
    old_pz_to_chap[d['old_pz']] = n  # may collide if two chapters had same PrimeZ — none currently

# Also map: which chapters have Δ != 0
delta_chaps = {n:d for n,d in deltas.items() if d['delta'] != 0}
# Chapters where band changes shape but Δ==0 (band narrows, e.g., chapter-1 Lv-1)
narrow_chaps = {}
for n,d in deltas.items():
    old_set=set(range(d['old_min'], d['old_max']+1))
    new_set=set(range(d['new_min'], d['new_max']+1))
    if d['delta']==0 and old_set != new_set:
        narrow_chaps[n] = (old_set - new_set)  # cells dropped

print(f'\nChapters with Δ!=0: {list(delta_chaps)}')
print(f'Chapters narrowing (Δ=0): {[(k, sorted(v)) for k,v in narrow_chaps.items()]}')

# ---- Step 2: Update chapter MinZ/MaxZ/PrimeZ ----
chap_changes = 0
for r in ch['Exports'][0]['Table']['Data']:
    n=r['Name']
    if n not in deltas: continue
    if st(r)=='Disabled': continue
    tgt = TARGETS[n]
    for fld, val in (('MinZ',tgt['min']),('MaxZ',tgt['max']),('PrimeZ',tgt['pz'])):
        p=fp(r['Value'],fld)
        if p is not None and p.get('Value') != val:
            p['Value'] = val
            chap_changes += 1
print(f'\n=== Chapter rows updated: {chap_changes} field writes ===')

# ---- Step 3: Cascade shifts ----
counts = defaultdict(lambda: defaultdict(int))  # chap -> kind -> count
drift = []  # (kind, ref_name, chap, value, would_shift_to)

def maybe_shift(value, chap_name, kind, ref_name, allow_band_match=False):
    """Return (new_value, action) where action in {'shift','drift','skip'}.
    Default rule: shift only if value == old PrimeZ of chap_name.
    If allow_band_match=True (used for orphan landmarks/subcells when locating chap by band),
    value already determined to be in band; we still only shift if == old PrimeZ.
    """
    d=deltas.get(chap_name)
    if not d: return value, 'skip'
    omn,omx,opz=d['old_min'],d['old_max'],d['old_pz']
    if value == opz:
        new_val = value + d['delta']
        return new_val, 'shift'
    if omn <= value <= omx:
        # In old band but not at old PrimeZ -- drift
        return value, 'drift'
    return value, 'skip'

# 3a. Zones: Position.Z and PreferredZOverride
for r in z['Exports'][0]['Table']['Data']:
    if zoneset(r) != 'SandboxSmall' or st(r)=='Disabled': continue
    chap = gf(r,'Chapter')
    if chap not in deltas: continue
    # Position.Z
    pos_p = fp(r['Value'],'Position')
    pos_d = gv_xyz(pos_p)
    if pos_d is not None:
        zv = pos_d.get('Z')
        if isinstance(zv,int) and not (pos_d.get('X')==0 and pos_d.get('Y')==0 and zv==0):
            new_zv, action = maybe_shift(zv, chap, 'zone_pos', r['Name'])
            if action=='shift':
                pos_d['Z']=new_zv; counts[chap]['zone_pos_shift']+=1
            elif action=='drift':
                drift.append(('zone_pos', r['Name'], chap, zv, None))
                counts[chap]['zone_pos_drift']+=1
    # PreferredZOverride
    pp = fp(r['Value'],'PreferredZOverride')
    if pp is not None:
        v = pp.get('Value')
        if isinstance(v,int) and v >= 0:
            new_v, action = maybe_shift(v, chap, 'zone_prefz', r['Name'])
            if action=='shift':
                pp['Value']=new_v; counts[chap]['zone_prefz_shift']+=1
            elif action=='drift':
                drift.append(('zone_prefz', r['Name'], chap, v, None))
                counts[chap]['zone_prefz_drift']+=1
    # Also flag if Pos.Z is in narrow_chaps dropped cells (Δ=0 narrowing)
    if chap in narrow_chaps and pos_d is not None:
        zv = pos_d.get('Z')
        if isinstance(zv,int) and zv in narrow_chaps[chap]:
            drift.append(('zone_pos_narrow', r['Name'], chap, zv, None))
            counts[chap]['zone_pos_narrow_drift']+=1

# 3b. Landmark BP.Z for landmarks hosted via LH on Live SS zones whose chapter has Δ != 0
# Build zone -> [landmark names] from LandmarkHandles, and zone -> chapter
zone_chap = {}
zone_lh_map = defaultdict(list)
for r in z['Exports'][0]['Table']['Data']:
    if zoneset(r) != 'SandboxSmall' or st(r)=='Disabled': continue
    zone_chap[r['Name']] = gf(r,'Chapter')
    p=fp(r['Value'],'LandmarkHandles')
    if not p: continue
    for entry in (p.get('Value') or []):
        sub=entry.get('Value') if isinstance(entry,dict) else None
        if not isinstance(sub,list): continue
        lm_struct = fp(sub,'Landmark')
        if not lm_struct: continue
        for inner in (lm_struct.get('Value') or []):
            if isinstance(inner,dict) and inner.get('Name')=='RowName':
                ln=inner.get('Value','')
                if ln and ln!='None': zone_lh_map[r['Name']].append(ln)

# landmark name -> primary chapter (from first hosting zone) for shift purposes
lm_primary_chap = {}
for zn, lns in zone_lh_map.items():
    chap = zone_chap.get(zn)
    for ln in lns:
        # If multiple zones host same landmark, prefer one whose chapter is in deltas
        cur = lm_primary_chap.get(ln)
        if chap in deltas and (cur is None or cur not in deltas):
            lm_primary_chap[ln] = chap
        elif cur is None:
            lm_primary_chap[ln] = chap

# Now iterate landmarks and shift BP.Z based on hosting chapter
for r in lm['Exports'][0]['Table']['Data']:
    n = r['Name']
    chap = lm_primary_chap.get(n)
    if not chap or chap not in deltas: continue
    bp_p = fp(r['Value'],'BasePosition')
    bp_d = gv_xyz(bp_p)
    if bp_d is None: continue
    if bp_d.get('X')==0 and bp_d.get('Y')==0: continue
    zv = bp_d.get('Z')
    if not isinstance(zv,int): continue
    new_zv, action = maybe_shift(zv, chap, 'lm_bp', n)
    if action=='shift':
        bp_d['Z']=new_zv; counts[chap]['lm_bp_shift']+=1
    elif action=='drift':
        drift.append(('lm_bp', n, chap, zv, None))
        counts[chap]['lm_bp_drift']+=1

# 3c. Orphan SS-namespaced landmarks
ss_namespaces=('Sandbox.',)
ss_bridge_names={'TradingPost','DurinsTower','DimrillDale','Sandbox_DurinsTower','Sandbox_TradingPost','Sandbox_DimrillDale'}
hosted = set(lm_primary_chap.keys())
# Build value -> chapter from old bands — for orphan, find which chapter's old band the BP.Z falls in
def chapter_for_z(zv):
    # find chapter whose old band contains zv AND has Δ != 0
    matches = [n for n,d in deltas.items() if d['old_min']<=zv<=d['old_max'] and d['delta']!=0]
    if len(matches)==1: return matches[0]
    return None

for r in lm['Exports'][0]['Table']['Data']:
    n=r['Name']
    if not (n.startswith(ss_namespaces) or n in ss_bridge_names): continue
    if st(r)=='Disabled': continue
    if n in hosted: continue
    bp_p=fp(r['Value'],'BasePosition')
    bp_d=gv_xyz(bp_p)
    if bp_d is None: continue
    if bp_d.get('X')==0 and bp_d.get('Y')==0: continue
    zv=bp_d.get('Z')
    if not isinstance(zv,int): continue
    chap = chapter_for_z(zv)
    if not chap: continue  # not in any delta-chapter old band
    new_zv, action = maybe_shift(zv, chap, 'orphan_lm_bp', n)
    if action=='shift':
        bp_d['Z']=new_zv; counts[chap]['orphan_lm_bp_shift']+=1
    elif action=='drift':
        drift.append(('orphan_lm_bp', n, chap, zv, None))
        counts[chap]['orphan_lm_bp_drift']+=1

# 3d. Connection nested Subcell.Z
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
                    chap = chapter_for_z(zv)
                    if not chap: continue
                    new_zv, action = maybe_shift(zv, chap, 'subcell', r['Name']+'.'+fld)
                    if action=='shift':
                        d['Z']=new_zv; counts[chap]['subcell_shift']+=1
                    elif action=='drift':
                        drift.append(('subcell', r['Name']+'.'+fld, chap, zv, None))
                        counts[chap]['subcell_drift']+=1

# ---- Step 4: Save ----
def save(path, obj):
    with open(path,'w',encoding='utf-8') as f:
        json.dump(obj, f, indent=2)

save(ZF, z)
save(CF, ch)
save(LF, lm)
save(KF, lc)

print('\n=== Cascade counts per chapter ===')
for chap in sorted(counts):
    print(f'  {chap}: {dict(counts[chap])}')

print('\n=== Drift / review items ===')
for item in drift:
    kind, ref, chap, val, _ = item
    print(f'  [{kind}] {ref}  chap={chap}  value={val} (in old band, not at old PrimeZ — UNCHANGED)')

print('\nFiles written:', ZF, CF, LF, KF)
