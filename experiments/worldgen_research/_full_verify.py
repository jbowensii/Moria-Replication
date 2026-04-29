"""Full verification + validation."""
import json, re, os

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

def zs(r):
    p = fp(r.get('Value', []), 'ZoneSet')
    return str(p.get('Value', '')).split('::')[-1] if p else None

def st(r):
    p = fp(r.get('Value', []), 'EnabledState')
    return str(p.get('Value', '')).split('::')[-1] if p else None

def axes(p1, s1, p2, s2):
    ox = min(p1[0]+s1[0]-1, p2[0]+s2[0]-1) - max(p1[0], p2[0]) + 1
    oy = min(p1[1]+s1[1]-1, p2[1]+s2[1]-1) - max(p1[1], p2[1]) + 1
    oz = min(p1[2]+s1[2]-1, p2[2]+s2[2]-1) - max(p1[2], p2[2]) + 1
    return ox, oy, oz

print('=' * 80)
print('FULL VERIFICATION & VALIDATION')
print('=' * 80)

# 1) NameMap counter sync
print('\n[1] NameMap counter sync')
print('-' * 80)
FILES = ['DT_Moria_Zones', 'DT_Moria_Chapters', 'DT_Moria_Landmarks', 'DT_Moria_Biomes',
         'DT_Moria_ZoneDeck', 'DT_Moria_ZoneBubbleFilters', 'DT_Moria_LayoutConnections',
         'DT_Moria_ZoneTemplates', 'World']
errs = 0
for stem in FILES:
    p = stem + '.json'
    if not os.path.exists(p): continue
    d = json.load(open(p, encoding='utf-8'))
    nm = d.get('NameMap', [])
    nrc = d.get('NamesReferencedFromExportDataCount', None)
    gen = None
    try:
        gen = d['Exports'][0]['Generations'][0]['NameCount']
    except Exception:
        pass
    nm_count = len(nm)
    flag = ''
    if nrc is not None and nrc != nm_count:
        flag += f' NRC={nrc}!=NM={nm_count}'
        errs += 1
    if gen is not None and gen != nm_count:
        flag += f' Gen={gen}!=NM={nm_count}'
        errs += 1
    status = 'PASS' if not flag else 'FAIL' + flag
    print(f'  {stem:<32} NM={nm_count} NRC={nrc} Gen={gen}  {status}')
print(f'  Total NameMap sync errors: {errs}')

# 2) Zone rule compliance
print('\n[2] Zone rule compliance')
print('-' * 80)
z = json.load(open('DT_Moria_Zones.json', encoding='utf-8'))
ch = json.load(open('DT_Moria_Chapters.json', encoding='utf-8'))
chap_minz = {}
chap_maxz = {}
chap_layer = {}
for r in ch['Exports'][0]['Table']['Data']:
    if st(r) == 'Disabled': continue
    chap_minz[r['Name']] = get(r, 'MinZ')
    chap_maxz[r['Name']] = get(r, 'MaxZ')
    chap_layer[r['Name']] = get(r, 'Layer')

EX = re.compile(r'(elevator|descent)', re.I)
zones = []
for r in z['Exports'][0]['Table']['Data']:
    if zs(r) != 'SandboxSmall' or st(r) == 'Disabled': continue
    p = gv(fp(r['Value'], 'Position'))
    s = gv(fp(r['Value'], 'TargetSize'))
    if None in p or None in s: continue
    zones.append((r['Name'], get(r, 'Chapter'), p, s))

pinned = [(n, c, p, s) for n, c, p, s in zones if p != (0, 0, 0)]
auto = [(n, c, p, s) for n, c, p, s in zones if p == (0, 0, 0)]

oob = [(n, p, s) for n, c, p, s in pinned if not (0 <= p[0] and p[0]+s[0]-1 <= 29 and 0 <= p[1] and p[1]+s[1]-1 <= 29)]
print(f'  X/Y bounds 0..29:           {"PASS" if not oob else f"FAIL {len(oob)}"}')

zoob = [(n, p, s) for n, c, p, s in pinned if p[2] < 0 or p[2]+s[2]-1 > 29]
print(f'  Z bounds 0..29:             {"PASS" if not zoob else f"FAIL {len(zoob)}"}')

big = [(n, s) for n, c, p, s in zones if s[0] > 14 or s[1] > 14 or s[2] > 4]
print(f'  Max size 14x14x4:           {"PASS" if not big else f"FAIL {len(big)}"}')

minz_v = []
for n, c, p, s in pinned:
    if EX.search(n): continue
    if c in chap_minz and p[2] != chap_minz[c]:
        minz_v.append((n, c, p[2], chap_minz[c]))
print(f'  MinZ rule (non-elev/desc):  {"PASS" if not minz_v else f"FAIL {len(minz_v)}"}')

intra = 0
cross_high = 0
for i in range(len(pinned)):
    for j in range(i+1, len(pinned)):
        n1, c1, p1, s1 = pinned[i]
        n2, c2, p2, s2 = pinned[j]
        ox, oy, oz = axes(p1, s1, p2, s2)
        if ox > 0 and oy > 0 and oz > 0:
            v1 = s1[0]*s1[1]*s1[2]
            v2 = s2[0]*s2[1]*s2[2]
            cv = max(ox*oy*oz/v1*100, ox*oy*oz/v2*100)
            if c1 == c2:
                intra += 1
            elif cv > 10:
                cross_high += 1
print(f'  Intra-chapter overlap:      {"PASS" if intra == 0 else f"FAIL {intra}"}')
print(f'  Cross-chapter overlap >10%: {"PASS" if cross_high == 0 else f"FAIL {cross_high}"}')

# 3) Chapter integrity
print('\n[3] Chapter integrity')
print('-' * 80)
ss = [r for r in ch['Exports'][0]['Table']['Data']
      if r['Name'].startswith('SandboxSmall-chapter-') and st(r) != 'Disabled']
total_h = sum(get(r, 'MaxZ') - get(r, 'MinZ') + 1 for r in ss)
zmin = min(get(r, 'MinZ') for r in ss)
zmax = max(get(r, 'MaxZ') for r in ss)
print(f'  SS chapters: {len(ss)}   total H: {total_h}   Z range: {zmin}..{zmax}')
print(f'  Z budget 0..29:             {"PASS" if 0 <= zmin and zmax <= 29 else "FAIL"}')

all_ids = [get(r, 'ChapterID') for r in ch['Exports'][0]['Table']['Data']
           if st(r) != 'Disabled' and get(r, 'ChapterID') is not None]
dups = {x for x in all_ids if all_ids.count(x) > 1}
print(f'  ChapterID uniqueness:       {"PASS" if not dups else f"FAIL dups={sorted(dups)}"}')

# 4) Stair landmark/zone consistency
print('\n[4] Stair landmark/zone consistency')
print('-' * 80)
lm = json.load(open('DT_Moria_Landmarks.json', encoding='utf-8'))
lm_bub = {r['Name']: get(r, 'BaseBubbleName') for r in lm['Exports'][0]['Table']['Data']}

missing_lm = []
for r in z['Exports'][0]['Table']['Data']:
    if zs(r) != 'SandboxSmall' or st(r) == 'Disabled': continue
    lh = fp(r['Value'], 'LandmarkHandles')
    for e in (lh.get('Value') or []) if lh else []:
        for sub in e.get('Value') or []:
            if isinstance(sub, dict) and sub.get('Name') == 'Landmark':
                lv = sub.get('Value')
                if isinstance(lv, list):
                    for it in lv:
                        if isinstance(it, dict) and it.get('Name') == 'RowName':
                            ln = it.get('Value')
                            if ln and ln not in lm_bub:
                                missing_lm.append((r['Name'], ln))
print(f'  Zone landmark refs resolve: {"PASS" if not missing_lm else f"FAIL {len(missing_lm)}"}')

stair_zones = [r for r in z['Exports'][0]['Table']['Data']
               if zs(r) == 'SandboxSmall' and st(r) == 'Live' and EX.search(r['Name'])]
print(f'  Active stair zones: {len(stair_zones)}')

# 5) StringTable references
print('\n[5] StringTable references')
print('-' * 80)
W = json.load(open('World.json', encoding='utf-8'))
st_keys = set()
for entry in W['Exports'][0]['Table']['Value']:
    if isinstance(entry, list) and len(entry) >= 1:
        st_keys.add(entry[0])

def text_keys(d):
    refs = set()
    def walk(o):
        if isinstance(o, dict):
            if 'TextPropertyData' in str(o.get('$type', '')) and o.get('HistoryType') == 'StringTableEntry':
                k = o.get('Value')
                if k: refs.add(str(k))
            for v in o.values(): walk(v)
        elif isinstance(o, list):
            for it in o: walk(it)
    walk(d)
    return refs

unresolved = 0
for stem in ['DT_Moria_Zones', 'DT_Moria_Landmarks', 'DT_Moria_Chapters', 'DT_Moria_Biomes']:
    refs = text_keys(json.load(open(stem + '.json', encoding='utf-8')))
    missing = refs - st_keys
    if missing:
        unresolved += len(missing)
        print(f'  {stem}: {len(missing)} missing keys')
        for k in list(missing)[:5]: print(f'    - {k}')
print(f'  StringTable refs resolve:   {"PASS" if unresolved == 0 else f"FAIL {unresolved}"}')

# 6) Sentinel zones
print('\n[6] (0,0,0) sentinel zones')
print('-' * 80)
unexpected = 0
for n, c, p, s in auto:
    is_elev = bool(EX.search(n))
    is_bridge = c and not c.startswith('SandboxSmall-chapter-')
    if not (is_elev or is_bridge):
        unexpected += 1
        print(f'  UNEXPECTED  {n}  chap={c}')
print(f'  Sentinel rule:              {"PASS" if unexpected == 0 else f"FAIL {unexpected}"}')

# Summary
print('\n' + '=' * 80)
print('SUMMARY')
print('=' * 80)
total_live = sum(1 for r in z['Exports'][0]['Table']['Data']
                 if zs(r) == 'SandboxSmall' and st(r) == 'Live')
print(f'Total Live SandboxSmall zones: {total_live}')
print(f'  Pinned: {len(pinned)}   Auto-placed: {len(auto)}')
print(f'  Active stair zones: {len(stair_zones)}')
print(f'  Active SS chapters: {len(ss)}')
