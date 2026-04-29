"""Add Sandbox.EighthStair (Urban bubble) to ch11 so Lv-11<->Lv-10 has
a non-CrystalDescent stair option."""
import json, copy
from pathlib import Path

HERE = Path(__file__).parent
ZP = HERE / 'DT_Moria_Zones.json'
LP = HERE / 'DT_Moria_Landmarks.json'
CP = HERE / 'DT_Moria_Chapters.json'

z = json.loads(ZP.read_text(encoding='utf-8'))
lm = json.loads(LP.read_text(encoding='utf-8'))
ch = json.loads(CP.read_text(encoding='utf-8'))


def fp(v, n):
    for p in v or []:
        if isinstance(p, dict) and p.get('Name') == n:
            return p
    return None


def set_rowname(prop, new):
    for it in prop.get('Value', []) or []:
        if isinstance(it, dict) and it.get('Name') == 'RowName':
            it['Value'] = new
            return


def setv(prop, x, y, zv):
    for it in (prop.get('Value') or []):
        if isinstance(it, dict):
            v = it.get('Value')
            if isinstance(v, dict) and 'X' in v:
                v['X'] = int(x); v['Y'] = int(y); v['Z'] = int(zv)
                return


def chap_minz(name):
    for r in ch['Exports'][0]['Table']['Data']:
        if r['Name'] == name:
            mz = fp(r['Value'], 'MinZ')
            return mz.get('Value') if mz else None
    return None


NEW_ZONE = 'Sandbox_Small_Elevator_I'
NEW_LM   = 'Sandbox.EighthStair'
CHAPTER  = 'SandboxSmall-chapter-11'

ch11_minz = chap_minz(CHAPTER)
print(f'ch11 MinZ = {ch11_minz}')

# Templates
elevator_B = next(r for r in z['Exports'][0]['Table']['Data']
                   if r['Name'] == 'Sandbox_Small_Elevator_B')
firstStair = next(r for r in lm['Exports'][0]['Table']['Data']
                   if r['Name'] == 'Sandbox.FirstStair')

# --- 1. Create new zone ---
zone_rows = z['Exports'][0]['Table']['Data']
zone_by = {r['Name']: r for r in zone_rows}
if NEW_ZONE in zone_by:
    print(f'{NEW_ZONE} already exists')
else:
    new_zone = copy.deepcopy(elevator_B)
    new_zone['Name'] = NEW_ZONE
    set_rowname(fp(new_zone['Value'], 'Chapter'), CHAPTER)
    setv(fp(new_zone['Value'], 'Position'), 0, 12, ch11_minz)
    # Rewrite LH entry to host the new stair landmark
    lh = fp(new_zone['Value'], 'LandmarkHandles')
    if lh and lh.get('Value'):
        tpl = copy.deepcopy(lh['Value'][0])
        for sub in (tpl.get('Value') or []):
            if not isinstance(sub, dict):
                continue
            n = sub.get('Name')
            if n == 'Landmark':
                set_rowname(sub, NEW_LM)
            elif n == 'Placement':
                cur = sub.get('Value', '')
                pref = cur.split('::', 1)[0] if '::' in cur else 'EZoneBubblePlacement'
                sub['Value'] = f'{pref}::Fixed'
            elif n == 'bExtendedConnectivityLandmark':
                sub['Value'] = True
        lh['Value'] = [tpl]
        lh.pop('DummyStruct', None)
    zone_rows.append(new_zone)
    print(f'Created zone {NEW_ZONE} in {CHAPTER}, Pos=(0,12,{ch11_minz}), Size=(6,6,4)')

# --- 2. Create new landmark ---
lm_rows = lm['Exports'][0]['Table']['Data']
lm_by = {r['Name']: r for r in lm_rows}
if NEW_LM in lm_by:
    print(f'{NEW_LM} already exists')
else:
    new_lm = copy.deepcopy(firstStair)
    new_lm['Name'] = NEW_LM
    # Bubble: keep BB_Sandbox_Elevator_Urban inherited from FirstStair (Urban, not Crystal)
    dp = fp(new_lm['Value'], 'DisplayName')
    if dp:
        dp['Value'] = f'Landmarks.{NEW_LM}'
    gc = fp(new_lm['Value'], 'GuaranteedConnections')
    if gc and gc.get('Value'):
        if 'DummyStruct' not in gc:
            gc['DummyStruct'] = copy.deepcopy(gc['Value'][0])
        gc['Value'] = []
    lm_rows.append(new_lm)
    print(f'Created landmark {NEW_LM}  (clone of FirstStair, Urban bubble, GC cleared)')

# --- 3. NameMaps ---
znm = z.get('NameMap', [])
for s in (NEW_ZONE, NEW_LM):
    if s not in znm:
        znm.append(s)
z['NameMap'] = znm

lnm = lm.get('NameMap', [])
for s in (NEW_LM, f'Landmarks.{NEW_LM}'):
    if s not in lnm:
        lnm.append(s)
lm['NameMap'] = lnm

ZP.write_text(json.dumps(z, indent=2), encoding='utf-8')
LP.write_text(json.dumps(lm, indent=2), encoding='utf-8')
print()
print('Saved.')
