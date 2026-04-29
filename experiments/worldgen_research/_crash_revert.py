"""_crash_revert.py — Surgical revert for the routing-fix crash.

Strategy (Option B): keep all 13 new LC rows (they match the working template),
but revert the 22 new GuaranteedConnections entries. The GC chain demanded
edges the LC graph cannot fulfill (10 GC arrows have no LC in EITHER direction).

Backups:
  DT_Moria_Landmarks.before_crash_diag.json
"""
import json, shutil
from pathlib import Path

WGR = Path(__file__).resolve().parent

LM_PATH      = WGR / 'DT_Moria_Landmarks.json'
LM_PRE_PATH  = WGR / 'DT_Moria_Landmarks.before_lvfix.json'
LM_BACKUP    = WGR / 'DT_Moria_Landmarks.before_crash_diag.json'

print('Backup current Landmarks ->', LM_BACKUP.name)
shutil.copy2(LM_PATH, LM_BACKUP)

with open(LM_PATH, 'r', encoding='utf-8') as f: cur_doc = json.load(f)
with open(LM_PRE_PATH, 'r', encoding='utf-8') as f: pre_doc = json.load(f)

def rows_of(doc):
    return doc['Exports'][0]['Table']['Data']

cur_rows = rows_of(cur_doc)
pre_rows = rows_of(pre_doc)
pre_by_name = {r.get('Name'): r for r in pre_rows}

# For each landmark in the routing-fix chain, replace its GuaranteedConnections
# property with the pre-routing-fix version.
TARGETS = {
    'Sandbox.CrystalDescent', 'Sandbox.LowerDescent',
    'Sandbox.FirstStair', 'Sandbox.SecondStair', 'Sandbox.ThirdStair',
    'Sandbox.FourthStair', 'Sandbox.SixthStair', 'Sandbox.SeventhStair',
    'Sandbox.EighthStair', 'Sandbox.NinthStair',
    'Sandbox.TenthStair', 'Sandbox.EleventhStair',
}

def find_gc(row):
    for i, p in enumerate(row.get('Value', [])):
        if isinstance(p, dict) and p.get('Name') == 'GuaranteedConnections':
            return i, p
    return -1, None

reverted = 0
for r in cur_rows:
    n = r.get('Name')
    if n not in TARGETS: continue
    pre = pre_by_name.get(n)
    if not pre:
        print(f'  WARNING: no pre-routing version of {n}; skipping')
        continue
    cur_idx, cur_gc = find_gc(r)
    pre_idx, pre_gc = find_gc(pre)
    if cur_idx < 0:
        print(f'  WARNING: no GC field on current {n}'); continue
    if pre_idx < 0:
        # pre version had no GC at all — drop the whole property from current
        del r['Value'][cur_idx]
        print(f'  {n}: removed GuaranteedConnections (none in pre)')
    else:
        # Deep-copy the pre GC property over the current one
        r['Value'][cur_idx] = json.loads(json.dumps(pre_gc))
        # Count entries
        before = len(cur_gc.get('Value') or [])
        after  = len(pre_gc.get('Value') or [])
        print(f'  {n}: GC entries {before} -> {after} (reverted to pre-routing-fix)')
    reverted += 1

# Ensure NameMap counters stay consistent — bump if any property removed
nm = cur_doc.get('NameMap', [])
n = len(nm)
cur_doc['NamesReferencedFromExportDataCount'] = n
gens = cur_doc.get('Generations') or []
if gens and isinstance(gens[0], dict):
    gens[0]['NameCount'] = n

with open(LM_PATH, 'w', encoding='utf-8') as f:
    json.dump(cur_doc, f, indent=2)

print(f'\nDone. Reverted GC for {reverted} landmark(s). Wrote {LM_PATH.name}.')
