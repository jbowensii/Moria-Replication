"""Apply: set EnabledState=Disabled on chapter rows (A), zone rows (B), stair zones (C)."""
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

ZONE_ROWS_TO_DISABLE = [
    "Sandbox_Small_OrcTown_C_Gundabad",
    "Sandbox_Small_DestroyedCity_E",
    "Sandbox_Small_DestroyedCity_A_Desolation",
    "Sandbox_Small_AngryCaverns_B",
    "Sandbox_Small_DarkestDeeps_D",
    "Sandbox_Small_AngryCaverns_C",
    "Sandbox_Small_Dragon_A",
]

STAIRS_TO_DISABLE = [
    "Sandbox_Small_Elevator_EighthStair",
    "Sandbox_Small_Elevator_SixthStair",
    "Sandbox_Small_Elevator_CrystalDescent",
    "Sandbox_Small_Elevator_LowerDescent",
]

DISABLED = "ERowEnabledState::Disabled"

def load(p):
    with open(p, "r", encoding="utf-8") as f: return json.load(f)
def save(p, a):
    with open(p, "w", encoding="utf-8") as f: json.dump(a, f, indent=2)
def get_data(a):
    for e in a.get("Exports", []):
        if "Table" in e: return e["Table"]["Data"]
def find(rows, k):
    for r in rows:
        if r.get("Name") == k: return r
def field(s, n):
    for v in s.get("Value", []):
        if v.get("Name") == n: return v

def set_disabled(row, label):
    es = field(row, "EnabledState")
    if es is None:
        print(f"  ! {label}: no EnabledState field")
        return False
    before = es["Value"]
    es["Value"] = DISABLED
    print(f"  {label:55s}  {before} -> {es['Value']}")
    return True

# Chapters
ch_path = BASE / "DT_Moria_Chapters.json"
ch_doc = load(ch_path)
cr = get_data(ch_doc)
print("=== Chapter rows ===")
for cn in CHAPTER_ROWS_TO_DISABLE:
    r = find(cr, cn)
    if r is None:
        print(f"  ! MISSING {cn}")
        continue
    set_disabled(r, cn)
save(ch_path, ch_doc)

# Zones (B + C)
zn_path = BASE / "DT_Moria_Zones.json"
zn_doc = load(zn_path)
zr = get_data(zn_doc)
print("\n=== Zone rows (Section B) ===")
for zn in ZONE_ROWS_TO_DISABLE:
    r = find(zr, zn)
    if r is None:
        print(f"  ! MISSING {zn}")
        continue
    set_disabled(r, zn)

print("\n=== Stair zones (Section C) ===")
for zn in STAIRS_TO_DISABLE:
    r = find(zr, zn)
    if r is None:
        print(f"  ! MISSING {zn}")
        continue
    set_disabled(r, zn)

save(zn_path, zn_doc)
print("\nSaved DT_Moria_Chapters.json and DT_Moria_Zones.json")
print("(Section D: no cleanups required — audit confirmed all keeping stairs reference only enabled chapters.)")
