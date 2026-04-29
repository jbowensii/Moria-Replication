import json, os
BASE = r"C:\Users\johnb\OneDrive\Documents\Projects\Moria-Replication\experiments\worldgen_research"
with open(os.path.join(BASE, "World.json"), "r", encoding="utf-8") as f:
    W = json.load(f)
# search for the StringTable structure
def walk(o, path=""):
    if isinstance(o, dict):
        # heuristic: look for keys that include 'StringTable' or 'TableData'
        t = o.get("$type", "")
        if "StringTable" in t or o.get("Name") == "StringTable":
            print(path, "->", t, list(o.keys())[:8])
        for k, v in o.items():
            walk(v, path + "/" + str(k))
    elif isinstance(o, list):
        for i, v in enumerate(o[:50]):
            walk(v, path + f"[{i}]")
walk(W)
print("\nNameMap (first 80):")
for n in W.get("NameMap", [])[:80]:
    print(" ", n)
