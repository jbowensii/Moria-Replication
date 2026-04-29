import json, os
BASE = r"C:\Users\johnb\OneDrive\Documents\Projects\Moria-Replication\experiments\worldgen_research"
with open(os.path.join(BASE, "DT_Moria_Zones.json"), "r", encoding="utf-8") as f:
    z = json.load(f)
for e in z.get("Exports", []):
    if "Table" in e:
        rows = e["Table"]["Data"]
        for r in rows:
            if r.get("Name") == "Sandbox_Small_Elevator_C":
                print(json.dumps(r, indent=2)[:6000])
                break
        break
