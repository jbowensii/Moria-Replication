"""Inspect raw structure of an Elevator zone row to understand schema."""
import json, os

BASE = os.path.dirname(os.path.abspath(__file__))
with open(os.path.join(BASE, "DT_Moria_Zones.json"), "r", encoding="utf-8") as f:
    zones = json.load(f)

for ex in zones.get("Exports", []):
    tbl = ex.get("Table")
    if tbl and "Data" in tbl:
        for row in tbl["Data"]:
            if row.get("Name") == "Sandbox_Small_Elevator_B":
                print(json.dumps(row, indent=2)[:6000])
                break
        break
