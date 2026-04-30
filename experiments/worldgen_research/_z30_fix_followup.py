"""Follow-up fixes for the z30 fix:
1. Desolation zone PreferredZOverride 30 -> 29
2. Sandbox_Small_21stHallToBridge connection Origin/Destination Subcell.Z 30 -> 29
"""
import json
import os

ROOT = os.path.dirname(os.path.abspath(__file__))


def load(name):
    with open(os.path.join(ROOT, name), 'r', encoding='utf-8') as f:
        return json.load(f)


def save(name, data):
    with open(os.path.join(ROOT, name), 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=2, ensure_ascii=False)


def get_rows(d):
    return d['Exports'][0]['Table']['Data']


def get_prop(row, name):
    for v in row.get('Value', []):
        if v.get('Name') == name:
            return v
    return None


changes = []

# --- Zones: PreferredZOverride ---
zo = load('DT_Moria_Zones.json')
for row in get_rows(zo):
    if row.get('Name') == 'Sandbox_Small_DestroyedCity_A_Desolation':
        p = get_prop(row, 'PreferredZOverride')
        if p is not None:
            old = p.get('Value')
            p['Value'] = 29
            changes.append(('Zones.Desolation.PreferredZOverride', old, 29))
save('DT_Moria_Zones.json', zo)

# --- LayoutConnections: 21stHallToBridge Subcell.Z ---
lc = load('DT_Moria_LayoutConnections.json')
for row in get_rows(lc):
    if row.get('Name') != 'Sandbox_Small_21stHallToBridge':
        continue
    for endpoint_field in ('OriginInterface', 'DestinationInterface'):
        ep = get_prop(row, endpoint_field)
        if not ep:
            continue
        inner = ep.get('Value', [])
        if not isinstance(inner, list):
            continue
        for sub in inner:
            if sub.get('Name') == 'Subcell':
                ivlist = sub.get('Value', [])
                if isinstance(ivlist, list):
                    for iv in ivlist:
                        v = iv.get('Value')
                        if isinstance(v, dict) and v.get('Z') == 30:
                            v['Z'] = 29
                            changes.append((f'LC.21stHallToBridge.{endpoint_field}.Subcell.Z', 30, 29))
save('DT_Moria_LayoutConnections.json', lc)

print('=== FOLLOW-UP CHANGES ===')
for c in changes:
    print(' ', c)
