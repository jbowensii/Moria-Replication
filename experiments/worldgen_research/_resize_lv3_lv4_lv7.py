"""Resize Lv-3, Lv-4, Lv-7 chapter heights.

Lv-3 (chap-3): h=4 -> h=2
Lv-4 (chap-4): h=3 -> h=2
Lv-7 (chap-7): h=1 -> h=4
Net height change: 0. Stack stays 30 cells, Z=0..29.

Affected chapters (Z bands change, deeps below Lv-2 unchanged):
  chap-3   Lv-3   Z=18..21 -> 18..19   (h=4 -> 2; MaxZ shrinks)
  chap-4   Lv-4   Z=22..24 -> 20..21   (h=3 -> 2; shifts down by 2)
  chap-5   Lv-5   Z=25..26 -> 22..23   (shift -3)
  chap-6   Lv-6   Z=27..28 -> 24..25   (shift -3)
  chap-7   Lv-7   Z=29..29 -> 26..29   (h=1 -> 4; grows downward)

Zone Position.Z and landmark BasePosition.Z in affected chapters are clamped
into their new bands (sentinel (0,0,0) zones / landmarks unaffected).

Hard rule enforced: every Z in [0, 29].
"""
import json, shutil
from pathlib import Path

HERE = Path(__file__).parent

# (chapter, Layer, MinZ, MaxZ, PrimeZ)
UPDATES = [
    ('SandboxSmall-chapter-3',  2, 18, 19, 18),
    ('SandboxSmall-chapter-4',  3, 20, 21, 20),
    ('SandboxSmall-chapter-5',  4, 22, 23, 22),
    ('SandboxSmall-chapter-6',  5, 24, 25, 24),
    ('SandboxSmall-chapter-7',  6, 26, 29, 27),
]
NEW_BANDS = {n: (mn, mx) for n, _, mn, mx, _ in UPDATES}
AFFECTED = set(NEW_BANDS.keys())


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
def get_intvec_z(prop):
    if not prop: return None
    v = prop.get('Value')
    if isinstance(v, list) and v:
        inner = v[0]
        if isinstance(inner, dict) and isinstance(inner.get('Value'), dict):
            return inner['Value'].get('Z')
    return None
def set_intvec_z(prop, z):
    v = prop.get('Value')
    if isinstance(v, list) and v:
        inner = v[0]
        if isinstance(inner, dict) and isinstance(inner.get('Value'), dict):
            inner['Value']['Z'] = z
            return True
    return False
def is_unplaced_sentinel(prop):
    if not prop: return True
    v = prop.get('Value')
    if isinstance(v, list) and v:
        inner = v[0]
        if isinstance(inner, dict) and isinstance(inner.get('Value'), dict):
            d = inner['Value']
            return d.get('X')==0 and d.get('Y')==0 and d.get('Z')==0
    return True
def set_scalar(r, k, v):
    p = fp(r['Value'], k)
    if p is not None: p['Value'] = v
def zoneset(r):
    p = fp(r.get('Value', []), 'ZoneSet')
    if not p: return None
    return str(p.get('Value', '')).split('::')[-1]


def main():
    BAK = HERE / 'backups' / 'before Lv3-Lv4-Lv7 resize'
    BAK.mkdir(parents=True, exist_ok=True)
    for src in sorted(HERE.glob('*.json')):
        if src.name.endswith('.original.json'): continue
        if not src.name.startswith(('DT_','BC_','World')): continue
        shutil.copy2(src, BAK / src.name)
    print('Snapshot saved.\n')

    # Phase 1
    print('=== Phase 1: Chapter Z-band updates ===')
    ch_path = HERE / 'DT_Moria_Chapters.json'
    ch = json.loads(ch_path.read_text(encoding='utf-8'))
    for r in ch['Exports'][0]['Table']['Data']:
        for name, layer, mn, mx, pz in UPDATES:
            if r['Name'] == name:
                old_mn = fp(r['Value'],'MinZ').get('Value')
                old_mx = fp(r['Value'],'MaxZ').get('Value')
                set_scalar(r,'Layer',layer); set_scalar(r,'MinZ',mn)
                set_scalar(r,'MaxZ',mx); set_scalar(r,'PrimeZ',pz)
                print(f'  {name:<32s}  Z={old_mn}..{old_mx} -> {mn}..{mx}  h={mx-mn+1}  PrimeZ={pz}')
                break
    ch_path.write_text(json.dumps(ch, indent=2), encoding='utf-8')

    # Phase 2: Zone clamps in affected chapters
    print('\n=== Phase 2: Zone Position.Z clamps ===')
    z_path = HERE / 'DT_Moria_Zones.json'
    z = json.loads(z_path.read_text(encoding='utf-8'))
    shifted = 0
    for r in z['Exports'][0]['Table']['Data']:
        if zoneset(r) != 'SandboxSmall': continue
        chap_name = get_rowname(fp(r['Value'], 'Chapter'))
        if chap_name not in AFFECTED: continue
        pos = fp(r['Value'], 'Position')
        if is_unplaced_sentinel(pos): continue
        cur_z = get_intvec_z(pos)
        if cur_z is None: continue
        new_mn, new_mx = NEW_BANDS[chap_name]
        if cur_z < new_mn:
            set_intvec_z(pos, new_mn)
            print(f'  {r["Name"]:<42s}  in {chap_name}  Z {cur_z} -> {new_mn} (MinZ)')
            shifted += 1
        elif cur_z > new_mx:
            set_intvec_z(pos, new_mx)
            print(f'  {r["Name"]:<42s}  in {chap_name}  Z {cur_z} -> {new_mx} (MaxZ)')
            shifted += 1
    if shifted == 0:
        print('  (no pinned zones in affected chapters needed clamping)')
    z_path.write_text(json.dumps(z, indent=2), encoding='utf-8')

    # Phase 3: Landmark clamps
    print('\n=== Phase 3: Landmark BasePosition.Z clamps ===')
    lm_path = HERE / 'DT_Moria_Landmarks.json'
    lm = json.loads(lm_path.read_text(encoding='utf-8'))
    hosts = {}
    for zr in z['Exports'][0]['Table']['Data']:
        if zoneset(zr) != 'SandboxSmall': continue
        chap_name = get_rowname(fp(zr['Value'], 'Chapter'))
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
                            if n: hosts.setdefault(n, set()).add(chap_name)
    shifted_lm = 0
    for r in lm['Exports'][0]['Table']['Data']:
        n = r['Name']
        host_chaps = hosts.get(n, set())
        if not (host_chaps & AFFECTED): continue
        if not host_chaps.issubset(AFFECTED): continue
        bp = fp(r['Value'], 'BasePosition')
        if is_unplaced_sentinel(bp): continue
        cur_z = get_intvec_z(bp)
        if cur_z is None: continue
        ref = next(iter(host_chaps & AFFECTED))
        new_mn, new_mx = NEW_BANDS[ref]
        if cur_z < new_mn:
            set_intvec_z(bp, new_mn)
            print(f'  {n:<42s}  host={ref}  BasePos.Z {cur_z} -> {new_mn}')
            shifted_lm += 1
        elif cur_z > new_mx:
            set_intvec_z(bp, new_mx)
            print(f'  {n:<42s}  host={ref}  BasePos.Z {cur_z} -> {new_mx}')
            shifted_lm += 1
    if shifted_lm == 0:
        print('  (no landmarks in affected chapters needed clamping)')
    lm_path.write_text(json.dumps(lm, indent=2), encoding='utf-8')

    print('\n=== DONE ===')


if __name__ == '__main__':
    main()
