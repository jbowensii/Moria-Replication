"""Audit current state of elevator zones and lore landmark BPs before factory reset."""
import json, os
BASE = os.path.dirname(os.path.abspath(__file__))

def load(p):
    with open(p,"r",encoding="utf-8") as f: return json.load(f)

zones = load(os.path.join(BASE,"DT_Moria_Zones.json"))
lms = load(os.path.join(BASE,"DT_Moria_Landmarks.json"))

def get_data(a):
    for e in a.get("Exports",[]):
        if "Table" in e: return e["Table"]["Data"]

def find(rows,k):
    for r in rows:
        if r.get("Name")==k: return r

def field(s,n):
    for v in s.get("Value",[]):
        if v.get("Name")==n: return v

zr = get_data(zones); lr = get_data(lms)

ELEV_ZONES = [
    "Sandbox_Small_Elevator_FirstStair","Sandbox_Small_Elevator_SecondStair",
    "Sandbox_Small_Elevator_ThirdStair","Sandbox_Small_Elevator_FourthStair",
    "Sandbox_Small_Elevator_FifthStair","Sandbox_Small_Elevator_SixthStair",
    "Sandbox_Small_Elevator_SeventhStair","Sandbox_Small_Elevator_EighthStair",
    "Sandbox_Small_Elevator_NinthStair","Sandbox_Small_Elevator_TenthStair",
    "Sandbox_Small_Elevator_EleventhStair","Sandbox_Small_Elevator_CrystalDescent",
    "Sandbox_Small_Elevator_LowerDescent",
]

print("=== ELEVATOR ZONE AUDIT ===")
for zn in ELEV_ZONES:
    z = find(zr, zn)
    if not z:
        print(f"  MISSING: {zn}")
        continue
    pos = field(z,"Position")
    sz = field(z,"TargetSize")
    pfl = field(z,"bPositionFromLandmarks")
    pfz = field(z,"bPositionFromZoneTable")
    es = field(z,"EnabledState")
    lh = field(z,"LandmarkHandles")
    ch = field(z,"Chapter")
    ach = field(z,"AdditionalChapters")
    p = pos["Value"][0]["Value"] if pos else None
    s = sz["Value"][0]["Value"] if sz else None
    chrn=None
    if ch:
        for v in ch["Value"]:
            if v.get("Name")=="RowName": chrn=v["Value"]
    achs=[]
    if ach:
        for entry in ach.get("Value",[]):
            for v in entry["Value"]:
                if v.get("Name")=="RowName": achs.append(v["Value"])
    lh_entries=[]
    if lh:
        for entry in lh.get("Value",[]):
            rn=None; ext=None; pl=None
            for v in entry["Value"]:
                if v.get("Name")=="Landmark":
                    for vv in v["Value"]:
                        if vv.get("Name")=="RowName": rn=vv["Value"]
                elif v.get("Name")=="bExtendedConnectivityLandmark": ext=v["Value"]
                elif v.get("Name")=="Placement": pl=v["Value"]
            lh_entries.append((rn,ext,pl))
    print(f"\n{zn}:")
    print(f"  Pos={p['X'],p['Y'],p['Z']} Size={s['X'],s['Y'],s['Z']}")
    print(f"  bPosFromLM={pfl['Value'] if pfl else None} bPosFromZT={pfz['Value'] if pfz else None}")
    print(f"  EnabledState={es['Value'] if es else None}")
    print(f"  Chapter={chrn} Additional={achs}")
    print(f"  LH count={len(lh_entries)}: {lh_entries}")

print("\n=== LORE LANDMARK BP AUDIT ===")
LORE = ["Sandbox.NogrodForge","Sandbox.MithrilForge","Sandbox.MithrilMineNexus",
        "Sandbox.Drainworks","Sandbox.LibrarySpring","Sandbox.HeadwaterNexus",
        "Sandbox.BelegostForge","Sandbox.ValleyOfKings","Sandbox.Deep1MineNexus"]
for lk in LORE:
    lm = find(lr,lk)
    if not lm:
        print(f"  MISSING: {lk}"); continue
    bp = field(lm,"BasePosition")
    p = bp["Value"][0]["Value"] if bp else None
    print(f"  {lk}: BP=({p['X']},{p['Y']},{p['Z']})")

print("\n=== STAIR LANDMARK BP AUDIT ===")
STAIRS = ["Sandbox.FirstStair","Sandbox.SecondStair","Sandbox.ThirdStair","Sandbox.FourthStair",
          "Sandbox.FifthStair","Sandbox.SixthStair","Sandbox.SeventhStair","Sandbox.EighthStair",
          "Sandbox.NinthStair","Sandbox.TenthStair","Sandbox.EleventhStair",
          "Sandbox.CrystalDescent","Sandbox.LowerDescent"]
for sk in STAIRS:
    lm = find(lr,sk)
    if not lm:
        print(f"  MISSING: {sk}"); continue
    bp = field(lm,"BasePosition")
    p = bp["Value"][0]["Value"] if bp else None
    print(f"  {sk}: BP=({p['X']},{p['Y']},{p['Z']})")
