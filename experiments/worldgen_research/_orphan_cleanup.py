"""Remove all orphan items WE added — strings, landmarks, chapter rows.
Vanilla items are filtered out by comparing against .original.json sidecars.
Sync NameMaps after each removal."""
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


# ===== Compute orphan sets (same logic as audit script) =====
W = json.load(open('World.json', encoding='utf-8'))
W_van = json.load(open('World.original.json', encoding='utf-8'))
lm = json.load(open('DT_Moria_Landmarks.json', encoding='utf-8'))
lm_van = json.load(open('DT_Moria_Landmarks.original.json', encoding='utf-8'))
ch = json.load(open('DT_Moria_Chapters.json', encoding='utf-8'))
ch_van = json.load(open('DT_Moria_Chapters.original.json', encoding='utf-8'))
z = json.load(open('DT_Moria_Zones.json', encoding='utf-8'))
lc = json.load(open('DT_Moria_LayoutConnections.json', encoding='utf-8'))

# StringTable orphans
cur_keys = {e[0] for e in W['Exports'][0]['Table']['Value']
            if isinstance(e, list) and len(e) >= 2}
van_keys = {e[0] for e in W_van['Exports'][0]['Table']['Value']
            if isinstance(e, list) and len(e) >= 1}
added_keys = cur_keys - van_keys

referenced_text = set()
def walk(obj):
    if isinstance(obj, dict):
        if 'TextPropertyData' in str(obj.get('$type', '')) and obj.get('HistoryType') == 'StringTableEntry':
            v = obj.get('Value')
            if v: referenced_text.add(str(v))
        for vv in obj.values(): walk(vv)
    elif isinstance(obj, list):
        for it in obj: walk(it)

for stem in ['DT_Moria_Zones', 'DT_Moria_Landmarks', 'DT_Moria_Chapters',
             'DT_Moria_Biomes', 'DT_Moria_LayoutConnections',
             'DT_Moria_ZoneDeck', 'DT_Moria_ZoneBubbleFilters',
             'DT_Moria_ZoneTemplates']:
    try:
        d = json.load(open(f'{stem}.json', encoding='utf-8'))
        walk(d)
    except FileNotFoundError:
        pass

orphan_strings = added_keys - referenced_text

# Landmark orphans
cur_lm_names = {r['Name'] for r in lm['Exports'][0]['Table']['Data']}
van_lm_names = {r['Name'] for r in lm_van['Exports'][0]['Table']['Data']}
added_lm_names = cur_lm_names - van_lm_names

referenced_lm = set()
for r in z['Exports'][0]['Table']['Data']:
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
for r in lm['Exports'][0]['Table']['Data']:
    if st_state(r) == 'Disabled': continue
    gc = fp(r['Value'], 'GuaranteedConnections')
    for entry in (gc.get('Value') or []) if gc else []:
        for sub in entry.get('Value') or []:
            if isinstance(sub, dict) and sub.get('Name') == 'TagName':
                tn = sub.get('Value', '').replace('World.Landmark.', '')
                if tn: referenced_lm.add(tn)
for r in lc['Exports'][0]['Table']['Data']:
    if st_state(r) == 'Disabled': continue
    for f in ('OriginLandmark', 'DestinationLandmark'):
        rn = get(r, f)
        if rn: referenced_lm.add(rn)

orphan_lm = added_lm_names - referenced_lm

# Chapter orphans
cur_ch_names = {r['Name'] for r in ch['Exports'][0]['Table']['Data']}
van_ch_names = {r['Name'] for r in ch_van['Exports'][0]['Table']['Data']}
added_ch_names = cur_ch_names - van_ch_names

referenced_ch = set()
for r in z['Exports'][0]['Table']['Data']:
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

orphan_ch = added_ch_names - referenced_ch

# ===== Apply removals =====
print(f'Removing {len(orphan_strings)} StringTable entries...')
W['Exports'][0]['Table']['Value'] = [
    e for e in W['Exports'][0]['Table']['Value']
    if not (isinstance(e, list) and len(e) >= 1 and e[0] in orphan_strings)
]

print(f'Removing {len(orphan_lm)} landmark rows...')
lm['Exports'][0]['Table']['Data'] = [
    r for r in lm['Exports'][0]['Table']['Data']
    if r['Name'] not in orphan_lm
]

print(f'Removing {len(orphan_ch)} chapter rows...')
ch['Exports'][0]['Table']['Data'] = [
    r for r in ch['Exports'][0]['Table']['Data']
    if r['Name'] not in orphan_ch
]

# ===== Sync NameMaps =====
def sync_nm(d, *, remove_set):
    nm = d.get('NameMap', [])
    new_nm = [n for n in nm if n not in remove_set]
    removed = len(nm) - len(new_nm)
    d['NameMap'] = new_nm
    if 'NamesReferencedFromExportDataCount' in d:
        d['NamesReferencedFromExportDataCount'] = len(new_nm)
    exp0 = d['Exports'][0]
    if 'Generations' in exp0 and exp0['Generations']:
        exp0['Generations'][0]['NameCount'] = len(new_nm)
    return removed

w_nm_removed = sync_nm(W, remove_set=orphan_strings)
print(f'  World NameMap removed: {w_nm_removed}')
lm_nm_removed = sync_nm(lm, remove_set=orphan_lm)
print(f'  Landmarks NameMap removed: {lm_nm_removed}')
ch_nm_removed = sync_nm(ch, remove_set=orphan_ch)
print(f'  Chapters NameMap removed: {ch_nm_removed}')

# Save
json.dump(W, open('World.json', 'w', encoding='utf-8'), indent=2)
json.dump(lm, open('DT_Moria_Landmarks.json', 'w', encoding='utf-8'), indent=2)
json.dump(ch, open('DT_Moria_Chapters.json', 'w', encoding='utf-8'), indent=2)
print('\nSaved.')
print(f'\nFinal counts:')
print(f'  World StringTable entries: {len(W["Exports"][0]["Table"]["Value"])}')
print(f'  Landmark rows:             {len(lm["Exports"][0]["Table"]["Data"])}')
print(f'  Chapter rows:              {len(ch["Exports"][0]["Table"]["Data"])}')
