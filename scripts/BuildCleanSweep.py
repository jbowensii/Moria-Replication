#!/usr/bin/env python3
"""
BuildCleanSweep.py — Batch-process ALL per-bubble removal specs into one mod pak.

Reads every .json file in project/bubbles/, groups them by uasset file,
runs the UAssetAPI removal engine on each, then packages everything into
a single IoStore mod pak called "CleanSweep".

Pipeline per uasset:
  1. UAssetGUI tojson  →  UAssetAPI JSON
  2. Merge all bubble specs that share this uasset
  3. Apply removals (type rules + position entries)
  4. UAssetGUI fromjson →  modified .uasset/.uexp
  5. Stage modified files

Final packaging:
  retoc to-zen  →  IoStore .pak/.ucas/.utoc
  zip to Downloads/CleanSweep.zip

Usage:
    python scripts/BuildCleanSweep.py
"""

import json
import os
import shutil
import subprocess
import sys
import zipfile
from pathlib import Path

# ---------------------------------------------------------------------------
# Paths
# ---------------------------------------------------------------------------
SCRIPT_DIR = Path(__file__).resolve().parent
PROJECT_ROOT = SCRIPT_DIR.parent

BUBBLES_DIR = PROJECT_ROOT / 'bubbles'
CLEANSWEEP_DIR = PROJECT_ROOT / 'cleansweep'
STAGING_DIR = CLEANSWEEP_DIR / 'staging'
DOWNLOADS_DIR = Path(os.path.expanduser('~/Downloads'))

LEGACY_ASSETS_DIR = PROJECT_ROOT / 'tools' / 'legacy-assets'
RETOC_EXE = PROJECT_ROOT / 'tools' / 'retoc' / 'bin' / 'retoc.exe'
UASSETGUI_EXE = PROJECT_ROOT / 'tools' / 'UAssetGUI' / 'UAssetGUI.exe'

UE_VERSION = 'VER_UE4_27'       # for UAssetGUI tojson/fromjson
RETOC_VERSION = 'UE4_27'        # for retoc to-zen (no VER_ prefix)

CLEANSWEEP_VERSION = '2.5.1'    # Mod version — update on each release

# Import the removal engine from bubble_data_remover
sys.path.insert(0, str(SCRIPT_DIR))
from bubble_data_remover import (
    apply_removals_uasset,
    count_uasset_objects,
    COORD_EPSILON,
)

# Game content path prefix for retoc staging
GAME_CONTENT_PREFIX = Path('Moria') / 'Content' / 'Tech' / 'Data' / 'Bubbles' / 'GameWorldCatalog'


# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------

def log(msg):
    print(msg)


def run_uassetgui_tojson(uasset_path: Path, json_output: Path):
    """Convert .uasset to UAssetAPI JSON using UAssetGUI."""
    cmd = [
        str(UASSETGUI_EXE), 'tojson',
        str(uasset_path),
        str(json_output),
        UE_VERSION,
    ]
    log(f"    UAssetGUI tojson: {uasset_path.name}")
    result = subprocess.run(cmd, capture_output=True, text=True, timeout=60)
    if result.returncode != 0:
        log(f"    ERROR: UAssetGUI tojson failed (exit={result.returncode})")
        log(f"    stderr: {result.stderr[:500]}")
        return False
    return True


def run_uassetgui_fromjson(json_path: Path, uasset_output: Path):
    """Convert UAssetAPI JSON back to .uasset/.uexp using UAssetGUI."""
    cmd = [
        str(UASSETGUI_EXE), 'fromjson',
        str(json_path),
        str(uasset_output),
        UE_VERSION,
    ]
    log(f"    UAssetGUI fromjson: {json_path.name}")
    result = subprocess.run(cmd, capture_output=True, text=True, timeout=60)
    if result.returncode != 0:
        log(f"    ERROR: UAssetGUI fromjson failed (exit={result.returncode})")
        log(f"    stderr: {result.stderr[:500]}")
        return False
    return True


def run_retoc_tozen(staging_dir: Path, output_dir: Path, pak_name: str):
    """Package staged files into IoStore pak using retoc to-zen.

    retoc syntax: retoc to-zen --version UE4_27 <INPUT_DIR> <OUTPUT_UTOC>
    NEVER use --override-container-header-version (causes ACCESS_VIOLATION crash).
    """
    output_utoc = output_dir / f'{pak_name}.utoc'
    cmd = [
        str(RETOC_EXE), 'to-zen', '-v',
        '--version', RETOC_VERSION,
        str(staging_dir),
        str(output_utoc),
    ]
    log(f"\n  retoc to-zen: {pak_name}")
    result = subprocess.run(cmd, capture_output=True, text=True, timeout=300)
    if result.stdout:
        for line in result.stdout.strip().split('\n')[-5:]:
            log(f"  [retoc] {line}")
    if result.stderr:
        for line in result.stderr.strip().split('\n')[-5:]:
            log(f"  [retoc] {line}")
    if result.returncode != 0:
        log(f"  ERROR: retoc to-zen failed (exit={result.returncode})")
        return False
    return True


# ---------------------------------------------------------------------------
# Main build
# ---------------------------------------------------------------------------

def parse_bubble_json(bubble_json_path: Path):
    """Parse a per-bubble JSON file and extract removal entries."""
    with open(bubble_json_path, 'r', encoding='utf-8') as f:
        data = json.load(f)

    bd_stem = data.get('bd_stem', '')
    bubble_name = data.get('bubble_name', '')

    # Parse type rules
    type_rules = []
    for tr in data.get('global_type_rules', []):
        rule_val = tr.get('typeRule', '')
        mesh_name = rule_val.split('-')[0]
        type_rules.append({
            'mesh_name': mesh_name,
            'bubble': None,
            'raw': rule_val,
        })

    for tr in data.get('bubble_type_rules', []):
        rule_val = tr.get('typeRule', '')
        # Format: "BubbleName | @MeshPattern" or "BubbleName | MeshPattern"
        if '|' in rule_val:
            mesh_part = rule_val.split('|', 1)[1].strip()
            if mesh_part.startswith('@'):
                mesh_part = mesh_part[1:]
            mesh_name = mesh_part.split('-')[0]
        else:
            mesh_name = rule_val.split('-')[0]
        type_rules.append({
            'mesh_name': mesh_name,
            'bubble': bubble_name,
            'raw': rule_val,
        })

    # Parse position entries
    position_entries = []
    for pe in data.get('position_entries', []):
        mesh_name = pe.get('mesh', '').split('-')[0]
        local = pe.get('local', [0, 0, 0])
        position_entries.append({
            'mesh_name': mesh_name,
            'bubble': pe.get('bubble', bubble_name),
            'local': local,
            'raw': pe.get('mesh', ''),
        })

    return bd_stem, bubble_name, type_rules, position_entries


def main():
    print('=' * 70)
    print('  CleanSweep Mod Builder')
    print('  Batch-processes all bubble removal specs into one IoStore mod pak')
    print('=' * 70)

    # Validate paths
    if not BUBBLES_DIR.exists():
        log(f'ERROR: Bubbles directory not found: {BUBBLES_DIR}')
        log('  Run SeparateBubbleData.py first to create per-bubble JSON files.')
        sys.exit(1)

    if not UASSETGUI_EXE.exists():
        log(f'ERROR: UAssetGUI not found: {UASSETGUI_EXE}')
        sys.exit(1)

    if not RETOC_EXE.exists():
        log(f'ERROR: retoc not found: {RETOC_EXE}')
        sys.exit(1)

    if not LEGACY_ASSETS_DIR.exists():
        log(f'ERROR: Legacy assets not found: {LEGACY_ASSETS_DIR}')
        sys.exit(1)

    # Clean and create working directories
    if CLEANSWEEP_DIR.exists():
        # Use cmd /c rmdir on Windows to avoid OneDrive permission locks
        if os.name == 'nt':
            os.system(f'cmd /c "rmdir /s /q {CLEANSWEEP_DIR}"')
            import time
            # Wait for OneDrive to release the directory
            for _ in range(10):
                if not CLEANSWEEP_DIR.exists():
                    break
                time.sleep(1)
        else:
            shutil.rmtree(CLEANSWEEP_DIR)
    CLEANSWEEP_DIR.mkdir(parents=True, exist_ok=True)
    STAGING_DIR.mkdir(parents=True)

    # Stage directory needs game content path structure for retoc
    game_path = STAGING_DIR / GAME_CONTENT_PREFIX
    game_path.mkdir(parents=True, exist_ok=True)

    # -----------------------------------------------------------------------
    # Phase 1: Read all bubble JSON files and group by BD stem
    # -----------------------------------------------------------------------
    log(f'\nPhase 1: Reading bubble specs from {BUBBLES_DIR}')

    bubble_files = sorted(BUBBLES_DIR.glob('*.json'))
    log(f'  Found {len(bubble_files)} bubble file(s)')

    # Group: bd_stem -> { type_rules: [...], position_entries: [...], bubble_names: [] }
    by_uasset = {}

    for bf in bubble_files:
        bd_stem, bubble_name, type_rules, position_entries = parse_bubble_json(bf)

        if bd_stem not in by_uasset:
            by_uasset[bd_stem] = {
                'type_rules': [],
                'position_entries': [],
                'bubble_names': [],
            }

        entry = by_uasset[bd_stem]
        entry['bubble_names'].append(bubble_name)

        # Merge type rules (deduplicate by mesh_name)
        existing_type_meshes = {tr['mesh_name'] for tr in entry['type_rules']}
        for tr in type_rules:
            if tr['mesh_name'] not in existing_type_meshes:
                entry['type_rules'].append(tr)
                existing_type_meshes.add(tr['mesh_name'])

        # Merge position entries (no dedup — coordinates differ)
        entry['position_entries'].extend(position_entries)

    log(f'  Grouped into {len(by_uasset)} unique uasset file(s)')

    # -----------------------------------------------------------------------
    # Phase 2: Process each uasset
    # -----------------------------------------------------------------------
    log(f'\nPhase 2: Processing uassets')

    total_removed = 0
    processed_count = 0
    skipped_count = 0

    for bd_stem, spec in sorted(by_uasset.items()):
        # Find the legacy .uasset file
        uasset_rel = Path('Moria') / 'Content' / 'Tech' / 'Data' / 'Bubbles' / 'GameWorldCatalog' / f'{bd_stem}.uasset'
        uasset_path = LEGACY_ASSETS_DIR / uasset_rel

        if not uasset_path.exists():
            log(f'\n  SKIP: {bd_stem} — uasset not found at {uasset_path}')
            skipped_count += 1
            continue

        bubbles_str = ', '.join(spec['bubble_names'][:3])
        if len(spec['bubble_names']) > 3:
            bubbles_str += f' +{len(spec["bubble_names"]) - 3} more'

        log(f'\n  {bd_stem}  ({bubbles_str})')
        log(f'    Rules: {len(spec["type_rules"])} type, '
            f'{len(spec["position_entries"])} position')

        # Step 1: tojson
        work_dir = CLEANSWEEP_DIR / bd_stem
        work_dir.mkdir(parents=True, exist_ok=True)

        json_path = work_dir / f'{bd_stem}.json'
        if not run_uassetgui_tojson(uasset_path, json_path):
            skipped_count += 1
            continue

        # Step 2: Load and apply removals
        with open(json_path, 'r', encoding='utf-8') as f:
            uasset_data = json.load(f)

        before = count_uasset_objects(uasset_data)

        stats = apply_removals_uasset(
            uasset_data,
            spec['type_rules'],
            spec['position_entries'],
            log_fn=log,
        )

        after = count_uasset_objects(uasset_data)

        log(f'    Removed: {stats.total} objects '
            f'(IM:{stats.instanced_mesh} IB:{stats.instanced_breakable} '
            f'CC:{stats.construction} DV:{stats.deco_volume} ATT:{stats.attachment})')
        log(f'    Before: {sum(before)}  After: {sum(after)}')

        if stats.total == 0:
            log(f'    SKIP: No removals applied')
            skipped_count += 1
            continue

        total_removed += stats.total

        # Step 3: Save modified JSON
        modified_json = work_dir / f'{bd_stem}_modified.json'
        with open(modified_json, 'w', encoding='utf-8') as f:
            json.dump(uasset_data, f, indent=2)

        # Step 4: fromjson — write directly to staging directory
        staged_uasset = game_path / f'{bd_stem}.uasset'
        if not run_uassetgui_fromjson(modified_json, staged_uasset):
            skipped_count += 1
            continue

        # Verify both .uasset and .uexp were created in staging
        staged_uexp = game_path / f'{bd_stem}.uexp'
        if not staged_uasset.exists():
            log(f'    ERROR: .uasset not created')
            skipped_count += 1
            continue
        if not staged_uexp.exists():
            log(f'    ERROR: .uexp not created')
            skipped_count += 1
            continue

        log(f'    Staged: {staged_uasset.stat().st_size/1024:.0f} KB .uasset + '
            f'{staged_uexp.stat().st_size/1024:.0f} KB .uexp')

        processed_count += 1

    # -----------------------------------------------------------------------
    # Phase 3: Package with retoc
    # -----------------------------------------------------------------------
    log(f'\n{"=" * 70}')
    log(f'Phase 3: Packaging')
    log(f'  Processed: {processed_count} uassets')
    log(f'  Skipped:   {skipped_count}')
    log(f'  Total removed: {total_removed} objects')

    if processed_count == 0:
        log('\n  ERROR: No uassets were successfully processed. Nothing to package.')
        sys.exit(1)

    # Run retoc
    output_dir = CLEANSWEEP_DIR / 'output'
    output_dir.mkdir(parents=True, exist_ok=True)

    if not run_retoc_tozen(STAGING_DIR, output_dir, 'CleanSweep_P'):
        log('  ERROR: retoc packaging failed!')
        sys.exit(1)

    # -----------------------------------------------------------------------
    # Phase 4: Zip to Downloads
    # -----------------------------------------------------------------------
    log(f'\nPhase 4: Creating zip')

    zip_path = DOWNLOADS_DIR / f'CleanSweep_v{CLEANSWEEP_VERSION}.zip'
    pak_files = list(output_dir.glob('*'))

    with zipfile.ZipFile(zip_path, 'w', zipfile.ZIP_DEFLATED) as zf:
        for pf in pak_files:
            zf.write(pf, pf.name)
            log(f'  Added: {pf.name} ({pf.stat().st_size / 1024:.1f} KB)')

    log(f'\n{"=" * 70}')
    log(f'  CleanSweep mod built successfully!')
    log(f'  {processed_count} bubble data files modified')
    log(f'  {total_removed} total objects removed')
    log(f'  Output: {zip_path}')
    log(f'{"=" * 70}')


if __name__ == '__main__':
    main()
