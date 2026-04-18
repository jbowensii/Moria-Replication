"""Generate FBX import manifest for UE4 Python import script."""
import json
import os
from pathlib import Path

FBX_DIR = Path(r"C:\Users\johnb\OneDrive\Documents\Projects\Moria-Replication\tools\umodel-meshes-fbx")
CONTENT_DIR = Path(r"C:\Users\johnb\OneDrive\Documents\Projects\Moria-Replication\project\Content")
MANIFEST_PATH = Path(r"C:\Users\johnb\OneDrive\Documents\Projects\Moria-Replication\tools\fbx-import-manifest.json")

entries = []
already_imported = 0
total_fbx = 0

for fbx_path in FBX_DIR.rglob("*.fbx"):
    total_fbx += 1
    rel = fbx_path.relative_to(FBX_DIR)
    parts = list(rel.parts)
    if parts[0] == "Game":
        parts = parts[1:]

    # Check if already imported
    uasset_path = CONTENT_DIR / Path(*parts).with_suffix(".uasset")
    if uasset_path.exists():
        already_imported += 1
        continue

    # Determine dest path and asset name
    asset_name = fbx_path.stem
    dest_path = "/Game/" + "/".join(parts[:-1])
    is_skeletal = asset_name.startswith("SK_")

    entries.append({
        "source": str(fbx_path).replace("\\", "/"),
        "dest": dest_path,
        "name": asset_name,
        "skeletal": is_skeletal,
    })

with open(MANIFEST_PATH, "w") as f:
    json.dump(entries, f, indent=2)

print(f"Total FBX files: {total_fbx}")
print(f"Already imported: {already_imported}")
print(f"To import: {len(entries)}")
print(f"  StaticMesh (SM_): {sum(1 for e in entries if not e['skeletal'])}")
print(f"  SkeletalMesh (SK_): {sum(1 for e in entries if e['skeletal'])}")
print(f"Manifest written to: {MANIFEST_PATH}")
