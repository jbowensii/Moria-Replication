import json, os
BASE = r"C:\Users\johnb\OneDrive\Documents\Projects\Moria-Replication\experiments\worldgen_research"
def load(n):
    with open(os.path.join(BASE, n), "r", encoding="utf-8") as f:
        return json.load(f)

zones = load("DT_Moria_Zones.json")
landmarks = load("DT_Moria_Landmarks.json")
chapters = load("DT_Moria_Chapters.json")
world = load("World.json")

def find_export_with_table(d):
    for e in d.get("Exports", []):
        if "Table" in e and isinstance(e["Table"], dict) and "Data" in e["Table"]:
            return e
    return None

def find_field(row, name):
    for v in row.get("Value", []):
        if v.get("Name") == name:
            return v
    return None

def get_iv(row, fname):
    f = find_field(row, fname)
    if not f: return None
    iv = f["Value"][0]["Value"]
    return (iv["X"], iv["Y"], iv["Z"])

zexp = find_export_with_table(zones)
zrows = zexp["Table"]["Data"]
def is_live_ss(r):
    z = find_field(r, "ZoneSet")
    s = find_field(r, "EnabledState")
    return (z and z.get("Value") == "EZoneSet::SandboxSmall" and
            s and s.get("Value") == "ERowEnabledState::Live")
live_ss = [r for r in zrows if is_live_ss(r)]
zoneinfo = []
for r in live_ss:
    p = get_iv(r, "Position"); s = get_iv(r, "TargetSize")
    if p and s:
        zoneinfo.append((r["Name"], p, s))

stairs = [(n,p,s) for n,p,s in zoneinfo if "Elevator" in n]
stairs.sort(key=lambda t: t[1][2])

print("=== Final stair zones ===")
for n,p,s in stairs:
    print(f"  {n}: Pos={p} Sz={s} Z={p[2]}..{p[2]+s[2]-1}")

print("\n=== Z=0..29 coverage ===")
all_covered = True
for z in range(30):
    cov = [n for n,p,s in stairs if p[2] <= z <= p[2]+s[2]-1]
    if not cov: all_covered = False
    print(f"  Z={z:2d}: {[n.replace('Sandbox_Small_','') for n in cov]}")
print(f"\nAll Z covered: {all_covered}")

print("\n=== Consecutive stair overlap pairs ===")
all_overlap = True
for i in range(len(stairs)-1):
    n1,p1,s1 = stairs[i]; n2,p2,s2 = stairs[i+1]
    z1lo, z1hi = p1[2], p1[2]+s1[2]-1
    z2lo, z2hi = p2[2], p2[2]+s2[2]-1
    olo = max(z1lo, z2lo); ohi = min(z1hi, z2hi)
    cells = max(0, ohi - olo + 1)
    ok = cells >= 1
    if not ok: all_overlap = False
    print(f"  {n1.replace('Sandbox_Small_','')} (Z={z1lo}..{z1hi})  <->  {n2.replace('Sandbox_Small_','')} (Z={z2lo}..{z2hi}): overlap Z={olo}..{ohi} ({cells} cell{'s' if cells!=1 else ''}) {'OK' if ok else 'FAIL'}")
print(f"\nAll consecutive overlaps OK: {all_overlap}")

# Cell-level collision: Elev_H vs other live SS zones at Z=13..18
print("\n=== Elev_H cell-level collision check (Z=13..18) ===")
elh = next((n,p,s) for n,p,s in zoneinfo if n == "Sandbox_Small_Elevator_H")
n,p,s = elh
ex=(p[0],p[0]+s[0]-1); ey=(p[1],p[1]+s[1]-1); ez=(p[2],p[2]+s[2]-1)
collisions = []
for nn,pp,ss in zoneinfo:
    if nn == "Sandbox_Small_Elevator_H": continue
    ox=(pp[0],pp[0]+ss[0]-1); oy=(pp[1],pp[1]+ss[1]-1); oz=(pp[2],pp[2]+ss[2]-1)
    if (max(ex[0],ox[0])<=min(ex[1],ox[1]) and
        max(ey[0],oy[0])<=min(ey[1],oy[1]) and
        max(ez[0],oz[0])<=min(ez[1],oz[1])):
        collisions.append(nn)
print(f"  Elev_H collisions: {collisions}")

# Elev_D cell-level vs DestroyedCity_A_Desolation
print("\n=== Elev_D vs DestroyedCity_A_Desolation ===")
ed = next((n,p,s) for n,p,s in zoneinfo if n == "Sandbox_Small_Elevator_D")
dca = next(((n,p,s) for n,p,s in zoneinfo if n == "Sandbox_Small_DestroyedCity_A_Desolation"), None)
print(f"  Elev_D: {ed}, DCA: {dca}")
if dca:
    n,p,s=ed; nn,pp,ss=dca
    ex=(p[0],p[0]+s[0]-1); ey=(p[1],p[1]+s[1]-1); ez=(p[2],p[2]+s[2]-1)
    ox=(pp[0],pp[0]+ss[0]-1); oy=(pp[1],pp[1]+ss[1]-1); oz=(pp[2],pp[2]+ss[2]-1)
    coll = (max(ex[0],ox[0])<=min(ex[1],ox[1]) and
            max(ey[0],oy[0])<=min(ey[1],oy[1]) and
            max(ez[0],oz[0])<=min(ez[1],oz[1]))
    print(f"  Collide: {coll}")

# NameMap consistency
print("\n=== NameMap counts (post) ===")
def info(d, label):
    nm = d.get("NameMap", [])
    nrc = d.get("NamesReferencedFromExportDataCount")
    gens = d.get("Generations", [])
    nc = gens[0].get("NameCount") if gens else None
    print(f"  {label}: NameMap={len(nm)} NRFE={nrc} Gen0.NameCount={nc} consistent={len(nm)==nrc and nc>=len(nm)}")
info(zones, "Zones")
info(landmarks, "Landmarks")
info(chapters, "Chapters")
info(world, "World")

# Confirm new entries exist
print("\n=== Existence checks ===")
zone_names = {r["Name"] for r in zrows}
print(f"  Zone Sandbox_Small_Elevator_H: {'Sandbox_Small_Elevator_H' in zone_names}")
cexp = find_export_with_table(chapters)
ch_names = {r["Name"] for r in cexp["Table"]["Data"]}
print(f"  Chapter SandboxSmall-Chapter14.Elevator_H: {'SandboxSmall-Chapter14.Elevator_H' in ch_names}")
lexp = find_export_with_table(landmarks)
lm_names = {r["Name"] for r in lexp["Table"]["Data"]}
for lm in ["Sandbox.NinthStair","Sandbox.TenthStair","Sandbox.EleventhStair"]:
    print(f"  Landmark {lm}: {lm in lm_names}")
wval = world["Exports"][0]["Table"]["Value"]
wkeys = {v[0] for v in wval}
for k in ["Landmarks.Sandbox.NinthStair","Landmarks.Sandbox.TenthStair","Landmarks.Sandbox.EleventhStair"]:
    print(f"  StringTable {k}: {k in wkeys}")

# Elev_D landmarkhandles
elev_d = next(r for r in zrows if r["Name"] == "Sandbox_Small_Elevator_D")
lh = find_field(elev_d, "LandmarkHandles")
names_in_lh = []
for entry in lh["Value"]:
    rh = entry["Value"][0]
    names_in_lh.append(rh["Value"][0]["Value"])
print(f"  Elev_D LandmarkHandles: {names_in_lh}")

# Elev_H landmarkhandles
elev_h = next(r for r in zrows if r["Name"] == "Sandbox_Small_Elevator_H")
lh = find_field(elev_h, "LandmarkHandles")
hh = []
for entry in lh["Value"]:
    rh = entry["Value"][0]
    nm = rh["Value"][0]["Value"]
    ext = entry["Value"][2]["Value"]
    hh.append((nm, f"ext={ext}"))
print(f"  Elev_H LandmarkHandles: {hh}")
