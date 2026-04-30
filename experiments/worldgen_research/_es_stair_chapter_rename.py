"""Apply Tasks A (ES values), B (stair landmark renames), C (chapter-prefix renames),
and D (NameMap sync). Updates DT_Moria_Chapters, Landmarks, Zones, LayoutConnections."""
import json
import re
from pathlib import Path

ROOT = Path(__file__).parent

# ---- Task A: ES targets per chapter ----
ES_TARGETS = {
    'SandboxSmall-chapter-1': 0,
    'SandboxSmall-chapter-2': 1,
    'SandboxSmall-chapter-3': 2,
    'SandboxSmall-chapter-4': 3,
    'SandboxSmall-chapter-5': 4,
    'SandboxSmall-chapter-6': 4,
    'SandboxSmall-chapter-7': 4,
    'SandboxSmall-chapter-8': 4,
    'SandboxSmall-chapter-9': 4,
    'SandboxSmall-chapter-10': 4,
    'SandboxSmall-chapter-11': 4,
    'SandboxSmall-chapter-12': 3,
    'SandboxSmall-chapter-13': 2,
    'SandboxSmall-chapter-14': 1,
}

# ---- Task B: stair landmark renames ----
STAIR_RENAMES = {
    'Sandbox.Lv3Lv4Connector': 'Sandbox.FifthStair',
    'Sandbox.TopElevator':     'Sandbox.SeventhStair',
    'Chapter3.CrystalDescent': 'Sandbox.FourteenthStair',
    'Sandbox.D7D6Stair':       'Sandbox.TwelfthStair',
    'Sandbox.DeepBottomEl':    'Sandbox.TenthStair',
    'Sandbox.D4D3Connector':   'Sandbox.EighthStair',
    'Sandbox.DeepMidEl':       'Sandbox.SixthStair',
    'Sandbox.DeepUpperEl':     'Sandbox.FourthStair',
    'Sandbox.D1Lv1Connector':  'Sandbox.SecondStair',
}

# Vanilla disabled rows that collide with new names — rename to _disabled_vanilla_ prefix
VANILLA_DISABLED_RENAMES = {
    'Sandbox.SecondStair':  'Sandbox._disabled_vanilla_SecondStair',
    'Sandbox.ThirdStair':   'Sandbox._disabled_vanilla_ThirdStair',
    'Sandbox.FourthStair':  'Sandbox._disabled_vanilla_FourthStair',
    'Sandbox.FifthStair':   'Sandbox._disabled_vanilla_FifthStair',
}

# ---- Task C: chapter-prefix renames ----
# Only landmark with a Live SS host is Chapter2.ElvenQuarterEntrance -> Chapter1
CHAPTER_PREFIX_RENAMES = {
    'Chapter2.ElvenQuarterEntrance': 'Chapter1.ElvenQuarterEntrance',
}

# Combine all landmark renames. ORDER MATTERS: vanilla first (clear the way), then stair, then chapter.
ALL_LM_RENAMES = {}
ALL_LM_RENAMES.update(VANILLA_DISABLED_RENAMES)
ALL_LM_RENAMES.update(STAIR_RENAMES)
ALL_LM_RENAMES.update(CHAPTER_PREFIX_RENAMES)


def load(p):
    with open(p, 'r', encoding='utf-8') as f:
        return json.load(f)

def save(p, d):
    with open(p, 'w', encoding='utf-8') as f:
        json.dump(d, f, indent=2)


def update_namemap(doc, new_strings):
    """Add new strings to NameMap if not present. Update NameMapLookup if present."""
    nm = doc.get('NameMap', [])
    existing = set(nm)
    added = 0
    for s in new_strings:
        if s not in existing:
            nm.append(s)
            existing.add(s)
            added += 1
    # NameMapIndexList & NameMapLookup may exist; UAssetGUI generally regenerates these
    # on fromjson, but we'll leave them as-is. Fresh strings appended is sufficient.
    return added


# ---- Task A: Apply ES values ----
def apply_task_a():
    p = ROOT / 'DT_Moria_Chapters.json'
    d = load(p)
    rows = d['Exports'][0]['Table']['Data']
    changes = []
    for r in rows:
        name = r.get('Name','')
        if name in ES_TARGETS:
            target = ES_TARGETS[name]
            for v in r.get('Value', []):
                if v.get('Name') == 'EnemyScalingLevel':
                    old = v.get('Value')
                    if old != target:
                        v['Value'] = target
                        changes.append((name, old, target))
                    break
    save(p, d)
    return changes


# ---- Task B + C: rename landmarks in DT_Moria_Landmarks ----
def apply_landmark_renames():
    p = ROOT / 'DT_Moria_Landmarks.json'
    d = load(p)
    rows = d['Exports'][0]['Table']['Data']
    renamed = []
    for r in rows:
        name = r.get('Name','')
        if name in ALL_LM_RENAMES:
            new = ALL_LM_RENAMES[name]
            r['Name'] = new
            renamed.append((name, new))
    # Update NameMap
    new_strings = list(ALL_LM_RENAMES.values())
    added = update_namemap(d, new_strings)
    save(p, d)
    return renamed, added


# ---- Update Zone LandmarkHandles refs ----
def apply_zone_ref_updates():
    p = ROOT / 'DT_Moria_Zones.json'
    d = load(p)
    rows = d['Exports'][0]['Table']['Data']
    ref_updates = 0
    for r in rows:
        for v in r.get('Value', []):
            if v.get('Name') == 'LandmarkHandles':
                for entry in v.get('Value', []):
                    for sub in entry.get('Value', []):
                        if sub.get('Name') == 'Landmark':
                            for nn in sub.get('Value', []):
                                if nn.get('Name') == 'RowName':
                                    val = nn.get('Value')
                                    if val in ALL_LM_RENAMES:
                                        nn['Value'] = ALL_LM_RENAMES[val]
                                        ref_updates += 1
    added = update_namemap(d, list(ALL_LM_RENAMES.values()))
    save(p, d)
    return ref_updates, added


# ---- Update LayoutConnections Origin/Destination Landmark refs ----
def apply_lc_ref_updates():
    p = ROOT / 'DT_Moria_LayoutConnections.json'
    d = load(p)
    rows = d['Exports'][0]['Table']['Data']
    ref_updates = 0
    for r in rows:
        for v in r.get('Value', []):
            if v.get('Name') in ('OriginLandmark', 'DestinationLandmark'):
                for nn in v.get('Value', []):
                    if nn.get('Name') == 'RowName':
                        val = nn.get('Value')
                        if val in ALL_LM_RENAMES:
                            nn['Value'] = ALL_LM_RENAMES[val]
                            ref_updates += 1
    added = update_namemap(d, list(ALL_LM_RENAMES.values()))
    save(p, d)
    return ref_updates, added


if __name__ == '__main__':
    print('=== Task A: EnemyScalingLevel updates ===')
    a_changes = apply_task_a()
    for name, old, new in a_changes:
        print(f'  {name}: {old} -> {new}')
    print(f'  total changed: {len(a_changes)}')

    print('\n=== Task B+C: Landmark renames ===')
    renamed, lm_added = apply_landmark_renames()
    for old, new in renamed:
        print(f'  {old} -> {new}')
    print(f'  total renamed: {len(renamed)} | NameMap added: {lm_added}')

    print('\n=== Zone reference updates ===')
    z_refs, z_added = apply_zone_ref_updates()
    print(f'  Zone landmark refs updated: {z_refs} | NameMap added: {z_added}')

    print('\n=== LayoutConnection reference updates ===')
    lc_refs, lc_added = apply_lc_ref_updates()
    print(f'  LC landmark refs updated: {lc_refs} | NameMap added: {lc_added}')
