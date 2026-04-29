"""Map display regression diagnostic.

Compares pre-sync vs post-sync landmark BasePositions and audits per-chapter
landmark counts, host-zone footprint overlaps, and (0,0,Z) sentinel changes.
Read-only.
"""
import json
from pathlib import Path
from collections import defaultdict

WGR = Path(__file__).resolve().parent
LMS_POST = WGR / 'DT_Moria_Landmarks.json'
LMS_PRE = WGR / 'DT_Moria_Landmarks.before_global_bp_sync.json'
ZONES = WGR / 'DT_Moria_Zones.json'
CHAPTERS = WGR / 'DT_Moria_Chapters.json'


def load(p):
    with open(p, 'r', encoding='utf-8') as f:
        return json.load(f)


def find_rows(u):
    for e in u.get('Exports', []):
        t = e.get('Table')
        if t and 'Data' in t:
            return t['Data']
    return []


def fp(v, n):
    for p in v or []:
        if isinstance(p, dict) and p.get('Name') == n:
            return p
    return None


def pv(v, n):
    p = fp(v, n)
    return p.get('Value') if p else None


def gv(p):
    if not p:
        return None
    v = p.get('Value')
    if isinstance(v, list) and v:
        d = v[0].get('Value') if isinstance(v[0], dict) else None
        if isinstance(d, dict):
            return (d.get('X'), d.get('Y'), d.get('Z'))
    return None


def gv_named(props, name):
    return gv(fp(props, name))


def landmark_handles(rd):
    out = []
    p = fp(rd, 'LandmarkHandles')
    if not p:
        return out
    for entry in p.get('Value', []) or []:
        ep = entry.get('Value', []) or []
        lh = fp(ep, 'Landmark')
        if lh:
            inner = lh.get('Value', []) or []
            rn = fp(inner, 'RowName')
            if rn:
                out.append(rn.get('Value'))
    return out


def addl_chapters(rd):
    out = []
    p = fp(rd, 'AdditionalChapters')
    if not p:
        return out
    for entry in p.get('Value', []) or []:
        if isinstance(entry, dict):
            inner = entry.get('Value', []) or []
            if isinstance(inner, list):
                rn = fp(inner, 'RowName')
                if rn:
                    out.append(rn.get('Value'))
            else:
                # NamePropertyData direct
                v = entry.get('Value')
                if isinstance(v, str):
                    out.append(v)
    return out


def chapter_ref(rd):
    p = fp(rd, 'Chapter')
    if not p:
        return None
    inner = p.get('Value', []) or []
    rn = fp(inner, 'RowName')
    if rn:
        return rn.get('Value')
    return None


def main():
    zd = find_rows(load(ZONES))
    cd = find_rows(load(CHAPTERS))
    pre = find_rows(load(LMS_PRE))
    post = find_rows(load(LMS_POST))

    # Build chapter index: name -> (cid, minz, maxz, layer, displayName, isLevelRow)
    chapters = {}
    cid_to_levelrow = {}
    for r in cd:
        v = r.get('Value', [])
        if pv(v, 'ZoneSet') != 'EZoneSet::SandboxSmall':
            continue
        if pv(v, 'EnabledState') != 'ERowEnabledState::Live':
            continue
        cid = pv(v, 'ChapterID')
        minz = pv(v, 'MinZ')
        maxz = pv(v, 'MaxZ')
        layer = pv(v, 'Layer')
        dn = pv(v, 'DisplayName')
        primez = pv(v, 'PrimeZ')
        chapters[r['Name']] = dict(cid=cid, minz=minz, maxz=maxz, layer=layer,
                                   dn=dn, primez=primez)
        # Heuristic: "level row" is one whose row-name ends in .LevelN, .DeepN, .Level1...Level7
        nm = r['Name']
        suffix = nm.split('.', 1)[-1] if '.' in nm else ''
        if suffix.startswith('Level') or suffix.startswith('Deep'):
            cid_to_levelrow[cid] = nm

    # Build landmark dict by name for both pre and post
    pre_by = {r.get('Name', ''): r for r in pre}
    post_by = {r.get('Name', ''): r for r in post}

    def lm_state(r):
        return pv(r.get('Value', []), 'EnabledState')

    def lm_bp(r):
        return gv_named(r.get('Value', []), 'BasePosition')

    # Index Live SS zones
    ss_zones = []
    for r in zd:
        v = r.get('Value', [])
        if pv(v, 'ZoneSet') != 'EZoneSet::SandboxSmall':
            continue
        if pv(v, 'EnabledState') != 'ERowEnabledState::Live':
            continue
        ss_zones.append(r)

    # ----- Section 1: BP changes from pre -> post -----
    print('=' * 78)
    print('SECTION 1: Landmark BP changes (pre -> post)')
    print('=' * 78)
    bp_changes = []
    for name, post_r in post_by.items():
        if lm_state(post_r) != 'ERowEnabledState::Live':
            continue
        pre_r = pre_by.get(name)
        if not pre_r:
            continue
        pb = lm_bp(pre_r)
        ob = lm_bp(post_r)
        if pb != ob:
            bp_changes.append((name, pb, ob))
    print(f'Total Live SS-relevant BP changes: {len(bp_changes)}')

    # ----- Section 2: (0,0,Z) sentinel landmarks moved off (0,0,*) -----
    print()
    print('=' * 78)
    print('SECTION 2: (0,0,Z) sentinel BPs moved to non-zero X/Y')
    print('=' * 78)
    sentinel_moves = []
    for name, pb, ob in bp_changes:
        if pb and pb[0] == 0 and pb[1] == 0:
            sentinel_moves.append((name, pb, ob))
    for n, pb, ob in sentinel_moves:
        print(f'  {n:42s}  {pb} -> {ob}')
    print(f'Count: {len(sentinel_moves)}')

    # ----- Section 3: per-chapter Live landmark counts (BP.Z within chapter Z band) -----
    print()
    print('=' * 78)
    print('SECTION 3: Live landmark count by chapter Z band (pre vs post)')
    print('=' * 78)

    # Build set of unique Z bands -> level/deep rows
    level_rows = []
    for cname, ci in chapters.items():
        # Look for level rows or deep rows
        suffix = cname.split('.', 1)[-1] if '.' in cname else ''
        is_level = suffix.startswith('Level') or suffix.startswith('Deep')
        if is_level:
            level_rows.append((cname, ci))
    level_rows.sort(key=lambda x: x[1]['layer'])

    def count_in_band(rows_dict, minz, maxz):
        n = 0
        for nm, r in rows_dict.items():
            if lm_state(r) != 'ERowEnabledState::Live':
                continue
            bp = lm_bp(r)
            if bp and bp[2] is not None and minz <= bp[2] <= maxz:
                n += 1
        return n

    print(f"{'chapter':40s} {'layer':>5s} {'minZ':>4s} {'maxZ':>4s} {'pre':>5s} {'post':>5s}")
    for cname, ci in level_rows:
        pre_n = count_in_band(pre_by, ci['minz'], ci['maxz'])
        post_n = count_in_band(post_by, ci['minz'], ci['maxz'])
        marker = ''
        if pre_n != post_n:
            marker = '  <-- changed'
        print(f"{cname:40s} {ci['layer']:>5d} {ci['minz']:>4d} {ci['maxz']:>4d} {pre_n:>5d} {post_n:>5d}{marker}")

    # ----- Section 4: Host validity & footprint overlap audit -----
    print()
    print('=' * 78)
    print('SECTION 4: Footprint overlaps after BP sync')
    print('=' * 78)
    # For each Live SS zone: compute footprint, group by Z, look for overlaps.
    cells_by_z = defaultdict(list)  # z -> [(zone_name, x_lo, x_hi, y_lo, y_hi)]
    for r in ss_zones:
        v = r.get('Value', [])
        pos = gv_named(v, 'Position')
        ts = gv_named(v, 'TargetSize')
        if not (pos and ts):
            continue
        x0, y0, z = pos
        sx, sy, sz = ts
        cells_by_z[z].append((r['Name'], x0, x0 + sx - 1, y0, y0 + sy - 1, sx, sy))

    overlaps = []
    for z, lst in cells_by_z.items():
        for i in range(len(lst)):
            for j in range(i + 1, len(lst)):
                a = lst[i]; b = lst[j]
                if (a[1] <= b[2] and b[1] <= a[2] and
                        a[3] <= b[4] and b[3] <= a[4]):
                    overlaps.append((z, a, b))
    print(f'Total Live SS zone-zone footprint overlaps: {len(overlaps)}')
    # Show overlaps involving stair / elevator / disappeared-floor zones
    floors_of_interest = {23, 27, 28, 4, 1, 0}  # Lv5..Lv7 + D5..D7
    for z, a, b in overlaps:
        if z in floors_of_interest:
            print(f'  Z={z}: {a[0]}  X[{a[1]}..{a[2]}] Y[{a[3]}..{a[4]}]')
            print(f'         vs {b[0]}  X[{b[1]}..{b[2]}] Y[{b[3]}..{b[4]}]')

    # ----- Section 5: AdditionalChapters audit for elevator-like zones -----
    print()
    print('=' * 78)
    print('SECTION 5: Zones with AdditionalChapters (elevator/stair bridges)')
    print('=' * 78)
    print(f"{'zone':42s} {'pos':>16s} {'sz':>10s} {'chapter':30s} {'addl':30s}")
    for r in ss_zones:
        v = r.get('Value', [])
        addl = addl_chapters(v)
        if not addl:
            continue
        pos = gv_named(v, 'Position')
        ts = gv_named(v, 'TargetSize')
        ch = chapter_ref(v)
        print(f"  {r['Name']:40s} {str(pos):>16s} {str(ts):>10s} {str(ch):30s} {','.join(addl)}")

    # ----- Section 6: Orphaned landmarks (Live, but no Live SS host zone references it) -----
    print()
    print('=' * 78)
    print('SECTION 6: Orphan check — Live SS landmarks with no Live SS host zone')
    print('=' * 78)
    referenced = set()
    for r in ss_zones:
        v = r.get('Value', [])
        for ln in landmark_handles(v):
            referenced.add(ln)
            # also accept short tail forms
    # collect all live landmark names in post
    orphans = []
    for n, r in post_by.items():
        if lm_state(r) != 'ERowEnabledState::Live':
            continue
        # Match: full name OR tail-after-last-dot
        tail = n.split('.')[-1]
        if n in referenced or tail in referenced:
            continue
        # also match: any referenced ends with '.tail' equal to this n's tail? handled by tail check
        # check reverse: any reference in 'referenced' that equals tail or full
        orphans.append(n)
    # Filter for landmarks within SS Z bands
    ss_zbands = sorted({(c['minz'], c['maxz']) for c in chapters.values()})
    def in_ss_band(z):
        if z is None:
            return False
        for mn, mx in ss_zbands:
            if mn <= z <= mx:
                return True
        return False
    orphans_ss = [n for n in orphans if in_ss_band(lm_bp(post_by[n])[2] if lm_bp(post_by[n]) else None)]
    print(f'Total Live landmarks not referenced by any Live SS zone: {len(orphans)}')
    print(f'  Of which BP.Z falls inside an SS chapter Z band: {len(orphans_ss)}')
    for n in orphans_ss[:30]:
        print(f'  {n:50s} BP={lm_bp(post_by[n])}')

    # ----- Section 7: Specific elevator landmarks pre/post -----
    print()
    print('=' * 78)
    print('SECTION 7: Elevator/stair landmark changes (focus list)')
    print('=' * 78)
    focus = ['ThirdStair', 'SixthStair', 'EighthStair', 'SeventhStair',
            'CrystalDescent', 'LowerDescent', 'FourthStair', 'FifthStair',
            'SecondStair', 'FirstStair']
    for n, r in sorted(post_by.items()):
        if lm_state(r) != 'ERowEnabledState::Live':
            continue
        tail = n.split('.')[-1]
        if tail not in focus:
            continue
        pb = lm_bp(pre_by.get(n)) if n in pre_by else None
        ob = lm_bp(r)
        # Find host zones (Live SS) referencing it
        hosts = []
        for zr in ss_zones:
            v = zr.get('Value', [])
            lhs = landmark_handles(v)
            if n in lhs or tail in lhs:
                pos = gv_named(v, 'Position')
                ts = gv_named(v, 'TargetSize')
                bpfl = pv(v, 'bPositionFromLandmarks')
                ch = chapter_ref(v)
                addl = addl_chapters(v)
                hosts.append((zr['Name'], pos, ts, bpfl, ch, addl))
        print(f'\n  {n}  pre_BP={pb}  post_BP={ob}')
        for hn, pos, ts, bpfl, ch, addl in hosts:
            print(f'    host: {hn}  Pos={pos}  Sz={ts}  bPosFromLM={bpfl}  Ch={ch}  Addl={addl}')


if __name__ == '__main__':
    main()
