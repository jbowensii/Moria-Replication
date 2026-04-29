"""From 12-chap working state (Z=1..28), add Lv-7 (top, h=1) and D-7
(absolute bottom, h=1) but extend Z range DOWN to 0 instead of UP to 30.

Final stack: 14 chapters, Z=0..29.

Existing chapter Z bands stay UNCHANGED — no zone shift needed.
Only renames cascade + 2 new edge chapters.

Stack:
  chap-7   Lv-7   +6   Z=29..29   h=1   NEW (top)
  chap-6   Lv-6   +5   Z=27..28   h=2
  chap-5   Lv-5   +4   Z=25..26   h=2
  chap-4   Lv-4   +3   Z=22..24   h=3
  chap-3   Lv-3   +2   Z=18..21   h=4
  chap-2   Lv-2   +1   Z=17..17   h=1
  chap-1   Lv-1    0   Z=15..16   h=2   (ground)
  ─────────
  chap-14  D-1   -1   Z=13..14   h=2
  chap-13  D-2   -2   Z=11..12   h=2
  chap-12  D-3   -3   Z=8..10    h=3
  chap-11  D-4   -4   Z=5..7     h=3
  chap-10  D-5   -5   Z=3..4     h=2
  chap-9   D-6   -6   Z=1..2     h=2
  chap-8   D-7   -7   Z=0..0     h=1   NEW (absolute bottom at Z=0)

Total: 30 cells, Z range 0..29
"""
import json, shutil, copy
from pathlib import Path

HERE = Path(__file__).parent

# All 14 chapter slots — same 12 chapters' Z bands as before, +2 new edges.
NEW_SPEC = [
    ('SandboxSmall-chapter-1',   0, 15, 16, 15, 0),  # unchanged
    ('SandboxSmall-chapter-2',   1, 17, 17, 17, 1),  # unchanged
    ('SandboxSmall-chapter-3',   2, 18, 21, 19, 2),  # unchanged
    ('SandboxSmall-chapter-4',   3, 22, 24, 23, 3),  # unchanged
    ('SandboxSmall-chapter-5',   4, 25, 26, 25, 4),  # unchanged
    ('SandboxSmall-chapter-6',   5, 27, 28, 27, 5),  # unchanged
    ('SandboxSmall-chapter-7',   6, 29, 29, 29, 6),  # NEW Lv-7 h=1
    ('SandboxSmall-chapter-8',  -7,  0,  0,  0, 7),  # NEW D-7 h=1 absolute bottom Z=0
    ('SandboxSmall-chapter-9',  -6,  1,  2,  1, 6),  # was chap-7
    ('SandboxSmall-chapter-10', -5,  3,  4,  3, 5),  # was chap-8
    ('SandboxSmall-chapter-11', -4,  5,  7,  6, 4),  # was chap-9
    ('SandboxSmall-chapter-12', -3,  8, 10,  9, 3),  # was chap-10
    ('SandboxSmall-chapter-13', -2, 11, 12, 11, 2),  # was chap-11
    ('SandboxSmall-chapter-14', -1, 13, 14, 13, 1),  # was chap-12
]

# Reverse-order renames (chap-12 freed first, no conflicts)
RENAME_PLAN = [
    ('SandboxSmall-chapter-12', 'SandboxSmall-chapter-14'),
    ('SandboxSmall-chapter-11', 'SandboxSmall-chapter-13'),
    ('SandboxSmall-chapter-10', 'SandboxSmall-chapter-12'),
    ('SandboxSmall-chapter-9',  'SandboxSmall-chapter-11'),
    ('SandboxSmall-chapter-8',  'SandboxSmall-chapter-10'),
    ('SandboxSmall-chapter-7',  'SandboxSmall-chapter-9'),
]
RENAME = {old: new for old, new in RENAME_PLAN}


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
    BAK = HERE / 'backups' / 'before 14-chapter Z0-29'
    BAK.mkdir(parents=True, exist_ok=True)
    for src in sorted(HERE.glob('*.json')):
        if src.name.endswith('.original.json'): continue
        if not src.name.startswith(('DT_', 'BC_', 'World')): continue
        shutil.copy2(src, BAK / src.name)
    print('Snapshot saved to backups/before 14-chapter Z0-29/\n')

    # Phase 1: Chapters
    ch_path = HERE / 'DT_Moria_Chapters.json'
    ch = json.loads(ch_path.read_text(encoding='utf-8'))
    rows = ch['Exports'][0]['Table']['Data']
    by_name = {r['Name']: r for r in rows}

    print('=== Phase 1: Renames (reverse order) ===')
    for old, new in RENAME_PLAN:
        if old in by_name and new not in by_name:
            r = by_name.pop(old); r['Name'] = new; by_name[new] = r
            print(f'  {old} -> {new}')
    print()

    template = next(r for r in rows if r['Name'] == 'SandboxSmall-chapter-1')
    print('=== Chapter Z-band updates ===')
    for name, layer, mn, mx, pz, esl in NEW_SPEC:
        if name in by_name:
            r = by_name[name]; tag = '(unchanged Z)'
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

    # Phase 2: Zones — chapter retargets only (no Z shift)
    z_path = HERE / 'DT_Moria_Zones.json'
    z = json.loads(z_path.read_text(encoding='utf-8'))
    chap_retargets = 0; addchap_retargets = 0
    for r in z['Exports'][0]['Table']['Data']:
        if zoneset(r) != 'SandboxSmall': continue
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
    add_to_namemap(z, new_names)
    z_path.write_text(json.dumps(z, indent=2), encoding='utf-8')
    print(f'\n=== Phase 2: Zones ===')
    print(f'  Chapter retargets: {chap_retargets}')
    print(f'  AdditionalChapters retargets: {addchap_retargets}')
    print(f'  Position.Z shifts: 0 (existing chapter Z bands unchanged)')

    # Phase 3: LayoutConnections retargets
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
                            it['Value'] = RENAME[it['Value']]; lc_retargets += 1
    add_to_namemap(lc, list(RENAME.values()))
    lc_path.write_text(json.dumps(lc, indent=2), encoding='utf-8')
    print(f'\n=== Phase 3: LayoutConnections ===')
    print(f'  Chapter retargets: {lc_retargets}')

    # Final chart
    print()
    print('=== NEW STACK (Z=0..29) ===')
    print(f'{"Lv":<5}  {"Chapter":<32s}  {"Layer":>6}  {"h":>3}  {"MinZ":>5}  {"MaxZ":>5}  {"PrimeZ":>7}')
    print('-' * 80)
    for name, layer, mn, mx, pz, esl in sorted(NEW_SPEC, key=lambda x: -x[1]):
        h = mx - mn + 1
        if layer == 0: lv = 'Lv-1'
        elif layer > 0: lv = f'Lv-{layer+1}'
        else: lv = f'D-{-layer}'
        print(f'{lv:<5}  {name:<32s}  {layer:>+6d}  {h:>3d}  {mn:>5d}  {mx:>5d}  {pz:>7d}')
        if layer == 0: print('-' * 80 + '   GROUND')
    print('\nTotal stack height: 30 cells, Z range 0..29')


if __name__ == '__main__':
    main()
