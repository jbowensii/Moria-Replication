#!/usr/bin/env python3
"""Renumber ChapterIDs per odd/up, even/down convention; audit DisplayName + StringTable; resolve conflicts."""
import json
from pathlib import Path

CHAPTERS = Path('DT_Moria_Chapters.json')
WORLD = Path('World.json')

# Renumber map: row name -> new ChapterID
RENUMBER = {
    'SandboxSmall-chapter-1':  1,   # Lv-1
    'SandboxSmall-chapter-2':  3,   # Lv-2
    'SandboxSmall-chapter-3':  5,   # Lv-3
    'SandboxSmall-chapter-4':  7,   # Lv-4
    'SandboxSmall-chapter-9':  9,   # Lv-5
    'SandboxSmall-chapter-10': 11,  # Lv-6
    'SandboxSmall-chapter-11': 13,  # Lv-7
    'SandboxSmall-chapter-5':  2,   # D-1
    'SandboxSmall-chapter-6':  4,   # D-2
    'SandboxSmall-chapter-7':  6,   # D-3
    'SandboxSmall-chapter-8':  8,   # D-4
    'SandboxSmall-chapter-12': 10,  # D-5
    'SandboxSmall-chapter-13': 12,  # D-6
    'SandboxSmall-chapter-14': 14,  # D-7
}

EXPECTED_DN = {
    'SandboxSmall-chapter-1':  'Chapter.Sandbox.Level1.Name',
    'SandboxSmall-chapter-2':  'Chapter.Sandbox.Level2.Name',
    'SandboxSmall-chapter-3':  'Chapter.Sandbox.Level3.Name',
    'SandboxSmall-chapter-4':  'Chapter.Sandbox.Level4.Name',
    'SandboxSmall-chapter-9':  'Chapter.Sandbox.Level5.Name',
    'SandboxSmall-chapter-10': 'Chapter.Sandbox.Level6.Name',
    'SandboxSmall-chapter-11': 'Chapter.Sandbox.Level7.Name',
    'SandboxSmall-chapter-5':  'Chapter.Sandbox.Deep1.Name',
    'SandboxSmall-chapter-6':  'Chapter.Sandbox.Deep2.Name',
    'SandboxSmall-chapter-7':  'Chapter.Sandbox.Deep3.Name',
    'SandboxSmall-chapter-8':  'Chapter.Sandbox.Deep4.Name',
    'SandboxSmall-chapter-12': 'Chapter.Sandbox.Deep5.Name',
    'SandboxSmall-chapter-13': 'Chapter.Sandbox.Deep6.Name',
    'SandboxSmall-chapter-14': 'Chapter.Sandbox.Deep7.Name',
}

EXPECTED_KEYS = set(EXPECTED_DN.values())
EXPECTED_TABLE_ID = '/Game/Tech/Data/StringTables/World.World'


def get_prop(row, name):
    for p in row.get('Value', []):
        if p.get('Name') == name:
            return p
    return None


def main():
    # Load chapters
    with open(CHAPTERS, 'r', encoding='utf-8') as f:
        chapters = json.load(f)
    rows = chapters['Exports'][0]['Table']['Data']

    by_name = {r['Name']: r for r in rows}

    # ---- Task 1: Renumber ----
    task1_results = []
    for row_name, new_id in RENUMBER.items():
        row = by_name.get(row_name)
        if row is None:
            task1_results.append((row_name, None, new_id, 'ROW MISSING'))
            continue
        cid_prop = get_prop(row, 'ChapterID')
        if cid_prop is None:
            task1_results.append((row_name, None, new_id, 'NO ChapterID PROP'))
            continue
        old = cid_prop.get('Value')
        cid_prop['Value'] = new_id
        task1_results.append((row_name, old, new_id, 'OK'))

    # ---- Task 2: DisplayName audit on all 14 SS chapters ----
    task2_issues = []
    for row_name, expected_key in EXPECTED_DN.items():
        row = by_name.get(row_name)
        if row is None:
            task2_issues.append(f'{row_name}: ROW MISSING')
            continue
        dn = get_prop(row, 'DisplayName')
        if dn is None:
            task2_issues.append(f'{row_name}: DisplayName property MISSING')
            continue
        if dn.get('TableId') != EXPECTED_TABLE_ID:
            task2_issues.append(f'{row_name}: TableId={dn.get("TableId")} (expected {EXPECTED_TABLE_ID})')
        if dn.get('Value') != expected_key:
            task2_issues.append(f'{row_name}: Value={dn.get("Value")} (expected {expected_key})')
        if dn.get('HistoryType') != 'StringTableEntry':
            task2_issues.append(f'{row_name}: HistoryType={dn.get("HistoryType")} (expected StringTableEntry)')

    # ---- Task 3: StringTable key audit ----
    with open(WORLD, 'r', encoding='utf-8') as f:
        world = json.load(f)
    st_entries = world['Exports'][0]['Table']['Value']  # list of [key, value]
    st_map = {e[0]: e[1] for e in st_entries if isinstance(e, list) and len(e) >= 2}

    task3_issues = []
    for k in sorted(EXPECTED_KEYS):
        if k not in st_map:
            task3_issues.append(f'MISSING: {k}')
        elif not st_map[k] or not str(st_map[k]).strip():
            task3_issues.append(f'EMPTY: {k}')

    # ---- Task 4a: ChapterID collisions across ALL rows ----
    # Build current state
    state = []
    for r in rows:
        name = r['Name']
        zs = get_prop(r, 'ZoneSet')
        cid = get_prop(r, 'ChapterID')
        es = get_prop(r, 'EnabledState')
        state.append({
            'name': name,
            'zoneset': zs.get('Value') if zs else None,
            'chapter_id': cid.get('Value') if cid else None,
            'enabled': es.get('Value') if es else None,
        })

    # Group by ChapterID
    from collections import defaultdict
    by_cid = defaultdict(list)
    for s in state:
        by_cid[s['chapter_id']].append(s)

    task4a_collisions = []
    task4a_resolutions = []
    for cid, items in sorted(by_cid.items(), key=lambda x: (x[0] is None, x[0])):
        if len(items) > 1:
            task4a_collisions.append((cid, [(i['name'], i['zoneset'], i['enabled']) for i in items]))

    # Note: Sandbox{Small,Medium,Moria} share ZoneSet partitions; the ChapterID
    # bucket conflict matters only when rows share BOTH ZoneSet AND ChapterID
    # OR if game UI keys solely on ChapterID. We list every collision but only
    # take action on rows that share ChapterID *with* a SandboxSmall row.
    # Strategy: SandboxMedium rows are unused per project; they ALSO use our 14 DisplayName keys
    # (4b conflict). Disable SandboxMedium rows entirely — resolves both 4a and 4b for them.
    # For Moria/Expedition rows that collide on ChapterID with our SS rows, bump by +100
    # (they have distinct ZoneSets but the user wants no shared ChapterID values across Live rows).
    ss_used_cids = set(RENUMBER.values())
    task4a_disabled_medium = []
    for cid, items in by_cid.items():
        if cid not in ss_used_cids:
            continue
        ss_rows = [i for i in items if i['zoneset'] == 'EZoneSet::SandboxSmall']
        non_ss = [i for i in items if i['zoneset'] != 'EZoneSet::SandboxSmall']
        if not ss_rows or not non_ss:
            continue
        for ni in non_ss:
            r = by_name[ni['name']]
            if ni['zoneset'] == 'EZoneSet::SandboxMedium':
                # Disable the row (unused per project memory; also a 4b DisplayName conflict)
                es = get_prop(r, 'EnabledState')
                if es and es.get('Value') != 'ERowEnabledState::Disabled':
                    es['Value'] = 'ERowEnabledState::Disabled'
                    ni['enabled'] = 'ERowEnabledState::Disabled'
                    task4a_disabled_medium.append(ni['name'])
            else:
                # Bump Moria / Expedition by +100
                cprop = get_prop(r, 'ChapterID')
                if cprop is not None:
                    old = cprop['Value']
                    new = old + 100
                    cprop['Value'] = new
                    ni['chapter_id'] = new
                    task4a_resolutions.append(f'{ni["name"]} ({ni["zoneset"]}, {ni["enabled"]}): ChapterID {old} -> {new}')

    # ---- Task 4b: DisplayName key conflicts on Live non-SS chapters using our 14 keys ----
    task4b_conflicts = []
    task4b_already_disabled = []
    for r in rows:
        name = r['Name']
        if name in EXPECTED_DN:
            continue
        zs = get_prop(r, 'ZoneSet')
        zs_val = zs.get('Value') if zs else None
        es = get_prop(r, 'EnabledState')
        es_val = es.get('Value') if es else None
        dn = get_prop(r, 'DisplayName')
        if dn is None:
            continue
        if dn.get('Value') in EXPECTED_KEYS:
            line = f'{name} ({zs_val}, {es_val}): uses {dn.get("Value")}'
            if es_val == 'ERowEnabledState::Disabled':
                task4b_already_disabled.append(line)
            else:
                task4b_conflicts.append(line)

    # ---- Task 4c: Stale/orphan rows (non-SS, Live, name like SandboxSmall-chapter-15+) ----
    task4c_disabled = []
    for r in rows:
        name = r['Name']
        zs = get_prop(r, 'ZoneSet')
        es = get_prop(r, 'EnabledState')
        zs_val = zs.get('Value') if zs else None
        es_val = es.get('Value') if es else None
        # An orphan: name starts with SandboxSmall- but not in our 14 mapped rows
        if name.startswith('SandboxSmall-') and name not in RENUMBER and es_val == 'ERowEnabledState::Live':
            es['Value'] = 'ERowEnabledState::Disabled'
            task4c_disabled.append(name)

    # ---- Save ----
    with open(CHAPTERS, 'w', encoding='utf-8') as f:
        json.dump(chapters, f, indent=2, ensure_ascii=False)

    # ---- REPORT ----
    print('=== Task 1: ChapterID renumber ===')
    print(f'{"Row":40} {"Old":>5} {"New":>5} {"Status"}')
    for n, o, nw, st in task1_results:
        print(f'{n:40} {str(o):>5} {nw:>5} {st}')

    print('\n=== Task 2: DisplayName audit ===')
    if not task2_issues:
        print('All 14 SS chapters: DisplayName OK (TableId, Value, HistoryType)')
    else:
        for i in task2_issues:
            print(' -', i)

    print('\n=== Task 3: StringTable key audit ===')
    if not task3_issues:
        print('All 14 expected keys present and non-empty:')
        for k in sorted(EXPECTED_KEYS):
            print(f'  {k} = {st_map[k]!r}')
    else:
        for i in task3_issues:
            print(' -', i)

    print('\n=== Task 4a: ChapterID collisions (post-renumber) ===')
    for cid, items in task4a_collisions:
        print(f'  ChapterID={cid}:')
        for nm, zs, es in items:
            print(f'    {nm} | {zs} | {es}')
    if task4a_resolutions:
        print('\n  Resolutions applied (Moria/Expedition bumped +100):')
        for r in task4a_resolutions:
            print('   ', r)
    if task4a_disabled_medium:
        print('\n  SandboxMedium rows disabled (unused + DisplayName conflict):')
        for n in task4a_disabled_medium:
            print('   ', n)
    if not task4a_resolutions and not task4a_disabled_medium:
        print('  No resolutions needed.')

    print('\n=== Task 4b: DisplayName key conflicts on non-SS rows ===')
    if not task4b_conflicts:
        print('  No Live conflicts — our 14 keys are used only by SS chapters and disabled rows.')
    else:
        for c in task4b_conflicts:
            print(' - LIVE CONFLICT:', c)
    if task4b_already_disabled:
        print('  (Resolved via 4a — these rows are now Disabled:)')
        for c in task4b_already_disabled:
            print('   ', c)

    print('\n=== Task 4c: Stale orphan SandboxSmall rows ===')
    if not task4c_disabled:
        print('  None.')
    else:
        for n in task4c_disabled:
            print('  Disabled:', n)

if __name__ == '__main__':
    main()
