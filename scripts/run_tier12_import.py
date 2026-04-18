"""Run BatchImport commandlet on pre-staged tier 1+2+3 JSONs.

Splits the staged files into batches and runs the commandlet per batch,
recovering from crashes by moving to the next batch.

Usage:
    python run_tier12_import.py              # Dry run
    python run_tier12_import.py --run        # Execute
    python run_tier12_import.py --run --start-batch 5  # Resume
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

SCRIPT_DIR = Path(__file__).parent
REPO_ROOT = SCRIPT_DIR.parent
STAGED_DIR = REPO_ROOT / "tools" / "batch-import-tier12"
TEMP_BASE = REPO_ROOT / "tools" / "batch-import-temp-tier12"
CONTENT_DIR = REPO_ROOT / "project" / "Content"
UPROJECT = REPO_ROOT / "project" / "Moria.uproject"
UE4_CMD = Path(r"C:\Program Files\Epic Games\UE_4.27\Engine\Binaries\Win64\UE4Editor-Cmd.exe")
LOG_FILE = REPO_ROOT / "tools" / "tier12-import-log.json"

BATCH_SIZE = 150


def get_content_set():
    """Get set of all asset paths already in project."""
    content_str = str(CONTENT_DIR.resolve())
    ps_cmd = (
        f"Get-ChildItem -Path '{content_str}' -Filter '*.uasset' "
        f"-Recurse -File | ForEach-Object {{ $_.FullName }}"
    )
    result = subprocess.run(
        ["powershell", "-NoProfile", "-Command", ps_cmd],
        capture_output=True, text=True, errors="replace", timeout=300
    )
    paths = set()
    for f in result.stdout.splitlines():
        f = f.strip()
        if f:
            rel = os.path.relpath(f, content_str).replace("\\", "/")
            paths.add(rel.rsplit(".", 1)[0])
    return paths


def collect_staged_files():
    """Collect all JSON files from the staged directory."""
    staged_root = STAGED_DIR / "Moria" / "Content"
    files = []
    for jp in staged_root.rglob("*.json"):
        rel = os.path.relpath(jp, staged_root).replace("\\", "/")
        game_path = rel.rsplit(".", 1)[0]
        files.append((game_path, jp))
    return sorted(files, key=lambda x: x[0])


def create_batch_dir(file_pairs, batch_dir):
    """Create a temp directory with Moria/Content/ structure for a batch."""
    if batch_dir.exists():
        shutil.rmtree(batch_dir)

    for game_path, src_file in file_pairs:
        dst = batch_dir / "Moria" / "Content" / (game_path + ".json")
        dst.parent.mkdir(parents=True, exist_ok=True)
        try:
            os.link(str(src_file), str(dst))
        except OSError:
            shutil.copy2(str(src_file), str(dst))


def run_commandlet(batch_dir, batch_num, total_batches, timeout_seconds=600):
    """Run the UE4 BatchImport commandlet on a batch directory."""
    batch_dir_win = str(batch_dir).replace("/", "\\")
    uproject_win = str(UPROJECT).replace("/", "\\")
    batch_log = TEMP_BASE / f"batch_{batch_num:04d}.log"

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
        "-nullrhi",
        "-log",
    ]

    file_count = sum(1 for _ in batch_dir.rglob("*.json"))
    print(f"\n{'='*65}")
    print(f"  Batch {batch_num}/{total_batches} -- {file_count} files")
    print(f"{'='*65}", flush=True)

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

        # Parse log for stats
        try:
            with open(batch_log, "r", encoding="utf-8", errors="replace") as f:
                for line in f:
                    if "BatchImport Complete" in line:
                        result["completed"] = True
                    elif "Success:" in line and "LogJsonAsAsset" in line:
                        try:
                            result["success"] = int(line.strip().split()[-1])
                        except (ValueError, IndexError):
                            pass
                    elif "Failed:" in line and "LogJsonAsAsset" in line:
                        try:
                            result["failed"] = int(line.strip().split()[-1])
                        except (ValueError, IndexError):
                            pass
                    elif "Saved" in line and "packages" in line and "LogJsonAsAsset" in line:
                        try:
                            result["saved_packages"] = int(line.split("Saved")[1].split()[0])
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
            print(f"  Log: {batch_log}")

    except subprocess.TimeoutExpired:
        elapsed = time.time() - start
        result["exit_code"] = -1
        result["elapsed_seconds"] = round(elapsed, 1)
        result["timeout"] = True
        print(f"  TIMEOUT after {timeout_seconds}s")

    return result


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--run", action="store_true")
    parser.add_argument("--start-batch", type=int, default=1)
    parser.add_argument("--batch-size", type=int, default=BATCH_SIZE)
    parser.add_argument("--timeout", type=int, default=600)
    args = parser.parse_args()

    if not STAGED_DIR.exists():
        print(f"ERROR: Staged directory not found: {STAGED_DIR}")
        sys.exit(1)

    # Collect all staged files
    print("Collecting staged files...")
    all_files = collect_staged_files()
    print(f"  Total staged: {len(all_files)}")

    # Skip already imported
    print("Checking already-imported assets...")
    content_set = get_content_set()
    remaining = [(gp, jp) for gp, jp in all_files if gp not in content_set]
    print(f"  Already imported: {len(all_files) - len(remaining)}")
    print(f"  Remaining: {len(remaining)}")

    if not remaining:
        print("\nAll staged assets are already imported!")
        return

    # Create batches
    batches = []
    for i in range(0, len(remaining), args.batch_size):
        batches.append(remaining[i:i + args.batch_size])

    print(f"\nBatch plan: {len(batches)} batches x {args.batch_size} max")

    if not args.run:
        print("\nDry run. Use --run to execute.")
        return

    # Execute
    TEMP_BASE.mkdir(parents=True, exist_ok=True)

    results = []
    total_success = 0
    total_failed = 0
    total_crashed = 0
    overall_start = time.time()

    for i, batch in enumerate(batches, 1):
        if i < args.start_batch:
            continue

        batch_dir = TEMP_BASE / f"batch_{i:04d}"
        create_batch_dir(batch, batch_dir)

        try:
            result = run_commandlet(batch_dir, i, len(batches), args.timeout)
            results.append(result)
            total_success += result.get("success", 0)
            total_failed += result.get("failed", 0)
            if not result.get("completed"):
                total_crashed += 1
        finally:
            if batch_dir.exists():
                shutil.rmtree(batch_dir, ignore_errors=True)

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


if __name__ == "__main__":
    main()
