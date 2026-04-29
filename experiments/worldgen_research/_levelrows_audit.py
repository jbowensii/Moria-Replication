import json, os, sys, collections

ROOT = r"C:/Users/johnb/OneDrive/Documents/Projects/Moria-Replication/experiments/worldgen_research"
CH = os.path.join(ROOT, "DT_Moria_Chapters.json")

with open(CH, "r", encoding="utf-8") as f:
    j = json.load(f)

def find_export(j):
    for ex in j["Exports"]:
        if ex.get("$type", "").startswith("UAssetAPI.ExportTypes.DataTableExport"):
            return ex
    return None

ex = find_export(j)
data = ex["Table"]["Data"]

def get_prop(row, name):
    for p in row["Value"]:
        if p.get("Name") == name:
            return p
    return None

# Map row name -> row dict
rows = {r["Name"]: r for r in data}

target_layers = {3,4,5,6,-1,-4,-5,-6}
existing_level_layers = {0,1,2,-2,-3,-7}

# Collect peers per layer for SandboxSmall- prefix
peers_by_layer = collections.defaultdict(list)
for name, r in rows.items():
    if not name.startswith("SandboxSmall-Chapter"):
        continue
    layer_p = get_prop(r, "Layer")
    if layer_p is None:
        continue
    layer = layer_p.get("Value")
    peers_by_layer[layer].append(name)

print("Layers and peer counts:")
for L in sorted(peers_by_layer.keys(), reverse=True):
    print(f"  Layer {L}: {len(peers_by_layer[L])} rows; sample: {peers_by_layer[L][:3]}")

print("\nTarget layer audit (Z values from anchored peer):")
fields = ["Layer","ChapterID","MinZ","MaxZ","PrimeZ","EnemyScalingLevel"]
for L in sorted(target_layers, reverse=True):
    peers = peers_by_layer.get(L, [])
    if not peers:
        print(f"  Layer {L}: NO PEER FOUND -- PAUSE")
        continue
    # pick first peer
    pname = peers[0]
    pr = rows[pname]
    vals = {}
    for fn in fields:
        p = get_prop(pr, fn)
        vals[fn] = p.get("Value") if p else None
    print(f"  Layer {L}: peer={pname} -> {vals}")

print("\nExisting level rows on layers we keep:")
for L in sorted(existing_level_layers, reverse=True):
    peers = peers_by_layer.get(L, [])
    print(f"  Layer {L}: {peers[:5]}")
