"""Audit: find anything WE added that's now orphan (unreferenced).
Skip anything that was in vanilla (don't touch vanilla even if unused)."""
import json

def fp(v, n):
    for p in v or []:
        if isinstance(p, dict) and p.get('Name') == n:
            return p
    return None

def get(r, k):
    p = fp(r['Value'], k)
    if not p: return None
    v = p.get('Value')
    if isinstance(v, list):
        for it in v:
            if isinstance(it, dict) and it.get('Name') == 'RowName':
                return it.get('Value', '')
    return v

def st_state(r):
    p = fp(r.get('Value', []), 'EnabledState')
    return str(p.get('Value', '')).split('::')[-1] if p else None


# Load current + vanilla
def load_pair(stem):
    cur = json.load(open(f'{stem}.json', encoding='utf-8'))
    try:
        van = json.load(open(f'{stem}.original.json', encoding='utf-8'))
    except FileNotFoundError:
        van = None
    return cur, van


# ===== StringTable =====
print('=' * 80)
print('1. WORLD STRINGTABLE — added strings not referenced')
print('=' * 80)

W_cur, W_van = load_pair('World')
cur_keys = {e[0]: e[1] for e in W_cur['Exports'][0]['Table']['Value']
            if isinstance(e, list) and len(e) >= 2}
van_keys = set()
if W_van:
    van_keys = {e[0] for e in W_van['Exports'][0]['Table']['Value']
                if isinstance(e, list) and len(e) >= 1}

added_keys = set(cur_keys) - van_keys
print(f'  Strings added (not in vanilla): {len(added_keys)}')

# Find every TextProperty StringTableEntry across DTs
referenced = set()

def walk_text_refs(obj):
    if isinstance(obj, dict):
        if 'TextPropertyData' in str(obj.get('$type', '')) and obj.get('HistoryType') == 'StringTableEntry':
            v = obj.get('Value')
            if v: referenced.add(str(v))
        for vv in obj.values():
            walk_text_refs(vv)
    elif isinstance(obj, list):
        for it in obj:
            walk_text_refs(it)

for stem in ['DT_Moria_Zones', 'DT_Moria_Landmarks', 'DT_Moria_Chapters',
             'DT_Moria_Biomes', 'DT_Moria_LayoutConnections',
             'DT_Moria_ZoneDeck', 'DT_Moria_ZoneBubbleFilters',
             'DT_Moria_ZoneTemplates']:
    try:
        d = json.load(open(f'{stem}.json', encoding='utf-8'))
        walk_text_refs(d)
    except FileNotFoundError:
        pass

orphan_added_strings = sorted(added_keys - referenced)
print(f'  Strings WE ADDED that are NOT referenced anywhere: {len(orphan_added_strings)}')
for k in orphan_added_strings:
    txt = cur_keys.get(k, '?')
    print(f'    - {k!r} = {txt!r}')

# Also flag added strings that ARE referenced (informational)
in_use_added = sorted(added_keys & referenced)
print(f'\n  Strings WE ADDED that ARE in use: {len(in_use_added)} (these are fine — kept for reference)')

# ===== Landmarks =====
print('\n' + '=' * 80)
print('2. DT_MORIA_LANDMARKS — added landmarks not referenced')
print('=' * 80)

lm_cur, lm_van = load_pair('DT_Moria_Landmarks')
cur_lm = {r['Name']: r for r in lm_cur['Exports'][0]['Table']['Data']}
van_lm = set()
if lm_van:
    van_lm = {r['Name'] for r in lm_van['Exports'][0]['Table']['Data']}
added_lm = set(cur_lm) - van_lm
print(f'  Landmarks added (not in vanilla): {len(added_lm)}')

# Find which landmarks are referenced (LandmarkHandles + GuaranteedConnections + LayoutConnections)
referenced_lm = set()
# By zones LandmarkHandles
z_cur = json.load(open('DT_Moria_Zones.json', encoding='utf-8'))
for r in z_cur['Exports'][0]['Table']['Data']:
    if st_state(r) == 'Disabled': continue
    lh = fp(r['Value'], 'LandmarkHandles')
    for e in (lh.get('Value') or []) if lh else []:
        for sub in e.get('Value') or []:
            if isinstance(sub, dict) and sub.get('Name') == 'Landmark':
                lv = sub.get('Value')
                if isinstance(lv, list):
                    for it in lv:
                        if isinstance(it, dict) and it.get('Name') == 'RowName':
                            rn = it.get('Value')
                            if rn: referenced_lm.add(rn)
# By GuaranteedConnections (every landmark mentions other landmarks)
for r in lm_cur['Exports'][0]['Table']['Data']:
    if st_state(r) == 'Disabled': continue
    gc = fp(r['Value'], 'GuaranteedConnections')
    for entry in (gc.get('Value') or []) if gc else []:
        for sub in entry.get('Value') or []:
            if isinstance(sub, dict) and sub.get('Name') == 'TagName':
                tn = sub.get('Value', '')
                short = tn.replace('World.Landmark.', '')
                if short: referenced_lm.add(short)
# By LayoutConnections
lc_cur = json.load(open('DT_Moria_LayoutConnections.json', encoding='utf-8'))
for r in lc_cur['Exports'][0]['Table']['Data']:
    if st_state(r) == 'Disabled': continue
    for f in ('OriginLandmark', 'DestinationLandmark'):
        rn = get(r, f)
        if rn: referenced_lm.add(rn)

orphan_added_lm = sorted(added_lm - referenced_lm)
print(f'  Landmarks WE ADDED that are NOT referenced by any Live row: {len(orphan_added_lm)}')
for n in orphan_added_lm:
    state = st_state(cur_lm[n])
    print(f'    - {n}  state={state}')

in_use_added_lm = sorted(added_lm & referenced_lm)
print(f'\n  Landmarks WE ADDED that ARE referenced: {len(in_use_added_lm)} (in use)')

# ===== Chapters =====
print('\n' + '=' * 80)
print('3. DT_MORIA_CHAPTERS — added chapter rows not referenced')
print('=' * 80)

ch_cur, ch_van = load_pair('DT_Moria_Chapters')
cur_ch = {r['Name']: r for r in ch_cur['Exports'][0]['Table']['Data']}
van_ch = set()
if ch_van:
    van_ch = {r['Name'] for r in ch_van['Exports'][0]['Table']['Data']}
added_ch = set(cur_ch) - van_ch
print(f'  Chapter rows added: {len(added_ch)}')

# Find which chapter rows are referenced by any zone's Chapter / AdditionalChapters
referenced_ch = set()
for r in z_cur['Exports'][0]['Table']['Data']:
    if st_state(r) == 'Disabled': continue
    rn = get(r, 'Chapter')
    if rn: referenced_ch.add(rn)
    ac = fp(r['Value'], 'AdditionalChapters')
    for entry in (ac.get('Value') or []) if ac else []:
        if isinstance(entry, dict):
            for sub in entry.get('Value') or []:
                if isinstance(sub, dict) and sub.get('Name') == 'RowName':
                    rn = sub.get('Value')
                    if rn: referenced_ch.add(rn)

orphan_added_ch = sorted(added_ch - referenced_ch)
print(f'  Chapter rows WE ADDED that are NOT referenced by any Live zone: {len(orphan_added_ch)}')
for n in orphan_added_ch:
    cid = get(cur_ch[n], 'ChapterID')
    L = get(cur_ch[n], 'Layer')
    state = st_state(cur_ch[n])
    print(f'    - {n}  ChapID={cid} Layer={L} state={state}')

# ===== Zones =====
print('\n' + '=' * 80)
print('4. DT_MORIA_ZONES — added zone rows that are Disabled (cleanup candidates)')
print('=' * 80)
z_cur_dict = {r['Name']: r for r in z_cur['Exports'][0]['Table']['Data']}
van_z = set()
try:
    z_van = json.load(open('DT_Moria_Zones.original.json', encoding='utf-8'))
    van_z = {r['Name'] for r in z_van['Exports'][0]['Table']['Data']}
except FileNotFoundError:
    pass
added_z = set(z_cur_dict) - van_z
disabled_added_z = sorted(n for n in added_z
                          if st_state(z_cur_dict[n]) == 'Disabled')
print(f'  Zones we added that are now Disabled: {len(disabled_added_z)}')
for n in disabled_added_z:
    print(f'    - {n}')

# ===== ZoneDeck =====
print('\n' + '=' * 80)
print('5. DT_MORIA_ZONEDECK — added decks not referenced')
print('=' * 80)
dk_cur, dk_van = load_pair('DT_Moria_ZoneDeck')
cur_dk = {r['Name']: r for r in dk_cur['Exports'][0]['Table']['Data']}
van_dk = set()
if dk_van:
    van_dk = {r['Name'] for r in dk_van['Exports'][0]['Table']['Data']}
added_dk = set(cur_dk) - van_dk

referenced_dk = set()
for r in z_cur['Exports'][0]['Table']['Data']:
    if st_state(r) == 'Disabled': continue
    for f in ('BubbleDeck', 'PassageDeck'):
        rn = get(r, f)
        if rn: referenced_dk.add(rn)

orphan_added_dk = sorted(added_dk - referenced_dk)
print(f'  Decks WE ADDED that are NOT referenced: {len(orphan_added_dk)}')
for n in orphan_added_dk: print(f'    - {n}')

# ===== Summary =====
print('\n' + '=' * 80)
print('SUMMARY (counts of WE-ADDED orphans only)')
print('=' * 80)
print(f'  Orphan strings:        {len(orphan_added_strings)}')
print(f'  Orphan landmarks:      {len(orphan_added_lm)}')
print(f'  Orphan chapter rows:   {len(orphan_added_ch)}')
print(f'  Disabled added zones:  {len(disabled_added_z)}')
print(f'  Orphan decks:          {len(orphan_added_dk)}')
