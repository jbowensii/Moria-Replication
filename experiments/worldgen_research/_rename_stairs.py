"""Bulk-rename stair landmarks per odd=up / even=down convention + update
zone and landmark display strings. Crystal descent stairs get 'Crystal Descent'
as their display text."""
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

# Apply renames in order that avoids name collisions. Map old -> new.
# Each step frees a name before it gets reused by a later step.
RENAMES = [
    # Free crystal-descent slots first (no name conflicts going to 12/14)
    ('Sandbox.FifthStair',    'Sandbox.TwelfthStair'),     # frees "FifthStair"
    ('Sandbox.FourthStair',   'Sandbox.FourteenthStair'),  # Crystal
    # Free other upper-range names
    ('Sandbox.EighthStair',   'Sandbox.TenthStair'),       # frees "EighthStair"
    # Now reuse freed names
    ('Sandbox.SixthStair',    'Sandbox.FifthStair'),       # uses freed FifthStair
    ('Sandbox.SeventhStair',  'Sandbox.EleventhStair'),
    ('Sandbox.SecondStair',   'Sandbox.SixthStair'),       # uses freed SixthStair
    ('Sandbox.ThirdStair',    'Sandbox.EighthStair'),      # uses freed EighthStair
]

# --- Landmark row renames ---
lm_rows = lm['Exports'][0]['Table']['Data']
applied = []
for old, new in RENAMES:
    lm_by = {r['Name']: r for r in lm_rows}
    if old not in lm_by:
        print(f'  (skip) {old} not found')
        continue
    if new in lm_by:
        print(f'  *** COLLISION: {new} already exists when renaming {old}. Aborting.')
        raise SystemExit(1)
    lm_by[old]['Name'] = new
    # Also change its DisplayName to point at the new Landmarks.Sandbox.X key
    dp = fp(lm_by[old]['Value'], 'DisplayName')
    if dp:
        dp['Value'] = f'Landmarks.{new}'
    applied.append((old, new))
    print(f'  landmark renamed: {old} -> {new}')

# --- Update zone LandmarkHandle refs ---
def set_rowname(prop, new):
    for it in prop.get('Value', []) or []:
        if isinstance(it, dict) and it.get('Name') == 'RowName':
            it['Value'] = new
            return

rename_map = dict(applied)
lh_updates = 0
for zr in z['Exports'][0]['Table']['Data']:
    lh = fp(zr['Value'], 'LandmarkHandles')
    if not lh:
        continue
    for e in (lh.get('Value') or []):
        for sub in (e.get('Value') or []):
            if isinstance(sub, dict) and sub.get('Name') == 'Landmark':
                for it in (sub.get('Value') or []):
                    if isinstance(it, dict) and it.get('Name') == 'RowName':
                        v = it.get('Value', '')
                        if v in rename_map:
                            it['Value'] = rename_map[v]
                            lh_updates += 1
print(f'\n  Updated {lh_updates} LandmarkHandle refs in zones')

# --- Update GuaranteedConnections tag refs everywhere ---
gc_updates = 0
for r in lm_rows:
    gc = fp(r['Value'], 'GuaranteedConnections')
    if not gc:
        continue
    for it in (gc.get('Value') or []):
        for sub in (it.get('Value') or []):
            if isinstance(sub, dict) and sub.get('Name') == 'TagName':
                v = sub.get('Value', '')
                # Tags look like 'World.Landmark.Sandbox.SixthStair'
                for old, new in rename_map.items():
                    old_tag = f'World.Landmark.{old}'
                    if v == old_tag:
                        sub['Value'] = f'World.Landmark.{new}'
                        gc_updates += 1
print(f'  Updated {gc_updates} GC tag refs')

# --- NameMap patches ---
for doc, path in [(z, ZP), (lm, LP)]:
    nm = doc.get('NameMap', [])
    for old, new in rename_map.items():
        if new not in nm:
            nm.append(new)
        # Tag forms
        new_tag = f'World.Landmark.{new}'
        if new_tag not in nm:
            nm.append(new_tag)
        new_disp = f'Landmarks.{new}'
        if new_disp not in nm:
            nm.append(new_disp)
    doc['NameMap'] = nm

ZP.write_text(json.dumps(z, indent=2), encoding='utf-8')
LP.write_text(json.dumps(lm, indent=2), encoding='utf-8')

# --- String updates ---
entries = w['Exports'][0]['Table']['Value']
by_key = {}
for i, e in enumerate(entries):
    if isinstance(e, (list, tuple)) and len(e) >= 1:
        by_key[e[0]] = (i, e)

def set_string(key, value):
    if key in by_key:
        i, _ = by_key[key]
        entries[i] = [key, value]
        return 'updated'
    else:
        entries.append([key, value])
        by_key[key] = (len(entries) - 1, entries[-1])
        return 'added'

# Zone display strings — these match the elevator letter to host chapter/stair
zone_strings = [
    # key,                                  English
    ('Zones.Names.SB_Elevator_B',           'First Stair'),
    ('Zones.Names.SB_Elevator_B.Banner',    'The First Stair'),
    ('Zones.Names.SB_Elevator_C',           'Sixth Stair'),
    ('Zones.Names.SB_Elevator_C.Banner',    'The Sixth Stair'),
    ('Zones.Names.SB_Elevator_D',           'Eighth Stair'),
    ('Zones.Names.SB_Elevator_D.Banner',    'The Eighth Stair'),
    ('Zones.Names.SB_Elevator_E',           'Crystal Descent'),
    ('Zones.Names.SB_Elevator_E.Banner',    'The Crystal Descent'),
    ('Zones.Names.SB_Elevator_E.Khuzdul',   'Émut Khaldul'),
    ('Zones.Names.SB_Elevator_F',           'Crystal Descent'),
    ('Zones.Names.SB_Elevator_F.Banner',    'The Crystal Descent'),
    ('Zones.Names.SB_Elevator_F.Khuzdul',   'Émut Khaldul'),
    ('Zones.Names.SB_Elevator_G',           'Fifth Stair'),
    ('Zones.Names.SB_Elevator_G.Banner',    'The Fifth Stair'),
    ('Zones.Names.SB_Elevator_H',           'Eleventh Stair'),
    ('Zones.Names.SB_Elevator_H.Banner',    'The Eleventh Stair'),
    ('Zones.Names.SB_Elevator_I',           'Tenth Stair'),
    ('Zones.Names.SB_Elevator_I.Banner',    'The Tenth Stair'),
]

# Landmark display strings — match new landmark row names
landmark_strings = [
    ('Landmarks.Sandbox.FirstStair',         'First Stair'),
    ('Landmarks.Sandbox.FifthStair',         'Fifth Stair'),
    ('Landmarks.Sandbox.SixthStair',         'Sixth Stair'),
    ('Landmarks.Sandbox.EighthStair',        'Eighth Stair'),
    ('Landmarks.Sandbox.TenthStair',         'Tenth Stair'),
    ('Landmarks.Sandbox.EleventhStair',      'Eleventh Stair'),
    ('Landmarks.Sandbox.TwelfthStair',       'Crystal Descent'),
    ('Landmarks.Sandbox.FourteenthStair',    'Crystal Descent'),
]

print('\n=== Zone string updates ===')
for k, v in zone_strings:
    st = set_string(k, v)
    print(f'  ({st}) {k:<45s} -> {v!r}')

print('\n=== Landmark string updates ===')
for k, v in landmark_strings:
    st = set_string(k, v)
    print(f'  ({st}) {k:<45s} -> {v!r}')

# Remove orphaned landmark strings (old Seventh Stair key, no longer referenced)
ORPHANED = ['Landmarks.Sandbox.SeventhStair']
kept = [e for e in entries
        if not (isinstance(e, (list, tuple)) and len(e) >= 1 and e[0] in ORPHANED)]
removed = len(entries) - len(kept)
w['Exports'][0]['Table']['Value'] = kept
print(f'\n  Removed {removed} orphaned string entries: {ORPHANED}')

WP.write_text(json.dumps(w, indent=2), encoding='utf-8')

print('\n=== Rename complete ===')
print(f'Renamed {len(applied)} landmarks, updated {lh_updates} LH refs, '
      f'{gc_updates} GC refs, rewrote {len(zone_strings)+len(landmark_strings)} strings.')
