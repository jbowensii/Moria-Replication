"""Post-rename verification: reference integrity, stair catalog, chapter-prefix audit."""
import json, re
from pathlib import Path

ROOT = Path(__file__).parent

def load(name):
    with open(ROOT / name, 'r', encoding='utf-8') as f:
        return json.load(f)

Z = load('DT_Moria_Zones.json')
LM = load('DT_Moria_Landmarks.json')
LC = load('DT_Moria_LayoutConnections.json')
CH = load('DT_Moria_Chapters.json')

zrows = Z['Exports'][0]['Table']['Data']
lmrows = LM['Exports'][0]['Table']['Data']
lcrows = LC['Exports'][0]['Table']['Data']
chrows = CH['Exports'][0]['Table']['Data']

def get_prop(row, name):
    for v in row.get('Value',[]):
        if v.get('Name') == name: return v
    return None

def get_value(row, name):
    p = get_prop(row, name)
    return p.get('Value') if p else None

def get_handle_rowname(row, prop_name):
    p = get_prop(row, prop_name)
    if not p: return None
    for sub in p.get('Value', []):
        if sub.get('Name') == 'RowName':
            return sub.get('Value')
    return None

def get_chapter(zrow):
    return get_handle_rowname(zrow, 'Chapter')

def get_landmark_refs(zrow):
    p = get_prop(zrow, 'LandmarkHandles')
    if not p: return []
    refs = []
    for entry in p.get('Value', []):
        for sub in entry.get('Value', []):
            if sub.get('Name') == 'Landmark':
                for nn in sub.get('Value', []):
                    if nn.get('Name') == 'RowName':
                        refs.append(nn.get('Value'))
    return refs

def get_extconn_lm(zrow):
    p = get_prop(zrow, 'LandmarkHandles')
    if not p: return []
    out = []
    for entry in p.get('Value', []):
        is_ext = False
        lm_name = None
        for sub in entry.get('Value', []):
            if sub.get('Name') == 'Landmark':
                for nn in sub.get('Value', []):
                    if nn.get('Name') == 'RowName':
                        lm_name = nn.get('Value')
            elif sub.get('Name') == 'bExtendedConnectivityLandmark':
                if sub.get('Value') is True:
                    is_ext = True
        if is_ext and lm_name:
            out.append(lm_name)
    return out

# Build sets
landmark_names = {r.get('Name') for r in lmrows}
lm_by_name = {r.get('Name'): r for r in lmrows}
zone_by_name = {r.get('Name'): r for r in zrows}

def get_enabled(row):
    return get_value(row, 'EnabledState')

# ---- 1. Reference integrity ----
print('=' * 70)
print('REFERENCE INTEGRITY AUDIT')
print('=' * 70)

# Live LayoutConnections
broken_lc = []
for r in lcrows:
    en = get_enabled(r)
    if en == 'ERowEnabledState::Disabled': continue
    name = r.get('Name','')
    o_lm = get_handle_rowname(r, 'OriginLandmark')
    d_lm = get_handle_rowname(r, 'DestinationLandmark')
    if o_lm and o_lm != 'None' and o_lm not in landmark_names:
        broken_lc.append((name, 'OriginLandmark', o_lm))
    if d_lm and d_lm != 'None' and d_lm not in landmark_names:
        broken_lc.append((name, 'DestinationLandmark', d_lm))
print(f'\nLive LayoutConnection broken refs: {len(broken_lc)}')
for x in broken_lc:
    print(f'  {x}')

# Live Zone landmark handles
broken_zlh = []
for r in zrows:
    en = get_enabled(r)
    if en == 'ERowEnabledState::Disabled': continue
    name = r.get('Name','')
    chap = get_chapter(r)
    if not chap or 'SandboxSmall' not in chap: continue  # only check live SS
    for lm in get_landmark_refs(r):
        if lm and lm != 'None' and lm not in landmark_names:
            broken_zlh.append((name, lm))
print(f'\nLive SS Zone landmark handle broken refs: {len(broken_zlh)}')
for x in broken_zlh:
    print(f'  {x}')

# Sandbox_Small_Chain_* connections
chain_lcs = [r for r in lcrows if r.get('Name','').startswith('Sandbox_Small_Chain_')
             and get_enabled(r) != 'ERowEnabledState::Disabled']
print(f'\nLive Sandbox_Small_Chain_* connections: {len(chain_lcs)}')
for r in chain_lcs:
    name = r.get('Name','')
    o_lm = get_handle_rowname(r, 'OriginLandmark')
    d_lm = get_handle_rowname(r, 'DestinationLandmark')
    o_ok = (o_lm == 'None') or (o_lm in landmark_names)
    d_ok = (d_lm == 'None') or (d_lm in landmark_names)
    print(f'  {name}: O={o_lm} ({"OK" if o_ok else "BROKEN"}), D={d_lm} ({"OK" if d_ok else "BROKEN"})')

# References to old stair names anywhere?
old_stair_names = ['Sandbox.Lv3Lv4Connector','Sandbox.TopElevator','Chapter3.CrystalDescent',
    'Sandbox.D7D6Stair','Sandbox.DeepBottomEl','Sandbox.D4D3Connector','Sandbox.DeepMidEl',
    'Sandbox.DeepUpperEl','Sandbox.D1Lv1Connector']
print('\nLeft-over refs to renamed-away stair landmarks:')
for old in old_stair_names:
    refs = []
    # zones
    for r in zrows:
        if old in get_landmark_refs(r):
            refs.append(('zone', r.get('Name')))
    # LCs
    for r in lcrows:
        if get_handle_rowname(r, 'OriginLandmark') == old or get_handle_rowname(r, 'DestinationLandmark') == old:
            refs.append(('lc', r.get('Name')))
    print(f'  {old}: {len(refs)} refs {refs[:3]}')

# References that point to Sandbox.SecondStair etc (these are now valid for our new stairs, but ensure no _disabled_vanilla_ collision)
print('\nLeft-over refs to renamed-out vanilla disabled stair names:')
old_vanilla = ['Sandbox._disabled_vanilla_SecondStair','Sandbox._disabled_vanilla_ThirdStair',
    'Sandbox._disabled_vanilla_FourthStair','Sandbox._disabled_vanilla_FifthStair']
for nm in old_vanilla:
    refs = []
    for r in zrows:
        if nm in get_landmark_refs(r):
            refs.append(('zone', r.get('Name')))
    for r in lcrows:
        if get_handle_rowname(r,'OriginLandmark') == nm or get_handle_rowname(r,'DestinationLandmark') == nm:
            refs.append(('lc', r.get('Name')))
    print(f'  {nm}: {len(refs)} refs {refs[:3]}')

# ---- 2. Stair catalog ----
print('\n' + '=' * 70)
print('STAIR CATALOG POST-RENAME')
print('=' * 70)

stair_zone_to_lm = {
    'Sandbox_Small_Elevator_B':       'Sandbox.FirstStair',
    'Sandbox_Small_Lv3Lv4Connector':  'Sandbox.FifthStair',
    'Sandbox_Small_TopElevator':      'Sandbox.SeventhStair',
    'Sandbox_Small_CrystalDescent':   'Sandbox.FourteenthStair',
    'Sandbox_Small_D7D6Stair':        'Sandbox.TwelfthStair',
    'Sandbox_Small_DeepBottomEl':     'Sandbox.TenthStair',
    'Sandbox_Small_D4D3Connector':    'Sandbox.EighthStair',
    'Sandbox_Small_DeepMidEl':        'Sandbox.SixthStair',
    'Sandbox_Small_DeepUpperEl':      'Sandbox.FourthStair',
    'Sandbox_Small_D1Lv1Connector':   'Sandbox.SecondStair',
}

def get_landmark_pos(lm_name):
    r = lm_by_name.get(lm_name)
    if not r: return None
    p = get_prop(r, 'BasePosition')
    if not p: return None
    coords = {}
    for v in p.get('Value', []):
        if v.get('Name') in ('X','Y','Z'):
            coords[v['Name']] = v.get('Value')
    return coords

print('\nStair zone -> landmark (extended connectivity check):')
chap_stairs = {}
for zname, expected_lm in stair_zone_to_lm.items():
    z = zone_by_name.get(zname)
    if not z:
        print(f'  {zname}: ZONE MISSING')
        continue
    ext_lms = get_extconn_lm(z)
    chap = get_chapter(z)
    pos = get_landmark_pos(expected_lm)
    has_ext = expected_lm in ext_lms
    print(f'  {zname} (chap={chap}): ext_lm includes {expected_lm}? {has_ext}; pos={pos}')
    if has_ext:
        chap_stairs.setdefault(chap, []).append(zname)

print('\nchapter_stair_uniqueness (stair zones per Live SS chapter):')
for chap, zns in sorted(chap_stairs.items()):
    flag = ' OK' if len(zns) == 1 else ' WARN multiple'
    print(f'  {chap}: {zns}{flag}')

# ---- 3. Chapter-prefix audit ----
print('\n' + '=' * 70)
print('CHAPTER-PREFIX AUDIT')
print('=' * 70)

# Build lm -> live SS hosts
lm_hosts = {}
for zr in zrows:
    en = get_enabled(zr)
    if en == 'ERowEnabledState::Disabled': continue
    chap = get_chapter(zr)
    if not chap or 'SandboxSmall' not in chap: continue
    for lm in get_landmark_refs(zr):
        lm_hosts.setdefault(lm, []).append((zr.get('Name'), chap))

print('\nChapterN.* landmarks remaining and their hosts:')
for r in lmrows:
    name = r.get('Name','')
    m = re.match(r'^Chapter(\d+)\.', name)
    if not m: continue
    prefix_n = int(m.group(1))
    hosts = lm_hosts.get(name, [])
    if hosts:
        host_chaps = set()
        for _, chap in hosts:
            cm = re.search(r'chapter-(\d+)', chap)
            if cm: host_chaps.add(int(cm.group(1)))
        match = (prefix_n in host_chaps)
        print(f'  {name}: hosts={hosts} prefix_n={prefix_n} match={match}')
    else:
        print(f'  {name}: NO LIVE SS HOST (untouched)')
