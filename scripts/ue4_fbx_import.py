"""UE4 Editor Python script to batch-import FBX files.

Run via:
    UE4Editor-Cmd.exe Moria.uproject -ExecutePythonScript="path/to/this_script.py" -nullrhi

Reads a manifest JSON file listing (source_fbx, dest_game_path) pairs
and imports each FBX as a StaticMesh or SkeletalMesh.
"""
import unreal
import json
import os

MANIFEST_PATH = r"C:\Users\johnb\OneDrive\Documents\Projects\Moria-Replication\tools\fbx-import-manifest.json"
LOG_PATH = r"C:\Users\johnb\OneDrive\Documents\Projects\Moria-Replication\tools\fbx-import-results.json"


def import_fbx_batch():
    """Import all FBX files from the manifest."""
    if not os.path.exists(MANIFEST_PATH):
        unreal.log_error("Manifest not found: " + MANIFEST_PATH)
        return

    with open(MANIFEST_PATH, "r") as f:
        entries = json.load(f)

    total = len(entries)
    unreal.log("Starting FBX import: {} files".format(total))

    asset_tools = unreal.AssetToolsHelpers.get_asset_tools()
    results = {"imported": 0, "skipped": 0, "failed": 0, "errors": []}

    for i, entry in enumerate(entries):
        fbx_path = entry["source"]
        dest_path = entry["dest"]
        asset_name = entry.get("name", "")
        is_skeletal = entry.get("skeletal", False)

        if i % 100 == 0:
            unreal.log("Progress: {}/{} (imported: {})".format(i, total, results["imported"]))

        # Check if already exists
        full_asset_path = dest_path + "/" + asset_name
        if unreal.EditorAssetLibrary.does_asset_exist(full_asset_path):
            results["skipped"] += 1
            continue

        try:
            task = unreal.AssetImportTask()
            task.set_editor_property("filename", fbx_path)
            task.set_editor_property("destination_path", dest_path)
            task.set_editor_property("destination_name", asset_name)
            task.set_editor_property("replace_existing", False)
            task.set_editor_property("automated", True)
            task.set_editor_property("save", True)

            options = unreal.FbxImportUI()
            options.set_editor_property("import_mesh", True)
            options.set_editor_property("import_textures", False)
            options.set_editor_property("import_materials", False)
            options.set_editor_property("import_as_skeletal", is_skeletal)

            if not is_skeletal:
                sm_data = unreal.FbxStaticMeshImportData()
                sm_data.set_editor_property("combine_meshes", True)
                sm_data.set_editor_property("generate_lightmap_u_vs", True)
                sm_data.set_editor_property("auto_generate_collision", True)
                options.set_editor_property("static_mesh_import_data", sm_data)

            task.set_editor_property("options", options)
            asset_tools.import_asset_tasks([task])

            # Verify import by checking if asset now exists
            if unreal.EditorAssetLibrary.does_asset_exist(full_asset_path):
                results["imported"] += 1
            else:
                results["failed"] += 1
                if len(results["errors"]) < 50:
                    results["errors"].append("Not created: " + asset_name)

        except Exception as e:
            results["failed"] += 1
            if len(results["errors"]) < 50:
                results["errors"].append("{}: {}".format(asset_name, str(e)))

    unreal.log("Import complete: {} imported, {} skipped, {} failed".format(
        results["imported"], results["skipped"], results["failed"]))

    with open(LOG_PATH, "w") as f:
        json.dump(results, f, indent=2)

    unreal.log("Results saved to " + LOG_PATH)


import_fbx_batch()
