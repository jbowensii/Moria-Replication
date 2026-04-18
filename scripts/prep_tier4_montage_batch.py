"""Stage tier 4 JSON-importable animation assets for BatchImport.

AnimMontage, BlendSpace, BlendSpace1D, AimOffsetBlendSpace1D
These depend on AnimSequence being imported first.
"""
import subprocess
import os
import shutil
import json
from pathlib import Path
from collections import defaultdict

CLOUD_BT = Path("tools/cloud-exports-by-type")
CLOUD = Path("tools/cloud-exports")
CONTENT = Path("project/Content")
BATCH_DIR = Path("tools/batch-import-tier4-montage")

TIER4_JSON_TYPES = [
    "AnimMontage",
    "BlendSpace",
    "BlendSpace1D",
    "AimOffsetBlendSpace1D",
]


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


def main():
    print("Building content index...")
    content_set = get_content_set()
    print(f"  {len(content_set)} assets in project")

    if BATCH_DIR.exists():
        shutil.rmtree(BATCH_DIR)

    total = 0
    by_type = defaultdict(int)

    for type_name in TIER4_JSON_TYPES:
        type_dir = CLOUD_BT / type_name
        if not type_dir.exists():
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

    print(f"\nStaged {total} JSON files in {BATCH_DIR}")
    for t, c in sorted(by_type.items(), key=lambda x: -x[1]):
        print(f"  {t}: {c}")


if __name__ == "__main__":
    main()
