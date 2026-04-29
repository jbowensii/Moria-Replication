import json, os, copy, shutil

BASE = r"C:\Users\johnb\OneDrive\Documents\Projects\Moria-Replication\experiments\worldgen_research"
ZONES = os.path.join(BASE, "DT_Moria_Zones.json")
LM = os.path.join(BASE, "DT_Moria_Landmarks.json")
CH = os.path.join(BASE, "DT_Moria_Chapters.json")
WORLD = os.path.join(BASE, "World.json")

# Backups
for p in [ZONES, LM, CH, WORLD]:
    bak = p.replace(".json", ".before_continuous.json")
    if not os.path.exists(bak):
        shutil.copy(p, bak)
        print(f"Backup: {bak}")

def load(p):
    with open(p, "r", encoding="utf-8") as f:
        return json.load(f)
def save(p, d):
    with open(p, "w", encoding="utf-8") as f:
        json.dump(d, f, indent=2)

zones = load(ZONES)
landmarks = load(LM)
chapters = load(CH)
world = load(WORLD)

def find_export_with_table(d):
    for e in d.get("Exports", []):
        if "Table" in e and isinstance(e["Table"], dict) and "Data" in e["Table"]:
            return e
    return None

def find_field(row, name):
    for v in row.get("Value", []):
        if v.get("Name") == name:
            return v
    return None

def set_intvector(row, fname, x, y, z):
    f = find_field(row, fname)
    if f is None:
        raise KeyError(fname)
    inner = f["Value"][0]
    iv = inner["Value"]
    iv["X"] = x; iv["Y"] = y; iv["Z"] = z

def set_int(row, fname, val):
    f = find_field(row, fname)
    f["Value"] = val

def set_name(row, fname, val):
    f = find_field(row, fname)
    f["Value"] = val

def set_chapter_rowname(row, val):
    f = find_field(row, "Chapter")
    rn = f["Value"][0]
    rn["Value"] = val

# ===== Change A: Extend Elev_D Sz.Z 6→7 =====
zexp = find_export_with_table(zones)
zrows = zexp["Table"]["Data"]
elev_d = next(r for r in zrows if r["Name"] == "Sandbox_Small_Elevator_D")
ts = find_field(elev_d, "TargetSize")
ts["Value"][0]["Value"]["Z"] = 7
print("Elev_D TargetSize.Z -> 7 (Z=23..29)")

# ===== Change B: New Elev_H zone (clone from Elev_C) =====
elev_c = next(r for r in zrows if r["Name"] == "Sandbox_Small_Elevator_C")
elev_h = copy.deepcopy(elev_c)
elev_h["Name"] = "Sandbox_Small_Elevator_H"
# Position (0,22,13)
set_intvector(elev_h, "Position", 0, 22, 13)
# TargetSize (6,6,6)
set_intvector(elev_h, "TargetSize", 6, 6, 6)
# Chapter rowname
set_chapter_rowname(elev_h, "SandboxSmall-Chapter14.Elevator_H")
# bPositionFromLandmarks=false, bPositionFromZoneTable=true
find_field(elev_h, "bPositionFromLandmarks")["Value"] = False
find_field(elev_h, "bPositionFromZoneTable")["Value"] = True
# EnabledState=Live
find_field(elev_h, "EnabledState")["Value"] = "ERowEnabledState::Live"

# Replace LandmarkHandles with two new entries: NinthStair (bottom, ext=false), TenthStair (top, ext=true)
lh_field = find_field(elev_h, "LandmarkHandles")
def make_lm_entry(rowname, ext):
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
lh_field["Value"] = [make_lm_entry("Sandbox.NinthStair", False), make_lm_entry("Sandbox.TenthStair", True)]

# Append Elev_H
zrows.append(elev_h)
print("Added zone: Sandbox_Small_Elevator_H Pos=(0,22,13) Sz=(6,6,6) Z=13..18")

# ===== Change C: New Chapter row SandboxSmall-Chapter14.Elevator_H (clone from Chapter12.Elevator_C) =====
cexp = find_export_with_table(chapters)
crows = cexp["Table"]["Data"]
src = next(r for r in crows if r["Name"] == "SandboxSmall-Chapter12.Elevator_C")
new_ch = copy.deepcopy(src)
new_ch["Name"] = "SandboxSmall-Chapter14.Elevator_H"
find_field(new_ch, "ChapterID")["Value"] = 14
find_field(new_ch, "Layer")["Value"] = -1
find_field(new_ch, "EnemyScalingLevel")["Value"] = 1
find_field(new_ch, "MinZ")["Value"] = 17
find_field(new_ch, "MaxZ")["Value"] = 17
find_field(new_ch, "PrimeZ")["Value"] = 17
find_field(new_ch, "DisplayName")["Value"] = "Chapter.Sandbox.Deep1.Name"
find_field(new_ch, "EnabledState")["Value"] = "ERowEnabledState::Live"
crows.append(new_ch)
print("Added chapter: SandboxSmall-Chapter14.Elevator_H (Layer=-1, ChapterID=14, PrimeZ=17, Deep1 family)")

# ===== Change D: Add NinthStair, TenthStair, EleventhStair landmarks (clone from SixthStair) =====
lexp = find_export_with_table(landmarks)
lrows = lexp["Table"]["Data"]
src_lm = next(r for r in lrows if r["Name"] == "Sandbox.SixthStair")

def make_landmark(name, base_xyz):
    nl = copy.deepcopy(src_lm)
    nl["Name"] = name
    set_intvector(nl, "BasePosition", *base_xyz)
    # InternalId.TagName
    iid = find_field(nl, "InternalId")
    iid["Value"][0]["Value"] = f"World.Landmark.{name}"
    # BaseBubbleName
    find_field(nl, "BaseBubbleName")["Value"] = "BB_Sandbox_Elevator_Urban"
    # DisplayName
    short = name.split(".")[-1]  # NinthStair
    find_field(nl, "DisplayName")["Value"] = f"Landmarks.Sandbox.{short}"
    # Placement Fixed already inherited
    # GuaranteedConnections empty already
    # bPlayerStartLocation false; ChallengeRating 0; EnabledState Live - already
    return nl

# NinthStair: interior bottom of Elev_H — Pos.X+2, Pos.Y+2, Z=14 → (2, 24, 14)
ninth = make_landmark("Sandbox.NinthStair", (2, 24, 14))
# TenthStair: interior top — Z=17 → (2, 24, 17)
tenth = make_landmark("Sandbox.TenthStair", (2, 24, 17))
# EleventhStair: on Elev_D at BasePosition (12, 8, 29)
eleventh = make_landmark("Sandbox.EleventhStair", (12, 8, 29))
# EleventhStair lives on Elev_D (CrystalDescent bubble). Use CrystalDescent like SixthStair
find_field(eleventh, "BaseBubbleName")["Value"] = "BB_Sandbox_CrystalDescent"

lrows.extend([ninth, tenth, eleventh])
print("Added landmarks: Sandbox.NinthStair, Sandbox.TenthStair, Sandbox.EleventhStair")

# ===== Change A continued: Add EleventhStair to Elev_D LandmarkHandles =====
ld_lh = find_field(elev_d, "LandmarkHandles")
ld_lh["Value"].append(make_lm_entry("Sandbox.EleventhStair", False))
print("Added EleventhStair handle to Elev_D (bExt=false, Z=29 is topmost)")

# ===== StringTable: add EleventhStair entry =====
wval = world["Exports"][0]["Table"]["Value"]
existing = {v[0] for v in wval}
if "Landmarks.Sandbox.EleventhStair" not in existing:
    wval.append(["Landmarks.Sandbox.EleventhStair", "The Eleventh Stair"])
    print("World StringTable: added Landmarks.Sandbox.EleventhStair = 'The Eleventh Stair'")

# ===== Change E: NameMap synchronization =====
def add_to_namemap(d, names, label):
    nm = d["NameMap"]
    existing = set(nm)
    added = []
    for n in names:
        if n not in existing:
            nm.append(n)
            existing.add(n)
            added.append(n)
    # Resync NamesReferencedFromExportDataCount
    d["NamesReferencedFromExportDataCount"] = len(nm)
    # Generations[0].NameCount left alone unless smaller
    gens = d.get("Generations", [])
    if gens and gens[0].get("NameCount", 0) < len(nm):
        gens[0]["NameCount"] = len(nm)
    print(f"{label} NameMap: +{len(added)} {added} -> total {len(nm)} (NRFE={d['NamesReferencedFromExportDataCount']})")

# Zones NameMap
add_to_namemap(zones, [
    "Sandbox_Small_Elevator_H",
    "SandboxSmall-Chapter14.Elevator_H",
    "Sandbox.NinthStair",
    "Sandbox.TenthStair",
    "Sandbox.EleventhStair",
], "Zones")

# Landmarks NameMap
add_to_namemap(landmarks, [
    "Sandbox.NinthStair",
    "Sandbox.TenthStair",
    "Sandbox.EleventhStair",
    "World.Landmark.Sandbox.NinthStair",
    "World.Landmark.Sandbox.TenthStair",
    "World.Landmark.Sandbox.EleventhStair",
    "Landmarks.Sandbox.NinthStair",
    "Landmarks.Sandbox.TenthStair",
    "Landmarks.Sandbox.EleventhStair",
], "Landmarks")

# Chapters NameMap
add_to_namemap(chapters, [
    "SandboxSmall-Chapter14.Elevator_H",
], "Chapters")

# World NameMap (only if added new entry — we did add EleventhStair)
add_to_namemap(world, [
    "Landmarks.Sandbox.EleventhStair",
    "The Eleventh Stair",
], "World")

# Save
save(ZONES, zones)
save(LM, landmarks)
save(CH, chapters)
save(WORLD, world)
print("\nAll files saved.")
