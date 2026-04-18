
import sys, json, os, bpy, addon_utils
addon_utils.enable('bl_ext.blender_org.io_scene_psk_psa')

argv = sys.argv[sys.argv.index("--") + 1:]
with open(argv[0], "r") as f:
    pairs = json.load(f)

total = len(pairs)
converted = 0
errors = 0
for i, (psk_in, fbx_out) in enumerate(pairs, 1):
    try:
        bpy.ops.wm.read_homefile(use_empty=True)
        addon_utils.enable('bl_ext.blender_org.io_scene_psk_psa')
        bpy.ops.psk.import_file(filepath=psk_in)
        os.makedirs(os.path.dirname(fbx_out), exist_ok=True)
        bpy.ops.export_scene.fbx(
            filepath=fbx_out, axis_forward='-Z', axis_up='Y',
            use_selection=False, global_scale=1.0, apply_unit_scale=True,
            apply_scale_options='FBX_SCALE_ALL', mesh_smooth_type='FACE',
            add_leaf_bones=False)
        converted += 1
        if i % 100 == 0 or i == total:
            print(f"PROGRESS: {i}/{total} ({converted} ok, {errors} err)", flush=True)
    except Exception as e:
        errors += 1
        if errors <= 20:
            print(f"ERROR [{i}]: {os.path.basename(psk_in)}: {e}", flush=True)

print(f"BATCH COMPLETE: {converted}/{total} converted, {errors} errors")
