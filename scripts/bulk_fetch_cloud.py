#!/usr/bin/env python3
"""
Bulk Asset Fetch from JsonAsAsset Cloud Server

Walks retoc-extracted .uasset files to discover all game asset paths,
then fetches JSON export data from the Cloud Server and saves to disk.
The saved JSON files can then be imported via the BatchImport commandlet
or the "Import Folder of JSON Files" toolbar button in the UE4 editor.

Usage:
    python bulk_fetch_cloud.py                          # Scan + summary only
    python bulk_fetch_cloud.py --fetch                  # Fetch all (skip WwiseAudio)
    python bulk_fetch_cloud.py --fetch --category Art   # Fetch specific category
    python bulk_fetch_cloud.py --fetch --resume         # Resume interrupted fetch
    python bulk_fetch_cloud.py --fetch --workers 4      # Parallel fetches (default: 4)
    python bulk_fetch_cloud.py --stats                  # Show stats on already-fetched

Requirements:
    - Cloud Server running at http://localhost:1500 with Moria profile loaded
    - retoc-extracted assets at tools/extracted-assets/Moria/Content/
"""

import argparse
import json
import os
import sys
import time
import urllib.request
import urllib.error
from collections import defaultdict
from concurrent.futures import ThreadPoolExecutor, as_completed
from pathlib import Path
from threading import Lock

# ── Paths ────────────────────────────────────────────────────────────────────
SCRIPT_DIR = Path(__file__).parent
REPO_ROOT = SCRIPT_DIR.parent
EXTRACTED_DIR = REPO_ROOT / "tools" / "extracted-assets" / "Moria" / "Content"
OUTPUT_DIR = REPO_ROOT / "tools" / "cloud-exports"
CLOUD_URL = "http://localhost:1500"

# Categories to skip by default (not importable via JsonAsAsset)
SKIP_CATEGORIES = {
    "WwiseAudio",   # Wwise audio middleware — separate pipeline
    "Movies",       # Video files
    "Cinematics",   # Sequencer — not useful for mod reconstruction
}

# ── Path conversion ──────────────────────────────────────────────────────────

def uasset_to_game_path(uasset_path: Path, content_root: Path) -> str:
    """Convert an extracted .uasset file path to a /Game/... path."""
    rel = uasset_path.relative_to(content_root)
    # Remove .uasset extension, use forward slashes
    game_path = "/Game/" + str(rel.with_suffix("")).replace("\\", "/")
    return game_path


def game_path_to_output_file(game_path: str, output_dir: Path) -> Path:
    """Convert a /Game/... path to the local JSON output file path."""
    # /Game/Art/Foo/Bar -> output_dir/Art/Foo/Bar.json
    rel = game_path.replace("/Game/", "", 1)
    return output_dir / (rel + ".json")


# ── Discovery ────────────────────────────────────────────────────────────────

def discover_assets(content_root: Path) -> dict:
    """Walk extracted assets and group by top-level category."""
    categories = defaultdict(list)

    for uasset in content_root.rglob("*.uasset"):
        game_path = uasset_to_game_path(uasset, content_root)
        # Top-level category = first path component after /Game/
        parts = game_path.split("/")
        # /Game/Art/... -> category = "Art"
        # /Game/GE_EnemyDifficultyScaling -> category = "_root"
        if len(parts) > 3:
            category = parts[2]
        else:
            category = "_root"
        categories[category].append(game_path)

    return dict(categories)


# ── Cloud Server fetch ───────────────────────────────────────────────────────

print_lock = Lock()
stats_lock = Lock()
stats = {"success": 0, "skip_exists": 0, "not_found": 0, "binary": 0, "error": 0}


def fetch_one(game_path: str, output_dir: Path, resume: bool) -> str:
    """Fetch a single asset from Cloud Server. Returns status string."""
    out_file = game_path_to_output_file(game_path, output_dir)

    # Resume mode: skip if already fetched
    if resume and out_file.exists() and out_file.stat().st_size > 0:
        with stats_lock:
            stats["skip_exists"] += 1
        return "skip_exists"

    url = f"{CLOUD_URL}/api/export?path={urllib.request.quote(game_path, safe='/')}"

    try:
        req = urllib.request.Request(url, headers={"Accept": "application/json"})
        with urllib.request.urlopen(req, timeout=30) as resp:
            content_type = resp.headers.get("Content-Type", "")
            data = resp.read()

            # Check if response is JSON (export data we want)
            if "json" in content_type or data[:1] == b"{" or data[:1] == b"[":
                try:
                    # Validate it's actual JSON and not an error
                    parsed = json.loads(data)
                    if isinstance(parsed, dict) and "errorCode" in parsed:
                        with stats_lock:
                            stats["not_found"] += 1
                        return "not_found"

                    # Cloud Server returns {"exports": [...]}, but JsonAsAsset's
                    # DeserializeJSON expects a raw JSON array [...] (FModel format).
                    # Extract the exports array so the importer can parse it.
                    if isinstance(parsed, dict) and "exports" in parsed:
                        save_data = json.dumps(parsed["exports"], separators=(",", ":")).encode()
                    elif isinstance(parsed, list):
                        save_data = data  # Already an array
                    else:
                        save_data = data  # Unknown format, save as-is

                    # Save JSON
                    out_file.parent.mkdir(parents=True, exist_ok=True)
                    with open(out_file, "wb") as f:
                        f.write(save_data)

                    with stats_lock:
                        stats["success"] += 1
                    return "success"

                except json.JSONDecodeError:
                    with stats_lock:
                        stats["error"] += 1
                    return "json_error"
            else:
                # Binary response (PNG texture, .pskx mesh path, etc.)
                # These are handled by Cloud Tools in the editor, not via JSON import
                with stats_lock:
                    stats["binary"] += 1
                return "binary"

    except urllib.error.HTTPError as e:
        if e.code == 404:
            with stats_lock:
                stats["not_found"] += 1
            return "not_found"
        with stats_lock:
            stats["error"] += 1
        return f"http_{e.code}"

    except Exception as e:
        with stats_lock:
            stats["error"] += 1
        return f"error: {e}"


def check_server() -> bool:
    """Check if Cloud Server is running and initialized."""
    try:
        with urllib.request.urlopen(f"{CLOUD_URL}/api/status", timeout=5) as resp:
            data = json.loads(resp.read())
            return data.get("status") == "Initialized"
    except Exception:
        return False


# ── Main ─────────────────────────────────────────────────────────────────────

def print_summary(categories: dict, skip_cats: set):
    """Print discovery summary."""
    print("\n" + "=" * 65)
    print("  Extracted Asset Inventory")
    print("=" * 65)

    total = 0
    fetchable = 0
    for cat in sorted(categories.keys()):
        count = len(categories[cat])
        total += count
        skipped = cat in skip_cats
        marker = "  [SKIP]" if skipped else ""
        if not skipped:
            fetchable += count
        print(f"  {cat:<30} {count:>6}{marker}")

    print(f"  {'-' * 30} {'-' * 6}")
    print(f"  {'TOTAL':<30} {total:>6}")
    print(f"  {'Fetchable (excl. skipped)':<30} {fetchable:>6}")
    print("=" * 65)
    return fetchable


def show_fetch_stats(output_dir: Path):
    """Show stats on already-fetched JSON files."""
    if not output_dir.exists():
        print(f"\nNo fetched data found at {output_dir}")
        return

    json_files = list(output_dir.rglob("*.json"))
    categories = defaultdict(int)
    total_size = 0
    for f in json_files:
        rel = f.relative_to(output_dir)
        parts = str(rel).replace("\\", "/").split("/")
        cat = parts[0] if len(parts) > 1 else "_root"
        categories[cat] += 1
        total_size += f.stat().st_size

    print(f"\n{'=' * 65}")
    print(f"  Already Fetched: {output_dir}")
    print(f"{'=' * 65}")
    for cat in sorted(categories.keys()):
        print(f"  {cat:<30} {categories[cat]:>6}")
    print(f"  {'-' * 30} {'-' * 6}")
    print(f"  {'TOTAL':<30} {len(json_files):>6}")
    print(f"  {'Total size':<30} {total_size / (1024*1024):.1f} MB")
    print(f"{'=' * 65}")


def main():
    parser = argparse.ArgumentParser(description="Bulk fetch asset JSON from Cloud Server")
    parser.add_argument("--fetch", action="store_true", help="Fetch JSON exports from Cloud Server")
    parser.add_argument("--category", type=str, default=None,
                        help="Fetch only this category (e.g., Art, Items, UI)")
    parser.add_argument("--resume", action="store_true", help="Skip already-fetched files")
    parser.add_argument("--workers", type=int, default=4, help="Parallel fetch workers (default: 4)")
    parser.add_argument("--stats", action="store_true", help="Show stats on already-fetched files")
    parser.add_argument("--include-all", action="store_true",
                        help="Include normally-skipped categories (WwiseAudio, Movies, etc.)")
    parser.add_argument("--output", type=str, default=None,
                        help=f"Output directory (default: {OUTPUT_DIR})")
    args = parser.parse_args()

    output_dir = Path(args.output) if args.output else OUTPUT_DIR

    if args.stats:
        show_fetch_stats(output_dir)
        return

    # Discover assets
    if not EXTRACTED_DIR.exists():
        print(f"ERROR: Extracted assets not found at: {EXTRACTED_DIR}")
        print("Run retoc extraction first.")
        sys.exit(1)

    print(f"Scanning extracted assets at: {EXTRACTED_DIR}")
    categories = discover_assets(EXTRACTED_DIR)

    skip_cats = set() if args.include_all else SKIP_CATEGORIES
    fetchable_count = print_summary(categories, skip_cats)

    if not args.fetch:
        print("\nTo fetch JSON exports, run with --fetch flag:")
        print("  python bulk_fetch_cloud.py --fetch                    # All fetchable")
        print("  python bulk_fetch_cloud.py --fetch --category Art     # Just Art assets")
        print("  python bulk_fetch_cloud.py --fetch --resume           # Resume interrupted")
        if output_dir.exists():
            print()
            show_fetch_stats(output_dir)
        return

    # Check Cloud Server
    if not check_server():
        print("\nERROR: Cloud Server not running or not initialized.")
        print("Start it with: scripts/start_cloud_server.bat")
        print("Then load the Moria profile in the GUI.")
        sys.exit(1)

    print(f"\nCloud Server: OK (Initialized)")

    # Build fetch list
    fetch_paths = []
    if args.category:
        if args.category not in categories:
            print(f"\nERROR: Category '{args.category}' not found.")
            print(f"Available: {', '.join(sorted(categories.keys()))}")
            sys.exit(1)
        fetch_paths = categories[args.category]
        print(f"\nFetching category: {args.category} ({len(fetch_paths)} assets)")
    else:
        for cat, paths in sorted(categories.items()):
            if cat not in skip_cats:
                fetch_paths.extend(paths)
        print(f"\nFetching {len(fetch_paths)} assets ({len(skip_cats)} categories skipped)")

    output_dir.mkdir(parents=True, exist_ok=True)

    # Fetch with thread pool
    start_time = time.time()
    completed = 0
    total = len(fetch_paths)

    print(f"Output: {output_dir}")
    print(f"Workers: {args.workers}")
    print(f"Resume mode: {'ON' if args.resume else 'OFF'}")
    print()

    with ThreadPoolExecutor(max_workers=args.workers) as executor:
        futures = {
            executor.submit(fetch_one, path, output_dir, args.resume): path
            for path in fetch_paths
        }

        for future in as_completed(futures):
            completed += 1
            result = future.result()

            # Progress every 100 assets
            if completed % 100 == 0 or completed == total:
                elapsed = time.time() - start_time
                rate = completed / elapsed if elapsed > 0 else 0
                eta = (total - completed) / rate if rate > 0 else 0
                with stats_lock:
                    s = dict(stats)
                print(
                    f"  [{completed:>6}/{total}] "
                    f"ok:{s['success']} skip:{s['skip_exists']} "
                    f"bin:{s['binary']} miss:{s['not_found']} err:{s['error']} "
                    f"({rate:.0f}/s, ETA {eta/60:.0f}m)",
                    flush=True,
                )

    elapsed = time.time() - start_time

    # Final report
    print(f"\n{'=' * 65}")
    print(f"  Fetch Complete — {elapsed:.0f}s ({elapsed/60:.1f}m)")
    print(f"{'=' * 65}")
    print(f"  JSON saved (importable):  {stats['success']:>6}")
    print(f"  Already existed (skipped): {stats['skip_exists']:>6}")
    print(f"  Binary (tex/mesh):         {stats['binary']:>6}")
    print(f"  Not found on server:       {stats['not_found']:>6}")
    print(f"  Errors:                    {stats['error']:>6}")
    print(f"{'=' * 65}")
    print(f"\nJSON exports saved to: {output_dir}")
    print(f"\nNext steps:")
    print(f"  1. In UE4 editor with Cloud enabled:")
    print(f"     JsonAsAsset toolbar -> Import Folder of JSON Files -> select {output_dir}")
    print(f"  2. Or via commandlet:")
    print(f'     python phase3_import.py --import --all --exports-dir "{output_dir}"')


if __name__ == "__main__":
    main()
