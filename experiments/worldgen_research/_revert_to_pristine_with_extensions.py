"""Revert sandbox zones + landmarks to pristine, but keep our 14-chapter
structure (with the 6 new Layer extensions empty)."""
import json, copy
from pathlib import Path

HERE = Path(__file__).parent
ZP = HERE / 'DT_Moria_Zones.json'
LP = HERE / 'DT_Moria_Landmarks.json'
CP = HERE / 'DT_Moria_Chapters.json'

z_cur = json.loads(ZP.read_text(encoding='utf-8'))
z_pri = json.loads((HERE / 'DT_Moria_Zones.original.json').read_text(encoding='utf-8'))
l_cur = json.loads(LP.read_text(encoding='utf-8'))
l_pri = json.loads((HERE / 'DT_Moria_Landmarks.original.json').read_text(encoding='utf-8'))
ch_cur = json.loads(CP.read_text(encoding='utf-8'))
ch_pri = json.loads((HERE / 'DT_Moria_Chapters.original.json').read_text(encoding='utf-8'))


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


def set_rowname(prop, new):
    for it in prop.get('Value', []) or []:
        if isinstance(it, dict) and it.get('Name') == 'RowName':
            it['Value'] = new
            return


# ============================================================================
# STEP 1: Build pristine -> current chapter name map by Layer
# ============================================================================
prist_layer_to_cur = {}
for r in ch_cur['Exports'][0]['Table']['Data']:
    if not r['Name'].startswith('SandboxSmall-chapter-'):
        continue
    L = get(r, 'Layer')
    if L is not None:
        prist_layer_to_cur[L] = r['Name']

prist_to_cur = {}  # pristine chapter name -> current chapter name
for pr in ch_pri['Exports'][0]['Table']['Data']:
    if not pr['Name'].startswith('SandboxSmall-chapter-'):
        continue
    L = get(pr, 'Layer')
    if L in prist_layer_to_cur:
        prist_to_cur[pr['Name']] = prist_layer_to_cur[L]

print('=== Chapter mapping (pristine -> current via Layer) ===')
for k, v in sorted(prist_to_cur.items()):
    print(f'  {k:32s} -> {v}')


# ============================================================================
# STEP 2: Revert zones — restore pristine + delete added
# ============================================================================
zone_pri_by = {r['Name']: r for r in z_pri['Exports'][0]['Table']['Data']}
zone_cur_by = {r['Name']: r for r in z_cur['Exports'][0]['Table']['Data']}

added_zones = sorted(set(zone_cur_by) - set(zone_pri_by))
removed_zones = sorted(set(zone_pri_by) - set(zone_cur_by))  # should be empty
common_zones = sorted(set(zone_cur_by) & set(zone_pri_by))

print(f'\n=== Zones: {len(added_zones)} to delete, {len(common_zones)} to restore ===')

new_zone_rows = []
for r in z_cur['Exports'][0]['Table']['Data']:
    if r['Name'] in added_zones:
        print(f'  DELETE: {r["Name"]}')
        continue
    # Replace with pristine copy
    pristine_row = zone_pri_by[r['Name']]
    fresh = copy.deepcopy(pristine_row)
    # Remap Chapter via prist_to_cur lookup
    chprop = fp(fresh['Value'], 'Chapter')
    if chprop:
        old_chap = ''
        for it in (chprop.get('Value') or []):
            if isinstance(it, dict) and it.get('Name') == 'RowName':
                old_chap = it.get('Value', '')
                if old_chap in prist_to_cur:
                    it['Value'] = prist_to_cur[old_chap]
    # AdditionalChapters too
    ac = fp(fresh['Value'], 'AdditionalChapters')
    if ac:
        for it in (ac.get('Value') or []):
            for sub in (it.get('Value') or []):
                if isinstance(sub, dict) and sub.get('Name') == 'RowName':
                    v = sub.get('Value', '')
                    if v in prist_to_cur:
                        sub['Value'] = prist_to_cur[v]
    new_zone_rows.append(fresh)

z_cur['Exports'][0]['Table']['Data'] = new_zone_rows

# Strip zone NameMap entries that we added (only the new-zone names)
znm = z_cur.get('NameMap', [])
znm = [s for s in znm if s not in added_zones]
z_cur['NameMap'] = znm

ZP.write_text(json.dumps(z_cur, indent=2), encoding='utf-8')
print(f'\n  Final zone count: {len(new_zone_rows)} (pristine has {len(z_pri["Exports"][0]["Table"]["Data"])})')


# ============================================================================
# STEP 3: Revert landmarks
# ============================================================================
lm_pri_by = {r['Name']: r for r in l_pri['Exports'][0]['Table']['Data']}
lm_cur_by = {r['Name']: r for r in l_cur['Exports'][0]['Table']['Data']}
added_lm = sorted(set(lm_cur_by) - set(lm_pri_by))
common_lm = sorted(set(lm_cur_by) & set(lm_pri_by))

print(f'\n=== Landmarks: {len(added_lm)} to delete, {len(common_lm)} to restore from pristine ===')

new_lm_rows = []
for r in l_cur['Exports'][0]['Table']['Data']:
    if r['Name'] in added_lm:
        print(f'  DELETE: {r["Name"]}')
        continue
    # Replace entire row with pristine
    new_lm_rows.append(copy.deepcopy(lm_pri_by[r['Name']]))

l_cur['Exports'][0]['Table']['Data'] = new_lm_rows

lnm = l_cur.get('NameMap', [])
lnm = [s for s in lnm if s not in added_lm
       and not s.startswith('Landmarks.Sandbox.Sixth')
       and not s.startswith('Landmarks.Sandbox.Seventh')
       and not s.startswith('Landmarks.Sandbox.Eighth')
       and not s.startswith('Landmarks.Sandbox.Tenth')
       and not s.startswith('Landmarks.Sandbox.Twelfth')
       and not s.startswith('Landmarks.Sandbox.Fourteenth')
       and not s.startswith('Landmarks.Sandbox.Eleventh')
       and not s.startswith('World.Landmark.Sandbox.Sixth')
       and not s.startswith('World.Landmark.Sandbox.Seventh')
       and not s.startswith('World.Landmark.Sandbox.Eighth')
       and not s.startswith('World.Landmark.Sandbox.Tenth')
       and not s.startswith('World.Landmark.Sandbox.Twelfth')
       and not s.startswith('World.Landmark.Sandbox.Fourteenth')
       and not s.startswith('World.Landmark.Sandbox.Eleventh')]
l_cur['NameMap'] = lnm

LP.write_text(json.dumps(l_cur, indent=2), encoding='utf-8')
print(f'\n  Final landmark count: {len(new_lm_rows)} (pristine has {len(l_pri["Exports"][0]["Table"]["Data"])})')


# ============================================================================
# STEP 4: Restore pristine chapter heights for the 8 pristine-layer chapters,
#         keep current heights for the 6 new-layer chapters, recompute Z + PrimeZ
# ============================================================================
print('\n=== Restoring chapter heights + recomputing Z bands ===')

# Pristine heights by Layer
prist_h_by_layer = {}
for pr in ch_pri['Exports'][0]['Table']['Data']:
    if not pr['Name'].startswith('SandboxSmall-chapter-'):
        continue
    L = get(pr, 'Layer')
    minz = get(pr, 'MinZ')
    maxz = get(pr, 'MaxZ')
    if L is not None and minz is not None and maxz is not None:
        prist_h_by_layer[L] = maxz - minz + 1

# Current heights by Layer (for layers without pristine equivalent)
cur_h_by_layer = {}
for r in ch_cur['Exports'][0]['Table']['Data']:
    if not r['Name'].startswith('SandboxSmall-chapter-'):
        continue
    L = get(r, 'Layer')
    minz = get(r, 'MinZ')
    maxz = get(r, 'MaxZ')
    if L is not None and minz is not None and maxz is not None:
        cur_h_by_layer[L] = maxz - minz + 1

# Final height per Layer
final_h_by_layer = {}
for L in sorted(cur_h_by_layer.keys()):
    if L in prist_h_by_layer:
        final_h_by_layer[L] = prist_h_by_layer[L]
        if final_h_by_layer[L] != cur_h_by_layer[L]:
            print(f'  Layer {L:+d}: height {cur_h_by_layer[L]} -> {prist_h_by_layer[L]} (revert to pristine)')
    else:
        final_h_by_layer[L] = cur_h_by_layer[L]
        print(f'  Layer {L:+d}: keep height {cur_h_by_layer[L]} (new layer)')

# Recompute Z bands contiguously bottom-up
sorted_layers = sorted(final_h_by_layer.keys())  # most-negative first
new_zbands = {}
zcur = 1
for L in sorted_layers:
    h = final_h_by_layer[L]
    minz = zcur
    maxz = zcur + h - 1
    pz = (minz + maxz) // 2
    new_zbands[L] = (minz, maxz, pz)
    zcur = maxz + 1

# Apply to chapters
def setv(r, k, v):
    p = fp(r['Value'], k)
    if p is not None:
        p['Value'] = v

for r in ch_cur['Exports'][0]['Table']['Data']:
    if not r['Name'].startswith('SandboxSmall-chapter-'):
        continue
    L = get(r, 'Layer')
    if L not in new_zbands:
        continue
    minz, maxz, pz = new_zbands[L]
    setv(r, 'MinZ', minz)
    setv(r, 'MaxZ', maxz)
    setv(r, 'PrimeZ', pz)

CP.write_text(json.dumps(ch_cur, indent=2), encoding='utf-8')

print('\n=== New Z-band stack (top to bottom) ===')
for L in reversed(sorted_layers):
    minz, maxz, pz = new_zbands[L]
    h = final_h_by_layer[L]
    cn = prist_layer_to_cur[L]
    lvl = int(cn.split('-')[-1])
    note = ''
    if L == 0:
        note = '  (GROUND)'
    elif L > 0:
        note = f'  ({L} above)'
    else:
        note = f'  ({-L} below — Deep{-L})'
    new_marker = '  NEW' if L not in prist_h_by_layer else ''
    print(f'  Layer {L:>+3}  Lv-{lvl:<2}  Z={minz:>3}..{maxz:<3}  h={h}  PrimeZ={pz}{note}{new_marker}')


print('\n=== Done ===')
print('Zones reverted to pristine. Landmarks reverted. Chapter heights restored.')
print('Empty layers (new): +4, +5, +6, -5, -6, -7 — no zones, no stairs to reach them.')
