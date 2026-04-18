"""UE4 Editor Python script to batch-import PNG textures.

Run via:
    UE4Editor-Cmd.exe Moria.uproject -ExecutePythonScript="path/to/this_script.py" -nullrhi
"""
import unreal
import json
import os

MANIFEST_PATH = r"C:\Users\johnb\OneDrive\Documents\Projects\Moria-Replication\tools\texture-import-manifest.json"
LOG_PATH = r"C:\Users\johnb\OneDrive\Documents\Projects\Moria-Replication\tools\texture-import-results.json"


def import_textures():
    if not os.path.exists(MANIFEST_PATH):
        unreal.log_error("Manifest not found: " + MANIFEST_PATH)
        return

    with open(MANIFEST_PATH, "r") as f:
        entries = json.load(f)

    total = len(entries)
    unreal.log("Starting texture import: {} files".format(total))

    asset_tools = unreal.AssetToolsHelpers.get_asset_tools()
    results = {"imported": 0, "skipped": 0, "failed": 0, "errors": []}

    for i, entry in enumerate(entries):
        png_path = entry["source"]
        dest_path = entry["dest"]
        asset_name = entry.get("name", "")

        full_asset_path = dest_path + "/" + asset_name
        if unreal.EditorAssetLibrary.does_asset_exist(full_asset_path):
            results["skipped"] += 1
            continue

        try:
            task = unreal.AssetImportTask()
            task.set_editor_property("filename", png_path)
            task.set_editor_property("destination_path", dest_path)
            task.set_editor_property("destination_name", asset_name)
            task.set_editor_property("replace_existing", False)
            task.set_editor_property("automated", True)
            task.set_editor_property("save", True)

            asset_tools.import_asset_tasks([task])

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

    unreal.log("Texture import complete: {} imported, {} skipped, {} failed".format(
        results["imported"], results["skipped"], results["failed"]))

    with open(LOG_PATH, "w") as f:
        json.dump(results, f, indent=2)

    unreal.log("Results saved to " + LOG_PATH)


import_textures()
