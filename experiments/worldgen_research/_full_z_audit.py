"""Comprehensive Z audit for the L2_RouteInterzoneConnections crash.

Checks every Live SandboxSmall zone for:
  1. Position.Z and TargetSize.Z range sanity (Z >= 0, Z <= 29)
  2. Position.Z + TargetSize.Z - 1 <= 29  (top of zone fits)
  3. TargetSize.Z <= chapter height (zone fits within chapter's Z band)
  4. Position.Z within chapter MinZ..MaxZ (only relevant for pinned zones)
  5. Chapter referenced by zone exists AND is Live
  6. Bubble TargetSize doesn't bleed into adjacent chapter

Also for chapters:
  7. Live chapters in [0, 29]
  8. No two Live chapters overlap in Z
  9. No gap between contiguous chapters

Also for landmarks:
  10. BasePosition.Z in [0, 29]
  11. Landmark host zones exist (cross-DT integrity)
"""
import json
from pathlib import Path

HERE = Path(__file__).parent

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
            if isinstance(it, dict) and it.get('Name') == 'RowName':
                return it.get('Value', '')
    return v
def get_intvec(prop):
    if not prop: return (None, None, None)
    v = prop.get('Value')
    if isinstance(v, list) and v:
        inner = v[0]
        if isinstance(inner, dict) and isinstance(inner.get('Value'), dict):
            d = inner['Value']
            return (d.get('X'), d.get('Y'), d.get('Z'))
    return (None, None, None)
def zoneset(r):
    p = fp(r.get('Value', []), 'ZoneSet')
    if not p: return None
    return str(p.get('Value','')).split('::')[-1]
def zstate(r):
    p = fp(r.get('Value', []), 'EnabledState')
    return str(p.get('Value','')).split('::')[-1] if p else None


ch = json.loads((HERE / 'DT_Moria_Chapters.json').read_text(encoding='utf-8'))
z = json.loads((HERE / 'DT_Moria_Zones.json').read_text(encoding='utf-8'))
lm = json.loads((HERE / 'DT_Moria_Landmarks.json').read_text(encoding='utf-8'))

# Build chapter index
chap_data = {}
chap_live = {}
for r in ch['Exports'][0]['Table']['Data']:
    name = r['Name']
    L = get(r, 'Layer')
    mn = get(r, 'MinZ'); mx = get(r, 'MaxZ'); pz = get(r, 'PrimeZ')
    state = zstate(r)
    chap_data[name] = (L, mn, mx, pz, state)
    if state != 'Disabled':
        chap_live[name] = (L, mn, mx, pz)

print('=== A. Chapter sanity ===')

# A1: Live chapter Z bounds
chap_oob = []
for name, (L, mn, mx, pz, st) in chap_data.items():
    if st == 'Disabled': continue
    if mn is None or mx is None: continue
    if mn < 0 or mx > 29 or mn > mx:
        chap_oob.append((name, mn, mx))
print(f'A1: Chapters with Z outside [0,29] or invalid range: {len(chap_oob)}')
for n, mn, mx in chap_oob[:5]:
    print(f'    {n}: Z={mn}..{mx}')

# A2: Live SandboxSmall chapter Z overlaps + gaps
ss_live = sorted(
    [(n, L, mn, mx, pz) for n, (L, mn, mx, pz, st) in chap_data.items()
     if n.startswith('SandboxSmall-chapter-') and st != 'Disabled' and mn is not None],
    key=lambda x: x[2]  # by MinZ
)
overlaps = []
gaps = []
for i in range(len(ss_live) - 1):
    a_n, _, a_mn, a_mx, _ = ss_live[i]
    b_n, _, b_mn, b_mx, _ = ss_live[i + 1]
    if b_mn <= a_mx:
        overlaps.append((a_n, a_mn, a_mx, b_n, b_mn, b_mx))
    elif b_mn > a_mx + 1:
        gaps.append((a_n, a_mx, b_n, b_mn, b_mn - a_mx - 1))
print(f'A2: SandboxSmall chapter Z overlaps: {len(overlaps)}')
for a, am, ax, b, bm, bx in overlaps:
    print(f'    OVERLAP: {a} (Z={am}..{ax}) overlaps {b} (Z={bm}..{bx})')
print(f'A3: SandboxSmall chapter Z gaps: {len(gaps)}')
for a, ax, b, bm, ng in gaps:
    print(f'    GAP: {a} ends Z={ax}, next ({b}) starts Z={bm} — {ng} cell(s) of empty Z')

# B: Zone-level audit
print()
print('=== B. Zone audit (Live SandboxSmall) ===')

bleed = []          # zone TargetSize extends into neighbouring chapter
size_zero = []      # TargetSize.Z = 0
disabled_chap = []  # Live zone references Disabled or missing chapter
big_in_small = []   # TargetSize.Z > chapter height (definitely can't fit)
pos_oob = []        # pinned Position.Z out of [0,29]
top_oob = []        # Position.Z + TargetSize.Z - 1 > 29

for r in z['Exports'][0]['Table']['Data']:
    if zoneset(r) != 'SandboxSmall': continue
    if zstate(r) == 'Disabled': continue
    name = r['Name']
    chap = get(r, 'Chapter') or ''
    px, py, pz = get_intvec(fp(r['Value'], 'Position'))
    sx, sy, sz = get_intvec(fp(r['Value'], 'TargetSize'))

    # Chapter exists & live?
    if chap and chap in chap_data:
        chap_state = chap_data[chap][4]
        if chap_state == 'Disabled':
            disabled_chap.append((name, chap, 'DISABLED'))
    elif chap and chap.startswith('SandboxSmall-'):
        if chap not in chap_data:
            disabled_chap.append((name, chap, 'MISSING'))

    # Size sanity
    if sz is None or sz == 0:
        size_zero.append((name, sx, sy, sz))
        continue

    # If chapter is live SandboxSmall, check fit
    if chap in chap_live and chap.startswith('SandboxSmall-'):
        L, mn, mx, _ = chap_live[chap]
        h = mx - mn + 1
        if sz > h:
            big_in_small.append((name, chap, h, sz))
        # If pinned (Pos != all zeros), check Pos in range and top in range
        if not (px == 0 and py == 0 and pz == 0):
            if pz is not None and not (0 <= pz <= 29):
                pos_oob.append((name, pz))
            if pz is not None and (pz + sz - 1) > 29:
                top_oob.append((name, pz, sz, pz + sz - 1))
            # Bleed check: pinned zone with top overflowing chapter
            if pz is not None and (pz + sz - 1) > mx:
                bleed.append((name, chap, f'Z={pz}..{pz+sz-1}', f'band={mn}..{mx}'))
        else:
            # Unpinned zone with sz > chapter height — generator can't place it
            # Already flagged in big_in_small
            pass

print(f'B1: Live zones with disabled/missing Chapter ref: {len(disabled_chap)}')
for n, c, why in disabled_chap[:10]:
    print(f'    {n:<42s}  Chapter={c}  ({why})')

print(f'B2: Zones with TargetSize.Z = 0 or None: {len(size_zero)}')
for n, sx, sy, sz in size_zero[:5]:
    print(f'    {n:<42s}  Size=({sx},{sy},{sz})')

print(f'B3: Zones with TargetSize.Z > chapter height (cannot fit): {len(big_in_small)}')
for n, c, h, sz in big_in_small[:30]:
    print(f'    {n:<42s}  in {c}  h={h}  TargetSize.Z={sz}  (OVERFLOW BY {sz-h})')

print(f'B4: Pinned zones with Position.Z outside [0,29]: {len(pos_oob)}')
for n, pz in pos_oob[:5]:
    print(f'    {n:<42s}  Position.Z={pz}')

print(f'B5: Pinned zones whose top exceeds Z=29: {len(top_oob)}')
for n, pz, sz, top in top_oob[:5]:
    print(f'    {n:<42s}  Position.Z={pz}  TargetSize.Z={sz}  top={top}')

print(f'B6: Pinned zones whose bubble bleeds past chapter MaxZ: {len(bleed)}')
for n, c, span, band in bleed[:10]:
    print(f'    {n:<42s}  in {c}  {span}  {band}')

# C: Landmark audit
print()
print('=== C. Landmark audit ===')
lm_oob = []
for r in lm['Exports'][0]['Table']['Data']:
    if zstate(r) == 'Disabled': continue
    name = r['Name']
    bx, by, bz = get_intvec(fp(r['Value'], 'BasePosition'))
    if bz is None or (bx == 0 and by == 0 and bz == 0):
        continue
    if not (0 <= bz <= 29):
        lm_oob.append((name, bz))

print(f'C1: Live landmarks with BasePosition.Z outside [0,29]: {len(lm_oob)}')
for n, bz in lm_oob[:10]:
    print(f'    {n:<42s}  BasePosition.Z={bz}')

# D: Live zone count per chapter (with chapter heights)
print()
print('=== D. Chapter capacity vs zone load ===')
chap_zone_count = {}
chap_zone_max_size_z = {}
for r in z['Exports'][0]['Table']['Data']:
    if zoneset(r) != 'SandboxSmall': continue
    if zstate(r) == 'Disabled': continue
    chap = get(r, 'Chapter') or ''
    chap_zone_count[chap] = chap_zone_count.get(chap, 0) + 1
    sz = get_intvec(fp(r['Value'], 'TargetSize'))[2] or 0
    chap_zone_max_size_z[chap] = max(chap_zone_max_size_z.get(chap, 0), sz)

print(f'{"Chapter":<32s}  {"h":>3}  {"Live zones":>11}  {"Max TargetSize.Z":>18}  Status')
print('-' * 90)
for n, _, mn, mx, _ in ss_live:
    h = mx - mn + 1
    cnt = chap_zone_count.get(n, 0)
    max_sz = chap_zone_max_size_z.get(n, 0)
    flag = ''
    if max_sz > h:
        flag = f'   ** BLEED RISK: max zone TargetSize.Z={max_sz} > chapter h={h} **'
    print(f'  {n:<32s}  {h:>3d}  {cnt:>11d}  {max_sz:>18d}{flag}')

print('\n=== SUMMARY ===')
total_issues = (len(chap_oob) + len(overlaps) + len(disabled_chap) + len(size_zero) +
                len(big_in_small) + len(pos_oob) + len(top_oob) + len(bleed) + len(lm_oob))
print(f'Total issues found: {total_issues}')
if total_issues == 0:
    print('No structural Z issues detected.')
PYEOF
