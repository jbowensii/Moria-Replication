"""_crash_validate.py — run BuildValidator against the on-disk DTs."""
import sys
from pathlib import Path

WGR = Path(__file__).resolve().parent
PROJ = WGR.parent.parent
sys.path.insert(0, str(PROJ / 'scripts'))

# tkinter import is required by SandboxZoneEditor at module-load — fine.
from SandboxZoneEditor import DataTableDoc, BuildValidator, DATATABLES, WGR_DIR

docs = {}
for k, (fname, stem, label) in DATATABLES.items():
    d = DataTableDoc(k, WGR_DIR / fname, stem, label)
    if d.load():
        docs[k] = d

print(f'Loaded {len(docs)} docs')
v = BuildValidator(docs)
issues = v.run()
errs = [i for i in issues if i.severity == 'error']
warns = [i for i in issues if i.severity == 'warning']
print(f'Validator: {len(errs)} errors, {len(warns)} warnings')
for it in issues:
    print(f'  [{it.severity}] {it.code}: {(it.message or "")[:200]}')
