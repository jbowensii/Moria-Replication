"""Fill the Lv-4<->Lv-5 gap with a 7th Stair (odd = up per rule).
Host in ch5 (Layer+4, Z=35..38, h=4) so the 4-floor elevator fits cleanly.
Uses SB_Elevator_J as next available letter. Vanilla has the string
'Ninth Stair' pre-registered for J — we overwrite to 'Seventh Stair' since
the interleaved numbering puts the 7th stair here."""
import json, copy
from pathlib import Path

HERE = Path(__file__).parent
ZP = HERE / 'DT_Moria_Zones.json'
LP = HERE / 'DT_Moria_Landmarks.json'
CP = HERE / 'DT_Moria_Chapters.json'
WP = HERE / 'World.json'

z  = json.loads(ZP.read_text(encoding='utf-8'))
lm = json.loads(LP.read_text(encoding='utf-8'))
ch = json.loads(CP.read_text(encoding='utf-8'))
w  = json.loads(WP.read_text(encoding='utf-8'))

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

NEW_ZONE = 'Sandbox_Small_Elevator_J'
NEW_LM   = 'Sandbox.SeventhStair'
CHAPTER  = 'SandboxSmall-chapter-5'
ch5_minz = chap_minz(CHAPTER)
print(f'ch5 MinZ = {ch5_minz}')

# Templates
elevator_B = next(r for r in z['Exports'][0]['Table']['Data']
                   if r['Name'] == 'Sandbox_Small_Elevator_B')
firstStair = next(r for r in lm['Exports'][0]['Table']['Data']
                   if r['Name'] == 'Sandbox.FirstStair')

# --- Create zone J ---
zone_rows = z['Exports'][0]['Table']['Data']
zone_by = {r['Name']: r for r in zone_rows}
if NEW_ZONE in zone_by:
    print(f'{NEW_ZONE} already exists — aborting to avoid clobber')
    raise SystemExit(1)

new_zone = copy.deepcopy(elevator_B)
new_zone['Name'] = NEW_ZONE
set_rowname(fp(new_zone['Value'], 'Chapter'), CHAPTER)
setv(fp(new_zone['Value'], 'Position'), 0, 12, ch5_minz)
# Zone DisplayName → Zones.Names.SB_Elevator_J (already pre-registered in vanilla)
dp = fp(new_zone['Value'], 'DisplayName')
if dp:
    dp['Value'] = 'Zones.Names.SB_Elevator_J'

# Rewrite LH entry to host the new stair
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
print(f'Created zone {NEW_ZONE}: chapter={CHAPTER}, Pos=(0,12,{ch5_minz}), Size=(6,6,4)')

# --- Create landmark Sandbox.SeventhStair (clone of FirstStair) ---
lm_rows = lm['Exports'][0]['Table']['Data']
lm_by = {r['Name']: r for r in lm_rows}
if NEW_LM in lm_by:
    print(f'{NEW_LM} already exists — aborting')
    raise SystemExit(1)

new_lm = copy.deepcopy(firstStair)
new_lm['Name'] = NEW_LM
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

# NameMaps
znm = z.get('NameMap', [])
for s in (NEW_ZONE, NEW_LM, 'Zones.Names.SB_Elevator_J'):
    if s not in znm:
        znm.append(s)
z['NameMap'] = znm

lnm = lm.get('NameMap', [])
for s in (NEW_LM, f'Landmarks.{NEW_LM}', f'World.Landmark.{NEW_LM}'):
    if s not in lnm:
        lnm.append(s)
lm['NameMap'] = lnm

ZP.write_text(json.dumps(z, indent=2), encoding='utf-8')
LP.write_text(json.dumps(lm, indent=2), encoding='utf-8')

# --- Update/add strings ---
entries = w['Exports'][0]['Table']['Value']
by_key = {e[0]: (i, e) for i, e in enumerate(entries)
          if isinstance(e, (list, tuple)) and len(e) >= 1}

def set_string(key, value):
    if key in by_key:
        i, _ = by_key[key]
        entries[i] = [key, value]
        return 'updated'
    else:
        entries.append([key, value])
        by_key[key] = (len(entries) - 1, entries[-1])
        return 'added'

strings = [
    ('Zones.Names.SB_Elevator_J',         'Seventh Stair'),
    ('Zones.Names.SB_Elevator_J.Banner',  'The Seventh Stair'),
    ('Landmarks.Sandbox.SeventhStair',    'Seventh Stair'),
]
for k, v in strings:
    st = set_string(k, v)
    print(f'  ({st}) {k:<42s} -> {v!r}')
WP.write_text(json.dumps(w, indent=2), encoding='utf-8')
print('\nDone.')
