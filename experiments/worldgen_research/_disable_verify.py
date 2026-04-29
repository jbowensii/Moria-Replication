"""Verify disable: counts, no Live zone refs disabled chapters, validator clean."""
import json, os, importlib.util
from pathlib import Path

BASE = Path(os.path.dirname(os.path.abspath(__file__)))
SZE_PATH = r"C:\Users\johnb\OneDrive\Documents\Projects\Moria-Replication\scripts\SandboxZoneEditor.py"

EXPECTED_DISABLED_CHAPTERS = {
    "SandboxSmall-Chapter06.Level6",
    "SandboxSmall-Chapter06.OrcTown_C_Gundabad",
    "SandboxSmall-Chapter06.DestroyedCity_E",
    "SandboxSmall-Chapter07.Level7",
    "SandboxSmall-Chapter07.DestroyedCity_A_Desolation",
    "SandboxSmall-Chapter08.Deep7",
    "SandboxSmall-Chapter08.AngryCaverns_B",
    "SandboxSmall-Chapter08.DarkestDeeps_D",
    "SandboxSmall-Chapter09.Deep6",
    "SandboxSmall-Chapter09.AngryCaverns_C",
    "SandboxSmall-Chapter09.Dragon_A",
}
EXPECTED_DISABLED_ZONES = {
    "Sandbox_Small_OrcTown_C_Gundabad",
    "Sandbox_Small_DestroyedCity_E",
    "Sandbox_Small_DestroyedCity_A_Desolation",
    "Sandbox_Small_AngryCaverns_B",
    "Sandbox_Small_DarkestDeeps_D",
    "Sandbox_Small_AngryCaverns_C",
    "Sandbox_Small_Dragon_A",
    "Sandbox_Small_Elevator_EighthStair",
    "Sandbox_Small_Elevator_SixthStair",
    "Sandbox_Small_Elevator_CrystalDescent",
    "Sandbox_Small_Elevator_LowerDescent",
}

def load(p):
    with open(p,"r",encoding="utf-8") as f: return json.load(f)
def get_data(a):
    for e in a.get("Exports",[]):
        if "Table" in e: return e["Table"]["Data"]
def find(rows, k):
    for r in rows:
        if r.get("Name") == k: return r
def field(s, n):
    for v in s.get("Value", []):
        if v.get("Name") == n: return v
def get_enabled(r):
    es = field(r, "EnabledState")
    return es["Value"] if es else None
def get_chrn(z):
    ch = field(z, "Chapter")
    if not ch: return None
    for v in ch.get("Value", []):
        if v.get("Name") == "RowName": return v["Value"]
    return None
def get_addls(z):
    ach = field(z, "AdditionalChapters")
    if not ach: return []
    out = []
    for entry in ach.get("Value", []):
        for v in entry.get("Value", []):
            if v.get("Name") == "RowName": out.append(v["Value"])
    return out

zr = get_data(load(BASE / "DT_Moria_Zones.json"))
cr = get_data(load(BASE / "DT_Moria_Chapters.json"))

# 1) Disabled chapter count
ss_chapters = [r for r in cr if r.get("Name", "").startswith("SandboxSmall-")]
disabled_chaps = {r["Name"] for r in ss_chapters if get_enabled(r) == "ERowEnabledState::Disabled"}
print(f"Disabled SS chapters: {len(disabled_chaps)} (expected {len(EXPECTED_DISABLED_CHAPTERS)})")
extra = disabled_chaps - EXPECTED_DISABLED_CHAPTERS
missing = EXPECTED_DISABLED_CHAPTERS - disabled_chaps
print(f"  extra: {extra}")
print(f"  missing: {missing}")

# 2) Disabled zone count
ss_zones = [r for r in zr if r.get("Name", "").startswith("Sandbox_Small_")]
disabled_zones = {r["Name"] for r in ss_zones if get_enabled(r) == "ERowEnabledState::Disabled"}
print(f"\nDisabled SS zones (intersect expected): {len(disabled_zones & EXPECTED_DISABLED_ZONES)} of {len(EXPECTED_DISABLED_ZONES)}")
print(f"  missing: {EXPECTED_DISABLED_ZONES - disabled_zones}")

# 3) No Live zone references disabled chapter
print("\nLive zones referencing disabled chapter (should be NONE):")
violations = 0
for z in ss_zones:
    if get_enabled(z) != "ERowEnabledState::Live": continue
    chrn = get_chrn(z)
    if chrn in disabled_chaps:
        print(f"  ! {z['Name']} -> {chrn}")
        violations += 1
print(f"  violations={violations}")

# 4) No Live stair AdditionalChapters reference disabled
print("\nLive stair AdditionalChapters referencing disabled chapters (should be NONE):")
addl_violations = 0
for z in ss_zones:
    if "Elevator" not in z["Name"]: continue
    if get_enabled(z) != "ERowEnabledState::Live": continue
    bad = [a for a in get_addls(z) if a in disabled_chaps]
    if bad:
        print(f"  ! {z['Name']} addl bad={bad}")
        addl_violations += 1
print(f"  violations={addl_violations}")

# 5) Run BuildValidator
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
errors = [r for r in results if str(getattr(r,'severity','')).lower()=='error']
warnings = [r for r in results if str(getattr(r,'severity','')).lower()=='warning']
print(f"Total: {len(results)}  errors={len(errors)}  warnings={len(warnings)}")
for r in results[:80]:
    sev = getattr(r,'severity','?')
    check = getattr(r,'check','?')
    dk = getattr(r,'doc_key','?')
    detail = getattr(r,'detail','')
    print(f"  [{sev}] {check} ({dk}): {detail}")

# 6) Per-floor active zone counts: Lv-1..Lv-5, D-1..D-5
print("\n" + "=" * 80)
print("ACTIVE ZONE COUNT PER REMAINING FLOOR (Lv-1..Lv-5, D-1..D-5)")
print("=" * 80)
# Map chapter row -> Layer + ChapterID
def get_int(r, name):
    f = field(r, name)
    return f["Value"] if f else None
chap_info = {}
for r in ss_chapters:
    chap_info[r["Name"]] = {
        "Layer": get_int(r, "Layer"),
        "ChapterID": get_int(r, "ChapterID"),
        "Enabled": get_enabled(r),
    }

# Floor name from Layer: positive=Lv, negative=D? Actually Layer per the data; use the parent CID per row name.
# Simpler: bucket Live zones by their primary chapter row's Chapter01..14 prefix and the level identity row.
# We'll group by ChapterID since that's the floor.
floor_zone_counts = {}  # cid -> count of Live zones whose chapter row's CID == cid
for z in ss_zones:
    if get_enabled(z) != "ERowEnabledState::Live": continue
    chrn = get_chrn(z)
    info = chap_info.get(chrn)
    if not info: continue
    cid = info["ChapterID"]
    floor_zone_counts.setdefault(cid, []).append(z["Name"])

# Floor labels: use the Level/Deep identity rows
floor_label = {}
for r in ss_chapters:
    nm = r["Name"]
    cid = chap_info[nm]["ChapterID"]
    short = nm.split(".", 1)[1] if "." in nm else nm
    if short.startswith("Level") or short.startswith("Deep"):
        floor_label[cid] = short

# Print: keep floors Lv-1..Lv-5, D-1..D-5 (skip disabled ones via floor_label being still mapped; we filter)
KEEP_FLOORS = {"Level1","Level2","Level3","Level4","Level5","Deep1","Deep2","Deep3","Deep4","Deep5"}
for cid in sorted(floor_label.keys()):
    label = floor_label[cid]
    if label not in KEEP_FLOORS: continue
    n = len(floor_zone_counts.get(cid, []))
    print(f"  CID={cid:3d}  {label:8s}  {n} Live zones")

print("\nDone.")
