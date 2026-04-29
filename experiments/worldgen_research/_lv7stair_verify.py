import json, os
BASE = os.path.dirname(os.path.abspath(__file__))
ZP = os.path.join(BASE, "DT_Moria_Zones.json")
LP = os.path.join(BASE, "DT_Moria_Landmarks.json")
WP = os.path.join(BASE, "World.json")

def load(p):
    with open(p,"r",encoding="utf-8") as f: return json.load(f)

zones = load(ZP); lms = load(LP); world = load(WP)
def get_data(a):
    for e in a.get("Exports",[]):
        if "Table" in e: return e["Table"]["Data"]
zr = get_data(zones); lr = get_data(lms)
def find(rows,k):
    for r in rows:
        if r.get("Name")==k: return r
def field(s,n):
    for v in s.get("Value",[]):
        if v.get("Name")==n: return v

ed = find(zr,"Sandbox_Small_Elevator_D")
edp = field(ed,"Position")["Value"][0]["Value"]
edsz = field(ed,"TargetSize")["Value"][0]["Value"]
ed_z_lo, ed_z_hi = edp["Z"], edp["Z"]+edsz["Z"]-1
ed_x_lo, ed_x_hi = edp["X"], edp["X"]+edsz["X"]-1
ed_y_lo, ed_y_hi = edp["Y"], edp["Y"]+edsz["Y"]-1
print(f"Elevator_D: Pos=({edp['X']},{edp['Y']},{edp['Z']}) Sz=({edsz['X']},{edsz['Y']},{edsz['Z']}) -> X={ed_x_lo}..{ed_x_hi} Y={ed_y_lo}..{ed_y_hi} Z={ed_z_lo}..{ed_z_hi}")
assert ed_z_lo==23 and ed_z_hi==28, "Elevator_D Z range FAIL"

dc = find(zr,"Sandbox_Small_DestroyedCity_A_Desolation")
dcp = field(dc,"Position")["Value"][0]["Value"]
dcsz = field(dc,"TargetSize")["Value"][0]["Value"]
dc_x_lo, dc_x_hi = dcp["X"], dcp["X"]+dcsz["X"]-1
dc_y_lo, dc_y_hi = dcp["Y"], dcp["Y"]+dcsz["Y"]-1
dc_z_lo, dc_z_hi = dcp["Z"], dcp["Z"]+dcsz["Z"]-1
print(f"DestroyedCity_A_Desolation: X={dc_x_lo}..{dc_x_hi} Y={dc_y_lo}..{dc_y_hi} Z={dc_z_lo}..{dc_z_hi}")
assert (dc_x_lo,dc_x_hi)==(4,9) and (dc_y_lo,dc_y_hi)==(1,6) and (dc_z_lo,dc_z_hi)==(28,29), "DC_A footprint FAIL"

# Cell collision check
collide=[]
for x in range(max(ed_x_lo,dc_x_lo), min(ed_x_hi,dc_x_hi)+1):
    for y in range(max(ed_y_lo,dc_y_lo), min(ed_y_hi,dc_y_hi)+1):
        for z in range(max(ed_z_lo,dc_z_lo), min(ed_z_hi,dc_z_hi)+1):
            collide.append((x,y,z))
print("Zone-zone collision cells (Elevator_D vs DC_A):", collide)
assert not collide, "COLLISION REMAINS"

# EighthStair landmark
es = find(lr,"Sandbox.EighthStair")
assert es is not None, "EighthStair missing"
bp = field(es,"BasePosition")["Value"][0]["Value"]
print(f"EighthStair BP=({bp['X']},{bp['Y']},{bp['Z']})")
assert (bp["X"],bp["Y"],bp["Z"])==(12,8,28)

# LandmarkHandles on Elevator_D
lh = field(ed,"LandmarkHandles")["Value"]
print(f"Elevator_D LandmarkHandles count: {len(lh)}")
entries=[]
for entry in lh:
    rn=None; ext=None; pl=None
    for v in entry["Value"]:
        if v.get("Name")=="Landmark":
            for vv in v["Value"]:
                if vv.get("Name")=="RowName": rn=vv["Value"]
        elif v.get("Name")=="bExtendedConnectivityLandmark": ext=v["Value"]
        elif v.get("Name")=="Placement": pl=v["Value"]
    entries.append((rn,ext,pl))
    print("  ", rn, "ext=",ext,"pl=",pl)
assert len(lh)==3
refs=[e[0] for e in entries]
assert "Sandbox.ThirdStair" in refs and "Sandbox.SixthStair" in refs and "Sandbox.EighthStair" in refs
for rn,ext,pl in entries:
    if rn=="Sandbox.EighthStair":
        assert ext is False, "EighthStair should be ext=False"
    if rn in ("Sandbox.ThirdStair","Sandbox.SixthStair"):
        assert ext is True

# Top tile at Z=28 within Lv-7 PrimeZ=28 - Elevator_D Z hi 28 confirmed
print("Elevator_D top Z=28 matches Chapter07.Level7 PrimeZ=28: OK")

# NameMap counts consistency
def chk(a, label):
    nm = a.get("NameMap",[])
    nrefed = a.get("NamesReferencedFromExportDataCount")
    gen = a.get("Generations",[{}])[0].get("NameCount")
    print(f"{label}: |NameMap|={len(nm)} NRefED={nrefed} Gen0={gen}")
    assert nrefed==len(nm)
    assert gen >= len(nm)
chk(zones,"Zones"); chk(lms,"Landmarks"); chk(world,"World")
print("\nALL CHECKS PASSED")
