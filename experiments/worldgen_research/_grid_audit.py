"""Grid redistribute audit (pre-state).

For each of the 10 active SS floor chapters, list Live SS non-elevator zones
whose primary Chapter row's ChapterNN prefix matches that floor.
Group: Chapter01..05 -> Level1..Level5 ; Chapter10..14 -> Deep5..Deep1.
Print Pos, Sz, variant cluster id. Show density % and current min-gap.
"""
import os, json, re
from collections import defaultdict

BASE = os.path.dirname(os.path.abspath(__file__))
ZP = os.path.join(BASE, "DT_Moria_Zones.json")
CP = os.path.join(BASE, "DT_Moria_Chapters.json")

# Floor key: chapter prefix number -> level chapter row name
FLOOR_FOR_PREFIX = {
    1:  "SandboxSmall-Chapter01.Level1",
    2:  "SandboxSmall-Chapter02.Level2",
    3:  "SandboxSmall-Chapter03.Level3",
    4:  "SandboxSmall-Chapter04.Level4",
    5:  "SandboxSmall-Chapter05.Level5",
    10: "SandboxSmall-Chapter10.Deep5",
    11: "SandboxSmall-Chapter11.Deep4",
    12: "SandboxSmall-Chapter12.Deep3",
    13: "SandboxSmall-Chapter13.Deep2",
    14: "SandboxSmall-Chapter14.Deep1",
}
FLOORS_ORDERED = [1,2,3,4,5,10,11,12,13,14]

CHAP_PREFIX_RE = re.compile(r"^SandboxSmall-Chapter(\d+)\.")

def chapter_prefix(rowname):
    if not rowname: return None
    m = CHAP_PREFIX_RE.match(rowname)
    if not m: return None
    return int(m.group(1))

def load(p):
    with open(p, "r", encoding="utf-8") as f: return json.load(f)
def get_data(asset):
    for exp in asset.get("Exports", []):
        if "Table" in exp and "Data" in exp["Table"]:
            return exp["Table"]["Data"]
def field(struct, name):
    for v in struct.get("Value", []):
        if v.get("Name") == name: return v
    return None
def rowname_of(struct, fname):
    f = field(struct, fname)
    if not f: return None
    for v in f.get("Value", []):
        if v.get("Name") == "RowName": return v.get("Value")
    return None
def intvec(struct, fname):
    f = field(struct, fname)
    if not f: return None
    val = f.get("Value", [])
    if not val: return None
    iv = val[0].get("Value", {})
    return (iv.get("X"), iv.get("Y"), iv.get("Z"))
def get_str(struct, fname):
    f = field(struct, fname)
    return f.get("Value") if f else None

def is_ss_zone(name): return name.startswith("Sandbox_Small_")
def is_elevator(name): return name.startswith("Sandbox_Small_Elevator_")

def rect_gap(p1, s1, p2, s2):
    """Cell gap (-1 if overlap) between two axis-aligned rectangles."""
    r1 = (p1[0], p1[1], p1[0]+s1[0]-1, p1[1]+s1[1]-1)
    r2 = (p2[0], p2[1], p2[0]+s2[0]-1, p2[1]+s2[1]-1)
    if r1[2] < r2[0]:   gx = r2[0] - r1[2] - 1
    elif r2[2] < r1[0]: gx = r1[0] - r2[2] - 1
    else:               gx = -1
    if r1[3] < r2[1]:   gy = r2[1] - r1[3] - 1
    elif r2[3] < r1[1]: gy = r1[1] - r2[3] - 1
    else:               gy = -1
    return max(gx, gy)

def main():
    zones = load(ZP); chapters = load(CP)
    zrows = get_data(zones); crows = get_data(chapters)

    chap_primez = {}
    for r in crows:
        nm = r.get("Name")
        pz = field(r, "PrimeZ")
        chap_primez[nm] = pz.get("Value") if pz else None

    print("=== Active floor PrimeZ ===")
    for k in FLOORS_ORDERED:
        flr = FLOOR_FOR_PREFIX[k]
        print(f"  prefix Chapter{k:02d} -> {flr}  PrimeZ={chap_primez.get(flr)}")

    # Group zones by floor prefix
    by_floor = defaultdict(list)
    for r in zrows:
        nm = r.get("Name", "")
        if not is_ss_zone(nm) or is_elevator(nm): continue
        en = get_str(r, "EnabledState")
        if en and "Live" not in en: continue
        chap = rowname_of(r, "Chapter")
        prefix = chapter_prefix(chap)
        if prefix not in FLOOR_FOR_PREFIX: continue
        pos = intvec(r, "Position")
        sz = intvec(r, "TargetSize")
        by_floor[prefix].append((nm, pos, sz))

    print("\n=== Pre-state per floor ===")
    summary = {}
    for k in FLOORS_ORDERED:
        flr = FLOOR_FOR_PREFIX[k]
        zs = by_floor[k]
        clusters = defaultdict(list)
        for (nm, pos, sz) in zs:
            clusters[(pos, sz)].append(nm)
        unique = list(clusters.keys())
        total_cells = sum(s[0]*s[1] for (_, s) in unique if s)
        density = total_cells / 900.0 * 100.0
        min_gap = None
        for i in range(len(unique)):
            for j in range(i+1, len(unique)):
                p1, s1 = unique[i]; p2, s2 = unique[j]
                if not (p1 and s1 and p2 and s2): continue
                g = rect_gap(p1, s1, p2, s2)
                if min_gap is None or g < min_gap: min_gap = g
        summary[k] = (len(zs), len(unique), density, min_gap)
        print(f"\n--- Chapter{k:02d} -> {flr} (PrimeZ={chap_primez.get(flr)}) zones={len(zs)} unique-clusters={len(unique)} ---")
        print(f"    density={density:.1f}%   min-gap={min_gap}")
        cid = 0
        for key, members in clusters.items():
            cid += 1
            pos, sz = key
            print(f"    cluster#{cid}  Pos={pos}  Sz={sz}  members={len(members)}")
            for m in members:
                print(f"        {m}")

    print("\n=== Summary table (pre) ===")
    print(f"{'Floor':<14} {'zones':>6} {'clusters':>9} {'density%':>9} {'min-gap':>8}")
    for k in FLOORS_ORDERED:
        z, u, d, g = summary[k]
        print(f"Chapter{k:02d}     {z:>6} {u:>9} {d:>9.1f} {str(g):>8}")

if __name__ == "__main__":
    main()
