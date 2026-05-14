"""UE4 Editor Python script — import PorterGoat icon PNGs as Texture2D assets.

Run via:
    UE4Editor-Cmd.exe project/Moria.uproject \
      -ExecutePythonScript="scripts/ue4_import_portergoat_icons.py" \
      -nullrhi -unattended -nopause -nosplash
"""
import unreal
import os

ENTRIES = [
    {
        "source": r"C:\Users\johnb\OneDrive\Documents\Projects\Moria-Replication\project\Content\Mods\PorterGoat\Icons\T_PorterGoatBell_src.png",
        "dest":   "/Game/Mods/PorterGoat/Icons",
        "name":   "T_PorterGoatBell",
    },
    {
        "source": r"C:\Users\johnb\OneDrive\Documents\Projects\Moria-Replication\project\Content\Mods\PorterGoat\Icons\T_PorterGoatSaddlebags_src.png",
        "dest":   "/Game/Mods/PorterGoat/Icons",
        "name":   "T_PorterGoatSaddlebags",
    },
]

LOG_PATH = r"C:\Users\johnb\OneDrive\Documents\Projects\Moria-Replication\tools\portergoat-icon-import-results.json"


def run():
    asset_tools = unreal.AssetToolsHelpers.get_asset_tools()
    results = {"imported": [], "skipped": [], "failed": []}

    for entry in ENTRIES:
        png_path   = entry["source"]
        dest_path  = entry["dest"]
        asset_name = entry["name"]
        full       = dest_path + "/" + asset_name

        if not os.path.exists(png_path):
            results["failed"].append({"name": asset_name, "error": "source missing: " + png_path})
            unreal.log_error("Missing source: " + png_path)
            continue

        # Overwrite if exists -- icons may be re-imported on updated art.
        if unreal.EditorAssetLibrary.does_asset_exist(full):
            unreal.EditorAssetLibrary.delete_asset(full)

        task = unreal.AssetImportTask()
        task.set_editor_property("filename", png_path)
        task.set_editor_property("destination_path", dest_path)
        task.set_editor_property("destination_name", asset_name)
        task.set_editor_property("replace_existing", True)
        task.set_editor_property("automated", True)
        task.set_editor_property("save", True)

        asset_tools.import_asset_tasks([task])

        if unreal.EditorAssetLibrary.does_asset_exist(full):
            # Set LODGroup = UI (sRGB on, no mips, NearestNeighbor disabled by default for UI is fine)
            tex = unreal.EditorAssetLibrary.load_asset(full)
            if tex:
                try:
                    tex.set_editor_property("lod_group", unreal.TextureGroup.TEXTUREGROUP_UI)
                    tex.set_editor_property("srgb", True)
                    tex.set_editor_property("never_stream", True)
                    unreal.EditorAssetLibrary.save_asset(full)
                except Exception as e:
                    unreal.log_warning("LODGroup set failed for {}: {}".format(asset_name, e))
            results["imported"].append(full)
            unreal.log("Imported: " + full)
        else:
            results["failed"].append({"name": asset_name, "error": "asset did not materialize"})
            unreal.log_error("Failed: " + asset_name)

    import json
    with open(LOG_PATH, "w") as f:
        json.dump(results, f, indent=2)
    unreal.log("Results: " + LOG_PATH)


run()
