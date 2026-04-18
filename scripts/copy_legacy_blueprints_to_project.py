"""Copy legacy-format Blueprint .uasset/.uexp into the UE4 project Content directory.

Replaces the IoStore-format cooked copies with proper legacy-format files
that the UE4.27 editor can actually read.

Usage:
    python copy_legacy_blueprints_to_project.py          # Dry run
    python copy_legacy_blueprints_to_project.py --run     # Execute copy
"""
import argparse
import os
import shutil
import subprocess
import sys
import time
from pathlib import Path

SCRIPT_DIR = Path(__file__).parent
REPO_ROOT = SCRIPT_DIR.parent
CONTENT = REPO_ROOT / "project" / "Content"
LEGACY_DIR = REPO_ROOT / "tools" / "legacy-assets" / "Moria" / "Content"

BP_PREFIXES = ("BP_", "WBP_", "ABP_")


def find_legacy_blueprints():
    """Find all Blueprint .uasset files in legacy-assets."""
    results = []
    for root, dirs, files in os.walk(str(LEGACY_DIR)):
        for f in files:
            if not f.endswith(".uasset"):
                continue
            name = f.rsplit(".", 1)[0]
            if not any(name.startswith(p) for p in BP_PREFIXES):
                continue
            full = os.path.join(root, f)
            rel = os.path.relpath(full, str(LEGACY_DIR)).replace("\\", "/")
            results.append((full, rel))
    return sorted(results, key=lambda x: x[1])


def main():
    parser = argparse.ArgumentParser(description="Copy legacy Blueprints into UE4 project")
    parser.add_argument("--run", action="store_true", help="Execute (default: dry run)")
    args = parser.parse_args()

    if not LEGACY_DIR.exists():
        print(f"ERROR: Legacy assets not found at: {LEGACY_DIR}")
        print(f"  Run batch_decompile_blueprints.py --run first")
        sys.exit(1)

    print("Finding legacy Blueprint assets...")
    blueprints = find_legacy_blueprints()
    print(f"  {len(blueprints)} Blueprint .uasset files found")

    if not blueprints:
        print("Nothing to copy!")
        return

    # Count how many have .uexp companions
    uexp_count = 0
    for full_path, rel in blueprints:
        uexp = full_path.rsplit(".", 1)[0] + ".uexp"
        if os.path.exists(uexp):
            uexp_count += 1

    print(f"  {uexp_count} have .uexp companions")
    total_files = len(blueprints) + uexp_count
    print(f"  {total_files} total files to copy (.uasset + .uexp)")

    if not args.run:
        print(f"\nDry run. Use --run to execute.")
        return

    print(f"\nCopying legacy Blueprints into {CONTENT}...")
    copied = 0
    errors = 0
    start = time.time()

    for i, (full_path, rel) in enumerate(blueprints, 1):
        dst_uasset = CONTENT / rel
        dst_uasset.parent.mkdir(parents=True, exist_ok=True)

        try:
            # Copy .uasset (overwrite IoStore version)
            shutil.copy2(full_path, str(dst_uasset))
            copied += 1

            # Copy .uexp if it exists
            uexp_src = full_path.rsplit(".", 1)[0] + ".uexp"
            if os.path.exists(uexp_src):
                uexp_dst = str(dst_uasset).rsplit(".", 1)[0] + ".uexp"
                shutil.copy2(uexp_src, uexp_dst)
                copied += 1
        except Exception as e:
            errors += 1
            if errors <= 10:
                name = os.path.basename(rel)
                print(f"  ERROR: {name}: {e}")

        if i % 500 == 0 or i == len(blueprints):
            print(f"  [{i:>5}/{len(blueprints)}] {copied} files copied, {errors} errors")

    elapsed = time.time() - start
    print(f"\nDone in {elapsed:.1f}s -- {copied} files copied, {errors} errors")


if __name__ == "__main__":
    main()
