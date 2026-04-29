"""Lv-5 / Lv-6 vs Lv-1 / Lv-2 structural deep-dive.

For each of the 4 floors, dumps:
  - level row + all anchored chapter rows sharing the CID
  - all Live SS zones whose Chapter or AdditionalChapters references the level
  - per-zone: Position, TargetSize, Chapter, AdditionalChapters, LandmarkHandles
  - landmarks whose BP.Z falls in the band
  - any zone-zone overlaps within the band

Read-only.
"""
import json
from pathlib import Path
from collections import defaultdict

WGR = Path(__file__).resolve().parent
LMS = WGR / 'DT_Moria_Landmarks.json'
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


def gameplay_tags(rd):
    out = []
    p = fp(rd, 'GameplayTags')
    if not p:
        return out
    v = p.get('Value', [])
    if isinstance(v, list):
        # nested struct, descend
        for item in v:
            if isinstance(item, dict):
                inner = item.get('Value', [])
                if isinstance(inner, list):
                    for ii in inner:
                        if isinstance(ii, dict) and ii.get('Name') == 'GameplayTags':
                            arr = ii.get('Value', [])
                            for tag in arr or []:
                                if isinstance(tag, dict):
                                    tg = tag.get('Value', [])
                                    if isinstance(tg, list):
                                        for tt in tg:
                                            if isinstance(tt, dict) and tt.get('Name') == 'TagName':
                                                out.append(tt.get('Value'))
    return out


def main():
    zd = find_rows(load(ZONES))
    cd = find_rows(load(CHAPTERS))
    ld = find_rows(load(LMS))

    chapters = {}
    for r in cd:
        v = r.get('Value', [])
        chapters[r['Name']] = dict(
            zoneset=pv(v, 'ZoneSet'),
            state=pv(v, 'EnabledState'),
            cid=pv(v, 'ChapterID'),
            minz=pv(v, 'MinZ'),
            maxz=pv(v, 'MaxZ'),
            primez=pv(v, 'PrimeZ'),
            layer=pv(v, 'Layer'),
            dn=pv(v, 'DisplayName'),
        )

    ss_zones = []
    for r in zd:
        v = r.get('Value', [])
        if pv(v, 'ZoneSet') != 'EZoneSet::SandboxSmall':
            continue
        if pv(v, 'EnabledState') != 'ERowEnabledState::Live':
            continue
        ss_zones.append(r)

    lm_by = {r.get('Name', ''): r for r in ld}

    targets = [
        ('Lv-1', 'SandboxSmall-Chapter01.Level1', 18, 1),
        ('Lv-2', 'SandboxSmall-Chapter02.Level2', 20, 2),
        ('Lv-5', 'SandboxSmall-Chapter05.Level5', 23, 5),
        ('Lv-6', 'SandboxSmall-Chapter06.Level6', 27, 6),
    ]

    for label, level_row, z, cid in targets:
        print('=' * 78)
        print(f'  {label}  level row: {level_row}  Z={z}  CID={cid}')
        print('=' * 78)

        # 1. anchored chapter rows with same CID
        print('\n--- (1) Chapter rows with this CID ---')
        for cname, ci in chapters.items():
            if ci['cid'] == cid:
                print(f"  {cname:50s} ZS={ci['zoneset']:25s} state={str(ci['state']):28s} "
                      f"layer={ci['layer']} minZ={ci['minz']} maxZ={ci['maxz']}")

        # 2. Live SS zones referencing this chapter (Chapter or AdditionalChapters) OR at Z
        print('\n--- (2) Live SS zones referencing this floor ---')
        floor_zones = []
        for r in ss_zones:
            v = r.get('Value', [])
            ch = chapter_ref(v)
            addl = addl_chapters(v)
            pos = gv_named(v, 'Position')
            zmatch = pos and pos[2] == z
            if (ch and (level_row in ch or chapters.get(ch, {}).get('cid') == cid)) \
                    or any(level_row in a or chapters.get(a, {}).get('cid') == cid for a in addl) \
                    or zmatch:
                floor_zones.append(r)

        for r in floor_zones:
            v = r.get('Value', [])
            pos = gv_named(v, 'Position')
            ts = gv_named(v, 'TargetSize')
            ch = chapter_ref(v)
            addl = addl_chapters(v)
            bpfl = pv(v, 'bPositionFromLandmarks')
            lhs = landmark_handles(v)
            tags = gameplay_tags(v)
            tpl = pv(v, 'bUseTemplate')
            templ_arr = fp(v, 'Templates')
            templ_n = len(templ_arr.get('Value', []) or []) if templ_arr else 0
            ext = pv(v, 'bExtendFootprint')
            print(f"  {r['Name']:42s} Pos={pos}  Sz={ts}  bPosFL={bpfl}  bExt={ext}")
            print(f"    Ch={ch}  Addl={addl}")
            print(f"    LH={lhs}  Tags={tags[:3]}  bUseTemplate={tpl} templ#={templ_n}")

        # 3. Landmarks with BP.Z == z
        print(f'\n--- (3) Live landmarks at Z={z} ---')
        for n, r in lm_by.items():
            v = r.get('Value', [])
            if pv(v, 'EnabledState') != 'ERowEnabledState::Live':
                continue
            bp = gv_named(v, 'BasePosition')
            if bp and bp[2] == z:
                # Find host zone(s)
                hosts = []
                for zr in floor_zones:
                    lhs = landmark_handles(zr.get('Value', []))
                    if n in lhs or n.split('.')[-1] in lhs:
                        hosts.append(zr['Name'])
                print(f"  {n:48s} BP={bp}  hosts={hosts}")

        # 4. Zone-zone overlaps at this Z
        print(f'\n--- (4) Footprint overlaps at Z={z} ---')
        cells = []
        for r in floor_zones:
            v = r.get('Value', [])
            pos = gv_named(v, 'Position')
            ts = gv_named(v, 'TargetSize')
            if not (pos and ts):
                continue
            if pos[2] != z:
                continue
            cells.append((r['Name'], pos[0], pos[0] + ts[0] - 1,
                          pos[1], pos[1] + ts[1] - 1))
        ov = []
        for i in range(len(cells)):
            for j in range(i + 1, len(cells)):
                a = cells[i]; b = cells[j]
                if a[1] <= b[2] and b[1] <= a[2] and a[3] <= b[4] and b[3] <= a[4]:
                    ov.append((a, b))
        if not ov:
            print('  none')
        for a, b in ov:
            print(f'  {a[0]} X[{a[1]}..{a[2]}] Y[{a[3]}..{a[4]}]  vs  '
                  f'{b[0]} X[{b[1]}..{b[2]}] Y[{b[3]}..{b[4]}]')

        # 5. Counts summary
        print('\n--- (5) Summary counts ---')
        primary = sum(1 for r in floor_zones
                      if (chapters.get(chapter_ref(r.get('Value', [])), {}) or {}).get('cid') == cid)
        bridge = sum(1 for r in floor_zones
                     if any(chapters.get(a, {}).get('cid') == cid
                            for a in addl_chapters(r.get('Value', []))))
        total_lh = sum(len(landmark_handles(r.get('Value', []))) for r in floor_zones)
        print(f'  zones primary chapter={primary}  bridge-via-Addl={bridge}  total floor zones={len(floor_zones)}  total LH refs={total_lh}')


if __name__ == '__main__':
    main()
