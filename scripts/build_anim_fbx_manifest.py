"""Build FBX import manifest for animation files.

Maps skeleton names to animation FBX paths for UE4 import.
Groups animations by skeleton to enable efficient batch import.

Usage:
    python build_anim_fbx_manifest.py
"""
import json
import os
import subprocess
from pathlib import Path
from collections import defaultdict

REPO_ROOT = Path(__file__).parent.parent
FBX_DIR = REPO_ROOT / "tools" / "anim-fbx"
CONTENT = REPO_ROOT / "project" / "Content"
MANIFEST_PATH = REPO_ROOT / "tools" / "anim-fbx-import-manifest.json"

# Known skeleton mappings: animation folder prefix -> skeleton game path
# These map the animation directory structure to the correct skeleton
SKELETON_MAP = {}  # Will be auto-populated


def get_content_set():
    content_str = str(CONTENT.resolve())
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


def find_skeletons(content_set):
    """Find all Skeleton assets in the project."""
    skeletons = {}
    for path in content_set:
        name = path.split("/")[-1]
        if "_Skeleton" in name and "Mesh" not in name:
            # Extract the creature/character name
            # e.g., CharacterArt/Creatures/BadgerBoar/SK_BadgerBoar_Skeleton
            skeletons[name] = path
    return skeletons


def main():
    print("Building content index...")
    content_set = get_content_set()
    print(f"  {len(content_set)} assets in project")

    print("Finding skeletons...")
    skeletons = find_skeletons(content_set)
    print(f"  {len(skeletons)} skeleton assets found")
    for name, path in sorted(skeletons.items()):
        print(f"    {name} -> {path}")

    print(f"\nScanning FBX directory: {FBX_DIR}")
    entries = []
    skipped = 0
    by_prefix = defaultdict(int)

    for fbx_path in sorted(FBX_DIR.rglob("*.fbx")):
        rel = fbx_path.relative_to(FBX_DIR)
        game_path = str(rel.with_suffix("")).replace("\\", "/")

        # Check if already imported
        if game_path in content_set:
            skipped += 1
            continue

        # Extract animation folder prefix for skeleton matching
        parts = game_path.split("/")
        prefix = parts[1] if len(parts) >= 3 and parts[0] == "Animations" else parts[0]
        by_prefix[prefix] += 1

        dest_dir = "/Game/" + str(rel.parent).replace("\\", "/")

        entries.append({
            "fbx": str(fbx_path),
            "game_path": "/Game/" + game_path,
            "dest_dir": dest_dir,
            "asset_name": rel.stem,
            "skeleton_hint": prefix,
        })

    # Write manifest
    manifest = {
        "total": len(entries),
        "skipped_existing": skipped,
        "skeletons_found": {k: f"/Game/{v}" for k, v in skeletons.items()},
        "by_skeleton_hint": dict(sorted(by_prefix.items(), key=lambda x: -x[1])),
        "entries": entries,
    }

    with open(MANIFEST_PATH, "w") as f:
        json.dump(manifest, f, indent=2)

    print(f"\nManifest: {MANIFEST_PATH}")
    print(f"  Total FBX to import: {len(entries)}")
    print(f"  Already imported:    {skipped}")
    print(f"\n  By skeleton group:")
    for prefix, count in sorted(by_prefix.items(), key=lambda x: -x[1]):
        print(f"    {prefix}: {count}")


if __name__ == "__main__":
    main()
