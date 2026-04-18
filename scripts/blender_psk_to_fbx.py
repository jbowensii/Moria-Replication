"""Blender headless script: convert PSK/PSKX files to FBX.
Usage: blender --background --python blender_psk_to_fbx.py -- input.pskx output.fbx
"""
import sys
import os

# Must enable the extension before using its operators
import bpy
import addon_utils

# Enable the PSK/PSA extension
ext_name = 'bl_ext.blender_org.io_scene_psk_psa'
try:
    addon_utils.enable(ext_name)
    print("Enabled: " + ext_name)
except Exception as e:
    # Try alternate
    try:
        addon_utils.enable('bl_ext.user_default.io_scene_psk_psa')
        print("Enabled: bl_ext.user_default.io_scene_psk_psa")
    except Exception as e2:
        print("ERROR enabling addon: " + str(e) + " / " + str(e2))

argv = sys.argv[sys.argv.index("--") + 1:]
psk_in = argv[0]
fbx_out = argv[1]

bpy.ops.wm.read_homefile(use_empty=True)

# Re-enable after read_homefile (which resets addons)
try:
    addon_utils.enable(ext_name)
except:
    try:
        addon_utils.enable('bl_ext.user_default.io_scene_psk_psa')
    except:
        pass

# Import PSK/PSKX using the addon operator
try:
    bpy.ops.psk.import_file(filepath=psk_in)
    print("PSK import OK")
except Exception as e:
    print("PSK operator failed: " + str(e))
    # Fallback: try import_scene.psk
    try:
        bpy.ops.import_scene.psk(filepath=psk_in)
        print("import_scene.psk OK")
    except Exception as e2:
        print("FATAL: Cannot import PSK: " + str(e2))
        sys.exit(1)

# Ensure output dir exists
os.makedirs(os.path.dirname(fbx_out), exist_ok=True)

# Export FBX with UE4-compatible settings
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

print("CONVERTED: " + psk_in + " -> " + fbx_out)
