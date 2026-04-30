"""Apply 9-zone chain connections + disable conflicting vanilla elevators.

Part 1: Disable vanilla full-stack elevators (Elevator_C/D/E/F) and any
LayoutConnections referencing them. Clear bExtendedConnectivityLandmark
on Sandbox_Small_Mines_C's Sandbox.Deep1MineNexus landmark entry (it's a
chapter transition, not a stair).

Part 2: Add 9 zone-to-zone bRequired LayoutConnections cloned from the
Sandbox_Small_GhashOrcTown_To_Descent template.
"""
from __future__ import annotations
import copy
import json
from pathlib import Path

ROOT = Path(r"C:\Users\johnb\OneDrive\Documents\Projects\Moria-Replication\experiments\worldgen_research")
ZN_PATH = ROOT / "DT_Moria_Zones.json"
LM_PATH = ROOT / "DT_Moria_Landmarks.json"
LC_PATH = ROOT / "DT_Moria_LayoutConnections.json"

def load(p): return json.load(open(p, "r", encoding="utf-8"))
def save(p, d): json.dump(d, open(p, "w", encoding="utf-8"), indent=2)

zn = load(ZN_PATH)
lm = load(LM_PATH)
lc = load(LC_PATH)

z_rows = zn["Exports"][0]["Table"]["Data"]
l_rows = lm["Exports"][0]["Table"]["Data"]
c_rows = lc["Exports"][0]["Table"]["Data"]

def get_prop(row, name):
    for v in row["Value"]:
        if v.get("Name") == name:
            return v
    return None

def name_val(prop):
    if prop is None: return None
    return prop["Value"][0]["Value"]

def set_name_val(prop, new):
    prop["Value"][0]["Value"] = new

# ---------------------------------------------------------------------
# Part 1a — Mines_C: clear bExtendedConnectivityLandmark on Deep1MineNexus
# ---------------------------------------------------------------------
print("== Part 1a: Mines_C bExtendedConnectivityLandmark flag clear ==")
mines_c = next(r for r in z_rows if r["Name"] == "Sandbox_Small_Mines_C")
lh = get_prop(mines_c, "LandmarkHandles")
cleared = 0
for entry in lh["Value"]:
    # entry has children: Landmark (RowHandle), Placement, bExtendedConnectivityLandmark
    children = entry["Value"]
    landmark_handle = next(c for c in children if c.get("Name") == "Landmark")
    lm_name = landmark_handle["Value"][0]["Value"]
    if lm_name == "Sandbox.Deep1MineNexus":
        for c in children:
            if c.get("Name") == "bExtendedConnectivityLandmark":
                if c["Value"]:
                    c["Value"] = False
                    cleared += 1
                    print(f"  cleared on {lm_name}")
print(f"  cleared {cleared} flag(s)")

# ---------------------------------------------------------------------
# Part 1b — Disable vanilla elevators C/D/E/F
# ---------------------------------------------------------------------
print("\n== Part 1b: Disable vanilla full-stack elevators ==")
DISABLE_ZONES = {"Sandbox_Small_Elevator_C", "Sandbox_Small_Elevator_D",
                 "Sandbox_Small_Elevator_E", "Sandbox_Small_Elevator_F"}
disabled_zones = []
for r in z_rows:
    if r["Name"] in DISABLE_ZONES:
        es = get_prop(r, "EnabledState")
        if es["Value"] != "ERowEnabledState::Disabled":
            es["Value"] = "ERowEnabledState::Disabled"
            disabled_zones.append(r["Name"])
            print(f"  disabled zone {r['Name']}")

# ---------------------------------------------------------------------
# Part 1c — Disable vanilla connections referencing disabled elevators
# ---------------------------------------------------------------------
print("\n== Part 1c: Disable connections referencing disabled elevators ==")
TARGET_LMS = {"Sandbox.SecondStair", "Sandbox.ThirdStair",
              "Sandbox.FourthStair", "Sandbox.FifthStair"}
disabled_conns = []
for r in c_rows:
    ol = name_val(get_prop(r, "OriginLandmark"))
    dl = name_val(get_prop(r, "DestinationLandmark"))
    oz = name_val(get_prop(r, "OriginZone"))
    dz = name_val(get_prop(r, "DestinationZone"))
    if (ol in TARGET_LMS or dl in TARGET_LMS or
        oz in DISABLE_ZONES or dz in DISABLE_ZONES):
        es = get_prop(r, "EnabledState")
        if es["Value"] != "ERowEnabledState::Disabled":
            es["Value"] = "ERowEnabledState::Disabled"
            disabled_conns.append((r["Name"], oz, ol, dz, dl))
            print(f"  disabled {r['Name']}: OZ={oz} OL={ol} DZ={dz} DL={dl}")

# ---------------------------------------------------------------------
# Part 2 — Add 9 chain connections cloned from Ghash template
# ---------------------------------------------------------------------
print("\n== Part 2: Add 9 chain connections ==")
TEMPLATE_NAME = "Sandbox_Small_GhashOrcTown_To_Descent"
template = next(r for r in c_rows if r["Name"] == TEMPLATE_NAME)

CHAIN = [
    ("Sandbox_Small_Chain_TopElToLv3Lv4",     "Sandbox_Small_TopElevator",     "Sandbox.TopElevator",     "Sandbox_Small_Lv3Lv4Connector", "Sandbox.Lv3Lv4Connector"),
    ("Sandbox_Small_Chain_Lv3Lv4ToUpperEl",   "Sandbox_Small_Lv3Lv4Connector", "Sandbox.Lv3Lv4Connector", "Sandbox_Small_Elevator_B",      "Sandbox.FirstStair"),
    ("Sandbox_Small_Chain_UpperElToD1Lv1",    "Sandbox_Small_Elevator_B",      "Sandbox.FirstStair",      "Sandbox_Small_D1Lv1Connector",  "Sandbox.D1Lv1Connector"),
    ("Sandbox_Small_Chain_D1Lv1ToDeepUpper",  "Sandbox_Small_D1Lv1Connector",  "Sandbox.D1Lv1Connector",  "Sandbox_Small_DeepUpperEl",     "Sandbox.DeepUpperEl"),
    ("Sandbox_Small_Chain_DeepUpperToDeepMid","Sandbox_Small_DeepUpperEl",     "Sandbox.DeepUpperEl",     "Sandbox_Small_DeepMidEl",       "Sandbox.DeepMidEl"),
    ("Sandbox_Small_Chain_DeepMidToD4D3",     "Sandbox_Small_DeepMidEl",       "Sandbox.DeepMidEl",       "Sandbox_Small_D4D3Connector",   "Sandbox.D4D3Connector"),
    ("Sandbox_Small_Chain_D4D3ToDeepBottom",  "Sandbox_Small_D4D3Connector",   "Sandbox.D4D3Connector",   "Sandbox_Small_DeepBottomEl",    "Sandbox.DeepBottomEl"),
    ("Sandbox_Small_Chain_DeepBottomToCD",    "Sandbox_Small_DeepBottomEl",    "Sandbox.DeepBottomEl",    "Sandbox_Small_CrystalDescent",  "Chapter3.CrystalDescent"),
    ("Sandbox_Small_Chain_CDToD7D6",          "Sandbox_Small_CrystalDescent",  "Chapter3.CrystalDescent", "Sandbox_Small_D7D6Stair",       "Sandbox.D7D6Stair"),
]

existing_names = {r["Name"] for r in c_rows}
added_rows = []
for new_name, oz, ol, dz, dl in CHAIN:
    if new_name in existing_names:
        print(f"  SKIP {new_name} (already present)")
        continue
    clone = copy.deepcopy(template)
    clone["Name"] = new_name
    set_name_val(get_prop(clone, "OriginZone"), oz)
    set_name_val(get_prop(clone, "OriginLandmark"), ol)
    set_name_val(get_prop(clone, "DestinationZone"), dz)
    set_name_val(get_prop(clone, "DestinationLandmark"), dl)
    # Ensure flags
    get_prop(clone, "bRequired")["Value"] = True
    get_prop(clone, "bExclusive")["Value"] = False
    get_prop(clone, "EnabledState")["Value"] = "ERowEnabledState::Live"
    get_prop(clone, "ZoneSet")["Value"] = "EZoneSet::SandboxSmall"
    c_rows.append(clone)
    added_rows.append(new_name)
    print(f"  +{new_name}: {oz}/{ol} -> {dz}/{dl}")

# ---------------------------------------------------------------------
# NameMap sync
# ---------------------------------------------------------------------
print("\n== NameMap sync ==")
def add_nm(d, names, label):
    nm = d.get("NameMap", [])
    existing = set(nm)
    added = 0
    for n in names:
        if n is None: continue
        if n not in existing:
            nm.append(n); existing.add(n); added += 1
    d["NameMap"] = nm
    if "NamesReferencedFromExportDataCount" in d:
        d["NamesReferencedFromExportDataCount"] = len(nm)
    exp0 = d["Exports"][0]
    if "Generations" in d and d["Generations"]:
        d["Generations"][0]["NameCount"] = len(nm)
    print(f"  {label}: +{added} (total {len(nm)})")
    return added

# All names referenced by new rows / new property values
lc_names = []
for nm_, oz, ol, dz, dl in CHAIN:
    lc_names += [nm_, oz, ol, dz, dl]
add_nm(lc, lc_names, "LayoutConnections")
# Zones: nothing new (only flag flips and EnabledState changes)
# Landmarks: nothing new
add_nm(zn, [], "Zones (no-op)")
add_nm(lm, [], "Landmarks (no-op)")

# ---------------------------------------------------------------------
# Save
# ---------------------------------------------------------------------
save(ZN_PATH, zn)
save(LM_PATH, lm)
save(LC_PATH, lc)

print("\n== Summary ==")
print(f"  Mines_C bExtendedConnectivityLandmark cleared: {cleared}")
print(f"  Disabled zones: {disabled_zones}")
print(f"  Disabled connections: {[x[0] for x in disabled_conns]}")
print(f"  Added connections: {added_rows}")
