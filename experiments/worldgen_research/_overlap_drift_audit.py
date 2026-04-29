"""Compare zone-zone overlaps between '10-chapter working' baseline and
current state. Show:
  - Overlap pairs that EXIST NOW but didn't in baseline (new conflicts)
  - Overlap pairs that EXISTED in baseline but don't anymore (resolved)
  - Overlap pairs in BOTH but the overlap volume changed (worse / better)
  - Zone size deltas
"""
import json
def fp(v, n):
    for p in v or []:
        if isinstance(p, dict) and p.get('Name') == n: return p
    return None
def get(r, k):
    p = fp(r['Value'], k)
    if not p: return None
    v = p.get('Value')
    if isinstance(v, list):
        for it in v:
            if isinstance(it, dict) and it.get('Name')=='RowName':
                return it.get('Value','')
    return v
def get_intvec(prop):
    v = prop.get('Value') if prop else None
    if isinstance(v, list) and v:
        inner = v[0]
        if isinstance(inner, dict) and isinstance(inner.get('Value'), dict):
            d = inner['Value']
            return (d.get('X'),d.get('Y'),d.get('Z'))
    return (None,None,None)
def zoneset(r):
    p = fp(r.get('Value', []), 'ZoneSet')
    return str(p.get('Value','')).split('::')[-1] if p else None
def zstate(r):
    p = fp(r.get('Value', []), 'EnabledState')
    return str(p.get('Value','')).split('::')[-1] if p else None
def axes_overlap(p1, s1, p2, s2):
    ox = min(p1[0]+s1[0]-1, p2[0]+s2[0]-1) - max(p1[0], p2[0]) + 1
    oy = min(p1[1]+s1[1]-1, p2[1]+s2[1]-1) - max(p1[1], p2[1]) + 1
    oz = min(p1[2]+s1[2]-1, p2[2]+s2[2]-1) - max(p1[2], p2[2]) + 1
    return ox, oy, oz

def collect_pinned(d):
    """Return [(name, chap, pos, size)] for pinned Live SS zones (Pos!=000)."""
    out = []
    for r in d['Exports'][0]['Table']['Data']:
        if zoneset(r) != 'SandboxSmall' or zstate(r) == 'Disabled': continue
        pos = get_intvec(fp(r['Value'], 'Position'))
        sz = get_intvec(fp(r['Value'], 'TargetSize'))
        if None in pos or None in sz: continue
        if pos == (0, 0, 0): continue
        chap = get(r, 'Chapter')
        out.append((r['Name'], chap, pos, sz))
    return out

def all_pairs_overlap(zones):
    """Yield (n1, c1, p1, s1, n2, c2, p2, s2, ox, oy, oz, ovol)."""
    pairs = []
    for i in range(len(zones)):
        for j in range(i+1, len(zones)):
            n1, c1, p1, s1 = zones[i]
            n2, c2, p2, s2 = zones[j]
            ox, oy, oz = axes_overlap(p1, s1, p2, s2)
            if ox <= 0 or oy <= 0 or oz <= 0: continue
            ovol = ox*oy*oz
            pairs.append((n1, c1, p1, s1, n2, c2, p2, s2, ox, oy, oz, ovol))
    return pairs

OLD_PATH = 'backups/10-chapter working/DT_Moria_Zones.json'
NEW_PATH = 'DT_Moria_Zones.json'

old = json.load(open(OLD_PATH, encoding='utf-8'))
new = json.load(open(NEW_PATH, encoding='utf-8'))

old_zones = collect_pinned(old)
new_zones = collect_pinned(new)

print(f'Pinned Live SS zones — baseline: {len(old_zones)}  current: {len(new_zones)}')

old_pairs = all_pairs_overlap(old_zones)
new_pairs = all_pairs_overlap(new_zones)

# Index by sorted pair name
def key(p): return tuple(sorted([p[0], p[4]]))
old_by_key = {key(p): p for p in old_pairs}
new_by_key = {key(p): p for p in new_pairs}

added = sorted(set(new_by_key) - set(old_by_key))
removed = sorted(set(old_by_key) - set(new_by_key))
common = sorted(set(old_by_key) & set(new_by_key))

print(f'Total overlap pairs — baseline: {len(old_by_key)}  current: {len(new_by_key)}')
print(f'  NEW pairs (introduced after baseline): {len(added)}')
print(f'  REMOVED pairs (resolved since baseline): {len(removed)}')
print(f'  Common pairs: {len(common)}')

# NEW PAIRS
if added:
    print('\n=== NEW OVERLAP PAIRS (introduced since baseline) ===')
    print('Sorted by overlap volume desc')
    sorted_added = sorted(added, key=lambda k: -new_by_key[k][11])
    for k in sorted_added:
        n1,c1,p1,s1,n2,c2,p2,s2,ox,oy,oz,ovol = new_by_key[k]
        v1=s1[0]*s1[1]*s1[2]; v2=s2[0]*s2[1]*s2[2]
        cv1 = ovol/v1*100 if v1 else 0
        cv2 = ovol/v2*100 if v2 else 0
        same = 'SAME-CHAP' if c1 == c2 else 'CROSS-CHAP'
        c1s = c1.replace('SandboxSmall-chapter-','c-') if c1 else '?'
        c2s = c2.replace('SandboxSmall-chapter-','c-') if c2 else '?'
        print(f'  [{same}] {n1} ({c1s}) vs {n2} ({c2s})')
        print(f'    P1={p1} S1={s1}  P2={p2} S2={s2}')
        print(f'    overlap=({ox},{oy},{oz}) vol={ovol}  cov: {cv1:.0f}% / {cv2:.0f}%')

# CHANGED PAIRS (in both but volume differs)
worsened = []
improved = []
for k in common:
    o = old_by_key[k]; n = new_by_key[k]
    if o[11] != n[11]:
        if n[11] > o[11]: worsened.append((k, o, n))
        else: improved.append((k, o, n))

if worsened:
    print('\n=== EXISTING PAIRS WHERE OVERLAP GREW ===')
    for k, o, n in sorted(worsened, key=lambda x: -(x[2][11] - x[1][11])):
        print(f'  {k[0]} vs {k[1]}: vol {o[11]} -> {n[11]}  (+{n[11]-o[11]})')

if improved:
    print('\n=== EXISTING PAIRS WHERE OVERLAP SHRUNK ===')
    for k, o, n in sorted(improved, key=lambda x: x[2][11] - x[1][11]):
        print(f'  {k[0]} vs {k[1]}: vol {o[11]} -> {n[11]}  ({n[11]-o[11]})')

# REMOVED PAIRS (no longer overlap)
if removed:
    print(f'\n=== RESOLVED OVERLAPS (no longer conflict) — {len(removed)} pairs ===')
    for k in removed[:15]:
        o = old_by_key[k]
        print(f'  {k[0]} vs {k[1]}  (was vol={o[11]})')
    if len(removed) > 15:
        print(f'  ...(+{len(removed)-15} more)')
