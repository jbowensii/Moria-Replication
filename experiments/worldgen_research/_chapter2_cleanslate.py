"""
Chapter-2 clean slate:
 - Only Sandbox_ElvenQuarter (Promenade) is active in chapter 2
 - Size(2,2,3), Pos(10,16,12)
 - Suburban_C and ElvenQuarter_B disabled, landmarks cleared
 - FirstStair (ch1) GC -> Promenade  (one entrance)
 - NEW Sandbox.WesternMinesStair landmark in ch5 Mines_A -> Promenade (second entrance)
 - Promenade GC -> [FirstStair, WesternMinesStair]
"""
import copy, json
from pathlib import Path

HERE = Path(__file__).parent
ZP = HERE / 'DT_Moria_Zones.json'
LP = HERE / 'DT_Moria_Landmarks.json'

z = json.loads(ZP.read_text(encoding='utf-8'))
lm = json.loads(LP.read_text(encoding='utf-8'))


def fp(v, n):
    for p in v or []:
        if isinstance(p, dict) and p.get('Name') == n:
            return p
    return None


def setv(prop, x, y, zv):
    for it in (prop.get('Value') or []):
        if isinstance(it, dict):
            v = it.get('Value')
            if isinstance(v, dict) and 'X' in v:
                v['X'] = int(x); v['Y'] = int(y); v['Z'] = int(zv)
                return


def set_rowname(prop, new):
    for it in prop.get('Value', []) or []:
        if isinstance(it, dict) and it.get('Name') == 'RowName':
            it['Value'] = new
            return


def ivec(p):
    if not p:
        return None
    for it in (p.get('Value') or []):
        if isinstance(it, dict):
            v = it.get('Value')
            if isinstance(v, dict) and 'X' in v:
                return (v['X'], v['Y'], v['Z'])
    return None


zrows = z['Exports'][0]['Table']['Data']
lm_rows = lm['Exports'][0]['Table']['Data']
lm_by = {r['Name']: r for r in lm_rows}
zbyname = {r['Name']: r for r in zrows}


def set_gc(row, tags):
    gc = fp(row['Value'], 'GuaranteedConnections')
    if gc is None:
        return
    tpl = None
    if gc.get('Value'):
        tpl = copy.deepcopy(gc['Value'][0])
    elif 'DummyStruct' in gc:
        tpl = copy.deepcopy(gc['DummyStruct'])
    if tpl is None:
        for r in lm_rows:
            g = fp(r['Value'], 'GuaranteedConnections')
            if g and g.get('Value'):
                tpl = copy.deepcopy(g['Value'][0])
                break
    if tpl is None:
        return
    items = []
    for t in tags:
        it = copy.deepcopy(tpl)
        for sub in it.get('Value', []) or []:
            if isinstance(sub, dict) and sub.get('Name') == 'TagName':
                sub['Value'] = t
                break
        items.append(it)
    gc['Value'] = items
    if items:
        gc.pop('DummyStruct', None)


# ---- 1. Disable Suburban_C and ElvenQuarter_B in ch2 ----
for name in ('Sandbox_Small_Suburban_C', 'Sandbox_Small_ElvenQuarter_B'):
    r = zbyname.get(name)
    if not r:
        continue
    es = fp(r['Value'], 'EnabledState')
    if es:
        cur = es.get('Value', '')
        prefix = cur.split('::', 1)[0] if '::' in cur else 'ERowEnabledState'
        es['Value'] = f'{prefix}::Disabled'
    lh = fp(r['Value'], 'LandmarkHandles')
    if lh and lh.get('Value'):
        if 'DummyStruct' not in lh:
            lh['DummyStruct'] = copy.deepcopy(lh['Value'][0])
        lh['Value'] = []
    print(f'{name}: Disabled, LandmarkHandles cleared')

# ---- 2. Set Sandbox_ElvenQuarter geometry ----
r = zbyname['Sandbox_ElvenQuarter']
setv(fp(r['Value'], 'Position'), 10, 16, 12)
setv(fp(r['Value'], 'TargetSize'), 2, 2, 3)
tb = fp(r['Value'], 'TargetBubbles')
if tb:
    tb['Value'] = 1
print('Sandbox_ElvenQuarter: Pos(10,16,12) Size(2,2,3) TargetBubbles=1')

# ---- 3. Restore FirstStair GC -> Promenade ----
set_gc(lm_by['Sandbox.FirstStair'], ['World.Landmark.Sandbox.ElvenQuarterPromenade'])
print('Sandbox.FirstStair  GC -> [ElvenQuarterPromenade]')

# ---- 4. Create new stair landmark in ch5 ----
NEW = 'Sandbox.WesternMinesStair'
if NEW not in lm_by:
    tpl = copy.deepcopy(lm_by['Sandbox.FirstStair'])
    tpl['Name'] = NEW
    for p in tpl.get('Value', []):
        if isinstance(p, dict):
            n = p.get('Name')
            if n == 'BaseBubbleName':
                p['Value'] = 'BB_Sandbox_Elevator_Urban'
            elif n == 'DisplayName':
                p['Value'] = 'Landmarks.Sandbox.WesternMinesStair'
            elif n == 'GuaranteedConnections':
                if p.get('Value') and 'DummyStruct' not in p:
                    p['DummyStruct'] = copy.deepcopy(p['Value'][0])
                p['Value'] = []
    lm_rows.append(tpl)
    lm_by[NEW] = tpl
    print(f'Created landmark {NEW} (bubble=BB_Sandbox_Elevator_Urban)')

set_gc(lm_by[NEW], ['World.Landmark.Sandbox.ElvenQuarterPromenade'])
print(f'{NEW}  GC -> [ElvenQuarterPromenade]')

# ---- 5. Promenade GC -> both stairs ----
set_gc(lm_by['Sandbox.ElvenQuarterPromenade'],
       ['World.Landmark.Sandbox.FirstStair',
        'World.Landmark.Sandbox.WesternMinesStair'])
print('Sandbox.ElvenQuarterPromenade  GC -> [FirstStair, WesternMinesStair]')

# ---- Landmark NameMap ----
nm = lm.get('NameMap', [])
for s in [NEW, 'BB_Sandbox_Elevator_Urban',
          'World.Landmark.Sandbox.WesternMinesStair',
          'World.Landmark.Sandbox.FirstStair',
          'World.Landmark.Sandbox.ElvenQuarterPromenade',
          f'Landmarks.{NEW}']:
    if s not in nm:
        nm.append(s)
lm['NameMap'] = nm
LP.write_text(json.dumps(lm, indent=2), encoding='utf-8')

# ---- 6. Attach new stair to ch5 Mines_A_WesternMines ----
mines_zone = zbyname.get('Sandbox_Small_Mines_A_WesternMines')
if mines_zone:
    lh = fp(mines_zone['Value'], 'LandmarkHandles')
    tpl = None
    if lh and lh.get('Value'):
        tpl = copy.deepcopy(lh['Value'][0])
    elif lh and 'DummyStruct' in lh:
        tpl = copy.deepcopy(lh['DummyStruct'])
    else:
        # borrow from Elevator_B which has an ExtendedConnectivity entry
        for r in zrows:
            if r['Name'] == 'Sandbox_Small_Elevator_B':
                olh = fp(r['Value'], 'LandmarkHandles')
                if olh and olh.get('Value'):
                    tpl = copy.deepcopy(olh['Value'][0])
                    break
    if tpl is None:
        raise SystemExit('Could not build LH entry template for Mines_A_WesternMines')
    for sub in (tpl.get('Value') or []):
        if not isinstance(sub, dict):
            continue
        n = sub.get('Name')
        if n == 'Landmark':
            set_rowname(sub, NEW)
        elif n == 'Placement':
            cur = sub.get('Value', '')
            pref = cur.split('::', 1)[0] if '::' in cur else 'EZoneBubblePlacement'
            sub['Value'] = f'{pref}::Fixed'
        elif n == 'bExtendedConnectivityLandmark':
            sub['Value'] = True
    lh['Value'] = [tpl]
    lh.pop('DummyStruct', None)
    print(f'Sandbox_Small_Mines_A_WesternMines  LH -> [{NEW}]  ExtendedConn=True')

znm = z.get('NameMap', [])
if NEW not in znm:
    znm.append(NEW)
z['NameMap'] = znm
ZP.write_text(json.dumps(z, indent=2), encoding='utf-8')


# ====================================================================
# VERIFICATION
# ====================================================================
print()
print('=' * 70)
print('VERIFICATION')
print('=' * 70)

# A) Chapter-2 active zones
print()
print('[A] Chapter-2 zones (only Sandbox_ElvenQuarter should be Live)')
for r in zrows:
    c = fp(r['Value'], 'Chapter')
    cv = ''
    if c:
        for it in (c.get('Value') or []):
            if isinstance(it, dict) and it.get('Name') == 'RowName':
                cv = it.get('Value', '')
    if cv != 'SandboxSmall-chapter-2':
        continue
    es = fp(r['Value'], 'EnabledState')
    es_val = str(es.get('Value', '')).split('::')[-1] if es else '?'
    pos = ivec(fp(r['Value'], 'Position'))
    sz = ivec(fp(r['Value'], 'TargetSize'))
    lh = fp(r['Value'], 'LandmarkHandles')
    lms = []
    if lh:
        for e in (lh.get('Value') or []):
            for sub in (e.get('Value') or []):
                if isinstance(sub, dict) and sub.get('Name') == 'Landmark':
                    for it in (sub.get('Value') or []):
                        if isinstance(it, dict) and it.get('Name') == 'RowName':
                            lms.append(it.get('Value', ''))
    print(f'  {r["Name"]:40s} [{es_val:10s}] Pos={pos} Sz={sz} LMs={lms}')

# B) Landmark wiring
print()
print('[B] Landmark GCs')
for name in ('Sandbox.FirstStair', 'Sandbox.WesternMinesStair',
             'Sandbox.ElvenQuarterPromenade'):
    r = lm_by.get(name)
    if not r:
        print(f'  {name}  *** MISSING ***'); continue
    bb = fp(r['Value'], 'BaseBubbleName')
    gc = fp(r['Value'], 'GuaranteedConnections')
    tags = []
    if gc:
        for it in (gc.get('Value') or []):
            for sub in (it.get('Value') or []):
                if isinstance(sub, dict) and sub.get('Name') == 'TagName':
                    tags.append(sub.get('Value', ''))
    print(f'  {name:38s} bubble={bb.get("Value", "?")}')
    print(f'    GC -> {tags}')

# C) ch5 Mines_A_WesternMines LH
print()
print('[C] Chapter-5 Sandbox_Small_Mines_A_WesternMines LandmarkHandles')
if mines_zone:
    lh = fp(mines_zone['Value'], 'LandmarkHandles')
    if lh:
        for e in (lh.get('Value') or []):
            lname = ''; ext = False; plac = ''
            for sub in (e.get('Value') or []):
                if not isinstance(sub, dict):
                    continue
                n = sub.get('Name')
                if n == 'Landmark':
                    for it in (sub.get('Value') or []):
                        if isinstance(it, dict) and it.get('Name') == 'RowName':
                            lname = it.get('Value', '')
                elif n == 'Placement':
                    plac = str(sub.get('Value', '')).split('::')[-1]
                elif n == 'bExtendedConnectivityLandmark':
                    ext = sub.get('Value') is True
            print(f'  LM={lname}  Placement={plac}  ExtendedConn={ext}')

# D) Cross-reference sanity
print()
print('[D] Cross-reference sanity')
issues = []
# FirstStair GC target should be the Promenade (which must exist)
if 'Sandbox.ElvenQuarterPromenade' not in lm_by:
    issues.append('Promenade landmark row missing')
if 'Sandbox.WesternMinesStair' not in lm_by:
    issues.append('WesternMinesStair landmark row missing')
# ch2 active zones count
active_ch2 = [r for r in zrows
              if fp(r['Value'], 'Chapter') and any(
                  isinstance(i, dict) and i.get('Name') == 'RowName'
                  and i.get('Value') == 'SandboxSmall-chapter-2'
                  for i in fp(r['Value'], 'Chapter').get('Value') or [])
              and str((fp(r['Value'], 'EnabledState') or {}).get('Value', ''))
              .endswith('Live')]
if len(active_ch2) != 1 or active_ch2[0]['Name'] != 'Sandbox_ElvenQuarter':
    issues.append(f'ch2 active zones: {[r["Name"] for r in active_ch2]} (expected only Sandbox_ElvenQuarter)')
if issues:
    for i in issues:
        print(f'  ISSUE: {i}')
else:
    print('  All checks pass: 1 active ch2 zone, both stair landmarks present, GCs wired')
