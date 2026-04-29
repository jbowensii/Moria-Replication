"""Apply gap-fix:
  Change 1: Repoint EleventhStair (Lv-7<->Lv-6) -> Lv-2<->Lv-3
  Change 2: Add new FifthStair zone D-4<->D-3 UP. Landmark already exists; reposition+rebrand.

Safety: backups to *.before_gap_fix.json (copy only if missing).
"""
import json, os, copy, shutil

BASE = os.path.dirname(os.path.abspath(__file__))
ZP = os.path.join(BASE, "DT_Moria_Zones.json")
LP = os.path.join(BASE, "DT_Moria_Landmarks.json")
WP = os.path.join(BASE, "World.json")

def load(p):
    with open(p, "r", encoding="utf-8") as f: return json.load(f)
def save(p, d):
    with open(p, "w", encoding="utf-8") as f: json.dump(d, f, indent=2)
def get_data(asset):
    for exp in asset.get("Exports", []):
        if "Table" in exp and "Data" in exp["Table"]:
            return exp["Table"]["Data"]
    raise RuntimeError("no DT")
def find_row(rows, k):
    for r in rows:
        if r.get("Name") == k: return r
    return None
def field(struct, name):
    for v in struct.get("Value", []):
        if v.get("Name") == name: return v
    return None
def set_rowname(struct, fname, val):
    f = field(struct, fname)
    for v in f.get("Value", []):
        if v.get("Name") == "RowName":
            v["Value"] = val
            return
    raise RuntimeError(f"no RowName in {fname}")

# Backups
for p in (ZP, LP, WP):
    bk = p.replace(".json", ".before_gap_fix.json")
    if not os.path.exists(bk):
        shutil.copy(p, bk)
        print("backup ->", bk)
    else:
        print("backup exists ->", bk)

zones = load(ZP); lms = load(LP); world = load(WP)
zrows = get_data(zones); lrows = get_data(lms)

# === CHANGE 1: Repoint EleventhStair zone + landmark ===
print("\n=== CHANGE 1: Eleventh stair Lv-7/Lv-6 -> Lv-2/Lv-3 ===")
elv = find_row(zrows, "Sandbox_Small_Elevator_EleventhStair")
assert elv, "EleventhStair zone missing"
# Chapter -> Level2
old_chap = []
chap_f = field(elv, "Chapter")
for v in chap_f["Value"]:
    if v.get("Name") == "RowName":
        old_chap.append(v["Value"]); v["Value"] = "SandboxSmall-Chapter02.Level2"
addl_f = field(elv, "AdditionalChapters")
old_addl = []
for ent in addl_f["Value"]:
    for v in ent.get("Value", []):
        if v.get("Name") == "RowName":
            old_addl.append(v["Value"]); v["Value"] = "SandboxSmall-Chapter03.Level3"
print(f"  zone Chapter: {old_chap} -> SandboxSmall-Chapter02.Level2")
print(f"  zone AdditionalChapters: {old_addl} -> ['SandboxSmall-Chapter03.Level3']")

# Verify ext flag remains True on the LandmarkHandle pointing at EleventhStair
lh_f = field(elv, "LandmarkHandles")
for ent in lh_f["Value"]:
    lm_f = field(ent, "Landmark")
    rn = None
    for v in lm_f.get("Value", []):
        if v.get("Name") == "RowName":
            rn = v.get("Value")
    if rn == "Sandbox.EleventhStair":
        ext_f = field(ent, "bExtendedConnectivityLandmark")
        if ext_f is None:
            print("  WARN: no bExtendedConnectivityLandmark field on LH; leaving as is")
        else:
            print(f"  zone LH bExtendedConnectivityLandmark current = {ext_f.get('Value')} (keep True)")
            ext_f["Value"] = True

# Landmark BasePosition (12,21,20)
elm = find_row(lrows, "Sandbox.EleventhStair")
assert elm, "EleventhStair landmark missing"
bp = field(elm, "BasePosition")["Value"][0]["Value"]
old_bp = (bp["X"], bp["Y"], bp["Z"])
bp["X"], bp["Y"], bp["Z"] = 12, 21, 20
print(f"  landmark BasePosition: {old_bp} -> (12, 21, 20)")

# === CHANGE 2: FifthStair landmark fixup + new zone ===
print("\n=== CHANGE 2: FifthStair landmark + new zone for D-4 <-> D-3 ===")
flm = find_row(lrows, "Sandbox.FifthStair")
assert flm, "Sandbox.FifthStair landmark missing (audit said it exists)"
# Reposition + rebrand
bp = field(flm, "BasePosition")["Value"][0]["Value"]
old_bp = (bp["X"], bp["Y"], bp["Z"])
bp["X"], bp["Y"], bp["Z"] = 8, 4, 8
print(f"  landmark BasePosition: {old_bp} -> (8, 4, 8)")

bb = field(flm, "BaseBubbleName")
old_bb = bb.get("Value")
bb["Value"] = "BB_Sandbox_Elevator_Urban"
print(f"  landmark BaseBubbleName: {old_bb!r} -> 'BB_Sandbox_Elevator_Urban'")

# Other required overrides per spec (most are likely already correct - set explicitly)
field(flm, "Placement")["Value"] = "ELandmarkPlacement::Fixed"
en_f = field(flm, "EnabledState")
if en_f: en_f["Value"] = "ERowEnabledState::Live"
ps_f = field(flm, "bPlayerStartLocation")
if ps_f: ps_f["Value"] = False
cr_f = field(flm, "ChallengeRating")
if cr_f: cr_f["Value"] = 0
gc_f = field(flm, "GuaranteedConnections")
if gc_f: gc_f["Value"] = []
# DisplayName key & InternalId TagName
dn_f = field(flm, "DisplayName")
if dn_f and "Value" in dn_f and isinstance(dn_f.get("Value"), str):
    dn_f["Value"] = "Landmarks.Sandbox.FifthStair"
iid_f = field(flm, "InternalId")
if iid_f:
    for v in iid_f["Value"]:
        if v.get("Name") == "TagName":
            v["Value"] = "World.Landmark.Sandbox.FifthStair"

# Build the new zone by cloning Sandbox_Small_Elevator_FirstStair (simplest)
fs_zone = find_row(zrows, "Sandbox_Small_Elevator_FifthStair")
if fs_zone:
    print("  zone Sandbox_Small_Elevator_FifthStair already exists; updating fields in place")
    new_zone = fs_zone
else:
    template = find_row(zrows, "Sandbox_Small_Elevator_FirstStair")
    assert template, "FirstStair zone template missing"
    new_zone = copy.deepcopy(template)
    new_zone["Name"] = "Sandbox_Small_Elevator_FifthStair"
    zrows.append(new_zone)
    print("  zone cloned from FirstStair -> Sandbox_Small_Elevator_FifthStair")

# Set Chapter=Deep4, AdditionalChapters=[Deep3]
set_rowname(new_zone, "Chapter", "SandboxSmall-Chapter11.Deep4")
addl_f = field(new_zone, "AdditionalChapters")
# Keep array length 1; rewrite first entry's RowName
if not addl_f["Value"]:
    # add a single struct copying shape - shouldn't happen since FirstStair has one
    raise RuntimeError("template AdditionalChapters empty; aborting")
# Rewrite all entries (FirstStair has one)
for i, ent in enumerate(addl_f["Value"]):
    for v in ent.get("Value", []):
        if v.get("Name") == "RowName":
            v["Value"] = "SandboxSmall-Chapter12.Deep3"
# Trim to one entry to be safe
addl_f["Value"] = addl_f["Value"][:1]

# LandmarkHandles -> point first entry to Sandbox.FifthStair, ext=True, Placement=Fixed
lh_f = field(new_zone, "LandmarkHandles")
# Reduce to first entry
if not lh_f["Value"]:
    raise RuntimeError("template LH empty")
lh_f["Value"] = lh_f["Value"][:1]
ent = lh_f["Value"][0]
lm = field(ent, "Landmark")
for v in lm["Value"]:
    if v.get("Name") == "RowName":
        v["Value"] = "Sandbox.FifthStair"
for v in ent.get("Value", []):
    if v.get("Name") == "Placement":
        v["Value"] = "EZoneBubblePlacement::Fixed"
    if v.get("Name") == "bExtendedConnectivityLandmark":
        v["Value"] = True

# EnabledState=Live
en_f = field(new_zone, "EnabledState")
if en_f: en_f["Value"] = "ERowEnabledState::Live"

print("  new_zone Chapter=Deep4, Addl=[Deep3], LH->Sandbox.FifthStair (ext=True, Fixed)")

# === NameMap synchronization ===
print("\n=== NameMap sync ===")
def ensure(asset, tok, label):
    nm = asset.setdefault("NameMap", [])
    if tok not in nm:
        nm.append(tok)
        print(f"  {label}: added {tok!r}")
        return True
    print(f"  {label}: {tok!r} already present")
    return False

# Zones: needs Sandbox_Small_Elevator_FifthStair, Sandbox.FifthStair
ensure(zones, "Sandbox_Small_Elevator_FifthStair", "Zones")
ensure(zones, "Sandbox.FifthStair", "Zones")
# Landmarks: needs FifthStair tokens (audit shows already present, double check)
ensure(lms, "Sandbox.FifthStair", "Landmarks")
ensure(lms, "Landmarks.Sandbox.FifthStair", "Landmarks")
ensure(lms, "World.Landmark.Sandbox.FifthStair", "Landmarks")
# World StringTable already has the entry; NameMap has key. No change needed.

def sync_counts(asset, label):
    nm_len = len(asset.get("NameMap", []))
    cur_nref = asset.get("NamesReferencedFromExportDataCount", 0)
    asset["NamesReferencedFromExportDataCount"] = max(cur_nref, nm_len)
    gens = asset.get("Generations", [])
    if gens:
        gens[0]["NameCount"] = max(gens[0].get("NameCount", 0), nm_len)
    print(f"  {label}: NameMap={nm_len} NRefED={asset['NamesReferencedFromExportDataCount']} "
          f"Gen0.NameCount={gens[0]['NameCount'] if gens else 'n/a'}")

print()
sync_counts(zones, "Zones")
sync_counts(lms, "Landmarks")
# World untouched in this run.

save(ZP, zones)
save(LP, lms)
print("\nDONE")
