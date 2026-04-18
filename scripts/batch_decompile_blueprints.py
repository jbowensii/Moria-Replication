"""Batch decompile all Blueprint uassets to Kismet pseudocode (.kms).

Pipeline:
  1. retoc to-legacy: converts IoStore .uasset -> legacy .uasset/.uexp
  2. KismetKompiler decompile: legacy .uasset -> .kms pseudocode

Output goes to decompiled/ at repo root (excluded from UE4 editor, included in git).

Usage:
    python batch_decompile_blueprints.py                  # Dry run
    python batch_decompile_blueprints.py --run             # Full decompile
    python batch_decompile_blueprints.py --run --skip-retoc # Skip retoc if legacy already built
    python batch_decompile_blueprints.py --run --filter "BP_Kitchen"  # Filter by name
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
CONTENT = REPO_ROOT / "project" / "Content"
DECOMPILED_DIR = REPO_ROOT / "decompiled"
LEGACY_DIR = REPO_ROOT / "tools" / "legacy-assets"
RETOC = REPO_ROOT / "tools" / "retoc" / "retoc.exe"
KISMET = REPO_ROOT / "tools" / "KismetKompiler" / "KismetKompiler.exe"
GAME_PAKS = Path(r"C:\Program Files\Epic Games\ReturnToMoria\Moria\Content\Paks")
LOG_FILE = REPO_ROOT / "tools" / "decompile-log.json"

# Blueprint prefixes we copied as cooked uassets
BP_PREFIXES = ("BP_", "WBP_", "ABP_")


def find_blueprint_uassets():
    """Find all Blueprint .uasset files in the project Content directory."""
    content_str = str(CONTENT.resolve()).replace("/", "\\")
    ps_cmd = (
        f"Get-ChildItem -Path '{content_str}' -Filter '*.uasset' "
        f"-Recurse -File | ForEach-Object {{ $_.FullName }}"
    )
    result = subprocess.run(
        ["powershell", "-NoProfile", "-Command", ps_cmd],
        capture_output=True, text=True, errors="replace", timeout=300
    )
    blueprints = []
    for f in result.stdout.splitlines():
        f = f.strip()
        if not f:
            continue
        name = os.path.basename(f).rsplit(".", 1)[0]
        if any(name.startswith(p) for p in BP_PREFIXES):
            rel = os.path.relpath(f, content_str).replace("\\", "/")
            blueprints.append(rel)
    return sorted(blueprints)


def run_retoc(filter_str=None):
    """Convert IoStore assets to legacy format using retoc."""
    if LEGACY_DIR.exists():
        print(f"  Cleaning {LEGACY_DIR}...")
        subprocess.run(["cmd", "/c", "rmdir", "/s", "/q", str(LEGACY_DIR)],
                        capture_output=True, timeout=60)
        if LEGACY_DIR.exists():
            shutil.rmtree(LEGACY_DIR, ignore_errors=True)

    LEGACY_DIR.mkdir(parents=True, exist_ok=True)

    cmd = [
        str(RETOC),
        "to-legacy",
        "--version", "UE4_27",
        "--no-shaders",
        "--no-script-objects",
        str(GAME_PAKS),
        str(LEGACY_DIR),
    ]
    if filter_str:
        cmd.insert(-2, "-f")
        cmd.insert(-2, filter_str)

    print(f"\n  Running retoc to-legacy...")
    print(f"  Input:  {GAME_PAKS}")
    print(f"  Output: {LEGACY_DIR}")
    if filter_str:
        print(f"  Filter: {filter_str}")

    start = time.time()
    result = subprocess.run(
        cmd, capture_output=True, text=True, errors="replace", timeout=3600
    )
    elapsed = time.time() - start

    # Parse retoc output
    output = result.stdout + result.stderr
    print(f"  retoc completed in {elapsed:.0f}s")
    for line in output.splitlines():
        if "Extracted" in line or "failed" in line:
            print(f"  {line.strip()}")

    return result.returncode


def find_legacy_blueprints(filter_str=None):
    """Find all Blueprint .uasset files in the legacy-assets directory."""
    if not LEGACY_DIR.exists():
        return []

    legacy_content = LEGACY_DIR / "Moria" / "Content"
    if not legacy_content.exists():
        # Try flat structure
        legacy_content = LEGACY_DIR

    blueprints = []
    for root, dirs, files in os.walk(str(legacy_content)):
        for f in files:
            if not f.endswith(".uasset"):
                continue
            name = f.rsplit(".", 1)[0]
            if not any(name.startswith(p) for p in BP_PREFIXES):
                continue
            if filter_str and filter_str.lower() not in name.lower():
                continue
            full = os.path.join(root, f)
            rel = os.path.relpath(full, str(legacy_content)).replace("\\", "/")
            blueprints.append((full, rel))

    return sorted(blueprints, key=lambda x: x[1])


def decompile_blueprint(uasset_path, rel_path):
    """Decompile a single Blueprint .uasset to .kms using KismetKompiler."""
    name = os.path.basename(rel_path).rsplit(".", 1)[0]
    # Mirror directory structure in decompiled/
    kms_rel = rel_path.rsplit(".", 1)[0] + ".kms"
    kms_path = DECOMPILED_DIR / kms_rel

    kms_path.parent.mkdir(parents=True, exist_ok=True)

    cmd = [
        str(KISMET),
        "decompile",
        "-v", "4.27",
        "--no-verify",
        "--no-strict",
        "-i", str(uasset_path),
        "-o", str(kms_path),
        "-f",  # Overwrite
    ]

    try:
        result = subprocess.run(
            cmd, capture_output=True, text=True, errors="replace", timeout=60
        )
        if result.returncode == 0 and kms_path.exists():
            return "ok"
        else:
            # Check if file was created despite non-zero exit
            if kms_path.exists() and kms_path.stat().st_size > 0:
                return "ok"
            error = (result.stdout + result.stderr).strip()
            # Compact the error
            for line in error.split("\n"):
                if "Exception" in line or "Error" in line:
                    return f"error: {line.strip()[:200]}"
            return f"error: exit code {result.returncode}"
    except subprocess.TimeoutExpired:
        return "error: timeout"
    except Exception as e:
        return f"error: {str(e)[:200]}"


def convert_kms_to_utf8(kms_path):
    """Convert KismetKompiler's UTF-16 output to UTF-8 for git-friendliness."""
    try:
        with open(kms_path, "r", encoding="utf-16") as f:
            content = f.read()
        with open(kms_path, "w", encoding="utf-8") as f:
            f.write(content)
        return True
    except Exception:
        return False


def main():
    parser = argparse.ArgumentParser(description="Batch decompile Blueprints to Kismet pseudocode")
    parser.add_argument("--run", action="store_true", help="Execute (default: dry run)")
    parser.add_argument("--skip-retoc", action="store_true", help="Skip retoc conversion (use existing legacy-assets)")
    parser.add_argument("--filter", type=str, default=None, help="Filter Blueprint names")
    parser.add_argument("--no-utf8", action="store_true", help="Keep UTF-16 output (default: convert to UTF-8)")
    args = parser.parse_args()

    # Validate tools
    if not RETOC.exists():
        print(f"ERROR: retoc not found at: {RETOC}")
        sys.exit(1)
    if not KISMET.exists():
        print(f"ERROR: KismetKompiler not found at: {KISMET}")
        sys.exit(1)
    if not GAME_PAKS.exists():
        print(f"ERROR: Game paks not found at: {GAME_PAKS}")
        sys.exit(1)

    print("Finding Blueprint uassets in project...")
    project_bps = find_blueprint_uassets()
    print(f"  {len(project_bps)} Blueprint uassets in project")

    if not args.run:
        by_prefix = defaultdict(int)
        for bp in project_bps:
            name = os.path.basename(bp).rsplit(".", 1)[0]
            prefix = name.split("_")[0] + "_"
            by_prefix[prefix] += 1
        for p, c in sorted(by_prefix.items(), key=lambda x: -x[1]):
            print(f"    {p}: {c}")

        print(f"\nPipeline:")
        print(f"  1. retoc to-legacy: IoStore -> legacy .uasset/.uexp")
        print(f"  2. KismetKompiler: legacy .uasset -> .kms pseudocode")
        print(f"  3. UTF-16 -> UTF-8 conversion for git")
        print(f"\nOutput: {DECOMPILED_DIR}/")
        print(f"\nDry run. Use --run to execute.")
        return

    # Step 1: Convert IoStore -> legacy
    if not args.skip_retoc:
        print("\n" + "=" * 65)
        print("  STEP 1: retoc to-legacy (IoStore -> legacy format)")
        print("=" * 65)
        retoc_rc = run_retoc(filter_str=args.filter)
    else:
        print("\n  Skipping retoc (--skip-retoc), using existing legacy-assets/")

    # Step 2: Find legacy Blueprints
    print("\n  Finding legacy Blueprint uassets...")
    legacy_bps = find_legacy_blueprints(filter_str=args.filter)
    print(f"  {len(legacy_bps)} Blueprint .uasset files found in legacy-assets/")

    if not legacy_bps:
        print("\nNo Blueprint uassets to decompile!")
        return

    # Step 3: Decompile
    print("\n" + "=" * 65)
    print(f"  STEP 2: KismetKompiler decompile ({len(legacy_bps)} Blueprints)")
    print("=" * 65)

    DECOMPILED_DIR.mkdir(parents=True, exist_ok=True)

    results = {"ok": 0, "error": 0, "errors": []}
    overall_start = time.time()

    for i, (full_path, rel_path) in enumerate(legacy_bps, 1):
        name = os.path.basename(rel_path).rsplit(".", 1)[0]
        status = decompile_blueprint(full_path, rel_path)

        if status == "ok":
            results["ok"] += 1
            # Convert to UTF-8
            if not args.no_utf8:
                kms_rel = rel_path.rsplit(".", 1)[0] + ".kms"
                kms_path = DECOMPILED_DIR / kms_rel
                convert_kms_to_utf8(kms_path)
        else:
            results["error"] += 1
            results["errors"].append({"name": name, "path": rel_path, "status": status})

        # Progress every 100
        if i % 100 == 0 or i == len(legacy_bps):
            elapsed = time.time() - overall_start
            rate = i / elapsed if elapsed > 0 else 0
            eta = (len(legacy_bps) - i) / rate if rate > 0 else 0
            print(f"  [{i:>5}/{len(legacy_bps)}] ok={results['ok']} err={results['error']} "
                  f"({rate:.1f}/s, ETA {eta:.0f}s)")

    overall_elapsed = time.time() - overall_start

    print(f"\n{'=' * 65}")
    print(f"  DECOMPILATION COMPLETE -- {overall_elapsed / 60:.1f} minutes")
    print(f"{'=' * 65}")
    print(f"  Blueprints decompiled: {results['ok']}")
    print(f"  Blueprints failed:     {results['error']}")
    print(f"  Output:                {DECOMPILED_DIR}/")
    print(f"{'=' * 65}")

    if results["errors"]:
        print(f"\nFailed Blueprints ({len(results['errors'])}):")
        for err in results["errors"][:20]:
            print(f"  {err['name']}: {err['status']}")
        if len(results["errors"]) > 20:
            print(f"  ... and {len(results['errors']) - 20} more")

    # Save log
    log_data = {
        "timestamp": time.strftime("%Y-%m-%d %H:%M:%S"),
        "total_blueprints": len(legacy_bps),
        "decompiled": results["ok"],
        "failed": results["error"],
        "elapsed_seconds": round(overall_elapsed, 1),
        "errors": results["errors"],
    }
    with open(LOG_FILE, "w") as f:
        json.dump(log_data, f, indent=2)
    print(f"\nLog: {LOG_FILE}")


if __name__ == "__main__":
    main()
