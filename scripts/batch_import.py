#!/usr/bin/env python3
"""
Batch Import via UE4 Commandlet -- Automated Batched Import

Splits cloud-exported JSON files into small batches, creates temporary
directories with correct FModel path structure (Moria/Content/...),
and runs the BatchImport commandlet on each batch.

If a batch crashes (GC thread issue), logs it and moves to next batch.
Already-imported assets (.uasset files) are skipped automatically.

Usage:
    python batch_import.py                         # Dry run -- show plan
    python batch_import.py --run                   # Execute all batches
    python batch_import.py --run --batch-size 100  # Smaller batches
    python batch_import.py --run --category Art    # Only one category
    python batch_import.py --run --start-batch 5   # Resume from batch 5
    python batch_import.py --status                # Show what's imported
"""

import argparse
import json
import os
import shutil
import subprocess
import sys
import time
from collections import defaultdict
from pathlib import Path

# -- Paths ------------------------------------------------------------------
SCRIPT_DIR = Path(__file__).parent
REPO_ROOT = SCRIPT_DIR.parent
CLOUD_EXPORTS = REPO_ROOT / "tools" / "cloud-exports"
CONTENT_DIR = REPO_ROOT / "project" / "Content"
TEMP_BASE = REPO_ROOT / "tools" / "batch-import-temp"
UPROJECT = REPO_ROOT / "project" / "Moria.uproject"
UE4_CMD = Path(r"C:\Program Files\Epic Games\UE_4.27\Engine\Binaries\Win64\UE4Editor-Cmd.exe")
LOG_FILE = REPO_ROOT / "tools" / "batch-import-log.json"

BATCH_SIZE_DEFAULT = 150


# -- Fast discovery using os.walk -------------------------------------------

def _fast_find(directory: Path, extension: str = ".json") -> list:
    """Fast recursive file listing. Uses PowerShell Get-ChildItem which is
    much faster than Python os.walk on OneDrive/network drives."""
    dir_str = str(directory).replace("/", "\\")
    try:
        # PowerShell Get-ChildItem is fast and handles recursion correctly
        ps_cmd = (
            f"Get-ChildItem -Path '{dir_str}' -Filter '*{extension}' "
            f"-Recurse -File | ForEach-Object {{ $_.FullName }}"
        )
        result = subprocess.run(
            ["powershell", "-NoProfile", "-Command", ps_cmd],
            capture_output=True, text=True, errors="replace", timeout=300
        )
        files = [line.strip() for line in result.stdout.splitlines() if line.strip()]
        if files:
            return files
    except Exception:
        pass

    # Fallback to os.walk
    print("  (Using os.walk fallback - may be slow on OneDrive)", flush=True)
    files = []
    for dirpath, _, filenames in os.walk(directory):
        for fn in filenames:
            if fn.endswith(extension):
                files.append(os.path.join(dirpath, fn))
    return files


def discover_json_files(cloud_dir: Path, category: str = None) -> dict:
    """Find all JSON files grouped by top-level category."""
    categories = defaultdict(list)
    scan_dir = cloud_dir / category if category else cloud_dir

    if not scan_dir.exists():
        return {}

    cloud_str = str(cloud_dir).replace("\\", "/")
    files = _fast_find(scan_dir, ".json")

    for full in files:
        full_norm = full.replace("\\", "/")
        if cloud_str in full_norm:
            rel = full_norm[len(cloud_str):].lstrip("/")
        else:
            rel = os.path.relpath(full, cloud_str).replace("\\", "/")
        parts = rel.split("/")
        cat = parts[0] if len(parts) > 1 else "_root"
        categories[cat].append(Path(full))

    total = sum(len(v) for v in categories.values())
    print(f"  Found {total} JSON files in {len(categories)} categories")
    return dict(categories)


def get_imported_assets(content_dir: Path) -> set:
    """Find .uasset files already in project Content directory."""
    imported = set()
    if not content_dir.exists():
        return imported

    content_str = str(content_dir).replace("\\", "/")
    files = _fast_find(content_dir, ".uasset")

    for full in files:
        full_norm = full.replace("\\", "/")
        if content_str in full_norm:
            rel = full_norm[len(content_str):].lstrip("/")
        else:
            rel = os.path.relpath(full, content_str).replace("\\", "/")
        game_path = rel.rsplit(".", 1)[0]
        imported.add(game_path)

    return imported


def filter_already_imported(json_files: list, cloud_dir: Path, imported: set) -> list:
    """Remove files whose assets already exist in the project."""
    cloud_str = str(cloud_dir)
    remaining = []
    for f in json_files:
        rel = os.path.relpath(str(f), cloud_str)
        game_path = rel.replace("\\", "/").rsplit(".", 1)[0]
        if game_path not in imported:
            remaining.append(f)
    return remaining


# -- Batch creation ---------------------------------------------------------

def create_batch_dir(batch_files: list, cloud_dir: Path, batch_dir: Path):
    """Create a temp directory with Moria/Content/ structure for a batch."""
    if batch_dir.exists():
        shutil.rmtree(batch_dir)

    cloud_str = str(cloud_dir)
    for src_file in batch_files:
        rel = os.path.relpath(str(src_file), cloud_str)
        dst = batch_dir / "Moria" / "Content" / rel
        dst.parent.mkdir(parents=True, exist_ok=True)
        try:
            os.link(str(src_file), str(dst))
        except OSError:
            shutil.copy2(str(src_file), str(dst))


def cleanup_batch_dir(batch_dir: Path):
    """Remove temporary batch directory."""
    if batch_dir.exists():
        shutil.rmtree(batch_dir, ignore_errors=True)


# -- Commandlet execution ---------------------------------------------------

def run_commandlet(batch_dir: Path, batch_num: int, total_batches: int,
                   timeout_seconds: int = 600, **kwargs) -> dict:
    """Run the UE4 BatchImport commandlet on a batch directory."""
    # Use Windows-style paths for UE4
    batch_dir_win = str(batch_dir).replace("/", "\\")
    uproject_win = str(UPROJECT).replace("/", "\\")

    # Write output to a log file (UE4 logs go through its own system, not stdout)
    batch_log = batch_dir.parent / f"batch_{batch_num:04d}.log"

    cmd = [
        str(UE4_CMD),
        uproject_win,
        "-run=BatchImport",
        f"-dir={batch_dir_win}",
        "-project=Moria",
        "-save",
        "-unattended",
        "-nosplash",
        "-nopause",
        "-log",
    ]

    # Cloud mode: enable Cloud Server for auto-downloading textures/meshes
    # No-cloud mode: use -nullrhi for faster headless import
    if kwargs.get("cloud"):
        cmd.append("-cloud")
    else:
        cmd.append("-nullrhi")

    file_count = sum(1 for _ in batch_dir.rglob("*.json"))
    print(f"\n{'='*65}")
    print(f"  Batch {batch_num}/{total_batches} -- {file_count} files")
    print(f"{'='*65}")

    start = time.time()
    result = {
        "batch": batch_num,
        "start_time": time.strftime("%H:%M:%S"),
        "file_count": file_count,
    }

    try:
        with open(batch_log, "w", encoding="utf-8", errors="replace") as log_fh:
            proc = subprocess.run(
                cmd,
                timeout=timeout_seconds,
                stdout=log_fh,
                stderr=subprocess.STDOUT,
                text=True,
                errors="replace",
            )
        elapsed = time.time() - start
        result["exit_code"] = proc.returncode
        result["elapsed_seconds"] = round(elapsed, 1)

        # Parse the log file for stats
        try:
            with open(batch_log, "r", encoding="utf-8", errors="replace") as f:
                for line in f:
                    if "BatchImport Complete" in line:
                        result["completed"] = True
                    if "Success:" in line and "BatchImport" not in line:
                        try:
                            result["success"] = int(line.strip().split()[-1])
                        except (ValueError, IndexError):
                            pass
                    if "Failed:" in line and "Success" not in line:
                        try:
                            result["failed"] = int(line.strip().split()[-1])
                        except (ValueError, IndexError):
                            pass
                    if "Saved" in line and "packages" in line:
                        try:
                            result["saved_packages"] = int(line.strip().split("Saved")[1].split()[0])
                        except (ValueError, IndexError):
                            pass
        except Exception:
            pass

        s = result.get("success", "?")
        f_count = result.get("failed", "?")
        saved = result.get("saved_packages", "?")

        if result.get("completed"):
            print(f"  Done -- {elapsed:.0f}s  (success: {s}, failed: {f_count}, saved: {saved} pkgs)")
        else:
            print(f"  CRASHED -- exit code {proc.returncode} after {elapsed:.0f}s")
            print(f"  (Assets saved before crash are preserved)")
            print(f"  Log: {batch_log}")

    except subprocess.TimeoutExpired:
        elapsed = time.time() - start
        result["exit_code"] = -1
        result["elapsed_seconds"] = round(elapsed, 1)
        result["timeout"] = True
        print(f"  TIMEOUT after {timeout_seconds}s")

    return result


# -- Status -----------------------------------------------------------------

def show_status(cloud_dir: Path, content_dir: Path):
    """Show import progress."""
    print("Scanning cloud exports...")
    categories = discover_json_files(cloud_dir)
    print("Scanning imported assets...")
    imported = get_imported_assets(content_dir)

    total_json = 0
    total_imported = 0

    print(f"\n{'='*65}")
    print(f"  Import Status")
    print(f"{'='*65}")
    print(f"  {'Category':<25} {'JSON':>6} {'Done':>6} {'Left':>6}")
    print(f"  {'-'*25} {'-'*6} {'-'*6} {'-'*6}")

    for cat in sorted(categories.keys()):
        files = categories[cat]
        remaining = filter_already_imported(files, cloud_dir, imported)
        done = len(files) - len(remaining)
        total_json += len(files)
        total_imported += done

        tag = " DONE" if not remaining else ""
        print(f"  {cat:<25} {len(files):>6} {done:>6} {len(remaining):>6}{tag}")

    print(f"  {'-'*25} {'-'*6} {'-'*6} {'-'*6}")
    print(f"  {'TOTAL':<25} {total_json:>6} {total_imported:>6} {total_json - total_imported:>6}")
    print(f"{'='*65}")

    if total_json > 0:
        print(f"\n  Progress: {total_imported / total_json * 100:.1f}%")


# -- Main -------------------------------------------------------------------

def main():
    parser = argparse.ArgumentParser(description="Batch import JSON assets via UE4 commandlet")
    parser.add_argument("--run", action="store_true", help="Execute imports (dry run without this)")
    parser.add_argument("--batch-size", type=int, default=BATCH_SIZE_DEFAULT,
                        help=f"Files per batch (default: {BATCH_SIZE_DEFAULT})")
    parser.add_argument("--category", type=str, default=None,
                        help="Import only this category (e.g., Art, Items, UI)")
    parser.add_argument("--start-batch", type=int, default=1,
                        help="Start from this batch number (for resuming)")
    parser.add_argument("--timeout", type=int, default=600,
                        help="Timeout per batch in seconds (default: 600)")
    parser.add_argument("--status", action="store_true", help="Show import progress")
    parser.add_argument("--no-skip", action="store_true",
                        help="Don't skip already-imported assets")
    parser.add_argument("--cloud", action="store_true",
                        help="Enable Cloud Server (auto-downloads textures/meshes)")
    args = parser.parse_args()

    # Validate
    if not CLOUD_EXPORTS.exists():
        print(f"ERROR: Cloud exports not found at: {CLOUD_EXPORTS}")
        sys.exit(1)

    if args.status:
        show_status(CLOUD_EXPORTS, CONTENT_DIR)
        return

    if args.run:
        if not UE4_CMD.exists():
            print(f"ERROR: UE4Editor-Cmd.exe not found at: {UE4_CMD}")
            sys.exit(1)
        if not UPROJECT.exists():
            print(f"ERROR: .uproject not found at: {UPROJECT}")
            sys.exit(1)

    # Discover
    print(f"Scanning cloud exports...")
    categories = discover_json_files(CLOUD_EXPORTS, args.category)

    if args.category and args.category not in categories:
        print(f"ERROR: Category '{args.category}' not found.")
        avail = discover_json_files(CLOUD_EXPORTS)
        print(f"Available: {', '.join(sorted(avail.keys()))}")
        sys.exit(1)

    # Get imported assets for skip logic
    imported = set()
    if not args.no_skip:
        print(f"Scanning already-imported assets...")
        imported = get_imported_assets(CONTENT_DIR)
        print(f"  Already imported: {len(imported)} assets")

    # Build file list
    all_files = []
    for cat in sorted(categories.keys()):
        all_files.extend(categories[cat])

    total = len(all_files)
    print(f"\nTotal JSON files: {total}")

    # Filter
    if imported:
        all_files = filter_already_imported(all_files, CLOUD_EXPORTS, imported)
        skipped = total - len(all_files)
        print(f"Skipping {skipped} already-imported, {len(all_files)} remaining")

    if not all_files:
        print("\nNothing to import -- all done!")
        return

    # Sort for deterministic batching
    all_files.sort(key=lambda f: str(f))

    # Create batches
    batches = []
    for i in range(0, len(all_files), args.batch_size):
        batches.append(all_files[i:i + args.batch_size])

    # Show plan
    print(f"\nBatch plan: {len(batches)} batches x {args.batch_size} max")
    for i, batch in enumerate(batches, 1):
        cats = defaultdict(int)
        for f in batch:
            rel = os.path.relpath(str(f), str(CLOUD_EXPORTS))
            parts = rel.replace("\\", "/").split("/")
            cats[parts[0] if len(parts) > 1 else "_root"] += 1
        summary = ", ".join(f"{c}:{n}" for c, n in sorted(cats.items()))
        mark = " <-- resume" if i == args.start_batch and args.start_batch > 1 else ""
        print(f"  Batch {i:>3}: {len(batch):>4} files  ({summary}){mark}")

    if not args.run:
        print(f"\nDry run. To execute:")
        print(f"  python batch_import.py --run")
        if args.category:
            print(f"  python batch_import.py --run --category {args.category}")
        return

    # ---- Execute ----
    print(f"\n{'#'*65}")
    print(f"  STARTING BATCH IMPORT -- {len(batches)} batches")
    print(f"  Close the UE4 editor before proceeding!")
    print(f"{'#'*65}")

    results = []
    total_success = 0
    total_failed = 0
    total_crashed = 0
    overall_start = time.time()

    for i, batch in enumerate(batches, 1):
        if i < args.start_batch:
            continue

        batch_dir = TEMP_BASE / f"batch_{i:04d}"
        create_batch_dir(batch, CLOUD_EXPORTS, batch_dir)

        try:
            result = run_commandlet(batch_dir, i, len(batches), args.timeout, cloud=args.cloud)
            results.append(result)

            total_success += result.get("success", 0)
            total_failed += result.get("failed", 0)
            if result.get("exit_code", -1) != 0:
                total_crashed += 1

        finally:
            cleanup_batch_dir(batch_dir)

        # Save progress
        log_data = {
            "last_batch": i,
            "total_batches": len(batches),
            "total_success": total_success,
            "total_failed": total_failed,
            "total_crashed": total_crashed,
            "results": results,
        }
        with open(LOG_FILE, "w") as f:
            json.dump(log_data, f, indent=2)

    overall_elapsed = time.time() - overall_start

    print(f"\n{'='*65}")
    print(f"  BATCH IMPORT COMPLETE -- {overall_elapsed/60:.1f} minutes")
    print(f"{'='*65}")
    print(f"  Batches run:     {len(results)}")
    print(f"  Batches crashed: {total_crashed}")
    print(f"  Assets success:  {total_success}")
    print(f"  Assets failed:   {total_failed}")
    print(f"{'='*65}")
    print(f"\nLog: {LOG_FILE}")
    print(f"Check status: python batch_import.py --status")


if __name__ == "__main__":
    main()
