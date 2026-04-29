"""Add Lv-7 (top) and D-7 (absolute bottom), each h=1.
Stack 28 -> 30 cells. All existing zones shift +1.
"""
import json, shutil, copy
from pathlib import Path

HERE = Path(__file__).parent

NEW_SPEC = [
    ('SandboxSmall-chapter-1',   0, 16, 17, 16, 0),
    ('SandboxSmall-chapter-2',   1, 18, 18, 18, 1),
    ('SandboxSmall-chapter-3',   2, 19, 22, 20, 2),
    ('SandboxSmall-chapter-4',   3, 23, 25, 24, 3),
    ('SandboxSmall-chapter-5',   4, 26, 27, 26, 4),
    ('SandboxSmall-chapter-6',   5, 28, 29, 28, 5),
    ('SandboxSmall-chapter-7',   6, 30, 30, 30, 6),  # NEW Lv-7 h=1
    ('SandboxSmall-chapter-8',  -7,  1,  1,  1, 7),  # NEW D-7 h=1 absolute bottom
    ('SandboxSmall-chapter-9',  -6,  2,  3,  2, 6),
    ('SandboxSmall-chapter-10', -5,  4,  5,  4, 5),
    ('SandboxSmall-chapter-11', -4,  6,  8,  7, 4),
    ('SandboxSmall-chapter-12', -3,  9, 11, 10, 3),
    ('SandboxSmall-chapter-13', -2, 12, 13, 12, 2),
    ('SandboxSmall-chapter-14', -1, 14, 15, 14, 1),
]

RENAME_PLAN = [
    ('SandboxSmall-chapter-12', 'SandboxSmall-chapter-14'),
    ('SandboxSmall-chapter-11', 'SandboxSmall-chapter-13'),
    ('SandboxSmall-chapter-10', 'SandboxSmall-chapter-12'),
    ('SandboxSmall-chapter-9',  'SandboxSmall-chapter-11'),
    ('SandboxSmall-chapter-8',  'SandboxSmall-chapter-10'),
    ('SandboxSmall-chapter-7',  'SandboxSmall-chapter-9'),
]
RENAME = {old: new for old, new in RENAME_PLAN}
Z_SHIFT = 1


def fp(v, n):
    for p in v or []:
        if isinstance(p, dict) and p.get('Name') == n: return p
    return None
def get_rowname(prop):
    if not prop: return None
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
def set_scalar(r, key, val):
    p = fp(r['Value'], key)
    if p is not None: p['Value'] = val
def zoneset(r):
    p = fp(r.get('Value', []), 'ZoneSet')
    if not p: return None
    return str(p.get('Value', '')).split('::')[-1]
def add_to_namemap(d, names):
    nm = d.setdefault('NameMap', [])
    present = set(nm); added = []
    for n in names:
        if isinstance(n, str) and n and n not in present:
            nm.append(n); present.add(n); added.append(n)
    n_now = len(nm)
    d['NamesReferencedFromExportDataCount'] = n_now
    gens = d.get('Generations') or []
    if gens and isinstance(gens[0], dict):
        gens[0]['NameCount'] = n_now
    return added


def main():
    BAK = HERE / 'backups' / 'before 14-chapter add-with-h1-edges'
    BAK.mkdir(parents=True, exist_ok=True)
    for src in sorted(HERE.glob('*.json')):
        if src.name.endswith('.original.json'): continue
        if not src.name.startswith(('DT_', 'BC_', 'World')): continue
        shutil.copy2(src, BAK / src.name)
    print('Snapshot saved to backups/before 14-chapter add-with-h1-edges/\n')

    # Phase 1: Chapters
    ch_path = HERE / 'DT_Moria_Chapters.json'
    ch = json.loads(ch_path.read_text(encoding='utf-8'))
    rows = ch['Exports'][0]['Table']['Data']
    by_name = {r['Name']: r for r in rows}

    print('=== Phase 1: Chapter renames + new rows ===')
    for old, new in RENAME_PLAN:
        if old in by_name and new not in by_name:
            r = by_name.pop(old); r['Name'] = new; by_name[new] = r
            print(f'  rename: {old} -> {new}')
    print()

    template = next(r for r in rows if r['Name'] == 'SandboxSmall-chapter-1')
    for name, layer, mn, mx, pz, esl in NEW_SPEC:
        if name in by_name:
            r = by_name[name]; tag = '(updated)'
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
        print(f'  {name:<32s}  Layer={layer:+d}  Z={mn}..{mx}  h={mx-mn+1}  {tag}')

    new_names = [n for n, *_ in NEW_SPEC]
    add_to_namemap(ch, new_names)
    ch_path.write_text(json.dumps(ch, indent=2), encoding='utf-8')

    # Phase 2: Zones
    z_path = HERE / 'DT_Moria_Zones.json'
    z = json.loads(z_path.read_text(encoding='utf-8'))
    shifted = 0; chap_retargets = 0; addchap_retargets = 0
    for r in z['Exports'][0]['Table']['Data']:
        if zoneset(r) != 'SandboxSmall': continue
        chap_prop = fp(r['Value'], 'Chapter')
        if chap_prop:
            cur = get_rowname(chap_prop)
            if cur in RENAME:
                set_rowname(chap_prop, RENAME[cur])
                chap_retargets += 1
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
        pos = fp(r['Value'], 'Position')
        zv = get_intvec_z(pos)
        if zv is None or zv == 0: continue
        add_intvec_z(pos, Z_SHIFT)
        shifted += 1
    add_to_namemap(z, new_names)
    z_path.write_text(json.dumps(z, indent=2), encoding='utf-8')
    print(f'\n=== Phase 2: Zones ===')
    print(f'  Chapter retargets: {chap_retargets}')
    print(f'  AdditionalChapters retargets: {addchap_retargets}')
    print(f'  Pinned zones shifted Position.Z +{Z_SHIFT}: {shifted}')

    # Phase 3: Landmarks
    lm_path = HERE / 'DT_Moria_Landmarks.json'
    lm = json.loads(lm_path.read_text(encoding='utf-8'))
    hosts = {}
    for zr in z['Exports'][0]['Table']['Data']:
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
                            n = it.get('Value', '')
                            if n: hosts.setdefault(n, set()).add((zr['Name'], zs))
    shifted_lm = 0
    for r in lm['Exports'][0]['Table']['Data']:
        n = r['Name']
        host_zs = {zs for _, zs in hosts.get(n, set())}
        if not host_zs or 'SandboxSmall' not in host_zs: continue
        if host_zs - {'SandboxSmall'}: continue
        bp = fp(r['Value'], 'BasePosition')
        zv = get_intvec_z(bp)
        if zv is None or zv == 0: continue
        add_intvec_z(bp, Z_SHIFT)
        shifted_lm += 1
    lm_path.write_text(json.dumps(lm, indent=2), encoding='utf-8')
    print(f'\n=== Phase 3: Landmarks ===')
    print(f'  Sandbox-only landmarks shifted BasePosition.Z +{Z_SHIFT}: {shifted_lm}')

    # Phase 4: LayoutConnections retargets
    lc_path = HERE / 'DT_Moria_LayoutConnections.json'
    lc = json.loads(lc_path.read_text(encoding='utf-8'))
    lc_retargets = 0
    for r in lc['Exports'][0]['Table']['Data']:
        for prop in r.get('Value', []):
            if not isinstance(prop, dict): continue
            v = prop.get('Value')
            if isinstance(v, list):
                for it in v:
                    if isinstance(it, dict) and it.get('Name') == 'RowName':
                        if it.get('Value') in RENAME:
                            it['Value'] = RENAME[it['Value']]
                            lc_retargets += 1
    add_to_namemap(lc, list(RENAME.values()))
    lc_path.write_text(json.dumps(lc, indent=2), encoding='utf-8')
    print(f'\n=== Phase 4: LayoutConnections ===')
    print(f'  Chapter retargets: {lc_retargets}')

    # Final chart
    print()
    print('=== NEW STACK ===')
    print(f'{"Lv":<5}  {"Chapter":<32s}  {"Layer":>6}  {"h":>3}  {"MinZ":>5}  {"MaxZ":>5}  {"PrimeZ":>7}')
    print('-' * 80)
    for name, layer, mn, mx, pz, esl in sorted(NEW_SPEC, key=lambda x: -x[1]):
        h = mx - mn + 1
        if layer == 0: lv = 'Lv-1'
        elif layer > 0: lv = f'Lv-{layer+1}'
        else: lv = f'D-{-layer}'
        print(f'{lv:<5}  {name:<32s}  {layer:>+6d}  {h:>3d}  {mn:>5d}  {mx:>5d}  {pz:>7d}')
        if layer == 0: print('-' * 80 + '   GROUND')
    print(f'\nTotal stack height: 30 cells')


if __name__ == '__main__':
    main()
