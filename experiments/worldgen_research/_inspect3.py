import json, os
BASE = r"C:\Users\johnb\OneDrive\Documents\Projects\Moria-Replication\experiments\worldgen_research"
with open(os.path.join(BASE, "DT_Moria_Chapters.json"), "r", encoding="utf-8") as f:
    c = json.load(f)
for e in c.get("Exports", []):
    if "Table" in e:
        rows = e["Table"]["Data"]
        for r in rows:
            if r.get("Name") == "SandboxSmall-Chapter12.Elevator_C":
                print(json.dumps(r, indent=2))
                break
        break
