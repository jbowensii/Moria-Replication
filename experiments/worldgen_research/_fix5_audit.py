"""Audit script for fix5: investigate before applying changes."""
import json
from pathlib import Path

HERE = Path(__file__).parent
ZP = HERE / "DT_Moria_Zones.json"
LP = HERE / "DT_Moria_Landmarks.json"
CP = HERE / "DT_Moria_Chapters.json"
LCP = HERE / "DT_Moria_LayoutConnections.json"

z = json.loads(ZP.read_text(encoding="utf-8"))
lm = json.loads(LP.read_text(encoding="utf-8"))
ch = json.loads(CP.read_text(encoding="utf-8"))

ch_orig = json.loads((HERE / "DT_Moria_Chapters.original.json").read_text(encoding="utf-8"))
ch_pre4 = json.loads((HERE / "DT_Moria_Chapters.before_fix4.json").read_text(encoding="utf-8"))
z_orig = json.loads((HERE / "DT_Moria_Zones.original.json").read_text(encoding="utf-8"))
z_pre4 = json.loads((HERE / "DT_Moria_Zones.before_fix4.json").read_text(encoding="utf-8"))


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


def get_intvec(prop):
    for it in prop.get("Value", []) or []:
        v = it.get("Value")
        if isinstance(v, dict) and "X" in v:
            return v
    return None


def find_row(table_json, name):
    for ex in table_json["Exports"]:
        tbl = ex.get("Table")
        if tbl and "Data" in tbl:
            for row in tbl["Data"]:
                if row.get("Name") == name:
                    return row
    return None


def all_rows(table_json):
    for ex in table_json["Exports"]:
        tbl = ex.get("Table")
        if tbl and "Data" in tbl:
            for row in tbl["Data"]:
                yield row


def chap_prime(ch_json, ch_name):
    r = find_row(ch_json, ch_name)
    if r is None:
        return None
    pz = fp(r["Value"], "PrimeZ")
    return pz.get("Value") if pz else None


def landmark_z(lm_json, lm_name):
    r = find_row(lm_json, lm_name)
    if r is None:
        return None, None
    bp = fp(r["Value"], "BasePosition")
    if not bp:
        return None, None
    v = get_intvec(bp)
    return r, v


print("=" * 70)
print("TASK 1: Elevator_C audit (TargetSize.Z 9 -> 5)")
print("=" * 70)

ec = find_row(z, "Sandbox_Small_Elevator_C")
pos = fp(ec["Value"], "Position"); ts = fp(ec["Value"], "TargetSize")
chh = fp(ec["Value"], "Chapter")
ch_name = get_rowname(chh)
print(f"Chapter row: {ch_name}")
pz = chap_prime(ch, ch_name)
print(f"Chapter PrimeZ: {pz}")
print(f"Position: {get_intvec(pos)}")
print(f"TargetSize: {get_intvec(ts)}")
sz = get_intvec(ts)
old_top = pz + sz["Z"] - 1
new_top = pz + 5 - 1
print(f"Current Z span: {pz}..{old_top}; New Z span: {pz}..{new_top}")

lh = fp(ec["Value"], "LandmarkHandles")
for entry in lh.get("Value", []) or []:
    lm_h = fp(entry.get("Value", []), "Landmark")
    if not lm_h:
        continue
    lname = get_rowname(lm_h)
    _, v = landmark_z(lm, lname)
    in_old = v and pz <= v["Z"] <= old_top
    in_new = v and pz <= v["Z"] <= new_top
    print(f"  LH -> {lname}: BP={v}, in_old={in_old}, in_new={in_new}")

print()
print("=" * 70)
print("TASK 2: D-7 / Chapter08 audit")
print("=" * 70)

print("\n-- Current chapter rows containing 'Chapter08' --")
for r in all_rows(ch):
    n = r["Name"]
    if "Chapter08" in n:
        cid = fp(r["Value"], "ChapterID"); pz = fp(r["Value"], "PrimeZ")
        minZ = fp(r["Value"], "MinZ"); maxZ = fp(r["Value"], "MaxZ")
        dn = fp(r["Value"], "DisplayName"); esl = fp(r["Value"], "EnemyScalingLevel")
        print(f"  {n}: CID={cid and cid.get('Value')} PrimeZ={pz and pz.get('Value')} "
              f"MinZ={minZ and minZ.get('Value')} MaxZ={maxZ and maxZ.get('Value')} "
              f"DN={dn and dn.get('Value')} ESL={esl and esl.get('Value')}")

print("\n-- before_fix4 Chapter08 rows --")
for r in all_rows(ch_pre4):
    n = r["Name"]
    if "Chapter08" in n:
        cid = fp(r["Value"], "ChapterID"); pz = fp(r["Value"], "PrimeZ")
        minZ = fp(r["Value"], "MinZ"); maxZ = fp(r["Value"], "MaxZ")
        dn = fp(r["Value"], "DisplayName"); esl = fp(r["Value"], "EnemyScalingLevel")
        print(f"  {n}: CID={cid and cid.get('Value')} PrimeZ={pz and pz.get('Value')} "
              f"MinZ={minZ and minZ.get('Value')} MaxZ={maxZ and maxZ.get('Value')} "
              f"DN={dn and dn.get('Value')} ESL={esl and esl.get('Value')}")

print("\n-- original.json Chapter08 rows --")
for r in all_rows(ch_orig):
    n = r["Name"]
    if "Chapter08" in n:
        cid = fp(r["Value"], "ChapterID"); pz = fp(r["Value"], "PrimeZ")
        minZ = fp(r["Value"], "MinZ"); maxZ = fp(r["Value"], "MaxZ")
        dn = fp(r["Value"], "DisplayName"); esl = fp(r["Value"], "EnemyScalingLevel")
        print(f"  {n}: CID={cid and cid.get('Value')} PrimeZ={pz and pz.get('Value')} "
              f"MinZ={minZ and minZ.get('Value')} MaxZ={maxZ and maxZ.get('Value')} "
              f"DN={dn and dn.get('Value')} ESL={esl and esl.get('Value')}")

print("\n-- L=-3 family (Chapter12) for naming reference --")
for r in all_rows(ch):
    n = r["Name"]
    if "Chapter12" in n:
        cid = fp(r["Value"], "ChapterID"); pz = fp(r["Value"], "PrimeZ")
        minZ = fp(r["Value"], "MinZ"); maxZ = fp(r["Value"], "MaxZ")
        dn = fp(r["Value"], "DisplayName"); esl = fp(r["Value"], "EnemyScalingLevel")
        print(f"  {n}: CID={cid and cid.get('Value')} PrimeZ={pz and pz.get('Value')} "
              f"MinZ={minZ and minZ.get('Value')} MaxZ={maxZ and maxZ.get('Value')} "
              f"DN={dn and dn.get('Value')} ESL={esl and esl.get('Value')}")

print("\n-- Elevator_E zone --")
ee = find_row(z, "Sandbox_Small_Elevator_E")
if ee:
    pos = fp(ee["Value"], "Position"); ts = fp(ee["Value"], "TargetSize")
    chh = fp(ee["Value"], "Chapter")
    print(f"  Position: {get_intvec(pos)}")
    print(f"  TargetSize: {get_intvec(ts)}")
    print(f"  Chapter: {get_rowname(chh)}")

print("\n-- All zones in Z=0..2 area --")
for r in all_rows(z):
    pos = fp(r["Value"], "Position"); ts = fp(r["Value"], "TargetSize")
    if not pos or not ts:
        continue
    pv = get_intvec(pos); sv = get_intvec(ts)
    if not pv or not sv:
        continue
    chh = fp(r["Value"], "Chapter")
    cn = get_rowname(chh) if chh else None
    pzv = chap_prime(ch, cn) if cn else None
    if pzv is None:
        continue
    top = pzv + sv["Z"] - 1
    if pzv <= 2 and top >= 0:
        print(f"  {r['Name']}: P={pv} Sz={sv} chap={cn} pz={pzv} span={pzv}..{top}")

print()
print("=" * 70)
print("TASK 3: OrcTown_C_Gundabad BD/PD")
print("=" * 70)
ot = find_row(z, "Sandbox_Small_OrcTown_C_Gundabad")
if ot:
    bd = fp(ot["Value"], "BubbleDeck"); pd_ = fp(ot["Value"], "PassageDeck")
    print(f"Current BD: {get_rowname(bd)}")
    print(f"Current PD: {get_rowname(pd_)}")

# search original
print("\n-- vanilla OrcTown rows for BD/PD reference --")
for r in all_rows(z_orig):
    n = r["Name"]
    if "OrcTown" in n or "Gundabad" in n:
        bd = fp(r["Value"], "BubbleDeck"); pd_ = fp(r["Value"], "PassageDeck")
        print(f"  {n}: BD={get_rowname(bd) if bd else None}, PD={get_rowname(pd_) if pd_ else None}")

print("\n-- before_fix4 OrcTown_C_Gundabad --")
otp = find_row(z_pre4, "Sandbox_Small_OrcTown_C_Gundabad")
if otp:
    bd = fp(otp["Value"], "BubbleDeck"); pd_ = fp(otp["Value"], "PassageDeck")
    print(f"  before_fix4 BD: {get_rowname(bd)}")
    print(f"  before_fix4 PD: {get_rowname(pd_)}")

print()
print("=" * 70)
print("TASK 4: Elevator_G dedicated landmark")
print("=" * 70)
eg = find_row(z, "Sandbox_Small_Elevator_G")
if eg:
    pos = fp(eg["Value"], "Position"); ts = fp(eg["Value"], "TargetSize")
    chh = fp(eg["Value"], "Chapter"); bbn = fp(eg["Value"], "BaseBubbleName")
    print(f"  Position: {get_intvec(pos)}")
    print(f"  TargetSize: {get_intvec(ts)}")
    print(f"  Chapter: {get_rowname(chh)}")
    print(f"  BaseBubbleName: {bbn and bbn.get('Value')}")
    pzv = chap_prime(ch, get_rowname(chh))
    sv = get_intvec(ts)
    print(f"  Z span: {pzv}..{pzv + sv['Z'] - 1}")
    lh = fp(eg["Value"], "LandmarkHandles")
    for entry in lh.get("Value", []) or []:
        lm_h = fp(entry.get("Value", []), "Landmark")
        ext = fp(entry.get("Value", []), "bExtendedConnectivityLandmark")
        plc = fp(entry.get("Value", []), "Placement")
        if lm_h:
            lname = get_rowname(lm_h)
            _, v = landmark_z(lm, lname)
            print(f"    LH -> {lname}: BP={v}, bExt={ext and ext.get('Value')}, "
                  f"Placement={plc and plc.get('Value')}")

print("\n-- Existing 'Stair' landmarks --")
for r in all_rows(lm):
    n = r["Name"]
    if "Stair" in n or "Descent" in n:
        bp = fp(r["Value"], "BasePosition")
        v = get_intvec(bp) if bp else None
        dn = fp(r["Value"], "DisplayName")
        print(f"  {n}: BP={v}, DN={dn and dn.get('Value')}")

print()
print("=" * 70)
print("TASK 5: Lv-7 sparse floor audit (Layer -7 = chapter PrimeZ corresponds to)")
print("=" * 70)

# find chapters where PrimeZ corresponds to Layer -7
# Layer 0 ground = the layer containing world top 29? Actually D-N = Layer -N.
# We need to find which chapter PrimeZ values map to layer -7 (D-7)
# Given Z=0..29 and 14 chapters, D-7 likely sits low in Z. Let's just iterate.
print("All chapters with their Z range to identify L=-7 layer:")
for r in all_rows(ch):
    n = r["Name"]
    if "Chapter" not in n:
        continue
    cid = fp(r["Value"], "ChapterID"); pz = fp(r["Value"], "PrimeZ")
    minZ = fp(r["Value"], "MinZ"); maxZ = fp(r["Value"], "MaxZ")
    print(f"  {n}: CID={cid and cid.get('Value')} PrimeZ={pz and pz.get('Value')} "
          f"MinZ={minZ and minZ.get('Value')} MaxZ={maxZ and maxZ.get('Value')}")

# Identify zones at Lv-7 layer (zones whose Z span covers chapter 8 territory presumably)
print("\nZones in current state that touch Z range of Chapter08:")
ch08_rows = [r for r in all_rows(ch) if "Chapter08" in r["Name"]]
for ch08 in ch08_rows:
    pz = fp(ch08["Value"], "PrimeZ"); minz = fp(ch08["Value"], "MinZ"); maxz = fp(ch08["Value"], "MaxZ")
    print(f"  Chapter08 row {ch08['Name']}: PZ={pz and pz.get('Value')}, MinZ={minz and minz.get('Value')}, MaxZ={maxz and maxz.get('Value')}")

print("\nZones with Chapter == any Chapter08.* row:")
for r in all_rows(z):
    chh = fp(r["Value"], "Chapter")
    if not chh: continue
    cn = get_rowname(chh)
    if cn and "Chapter08" in cn:
        pos = fp(r["Value"], "Position"); ts = fp(r["Value"], "TargetSize")
        pv = get_intvec(pos); sv = get_intvec(ts)
        en = fp(r["Value"], "bEnabled")
        print(f"  {r['Name']}: chap={cn} P={pv} Sz={sv} bEnabled={en and en.get('Value')}")

print("\n-- before_fix4 zones with Chapter08.* --")
for r in all_rows(z_pre4):
    chh = fp(r["Value"], "Chapter")
    if not chh: continue
    cn = get_rowname(chh)
    if cn and "Chapter08" in cn:
        pos = fp(r["Value"], "Position"); ts = fp(r["Value"], "TargetSize")
        pv = get_intvec(pos); sv = get_intvec(ts)
        en = fp(r["Value"], "bEnabled")
        print(f"  {r['Name']}: chap={cn} P={pv} Sz={sv} bEnabled={en and en.get('Value')}")
