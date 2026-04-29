"""Quick inspect: list ALL Live SS non-elevator zones by primary Chapter."""
import os, json
from collections import defaultdict
BASE = os.path.dirname(os.path.abspath(__file__))
def load(p):
    with open(p, "r", encoding="utf-8") as f: return json.load(f)
def get_data(asset):
    for exp in asset.get("Exports", []):
        if "Table" in exp and "Data" in exp["Table"]:
            return exp["Table"]["Data"]
def field(s, n):
    for v in s.get("Value", []):
        if v.get("Name") == n: return v
    return None
def rowname_of(s, fn):
    f = field(s, fn)
    if not f: return None
    for v in f.get("Value", []):
        if v.get("Name") == "RowName": return v.get("Value")
def get_str(s, fn):
    f = field(s, fn); return f.get("Value") if f else None
zones = load(os.path.join(BASE, "DT_Moria_Zones.json"))
zrows = get_data(zones)
by_chap = defaultdict(list)
for r in zrows:
    nm = r.get("Name", "")
    if not nm.startswith("Sandbox_Small_"): continue
    if nm.startswith("Sandbox_Small_Elevator_"): continue
    en = get_str(r, "EnabledState")
    if en and "Live" not in en: continue
    chap = rowname_of(r, "Chapter") or "<NONE>"
    by_chap[chap].append(nm)
print(f"Total live SS non-elevator zones: {sum(len(v) for v in by_chap.values())}")
for c, names in sorted(by_chap.items()):
    print(f"\n[{c}]  count={len(names)}")
    for n in names[:20]:
        print(f"    {n}")
    if len(names) > 20:
        print(f"    ... +{len(names)-20} more")
