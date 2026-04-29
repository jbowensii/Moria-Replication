"""Apply floor anchors to Lv-3, Lv-4, Lv-5 content zones.

Strategy: reuse 7 orphan landmarks (re-anchor each to the target zone's center)
and add a single LandmarkHandle entry to each target zone.
No new landmarks required — all 7 target zones are filled by orphans.
"""
import json, os, copy, shutil
from pathlib import Path

BASE = Path(r"C:\Users\johnb\OneDrive\Documents\Projects\Moria-Replication\experiments\worldgen_research")
ZONES = BASE / "DT_Moria_Zones.json"
LM    = BASE / "DT_Moria_Landmarks.json"
WORLD = BASE / "World.json"

# Backups
for p in [ZONES, LM, WORLD]:
    bak = str(p).replace(".json", ".before_floor_anchors.json")
    if not os.path.exists(bak):
        shutil.copy(p, bak)
        print(f"Backup: {bak}")

def load(p):
    with open(p, "r", encoding="utf-8") as f: return json.load(f)
def save(p, d):
    with open(p, "w", encoding="utf-8") as f: json.dump(d, f, indent=2)

zones = load(ZONES); lms = load(LM); world = load(WORLD)

def get_data(a):
    for e in a.get("Exports", []):
        if "Table" in e: return e["Table"]["Data"]
def field(s, n):
    for v in s.get("Value", []):
        if v.get("Name") == n: return v
def get_iv(r, fn):
    f = field(r, fn);  iv = f["Value"][0]["Value"]
    return (iv["X"], iv["Y"], iv["Z"])
def set_iv(r, fn, x, y, z):
    f = field(r, fn); iv = f["Value"][0]["Value"]
    iv["X"] = x; iv["Y"] = y; iv["Z"] = z

zrows = get_data(zones); lrows = get_data(lms)

# ----- Plan: orphan landmark -> target zone -----
# (orphan_name, target_zone)
PLAN = [
    ("Sandbox.MithrilMineNexus", "Sandbox_Small_Mines_B"),         # Lv-3
    ("Sandbox.CrystalDescent",   "Sandbox_Small_City_D"),          # Lv-3
    ("Sandbox.NogrodForge",      "Sandbox_Small_Suburban_D"),      # Lv-4
    ("Sandbox.21stHall",         "Sandbox_Small_DestroyedCity_B"), # Lv-4
    ("Sandbox.DurinsForge",      "Sandbox_Small_DarkestDeeps_E"),  # Lv-4
    ("Sandbox.MithrilForge",     "Sandbox_Small_MusteringHalls"),  # Lv-5
    ("Sandbox.BalrogsNest",      "Sandbox_Small_OrcTown_D_Redeye"),# Lv-5
]

zmap = {z["Name"]: z for z in zrows}
lmap = {r["Name"]: r for r in lrows}

def make_lm_entry(rowname, ext=False):
    return {
        "$type": "UAssetAPI.PropertyTypes.Structs.StructPropertyData, UAssetAPI",
        "StructType": "MorZoneLandmarkEntry",
        "SerializeNone": True,
        "StructGUID": "{00000000-0000-0000-0000-000000000000}",
        "SerializationControl": "NoExtension",
        "Operation": "None",
        "Name": "LandmarkHandles",
        "ArrayIndex": 0,
        "IsZero": False,
        "PropertyTagFlags": "None",
        "PropertyTagExtensions": "NoExtension",
        "Value": [
            {
                "$type": "UAssetAPI.PropertyTypes.Structs.StructPropertyData, UAssetAPI",
                "StructType": "MorLandmarkRowHandle",
                "SerializeNone": True,
                "StructGUID": "{00000000-0000-0000-0000-000000000000}",
                "SerializationControl": "NoExtension",
                "Operation": "None",
                "Name": "Landmark",
                "ArrayIndex": 0,
                "IsZero": False,
                "PropertyTagFlags": "None",
                "PropertyTagExtensions": "NoExtension",
                "Value": [
                    {
                        "$type": "UAssetAPI.PropertyTypes.Objects.NamePropertyData, UAssetAPI",
                        "Name": "RowName",
                        "ArrayIndex": 0,
                        "IsZero": False,
                        "PropertyTagFlags": "None",
                        "PropertyTagExtensions": "NoExtension",
                        "Value": rowname
                    }
                ]
            },
            {
                "$type": "UAssetAPI.PropertyTypes.Objects.EnumPropertyData, UAssetAPI",
                "EnumType": "EZoneBubblePlacement",
                "InnerType": None,
                "Name": "Placement",
                "ArrayIndex": 0,
                "IsZero": False,
                "PropertyTagFlags": "None",
                "PropertyTagExtensions": "NoExtension",
                "Value": "EZoneBubblePlacement::Fixed"
            },
            {
                "$type": "UAssetAPI.PropertyTypes.Objects.BoolPropertyData, UAssetAPI",
                "Name": "bExtendedConnectivityLandmark",
                "ArrayIndex": 0,
                "IsZero": False,
                "PropertyTagFlags": "None",
                "PropertyTagExtensions": "NoExtension",
                "Value": ext
            }
        ]
    }

print("=" * 80)
print("APPLYING FLOOR ANCHORS")
print("=" * 80)

bp_moves = []
lh_adds = []
for orphan, zone_name in PLAN:
    z = zmap[zone_name]
    p = get_iv(z, "Position"); s = get_iv(z, "TargetSize")
    center = (p[0] + s[0] // 2, p[1] + s[1] // 2, p[2])
    # Move orphan BasePosition to zone center
    lm_row = lmap[orphan]
    old_bp = get_iv(lm_row, "BasePosition")
    set_iv(lm_row, "BasePosition", *center)
    bp_moves.append((orphan, old_bp, center, zone_name))
    print(f"  {orphan:32s}  BP {old_bp} -> {center}  [host: {zone_name}]")
    # Add LandmarkHandle entry to target zone
    lh = field(z, "LandmarkHandles")
    lh["Value"].append(make_lm_entry(orphan, ext=False))
    lh_adds.append((zone_name, orphan))

# ----- NameMap synchronization -----
def add_to_namemap(d, names, label):
    nm = d["NameMap"]; existing = set(nm); added = []
    before = len(nm)
    for n in names:
        if n not in existing:
            nm.append(n); existing.add(n); added.append(n)
    d["NamesReferencedFromExportDataCount"] = len(nm)
    gens = d.get("Generations", [])
    if gens and gens[0].get("NameCount", 0) < len(nm):
        gens[0]["NameCount"] = len(nm)
    print(f"  {label}: NameMap {before} -> {len(nm)} (+{len(added)}) added={added} NRFE={d['NamesReferencedFromExportDataCount']} Gen0.NameCount={gens[0]['NameCount'] if gens else None}")

# All orphan names need to be in Zones NameMap (referenced via LH RowName).
orphan_names = [orphan for orphan, _ in PLAN]
print("\n" + "=" * 80)
print("NAMEMAP SYNC")
print("=" * 80)
add_to_namemap(zones, orphan_names, "Zones")
# Landmarks NameMap: orphans were already there since they exist as rows.
# But verify: add if missing.
add_to_namemap(lms, orphan_names, "Landmarks")
# World StringTable: no new entries needed (orphans had pre-existing DisplayName StringTable refs).

# Save
save(ZONES, zones)
save(LM, lms)
save(WORLD, world)

print("\n" + "=" * 80)
print("SUMMARY")
print("=" * 80)
print(f"BP moves: {len(bp_moves)}")
for o, ob, nb, z in bp_moves:
    print(f"  {o}: {ob} -> {nb} (zone {z})")
print(f"\nLandmarkHandle additions: {len(lh_adds)}")
for z, o in lh_adds:
    print(f"  {z} += {o}")
print("\nFiles saved: DT_Moria_Zones.json, DT_Moria_Landmarks.json, World.json")
