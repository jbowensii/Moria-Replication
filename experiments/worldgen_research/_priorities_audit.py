"""Pre-state audit for P1 (null-endpoint LCs) and P3 (orphan StringTable keys).

Run from the worldgen_research directory or any cwd; uses absolute paths.
"""
import json
import sys
from pathlib import Path

WGR = Path(__file__).resolve().parent

P1_TARGET_ROWS = [
    'Sandbox_DoorsOfDurinToElvenEntrance',
    'Sandbox_DoorsOfDurinToElvenQuarterA',
    'Sandbox_Small_BastionToCrossroads',
    'Sandbox_Small_ElvenQuarterToBastion',
    'Sandbox_Small_Mines_CToElvenQuarter',
    'Sandbox_Small_SuburbanDTOElevatorB',
]

P3_KEYS = [
    'Chapter.FoundationsOfStone',
    'Landmarks.Ch2.DeepMinesNexus',
    'Landmarks.Ch2.ElvenQuarterEntrance',
    'Landmarks.Ch4.BalrogsWake',
    'Zones.Names.FoundationsOfStone',
    'Zones.Names.FoundationsOfStone.Banner',
    'Zones.Names.FoundationsOfStone.Khuzdul',
    'Zones.Names.sb_Capital',
    'Zones.Names.sb_Capital.Banner',
    'Zones.Names.sb_Capital.Khuzdul',
    'Zones.Names.sb_DestroyedCity_E',
    'Zones.Names.sb_DestroyedCity_E.Banner',
    'Zones.Names.sb_DestroyedCity_E.Khuzdul',
    'Zones.Names.sb_ElvenQuarter',
    'Zones.Names.sb_GatheringHalls',
    'Zones.Names.sb_GatheringHalls.Banner',
    'Zones.Names.sb_GatheringHalls.Khuzdul',
]

# Doc map: key -> filename
DTS = {
    'zones': 'DT_Moria_Zones.json',
    'chapters': 'DT_Moria_Chapters.json',
    'biomes': 'DT_Moria_Biomes.json',
    'decks': 'DT_Moria_ZoneDeck.json',
    'filters': 'DT_Moria_ZoneBubbleFilters.json',
    'landmarks': 'DT_Moria_Landmarks.json',
    'connections': 'DT_Moria_LayoutConnections.json',
    'templates': 'DT_Moria_ZoneTemplates.json',
}


def load(name):
    p = WGR / name
    with open(p, 'r', encoding='utf-8') as f:
        return json.load(f)


def get_rows(data):
    ex = data.get('Exports', [])
    if not ex:
        return []
    table = ex[0].get('Table', {})
    return table.get('Data', []) or []


def fp(value_list, name):
    for p in value_list or []:
        if isinstance(p, dict) and p.get('Name') == name:
            return p
    return None


def get_rowname(prop):
    """Extract RowName from a struct property like OriginLandmark."""
    if not prop:
        return None
    v = prop.get('Value')
    if isinstance(v, list):
        for it in v:
            if isinstance(it, dict) and it.get('Name') == 'RowName':
                return it.get('Value', '')
    return v


def is_null(rn):
    return rn is None or rn == '' or rn == 'None'


def get_enabled_state(row):
    p = fp(row.get('Value', []), 'EnabledState')
    if not p:
        return None
    return p.get('Value', '')


def section_p1():
    print("=" * 70)
    print("SECTION A AUDIT — Priority 1: null-endpoint LayoutConnections")
    print("=" * 70)
    data = load(DTS['connections'])
    rows = get_rows(data)
    by_name = {r.get('Name'): r for r in rows if isinstance(r, dict)}
    qualifies = []
    skipped = []
    not_found = []
    for name in P1_TARGET_ROWS:
        r = by_name.get(name)
        if not r:
            not_found.append(name)
            continue
        origin = get_rowname(fp(r.get('Value', []), 'OriginLandmark'))
        dest = get_rowname(fp(r.get('Value', []), 'DestinationLandmark'))
        es = get_enabled_state(r)
        nullo = is_null(origin)
        nulld = is_null(dest)
        print(f"  {name}")
        print(f"     OriginLandmark.RowName     = {origin!r}  null={nullo}")
        print(f"     DestinationLandmark.RowName= {dest!r}  null={nulld}")
        print(f"     EnabledState               = {es}")
        if nullo and nulld:
            qualifies.append(name)
        else:
            skipped.append((name, origin, dest))
    print()
    print(f"  -> qualifies for disable: {len(qualifies)}")
    for n in qualifies:
        print(f"      {n}")
    if skipped:
        print(f"  -> SKIPPED (has valid endpoints):")
        for n, o, d in skipped:
            print(f"      {n} origin={o!r} dest={d!r}")
    if not_found:
        print(f"  -> NOT FOUND:")
        for n in not_found:
            print(f"      {n}")
    return qualifies


def find_stringtable_refs(data, doc_key, target_keys):
    """Walk every TextPropertyData with HistoryType=StringTableEntry in this
    doc; collect (row_name, target_key, path_hint)."""
    rows = get_rows(data)
    hits = []
    for r in rows:
        if not isinstance(r, dict):
            continue
        row_name = r.get('Name')
        es = get_enabled_state(r)
        # walk row tree
        stack = [(r.get('Value', []), 'Value')]
        while stack:
            obj, hint = stack.pop()
            if isinstance(obj, dict):
                t = obj.get('$type', '') or ''
                if 'TextPropertyData' in t:
                    if obj.get('HistoryType') == 'StringTableEntry':
                        v = obj.get('Value')
                        # Value may be a list of {Name, Value} pairs
                        # In UAssetGUI text is split across CultureInvariantString or
                        # nested fields. Common shape: 'Value' has list with TableId/Key.
                        # We grab any string field that matches target_keys.
                        def collect_strings(o, acc):
                            if isinstance(o, dict):
                                for vv in o.values():
                                    collect_strings(vv, acc)
                            elif isinstance(o, list):
                                for it in o:
                                    collect_strings(it, acc)
                            elif isinstance(o, str):
                                acc.append(o)
                        acc = []
                        collect_strings(obj, acc)
                        for s in acc:
                            if s in target_keys:
                                hits.append({
                                    'doc': doc_key,
                                    'row': row_name,
                                    'enabled_state': es,
                                    'key': s,
                                    'prop_name': obj.get('Name'),
                                })
                for vv in obj.values():
                    if isinstance(vv, (dict, list)):
                        stack.append((vv, hint))
            elif isinstance(obj, list):
                for it in obj:
                    if isinstance(it, (dict, list)):
                        stack.append((it, hint))
    return hits


def section_p3():
    print()
    print("=" * 70)
    print("SECTION C AUDIT — Priority 3: removed StringTable keys")
    print("=" * 70)
    target = set(P3_KEYS)
    all_hits = []
    for key, fname in DTS.items():
        try:
            data = load(fname)
        except FileNotFoundError:
            print(f"  (missing {fname})")
            continue
        hits = find_stringtable_refs(data, key, target)
        all_hits.extend(hits)
    # group by key
    by_key = {k: [] for k in P3_KEYS}
    for h in all_hits:
        by_key[h['key']].append(h)
    print()
    for k in P3_KEYS:
        hits = by_key[k]
        if not hits:
            continue  # zero-ref keys safely removed
        print(f"  {k}  -> {len(hits)} reference(s)")
        for h in hits:
            print(f"      doc={h['doc']:12s} row={h['row']!r:50s} "
                  f"prop={h['prop_name']!r}  enabled={h['enabled_state']}")
    zeros = [k for k in P3_KEYS if not by_key[k]]
    print()
    print(f"  Zero-ref keys (safely removed): {len(zeros)}/{len(P3_KEYS)}")
    for k in zeros:
        print(f"      {k}")
    return by_key


if __name__ == '__main__':
    qualifies = section_p1()
    by_key = section_p3()
    print()
    print("AUDIT DONE.")
