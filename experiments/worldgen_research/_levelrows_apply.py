import json, os, copy

ROOT = r"C:/Users/johnb/OneDrive/Documents/Projects/Moria-Replication/experiments/worldgen_research"
CH = os.path.join(ROOT, "DT_Moria_Chapters.json")

with open(CH, "r", encoding="utf-8") as f:
    j = json.load(f)

def find_dt_export(j):
    for ex in j["Exports"]:
        if ex.get("$type", "").startswith("UAssetAPI.ExportTypes.DataTableExport"):
            return ex
    return None

ex = find_dt_export(j)
data = ex["Table"]["Data"]
rows = {r["Name"]: r for r in data}

def get_prop(row, name):
    for p in row["Value"]:
        if p.get("Name") == name:
            return p
    return None

def set_prop(row, name, value):
    p = get_prop(row, name)
    if p is None:
        raise KeyError(f"prop {name} not found")
    p["Value"] = value

# Specs: layer -> (row_name, chap_id, display_key, template_row_name)
ABOVE = "SandboxSmall-Chapter01.Level1"
BELOW = "SandboxSmall-Chapter13.Deep2"

specs = [
    ( 3, "SandboxSmall-Chapter04.Level4",  4, "Chapter.Sandbox.Level4.Name", ABOVE),
    ( 4, "SandboxSmall-Chapter05.Level5",  5, "Chapter.Sandbox.Level5.Name", ABOVE),
    ( 5, "SandboxSmall-Chapter06.Level6",  6, "Chapter.Sandbox.Level6.Name", ABOVE),
    ( 6, "SandboxSmall-Chapter07.Level7",  7, "Chapter.Sandbox.Level7.Name", ABOVE),
    (-1, "SandboxSmall-Chapter14.Deep1", 14, "Chapter.Sandbox.Deep1.Name",  BELOW),
    (-4, "SandboxSmall-Chapter11.Deep4", 11, "Chapter.Sandbox.Deep4.Name",  BELOW),
    (-5, "SandboxSmall-Chapter10.Deep5", 10, "Chapter.Sandbox.Deep5.Name",  BELOW),
    (-6, "SandboxSmall-Chapter09.Deep6",  9, "Chapter.Sandbox.Deep6.Name",  BELOW),
]

# For each layer, find an anchored peer (any SandboxSmall-Chapter row currently on that layer)
def find_peer_z_esl(layer):
    for name, r in rows.items():
        if not name.startswith("SandboxSmall-Chapter"):
            continue
        lp = get_prop(r, "Layer")
        if lp and lp.get("Value") == layer:
            return {
                "MinZ":  get_prop(r, "MinZ").get("Value"),
                "MaxZ":  get_prop(r, "MaxZ").get("Value"),
                "PrimeZ":get_prop(r, "PrimeZ").get("Value"),
                "EnemyScalingLevel": get_prop(r, "EnemyScalingLevel").get("Value"),
                "_peer": name,
            }
    return None

before_namemap_len = len(j["NameMap"])
before_nrfedc = j.get("NamesReferencedFromExportDataCount")

added = []
for layer, new_name, chap_id, disp_key, tmpl_name in specs:
    if new_name in rows:
        print(f"SKIP existing: {new_name}")
        continue
    peer = find_peer_z_esl(layer)
    if peer is None:
        raise RuntimeError(f"No peer for layer {layer}")
    tmpl = rows[tmpl_name]
    new_row = copy.deepcopy(tmpl)
    new_row["Name"] = new_name
    set_prop(new_row, "ChapterID", chap_id)
    set_prop(new_row, "Layer", layer)
    set_prop(new_row, "EnemyScalingLevel", peer["EnemyScalingLevel"])
    set_prop(new_row, "MinZ", peer["MinZ"])
    set_prop(new_row, "MaxZ", peer["MaxZ"])
    set_prop(new_row, "PrimeZ", peer["PrimeZ"])
    set_prop(new_row, "DisplayName", disp_key)
    # ensure EnabledState Live (template already is)
    es = get_prop(new_row, "EnabledState")
    es["Value"] = "ERowEnabledState::Live"
    data.append(new_row)
    rows[new_name] = new_row
    added.append((layer, new_name, chap_id, peer))
    print(f"ADD layer={layer:+d} {new_name} chap={chap_id} Z={peer['MinZ']}/{peer['MaxZ']}/{peer['PrimeZ']} ESL={peer['EnemyScalingLevel']} (peer={peer['_peer']})")

# Update NameMap: ensure each new row name AND its DisplayName key are in NameMap
# (DisplayName values are FString in TextProperty StringTableEntry; check existing rows to see if they're added)
namemap = j["NameMap"]
ns = set(namemap)

# Also DisplayName key strings -- check if Level1 key is in NameMap currently
for nm in ["Chapter.Sandbox.Level1.Name", "Chapter.Sandbox.Deep2.Name"]:
    print(f"  baseline NameMap contains {nm!r}: {nm in ns}")

def add_name(s):
    if s not in ns:
        namemap.append(s)
        ns.add(s)
        return True
    return False

new_added_names = []
for layer, new_name, chap_id, peer in added:
    if add_name(new_name):
        new_added_names.append(new_name)

# DisplayName key strings: check if existing level rows have their keys in NameMap
# If yes, add ours too. If no, leave alone (consistent with existing pattern).
disp_in_nm = "Chapter.Sandbox.Level1.Name" in ns
print(f"  Level1.Name in NameMap (baseline): {disp_in_nm}")
if disp_in_nm:
    for layer, new_name, chap_id, peer in added:
        # find disp_key from spec
        pass
    for spec in specs:
        layer, new_name, chap_id, disp_key, tmpl_name = spec
        if rows[new_name].get("Name") == new_name:  # row exists
            if add_name(disp_key):
                new_added_names.append(disp_key)

# Sync NamesReferencedFromExportDataCount = len(NameMap)
j["NamesReferencedFromExportDataCount"] = len(namemap)
# Generations[0].NameCount: leave alone unless less than NameMap len
gens = j.get("Generations", [])
if gens and gens[0].get("NameCount", 0) < len(namemap):
    gens[0]["NameCount"] = len(namemap)

print(f"\nNameMap before: {before_namemap_len}, after: {len(namemap)}")
print(f"NamesReferencedFromExportDataCount before: {before_nrfedc}, after: {j['NamesReferencedFromExportDataCount']}")
print(f"Names added to NameMap: {new_added_names}")

with open(CH, "w", encoding="utf-8") as f:
    json.dump(j, f, indent=2)
print("WROTE", CH)
