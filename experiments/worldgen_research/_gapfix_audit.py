"""Audit current state before applying gap-fix:
- Eleventh stair zone chapter refs and landmark BP
- FifthStair landmark current state (already present from prior pass)
- Confirm any zone footprint conflict at proposed cells (8,4,8) and (12,21,20)
- Confirm consecutive-floor stair coverage and which gaps exist.
"""
import json, os
BASE = os.path.dirname(os.path.abspath(__file__))
ZP = os.path.join(BASE, "DT_Moria_Zones.json")
LP = os.path.join(BASE, "DT_Moria_Landmarks.json")
WP = os.path.join(BASE, "World.json")
CP = os.path.join(BASE, "DT_Moria_Chapters.json")

def load(p):
    with open(p, "r", encoding="utf-8") as f: return json.load(f)
def get_data(asset):
    for exp in asset.get("Exports", []):
        if "Table" in exp and "Data" in exp["Table"]:
            return exp["Table"]["Data"]
def find(rows, key):
    for r in rows:
        if r.get("Name") == key: return r
    return None
def field(struct, name):
    for v in struct.get("Value", []):
        if v.get("Name") == name: return v
    return None
def rowname_of(struct, fname):
    f = field(struct, fname)
    if not f: return None
    for v in f.get("Value", []):
        if v.get("Name") == "RowName":
            return v.get("Value")
    return None

zones = load(ZP); lms = load(LP); world = load(WP); chapters = load(CP)
zrows = get_data(zones); lrows = get_data(lms); crows = get_data(chapters)

# Layer Z map per spec
LAYER_Z = {
    'Lv-7':28,'Lv-6':27,'Lv-5':23,'Lv-4':22,'Lv-3':21,'Lv-2':20,'Lv-1':18,
    'D-1':17,'D-2':13,'D-3':9,'D-4':8,'D-5':4,'D-6':1,'D-7':0,
}
Z_TO_LABEL = {v:k for k,v in LAYER_Z.items()}
ORDER = ['Lv-7','Lv-6','Lv-5','Lv-4','Lv-3','Lv-2','Lv-1','D-1','D-2','D-3','D-4','D-5','D-6','D-7']

# Map chapter rowname -> Layer label by inspecting chapters table
CHAP_LAYER = {}
for r in crows:
    nm = r.get('Name')
    layer_f = field(r, 'Layer')
    pz_f = field(r, 'PrimeZ') or field(r, 'PrimeHeight')
    if layer_f is not None:
        CHAP_LAYER[nm] = layer_f.get('Value')

print("=== Stair zones: chapter refs ===")
for r in zrows:
    nm = r.get('Name','')
    if 'Stair' not in nm: continue
    chap = rowname_of(r, 'Chapter')
    addl = field(r, 'AdditionalChapters')
    addl_names = []
    if addl:
        for ent in addl.get('Value', []):
            for v in ent.get('Value', []) if isinstance(ent, dict) else []:
                if v.get('Name') == 'RowName':
                    addl_names.append(v.get('Value'))
    print(f"  {nm}: chap={chap}, addl={addl_names}")

print()
print("=== Stair landmarks: BasePosition + BaseBubble ===")
for r in lrows:
    nm = r.get('Name','')
    if 'Stair' not in nm: continue
    bp_f = field(r, 'BasePosition')
    bp = bp_f['Value'][0]['Value'] if bp_f else None
    bb_f = field(r, 'BaseBubbleName')
    bb = bb_f.get('Value') if bb_f else None
    en_f = field(r, 'EnabledState')
    en = en_f.get('Value') if en_f else None
    print(f"  {nm}: BP={bp}, BB={bb}, En={en}")

print()
print("=== Conflict check: any zone whose BasePosition/Position is at (12,21,20) or (8,4,8) ===")
def get_pos(r):
    pf = field(r, 'Position')
    if pf:
        try: return pf['Value'][0]['Value']
        except: return None
    return None
TARGETS = [(12,21,20),(8,4,8),(10,6,8)]
for r in zrows:
    p = get_pos(r)
    if not p: continue
    t = (p.get('X'), p.get('Y'), p.get('Z'))
    if t in TARGETS:
        print(f"  CONFLICT? zone {r.get('Name')} at {t}")
for r in lrows:
    bp_f = field(r, 'BasePosition')
    if not bp_f: continue
    p = bp_f['Value'][0]['Value']
    t = (p.get('X'), p.get('Y'), p.get('Z'))
    if t in TARGETS:
        print(f"  landmark {r.get('Name')} BP at {t}")

print()
print("=== StringTable check for FifthStair key ===")
def find_st(obj, hits=None):
    if hits is None: hits=[]
    if isinstance(obj, dict):
        for k,v in obj.items():
            if k == "Landmarks.Sandbox.FirstStair" and isinstance(v, str):
                hits.append(obj)
            else:
                find_st(v, hits)
    elif isinstance(obj, list):
        for v in obj: find_st(v, hits)
    return hits
sts = find_st(world)
print(f"  found {len(sts)} StringTable map(s) containing FirstStair")
for st in sts:
    print(f"    has FifthStair key: {'Landmarks.Sandbox.FifthStair' in st}")
    if 'Landmarks.Sandbox.FifthStair' in st:
        print(f"      value: {st['Landmarks.Sandbox.FifthStair']!r}")

print()
print("=== NameMap presence ===")
for label, asset, toks in [
    ('Zones', zones, ['Sandbox_Small_Elevator_FifthStair','Sandbox.FifthStair']),
    ('Landmarks', lms, ['Sandbox.FifthStair','Landmarks.Sandbox.FifthStair','World.Landmark.Sandbox.FifthStair']),
    ('World', world, ['Landmarks.Sandbox.FifthStair']),
]:
    nm = asset.get('NameMap', [])
    for t in toks:
        print(f"  {label}: {t!r} in NameMap = {t in nm}")

print()
print("=== Chapter layer map (relevant rows) ===")
for k in ['SandboxSmall-Chapter02.Level2','SandboxSmall-Chapter03.Level3',
          'SandboxSmall-Chapter06.Level6','SandboxSmall-Chapter07.Level7',
          'SandboxSmall-Chapter11.Deep4','SandboxSmall-Chapter12.Deep3']:
    print(f"  {k} layer={CHAP_LAYER.get(k)}")
