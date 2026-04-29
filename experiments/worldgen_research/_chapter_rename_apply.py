"""Apply chapter restructure per user spec.

Renames 14 SandboxSmall-chapter-N -> SandboxSmall-ChapterNN.LevelN/DeepN
Updates 71 zone Chapter refs.
Appends 51 zone-anchored chapter rows + 35 landmark-anchored chapter rows.
Adds StringTable entries for each new + renamed chapter.
Bridge chapters (Moria-DurinTower/DimrillDale/TradingPost) and their zones/landmarks
are LEFT ALONE.
"""
import json
import copy

CHAP_PATH = 'DT_Moria_Chapters.json'
Z_PATH = 'DT_Moria_Zones.json'
W_PATH = 'World.json'

SKIP_LANDMARKS = {'Sandbox.DurinsTower', 'Sandbox.DimrillDale', 'Sandbox.TradingPost'}
SKIP_ZONES = {'Sandbox_DurinsTower', 'Sandbox_DimrillDale', 'Sandbox_TradingPost'}


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


def st(r):
    p = fp(r.get('Value', []), 'EnabledState')
    return str(p.get('Value', '')).split('::')[-1] if p else None


def zoneset(r):
    p = fp(r.get('Value', []), 'ZoneSet')
    return str(p.get('Value', '')).split('::')[-1] if p else None


# Load
chap = json.load(open(CHAP_PATH, encoding='utf-8'))
z = json.load(open(Z_PATH, encoding='utf-8'))
W = json.load(open(W_PATH, encoding='utf-8'))

# Build maps from current state (BEFORE any renames)
chap_layer = {r['Name']: get(r, 'Layer') for r in chap['Exports'][0]['Table']['Data']}
chap_chapid = {r['Name']: get(r, 'ChapterID') for r in chap['Exports'][0]['Table']['Data']}


def lv_name(c):
    L = chap_layer.get(c)
    if L is None:
        return None
    if L == 0:
        return 'Level1'
    if L > 0:
        return f'Level{L+1}'
    return f'Deep{-L}'


# 14 SS chapter renames
RENAMES = {}
for cname in chap_layer:
    if not cname.startswith('SandboxSmall-chapter-'):
        continue
    cid = chap_chapid.get(cname)
    if cid is None:
        continue
    RENAMES[cname] = f'SandboxSmall-Chapter{cid:02d}.{lv_name(cname)}'

print(f'Step 1: Rename {len(RENAMES)} chapter rows')
for cd in chap['Exports'][0]['Table']['Data']:
    if cd['Name'] in RENAMES:
        old = cd['Name']
        cd['Name'] = RENAMES[old]
        print(f'  {old} -> {cd["Name"]}')

# Step 2: Update 71 zone Chapter refs
print(f'\nStep 2: Update zone Chapter refs')
ref_updates = 0
for r in z['Exports'][0]['Table']['Data']:
    cprop = fp(r['Value'], 'Chapter')
    if not cprop:
        continue
    val = cprop.get('Value')
    if not isinstance(val, list):
        continue
    for it in val:
        if isinstance(it, dict) and it.get('Name') == 'RowName':
            old = it.get('Value')
            if old in RENAMES:
                it['Value'] = RENAMES[old]
                ref_updates += 1
print(f'  Updated {ref_updates} zone Chapter refs')

# Step 3: Build the list of new chapter rows to append
# Need parent row template per ChapterID
parent_row_by_cid = {}
for cd in chap['Exports'][0]['Table']['Data']:
    cid = get(cd, 'ChapterID')
    name = cd['Name']
    # Only track SS-renamed levels, not bridges
    if cid is not None and name.startswith('SandboxSmall-Chapter') and '.Level' in name or (name.startswith('SandboxSmall-Chapter') and '.Deep' in name):
        parent_row_by_cid[cid] = cd

# Collect zone-anchored rows
zones_per_old_chap = {}
for r in z['Exports'][0]['Table']['Data']:
    if zoneset(r) != 'SandboxSmall' or st(r) == 'Disabled':
        continue
    if r['Name'] in SKIP_ZONES:
        continue
    c = get(r, 'Chapter')
    # c is now the renamed name
    zones_per_old_chap.setdefault(c, []).append(r['Name'])

# Collect landmark-anchored (per Q3B: dedupe across hosts, primary = lowest cid)
lm_hosts = {}
for r in z['Exports'][0]['Table']['Data']:
    if zoneset(r) != 'SandboxSmall' or st(r) == 'Disabled':
        continue
    c = get(r, 'Chapter')  # already renamed
    lh = fp(r['Value'], 'LandmarkHandles')
    for e in (lh.get('Value') or []) if lh else []:
        for sub in e.get('Value') or []:
            if isinstance(sub, dict) and sub.get('Name') == 'Landmark':
                lv = sub.get('Value')
                if isinstance(lv, list):
                    for it in lv:
                        if isinstance(it, dict) and it.get('Name') == 'RowName':
                            ln = it.get('Value')
                            if ln and ln not in SKIP_LANDMARKS:
                                lm_hosts.setdefault(ln, set()).add(c)

# Rebuild ChapterID lookup with renamed keys
chap_chapid_new = {r['Name']: get(r, 'ChapterID')
                   for r in chap['Exports'][0]['Table']['Data']}


def short_zone(zn):
    return zn.replace('Sandbox_Small_', '').replace('Sandbox_', '')


def short_lm(ln):
    return (ln.replace('Sandbox.', '').replace('Chapter2.', '')
            .replace('Chapter3.', '').replace('Chapter4.', '')
            .replace('Chapter5.', '').replace('Chapter6.', ''))


# Build the additions
NEW_ROWS = []  # (new_name, parent_cid, source_kind, source_name)

for parent_chap, zlist in zones_per_old_chap.items():
    cid = chap_chapid_new.get(parent_chap)
    if cid is None:
        print(f'  SKIP: zones in {parent_chap} (no ChapterID)')
        continue
    for zn in sorted(zlist):
        new_name = f'SandboxSmall-Chapter{cid:02d}.{short_zone(zn)}'
        NEW_ROWS.append((new_name, cid, 'zone', zn, parent_chap))

for ln in sorted(lm_hosts):
    primary = min(lm_hosts[ln], key=lambda x: chap_chapid_new.get(x, 99))
    cid = chap_chapid_new.get(primary)
    if cid is None:
        continue
    new_name = f'SandboxSmall-Chapter{cid:02d}.{short_lm(ln)}'
    NEW_ROWS.append((new_name, cid, 'landmark', ln, primary))

print(f'\nStep 3: Appending {len(NEW_ROWS)} new chapter rows')

# Need parent row by current renamed name for cloning
parent_by_name = {cd['Name']: cd for cd in chap['Exports'][0]['Table']['Data']}

added = 0
new_strings = []
existing_row_names = {cd['Name'] for cd in chap['Exports'][0]['Table']['Data']}
for new_name, cid, kind, source, parent_chap in NEW_ROWS:
    if new_name in existing_row_names:
        print(f'  skip (exists): {new_name}')
        continue
    parent = parent_by_name.get(parent_chap)
    if not parent:
        print(f'  SKIP {new_name}: parent {parent_chap} not found')
        continue
    clone = copy.deepcopy(parent)
    clone['Name'] = new_name

    # Update DisplayName StringTable key
    suffix = new_name.split('.', 1)[1]  # e.g. "Suburban_A_Westgate"
    st_key = f'Chapters.SandboxSmall.{suffix}'
    pretty_value = suffix.replace('_', ' ')
    new_strings.append((st_key, pretty_value))

    dn = fp(clone['Value'], 'DisplayName')
    if dn and 'TextPropertyData' in str(dn.get('$type', '')):
        dn['Value'] = st_key

    chap['Exports'][0]['Table']['Data'].append(clone)
    existing_row_names.add(new_name)
    added += 1

print(f'  Appended {added} new chapter rows')

# Step 4: Renamed level rows also need DisplayName updated to new StringTable key
print(f'\nStep 4: Update renamed level chapter DisplayName keys')
renamed_strings = []
for new_name in RENAMES.values():
    suffix = new_name.split('.', 1)[1]  # e.g. "Level1" or "Deep7"
    st_key = f'Chapters.SandboxSmall.{suffix}'
    pretty = suffix.replace('Level', 'Level ').replace('Deep', 'Deep ')
    renamed_strings.append((st_key, pretty))
    # Find the renamed chapter row and update its DisplayName
    for cd in chap['Exports'][0]['Table']['Data']:
        if cd['Name'] != new_name:
            continue
        dn = fp(cd['Value'], 'DisplayName')
        if dn and 'TextPropertyData' in str(dn.get('$type', '')):
            dn['Value'] = st_key
        break
print(f'  Updated {len(renamed_strings)} level DisplayName keys')

# Step 5: Add StringTable entries
print(f'\nStep 5: Adding StringTable entries')
all_new_keys = renamed_strings + new_strings
existing_st_keys = {entry[0] for entry in W['Exports'][0]['Table']['Value']
                    if isinstance(entry, list) and len(entry) >= 1}
added_st = 0
for k, v in all_new_keys:
    if k in existing_st_keys:
        continue
    W['Exports'][0]['Table']['Value'].append([k, v])
    existing_st_keys.add(k)
    added_st += 1
print(f'  Added {added_st} StringTable entries')

# Step 6: Sync NameMaps
print(f'\nStep 6: Sync NameMaps')


def add_nm(d, names):
    nm = d.get('NameMap', [])
    existing = set(nm)
    added = 0
    for n in names:
        if n is None:
            continue
        if n not in existing:
            nm.append(n)
            existing.add(n)
            added += 1
    d['NameMap'] = nm
    if 'NamesReferencedFromExportDataCount' in d:
        d['NamesReferencedFromExportDataCount'] = len(nm)
    exp0 = d['Exports'][0]
    if 'Generations' in exp0 and exp0['Generations']:
        exp0['Generations'][0]['NameCount'] = len(nm)
    return added


# Chapters NameMap: add all new chapter row names
new_chap_names = [new_name for new_name, _, _, _, _ in NEW_ROWS]
new_chap_names += list(RENAMES.values())
chap_added = add_nm(chap, new_chap_names)
print(f'  Chapters NameMap +{chap_added}')

# Zones NameMap: needs the new (renamed) chapter names since zones reference them
zone_added = add_nm(z, list(RENAMES.values()))
print(f'  Zones NameMap +{zone_added}')

# World NameMap: add the new StringTable keys
world_added = add_nm(W, [k for k, v in all_new_keys])
print(f'  World NameMap +{world_added}')

# Save
json.dump(chap, open(CHAP_PATH, 'w', encoding='utf-8'), indent=2)
json.dump(z, open(Z_PATH, 'w', encoding='utf-8'), indent=2)
json.dump(W, open(W_PATH, 'w', encoding='utf-8'), indent=2)
print('\nApplied.')
