import json, os
BASE = r"C:\Users\johnb\OneDrive\Documents\Projects\Moria-Replication\experiments\worldgen_research"

with open(os.path.join(BASE, "DT_Moria_Landmarks.json"), "r", encoding="utf-8") as f:
    L = json.load(f)
for e in L.get("Exports", []):
    if "Table" in e:
        rows = e["Table"]["Data"]
        for r in rows:
            if r.get("Name") == "Sandbox.SixthStair":
                print("=== Sandbox.SixthStair landmark ===")
                print(json.dumps(r, indent=2))
                break
        break

with open(os.path.join(BASE, "DT_Moria_Zones.json"), "r", encoding="utf-8") as f:
    Z = json.load(f)
for e in Z.get("Exports", []):
    if "Table" in e:
        rows = e["Table"]["Data"]
        for r in rows:
            if r.get("Name") == "Sandbox_Small_Elevator_D":
                print("\n=== Elev_D LandmarkHandles ===")
                for v in r.get("Value", []):
                    if v.get("Name") == "LandmarkHandles":
                        print(json.dumps(v, indent=2))
                        break
                break
        break
