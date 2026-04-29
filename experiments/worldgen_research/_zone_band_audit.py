"""Audit zone Position.Z vs chapter MinZ/MaxZ band.

Uses the CORRECT extractor for UAssetGUI's compact struct types
(IntVector, Vector, IntPoint, Quat, Rotator, Color) where
prop.Value[0].Value is a flat dict {X,Y,Z} rather than a list of
named property entries.

Note: chapter band is a generation-time hint, NOT a runtime constraint.
Pristine itself has ~38 zones with Position outside their chapter band,
mostly because Pos=(0,0,0) means "let the generator place this".
"""
import json
from pathlib import Path

HERE = Path(__file__).parent

COMPACT_STRUCTS = {'Vector','IntVector','IntPoint','Quat','Rotator',
                   'Color','LinearColor','Vector2D','Vector4','Box',
                   'Box2D','Plane'}


def get_vec(zr, propname):
    """Return (X,Y,Z) for a struct property, handling both compact
    (FIntVector etc.) and generic struct serialization."""
    for p in zr.get('Value') or []:
        if p.get('Name') != propname:
            continue
        val = p.get('Value')
        if not isinstance(val, list) or not val:
            return (None, None, None)
        inner = val[0]
        iv = inner.get('Value')
        # Compact: inner.Value is a dict {X,Y,Z}
        if isinstance(iv, dict):
            return (iv.get('X'), iv.get('Y'), iv.get('Z'))
        # Generic: inner.Value is a list of named property entries
        if isinstance(iv, list):
            x = y = z = None
            for it in iv:
                if not isinstance(it, dict):
                    continue
                n, v = it.get('Name'), it.get('Value')
                if n == 'X': x = v
                elif n == 'Y': y = v
                elif n == 'Z': z = v
            return (x, y, z)
        return (None, None, None)
    return (None, None, None)


def fp(v, n):
    for p in v or []:
        if isinstance(p, dict) and p.get('Name') == n:
            return p
    return None


def get(r, k):
    p = fp(r['Value'], k)
    if not p:
        return None
    v = p.get('Value')
    if isinstance(v, list):
        for it in v:
            if isinstance(it, dict) and it.get('Name') == 'RowName':
                return it.get('Value', '')
    return v


def chap_of(zr):
    c = fp(zr['Value'], 'Chapter')
    if c:
        for it in (c.get('Value') or []):
            if isinstance(it, dict) and it.get('Name') == 'RowName':
                return it.get('Value', '')
    return ''


def zstate(zr):
    es = fp(zr['Value'], 'EnabledState')
    return str(es.get('Value', '')).split('::')[-1] if es else '?'


def main():
    z = json.loads((HERE / 'DT_Moria_Zones.json').read_text(encoding='utf-8'))
    ch = json.loads((HERE / 'DT_Moria_Chapters.json').read_text(encoding='utf-8'))

    bands = {}
    for r in ch['Exports'][0]['Table']['Data']:
        bands[r['Name']] = (get(r, 'Layer'), get(r, 'MinZ'), get(r, 'MaxZ'))

    print('=== Chapter Z bands ===')
    for c, (L, mn, mx) in sorted(bands.items()):
        if L is None:
            continue
        print(f'  {c:<32s}  Layer={L:>+3}  Z={mn}..{mx}')

    print('\n=== Live zones: Position vs chapter band ===')
    viol = 0; pinned = 0; unpinned = 0
    for zr in z['Exports'][0]['Table']['Data']:
        if zstate(zr) != 'Live':
            continue
        c = chap_of(zr)
        if c not in bands:
            continue
        L, mn, mx = bands[c]
        if mn is None:
            continue
        px, py, pz = get_vec(zr, 'Position')
        sx, sy, sz = get_vec(zr, 'TargetSize')
        if (px, py, pz) == (0, 0, 0):
            unpinned += 1
            tag = '  (unpinned)'
        else:
            pinned += 1
            top = (pz or 0) + (sz or 1) - 1
            in_band = (mn <= (pz or 0)) and (top <= mx)
            tag = '' if in_band else '  <-- OUT OF BAND'
            if not in_band:
                viol += 1
        print(f'  {zr["Name"]:<42s} {c:<30s} L{L:>+3}  band={mn}..{mx}'
              f'  Pos=({px},{py},{pz}) Size=({sx},{sy},{sz}){tag}')

    print(f'\nPinned zones: {pinned}  (out of band: {viol})')
    print(f'Unpinned zones (Pos=0,0,0): {unpinned}')
    print('Note: Out-of-band on PINNED zones is the only thing worth investigating.')


if __name__ == '__main__':
    main()
