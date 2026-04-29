import json, os
BASE = r"C:\Users\johnb\OneDrive\Documents\Projects\Moria-Replication\experiments\worldgen_research"
with open(os.path.join(BASE, "World.json"), "r", encoding="utf-8") as f:
    W = json.load(f)
tbl = W["Exports"][0]["Table"]
print("Namespace:", tbl["TableNamespace"])
val = tbl["Value"]
print("Value type:", type(val), "len:", len(val))
# Find one entry
print("First two:")
print(json.dumps(val[0], indent=2))
print(json.dumps(val[1], indent=2))
# search for NinthStair etc
for v in val:
    s = json.dumps(v)
    if "NinthStair" in s or "EleventhStair" in s:
        print("MATCH:", json.dumps(v))
