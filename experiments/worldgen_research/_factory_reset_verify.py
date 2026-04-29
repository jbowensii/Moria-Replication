"""Verify factory reset: BuildValidator + per-elevator + lore BPs + stair BPs."""
import json, os, importlib.util
from pathlib import Path

BASE = Path(os.path.dirname(os.path.abspath(__file__)))
SZE_PATH = r"C:\Users\johnb\OneDrive\Documents\Projects\Moria-Replication\scripts\SandboxZoneEditor.py"

# Load SandboxZoneEditor module
spec = importlib.util.spec_from_file_location("sze", SZE_PATH)
sze = importlib.util.module_from_spec(spec)
spec.loader.exec_module(sze)

# Build docs dict like WorldGenApp does
docs = {}
for k, (fname, stem, label) in sze.DATATABLES.items():
    doc = sze.DataTableDoc(k, BASE / fname, stem, label)
    if doc.load():
        docs[k] = doc

# Run validator
print("=" * 80)
print("BUILD VALIDATOR")
print("=" * 80)
results = sze.BuildValidator(docs).run()
errors = [r for r in results if str(getattr(r,'severity','')).lower()=='error']
warnings = [r for r in results if str(getattr(r,'severity','')).lower()=='warning']
print(f"Total issues: {len(results)}  errors={len(errors)}  warnings={len(warnings)}")
for r in results[:50]:
    sev = getattr(r,'severity','?')
    code = getattr(r,'code','?')
    where = getattr(r,'where',None)
    msg = getattr(r,'message','')
    print(f"  [{sev}] {code} {where}: {msg}")

# Helpers for raw JSON access
def load(p):
    with open(p,"r",encoding="utf-8") as f: return json.load(f)
def get_data(a):
    for e in a.get("Exports",[]):
        if "Table" in e: return e["Table"]["Data"]
def find(rows,k):
    for r in rows:
        if r.get("Name")==k: return r
def field(s,n):
    for v in s.get("Value",[]):
        if v.get("Name")==n: return v

zr = get_data(load(BASE/"DT_Moria_Zones.json"))
lr = get_data(load(BASE/"DT_Moria_Landmarks.json"))

ELEV_SPEC = [
    ("Sandbox_Small_Elevator_FirstStair",   "Sandbox.FirstStair",     True,  "SandboxSmall-Chapter01.Level1", "SandboxSmall-Chapter02.Level2"),
    ("Sandbox_Small_Elevator_SecondStair",  "Sandbox.SecondStair",    True,  "SandboxSmall-Chapter13.Deep2",  "SandboxSmall-Chapter12.Deep3"),
    ("Sandbox_Small_Elevator_ThirdStair",   "Sandbox.ThirdStair",     True,  "SandboxSmall-Chapter04.Level4", "SandboxSmall-Chapter05.Level5"),
    ("Sandbox_Small_Elevator_FourthStair",  "Sandbox.FourthStair",    True,  "SandboxSmall-Chapter04.Level4", "SandboxSmall-Chapter03.Level3"),
    ("Sandbox_Small_Elevator_FifthStair",   "Sandbox.FifthStair",     True,  "SandboxSmall-Chapter11.Deep4",  "SandboxSmall-Chapter12.Deep3"),
    ("Sandbox_Small_Elevator_SixthStair",   "Sandbox.SixthStair",     True,  "SandboxSmall-Chapter06.Level6", "SandboxSmall-Chapter05.Level5"),
    ("Sandbox_Small_Elevator_SeventhStair", "Sandbox.SeventhStair",   True,  "SandboxSmall-Chapter10.Deep5",  "SandboxSmall-Chapter11.Deep4"),
    ("Sandbox_Small_Elevator_EighthStair",  "Sandbox.EighthStair",    False, "SandboxSmall-Chapter07.Level7", "SandboxSmall-Chapter06.Level6"),
    ("Sandbox_Small_Elevator_NinthStair",   "Sandbox.NinthStair",     True,  "SandboxSmall-Chapter13.Deep2",  "SandboxSmall-Chapter14.Deep1"),
    ("Sandbox_Small_Elevator_TenthStair",   "Sandbox.TenthStair",     True,  "SandboxSmall-Chapter01.Level1", "SandboxSmall-Chapter14.Deep1"),
    ("Sandbox_Small_Elevator_EleventhStair","Sandbox.EleventhStair",  True,  "SandboxSmall-Chapter02.Level2", "SandboxSmall-Chapter03.Level3"),
    ("Sandbox_Small_Elevator_CrystalDescent","Sandbox.CrystalDescent",True,  "SandboxSmall-Chapter09.Deep6",  "SandboxSmall-Chapter10.Deep5"),
    ("Sandbox_Small_Elevator_LowerDescent", "Sandbox.LowerDescent",   True,  "SandboxSmall-Chapter09.Deep6",  "SandboxSmall-Chapter08.Deep7"),
]

print("\n" + "=" * 80)
print("PER-ELEVATOR CONFIG TABLE")
print("=" * 80)
hdr = f"{'Zone':40s} {'Pos':10s} {'Size':10s} {'PFL':4s} {'LH#':4s} {'Landmark':22s} {'ext':6s} {'Primary':32s} {'Additional':32s}"
print(hdr); print("-" * len(hdr))
all_ok = True
for zn, exp_lh, exp_ext, exp_chap, exp_add in ELEV_SPEC:
    z = find(zr, zn)
    pos = field(z,"Position")["Value"][0]["Value"]
    sz  = field(z,"TargetSize")["Value"][0]["Value"]
    pfl = field(z,"bPositionFromLandmarks")["Value"]
    pfz = field(z,"bPositionFromZoneTable")["Value"]
    es  = field(z,"EnabledState")["Value"]
    lh  = field(z,"LandmarkHandles")["Value"]
    ch  = field(z,"Chapter")
    chrn = next((v["Value"] for v in ch["Value"] if v.get("Name")=="RowName"), None)
    ach = field(z,"AdditionalChapters")
    achs=[]
    for entry in ach.get("Value",[]):
        for v in entry["Value"]:
            if v.get("Name")=="RowName": achs.append(v["Value"])
    lh_rn=lh_ext=lh_pl=None
    for entry in lh:
        for v in entry["Value"]:
            if v.get("Name")=="Landmark":
                for vv in v["Value"]:
                    if vv.get("Name")=="RowName": lh_rn=vv["Value"]
            elif v.get("Name")=="bExtendedConnectivityLandmark": lh_ext=v["Value"]
            elif v.get("Name")=="Placement": lh_pl=v["Value"]
    ok = (
        (pos["X"],pos["Y"],pos["Z"])==(0,0,0) and
        (sz["X"],sz["Y"],sz["Z"])==(6,6,4) and
        pfl is True and pfz is True and
        es=="ERowEnabledState::Live" and
        len(lh)==1 and lh_rn==exp_lh and lh_ext==exp_ext and
        lh_pl=="EZoneBubblePlacement::Fixed" and
        chrn==exp_chap and achs==[exp_add]
    )
    if not ok: all_ok=False
    posS=f"{pos['X']},{pos['Y']},{pos['Z']}"
    szS=f"{sz['X']},{sz['Y']},{sz['Z']}"
    print(f"{zn:40s} ({posS:8s}) ({szS:8s}) {str(pfl):4s} {len(lh):<4d} {lh_rn:22s} {str(lh_ext):6s} {chrn:32s} {achs[0] if achs else '':32s}")
print(f"\nAll match spec: {'YES' if all_ok else 'NO'}")

print("\n" + "=" * 80)
print("STAIR LANDMARK BP TABLE (must remain at synced (10,4|19,*) values)")
print("=" * 80)
EXPECTED_STAIR_BPS = {
    "Sandbox.FirstStair":     (10,19,18),
    "Sandbox.SecondStair":    (10, 4,13),
    "Sandbox.ThirdStair":     (10, 4,23),
    "Sandbox.FourthStair":    (10,19,22),
    "Sandbox.FifthStair":     (10,19, 8),
    "Sandbox.SixthStair":     (10,19,27),
    "Sandbox.SeventhStair":   (10, 4, 4),
    "Sandbox.EighthStair":    (10, 4,28),
    "Sandbox.NinthStair":     (10,19,14),
    "Sandbox.TenthStair":     (10, 4,17),
    "Sandbox.EleventhStair":  (10, 4,20),
    "Sandbox.CrystalDescent": (10,19, 1),
    "Sandbox.LowerDescent":   (10, 5, 0),
}
stair_ok=True
for sk, exp in EXPECTED_STAIR_BPS.items():
    lm = find(lr, sk)
    bp = field(lm,"BasePosition")["Value"][0]["Value"]
    cur=(bp["X"],bp["Y"],bp["Z"])
    flag = "OK" if cur==exp else f"DRIFT (expected {exp})"
    if cur!=exp: stair_ok=False
    print(f"  {sk:30s} BP={cur}  {flag}")
print(f"\nStair BPs unchanged: {'YES' if stair_ok else 'NO'}")

print("\n" + "=" * 80)
print("LORE LANDMARK SENTINEL BPs")
print("=" * 80)
LORE = [
    ("Sandbox.NogrodForge",      (0, 0, 27)),
    ("Sandbox.MithrilForge",     (0, 0, 1)),
    ("Sandbox.MithrilMineNexus", (0, 0, 1)),
    ("Sandbox.Drainworks",       (0, 0, 13)),
    ("Sandbox.LibrarySpring",    (0, 0, 9)),
    ("Sandbox.HeadwaterNexus",   (0, 0, 13)),
    ("Sandbox.BelegostForge",    (0, 0, 9)),
    ("Sandbox.ValleyOfKings",    (0, 0, 13)),
    ("Sandbox.Deep1MineNexus",   (0, 0, 17)),
]
lore_ok=True
for lk, exp in LORE:
    lm = find(lr, lk)
    bp = field(lm,"BasePosition")["Value"][0]["Value"]
    cur=(bp["X"],bp["Y"],bp["Z"])
    flag = "OK" if cur==exp else f"FAIL (expected {exp})"
    if cur!=exp: lore_ok=False
    print(f"  {lk:30s} BP={cur}  {flag}")
print(f"\nLore sentinel BPs OK: {'YES' if lore_ok else 'NO'}")

print("\n" + "=" * 80)
print(f"OVERALL: validator_errors={len(errors)} validator_warnings={len(warnings)}  "
      f"elevators={'OK' if all_ok else 'FAIL'}  stairs={'OK' if stair_ok else 'FAIL'}  lore={'OK' if lore_ok else 'FAIL'}")
print("=" * 80)
