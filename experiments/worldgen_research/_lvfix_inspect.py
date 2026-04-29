import json, os
ROOT = os.path.dirname(os.path.abspath(__file__))
def load(n):
    with open(os.path.join(ROOT,n),'r',encoding='utf-8') as f: return json.load(f)

zones = load('DT_Moria_Zones.json')
lms = load('DT_Moria_Landmarks.json')

def rows(dt):
    for exp in dt.get('Exports', []):
        if 'Table' in exp:
            return exp['Table'].get('Data', [])
    return []

zr = rows(zones)
lr = rows(lms)

# find Sandbox_Small_Elevator_B
for r in zr:
    if r.get('Name') == 'Sandbox_Small_Elevator_B':
        print(json.dumps(r, indent=2)[:4000])
        break
