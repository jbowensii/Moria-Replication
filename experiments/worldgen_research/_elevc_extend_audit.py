import json, os
os.chdir(os.path.dirname(os.path.abspath(__file__)))

with open("DT_Moria_Zones.json","r",encoding="utf-8") as f:
    zones = json.load(f)
with open("DT_Moria_Landmarks.json","r",encoding="utf-8") as f:
    lms = json.load(f)

# Find rows
def find_export_rows(data):
    # rows live in Exports[?].Table.Data each row is a StructPropertyData with Name = row name
    for exp in data.get("Exports", []):
        if "Table" in exp and "Data" in exp["Table"]:
            return exp["Table"]["Data"], exp
    return None, None

zrows, zexp = find_export_rows(zones)
lrows, lexp = find_export_rows(lms)

def get_prop(row, name):
    for v in row.get("Value", []):
        if v.get("Name") == name:
            return v
    return None

def get_struct_xyz(row, propname):
    p = get_prop(row, propname)
    if not p: return None
    # p.Value is a list with one IntVectorPropertyData; .Value is dict with X/Y/Z
    val = p.get("Value", [])
    if val and isinstance(val, list):
        inner = val[0].get("Value")
        if isinstance(inner, dict) and "X" in inner:
            return {"X": inner["X"], "Y": inner["Y"], "Z": inner["Z"]}
    return None

# Build zone footprints for SandboxSmall
def is_sandbox_small(row):
    # row Name is something like "SandboxSmall.Sandbox_Small_Elevator_C"
    return row.get("Name","").startswith("SandboxSmall.") or "Sandbox_Small_" in row.get("Name","")

zone_data = {}
for r in zrows:
    name = r.get("Name","")
    pos = get_struct_xyz(r, "Position")
    sz = get_struct_xyz(r, "TargetSize")
    if pos and sz:
        zone_data[name] = (pos, sz)

# Find Elevator_C
ec_key = None
for k in zone_data:
    if "Sandbox_Small_Elevator_C" in k:
        ec_key = k; break
print("Elevator_C key:", ec_key)
print("Elevator_C pos/size:", zone_data[ec_key])

ec_pos, ec_sz = zone_data[ec_key]
# After extension Z range
new_x_lo, new_x_hi = ec_pos["X"], ec_pos["X"]+ec_sz["X"]-1  # cells X..X+Sz-1
new_y_lo, new_y_hi = ec_pos["Y"], ec_pos["Y"]+ec_sz["Y"]-1
new_z_lo, new_z_hi = ec_pos["Z"], ec_pos["Z"]+10-1  # Sz.Z=10
print(f"After extend (Sz.Z=10): X={new_x_lo}..{new_x_hi}, Y={new_y_lo}..{new_y_hi}, Z={new_z_lo}..{new_z_hi}")

# Audit overlaps in NEW Z range 14..18
print("\n== Collision audit (overlap with extended Elev_C cells in Z=14..18) ==")
collisions = []
for k,(pos,sz) in zone_data.items():
    if k == ec_key: continue
    x_lo, x_hi = pos["X"], pos["X"]+sz["X"]-1
    y_lo, y_hi = pos["Y"], pos["Y"]+sz["Y"]-1
    z_lo, z_hi = pos["Z"], pos["Z"]+sz["Z"]-1
    # overlap with new Elev_C range
    ox_lo, ox_hi = max(x_lo, new_x_lo), min(x_hi, new_x_hi)
    oy_lo, oy_hi = max(y_lo, new_y_lo), min(y_hi, new_y_hi)
    oz_lo, oz_hi = max(z_lo, max(14, new_z_lo)), min(z_hi, new_z_hi)
    if ox_lo<=ox_hi and oy_lo<=oy_hi and oz_lo<=oz_hi:
        collisions.append((k, (x_lo,x_hi,y_lo,y_hi,z_lo,z_hi), (ox_lo,ox_hi,oy_lo,oy_hi,oz_lo,oz_hi)))

for c in collisions:
    print("  COLLIDES:", c[0], "zone box:", c[1], "overlap:", c[2])
if not collisions:
    print("  (none)")

# Landmarks: check NinthStair / TenthStair existence
print("\n== Landmark name check ==")
lm_names = [r.get("Name","") for r in lrows]
for n in ["Sandbox.NinthStair","Sandbox.TenthStair","Sandbox.SixthStair","Sandbox.SecondStair"]:
    print(f"  {n}: {'EXISTS' if n in lm_names else 'absent'}")

# Print Elevator_C LandmarkHandles
lh = get_prop(zrows[[r.get("Name","") for r in zrows].index(ec_key)], "LandmarkHandles")
print("\n== Elevator_C LandmarkHandles ==")
if lh:
    for entry in lh.get("Value", []):
        info = {}
        for v in entry.get("Value", []):
            nm = v.get("Name")
            val = v.get("Value")
            # If LandmarkRowHandle struct, dive in
            if isinstance(val, list) and val and isinstance(val[0], dict) and val[0].get("Name") == "RowName":
                info[nm] = val[0].get("Value")
            else:
                info[nm] = val
        print(" ", info)

# NameMap counts
print("\n== NameMap sizes ==")
print("  Zones NameMap:", len(zones.get("NameMap",[])), "NamesRefDataCount:", zones.get("NamesReferencedFromExportDataCount"))
print("  Landmarks NameMap:", len(lms.get("NameMap",[])), "NamesRefDataCount:", lms.get("NamesReferencedFromExportDataCount"))
