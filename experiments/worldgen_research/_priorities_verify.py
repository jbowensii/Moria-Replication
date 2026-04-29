"""Verify P1+P2 by importing the patched editor and running BuildValidator.run().
"""
import sys
import importlib.util
from pathlib import Path

WGR = Path(__file__).resolve().parent
SCRIPTS = WGR.parent.parent / 'scripts'

# Load the editor module without executing the GUI bootstrap. The module
# guards GUI startup behind `if __name__ == '__main__':`, so importing is safe.
spec = importlib.util.spec_from_file_location(
    'sandbox_zone_editor', SCRIPTS / 'SandboxZoneEditor.py')
mod = importlib.util.module_from_spec(spec)
sys.modules['sandbox_zone_editor'] = mod
spec.loader.exec_module(mod)

DataTableDoc = mod.DataTableDoc
BuildValidator = mod.BuildValidator
DATATABLES = mod.DATATABLES

# Build docs dict pointing at WGR_DIR JSONs
docs = {}
for key, (fname, stem, label) in DATATABLES.items():
    if key == 'strings':
        continue  # StringTable lacks DT row shape; not used by validator core
    p = WGR / fname
    if not p.exists():
        continue
    d = DataTableDoc(key, p, stem, label)
    if d.load():
        docs[key] = d

print(f"loaded {len(docs)} DataTableDocs: {sorted(docs.keys())}")

bv = BuildValidator(docs)
checks = bv.CHECKS
names = [c.__name__ for c in checks]
print(f"CHECKS list ({len(checks)} checks):")
for n in names:
    flag = '<-- new' if n == '_check_connection_null_endpoints' else ''
    print(f"   {n} {flag}")

assert '_check_connection_null_endpoints' in names, "new check not in CHECKS!"

print()
print("Running BuildValidator.run() ...")
issues = bv.run()
errors = [i for i in issues if i.severity == 'error']
warnings = [i for i in issues if i.severity == 'warning']
print(f"  total issues: {len(issues)}")
print(f"  errors:       {len(errors)}")
print(f"  warnings:     {len(warnings)}")

# Group by check id
from collections import Counter
by_check = Counter(i.check for i in issues)
print()
print("by check:")
for k, c in by_check.most_common():
    print(f"  {k}: {c}")

# Verify the new check would catch null endpoints if any existed.
# Synthesize a test by temporarily injecting a null-endpoint Live row in memory.
print()
print("=== smoke test: inject a fake Live null-endpoint row ===")
conns = docs['connections']
# duplicate last row, mutate
import copy, json
row = copy.deepcopy(conns.rows[0])
row['Name'] = '__TEST_NULL_ENDPOINTS__'
# Force EnabledState=Live and Origin/Dest RowName='None'
def fp(vl, n):
    for p in vl or []:
        if isinstance(p, dict) and p.get('Name') == n:
            return p
    return None
es = fp(row.get('Value', []), 'EnabledState')
if es: es['Value'] = 'ERowEnabledState::Live'
for fld in ('OriginLandmark', 'DestinationLandmark'):
    p = fp(row.get('Value', []), fld)
    if p:
        for it in (p.get('Value') or []):
            if isinstance(it, dict) and it.get('Name') == 'RowName':
                it['Value'] = 'None'
conns.rows.append(row)
test_issues = bv._check_connection_null_endpoints()
print(f"  injected one null-endpoint Live row; check returned {len(test_issues)} issue(s)")
for it in test_issues:
    print(f"    {it.severity} {it.check}: {it.detail[:120]}")
# remove fake row
conns.rows.pop()
assert any('__TEST_NULL_ENDPOINTS__' in i.detail for i in test_issues), \
    'new check did not catch synthetic null-endpoint row!'

# Show that disabled LCs are NOT flagged by other checks.
print()
print("=== check disabled LCs are not flagged ===")
DISABLED = {
    'Sandbox_DoorsOfDurinToElvenEntrance',
    'Sandbox_DoorsOfDurinToElvenQuarterA',
    'Sandbox_Small_BastionToCrossroads',
    'Sandbox_Small_ElvenQuarterToBastion',
    'Sandbox_Small_Mines_CToElvenQuarter',
    'Sandbox_Small_SuburbanDTOElevatorB',
}
flagged = []
for it in issues:
    for n in DISABLED:
        if n in (it.detail or ''):
            flagged.append((n, it.check, it.severity))
if flagged:
    print(f"  WARNING: disabled LCs appear in issues:")
    for n, c, s in flagged:
        print(f"    {n} -> {s} {c}")
else:
    print("  none of the 6 disabled LCs are flagged by any check.")

# Print remaining errors with detail
print()
if errors:
    print("=== remaining errors (post-fix) ===")
    for it in errors:
        print(f"  {it.check}/{it.doc_key}: {it.detail[:200]}")
else:
    print("=== 0 errors ===")

print()
print("VERIFY DONE.")
