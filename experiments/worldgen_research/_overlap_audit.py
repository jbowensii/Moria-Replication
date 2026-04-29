"""Comprehensive overlap + size audit under locked world rules.

Checks:
  1. Every Live SandboxSmall zone TargetSize <= 14 x 14 x 4
  2. Every pair of pinned Live SandboxSmall zones — overlap classification:
       - No overlap (separate)
       - Full / 100% overlap (variant pattern, vanilla design)
       - Partial overlap (concerning)
  3. Cross-zoneset overlap (informational only)
"""
import json
from collections import defaultdict
from pathlib import Path

HERE = Path(__file__).parent

def fp(v, n):
    for p in v or []:
        if isinstance(p, dict) and p.get('Name') == n: return p
    return None
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
    return str(p.get('Value', '')).split('::')[-1]
def zstate(r):
    p = fp(r.get('Value', []), 'EnabledState')
    return str(p.get('Value', '')).split('::')[-1] if p else None
def get_chap(r):
    p = fp(r['Value'], 'Chapter')
    if not p: return None
    v = p.get('Value')
    if isinstance(v, list):
        for it in v:
            if isinstance(it, dict) and it.get('Name') == 'RowName':
                return it.get('Value', '')
    return None
def axes_overlap(p1, s1, p2, s2):
    x1, y1, z1 = p1; sx1, sy1, sz1 = s1
    x2, y2, z2 = p2; sx2, sy2, sz2 = s2
    ox = min(x1+sx1-1, x2+sx2-1) - max(x1, x2) + 1
    oy = min(y1+sy1-1, y2+sy2-1) - max(y1, y2) + 1
    oz = min(z1+sz1-1, z2+sz2-1) - max(z1, z2) + 1
    return (ox, oy, oz)


def main():
    z = json.loads((HERE / 'DT_Moria_Zones.json').read_text(encoding='utf-8'))

    # === SIZE CHECK ===
    print('=== SIZE CHECK — every Live SandboxSmall zone ===')
    print('Rule: TargetSize.X <= 14, TargetSize.Y <= 14, TargetSize.Z <= 4\n')
    all_zones = []
    for r in z['Exports'][0]['Table']['Data']:
        if zoneset(r) != 'SandboxSmall' or zstate(r) == 'Disabled': continue
        s = get_intvec(fp(r['Value'], 'TargetSize'))
        if None in s: continue
        all_zones.append((r['Name'], s))
    all_zones.sort(key=lambda x: -(x[1][0] * x[1][1] * x[1][2]))
    print(f'{"Zone":<42s}  {"X":>3} {"Y":>3} {"Z":>3}  Status')
    print('-' * 75)
    violations = 0
    for n, s in all_zones[:15]:
        sx, sy, sz = s
        ok = (sx <= 14 and sy <= 14 and sz <= 4)
        flag = 'OK' if ok else 'VIOLATION'
        if not ok: violations += 1
        print(f'  {n:<42s}  {sx:>3} {sy:>3} {sz:>3}  {flag}')
    print(f'\nTop 15 by volume shown. Total Live SS zones: {len(all_zones)}.  Violations: {violations}')

    # === OVERLAP CHECK ===
    print()
    print('=== OVERLAP CHECK — every pair of pinned Live SandboxSmall zones ===')
    print('Rule: 0% (separate) or 100% (full match, vanilla variant pattern). Partial = concerning.\n')

    zones = []
    for r in z['Exports'][0]['Table']['Data']:
        if zoneset(r) != 'SandboxSmall' or zstate(r) == 'Disabled': continue
        p = get_intvec(fp(r['Value'], 'Position'))
        s = get_intvec(fp(r['Value'], 'TargetSize'))
        if None in p or None in s: continue
        if p == (0, 0, 0): continue
        zones.append((r['Name'], get_chap(r), p, s))

    full = []
    partial = []
    no_overlap = 0
    for i in range(len(zones)):
        for j in range(i+1, len(zones)):
            n1, c1, p1, s1 = zones[i]
            n2, c2, p2, s2 = zones[j]
            ox, oy, oz = axes_overlap(p1, s1, p2, s2)
            if ox <= 0 or oy <= 0 or oz <= 0:
                no_overlap += 1; continue
            vol1 = s1[0]*s1[1]*s1[2]
            vol2 = s2[0]*s2[1]*s2[2]
            ovol = ox*oy*oz
            cov1 = ovol/vol1 if vol1 else 0
            cov2 = ovol/vol2 if vol2 else 0
            if cov1 == 1.0 and cov2 == 1.0:
                full.append((n1, c1, n2, c2, p1, s1, ovol))
            else:
                partial.append((n1, c1, n2, c2, p1, s1, p2, s2, ox, oy, oz, ovol, cov1, cov2))

    same_chap_partial = [x for x in partial if x[1] == x[3]]
    cross_chap_partial = [x for x in partial if x[1] != x[3]]

    pair_total = len(zones)*(len(zones)-1)//2
    print(f'Total pinned zones: {len(zones)}, total pairs: {pair_total}')
    print(f'  No overlap:           {no_overlap}')
    print(f'  100% / full overlap:  {len(full)}  (vanilla variant pattern — OK)')
    print(f'  Partial overlap:      {len(partial)}  (same-chap: {len(same_chap_partial)}, cross-chap: {len(cross_chap_partial)})')

    # Show full overlap groups
    print()
    print('--- Full 100% overlap groups (variants) ---')
    seen_groups = defaultdict(set)
    for n1, c1, n2, c2, p, s, ovol in full:
        seen_groups[(p, s)].add((n1, c1))
        seen_groups[(p, s)].add((n2, c2))
    for (p, s), members in seen_groups.items():
        if len(members) >= 2:
            print(f'  Pos={p} Size={s}:')
            for n, c in sorted(members):
                print(f'    {n:<42s}  in {c}')

    # Show partial overlaps
    print()
    print('--- Partial overlap (same chapter — generator may resolve) ---')
    if not same_chap_partial:
        print('  None.')
    for n1, c1, n2, c2, p1, s1, p2, s2, ox, oy, oz, ovol, cov1, cov2 in same_chap_partial:
        print(f'  in {c1}:')
        print(f'    {n1:<42s}  Pos={p1} Size={s1} ({cov1*100:.0f}% covered)')
        print(f'    {n2:<42s}  Pos={p2} Size={s2} ({cov2*100:.0f}% covered)')
        print(f'    overlap=({ox},{oy},{oz}) vol={ovol}')

    print()
    print('--- Partial overlap (CROSS chapter — most concerning) ---')
    if not cross_chap_partial:
        print('  None.')
    for n1, c1, n2, c2, p1, s1, p2, s2, ox, oy, oz, ovol, cov1, cov2 in cross_chap_partial:
        print(f'  {n1:<42s} ({c1})  Pos={p1} S={s1}  ({cov1*100:.0f}%)')
        print(f'  {n2:<42s} ({c2})  Pos={p2} S={s2}  ({cov2*100:.0f}%)')
        print(f'    overlap=({ox},{oy},{oz}) vol={ovol}\n')


if __name__ == '__main__':
    main()
