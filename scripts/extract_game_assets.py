"""
extract_game_assets.py -- Automated game asset extraction for Moria-Replication

Performs a FULL unpack of the Return to Moria IoStore pak using retoc,
then indexes and validates the results. All assets are extracted -- no
cherry-picking -- because the editor project needs the complete content
tree to resolve references.

After extraction, runs validation to confirm critical assets are present
and cross-references against FModel JSON exports.

Usage:
    python extract_game_assets.py              # Full unpack + validate
    python extract_game_assets.py --validate   # Validate only (skip unpack)
    python extract_game_assets.py --dry-run    # Index and report only
    python extract_game_assets.py --stats      # Show asset type breakdown

Requirements:
    - retoc installed at: <project>\\tools\\retoc\\bin\\retoc.exe
    - Game installed at: C:\\Program Files\\Epic Games\\ReturnToMoria\\
"""

import argparse
import os
import subprocess
import sys
from collections import defaultdict
from pathlib import Path

# -- Paths -------------------------------------------------------------------
PROJECT_ROOT = Path(__file__).resolve().parent.parent
TOOLS_DIR = PROJECT_ROOT / "tools"
RETOC = TOOLS_DIR / "retoc" / "bin" / "retoc.exe"
GAME_PAKS = Path(r"C:\Program Files\Epic Games\ReturnToMoria\Moria\Content\Paks")
UTOC_MAIN = GAME_PAKS / "Moria-WindowsNoEditor.utoc"
OUTPUT_DIR = TOOLS_DIR / "extracted-assets"
FMODEL_EXPORT_DIR = TOOLS_DIR / "fmodel-export"

# -- Critical DataTables that MUST exist for the project to work -------------
CRITICAL_DATATABLES = [
    "DT_Constructions",
    "DT_ConstructionRecipes",
    "DT_Items",
    "DT_Weapons",
    "DT_Tools",
    "DT_Armor",
    "DT_Consumables",
    "DT_Ores",
    "DT_ContainerItems",
    "DT_Storage",
    "DT_SettlementLevelData",
    "DT_WorldLevelData",
]

# -- Critical biome/zone assets ---------------------------------------------
CRITICAL_BIOME_ASSETS = [
    "DT_Moria_Biomes",
    "DT_Moria_Zones",
    "DT_Moria_ZoneTemplates",
    "DT_Moria_ZoneDeck",
    "DT_Moria_ZoneResources",
]


def check_prerequisites():
    """Verify all required tools and paths exist."""
    errors = []
    if not RETOC.exists():
        errors.append(f"retoc not found at {RETOC}")
    if not UTOC_MAIN.exists():
        errors.append(f"Game .utoc not found at {UTOC_MAIN}")
    if errors:
        for e in errors:
            print(f"  ERROR: {e}")
        sys.exit(1)
    print(f"  retoc:      {RETOC}")
    print(f"  Game paks:  {GAME_PAKS}")
    print(f"  Output:     {OUTPUT_DIR}")


def build_asset_index():
    """Run retoc list --path and parse the full asset index."""
    print("\nIndexing game pak...")
    result = subprocess.run(
        [str(RETOC), "list", "--path", str(UTOC_MAIN)],
        capture_output=True, text=True, encoding="utf-8", errors="replace"
    )
    if result.returncode != 0:
        print(f"  ERROR: retoc list failed:\n{result.stderr}")
        sys.exit(1)

    assets = []
    for line in result.stdout.splitlines():
        parts = line.split()
        if len(parts) >= 4:
            path = parts[-1]
            if path.startswith("../../../"):
                path = path[9:]
            assets.append(path)

    print(f"  Indexed {len(assets):,} assets in pak")
    return assets


def full_unpack():
    """Extract the entire pak to the output directory."""
    if OUTPUT_DIR.exists():
        # Check if already unpacked
        existing = sum(1 for _ in OUTPUT_DIR.rglob("*.uasset"))
        if existing > 1000:
            print(f"\n  Output directory already contains {existing:,} .uasset files.")
            print(f"  Skipping unpack. Delete {OUTPUT_DIR} to force re-extraction.")
            return True

    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    print(f"\n  Unpacking full game pak to {OUTPUT_DIR}")
    print(f"  This will take several minutes for a 15+ GB pak...")

    result = subprocess.run(
        [str(RETOC), "unpack", str(UTOC_MAIN), str(OUTPUT_DIR)],
        capture_output=True, text=True, encoding="utf-8", errors="replace"
    )

    if result.returncode != 0:
        print(f"  ERROR: retoc unpack failed:")
        print(result.stderr[:1000] if result.stderr else "(no stderr)")
        return False

    # Count what we got
    uasset_count = sum(1 for _ in OUTPUT_DIR.rglob("*.uasset"))
    uexp_count = sum(1 for _ in OUTPUT_DIR.rglob("*.uexp"))
    umap_count = sum(1 for _ in OUTPUT_DIR.rglob("*.umap"))
    total_size = sum(f.stat().st_size for f in OUTPUT_DIR.rglob("*") if f.is_file())

    print(f"\n  Unpack complete:")
    print(f"    .uasset files:  {uasset_count:,}")
    print(f"    .uexp files:    {uexp_count:,}")
    print(f"    .umap files:    {umap_count:,}")
    print(f"    Total size:     {total_size / (1024**3):.2f} GB")
    return True


def compute_stats(assets):
    """Break down assets by type/extension and content directory."""
    by_ext = defaultdict(int)
    by_dir = defaultdict(int)

    for a in assets:
        ext = Path(a).suffix.lower()
        by_ext[ext] += 1

        # Top-level content directory
        parts = Path(a).parts
        if len(parts) >= 3:
            by_dir[parts[2]] += 1  # Moria/Content/<THIS>

    print("\n  Asset types:")
    for ext, count in sorted(by_ext.items(), key=lambda x: -x[1]):
        print(f"    {ext:20s}  {count:,}")

    print("\n  Top content directories:")
    for d, count in sorted(by_dir.items(), key=lambda x: -x[1])[:20]:
        print(f"    {d:30s}  {count:,}")


def validate_critical_assets():
    """Check that critical DataTables and biome assets exist in both raw and JSON form."""
    print("\n" + "=" * 70)
    print("CRITICAL ASSET VALIDATION")
    print("=" * 70)

    all_ok = True

    # -- DataTables (raw extraction) --
    print("\n  Raw extraction (.uasset in extracted-assets/):")
    for dt_name in CRITICAL_DATATABLES:
        matches = list(OUTPUT_DIR.rglob(f"{dt_name}.uasset"))
        if matches:
            size = matches[0].stat().st_size
            print(f"    OK    {dt_name}.uasset ({size:,} bytes)")
        else:
            print(f"    FAIL  {dt_name}.uasset -- NOT FOUND")
            all_ok = False

    # -- DataTables (FModel JSON) --
    print("\n  FModel JSON exports (fmodel-export/):")
    for dt_name in CRITICAL_DATATABLES:
        matches = list(FMODEL_EXPORT_DIR.rglob(f"{dt_name}.json"))
        if matches:
            size = matches[0].stat().st_size
            status = "OK" if size > 100 else "WARN (small)"
            print(f"    {status:6s}  {dt_name}.json ({size:,} bytes)")
        else:
            print(f"    FAIL  {dt_name}.json -- NOT FOUND (export from FModel)")
            all_ok = False

    # -- Biome/Zone assets --
    print("\n  Biome/Zone critical assets:")
    for name in CRITICAL_BIOME_ASSETS:
        raw = list(OUTPUT_DIR.rglob(f"{name}.uasset"))
        json = list(FMODEL_EXPORT_DIR.rglob(f"{name}.json"))
        raw_ok = "OK" if raw else "FAIL"
        json_ok = "OK" if json else "MISSING"
        print(f"    {raw_ok:6s} raw  /  {json_ok:7s} json  --  {name}")
        if not raw:
            all_ok = False

    # -- Landmark/Level assets --
    print("\n  Landmark assets (spot check):")
    landmark_dirs = list(OUTPUT_DIR.rglob("Landmarks"))
    if landmark_dirs:
        landmark_count = sum(1 for _ in landmark_dirs[0].rglob("*.uasset"))
        print(f"    OK    Found Landmarks/ directory with {landmark_count} assets")
    else:
        print(f"    INFO  No 'Landmarks/' directory found (may use different naming)")

    # -- .umap level files --
    print("\n  Level files (.umap):")
    umaps = list(OUTPUT_DIR.rglob("*.umap"))
    if umaps:
        print(f"    OK    {len(umaps)} .umap files found")
        for m in umaps[:5]:
            print(f"          {m.relative_to(OUTPUT_DIR)}")
        if len(umaps) > 5:
            print(f"          ... and {len(umaps) - 5} more")
    else:
        print(f"    INFO  No .umap files found (may be in separate container)")

    return all_ok


def validate_fmodel_coverage(assets):
    """Check what percentage of DataTables have FModel JSON exports."""
    print("\n" + "=" * 70)
    print("FMODEL JSON COVERAGE")
    print("=" * 70)

    dt_assets = [a for a in assets if "/DT_" in a and a.endswith(".uasset")]
    found = 0
    missing = []

    for dt in dt_assets:
        json_name = dt.replace(".uasset", ".json")
        json_path = FMODEL_EXPORT_DIR / "Exports" / json_name
        if json_path.exists():
            found += 1
        else:
            missing.append(Path(dt).stem)

    pct = (found / len(dt_assets) * 100) if dt_assets else 0
    print(f"\n  DataTables: {found}/{len(dt_assets)} have JSON exports ({pct:.0f}%)")

    if missing:
        print(f"\n  Missing JSON exports ({len(missing)}):")
        for m in missing[:15]:
            print(f"    - {m}")
        if len(missing) > 15:
            print(f"    ... and {len(missing) - 15} more")
        print(f"\n  To fix: In FModel, Ctrl+Shift+F -> search 'DT_' -> Save Properties (.json)")
    else:
        print(f"  All DataTable JSON exports present!")


def study_existing_mods():
    """Analyze existing mod pak structure for reference."""
    print("\n" + "=" * 70)
    print("EXISTING MOD PAK ANALYSIS")
    print("=" * 70)

    mod_paks = [
        ("TobiModsAddons", GAME_PAKS / "Secrets of Khazad-dum" / "TobiModsAddons_P.utoc"),
        ("SecretsOfKhazadDum", GAME_PAKS / "Secrets of Khazad-dum" / "SecretsOfKhazadDum_P.utoc"),
    ]

    for name, utoc in mod_paks:
        if not utoc.exists():
            print(f"\n  {name}: .utoc not found at {utoc}")
            continue

        result = subprocess.run(
            [str(RETOC), "list", "--path", "--size", str(utoc)],
            capture_output=True, text=True, encoding="utf-8", errors="replace"
        )

        if result.returncode != 0:
            print(f"\n  {name}: retoc list failed")
            continue

        lines = result.stdout.strip().splitlines()
        print(f"\n  {name} ({len(lines)} chunks):")
        for line in lines[:20]:
            print(f"    {line}")
        if len(lines) > 20:
            print(f"    ... and {len(lines) - 20} more")


def main():
    parser = argparse.ArgumentParser(
        description="Extract and validate Return to Moria game assets"
    )
    parser.add_argument(
        "--dry-run", action="store_true",
        help="Index pak and report stats only -- no extraction"
    )
    parser.add_argument(
        "--validate", action="store_true",
        help="Skip extraction, only validate existing files"
    )
    parser.add_argument(
        "--stats", action="store_true",
        help="Show asset type/directory breakdown"
    )
    parser.add_argument(
        "--study-mods", action="store_true",
        help="Analyze existing mod pak structure"
    )
    args = parser.parse_args()

    print("=" * 70)
    print("Moria-Replication Asset Extractor")
    print("=" * 70)

    print("\nChecking prerequisites...")
    check_prerequisites()

    # Build index from pak
    assets = build_asset_index()

    if args.stats or args.dry_run:
        compute_stats(assets)

    if args.study_mods:
        study_existing_mods()

    if args.dry_run:
        print(f"\nDry run complete. {len(assets):,} assets indexed.")
        return

    # Full extraction
    if not args.validate:
        ok = full_unpack()
        if not ok:
            print("\nExtraction failed. Fix errors above and retry.")
            sys.exit(1)

    # Validation
    all_ok = validate_critical_assets()
    validate_fmodel_coverage(assets)

    # Study existing mods (always useful context)
    study_existing_mods()

    # Final status
    print("\n" + "=" * 70)
    if all_ok:
        print("ALL CHECKS PASSED")
    else:
        print("SOME CHECKS FAILED -- see details above")
    print("=" * 70)
    print(f"\nExtracted assets: {OUTPUT_DIR}")
    print(f"FModel JSON:      {FMODEL_EXPORT_DIR}")


if __name__ == "__main__":
    main()
