import json, os, sys

BASE = r"C:\Users\johnb\OneDrive\Documents\Projects\Moria-Replication\experiments\worldgen_research"
ZONES = os.path.join(BASE, "DT_Moria_Zones.json")
LM = os.path.join(BASE, "DT_Moria_Landmarks.json")
CH = os.path.join(BASE, "DT_Moria_Chapters.json")
WORLD = os.path.join(BASE, "World.json")

def load(p):
    with open(p, "r", encoding="utf-8") as f:
        return json.load(f)

zones = load(ZONES)
landmarks = load(LM)
chapters = load(CH)

def find_export(d):
    # Find Export with Table->Data
    for e in d.get("Exports", []):
        if "Table" in e and "Data" in e["Table"]:
            return e
    return None

zexp = find_export(zones)
zrows = zexp["Table"]["Data"]
print(f"Zones: {len(zrows)} rows")

def get_struct_field(row, name):
    for v in row.get("Value", []):
        if v.get("Name") == name:
            return v
    return None

def get_intpoint(row, fname):
    f = get_struct_field(row, fname)
    if not f:
        return None
    inner = f.get("Value", [])
    if not inner:
        return None
    iv = inner[0].get("Value")
    if isinstance(iv, dict):
        return (iv.get("X"), iv.get("Y"), iv.get("Z"))
    return None

def get_name(row, fname):
    f = get_struct_field(row, fname)
    if not f:
        return None
    return f.get("Value")

def get_enum(row, fname):
    f = get_struct_field(row, fname)
    if not f:
        return None
    return f.get("Value")

# Collect zones with positions
LIVE = "ERowEnabledState::Live"

# Build map of name->zone
zonemap = {}
for r in zrows:
    n = r.get("Name")
    zonemap[n] = r

# Print SandboxSmall zones
ssm = [n for n in zonemap if n.startswith("Sandbox_Small_")]
print(f"SandboxSmall zones: {len(ssm)}")

def zone_state(r):
    f = get_struct_field(r, "EnabledState")
    if f:
        return f.get("Value")
    return None

def zone_zoneset(r):
    f = get_struct_field(r, "ZoneSet")
    if f:
        v = f.get("Value")
        if isinstance(v, str):
            return v.split("::")[-1] if "::" in v else v
    return None

# Filter Live zones with ZoneSet=SandboxSmall
def is_sandboxsmall_live(r):
    if zone_state(r) != LIVE:
        return False
    zs = zone_zoneset(r)
    return zs == "SandboxSmall"

live_ss = [r for r in zrows if is_sandboxsmall_live(r)]
print(f"Live SandboxSmall zones: {len(live_ss)}")

# Build (pos, size, name) tuples
zoneinfo = []
for r in live_ss:
    pos = get_intpoint(r, "Position")
    sz = get_intpoint(r, "TargetSize")
    if pos and sz:
        zoneinfo.append((r["Name"], pos, sz))

# Show stairs
print("\n=== Current stair zones ===")
for n, p, s in sorted(zoneinfo, key=lambda t: t[1][2]):
    if "Elevator" in n:
        print(f"  {n}: Pos={p} Sz={s} Z={p[2]}..{p[2]+s[2]-1}")

# Per-Z coverage
print("\n=== Per-Z coverage (current) ===")
stairs = [(n,p,s) for n,p,s in zoneinfo if "Elevator" in n]
for z in range(30):
    cov = [n for n,p,s in stairs if p[2] <= z <= p[2]+s[2]-1]
    print(f"  Z={z:2d}: {cov}")

# After changes:
print("\n=== With Elev_D extended Sz.Z 6->7 ===")
print("Elev_D: Pos=(10,6,23) Sz=(6,6,7) → Z=23..29")

# Check Elev_D vs DestroyedCity_A_Desolation
# Need to find DestroyedCity_A_Desolation
dcad = zonemap.get("Sandbox_Small_DestroyedCity_A_Desolation")
if dcad:
    p = get_intpoint(dcad, "Position")
    s = get_intpoint(dcad, "TargetSize")
    st = zone_state(dcad)
    print(f"  DestroyedCity_A_Desolation: Pos={p} Sz={s} state={st}")
    if p and s:
        print(f"    X={p[0]}..{p[0]+s[0]-1} Y={p[1]}..{p[1]+s[1]-1} Z={p[2]}..{p[2]+s[2]-1}")
        # Elev_D extended: X=10..15 Y=6..11 Z=23..29
        ex = (10, 15); ey = (6, 11); ez = (23, 29)
        ox = (p[0], p[0]+s[0]-1); oy = (p[1], p[1]+s[1]-1); oz = (p[2], p[2]+s[2]-1)
        ox_ov = max(ex[0], ox[0]) <= min(ex[1], ox[1])
        oy_ov = max(ey[0], oy[0]) <= min(ey[1], oy[1])
        oz_ov = max(ez[0], oz[0]) <= min(ez[1], oz[1])
        print(f"    Overlap with extended Elev_D? X={ox_ov} Y={oy_ov} Z={oz_ov} → collide={ox_ov and oy_ov and oz_ov}")

# Candidate Elev_H footprints
print("\n=== Candidate footprints for Elev_H Z=13..18 ===")
candidates = [
    ("A", (0, 22, 13), (6, 6, 6)),
    ("B", (24, 24, 13), (6, 6, 6)),
    ("C", (0, 0, 13), (6, 6, 6)),
]
# Find all live SS zones overlapping Z=13..18
def overlaps_z(p, s, lo, hi):
    return max(p[2], lo) <= min(p[2]+s[2]-1, hi)

candidates_z = [(n,p,s) for n,p,s in zoneinfo if overlaps_z(p, s, 13, 18)]
print(f"  Live SS zones overlapping Z=13..18: {len(candidates_z)}")
for n,p,s in candidates_z:
    print(f"    {n}: Pos={p} Sz={s}")

print("\n  Per-candidate cell collision check:")
for label, cp, cs in candidates:
    cx = (cp[0], cp[0]+cs[0]-1)
    cy = (cp[1], cp[1]+cs[1]-1)
    cz = (cp[2], cp[2]+cs[2]-1)
    collisions = []
    for n,p,s in candidates_z:
        ox = (p[0], p[0]+s[0]-1); oy = (p[1], p[1]+s[1]-1); oz = (p[2], p[2]+s[2]-1)
        if (max(cx[0], ox[0]) <= min(cx[1], ox[1]) and
            max(cy[0], oy[0]) <= min(cy[1], oy[1]) and
            max(cz[0], oz[0]) <= min(cz[1], oz[1])):
            collisions.append(n)
    print(f"    Candidate {label} Pos={cp} Sz={cs}: collisions={collisions}")

# Check existing landmark names
print("\n=== Landmark name check ===")
lexp = find_export(landmarks)
lrows = lexp["Table"]["Data"]
lnames = [r.get("Name") for r in lrows]
for nm in ["Sandbox.NinthStair", "Sandbox.TenthStair", "Sandbox.EleventhStair"]:
    print(f"  {nm}: exists={nm in lnames}")

# Print Sandbox stairs landmarks
print("  Existing Sandbox*Stair landmarks:")
for n in lnames:
    if n and "Stair" in n and "Sandbox" in n:
        print(f"    {n}")

# Chapter rows
print("\n=== Chapter rows ===")
cexp = find_export(chapters)
crows = cexp["Table"]["Data"]
cnames = [r.get("Name") for r in crows]
print(f"  Total: {len(crows)}")
for n in cnames:
    if n and "SandboxSmall-Chapter1" in n and ("Elev" in n or "Chapter12" in n or "Chapter14" in n):
        print(f"    {n}")
print(f"  Chapter14.Elevator_H exists: {'SandboxSmall-Chapter14.Elevator_H' in cnames}")

# Check World.json StringTable for needed keys
print("\n=== World.json StringTable check ===")
world = load(WORLD)
def find_stringtable_keys(obj):
    keys = set()
    def walk(x):
        if isinstance(x, dict):
            # StringTable structure
            if x.get("$type", "").endswith("UAssetAPI.PropertyTypes.Structs.StringTablePropertyData, UAssetAPI") or x.get("$type", "").startswith("UAssetAPI.PropertyTypes.Objects.StringTable"):
                pass
            for v in x.values():
                walk(v)
        elif isinstance(x, list):
            for v in x:
                walk(v)
    walk(obj)
    return keys

# Just search keys directly in flattened
import re
text = json.dumps(world)
for k in ["Landmarks.Sandbox.NinthStair", "Landmarks.Sandbox.TenthStair", "Landmarks.Sandbox.EleventhStair"]:
    print(f"  '{k}' present in World.json: {k in text}")

# NameMap counts
def namemap_info(d, label):
    nm = d.get("NameMap", [])
    nrc = d.get("NamesReferencedFromExportDataCount")
    gens = d.get("Generations", [])
    nc = gens[0].get("NameCount") if gens else None
    print(f"  {label}: NameMap={len(nm)} NamesReferencedFromExportDataCount={nrc} Gen0.NameCount={nc}")

print("\n=== NameMap counts (pre) ===")
namemap_info(zones, "Zones")
namemap_info(landmarks, "Landmarks")
namemap_info(chapters, "Chapters")
namemap_info(world, "World")
