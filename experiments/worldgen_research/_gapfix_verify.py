"""Verify gap-fix:
1. Run BuildValidator.run() (import-from-file pattern)
2. Print stair coverage table for all 13 consecutive floor pairs
3. Confirm 14 level identity rows still present
"""
import sys, os, json, importlib.util
from pathlib import Path

WGR = Path(__file__).resolve().parent
SCRIPTS = WGR.parent.parent / 'scripts'

spec = importlib.util.spec_from_file_location(
    'sandbox_zone_editor', SCRIPTS / 'SandboxZoneEditor.py')
mod = importlib.util.module_from_spec(spec)
sys.modules['sandbox_zone_editor'] = mod
spec.loader.exec_module(mod)

DataTableDoc = mod.DataTableDoc
BuildValidator = mod.BuildValidator
DATATABLES = mod.DATATABLES

docs = {}
for key, (fname, stem, label) in DATATABLES.items():
    if key == 'strings':
        continue
    p = WGR / fname
    if not p.exists():
        continue
    d = DataTableDoc(key, p, stem, label)
    if d.load():
        docs[key] = d
print(f"loaded {len(docs)} DataTableDocs: {sorted(docs.keys())}")

bv = BuildValidator(docs)
print("\nRunning BuildValidator.run() ...")
issues = bv.run()
errors = [i for i in issues if i.severity == 'error']
warnings = [i for i in issues if i.severity == 'warning']
print(f"  total issues: {len(issues)}  errors: {len(errors)}  warnings: {len(warnings)}")
from collections import Counter
by_check = Counter(i.check for i in issues)
if by_check:
    print("  by check:")
    for k,c in by_check.most_common():
        print(f"    {k}: {c}")
if errors:
    print("\nERRORS (first 30):")
    for it in errors[:30]:
        print(f"  {it.check}/{it.doc_key}: {it.detail[:200]}")
if warnings:
    print("\nWARNINGS (first 30):")
    for it in warnings[:30]:
        print(f"  {it.check}/{it.doc_key}: {it.detail[:200]}")

# === Stair coverage table ===
print("\n=== STAIR COVERAGE ===")
def get_data(asset):
    for exp in asset.get("Exports", []):
        if "Table" in exp and "Data" in exp["Table"]:
            return exp["Table"]["Data"]
def find_row(rows, k):
    for r in rows:
        if r.get('Name')==k: return r
def field(struct, name):
    for v in struct.get('Value',[]):
        if v.get('Name')==name: return v
def rowname_of(struct, fname):
    f = field(struct, fname)
    if not f: return None
    for v in f.get('Value',[]):
        if v.get('Name')=='RowName': return v.get('Value')
    return None

zones = json.load(open(WGR/'DT_Moria_Zones.json'))
chapters = json.load(open(WGR/'DT_Moria_Chapters.json'))
zrows = get_data(zones); crows = get_data(chapters)

# Build chapter -> Layer index
CHAP_LAYER = {}
for r in crows:
    nm = r.get('Name')
    lf = field(r, 'Layer')
    if lf is not None:
        CHAP_LAYER[nm] = lf.get('Value')

# Layer order: 6 (Lv-7) down to -7 (D-7)
LAYER_LABEL = {
    6:'Lv-7',5:'Lv-6',4:'Lv-5',3:'Lv-4',2:'Lv-3',1:'Lv-2',0:'Lv-1',
    -1:'D-1',-2:'D-2',-3:'D-3',-4:'D-4',-5:'D-5',-6:'D-6',-7:'D-7',
}
layers_sorted = sorted(LAYER_LABEL.keys(), reverse=True)  # 6..-7

# For each stair zone, gather (primary_layer, additional_layers, name)
stairs = []
for r in zrows:
    nm = r.get('Name','')
    if 'Stair' not in nm: continue
    enf = field(r,'EnabledState')
    en = enf.get('Value') if enf else None
    if en and 'Live' not in en:  # skip non-live
        continue
    ch = rowname_of(r, 'Chapter')
    addl = field(r, 'AdditionalChapters')
    addl_names = []
    if addl:
        for ent in addl.get('Value',[]):
            for v in ent.get('Value',[]):
                if v.get('Name')=='RowName':
                    addl_names.append(v.get('Value'))
    primary_layer = CHAP_LAYER.get(ch)
    addl_layers = [CHAP_LAYER.get(a) for a in addl_names if CHAP_LAYER.get(a) is not None]
    stairs.append((nm, ch, primary_layer, addl_names, addl_layers))

# For each consecutive pair (upper, lower) where upper.layer = lower.layer + 1, find stairs spanning both
print(f"{'Pair':<14} {'Stair zones':<60}")
print('-'*80)
gaps = []
for i in range(len(layers_sorted)-1):
    upper = layers_sorted[i]; lower = layers_sorted[i+1]
    pair_label = f"{LAYER_LABEL[upper]}<->{LAYER_LABEL[lower]}"
    matching = []
    for (nm, ch, pl, an, al) in stairs:
        layers_set = set([pl] + al) - {None}
        if upper in layers_set and lower in layers_set:
            matching.append(nm.replace('Sandbox_Small_Elevator_',''))
    if not matching:
        gaps.append(pair_label)
        print(f"{pair_label:<14} *** GAP ***")
    else:
        print(f"{pair_label:<14} {', '.join(matching)}")

print()
print(f"Gaps: {len(gaps)}  -> {gaps if gaps else 'none'}")

# === 14 level identity rows present? ===
print("\n=== Level identity rows ===")
EXPECTED = [
    'SandboxSmall-Chapter01.Level1','SandboxSmall-Chapter02.Level2','SandboxSmall-Chapter03.Level3',
    'SandboxSmall-Chapter04.Level4','SandboxSmall-Chapter05.Level5','SandboxSmall-Chapter06.Level6',
    'SandboxSmall-Chapter07.Level7',
    'SandboxSmall-Chapter08.Deep7','SandboxSmall-Chapter09.Deep6','SandboxSmall-Chapter10.Deep5',
    'SandboxSmall-Chapter11.Deep4','SandboxSmall-Chapter12.Deep3','SandboxSmall-Chapter13.Deep2',
    'SandboxSmall-Chapter14.Deep1',
]
present = [k for k in EXPECTED if find_row(crows, k)]
print(f"  {len(present)}/14 level rows present")
missing = [k for k in EXPECTED if k not in present]
if missing:
    print(f"  MISSING: {missing}")

print("\nVERIFY DONE.")
