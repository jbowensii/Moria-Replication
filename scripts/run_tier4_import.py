"""Stage and import remaining Tier 4 assets (AnimMontage, BlendSpace, etc.)

Stages missing JSON files then runs the BatchImport commandlet in batches.
BlendSpace/BlendSpace1D/AimOffsetBlendSpace1D are already fully imported,
so this primarily handles the remaining AnimMontage assets.

Usage:
    python run_tier4_import.py              # Dry run -- show what's missing
    python run_tier4_import.py --run        # Execute import
"""
import argparse
import json
import os
import shutil
import subprocess
import sys
import time
from pathlib import Path
from collections import defaultdict

SCRIPT_DIR = Path(__file__).parent
REPO_ROOT = SCRIPT_DIR.parent
CLOUD_BT = REPO_ROOT / "tools" / "cloud-exports-by-type"
CLOUD = REPO_ROOT / "tools" / "cloud-exports"
CONTENT = REPO_ROOT / "project" / "Content"
BATCH_DIR = REPO_ROOT / "tools" / "batch-import-tier4"
TEMP_BASE = REPO_ROOT / "tools" / "batch-import-temp-tier4"
UPROJECT = REPO_ROOT / "project" / "Moria.uproject"
UE4_CMD = Path(r"C:\Program Files\Epic Games\UE_4.27\Engine\Binaries\Win64\UE4Editor-Cmd.exe")
LOG_FILE = REPO_ROOT / "tools" / "tier4-import-log.json"

BATCH_SIZE = 150

TIER4_TYPES = [
    "AnimMontage",
    "BlendSpace",
    "BlendSpace1D",
    "AimOffsetBlendSpace1D",
]


def get_content_set():
    """Get set of all asset paths already in project."""
    content_str = str(CONTENT.resolve()).replace("/", "\\")
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


def stage_missing(content_set):
    """Stage missing tier 4 JSON files for batch import."""
    if BATCH_DIR.exists():
        # Use cmd rmdir to handle OneDrive locks
        import subprocess as _sp
        _sp.run(["cmd", "/c", "rmdir", "/s", "/q", str(BATCH_DIR)],
                capture_output=True, timeout=30)
        if BATCH_DIR.exists():
            shutil.rmtree(BATCH_DIR, ignore_errors=True)

    total = 0
    by_type = defaultdict(int)

    for type_name in TIER4_TYPES:
        type_dir = CLOUD_BT / type_name
        if not type_dir.exists():
            continue

        for jp in type_dir.rglob("*.json"):
            rel = os.path.relpath(jp, type_dir).replace("\\", "/")
            game_path = rel.rsplit(".", 1)[0]

            if game_path in content_set:
                continue

            # Prefer cloud-exports source (has full path structure)
            src = CLOUD / (game_path + ".json")
            if not src.exists():
                src = jp

            dst = BATCH_DIR / "Moria" / "Content" / (game_path + ".json")
            dst.parent.mkdir(parents=True, exist_ok=True)
            try:
                os.link(str(src), str(dst))
            except OSError:
                shutil.copy2(str(src), str(dst))

            total += 1
            by_type[type_name] += 1

    return total, dict(by_type)


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
    result = {"batch": batch_num, "file_count": file_count}

    try:
        with open(batch_log, "w", encoding="utf-8", errors="replace") as log_fh:
            proc = subprocess.run(
                cmd, timeout=timeout_seconds,
                stdout=log_fh, stderr=subprocess.STDOUT,
                text=True, errors="replace",
            )
        elapsed = time.time() - start
        result["exit_code"] = proc.returncode
        result["elapsed_seconds"] = round(elapsed, 1)

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
        except Exception:
            pass

        s = result.get("success", "?")
        f_count = result.get("failed", "?")
        if result.get("completed"):
            print(f"  Done -- {elapsed:.0f}s  (success: {s}, failed: {f_count})")
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
    parser = argparse.ArgumentParser(description="Stage and import Tier 4 assets")
    parser.add_argument("--run", action="store_true", help="Execute (default: dry run)")
    parser.add_argument("--timeout", type=int, default=600)
    args = parser.parse_args()

    print("Building content index...")
    content_set = get_content_set()
    print(f"  {len(content_set)} assets in project")

    print("\nStaging missing Tier 4 assets...")
    total, by_type = stage_missing(content_set)

    print(f"\nStaged {total} JSON files in {BATCH_DIR}")
    for t, c in sorted(by_type.items(), key=lambda x: -x[1]):
        print(f"  {t}: {c}")

    if total == 0:
        print("\nAll Tier 4 assets are already imported!")
        return

    if not args.run:
        print(f"\nDry run. Use --run to execute.")
        return

    if not UE4_CMD.exists():
        print(f"ERROR: UE4Editor-Cmd.exe not found at: {UE4_CMD}")
        sys.exit(1)

    # Collect staged files and batch them
    staged_root = BATCH_DIR / "Moria" / "Content"
    all_files = sorted(staged_root.rglob("*.json"))

    batches = []
    for i in range(0, len(all_files), BATCH_SIZE):
        batches.append(all_files[i:i + BATCH_SIZE])

    print(f"\n{'#'*65}")
    print(f"  STARTING TIER 4 IMPORT -- {len(batches)} batch(es), {total} files")
    print(f"  Close the UE4 editor before proceeding!")
    print(f"{'#'*65}")

    TEMP_BASE.mkdir(parents=True, exist_ok=True)
    results = []
    total_success = 0
    total_failed = 0
    overall_start = time.time()

    for i, batch in enumerate(batches, 1):
        batch_dir = TEMP_BASE / f"batch_{i:04d}"
        if batch_dir.exists():
            shutil.rmtree(batch_dir)

        for src in batch:
            rel = os.path.relpath(src, staged_root).replace("\\", "/")
            dst = batch_dir / "Moria" / "Content" / rel
            dst.parent.mkdir(parents=True, exist_ok=True)
            try:
                os.link(str(src), str(dst))
            except OSError:
                shutil.copy2(str(src), str(dst))

        try:
            result = run_commandlet(batch_dir, i, len(batches), args.timeout)
            results.append(result)
            total_success += result.get("success", 0)
            total_failed += result.get("failed", 0)
        finally:
            if batch_dir.exists():
                shutil.rmtree(batch_dir, ignore_errors=True)

    overall_elapsed = time.time() - overall_start

    print(f"\n{'='*65}")
    print(f"  TIER 4 IMPORT COMPLETE -- {overall_elapsed/60:.1f} minutes")
    print(f"{'='*65}")
    print(f"  Assets success: {total_success}")
    print(f"  Assets failed:  {total_failed}")
    print(f"{'='*65}")

    with open(LOG_FILE, "w") as f:
        json.dump({
            "total_success": total_success,
            "total_failed": total_failed,
            "results": results,
        }, f, indent=2)
    print(f"\nLog: {LOG_FILE}")


if __name__ == "__main__":
    main()
