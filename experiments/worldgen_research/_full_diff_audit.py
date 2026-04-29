"""Field-level diff: every modified DataTable vs its .original.json sidecar.
Reports added/removed/changed rows. For Sandbox-flavoured rows, summarises
what fields changed."""
import json, os
def fp(v, n):
    for p in v or []:
        if isinstance(p, dict) and p.get('Name') == n: return p
    return None

FILES = [
    ('DT_Moria_Zones',             'Zones'),
    ('DT_Moria_Chapters',          'Chapters'),
    ('DT_Moria_Biomes',            'Biomes'),
    ('DT_Moria_Landmarks',         'Landmarks'),
    ('DT_Moria_ZoneDeck',          'ZoneDeck'),
    ('DT_Moria_ZoneBubbleFilters', 'BubbleFilters'),
    ('DT_Moria_LayoutConnections', 'LayoutConnections'),
    ('DT_Moria_ZoneTemplates',     'ZoneTemplates'),
    ('World',                      'Strings'),
]

def changed_fields(old_row, new_row):
    """Return list of (field_name, old_value, new_value) tuples for rows
    that differ at the field level. Compares serialized property values."""
    diffs = []
    if not old_row or not new_row: return diffs
    old_props = {p.get('Name'): p for p in old_row.get('Value', []) if isinstance(p, dict)}
    new_props = {p.get('Name'): p for p in new_row.get('Value', []) if isinstance(p, dict)}
    keys = set(old_props) | set(new_props)
    for k in keys:
        a = old_props.get(k)
        b = new_props.get(k)
        sa = json.dumps(a, sort_keys=True) if a else None
        sb = json.dumps(b, sort_keys=True) if b else None
        if sa != sb:
            diffs.append(k)
    return diffs

for stem, label in FILES:
    cur_p = stem + '.json'
    orig_p = stem + '.original.json'
    if not (os.path.exists(cur_p) and os.path.exists(orig_p)):
        print(f'\n--- {label} ({stem}) — no .original sidecar')
        continue
    cur = json.load(open(cur_p, encoding='utf-8'))
    orig = json.load(open(orig_p, encoding='utf-8'))

    # Compare top-level digest
    if json.dumps(cur, sort_keys=True) == json.dumps(orig, sort_keys=True):
        print(f'\n--- {label} ({stem}) — IDENTICAL to pristine')
        continue

    cur_rows = {r['Name']: r for r in cur['Exports'][0]['Table']['Data']}
    orig_rows = {r['Name']: r for r in orig['Exports'][0]['Table']['Data']}
    added = sorted(set(cur_rows) - set(orig_rows))
    removed = sorted(set(orig_rows) - set(cur_rows))
    common = sorted(set(cur_rows) & set(orig_rows))
    modified = []
    for n in common:
        if json.dumps(cur_rows[n], sort_keys=True) != json.dumps(orig_rows[n], sort_keys=True):
            modified.append(n)

    nm_cur = cur.get('NameMap', [])
    nm_orig = orig.get('NameMap', [])
    nm_added = [x for x in nm_cur if x not in set(nm_orig)]

    print(f'\n=== {label} ({stem}) ===')
    print(f'  Rows: orig={len(orig_rows)} cur={len(cur_rows)}  '
          + f'added={len(added)} removed={len(removed)} modified={len(modified)}')
    if nm_added:
        print(f'  NameMap entries added (' + str(len(nm_added)) + '):')
        for n in nm_added[:10]: print(f'    + {n}')
        if len(nm_added) > 10: print(f'    ...(+{len(nm_added)-10} more)')

    if added:
        print(f'  Added rows ({len(added)}):')
        for n in added: print(f'    + {n}')
    if removed:
        print(f'  Removed rows ({len(removed)}):')
        for n in removed: print(f'    - {n}')
    if modified:
        print(f'  Modified rows ({len(modified)}):')
        for n in modified:
            diffs = changed_fields(orig_rows[n], cur_rows[n])
            print(f'    ~ {n}  fields: {diffs}')

    # If StringTable, show the entries diff
    if stem == 'World':
        try:
            ct = cur['Exports'][0]['Table']['Value']
            ot = orig['Exports'][0]['Table']['Value']
            ckeys = {k: v for k, v in ct}
            okeys = {k: v for k, v in ot}
            new_st = sorted(set(ckeys) - set(okeys))
            del_st = sorted(set(okeys) - set(ckeys))
            chg_st = sorted(k for k in (set(ckeys) & set(okeys)) if ckeys[k] != okeys[k])
            print(f'  StringTable entries: added={len(new_st)} removed={len(del_st)} changed={len(chg_st)}')
            for k in new_st: print(f'    + {k!r} = {ckeys[k]!r}')
            for k in del_st: print(f'    - {k!r}')
            for k in chg_st: print(f'    ~ {k!r}: {okeys[k]!r} -> {ckeys[k]!r}')
        except Exception as e:
            print(f'  (could not diff StringTable: {e})')
