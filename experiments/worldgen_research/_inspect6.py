import json, os
BASE = r"C:\Users\johnb\OneDrive\Documents\Projects\Moria-Replication\experiments\worldgen_research"
with open(os.path.join(BASE, "World.json"), "r", encoding="utf-8") as f:
    W = json.load(f)
e = W["Exports"][0]
print("Top keys:", list(e.keys()))
print("Table type:", type(e.get("Table")))
tbl = e.get("Table")
if isinstance(tbl, dict):
    print("Table keys:", list(tbl.keys()))
    data = tbl.get("Data")
    print("Data type:", type(data), "len:", len(data) if hasattr(data, "__len__") else "?")
    if isinstance(data, list) and data:
        print("First entry:", json.dumps(data[0], indent=2)[:800])
        # search for NinthStair / TenthStair and EighthStair entries
        for d in data:
            s = json.dumps(d)
            if "NinthStair" in s or "TenthStair" in s or "EighthStair" in s or "EleventhStair" in s:
                print("---")
                print(json.dumps(d, indent=2)[:600])
