"""Grid redistribute apply.

For each of 10 active floors (Chapter01..05 + Chapter10..14):
  - Find Live SS non-elevator zones whose Chapter prefix matches that floor.
  - Group into variant clusters by (Pos, Sz). Each cluster -> one grid cell.
  - Pack zones using row-major layout with PADDING=3 (fall back 2 then 1).
  - Propagate cluster representative position to all variant siblings.

Only Position.X and Position.Y change. Position.Z stays at PrimeZ.
TargetSize, Chapter, AdditionalChapters, LandmarkHandles unchanged.
"""
import os, json, re, shutil
from collections import defaultdict

BASE = os.path.dirname(os.path.abspath(__file__))
ZP = os.path.join(BASE, "DT_Moria_Zones.json")
CP = os.path.join(BASE, "DT_Moria_Chapters.json")
BACKUP = os.path.join(BASE, "DT_Moria_Zones.before_grid_redistribute.json")

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

WORLD = 30
START_X = 2
START_Y = 2

def load(p):
    with open(p, "r", encoding="utf-8") as f: return json.load(f)
def save(p, d):
    with open(p, "w", encoding="utf-8") as f: json.dump(d, f, indent=2)
def get_data(asset):
    for exp in asset.get("Exports", []):
        if "Table" in exp and "Data" in exp["Table"]:
            return exp["Table"]["Data"]
def field(s, n):
    for v in s.get("Value", []):
        if v.get("Name") == n: return v
    return None
def rowname_of(s, fn):
    f = field(s, fn)
    if not f: return None
    for v in f.get("Value", []):
        if v.get("Name") == "RowName": return v.get("Value")
def intvec(s, fn):
    f = field(s, fn)
    if not f: return None
    val = f.get("Value", [])
    if not val: return None
    iv = val[0].get("Value", {})
    return (iv.get("X"), iv.get("Y"), iv.get("Z"))
def set_intvec_xy(s, fn, x, y):
    f = field(s, fn)
    iv = f["Value"][0]["Value"]
    iv["X"] = x; iv["Y"] = y
def get_str(s, fn):
    f = field(s, fn); return f.get("Value") if f else None
def chapter_prefix(rn):
    if not rn: return None
    m = CHAP_PREFIX_RE.match(rn)
    return int(m.group(1)) if m else None

def pack(clusters, padding):
    """Try to pack clusters [(pos, sz, members)] sorted largest-first.
    Returns dict cluster_idx -> (new_x, new_y) or None if overflow.
    """
    placements = {}
    cursor_x = START_X
    cursor_y = START_Y
    row_max_y = 0
    for idx, (pos, sz, members) in enumerate(clusters):
        sx, sy = sz[0], sz[1]
        # Wrap if won't fit horizontally with padding gap after
        if cursor_x + sx + padding >= WORLD:
            cursor_x = START_X
            cursor_y += row_max_y + padding
            row_max_y = 0
        # Check Y fits
        if cursor_y + sy > WORLD - 1:  # zone goes 0..29 inclusive
            return None  # overflow
        placements[idx] = (cursor_x, cursor_y)
        cursor_x += sx + padding
        if sy > row_max_y: row_max_y = sy
    return placements

def main():
    if not os.path.exists(BACKUP):
        shutil.copy(ZP, BACKUP)
        print(f"backup -> {BACKUP}")
    else:
        print(f"backup already exists -> {BACKUP}")

    zones = load(ZP); chapters = load(CP)
    zrows = get_data(zones); crows = get_data(chapters)

    chap_primez = {}
    for r in crows:
        nm = r.get("Name")
        pz = field(r, "PrimeZ")
        chap_primez[nm] = pz.get("Value") if pz else None

    # Collect zones per floor prefix
    zones_by_floor = defaultdict(list)  # prefix -> list of (rowname, row_obj, pos, sz)
    for r in zrows:
        nm = r.get("Name", "")
        if not nm.startswith("Sandbox_Small_") or nm.startswith("Sandbox_Small_Elevator_"): continue
        en = get_str(r, "EnabledState")
        if en and "Live" not in en: continue
        chap = rowname_of(r, "Chapter")
        prefix = chapter_prefix(chap)
        if prefix not in FLOOR_FOR_PREFIX: continue
        pos = intvec(r, "Position"); sz = intvec(r, "TargetSize")
        zones_by_floor[prefix].append((nm, r, pos, sz))

    overall_changes = []
    floor_results = {}

    for prefix in FLOORS_ORDERED:
        flr = FLOOR_FOR_PREFIX[prefix]
        primez = chap_primez.get(flr)
        zlist = zones_by_floor[prefix]
        print(f"\n=== Chapter{prefix:02d} -> {flr} (PrimeZ={primez}) zones={len(zlist)} ===")
        if not zlist:
            floor_results[prefix] = {"padding": None, "placed": 0, "overflow": False}
            continue
        # Build clusters
        clusters_map = defaultdict(list)
        for (nm, row, pos, sz) in zlist:
            clusters_map[(pos, sz)].append((nm, row))
        # List of (pos, sz, members[])
        cluster_list = [(k[0], k[1], v) for k, v in clusters_map.items()]
        # Sort by max(sx, sy) descending
        cluster_list.sort(key=lambda c: max(c[1][0], c[1][1]), reverse=True)

        # Try padding 3 -> 2 -> 1
        chosen = None; placements = None
        for pad in (3, 2, 1):
            placements = pack(cluster_list, pad)
            if placements is not None:
                chosen = pad
                break
        if placements is None:
            print(f"  !! OVERFLOW even at PADDING=1; falling back to PADDING=1 with clipping (last row may go off-world)")
            chosen = 1
            placements = {}
            cursor_x = START_X; cursor_y = START_Y; row_max_y = 0
            for idx, (pos, sz, members) in enumerate(cluster_list):
                sx, sy = sz[0], sz[1]
                if cursor_x + sx + 1 >= WORLD:
                    cursor_x = START_X
                    cursor_y += row_max_y + 1
                    row_max_y = 0
                placements[idx] = (cursor_x, cursor_y)
                cursor_x += sx + 1
                if sy > row_max_y: row_max_y = sy
            floor_results[prefix] = {"padding": chosen, "placed": len(placements), "overflow": True}
        else:
            floor_results[prefix] = {"padding": chosen, "placed": len(placements), "overflow": False}

        print(f"  PADDING used = {chosen}")
        # Apply placements (propagate to all members of each cluster)
        for idx, (pos, sz, members) in enumerate(cluster_list):
            nx, ny = placements[idx]
            for (nm, row) in members:
                old_pos = intvec(row, "Position")
                set_intvec_xy(row, "Position", nx, ny)
                # Z stays at primez (it should already)
                # but enforce: leave Z untouched per spec
                new_pos = intvec(row, "Position")
                print(f"    {nm:50s}  {old_pos} -> {new_pos}  Sz={sz}")
                overall_changes.append((nm, old_pos, new_pos))

    save(ZP, zones)
    print(f"\nSaved -> {ZP}")
    print(f"Total zones repositioned: {len(overall_changes)}")
    print("\n=== Per-floor result ===")
    for prefix in FLOORS_ORDERED:
        r = floor_results[prefix]
        print(f"  Chapter{prefix:02d}: padding={r['padding']}  placed={r['placed']}  overflow={r['overflow']}")

if __name__ == "__main__":
    main()
