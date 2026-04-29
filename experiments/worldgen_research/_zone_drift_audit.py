"""Compare every Live SS zone in the current state vs the
'10-chapter working' baseline. Show only zones where size, position,
chapter, deck, or extension flags drifted."""
import json, os
def fp(v, n):
    for p in v or []:
        if isinstance(p, dict) and p.get('Name') == n: return p
    return None
def get(r, k):
    p = fp(r['Value'], k)
    if not p: return None
    v = p.get('Value')
    if isinstance(v, list):
        for it in v:
            if isinstance(it, dict) and it.get('Name')=='RowName':
                return it.get('Value','')
    return v
def get_intvec(prop):
    v = prop.get('Value') if prop else None
    if isinstance(v, list) and v:
        inner = v[0]
        if isinstance(inner, dict) and isinstance(inner.get('Value'), dict):
            d = inner['Value']
            return (d.get('X'),d.get('Y'),d.get('Z'))
    return (None,None,None)
def get_bool(r, k):
    p = fp(r['Value'], k)
    return bool(p.get('Value')) if p else None
def zoneset(r):
    p = fp(r.get('Value', []), 'ZoneSet')
    return str(p.get('Value','')).split('::')[-1] if p else None
def zstate(r):
    p = fp(r.get('Value', []), 'EnabledState')
    return str(p.get('Value','')).split('::')[-1] if p else None

def zone_summary(r):
    """Capture the dimensional/placement state of one zone."""
    return {
        'chap': get(r, 'Chapter'),
        'pos': get_intvec(fp(r['Value'], 'Position')),
        'size': get_intvec(fp(r['Value'], 'TargetSize')),
        'bubble_deck': get(r, 'BubbleDeck'),
        'passage_deck': get(r, 'PassageDeck'),
        'pos_from_lm': get_bool(r, 'bPositionFromLandmarks'),
        'extend_footprint': get_bool(r, 'bExtendFootprint'),
        'state': zstate(r),
    }

OLD_PATH = 'backups/10-chapter working/DT_Moria_Zones.json'
NEW_PATH = 'DT_Moria_Zones.json'

old = json.load(open(OLD_PATH, encoding='utf-8'))
new = json.load(open(NEW_PATH, encoding='utf-8'))

# Build summary maps for SS zones
def ss_summary_map(d):
    m = {}
    for r in d['Exports'][0]['Table']['Data']:
        if zoneset(r) != 'SandboxSmall': continue
        m[r['Name']] = zone_summary(r)
    return m

old_m = ss_summary_map(old)
new_m = ss_summary_map(new)

added = sorted(set(new_m) - set(old_m))
removed = sorted(set(old_m) - set(new_m))
common = sorted(set(old_m) & set(new_m))

# Filter to zones with ANY drift
drifted = []
for n in common:
    if old_m[n] != new_m[n]:
        drifted.append(n)

print(f'=== SandboxSmall zone drift: 10-chapter working -> CURRENT ===')
print(f'Old SS zone count: {len(old_m)}')
print(f'New SS zone count: {len(new_m)}')
print(f'Added (new since baseline): {len(added)}')
print(f'Removed: {len(removed)}')
print(f'Drifted (any field changed): {len(drifted)}')

if added:
    print('\n--- ZONES ADDED since baseline ---')
    for n in added:
        s = new_m[n]
        print(f'  + {n}')
        print(f'      chap={s["chap"]}  Pos={s["pos"]}  Size={s["size"]}  state={s["state"]}')
        print(f'      decks: B={s["bubble_deck"]}  P={s["passage_deck"]}')

if removed:
    print('\n--- ZONES REMOVED since baseline ---')
    for n in removed:
        print(f'  - {n}')

if drifted:
    print('\n--- ZONES WITH DRIFT (only fields that changed shown) ---')
    for n in drifted:
        old_s = old_m[n]; new_s = new_m[n]
        print(f'  ~ {n}')
        for k in ['chap', 'pos', 'size', 'bubble_deck', 'passage_deck',
                  'pos_from_lm', 'extend_footprint', 'state']:
            if old_s[k] != new_s[k]:
                print(f'      {k:<18s}: {old_s[k]!r}  ->  {new_s[k]!r}')

# Compute overlap-related deltas
print('\n=== Footprint changes summary (X*Y horizontal area) ===')
shrunk = []
grown = []
for n in drifted:
    o = old_m[n]; nw = new_m[n]
    if None in o['size'] or None in nw['size']: continue
    o_area = o['size'][0] * o['size'][1]
    n_area = nw['size'][0] * nw['size'][1]
    if o_area != n_area:
        diff = n_area - o_area
        pct = (diff / o_area * 100) if o_area else 0
        if diff < 0:
            shrunk.append((n, o['size'], nw['size'], pct))
        else:
            grown.append((n, o['size'], nw['size'], pct))

if shrunk:
    print('\nShrunk zones (less ground covered):')
    for n, os_, ns_, pct in shrunk:
        print(f'  {n}: {os_} -> {ns_}  ({pct:+.0f}%)')
if grown:
    print('\nGrown zones (more ground covered):')
    for n, os_, ns_, pct in grown:
        print(f'  {n}: {os_} -> {ns_}  ({pct:+.0f}%)')
if not shrunk and not grown:
    print('  No horizontal footprint changes.')
