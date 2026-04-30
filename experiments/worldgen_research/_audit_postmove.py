"""Comprehensive post-move audit. INVESTIGATION ONLY."""
import json, os, sys
from collections import defaultdict, Counter

ROOT = os.path.dirname(os.path.abspath(__file__))
PRIOR = os.path.join(ROOT, "backups", "14-floor chain + ChapterID renumber")

def load(p):
    with open(p, "r", encoding="utf-8") as f:
        return json.load(f)

def rows(dt):
    # UAssetGUI table data lives under Exports[1].Table.Data or Data
    for ex in dt.get("Exports", []):
        tbl = ex.get("Table") or ex.get("Data") or {}
        data = tbl.get("Data") if isinstance(tbl, dict) else None
        if data is None and "Data" in ex:
            data = ex["Data"]
        if data:
            return data
    return []

def get_prop(row, name):
    """row is a dict with 'Value' list of property dicts."""
    if isinstance(row, dict):
        vals = row.get("Value") or row.get("Data") or []
    else:
        vals = row
    for p in vals:
        if isinstance(p, dict) and p.get("Name") == name:
            return p
    return None

def prop_val(row, name, default=None):
    p = get_prop(row, name)
    if p is None:
        return default
    return p.get("Value", default)

def row_name(row):
    return row.get("Name") if isinstance(row, dict) else None

def get_struct(row, name):
    p = get_prop(row, name)
    if p is None:
        return None
    return p.get("Value", [])

def get_int(row, name, default=0):
    v = prop_val(row, name, default)
    try:
        return int(v) if v is not None else default
    except Exception:
        return default

def get_bool(row, name, default=False):
    v = prop_val(row, name, default)
    return bool(v) if v is not None else default

def get_str(row, name, default=""):
    v = prop_val(row, name, default)
    return str(v) if v is not None else default

def unwrap_name(v):
    """Unwrap a NameProperty or struct-wrapped RowName into a plain string."""
    if v is None: return ""
    if isinstance(v, str): return v
    if isinstance(v, list):
        # list of property dicts (e.g. struct with RowName)
        for p in v:
            if isinstance(p, dict) and p.get("Name") == "RowName":
                return unwrap_name(p.get("Value"))
        # fallback: first element
        if v and isinstance(v[0], dict):
            return unwrap_name(v[0].get("Value", v[0]))
        return ""
    if isinstance(v, dict):
        return unwrap_name(v.get("Value"))
    return str(v)

def get_name(row, name, default=""):
    """Get a Name/RowName-wrapped property as plain string."""
    p = get_prop(row, name)
    if p is None: return default
    return unwrap_name(p.get("Value"))

def get_enum(row, name, default=""):
    """Get an enum string and strip 'EFoo::' prefix."""
    v = prop_val(row, name, default)
    s = str(v) if v is not None else default
    if "::" in s:
        s = s.split("::", 1)[1]
    return s

def is_live(row):
    """Row Live if EnabledState != Disabled (or absent)."""
    es = prop_val(row, "EnabledState", None)
    if es is None:
        return True
    s = str(es)
    return "Disabled" not in s and "Disable" not in s

def get_vec(struct_props, axis):
    """Given inner property list of a Vector struct, find axis."""
    if struct_props is None: return None
    for p in struct_props:
        if isinstance(p, dict) and p.get("Name") == axis:
            return p.get("Value")
    return None

def get_struct_props(row, name):
    p = get_prop(row, name)
    if p is None: return None
    return p.get("Value", [])

# ---- Load current ----
zones_dt = load(os.path.join(ROOT, "DT_Moria_Zones.json"))
chap_dt = load(os.path.join(ROOT, "DT_Moria_Chapters.json"))
lm_dt = load(os.path.join(ROOT, "DT_Moria_Landmarks.json"))
lc_dt = load(os.path.join(ROOT, "DT_Moria_LayoutConnections.json"))

zones = rows(zones_dt)
chaps = rows(chap_dt)
lms = rows(lm_dt)
lcs = rows(lc_dt)

print(f"Loaded: zones={len(zones)} chapters={len(chaps)} landmarks={len(lms)} connections={len(lcs)}")

# ---- Helpers for ZoneSet / SS filter ----
def zone_zoneset(z):
    return get_enum(z, "ZoneSet", "")

def zone_chapter(z):
    return get_name(z, "Chapter", "")

def zone_addchaps(z):
    p = get_prop(z, "AdditionalChapters")
    if p is None: return []
    v = p.get("Value", [])
    if not isinstance(v, list): return []
    out = []
    for item in v:
        # item is a struct with inner RowName, OR a NamePropertyData
        if isinstance(item, dict):
            iv = item.get("Value")
            out.append(unwrap_name(iv if iv is not None else item))
    return [x for x in out if x and x != "None"]

def get_intvec_axis(row, propname, axis):
    """For IntVector struct: outer struct -> Value[0] (IntVectorPropertyData) -> Value (FIntVector dict)."""
    p = get_prop(row, propname)
    if p is None: return None
    outer = p.get("Value", [])
    if not isinstance(outer, list) or not outer:
        return None
    inner = outer[0]
    if not isinstance(inner, dict): return None
    fv = inner.get("Value")
    if isinstance(fv, dict):
        return fv.get(axis)
    if isinstance(fv, list):
        # fall back: properties Value list with X/Y/Z
        for q in fv:
            if isinstance(q, dict) and q.get("Name") == axis:
                return q.get("Value")
    return None

def zone_targetsize_z(z):
    v = get_intvec_axis(z, "TargetSize", "Z")
    return int(v) if v is not None else 0

def zone_position_z(z):
    v = get_intvec_axis(z, "Position", "Z")
    return int(v) if v is not None else 0

def zone_pos_from_lm(z):
    return get_bool(z, "bPositionFromLandmarks", False)

def zone_lm_handles(z):
    """Returns list of (LandmarkRowName, bExtendedConnectivityLandmark) for the zone."""
    p = get_prop(z, "LandmarkHandles")
    if p is None: return []
    v = p.get("Value", [])
    out = []
    if not isinstance(v, list): return out
    for item in v:
        if not isinstance(item, dict): continue
        inner = item.get("Value", [])
        rn = None; ext = False
        for ip in inner:
            if not isinstance(ip, dict): continue
            n = ip.get("Name")
            if n == "Landmark":
                rn = unwrap_name(ip.get("Value"))
            elif n == "bExtendedConnectivityLandmark":
                ext = bool(ip.get("Value", False))
        out.append((rn, ext))
    return out

# Build maps
zones_by_name = {row_name(z): z for z in zones}
chaps_by_name = {row_name(c): c for c in chaps}
lms_by_name = {row_name(l): l for l in lms}
lcs_by_name = {row_name(c): c for c in lcs}

def chap_band(c):
    return (get_int(c, "MinZ"), get_int(c, "MaxZ"), get_int(c, "PrimeZ"))

def chap_layer(c):
    return get_int(c, "Layer")

def chap_id(c):
    return get_int(c, "ChapterID")

def chap_lv(c):
    # Friendly label - try ChapterName or Name field
    return get_str(c, "ChapterName", "") or get_str(c, "Lv", "")

def chap_zoneset(c):
    return get_enum(c, "ZoneSet", "")

# Filter Live SandboxSmall
live_ss_zones = [z for z in zones if is_live(z) and zone_zoneset(z) == "SandboxSmall"]
live_ss_chaps = [c for c in chaps if is_live(c) and chap_zoneset(c) == "SandboxSmall"]
live_ss_lcs = [c for c in lcs if is_live(c) and get_enum(c, "ZoneSet", "") == "SandboxSmall"]

print(f"\nLive SS: zones={len(live_ss_zones)} chapters={len(live_ss_chaps)} connections={len(live_ss_lcs)}")

# ============ SECTION 1: Per-chapter zone occupancy ============
print("\n" + "="*78)
print("SECTION 1: PER-CHAPTER ZONE OCCUPANCY")
print("="*78)

zones_by_chap = defaultdict(list)
for z in live_ss_zones:
    zones_by_chap[zone_chapter(z)].append(row_name(z))

# Identify stair zones (per spec)
def is_stair_zone(z):
    sz = zone_targetsize_z(z)
    if sz < 2: return False
    for (lm, ext) in zone_lm_handles(z):
        if ext: return True
    return False

stair_zones = {row_name(z) for z in live_ss_zones if is_stair_zone(z)}

print(f"{'Chapter':40} {'Lv':6} {'Lay':4} {'CID':4} {'Z-band':10} {'Prm':4} {'Cnt':4}  Zones")
empty_chaps = []
stair_only_chaps = []
for c in sorted(live_ss_chaps, key=lambda x: -chap_layer(x)):
    cn = row_name(c)
    mn, mx, pr = chap_band(c)
    cid = chap_id(c); lay = chap_layer(c)
    znames = zones_by_chap.get(cn, [])
    cnt = len(znames)
    band = f"{mn}..{mx}"
    print(f"{cn:40} {chap_lv(c):6} {lay:4} {cid:4} {band:10} {pr:4} {cnt:4}  {', '.join(znames)}")
    if cnt == 0:
        empty_chaps.append(cn)
    else:
        stair_in = [n for n in znames if n in stair_zones]
        if cnt == 1 and stair_in:
            stair_only_chaps.append(cn)

print(f"\nEMPTY chapters ({len(empty_chaps)}): {empty_chaps}")
print(f"STAIR-ONLY chapters ({len(stair_only_chaps)}): {stair_only_chaps}")

# ============ SECTION 3: Chain connection integrity ============
print("\n" + "="*78)
print("SECTION 3: CHAIN CONNECTION INTEGRITY (9 bRequired chain rows)")
print("="*78)

CHAIN_ROWS = [
    "Sandbox_Small_Chain_TopElToLv3Lv4",
    "Sandbox_Small_Chain_Lv3Lv4ToUpperEl",
    "Sandbox_Small_Chain_UpperElToD1Lv1",
    "Sandbox_Small_Chain_D1Lv1ToDeepUpper",
    "Sandbox_Small_Chain_DeepUpperToDeepMid",
    "Sandbox_Small_Chain_DeepMidToD4D3",
    "Sandbox_Small_Chain_D4D3ToDeepBottom",
    "Sandbox_Small_Chain_DeepBottomToCD",
    "Sandbox_Small_Chain_CDToD7D6",
]

def lc_endpoints(lc):
    return {
        "OriginZone": get_name(lc, "OriginZone"),
        "DestinationZone": get_name(lc, "DestinationZone"),
        "OriginLandmark": get_name(lc, "OriginLandmark"),
        "DestinationLandmark": get_name(lc, "DestinationLandmark"),
        "ZoneSet": get_enum(lc, "ZoneSet"),
        "bRequired": get_bool(lc, "bRequired"),
        "Live": is_live(lc),
    }

chain_problems = []
for rn in CHAIN_ROWS:
    lc = lcs_by_name.get(rn)
    if lc is None:
        chain_problems.append(f"  MISSING: {rn}")
        print(f"  MISSING ROW: {rn}")
        continue
    e = lc_endpoints(lc)
    issues = []
    if not e["Live"]: issues.append("NOT LIVE")
    if not e["bRequired"]: issues.append("bRequired=false")
    if e["ZoneSet"] != "SandboxSmall": issues.append(f"ZoneSet={e['ZoneSet']}")
    oz = zones_by_name.get(e["OriginZone"])
    dz = zones_by_name.get(e["DestinationZone"])
    ol = lms_by_name.get(e["OriginLandmark"])
    dl = lms_by_name.get(e["DestinationLandmark"])
    if oz is None: issues.append(f"OriginZone missing: {e['OriginZone']}")
    elif not is_live(oz): issues.append(f"OriginZone disabled: {e['OriginZone']}")
    if dz is None: issues.append(f"DestZone missing: {e['DestinationZone']}")
    elif not is_live(dz): issues.append(f"DestZone disabled: {e['DestinationZone']}")
    if ol is None: issues.append(f"OriginLM missing: {e['OriginLandmark']}")
    elif not is_live(ol): issues.append(f"OriginLM disabled: {e['OriginLandmark']}")
    if dl is None: issues.append(f"DestLM missing: {e['DestinationLandmark']}")
    elif not is_live(dl): issues.append(f"DestLM disabled: {e['DestinationLandmark']}")
    oz_ch = zone_chapter(oz) if oz else "?"
    dz_ch = zone_chapter(dz) if dz else "?"
    status = "OK" if not issues else "FAIL"
    print(f"  [{status}] {rn}")
    print(f"        OZ={e['OriginZone']} (chap={oz_ch})  DZ={e['DestinationZone']} (chap={dz_ch})")
    print(f"        OL={e['OriginLandmark']}  DL={e['DestinationLandmark']}")
    if issues:
        for i in issues: print(f"        !! {i}")
        chain_problems.append(rn)

print(f"\nChain problem rows: {len(chain_problems)}")

# ============ SECTION 4: Stair zone catalog ============
print("\n" + "="*78)
print("SECTION 4: STAIR ZONE CATALOG")
print("="*78)
stair_catalog = []
xy_seen = defaultdict(list)
chap_stair_count = defaultdict(int)
for z in live_ss_zones:
    if not is_stair_zone(z): continue
    name = row_name(z)
    chap = zone_chapter(z)
    chap_stair_count[chap] += 1
    addch = zone_addchaps(z)
    sz = zone_targetsize_z(z)
    bp_z = None; lm_x = None; lm_y = None; anchor_lm = None
    for (lmname, ext) in zone_lm_handles(z):
        lm = lms_by_name.get(lmname)
        if lm is None: continue
        x = get_intvec_axis(lm, "BasePosition", "X")
        y = get_intvec_axis(lm, "BasePosition", "Y")
        zz = get_intvec_axis(lm, "BasePosition", "Z")
        if anchor_lm is None:
            anchor_lm = lmname; bp_z = zz; lm_x = x; lm_y = y
        if ext:
            anchor_lm = lmname; bp_z = zz; lm_x = x; lm_y = y
            break
    stair_catalog.append((name, chap, bp_z, sz, addch, lm_x, lm_y, anchor_lm))
    if lm_x is not None and lm_y is not None:
        xy_seen[(lm_x, lm_y)].append(name)

print(f"{'Zone':45} {'Chapter':30} {'BP.Z':5} {'Sz':3} {'X':6} {'Y':6}  AddCh")
for n, c, z, sz, addch, x, y, lm in stair_catalog:
    print(f"{n:45} {c:30} {str(z):5} {sz:3} {str(x):6} {str(y):6}  {addch}")

print("\nValidation:")
multi = [(c,n) for c,n in chap_stair_count.items() if n > 1]
if multi:
    print(f"  FAIL chapter_stair_uniqueness: chapters with >1 stair: {multi}")
else:
    print(f"  OK chapter_stair_uniqueness")

xy_collide = [(k,v) for k,v in xy_seen.items() if len(v) > 1]
if xy_collide:
    print(f"  FAIL stair_xy_collision:")
    for (x,y), names in xy_collide:
        print(f"    ({x},{y}): {names}")
else:
    print(f"  OK stair_xy_collision")

zero_xy = [(name, lm) for (name, c, z, sz, addch, x, y, lm) in stair_catalog
           if (x == 0 and y == 0)]
print(f"  Zero-XY stair landmarks: {zero_xy}")

# ============ SECTION 5: All LayoutConnections sanity ============
print("\n" + "="*78)
print("SECTION 5: ALL LAYOUTCONNECTIONS SANITY (Live SS)")
print("="*78)

total = len(live_ss_lcs)
broken_zone = []
broken_lm = []
required_broken = []
empty_endpoints = []
for lc in live_ss_lcs:
    e = lc_endpoints(lc)
    rn = row_name(lc)
    bad = []
    has_empty = False
    for k in ("OriginZone","DestinationZone"):
        v = e[k]
        if not v or v == "None":
            has_empty = True
        else:
            z = zones_by_name.get(v)
            if z is None or not is_live(z):
                bad.append(f"{k}={v}")
                broken_zone.append((rn, k, v))
    for k in ("OriginLandmark","DestinationLandmark"):
        v = e[k]
        if not v or v == "None":
            has_empty = True
        else:
            l = lms_by_name.get(v)
            if l is None or not is_live(l):
                bad.append(f"{k}={v}")
                broken_lm.append((rn, k, v))
    if has_empty:
        empty_endpoints.append(rn)
    if bad and e["bRequired"]:
        required_broken.append((rn, bad))

print(f"  Total Live SS connections: {total}")
print(f"  Connections with broken zone refs: {len(broken_zone)}")
for r in broken_zone[:10]: print(f"     {r}")
print(f"  Connections with broken landmark refs: {len(broken_lm)}")
for r in broken_lm[:10]: print(f"     {r}")
print(f"  bRequired connections that may FAIL: {len(required_broken)}")
for r in required_broken[:10]: print(f"     {r}")
print(f"  Connections with empty/null endpoints (vanilla pattern): {len(empty_endpoints)}")

# ============ SECTION 6: Zone Position.Z coherence ============
print("\n" + "="*78)
print("SECTION 6: ZONE POSITION.Z COHERENCE WITH CHAPTER BAND")
print("="*78)

z_drift = []
for z in live_ss_zones:
    if zone_pos_from_lm(z): continue
    pz = zone_position_z(z)
    if pz == 0: continue
    chap = zones_by_name and zone_chapter(z)
    cobj = chaps_by_name.get(chap)
    if cobj is None: continue
    mn, mx, _ = chap_band(cobj)
    sz = zone_targetsize_z(z)
    top = pz + max(0, sz-1)
    if pz < mn - 5 or top > mx + 5:
        z_drift.append((row_name(z), chap, pz, top, mn, mx))

print(f"  Zones with Position.Z drifted >5 cells outside chapter band: {len(z_drift)}")
for r in z_drift:
    print(f"     {r[0]} chap={r[1]} posZ={r[2]} top={r[3]} band={r[4]}..{r[5]}")

# ============ SECTION 7: Landmark BasePosition.Z coherence ============
print("\n" + "="*78)
print("SECTION 7: LANDMARK BASEPOSITION.Z COHERENCE")
print("="*78)

# Build landmark -> host zone map (via LandmarkHandles)
lm_to_host = {}
for z in live_ss_zones:
    for (lmname, ext) in zone_lm_handles(z):
        if lmname:
            lm_to_host.setdefault(lmname, row_name(z))

drift_lms = []
for lm in lms:
    if not is_live(lm): continue
    name = row_name(lm)
    host = lm_to_host.get(name)
    if host is None: continue
    z = zones_by_name.get(host)
    if z is None: continue
    chap = zone_chapter(z)
    cobj = chaps_by_name.get(chap)
    if cobj is None: continue
    mn, mx, _ = chap_band(cobj)
    bz = get_intvec_axis(lm, "BasePosition", "Z")
    if bz is None: continue
    if bz < mn or bz > mx:
        # exception - if the host zone is a stair zone with TargetSize.Z>=2 and lm is its extended connectivity, allow span
        is_stair = host in stair_zones
        drift_lms.append((name, host, chap, bz, mn, mx, is_stair))

print(f"  Landmarks with BP.Z outside host chapter band: {len(drift_lms)}")
for r in drift_lms:
    print(f"     {r[0]} host={r[1]} chap={r[2]} BP.Z={r[3]} band={r[4]}..{r[5]} stair={r[6]}")

# ============ SECTION 8: Empty chapters watchlist ============
print("\n" + "="*78)
print("SECTION 8: EMPTY CHAPTERS WATCHLIST")
print("="*78)
print(f"  Currently EMPTY chapters: {empty_chaps}")
PRIOR_EMPTY = ["SandboxSmall-chapter-9","SandboxSmall-chapter-10","SandboxSmall-chapter-11"]
print(f"  Previously empty (chapters 9, 10, 11): {PRIOR_EMPTY}")
recovered = [c for c in PRIOR_EMPTY if c not in empty_chaps]
new_empty = [c for c in empty_chaps if c not in PRIOR_EMPTY]
print(f"  Recovered (now populated): {recovered}")
print(f"  Newly empty (regression risk): {new_empty}")

# ============ SECTION 9: Stair connectivity matrix ============
print("\n" + "="*78)
print("SECTION 9: STAIR CONNECTIVITY MATRIX (per chapter)")
print("="*78)
stair_reach = defaultdict(list)  # chapter -> list of stair zones reaching it
for (name, prim, bp_z, sz, addch, x, y, lm) in stair_catalog:
    stair_reach[prim].append(name)
    for ch in addch:
        if ch and ch != "None":
            stair_reach[ch].append(name)

# All Live SS chapter names sorted by Layer desc
ordered_chs = sorted(live_ss_chaps, key=lambda c: -chap_layer(c))
no_stair = []
for c in ordered_chs:
    cn = row_name(c)
    reach = stair_reach.get(cn, [])
    print(f"  {cn:40} (Lay={chap_layer(c):3}) stairs reaching: {reach}")
    if not reach:
        no_stair.append(cn)
print(f"\n  Chapters NOT reachable by any stair: {no_stair}")

# Adjacent floor pairs (by Layer)
print("\n  Adjacent-floor stair coverage:")
ordered_layers = sorted(ordered_chs, key=lambda c: chap_layer(c))
gaps = []
for i in range(len(ordered_layers)-1):
    a = ordered_layers[i]; b = ordered_layers[i+1]
    sa = set(stair_reach.get(row_name(a), []))
    sb = set(stair_reach.get(row_name(b), []))
    shared = sa & sb
    if not shared:
        gaps.append((row_name(a), row_name(b)))
    print(f"    {row_name(a)} <-> {row_name(b)}: shared={list(shared) or 'NONE'}")
print(f"\n  Gaps (no shared stair): {gaps}")

# ============ SECTION 10: Diff vs prior milestone ============
print("\n" + "="*78)
print("SECTION 10: DIFF vs '14-floor chain + ChapterID renumber'")
print("="*78)

p_zones = rows(load(os.path.join(PRIOR, "DT_Moria_Zones.json")))
p_chaps = rows(load(os.path.join(PRIOR, "DT_Moria_Chapters.json")))
p_lms = rows(load(os.path.join(PRIOR, "DT_Moria_Landmarks.json")))
p_lcs = rows(load(os.path.join(PRIOR, "DT_Moria_LayoutConnections.json")))

p_zbn = {row_name(z): z for z in p_zones}
p_lbn = {row_name(l): l for l in p_lms}
p_lcbn = {row_name(l): l for l in p_lcs}

# Chapter changes
chap_changes = []
cur_zone_chap = {row_name(z): zone_chapter(z) for z in zones if zone_zoneset(z) == "SandboxSmall"}
prior_zone_chap = {row_name(z): zone_chapter(z) for z in p_zones if zone_zoneset(z) == "SandboxSmall"}
for n in cur_zone_chap:
    if n in prior_zone_chap and cur_zone_chap[n] != prior_zone_chap[n]:
        chap_changes.append((n, prior_zone_chap[n], cur_zone_chap[n]))

print(f"  Zones whose primary Chapter changed: {len(chap_changes)}")
for c in chap_changes:
    print(f"    {c[0]}: {c[1]}  ->  {c[2]}")

# Position.Z changes
pos_changes = []
for n, z in zones_by_name.items():
    pz_now = zone_position_z(z)
    pz_old = zone_position_z(p_zbn[n]) if n in p_zbn else None
    if pz_old is not None and pz_now != pz_old:
        pos_changes.append((n, pz_old, pz_now))
print(f"  Zones with Position.Z changed: {len(pos_changes)}")
for c in pos_changes[:30]:
    print(f"    {c[0]}: {c[1]} -> {c[2]}")

# Landmark BP.Z changes
lm_changes = []
for n, l in lms_by_name.items():
    if n not in p_lbn: continue
    nz = get_intvec_axis(l, "BasePosition", "Z")
    oz = get_intvec_axis(p_lbn[n], "BasePosition", "Z")
    if nz is None or oz is None: continue
    if nz != oz:
        lm_changes.append((n, oz, nz))
print(f"  Landmarks with BasePosition.Z changed: {len(lm_changes)}")
for c in lm_changes[:30]:
    print(f"    {c[0]}: {c[1]} -> {c[2]}")

# New / removed / disabled rows
cur_zn = set(zones_by_name)
old_zn = set(p_zbn)
print(f"  New zone rows: {sorted(cur_zn - old_zn)}")
print(f"  Removed zone rows: {sorted(old_zn - cur_zn)}")

# Disabled state changes
state_flips = []
for n in cur_zn & old_zn:
    if is_live(zones_by_name[n]) != is_live(p_zbn[n]):
        state_flips.append((n, is_live(p_zbn[n]), is_live(zones_by_name[n])))
print(f"  Zone Live/Disabled state flips: {len(state_flips)}")
for s in state_flips: print(f"    {s}")

print("\n" + "="*78)
print("AUDIT COMPLETE")
print("="*78)
