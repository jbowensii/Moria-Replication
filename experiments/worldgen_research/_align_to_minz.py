"""Anchor every Live SS zone Position.Z, and every attached landmark
BasePosition.Z, to the host chapter's MinZ. Skip generator-placed
sentinel zones (Pos=(0,0,0)). Skip bridge zones (Moria-* chapters)."""
import json

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
def get_intvec_struct(prop):
    v = prop.get('Value') if prop else None
    if isinstance(v, list) and v:
        inner = v[0]
        if isinstance(inner, dict) and isinstance(inner.get('Value'), dict):
            return inner['Value']
    return None
def zoneset(r):
    p = fp(r.get('Value', []), 'ZoneSet')
    return str(p.get('Value','')).split('::')[-1] if p else None
def zstate(r):
    p = fp(r.get('Value', []), 'EnabledState')
    return str(p.get('Value','')).split('::')[-1] if p else None

z = json.load(open('DT_Moria_Zones.json'))
ch = json.load(open('DT_Moria_Chapters.json'))
lm = json.load(open('DT_Moria_Landmarks.json'))

# SS chapter MinZ map (skip bridges)
ss_minz = {}
for r in ch['Exports'][0]['Table']['Data']:
    if not r['Name'].startswith('SandboxSmall-chapter-'): continue
    if zstate(r) == 'Disabled': continue
    mn = get(r, 'MinZ')
    if isinstance(mn, int):
        ss_minz[r['Name']] = mn

# 1. Move zones whose Pos.Z != chapter MinZ (excluding sentinel and bridges)
zone_changes = []
zone_lm_pairs = []  # (zone_name, chap, mn, attached_landmark_names)
for r in z['Exports'][0]['Table']['Data']:
    if zoneset(r) != 'SandboxSmall' or zstate(r) == 'Disabled': continue
    chap = get(r, 'Chapter')
    if chap not in ss_minz: continue   # skip bridge zones
    mn = ss_minz[chap]
    pos_struct = get_intvec_struct(fp(r['Value'], 'Position'))
    if pos_struct is None: continue
    px, py, pz = pos_struct.get('X'), pos_struct.get('Y'), pos_struct.get('Z')
    # Skip generator-placed sentinel
    if (px, py, pz) == (0, 0, 0):
        # Still track landmarks for Step 2
        pass
    elif pz != mn:
        old = pz
        pos_struct['Z'] = mn
        zone_changes.append((r['Name'], chap, mn, old, mn))
    # Collect attached landmarks for Step 2
    lh = fp(r['Value'], 'LandmarkHandles')
    if lh:
        for e in (lh.get('Value') or []):
            if not isinstance(e, dict): continue
            inner = e.get('Value')
            if not isinstance(inner, list): continue
            lhprop = fp(inner, 'Landmark')
            if not lhprop: continue
            lv = lhprop.get('Value')
            if isinstance(lv, list):
                for it in lv:
                    if isinstance(it, dict) and it.get('Name') == 'RowName':
                        ln = it.get('Value', '')
                        if ln and ln != 'None':
                            zone_lm_pairs.append((r['Name'], chap, mn, ln))

json.dump(z, open('DT_Moria_Zones.json', 'w', encoding='utf-8'), indent=2)
print('Zones moved to chapter MinZ:')
for n, c, mn, oldz, newz in zone_changes:
    print('  ' + n + '  in ' + c + '  Pos.Z ' + str(oldz) + ' -> ' + str(newz))
print('Total zone moves:', len(zone_changes))

# 2. Move landmarks attached to Live SS zones (in SS chapters) to chapter MinZ
# Build deduped target set: landmark -> (target_minz, source_zone, source_chap)
needed = {}
for zn, chap, mn, ln in zone_lm_pairs:
    if ln not in needed:
        needed[ln] = (mn, zn, chap)

lm_changes = []
for r in lm['Exports'][0]['Table']['Data']:
    if r['Name'] not in needed: continue
    mn, zn, chap = needed[r['Name']]
    bp = get_intvec_struct(fp(r['Value'], 'BasePosition'))
    if bp is None: continue
    cur_z = bp.get('Z')
    if cur_z is None: continue
    if cur_z != mn:
        bp['Z'] = mn
        lm_changes.append((r['Name'], cur_z, mn, zn, chap))

json.dump(lm, open('DT_Moria_Landmarks.json', 'w', encoding='utf-8'), indent=2)
print('\nLandmarks moved to host chapter MinZ:')
for ln, oldz, newz, zn, chap in lm_changes:
    print('  ' + ln + '  Z ' + str(oldz) + ' -> ' + str(newz) + '  (host: ' + zn + ' in ' + chap + ')')
print('Total landmark moves:', len(lm_changes))
