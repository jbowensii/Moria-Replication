"""Hard scrub of the 7 restored trial-1 files. Looks for every defect class
we've identified across this debugging arc:

1. Cross-DT row references that don't resolve
2. Duplicate row names within a DT
3. Empty StructProperty arrays missing DummyStruct
4. EnabledState values not a recognized enum
5. RowHandle.RowName pointing at a Disabled/Cooked row
6. NameMap consistency (final verify)
7. Imports table FNames present in NameMap
8. Duplicate NameMap entries
9. Counter sync (NamesReferencedFromExportDataCount, Generations[0].NameCount)
"""
import json
from pathlib import Path

HERE = Path(__file__).parent
TRIAL1_FILES = ['DT_Moria_Chapters', 'DT_Moria_Landmarks', 'DT_Moria_LayoutConnections',
                'DT_Moria_ZoneBubbleFilters', 'DT_Moria_ZoneDeck', 'DT_Moria_Zones', 'World']
EXTRA_FILES = ['DT_Moria_Biomes', 'DT_Moria_ZoneTemplates', 'DT_Moria_AdditiveZonePass']


def load(stem):
    return json.loads((HERE / f'{stem}.json').read_text(encoding='utf-8'))


def fp(v, n):
    for p in v or []:
        if isinstance(p, dict) and p.get('Name') == n:
            return p
    return None


def get(r, k):
    p = fp(r['Value'], k)
    if not p:
        return None
    v = p.get('Value')
    if isinstance(v, list):
        for it in v:
            if isinstance(it, dict) and it.get('Name') == 'RowName':
                return it.get('Value', '')
    return v


def zstate(r):
    p = fp(r['Value'], 'EnabledState')
    return str(p.get('Value', '')).split('::')[-1] if p else None


def main():
    docs = {s: load(s) for s in TRIAL1_FILES + EXTRA_FILES}

    def rowset(stem):
        return {r['Name'] for r in docs[stem]['Exports'][0].get('Table', {}).get('Data', [])}

    def live_rowset(stem):
        return {r['Name'] for r in docs[stem]['Exports'][0].get('Table', {}).get('Data', [])
                if zstate(r) != 'Disabled'}

    issues = []

    # ---- 1: Duplicate row names ----
    print('=== 1: Duplicate row names within each DT ===')
    for stem in TRIAL1_FILES:
        seen = {}
        for r in docs[stem]['Exports'][0].get('Table', {}).get('Data', []):
            seen[r['Name']] = seen.get(r['Name'], 0) + 1
        dups = {k: c for k, c in seen.items() if c > 1}
        if dups:
            issues.append((stem, 'duplicate rows', dups))
            print(f'  {stem}: {dups}')
        else:
            print(f'  {stem}: OK')

    # ---- 2: Duplicate NameMap entries ----
    print('\n=== 2: Duplicate NameMap entries ===')
    for stem in TRIAL1_FILES:
        nm = docs[stem].get('NameMap', [])
        seen = {}
        for s in nm:
            seen[s] = seen.get(s, 0) + 1
        dups = {k: c for k, c in seen.items() if c > 1}
        if dups:
            issues.append((stem, 'dup NameMap', dups))
            print(f'  {stem}: {len(dups)} dups')
            for k, c in list(dups.items())[:5]:
                print(f'    {c}x  {k!r}')
        else:
            print(f'  {stem}: OK ({len(nm)} entries)')

    # ---- 3: Cross-DT references ----
    print('\n=== 3: Cross-DT references resolve ===')
    chapter_rows = rowset('DT_Moria_Chapters')
    zonedeck_rows = rowset('DT_Moria_ZoneDeck')
    landmark_rows = rowset('DT_Moria_Landmarks')
    zonetemplate_rows = rowset('DT_Moria_ZoneTemplates')
    add_pass_rows = rowset('DT_Moria_AdditiveZonePass')
    zone_rows = rowset('DT_Moria_Zones')

    # 'None' is the null-FName sentinel — not a missing reference
    NULL_FNAMES = {'None', 'Null', ''}
    broken_z = []
    for r in docs['DT_Moria_Zones']['Exports'][0]['Table']['Data']:
        n = r['Name']
        for fld, target in (('Chapter', chapter_rows),
                            ('BubbleDeck', zonedeck_rows),
                            ('PassageDeck', zonedeck_rows),
                            ('Template', zonetemplate_rows),
                            ('AdditiveZonePass', add_pass_rows)):
            v = get(r, fld)
            if v and v not in NULL_FNAMES and v not in target:
                broken_z.append((n, fld, v))
        ac = fp(r['Value'], 'AdditionalChapters')
        if ac:
            for it in (ac.get('Value') or []):
                inner = it.get('Value') if isinstance(it, dict) else None
                if isinstance(inner, list):
                    for sub in inner:
                        if isinstance(sub, dict) and sub.get('Name') == 'RowName':
                            v = sub.get('Value', '')
                            if v and v not in chapter_rows:
                                broken_z.append((n, 'AdditionalChapters', v))
        lh = fp(r['Value'], 'LandmarkHandles')
        if lh:
            for e in (lh.get('Value') or []):
                inner = e.get('Value') if isinstance(e, dict) else None
                if isinstance(inner, list):
                    for sub in inner:
                        if isinstance(sub, dict) and sub.get('Name') == 'Landmark':
                            for it in (sub.get('Value') or []):
                                if isinstance(it, dict) and it.get('Name') == 'RowName':
                                    v = it.get('Value', '')
                                    if v and v not in landmark_rows:
                                        broken_z.append((n, 'LandmarkHandles', v))
    print(f'  Zones: {len(broken_z)} broken')
    for b in broken_z[:20]:
        print(f'    {b}')
    if broken_z:
        issues.append(('Zones', 'broken refs', broken_z))

    broken_lc = []
    for r in docs['DT_Moria_LayoutConnections']['Exports'][0]['Table']['Data']:
        n = r['Name']
        for fld, target in (('OriginZone', zone_rows),
                            ('DestinationZone', zone_rows),
                            ('OriginLandmark', landmark_rows),
                            ('DestinationLandmark', landmark_rows)):
            v = get(r, fld)
            if v and v not in NULL_FNAMES and v not in target:
                broken_lc.append((n, fld, v))
    print(f'  LayoutConnections: {len(broken_lc)} broken')
    for b in broken_lc[:20]:
        print(f'    {b}')
    if broken_lc:
        issues.append(('LayoutConnections', 'broken refs', broken_lc))

    # ---- 4: Empty struct arrays missing DummyStruct ----
    print('\n=== 4: Empty StructProperty arrays missing DummyStruct ===')

    def check_arrays(stem):
        bad = []

        def walk(obj, path=''):
            if isinstance(obj, dict):
                t = obj.get('$type', '')
                if 'ArrayPropertyData' in t and obj.get('ArrayType') == 'StructProperty':
                    v = obj.get('Value') or []
                    if not v and not obj.get('DummyStruct'):
                        bad.append(f'{path}.{obj.get("Name","?")}')
                for k, val in obj.items():
                    walk(val, f'{path}.{k}')
            elif isinstance(obj, list):
                for i, it in enumerate(obj):
                    walk(it, f'{path}[{i}]')

        walk(docs[stem].get('Exports', []))
        return bad

    for stem in TRIAL1_FILES:
        bad = check_arrays(stem)
        if bad:
            issues.append((stem, 'empty arrays no DummyStruct', bad))
            print(f'  {stem}: {len(bad)}')
            for b in bad[:5]:
                print(f'    {b}')
        else:
            print(f'  {stem}: OK')

    # ---- 5: EnabledState valid ----
    print('\n=== 5: EnabledState values ===')
    # ERowEnabledState::Test is used by vanilla Test_* LayoutConnection rules
    VALID = {'ERowEnabledState::Live', 'ERowEnabledState::Disabled',
             'ERowEnabledState::CookedOut', 'ERowEnabledState::Test'}
    for stem in TRIAL1_FILES:
        bad = []
        for r in docs[stem]['Exports'][0].get('Table', {}).get('Data', []):
            p = fp(r['Value'], 'EnabledState')
            if p and p.get('Value') not in VALID:
                bad.append((r['Name'], p.get('Value')))
        if bad:
            issues.append((stem, 'invalid EnabledState', bad))
            print(f'  {stem}: {bad[:5]}')
        else:
            print(f'  {stem}: OK')

    # ---- 6: RowHandle pointing at Disabled rows ----
    print('\n=== 6: Live zones referencing Disabled chapter / landmark / deck rows ===')
    disabled_chap = rowset('DT_Moria_Chapters') - live_rowset('DT_Moria_Chapters')
    disabled_lm = rowset('DT_Moria_Landmarks') - live_rowset('DT_Moria_Landmarks')
    disabled_deck = rowset('DT_Moria_ZoneDeck') - live_rowset('DT_Moria_ZoneDeck')
    risky = []
    for r in docs['DT_Moria_Zones']['Exports'][0]['Table']['Data']:
        if zstate(r) == 'Disabled':
            continue
        n = r['Name']
        c = get(r, 'Chapter')
        if c in disabled_chap:
            risky.append((n, 'Chapter (disabled)', c))
        for fld in ('BubbleDeck', 'PassageDeck'):
            d = get(r, fld)
            if d in disabled_deck:
                risky.append((n, f'{fld} (disabled)', d))
        lh = fp(r['Value'], 'LandmarkHandles')
        if lh:
            for e in (lh.get('Value') or []):
                inner = e.get('Value') if isinstance(e, dict) else None
                if isinstance(inner, list):
                    for sub in inner:
                        if isinstance(sub, dict) and sub.get('Name') == 'Landmark':
                            for it in (sub.get('Value') or []):
                                if isinstance(it, dict) and it.get('Name') == 'RowName':
                                    v = it.get('Value', '')
                                    if v in disabled_lm:
                                        risky.append((n, 'Landmark (disabled)', v))
    print(f'  {len(risky)} risky')
    for r in risky[:20]:
        print(f'    {r}')
    if risky:
        issues.append(('Zones', 'live row refs disabled target', risky))

    # ---- 7: All export-data FName refs in NameMap ----
    print('\n=== 7: NameMap completeness ===')
    FNAME_PROPS = {'RowName', 'TagName', 'Bubble', 'BaseBubbleName'}
    for stem in TRIAL1_FILES:
        d = docs[stem]
        nm = set(d.get('NameMap', []))
        missing = []

        def walk(obj):
            if isinstance(obj, dict):
                n = obj.get('Name'); v = obj.get('Value')
                t = obj.get('$type', '') or ''
                if n in FNAME_PROPS and isinstance(v, str) and v and v != 'None':
                    if v not in nm:
                        missing.append((n, v))
                if 'EnumPropertyData' in t:
                    et = obj.get('EnumType')
                    if et and et not in nm:
                        missing.append(('EnumType', et))
                    if isinstance(v, str) and v not in nm:
                        missing.append(('EnumValue', v))
                        if '::' in v and v.split('::', 1)[0] not in nm:
                            missing.append(('EnumBareType', v.split('::', 1)[0]))
                st = obj.get('StructType')
                if st and st != 'Generic' and st not in nm:
                    missing.append(('StructType', st))
                for val in obj.values():
                    walk(val)
            elif isinstance(obj, list):
                for it in obj:
                    walk(it)

        walk(d.get('Exports', []))
        for r in d['Exports'][0].get('Table', {}).get('Data', []):
            if r.get('Name') and r['Name'] not in nm:
                missing.append(('RowName(table)', r['Name']))
        if missing:
            issues.append((stem, 'NameMap missing', missing))
            print(f'  {stem}: {len(missing)} missing')
            for m in missing[:5]:
                print(f'    {m}')
        else:
            print(f'  {stem}: OK ({len(nm)} entries)')

    # ---- 8: Imports table names ----
    print('\n=== 8: Imports table FNames in NameMap ===')
    for stem in TRIAL1_FILES:
        d = docs[stem]
        nm = set(d.get('NameMap', []))
        missing = []
        for imp in d.get('Imports', []):
            for k in ('ObjectName', 'ClassPackage', 'ClassName', 'PackageName'):
                v = imp.get(k)
                if isinstance(v, str) and v and v != 'None' and v not in nm:
                    missing.append((k, v))
        if missing:
            issues.append((stem, 'Imports FNames missing', missing))
            print(f'  {stem}: {len(missing)}')
            for m in missing[:5]:
                print(f'    {m}')
        else:
            print(f'  {stem}: OK')

    # ---- 9: Counter sync ----
    print('\n=== 9: Counter sync (NamesRef + Generations[0].NameCount) ===')
    for stem in TRIAL1_FILES:
        d = docs[stem]
        n = len(d.get('NameMap', []))
        nr = d.get('NamesReferencedFromExportDataCount')
        gens = d.get('Generations') or []
        gn = gens[0].get('NameCount') if gens and isinstance(gens[0], dict) else None
        if nr != n or gn != n:
            issues.append((stem, 'counter mismatch', {'NameMap': n, 'NamesRef': nr, 'Gen.NameCount': gn}))
            print(f'  {stem}: NM={n} NR={nr} Gen={gn}  MISMATCH')
        else:
            print(f'  {stem}: OK ({n})')

    print('\n=== SUMMARY ===')
    if not issues:
        print('ALL 7 FILES CLEAN — no issues detected.')
    else:
        print(f'{len(issues)} issue groups detected.')
        for (stem, kind, _) in issues:
            print(f'  {stem}: {kind}')


if __name__ == '__main__':
    main()
