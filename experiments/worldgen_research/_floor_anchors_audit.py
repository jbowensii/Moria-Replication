"""Audit Lv-3, Lv-4, Lv-5 content zones for landmark anchors and identify orphan landmarks.

Outputs:
  - Live SS landmarks not hosted by any Live SS zone (orphans).
  - Each target zone's current LandmarkHandles count.
"""
import json, os
from pathlib import Path

BASE = Path(r"C:\Users\johnb\OneDrive\Documents\Projects\Moria-Replication\experiments\worldgen_research")

def load(p):
    with open(p, "r", encoding="utf-8") as f: return json.load(f)
def get_data(a):
    for e in a.get("Exports", []):
        if "Table" in e: return e["Table"]["Data"]
def field(s, n):
    for v in s.get("Value", []):
        if v.get("Name") == n: return v
def get_iv(r, fn):
    f = field(r, fn)
    if not f: return None
    iv = f["Value"][0]["Value"]
    return (iv["X"], iv["Y"], iv["Z"])

zones = load(BASE / "DT_Moria_Zones.json")
lms = load(BASE / "DT_Moria_Landmarks.json")
zrows = get_data(zones); lrows = get_data(lms)

def is_live_ss(r):
    z = field(r, "ZoneSet"); s = field(r, "EnabledState")
    return (z and z.get("Value") == "EZoneSet::SandboxSmall" and
            s and s.get("Value") == "ERowEnabledState::Live")
live_ss = [r for r in zrows if is_live_ss(r)]

# Collect all landmark RowNames referenced by any Live SS zone
referenced_lms = set()
for z in live_ss:
    lh = field(z, "LandmarkHandles")
    if not lh: continue
    for entry in lh.get("Value", []):
        rh = entry["Value"][0]
        rn = rh["Value"][0]["Value"]
        referenced_lms.add(rn)

# All Live (non-Disabled) landmarks
def lm_enabled(r):
    es = field(r, "EnabledState")
    if not es: return True  # absent = treat as live
    return es.get("Value") != "ERowEnabledState::Disabled"

live_lms = [r for r in lrows if lm_enabled(r)]
orphan_lms = [r for r in live_lms if r["Name"] not in referenced_lms and r["Name"].startswith("Sandbox.")]

print("=" * 80)
print(f"ORPHAN LANDMARKS (Live but not referenced by any Live SS zone): {len(orphan_lms)}")
print("=" * 80)
for r in orphan_lms:
    bp = get_iv(r, "BasePosition")
    iid = field(r, "InternalId")
    tag = iid["Value"][0]["Value"] if iid else "?"
    print(f"  {r['Name']:50s}  BP={bp}  Tag={tag}")

# Target zones to audit
TARGETS = {
    "Lv-3": ["Sandbox_Small_City_D", "Sandbox_Small_Mines_B"],
    "Lv-4": ["Sandbox_Small_Suburban_D", "Sandbox_Small_DestroyedCity_B", "Sandbox_Small_DarkestDeeps_E"],
    "Lv-5": ["Sandbox_Small_MusteringHalls", "Sandbox_Small_OrcTown_D_Redeye", "Sandbox_Small_City_B_Dwarrowdelf"],
}

print("\n" + "=" * 80)
print("TARGET ZONE LANDMARK HANDLE STATUS")
print("=" * 80)
zmap = {z["Name"]: z for z in live_ss}
for floor, names in TARGETS.items():
    print(f"\n[{floor}]")
    for n in names:
        z = zmap.get(n)
        if not z:
            print(f"  ! {n}: NOT FOUND or not Live SS")
            continue
        p = get_iv(z, "Position"); s = get_iv(z, "TargetSize")
        center = (p[0] + s[0] // 2, p[1] + s[1] // 2, p[2])
        lh = field(z, "LandmarkHandles")
        lh_names = []
        if lh:
            for e in lh.get("Value", []):
                rh = e["Value"][0]
                lh_names.append(rh["Value"][0]["Value"])
        print(f"  {n:45s}  Pos={p} Sz={s}  Center={center}  LH({len(lh_names)})={lh_names}")
