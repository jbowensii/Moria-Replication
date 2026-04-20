#!/usr/bin/env python3
"""
SyncFromRemovedInstances.py — Sync all entries from removed_instances.txt to bubble JSONs.

ADDITIVE ONLY — never removes or overwrites existing data.

For each entry in removed_instances.txt:
  - Global typeRule: add to every bubble JSON's global_type_rules if not present
  - Bubble-scoped typeRule: add to specific bubble's bubble_type_rules if not present
  - Position entry with known bubble: add to that bubble's position_entries if not present
  - Position entry with unknown bubble: report for manual resolution
  - Commented-out rules: add to tracked_items with status="tracked" if not present

Usage:
    python scripts/SyncFromRemovedInstances.py
"""

import json
import sys
from pathlib import Path

SCRIPT_DIR = Path(__file__).resolve().parent
PROJECT_ROOT = SCRIPT_DIR.parent
BUBBLES_DIR = PROJECT_ROOT / 'bubbles'
REMOVED_INSTANCES = Path(r'C:\Program Files\Epic Games\ReturnToMoria\Moria\Binaries\Win64\ue4ss\Mods\MoriaCppMod\removed_instances.txt')

COORD_EPSILON = 50.0  # match tolerance for position entries


def coords_match(x1, y1, z1, x2, y2, z2):
    return (abs(x1 - x2) < COORD_EPSILON and
            abs(y1 - y2) < COORD_EPSILON and
            abs(z1 - z2) < COORD_EPSILON)


def position_exists(existing_entries, new_entry):
    """Check if a position entry already exists (by mesh name + coordinates)."""
    new_mesh = new_entry['mesh'].split('-')[0]
    new_local = new_entry.get('local', [0, 0, 0])

    for pe in existing_entries:
        ex_mesh = pe.get('mesh', '').split('-')[0]
        if new_mesh != ex_mesh:
            continue
        ex_local = pe.get('local', [0, 0, 0])
        if coords_match(new_local[0], new_local[1], new_local[2],
                        ex_local[0], ex_local[1], ex_local[2]):
            return True
    return False


def parse_removed_instances(path):
    """Parse removed_instances.txt into structured categories."""
    active_global_rules = []
    active_bubble_rules = []  # {bubble, rule}
    active_positions = []
    commented_rules = []
    commented_positions = []

    with open(path, 'r', encoding='utf-8') as f:
        lines = f.readlines()

    for line in lines:
        line = line.strip()
        if not line:
            continue

        if line.startswith('#'):
            # Check for commented-out JSON
            stripped = line.lstrip('# ')
            if stripped.startswith('{'):
                try:
                    data = json.loads(stripped)
                    if 'typeRule' in data:
                        commented_rules.append(data['typeRule'])
                    elif 'mesh' in data:
                        commented_positions.append(data)
                except json.JSONDecodeError:
                    pass
            continue

        try:
            data = json.loads(line)
        except json.JSONDecodeError:
            continue

        if 'typeRule' in data:
            rule = data['typeRule']
            if '|' in rule:
                parts = rule.split('|', 1)
                bubble = parts[0].strip()
                active_bubble_rules.append({'bubble': bubble, 'rule': rule})
            else:
                active_global_rules.append(rule)
        elif 'mesh' in data:
            active_positions.append(data)

    return {
        'global_rules': active_global_rules,
        'bubble_rules': active_bubble_rules,
        'positions': active_positions,
        'commented_rules': commented_rules,
        'commented_positions': commented_positions,
    }


def main():
    print('=' * 70)
    print('  SyncFromRemovedInstances — Full sync to bubble JSONs')
    print('  ADDITIVE ONLY — never removes existing data')
    print('=' * 70)

    if not BUBBLES_DIR.exists():
        print(f'ERROR: Bubbles directory not found: {BUBBLES_DIR}')
        sys.exit(1)

    if not REMOVED_INSTANCES.exists():
        print(f'ERROR: removed_instances.txt not found: {REMOVED_INSTANCES}')
        sys.exit(1)

    # Parse source
    source = parse_removed_instances(REMOVED_INSTANCES)
    print(f'\nSource: {REMOVED_INSTANCES.name}')
    print(f'  Active global type rules: {len(source["global_rules"])}')
    print(f'  Active bubble-scoped rules: {len(source["bubble_rules"])}')
    print(f'  Active position entries: {len(source["positions"])}')
    print(f'  Commented rules (tracked): {len(source["commented_rules"])}')
    print(f'  Commented positions (tracked): {len(source["commented_positions"])}')

    # Group positions by bubble
    pos_by_bubble = {}
    unknown_positions = []
    for p in source['positions']:
        bubble = p.get('bubble', 'unknown')
        if bubble and bubble != 'unknown':
            pos_by_bubble.setdefault(bubble, []).append(p)
        else:
            unknown_positions.append(p)

    # Load all bubble JSONs
    bubble_files = sorted(BUBBLES_DIR.glob('*.json'))
    print(f'\nTarget: {len(bubble_files)} bubble JSON files')

    # Build lookup: bubble_name -> file path
    bubble_lookup = {}
    for bf in bubble_files:
        with open(bf, 'r', encoding='utf-8') as f:
            data = json.load(f)
        bubble_lookup[data.get('bubble_name', bf.stem)] = bf

    total_global_added = 0
    total_bubble_added = 0
    total_pos_added = 0
    total_tracked_added = 0
    updated_files = set()

    # Process each bubble file
    for bf in bubble_files:
        with open(bf, 'r', encoding='utf-8') as f:
            data = json.load(f)

        bubble_name = data.get('bubble_name', bf.stem)
        modified = False

        # --- 1. Add missing global type rules ---
        existing_global = {tr['typeRule'] for tr in data.get('global_type_rules', [])}
        if 'global_type_rules' not in data:
            data['global_type_rules'] = []

        for rule in source['global_rules']:
            if rule not in existing_global:
                data['global_type_rules'].append({'typeRule': rule})
                existing_global.add(rule)
                total_global_added += 1
                modified = True

        # --- 2. Add missing bubble-scoped rules ---
        existing_bubble = {tr['typeRule'] for tr in data.get('bubble_type_rules', [])}
        if 'bubble_type_rules' not in data:
            data['bubble_type_rules'] = []

        for br in source['bubble_rules']:
            if br['bubble'] == bubble_name:
                if br['rule'] not in existing_bubble:
                    data['bubble_type_rules'].append({'typeRule': br['rule']})
                    existing_bubble.add(br['rule'])
                    total_bubble_added += 1
                    modified = True

        # --- 3. Add missing position entries ---
        existing_positions = data.get('position_entries', [])
        if 'position_entries' not in data:
            data['position_entries'] = []

        if bubble_name in pos_by_bubble:
            for pe in pos_by_bubble[bubble_name]:
                if not position_exists(existing_positions, pe):
                    data['position_entries'].append(pe)
                    existing_positions = data['position_entries']  # refresh
                    total_pos_added += 1
                    modified = True

        # --- 4. Add commented-out rules as tracked items ---
        if 'tracked_items' not in data:
            data['tracked_items'] = []

        existing_tracked_rules = set()
        for item in data['tracked_items']:
            for r in item.get('rules', []):
                existing_tracked_rules.add(r)

        # Check if we need a "Commented/Disabled Rules" tracked category
        new_commented = [r for r in source['commented_rules']
                         if r not in existing_tracked_rules
                         and r not in existing_global
                         and r not in existing_bubble]

        if new_commented:
            # Check if category already exists
            cat_name = "Commented/Disabled Rules"
            existing_cat = None
            for item in data['tracked_items']:
                if item.get('category') == cat_name:
                    existing_cat = item
                    break

            if existing_cat:
                existing_cat_rules = set(existing_cat.get('rules', []))
                for r in new_commented:
                    if r not in existing_cat_rules:
                        existing_cat['rules'].append(r)
                        total_tracked_added += 1
                        modified = True
            else:
                data['tracked_items'].append({
                    'category': cat_name,
                    'status': 'disabled',
                    'scope': 'mixed',
                    'rules': new_commented,
                })
                total_tracked_added += len(new_commented)
                modified = True

        if modified:
            with open(bf, 'w', encoding='utf-8') as f:
                json.dump(data, f, indent=2, ensure_ascii=False)
            updated_files.add(bf.name)

    # --- Report ---
    print(f'\n{"=" * 70}')
    print(f'  Results:')
    print(f'    Files updated: {len(updated_files)}')
    print(f'    Global rules added: {total_global_added}')
    print(f'    Bubble-scoped rules added: {total_bubble_added}')
    print(f'    Position entries added: {total_pos_added}')
    print(f'    Tracked/disabled rules added: {total_tracked_added}')

    # Report unresolved
    if unknown_positions:
        print(f'\n  UNRESOLVED — {len(unknown_positions)} position entries with unknown bubble:')
        for p in unknown_positions:
            mesh = p['mesh'].split('-')[0]
            world = p.get('world', [0, 0, 0])
            local = p.get('local', [0, 0, 0])
            origin = [world[i] - local[i] for i in range(3)]
            print(f'    {mesh:50s} world=({world[0]:.0f}, {world[1]:.0f}, {world[2]:.0f})')
            print(f'    {"":50s} origin=({origin[0]:.0f}, {origin[1]:.0f}, {origin[2]:.0f})')

    # Check for bubble-scoped rules targeting non-existent bubbles
    all_bubble_names = set(bubble_lookup.keys())
    for br in source['bubble_rules']:
        if br['bubble'] not in all_bubble_names:
            print(f'\n  WARNING: Bubble-scoped rule targets non-existent bubble: {br["bubble"]}')
            print(f'    Rule: {br["rule"]}')

    # Check for position entries targeting non-existent bubbles
    for bubble, entries in pos_by_bubble.items():
        if bubble not in all_bubble_names:
            print(f'\n  WARNING: {len(entries)} position entries target non-existent bubble: {bubble}')
            # Try to find closest match
            for bname in sorted(all_bubble_names):
                if bubble.lower().replace('_', '') in bname.lower().replace('_', '') or \
                   bname.lower().replace('_', '') in bubble.lower().replace('_', ''):
                    print(f'    Possible match: {bname}')

    print(f'\n{"=" * 70}')


if __name__ == '__main__':
    main()
