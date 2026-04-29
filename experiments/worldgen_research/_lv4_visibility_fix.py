"""
Lv-4 visibility fix:
  Fix 1: Sandbox_Small_OrcTown_D_Redeye -> Position.Z = 22
  Fix 2: 4 unanchored ch-4 zones -> Position.Z=22, bPositionFromLandmarks=false
  Fix 3: Sandbox_Small_UpperStair -> TargetSize.Z = 2
"""
import json, os, sys

WG = r"C:/Users/johnb/OneDrive/Documents/Projects/Moria-Replication/experiments/worldgen_research"
ZONES_PATH = os.path.join(WG, "DT_Moria_Zones.json")

FIX1 = {"Sandbox_Small_OrcTown_D_Redeye"}
FIX2 = {
    "Sandbox_Small_AngryCaverns_C",
    "Sandbox_Small_City_D",
    "Sandbox_Small_DarkestDeeps_E",
    "Sandbox_Small_DestroyedCity_B",
}
FIX3 = "Sandbox_Small_UpperStair"

def find_rows(data):
    """Return list of (row_name, row_struct_value) for the DataTable."""
    # UAssetGUI tojson layout: Exports -> [export with Table] -> Table.Data is a list of struct entries
    # Each row entry has Name (the row key) and Value (list of property entries)
    for export in data.get("Exports", []):
        tbl = export.get("Table")
        if tbl and isinstance(tbl, dict):
            return tbl.get("Data", [])
    return []

def get_prop(row_value_list, name):
    for p in row_value_list:
        if p.get("Name") == name:
            return p
    return None

def get_struct_inner(prop):
    # StructPropertyData has Value (list of inner properties)
    return prop.get("Value", []) if prop else []

def set_vec_z(prop, new_z):
    """For an IntVector StructPropertyData, set the Z component.
    Layout: prop.Value -> [ IntVectorPropertyData{ Value: {X,Y,Z} } ]
    """
    if prop is None:
        return False, "missing prop"
    outer = prop.get("Value")
    if isinstance(outer, list) and outer:
        ivp = outer[0]
        v = ivp.get("Value")
        if isinstance(v, dict) and "Z" in v:
            old = v["Z"]
            v["Z"] = int(new_z)
            return True, old
        return False, f"inner Value not a dict with Z: {type(v).__name__}"
    return False, f"outer Value not a list: {type(outer).__name__}"

def set_bool(prop, new_val):
    if prop is None:
        return False, "missing"
    old = prop.get("Value")
    prop["Value"] = bool(new_val)
    return True, old

def verify_namemap(data, label):
    nm = data.get("NameMap", [])
    nm_len = len(nm)
    refs = data.get("NamesReferencedFromExportDataCount")
    gens = data.get("Generations", [])
    gen_count = gens[0].get("NameCount") if gens else None
    ok = (nm_len == refs == gen_count)
    print(f"  [{label}] NameMap len={nm_len} refs={refs} gen0.NameCount={gen_count} -> {'OK' if ok else 'MISMATCH'}")
    return ok

def main():
    with open(ZONES_PATH, "r", encoding="utf-8") as f:
        data = json.load(f)

    print(f"Loaded {ZONES_PATH}")
    verify_namemap(data, "before")

    rows = find_rows(data)
    print(f"Total rows: {len(rows)}")

    # Index by row name
    by_name = {}
    for row in rows:
        nm = row.get("Name")
        if nm:
            by_name[nm] = row

    report = []

    # ---- FIX 1 + FIX 2: combined Position.Z = 22 with optional bPositionFromLandmarks=false ----
    targets_z22 = {n: ("fix2" if n in FIX2 else "fix1") for n in (FIX1 | FIX2)}
    for zname, kind in targets_z22.items():
        row = by_name.get(zname)
        if row is None:
            report.append((zname, "ERROR", "row not found"))
            continue
        rval = row.get("Value", [])
        pos = get_prop(rval, "Position")
        if pos is None:
            report.append((zname, "ERROR", "Position prop missing"))
            continue
        ok, old = set_vec_z(pos, 22)
        if ok:
            report.append((zname, f"Position.Z {old} -> 22", kind))
        else:
            report.append((zname, "ERROR", f"set Position.Z failed: {old}"))
            continue

        if kind == "fix2":
            bp = get_prop(rval, "bPositionFromLandmarks")
            if bp is None:
                report.append((zname, "WARN", "bPositionFromLandmarks missing -> skipped flip"))
            else:
                ok2, old2 = set_bool(bp, False)
                report.append((zname, f"bPositionFromLandmarks {old2} -> False", "fix2"))

    # ---- FIX 3: UpperStair TargetSize.Z = 2 ----
    row = by_name.get(FIX3)
    if row is None:
        report.append((FIX3, "ERROR", "row not found"))
    else:
        ts = get_prop(row.get("Value", []), "TargetSize")
        if ts is None:
            report.append((FIX3, "ERROR", "TargetSize prop missing"))
        else:
            ok, old = set_vec_z(ts, 2)
            if ok:
                report.append((FIX3, f"TargetSize.Z {old} -> 2", "fix3"))
            else:
                report.append((FIX3, "ERROR", f"set TargetSize.Z failed: {old}"))

    # Print report
    print("\n=== APPLY REPORT ===")
    for r in report:
        print(" ", r)

    # Save
    with open(ZONES_PATH, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2, ensure_ascii=False)
    print(f"\nSaved {ZONES_PATH}")
    verify_namemap(data, "after")

if __name__ == "__main__":
    main()
