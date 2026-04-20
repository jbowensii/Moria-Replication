#!/usr/bin/env python3
"""
AdditiveMergeRules.py — Add new type rules to bubble JSONs' actual rule fields.

Reads tracked_items with status="removing" and adds their rules to
global_type_rules or bubble_type_rules as appropriate.
ADDITIVE ONLY — never removes or overwrites existing rules.

Usage:
    python scripts/AdditiveMergeRules.py
"""

import json
import sys
from pathlib import Path

SCRIPT_DIR = Path(__file__).resolve().parent
PROJECT_ROOT = SCRIPT_DIR.parent
BUBBLES_DIR = PROJECT_ROOT / 'bubbles'


def load_bubble_json(path):
    with open(path, 'r', encoding='utf-8') as f:
        return json.load(f)


def save_bubble_json(path, data):
    with open(path, 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=2, ensure_ascii=False)


def main():
    print('=' * 70)
    print('  AdditiveMergeRules — Propagate tracked removing rules to type rule fields')
    print('  ADDITIVE ONLY — never removes existing rules')
    print('=' * 70)

    if not BUBBLES_DIR.exists():
        print(f'ERROR: Bubbles directory not found: {BUBBLES_DIR}')
        sys.exit(1)

    bubble_files = sorted(BUBBLES_DIR.glob('*.json'))
    print(f'\nFound {len(bubble_files)} bubble JSON files')

    updated_count = 0
    total_rules_added = 0

    for bf in bubble_files:
        data = load_bubble_json(bf)
        bubble_name = data.get('bubble_name', bf.stem)
        modified = False
        rules_added = 0

        # Get existing rules in actual fields
        existing_global = {tr['typeRule'] for tr in data.get('global_type_rules', [])}
        existing_bubble = {tr['typeRule'] for tr in data.get('bubble_type_rules', [])}

        # Ensure lists exist
        if 'global_type_rules' not in data:
            data['global_type_rules'] = []
        if 'bubble_type_rules' not in data:
            data['bubble_type_rules'] = []

        # Process tracked_items with status="removing"
        for item in data.get('tracked_items', []):
            if item.get('status') != 'removing':
                continue

            scope = item.get('scope', 'global')

            for rule in item.get('rules', []):
                if scope == 'global':
                    if rule not in existing_global:
                        data['global_type_rules'].append({'typeRule': rule})
                        existing_global.add(rule)
                        rules_added += 1
                        modified = True
                elif scope == 'bubble':
                    if rule not in existing_bubble:
                        data['bubble_type_rules'].append({'typeRule': rule})
                        existing_bubble.add(rule)
                        rules_added += 1
                        modified = True

        if modified:
            save_bubble_json(bf, data)
            print(f'  UPDATED: {bf.name} — +{rules_added} rules added')
            updated_count += 1
            total_rules_added += rules_added

    print(f'\n{"=" * 70}')
    print(f'  Updated: {updated_count} files')
    print(f'  Total rules added: {total_rules_added}')
    print(f'{"=" * 70}')


if __name__ == '__main__':
    main()
