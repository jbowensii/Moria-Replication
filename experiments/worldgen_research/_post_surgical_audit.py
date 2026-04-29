"""Post-surgical-fix audit. Run level chart + deep analysis under the
project's locked world rules:
  X/Y/Z range: 0..29 inclusive
  Max TargetSize: 14 x 14 x 4
  Variant overlap: full 100% allowed (vanilla pattern)
  bPositionFromLandmarks: must align with landmark having entry for host chapter
"""
import json
from collections import defaultdict
from pathlib import Path

HERE = Path(__file__).parent

def fp(v, n):
    for p in v or []:
        if isinstance(p, dict) and p.get('Name') == n:
            return p
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
    return str(p.get('Value', '')).split('::')[-1]
def zstate(r):
    p = fp(r.get('Value', []), 'EnabledState')
    return str(p.get('Value', '')).split('::')[-1] if p else None


def main():
    ch = json.loads((HERE / 'DT_Moria_Chapters.json').read_text(encoding='utf-8'))
    z = json.loads((HERE / 'DT_Moria_Zones.json').read_text(encoding='utf-8'))
    lm = json.loads((HERE / 'DT_Moria_Landmarks.json').read_text(encoding='utf-8'))

    # === LEVEL CHART ===
    print('=== LEVEL CHART (after surgical fix) ===')
    counts = defaultdict(int)
    for r in z['Exports'][0]['Table']['Data']:
        if zoneset(r) != 'SandboxSmall': continue
        if zstate(r) == 'Disabled': continue
        counts[get(r, 'Chapter') or '(none)'] += 1

    ss = [r for r in ch['Exports'][0]['Table']['Data']
          if r['Name'].startswith('SandboxSmall-chapter-') and zstate(r) != 'Disabled']
    ss.sort(key=lambda r: -(get(r, 'Layer') or 0))
    hdr = (f'{"Lv":<5}  {"Chapter":<32s}  {"Layer":>6}  {"ChID":>4}  '
           f'{"h":>3}  {"MinZ":>5}  {"MaxZ":>5}  {"PrimeZ":>7}  {"ESL":>3}  {"Live":>5}')
    print(hdr)
    print('-' * len(hdr))
    total_h = 0
    for r in ss:
        L = get(r, 'Layer'); mn = get(r, 'MinZ'); mx = get(r, 'MaxZ'); pz = get(r, 'PrimeZ')
        cid = get(r, 'ChapterID'); esl = get(r, 'EnemyScalingLevel')
        h = mx - mn + 1
        total_h += h
        c = counts.get(r['Name'], 0)
        if L == 0: lv = 'Lv-1'
        elif L > 0: lv = f'Lv-{L+1}'
        else: lv = f'D-{-L}'
        flag = '   EMPTY' if c == 0 else ''
        print(f'{lv:<5}  {r["Name"]:<32s}  {L:>+6d}  {cid:>4}  {h:>3d}  {mn:>5d}  {mx:>5d}  {pz:>7d}  {esl:>3}  {c:>5d}{flag}')
        if L == 0: print('-' * len(hdr) + '   GROUND')
    print(f'\nTotal stack height: {total_h} cells. Range Z=0..29.  Total Live SandboxSmall zones: {sum(counts.values())}')

    # === DEEP ANALYSIS ===
    print('\n=== DEEP ANALYSIS — REMAINING ISSUES UNDER NEW WORLD RULES ===')

    issues_found = 0

    # 1. Pos+Size reach > 29 in any axis
    print('\n--- 1. Position+TargetSize reach exceeds world bound 29 (X/Y/Z) ---')
    cnt = 0
    for r in z['Exports'][0]['Table']['Data']:
        if zoneset(r) != 'SandboxSmall' or zstate(r) == 'Disabled': continue
        px, py, pz = get_intvec(fp(r['Value'], 'Position'))
        sx, sy, sz = get_intvec(fp(r['Value'], 'TargetSize'))
        if None in (px, py, pz, sx, sy, sz): continue
        if px == 0 and py == 0 and pz == 0: continue
        xr = px + sx - 1; yr = py + sy - 1; zr = pz + sz - 1
        if xr > 29 or yr > 29 or zr > 29:
            cnt += 1
            print(f'    {r["Name"]:<42s}  Pos=({px},{py},{pz}) Size=({sx},{sy},{sz}) reach=({xr},{yr},{zr})')
    print(f'  Total: {cnt}')
    issues_found += cnt

    # 2. TargetSize > 14 X/Y or > 4 Z
    print('\n--- 2. TargetSize violates 14x14x4 max rule ---')
    cnt = 0
    for r in z['Exports'][0]['Table']['Data']:
        if zoneset(r) != 'SandboxSmall' or zstate(r) == 'Disabled': continue
        sx, sy, sz = get_intvec(fp(r['Value'], 'TargetSize'))
        if None in (sx, sy, sz): continue
        if sx > 14 or sy > 14 or sz > 4:
            cnt += 1
            print(f'    {r["Name"]:<42s}  Size=({sx},{sy},{sz})')
    print(f'  Total: {cnt}')
    issues_found += cnt

    # 3. Any remaining bPositionFromLandmarks=true
    print('\n--- 3. Zones with bPositionFromLandmarks=True (should be all False) ---')
    cnt = 0
    for r in z['Exports'][0]['Table']['Data']:
        if zoneset(r) != 'SandboxSmall' or zstate(r) == 'Disabled': continue
        pfl = fp(r['Value'], 'bPositionFromLandmarks')
        if pfl and pfl.get('Value') is True:
            cnt += 1
            print(f'    {r["Name"]}')
    print(f'  Total: {cnt}')
    issues_found += cnt

    # 4. Live zones referencing missing/Disabled chapters
    print('\n--- 4. Live zones referencing missing/Disabled chapters ---')
    chap_state = {r['Name']: zstate(r) for r in ch['Exports'][0]['Table']['Data']}
    cnt = 0
    for r in z['Exports'][0]['Table']['Data']:
        if zoneset(r) != 'SandboxSmall' or zstate(r) == 'Disabled': continue
        chap = get(r, 'Chapter')
        if not chap: continue
        st = chap_state.get(chap)
        if st is None:
            cnt += 1; print(f'    {r["Name"]:<42s}  Chapter={chap}  MISSING')
        elif st == 'Disabled':
            cnt += 1; print(f'    {r["Name"]:<42s}  Chapter={chap}  DISABLED')
    print(f'  Total: {cnt}')
    issues_found += cnt

    # 5. Bubble bleed > 1 cell above/below chapter
    print('\n--- 5. Pinned zones bleeding >1 cell beyond chapter band ---')
    chap_mn = {r['Name']: get(r, 'MinZ') for r in ch['Exports'][0]['Table']['Data']}
    chap_mx = {r['Name']: get(r, 'MaxZ') for r in ch['Exports'][0]['Table']['Data']}
    cnt = 0
    for r in z['Exports'][0]['Table']['Data']:
        if zoneset(r) != 'SandboxSmall' or zstate(r) == 'Disabled': continue
        chap = get(r, 'Chapter')
        if chap not in chap_mn: continue
        px, py, pz = get_intvec(fp(r['Value'], 'Position'))
        sx, sy, sz = get_intvec(fp(r['Value'], 'TargetSize'))
        if None in (px, py, pz, sx, sy, sz): continue
        if px == 0 and py == 0 and pz == 0: continue
        cmn = chap_mn[chap]; cmx = chap_mx[chap]
        if cmn is None or cmx is None: continue
        top = pz + sz - 1
        bleed_above = max(0, top - cmx)
        bleed_below = max(0, cmn - pz)
        if bleed_above > 1 or bleed_below > 1:
            cnt += 1
            print(f'    {r["Name"]:<42s}  in {chap}  Z={pz}..{top}  band={cmn}..{cmx}  '
                  f'bleed={"+"+str(bleed_above) if bleed_above else "-"+str(bleed_below)}')
    print(f'  Total (bleed > 1): {cnt}')
    issues_found += cnt

    # 6. Stair zones with no Layer±1 neighbour
    print('\n--- 6. Extended-connectivity stairs without Layer±1 Live neighbour ---')
    chap_layer = {r['Name']: get(r, 'Layer') for r in ch['Exports'][0]['Table']['Data']
                  if zstate(r) != 'Disabled'}
    live_layers = set(chap_layer.values())
    cnt = 0
    for r in z['Exports'][0]['Table']['Data']:
        if zoneset(r) != 'SandboxSmall' or zstate(r) == 'Disabled': continue
        chap = get(r, 'Chapter')
        if chap not in chap_layer: continue
        L = chap_layer[chap]
        lh = fp(r['Value'], 'LandmarkHandles')
        if not lh: continue
        for e in (lh.get('Value') or []):
            inner = e.get('Value') if isinstance(e, dict) else None
            if not isinstance(inner, list): continue
            rn = ''; ext = False
            for sub in inner:
                if isinstance(sub, dict):
                    if sub.get('Name') == 'Landmark':
                        for it in (sub.get('Value') or []):
                            if isinstance(it, dict) and it.get('Name') == 'RowName':
                                rn = it.get('Value', '')
                    elif sub.get('Name') == 'bExtendedConnectivityLandmark':
                        ext = sub.get('Value') is True
            if ext and rn:
                up = L + 1 in live_layers
                down = L - 1 in live_layers
                if not (up or down):
                    cnt += 1
                    print(f'    {r["Name"]:<42s}  Layer={L} landmark={rn}  no neighbours')
    print(f'  Total: {cnt}')
    issues_found += cnt

    # 7. Variant overlap groups (informational, not an issue)
    print('\n--- 7. Variant overlap groups (informational — vanilla pattern) ---')
    groups = defaultdict(list)
    for r in z['Exports'][0]['Table']['Data']:
        if zoneset(r) != 'SandboxSmall' or zstate(r) == 'Disabled': continue
        pos = get_intvec(fp(r['Value'], 'Position'))
        siz = get_intvec(fp(r['Value'], 'TargetSize'))
        if pos == (0, 0, 0) or None in pos or None in siz: continue
        groups[(pos, siz)].append(r['Name'])
    grp_count = sum(1 for v in groups.values() if len(v) > 1)
    print(f'  {grp_count} variant groups (same Pos+Size — generator picks one):')
    for k, v in groups.items():
        if len(v) < 2: continue
        print(f'    Pos={k[0]} Size={k[1]}: {v}')

    # 8. Landmark BasePos.Z vs host zone Z mismatch
    print('\n--- 8. Landmark BasePos.Z >3 cells from host zone Z-range ---')
    hosts = defaultdict(list)
    for r in z['Exports'][0]['Table']['Data']:
        if zoneset(r) != 'SandboxSmall' or zstate(r) == 'Disabled': continue
        px, py, pz = get_intvec(fp(r['Value'], 'Position'))
        sx, sy, sz = get_intvec(fp(r['Value'], 'TargetSize'))
        if px == 0 and py == 0 and pz == 0: continue
        lh = fp(r['Value'], 'LandmarkHandles')
        if not lh: continue
        for e in (lh.get('Value') or []):
            inner = e.get('Value') if isinstance(e, dict) else None
            if not isinstance(inner, list): continue
            for sub in inner:
                if isinstance(sub, dict) and sub.get('Name') == 'Landmark':
                    for it in (sub.get('Value') or []):
                        if isinstance(it, dict) and it.get('Name') == 'RowName':
                            n = it.get('Value', '')
                            if n:
                                hosts[n].append((r['Name'], pz, pz + (sz or 1) - 1))
    cnt = 0
    for r in lm['Exports'][0]['Table']['Data']:
        if zstate(r) == 'Disabled': continue
        n = r['Name']
        bp = fp(r['Value'], 'BasePosition')
        bx, by, bz = get_intvec(bp)
        if (bx, by, bz) == (0, 0, 0) or bz is None: continue
        if n not in hosts: continue
        for hn, hpz, htop in hosts[n]:
            if bz < hpz - 3 or bz > htop + 3:
                cnt += 1
                print(f'    {n:<42s}  BasePos.Z={bz} vs host {hn} Z={hpz}..{htop}')
                break
    print(f'  Total: {cnt}')
    issues_found += cnt

    # 9. Duplicate ChapterIDs (map UI bug)
    print('\n--- 9. Duplicate ChapterID values (map UI display bug) ---')
    chap_ids = [get(r, 'ChapterID') for r in ss]
    dups = {x for x in chap_ids if chap_ids.count(x) > 1}
    if dups:
        print(f'    Duplicates: {sorted(dups)} — currently DEFERRED')
    else:
        print(f'    No duplicates.')

    print()
    print('=' * 70)
    print(f'TOTAL HARD ISSUES: {issues_found}')


if __name__ == '__main__':
    main()
