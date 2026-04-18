"""BubbleData Level Reconstruction Tool — All 3 Phases.

Reads BD_*.json (FModel export of MorBubbleData) and generates a UE4 Python
editor script that spawns actors in a new level, reconstructing the bubble.

Phases:
  1. InstancedMeshCatalog  -> StaticMeshActor placement (mesh + transforms)
  2. ConstructionCatalog   -> Construction block actors (transforms from DecoVolumes)
  3. InstancedBreakableCatalog + DecoVolumes -> Breakable actors + deco volume markers

Usage:
    python reconstruct_level.py <BD_json>                    # Generate UE4 script (dry run)
    python reconstruct_level.py <BD_json> --output out.py    # Write to specific file
    python reconstruct_level.py <BD_json> --stats            # Show data stats only

The generated .py is meant to be run inside UE4's Python console or via
Edit -> Execute Python Script.
"""
import argparse
import json
import math
import os
import sys
from pathlib import Path

SCRIPT_DIR = Path(__file__).parent
REPO_ROOT = SCRIPT_DIR.parent


# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------

def parse_object_path(obj_path: str) -> str:
    """Convert FModel ObjectPath like '/Game/Art/Foo/Bar.2' to UE asset path.

    Strips the trailing '.N' object index that FModel appends.
    """
    if "." in obj_path:
        base = obj_path.rsplit(".", 1)[0]
    else:
        base = obj_path
    return base


def parse_asset_path_name(apn: str) -> str:
    """Convert AssetPathName like '/Game/Art/Foo/Bar.Bar' to '/Game/Art/Foo/Bar'."""
    if "." in apn:
        base = apn.rsplit(".", 1)[0]
    else:
        base = apn
    return base


def quat_to_rotator(x, y, z, w):
    """Convert quaternion (X,Y,Z,W) to UE Rotator (Pitch, Yaw, Roll) in degrees.

    Uses the same decomposition as FQuat::Rotator() in UE4.
    """
    # Singularity test
    singularity_test = z * x - w * y
    yaw_y = 2.0 * (w * z + x * y)
    yaw_x = 1.0 - 2.0 * (y * y + z * z)

    SINGULARITY_THRESHOLD = 0.4999995
    RAD_TO_DEG = 180.0 / math.pi

    if singularity_test < -SINGULARITY_THRESHOLD:
        pitch = -90.0
        yaw = math.atan2(yaw_y, yaw_x) * RAD_TO_DEG
        roll = (-yaw - 2.0 * math.atan2(x, w) * RAD_TO_DEG)
    elif singularity_test > SINGULARITY_THRESHOLD:
        pitch = 90.0
        yaw = math.atan2(yaw_y, yaw_x) * RAD_TO_DEG
        roll = (yaw - 2.0 * math.atan2(x, w) * RAD_TO_DEG)
    else:
        pitch = math.asin(2.0 * singularity_test) * RAD_TO_DEG
        yaw = math.atan2(yaw_y, yaw_x) * RAD_TO_DEG
        roll = math.atan2(-2.0 * (w * x + y * z),
                          1.0 - 2.0 * (x * x + y * y)) * RAD_TO_DEG

    return pitch, yaw, roll


def transform_to_ue(t: dict):
    """Extract (location, rotation, scale) from a BD transform dict."""
    trans = t.get("Translation", {})
    loc = (trans.get("X", 0), trans.get("Y", 0), trans.get("Z", 0))

    rot_q = t.get("Rotation", {})
    qx = rot_q.get("X", 0)
    qy = rot_q.get("Y", 0)
    qz = rot_q.get("Z", 0)
    qw = rot_q.get("W", 1)
    pitch, yaw, roll = quat_to_rotator(qx, qy, qz, qw)
    rot = (pitch, yaw, roll)

    sc = t.get("Scale3D", {})
    scale = (sc.get("X", 1), sc.get("Y", 1), sc.get("Z", 1))

    return loc, rot, scale


# ---------------------------------------------------------------------------
# Data loading
# ---------------------------------------------------------------------------

def load_bubble_data(json_path: str) -> dict:
    """Load and return the Properties dict from a BD_*.json file."""
    with open(json_path, "r", encoding="utf-8") as f:
        data = json.load(f)

    if isinstance(data, list):
        data = data[0]

    props = data.get("Properties", {})
    name = data.get("Name", "Unknown")
    return name, props


def get_stats(props: dict) -> dict:
    """Return a summary of counts in the bubble data."""
    imc = props.get("InstancedMeshCatalog", {})
    ibc = props.get("InstancedBreakableCatalog", {})
    cc = props.get("ConstructionCatalog", {})
    dv = props.get("DecoVolumes", {})
    ba = props.get("BreakableAttachmentDefinition", {})

    mesh_batches = imc.get("Batches", [])
    mesh_instances = sum(len(b.get("Instances", [])) for b in mesh_batches)
    brk_batches = ibc.get("Batches", [])
    brk_instances = sum(len(b.get("Instances", [])) for b in brk_batches)

    return {
        "mesh_batches": len(mesh_batches),
        "mesh_instances": mesh_instances,
        "construction_blocks": len(cc.get("Blocks", [])),
        "breakable_batches": len(brk_batches),
        "breakable_instances": brk_instances,
        "deco_volumes": len(dv.get("Volumes", [])),
        "breakable_attachments": len(ba.get("Attachments", [])),
    }


# ---------------------------------------------------------------------------
# UE4 Python script generation
# ---------------------------------------------------------------------------

def generate_ue4_script(name: str, props: dict) -> str:
    """Generate a complete UE4 Python editor script for level reconstruction."""
    lines = []
    w = lines.append

    w('"""Auto-generated level reconstruction script.')
    w(f'Bubble: {name}')
    w('Run via Edit -> Execute Python Script in UE4.27 editor."""')
    w('')
    w('import unreal')
    w('')
    w('def load_mesh(path):')
    w('    """Try to load a static mesh asset."""')
    w('    obj = unreal.load_asset(path)')
    w('    if obj is None:')
    w('        unreal.log_warning(f"Could not load mesh: {path}")')
    w('    return obj')
    w('')
    w('def load_material(path):')
    w('    """Try to load a material asset."""')
    w('    obj = unreal.load_asset(path)')
    w('    if obj is None:')
    w('        unreal.log_warning(f"Could not load material: {path}")')
    w('    return obj')
    w('')
    w('def spawn_static_mesh(mesh_path, materials, loc, rot, scale, label, folder):')
    w('    """Spawn a StaticMeshActor with the given transform."""')
    w('    mesh = load_mesh(mesh_path)')
    w('    if mesh is None:')
    w('        return None')
    w('    location = unreal.Vector(*loc)')
    w('    rotation = unreal.Rotator(*rot)')
    w('    actor = unreal.EditorLevelLibrary.spawn_actor_from_class(')
    w('        unreal.StaticMeshActor, location, rotation)')
    w('    if actor is None:')
    w('        unreal.log_warning(f"Failed to spawn actor for {label}")')
    w('        return None')
    w('    smc = actor.static_mesh_component')
    w('    smc.set_static_mesh(mesh)')
    w('    actor.set_actor_scale3d(unreal.Vector(*scale))')
    w('    actor.set_actor_label(label)')
    w('    actor.set_folder_path(folder)')
    w('    # Apply materials')
    w('    for i, mat_path in enumerate(materials):')
    w('        mat = load_material(mat_path)')
    w('        if mat is not None:')
    w('            smc.set_material(i, mat)')
    w('    return actor')
    w('')
    w('def spawn_note(loc, text, folder):')
    w('    """Spawn a Note actor as a marker/placeholder."""')
    w('    location = unreal.Vector(*loc)')
    w('    actor = unreal.EditorLevelLibrary.spawn_actor_from_class(')
    w('        unreal.Note, location, unreal.Rotator())')
    w('    if actor:')
    w('        actor.set_actor_label(text)')
    w('        actor.set_folder_path(folder)')
    w('    return actor')
    w('')
    w(f'BUBBLE_NAME = "{name}"')
    w('placed = 0')
    w('skipped = 0')
    w('errors = 0')
    w('')

    # ===== PHASE 1: Instanced Mesh Catalog =====
    w('# ' + '=' * 70)
    w(f'# PHASE 1: InstancedMeshCatalog  (static mesh placement)')
    w('# ' + '=' * 70)
    w('unreal.log(f"[{BUBBLE_NAME}] Phase 1: Placing static meshes...")')
    w('')

    imc = props.get("InstancedMeshCatalog", {})
    batches = imc.get("Batches", [])

    for bi, batch in enumerate(batches):
        defn = batch.get("Definition", {})
        instances = batch.get("Instances", [])
        if not instances:
            continue

        mesh_obj = defn.get("Mesh", {})
        mesh_path = parse_object_path(mesh_obj.get("ObjectPath", ""))
        mesh_name = mesh_obj.get("ObjectName", "Unknown")

        mat_paths = []
        for mat in defn.get("Materials", []):
            mat_paths.append(parse_object_path(mat.get("ObjectPath", "")))

        collision = defn.get("CollisionProfile", "BlockAll")

        w(f'# Batch {bi}: {mesh_name} ({len(instances)} instances)')
        w(f'_mesh_path = "{mesh_path}"')
        w(f'_materials = {mat_paths}')
        w(f'_folder = "Reconstruction/{name}/Meshes"')

        for inst in instances:
            inst_name = inst.get("Name", f"mesh_{bi}")
            transform = inst.get("Transform", {})
            loc, rot, scale = transform_to_ue(transform)

            w(f'a = spawn_static_mesh(_mesh_path, _materials, '
              f'{loc}, {rot}, {scale}, '
              f'"{inst_name}", _folder)')
            w(f'if a: placed += 1')
            w(f'else: skipped += 1')

        w('')

    # ===== PHASE 2: Construction Catalog =====
    w('# ' + '=' * 70)
    w(f'# PHASE 2: ConstructionCatalog  (construction blocks)')
    w('# ' + '=' * 70)
    w('unreal.log(f"[{BUBBLE_NAME}] Phase 2: Placing construction blocks...")')
    w('')

    cc = props.get("ConstructionCatalog", {})
    dv = props.get("DecoVolumes", {})
    ba = props.get("BreakableAttachmentDefinition", {})

    # Build DecoVolume lookup by name
    dv_lookup = {}
    for vol in dv.get("Volumes", []):
        dv_lookup[vol["Name"]] = vol

    # Build BreakableAttachment lookup
    ba_lookup = {}
    for att in ba.get("Attachments", []):
        ba_lookup[att["Key"]] = att.get("Value", {})

    blocks = cc.get("Blocks", [])
    if blocks:
        w('# Construction blocks use DecoVolume transforms (matched by Name)')
        w(f'_folder = "Reconstruction/{name}/Construction"')
        w('')

        for block in blocks:
            block_name = block["Name"]
            snap = block.get("Snap", {})
            stability = block.get("Stability", {})
            snap_rule = snap.get("SnapRule", "Unknown")
            grid_size = snap.get("GridSizeHandle", {}).get("RowName", "Default")
            stability_type = snap.get("StabilityHandle", {}).get("RowName", "Default")

            # Get transform from DecoVolume
            dv_entry = dv_lookup.get(block_name)
            if dv_entry:
                vol = dv_entry.get("Volume", {})
                base_transform = vol.get("BaseTransform", {})
                loc, rot, scale = transform_to_ue(base_transform)
                vol_spec = vol.get("VolumeSpec", {})
                shape = vol_spec.get("Shape", "Unknown")
                box_ext = vol_spec.get("BoxExtent", {})
                box_str = (f"({box_ext.get('X',0):.1f}, "
                           f"{box_ext.get('Y',0):.1f}, "
                           f"{box_ext.get('Z',0):.1f})")

                # Try to find the actual mesh for this construction block
                # Block names follow pattern: AB_<Kit>_<Type>_<Size>_<Variant>
                # We'll place a cube scaled to the box extent as a proxy
                w(f'# Construction: {block_name}')
                w(f'#   Snap: {snap_rule}, Grid: {grid_size}, Stability: {stability_type}')
                w(f'#   Volume: {shape}, BoxExtent: {box_str}')

                # Scale cube to match box extent (UE Cube is 100x100x100)
                bx = box_ext.get("X", 50) / 50.0
                by = box_ext.get("Y", 50) / 50.0
                bz = box_ext.get("Z", 50) / 50.0

                w(f'a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], '
                  f'{loc}, {rot}, ({bx:.4f}, {by:.4f}, {bz:.4f}), '
                  f'"{block_name}", _folder)')
                w(f'if a: placed += 1')
                w(f'else: skipped += 1')
                w('')
            else:
                w(f'# Construction: {block_name} -- NO DecoVolume transform found!')
                w(f'spawn_note((0,0,0), "MISSING: {block_name}", _folder)')
                w(f'skipped += 1')
                w('')

    # ===== PHASE 3: Breakables + Remaining DecoVolumes =====
    w('# ' + '=' * 70)
    w(f'# PHASE 3: Breakables + DecoVolumes')
    w('# ' + '=' * 70)
    w('unreal.log(f"[{BUBBLE_NAME}] Phase 3: Placing breakables and deco volumes...")')
    w('')

    ibc = props.get("InstancedBreakableCatalog", {})
    brk_batches = ibc.get("Batches", [])

    if brk_batches:
        w(f'_folder = "Reconstruction/{name}/Breakables"')
        w('')

        for bi, batch in enumerate(brk_batches):
            defn = batch.get("Definition", {})
            instances = batch.get("Instances", [])
            if not instances:
                continue

            bp_class = parse_asset_path_name(
                defn.get("BreakableClass", {}).get("AssetPathName", ""))
            mesh_info = defn.get("Mesh", {})
            mesh_asset = mesh_info.get("Mesh", {})
            mesh_path = parse_asset_path_name(mesh_asset.get("AssetPathName", ""))

            mat_paths = []
            for mat in mesh_info.get("Materials", []):
                mat_paths.append(parse_asset_path_name(
                    mat.get("AssetPathName", "")))

            bp_name = bp_class.rsplit("/", 1)[-1] if bp_class else f"Breakable_{bi}"

            w(f'# Breakable Batch {bi}: {bp_name} ({len(instances)} instances)')
            w(f'#   BP Class: {bp_class}')
            w(f'_brk_mesh = "{mesh_path}"')
            w(f'_brk_mats = {mat_paths}')

            for inst in instances:
                inst_name = inst.get("Name", f"breakable_{bi}")
                transform = inst.get("Transform", {})
                loc, rot, scale = transform_to_ue(transform)

                w(f'a = spawn_static_mesh(_brk_mesh, _brk_mats, '
                  f'{loc}, {rot}, {scale}, '
                  f'"{inst_name}", _folder)')
                w(f'if a: placed += 1')
                w(f'else: skipped += 1')

            w('')

    # Remaining DecoVolumes (not tied to construction blocks)
    construction_names = set(b["Name"] for b in blocks)
    extra_dvs = [v for v in dv.get("Volumes", [])
                 if v["Name"] not in construction_names]

    if extra_dvs:
        w(f'# --- Extra DecoVolumes (not construction blocks) ---')
        w(f'_folder = "Reconstruction/{name}/DecoVolumes"')
        w('')

        for vol_entry in extra_dvs:
            vol_name = vol_entry["Name"]
            vol = vol_entry.get("Volume", {})
            base_transform = vol.get("BaseTransform", {})
            loc, rot, scale = transform_to_ue(base_transform)
            vol_spec = vol.get("VolumeSpec", {})
            shape = vol_spec.get("Shape", "Unknown")
            box_ext = vol_spec.get("BoxExtent", {})

            # Place cube scaled to extent as a volume proxy
            bx = max(box_ext.get("X", 50), 1) / 50.0
            by = max(box_ext.get("Y", 50), 1) / 50.0
            bz = max(box_ext.get("Z", 50), 1) / 50.0

            is_breakable = vol_entry.get("Volume", {}).get("bIsBreakableFallback", False)
            label = f"DV_{vol_name}" + ("_BRK" if is_breakable else "")

            w(f'# DecoVolume: {vol_name} ({shape})')
            w(f'a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], '
              f'{loc}, {rot}, ({bx:.4f}, {by:.4f}, {bz:.4f}), '
              f'"{label}", _folder)')
            w(f'if a: placed += 1')
            w(f'else: skipped += 1')

        w('')

    # ===== Summary =====
    w('# ' + '=' * 70)
    w('# SUMMARY')
    w('# ' + '=' * 70)
    w('unreal.log(f"[{BUBBLE_NAME}] Reconstruction complete: {placed} placed, {skipped} skipped, {errors} errors")')
    w('')

    return "\n".join(lines)


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

def main():
    parser = argparse.ArgumentParser(
        description="BubbleData Level Reconstruction Tool")
    parser.add_argument("json_file",
                        help="Path to BD_*.json file (FModel export)")
    parser.add_argument("--output", "-o",
                        help="Output .py file (default: auto-named in scripts/)")
    parser.add_argument("--stats", action="store_true",
                        help="Show data statistics only, don't generate script")
    parser.add_argument("--all", action="store_true",
                        help="Process ALL BD_*.json files in the catalog directory")
    args = parser.parse_args()

    json_path = args.json_file

    if args.all:
        # Process all BD_ files in the same directory
        catalog_dir = Path(json_path).parent
        bd_files = sorted(catalog_dir.glob("BD_BB_*.json"))
        print(f"Found {len(bd_files)} BD_ files in {catalog_dir}")

        for bd_file in bd_files:
            name, props = load_bubble_data(str(bd_file))
            stats = get_stats(props)
            total = (stats["mesh_instances"] + stats["construction_blocks"]
                     + stats["breakable_instances"] + stats["deco_volumes"])

            if args.stats:
                print(f"  {name}: {total} total "
                      f"({stats['mesh_instances']} meshes, "
                      f"{stats['construction_blocks']} construction, "
                      f"{stats['breakable_instances']} breakables, "
                      f"{stats['deco_volumes']} deco)")
            else:
                script = generate_ue4_script(name, props)
                out_name = f"reconstruct_{name}.py"
                out_dir = REPO_ROOT / "scripts" / "reconstructed"
                out_dir.mkdir(parents=True, exist_ok=True)
                out_path = out_dir / out_name
                with open(str(out_path), "w", encoding="utf-8") as f:
                    f.write(script)
                print(f"  {name} -> {out_path.name} ({total} actors)")

        if not args.stats:
            print(f"\nGenerated scripts in: {out_dir}")
        return

    # Single file mode
    if not os.path.exists(json_path):
        print(f"ERROR: File not found: {json_path}")
        sys.exit(1)

    name, props = load_bubble_data(json_path)
    stats = get_stats(props)

    print(f"Bubble: {name}")
    print(f"  Mesh batches:          {stats['mesh_batches']}")
    print(f"  Mesh instances:        {stats['mesh_instances']}")
    print(f"  Construction blocks:   {stats['construction_blocks']}")
    print(f"  Breakable batches:     {stats['breakable_batches']}")
    print(f"  Breakable instances:   {stats['breakable_instances']}")
    print(f"  Deco volumes:          {stats['deco_volumes']}")
    print(f"  Breakable attachments: {stats['breakable_attachments']}")

    total = (stats["mesh_instances"] + stats["construction_blocks"]
             + stats["breakable_instances"] + stats["deco_volumes"])
    print(f"  Total actors to place: {total}")

    if args.stats:
        return

    script = generate_ue4_script(name, props)

    if args.output:
        out_path = args.output
    else:
        out_path = str(REPO_ROOT / "scripts" / "reconstructed"
                       / f"reconstruct_{name}.py")

    Path(out_path).parent.mkdir(parents=True, exist_ok=True)

    with open(out_path, "w", encoding="utf-8") as f:
        f.write(script)

    line_count = script.count("\n") + 1
    print(f"\nGenerated: {out_path}")
    print(f"  {line_count} lines of UE4 Python")
    print(f"  Run in UE4 editor: Edit -> Execute Python Script")


if __name__ == "__main__":
    main()
