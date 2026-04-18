"""Analyze what's in cloud exports but not yet imported to the project."""
import subprocess
import os
from pathlib import Path
from collections import defaultdict


def fast_find(directory, extension):
    """Fast recursive file listing via PowerShell."""
    dir_str = str(directory).replace("/", "\\")
    ps_cmd = (
        f"Get-ChildItem -Path '{dir_str}' -Filter '*{extension}' "
        f"-Recurse -File | ForEach-Object {{ $_.FullName }}"
    )
    result = subprocess.run(
        ["powershell", "-NoProfile", "-Command", ps_cmd],
        capture_output=True, text=True, errors="replace", timeout=300
    )
    return [l.strip() for l in result.stdout.splitlines() if l.strip()]


def main():
    cloud = Path("tools/cloud-exports")
    content = Path("project/Content")

    print("Scanning cloud exports...")
    cloud_files = fast_find(cloud, ".json")
    print(f"  Cloud export JSONs: {len(cloud_files)}")

    print("Scanning project Content...")
    content_files = fast_find(content, ".uasset")
    print(f"  Project uassets: {len(content_files)}")

    # Build relative path sets
    cloud_str = str(cloud.resolve())
    content_str = str(content.resolve())

    cloud_paths = set()
    for f in cloud_files:
        rel = os.path.relpath(f, cloud_str).replace("\\", "/")
        rel = rel.rsplit(".", 1)[0]  # strip .json
        cloud_paths.add(rel)

    content_paths = set()
    for f in content_files:
        rel = os.path.relpath(f, content_str).replace("\\", "/")
        rel = rel.rsplit(".", 1)[0]  # strip .uasset
        content_paths.add(rel)

    missing = cloud_paths - content_paths
    imported = cloud_paths & content_paths
    extra = content_paths - cloud_paths

    print()
    print(f"Cloud exports with matching project asset: {len(imported)}")
    print(f"Cloud exports WITHOUT project asset:       {len(missing)}")
    print(f"Project assets without cloud export:       {len(extra)}")

    # Categorize missing by top-level directory
    by_category = defaultdict(int)
    by_prefix = defaultdict(int)

    for m in missing:
        parts = m.split("/")
        cat = parts[0] if parts else "unknown"
        by_category[cat] += 1

        name = parts[-1] if parts else m
        for pfx in ["SM_", "SK_", "MI_", "M_", "T_", "DT_", "BP_", "WBP_",
                     "ABP_", "DA_", "NS_", "GE_", "GA_", "GC_", "AM_",
                     "UCX_", "PA_", "PS_", "MF_", "FT_", "LUT_", "SS_",
                     "MM_", "MPC_", "Cue_", "ALS_"]:
            if name.startswith(pfx):
                by_prefix[pfx] += 1
                break
        else:
            by_prefix["(no standard prefix)"] += 1

    print()
    print("=== MISSING BY DIRECTORY ===")
    for cat, count in sorted(by_category.items(), key=lambda x: -x[1]):
        print(f"  {cat}: {count}")

    print()
    print("=== MISSING BY NAME PREFIX ===")
    for prefix, count in sorted(by_prefix.items(), key=lambda x: -x[1]):
        print(f"  {prefix}: {count}")

    # Also check cloud-exports-by-type for type breakdown
    bt = Path("tools/cloud-exports-by-type")
    if bt.exists():
        print()
        print("=== CLOUD EXPORTS BY TYPE (from by-type dir) ===")
        type_counts = {}
        for type_dir in sorted(bt.iterdir()):
            if type_dir.is_dir():
                count = len(fast_find(type_dir, ".json"))
                if count > 0:
                    type_counts[type_dir.name] = count
        for t, c in sorted(type_counts.items(), key=lambda x: -x[1]):
            print(f"  {t}: {c}")


if __name__ == "__main__":
    main()
