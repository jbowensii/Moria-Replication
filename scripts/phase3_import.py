#!/usr/bin/env python3
"""
Phase 3: Asset Import Automation for Moria Replication Project

Scans FModel JSON exports, categorizes them by asset type, and invokes
the BatchImport commandlet to import them into the UE4.27 editor project.

Usage:
    python phase3_import.py                    # Scan and show summary only
    python phase3_import.py --import           # Import all DataTables (recommended first step)
    python phase3_import.py --import --all     # Import all asset types
    python phase3_import.py --import --type Texture  # Import specific type
    python phase3_import.py --save             # Auto-save after import
    python phase3_import.py --dry-run          # Show what would be imported without importing

Requirements:
    - UE4.27 installed at C:\\Program Files\\Epic Games\\UE_4.27
    - Project built (run UBT first if needed)
    - FModel exports at tools/fmodel-export/Exports/
"""

import argparse
import json
import os
import subprocess
import sys
from collections import Counter, defaultdict
from pathlib import Path

# Paths (relative to this script)
SCRIPT_DIR = Path(__file__).parent
REPO_ROOT = SCRIPT_DIR.parent
PROJECT_FILE = REPO_ROOT / "project" / "Moria.uproject"
EXPORTS_DIR = REPO_ROOT / "tools" / "fmodel-export" / "Exports"
UE4_EDITOR_CMD = Path(r"C:\Program Files\Epic Games\UE_4.27\Engine\Binaries\Win64\UE4Editor-Cmd.exe")

# Priority order for asset types (DataTables first — needed for build menu injection)
IMPORT_PRIORITY = [
    "DataTable",
    "CurveTable",
    "CurveFloat",
    "CurveLinearColor",
    "StringTable",
    "DataAsset",
    "Material",
    "MaterialInstanceConstant",
    "Texture2D",
    "TextureCube",
    "SubsurfaceProfile",
    "PhysicalMaterial",
    "SoundCue",
    "SoundWave",
    "NiagaraSystem",
    "NiagaraEmitter",
    "SkeletalMesh",
    "StaticMesh",
    "Skeleton",
    "AnimSequence",
    "AnimMontage",
    "AnimBlueprint",
    "WidgetBlueprint",
    "Blueprint",
]


def scan_exports(exports_dir: Path) -> dict:
    """Scan all JSON files and categorize by asset type."""
    type_to_files = defaultdict(list)
    errors = []

    json_files = list(exports_dir.rglob("*.json"))
    print(f"Scanning {len(json_files)} JSON files...")

    for json_file in json_files:
        try:
            with open(json_file, "r", encoding="utf-8") as f:
                first_chunk = f.read(2048)

            # Extract Type via regex (fast, avoids full JSON parse of large files)
            import re
            match = re.search(r'"Type"\s*:\s*"([^"]+)"', first_chunk)
            if match:
                type_to_files[match.group(1)].append(str(json_file))
            else:
                type_to_files["Unknown"].append(str(json_file))
        except Exception as e:
            errors.append((str(json_file), str(e)))

    return dict(type_to_files), errors


def print_summary(type_to_files: dict, errors: list):
    """Print a summary table of discovered assets."""
    print("\n" + "=" * 60)
    print("  FModel Export Summary")
    print("=" * 60)

    total = sum(len(files) for files in type_to_files.values())
    print(f"  Total JSON files: {total}")
    if errors:
        print(f"  Parse errors: {len(errors)}")
    print()

    # Sort by priority, then alphabetically for unlisted types
    priority_set = set(IMPORT_PRIORITY)
    sorted_types = []
    for t in IMPORT_PRIORITY:
        if t in type_to_files:
            sorted_types.append(t)
    for t in sorted(type_to_files.keys()):
        if t not in priority_set:
            sorted_types.append(t)

    print(f"  {'Asset Type':<35} {'Count':>6}  Priority")
    print(f"  {'-' * 35} {'-' * 6}  {'-' * 8}")
    for asset_type in sorted_types:
        count = len(type_to_files[asset_type])
        priority = ""
        if asset_type in priority_set:
            idx = IMPORT_PRIORITY.index(asset_type)
            if idx == 0:
                priority = "HIGH"
            elif idx < 5:
                priority = "medium"
            else:
                priority = "low"
        print(f"  {asset_type:<35} {count:>6}  {priority}")

    print(f"\n  {'TOTAL':<35} {total:>6}")
    print("=" * 60)


def run_batch_import(exports_dir: Path, filter_type: str = None, save: bool = False):
    """Run the UE4 BatchImport commandlet."""
    if not UE4_EDITOR_CMD.exists():
        print(f"ERROR: UE4Editor-Cmd.exe not found at: {UE4_EDITOR_CMD}")
        sys.exit(1)

    if not PROJECT_FILE.exists():
        print(f"ERROR: Project file not found at: {PROJECT_FILE}")
        sys.exit(1)

    cmd = [
        str(UE4_EDITOR_CMD),
        str(PROJECT_FILE),
        "-run=BatchImport",
        f"-dir={exports_dir}",
        "-project=Moria",
    ]

    if filter_type:
        cmd.append(f"-filter={filter_type}")

    if save:
        cmd.append("-save")

    # UE4 commandlet flags
    cmd.extend(["-unattended", "-nosplash", "-nullrhi"])

    print(f"\nRunning commandlet:")
    print(f"  {' '.join(cmd)}")
    print()

    result = subprocess.run(cmd, capture_output=False)
    return result.returncode


def main():
    parser = argparse.ArgumentParser(description="Phase 3: Import FModel JSON exports into UE4 editor")
    parser.add_argument("--import", dest="do_import", action="store_true",
                        help="Run the import (default: scan only)")
    parser.add_argument("--all", action="store_true",
                        help="Import all asset types (default: DataTables only)")
    parser.add_argument("--type", type=str, default=None,
                        help="Import only assets of this type (e.g., DataTable, Texture2D)")
    parser.add_argument("--save", action="store_true",
                        help="Auto-save imported assets to disk")
    parser.add_argument("--dry-run", action="store_true",
                        help="Show what would be imported without importing")
    parser.add_argument("--exports-dir", type=str, default=None,
                        help=f"Override exports directory (default: {EXPORTS_DIR})")
    args = parser.parse_args()

    exports_dir = Path(args.exports_dir) if args.exports_dir else EXPORTS_DIR

    if not exports_dir.exists():
        print(f"ERROR: Exports directory not found: {exports_dir}")
        print("Run FModel export first, or specify --exports-dir")
        sys.exit(1)

    # Scan and summarize
    type_to_files, errors = scan_exports(exports_dir)
    print_summary(type_to_files, errors)

    if not args.do_import and not args.dry_run:
        print("\nTo import assets, run with --import flag:")
        print("  python phase3_import.py --import              # DataTables only (recommended)")
        print("  python phase3_import.py --import --all        # All asset types")
        print("  python phase3_import.py --import --type X     # Specific type")
        return

    # Determine filter
    filter_type = None
    if args.type:
        filter_type = args.type
    elif not args.all:
        filter_type = "DataTable"
        print(f"\nDefaulting to DataTable imports only. Use --all for everything.")

    if filter_type:
        count = len(type_to_files.get(filter_type, []))
        print(f"\nWill import {count} {filter_type} assets.")
    else:
        total = sum(len(f) for f in type_to_files.values())
        print(f"\nWill import all {total} assets.")

    if args.dry_run:
        target_files = type_to_files.get(filter_type, []) if filter_type else []
        if not filter_type:
            for files in type_to_files.values():
                target_files.extend(files) if isinstance(target_files, list) else None
        print(f"\n[DRY RUN] Would import {len(target_files) if isinstance(target_files, list) else 'all'} files.")
        if filter_type and filter_type in type_to_files:
            for f in type_to_files[filter_type][:20]:
                rel = os.path.relpath(f, exports_dir)
                print(f"  {rel}")
            if len(type_to_files[filter_type]) > 20:
                print(f"  ... and {len(type_to_files[filter_type]) - 20} more")
        return

    # Run the import
    print(f"\nStarting import...")
    exit_code = run_batch_import(exports_dir, filter_type, args.save)

    if exit_code == 0:
        print("\nImport completed successfully!")
    else:
        print(f"\nImport completed with some failures (exit code: {exit_code})")

    sys.exit(exit_code)


if __name__ == "__main__":
    main()
