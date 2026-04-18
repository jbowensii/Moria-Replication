"""Blender script: batch convert PSA animation files to FBX.

Uses io_scene_psk_psa's PsaReader + importer directly (no operator needed).

Usage:
    blender --background --python blender_psa_to_fbx.py -- <psa_dir> <fbx_dir> [--limit N]
"""
import bpy
import os
import sys
import json
import time
import math
from pathlib import Path
from mathutils import Vector, Quaternion, Matrix

# ── Setup psk_psa_py from the extension's wheels ────────────────────────
ADDON_DIR = os.path.join(
    os.environ.get("APPDATA", ""),
    "Blender Foundation", "Blender", "5.0", "extensions",
    "blender_org", "io_scene_psk_psa"
)
WHEEL_DIR = os.path.join(ADDON_DIR, "wheels")
WHEEL_PATH = os.path.join(WHEEL_DIR, "psk_psa_py-0.0.1-py3-none-any.whl")

if os.path.exists(WHEEL_PATH):
    sys.path.insert(0, WHEEL_PATH)
sys.path.insert(0, ADDON_DIR)

from psk_psa_py.psa.reader import PsaReader
from psa.importer import import_psa, PsaImportOptions


def clear_scene():
    """Remove all objects and data."""
    for obj in list(bpy.data.objects):
        bpy.data.objects.remove(obj, do_unlink=True)
    for arm in list(bpy.data.armatures):
        bpy.data.armatures.remove(arm)
    for act in list(bpy.data.actions):
        bpy.data.actions.remove(act)
    for mesh in list(bpy.data.meshes):
        bpy.data.meshes.remove(mesh)


def build_armature_from_psa(psa_reader):
    """Create a Blender armature from PSA bone data."""
    arm_data = bpy.data.armatures.new("PSA_Armature")
    arm_obj = bpy.data.objects.new("PSA_Armature", arm_data)
    bpy.context.collection.objects.link(arm_obj)
    bpy.context.view_layer.objects.active = arm_obj
    arm_obj.select_set(True)

    bpy.ops.object.mode_set(mode='EDIT')

    bones = psa_reader.bones
    edit_bones = []

    for i, psa_bone in enumerate(bones):
        bone_name = psa_bone.name
        if isinstance(bone_name, bytes):
            bone_name = bone_name.decode('utf-8', errors='replace')
        bone_name = bone_name.strip().rstrip('\x00')
        eb = arm_data.edit_bones.new(bone_name)

        # PSA bones have position and rotation relative to parent
        pos = Vector((psa_bone.location.x, -psa_bone.location.y, psa_bone.location.z))
        rot = Quaternion((psa_bone.rotation.w, psa_bone.rotation.x, -psa_bone.rotation.y, psa_bone.rotation.z))

        # Build transform matrix
        mat = rot.to_matrix().to_4x4()
        mat.translation = pos

        # Set parent
        parent_idx = psa_bone.parent_index
        if parent_idx >= 0 and parent_idx < len(edit_bones):
            eb.parent = edit_bones[parent_idx]
            # Child bones are in parent space
            parent_mat = edit_bones[parent_idx].matrix
            mat = parent_mat @ mat

        # Apply the transform - edit bones need head/tail
        eb.head = mat.translation
        eb.tail = mat.translation + mat.to_3x3() @ Vector((0, 0.05, 0))
        eb.roll = 0

        edit_bones.append(eb)

    bpy.ops.object.mode_set(mode='OBJECT')
    return arm_obj


def export_fbx(fbx_path, arm_obj):
    """Export armature with animation as FBX."""
    os.makedirs(os.path.dirname(fbx_path), exist_ok=True)

    bpy.ops.object.select_all(action='DESELECT')
    arm_obj.select_set(True)
    bpy.context.view_layer.objects.active = arm_obj

    bpy.ops.export_scene.fbx(
        filepath=str(fbx_path),
        use_selection=True,
        object_types={'ARMATURE'},
        bake_anim=True,
        bake_anim_use_all_actions=False,
        bake_anim_use_nla_strips=False,
        bake_anim_force_startend_keying=True,
        add_leaf_bones=False,
        primary_bone_axis='X',
        secondary_bone_axis='Y',
        axis_forward='-Y',
        axis_up='Z',
        global_scale=1.0,
        apply_scale_options='FBX_SCALE_ALL',
    )


def main():
    argv = sys.argv
    if "--" in argv:
        argv = argv[argv.index("--") + 1:]
    else:
        print("Usage: blender --background --python blender_psa_to_fbx.py -- <psa_dir> <fbx_dir> [--limit N]")
        return

    psa_dir = Path(argv[0])
    fbx_dir = Path(argv[1])
    limit = None

    if "--limit" in argv:
        idx = argv.index("--limit")
        limit = int(argv[idx + 1])

    # Collect all PSA files
    psa_files = sorted(psa_dir.rglob("*.psa"))
    print(f"Found {len(psa_files)} PSA files in {psa_dir}")

    if limit:
        psa_files = psa_files[:limit]
        print(f"  Limited to {limit}")

    success = 0
    failed = 0
    skipped = 0
    errors = []
    start = time.time()

    for i, psa_path in enumerate(psa_files):
        rel = psa_path.relative_to(psa_dir)
        fbx_path = fbx_dir / rel.with_suffix(".fbx")

        if fbx_path.exists():
            skipped += 1
            continue

        try:
            clear_scene()

            # Read PSA
            psa_reader = PsaReader(str(psa_path))

            if len(psa_reader.sequences) == 0:
                errors.append((str(rel), "No sequences in PSA"))
                failed += 1
                continue

            # Build armature from PSA bone data
            arm_obj = build_armature_from_psa(psa_reader)

            # Import animation onto armature
            options = PsaImportOptions()
            result = import_psa(bpy.context, psa_reader, arm_obj, options)

            # Export as FBX
            export_fbx(str(fbx_path), arm_obj)
            success += 1

            if (success + failed) % 100 == 0:
                elapsed = time.time() - start
                rate = (success + failed) / elapsed if elapsed > 0 else 0
                print(f"  Progress: {success} ok, {failed} fail, {skipped} skip "
                      f"({rate:.1f}/s, {elapsed:.0f}s)")

        except Exception as e:
            errors.append((str(rel), str(e)))
            failed += 1
            if failed <= 20:
                import traceback
                print(f"  FAIL [{rel}]: {e}")
                traceback.print_exc()

    elapsed = time.time() - start
    print(f"\n{'='*60}")
    print(f"  PSA -> FBX Conversion Complete — {elapsed:.0f}s")
    print(f"{'='*60}")
    print(f"  Success:  {success}")
    print(f"  Failed:   {failed}")
    print(f"  Skipped:  {skipped}")
    print(f"  Total:    {len(psa_files)}")
    print(f"{'='*60}")

    if errors:
        os.makedirs(str(fbx_dir), exist_ok=True)
        error_log = fbx_dir / "_conversion_errors.json"
        with open(error_log, "w") as f:
            json.dump(errors, f, indent=2)
        print(f"  Error log: {error_log}")


if __name__ == "__main__":
    main()
