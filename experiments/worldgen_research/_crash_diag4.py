"""_crash_diag4.py — final pinpoint:
- Show full template field values (bExclusive, bRequired, ZoneRule, bLeafZoneRoute)
- Tabulate all 22 new GC arrows vs 13 new LC arrows; flag the unmatched GC arrows
"""
import json
from pathlib import Path

WGR = Path(__file__).resolve().parent

def load(name):
    with open(WGR / name, 'r', encoding='utf-8') as f:
        d = json.load(f)
    table = d['Exports'][0].get('Table', {})
    rows = table.get('Data', []) if 'Data' in table else (table.get('Value', []) or [])
    return d, rows

_, conns_rows = load('DT_Moria_LayoutConnections.json')

def field_value(r, key):
    p = next((p for p in r.get('Value', []) if isinstance(p, dict) and p.get('Name') == key), None)
    if not p: return None
    v = p.get('Value')
    if isinstance(v, list) and v and isinstance(v[0], dict):
        inner = v[0].get('Value')
        if isinstance(inner, list):
            for it in inner:
                if isinstance(it, dict) and it.get('Name') == 'RowName':
                    return it.get('Value', '')
        return inner
    return v

# Show key template fields
def show(rows, name):
    r = next((rr for rr in rows if rr.get('Name') == name), None)
    if not r: print(f'NOT FOUND: {name}'); return
    print(f'\n--- {name} ---')
    for k in ('OriginLandmark','DestinationLandmark','OriginZone','DestinationZone',
             'OriginInterface','DestinationInterface','OriginKind','DestinationKind',
             'OriginCoord','DestinationCoord','OriginFavor','DestinationFavor',
             'ZoneSet','ZoneRule','EnabledState','bExclusive','bRequired','bLeafZoneRoute'):
        print(f'   {k:22s} = {field_value(r,k)!r}')

for n in ('Sandbox_ElvenEntranceToPromenade',
          'Sandbox_E_LowerDescent_to_F_CrystalDescent',
          'Sandbox_FloorD6_Internal'):
    show(conns_rows, n)

# Also pick a vanilla stair-relevant LC (look for stair names in any LC)
print('\n=== Any vanilla LC where landmark name contains "Stair" or "Descent" ===')
for r in conns_rows:
    n = r.get('Name','')
    if n.startswith('Sandbox_E_') or n.startswith('Sandbox_F_') or n.startswith('Sandbox_G_') \
       or n.startswith('Sandbox_C_') or n.startswith('Sandbox_H_') or n.startswith('Sandbox_B_') \
       or n.startswith('Sandbox_Floor'):
        continue   # skip our new rows
    o = field_value(r, 'OriginLandmark') or ''
    d = field_value(r, 'DestinationLandmark') or ''
    if any(s in (o + d) for s in ('Stair','Descent')):
        print(f'  {r["Name"]}: OL={o}  DL={d}')

# Build the 22 GC arrows table from current landmarks doc
print('\n=== 22 new GC arrows vs 13 new LC arrows ===')
_, lm_rows = load('DT_Moria_Landmarks.json')
_, pre_lm  = load('DT_Moria_Landmarks.before_lvfix.json')

def gc_set(rows):
    out = {}
    for r in rows:
        n = r.get('Name');
        gcs = []
        for p in r.get('Value', []) or []:
            if isinstance(p, dict) and p.get('Name') == 'GuaranteedConnections':
                v = p.get('Value') or []
                for e in v:
                    if isinstance(e, dict):
                        ev = e.get('Value')
                        if isinstance(ev, list):
                            for it in ev:
                                if isinstance(it, dict) and it.get('Name') == 'TagName':
                                    gcs.append(it.get('Value'))
        out[n] = sorted(gcs)
    return out

cur_gc = gc_set(lm_rows)
pre_gc = gc_set(pre_lm)

# Build new GC arrows: list of (src_landmark_name, dest_short)
new_gc_arrows = []
for n, cgs in cur_gc.items():
    pgs = set(pre_gc.get(n, []))
    for tag in cgs:
        if tag not in pgs and isinstance(tag, str) and tag.startswith('World.Landmark.'):
            new_gc_arrows.append((n, tag.split('.')[-1]))

# Build new LC arrows: list of (origin_landmark, dest_landmark)
def lm_short(s): return s.split('.')[-1] if s else s
new_lc_names = {
    'Sandbox_E_LowerDescent_to_F_CrystalDescent',
    'Sandbox_F_CrystalDescent_to_G_SeventhStair',
    'Sandbox_G_SeventhStair_to_C_SecondStair',
    'Sandbox_C_SecondStair_to_H_NinthStair',
    'Sandbox_H_TenthStair_to_B_FirstStair',
    'Sandbox_B_FourthStair_to_D_ThirdStair',
    'Sandbox_FloorD6_Internal','Sandbox_FloorD5_Internal','Sandbox_FloorD2_Internal',
    'Sandbox_FloorLv1bot_Internal','Sandbox_FloorLv1_Internal','Sandbox_FloorLv5_Internal',
    'Sandbox_FloorLv6_Internal'
}
new_lc_arrows = set()
for r in conns_rows:
    if r.get('Name') in new_lc_names:
        o = field_value(r, 'OriginLandmark') or ''
        d = field_value(r, 'DestinationLandmark') or ''
        new_lc_arrows.add((lm_short(o), lm_short(d)))

print(f'  {len(new_gc_arrows)} new GC arrows, {len(new_lc_arrows)} new LC arrows')

# For each new GC arrow, is there an LC arrow (in either direction, anywhere in DT) backing it?
# Build all-LC arrow set (any direction) keyed by short names
all_lc_arrows = set()
for r in conns_rows:
    o = field_value(r, 'OriginLandmark') or ''
    d = field_value(r, 'DestinationLandmark') or ''
    if o and d:
        all_lc_arrows.add((lm_short(o), lm_short(d)))

print('\n  Match status of each new GC arrow:')
unmatched = []
for src, dst in new_gc_arrows:
    src_short = lm_short(src)
    has_fwd = (src_short, dst) in all_lc_arrows
    has_rev = (dst, src_short) in all_lc_arrows
    flag = ''
    if not (has_fwd or has_rev):
        flag = '** UNMATCHED **'
        unmatched.append((src, dst))
    print(f'    {src_short:22s} -> {dst:22s}  fwd={has_fwd} rev={has_rev}  {flag}')

print(f'\n  {len(unmatched)} GC arrows have NO LC in either direction:')
for src, dst in unmatched:
    print(f'    {src} -> {dst}')
