"""Sequentially renumber stairs: odd = up (1/3/5/7) and even = down (2/4/6/8/10)
in the order they're encountered going away from ground. Crystal descent stairs
become 8th and 10th (deepest 2 down transitions) with display 'Crystal Descent'.
"""
import json, copy
from pathlib import Path

HERE = Path(__file__).parent
ZP = HERE / 'DT_Moria_Zones.json'
LP = HERE / 'DT_Moria_Landmarks.json'
WP = HERE / 'World.json'

z  = json.loads(ZP.read_text(encoding='utf-8'))
lm = json.loads(LP.read_text(encoding='utf-8'))
w  = json.loads(WP.read_text(encoding='utf-8'))

def fp(v, n):
    for p in v or []:
        if isinstance(p, dict) and p.get('Name') == n:
            return p
    return None

# RENAMES in dependency-safe order: frees names before reusing them.
RENAMES = [
    # Step 1: free names needed later by temporarily renaming their current holders.
    ('Sandbox.SixthStair',       'Sandbox.SecondStair'),    # frees SixthStair
    ('Sandbox.EighthStair',      'Sandbox.FourthStair'),    # frees EighthStair
    ('Sandbox.TenthStair',       'Sandbox.SixthStair'),     # uses freed SixthStair, frees TenthStair
    ('Sandbox.TwelfthStair',     'Sandbox.EighthStair'),    # uses freed EighthStair (Crystal)
    ('Sandbox.FourteenthStair',  'Sandbox.TenthStair'),     # uses freed TenthStair (Crystal)
    ('Sandbox.FifthStair',       'Sandbox.ThirdStair'),     # frees FifthStair
    ('Sandbox.SeventhStair',     'Sandbox.FifthStair'),     # uses freed FifthStair, frees SeventhStair
    ('Sandbox.EleventhStair',    'Sandbox.SeventhStair'),   # uses freed SeventhStair
]

lm_rows = lm['Exports'][0]['Table']['Data']

applied = []
for old, new in RENAMES:
    lm_by = {r['Name']: r for r in lm_rows}
    if old not in lm_by:
        print(f'  (skip) {old} not found'); continue
    if new in lm_by:
        print(f'  *** COLLISION: {new} already exists before renaming {old}. Aborting.')
        raise SystemExit(1)
    lm_by[old]['Name'] = new
    dp = fp(lm_by[old]['Value'], 'DisplayName')
    if dp:
        dp['Value'] = f'Landmarks.{new}'
    applied.append((old, new))
    print(f'  landmark renamed: {old} -> {new}')

rename_map = dict(applied)

# Update LandmarkHandles in zones
def set_rowname(prop, new):
    for it in prop.get('Value', []) or []:
        if isinstance(it, dict) and it.get('Name') == 'RowName':
            it['Value'] = new
            return

lh_updates = 0
for zr in z['Exports'][0]['Table']['Data']:
    lh = fp(zr['Value'], 'LandmarkHandles')
    if not lh: continue
    for e in (lh.get('Value') or []):
        for sub in (e.get('Value') or []):
            if isinstance(sub, dict) and sub.get('Name') == 'Landmark':
                for it in (sub.get('Value') or []):
                    if isinstance(it, dict) and it.get('Name') == 'RowName':
                        v = it.get('Value', '')
                        if v in rename_map:
                            it['Value'] = rename_map[v]
                            lh_updates += 1

# Update GC tag refs
gc_updates = 0
for r in lm_rows:
    gc = fp(r['Value'], 'GuaranteedConnections')
    if not gc: continue
    for it in (gc.get('Value') or []):
        for sub in (it.get('Value') or []):
            if isinstance(sub, dict) and sub.get('Name') == 'TagName':
                v = sub.get('Value', '')
                for old, new in rename_map.items():
                    if v == f'World.Landmark.{old}':
                        sub['Value'] = f'World.Landmark.{new}'
                        gc_updates += 1

# NameMap patches
for doc, _path in [(z, ZP), (lm, LP)]:
    nm = doc.get('NameMap', [])
    for new in set(rename_map.values()):
        for s in (new, f'World.Landmark.{new}', f'Landmarks.{new}'):
            if s not in nm:
                nm.append(s)
    doc['NameMap'] = nm

ZP.write_text(json.dumps(z, indent=2), encoding='utf-8')
LP.write_text(json.dumps(lm, indent=2), encoding='utf-8')

print(f'\n  Updated {lh_updates} LandmarkHandle refs, {gc_updates} GC refs')

# --- Zone + landmark display strings ---
entries = w['Exports'][0]['Table']['Value']
by_key = {e[0]: (i, e) for i, e in enumerate(entries)
          if isinstance(e, (list, tuple)) and len(e) >= 1}

def set_string(key, value):
    if key in by_key:
        i, _ = by_key[key]; entries[i] = [key, value]
        return 'updated'
    else:
        entries.append([key, value])
        by_key[key] = (len(entries) - 1, entries[-1])
        return 'added'

zone_strings = [
    ('Zones.Names.SB_Elevator_B',         'First Stair'),
    ('Zones.Names.SB_Elevator_B.Banner',  'The First Stair'),
    ('Zones.Names.SB_Elevator_C',         'Second Stair'),
    ('Zones.Names.SB_Elevator_C.Banner',  'The Second Stair'),
    ('Zones.Names.SB_Elevator_D',         'Fourth Stair'),
    ('Zones.Names.SB_Elevator_D.Banner',  'The Fourth Stair'),
    ('Zones.Names.SB_Elevator_E',         'Crystal Descent'),
    ('Zones.Names.SB_Elevator_E.Banner',  'The Crystal Descent'),
    ('Zones.Names.SB_Elevator_F',         'Crystal Descent'),
    ('Zones.Names.SB_Elevator_F.Banner',  'The Crystal Descent'),
    ('Zones.Names.SB_Elevator_G',         'Third Stair'),
    ('Zones.Names.SB_Elevator_G.Banner',  'The Third Stair'),
    ('Zones.Names.SB_Elevator_H',         'Seventh Stair'),
    ('Zones.Names.SB_Elevator_H.Banner',  'The Seventh Stair'),
    ('Zones.Names.SB_Elevator_I',         'Sixth Stair'),
    ('Zones.Names.SB_Elevator_I.Banner',  'The Sixth Stair'),
    ('Zones.Names.SB_Elevator_J',         'Fifth Stair'),
    ('Zones.Names.SB_Elevator_J.Banner',  'The Fifth Stair'),
]

landmark_strings = [
    ('Landmarks.Sandbox.FirstStair',      'First Stair'),
    ('Landmarks.Sandbox.SecondStair',     'Second Stair'),
    ('Landmarks.Sandbox.ThirdStair',      'Third Stair'),
    ('Landmarks.Sandbox.FourthStair',     'Fourth Stair'),
    ('Landmarks.Sandbox.FifthStair',      'Fifth Stair'),
    ('Landmarks.Sandbox.SixthStair',      'Sixth Stair'),
    ('Landmarks.Sandbox.SeventhStair',    'Seventh Stair'),
    ('Landmarks.Sandbox.EighthStair',     'Crystal Descent'),
    ('Landmarks.Sandbox.TenthStair',      'Crystal Descent'),
]

print('\n=== Zone display strings ===')
for k, v in zone_strings:
    st = set_string(k, v)
    print(f'  ({st}) {k:<45s} -> {v!r}')

print('\n=== Landmark display strings ===')
for k, v in landmark_strings:
    st = set_string(k, v)
    print(f'  ({st}) {k:<45s} -> {v!r}')

# Remove orphaned landmark strings that no longer correspond to any landmark
orphans = [
    'Landmarks.Sandbox.EleventhStair',
    'Landmarks.Sandbox.TwelfthStair',
    'Landmarks.Sandbox.FourteenthStair',
]
kept = [e for e in entries
        if not (isinstance(e, (list, tuple)) and len(e) >= 1 and e[0] in orphans)]
removed = len(entries) - len(kept)
w['Exports'][0]['Table']['Value'] = kept
print(f'\n  Removed {removed} orphaned entries: {orphans}')

WP.write_text(json.dumps(w, indent=2), encoding='utf-8')
print(f'\n=== Done ===')
print(f'Renamed {len(applied)} landmarks.')
