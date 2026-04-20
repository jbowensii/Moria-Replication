#!/usr/bin/env python3
"""
AdditiveMerge.py — Additively merge new type rules and tracked items into bubble JSONs.

NEVER overwrites existing data. Only APPENDS new entries that don't already exist.
Reads removed_instances.txt for the new rules added this session and merges them
into the appropriate bubble JSON files.

Usage:
    python scripts/AdditiveMerge.py
"""

import json
import os
import sys
from pathlib import Path

SCRIPT_DIR = Path(__file__).resolve().parent
PROJECT_ROOT = SCRIPT_DIR.parent
BUBBLES_DIR = PROJECT_ROOT / 'bubbles'

# The new type rules added this session, organized by category
# These are GLOBAL rules (apply to all bubbles) unless otherwise noted

NEW_GLOBAL_TYPE_RULES = {
    "rugs": {
        "category": "Rugs",
        "status": "removing",
        "rules": [
            "Rug_End_3M-BlockAll-dcl-L100",
            "Rug_Flat_3M-BlockAll-dcl-L100",
            "Rug_Flat_6M-BlockAll-dcl-L100",
            "Rug_Single-BlockAll-dcl-L100",
            "Rug_Stair_1x3M-BlockAll-dcl-L100",
        ]
    },
    "banners": {
        "category": "Banners",
        "status": "removing",
        "rules": [
            "SM_BannerPole-BlockAll-dcl-L100",
            "SM_Banner_AA-BlockAll-dcl-L100",
            "SM_Banner_BB-BlockAll-dcl-L100",
            "OrcBanner-BlockAll-dcl-L100",
            "Warren_lighting_Banner-BlockAll-dcl-L100",
            "BP_DM_Deco_Orc_Banner-BlockAll-dcl-L100",
            "BP_DM_Warren_lighting_Banner-BlockAll-dcl-L100",
        ]
    },
    "tapestries": {
        "category": "Tapestries",
        "status": "removing",
        "rules": [
            "Dwelling_Tapestry-BlockAll-dcl-L100",
        ]
    },
    "spider_webs": {
        "category": "Spider Webs",
        "status": "removing",
        "rules": [
            "SpiderWeb-BlockAll-dcl-L100",
            "SpiderWeb3_placeholder-BlockAll-dcl-L100",
            "SpiderWeb_Mines-BlockAll-dcl-L100",
        ]
    },
    "decorative_weapons": {
        "category": "Decorative Weapons",
        "status": "removing",
        "rules": [
            "D_Weapon_IronHills-BlockAll-dcl-L100",
            "D_Weapon_Khazad-BlockAll-dcl-L100",
            "D_Weapon_Steel-BlockAll-dcl-L100",
            "D_Weapon_Rohan-BlockAll-dcl-L100",
        ]
    },
    "scaffolding_open": {
        "category": "Scaffolding (Open)",
        "status": "removing",
        "rules": [
            "AB_Mines_Scaffolding_Platform_3x3x3_Open-BlockAll-dcl-L100",
        ]
    },
    "garden_ivy": {
        "category": "Garden Ivy",
        "status": "tracked",  # NOT removing — user wants to keep
        "rules": [
            "Garden_Ivy_Fance-MI_Mines_Scaffolding_C_Mat-BlockAll-dcl-L100",
        ]
    },
    "weapon_racks": {
        "category": "Weapon/Armor Racks",
        "status": "tracked",  # NOT removing — user wants to keep
        "rules": [
            "WeaponRack-BlockAll-dcl-L100",
            "BP_ItemRack_Weapons-BlockAll-dcl-L100",
        ]
    },
    "structural_walls": {
        "category": "Structural Walls (DO NOT REMOVE)",
        "status": "tracked",  # NOT removing — destroys environment
        "rules": [
            "PWM_Quarry_4x4x4_A-ProcMaterial_City_4m_Floor-BlockAll-dcl-L100",
            "PWM_Quarry_4x5x10-ProcMaterial_Quarry_Atlas_A-BlockAll-dcl-L100",
        ]
    },
}

# Bubble-scoped rules (only apply to specific bubbles)
BUBBLE_SCOPED_RULES = {
    "Aftermath": {
        "rubble_debris": {
            "category": "Rubble & Debris",
            "status": "removing",
            "rules": [
                "Aftermath | @Rubble_Masonry-BlockAll-dcl-L100",
                "Aftermath | @PWM_Quarry_RockDebris-BlockAll-dcl-L100",
                "Aftermath | @SM_Debris_Floor-BlockAll-dcl-L100",
                "Aftermath | @Mine_tailings_Debris-BlockAll-dcl-L100",
            ]
        },
        "broken_floors": {
            "category": "Broken Floors (DO NOT REMOVE)",
            "status": "tracked",  # NOT removing in Aftermath
            "rules": [
                "Aftermath | @Suburbs_Floor_3x3m_AA_Broken-BlockAll-dcl-L100",
                "Aftermath | @Suburbs_Floor_3x3m_AB_Broken-BlockAll-dcl-L100",
            ]
        },
        "burning_debris": {
            "category": "Burning Debris (DO NOT REMOVE)",
            "status": "tracked",  # NOT removing in Aftermath
            "rules": [
                "Aftermath | @BP_BurningDebris-BlockAll-dcl-L100",
            ]
        },
    },
    "The_Doors_of_Durin": {
        "rubble_debris": {
            "category": "Rubble & Debris",
            "status": "removing",
            "rules": [
                "The_Doors_of_Durin | @Rubble_Masonry-BlockAll-dcl-L100",
                "The_Doors_of_Durin | @PWM_Quarry_RockDebris-BlockAll-dcl-L100",
                "The_Doors_of_Durin | @SM_Debris_Floor-BlockAll-dcl-L100",
                "The_Doors_of_Durin | @Mine_tailings_Debris-BlockAll-dcl-L100",
            ]
        },
        "broken_floors": {
            "category": "Broken Floors",
            "status": "removing",  # Removing in Doors of Durin
            "rules": [
                "The_Doors_of_Durin | @Suburbs_Floor_3x3m_AA_Broken-BlockAll-dcl-L100",
                "The_Doors_of_Durin | @Suburbs_Floor_3x3m_AB_Broken-BlockAll-dcl-L100",
            ]
        },
    },
}


def load_bubble_json(path):
    with open(path, 'r', encoding='utf-8') as f:
        return json.load(f)


def save_bubble_json(path, data):
    with open(path, 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=2, ensure_ascii=False)


def get_existing_rules(data):
    """Get set of all existing typeRule values in a bubble JSON."""
    rules = set()
    for tr in data.get('global_type_rules', []):
        rules.add(tr.get('typeRule', ''))
    for tr in data.get('bubble_type_rules', []):
        rules.add(tr.get('typeRule', ''))
    # Also check tracked_items if present
    for item in data.get('tracked_items', []):
        for rule in item.get('rules', []):
            rules.add(rule)
    return rules


def main():
    print('=' * 70)
    print('  Additive Merge — Adding tracked items to bubble JSONs')
    print('  ADDITIVE ONLY — never overwrites existing data')
    print('=' * 70)

    if not BUBBLES_DIR.exists():
        print(f'ERROR: Bubbles directory not found: {BUBBLES_DIR}')
        sys.exit(1)

    bubble_files = sorted(BUBBLES_DIR.glob('*.json'))
    print(f'\nFound {len(bubble_files)} bubble JSON files')

    updated_count = 0
    skipped_count = 0

    for bf in bubble_files:
        data = load_bubble_json(bf)
        bubble_name = data.get('bubble_name', bf.stem)
        modified = False

        # Ensure tracked_items list exists
        if 'tracked_items' not in data:
            data['tracked_items'] = []

        existing_rules = get_existing_rules(data)
        existing_categories = {item['category'] for item in data['tracked_items']}

        # Add global type rules as tracked items
        for key, group in NEW_GLOBAL_TYPE_RULES.items():
            category = group['category']
            if category in existing_categories:
                continue  # Already has this category

            # Check if any rules from this group are new
            new_rules = [r for r in group['rules'] if r not in existing_rules]
            if not new_rules and not group['rules']:
                continue

            data['tracked_items'].append({
                'category': category,
                'status': group['status'],
                'scope': 'global',
                'rules': group['rules'],
            })
            modified = True

        # Add bubble-scoped rules if this bubble has them
        if bubble_name in BUBBLE_SCOPED_RULES:
            for key, group in BUBBLE_SCOPED_RULES[bubble_name].items():
                category = f"{group['category']} ({bubble_name})"
                if category in existing_categories:
                    continue

                data['tracked_items'].append({
                    'category': category,
                    'status': group['status'],
                    'scope': 'bubble',
                    'bubble': bubble_name,
                    'rules': group['rules'],
                })
                modified = True

        if modified:
            save_bubble_json(bf, data)
            n_items = len(data['tracked_items'])
            print(f'  UPDATED: {bf.name} — {n_items} tracked item categories')
            updated_count += 1
        else:
            skipped_count += 1

    print(f'\n{"=" * 70}')
    print(f'  Updated: {updated_count} files')
    print(f'  Skipped: {skipped_count} files (already up to date)')
    print(f'{"=" * 70}')


if __name__ == '__main__':
    main()
