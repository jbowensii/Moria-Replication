"""
split_removal_spec.py — Split removed_instances.txt into per-bubble JSON files.

Reads the master removal spec (JSON Lines) from the game directory and produces
one .json file per bubble in the project's bubbles/ directory.  Each output file
contains:
  - "uasset_files" : list of matching .uasset paths for the bubble
  - "global_type_rules" : type rules that apply to ALL bubbles (duplicated)
  - "bubble_type_rules" : type rules scoped to this specific bubble
  - "position_entries"  : mesh+coordinate removal entries for this bubble

Position entries with bubble="unknown" are resolved by searching all BD_BB_*.json
FModel exports for the mesh name; matches are placed in the corresponding bubble
file(s).

Usage:
    python scripts/split_removal_spec.py
"""

import json
import os
import re
import sys
from pathlib import Path

# ---------------------------------------------------------------------------
# Paths
# ---------------------------------------------------------------------------
SCRIPT_DIR = Path(__file__).resolve().parent
PROJECT_DIR = SCRIPT_DIR.parent
BUBBLES_DIR = PROJECT_DIR / 'bubbles'

REMOVAL_SPEC = Path(
    r'C:\Program Files\Epic Games\ReturnToMoria\Moria\Binaries'
    r'\Win64\ue4ss\Mods\MoriaCppMod\removed_instances.txt'
)

FMODEL_CATALOG_DIR = (
    PROJECT_DIR / 'tools' / 'cloud-exports' / 'Tech' / 'Data'
    / 'Bubbles' / 'GameWorldCatalog'
)

LEGACY_ASSETS_DIR = (
    PROJECT_DIR / 'tools' / 'legacy-assets' / 'Moria' / 'Content'
    / 'Tech' / 'Data' / 'Bubbles' / 'GameWorldCatalog'
)

# ---------------------------------------------------------------------------
# Display-name ↔ BD_BB filename mapping
# The game uses human-readable bubble display names (e.g. "Aftermath") but
# the data files use internal identifiers (e.g. BD_BB_Chapter2_GameStart).
# This table maps the underscore form of the display name (as it appears in
# removed_instances.txt "bubble" field) to the BD_BB stem.
# ---------------------------------------------------------------------------
BUBBLE_NAME_TO_BD = {
    # Chapter 2
    'Aftermath':                    'BD_BB_Chapter2_GameStart',
    'The_Doors_of_Durin':           'BD_BB_Chapter2_DoorsOfDurin',
    'The_Elven_Quarter':            'BD_BB_Chapter2_ElvenQuarterEntrance',
    'The_Great_Forge_of_Narvi':     'BD_BB_Chapter2_ElvenQuarterPromenade',
    'Gate_to_Durins_Highway':       'BD_BB_Chapter2_BlockedHighwayWestTown',
    # Chapter 3
    'Crystal_Descent':              'BD_BB_Chapter3_CrystalDescent',
    'The_Drainworks':               'BD_BB_Chapter3_Drainworks',
    'Eastern_Stairs':               'BD_BB_Chapter3_EasternStairs',
    'The_Flooded_Forge':            'BD_BB_Chapter3_FloodedForge',
    'Headwater_Nexus':              'BD_BB_Chapter3_HeadwaterNexus',
    'The_Library_Spring':           'BD_BB_Chapter3_LibrarySpring',
    'Rising_Floor':                 'BD_BB_Chapter3_RisingFloor',
    'Underground_Lake':             'BD_BB_Chapter3_UndergroundLake',
    'Valley_of_Kings':              'BD_BB_Chapter3_ValleyOfKings',
    # Chapter 4
    'Dwarrowdelf':                  'BD_BB_Chapter4_BalrogsWake',
    'The_Balrogs_Wake':             'BD_BB_Chapter4_BalrogsWake',
    'Durins_Forge':                 'BD_BB_Chapter4_DurinsForge',
    'The_Bridge_of_Khazad_Dum':     'BD_BB_Chapter4_Bridge',
    'City_Nexus':                   'BD_BB_Chapter4_CityNexus',
    'Nogrod_Forge':                 'BD_BB_Chapter4_NogrodForge',
    'Upper_Armoury':                'BD_BB_Chapter4_UpperArmoury',
    'Highway_East':                 'BD_BB_Chapter4_BlockedHighwayEast',
    # Chapter 5
    'The_Balrogs_Nest':             'BD_BB_Chapter5_BalrogsNest',
    'Bone_Hoard':                   'BD_BB_Chapter5_BoneHoard',
    'The_Broken_Seal':              'BD_BB_Chapter5_BrokenSeal',
    'Cavern_Shaft':                 'BD_BB_Chapter5_CavernShaft',
    'The_Crossroads_of_Zirakzigil': 'BD_BB_Chapter5_Crossroads',
    'Mithril_Forge':                'BD_BB_Chapter5_MithrilForge',
    'Mithril_Mine_Nexus':           'BD_BB_Chapter5_MithrilMineNexus',
    'The_Desolation':               'BD_BB_Chapter4_BalrogsWake',
    # Chapter 6
    'Dimrill_Gate':                  'BD_BB_Chapter6_DimrillGate',
    # Shared / procedural
    'Western_Mines':                'BD_BB_Nexus_MineA',
    'The_Chamber_of_Mazarbul':      'BD_BB_Chapter4_BalrogsWake',  # sub-area
    'Highway':                      'BD_BB_Highway',
    'DwarfHall':                    'BD_BB_DwarfHall1',
    'Wild_Mine':                    'BD_BB_WildMine',
    'Orc_Town_Gate':                'BD_BB_OrcTown_Gate',
    'Orc_Prison':                   'BD_BB_OrcPrison',
    'Urban_Circle':                 'BD_BB_UrbanCircle',
    'Troll_Cave':                   'BD_BB_TrollCave',
    'Farm_Cavern':                  'BD_BB_FarmCavern',
    'Mining_Camp':                  'BD_BB_MiningCamp',
    'Snaking_River':                'BD_BB_SnakingRiver',
}

# Reverse map: BD stem -> list of display names
BD_TO_BUBBLE_NAMES = {}
for display, bd in BUBBLE_NAME_TO_BD.items():
    BD_TO_BUBBLE_NAMES.setdefault(bd, []).append(display)


def bd_stem_from_json_filename(json_filename: str) -> str:
    """BD_BB_Chapter2_GameStart.json -> BD_BB_Chapter2_GameStart"""
    return json_filename.replace('.json', '')


def find_uasset_files(bd_stem: str) -> list[str]:
    """Find .uasset file(s) for a given BD stem in the legacy-assets tree."""
    results = []
    if LEGACY_ASSETS_DIR.exists():
        for ext in ('.uasset',):
            p = LEGACY_ASSETS_DIR / f'{bd_stem}{ext}'
            if p.exists():
                results.append(str(p))
    # Also note the relative game path
    game_path = f'Moria/Content/Tech/Data/Bubbles/GameWorldCatalog/{bd_stem}.uasset'
    results.append(game_path)
    return results


# ---------------------------------------------------------------------------
# Parse the removal spec
# ---------------------------------------------------------------------------
def parse_removal_spec(path: Path):
    """Parse removed_instances.txt into categorized entries."""
    global_type_rules = []      # type rules with no bubble scope
    bubble_type_rules = {}      # bubble_name -> [type_rule_strings]
    bubble_positions = {}       # bubble_name -> [position_entry_dicts]
    unknown_positions = []      # position entries with bubble="unknown"

    with open(path, 'r', encoding='utf-8') as f:
        for line_num, line in enumerate(f, 1):
            line = line.strip()
            if not line or line.startswith('#'):
                continue
            try:
                obj = json.loads(line)
            except json.JSONDecodeError:
                print(f'  WARN: skipping invalid JSON on line {line_num}')
                continue

            if 'typeRule' in obj:
                rule_val = obj['typeRule']
                if '|' in rule_val:
                    # Bubble-scoped type rule: "BubbleName | @MeshPattern"
                    parts = rule_val.split('|', 1)
                    bub = parts[0].strip()
                    rule = parts[1].strip()
                    bubble_type_rules.setdefault(bub, []).append(rule)
                else:
                    # Global type rule
                    global_type_rules.append(rule_val)

            elif 'mesh' in obj:
                bubble = obj.get('bubble', 'unknown')
                if bubble == 'unknown' or not bubble:
                    unknown_positions.append(obj)
                else:
                    bubble_positions.setdefault(bubble, []).append(obj)

    return global_type_rules, bubble_type_rules, bubble_positions, unknown_positions


# ---------------------------------------------------------------------------
# Resolve unknown bubble entries by searching FModel JSON exports
# ---------------------------------------------------------------------------
def resolve_unknowns(unknown_positions: list[dict], catalog_dir: Path,
                     tolerance: float = 200.0) -> dict:
    """
    For each unknown-bubble position entry, search all BD_BB_*.json files
    for a mesh name match.  Returns a dict of bd_stem -> [position_entries].
    """
    if not unknown_positions:
        return {}

    print(f'\n  Resolving {len(unknown_positions)} unknown-bubble entries...')

    # Extract mesh base names from unknowns
    unknown_meshes = set()
    for entry in unknown_positions:
        mesh_full = entry['mesh']
        mesh_base = mesh_full.split('-')[0]
        unknown_meshes.add(mesh_base)

    print(f'  Unique mesh base names to search: {len(unknown_meshes)}')

    # Scan each BD_BB file for these mesh names
    bd_mesh_presence = {}  # bd_stem -> set of mesh base names found
    json_files = sorted(catalog_dir.glob('BD_BB_*.json'))

    for jf in json_files:
        bd_stem = bd_stem_from_json_filename(jf.name)
        try:
            with open(jf, 'r', encoding='utf-8') as f:
                text = f.read()
        except Exception as e:
            print(f'  WARN: cannot read {jf.name}: {e}')
            continue

        found = set()
        for mesh_base in unknown_meshes:
            if mesh_base in text:
                found.add(mesh_base)

        if found:
            bd_mesh_presence[bd_stem] = found

    # Assign each unknown entry to matching bubble(s)
    resolved = {}  # bd_stem -> [position_entries]
    unresolved = []

    for entry in unknown_positions:
        mesh_full = entry['mesh']
        mesh_base = mesh_full.split('-')[0]

        matches = []
        for bd_stem, found_meshes in bd_mesh_presence.items():
            if mesh_base in found_meshes:
                matches.append(bd_stem)

        if matches:
            for bd_stem in matches:
                resolved.setdefault(bd_stem, []).append(entry)
        else:
            unresolved.append(entry)

    if unresolved:
        print(f'  WARNING: {len(unresolved)} entries could not be resolved:')
        for e in unresolved:
            print(f'    {e["mesh"][:60]}  world={e.get("world")}')

    # Summary
    total_placed = sum(len(v) for v in resolved.values())
    print(f'  Resolved {total_placed} entries across {len(resolved)} bubble(s)')

    return resolved


# ---------------------------------------------------------------------------
# Build and write per-bubble JSON files
# ---------------------------------------------------------------------------
def build_bubble_json(bubble_display_name: str,
                      bd_stem: str,
                      global_type_rules: list[str],
                      specific_type_rules: list[str],
                      position_entries: list[dict]) -> dict:
    """Construct the output JSON structure for one bubble."""
    uasset_files = find_uasset_files(bd_stem)

    output = {
        'bubble_name': bubble_display_name,
        'bd_stem': bd_stem,
        'uasset_files': uasset_files,
        'global_type_rules': [{'typeRule': r} for r in global_type_rules],
        'bubble_type_rules': [{'typeRule': f'{bubble_display_name} | {r}'}
                              for r in specific_type_rules],
        'position_entries': position_entries,
        'summary': {
            'global_type_rule_count': len(global_type_rules),
            'bubble_type_rule_count': len(specific_type_rules),
            'position_entry_count': len(position_entries),
            'total_entries': (len(global_type_rules)
                              + len(specific_type_rules)
                              + len(position_entries)),
        }
    }
    return output


def main():
    print('=' * 60)
    print('  Bubble Removal Spec Splitter')
    print('=' * 60)

    # Validate paths
    if not REMOVAL_SPEC.exists():
        print(f'ERROR: Removal spec not found: {REMOVAL_SPEC}')
        sys.exit(1)

    if not FMODEL_CATALOG_DIR.exists():
        print(f'ERROR: FModel catalog dir not found: {FMODEL_CATALOG_DIR}')
        sys.exit(1)

    BUBBLES_DIR.mkdir(parents=True, exist_ok=True)

    # Parse
    print(f'\nReading: {REMOVAL_SPEC}')
    (global_type_rules, bubble_type_rules,
     bubble_positions, unknown_positions) = parse_removal_spec(REMOVAL_SPEC)

    print(f'\n  Global type rules:          {len(global_type_rules)}')
    print(f'  Bubble-scoped type rules:   '
          f'{sum(len(v) for v in bubble_type_rules.values())} '
          f'across {len(bubble_type_rules)} bubble(s)')
    print(f'  Position entries (known):   '
          f'{sum(len(v) for v in bubble_positions.values())} '
          f'across {len(bubble_positions)} bubble(s)')
    print(f'  Position entries (unknown): {len(unknown_positions)}')

    # Resolve unknowns
    resolved_unknowns = resolve_unknowns(
        unknown_positions, FMODEL_CATALOG_DIR
    )

    # Collect all bubble names that need output files
    all_bubble_names = set()
    all_bubble_names.update(bubble_type_rules.keys())
    all_bubble_names.update(bubble_positions.keys())

    # For resolved unknowns, map BD stems back to display names
    # If we don't have a display name, use the BD stem as-is
    resolved_by_display = {}   # display_name -> [entries]
    for bd_stem, entries in resolved_unknowns.items():
        display_names = BD_TO_BUBBLE_NAMES.get(bd_stem)
        if display_names:
            # Use first display name
            name = display_names[0]
        else:
            # Derive a name from BD stem: BD_BB_Chapter2_GameStart -> Chapter2_GameStart
            name = bd_stem.replace('BD_BB_', '')
        resolved_by_display.setdefault(name, []).extend(entries)
        all_bubble_names.add(name)

    # Write output files
    print(f'\n  Writing {len(all_bubble_names)} bubble file(s) to: {BUBBLES_DIR}')
    print('-' * 60)

    files_written = 0
    for bubble_name in sorted(all_bubble_names):
        # Resolve BD stem
        bd_stem = BUBBLE_NAME_TO_BD.get(bubble_name)
        if not bd_stem:
            # Try treating bubble_name as a BD stem fragment
            candidate = f'BD_BB_{bubble_name}'
            json_path = FMODEL_CATALOG_DIR / f'{candidate}.json'
            if json_path.exists():
                bd_stem = candidate
            else:
                # Search for partial match
                for jf in FMODEL_CATALOG_DIR.glob('BD_BB_*.json'):
                    stem = bd_stem_from_json_filename(jf.name)
                    if bubble_name.lower().replace('_', '') in stem.lower().replace('_', ''):
                        bd_stem = stem
                        break
                if not bd_stem:
                    print(f'  WARN: No BD file mapping for "{bubble_name}" — '
                          f'using name as-is')
                    bd_stem = f'BD_BB_{bubble_name}'

        # Gather entries
        type_rules = bubble_type_rules.get(bubble_name, [])
        positions = bubble_positions.get(bubble_name, [])
        resolved_pos = resolved_by_display.get(bubble_name, [])

        # Merge resolved unknowns into position entries
        all_positions = positions + resolved_pos

        # Build output
        data = build_bubble_json(
            bubble_name, bd_stem,
            global_type_rules, type_rules, all_positions
        )

        # Mark resolved entries
        if resolved_pos:
            data['resolved_unknown_count'] = len(resolved_pos)

        # Write
        out_path = BUBBLES_DIR / f'{bubble_name}.json'
        with open(out_path, 'w', encoding='utf-8') as f:
            json.dump(data, f, indent=2)

        total = data['summary']['total_entries']
        print(f'  {bubble_name}.json  ({total} entries: '
              f'{data["summary"]["global_type_rule_count"]}g + '
              f'{data["summary"]["bubble_type_rule_count"]}t + '
              f'{data["summary"]["position_entry_count"]}p)')
        files_written += 1

    print(f'\n{"=" * 60}')
    print(f'  Done! {files_written} files written to {BUBBLES_DIR}')
    print(f'{"=" * 60}')


if __name__ == '__main__':
    main()
