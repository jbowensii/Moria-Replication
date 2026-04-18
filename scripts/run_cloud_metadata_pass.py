"""Cloud Tools metadata pass: import SkeletalMesh + DestructibleMesh via Cloud Server.

These JSON exports contain metadata (material slots, sockets, LOD settings, physics)
that gets applied to mesh assets. Requires the Cloud Server running at localhost:1500.

Remaining: ~15 SkeletalMesh + ~1,307 DestructibleMesh

Usage:
    python run_cloud_metadata_pass.py                   # Dry run
    python run_cloud_metadata_pass.py --run             # Execute (Cloud Server must be running)
    python run_cloud_metadata_pass.py --run --start-batch 5  # Resume from batch 5
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
BATCH_DIR = REPO_ROOT / "tools" / "batch-import-cloud-metadata"
TEMP_BASE = REPO_ROOT / "tools" / "batch-import-temp-cloud"
UPROJECT = REPO_ROOT / "project" / "Moria.uproject"
UE4_CMD = Path(r"C:\Program Files\Epic Games\UE_4.27\Engine\Binaries\Win64\UE4Editor-Cmd.exe")
CLOUD_SERVER = REPO_ROOT / "tools" / "JsonAsAssetServer" / "Core.exe"
LOG_FILE = REPO_ROOT / "tools" / "cloud-metadata-import-log.json"

BATCH_SIZE = 100  # Smaller batches — cloud imports are heavier (downloads textures/meshes)

# Asset types that need Cloud Server for metadata
CLOUD_METADATA_TYPES = [
    "SkeletalMesh",
    "DestructibleMesh",
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
    """Stage missing cloud metadata JSON files for batch import."""
    if BATCH_DIR.exists():
        # Use cmd rmdir to handle OneDrive locks
        import subprocess as _sp
        _sp.run(["cmd", "/c", "rmdir", "/s", "/q", str(BATCH_DIR)],
                capture_output=True, timeout=30)
        if BATCH_DIR.exists():
            shutil.rmtree(BATCH_DIR, ignore_errors=True)

    total = 0
    by_type = defaultdict(int)

    for type_name in CLOUD_METADATA_TYPES:
        type_dir = CLOUD_BT / type_name
        if not type_dir.exists():
            print(f"  WARNING: {type_dir} not found, skipping {type_name}")
            continue

        for jp in type_dir.rglob("*.json"):
            rel = os.path.relpath(jp, type_dir).replace("\\", "/")
            game_path = rel.rsplit(".", 1)[0]

            if game_path in content_set:
                continue

            # Prefer cloud-exports source
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


def check_cloud_server():
    """Check if the Cloud Server is reachable."""
    import urllib.request
    try:
        resp = urllib.request.urlopen("http://localhost:1500/api/status", timeout=5)
        return resp.status == 200
    except Exception:
        pass
    # Try a simple TCP connect
    import socket
    try:
        s = socket.create_connection(("localhost", 1500), timeout=3)
        s.close()
        return True
    except Exception:
        return False


def run_commandlet(batch_dir, batch_num, total_batches, timeout_seconds=900):
    """Run the UE4 BatchImport commandlet with Cloud Server enabled."""
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
        "-cloud",           # Enable Cloud Server for mesh/texture downloads
        "-unattended",
        "-nosplash",
        "-nopause",
        "-log",
        # Note: NOT using -nullrhi — cloud imports may need rendering context
    ]

    file_count = sum(1 for _ in batch_dir.rglob("*.json"))
    print(f"\n{'='*65}")
    print(f"  Batch {batch_num}/{total_batches} -- {file_count} files (cloud mode)")
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
            print(f"  (Assets saved before crash are preserved)")
            print(f"  Log: {batch_log}")

    except subprocess.TimeoutExpired:
        elapsed = time.time() - start
        result["exit_code"] = -1
        result["elapsed_seconds"] = round(elapsed, 1)
        result["timeout"] = True
        print(f"  TIMEOUT after {timeout_seconds}s")

    return result


def main():
    parser = argparse.ArgumentParser(description="Cloud Tools metadata pass for mesh assets")
    parser.add_argument("--run", action="store_true", help="Execute (default: dry run)")
    parser.add_argument("--start-batch", type=int, default=1, help="Resume from batch N")
    parser.add_argument("--batch-size", type=int, default=BATCH_SIZE)
    parser.add_argument("--timeout", type=int, default=900,
                        help="Timeout per batch in seconds (default: 900, cloud is slower)")
    args = parser.parse_args()

    print("Building content index...")
    content_set = get_content_set()
    print(f"  {len(content_set)} assets in project")

    print("\nStaging missing cloud metadata assets...")
    total, by_type = stage_missing(content_set)

    print(f"\nStaged {total} JSON files in {BATCH_DIR}")
    for t, c in sorted(by_type.items(), key=lambda x: -x[1]):
        print(f"  {t}: {c}")

    if total == 0:
        print("\nAll cloud metadata assets are already imported!")
        return

    # Create batches from staged files
    staged_root = BATCH_DIR / "Moria" / "Content"
    all_files = sorted(staged_root.rglob("*.json"))

    batches = []
    for i in range(0, len(all_files), args.batch_size):
        batches.append(all_files[i:i + args.batch_size])

    print(f"\nBatch plan: {len(batches)} batches x {args.batch_size} max")
    for i, batch in enumerate(batches, 1):
        mark = " <-- resume" if i == args.start_batch and args.start_batch > 1 else ""
        print(f"  Batch {i:>3}: {len(batch):>4} files{mark}")

    if not args.run:
        print(f"\nDry run. To execute:")
        print(f"  1. Start Cloud Server: tools\\JsonAsAssetServer\\Core.exe")
        print(f"  2. Close UE4 Editor")
        print(f"  3. python run_cloud_metadata_pass.py --run")
        return

    # Validate prerequisites
    if not UE4_CMD.exists():
        print(f"ERROR: UE4Editor-Cmd.exe not found at: {UE4_CMD}")
        sys.exit(1)
    if not UPROJECT.exists():
        print(f"ERROR: .uproject not found at: {UPROJECT}")
        sys.exit(1)

    print("\nChecking Cloud Server...")
    if not check_cloud_server():
        print(f"ERROR: Cloud Server not reachable at localhost:1500")
        print(f"  Start it first: {CLOUD_SERVER}")
        sys.exit(1)
    print("  Cloud Server is running.")

    print(f"\n{'#'*65}")
    print(f"  STARTING CLOUD METADATA IMPORT -- {len(batches)} batches")
    print(f"  Close the UE4 editor before proceeding!")
    print(f"{'#'*65}")

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
            if not result.get("completed"):
                total_crashed += 1
        finally:
            if batch_dir.exists():
                shutil.rmtree(batch_dir, ignore_errors=True)

        # Save progress after each batch
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
    print(f"  CLOUD METADATA IMPORT COMPLETE -- {overall_elapsed/60:.1f} minutes")
    print(f"{'='*65}")
    print(f"  Batches run:     {len(results)}")
    print(f"  Batches crashed: {total_crashed}")
    print(f"  Assets success:  {total_success}")
    print(f"  Assets failed:   {total_failed}")
    print(f"{'='*65}")
    print(f"\nLog: {LOG_FILE}")


if __name__ == "__main__":
    main()
