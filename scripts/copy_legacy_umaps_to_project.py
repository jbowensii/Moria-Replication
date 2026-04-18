"""Copy legacy-format .umap/.uexp into the UE4 project Content directory.

Usage:
    python copy_legacy_umaps_to_project.py          # Dry run
    python copy_legacy_umaps_to_project.py --run     # Execute copy
"""
import argparse
import os
import shutil
import time
from pathlib import Path

SCRIPT_DIR = Path(__file__).parent
REPO_ROOT = SCRIPT_DIR.parent
CONTENT = REPO_ROOT / "project" / "Content"
LEGACY_DIR = REPO_ROOT / "tools" / "legacy-assets" / "Moria" / "Content"


def find_legacy_umaps():
    """Find all .umap files in legacy-assets."""
    results = []
    for root, dirs, files in os.walk(str(LEGACY_DIR)):
        for f in files:
            if not f.endswith(".umap"):
                continue
            full = os.path.join(root, f)
            rel = os.path.relpath(full, str(LEGACY_DIR)).replace("\\", "/")
            results.append((full, rel))
    return sorted(results, key=lambda x: x[1])


def main():
    parser = argparse.ArgumentParser(description="Copy legacy .umap files into UE4 project")
    parser.add_argument("--run", action="store_true", help="Execute (default: dry run)")
    args = parser.parse_args()

    if not LEGACY_DIR.exists():
        print(f"ERROR: Legacy assets not found at: {LEGACY_DIR}")
        print(f"  Run batch_decompile_blueprints.py --run first (retoc step)")
        exit(1)

    print("Finding legacy .umap files...")
    umaps = find_legacy_umaps()
    print(f"  {len(umaps)} .umap files found")

    uexp_count = 0
    for full_path, rel in umaps:
        uexp = full_path.rsplit(".", 1)[0] + ".uexp"
        if os.path.exists(uexp):
            uexp_count += 1

    total_files = len(umaps) + uexp_count
    print(f"  {uexp_count} have .uexp companions")
    print(f"  {total_files} total files to copy")

    if not args.run:
        print(f"\nDry run. Use --run to execute.")
        return

    print(f"\nCopying into {CONTENT}...")
    copied = 0
    errors = 0
    start = time.time()

    for i, (full_path, rel) in enumerate(umaps, 1):
        dst = CONTENT / rel
        dst.parent.mkdir(parents=True, exist_ok=True)
        try:
            shutil.copy2(full_path, str(dst))
            copied += 1
            uexp_src = full_path.rsplit(".", 1)[0] + ".uexp"
            if os.path.exists(uexp_src):
                uexp_dst = str(dst).rsplit(".", 1)[0] + ".uexp"
                shutil.copy2(uexp_src, uexp_dst)
                copied += 1
        except Exception as e:
            errors += 1
            if errors <= 10:
                print(f"  ERROR: {os.path.basename(rel)}: {e}")

        if i % 100 == 0 or i == len(umaps):
            print(f"  [{i:>4}/{len(umaps)}] {copied} files copied, {errors} errors")

    elapsed = time.time() - start
    print(f"\nDone in {elapsed:.1f}s -- {copied} files copied, {errors} errors")


if __name__ == "__main__":
    main()
