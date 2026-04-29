"""Swap D-3 (chap-12) h=2 -> h=3 and D-1 (chap-14) h=2 -> h=1.

Net height change: 0. Stack stays 30 cells (Z=0..29).

Affected chapter Z-band updates (3 chapters change, others stay put):
  chap-12  D-3  Z=9..10  -> 9..11   (h=2 -> h=3, MaxZ +1)
  chap-13  D-2  Z=11..12 -> 12..13  (h=2 unchanged, shifted +1 by chap-12 growth)
  chap-14  D-1  Z=13..14 -> 14..14  (h=2 -> h=1, MinZ +1, MaxZ same)

Zone Position.Z and landmark BasePosition.Z are clamped to the new bands
(except (0,0,0) sentinels which mean "generator-placed").

Hard rule: every Z in [0, 29].
"""
import json, shutil
from pathlib import Path

HERE = Path(__file__).parent

# (chapter, Layer, MinZ, MaxZ, PrimeZ)
UPDATES = [
    ('SandboxSmall-chapter-12', -3,  9, 11, 10),  # D-3 h=2 -> 3, MaxZ extends
    ('SandboxSmall-chapter-13', -2, 12, 13, 12),  # D-2 shifted +1
    ('SandboxSmall-chapter-14', -1, 14, 14, 14),  # D-1 h=2 -> 1, MinZ +1
]
NEW_BANDS = {n: (mn, mx) for n, _, mn, mx, _ in UPDATES}
AFFECTED_CHAPTERS = set(NEW_BANDS.keys())


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
            return (d.get('X') == 0 and d.get('Y') == 0 and d.get('Z') == 0)
    return True
def set_scalar(r, key, val):
    p = fp(r['Value'], key)
    if p is not None: p['Value'] = val
def zoneset(r):
    p = fp(r.get('Value', []), 'ZoneSet')
    if not p: return None
    return str(p.get('Value','')).split('::')[-1]


def main():
    BAK = HERE / 'backups' / 'before D1-D3 height swap'
    BAK.mkdir(parents=True, exist_ok=True)
    for src in sorted(HERE.glob('*.json')):
        if src.name.endswith('.original.json'): continue
        if not src.name.startswith(('DT_', 'BC_', 'World')): continue
        shutil.copy2(src, BAK / src.name)
    print('Snapshot saved to backups/before D1-D3 height swap/\n')

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

    # Phase 2: Zone clamps
    print('\n=== Phase 2: Zone Position.Z clamps in affected chapters ===')
    z_path = HERE / 'DT_Moria_Zones.json'
    z = json.loads(z_path.read_text(encoding='utf-8'))
    shifted = 0
    for r in z['Exports'][0]['Table']['Data']:
        if zoneset(r) != 'SandboxSmall': continue
        chap_name = get_rowname(fp(r['Value'], 'Chapter'))
        if chap_name not in AFFECTED_CHAPTERS: continue
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
    print('\n=== Phase 3: Landmark BasePosition.Z clamps in affected chapters ===')
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
        if not (host_chaps & AFFECTED_CHAPTERS): continue
        if not host_chaps.issubset(AFFECTED_CHAPTERS): continue
        bp = fp(r['Value'], 'BasePosition')
        if is_unplaced_sentinel(bp): continue
        cur_z = get_intvec_z(bp)
        if cur_z is None: continue
        ref_chap = next(iter(host_chaps & AFFECTED_CHAPTERS))
        new_mn, new_mx = NEW_BANDS[ref_chap]
        if cur_z < new_mn:
            set_intvec_z(bp, new_mn)
            print(f'  {n:<42s}  host={ref_chap}  BasePos.Z {cur_z} -> {new_mn}')
            shifted_lm += 1
        elif cur_z > new_mx:
            set_intvec_z(bp, new_mx)
            print(f'  {n:<42s}  host={ref_chap}  BasePos.Z {cur_z} -> {new_mx}')
            shifted_lm += 1
    if shifted_lm == 0:
        print('  (no landmarks in affected chapters needed clamping)')
    lm_path.write_text(json.dumps(lm, indent=2), encoding='utf-8')

    # Final stack chart
    print('\n=== NEW STACK ===')
    ch2 = json.loads(ch_path.read_text(encoding='utf-8'))
    rows = sorted(
        [r for r in ch2['Exports'][0]['Table']['Data']
         if r['Name'].startswith('SandboxSmall-chapter-')],
        key=lambda r: -(fp(r['Value'],'Layer').get('Value') or 0)
    )
    print(f'{"Lv":<5}  {"Chapter":<32s}  {"Layer":>6}  {"h":>3}  {"MinZ":>5}  {"MaxZ":>5}  {"PrimeZ":>7}')
    print('-' * 80)
    total_h = 0
    for r in rows:
        L = fp(r['Value'],'Layer').get('Value')
        mn = fp(r['Value'],'MinZ').get('Value')
        mx = fp(r['Value'],'MaxZ').get('Value')
        pz = fp(r['Value'],'PrimeZ').get('Value')
        h = mx - mn + 1
        total_h += h
        if L == 0: lv = 'Lv-1'
        elif L > 0: lv = f'Lv-{L+1}'
        else: lv = f'D-{-L}'
        print(f'{lv:<5}  {r["Name"]:<32s}  {L:>+6d}  {h:>3d}  {mn:>5d}  {mx:>5d}  {pz:>7d}')
        if L == 0: print('-' * 80 + '   GROUND')
    print(f'\nTotal height: {total_h} cells')


if __name__ == '__main__':
    main()
