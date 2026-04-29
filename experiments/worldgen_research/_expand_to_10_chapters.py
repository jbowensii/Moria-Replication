"""Expand SandboxSmall from 8 chapters to 10 (one new level above + one
new deep below). All NEW chapters are h=3.

Chapter numbering (rotation convention):
  chapter-1   = Layer  0  (ground, existing)
  chapter-2   = Layer +1  (Lv-2, existing)
  chapter-3   = Layer +2  (Lv-3, existing)
  chapter-4   = Layer +3  (Lv-4, existing)
  chapter-5   = Layer +4  (Lv-5, NEW top)
  chapter-6   = Layer -5  (Deep 5, NEW absolute bottom)
  chapter-7   = Layer -4  (RENAMED from pristine chapter-8 / Deep 4)
  chapter-8   = Layer -3  (RENAMED from pristine chapter-7 / Deep 3)
  chapter-9   = Layer -2  (RENAMED from pristine chapter-6 / Deep 2)
  chapter-10  = Layer -1  (RENAMED from pristine chapter-5 / Deep 1)

NOTE: pristine chapter-7 ↔ chapter-8 swap. Use temp name to handle safely.

Z-band stack (26 cells total):
  chapter-5   +4   Z=24..26  PrimeZ=25
  chapter-4   +3   Z=21..23  PrimeZ=22
  chapter-3   +2   Z=17..20  PrimeZ=18
  chapter-2   +1   Z=16..16  PrimeZ=16
  chapter-1    0   Z=14..15  PrimeZ=14   (ground)
  ─────────────────────────────────────
  chapter-10  -1   Z=12..13  PrimeZ=12
  chapter-9   -2   Z=10..11  PrimeZ=10
  chapter-8   -3   Z=7..9    PrimeZ=8
  chapter-7   -4   Z=4..6    PrimeZ=5
  chapter-6   -5   Z=1..3    PrimeZ=2    (absolute bottom)

Z shift: +3 (one new chapter h=3 added below pristine D-4)
"""
import copy
import json
import shutil
from pathlib import Path

HERE = Path(__file__).parent

NEW_CHAPTER_SPEC = [
    ('SandboxSmall-chapter-1',   0, 14, 15, 14, 0),
    ('SandboxSmall-chapter-2',   1, 16, 16, 16, 1),
    ('SandboxSmall-chapter-3',   2, 17, 20, 18, 2),
    ('SandboxSmall-chapter-4',   3, 21, 23, 22, 3),
    ('SandboxSmall-chapter-5',   4, 24, 26, 25, 4),  # NEW Lv-5
    ('SandboxSmall-chapter-6',  -5,  1,  3,  2, 5),  # NEW D-5 absolute bottom
    ('SandboxSmall-chapter-7',  -4,  4,  6,  5, 4),  # was pristine chapter-8
    ('SandboxSmall-chapter-8',  -3,  7,  9,  8, 3),  # was pristine chapter-7
    ('SandboxSmall-chapter-9',  -2, 10, 11, 10, 2),  # was pristine chapter-6
    ('SandboxSmall-chapter-10', -1, 12, 13, 12, 1),  # was pristine chapter-5
]

# 4 renames including the 7↔8 swap. Order matters: do the conflict-free renames
# first, then resolve the 7↔8 swap with a temp.
RENAME_PLAN = [
    ('SandboxSmall-chapter-5',  'SandboxSmall-chapter-10'),
    ('SandboxSmall-chapter-6',  'SandboxSmall-chapter-9'),
    # 7↔8 swap via temp
    ('SandboxSmall-chapter-7',  '__TEMP_chapter_swap__'),
    ('SandboxSmall-chapter-8',  'SandboxSmall-chapter-7'),
    ('__TEMP_chapter_swap__',   'SandboxSmall-chapter-8'),
]

# Effective mapping (final destination, used for zone retargets)
RENAME = {
    'SandboxSmall-chapter-5':  'SandboxSmall-chapter-10',
    'SandboxSmall-chapter-6':  'SandboxSmall-chapter-9',
    'SandboxSmall-chapter-7':  'SandboxSmall-chapter-8',
    'SandboxSmall-chapter-8':  'SandboxSmall-chapter-7',
}

Z_SHIFT = 3


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


def add_to_namemap(d, names):
    nm = d.setdefault('NameMap', [])
    present = set(nm)
    added = []
    for n in names:
        if isinstance(n, str) and n and n != 'None' and n not in present:
            nm.append(n); present.add(n); added.append(n)
    n_now = len(nm)
    d['NamesReferencedFromExportDataCount'] = n_now
    gens = d.get('Generations') or []
    if gens and isinstance(gens[0], dict):
        gens[0]['NameCount'] = n_now
    return added


def transform_chapters():
    p = HERE / 'DT_Moria_Chapters.json'
    d = json.loads(p.read_text(encoding='utf-8'))
    rows = d['Exports'][0]['Table']['Data']
    by_name = {r['Name']: r for r in rows}

    print('  --- chapter renames (including 7<->8 swap) ---')
    for old, new in RENAME_PLAN:
        if old not in by_name:
            print(f'    ! {old} not found, skipping'); continue
        if new in by_name:
            print(f'    ! {new} already exists, skipping rename of {old}'); continue
        r = by_name.pop(old)
        r['Name'] = new
        by_name[new] = r
        print(f'    {old} -> {new}')

    template_row = None
    for r in rows:
        if r['Name'] == 'SandboxSmall-chapter-1':
            template_row = r; break

    print('\n  --- chapter Z-band updates ---')
    for name, layer, mn, mx, pz, esl in NEW_CHAPTER_SPEC:
        if name in by_name:
            r = by_name[name]
            tag = '(existing data, new Z)'
        else:
            r = copy.deepcopy(template_row)
            r['Name'] = name
            rows.append(r)
            by_name[name] = r
            tag = '** NEW **'
        set_scalar(r, 'Layer', layer)
        set_scalar(r, 'MinZ', mn)
        set_scalar(r, 'MaxZ', mx)
        set_scalar(r, 'PrimeZ', pz)
        esp = fp(r['Value'], 'EnemyScalingLevel')
        if esp is not None:
            esp['Value'] = esl
        es = fp(r['Value'], 'EnabledState')
        if es is not None:
            es['Value'] = 'ERowEnabledState::Live'
        print(f'    {name:<32s}  Layer={layer:+d}  Z={mn}..{mx}  PrimeZ={pz}  {tag}')

    new_names = [name for name, *_ in NEW_CHAPTER_SPEC]
    added = add_to_namemap(d, new_names)
    print(f'  NameMap: appended {len(added)}; total {len(d["NameMap"])}')

    p.write_text(json.dumps(d, indent=2), encoding='utf-8')


def transform_zones():
    p = HERE / 'DT_Moria_Zones.json'
    d = json.loads(p.read_text(encoding='utf-8'))
    rows = d['Exports'][0]['Table']['Data']

    shifted = 0
    skipped_zero = 0
    skipped_oor = 0
    skipped_nonsandbox = 0
    chapter_retargets = 0
    addchap_retargets = 0
    sample_shifts = []

    for r in rows:
        zs = zoneset(r)
        if zs != 'SandboxSmall':
            skipped_nonsandbox += 1
            continue

        # Chapter retarget
        chap_prop = fp(r['Value'], 'Chapter')
        if chap_prop:
            cur = get_rowname(chap_prop)
            if cur in RENAME:
                set_rowname(chap_prop, RENAME[cur])
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

        # Position.Z shift
        pos = fp(r['Value'], 'Position')
        z = get_intvec_z(pos)
        if z is None: continue
        if z == 0:
            skipped_zero += 1; continue
        if 1 <= z <= 20:
            add_intvec_z(pos, Z_SHIFT)
            shifted += 1
            if len(sample_shifts) < 6:
                sample_shifts.append((r['Name'], z, z + Z_SHIFT))
        else:
            skipped_oor += 1

    new_names = [name for name, *_ in NEW_CHAPTER_SPEC]
    added = add_to_namemap(d, new_names)
    print(f'  Zones: Position.Z shifted by +{Z_SHIFT}: {shifted}')
    print(f'         skipped (Pos=0,0,0): {skipped_zero}')
    print(f'         skipped (Z out of pristine range): {skipped_oor}')
    print(f'         skipped (non-SandboxSmall ZoneSet): {skipped_nonsandbox}')
    print(f'         chapter retargets: {chapter_retargets}')
    print(f'         additional-chapter retargets: {addchap_retargets}')
    print(f'         NameMap appended {len(added)}; total {len(d["NameMap"])}')
    print(f'  Sample shifts (zone: oldZ -> newZ):')
    for n, o, nw in sample_shifts:
        print(f'    {n:<42s}  Z {o:>2} -> {nw}')
    p.write_text(json.dumps(d, indent=2), encoding='utf-8')


def transform_landmarks(zones_rows):
    p = HERE / 'DT_Moria_Landmarks.json'
    d = json.loads(p.read_text(encoding='utf-8'))
    rows = d['Exports'][0]['Table']['Data']

    hosts = {}
    for zr in zones_rows:
        zs = zoneset(zr)
        lh = fp(zr['Value'], 'LandmarkHandles')
        if not lh: continue
        for e in (lh.get('Value') or []):
            inner = e.get('Value') if isinstance(e, dict) else None
            if not isinstance(inner, list): continue
            for sub in inner:
                if isinstance(sub, dict) and sub.get('Name') == 'Landmark':
                    for it in (sub.get('Value') or []):
                        if isinstance(it, dict) and it.get('Name') == 'RowName':
                            lname = it.get('Value', '')
                            if lname:
                                hosts.setdefault(lname, set()).add((zr['Name'], zs))

    shifted = 0
    skipped_mixed = 0
    skipped_no_host = 0
    skipped_zero = 0
    skipped_nonsandbox = 0
    sample_shifts = []

    for r in rows:
        lname = r['Name']
        host_sets = {zs for _, zs in hosts.get(lname, set())}
        if not host_sets:
            skipped_no_host += 1; continue
        if 'SandboxSmall' not in host_sets:
            skipped_nonsandbox += 1; continue
        if host_sets - {'SandboxSmall'}:
            skipped_mixed += 1; continue

        bp = fp(r['Value'], 'BasePosition')
        z = get_intvec_z(bp)
        if z is None or z == 0:
            skipped_zero += 1; continue
        if 1 <= z <= 20:
            add_intvec_z(bp, Z_SHIFT)
            shifted += 1
            if len(sample_shifts) < 6:
                sample_shifts.append((lname, z, z + Z_SHIFT))

    print(f'  Landmarks: BasePosition.Z shifted by +{Z_SHIFT}: {shifted}')
    print(f'             skipped (no host): {skipped_no_host}, non-sandbox: {skipped_nonsandbox}')
    print(f'             skipped (mixed campaign+sandbox): {skipped_mixed}')
    print(f'             skipped (BasePos.Z=0 or out of range): {skipped_zero}')
    print(f'  Sample shifts (landmark: oldZ -> newZ):')
    for n, o, nw in sample_shifts:
        print(f'    {n:<42s}  Z {o:>2} -> {nw}')
    p.write_text(json.dumps(d, indent=2), encoding='utf-8')


def transform_layoutconnections():
    p = HERE / 'DT_Moria_LayoutConnections.json'
    d = json.loads(p.read_text(encoding='utf-8'))
    retargets = 0
    for r in d['Exports'][0]['Table']['Data']:
        for prop in r.get('Value', []):
            if not isinstance(prop, dict): continue
            v = prop.get('Value')
            if isinstance(v, list):
                for it in v:
                    if isinstance(it, dict) and it.get('Name') == 'RowName':
                        if it.get('Value') in RENAME:
                            it['Value'] = RENAME[it['Value']]
                            retargets += 1
    new_names = list(RENAME.values())
    added = add_to_namemap(d, new_names)
    print(f'  LayoutConnections: chapter retargets={retargets}; NameMap appended {len(added)}')
    p.write_text(json.dumps(d, indent=2), encoding='utf-8')


def main():
    print('=== Snapshot before changes ===')
    BACKUP = HERE / 'backups' / 'before 10-chapter expansion'
    BACKUP.mkdir(parents=True, exist_ok=True)
    for src in sorted(HERE.glob('*.json')):
        if src.name.endswith('.original.json'): continue
        if not src.name.startswith(('DT_', 'BC_', 'World')): continue
        shutil.copy2(src, BACKUP / src.name)
    print(f'  Saved to backups/before 10-chapter expansion/\n')

    print('=== Phase 1: DT_Moria_Chapters ===')
    transform_chapters()
    print()
    print('=== Phase 2: DT_Moria_Zones ===')
    transform_zones()
    print()
    print('=== Phase 3: DT_Moria_Landmarks ===')
    zones_doc = json.loads((HERE / 'DT_Moria_Zones.json').read_text(encoding='utf-8'))
    transform_landmarks(zones_doc['Exports'][0]['Table']['Data'])
    print()
    print('=== Phase 4: DT_Moria_LayoutConnections ===')
    transform_layoutconnections()
    print()
    print('=== DONE ===')


if __name__ == '__main__':
    main()
