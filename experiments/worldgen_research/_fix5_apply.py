"""Apply fix5: 5 worldgen issues.

Task 1: Shrink Elevator_C TargetSize.Z 9->5; move SecondStair BP.Z 17->13 (top of new span).
Task 2: Restore SandboxSmall-Chapter08.Deep7 LEVEL row (CID=8, PrimeZ=0, ESL=7).
Task 3: Swap BD/PD on OrcTown_C_Gundabad to match vanilla pattern.
Task 4: Create Sandbox.SeventhStair landmark at (7,4,4); update Elevator_G LH from FourthStair.
Task 5: No change — Lv-7 (DestroyedCity_A_Desolation only) is intentional cap floor.
"""
import json, copy
from pathlib import Path

HERE = Path(__file__).parent
ZP = HERE / "DT_Moria_Zones.json"
LP = HERE / "DT_Moria_Landmarks.json"
CP = HERE / "DT_Moria_Chapters.json"

z = json.loads(ZP.read_text(encoding="utf-8"))
lm = json.loads(LP.read_text(encoding="utf-8"))
ch = json.loads(CP.read_text(encoding="utf-8"))


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
        v["X"] = int(x); v["Y"] = int(y); v["Z"] = int(zv)


def find_row(table_json, name):
    for ex in table_json["Exports"]:
        tbl = ex.get("Table")
        if tbl and "Data" in tbl:
            for row in tbl["Data"]:
                if row.get("Name") == name:
                    return row
    return None


def append_row(table_json, row):
    for ex in table_json["Exports"]:
        tbl = ex.get("Table")
        if tbl and "Data" in tbl:
            tbl["Data"].append(row)
            return True
    return False


def add_namemap_entries(d, entries):
    nm = d.get("NameMap", [])
    added = 0
    for s in entries:
        if s and s not in nm:
            nm.append(s)
            added += 1
    d["NameMap"] = nm
    if added:
        if d.get("NamesReferencedFromExportDataCount") is not None:
            d["NamesReferencedFromExportDataCount"] = len(nm)
        gens = d.get("Generations", [])
        if gens and "NameCount" in gens[0]:
            cur = gens[0]["NameCount"]
            if cur < len(nm):
                gens[0]["NameCount"] = cur + added
    return added


changes = []

# ============================================================
# Task 1: Shrink Elevator_C; relocate SecondStair to top of new span
# ============================================================
ec = find_row(z, "Sandbox_Small_Elevator_C")
ts = fp(ec["Value"], "TargetSize")
sz = get_intvec(ts)
old_z = sz["Z"]
sz["Z"] = 5
changes.append(f"Elevator_C TargetSize.Z: {old_z} -> 5 (span 9..17 -> 9..13)")

# Move SecondStair BP from (7,11,17) to (7,11,13) — top of new span
sec = find_row(lm, "Sandbox.SecondStair")
bp = fp(sec["Value"], "BasePosition")
old_iv = dict(get_intvec(bp))
setv(bp, old_iv["X"], old_iv["Y"], 13)
changes.append(f"SecondStair BP.Z: {old_iv['Z']} -> 13 (top of new Elevator_C span)")

# ============================================================
# Task 2: Restore SandboxSmall-Chapter08.Deep7 LEVEL row
# Clone from existing AngryCaverns_B (same chapter shape) and rename.
# ============================================================
existing_deep7 = find_row(ch, "SandboxSmall-Chapter08.Deep7")
if existing_deep7 is None:
    template = find_row(ch, "SandboxSmall-Chapter08.AngryCaverns_B")
    assert template is not None
    new_row = copy.deepcopy(template)
    new_row["Name"] = "SandboxSmall-Chapter08.Deep7"
    # All shape values already match (CID=8, PrimeZ=0, MinZ=0, MaxZ=0, ESL=7, DN=Chapter.Sandbox.Deep7.Name)
    append_row(ch, new_row)
    add_namemap_entries(ch, ["SandboxSmall-Chapter08.Deep7"])
    changes.append("Restored chapter row SandboxSmall-Chapter08.Deep7 (CID=8, PrimeZ=0, ESL=7)")
else:
    changes.append("SandboxSmall-Chapter08.Deep7 already present; no action")

# ============================================================
# Task 3: Swap BD/PD on OrcTown_C_Gundabad
# ============================================================
ot = find_row(z, "Sandbox_Small_OrcTown_C_Gundabad")
bd = fp(ot["Value"], "BubbleDeck")
pd_ = fp(ot["Value"], "PassageDeck")
bd_name = get_rowname(bd); pd_name = get_rowname(pd_)
set_rowname(bd, pd_name)
set_rowname(pd_, bd_name)
changes.append(f"OrcTown_C_Gundabad swapped: BD {bd_name}->{pd_name}, PD {pd_name}->{bd_name}")

# ============================================================
# Task 4: Create Sandbox.SeventhStair landmark; rewire Elevator_G LH
# ============================================================
existing7 = find_row(lm, "Sandbox.SeventhStair")
if existing7 is None:
    template = find_row(lm, "Sandbox.SixthStair")
    assert template is not None
    new7 = copy.deepcopy(template)
    new7["Name"] = "Sandbox.SeventhStair"
    bp7 = fp(new7["Value"], "BasePosition")
    # Elevator_G Position=(7,4,4); place at the bottom cell (PrimeZ=4, bottom of zone)
    setv(bp7, 7, 4, 4)
    iid = fp(new7["Value"], "InternalId")
    if iid:
        for it in iid.get("Value", []) or []:
            if isinstance(it, dict) and it.get("Name") == "TagName":
                it["Value"] = "World.Landmark.Sandbox.SeventhStair"
    dn = fp(new7["Value"], "DisplayName")
    if dn:
        dn["Value"] = "Landmarks.Sandbox.SeventhStair"
    gc = fp(new7["Value"], "GuaranteedConnections")
    if gc and gc.get("Value"):
        if "DummyStruct" not in gc:
            gc["DummyStruct"] = copy.deepcopy(gc["Value"][0])
        gc["Value"] = []
    append_row(lm, new7)
    changes.append("Created Sandbox.SeventhStair landmark at BP=(7,4,4) — Elevator_G floor anchor")
else:
    bp7 = fp(existing7["Value"], "BasePosition")
    setv(bp7, 7, 4, 4)
    changes.append("Sandbox.SeventhStair existed; ensured BP=(7,4,4)")

# NameMap: Landmarks
add_namemap_entries(lm, [
    "Sandbox.SeventhStair",
    "Landmarks.Sandbox.SeventhStair",
    "World.Landmark.Sandbox.SeventhStair",
])
# NameMap: Zones (LH RowName references Sandbox.SeventhStair)
add_namemap_entries(z, ["Sandbox.SeventhStair"])

# Update Elevator_G LH from FourthStair -> SeventhStair, bExt=False (bottom anchor)
eg = find_row(z, "Sandbox_Small_Elevator_G")
lh = fp(eg["Value"], "LandmarkHandles")
for entry in lh.get("Value", []) or []:
    lh_h = fp(entry.get("Value", []), "Landmark")
    if not lh_h:
        continue
    if get_rowname(lh_h) == "Sandbox.FourthStair":
        set_rowname(lh_h, "Sandbox.SeventhStair")
        ext = fp(entry.get("Value", []), "bExtendedConnectivityLandmark")
        if ext is not None:
            ext["Value"] = False  # bottom anchor
        changes.append("Elevator_G LH rewired: Sandbox.FourthStair -> Sandbox.SeventhStair (bExt=False, bottom)")

# ============================================================
# Task 5: NO CHANGE
# ============================================================
changes.append("Task 5: No change. Lv-7 contains only DestroyedCity_A_Desolation; "
               "matches before_fix4 baseline. Cap floor — intentional sparse layer.")

# ============================================================
# Save
# ============================================================
ZP.write_text(json.dumps(z, indent=2), encoding="utf-8")
LP.write_text(json.dumps(lm, indent=2), encoding="utf-8")
CP.write_text(json.dumps(ch, indent=2), encoding="utf-8")

print("CHANGES APPLIED:")
for c in changes:
    print("  -", c)
print("\nWrote:", ZP.name, LP.name, CP.name)
