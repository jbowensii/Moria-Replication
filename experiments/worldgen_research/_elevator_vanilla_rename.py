"""Delete disabled elevator zones, rename active 6 to vanilla letter pattern,
reassign landmarks, restore crystal-descent bubbles on FourthStair/FifthStair.

Rename plan (avoids collisions by ordering):
  G  -> D   (Lv-5 stair, host ThirdStair)
  E  -> G   (D-5 stair, host SixthStair)
  M  -> E   (D-7 crystal descent, host FourthStair)
  K  -> C   (D-3 stair, host SecondStair)
  B  -> B   (no change)
  F  -> F   (no change)

Landmark bubble fixes:
  Sandbox.FourthStair   -> BB_Sandbox_CrystalDescent  (vanilla pattern)
  Sandbox.FifthStair    -> BB_Sandbox_CrystalDescent  (vanilla pattern)
"""
import json

DELETE_ZONES = {
    'Sandbox_Small_Elevator_C',
    'Sandbox_Small_Elevator_D',
    'Sandbox_Small_Elevator_H',
    'Sandbox_Small_Elevator_I',
    'Sandbox_Small_Elevator_J',
    'Sandbox_Small_Elevator_L',
}

# (old_zone_name, new_zone_name, new_landmark_rowname, new_bubble_for_landmark)
RENAMES = [
    ('Sandbox_Small_Elevator_G', 'Sandbox_Small_Elevator_D', 'Sandbox.ThirdStair',  'BB_Sandbox_Elevator_Urban'),
    ('Sandbox_Small_Elevator_E', 'Sandbox_Small_Elevator_G', 'Sandbox.SixthStair',  'BB_Sandbox_Elevator_Urban'),
    ('Sandbox_Small_Elevator_M', 'Sandbox_Small_Elevator_E', 'Sandbox.FourthStair', 'BB_Sandbox_CrystalDescent'),
    ('Sandbox_Small_Elevator_K', 'Sandbox_Small_Elevator_C', 'Sandbox.SecondStair', 'BB_Sandbox_Elevator_Urban'),
    ('Sandbox_Small_Elevator_B', 'Sandbox_Small_Elevator_B', 'Sandbox.FirstStair',  'BB_Sandbox_Elevator_Urban'),
    ('Sandbox_Small_Elevator_F', 'Sandbox_Small_Elevator_F', 'Sandbox.FifthStair',  'BB_Sandbox_CrystalDescent'),
]


def fp(v, n):
    for p in v or []:
        if isinstance(p, dict) and p.get('Name') == n:
            return p
    return None


# Load
z = json.load(open('DT_Moria_Zones.json', encoding='utf-8'))
ch = json.load(open('DT_Moria_Chapters.json', encoding='utf-8'))
lm = json.load(open('DT_Moria_Landmarks.json', encoding='utf-8'))

# === STEP 1: Delete disabled zone rows ===
zrows = z['Exports'][0]['Table']['Data']
deleted_zones = []
new_zrows = []
for r in zrows:
    if r['Name'] in DELETE_ZONES:
        deleted_zones.append(r['Name'])
        continue
    new_zrows.append(r)
z['Exports'][0]['Table']['Data'] = new_zrows
print(f'Deleted {len(deleted_zones)} disabled zone rows: {deleted_zones}')

# === STEP 2: Delete anchored chapter rows for deleted elevators ===
# Anchored row name format: SandboxSmall-Chapter##.<ZoneShortName>
deleted_short_names = {n.replace('Sandbox_Small_', '').replace('Sandbox_', '')
                       for n in deleted_zones}
crows = ch['Exports'][0]['Table']['Data']
new_crows = []
deleted_chap = []
for r in crows:
    n = r['Name']
    if not n.startswith('SandboxSmall-Chapter'):
        new_crows.append(r); continue
    tail = n.split('.', 1)[1] if '.' in n else ''
    if tail in deleted_short_names:
        deleted_chap.append(n)
        continue
    new_crows.append(r)
ch['Exports'][0]['Table']['Data'] = new_crows
print(f'Deleted {len(deleted_chap)} anchored chapter rows: {deleted_chap}')

# === STEP 3: Rename active zones (using temp names to avoid collisions) ===

# Build mapping old -> new (skipping no-change entries)
RENAME_MAP = {old: new for old, new, _, _ in RENAMES if old != new}

# Use temp prefix so target letters don't clash mid-rename
TEMP_PREFIX = 'Sandbox_Small_TEMP_RENAME_'

# Phase A: rename to temp
zrows = z['Exports'][0]['Table']['Data']
for r in zrows:
    if r['Name'] in RENAME_MAP:
        new_temp = TEMP_PREFIX + r['Name'].replace('Sandbox_Small_Elevator_', '')
        r['_pending_new'] = RENAME_MAP[r['Name']]
        r['Name'] = new_temp

# Phase B: rename from temp to final
for r in zrows:
    pending = r.get('_pending_new')
    if pending:
        r['Name'] = pending
        del r['_pending_new']
        print(f'  Renamed zone -> {pending}')

# === STEP 4: Update anchored chapter row names to match new zone names ===
# For each kept active elevator, find its anchored chapter row and rename suffix
# We need to find the OLD anchored row first (by old short name), then rename
# both the row's Name AND any zone's Chapter field that points to it.

OLD_TO_NEW_SHORT = {}
for old, new, _, _ in RENAMES:
    old_short = old.replace('Sandbox_Small_', '').replace('Sandbox_', '')
    new_short = new.replace('Sandbox_Small_', '').replace('Sandbox_', '')
    if old_short != new_short:
        OLD_TO_NEW_SHORT[old_short] = new_short

# Build chapter rename map (old chapter rowname -> new chapter rowname)
CHAP_RENAME_MAP = {}
crows = ch['Exports'][0]['Table']['Data']
for r in crows:
    n = r['Name']
    if not n.startswith('SandboxSmall-Chapter'): continue
    if '.' not in n: continue
    prefix, tail = n.split('.', 1)
    if tail in OLD_TO_NEW_SHORT:
        new_n = f'{prefix}.{OLD_TO_NEW_SHORT[tail]}'
        CHAP_RENAME_MAP[n] = new_n
        r['Name'] = new_n
        print(f'  Renamed chapter row {n} -> {new_n}')

# Update zone Chapter refs that point to renamed chapter rows
for r in z['Exports'][0]['Table']['Data']:
    cprop = fp(r['Value'], 'Chapter')
    if not cprop: continue
    val = cprop.get('Value')
    if isinstance(val, list):
        for it in val:
            if isinstance(it, dict) and it.get('Name') == 'RowName':
                old = it.get('Value')
                if old in CHAP_RENAME_MAP:
                    it['Value'] = CHAP_RENAME_MAP[old]

# === STEP 5: Reassign landmarks on each renamed zone ===
for old_zone, new_zone, new_landmark, _ in RENAMES:
    target_zone = new_zone  # current name in data
    for r in z['Exports'][0]['Table']['Data']:
        if r['Name'] != target_zone: continue
        lh = fp(r['Value'], 'LandmarkHandles')
        if not lh: continue
        # Update first LandmarkHandle entry (the primary stair landmark)
        for e in (lh.get('Value') or [])[:1]:
            for sub in e.get('Value') or []:
                if isinstance(sub, dict) and sub.get('Name') == 'Landmark':
                    lv = sub.get('Value')
                    if isinstance(lv, list):
                        for it in lv:
                            if isinstance(it, dict) and it.get('Name') == 'RowName':
                                old = it.get('Value')
                                it['Value'] = new_landmark
                                print(f'  Zone {target_zone} landmark: {old} -> {new_landmark}')

# === STEP 6: Restore FourthStair and FifthStair landmark bubble to crystal ===
for r in lm['Exports'][0]['Table']['Data']:
    if r['Name'] in ('Sandbox.FourthStair', 'Sandbox.FifthStair'):
        bp = fp(r['Value'], 'BaseBubbleName')
        if bp:
            old = bp.get('Value')
            bp['Value'] = 'BB_Sandbox_CrystalDescent'
            print(f'  Landmark {r["Name"]} BaseBubbleName: {old} -> BB_Sandbox_CrystalDescent')

# === STEP 7: Sync NameMaps and counters ===
def sync_nm(d, *, add=(), remove=()):
    nm = d.get('NameMap', [])
    s = set(nm); changed = False
    for n in remove:
        if n in s:
            nm.remove(n); s.discard(n); changed = True
    for n in add:
        if n and n not in s:
            nm.append(n); s.add(n); changed = True
    if changed:
        d['NameMap'] = nm
        if 'NamesReferencedFromExportDataCount' in d:
            d['NamesReferencedFromExportDataCount'] = len(nm)
        exp0 = d['Exports'][0]
        if 'Generations' in exp0 and exp0['Generations']:
            exp0['Generations'][0]['NameCount'] = len(nm)
    return changed

# Add new zone names + chapter row names to NameMaps
new_zone_names = [new for old, new, _, _ in RENAMES if old != new]
new_chap_names = list(CHAP_RENAME_MAP.values())
sync_nm(z, add=new_zone_names + new_chap_names, remove=list(DELETE_ZONES))
sync_nm(ch, add=new_chap_names, remove=deleted_chap)

# Save
json.dump(z, open('DT_Moria_Zones.json', 'w', encoding='utf-8'), indent=2)
json.dump(ch, open('DT_Moria_Chapters.json', 'w', encoding='utf-8'), indent=2)
json.dump(lm, open('DT_Moria_Landmarks.json', 'w', encoding='utf-8'), indent=2)

# === Verify ===
print('\n=== Final state — active stair zones ===')
for r in z['Exports'][0]['Table']['Data']:
    n = r['Name']
    if not n.startswith('Sandbox_Small_Elevator_'): continue
    es = fp(r['Value'], 'EnabledState')
    state = str(es.get('Value', '')).split('::')[-1] if es else ''
    cprop = fp(r['Value'], 'Chapter')
    chap = '?'
    if cprop:
        for it in cprop.get('Value') or []:
            if isinstance(it, dict) and it.get('Name') == 'RowName':
                chap = it.get('Value')
    lh = fp(r['Value'], 'LandmarkHandles')
    lname = ''
    for e in (lh.get('Value') or []) if lh else []:
        for sub in e.get('Value') or []:
            if isinstance(sub, dict) and sub.get('Name') == 'Landmark':
                lv = sub.get('Value')
                if isinstance(lv, list):
                    for it in lv:
                        if isinstance(it, dict) and it.get('Name') == 'RowName':
                            lname = it.get('Value')
        break
    print(f'  {n:<32} chap={chap:<48} landmark={lname:<28} state={state}')

print('\nSaved.')
