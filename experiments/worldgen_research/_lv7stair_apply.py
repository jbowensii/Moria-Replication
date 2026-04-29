import json, os, copy, shutil
BASE = os.path.dirname(os.path.abspath(__file__))
ZP = os.path.join(BASE, "DT_Moria_Zones.json")
LP = os.path.join(BASE, "DT_Moria_Landmarks.json")
WP = os.path.join(BASE, "World.json")

def load(p):
    with open(p, "r", encoding="utf-8") as f: return json.load(f)
def save(p, d):
    with open(p, "w", encoding="utf-8") as f: json.dump(d, f, indent=2)

# Backups
for p in [ZP, LP, WP]:
    bk = p.replace(".json", ".before_lv7stair.json")
    if not os.path.exists(bk):
        shutil.copy(p, bk)
        print("backup ->", bk)

zones = load(ZP); lms = load(LP); world = load(WP)

def get_table_data(asset):
    for exp in asset.get("Exports", []):
        if "Table" in exp and "Data" in exp["Table"]:
            return exp["Table"]["Data"]
    raise RuntimeError("no DataTable found")

def find_row(rows, key):
    for r in rows:
        if r.get("Name") == key: return r
    return None

def field(struct, name):
    for v in struct.get("Value", []):
        if v.get("Name") == name: return v
    return None

zrows = get_table_data(zones)
lrows = get_table_data(lms)

# === 1. DestroyedCity_A_Desolation X: 5 -> 4 ===
dc = find_row(zrows, "Sandbox_Small_DestroyedCity_A_Desolation")
pos = field(dc, "Position")["Value"][0]["Value"]
assert pos["X"] == 5 and pos["Y"] == 1 and pos["Z"] == 28, f"unexpected pos {pos}"
pos["X"] = 4
print("DC_A_Desolation new pos:", pos)

# === 2. Elevator_D TargetSize.Z: 5 -> 6 ===
ed = find_row(zrows, "Sandbox_Small_Elevator_D")
ed_pos = field(ed, "Position")["Value"][0]["Value"]
assert ed_pos == {"$type":"UAssetAPI.UnrealTypes.FIntVector, UAssetAPI","X":10,"Y":6,"Z":23}, ed_pos
ed_sz = field(ed, "TargetSize")["Value"][0]["Value"]
assert ed_sz["Z"] == 5
ed_sz["Z"] = 6
print("Elevator_D new TargetSize:", ed_sz)

# === 3. Create Sandbox.EighthStair landmark by cloning SixthStair ===
sixth = find_row(lrows, "Sandbox.SixthStair")
if find_row(lrows, "Sandbox.EighthStair") is None:
    new = copy.deepcopy(sixth)
    new["Name"] = "Sandbox.EighthStair"
    # Update fields:
    bp = field(new, "BasePosition")["Value"][0]["Value"]
    bp["X"], bp["Y"], bp["Z"] = 12, 8, 28
    # InternalId TagName
    iid = field(new, "InternalId")
    for v in iid["Value"]:
        if v.get("Name") == "TagName":
            v["Value"] = "World.Landmark.Sandbox.EighthStair"
    # DisplayName StringTable key
    dn = field(new, "DisplayName")
    dn["Value"] = "Landmarks.Sandbox.EighthStair"
    # GuaranteedConnections - clear
    gc = field(new, "GuaranteedConnections")
    gc["Value"] = []
    # bPlayerStartLocation false
    field(new, "bPlayerStartLocation")["Value"] = False
    # ChallengeRating 0
    field(new, "ChallengeRating")["Value"] = 0
    # Placement Fixed
    field(new, "Placement")["Value"] = "ELandmarkPlacement::Fixed"
    # EnabledState Live
    field(new, "EnabledState")["Value"] = "ERowEnabledState::Live"
    # BaseBubbleName already copied from SixthStair (BB_Sandbox_CrystalDescent)
    lrows.append(new)
    print("Added Sandbox.EighthStair landmark, BP=(12,8,28), BB=", field(new,"BaseBubbleName")["Value"])
else:
    print("EighthStair already exists, skip create")

# === 4. Anchor on Elevator_D LandmarkHandles ===
lh = field(ed, "LandmarkHandles")
# template: copy from SixthStair entry (index 1) - has placement Fixed and ext True; we'll change ref + ext
existing_refs = []
for entry in lh["Value"]:
    rn_struct = field(entry, "Landmark")
    for v in rn_struct["Value"]:
        if v.get("Name") == "RowName":
            existing_refs.append(v["Value"])
print("Existing LH refs on Elevator_D:", existing_refs)

if "Sandbox.EighthStair" not in existing_refs:
    template = copy.deepcopy(lh["Value"][-1])
    # set Landmark.RowName -> Sandbox.EighthStair
    rn_struct = field(template, "Landmark")
    for v in rn_struct["Value"]:
        if v.get("Name") == "RowName":
            v["Value"] = "Sandbox.EighthStair"
    # placement Fixed
    for v in template.get("Value", []):
        if v.get("Name") == "Placement":
            v["Value"] = "EZoneBubblePlacement::Fixed"
        if v.get("Name") == "bExtendedConnectivityLandmark":
            v["Value"] = False
    lh["Value"].append(template)
    print("Appended EighthStair LandmarkHandle entry (ext=False)")
else:
    print("EighthStair LH entry already exists")

# === 5. NameMap synchronization ===
def ensure_name(asset, tok):
    nm = asset.get("NameMap", [])
    if tok not in nm:
        nm.append(tok)
        return True
    return False

added_z = ensure_name(zones, "Sandbox.EighthStair")
added_l1 = ensure_name(lms, "Sandbox.EighthStair")
added_l2 = ensure_name(lms, "Landmarks.Sandbox.EighthStair")
added_l3 = ensure_name(lms, "World.Landmark.Sandbox.EighthStair")
print("NameMap added: Zones.EighthStair=", added_z, "Lms: SS=", added_l1, "Lms.E=", added_l2, "Lms.WLE=", added_l3)

# StringTable check in World.json: search for SixthStair entry pattern
def find_stringtable_entries(obj):
    # Recursively find any object that looks like a StringTable map. Heuristic: capture parent dict that contains key "Landmarks.Sandbox.SixthStair"
    found = []
    def walk(o, parent=None, parent_key=None):
        if isinstance(o, dict):
            if "Landmarks.Sandbox.SixthStair" in o and isinstance(o.get("Landmarks.Sandbox.SixthStair"), str):
                found.append(o)
            for k, v in o.items():
                walk(v, o, k)
        elif isinstance(o, list):
            for i, v in enumerate(o):
                walk(v, o, i)
    walk(obj)
    return found

st_dicts = find_stringtable_entries(world)
print("World StringTable dicts containing SixthStair:", len(st_dicts))
world_modified = False
for st in st_dicts:
    if "Landmarks.Sandbox.EighthStair" not in st:
        st["Landmarks.Sandbox.EighthStair"] = "The Eighth Stair"
        world_modified = True
        print("  added StringTable entry 'The Eighth Stair'")

# Ensure World.json NameMap has Landmarks.Sandbox.EighthStair (already true per audit, but be safe)
added_w = ensure_name(world, "Landmarks.Sandbox.EighthStair")
if added_w: world_modified = True

# Update NamesReferencedFromExportDataCount per file
def sync_nrefed(asset, label):
    nm_len = len(asset.get("NameMap", []))
    asset["NamesReferencedFromExportDataCount"] = nm_len
    gens = asset.get("Generations", [])
    if gens and gens[0].get("NameCount", 0) < nm_len:
        gens[0]["NameCount"] = nm_len
    print(f"{label}: NameMap={nm_len}, NRefED set, Gen0.NameCount={gens[0].get('NameCount') if gens else 'n/a'}")

sync_nrefed(zones, "Zones")
sync_nrefed(lms, "Landmarks")
if world_modified:
    sync_nrefed(world, "World")
else:
    print("World: no modifications (NameMap already had token, no StringTable changes)")

save(ZP, zones)
save(LP, lms)
if world_modified:
    save(WP, world)
print("DONE")
