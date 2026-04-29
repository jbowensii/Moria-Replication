import json, os
BASE = os.path.dirname(os.path.abspath(__file__))
ZP = os.path.join(BASE, "DT_Moria_Zones.json")
LP = os.path.join(BASE, "DT_Moria_Landmarks.json")
WP = os.path.join(BASE, "World.json")

def load(p):
    with open(p, "r", encoding="utf-8") as f:
        return json.load(f)

def find_export(d, name):
    # Heuristic: look for an Export with ObjectName==name; structure is UAssetGUI tree
    # Walk Exports list and inspect Data rows.
    return d

def get_datatable_rows(asset):
    # UAssetGUI: Exports -> first export with $type DataTableExport has 'Table' -> 'Data' which is a list of structs (rows).
    for exp in asset.get("Exports", []):
        if "Table" in exp and "Data" in exp["Table"]:
            return exp["Table"]["Data"]
    return []

def get_struct_field(struct, name):
    for v in struct.get("Value", []):
        if v.get("Name") == name:
            return v
    return None

zones = load(ZP)
lms = load(LP)
world = load(WP)

zrows = get_datatable_rows(zones)
lrows = get_datatable_rows(lms)

def find_row(rows, key):
    for r in rows:
        if r.get("Name") == key:
            return r
    return None

def show_zone(name):
    r = find_row(zrows, name)
    if not r:
        print(f"[ZONE MISSING] {name}"); return None
    pos = get_struct_field(r, "Position")
    sz = get_struct_field(r, "TargetSize")
    lh = get_struct_field(r, "LandmarkHandles")
    print(f"-- {name} --")
    print("Position:", json.dumps(pos, indent=2) if pos else None)
    print("TargetSize:", json.dumps(sz, indent=2) if sz else None)
    if lh:
        print("LandmarkHandles entries:", len(lh.get("Value", [])))
        for entry in lh.get("Value", []):
            ref = get_struct_field(entry, "Reference")
            ext = get_struct_field(entry, "bExtendedConnectivityLandmark")
            print("  ref=", ref.get("Value") if ref else None, "ext=", ext.get("Value") if ext else None)
    return r

show_zone("Sandbox_Small_Elevator_D")
show_zone("Sandbox_Small_DestroyedCity_A_Desolation")

print("\n-- Stair landmarks --")
for r in lrows:
    n = r.get("Name", "")
    if "Stair" in n:
        bp = get_struct_field(r, "BasePosition")
        bb = get_struct_field(r, "BaseBubbleName")
        print(n, "BP=", bp.get("Value") if bp else None, "BB=", bb.get("Value") if bb else None)

print("\nSandbox.EighthStair landmark exists:", find_row(lrows, "Sandbox.EighthStair") is not None)

# NameMap checks
def nm(asset): return asset.get("NameMap", [])
print("\nNameMap counts: Zones=", len(nm(zones)), "Landmarks=", len(nm(lms)), "World=", len(nm(world)))
print("Zones NRefED=", zones.get("NamesReferencedFromExportDataCount"))
print("Landmarks NRefED=", lms.get("NamesReferencedFromExportDataCount"))
print("World NRefED=", world.get("NamesReferencedFromExportDataCount"))

for tok in ["Sandbox.EighthStair", "Landmarks.Sandbox.EighthStair", "World.Landmark.Sandbox.EighthStair"]:
    print(f"  '{tok}' in Zones NameMap:", tok in nm(zones), "Landmarks:", tok in nm(lms), "World:", tok in nm(world))

# Check existing SixthStair for cloning template
ss = find_row(lrows, "Sandbox.SixthStair")
print("\nSixthStair row found:", ss is not None)
if ss:
    print(json.dumps(ss, indent=2)[:3000])

# Check World StringTable for the new key
print("\nWorld StringTable scan for 'Landmarks.Sandbox.EighthStair'...")
def search_world_for_key(obj, key, path=""):
    found = []
    if isinstance(obj, dict):
        for k, v in obj.items():
            found.extend(search_world_for_key(v, key, path+"/"+str(k)))
    elif isinstance(obj, list):
        for i, v in enumerate(obj):
            found.extend(search_world_for_key(v, key, path+f"[{i}]"))
    elif isinstance(obj, str):
        if obj == key:
            found.append(path)
    return found

print("EighthStair key occurrences in World.json:", search_world_for_key(world, "Landmarks.Sandbox.EighthStair"))
print("SixthStair key occurrences in World.json:", search_world_for_key(world, "Landmarks.Sandbox.SixthStair")[:5])
