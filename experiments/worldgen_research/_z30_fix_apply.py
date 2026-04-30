"""Z=30 fix v2: shrink chap-4 (Lv-4) by one cell, shift chaps 9/10/11 down by 1.

Backups are in backups/before_z30_fix/.
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


def get_intvector_z(row, struct_name):
    """Return the IntVector inner FIntVector dict for row.<struct_name>.Value (a list)."""
    s = get_prop(row, struct_name)
    if not s:
        return None
    inner = s.get('Value', [])
    if not isinstance(inner, list):
        return None
    for v in inner:
        # IntVectorPropertyData with Value = {X,Y,Z}
        if isinstance(v.get('Value'), dict) and 'Z' in v['Value']:
            return v['Value']
    return None


def get_chapter_name(row):
    """Return RowName string from row.Chapter handle."""
    s = get_prop(row, 'Chapter')
    if not s:
        return None
    inner = s.get('Value', [])
    if isinstance(inner, list):
        for v in inner:
            if v.get('Name') == 'RowName':
                return v.get('Value')
    return None


# ---------- 1. Chapters ----------
ch = load('DT_Moria_Chapters.json')
ch_changes = []
ch_targets = {
    'SandboxSmall-chapter-4':  {'MaxZ': 26},
    'SandboxSmall-chapter-9':  {'MinZ': 27, 'MaxZ': 27, 'PrimeZ': 27},
    'SandboxSmall-chapter-10': {'MinZ': 28, 'MaxZ': 28, 'PrimeZ': 28},
    'SandboxSmall-chapter-11': {'MinZ': 29, 'MaxZ': 29, 'PrimeZ': 29},
}
for row in get_rows(ch):
    n = row.get('Name', '')
    if n in ch_targets:
        for fld, newv in ch_targets[n].items():
            p = get_prop(row, fld)
            if p is None:
                ch_changes.append((n, fld, 'MISSING', None))
                continue
            old = p.get('Value')
            p['Value'] = newv
            ch_changes.append((n, fld, old, newv))

save('DT_Moria_Chapters.json', ch)

# ---------- 2. Zones ----------
zo = load('DT_Moria_Zones.json')
zone_targets = {
    'Sandbox_Small_DestroyedCity_A_Desolation': 29,
    'Sandbox_Small_OrcTown_C_Gundabad':          28,
    'Sandbox_Small_City_B_Dwarrowdelf':          27,
}
zone_changes = []
chap4_topcell_zones = []  # zones whose Position.Z == 27 in chap-4
zone_chapter_map = {}     # zonename -> chapterRowName
zone_landmarks_map = {}   # zonename -> [landmark row name]
for row in get_rows(zo):
    n = row.get('Name', '')
    pos = get_intvector_z(row, 'Position')
    if pos is None:
        continue
    z = pos.get('Z')
    chap = get_chapter_name(row)
    zone_chapter_map[n] = chap
    if n in zone_targets:
        old = z
        pos['Z'] = zone_targets[n]
        zone_changes.append((n, old, zone_targets[n]))
    if chap == 'SandboxSmall-chapter-4' and z == 27:
        chap4_topcell_zones.append(n)
    # collect LandmarkHandles
    lh = get_prop(row, 'LandmarkHandles')
    if lh:
        arr = lh.get('Value', [])
        if isinstance(arr, list):
            lms = []
            for entry in arr:
                # entry is MorZoneLandmarkEntry with Value list containing Landmark handle (RowName)
                if not isinstance(entry, dict):
                    continue
                ev = entry.get('Value', [])
                if isinstance(ev, list):
                    for sub in ev:
                        if sub.get('Name') == 'Landmark':
                            inner = sub.get('Value', [])
                            if isinstance(inner, list):
                                for k in inner:
                                    if k.get('Name') == 'RowName':
                                        lms.append(k.get('Value'))
            if lms:
                zone_landmarks_map[n] = lms

save('DT_Moria_Zones.json', zo)

# ---------- 3. Landmarks ----------
lm = load('DT_Moria_Landmarks.json')
lm_targets = {
    'Sandbox.21stHall':         29,
    'Sandbox.Dwarrowdelf':      27,
    'Sandbox.TopElevator':      26,
    'Sandbox.MithrilMineNexus':  4,
}
lm_changes = []

# Build reverse: landmark name -> hosting zones
lm_to_zones = {}
for zname, lms in zone_landmarks_map.items():
    for ln in lms:
        lm_to_zones.setdefault(ln, []).append(zname)

moved_zone_set = set(zone_targets.keys())
old_to_new = {30: 29, 29: 28, 28: 27}

extra_changes = []  # other landmarks under moved zones still at old z

for row in get_rows(lm):
    n = row.get('Name', '')
    bp = get_intvector_z(row, 'BasePosition')
    if bp is None:
        continue
    z = bp.get('Z')
    if n in lm_targets:
        old = z
        bp['Z'] = lm_targets[n]
        lm_changes.append((n, old, lm_targets[n]))
        continue
    # auto-shift if hosted by a moved zone and Z matches old chapter Z
    hosts = lm_to_zones.get(n, [])
    if any(h in moved_zone_set for h in hosts):
        if z in old_to_new:
            new_z = old_to_new[z]
            bp['Z'] = new_z
            extra_changes.append((n, hosts, z, new_z))

save('DT_Moria_Landmarks.json', lm)

# ---------- Report ----------
print('=== CHAPTER CHANGES ===')
for c in ch_changes:
    print(' ', c)
print('=== ZONE CHANGES ===')
for c in zone_changes:
    print(' ', c)
print('=== LANDMARK CHANGES (explicit) ===')
for c in lm_changes:
    print(' ', c)
print('=== EXTRA LANDMARKS ON MOVED ZONES (auto-shifted) ===')
for c in extra_changes:
    print(' ', c)
print('=== ZONES IN CHAP-4 WITH Z=27 (need attention) ===')
for n in chap4_topcell_zones:
    print(' ', n)
print('=== HOSTED-LANDMARKS PER MOVED ZONE ===')
for z in moved_zone_set:
    print(' ', z, '->', zone_landmarks_map.get(z, []))
