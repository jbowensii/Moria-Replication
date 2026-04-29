"""Audit floors to disable: Lv-6, Lv-7, D-6, D-7. Print before-state."""
import json, os
from pathlib import Path

BASE = Path(os.path.dirname(os.path.abspath(__file__)))

CHAPTER_ROWS_TO_DISABLE = [
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
]

STAIRS_TO_DISABLE = [
    "Sandbox_Small_Elevator_EighthStair",
    "Sandbox_Small_Elevator_SixthStair",
    "Sandbox_Small_Elevator_CrystalDescent",
    "Sandbox_Small_Elevator_LowerDescent",
]

def load(p):
    with open(p, "r", encoding="utf-8") as f: return json.load(f)
def get_data(a):
    for e in a.get("Exports", []):
        if "Table" in e: return e["Table"]["Data"]
def find(rows, k):
    for r in rows:
        if r.get("Name") == k: return r
def field(s, n):
    for v in s.get("Value", []):
        if v.get("Name") == n: return v

zr = get_data(load(BASE / "DT_Moria_Zones.json"))
cr = get_data(load(BASE / "DT_Moria_Chapters.json"))

def get_enabled(row):
    es = field(row, "EnabledState")
    return es["Value"] if es else None

def get_chapter_rowname(zone):
    ch = field(zone, "Chapter")
    if not ch: return None
    for v in ch.get("Value", []):
        if v.get("Name") == "RowName": return v["Value"]
    return None

def get_addl_chapter_rownames(zone):
    ach = field(zone, "AdditionalChapters")
    if not ach: return []
    out = []
    for entry in ach.get("Value", []):
        for v in entry.get("Value", []):
            if v.get("Name") == "RowName": out.append(v["Value"])
    return out

print("=" * 80)
print("SECTION A: CHAPTER ROWS TO DISABLE")
print("=" * 80)
disabled_chapter_set = set()
for cn in CHAPTER_ROWS_TO_DISABLE:
    r = find(cr, cn)
    if r is None:
        print(f"  MISSING: {cn}")
        continue
    es = get_enabled(r)
    print(f"  {cn:55s}  EnabledState={es}")
    disabled_chapter_set.add(cn)

# Find SS chapter rows even if name didn't appear (for verification)
print("\n--- All SS chapter rows currently in DT_Moria_Chapters ---")
ss_chapter_rows = [r for r in cr if r.get("Name", "").startswith("SandboxSmall-")]
for r in ss_chapter_rows:
    print(f"  {r['Name']:55s}  EnabledState={get_enabled(r)}")

print("\n" + "=" * 80)
print("SECTION B: ZONE ROWS WITH CHAPTER ON DISABLED FLOOR")
print("=" * 80)
ss_zones = [r for r in zr if r.get("Name", "").startswith("Sandbox_Small_")]
b_zones = []
for z in ss_zones:
    es = get_enabled(z)
    if es != "ERowEnabledState::Live": continue
    chrn = get_chapter_rowname(z)
    if chrn in disabled_chapter_set:
        b_zones.append((z["Name"], chrn))
        print(f"  {z['Name']:55s}  Chapter={chrn}")

print("\n" + "=" * 80)
print("SECTION C: STAIR ZONES TO DISABLE")
print("=" * 80)
for sn in STAIRS_TO_DISABLE:
    z = find(zr, sn)
    if z is None:
        print(f"  MISSING: {sn}")
        continue
    es = get_enabled(z)
    chrn = get_chapter_rowname(z)
    addl = get_addl_chapter_rownames(z)
    print(f"  {sn:45s}  ES={es}  primary={chrn}  addl={addl}")

print("\n" + "=" * 80)
print("SECTION D: KEEPING STAIR ZONES - AdditionalChapters audit")
print("=" * 80)
# Find all elevator zones still Live and not in STAIRS_TO_DISABLE
keeping_stairs = []
for z in ss_zones:
    name = z["Name"]
    if "Elevator" not in name: continue
    if name in STAIRS_TO_DISABLE: continue
    if get_enabled(z) != "ERowEnabledState::Live": continue
    keeping_stairs.append(z)

cleanups = []
for z in keeping_stairs:
    chrn = get_chapter_rowname(z)
    addl = get_addl_chapter_rownames(z)
    bad = [a for a in addl if a in disabled_chapter_set]
    flag = " <-- needs cleanup" if bad else ""
    print(f"  {z['Name']:45s}  primary={chrn}  addl={addl}{flag}")
    if bad:
        cleanups.append((z["Name"], bad))

print("\n--- Cleanups needed ---")
for n, b in cleanups:
    print(f"  {n}: remove {b}")
if not cleanups: print("  (none)")

print("\n" + "=" * 80)
print("PER-FLOOR ACTIVE ZONE COUNT (BEFORE)")
print("=" * 80)
chap_to_zones = {}
for z in ss_zones:
    if get_enabled(z) != "ERowEnabledState::Live": continue
    chrn = get_chapter_rowname(z)
    chap_to_zones.setdefault(chrn, []).append(z["Name"])
for c in sorted(chap_to_zones.keys()):
    print(f"  {c:55s}  {len(chap_to_zones[c])} zones")
