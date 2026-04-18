"""Blender headless script: convert glTF to FBX.

Single file mode:
    blender --background --python blender_gltf_to_fbx.py -- input.gltf output.fbx

Batch mode (via manifest):
    blender --background --python blender_gltf_to_fbx.py -- --manifest manifest.json
"""
import sys
import os
import json
import bpy

argv = sys.argv[sys.argv.index("--") + 1:]

if argv[0] == "--manifest":
    # Batch mode
    with open(argv[1], "r") as f:
        pairs = json.load(f)
else:
    # Single file mode
    pairs = [[argv[0], argv[1]]]

total = len(pairs)
converted = 0
errors = 0

for i, (gltf_in, fbx_out) in enumerate(pairs, 1):
    try:
        bpy.ops.wm.read_homefile(use_empty=True)
        bpy.ops.import_scene.gltf(filepath=gltf_in)
        os.makedirs(os.path.dirname(fbx_out), exist_ok=True)
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
        converted += 1
        if i % 25 == 0 or i == total:
            print(f"PROGRESS: {i}/{total} ({converted} ok, {errors} err)", flush=True)
    except Exception as e:
        errors += 1
        print(f"ERROR [{i}/{total}] {gltf_in}: {e}", flush=True)

print(f"BATCH COMPLETE: {converted}/{total} converted, {errors} errors")
