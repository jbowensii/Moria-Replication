"""Full audit of chapter Z-bands, zone placements, and all mod changes so far."""
import json, os
from pathlib import Path

HERE = Path(__file__).parent
os.chdir(HERE)

files = {
    'chapters': 'DT_Moria_Chapters.json',
    'zones':    'DT_Moria_Zones.json',
    'landmarks':'DT_Moria_Landmarks.json',
    'decks':    'DT_Moria_ZoneDeck.json',
    'filters':  'DT_Moria_ZoneBubbleFilters.json',
    'world':    'World.json',
    'layoutConnections': 'DT_Moria_LayoutConnections.json',
}
data = {k: json.load(open(v, encoding='utf-8')) for k, v in files.items()}
orig = {
    'chapters': json.load(open('DT_Moria_Chapters.original.json', encoding='utf-8')),
    'zones':    json.load(open('DT_Moria_Zones.original.json', encoding='utf-8')),
    'landmarks':json.load(open('DT_Moria_Landmarks.original.json', encoding='utf-8')),
    'decks':    json.load(open('DT_Moria_ZoneDeck.original.json', encoding='utf-8')),
    'world':    json.load(open('World.original.json', encoding='utf-8')),
}


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


def ivec(p):
    if not p: return None
    for it in (p.get('Value') or []):
        if isinstance(it, dict):
            v = it.get('Value')
            if isinstance(v, dict) and 'X' in v:
                return (v['X'], v['Y'], v['Z'])


def rows(doc): return doc['Exports'][0]['Table']['Data']
def strings(doc):
    return {e[0]: e[1] for e in doc['Exports'][0]['Table']['Value']
            if isinstance(e, (list, tuple)) and len(e) >= 2}


w_strings = strings(data['world'])


# =============================================================================
# 1. CHAPTER AUDIT
# =============================================================================
print('=' * 96)
print('1. CHAPTER AUDIT (Z-bands, PrimeZ, EnemyScalingLevel, contiguity)')
print('=' * 96)

ss_ch = [r for r in rows(data['chapters']) if r['Name'].startswith('SandboxSmall-chapter-')]
ss_ch.sort(key=lambda r: -(get(r, 'Layer') or 0))

issues_chapters = []
print(f'{"Layer":>5}  {"Lv":<4}  {"ID":>3}  {"Z-band":<10}  {"h":>2}  {"PrimeZ":>6}  {"Pr_calc":>7}  '
      f'{"Scale":>5}  {"Sc_exp":>6}  {"State":<9}  {"Display"}')
print('-' * 110)

prev_max = None
for r in ss_ch:
    lvl = int(r['Name'].split('-')[-1])
    layer = get(r, 'Layer'); minz = get(r, 'MinZ'); maxz = get(r, 'MaxZ')
    pz = get(r, 'PrimeZ'); cid = get(r, 'ChapterID'); scale = get(r, 'EnemyScalingLevel')
    es = str(get(r, 'EnabledState') or '').split('::')[-1]
    dn = get(r, 'DisplayName')
    h = maxz - minz + 1

    pr_expected = (minz + maxz) // 2
    sc_expected = abs(layer)
    cid_expected = lvl

    ok_pr = '' if pz == pr_expected else f'! (expected {pr_expected})'
    ok_sc = '' if scale == sc_expected else f'! (expected {sc_expected})'
    ok_cid = '' if cid == cid_expected else f'! (expected {cid_expected})'

    if pz != pr_expected:
        issues_chapters.append(f'ch{lvl}: PrimeZ={pz} should be {pr_expected}')
    if scale != sc_expected:
        issues_chapters.append(f'ch{lvl}: Scale={scale} should be {sc_expected}')
    if cid != cid_expected:
        issues_chapters.append(f'ch{lvl}: ChapterID={cid} should be {cid_expected}')

    print(f'  {layer:>+3}  Lv-{lvl:<2}  {cid:>3}  {minz:>3}..{maxz:<3}  {h:>2}  {pz:>6}  {pr_expected:>7}  '
          f'{scale:>5}  {sc_expected:>6}  {es:<9}  {dn}')

# Contiguity check
print()
print('  Contiguity check (bottom-up):')
ss_up = sorted(ss_ch, key=lambda r: get(r, 'Layer'))
prev_max = None
for r in ss_up:
    layer = get(r, 'Layer'); minz = get(r, 'MinZ'); maxz = get(r, 'MaxZ')
    if prev_max is not None:
        gap = minz - prev_max - 1
        note = 'contiguous' if gap == 0 else (f'OVERLAP {-gap}' if gap < 0 else f'GAP {gap}')
        if gap != 0:
            issues_chapters.append(f'ch{int(r["Name"].split("-")[-1])} Layer {layer:+d}: {note}')
        print(f'    Layer {layer:>+3}  Z={minz}..{maxz}  {note}')
    else:
        print(f'    Layer {layer:>+3}  Z={minz}..{maxz}  (bottom)')
    prev_max = maxz

if issues_chapters:
    print(f'\n  CHAPTER ISSUES ({len(issues_chapters)}):')
    for i in issues_chapters: print(f'    * {i}')
else:
    print('\n  All chapter rules pass.')


# =============================================================================
# 2. ZONE AUDIT (Pos.Z vs chapter band, Size.Z overflow, references)
# =============================================================================
print()
print('=' * 96)
print('2. ZONE AUDIT (SandboxSmall zones: Pos.Z alignment, overflow, chapter occupancy)')
print('=' * 96)

chap_minz = {r['Name']: get(r, 'MinZ') for r in ss_ch}
chap_maxz = {r['Name']: get(r, 'MaxZ') for r in ss_ch}

def chap_of(r):
    c = fp(r['Value'], 'Chapter')
    if c:
        for it in (c.get('Value') or []):
            if isinstance(it, dict) and it.get('Name') == 'RowName':
                return it.get('Value', '')
    return ''

sandbox_zones = [r for r in rows(data['zones'])
                 if get(r, 'ZoneSet') == 'EZoneSet::SandboxSmall']
print(f'  SandboxSmall zones on disk: {len(sandbox_zones)}')

issues_zones = []
overflows = []
per_chapter = {}
for r in sandbox_zones:
    c = chap_of(r)
    per_chapter.setdefault(c, []).append(r)

# Sort chapters by Layer for report
ch_order = [r['Name'] for r in sorted(ss_ch, key=lambda r: -(get(r, 'Layer') or 0))]

for chn in ch_order:
    zones = per_chapter.get(chn, [])
    if chn not in chap_minz:
        continue
    mnz, mxz = chap_minz[chn], chap_maxz[chn]
    lvl = int(chn.split('-')[-1])
    live_count = sum(1 for r in zones
                     if str(get(r, 'EnabledState') or '').split('::')[-1] == 'Live')
    print(f'\n  Lv-{lvl:<2} ({chn}, Z={mnz}..{mxz})  [{live_count}/{len(zones)} Live]')
    for r in zones:
        pos = ivec(fp(r['Value'], 'Position'))
        sz = ivec(fp(r['Value'], 'TargetSize'))
        es = str(get(r, 'EnabledState') or '').split('::')[-1]
        if not pos or not sz:
            continue
        zlo, zsize = pos[2], sz[2]
        zhi = zlo + zsize - 1
        status = ''
        if zlo != mnz:
            status = f' POS.Z={zlo} != MinZ={mnz}'
            issues_zones.append(f'{r["Name"]}: Pos.Z={zlo} should be {mnz}')
        if zhi > mxz:
            overflow = zhi - mxz
            status += f' OVERFLOW +{overflow}'
            overflows.append((r['Name'], chn, sz[2], mxz - mnz + 1, overflow))
        print(f'    {r["Name"]:<42s} [{es:<8}]  Pos={pos} Size={sz}{status}')

# Hub zones (Moria-* chapters)
print()
print('  Hub zones (ZoneSet=SandboxSmall, chapter=Moria-*):')
hub_zones = [r for r in rows(data['zones'])
             if get(r, 'ZoneSet') == 'EZoneSet::SandboxSmall'
             and chap_of(r).startswith('Moria-')]
for r in hub_zones:
    pos = ivec(fp(r['Value'], 'Position'))
    sz = ivec(fp(r['Value'], 'TargetSize'))
    es = str(get(r, 'EnabledState') or '').split('::')[-1]
    dn = get(r, 'DisplayName')
    print(f'    {r["Name"]:<32}  chapter={chap_of(r):<32}  Pos={pos} Size={sz}  [{es}]  Display={dn}')

if issues_zones:
    print(f'\n  ZONE-PLACEMENT ISSUES ({len(issues_zones)}):')
    for i in issues_zones[:20]:
        print(f'    * {i}')
    if len(issues_zones) > 20:
        print(f'    ... and {len(issues_zones)-20} more')
else:
    print('\n  All sandbox zones have Pos.Z aligned to chapter MinZ.')

if overflows:
    print(f'\n  ACCEPTED OVERFLOWS ({len(overflows)} — user choice: leave as vanilla tolerates):')
    for name, chn, zs, ch_h, over in overflows:
        lvl = int(chn.split('-')[-1])
        print(f'    {name:<42}  Lv-{lvl:<2} (h={ch_h}) + Size.Z={zs}  overflows by +{over}')


# =============================================================================
# 3. STAIR / CONNECTIVITY AUDIT
# =============================================================================
print()
print('=' * 96)
print('3. STAIR AUDIT (bExtendedConnectivityLandmark coverage of Lv-N transitions)')
print('=' * 96)

layer_to_lv = {get(r, 'Layer'): int(r['Name'].split('-')[-1]) for r in ss_ch}

stairs_info = []
for zr in rows(data['zones']):
    lh = fp(zr['Value'], 'LandmarkHandles')
    if not lh: continue
    for e in (lh.get('Value') or []):
        lname = ''; ext = False
        for sub in (e.get('Value') or []):
            if isinstance(sub, dict):
                if sub.get('Name') == 'Landmark':
                    for it in (sub.get('Value') or []):
                        if isinstance(it, dict) and it.get('Name') == 'RowName':
                            lname = it.get('Value', '')
                elif sub.get('Name') == 'bExtendedConnectivityLandmark':
                    ext = sub.get('Value') is True
        if ext and lname:
            lr = next((r for r in rows(data['landmarks']) if r['Name'] == lname), None)
            bb = get(lr, 'BaseBubbleName') if lr else '?'
            c = chap_of(zr)
            if c.startswith('SandboxSmall-chapter-'):
                layer_p = next((r for r in ss_ch if r['Name'] == c), None)
                layer = get(layer_p, 'Layer') if layer_p else None
                stairs_info.append((lname, zr['Name'], c, layer, bb))

stairs_info.sort(key=lambda s: -(s[3] or 0))

print(f'  Stair landmarks in SandboxSmall chapters: {len(stairs_info)}')
print(f'  {"Landmark":<30}  {"Host":<30}  {"Chapter":<28}  {"Layer":>5}  Bubble')
print('  ' + '-' * 110)
for lname, zn, c, layer, bb in stairs_info:
    kind = 'CRYSTAL' if 'CrystalDescent' in bb else ('URBAN' if 'Elevator_Urban' in bb else bb)
    print(f'  {lname:<30s}  {zn:<30}  {c:<28}  {layer:>+5d}  {kind}')

# Coverage matrix
print()
print('  Transition coverage (by Layer adjacency):')
cov = {}
for lname, zn, c, layer, bb in stairs_info:
    if layer is None: continue
    # Each stair auto-connects to Layer+1 and Layer-1
    for target_layer in (layer + 1, layer - 1):
        if target_layer in layer_to_lv:
            host_lv = layer_to_lv[layer]
            target_lv = layer_to_lv[target_layer]
            # Canonical pair (lower layer first)
            key = tuple(sorted([layer, target_layer]))
            cov.setdefault(key, []).append((lname, 'CRYSTAL' if 'CrystalDescent' in bb else 'URBAN'))

# Print for each adjacent layer pair
all_layers = sorted(set(get(r, 'Layer') for r in ss_ch))
gaps = []
for i in range(len(all_layers) - 1):
    lo, hi = all_layers[i], all_layers[i + 1]
    lvs = (layer_to_lv[lo], layer_to_lv[hi])
    key = (lo, hi)
    stairs_there = cov.get(key, [])
    mark = 'OK' if stairs_there else '** MISSING'
    kinds = sorted(set(k for _, k in stairs_there))
    kind_str = '+'.join(kinds) if kinds else 'none'
    print(f'    Lv-{lvs[0]:<2} <-> Lv-{lvs[1]:<2}  (Layer {lo:+d} <-> {hi:+d})  [{mark}]  {kind_str}')
    if not stairs_there:
        gaps.append(f'Layer {lo:+d} <-> {hi:+d}')

if gaps:
    print(f'\n  COVERAGE GAPS: {gaps}')
else:
    print('\n  All adjacent-layer transitions covered.')


# =============================================================================
# 4. LANDMARK + DISPLAY STRING AUDIT
# =============================================================================
print()
print('=' * 96)
print('4. LANDMARK / DISPLAY-STRING AUDIT (cross-reference validity)')
print('=' * 96)

lm_names = {r['Name'] for r in rows(data['landmarks'])}
# Every landmark referenced by a zone LH must exist
broken_lh = []
for r in rows(data['zones']):
    lh = fp(r['Value'], 'LandmarkHandles')
    if not lh: continue
    for e in (lh.get('Value') or []):
        for sub in (e.get('Value') or []):
            if isinstance(sub, dict) and sub.get('Name') == 'Landmark':
                for it in (sub.get('Value') or []):
                    if isinstance(it, dict) and it.get('Name') == 'RowName':
                        v = it.get('Value', '')
                        if v and v not in lm_names:
                            broken_lh.append((r['Name'], v))
if broken_lh:
    print(f'  BROKEN LandmarkHandle refs ({len(broken_lh)}):')
    for zn, v in broken_lh: print(f'    {zn} -> {v}')
else:
    print('  All LandmarkHandle refs resolve.')

# Every GC tag must reference an existing landmark
broken_gc = []
for r in rows(data['landmarks']):
    gc = fp(r['Value'], 'GuaranteedConnections')
    if not gc: continue
    for it in (gc.get('Value') or []):
        for sub in (it.get('Value') or []):
            if isinstance(sub, dict) and sub.get('Name') == 'TagName':
                v = sub.get('Value', '')
                if v.startswith('World.Landmark.'):
                    target = v[len('World.Landmark.'):]
                    if target not in lm_names:
                        broken_gc.append((r['Name'], v))
if broken_gc:
    print(f'\n  BROKEN GuaranteedConnections tags ({len(broken_gc)}):')
    for ln, v in broken_gc: print(f'    {ln} -> {v}')
else:
    print('  All GuaranteedConnections refs resolve.')

# Every DisplayName TextProperty pointing at World table must have a string entry
def collect_world_refs(obj, out):
    if isinstance(obj, dict):
        if (obj.get('$type', '').startswith('UAssetAPI.PropertyTypes.Objects.TextPropertyData')
                and obj.get('HistoryType') == 'StringTableEntry'
                and 'World' in obj.get('TableId', '')):
            v = obj.get('Value', '')
            if v: out.append(v)
        for v in obj.values(): collect_world_refs(v, out)
    elif isinstance(obj, list):
        for v in obj: collect_world_refs(v, out)

refs = []
for f in ('zones', 'landmarks', 'chapters', 'decks', 'filters',
          'layoutConnections'):
    if f in data:
        collect_world_refs(data[f], refs)

missing_strings = sorted(set(refs) - set(w_strings.keys()))
print(f'\n  World-table string refs encountered: {len(set(refs))}')
if missing_strings:
    print(f'  MISSING string entries ({len(missing_strings)}):')
    for k in missing_strings: print(f'    {k}')
else:
    print('  All World-table string refs resolve.')


# =============================================================================
# 5. DECK AUDIT
# =============================================================================
print()
print('=' * 96)
print('5. DECK AUDIT (ZoneDeck rows referenced by zones actually exist)')
print('=' * 96)

deck_names = {r['Name'] for r in rows(data['decks'])}
broken_decks = []
for r in rows(data['zones']):
    for f in ('BubbleDeck', 'PassageDeck'):
        p = fp(r['Value'], f)
        if p:
            for it in (p.get('Value') or []):
                if isinstance(it, dict) and it.get('Name') == 'RowName':
                    v = it.get('Value', '')
                    if v and v not in deck_names:
                        broken_decks.append((r['Name'], f, v))
if broken_decks:
    print(f'  BROKEN deck refs ({len(broken_decks)}):')
    for zn, f, v in broken_decks: print(f'    {zn}.{f} -> {v}')
else:
    print('  All zone BubbleDeck/PassageDeck refs resolve.')


# =============================================================================
# 6. CHANGE SUMMARY (this file vs pristine)
# =============================================================================
print()
print('=' * 96)
print('6. CHANGES VS PRISTINE (what we have modified)')
print('=' * 96)

def diff_rows(cur_doc, orig_doc):
    cur_names = {r['Name'] for r in rows(cur_doc)}
    orig_names = {r['Name'] for r in rows(orig_doc)}
    added = sorted(cur_names - orig_names)
    removed = sorted(orig_names - cur_names)
    common = cur_names & orig_names
    modified = []
    cur_by = {r['Name']: r for r in rows(cur_doc)}
    orig_by = {r['Name']: r for r in rows(orig_doc)}
    for n in common:
        if json.dumps(cur_by[n], sort_keys=True) != json.dumps(orig_by[n], sort_keys=True):
            modified.append(n)
    return added, removed, sorted(modified)

for key in ('chapters', 'zones', 'landmarks', 'decks'):
    added, removed, modified = diff_rows(data[key], orig[key])
    print(f'\n  {key.upper()}:')
    print(f'    Added ({len(added)}):   {added}')
    print(f'    Removed ({len(removed)}): {removed}')
    print(f'    Modified ({len(modified)}): {len(modified)} rows  '
          f'({", ".join(modified[:8])}{"..." if len(modified)>8 else ""})')

# World strings: how many added/removed/changed
cur_str = w_strings
orig_str = strings(orig['world'])
added_str = sorted(set(cur_str) - set(orig_str))
removed_str = sorted(set(orig_str) - set(cur_str))
changed_str = sorted(k for k in set(cur_str) & set(orig_str) if cur_str[k] != orig_str[k])
print(f'\n  WORLD STRINGS:')
print(f'    Added ({len(added_str)}):   {added_str[:15]}{"..." if len(added_str)>15 else ""}')
print(f'    Removed ({len(removed_str)}): {removed_str}')
print(f'    Changed ({len(changed_str)}): {changed_str[:15]}{"..." if len(changed_str)>15 else ""}')


# =============================================================================
# 7. SUMMARY
# =============================================================================
print()
print('=' * 96)
print('7. FINAL SUMMARY')
print('=' * 96)
total_issues = len(issues_chapters) + len(issues_zones) + len(broken_lh) + len(broken_gc) + len(missing_strings) + len(broken_decks) + len(gaps)
print(f'  Chapter issues:         {len(issues_chapters)}')
print(f'  Zone placement issues:  {len(issues_zones)}')
print(f'  Zone overflows:         {len(overflows)}  (accepted)')
print(f'  Broken LH refs:         {len(broken_lh)}')
print(f'  Broken GC refs:         {len(broken_gc)}')
print(f'  Missing string refs:    {len(missing_strings)}')
print(f'  Broken deck refs:       {len(broken_decks)}')
print(f'  Stair coverage gaps:    {len(gaps)}')
print()
if total_issues == 0:
    print('  ==> ALL CHECKS PASS. Data is consistent with derived rules.')
else:
    print(f'  ==> {total_issues} issue(s) found. See sections above.')
