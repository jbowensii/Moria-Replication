"""Re-verify post-fix4 state."""
import json, os
from pathlib import Path

HERE = Path(__file__).parent
z = json.loads((HERE / "DT_Moria_Zones.json").read_text(encoding="utf-8"))
lm = json.loads((HERE / "DT_Moria_Landmarks.json").read_text(encoding="utf-8"))
ch = json.loads((HERE / "DT_Moria_Chapters.json").read_text(encoding="utf-8"))


def fp(props, name):
    for p in props or []:
        if isinstance(p, dict) and p.get("Name") == name:
            return p
    return None


def get_iv(prop):
    for it in prop.get("Value", []) or []:
        v = it.get("Value")
        if isinstance(v, dict) and "X" in v:
            return v
    return None


def get_rn(prop):
    for it in prop.get("Value", []) or []:
        if isinstance(it, dict) and it.get("Name") == "RowName":
            return it.get("Value")
    return None


# Chapter PrimeZ map
chap_pz = {}
for ex in ch["Exports"]:
    tbl = ex.get("Table")
    if tbl and "Data" in tbl:
        for row in tbl["Data"]:
            pz = fp(row["Value"], "PrimeZ")
            if pz:
                chap_pz[row["Name"]] = pz.get("Value")
        break

# Landmark Z map
lm_z = {}
for ex in lm["Exports"]:
    tbl = ex.get("Table")
    if tbl and "Data" in tbl:
        for row in tbl["Data"]:
            bp = fp(row["Value"], "BasePosition")
            if bp:
                iv = get_iv(bp)
                if iv:
                    lm_z[row["Name"]] = iv["Z"]
        break

print("=== STAIR LANDMARK Z VALUES ===")
for n in sorted(lm_z):
    if "Stair" in n or "Descent" in n:
        print(f"  {n}: Z={lm_z[n]}")

print("\n=== ELEVATOR ZONES ===")
for ex in z["Exports"]:
    tbl = ex.get("Table")
    if tbl and "Data" in tbl:
        for row in tbl["Data"]:
            n = row.get("Name", "")
            if "Sandbox_Small_Elevator_" not in n:
                continue
            chh = fp(row["Value"], "Chapter")
            ch_name = get_rn(chh)
            tgt = fp(row["Value"], "TargetSize")
            sz = get_iv(tgt)
            base_z = chap_pz.get(ch_name)
            top_z = base_z + sz["Z"] - 1 if base_z is not None else None
            print(f"\n{n}: chapter={ch_name} Z={base_z}..{top_z} Sz.Z={sz['Z']}")
            lh = fp(row["Value"], "LandmarkHandles")
            for i, entry in enumerate(lh.get("Value", []) or []):
                lh_lm = fp(entry.get("Value", []), "Landmark")
                pl = fp(entry.get("Value", []), "Placement")
                ext = fp(entry.get("Value", []), "bExtendedConnectivityLandmark")
                lm_name = get_rn(lh_lm) if lh_lm else None
                lz = lm_z.get(lm_name)
                in_range = (
                    "in-range"
                    if (base_z is not None and lz is not None and base_z <= lz <= top_z)
                    else "OUT-OF-RANGE"
                )
                print(
                    f"  LH[{i}] -> {lm_name} (lm Z={lz}, {in_range}) "
                    f"Placement={pl.get('Value') if pl else '?'} "
                    f"bExt={ext.get('Value') if ext else '?'}"
                )

print("\n=== ISSUE CHECK ===")
# Issue 1: Lv-4 at Z=22 reachable?
print("Issue 1 (Lv-4 Z=22 anchor):")
B = next(r for ex in z["Exports"] for r in ex["Table"]["Data"] if r.get("Name") == "Sandbox_Small_Elevator_B")
lh = fp(B["Value"], "LandmarkHandles")
hit = False
for entry in lh.get("Value", []):
    h = fp(entry.get("Value", []), "Landmark")
    if h and get_rn(h) == "Sandbox.FourthStair" and lm_z.get("Sandbox.FourthStair") == 22:
        ext = fp(entry.get("Value", []), "bExtendedConnectivityLandmark")
        print(f"  PASS: Elevator_B -> FourthStair @ Z=22, bExt={ext.get('Value')}")
        hit = True
if not hit:
    print("  FAIL")

print("Issue 2 (Lv-6 Z=27 anchor):")
D = next(r for ex in z["Exports"] for r in ex["Table"]["Data"] if r.get("Name") == "Sandbox_Small_Elevator_D")
lh = fp(D["Value"], "LandmarkHandles")
hit = False
for entry in lh.get("Value", []):
    h = fp(entry.get("Value", []), "Landmark")
    if h and get_rn(h) == "Sandbox.SixthStair" and lm_z.get("Sandbox.SixthStair") == 27:
        ext = fp(entry.get("Value", []), "bExtendedConnectivityLandmark")
        print(f"  PASS: Elevator_D -> SixthStair @ Z=27, bExt={ext.get('Value')}")
        hit = True
if not hit:
    print("  FAIL")

print("Issue 3 (no overlap at (10,6,28)):")
tgt = fp(D["Value"], "TargetSize")
sz = get_iv(tgt)
pos = fp(D["Value"], "Position")
posv = get_iv(pos)
top_z_D = posv["Z"] + sz["Z"] - 1
print(f"  Elevator_D Pos.Z={posv['Z']} Sz.Z={sz['Z']} -> top Z={top_z_D}")
if top_z_D < 28:
    print("  PASS: Elevator_D no longer occupies Z=28")
else:
    print("  FAIL: still hits Z=28")

print("Issue 4 (bExt flags on multi-Z elevators):")
for ex in z["Exports"]:
    tbl = ex.get("Table")
    if tbl and "Data" in tbl:
        for row in tbl["Data"]:
            n = row.get("Name", "")
            if "Sandbox_Small_Elevator_" not in n:
                continue
            tgt = fp(row["Value"], "TargetSize")
            sz = get_iv(tgt)
            if sz["Z"] <= 1:
                continue
            chh = fp(row["Value"], "Chapter")
            ch_name = get_rn(chh)
            base_z = chap_pz.get(ch_name)
            top_z = base_z + sz["Z"] - 1 if base_z is not None else None
            lh = fp(row["Value"], "LandmarkHandles")
            for entry in lh.get("Value", []) or []:
                h = fp(entry.get("Value", []), "Landmark")
                lm_name = get_rn(h) if h else None
                lz = lm_z.get(lm_name)
                ext = fp(entry.get("Value", []), "bExtendedConnectivityLandmark")
                ext_v = ext.get("Value") if ext else None
                is_top = lz == top_z
                edge = (lz is not None and (lz >= 29 or lz <= 0))
                ok = "OK"
                if edge and ext_v:
                    ok = "WARN: world edge but bExt=True"
                print(f"  {n}[{lm_name} Z={lz} top={top_z}] is_top={is_top} edge={edge} bExt={ext_v} [{ok}]")

# Sanity: NameMap counts on Landmarks
print("\n=== Landmarks NameMap sanity ===")
nm = lm.get("NameMap", [])
print(f"  NameMap len: {len(nm)}")
print(f"  NamesReferencedFromExportDataCount: {lm.get('NamesReferencedFromExportDataCount')}")
gens = lm.get("Generations", [])
if gens:
    print(f"  Generations[0].NameCount: {gens[0].get('NameCount')}")
for tok in ("Sandbox.SixthStair", "Landmarks.Sandbox.SixthStair", "World.Landmark.Sandbox.SixthStair"):
    print(f"  '{tok}' in NameMap: {tok in nm}")
