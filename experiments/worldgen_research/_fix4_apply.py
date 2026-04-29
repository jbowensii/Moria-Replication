"""Apply fix4: 4 worldgen issues.

Issue 1: Add LH on Elevator_B referencing FourthStair; move FourthStair BP Z 13->22.
Issue 2: Create new SixthStair landmark at (10,6,27); add LH on Elevator_D referencing it.
Issue 3: Shrink Elevator_D Sz.Z 6 -> 5 to resolve overlap at (10,6,28) with DestroyedCity_A_Desolation.
Issue 4: Audit/fix bExtendedConnectivityLandmark on multi-Z elevators per top-of-range rule
         (skip world edge cases at Z=0/Z=29).
"""
import json, copy, os
from pathlib import Path

HERE = Path(__file__).parent
ZP = HERE / "DT_Moria_Zones.json"
LP = HERE / "DT_Moria_Landmarks.json"
CP = HERE / "DT_Moria_Chapters.json"
LCP = HERE / "DT_Moria_LayoutConnections.json"

z = json.loads(ZP.read_text(encoding="utf-8"))
lm = json.loads(LP.read_text(encoding="utf-8"))
ch = json.loads(CP.read_text(encoding="utf-8"))
lc = json.loads(LCP.read_text(encoding="utf-8"))


def fp(props, name):
    for p in props or []:
        if isinstance(p, dict) and p.get("Name") == name:
            return p
    return None


def get_rowname(prop):
    for it in prop.get("Value", []) or []:
        if isinstance(it, dict) and it.get("Name") == "RowName":
            return it.get("Value")
    return None


def set_rowname(prop, new):
    for it in prop.get("Value", []) or []:
        if isinstance(it, dict) and it.get("Name") == "RowName":
            it["Value"] = new
            return


def get_intvec(prop):
    for it in prop.get("Value", []) or []:
        v = it.get("Value")
        if isinstance(v, dict) and "X" in v:
            return v
    return None


def setv(prop, x, y, zv):
    v = get_intvec(prop)
    if v is not None:
        v["X"] = int(x)
        v["Y"] = int(y)
        v["Z"] = int(zv)


def find_row(table_json, name):
    for ex in table_json["Exports"]:
        tbl = ex.get("Table")
        if tbl and "Data" in tbl:
            for row in tbl["Data"]:
                if row.get("Name") == name:
                    return row
    return None


def add_namemap_entries(d, entries):
    nm = d.get("NameMap", [])
    added = 0
    for s in entries:
        if s and s not in nm:
            nm.append(s)
            added += 1
    d["NameMap"] = nm
    if added:
        # update counts
        if d.get("NamesReferencedFromExportDataCount") is not None:
            d["NamesReferencedFromExportDataCount"] = len(nm)
        gens = d.get("Generations", [])
        if gens and "NameCount" in gens[0]:
            # NameCount can be NameMap len + extra header names; safest to set to NameMap length
            # only when current value < new len.
            cur = gens[0]["NameCount"]
            if cur < len(nm):
                # increment by added
                gens[0]["NameCount"] = cur + added
    return added


changes = []

# ============================================================
# Issue 1: Move FourthStair BP Z 13 -> 22 ; add LH on Elevator_B
# ============================================================
fourth = find_row(lm, "Sandbox.FourthStair")
assert fourth is not None, "Sandbox.FourthStair landmark not found"
bp = fp(fourth["Value"], "BasePosition")
old_iv = dict(get_intvec(bp))
setv(bp, 11, 12, 22)
changes.append(f"FourthStair BP: ({old_iv['X']},{old_iv['Y']},{old_iv['Z']}) -> (11,12,22)")

elev_B = find_row(z, "Sandbox_Small_Elevator_B")
assert elev_B is not None
lh_B = fp(elev_B["Value"], "LandmarkHandles")
assert lh_B is not None
# Clone first entry to use as a template
existing_entries = lh_B.get("Value") or []
assert existing_entries, "Elevator_B has no LH entries to template from"
new_lh_entry = copy.deepcopy(existing_entries[0])
for sub in new_lh_entry.get("Value", []) or []:
    if not isinstance(sub, dict):
        continue
    n = sub.get("Name")
    if n == "Landmark":
        set_rowname(sub, "Sandbox.FourthStair")
    elif n == "Placement":
        cur = sub.get("Value", "")
        pref = cur.split("::", 1)[0] if "::" in cur else "EZoneBubblePlacement"
        sub["Value"] = f"{pref}::Fixed"
    elif n == "bExtendedConnectivityLandmark":
        sub["Value"] = True
existing_entries.append(new_lh_entry)
lh_B["Value"] = existing_entries
changes.append(f"Added LH on Elevator_B -> Sandbox.FourthStair (Placement=Fixed, bExt=True)")

# ============================================================
# Issue 2: Create Sandbox.SixthStair (clone of FifthStair) at (10,6,27); add LH on Elevator_D
# ============================================================
fifth = find_row(lm, "Sandbox.FifthStair")
assert fifth is not None
existing_sixth = find_row(lm, "Sandbox.SixthStair")
if existing_sixth is None:
    new_sixth = copy.deepcopy(fifth)
    new_sixth["Name"] = "Sandbox.SixthStair"
    bp6 = fp(new_sixth["Value"], "BasePosition")
    setv(bp6, 10, 6, 27)
    # Update InternalId TagName -> World.Landmark.Sandbox.SixthStair
    iid = fp(new_sixth["Value"], "InternalId")
    if iid:
        for it in iid.get("Value", []) or []:
            if isinstance(it, dict) and it.get("Name") == "TagName":
                it["Value"] = "World.Landmark.Sandbox.SixthStair"
    # Update DisplayName -> Landmarks.Sandbox.SixthStair
    dn = fp(new_sixth["Value"], "DisplayName")
    if dn:
        dn["Value"] = "Landmarks.Sandbox.SixthStair"
    # Clear GuaranteedConnections to avoid carrying over Fifth's connections
    gc = fp(new_sixth["Value"], "GuaranteedConnections")
    if gc and gc.get("Value"):
        if "DummyStruct" not in gc:
            gc["DummyStruct"] = copy.deepcopy(gc["Value"][0])
        gc["Value"] = []
    # Append to landmarks table
    for ex in lm["Exports"]:
        tbl = ex.get("Table")
        if tbl and "Data" in tbl:
            tbl["Data"].append(new_sixth)
            break
    changes.append("Created Sandbox.SixthStair landmark (clone of FifthStair) at BP=(10,6,27)")
else:
    # ensure BP is correct
    bp6 = fp(existing_sixth["Value"], "BasePosition")
    setv(bp6, 10, 6, 27)
    changes.append("Sandbox.SixthStair existed; ensured BP=(10,6,27)")

# Add Landmarks NameMap entries (Zones already has Sandbox.SixthStair)
add_namemap_entries(
    lm,
    [
        "Sandbox.SixthStair",
        "Landmarks.Sandbox.SixthStair",
        "World.Landmark.Sandbox.SixthStair",
    ],
)

# Add LH on Elevator_D referencing SixthStair, bExt=True
elev_D = find_row(z, "Sandbox_Small_Elevator_D")
assert elev_D is not None
lh_D = fp(elev_D["Value"], "LandmarkHandles")
existing_D = lh_D.get("Value") or []
new_lh_D = copy.deepcopy(existing_D[0])
for sub in new_lh_D.get("Value", []) or []:
    if not isinstance(sub, dict):
        continue
    n = sub.get("Name")
    if n == "Landmark":
        set_rowname(sub, "Sandbox.SixthStair")
    elif n == "Placement":
        cur = sub.get("Value", "")
        pref = cur.split("::", 1)[0] if "::" in cur else "EZoneBubblePlacement"
        sub["Value"] = f"{pref}::Fixed"
    elif n == "bExtendedConnectivityLandmark":
        sub["Value"] = True
existing_D.append(new_lh_D)
lh_D["Value"] = existing_D
changes.append("Added LH on Elevator_D -> Sandbox.SixthStair (Placement=Fixed, bExt=True)")

# ============================================================
# Issue 3: Shrink Elevator_D Sz.Z 6 -> 5
# ============================================================
tgt_D = fp(elev_D["Value"], "TargetSize")
sz_D = get_intvec(tgt_D)
old_z = sz_D["Z"]
sz_D["Z"] = 5
changes.append(f"Elevator_D TargetSize.Z: {old_z} -> 5 (now spans Z=23..27, no longer hits Z=28)")

# ============================================================
# Issue 4: Audit / set bExtendedConnectivityLandmark per rule
# Top-of-range anchors get bExt=true; world-edge cases skipped.
# Build map of zone -> Z range, landmark -> Z, then walk LH entries.
# ============================================================
# Build chapter Z map (PrimeZ)
chap_pz = {}
for ex in ch["Exports"]:
    tbl = ex.get("Table")
    if tbl and "Data" in tbl:
        for row in tbl["Data"]:
            pz = fp(row["Value"], "PrimeZ")
            if pz is not None:
                chap_pz[row["Name"]] = pz.get("Value")
        break

# Build landmark Z map
lm_z = {}
for ex in lm["Exports"]:
    tbl = ex.get("Table")
    if tbl and "Data" in tbl:
        for row in tbl["Data"]:
            bp = fp(row["Value"], "BasePosition")
            if bp:
                v = get_intvec(bp)
                if v:
                    lm_z[row["Name"]] = v["Z"]
        break

# Walk all elevator zones with TargetSize.Z > 1
issue4_changes = []
for ex in z["Exports"]:
    tbl = ex.get("Table")
    if tbl and "Data" in tbl:
        for row in tbl["Data"]:
            n = row.get("Name", "")
            if "Sandbox_Small_Elevator_" not in n:
                continue
            tgt = fp(row["Value"], "TargetSize")
            if not tgt:
                continue
            sz = get_intvec(tgt)
            if not sz or sz["Z"] <= 1:
                continue
            chh = fp(row["Value"], "Chapter")
            if not chh:
                continue
            ch_name = get_rowname(chh)
            base_z = chap_pz.get(ch_name)
            if base_z is None:
                continue
            top_z = base_z + sz["Z"] - 1
            lh = fp(row["Value"], "LandmarkHandles")
            if not lh:
                continue
            for entry in lh.get("Value", []) or []:
                lm_handle = fp(entry.get("Value", []), "Landmark")
                if not lm_handle:
                    continue
                lm_name = get_rowname(lm_handle)
                lz = lm_z.get(lm_name)
                ext = fp(entry.get("Value", []), "bExtendedConnectivityLandmark")
                if ext is None:
                    continue
                old_v = ext.get("Value")
                # Determine new value
                new_v = old_v  # default keep
                if lz is None:
                    # unknown landmark Z — keep
                    pass
                else:
                    is_top = lz == top_z
                    is_world_edge = (lz >= 29) or (lz <= 0)
                    # Apply rule: only the TOP anchor of multi-Z zone gets bExt=true,
                    # and not at world edges. But we ALSO preserve true on landmarks
                    # that were explicitly set true above (FirstStair@18 in B, FourthStair@22 in B,
                    # SixthStair@27 in D). Per task brief Issue 1/2, those must remain true.
                    # The "top of range" rule says only the top anchor needs it.
                    # However, FirstStair@Z=18 is BOTTOM of B's range — task brief Issue 1 keeps
                    # that as-is (was already true). So we leave existing true alone unless at
                    # world edge. We only ADD true on top-of-range that isn't currently true.
                    if is_top and not is_world_edge:
                        new_v = True
                    elif is_world_edge:
                        new_v = False
                if new_v != old_v:
                    ext["Value"] = new_v
                    issue4_changes.append(
                        f"  {n}[{lm_name} @ Z={lz}, zone Z={base_z}..{top_z}] bExt: {old_v} -> {new_v}"
                    )

if issue4_changes:
    changes.append("Issue 4 bExt audits:")
    changes.extend(issue4_changes)
else:
    changes.append("Issue 4: no bExt changes required (top-of-range entries already correct or N/A)")

# ============================================================
# Save
# ============================================================
ZP.write_text(json.dumps(z, indent=2), encoding="utf-8")
LP.write_text(json.dumps(lm, indent=2), encoding="utf-8")
# chapters and layoutconnections unchanged in this fix; rewrite anyway? No - leave untouched.

print("CHANGES APPLIED:")
for c in changes:
    print("  -", c)
print("\nWrote:", ZP.name, LP.name)
