"""Auto-generated level reconstruction script.
Bubble: BD_BB_SnakingRiver_Urban
Run via Edit -> Execute Python Script in UE4.27 editor."""

import unreal

def load_mesh(path):
    """Try to load a static mesh asset."""
    obj = unreal.load_asset(path)
    if obj is None:
        unreal.log_warning(f"Could not load mesh: {path}")
    return obj

def load_material(path):
    """Try to load a material asset."""
    obj = unreal.load_asset(path)
    if obj is None:
        unreal.log_warning(f"Could not load material: {path}")
    return obj

def spawn_static_mesh(mesh_path, materials, loc, rot, scale, label, folder):
    """Spawn a StaticMeshActor with the given transform."""
    mesh = load_mesh(mesh_path)
    if mesh is None:
        return None
    location = unreal.Vector(*loc)
    rotation = unreal.Rotator(*rot)
    actor = unreal.EditorLevelLibrary.spawn_actor_from_class(
        unreal.StaticMeshActor, location, rotation)
    if actor is None:
        unreal.log_warning(f"Failed to spawn actor for {label}")
        return None
    smc = actor.static_mesh_component
    smc.set_static_mesh(mesh)
    actor.set_actor_scale3d(unreal.Vector(*scale))
    actor.set_actor_label(label)
    actor.set_folder_path(folder)
    # Apply materials
    for i, mat_path in enumerate(materials):
        mat = load_material(mat_path)
        if mat is not None:
            smc.set_material(i, mat)
    return actor

def spawn_note(loc, text, folder):
    """Spawn a Note actor as a marker/placeholder."""
    location = unreal.Vector(*loc)
    actor = unreal.EditorLevelLibrary.spawn_actor_from_class(
        unreal.Note, location, unreal.Rotator())
    if actor:
        actor.set_actor_label(text)
        actor.set_folder_path(folder)
    return actor

BUBBLE_NAME = "BD_BB_SnakingRiver_Urban"
placed = 0
skipped = 0
errors = 0

# ======================================================================
# PHASE 1: InstancedMeshCatalog  (static mesh placement)
# ======================================================================
unreal.log(f"[{BUBBLE_NAME}] Phase 1: Placing static meshes...")

# Batch 0: StaticMesh'Cube' (25 instances)
_mesh_path = "/Engine/BasicShapes/Cube"
_materials = ['/Game/Art/Assets/Kits/Architecture/Suburbs/Destructable/Materials/MI_Suburbs_Wall_Non_Dest']
_folder = "Reconstruction/BD_BB_SnakingRiver_Urban/Meshes"
a = spawn_static_mesh(_mesh_path, _materials, (5800.0, 4500.0, 250.0), (0.0, 0.0, -0.0), (8.0, 3.0, 5.0), "Cube10", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (6050.0, 4950.0, 350.0), (0.0, 0.0, -0.0), (1.0, 6.0, 7.0), "Cube11", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5550.0, 5200.0, 200.0), (0.0, 0.0, -0.0), (9.0, 1.0, 4.0), "Cube12", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4300.0, 5200.0, 200.0), (0.0, 0.0, -0.0), (16.0, 1.0, 4.0), "Cube13", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3550.0, 5750.0, 200.0), (0.0, 0.0, -0.0), (1.0, 10.0, 4.0), "Cube14", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2850.0, 5600.0, 200.0), (0.0, 0.0, -0.0), (1.0, 12.0, 4.0), "Cube15", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3050.0, 5900.0, 750.0), (0.0, 0.0, -0.0), (11.0, 6.0, 1.0), "Cube16", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2050.0, 6250.0, 1750.0), (0.0, 0.0, -0.0), (9.0, 1.0, 19.0), "Cube17", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1300.0, 6000.0, 1850.0), (0.0, 0.0, -0.0), (6.0, 6.0, 21.0), "Cube18", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (700.0, 5900.0, 1850.0), (0.0, 0.0, -0.0), (6.0, 6.0, 21.0), "Cube19", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5750.0, 2550.0, 1350.0), (0.0, 0.0, -0.0), (11.0, 6.0, 13.0), "Cube2", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (350.0, 5000.0, 1750.0), (0.0, 0.0, -0.0), (4.0, 12.0, 19.0), "Cube20", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2550.0, 5050.0, 200.0), (0.0, 0.0, -0.0), (5.0, 1.0, 4.0), "Cube21", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4650.0, 5000.0, 200.0), (0.0, 0.0, -0.0), (9.0, 3.0, 4.0), "Cube22", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (850.0, 5000.0, 750.0), (0.0, 0.0, -0.0), (6.0, 12.0, 1.0), "Cube24", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3200.0, 6100.0, 350.0), (0.0, 0.0, -0.0), (6.0, 3.0, 7.0), "Cube25", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1360.0, 5000.0, 750.0), (0.0, 0.0, -0.0), (6.0, 12.0, 1.0), "Cube26", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1680.0, 5330.0, 750.0), (0.0, 89.99999818714215, -0.0), (6.0, 12.0, 1.0), "Cube27", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (6350.0, 3150.0, 1500.0), (0.0, 0.0, -0.0), (1.0, 30.0, 22.0), "Cube3", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4850.0, 6150.0, 1700.0), (0.0, 0.0, -0.0), (19.0, 2.0, 22.0), "Cube4", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4850.0, 5750.0, 650.0), (0.0, 0.0, -0.0), (19.0, 6.0, 1.0), "Cube5", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (6000.0, 5700.0, 1550.0), (0.0, 0.0, -0.0), (4.0, 9.0, 25.0), "Cube6", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (6250.0, 4950.0, 1450.0), (0.0, 0.0, -0.0), (3.0, 6.0, 23.0), "Cube7", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4850.0, 3100.0, 250.0), (0.0, 0.0, -0.0), (1.0, 25.0, 5.0), "Cube8", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5200.0, 4300.0, 250.0), (0.0, 0.0, -0.0), (6.0, 1.0, 5.0), "Cube9", _folder)
if a: placed += 1
else: skipped += 1

# Batch 1: StaticMesh'Plane' (1 instances)
_mesh_path = "/Engine/BasicShapes/Plane"
_materials = ['/Game/FX/WaterInteraction/Materials/MI_WaterShallow']
_folder = "Reconstruction/BD_BB_SnakingRiver_Urban/Meshes"
a = spawn_static_mesh(_mesh_path, _materials, (3200.0, 3200.0, 630.0), (2.8000000540964242e-05, 0.0, -0.0), (59.0, 59.0, 1.0), "Plane_2", _folder)
if a: placed += 1
else: skipped += 1

# Batch 2: StaticMesh'NonDest_Floor_Trim_Corner_M' (6 instances)
_mesh_path = "/Game/Art/Assets/Kits/Architecture/Non_D/NonDest_Floor_Trim_Corner_M"
_materials = ['/Game/Art/Assets/Kits/Architecture/Suburbs/Materials/Suburbs_Trim_Sheet_A/MI_Suburbs_Trim_Sheet_A']
_folder = "Reconstruction/BD_BB_SnakingRiver_Urban/Meshes"
a = spawn_static_mesh(_mesh_path, _materials, (4200.0, 5150.0, 700.0), (0.0, 0.0, -0.0), (1.0, 1.0, 1.0), "NonDest_Floor_Trim_Corner_M_33", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5100.0, 5150.0, 700.0), (0.0, 90.0001164887758, -0.0), (1.0, 1.0, 1.0), "NonDest_Floor_Trim_Corner_M2", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2500.0, 5598.883, 797.85913), (0.0, 90.0001164887758, -0.0), (1.0, 1.0, 1.0), "NonDest_Floor_Trim_Corner_M3_128", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1700.0, 5000.0, 796.90015), (0.0, 90.0001164887758, -0.0), (1.0, 1.0, 1.0), "NonDest_Floor_Trim_Corner_M4_163", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2300.0, 5300.0, 800.0), (0.0, 90.0001164887758, -0.0), (1.0, 1.0, 1.0), "NonDest_Floor_Trim_Corner_M5_180", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5400.0, 4350.0, 797.563), (0.0, -89.99957359878371, 0.0), (1.0, 1.0, 1.0), "NonDest_Floor_Trim_Corner_M6", _folder)
if a: placed += 1
else: skipped += 1

# Batch 3: StaticMesh'NonDest_Floor_Trim_Thin_1_5M_A' (5 instances)
_mesh_path = "/Game/Art/Assets/Kits/Architecture/Non_D/NonDest_Floor_Trim_Thin_1_5M_A"
_materials = ['/Game/Art/Assets/Kits/Architecture/Suburbs/Materials/Suburbs_Trim_Sheet_A/MI_Suburbs_Trim_Sheet_A']
_folder = "Reconstruction/BD_BB_SnakingRiver_Urban/Meshes"
a = spawn_static_mesh(_mesh_path, _materials, (4200.0, 5150.0, 700.0), (0.0, -89.99999818714215, 0.0), (1.0, 1.0, 1.0), "NonDest_Floor_Trim_Thin_1_5M_A_42", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5100.0, 5000.0, 700.0), (0.0, 90.00026882252801, -0.0), (1.0, 1.0, 1.0), "NonDest_Floor_Trim_Thin_1_5M_A2", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4050.0, 5150.0, 700.0), (0.0, 0.0, -0.0), (1.0, 1.0, 1.0), "NonDest_Floor_Trim_Thin_1_5M_A3_61", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5399.8857, 4499.9995, 797.563), (0.0, -89.99945205658098, 0.0), (1.0, 1.0, 1.0), "NonDest_Floor_Trim_Thin_1_5M_A5", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5100.0, 4350.485, 797.7731), (0.0, -179.99980192457332, 0.0), (1.0, 1.0, 1.0), "NonDest_Floor_Trim_Thin_1_5M_A6_211", _folder)
if a: placed += 1
else: skipped += 1

# Batch 4: StaticMesh'NonDest_Floor_Trim_Thin_1M_A' (2 instances)
_mesh_path = "/Game/Art/Assets/Kits/Architecture/Non_D/NonDest_Floor_Trim_Thin_1M_A"
_materials = ['/Game/Art/Assets/Kits/Architecture/Suburbs/Materials/Suburbs_Trim_Sheet_A/MI_Suburbs_Trim_Sheet_A']
_folder = "Reconstruction/BD_BB_SnakingRiver_Urban/Meshes"
a = spawn_static_mesh(_mesh_path, _materials, (2500.4814, 5500.0, 798.02325), (0.0, 90.00011648875932, -0.0), (1.0, 1.0, 1.0), "NonDest_Floor_Trim_Thin_1_5M_A4_146", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3650.0, 5150.0, 700.0), (0.0, 0.0, -0.0), (1.0, 1.0, 1.0), "NonDest_Floor_Trim_Thin_1M_A_64", _folder)
if a: placed += 1
else: skipped += 1

# Batch 5: StaticMesh'NonDest_Floor_Trim_Thin_2M_A' (15 instances)
_mesh_path = "/Game/Art/Assets/Kits/Architecture/Non_D/NonDest_Floor_Trim_Thin_2M_A"
_materials = ['/Game/Art/Assets/Kits/Architecture/Suburbs/Materials/Suburbs_Trim_Sheet_A/MI_Suburbs_Trim_Sheet_A']
_folder = "Reconstruction/BD_BB_SnakingRiver_Urban/Meshes"
a = spawn_static_mesh(_mesh_path, _materials, (2300.0, 5299.615, 798.116), (0.0, 0.0, -0.0), (1.0, 1.0, 1.0), "NonDest_Floor_Trim_Thin_1M_A2_183", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2500.6953, 5299.615, 798.116), (0.0, 90.0001164887758, -0.0), (1.0, 1.0, 1.0), "NonDest_Floor_Trim_Thin_1M_A3_190", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3700.0, 5450.0, 697.6511), (0.0, -179.99976777351753, 0.0), (1.0, 1.0, 1.0), "NonDest_Floor_Trim_Thin_2M_A_113", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2450.0, 5200.0, 700.0), (0.0, -89.99978589276644, 0.0), (1.0, 1.0, 1.0), "NonDest_Floor_Trim_Thin_2M_A10", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3900.455, 5598.0938, 796.42), (0.0, 90.00002735739477, -0.0), (1.0, 1.0, 1.0), "NonDest_Floor_Trim_Thin_2M_A11", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3900.455, 5798.0938, 796.42), (0.0, 90.00002735739477, -0.0), (1.0, 1.0, 1.0), "NonDest_Floor_Trim_Thin_2M_A12", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3900.455, 5998.0938, 796.42), (0.0, 90.00002735739477, -0.0), (1.0, 1.0, 1.0), "NonDest_Floor_Trim_Thin_2M_A13", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3899.9998, 5450.0, 697.6511), (0.0, -179.99976777351753, 0.0), (1.0, 1.0, 1.0), "NonDest_Floor_Trim_Thin_2M_A2", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3700.0005, 5598.0938, 796.42), (0.0, -6.103515418554748e-05, 0.0), (1.0, 1.0, 1.0), "NonDest_Floor_Trim_Thin_2M_A3", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3499.9998, 5598.094, 796.42), (0.0, -6.103515418554748e-05, 0.0), (1.0, 1.0, 1.0), "NonDest_Floor_Trim_Thin_2M_A4", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2700.0005, 5598.0938, 796.42), (0.0, -6.103515418554748e-05, 0.0), (1.0, 1.0, 1.0), "NonDest_Floor_Trim_Thin_2M_A5", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2499.9998, 5598.094, 796.42), (0.0, -6.103515418554748e-05, 0.0), (1.0, 1.0, 1.0), "NonDest_Floor_Trim_Thin_2M_A6", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2900.0, 5450.0, 700.0), (0.0, -179.99998633961752, -0.0), (1.0, 1.0, 1.0), "NonDest_Floor_Trim_Thin_2M_A7_171", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2700.0, 5450.0, 700.0), (0.0, -179.99998633961752, -0.0), (1.0, 1.0, 1.0), "NonDest_Floor_Trim_Thin_2M_A8", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2450.0, 5400.0, 700.0), (0.0, -89.99978589276644, 0.0), (1.0, 1.0, 1.0), "NonDest_Floor_Trim_Thin_2M_A9", _folder)
if a: placed += 1
else: skipped += 1

# Batch 6: StaticMesh'NonDest_Floor_Trim_Thin_3M_A' (35 instances)
_mesh_path = "/Game/Art/Assets/Kits/Architecture/Non_D/NonDest_Floor_Trim_Thin_3M_A"
_materials = ['/Game/Art/Assets/Kits/Architecture/Suburbs/Materials/Suburbs_Trim_Sheet_A/MI_Suburbs_Trim_Sheet_A']
_folder = "Reconstruction/BD_BB_SnakingRiver_Urban/Meshes"
a = spawn_static_mesh(_mesh_path, _materials, (4650.0, 4850.0, 700.0), (0.0, 0.0, -0.0), (1.0, 1.0, 1.0), "NonDest_Floor_Trim_Thin_3M_A_29", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2300.794, 5000.0, 796.4373), (0.0, 90.0001164887758, -0.0), (1.0, 1.0, 1.0), "NonDest_Floor_Trim_Thin_3M_A10_154", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2000.794, 4999.846, 796.4373), (0.0, -3.051757709276941e-05, 0.0), (1.0, 1.0, 1.0), "NonDest_Floor_Trim_Thin_3M_A11", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1700.794, 4999.846, 796.4373), (0.0, -3.051757709276941e-05, 0.0), (1.0, 1.0, 1.0), "NonDest_Floor_Trim_Thin_3M_A12", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1700.794, 4699.846, 796.4373), (0.0, 90.00004680423052, -0.0), (1.0, 1.0, 1.0), "NonDest_Floor_Trim_Thin_3M_A13", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1700.794, 4399.846, 796.4373), (0.0, 90.00004680423052, -0.0), (1.0, 1.0, 1.0), "NonDest_Floor_Trim_Thin_3M_A14", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1400.794, 4399.846, 796.4373), (0.0, -9.155273700792082e-05, 0.0), (1.0, 1.0, 1.0), "NonDest_Floor_Trim_Thin_3M_A15", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1100.794, 4399.846, 796.4373), (0.0, -9.155273700792082e-05, 0.0), (1.0, 1.0, 1.0), "NonDest_Floor_Trim_Thin_3M_A16", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2300.794, 4999.846, 696.4373), (0.0, -3.051757709276941e-05, 0.0), (1.0, 1.0, 1.0), "NonDest_Floor_Trim_Thin_3M_A17", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2600.794, 4999.846, 696.4373), (0.0, -3.051757709276941e-05, 0.0), (1.0, 1.0, 1.0), "NonDest_Floor_Trim_Thin_3M_A18", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2900.794, 4999.846, 696.4373), (0.0, 90.00004680423052, -0.0), (1.0, 1.0, 1.0), "NonDest_Floor_Trim_Thin_3M_A19", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4350.0, 4850.0, 700.0), (0.0, 0.0, -0.0), (1.0, 1.0, 1.0), "NonDest_Floor_Trim_Thin_3M_A2", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2900.794, 5299.846, 696.4373), (0.0, 90.00004680423052, -0.0), (1.0, 1.0, 1.0), "NonDest_Floor_Trim_Thin_3M_A20", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5400.0, 4350.485, 797.563), (0.0, -179.99986339621609, 0.0), (1.0, 1.0, 1.0), "NonDest_Floor_Trim_Thin_3M_A21", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5850.0, 4650.485, 797.563), (0.0, -179.99986339621609, 0.0), (1.0, 1.0, 1.0), "NonDest_Floor_Trim_Thin_3M_A22_214", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (6150.0, 4650.485, 797.563), (0.0, -179.99986339621609, 0.0), (1.0, 1.0, 1.0), "NonDest_Floor_Trim_Thin_3M_A23", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (6450.0, 4650.485, 797.563), (0.0, -179.99986339621609, 0.0), (1.0, 1.0, 1.0), "NonDest_Floor_Trim_Thin_3M_A24", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4799.8423, 4200.485, 797.563), (0.0, -89.99966272977818, 0.0), (1.0, 1.0, 1.0), "NonDest_Floor_Trim_Thin_3M_A25", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4799.8423, 3900.4849, 797.563), (0.0, -89.99966272977818, 0.0), (1.0, 1.0, 1.0), "NonDest_Floor_Trim_Thin_3M_A26", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4799.8423, 3600.4849, 797.563), (0.0, -89.99966272977818, 0.0), (1.0, 1.0, 1.0), "NonDest_Floor_Trim_Thin_3M_A27", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4799.8423, 3300.4849, 797.563), (0.0, -89.99966272977818, 0.0), (1.0, 1.0, 1.0), "NonDest_Floor_Trim_Thin_3M_A28", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4799.8423, 3000.4849, 797.563), (0.0, -89.99966272977818, 0.0), (1.0, 1.0, 1.0), "NonDest_Floor_Trim_Thin_3M_A29", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5100.0, 5150.0, 700.0), (0.0, 0.0, -0.0), (1.0, 1.0, 1.0), "NonDest_Floor_Trim_Thin_3M_A3", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4799.8423, 2700.4849, 797.563), (0.0, -89.99966272977818, 0.0), (1.0, 1.0, 1.0), "NonDest_Floor_Trim_Thin_3M_A30", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4799.8423, 2400.4849, 797.563), (0.0, -89.99966272977818, 0.0), (1.0, 1.0, 1.0), "NonDest_Floor_Trim_Thin_3M_A31", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2000.794, 3650.271, 796.4373), (0.0, -179.99988388675877, 0.0), (1.0, 1.0, 1.0), "NonDest_Floor_Trim_Thin_3M_A32", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1700.794, 3650.271, 796.4373), (0.0, -179.99988388675877, 0.0), (1.0, 1.0, 1.0), "NonDest_Floor_Trim_Thin_3M_A33", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1400.794, 3650.271, 796.4373), (0.0, -179.99988388675877, 0.0), (1.0, 1.0, 1.0), "NonDest_Floor_Trim_Thin_3M_A34", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1100.794, 3650.271, 796.4373), (0.0, -179.99988388675877, 0.0), (1.0, 1.0, 1.0), "NonDest_Floor_Trim_Thin_3M_A35", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5400.0, 5150.0, 700.0), (0.0, 0.0, -0.0), (1.0, 1.0, 1.0), "NonDest_Floor_Trim_Thin_3M_A4", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5700.0, 5150.0, 700.0), (0.0, 0.0, -0.0), (1.0, 1.0, 1.0), "NonDest_Floor_Trim_Thin_3M_A5", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3750.0, 5150.0, 700.0), (0.0, 0.0, -0.0), (1.0, 1.0, 1.0), "NonDest_Floor_Trim_Thin_3M_A6", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3500.0, 5600.0, 700.0), (0.0, -90.0001164887758, 0.0), (1.0, 1.0, 1.0), "NonDest_Floor_Trim_Thin_3M_A7_66", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2900.0, 5598.0835, 796.49066), (0.0, 0.0, -0.0), (1.0, 1.0, 1.0), "NonDest_Floor_Trim_Thin_3M_A8_122", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3200.0, 5598.0835, 796.49066), (0.0, 0.0, -0.0), (1.0, 1.0, 1.0), "NonDest_Floor_Trim_Thin_3M_A9_124", _folder)
if a: placed += 1
else: skipped += 1

# Batch 7: StaticMesh'NonDest_Floor_Trim_Thin_Corner_A' (5 instances)
_mesh_path = "/Game/Art/Assets/Kits/Architecture/Non_D/NonDest_Floor_Trim_Thin_Corner_A"
_materials = ['/Game/Art/Assets/Kits/Architecture/Suburbs/Materials/Suburbs_Trim_Sheet_A/MI_Suburbs_Trim_Sheet_A']
_folder = "Reconstruction/BD_BB_SnakingRiver_Urban/Meshes"
a = spawn_static_mesh(_mesh_path, _materials, (4200.0, 5000.0, 700.0), (0.0, -90.0001164887758, 0.0), (1.0, 1.0, 1.0), "NonDest_Floor_Trim_Thin_Corner_A_24", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4950.0, 4850.0, 700.0), (0.0, 6.484984988975128e-05, -0.0), (1.0, 1.0, 1.0), "NonDest_Floor_Trim_Thin_Corner_A2", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3500.0, 5300.0, 700.0), (0.0, -90.0001164887758, 0.0), (1.0, 1.0, 1.0), "NonDest_Floor_Trim_Thin_Corner_A3", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4949.578, 4350.0, 797.7731), (0.0, -179.9995970188438, 0.0), (1.0, 1.0, 1.0), "NonDest_Floor_Trim_Thin_Corner_A4_205", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5549.578, 4650.0, 797.7731), (0.0, -179.9995970188438, 0.0), (1.0, 1.0, 1.0), "NonDest_Floor_Trim_Thin_Corner_A5", _folder)
if a: placed += 1
else: skipped += 1

# Batch 8: StaticMesh'NonDest_Pillar_6M_A' (12 instances)
_mesh_path = "/Game/Art/Assets/Kits/Architecture/Non_D/NonDest_Pillar_6M_A"
_materials = ['/Game/Art/Assets/Kits/Architecture/Suburbs/Materials/Suburbs_Trim_Sheet_A/MI_Suburbs_Trim_Sheet_A']
_folder = "Reconstruction/BD_BB_SnakingRiver_Urban/Meshes"
a = spawn_static_mesh(_mesh_path, _materials, (3500.0, 5150.0, 100.0), (0.0, 0.0, -0.0), (1.0, 1.0, 1.0), "NonDest_Pillar_5M_A_80", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4800.0, 4350.0, 200.0), (0.0, 0.0, -0.0), (1.0, 1.0, 1.0), "NonDest_Pillar_5M_A10", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5400.0, 4350.0, 200.0), (0.0, 0.0, -0.0), (1.0, 1.0, 1.0), "NonDest_Pillar_5M_A11", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5400.0, 4650.0, 200.0), (0.0, 0.0, -0.0), (1.0, 1.0, 1.0), "NonDest_Pillar_5M_A12", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4200.0, 4850.0, 100.0), (0.0, 0.0, -0.0), (1.0, 1.0, 1.0), "NonDest_Pillar_5M_A2", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5100.0, 4850.0, 100.0), (0.0, 0.0, -0.0), (1.0, 1.0, 1.0), "NonDest_Pillar_5M_A3", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5100.0, 5150.0, 100.0), (0.0, 0.0, -0.0), (1.0, 1.0, 1.0), "NonDest_Pillar_5M_A4", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4200.0, 5150.0, 100.0), (0.0, 0.0, -0.0), (1.0, 1.0, 1.0), "NonDest_Pillar_5M_A5", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2900.0, 5000.0, 100.0), (0.0, 0.0, -0.0), (1.0, 1.0, 1.0), "NonDest_Pillar_5M_A6", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1700.0, 5000.0, 200.0), (0.0, 0.0, -0.0), (1.0, 1.0, 1.0), "NonDest_Pillar_5M_A7", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2300.0, 5000.0, 200.0), (0.0, 0.0, -0.0), (1.0, 1.0, 1.0), "NonDest_Pillar_5M_A8", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1700.0, 4400.0, 200.0), (0.0, 0.0, -0.0), (1.0, 1.0, 1.0), "NonDest_Pillar_5M_A9", _folder)
if a: placed += 1
else: skipped += 1

# Batch 9: StaticMesh'NonDest_Trim_3M_B' (26 instances)
_mesh_path = "/Game/Art/Assets/Kits/Architecture/Non_D/NonDest_Trim_3M_B"
_materials = ['/Game/Environments/Materials/MI_Suburbs_Non_Destructible', '/Game/Art/Assets/Kits/Architecture/Suburbs/Materials/Suburbs_Trim_Sheet_A/MI_Suburbs_Trim_Sheet_A']
_folder = "Reconstruction/BD_BB_SnakingRiver_Urban/Meshes"
a = spawn_static_mesh(_mesh_path, _materials, (2150.0, 5000.0, 700.0), (0.0, 0.0, -0.0), (1.0, 1.0, 1.0), "NonDest_Trim_3M_A_110", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4800.0, 3900.0, 700.0), (0.0, -90.0001164887758, 0.0), (1.0, 1.0, 1.0), "NonDest_Trim_3M_A10", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4800.0, 3600.0, 700.0), (0.0, -90.0001164887758, 0.0), (1.0, 1.0, 1.0), "NonDest_Trim_3M_A11", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4800.0, 3300.0, 700.0), (0.0, -90.0001164887758, 0.0), (1.0, 1.0, 1.0), "NonDest_Trim_3M_A12", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4800.0, 3000.0, 700.0), (0.0, -90.0001164887758, 0.0), (1.0, 1.0, 1.0), "NonDest_Trim_3M_A13", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4800.0, 2700.0, 700.0), (0.0, -90.0001164887758, 0.0), (1.0, 1.0, 1.0), "NonDest_Trim_3M_A14", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4800.0, 2400.0, 700.0), (0.0, -90.0001164887758, 0.0), (1.0, 1.0, 1.0), "NonDest_Trim_3M_A15", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4800.0, 2100.0, 700.0), (0.0, -90.0001164887758, 0.0), (1.0, 1.0, 1.0), "NonDest_Trim_3M_A16", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2350.0, 5300.0, 700.0), (0.0, 0.0, -0.0), (1.0, 1.0, 1.0), "NonDest_Trim_3M_A17", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2500.0, 5450.0, 700.0), (0.0, 90.0001164887758, -0.0), (1.0, 1.0, 1.0), "NonDest_Trim_3M_A18", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3900.0, 5750.0, 700.0), (0.0, 90.00007597449323, -0.0), (1.0, 1.0, 1.0), "NonDest_Trim_3M_A19", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1700.0, 4850.0, 700.0), (0.0, 89.99999818714215, -0.0), (1.0, 1.0, 1.0), "NonDest_Trim_3M_A2", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3900.0, 6050.0, 700.0), (0.0, 90.00007597449323, -0.0), (1.0, 1.0, 1.0), "NonDest_Trim_3M_A20", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4800.0, 4200.0, 700.0), (0.0, -90.0001164887758, 0.0), (1.0, 1.0, 1.0), "NonDest_Trim_3M_A3", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4950.0, 4350.0, 700.0), (0.0, 179.99976777355934, -0.0), (1.0, 1.0, 1.0), "NonDest_Trim_3M_A4", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5250.0, 4350.0, 700.0), (0.0, 179.99976777355934, -0.0), (1.0, 1.0, 1.0), "NonDest_Trim_3M_A5", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5400.0, 4500.0, 700.0), (0.0, -90.00005166594045, 0.0), (1.0, 1.0, 1.0), "NonDest_Trim_3M_A6", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5550.0, 4650.0, 700.0), (0.0, 179.9998975471592, -0.0), (1.0, 1.0, 1.0), "NonDest_Trim_3M_A7", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5850.0, 4650.0, 700.0), (0.0, 179.9998975471592, -0.0), (1.0, 1.0, 1.0), "NonDest_Trim_3M_A8", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (6150.0, 4650.0, 700.0), (0.0, 179.9998975471592, -0.0), (1.0, 1.0, 1.0), "NonDest_Trim_3M_A9", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1850.0, 5000.0, 700.0), (0.0, 0.0, -0.0), (1.0, 1.0, 1.0), "NonDest_Trim_3M_A_L_106", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1700.0004, 4550.0, 700.0), (0.0, 89.99999818714215, -0.0), (1.0, 1.0, 1.0), "NonDest_Trim_3M_A_L2_113", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1550.0004, 4400.0, 700.0), (0.0, 0.0, -0.0), (1.0, 1.0, 1.0), "NonDest_Trim_3M_A_L3", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1850.0, 3650.0, 700.0), (0.0, -179.99976777351753, 0.0), (1.0, 1.0, 1.0), "NonDest_Trim_3M_A_L4", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1550.0, 3650.0, 700.0), (0.0, -179.99976777351753, 0.0), (1.0, 1.0, 1.0), "NonDest_Trim_3M_A_L5", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1250.0, 3650.0, 700.0), (0.0, -179.99976777351753, 0.0), (1.0, 1.0, 1.0), "NonDest_Trim_3M_A_L6", _folder)
if a: placed += 1
else: skipped += 1

# Batch 10: StaticMesh'NonDest_Wall_3M_B' (42 instances)
_mesh_path = "/Game/Art/Assets/Kits/Architecture/Non_D/NonDest_Wall_3M_B"
_materials = ['/Game/Environments/Materials/MI_Suburbs_Non_Destructible', '/Game/Art/Assets/Kits/Architecture/Suburbs/Materials/Suburbs_Trim_Sheet_A/MI_Suburbs_Trim_Sheet_A']
_folder = "Reconstruction/BD_BB_SnakingRiver_Urban/Meshes"
a = spawn_static_mesh(_mesh_path, _materials, (3800.0, 5150.0, 400.0), (0.0, -179.99998633961752, -0.0), (1.0, 1.0, 1.0), "NonDest_Wall_3M_B_2", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5400.0, 5150.0, 400.0), (0.0, -179.99981558486024, 0.0), (1.0, 1.0, 1.0), "NonDest_Wall_3M_B10", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5700.0, 5150.0, 400.0), (0.0, -179.99981558486024, 0.0), (1.0, 1.0, 1.0), "NonDest_Wall_3M_B11", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (6000.0, 5150.0, 400.0), (0.0, -179.99981558486024, 0.0), (1.0, 1.0, 1.0), "NonDest_Wall_3M_B12", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4400.0, 5150.0, 400.0), (0.0, -179.99998633961752, -0.0), (1.0, 1.0, 1.0), "NonDest_Wall_3M_B13", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2900.0, 5000.0, 400.0), (0.0, -179.99998633961752, -0.0), (1.0, 1.0, 1.0), "NonDest_Wall_3M_B14", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2900.0, 5300.0, 400.0), (0.0, -89.99978589276644, 0.0), (1.0, 1.0, 1.0), "NonDest_Wall_3M_B15", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2900.0, 5600.0, 400.0), (0.0, -89.99978589276644, 0.0), (1.0, 1.0, 1.0), "NonDest_Wall_3M_B16", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2900.0, 5900.0, 400.0), (0.0, -89.99978589276644, 0.0), (1.0, 1.0, 1.0), "NonDest_Wall_3M_B17", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2900.0, 6200.0, 400.0), (0.0, -89.99978589276644, 0.0), (1.0, 1.0, 1.0), "NonDest_Wall_3M_B18", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3500.0, 5750.0, 400.0), (0.0, 89.9998815062137, -0.0), (1.0, 1.0, 1.0), "NonDest_Wall_3M_B19", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3500.0, 5150.0, 400.0), (0.0, 89.9998815062137, -0.0), (1.0, 1.0, 1.0), "NonDest_Wall_3M_B2", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2600.0, 5000.0, 400.0), (0.0, -179.99998633961752, -0.0), (1.0, 1.0, 1.0), "NonDest_Wall_3M_B20", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2300.0, 5000.0, 400.0), (0.0, -179.99998633961752, -0.0), (1.0, 1.0, 1.0), "NonDest_Wall_3M_B21", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2000.0, 5000.0, 400.0), (0.0, -179.99998633961752, -0.0), (1.0, 1.0, 1.0), "NonDest_Wall_3M_B22", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1700.0, 5000.0, 400.0), (0.0, -89.99975996369572, 0.0), (1.0, 1.0, 1.0), "NonDest_Wall_3M_B23", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1700.0, 4700.0, 400.0), (0.0, -89.99975996369572, 0.0), (1.0, 1.0, 1.0), "NonDest_Wall_3M_B24", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1700.0, 4400.0, 400.0), (0.0, -179.9998360754275, 0.0), (1.0, 1.0, 1.0), "NonDest_Wall_3M_B25", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1700.0002, 3650.0, 400.0), (0.0, 0.00039672851366830966, -0.0), (1.0, 1.0, 1.0), "NonDest_Wall_3M_B26", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1400.0002, 3650.0, 400.0), (0.0, 0.00039672851366830966, -0.0), (1.0, 1.0, 1.0), "NonDest_Wall_3M_B27", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1100.0002, 3650.0, 400.0), (0.0, 0.00039672851366830966, -0.0), (1.0, 1.0, 1.0), "NonDest_Wall_3M_B28", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4799.999, 4050.0, 400.0), (0.0, 89.99985719769576, -0.0), (1.0, 1.0, 1.0), "NonDest_Wall_3M_B29", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3500.0, 5450.0, 400.0), (0.0, 89.9998815062137, -0.0), (1.0, 1.0, 1.0), "NonDest_Wall_3M_B3", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4800.0005, 4350.002, 400.0), (0.0, -0.00030517577092912265, 0.0), (1.0, 1.0, 1.0), "NonDest_Wall_3M_B30", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5100.0005, 4350.002, 400.0), (0.0, -0.00030517577092912265, 0.0), (1.0, 1.0, 1.0), "NonDest_Wall_3M_B31", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5399.999, 4350.0, 400.0), (0.0, 89.99977616935033, -0.0), (1.0, 1.0, 1.0), "NonDest_Wall_3M_B32", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5400.0005, 4650.002, 400.0), (0.0, -0.00036621094803402087, 0.0), (1.0, 1.0, 1.0), "NonDest_Wall_3M_B33", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5700.0005, 4650.002, 400.0), (0.0, -0.00036621094803402087, 0.0), (1.0, 1.0, 1.0), "NonDest_Wall_3M_B34", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (6000.0005, 4650.002, 400.0), (0.0, -0.00036621094803402087, 0.0), (1.0, 1.0, 1.0), "NonDest_Wall_3M_B35", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4799.999, 3750.0, 400.0), (0.0, 89.99985719769576, -0.0), (1.0, 1.0, 1.0), "NonDest_Wall_3M_B36", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4799.999, 3450.0, 400.0), (0.0, 89.99985719769576, -0.0), (1.0, 1.0, 1.0), "NonDest_Wall_3M_B37", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4799.999, 3150.0, 400.0), (0.0, 89.99985719769576, -0.0), (1.0, 1.0, 1.0), "NonDest_Wall_3M_B38", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4799.999, 2850.0, 400.0), (0.0, 89.99985719769576, -0.0), (1.0, 1.0, 1.0), "NonDest_Wall_3M_B39", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4100.0, 5150.0, 400.0), (0.0, -179.99998633961752, -0.0), (1.0, 1.0, 1.0), "NonDest_Wall_3M_B4", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4799.999, 2550.0, 400.0), (0.0, 89.99985719769576, -0.0), (1.0, 1.0, 1.0), "NonDest_Wall_3M_B40", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4799.999, 2250.0, 400.0), (0.0, 89.99985719769576, -0.0), (1.0, 1.0, 1.0), "NonDest_Wall_3M_B41", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4799.999, 1950.0, 400.0), (0.0, 89.99985719769576, -0.0), (1.0, 1.0, 1.0), "NonDest_Wall_3M_B42", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4200.0, 4850.0, 400.0), (0.0, 89.9998815062137, -0.0), (1.0, 1.0, 1.0), "NonDest_Wall_3M_B5", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4500.0, 4850.0, 400.0), (0.0, -179.9999795094293, 0.0), (1.0, 1.0, 1.0), "NonDest_Wall_3M_B6", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4800.0, 4850.0, 400.0), (0.0, -179.9999795094293, 0.0), (1.0, 1.0, 1.0), "NonDest_Wall_3M_B7", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5100.0, 4850.0, 400.0), (0.0, -179.9999795094293, 0.0), (1.0, 1.0, 1.0), "NonDest_Wall_3M_B8", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5100.0, 5150.0, 400.0), (0.0, -89.99978589276644, 0.0), (1.0, 1.0, 1.0), "NonDest_Wall_3M_B9", _folder)
if a: placed += 1
else: skipped += 1

# Batch 11: StaticMesh'Suburbs_Floor_1-5x1-5m_A' (1 instances)
_mesh_path = "/Game/Art/Assets/Kits/Architecture/Suburbs/Suburbs_Floor_1-5x1-5m_A"
_materials = ['/Game/Art/Assets/Kits/Architecture/Suburbs/Suburbs_Floor/Materials/Subrubs_Floor_Tileable_A/MI_Suburbs_Floor_A_inst']
_folder = "Reconstruction/BD_BB_SnakingRiver_Urban/Meshes"
a = spawn_static_mesh(_mesh_path, _materials, (450.0, 3850.0, 800.0), (0.0, 0.0, -0.0), (1.0, 1.0, 1.0), "Suburbs_Floor_1-5x1-5m_A_66", _folder)
if a: placed += 1
else: skipped += 1

# Batch 12: StaticMesh'Suburbs_Floor_1x1m_A' (6 instances)
_mesh_path = "/Game/Art/Assets/Kits/Architecture/Suburbs/Suburbs_Floor_1x1m_A"
_materials = ['/Game/Art/Assets/Kits/Architecture/Suburbs/Suburbs_Floor/Materials/Subrubs_Floor_Tileable_A/MI_Suburbs_Floor_A_inst']
_folder = "Reconstruction/BD_BB_SnakingRiver_Urban/Meshes"
a = spawn_static_mesh(_mesh_path, _materials, (1800.0, 5400.0, 800.0), (0.0, 0.0, -0.0), (1.0, 1.0, 1.0), "Suburbs_Floor_1x1m_A_82", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1800.0, 5500.0, 800.0), (0.0, 0.0, -0.0), (1.0, 1.0, 1.0), "Suburbs_Floor_1x1m_A2", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1800.0, 5600.0, 800.0), (0.0, 0.0, -0.0), (1.0, 1.0, 1.0), "Suburbs_Floor_1x1m_A3", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1400.0, 5400.0, 800.0), (0.0, 0.0, -0.0), (1.0, 1.0, 1.0), "Suburbs_Floor_1x1m_A4", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1400.0, 5500.0, 800.0), (0.0, 0.0, -0.0), (1.0, 1.0, 1.0), "Suburbs_Floor_1x1m_A5", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1400.0, 5600.0, 800.0), (0.0, 0.0, -0.0), (1.0, 1.0, 1.0), "Suburbs_Floor_1x1m_A6", _folder)
if a: placed += 1
else: skipped += 1

# Batch 13: StaticMesh'Suburbs_Floor_1x1m_B' (9 instances)
_mesh_path = "/Game/Art/Assets/Kits/Architecture/Suburbs/Suburbs_Floor_1x1m_B"
_materials = ['/Game/Art/Assets/Kits/Architecture/Suburbs/Suburbs_Floor/Materials/Subrubs_Floor_Tileable_A/MI_Suburbs_Floor_A_inst']
_folder = "Reconstruction/BD_BB_SnakingRiver_Urban/Meshes"
a = spawn_static_mesh(_mesh_path, _materials, (3600.0, 5900.0, 800.0), (0.0, 0.0, -0.0), (1.0, 1.0, 1.0), "Suburbs_Floor_1x1m_B_139", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3600.0, 5800.0, 800.0), (0.0, 0.0, -0.0), (1.0, 1.0, 1.0), "Suburbs_Floor_1x1m_B2", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3600.0, 5700.0, 800.0), (0.0, 0.0, -0.0), (1.0, 1.0, 1.0), "Suburbs_Floor_1x1m_B3", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3900.0, 6200.0, 800.0), (0.0, 0.0, -0.0), (1.0, 1.0, 1.0), "Suburbs_Floor_1x1m_B4", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3900.0, 6100.0, 800.0), (0.0, 0.0, -0.0), (1.0, 1.0, 1.0), "Suburbs_Floor_1x1m_B5", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3900.0, 6000.0, 800.0), (0.0, 0.0, -0.0), (1.0, 1.0, 1.0), "Suburbs_Floor_1x1m_B6", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4200.0, 5450.0, 700.0), (0.0, 0.0, -0.0), (1.0, 1.0, 1.0), "Suburbs_Floor_1x1m_B7", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4200.0, 5350.0, 700.0), (0.0, 0.0, -0.0), (1.0, 1.0, 1.0), "Suburbs_Floor_1x1m_B8", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4200.0, 5250.0, 700.0), (0.0, 0.0, -0.0), (1.0, 1.0, 1.0), "Suburbs_Floor_1x1m_B9", _folder)
if a: placed += 1
else: skipped += 1

# Batch 14: StaticMesh'Suburbs_Floor_3x3m_A' (113 instances)
_mesh_path = "/Game/Art/Assets/Kits/Architecture/Suburbs/Suburbs_Floor_3x3m_A"
_materials = ['/Game/Art/Assets/Kits/Architecture/Suburbs/Suburbs_Floor/Materials/Subrubs_Floor_Tileable_A/MI_Suburbs_Floor_A_inst']
_folder = "Reconstruction/BD_BB_SnakingRiver_Urban/Meshes"
a = spawn_static_mesh(_mesh_path, _materials, (3050.0, 200.0, 800.0), (0.0, 0.0, -0.0), (1.0, 1.0, 1.0), "Suburbs_Floor_3x3m_A_1045", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1550.0, 3200.0, 800.0), (0.0, 0.0, -0.0), (1.0, 1.0, 1.0), "Suburbs_Floor_3x3m_A10", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (6150.0, 3000.0, 800.0), (0.0, 0.0, -0.0), (1.0, 1.0, 1.0), "Suburbs_Floor_3x3m_A100", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4950.0, 3000.0, 800.0), (0.0, 0.0, -0.0), (1.0, 1.0, 1.0), "Suburbs_Floor_3x3m_A101", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5250.0, 3000.0, 800.0), (0.0, 0.0, -0.0), (1.0, 1.0, 1.0), "Suburbs_Floor_3x3m_A102", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4950.0, 2700.0, 800.0), (0.0, 0.0, -0.0), (1.0, 1.0, 1.0), "Suburbs_Floor_3x3m_A103", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4950.0, 2400.0, 800.0), (0.0, 0.0, -0.0), (1.0, 1.0, 1.0), "Suburbs_Floor_3x3m_A104", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4950.0, 2100.0, 800.0), (0.0, 0.0, -0.0), (1.0, 1.0, 1.0), "Suburbs_Floor_3x3m_A105", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1550.0, 6050.0, 800.0), (0.0, 0.0, -0.0), (1.0, 1.0, 1.0), "Suburbs_Floor_3x3m_A106", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1250.0, 5750.0, 800.0), (0.0, 0.0, -0.0), (1.0, 1.0, 1.0), "Suburbs_Floor_3x3m_A107", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1250.0, 6050.0, 800.0), (0.0, 0.0, -0.0), (1.0, 1.0, 1.0), "Suburbs_Floor_3x3m_A108", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (950.0, 5750.0, 800.0), (0.0, 0.0, -0.0), (1.0, 1.0, 1.0), "Suburbs_Floor_3x3m_A109", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1850.0, 3200.0, 800.0), (0.0, 0.0, -0.0), (1.0, 1.0, 1.0), "Suburbs_Floor_3x3m_A11", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (950.0, 6050.0, 800.0), (0.0, 0.0, -0.0), (1.0, 1.0, 1.0), "Suburbs_Floor_3x3m_A110", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3950.0, 5900.0, 700.0), (0.0, 0.0, -0.0), (1.0, 1.0, 1.0), "Suburbs_Floor_3x3m_A111", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4250.0, 5900.0, 700.0), (0.0, 0.0, -0.0), (1.0, 1.0, 1.0), "Suburbs_Floor_3x3m_A112", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4550.0, 5900.0, 700.0), (0.0, 0.0, -0.0), (1.0, 1.0, 1.0), "Suburbs_Floor_3x3m_A113", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4850.0, 5900.0, 700.0), (0.0, 0.0, -0.0), (1.0, 1.0, 1.0), "Suburbs_Floor_3x3m_A114", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5150.0, 5900.0, 700.0), (0.0, 0.0, -0.0), (1.0, 1.0, 1.0), "Suburbs_Floor_3x3m_A115", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5450.0, 5900.0, 700.0), (0.0, 0.0, -0.0), (1.0, 1.0, 1.0), "Suburbs_Floor_3x3m_A116", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5750.0, 5900.0, 700.0), (0.0, 0.0, -0.0), (1.0, 1.0, 1.0), "Suburbs_Floor_3x3m_A117", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1250.0, 2900.0, 800.0), (0.0, 0.0, -0.0), (1.0, 1.0, 1.0), "Suburbs_Floor_3x3m_A12", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1550.0, 2900.0, 800.0), (0.0, 0.0, -0.0), (1.0, 1.0, 1.0), "Suburbs_Floor_3x3m_A13", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1850.0, 2900.0, 800.0), (0.0, 0.0, -0.0), (1.0, 1.0, 1.0), "Suburbs_Floor_3x3m_A14", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1850.0, 3500.0, 800.0), (0.0, 0.0, -0.0), (1.0, 1.0, 1.0), "Suburbs_Floor_3x3m_A15", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1250.0, 4550.0, 800.0), (0.0, 0.0, -0.0), (1.0, 1.0, 1.0), "Suburbs_Floor_3x3m_A16_71", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1850.0, 5150.0, 800.0), (0.0, 0.0, -0.0), (1.0, 1.0, 1.0), "Suburbs_Floor_3x3m_A17", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2150.0, 5150.0, 800.0), (0.0, 0.0, -0.0), (1.0, 1.0, 1.0), "Suburbs_Floor_3x3m_A18", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1550.0, 3500.0, 800.0), (0.0, 0.0, -0.0), (1.0, 1.0, 1.0), "Suburbs_Floor_3x3m_A19", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3350.0, 200.0, 800.0), (0.0, 0.0, -0.0), (1.0, 1.0, 1.0), "Suburbs_Floor_3x3m_A2", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1250.0, 3500.0, 800.0), (0.0, 0.0, -0.0), (1.0, 1.0, 1.0), "Suburbs_Floor_3x3m_A20", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2450.0, 5450.0, 700.0), (0.0, 0.0, -0.0), (1.0, 1.0, 1.0), "Suburbs_Floor_3x3m_A21", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2450.0, 5750.0, 800.0), (0.0, 0.0, -0.0), (1.0, 1.0, 1.0), "Suburbs_Floor_3x3m_A23", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2750.0, 5750.0, 800.0), (0.0, 0.0, -0.0), (1.0, 1.0, 1.0), "Suburbs_Floor_3x3m_A24", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2450.0, 6050.0, 800.0), (0.0, 0.0, -0.0), (1.0, 1.0, 1.0), "Suburbs_Floor_3x3m_A25", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1550.0, 4850.0, 800.0), (0.0, 0.0, -0.0), (1.0, 1.0, 1.0), "Suburbs_Floor_3x3m_A26", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1550.0, 5150.0, 800.0), (0.0, 0.0, -0.0), (1.0, 1.0, 1.0), "Suburbs_Floor_3x3m_A27", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1550.0, 4550.0, 800.0), (0.0, 0.0, -0.0), (1.0, 1.0, 1.0), "Suburbs_Floor_3x3m_A28", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1650.0, 5450.0, 800.0), (0.0, 0.0, -0.0), (1.0, 1.0, 1.0), "Suburbs_Floor_3x3m_A29", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (150.0, 2950.0, 800.0), (0.0, 0.0, -0.0), (1.0, 1.0, 1.0), "Suburbs_Floor_3x3m_A3_11", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1250.0, 4850.0, 800.0), (0.0, 0.0, -0.0), (1.0, 1.0, 1.0), "Suburbs_Floor_3x3m_A30", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1250.0, 5150.0, 800.0), (0.0, 0.0, -0.0), (1.0, 1.0, 1.0), "Suburbs_Floor_3x3m_A31", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1250.0, 5450.0, 800.0), (0.0, 0.0, -0.0), (1.0, 1.0, 1.0), "Suburbs_Floor_3x3m_A32", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (950.0, 4850.0, 800.0), (0.0, 0.0, -0.0), (1.0, 1.0, 1.0), "Suburbs_Floor_3x3m_A33", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (950.0, 5150.0, 800.0), (0.0, 0.0, -0.0), (1.0, 1.0, 1.0), "Suburbs_Floor_3x3m_A34", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (950.0, 5450.0, 800.0), (0.0, 0.0, -0.0), (1.0, 1.0, 1.0), "Suburbs_Floor_3x3m_A35", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2750.0, 6050.0, 800.0), (0.0, 0.0, -0.0), (1.0, 1.0, 1.0), "Suburbs_Floor_3x3m_A36", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3050.0, 5750.0, 800.0), (0.0, 0.0, -0.0), (1.0, 1.0, 1.0), "Suburbs_Floor_3x3m_A37", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3050.0, 6050.0, 800.0), (0.0, 0.0, -0.0), (1.0, 1.0, 1.0), "Suburbs_Floor_3x3m_A38", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3350.0, 5750.0, 800.0), (0.0, 0.0, -0.0), (1.0, 1.0, 1.0), "Suburbs_Floor_3x3m_A39", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (150.0, 3250.0, 800.0), (0.0, 0.0, -0.0), (1.0, 1.0, 1.0), "Suburbs_Floor_3x3m_A4", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3350.0, 6050.0, 800.0), (0.0, 0.0, -0.0), (1.0, 1.0, 1.0), "Suburbs_Floor_3x3m_A40", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (950.0, 4550.0, 800.0), (0.0, 0.0, -0.0), (1.0, 1.0, 1.0), "Suburbs_Floor_3x3m_A41", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3650.0, 6050.0, 800.0), (0.0, 0.0, -0.0), (1.0, 1.0, 1.0), "Suburbs_Floor_3x3m_A42", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2150.0, 5750.0, 800.0), (0.0, 0.0, -0.0), (1.0, 1.0, 1.0), "Suburbs_Floor_3x3m_A43", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2150.0, 6050.0, 800.0), (0.0, 0.0, -0.0), (1.0, 1.0, 1.0), "Suburbs_Floor_3x3m_A44", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1850.0, 5750.0, 800.0), (0.0, 0.0, -0.0), (1.0, 1.0, 1.0), "Suburbs_Floor_3x3m_A45", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1850.0, 6050.0, 800.0), (0.0, 0.0, -0.0), (1.0, 1.0, 1.0), "Suburbs_Floor_3x3m_A46", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2350.0, 5450.0, 800.0), (0.0, 0.0, -0.0), (1.0, 1.0, 1.0), "Suburbs_Floor_3x3m_A47", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2050.0, 5450.0, 800.0), (0.0, 0.0, -0.0), (1.0, 1.0, 1.0), "Suburbs_Floor_3x3m_A48", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1550.0, 5750.0, 800.0), (0.0, 0.0, -0.0), (1.0, 1.0, 1.0), "Suburbs_Floor_3x3m_A49", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (150.0, 3550.0, 800.0), (0.0, 0.0, -0.0), (1.0, 1.0, 1.0), "Suburbs_Floor_3x3m_A5", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3950.0, 5600.0, 700.0), (0.0, 0.0, -0.0), (1.0, 1.0, 1.0), "Suburbs_Floor_3x3m_A50", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4250.0, 5600.0, 700.0), (0.0, 0.0, -0.0), (1.0, 1.0, 1.0), "Suburbs_Floor_3x3m_A51", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4550.0, 5600.0, 700.0), (0.0, 0.0, -0.0), (1.0, 1.0, 1.0), "Suburbs_Floor_3x3m_A52", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4350.0, 5300.0, 700.0), (0.0, 0.0, -0.0), (1.0, 1.0, 1.0), "Suburbs_Floor_3x3m_A53", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4650.0, 5300.0, 700.0), (0.0, 0.0, -0.0), (1.0, 1.0, 1.0), "Suburbs_Floor_3x3m_A54", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4950.0, 5300.0, 700.0), (0.0, 0.0, -0.0), (1.0, 1.0, 1.0), "Suburbs_Floor_3x3m_A55_5", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4850.0, 5600.0, 700.0), (0.0, 0.0, -0.0), (1.0, 1.0, 1.0), "Suburbs_Floor_3x3m_A56", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5550.0, 4200.0, 800.0), (0.0, 0.0, -0.0), (1.0, 1.0, 1.0), "Suburbs_Floor_3x3m_A57", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5150.0, 5600.0, 700.0), (0.0, 0.0, -0.0), (1.0, 1.0, 1.0), "Suburbs_Floor_3x3m_A58", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5850.0, 4200.0, 800.0), (0.0, 0.0, -0.0), (1.0, 1.0, 1.0), "Suburbs_Floor_3x3m_A59", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5250.0, 2700.0, 800.0), (0.0, 0.0, -0.0), (1.0, 1.0, 1.0), "Suburbs_Floor_3x3m_A60", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5250.0, 2400.0, 800.0), (0.0, 0.0, -0.0), (1.0, 1.0, 1.0), "Suburbs_Floor_3x3m_A61", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5250.0, 2100.0, 800.0), (0.0, 0.0, -0.0), (1.0, 1.0, 1.0), "Suburbs_Floor_3x3m_A62", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5450.0, 5600.0, 700.0), (0.0, 0.0, -0.0), (1.0, 1.0, 1.0), "Suburbs_Floor_3x3m_A63", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5750.0, 5600.0, 700.0), (0.0, 0.0, -0.0), (1.0, 1.0, 1.0), "Suburbs_Floor_3x3m_A64", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3950.0, 5300.0, 700.0), (0.0, 0.0, -0.0), (1.0, 1.0, 1.0), "Suburbs_Floor_3x3m_A65", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3650.0, 5300.0, 700.0), (0.0, 0.0, -0.0), (1.0, 1.0, 1.0), "Suburbs_Floor_3x3m_A66", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4350.0, 5000.0, 700.0), (0.0, 0.0, -0.0), (1.0, 1.0, 1.0), "Suburbs_Floor_3x3m_A67", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4650.0, 5000.0, 700.0), (0.0, 0.0, -0.0), (1.0, 1.0, 1.0), "Suburbs_Floor_3x3m_A68", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4950.0, 5000.0, 700.0), (0.0, 0.0, -0.0), (1.0, 1.0, 1.0), "Suburbs_Floor_3x3m_A69", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5250.0, 5300.0, 700.0), (0.0, 0.0, -0.0), (1.0, 1.0, 1.0), "Suburbs_Floor_3x3m_A70", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5550.0, 5300.0, 700.0), (0.0, 0.0, -0.0), (1.0, 1.0, 1.0), "Suburbs_Floor_3x3m_A71", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5850.0, 5300.0, 700.0), (0.0, 0.0, -0.0), (1.0, 1.0, 1.0), "Suburbs_Floor_3x3m_A72_50", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3750.0, 5750.0, 800.0), (0.0, 0.0, -0.0), (1.0, 1.0, 1.0), "Suburbs_Floor_3x3m_A73", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2750.0, 5150.0, 700.0), (0.0, 0.0, -0.0), (1.0, 1.0, 1.0), "Suburbs_Floor_3x3m_A74", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2450.0, 5150.0, 700.0), (0.0, 0.0, -0.0), (1.0, 1.0, 1.0), "Suburbs_Floor_3x3m_A75", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2750.0, 5450.0, 700.0), (0.0, 0.0, -0.0), (1.0, 1.0, 1.0), "Suburbs_Floor_3x3m_A76", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5550.0, 4500.0, 800.0), (0.0, 0.0, -0.0), (1.0, 1.0, 1.0), "Suburbs_Floor_3x3m_A77", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5850.0, 4500.0, 800.0), (0.0, 0.0, -0.0), (1.0, 1.0, 1.0), "Suburbs_Floor_3x3m_A78", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (6150.0, 4200.0, 800.0), (0.0, 0.0, -0.0), (1.0, 1.0, 1.0), "Suburbs_Floor_3x3m_A79", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (6150.0, 4500.0, 800.0), (0.0, 0.0, -0.0), (1.0, 1.0, 1.0), "Suburbs_Floor_3x3m_A80", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4950.0, 4200.0, 800.0), (0.0, 0.0, -0.0), (1.0, 1.0, 1.0), "Suburbs_Floor_3x3m_A81", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5250.0, 4200.0, 800.0), (0.0, 0.0, -0.0), (1.0, 1.0, 1.0), "Suburbs_Floor_3x3m_A82", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5550.0, 3900.0, 800.0), (0.0, 0.0, -0.0), (1.0, 1.0, 1.0), "Suburbs_Floor_3x3m_A83", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5850.0, 3900.0, 800.0), (0.0, 0.0, -0.0), (1.0, 1.0, 1.0), "Suburbs_Floor_3x3m_A84", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (6150.0, 3900.0, 800.0), (0.0, 0.0, -0.0), (1.0, 1.0, 1.0), "Suburbs_Floor_3x3m_A85", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4950.0, 3900.0, 800.0), (0.0, 0.0, -0.0), (1.0, 1.0, 1.0), "Suburbs_Floor_3x3m_A86", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5250.0, 3900.0, 800.0), (0.0, 0.0, -0.0), (1.0, 1.0, 1.0), "Suburbs_Floor_3x3m_A87", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5550.0, 3600.0, 800.0), (0.0, 0.0, -0.0), (1.0, 1.0, 1.0), "Suburbs_Floor_3x3m_A88", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5850.0, 3600.0, 800.0), (0.0, 0.0, -0.0), (1.0, 1.0, 1.0), "Suburbs_Floor_3x3m_A89", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1250.0, 3200.0, 800.0), (0.0, 0.0, -0.0), (1.0, 1.0, 1.0), "Suburbs_Floor_3x3m_A9", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (6150.0, 3600.0, 800.0), (0.0, 0.0, -0.0), (1.0, 1.0, 1.0), "Suburbs_Floor_3x3m_A90", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4950.0, 3600.0, 800.0), (0.0, 0.0, -0.0), (1.0, 1.0, 1.0), "Suburbs_Floor_3x3m_A91", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5250.0, 3600.0, 800.0), (0.0, 0.0, -0.0), (1.0, 1.0, 1.0), "Suburbs_Floor_3x3m_A92", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5550.0, 3300.0, 800.0), (0.0, 0.0, -0.0), (1.0, 1.0, 1.0), "Suburbs_Floor_3x3m_A93", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5850.0, 3300.0, 800.0), (0.0, 0.0, -0.0), (1.0, 1.0, 1.0), "Suburbs_Floor_3x3m_A94", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (6150.0, 3300.0, 800.0), (0.0, 0.0, -0.0), (1.0, 1.0, 1.0), "Suburbs_Floor_3x3m_A95", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4950.0, 3300.0, 800.0), (0.0, 0.0, -0.0), (1.0, 1.0, 1.0), "Suburbs_Floor_3x3m_A96", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5250.0, 3300.0, 800.0), (0.0, 0.0, -0.0), (1.0, 1.0, 1.0), "Suburbs_Floor_3x3m_A97", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5550.0, 3000.0, 800.0), (0.0, 0.0, -0.0), (1.0, 1.0, 1.0), "Suburbs_Floor_3x3m_A98", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5850.0, 3000.0, 800.0), (0.0, 0.0, -0.0), (1.0, 1.0, 1.0), "Suburbs_Floor_3x3m_A99", _folder)
if a: placed += 1
else: skipped += 1

# Batch 15: StaticMesh'Suburbs_Floor_3x3m_AA_Broken' (2 instances)
_mesh_path = "/Game/Art/Assets/Kits/Architecture/Suburbs/Suburbs_Floor_3x3m_AA_Broken"
_materials = ['/Game/Art/Assets/Kits/Architecture/Suburbs/Suburbs_Floor/Materials/Subrubs_Floor_Tileable_A/MI_Suburbs_Floor_A_inst']
_folder = "Reconstruction/BD_BB_SnakingRiver_Urban/Meshes"
a = spawn_static_mesh(_mesh_path, _materials, (3350.0, 500.0, 800.0), (0.0, -90.00002735739477, 0.0), (-1.0, 1.0, 1.0), "Suburbs_Floor_3x3m_AA_Broken_1088", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (450.0, 2950.0, 800.0), (0.0, 90.00004680423052, -0.0), (1.0, 1.0, 1.0), "Suburbs_Floor_3x3m_AA_Broken2_16", _folder)
if a: placed += 1
else: skipped += 1

# Batch 16: StaticMesh'Suburbs_Floor_3x3m_AB_Broken' (3 instances)
_mesh_path = "/Game/Art/Assets/Kits/Architecture/Suburbs/Suburbs_Floor_3x3m_AB_Broken"
_materials = ['/Game/Art/Assets/Kits/Architecture/Suburbs/Suburbs_Floor/Materials/Subrubs_Floor_Tileable_A/MI_Suburbs_Floor_A_inst']
_folder = "Reconstruction/BD_BB_SnakingRiver_Urban/Meshes"
a = spawn_static_mesh(_mesh_path, _materials, (3050.0, 500.0, 800.0), (0.0, 179.99992486791828, -0.0), (-1.0, 1.0, 1.0), "Suburbs_Floor_3x3m_AB_Broken_1104", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (450.0, 3250.0, 800.0), (0.0, 89.99995929348692, -0.0), (1.0, 1.0, 1.0), "Suburbs_Floor_3x3m_AB_Broken2_19", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (450.0, 3550.0, 800.0), (0.0, 90.00004680423052, -0.0), (1.0, 1.0, 1.0), "Suburbs_Floor_3x3m_AB_Broken3", _folder)
if a: placed += 1
else: skipped += 1

# Batch 17: StaticMesh'Suburbs_Floor_3x3m_Detail_A' (13 instances)
_mesh_path = "/Game/Art/Assets/Kits/Architecture/Suburbs/Suburbs_Floor_3x3m_Detail_A"
_materials = ['/Game/Art/Assets/Kits/Architecture/Suburbs/Suburbs_Floor/Materials/Subrubs_Floor_Tileable_A/MI_Suburbs_Floor_A_inst']
_folder = "Reconstruction/BD_BB_SnakingRiver_Urban/Meshes"
a = spawn_static_mesh(_mesh_path, _materials, (3088.0, 453.0, 805.0), (5.318462494561113, 9.999595081871812e-07, 0.5430360045783825), (1.0, 1.0, 1.0), "Suburbs_Floor_3x3m_Detail_A_1107", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (338.31808, 3652.7356, 806.33435), (-3.208679274775292, 0.0, -0.0), (1.0, 1.0, 1.0), "Suburbs_Floor_3x3m_Detail_A10_60", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (129.08083, 3108.598, 805.96277), (2.3542571090871625, 5.831739567455908e-09, 1.8319018572770829), (1.0, 1.0, 1.0), "Suburbs_Floor_3x3m_Detail_A11_69", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (244.08447, 3110.0083, 805.4171), (-1.4992066983556, -0.02587890849513146, 0.989507972954555), (1.0, 1.0, 1.0), "Suburbs_Floor_3x3m_Detail_A12_75", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (501.642, 3384.7554, 797.94763), (-7.572844968623544, -179.62359442149491, -1.802063059796318), (1.0, 1.0, 1.0), "Suburbs_Floor_3x3m_Detail_A13", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3443.0, 697.0, 801.0), (4.429477193603114, 0.3030000359590712, 8.181247931022504), (1.0, 1.0, 1.0), "Suburbs_Floor_3x3m_Detail_A2", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3123.0, 245.0, 806.0), (0.0, 0.0, -0.0), (1.0, 1.0, 1.0), "Suburbs_Floor_3x3m_Detail_A3_1130", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3330.0, 134.0, 806.0), (1.3924770696304016, -0.2159118475447436, -3.025237575228664), (1.0, 1.0, 1.0), "Suburbs_Floor_3x3m_Detail_A4", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3185.0, 613.0, 798.0), (0.0, 0.0, 1.4850259729644932), (1.0, 1.0, 1.0), "Suburbs_Floor_3x3m_Detail_A5_4", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (350.0, 3300.0, 800.0), (0.0, 0.0, -0.0), (1.0, 1.0, 1.0), "Suburbs_Floor_3x3m_Detail_A6_27", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (413.57272, 3533.9446, 802.92365), (4.410197046145984, -179.99998633961633, 2.9999992437652227e-06), (1.0, 1.0, 1.0), "Suburbs_Floor_3x3m_Detail_A7_33", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (634.4103, 2990.6555, 797.94763), (7.572826617114433, -0.37640381965301534, -1.802062988148367), (1.0, 1.0, 1.0), "Suburbs_Floor_3x3m_Detail_A8_39", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (279.971, 3335.1724, 806.3344), (1.4383167277957492, 0.1371749840346452, 2.1330656891762185), (1.0, 1.0, 1.0), "Suburbs_Floor_3x3m_Detail_A9_54", _folder)
if a: placed += 1
else: skipped += 1

# Batch 18: StaticMesh'Suburbs_Floor_3x3m_Detail_C' (13 instances)
_mesh_path = "/Game/Art/Assets/Kits/Architecture/Suburbs/Suburbs_Floor_3x3m_Detail_C"
_materials = ['/Game/Art/Assets/Kits/Architecture/Suburbs/Suburbs_Floor/Materials/Subrubs_Floor_Tileable_A/MI_Suburbs_Floor_A_inst']
_folder = "Reconstruction/BD_BB_SnakingRiver_Urban/Meshes"
a = spawn_static_mesh(_mesh_path, _materials, (3218.0, 435.0, 802.0), (2.5740957617316487, -2.9747982671640647e-09, 2.5792145662633743), (1.0, 1.0, 1.0), "Suburbs_Floor_3x3m_Detail_C_1113", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (527.90656, 3077.7961, 795.9414), (-2.868682865866882, 0.7458389797060945, -6.547485423052173), (1.0, 1.0, 1.0), "Suburbs_Floor_3x3m_Detail_C10_42", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (263.92783, 2940.9028, 806.43634), (-1.6519776141621996, 0.019595998287150487, -0.3622436304982521), (1.0, 1.0, 1.0), "Suburbs_Floor_3x3m_Detail_C11_45", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (187.53064, 3503.5762, 805.3052), (2.953319060504046, -0.06933593272650176, 0.49432996141584906), (1.0, 1.0, 1.0), "Suburbs_Floor_3x3m_Detail_C12_57", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (75.049576, 3391.0923, 803.7905), (-1.264221148711189, 0.0, -0.0), (1.0, 1.0, 1.0), "Suburbs_Floor_3x3m_Detail_C13_72", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3294.0, 544.0, 806.0), (-3.3234248744297212, -0.95742807958047, -2.6616817560298225), (1.0, 1.0, 1.0), "Suburbs_Floor_3x3m_Detail_C2", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3275.0, 266.0, 806.0), (2.7270476342962056, 5.567519878108301e-09, -3.6692500624672615), (1.0, 1.0, 1.0), "Suburbs_Floor_3x3m_Detail_C3_2", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3118.0, 276.0, 802.0), (2.5740957617316487, -2.9747982671640647e-09, 2.5792145662633743), (1.0, 1.0, 1.0), "Suburbs_Floor_3x3m_Detail_C4", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3012.0, 340.0, 806.0), (-1.3638303787075359, 0.10049099233706381, -1.63540642892902), (1.0, 1.0, 1.0), "Suburbs_Floor_3x3m_Detail_C5", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3005.0, 500.0, 795.0), (-1.833312987115641, -0.125274648122525, -11.126036371444743), (1.0, 1.0, 1.0), "Suburbs_Floor_3x3m_Detail_C6", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (428.5251, 3260.0732, 799.5354), (-10.000000164519466, 0.0, -0.0), (1.0, 1.0, 1.0), "Suburbs_Floor_3x3m_Detail_C7_24", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (393.87408, 3108.9395, 806.3345), (-4.996825892141039, 0.17734197186997205, -2.0345457144206036), (1.0, 1.0, 1.0), "Suburbs_Floor_3x3m_Detail_C8_30", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (601.6341, 2865.9297, 803.72705), (-2.9879760189912923, -0.3427124114431663, 6.546065086091424), (1.0, 1.0, 1.0), "Suburbs_Floor_3x3m_Detail_C9_36", _folder)
if a: placed += 1
else: skipped += 1

# Batch 19: StaticMesh'Suburbs_Stairs_Small_B_NonDest' (4 instances)
_mesh_path = "/Game/Art/Assets/Kits/Architecture/Suburbs/Suburbs_Stairs_Small_B_NonDest"
_materials = ['/Game/Art/Assets/Kits/Architecture/Suburbs/Destructable/Materials/MI_Suburbs_Wall_Non_Dest', '/Game/Art/Assets/Kits/Architecture/Suburbs/Materials/Stairs_Medium_C_NonDest/MI_Stairs_Medium_C_NonDes']
_folder = "Reconstruction/BD_BB_SnakingRiver_Urban/Meshes"
a = spawn_static_mesh(_mesh_path, _materials, (2800.0, 5600.0, 700.0), (0.0, -179.9999795094293, 0.0), (1.0, 1.0, 1.0), "Suburbs_Stairs_Small_B2_111", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2600.0, 5600.0, 700.0), (0.0, -179.9999795094293, 0.0), (1.0, 1.0, 1.0), "Suburbs_Stairs_Small_B3", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3800.0, 5600.0, 700.0), (0.0, -179.9999795094293, 0.0), (1.0, 1.0, 1.0), "Suburbs_Stairs_Small_B4", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3600.0, 5600.0, 700.0), (0.0, -179.9999795094293, 0.0), (1.0, 1.0, 1.0), "Suburbs_Stairs_Small_B5", _folder)
if a: placed += 1
else: skipped += 1

# Batch 20: StaticMesh'Suburbs_Stairs_Small_C_NonDest' (1 instances)
_mesh_path = "/Game/Art/Assets/Kits/Architecture/Suburbs/Suburbs_Stairs_Small_C_NonDest"
_materials = ['/Game/Art/Assets/Kits/Architecture/Suburbs/Destructable/Materials/MI_Suburbs_Wall_Non_Dest', '/Game/Art/Assets/Kits/Architecture/Suburbs/Materials/Stairs_Medium_C_NonDest/MI_Stairs_Medium_C_NonDes']
_folder = "Reconstruction/BD_BB_SnakingRiver_Urban/Meshes"
a = spawn_static_mesh(_mesh_path, _materials, (2300.0, 5150.0, 700.0), (0.0, -89.99999818714215, 0.0), (1.0, 1.0, 1.0), "Suburbs_Stairs_Small_C2_120", _folder)
if a: placed += 1
else: skipped += 1

# Batch 21: StaticMesh'Suburbs_Wall_Thick_1x3_A' (2 instances)
_mesh_path = "/Game/Art/Assets/Kits/Architecture/Suburbs/Suburbs_Wall_Thick_1x3_A"
_materials = ['/Game/Art/Assets/Kits/Architecture/Suburbs/Destructable/Materials/MI_Suburbs_Wall_Thick_3x3m_Moss_DMG_A_Dest']
_folder = "Reconstruction/BD_BB_SnakingRiver_Urban/Meshes"
a = spawn_static_mesh(_mesh_path, _materials, (1450.0, 3600.0, 100.0), (0.0, 0.0, -0.0), (1.0, 1.0, 1.0), "Suburbs_Wall_Thick_1x3_A_30", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1750.0, 3600.0, 100.0), (0.0, 0.0, -0.0), (1.0, 1.0, 1.0), "Suburbs_Wall_Thick_1x3_A2", _folder)
if a: placed += 1
else: skipped += 1

# Batch 22: StaticMesh'Suburbs_Wall_Thick_3x3m_A' (9 instances)
_mesh_path = "/Game/Art/Assets/Kits/Architecture/Suburbs/Suburbs_Wall_Thick_3x3m_A"
_materials = ['/Game/Art/Assets/Kits/Architecture/Suburbs/Destructable/Materials/MI_Suburbs_Wall_Non_Dest']
_folder = "Reconstruction/BD_BB_SnakingRiver_Urban/Meshes"
a = spawn_static_mesh(_mesh_path, _materials, (1850.0, 5050.0, 200.0), (0.0, 0.0, -0.0), (1.0, 1.0, 1.0), "Suburbs_Wall_Thick_3x3m_A10", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1550.0, 4450.0, 200.0), (0.0, 0.0, -0.0), (1.0, 1.0, 1.0), "Suburbs_Wall_Thick_3x3m_A11_38", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2150.0, 5050.0, 200.0), (0.0, 0.0, -0.0), (1.0, 1.0, 1.0), "Suburbs_Wall_Thick_3x3m_A13", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1650.0, 4900.0, 200.0), (0.0, 90.0000030488508, -0.0), (1.0, 1.0, 1.0), "Suburbs_Wall_Thick_3x3m_A15", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1650.0, 4600.0, 200.0), (0.0, 90.0000030488508, -0.0), (1.0, 1.0, 1.0), "Suburbs_Wall_Thick_3x3m_A17", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1250.0, 3600.0, 200.0), (0.0, 0.0, -0.0), (1.0, 1.0, 1.0), "Suburbs_Wall_Thick_3x3m_A4", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1550.0, 3600.0, 200.0), (0.0, 0.0, -0.0), (1.0, 1.0, 1.0), "Suburbs_Wall_Thick_3x3m_A5", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1850.0, 3600.0, 200.0), (0.0, 0.0, -0.0), (1.0, 1.0, 1.0), "Suburbs_Wall_Thick_3x3m_A6", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1250.0, 4450.0, 500.0), (0.0, 0.0, -0.0), (1.0, 1.0, 1.0), "Suburbs_Wall_Thick_3x3m_A7", _folder)
if a: placed += 1
else: skipped += 1

# Batch 23: StaticMesh'Suburbs_Dirt_Mound_A' (4 instances)
_mesh_path = "/Game/Art/Assets/Kits/Misc/Dirt_Mounds/Suburbs_Dirt_Mound_A"
_materials = ['/Game/Art/Assets/Kits/Misc/Dirt_Mounds/Materials/Suburbs_Dirt_Inst']
_folder = "Reconstruction/BD_BB_SnakingRiver_Urban/Meshes"
a = spawn_static_mesh(_mesh_path, _materials, (3013.0, 418.0, 800.0), (0.0, -27.713104875438443, 0.0), (1.0, 1.0, 1.0), "Suburbs_Dirt_Mound_A_1120", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3485.0, 674.0, 800.0), (0.0, 117.3158743704739, -0.0), (1.40625, 1.375, 0.5625), "Suburbs_Dirt_Mound_A2_1127", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (539.75574, 2938.571, 795.9829), (0.0, 144.0354705830427, -0.0), (1.28125, 1.28125, 0.90625), "Suburbs_Dirt_Mound_A3_91", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (648.8461, 2824.8884, 798.34674), (0.0, -64.05920713349033, 0.0), (1.0, 1.0, 1.0), "Suburbs_Dirt_Mound_A4_97", _folder)
if a: placed += 1
else: skipped += 1

# Batch 24: StaticMesh'Suburbs_Dirt_Mound_B' (6 instances)
_mesh_path = "/Game/Art/Assets/Kits/Misc/Dirt_Mounds/Suburbs_Dirt_Mound_B"
_materials = ['/Game/Art/Assets/Kits/Misc/Dirt_Mounds/Materials/Suburbs_Dirt_Inst']
_folder = "Reconstruction/BD_BB_SnakingRiver_Urban/Meshes"
a = spawn_static_mesh(_mesh_path, _materials, (3304.0, 580.0, 796.0), (0.0, 26.27681846207435, -0.0), (1.375, 1.375, 1.375), "Suburbs_Dirt_Mound_B_7", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (443.00113, 3623.0874, 793.34485), (0.0, 98.80760614192087, -0.0), (1.0, 1.0, 1.0), "Suburbs_Dirt_Mound_B2_79", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (462.74466, 3029.2468, 789.8192), (0.0, -53.292145451184616, 0.0), (1.4375, 1.4375, 1.65625), "Suburbs_Dirt_Mound_B3_88", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (443.06375, 3502.41, 792.49915), (0.0, 5.00457812112403, -0.0), (1.40625, 1.40625, 1.40625), "Suburbs_Dirt_Mound_B4_100", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (406.595, 3338.5154, 792.8446), (0.0, 0.0, -0.0), (1.375, 1.65625, 1.0), "Suburbs_Dirt_Mound_B5_103", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (429.16284, 3133.2363, 789.6428), (0.0, -69.12411563902785, 0.0), (1.59375, 1.59375, 1.59375), "Suburbs_Dirt_Mound_B6_106", _folder)
if a: placed += 1
else: skipped += 1

# Batch 25: StaticMesh'Suburbs_Dirt_Mound_C' (3 instances)
_mesh_path = "/Game/Art/Assets/Kits/Misc/Dirt_Mounds/Suburbs_Dirt_Mound_C"
_materials = ['/Game/Art/Assets/Kits/Misc/Dirt_Mounds/Materials/Suburbs_Dirt_Inst']
_folder = "Reconstruction/BD_BB_SnakingRiver_Urban/Meshes"
a = spawn_static_mesh(_mesh_path, _materials, (3383.0, 630.0, 792.0), (0.0, 168.04460078485366, -0.0), (1.0, 1.0, 1.3125), "Suburbs_Dirt_Mound_C_1124", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (383.73373, 3264.3123, 788.16943), (0.0, 98.87859250654955, -0.0), (1.28125, 1.28125, 1.34375), "Suburbs_Dirt_Mound_C2_82", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (609.5988, 2991.5803, 792.6974), (0.0, -114.6692466165626, 0.0), (1.0, 1.0, 1.0), "Suburbs_Dirt_Mound_C3_94", _folder)
if a: placed += 1
else: skipped += 1

# Batch 26: StaticMesh'Suburbs_Dirt_Mound_D' (1 instances)
_mesh_path = "/Game/Art/Assets/Kits/Misc/Dirt_Mounds/Suburbs_Dirt_Mound_D"
_materials = ['/Game/Art/Assets/Kits/Misc/Dirt_Mounds/Materials/Suburbs_Dirt_Inst']
_folder = "Reconstruction/BD_BB_SnakingRiver_Urban/Meshes"
a = spawn_static_mesh(_mesh_path, _materials, (3293.0, 454.0, 800.0), (0.0, 60.70852775878679, -0.0), (1.96875, 1.90625, 0.8125), "Suburbs_Dirt_Mound_D_1117", _folder)
if a: placed += 1
else: skipped += 1

# Batch 27: StaticMesh'SM_Bubble_SnakingRiver_Urban_Floor' (1 instances)
_mesh_path = "/Game/LevelDesign/GuideMeshes/Generic/SnakingRiver/SM_Bubble_SnakingRiver_Urban_Floor"
_materials = ['/Game/Environments/ProcTexturing/MI_ProcGenRock_Quarry_Parent']
_folder = "Reconstruction/BD_BB_SnakingRiver_Urban/Meshes"
a = spawn_static_mesh(_mesh_path, _materials, (0.0, 0.0, 0.0), (0.0, 0.0, -0.0), (1.0, 1.0, 1.0), "SM_Bubble_SnakingRiver_Urban_Floor_2", _folder)
if a: placed += 1
else: skipped += 1

# Batch 28: StaticMesh'PWM_Quarry_1x1x1_A' (73 instances)
_mesh_path = "/Game/Unshippable/Whitebox/Rocks/Meshes/PWM_Quarry_1x1x1_A"
_materials = ['/Game/Environments/ProcTexturing/ProcMaterial_Quarry_Atlas_1']
_folder = "Reconstruction/BD_BB_SnakingRiver_Urban/Meshes"
a = spawn_static_mesh(_mesh_path, _materials, (800.0, 2550.0, 1150.0), (-15.000001513189739, 0.0, -0.0), (3.34375, 2.21875, 2.46875), "PWM_Quarry_1x1x1_A_5", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (300.0, 3964.1313, 895.81604), (4.565380272359259, -44.51162829206292, 3.775903651035597), (1.84375, 3.625, 2.4375), "PWM_Quarry_1x1x1_A10_174", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (199.99951, 4112.907, 826.81726), (-4.999818246788899, -90.00007295986362, -179.99936502245257), (2.5, 1.0, 2.15625), "PWM_Quarry_1x1x1_A11_180", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (575.00006, 3793.3013, 700.0), (0.0, -30.000089710185883, 0.0), (2.90625, 3.03125, 2.75), "PWM_Quarry_1x1x1_A12_198", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2138.0288, 3767.9749, 709.4426), (9.846570891505824, 9.85103798402472, -91.75368605455009), (3.1875, 1.71875, 1.90625), "PWM_Quarry_1x1x1_A13_207", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2366.3792, 3906.699, 552.5593), (4.328995311187839, -149.90476108462036, 92.5049597439834), (3.0625, 1.8125, 2.4375), "PWM_Quarry_1x1x1_A14_213", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2411.2312, 2912.2175, 1188.9319), (7.4370175238382465, -59.144945372114044, -166.93008627411373), (2.875, 2.71875, 2.28125), "PWM_Quarry_1x1x1_A15", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4615.6123, 3841.5444, 1749.2075), (-46.08932477416184, 5.288136304219076, 178.6043535202296), (1.90625, 3.59375, 1.34375), "PWM_Quarry_1x1x1_A16_227", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (691.396, 4300.0, 596.20636), (4.923863337754466, -114.96160171648123, 0.8703909669435534), (3.9375, 3.5625, 3.71875), "PWM_Quarry_1x1x1_A17_264", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (741.396, 4400.0, 946.2063), (9.618244109998495, 20.258403702275487, 2.6061370708181273), (3.9375, 2.40625, 3.34375), "PWM_Quarry_1x1x1_A18", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (600.0, 3900.0, 600.0), (0.0, 40.00004110866871, -0.0), (4.1875, 5.34375, 1.875), "PWM_Quarry_1x1x1_A19_285", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2148.7544, 2778.0408, 1474.238), (-14.999939281381, 45.0003043659119, 5.7250708318724945e-05), (3.25, 1.78125, 2.15625), "PWM_Quarry_1x1x1_A2_43", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2694.5007, 4050.0, 574.0435), (-4.923858421121702, 10.037483212036618, 89.12969301663965), (2.78125, 1.4375, 3.0625), "PWM_Quarry_1x1x1_A20_297", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3493.7615, 3951.3054, 590.5174), (-0.6459351629491082, -7.175812406400497, -10.933197547220663), (3.0, 3.0, 1.875), "PWM_Quarry_1x1x1_A21_309", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3346.4028, 4105.622, 1431.8865), (-3.49878516601795e-14, 4.999999778234487e-06, 10.000514373082543), (2.78125, 1.75, 1.34375), "PWM_Quarry_1x1x1_A24_385", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3617.101, 3996.9846, 1350.0), (0.0, -20.000060948281234, 0.0), (4.625, 2.03125, 2.625), "PWM_Quarry_1x1x1_A26_431", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1393.49, 2546.244, 1132.696), (-14.999848299004778, 20.000075602625664, 1.2197343913029859e-06), (2.59375, 1.875, 1.65625), "PWM_Quarry_1x1x1_A3_49", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3900.0002, 4012.9421, 1648.296), (2.5760132104262845, -9.66580172455158, 14.783602647461501), (1.0, 3.0625, 1.0), "PWM_Quarry_1x1x1_A31_480", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3167.101, 4203.0156, 1450.0), (0.0, 20.000177425948408, -0.0), (1.53125, 1.0, 1.21875), "PWM_Quarry_1x1x1_A32_492", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4150.0, 3900.0, 1650.0), (-19.68319827853131, -18.617735211651635, 10.629699975000037), (1.0, 2.8125, 1.0), "PWM_Quarry_1x1x1_A33_513", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5150.0, 2550.0, 1200.0), (4.98092212416651, -5.019103342187573, 9.563248853997756), (0.90625, 3.59375, 1.71875), "PWM_Quarry_1x1x1_A35_653", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3950.0, 2900.0, 950.0), (0.0, 0.0, 79.9999683893994), (1.8125, 3.15625, 4.46875), "PWM_Quarry_1x1x1_A36_549", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4350.0, 3100.0, 1800.0), (-10.000000969912895, 70.00005735955085, 1.0103111475757249e-06), (3.5, 1.84375, 1.0), "PWM_Quarry_1x1x1_A37_576", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4600.0, 2950.0, 1850.0), (-21.97320194133043, -23.835722122413298, 98.4608687654708), (2.53125, 1.46875, 6.71875), "PWM_Quarry_1x1x1_A38_588", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4177.743, 2223.776, 1740.2329), (-3.0532570513635925e-05, -10.000152328388964, 5.001120053568466), (2.15625, 5.0625, 2.09375), "PWM_Quarry_1x1x1_A39_624", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2146.9373, 2771.49, 1153.472), (-5.0482741924753486e-09, -30.00006702968785, 15.001306446609659), (1.0, 3.46875, 2.28125), "PWM_Quarry_1x1x1_A4_64", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5200.0, 2400.0, 1450.0), (14.757675571719917, -14.81176639311832, 11.578537343861761), (2.0, 4.3125, 2.21875), "PWM_Quarry_1x1x1_A40_633", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3940.4277, 2337.0679, 1671.9858), (-10.5251776361411, -28.013856392667766, 11.556828076220093), (1.59375, 3.875, 1.4375), "PWM_Quarry_1x1x1_A42_671", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3819.6853, 1837.159, 1743.2292), (7.547395987601711e-07, -39.99954179671332, 20.000244636111756), (1.90625, 3.5625, 1.34375), "PWM_Quarry_1x1x1_A43_680", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4550.0, 1600.0, 1500.0), (7.4357316926286865, -29.14718409670917, 13.065629146002435), (1.84375, 4.53125, 1.375), "PWM_Quarry_1x1x1_A44_692", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4001.889, 2514.875, 1539.9509), (-12.208494208282211, -39.880578752854646, 12.332909311870571), (1.0, 4.40625, 1.5), "PWM_Quarry_1x1x1_A45_701", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1762.9409, 3700.0, 1948.2963), (-9.999969562555277, 0.0, -0.0), (3.4375, 2.3125, 1.75), "PWM_Quarry_1x1x1_A5_87", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4133.2847, 942.9869, 849.3069), (9.657558051789334, -105.21910971955792, 2.3872576788372153), (2.6875, 3.84375, 2.03125), "PWM_Quarry_1x1x1_A53_809", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4211.6978, 1182.1394, 1300.0), (0.0, -40.00005923828246, 0.0), (1.0, 2.90625, 1.0625), "PWM_Quarry_1x1x1_A54_821", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3528.8704, 314.05627, 1257.1104), (4.2087544269133454, -24.66387957015627, 9.08095857367389), (1.0, 3.28125, 1.78125), "PWM_Quarry_1x1x1_A55_827", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4571.3213, 1840.9575, 650.0), (0.0, 40.000080625833, -0.0), (2.96875, 2.6875, 1.875), "PWM_Quarry_1x1x1_A56_833", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3208.0388, 1368.2318, 600.0), (0.0, -54.99929925772355, 0.0), (1.6875, 3.84375, 1.40625), "PWM_Quarry_1x1x1_A57_845", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2917.3657, 301.5194, 700.0), (0.0, 10.000611709903884, -0.0), (1.65625, 3.78125, 1.6875), "PWM_Quarry_1x1x1_A58_854", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2767.101, 1046.9846, 700.0), (0.0, -20.000060948281234, 0.0), (1.5, 1.5, 1.84375), "PWM_Quarry_1x1x1_A59_866", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3050.0, 3903.4077, 1575.8828), (0.0, 0.0, 15.000522649573501), (1.875, 3.53125, 1.5), "PWM_Quarry_1x1x1_A6_105", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3916.9326, 2533.3564, 1420.0498), (-22.315428083848342, -45.24791953998414, 15.251318254350755), (1.375, 3.21875, 1.1875), "PWM_Quarry_1x1x1_A60_872", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3950.0, 2550.0, 950.0), (-4.999847346439805, 45.000085275101526, 5.674812628209812e-06), (1.71875, 1.71875, 1.71875), "PWM_Quarry_1x1x1_A61_887", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3595.1365, 2291.5325, 692.1867), (2.7171006012523038e-05, -59.99960400503391, 15.000635045922868), (1.0, 4.53125, 2.71875), "PWM_Quarry_1x1x1_A62_899", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3328.4321, 2095.9373, 949.2403), (-14.99993918385201, 35.0012119425259, 6.210587731034327e-05), (3.21875, 1.0, 2.125), "PWM_Quarry_1x1x1_A63_905", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3869.9006, 2416.6953, 792.8993), (-9.999632597891805, -139.99870277148096, 0.0002376358608803319), (2.75, 1.0, 1.34375), "PWM_Quarry_1x1x1_A64_911", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2916.5266, 1757.5884, 1416.6122), (-23.39874094838222, -59.061402788162724, 21.8804300269191), (1.4375, 5.21875, 2.0), "PWM_Quarry_1x1x1_A65_917", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2418.0212, 1379.4603, 1634.5142), (2.754142231071346e-05, -59.9988689883249, 24.99703614461445), (1.0, 5.25, 1.9375), "PWM_Quarry_1x1x1_A66_927", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1993.2065, 1136.0837, 672.2579), (1.5811961987700418, -39.70718914893999, 24.348975499391475), (1.0, 2.90625, 2.5), "PWM_Quarry_1x1x1_A67_933", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1843.7717, 556.75525, 695.659), (-4.980926239519767, -16.316738057402347, 34.621664211964045), (1.0, 3.21875, 1.5), "PWM_Quarry_1x1x1_A68_942", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1850.0, 749.9996, 900.0), (0.0, 0.0, -89.99954442862955), (1.0, 1.0, 2.25), "PWM_Quarry_1x1x1_A69_951", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (300.0, 4696.7344, 644.15967), (0.0, 0.0, -4.999847507378993), (1.96875, 3.96875, 1.9375), "PWM_Quarry_1x1x1_A7_126", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1758.2157, 717.9484, 980.3159), (0.22313740663971274, 172.3816569084096, -101.18736702225908), (1.0, 1.4375, 2.75), "PWM_Quarry_1x1x1_A70", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2809.3691, 342.2619, 900.0), (0.0, -15.000058335092751, 0.0), (1.875, 1.6875, 1.78125), "PWM_Quarry_1x1x1_A71_1018", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3550.0, 200.0, 950.0), (0.0, 0.0, -0.0), (1.78125, 2.6875, 2.59375), "PWM_Quarry_1x1x1_A72_963", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2747.943, 1333.8081, 1657.448), (-1.293273952380695, -35.16796796640751, 4.949585856021909), (2.0, 4.375, 1.53125), "PWM_Quarry_1x1x1_A73_973", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3531.2617, 566.75977, 1385.3232), (-5.715972539603886, -34.58905370284019, -8.219023324141613), (1.96875, 2.84375, 1.0), "PWM_Quarry_1x1x1_A74_983", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2950.761, 493.5299, 1371.4768), (-6.122436595460167, -3.53500394994402, -15.030915956129352), (2.625, 4.0, 0.53125), "PWM_Quarry_1x1x1_A75_989", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2705.789, 665.7824, 1490.6095), (-6.584991385223585, -9.041229199840325, -14.041900056376466), (3.0, 4.5, 0.65625), "PWM_Quarry_1x1x1_A76_995", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2288.6418, 1033.4904, 1767.4109), (6.31730955338697, -35.768922087009216, 4.2130376397233835), (1.96875, 5.25, 1.9375), "PWM_Quarry_1x1x1_A77", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2415.7979, 493.96924, 600.0), (0.0, 20.000039410127965, -0.0), (4.15625, 3.40625, 2.5), "PWM_Quarry_1x1x1_A78_1005", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2500.0, 450.0, 800.0), (0.0, -10.000030597161448, 0.0), (3.8125, 1.6875, 1.53125), "PWM_Quarry_1x1x1_A79_1011", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2760.3843, 3805.5237, 750.75964), (2.009356359518124e-05, 155.00024767060367, -15.00005762697777), (2.125, 3.09375, 1.8125), "PWM_Quarry_1x1x1_A8_139", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2888.7617, 151.6, 1100.0), (0.0, 99.99988498550958, -0.0), (2.15625, 1.0, 2.125), "PWM_Quarry_1x1x1_A80", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2500.0, 450.0, 1400.0), (0.0, 0.0, -0.0), (3.53125, 1.5, 1.5625), "PWM_Quarry_1x1x1_A81_1025", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1966.382, 1426.0172, 1094.6542), (-4.8292239219723, -46.2972424978938, 5.055948030161609), (2.03125, 2.125, 4.0625), "PWM_Quarry_1x1x1_A83_1034", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3676.5933, 2806.8198, 876.7267), (-27.74041517616997, 36.23053432156212, 1.0372850605037974e-06), (1.8125, 3.75, 1.59375), "PWM_Quarry_1x1x1_A84_8", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3130.3635, 3337.721, 1400.0), (0.0, 145.00014668267553, -0.0), (3.84375, 1.65625, 1.875), "PWM_Quarry_1x1x1_A85_17", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2785.466, 2904.1614, 1350.0), (0.0, 129.99999598831678, -0.0), (2.9375, 1.0, 2.5), "PWM_Quarry_1x1x1_A86_29", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1985.3549, 688.1736, 1206.7312), (-2.5758969173971624, -14.78259064867101, -9.66586202908851), (2.375, 1.5, 2.34375), "PWM_Quarry_1x1x1_A87_56", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2650.0, 452.27887, 1223.9525), (0.0, 0.0, -10.000030597161448), (1.4375, 2.53125, 1.0), "PWM_Quarry_1x1x1_A88_62", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2714.968, 824.8738, 800.0), (0.0, -50.00006299960901, 0.0), (2.0625, 1.75, 1.0), "PWM_Quarry_1x1x1_A89_71", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (349.9977, 4066.227, 672.1144), (-1.1638796439426515, -134.82671799145257, -3.212524806578381), (4.75, 2.9375, 3.78125), "PWM_Quarry_1x1x1_A9_160", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4638.3022, 1832.1394, 750.0), (0.0, 40.000051265877424, -0.0), (2.09375, 1.0, 1.0), "PWM_Quarry_1x1x1_A90_74", _folder)
if a: placed += 1
else: skipped += 1

# Batch 29: StaticMesh'PWM_Quarry_1X1x1_C' (4 instances)
_mesh_path = "/Game/Unshippable/Whitebox/Rocks/Meshes/PWM_Quarry_1X1x1_C"
_materials = ['/Game/Environments/ProcTexturing/ProcMaterial_Quarry_Atlas_1']
_folder = "Reconstruction/BD_BB_SnakingRiver_Urban/Meshes"
a = spawn_static_mesh(_mesh_path, _materials, (700.0, 2600.0, 1700.0), (-15.000000804899807, -15.000059229117822, -6.75271519797669e-08), (4.40625, 1.0, 2.15625), "PWM_Quarry_1X1x1_C_11", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4100.0, 2900.0, 1750.0), (-64.99947495224853, -179.999986339611, -179.99994535844377), (2.03125, 5.0, 4.5625), "PWM_Quarry_1X1x1_C2_567", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3000.0, 3749.2405, 1341.3175), (0.0, 0.0, 10.000119242168408), (1.90625, 3.28125, 4.28125), "PWM_Quarry_1X1x1_C3_148", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4664.2793, 2181.894, 1797.248), (-1.7081904594614439, -19.929961224246565, 15.300260319839186), (3.625, 4.03125, 2.4375), "PWM_Quarry_1X1x1_C4_618", _folder)
if a: placed += 1
else: skipped += 1

# Batch 30: StaticMesh'PWM_Quarry_2x2x2_A' (104 instances)
_mesh_path = "/Game/Unshippable/Whitebox/Rocks/Meshes/PWM_Quarry_2x2x2_A"
_materials = ['/Game/Environments/ProcTexturing/ProcMaterial_Quarry_Atlas_1']
_folder = "Reconstruction/BD_BB_SnakingRiver_Urban/Meshes"
a = spawn_static_mesh(_mesh_path, _materials, (400.0, 2500.0, 850.0), (-15.000001513189739, 0.0, -0.0), (2.9375, 1.90625, 0.96875), "PWM_Quarry_2x2x2_A_204", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1385.306, 3175.3237, 1843.9639), (-2.293579152517563, -56.4705838580258, 8.622642201550677), (1.75, 1.84375, 1.0), "PWM_Quarry_2x2x2_A10_81", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4001.3347, 784.1986, 1054.3566), (0.00038066442732330506, 145.0002269220846, -94.99954478942522), (1.0, 1.0, 3.09375), "PWM_Quarry_2x2x2_A105_812", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3669.8457, 605.0244, 895.09143), (0.8671640272945462, -24.96200600036436, 9.925231910424133), (1.0, 2.59375, 1.53125), "PWM_Quarry_2x2x2_A106_815", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4091.0835, 928.611, 1132.4938), (2.49764991178135, -29.905460436745514, 9.333379911032544), (1.0, 1.96875, 1.125), "PWM_Quarry_2x2x2_A107_824", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4800.0, 1900.0, 650.0), (0.0, 44.99992995072874, -0.0), (2.09375, 1.40625, 1.40625), "PWM_Quarry_2x2x2_A108_830", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4057.0771, 1718.0771, 750.0), (0.0, -70.00002222525863, 0.0), (0.65625, 2.375, 0.5), "PWM_Quarry_2x2x2_A109_838", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2304.522, 3449.6196, 1850.5521), (-14.941468270445478, 5.175541801423266, -1.3377990366886292), (3.0, 2.03125, 1.0), "PWM_Quarry_2x2x2_A11_90", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3288.3022, 1367.8606, 700.0), (0.0, -50.00006299960901, 0.0), (1.0, 1.90625, 0.78125), "PWM_Quarry_2x2x2_A110_848", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3034.2368, 1218.6764, 650.0), (0.0, 15.000067733688155, -0.0), (1.4375, 1.4375, 1.25), "PWM_Quarry_2x2x2_A111_851", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2806.281, 1148.4833, 700.0), (0.0, 30.000121573861183, -0.0), (1.0, 0.84375, 1.0), "PWM_Quarry_2x2x2_A112_860", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3399.959, 2199.9626, 1575.8439), (3.845936500395508e-05, -44.99902834591456, 100.0004847194833), (1.0, 1.0, 2.59375), "PWM_Quarry_2x2x2_A113_869", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4002.377, 2634.0967, 1123.9633), (-5.940215622931171, 43.68549520286436, 1.445153369885599), (1.3125, 0.8125, 0.9375), "PWM_Quarry_2x2x2_A114_884", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3310.9614, 2072.026, 1423.1139), (-14.766420195590088, 44.650164602990166, -12.33938717895543), (2.0625, 1.0, 1.0), "PWM_Quarry_2x2x2_A115_896", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3189.844, 2054.9214, 1085.2379), (-17.086304275588958, -44.87033161343101, 12.854811055455034), (1.125, 2.5, 2.125), "PWM_Quarry_2x2x2_A116_902", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2448.5713, 1606.7908, 1042.3177), (19.6062232909497, -154.8917572239492, 1.3568951758509433), (2.375, 1.0, 1.25), "PWM_Quarry_2x2x2_A117_923", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2616.8186, 1674.9929, 1246.8744), (3.405026544006834, -54.406774844523085, 109.7205131715607), (1.0, 1.1875, 3.375), "PWM_Quarry_2x2x2_A118", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1702.9612, 946.58923, 711.2913), (3.404997253156469, -24.40817205894296, 94.72004314842074), (1.59375, 1.59375, 1.59375), "PWM_Quarry_2x2x2_A119_939", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2950.0, 3668.0527, 1587.1202), (0.0003069999552305531, 179.9998633962053, -105.00052189344095), (1.0, 1.21875, 2.6875), "PWM_Quarry_2x2x2_A12_99", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1981.698, 641.5066, 650.0), (0.0, -119.99980674848695, 0.0), (2.21875, 1.96875, 1.96875), "PWM_Quarry_2x2x2_A120_1002", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2201.0437, 1520.361, 1099.3436), (5.874693145449145, -48.810488591638375, 19.247985444802648), (1.0, 2.375, 1.21875), "PWM_Quarry_2x2x2_A121_955", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1768.9022, 651.8776, 1317.669), (-12.60238542057877, -2.893280004716952, 94.23415795076505), (1.0, 1.53125, 2.0), "PWM_Quarry_2x2x2_A122", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3176.614, 1549.5029, 1643.9694), (-3.1047359992345225, -31.13381510615138, 14.871209387560722), (1.0, 1.9375, 1.25), "PWM_Quarry_2x2x2_A123_967", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3512.3108, 923.71716, 1610.5172), (82.8547685575886, 79.94291103185216, 109.77481928563626), (1.0, 1.71875, 2.15625), "PWM_Quarry_2x2x2_A124_976", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3179.5686, 1071.0547, 1635.5231), (-79.65264313172077, -138.42071180936557, -72.44476940126124), (0.71875, 1.9375, 2.21875), "PWM_Quarry_2x2x2_A125", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3154.3577, 644.3891, 1514.323), (-4.923827970150549, 0.8703890191725907, -10.037537069991329), (1.9375, 1.96875, 1.0), "PWM_Quarry_2x2x2_A126_986", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3150.0, 238.76302, 1285.3558), (19.999557911241208, 89.99999275921428, 89.99999275921428), (1.71875, 0.5625, 3.21875), "PWM_Quarry_2x2x2_A127_992", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2193.7546, 606.01733, 1580.1233), (-73.25258399145727, 74.19765141558011, -89.64982493907766), (1.28125, 3.125, 2.34375), "PWM_Quarry_2x2x2_A128_998", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1884.2429, 464.96814, 1100.0), (0.0, -25.00003249417806, 0.0), (2.4375, 1.9375, 2.28125), "PWM_Quarry_2x2x2_A129_1014", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2505.0557, 3088.972, 1611.2372), (-14.999939528313893, 39.99992005392584, 5.80510081273322e-05), (1.71875, 1.15625, 0.71875), "PWM_Quarry_2x2x2_A13_108", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2935.7761, 143.44739, 950.0), (2.943030691826996e-05, 25.00037665113935, 89.99996989264561), (0.59375, 1.375, 1.15625), "PWM_Quarry_2x2x2_A130_1021", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3371.4575, 2226.178, 1063.6681), (-1.2186888184605051, 46.622932881012616, -5.374694261369539), (0.90625, 1.0, 1.96875), "PWM_Quarry_2x2x2_A132_5", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2685.3555, 3314.6448, 750.0), (4.999998135669519, -134.99986047448618, 8.069160455819167e-06), (2.09375, 1.0, 1.15625), "PWM_Quarry_2x2x2_A133_20", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3266.0652, 2394.328, 1011.4238), (-4.9236748120939255, 40.03760202875448, 179.12959364482157), (0.5625, 2.0625, 1.625), "PWM_Quarry_2x2x2_A134_26", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3172.2068, 3237.5884, 1550.0), (0.0, -35.00006033507422, 0.0), (2.59375, 1.65625, 1.0), "PWM_Quarry_2x2x2_A135_35", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3014.6445, 2835.3552, 1549.9995), (-0.0002787172279617567, 45.00007051095174, -89.9996036080239), (1.75, 1.0, 3.0), "PWM_Quarry_2x2x2_A136_38", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2578.208, 572.762, 800.0), (0.0, 25.00004105917833, -0.0), (1.0, 1.0, 2.3125), "PWM_Quarry_2x2x2_A137_44", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2350.0, 650.0, 800.0), (2.1811887881968305e-13, -10.000030597162153, -3.0517575447653198e-05), (1.65625, 1.15625, 2.78125), "PWM_Quarry_2x2x2_A138_59", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2200.0, 850.0, 1500.0), (0.0, 0.0, -15.000058335092751), (1.21875, 2.15625, 1.0), "PWM_Quarry_2x2x2_A139_65", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2192.751, 3903.0022, 1873.444), (-9.846527892100111, 5.929470903539134, 88.6492980021665), (2.78125, 1.0, 2.09375), "PWM_Quarry_2x2x2_A14", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2700.7595, 654.715, 750.0), (0.0, -79.99999917458362, 0.0), (1.78125, 1.0, 1.5), "PWM_Quarry_2x2x2_A140_68", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4300.0, 1750.0, 750.0), (0.0, 0.0, -0.0), (1.6875, 0.71875, 0.6875), "PWM_Quarry_2x2x2_A141_77", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1450.2532, 3987.7942, 2044.089), (-9.828613369399152, 3.3010750513134135, 98.83637959539487), (2.78125, 1.53125, 2.09375), "PWM_Quarry_2x2x2_A15", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2310.178, 3914.5024, 1767.3457), (-71.42962701035981, -130.46398574778527, 142.1954848953645), (1.0, 2.5, 5.0625), "PWM_Quarry_2x2x2_A16", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1056.9211, 4184.593, 1997.7211), (5.0001350863693474, 15.003172417153486, 89.99988671517211), (2.4375, 1.0, 2.0), "PWM_Quarry_2x2x2_A17_118", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (550.0, 2550.0, 1550.0), (15.000084185840608, 179.99995901886524, 3.999999976777645e-06), (1.9375, 1.28125, 1.375), "PWM_Quarry_2x2x2_A2_14", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (123.060394, 4359.877, 1495.8838), (-11.249632681157767, -13.182493988602921, 86.38305371477091), (1.90625, 2.03125, 4.625), "PWM_Quarry_2x2x2_A20", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (293.96866, 4559.7124, 1107.0626), (5.000231510933961, 90.00008807197365, -19.999939770030714), (2.40625, 2.09375, 1.84375), "PWM_Quarry_2x2x2_A21_157", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (500.0, 4347.762, 971.71326), (2.110882905582273, -34.91647359300703, -0.4663696193789142), (1.4375, 2.5, 1.8125), "PWM_Quarry_2x2x2_A22_168", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (898.2963, 3637.059, 600.0), (0.0, 165.00004804796816, -0.0), (1.625, 1.25, 2.15625), "PWM_Quarry_2x2x2_A23_201", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2175.3333, 3763.9536, 648.72375), (-4.828919067498591, 99.94216463212668, 1.2974912813223538), (1.4375, 2.0625, 1.125), "PWM_Quarry_2x2x2_A24_210", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4231.641, 3997.2698, 1761.0558), (-58.138184404009785, -35.62610513814246, 117.23450607951612), (1.0, 1.0, 2.03125), "PWM_Quarry_2x2x2_A26_242", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (500.0, 3850.0, 1900.0), (0.0, 0.0, 5.000006435349079), (2.3125, 1.5625, 1.0), "PWM_Quarry_2x2x2_A29_272", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1350.0, 2700.0, 1850.0), (-15.000001241946444, 15.000050486804488, 1.1403490254292013e-07), (2.96875, 1.46875, 1.0), "PWM_Quarry_2x2x2_A3_26", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (400.0, 4347.762, 1671.7133), (9.961556998648348, -19.119566398491838, 0.07675604000087848), (0.96875, 2.5, 1.3125), "PWM_Quarry_2x2x2_A30", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (750.0, 4600.0, 1300.0), (-0.6009520148418067, -139.74445333387618, -7.0411373051786255), (1.625, 1.0, 1.25), "PWM_Quarry_2x2x2_A32", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (550.0, 4397.762, 1471.7133), (-9.961301761969533, 134.1192556555796, -179.92295619435086), (0.96875, 2.5, 1.0625), "PWM_Quarry_2x2x2_A33", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3100.0, 4050.0, 650.0), (-4.923858109772965, -10.037505561026443, 0.8703899096430127), (2.40625, 1.0, 1.53125), "PWM_Quarry_2x2x2_A34_288", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2445.452, 4000.0, 595.83246), (-4.923857963997129, 10.037486273235462, -90.87047257001117), (1.25, 0.9375, 1.34375), "PWM_Quarry_2x2x2_A35_300", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2050.0, 3850.0, 500.0), (-2.6494455437443784e-07, 24.999998016353274, -89.99999575998534), (1.875, 0.875, 1.53125), "PWM_Quarry_2x2x2_A36_303", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3000.0, 3900.0, 1400.0), (-3.404876554744746, 19.719804660790277, 9.40805779090585), (1.0, 1.90625, 1.0), "PWM_Quarry_2x2x2_A38_321", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1200.0, 4450.0, 450.0), (-5.297851370948308, 24.771529594172474, 91.71548242008338), (3.46875, 1.46875, 1.75), "PWM_Quarry_2x2x2_A39_330", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1500.0, 2500.0, 1600.0), (-15.000001241946444, 15.000050486804488, 1.1403490254292013e-07), (3.125, 1.625, 1.34375), "PWM_Quarry_2x2x2_A4_31", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4950.0, 2050.0, 1650.0), (-2.886077567653245e-07, -15.000059931660612, 20.000108582742286), (1.0, 2.25, 1.75), "PWM_Quarry_2x2x2_A44_656", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3767.6697, 3934.3528, 613.07336), (-9.999969892902588, -49.99941654291306, -3.0332025851576207e-05), (1.46875, 1.28125, 1.0), "PWM_Quarry_2x2x2_A45_370", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3189.6196, 3879.7642, 1073.0248), (-4.13284241023647, 0.07536998532111079, 9.960441665997989), (1.9375, 1.0, 1.65625), "PWM_Quarry_2x2x2_A46_376", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3400.0, 4120.8647, 1588.8536), (0.0, 0.0, 15.000481530659496), (1.71875, 1.65625, 1.0), "PWM_Quarry_2x2x2_A47_379", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1982.8989, 2746.9846, 850.0), (15.000004098872365, -159.9998570458971, 3.699662792800385e-05), (3.03125, 1.34375, 1.0), "PWM_Quarry_2x2x2_A5_37", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3408.6824, 3999.2405, 1100.0), (4.999999022662149, -10.000090778232467, 4.005053627977533e-06), (1.71875, 0.75, 1.21875), "PWM_Quarry_2x2x2_A54_428", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3717.2808, 3860.5615, 852.7532), (-4.923828247038998, -29.962648797710504, -0.8703612465786013), (1.84375, 1.0, 1.40625), "PWM_Quarry_2x2x2_A55_447", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3607.1816, 4036.877, 1615.0531), (0.0, 0.0, 15.000481530659496), (1.71875, 1.65625, 1.0), "PWM_Quarry_2x2x2_A56", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3797.837, 4254.1597, 1734.7463), (11.480816382308312, -9.520873852138172, 105.74658562602296), (1.0, 1.0, 2.9375), "PWM_Quarry_2x2x2_A57", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2236.8303, 2813.792, 951.704), (-3.008135675133081e-07, -30.000060584518675, 15.001107364255875), (1.0, 2.375, 1.0), "PWM_Quarry_2x2x2_A6_46", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3900.0, 3600.0, 900.0), (0.0, 45.00003936799035, -0.0), (1.3125, 2.1875, 1.0), "PWM_Quarry_2x2x2_A62_642", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4000.0, 4000.0, 1650.0), (0.0, 0.0, 10.00015864470678), (0.59375, 2.34375, 0.78125), "PWM_Quarry_2x2x2_A63_489", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3687.059, 3851.7036, 1100.0), (-9.999939708518289, -35.000057930375554, 2.2981305710591017e-05), (1.71875, 1.0, 1.0), "PWM_Quarry_2x2x2_A65_504", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3867.3647, 3817.1025, 1596.9844), (-9.846557394548517, -1.753845109602231, 10.152097264543517), (1.0, 2.125, 1.0), "PWM_Quarry_2x2x2_A66_510", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4049.2402, 3058.6829, 700.0), (2.527604984216908e-08, 10.001155917834847, -5.000000398578027), (1.78125, 3.3125, 1.9375), "PWM_Quarry_2x2x2_A67_519", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4201.7036, 3237.0588, 600.0), (0.0, 95.00016995804515, -0.0), (1.71875, 1.0, 1.0), "PWM_Quarry_2x2x2_A68_525", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3728.87, 3804.684, 1300.0), (-13.565794391358144, -50.76854848295046, 6.460782597461368), (1.875, 1.0, 1.0), "PWM_Quarry_2x2x2_A69_531", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1440.6207, 2831.4854, 1778.3364), (-4.847961076744044, 5.810653547040319, 78.66451697523622), (2.78125, 1.53125, 2.09375), "PWM_Quarry_2x2x2_A7_52", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4150.0, 2800.0, 550.0), (0.0, 0.0, -0.0), (1.21875, 2.0, 1.71875), "PWM_Quarry_2x2x2_A70_537", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4174.131, 2811.938, 930.4908), (0.43524701464368565, -175.01869093119578, 10.019701514139815), (0.9375, 1.71875, 1.0), "PWM_Quarry_2x2x2_A71_543", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4050.0, 2626.047, 752.27893), (5.000003483304445, 90.00002091997965, 9.018535562560427e-07), (1.0, 1.21875, 1.78125), "PWM_Quarry_2x2x2_A72_552", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4051.7036, 2887.0588, 1150.0), (9.961557917748399, 95.07690188414091, 0.8804772869897866), (1.71875, 1.0, 1.3125), "PWM_Quarry_2x2x2_A73", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4050.0, 3200.0, 1750.0), (0.0, 0.0, 10.000023180215065), (1.0, 2.78125, 1.46875), "PWM_Quarry_2x2x2_A74_564", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4650.0, 3650.0, 1800.0), (-9.846558056938012, 69.84888373837775, 1.753787222863612), (2.4375, 1.0, 1.0), "PWM_Quarry_2x2x2_A75_573", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4046.5928, 2850.0, 1624.1182), (-14.999938773183196, 8.000000709687928e-06, -3.0517581504810666e-05), (2.28125, 2.125, 1.5), "PWM_Quarry_2x2x2_A76_579", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4450.0, 2950.0, 1900.0), (10.116391016405634, -110.47137992269136, -1.9110110626566768), (2.09375, 1.0, 1.0), "PWM_Quarry_2x2x2_A77_586", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4350.0, 2700.0, 1800.0), (-69.55846756804489, -164.67010673593384, 147.3095670179407), (0.375, 2.40625, 1.09375), "PWM_Quarry_2x2x2_A78_594", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (635.2573, 3204.5642, 2009.8839), (4.944209396267398, -175.05746783838475, 91.29738371204961), (2.71875, 1.0, 2.34375), "PWM_Quarry_2x2x2_A8_58", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4850.0, 2700.0, 1800.0), (-76.69295915692408, -104.38744664993139, -82.30675818612156), (0.375, 2.40625, 1.09375), "PWM_Quarry_2x2x2_A80", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4520.22, 2476.1985, 1835.6327), (69.53351952312192, 92.08500348293728, 101.0088753227748), (1.0, 1.5625, 2.875), "PWM_Quarry_2x2x2_A81_612", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4000.0, 2300.0, 1900.0), (-1.6978875440051386e-07, -10.000060246933884, -74.99990640335753), (1.0, 1.0, 3.40625), "PWM_Quarry_2x2x2_A82_621", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3932.1394, 3688.3022, 1450.0), (0.0, 50.0000431017326, -0.0), (1.59375, 2.625, 1.5), "PWM_Quarry_2x2x2_A84", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4303.3496, 1353.9236, 1749.7332), (-2.5755615216834276, -14.785277083696844, 10.335858520971403), (1.0, 2.4375, 1.375), "PWM_Quarry_2x2x2_A85_662", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4000.0, 1600.0, 1800.0), (-72.0359835419642, -145.7334580616786, 127.05375974438492), (0.71875, 2.28125, 2.34375), "PWM_Quarry_2x2x2_A86_668", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4149.4414, 1535.5253, 1823.1711), (-76.36794118501108, -152.12256579304304, 114.30530477367466), (1.0, 3.21875, 1.59375), "PWM_Quarry_2x2x2_A87_674", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4015.7554, 1063.9534, 1711.2087), (34.12224582246449, -31.116025214807323, 10.13672627193417), (1.375, 2.3125, 1.4375), "PWM_Quarry_2x2x2_A88_686", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4909.6777, 2059.3484, 1417.1052), (6.27977144725847, -24.2475303057559, 13.65049073009574), (1.0, 2.3125, 1.0), "PWM_Quarry_2x2x2_A89_689", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (610.5874, 3601.6672, 2113.2385), (-84.88862634694435, 170.22019048679755, -165.3337515142497), (1.53125, 2.8125, 3.5625), "PWM_Quarry_2x2x2_A9_67", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3720.7761, 2302.949, 1595.3834), (-19.055938558184533, -35.21017381805299, 11.745836740264345), (1.0, 2.84375, 1.0), "PWM_Quarry_2x2x2_A90_698", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4300.0, 1250.0, 1450.0), (-4.853132671365295e-08, -24.998869959806953, 5.000227226142454), (1.0, 2.34375, 1.0), "PWM_Quarry_2x2x2_A91_707", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3997.0308, 3104.1062, 800.25745), (-3.4141836838825297, 14.606780818528295, 99.5253605061673), (2.25, 2.0, 2.0), "PWM_Quarry_2x2x2_A92_710", _folder)
if a: placed += 1
else: skipped += 1

# Batch 31: StaticMesh'PWM_Quarry_2x2x5_A' (3 instances)
_mesh_path = "/Game/Unshippable/Whitebox/Rocks/Meshes/PWM_Quarry_2x2x5_A"
_materials = ['/Game/Environments/ProcTexturing/ProcMaterial_Quarry_Atlas_2']
_folder = "Reconstruction/BD_BB_SnakingRiver_Urban/Meshes"
a = spawn_static_mesh(_mesh_path, _materials, (1083.4817, 2446.9846, 1254.4261), (-14.076081027016224, 10.646910975014451, -5.236236575081608), (3.65625, 1.71875, 1.21875), "PWM_Quarry_2x2x5_A_17", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2984.1047, 3632.658, 1000.19025), (-1.0905099971248445e-07, 155.0002735416432, -10.000029574349162), (1.0, 2.34375, 1.25), "PWM_Quarry_2x2x5_A2_136", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2600.0, 550.0, 1000.0), (0.0, 0.0, -0.0), (1.15625, 1.0, 1.21875), "PWM_Quarry_2x2x5_A3_50", _folder)
if a: placed += 1
else: skipped += 1

# Batch 32: StaticMesh'PWM_Quarry_2x2x5_B' (1 instances)
_mesh_path = "/Game/Unshippable/Whitebox/Rocks/Meshes/PWM_Quarry_2x2x5_B"
_materials = ['/Game/Environments/ProcTexturing/ProcMaterial_Quarry_Atlas_2']
_folder = "Reconstruction/BD_BB_SnakingRiver_Urban/Meshes"
a = spawn_static_mesh(_mesh_path, _materials, (2150.0, 700.0, 800.0), (0.0, 0.0, -0.0), (1.34375, 1.4375, 1.625), "PWM_Quarry_2x2x5_B3_53", _folder)
if a: placed += 1
else: skipped += 1

# Batch 33: StaticMesh'PWM_Quarry_4x4x4_A' (50 instances)
_mesh_path = "/Game/Unshippable/Whitebox/Rocks/Meshes/PWM_Quarry_4x4x4_A"
_materials = ['/Game/Environments/ProcTexturing/ProcMaterial_Quarry_Atlas_2']
_folder = "Reconstruction/BD_BB_SnakingRiver_Urban/Meshes"
a = spawn_static_mesh(_mesh_path, _materials, (800.0, 2550.0, 900.0), (-15.000001513189739, 0.0, -0.0), (1.5625, 0.71875, 0.46875), "PWM_Quarry_4x4x4_A_207", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2129.6125, 3983.9905, 1980.8354), (-9.942870406819925, 5.057170179470925, -1.3122864372667316), (2.03125, 2.0, 0.53125), "PWM_Quarry_4x4x4_A10", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (199.98718, 4950.0024, 339.34097), (0.0003560000174477822, -179.9992555094555, -84.99967263965598), (1.0, 1.0, 2.5), "PWM_Quarry_4x4x4_A11_121", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3088.9297, 3585.317, 856.7777), (3.4048553969642565, -19.71988238745039, -75.59126252513877), (1.0, 1.71875, 1.34375), "PWM_Quarry_4x4x4_A13_142", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1894.2979, 2778.9592, 1790.7928), (-19.99993989887621, 20.000091134442478, 2.687738881120575e-05), (1.78125, 1.0, 1.0625), "PWM_Quarry_4x4x4_A14", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (99.999985, 4326.4155, 715.9532), (4.1000001024620297e-05, 179.9999590188666, 89.99851213476958), (1.0, 0.5625, 1.28125), "PWM_Quarry_4x4x4_A15_186", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2387.1382, 3848.2822, 651.8417), (-4.530517712207495, 15.083824469356454, -2.117523137396574), (1.09375, 0.5, 0.90625), "PWM_Quarry_4x4x4_A16_204", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2236.7922, 2903.7522, 1502.8284), (-14.709171347134134, 15.511412212571587, -3.9888618404042253), (1.65625, 1.0, 0.90625), "PWM_Quarry_4x4x4_A17", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5100.0, 2250.0, 1800.0), (-1.292572633785681, -14.945556210036866, -74.83044107532548), (1.0, 1.0, 2.4375), "PWM_Quarry_4x4x4_A18_615", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4399.1304, 3670.16, 1862.5061), (51.17474407797022, -178.76474307910226, 90.02115199859885), (0.4375, 0.78125, 1.5625), "PWM_Quarry_4x4x4_A19_224", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1383.2446, 2598.484, 854.4895), (-15.000001433398735, 10.345424824778975, -2.664002016082348), (1.375, 1.0, 0.90625), "PWM_Quarry_4x4x4_A2_8", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3615.2537, 3865.1062, 900.0), (90.0, -6.2920781470117495, -66.29257285185533), (0.625, 1.21875, 0.71875), "PWM_Quarry_4x4x4_A25_364", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3980.857, 3517.5454, 724.19025), (-10.617491446408676, -56.211397018559516, 15.620647127704283), (1.40625, 1.0, 0.6875), "PWM_Quarry_4x4x4_A26_373", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3369.694, 3853.223, 1400.0), (84.99874221604917, 164.99961448291936, -179.99996801141984), (0.59375, 1.0, 1.46875), "PWM_Quarry_4x4x4_A27_382", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (780.619, 2645.6794, 1769.106), (-4.777007746571318, 2.5849279797684566, 140.11936066281078), (1.96875, 1.0, 1.0), "PWM_Quarry_4x4x4_A3_20", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3886.17, 3435.2842, 1150.0), (9.427607007128577, -151.01495371046678, -87.99721901897951), (0.9375, 1.03125, 1.59375), "PWM_Quarry_4x4x4_A34_501", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3785.5298, 3623.065, 1450.7596), (-9.923003204538102, -45.114159145174845, 0.880429903375582), (1.21875, 0.6875, 0.4375), "PWM_Quarry_4x4x4_A35_507", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4107.3896, 3010.6533, 1208.017), (4.596121642689418, 8.880400535690647, -79.6561777098868), (0.78125, 0.96875, 1.59375), "PWM_Quarry_4x4x4_A36_522", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3974.788, 2700.1665, 650.0), (-4.923827869173999, -29.129671423992974, -10.037507850749778), (1.0, 1.375, 0.8125), "PWM_Quarry_4x4x4_A37_534", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4000.0, 2673.7686, 828.32623), (0.0, 0.0, -10.000030597161448), (0.34375, 1.0, 0.46875), "PWM_Quarry_4x4x4_A38_558", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4250.0, 3100.0, 1800.0), (7.670575630224711e-09, -4.999999802855636, 10.000037894886074), (0.5, 2.125, 0.53125), "PWM_Quarry_4x4x4_A39_570", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1855.9196, 2392.5278, 1162.9409), (-14.999938468061112, 20.00009165764435, 2.6129527134538226e-05), (1.78125, 1.0, 1.0625), "PWM_Quarry_4x4x4_A4_34", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4000.0, 2450.0, 1900.0), (-79.99996873541822, -90.00007452785616, 80.00036632802968), (0.28125, 1.59375, 0.9375), "PWM_Quarry_4x4x4_A40_582", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4353.976, 1838.0255, 1851.6182), (75.38359136215342, 108.36832961551214, -136.44122251973778), (0.75, 1.0, 2.1875), "PWM_Quarry_4x4x4_A42_627", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3643.5168, 3031.4326, 1317.3071), (7.865131545811522, 126.78573691198643, 0.10402864661177261), (1.9375, 0.875, 1.09375), "PWM_Quarry_4x4x4_A43_11", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3850.0, 2150.0, 1900.0), (-79.56070717128938, -75.75498845776241, 55.531009356105294), (0.8125, 1.78125, 1.0), "PWM_Quarry_4x4x4_A44_665", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3342.2747, 1794.3756, 1785.1204), (74.99584260027144, 45.00058184269771, 1.7390252525903283e-05), (0.5, 1.0, 1.75), "PWM_Quarry_4x4x4_A45_683", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3953.6077, 881.3646, 1349.7096), (24.835720620889962, -41.83187955779427, -80.8311122026362), (0.4375, 0.71875, 1.75), "PWM_Quarry_4x4x4_A46_695", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1214.2675, 3153.567, 1989.835), (74.99924321653423, 0.00024338559385906285, -4.999756333081561), (0.5625, 1.5625, 1.78125), "PWM_Quarry_4x4x4_A5_55", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3697.3545, 542.73254, 1251.0187), (5.079480639786139, -39.36935494302266, -75.8639533250048), (0.34375, 1.0, 1.0), "PWM_Quarry_4x4x4_A53_818", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4098.2964, 1762.941, 600.0), (0.0, 15.000148960076068, -0.0), (1.21875, 0.5625, 0.5625), "PWM_Quarry_4x4x4_A54", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3661.7617, 1596.9465, 649.9999), (3.570145401214172e-06, -64.99996198686775, -89.9999401759623), (0.5625, 0.65625, 1.40625), "PWM_Quarry_4x4x4_A55_842", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2800.1902, 845.64105, 650.0006), (-6.078862197413419e-05, 5.000093194638864, -89.99936238523529), (0.4375, 0.59375, 1.28125), "PWM_Quarry_4x4x4_A56_863", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3949.308, 2593.507, 1243.3994), (-12.80172695911798, -27.604737644767116, 10.577153702262516), (0.25, 0.75, 0.53125), "PWM_Quarry_4x4x4_A57_875", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2923.7744, 1875.4081, 1633.8873), (-14.47738724202609, -43.96668030771933, 15.50651924071669), (1.0, 2.1875, 0.78125), "PWM_Quarry_4x4x4_A58_890", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3076.359, 2120.0117, 623.947), (-1.7079782683891396, -50.29845937542287, 19.930472028425697), (1.0, 2.6875, 1.15625), "PWM_Quarry_4x4x4_A59_908", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1769.7104, 3153.8232, 1834.911), (-9.942870406819925, 5.057170179470925, -1.3122864372667316), (1.09375, 1.25, 0.53125), "PWM_Quarry_4x4x4_A6_61", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2114.5137, 1338.8628, 1540.6309), (-4.208497645758347, -40.9213951603841, 24.66305090627242), (0.5625, 2.125, 1.0), "PWM_Quarry_4x4x4_A60_930", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2463.9133, 226.49622, 1106.04), (84.99959743864798, -30.00013772964667, -10.00009425238228), (1.0, 0.90625, 2.03125), "PWM_Quarry_4x4x4_A61_1008", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3766.6335, 1173.5092, 1724.6711), (84.65325860126538, 46.9573632784953, -8.90572584703236), (0.4375, 0.71875, 1.15625), "PWM_Quarry_4x4x4_A62", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3382.5923, 1339.5474, 1691.8536), (1.2925996084746394, -34.945367305391116, 14.8319478717391), (1.0, 1.4375, 0.53125), "PWM_Quarry_4x4x4_A63_970", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2976.7952, 1108.6826, 1649.2401), (4.981017829278257, -29.62149037723085, 8.68272226194474), (0.5, 0.96875, 0.34375), "PWM_Quarry_4x4x4_A64_979", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3350.0, 3150.0, 1000.0), (7.390260804425105e-06, 39.999987101852696, -89.99993770598522), (0.53125, 1.0, 2.46875), "PWM_Quarry_4x4x4_A65_14", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2761.6519, 2645.3262, 1058.683), (2.374171462174018e-07, -50.00000060698041, 10.000673206808251), (1.9375, 1.0, 0.9375), "PWM_Quarry_4x4x4_A66_23", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3150.0, 2500.0, 1350.0), (-4.999969179645097, -34.999999310033694, -1.1853674671627378e-08), (1.21875, 0.5, 0.8125), "PWM_Quarry_4x4x4_A67_32", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3600.0, 2500.0, 1700.0), (0.0, -35.00006033507422, 0.0), (1.5, 1.21875, 1.0), "PWM_Quarry_4x4x4_A68_41", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2350.0, 500.0, 1400.0), (0.0, 0.0, -20.000060948281234), (1.0, 1.0, 0.6875), "PWM_Quarry_4x4x4_A69_47", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2351.164, 2839.032, 977.6521), (5.084040086465475e-08, -44.99991088324929, 15.001286874278088), (1.0, 1.46875, 1.0), "PWM_Quarry_4x4x4_A7_78", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2643.9817, 3252.4219, 1651.2053), (-9.115357643919925, -65.82300135335436, 23.99437388375143), (0.84375, 1.1875, 0.53125), "PWM_Quarry_4x4x4_A8_93", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2800.0, 3897.2808, 1879.3492), (0.0, 0.0, 105.00001874691905), (1.0, 0.46875, 1.75), "PWM_Quarry_4x4x4_A9_111", _folder)
if a: placed += 1
else: skipped += 1

# Batch 34: StaticMesh'PWM_Quarry_8x8x8_A' (18 instances)
_mesh_path = "/Game/Unshippable/Whitebox/Rocks/Meshes/PWM_Quarry_8x8x8_A"
_materials = ['/Game/Environments/ProcTexturing/ProcMaterial_Quarry_Atlas_2']
_folder = "Reconstruction/BD_BB_SnakingRiver_Urban/Meshes"
a = spawn_static_mesh(_mesh_path, _materials, (600.0, 2500.0, 1250.0), (-15.810271174908987, -8.639618154983033, -5.117950239679797), (1.0, 0.375, 0.8125), "PWM_Quarry_8x8x8_A_2", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (250.0, 4448.094, 814.5603), (-6.111054403507258, -14.593935954407279, -3.5566710680867897), (0.28125, 0.90625, 0.34375), "PWM_Quarry_8x8x8_A10_177", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (512.84204, 4197.721, 2022.8291), (9.054616899868181, -85.73779473314757, 5.33707191515818), (0.65625, 1.28125, 0.6875), "PWM_Quarry_8x8x8_A11_195", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4500.0, 1600.0, 1700.0), (79.20459224929014, 78.07763942518025, 107.4030743681609), (0.25, 1.1875, 0.3125), "PWM_Quarry_8x8x8_A12_659", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3100.0, 4100.0, 500.0), (0.0, -10.000090733275822, 0.0), (0.5625, -0.3125, -0.40625), "PWM_Quarry_8x8x8_A13_291", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3200.0, 4000.0, 800.0), (-5.000000000253746, 0.0, -0.0), (0.65625, 0.15625, 0.375), "PWM_Quarry_8x8x8_A14_306", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (759.2354, 2870.2632, 1963.8701), (-7.56445310626095, 16.64185502989293, 166.18153876353838), (1.09375, 0.6875, 0.46875), "PWM_Quarry_8x8x8_A2_23", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4100.137, 3329.5103, 1608.682), (-15.65726065588159, 103.60589625289273, -110.41950601767658), (0.65625, 0.375, 0.625), "PWM_Quarry_8x8x8_A23_540", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4000.0, 2992.3525, 1292.2057), (-10.397033980206773, -9.102753957840877, 84.93568047995508), (0.3125, 0.40625, 0.75), "PWM_Quarry_8x8x8_A24_546", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4150.0, 3850.0, 1700.0), (0.0, 0.0, 10.00054971950808), (0.21875, 0.75, 0.21875), "PWM_Quarry_8x8x8_A25_561", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3528.3752, 1766.8164, 1837.6852), (2.6771955970902265e-07, -44.99994051026129, 15.000278287576357), (1.0, 1.0, 0.25), "PWM_Quarry_8x8x8_A26_677", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2344.4182, 1666.2716, 620.34753), (-0.870574845939689, -55.1127892800216, 19.928834656728682), (0.46875, 1.3125, 0.65625), "PWM_Quarry_8x8x8_A29_920", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2139.859, 2835.5066, 1787.4956), (-13.56570462541713, 25.7684905413751, 173.539576518868), (1.09375, 0.53125, 0.375), "PWM_Quarry_8x8x8_A3_40", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1926.498, 965.124, 1601.4229), (6.852756391824647e-06, -35.00006123461061, 19.999430469491433), (0.21875, 0.40625, 0.25), "PWM_Quarry_8x8x8_A30_936", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1233.1371, 3656.699, 2006.2825), (-9.942717326972247, 5.057200827508349, 88.68779831279257), (0.875, 0.3125, 0.6875), "PWM_Quarry_8x8x8_A4_71", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1577.1399, 3486.1772, 1954.5586), (-14.941468270445478, 5.175541801423266, -1.3377990366886292), (1.0, 0.5625, 0.28125), "PWM_Quarry_8x8x8_A5_84", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3000.0, 3949.94, 1719.756), (0.0, 0.0, 15.000073607810464), (0.5625, 0.90625, 0.25), "PWM_Quarry_8x8x8_A6_96", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1461.3541, 2783.8105, 1710.277), (-14.765866662665434, 10.345277330522558, 172.33601971852718), (0.6875, 0.53125, 0.375), "PWM_Quarry_8x8x8_A8", _folder)
if a: placed += 1
else: skipped += 1

# Batch 35: StaticMesh'PWM_Quarry_Floor_6x2x1_A' (2 instances)
_mesh_path = "/Game/Unshippable/Whitebox/Rocks/Meshes/PWM_Quarry_Floor_6x2x1_A"
_materials = ['/Game/Environments/ProcTexturing/ProcMaterial_Quarry_Atlas_4']
_folder = "Reconstruction/BD_BB_SnakingRiver_Urban/Meshes"
a = spawn_static_mesh(_mesh_path, _materials, (249.99982, 4226.416, 1015.95496), (-0.0006713867275324903, -104.99996276952491, -0.000335693374756094), (2.0, 1.65625, 4.0), "PWM_Quarry_Floor_6x2x1_A_171", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (149.99982, 4276.416, 1565.955), (-4.661742267651659, -87.41531098243446, -9.992675732370671), (2.0, 2.03125, 3.34375), "PWM_Quarry_Floor_6x2x1_A2", _folder)
if a: placed += 1
else: skipped += 1

# Batch 36: StaticMesh'PWM_Quarry_Floor_8x4x1_A' (1 instances)
_mesh_path = "/Game/Unshippable/Whitebox/Rocks/Meshes/PWM_Quarry_Floor_8x4x1_A"
_materials = ['/Game/Environments/ProcTexturing/ProcMaterial_Quarry_Atlas_6']
_folder = "Reconstruction/BD_BB_SnakingRiver_Urban/Meshes"
a = spawn_static_mesh(_mesh_path, _materials, (200.00003, 4453.0273, 551.6793), (0.0010550000839547216, 90.0001164945902, 0.00010100001877030561), (1.0, 0.40625, 1.5625), "PWM_Quarry_Floor_8x4x1_A_183", _folder)
if a: placed += 1
else: skipped += 1

# ======================================================================
# PHASE 2: ConstructionCatalog  (construction blocks)
# ======================================================================
unreal.log(f"[{BUBBLE_NAME}] Phase 2: Placing construction blocks...")

# Construction blocks use DecoVolume transforms (matched by Name)
_folder = "Reconstruction/BD_BB_SnakingRiver_Urban/Construction"

# Construction: BP_Archway_3m_A_2
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Advanced
#   Volume: EMorSimpleShape::Empty, BoxExtent: (100.0, 100.0, 100.0)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (3200.0, 50.0, 950.0), (0.0, 0.0, -0.0), (2.0000, 2.0000, 2.0000), "BP_Archway_3m_A_2", _folder)
if a: placed += 1
else: skipped += 1

# Construction: BP_Column_1x2m_A_Base_2
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Stone
#   Volume: EMorSimpleShape::Capsule, BoxExtent: (100.0, 100.0, 100.0)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (5100.0, 2250.0, 895.0), (0.0, 0.00019000000121563605, -0.0), (2.0000, 2.0000, 2.0000), "BP_Column_1x2m_A_Base_2", _folder)
if a: placed += 1
else: skipped += 1

# Construction: BP_Column_1x2m_A_Capital_2
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Stone
#   Volume: EMorSimpleShape::Capsule, BoxExtent: (100.0, 100.0, 100.0)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (5100.0, 2250.0, 1900.0), (0.0, 0.0, -0.0), (2.0000, 2.0000, 2.0000), "BP_Column_1x2m_A_Capital_2", _folder)
if a: placed += 1
else: skipped += 1

# Construction: BP_Column_1x2m_A_Shaft_2
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Stone
#   Volume: EMorSimpleShape::Capsule, BoxExtent: (100.0, 100.0, 100.0)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (5100.0, 2250.0, 1100.0), (0.0, 0.0, -0.0), (2.0000, 2.0000, 2.0000), "BP_Column_1x2m_A_Shaft_2", _folder)
if a: placed += 1
else: skipped += 1

# Construction: BP_Column_1x2m_A_Shaft2_5
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Stone
#   Volume: EMorSimpleShape::Capsule, BoxExtent: (100.0, 100.0, 100.0)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (5100.0, 2250.0, 1300.0), (0.0, 0.0, -0.0), (2.0000, 2.0000, 2.0000), "BP_Column_1x2m_A_Shaft2_5", _folder)
if a: placed += 1
else: skipped += 1

# Construction: BP_Column_1x2m_A_Shaft3
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Stone
#   Volume: EMorSimpleShape::Capsule, BoxExtent: (100.0, 100.0, 100.0)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (5100.0, 2250.0, 1500.0), (0.0, 0.0, -0.0), (2.0000, 2.0000, 2.0000), "BP_Column_1x2m_A_Shaft3", _folder)
if a: placed += 1
else: skipped += 1

# Construction: BP_Column_1x2m_A_Shaft4
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Stone
#   Volume: EMorSimpleShape::Capsule, BoxExtent: (100.0, 100.0, 100.0)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (5100.0, 2250.0, 1700.0), (0.0, 0.0, -0.0), (2.0000, 2.0000, 2.0000), "BP_Column_1x2m_A_Shaft4", _folder)
if a: placed += 1
else: skipped += 1

# Construction: BP_Suburb_Stairs_Trim_Pillar_B_Breakable35_35
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Stone
#   Volume: EMorSimpleShape::OrientedBox, BoxExtent: (45.4, 44.7, 86.0)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (1699.9368, 4399.9976, 950.7466), (0.0, 0.0, -0.0), (0.9081, 0.8947, 1.7195), "BP_Suburb_Stairs_Trim_Pillar_B_Breakable35_35", _folder)
if a: placed += 1
else: skipped += 1

# Construction: BP_Suburb_Stairs_Trim_Pillar_B_Breakable36
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Stone
#   Volume: EMorSimpleShape::OrientedBox, BoxExtent: (45.4, 44.7, 86.0)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (1699.9368, 3699.9976, 950.7466), (0.0, 0.0, -0.0), (0.9081, 0.8947, 1.7195), "BP_Suburb_Stairs_Trim_Pillar_B_Breakable36", _folder)
if a: placed += 1
else: skipped += 1

# Construction: BP_Suburb_Stairs_Trim_Pillar_B_Breakable37
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Stone
#   Volume: EMorSimpleShape::OrientedBox, BoxExtent: (45.4, 44.7, 86.0)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (1399.9368, 4399.9976, 950.7466), (0.0, 0.0, -0.0), (0.9081, 0.8947, 1.7195), "BP_Suburb_Stairs_Trim_Pillar_B_Breakable37", _folder)
if a: placed += 1
else: skipped += 1

# Construction: BP_Suburb_Stairs_Trim_Pillar_B_Breakable38
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Stone
#   Volume: EMorSimpleShape::OrientedBox, BoxExtent: (45.4, 44.7, 86.0)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (1399.9368, 3699.9976, 950.7466), (0.0, 0.0, -0.0), (0.9081, 0.8947, 1.7195), "BP_Suburb_Stairs_Trim_Pillar_B_Breakable38", _folder)
if a: placed += 1
else: skipped += 1

# Construction: BP_Suburbs_Balustrade_2m_A10
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Stone
#   Volume: EMorSimpleShape::OrientedBox, BoxExtent: (15.8, 100.0, 40.2)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (1399.6816, 4249.9004, 939.9383), (0.0, 0.0, -0.0), (0.3158, 2.0000, 0.8049), "BP_Suburbs_Balustrade_2m_A10", _folder)
if a: placed += 1
else: skipped += 1

# Construction: BP_Suburbs_Balustrade_2m_A2_8
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Stone
#   Volume: EMorSimpleShape::OrientedBox, BoxExtent: (15.8, 100.0, 40.2)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (1700.3184, 3850.0994, 939.9383), (0.0, 0.0, -0.0), (0.3158, 2.0000, 0.8049), "BP_Suburbs_Balustrade_2m_A2_8", _folder)
if a: placed += 1
else: skipped += 1

# Construction: BP_Suburbs_Balustrade_2m_A3
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Stone
#   Volume: EMorSimpleShape::OrientedBox, BoxExtent: (15.8, 100.0, 40.2)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (1700.3184, 4050.0994, 939.9383), (0.0, 0.0, -0.0), (0.3158, 2.0000, 0.8049), "BP_Suburbs_Balustrade_2m_A3", _folder)
if a: placed += 1
else: skipped += 1

# Construction: BP_Suburbs_Balustrade_2m_A4
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Stone
#   Volume: EMorSimpleShape::OrientedBox, BoxExtent: (15.8, 100.0, 40.2)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (1400.3184, 3850.0994, 939.9383), (0.0, 0.0, -0.0), (0.3158, 2.0000, 0.8049), "BP_Suburbs_Balustrade_2m_A4", _folder)
if a: placed += 1
else: skipped += 1

# Construction: BP_Suburbs_Balustrade_2m_A5
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Stone
#   Volume: EMorSimpleShape::OrientedBox, BoxExtent: (100.0, 15.8, 40.2)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (3400.0994, 5599.6816, 939.9383), (0.0, 0.0, -0.0), (2.0000, 0.3158, 0.8049), "BP_Suburbs_Balustrade_2m_A5", _folder)
if a: placed += 1
else: skipped += 1

# Construction: BP_Suburbs_Balustrade_2m_A6
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Stone
#   Volume: EMorSimpleShape::OrientedBox, BoxExtent: (100.0, 15.8, 40.2)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (3200.0994, 5599.6816, 939.9383), (0.0, 0.0, -0.0), (2.0000, 0.3158, 0.8049), "BP_Suburbs_Balustrade_2m_A6", _folder)
if a: placed += 1
else: skipped += 1

# Construction: BP_Suburbs_Balustrade_2m_A8
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Stone
#   Volume: EMorSimpleShape::OrientedBox, BoxExtent: (100.0, 15.8, 40.2)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (3000.0994, 5599.6816, 939.9383), (0.0, 0.0, -0.0), (2.0000, 0.3158, 0.8049), "BP_Suburbs_Balustrade_2m_A8", _folder)
if a: placed += 1
else: skipped += 1

# Construction: BP_Suburbs_Balustrade_2m_B2_17
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Stone
#   Volume: EMorSimpleShape::OrientedBox, BoxExtent: (15.8, 100.0, 40.2)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (1700.318, 4250.0996, 939.9383), (0.0, 0.0, -0.0), (0.3157, 2.0000, 0.8049), "BP_Suburbs_Balustrade_2m_B2_17", _folder)
if a: placed += 1
else: skipped += 1

# Construction: BP_Suburbs_Balustrade_2m_B8
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Stone
#   Volume: EMorSimpleShape::OrientedBox, BoxExtent: (15.8, 100.0, 40.2)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (1399.682, 4049.9004, 939.9383), (0.0, 0.0, -0.0), (0.3157, 2.0000, 0.8049), "BP_Suburbs_Balustrade_2m_B8", _folder)
if a: placed += 1
else: skipped += 1

# Construction: BP_Suburbs_Floor_A_8
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Stone
#   Volume: EMorSimpleShape::OrientedBox, BoxExtent: (151.0, 151.0, 25.9)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (1550.0, 3800.0, 875.0), (0.0, 0.0, -0.0), (3.0201, 3.0200, 0.5174), "BP_Suburbs_Floor_A_8", _folder)
if a: placed += 1
else: skipped += 1

# Construction: BP_Suburbs_Floor_A2
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Stone
#   Volume: EMorSimpleShape::OrientedBox, BoxExtent: (151.0, 151.0, 25.9)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (1550.0, 4300.0, 875.0), (0.0, 0.0, -0.0), (3.0201, 3.0200, 0.5174), "BP_Suburbs_Floor_A2", _folder)
if a: placed += 1
else: skipped += 1

# Construction: BP_Suburbs_Floor_A3
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Stone
#   Volume: EMorSimpleShape::OrientedBox, BoxExtent: (151.0, 99.7, 25.9)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (1550.0, 4050.0, 875.0), (0.0, 0.0, -0.0), (3.0201, 1.9932, 0.5174), "BP_Suburbs_Floor_A3", _folder)
if a: placed += 1
else: skipped += 1

# Construction: BP_Suburbs_Gate_Trim_A_3m2
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Stone
#   Volume: EMorSimpleShape::OrientedBox, BoxExtent: (150.2, 20.9, 75.0)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (1250.1654, 4379.227, 724.9881), (0.0, 0.0, -0.0), (3.0034, 0.4175, 1.5000), "BP_Suburbs_Gate_Trim_A_3m2", _folder)
if a: placed += 1
else: skipped += 1

# Construction: BP_Suburbs_Stairs_Small_C1_Breakable_5
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Advanced
#   Volume: EMorSimpleShape::OrientedBox, BoxExtent: (153.0, 76.8, 52.4)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (1548.9878, 3574.168, 850.4567), (0.0, 0.0, -0.0), (3.0603, 1.5355, 1.0486), "BP_Suburbs_Stairs_Small_C1_Breakable_5", _folder)
if a: placed += 1
else: skipped += 1

# Construction: BP_Suburbs_Stairs_Small_C1_Breakable2
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Advanced
#   Volume: EMorSimpleShape::OrientedBox, BoxExtent: (153.0, 76.8, 52.4)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (1551.0122, 4525.832, 850.4567), (0.0, 0.0, -0.0), (3.0603, 1.5355, 1.0486), "BP_Suburbs_Stairs_Small_C1_Breakable2", _folder)
if a: placed += 1
else: skipped += 1

# Construction: BP_Suburbs_Wall_Thick_1x3m_A_Breakable_2
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Advanced
#   Volume: EMorSimpleShape::OrientedBox, BoxExtent: (151.5, 50.0, 50.8)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (3350.0, 50.0, 1250.2108), (0.0, 0.0, -0.0), (3.0300, 1.0000, 1.0150), "BP_Suburbs_Wall_Thick_1x3m_A_Breakable_2", _folder)
if a: placed += 1
else: skipped += 1

# Construction: BP_Suburbs_Wall_Thick_1x3m_A_Breakable2
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Advanced
#   Volume: EMorSimpleShape::OrientedBox, BoxExtent: (151.5, 50.0, 50.8)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (3050.0, 50.0, 1250.2108), (0.0, 0.0, -0.0), (3.0300, 1.0000, 1.0150), "BP_Suburbs_Wall_Thick_1x3m_A_Breakable2", _folder)
if a: placed += 1
else: skipped += 1

# Construction: BP_Suburbs_Wall_Thick_1x3m_A_Breakable3_2
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Advanced
#   Volume: EMorSimpleShape::OrientedBox, BoxExtent: (50.0, 151.5, 50.8)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (6050.0, 5100.0, 750.2109), (0.0, 0.0, -0.0), (1.0000, 3.0300, 1.0150), "BP_Suburbs_Wall_Thick_1x3m_A_Breakable3_2", _folder)
if a: placed += 1
else: skipped += 1

# Construction: BP_Suburbs_Wall_Thick_1x3m_A_Breakable4
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Advanced
#   Volume: EMorSimpleShape::OrientedBox, BoxExtent: (50.0, 151.5, 50.8)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (6050.0, 4800.0, 750.2109), (0.0, 0.0, -0.0), (1.0000, 3.0300, 1.0150), "BP_Suburbs_Wall_Thick_1x3m_A_Breakable4", _folder)
if a: placed += 1
else: skipped += 1

# Construction: BP_Suburbs_Wall_Thick_3x3m_A_41
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Advanced
#   Volume: EMorSimpleShape::OrientedBox, BoxExtent: (151.5, 50.0, 150.8)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (1449.839, 5650.0, 950.75), (0.0, 0.0, -0.0), (3.0300, 1.0000, 3.0150), "BP_Suburbs_Wall_Thick_3x3m_A_41", _folder)
if a: placed += 1
else: skipped += 1

# Construction: BP_Suburbs_Wall_Thick_3x3m_A10
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Advanced
#   Volume: EMorSimpleShape::OrientedBox, BoxExtent: (151.5, 50.0, 150.8)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (1149.839, 5650.0, 2150.75), (0.0, 0.0, -0.0), (3.0300, 1.0000, 3.0150), "BP_Suburbs_Wall_Thick_3x3m_A10", _folder)
if a: placed += 1
else: skipped += 1

# Construction: BP_Suburbs_Wall_Thick_3x3m_A11
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Advanced
#   Volume: EMorSimpleShape::OrientedBox, BoxExtent: (151.5, 50.0, 150.8)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (1449.839, 5650.0, 2450.75), (0.0, 0.0, -0.0), (3.0300, 1.0000, 3.0150), "BP_Suburbs_Wall_Thick_3x3m_A11", _folder)
if a: placed += 1
else: skipped += 1

# Construction: BP_Suburbs_Wall_Thick_3x3m_A12
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Advanced
#   Volume: EMorSimpleShape::OrientedBox, BoxExtent: (151.5, 50.0, 150.8)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (1149.839, 5650.0, 2450.75), (0.0, 0.0, -0.0), (3.0300, 1.0000, 3.0150), "BP_Suburbs_Wall_Thick_3x3m_A12", _folder)
if a: placed += 1
else: skipped += 1

# Construction: BP_Suburbs_Wall_Thick_3x3m_A13_2
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Advanced
#   Volume: EMorSimpleShape::OrientedBox, BoxExtent: (50.0, 151.5, 150.8)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (5150.0, 2700.161, 950.75), (0.0, 0.0, -0.0), (1.0000, 3.0300, 3.0150), "BP_Suburbs_Wall_Thick_3x3m_A13_2", _folder)
if a: placed += 1
else: skipped += 1

# Construction: BP_Suburbs_Wall_Thick_3x3m_A14
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Advanced
#   Volume: EMorSimpleShape::OrientedBox, BoxExtent: (50.0, 151.5, 150.8)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (5150.0, 2400.161, 950.75), (0.0, 0.0, -0.0), (1.0000, 3.0300, 3.0150), "BP_Suburbs_Wall_Thick_3x3m_A14", _folder)
if a: placed += 1
else: skipped += 1

# Construction: BP_Suburbs_Wall_Thick_3x3m_A15
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Advanced
#   Volume: EMorSimpleShape::OrientedBox, BoxExtent: (50.0, 151.5, 150.8)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (5150.0, 2700.161, 1250.75), (0.0, 0.0, -0.0), (1.0000, 3.0300, 3.0150), "BP_Suburbs_Wall_Thick_3x3m_A15", _folder)
if a: placed += 1
else: skipped += 1

# Construction: BP_Suburbs_Wall_Thick_3x3m_A16
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Advanced
#   Volume: EMorSimpleShape::OrientedBox, BoxExtent: (50.0, 151.5, 150.8)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (5150.0, 2400.161, 1250.75), (0.0, 0.0, -0.0), (1.0000, 3.0300, 3.0150), "BP_Suburbs_Wall_Thick_3x3m_A16", _folder)
if a: placed += 1
else: skipped += 1

# Construction: BP_Suburbs_Wall_Thick_3x3m_A17
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Advanced
#   Volume: EMorSimpleShape::OrientedBox, BoxExtent: (50.0, 151.5, 150.8)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (5150.0, 2700.161, 1550.75), (0.0, 0.0, -0.0), (1.0000, 3.0300, 3.0150), "BP_Suburbs_Wall_Thick_3x3m_A17", _folder)
if a: placed += 1
else: skipped += 1

# Construction: BP_Suburbs_Wall_Thick_3x3m_A18
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Advanced
#   Volume: EMorSimpleShape::OrientedBox, BoxExtent: (50.0, 151.5, 150.8)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (5150.0, 2400.161, 1550.75), (0.0, 0.0, -0.0), (1.0000, 3.0300, 3.0150), "BP_Suburbs_Wall_Thick_3x3m_A18", _folder)
if a: placed += 1
else: skipped += 1

# Construction: BP_Suburbs_Wall_Thick_3x3m_A19
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Advanced
#   Volume: EMorSimpleShape::OrientedBox, BoxExtent: (50.0, 151.5, 150.8)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (5150.0, 2700.161, 1850.75), (0.0, 0.0, -0.0), (1.0000, 3.0300, 3.0150), "BP_Suburbs_Wall_Thick_3x3m_A19", _folder)
if a: placed += 1
else: skipped += 1

# Construction: BP_Suburbs_Wall_Thick_3x3m_A2
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Advanced
#   Volume: EMorSimpleShape::OrientedBox, BoxExtent: (151.5, 50.0, 150.8)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (1149.839, 5650.0, 950.75), (0.0, 0.0, -0.0), (3.0300, 1.0000, 3.0150), "BP_Suburbs_Wall_Thick_3x3m_A2", _folder)
if a: placed += 1
else: skipped += 1

# Construction: BP_Suburbs_Wall_Thick_3x3m_A20
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Advanced
#   Volume: EMorSimpleShape::OrientedBox, BoxExtent: (50.0, 151.5, 150.8)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (5150.0, 2400.161, 1850.75), (0.0, 0.0, -0.0), (1.0000, 3.0300, 3.0150), "BP_Suburbs_Wall_Thick_3x3m_A20", _folder)
if a: placed += 1
else: skipped += 1

# Construction: BP_Suburbs_Wall_Thick_3x3m_A21_12
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Advanced
#   Volume: EMorSimpleShape::OrientedBox, BoxExtent: (50.0, 151.5, 150.8)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (5750.0, 5899.839, 850.75), (0.0, 0.0, -0.0), (1.0000, 3.0300, 3.0150), "BP_Suburbs_Wall_Thick_3x3m_A21_12", _folder)
if a: placed += 1
else: skipped += 1

# Construction: BP_Suburbs_Wall_Thick_3x3m_A22
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Advanced
#   Volume: EMorSimpleShape::OrientedBox, BoxExtent: (50.0, 151.5, 150.8)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (5750.0, 5599.839, 850.75), (0.0, 0.0, -0.0), (1.0000, 3.0300, 3.0150), "BP_Suburbs_Wall_Thick_3x3m_A22", _folder)
if a: placed += 1
else: skipped += 1

# Construction: BP_Suburbs_Wall_Thick_3x3m_A23
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Advanced
#   Volume: EMorSimpleShape::OrientedBox, BoxExtent: (50.0, 151.5, 150.8)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (5750.0, 5299.839, 850.75), (0.0, 0.0, -0.0), (1.0000, 3.0300, 3.0150), "BP_Suburbs_Wall_Thick_3x3m_A23", _folder)
if a: placed += 1
else: skipped += 1

# Construction: BP_Suburbs_Wall_Thick_3x3m_A24
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Advanced
#   Volume: EMorSimpleShape::OrientedBox, BoxExtent: (50.0, 151.5, 150.8)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (5750.0, 5899.839, 1150.75), (0.0, 0.0, -0.0), (1.0000, 3.0300, 3.0150), "BP_Suburbs_Wall_Thick_3x3m_A24", _folder)
if a: placed += 1
else: skipped += 1

# Construction: BP_Suburbs_Wall_Thick_3x3m_A25
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Advanced
#   Volume: EMorSimpleShape::OrientedBox, BoxExtent: (50.0, 151.5, 150.8)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (5750.0, 5599.839, 1150.75), (0.0, 0.0, -0.0), (1.0000, 3.0300, 3.0150), "BP_Suburbs_Wall_Thick_3x3m_A25", _folder)
if a: placed += 1
else: skipped += 1

# Construction: BP_Suburbs_Wall_Thick_3x3m_A26
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Advanced
#   Volume: EMorSimpleShape::OrientedBox, BoxExtent: (50.0, 151.5, 150.8)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (5750.0, 5299.839, 1150.75), (0.0, 0.0, -0.0), (1.0000, 3.0300, 3.0150), "BP_Suburbs_Wall_Thick_3x3m_A26", _folder)
if a: placed += 1
else: skipped += 1

# Construction: BP_Suburbs_Wall_Thick_3x3m_A27
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Advanced
#   Volume: EMorSimpleShape::OrientedBox, BoxExtent: (50.0, 151.5, 150.8)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (5750.0, 5899.839, 1450.75), (0.0, 0.0, -0.0), (1.0000, 3.0300, 3.0150), "BP_Suburbs_Wall_Thick_3x3m_A27", _folder)
if a: placed += 1
else: skipped += 1

# Construction: BP_Suburbs_Wall_Thick_3x3m_A28
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Advanced
#   Volume: EMorSimpleShape::OrientedBox, BoxExtent: (50.0, 151.5, 150.8)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (5750.0, 5599.839, 1450.75), (0.0, 0.0, -0.0), (1.0000, 3.0300, 3.0150), "BP_Suburbs_Wall_Thick_3x3m_A28", _folder)
if a: placed += 1
else: skipped += 1

# Construction: BP_Suburbs_Wall_Thick_3x3m_A29
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Advanced
#   Volume: EMorSimpleShape::OrientedBox, BoxExtent: (50.0, 151.5, 150.8)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (5750.0, 5299.839, 1450.75), (0.0, 0.0, -0.0), (1.0000, 3.0300, 3.0150), "BP_Suburbs_Wall_Thick_3x3m_A29", _folder)
if a: placed += 1
else: skipped += 1

# Construction: BP_Suburbs_Wall_Thick_3x3m_A3
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Advanced
#   Volume: EMorSimpleShape::OrientedBox, BoxExtent: (151.5, 50.0, 150.8)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (1449.839, 5650.0, 1250.75), (0.0, 0.0, -0.0), (3.0300, 1.0000, 3.0150), "BP_Suburbs_Wall_Thick_3x3m_A3", _folder)
if a: placed += 1
else: skipped += 1

# Construction: BP_Suburbs_Wall_Thick_3x3m_A30
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Advanced
#   Volume: EMorSimpleShape::OrientedBox, BoxExtent: (50.0, 151.5, 150.8)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (5750.0, 5899.839, 1750.75), (0.0, 0.0, -0.0), (1.0000, 3.0300, 3.0150), "BP_Suburbs_Wall_Thick_3x3m_A30", _folder)
if a: placed += 1
else: skipped += 1

# Construction: BP_Suburbs_Wall_Thick_3x3m_A31
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Advanced
#   Volume: EMorSimpleShape::OrientedBox, BoxExtent: (50.0, 151.5, 150.8)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (5750.0, 5599.839, 1750.75), (0.0, 0.0, -0.0), (1.0000, 3.0300, 3.0150), "BP_Suburbs_Wall_Thick_3x3m_A31", _folder)
if a: placed += 1
else: skipped += 1

# Construction: BP_Suburbs_Wall_Thick_3x3m_A32
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Advanced
#   Volume: EMorSimpleShape::OrientedBox, BoxExtent: (50.0, 151.5, 150.8)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (5750.0, 5299.839, 1750.75), (0.0, 0.0, -0.0), (1.0000, 3.0300, 3.0150), "BP_Suburbs_Wall_Thick_3x3m_A32", _folder)
if a: placed += 1
else: skipped += 1

# Construction: BP_Suburbs_Wall_Thick_3x3m_A33
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Advanced
#   Volume: EMorSimpleShape::OrientedBox, BoxExtent: (50.0, 151.5, 150.8)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (5750.0, 5899.839, 2050.75), (0.0, 0.0, -0.0), (1.0000, 3.0300, 3.0150), "BP_Suburbs_Wall_Thick_3x3m_A33", _folder)
if a: placed += 1
else: skipped += 1

# Construction: BP_Suburbs_Wall_Thick_3x3m_A34
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Advanced
#   Volume: EMorSimpleShape::OrientedBox, BoxExtent: (50.0, 151.5, 150.8)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (5750.0, 5599.839, 2050.75), (0.0, 0.0, -0.0), (1.0000, 3.0300, 3.0150), "BP_Suburbs_Wall_Thick_3x3m_A34", _folder)
if a: placed += 1
else: skipped += 1

# Construction: BP_Suburbs_Wall_Thick_3x3m_A35
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Advanced
#   Volume: EMorSimpleShape::OrientedBox, BoxExtent: (50.0, 151.5, 150.8)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (5750.0, 5299.839, 2050.75), (0.0, 0.0, -0.0), (1.0000, 3.0300, 3.0150), "BP_Suburbs_Wall_Thick_3x3m_A35", _folder)
if a: placed += 1
else: skipped += 1

# Construction: BP_Suburbs_Wall_Thick_3x3m_A36
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Advanced
#   Volume: EMorSimpleShape::OrientedBox, BoxExtent: (50.0, 151.5, 150.8)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (5750.0, 5899.839, 2350.75), (0.0, 0.0, -0.0), (1.0000, 3.0300, 3.0150), "BP_Suburbs_Wall_Thick_3x3m_A36", _folder)
if a: placed += 1
else: skipped += 1

# Construction: BP_Suburbs_Wall_Thick_3x3m_A37
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Advanced
#   Volume: EMorSimpleShape::OrientedBox, BoxExtent: (50.0, 151.5, 150.8)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (5750.0, 5599.839, 2350.75), (0.0, 0.0, -0.0), (1.0000, 3.0300, 3.0150), "BP_Suburbs_Wall_Thick_3x3m_A37", _folder)
if a: placed += 1
else: skipped += 1

# Construction: BP_Suburbs_Wall_Thick_3x3m_A38
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Advanced
#   Volume: EMorSimpleShape::OrientedBox, BoxExtent: (50.0, 151.5, 150.8)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (5750.0, 5299.839, 2350.75), (0.0, 0.0, -0.0), (1.0000, 3.0300, 3.0150), "BP_Suburbs_Wall_Thick_3x3m_A38", _folder)
if a: placed += 1
else: skipped += 1

# Construction: BP_Suburbs_Wall_Thick_3x3m_A39
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Advanced
#   Volume: EMorSimpleShape::OrientedBox, BoxExtent: (50.0, 151.5, 150.8)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (6050.0, 4799.839, 1250.75), (0.0, 0.0, -0.0), (1.0000, 3.0300, 3.0150), "BP_Suburbs_Wall_Thick_3x3m_A39", _folder)
if a: placed += 1
else: skipped += 1

# Construction: BP_Suburbs_Wall_Thick_3x3m_A4
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Advanced
#   Volume: EMorSimpleShape::OrientedBox, BoxExtent: (151.5, 50.0, 150.8)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (1149.839, 5650.0, 1250.75), (0.0, 0.0, -0.0), (3.0300, 1.0000, 3.0150), "BP_Suburbs_Wall_Thick_3x3m_A4", _folder)
if a: placed += 1
else: skipped += 1

# Construction: BP_Suburbs_Wall_Thick_3x3m_A40
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Advanced
#   Volume: EMorSimpleShape::OrientedBox, BoxExtent: (50.0, 151.5, 150.8)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (6050.0, 4799.839, 1550.75), (0.0, 0.0, -0.0), (1.0000, 3.0300, 3.0150), "BP_Suburbs_Wall_Thick_3x3m_A40", _folder)
if a: placed += 1
else: skipped += 1

# Construction: BP_Suburbs_Wall_Thick_3x3m_A41
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Advanced
#   Volume: EMorSimpleShape::OrientedBox, BoxExtent: (50.0, 151.5, 150.8)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (6050.0, 4799.839, 1850.75), (0.0, 0.0, -0.0), (1.0000, 3.0300, 3.0150), "BP_Suburbs_Wall_Thick_3x3m_A41", _folder)
if a: placed += 1
else: skipped += 1

# Construction: BP_Suburbs_Wall_Thick_3x3m_A42
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Advanced
#   Volume: EMorSimpleShape::OrientedBox, BoxExtent: (50.0, 151.5, 150.8)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (6050.0, 4799.839, 2150.75), (0.0, 0.0, -0.0), (1.0000, 3.0300, 3.0150), "BP_Suburbs_Wall_Thick_3x3m_A42", _folder)
if a: placed += 1
else: skipped += 1

# Construction: BP_Suburbs_Wall_Thick_3x3m_A43
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Advanced
#   Volume: EMorSimpleShape::OrientedBox, BoxExtent: (50.0, 151.5, 150.8)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (6050.0, 4799.839, 2450.75), (0.0, 0.0, -0.0), (1.0000, 3.0300, 3.0150), "BP_Suburbs_Wall_Thick_3x3m_A43", _folder)
if a: placed += 1
else: skipped += 1

# Construction: BP_Suburbs_Wall_Thick_3x3m_A44
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Advanced
#   Volume: EMorSimpleShape::OrientedBox, BoxExtent: (50.0, 151.5, 150.8)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (6050.0, 4799.839, 950.75), (0.0, 0.0, -0.0), (1.0000, 3.0300, 3.0150), "BP_Suburbs_Wall_Thick_3x3m_A44", _folder)
if a: placed += 1
else: skipped += 1

# Construction: BP_Suburbs_Wall_Thick_3x3m_A45
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Advanced
#   Volume: EMorSimpleShape::OrientedBox, BoxExtent: (50.0, 151.5, 150.8)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (6050.0, 5099.839, 1250.75), (0.0, 0.0, -0.0), (1.0000, 3.0300, 3.0150), "BP_Suburbs_Wall_Thick_3x3m_A45", _folder)
if a: placed += 1
else: skipped += 1

# Construction: BP_Suburbs_Wall_Thick_3x3m_A46
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Advanced
#   Volume: EMorSimpleShape::OrientedBox, BoxExtent: (50.0, 151.5, 150.8)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (6050.0, 5099.839, 1550.75), (0.0, 0.0, -0.0), (1.0000, 3.0300, 3.0150), "BP_Suburbs_Wall_Thick_3x3m_A46", _folder)
if a: placed += 1
else: skipped += 1

# Construction: BP_Suburbs_Wall_Thick_3x3m_A47
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Advanced
#   Volume: EMorSimpleShape::OrientedBox, BoxExtent: (50.0, 151.5, 150.8)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (6050.0, 5099.839, 1850.75), (0.0, 0.0, -0.0), (1.0000, 3.0300, 3.0150), "BP_Suburbs_Wall_Thick_3x3m_A47", _folder)
if a: placed += 1
else: skipped += 1

# Construction: BP_Suburbs_Wall_Thick_3x3m_A48
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Advanced
#   Volume: EMorSimpleShape::OrientedBox, BoxExtent: (50.0, 151.5, 150.8)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (6050.0, 5099.839, 2150.75), (0.0, 0.0, -0.0), (1.0000, 3.0300, 3.0150), "BP_Suburbs_Wall_Thick_3x3m_A48", _folder)
if a: placed += 1
else: skipped += 1

# Construction: BP_Suburbs_Wall_Thick_3x3m_A49
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Advanced
#   Volume: EMorSimpleShape::OrientedBox, BoxExtent: (50.0, 151.5, 150.8)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (6050.0, 5099.839, 2450.75), (0.0, 0.0, -0.0), (1.0000, 3.0300, 3.0150), "BP_Suburbs_Wall_Thick_3x3m_A49", _folder)
if a: placed += 1
else: skipped += 1

# Construction: BP_Suburbs_Wall_Thick_3x3m_A5
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Advanced
#   Volume: EMorSimpleShape::OrientedBox, BoxExtent: (151.5, 50.0, 150.8)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (1449.839, 5650.0, 1550.75), (0.0, 0.0, -0.0), (3.0300, 1.0000, 3.0150), "BP_Suburbs_Wall_Thick_3x3m_A5", _folder)
if a: placed += 1
else: skipped += 1

# Construction: BP_Suburbs_Wall_Thick_3x3m_A50
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Advanced
#   Volume: EMorSimpleShape::OrientedBox, BoxExtent: (50.0, 151.5, 150.8)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (6050.0, 5099.839, 950.75), (0.0, 0.0, -0.0), (1.0000, 3.0300, 3.0150), "BP_Suburbs_Wall_Thick_3x3m_A50", _folder)
if a: placed += 1
else: skipped += 1

# Construction: BP_Suburbs_Wall_Thick_3x3m_A51
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Advanced
#   Volume: EMorSimpleShape::OrientedBox, BoxExtent: (151.5, 50.0, 150.8)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (5950.161, 5200.0, 1150.75), (0.0, 0.0, -0.0), (3.0300, 1.0000, 3.0150), "BP_Suburbs_Wall_Thick_3x3m_A51", _folder)
if a: placed += 1
else: skipped += 1

# Construction: BP_Suburbs_Wall_Thick_3x3m_A52
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Advanced
#   Volume: EMorSimpleShape::OrientedBox, BoxExtent: (151.5, 50.0, 150.8)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (5950.161, 5200.0, 1450.75), (0.0, 0.0, -0.0), (3.0300, 1.0000, 3.0150), "BP_Suburbs_Wall_Thick_3x3m_A52", _folder)
if a: placed += 1
else: skipped += 1

# Construction: BP_Suburbs_Wall_Thick_3x3m_A53
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Advanced
#   Volume: EMorSimpleShape::OrientedBox, BoxExtent: (151.5, 50.0, 150.8)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (5950.161, 5200.0, 1750.75), (0.0, 0.0, -0.0), (3.0300, 1.0000, 3.0150), "BP_Suburbs_Wall_Thick_3x3m_A53", _folder)
if a: placed += 1
else: skipped += 1

# Construction: BP_Suburbs_Wall_Thick_3x3m_A54
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Advanced
#   Volume: EMorSimpleShape::OrientedBox, BoxExtent: (151.5, 50.0, 150.8)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (5950.161, 5200.0, 2050.75), (0.0, 0.0, -0.0), (3.0300, 1.0000, 3.0150), "BP_Suburbs_Wall_Thick_3x3m_A54", _folder)
if a: placed += 1
else: skipped += 1

# Construction: BP_Suburbs_Wall_Thick_3x3m_A55
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Advanced
#   Volume: EMorSimpleShape::OrientedBox, BoxExtent: (151.5, 50.0, 150.8)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (5950.161, 5200.0, 2350.75), (0.0, 0.0, -0.0), (3.0300, 1.0000, 3.0150), "BP_Suburbs_Wall_Thick_3x3m_A55", _folder)
if a: placed += 1
else: skipped += 1

# Construction: BP_Suburbs_Wall_Thick_3x3m_A56
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Advanced
#   Volume: EMorSimpleShape::OrientedBox, BoxExtent: (151.5, 50.0, 150.8)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (5950.161, 5200.0, 850.75), (0.0, 0.0, -0.0), (3.0300, 1.0000, 3.0150), "BP_Suburbs_Wall_Thick_3x3m_A56", _folder)
if a: placed += 1
else: skipped += 1

# Construction: BP_Suburbs_Wall_Thick_3x3m_A57
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Advanced
#   Volume: EMorSimpleShape::OrientedBox, BoxExtent: (50.0, 151.5, 150.8)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (5750.0, 5899.839, 2650.75), (0.0, 0.0, -0.0), (1.0000, 3.0300, 3.0150), "BP_Suburbs_Wall_Thick_3x3m_A57", _folder)
if a: placed += 1
else: skipped += 1

# Construction: BP_Suburbs_Wall_Thick_3x3m_A58
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Advanced
#   Volume: EMorSimpleShape::OrientedBox, BoxExtent: (50.0, 151.5, 150.8)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (5750.0, 5599.839, 2650.75), (0.0, 0.0, -0.0), (1.0000, 3.0300, 3.0150), "BP_Suburbs_Wall_Thick_3x3m_A58", _folder)
if a: placed += 1
else: skipped += 1

# Construction: BP_Suburbs_Wall_Thick_3x3m_A59
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Advanced
#   Volume: EMorSimpleShape::OrientedBox, BoxExtent: (50.0, 151.5, 150.8)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (5750.0, 5299.839, 2650.75), (0.0, 0.0, -0.0), (1.0000, 3.0300, 3.0150), "BP_Suburbs_Wall_Thick_3x3m_A59", _folder)
if a: placed += 1
else: skipped += 1

# Construction: BP_Suburbs_Wall_Thick_3x3m_A6
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Advanced
#   Volume: EMorSimpleShape::OrientedBox, BoxExtent: (151.5, 50.0, 150.8)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (1149.839, 5650.0, 1550.75), (0.0, 0.0, -0.0), (3.0300, 1.0000, 3.0150), "BP_Suburbs_Wall_Thick_3x3m_A6", _folder)
if a: placed += 1
else: skipped += 1

# Construction: BP_Suburbs_Wall_Thick_3x3m_A60
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Advanced
#   Volume: EMorSimpleShape::OrientedBox, BoxExtent: (151.5, 50.0, 150.8)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (5950.161, 5200.0, 2650.75), (0.0, 0.0, -0.0), (3.0300, 1.0000, 3.0150), "BP_Suburbs_Wall_Thick_3x3m_A60", _folder)
if a: placed += 1
else: skipped += 1

# Construction: BP_Suburbs_Wall_Thick_3x3m_A61
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Advanced
#   Volume: EMorSimpleShape::OrientedBox, BoxExtent: (151.5, 50.0, 150.8)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (1449.839, 5650.0, 2750.75), (0.0, 0.0, -0.0), (3.0300, 1.0000, 3.0150), "BP_Suburbs_Wall_Thick_3x3m_A61", _folder)
if a: placed += 1
else: skipped += 1

# Construction: BP_Suburbs_Wall_Thick_3x3m_A62
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Advanced
#   Volume: EMorSimpleShape::OrientedBox, BoxExtent: (151.5, 50.0, 150.8)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (1149.839, 5650.0, 2750.75), (0.0, 0.0, -0.0), (3.0300, 1.0000, 3.0150), "BP_Suburbs_Wall_Thick_3x3m_A62", _folder)
if a: placed += 1
else: skipped += 1

# Construction: BP_Suburbs_Wall_Thick_3x3m_A7
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Advanced
#   Volume: EMorSimpleShape::OrientedBox, BoxExtent: (151.5, 50.0, 150.8)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (1449.839, 5650.0, 1850.75), (0.0, 0.0, -0.0), (3.0300, 1.0000, 3.0150), "BP_Suburbs_Wall_Thick_3x3m_A7", _folder)
if a: placed += 1
else: skipped += 1

# Construction: BP_Suburbs_Wall_Thick_3x3m_A8
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Advanced
#   Volume: EMorSimpleShape::OrientedBox, BoxExtent: (151.5, 50.0, 150.8)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (1149.839, 5650.0, 1850.75), (0.0, 0.0, -0.0), (3.0300, 1.0000, 3.0150), "BP_Suburbs_Wall_Thick_3x3m_A8", _folder)
if a: placed += 1
else: skipped += 1

# Construction: BP_Suburbs_Wall_Thick_3x3m_A9
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Advanced
#   Volume: EMorSimpleShape::OrientedBox, BoxExtent: (151.5, 50.0, 150.8)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (1449.839, 5650.0, 2150.75), (0.0, 0.0, -0.0), (3.0300, 1.0000, 3.0150), "BP_Suburbs_Wall_Thick_3x3m_A9", _folder)
if a: placed += 1
else: skipped += 1

# Construction: BP_Suburbs_Wall_Thin_1x1m_A_2
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Advanced
#   Volume: EMorSimpleShape::Empty, BoxExtent: (100.0, 100.0, 100.0)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (3000.0, 50.0, 1155.0), (0.0, 0.0, -0.0), (2.0000, 2.0000, 2.0000), "BP_Suburbs_Wall_Thin_1x1m_A_2", _folder)
if a: placed += 1
else: skipped += 1

# Construction: BP_Suburbs_Wall_Thin_1x1m_A2
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Advanced
#   Volume: EMorSimpleShape::Empty, BoxExtent: (100.0, 100.0, 100.0)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (3400.0, 50.0, 1155.0), (0.0, 0.0, -0.0), (2.0000, 2.0000, 2.0000), "BP_Suburbs_Wall_Thin_1x1m_A2", _folder)
if a: placed += 1
else: skipped += 1

# Construction: BP_Suburbs_Wall_Thin_1x1m_B_2
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Stone
#   Volume: EMorSimpleShape::OrientedBox, BoxExtent: (32.0, 50.0, 50.3)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (1392.9781, 3700.0244, 850.2746), (0.0, 0.0, -0.0), (0.6404, 1.0005, 1.0055), "BP_Suburbs_Wall_Thin_1x1m_B_2", _folder)
if a: placed += 1
else: skipped += 1

# Construction: BP_Suburbs_Wall_Thin_1x1m_B2
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Stone
#   Volume: EMorSimpleShape::OrientedBox, BoxExtent: (32.0, 50.0, 50.3)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (1392.9783, 4400.0244, 850.2746), (0.0, 0.0, -0.0), (0.6404, 1.0005, 1.0055), "BP_Suburbs_Wall_Thin_1x1m_B2", _folder)
if a: placed += 1
else: skipped += 1

# Construction: BP_Suburbs_Wall_Thin_1x1m_B3
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Stone
#   Volume: EMorSimpleShape::OrientedBox, BoxExtent: (32.0, 50.0, 50.3)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (1707.0219, 3699.9756, 850.2746), (0.0, 0.0, -0.0), (0.6404, 1.0005, 1.0055), "BP_Suburbs_Wall_Thin_1x1m_B3", _folder)
if a: placed += 1
else: skipped += 1

# Construction: BP_Suburbs_Wall_Thin_1x1m_B4
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Stone
#   Volume: EMorSimpleShape::OrientedBox, BoxExtent: (32.0, 50.0, 50.3)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (1707.0219, 4399.9756, 850.2746), (0.0, 0.0, -0.0), (0.6404, 1.0005, 1.0055), "BP_Suburbs_Wall_Thin_1x1m_B4", _folder)
if a: placed += 1
else: skipped += 1

# Construction: BP_Suburbs_Wall_Thin_1x3m_G10
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Stone
#   Volume: EMorSimpleShape::OrientedBox, BoxExtent: (150.0, 32.0, 50.0)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (3049.9717, 5593.001, 850.49506), (0.0, 0.0, -0.0), (3.0006, 0.6400, 1.0000), "BP_Suburbs_Wall_Thin_1x3m_G10", _folder)
if a: placed += 1
else: skipped += 1

# Construction: BP_Suburbs_Wall_Thin_1x3m_G3
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Stone
#   Volume: EMorSimpleShape::OrientedBox, BoxExtent: (32.0, 150.0, 50.0)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (1706.9993, 4199.9717, 850.49506), (0.0, 0.0, -0.0), (0.6400, 3.0006, 1.0000), "BP_Suburbs_Wall_Thin_1x3m_G3", _folder)
if a: placed += 1
else: skipped += 1

# Construction: BP_Suburbs_Wall_Thin_1x3m_G4
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Stone
#   Volume: EMorSimpleShape::OrientedBox, BoxExtent: (32.0, 150.0, 50.0)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (1393.0007, 4200.0283, 850.49506), (0.0, 0.0, -0.0), (0.6400, 3.0006, 1.0000), "BP_Suburbs_Wall_Thin_1x3m_G4", _folder)
if a: placed += 1
else: skipped += 1

# Construction: BP_Suburbs_Wall_Thin_1x3m_G5_2
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Stone
#   Volume: EMorSimpleShape::OrientedBox, BoxExtent: (32.0, 150.0, 50.0)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (1393.0007, 3900.0283, 850.49506), (0.0, 0.0, -0.0), (0.6400, 3.0006, 1.0000), "BP_Suburbs_Wall_Thin_1x3m_G5_2", _folder)
if a: placed += 1
else: skipped += 1

# Construction: BP_Suburbs_Wall_Thin_1x3m_G6
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Stone
#   Volume: EMorSimpleShape::OrientedBox, BoxExtent: (32.0, 150.0, 50.0)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (1706.9993, 3899.9717, 850.49506), (0.0, 0.0, -0.0), (0.6400, 3.0006, 1.0000), "BP_Suburbs_Wall_Thin_1x3m_G6", _folder)
if a: placed += 1
else: skipped += 1

# Construction: BP_Suburbs_Wall_Thin_1x3m_G7
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Stone
#   Volume: EMorSimpleShape::OrientedBox, BoxExtent: (150.0, 32.0, 50.0)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (3349.9717, 5593.001, 850.49506), (0.0, 0.0, -0.0), (3.0006, 0.6400, 1.0000), "BP_Suburbs_Wall_Thin_1x3m_G7", _folder)
if a: placed += 1
else: skipped += 1

# Construction: BP_Suburbs_Wall_Thin_1x3m_H_2
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Advanced
#   Volume: EMorSimpleShape::OrientedBox, BoxExtent: (150.0, 42.7, 52.0)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (3199.9717, 67.6544, 1148.2305), (0.0, 0.0, -0.0), (3.0006, 0.8531, 1.0400), "BP_Suburbs_Wall_Thin_1x3m_H_2", _folder)
if a: placed += 1
else: skipped += 1

# Construction: BP_Suburbs_Wall_Thin_3x15m_B_Breakable_2
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Stone
#   Volume: EMorSimpleShape::OrientedBox, BoxExtent: (26.9, 40.7, 174.7)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (3049.6887, 65.33481, 974.7254), (0.0, 0.0, -0.0), (0.5380, 0.8150, 3.4945), "BP_Suburbs_Wall_Thin_3x15m_B_Breakable_2", _folder)
if a: placed += 1
else: skipped += 1

# Construction: BP_Suburbs_Wall_Thin_3x15m_B_Breakable2
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Stone
#   Volume: EMorSimpleShape::OrientedBox, BoxExtent: (26.9, 40.7, 174.7)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (2999.6887, 65.33481, 974.7254), (0.0, 0.0, -0.0), (0.5380, 0.8150, 3.4945), "BP_Suburbs_Wall_Thin_3x15m_B_Breakable2", _folder)
if a: placed += 1
else: skipped += 1

# Construction: BP_Suburbs_Wall_Thin_3x15m_B_Breakable3
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Stone
#   Volume: EMorSimpleShape::OrientedBox, BoxExtent: (26.9, 40.7, 174.7)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (3350.3113, 65.33481, 974.7254), (0.0, 0.0, -0.0), (0.5380, 0.8150, 3.4945), "BP_Suburbs_Wall_Thin_3x15m_B_Breakable3", _folder)
if a: placed += 1
else: skipped += 1

# Construction: BP_Suburbs_Wall_Thin_3x15m_B_Breakable4
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Stone
#   Volume: EMorSimpleShape::OrientedBox, BoxExtent: (26.9, 40.7, 174.7)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (3400.3113, 65.33481, 974.7254), (0.0, 0.0, -0.0), (0.5380, 0.8150, 3.4945), "BP_Suburbs_Wall_Thin_3x15m_B_Breakable4", _folder)
if a: placed += 1
else: skipped += 1

# Construction: BP_Suburbs_Wall_Thin_Arch_Half_C_2
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Advanced
#   Volume: EMorSimpleShape::OrientedBox, BoxExtent: (50.0, 25.0, 149.8)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (1550.0, 5600.0, 950.2022), (0.0, 0.0, -0.0), (1.0000, 0.5000, 2.9964), "BP_Suburbs_Wall_Thin_Arch_Half_C_2", _folder)
if a: placed += 1
else: skipped += 1

# Construction: BP_Suburbs_Wall_Thin_Arch_Half_C10
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Advanced
#   Volume: EMorSimpleShape::OrientedBox, BoxExtent: (50.0, 25.0, 149.8)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (2950.0, 5600.0, 350.2022), (0.0, 0.0, -0.0), (1.0000, 0.5000, 2.9964), "BP_Suburbs_Wall_Thin_Arch_Half_C10", _folder)
if a: placed += 1
else: skipped += 1

# Construction: BP_Suburbs_Wall_Thin_Arch_Half_C11
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Advanced
#   Volume: EMorSimpleShape::OrientedBox, BoxExtent: (25.0, 50.0, 149.8)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (1700.0, 4400.0, 350.2022), (0.0, 0.0, -0.0), (0.5000, 1.0000, 2.9964), "BP_Suburbs_Wall_Thin_Arch_Half_C11", _folder)
if a: placed += 1
else: skipped += 1

# Construction: BP_Suburbs_Wall_Thin_Arch_Half_C12
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Advanced
#   Volume: EMorSimpleShape::OrientedBox, BoxExtent: (25.0, 50.0, 149.8)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (1400.0, 4400.0, 350.2022), (0.0, 0.0, -0.0), (0.5000, 1.0000, 2.9964), "BP_Suburbs_Wall_Thin_Arch_Half_C12", _folder)
if a: placed += 1
else: skipped += 1

# Construction: BP_Suburbs_Wall_Thin_Arch_Half_C13
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Advanced
#   Volume: EMorSimpleShape::OrientedBox, BoxExtent: (25.0, 50.0, 149.8)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (1400.0, 3700.0, 350.2022), (0.0, 0.0, -0.0), (0.5000, 1.0000, 2.9964), "BP_Suburbs_Wall_Thin_Arch_Half_C13", _folder)
if a: placed += 1
else: skipped += 1

# Construction: BP_Suburbs_Wall_Thin_Arch_Half_C14
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Advanced
#   Volume: EMorSimpleShape::OrientedBox, BoxExtent: (25.0, 50.0, 149.8)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (1700.0, 3700.0, 350.2022), (0.0, 0.0, -0.0), (0.5000, 1.0000, 2.9964), "BP_Suburbs_Wall_Thin_Arch_Half_C14", _folder)
if a: placed += 1
else: skipped += 1

# Construction: BP_Suburbs_Wall_Thin_Arch_Half_C15
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Advanced
#   Volume: EMorSimpleShape::OrientedBox, BoxExtent: (25.0, 50.0, 149.8)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (5700.0, 5200.0, 2650.2021), (0.0, 0.0, -0.0), (0.5000, 1.0000, 2.9964), "BP_Suburbs_Wall_Thin_Arch_Half_C15", _folder)
if a: placed += 1
else: skipped += 1

# Construction: BP_Suburbs_Wall_Thin_Arch_Half_C16
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Advanced
#   Volume: EMorSimpleShape::OrientedBox, BoxExtent: (50.0, 25.0, 149.8)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (5750.0, 5150.0, 2650.2021), (0.0, 0.0, -0.0), (1.0000, 0.5000, 2.9964), "BP_Suburbs_Wall_Thin_Arch_Half_C16", _folder)
if a: placed += 1
else: skipped += 1

# Construction: BP_Suburbs_Wall_Thin_Arch_Half_C17
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Advanced
#   Volume: EMorSimpleShape::OrientedBox, BoxExtent: (50.0, 25.0, 149.8)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (1550.0, 5600.0, 2750.2021), (0.0, 0.0, -0.0), (1.0000, 0.5000, 2.9964), "BP_Suburbs_Wall_Thin_Arch_Half_C17", _folder)
if a: placed += 1
else: skipped += 1

# Construction: BP_Suburbs_Wall_Thin_Arch_Half_C2
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Advanced
#   Volume: EMorSimpleShape::OrientedBox, BoxExtent: (50.0, 25.0, 149.8)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (1550.0, 5600.0, 1850.2023), (0.0, 0.0, -0.0), (1.0000, 0.5000, 2.9964), "BP_Suburbs_Wall_Thin_Arch_Half_C2", _folder)
if a: placed += 1
else: skipped += 1

# Construction: BP_Suburbs_Wall_Thin_Arch_Half_C3
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Advanced
#   Volume: EMorSimpleShape::OrientedBox, BoxExtent: (25.0, 50.0, 149.8)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (5700.0, 5200.0, 850.2022), (0.0, 0.0, -0.0), (0.5000, 1.0000, 2.9964), "BP_Suburbs_Wall_Thin_Arch_Half_C3", _folder)
if a: placed += 1
else: skipped += 1

# Construction: BP_Suburbs_Wall_Thin_Arch_Half_C4
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Advanced
#   Volume: EMorSimpleShape::OrientedBox, BoxExtent: (25.0, 50.0, 149.8)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (5700.0, 5200.0, 1750.2023), (0.0, 0.0, -0.0), (0.5000, 1.0000, 2.9964), "BP_Suburbs_Wall_Thin_Arch_Half_C4", _folder)
if a: placed += 1
else: skipped += 1

# Construction: BP_Suburbs_Wall_Thin_Arch_Half_C5_6
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Advanced
#   Volume: EMorSimpleShape::OrientedBox, BoxExtent: (50.0, 25.0, 149.8)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (5750.0, 5150.0, 850.2022), (0.0, 0.0, -0.0), (1.0000, 0.5000, 2.9964), "BP_Suburbs_Wall_Thin_Arch_Half_C5_6", _folder)
if a: placed += 1
else: skipped += 1

# Construction: BP_Suburbs_Wall_Thin_Arch_Half_C6_7
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Advanced
#   Volume: EMorSimpleShape::OrientedBox, BoxExtent: (50.0, 25.0, 149.8)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (5750.0, 5150.0, 1750.2023), (0.0, 0.0, -0.0), (1.0000, 0.5000, 2.9964), "BP_Suburbs_Wall_Thin_Arch_Half_C6_7", _folder)
if a: placed += 1
else: skipped += 1

# Construction: BP_Suburbs_Wall_Thin_Arch_Half_C7
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Advanced
#   Volume: EMorSimpleShape::OrientedBox, BoxExtent: (25.0, 50.0, 149.8)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (6000.0, 4700.0, 850.2022), (0.0, 0.0, -0.0), (0.5000, 1.0000, 2.9964), "BP_Suburbs_Wall_Thin_Arch_Half_C7", _folder)
if a: placed += 1
else: skipped += 1

# Construction: BP_Suburbs_Wall_Thin_Arch_Half_C8
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Advanced
#   Volume: EMorSimpleShape::OrientedBox, BoxExtent: (25.0, 50.0, 149.8)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (6000.0, 4700.0, 1750.2023), (0.0, 0.0, -0.0), (0.5000, 1.0000, 2.9964), "BP_Suburbs_Wall_Thin_Arch_Half_C8", _folder)
if a: placed += 1
else: skipped += 1

# Construction: BP_Suburbs_Wall_Thin_Arch_Half_C9
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Advanced
#   Volume: EMorSimpleShape::OrientedBox, BoxExtent: (50.0, 25.0, 149.8)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (3450.0, 5600.0, 350.2022), (0.0, 0.0, -0.0), (1.0000, 0.5000, 2.9964), "BP_Suburbs_Wall_Thin_Arch_Half_C9", _folder)
if a: placed += 1
else: skipped += 1

# Construction: BP_Suburbs_Wall_Thin_Arch_Half_D_2
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Advanced
#   Volume: EMorSimpleShape::OrientedBox, BoxExtent: (25.2, 150.0, 149.7)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (1699.7856, 3800.0, 649.6787), (0.0, 0.0, -0.0), (0.5043, 3.0000, 2.9936), "BP_Suburbs_Wall_Thin_Arch_Half_D_2", _folder)
if a: placed += 1
else: skipped += 1

# Construction: BP_Suburbs_Wall_Thin_Arch_Half_D10
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Advanced
#   Volume: EMorSimpleShape::OrientedBox, BoxExtent: (25.2, 150.0, 149.7)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (5699.7856, 5300.0, 1149.6787), (0.0, 0.0, -0.0), (0.5043, 3.0000, 2.9936), "BP_Suburbs_Wall_Thin_Arch_Half_D10", _folder)
if a: placed += 1
else: skipped += 1

# Construction: BP_Suburbs_Wall_Thin_Arch_Half_D11
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Advanced
#   Volume: EMorSimpleShape::OrientedBox, BoxExtent: (25.2, 150.0, 149.7)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (5700.2144, 5300.0, 1450.3214), (0.0, 0.0, -0.0), (0.5043, 3.0000, 2.9936), "BP_Suburbs_Wall_Thin_Arch_Half_D11", _folder)
if a: placed += 1
else: skipped += 1

# Construction: BP_Suburbs_Wall_Thin_Arch_Half_D12
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Advanced
#   Volume: EMorSimpleShape::OrientedBox, BoxExtent: (150.0, 25.2, 149.7)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (3050.0, 5600.2144, 649.6787), (0.0, 0.0, -0.0), (3.0000, 0.5043, 2.9936), "BP_Suburbs_Wall_Thin_Arch_Half_D12", _folder)
if a: placed += 1
else: skipped += 1

# Construction: BP_Suburbs_Wall_Thin_Arch_Half_D13
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Advanced
#   Volume: EMorSimpleShape::OrientedBox, BoxExtent: (25.2, 150.0, 149.7)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (5699.7856, 5300.0, 2049.6787), (0.0, 0.0, -0.0), (0.5043, 3.0000, 2.9936), "BP_Suburbs_Wall_Thin_Arch_Half_D13", _folder)
if a: placed += 1
else: skipped += 1

# Construction: BP_Suburbs_Wall_Thin_Arch_Half_D14
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Advanced
#   Volume: EMorSimpleShape::OrientedBox, BoxExtent: (25.2, 150.0, 149.7)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (5700.2144, 5300.0, 2350.3215), (0.0, 0.0, -0.0), (0.5043, 3.0000, 2.9936), "BP_Suburbs_Wall_Thin_Arch_Half_D14", _folder)
if a: placed += 1
else: skipped += 1

# Construction: BP_Suburbs_Wall_Thin_Arch_Half_D15
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Advanced
#   Volume: EMorSimpleShape::OrientedBox, BoxExtent: (150.0, 25.2, 149.7)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (5850.0, 5150.2144, 1149.6787), (0.0, 0.0, -0.0), (3.0000, 0.5043, 2.9936), "BP_Suburbs_Wall_Thin_Arch_Half_D15", _folder)
if a: placed += 1
else: skipped += 1

# Construction: BP_Suburbs_Wall_Thin_Arch_Half_D16
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Advanced
#   Volume: EMorSimpleShape::OrientedBox, BoxExtent: (150.0, 25.2, 149.7)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (5850.0, 5149.7856, 1450.3213), (0.0, 0.0, -0.0), (3.0000, 0.5043, 2.9936), "BP_Suburbs_Wall_Thin_Arch_Half_D16", _folder)
if a: placed += 1
else: skipped += 1

# Construction: BP_Suburbs_Wall_Thin_Arch_Half_D17
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Advanced
#   Volume: EMorSimpleShape::OrientedBox, BoxExtent: (150.0, 25.2, 149.7)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (5850.0, 5150.2144, 2049.6787), (0.0, 0.0, -0.0), (3.0000, 0.5043, 2.9936), "BP_Suburbs_Wall_Thin_Arch_Half_D17", _folder)
if a: placed += 1
else: skipped += 1

# Construction: BP_Suburbs_Wall_Thin_Arch_Half_D18
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Advanced
#   Volume: EMorSimpleShape::OrientedBox, BoxExtent: (150.0, 25.2, 149.7)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (5850.0, 5149.7856, 2350.3213), (0.0, 0.0, -0.0), (3.0000, 0.5043, 2.9936), "BP_Suburbs_Wall_Thin_Arch_Half_D18", _folder)
if a: placed += 1
else: skipped += 1

# Construction: BP_Suburbs_Wall_Thin_Arch_Half_D19
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Advanced
#   Volume: EMorSimpleShape::OrientedBox, BoxExtent: (25.2, 150.0, 149.7)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (5999.7856, 4800.0, 1149.6787), (0.0, 0.0, -0.0), (0.5043, 3.0000, 2.9936), "BP_Suburbs_Wall_Thin_Arch_Half_D19", _folder)
if a: placed += 1
else: skipped += 1

# Construction: BP_Suburbs_Wall_Thin_Arch_Half_D2
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Advanced
#   Volume: EMorSimpleShape::OrientedBox, BoxExtent: (25.2, 150.0, 149.7)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (1399.7856, 3800.0, 649.6787), (0.0, 0.0, -0.0), (0.5043, 3.0000, 2.9936), "BP_Suburbs_Wall_Thin_Arch_Half_D2", _folder)
if a: placed += 1
else: skipped += 1

# Construction: BP_Suburbs_Wall_Thin_Arch_Half_D20
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Advanced
#   Volume: EMorSimpleShape::OrientedBox, BoxExtent: (25.2, 150.0, 149.7)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (6000.2144, 4800.0, 1450.3214), (0.0, 0.0, -0.0), (0.5043, 3.0000, 2.9936), "BP_Suburbs_Wall_Thin_Arch_Half_D20", _folder)
if a: placed += 1
else: skipped += 1

# Construction: BP_Suburbs_Wall_Thin_Arch_Half_D21
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Advanced
#   Volume: EMorSimpleShape::OrientedBox, BoxExtent: (25.2, 150.0, 149.7)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (5999.7856, 4800.0, 2049.6787), (0.0, 0.0, -0.0), (0.5043, 3.0000, 2.9936), "BP_Suburbs_Wall_Thin_Arch_Half_D21", _folder)
if a: placed += 1
else: skipped += 1

# Construction: BP_Suburbs_Wall_Thin_Arch_Half_D22
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Advanced
#   Volume: EMorSimpleShape::OrientedBox, BoxExtent: (25.2, 150.0, 149.7)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (6000.2144, 4800.0, 2350.3215), (0.0, 0.0, -0.0), (0.5043, 3.0000, 2.9936), "BP_Suburbs_Wall_Thin_Arch_Half_D22", _folder)
if a: placed += 1
else: skipped += 1

# Construction: BP_Suburbs_Wall_Thin_Arch_Half_D3
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Advanced
#   Volume: EMorSimpleShape::OrientedBox, BoxExtent: (25.2, 150.0, 149.7)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (1400.2144, 4300.0, 649.6787), (0.0, 0.0, -0.0), (0.5043, 3.0000, 2.9936), "BP_Suburbs_Wall_Thin_Arch_Half_D3", _folder)
if a: placed += 1
else: skipped += 1

# Construction: BP_Suburbs_Wall_Thin_Arch_Half_D4
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Advanced
#   Volume: EMorSimpleShape::OrientedBox, BoxExtent: (25.2, 150.0, 149.7)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (1700.2144, 4300.0, 649.6787), (0.0, 0.0, -0.0), (0.5043, 3.0000, 2.9936), "BP_Suburbs_Wall_Thin_Arch_Half_D4", _folder)
if a: placed += 1
else: skipped += 1

# Construction: BP_Suburbs_Wall_Thin_Arch_Half_D5_8
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Advanced
#   Volume: EMorSimpleShape::OrientedBox, BoxExtent: (150.0, 25.2, 149.7)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (1450.0, 5599.7856, 1249.6787), (0.0, 0.0, -0.0), (3.0000, 0.5043, 2.9936), "BP_Suburbs_Wall_Thin_Arch_Half_D5_8", _folder)
if a: placed += 1
else: skipped += 1

# Construction: BP_Suburbs_Wall_Thin_Arch_Half_D6
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Advanced
#   Volume: EMorSimpleShape::OrientedBox, BoxExtent: (150.0, 25.2, 149.7)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (1450.0, 5600.2144, 1550.3215), (0.0, 0.0, -0.0), (3.0000, 0.5043, 2.9936), "BP_Suburbs_Wall_Thin_Arch_Half_D6", _folder)
if a: placed += 1
else: skipped += 1

# Construction: BP_Suburbs_Wall_Thin_Arch_Half_D7
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Advanced
#   Volume: EMorSimpleShape::OrientedBox, BoxExtent: (150.0, 25.2, 149.7)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (1450.0, 5599.7856, 2149.6787), (0.0, 0.0, -0.0), (3.0000, 0.5043, 2.9936), "BP_Suburbs_Wall_Thin_Arch_Half_D7", _folder)
if a: placed += 1
else: skipped += 1

# Construction: BP_Suburbs_Wall_Thin_Arch_Half_D8
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Advanced
#   Volume: EMorSimpleShape::OrientedBox, BoxExtent: (150.0, 25.2, 149.7)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (1450.0, 5600.2144, 2450.3215), (0.0, 0.0, -0.0), (3.0000, 0.5043, 2.9936), "BP_Suburbs_Wall_Thin_Arch_Half_D8", _folder)
if a: placed += 1
else: skipped += 1

# Construction: BP_Suburbs_Wall_Thin_Arch_Half_D9
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Advanced
#   Volume: EMorSimpleShape::OrientedBox, BoxExtent: (150.0, 25.2, 149.7)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (3350.0, 5599.7856, 649.6787), (0.0, 0.0, -0.0), (3.0000, 0.5043, 2.9936), "BP_Suburbs_Wall_Thin_Arch_Half_D9", _folder)
if a: placed += 1
else: skipped += 1

# Construction: BP_Suburbs_Wall_Thin_Arch_Half_E_2m_2
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Stone
#   Volume: EMorSimpleShape::OrientedBox, BoxExtent: (25.0, 99.7, 50.0)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (1400.0, 4050.0, 750.0), (0.0, 0.0, -0.0), (0.5000, 1.9945, 1.0000), "BP_Suburbs_Wall_Thin_Arch_Half_E_2m_2", _folder)
if a: placed += 1
else: skipped += 1

# Construction: BP_Suburbs_Wall_Thin_Arch_Half_E_2m10
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Stone
#   Volume: EMorSimpleShape::OrientedBox, BoxExtent: (99.7, 25.0, 50.0)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (1000.0, 5600.0, 2350.0), (0.0, 0.0, -0.0), (1.9945, 0.5000, 1.0000), "BP_Suburbs_Wall_Thin_Arch_Half_E_2m10", _folder)
if a: placed += 1
else: skipped += 1

# Construction: BP_Suburbs_Wall_Thin_Arch_Half_E_2m11
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Stone
#   Volume: EMorSimpleShape::OrientedBox, BoxExtent: (25.0, 99.7, 50.0)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (5700.0, 5550.0, 1250.0), (0.0, 0.0, -0.0), (0.5000, 1.9945, 1.0000), "BP_Suburbs_Wall_Thin_Arch_Half_E_2m11", _folder)
if a: placed += 1
else: skipped += 1

# Construction: BP_Suburbs_Wall_Thin_Arch_Half_E_2m12
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Stone
#   Volume: EMorSimpleShape::OrientedBox, BoxExtent: (25.0, 99.7, 50.0)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (5700.0, 5550.0, 1350.0), (0.0, 0.0, -0.0), (0.5000, 1.9945, 1.0000), "BP_Suburbs_Wall_Thin_Arch_Half_E_2m12", _folder)
if a: placed += 1
else: skipped += 1

# Construction: BP_Suburbs_Wall_Thin_Arch_Half_E_2m13
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Stone
#   Volume: EMorSimpleShape::OrientedBox, BoxExtent: (25.0, 99.7, 50.0)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (5700.0, 5550.0, 2150.0), (0.0, 0.0, -0.0), (0.5000, 1.9945, 1.0000), "BP_Suburbs_Wall_Thin_Arch_Half_E_2m13", _folder)
if a: placed += 1
else: skipped += 1

# Construction: BP_Suburbs_Wall_Thin_Arch_Half_E_2m14
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Stone
#   Volume: EMorSimpleShape::OrientedBox, BoxExtent: (25.0, 99.7, 50.0)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (5700.0, 5550.0, 2250.0), (0.0, 0.0, -0.0), (0.5000, 1.9945, 1.0000), "BP_Suburbs_Wall_Thin_Arch_Half_E_2m14", _folder)
if a: placed += 1
else: skipped += 1

# Construction: BP_Suburbs_Wall_Thin_Arch_Half_E_2m15
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Stone
#   Volume: EMorSimpleShape::OrientedBox, BoxExtent: (25.0, 99.7, 50.0)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (5700.0, 5750.0, 1250.0), (0.0, 0.0, -0.0), (0.5000, 1.9945, 1.0000), "BP_Suburbs_Wall_Thin_Arch_Half_E_2m15", _folder)
if a: placed += 1
else: skipped += 1

# Construction: BP_Suburbs_Wall_Thin_Arch_Half_E_2m16
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Stone
#   Volume: EMorSimpleShape::OrientedBox, BoxExtent: (25.0, 99.7, 50.0)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (5700.0, 5750.0, 1350.0), (0.0, 0.0, -0.0), (0.5000, 1.9945, 1.0000), "BP_Suburbs_Wall_Thin_Arch_Half_E_2m16", _folder)
if a: placed += 1
else: skipped += 1

# Construction: BP_Suburbs_Wall_Thin_Arch_Half_E_2m17
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Stone
#   Volume: EMorSimpleShape::OrientedBox, BoxExtent: (25.0, 99.7, 50.0)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (5700.0, 5750.0, 2150.0), (0.0, 0.0, -0.0), (0.5000, 1.9945, 1.0000), "BP_Suburbs_Wall_Thin_Arch_Half_E_2m17", _folder)
if a: placed += 1
else: skipped += 1

# Construction: BP_Suburbs_Wall_Thin_Arch_Half_E_2m18
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Stone
#   Volume: EMorSimpleShape::OrientedBox, BoxExtent: (25.0, 99.7, 50.0)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (5700.0, 5750.0, 2250.0), (0.0, 0.0, -0.0), (0.5000, 1.9945, 1.0000), "BP_Suburbs_Wall_Thin_Arch_Half_E_2m18", _folder)
if a: placed += 1
else: skipped += 1

# Construction: BP_Suburbs_Wall_Thin_Arch_Half_E_2m2
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Stone
#   Volume: EMorSimpleShape::OrientedBox, BoxExtent: (25.0, 99.7, 50.0)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (1700.0, 4050.0, 750.0), (0.0, 0.0, -0.0), (0.5000, 1.9945, 1.0000), "BP_Suburbs_Wall_Thin_Arch_Half_E_2m2", _folder)
if a: placed += 1
else: skipped += 1

# Construction: BP_Suburbs_Wall_Thin_Arch_Half_E_2m23
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Stone
#   Volume: EMorSimpleShape::OrientedBox, BoxExtent: (25.0, 99.7, 50.0)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (6000.0, 5050.0, 1250.0), (0.0, 0.0, -0.0), (0.5000, 1.9945, 1.0000), "BP_Suburbs_Wall_Thin_Arch_Half_E_2m23", _folder)
if a: placed += 1
else: skipped += 1

# Construction: BP_Suburbs_Wall_Thin_Arch_Half_E_2m24
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Stone
#   Volume: EMorSimpleShape::OrientedBox, BoxExtent: (25.0, 99.7, 50.0)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (6000.0, 5050.0, 1350.0), (0.0, 0.0, -0.0), (0.5000, 1.9945, 1.0000), "BP_Suburbs_Wall_Thin_Arch_Half_E_2m24", _folder)
if a: placed += 1
else: skipped += 1

# Construction: BP_Suburbs_Wall_Thin_Arch_Half_E_2m25
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Stone
#   Volume: EMorSimpleShape::OrientedBox, BoxExtent: (25.0, 99.7, 50.0)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (6000.0, 5050.0, 2150.0), (0.0, 0.0, -0.0), (0.5000, 1.9945, 1.0000), "BP_Suburbs_Wall_Thin_Arch_Half_E_2m25", _folder)
if a: placed += 1
else: skipped += 1

# Construction: BP_Suburbs_Wall_Thin_Arch_Half_E_2m26
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Stone
#   Volume: EMorSimpleShape::OrientedBox, BoxExtent: (25.0, 99.7, 50.0)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (6000.0, 5050.0, 2250.0), (0.0, 0.0, -0.0), (0.5000, 1.9945, 1.0000), "BP_Suburbs_Wall_Thin_Arch_Half_E_2m26", _folder)
if a: placed += 1
else: skipped += 1

# Construction: BP_Suburbs_Wall_Thin_Arch_Half_E_2m3_9
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Stone
#   Volume: EMorSimpleShape::OrientedBox, BoxExtent: (99.7, 25.0, 50.0)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (1200.0, 5600.0, 1350.0), (0.0, 0.0, -0.0), (1.9945, 0.5000, 1.0000), "BP_Suburbs_Wall_Thin_Arch_Half_E_2m3_9", _folder)
if a: placed += 1
else: skipped += 1

# Construction: BP_Suburbs_Wall_Thin_Arch_Half_E_2m4
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Stone
#   Volume: EMorSimpleShape::OrientedBox, BoxExtent: (99.7, 25.0, 50.0)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (1200.0, 5600.0, 1450.0), (0.0, 0.0, -0.0), (1.9945, 0.5000, 1.0000), "BP_Suburbs_Wall_Thin_Arch_Half_E_2m4", _folder)
if a: placed += 1
else: skipped += 1

# Construction: BP_Suburbs_Wall_Thin_Arch_Half_E_2m5
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Stone
#   Volume: EMorSimpleShape::OrientedBox, BoxExtent: (99.7, 25.0, 50.0)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (1200.0, 5600.0, 2250.0), (0.0, 0.0, -0.0), (1.9945, 0.5000, 1.0000), "BP_Suburbs_Wall_Thin_Arch_Half_E_2m5", _folder)
if a: placed += 1
else: skipped += 1

# Construction: BP_Suburbs_Wall_Thin_Arch_Half_E_2m6
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Stone
#   Volume: EMorSimpleShape::OrientedBox, BoxExtent: (99.7, 25.0, 50.0)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (1200.0, 5600.0, 2350.0), (0.0, 0.0, -0.0), (1.9945, 0.5000, 1.0000), "BP_Suburbs_Wall_Thin_Arch_Half_E_2m6", _folder)
if a: placed += 1
else: skipped += 1

# Construction: BP_Suburbs_Wall_Thin_Arch_Half_E_2m7
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Stone
#   Volume: EMorSimpleShape::OrientedBox, BoxExtent: (99.7, 25.0, 50.0)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (1000.0, 5600.0, 1350.0), (0.0, 0.0, -0.0), (1.9945, 0.5000, 1.0000), "BP_Suburbs_Wall_Thin_Arch_Half_E_2m7", _folder)
if a: placed += 1
else: skipped += 1

# Construction: BP_Suburbs_Wall_Thin_Arch_Half_E_2m8
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Stone
#   Volume: EMorSimpleShape::OrientedBox, BoxExtent: (99.7, 25.0, 50.0)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (1000.0, 5600.0, 1450.0), (0.0, 0.0, -0.0), (1.9945, 0.5000, 1.0000), "BP_Suburbs_Wall_Thin_Arch_Half_E_2m8", _folder)
if a: placed += 1
else: skipped += 1

# Construction: BP_Suburbs_Wall_Thin_Arch_Half_E_2m9
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Stone
#   Volume: EMorSimpleShape::OrientedBox, BoxExtent: (99.7, 25.0, 50.0)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (1000.0, 5600.0, 2250.0), (0.0, 0.0, -0.0), (1.9945, 0.5000, 1.0000), "BP_Suburbs_Wall_Thin_Arch_Half_E_2m9", _folder)
if a: placed += 1
else: skipped += 1

# ======================================================================
# PHASE 3: Breakables + DecoVolumes
# ======================================================================
unreal.log(f"[{BUBBLE_NAME}] Phase 3: Placing breakables and deco volumes...")

_folder = "Reconstruction/BD_BB_SnakingRiver_Urban/Breakables"

# Breakable Batch 0: BP_Suburb_Stairs_Trim_Angle_B_Breakable (4 instances)
#   BP Class: /Game/LevelDesign/Architecture/Suburbs/BP_Suburb_Stairs_Trim_Angle_B_Breakable
_brk_mesh = "/Game/Art/Assets/Kits/Architecture/Suburbs/Suburb_Stairs_Trim_Angle_B"
_brk_mats = ['/Game/Art/Assets/Kits/Architecture/Suburbs/Materials/Suburb_Stairs_Trim/MI_Suburbs_Stairs_Trim_Angle_Dest']
a = spawn_static_mesh(_brk_mesh, _brk_mats, (1400.0, 3700.0, 900.0), (0.0, 90.0000030488508, -0.0), (1.0, 1.0, 1.0), "BP_Suburb_Stairs_Trim_Angle_B_Breakable_6", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_brk_mesh, _brk_mats, (1700.0, 3700.0, 900.0), (0.0, 90.0000030488508, -0.0), (1.0, 1.0, 1.0), "BP_Suburb_Stairs_Trim_Angle_B_Breakable2_8", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_brk_mesh, _brk_mats, (1700.0, 4400.0, 900.0), (0.0, -89.99997063746636, 0.0), (1.0, 1.0, 1.0), "BP_Suburb_Stairs_Trim_Angle_B_Breakable3", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_brk_mesh, _brk_mats, (1400.0, 4400.0, 900.0), (0.0, -89.99997063746636, 0.0), (1.0, 1.0, 1.0), "BP_Suburb_Stairs_Trim_Angle_B_Breakable4", _folder)
if a: placed += 1
else: skipped += 1

# --- Extra DecoVolumes (not construction blocks) ---
_folder = "Reconstruction/BD_BB_SnakingRiver_Urban/DecoVolumes"

# DecoVolume: BP_Suburb_Stairs_Trim_Angle_B_Breakable_6 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (1399.3438, 3577.0486, 868.09753), (0.0, 0.0, -0.0), (0.4712, 2.4621, 2.6391), "DV_BP_Suburb_Stairs_Trim_Angle_B_Breakable_6_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_Suburb_Stairs_Trim_Angle_B_Breakable2_8 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (1699.3438, 3577.0486, 868.09753), (0.0, 0.0, -0.0), (0.4712, 2.4621, 2.6391), "DV_BP_Suburb_Stairs_Trim_Angle_B_Breakable2_8_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_Suburb_Stairs_Trim_Angle_B_Breakable3 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (1700.6561, 4522.951, 868.09753), (0.0, 0.0, -0.0), (0.4712, 2.4621, 2.6391), "DV_BP_Suburb_Stairs_Trim_Angle_B_Breakable3_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_Suburb_Stairs_Trim_Angle_B_Breakable4 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (1400.6561, 4522.951, 868.09753), (0.0, 0.0, -0.0), (0.4712, 2.4621, 2.6391), "DV_BP_Suburb_Stairs_Trim_Angle_B_Breakable4_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: DecorationBlockingVolume1 (EMorSimpleShape::Empty)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (3200.0, 3200.0, 200.0), (0.0, 0.0, -0.0), (2.0000, 2.0000, 2.0000), "DV_DecorationBlockingVolume1", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: DecorationBlockingVolume12 (EMorSimpleShape::Empty)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (1240.0, 3305.0, 1125.0), (0.0, 0.0, -0.0), (2.0000, 2.0000, 2.0000), "DV_DecorationBlockingVolume12", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: DecorationBlockingVolume13 (EMorSimpleShape::Empty)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (1987.8779, 3455.819, 1175.0), (0.0, 20.00008835691688, -0.0), (2.0000, 2.0000, 2.0000), "DV_DecorationBlockingVolume13", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: DecorationBlockingVolume14 (EMorSimpleShape::Empty)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (4628.326, 4452.291, 1125.0), (-0.0, -49.99987822834905, -0.0), (2.0000, 2.0000, 2.0000), "DV_DecorationBlockingVolume14", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: DecorationBlockingVolume15 (EMorSimpleShape::Empty)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (3566.6865, 1181.104, 1179.9973), (-0.0, -129.99983575060648, -0.0), (2.0000, 2.0000, 2.0000), "DV_DecorationBlockingVolume15", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: DecorationBlockingVolume16 (EMorSimpleShape::Empty)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (2462.881, 956.6835, 935.0), (-0.0, -109.99973131031221, -0.0), (2.0000, 2.0000, 2.0000), "DV_DecorationBlockingVolume16", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: DecorationBlockingVolume17 (EMorSimpleShape::Empty)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (2970.2302, 1573.6122, 935.0), (-0.0, -149.9996984577285, -0.0), (2.0000, 2.0000, 2.0000), "DV_DecorationBlockingVolume17", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: DecorationBlockingVolume18 (EMorSimpleShape::Empty)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (3873.2144, 2129.5967, 935.0), (-0.0, -149.9996984577285, -0.0), (2.0000, 2.0000, 2.0000), "DV_DecorationBlockingVolume18", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: DecorationBlockingVolume19 (EMorSimpleShape::Empty)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (4540.091, 2738.1604, 935.0), (-0.0, -109.9995979964564, -0.0), (2.0000, 2.0000, 2.0000), "DV_DecorationBlockingVolume19", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: DecorationBlockingVolume20 (EMorSimpleShape::Empty)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (4559.829, 3557.8018, 935.0), (-0.0, -59.99948380101396, -0.0), (2.0000, 2.0000, 2.0000), "DV_DecorationBlockingVolume20", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: DecorationBlockingVolume21 (EMorSimpleShape::Empty)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (4012.2336, 4175.5674, 935.0), (-0.0, -39.99944938683695, -0.0), (2.0000, 2.0000, 2.0000), "DV_DecorationBlockingVolume21", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: DecorationBlockingVolume22 (EMorSimpleShape::Empty)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (3120.382, 4488.902, 935.0), (0.0, 10.000941373989438, -0.0), (2.0000, 2.0000, 2.0000), "DV_DecorationBlockingVolume22", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: DecorationBlockingVolume23 (EMorSimpleShape::Empty)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (2194.6667, 4325.656, 1080.0), (0.0, 10.000941373989438, -0.0), (2.0000, 2.0000, 2.0000), "DV_DecorationBlockingVolume23", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: DecorationBlockingVolume24 (EMorSimpleShape::Empty)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (1140.9255, 4134.8354, 935.0), (0.0, 0.0009409999850728273, -0.0), (2.0000, 2.0000, 2.0000), "DV_DecorationBlockingVolume24", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: DecorationBlockingVolume26 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (1766.6865, 1181.104, 1179.9973), (0.0, 75.59978389147341, -0.0), (2.0000, 6.0000, 4.0000), "DV_DecorationBlockingVolume26", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: DecorationBlockingVolume8 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (3200.0, 250.0, 1050.0), (0.0, 0.0, -0.0), (5.0000, 9.0000, 5.0000), "DV_DecorationBlockingVolume8", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: DecorationBlockingVolume9 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (250.0, 3200.0, 1050.0), (-0.0, -90.0001164887758, -0.0), (5.0000, 9.0000, 5.0000), "DV_DecorationBlockingVolume9", _folder)
if a: placed += 1
else: skipped += 1

# ======================================================================
# SUMMARY
# ======================================================================
unreal.log(f"[{BUBBLE_NAME}] Reconstruction complete: {placed} placed, {skipped} skipped, {errors} errors")
