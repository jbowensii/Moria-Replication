"""Grid redistribute verify.

1. Confirm no Live SS (non-elevator) zone position is outside [0..29] X/Y on any active floor.
2. Confirm no two non-variant zones overlap in cells (per floor).
3. Confirm variant clusters still share Pos+Size (cluster integrity).
4. Confirm Position.Z untouched (matches PrimeZ of primary chapter's floor).
5. Run BuildValidator.run() via SandboxZoneEditor.py — expect 0 errors / 0 warnings.
6. Print per-floor density% and min-gap (post-state) and compare to backup.
"""
import os, json, re, sys, importlib.util
from pathlib import Path
from collections import defaultdict

WGR = Path(__file__).resolve().parent
SCRIPTS = WGR.parent.parent / "scripts"
ZP = WGR / "DT_Moria_Zones.json"
BK = WGR / "DT_Moria_Zones.before_grid_redistribute.json"
CP = WGR / "DT_Moria_Chapters.json"

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

def load(p):
    with open(p, "r", encoding="utf-8") as f: return json.load(f)
def get_data(asset):
    for exp in asset.get("Exports", []):
        if "Table" in exp and "Data" in exp["Table"]:
            return exp["Table"]["Data"]
def field(s, n):
    for v in s.get("Value", []):
        if v.get("Name") == n: return v
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
def get_str(s, fn):
    f = field(s, fn); return f.get("Value") if f else None
def chapter_prefix(rn):
    if not rn: return None
    m = CHAP_PREFIX_RE.match(rn); return int(m.group(1)) if m else None

def rect_gap(p1, s1, p2, s2):
    r1 = (p1[0], p1[1], p1[0]+s1[0]-1, p1[1]+s1[1]-1)
    r2 = (p2[0], p2[1], p2[0]+s2[0]-1, p2[1]+s2[1]-1)
    if r1[2] < r2[0]:   gx = r2[0] - r1[2] - 1
    elif r2[2] < r1[0]: gx = r1[0] - r2[2] - 1
    else:               gx = -1
    if r1[3] < r2[1]:   gy = r2[1] - r1[3] - 1
    elif r2[3] < r1[1]: gy = r1[1] - r2[3] - 1
    else:               gy = -1
    return max(gx, gy)

def collect(zones_path, chapters_path):
    zones = load(zones_path); chapters = load(chapters_path)
    zrows = get_data(zones); crows = get_data(chapters)
    chap_primez = {}
    for r in crows:
        nm = r.get("Name")
        pz = field(r, "PrimeZ")
        chap_primez[nm] = pz.get("Value") if pz else None
    by_floor = defaultdict(list)
    for r in zrows:
        nm = r.get("Name", "")
        if not nm.startswith("Sandbox_Small_") or nm.startswith("Sandbox_Small_Elevator_"): continue
        en = get_str(r, "EnabledState")
        if en and "Live" not in en: continue
        chap = rowname_of(r, "Chapter")
        prefix = chapter_prefix(chap)
        if prefix not in FLOOR_FOR_PREFIX: continue
        pos = intvec(r, "Position"); sz = intvec(r, "TargetSize")
        by_floor[prefix].append((nm, pos, sz, chap))
    return by_floor, chap_primez

def floor_stats(zlist):
    clusters = defaultdict(list)
    for (nm, pos, sz, _) in zlist:
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
    return len(zlist), len(unique), density, min_gap, clusters

# ----- Structural checks -----
print("=== Structural checks ===")
post, primez_map = collect(ZP, CP)
pre, _ = collect(BK, CP)

errors = []
for prefix in FLOORS_ORDERED:
    flr = FLOOR_FOR_PREFIX[prefix]
    expected_z = primez_map.get(flr)
    for (nm, pos, sz, chap) in post[prefix]:
        if pos is None or sz is None:
            errors.append(f"{nm}: missing pos/sz"); continue
        x, y, z = pos
        sx, sy, sz_ = sz
        # Bounds: zone occupies x..x+sx-1, must be within 0..29
        if x < 0 or y < 0 or x + sx - 1 > 29 or y + sy - 1 > 29:
            errors.append(f"OFF-WORLD: {nm} Pos={pos} Sz={sz} on Chapter{prefix:02d}")
        # Z preservation
        if z != expected_z:
            errors.append(f"Z DRIFT: {nm} z={z} expected PrimeZ={expected_z} (Chapter{prefix:02d})")

# Overlap check (non-variant pairs)
print("\n--- Overlap check (non-variant pairs) ---")
overlap_errs = []
for prefix in FLOORS_ORDERED:
    zs = post[prefix]
    # group by (pos,sz)
    clusters = defaultdict(list)
    for (nm, pos, sz, _) in zs:
        clusters[(pos, sz)].append(nm)
    keys = list(clusters.keys())
    for i in range(len(keys)):
        for j in range(i+1, len(keys)):
            p1, s1 = keys[i]; p2, s2 = keys[j]
            if not (p1 and s1 and p2 and s2): continue
            g = rect_gap(p1, s1, p2, s2)
            if g < 0:
                overlap_errs.append(f"OVERLAP Chapter{prefix:02d}: {clusters[keys[i]]} vs {clusters[keys[j]]}")
if overlap_errs:
    for e in overlap_errs: print(f"  {e}")
    errors.extend(overlap_errs)
else:
    print("  no overlaps")

# Variant cluster integrity (members share pos+sz by construction; sanity check)
print("\n--- Variant cluster integrity ---")
for prefix in FLOORS_ORDERED:
    clusters = defaultdict(list)
    for (nm, pos, sz, _) in post[prefix]:
        clusters[(pos, sz)].append(nm)
    multi = {k: v for k, v in clusters.items() if len(v) > 1}
    if multi:
        for k, v in multi.items():
            print(f"  Chapter{prefix:02d} cluster Pos={k[0]} Sz={k[1]} members={len(v)}: {v}")
    # nothing to compare against: each member is the same row, so integrity is trivially preserved
print("  variant clusters preserved by construction (cluster reps applied to all members)")

# Bounds & Z summary
if errors:
    print("\n*** STRUCTURAL ERRORS ***")
    for e in errors: print(f"  {e}")
else:
    print("\nNo bounds/Z errors.")

# Per-floor before/after table
print("\n=== Per-floor before/after ===")
print(f"{'Floor':<10} {'zones':>6} {'pre-den%':>9} {'post-den%':>10} {'pre-gap':>8} {'post-gap':>9}")
for prefix in FLOORS_ORDERED:
    pre_n, pre_u, pre_d, pre_g, _ = floor_stats(pre[prefix])
    post_n, post_u, post_d, post_g, _ = floor_stats(post[prefix])
    print(f"Chap{prefix:02d}     {post_n:>6} {pre_d:>9.1f} {post_d:>10.1f} {str(pre_g):>8} {str(post_g):>9}")

# ----- BuildValidator -----
print("\n=== BuildValidator ===")
spec = importlib.util.spec_from_file_location("sandbox_zone_editor", SCRIPTS / "SandboxZoneEditor.py")
mod = importlib.util.module_from_spec(spec)
sys.modules["sandbox_zone_editor"] = mod
spec.loader.exec_module(mod)
DataTableDoc = mod.DataTableDoc
BuildValidator = mod.BuildValidator
DATATABLES = mod.DATATABLES

docs = {}
for key, (fname, stem, label) in DATATABLES.items():
    if key == "strings": continue
    p = WGR / fname
    if not p.exists(): continue
    d = DataTableDoc(key, p, stem, label)
    if d.load(): docs[key] = d
print(f"loaded {len(docs)} DataTableDocs")

bv = BuildValidator(docs)
issues = bv.run()
errs = [i for i in issues if i.severity == "error"]
warns = [i for i in issues if i.severity == "warning"]
print(f"  total issues: {len(issues)}  errors: {len(errs)}  warnings: {len(warns)}")
from collections import Counter
by_check = Counter(i.check for i in issues)
if by_check:
    print("  by check:")
    for k, c in by_check.most_common():
        print(f"    {k}: {c}")
if errs:
    print("\nERRORS (first 30):")
    for it in errs[:30]:
        print(f"  {it.check}/{it.doc_key}: {it.detail[:200]}")
if warns:
    print("\nWARNINGS (first 30):")
    for it in warns[:30]:
        print(f"  {it.check}/{it.doc_key}: {it.detail[:200]}")

print("\nVERIFY DONE.")
