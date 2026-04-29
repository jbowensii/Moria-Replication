"""Compare vanilla Chapter2.ElvenQuarterEntrance setup vs current."""
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

def gv(prop):
    v = prop.get('Value') if prop else None
    if isinstance(v, list) and v:
        inn = v[0]
        if isinstance(inn, dict) and isinstance(inn.get('Value'), dict):
            d = inn['Value']
            return (d.get('X'), d.get('Y'), d.get('Z'))
    return (None, None, None)

def st(r):
    p = fp(r.get('Value', []), 'EnabledState')
    return str(p.get('Value', '')).split('::')[-1] if p else None

def zs(r):
    p = fp(r.get('Value', []), 'ZoneSet')
    return str(p.get('Value', '')).split('::')[-1] if p else None


def show_landmark(r, label, keys=None):
    print(f'\n{label}: {r["Name"]}')
    for fld in ('Placement', 'BaseBubbleName', 'ChallengeRating', 'EnabledState',
                'bPlayerStartLocation'):
        p = fp(r['Value'], fld)
        v = p.get('Value') if p else '?'
        print(f'  {fld}: {v}')
    bp = gv(fp(r['Value'], 'BasePosition'))
    print(f'  BasePosition: {bp}')
    dn = fp(r['Value'], 'DisplayName')
    if dn and keys is not None:
        k = dn.get('Value')
        print(f'  DisplayName: {k} -> {keys.get(k, "?")}')
    gc = fp(r['Value'], 'GuaranteedConnections')
    targets = []
    for entry in (gc.get('Value') or []) if gc else []:
        for sub in entry.get('Value') or []:
            if isinstance(sub, dict) and sub.get('Name') == 'TagName':
                targets.append(sub.get('Value', '').replace('World.Landmark.', ''))
    print(f'  GuaranteedConnections: {targets}')


def hosts_for(landmark_substr, doc):
    out = []
    for r in doc['Exports'][0]['Table']['Data']:
        lh = fp(r['Value'], 'LandmarkHandles')
        if not lh: continue
        for e in (lh.get('Value') or []):
            for sub in e.get('Value') or []:
                if isinstance(sub, dict) and sub.get('Name') == 'Landmark':
                    lv = sub.get('Value')
                    if isinstance(lv, list):
                        for it in lv:
                            if isinstance(it, dict) and it.get('Name') == 'RowName':
                                ln = it.get('Value')
                                if landmark_substr in (ln or ''):
                                    ext = False; place = ''
                                    for s2 in e.get('Value') or []:
                                        if isinstance(s2, dict):
                                            if s2.get('Name') == 'bExtendedConnectivityLandmark':
                                                ext = bool(s2.get('Value'))
                                            elif s2.get('Name') == 'Placement':
                                                place = s2.get('Value', '')
                                    out.append((r, ln, place, ext))
    return out


def show_zone(r, ln, pl, ext):
    pos = gv(fp(r['Value'], 'Position'))
    sz = gv(fp(r['Value'], 'TargetSize'))
    print(f'  Zone: {r["Name"]}')
    print(f'    ZoneSet: {zs(r)}  Chapter: {get(r, "Chapter")}')
    print(f'    Pos={pos}  Size={sz}  State={st(r)}')
    print(f'    BubbleDeck: {get(r, "BubbleDeck")}')
    print(f'    PassageDeck: {get(r, "PassageDeck")}')
    print(f'    LandmarkHandle: {ln}  placement={pl}  ext={ext}')


# ===== Vanilla =====
print('=' * 80)
print('VANILLA — Chapter2.ElvenQuarterEntrance')
print('=' * 80)

zV = json.load(open('DT_Moria_Zones.original.json', encoding='utf-8'))
lmV = json.load(open('DT_Moria_Landmarks.original.json', encoding='utf-8'))
lcV = json.load(open('DT_Moria_LayoutConnections.original.json', encoding='utf-8'))

for r in lmV['Exports'][0]['Table']['Data']:
    if r['Name'] == 'Chapter2.ElvenQuarterEntrance':
        show_landmark(r, 'LANDMARK')

print('\nVanilla zones hosting Chapter2.ElvenQuarterEntrance:')
for r, ln, pl, ext in hosts_for('Chapter2.ElvenQuarterEntrance', zV):
    show_zone(r, ln, pl, ext)

print('\nVanilla LayoutConnections referencing Chapter2.ElvenQuarterEntrance:')
for r in lcV['Exports'][0]['Table']['Data']:
    ol = get(r, 'OriginLandmark'); dl = get(r, 'DestinationLandmark')
    if 'ElvenQuarterEntrance' in (ol or '') or 'ElvenQuarterEntrance' in (dl or ''):
        print(f'  {r["Name"]:<48} OL={ol} DL={dl} state={st(r)}')

# ===== Current =====
print('\n' + '=' * 80)
print('CURRENT — Sandbox.ElvenQuarterEntrance')
print('=' * 80)

z = json.load(open('DT_Moria_Zones.json', encoding='utf-8'))
lm = json.load(open('DT_Moria_Landmarks.json', encoding='utf-8'))
lc = json.load(open('DT_Moria_LayoutConnections.json', encoding='utf-8'))
W = json.load(open('World.json', encoding='utf-8'))
keys = {e[0]: e[1] for e in W['Exports'][0]['Table']['Value']
        if isinstance(e, list) and len(e) >= 2}

for r in lm['Exports'][0]['Table']['Data']:
    if r['Name'] == 'Sandbox.ElvenQuarterEntrance':
        show_landmark(r, 'LANDMARK', keys=keys)

print('\nCurrent zones hosting any ElvenQuarterEntrance:')
for r, ln, pl, ext in hosts_for('ElvenQuarterEntrance', z):
    show_zone(r, ln, pl, ext)

print('\nCurrent LayoutConnections referencing ElvenQuarterEntrance:')
for r in lc['Exports'][0]['Table']['Data']:
    ol = get(r, 'OriginLandmark'); dl = get(r, 'DestinationLandmark')
    if 'ElvenQuarterEntrance' in (ol or '') or 'ElvenQuarterEntrance' in (dl or ''):
        zsr = fp(r['Value'], 'ZoneSet')
        zs_v = str(zsr.get('Value', '')).split('::')[-1] if zsr else ''
        print(f'  {r["Name"]:<48} ZoneSet={zs_v} OL={ol} DL={dl} state={st(r)}')

print('\nDedicated ElvenEntrance zone in current?')
for r in z['Exports'][0]['Table']['Data']:
    n = r['Name']
    if 'ElvenEntrance' in n or 'ElvenQuarterEntrance' in n:
        pos = gv(fp(r['Value'], 'Position'))
        sz = gv(fp(r['Value'], 'TargetSize'))
        print(f'  Zone {n}: state={st(r)} ZoneSet={zs(r)} Chapter={get(r, "Chapter")}'
              f' Pos={pos} Size={sz}')
