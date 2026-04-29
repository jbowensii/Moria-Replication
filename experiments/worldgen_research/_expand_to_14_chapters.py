"""Expand SandboxSmall from 8 chapters (3 above + ground + 4 below) to
14 chapters (6 above + ground + 7 below).

Chapter numbering convention (per user request, "rotation"):
  chapter-1   = Layer  0  (ground)
  chapter-2   = Layer +1  (Lv-2)
  chapter-3   = Layer +2  (Lv-3)
  chapter-4   = Layer +3  (Lv-4)
  chapter-5   = Layer +4  (Lv-5, NEW)
  chapter-6   = Layer +5  (Lv-6, NEW)
  chapter-7   = Layer +6  (Lv-7, NEW)
  chapter-8   = Layer -7  (Deep 7, absolute bottom, NEW)
  chapter-9   = Layer -6  (Deep 6, NEW)
  chapter-10  = Layer -5  (Deep 5, NEW)
  chapter-11  = Layer -4  (RENAMED from pristine chapter-8 / Deep 4)
  chapter-12  = Layer -3  (RENAMED from pristine chapter-7 / Deep 3)
  chapter-13  = Layer -2  (RENAMED from pristine chapter-6 / Deep 2)
  chapter-14  = Layer -1  (RENAMED from pristine chapter-5 / Deep 1)

Z-band stack (38 cells total):
  chapter-7   +6  Z=36..38  PrimeZ=37
  chapter-6   +5  Z=33..35  PrimeZ=34
  chapter-5   +4  Z=30..32  PrimeZ=31
  chapter-4   +3  Z=27..29  PrimeZ=28
  chapter-3   +2  Z=23..26  PrimeZ=24
  chapter-2   +1  Z=22..22  PrimeZ=22
  chapter-1    0  Z=20..21  PrimeZ=20  (ground)
  chapter-14  -1  Z=18..19  PrimeZ=18
  chapter-13  -2  Z=16..17  PrimeZ=16
  chapter-12  -3  Z=13..15  PrimeZ=14
  chapter-11  -4  Z=10..12  PrimeZ=11
  chapter-10  -5  Z=7..9    PrimeZ=8
  chapter-9   -6  Z=4..6    PrimeZ=5
  chapter-8   -7  Z=1..3    PrimeZ=2

Transforms:
  Chapters: rename 4 pristine rows (chapter-5..8 → chapter-14..11),
            update Z bands on all 8 pristine + add 6 new rows.
  Zones:    shift Position.Z += 9 for Live SandboxSmall zones (skip Pos=0,0,0).
            Retarget Chapter ref + AdditionalChapters[] for chapter-5..8.
  Landmarks: shift BasePosition.Z += 9 for landmarks attached only to
             SandboxSmall zones (skip campaign-bound and zero-Z).
  LayoutConnections: retarget any chapter refs (rare).
"""
import copy
import json
import shutil
from pathlib import Path

HERE = Path(__file__).parent

# ---------------------------------------------------------------------
# Final chapter spec (after expansion)
#   Each tuple is: row name, Layer, MinZ, MaxZ, PrimeZ, EnemyScalingLevel
# ---------------------------------------------------------------------
NEW_CHAPTER_SPEC = [
    ('SandboxSmall-chapter-1',   0, 20, 21, 20, 0),  # ground
    ('SandboxSmall-chapter-2',   1, 22, 22, 22, 1),
    ('SandboxSmall-chapter-3',   2, 23, 26, 24, 2),
    ('SandboxSmall-chapter-4',   3, 27, 29, 28, 3),
    ('SandboxSmall-chapter-5',   4, 30, 32, 31, 4),  # NEW Lv-5
    ('SandboxSmall-chapter-6',   5, 33, 35, 34, 5),  # NEW Lv-6
    ('SandboxSmall-chapter-7',   6, 36, 38, 37, 6),  # NEW Lv-7
    ('SandboxSmall-chapter-8',  -7,  1,  3,  2, 7),  # NEW D-7 (absolute bottom)
    ('SandboxSmall-chapter-9',  -6,  4,  6,  5, 6),  # NEW D-6
    ('SandboxSmall-chapter-10', -5,  7,  9,  8, 5),  # NEW D-5
    ('SandboxSmall-chapter-11', -4, 10, 12, 11, 4),  # RENAMED from pristine chapter-8
    ('SandboxSmall-chapter-12', -3, 13, 15, 14, 3),  # RENAMED from pristine chapter-7
    ('SandboxSmall-chapter-13', -2, 16, 17, 16, 2),  # RENAMED from pristine chapter-6
    ('SandboxSmall-chapter-14', -1, 18, 19, 18, 1),  # RENAMED from pristine chapter-5
]

# Pristine row name → new row name mapping (for the 4 renames)
RENAME = {
    'SandboxSmall-chapter-5':  'SandboxSmall-chapter-14',
    'SandboxSmall-chapter-6':  'SandboxSmall-chapter-13',
    'SandboxSmall-chapter-7':  'SandboxSmall-chapter-12',
    'SandboxSmall-chapter-8':  'SandboxSmall-chapter-11',
}

Z_SHIFT = 9  # uniform +9 shift for all sandbox content

# ---------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------

def fp(v, n):
    for p in v or []:
        if isinstance(p, dict) and p.get('Name') == n:
            return p
    return None


def get_rowname(prop):
    if not prop:
        return None
    v = prop.get('Value')
    if isinstance(v, list):
        for it in v:
            if isinstance(it, dict) and it.get('Name') == 'RowName':
                return it.get('Value', '')
    return None


def set_rowname(prop, new):
    v = prop.get('Value')
    if isinstance(v, list):
        for it in v:
            if isinstance(it, dict) and it.get('Name') == 'RowName':
                it['Value'] = new
                return True
    return False


def get_intvec_z(prop):
    if not prop:
        return None
    v = prop.get('Value')
    if isinstance(v, list) and v:
        inner = v[0]
        if isinstance(inner, dict) and isinstance(inner.get('Value'), dict):
            return inner['Value'].get('Z')
    return None


def add_intvec_z(prop, delta):
    v = prop.get('Value')
    if isinstance(v, list) and v:
        inner = v[0]
        if isinstance(inner, dict) and isinstance(inner.get('Value'), dict):
            d = inner['Value']
            d['Z'] = (d.get('Z', 0) or 0) + delta
            return True
    return False


def zstate(r):
    p = fp(r.get('Value', []), 'EnabledState')
    return str(p.get('Value', '')).split('::')[-1] if p else None


def zoneset(r):
    p = fp(r.get('Value', []), 'ZoneSet')
    if not p:
        return None
    v = p.get('Value', '')
    return v.split('::')[-1] if isinstance(v, str) else None


def set_scalar(r, key, val):
    p = fp(r['Value'], key)
    if p is not None:
        p['Value'] = val
        return True
    return False


def add_to_namemap(d, names):
    nm = d.setdefault('NameMap', [])
    present = set(nm)
    added = []
    for n in names:
        if isinstance(n, str) and n and n != 'None' and n not in present:
            nm.append(n)
            present.add(n)
            added.append(n)
    n_now = len(nm)
    d['NamesReferencedFromExportDataCount'] = n_now
    gens = d.get('Generations') or []
    if gens and isinstance(gens[0], dict):
        gens[0]['NameCount'] = n_now
    return added


# ---------------------------------------------------------------------
# Transforms
# ---------------------------------------------------------------------

def transform_chapters():
    p = HERE / 'DT_Moria_Chapters.json'
    d = json.loads(p.read_text(encoding='utf-8'))
    rows = d['Exports'][0]['Table']['Data']
    by_name = {r['Name']: r for r in rows}

    # Step 1: rename pristine chapter-5..8 → chapter-14..11
    print('  --- chapter renames ---')
    for old, new in RENAME.items():
        if old not in by_name:
            print(f'    ! pristine {old} not found, skipping rename')
            continue
        if new in by_name:
            print(f'    ! target {new} already exists, skipping rename')
            continue
        r = by_name.pop(old)
        r['Name'] = new
        by_name[new] = r
        print(f'    {old} -> {new}')

    # Step 2: apply Z spec to every chapter we know about (including renamed)
    template_row = None
    for r in rows:
        if r['Name'] == 'SandboxSmall-chapter-1':
            template_row = r; break
    if template_row is None:
        raise RuntimeError('Cannot find SandboxSmall-chapter-1 as a template for new rows')

    print('  --- chapter Z-band updates ---')
    for name, layer, mn, mx, pz, esl in NEW_CHAPTER_SPEC:
        if name in by_name:
            r = by_name[name]
            old_layer = fp(r['Value'], 'Layer').get('Value') if fp(r['Value'], 'Layer') else None
            old_mn = fp(r['Value'], 'MinZ').get('Value') if fp(r['Value'], 'MinZ') else None
            old_mx = fp(r['Value'], 'MaxZ').get('Value') if fp(r['Value'], 'MaxZ') else None
            old_pz = fp(r['Value'], 'PrimeZ').get('Value') if fp(r['Value'], 'PrimeZ') else None
            set_scalar(r, 'Layer', layer)
            set_scalar(r, 'MinZ', mn)
            set_scalar(r, 'MaxZ', mx)
            set_scalar(r, 'PrimeZ', pz)
            esp = fp(r['Value'], 'EnemyScalingLevel')
            if esp is not None:
                esp['Value'] = esl
            tag = ' (existing)' if old_mn is not None else ''
            print(f'    {name:<32s}  Layer={layer:+d}  Z={mn}..{mx}  PrimeZ={pz}{tag}')
        else:
            # NEW row — clone template + overwrite identifying fields
            r = copy.deepcopy(template_row)
            r['Name'] = name
            set_scalar(r, 'Layer', layer)
            set_scalar(r, 'MinZ', mn)
            set_scalar(r, 'MaxZ', mx)
            set_scalar(r, 'PrimeZ', pz)
            esp = fp(r['Value'], 'EnemyScalingLevel')
            if esp is not None:
                esp['Value'] = esl
            # Force EnabledState::Live
            es = fp(r['Value'], 'EnabledState')
            if es is not None:
                es['Value'] = 'ERowEnabledState::Live'
            rows.append(r)
            by_name[name] = r
            print(f'    {name:<32s}  Layer={layer:+d}  Z={mn}..{mx}  PrimeZ={pz}  ** NEW (Live) **')

    # Step 3: update NameMap with all new chapter names
    new_names = [name for name, *_ in NEW_CHAPTER_SPEC]
    added = add_to_namemap(d, new_names)
    print(f'  NameMap: appended {len(added)} new chapter names; total now {len(d["NameMap"])}')

    p.write_text(json.dumps(d, indent=2), encoding='utf-8')
    return rows


def transform_zones():
    p = HERE / 'DT_Moria_Zones.json'
    d = json.loads(p.read_text(encoding='utf-8'))
    rows = d['Exports'][0]['Table']['Data']

    shifted = 0
    skipped_zero = 0
    skipped_nonsandbox = 0
    chapter_retargets = 0
    addchap_retargets = 0

    for r in rows:
        zs = zoneset(r)
        if zs != 'SandboxSmall':
            skipped_nonsandbox += 1
            continue
        if zstate(r) == 'Disabled':
            # Still retarget chapter refs even on disabled rows so NameMap
            # is internally clean
            pass

        # Chapter retarget
        chap_prop = fp(r['Value'], 'Chapter')
        if chap_prop:
            cur_chap = get_rowname(chap_prop)
            if cur_chap in RENAME:
                set_rowname(chap_prop, RENAME[cur_chap])
                chapter_retargets += 1

        # AdditionalChapters retarget
        ac = fp(r['Value'], 'AdditionalChapters')
        if ac:
            for it in (ac.get('Value') or []):
                inner = it.get('Value') if isinstance(it, dict) else None
                if isinstance(inner, list):
                    for sub in inner:
                        if isinstance(sub, dict) and sub.get('Name') == 'RowName':
                            v = sub.get('Value', '')
                            if v in RENAME:
                                sub['Value'] = RENAME[v]
                                addchap_retargets += 1

        # Position.Z shift (skip if all zeros — generator-placed sentinel)
        pos = fp(r['Value'], 'Position')
        z = get_intvec_z(pos)
        if z is None:
            continue
        # Only shift if Z is in pristine sandbox range (1..20) and non-zero
        if z == 0:
            skipped_zero += 1
            continue
        # Sanity: pristine SandboxSmall zone Z values are all in 1..20
        if 1 <= z <= 20:
            add_intvec_z(pos, Z_SHIFT)
            shifted += 1

    # Re-add new chapter names in NameMap so RowHandle refs resolve
    new_names = [name for name, *_ in NEW_CHAPTER_SPEC]
    added = add_to_namemap(d, new_names)
    print(f'  Zones: SandboxSmall zones shifted Position.Z +{Z_SHIFT}: {shifted}')
    print(f'         skipped (Pos=0,0,0): {skipped_zero}')
    print(f'         skipped (non-SandboxSmall ZoneSet): {skipped_nonsandbox}')
    print(f'         chapter retargets: {chapter_retargets}')
    print(f'         additional-chapter retargets: {addchap_retargets}')
    print(f'         NameMap: appended {len(added)} entries; total {len(d["NameMap"])}')

    p.write_text(json.dumps(d, indent=2), encoding='utf-8')


def transform_landmarks(zones_rows):
    p = HERE / 'DT_Moria_Landmarks.json'
    d = json.loads(p.read_text(encoding='utf-8'))
    rows = d['Exports'][0]['Table']['Data']

    # Build landmark host index: lname -> set of (zonename, zoneset)
    hosts = {}
    for zr in zones_rows:
        zn = zr['Name']
        zs = zoneset(zr)
        lh = fp(zr['Value'], 'LandmarkHandles')
        if not lh:
            continue
        for e in (lh.get('Value') or []):
            inner = e.get('Value') if isinstance(e, dict) else None
            if not isinstance(inner, list):
                continue
            for sub in inner:
                if isinstance(sub, dict) and sub.get('Name') == 'Landmark':
                    for it in (sub.get('Value') or []):
                        if isinstance(it, dict) and it.get('Name') == 'RowName':
                            lname = it.get('Value', '')
                            if lname:
                                hosts.setdefault(lname, set()).add((zn, zs))

    shifted = 0
    skipped_mixed = 0
    skipped_no_host = 0
    skipped_zero = 0
    skipped_nonsandbox = 0

    for r in rows:
        lname = r['Name']
        host_sets = {zs for _, zs in hosts.get(lname, set())}
        if not host_sets:
            skipped_no_host += 1
            continue
        if 'SandboxSmall' not in host_sets:
            skipped_nonsandbox += 1
            continue
        if host_sets - {'SandboxSmall'}:
            # Mixed host (SandboxSmall AND others) — skip to preserve campaign coords
            skipped_mixed += 1
            continue

        # Pure SandboxSmall landmark — shift BasePosition.Z
        bp = fp(r['Value'], 'BasePosition')
        z = get_intvec_z(bp)
        if z is None or z == 0:
            skipped_zero += 1
            continue
        if 1 <= z <= 20:
            add_intvec_z(bp, Z_SHIFT)
            shifted += 1

    print(f'  Landmarks: shifted BasePosition.Z +{Z_SHIFT}: {shifted}')
    print(f'             skipped (no host zone): {skipped_no_host}')
    print(f'             skipped (host not SandboxSmall): {skipped_nonsandbox}')
    print(f'             skipped (mixed-host campaign+sandbox): {skipped_mixed}')
    print(f'             skipped (BasePosition.Z=0 or out of range): {skipped_zero}')

    p.write_text(json.dumps(d, indent=2), encoding='utf-8')


def transform_layoutconnections():
    p = HERE / 'DT_Moria_LayoutConnections.json'
    d = json.loads(p.read_text(encoding='utf-8'))
    rows = d['Exports'][0]['Table']['Data']

    retargets = 0
    for r in rows:
        # Look for any chapter-RowHandle-like field; LayoutConnections typically
        # reference ZONES and LANDMARKS (not chapters), but be defensive.
        for prop in r.get('Value', []):
            if not isinstance(prop, dict): continue
            v = prop.get('Value')
            if isinstance(v, list):
                for it in v:
                    if isinstance(it, dict) and it.get('Name') == 'RowName':
                        if it.get('Value') in RENAME:
                            it['Value'] = RENAME[it['Value']]
                            retargets += 1
    # NameMap addition (just in case)
    new_names = list(RENAME.values())
    added = add_to_namemap(d, new_names)
    print(f'  LayoutConnections: chapter retargets: {retargets}; NameMap added {len(added)}')
    p.write_text(json.dumps(d, indent=2), encoding='utf-8')


def main():
    print('=== Snapshot before changes ===')
    BACKUP = HERE / 'backups' / 'before 14-chapter expansion'
    BACKUP.mkdir(parents=True, exist_ok=True)
    for src in sorted(HERE.glob('*.json')):
        if src.name.endswith('.original.json'): continue
        if not src.name.startswith(('DT_', 'BC_', 'World')): continue
        shutil.copy2(src, BACKUP / src.name)
    print(f'  Saved working state to backups/before 14-chapter expansion/\n')

    print('=== Phase 1: DT_Moria_Chapters ===')
    chapter_rows = transform_chapters()
    print()

    print('=== Phase 2: DT_Moria_Zones ===')
    zones_doc = json.loads((HERE / 'DT_Moria_Zones.json').read_text(encoding='utf-8'))
    zones_rows = zones_doc['Exports'][0]['Table']['Data']
    transform_zones()
    print()

    print('=== Phase 3: DT_Moria_Landmarks ===')
    # Re-load zones since transform_zones changed them
    zones_doc = json.loads((HERE / 'DT_Moria_Zones.json').read_text(encoding='utf-8'))
    zones_rows = zones_doc['Exports'][0]['Table']['Data']
    transform_landmarks(zones_rows)
    print()

    print('=== Phase 4: DT_Moria_LayoutConnections ===')
    transform_layoutconnections()
    print()

    print('=== DONE ===')


if __name__ == '__main__':
    main()
