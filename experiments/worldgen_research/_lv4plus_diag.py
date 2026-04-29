"""
_lv4plus_diag.py — Diagnostic for Lv-4..Lv-7 not generating in-game.

Tests 9 hypotheses, prints evidence for each, ranks results.
Read-only.
"""
import json, os, sys
from collections import defaultdict, Counter

ROOT = os.path.dirname(os.path.abspath(__file__))

def load(name):
    with open(os.path.join(ROOT, name), "r", encoding="utf-8") as f:
        return json.load(f)

def rows(dt):
    if isinstance(dt, dict) and "Exports" in dt:
        for ex in dt["Exports"]:
            if isinstance(ex, dict) and "Table" in ex:
                t = ex["Table"]
                if isinstance(t, dict) and "Data" in t:
                    return t["Data"]
    if isinstance(dt, dict) and "Data" in dt:
        return dt["Data"]
    return []

def row_name(r):
    return r.get("Name") or r.get("RowName") or ""

def get_struct(r):
    # Row often has a "Value" list of properties.
    return r.get("Value", r.get("Properties", []))

def prop(struct, name):
    if isinstance(struct, list):
        for p in struct:
            if isinstance(p, dict) and p.get("Name") == name:
                return p
    elif isinstance(struct, dict):
        return struct.get(name)
    return None

def pval(struct, name, default=None):
    p = prop(struct, name)
    if p is None: return default
    if isinstance(p, dict):
        if "Value" in p: return p["Value"]
        return p
    return p

def vec_to_xyz(v):
    if v is None: return None
    if isinstance(v, dict):
        if "Value" in v and isinstance(v["Value"], (list, dict)):
            v = v["Value"]
    if isinstance(v, list):
        # list of three FloatProperty/IntProperty entries OR named X/Y/Z
        out = {}
        for it in v:
            if isinstance(it, dict):
                n = it.get("Name")
                if n in ("X","Y","Z"):
                    out[n] = it.get("Value")
        if all(k in out for k in ("X","Y","Z")):
            return (out["X"], out["Y"], out["Z"])
    if isinstance(v, dict) and all(k in v for k in ("X","Y","Z")):
        return (v["X"], v["Y"], v["Z"])
    return None

def section(t):
    print("\n" + "="*78); print(t); print("="*78)

# --- Load datasets ---
chapters_cur   = rows(load("DT_Moria_Chapters.json"))
chapters_bcont = rows(load("DT_Moria_Chapters.before_continuous.json"))
chapters_brec  = rows(load("DT_Moria_Chapters.before_levelrow_recover.json"))
zones_cur      = rows(load("DT_Moria_Zones.json"))
zones_blv7     = rows(load("DT_Moria_Zones.before_lv7stair.json"))
zones_bcont    = rows(load("DT_Moria_Zones.before_continuous.json"))
landmarks_cur  = rows(load("DT_Moria_Landmarks.json"))
landmarks_blv7 = rows(load("DT_Moria_Landmarks.before_lv7stair.json"))

print(f"Loaded: chapters={len(chapters_cur)} zones={len(zones_cur)} landmarks={len(landmarks_cur)}")

# Index
def idx_by_name(rs):
    return {row_name(r): r for r in rs}

ch_cur = idx_by_name(chapters_cur)
ch_bcont = idx_by_name(chapters_bcont)
ch_brec = idx_by_name(chapters_brec)
zn_cur = idx_by_name(zones_cur)
zn_blv7 = idx_by_name(zones_blv7)
zn_bcont = idx_by_name(zones_bcont)
lm_cur = idx_by_name(landmarks_cur)
lm_blv7 = idx_by_name(landmarks_blv7)

# Helper to extract chapter fields
CHAPTER_FIELDS = ["ChapterID","Layer","MinZ","MaxZ","PrimeZ","EnemyScalingLevel","DisplayName"]

def chap_fields(r):
    s = get_struct(r)
    out = {}
    for f in CHAPTER_FIELDS:
        v = pval(s, f)
        # DisplayName may be FText struct with nested key
        if f == "DisplayName" and isinstance(v, (dict, list)):
            # try to extract a Key
            try:
                if isinstance(v, list):
                    for it in v:
                        if isinstance(it, dict) and it.get("Name") in ("Key","SourceString","TableId"):
                            out.setdefault("DisplayKey", []).append((it.get("Name"), it.get("Value")))
                elif isinstance(v, dict):
                    out["DisplayName_raw"] = str(v)[:120]
            except Exception:
                pass
            continue
        out[f] = v
    return out

# === H1: restored level rows vs anchored siblings ===
section("H1: Level rows vs anchored siblings (Lv-4..Lv-7)")
LEVEL_TARGETS = {
    "Chapter04": [4, "SandboxSmall-Chapter04.Level4",
                  ["Chapter04.DarkestDeeps_E","Chapter04.DestroyedCity_B","Chapter04.Suburban_D"]],
    "Chapter05": [5, "SandboxSmall-Chapter05.Level5",
                  ["Chapter05.City_B_Dwarrowdelf","Chapter05.Elevator_D","Chapter05.MusteringHalls","Chapter05.OrcTown_D_Redeye"]],
    "Chapter06": [6, "SandboxSmall-Chapter06.Level6",
                  ["Chapter06.DestroyedCity_E","Chapter06.OrcTown_C_Gundabad"]],
    "Chapter07": [7, "SandboxSmall-Chapter07.Level7",
                  ["Chapter07.DestroyedCity_A_Desolation"]],
}

def find_chapter_row(name_hint):
    # search ch_cur for row whose name contains hint
    for n, r in ch_cur.items():
        if name_hint in n:
            return n, r
    return None, None

h1_findings = []
for ch_key, (lvl_n, lvl_row_hint, anchored) in LEVEL_TARGETS.items():
    # Find the level row
    lvl_name, lvl_row = find_chapter_row(lvl_row_hint)
    if not lvl_row:
        # try without "SandboxSmall-" prefix
        for n, r in ch_cur.items():
            if n.endswith(f".Level{lvl_n}"):
                lvl_name, lvl_row = n, r; break
    if not lvl_row:
        h1_findings.append(f"  [!!!] Level row for Lv-{lvl_n} NOT FOUND in current Chapters")
        continue
    lf = chap_fields(lvl_row)
    print(f"\n  Lv-{lvl_n} level row: {lvl_name}")
    print(f"    fields: {lf}")
    for anc in anchored:
        anc_name, anc_row = find_chapter_row(anc)
        if not anc_row:
            h1_findings.append(f"  [MISSING anchored row] {anc}")
            print(f"    [MISSING] {anc}")
            continue
        af = chap_fields(anc_row)
        diffs = []
        for f in ("ChapterID","Layer","MinZ","MaxZ","PrimeZ","EnemyScalingLevel"):
            if lf.get(f) != af.get(f):
                diffs.append(f"{f}: lvl={lf.get(f)} vs anc={af.get(f)}")
        if diffs:
            h1_findings.append(f"  [MISMATCH] {anc_name} vs {lvl_name}: {diffs}")
            print(f"    [MISMATCH] {anc_name}: {diffs}")
        else:
            print(f"    [ok] {anc_name}")
print("\nH1 summary issues:", len(h1_findings))
for f in h1_findings: print(f)

# === Compare level rows: current vs before_continuous vs before_levelrow_recover ===
section("H1b: Level row diffs across snapshots")
for ch_key, (lvl_n, lvl_row_hint, _) in LEVEL_TARGETS.items():
    nm = None
    for n in ch_cur:
        if n.endswith(f".Level{lvl_n}"):
            nm = n; break
    if not nm: continue
    cur = chap_fields(ch_cur.get(nm, {}))
    bc = chap_fields(ch_bcont.get(nm, {})) if nm in ch_bcont else None
    br = chap_fields(ch_brec.get(nm, {})) if nm in ch_brec else None
    print(f"\n  Lv-{lvl_n} ({nm})")
    print(f"    current:           {cur}")
    print(f"    before_continuous: {bc}")
    print(f"    before_recover:    {br}")

# === H2: stair landmarks ===
section("H2: Stair landmarks (FourthStair/SixthStair/EighthStair/EleventhStair)")
target_stairs = ["FourthStair","SixthStair","EighthStair","EleventhStair","FirstStair","ThirdStair"]
for nm in lm_cur:
    for t in target_stairs:
        if t in nm:
            r = lm_cur[nm]
            s = get_struct(r)
            bp = pval(s, "BasePosition")
            bbn = pval(s, "BaseBubbleName")
            print(f"  {nm}: BaseBubble={bbn} BP={vec_to_xyz(bp)}")

# Find stair landmark refs in zones (Elevator_B, Elevator_D)
section("H2b: Elevator_B / Elevator_D LandmarkHandles")
for zname in list(zn_cur.keys()):
    if "Elevator_B" in zname or "Elevator_D" in zname or "Sandbox_Small_Elevator" in zname:
        if "Chapter" not in zname:  # skip chapter-row anchored zones
            continue
        r = zn_cur[zname]
        s = get_struct(r)
        pos = vec_to_xyz(pval(s, "Position"))
        sz = vec_to_xyz(pval(s, "TargetSize"))
        lhs = pval(s, "LandmarkHandles")
        print(f"\n  {zname}  Pos={pos}  Sz={sz}")
        if isinstance(lhs, list):
            for lh in lhs:
                # lh is a struct prop; get its Value
                val = lh.get("Value") if isinstance(lh, dict) else lh
                if isinstance(val, list):
                    inner = {}
                    for it in val:
                        if isinstance(it, dict):
                            inner[it.get("Name")] = it.get("Value")
                    bp = vec_to_xyz(inner.get("BasePosition"))
                    print(f"    LH: name={inner.get('LandmarkName') or inner.get('LandmarkHandle')} "
                          f"BP={bp} Placement={inner.get('Placement')} "
                          f"bExt={inner.get('bExtendedConnectivityLandmark')}")

# === H3: DisplayName key consistency ===
section("H3: DisplayName key consistency on anchored rows")
def disp_key(struct):
    p = prop(struct, "DisplayName")
    if p is None: return None
    val = p.get("Value") if isinstance(p, dict) else p
    if isinstance(val, list):
        for it in val:
            if isinstance(it, dict) and it.get("Name") == "Key":
                return it.get("Value")
    if isinstance(val, dict):
        return val.get("Key")
    return None

for ch_key, (lvl_n, _, anchored) in LEVEL_TARGETS.items():
    for nm in [n for n in ch_cur if n.endswith(f".Level{lvl_n}")] + \
              [n for n in ch_cur for a in anchored if a in n]:
        k = disp_key(get_struct(ch_cur[nm]))
        print(f"  {nm}: DisplayKey={k}")

# === H4: zone Pos/Size vs hosting chapter MinZ..MaxZ ===
section("H4: Zone Z-range vs hosting chapter Z-band")
# Build chapter row -> (MinZ,MaxZ) lookup
def get_minmax(r):
    s = get_struct(r)
    return pval(s, "MinZ"), pval(s, "MaxZ")

# Zones reference a chapter via... let's see. Check zone struct fields.
sample = zones_cur[0] if zones_cur else None
if sample:
    print(f"  zone sample fields: {[p.get('Name') for p in get_struct(sample) if isinstance(p, dict)][:20]}")

# Iterate zones; if zone name has 'ChapterNN.' prefix, that's the host
for zname, zr in zn_cur.items():
    m = None
    for ch_key, (lvl_n, _, _) in LEVEL_TARGETS.items():
        if zname.startswith(ch_key + "."):
            m = ch_key; break
    if not m: continue
    s = get_struct(zr)
    pos = vec_to_xyz(pval(s, "Position"))
    sz = vec_to_xyz(pval(s, "TargetSize"))
    if not pos or not sz: continue
    z0 = int(pos[2]); z1 = int(pos[2]+sz[2]-1)
    # The hosting chapter row IS this zone's row in chapters table (anchored)
    hostname = None
    for n in ch_cur:
        if n == zname or n.endswith("."+zname.split(".",1)[1]):
            hostname = n; break
    if hostname:
        mn, mx = get_minmax(ch_cur[hostname])
        ok = (mn is not None and mx is not None and z0 >= mn and z1 <= mx)
        flag = "" if ok else "  [OUT OF BAND]"
        print(f"  {zname}: zoneZ={z0}..{z1}  chapter[{hostname}] band={mn}..{mx}{flag}")
    else:
        print(f"  {zname}: zoneZ={z0}..{z1}  [NO chapter row found by name]")

# === H5: bExt=true at top of world (Z>=29) ===
section("H5: bExtendedConnectivityLandmark on Z>=29 cells")
for zname, zr in zn_cur.items():
    s = get_struct(zr)
    lhs = pval(s, "LandmarkHandles")
    if not isinstance(lhs, list): continue
    for lh in lhs:
        val = lh.get("Value") if isinstance(lh, dict) else lh
        if not isinstance(val, list): continue
        inner = {}
        for it in val:
            if isinstance(it, dict):
                inner[it.get("Name")] = it.get("Value")
        bp = vec_to_xyz(inner.get("BasePosition"))
        ext = inner.get("bExtendedConnectivityLandmark")
        if bp and bp[2] is not None and bp[2] >= 29 and ext:
            print(f"  [WARN] {zname}: LH BP.Z={bp[2]} bExt={ext} — top-of-world extension!")

# === H6: cross-chapter overlap on Lv-4..Lv-7 zones ===
section("H6: Zone overlaps in Lv-4..Lv-7")
def zbox(r):
    s = get_struct(r)
    p = vec_to_xyz(pval(s, "Position"))
    sz = vec_to_xyz(pval(s, "TargetSize"))
    if not p or not sz: return None
    return (int(p[0]),int(p[1]),int(p[2]),int(p[0]+sz[0]-1),int(p[1]+sz[1]-1),int(p[2]+sz[2]-1))

target_zones = [z for z in zn_cur if any(z.startswith(c+".") for c in LEVEL_TARGETS)]
all_other = [z for z in zn_cur if z not in target_zones]
def vol(b): return (b[3]-b[0]+1)*(b[4]-b[1]+1)*(b[5]-b[2]+1)
def inter(a,b):
    dx=max(0,min(a[3],b[3])-max(a[0],b[0])+1)
    dy=max(0,min(a[4],b[4])-max(a[1],b[1])+1)
    dz=max(0,min(a[5],b[5])-max(a[2],b[2])+1)
    return dx*dy*dz

for tz in target_zones:
    a = zbox(zn_cur[tz])
    if not a: continue
    for oz in all_other:
        b = zbox(zn_cur[oz])
        if not b: continue
        v = inter(a,b)
        if v <= 0: continue
        ov = v / min(vol(a), vol(b))
        if ov > 0.20:
            print(f"  {tz} vs {oz}: overlap={ov:.0%} ({v}/{min(vol(a),vol(b))})")

# === H8: chapter Z-band gap analysis ===
section("H8: Z-band coverage by LEVEL rows only")
level_rows = []
for n, r in ch_cur.items():
    if ".Level" in n or ".Deep" in n:
        f = chap_fields(r)
        if f.get("MinZ") is not None and f.get("MaxZ") is not None:
            level_rows.append((n, f))
level_rows.sort(key=lambda x: x[1].get("MinZ", 0))
covered = set()
for n, f in level_rows:
    for z in range(f["MinZ"], f["MaxZ"]+1):
        covered.add(z)
    print(f"  {n}: Z={f['MinZ']}..{f['MaxZ']} PrimeZ={f['PrimeZ']} CID={f['ChapterID']} Layer={f['Layer']}")
gaps = sorted(set(range(0,30)) - covered)
print(f"  Z-coverage gaps (0..29): {gaps}")

# === unique CID per layer check ===
section("Unique ChapterID & Layer per LEVEL row")
cid_counter = Counter()
layer_counter = Counter()
for n, f in level_rows:
    cid_counter[f.get("ChapterID")] += 1
    layer_counter[f.get("Layer")] += 1
print("  CID counts:", dict(cid_counter))
print("  Layer counts:", dict(layer_counter))
dups_cid = [k for k,v in cid_counter.items() if v>1]
dups_lay = [k for k,v in layer_counter.items() if v>1]
if dups_cid: print(f"  [!!!] duplicate CIDs across level rows: {dups_cid}")
if dups_lay: print(f"  [!!!] duplicate Layers across level rows: {dups_lay}")

# === H9: diff vs before_continuous on Lv-4..Lv-7 anchored rows ===
section("H9: Anchored-zone Position/Size diffs vs before_lv7stair")
for zname in target_zones:
    if zname in zn_blv7:
        a = zbox(zn_cur[zname]); b = zbox(zn_blv7[zname])
        if a != b:
            print(f"  {zname}: cur={a}  before_lv7stair={b}")
    else:
        print(f"  {zname}: not in before_lv7stair (NEW since)")

print("\n=== DONE ===")
