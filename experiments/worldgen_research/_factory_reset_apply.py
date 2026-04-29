"""Factory reset apply: backup checkpoint + reset elevator zones + reset lore landmark BPs."""
import json, os, shutil
BASE = os.path.dirname(os.path.abspath(__file__))

def load(p):
    with open(p,"r",encoding="utf-8") as f: return json.load(f)

def save(p, obj):
    with open(p,"w",encoding="utf-8") as f: json.dump(obj, f, indent=2)

# ---- Task 1: Backup ----
BACKUP_DIR = os.path.join(BASE, "backups", "Lv4 to D4 working")
os.makedirs(BACKUP_DIR, exist_ok=True)
BACKUP_FILES = ["DT_Moria_Zones.json","DT_Moria_Chapters.json","DT_Moria_Landmarks.json",
                "DT_Moria_LayoutConnections.json","World.json"]
print("=== BACKUP ===")
for fn in BACKUP_FILES:
    src = os.path.join(BASE, fn); dst = os.path.join(BACKUP_DIR, fn)
    shutil.copy2(src, dst)
    print(f"  {fn} -> {os.path.getsize(dst):,} bytes")

# ---- Task 2: Reset elevator zones ----
zones_path = os.path.join(BASE,"DT_Moria_Zones.json")
zones = load(zones_path)

def get_data(a):
    for e in a.get("Exports",[]):
        if "Table" in e: return e["Table"]["Data"]

def find(rows,k):
    for r in rows:
        if r.get("Name")==k: return r

def field(s,n):
    for v in s.get("Value",[]):
        if v.get("Name")==n: return v

zr = get_data(zones)

ELEV_ZONES = [
    "Sandbox_Small_Elevator_FirstStair","Sandbox_Small_Elevator_SecondStair",
    "Sandbox_Small_Elevator_ThirdStair","Sandbox_Small_Elevator_FourthStair",
    "Sandbox_Small_Elevator_FifthStair","Sandbox_Small_Elevator_SixthStair",
    "Sandbox_Small_Elevator_SeventhStair","Sandbox_Small_Elevator_EighthStair",
    "Sandbox_Small_Elevator_NinthStair","Sandbox_Small_Elevator_TenthStair",
    "Sandbox_Small_Elevator_EleventhStair","Sandbox_Small_Elevator_CrystalDescent",
    "Sandbox_Small_Elevator_LowerDescent",
]

print("\n=== ELEVATOR ZONE RESET ===")
for zn in ELEV_ZONES:
    z = find(zr, zn)
    if not z:
        print(f"  MISSING: {zn}"); continue
    pos = field(z,"Position")["Value"][0]["Value"]
    sz  = field(z,"TargetSize")["Value"][0]["Value"]
    before = (pos["X"],pos["Y"],pos["Z"], sz["X"],sz["Y"],sz["Z"])
    pos["X"]=0; pos["Y"]=0; pos["Z"]=0
    sz["X"]=6; sz["Y"]=6; sz["Z"]=4
    pfl = field(z,"bPositionFromLandmarks"); pfl["Value"]=True
    pfz = field(z,"bPositionFromZoneTable"); pfz["Value"]=True
    es = field(z,"EnabledState"); es["Value"]="ERowEnabledState::Live"
    after = (pos["X"],pos["Y"],pos["Z"], sz["X"],sz["Y"],sz["Z"])
    print(f"  {zn}: Pos/Size {before} -> {after}")

save(zones_path, zones)
print(f"\nSaved: {zones_path}")

# ---- Task 3: Reset lore landmark BPs ----
lms_path = os.path.join(BASE,"DT_Moria_Landmarks.json")
lms = load(lms_path)
lr = get_data(lms)

LORE_RESETS = [
    ("Sandbox.NogrodForge",      0, 0, 27),
    ("Sandbox.MithrilForge",     0, 0, 1),
    ("Sandbox.MithrilMineNexus", 0, 0, 1),
    ("Sandbox.Drainworks",       0, 0, 13),
    ("Sandbox.LibrarySpring",    0, 0, 9),
    ("Sandbox.HeadwaterNexus",   0, 0, 13),
    ("Sandbox.BelegostForge",    0, 0, 9),
    ("Sandbox.ValleyOfKings",    0, 0, 13),
    ("Sandbox.Deep1MineNexus",   0, 0, 17),
]

print("\n=== LORE BP RESET ===")
for lk, X, Y, Z in LORE_RESETS:
    lm = find(lr, lk)
    if not lm:
        print(f"  MISSING: {lk}"); continue
    bp = field(lm,"BasePosition")["Value"][0]["Value"]
    before = (bp["X"], bp["Y"], bp["Z"])
    bp["X"]=X; bp["Y"]=Y; bp["Z"]=Z
    after = (bp["X"], bp["Y"], bp["Z"])
    print(f"  {lk}: BP {before} -> {after}")

save(lms_path, lms)
print(f"\nSaved: {lms_path}")
print("\nDone.")
