"""Expand SandboxSmall from 10 chapters to 12 (one new level above + one
new deep below). All NEW chapters are h=3.

Rotation numbering after expansion:
  chapter-1  = Layer  0  (ground, existing)
  chapter-2  = Layer +1
  chapter-3  = Layer +2
  chapter-4  = Layer +3
  chapter-5  = Layer +4
  chapter-6  = Layer +5  (Lv-6, NEW top)
  chapter-7  = Layer -6  (D-6, NEW absolute bottom)
  chapter-8  = Layer -5  (D-5, RENAMED from chap-6)
  chapter-9  = Layer -4  (D-4, RENAMED from chap-7)
  chapter-10 = Layer -3  (D-3, RENAMED from chap-8)
  chapter-11 = Layer -2  (D-2, RENAMED from chap-9)
  chapter-12 = Layer -1  (D-1, RENAMED from chap-10)

Z-band stack (32 cells):
  chap-6   +5  Z=30..32  PrimeZ=31  NEW
  chap-5   +4  Z=27..29  PrimeZ=28
  chap-4   +3  Z=24..26  PrimeZ=25
  chap-3   +2  Z=20..23  PrimeZ=21
  chap-2   +1  Z=19..19  PrimeZ=19
  chap-1    0  Z=17..18  PrimeZ=17  (ground)
  ─────────
  chap-12  -1  Z=15..16  PrimeZ=15
  chap-11  -2  Z=13..14  PrimeZ=13
  chap-10  -3  Z=10..12  PrimeZ=11
  chap-9   -4  Z=7..9    PrimeZ=8
  chap-8   -5  Z=4..6    PrimeZ=5
  chap-7   -6  Z=1..3    PrimeZ=2   NEW (absolute bottom)

Z shift: +3 (one new chapter h=3 added below current D-5)
"""
import copy
import json
import shutil
from pathlib import Path

HERE = Path(__file__).parent

NEW_CHAPTER_SPEC = [
    ('SandboxSmall-chapter-1',   0, 17, 18, 17, 0),
    ('SandboxSmall-chapter-2',   1, 19, 19, 19, 1),
    ('SandboxSmall-chapter-3',   2, 20, 23, 21, 2),
    ('SandboxSmall-chapter-4',   3, 24, 26, 25, 3),
    ('SandboxSmall-chapter-5',   4, 27, 29, 28, 4),
    ('SandboxSmall-chapter-6',   5, 30, 32, 31, 5),  # NEW Lv-6
    ('SandboxSmall-chapter-7',  -6,  1,  3,  2, 6),  # NEW D-6 absolute bottom
    ('SandboxSmall-chapter-8',  -5,  4,  6,  5, 5),  # was chap-6 (D-5)
    ('SandboxSmall-chapter-9',  -4,  7,  9,  8, 4),  # was chap-7 (D-4)
    ('SandboxSmall-chapter-10', -3, 10, 12, 11, 3),  # was chap-8 (D-3)
    ('SandboxSmall-chapter-11', -2, 13, 14, 13, 2),  # was chap-9 (D-2)
    ('SandboxSmall-chapter-12', -1, 15, 16, 15, 1),  # was chap-10 (D-1)
]

# Renames done in REVERSE order to avoid conflicts (chap-10 freed first)
RENAME_PLAN = [
    ('SandboxSmall-chapter-10', 'SandboxSmall-chapter-12'),
    ('SandboxSmall-chapter-9',  'SandboxSmall-chapter-11'),
    ('SandboxSmall-chapter-8',  'SandboxSmall-chapter-10'),
    ('SandboxSmall-chapter-7',  'SandboxSmall-chapter-9'),
    ('SandboxSmall-chapter-6',  'SandboxSmall-chapter-8'),
]

# Effective mapping for zone retargets
RENAME = {
    'SandboxSmall-chapter-6':  'SandboxSmall-chapter-8',
    'SandboxSmall-chapter-7':  'SandboxSmall-chapter-9',
    'SandboxSmall-chapter-8':  'SandboxSmall-chapter-10',
    'SandboxSmall-chapter-9':  'SandboxSmall-chapter-11',
    'SandboxSmall-chapter-10': 'SandboxSmall-chapter-12',
}

Z_SHIFT = 3


def fp(v, n):
    for p in v or []:
        if isinstance(p, dict) and p.get('Name') == n: return p
    return None
def get_rowname(prop):
    if not prop: return None
    v = prop.get('Value')
    if isinstance(v, list):
        for it in v:
            if isinstance(it, dict) and it.get('Name')=='RowName': return it.get('Value','')
    return None
def set_rowname(prop, new):
    v = prop.get('Value')
    if isinstance(v, list):
        for it in v:
            if isinstance(it, dict) and it.get('Name')=='RowName':
                it['Value'] = new; return True
    return False
def get_intvec_z(prop):
    if not prop: return None
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
    if not p: return None
    return str(p.get('Value','')).split('::')[-1]
def set_scalar(r, key, val):
    p = fp(r['Value'], key)
    if p is not None: p['Value'] = val
def add_to_namemap(d, names):
    nm = d.setdefault('NameMap', [])
    present = set(nm); added = []
    for n in names:
        if isinstance(n, str) and n and n != 'None' and n not in present:
            nm.append(n); present.add(n); added.append(n)
    n_now = len(nm)
    d['NamesReferencedFromExportDataCount'] = n_now
    gens = d.get('Generations') or []
    if gens and isinstance(gens[0], dict): gens[0]['NameCount'] = n_now
    return added


def transform_chapters():
    p = HERE / 'DT_Moria_Chapters.json'
    d = json.loads(p.read_text(encoding='utf-8'))
    rows = d['Exports'][0]['Table']['Data']
    by_name = {r['Name']: r for r in rows}

    print('  --- chapter renames (reverse-order to avoid conflicts) ---')
    for old, new in RENAME_PLAN:
        if old not in by_name:
            print(f'    ! {old} not found, skipping'); continue
        if new in by_name:
            print(f'    ! {new} already exists; aborting'); raise SystemExit(1)
        r = by_name.pop(old)
        r['Name'] = new
        by_name[new] = r
        print(f'    {old} -> {new}')

    template = next(r for r in rows if r['Name'] == 'SandboxSmall-chapter-1')
    print('\n  --- chapter Z-band updates ---')
    for name, layer, mn, mx, pz, esl in NEW_CHAPTER_SPEC:
        if name in by_name:
            r = by_name[name]; tag = '(existing data, new Z)'
        else:
            r = copy.deepcopy(template)
            r['Name'] = name
            rows.append(r); by_name[name] = r
            tag = '** NEW **'
        set_scalar(r, 'Layer', layer)
        set_scalar(r, 'MinZ', mn)
        set_scalar(r, 'MaxZ', mx)
        set_scalar(r, 'PrimeZ', pz)
        esp = fp(r['Value'], 'EnemyScalingLevel')
        if esp is not None: esp['Value'] = esl
        es = fp(r['Value'], 'EnabledState')
        if es is not None: es['Value'] = 'ERowEnabledState::Live'
        print(f'    {name:<32s}  Layer={layer:+d}  Z={mn}..{mx}  PrimeZ={pz}  {tag}')

    new_names = [n for n, *_ in NEW_CHAPTER_SPEC]
    added = add_to_namemap(d, new_names)
    print(f'  NameMap appended {len(added)}; total {len(d["NameMap"])}')
    p.write_text(json.dumps(d, indent=2), encoding='utf-8')


def transform_zones():
    p = HERE / 'DT_Moria_Zones.json'
    d = json.loads(p.read_text(encoding='utf-8'))
    rows = d['Exports'][0]['Table']['Data']
    shifted = 0; skipped_zero = 0; skipped_oor = 0; skipped_nonsbx = 0
    chap_retargets = 0; addchap_retargets = 0
    samples = []

    # The pristine sandbox Z range was 1..20. After +3 (10-chap), it became 1..23.
    # After this +3 shift it'll be 1..26. Use a generous shift range for any
    # currently-pinned Z value we touch.
    SHIFT_RANGE = (1, 30)

    for r in rows:
        if zoneset(r) != 'SandboxSmall':
            skipped_nonsbx += 1; continue
        chap_prop = fp(r['Value'], 'Chapter')
        if chap_prop:
            cur = get_rowname(chap_prop)
            if cur in RENAME:
                set_rowname(chap_prop, RENAME[cur]); chap_retargets += 1
        ac = fp(r['Value'], 'AdditionalChapters')
        if ac:
            for it in (ac.get('Value') or []):
                inner = it.get('Value') if isinstance(it, dict) else None
                if isinstance(inner, list):
                    for sub in inner:
                        if isinstance(sub, dict) and sub.get('Name') == 'RowName':
                            v = sub.get('Value', '')
                            if v in RENAME:
                                sub['Value'] = RENAME[v]; addchap_retargets += 1
        pos = fp(r['Value'], 'Position')
        z = get_intvec_z(pos)
        if z is None: continue
        if z == 0: skipped_zero += 1; continue
        if SHIFT_RANGE[0] <= z <= SHIFT_RANGE[1]:
            add_intvec_z(pos, Z_SHIFT)
            shifted += 1
            if len(samples) < 6:
                samples.append((r['Name'], z, z + Z_SHIFT))
        else:
            skipped_oor += 1

    new_names = [n for n, *_ in NEW_CHAPTER_SPEC]
    added = add_to_namemap(d, new_names)
    print(f'  Zones: shifted Position.Z +{Z_SHIFT}: {shifted}')
    print(f'         skipped Pos=0,0,0: {skipped_zero}, OOR: {skipped_oor}, non-Sandbox: {skipped_nonsbx}')
    print(f'         chapter retargets: {chap_retargets}, additional-chapter retargets: {addchap_retargets}')
    print(f'         NameMap appended {len(added)}; total {len(d["NameMap"])}')
    print(f'  Sample shifts:')
    for n, o, nw in samples: print(f'    {n:<42s}  Z {o:>2} -> {nw}')
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
                        if isinstance(it, dict) and it.get('Name')=='RowName':
                            lname = it.get('Value', '')
                            if lname:
                                hosts.setdefault(lname, set()).add((zr['Name'], zs))

    shifted = 0; skipped_mixed = 0; skipped_no_host = 0; skipped_zero = 0; skipped_nonsbx = 0
    samples = []
    for r in rows:
        lname = r['Name']
        host_sets = {zs for _, zs in hosts.get(lname, set())}
        if not host_sets: skipped_no_host += 1; continue
        if 'SandboxSmall' not in host_sets: skipped_nonsbx += 1; continue
        if host_sets - {'SandboxSmall'}: skipped_mixed += 1; continue
        bp = fp(r['Value'], 'BasePosition')
        z = get_intvec_z(bp)
        if z is None or z == 0: skipped_zero += 1; continue
        if 1 <= z <= 30:
            add_intvec_z(bp, Z_SHIFT); shifted += 1
            if len(samples) < 6: samples.append((lname, z, z + Z_SHIFT))

    print(f'  Landmarks: BasePosition.Z shifted +{Z_SHIFT}: {shifted}')
    print(f'             skipped no-host: {skipped_no_host}, non-sbx: {skipped_nonsbx}, mixed: {skipped_mixed}, zero/OOR: {skipped_zero}')
    print(f'  Sample shifts:')
    for n, o, nw in samples: print(f'    {n:<42s}  Z {o:>2} -> {nw}')
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
                    if isinstance(it, dict) and it.get('Name')=='RowName':
                        if it.get('Value') in RENAME:
                            it['Value'] = RENAME[it['Value']]; retargets += 1
    new_names = list(RENAME.values())
    added = add_to_namemap(d, new_names)
    print(f'  LayoutConnections: retargets={retargets}; NameMap appended {len(added)}')
    p.write_text(json.dumps(d, indent=2), encoding='utf-8')


def main():
    print('=== Snapshot before changes ===')
    BACKUP = HERE / 'backups' / 'before 12-chapter expansion'
    BACKUP.mkdir(parents=True, exist_ok=True)
    for src in sorted(HERE.glob('*.json')):
        if src.name.endswith('.original.json'): continue
        if not src.name.startswith(('DT_', 'BC_', 'World')): continue
        shutil.copy2(src, BACKUP / src.name)
    print('  Saved to backups/before 12-chapter expansion/\n')

    print('=== Phase 1: Chapters ===')
    transform_chapters()
    print()
    print('=== Phase 2: Zones ===')
    transform_zones()
    print()
    print('=== Phase 3: Landmarks ===')
    zd = json.loads((HERE / 'DT_Moria_Zones.json').read_text(encoding='utf-8'))
    transform_landmarks(zd['Exports'][0]['Table']['Data'])
    print()
    print('=== Phase 4: LayoutConnections ===')
    transform_layoutconnections()
    print()
    print('=== DONE ===')


if __name__ == '__main__':
    main()
