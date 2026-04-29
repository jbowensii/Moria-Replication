"""Verify floor anchors: per-floor LH counts + BuildValidator clean."""
import json, os, importlib.util
from pathlib import Path

BASE = Path(r"C:\Users\johnb\OneDrive\Documents\Projects\Moria-Replication\experiments\worldgen_research")
SZE_PATH = r"C:\Users\johnb\OneDrive\Documents\Projects\Moria-Replication\scripts\SandboxZoneEditor.py"

def load(p):
    with open(p, "r", encoding="utf-8") as f: return json.load(f)
def get_data(a):
    for e in a.get("Exports", []):
        if "Table" in e: return e["Table"]["Data"]
def field(s, n):
    for v in s.get("Value", []):
        if v.get("Name") == n: return v
def get_iv(r, fn):
    f = field(r, fn);  iv = f["Value"][0]["Value"]
    return (iv["X"], iv["Y"], iv["Z"])

zones = load(BASE / "DT_Moria_Zones.json")
zrows = get_data(zones)
zmap = {z["Name"]: z for z in zrows}

TARGETS = {
    "Lv-3": ["Sandbox_Small_City_D", "Sandbox_Small_Mines_B"],
    "Lv-4": ["Sandbox_Small_Suburban_D", "Sandbox_Small_DestroyedCity_B", "Sandbox_Small_DarkestDeeps_E"],
    "Lv-5": ["Sandbox_Small_MusteringHalls", "Sandbox_Small_OrcTown_D_Redeye", "Sandbox_Small_City_B_Dwarrowdelf"],
}

print("=" * 80)
print("PER-FLOOR LANDMARKHANDLE COUNT")
print("=" * 80)
all_ok = True
for floor, names in TARGETS.items():
    print(f"\n[{floor}]")
    for n in names:
        z = zmap.get(n)
        if not z:
            print(f"  ! {n}: missing"); all_ok = False; continue
        lh = field(z, "LandmarkHandles")
        lh_names = [e["Value"][0]["Value"][0]["Value"] for e in lh.get("Value", [])]
        ok = len(lh_names) >= 1
        if not ok: all_ok = False
        print(f"  {n:45s}  LH({len(lh_names)})={lh_names}  {'OK' if ok else 'FAIL'}")

print(f"\nAll target zones have >=1 LH: {all_ok}")

# Validate BPs are inside their host zone footprints
print("\n" + "=" * 80)
print("ORPHAN BasePosition INSIDE TARGET ZONE FOOTPRINT?")
print("=" * 80)
lms = load(BASE / "DT_Moria_Landmarks.json")
lrows = get_data(lms)
lmap = {r["Name"]: r for r in lrows}
PLAN = [
    ("Sandbox.MithrilMineNexus", "Sandbox_Small_Mines_B"),
    ("Sandbox.CrystalDescent",   "Sandbox_Small_City_D"),
    ("Sandbox.NogrodForge",      "Sandbox_Small_Suburban_D"),
    ("Sandbox.21stHall",         "Sandbox_Small_DestroyedCity_B"),
    ("Sandbox.DurinsForge",      "Sandbox_Small_DarkestDeeps_E"),
    ("Sandbox.MithrilForge",     "Sandbox_Small_MusteringHalls"),
    ("Sandbox.BalrogsNest",      "Sandbox_Small_OrcTown_D_Redeye"),
]
for orphan, zone_name in PLAN:
    z = zmap[zone_name]
    p = get_iv(z, "Position"); s = get_iv(z, "TargetSize")
    bp = get_iv(lmap[orphan], "BasePosition")
    inside = (p[0] <= bp[0] < p[0]+s[0] and
              p[1] <= bp[1] < p[1]+s[1] and
              p[2] <= bp[2] < p[2]+s[2])
    print(f"  {orphan:32s} BP={bp}  zone {zone_name} {p}+{s}  inside={inside}")

# BuildValidator
print("\n" + "=" * 80)
print("BUILD VALIDATOR")
print("=" * 80)
spec = importlib.util.spec_from_file_location("sze", SZE_PATH)
sze = importlib.util.module_from_spec(spec)
spec.loader.exec_module(sze)
docs = {}
for k, (fname, stem, label) in sze.DATATABLES.items():
    doc = sze.DataTableDoc(k, BASE / fname, stem, label)
    if doc.load():
        docs[k] = doc
results = sze.BuildValidator(docs).run()
errors = [r for r in results if str(getattr(r, 'severity', '')).lower() == 'error']
warnings = [r for r in results if str(getattr(r, 'severity', '')).lower() == 'warning']
print(f"Total: {len(results)}  errors={len(errors)}  warnings={len(warnings)}")
for r in results[:60]:
    sev = getattr(r, 'severity', '?')
    check = getattr(r, 'check', '?')
    dk = getattr(r, 'doc_key', '?')
    detail = getattr(r, 'detail', '')
    print(f"  [{sev}] {check} ({dk}): {detail}")

print("\nDone.")
