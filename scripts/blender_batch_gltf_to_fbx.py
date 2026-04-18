"""Blender batch script: convert multiple glTF files to FBX.
Usage: blender --background --python this_script.py -- manifest.json
"""
import sys
import json
import os
import bpy

argv = sys.argv[sys.argv.index("--") + 1:]
manifest_path = argv[0]

with open(manifest_path, "r") as f:
    pairs = json.load(f)

total = len(pairs)
for i, (gltf_in, fbx_out) in enumerate(pairs, 1):
    try:
        # Reset scene
        bpy.ops.wm.read_homefile(use_empty=True)

        # Import glTF
        bpy.ops.import_scene.gltf(filepath=gltf_in)

        # Ensure output directory exists
        os.makedirs(os.path.dirname(fbx_out), exist_ok=True)

        # Export FBX -- UE4-compatible settings
        bpy.ops.export_scene.fbx(
            filepath=fbx_out,
            axis_forward='-Z',
            axis_up='Y',
            use_selection=False,
            global_scale=1.0,
            apply_unit_scale=True,
            apply_scale_options='FBX_SCALE_ALL',
            mesh_smooth_type='FACE',
            add_leaf_bones=False,
        )

        if i % 25 == 0 or i == total:
            print(f"PROGRESS: {i}/{total} converted", flush=True)

    except Exception as e:
        print(f"ERROR converting {gltf_in}: {e}", flush=True)

print(f"BATCH COMPLETE: {total} files processed")
