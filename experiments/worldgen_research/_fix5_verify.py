"""Verify fix5 changes."""
import json
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


def find_row(j, n):
    for ex in j["Exports"]:
        tbl = ex.get("Table")
        if tbl and "Data" in tbl:
            for r in tbl["Data"]:
                if r.get("Name") == n:
                    return r
    return None


fail = []

# Task 1
ec = find_row(z, "Sandbox_Small_Elevator_C")
ts_z = get_intvec(fp(ec["Value"], "TargetSize"))["Z"]
print(f"[T1] Elevator_C TargetSize.Z = {ts_z} (expect 5)"); fail.append(ts_z != 5)
sec_z = get_intvec(fp(find_row(lm, "Sandbox.SecondStair")["Value"], "BasePosition"))["Z"]
print(f"[T1] SecondStair BP.Z = {sec_z} (expect 13)"); fail.append(sec_z != 13)
# is in span 9..13?
print(f"[T1] SecondStair Z in [9,13]: {9 <= sec_z <= 13}")

# Task 2
deep7 = find_row(ch, "SandboxSmall-Chapter08.Deep7")
print(f"[T2] Chapter08.Deep7 row exists: {deep7 is not None}"); fail.append(deep7 is None)
if deep7:
    cid = fp(deep7["Value"], "ChapterID").get("Value")
    pz = fp(deep7["Value"], "PrimeZ").get("Value")
    esl = fp(deep7["Value"], "EnemyScalingLevel").get("Value")
    dn = fp(deep7["Value"], "DisplayName").get("Value")
    print(f"[T2]   CID={cid} PrimeZ={pz} ESL={esl} DN={dn}")
    fail.append(cid != 8 or pz != 0 or esl != 7)
print(f"[T2] NameMap has 'SandboxSmall-Chapter08.Deep7': {'SandboxSmall-Chapter08.Deep7' in ch.get('NameMap', [])}")

# Task 3
ot = find_row(z, "Sandbox_Small_OrcTown_C_Gundabad")
bd = get_rowname(fp(ot["Value"], "BubbleDeck"))
pd_ = get_rowname(fp(ot["Value"], "PassageDeck"))
print(f"[T3] OrcTown_C_Gundabad BD={bd} PD={pd_}")
print(f"[T3] Matches vanilla pattern (BD=Bubbles, PD=Passages): "
      f"{bd == 'Sandbox_OrcTownBubbles' and pd_ == 'Sandbox_OrcTownPassages'}")
fail.append(not (bd == "Sandbox_OrcTownBubbles" and pd_ == "Sandbox_OrcTownPassages"))

# Task 4
seventh = find_row(lm, "Sandbox.SeventhStair")
print(f"[T4] SeventhStair landmark exists: {seventh is not None}"); fail.append(seventh is None)
if seventh:
    bp7 = get_intvec(fp(seventh["Value"], "BasePosition"))
    print(f"[T4]   SeventhStair BP={bp7}")
    fail.append(not (bp7["X"] == 7 and bp7["Y"] == 4 and bp7["Z"] == 4))
eg = find_row(z, "Sandbox_Small_Elevator_G")
lh = fp(eg["Value"], "LandmarkHandles")
hits = []
for entry in lh.get("Value", []) or []:
    lh_h = fp(entry.get("Value", []), "Landmark")
    if lh_h:
        ln = get_rowname(lh_h)
        ext = fp(entry.get("Value", []), "bExtendedConnectivityLandmark")
        hits.append((ln, ext.get("Value") if ext else None))
print(f"[T4] Elevator_G LH entries: {hits}")
print(f"[T4] No FourthStair ref: {all(h[0] != 'Sandbox.FourthStair' for h in hits)}")
print(f"[T4] Has SeventhStair bExt=False: {any(h[0] == 'Sandbox.SeventhStair' and h[1] is False for h in hits)}")
fail.append(not any(h[0] == "Sandbox.SeventhStair" for h in hits))

# NameMaps
for token in ["Sandbox.SeventhStair", "Landmarks.Sandbox.SeventhStair", "World.Landmark.Sandbox.SeventhStair"]:
    print(f"[NM-Lm] '{token}' in Landmarks NameMap: {token in lm.get('NameMap', [])}")
print(f"[NM-Z] 'Sandbox.SeventhStair' in Zones NameMap: {'Sandbox.SeventhStair' in z.get('NameMap', [])}")

# Header invariants
for label, j in [("Zones", z), ("Landmarks", lm), ("Chapters", ch)]:
    nm_len = len(j.get("NameMap", []))
    nrc = j.get("NamesReferencedFromExportDataCount")
    nc = j.get("Generations", [{}])[0].get("NameCount")
    print(f"[HDR] {label}: NameMap len={nm_len}, NamesReferencedFromExportDataCount={nrc}, Gen[0].NameCount={nc}")

print()
if any(fail):
    print(f"FAILED: {sum(1 for f in fail if f)} check(s) failed")
else:
    print("ALL CHECKS PASSED")
