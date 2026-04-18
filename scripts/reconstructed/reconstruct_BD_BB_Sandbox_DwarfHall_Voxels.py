"""Auto-generated level reconstruction script.
Bubble: BD_BB_Sandbox_DwarfHall_Voxels
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

BUBBLE_NAME = "BD_BB_Sandbox_DwarfHall_Voxels"
placed = 0
skipped = 0
errors = 0

# ======================================================================
# PHASE 1: InstancedMeshCatalog  (static mesh placement)
# ======================================================================
unreal.log(f"[{BUBBLE_NAME}] Phase 1: Placing static meshes...")

# Batch 0: StaticMesh'Cube' (13 instances)
_mesh_path = "/Engine/BasicShapes/Cube"
_materials = ['/Game/Art/Assets/Kits/Architecture/Suburbs/Destructable/Materials/MI_Suburbs_Wall_Non_Dest']
_folder = "Reconstruction/BD_BB_Sandbox_DwarfHall_Voxels/Meshes"
a = spawn_static_mesh(_mesh_path, _materials, (5850.0, 3950.0, 1500.0), (0.0, 0.0, -0.0), (11.0, 1.0, 12.0), "Cube_2", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2600.0, 600.0, 2050.0), (0.0, -90.00009542133918, 0.0), (8.0, 1.0, 8.0), "Cube10", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3850.0, 600.0, 1250.0), (0.0, -90.00009542133918, 0.0), (7.0, 1.0, 8.0), "Cube11", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3850.0, 600.0, 2050.0), (0.0, -90.00009542133918, 0.0), (7.0, 1.0, 8.0), "Cube12", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5850.0, 2500.0, 1500.0), (0.0, 0.0, -0.0), (11.0, 1.0, 12.0), "Cube15_6", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5100.0, 4600.0, 1600.0), (0.0, 90.00001925454477, -0.0), (14.0, 1.0, 14.0), "Cube2", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4400.0, 5300.0, 1550.0), (0.0, -179.99995901885745, 0.0), (14.0, 1.0, 14.0), "Cube3", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3850.0005, 5900.0, 1200.0), (0.0, 89.99981506294705, -0.0), (8.0, 1.0, 6.0), "Cube4", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3850.0005, 5900.0, 1850.0), (0.0, 89.99981506294705, -0.0), (8.0, 1.0, 7.0), "Cube5", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (650.0, 2500.0, 1550.0), (0.0, 0.0, -0.0), (14.0, 1.0, 14.0), "Cube6_10", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1400.0, 1799.9999, 1550.0), (0.0, -90.00014890018252, 0.0), (14.0, 1.0, 14.0), "Cube7_12", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2000.0, 1050.0, 1550.0), (0.0, -6.103515418554748e-05, 0.0), (14.0, 1.0, 14.0), "Cube8", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2600.0, 600.0, 1250.0), (0.0, -90.00009542133918, 0.0), (8.0, 1.0, 8.0), "Cube9", _folder)
if a: placed += 1
else: skipped += 1

# Batch 1: StaticMesh'Cube' (9 instances)
_mesh_path = "/Engine/BasicShapes/Cube"
_materials = ['/Game/Art/Assets/Kits/Misc/Dirt_Mounds/Materials/Suburbs_Dirt_Inst']
_folder = "Reconstruction/BD_BB_Sandbox_DwarfHall_Voxels/Meshes"
a = spawn_static_mesh(_mesh_path, _materials, (2150.0, 3379.8691, 778.7165), (0.0, 0.0, -0.0), (8.0, 8.0, 0.5), "Temp_FloorPatch", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2090.7075, 2463.8115, 822.5398), (0.0, 0.0, -0.0), (8.0, 8.0, 0.5), "Temp_FloorPatch2", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1140.7075, 1863.8115, 822.5398), (0.0, 0.0, -0.0), (8.0, 8.0, 0.5), "Temp_FloorPatch3_196", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1990.7075, 813.8115, 822.5398), (0.0, 0.0, -0.0), (8.0, 8.0, 0.5), "Temp_FloorPatch4_198", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5492.1343, 4186.7217, 875.2637), (0.0, 0.0, -0.0), (8.0, 8.0, 0.5), "Temp_FloorPatch5_11", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5492.1343, 4986.7217, 875.2637), (0.0, 0.0, -0.0), (8.0, 8.0, 0.5), "Temp_FloorPatch6_3", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3780.5452, 4590.0, 873.513), (0.0, 0.0, -0.0), (4.0, 4.0, 0.5), "Temp_FloorPatch7", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4442.1343, 5586.7217, 875.2637), (0.0, 0.0, -0.0), (8.0, 8.0, 0.5), "Temp_FloorPatch8", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1990.7075, 1813.8115, 822.5398), (0.0, 0.0, -0.0), (8.0, 8.0, 0.5), "Temp_FloorPatch9", _folder)
if a: placed += 1
else: skipped += 1

# Batch 2: StaticMesh'Cube' (1 instances)
_mesh_path = "/Engine/BasicShapes/Cube"
_materials = ['/Game/Art/Assets/Kits/Misc/Dirt_Mounds/Materials/Sururbs_Dirt_Fix_Inst']
_folder = "Reconstruction/BD_BB_Sandbox_DwarfHall_Voxels/Meshes"
a = spawn_static_mesh(_mesh_path, _materials, (3300.0, 4679.869, 817.87085), (0.0, 0.0, -0.0), (8.0, 8.0, 0.5), "Temp_FloorPatch10", _folder)
if a: placed += 1
else: skipped += 1

# Batch 3: StaticMesh'Plane' (1 instances)
_mesh_path = "/Engine/BasicShapes/Plane"
_materials = ['/Game/Unshippable/WhiteboxMaterials/MI_WB_Grid_DarkGrey']
_folder = "Reconstruction/BD_BB_Sandbox_DwarfHall_Voxels/Meshes"
a = spawn_static_mesh(_mesh_path, _materials, (3200.0, 3200.0, 3200.0), (0.00027084339324111225, -179.99998633961394, -179.9999590188469), (64.0, 64.0, 1.0), "Plane_2", _folder)
if a: placed += 1
else: skipped += 1

# Batch 4: StaticMesh'Architectural_sunstone_window_small' (5 instances)
_mesh_path = "/Game/Art/Assets/Kits/Architecture/City/Architectural_sunstone_window_small"
_materials = ['/Game/Art/Assets/Kits/Architecture/Suburbs/Materials/Suburbs_Trim_Sheet_A/MI_Suburbs_Trim_Sheet_A', '/Game/Environments/Materials/MI_CrystalRoofBright']
_folder = "Reconstruction/BD_BB_Sandbox_DwarfHall_Voxels/Meshes"
a = spawn_static_mesh(_mesh_path, _materials, (3250.0, 3200.0, 2300.0), (0.0, -90.00005166594045, 0.0), (1.2159637, 1.2159637, 1.0), "Skylight_Window_Center", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4450.0, 3200.0, 2300.0), (0.0, -90.00005166594045, 0.0), (1.215964, 1.215964, 1.0), "Skylight_Window_East", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3250.0, 1800.0, 2300.0), (0.0, -90.00005166594045, 0.0), (1.215964, 1.215964, 1.0), "Skylight_Window_North", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3250.0, 4600.0, 2300.0), (0.0, -90.00005166594045, 0.0), (1.215964, 1.215964, 1.0), "Skylight_Window_South", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2050.0, 3200.0, 2300.0), (0.0, -90.00005166594045, 0.0), (1.215964, 1.215964, 1.0), "Skylight_Window_West", _folder)
if a: placed += 1
else: skipped += 1

# Batch 5: StaticMesh'NonD_Stairs_Trim_C_L' (2 instances)
_mesh_path = "/Game/Art/Assets/Kits/Architecture/Non_D/NonD_Stairs_Trim_C_L"
_materials = ['/Game/Art/Assets/Kits/Architecture/Suburbs/Materials/Suburbs_Trim_Sheet_A/MI_Suburbs_Trim_Sheet_A']
_folder = "Reconstruction/BD_BB_Sandbox_DwarfHall_Voxels/Meshes"
a = spawn_static_mesh(_mesh_path, _materials, (6300.0, 3800.0, 700.0), (0.0, -90.0001164887758, 0.0), (1.0, 1.0, 1.0), "NonD_Stairs_Trim_C_L_121", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (6300.0, 2600.0, 700.0), (0.0, 90.00001925454748, -0.0), (1.0, 1.0, 1.0), "NonD_Stairs_Trim_C_L2", _folder)
if a: placed += 1
else: skipped += 1

# Batch 6: StaticMesh'NonDest_Floor_Trim_3M_A' (4 instances)
_mesh_path = "/Game/Art/Assets/Kits/Architecture/Non_D/NonDest_Floor_Trim_3M_A"
_materials = ['/Game/Art/Assets/Kits/Architecture/Suburbs/Materials/Suburbs_Trim_Sheet_A/MI_Suburbs_Trim_Sheet_A']
_folder = "Reconstruction/BD_BB_Sandbox_DwarfHall_Voxels/Meshes"
a = spawn_static_mesh(_mesh_path, _materials, (6300.0, 2600.0, 900.0), (0.0, -179.99998633961752, -0.0), (1.0, 1.0, 1.0), "NonDest_Floor_Trim_3M_A2_1008", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (6300.0, 4100.0, 900.0), (0.0, -179.99998633961752, -0.0), (1.0, 1.0, 1.0), "NonDest_Floor_Trim_3M_A3", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5400.0, 2700.0, 797.5235), (0.0, 90.0001164887758, -0.0), (1.0, 1.0, 1.0), "NonDest_Floor_Trim_3M_A4_1132", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5100.0, 3700.0, 797.5235), (0.0, -89.99959790717821, 0.0), (1.0, 1.0, 1.0), "NonDest_Floor_Trim_3M_A5", _folder)
if a: placed += 1
else: skipped += 1

# Batch 7: StaticMesh'NonDest_Floor_Trim_Corner_B' (1 instances)
_mesh_path = "/Game/Art/Assets/Kits/Architecture/Non_D/NonDest_Floor_Trim_Corner_B"
_materials = ['/Game/Art/Assets/Kits/Architecture/Suburbs/Materials/Suburbs_Trim_Sheet_A/MI_Suburbs_Trim_Sheet_A']
_folder = "Reconstruction/BD_BB_Sandbox_DwarfHall_Voxels/Meshes"
a = spawn_static_mesh(_mesh_path, _materials, (2450.0, 5900.0, 850.0), (0.0, -90.0001164887758, 0.0), (1.0, 1.0, 1.0), "NonDest_Floor_Trim_Corner_B_1079", _folder)
if a: placed += 1
else: skipped += 1

# Batch 8: StaticMesh'NonDest_Floor_Trim_Corner_M' (4 instances)
_mesh_path = "/Game/Art/Assets/Kits/Architecture/Non_D/NonDest_Floor_Trim_Corner_M"
_materials = ['/Game/Art/Assets/Kits/Architecture/Suburbs/Materials/Suburbs_Trim_Sheet_A/MI_Suburbs_Trim_Sheet_A']
_folder = "Reconstruction/BD_BB_Sandbox_DwarfHall_Voxels/Meshes"
a = spawn_static_mesh(_mesh_path, _materials, (2999.455, 2900.3105, 847.7061), (0.0, -90.0001164887758, 0.0), (1.0, 1.0, 1.0), "NonDest_Floor_Trim_Corner_M_5", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3000.0, 3500.0, 847.7061), (0.0, 9.346008142227729e-05, -0.0), (1.0, 1.0, 1.0), "NonDest_Floor_Trim_Corner_M2", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3350.0, 2249.0002, 850.0), (0.0, 179.9999795094293, -0.0), (1.0, 1.0, 1.0), "NonDest_Floor_Trim_Thin_3M_A90", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3350.0002, 4149.0, 850.0), (0.0, 89.99991067642716, -0.0), (1.0, 1.0, 1.0), "NonDest_Floor_Trim_Thin_3M_A99", _folder)
if a: placed += 1
else: skipped += 1

# Batch 9: StaticMesh'NonDest_Floor_Trim_Thin_1_5M_A' (6 instances)
_mesh_path = "/Game/Art/Assets/Kits/Architecture/Non_D/NonDest_Floor_Trim_Thin_1_5M_A"
_materials = ['/Game/Art/Assets/Kits/Architecture/Suburbs/Materials/Suburbs_Trim_Sheet_A/MI_Suburbs_Trim_Sheet_A']
_folder = "Reconstruction/BD_BB_Sandbox_DwarfHall_Voxels/Meshes"
a = spawn_static_mesh(_mesh_path, _materials, (250.0, 3450.0032, 800.0), (0.0, 179.99988388675877, -0.0), (1.0, 1.0, 1.0), "NonDest_Floor_Trim_Thin_3M_A127", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (99.99952, 2950.0032, 800.0), (0.0, 9.53674315662118e-05, -0.0), (1.0, 1.0, 1.0), "NonDest_Floor_Trim_Thin_3M_A128", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3000.0, 498.99994, 850.0), (0.0, -6.103515418554748e-05, 0.0), (1.0, 1.0, 1.0), "NonDest_Floor_Trim_Thin_3M_A78", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3250.0, 498.99963, 850.0), (0.0, -6.103515418554748e-05, 0.0), (1.0, 1.0, 1.0), "NonDest_Floor_Trim_Thin_3M_A81", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3350.0, 2749.0002, 850.0), (0.0, 90.00001925454748, -0.0), (1.0, 1.0, 1.0), "NonDest_Floor_Trim_Thin_3M_A96", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3350.0, 3499.0002, 850.0), (0.0, 90.00001925454748, -0.0), (1.0, 1.0, 1.0), "NonDest_Floor_Trim_Thin_3M_A97", _folder)
if a: placed += 1
else: skipped += 1

# Batch 10: StaticMesh'NonDest_Floor_Trim_Thin_1M_A' (8 instances)
_mesh_path = "/Game/Art/Assets/Kits/Architecture/Non_D/NonDest_Floor_Trim_Thin_1M_A"
_materials = ['/Game/Art/Assets/Kits/Architecture/Suburbs/Materials/Suburbs_Trim_Sheet_A/MI_Suburbs_Trim_Sheet_A']
_folder = "Reconstruction/BD_BB_Sandbox_DwarfHall_Voxels/Meshes"
a = spawn_static_mesh(_mesh_path, _materials, (3550.0, 2299.6677, 900.0), (0.0, 0.0, -0.0), (1.0, 1.0, 1.0), "NonDest_Floor_Trim_Thin_1M_A_50", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3650.0, 4100.0, 900.0), (0.0, -179.99998633961752, -0.0), (1.0, 1.0, 1.0), "NonDest_Floor_Trim_Thin_1M_A2_56", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3550.0002, 5649.0, 850.0), (0.0, 89.99995929348692, -0.0), (1.0, 1.0, 1.0), "NonDest_Floor_Trim_Thin_3M_A106_72", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2850.0007, 5749.0, 850.0), (0.0, -90.00018131163026, 0.0), (1.0, 1.0, 1.0), "NonDest_Floor_Trim_Thin_3M_A111", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (-0.00048065186, 2950.0032, 800.0), (0.0, 9.500000060768745e-05, -0.0), (1.0, 1.0, 1.0), "NonDest_Floor_Trim_Thin_3M_A140", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (100.0, 3450.0032, 800.0), (0.0, 179.99988388675877, -0.0), (1.0, 1.0, 1.0), "NonDest_Floor_Trim_Thin_3M_A141", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3150.0, 498.99976, 850.0), (0.0, -6.103515418554748e-05, 0.0), (1.0, 1.0, 1.0), "NonDest_Floor_Trim_Thin_3M_A83", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3550.0, 2149.0002, 850.0), (0.0, 90.00001925454748, -0.0), (1.0, 1.0, 1.0), "NonDest_Floor_Trim_Thin_3M_A88_40", _folder)
if a: placed += 1
else: skipped += 1

# Batch 11: StaticMesh'NonDest_Floor_Trim_Thin_2M_A' (8 instances)
_mesh_path = "/Game/Art/Assets/Kits/Architecture/Non_D/NonDest_Floor_Trim_Thin_2M_A"
_materials = ['/Game/Art/Assets/Kits/Architecture/Suburbs/Materials/Suburbs_Trim_Sheet_A/MI_Suburbs_Trim_Sheet_A']
_folder = "Reconstruction/BD_BB_Sandbox_DwarfHall_Voxels/Meshes"
a = spawn_static_mesh(_mesh_path, _materials, (3350.0, 4149.0, 850.0), (0.0, -6.103515418554748e-05, 0.0), (1.0, 1.0, 1.0), "NonDest_Floor_Trim_Thin_3M_A100", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3400.0002, 5899.0, 850.0), (0.0, 179.9999590188648, -0.0), (1.0, 1.0, 1.0), "NonDest_Floor_Trim_Thin_3M_A108", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3200.0002, 5899.0, 850.0), (0.0, 179.9999590188648, -0.0), (1.0, 1.0, 1.0), "NonDest_Floor_Trim_Thin_3M_A109", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2800.0732, 6200.0, 897.78503), (0.0, 89.99959790717821, -0.0), (1.0, 1.0, 1.0), "NonDest_Floor_Trim_Thin_3M_A138", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2499.756, 6400.0, 897.78503), (0.0, -90.0001164887758, 0.0), (1.0, 1.0, 1.0), "NonDest_Floor_Trim_Thin_3M_A139", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3549.9995, 2249.0002, 850.0), (0.0, -179.9998224150775, 0.0), (1.0, 1.0, 1.0), "NonDest_Floor_Trim_Thin_3M_A89_43", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3350.0, 2549.0002, 850.0), (0.0, 90.00001925454748, -0.0), (1.0, 1.0, 1.0), "NonDest_Floor_Trim_Thin_3M_A92", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3350.0, 3649.0002, 850.0), (0.0, 90.00001925454748, -0.0), (1.0, 1.0, 1.0), "NonDest_Floor_Trim_Thin_3M_A95_58", _folder)
if a: placed += 1
else: skipped += 1

# Batch 12: StaticMesh'NonDest_Floor_Trim_Thin_3M_A' (113 instances)
_mesh_path = "/Game/Art/Assets/Kits/Architecture/Non_D/NonDest_Floor_Trim_Thin_3M_A"
_materials = ['/Game/Art/Assets/Kits/Architecture/Suburbs/Materials/Suburbs_Trim_Sheet_A/MI_Suburbs_Trim_Sheet_A']
_folder = "Reconstruction/BD_BB_Sandbox_DwarfHall_Voxels/Meshes"
a = spawn_static_mesh(_mesh_path, _materials, (2999.5967, 3200.0, 847.7061), (0.0, -90.00005166594045, 0.0), (1.0, 1.0, 1.0), "NonDest_Floor_Trim_Thin_3M_A_8", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (899.7998, 2900.5234, 847.7061), (0.0, 179.99994535848643, -0.0), (1.0, 1.0, 1.0), "NonDest_Floor_Trim_Thin_3M_A10", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3550.0, 4149.0, 850.0), (0.0, 89.99995929348692, -0.0), (1.0, 1.0, 1.0), "NonDest_Floor_Trim_Thin_3M_A101", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3550.0002, 4449.0, 850.0), (0.0, 89.99995929348692, -0.0), (1.0, 1.0, 1.0), "NonDest_Floor_Trim_Thin_3M_A102", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3550.0002, 4749.0, 850.0), (0.0, 89.99995929348692, -0.0), (1.0, 1.0, 1.0), "NonDest_Floor_Trim_Thin_3M_A103", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3550.0002, 5049.0, 850.0), (0.0, 89.99995929348692, -0.0), (1.0, 1.0, 1.0), "NonDest_Floor_Trim_Thin_3M_A104", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3550.0002, 5349.0, 850.0), (0.0, 89.99995929348692, -0.0), (1.0, 1.0, 1.0), "NonDest_Floor_Trim_Thin_3M_A105", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (599.7998, 2900.5234, 847.7061), (0.0, 179.99994535848643, -0.0), (1.0, 1.0, 1.0), "NonDest_Floor_Trim_Thin_3M_A11", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2850.0002, 5649.0, 850.0), (0.0, -90.0001164887758, 0.0), (1.0, 1.0, 1.0), "NonDest_Floor_Trim_Thin_3M_A112", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2850.0002, 5349.0, 850.0), (0.0, -90.0001164887758, 0.0), (1.0, 1.0, 1.0), "NonDest_Floor_Trim_Thin_3M_A113", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2850.0002, 5049.0, 850.0), (0.0, -90.0001164887758, 0.0), (1.0, 1.0, 1.0), "NonDest_Floor_Trim_Thin_3M_A114", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2849.9995, 4749.0, 850.0), (0.0, -90.0001164887758, 0.0), (1.0, 1.0, 1.0), "NonDest_Floor_Trim_Thin_3M_A115", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2849.999, 4449.0, 850.0), (0.0, -90.0001164887758, 0.0), (1.0, 1.0, 1.0), "NonDest_Floor_Trim_Thin_3M_A116", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2850.0005, 1549.0001, 850.0), (0.0, -90.0001164887758, 0.0), (1.0, 1.0, 1.0), "NonDest_Floor_Trim_Thin_3M_A117", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2850.0005, 1849.0001, 850.0), (0.0, -90.0001164887758, 0.0), (1.0, 1.0, 1.0), "NonDest_Floor_Trim_Thin_3M_A118", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2850.0007, 2149.0, 850.0), (0.0, -90.0001164887758, 0.0), (1.0, 1.0, 1.0), "NonDest_Floor_Trim_Thin_3M_A119", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (299.7998, 2900.5234, 847.7061), (0.0, 179.99994535848643, -0.0), (1.0, 1.0, 1.0), "NonDest_Floor_Trim_Thin_3M_A12", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2850.001, 2449.0, 850.0), (0.0, -90.0001164887758, 0.0), (1.0, 1.0, 1.0), "NonDest_Floor_Trim_Thin_3M_A120", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2050.0, 3450.001, 800.0), (0.0, 179.99988388675877, -0.0), (1.0, 1.0, 1.0), "NonDest_Floor_Trim_Thin_3M_A121", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1750.0, 3450.0012, 800.0), (0.0, 179.99988388675877, -0.0), (1.0, 1.0, 1.0), "NonDest_Floor_Trim_Thin_3M_A122", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1450.0, 3450.0015, 800.0), (0.0, 179.99988388675877, -0.0), (1.0, 1.0, 1.0), "NonDest_Floor_Trim_Thin_3M_A123", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1150.0, 3450.0022, 800.0), (0.0, 179.99988388675877, -0.0), (1.0, 1.0, 1.0), "NonDest_Floor_Trim_Thin_3M_A124", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (850.0, 3450.0024, 800.0), (0.0, 179.99988388675877, -0.0), (1.0, 1.0, 1.0), "NonDest_Floor_Trim_Thin_3M_A125", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (550.0, 3450.003, 800.0), (0.0, 179.99988388675877, -0.0), (1.0, 1.0, 1.0), "NonDest_Floor_Trim_Thin_3M_A126", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (249.99649, 2950.0042, 800.0), (0.0, -0.00039672851366830966, 0.0), (1.0, 1.0, 1.0), "NonDest_Floor_Trim_Thin_3M_A129", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2700.0, 3499.685, 847.7061), (0.0, -0.0004272461022210228, 0.0), (1.0, 1.0, 1.0), "NonDest_Floor_Trim_Thin_3M_A13", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (549.99646, 2950.003, 800.0), (0.0, -0.00039672851366830966, 0.0), (1.0, 1.0, 1.0), "NonDest_Floor_Trim_Thin_3M_A130", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (849.99646, 2950.0002, 800.0), (0.0, -0.00039672851366830966, 0.0), (1.0, 1.0, 1.0), "NonDest_Floor_Trim_Thin_3M_A131", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1149.9965, 2949.999, 800.0), (0.0, -0.00039672851366830966, 0.0), (1.0, 1.0, 1.0), "NonDest_Floor_Trim_Thin_3M_A132", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1449.9965, 2949.9958, 800.0), (0.0, -0.00039672851366830966, 0.0), (1.0, 1.0, 1.0), "NonDest_Floor_Trim_Thin_3M_A133", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1749.9965, 2949.9946, 800.0), (0.0, -0.00039672851366830966, 0.0), (1.0, 1.0, 1.0), "NonDest_Floor_Trim_Thin_3M_A134", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2049.9966, 2949.992, 800.0), (0.0, -0.00039672851366830966, 0.0), (1.0, 1.0, 1.0), "NonDest_Floor_Trim_Thin_3M_A135", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2349.9966, 2949.9907, 800.0), (0.0, -0.00039672851366830966, 0.0), (1.0, 1.0, 1.0), "NonDest_Floor_Trim_Thin_3M_A136", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2649.9966, 2949.9888, 800.0), (0.0, -0.00039672851366830966, 0.0), (1.0, 1.0, 1.0), "NonDest_Floor_Trim_Thin_3M_A137", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2400.0, 3499.685, 847.7061), (0.0, -0.0004272461022210228, 0.0), (1.0, 1.0, 1.0), "NonDest_Floor_Trim_Thin_3M_A14", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2100.0, 3499.685, 847.7061), (0.0, -0.0004272461022210228, 0.0), (1.0, 1.0, 1.0), "NonDest_Floor_Trim_Thin_3M_A15", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1800.0, 3499.685, 847.7061), (0.0, -0.0004272461022210228, 0.0), (1.0, 1.0, 1.0), "NonDest_Floor_Trim_Thin_3M_A16", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1500.0, 3499.685, 847.7061), (0.0, -0.0004272461022210228, 0.0), (1.0, 1.0, 1.0), "NonDest_Floor_Trim_Thin_3M_A17", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1200.0, 3499.685, 847.7061), (0.0, -0.0004272461022210228, 0.0), (1.0, 1.0, 1.0), "NonDest_Floor_Trim_Thin_3M_A18", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (900.0, 3499.685, 847.7061), (0.0, -0.0004272461022210228, 0.0), (1.0, 1.0, 1.0), "NonDest_Floor_Trim_Thin_3M_A19", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2999.5967, 3500.0, 847.7061), (0.0, -90.00005166594045, 0.0), (1.0, 1.0, 1.0), "NonDest_Floor_Trim_Thin_3M_A2", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (600.0, 3499.685, 847.7061), (0.0, -0.0004272461022210228, 0.0), (1.0, 1.0, 1.0), "NonDest_Floor_Trim_Thin_3M_A20", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (300.0, 3499.685, 847.7061), (0.0, -0.0004272461022210228, 0.0), (1.0, 1.0, 1.0), "NonDest_Floor_Trim_Thin_3M_A21", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (0.0, 3499.685, 847.7061), (0.0, -0.0004272461022210228, 0.0), (1.0, 1.0, 1.0), "NonDest_Floor_Trim_Thin_3M_A22", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3399.4844, 3950.0, 897.5041), (0.0, -90.0001164887758, 0.0), (1.0, 1.0, 1.0), "NonDest_Floor_Trim_Thin_3M_A23_39", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3399.4844, 3650.0, 897.5041), (0.0, -90.0001164887758, 0.0), (1.0, 1.0, 1.0), "NonDest_Floor_Trim_Thin_3M_A24", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3399.4844, 3350.0, 897.5041), (0.0, -90.0001164887758, 0.0), (1.0, 1.0, 1.0), "NonDest_Floor_Trim_Thin_3M_A25", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3399.4844, 3050.0, 897.5041), (0.0, -90.0001164887758, 0.0), (1.0, 1.0, 1.0), "NonDest_Floor_Trim_Thin_3M_A26", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3399.4844, 2750.0, 897.5041), (0.0, -90.0001164887758, 0.0), (1.0, 1.0, 1.0), "NonDest_Floor_Trim_Thin_3M_A27", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3599.6755, 5000.0, 897.78503), (0.0, -90.0001164887758, 0.0), (1.0, 1.0, 1.0), "NonDest_Floor_Trim_Thin_3M_A28_59", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3599.6755, 4700.0, 897.78503), (0.0, -90.0001164887758, 0.0), (1.0, 1.0, 1.0), "NonDest_Floor_Trim_Thin_3M_A29", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2999.7998, 2900.5234, 847.7061), (0.0, 179.99994535848643, -0.0), (1.0, 1.0, 1.0), "NonDest_Floor_Trim_Thin_3M_A3", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3599.6755, 4400.0, 897.78503), (0.0, -90.0001164887758, 0.0), (1.0, 1.0, 1.0), "NonDest_Floor_Trim_Thin_3M_A30", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3599.6755, 5300.0, 897.78503), (0.0, -90.0001164887758, 0.0), (1.0, 1.0, 1.0), "NonDest_Floor_Trim_Thin_3M_A31", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3599.6755, 5600.0, 897.78503), (0.0, -90.0001164887758, 0.0), (1.0, 1.0, 1.0), "NonDest_Floor_Trim_Thin_3M_A32", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3599.6755, 5900.0, 897.78503), (0.0, -90.0001164887758, 0.0), (1.0, 1.0, 1.0), "NonDest_Floor_Trim_Thin_3M_A33", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3599.6755, 6200.0, 897.78503), (0.0, -90.0001164887758, 0.0), (1.0, 1.0, 1.0), "NonDest_Floor_Trim_Thin_3M_A34", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2950.0, 3450.0, 800.0), (0.0, 179.99988388675877, -0.0), (1.0, 1.0, 1.0), "NonDest_Floor_Trim_Thin_3M_A35_97", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2650.0, 3450.0002, 800.0), (0.0, 179.99988388675877, -0.0), (1.0, 1.0, 1.0), "NonDest_Floor_Trim_Thin_3M_A36", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2350.0, 3450.0007, 800.0), (0.0, 179.99988388675877, -0.0), (1.0, 1.0, 1.0), "NonDest_Floor_Trim_Thin_3M_A37", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2800.0713, 5900.0, 897.78503), (0.0, 89.99959790717821, -0.0), (1.0, 1.0, 1.0), "NonDest_Floor_Trim_Thin_3M_A38", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2800.0713, 5600.0, 897.78503), (0.0, 89.99959790717821, -0.0), (1.0, 1.0, 1.0), "NonDest_Floor_Trim_Thin_3M_A39", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2699.7998, 2900.5234, 847.7061), (0.0, 179.99994535848643, -0.0), (1.0, 1.0, 1.0), "NonDest_Floor_Trim_Thin_3M_A4", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2499.7576, 5899.9995, 897.78503), (0.0, -90.0001164887758, 0.0), (1.0, 1.0, 1.0), "NonDest_Floor_Trim_Thin_3M_A40", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2499.756, 6200.0, 897.78503), (0.0, -90.0001164887758, 0.0), (1.0, 1.0, 1.0), "NonDest_Floor_Trim_Thin_3M_A41", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2800.0713, 4700.0, 897.78503), (0.0, 89.99959790717821, -0.0), (1.0, 1.0, 1.0), "NonDest_Floor_Trim_Thin_3M_A42_81", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2800.0713, 4400.0, 897.78503), (0.0, 89.99959790717821, -0.0), (1.0, 1.0, 1.0), "NonDest_Floor_Trim_Thin_3M_A43_82", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2499.7576, 4699.9995, 897.78503), (0.0, -90.0001164887758, 0.0), (1.0, 1.0, 1.0), "NonDest_Floor_Trim_Thin_3M_A44_83", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2499.756, 5000.0, 897.78503), (0.0, -90.0001164887758, 0.0), (1.0, 1.0, 1.0), "NonDest_Floor_Trim_Thin_3M_A45_84", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2800.0713, 4100.0, 897.78503), (0.0, 89.99959790717821, -0.0), (1.0, 1.0, 1.0), "NonDest_Floor_Trim_Thin_3M_A46", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2499.7576, 4399.9995, 897.78503), (0.0, -90.0001164887758, 0.0), (1.0, 1.0, 1.0), "NonDest_Floor_Trim_Thin_3M_A47", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3599.4844, 2300.0, 897.5041), (0.0, -90.0001164887758, 0.0), (1.0, 1.0, 1.0), "NonDest_Floor_Trim_Thin_3M_A48", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3599.4844, 2000.0, 897.5041), (0.0, -90.0001164887758, 0.0), (1.0, 1.0, 1.0), "NonDest_Floor_Trim_Thin_3M_A49", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2399.7998, 2900.5234, 847.7061), (0.0, 179.99994535848643, -0.0), (1.0, 1.0, 1.0), "NonDest_Floor_Trim_Thin_3M_A5", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3599.4844, 1700.0, 897.5041), (0.0, -90.0001164887758, 0.0), (1.0, 1.0, 1.0), "NonDest_Floor_Trim_Thin_3M_A50", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3599.4844, 1400.0, 897.5041), (0.0, -90.0001164887758, 0.0), (1.0, 1.0, 1.0), "NonDest_Floor_Trim_Thin_3M_A51", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3599.4844, 1100.0, 897.5041), (0.0, -90.0001164887758, 0.0), (1.0, 1.0, 1.0), "NonDest_Floor_Trim_Thin_3M_A52", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3599.4844, 800.0, 897.5041), (0.0, -90.0001164887758, 0.0), (1.0, 1.0, 1.0), "NonDest_Floor_Trim_Thin_3M_A53", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3599.4844, 500.0, 897.5041), (0.0, -90.0001164887758, 0.0), (1.0, 1.0, 1.0), "NonDest_Floor_Trim_Thin_3M_A54", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4900.398, 2749.9993, 897.5041), (0.0, 90.00014890018252, -0.0), (1.0, 1.0, 1.0), "NonDest_Floor_Trim_Thin_3M_A55", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4900.397, 3050.0, 897.5041), (0.0, 90.00014890018252, -0.0), (1.0, 1.0, 1.0), "NonDest_Floor_Trim_Thin_3M_A56", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4900.395, 3350.0, 897.5041), (0.0, 90.00014890018252, -0.0), (1.0, 1.0, 1.0), "NonDest_Floor_Trim_Thin_3M_A57", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5400.3945, 3798.1794, 897.5041), (0.0, -3.051757709276941e-05, 0.0), (1.0, 1.0, 1.0), "NonDest_Floor_Trim_Thin_3M_A58", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5700.3945, 3798.1797, 897.5041), (0.0, -3.051757709276941e-05, 0.0), (1.0, 1.0, 1.0), "NonDest_Floor_Trim_Thin_3M_A59", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2099.7998, 2900.5234, 847.7061), (0.0, 179.99994535848643, -0.0), (1.0, 1.0, 1.0), "NonDest_Floor_Trim_Thin_3M_A6", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (6000.395, 3798.181, 897.5041), (0.0, -3.051757709276941e-05, 0.0), (1.0, 1.0, 1.0), "NonDest_Floor_Trim_Thin_3M_A60", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5100.3945, 3798.1794, 897.5041), (0.0, -3.051757709276941e-05, 0.0), (1.0, 1.0, 1.0), "NonDest_Floor_Trim_Thin_3M_A61", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (6300.3955, 2600.5864, 897.5041), (0.0, -179.9998360754275, 0.0), (1.0, 1.0, 1.0), "NonDest_Floor_Trim_Thin_3M_A62", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (6000.3955, 2600.5857, 897.5041), (0.0, -179.9998360754275, 0.0), (1.0, 1.0, 1.0), "NonDest_Floor_Trim_Thin_3M_A63", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5700.395, 2600.5825, 897.5041), (0.0, -179.9998360754275, 0.0), (1.0, 1.0, 1.0), "NonDest_Floor_Trim_Thin_3M_A64", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5400.395, 2600.5825, 897.5041), (0.0, -179.9998360754275, 0.0), (1.0, 1.0, 1.0), "NonDest_Floor_Trim_Thin_3M_A65", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2499.4844, 800.0, 897.5041), (0.0, -90.0001164887758, 0.0), (1.0, 1.0, 1.0), "NonDest_Floor_Trim_Thin_3M_A66", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2800.9463, 500.0, 897.5041), (0.0, 90.00016510590689, -0.0), (1.0, 1.0, 1.0), "NonDest_Floor_Trim_Thin_3M_A67", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2499.4844, 500.0, 897.5041), (0.0, -90.0001164887758, 0.0), (1.0, 1.0, 1.0), "NonDest_Floor_Trim_Thin_3M_A68_6", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2800.9463, 200.0, 897.5041), (0.0, 90.00016510590689, -0.0), (1.0, 1.0, 1.0), "NonDest_Floor_Trim_Thin_3M_A69_7", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1799.7998, 2900.5234, 847.7061), (0.0, 179.99994535848643, -0.0), (1.0, 1.0, 1.0), "NonDest_Floor_Trim_Thin_3M_A7", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2800.9463, 1350.0, 897.5041), (0.0, 90.00016510590689, -0.0), (1.0, 1.0, 1.0), "NonDest_Floor_Trim_Thin_3M_A70", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4899.485, 2599.9983, 897.5041), (0.0, 179.99978826413437, -0.0), (1.0, 1.0, 1.0), "NonDest_Floor_Trim_Thin_3M_A71", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4599.4844, 2599.999, 897.5041), (0.0, 179.99978826413437, -0.0), (1.0, 1.0, 1.0), "NonDest_Floor_Trim_Thin_3M_A72", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4299.4844, 2600.0, 897.5041), (0.0, 179.99978826413437, -0.0), (1.0, 1.0, 1.0), "NonDest_Floor_Trim_Thin_3M_A73", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2850.0, 949.0001, 850.0), (0.0, -90.0001164887758, 0.0), (1.0, 1.0, 1.0), "NonDest_Floor_Trim_Thin_3M_A76_6", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2850.0002, 1249.0001, 850.0), (0.0, -90.0001164887758, 0.0), (1.0, 1.0, 1.0), "NonDest_Floor_Trim_Thin_3M_A79_89", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1499.7998, 2900.5234, 847.7061), (0.0, 179.99994535848643, -0.0), (1.0, 1.0, 1.0), "NonDest_Floor_Trim_Thin_3M_A8", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3550.0, 649.00024, 850.0), (0.0, 90.00001925454748, -0.0), (1.0, 1.0, 1.0), "NonDest_Floor_Trim_Thin_3M_A82", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3550.0, 949.00024, 850.0), (0.0, 90.00001925454748, -0.0), (1.0, 1.0, 1.0), "NonDest_Floor_Trim_Thin_3M_A84", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3550.0, 1249.0002, 850.0), (0.0, 90.00001925454748, -0.0), (1.0, 1.0, 1.0), "NonDest_Floor_Trim_Thin_3M_A85", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3550.0, 1549.0002, 850.0), (0.0, 90.00001925454748, -0.0), (1.0, 1.0, 1.0), "NonDest_Floor_Trim_Thin_3M_A86", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3550.0, 1849.0002, 850.0), (0.0, 90.00001925454748, -0.0), (1.0, 1.0, 1.0), "NonDest_Floor_Trim_Thin_3M_A87_38", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1199.7998, 2900.5234, 847.7061), (0.0, 179.99994535848643, -0.0), (1.0, 1.0, 1.0), "NonDest_Floor_Trim_Thin_3M_A9", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3350.0, 2249.0002, 850.0), (0.0, 90.00001925454748, -0.0), (1.0, 1.0, 1.0), "NonDest_Floor_Trim_Thin_3M_A91", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3350.0, 2899.0002, 850.0), (0.0, 90.00001925454748, -0.0), (1.0, 1.0, 1.0), "NonDest_Floor_Trim_Thin_3M_A93", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3350.0, 3199.0002, 850.0), (0.0, 90.00001925454748, -0.0), (1.0, 1.0, 1.0), "NonDest_Floor_Trim_Thin_3M_A94", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3350.0, 3849.0002, 850.0), (0.0, 90.00001925454748, -0.0), (1.0, 1.0, 1.0), "NonDest_Floor_Trim_Thin_3M_A98", _folder)
if a: placed += 1
else: skipped += 1

# Batch 13: StaticMesh'NonDest_Floor_Trim_Thin_Corner_A' (6 instances)
_mesh_path = "/Game/Art/Assets/Kits/Architecture/Non_D/NonDest_Floor_Trim_Thin_Corner_A"
_materials = ['/Game/Art/Assets/Kits/Architecture/Suburbs/Materials/Suburbs_Trim_Sheet_A/MI_Suburbs_Trim_Sheet_A']
_folder = "Reconstruction/BD_BB_Sandbox_DwarfHall_Voxels/Meshes"
a = spawn_static_mesh(_mesh_path, _materials, (3550.0002, 5749.0, 850.0), (0.0, 89.99995929348692, -0.0), (1.0, 1.0, 1.0), "NonDest_Floor_Trim_Thin_3M_A107", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3000.0002, 5899.0, 850.0), (0.0, 179.9999795094293, -0.0), (1.0, 1.0, 1.0), "NonDest_Floor_Trim_Thin_3M_A110", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2849.9998, 649.0001, 850.0), (0.0, -90.0001164887758, 0.0), (1.0, 1.0, 1.0), "NonDest_Floor_Trim_Thin_3M_A77", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3399.9998, 498.99875, 850.0), (0.0, -3.051757709276941e-05, 0.0), (1.0, 1.0, 1.0), "NonDest_Floor_Trim_Thin_3M_A80", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3549.4844, 4100.0, 897.5041), (0.0, 179.99981558486024, -0.0), (1.0, 1.0, 1.0), "NonDest_Floor_Trim_Thin_Corner_A_36", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3399.4844, 2449.6677, 897.5041), (0.0, -89.99999818714215, 0.0), (1.0, 1.0, 1.0), "NonDest_Floor_Trim_Thin_Corner_A2", _folder)
if a: placed += 1
else: skipped += 1

# Batch 14: StaticMesh'NonDest_Trim_3M_B' (20 instances)
_mesh_path = "/Game/Art/Assets/Kits/Architecture/Non_D/NonDest_Trim_3M_B"
_materials = ['/Game/Environments/Materials/MI_Suburbs_Non_Destructible', '/Game/Art/Assets/Kits/Architecture/Suburbs/Materials/Suburbs_Trim_Sheet_A/MI_Suburbs_Trim_Sheet_A']
_folder = "Reconstruction/BD_BB_Sandbox_DwarfHall_Voxels/Meshes"
a = spawn_static_mesh(_mesh_path, _materials, (223.86917, 4650.0, 850.0), (0.0, 90.00007597449323, -0.0), (1.0, 1.0, 1.0), "NonDest_Trim_3M_B11", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (202.11961, 4650.0, 850.0), (0.0, -89.99999818714215, 0.0), (1.0, 1.0, 1.0), "NonDest_Trim_3M_B12", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (223.86917, 5500.0, 850.0), (0.0, 90.00007597449323, -0.0), (1.0, 1.0, 1.0), "NonDest_Trim_3M_B13", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (202.11961, 5500.0, 850.0), (0.0, -89.99999818714215, 0.0), (1.0, 1.0, 1.0), "NonDest_Trim_3M_B14", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (223.86917, 5800.0, 850.0), (0.0, 90.00007597449323, -0.0), (1.0, 1.0, 1.0), "NonDest_Trim_3M_B15", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (202.11961, 5800.0, 850.0), (0.0, -89.99999818714215, 0.0), (1.0, 1.0, 1.0), "NonDest_Trim_3M_B16", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (602.1196, 6178.2505, 850.0), (0.0, -6.103515418554748e-05, 0.0), (1.0, 1.0, 1.0), "NonDest_Trim_3M_B17", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (602.1196, 6200.0, 850.0), (0.0, 179.99994535848643, -0.0), (1.0, 1.0, 1.0), "NonDest_Trim_3M_B18", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (902.1196, 6178.2505, 850.0), (0.0, -6.103515418554748e-05, 0.0), (1.0, 1.0, 1.0), "NonDest_Trim_3M_B19", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (902.1196, 6200.0, 850.0), (0.0, 179.99994535848643, -0.0), (1.0, 1.0, 1.0), "NonDest_Trim_3M_B20", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1752.1196, 6178.2505, 850.0), (0.0, -6.103515418554748e-05, 0.0), (1.0, 1.0, 1.0), "NonDest_Trim_3M_B21", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1752.1196, 6200.0, 850.0), (0.0, 179.99994535848643, -0.0), (1.0, 1.0, 1.0), "NonDest_Trim_3M_B22", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4652.1196, 221.74945, 850.0), (0.0, -179.9998360754275, 0.0), (1.0, 1.0, 1.0), "NonDest_Trim_3M_B51", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4652.1196, 200.0, 850.0), (0.0, 0.00021199999918528064, -0.0), (1.0, 1.0, 1.0), "NonDest_Trim_3M_B52", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4952.1196, 221.74945, 850.0), (0.0, -179.9998360754275, 0.0), (1.0, 1.0, 1.0), "NonDest_Trim_3M_B53", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4952.1196, 200.0, 850.0), (0.0, 0.00021199999918528064, -0.0), (1.0, 1.0, 1.0), "NonDest_Trim_3M_B54", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1452.1196, 6178.2505, 850.0), (0.0, -6.103515418554748e-05, 0.0), (1.0, 1.0, 1.0), "NonDest_Trim_3M_B61", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1452.1196, 6200.0, 850.0), (0.0, 179.99994535848643, -0.0), (1.0, 1.0, 1.0), "NonDest_Trim_3M_B62", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (223.86917, 4950.0, 850.0), (0.0, 90.00007597449323, -0.0), (1.0, 1.0, 1.0), "NonDest_Trim_3M_B63", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (202.11961, 4950.0, 850.0), (0.0, -89.99999818714215, 0.0), (1.0, 1.0, 1.0), "NonDest_Trim_3M_B64", _folder)
if a: placed += 1
else: skipped += 1

# Batch 15: StaticMesh'Dwarf_Hall_Column_Mural_Large' (8 instances)
_mesh_path = "/Game/Art/Assets/Kits/Architecture/Suburbs/Dwarf_Hall_Column_Mural_Large"
_materials = ['/Game/Art/Assets/Kits/Architecture/Suburbs/Materials/Suburbs_Trim_Sheet_B/MI_Suburbs_Trim_Sheet_B_Gold']
_folder = "Reconstruction/BD_BB_Sandbox_DwarfHall_Voxels/Meshes"
a = spawn_static_mesh(_mesh_path, _materials, (2650.0, 2805.9683, 1000.0), (0.0, 0.0, -0.0), (1.0, 1.0, 1.0), "Dwarf_Hall_Column_Mural_Large_2", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1450.0, 2805.9683, 1000.0), (0.0, 0.0, -0.0), (1.0, 1.0, 1.0), "Dwarf_Hall_Column_Mural_Large2", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3850.0, 2805.9683, 1000.0), (0.0, 0.0, -0.0), (1.0, 1.0, 1.0), "Dwarf_Hall_Column_Mural_Large3", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5050.0, 2805.9683, 1000.0), (0.0, 0.0, -0.0), (1.0, 1.0, 1.0), "Dwarf_Hall_Column_Mural_Large4", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5050.0, 3592.9287, 1000.0), (0.0, -179.99980192457332, 0.0), (1.0, 1.0, 1.0), "Dwarf_Hall_Column_Mural_Large5", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3850.0, 3592.9287, 1000.0), (0.0, -179.99980192457332, 0.0), (1.0, 1.0, 1.0), "Dwarf_Hall_Column_Mural_Large6", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2650.0, 3592.9287, 1000.0), (0.0, -179.99980192457332, 0.0), (1.0, 1.0, 1.0), "Dwarf_Hall_Column_Mural_Large7", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1450.0, 3592.9287, 1000.0), (0.0, -179.99980192457332, 0.0), (1.0, 1.0, 1.0), "Dwarf_Hall_Column_Mural_Large8", _folder)
if a: placed += 1
else: skipped += 1

# Batch 16: StaticMesh'Suburb_Stairs_Trim_3M_B' (38 instances)
_mesh_path = "/Game/Art/Assets/Kits/Architecture/Suburbs/Suburb_Stairs_Trim_3M_B"
_materials = ['/Game/Art/Assets/Kits/Architecture/Suburbs/Materials/Suburb_Stairs_Trim/MI_Suburb_Stairs_Trim_3M']
_folder = "Reconstruction/BD_BB_Sandbox_DwarfHall_Voxels/Meshes"
a = spawn_static_mesh(_mesh_path, _materials, (3083.561, 6099.8604, 2299.9685), (0.0, -89.99999818714215, 0.0), (1.169843, 1.0, 1.0), "Suburb_Stairs_Trim_3M2_201", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5816.4355, 2850.0, 2300.0007), (0.0, 90.00005166594045, -0.0), (1.169843, 1.0, 1.0), "Suburb_Stairs_Trim_3M2_4005", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (966.43555, 2850.0, 2300.0007), (0.0, 90.00005166594045, -0.0), (1.169843, 1.0, 1.0), "Suburb_Stairs_Trim_3M2_4073", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (633.5651, 3549.9868, 2299.965), (0.0, -89.99999818714215, 0.0), (1.169843, 1.0, 1.0), "Suburb_Stairs_Trim_3M2_4090", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5483.3203, 2149.9546, 2299.965), (0.0, -89.99999818714215, 0.0), (1.169843, 1.0, 1.0), "Suburb_Stairs_Trim_3M2_4192", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3418.4812, 150.00012, 2300.0007), (0.0, 90.00005166594045, -0.0), (1.169843, 1.0, 1.0), "Suburb_Stairs_Trim_3M2_4347", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (883.5899, 4949.9355, 2299.965), (0.0, -89.99999818714215, 0.0), (1.169843, 1.0, 1.0), "Suburb_Stairs_Trim_3M2_5117", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1216.4355, 4250.0, 2300.0007), (0.0, 90.00005166594045, -0.0), (1.169843, 1.0, 1.0), "Suburb_Stairs_Trim_3M2_5137", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5483.3203, 3549.9192, 2299.965), (0.0, -89.99999818714215, 0.0), (1.169843, 1.0, 1.0), "Suburb_Stairs_Trim_3M2_5197", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4616.4355, 4250.0, 2300.0007), (0.0, 90.00005166594045, -0.0), (1.169843, 1.0, 1.0), "Suburb_Stairs_Trim_3M2_5217", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4283.5903, 4949.999, 2299.965), (0.0, -89.99999818714215, 0.0), (1.169843, 1.0, 1.0), "Suburb_Stairs_Trim_3M2_5237", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2216.4375, 5399.9995, 2300.0007), (0.0, 90.00002735739477, -0.0), (1.169843, 1.0, 1.0), "Suburb_Stairs_Trim_3M2_5297", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1216.4395, 5399.9995, 2300.0007), (0.0, 90.00002735739477, -0.0), (1.169843, 1.0, 1.0), "Suburb_Stairs_Trim_3M2_5317", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3416.4375, 5649.999, 2300.0007), (0.0, 90.00002735739477, -0.0), (1.169843, 1.0, 1.0), "Suburb_Stairs_Trim_3M2_5337", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3083.5938, 749.9949, 2299.965), (0.0, -89.99999818714215, 0.0), (1.169843, 1.0, 1.0), "Suburb_Stairs_Trim_3M2_5417", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2216.4355, 1450.0001, 2300.0007), (0.0, 90.00005166594045, -0.0), (1.169843, 1.0, 1.0), "Suburb_Stairs_Trim_3M2_5437", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1883.5903, 2149.9868, 2299.965), (0.0, -89.99999818714215, 0.0), (1.169843, 1.0, 1.0), "Suburb_Stairs_Trim_3M2_5457", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1883.5903, 6099.9297, 2299.9666), (0.0, -89.99999818714215, 0.0), (1.169843, 1.0, 1.0), "Suburb_Stairs_Trim_3M2_5537", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (883.5897, 6099.996, 2299.9666), (0.0, -89.99999818714215, 0.0), (1.169843, 1.0, 1.0), "Suburb_Stairs_Trim_3M2_5557", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3415.478, 6100.003, 2299.9685), (0.0, -89.99991067642716, 0.0), (1.169843, 1.0, 1.0), "Suburb_Stairs_Trim_3M3_202", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5484.5254, 2850.0, 2300.0007), (0.0, 89.99995929348692, -0.0), (1.169843, 1.0, 1.0), "Suburb_Stairs_Trim_3M3_4006", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (634.52563, 2850.0, 2300.0007), (0.0, 89.99995929348692, -0.0), (1.169843, 1.0, 1.0), "Suburb_Stairs_Trim_3M3_4074", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (965.48065, 3549.987, 2299.965), (0.0, -89.99991067642716, 0.0), (1.169843, 1.0, 1.0), "Suburb_Stairs_Trim_3M3_4091", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5815.204, 2149.9868, 2299.965), (0.0, -89.99991067642716, 0.0), (1.169843, 1.0, 1.0), "Suburb_Stairs_Trim_3M3_4193", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3086.5713, 150.0, 2300.0007), (0.0, 89.99995929348692, -0.0), (1.169843, 1.0, 1.0), "Suburb_Stairs_Trim_3M3_4348", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1215.4886, 4950.0, 2299.965), (0.0, -89.99991067642716, 0.0), (1.169843, 1.0, 1.0), "Suburb_Stairs_Trim_3M3_5118", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (884.52563, 4250.0, 2300.0007), (0.0, 89.99995929348692, -0.0), (1.169843, 1.0, 1.0), "Suburb_Stairs_Trim_3M3_5138", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5815.204, 3549.987, 2299.965), (0.0, -89.99991067642716, 0.0), (1.169843, 1.0, 1.0), "Suburb_Stairs_Trim_3M3_5198", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4284.5254, 4250.0, 2300.0007), (0.0, 89.99995929348692, -0.0), (1.169843, 1.0, 1.0), "Suburb_Stairs_Trim_3M3_5218", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4615.3394, 4950.0, 2299.965), (0.0, -89.99991067642716, 0.0), (1.169843, 1.0, 1.0), "Suburb_Stairs_Trim_3M3_5238", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1884.5293, 5399.9995, 2300.0007), (0.0, 89.99993822608693, -0.0), (1.169843, 1.0, 1.0), "Suburb_Stairs_Trim_3M3_5298", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (884.5293, 5399.9995, 2300.0007), (0.0, 89.99993822608693, -0.0), (1.169843, 1.0, 1.0), "Suburb_Stairs_Trim_3M3_5318", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3084.5276, 5649.999, 2300.0007), (0.0, 89.99993822608693, -0.0), (1.169843, 1.0, 1.0), "Suburb_Stairs_Trim_3M3_5338", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3415.5103, 749.98706, 2299.965), (0.0, -89.99991067642716, 0.0), (1.169843, 1.0, 1.0), "Suburb_Stairs_Trim_3M3_5418", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1884.5256, 1450.0, 2300.0007), (0.0, 89.99995929348692, -0.0), (1.169843, 1.0, 1.0), "Suburb_Stairs_Trim_3M3_5438", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2215.4746, 2149.987, 2299.965), (0.0, -89.99991067642716, 0.0), (1.169843, 1.0, 1.0), "Suburb_Stairs_Trim_3M3_5458", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2215.459, 6100.0654, 2299.9666), (0.0, -89.99991067642716, 0.0), (1.169843, 1.0, 1.0), "Suburb_Stairs_Trim_3M3_5538", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1215.4807, 6100.0625, 2299.9666), (0.0, -89.99991067642716, 0.0), (1.169843, 1.0, 1.0), "Suburb_Stairs_Trim_3M3_5558", _folder)
if a: placed += 1
else: skipped += 1

# Batch 17: StaticMesh'Suburb_Stairs_Trim_Angle_B' (56 instances)
_mesh_path = "/Game/Art/Assets/Kits/Architecture/Suburbs/Suburb_Stairs_Trim_Angle_B"
_materials = ['/Game/Art/Assets/Kits/Architecture/Suburbs/Materials/Suburb_Stairs_Trim/MI_Suburbs_Stairs_Trim_Angle']
_folder = "Reconstruction/BD_BB_Sandbox_DwarfHall_Voxels/Meshes"
a = spawn_static_mesh(_mesh_path, _materials, (3068.9834, 6099.8594, 2299.9685), (0.0, -89.99993822608693, 0.0), (1.0, 1.0, 1.0), "Suburb_Stairs_Trim_Angle_B_207", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2231.0132, 2850.0002, 2300.0007), (0.0, 89.99995929348692, -0.0), (1.0, 1.0, 1.0), "Suburb_Stairs_Trim_Angle_B_3929", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3431.0132, 2850.0002, 2300.0007), (0.0, 89.99995929348692, -0.0), (1.0, 1.0, 1.0), "Suburb_Stairs_Trim_Angle_B_3977", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4631.013, 2850.0002, 2300.0007), (0.0, 89.99995929348692, -0.0), (1.0, 1.0, 1.0), "Suburb_Stairs_Trim_Angle_B_3994", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5831.013, 2850.0002, 2300.0007), (0.0, 89.99995929348692, -0.0), (1.0, 1.0, 1.0), "Suburb_Stairs_Trim_Angle_B_4011", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4269.012, 3549.9192, 2299.965), (0.0, -89.99993822608693, 0.0), (1.0, 1.0, 1.0), "Suburb_Stairs_Trim_Angle_B_4028", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3069.0498, 3549.9492, 2299.9631), (0.0, -89.99993822608693, 0.0), (1.0, 1.0, 1.0), "Suburb_Stairs_Trim_Angle_B_4045", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1869.0127, 3549.9512, 2299.965), (0.0, -89.99993822608693, 0.0), (1.0, 1.0, 1.0), "Suburb_Stairs_Trim_Angle_B_4062", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (981.0132, 2850.0002, 2300.0007), (0.0, 89.99995929348692, -0.0), (1.0, 1.0, 1.0), "Suburb_Stairs_Trim_Angle_B_4079", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (618.9875, 3549.9868, 2299.965), (0.0, -89.99993822608693, 0.0), (1.0, 1.0, 1.0), "Suburb_Stairs_Trim_Angle_B_4096", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3431.0132, 1450.0002, 2300.0007), (0.0, 89.99995929348692, -0.0), (1.0, 1.0, 1.0), "Suburb_Stairs_Trim_Angle_B_4147", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3069.0479, 2149.9866, 2299.965), (0.0, -89.99993822608693, 0.0), (1.0, 1.0, 1.0), "Suburb_Stairs_Trim_Angle_B_4164", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5468.742, 2149.9546, 2299.965), (0.0, -89.99993822608693, 0.0), (1.0, 1.0, 1.0), "Suburb_Stairs_Trim_Angle_B_4198", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3431.0132, 4250.0, 2300.0007), (0.0, 89.99995929348692, -0.0), (1.0, 1.0, 1.0), "Suburb_Stairs_Trim_Angle_B_4215", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3069.0195, 4949.793, 2299.9617), (0.0, -89.99993822608693, 0.0), (1.0, 1.0, 1.0), "Suburb_Stairs_Trim_Angle_B_4232", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (869.01227, 4949.9346, 2299.965), (0.0, -89.99993822608693, 0.0), (1.0, 1.0, 1.0), "Suburb_Stairs_Trim_Angle_B_5123", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1231.0132, 4250.0, 2300.0007), (0.0, 89.99995929348692, -0.0), (1.0, 1.0, 1.0), "Suburb_Stairs_Trim_Angle_B_5143", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5468.742, 3549.9192, 2299.965), (0.0, -89.99993822608693, 0.0), (1.0, 1.0, 1.0), "Suburb_Stairs_Trim_Angle_B_5203", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4631.013, 4250.0, 2300.0007), (0.0, 89.99995929348692, -0.0), (1.0, 1.0, 1.0), "Suburb_Stairs_Trim_Angle_B_5223", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4269.012, 4949.999, 2299.965), (0.0, -89.99993822608693, 0.0), (1.0, 1.0, 1.0), "Suburb_Stairs_Trim_Angle_B_5243", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2231.0151, 5399.9995, 2300.0007), (0.0, 89.99993822608693, -0.0), (1.0, 1.0, 1.0), "Suburb_Stairs_Trim_Angle_B_5303", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1231.0171, 5399.9995, 2300.0007), (0.0, 89.99993822608693, -0.0), (1.0, 1.0, 1.0), "Suburb_Stairs_Trim_Angle_B_5323", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3431.0151, 5649.999, 2300.0007), (0.0, 89.99993822608693, -0.0), (1.0, 1.0, 1.0), "Suburb_Stairs_Trim_Angle_B_5343", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3069.016, 749.99475, 2299.965), (0.0, -89.99993822608693, 0.0), (1.0, 1.0, 1.0), "Suburb_Stairs_Trim_Angle_B_5423", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2231.0132, 1450.0002, 2300.0007), (0.0, 89.99995929348692, -0.0), (1.0, 1.0, 1.0), "Suburb_Stairs_Trim_Angle_B_5443", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1869.0127, 2149.9868, 2299.965), (0.0, -89.99993822608693, 0.0), (1.0, 1.0, 1.0), "Suburb_Stairs_Trim_Angle_B_5463", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1869.0127, 6099.9297, 2299.9666), (0.0, -89.99993822608693, 0.0), (1.0, 1.0, 1.0), "Suburb_Stairs_Trim_Angle_B_5543", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (869.0121, 6099.996, 2299.9666), (0.0, -89.99993822608693, 0.0), (1.0, 1.0, 1.0), "Suburb_Stairs_Trim_Angle_B_5563", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3400.0024, 6100.003, 2299.9685), (0.0, -89.99999818714215, 0.0), (1.0, 1.0, 1.0), "Suburb_Stairs_Trim_Angle_B2_208", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1900.0012, 2850.0, 2300.0007), (0.0, 89.99993822608693, -0.0), (1.0, 1.0, 1.0), "Suburb_Stairs_Trim_Angle_B2_3930", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3100.0012, 2850.0, 2300.0007), (0.0, 89.99993822608693, -0.0), (1.0, 1.0, 1.0), "Suburb_Stairs_Trim_Angle_B2_3978", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4300.001, 2850.0, 2300.0007), (0.0, 89.99993822608693, -0.0), (1.0, 1.0, 1.0), "Suburb_Stairs_Trim_Angle_B2_3995", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5500.001, 2850.0, 2300.0007), (0.0, 89.99993822608693, -0.0), (1.0, 1.0, 1.0), "Suburb_Stairs_Trim_Angle_B2_4012", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4599.864, 3550.0188, 2299.965), (0.0, -89.99999818714215, 0.0), (1.0, 1.0, 1.0), "Suburb_Stairs_Trim_Angle_B2_4029", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3400.0684, 3549.9492, 2299.9631), (0.0, -89.99999818714215, 0.0), (1.0, 1.0, 1.0), "Suburb_Stairs_Trim_Angle_B2_4046", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2199.983, 3549.9512, 2299.965), (0.0, -89.99999818714215, 0.0), (1.0, 1.0, 1.0), "Suburb_Stairs_Trim_Angle_B2_4063", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (650.0012, 2850.0, 2300.0007), (0.0, 89.99993822608693, -0.0), (1.0, 1.0, 1.0), "Suburb_Stairs_Trim_Angle_B2_4080", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (949.98816, 3549.9868, 2299.965), (0.0, -89.99999818714215, 0.0), (1.0, 1.0, 1.0), "Suburb_Stairs_Trim_Angle_B2_4097", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3100.0012, 1450.0001, 2300.0007), (0.0, 89.99993822608693, -0.0), (1.0, 1.0, 1.0), "Suburb_Stairs_Trim_Angle_B2_4148", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3400.0664, 2149.9194, 2299.965), (0.0, -89.99999818714215, 0.0), (1.0, 1.0, 1.0), "Suburb_Stairs_Trim_Angle_B2_4165", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5799.7285, 2149.987, 2299.965), (0.0, -89.99999818714215, 0.0), (1.0, 1.0, 1.0), "Suburb_Stairs_Trim_Angle_B2_4199", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3100.0012, 4250.0, 2300.0007), (0.0, 89.99993822608693, -0.0), (1.0, 1.0, 1.0), "Suburb_Stairs_Trim_Angle_B2_4216", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3400.038, 4949.9355, 2299.9617), (0.0, -89.99999818714215, 0.0), (1.0, 1.0, 1.0), "Suburb_Stairs_Trim_Angle_B2_4233", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1199.9961, 4950.0, 2299.965), (0.0, -89.99999818714215, 0.0), (1.0, 1.0, 1.0), "Suburb_Stairs_Trim_Angle_B2_5124", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (900.0012, 4250.0, 2300.0007), (0.0, 89.99993822608693, -0.0), (1.0, 1.0, 1.0), "Suburb_Stairs_Trim_Angle_B2_5144", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5799.7285, 3550.0188, 2299.965), (0.0, -89.99999818714215, 0.0), (1.0, 1.0, 1.0), "Suburb_Stairs_Trim_Angle_B2_5204", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4300.001, 4250.0, 2300.0007), (0.0, 89.99993822608693, -0.0), (1.0, 1.0, 1.0), "Suburb_Stairs_Trim_Angle_B2_5224", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4599.864, 4950.0, 2299.965), (0.0, -89.99999818714215, 0.0), (1.0, 1.0, 1.0), "Suburb_Stairs_Trim_Angle_B2_5244", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1900.0049, 5399.9995, 2300.0007), (0.0, 89.99993012324896, -0.0), (1.0, 1.0, 1.0), "Suburb_Stairs_Trim_Angle_B2_5304", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (900.0049, 5399.9995, 2300.0007), (0.0, 89.99993012324896, -0.0), (1.0, 1.0, 1.0), "Suburb_Stairs_Trim_Angle_B2_5324", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3100.0032, 5649.999, 2300.0007), (0.0, 89.99993012324896, -0.0), (1.0, 1.0, 1.0), "Suburb_Stairs_Trim_Angle_B2_5344", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3400.0347, 749.9949, 2299.965), (0.0, -89.99999818714215, 0.0), (1.0, 1.0, 1.0), "Suburb_Stairs_Trim_Angle_B2_5424", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1900.0012, 1450.0001, 2300.0007), (0.0, 89.99993822608693, -0.0), (1.0, 1.0, 1.0), "Suburb_Stairs_Trim_Angle_B2_5444", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2199.999, 2149.9868, 2299.965), (0.0, -89.99999818714215, 0.0), (1.0, 1.0, 1.0), "Suburb_Stairs_Trim_Angle_B2_5464", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2199.9834, 6100.0654, 2299.9666), (0.0, -89.99999818714215, 0.0), (1.0, 1.0, 1.0), "Suburb_Stairs_Trim_Angle_B2_5544", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1199.9883, 6100.0625, 2299.9666), (0.0, -89.99999818714215, 0.0), (1.0, 1.0, 1.0), "Suburb_Stairs_Trim_Angle_B2_5564", _folder)
if a: placed += 1
else: skipped += 1

# Batch 18: StaticMesh'Suburbs_Column_Large_A_Base' (167 instances)
_mesh_path = "/Game/Art/Assets/Kits/Architecture/Suburbs/Suburbs_Column_Large_A_Base"
_materials = ['/Game/Art/Assets/Kits/Architecture/Suburbs/Materials/Suburbs_Column_Large/MI_Suburbs_Column_Large_A_Base']
_folder = "Reconstruction/BD_BB_Sandbox_DwarfHall_Voxels/Meshes"
a = spawn_static_mesh(_mesh_path, _materials, (1550.0, 2399.9985, 900.0), (0.0, -89.9995168790839, 0.0), (1.0, 1.0, 1.0), "Suburbs_Column_Large_A_Base25_0", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3750.0, 1200.0013, 900.0), (0.0, 90.00055404374588, -0.0), (1.0, 1.0, 1.0), "Suburbs_Column_Large_A_Base25_18", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4950.0, 2600.0017, 900.0), (0.0, 90.00055404374588, -0.0), (1.0, 1.0, 1.0), "Suburbs_Column_Large_A_Base25_31", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3749.9983, 1000.0, 900.0), (0.0, -179.9993852828675, 0.0), (1.0, 1.0, 1.0), "Suburbs_Column_Large_A_Base25_36", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3750.0, 2600.0015, 900.0), (0.0, 90.00055404374588, -0.0), (1.0, 1.0, 1.0), "Suburbs_Column_Large_A_Base25_184", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3749.9983, 2400.0, 900.0), (0.0, -179.9993852828675, 0.0), (1.0, 1.0, 1.0), "Suburbs_Column_Large_A_Base25_202", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3950.0017, 2600.0, 900.0), (0.0, 0.0005020189737896272, -0.0), (1.0, 1.0, 1.0), "Suburbs_Column_Large_A_Base25_220", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5150.002, 2600.0, 900.0), (0.0, 0.0005020189737896272, -0.0), (1.0, 1.0, 1.0), "Suburbs_Column_Large_A_Base25_295", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1550.0015, 1199.9998, 900.0), (0.0, 0.0005020189737896272, -0.0), (1.0, 1.0, 1.0), "Suburbs_Column_Large_A_Base25_367", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2550.0, 1200.002, 900.0), (0.0, 90.00055404374588, -0.0), (1.0, 1.0, 1.0), "Suburbs_Column_Large_A_Base25_403", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2750.0015, 1199.9998, 900.0), (0.0, 0.0005020189737896272, -0.0), (1.0, 1.0, 1.0), "Suburbs_Column_Large_A_Base25_441", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1349.9995, 2600.0017, 900.0), (0.0, 90.00055404374588, -0.0), (1.0, 1.0, 1.0), "Suburbs_Column_Large_A_Base25_477", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1550.0012, 2600.0, 900.0), (0.0, 0.0005020189737896272, -0.0), (1.0, 1.0, 1.0), "Suburbs_Column_Large_A_Base25_515", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2550.0, 2600.0017, 900.0), (0.0, 90.00055404374588, -0.0), (1.0, 1.0, 1.0), "Suburbs_Column_Large_A_Base25_551", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2549.998, 2400.0002, 900.0), (0.0, -179.9993852828675, 0.0), (1.0, 1.0, 1.0), "Suburbs_Column_Large_A_Base25_569", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2750.0015, 2599.9998, 900.0), (0.0, 0.0005020189737896272, -0.0), (1.0, 1.0, 1.0), "Suburbs_Column_Large_A_Base25_587", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3750.0, 4000.0017, 900.0), (0.0, 90.00055404374588, -0.0), (1.0, 1.0, 1.0), "Suburbs_Column_Large_A_Base25_623", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3749.9983, 3800.0, 900.0), (0.0, -179.9993852828675, 0.0), (1.0, 1.0, 1.0), "Suburbs_Column_Large_A_Base25_641", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3950.0017, 4000.0, 900.0), (0.0, 0.0005020189737896272, -0.0), (1.0, 1.0, 1.0), "Suburbs_Column_Large_A_Base25_659", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3950.041, 3799.9983, 900.0), (0.0, -89.99938723407456, 0.0), (1.0, 1.0, 1.0), "Suburbs_Column_Large_A_Base25_677", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4950.0, 4000.0017, 900.0), (0.0, 90.00055404374588, -0.0), (1.0, 1.0, 1.0), "Suburbs_Column_Large_A_Base25_695", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5150.002, 4000.0, 900.0), (0.0, 0.0005020189737896272, -0.0), (1.0, 1.0, 1.0), "Suburbs_Column_Large_A_Base25_731", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5150.041, 3800.001, 900.0), (0.0, -89.99938723407456, 0.0), (1.0, 1.0, 1.0), "Suburbs_Column_Large_A_Base25_749", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3750.0, 5400.0024, 900.0), (0.0, 90.00055404374588, -0.0), (1.0, 1.0, 1.0), "Suburbs_Column_Large_A_Base25_767", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3749.9983, 5200.0, 900.0), (0.0, -179.9993852828675, 0.0), (1.0, 1.0, 1.0), "Suburbs_Column_Large_A_Base25_785", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4949.998, 5200.0, 900.0), (0.0, -179.9993852828675, 0.0), (1.0, 1.0, 1.0), "Suburbs_Column_Large_A_Base25_857", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1349.9978, 3799.9998, 900.0), (0.0, -179.9993852828675, 0.0), (1.0, 1.0, 1.0), "Suburbs_Column_Large_A_Base25_929", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1550.002, 4000.0002, 900.0), (0.0, 0.0005020189737896272, -0.0), (1.0, 1.0, 1.0), "Suburbs_Column_Large_A_Base25_947", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2549.998, 3800.0002, 900.0), (0.0, -179.9993852828675, 0.0), (1.0, 1.0, 1.0), "Suburbs_Column_Large_A_Base25_1001", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2750.0017, 4000.0, 900.0), (0.0, 0.0005020189737896272, -0.0), (1.0, 1.0, 1.0), "Suburbs_Column_Large_A_Base25_1019", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2550.0, 5400.003, 900.0), (0.0, 90.00055404374588, -0.0), (1.0, 1.0, 1.0), "Suburbs_Column_Large_A_Base25_1127", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2549.9983, 5200.0, 900.0), (0.0, -179.9993852828675, 0.0), (1.0, 1.0, 1.0), "Suburbs_Column_Large_A_Base25_1145", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2749.9995, 2399.998, 900.0), (0.0, -89.9995168790839, 0.0), (1.0, 1.0, 1.0), "Suburbs_Column_Large_A_Base25_1162", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2750.0015, 5400.0005, 900.0), (0.0, 0.0005020189737896272, -0.0), (1.0, 1.0, 1.0), "Suburbs_Column_Large_A_Base25_1163", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3950.0, 2399.9983, 900.0), (0.0, -89.9995168790839, 0.0), (1.0, 1.0, 1.0), "Suburbs_Column_Large_A_Base25_1185", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2749.9998, 999.9988, 900.0), (0.0, -89.99938723407456, 0.0), (1.0, 1.0, 1.0), "Suburbs_Column_Large_A_Base25_1249", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2749.9995, 3799.9983, 900.0), (0.0, -89.99954442862955, 0.0), (1.0, 1.0, 1.0), "Suburbs_Column_Large_A_Base25_3280", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2750.0, 5199.998, 900.0), (0.0, -89.9995168790839, 0.0), (1.0, 1.0, 1.0), "Suburbs_Column_Large_A_Base25_3299", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3950.0, 5199.998, 900.0), (0.0, -89.9995168790839, 0.0), (1.0, 1.0, 1.0), "Suburbs_Column_Large_A_Base25_3318", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4950.039, 3800.0, 900.0), (0.0, -179.99950822623498, 0.0), (1.0, 1.0, 1.0), "Suburbs_Column_Large_A_Base25_3337", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1550.0, 2399.9985, 900.0), (0.0, 0.0007205849547276367, -0.0), (1.0, 1.0, 1.0), "Suburbs_Column_Large_A_Base26_1", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3750.0, 1200.0013, 900.0), (0.0, -179.99922135866876, 0.0), (1.0, 1.0, 1.0), "Suburbs_Column_Large_A_Base26_19", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4950.0, 2600.0017, 900.0), (0.0, -179.99922135866876, 0.0), (1.0, 1.0, 1.0), "Suburbs_Column_Large_A_Base26_32", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3749.9983, 1000.0, 900.0), (0.0, -89.99920897263199, 0.0), (1.0, 1.0, 1.0), "Suburbs_Column_Large_A_Base26_37", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3750.0, 2600.0015, 900.0), (0.0, -179.99922135866876, 0.0), (1.0, 1.0, 1.0), "Suburbs_Column_Large_A_Base26_185", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3749.9983, 2400.0, 900.0), (0.0, -89.99920897263199, 0.0), (1.0, 1.0, 1.0), "Suburbs_Column_Large_A_Base26_203", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3950.0017, 2600.0, 900.0), (0.0, 90.00073230747108, -0.0), (1.0, 1.0, 1.0), "Suburbs_Column_Large_A_Base26_221", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5150.002, 2600.0, 900.0), (0.0, 90.00073230747108, -0.0), (1.0, 1.0, 1.0), "Suburbs_Column_Large_A_Base26_296", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1550.0015, 1199.9998, 900.0), (0.0, 90.00073230747108, -0.0), (1.0, 1.0, 1.0), "Suburbs_Column_Large_A_Base26_368", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2550.0, 1200.002, 900.0), (0.0, -179.99922135866876, 0.0), (1.0, 1.0, 1.0), "Suburbs_Column_Large_A_Base26_404", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2750.0015, 1199.9998, 900.0), (0.0, 90.00073230747108, -0.0), (1.0, 1.0, 1.0), "Suburbs_Column_Large_A_Base26_442", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1349.9995, 2600.0017, 900.0), (0.0, -179.99922135866876, 0.0), (1.0, 1.0, 1.0), "Suburbs_Column_Large_A_Base26_478", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1550.0012, 2600.0, 900.0), (0.0, 90.00073230747108, -0.0), (1.0, 1.0, 1.0), "Suburbs_Column_Large_A_Base26_516", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2550.0, 2600.0017, 900.0), (0.0, -179.99922135866876, 0.0), (1.0, 1.0, 1.0), "Suburbs_Column_Large_A_Base26_552", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2549.998, 2400.0002, 900.0), (0.0, -89.99920897263199, 0.0), (1.0, 1.0, 1.0), "Suburbs_Column_Large_A_Base26_570", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2750.0015, 2599.9998, 900.0), (0.0, 90.00073230747108, -0.0), (1.0, 1.0, 1.0), "Suburbs_Column_Large_A_Base26_588", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3750.0, 4000.0017, 900.0), (0.0, -179.99922135866876, 0.0), (1.0, 1.0, 1.0), "Suburbs_Column_Large_A_Base26_624", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3749.9983, 3800.0, 900.0), (0.0, -89.99920897263199, 0.0), (1.0, 1.0, 1.0), "Suburbs_Column_Large_A_Base26_642", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3950.0017, 4000.0, 900.0), (0.0, 90.00073230747108, -0.0), (1.0, 1.0, 1.0), "Suburbs_Column_Large_A_Base26_660", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3950.041, 3799.9983, 900.0), (0.0, 0.0007888867951248759, -0.0), (1.0, 1.0, 1.0), "Suburbs_Column_Large_A_Base26_678", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4950.0, 4000.0017, 900.0), (0.0, -179.99922135866876, 0.0), (1.0, 1.0, 1.0), "Suburbs_Column_Large_A_Base26_696", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5150.002, 4000.0, 900.0), (0.0, 90.00073230747108, -0.0), (1.0, 1.0, 1.0), "Suburbs_Column_Large_A_Base26_732", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5150.041, 3800.001, 900.0), (0.0, 0.000829868059791934, -0.0), (1.0, 1.0, 1.0), "Suburbs_Column_Large_A_Base26_750", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3750.0, 5400.0024, 900.0), (0.0, -179.99922135866876, 0.0), (1.0, 1.0, 1.0), "Suburbs_Column_Large_A_Base26_768", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3749.9983, 5200.0, 900.0), (0.0, -89.99920897263199, 0.0), (1.0, 1.0, 1.0), "Suburbs_Column_Large_A_Base26_786", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4949.998, 5200.0, 900.0), (0.0, -89.99920897263199, 0.0), (1.0, 1.0, 1.0), "Suburbs_Column_Large_A_Base26_858", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1349.9978, 3799.9998, 900.0), (0.0, -89.99920897263199, 0.0), (1.0, 1.0, 1.0), "Suburbs_Column_Large_A_Base26_930", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1550.002, 4000.0002, 900.0), (0.0, 90.00073230747108, -0.0), (1.0, 1.0, 1.0), "Suburbs_Column_Large_A_Base26_948", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2549.998, 3800.0002, 900.0), (0.0, -89.99920897263199, 0.0), (1.0, 1.0, 1.0), "Suburbs_Column_Large_A_Base26_1002", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2750.0017, 4000.0, 900.0), (0.0, 90.00073230747108, -0.0), (1.0, 1.0, 1.0), "Suburbs_Column_Large_A_Base26_1020", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2550.0, 5400.003, 900.0), (0.0, -179.99922135866876, 0.0), (1.0, 1.0, 1.0), "Suburbs_Column_Large_A_Base26_1128", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2549.9983, 5200.0, 900.0), (0.0, -89.99920897263199, 0.0), (1.0, 1.0, 1.0), "Suburbs_Column_Large_A_Base26_1146", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2749.9995, 2399.998, 900.0), (0.0, 0.0007205849547276367, -0.0), (1.0, 1.0, 1.0), "Suburbs_Column_Large_A_Base26_1163", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2750.0015, 5400.0005, 900.0), (0.0, 90.00073230747108, -0.0), (1.0, 1.0, 1.0), "Suburbs_Column_Large_A_Base26_1164", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3950.0, 2399.9983, 900.0), (0.0, 0.0007035094373327111, -0.0), (1.0, 1.0, 1.0), "Suburbs_Column_Large_A_Base26_1186", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2749.9998, 999.9988, 900.0), (0.0, 0.000829868059791934, -0.0), (1.0, 1.0, 1.0), "Suburbs_Column_Large_A_Base26_1250", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2749.9995, 3799.9983, 900.0), (0.0, 0.0006898490577942835, -0.0), (1.0, 1.0, 1.0), "Suburbs_Column_Large_A_Base26_3281", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2750.0, 5199.998, 900.0), (0.0, 0.0007035094373327111, -0.0), (1.0, 1.0, 1.0), "Suburbs_Column_Large_A_Base26_3300", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3950.0, 5199.998, 900.0), (0.0, 0.0007035094373327111, -0.0), (1.0, 1.0, 1.0), "Suburbs_Column_Large_A_Base26_3319", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4950.039, 3800.0, 900.0), (0.0, -89.9992640716205, 0.0), (1.0, 1.0, 1.0), "Suburbs_Column_Large_A_Base26_3338", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1550.0, 2399.9985, 900.0), (0.0, 90.00019103504636, -0.0), (1.0, 1.0, 1.0), "Suburbs_Column_Large_A_Base27_2", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3750.0, 1200.0013, 900.0), (0.0, -89.99975996369572, 0.0), (1.0, 1.0, 1.0), "Suburbs_Column_Large_A_Base27_20", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4950.0, 2600.0017, 900.0), (0.0, -89.99975996369572, 0.0), (1.0, 1.0, 1.0), "Suburbs_Column_Large_A_Base27_33", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3749.9983, 1000.0, 900.0), (0.0, 0.0002697924758114751, -0.0), (1.0, 1.0, 1.0), "Suburbs_Column_Large_A_Base27_38", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3750.0, 2600.0015, 900.0), (0.0, -89.99975996369572, 0.0), (1.0, 1.0, 1.0), "Suburbs_Column_Large_A_Base27_186", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3749.9983, 2400.0, 900.0), (0.0, 0.0002697924758114751, -0.0), (1.0, 1.0, 1.0), "Suburbs_Column_Large_A_Base27_204", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3950.0017, 2600.0, 900.0), (0.0, -179.99978826413437, 0.0), (1.0, 1.0, 1.0), "Suburbs_Column_Large_A_Base27_222", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5150.002, 2600.0, 900.0), (0.0, -179.99978826413437, 0.0), (1.0, 1.0, 1.0), "Suburbs_Column_Large_A_Base27_297", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1550.0015, 1199.9998, 900.0), (0.0, -179.99978826413437, 0.0), (1.0, 1.0, 1.0), "Suburbs_Column_Large_A_Base27_369", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2550.0, 1200.002, 900.0), (0.0, -89.99975996369572, 0.0), (1.0, 1.0, 1.0), "Suburbs_Column_Large_A_Base27_405", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2750.0015, 1199.9998, 900.0), (0.0, -179.99978826413437, 0.0), (1.0, 1.0, 1.0), "Suburbs_Column_Large_A_Base27_443", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1349.9995, 2600.0017, 900.0), (0.0, -89.99975996369572, 0.0), (1.0, 1.0, 1.0), "Suburbs_Column_Large_A_Base27_479", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1550.0012, 2600.0, 900.0), (0.0, -179.99978826413437, 0.0), (1.0, 1.0, 1.0), "Suburbs_Column_Large_A_Base27_517", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2550.0, 2600.0017, 900.0), (0.0, -89.99975996369572, 0.0), (1.0, 1.0, 1.0), "Suburbs_Column_Large_A_Base27_553", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2549.998, 2400.0002, 900.0), (0.0, 0.0002697924758114751, -0.0), (1.0, 1.0, 1.0), "Suburbs_Column_Large_A_Base27_571", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2750.0015, 2599.9998, 900.0), (0.0, -179.99978826413437, 0.0), (1.0, 1.0, 1.0), "Suburbs_Column_Large_A_Base27_589", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3750.0, 4000.0017, 900.0), (0.0, -89.99975996369572, 0.0), (1.0, 1.0, 1.0), "Suburbs_Column_Large_A_Base27_625", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3749.9983, 3800.0, 900.0), (0.0, 0.0002697924758114751, -0.0), (1.0, 1.0, 1.0), "Suburbs_Column_Large_A_Base27_643", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3950.0017, 4000.0, 900.0), (0.0, -179.99978826413437, 0.0), (1.0, 1.0, 1.0), "Suburbs_Column_Large_A_Base27_661", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3950.041, 3799.9983, 900.0), (0.0, 90.00022020536449, -0.0), (1.0, 1.0, 1.0), "Suburbs_Column_Large_A_Base27_679", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4950.0, 4000.0017, 900.0), (0.0, -89.99975996369572, 0.0), (1.0, 1.0, 1.0), "Suburbs_Column_Large_A_Base27_697", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5150.002, 4000.0, 900.0), (0.0, -179.99978826413437, 0.0), (1.0, 1.0, 1.0), "Suburbs_Column_Large_A_Base27_733", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5150.041, 3800.001, 900.0), (0.0, 90.0002947517003, -0.0), (1.0, 1.0, 1.0), "Suburbs_Column_Large_A_Base27_751", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3750.0, 5400.0024, 900.0), (0.0, -89.99975996369572, 0.0), (1.0, 1.0, 1.0), "Suburbs_Column_Large_A_Base27_769", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3749.9983, 5200.0, 900.0), (0.0, 0.0002697924758114751, -0.0), (1.0, 1.0, 1.0), "Suburbs_Column_Large_A_Base27_787", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4949.998, 5200.0, 900.0), (0.0, 0.0002697924758114751, -0.0), (1.0, 1.0, 1.0), "Suburbs_Column_Large_A_Base27_859", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1349.9978, 3799.9998, 900.0), (0.0, 0.0002697924758114751, -0.0), (1.0, 1.0, 1.0), "Suburbs_Column_Large_A_Base27_931", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1550.002, 4000.0002, 900.0), (0.0, -179.99978826413437, 0.0), (1.0, 1.0, 1.0), "Suburbs_Column_Large_A_Base27_949", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2549.998, 3800.0002, 900.0), (0.0, 0.0002697924758114751, -0.0), (1.0, 1.0, 1.0), "Suburbs_Column_Large_A_Base27_1003", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2750.0017, 4000.0, 900.0), (0.0, -179.99978826413437, 0.0), (1.0, 1.0, 1.0), "Suburbs_Column_Large_A_Base27_1021", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2550.0, 5400.003, 900.0), (0.0, -89.99975996369572, 0.0), (1.0, 1.0, 1.0), "Suburbs_Column_Large_A_Base27_1129", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2549.9983, 5200.0, 900.0), (0.0, 0.0002697924758114751, -0.0), (1.0, 1.0, 1.0), "Suburbs_Column_Large_A_Base27_1147", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2749.9995, 2399.998, 900.0), (0.0, 90.00019103504636, -0.0), (1.0, 1.0, 1.0), "Suburbs_Column_Large_A_Base27_1164", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2750.0015, 5400.0005, 900.0), (0.0, -179.99978826413437, 0.0), (1.0, 1.0, 1.0), "Suburbs_Column_Large_A_Base27_1165", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3950.0, 2399.9983, 900.0), (0.0, 90.0001326944829, -0.0), (1.0, 1.0, 1.0), "Suburbs_Column_Large_A_Base27_1187", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2749.9998, 999.9988, 900.0), (0.0, 90.0002947517003, -0.0), (1.0, 1.0, 1.0), "Suburbs_Column_Large_A_Base27_1251", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2749.9995, 3799.9983, 900.0), (0.0, 90.0001326944829, -0.0), (1.0, 1.0, 1.0), "Suburbs_Column_Large_A_Base27_3282", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2750.0, 5199.998, 900.0), (0.0, 90.0001326944829, -0.0), (1.0, 1.0, 1.0), "Suburbs_Column_Large_A_Base27_3301", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3950.0, 5199.998, 900.0), (0.0, 90.0001326944829, -0.0), (1.0, 1.0, 1.0), "Suburbs_Column_Large_A_Base27_3320", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4950.039, 3800.0, 900.0), (0.0, 0.00020149055520549277, -0.0), (1.0, 1.0, 1.0), "Suburbs_Column_Large_A_Base27_3339", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1550.0, 2399.9985, 900.0), (0.0, -179.99953554711865, 0.0), (1.0, 1.0, 1.0), "Suburbs_Column_Large_A_Base28_3", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3750.0, 1200.0013, 900.0), (0.0, 0.00048494337618129564, -0.0), (1.0, 1.0, 1.0), "Suburbs_Column_Large_A_Base28_21", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4950.0, 2600.0017, 900.0), (0.0, 0.00048494337618129564, -0.0), (1.0, 1.0, 1.0), "Suburbs_Column_Large_A_Base28_34", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3749.9983, 1000.0, 900.0), (0.0, 90.00052163220809, -0.0), (1.0, 1.0, 1.0), "Suburbs_Column_Large_A_Base28_39", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3750.0, 2600.0015, 900.0), (0.0, 0.00048494337618129564, -0.0), (1.0, 1.0, 1.0), "Suburbs_Column_Large_A_Base28_187", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3749.9983, 2400.0, 900.0), (0.0, 90.00052163220809, -0.0), (1.0, 1.0, 1.0), "Suburbs_Column_Large_A_Base28_205", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3950.0017, 2600.0, 900.0), (0.0, -89.99957359878371, 0.0), (1.0, 1.0, 1.0), "Suburbs_Column_Large_A_Base28_223", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5150.002, 2600.0, 900.0), (0.0, -89.99957359878371, 0.0), (1.0, 1.0, 1.0), "Suburbs_Column_Large_A_Base28_298", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2550.0, 1200.002, 900.0), (0.0, 0.00048494337618129564, -0.0), (1.0, 1.0, 1.0), "Suburbs_Column_Large_A_Base28_406", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2750.0015, 1199.9998, 900.0), (0.0, -89.99957359878371, 0.0), (1.0, 1.0, 1.0), "Suburbs_Column_Large_A_Base28_444", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1349.9995, 2600.0017, 900.0), (0.0, 0.00048494337618129564, -0.0), (1.0, 1.0, 1.0), "Suburbs_Column_Large_A_Base28_480", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1550.0012, 2600.0, 900.0), (0.0, -89.99957359878371, 0.0), (1.0, 1.0, 1.0), "Suburbs_Column_Large_A_Base28_518", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2550.0, 2600.0017, 900.0), (0.0, 0.00048494337618129564, -0.0), (1.0, 1.0, 1.0), "Suburbs_Column_Large_A_Base28_554", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2549.998, 2400.0002, 900.0), (0.0, 90.00052163220809, -0.0), (1.0, 1.0, 1.0), "Suburbs_Column_Large_A_Base28_572", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2750.0015, 2599.9998, 900.0), (0.0, -89.99957359878371, 0.0), (1.0, 1.0, 1.0), "Suburbs_Column_Large_A_Base28_590", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3750.0, 4000.0017, 900.0), (0.0, 0.00048494337618129564, -0.0), (1.0, 1.0, 1.0), "Suburbs_Column_Large_A_Base28_626", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3749.9983, 3800.0, 900.0), (0.0, 90.00052163220809, -0.0), (1.0, 1.0, 1.0), "Suburbs_Column_Large_A_Base28_644", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3950.0017, 4000.0, 900.0), (0.0, -89.99957359878371, 0.0), (1.0, 1.0, 1.0), "Suburbs_Column_Large_A_Base28_662", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3950.041, 3799.9983, 900.0), (0.0, -179.99950822623498, 0.0), (1.0, 1.0, 1.0), "Suburbs_Column_Large_A_Base28_680", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4950.0, 4000.0017, 900.0), (0.0, 0.00048494337618129564, -0.0), (1.0, 1.0, 1.0), "Suburbs_Column_Large_A_Base28_698", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5150.002, 4000.0, 900.0), (0.0, -89.99957359878371, 0.0), (1.0, 1.0, 1.0), "Suburbs_Column_Large_A_Base28_734", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5150.041, 3800.001, 900.0), (0.0, -179.9994604150484, 0.0), (1.0, 1.0, 1.0), "Suburbs_Column_Large_A_Base28_752", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3750.0, 5400.0024, 900.0), (0.0, 0.00048494337618129564, -0.0), (1.0, 1.0, 1.0), "Suburbs_Column_Large_A_Base28_770", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3749.9983, 5200.0, 900.0), (0.0, 90.00052163220809, -0.0), (1.0, 1.0, 1.0), "Suburbs_Column_Large_A_Base28_788", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1349.9978, 3799.9998, 900.0), (0.0, 90.00052163220809, -0.0), (1.0, 1.0, 1.0), "Suburbs_Column_Large_A_Base28_932", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1550.002, 4000.0002, 900.0), (0.0, -89.99957359878371, 0.0), (1.0, 1.0, 1.0), "Suburbs_Column_Large_A_Base28_950", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2549.998, 3800.0002, 900.0), (0.0, 90.00052163220809, -0.0), (1.0, 1.0, 1.0), "Suburbs_Column_Large_A_Base28_1004", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2750.0017, 4000.0, 900.0), (0.0, -89.99957359878371, 0.0), (1.0, 1.0, 1.0), "Suburbs_Column_Large_A_Base28_1022", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2550.0, 5400.003, 900.0), (0.0, 0.00048494337618129564, -0.0), (1.0, 1.0, 1.0), "Suburbs_Column_Large_A_Base28_1130", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2549.9983, 5200.0, 900.0), (0.0, 90.00052163220809, -0.0), (1.0, 1.0, 1.0), "Suburbs_Column_Large_A_Base28_1148", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2749.9995, 2399.998, 900.0), (0.0, -179.99953554711865, 0.0), (1.0, 1.0, 1.0), "Suburbs_Column_Large_A_Base28_1165", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2750.0015, 5400.0005, 900.0), (0.0, -89.99957359878371, 0.0), (1.0, 1.0, 1.0), "Suburbs_Column_Large_A_Base28_1166", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3950.0, 2399.9983, 900.0), (0.0, -179.9995560376937, 0.0), (1.0, 1.0, 1.0), "Suburbs_Column_Large_A_Base28_1188", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2749.9998, 999.9988, 900.0), (0.0, -179.9994604150484, 0.0), (1.0, 1.0, 1.0), "Suburbs_Column_Large_A_Base28_1252", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2749.9995, 3799.9983, 900.0), (0.0, -179.99958335846424, 0.0), (1.0, 1.0, 1.0), "Suburbs_Column_Large_A_Base28_3283", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2750.0, 5199.998, 900.0), (0.0, -179.9995560376937, 0.0), (1.0, 1.0, 1.0), "Suburbs_Column_Large_A_Base28_3302", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3950.0, 5199.998, 900.0), (0.0, -179.9995560376937, 0.0), (1.0, 1.0, 1.0), "Suburbs_Column_Large_A_Base28_3321", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4950.039, 3800.0, 900.0), (0.0, 90.00044060340373, -0.0), (1.0, 1.0, 1.0), "Suburbs_Column_Large_A_Base28_3340", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (250.0, 6150.0, 850.0), (0.0, 0.0001649999962307018, -0.0), (1.0, 1.0, 1.0), "Suburbs_Column_Large_A_Base29_488", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2550.0017, 4000.0, 900.0), (0.0, 90.00073230747108, -0.0), (1.0, 1.0, 1.0), "Suburbs_Column_Large_A_Base30", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2550.0017, 4000.0, 900.0), (0.0, -179.99978826413437, 0.0), (1.0, 1.0, 1.0), "Suburbs_Column_Large_A_Base31", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2550.0017, 4000.0, 900.0), (0.0, -89.99913766804917, 0.0), (1.0, 1.0, 1.0), "Suburbs_Column_Large_A_Base32", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2550.0017, 4000.0, 900.0), (0.0, 0.00046539310510081963, -0.0), (1.0, 1.0, 1.0), "Suburbs_Column_Large_A_Base33", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (250.0, 5150.0, 900.0), (0.0, 0.0005019999859682958, -0.0), (1.0, 1.0, 1.0), "Suburbs_Column_Large_A_Base39_350", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1249.9999, 6150.0, 900.0), (0.0, -89.99954442862955, 0.0), (1.0, 1.0, 1.0), "Suburbs_Column_Large_A_Base39_450", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (250.0, 5150.0, 900.0), (0.0, 90.00055404374588, -0.0), (1.0, 1.0, 1.0), "Suburbs_Column_Large_A_Base40", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1249.9999, 6150.0, 900.0), (0.0, 0.0005020189050346918, -0.0), (1.0, 1.0, 1.0), "Suburbs_Column_Large_A_Base40_335", _folder)
if a: placed += 1
else: skipped += 1

# Batch 19: StaticMesh'Suburbs_Column_Large_A_Capitol' (159 instances)
_mesh_path = "/Game/Art/Assets/Kits/Architecture/Suburbs/Suburbs_Column_Large_A_Capitol"
_materials = ['/Game/Art/Assets/Kits/Architecture/Suburbs/Materials/Suburbs_Column_Large/MI_Suburbs_Column_Large_A_Capitol']
_folder = "Reconstruction/BD_BB_Sandbox_DwarfHall_Voxels/Meshes"
a = spawn_static_mesh(_mesh_path, _materials, (1550.0, 2399.9985, 1700.0), (0.0, 90.00023965221622, -0.0), (1.0, 1.0, 1.0), "Suburbs_Column_Large_A_Capitol21_8", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3750.0, 1200.0013, 1700.0), (0.0, -89.99968865881478, 0.0), (1.0, 1.0, 1.0), "Suburbs_Column_Large_A_Capitol21_26", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4950.0, 2600.0017, 1700.0), (0.0, -89.99968865881478, 0.0), (1.0, 1.0, 1.0), "Suburbs_Column_Large_A_Capitol21_39", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3749.9983, 1000.0, 1700.0), (0.0, 0.0003380943391220613, -0.0), (1.0, 1.0, 1.0), "Suburbs_Column_Large_A_Capitol21_44", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3750.0, 2600.0015, 1700.0), (0.0, -89.99968865881478, 0.0), (1.0, 1.0, 1.0), "Suburbs_Column_Large_A_Capitol21_192", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3749.9983, 2400.0, 1700.0), (0.0, 0.0003380943391220613, -0.0), (1.0, 1.0, 1.0), "Suburbs_Column_Large_A_Capitol21_210", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3950.0017, 2600.0, 1700.0), (0.0, -179.99976777355934, 0.0), (1.0, 1.0, 1.0), "Suburbs_Column_Large_A_Capitol21_228", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4949.998, 2400.0, 1700.0), (0.0, 0.0003380943391220613, -0.0), (1.0, 1.0, 1.0), "Suburbs_Column_Large_A_Capitol21_282", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5150.002, 2600.0, 1700.0), (0.0, -179.99976777355934, 0.0), (1.0, 1.0, 1.0), "Suburbs_Column_Large_A_Capitol21_303", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2550.0, 1200.002, 1700.0), (0.0, -89.99968865881478, 0.0), (1.0, 1.0, 1.0), "Suburbs_Column_Large_A_Capitol21_411", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2549.9985, 999.99976, 1700.0), (0.0, 0.0003380943391220613, -0.0), (1.0, 1.0, 1.0), "Suburbs_Column_Large_A_Capitol21_429", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2750.0015, 1199.9998, 1700.0), (0.0, -179.99976777355934, 0.0), (1.0, 1.0, 1.0), "Suburbs_Column_Large_A_Capitol21_449", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1349.9995, 2600.0017, 1700.0), (0.0, -89.99968865881478, 0.0), (1.0, 1.0, 1.0), "Suburbs_Column_Large_A_Capitol21_485", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1349.998, 2399.9998, 1700.0), (0.0, 0.0003380943391220613, -0.0), (1.0, 1.0, 1.0), "Suburbs_Column_Large_A_Capitol21_503", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1550.0012, 2600.0, 1700.0), (0.0, -179.99976777355934, 0.0), (1.0, 1.0, 1.0), "Suburbs_Column_Large_A_Capitol21_523", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2550.0, 2600.0017, 1700.0), (0.0, -89.99968865881478, 0.0), (1.0, 1.0, 1.0), "Suburbs_Column_Large_A_Capitol21_559", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2549.998, 2400.0002, 1700.0), (0.0, 0.0003380943391220613, -0.0), (1.0, 1.0, 1.0), "Suburbs_Column_Large_A_Capitol21_577", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2750.0015, 2599.9998, 1700.0), (0.0, -179.99976777355934, 0.0), (1.0, 1.0, 1.0), "Suburbs_Column_Large_A_Capitol21_595", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3750.0, 4000.0017, 1700.0), (0.0, -89.99968865881478, 0.0), (1.0, 1.0, 1.0), "Suburbs_Column_Large_A_Capitol21_631", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3749.9983, 3800.0, 1700.0), (0.0, 0.0003380943391220613, -0.0), (1.0, 1.0, 1.0), "Suburbs_Column_Large_A_Capitol21_649", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3950.0017, 4000.0, 1700.0), (0.0, -179.99976777355934, 0.0), (1.0, 1.0, 1.0), "Suburbs_Column_Large_A_Capitol21_667", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3950.041, 3799.9983, 1700.0), (0.0, 90.00027854599058, -0.0), (1.0, 1.0, 1.0), "Suburbs_Column_Large_A_Capitol21_685", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4950.0, 4000.0017, 1700.0), (0.0, -89.99968865881478, 0.0), (1.0, 1.0, 1.0), "Suburbs_Column_Large_A_Capitol21_703", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5150.002, 4000.0, 1700.0), (0.0, -179.99976777355934, 0.0), (1.0, 1.0, 1.0), "Suburbs_Column_Large_A_Capitol21_739", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5150.041, 3800.001, 1700.0), (0.0, 90.0003595746567, -0.0), (1.0, 1.0, 1.0), "Suburbs_Column_Large_A_Capitol21_757", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3750.0, 5400.0024, 1700.0), (0.0, -89.99968865881478, 0.0), (1.0, 1.0, 1.0), "Suburbs_Column_Large_A_Capitol21_775", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3749.9983, 5200.0, 1700.0), (0.0, 0.0003380943391220613, -0.0), (1.0, 1.0, 1.0), "Suburbs_Column_Large_A_Capitol21_793", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1349.9978, 3799.9998, 1700.0), (0.0, 0.0003380943391220613, -0.0), (1.0, 1.0, 1.0), "Suburbs_Column_Large_A_Capitol21_937", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2549.998, 3800.0002, 1700.0), (0.0, 0.0003380943391220613, -0.0), (1.0, 1.0, 1.0), "Suburbs_Column_Large_A_Capitol21_1009", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2750.0017, 4000.0, 1700.0), (0.0, -179.99976777355934, 0.0), (1.0, 1.0, 1.0), "Suburbs_Column_Large_A_Capitol21_1027", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2550.0, 5400.003, 1700.0), (0.0, -89.99968865881478, 0.0), (1.0, 1.0, 1.0), "Suburbs_Column_Large_A_Capitol21_1135", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5150.0, 2399.9983, 1700.0), (0.0, 90.00023965221622, -0.0), (1.0, 1.0, 1.0), "Suburbs_Column_Large_A_Capitol21_1148", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2749.9995, 2399.998, 1700.0), (0.0, 90.00023965221622, -0.0), (1.0, 1.0, 1.0), "Suburbs_Column_Large_A_Capitol21_1170", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2750.0015, 5400.0005, 1700.0), (0.0, -179.99976777355934, 0.0), (1.0, 1.0, 1.0), "Suburbs_Column_Large_A_Capitol21_1171", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3950.0, 2399.9983, 1700.0), (0.0, 90.0002299287806, -0.0), (1.0, 1.0, 1.0), "Suburbs_Column_Large_A_Capitol21_1193", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2749.9998, 999.9988, 1700.0), (0.0, 90.0003595746567, -0.0), (1.0, 1.0, 1.0), "Suburbs_Column_Large_A_Capitol21_1257", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2749.9995, 3799.9983, 1700.0), (0.0, 90.0002137230564, -0.0), (1.0, 1.0, 1.0), "Suburbs_Column_Large_A_Capitol21_3288", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2750.0, 5199.998, 1700.0), (0.0, 90.0002299287806, -0.0), (1.0, 1.0, 1.0), "Suburbs_Column_Large_A_Capitol21_3307", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3950.0, 5199.998, 1700.0), (0.0, 90.0002299287806, -0.0), (1.0, 1.0, 1.0), "Suburbs_Column_Large_A_Capitol21_3326", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4950.039, 3800.0, 1700.0), (0.0, 0.0002697924758114751, -0.0), (1.0, 1.0, 1.0), "Suburbs_Column_Large_A_Capitol21_3345", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1550.0, 2399.9985, 1700.0), (0.0, 0.00017416980758966604, -0.0), (1.0, 1.0, 1.0), "Suburbs_Column_Large_A_Capitol22_9", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3750.0, 1200.0013, 1700.0), (0.0, -179.99976777355934, 0.0), (1.0, 1.0, 1.0), "Suburbs_Column_Large_A_Capitol22_27", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4950.0, 2600.0017, 1700.0), (0.0, -179.99976777355934, 0.0), (1.0, 1.0, 1.0), "Suburbs_Column_Large_A_Capitol22_40", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3749.9983, 1000.0, 1700.0), (0.0, -89.99968865881478, 0.0), (1.0, 1.0, 1.0), "Suburbs_Column_Large_A_Capitol22_45", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3750.0, 2600.0015, 1700.0), (0.0, -179.99976777355934, 0.0), (1.0, 1.0, 1.0), "Suburbs_Column_Large_A_Capitol22_193", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3749.9983, 2400.0, 1700.0), (0.0, -89.99968865881478, 0.0), (1.0, 1.0, 1.0), "Suburbs_Column_Large_A_Capitol22_211", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3950.0017, 2600.0, 1700.0), (0.0, 90.00019103504636, -0.0), (1.0, 1.0, 1.0), "Suburbs_Column_Large_A_Capitol22_229", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5150.002, 2600.0, 1700.0), (0.0, 90.00019103504636, -0.0), (1.0, 1.0, 1.0), "Suburbs_Column_Large_A_Capitol22_304", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1550.0015, 1199.9998, 1700.0), (0.0, 90.00019103504636, -0.0), (1.0, 1.0, 1.0), "Suburbs_Column_Large_A_Capitol22_376", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2550.0, 1200.002, 1700.0), (0.0, -179.99976777355934, 0.0), (1.0, 1.0, 1.0), "Suburbs_Column_Large_A_Capitol22_412", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2750.0015, 1199.9998, 1700.0), (0.0, 90.00019103504636, -0.0), (1.0, 1.0, 1.0), "Suburbs_Column_Large_A_Capitol22_450", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1349.9995, 2600.0017, 1700.0), (0.0, -179.99976777355934, 0.0), (1.0, 1.0, 1.0), "Suburbs_Column_Large_A_Capitol22_486", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1550.0012, 2600.0, 1700.0), (0.0, 90.00019103504636, -0.0), (1.0, 1.0, 1.0), "Suburbs_Column_Large_A_Capitol22_524", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2550.0, 2600.0017, 1700.0), (0.0, -179.99976777355934, 0.0), (1.0, 1.0, 1.0), "Suburbs_Column_Large_A_Capitol22_560", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2549.998, 2400.0002, 1700.0), (0.0, -89.99968865881478, 0.0), (1.0, 1.0, 1.0), "Suburbs_Column_Large_A_Capitol22_578", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2750.0015, 2599.9998, 1700.0), (0.0, 90.00019103504636, -0.0), (1.0, 1.0, 1.0), "Suburbs_Column_Large_A_Capitol22_596", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3750.0, 4000.0017, 1700.0), (0.0, -179.99976777355934, 0.0), (1.0, 1.0, 1.0), "Suburbs_Column_Large_A_Capitol22_632", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3749.9983, 3800.0, 1700.0), (0.0, -89.99968865881478, 0.0), (1.0, 1.0, 1.0), "Suburbs_Column_Large_A_Capitol22_650", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3950.0017, 4000.0, 1700.0), (0.0, 90.00019103504636, -0.0), (1.0, 1.0, 1.0), "Suburbs_Column_Large_A_Capitol22_668", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3950.041, 3799.9983, 1700.0), (0.0, 0.0002424716938180545, -0.0), (1.0, 1.0, 1.0), "Suburbs_Column_Large_A_Capitol22_686", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4950.0, 4000.0017, 1700.0), (0.0, -179.99976777355934, 0.0), (1.0, 1.0, 1.0), "Suburbs_Column_Large_A_Capitol22_704", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5150.002, 4000.0, 1700.0), (0.0, 90.00019103504636, -0.0), (1.0, 1.0, 1.0), "Suburbs_Column_Large_A_Capitol22_740", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5150.041, 3800.001, 1700.0), (0.0, 0.0002936981084895667, -0.0), (1.0, 1.0, 1.0), "Suburbs_Column_Large_A_Capitol22_758", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3750.0, 5400.0024, 1700.0), (0.0, -179.99976777355934, 0.0), (1.0, 1.0, 1.0), "Suburbs_Column_Large_A_Capitol22_776", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3749.9983, 5200.0, 1700.0), (0.0, -89.99968865881478, 0.0), (1.0, 1.0, 1.0), "Suburbs_Column_Large_A_Capitol22_794", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4949.998, 5200.0, 1700.0), (0.0, -89.99968865881478, 0.0), (1.0, 1.0, 1.0), "Suburbs_Column_Large_A_Capitol22_866", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1349.9978, 3799.9998, 1700.0), (0.0, -89.99968865881478, 0.0), (1.0, 1.0, 1.0), "Suburbs_Column_Large_A_Capitol22_938", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2549.998, 3800.0002, 1700.0), (0.0, -89.99968865881478, 0.0), (1.0, 1.0, 1.0), "Suburbs_Column_Large_A_Capitol22_1010", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2750.0017, 4000.0, 1700.0), (0.0, 90.00019103504636, -0.0), (1.0, 1.0, 1.0), "Suburbs_Column_Large_A_Capitol22_1028", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2550.0, 5400.003, 1700.0), (0.0, -179.99976777355934, 0.0), (1.0, 1.0, 1.0), "Suburbs_Column_Large_A_Capitol22_1136", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2749.9995, 2399.998, 1700.0), (0.0, 0.00017416980758966604, -0.0), (1.0, 1.0, 1.0), "Suburbs_Column_Large_A_Capitol22_1171", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2750.0015, 5400.0005, 1700.0), (0.0, 90.00019103504636, -0.0), (1.0, 1.0, 1.0), "Suburbs_Column_Large_A_Capitol22_1172", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3950.0, 2399.9983, 1700.0), (0.0, 0.00015709433603261142, -0.0), (1.0, 1.0, 1.0), "Suburbs_Column_Large_A_Capitol22_1194", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2749.9998, 999.9988, 1700.0), (0.0, 0.0002936981084895667, -0.0), (1.0, 1.0, 1.0), "Suburbs_Column_Large_A_Capitol22_1258", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2749.9995, 3799.9983, 1700.0), (0.0, 0.00014343395649514662, -0.0), (1.0, 1.0, 1.0), "Suburbs_Column_Large_A_Capitol22_3289", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2750.0, 5199.998, 1700.0), (0.0, 0.00015709433603261142, -0.0), (1.0, 1.0, 1.0), "Suburbs_Column_Large_A_Capitol22_3308", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3950.0, 5199.998, 1700.0), (0.0, 0.00015709433603261142, -0.0), (1.0, 1.0, 1.0), "Suburbs_Column_Large_A_Capitol22_3327", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4950.039, 3800.0, 1700.0), (0.0, -89.99981506294705, 0.0), (1.0, 1.0, 1.0), "Suburbs_Column_Large_A_Capitol22_3346", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1550.0, 2399.9985, 1700.0), (0.0, -90.00005166594045, 0.0), (1.0, 1.0, 1.0), "Suburbs_Column_Large_A_Capitol23_10", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3750.0, 1200.0013, 1700.0), (0.0, 90.00001925454477, -0.0), (1.0, 1.0, 1.0), "Suburbs_Column_Large_A_Capitol23_28", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4950.0, 2600.0017, 1700.0), (0.0, 90.00001925454477, -0.0), (1.0, 1.0, 1.0), "Suburbs_Column_Large_A_Capitol23_41", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3749.9983, 1000.0, 1700.0), (0.0, -179.99995901885745, 0.0), (1.0, 1.0, 1.0), "Suburbs_Column_Large_A_Capitol23_46", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3750.0, 2600.0015, 1700.0), (0.0, 90.00001925454477, -0.0), (1.0, 1.0, 1.0), "Suburbs_Column_Large_A_Capitol23_194", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3749.9983, 2400.0, 1700.0), (0.0, -179.99995901885745, 0.0), (1.0, 1.0, 1.0), "Suburbs_Column_Large_A_Capitol23_212", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3950.0017, 2600.0, 1700.0), (0.0, -3.051757709276941e-05, 0.0), (1.0, 1.0, 1.0), "Suburbs_Column_Large_A_Capitol23_230", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5150.002, 2600.0, 1700.0), (0.0, -3.051757709276941e-05, 0.0), (1.0, 1.0, 1.0), "Suburbs_Column_Large_A_Capitol23_305", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1550.0015, 1199.9998, 1700.0), (0.0, -3.051757709276941e-05, 0.0), (1.0, 1.0, 1.0), "Suburbs_Column_Large_A_Capitol23_377", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2550.0, 1200.002, 1700.0), (0.0, 90.00001925454477, -0.0), (1.0, 1.0, 1.0), "Suburbs_Column_Large_A_Capitol23_413", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2750.0015, 1199.9998, 1700.0), (0.0, -3.051757709276941e-05, 0.0), (1.0, 1.0, 1.0), "Suburbs_Column_Large_A_Capitol23_451", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1349.9995, 2600.0017, 1700.0), (0.0, 90.00001925454477, -0.0), (1.0, 1.0, 1.0), "Suburbs_Column_Large_A_Capitol23_487", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1550.0012, 2600.0, 1700.0), (0.0, -3.051757709276941e-05, 0.0), (1.0, 1.0, 1.0), "Suburbs_Column_Large_A_Capitol23_525", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2550.0, 2600.0017, 1700.0), (0.0, 90.00001925454477, -0.0), (1.0, 1.0, 1.0), "Suburbs_Column_Large_A_Capitol23_561", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2549.998, 2400.0002, 1700.0), (0.0, -179.99995901885745, 0.0), (1.0, 1.0, 1.0), "Suburbs_Column_Large_A_Capitol23_579", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2750.0015, 2599.9998, 1700.0), (0.0, -3.051757709276941e-05, 0.0), (1.0, 1.0, 1.0), "Suburbs_Column_Large_A_Capitol23_597", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3750.0, 4000.0017, 1700.0), (0.0, 90.00001925454477, -0.0), (1.0, 1.0, 1.0), "Suburbs_Column_Large_A_Capitol23_633", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3749.9983, 3800.0, 1700.0), (0.0, -179.99995901885745, 0.0), (1.0, 1.0, 1.0), "Suburbs_Column_Large_A_Capitol23_651", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3950.0017, 4000.0, 1700.0), (0.0, -3.051757709276941e-05, 0.0), (1.0, 1.0, 1.0), "Suburbs_Column_Large_A_Capitol23_669", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3950.041, 3799.9983, 1700.0), (0.0, -89.99993822608693, 0.0), (1.0, 1.0, 1.0), "Suburbs_Column_Large_A_Capitol23_687", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4950.0, 4000.0017, 1700.0), (0.0, 90.00001925454477, -0.0), (1.0, 1.0, 1.0), "Suburbs_Column_Large_A_Capitol23_705", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5150.002, 4000.0, 1700.0), (0.0, -3.051757709276941e-05, 0.0), (1.0, 1.0, 1.0), "Suburbs_Column_Large_A_Capitol23_741", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5150.041, 3800.001, 1700.0), (0.0, -89.99993822608693, 0.0), (1.0, 1.0, 1.0), "Suburbs_Column_Large_A_Capitol23_759", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3750.0, 5400.0024, 1700.0), (0.0, 90.00001925454477, -0.0), (1.0, 1.0, 1.0), "Suburbs_Column_Large_A_Capitol23_777", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3749.9983, 5200.0, 1700.0), (0.0, -179.99995901885745, 0.0), (1.0, 1.0, 1.0), "Suburbs_Column_Large_A_Capitol23_795", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4949.998, 5200.0, 1700.0), (0.0, -179.99995901885745, 0.0), (1.0, 1.0, 1.0), "Suburbs_Column_Large_A_Capitol23_867", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1349.9978, 3799.9998, 1700.0), (0.0, -179.99995901885745, 0.0), (1.0, 1.0, 1.0), "Suburbs_Column_Large_A_Capitol23_939", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2549.998, 3800.0002, 1700.0), (0.0, -179.99995901885745, 0.0), (1.0, 1.0, 1.0), "Suburbs_Column_Large_A_Capitol23_1011", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2750.0017, 4000.0, 1700.0), (0.0, -3.051757709276941e-05, 0.0), (1.0, 1.0, 1.0), "Suburbs_Column_Large_A_Capitol23_1029", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2550.0, 5400.003, 1700.0), (0.0, 90.00001925454477, -0.0), (1.0, 1.0, 1.0), "Suburbs_Column_Large_A_Capitol23_1137", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2749.9995, 2399.998, 1700.0), (0.0, -90.00005166594045, 0.0), (1.0, 1.0, 1.0), "Suburbs_Column_Large_A_Capitol23_1172", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2750.0015, 5400.0005, 1700.0), (0.0, -3.051757709276941e-05, 0.0), (1.0, 1.0, 1.0), "Suburbs_Column_Large_A_Capitol23_1173", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3950.0, 2399.9983, 1700.0), (0.0, -90.00005166594045, 0.0), (1.0, 1.0, 1.0), "Suburbs_Column_Large_A_Capitol23_1195", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2749.9998, 999.9988, 1700.0), (0.0, -89.99993822608693, 0.0), (1.0, 1.0, 1.0), "Suburbs_Column_Large_A_Capitol23_1259", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2749.9995, 3799.9983, 1700.0), (0.0, -90.00005166594045, 0.0), (1.0, 1.0, 1.0), "Suburbs_Column_Large_A_Capitol23_3290", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2750.0, 5199.998, 1700.0), (0.0, -90.00005166594045, 0.0), (1.0, 1.0, 1.0), "Suburbs_Column_Large_A_Capitol23_3309", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3950.0, 5199.998, 1700.0), (0.0, -90.00005166594045, 0.0), (1.0, 1.0, 1.0), "Suburbs_Column_Large_A_Capitol23_3328", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4950.039, 3800.0, 1700.0), (0.0, 179.99986339621609, -0.0), (1.0, 1.0, 1.0), "Suburbs_Column_Large_A_Capitol23_3347", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1550.0, 2399.9985, 1700.0), (0.0, 179.99978826413437, -0.0), (1.0, 1.0, 1.0), "Suburbs_Column_Large_A_Capitol24_11", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3750.0, 1200.0013, 1700.0), (0.0, -0.0001525878854640202, 0.0), (1.0, 1.0, 1.0), "Suburbs_Column_Large_A_Capitol24_29", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4950.0, 2600.0017, 1700.0), (0.0, -0.0001525878854640202, 0.0), (1.0, 1.0, 1.0), "Suburbs_Column_Large_A_Capitol24_42", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3749.9983, 1000.0, 1700.0), (0.0, 89.9998815062137, -0.0), (1.0, 1.0, 1.0), "Suburbs_Column_Large_A_Capitol24_47", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3750.0, 2600.0015, 1700.0), (0.0, -0.0001525878854640202, 0.0), (1.0, 1.0, 1.0), "Suburbs_Column_Large_A_Capitol24_195", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3749.9983, 2400.0, 1700.0), (0.0, 89.9998815062137, -0.0), (1.0, 1.0, 1.0), "Suburbs_Column_Large_A_Capitol24_213", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3950.0017, 2600.0, 1700.0), (0.0, -90.00022020536449, 0.0), (1.0, 1.0, 1.0), "Suburbs_Column_Large_A_Capitol24_231", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5150.002, 2600.0, 1700.0), (0.0, -90.00022020536449, 0.0), (1.0, 1.0, 1.0), "Suburbs_Column_Large_A_Capitol24_306", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1550.0015, 1199.9998, 1700.0), (0.0, -90.00022020536449, 0.0), (1.0, 1.0, 1.0), "Suburbs_Column_Large_A_Capitol24_378", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2550.0, 1200.002, 1700.0), (0.0, -0.0001525878854640202, 0.0), (1.0, 1.0, 1.0), "Suburbs_Column_Large_A_Capitol24_414", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2750.0015, 1199.9998, 1700.0), (0.0, -90.00022020536449, 0.0), (1.0, 1.0, 1.0), "Suburbs_Column_Large_A_Capitol24_452", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1349.9995, 2600.0017, 1700.0), (0.0, -0.0001525878854640202, 0.0), (1.0, 1.0, 1.0), "Suburbs_Column_Large_A_Capitol24_488", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1550.0012, 2600.0, 1700.0), (0.0, -90.00022020536449, 0.0), (1.0, 1.0, 1.0), "Suburbs_Column_Large_A_Capitol24_526", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2550.0, 2600.0017, 1700.0), (0.0, -0.0001525878854640202, 0.0), (1.0, 1.0, 1.0), "Suburbs_Column_Large_A_Capitol24_562", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2549.998, 2400.0002, 1700.0), (0.0, 89.9998815062137, -0.0), (1.0, 1.0, 1.0), "Suburbs_Column_Large_A_Capitol24_580", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2750.0015, 2599.9998, 1700.0), (0.0, -90.00022020536449, 0.0), (1.0, 1.0, 1.0), "Suburbs_Column_Large_A_Capitol24_598", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3750.0, 4000.0017, 1700.0), (0.0, -0.0001525878854640202, 0.0), (1.0, 1.0, 1.0), "Suburbs_Column_Large_A_Capitol24_634", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3749.9983, 3800.0, 1700.0), (0.0, 89.9998815062137, -0.0), (1.0, 1.0, 1.0), "Suburbs_Column_Large_A_Capitol24_652", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3950.0017, 4000.0, 1700.0), (0.0, -90.00022020536449, 0.0), (1.0, 1.0, 1.0), "Suburbs_Column_Large_A_Capitol24_670", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3950.041, 3799.9983, 1700.0), (0.0, 179.99986339621609, -0.0), (1.0, 1.0, 1.0), "Suburbs_Column_Large_A_Capitol24_688", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4950.0, 4000.0017, 1700.0), (0.0, -0.0001525878854640202, 0.0), (1.0, 1.0, 1.0), "Suburbs_Column_Large_A_Capitol24_706", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5150.002, 4000.0, 1700.0), (0.0, -90.00022020536449, 0.0), (1.0, 1.0, 1.0), "Suburbs_Column_Large_A_Capitol24_742", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5150.041, 3800.001, 1700.0), (0.0, 179.9998975471592, -0.0), (1.0, 1.0, 1.0), "Suburbs_Column_Large_A_Capitol24_760", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3750.0, 5400.0024, 1700.0), (0.0, -0.0001525878854640202, 0.0), (1.0, 1.0, 1.0), "Suburbs_Column_Large_A_Capitol24_778", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3749.9983, 5200.0, 1700.0), (0.0, 89.9998815062137, -0.0), (1.0, 1.0, 1.0), "Suburbs_Column_Large_A_Capitol24_796", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4949.998, 5200.0, 1700.0), (0.0, 89.9998815062137, -0.0), (1.0, 1.0, 1.0), "Suburbs_Column_Large_A_Capitol24_868", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1349.9978, 3799.9998, 1700.0), (0.0, 89.9998815062137, -0.0), (1.0, 1.0, 1.0), "Suburbs_Column_Large_A_Capitol24_940", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2549.998, 3800.0002, 1700.0), (0.0, 89.9998815062137, -0.0), (1.0, 1.0, 1.0), "Suburbs_Column_Large_A_Capitol24_1012", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2750.0017, 4000.0, 1700.0), (0.0, -90.00022020536449, 0.0), (1.0, 1.0, 1.0), "Suburbs_Column_Large_A_Capitol24_1030", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2550.0, 5400.003, 1700.0), (0.0, -0.0001525878854640202, 0.0), (1.0, 1.0, 1.0), "Suburbs_Column_Large_A_Capitol24_1138", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2749.9995, 2399.998, 1700.0), (0.0, 179.99978826413437, -0.0), (1.0, 1.0, 1.0), "Suburbs_Column_Large_A_Capitol24_1173", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2750.0015, 5400.0005, 1700.0), (0.0, -90.00022020536449, 0.0), (1.0, 1.0, 1.0), "Suburbs_Column_Large_A_Capitol24_1174", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3950.0, 2399.9983, 1700.0), (0.0, 179.99976777355934, -0.0), (1.0, 1.0, 1.0), "Suburbs_Column_Large_A_Capitol24_1196", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2749.9998, 999.9988, 1700.0), (0.0, 179.9998975471592, -0.0), (1.0, 1.0, 1.0), "Suburbs_Column_Large_A_Capitol24_1260", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2749.9995, 3799.9983, 1700.0), (0.0, 179.99976777355934, -0.0), (1.0, 1.0, 1.0), "Suburbs_Column_Large_A_Capitol24_3291", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2750.0, 5199.998, 1700.0), (0.0, 179.99976777355934, -0.0), (1.0, 1.0, 1.0), "Suburbs_Column_Large_A_Capitol24_3310", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3950.0, 5199.998, 1700.0), (0.0, 179.99976777355934, -0.0), (1.0, 1.0, 1.0), "Suburbs_Column_Large_A_Capitol24_3329", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4950.039, 3800.0, 1700.0), (0.0, 89.99979237503166, -0.0), (1.0, 1.0, 1.0), "Suburbs_Column_Large_A_Capitol24_3348", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (250.0, 5150.0, 1900.0), (0.0, -3.051757709276941e-05, 0.0), (1.0, 1.0, 1.0), "Suburbs_Column_Large_A_Capitol38_355", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1249.9999, 6150.0, 1900.0), (0.0, -90.00005166594045, 0.0), (1.0, 1.0, 1.0), "Suburbs_Column_Large_A_Capitol38_455", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (250.0, 5150.0, 1900.0), (0.0, -89.99999818714215, 0.0), (1.0, 1.0, 1.0), "Suburbs_Column_Large_A_Capitol39_356", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1249.9999, 6150.0, 1900.0), (0.0, 179.99992486791828, -0.0), (1.0, 1.0, 1.0), "Suburbs_Column_Large_A_Capitol39_456", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (250.0, 6150.0, 1850.0), (0.0, -90.00018131163026, 0.0), (1.0, 1.0, 1.0), "Suburbs_Column_Large_A_Capitol40_494", _folder)
if a: placed += 1
else: skipped += 1

# Batch 20: StaticMesh'Suburbs_Column_Large_A_Shaft' (165 instances)
_mesh_path = "/Game/Art/Assets/Kits/Architecture/Suburbs/Suburbs_Column_Large_A_Shaft"
_materials = ['/Game/Art/Assets/Kits/Architecture/Suburbs/Materials/Suburbs_Column_Large/MI_Suburbs_Column_Large_A_Shaft']
_folder = "Reconstruction/BD_BB_Sandbox_DwarfHall_Voxels/Meshes"
a = spawn_static_mesh(_mesh_path, _materials, (1550.0, 2399.9985, 1300.0), (0.0, 90.00023965221622, -0.0), (1.0, 1.0, 1.0), "Suburbs_Column_Large_A_Shaft21_4", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3750.0, 1200.0013, 1300.0), (0.0, -89.99968865881478, 0.0), (1.0, 1.0, 1.0), "Suburbs_Column_Large_A_Shaft21_22", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4950.0, 2600.0017, 1300.0), (0.0, -89.99968865881478, 0.0), (1.0, 1.0, 1.0), "Suburbs_Column_Large_A_Shaft21_35", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3749.9983, 1000.0, 1300.0), (0.0, 0.0003380943391220613, -0.0), (1.0, 1.0, 1.0), "Suburbs_Column_Large_A_Shaft21_40", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3750.0, 2600.0015, 1300.0), (0.0, -89.99968865881478, 0.0), (1.0, 1.0, 1.0), "Suburbs_Column_Large_A_Shaft21_188", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3749.9983, 2400.0, 1300.0), (0.0, 0.0003380943391220613, -0.0), (1.0, 1.0, 1.0), "Suburbs_Column_Large_A_Shaft21_206", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3950.0017, 2600.0, 1300.0), (0.0, -179.99976777355934, 0.0), (1.0, 1.0, 1.0), "Suburbs_Column_Large_A_Shaft21_224", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5150.002, 2600.0, 1300.0), (0.0, -179.99976777355934, 0.0), (1.0, 1.0, 1.0), "Suburbs_Column_Large_A_Shaft21_299", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2550.0, 1200.002, 1300.0), (0.0, -89.99968865881478, 0.0), (1.0, 1.0, 1.0), "Suburbs_Column_Large_A_Shaft21_407", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2549.9985, 999.99976, 1300.0), (0.0, 0.0003380943391220613, -0.0), (1.0, 1.0, 1.0), "Suburbs_Column_Large_A_Shaft21_425", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2750.0015, 1199.9998, 1300.0), (0.0, -179.99976777355934, 0.0), (1.0, 1.0, 1.0), "Suburbs_Column_Large_A_Shaft21_445", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1349.9995, 2600.0017, 1300.0), (0.0, -89.99968865881478, 0.0), (1.0, 1.0, 1.0), "Suburbs_Column_Large_A_Shaft21_481", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1550.0012, 2600.0, 1300.0), (0.0, -179.99976777355934, 0.0), (1.0, 1.0, 1.0), "Suburbs_Column_Large_A_Shaft21_519", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2550.0, 2600.0017, 1300.0), (0.0, -89.99968865881478, 0.0), (1.0, 1.0, 1.0), "Suburbs_Column_Large_A_Shaft21_555", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2549.998, 2400.0002, 1300.0), (0.0, 0.0003380943391220613, -0.0), (1.0, 1.0, 1.0), "Suburbs_Column_Large_A_Shaft21_573", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2750.0015, 2599.9998, 1300.0), (0.0, -179.99976777355934, 0.0), (1.0, 1.0, 1.0), "Suburbs_Column_Large_A_Shaft21_591", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3750.0, 4000.0017, 1300.0), (0.0, -89.99968865881478, 0.0), (1.0, 1.0, 1.0), "Suburbs_Column_Large_A_Shaft21_627", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3749.9983, 3800.0, 1300.0), (0.0, 0.0003380943391220613, -0.0), (1.0, 1.0, 1.0), "Suburbs_Column_Large_A_Shaft21_645", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3950.0017, 4000.0, 1300.0), (0.0, -179.99976777355934, 0.0), (1.0, 1.0, 1.0), "Suburbs_Column_Large_A_Shaft21_663", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3950.041, 3799.9983, 1300.0), (0.0, 90.00027854599058, -0.0), (1.0, 1.0, 1.0), "Suburbs_Column_Large_A_Shaft21_681", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4950.0, 4000.0017, 1300.0), (0.0, -89.99968865881478, 0.0), (1.0, 1.0, 1.0), "Suburbs_Column_Large_A_Shaft21_699", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5150.002, 4000.0, 1300.0), (0.0, -179.99976777355934, 0.0), (1.0, 1.0, 1.0), "Suburbs_Column_Large_A_Shaft21_735", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5150.041, 3800.001, 1300.0), (0.0, 90.0003595746567, -0.0), (1.0, 1.0, 1.0), "Suburbs_Column_Large_A_Shaft21_753", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3750.0, 5400.0024, 1300.0), (0.0, -89.99968865881478, 0.0), (1.0, 1.0, 1.0), "Suburbs_Column_Large_A_Shaft21_771", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3749.9983, 5200.0, 1300.0), (0.0, 0.0003380943391220613, -0.0), (1.0, 1.0, 1.0), "Suburbs_Column_Large_A_Shaft21_789", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1349.9978, 3799.9998, 1300.0), (0.0, 0.0003380943391220613, -0.0), (1.0, 1.0, 1.0), "Suburbs_Column_Large_A_Shaft21_933", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1550.002, 4000.0002, 1300.0), (0.0, -179.99976777355934, 0.0), (1.0, 1.0, 1.0), "Suburbs_Column_Large_A_Shaft21_951", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2549.998, 3800.0002, 1300.0), (0.0, 0.0003380943391220613, -0.0), (1.0, 1.0, 1.0), "Suburbs_Column_Large_A_Shaft21_1005", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2750.0017, 4000.0, 1300.0), (0.0, -179.99976777355934, 0.0), (1.0, 1.0, 1.0), "Suburbs_Column_Large_A_Shaft21_1023", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2550.0, 5400.003, 1300.0), (0.0, -89.99968865881478, 0.0), (1.0, 1.0, 1.0), "Suburbs_Column_Large_A_Shaft21_1131", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2749.9995, 2399.998, 1300.0), (0.0, 90.00023965221622, -0.0), (1.0, 1.0, 1.0), "Suburbs_Column_Large_A_Shaft21_1166", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2750.0015, 5400.0005, 1300.0), (0.0, -179.99976777355934, 0.0), (1.0, 1.0, 1.0), "Suburbs_Column_Large_A_Shaft21_1167", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3950.0, 2399.9983, 1300.0), (0.0, 90.0002299287806, -0.0), (1.0, 1.0, 1.0), "Suburbs_Column_Large_A_Shaft21_1189", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2749.9998, 999.9988, 1300.0), (0.0, 90.0003595746567, -0.0), (1.0, 1.0, 1.0), "Suburbs_Column_Large_A_Shaft21_1253", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2749.9995, 3799.9983, 1300.0), (0.0, 90.0002137230564, -0.0), (1.0, 1.0, 1.0), "Suburbs_Column_Large_A_Shaft21_3284", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2750.0, 5199.998, 1300.0), (0.0, 90.0002299287806, -0.0), (1.0, 1.0, 1.0), "Suburbs_Column_Large_A_Shaft21_3303", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3950.0, 5199.998, 1300.0), (0.0, 90.0002299287806, -0.0), (1.0, 1.0, 1.0), "Suburbs_Column_Large_A_Shaft21_3322", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4950.039, 3800.0, 1300.0), (0.0, 0.0002697924758114751, -0.0), (1.0, 1.0, 1.0), "Suburbs_Column_Large_A_Shaft21_3341", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1550.0, 2399.9985, 1300.0), (0.0, 0.00017416980758966604, -0.0), (1.0, 1.0, 1.0), "Suburbs_Column_Large_A_Shaft22_5", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3750.0, 1200.0013, 1300.0), (0.0, -179.99976777355934, 0.0), (1.0, 1.0, 1.0), "Suburbs_Column_Large_A_Shaft22_23", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4950.0, 2600.0017, 1300.0), (0.0, -179.99976777355934, 0.0), (1.0, 1.0, 1.0), "Suburbs_Column_Large_A_Shaft22_36", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3749.9983, 1000.0, 1300.0), (0.0, -89.99968865881478, 0.0), (1.0, 1.0, 1.0), "Suburbs_Column_Large_A_Shaft22_41", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3750.0, 2600.0015, 1300.0), (0.0, -179.99976777355934, 0.0), (1.0, 1.0, 1.0), "Suburbs_Column_Large_A_Shaft22_189", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3749.9983, 2400.0, 1300.0), (0.0, -89.99968865881478, 0.0), (1.0, 1.0, 1.0), "Suburbs_Column_Large_A_Shaft22_207", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3950.0017, 2600.0, 1300.0), (0.0, 90.00019103504636, -0.0), (1.0, 1.0, 1.0), "Suburbs_Column_Large_A_Shaft22_225", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5150.002, 2600.0, 1300.0), (0.0, 90.00019103504636, -0.0), (1.0, 1.0, 1.0), "Suburbs_Column_Large_A_Shaft22_300", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1550.0015, 1199.9998, 1300.0), (0.0, 90.00019103504636, -0.0), (1.0, 1.0, 1.0), "Suburbs_Column_Large_A_Shaft22_372", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2550.0, 1200.002, 1300.0), (0.0, -179.99976777355934, 0.0), (1.0, 1.0, 1.0), "Suburbs_Column_Large_A_Shaft22_408", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2750.0015, 1199.9998, 1300.0), (0.0, 90.00019103504636, -0.0), (1.0, 1.0, 1.0), "Suburbs_Column_Large_A_Shaft22_446", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1349.9995, 2600.0017, 1300.0), (0.0, -179.99976777355934, 0.0), (1.0, 1.0, 1.0), "Suburbs_Column_Large_A_Shaft22_482", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1550.0012, 2600.0, 1300.0), (0.0, 90.00019103504636, -0.0), (1.0, 1.0, 1.0), "Suburbs_Column_Large_A_Shaft22_520", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2550.0, 2600.0017, 1300.0), (0.0, -179.99976777355934, 0.0), (1.0, 1.0, 1.0), "Suburbs_Column_Large_A_Shaft22_556", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2549.998, 2400.0002, 1300.0), (0.0, -89.99968865881478, 0.0), (1.0, 1.0, 1.0), "Suburbs_Column_Large_A_Shaft22_574", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2750.0015, 2599.9998, 1300.0), (0.0, 90.00019103504636, -0.0), (1.0, 1.0, 1.0), "Suburbs_Column_Large_A_Shaft22_592", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3750.0, 4000.0017, 1300.0), (0.0, -179.99976777355934, 0.0), (1.0, 1.0, 1.0), "Suburbs_Column_Large_A_Shaft22_628", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3749.9983, 3800.0, 1300.0), (0.0, -89.99968865881478, 0.0), (1.0, 1.0, 1.0), "Suburbs_Column_Large_A_Shaft22_646", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3950.0017, 4000.0, 1300.0), (0.0, 90.00019103504636, -0.0), (1.0, 1.0, 1.0), "Suburbs_Column_Large_A_Shaft22_664", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3950.041, 3799.9983, 1300.0), (0.0, 0.0002424716938180545, -0.0), (1.0, 1.0, 1.0), "Suburbs_Column_Large_A_Shaft22_682", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4950.0, 4000.0017, 1300.0), (0.0, -179.99976777355934, 0.0), (1.0, 1.0, 1.0), "Suburbs_Column_Large_A_Shaft22_700", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5150.002, 4000.0, 1300.0), (0.0, 90.00019103504636, -0.0), (1.0, 1.0, 1.0), "Suburbs_Column_Large_A_Shaft22_736", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5150.041, 3800.001, 1300.0), (0.0, 0.0002936981084895667, -0.0), (1.0, 1.0, 1.0), "Suburbs_Column_Large_A_Shaft22_754", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3750.0, 5400.0024, 1300.0), (0.0, -179.99976777355934, 0.0), (1.0, 1.0, 1.0), "Suburbs_Column_Large_A_Shaft22_772", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3749.9983, 5200.0, 1300.0), (0.0, -89.99968865881478, 0.0), (1.0, 1.0, 1.0), "Suburbs_Column_Large_A_Shaft22_790", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4949.998, 5200.0, 1300.0), (0.0, -89.99968865881478, 0.0), (1.0, 1.0, 1.0), "Suburbs_Column_Large_A_Shaft22_862", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1349.9978, 3799.9998, 1300.0), (0.0, -89.99968865881478, 0.0), (1.0, 1.0, 1.0), "Suburbs_Column_Large_A_Shaft22_934", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1550.002, 4000.0002, 1300.0), (0.0, 90.00019103504636, -0.0), (1.0, 1.0, 1.0), "Suburbs_Column_Large_A_Shaft22_952", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2549.998, 3800.0002, 1300.0), (0.0, -89.99968865881478, 0.0), (1.0, 1.0, 1.0), "Suburbs_Column_Large_A_Shaft22_1006", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2750.0017, 4000.0, 1300.0), (0.0, 90.00019103504636, -0.0), (1.0, 1.0, 1.0), "Suburbs_Column_Large_A_Shaft22_1024", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2550.0, 5400.003, 1300.0), (0.0, -179.99976777355934, 0.0), (1.0, 1.0, 1.0), "Suburbs_Column_Large_A_Shaft22_1132", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2749.9995, 2399.998, 1300.0), (0.0, 0.00017416980758966604, -0.0), (1.0, 1.0, 1.0), "Suburbs_Column_Large_A_Shaft22_1167", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2750.0015, 5400.0005, 1300.0), (0.0, 90.00019103504636, -0.0), (1.0, 1.0, 1.0), "Suburbs_Column_Large_A_Shaft22_1168", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3950.0, 2399.9983, 1300.0), (0.0, 0.00015709433603261142, -0.0), (1.0, 1.0, 1.0), "Suburbs_Column_Large_A_Shaft22_1190", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2749.9998, 999.9988, 1300.0), (0.0, 0.0002936981084895667, -0.0), (1.0, 1.0, 1.0), "Suburbs_Column_Large_A_Shaft22_1254", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2749.9995, 3799.9983, 1300.0), (0.0, 0.00014343395649514662, -0.0), (1.0, 1.0, 1.0), "Suburbs_Column_Large_A_Shaft22_3285", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2750.0, 5199.998, 1300.0), (0.0, 0.00015709433603261142, -0.0), (1.0, 1.0, 1.0), "Suburbs_Column_Large_A_Shaft22_3304", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3950.0, 5199.998, 1300.0), (0.0, 0.00015709433603261142, -0.0), (1.0, 1.0, 1.0), "Suburbs_Column_Large_A_Shaft22_3323", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4950.039, 3800.0, 1300.0), (0.0, -89.99981506294705, 0.0), (1.0, 1.0, 1.0), "Suburbs_Column_Large_A_Shaft22_3342", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1550.0, 2399.9985, 1300.0), (0.0, -90.00005166594045, 0.0), (1.0, 1.0, 1.0), "Suburbs_Column_Large_A_Shaft23_6", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3750.0, 1200.0013, 1300.0), (0.0, 90.00001925454477, -0.0), (1.0, 1.0, 1.0), "Suburbs_Column_Large_A_Shaft23_24", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4950.0, 2600.0017, 1300.0), (0.0, 90.00001925454477, -0.0), (1.0, 1.0, 1.0), "Suburbs_Column_Large_A_Shaft23_37", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3749.9983, 1000.0, 1300.0), (0.0, -179.99995901885745, 0.0), (1.0, 1.0, 1.0), "Suburbs_Column_Large_A_Shaft23_42", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3750.0, 2600.0015, 1300.0), (0.0, 90.00001925454477, -0.0), (1.0, 1.0, 1.0), "Suburbs_Column_Large_A_Shaft23_190", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3749.9983, 2400.0, 1300.0), (0.0, -179.99995901885745, 0.0), (1.0, 1.0, 1.0), "Suburbs_Column_Large_A_Shaft23_208", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3950.0017, 2600.0, 1300.0), (0.0, -3.051757709276941e-05, 0.0), (1.0, 1.0, 1.0), "Suburbs_Column_Large_A_Shaft23_226", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5150.002, 2600.0, 1300.0), (0.0, -3.051757709276941e-05, 0.0), (1.0, 1.0, 1.0), "Suburbs_Column_Large_A_Shaft23_301", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1550.0015, 1199.9998, 1300.0), (0.0, -3.051757709276941e-05, 0.0), (1.0, 1.0, 1.0), "Suburbs_Column_Large_A_Shaft23_373", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2550.0, 1200.002, 1300.0), (0.0, 90.00001925454477, -0.0), (1.0, 1.0, 1.0), "Suburbs_Column_Large_A_Shaft23_409", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2750.0015, 1199.9998, 1300.0), (0.0, -3.051757709276941e-05, 0.0), (1.0, 1.0, 1.0), "Suburbs_Column_Large_A_Shaft23_447", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1349.9995, 2600.0017, 1300.0), (0.0, 90.00001925454477, -0.0), (1.0, 1.0, 1.0), "Suburbs_Column_Large_A_Shaft23_483", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1550.0012, 2600.0, 1300.0), (0.0, -3.051757709276941e-05, 0.0), (1.0, 1.0, 1.0), "Suburbs_Column_Large_A_Shaft23_521", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2550.0, 2600.0017, 1300.0), (0.0, 90.00001925454477, -0.0), (1.0, 1.0, 1.0), "Suburbs_Column_Large_A_Shaft23_557", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2549.998, 2400.0002, 1300.0), (0.0, -179.99995901885745, 0.0), (1.0, 1.0, 1.0), "Suburbs_Column_Large_A_Shaft23_575", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2750.0015, 2599.9998, 1300.0), (0.0, -3.051757709276941e-05, 0.0), (1.0, 1.0, 1.0), "Suburbs_Column_Large_A_Shaft23_593", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3750.0, 4000.0017, 1300.0), (0.0, 90.00001925454477, -0.0), (1.0, 1.0, 1.0), "Suburbs_Column_Large_A_Shaft23_629", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3749.9983, 3800.0, 1300.0), (0.0, -179.99995901885745, 0.0), (1.0, 1.0, 1.0), "Suburbs_Column_Large_A_Shaft23_647", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3950.0017, 4000.0, 1300.0), (0.0, -3.051757709276941e-05, 0.0), (1.0, 1.0, 1.0), "Suburbs_Column_Large_A_Shaft23_665", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3950.041, 3799.9983, 1300.0), (0.0, -89.99993822608693, 0.0), (1.0, 1.0, 1.0), "Suburbs_Column_Large_A_Shaft23_683", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4950.0, 4000.0017, 1300.0), (0.0, 90.00001925454477, -0.0), (1.0, 1.0, 1.0), "Suburbs_Column_Large_A_Shaft23_701", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5150.002, 4000.0, 1300.0), (0.0, -3.051757709276941e-05, 0.0), (1.0, 1.0, 1.0), "Suburbs_Column_Large_A_Shaft23_737", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5150.041, 3800.001, 1300.0), (0.0, -89.99993822608693, 0.0), (1.0, 1.0, 1.0), "Suburbs_Column_Large_A_Shaft23_755", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3750.0, 5400.0024, 1300.0), (0.0, 90.00001925454477, -0.0), (1.0, 1.0, 1.0), "Suburbs_Column_Large_A_Shaft23_773", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3749.9983, 5200.0, 1300.0), (0.0, -179.99995901885745, 0.0), (1.0, 1.0, 1.0), "Suburbs_Column_Large_A_Shaft23_791", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4949.998, 5200.0, 1300.0), (0.0, -179.99995901885745, 0.0), (1.0, 1.0, 1.0), "Suburbs_Column_Large_A_Shaft23_863", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1349.9978, 3799.9998, 1300.0), (0.0, -179.99995901885745, 0.0), (1.0, 1.0, 1.0), "Suburbs_Column_Large_A_Shaft23_935", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1550.002, 4000.0002, 1300.0), (0.0, -3.051757709276941e-05, 0.0), (1.0, 1.0, 1.0), "Suburbs_Column_Large_A_Shaft23_953", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2549.998, 3800.0002, 1300.0), (0.0, -179.99995901885745, 0.0), (1.0, 1.0, 1.0), "Suburbs_Column_Large_A_Shaft23_1007", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2750.0017, 4000.0, 1300.0), (0.0, -3.051757709276941e-05, 0.0), (1.0, 1.0, 1.0), "Suburbs_Column_Large_A_Shaft23_1025", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2550.0, 5400.003, 1300.0), (0.0, 90.00001925454477, -0.0), (1.0, 1.0, 1.0), "Suburbs_Column_Large_A_Shaft23_1133", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2749.9995, 2399.998, 1300.0), (0.0, -90.00005166594045, 0.0), (1.0, 1.0, 1.0), "Suburbs_Column_Large_A_Shaft23_1168", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2750.0015, 5400.0005, 1300.0), (0.0, -3.051757709276941e-05, 0.0), (1.0, 1.0, 1.0), "Suburbs_Column_Large_A_Shaft23_1169", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3950.0, 2399.9983, 1300.0), (0.0, -90.00005166594045, 0.0), (1.0, 1.0, 1.0), "Suburbs_Column_Large_A_Shaft23_1191", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2749.9998, 999.9988, 1300.0), (0.0, -89.99993822608693, 0.0), (1.0, 1.0, 1.0), "Suburbs_Column_Large_A_Shaft23_1255", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2749.9995, 3799.9983, 1300.0), (0.0, -90.00005166594045, 0.0), (1.0, 1.0, 1.0), "Suburbs_Column_Large_A_Shaft23_3286", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2750.0, 5199.998, 1300.0), (0.0, -90.00005166594045, 0.0), (1.0, 1.0, 1.0), "Suburbs_Column_Large_A_Shaft23_3305", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3950.0, 5199.998, 1300.0), (0.0, -90.00005166594045, 0.0), (1.0, 1.0, 1.0), "Suburbs_Column_Large_A_Shaft23_3324", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4950.039, 3800.0, 1300.0), (0.0, 179.99986339621609, -0.0), (1.0, 1.0, 1.0), "Suburbs_Column_Large_A_Shaft23_3343", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1550.0, 2399.9985, 1300.0), (0.0, 179.99978826413437, -0.0), (1.0, 1.0, 1.0), "Suburbs_Column_Large_A_Shaft24_7", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3750.0, 1200.0013, 1300.0), (0.0, -0.0001525878854640202, 0.0), (1.0, 1.0, 1.0), "Suburbs_Column_Large_A_Shaft24_25", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4950.0, 2600.0017, 1300.0), (0.0, -0.0001525878854640202, 0.0), (1.0, 1.0, 1.0), "Suburbs_Column_Large_A_Shaft24_38", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3749.9983, 1000.0, 1300.0), (0.0, 89.9998815062137, -0.0), (1.0, 1.0, 1.0), "Suburbs_Column_Large_A_Shaft24_43", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3750.0, 2600.0015, 1300.0), (0.0, -0.0001525878854640202, 0.0), (1.0, 1.0, 1.0), "Suburbs_Column_Large_A_Shaft24_191", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3749.9983, 2400.0, 1300.0), (0.0, 89.9998815062137, -0.0), (1.0, 1.0, 1.0), "Suburbs_Column_Large_A_Shaft24_209", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3950.0017, 2600.0, 1300.0), (0.0, -90.00022020536449, 0.0), (1.0, 1.0, 1.0), "Suburbs_Column_Large_A_Shaft24_227", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5150.002, 2600.0, 1300.0), (0.0, -90.00022020536449, 0.0), (1.0, 1.0, 1.0), "Suburbs_Column_Large_A_Shaft24_302", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1550.0015, 1199.9998, 1300.0), (0.0, -90.00022020536449, 0.0), (1.0, 1.0, 1.0), "Suburbs_Column_Large_A_Shaft24_374", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2550.0, 1200.002, 1300.0), (0.0, -0.0001525878854640202, 0.0), (1.0, 1.0, 1.0), "Suburbs_Column_Large_A_Shaft24_410", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2750.0015, 1199.9998, 1300.0), (0.0, -90.00022020536449, 0.0), (1.0, 1.0, 1.0), "Suburbs_Column_Large_A_Shaft24_448", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1349.9995, 2600.0017, 1300.0), (0.0, -0.0001525878854640202, 0.0), (1.0, 1.0, 1.0), "Suburbs_Column_Large_A_Shaft24_484", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1550.0012, 2600.0, 1300.0), (0.0, -90.00022020536449, 0.0), (1.0, 1.0, 1.0), "Suburbs_Column_Large_A_Shaft24_522", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2550.0, 2600.0017, 1300.0), (0.0, -0.0001525878854640202, 0.0), (1.0, 1.0, 1.0), "Suburbs_Column_Large_A_Shaft24_558", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2549.998, 2400.0002, 1300.0), (0.0, 89.9998815062137, -0.0), (1.0, 1.0, 1.0), "Suburbs_Column_Large_A_Shaft24_576", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2750.0015, 2599.9998, 1300.0), (0.0, -90.00022020536449, 0.0), (1.0, 1.0, 1.0), "Suburbs_Column_Large_A_Shaft24_594", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3750.0, 4000.0017, 1300.0), (0.0, -0.0001525878854640202, 0.0), (1.0, 1.0, 1.0), "Suburbs_Column_Large_A_Shaft24_630", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3749.9983, 3800.0, 1300.0), (0.0, 89.9998815062137, -0.0), (1.0, 1.0, 1.0), "Suburbs_Column_Large_A_Shaft24_648", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3950.0017, 4000.0, 1300.0), (0.0, -90.00022020536449, 0.0), (1.0, 1.0, 1.0), "Suburbs_Column_Large_A_Shaft24_666", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3950.041, 3799.9983, 1300.0), (0.0, 179.99986339621609, -0.0), (1.0, 1.0, 1.0), "Suburbs_Column_Large_A_Shaft24_684", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4950.0, 4000.0017, 1300.0), (0.0, -0.0001525878854640202, 0.0), (1.0, 1.0, 1.0), "Suburbs_Column_Large_A_Shaft24_702", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5150.002, 4000.0, 1300.0), (0.0, -90.00022020536449, 0.0), (1.0, 1.0, 1.0), "Suburbs_Column_Large_A_Shaft24_738", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5150.041, 3800.001, 1300.0), (0.0, 179.9998975471592, -0.0), (1.0, 1.0, 1.0), "Suburbs_Column_Large_A_Shaft24_756", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3750.0, 5400.0024, 1300.0), (0.0, -0.0001525878854640202, 0.0), (1.0, 1.0, 1.0), "Suburbs_Column_Large_A_Shaft24_774", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3749.9983, 5200.0, 1300.0), (0.0, 89.9998815062137, -0.0), (1.0, 1.0, 1.0), "Suburbs_Column_Large_A_Shaft24_792", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4949.998, 5200.0, 1300.0), (0.0, 89.9998815062137, -0.0), (1.0, 1.0, 1.0), "Suburbs_Column_Large_A_Shaft24_864", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1349.9978, 3799.9998, 1300.0), (0.0, 89.9998815062137, -0.0), (1.0, 1.0, 1.0), "Suburbs_Column_Large_A_Shaft24_936", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1550.002, 4000.0002, 1300.0), (0.0, -90.00022020536449, 0.0), (1.0, 1.0, 1.0), "Suburbs_Column_Large_A_Shaft24_954", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2549.998, 3800.0002, 1300.0), (0.0, 89.9998815062137, -0.0), (1.0, 1.0, 1.0), "Suburbs_Column_Large_A_Shaft24_1008", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2750.0017, 4000.0, 1300.0), (0.0, -90.00022020536449, 0.0), (1.0, 1.0, 1.0), "Suburbs_Column_Large_A_Shaft24_1026", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2550.0, 5400.003, 1300.0), (0.0, -0.0001525878854640202, 0.0), (1.0, 1.0, 1.0), "Suburbs_Column_Large_A_Shaft24_1134", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2749.9995, 2399.998, 1300.0), (0.0, 179.99978826413437, -0.0), (1.0, 1.0, 1.0), "Suburbs_Column_Large_A_Shaft24_1169", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2750.0015, 5400.0005, 1300.0), (0.0, -90.00022020536449, 0.0), (1.0, 1.0, 1.0), "Suburbs_Column_Large_A_Shaft24_1170", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3950.0, 2399.9983, 1300.0), (0.0, 179.99976777355934, -0.0), (1.0, 1.0, 1.0), "Suburbs_Column_Large_A_Shaft24_1192", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2749.9998, 999.9988, 1300.0), (0.0, 179.9998975471592, -0.0), (1.0, 1.0, 1.0), "Suburbs_Column_Large_A_Shaft24_1256", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2749.9995, 3799.9983, 1300.0), (0.0, 179.99976777355934, -0.0), (1.0, 1.0, 1.0), "Suburbs_Column_Large_A_Shaft24_3287", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2750.0, 5199.998, 1300.0), (0.0, 179.99976777355934, -0.0), (1.0, 1.0, 1.0), "Suburbs_Column_Large_A_Shaft24_3306", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3950.0, 5199.998, 1300.0), (0.0, 179.99976777355934, -0.0), (1.0, 1.0, 1.0), "Suburbs_Column_Large_A_Shaft24_3325", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4950.039, 3800.0, 1300.0), (0.0, 89.99979237503166, -0.0), (1.0, 1.0, 1.0), "Suburbs_Column_Large_A_Shaft24_3344", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (250.0, 5150.0, 1300.0), (0.0, 4.799999765332643e-05, -0.0), (1.0, 1.0, 0.5), "Suburbs_Column_Large_A_Shaft41_351", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1249.9999, 6150.0, 1300.0), (0.0, -89.99999818714215, 0.0), (1.0, 1.0, 0.5), "Suburbs_Column_Large_A_Shaft41_451", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (250.0, 5150.0, 1300.0), (0.0, -89.99999818714215, 0.0), (1.0, 1.0, 0.5), "Suburbs_Column_Large_A_Shaft42_352", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1249.9999, 6150.0, 1300.0), (0.0, 179.99992486791828, -0.0), (1.0, 1.0, 0.5), "Suburbs_Column_Large_A_Shaft42_452", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (250.0, 5150.0, 1500.0), (0.0, 4.799999765332643e-05, -0.0), (1.0, 1.0, 1.0), "Suburbs_Column_Large_A_Shaft43_353", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1249.9999, 6150.0, 1500.0), (0.0, -89.99999818714215, 0.0), (1.0, 1.0, 1.0), "Suburbs_Column_Large_A_Shaft43_453", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (250.0, 5150.0, 1500.0), (0.0, -89.99999818714215, 0.0), (1.0, 1.0, 1.0), "Suburbs_Column_Large_A_Shaft44_354", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1249.9999, 6150.0, 1500.0), (0.0, 179.99992486791828, -0.0), (1.0, 1.0, 1.0), "Suburbs_Column_Large_A_Shaft44_454", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (250.0, 6150.0, 1250.0), (0.0, -90.00005166594045, 0.0), (1.0, 1.0, 0.5), "Suburbs_Column_Large_A_Shaft45_492", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (250.0, 6150.0, 1450.0), (0.0, -89.99978589276644, 0.0), (1.0, 1.0, 1.0), "Suburbs_Column_Large_A_Shaft46_495", _folder)
if a: placed += 1
else: skipped += 1

# Batch 21: StaticMesh'Suburbs_Column_Single_Arch_A' (32 instances)
_mesh_path = "/Game/Art/Assets/Kits/Architecture/Suburbs/Suburbs_Column_Single_Arch_A"
_materials = ['/Game/Art/Assets/Kits/Architecture/Suburbs/Materials/Suburbs_Column_Single/MI_Suburbs_Column_Single_Arch_A']
_folder = "Reconstruction/BD_BB_Sandbox_DwarfHall_Voxels/Meshes"
a = spawn_static_mesh(_mesh_path, _materials, (6299.991, 2502.1387, 2134.3347), (0.0, 89.99958170155884, -0.0), (1.0, 1.0, 1.0), "Suburbs_Column_Single_Arch_A_112", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3250.0156, 6250.003, 2149.9685), (0.0, -179.9999590188648, 0.0), (1.0, 1.0, 1.0), "Suburbs_Column_Single_Arch_A_212", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2050.0007, 2700.0, 2150.0007), (0.0, 0.0, -0.0), (1.0, 1.0, 1.0), "Suburbs_Column_Single_Arch_A_3934", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3250.0007, 2700.0, 2150.0007), (0.0, 0.0, -0.0), (1.0, 1.0, 1.0), "Suburbs_Column_Single_Arch_A_3982", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4450.001, 2700.0, 2150.0007), (0.0, 0.0, -0.0), (1.0, 1.0, 1.0), "Suburbs_Column_Single_Arch_A_3999", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5650.001, 2700.0, 2150.0007), (0.0, 0.0, -0.0), (1.0, 1.0, 1.0), "Suburbs_Column_Single_Arch_A_4016", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4450.0635, 3699.987, 2149.965), (0.0, -179.9999590188648, 0.0), (1.0, 1.0, 1.0), "Suburbs_Column_Single_Arch_A_4033", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3250.0476, 3699.9868, 2149.965), (0.0, -179.9999590188648, 0.0), (1.0, 1.0, 1.0), "Suburbs_Column_Single_Arch_A_4050", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2050.0474, 3699.9868, 2149.965), (0.0, -179.9999590188648, 0.0), (1.0, 1.0, 1.0), "Suburbs_Column_Single_Arch_A_4067", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (800.00073, 2700.0, 2150.0007), (0.0, 0.0, -0.0), (1.0, 1.0, 1.0), "Suburbs_Column_Single_Arch_A_4084", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (800.01184, 3700.0227, 2149.965), (0.0, -179.9999590188648, 0.0), (1.0, 1.0, 1.0), "Suburbs_Column_Single_Arch_A_4101", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3250.0007, 1300.0, 2150.0007), (0.0, 0.0, -0.0), (1.0, 1.0, 1.0), "Suburbs_Column_Single_Arch_A_4152", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3250.0796, 2299.9863, 2149.965), (0.0, -179.9999590188648, 0.0), (1.0, 1.0, 1.0), "Suburbs_Column_Single_Arch_A_4169", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5649.8643, 2299.955, 2149.965), (0.0, -179.9999590188648, 0.0), (1.0, 1.0, 1.0), "Suburbs_Column_Single_Arch_A_4203", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3250.0007, 4100.0, 2150.0007), (0.0, 0.0, -0.0), (1.0, 1.0, 1.0), "Suburbs_Column_Single_Arch_A_4220", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3250.0476, 5099.9355, 2149.965), (0.0, -179.9999590188648, 0.0), (1.0, 1.0, 1.0), "Suburbs_Column_Single_Arch_A_4237", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2050.0007, 4100.0, 2150.0007), (0.0, 0.0, -0.0), (1.0, 1.0, 1.0), "Suburbs_Column_Single_Arch_A_4271", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2050.0793, 5099.8643, 2149.965), (0.0, -179.9999590188648, 0.0), (1.0, 1.0, 1.0), "Suburbs_Column_Single_Arch_A_4288", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1050.0118, 5099.9355, 2149.965), (0.0, -179.9999590188648, 0.0), (1.0, 1.0, 1.0), "Suburbs_Column_Single_Arch_A_5128", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1050.0007, 4100.0, 2150.0007), (0.0, 0.0, -0.0), (1.0, 1.0, 1.0), "Suburbs_Column_Single_Arch_A_5148", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5649.8643, 3700.0227, 2149.965), (0.0, -179.9999590188648, 0.0), (1.0, 1.0, 1.0), "Suburbs_Column_Single_Arch_A_5208", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4450.001, 4100.0, 2150.0007), (0.0, 0.0, -0.0), (1.0, 1.0, 1.0), "Suburbs_Column_Single_Arch_A_5228", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4450.0625, 5100.0, 2149.965), (0.0, -179.9999590188648, 0.0), (1.0, 1.0, 1.0), "Suburbs_Column_Single_Arch_A_5248", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2050.0027, 5249.9995, 2150.0007), (0.0, 0.0, -0.0), (1.0, 1.0, 1.0), "Suburbs_Column_Single_Arch_A_5308", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1050.0049, 5249.9995, 2150.0007), (0.0, 0.0, -0.0), (1.0, 1.0, 1.0), "Suburbs_Column_Single_Arch_A_5328", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3250.0027, 5499.9995, 2150.0007), (0.0, 0.0, -0.0), (1.0, 1.0, 1.0), "Suburbs_Column_Single_Arch_A_5348", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3250.0476, 899.98694, 2149.965), (0.0, -179.9999590188648, 0.0), (1.0, 1.0, 1.0), "Suburbs_Column_Single_Arch_A_5428", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2050.0007, 1300.0, 2150.0007), (0.0, 0.0, -0.0), (1.0, 1.0, 1.0), "Suburbs_Column_Single_Arch_A_5448", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2050.0793, 2299.9548, 2149.965), (0.0, -179.9999590188648, 0.0), (1.0, 1.0, 1.0), "Suburbs_Column_Single_Arch_A_5468", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2050.0808, 6249.9307, 2149.9666), (0.0, -179.9999590188648, 0.0), (1.0, 1.0, 1.0), "Suburbs_Column_Single_Arch_A_5548", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1050.0115, 6249.997, 2149.9666), (0.0, -179.9999590188648, 0.0), (1.0, 1.0, 1.0), "Suburbs_Column_Single_Arch_A_5568", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (6299.9907, 3902.4944, 2134.3347), (0.0, 89.99958170155884, -0.0), (1.0, 1.0, 1.0), "Suburbs_Column_Single_Arch_A2", _folder)
if a: placed += 1
else: skipped += 1

# Batch 22: StaticMesh'Suburbs_Column_Single_Capitol_A' (60 instances)
_mesh_path = "/Game/Art/Assets/Kits/Architecture/Suburbs/Suburbs_Column_Single_Capitol_A"
_materials = ['/Game/Art/Assets/Kits/Architecture/Suburbs/Materials/Suburbs_Column_Single/MI_Suburbs_Column_Single_Capitol_A_Dest']
_folder = "Reconstruction/BD_BB_Sandbox_DwarfHall_Voxels/Meshes"
a = spawn_static_mesh(_mesh_path, _materials, (965.0, 3715.0, 2100.0), (0.0, 0.0, -0.0), (1.0, 1.0, 1.0), "Suburbs_Column_Single_Capitol_A_127", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2215.0, 2315.0, 2100.0), (0.0, 0.0, -0.0), (1.0, 1.0, 1.0), "Suburbs_Column_Single_Capitol_A10", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1885.0, 2315.0, 2100.0), (0.0, 0.0, -0.0), (1.0, 1.0, 1.0), "Suburbs_Column_Single_Capitol_A11", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3415.0, 2315.0, 2100.0), (0.0, 0.0, -0.0), (1.0, 1.0, 1.0), "Suburbs_Column_Single_Capitol_A12", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3085.0, 2315.0, 2100.0), (0.0, 0.0, -0.0), (1.0, 1.0, 1.0), "Suburbs_Column_Single_Capitol_A13", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5815.0, 2315.0, 2100.0), (0.0, 0.0, -0.0), (1.0, 1.0, 1.0), "Suburbs_Column_Single_Capitol_A16", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5485.0, 2315.0, 2100.0), (0.0, 0.0, -0.0), (1.0, 1.0, 1.0), "Suburbs_Column_Single_Capitol_A17", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2215.0, 1290.0, 2100.0), (0.0, 0.0, -0.0), (1.0, 1.0, 1.0), "Suburbs_Column_Single_Capitol_A18", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1885.0, 1290.0, 2100.0), (0.0, 0.0, -0.0), (1.0, 1.0, 1.0), "Suburbs_Column_Single_Capitol_A19", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (635.0, 3715.0, 2100.0), (0.0, 0.0, -0.0), (1.0, 1.0, 1.0), "Suburbs_Column_Single_Capitol_A2", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3415.0, 1290.0, 2100.0), (0.0, 0.0, -0.0), (1.0, 1.0, 1.0), "Suburbs_Column_Single_Capitol_A20", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3085.0, 1290.0, 2100.0), (0.0, 0.0, -0.0), (1.0, 1.0, 1.0), "Suburbs_Column_Single_Capitol_A21", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5485.0, 1290.0, 2100.0), (0.0, 0.0, -0.0), (1.0, 1.0, 1.0), "Suburbs_Column_Single_Capitol_A25", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3415.0, 910.0, 2100.0), (0.0, 0.0, -0.0), (1.0, 1.0, 1.0), "Suburbs_Column_Single_Capitol_A28", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3085.0, 910.0, 2100.0), (0.0, 0.0, -0.0), (1.0, 1.0, 1.0), "Suburbs_Column_Single_Capitol_A29", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (965.0, 2685.0, 2100.0), (0.0, 0.0, -0.0), (1.0, 1.0, 1.0), "Suburbs_Column_Single_Capitol_A3", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4615.0, 860.0, 2100.0), (0.0, 0.0, -0.0), (1.0, 1.0, 1.0), "Suburbs_Column_Single_Capitol_A30", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4285.0, 860.0, 2100.0), (0.0, 0.0, -0.0), (1.0, 1.0, 1.0), "Suburbs_Column_Single_Capitol_A31", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2215.0, 2685.0, 2100.0), (0.0, 0.0, -0.0), (1.0, 1.0, 1.0), "Suburbs_Column_Single_Capitol_A34", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1885.0, 2685.0, 2100.0), (0.0, 0.0, -0.0), (1.0, 1.0, 1.0), "Suburbs_Column_Single_Capitol_A35", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3415.0, 2685.0, 2100.0), (0.0, 0.0, -0.0), (1.0, 1.0, 1.0), "Suburbs_Column_Single_Capitol_A36", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3085.0, 2685.0, 2100.0), (0.0, 0.0, -0.0), (1.0, 1.0, 1.0), "Suburbs_Column_Single_Capitol_A37", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4615.0, 2685.0, 2100.0), (0.0, 0.0, -0.0), (1.0, 1.0, 1.0), "Suburbs_Column_Single_Capitol_A38", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4285.0, 2685.0, 2100.0), (0.0, 0.0, -0.0), (1.0, 1.0, 1.0), "Suburbs_Column_Single_Capitol_A39", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (635.0, 2685.0, 2100.0), (0.0, 0.0, -0.0), (1.0, 1.0, 1.0), "Suburbs_Column_Single_Capitol_A4", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5815.0, 2685.0, 2100.0), (0.0, 0.0, -0.0), (1.0, 1.0, 1.0), "Suburbs_Column_Single_Capitol_A40", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5485.0, 2685.0, 2100.0), (0.0, 0.0, -0.0), (1.0, 1.0, 1.0), "Suburbs_Column_Single_Capitol_A41", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4615.0, 3710.0, 2100.0), (0.0, 0.0, -0.0), (1.0, 1.0, 1.0), "Suburbs_Column_Single_Capitol_A42", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4285.0, 3710.0, 2100.0), (0.0, 0.0, -0.0), (1.0, 1.0, 1.0), "Suburbs_Column_Single_Capitol_A43", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5815.0, 3710.0, 2100.0), (0.0, 0.0, -0.0), (1.0, 1.0, 1.0), "Suburbs_Column_Single_Capitol_A44", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5485.0, 3710.0, 2100.0), (0.0, 0.0, -0.0), (1.0, 1.0, 1.0), "Suburbs_Column_Single_Capitol_A45", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3415.0, 3710.0, 2100.0), (0.0, 0.0, -0.0), (1.0, 1.0, 1.0), "Suburbs_Column_Single_Capitol_A46", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3085.0, 3710.0, 2100.0), (0.0, 0.0, -0.0), (1.0, 1.0, 1.0), "Suburbs_Column_Single_Capitol_A47", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2215.0, 3710.0, 2100.0), (0.0, 0.0, -0.0), (1.0, 1.0, 1.0), "Suburbs_Column_Single_Capitol_A48", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1885.0, 3710.0, 2100.0), (0.0, 0.0, -0.0), (1.0, 1.0, 1.0), "Suburbs_Column_Single_Capitol_A49", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1215.0, 4090.0, 2100.0), (0.0, 0.0, -0.0), (1.0, 1.0, 1.0), "Suburbs_Column_Single_Capitol_A50", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (885.0, 4090.0, 2100.0), (0.0, 0.0, -0.0), (1.0, 1.0, 1.0), "Suburbs_Column_Single_Capitol_A51", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2215.0, 4090.0, 2100.0), (0.0, 0.0, -0.0), (1.0, 1.0, 1.0), "Suburbs_Column_Single_Capitol_A52", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1885.0, 4090.0, 2100.0), (0.0, 0.0, -0.0), (1.0, 1.0, 1.0), "Suburbs_Column_Single_Capitol_A53", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3415.0, 4090.0, 2100.0), (0.0, 0.0, -0.0), (1.0, 1.0, 1.0), "Suburbs_Column_Single_Capitol_A54", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3085.0, 4090.0, 2100.0), (0.0, 0.0, -0.0), (1.0, 1.0, 1.0), "Suburbs_Column_Single_Capitol_A55", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4615.0, 4090.0, 2100.0), (0.0, 0.0, -0.0), (1.0, 1.0, 1.0), "Suburbs_Column_Single_Capitol_A56", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4285.0, 4090.0, 2100.0), (0.0, 0.0, -0.0), (1.0, 1.0, 1.0), "Suburbs_Column_Single_Capitol_A57", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4615.0, 5115.0, 2100.0), (0.0, 0.0, -0.0), (1.0, 1.0, 1.0), "Suburbs_Column_Single_Capitol_A60", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4285.0, 5115.0, 2100.0), (0.0, 0.0, -0.0), (1.0, 1.0, 1.0), "Suburbs_Column_Single_Capitol_A61", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3415.0, 5115.0, 2100.0), (0.0, 0.0, -0.0), (1.0, 1.0, 1.0), "Suburbs_Column_Single_Capitol_A62", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3085.0, 5115.0, 2100.0), (0.0, 0.0, -0.0), (1.0, 1.0, 1.0), "Suburbs_Column_Single_Capitol_A63", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2215.0, 5115.0, 2100.0), (0.0, 0.0, -0.0), (1.0, 1.0, 1.0), "Suburbs_Column_Single_Capitol_A64", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1885.0, 5115.0, 2100.0), (0.0, 0.0, -0.0), (1.0, 1.0, 1.0), "Suburbs_Column_Single_Capitol_A65", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1215.0, 5115.0, 2100.0), (0.0, 0.0, -0.0), (1.0, 1.0, 1.0), "Suburbs_Column_Single_Capitol_A66", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (885.0, 5115.0, 2100.0), (0.0, 0.0, -0.0), (1.0, 1.0, 1.0), "Suburbs_Column_Single_Capitol_A67", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1215.0, 5240.0, 2100.0), (0.0, 0.0, -0.0), (1.0, 1.0, 1.0), "Suburbs_Column_Single_Capitol_A68", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (885.0, 5240.0, 2100.0), (0.0, 0.0, -0.0), (1.0, 1.0, 1.0), "Suburbs_Column_Single_Capitol_A69", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3415.0, 5490.0, 2100.0), (0.0, 0.0, -0.0), (1.0, 1.0, 1.0), "Suburbs_Column_Single_Capitol_A70_66", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1885.0, 5240.0, 2100.0), (0.0, 0.0, -0.0), (1.0, 1.0, 1.0), "Suburbs_Column_Single_Capitol_A71", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3085.0, 5490.0, 2100.0), (0.0, 0.0, -0.0), (1.0, 1.0, 1.0), "Suburbs_Column_Single_Capitol_A72", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2215.0, 6265.0, 2100.0), (0.0, 0.0, -0.0), (1.0, 1.0, 1.0), "Suburbs_Column_Single_Capitol_A79", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1885.0, 6265.0, 2100.0), (0.0, 0.0, -0.0), (1.0, 1.0, 1.0), "Suburbs_Column_Single_Capitol_A80", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3415.0, 6265.0, 2100.0), (0.0, 0.0, -0.0), (1.0, 1.0, 1.0), "Suburbs_Column_Single_Capitol_A81", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3085.0, 6265.0, 2100.0), (0.0, 0.0, -0.0), (1.0, 1.0, 1.0), "Suburbs_Column_Single_Capitol_A82", _folder)
if a: placed += 1
else: skipped += 1

# Batch 23: StaticMesh'Suburbs_Column_X_Large_A_ArchL' (45 instances)
_mesh_path = "/Game/Art/Assets/Kits/Architecture/Suburbs/Suburbs_Column_X_Large_A_ArchL"
_materials = ['/Game/Art/Assets/Kits/Architecture/Suburbs/Materials/Suburbs_Trim_Sheet_A/MI_Suburbs_Trim_Sheet_A']
_folder = "Reconstruction/BD_BB_Sandbox_DwarfHall_Voxels/Meshes"
a = spawn_static_mesh(_mesh_path, _materials, (3749.7275, 2350.0, 2149.965), (0.0, 89.99997063746636, -0.0), (0.3125, 0.5, 0.3125), "Suburbs_Column_X_Large_A_Arch105", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2999.7275, 2350.0005, 2149.965), (0.0, 89.99997063746636, -0.0), (0.3125, 0.5, 0.3125), "Suburbs_Column_X_Large_A_Arch107", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2249.7275, 2350.0005, 2149.965), (0.0, 89.99997063746636, -0.0), (0.3125, 0.5, 0.3125), "Suburbs_Column_X_Large_A_Arch109", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1499.7275, 2350.0007, 2149.965), (0.0, 89.99997063746636, -0.0), (0.3125, 0.5, 0.3125), "Suburbs_Column_X_Large_A_Arch111", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2050.002, 1249.999, 2150.0007), (0.0, -90.00005166594045, 0.0), (0.3125, 0.5, 0.3125), "Suburbs_Column_X_Large_A_Arch118", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5390.0, 2649.9988, 2150.5), (0.0, -90.00005166594045, 0.0), (0.3125, 0.5, 0.3125), "Suburbs_Column_X_Large_A_Arch12_283", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2800.002, 1249.9984, 2150.0007), (0.0, -90.00005166594045, 0.0), (0.3125, 0.5, 0.3125), "Suburbs_Column_X_Large_A_Arch120", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3550.002, 1249.9978, 2150.0007), (0.0, -90.00005166594045, 0.0), (0.3125, 0.5, 0.3125), "Suburbs_Column_X_Large_A_Arch122", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5149.7275, 3750.0415, 2149.965), (0.0, 89.99997063746636, -0.0), (0.3125, 0.5, 0.3125), "Suburbs_Column_X_Large_A_Arch16_248", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1200.0255, 6299.971, 2149.9666), (0.0, 89.99997063746636, -0.0), (0.3125, 0.5, 0.3125), "Suburbs_Column_X_Large_A_Arch19_265", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1950.0254, 6299.971, 2149.9666), (0.0, 89.99997063746636, -0.0), (0.3125, 0.5, 0.3125), "Suburbs_Column_X_Large_A_Arch22", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2792.527, 5169.457, 2150.0007), (0.0, 89.99997063746636, -0.0), (0.335581, 0.5, 0.3125), "Suburbs_Column_X_Large_A_Arch25", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5249.7275, 2350.0, 2149.965), (0.0, 89.99997063746636, -0.0), (0.3125, 0.5, 0.3125), "Suburbs_Column_X_Large_A_Arch26_303", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3542.527, 5169.4595, 2150.0007), (0.0, 89.99997063746636, -0.0), (0.335581, 0.5, 0.3125), "Suburbs_Column_X_Large_A_Arch28_205", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (6140.0, 2650.0, 2150.5), (0.0, -90.00005166594045, 0.0), (0.3125, 0.5, 0.3125), "Suburbs_Column_X_Large_A_Arch3_4004", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (542.5271, 5169.454, 2150.0007), (0.0, 89.99997063746636, -0.0), (0.335581, 0.5, 0.3125), "Suburbs_Column_X_Large_A_Arch3_5116", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (450.0255, 6299.971, 2149.9666), (0.0, 89.99997063746636, -0.0), (0.3125, 0.5, 0.3125), "Suburbs_Column_X_Large_A_Arch3_5556", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4292.527, 5169.461, 2150.0007), (0.0, 89.99997063746636, -0.0), (0.335581, 0.5, 0.3125), "Suburbs_Column_X_Large_A_Arch31_209", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1785.0059, 5200.0, 2150.0007), (0.0, -90.00002735739477, 0.0), (0.3125, 0.5, 0.3125), "Suburbs_Column_X_Large_A_Arch36", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2535.0059, 5200.0, 2150.0007), (0.0, -90.00002735739477, 0.0), (0.3125, 0.5, 0.3125), "Suburbs_Column_X_Large_A_Arch38", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5999.7275, 2350.0, 2149.965), (0.0, 89.99997063746636, -0.0), (0.3125, 0.5, 0.3125), "Suburbs_Column_X_Large_A_Arch4_4204", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5899.7275, 3750.0415, 2149.965), (0.0, 89.99997063746636, -0.0), (0.3125, 0.5, 0.3125), "Suburbs_Column_X_Large_A_Arch4_5209", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1035.0059, 5200.0, 2150.0007), (0.0, -90.00002735739477, 0.0), (0.3125, 0.5, 0.3125), "Suburbs_Column_X_Large_A_Arch4_5329", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3000.004, 5450.0, 2150.0007), (0.0, -90.00002735739477, 0.0), (0.3125, 0.5, 0.3125), "Suburbs_Column_X_Large_A_Arch4_5349", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3750.004, 5450.0, 2150.0007), (0.0, -90.00002735739477, 0.0), (0.3125, 0.5, 0.3125), "Suburbs_Column_X_Large_A_Arch41", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1085.2308, 4049.9995, 2150.0007), (0.0, -90.00005166594045, 0.0), (0.3125, 0.5, 0.3125), "Suburbs_Column_X_Large_A_Arch49", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3335.231, 4049.9985, 2150.0007), (0.0, -90.00005166594045, 0.0), (0.3125, 0.5, 0.3125), "Suburbs_Column_X_Large_A_Arch55", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4085.231, 4049.9983, 2150.0007), (0.0, -90.00005166594045, 0.0), (0.3125, 0.5, 0.3125), "Suburbs_Column_X_Large_A_Arch57", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4835.231, 4049.9978, 2150.0007), (0.0, -90.00005166594045, 0.0), (0.3125, 0.5, 0.3125), "Suburbs_Column_X_Large_A_Arch59", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (335.23087, 4050.0, 2150.0007), (0.0, -90.00005166594045, 0.0), (0.3125, 0.5, 0.3125), "Suburbs_Column_X_Large_A_Arch6", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4399.7275, 3750.0415, 2149.965), (0.0, 89.99997063746636, -0.0), (0.3125, 0.5, 0.3125), "Suburbs_Column_X_Large_A_Arch64", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3649.7275, 3750.0417, 2149.965), (0.0, 89.99997063746636, -0.0), (0.3125, 0.5, 0.3125), "Suburbs_Column_X_Large_A_Arch66", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2899.7275, 3750.0417, 2149.965), (0.0, 89.99997063746636, -0.0), (0.3125, 0.5, 0.3125), "Suburbs_Column_X_Large_A_Arch68", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2149.7275, 3750.0417, 2149.965), (0.0, 89.99997063746636, -0.0), (0.3125, 0.5, 0.3125), "Suburbs_Column_X_Large_A_Arch70", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1399.7275, 3750.0417, 2149.965), (0.0, 89.99997063746636, -0.0), (0.3125, 0.5, 0.3125), "Suburbs_Column_X_Large_A_Arch72", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (649.72754, 3750.0417, 2149.965), (0.0, 89.99997063746636, -0.0), (0.3125, 0.5, 0.3125), "Suburbs_Column_X_Large_A_Arch74", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (-100.272446, 3750.0417, 2149.965), (0.0, 89.99997063746636, -0.0), (0.3125, 0.5, 0.3125), "Suburbs_Column_X_Large_A_Arch75", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2700.0254, 6299.971, 2149.9666), (0.0, 89.99997063746636, -0.0), (0.3125, 0.5, 0.3125), "Suburbs_Column_X_Large_A_Arch77", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3450.0254, 6299.971, 2149.9666), (0.0, 89.99997063746636, -0.0), (0.3125, 0.5, 0.3125), "Suburbs_Column_X_Large_A_Arch79", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4640.0, 2649.9976, 2150.5), (0.0, -90.00005166594045, 0.0), (0.3125, 0.5, 0.3125), "Suburbs_Column_X_Large_A_Arch87_287", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3890.0, 2649.9968, 2150.5), (0.0, -90.00005166594045, 0.0), (0.3125, 0.5, 0.3125), "Suburbs_Column_X_Large_A_Arch90", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3140.0, 2649.9963, 2150.5), (0.0, -90.00005166594045, 0.0), (0.3125, 0.5, 0.3125), "Suburbs_Column_X_Large_A_Arch92", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2390.0, 2649.995, 2150.5), (0.0, -90.00005166594045, 0.0), (0.3125, 0.5, 0.3125), "Suburbs_Column_X_Large_A_Arch94", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1640.0, 2649.994, 2150.5), (0.0, -90.00005166594045, 0.0), (0.3125, 0.5, 0.3125), "Suburbs_Column_X_Large_A_Arch96", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (890.0, 2649.9924, 2150.5), (0.0, -90.00005166594045, 0.0), (0.3125, 0.5, 0.3125), "Suburbs_Column_X_Large_A_Arch98", _folder)
if a: placed += 1
else: skipped += 1

# Batch 24: StaticMesh'Suburbs_Column_X_Large_A_ArchR' (49 instances)
_mesh_path = "/Game/Art/Assets/Kits/Architecture/Suburbs/Suburbs_Column_X_Large_A_ArchR"
_materials = ['/Game/Art/Assets/Kits/Architecture/Suburbs/Materials/Suburbs_Trim_Sheet_A/MI_Suburbs_Trim_Sheet_A']
_folder = "Reconstruction/BD_BB_Sandbox_DwarfHall_Voxels/Meshes"
a = spawn_static_mesh(_mesh_path, _materials, (5999.729, 2350.0, 2149.964), (0.0, 89.99997063746636, -0.0), (0.3125, 0.5, 0.3125), "Suburbs_Column_X_Large_A_Arch_4194", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5899.729, 3750.0396, 2149.964), (0.0, 89.99997063746636, -0.0), (0.3125, 0.5, 0.3125), "Suburbs_Column_X_Large_A_Arch_5199", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3000.0044, 5450.0, 2150.0007), (0.0, -90.00002735739477, 0.0), (0.3125, 0.5, 0.3125), "Suburbs_Column_X_Large_A_Arch_5339", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (140.01904, 2649.9912, 2150.0007), (0.0, -89.9998815062137, 0.0), (0.3125, 0.5, 0.3125), "Suburbs_Column_X_Large_A_Arch101", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3749.729, 2350.0, 2149.964), (0.0, 89.99997063746636, -0.0), (0.3125, 0.5, 0.3125), "Suburbs_Column_X_Large_A_Arch104", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2999.729, 2350.0005, 2149.964), (0.0, 89.99997063746636, -0.0), (0.3125, 0.5, 0.3125), "Suburbs_Column_X_Large_A_Arch106", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2249.729, 2350.0005, 2149.964), (0.0, 89.99997063746636, -0.0), (0.3125, 0.5, 0.3125), "Suburbs_Column_X_Large_A_Arch108", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (542.5271, 5169.454, 2150.0007), (0.0, 90.00018131163026, -0.0), (0.33558074, 0.5, 0.3125), "Suburbs_Column_X_Large_A_Arch11_768", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1300.0024, 1249.9995, 2150.0007), (0.0, -90.00005166594045, 0.0), (0.3125, 0.5, 0.3125), "Suburbs_Column_X_Large_A_Arch115", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2050.0024, 1249.999, 2150.0007), (0.0, -90.00005166594045, 0.0), (0.3125, 0.5, 0.3125), "Suburbs_Column_X_Large_A_Arch117", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2800.0024, 1249.9984, 2150.0007), (0.0, -90.00005166594045, 0.0), (0.3125, 0.5, 0.3125), "Suburbs_Column_X_Large_A_Arch119", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3550.0024, 1249.9978, 2150.0007), (0.0, -90.00005166594045, 0.0), (0.3125, 0.5, 0.3125), "Suburbs_Column_X_Large_A_Arch121", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5249.729, 2350.0, 2149.964), (0.0, 89.99997063746636, -0.0), (0.3125, 0.5, 0.3125), "Suburbs_Column_X_Large_A_Arch13_302", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (6140.019, 2650.0, 2150.0007), (0.0, -89.9998815062137, 0.0), (0.3125, 0.5, 0.3125), "Suburbs_Column_X_Large_A_Arch15", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1292.5271, 5169.455, 2150.0007), (0.0, 90.00018131163026, -0.0), (0.335581, 0.5, 0.3125), "Suburbs_Column_X_Large_A_Arch17", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (450.0255, 6299.971, 2149.9666), (0.0, 89.99997063746636, -0.0), (0.3125, 0.5, 0.3125), "Suburbs_Column_X_Large_A_Arch2_5560", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5390.019, 2649.9988, 2150.0007), (0.0, -89.9998815062137, 0.0), (0.3125, 0.5, 0.3125), "Suburbs_Column_X_Large_A_Arch20_284", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1200.0255, 6299.971, 2149.9666), (0.0, 89.99997063746636, -0.0), (0.3125, 0.5, 0.3125), "Suburbs_Column_X_Large_A_Arch21_266", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2792.527, 5169.457, 2150.0007), (0.0, 90.00018131163026, -0.0), (0.335581, 0.5, 0.3125), "Suburbs_Column_X_Large_A_Arch27", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3542.527, 5169.46, 2150.0007), (0.0, 90.00018131163026, -0.0), (0.335581, 0.5, 0.3125), "Suburbs_Column_X_Large_A_Arch29", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4292.527, 5169.4624, 2150.0007), (0.0, 90.00018131163026, -0.0), (0.335581, 0.5, 0.3125), "Suburbs_Column_X_Large_A_Arch30_206", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5042.527, 5169.464, 2150.0007), (0.0, 90.00018131163026, -0.0), (0.335581, 0.5, 0.3125), "Suburbs_Column_X_Large_A_Arch32_210", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1035.0105, 5200.0, 2150.0007), (0.0, -90.00005166594045, 0.0), (0.3125, 0.5, 0.3125), "Suburbs_Column_X_Large_A_Arch37", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1785.0105, 5200.0, 2150.0007), (0.0, -90.00005166594045, 0.0), (0.3125, 0.5, 0.3125), "Suburbs_Column_X_Large_A_Arch39", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2535.0105, 5199.9995, 2150.0007), (0.0, -90.00005166594045, 0.0), (0.3125, 0.5, 0.3125), "Suburbs_Column_X_Large_A_Arch40", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1085.0104, 4049.9995, 2150.0007), (0.0, -90.00005166594045, 0.0), (0.3125, 0.5, 0.3125), "Suburbs_Column_X_Large_A_Arch48", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (335.01038, 4050.0, 2150.0007), (0.0, -90.00005166594045, 0.0), (0.3125, 0.5, 0.3125), "Suburbs_Column_X_Large_A_Arch5", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2585.0103, 4049.9988, 2150.0007), (0.0, -90.00005166594045, 0.0), (0.3125, 0.5, 0.3125), "Suburbs_Column_X_Large_A_Arch52", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3335.0103, 4049.9985, 2150.0007), (0.0, -90.00005166594045, 0.0), (0.3125, 0.5, 0.3125), "Suburbs_Column_X_Large_A_Arch54", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4085.0103, 4049.9983, 2150.0007), (0.0, -90.00005166594045, 0.0), (0.3125, 0.5, 0.3125), "Suburbs_Column_X_Large_A_Arch56", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4835.0103, 4049.9978, 2150.0007), (0.0, -90.00005166594045, 0.0), (0.3125, 0.5, 0.3125), "Suburbs_Column_X_Large_A_Arch58", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4399.729, 3750.0396, 2149.964), (0.0, 89.99997063746636, -0.0), (0.3125, 0.5, 0.3125), "Suburbs_Column_X_Large_A_Arch63", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3649.729, 3750.0398, 2149.964), (0.0, 89.99997063746636, -0.0), (0.3125, 0.5, 0.3125), "Suburbs_Column_X_Large_A_Arch65", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2899.729, 3750.0398, 2149.964), (0.0, 89.99997063746636, -0.0), (0.3125, 0.5, 0.3125), "Suburbs_Column_X_Large_A_Arch67", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2149.729, 3750.0398, 2149.964), (0.0, 89.99997063746636, -0.0), (0.3125, 0.5, 0.3125), "Suburbs_Column_X_Large_A_Arch69", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5149.729, 3750.0396, 2149.964), (0.0, 89.99997063746636, -0.0), (0.3125, 0.5, 0.3125), "Suburbs_Column_X_Large_A_Arch7", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1399.729, 3750.0398, 2149.964), (0.0, 89.99997063746636, -0.0), (0.3125, 0.5, 0.3125), "Suburbs_Column_X_Large_A_Arch71", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (649.729, 3750.0398, 2149.964), (0.0, 89.99997063746636, -0.0), (0.3125, 0.5, 0.3125), "Suburbs_Column_X_Large_A_Arch73", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1950.0254, 6299.971, 2149.9666), (0.0, 89.99997063746636, -0.0), (0.3125, 0.5, 0.3125), "Suburbs_Column_X_Large_A_Arch76", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2700.0254, 6299.971, 2149.9666), (0.0, 89.99997063746636, -0.0), (0.3125, 0.5, 0.3125), "Suburbs_Column_X_Large_A_Arch78", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (285.01056, 5200.0, 2150.0007), (0.0, -90.00005166594045, 0.0), (0.3125, 0.5, 0.3125), "Suburbs_Column_X_Large_A_Arch8", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3450.0254, 6299.971, 2149.9666), (0.0, 89.99997063746636, -0.0), (0.3125, 0.5, 0.3125), "Suburbs_Column_X_Large_A_Arch80", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3850.0244, 5949.971, 2151.377), (0.0, -9.155273700792082e-05, 0.0), (0.3125, 0.5, 0.3125), "Suburbs_Column_X_Large_A_Arch82", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4640.019, 2649.9976, 2150.0007), (0.0, -89.9998815062137, 0.0), (0.3125, 0.5, 0.3125), "Suburbs_Column_X_Large_A_Arch89", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3890.019, 2649.9968, 2150.0007), (0.0, -89.9998815062137, 0.0), (0.3125, 0.5, 0.3125), "Suburbs_Column_X_Large_A_Arch91", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3140.019, 2649.9963, 2150.0007), (0.0, -89.9998815062137, 0.0), (0.3125, 0.5, 0.3125), "Suburbs_Column_X_Large_A_Arch93", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2390.019, 2649.995, 2150.0007), (0.0, -89.9998815062137, 0.0), (0.3125, 0.5, 0.3125), "Suburbs_Column_X_Large_A_Arch95", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1640.019, 2649.994, 2150.0007), (0.0, -89.9998815062137, 0.0), (0.3125, 0.5, 0.3125), "Suburbs_Column_X_Large_A_Arch97", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (890.01904, 2649.9924, 2150.0007), (0.0, -89.9998815062137, 0.0), (0.3125, 0.5, 0.3125), "Suburbs_Column_X_Large_A_Arch99", _folder)
if a: placed += 1
else: skipped += 1

# Batch 25: StaticMesh'Suburbs_Column_X_Large_A_Base_1' (96 instances)
_mesh_path = "/Game/Art/Assets/Kits/Architecture/Suburbs/Suburbs_Column_X_Large_A_Base_1"
_materials = ['/Game/Art/Assets/Kits/Architecture/Suburbs/Materials/Suburbs_Trim_Sheet_A/MI_Suburbs_Trim_Sheet_A']
_folder = "Reconstruction/BD_BB_Sandbox_DwarfHall_Voxels/Meshes"
a = spawn_static_mesh(_mesh_path, _materials, (1399.999, 2500.0198, 900.0), (0.0, 89.9998815062137, -0.0), (0.5, 1.0, 1.0), "Suburbs_Column_X_Large_A_Base_12", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1449.9985, 2550.0198, 1700.0), (-0.00015258785899794667, -179.99995901885794, 179.99963116974615), (0.5, 1.0, 1.0), "Suburbs_Column_X_Large_A_Base_15", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5050.001, 2449.9805, 1700.0), (-0.0001525878866182784, 9.22080386819026e-05, 179.99963116979015), (0.5, 1.0, 1.0), "Suburbs_Column_X_Large_A_Base_25", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5100.001, 2499.9805, 900.0), (0.0, -90.00005166594045, 0.0), (0.5, 1.0, 1.0), "Suburbs_Column_X_Large_A_Base_28", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3900.0007, 1099.9805, 900.0), (0.0, -90.00005166594045, 0.0), (0.5, 1.0, 1.0), "Suburbs_Column_X_Large_A_Base_30", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3850.001, 1049.9805, 1700.0), (-0.0001525878866182784, 9.22080386819026e-05, 179.99963116979015), (0.5, 1.0, 1.0), "Suburbs_Column_X_Large_A_Base_33", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3850.0193, 1150.0007, 900.0), (0.0, -3.051757709276941e-05, 0.0), (0.5, 1.0, 1.0), "Suburbs_Column_X_Large_A_Base_48", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3900.0193, 1100.001, 1700.0), (-0.0001525878918860807, 90.0001326956692, 179.99963116976886), (0.5, 1.0, 1.0), "Suburbs_Column_X_Large_A_Base_51", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3849.9802, 1049.9993, 900.0), (0.0, 179.9998975471592, -0.0), (0.5, 1.0, 1.0), "Suburbs_Column_X_Large_A_Base_66", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3850.0396, 1150.019, 1700.0), (-0.00015258786715984288, -179.99981558486186, 179.99963116973848), (0.5, 1.0, 1.0), "Suburbs_Column_X_Large_A_Base_88", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1399.999, 3900.0203, 900.0), (0.0, 89.9998815062137, -0.0), (0.5, 1.0, 1.0), "Suburbs_Column_X_Large_A_Base_140", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1449.9988, 3950.0195, 1700.0), (-0.00015258785899794667, -179.99995901885794, 179.99963116974615), (0.5, 1.0, 1.0), "Suburbs_Column_X_Large_A_Base_143", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3900.001, 2499.9805, 900.0), (0.0, -90.00005166594045, 0.0), (0.5, 1.0, 1.0), "Suburbs_Column_X_Large_A_Base_196", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3850.001, 2449.9805, 1700.0), (-0.0001525878866182784, 9.22080386819026e-05, 179.99963116979015), (0.5, 1.0, 1.0), "Suburbs_Column_X_Large_A_Base_199", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3850.0195, 2550.001, 900.0), (0.0, -3.051757709276941e-05, 0.0), (0.5, 1.0, 1.0), "Suburbs_Column_X_Large_A_Base_214", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3900.0195, 2500.001, 1700.0), (-0.0001525878918860807, 90.0001326956692, 179.99963116976886), (0.5, 1.0, 1.0), "Suburbs_Column_X_Large_A_Base_217", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3849.98, 2449.999, 900.0), (0.0, 179.9998975471592, -0.0), (0.5, 1.0, 1.0), "Suburbs_Column_X_Large_A_Base_232", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3799.9805, 2499.999, 1700.0), (-0.000152587874233353, -89.99993822629096, 179.9996311697447), (0.5, 1.0, 1.0), "Suburbs_Column_X_Large_A_Base_235", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5100.0195, 2500.001, 1700.0), (-0.0001525878918860807, 90.0001326956692, 179.99963116976886), (0.5, 1.0, 1.0), "Suburbs_Column_X_Large_A_Base_292", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5049.9805, 2449.999, 900.0), (0.0, 179.9998975471592, -0.0), (0.5, 1.0, 1.0), "Suburbs_Column_X_Large_A_Base_307", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4999.9805, 2499.9993, 1700.0), (-0.000152587874233353, -89.99993822629096, 179.9996311697447), (0.5, 1.0, 1.0), "Suburbs_Column_X_Large_A_Base_310", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (150.005, 5050.0, 900.0), (0.0, -179.99992486791828, 0.0), (1.0, 1.0, 1.0), "Suburbs_Column_X_Large_A_Base_347", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (150.0, 5250.0, 1900.0), (0.0003141886821653087, -179.9998975471642, -179.99976777357637), (1.0, 1.0, 1.0), "Suburbs_Column_X_Large_A_Base_360", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1449.98, 1049.9985, 900.0), (0.0, 179.9998975471592, -0.0), (0.5, 1.0, 1.0), "Suburbs_Column_X_Large_A_Base_379", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1399.98, 1099.9988, 1700.0), (-0.000152587874233353, -89.99993822629096, 179.9996311697447), (0.5, 1.0, 1.0), "Suburbs_Column_X_Large_A_Base_382", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2700.0007, 1099.9805, 900.0), (0.0, -90.00005166594045, 0.0), (0.5, 1.0, 1.0), "Suburbs_Column_X_Large_A_Base_415", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2650.0005, 1049.9805, 1700.0), (-0.0001525878866182784, 9.22080386819026e-05, 179.99963116979015), (0.5, 1.0, 1.0), "Suburbs_Column_X_Large_A_Base_418", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2650.0195, 1150.001, 900.0), (0.0, -3.051757709276941e-05, 0.0), (0.5, 1.0, 1.0), "Suburbs_Column_X_Large_A_Base_433", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1150.0, 6249.995, 900.0), (0.0, 90.00001925454748, -0.0), (1.0, 1.0, 1.0), "Suburbs_Column_X_Large_A_Base_447", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2649.98, 1049.9993, 900.0), (0.0, 179.9998975471592, -0.0), (0.5, 1.0, 1.0), "Suburbs_Column_X_Large_A_Base_453", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2599.98, 1099.999, 1700.0), (-0.000152587874233353, -89.99993822629096, 179.9996311697447), (0.5, 1.0, 1.0), "Suburbs_Column_X_Large_A_Base_456", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1350.0, 6250.0, 1900.0), (0.0003141886794769195, 90.00005166724321, -179.99976777359922), (1.0, 1.0, 1.0), "Suburbs_Column_X_Large_A_Base_460", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1500.0005, 2499.9805, 900.0), (0.0, -90.00005166594045, 0.0), (0.5, 1.0, 1.0), "Suburbs_Column_X_Large_A_Base_489", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1450.001, 2449.9805, 1700.0), (-0.0001525878866182784, 9.22080386819026e-05, 179.99963116979015), (0.5, 1.0, 1.0), "Suburbs_Column_X_Large_A_Base_492", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1450.019, 2550.0007, 900.0), (0.0, -3.051757709276941e-05, 0.0), (0.5, 1.0, 1.0), "Suburbs_Column_X_Large_A_Base_507", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1449.98, 2449.999, 900.0), (0.0, 179.9998975471592, -0.0), (0.5, 1.0, 1.0), "Suburbs_Column_X_Large_A_Base_527", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1399.98, 2499.9993, 1700.0), (-0.000152587874233353, -89.99993822629096, 179.9996311697447), (0.5, 1.0, 1.0), "Suburbs_Column_X_Large_A_Base_530", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2700.0007, 2499.9805, 900.0), (0.0, -90.00005166594045, 0.0), (0.5, 1.0, 1.0), "Suburbs_Column_X_Large_A_Base_563", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2650.001, 2449.9805, 1700.0), (-0.0001525878866182784, 9.22080386819026e-05, 179.99963116979015), (0.5, 1.0, 1.0), "Suburbs_Column_X_Large_A_Base_566", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2650.019, 2550.001, 900.0), (0.0, -3.051757709276941e-05, 0.0), (0.5, 1.0, 1.0), "Suburbs_Column_X_Large_A_Base_581", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2700.0195, 2500.0007, 1700.0), (-0.0001525878918860807, 90.0001326956692, 179.99963116976886), (0.5, 1.0, 1.0), "Suburbs_Column_X_Large_A_Base_584", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2649.98, 2449.9993, 900.0), (0.0, 179.9998975471592, -0.0), (0.5, 1.0, 1.0), "Suburbs_Column_X_Large_A_Base_599", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2599.9802, 2499.9993, 1700.0), (-0.000152587874233353, -89.99993822629096, 179.9996311697447), (0.5, 1.0, 1.0), "Suburbs_Column_X_Large_A_Base_602", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3900.001, 3899.9807, 900.0), (0.0, -90.00005166594045, 0.0), (0.5, 1.0, 1.0), "Suburbs_Column_X_Large_A_Base_635", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3850.001, 3849.9805, 1700.0), (-0.0001525878866182784, 9.22080386819026e-05, 179.99963116979015), (0.5, 1.0, 1.0), "Suburbs_Column_X_Large_A_Base_638", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3850.0193, 3950.001, 900.0), (0.0, -3.051757709276941e-05, 0.0), (0.5, 1.0, 1.0), "Suburbs_Column_X_Large_A_Base_653", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3900.0195, 3900.001, 1700.0), (-0.0001525878918860807, 90.0001326956692, 179.99963116976886), (0.5, 1.0, 1.0), "Suburbs_Column_X_Large_A_Base_656", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3849.98, 3849.999, 900.0), (0.0, 179.9998975471592, -0.0), (0.5, 1.0, 1.0), "Suburbs_Column_X_Large_A_Base_671", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3799.9805, 3899.9993, 1700.0), (-0.000152587874233353, -89.99993822629096, 179.9996311697447), (0.5, 1.0, 1.0), "Suburbs_Column_X_Large_A_Base_674", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3800.04, 3900.0195, 900.0), (0.0, 89.99995443177896, -0.0), (0.5, 1.0, 1.0), "Suburbs_Column_X_Large_A_Base_689", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3850.04, 3950.0195, 1700.0), (-0.00015258787656216615, -179.99989754716083, 179.9996311697765), (0.5, 1.0, 1.0), "Suburbs_Column_X_Large_A_Base_692", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5100.001, 3899.9807, 900.0), (0.0, -90.00005166594045, 0.0), (0.5, 1.0, 1.0), "Suburbs_Column_X_Large_A_Base_707", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5050.001, 3849.9805, 1700.0), (-0.0001525878866182784, 9.22080386819026e-05, 179.99963116979015), (0.5, 1.0, 1.0), "Suburbs_Column_X_Large_A_Base_710", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5049.9805, 3849.999, 900.0), (0.0, 179.9998975471592, -0.0), (0.5, 1.0, 1.0), "Suburbs_Column_X_Large_A_Base_743", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4999.9805, 3899.9995, 1700.0), (-0.000152587874233353, -89.99993822629096, 179.9996311697447), (0.5, 1.0, 1.0), "Suburbs_Column_X_Large_A_Base_746", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5000.04, 3900.022, 900.0), (0.0, 90.00001925454477, -0.0), (0.5, 1.0, 1.0), "Suburbs_Column_X_Large_A_Base_761", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5050.04, 3950.022, 1700.0), (-0.00015258786715984288, -179.99981558486186, 179.99963116973848), (0.5, 1.0, 1.0), "Suburbs_Column_X_Large_A_Base_764", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3900.001, 5299.9805, 900.0), (0.0, -90.00005166594045, 0.0), (0.5, 1.0, 1.0), "Suburbs_Column_X_Large_A_Base_779", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3850.001, 5249.9805, 1700.0), (-0.0001525878866182784, 9.22080386819026e-05, 179.99963116979015), (0.5, 1.0, 1.0), "Suburbs_Column_X_Large_A_Base_782", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3850.0195, 5350.001, 900.0), (0.0, -3.051757709276941e-05, 0.0), (0.5, 1.0, 1.0), "Suburbs_Column_X_Large_A_Base_797", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3900.0195, 5300.001, 1700.0), (-0.0001525878918860807, 90.0001326956692, 179.99963116976886), (0.5, 1.0, 1.0), "Suburbs_Column_X_Large_A_Base_800", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5050.0195, 5350.0015, 900.0), (0.0, -3.051757709276941e-05, 0.0), (0.5, 1.0, 1.0), "Suburbs_Column_X_Large_A_Base_869", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5100.0195, 5300.001, 1700.0), (-0.0001525878918860807, 90.0001326956692, 179.99963116976886), (0.5, 1.0, 1.0), "Suburbs_Column_X_Large_A_Base_872", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1500.001, 3899.9802, 900.0), (0.0, -90.00005166594045, 0.0), (0.5, 1.0, 1.0), "Suburbs_Column_X_Large_A_Base_923", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1450.0005, 3849.9807, 1700.0), (-0.0001525878866182784, 9.22080386819026e-05, 179.99963116979015), (0.5, 1.0, 1.0), "Suburbs_Column_X_Large_A_Base_926", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1450.019, 3950.001, 900.0), (0.0, -3.051757709276941e-05, 0.0), (0.5, 1.0, 1.0), "Suburbs_Column_X_Large_A_Base_941", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1500.0193, 3900.0012, 1700.0), (-0.0001525878918860807, 90.0001326956692, 179.99963116976886), (0.5, 1.0, 1.0), "Suburbs_Column_X_Large_A_Base_944", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1449.9802, 3849.9988, 900.0), (0.0, 179.9998975471592, -0.0), (0.5, 1.0, 1.0), "Suburbs_Column_X_Large_A_Base_959", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1399.9802, 3899.9993, 1700.0), (-0.000152587874233353, -89.99993822629096, 179.9996311697447), (0.5, 1.0, 1.0), "Suburbs_Column_X_Large_A_Base_962", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2700.0007, 3899.9805, 900.0), (0.0, -90.00005166594045, 0.0), (0.5, 1.0, 1.0), "Suburbs_Column_X_Large_A_Base_995", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2650.0005, 3849.9805, 1700.0), (-0.0001525878866182784, 9.22080386819026e-05, 179.99963116979015), (0.5, 1.0, 1.0), "Suburbs_Column_X_Large_A_Base_998", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2650.019, 3950.001, 900.0), (0.0, -3.051757709276941e-05, 0.0), (0.5, 1.0, 1.0), "Suburbs_Column_X_Large_A_Base_1013", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2700.0195, 3900.0007, 1700.0), (-0.0001525878918860807, 90.0001326956692, 179.99963116976886), (0.5, 1.0, 1.0), "Suburbs_Column_X_Large_A_Base_1016", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2649.98, 3849.9993, 900.0), (0.0, 179.9998975471592, -0.0), (0.5, 1.0, 1.0), "Suburbs_Column_X_Large_A_Base_1031", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2599.9802, 3899.9993, 1700.0), (-0.000152587874233353, -89.99993822629096, 179.9996311697447), (0.5, 1.0, 1.0), "Suburbs_Column_X_Large_A_Base_1034", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2700.0005, 5299.9805, 900.0), (0.0, -90.00005166594045, 0.0), (0.5, 1.0, 1.0), "Suburbs_Column_X_Large_A_Base_1139", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2650.001, 5249.9814, 1700.0), (-0.0001525878866182784, 9.22080386819026e-05, 179.99963116979015), (0.5, 1.0, 1.0), "Suburbs_Column_X_Large_A_Base_1142", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4999.999, 2500.0198, 900.0), (0.0, 89.9998815062137, -0.0), (0.5, 1.0, 1.0), "Suburbs_Column_X_Large_A_Base_1152", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2650.0193, 5350.002, 900.0), (0.0, -3.051757709276941e-05, 0.0), (0.5, 1.0, 1.0), "Suburbs_Column_X_Large_A_Base_1157", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2700.0195, 5300.001, 1700.0), (-0.0001525878918860807, 90.0001326956692, 179.99963116976886), (0.5, 1.0, 1.0), "Suburbs_Column_X_Large_A_Base_1160", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2599.999, 2500.0198, 900.0), (0.0, 89.9998815062137, -0.0), (0.5, 1.0, 1.0), "Suburbs_Column_X_Large_A_Base_1174", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2649.9802, 5249.9995, 900.0), (0.0, 179.9998975471592, -0.0), (0.5, 1.0, 1.0), "Suburbs_Column_X_Large_A_Base_1175", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2599.9797, 5299.9995, 1700.0), (-0.000152587874233353, -89.99993822629096, 179.9996311697447), (0.5, 1.0, 1.0), "Suburbs_Column_X_Large_A_Base_1178", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2649.999, 2550.0195, 1700.0), (-0.00015258785899794667, -179.99995901885794, 179.99963116974615), (0.5, 1.0, 1.0), "Suburbs_Column_X_Large_A_Base_1180", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3799.9993, 2500.0198, 900.0), (0.0, 89.9998815062137, -0.0), (0.5, 1.0, 1.0), "Suburbs_Column_X_Large_A_Base_1197", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3849.9993, 2550.0198, 1700.0), (-0.00015258785899794667, -179.99995901885794, 179.99963116974615), (0.5, 1.0, 1.0), "Suburbs_Column_X_Large_A_Base_1199", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2599.9985, 1100.0198, 900.0), (0.0, 90.00001925454477, -0.0), (0.5, 1.0, 1.0), "Suburbs_Column_X_Large_A_Base_1261", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2649.9985, 1150.02, 1700.0), (-0.00015258786715984288, -179.99981558486186, 179.99963116973848), (0.5, 1.0, 1.0), "Suburbs_Column_X_Large_A_Base_1264", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2599.9993, 3900.0198, 900.0), (0.0, 89.99982478636315, -0.0), (0.5, 1.0, 1.0), "Suburbs_Column_X_Large_A_Base_3292", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2649.999, 3950.0195, 1700.0), (-0.00015258785899794667, -179.99995901885794, 179.99963116974615), (0.5, 1.0, 1.0), "Suburbs_Column_X_Large_A_Base_3294", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2599.9985, 5300.0195, 900.0), (0.0, 89.9998815062137, -0.0), (0.5, 1.0, 1.0), "Suburbs_Column_X_Large_A_Base_3311", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2649.9995, 5350.0195, 1700.0), (-0.00015258785899794667, -179.99995901885794, 179.99963116974615), (0.5, 1.0, 1.0), "Suburbs_Column_X_Large_A_Base_3313", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3799.999, 5300.0195, 900.0), (0.0, 89.9998815062137, -0.0), (0.5, 1.0, 1.0), "Suburbs_Column_X_Large_A_Base_3330", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3849.9993, 5350.0195, 1700.0), (-0.00015258785899794667, -179.99995901885794, 179.99963116974615), (0.5, 1.0, 1.0), "Suburbs_Column_X_Large_A_Base_3332", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5050.06, 3950.0012, 900.0), (0.0, -6.103515418554748e-05, 0.0), (0.5, 1.0, 1.0), "Suburbs_Column_X_Large_A_Base_3349", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5100.06, 3899.9995, 1700.0), (-0.0001525878948974861, 90.00005166712674, 179.99963116981755), (0.5, 1.0, 1.0), "Suburbs_Column_X_Large_A_Base_3351", _folder)
if a: placed += 1
else: skipped += 1

# Batch 26: StaticMesh'Suburbs_Column_X_Large_A_Base_1_R' (95 instances)
_mesh_path = "/Game/Art/Assets/Kits/Architecture/Suburbs/Suburbs_Column_X_Large_A_Base_1_R"
_materials = ['/Game/Art/Assets/Kits/Architecture/Suburbs/Materials/Suburbs_Trim_Sheet_A/MI_Suburbs_Trim_Sheet_A']
_folder = "Reconstruction/BD_BB_Sandbox_DwarfHall_Voxels/Meshes"
a = spawn_static_mesh(_mesh_path, _materials, (1449.9985, 2550.0198, 900.0), (0.0, -179.99928966033286, 0.0), (0.5, 1.0, 1.0), "Suburbs_Column_X_Large_A_Base_3", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1400.0049, 2500.0217, 1700.0), (0.00015709432902761566, 89.99993822628254, 179.99963116973436), (0.5, 1.0, 1.0), "Suburbs_Column_X_Large_A_Base_13", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5050.001, 2449.9805, 900.0), (0.0, 0.0007171698054120229, -0.0), (0.5, 1.0, 1.0), "Suburbs_Column_X_Large_A_Base_26", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5099.9946, 2499.9785, 1700.0), (0.00015709432794365317, -89.99999818834902, 179.99963116973228), (0.5, 1.0, 1.0), "Suburbs_Column_X_Large_A_Base_27", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3899.9946, 1099.9783, 1700.0), (0.00015709432794365317, -89.99999818834902, 179.99963116973228), (0.5, 1.0, 1.0), "Suburbs_Column_X_Large_A_Base_31", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3850.001, 1049.9805, 900.0), (0.0, 0.0007171698054120229, -0.0), (0.5, 1.0, 1.0), "Suburbs_Column_X_Large_A_Base_32", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3850.0212, 1149.9945, 1700.0), (0.0001570943318281843, 3.0735342025214286e-05, 179.9996311697717), (0.5, 1.0, 1.0), "Suburbs_Column_X_Large_A_Base_49", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3900.0193, 1100.001, 900.0), (0.0, 90.00072258395141, -0.0), (0.5, 1.0, 1.0), "Suburbs_Column_X_Large_A_Base_50", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3849.978, 1050.0052, 1700.0), (0.00015709431583650664, 179.99991120752708, 179.99963116974772), (0.5, 1.0, 1.0), "Suburbs_Column_X_Large_A_Base_67", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3850.0396, 1150.019, 900.0), (0.0, -179.99924184886228, 0.0), (0.5, 1.0, 1.0), "Suburbs_Column_X_Large_A_Base_87", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1400.0054, 3900.0217, 1700.0), (0.00015709432902761566, 89.99993822628254, 179.99963116973436), (0.5, 1.0, 1.0), "Suburbs_Column_X_Large_A_Base_141", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1449.9988, 3950.0195, 900.0), (0.0, -179.99928966033286, 0.0), (0.5, 1.0, 1.0), "Suburbs_Column_X_Large_A_Base_142", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3899.9946, 2499.9785, 1700.0), (0.00015709432794365317, -89.99999818834902, 179.99963116973228), (0.5, 1.0, 1.0), "Suburbs_Column_X_Large_A_Base_197", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3850.001, 2449.9805, 900.0), (0.0, 0.0007171698054120229, -0.0), (0.5, 1.0, 1.0), "Suburbs_Column_X_Large_A_Base_198", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3850.0215, 2549.9946, 1700.0), (0.0001570943318281843, 3.0735342025214286e-05, 179.9996311697717), (0.5, 1.0, 1.0), "Suburbs_Column_X_Large_A_Base_215", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3900.0195, 2500.001, 900.0), (0.0, 90.00072258395141, -0.0), (0.5, 1.0, 1.0), "Suburbs_Column_X_Large_A_Base_216", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3849.978, 2450.0054, 1700.0), (0.00015709431583650664, 179.99991120752708, 179.99963116974772), (0.5, 1.0, 1.0), "Suburbs_Column_X_Large_A_Base_233", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3799.9805, 2499.999, 900.0), (0.0, -89.99933213511346, 0.0), (0.5, 1.0, 1.0), "Suburbs_Column_X_Large_A_Base_234", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5100.0195, 2500.001, 900.0), (0.0, 90.00072258395141, -0.0), (0.5, 1.0, 1.0), "Suburbs_Column_X_Large_A_Base_291", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5049.9785, 2450.0054, 1700.0), (0.00015709431583650664, 179.99991120752708, 179.99963116974772), (0.5, 1.0, 1.0), "Suburbs_Column_X_Large_A_Base_308", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4999.9805, 2499.9993, 900.0), (0.0, -89.99933213511346, 0.0), (0.5, 1.0, 1.0), "Suburbs_Column_X_Large_A_Base_309", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (150.0, 5250.0, 900.0), (0.0, -179.9998975471592, 0.0), (1.0, 1.0, 1.0), "Suburbs_Column_X_Large_A_Base_348", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (150.00488, 5050.0, 1900.0), (0.0002936981200224604, 179.99989754716017, 179.99989754716017), (1.0, 1.0, 1.0), "Suburbs_Column_X_Large_A_Base_359", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1449.978, 1050.0056, 1700.0), (0.00015709431583650664, 179.99991120752708, 179.99963116974772), (0.5, 1.0, 1.0), "Suburbs_Column_X_Large_A_Base_380", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1399.98, 1099.9988, 900.0), (0.0, -89.99933213511346, 0.0), (0.5, 1.0, 1.0), "Suburbs_Column_X_Large_A_Base_381", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2699.9949, 1099.9785, 1700.0), (0.00015709432794365317, -89.99999818834902, 179.99963116973228), (0.5, 1.0, 1.0), "Suburbs_Column_X_Large_A_Base_416", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2650.0005, 1049.9805, 900.0), (0.0, 0.0007171698054120229, -0.0), (0.5, 1.0, 1.0), "Suburbs_Column_X_Large_A_Base_417", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2650.021, 1149.9949, 1700.0), (0.0001570943318281843, 3.0735342025214286e-05, 179.9996311697717), (0.5, 1.0, 1.0), "Suburbs_Column_X_Large_A_Base_434", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1350.0, 6250.0, 900.0), (0.0, 90.00005166594045, -0.0), (1.0, 1.0, 1.0), "Suburbs_Column_X_Large_A_Base_448", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2649.9775, 1050.0054, 1700.0), (0.00015709431583650664, 179.99991120752708, 179.99963116974772), (0.5, 1.0, 1.0), "Suburbs_Column_X_Large_A_Base_454", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2599.98, 1099.999, 900.0), (0.0, -89.99933213511346, 0.0), (0.5, 1.0, 1.0), "Suburbs_Column_X_Large_A_Base_455", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1150.0, 6249.995, 1900.0), (0.0002936981017453845, 89.99983450991463, 179.9998975471641), (1.0, 1.0, 1.0), "Suburbs_Column_X_Large_A_Base_459", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1499.9946, 2499.9785, 1700.0), (0.00015709432794365317, -89.99999818834902, 179.99963116973228), (0.5, 1.0, 1.0), "Suburbs_Column_X_Large_A_Base_490", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1450.001, 2449.9805, 900.0), (0.0, 0.0007171698054120229, -0.0), (0.5, 1.0, 1.0), "Suburbs_Column_X_Large_A_Base_491", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1449.9785, 2450.0054, 1700.0), (0.00015709431583650664, 179.99991120752708, 179.99963116974772), (0.5, 1.0, 1.0), "Suburbs_Column_X_Large_A_Base_528", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1399.98, 2499.9993, 900.0), (0.0, -89.99933213511346, 0.0), (0.5, 1.0, 1.0), "Suburbs_Column_X_Large_A_Base_529", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2699.9944, 2499.9788, 1700.0), (0.00015709432794365317, -89.99999818834902, 179.99963116973228), (0.5, 1.0, 1.0), "Suburbs_Column_X_Large_A_Base_564", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2650.001, 2449.9805, 900.0), (0.0, 0.0007171698054120229, -0.0), (0.5, 1.0, 1.0), "Suburbs_Column_X_Large_A_Base_565", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2650.0215, 2549.9946, 1700.0), (0.0001570943318281843, 3.0735342025214286e-05, 179.9996311697717), (0.5, 1.0, 1.0), "Suburbs_Column_X_Large_A_Base_582", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2700.0195, 2500.0007, 900.0), (0.0, 90.00072258395141, -0.0), (0.5, 1.0, 1.0), "Suburbs_Column_X_Large_A_Base_583", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2649.978, 2450.0054, 1700.0), (0.00015709431583650664, 179.99991120752708, 179.99963116974772), (0.5, 1.0, 1.0), "Suburbs_Column_X_Large_A_Base_600", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2599.9802, 2499.9993, 900.0), (0.0, -89.99933213511346, 0.0), (0.5, 1.0, 1.0), "Suburbs_Column_X_Large_A_Base_601", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3899.9946, 3899.9785, 1700.0), (0.00015709432794365317, -89.99999818834902, 179.99963116973228), (0.5, 1.0, 1.0), "Suburbs_Column_X_Large_A_Base_636", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3850.001, 3849.9805, 900.0), (0.0, 0.0007171698054120229, -0.0), (0.5, 1.0, 1.0), "Suburbs_Column_X_Large_A_Base_637", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3850.0215, 3949.9949, 1700.0), (0.0001570943318281843, 3.0735342025214286e-05, 179.9996311697717), (0.5, 1.0, 1.0), "Suburbs_Column_X_Large_A_Base_654", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3900.0195, 3900.001, 900.0), (0.0, 90.00072258395141, -0.0), (0.5, 1.0, 1.0), "Suburbs_Column_X_Large_A_Base_655", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3849.9783, 3850.0054, 1700.0), (0.00015709431583650664, 179.99991120752708, 179.99963116974772), (0.5, 1.0, 1.0), "Suburbs_Column_X_Large_A_Base_672", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3799.9805, 3899.9993, 900.0), (0.0, -89.99933213511346, 0.0), (0.5, 1.0, 1.0), "Suburbs_Column_X_Large_A_Base_673", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3800.0464, 3900.0217, 1700.0), (0.00015709433324715381, 89.99995929368254, 179.9996311698142), (0.5, 1.0, 1.0), "Suburbs_Column_X_Large_A_Base_690", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3850.04, 3950.0195, 900.0), (0.0, -179.99924184886228, 0.0), (0.5, 1.0, 1.0), "Suburbs_Column_X_Large_A_Base_691", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5099.9946, 3899.9785, 1700.0), (0.00015709432794365317, -89.99999818834902, 179.99963116973228), (0.5, 1.0, 1.0), "Suburbs_Column_X_Large_A_Base_708", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5050.001, 3849.9805, 900.0), (0.0, 0.0007171698054120229, -0.0), (0.5, 1.0, 1.0), "Suburbs_Column_X_Large_A_Base_709", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5049.9785, 3850.0056, 1700.0), (0.00015709431583650664, 179.99991120752708, 179.99963116974772), (0.5, 1.0, 1.0), "Suburbs_Column_X_Large_A_Base_744", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4999.9805, 3899.9995, 900.0), (0.0, -89.99933213511346, 0.0), (0.5, 1.0, 1.0), "Suburbs_Column_X_Large_A_Base_745", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5000.0464, 3900.024, 1700.0), (0.0001570943143331447, 90.00001925474311, 179.99963116976443), (0.5, 1.0, 1.0), "Suburbs_Column_X_Large_A_Base_762", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5050.04, 3950.022, 900.0), (0.0, -179.99924184886228, 0.0), (0.5, 1.0, 1.0), "Suburbs_Column_X_Large_A_Base_763", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3899.9946, 5299.9785, 1700.0), (0.00015709432794365317, -89.99999818834902, 179.99963116973228), (0.5, 1.0, 1.0), "Suburbs_Column_X_Large_A_Base_780", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3850.001, 5249.9805, 900.0), (0.0, 0.0007171698054120229, -0.0), (0.5, 1.0, 1.0), "Suburbs_Column_X_Large_A_Base_781", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3850.0215, 5349.995, 1700.0), (0.0001570943318281843, 3.0735342025214286e-05, 179.9996311697717), (0.5, 1.0, 1.0), "Suburbs_Column_X_Large_A_Base_798", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3900.0195, 5300.001, 900.0), (0.0, 90.00072258395141, -0.0), (0.5, 1.0, 1.0), "Suburbs_Column_X_Large_A_Base_799", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5050.0215, 5349.9946, 1700.0), (0.0001570943318281843, 3.0735342025214286e-05, 179.9996311697717), (0.5, 1.0, 1.0), "Suburbs_Column_X_Large_A_Base_870", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5100.0195, 5300.001, 900.0), (0.0, 90.00072258395141, -0.0), (0.5, 1.0, 1.0), "Suburbs_Column_X_Large_A_Base_871", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1499.9944, 3899.9788, 1700.0), (0.00015709432794365317, -89.99999818834902, 179.99963116973228), (0.5, 1.0, 1.0), "Suburbs_Column_X_Large_A_Base_924", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1450.0005, 3849.9807, 900.0), (0.0, 0.0007171698054120229, -0.0), (0.5, 1.0, 1.0), "Suburbs_Column_X_Large_A_Base_925", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1450.021, 3949.9946, 1700.0), (0.0001570943318281843, 3.0735342025214286e-05, 179.9996311697717), (0.5, 1.0, 1.0), "Suburbs_Column_X_Large_A_Base_942", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1500.0193, 3900.0012, 900.0), (0.0, 90.00072258395141, -0.0), (0.5, 1.0, 1.0), "Suburbs_Column_X_Large_A_Base_943", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1449.9785, 3850.0056, 1700.0), (0.00015709431583650664, 179.99991120752708, 179.99963116974772), (0.5, 1.0, 1.0), "Suburbs_Column_X_Large_A_Base_960", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1399.9802, 3899.9993, 900.0), (0.0, -89.99933213511346, 0.0), (0.5, 1.0, 1.0), "Suburbs_Column_X_Large_A_Base_961", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2699.9944, 3899.9788, 1700.0), (0.00015709432794365317, -89.99999818834902, 179.99963116973228), (0.5, 1.0, 1.0), "Suburbs_Column_X_Large_A_Base_996", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2650.0005, 3849.9805, 900.0), (0.0, 0.0007171698054120229, -0.0), (0.5, 1.0, 1.0), "Suburbs_Column_X_Large_A_Base_997", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2650.0217, 3949.9946, 1700.0), (0.0001570943318281843, 3.0735342025214286e-05, 179.9996311697717), (0.5, 1.0, 1.0), "Suburbs_Column_X_Large_A_Base_1014", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2700.0195, 3900.0007, 900.0), (0.0, 90.00072258395141, -0.0), (0.5, 1.0, 1.0), "Suburbs_Column_X_Large_A_Base_1015", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2649.9778, 3850.0054, 1700.0), (0.00015709431583650664, 179.99991120752708, 179.99963116974772), (0.5, 1.0, 1.0), "Suburbs_Column_X_Large_A_Base_1032", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2599.9802, 3899.9993, 900.0), (0.0, -89.99933213511346, 0.0), (0.5, 1.0, 1.0), "Suburbs_Column_X_Large_A_Base_1033", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2699.9944, 5299.9785, 1700.0), (0.00015709432794365317, -89.99999818834902, 179.99963116973228), (0.5, 1.0, 1.0), "Suburbs_Column_X_Large_A_Base_1140", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2650.001, 5249.9814, 900.0), (0.0, 0.0007171698054120229, -0.0), (0.5, 1.0, 1.0), "Suburbs_Column_X_Large_A_Base_1141", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5000.0054, 2500.0217, 1700.0), (0.00015709432902761566, 89.99993822628254, 179.99963116973436), (0.5, 1.0, 1.0), "Suburbs_Column_X_Large_A_Base_1153", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2650.0212, 5349.995, 1700.0), (0.0001570943318281843, 3.0735342025214286e-05, 179.9996311697717), (0.5, 1.0, 1.0), "Suburbs_Column_X_Large_A_Base_1158", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2700.0195, 5300.001, 900.0), (0.0, 90.00072258395141, -0.0), (0.5, 1.0, 1.0), "Suburbs_Column_X_Large_A_Base_1159", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2649.9778, 5250.006, 1700.0), (0.00015709431583650664, 179.99991120752708, 179.99963116974772), (0.5, 1.0, 1.0), "Suburbs_Column_X_Large_A_Base_1176", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2599.9797, 5299.9995, 900.0), (0.0, -89.99933213511346, 0.0), (0.5, 1.0, 1.0), "Suburbs_Column_X_Large_A_Base_1177", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2600.0051, 2500.0217, 1700.0), (0.00015709432902761566, 89.99993822628254, 179.99963116973436), (0.5, 1.0, 1.0), "Suburbs_Column_X_Large_A_Base_1179", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2649.999, 2550.0195, 900.0), (0.0, -179.99928966033286, 0.0), (0.5, 1.0, 1.0), "Suburbs_Column_X_Large_A_Base_1184", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3800.0056, 2500.0217, 1700.0), (0.00015709435102652272, 89.99992202060832, 179.9996311698036), (0.5, 1.0, 1.0), "Suburbs_Column_X_Large_A_Base_1198", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3849.9993, 2550.0198, 900.0), (0.0, -179.99936479259367, 0.0), (0.5, 1.0, 1.0), "Suburbs_Column_X_Large_A_Base_1203", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2600.0044, 1100.022, 1700.0), (0.0001570943143331447, 90.00001925474311, 179.99963116976443), (0.5, 1.0, 1.0), "Suburbs_Column_X_Large_A_Base_1262", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2649.9985, 1150.02, 900.0), (0.0, -179.99924184886228, 0.0), (0.5, 1.0, 1.0), "Suburbs_Column_X_Large_A_Base_1263", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2600.0056, 3900.022, 1700.0), (0.0001570943355625076, 89.99988150640931, 179.99963116980618), (0.5, 1.0, 1.0), "Suburbs_Column_X_Large_A_Base_3293", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2649.999, 3950.0195, 900.0), (0.0, -179.99936479259367, 0.0), (0.5, 1.0, 1.0), "Suburbs_Column_X_Large_A_Base_3298", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2600.006, 5300.022, 1700.0), (0.00015709435102652272, 89.99992202060832, 179.9996311698036), (0.5, 1.0, 1.0), "Suburbs_Column_X_Large_A_Base_3312", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2649.9995, 5350.0195, 900.0), (0.0, -179.99936479259367, 0.0), (0.5, 1.0, 1.0), "Suburbs_Column_X_Large_A_Base_3317", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3800.0059, 5300.022, 1700.0), (0.00015709435102652272, 89.99992202060832, 179.9996311698036), (0.5, 1.0, 1.0), "Suburbs_Column_X_Large_A_Base_3331", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3849.9993, 5350.0195, 900.0), (0.0, -179.99936479259367, 0.0), (0.5, 1.0, 1.0), "Suburbs_Column_X_Large_A_Base_3336", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5050.062, 3949.9946, 1700.0), (0.00015709433438907948, -6.103515561524457e-05, 179.9996311697834), (0.5, 1.0, 1.0), "Suburbs_Column_X_Large_A_Base_3350", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5100.06, 3899.9995, 900.0), (0.0, 90.00067396651535, -0.0), (0.5, 1.0, 1.0), "Suburbs_Column_X_Large_A_Base_3355", _folder)
if a: placed += 1
else: skipped += 1

# Batch 27: StaticMesh'Suburbs_Column_X_Large_A_Base_A' (33 instances)
_mesh_path = "/Game/Art/Assets/Kits/Architecture/Suburbs/Suburbs_Column_X_Large_A_Base_A"
_materials = ['/Game/Art/Assets/Kits/Architecture/Suburbs/Materials/Suburbs_Trim_Sheet_A/MI_Suburbs_Trim_Sheet_A']
_folder = "Reconstruction/BD_BB_Sandbox_DwarfHall_Voxels/Meshes"
a = spawn_static_mesh(_mesh_path, _materials, (2650.0, 1099.9993, 800.0), (0.0, 90.00001925454477, -0.0), (0.875, 0.875, 1.0), "Suburbs_Column_X_Large_A_Base3", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1450.0, 2499.9985, 800.0), (0.0, 89.99992202041271, -0.0), (0.875, 0.875, 1.0), "Suburbs_Column_X_Large_A_Base3_18", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5049.9995, 2500.0015, 800.0), (0.0, -90.00002735739477, 0.0), (0.875, 0.875, 1.0), "Suburbs_Column_X_Large_A_Base3_45", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2650.0005, 2499.9985, 800.0), (0.0, 89.99992202041271, -0.0), (0.875, 0.875, 1.0), "Suburbs_Column_X_Large_A_Base3_1183", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3849.9995, 1100.0012, 800.0), (0.0, -90.00002735739477, 0.0), (0.875, 0.875, 1.0), "Suburbs_Column_X_Large_A_Base3_1304", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3849.9983, 1099.9995, 800.0), (0.0, 0.0, -0.0), (0.875, 0.875, 1.0), "Suburbs_Column_X_Large_A_Base3_1337", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3849.9985, 2499.9995, 800.0), (0.0, 0.0, -0.0), (0.875, 0.875, 1.0), "Suburbs_Column_X_Large_A_Base3_1601", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5050.0015, 2500.0005, 800.0), (0.0, 179.99991120752276, -0.0), (0.875, 0.875, 1.0), "Suburbs_Column_X_Large_A_Base3_1766", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1450.0015, 1100.0002, 800.0), (0.0, 179.99991120752276, -0.0), (0.875, 0.875, 1.0), "Suburbs_Column_X_Large_A_Base3_1898", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2649.999, 1100.001, 800.0), (0.0, -90.00002735739477, 0.0), (0.875, 0.875, 1.0), "Suburbs_Column_X_Large_A_Base3_1964", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2650.0012, 1100.0005, 800.0), (0.0, 179.99991120752276, -0.0), (0.875, 0.875, 1.0), "Suburbs_Column_X_Large_A_Base3_2030", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1449.9993, 2500.0012, 800.0), (0.0, -90.00002735739477, 0.0), (0.875, 0.875, 1.0), "Suburbs_Column_X_Large_A_Base3_2096", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1450.001, 2500.0007, 800.0), (0.0, 179.99991120752276, -0.0), (0.875, 0.875, 1.0), "Suburbs_Column_X_Large_A_Base3_2162", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2649.9993, 2500.0012, 800.0), (0.0, -90.00002735739477, 0.0), (0.875, 0.875, 1.0), "Suburbs_Column_X_Large_A_Base3_2228", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2649.9983, 2499.9998, 800.0), (0.0, 0.0, -0.0), (0.875, 0.875, 1.0), "Suburbs_Column_X_Large_A_Base3_2261", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2650.0012, 2500.0007, 800.0), (0.0, 179.99991120752276, -0.0), (0.875, 0.875, 1.0), "Suburbs_Column_X_Large_A_Base3_2294", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3849.9995, 3900.0015, 800.0), (0.0, -90.00002735739477, 0.0), (0.875, 0.875, 1.0), "Suburbs_Column_X_Large_A_Base3_2360", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5050.0415, 3900.0007, 800.0), (0.0, 90.00001925454477, -0.0), (0.875, 0.875, 1.0), "Suburbs_Column_X_Large_A_Base3_2591", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3849.9995, 5300.0015, 800.0), (0.0, -90.00002735739477, 0.0), (0.875, 0.875, 1.0), "Suburbs_Column_X_Large_A_Base3_2624", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3849.9983, 5300.0, 800.0), (0.0, 0.0, -0.0), (0.875, 0.875, 1.0), "Suburbs_Column_X_Large_A_Base3_2657", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1449.999, 3900.0012, 800.0), (0.0, -90.00002735739477, 0.0), (0.875, 0.875, 1.0), "Suburbs_Column_X_Large_A_Base3_2888", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1449.9983, 3899.9995, 800.0), (0.0, 0.0, -0.0), (0.875, 0.875, 1.0), "Suburbs_Column_X_Large_A_Base3_2921", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1450.0012, 3900.0005, 800.0), (0.0, 179.99991120752276, -0.0), (0.875, 0.875, 1.0), "Suburbs_Column_X_Large_A_Base3_2954", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2649.9993, 3900.0012, 800.0), (0.0, -90.00002735739477, 0.0), (0.875, 0.875, 1.0), "Suburbs_Column_X_Large_A_Base3_3020", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2649.9983, 3899.9998, 800.0), (0.0, 0.0, -0.0), (0.875, 0.875, 1.0), "Suburbs_Column_X_Large_A_Base3_3053", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2650.0015, 3900.0005, 800.0), (0.0, 179.99991120752276, -0.0), (0.875, 0.875, 1.0), "Suburbs_Column_X_Large_A_Base3_3086", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2649.9998, 5300.002, 800.0), (0.0, -90.00002735739477, 0.0), (0.875, 0.875, 1.0), "Suburbs_Column_X_Large_A_Base3_3152", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2649.9983, 5300.0, 800.0), (0.0, 0.0, -0.0), (0.875, 0.875, 1.0), "Suburbs_Column_X_Large_A_Base3_3185", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2650.0015, 5300.001, 800.0), (0.0, 179.99991120752276, -0.0), (0.875, 0.875, 1.0), "Suburbs_Column_X_Large_A_Base3_3218", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1450.0, 3899.9983, 800.0), (0.0, 89.99992202041271, -0.0), (0.875, 0.875, 1.0), "Suburbs_Column_X_Large_A_Base3_3279", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2650.0005, 3899.9983, 800.0), (0.0, 89.9998815062137, -0.0), (0.875, 0.875, 1.0), "Suburbs_Column_X_Large_A_Base3_3297", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2650.0002, 5299.9985, 800.0), (0.0, 89.9998815062137, -0.0), (0.875, 0.875, 1.0), "Suburbs_Column_X_Large_A_Base3_3316", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5050.039, 3899.9995, 800.0), (0.0, -9.155273700792082e-05, 0.0), (0.875, 0.875, 1.0), "Suburbs_Column_X_Large_A_Base3_3354", _folder)
if a: placed += 1
else: skipped += 1

# Batch 28: StaticMesh'Suburbs_Column_X_Large_A_Base_B' (2 instances)
_mesh_path = "/Game/Art/Assets/Kits/Architecture/Suburbs/Suburbs_Column_X_Large_A_Base_B"
_materials = ['/Game/Art/Assets/Kits/Architecture/Suburbs/Materials/Suburbs_Trim_Sheet_A/MI_Suburbs_Trim_Sheet_A']
_folder = "Reconstruction/BD_BB_Sandbox_DwarfHall_Voxels/Meshes"
a = spawn_static_mesh(_mesh_path, _materials, (150.0, 5150.0, 800.0), (0.0, -179.9998975471592, 0.0), (1.0, 1.0387702, 1.0), "Suburbs_Column_X_Large_A_Base_B_1074", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1250.0, 6300.0, 850.0), (0.0, 90.00002735739477, -0.0), (1.0, 1.0490932, 1.0), "Suburbs_Column_X_Large_A_Base_B2_146", _folder)
if a: placed += 1
else: skipped += 1

# Batch 29: StaticMesh'Suburbs_Column_X_Large_A_CapitalL' (44 instances)
_mesh_path = "/Game/Art/Assets/Kits/Architecture/Suburbs/Suburbs_Column_X_Large_A_CapitalL"
_materials = ['/Game/Art/Assets/Kits/Architecture/Suburbs/Materials/Suburbs_Trim_Sheet_A/MI_Suburbs_Trim_Sheet_A']
_folder = "Reconstruction/BD_BB_Sandbox_DwarfHall_Voxels/Meshes"
a = spawn_static_mesh(_mesh_path, _materials, (1399.999, 2500.0198, 1700.0), (0.0, 89.99975996369572, -0.0), (1.0, 1.0, 1.0), "Suburbs_Column_X_Large_A_Captol2_17", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3900.0007, 1099.9805, 1700.0), (0.0, -90.00018131163026, 0.0), (1.0, 1.0, 1.0), "Suburbs_Column_X_Large_A_Captol2_35", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5100.001, 2499.9805, 1700.0), (0.0, -90.00018131163026, 0.0), (1.0, 1.0, 1.0), "Suburbs_Column_X_Large_A_Captol2_44", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3850.0193, 1150.0007, 1700.0), (0.0, -0.0001525878854640202, 0.0), (1.0, 1.0, 1.0), "Suburbs_Column_X_Large_A_Captol2_53", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3849.9802, 1049.9993, 1700.0), (0.0, 179.99976777355934, -0.0), (1.0, 1.0, 1.0), "Suburbs_Column_X_Large_A_Captol2_72", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3900.001, 2499.9805, 1700.0), (0.0, -90.00018131163026, 0.0), (1.0, 1.0, 1.0), "Suburbs_Column_X_Large_A_Captol2_201", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3850.0195, 2550.001, 1700.0), (0.0, -0.0001525878854640202, 0.0), (1.0, 1.0, 1.0), "Suburbs_Column_X_Large_A_Captol2_219", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3849.98, 2449.999, 1700.0), (0.0, 179.99976777355934, -0.0), (1.0, 1.0, 1.0), "Suburbs_Column_X_Large_A_Captol2_237", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5049.9805, 2449.999, 1700.0), (0.0, 179.99976777355934, -0.0), (1.0, 1.0, 1.0), "Suburbs_Column_X_Large_A_Captol2_312", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1449.98, 1049.9985, 1700.0), (0.0, 179.99976777355934, -0.0), (1.0, 1.0, 1.0), "Suburbs_Column_X_Large_A_Captol2_384", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2700.0007, 1099.9805, 1700.0), (0.0, -90.00018131163026, 0.0), (1.0, 1.0, 1.0), "Suburbs_Column_X_Large_A_Captol2_420", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2649.98, 1049.9993, 1700.0), (0.0, 179.99976777355934, -0.0), (1.0, 1.0, 1.0), "Suburbs_Column_X_Large_A_Captol2_458", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1500.0005, 2499.9805, 1700.0), (0.0, -90.00018131163026, 0.0), (1.0, 1.0, 1.0), "Suburbs_Column_X_Large_A_Captol2_494", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1449.98, 2449.999, 1700.0), (0.0, 179.99976777355934, -0.0), (1.0, 1.0, 1.0), "Suburbs_Column_X_Large_A_Captol2_532", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2700.0007, 2499.9805, 1700.0), (0.0, -90.00018131163026, 0.0), (1.0, 1.0, 1.0), "Suburbs_Column_X_Large_A_Captol2_568", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2650.019, 2550.001, 1700.0), (0.0, -0.0001525878854640202, 0.0), (1.0, 1.0, 1.0), "Suburbs_Column_X_Large_A_Captol2_586", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2649.98, 2449.9993, 1700.0), (0.0, 179.99976777355934, -0.0), (1.0, 1.0, 1.0), "Suburbs_Column_X_Large_A_Captol2_604", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3900.001, 3899.9807, 1700.0), (0.0, -90.00018131163026, 0.0), (1.0, 1.0, 1.0), "Suburbs_Column_X_Large_A_Captol2_640", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3850.0193, 3950.001, 1700.0), (0.0, -0.0001525878854640202, 0.0), (1.0, 1.0, 1.0), "Suburbs_Column_X_Large_A_Captol2_658", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3849.98, 3849.999, 1700.0), (0.0, 179.99976777355934, -0.0), (1.0, 1.0, 1.0), "Suburbs_Column_X_Large_A_Captol2_676", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3800.04, 3900.0195, 1700.0), (0.0, 89.99979237503166, -0.0), (1.0, 1.0, 1.0), "Suburbs_Column_X_Large_A_Captol2_694", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5100.001, 3899.9807, 1700.0), (0.0, -90.00018131163026, 0.0), (1.0, 1.0, 1.0), "Suburbs_Column_X_Large_A_Captol2_712", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5000.04, 3900.022, 1700.0), (0.0, 89.9998815062137, -0.0), (1.0, 1.0, 1.0), "Suburbs_Column_X_Large_A_Captol2_766", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3900.001, 5299.9805, 1700.0), (0.0, -90.00018131163026, 0.0), (1.0, 1.0, 1.0), "Suburbs_Column_X_Large_A_Captol2_784", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3850.0195, 5350.001, 1700.0), (0.0, -0.0001525878854640202, 0.0), (1.0, 1.0, 1.0), "Suburbs_Column_X_Large_A_Captol2_802", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5050.0195, 5350.0015, 1700.0), (0.0, -0.0001525878854640202, 0.0), (1.0, 1.0, 1.0), "Suburbs_Column_X_Large_A_Captol2_874", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1500.001, 3899.9802, 1700.0), (0.0, -90.00018131163026, 0.0), (1.0, 1.0, 1.0), "Suburbs_Column_X_Large_A_Captol2_928", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1450.019, 3950.001, 1700.0), (0.0, -0.0001525878854640202, 0.0), (1.0, 1.0, 1.0), "Suburbs_Column_X_Large_A_Captol2_946", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1449.9802, 3849.9988, 1700.0), (0.0, 179.99976777355934, -0.0), (1.0, 1.0, 1.0), "Suburbs_Column_X_Large_A_Captol2_964", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2700.0007, 3899.9805, 1700.0), (0.0, -90.00018131163026, 0.0), (1.0, 1.0, 1.0), "Suburbs_Column_X_Large_A_Captol2_1000", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2650.019, 3950.001, 1700.0), (0.0, -0.0001525878854640202, 0.0), (1.0, 1.0, 1.0), "Suburbs_Column_X_Large_A_Captol2_1018", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2649.98, 3849.9993, 1700.0), (0.0, 179.99976777355934, -0.0), (1.0, 1.0, 1.0), "Suburbs_Column_X_Large_A_Captol2_1036", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2700.0005, 5299.9805, 1700.0), (0.0, -90.00018131163026, 0.0), (1.0, 1.0, 1.0), "Suburbs_Column_X_Large_A_Captol2_1144", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4999.999, 2500.0198, 1700.0), (0.0, 89.99975996369572, -0.0), (1.0, 1.0, 1.0), "Suburbs_Column_X_Large_A_Captol2_1156", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2650.0193, 5350.002, 1700.0), (0.0, -0.0001525878854640202, 0.0), (1.0, 1.0, 1.0), "Suburbs_Column_X_Large_A_Captol2_1162", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2649.9802, 5249.9995, 1700.0), (0.0, 179.99976777355934, -0.0), (1.0, 1.0, 1.0), "Suburbs_Column_X_Large_A_Captol2_1180", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2599.999, 2500.0198, 1700.0), (0.0, 89.99975996369572, -0.0), (1.0, 1.0, 1.0), "Suburbs_Column_X_Large_A_Captol2_1182", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3799.9993, 2500.0198, 1700.0), (0.0, 89.99971782898, -0.0), (1.0, 1.0, 1.0), "Suburbs_Column_X_Large_A_Captol2_1201", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2599.9985, 1100.0198, 1700.0), (0.0, 89.9998815062137, -0.0), (1.0, 1.0, 1.0), "Suburbs_Column_X_Large_A_Captol2_1266", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1399.999, 3900.0203, 1700.0), (0.0, 89.99975996369572, -0.0), (1.0, 1.0, 1.0), "Suburbs_Column_X_Large_A_Captol2_3278", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2599.9993, 3900.0198, 1700.0), (0.0, 89.999695141049, -0.0), (1.0, 1.0, 1.0), "Suburbs_Column_X_Large_A_Captol2_3296", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2599.9985, 5300.0195, 1700.0), (0.0, 89.99971782898, -0.0), (1.0, 1.0, 1.0), "Suburbs_Column_X_Large_A_Captol2_3315", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3799.999, 5300.0195, 1700.0), (0.0, 89.99971782898, -0.0), (1.0, 1.0, 1.0), "Suburbs_Column_X_Large_A_Captol2_3334", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5050.06, 3950.0012, 1700.0), (0.0, -0.0002136230511090266, 0.0), (1.0, 1.0, 1.0), "Suburbs_Column_X_Large_A_Captol2_3353", _folder)
if a: placed += 1
else: skipped += 1

# Batch 30: StaticMesh'Suburbs_Column_X_Large_A_CapitalR1' (44 instances)
_mesh_path = "/Game/Art/Assets/Kits/Architecture/Suburbs/Suburbs_Column_X_Large_A_CapitalR1"
_materials = ['/Game/Art/Assets/Kits/Architecture/Suburbs/Materials/Suburbs_Trim_Sheet_A/MI_Suburbs_Trim_Sheet_A']
_folder = "Reconstruction/BD_BB_Sandbox_DwarfHall_Voxels/Meshes"
a = spawn_static_mesh(_mesh_path, _materials, (1450.6362, 2550.0571, 1699.5), (0.01999879423723968, -179.98007634043458, -0.019989015858909567), (1.0, 1.0, 1.0), "Suburbs_Column_X_Large_A_Captol_16", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3849.3635, 1049.9424, 1699.5), (0.019998794087636156, 0.019988475044310897, -0.019989016010913213), (1.0, 1.0, 1.0), "Suburbs_Column_X_Large_A_Captol_34", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5049.3633, 2449.9429, 1699.5), (0.019998794087636156, 0.019988475044310897, -0.019989016010913213), (1.0, 1.0, 1.0), "Suburbs_Column_X_Large_A_Captol_43", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3900.057, 1099.3636, 1699.5), (0.019998793760219426, 90.02000262190859, -0.01998901448987932), (1.0, 1.0, 1.0), "Suburbs_Column_X_Large_A_Captol_52", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3849.3633, 2449.9429, 1699.5), (0.019998794087636156, 0.019988475044310897, -0.019989016010913213), (1.0, 1.0, 1.0), "Suburbs_Column_X_Large_A_Captol_200", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3900.0571, 2499.3635, 1699.5), (0.019998793760219426, 90.02000262190859, -0.01998901448987932), (1.0, 1.0, 1.0), "Suburbs_Column_X_Large_A_Captol_218", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3799.9429, 2500.6367, 1699.5), (0.019998792260865234, -89.9800787550863, -0.019989016835321942), (1.0, 1.0, 1.0), "Suburbs_Column_X_Large_A_Captol_236", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5100.057, 2499.3635, 1699.5), (0.019998793760219426, 90.02000262190859, -0.01998901448987932), (1.0, 1.0, 1.0), "Suburbs_Column_X_Large_A_Captol_293", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4999.943, 2500.6367, 1699.5), (0.019998792260865234, -89.9800787550863, -0.019989016835321942), (1.0, 1.0, 1.0), "Suburbs_Column_X_Large_A_Captol_311", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1399.9424, 1100.636, 1699.5), (0.019998792260865234, -89.9800787550863, -0.019989016835321942), (1.0, 1.0, 1.0), "Suburbs_Column_X_Large_A_Captol_383", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2649.3633, 1049.9426, 1699.5), (0.019998794087636156, 0.019988475044310897, -0.019989016010913213), (1.0, 1.0, 1.0), "Suburbs_Column_X_Large_A_Captol_419", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2599.943, 1100.6362, 1699.5), (0.019998792260865234, -89.9800787550863, -0.019989016835321942), (1.0, 1.0, 1.0), "Suburbs_Column_X_Large_A_Captol_457", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1449.3633, 2449.9426, 1699.5), (0.019998794087636156, 0.019988475044310897, -0.019989016010913213), (1.0, 1.0, 1.0), "Suburbs_Column_X_Large_A_Captol_493", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1399.9424, 2500.6367, 1699.5), (0.019998792260865234, -89.9800787550863, -0.019989016835321942), (1.0, 1.0, 1.0), "Suburbs_Column_X_Large_A_Captol_531", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2649.3633, 2449.9429, 1699.5), (0.019998794087636156, 0.019988475044310897, -0.019989016010913213), (1.0, 1.0, 1.0), "Suburbs_Column_X_Large_A_Captol_567", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2700.057, 2499.3635, 1699.5), (0.019998793760219426, 90.02000262190859, -0.01998901448987932), (1.0, 1.0, 1.0), "Suburbs_Column_X_Large_A_Captol_585", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2599.9426, 2500.6367, 1699.5), (0.019998792260865234, -89.9800787550863, -0.019989016835321942), (1.0, 1.0, 1.0), "Suburbs_Column_X_Large_A_Captol_603", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3849.3633, 3849.9429, 1699.5), (0.019998794087636156, 0.019988475044310897, -0.019989016010913213), (1.0, 1.0, 1.0), "Suburbs_Column_X_Large_A_Captol_639", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3900.0571, 3899.3635, 1699.5), (0.019998793760219426, 90.02000262190859, -0.01998901448987932), (1.0, 1.0, 1.0), "Suburbs_Column_X_Large_A_Captol_657", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3799.9429, 3900.6367, 1699.5), (0.019998792260865234, -89.9800787550863, -0.019989016835321942), (1.0, 1.0, 1.0), "Suburbs_Column_X_Large_A_Captol_675", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3850.6777, 3950.0574, 1699.5), (0.019998790288531923, -179.9799738839728, -0.019989012828568912), (1.0, 1.0, 1.0), "Suburbs_Column_X_Large_A_Captol_693", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5049.3633, 3849.9429, 1699.5), (0.019998794087636156, 0.019988475044310897, -0.019989016010913213), (1.0, 1.0, 1.0), "Suburbs_Column_X_Large_A_Captol_711", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5050.6777, 3950.0596, 1699.5), (0.019998793964235793, -179.9799465666636, -0.01998901613673599), (1.0, 1.0, 1.0), "Suburbs_Column_X_Large_A_Captol_765", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3849.3635, 5249.943, 1699.5), (0.019998794087636156, 0.019988475044310897, -0.019989016010913213), (1.0, 1.0, 1.0), "Suburbs_Column_X_Large_A_Captol_783", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3900.0571, 5299.3643, 1699.5), (0.019998793760219426, 90.02000262190859, -0.01998901448987932), (1.0, 1.0, 1.0), "Suburbs_Column_X_Large_A_Captol_801", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5100.057, 5299.3643, 1699.5), (0.019998793760219426, 90.02000262190859, -0.01998901448987932), (1.0, 1.0, 1.0), "Suburbs_Column_X_Large_A_Captol_873", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1449.3633, 3849.943, 1699.5), (0.019998794087636156, 0.019988475044310897, -0.019989016010913213), (1.0, 1.0, 1.0), "Suburbs_Column_X_Large_A_Captol_927", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1500.0571, 3899.3638, 1699.5), (0.019998793760219426, 90.02000262190859, -0.01998901448987932), (1.0, 1.0, 1.0), "Suburbs_Column_X_Large_A_Captol_945", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1399.9429, 3900.6365, 1699.5), (0.019998792260865234, -89.9800787550863, -0.019989016835321942), (1.0, 1.0, 1.0), "Suburbs_Column_X_Large_A_Captol_963", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2649.363, 3849.9429, 1699.5), (0.019998794087636156, 0.019988475044310897, -0.019989016010913213), (1.0, 1.0, 1.0), "Suburbs_Column_X_Large_A_Captol_999", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2700.057, 3899.3635, 1699.5), (0.019998793760219426, 90.02000262190859, -0.01998901448987932), (1.0, 1.0, 1.0), "Suburbs_Column_X_Large_A_Captol_1017", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2599.9426, 3900.6367, 1699.5), (0.019998792260865234, -89.9800787550863, -0.019989016835321942), (1.0, 1.0, 1.0), "Suburbs_Column_X_Large_A_Captol_1035", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2649.363, 5249.9434, 1699.5), (0.019998794087636156, 0.019988475044310897, -0.019989016010913213), (1.0, 1.0, 1.0), "Suburbs_Column_X_Large_A_Captol_1143", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5050.6367, 2550.0571, 1699.5), (0.01999879423723968, -179.98007634043458, -0.019989015858909567), (1.0, 1.0, 1.0), "Suburbs_Column_X_Large_A_Captol_1155", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2700.0571, 5299.3643, 1699.5), (0.019998793760219426, 90.02000262190859, -0.01998901448987932), (1.0, 1.0, 1.0), "Suburbs_Column_X_Large_A_Captol_1161", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2599.9426, 5300.6367, 1699.5), (0.019998792260865234, -89.9800787550863, -0.019989016835321942), (1.0, 1.0, 1.0), "Suburbs_Column_X_Large_A_Captol_1179", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2650.6362, 2550.057, 1699.5), (0.01999879423723968, -179.98007634043458, -0.019989015858909567), (1.0, 1.0, 1.0), "Suburbs_Column_X_Large_A_Captol_1181", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3850.6367, 2550.0574, 1699.5), (0.01999879423723968, -179.98007634043458, -0.019989015858909567), (1.0, 1.0, 1.0), "Suburbs_Column_X_Large_A_Captol_1200", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2650.6357, 1150.0579, 1699.5), (0.019998793964235793, -179.9799465666636, -0.01998901613673599), (1.0, 1.0, 1.0), "Suburbs_Column_X_Large_A_Captol_1265", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1450.6362, 3950.0571, 1699.5), (0.01999879423723968, -179.98007634043458, -0.019989015858909567), (1.0, 1.0, 1.0), "Suburbs_Column_X_Large_A_Captol_3277", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2650.6362, 3950.057, 1699.5), (0.01999879423723968, -179.98007634043458, -0.019989015858909567), (1.0, 1.0, 1.0), "Suburbs_Column_X_Large_A_Captol_3295", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2650.6367, 5350.057, 1699.5), (0.01999879423723968, -179.98007634043458, -0.019989015858909567), (1.0, 1.0, 1.0), "Suburbs_Column_X_Large_A_Captol_3314", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3850.6367, 5350.0576, 1699.5), (0.01999879423723968, -179.98007634043458, -0.019989015858909567), (1.0, 1.0, 1.0), "Suburbs_Column_X_Large_A_Captol_3333", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5100.0977, 3899.3623, 1699.5), (0.0199987911726626, 90.01995399719607, -0.019989016228240883), (1.0, 1.0, 1.0), "Suburbs_Column_X_Large_A_Captol_3352", _folder)
if a: placed += 1
else: skipped += 1

# Batch 31: StaticMesh'Suburbs_Column_X_Large_A_Capitol' (2 instances)
_mesh_path = "/Game/Art/Assets/Kits/Architecture/Suburbs/Suburbs_Column_X_Large_A_Capitol"
_materials = ['/Game/Art/Assets/Kits/Architecture/Suburbs/Materials/Suburbs_Trim_Sheet_A/MI_Suburbs_Trim_Sheet_A']
_folder = "Reconstruction/BD_BB_Sandbox_DwarfHall_Voxels/Meshes"
a = spawn_static_mesh(_mesh_path, _materials, (150.0, 5150.0, 1900.0), (0.0, -179.9998975471592, 0.0), (1.0, 1.0, 1.0), "Suburbs_Column_X_Large_A_Capitol_1077", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1250.0, 6250.0, 1900.0), (0.0, 90.00005166594045, -0.0), (1.0, 1.0, 1.0), "Suburbs_Column_X_Large_A_Capitol_1805", _folder)
if a: placed += 1
else: skipped += 1

# Batch 32: StaticMesh'Suburbs_Column_X_Large_A_Captol_Corner' (1 instances)
_mesh_path = "/Game/Art/Assets/Kits/Architecture/Suburbs/Suburbs_Column_X_Large_A_Captol_Corner"
_materials = ['/Game/Art/Assets/Kits/Architecture/Suburbs/Materials/Suburbs_Trim_Sheet_A/MI_Suburbs_Trim_Sheet_A']
_folder = "Reconstruction/BD_BB_Sandbox_DwarfHall_Voxels/Meshes"
a = spawn_static_mesh(_mesh_path, _materials, (150.0, 6250.0, 1850.0), (0.0, 90.00001925454477, -0.0), (1.0, 1.0, 1.0), "Suburbs_Column_X_Large_A_Captol_Corner5_496", _folder)
if a: placed += 1
else: skipped += 1

# Batch 33: StaticMesh'Suburbs_Column_X_Large_A_Lower_Corner' (2 instances)
_mesh_path = "/Game/Art/Assets/Kits/Architecture/Suburbs/Suburbs_Column_X_Large_A_Lower_Corner"
_materials = ['/Game/Art/Assets/Kits/Architecture/Suburbs/Materials/Suburbs_Trim_Sheet_A/MI_Suburbs_Trim_Sheet_A']
_folder = "Reconstruction/BD_BB_Sandbox_DwarfHall_Voxels/Meshes"
a = spawn_static_mesh(_mesh_path, _materials, (150.0, 6250.0, 850.0), (0.0, 90.00001925454477, -0.0), (1.0, 1.0, 1.0), "Suburbs_Column_X_Large_A_Lower_Corner13_489", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (150.0, 6250.0005, 1850.0), (-3.0517576774376916e-05, 179.99963116977088, -179.9997677735757), (1.0, 1.0, 1.0), "Suburbs_Column_X_Large_A_Lower_Corner14_493", _folder)
if a: placed += 1
else: skipped += 1

# Batch 34: StaticMesh'Suburbs_Column_X_Large_A_Shaft' (149 instances)
_mesh_path = "/Game/Art/Assets/Kits/Architecture/Suburbs/Suburbs_Column_X_Large_A_Shaft"
_materials = ['/Game/Art/Assets/Kits/Architecture/Suburbs/Materials/Suburbs_Column_X_Large_A/MI_Suburbs_Column_X_Large_A_Shaft']
_folder = "Reconstruction/BD_BB_Sandbox_DwarfHall_Voxels/Meshes"
a = spawn_static_mesh(_mesh_path, _materials, (5799.983, 2449.888, 2363.3804), (-90.0, 143.13436039968178, -53.13477522113375), (0.3125, 0.75, 0.625), "Suburbs_Column_X_Large_A_Shaft_109", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5800.19, 3449.8882, 2363.3804), (-90.0, 90.00033014173464, -0.0002797214466454534), (0.3125, 0.75, 0.625), "Suburbs_Column_X_Large_A_Shaft_129", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3250.1284, 5749.995, 2363.3481), (-90.0, 0.009073072503357336, -180.00893018915448), (0.3125, 0.75, 0.625), "Suburbs_Column_X_Large_A_Shaft_209", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2049.8882, 3200.0085, 2363.3804), (-90.0, -0.0035067583095234095, 0.0035154893949095787), (0.3125, 0.75, 0.625), "Suburbs_Column_X_Large_A_Shaft_3931", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3249.8882, 3200.0085, 2363.3804), (-90.0, -0.0035067583095234095, 0.0035154893949095787), (0.3125, 0.75, 0.625), "Suburbs_Column_X_Large_A_Shaft_3979", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4449.888, 3200.0085, 2363.3804), (-90.0, -0.0035067583095234095, 0.0035154893949095787), (0.3125, 0.75, 0.625), "Suburbs_Column_X_Large_A_Shaft_3996", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5649.888, 3200.0085, 2364.6504), (-90.0, 0.004647983535453326, -0.004643013693960199), (0.3125, 0.75, 0.625), "Suburbs_Column_X_Large_A_Shaft_4013", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4450.1123, 3199.9912, 2363.3447), (-90.0, -0.3286359960515908, 180.32869478223907), (0.3125, 0.75, 0.625), "Suburbs_Column_X_Large_A_Shaft_4030", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3250.125, 3199.9912, 2363.3447), (-90.0, -0.3286359960515908, 180.32869478223907), (0.3125, 0.75, 0.625), "Suburbs_Column_X_Large_A_Shaft_4047", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2050.1248, 3199.9912, 2363.3447), (-90.0, -0.3286359960515908, 180.32869478223907), (0.3125, 0.75, 0.625), "Suburbs_Column_X_Large_A_Shaft_4064", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (799.8882, 3200.0085, 2363.3804), (-90.0, -0.0035067583095234095, 0.0035154893949095787), (0.3125, 0.75, 0.625), "Suburbs_Column_X_Large_A_Shaft_4081", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (800.12463, 3200.0269, 2363.3447), (-90.0, -0.3286359960515908, 180.32869478223907), (0.3125, 0.75, 0.625), "Suburbs_Column_X_Large_A_Shaft_4098", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3249.8882, 1800.0084, 2363.3804), (-90.0, -0.0035067583095234095, 0.0035154893949095787), (0.3125, 0.75, 0.625), "Suburbs_Column_X_Large_A_Shaft_4149", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3250.125, 1800.0074, 2363.3447), (-90.0, -0.3286359960515908, 180.32869478223907), (0.3125, 0.75, 0.625), "Suburbs_Column_X_Large_A_Shaft_4166", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5649.913, 1800.0253, 2363.3447), (-90.0, -0.3286359960515908, 180.32869478223907), (0.3125, 0.75, 0.625), "Suburbs_Column_X_Large_A_Shaft_4200", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3249.8882, 4600.0083, 2363.3804), (-90.0, -0.0035067583095234095, 0.0035154893949095787), (0.3125, 0.75, 0.625), "Suburbs_Column_X_Large_A_Shaft_4217", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3250.125, 4599.864, 2363.3447), (-90.0, -0.3286359960515908, 180.32869478223907), (0.3125, 0.75, 0.625), "Suburbs_Column_X_Large_A_Shaft_4234", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2849.8882, 500.00842, 2363.3804), (-90.0, -0.0035067583095234095, 0.0035154893949095787), (0.3125, 0.75, 0.625), "Suburbs_Column_X_Large_A_Shaft_4355", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1050.1248, 4599.864, 2363.3447), (-90.0, -0.3286359960515908, 180.32869478223907), (0.3125, 0.75, 0.625), "Suburbs_Column_X_Large_A_Shaft_5125", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1049.8882, 4600.0083, 2363.3804), (-90.0, -0.0035067583095234095, 0.0035154893949095787), (0.3125, 0.75, 0.625), "Suburbs_Column_X_Large_A_Shaft_5145", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5649.913, 3200.0269, 2363.3447), (-90.0, -1.367109057531818e-05, -179.9998975364387), (0.3125, 0.75, 0.625), "Suburbs_Column_X_Large_A_Shaft_5205", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4449.888, 4600.0083, 2363.3804), (-90.0, -0.0035067583095234095, 0.0035154893949095787), (0.3125, 0.75, 0.625), "Suburbs_Column_X_Large_A_Shaft_5225", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4450.1123, 4599.9277, 2363.3447), (-90.0, -0.3286359960515908, 180.32869478223907), (0.3125, 0.75, 0.625), "Suburbs_Column_X_Large_A_Shaft_5245", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2049.8901, 5750.0073, 2363.3804), (-90.0, 0.0005485968237561715, -0.0005309468409646062), (0.3125, 0.75, 0.625), "Suburbs_Column_X_Large_A_Shaft_5305", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1049.8921, 5750.0073, 2363.3804), (-90.0, 0.0023354114856125098, -0.002338589433854143), (0.3125, 0.75, 0.625), "Suburbs_Column_X_Large_A_Shaft_5325", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3249.8901, 6000.0073, 2363.3804), (-90.0, -0.0023274379564941095, 0.0023265012197113116), (0.3125, 0.75, 0.625), "Suburbs_Column_X_Large_A_Shaft_5345", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3250.125, 399.99542, 2363.3447), (-90.0, -0.3286359960515908, 180.32869478223907), (0.3125, 0.75, 0.625), "Suburbs_Column_X_Large_A_Shaft_5425", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2049.8882, 1800.0084, 2363.3804), (-90.0, -0.0035067583095234095, 0.0035154893949095787), (0.3125, 0.75, 0.625), "Suburbs_Column_X_Large_A_Shaft_5445", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2050.1248, 1800.0253, 2363.3447), (-90.0, -0.3286359960515908, 180.32869478223907), (0.3125, 0.75, 0.625), "Suburbs_Column_X_Large_A_Shaft_5465", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2050.161, 5749.9224, 2363.3462), (-90.0, -1.367109057531818e-05, -179.9998975364387), (0.3125, 0.75, 0.625), "Suburbs_Column_X_Large_A_Shaft_5545", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1050.1241, 5749.989, 2363.3462), (-90.0, -1.367109057531818e-05, -179.9998975364387), (0.3125, 0.75, 0.625), "Suburbs_Column_X_Large_A_Shaft_5565", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (299.9751, 5750.0986, 2363.3875), (-90.0, -0.00015223549082056932, 0.00041323546162272336), (0.3125, 0.75, 0.625), "Suburbs_Column_X_Large_A_Shaft10", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (299.9751, 6012.512, 2363.3875), (-90.0, -0.00015223554144580125, 0.0004132355446593464), (0.3125, 0.75, 0.625), "Suburbs_Column_X_Large_A_Shaft11_791", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (550.1289, 4026.2605, 2136.2048), (-90.0, -0.00015223546550795336, 0.00041323542010441184), (0.3125, 0.75, 0.625), "Suburbs_Column_X_Large_A_Shaft12", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (300.46634, 4026.2605, 2136.2048), (-90.0, -0.00015223546550795336, 0.00041323542010441184), (0.3125, 0.75, 0.625), "Suburbs_Column_X_Large_A_Shaft13", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (51.11383, 4026.2605, 2136.2048), (-90.0, -0.00015223546550795336, 0.00041323542010441184), (0.3125, 0.75, 0.625), "Suburbs_Column_X_Large_A_Shaft14", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (550.1289, 2627.448, 2136.2048), (-90.0, -0.00015223549082056932, 0.00041323546162272336), (0.3125, 0.75, 0.625), "Suburbs_Column_X_Large_A_Shaft15", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (300.46634, 2627.448, 2136.2048), (-90.0, -0.00015223549082056932, 0.00041323546162272336), (0.3125, 0.75, 0.625), "Suburbs_Column_X_Large_A_Shaft16", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (51.11383, 2627.448, 2136.2048), (-90.0, -0.00015223549082056932, 0.00041323546162272336), (0.3125, 0.75, 0.625), "Suburbs_Column_X_Large_A_Shaft17", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1600.0466, 1799.9634, 2363.287), (-90.0, -6.767199523072967e-05, -179.9998890701384), (0.3125, 0.75, 0.625), "Suburbs_Column_X_Large_A_Shaft18", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2499.8857, 500.0539, 2363.3804), (-90.0, 0.002670039117958495, -0.0022479510167400856), (0.3125, 0.75, 0.625), "Suburbs_Column_X_Large_A_Shaft2_104", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3000.111, 5749.811, 2363.3481), (-90.0, 0.009073072503357336, -180.00893018915448), (0.3125, 0.75, 0.625), "Suburbs_Column_X_Large_A_Shaft2_210", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2299.8857, 3200.05, 2363.3804), (-90.0, -0.0035067583095234095, 0.0035154893949095787), (0.3125, 0.75, 0.625), "Suburbs_Column_X_Large_A_Shaft2_3932", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3499.8857, 3200.05, 2363.3804), (-90.0, -0.0035067583095234095, 0.0035154893949095787), (0.3125, 0.75, 0.625), "Suburbs_Column_X_Large_A_Shaft2_3980", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4699.8857, 3200.05, 2363.3804), (-90.0, -0.0035067583095234095, 0.0035154893949095787), (0.3125, 0.75, 0.625), "Suburbs_Column_X_Large_A_Shaft2_3997", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4200.1396, 3199.9497, 2363.3447), (-90.0, -0.3286359960515908, 180.32869478223907), (0.3125, 0.75, 0.625), "Suburbs_Column_X_Large_A_Shaft2_4031", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3000.1082, 3199.9817, 2363.3447), (-90.0, -0.3286359960515908, 180.32869478223907), (0.3125, 0.75, 0.625), "Suburbs_Column_X_Large_A_Shaft2_4048", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1800.14, 3199.9817, 2363.3447), (-90.0, -0.3286359960515908, 180.32869478223907), (0.3125, 0.75, 0.625), "Suburbs_Column_X_Large_A_Shaft2_4065", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1049.8857, 3200.05, 2363.3804), (-90.0, -0.0035067583095234095, 0.0035154893949095787), (0.3125, 0.75, 0.625), "Suburbs_Column_X_Large_A_Shaft2_4082", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (550.14, 3199.9497, 2363.3447), (-90.0, -0.3286359960515908, 180.32869478223907), (0.3125, 0.75, 0.625), "Suburbs_Column_X_Large_A_Shaft2_4099", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3499.8857, 1800.05, 2363.3804), (-90.0, -0.0035067583095234095, 0.0035154893949095787), (0.3125, 0.75, 0.625), "Suburbs_Column_X_Large_A_Shaft2_4150", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3000.1082, 1799.9834, 2363.3447), (-90.0, -0.3286359960515908, 180.32869478223907), (0.3125, 0.75, 0.625), "Suburbs_Column_X_Large_A_Shaft2_4167", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5400.005, 1800.0012, 2363.3447), (-90.0, -0.3286359960515908, 180.32869478223907), (0.3125, 0.75, 0.625), "Suburbs_Column_X_Large_A_Shaft2_4201", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3499.8857, 4600.0503, 2363.3804), (-90.0, -0.0035067583095234095, 0.0035154893949095787), (0.3125, 0.75, 0.625), "Suburbs_Column_X_Large_A_Shaft2_4218", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3000.1082, 4599.687, 2363.3447), (-90.0, -0.3286359960515908, 180.32869478223907), (0.3125, 0.75, 0.625), "Suburbs_Column_X_Large_A_Shaft2_4235", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3099.8857, 500.05005, 2363.3804), (-90.0, 0.004647983535453326, -0.004643013693960199), (0.3125, 0.75, 0.625), "Suburbs_Column_X_Large_A_Shaft2_4356", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (800.13995, 4599.8223, 2363.3447), (-90.0, -0.3286359960515908, 180.32869478223907), (0.3125, 0.75, 0.625), "Suburbs_Column_X_Large_A_Shaft2_5126", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1299.8857, 4600.0503, 2363.3804), (-90.0, -0.0035067583095234095, 0.0035154893949095787), (0.3125, 0.75, 0.625), "Suburbs_Column_X_Large_A_Shaft2_5146", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4699.8857, 4600.0503, 2363.3804), (-90.0, -0.0035067583095234095, 0.0035154893949095787), (0.3125, 0.75, 0.625), "Suburbs_Column_X_Large_A_Shaft2_5226", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4200.1406, 4599.886, 2363.3447), (-90.0, -0.3286359960515908, 180.32869478223907), (0.3125, 0.75, 0.625), "Suburbs_Column_X_Large_A_Shaft2_5246", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2299.8877, 5750.0493, 2363.3804), (-90.0, 0.0005485968237561715, -0.0005309468409646062), (0.3125, 0.75, 0.625), "Suburbs_Column_X_Large_A_Shaft2_5306", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1299.8896, 5750.0493, 2363.3804), (-90.0, 0.0023354114856125098, -0.002338589433854143), (0.3125, 0.75, 0.625), "Suburbs_Column_X_Large_A_Shaft2_5326", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3499.8877, 6000.0493, 2363.3804), (-90.0, -0.0023274379564941095, 0.0023265012197113116), (0.3125, 0.75, 0.625), "Suburbs_Column_X_Large_A_Shaft2_5346", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3000.1082, 399.95367, 2363.3447), (-90.0, -0.3286359960515908, 180.32869478223907), (0.3125, 0.75, 0.625), "Suburbs_Column_X_Large_A_Shaft2_5426", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2299.8857, 1800.05, 2363.3804), (-90.0, -0.0035067583095234095, 0.0035154893949095787), (0.3125, 0.75, 0.625), "Suburbs_Column_X_Large_A_Shaft2_5446", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1800.14, 1799.9834, 2363.3447), (-90.0, -0.3286359960515908, 180.32869478223907), (0.3125, 0.75, 0.625), "Suburbs_Column_X_Large_A_Shaft2_5466", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1800.2076, 5749.881, 2363.3462), (-90.0, -1.367109057531818e-05, -179.9998975364387), (0.3125, 0.75, 0.625), "Suburbs_Column_X_Large_A_Shaft2_5546", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (800.1062, 5749.9473, 2363.3462), (-90.0, -1.367109057531818e-05, -179.9998975364387), (0.3125, 0.75, 0.625), "Suburbs_Column_X_Large_A_Shaft2_5566", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (50.22702, 3200.0996, 2363.3875), (-90.0, -0.00015223549082056932, 0.00041323546162272336), (0.3125, 0.75, 0.625), "Suburbs_Column_X_Large_A_Shaft22", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1549.7422, 3199.9275, 2363.2656), (-90.0, -6.767199523072967e-05, -179.9998890701384), (0.3125, 0.75, 0.625), "Suburbs_Column_X_Large_A_Shaft23", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5690.344, 2375.4514, 2173.7131), (-90.0, -26.569466821997995, 116.56907721067394), (0.3125, 0.75, 0.625), "Suburbs_Column_X_Large_A_Shaft28", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5799.9805, 2200.0017, 2363.3804), (-90.0, -90.00913094855933, 180.0087562341351), (0.3125, 0.75, 0.625), "Suburbs_Column_X_Large_A_Shaft3_111", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5799.991, 3200.002, 2363.3804), (-90.0, 130.6020016651212, -40.60187561439368), (0.3125, 0.75, 0.625), "Suburbs_Column_X_Large_A_Shaft3_131", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3499.969, 5750.06, 2363.3481), (-90.0, -0.29805118014141196, 180.29799286560544), (0.3125, 0.75, 0.625), "Suburbs_Column_X_Large_A_Shaft3_211", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1800.002, 3200.0088, 2363.3804), (-90.0, 0.00030653606620420953, -0.0002405579151396222), (0.3125, 0.75, 0.625), "Suburbs_Column_X_Large_A_Shaft3_3933", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3000.002, 3200.0088, 2363.3804), (-90.0, 0.00030653606620420953, -0.0002405579151396222), (0.3125, 0.75, 0.625), "Suburbs_Column_X_Large_A_Shaft3_3981", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4200.002, 3200.0088, 2363.3804), (-90.0, 0.00030653606620420953, -0.0002405579151396222), (0.3125, 0.75, 0.625), "Suburbs_Column_X_Large_A_Shaft3_3998", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5400.002, 3200.0088, 2363.3804), (-90.0, 0.00030653606620420953, -0.0002405579151396222), (0.3125, 0.75, 0.625), "Suburbs_Column_X_Large_A_Shaft3_4015", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4699.998, 3199.9912, 2363.3447), (-90.0, 5.495495639269788e-05, 179.99986080604415), (0.3125, 0.75, 0.625), "Suburbs_Column_X_Large_A_Shaft3_4032", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3499.966, 3199.9912, 2363.3447), (-90.0, 5.495495639269788e-05, 179.99986080604415), (0.3125, 0.75, 0.625), "Suburbs_Column_X_Large_A_Shaft3_4049", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2299.9822, 3199.9236, 2363.3447), (-90.0, 5.495495639269788e-05, 179.99986080604415), (0.3125, 0.75, 0.625), "Suburbs_Column_X_Large_A_Shaft3_4066", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (550.00195, 3200.0088, 2363.3804), (-90.0, 0.00030653606620420953, -0.0002405579151396222), (0.3125, 0.75, 0.625), "Suburbs_Column_X_Large_A_Shaft3_4083", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1049.9893, 3199.9592, 2363.3447), (-90.0, 5.495495639269788e-05, 179.99986080604415), (0.3125, 0.75, 0.625), "Suburbs_Column_X_Large_A_Shaft3_4100", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3000.002, 1800.0089, 2363.3804), (-90.0, 0.00030653606620420953, -0.0002405579151396222), (0.3125, 0.75, 0.625), "Suburbs_Column_X_Large_A_Shaft3_4151", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3499.966, 1799.9911, 2363.3447), (-90.0, 5.495495639269788e-05, 179.99986080604415), (0.3125, 0.75, 0.625), "Suburbs_Column_X_Large_A_Shaft3_4168", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5899.863, 1800.0089, 2363.3447), (-90.0, 5.495495639269788e-05, 179.99986080604415), (0.3125, 0.75, 0.625), "Suburbs_Column_X_Large_A_Shaft3_4202", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3000.002, 4600.009, 2363.3804), (-90.0, 0.00030653606620420953, -0.0002405579151396222), (0.3125, 0.75, 0.625), "Suburbs_Column_X_Large_A_Shaft3_4219", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3499.966, 4599.9272, 2363.3447), (-90.0, 5.495495639269788e-05, 179.99986080604415), (0.3125, 0.75, 0.625), "Suburbs_Column_X_Large_A_Shaft3_4236", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2600.002, 500.0089, 2363.3804), (-90.0, 0.00030653606620420953, -0.0002405579151396222), (0.3125, 0.75, 0.625), "Suburbs_Column_X_Large_A_Shaft3_4357", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1299.9893, 4599.9272, 2363.3447), (-90.0, 5.495495639269788e-05, 179.99986080604415), (0.3125, 0.75, 0.625), "Suburbs_Column_X_Large_A_Shaft3_5127", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (800.00195, 4600.009, 2363.3804), (-90.0, 0.00030653606620420953, -0.0002405579151396222), (0.3125, 0.75, 0.625), "Suburbs_Column_X_Large_A_Shaft3_5147", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5899.863, 3199.9912, 2363.3447), (-90.0, 5.495495639269788e-05, 179.99986080604415), (0.3125, 0.75, 0.625), "Suburbs_Column_X_Large_A_Shaft3_5207", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4200.002, 4600.009, 2363.3804), (-90.0, 0.00030653606620420953, -0.0002405579151396222), (0.3125, 0.75, 0.625), "Suburbs_Column_X_Large_A_Shaft3_5227", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4699.998, 4599.9272, 2363.3447), (-90.0, 5.495495639269788e-05, 179.99986080604415), (0.3125, 0.75, 0.625), "Suburbs_Column_X_Large_A_Shaft3_5247", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1800.0059, 5750.008, 2363.3804), (-90.0, -0.0002676321740164274, 0.00034048752961991845), (0.3125, 0.75, 0.625), "Suburbs_Column_X_Large_A_Shaft3_5307", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (800.00586, 5750.008, 2363.3804), (-90.0, 0.0003485100082101474, -0.00027662175341780385), (0.3125, 0.75, 0.625), "Suburbs_Column_X_Large_A_Shaft3_5327", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3000.004, 6000.008, 2363.3804), (-90.0, 0.0003485100082101474, -0.00027662175341780385), (0.3125, 0.75, 0.625), "Suburbs_Column_X_Large_A_Shaft3_5347", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3499.966, 399.99506, 2363.3447), (-90.0, 5.495495639269788e-05, 179.99986080604415), (0.3125, 0.75, 0.625), "Suburbs_Column_X_Large_A_Shaft3_5427", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1800.002, 1800.0089, 2363.3804), (-90.0, 0.00030653606620420953, -0.0002405579151396222), (0.3125, 0.75, 0.625), "Suburbs_Column_X_Large_A_Shaft3_5447", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2299.9822, 1800.0089, 2363.3447), (-90.0, 5.495495639269788e-05, 179.99986080604415), (0.3125, 0.75, 0.625), "Suburbs_Column_X_Large_A_Shaft3_5467", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2299.9817, 5750.057, 2363.3462), (-90.0, -0.29805118014141196, 180.29799286560544), (0.3125, 0.75, 0.625), "Suburbs_Column_X_Large_A_Shaft3_5547", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1299.9895, 5750.057, 2363.3462), (-90.0, -0.29805118014141196, 180.29799286560544), (0.3125, 0.75, 0.625), "Suburbs_Column_X_Large_A_Shaft3_5567", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5952.949, 2375.4514, 2173.7131), (-90.0, -26.569466821997995, 116.56907721067394), (0.3125, 0.75, 0.625), "Suburbs_Column_X_Large_A_Shaft31", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5804.6006, 3200.0085, 2363.3804), (-90.0, -2.6723493508410365e-07, 4.380598849429296e-07), (0.3125, 0.75, 0.625), "Suburbs_Column_X_Large_A_Shaft33", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5952.949, 3775.8743, 2173.7131), (-90.0, -26.569466821997995, 116.56907721067394), (0.3125, 0.75, 0.625), "Suburbs_Column_X_Large_A_Shaft34_833", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5690.281, 3775.873, 2173.7131), (-90.0, -26.569466821997995, 116.56907721067394), (0.3125, 0.75, 0.625), "Suburbs_Column_X_Large_A_Shaft35", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (6399.856, 3199.9019, 2363.3518), (-90.0, 0.0002627253621276672, -179.99990638687026), (0.3125, 0.75, 0.625), "Suburbs_Column_X_Large_A_Shaft39_360", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2350.0088, 500.0996, 2363.3875), (-90.0, -0.00015223546550795336, 0.00041323542010441184), (0.3125, 0.75, 0.625), "Suburbs_Column_X_Large_A_Shaft4", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3600.0088, 500.0996, 2363.3875), (-90.0, -0.00015223546550795336, 0.00041323542010441184), (0.3125, 0.75, 0.625), "Suburbs_Column_X_Large_A_Shaft4_35", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5799.888, 1950.0085, 2363.3875), (-90.0, -90.00668430415503, 180.00656169117832), (0.3125, 0.75, 0.625), "Suburbs_Column_X_Large_A_Shaft4_115", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5800.1, 2950.0088, 2363.3875), (-90.0, 90.00458382456497, -0.004360371013703457), (0.3125, 0.75, 0.625), "Suburbs_Column_X_Large_A_Shaft4_135", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3749.9946, 5749.969, 2363.3552), (-90.0, 179.6457029177508, -359.6453672743309), (0.3125, 0.75, 0.625), "Suburbs_Column_X_Large_A_Shaft4_215", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1550.0088, 3200.0996, 2363.3875), (-90.0, -0.00015223546550795336, 0.00041323542010441184), (0.3125, 0.75, 0.625), "Suburbs_Column_X_Large_A_Shaft4_4393", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2750.0088, 3200.0996, 2363.3875), (-90.0, -0.00015223546550795336, 0.00041323542010441184), (0.3125, 0.75, 0.625), "Suburbs_Column_X_Large_A_Shaft4_4430", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3950.0088, 3200.0996, 2363.3875), (-90.0, -0.00015223546550795336, 0.00041323542010441184), (0.3125, 0.75, 0.625), "Suburbs_Column_X_Large_A_Shaft4_4467", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5150.009, 3200.0996, 2363.3875), (-90.0, -0.00015223546550795336, 0.00041323542010441184), (0.3125, 0.75, 0.625), "Suburbs_Column_X_Large_A_Shaft4_4504", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4949.9556, 3199.9004, 2363.3518), (-90.0, 0.0007230137426489738, -180.00036653430266), (0.3125, 0.75, 0.625), "Suburbs_Column_X_Large_A_Shaft4_4541", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3749.9912, 3199.9004, 2363.3518), (-90.0, 0.0007230137426489738, -180.00036653430266), (0.3125, 0.75, 0.625), "Suburbs_Column_X_Large_A_Shaft4_4578", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2550.0088, 3199.9004, 2363.3518), (-90.0, 0.0007230137426489738, -180.00036653430266), (0.3125, 0.75, 0.625), "Suburbs_Column_X_Large_A_Shaft4_4615", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (300.0088, 3200.0996, 2363.3875), (-90.0, -0.00015223546550795336, 0.00041323542010441184), (0.3125, 0.75, 0.625), "Suburbs_Column_X_Large_A_Shaft4_4652", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1299.9847, 3199.9683, 2363.3516), (-90.0, 179.6457029177508, -359.6453672743309), (0.3125, 0.75, 0.625), "Suburbs_Column_X_Large_A_Shaft4_4689", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2750.0088, 1800.0996, 2363.3875), (-90.0, -0.00015223546550795336, 0.00041323542010441184), (0.3125, 0.75, 0.625), "Suburbs_Column_X_Large_A_Shaft4_4800", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3749.9912, 1799.9502, 2363.3518), (-90.0, 0.0007230137426489738, -180.00036653430266), (0.3125, 0.75, 0.625), "Suburbs_Column_X_Large_A_Shaft4_4837", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (6149.856, 1799.968, 2363.3518), (-90.0, 0.0007230137426489738, -180.00036653430266), (0.3125, 0.75, 0.625), "Suburbs_Column_X_Large_A_Shaft4_4911", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2750.0088, 4600.0996, 2363.3875), (-90.0, -0.00015223546550795336, 0.00041323542010441184), (0.3125, 0.75, 0.625), "Suburbs_Column_X_Large_A_Shaft4_4948", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3749.9912, 4599.8364, 2363.3518), (-90.0, 0.0007230137426489738, -180.00036653430266), (0.3125, 0.75, 0.625), "Suburbs_Column_X_Large_A_Shaft4_4985", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (550.0088, 4600.0996, 2363.3875), (-90.0, -0.00015223546550795336, 0.00041323542010441184), (0.3125, 0.75, 0.625), "Suburbs_Column_X_Large_A_Shaft4_5151", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (6149.856, 3199.9004, 2363.3518), (-90.0, 0.0007230137426489738, -180.00036653430266), (0.3125, 0.75, 0.625), "Suburbs_Column_X_Large_A_Shaft4_5211", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3950.0088, 4600.0996, 2363.3875), (-90.0, -0.00015223546550795336, 0.00041323542010441184), (0.3125, 0.75, 0.625), "Suburbs_Column_X_Large_A_Shaft4_5231", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4949.9233, 4599.8364, 2363.3518), (-90.0, 0.0007230137426489738, -180.00036653430266), (0.3125, 0.75, 0.625), "Suburbs_Column_X_Large_A_Shaft4_5251", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1550.0127, 5750.0986, 2363.3875), (-90.0, -0.00015223549082056932, 0.00041323546162272336), (0.3125, 0.75, 0.625), "Suburbs_Column_X_Large_A_Shaft4_5311", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (550.0127, 5750.0986, 2363.3875), (-90.0, -0.00015223549082056932, 0.00041323546162272336), (0.3125, 0.75, 0.625), "Suburbs_Column_X_Large_A_Shaft4_5331", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2750.0107, 6000.0986, 2363.3875), (-90.0, -0.00015223549082056932, 0.00041323546162272336), (0.3125, 0.75, 0.625), "Suburbs_Column_X_Large_A_Shaft4_5351", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3749.9912, 399.90448, 2363.3518), (-90.0, 0.0007230137426489738, -180.00036653430266), (0.3125, 0.75, 0.625), "Suburbs_Column_X_Large_A_Shaft4_5431", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1550.0088, 1800.0996, 2363.3875), (-90.0, -0.00015223546550795336, 0.00041323542010441184), (0.3125, 0.75, 0.625), "Suburbs_Column_X_Large_A_Shaft4_5451", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2550.0088, 1799.9342, 2363.3518), (-90.0, 0.0007230137426489738, -180.00036653430266), (0.3125, 0.75, 0.625), "Suburbs_Column_X_Large_A_Shaft4_5471", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2550.0083, 5749.9663, 2363.3533), (-90.0, 179.6457029177508, -359.6453672743309), (0.3125, 0.75, 0.625), "Suburbs_Column_X_Large_A_Shaft4_5551", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1549.9929, 5750.102, 2363.353), (-90.0, 0.0012236897775520566, -180.00092062832388), (0.3125, 0.75, 0.625), "Suburbs_Column_X_Large_A_Shaft4_5571", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (6054.6006, 3200.0085, 2363.3804), (-90.0, -3.509112953571926e-05, 1.823393001876049e-05), (0.3125, 0.75, 0.625), "Suburbs_Column_X_Large_A_Shaft42_362", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5399.9434, 3200.0269, 2363.3447), (-90.0, -0.0006523807757713588, 180.00071840587455), (0.3125, 0.75, 0.625), "Suburbs_Column_X_Large_A_Shaft43", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3349.8857, 500.05005, 2363.3804), (-90.0, -2.6723493508410365e-07, 4.380598849429296e-07), (0.3125, 0.75, 0.625), "Suburbs_Column_X_Large_A_Shaft44", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (300.14, 3199.9497, 2363.3447), (-90.0, -2.383746980760527, 182.38379320224672), (0.3125, 0.75, 0.625), "Suburbs_Column_X_Large_A_Shaft47", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (299.88416, 4600.0996, 2363.3875), (-90.0, -0.00015223546550795336, 0.00041323542010441184), (0.3125, 0.75, 0.625), "Suburbs_Column_X_Large_A_Shaft5", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (50.566772, 4600.0996, 2363.3875), (-90.0, -0.00015223549082056932, 0.00041323546162272336), (0.3125, 0.75, 0.625), "Suburbs_Column_X_Large_A_Shaft6_787", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (150.005, 5050.0, 1300.0), (0.0, -179.99980192457332, 0.0), (1.0, 1.0, 0.5), "Suburbs_Column_X_Large_A_Shaft7_357", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1150.0, 6249.995, 1300.0), (0.0, 90.0001164887758, -0.0), (1.0, 1.0, 0.5), "Suburbs_Column_X_Large_A_Shaft7_457", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (249.99976, 5250.0, 1300.0), (0.0, 0.00022899997782330336, -0.0), (1.0, 1.0, 0.5), "Suburbs_Column_X_Large_A_Shaft8_358", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1349.9998, 6150.0, 1300.0), (0.0, -89.99981506294705, 0.0), (1.0, 1.0, 0.5), "Suburbs_Column_X_Large_A_Shaft8_458", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (299.88403, 4862.766, 2363.3875), (-90.0, -0.00015223549082056932, 0.00041323546162272336), (0.3125, 0.75, 0.625), "Suburbs_Column_X_Large_A_Shaft9_783", _folder)
if a: placed += 1
else: skipped += 1

# Batch 35: StaticMesh'Suburbs_Column_X_Large_A_Shaft_Corner' (1 instances)
_mesh_path = "/Game/Art/Assets/Kits/Architecture/Suburbs/Suburbs_Column_X_Large_A_Shaft_Corner"
_materials = ['/Game/Art/Assets/Kits/Architecture/Suburbs/Materials/Suburbs_Column_X_Large_A/MI_Suburbs_Column_X_Large_A_Shaft']
_folder = "Reconstruction/BD_BB_Sandbox_DwarfHall_Voxels/Meshes"
a = spawn_static_mesh(_mesh_path, _materials, (150.0, 6250.0, 1250.0), (0.0, 90.00001925454477, -0.0), (1.0, 1.0, 0.5), "Suburbs_Column_X_Large_A_Shaft_Corner_491", _folder)
if a: placed += 1
else: skipped += 1

# Batch 36: StaticMesh'Suburbs_Floor_1x1m_A' (6 instances)
_mesh_path = "/Game/Art/Assets/Kits/Architecture/Suburbs/Suburbs_Floor_1x1m_A"
_materials = ['/Game/Environments/ProcTexturing/GuideMeshFloor/M_GuideMeshFloor_Urban']
_folder = "Reconstruction/BD_BB_Sandbox_DwarfHall_Voxels/Meshes"
a = spawn_static_mesh(_mesh_path, _materials, (2700.0, 6300.0, 900.0), (0.0, 0.0, -0.0), (1.0, 1.0, 1.0), "Suburbs_Floor_1-5x1-5m_A10", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2700.0, 6200.0, 900.0), (0.0, -179.9999590188648, 0.0), (1.0, 1.0, 1.0), "Suburbs_Floor_1-5x1-5m_A11", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2800.001, 6300.0, 900.0), (0.0, 179.99991120752276, -0.0), (1.0, 1.0, 1.0), "Suburbs_Floor_1-5x1-5m_A12", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2600.0012, 6300.0005, 900.0), (0.0, 179.99991120752276, -0.0), (1.0, 1.0, 1.0), "Suburbs_Floor_1-5x1-5m_A13", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2600.001, 6400.0, 900.0), (0.0, -0.0002136230511090266, 0.0), (1.0, 1.0, 1.0), "Suburbs_Floor_1-5x1-5m_A14", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2500.0, 6300.0, 900.0), (0.0, 0.0, -0.0), (1.0, 1.0, 1.0), "Suburbs_Floor_1-5x1-5m_A9_159", _folder)
if a: placed += 1
else: skipped += 1

# Batch 37: StaticMesh'Suburbs_Floor_3x3m_A' (1 instances)
_mesh_path = "/Game/Art/Assets/Kits/Architecture/Suburbs/Suburbs_Floor_3x3m_A"
_materials = ['/Game/Environments/ProcTexturing/GuideMeshFloor/M_GuideMeshFloor_Urban']
_folder = "Reconstruction/BD_BB_Sandbox_DwarfHall_Voxels/Meshes"
a = spawn_static_mesh(_mesh_path, _materials, (2650.0005, 5274.999, 989.93506), (0.0, -179.99995901885745, 0.0), (-1.0, 1.0, 1.0), "Suburbs_Floor_3x3m_A905", _folder)
if a: placed += 1
else: skipped += 1

# Batch 38: StaticMesh'Suburbs_Floor_3x9m_B' (19 instances)
_mesh_path = "/Game/Art/Assets/Kits/Architecture/Suburbs/Suburbs_Floor_3x9m_B"
_materials = ['/Game/Art/Assets/Kits/Architecture/Suburbs/Materials/Suburbs_Trim_Sheet_A/MI_Suburbs_Trim_Sheet_A', '/Game/Art/Assets/Kits/Architecture/Suburbs/Materials/Suburbs_Trim_Sheet_A/MI_Suburbs_Trim_Sheet_A']
_folder = "Reconstruction/BD_BB_Sandbox_DwarfHall_Voxels/Meshes"
a = spawn_static_mesh(_mesh_path, _materials, (250.0, 2450.0, 850.0), (0.0, -90.00005166594045, 0.0), (1.0, 1.0, 1.0), "Suburbs_Floor_3x9m_B_972", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4050.0, 6050.0, 900.0), (0.0, -179.99971996224815, 0.0), (1.0, 1.0, 1.0), "Suburbs_Floor_3x9m_B16", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3199.999, 6250.0, 800.0), (0.0, -179.99971996224815, 0.0), (1.0, 1.0, 1.0), "Suburbs_Floor_3x9m_B17", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1700.0, 6050.0, 850.0), (0.0, -179.99971996224815, 0.0), (1.0, 1.0, 1.0), "Suburbs_Floor_3x9m_B18", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (850.0, 6050.0, 850.0), (0.0, -179.99971996224815, 0.0), (1.0, 1.0, 1.0), "Suburbs_Floor_3x9m_B19", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (250.0, 5750.0, 850.0), (0.0, -89.99945205658098, 0.0), (1.0, 1.0, 1.0), "Suburbs_Floor_3x9m_B20", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (250.0, 4850.0, 850.0), (0.0, -89.99945205658098, 0.0), (1.0, 1.0, 1.0), "Suburbs_Floor_3x9m_B21", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (250.0, 3950.0, 850.0), (0.0, -89.99945205658098, 0.0), (1.0, 1.0, 1.0), "Suburbs_Floor_3x9m_B22", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2300.0, 5450.0, 850.0), (0.0, 90.00009542133918, -0.0), (1.0, 1.0, 1.0), "Suburbs_Floor_3x9m_B23", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2300.0, 4550.0, 850.0), (0.0, 90.00009542133918, -0.0), (1.0, 1.0, 1.0), "Suburbs_Floor_3x9m_B24", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5850.0, 2850.0, 797.4268), (0.0, 9.536742698250585e-06, -0.0), (1.0, 1.0, 1.0), "Suburbs_Floor_3x9m_B25", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5150.0, 3200.0, 796.23627), (0.0, -90.0001164887758, 0.0), (1.0, 1.0, 1.0), "Suburbs_Floor_3x9m_B26", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5850.0, 3550.0, 797.4268), (0.0, -179.9998975471592, 0.0), (1.0, 1.0, 1.0), "Suburbs_Floor_3x9m_B27_1134", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2850.0, 3200.0, 798.1454), (0.0, 90.00019751736242, -0.0), (1.0, 1.0, 1.0), "Suburbs_Floor_3x9m_B28", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (150.0, 3200.0, 795.0), (0.0, -90.00005166594045, 0.0), (1.0, 1.0, 1.0), "Suburbs_Floor_3x9m_B29_8", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (6255.0, 3199.996, 795.0), (0.0, 89.99957359878371, -0.0), (1.0, 1.0, 1.0), "Suburbs_Floor_3x9m_B30", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3200.0, 150.0, 800.0), (0.0, 0.00010899999514861327, -0.0), (1.0, 1.0, 1.0), "Suburbs_Floor_3x9m_B6", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4050.0, 350.0, 900.0), (0.0, 0.00010899999514861327, -0.0), (1.0, 1.0, 1.0), "Suburbs_Floor_3x9m_B7", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4950.0, 350.0, 900.0), (0.0, 0.00010899999514861327, -0.0), (1.0, 1.0, 1.0), "Suburbs_Floor_3x9m_B8", _folder)
if a: placed += 1
else: skipped += 1

# Batch 39: StaticMesh'Suburbs_Floor_Stone_IND_A' (1 instances)
_mesh_path = "/Game/Art/Assets/Kits/Architecture/Suburbs/Suburbs_Floor_Stone_IND_A"
_materials = ['/Game/Art/Assets/Kits/Architecture/Suburbs/Materials/Suburbs_Floor_Stone_IND/MI_Suburbs_Floor_Stone_IND_MAT_Inst_Dest_lighter']
_folder = "Reconstruction/BD_BB_Sandbox_DwarfHall_Voxels/Meshes"
a = spawn_static_mesh(_mesh_path, _materials, (3145.5142, 4723.368, 847.8854), (-2.135620194458533, 0.1502127001155054, 2.038400217458638), (1.0, 1.0, 1.0), "Suburbs_Floor_Stone_IND_A11_499", _folder)
if a: placed += 1
else: skipped += 1

# Batch 40: StaticMesh'Suburbs_Floor_Stone_IND_A' (9 instances)
_mesh_path = "/Game/Art/Assets/Kits/Architecture/Suburbs/Suburbs_Floor_Stone_IND_A"
_materials = ['/Game/Art/Assets/Kits/Architecture/Suburbs/Materials/Suburbs_Floor_Stone_IND/MI_Suburbs_Floor_Stone_IND_MAT_Inst_Dest_lighter']
_folder = "Reconstruction/BD_BB_Sandbox_DwarfHall_Voxels/Meshes"
a = spawn_static_mesh(_mesh_path, _materials, (2229.0742, 3116.2856, 809.22644), (0.0, 0.0, -0.0), (1.0, 1.0, 1.0), "Suburbs_Floor_Stone_IND_A_309", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1024.1813, 1755.7728, 858.60504), (0.0, 0.0, -0.0), (1.0, 1.0, 1.0), "Suburbs_Floor_Stone_IND_A10", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4339.357, 5917.425, 908.54553), (0.0, 0.0, -0.0), (1.0, 1.0, 1.0), "Suburbs_Floor_Stone_IND_A3_592", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4507.901, 5821.148, 911.3142), (0.0, 0.0, -0.0), (1.0, 1.0, 1.0), "Suburbs_Floor_Stone_IND_A4_598", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4711.8, 5616.9375, 911.43146), (0.0, 0.0, -0.0), (1.0, 1.0, 1.0), "Suburbs_Floor_Stone_IND_A5", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5331.5923, 4395.472, 909.2546), (0.0, 0.0, -0.0), (1.0, 1.0, 1.0), "Suburbs_Floor_Stone_IND_A6_40", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5623.025, 4504.303, 909.2286), (0.0, -89.99999818714215, 0.0), (1.0, 1.0, 1.0), "Suburbs_Floor_Stone_IND_A7_62", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5387.343, 5177.2207, 908.8155), (0.0, 89.99999818714215, -0.0), (1.0, 1.0, 1.0), "Suburbs_Floor_Stone_IND_A8_155", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4547.2085, 3528.0266, 908.6626), (0.0, 89.99999818714215, -0.0), (1.0, 1.0, 1.0), "Suburbs_Floor_Stone_IND_A9_85", _folder)
if a: placed += 1
else: skipped += 1

# Batch 41: StaticMesh'Suburbs_Floor_Stone_IND_B' (2 instances)
_mesh_path = "/Game/Art/Assets/Kits/Architecture/Suburbs/Suburbs_Floor_Stone_IND_B"
_materials = ['/Game/Art/Assets/Kits/Architecture/Suburbs/Materials/Suburbs_Floor_Stone_IND/MI_Suburbs_Floor_Stone_IND_MAT_Inst_Dest_lighter']
_folder = "Reconstruction/BD_BB_Sandbox_DwarfHall_Voxels/Meshes"
a = spawn_static_mesh(_mesh_path, _materials, (3133.8784, 4859.327, 857.908), (0.0, 0.0, 1.497379150908703), (1.0, 1.0, 1.0), "Suburbs_Floor_Stone_IND_B18_489", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2983.0645, 4753.5693, 856.33435), (0.0, 0.0, -0.0), (1.0, 1.0, 1.0), "Suburbs_Floor_Stone_IND_B19", _folder)
if a: placed += 1
else: skipped += 1

# Batch 42: StaticMesh'Suburbs_Floor_Stone_IND_B' (19 instances)
_mesh_path = "/Game/Art/Assets/Kits/Architecture/Suburbs/Suburbs_Floor_Stone_IND_B"
_materials = ['/Game/Art/Assets/Kits/Architecture/Suburbs/Materials/Suburbs_Floor_Stone_IND/MI_Suburbs_Floor_Stone_IND_MAT_Inst_Dest_lighter']
_folder = "Reconstruction/BD_BB_Sandbox_DwarfHall_Voxels/Meshes"
a = spawn_static_mesh(_mesh_path, _materials, (1352.3976, 3293.4526, 807.5334), (0.0, -179.99998633961752, -0.0), (1.0, 1.0, 1.0), "Suburbs_Floor_Stone_IND_B_334", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4406.3013, 3593.7952, 909.61707), (0.0, 0.0, -0.0), (1.0, 1.0, 1.0), "Suburbs_Floor_Stone_IND_B10_82", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4123.4976, 3423.1194, 907.94696), (0.0, 0.0, -0.0), (1.0, 1.0, 1.0), "Suburbs_Floor_Stone_IND_B11_94", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1028.081, 1382.8326, 857.4831), (0.0, 0.0, -0.0), (1.0, 1.0, 1.0), "Suburbs_Floor_Stone_IND_B14_203", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3138.5845, 1722.1239, 857.6647), (0.0, 0.0, -0.0), (1.0, 1.0, 1.0), "Suburbs_Floor_Stone_IND_B15", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3062.8433, 2137.6782, 857.6647), (0.0, 0.0, -0.0), (1.0, 1.0, 1.0), "Suburbs_Floor_Stone_IND_B16", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3032.3987, 1450.5383, 859.22473), (0.0, 89.99999818714215, -0.0), (1.0, 1.0, 1.0052562), "Suburbs_Floor_Stone_IND_B17", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1806.0891, 3331.8674, 807.9087), (0.0, -179.99998633961752, -0.0), (1.0, 1.0, 1.0), "Suburbs_Floor_Stone_IND_B2_355", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3138.089, 3844.333, 857.0002), (0.0, 0.0, -0.0), (1.0, 1.0, 0.29981124), "Suburbs_Floor_Stone_IND_B20_508", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3287.8506, 1610.9133, 858.84863), (1.842108588157778, 3.23667466127092e-08, -3.2291564784895326), (1.0, 1.0, 1.0), "Suburbs_Floor_Stone_IND_B21", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3461.6187, 1384.6819, 860.46826), (0.0, 86.47073602073473, -0.0), (1.0, 1.0, 1.0), "Suburbs_Floor_Stone_IND_B22_539", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4531.4204, 5715.9556, 908.84265), (0.0, 0.0, -0.0), (1.0, 1.0, 1.0), "Suburbs_Floor_Stone_IND_B23", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1321.0446, 1844.4877, 858.1543), (0.0, 89.99999818714215, -0.0), (1.0, 1.0, 1.0), "Suburbs_Floor_Stone_IND_B3_466", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4531.4204, 5615.9556, 908.84265), (0.0, 0.0, -0.0), (1.0, 1.0, 1.0), "Suburbs_Floor_Stone_IND_B4_583", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5400.0435, 4148.0356, 907.0287), (0.0, 89.99999818714215, -0.0), (1.0, 1.0, 1.0), "Suburbs_Floor_Stone_IND_B5_647", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5436.2246, 4972.5796, 907.0287), (0.0, 89.99999818714215, -0.0), (1.0, 1.0, 1.0), "Suburbs_Floor_Stone_IND_B6", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5480.5537, 4542.4077, 903.3025), (0.0, 0.0, -0.0), (1.0, 1.0, 1.0), "Suburbs_Floor_Stone_IND_B7_49", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3682.4087, 4701.13, 905.8044), (4.1653427832351015, 0.0, -0.0), (1.0, 1.0, 1.0), "Suburbs_Floor_Stone_IND_B8_192", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3725.1516, 4477.6074, 905.4429), (0.0, 0.0, -0.0), (1.0, 1.0, 1.0), "Suburbs_Floor_Stone_IND_B9", _folder)
if a: placed += 1
else: skipped += 1

# Batch 43: StaticMesh'Suburbs_Floor_Stone_IND_C' (16 instances)
_mesh_path = "/Game/Art/Assets/Kits/Architecture/Suburbs/Suburbs_Floor_Stone_IND_C"
_materials = ['/Game/Art/Assets/Kits/Architecture/Suburbs/Materials/Suburbs_Floor_Stone_IND/MI_Suburbs_Floor_Stone_IND_MAT_Inst_Dest_lighter', '/Game/Art/Assets/Kits/Architecture/Suburbs/Materials/Suburbs_Floor_Stone_IND/MI_Suburbs_Floor_Stone_IND_MAT_Inst_Dest']
_folder = "Reconstruction/BD_BB_Sandbox_DwarfHall_Voxels/Meshes"
a = spawn_static_mesh(_mesh_path, _materials, (1888.0635, 3066.244, 807.5403), (0.0, 0.0, -0.0), (1.0, 1.0, 1.0), "Suburbs_Floor_Stone_IND_C_300", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4181.9307, 3602.3562, 909.42957), (0.0, 89.99999818714215, -0.0), (1.0, 1.0, 1.0), "Suburbs_Floor_Stone_IND_C10_79", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3187.9526, 4007.5261, 857.2332), (0.0, 0.0, -0.0), (1.0, 1.0, 1.0), "Suburbs_Floor_Stone_IND_C15_502", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3191.903, 4912.63, 856.59955), (0.0, 0.0, -0.0), (1.0, 1.0, 1.0), "Suburbs_Floor_Stone_IND_C16_4401", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3170.6594, 5787.2754, 856.5997), (0.0, 89.99999818714215, -0.0), (1.0, 1.0, 1.0), "Suburbs_Floor_Stone_IND_C17", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3241.903, 4662.63, 857.98285), (-1.6396484280470347, 3.3209857023046096e-09, -1.0032349106914458), (1.0, 1.0, 1.0), "Suburbs_Floor_Stone_IND_C18", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3041.903, 4612.63, 856.59955), (0.0, 0.0, -0.0), (1.0, 1.0, 1.0), "Suburbs_Floor_Stone_IND_C19", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2175.8677, 3223.553, 806.7068), (0.0, 89.99999818714215, -0.0), (1.0, 1.0, 1.0), "Suburbs_Floor_Stone_IND_C2_315", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3380.0798, 1495.295, 857.4145), (0.0, 0.0, -0.0), (1.0, 1.0, 1.0), "Suburbs_Floor_Stone_IND_C20_516", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3269.7805, 1312.827, 857.25775), (0.0, 0.0, -0.0), (1.0, 1.0, 1.0), "Suburbs_Floor_Stone_IND_C21_536", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2392.8677, 3223.553, 806.7068), (0.0, 89.99999818714215, -0.0), (1.0, 1.0, 1.0), "Suburbs_Floor_Stone_IND_C22", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1601.6156, 3358.3086, 807.103), (0.0, 0.0, -0.0), (1.0, 1.0, 1.0), "Suburbs_Floor_Stone_IND_C3", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (757.3404, 1912.3712, 853.39404), (0.0, 0.0, -0.0), (1.0, 1.0, 1.0), "Suburbs_Floor_Stone_IND_C4", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2123.4941, 2786.2578, 855.2885), (0.0, 0.0, 1.2038433486346332), (1.0, 1.0, 1.0), "Suburbs_Floor_Stone_IND_C6_487", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5664.7285, 4075.697, 907.2246), (0.0, 89.99999818714215, -0.0), (1.0, 1.0, 1.0), "Suburbs_Floor_Stone_IND_C8_630", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5733.0503, 4167.1387, 908.60846), (0.0, 89.99999818714215, -0.0), (1.0, 1.0, 1.0), "Suburbs_Floor_Stone_IND_C9_641", _folder)
if a: placed += 1
else: skipped += 1

# Batch 44: StaticMesh'Suburbs_Floor_Stone_IND_D' (1 instances)
_mesh_path = "/Game/Art/Assets/Kits/Architecture/Suburbs/Suburbs_Floor_Stone_IND_D"
_materials = ['/Game/Art/Assets/Kits/Architecture/Suburbs/Materials/Suburbs_Floor_Stone_IND/MI_Suburbs_Floor_Stone_IND_MAT_Inst_Dest_lighter']
_folder = "Reconstruction/BD_BB_Sandbox_DwarfHall_Voxels/Meshes"
a = spawn_static_mesh(_mesh_path, _materials, (3031.6794, 4812.4336, 863.04083), (0.0, 0.0, -0.0), (1.0, 1.0, 1.0), "Suburbs_Floor_Stone_IND_D11_493", _folder)
if a: placed += 1
else: skipped += 1

# Batch 45: StaticMesh'Suburbs_Floor_Stone_IND_D' (13 instances)
_mesh_path = "/Game/Art/Assets/Kits/Architecture/Suburbs/Suburbs_Floor_Stone_IND_D"
_materials = ['/Game/Art/Assets/Kits/Architecture/Suburbs/Materials/Suburbs_Floor_Stone_IND/MI_Suburbs_Floor_Stone_IND_MAT_Inst_Dest_lighter']
_folder = "Reconstruction/BD_BB_Sandbox_DwarfHall_Voxels/Meshes"
a = spawn_static_mesh(_mesh_path, _materials, (2359.9915, 3145.191, 808.74506), (0.0, 0.0, -0.0), (1.0, 1.0, 1.0), "Suburbs_Floor_Stone_IND_D_306", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2114.5896, 527.93286, 859.5781), (0.0, 0.0, -0.0), (1.0, 1.0, 1.0), "Suburbs_Floor_Stone_IND_D10_193", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3115.933, 3949.565, 857.2608), (0.0, 0.0, -0.0), (1.0, 1.0, 0.23035757), "Suburbs_Floor_Stone_IND_D12_505", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3117.248, 1335.1992, 856.24146), (-6.000029999554044, 5.40482298481859e-07, 4.573155822943025), (1.0, 1.0, 1.0), "Suburbs_Floor_Stone_IND_D13_527", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3206.7512, 1534.752, 854.87085), (0.0, 0.0, -0.0), (1.0, 1.0, 1.0), "Suburbs_Floor_Stone_IND_D14_542", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3304.265, 1226.8522, 856.33435), (0.0, 0.0, -0.0), (1.0, 1.0, 1.0), "Suburbs_Floor_Stone_IND_D15_548", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2208.0413, 3014.705, 810.3083), (0.0, 89.99999818714215, -0.0), (1.0, 1.0, 1.0), "Suburbs_Floor_Stone_IND_D2_312", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2432.854, 3075.9253, 808.74506), (0.0, 0.0, -0.0), (1.0, 1.0, 1.0), "Suburbs_Floor_Stone_IND_D3", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1421.6227, 3112.776, 810.2097), (0.0, 0.0, -0.0), (1.0, 1.0, 1.0), "Suburbs_Floor_Stone_IND_D4_340", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1675.2704, 3265.4287, 806.3864), (0.0, 0.0, -0.0), (1.0, 1.0, 1.0), "Suburbs_Floor_Stone_IND_D5_358", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1291.9888, 1686.5753, 858.91455), (0.0, 0.0, -0.0), (1.0, 1.0, 1.0), "Suburbs_Floor_Stone_IND_D7_469", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4758.702, 3453.0562, 909.2535), (0.0, 89.99999818714215, -0.0), (1.0, 1.0, 1.0), "Suburbs_Floor_Stone_IND_D8_88", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2113.316, 721.16125, 856.2694), (0.0, 0.0, -0.0), (1.0, 1.0, 1.0), "Suburbs_Floor_Stone_IND_D9_187", _folder)
if a: placed += 1
else: skipped += 1

# Batch 46: StaticMesh'Suburbs_Floor_Stone_IND_E' (2 instances)
_mesh_path = "/Game/Art/Assets/Kits/Architecture/Suburbs/Suburbs_Floor_Stone_IND_E"
_materials = ['/Game/Art/Assets/Kits/Architecture/Suburbs/Materials/Suburbs_Floor_Stone_IND/MI_Suburbs_Floor_Stone_IND_MAT_Inst_Dest_lighter']
_folder = "Reconstruction/BD_BB_Sandbox_DwarfHall_Voxels/Meshes"
a = spawn_static_mesh(_mesh_path, _materials, (3073.1265, 4498.4775, 859.91534), (0.0, 0.0, -0.0), (1.0, 1.0, 1.0), "Suburbs_Floor_Stone_IND_E24_485", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3155.5723, 4579.5786, 859.91534), (0.0, 0.0, -0.0), (1.0, 1.0, 1.0), "Suburbs_Floor_Stone_IND_E25", _folder)
if a: placed += 1
else: skipped += 1

# Batch 47: StaticMesh'Suburbs_Floor_Stone_IND_E' (33 instances)
_mesh_path = "/Game/Art/Assets/Kits/Architecture/Suburbs/Suburbs_Floor_Stone_IND_E"
_materials = ['/Game/Art/Assets/Kits/Architecture/Suburbs/Materials/Suburbs_Floor_Stone_IND/MI_Suburbs_Floor_Stone_IND_MAT_Inst_Dest_lighter']
_folder = "Reconstruction/BD_BB_Sandbox_DwarfHall_Voxels/Meshes"
a = spawn_static_mesh(_mesh_path, _materials, (1976.9806, 3241.6826, 809.6329), (0.0, -179.9999795094293, 0.0), (1.0, 1.0, 1.0), "Suburbs_Floor_Stone_IND_E_303", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4267.3647, 5725.7456, 910.4727), (0.0, 0.0, -0.0), (1.0, 1.0, 1.0), "Suburbs_Floor_Stone_IND_E10_589", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4286.749, 5829.1377, 908.68317), (0.0, 89.99999818714215, -0.0), (1.0, 1.0, 1.0), "Suburbs_Floor_Stone_IND_E11_595", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4227.4355, 5575.6685, 910.4727), (0.0, 0.0, -0.0), (1.0, 1.0, 1.0), "Suburbs_Floor_Stone_IND_E12", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4006.5552, 5612.343, 907.81635), (0.0, 0.0, -0.0), (1.0, 1.0, 1.0), "Suburbs_Floor_Stone_IND_E13", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5598.272, 4322.37, 908.23004), (0.0, 0.0, -0.0), (1.0, 1.0, 1.0), "Suburbs_Floor_Stone_IND_E14_644", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5545.899, 4228.273, 909.6824), (0.0, 0.0, -0.0), (1.0, 1.0, 1.0), "Suburbs_Floor_Stone_IND_E15_650", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5561.86, 4733.6875, 908.23004), (0.0, 0.0, -0.0), (1.0, 1.0, 1.0), "Suburbs_Floor_Stone_IND_E16", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5488.0796, 4841.562, 909.6824), (0.0, 0.0, -0.0), (1.0, 1.0, 1.0), "Suburbs_Floor_Stone_IND_E17", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5546.962, 4408.5425, 908.23004), (0.0, 0.0, -0.0), (1.0, 1.0, 1.0), "Suburbs_Floor_Stone_IND_E18", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5218.8833, 4674.5703, 910.0455), (2.396576531698994, 90.00002547170016, 1.7250236504710264e-06), (1.0, 1.0, 1.0), "Suburbs_Floor_Stone_IND_E19_59", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1985.7845, 3052.9583, 809.6292), (0.0, 0.0, -0.0), (1.0, 1.0, 1.0), "Suburbs_Floor_Stone_IND_E2_318", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3819.4355, 4664.0425, 910.7515), (0.0, 89.99999818714215, -0.0), (1.0, 1.0, 1.0), "Suburbs_Floor_Stone_IND_E20_195", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3697.1108, 4576.5474, 907.85297), (0.0, 0.0, -0.0), (1.0, 1.0, 1.0), "Suburbs_Floor_Stone_IND_E21", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2141.7456, 820.2009, 858.6979), (0.0, 89.99999818714215, -0.0), (1.0, 1.0, 1.0), "Suburbs_Floor_Stone_IND_E22_190", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (917.5759, 1449.5897, 859.0365), (0.0, 0.0, -0.0), (1.0, 1.0, 1.0), "Suburbs_Floor_Stone_IND_E23_206", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3289.2336, 4900.0225, 859.219), (0.9795445981266937, 5.192311636231186e-09, 1.5160251641427107), (1.0, 1.0, 1.0), "Suburbs_Floor_Stone_IND_E26_4402", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3345.48, 5712.182, 857.92523), (0.0, 0.0, -0.0), (1.0, 1.0, 1.0), "Suburbs_Floor_Stone_IND_E27", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3239.2336, 4800.0225, 859.9517), (-1.9812924644894194, -89.99993929957523, 1.512363168639768), (1.0, 1.0, 1.0), "Suburbs_Floor_Stone_IND_E28", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3118.2249, 2759.9602, 857.5584), (1.1262592741590185, 0.036395390889446204, -0.4107971151725685), (1.0, 1.0, 0.40624163), "Suburbs_Floor_Stone_IND_E29_511", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1757.7272, 3111.9316, 809.0701), (4.852761142821566e-08, 90.0000057753137, 2.7507363356195764), (1.0, 1.0, 1.0), "Suburbs_Floor_Stone_IND_E3", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3189.4175, 2865.095, 856.89667), (-0.01138305582374797, -179.61293925599009, 1.6762359499950756), (1.0, 1.0, 1.0), "Suburbs_Floor_Stone_IND_E30", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3398.247, 1296.3, 857.7864), (0.0, 0.0, -0.0), (1.0, 1.0, 1.0), "Suburbs_Floor_Stone_IND_E31_519", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3194.0686, 1169.412, 858.12744), (0.0, 0.0, -0.0), (1.0, 1.0, 1.0), "Suburbs_Floor_Stone_IND_E32_522", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3135.9011, 1274.2341, 858.12744), (0.0, -90.60516377801856, 0.0), (1.0, 1.0, 1.0), "Suburbs_Floor_Stone_IND_E33", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3056.639, 1317.0907, 858.12744), (0.0, 89.46554554672608, -0.0), (1.0, 1.0, 1.0), "Suburbs_Floor_Stone_IND_E34", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3118.8179, 1550.4366, 858.4416), (-0.9148864774912682, 0.02383072445669233, 0.49543076373094447), (1.0, 1.0, 1.0), "Suburbs_Floor_Stone_IND_E35_530", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1596.0488, 3242.888, 808.71265), (0.0, -179.99998633961752, -0.0), (1.0, 1.0, 1.0), "Suburbs_Floor_Stone_IND_E4", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1294.6545, 3092.2568, 808.8273), (0.0, -179.99994535848643, 0.0), (1.0, 1.0, 1.0), "Suburbs_Floor_Stone_IND_E5_337", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1293.291, 3168.9724, 808.1543), (0.0, -179.99998633961752, -0.0), (1.0, 1.0, 1.0), "Suburbs_Floor_Stone_IND_E6_343", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1086.9004, 1779.2227, 858.7329), (0.0, 89.99999818714215, -0.0), (1.0, 1.0, 1.0), "Suburbs_Floor_Stone_IND_E7", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (855.06146, 1899.0857, 855.483), (0.0, 0.0, -0.0), (1.0, 1.0, 1.0), "Suburbs_Floor_Stone_IND_E8", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1943.9095, 2796.8518, 857.96295), (0.0, 0.0, 3.992892221675806), (1.0, 1.0, 1.0), "Suburbs_Floor_Stone_IND_E9_484", _folder)
if a: placed += 1
else: skipped += 1

# Batch 48: StaticMesh'Suburbs_Floor_Stone_IND_F' (6 instances)
_mesh_path = "/Game/Art/Assets/Kits/Architecture/Suburbs/Suburbs_Floor_Stone_IND_F"
_materials = ['/Game/Art/Assets/Kits/Architecture/Suburbs/Materials/Suburbs_Floor_Stone_IND/MI_Suburbs_Floor_Stone_IND_MAT_Inst_Dest_lighter']
_folder = "Reconstruction/BD_BB_Sandbox_DwarfHall_Voxels/Meshes"
a = spawn_static_mesh(_mesh_path, _materials, (4433.615, 5913.199, 911.0277), (0.0, 0.0, -0.0), (1.0, 1.0, 1.0), "Suburbs_Floor_Stone_IND_F2_601", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5222.6934, 4414.0527, 906.9993), (0.0, 0.0, -0.0), (1.0, 1.0, 1.0), "Suburbs_Floor_Stone_IND_F3_43", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5342.777, 4921.5728, 904.3347), (0.0, 0.0, -0.0), (1.0, 1.0, 1.0), "Suburbs_Floor_Stone_IND_F4_52", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4704.758, 3531.4678, 907.86066), (0.0, 0.0, -0.0), (1.0, 1.0, 1.0), "Suburbs_Floor_Stone_IND_F5_91", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3188.5747, 1461.5953, 856.87085), (0.0, -177.18738697646918, 0.0), (1.0, 1.0, 1.0), "Suburbs_Floor_Stone_IND_F6_533", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3127.695, 1478.1007, 854.87085), (0.0, 0.0, -0.0), (1.0, 1.0, 1.0), "Suburbs_Floor_Stone_IND_F7_545", _folder)
if a: placed += 1
else: skipped += 1

# Batch 49: StaticMesh'Suburbs_Floor_Trim_A_2m' (2 instances)
_mesh_path = "/Game/Art/Assets/Kits/Architecture/Suburbs/Suburbs_Floor_Trim_A_2m"
_materials = ['/Game/Art/Assets/Kits/Architecture/Suburbs/Materials/Suburbs_Floor_A/MI_Suburbs_Floor_A_2_Inst']
_folder = "Reconstruction/BD_BB_Sandbox_DwarfHall_Voxels/Meshes"
a = spawn_static_mesh(_mesh_path, _materials, (5100.0, 2600.9578, 904.2389), (0.0, 89.99999818714215, -0.0), (1.0, 1.0, 1.0), "Suburbs_Floor_Trim_A_2m_4362", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4900.0, 3799.0283, 904.2389), (0.0, -89.99999818714215, 0.0), (1.0, 1.0, 1.0), "Suburbs_Floor_Trim_A_2m2", _folder)
if a: placed += 1
else: skipped += 1

# Batch 50: StaticMesh'Suburbs_Stairs_Small_A_NonDest' (5 instances)
_mesh_path = "/Game/Art/Assets/Kits/Architecture/Suburbs/Suburbs_Stairs_Small_A_NonDest"
_materials = ['/Game/Art/Assets/Kits/Architecture/Suburbs/Destructable/Materials/MI_Suburbs_Wall_Non_Dest', '/Game/Art/Assets/Kits/Architecture/Suburbs/Materials/Stairs_Medium_C_NonDest/MI_Stairs_Medium_C_NonDes']
_folder = "Reconstruction/BD_BB_Sandbox_DwarfHall_Voxels/Meshes"
a = spawn_static_mesh(_mesh_path, _materials, (300.0, 2900.0, 750.0), (0.0, 0.0, -0.0), (1.0, 1.0, 1.0), "Suburbs_Stairs_Small_A15_302", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (150.0, 2900.0, 750.0), (0.0, 0.0, -0.0), (1.0, 1.0, 1.0), "Suburbs_Stairs_Small_A16", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (6150.0, 3799.9995, 800.0), (0.0, -179.99981558486024, 0.0), (1.0, 1.0, 1.0), "Suburbs_Stairs_Small_A20", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (6300.0, 2599.9985, 800.0), (0.0, 0.0, -0.0), (1.0, 1.0, 1.0), "Suburbs_Stairs_Small_A21", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3550.0, 4100.0, 800.0), (0.0, 0.0, -0.0), (1.0, 1.0, 1.0), "Suburbs_Stairs_Small_A5", _folder)
if a: placed += 1
else: skipped += 1

# Batch 51: StaticMesh'Suburbs_Stairs_Small_B_NonDest' (5 instances)
_mesh_path = "/Game/Art/Assets/Kits/Architecture/Suburbs/Suburbs_Stairs_Small_B_NonDest"
_materials = ['/Game/Art/Assets/Kits/Architecture/Suburbs/Destructable/Materials/MI_Suburbs_Wall_Non_Dest', '/Game/Art/Assets/Kits/Architecture/Suburbs/Materials/Stairs_Medium_C_NonDest/MI_Stairs_Medium_C_NonDes']
_folder = "Reconstruction/BD_BB_Sandbox_DwarfHall_Voxels/Meshes"
a = spawn_static_mesh(_mesh_path, _materials, (3600.0, 6300.0, 800.0), (0.0, 89.99999818714215, -0.0), (1.0, 1.0, 1.0), "Suburbs_Stairs_Small_A_NonDest_5", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2800.0, 6300.0, 800.0), (0.0, -89.99999818714215, 0.0), (1.0, 1.0, 1.0), "Suburbs_Stairs_Small_A_NonDest2", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2500.0, 6300.0, 800.0), (0.0, 89.99999818714215, -0.0), (1.0, 1.0, 1.0), "Suburbs_Stairs_Small_A_NonDest3", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3600.001, 100.20874, 800.0), (0.0, 89.99999818714215, -0.0), (1.0, 1.0, 1.0), "Suburbs_Stairs_Small_A_NonDest4", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2800.0007, 100.99756, 800.0), (0.0, -89.99999818714215, 0.0), (1.0, 1.0, 1.0), "Suburbs_Stairs_Small_A_NonDest5", _folder)
if a: placed += 1
else: skipped += 1

# Batch 52: StaticMesh'Suburbs_Stairs_Small_C_CornerExt_NonDest' (2 instances)
_mesh_path = "/Game/Art/Assets/Kits/Architecture/Suburbs/Suburbs_Stairs_Small_C_CornerExt_NonDest"
_materials = ['/Game/Art/Assets/Kits/Architecture/Suburbs/Destructable/Materials/MI_Suburbs_Wall_Non_Dest', '/Game/Art/Assets/Kits/Architecture/Suburbs/Materials/Stairs_Medium_C_NonDest/MI_Stairs_Medium_C_NonDes']
_folder = "Reconstruction/BD_BB_Sandbox_DwarfHall_Voxels/Meshes"
a = spawn_static_mesh(_mesh_path, _materials, (3400.0, 4100.0, 800.0), (0.0, -6.103515418554748e-05, 0.0), (1.0, 1.0, 1.0), "Suburbs_Stairs_CornerExt_2", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3400.0, 2300.0, 800.0), (0.0, 90.00011648875932, -0.0), (1.0, 1.0, 1.0), "Suburbs_Stairs_CornerExt_01_3690", _folder)
if a: placed += 1
else: skipped += 1

# Batch 53: StaticMesh'Suburbs_Stairs_Small_C_NonDest' (19 instances)
_mesh_path = "/Game/Art/Assets/Kits/Architecture/Suburbs/Suburbs_Stairs_Small_C_NonDest"
_materials = ['/Game/Art/Assets/Kits/Architecture/Suburbs/Destructable/Materials/MI_Suburbs_Wall_Non_Dest', '/Game/Art/Assets/Kits/Architecture/Suburbs/Materials/Stairs_Medium_C_NonDest/MI_Stairs_Medium_C_NonDes']
_folder = "Reconstruction/BD_BB_Sandbox_DwarfHall_Voxels/Meshes"
a = spawn_static_mesh(_mesh_path, _materials, (3400.0, 3050.0, 800.0), (0.0, 89.99995929348692, -0.0), (1.0, 1.0, 1.0), "Suburbs_Stairs_Small_A22", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3400.0, 3350.0, 800.0), (0.0, 89.99995929348692, -0.0), (1.0, 1.0, 1.0), "Suburbs_Stairs_Small_A23", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3400.0, 3650.0, 800.0), (0.0, 89.99995929348692, -0.0), (1.0, 1.0, 1.0), "Suburbs_Stairs_Small_A24", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3400.0, 3950.0, 800.0), (0.0, 89.99995929348692, -0.0), (1.0, 1.0, 1.0), "Suburbs_Stairs_Small_A25", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3550.0, 2300.0, 800.0), (0.0, -179.99995901885745, 0.0), (1.0, 1.0, 1.0), "Suburbs_Stairs_Small_A6", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3400.0, 2750.0, 800.0), (0.0, 89.99995929348692, -0.0), (1.0, 1.0, 1.0), "Suburbs_Stairs_Small_A7", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4900.003, 3050.0, 800.0), (0.0, -89.99975996369572, 0.0), (1.0, 1.0, 1.0), "Suburbs_Stairs_Small_C15_646", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4900.0, 3350.0, 800.0), (0.0, -89.99975996369572, 0.0), (1.0, 1.0, 1.0), "Suburbs_Stairs_Small_C16", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5200.0, 3800.0, 800.0), (0.0, -179.99970630186863, 0.0), (1.0, 1.0, 1.0), "Suburbs_Stairs_Small_C18_3679", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5400.0, 3799.9995, 800.0), (0.0, -179.99970630186863, 0.0), (1.0, 1.0, 1.0), "Suburbs_Stairs_Small_C19_3681", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5399.9995, 2599.9993, 800.0), (0.0, 0.0005187987303700534, -0.0), (1.0, 1.0, 1.0), "Suburbs_Stairs_Small_C20", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5100.0, 2599.9985, 800.0), (0.0, 0.0005187987303700534, -0.0), (1.0, 1.0, 1.0), "Suburbs_Stairs_Small_C21", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4900.0, 3650.0, 800.0), (0.0, -89.99975996369572, 0.0), (1.0, 1.0, 1.0), "Suburbs_Stairs_Small_C22", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4900.003, 2750.0, 800.0), (0.0, -89.99975996369572, 0.0), (1.0, 1.0, 1.0), "Suburbs_Stairs_Small_C23", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3400.0, 2450.0, 800.0), (0.0, 90.00004680423052, -0.0), (1.0, 1.0, 1.0), "Suburbs_Stairs_Small_C24", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5699.9995, 2599.9978, 800.0), (0.0, 0.0005187987303700534, -0.0), (1.0, 1.0, 1.0), "Suburbs_Stairs_Small_C25", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5700.0, 3799.9995, 800.0), (0.0, -179.99970630186863, 0.0), (1.0, 1.0, 1.0), "Suburbs_Stairs_Small_C26_260", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (6000.0, 3799.9995, 800.0), (0.0, -179.99970630186863, 0.0), (1.0, 1.0, 1.0), "Suburbs_Stairs_Small_C27", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5999.9995, 2600.0007, 800.0), (0.0, 0.0005190000104434912, -0.0), (1.0, 1.0, 1.0), "Suburbs_Stairs_Small_C28", _folder)
if a: placed += 1
else: skipped += 1

# Batch 54: StaticMesh'Suburbs_Stairs_Small_D1' (5 instances)
_mesh_path = "/Game/Art/Assets/Kits/Architecture/Suburbs/Suburbs_Stairs_Small_D1"
_materials = ['/Game/Art/Assets/Kits/Architecture/Suburbs/Materials/Suburbs_Wall/MI_Suburbs_Wall_Tile_B_Inst_Dest', '/Game/Art/Assets/Kits/Architecture/Suburbs/Materials/Suburbs_Stairs/MI_Suburbs_Stairs_01', '/Game/Art/Assets/Kits/Architecture/Suburbs/Materials/Suburbs_Stairs/MI_Suburbs_Stairs_02']
_folder = "Reconstruction/BD_BB_Sandbox_DwarfHall_Voxels/Meshes"
a = spawn_static_mesh(_mesh_path, _materials, (2800.0017, 949.99756, 850.0), (0.0, -90.00029475174199, 0.0), (1.0, 1.0, 1.0), "Suburbs_Stairs_Small_D108", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2800.002, 1249.9985, 850.0), (0.0, -90.00029475174199, 0.0), (1.0, 1.0, 1.0), "Suburbs_Stairs_Small_D109", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3600.002, 2449.9976, 850.0), (0.0, 89.99978589276644, -0.0), (1.0, 1.0, 1.0), "Suburbs_Stairs_Small_D120", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2500.002, 1249.998, 850.0), (0.0, 89.9997923750023, -0.0), (1.0, 1.0, 1.0), "Suburbs_Stairs_Small_D121", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3600.001, 3949.9976, 850.0), (0.0, 89.99978589276644, -0.0), (1.0, 1.0, 1.0), "Suburbs_Stairs_Small_D127", _folder)
if a: placed += 1
else: skipped += 1

# Batch 55: StaticMesh'Suburbs_Stairs_Small_D2' (1 instances)
_mesh_path = "/Game/Art/Assets/Kits/Architecture/Suburbs/Suburbs_Stairs_Small_D2"
_materials = ['/Game/Art/Assets/Kits/Architecture/Suburbs/Materials/Suburbs_Wall/MI_Suburbs_Wall_Tile_B_Inst_Dest', '/Game/Art/Assets/Kits/Architecture/Suburbs/Materials/Suburbs_Stairs/MI_Suburbs_Stairs_elements']
_folder = "Reconstruction/BD_BB_Sandbox_DwarfHall_Voxels/Meshes"
a = spawn_static_mesh(_mesh_path, _materials, (2500.0, 2450.0, 850.0), (0.0, 90.00002735739477, -0.0), (1.0, 1.0, 1.0), "Suburbs_Stairs_Small_D8", _folder)
if a: placed += 1
else: skipped += 1

# Batch 56: StaticMesh'Suburbs_Stairs_Small_D_NonDest' (61 instances)
_mesh_path = "/Game/Art/Assets/Kits/Architecture/Suburbs/Suburbs_Stairs_Small_D_NonDest"
_materials = ['/Game/Art/Assets/Kits/Architecture/Suburbs/Destructable/Materials/MI_Suburbs_Wall_Non_Dest', '/Game/Art/Assets/Kits/Architecture/Suburbs/Materials/Stairs_Medium_C_NonDest/MI_Stairs_Medium_C_NonDes', '/Game/Art/Assets/Kits/Architecture/Suburbs/Destructable/Materials/MI_Suburbs_Wall_Non_Dest']
_folder = "Reconstruction/BD_BB_Sandbox_DwarfHall_Voxels/Meshes"
a = spawn_static_mesh(_mesh_path, _materials, (2800.002, 4850.0005, 850.0002), (5.8160797888042265e-06, -89.99959790717836, -1.0542698447635757e-13), (1.0, 1.0, 1.0), "Suburbs_Stairs_Small_D101_242", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2800.0042, 5750.0005, 850.0001), (5.8160797888042265e-06, -89.99959790717836, -1.0542698447635757e-13), (1.0, 1.0, 1.0), "Suburbs_Stairs_Small_D102", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2500.002, 2149.998, 850.0), (0.0, 89.99979237503166, -0.0), (1.0, 1.0, 1.0), "Suburbs_Stairs_Small_D103", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2500.002, 1849.998, 850.0), (0.0, 89.99979237503166, -0.0), (1.0, 1.0, 1.0), "Suburbs_Stairs_Small_D104", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2500.002, 1549.998, 850.0), (0.0, 89.99979237503166, -0.0), (1.0, 1.0, 1.0), "Suburbs_Stairs_Small_D105", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3600.002, 949.99756, 850.0), (0.0, 89.99978589276644, -0.0), (1.0, 1.0, 1.0), "Suburbs_Stairs_Small_D106", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3600.001, 649.99756, 850.0), (0.0, 89.99978589276644, -0.0), (1.0, 1.0, 1.0), "Suburbs_Stairs_Small_D107", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2800.002, 1849.9976, 850.0), (0.0, -90.00029475174199, 0.0), (1.0, 1.0, 1.0), "Suburbs_Stairs_Small_D110", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2800.0022, 2149.9985, 850.0), (0.0, -90.00029475174199, 0.0), (1.0, 1.0, 1.0), "Suburbs_Stairs_Small_D111", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2800.002, 1549.998, 850.0), (0.0, -90.00029475174199, 0.0), (1.0, 1.0, 1.0), "Suburbs_Stairs_Small_D112", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2800.0017, 649.99756, 850.0), (0.0, -90.00029475174199, 0.0), (1.0, 1.0, 1.0), "Suburbs_Stairs_Small_D113", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3600.002, 1849.9976, 850.0), (0.0, 89.99978589276644, -0.0), (1.0, 1.0, 1.0), "Suburbs_Stairs_Small_D114", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3600.001, 1549.9976, 850.0), (0.0, 89.99978589276644, -0.0), (1.0, 1.0, 1.0), "Suburbs_Stairs_Small_D115", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3600.002, 4849.9976, 850.0), (0.0, 89.99978589276644, -0.0), (1.0, 1.0, 1.0), "Suburbs_Stairs_Small_D116", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3600.001, 4549.9976, 850.0), (0.0, 89.99978589276644, -0.0), (1.0, 1.0, 1.0), "Suburbs_Stairs_Small_D117", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3600.001, 1249.9976, 850.0), (0.0, 89.99978589276644, -0.0), (1.0, 1.0, 1.0), "Suburbs_Stairs_Small_D118", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3600.002, 2149.9976, 850.0), (0.0, 89.99978589276644, -0.0), (1.0, 1.0, 1.0), "Suburbs_Stairs_Small_D119", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2800.0007, 349.99756, 850.0), (0.0, -90.00029475174199, 0.0), (1.0204197, 1.0, 1.0204197), "Suburbs_Stairs_Small_D124", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3600.001, 4249.9976, 850.0), (0.0, 89.99978589276644, -0.0), (1.0, 1.0, 1.0), "Suburbs_Stairs_Small_D125", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3600.002, 5149.9976, 850.0), (0.0, 89.99978589276644, -0.0), (1.0, 1.0, 1.0), "Suburbs_Stairs_Small_D126", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3600.001, 349.99756, 850.0), (0.0, 89.99978589276644, -0.0), (1.0, 1.0, 1.0), "Suburbs_Stairs_Small_D132", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3599.9998, 6050.0005, 850.0), (0.0, 90.0002137230564, -0.0), (1.0, 1.0, 1.0), "Suburbs_Stairs_Small_D133", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2800.003, 6050.0015, 850.00006), (5.8160797888042265e-06, -89.99959790717836, -1.0542698447635757e-13), (1.0, 1.0, 1.0), "Suburbs_Stairs_Small_D134", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2870.0005, 6050.0015, 800.0), (5.8160797888042265e-06, -89.99959790717836, -1.0542698447635757e-13), (1.0, 1.150392, 1.0), "Suburbs_Stairs_Small_D135", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3529.9998, 6050.0005, 800.0), (0.0, 90.0002137230564, -0.0), (1.0, 1.1795558, 1.0), "Suburbs_Stairs_Small_D136", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3050.0005, 5890.0015, 800.0), (0.0, 0.0005350112587333198, -0.0), (1.0, 1.0, 1.0), "Suburbs_Stairs_Small_D137", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3350.0005, 5890.0015, 800.0), (0.0, 0.0005349999714647552, -0.0), (1.0, 1.0, 1.0), "Suburbs_Stairs_Small_D138", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2870.0005, 350.00146, 800.0), (0.0, -89.99968865881478, 0.0), (1.0, 1.1500458, 1.0), "Suburbs_Stairs_Small_D139", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3529.9998, 350.0005, 800.0), (0.0, 90.0002137230564, -0.0), (1.0, 1.1662719, 1.0), "Suburbs_Stairs_Small_D140", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3050.0005, 502.3022, 799.99994), (0.0, -179.99998633961752, -0.0), (1.0, 1.0, 1.0), "Suburbs_Stairs_Small_D141", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3350.0005, 502.3022, 799.99994), (0.0, -179.99998633961752, -0.0), (1.0, 1.0, 1.0), "Suburbs_Stairs_Small_D142", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2550.002, 2900.0, 800.0), (4.506451586731551e-06, 0.0001706323456445305, 6.103515631234381e-05), (1.0, 1.0, 1.0), "Suburbs_Stairs_Small_D50", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2250.002, 2900.0, 800.0), (4.506451586731551e-06, 0.0001706323456445305, 6.103515631234381e-05), (1.0, 1.0, 1.0), "Suburbs_Stairs_Small_D51", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1950.002, 2900.0, 800.0), (4.506451586731551e-06, 0.0001706323456445305, 6.103515631234381e-05), (1.0, 1.0, 1.0), "Suburbs_Stairs_Small_D52", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1650.0017, 3500.002, 799.9968), (4.5924126282603064e-05, -179.99970630186706, 6.103515729792168e-05), (1.0, 1.0, 1.0), "Suburbs_Stairs_Small_D53_18", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1950.002, 3500.003, 799.99713), (4.5924126282603064e-05, -179.99970630186706, 6.103515729792168e-05), (1.0, 1.0, 1.0), "Suburbs_Stairs_Small_D54_19", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2250.0022, 3500.0034, 799.9969), (4.5924126282603064e-05, -179.99970630186706, 6.103515729792168e-05), (1.0, 1.0, 1.0), "Suburbs_Stairs_Small_D55_20", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1350.0017, 3500.002, 799.9968), (4.5924126282603064e-05, -179.99970630186706, 6.103515729792168e-05), (1.0, 1.0, 1.0), "Suburbs_Stairs_Small_D56", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2550.0022, 3500.0034, 799.9969), (4.5924126282603064e-05, -179.99970630186706, 6.103515729792168e-05), (1.0, 1.0, 1.0), "Suburbs_Stairs_Small_D57", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1650.002, 2900.0, 800.0), (4.506451586731551e-06, 0.0001706323456445305, 6.103515631234381e-05), (1.0, 1.0, 1.0), "Suburbs_Stairs_Small_D58", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1350.002, 2900.0, 800.0), (4.506451586731551e-06, 0.0001706323456445305, 6.103515631234381e-05), (1.0, 1.0, 1.0), "Suburbs_Stairs_Small_D59", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1050.0017, 3500.002, 799.9968), (4.5924126282603064e-05, -179.99970630186706, 6.103515729792168e-05), (1.0, 1.0, 1.0), "Suburbs_Stairs_Small_D60_278", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1050.002, 2900.0, 800.0), (4.506451586731551e-06, 0.0001706323456445305, 6.103515631234381e-05), (1.0, 1.0, 1.0), "Suburbs_Stairs_Small_D61_280", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (750.0017, 3500.002, 799.9968), (4.5924126282603064e-05, -179.99970630186706, 6.103515729792168e-05), (1.0, 1.0, 1.0), "Suburbs_Stairs_Small_D62_290", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (450.0017, 3500.0032, 799.99524), (4.5924126282603064e-05, -179.99970630186706, 6.103515729792168e-05), (1.0, 1.0, 1.0), "Suburbs_Stairs_Small_D63", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (750.00195, 2900.0, 800.0), (4.506451586731551e-06, 0.0001706323456445305, 6.103515631234381e-05), (1.0, 1.0, 1.0), "Suburbs_Stairs_Small_D64_292", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (450.00195, 2900.0, 800.0), (4.506451586731551e-06, 0.0001706323456445305, 6.103515631234381e-05), (1.0, 1.0, 1.0), "Suburbs_Stairs_Small_D65", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2850.002, 3500.002, 799.9968), (4.5924126282603064e-05, -179.99970630186706, 6.103515729792168e-05), (1.0, 1.0, 1.0), "Suburbs_Stairs_Small_D66", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (150.00177, 3500.0005, 799.9984), (0.0, -179.99980192457332, 0.0), (1.0, 1.0, 1.0), "Suburbs_Stairs_Small_D67", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2850.002, 2900.0, 800.0), (4.506451586731551e-06, 0.0001706323456445305, 6.103515631234381e-05), (1.0, 1.0, 1.0), "Suburbs_Stairs_Small_D69", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3000.002, 3050.0, 800.0), (3.1827201518966565e-05, 90.00016510594452, 6.1035152106383486e-05), (1.0, 1.0, 1.0), "Suburbs_Stairs_Small_D70", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2500.002, 4250.0, 850.0), (3.182720619266383e-05, 90.00019103505078, -4.563659700830238e-13), (1.0, 1.0, 1.0), "Suburbs_Stairs_Small_D77_444", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2500.002, 4550.0, 850.0), (3.182720619266383e-05, 90.00019103505078, -4.563659700830238e-13), (1.0, 1.0, 1.0), "Suburbs_Stairs_Small_D78_446", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2499.999, 5750.0, 850.0), (3.182720619266383e-05, 90.00019103505078, -4.563659700830238e-13), (1.0, 1.0, 1.0), "Suburbs_Stairs_Small_D81", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2500.002, 4850.0, 850.0), (3.182720619266383e-05, 90.00019103505078, -4.563659700830238e-13), (1.0, 1.0, 1.0), "Suburbs_Stairs_Small_D83_637", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2500.0005, 6050.0, 850.0), (3.182720619266383e-05, 90.00019103505078, -4.563659700830238e-13), (1.0, 1.0, 1.0), "Suburbs_Stairs_Small_D84", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3000.002, 3350.0, 800.0), (3.1827201518966565e-05, 90.00016510594452, 6.1035152106383486e-05), (1.0, 1.0, 1.0), "Suburbs_Stairs_Small_D93", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2800.002, 4550.0005, 850.0002), (5.8160797888042265e-06, -89.99959790717836, -1.0542698447635757e-13), (1.0, 1.0, 1.0), "Suburbs_Stairs_Small_D96_3419", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3600.002, 5450.0005, 850.0), (0.0, 90.0002137230564, -0.0), (1.0, 1.0, 1.0), "Suburbs_Stairs_Small_D97", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3600.001, 5750.0005, 850.0), (0.0, 90.0002137230564, -0.0), (1.0, 1.0, 1.0), "Suburbs_Stairs_Small_D98", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2800.0022, 4249.9995, 850.0), (5.8160797888042265e-06, -89.99959790717836, -1.0542698447635757e-13), (1.0, 1.0, 1.0), "Suburbs_Stairs_Small_D99_3420", _folder)
if a: placed += 1
else: skipped += 1

# Batch 57: StaticMesh'Suburbs_Wall_Thick_3x3m_A' (15 instances)
_mesh_path = "/Game/Art/Assets/Kits/Architecture/Suburbs/Suburbs_Wall_Thick_3x3m_A"
_materials = ['/Game/Art/Assets/Kits/Architecture/Suburbs/Destructable/Materials/MI_Suburbs_Wall_Non_Dest']
_folder = "Reconstruction/BD_BB_Sandbox_DwarfHall_Voxels/Meshes"
a = spawn_static_mesh(_mesh_path, _materials, (5800.0, 2650.0, 2100.0), (0.0, 0.0, -90.00005166594045), (1.0, 1.0, 1.0), "Suburbs_Wall_Thick_3x3m_A_163", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (6300.0, 2500.0, 2050.0), (0.0, 89.99997063746636, -0.0), (1.0, 1.0, 1.0), "Suburbs_Wall_Thick_3x3m_A10", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (6300.0, 3900.0, 2050.0002), (0.0, 89.99997063746636, -0.0), (1.0, 1.0, 1.0), "Suburbs_Wall_Thick_3x3m_A11", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (699.9995, 3749.9927, 2099.9949), (-6.103514253126392e-05, -179.99988388677463, -89.99956549604322), (1.0, 1.0, 1.0), "Suburbs_Wall_Thick_3x3m_A16", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (199.99951, 3899.9924, 2049.9946), (4.098113657917154e-05, -89.99981506311053, -0.00015258788218100005), (1.0, 1.0, 1.0), "Suburbs_Wall_Thick_3x3m_A17", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (400.0, 3749.992, 2099.9946), (-6.103514253126392e-05, -179.99988388677463, -89.99956549604322), (1.0, 1.0, 1.0), "Suburbs_Wall_Thick_3x3m_A18", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (700.0026, 2349.9927, 2099.9827), (-6.103514253126392e-05, -179.99988388677463, -89.99956549604322), (1.0, 1.0, 1.0), "Suburbs_Wall_Thick_3x3m_A19", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5500.0, 2600.0, 2050.0), (0.0, 0.0, -0.0), (1.0, 1.0, 1.0), "Suburbs_Wall_Thick_3x3m_A2", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (200.00243, 2499.9924, 2049.9824), (4.1000000006329254e-05, -89.99981506311057, -0.0001525878821508552), (1.0, 1.0, 1.0), "Suburbs_Wall_Thick_3x3m_A20", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (400.00272, 2349.992, 2099.9824), (-6.103514253126392e-05, -179.99988388677463, -89.99956549604322), (1.0, 1.0, 1.0), "Suburbs_Wall_Thick_3x3m_A21", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (6100.0, 2650.0, 2100.0), (0.0, 0.0, -90.00005166594045), (1.0, 1.0, 1.0), "Suburbs_Wall_Thick_3x3m_A3_88", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5800.0, 4050.0, 2100.0002), (0.0, 0.0, -90.00005166594045), (1.0, 1.0, 1.0), "Suburbs_Wall_Thick_3x3m_A4_102", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5500.0, 2500.0, 2050.0), (0.0, 0.0, -0.0), (1.0, 1.0, 1.0), "Suburbs_Wall_Thick_3x3m_A5", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (6100.0, 4050.0, 2100.0002), (0.0, 0.0, -90.00005166594045), (1.0, 1.0, 1.0), "Suburbs_Wall_Thick_3x3m_A6_103", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5500.0, 2400.0, 2050.0), (0.0, 0.0, -0.0), (1.0, 1.0, 1.0), "Suburbs_Wall_Thick_3x3m_A8", _folder)
if a: placed += 1
else: skipped += 1

# Batch 58: StaticMesh'Suburbs_Wall_Thin_Arch_Half_E_3m' (94 instances)
_mesh_path = "/Game/Art/Assets/Kits/Architecture/Suburbs/Suburbs_Wall_Thin_Arch_Half_E_3m"
_materials = ['/Game/Art/Assets/Kits/Architecture/Suburbs/Destructable/Materials/MI_Suburbs_Wall_Base_Dest']
_folder = "Reconstruction/BD_BB_Sandbox_DwarfHall_Voxels/Meshes"
a = spawn_static_mesh(_mesh_path, _materials, (1700.0205, 2650.0234, 2050.0007), (0.0, -3.051757709276941e-05, 0.0), (1.0625, 1.25, 1.25), "Suburbs_Wall_Thin_Arch_Half_E_3m_3936", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2900.0205, 2650.0234, 2050.0007), (0.0, -3.051757709276941e-05, 0.0), (1.0625, 1.25, 1.25), "Suburbs_Wall_Thin_Arch_Half_E_3m_3984", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4100.0205, 2650.0234, 2050.0007), (0.0, -3.051757709276941e-05, 0.0), (1.0625, 1.25, 1.25), "Suburbs_Wall_Thin_Arch_Half_E_3m_4001", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5200.0205, 2650.0234, 2050.0007), (0.0, -3.051757709276941e-05, 0.0), (1.0625, 1.25, 1.25), "Suburbs_Wall_Thin_Arch_Half_E_3m_4018", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4799.844, 3749.9512, 2049.965), (0.0, 179.9999795094293, -0.0), (1.0625, 1.25, 1.25), "Suburbs_Wall_Thin_Arch_Half_E_3m_4035", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3600.015, 3749.9512, 2049.965), (0.0, 179.9999795094293, -0.0), (1.0625, 1.25, 1.25), "Suburbs_Wall_Thin_Arch_Half_E_3m_4052", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2399.997, 3749.9512, 2049.965), (0.0, 179.9999795094293, -0.0), (1.0625, 1.25, 1.25), "Suburbs_Wall_Thin_Arch_Half_E_3m_4069", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (450.0205, 2650.0234, 2050.0007), (0.0, -3.051757709276941e-05, 0.0), (1.0625, 1.25, 1.25), "Suburbs_Wall_Thin_Arch_Half_E_3m_4086", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1149.9623, 3749.9512, 2049.9648), (0.0, 179.9999795094293, -0.0), (1.0625, 1.25, 1.25), "Suburbs_Wall_Thin_Arch_Half_E_3m_4103", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2900.0205, 1250.0234, 2050.0007), (0.0, -3.051757709276941e-05, 0.0), (1.0625, 1.25, 1.25), "Suburbs_Wall_Thin_Arch_Half_E_3m_4154", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3600.0469, 2349.9512, 2049.965), (0.0, 179.9999795094293, -0.0), (1.0625, 1.25, 1.25), "Suburbs_Wall_Thin_Arch_Half_E_3m_4171", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (6199.709, 2349.9512, 2049.965), (0.0, 179.9999795094293, -0.0), (1.0625, 1.25, 1.25), "Suburbs_Wall_Thin_Arch_Half_E_3m_4205", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2900.0205, 4050.0234, 2050.0007), (0.0, -3.051757709276941e-05, 0.0), (1.0625, 1.25, 1.25), "Suburbs_Wall_Thin_Arch_Half_E_3m_4222", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3599.9473, 5150.086, 2049.965), (0.0, 179.9999795094293, -0.0), (1.0625, 1.25, 1.25), "Suburbs_Wall_Thin_Arch_Half_E_3m_4239", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1700.0205, 4050.0234, 2050.0007), (0.0, -3.051757709276941e-05, 0.0), (1.0625, 1.25, 1.25), "Suburbs_Wall_Thin_Arch_Half_E_3m_4273", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2399.997, 5150.086, 2049.965), (0.0, 179.9999795094293, -0.0), (1.0625, 1.25, 1.25), "Suburbs_Wall_Thin_Arch_Half_E_3m_4290", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1399.9702, 5150.087, 2049.9648), (0.0, 179.9999795094293, -0.0), (1.0625, 1.25, 1.25), "Suburbs_Wall_Thin_Arch_Half_E_3m_5130", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (700.0205, 4050.0234, 2050.0007), (0.0, -3.051757709276941e-05, 0.0), (1.0625, 1.25, 1.25), "Suburbs_Wall_Thin_Arch_Half_E_3m_5150", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5999.709, 3749.9512, 2049.965), (0.0, 179.9999795094293, -0.0), (1.0625, 1.25, 1.25), "Suburbs_Wall_Thin_Arch_Half_E_3m_5210", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4100.0205, 4050.0234, 2050.0007), (0.0, -3.051757709276941e-05, 0.0), (1.0625, 1.25, 1.25), "Suburbs_Wall_Thin_Arch_Half_E_3m_5230", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4799.7803, 5150.086, 2049.965), (0.0, 179.9999795094293, -0.0), (1.0625, 1.25, 1.25), "Suburbs_Wall_Thin_Arch_Half_E_3m_5250", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1700.0244, 5200.023, 2050.0007), (0.0, -3.051757709276941e-05, 0.0), (1.0625, 1.25, 1.25), "Suburbs_Wall_Thin_Arch_Half_E_3m_5310", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (700.0244, 5200.023, 2050.0007), (0.0, -3.051757709276941e-05, 0.0), (1.0625, 1.25, 1.25), "Suburbs_Wall_Thin_Arch_Half_E_3m_5330", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2900.0225, 5450.023, 2050.0007), (0.0, -3.051757709276941e-05, 0.0), (1.0625, 1.25, 1.25), "Suburbs_Wall_Thin_Arch_Half_E_3m_5350", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3600.015, 949.9508, 2049.965), (0.0, 179.9999795094293, -0.0), (1.0625, 1.25, 1.25), "Suburbs_Wall_Thin_Arch_Half_E_3m_5430", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1700.0205, 1250.0234, 2050.0007), (0.0, -3.051757709276941e-05, 0.0), (1.0625, 1.25, 1.25), "Suburbs_Wall_Thin_Arch_Half_E_3m_5450", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2399.997, 2349.9512, 2049.965), (0.0, 179.9999795094293, -0.0), (1.0625, 1.25, 1.25), "Suburbs_Wall_Thin_Arch_Half_E_3m_5470", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1518.012, 2349.981, 2049.8503), (0.0, 179.9999795094293, -0.0), (1.0625, 1.25, 1.25), "Suburbs_Wall_Thin_Arch_Half_E_3m10", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (6217.7573, 2650.0205, 2050.0007), (0.0, -3.051757709276941e-05, 0.0), (1.0625, 1.25, 1.25), "Suburbs_Wall_Thin_Arch_Half_E_3m11", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4982.0347, 2349.953, 2049.9158), (0.0, 179.9999795094293, -0.0), (1.0625, 1.25, 1.25), "Suburbs_Wall_Thin_Arch_Half_E_3m12", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4982.2695, 3750.037, 2049.943), (0.0, 179.9999795094293, -0.0), (1.0625, 1.25, 1.25), "Suburbs_Wall_Thin_Arch_Half_E_3m13", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (382.07175, 4050.0234, 2050.0007), (0.0, -3.051757709276941e-05, 0.0), (1.0625, 1.25, 1.25), "Suburbs_Wall_Thin_Arch_Half_E_3m2", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (133.00165, 3749.9536, 2049.965), (0.0, 179.9999795094293, -0.0), (1.0625, 1.25, 1.25), "Suburbs_Wall_Thin_Arch_Half_E_3m24", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5182.8657, 2349.9531, 2049.9648), (0.0, 179.9999795094293, -0.0), (1.0625, 1.25, 1.25), "Suburbs_Wall_Thin_Arch_Half_E_3m26", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (383.0016, 5150.025, 2049.965), (0.0, 179.9999795094293, -0.0), (1.0625, 1.25, 1.25), "Suburbs_Wall_Thin_Arch_Half_E_3m27", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1717.9148, 5150.409, 2049.9153), (0.0, 179.9999795094293, -0.0), (1.0625, 1.25, 1.25), "Suburbs_Wall_Thin_Arch_Half_E_3m3", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2400.024, 2650.0205, 2050.0007), (0.0, -3.051757709276941e-05, 0.0), (1.0625, 1.25, 1.25), "Suburbs_Wall_Thin_Arch_Half_E_3m4_4394", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3600.024, 2650.0205, 2050.0007), (0.0, -3.051757709276941e-05, 0.0), (1.0625, 1.25, 1.25), "Suburbs_Wall_Thin_Arch_Half_E_3m4_4431", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4800.024, 2650.0205, 2050.0007), (0.0, -3.051757709276941e-05, 0.0), (1.0625, 1.25, 1.25), "Suburbs_Wall_Thin_Arch_Half_E_3m4_4468", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5900.024, 2650.0205, 2050.0007), (0.0, -3.051757709276941e-05, 0.0), (1.0625, 1.25, 1.25), "Suburbs_Wall_Thin_Arch_Half_E_3m4_4505", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4100.0015, 3749.9536, 2049.965), (0.0, 179.9999795094293, -0.0), (1.0625, 1.25, 1.25), "Suburbs_Wall_Thin_Arch_Half_E_3m4_4542", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2899.97, 3749.9536, 2049.965), (0.0, 179.9999795094293, -0.0), (1.0625, 1.25, 1.25), "Suburbs_Wall_Thin_Arch_Half_E_3m4_4579", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1700.0374, 3749.985, 2049.965), (0.0, 179.9999795094293, -0.0), (1.0625, 1.25, 1.25), "Suburbs_Wall_Thin_Arch_Half_E_3m4_4616", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1150.0239, 2650.0205, 2050.0007), (0.0, -3.051757709276941e-05, 0.0), (1.0625, 1.25, 1.25), "Suburbs_Wall_Thin_Arch_Half_E_3m4_4653", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (450.00165, 3749.9536, 2049.965), (0.0, 179.9999795094293, -0.0), (1.0625, 1.25, 1.25), "Suburbs_Wall_Thin_Arch_Half_E_3m4_4690", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3600.024, 1250.0206, 2050.0007), (0.0, -3.051757709276941e-05, 0.0), (1.0625, 1.25, 1.25), "Suburbs_Wall_Thin_Arch_Half_E_3m4_4801", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2900.0017, 2349.9531, 2049.965), (0.0, 179.9999795094293, -0.0), (1.0625, 1.25, 1.25), "Suburbs_Wall_Thin_Arch_Half_E_3m4_4838", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5499.8657, 2349.9531, 2049.9648), (0.0, 179.9999795094293, -0.0), (1.0625, 1.25, 1.25), "Suburbs_Wall_Thin_Arch_Half_E_3m4_4912", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3600.024, 4050.0205, 2050.0007), (0.0, -3.051757709276941e-05, 0.0), (1.0625, 1.25, 1.25), "Suburbs_Wall_Thin_Arch_Half_E_3m4_4949", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2899.9692, 5149.8896, 2049.965), (0.0, 179.9999795094293, -0.0), (1.0625, 1.25, 1.25), "Suburbs_Wall_Thin_Arch_Half_E_3m4_4986", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2400.024, 4050.0205, 2050.0007), (0.0, -3.051757709276941e-05, 0.0), (1.0625, 1.25, 1.25), "Suburbs_Wall_Thin_Arch_Half_E_3m4_5023", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1699.9697, 5149.9536, 2049.965), (0.0, 179.9999795094293, -0.0), (1.0625, 1.25, 1.25), "Suburbs_Wall_Thin_Arch_Half_E_3m4_5060", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (700.0016, 5150.025, 2049.965), (0.0, 179.9999795094293, -0.0), (1.0625, 1.25, 1.25), "Suburbs_Wall_Thin_Arch_Half_E_3m4_5132", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1400.0239, 4050.0205, 2050.0007), (0.0, -3.051757709276941e-05, 0.0), (1.0625, 1.25, 1.25), "Suburbs_Wall_Thin_Arch_Half_E_3m4_5152", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5299.8657, 3749.9536, 2049.9648), (0.0, 179.9999795094293, -0.0), (1.0625, 1.25, 1.25), "Suburbs_Wall_Thin_Arch_Half_E_3m4_5212", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4800.024, 4050.0205, 2050.0007), (0.0, -3.051757709276941e-05, 0.0), (1.0625, 1.25, 1.25), "Suburbs_Wall_Thin_Arch_Half_E_3m4_5232", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4099.9375, 5149.9536, 2049.965), (0.0, 179.9999795094293, -0.0), (1.0625, 1.25, 1.25), "Suburbs_Wall_Thin_Arch_Half_E_3m4_5252", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2400.026, 5200.02, 2050.0007), (0.0, -3.051757709276941e-05, 0.0), (1.0625, 1.25, 1.25), "Suburbs_Wall_Thin_Arch_Half_E_3m4_5312", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1400.0278, 5200.02, 2050.0007), (0.0, -3.051757709276941e-05, 0.0), (1.0625, 1.25, 1.25), "Suburbs_Wall_Thin_Arch_Half_E_3m4_5332", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3600.026, 5450.02, 2050.0007), (0.0, -3.051757709276941e-05, 0.0), (1.0625, 1.25, 1.25), "Suburbs_Wall_Thin_Arch_Half_E_3m4_5352", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2899.97, 949.9535, 2049.965), (0.0, 179.9999795094293, -0.0), (1.0625, 1.25, 1.25), "Suburbs_Wall_Thin_Arch_Half_E_3m4_5432", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2400.024, 1250.0206, 2050.0007), (0.0, -3.051757709276941e-05, 0.0), (1.0625, 1.25, 1.25), "Suburbs_Wall_Thin_Arch_Half_E_3m4_5452", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1700.0693, 2349.985, 2049.965), (0.0, 179.9999795094293, -0.0), (1.0625, 1.25, 1.25), "Suburbs_Wall_Thin_Arch_Half_E_3m4_5472", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2050.0198, 2650.0298, 2050.0007), (0.0, -3.051757709276941e-05, 0.0), (1.28125, 1.25, 1.25), "Suburbs_Wall_Thin_Arch_Half_E_3m5_4395", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3250.0198, 2650.0298, 2050.0007), (0.0, -3.051757709276941e-05, 0.0), (1.28125, 1.25, 1.25), "Suburbs_Wall_Thin_Arch_Half_E_3m5_4432", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4450.0195, 2650.0298, 2050.0007), (0.0, -3.051757709276941e-05, 0.0), (1.28125, 1.25, 1.25), "Suburbs_Wall_Thin_Arch_Half_E_3m5_4469", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5550.0195, 2650.0298, 2050.0007), (0.0, -3.051757709276941e-05, 0.0), (1.28125, 1.25, 1.25), "Suburbs_Wall_Thin_Arch_Half_E_3m5_4506", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4450.044, 3749.9443, 2049.965), (0.0, 179.9999795094293, -0.0), (1.28125, 1.25, 1.25), "Suburbs_Wall_Thin_Arch_Half_E_3m5_4543", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3250.0286, 3749.9443, 2049.965), (0.0, 179.9999795094293, -0.0), (1.28125, 1.25, 1.25), "Suburbs_Wall_Thin_Arch_Half_E_3m5_4580", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2050.0283, 3749.9443, 2049.965), (0.0, 179.9999795094293, -0.0), (1.28125, 1.25, 1.25), "Suburbs_Wall_Thin_Arch_Half_E_3m5_4617", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (800.0198, 2650.0298, 2050.0007), (0.0, -3.051757709276941e-05, 0.0), (1.28125, 1.25, 1.25), "Suburbs_Wall_Thin_Arch_Half_E_3m5_4654", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (799.9928, 3749.98, 2049.965), (0.0, 179.9999795094293, -0.0), (1.28125, 1.25, 1.25), "Suburbs_Wall_Thin_Arch_Half_E_3m5_4691", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3250.0198, 1250.0298, 2050.0007), (0.0, -3.051757709276941e-05, 0.0), (1.28125, 1.25, 1.25), "Suburbs_Wall_Thin_Arch_Half_E_3m5_4802", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3250.0605, 2349.976, 2049.965), (0.0, 179.9999795094293, -0.0), (1.28125, 1.25, 1.25), "Suburbs_Wall_Thin_Arch_Half_E_3m5_4839", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5849.8447, 2349.9446, 2049.965), (0.0, 179.9999795094293, -0.0), (1.28125, 1.25, 1.25), "Suburbs_Wall_Thin_Arch_Half_E_3m5_4913", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3250.0198, 4050.0298, 2050.0007), (0.0, -3.051757709276941e-05, 0.0), (1.28125, 1.25, 1.25), "Suburbs_Wall_Thin_Arch_Half_E_3m5_4950", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3249.961, 5150.0156, 2049.965), (0.0, 179.9999795094293, -0.0), (1.28125, 1.25, 1.25), "Suburbs_Wall_Thin_Arch_Half_E_3m5_4987", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2050.0198, 4050.0298, 2050.0007), (0.0, -3.051757709276941e-05, 0.0), (1.28125, 1.25, 1.25), "Suburbs_Wall_Thin_Arch_Half_E_3m5_5024", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2049.9927, 5149.9443, 2049.965), (0.0, 179.9999795094293, -0.0), (1.28125, 1.25, 1.25), "Suburbs_Wall_Thin_Arch_Half_E_3m5_5061", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1049.9928, 5150.0156, 2049.965), (0.0, 179.9999795094293, -0.0), (1.28125, 1.25, 1.25), "Suburbs_Wall_Thin_Arch_Half_E_3m5_5133", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1050.0198, 4050.0298, 2050.0007), (0.0, -3.051757709276941e-05, 0.0), (1.28125, 1.25, 1.25), "Suburbs_Wall_Thin_Arch_Half_E_3m5_5153", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5649.8447, 3749.98, 2049.965), (0.0, 179.9999795094293, -0.0), (1.28125, 1.25, 1.25), "Suburbs_Wall_Thin_Arch_Half_E_3m5_5213", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4450.0195, 4050.0298, 2050.0007), (0.0, -3.051757709276941e-05, 0.0), (1.28125, 1.25, 1.25), "Suburbs_Wall_Thin_Arch_Half_E_3m5_5233", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4449.9805, 5150.0796, 2049.965), (0.0, 179.9999795094293, -0.0), (1.28125, 1.25, 1.25), "Suburbs_Wall_Thin_Arch_Half_E_3m5_5253", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2050.0217, 5200.0293, 2050.0007), (0.0, -3.051757709276941e-05, 0.0), (1.28125, 1.25, 1.25), "Suburbs_Wall_Thin_Arch_Half_E_3m5_5313", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1050.0234, 5200.0293, 2050.0007), (0.0, -3.051757709276941e-05, 0.0), (1.28125, 1.25, 1.25), "Suburbs_Wall_Thin_Arch_Half_E_3m5_5333", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3250.0217, 5450.0293, 2050.0007), (0.0, -3.051757709276941e-05, 0.0), (1.28125, 1.25, 1.25), "Suburbs_Wall_Thin_Arch_Half_E_3m5_5353", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3250.0286, 949.94434, 2049.965), (0.0, 179.9999795094293, -0.0), (1.28125, 1.25, 1.25), "Suburbs_Wall_Thin_Arch_Half_E_3m5_5433", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2050.0198, 1250.0298, 2050.0007), (0.0, -3.051757709276941e-05, 0.0), (1.28125, 1.25, 1.25), "Suburbs_Wall_Thin_Arch_Half_E_3m5_5453", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2050.0603, 2349.9443, 2049.965), (0.0, 179.9999795094293, -0.0), (1.28125, 1.25, 1.25), "Suburbs_Wall_Thin_Arch_Half_E_3m5_5473", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (382.0669, 5200.023, 2050.0007), (0.0, -3.051757709276941e-05, 0.0), (1.0625, 1.25, 1.25), "Suburbs_Wall_Thin_Arch_Half_E_3m6", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1468.2032, 3750.04, 2049.9387), (0.0, 179.9999795094293, -0.0), (1.0625, 1.25, 1.25), "Suburbs_Wall_Thin_Arch_Half_E_3m7", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (84.769104, 4050.0234, 2050.0007), (0.0, -3.051757709276941e-05, 0.0), (0.9226927, 1.25, 1.25), "Suburbs_Wall_Thin_Arch_Half_E_3m8", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (131.78241, 2650.0234, 2050.0007), (0.0, -3.051757709276941e-05, 0.0), (1.0625, 1.25, 1.25), "Suburbs_Wall_Thin_Arch_Half_E_3m9_802", _folder)
if a: placed += 1
else: skipped += 1

# Batch 59: StaticMesh'Trim_A_2m' (3 instances)
_mesh_path = "/Game/Art/Assets/Kits/Architecture/Suburbs/Trim_A_2m"
_materials = ['/Game/Art/Assets/Kits/Architecture/Suburbs/Materials/Suburbs_Trim_A/MI_Trim_A_1m_Dest']
_folder = "Reconstruction/BD_BB_Sandbox_DwarfHall_Voxels/Meshes"
a = spawn_static_mesh(_mesh_path, _materials, (2200.0, 2700.0, 2200.0), (0.00027036660326760825, -179.99998633961692, -179.99994535847677), (1.0, 1.0, 1.0), "Trim_A_2m_3782", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3400.0, 2700.0, 2200.0), (0.00026999991031538973, -179.9999863396171, -179.99994535847682), (1.0, 1.0, 1.0), "Trim_A_2m2_3870", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4550.0, 2700.0, 2200.0), (0.00026999991031538973, -179.9999863396171, -179.99994535847682), (1.0, 1.0, 1.0), "Trim_A_2m3", _folder)
if a: placed += 1
else: skipped += 1

# Batch 60: StaticMesh'Trim_A_3m_B' (1 instances)
_mesh_path = "/Game/Art/Assets/Kits/Architecture/Suburbs/Trim_A_3m_B"
_materials = ['/Game/Art/Assets/Kits/Architecture/Suburbs/Materials/Suburbs_Trim_A/MI_Trim_A_3m']
_folder = "Reconstruction/BD_BB_Sandbox_DwarfHall_Voxels/Meshes"
a = spawn_static_mesh(_mesh_path, _materials, (4850.0, 2700.0, 2200.0), (0.0004969999218819963, -179.99998633961775, -179.99994535847497), (1.0, 1.0, 1.0), "Trim_A_3m_B5", _folder)
if a: placed += 1
else: skipped += 1

# Batch 61: StaticMesh'Dirt_Mound_D' (2 instances)
_mesh_path = "/Game/Art/Assets/Kits/Misc/Dirt_Mounds/Dirt_Mound_D"
_materials = ['/Game/Art/Assets/Kits/Misc/Dirt_Mounds/Materials/Suburbs_Dirt_Inst']
_folder = "Reconstruction/BD_BB_Sandbox_DwarfHall_Voxels/Meshes"
a = spawn_static_mesh(_mesh_path, _materials, (4945.784, 1718.2423, 905.00525), (0.0, -177.56388390184992, 0.0), (0.55963695, 0.55963695, 0.55963695), "Dirt_Mound_D_299", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (343.2104, 5416.0103, 855.00525), (0.0, 12.607297307988382, -0.0), (0.91446984, 0.91446984, 1.0), "Dirt_Mound_D2_435", _folder)
if a: placed += 1
else: skipped += 1

# Batch 62: StaticMesh'Dirt_Mound_E' (1 instances)
_mesh_path = "/Game/Art/Assets/Kits/Misc/Dirt_Mounds/Dirt_Mound_E"
_materials = ['/Game/Art/Assets/Kits/Misc/Dirt_Mounds/Materials/Suburbs_Dirt_Inst']
_folder = "Reconstruction/BD_BB_Sandbox_DwarfHall_Voxels/Meshes"
a = spawn_static_mesh(_mesh_path, _materials, (2388.4922, 5299.27, 850.72217), (0.0, 0.0, -0.0), (1.0, 0.7702244, 1.0), "Dirt_Mound_E_438", _folder)
if a: placed += 1
else: skipped += 1

# Batch 63: StaticMesh'Dirt_Mound_G' (6 instances)
_mesh_path = "/Game/Art/Assets/Kits/Misc/Dirt_Mounds/Dirt_Mound_G"
_materials = ['/Game/Art/Assets/Kits/Misc/Dirt_Mounds/Materials/Suburbs_Dirt_Inst']
_folder = "Reconstruction/BD_BB_Sandbox_DwarfHall_Voxels/Meshes"
a = spawn_static_mesh(_mesh_path, _materials, (1272.9036, 5947.021, 853.14484), (0.0, -87.07053381843873, 0.0), (1.6283157, 1.0674018, 1.7827753), "Dirt_Mound_G10_428", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1185.9062, 6113.088, 860.84607), (0.0, -87.07053381843873, 0.0), (1.628316, 1.067402, 1.782775), "Dirt_Mound_G11_431", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1517.3936, 6152.0786, 842.0966), (0.0, -87.07053381843873, 0.0), (1.4826306, 0.92171615, 1.7242732), "Dirt_Mound_G12", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4167.2793, 1187.0427, 905.00525), (0.0, -162.80573192839972, 0.0), (1.0, 1.0, 1.0), "Dirt_Mound_G2_319", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4738.474, 2499.4597, 905.0021), (0.0, -8.035492480301619, 0.0), (1.0, 0.84689283, 1.0), "Dirt_Mound_G7_346", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3577.6736, 1247.9392, 922.64746), (-2.1329054969323735, 54.01760745400754, 62.98468712811322), (0.910558, 1.0, 1.0), "Dirt_Mound_G9", _folder)
if a: placed += 1
else: skipped += 1

# Batch 64: StaticMesh'Dirt_Mound_H' (2 instances)
_mesh_path = "/Game/Art/Assets/Kits/Misc/Dirt_Mounds/Dirt_Mound_H"
_materials = ['/Game/Art/Assets/Kits/Misc/Dirt_Mounds/Materials/Suburbs_Dirt_Inst']
_folder = "Reconstruction/BD_BB_Sandbox_DwarfHall_Voxels/Meshes"
a = spawn_static_mesh(_mesh_path, _materials, (4906.3164, 4952.2417, 905.0), (0.0, 40.00004908107326, -0.0), (1.461283, 1.461283, 1.461283), "Dirt_Mound_H7_157", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4171.792, 5272.7617, 900.0), (0.0, -25.0000005816717, 0.0), (1.5207708, 1.5207708, 1.5207708), "Dirt_Mound_H8_160", _folder)
if a: placed += 1
else: skipped += 1

# Batch 65: StaticMesh'Dirt_Mound_I' (20 instances)
_mesh_path = "/Game/Art/Assets/Kits/Misc/Dirt_Mounds/Dirt_Mound_I"
_materials = ['/Game/Art/Assets/Kits/Misc/Dirt_Mounds/Materials/Suburbs_Dirt_Inst']
_folder = "Reconstruction/BD_BB_Sandbox_DwarfHall_Voxels/Meshes"
a = spawn_static_mesh(_mesh_path, _materials, (3988.798, 2375.3455, 905.00525), (0.0, 0.0, -0.0), (0.65475816, 0.65475816, 0.65475816), "Dirt_Mound_I_311", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2814.9148, 4097.6396, 888.615), (12.701075773755573, 173.33751448239053, -5.70584006265172), (0.654758, 0.54924023, 0.679733), "Dirt_Mound_I10", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2788.8286, 5029.113, 880.0651), (13.086424860635708, 99.83948230722174, -7.928163040716837), (0.654758, 0.54924, 0.679733), "Dirt_Mound_I11", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2804.0146, 5557.619, 880.0651), (13.0864207777016, -174.58820475346144, -7.928161000859741), (0.654758, 0.54924, 0.679733), "Dirt_Mound_I12", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3691.7524, 5501.4507, 897.0466), (14.779617313907197, -23.177123287578983, 3.8608097361033638), (0.654758, 0.54924, 0.679733), "Dirt_Mound_I13", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3630.3816, 5082.014, 867.429), (13.086424593017169, 17.280516638516136, -7.9281623434049004), (0.654758, 0.54924, 0.679733), "Dirt_Mound_I14", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3537.3286, 5256.837, 822.4037), (0.0, 0.0, -0.0), (0.654758, 0.54924, 0.679733), "Dirt_Mound_I15", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2735.0, 2030.0, 855.0), (0.0, 0.0, -0.0), (1.0, 1.0, 0.87146306), "Dirt_Mound_I16_3", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3209.1904, 4507.2695, 844.1673), (0.0, -18.003416946018184, 0.0), (0.654758, 0.654758, 0.144915), "Dirt_Mound_I17_2", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2735.0, 1790.0, 855.0), (0.0, 22.897512355297653, -0.0), (1.0, 1.0, 0.871463), "Dirt_Mound_I18_5", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3886.6138, 1273.6971, 905.00525), (0.0, -18.003416946018184, 0.0), (0.654758, 0.654758, 0.654758), "Dirt_Mound_I2", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3585.2625, 840.0932, 838.47534), (11.220505724708541, -19.645143311976124, -12.680786645191562), (0.654758, 0.654758, 0.654758), "Dirt_Mound_I20", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2838.373, 842.22253, 838.47534), (11.220510720808285, 102.67290137561413, -12.684111873897054), (1.2242789, 0.654758, 0.654758), "Dirt_Mound_I21", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4005.5503, 944.4243, 905.00525), (0.0, -18.003416946018184, 0.0), (0.654758, 0.654758, 0.654758), "Dirt_Mound_I3", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5153.2476, 2259.7222, 905.00525), (0.0, -43.00344781631997, 0.0), (0.58076805, 0.58076805, 0.58076805), "Dirt_Mound_I4", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3589.7803, 1216.9362, 841.12384), (0.0, -4.907409859751666, 0.0), (0.654758, 0.654758, 0.654758), "Dirt_Mound_I5", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4702.334, 1201.6216, 889.76184), (0.0, -90.0198405356686, 0.0), (0.89692163, 0.89692163, 1.8230809), "Dirt_Mound_I6_385", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1526.4812, 4058.0422, 842.0698), (0.0, -90.0198405356686, 0.0), (0.896922, 0.896922, 1.823081), "Dirt_Mound_I7", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3640.7236, 2365.0354, 890.6194), (12.360807919701827, 7.6689441141166945, -8.557830366466016), (0.8977113, 0.84445816, 0.6797334), "Dirt_Mound_I8", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3655.0764, 4099.4917, 903.6194), (12.360806567477635, -81.87902051167531, -8.557828829090615), (0.654758, 0.654758, 0.679733), "Dirt_Mound_I9", _folder)
if a: placed += 1
else: skipped += 1

# Batch 66: StaticMesh'Dirt_Mound_I' (1 instances)
_mesh_path = "/Game/Art/Assets/Kits/Misc/Dirt_Mounds/Dirt_Mound_I"
_materials = ['/Game/Art/Assets/Kits/Misc/Dirt_Mounds/Materials/Sururbs_Dirt_Fix_Inst']
_folder = "Reconstruction/BD_BB_Sandbox_DwarfHall_Voxels/Meshes"
a = spawn_static_mesh(_mesh_path, _materials, (3251.1904, 1387.2695, 845.1673), (0.0, 12.93406034180721, -0.0), (0.654758, 0.654758, 0.144915), "Dirt_Mound_I23", _folder)
if a: placed += 1
else: skipped += 1

# Batch 67: StaticMesh'Mining_Dirt_Mound_A' (5 instances)
_mesh_path = "/Game/Art/Assets/Kits/Misc/Dirt_Mounds/Mining_Dirt_Mound_A"
_materials = ['/Game/Art/Assets/Kits/Misc/Dirt_Mounds/Materials/Suburbs_Dirt_Inst']
_folder = "Reconstruction/BD_BB_Sandbox_DwarfHall_Voxels/Meshes"
a = spawn_static_mesh(_mesh_path, _materials, (2235.3135, 2392.427, 860.5973), (-8.30374186625151, -89.10544316600662, -4.339965954381736), (1.0, 1.0, 1.0), "Mining_Dirt_Mound_A_10", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1859.3113, 1225.0256, 853.3148), (0.0, 86.48546514175962, -0.0), (1.0, 1.0, 1.0), "Mining_Dirt_Mound_A2_81", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4114.4277, 5623.4673, 906.2694), (0.0, 142.8476375658422, -0.0), (1.0, 1.0, 1.0), "Mining_Dirt_Mound_A3_3", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4962.409, 4850.416, 906.2694), (0.0, -118.11205982026401, 0.0), (1.0, 1.0, 1.0), "Mining_Dirt_Mound_A5_47", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2486.0464, 2761.228, 899.81537), (0.0, 138.33109246465867, -0.0), (1.0, 1.0, 0.48634955), "Mining_Dirt_Mound_A7_224", _folder)
if a: placed += 1
else: skipped += 1

# Batch 68: StaticMesh'Mining_Dirt_Mound_B' (35 instances)
_mesh_path = "/Game/Art/Assets/Kits/Misc/Dirt_Mounds/Mining_Dirt_Mound_B"
_materials = ['/Game/Art/Assets/Kits/Misc/Dirt_Mounds/Materials/Suburbs_Dirt_Inst']
_folder = "Reconstruction/BD_BB_Sandbox_DwarfHall_Voxels/Meshes"
a = spawn_static_mesh(_mesh_path, _materials, (2214.4504, 2656.7886, 844.4061), (0.0, -179.99998633961752, -0.0), (1.7940159, 1.7940159, 2.19366), "Mining_Dirt_Mound_B_2", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1616.3916, 1585.8308, 844.4061), (0.0, 89.99583826113562, -0.0), (1.794016, 1.794016, 2.19366), "Mining_Dirt_Mound_B10", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2012.3721, 1272.8727, 844.4061), (0.0, 179.99574479211995, -0.0), (1.794016, 1.794016, 2.19366), "Mining_Dirt_Mound_B11", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2829.9597, 2975.11, 800.9317), (0.0, -138.35074827412717, 0.0), (1.0, 1.0, 1.0), "Mining_Dirt_Mound_B14_372", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2904.2307, 3068.796, 800.9317), (0.0, -103.18844099586389, 0.0), (1.0, 1.0, 1.0), "Mining_Dirt_Mound_B15", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2888.2166, 3402.905, 800.93176), (0.0, -25.59472647922142, 0.0), (1.0, 1.0, 1.0), "Mining_Dirt_Mound_B16", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4229.368, 3696.5176, 894.74554), (0.0, 0.0, -0.0), (1.7434455, 1.7434455, 1.7434455), "Mining_Dirt_Mound_B17_398", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3778.7803, 4941.808, 906.33435), (0.0, 0.0, -0.0), (1.0, 1.0, 1.0), "Mining_Dirt_Mound_B18_490", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4705.0293, 5438.955, 900.48627), (0.0, -137.60155077616736, 0.0), (1.0, 1.0, 1.0), "Mining_Dirt_Mound_B19_511", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2001.5214, 2660.7937, 844.4061), (0.0, -179.99998633961752, -0.0), (1.794016, 1.794016, 2.19366), "Mining_Dirt_Mound_B2", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4685.7983, 5300.446, 902.27216), (0.0, -89.78750506865848, 0.0), (1.0, 1.0, 1.0), "Mining_Dirt_Mound_B20_514", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2811.2148, 1388.0856, 850.68335), (0.0, 90.52923117571878, -0.0), (1.794016, 1.794016, 2.19366), "Mining_Dirt_Mound_B21", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2813.248, 1601.0432, 850.68335), (0.0, 90.52923117571878, -0.0), (1.794016, 1.794016, 2.19366), "Mining_Dirt_Mound_B22", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2807.1074, 1829.2593, 850.68335), (0.0, 90.52923117571878, -0.0), (1.794016, 1.794016, 2.19366), "Mining_Dirt_Mound_B23", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2809.1396, 2042.2161, 850.68335), (0.0, 90.52923117571878, -0.0), (1.794016, 1.794016, 2.19366), "Mining_Dirt_Mound_B24", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4799.3364, 4246.4365, 897.0947), (0.0, -88.03894432703426, 0.0), (2.340636, 2.340636, 2.340636), "Mining_Dirt_Mound_B29", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1787.962, 2666.134, 842.68896), (-1.068542220621576, -179.99998633961587, 3.6544276511585494e-07), (1.794016, 1.794016, 2.19366), "Mining_Dirt_Mound_B3", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4182.2163, 5103.1655, 899.5775), (-5.577667197423668, 1.3880005687060395, -0.13497926119469317), (2.016683, 2.016683, 2.016683), "Mining_Dirt_Mound_B31", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4700.2495, 5434.8003, 894.7925), (0.0, -168.31337770784017, 0.0), (2.016683, 2.016683, 2.016683), "Mining_Dirt_Mound_B33", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4492.25, 5145.8354, 897.0947), (0.0, -13.410522077027084, 0.0), (2.016683, 2.016683, 1.6199837), "Mining_Dirt_Mound_B34", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3685.4749, 4310.443, 900.35315), (0.0, -88.20888890522593, 0.0), (1.521443, 1.521443, 2.4951384), "Mining_Dirt_Mound_B35_123", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4565.133, 3718.314, 906.2695), (0.0, -29.901272579171483, 0.0), (1.2713238, 1.2713238, 2.226469), "Mining_Dirt_Mound_B36_20", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4407.165, 3728.3037, 887.0558), (7.072974397262319, -2.3497315942970896, -2.2018735189314236), (1.7410532, 1.43606, 2.226469), "Mining_Dirt_Mound_B37_23", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4795.6777, 3696.642, 906.2694), (0.0, 22.11983487018004, -0.0), (1.271324, 1.271324, 2.226469), "Mining_Dirt_Mound_B38", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1322.9872, 1539.7483, 853.69604), (0.0, -93.50365787912804, 0.0), (1.3099593, 1.039922, 1.039922), "Mining_Dirt_Mound_B4_19", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4668.6, 3783.2273, 906.2695), (0.0, -76.18951398169017, 0.0), (1.271324, 1.271324, 2.226469), "Mining_Dirt_Mound_B40", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4277.4595, 4013.3584, 894.74554), (0.0, 170.35550938966225, -0.0), (1.743446, 1.743446, 1.743446), "Mining_Dirt_Mound_B42", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2005.4929, 2741.8652, 851.2905), (0.0, -152.52304986025248, 0.0), (1.1139547, 1.1139547, 1.6658698), "Mining_Dirt_Mound_B43_9", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2189.412, 2768.2244, 851.2905), (0.0, 171.5598369829155, -0.0), (1.113955, 1.113955, 1.6821771), "Mining_Dirt_Mound_B44", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2347.4512, 2700.4634, 851.2905), (0.0, 143.64539068720418, -0.0), (1.113955, 1.113955, 1.745818), "Mining_Dirt_Mound_B45", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2153.25, 2570.974, 851.2905), (0.0, -9.687743579096933, 0.0), (1.113955, 1.113955, 1.745818), "Mining_Dirt_Mound_B47", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2903.86, 1624.935, 844.2935), (4.096583508177744, 79.21421977520268, 1.2615563561318648e-06), (1.660578, 1.3837504, 1.9064627), "Mining_Dirt_Mound_B55", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2866.5068, 1207.5083, 891.125), (0.0, -83.87423502931091, 0.0), (1.0, 1.0, 1.0), "Mining_Dirt_Mound_B56_130", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1594.525, 2074.9773, 853.69604), (0.0, 86.49659557844485, -0.0), (1.4410928, 1.1710557, 1.1710557), "Mining_Dirt_Mound_B6", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1612.383, 1864.0939, 844.4061), (0.0, 89.9959354918078, -0.0), (1.794016, 1.794016, 2.19366), "Mining_Dirt_Mound_B9", _folder)
if a: placed += 1
else: skipped += 1

# Batch 69: StaticMesh'Mining_Dirt_Mound_C' (24 instances)
_mesh_path = "/Game/Art/Assets/Kits/Misc/Dirt_Mounds/Mining_Dirt_Mound_C"
_materials = ['/Game/Art/Assets/Kits/Misc/Dirt_Mounds/Materials/Suburbs_Dirt_Inst']
_folder = "Reconstruction/BD_BB_Sandbox_DwarfHall_Voxels/Meshes"
a = spawn_static_mesh(_mesh_path, _materials, (5149.1343, 4139.377, 992.76306), (0.0, 81.73609596076841, -0.0), (1.0, 1.0, 1.0), "Mining_Dirt_Mound_C_84", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4748.627, 5369.4136, 933.23785), (9.67309327854845e-07, 45.66339135498529, 52.480863740045), (1.0, 1.0, 1.0), "Mining_Dirt_Mound_C11_55", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3788.992, 4141.72, 1052.406), (6.84955780339814e-06, 45.14384447072363, 70.20905123448883), (1.0, 1.0, 1.0), "Mining_Dirt_Mound_C16_200", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3721.9116, 4152.993, 999.6256), (0.0, -91.23861324855517, 0.0), (1.0, 1.0, 1.0), "Mining_Dirt_Mound_C17_2", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3541.9138, 3980.2046, 916.2351), (-4.569321142158589e-08, 33.40507607293498, 61.90375478881289), (1.0, 1.0, 1.0), "Mining_Dirt_Mound_C18_17", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4723.104, 3999.0051, 900.7085), (0.0, 0.0, -0.0), (1.0, 1.0, 1.0), "Mining_Dirt_Mound_C19_37", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5148.193, 5040.161, 993.70233), (0.0, 85.41151274701718, -0.0), (1.0, 1.0, 1.0), "Mining_Dirt_Mound_C2_106", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4753.034, 4098.5, 900.7085), (0.0, -46.96273902020321, 0.0), (1.0, 1.0, 1.0), "Mining_Dirt_Mound_C20", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4737.29, 3981.8513, 920.0292), (1.0557082990924072, 38.11048801991766, 65.64741280644328), (1.0, 0.763877, 1.0), "Mining_Dirt_Mound_C21_41", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4968.722, 3591.0776, 897.6387), (8.885671252695785, 121.33097828721357, 68.40768516214554), (1.0, 1.0, 1.0), "Mining_Dirt_Mound_C22_44", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4803.8604, 3803.566, 1003.2265), (-38.49694605758749, -170.41223774441045, 0.89939979112883), (1.0, 1.0, 1.0), "Mining_Dirt_Mound_C23_64", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4957.685, 3662.0884, 1005.3009), (-17.508239548073416, -98.10560368345722, -2.7586062664764506), (1.0, 1.0, 0.3509149), "Mining_Dirt_Mound_C24_67", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2950.9863, 2425.2075, 900.8661), (6.627409304402094, -144.3075616949578, 74.22523878351572), (1.0, 1.0, 1.0), "Mining_Dirt_Mound_C26", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1754.5532, 2790.6362, 853.53796), (0.0, -135.82211951789503, 0.0), (1.0, 1.0, 0.62444437), "Mining_Dirt_Mound_C27_210", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1700.4609, 2738.0747, 896.5776), (0.0, -135.82211951789503, 0.0), (1.0, 1.0, 0.624444), "Mining_Dirt_Mound_C28", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1770.3873, 2633.3708, 896.5776), (0.0, 177.90168261412418, -0.0), (1.0, 1.0, 0.624444), "Mining_Dirt_Mound_C29", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2771.8503, 1477.4503, 896.92737), (0.0, 0.0, -0.0), (1.0, 1.0, 0.58869946), "Mining_Dirt_Mound_C3", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2338.548, 2565.8555, 901.53125), (6.3467620800208495, 41.73145777878649, 77.05975114351642), (1.0, 1.0, 1.0), "Mining_Dirt_Mound_C30_215", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5305.6406, 2400.3237, 998.04065), (0.0, 165.58029290187585, -0.0), (1.0, 1.0, 1.0), "Mining_Dirt_Mound_C34", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3844.652, 4841.996, 901.8368), (0.0, 0.0, -0.0), (1.0, 1.0, 1.0), "Mining_Dirt_Mound_C4_496", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5295.8896, 5200.658, 993.9704), (0.0, 0.0, -0.0), (1.0, 1.0, 1.0), "Mining_Dirt_Mound_C5_112", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5356.3945, 4037.506, 906.2694), (0.0, -178.80531672820553, 0.0), (1.0, 1.0, 1.0), "Mining_Dirt_Mound_C6_128", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4939.351, 4153.409, 996.3209), (0.0, -87.1926239717035, 0.0), (1.0, 1.0, 1.0), "Mining_Dirt_Mound_C7_140", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5409.988, 3895.9414, 898.9627), (0.0, 159.33279861212355, -0.0), (1.0, 1.0, 0.7646554), "Mining_Dirt_Mound_C8_164", _folder)
if a: placed += 1
else: skipped += 1

# Batch 70: StaticMesh'Orc_Fort_9X9_Mound' (16 instances)
_mesh_path = "/Game/Art/Assets/Kits/Misc/Dirt_Mounds/Orc_Fort_9X9_Mound"
_materials = ['/Game/Art/Assets/Kits/Misc/Dirt_Mounds/Materials/Suburbs_Dirt_Inst']
_folder = "Reconstruction/BD_BB_Sandbox_DwarfHall_Voxels/Meshes"
a = spawn_static_mesh(_mesh_path, _materials, (2054.0076, 2892.5974, 817.6564), (5.50227059779246, -89.99994205930822, 6.839598600761015e-06), (1.0, 1.0, 1.0), "Orc_Fort_9X9_Mound_361", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3558.0662, 1672.4841, 857.1524), (0.0, 0.0, -0.0), (1.0, 1.0, 1.0), "Orc_Fort_9X9_Mound10", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3558.0662, 2217.8838, 857.1524), (0.0, 0.0, -0.0), (1.0, 1.0, 1.0), "Orc_Fort_9X9_Mound11", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5052.627, 4655.3438, 932.99567), (14.510332795645498, 4.710721847710972, -0.9711605889227968), (1.0, 1.0, 1.0), "Orc_Fort_9X9_Mound12_53", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3608.0662, 4422.4844, 857.1524), (0.0, 0.0, -0.0), (1.0, 1.0, 1.0), "Orc_Fort_9X9_Mound15", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3608.0662, 4772.4844, 857.1524), (0.0, 0.0, -0.0), (1.0, 1.0, 1.0), "Orc_Fort_9X9_Mound16", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2808.0662, 4772.4844, 857.1524), (0.0, -179.99998633961752, -0.0), (1.0, 1.0, 1.0), "Orc_Fort_9X9_Mound17", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2808.0662, 4322.4844, 857.1524), (0.0, -179.99998633961752, -0.0), (1.0, 1.0, 1.0), "Orc_Fort_9X9_Mound18", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1391.6624, 2892.5974, 817.6564), (5.502270435172773, -89.99994202805064, 7.327456840959157e-06), (1.0, 1.0, 1.0), "Orc_Fort_9X9_Mound2", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2544.6414, 2892.5974, 817.6564), (5.502270435172773, -89.99994202805064, 7.327456840959157e-06), (1.0, 1.0, 1.0), "Orc_Fort_9X9_Mound3", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2054.0076, 3460.5022, 805.30597), (5.502269589336988, 90.00000109460008, 7.227067732097483e-06), (1.0, 1.0, 1.0), "Orc_Fort_9X9_Mound4", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2544.6414, 3460.5022, 805.30597), (5.502269589336988, 90.00000109460008, 7.227067732097483e-06), (1.0, 1.0, 1.0), "Orc_Fort_9X9_Mound5", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1015.3479, 3460.5007, 805.3056), (5.502269589336988, 90.00000109460008, 7.227067732097483e-06), (1.0, 1.0, 1.0), "Orc_Fort_9X9_Mound6", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1505.9817, 3460.5007, 805.3056), (5.502269589336988, 90.00000109460008, 7.227067732097483e-06), (1.0, 1.0, 1.0), "Orc_Fort_9X9_Mound7", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2807.1477, 1804.7632, 857.15247), (0.0, -179.99998633961752, -0.0), (1.0, 1.0, 1.0), "Orc_Fort_9X9_Mound8_659", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2460.7263, 1790.8855, 856.2694), (0.0, 0.0, -0.0), (1.0, 1.0, 1.0), "Orc_Fort_9X9_Mound9_675", _folder)
if a: placed += 1
else: skipped += 1

# Batch 71: StaticMesh'Orc_Shanty_Tent_Medium_A_Custom_Mound_B' (2 instances)
_mesh_path = "/Game/Art/Assets/Kits/Misc/Dirt_Mounds/Orc_Shanty_Tent_Medium_A_Custom_Mound_B"
_materials = ['/Game/Art/Assets/Kits/Misc/Dirt_Mounds/Materials/Suburbs_Dirt_Inst']
_folder = "Reconstruction/BD_BB_Sandbox_DwarfHall_Voxels/Meshes"
a = spawn_static_mesh(_mesh_path, _materials, (3897.6592, 3718.391, 900.03577), (0.0, 89.99999818714215, -0.0), (0.75849915, 0.75849915, 0.3179766), "Orc_Shanty_Tent_Medium_A_Custom_Mound_B_391", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3931.8162, 5513.4155, 881.43896), (0.0, -126.64031179424427, 0.0), (0.935056, 0.935056, 0.431344), "Orc_Shanty_Tent_Medium_A_Custom_Mound_B3", _folder)
if a: placed += 1
else: skipped += 1

# Batch 72: StaticMesh'Suburbs_Dirt_Mound_A' (42 instances)
_mesh_path = "/Game/Art/Assets/Kits/Misc/Dirt_Mounds/Suburbs_Dirt_Mound_A"
_materials = ['/Game/Art/Assets/Kits/Misc/Dirt_Mounds/Materials/Suburbs_Dirt_Inst']
_folder = "Reconstruction/BD_BB_Sandbox_DwarfHall_Voxels/Meshes"
a = spawn_static_mesh(_mesh_path, _materials, (1799.5022, 2450.4797, 858.8672), (0.0, 0.0, -0.0), (1.4514799, 1.4514799, 1.4514799), "Suburbs_Dirt_Mound_A_13", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3553.713, 3799.9355, 905.4446), (0.0, 87.19174898961889, -0.0), (1.202297, 1.0, 1.0), "Suburbs_Dirt_Mound_A10", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3688.8667, 5609.8213, 902.5458), (0.0, 0.0, -0.0), (1.0, 1.0, 1.0), "Suburbs_Dirt_Mound_A11_518", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3757.0234, 5589.0503, 939.0798), (55.19324419609438, -51.91634974747774, -3.840332432337721), (0.752815, 0.752815, 0.752815), "Suburbs_Dirt_Mound_A13", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2626.7656, 2029.7433, 865.1444), (0.0, -89.47210119722475, 0.0), (1.45148, 1.45148, 1.45148), "Suburbs_Dirt_Mound_A14", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2831.6506, 2143.619, 869.9441), (-11.764222013021152, 0.0, -0.0), (1.0, 1.0, 1.0), "Suburbs_Dirt_Mound_A15_662", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2419.9922, 2174.1318, 857.1697), (0.0, 0.0, -0.0), (1.0, 1.0, 1.0), "Suburbs_Dirt_Mound_A16_678", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3553.713, 4149.9355, 855.4446), (0.0, 87.19174898961889, -0.0), (1.202297, 1.0, 1.0), "Suburbs_Dirt_Mound_A17", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3553.713, 5059.6816, 855.4446), (0.0, 87.19174898961889, -0.0), (1.202297, 1.0, 1.0), "Suburbs_Dirt_Mound_A18", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3558.7578, 5530.616, 855.4446), (0.0, 87.19174898961889, -0.0), (1.202297, 1.0, 1.0), "Suburbs_Dirt_Mound_A19", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1283.051, 1814.1497, 857.0596), (0.0, -95.42306456623133, 0.0), (1.0, 1.0, 0.33073634), "Suburbs_Dirt_Mound_A2_37", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5290.399, 3984.3782, 1013.7037), (0.012006321884434314, -83.06194698152012, 23.878136041732542), (0.7674422, 0.7674422, 0.7674422), "Suburbs_Dirt_Mound_A20_87", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4950.492, 4988.093, 906.2694), (0.0, 0.0, -0.0), (1.0, 1.0, 1.0), "Suburbs_Dirt_Mound_A21_97", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4922.6377, 5080.4146, 999.2801), (0.0, 0.0, -0.0), (1.0, 1.0, 1.0), "Suburbs_Dirt_Mound_A22_100", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5392.57, 3965.3591, 903.5999), (0.0, -72.79351836808613, 0.0), (1.0, 1.0, 1.0), "Suburbs_Dirt_Mound_A26_161", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4713.385, 5163.4927, 919.931), (-1.234557988798722, -6.938232191393416, -15.13796923422999), (1.0, 1.0, 1.0), "Suburbs_Dirt_Mound_A27_34", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4164.138, 5158.544, 906.2694), (0.0, 176.60247936447675, -0.0), (1.0, 1.0, 0.51236933), "Suburbs_Dirt_Mound_A28_43", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3798.5774, 4516.188, 908.35156), (0.0, 0.0, -0.0), (1.0, 1.0, 1.0), "Suburbs_Dirt_Mound_A29_130", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1356.8003, 1547.8843, 858.31116), (0.0, 0.0, -0.0), (1.0, 1.0, 0.7289608), "Suburbs_Dirt_Mound_A3_52", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3685.4983, 4471.608, 908.4946), (0.0, -62.168063104556296, 0.0), (1.0, 1.0, 1.0), "Suburbs_Dirt_Mound_A30_133", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3857.532, 4464.6978, 906.2694), (0.0, -85.01117450902586, 0.0), (1.0, 1.0, 0.7808359), "Suburbs_Dirt_Mound_A31_148", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3579.029, 4068.6729, 904.8646), (0.0, 0.0, -0.0), (1.0, 1.0, 0.9450986), "Suburbs_Dirt_Mound_A32_11", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4421.1987, 3927.8313, 905.8003), (0.0, 0.0, -0.0), (1.0, 1.0, 1.0), "Suburbs_Dirt_Mound_A33_31", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5013.567, 4517.9956, 902.75006), (5.932182462122835, -131.6400553946963, -5.250061386335483), (1.0, 1.0, 0.7064479), "Suburbs_Dirt_Mound_A34_50", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3961.5354, 3628.0374, 925.42126), (-3.697331015274428e-07, 30.83931053233645, -35.18621974820021), (1.0, 1.0, 1.0), "Suburbs_Dirt_Mound_A35_56", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3961.5354, 3680.968, 1023.7767), (-3.697331015274428e-07, 30.83931053233645, -35.18621974820021), (1.0, 1.0, 1.0), "Suburbs_Dirt_Mound_A36", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4079.6548, 3831.694, 1023.7767), (3.7861013288424e-05, 85.13068576186907, -35.186219127665844), (1.0, 1.0, 1.0), "Suburbs_Dirt_Mound_A37", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2220.27, 2572.0095, 913.30505), (-4.308380157612046, 0.0, -0.0), (1.2878691, 1.217988, 1.0), "Suburbs_Dirt_Mound_A38_19", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2113.541, 2589.4375, 911.90405), (9.289693694150145e-09, 15.814609698112926, -3.216888442923195), (1.2147952, 1.2147952, 1.0695224), "Suburbs_Dirt_Mound_A39", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1127.4247, 1300.1556, 856.33435), (0.0, 43.97006685511278, -0.0), (1.0, 1.0, 0.40128535), "Suburbs_Dirt_Mound_A4_58", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1934.9573, 2619.7522, 883.39685), (7.135272127733035, -43.266962700522726, 5.579966208900691), (1.0, 1.0, 1.0), "Suburbs_Dirt_Mound_A40_27", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2821.307, 767.0485, 875.9788), (-20.897432223113064, 5.3039580771323305, -14.588901224196995), (1.0, 1.0, 1.0), "Suburbs_Dirt_Mound_A44_89", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2732.1938, 1981.0201, 917.10236), (-3.9068604317905002, 81.57813326495767, 1.7366024786488775e-06), (1.4354166, 1.2354859, 0.87869906), "Suburbs_Dirt_Mound_A45_107", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2722.1602, 1833.4064, 918.3159), (4.218113412298129, 92.49659275622543, -0.746765493984477), (1.435417, 1.235486, 0.878699), "Suburbs_Dirt_Mound_A46", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2906.9802, 1304.0325, 901.05475), (0.0, -48.86505122529664, 0.0), (1.0, 1.0, 1.2255801), "Suburbs_Dirt_Mound_A47_133", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2272.0964, 1227.8068, 856.2695), (0.0, 0.0, -0.0), (1.0, 1.0, 1.0), "Suburbs_Dirt_Mound_A5_89", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2552.7195, 2790.9727, 930.1324), (52.24065767370853, -55.98806700681804, 7.169836590635686), (0.65878594, 0.65878594, 0.65878594), "Suburbs_Dirt_Mound_A50_218", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2386.1455, 2663.2644, 899.9229), (0.0, 79.93834478515939, -0.0), (1.0, 1.0, 0.4452225), "Suburbs_Dirt_Mound_A51_221", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5160.4526, 2268.8123, 1023.2999), (-6.542653277270561e-08, 9.794485693744672, -25.345763201082704), (1.0, 1.0, 1.0), "Suburbs_Dirt_Mound_A52_370", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1494.866, 1433.6981, 858.8672), (0.0, 89.9944608350074, -0.0), (1.45148, 1.45148, 1.45148), "Suburbs_Dirt_Mound_A6", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1009.3289, 2956.3618, 801.6567), (0.0, 0.0, -0.0), (1.0, 1.0, 0.6157723), "Suburbs_Dirt_Mound_A7_365", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (674.77356, 3444.5046, 795.3927), (0.0, 0.0, -0.0), (1.0, 1.0, 1.0), "Suburbs_Dirt_Mound_A8_384", _folder)
if a: placed += 1
else: skipped += 1

# Batch 73: StaticMesh'Suburbs_Dirt_Mound_B' (22 instances)
_mesh_path = "/Game/Art/Assets/Kits/Misc/Dirt_Mounds/Suburbs_Dirt_Mound_B"
_materials = ['/Game/Art/Assets/Kits/Misc/Dirt_Mounds/Materials/Suburbs_Dirt_Inst']
_folder = "Reconstruction/BD_BB_Sandbox_DwarfHall_Voxels/Meshes"
a = spawn_static_mesh(_mesh_path, _materials, (1857.1957, 2708.6665, 856.2694), (0.0, 0.0, -0.0), (1.0, 1.0, 1.0), "Suburbs_Dirt_Mound_B_16", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2978.1218, 2304.9255, 856.2694), (0.0, 130.93996795660442, -0.0), (1.0, 1.0, 1.0), "Suburbs_Dirt_Mound_B12", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2967.594, 2353.893, 856.2694), (0.0, 91.6617194738854, -0.0), (1.0, 1.0, 1.0), "Suburbs_Dirt_Mound_B13", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5360.3457, 5175.7603, 906.2695), (0.0, 0.0, -0.0), (1.0, 1.0, 1.0), "Suburbs_Dirt_Mound_B14_152", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5344.0073, 5361.5215, 906.2695), (0.0, 0.0, -0.0), (1.0, 1.2220486, 1.0), "Suburbs_Dirt_Mound_B15", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5357.8325, 5259.5044, 903.3471), (0.0, -103.53237360764253, 0.0), (1.0, 1.222049, 1.0), "Suburbs_Dirt_Mound_B16", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4731.8022, 5180.8896, 927.4045), (17.0047166630604, 9.273699048539646, -15.226378497435709), (1.0, 1.0, 1.0), "Suburbs_Dirt_Mound_B17_37", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1151.756, 1406.2891, 853.6565), (0.0, -148.49638233533, 0.0), (1.3100914, 1.1281204, 0.5714228), "Suburbs_Dirt_Mound_B2_55", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4011.8503, 5029.1177, 906.2694), (0.0, 0.0, -0.0), (1.0, 1.0, 1.0), "Suburbs_Dirt_Mound_B20_114", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3895.5408, 4381.315, 906.2694), (0.0, 50.2244343405895, -0.0), (1.0, 1.0, 1.0), "Suburbs_Dirt_Mound_B21_151", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3869.3066, 4288.5156, 906.2694), (0.0, 174.7067764063754, -0.0), (1.0, 1.0, 1.0), "Suburbs_Dirt_Mound_B22", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3888.8384, 4274.558, 926.6467), (-36.461734782170524, 18.87710692592605, 5.200471508207725e-05), (1.0, 1.0, 1.0), "Suburbs_Dirt_Mound_B23_158", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3868.8845, 4379.0894, 926.6467), (-36.46163503693297, 7.154028519299869, 5.8118536551887096e-05), (1.0, 1.0, 1.0), "Suburbs_Dirt_Mound_B24", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4678.541, 3943.5867, 906.2695), (0.0, -153.38256935511305, 0.0), (1.0, 1.0, 1.0), "Suburbs_Dirt_Mound_B25_34", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3511.8215, 1224.9885, 851.43774), (0.0, 0.0, -0.0), (1.3593252, 1.3593252, 1.3593252), "Suburbs_Dirt_Mound_B29_136", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2121.7605, 2425.3608, 856.2694), (0.0, 0.0, -0.0), (1.4039328, 1.0, 0.6371423), "Suburbs_Dirt_Mound_B3_65", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1941.9679, 2460.372, 862.5992), (-4.18407632218667e-08, -174.7443131438553, 7.7843546963872905), (1.2386494, 1.2290934, 0.8662357), "Suburbs_Dirt_Mound_B4", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2177.628, 1237.098, 856.2694), (0.0, 140.41198691745882, -0.0), (1.0, 1.0, 1.0), "Suburbs_Dirt_Mound_B5_93", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2384.8323, 781.5421, 855.84064), (0.0, 0.0, -0.0), (1.0, 1.0, 0.33517396), "Suburbs_Dirt_Mound_B6_97", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1750.242, 810.6996, 855.84064), (0.0, 27.260509581683426, -0.0), (1.0, 1.0, 0.335174), "Suburbs_Dirt_Mound_B7", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2739.8271, 2149.286, 904.63666), (0.0, 0.0, -0.0), (1.0, 1.0, 1.0), "Suburbs_Dirt_Mound_B8_124", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2977.8137, 3290.917, 806.33435), (0.0, 0.0, -0.0), (1.0, 1.0, 0.41686937), "Suburbs_Dirt_Mound_B9_377", _folder)
if a: placed += 1
else: skipped += 1

# Batch 74: StaticMesh'Suburbs_Dirt_Mound_C' (7 instances)
_mesh_path = "/Game/Art/Assets/Kits/Misc/Dirt_Mounds/Suburbs_Dirt_Mound_C"
_materials = ['/Game/Art/Assets/Kits/Misc/Dirt_Mounds/Materials/Suburbs_Dirt_Inst']
_folder = "Reconstruction/BD_BB_Sandbox_DwarfHall_Voxels/Meshes"
a = spawn_static_mesh(_mesh_path, _materials, (1247.5732, 1470.7881, 851.7787), (0.0, 0.0, -0.0), (1.0, 1.0, 1.0), "Suburbs_Dirt_Mound_C_40", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2967.2686, 1385.5117, 849.4039), (0.0, -77.63302671334485, 0.0), (1.0, 1.0, 1.0), "Suburbs_Dirt_Mound_C10_173", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2068.196, 1235.9825, 850.8011), (0.0, 0.0, -0.0), (1.4901326, 1.0, 1.0), "Suburbs_Dirt_Mound_C2_84", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1933.0292, 1211.2512, 850.8011), (0.0, 0.0, -0.0), (1.490133, 1.0, 1.0), "Suburbs_Dirt_Mound_C3", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2952.182, 2968.3118, 823.116), (15.574346294122359, 4.5667219393393425e-06, 16.659847247488248), (1.0, 1.0, 1.0), "Suburbs_Dirt_Mound_C4_369", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1433.8575, 1752.5364, 917.298), (0.0, 0.0, -0.0), (1.0, 1.0, 1.0), "Suburbs_Dirt_Mound_C5_42", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2466.5588, 1467.8407, 870.4018), (26.334990816367036, -27.241824136448034, -3.4477845117311468), (1.0, 1.0, 1.0), "Suburbs_Dirt_Mound_C6_672", _folder)
if a: placed += 1
else: skipped += 1

# Batch 75: StaticMesh'Suburbs_Dirt_Mound_Corner_1m' (1 instances)
_mesh_path = "/Game/Art/Assets/Kits/Misc/Dirt_Mounds/Suburbs_Dirt_Mound_Corner_1m"
_materials = ['/Game/Art/Assets/Kits/Misc/Dirt_Mounds/Materials/Suburbs_Dirt_Inst']
_folder = "Reconstruction/BD_BB_Sandbox_DwarfHall_Voxels/Meshes"
a = spawn_static_mesh(_mesh_path, _materials, (2952.0037, 2628.046, 904.17114), (0.0, -171.61284197514934, 0.0), (1.0, 1.0, 1.0), "Suburbs_Dirt_Mound_Corner_1m_6", _folder)
if a: placed += 1
else: skipped += 1

# Batch 76: StaticMesh'Suburbs_Dirt_Mound_Corner_2m' (6 instances)
_mesh_path = "/Game/Art/Assets/Kits/Misc/Dirt_Mounds/Suburbs_Dirt_Mound_Corner_2m"
_materials = ['/Game/Art/Assets/Kits/Misc/Dirt_Mounds/Materials/Suburbs_Dirt_Inst']
_folder = "Reconstruction/BD_BB_Sandbox_DwarfHall_Voxels/Meshes"
a = spawn_static_mesh(_mesh_path, _materials, (4806.069, 5063.7837, 910.76074), (0.0, 45.147616215584065, -0.0), (1.0, 1.0, 1.0), "Suburbs_Dirt_Mound_Corner_2m_92", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4099.6294, 5067.805, 909.7063), (0.0, 134.26818401568732, -0.0), (1.0, 1.0, 1.0), "Suburbs_Dirt_Mound_Corner_2m2_101", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3597.668, 4128.4204, 908.6035), (0.0, -44.47790485072504, 0.0), (1.0, 1.0, 1.0), "Suburbs_Dirt_Mound_Corner_2m3_8", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1577.4391, 755.6446, 860.4444), (0.0, 89.86658302938405, -0.0), (1.0, 1.0, 1.0), "Suburbs_Dirt_Mound_Corner_2m5_75", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1391.4668, 758.91895, 860.4444), (0.0, 89.06848360187227, -0.0), (1.0, 1.0, 1.0), "Suburbs_Dirt_Mound_Corner_2m6", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2923.2087, 802.4489, 856.9313), (-15.202242416199631, 134.19658232521823, 0.07854582360019688), (1.0, 1.0, 1.6123321), "Suburbs_Dirt_Mound_Corner_2m7_86", _folder)
if a: placed += 1
else: skipped += 1

# Batch 77: StaticMesh'Suburbs_Dirt_Mound_D' (27 instances)
_mesh_path = "/Game/Art/Assets/Kits/Misc/Dirt_Mounds/Suburbs_Dirt_Mound_D"
_materials = ['/Game/Art/Assets/Kits/Misc/Dirt_Mounds/Materials/Suburbs_Dirt_Inst']
_folder = "Reconstruction/BD_BB_Sandbox_DwarfHall_Voxels/Meshes"
a = spawn_static_mesh(_mesh_path, _materials, (1283.5728, 2137.142, 851.97253), (0.0, 0.0, -0.0), (1.5744978, 1.5744978, 1.5744978), "Suburbs_Dirt_Mound_D_43", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5369.8755, 3841.2104, 905.93427), (0.0, 0.0, -0.0), (1.0, 1.0, 1.0), "Suburbs_Dirt_Mound_D10_167", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4682.605, 5197.16, 924.8121), (7.222814359160698, -0.19201663360344376, -7.597808476801798), (1.3413755, 1.3413755, 1.3413755), "Suburbs_Dirt_Mound_D11_40", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4899.507, 5000.9316, 903.9427), (0.0, 0.0, -0.0), (1.0, 1.0, 1.0), "Suburbs_Dirt_Mound_D15_95", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3893.4753, 4939.775, 906.2694), (0.0, 0.0, -0.0), (1.0, 1.0, 1.0), "Suburbs_Dirt_Mound_D16_104", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3936.3418, 4984.503, 906.2694), (0.0, 35.944983426326694, -0.0), (1.0, 1.0, 1.0), "Suburbs_Dirt_Mound_D17", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3758.759, 4435.0005, 906.81915), (0.0, 0.0, -0.0), (1.7523222, 2.2693315, 2.1700542), "Suburbs_Dirt_Mound_D18_142", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3718.56, 4456.149, 917.75305), (5.585193952776994, -32.81435914959314, 6.532113985806458), (1.0, 1.3002138, 1.0), "Suburbs_Dirt_Mound_D19_145", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2849.749, 1449.1562, 863.6697), (-15.78103644386481, -1.3726806777581322, 5.03531377151557), (1.0, 1.0, 1.0), "Suburbs_Dirt_Mound_D2_665", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3934.068, 4203.555, 904.3524), (0.0, -37.15734927830941, 0.0), (1.3296772, 1.269021, 1.0), "Suburbs_Dirt_Mound_D20_155", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3881.6807, 4336.6475, 913.6293), (-26.02142322561154, 0.0, -0.0), (1.0, 1.0, 1.0), "Suburbs_Dirt_Mound_D21_162", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3790.25, 4483.7563, 921.7213), (3.4222314323855336, 30.235923325715625, 1.9926578866897302), (1.0, 1.0, 1.0), "Suburbs_Dirt_Mound_D22_176", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3538.6455, 3996.1624, 904.1276), (0.0, -38.388340348447784, 0.0), (1.475307, 1.475307, 1.475307), "Suburbs_Dirt_Mound_D23_14", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2022.6913, 2570.7678, 894.67163), (0.0, 0.0, -0.0), (2.8310885, 2.0738044, 2.0738044), "Suburbs_Dirt_Mound_D24_30", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1126.807, 1366.3094, 854.7882), (0.0, 0.0, -0.0), (1.0, 1.0, 1.4007013), "Suburbs_Dirt_Mound_D25_59", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1691.3446, 767.5317, 853.62274), (0.0, 0.0, -0.0), (1.0, 1.0, 0.5206013), "Suburbs_Dirt_Mound_D26_78", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2726.5044, 2029.7816, 920.9052), (0.0, 0.0, -0.0), (2.473339, 2.473339, 2.1564114), "Suburbs_Dirt_Mound_D29_127", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2821.169, 1450.7091, 881.99445), (-15.781036445382638, -1.3726806418588318, 5.0353143464819885), (1.0, 1.0, 1.0), "Suburbs_Dirt_Mound_D3", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3482.9397, 978.1771, 853.3339), (0.0, 0.0, -0.0), (1.3796839, 1.3796839, 1.3796839), "Suburbs_Dirt_Mound_D30_139", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3015.6484, 1291.3304, 853.70404), (0.0, 0.0, -0.0), (1.0, 1.0, 1.0), "Suburbs_Dirt_Mound_D31_142", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2816.742, 1380.6965, 899.9022), (0.0, 44.77440671107637, -0.0), (1.0, 1.0, 1.0), "Suburbs_Dirt_Mound_D32_148", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5286.715, 4061.9202, 993.6807), (0.0, 18.680461367901106, -0.0), (1.0, 1.0, 1.0), "Suburbs_Dirt_Mound_D4_90", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5215.22, 4142.111, 996.8021), (0.0, -36.432586635919485, 0.0), (1.0, 1.0, 1.0), "Suburbs_Dirt_Mound_D5_93", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5217.606, 5055.008, 995.6153), (0.0, 46.506364141729556, -0.0), (1.0, 1.0, 1.0), "Suburbs_Dirt_Mound_D6_109", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5285.4634, 5122.547, 1003.00214), (-13.09643636106185, -38.64904644920135, -2.928589191789349), (1.0, 1.0, 1.0), "Suburbs_Dirt_Mound_D7_121", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5186.934, 5046.5215, 1001.5153), (0.0, 0.0, -9.846069838244027), (0.96397775, 0.96397775, 0.96397775), "Suburbs_Dirt_Mound_D8_124", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5285.4634, 5167.775, 1002.7849), (-13.09643636106185, -38.64904644920135, -2.928589191789349), (1.0, 1.0, 1.0), "Suburbs_Dirt_Mound_D9", _folder)
if a: placed += 1
else: skipped += 1

# Batch 78: StaticMesh'SM_AR_Floor_Stone_100x100x010_B' (2 instances)
_mesh_path = "/Game/Environments/Models/Architecture/Meshes/SM_AR_Floor_Stone_100x100x010_B"
_materials = ['/Game/Environments/Models/Architecture/Materials/MI_ArchSimple_Stone_Floor_A_Lighter_MAT', '/Game/Environments/Models/Architecture/Materials/MI_ArchSimple_Stone_Damaged_A_MAT']
_folder = "Reconstruction/BD_BB_Sandbox_DwarfHall_Voxels/Meshes"
a = spawn_static_mesh(_mesh_path, _materials, (4250.0, 2150.0, 900.0), (0.0, 5.000006090594674, -0.0), (1.0, 1.0, 1.0), "SM_AR_Floor_Stone_100x100x010_B_39", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1850.0, 4950.0, 850.0), (0.0, 5.000565745944915, -0.0), (1.0, 1.0, 1.0), "SM_AR_Floor_Stone_100x100x010_B2_75", _folder)
if a: placed += 1
else: skipped += 1

# Batch 79: StaticMesh'SM_AR_Floor_Stone_100x100x010_Broken' (1 instances)
_mesh_path = "/Game/Environments/Models/Architecture/Meshes/SM_AR_Floor_Stone_100x100x010_Broken"
_materials = ['/Game/Environments/Models/Architecture/Materials/MI_ArchSimple_Stone_Foundation_A_MAT']
_folder = "Reconstruction/BD_BB_Sandbox_DwarfHall_Voxels/Meshes"
a = spawn_static_mesh(_mesh_path, _materials, (1250.0, 4850.0, 850.0), (0.0, -4.999999999933509, 0.0), (1.0, 1.0, 1.0), "SM_AR_Floor_Stone_100x100x010_Broken_81", _folder)
if a: placed += 1
else: skipped += 1

# Batch 80: StaticMesh'SM_AR_Floor_Stone_100x100x010_C' (1 instances)
_mesh_path = "/Game/Environments/Models/Architecture/Meshes/SM_AR_Floor_Stone_100x100x010_C"
_materials = ['/Game/Environments/Models/Architecture/Materials/MI_ArchSimple_Stone_Damaged_A_MAT', '/Game/Environments/Models/Architecture/Materials/MI_ArchSimple_Stone_Floor_A_Lighter_MAT']
_folder = "Reconstruction/BD_BB_Sandbox_DwarfHall_Voxels/Meshes"
a = spawn_static_mesh(_mesh_path, _materials, (1450.0, 5150.0, 850.0), (0.0, -4.999999999933509, 0.0), (1.0, 1.0, 1.0), "SM_AR_Floor_Stone_100x100x010_C_78", _folder)
if a: placed += 1
else: skipped += 1

# Batch 81: StaticMesh'SM_AR_Floor_Stone_200x200x010_B' (3 instances)
_mesh_path = "/Game/Environments/Models/Architecture/Meshes/SM_AR_Floor_Stone_200x200x010_B"
_materials = ['/Game/Environments/Models/Architecture/Materials/MI_ArchSimple_Stone_Floor_A_Lighter_MAT', '/Game/Environments/Models/Architecture/Materials/MI_ArchSimple_Stone_Damaged_A_MAT']
_folder = "Reconstruction/BD_BB_Sandbox_DwarfHall_Voxels/Meshes"
a = spawn_static_mesh(_mesh_path, _materials, (4700.0, 2100.0, 900.0), (0.0, 0.0, -0.0), (1.0, 1.0, 1.0), "SM_AR_Floor_Stone_200x200x010_B_42", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4600.0, 1600.0, 900.0), (0.0, -85.00006134235026, 0.0), (1.0, 1.0, 1.0), "SM_AR_Floor_Stone_200x200x010_B2_54", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1800.0, 5500.0, 850.0), (0.0, -90.00002735739477, 0.0), (1.0, 1.0, 1.0), "SM_AR_Floor_Stone_200x200x010_B3_96", _folder)
if a: placed += 1
else: skipped += 1

# Batch 82: StaticMesh'SM_AR_Floor_Stone_200x200x010_C' (5 instances)
_mesh_path = "/Game/Environments/Models/Architecture/Meshes/SM_AR_Floor_Stone_200x200x010_C"
_materials = ['/Game/Environments/Models/Architecture/Materials/MI_ArchSimple_Stone_Floor_A_Lighter_MAT', '/Game/Environments/Models/Architecture/Materials/MI_ArchSimple_Stone_Damaged_A_MAT']
_folder = "Reconstruction/BD_BB_Sandbox_DwarfHall_Voxels/Meshes"
a = spawn_static_mesh(_mesh_path, _materials, (4200.0, 1700.0, 900.0), (0.0, 0.0, -0.0), (1.0, 1.0, 1.0), "BP_AB_Suburbs_Floor_Stone_200x200x010_C_2", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1700.0, 5200.0, 850.0), (0.0, 0.0, -0.0), (1.0, 1.0, 1.0), "BP_AB_Suburbs_Floor_Stone_200x200x010_C2_8", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1400.0, 4600.0, 850.0), (0.0, 90.00002735739477, -0.0), (1.0, 1.0, 1.0), "SM_AR_Floor_Stone_200x200x010_C_84", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2000.0, 5600.0, 850.0), (0.0, 90.00001925454748, -0.0), (1.0, 1.0, 1.0), "SM_AR_Floor_Stone_200x200x010_C2_93", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2200.0, 4600.0, 850.0), (0.0, -89.99997063746636, 0.0), (1.0, 1.0, 1.0), "SM_AR_Floor_Stone_200x200x010_C3_106", _folder)
if a: placed += 1
else: skipped += 1

# Batch 83: StaticMesh'SM_AR_Floor_Stone_300x300x010_B' (4 instances)
_mesh_path = "/Game/Environments/Models/Architecture/Meshes/SM_AR_Floor_Stone_300x300x010_B"
_materials = ['/Game/Environments/Models/Architecture/Materials/MI_ArchSimple_Stone_Floor_A_Lighter_MAT', '/Game/Environments/Models/Architecture/Materials/MI_ArchSimple_Stone_Damaged_A_MAT']
_folder = "Reconstruction/BD_BB_Sandbox_DwarfHall_Voxels/Meshes"
a = spawn_static_mesh(_mesh_path, _materials, (3750.0, 1750.0, 900.0), (0.0, 0.0, -0.0), (1.0, 1.0, 1.0), "BP_AB_Suburbs_Floor_Stone_300x300x010_B_2", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1750.0, 4650.0, 850.0), (0.0, 0.0, -0.0), (1.0, 1.0, 1.0), "BP_AB_Suburbs_Floor_Stone_300x300x010_B2_5", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4850.0, 1750.0, 900.0), (0.0, -90.00009542133918, 0.0), (1.0, 1.0, 1.0), "SM_AR_Floor_Stone_300x300x010_B_48", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1950.0, 4150.0, 850.0), (0.0, 90.00004680423052, -0.0), (1.0, 1.0, 1.0), "SM_AR_Floor_Stone_300x300x010_B2_87", _folder)
if a: placed += 1
else: skipped += 1

# Batch 84: StaticMesh'SM_AR_Floor_Stone_300x300x010_C' (8 instances)
_mesh_path = "/Game/Environments/Models/Architecture/Meshes/SM_AR_Floor_Stone_300x300x010_C"
_materials = ['/Game/Environments/Models/Architecture/Materials/MI_ArchSimple_Stone_Floor_A_Lighter_MAT', '/Game/Environments/Models/Architecture/Materials/MI_ArchSimple_Stone_Damaged_A_MAT']
_folder = "Reconstruction/BD_BB_Sandbox_DwarfHall_Voxels/Meshes"
a = spawn_static_mesh(_mesh_path, _materials, (4050.0, 1950.0, 900.0), (0.0, 0.0, -0.0), (1.0, 1.0, 1.0), "BP_AB_Suburbs_Floor_Stone_300x300x010_C_2", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1550.0, 4950.0, 850.0), (0.0, 0.0, -0.0), (1.0, 1.0, 1.0), "BP_AB_Suburbs_Floor_Stone_300x300x010_C2_5", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1250.0, 5450.0, 850.0), (0.0, -90.00002735739477, 0.0), (1.0, 1.0, 1.0), "BP_AB_Suburbs_Floor_Stone_300x300x010_C3", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4550.0, 2350.0, 900.0), (0.0, 90.00011648875932, -0.0), (1.0, 1.0, 1.0), "SM_AR_Floor_Stone_300x300x010_C_45", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2250.0, 4050.0, 850.0), (0.0, 0.0, -0.0), (1.0, 1.0, 1.0), "SM_AR_Floor_Stone_300x300x010_C2_90", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2150.0, 5150.0, 850.0), (0.0, -90.00002735739477, 0.0), (1.0, 1.0, 1.0), "SM_AR_Floor_Stone_300x300x010_C3_99", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1050.0, 4750.0, 850.0), (0.0, 179.9998224150775, -0.0), (1.0, 1.0, 1.0), "SM_AR_Floor_Stone_300x300x010_C4", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1950.0, 3650.0, 850.0), (0.0, -89.99999818714215, 0.0), (1.0, 1.0, 1.0), "SM_AR_Floor_Stone_300x300x010_C5_103", _folder)
if a: placed += 1
else: skipped += 1

# Batch 85: StaticMesh'SM_Grass_Patch_Dry_01' (3 instances)
_mesh_path = "/Game/Unshippable/ThirdParty/Lordenfel/Environment/Vegetation/Meshes/SM_Grass_Patch_Dry_01"
_materials = ['/Game/Unshippable/ThirdParty/Lordenfel/Environment/Materials/MI_Grass_Dry_01']
_folder = "Reconstruction/BD_BB_Sandbox_DwarfHall_Voxels/Meshes"
a = spawn_static_mesh(_mesh_path, _materials, (3738.296, 3583.3743, 918.1034), (0.0, 0.0, -0.0), (1.0, 1.0, 1.0), "SM_Grass_Patch_Dry_39", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3469.8643, 3467.2478, 908.2477), (0.0, 0.0, -0.0), (1.0, 1.0, 1.0), "SM_Grass_Patch_Dry_57", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4748.6323, 3554.225, 933.1891), (0.0, 0.0, -0.0), (1.0, 1.0, 1.0), "SM_Grass_Patch_Dry_01_24", _folder)
if a: placed += 1
else: skipped += 1

# Batch 86: StaticMesh'SM_Grass_Patch_Dry_04' (2 instances)
_mesh_path = "/Game/Unshippable/ThirdParty/Lordenfel/Environment/Vegetation/Meshes/SM_Grass_Patch_Dry_04"
_materials = ['/Game/Unshippable/ThirdParty/Lordenfel/Environment/Materials/MI_Grass_Dry_01']
_folder = "Reconstruction/BD_BB_Sandbox_DwarfHall_Voxels/Meshes"
a = spawn_static_mesh(_mesh_path, _materials, (2320.8843, 3169.676, 796.79614), (0.0, 0.0, -0.0), (1.0, 1.0, 1.0), "SM_Grass_Patch_Dry_51", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3639.5588, 3468.6013, 906.2694), (0.0, 0.0, -0.0), (1.0, 1.0, 1.0), "SM_Grass_Patch_Dry_66", _folder)
if a: placed += 1
else: skipped += 1

# Batch 87: StaticMesh'SM_Grass_Patch_Dry_05' (1 instances)
_mesh_path = "/Game/Unshippable/ThirdParty/Lordenfel/Environment/Vegetation/Meshes/SM_Grass_Patch_Dry_05"
_materials = ['/Game/Unshippable/ThirdParty/Lordenfel/Environment/Materials/MI_Grass_Dry_01']
_folder = "Reconstruction/BD_BB_Sandbox_DwarfHall_Voxels/Meshes"
a = spawn_static_mesh(_mesh_path, _materials, (3742.797, 2080.0032, 905.00525), (0.0, 0.0, -0.0), (1.0, 1.0, 1.0), "SM_Grass_Patch_Dry_05_63", _folder)
if a: placed += 1
else: skipped += 1

# Batch 88: StaticMesh'SM_Grass_Patch_Dry_06' (4 instances)
_mesh_path = "/Game/Unshippable/ThirdParty/Lordenfel/Environment/Vegetation/Meshes/SM_Grass_Patch_Dry_06"
_materials = ['/Game/Unshippable/ThirdParty/Lordenfel/Environment/Materials/MI_Grass_Dry_01']
_folder = "Reconstruction/BD_BB_Sandbox_DwarfHall_Voxels/Meshes"
a = spawn_static_mesh(_mesh_path, _materials, (3521.2307, 4035.658, 915.93115), (0.0, 0.0, -0.0), (1.0, 1.0, 1.0), "SM_Grass_Patch_Dry_42", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3706.443, 4956.8374, 920.31445), (0.0, 0.0, -0.0), (1.0, 1.0, 1.0), "SM_Grass_Patch_Dry_45", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3460.7678, 5154.5117, 876.23004), (0.0, 0.0, -0.0), (1.0, 1.0, 1.0), "SM_Grass_Patch_Dry_48", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1959.123, 3205.2605, 792.87085), (0.0, 0.0, -0.0), (1.0, 1.0, 1.0), "SM_Grass_Patch_Dry_54", _folder)
if a: placed += 1
else: skipped += 1

# Batch 89: StaticMesh'SM_Grass_Patch_Dry_07' (1 instances)
_mesh_path = "/Game/Unshippable/ThirdParty/Lordenfel/Environment/Vegetation/Meshes/SM_Grass_Patch_Dry_07"
_materials = ['/Game/Unshippable/ThirdParty/Lordenfel/Environment/Materials/MI_Grass_Dry_01']
_folder = "Reconstruction/BD_BB_Sandbox_DwarfHall_Voxels/Meshes"
a = spawn_static_mesh(_mesh_path, _materials, (3608.0273, 3649.7825, 900.0), (0.0, -45.000056798727684, 0.0), (1.0, 1.0, 1.0), "SM_Grass_Patch_Dry_07_21", _folder)
if a: placed += 1
else: skipped += 1

# Batch 90: StaticMesh'PWM_Quarry_2x2x5_A' (2 instances)
_mesh_path = "/Game/Unshippable/Whitebox/Rocks/Meshes/PWM_Quarry_2x2x5_A"
_materials = ['/Game/Environments/ProcTexturing/ProcMaterial_Quarry_Atlas_2']
_folder = "Reconstruction/BD_BB_Sandbox_DwarfHall_Voxels/Meshes"
a = spawn_static_mesh(_mesh_path, _materials, (4932.208, 1093.5018, 1881.8098), (-7.092558947145714, -165.116316206807, -12.227171515540796), (2.0, 2.0, 2.3786862), "PWM_Quarry_2x2x5_A_19", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5024.5825, 2272.735, 1881.8098), (-7.8721305219874935, -93.80354945115292, -22.283080915287098), (2.0, 2.0, 2.378686), "PWM_Quarry_2x2x5_A2", _folder)
if a: placed += 1
else: skipped += 1

# Batch 91: StaticMesh'PWM_Quarry_4x4x4_A' (17 instances)
_mesh_path = "/Game/Unshippable/Whitebox/Rocks/Meshes/PWM_Quarry_4x4x4_A"
_materials = ['/Game/Environments/ProcTexturing/ProcMaterial_Quarry_Atlas_2']
_folder = "Reconstruction/BD_BB_Sandbox_DwarfHall_Voxels/Meshes"
a = spawn_static_mesh(_mesh_path, _materials, (4900.0, 2150.0, 2450.0), (-4.093994263475549, 35.10290622013961, -2.8728026511866656), (1.0, 1.2842662, 0.7977557), "PWM_Quarry_4x4x4_A_5", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4061.1267, 985.8168, 1051.0692), (-12.416777839920782, -110.50292697435272, -0.4385070798915353), (0.749472, 1.284266, 1.235688), "PWM_Quarry_4x4x4_A10", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2458.7153, 4950.0, 2549.6196), (-4.093994263475549, 35.10290622013961, -2.8728026511866656), (1.0, 1.284266, 0.797756), "PWM_Quarry_4x4x4_A11", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2511.8354, 4265.9146, 2544.972), (-4.093993791580771, -35.102626755178484, 2.8726828349819664), (0.6643487, 1.284266, 0.797756), "PWM_Quarry_4x4x4_A12", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2019.9204, 3944.3115, 2487.626), (1.708181500331472, 109.93027818371698, -4.6997685355417955), (1.0, 1.284266, 0.797756), "PWM_Quarry_4x4x4_A13", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1875.9712, 5076.927, 2491.472), (4.829175353070161, 79.94523570154328, -1.2971492993008875), (0.6623775, 1.284266, 0.797756), "PWM_Quarry_4x4x4_A14", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1611.6174, 4255.026, 2573.1582), (4.530540920679165, -154.9162210664901, -177.88250770604367), (0.694564, 1.284266, 0.5943654), "PWM_Quarry_4x4x4_A15", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1690.6688, 4082.7236, 2632.8027), (11.674030963259936, -140.90220355910324, -4.797180763248927), (0.749472, 1.284266, 0.9242389), "PWM_Quarry_4x4x4_A16", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1553.9883, 4781.2593, 2628.5393), (4.094075775023103, 165.10281739238556, -177.12705760357616), (0.694564, 1.284266, 0.797756), "PWM_Quarry_4x4x4_A17", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4953.12, 1465.9146, 2445.3523), (-4.093993791580771, -35.102626755178484, 2.8726828349819664), (1.0, 1.284266, 0.797756), "PWM_Quarry_4x4x4_A2", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4469.9204, 1144.3114, 2487.626), (1.708181500331472, 109.93027818371698, -4.6997685355417955), (1.0, 1.284266, 0.797756), "PWM_Quarry_4x4x4_A3", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4325.971, 2376.9265, 2491.472), (4.829175514176972, 164.94542116195743, -1.2971496099038375), (1.0, 1.284266, 0.797756), "PWM_Quarry_4x4x4_A4", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4021.272, 1969.9047, 2526.8784), (4.829175051049132, 164.9454211622553, -1.297149605988193), (1.0, 1.284266, 0.797756), "PWM_Quarry_4x4x4_A5", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4061.6174, 1455.0258, 2473.1582), (4.530540335227258, -154.91622106789103, -177.88250771819733), (0.69456375, 1.284266, 0.797756), "PWM_Quarry_4x4x4_A6", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4125.1074, 1253.9146, 2236.4202), (11.674030963259936, -140.90220355910324, -4.797180763248927), (0.7494717, 1.284266, 1.2356882), "PWM_Quarry_4x4x4_A7", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4153.717, 1061.2551, 1810.176), (12.282071854804327, -105.10178259983223, 2.872858745116858), (0.749472, 1.284266, 1.235688), "PWM_Quarry_4x4x4_A8", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4114.1094, 990.85034, 1398.4156), (-12.59167462352114, 64.66289767886379, -0.6629958314940476), (0.749472, 1.284266, 1.235688), "PWM_Quarry_4x4x4_A9", _folder)
if a: placed += 1
else: skipped += 1

# Batch 92: StaticMesh'PWM_Quarry_8x8x8_A' (6 instances)
_mesh_path = "/Game/Unshippable/Whitebox/Rocks/Meshes/PWM_Quarry_8x8x8_A"
_materials = ['/Game/Environments/ProcTexturing/ProcMaterial_Quarry_Atlas_2']
_folder = "Reconstruction/BD_BB_Sandbox_DwarfHall_Voxels/Meshes"
a = spawn_static_mesh(_mesh_path, _materials, (4606.6543, 1700.0, 2747.537), (-10.000000164519466, 0.0, -0.0), (1.0, 1.0, 0.4379149), "PWM_Quarry_8x8x8_A_2", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5407.414, 1750.0, 1888.8547), (10.000004337543727, 6.1228613477970766e-06, -179.9997677735534), (1.0, 1.5540062, 1.1626124), "PWM_Quarry_8x8x8_A2", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4629.5283, 895.32227, 1846.1014), (-9.846678241806963, 84.84887359379589, -178.24647122441175), (0.55377305, 1.554006, 1.162612), "PWM_Quarry_8x8x8_A3", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4815.645, 794.5714, 1216.3988), (2.5887982027746284, -179.9245810055844, -170.26150219860648), (1.4839287, 0.8673061, 1.2930292), "PWM_Quarry_8x8x8_A4", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5340.1797, 1749.9866, 1215.2211), (-0.4349670584575941, -85.01717965221196, 4.980926635743883), (1.5034151, 0.7309731, 1.162612), "PWM_Quarry_8x8x8_A5", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2156.6543, 4500.0, 2747.537), (-10.000000164519466, 0.0, -0.0), (1.0, 1.0, 0.437915), "PWM_Quarry_8x8x8_A6", _folder)
if a: placed += 1
else: skipped += 1

# Batch 93: StaticMesh'PWM_Quarry_Ceilling_Fissure_8x4_A' (9 instances)
_mesh_path = "/Game/Unshippable/Whitebox/Rocks/Meshes/PWM_Quarry_Ceilling_Fissure_8x4_A"
_materials = ['/Game/Environments/ProcTexturing/ProcMaterial_Quarry_Floor_8x4x1']
_folder = "Reconstruction/BD_BB_Sandbox_DwarfHall_Voxels/Meshes"
a = spawn_static_mesh(_mesh_path, _materials, (4600.0, 1100.0, 2250.0), (0.0, 0.0, -0.0), (1.5, 1.5, 1.5), "PWM_Quarry_Ceilling_Fissure_8x4_A_8", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5100.0, 1600.0, 2250.0), (0.0, 90.00001925454748, -0.0), (1.5, 1.5, 1.5), "PWM_Quarry_Ceilling_Fissure_8x4_A2", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4700.0, 2350.0002, 2250.0), (0.0, 164.99991169031665, -0.0), (1.5, 1.5, 1.5), "PWM_Quarry_Ceilling_Fissure_8x4_A3", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3950.0, 1600.0006, 2250.0), (0.0, -84.9999675487271, 0.0), (1.5, 1.5, 1.5), "PWM_Quarry_Ceilling_Fissure_8x4_A4", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4100.0, 2250.0002, 2250.0), (0.0, -135.00001466939858, 0.0), (1.1466072, 1.070129, 1.5), "PWM_Quarry_Ceilling_Fissure_8x4_A5", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2150.0, 3900.0, 2350.0), (0.0, 0.0, -0.0), (1.5, 1.5, 1.5), "PWM_Quarry_Ceilling_Fissure_8x4_A6", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2237.059, 5001.7036, 2450.0), (0.0, 164.99991169031665, -0.0), (1.5, 1.2368336, 1.5), "PWM_Quarry_Ceilling_Fissure_8x4_A7", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1428.5908, 4644.707, 2454.358), (2.796929728924024e-07, -84.99994227018392, 5.000089893286117), (1.5, 1.5, 1.5), "PWM_Quarry_Ceilling_Fissure_8x4_A8", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1650.0, 5100.0, 2350.0), (0.0, 174.99997895502398, -0.0), (1.146607, 0.84129643, 1.5), "PWM_Quarry_Ceilling_Fissure_8x4_A9", _folder)
if a: placed += 1
else: skipped += 1

# Batch 94: StaticMesh'PWM_Quarry_Floor_4x4x4_A' (1 instances)
_mesh_path = "/Game/Unshippable/Whitebox/Rocks/Meshes/PWM_Quarry_Floor_4x4x4_A"
_materials = ['/Game/Environments/ProcTexturing/ProcMaterial_Quarry_Atlas_4']
_folder = "Reconstruction/BD_BB_Sandbox_DwarfHall_Voxels/Meshes"
a = spawn_static_mesh(_mesh_path, _materials, (3230.0, 1370.0, 750.0), (0.0, 0.0, -0.0), (1.1, 1.1, 0.5), "PWM_Quarry_Floor_4x4x4_A_2", _folder)
if a: placed += 1
else: skipped += 1

# Batch 95: StaticMesh'PWM_Quarry_RockDebris_A' (4 instances)
_mesh_path = "/Game/Unshippable/Whitebox/Rocks/Meshes/PWM_Quarry_RockDebris_A"
_materials = ['/Game/Environments/ProcTexturing/ProcMaterial_Quarry_Atlas_5']
_folder = "Reconstruction/BD_BB_Sandbox_DwarfHall_Voxels/Meshes"
a = spawn_static_mesh(_mesh_path, _materials, (2372.6362, 3218.9133, 793.9077), (0.0, -60.91842783324869, 0.0), (1.0, 1.0, 1.0), "PWM_Quarry_RockDebris_A_321", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2150.76, 3121.9763, 797.8323), (0.0, -14.125000798890165, 0.0), (1.0, 1.0, 1.0), "PWM_Quarry_RockDebris_A2", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1950.4974, 3217.482, 795.38654), (0.0, -14.125000798890165, 0.0), (1.0, 1.0, 1.0), "PWM_Quarry_RockDebris_A3", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2020.2756, 2719.2107, 848.57416), (0.0, -14.125000798890165, 0.0), (1.0, 1.0, 1.0), "PWM_Quarry_RockDebris_A8", _folder)
if a: placed += 1
else: skipped += 1

# ======================================================================
# PHASE 2: ConstructionCatalog  (construction blocks)
# ======================================================================
unreal.log(f"[{BUBBLE_NAME}] Phase 2: Placing construction blocks...")

# Construction blocks use DecoVolume transforms (matched by Name)
_folder = "Reconstruction/BD_BB_Sandbox_DwarfHall_Voxels/Construction"

# Construction: BP_Floor_Stone_Polished_100x100x050_A_Breakable46
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Stone
#   Volume: EMorSimpleShape::OrientedBox, BoxExtent: (51.0, 51.0, 27.2)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (2683.2114, 2161.5222, 873.54376), (0.0, 0.0, -0.0), (1.0200, 1.0200, 0.5447), "BP_Floor_Stone_Polished_100x100x050_A_Breakable46", _folder)
if a: placed += 1
else: skipped += 1

# Construction: BP_Floor_Stone_Polished_100x100x050_A_Breakable48
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Stone
#   Volume: EMorSimpleShape::OrientedBox, BoxExtent: (51.0, 51.0, 27.2)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (2683.3826, 2061.5215, 873.54376), (0.0, 0.0, -0.0), (1.0200, 1.0200, 0.5447), "BP_Floor_Stone_Polished_100x100x050_A_Breakable48", _folder)
if a: placed += 1
else: skipped += 1

# Construction: BP_Floor_Stone_Polished_100x100x050_A_Breakable50
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Stone
#   Volume: EMorSimpleShape::OrientedBox, BoxExtent: (51.0, 51.0, 27.2)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (2683.5554, 1961.523, 873.54376), (0.0, 0.0, -0.0), (1.0200, 1.0200, 0.5447), "BP_Floor_Stone_Polished_100x100x050_A_Breakable50", _folder)
if a: placed += 1
else: skipped += 1

# Construction: BP_Floor_Stone_Polished_100x100x050_A_Breakable52
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Stone
#   Volume: EMorSimpleShape::OrientedBox, BoxExtent: (51.0, 51.0, 27.2)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (2683.7273, 1861.5234, 873.54376), (0.0, 0.0, -0.0), (1.0200, 1.0200, 0.5447), "BP_Floor_Stone_Polished_100x100x050_A_Breakable52", _folder)
if a: placed += 1
else: skipped += 1

# Construction: BP_Floor_Stone_Polished_100x100x050_A_Breakable54
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Stone
#   Volume: EMorSimpleShape::OrientedBox, BoxExtent: (51.0, 51.0, 27.2)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (2683.8967, 1761.523, 873.54376), (0.0, 0.0, -0.0), (1.0200, 1.0200, 0.5447), "BP_Floor_Stone_Polished_100x100x050_A_Breakable54", _folder)
if a: placed += 1
else: skipped += 1

# Construction: BP_Floor_Stone_Polished_100x100x050_A_Breakable56
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Stone
#   Volume: EMorSimpleShape::OrientedBox, BoxExtent: (51.0, 51.0, 27.2)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (2684.0686, 1661.5238, 873.54376), (0.0, 0.0, -0.0), (1.0200, 1.0200, 0.5447), "BP_Floor_Stone_Polished_100x100x050_A_Breakable56", _folder)
if a: placed += 1
else: skipped += 1

# Construction: BP_Floor_Stone_Polished_100x100x050_A_Breakable58
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Stone
#   Volume: EMorSimpleShape::OrientedBox, BoxExtent: (51.0, 51.0, 27.2)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (2684.24, 1561.5236, 873.54376), (0.0, 0.0, -0.0), (1.0200, 1.0200, 0.5447), "BP_Floor_Stone_Polished_100x100x050_A_Breakable58", _folder)
if a: placed += 1
else: skipped += 1

# Construction: BP_Floor_Stone_Polished_100x100x050_A_Breakable60
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Stone
#   Volume: EMorSimpleShape::OrientedBox, BoxExtent: (51.0, 51.0, 27.2)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (2684.24, 1461.5236, 873.54376), (0.0, 0.0, -0.0), (1.0200, 1.0200, 0.5447), "BP_Floor_Stone_Polished_100x100x050_A_Breakable60", _folder)
if a: placed += 1
else: skipped += 1

# Construction: BP_Floor_Stone_Polished_100x100x050_A_Breakable93
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Stone
#   Volume: EMorSimpleShape::OrientedBox, BoxExtent: (51.0, 51.0, 27.2)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (4011.917, 5288.399, 923.54376), (0.0, 0.0, -0.0), (1.0200, 1.0200, 0.5447), "BP_Floor_Stone_Polished_100x100x050_A_Breakable93", _folder)
if a: placed += 1
else: skipped += 1

# Construction: BP_Floor_Stone_Polished_100x100x050_A_Breakable94
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Stone
#   Volume: EMorSimpleShape::OrientedBox, BoxExtent: (51.0, 51.0, 27.2)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (4011.917, 5288.399, 873.54376), (0.0, 0.0, -0.0), (1.0200, 1.0200, 0.5447), "BP_Floor_Stone_Polished_100x100x050_A_Breakable94", _folder)
if a: placed += 1
else: skipped += 1

# Construction: BP_Floor_Stone_Polished_100x100x050_A_Breakable95
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Stone
#   Volume: EMorSimpleShape::OrientedBox, BoxExtent: (51.0, 51.0, 27.2)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (4111.9175, 5288.5703, 923.54376), (0.0, 0.0, -0.0), (1.0200, 1.0200, 0.5447), "BP_Floor_Stone_Polished_100x100x050_A_Breakable95", _folder)
if a: placed += 1
else: skipped += 1

# Construction: BP_Floor_Stone_Polished_100x100x050_A_Breakable96
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Stone
#   Volume: EMorSimpleShape::OrientedBox, BoxExtent: (51.0, 51.0, 27.2)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (4111.9175, 5288.5703, 873.54376), (0.0, 0.0, -0.0), (1.0200, 1.0200, 0.5447), "BP_Floor_Stone_Polished_100x100x050_A_Breakable96", _folder)
if a: placed += 1
else: skipped += 1

# Construction: BP_Ruin_Wall_Brick_B2_2
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Stone
#   Volume: EMorSimpleShape::OrientedBox, BoxExtent: (29.3, 24.1, 14.3)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (2296.6958, 2521.409, 1258.0171), (0.0, 0.0, -0.0), (0.5859, 0.4821, 0.2859), "BP_Ruin_Wall_Brick_B2_2", _folder)
if a: placed += 1
else: skipped += 1

# Construction: BP_Ruin_Wall_Brick_B3
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Stone
#   Volume: EMorSimpleShape::OrientedBox, BoxExtent: (29.3, 24.1, 14.3)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (2316.0889, 2521.4338, 1230.0242), (0.0, 0.0, -0.0), (0.5859, 0.4821, 0.2859), "BP_Ruin_Wall_Brick_B3", _folder)
if a: placed += 1
else: skipped += 1

# Construction: BP_Ruin_Wall_Brick_C2_5
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Stone
#   Volume: EMorSimpleShape::OrientedBox, BoxExtent: (32.6, 28.0, 15.7)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (1854.176, 3948.603, 861.94366), (0.0, 0.0, -0.0), (0.6520, 0.5598, 0.3132), "BP_Ruin_Wall_Brick_C2_5", _folder)
if a: placed += 1
else: skipped += 1

# Construction: BP_Ruin_Wall_Brick_C3
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Stone
#   Volume: EMorSimpleShape::OrientedBox, BoxExtent: (32.6, 31.5, 30.1)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (1860.005, 3907.0215, 882.2608), (0.0, 0.0, -0.0), (0.6520, 0.6294, 0.6011), "BP_Ruin_Wall_Brick_C3", _folder)
if a: placed += 1
else: skipped += 1

# Construction: BP_Ruin_Wall_Thick_1x1m_B_Breakable_2
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Stone
#   Volume: EMorSimpleShape::OrientedBox, BoxExtent: (52.4, 49.7, 52.7)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (4700.4937, 3881.9832, 1549.9584), (0.0, 0.0, -0.0), (1.0488, 0.9934, 1.0542), "BP_Ruin_Wall_Thick_1x1m_B_Breakable_2", _folder)
if a: placed += 1
else: skipped += 1

# Construction: BP_Ruin_Wall_Thick_1x1m_B_Breakable2_5
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Stone
#   Volume: EMorSimpleShape::OrientedBox, BoxExtent: (49.7, 52.4, 52.7)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (3898.0168, 4450.4937, 1849.9584), (0.0, 0.0, -0.0), (0.9934, 1.0488, 1.0542), "BP_Ruin_Wall_Thick_1x1m_B_Breakable2_5", _folder)
if a: placed += 1
else: skipped += 1

# Construction: BP_Ruin_Wall_Thick_1x1m_B_Breakable3
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Stone
#   Volume: EMorSimpleShape::OrientedBox, BoxExtent: (49.7, 52.4, 52.7)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (3898.0168, 4650.4937, 1949.9584), (0.0, 0.0, -0.0), (0.9934, 1.0488, 1.0542), "BP_Ruin_Wall_Thick_1x1m_B_Breakable3", _folder)
if a: placed += 1
else: skipped += 1

# Construction: BP_Ruin_Wall_Thick_1x2m_B_Breakable_3
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Stone
#   Volume: EMorSimpleShape::OrientedBox, BoxExtent: (53.1, 98.0, 49.3)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (3899.358, 4599.9863, 1847.744), (0.0, 0.0, -0.0), (1.0624, 1.9599, 0.9851), "BP_Ruin_Wall_Thick_1x2m_B_Breakable_3", _folder)
if a: placed += 1
else: skipped += 1

# Construction: BP_Ruin_Wall_Thick_1x2m_B_Breakable2_2
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Stone
#   Volume: EMorSimpleShape::OrientedBox, BoxExtent: (53.1, 98.0, 49.3)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (1449.3578, 1499.9862, 897.7441), (0.0, 0.0, -0.0), (1.0624, 1.9599, 0.9852), "BP_Ruin_Wall_Thick_1x2m_B_Breakable2_2", _folder)
if a: placed += 1
else: skipped += 1

# Construction: BP_Ruin_Wall_Thick_1x2m_C_Breakable_2
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Stone
#   Volume: EMorSimpleShape::OrientedBox, BoxExtent: (107.9, 47.6, 47.0)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (4349.265, 3877.625, 1140.4452), (0.0, 0.0, -0.0), (2.1571, 0.9517, 0.9394), "BP_Ruin_Wall_Thick_1x2m_C_Breakable_2", _folder)
if a: placed += 1
else: skipped += 1

# Construction: BP_Ruin_Wall_Thick_1x3m_B_Breakable_5
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Stone
#   Volume: EMorSimpleShape::OrientedBox, BoxExtent: (51.2, 150.1, 53.6)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (1451.2899, 2050.0, 902.89703), (0.0, 0.0, -0.0), (1.0250, 3.0018, 1.0725), "BP_Ruin_Wall_Thick_1x3m_B_Breakable_5", _folder)
if a: placed += 1
else: skipped += 1

# Construction: BP_Ruin_Wall_Thick_1x3m_B_Breakable2
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Stone
#   Volume: EMorSimpleShape::OrientedBox, BoxExtent: (150.1, 51.2, 53.6)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (2200.0, 1151.2898, 1297.103), (0.0, 0.0, -0.0), (3.0018, 1.0250, 1.0725), "BP_Ruin_Wall_Thick_1x3m_B_Breakable2", _folder)
if a: placed += 1
else: skipped += 1

# Construction: BP_Ruin_Wall_Thick_1x3m_B_Breakable3_5
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Stone
#   Volume: EMorSimpleShape::OrientedBox, BoxExtent: (150.1, 51.2, 53.6)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (2200.0, 2496.4028, 1197.103), (0.0, 0.0, -0.0), (3.0018, 1.0250, 1.0725), "BP_Ruin_Wall_Thick_1x3m_B_Breakable3_5", _folder)
if a: placed += 1
else: skipped += 1

# Construction: BP_Ruin_Wall_Thick_1x3m_B_Breakable4
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Stone
#   Volume: EMorSimpleShape::OrientedBox, BoxExtent: (51.2, 150.1, 53.6)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (1451.2899, 1750.0, 902.89703), (0.0, 0.0, -0.0), (1.0250, 3.0018, 1.0725), "BP_Ruin_Wall_Thick_1x3m_B_Breakable4", _folder)
if a: placed += 1
else: skipped += 1

# Construction: BP_Ruin_Wall_Thick_1x3m_B_Breakable5_2
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Stone
#   Volume: EMorSimpleShape::OrientedBox, BoxExtent: (51.2, 150.1, 53.6)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (2651.2898, 1650.0, 947.10297), (0.0, 0.0, -0.0), (1.0250, 3.0018, 1.0725), "BP_Ruin_Wall_Thick_1x3m_B_Breakable5_2", _folder)
if a: placed += 1
else: skipped += 1

# Construction: BP_Ruin_Wall_Thick_1x3m_B_Breakable6_5
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Stone
#   Volume: EMorSimpleShape::OrientedBox, BoxExtent: (51.2, 150.1, 53.6)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (3901.2898, 4850.0, 1847.103), (0.0, 0.0, -0.0), (1.0250, 3.0018, 1.0725), "BP_Ruin_Wall_Thick_1x3m_B_Breakable6_5", _folder)
if a: placed += 1
else: skipped += 1

# Construction: BP_Ruin_Wall_Thick_1x3m_B_Breakable7_8
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Stone
#   Volume: EMorSimpleShape::OrientedBox, BoxExtent: (150.1, 51.2, 53.6)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (4750.0005, 5251.29, 952.8975), (0.0, 0.0, -0.0), (3.0018, 1.0250, 1.0726), "BP_Ruin_Wall_Thick_1x3m_B_Breakable7_8", _folder)
if a: placed += 1
else: skipped += 1

# Construction: BP_Ruin_Wall_Thick_1x3m_C_Breakable_2
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Stone
#   Volume: EMorSimpleShape::OrientedBox, BoxExtent: (150.1, 51.2, 50.0)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (2200.0, 2501.2898, 1256.5707), (0.0, 0.0, -0.0), (3.0018, 1.0250, 0.9991), "BP_Ruin_Wall_Thick_1x3m_C_Breakable_2", _folder)
if a: placed += 1
else: skipped += 1

# Construction: BP_Ruin_Wall_Thick_1x3m_C_Breakable2_5
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Stone
#   Volume: EMorSimpleShape::OrientedBox, BoxExtent: (51.2, 150.1, 50.0)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (1451.2898, 1550.0, 993.4293), (0.0, 0.0, -0.0), (1.0250, 3.0018, 0.9991), "BP_Ruin_Wall_Thick_1x3m_C_Breakable2_5", _folder)
if a: placed += 1
else: skipped += 1

# Construction: BP_Ruin_Wall_Thick_3x1m_A_2
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Stone
#   Volume: EMorSimpleShape::OrientedBox, BoxExtent: (51.7, 50.9, 152.1)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (2648.996, 1449.9784, 1050.2668), (0.0, 0.0, -0.0), (1.0339, 1.0178, 3.0420), "BP_Ruin_Wall_Thick_3x1m_A_2", _folder)
if a: placed += 1
else: skipped += 1

# Construction: BP_Ruin_Wall_Thick_3x1m_A10
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Stone
#   Volume: EMorSimpleShape::OrientedBox, BoxExtent: (50.9, 51.7, 152.1)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (1449.9784, 2051.004, 1100.2668), (0.0, 0.0, -0.0), (1.0178, 1.0339, 3.0420), "BP_Ruin_Wall_Thick_3x1m_A10", _folder)
if a: placed += 1
else: skipped += 1

# Construction: BP_Ruin_Wall_Thick_3x1m_A11_18
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Stone
#   Volume: EMorSimpleShape::OrientedBox, BoxExtent: (51.7, 50.9, 152.1)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (4698.996, 3879.9783, 1350.2668), (0.0, 0.0, -0.0), (1.0339, 1.0178, 3.0420), "BP_Ruin_Wall_Thick_3x1m_A11_18", _folder)
if a: placed += 1
else: skipped += 1

# Construction: BP_Ruin_Wall_Thick_3x1m_A12_21
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Stone
#   Volume: EMorSimpleShape::OrientedBox, BoxExtent: (51.7, 50.9, 152.1)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (3898.996, 4549.9785, 1350.2668), (0.0, 0.0, -0.0), (1.0339, 1.0178, 3.0420), "BP_Ruin_Wall_Thick_3x1m_A12_21", _folder)
if a: placed += 1
else: skipped += 1

# Construction: BP_Ruin_Wall_Thick_3x1m_A13
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Stone
#   Volume: EMorSimpleShape::OrientedBox, BoxExtent: (50.9, 51.7, 152.1)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (3899.9783, 4951.004, 1350.2668), (0.0, 0.0, -0.0), (1.0178, 1.0339, 3.0420), "BP_Ruin_Wall_Thick_3x1m_A13", _folder)
if a: placed += 1
else: skipped += 1

# Construction: BP_Ruin_Wall_Thick_3x1m_A2_12
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Stone
#   Volume: EMorSimpleShape::OrientedBox, BoxExtent: (51.7, 50.9, 152.1)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (1448.9961, 2149.9783, 1100.2668), (0.0, 0.0, -0.0), (1.0339, 1.0178, 3.0420), "BP_Ruin_Wall_Thick_3x1m_A2_12", _folder)
if a: placed += 1
else: skipped += 1

# Construction: BP_Ruin_Wall_Thick_3x1m_A3
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Stone
#   Volume: EMorSimpleShape::OrientedBox, BoxExtent: (51.7, 50.9, 152.1)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (1798.9961, 2499.9783, 1000.2669), (0.0, 0.0, -0.0), (1.0339, 1.0178, 3.0420), "BP_Ruin_Wall_Thick_3x1m_A3", _folder)
if a: placed += 1
else: skipped += 1

# Construction: BP_Ruin_Wall_Thick_3x1m_A4_8
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Stone
#   Volume: EMorSimpleShape::OrientedBox, BoxExtent: (51.7, 50.9, 152.1)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (1898.9961, 2499.9783, 1000.2669), (0.0, 0.0, -0.0), (1.0339, 1.0178, 3.0420), "BP_Ruin_Wall_Thick_3x1m_A4_8", _folder)
if a: placed += 1
else: skipped += 1

# Construction: BP_Ruin_Wall_Thick_3x1m_A5_25
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Stone
#   Volume: EMorSimpleShape::OrientedBox, BoxExtent: (51.7, 50.9, 152.1)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (4998.996, 4949.9785, 1050.2668), (0.0, 0.0, -0.0), (1.0339, 1.0178, 3.0420), "BP_Ruin_Wall_Thick_3x1m_A5_25", _folder)
if a: placed += 1
else: skipped += 1

# Construction: BP_Ruin_Wall_Thick_3x1m_A7
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Stone
#   Volume: EMorSimpleShape::OrientedBox, BoxExtent: (50.9, 51.7, 152.1)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (3900.0217, 4948.996, 1050.2668), (0.0, 0.0, -0.0), (1.0178, 1.0339, 3.0420), "BP_Ruin_Wall_Thick_3x1m_A7", _folder)
if a: placed += 1
else: skipped += 1

# Construction: BP_Ruin_Wall_Thick_3x1m_A8
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Stone
#   Volume: EMorSimpleShape::OrientedBox, BoxExtent: (51.7, 50.9, 152.1)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (3901.004, 4550.0215, 1050.2668), (0.0, 0.0, -0.0), (1.0339, 1.0178, 3.0420), "BP_Ruin_Wall_Thick_3x1m_A8", _folder)
if a: placed += 1
else: skipped += 1

# Construction: BP_Ruin_Wall_Thick_3x1m_A9
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Stone
#   Volume: EMorSimpleShape::OrientedBox, BoxExtent: (51.7, 50.9, 152.1)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (2298.996, 2499.9783, 1000.2669), (0.0, 0.0, -0.0), (1.0339, 1.0178, 3.0420), "BP_Ruin_Wall_Thick_3x1m_A9", _folder)
if a: placed += 1
else: skipped += 1

# Construction: BP_Ruin_Wall_Thick_3x1m_B_Breakable_2
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Stone
#   Volume: EMorSimpleShape::OrientedBox, BoxExtent: (51.7, 50.9, 150.2)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (4197.759, 3870.0, 1348.4019), (0.0, 0.0, -0.0), (1.0339, 1.0178, 3.0047), "BP_Ruin_Wall_Thick_3x1m_B_Breakable_2", _folder)
if a: placed += 1
else: skipped += 1

# Construction: BP_Ruin_Wall_Thick_3x1m_B_Breakable4_8
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Stone
#   Volume: EMorSimpleShape::OrientedBox, BoxExtent: (50.9, 51.7, 150.2)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (2645.6768, 1447.7585, 1348.4019), (0.0, 0.0, -0.0), (1.0178, 1.0339, 3.0047), "BP_Ruin_Wall_Thick_3x1m_B_Breakable4_8", _folder)
if a: placed += 1
else: skipped += 1

# Construction: BP_Ruin_Wall_Thick_3x1m_B_Breakable8_8
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Stone
#   Volume: EMorSimpleShape::OrientedBox, BoxExtent: (51.7, 50.9, 150.2)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (1447.7585, 2150.0, 1398.4019), (0.0, 0.0, -0.0), (1.0339, 1.0178, 3.0047), "BP_Ruin_Wall_Thick_3x1m_B_Breakable8_8", _folder)
if a: placed += 1
else: skipped += 1

# Construction: BP_Ruin_Wall_Thick_3x1m_C_Breakable_2
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Stone
#   Volume: EMorSimpleShape::OrientedBox, BoxExtent: (51.7, 49.2, 95.8)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (1452.2415, 2050.0, 1343.9526), (0.0, 0.0, -0.0), (1.0339, 0.9840, 1.9157), "BP_Ruin_Wall_Thick_3x1m_C_Breakable_2", _folder)
if a: placed += 1
else: skipped += 1

# Construction: BP_Ruin_Wall_Thick_3x1m_C_Breakable2_2
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Stone
#   Volume: EMorSimpleShape::OrientedBox, BoxExtent: (51.7, 49.2, 95.8)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (2647.7585, 1850.0, 993.95264), (0.0, 0.0, -0.0), (1.0339, 0.9840, 1.9157), "BP_Ruin_Wall_Thick_3x1m_C_Breakable2_2", _folder)
if a: placed += 1
else: skipped += 1

# Construction: BP_Ruin_Wall_Thick_3x1m_C_Breakable3_2
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Stone
#   Volume: EMorSimpleShape::OrientedBox, BoxExtent: (49.2, 51.7, 95.8)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (4300.0, 3882.2415, 1293.9526), (0.0, 0.0, -0.0), (0.9840, 1.0339, 1.9157), "BP_Ruin_Wall_Thick_3x1m_C_Breakable3_2", _folder)
if a: placed += 1
else: skipped += 1

# Construction: BP_Ruin_Wall_Thick_3x1m_C_Breakable4_2
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Stone
#   Volume: EMorSimpleShape::OrientedBox, BoxExtent: (49.2, 51.7, 95.8)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (2950.0, 1102.2413, 943.95264), (0.0, 0.0, -0.0), (0.9840, 1.0339, 1.9157), "BP_Ruin_Wall_Thick_3x1m_C_Breakable4_2", _folder)
if a: placed += 1
else: skipped += 1

# Construction: BP_Ruin_Wall_Thick_3x1m_C_Breakable6_5
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Stone
#   Volume: EMorSimpleShape::OrientedBox, BoxExtent: (51.7, 49.2, 95.8)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (4997.759, 4950.0, 1293.9526), (0.0, 0.0, -0.0), (1.0339, 0.9840, 1.9157), "BP_Ruin_Wall_Thick_3x1m_C_Breakable6_5", _folder)
if a: placed += 1
else: skipped += 1

# Construction: BP_Ruin_Wall_Thick_3x1m_C_Breakable7
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Stone
#   Volume: EMorSimpleShape::OrientedBox, BoxExtent: (51.7, 49.2, 95.8)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (4997.759, 4250.0, 993.95264), (0.0, 0.0, -0.0), (1.0339, 0.9840, 1.9157), "BP_Ruin_Wall_Thick_3x1m_C_Breakable7", _folder)
if a: placed += 1
else: skipped += 1

# Construction: BP_Ruin_Wall_Thick_3x3m_A_Breakable_5
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Stone
#   Volume: EMorSimpleShape::OrientedBox, BoxExtent: (149.9, 53.2, 150.0)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (4600.0005, 3882.1797, 1049.4979), (0.0, 0.0, -0.0), (2.9982, 1.0637, 3.0002), "BP_Ruin_Wall_Thick_3x3m_A_Breakable_5", _folder)
if a: placed += 1
else: skipped += 1

# Construction: BP_Ruin_Wall_Thick_3x3m_A_Breakable10
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Stone
#   Volume: EMorSimpleShape::OrientedBox, BoxExtent: (53.2, 149.9, 150.0)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (3897.8203, 4350.0005, 1049.4979), (0.0, 0.0, -0.0), (1.0637, 2.9982, 3.0002), "BP_Ruin_Wall_Thick_3x3m_A_Breakable10", _folder)
if a: placed += 1
else: skipped += 1

# Construction: BP_Ruin_Wall_Thick_3x3m_A_Breakable12_2
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Stone
#   Volume: EMorSimpleShape::OrientedBox, BoxExtent: (149.9, 53.2, 150.0)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (1900.0005, 2502.1797, 1299.4979), (0.0, 0.0, -0.0), (2.9982, 1.0637, 3.0002), "BP_Ruin_Wall_Thick_3x3m_A_Breakable12_2", _folder)
if a: placed += 1
else: skipped += 1

# Construction: BP_Ruin_Wall_Thick_3x3m_A_Breakable16
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Stone
#   Volume: EMorSimpleShape::OrientedBox, BoxExtent: (53.2, 149.9, 150.0)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (3897.8203, 4750.0005, 1349.4979), (0.0, 0.0, -0.0), (1.0637, 2.9982, 3.0002), "BP_Ruin_Wall_Thick_3x3m_A_Breakable16", _folder)
if a: placed += 1
else: skipped += 1

# Construction: BP_Ruin_Wall_Thick_3x3m_A_Breakable17
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Stone
#   Volume: EMorSimpleShape::OrientedBox, BoxExtent: (53.2, 149.9, 150.0)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (3897.8203, 4850.0005, 1649.4979), (0.0, 0.0, -0.0), (1.0637, 2.9982, 3.0002), "BP_Ruin_Wall_Thick_3x3m_A_Breakable17", _folder)
if a: placed += 1
else: skipped += 1

# Construction: BP_Ruin_Wall_Thick_3x3m_A_Breakable18_19
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Stone
#   Volume: EMorSimpleShape::OrientedBox, BoxExtent: (53.2, 149.9, 150.0)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (3902.1797, 4549.9995, 1649.4979), (0.0, 0.0, -0.0), (1.0637, 2.9982, 3.0002), "BP_Ruin_Wall_Thick_3x3m_A_Breakable18_19", _folder)
if a: placed += 1
else: skipped += 1

# Construction: BP_Ruin_Wall_Thick_3x3m_A_Breakable26
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Stone
#   Volume: EMorSimpleShape::OrientedBox, BoxExtent: (149.9, 53.2, 150.0)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (4749.9995, 5247.8203, 1149.4979), (0.0, 0.0, -0.0), (2.9982, 1.0637, 3.0002), "BP_Ruin_Wall_Thick_3x3m_A_Breakable26", _folder)
if a: placed += 1
else: skipped += 1

# Construction: BP_Ruin_Wall_Thick_3x3m_A_Breakable36
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Stone
#   Volume: EMorSimpleShape::OrientedBox, BoxExtent: (53.2, 149.9, 150.0)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (5002.1797, 4749.9995, 1049.4979), (0.0, 0.0, -0.0), (1.0637, 2.9982, 3.0002), "BP_Ruin_Wall_Thick_3x3m_A_Breakable36", _folder)
if a: placed += 1
else: skipped += 1

# Construction: BP_Ruin_Wall_Thick_3x3m_A_Breakable38
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Stone
#   Volume: EMorSimpleShape::OrientedBox, BoxExtent: (149.9, 53.2, 150.0)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (2100.0005, 2502.1797, 999.4979), (0.0, 0.0, -0.0), (2.9982, 1.0637, 3.0002), "BP_Ruin_Wall_Thick_3x3m_A_Breakable38", _folder)
if a: placed += 1
else: skipped += 1

# Construction: BP_Ruin_Wall_Thick_3x3m_A_Breakable4
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Stone
#   Volume: EMorSimpleShape::OrientedBox, BoxExtent: (149.9, 53.2, 150.0)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (4300.0005, 3872.1797, 1049.4979), (0.0, 0.0, -0.0), (2.9982, 1.0637, 3.0002), "BP_Ruin_Wall_Thick_3x3m_A_Breakable4", _folder)
if a: placed += 1
else: skipped += 1

# Construction: BP_Ruin_Wall_Thick_3x3m_A_Breakable62
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Stone
#   Volume: EMorSimpleShape::OrientedBox, BoxExtent: (53.2, 149.9, 150.0)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (2652.1797, 2299.9995, 2049.4978), (0.0, 0.0, -0.0), (1.0637, 2.9982, 3.0002), "BP_Ruin_Wall_Thick_3x3m_A_Breakable62", _folder)
if a: placed += 1
else: skipped += 1

# Construction: BP_Ruin_Wall_Thick_3x3m_A_Breakable72
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Stone
#   Volume: EMorSimpleShape::OrientedBox, BoxExtent: (149.9, 53.2, 150.0)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (1900.0005, 1152.1796, 1099.4979), (0.0, 0.0, -0.0), (2.9982, 1.0637, 3.0002), "BP_Ruin_Wall_Thick_3x3m_A_Breakable72", _folder)
if a: placed += 1
else: skipped += 1

# Construction: BP_Ruin_Wall_Thick_3x3m_A_Breakable73
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Stone
#   Volume: EMorSimpleShape::OrientedBox, BoxExtent: (149.9, 53.2, 150.0)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (2200.0005, 1152.1796, 1099.4979), (0.0, 0.0, -0.0), (2.9982, 1.0637, 3.0002), "BP_Ruin_Wall_Thick_3x3m_A_Breakable73", _folder)
if a: placed += 1
else: skipped += 1

# Construction: BP_Ruin_Wall_Thick_3x3m_A_Breakable9
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Stone
#   Volume: EMorSimpleShape::OrientedBox, BoxExtent: (53.2, 149.9, 150.0)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (3897.8203, 4750.0005, 1049.4979), (0.0, 0.0, -0.0), (1.0637, 2.9982, 3.0002), "BP_Ruin_Wall_Thick_3x3m_A_Breakable9", _folder)
if a: placed += 1
else: skipped += 1

# Construction: BP_Ruin_Wall_Thick_3x3m_B_Breakable_2
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Stone
#   Volume: EMorSimpleShape::OrientedBox, BoxExtent: (51.8, 150.0, 150.0)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (3899.8647, 4350.0, 1349.5272), (0.0, 0.0, -0.0), (1.0361, 2.9995, 3.0008), "BP_Ruin_Wall_Thick_3x3m_B_Breakable_2", _folder)
if a: placed += 1
else: skipped += 1

# Construction: BP_Ruin_Wall_Thick_3x3m_B_Breakable2_8
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Stone
#   Volume: EMorSimpleShape::OrientedBox, BoxExtent: (150.0, 51.8, 150.0)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (4450.0, 5249.8647, 1049.5272), (0.0, 0.0, -0.0), (2.9995, 1.0361, 3.0008), "BP_Ruin_Wall_Thick_3x3m_B_Breakable2_8", _folder)
if a: placed += 1
else: skipped += 1

# Construction: BP_Ruin_Wall_Thick_3x3m_C_Breakable_2
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Stone
#   Volume: EMorSimpleShape::OrientedBox, BoxExtent: (52.1, 153.0, 150.2)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (4950.0, 2201.1345, 1047.7528), (0.0, 0.0, -0.0), (1.0424, 3.0591, 3.0045), "BP_Ruin_Wall_Thick_3x3m_C_Breakable_2", _folder)
if a: placed += 1
else: skipped += 1

# Construction: BP_Ruin_Wall_Thick_3x3m_C_Breakable10
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Stone
#   Volume: EMorSimpleShape::OrientedBox, BoxExtent: (153.0, 52.1, 150.2)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (4198.865, 3779.9995, 2052.247), (0.0, 0.0, -0.0), (3.0591, 1.0425, 3.0045), "BP_Ruin_Wall_Thick_3x3m_C_Breakable10", _folder)
if a: placed += 1
else: skipped += 1

# Construction: BP_Ruin_Wall_Thick_3x3m_C_Breakable11_18
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Stone
#   Volume: EMorSimpleShape::OrientedBox, BoxExtent: (52.1, 153.0, 150.2)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (5000.0, 4451.135, 1047.7528), (0.0, 0.0, -0.0), (1.0424, 3.0591, 3.0045), "BP_Ruin_Wall_Thick_3x3m_C_Breakable11_18", _folder)
if a: placed += 1
else: skipped += 1

# Construction: BP_Ruin_Wall_Thick_3x3m_C_Breakable13
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Stone
#   Volume: EMorSimpleShape::OrientedBox, BoxExtent: (153.0, 52.1, 150.2)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (4501.135, 3880.0, 1347.7528), (0.0, 0.0, -0.0), (3.0591, 1.0424, 3.0045), "BP_Ruin_Wall_Thick_3x3m_C_Breakable13", _folder)
if a: placed += 1
else: skipped += 1

# Construction: BP_Ruin_Wall_Thick_3x3m_C_Breakable18
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Stone
#   Volume: EMorSimpleShape::OrientedBox, BoxExtent: (52.1, 153.0, 150.2)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (1450.0, 1851.1346, 1097.7528), (0.0, 0.0, -0.0), (1.0424, 3.0591, 3.0045), "BP_Ruin_Wall_Thick_3x3m_C_Breakable18", _folder)
if a: placed += 1
else: skipped += 1

# Construction: BP_Ruin_Wall_Thick_3x3m_C_Breakable2
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Stone
#   Volume: EMorSimpleShape::OrientedBox, BoxExtent: (52.1, 153.0, 150.2)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (4950.0, 1448.8654, 1047.7528), (0.0, 0.0, -0.0), (1.0424, 3.0591, 3.0045), "BP_Ruin_Wall_Thick_3x3m_C_Breakable2", _folder)
if a: placed += 1
else: skipped += 1

# Construction: BP_Ruin_Wall_Thick_3x3m_C_Breakable22
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Stone
#   Volume: EMorSimpleShape::OrientedBox, BoxExtent: (52.1, 153.0, 150.2)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (2645.677, 1648.8655, 1147.7528), (0.0, 0.0, -0.0), (1.0424, 3.0591, 3.0045), "BP_Ruin_Wall_Thick_3x3m_C_Breakable22", _folder)
if a: placed += 1
else: skipped += 1

# Construction: BP_Ruin_Wall_Thick_3x3m_C_Breakable26
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Stone
#   Volume: EMorSimpleShape::OrientedBox, BoxExtent: (153.0, 52.1, 150.2)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (1898.8655, 1150.0, 1397.7528), (0.0, 0.0, -0.0), (3.0591, 1.0424, 3.0045), "BP_Ruin_Wall_Thick_3x3m_C_Breakable26", _folder)
if a: placed += 1
else: skipped += 1

# Construction: BP_Ruin_Wall_Thick_3x3m_C_Breakable3
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Stone
#   Volume: EMorSimpleShape::OrientedBox, BoxExtent: (153.0, 52.1, 150.2)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (2198.8655, 2498.093, 1447.7528), (0.0, 0.0, -0.0), (3.0591, 1.0424, 3.0045), "BP_Ruin_Wall_Thick_3x3m_C_Breakable3", _folder)
if a: placed += 1
else: skipped += 1

# Construction: BP_Ruin_Wall_Thick_3x3m_C_Breakable4
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Stone
#   Volume: EMorSimpleShape::OrientedBox, BoxExtent: (65.0, 153.0, 154.2)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (3712.878, 3998.8652, 2152.8096), (0.0, 0.0, -0.0), (1.3003, 3.0591, 3.0840), "BP_Ruin_Wall_Thick_3x3m_C_Breakable4", _folder)
if a: placed += 1
else: skipped += 1

# Construction: BP_Ruin_Wall_Thick_3x3m_C_Breakable6_11
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Stone
#   Volume: EMorSimpleShape::OrientedBox, BoxExtent: (153.0, 52.1, 150.2)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (4751.135, 5250.0, 1447.7528), (0.0, 0.0, -0.0), (3.0591, 1.0424, 3.0045), "BP_Ruin_Wall_Thick_3x3m_C_Breakable6_11", _folder)
if a: placed += 1
else: skipped += 1

# Construction: BP_Ruin_Wall_Thick_3x3m_C_Breakable7
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Stone
#   Volume: EMorSimpleShape::OrientedBox, BoxExtent: (153.0, 52.1, 150.2)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (4148.865, 5250.0, 1147.7528), (0.0, 0.0, -0.0), (3.0591, 1.0424, 3.0045), "BP_Ruin_Wall_Thick_3x3m_C_Breakable7", _folder)
if a: placed += 1
else: skipped += 1

# Construction: BP_Ruin_Wall_Thick_3x3m_D_Breakable_2
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Stone
#   Volume: EMorSimpleShape::OrientedBox, BoxExtent: (149.7, 51.2, 146.8)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (4800.0, 1299.366, 1046.272), (0.0, 0.0, -0.0), (2.9947, 1.0242, 2.9363), "BP_Ruin_Wall_Thick_3x3m_D_Breakable_2", _folder)
if a: placed += 1
else: skipped += 1

# Construction: BP_Ruin_Wall_Thick_3x3m_D_Breakable10
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Stone
#   Volume: EMorSimpleShape::OrientedBox, BoxExtent: (52.1, 153.0, 150.2)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (2646.565, 2051.1338, 1097.7528), (0.0, 0.0, -0.0), (1.0424, 3.0591, 3.0045), "BP_Ruin_Wall_Thick_3x3m_D_Breakable10", _folder)
if a: placed += 1
else: skipped += 1

# Construction: BP_Ruin_Wall_Thick_3x3m_D_Breakable2_17
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Stone
#   Volume: EMorSimpleShape::OrientedBox, BoxExtent: (51.2, 149.7, 146.8)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (5000.634, 4750.0, 1346.272), (0.0, 0.0, -0.0), (1.0242, 2.9947, 2.9363), "BP_Ruin_Wall_Thick_3x3m_D_Breakable2_17", _folder)
if a: placed += 1
else: skipped += 1

# Construction: BP_Ruin_Wall_Thick_3x3m_D_Breakable5_5
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Stone
#   Volume: EMorSimpleShape::OrientedBox, BoxExtent: (149.7, 51.2, 146.8)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (1900.0, 2499.366, 1596.272), (0.0, 0.0, -0.0), (2.9947, 1.0242, 2.9363), "BP_Ruin_Wall_Thick_3x3m_D_Breakable5_5", _folder)
if a: placed += 1
else: skipped += 1

# Construction: BP_Ruin_Wall_Thin_1x3m_B_Breakable_2
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Stone
#   Volume: EMorSimpleShape::OrientedBox, BoxExtent: (147.3, 26.6, 52.4)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (2200.0, 1174.3926, 901.9256), (0.0, 0.0, -0.0), (2.9467, 0.5325, 1.0488), "BP_Ruin_Wall_Thin_1x3m_B_Breakable_2", _folder)
if a: placed += 1
else: skipped += 1

# Construction: BP_Ruin_Wall_Thin_1x3m_B_Breakable2
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Stone
#   Volume: EMorSimpleShape::OrientedBox, BoxExtent: (147.3, 26.6, 52.4)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (1900.0, 1174.3926, 901.9256), (0.0, 0.0, -0.0), (2.9467, 0.5325, 1.0488), "BP_Ruin_Wall_Thin_1x3m_B_Breakable2", _folder)
if a: placed += 1
else: skipped += 1

# Construction: BP_Ruin_Wall_Trim_B_3m_Breakable_2
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Stone
#   Volume: EMorSimpleShape::OrientedBox, BoxExtent: (149.9, 18.6, 25.1)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (1900.033, 2568.4683, 974.84607), (0.0, 0.0, -0.0), (2.9984, 0.3715, 0.5017), "BP_Ruin_Wall_Trim_B_3m_Breakable_2", _folder)
if a: placed += 1
else: skipped += 1

# Construction: BP_Ruin_Wall_Trim_B_3m_Breakable10
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Stone
#   Volume: EMorSimpleShape::OrientedBox, BoxExtent: (18.6, 149.9, 25.1)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (2717.773, 1949.967, 974.84607), (0.0, 0.0, -0.0), (0.3715, 2.9984, 0.5017), "BP_Ruin_Wall_Trim_B_3m_Breakable10", _folder)
if a: placed += 1
else: skipped += 1

# Construction: BP_Ruin_Wall_Trim_B_3m_Breakable11_6
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Stone
#   Volume: EMorSimpleShape::OrientedBox, BoxExtent: (18.6, 149.9, 25.1)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (3831.5334, 4250.0327, 974.8461), (0.0, 0.0, -0.0), (0.3716, 2.9984, 0.5017), "BP_Ruin_Wall_Trim_B_3m_Breakable11_6", _folder)
if a: placed += 1
else: skipped += 1

# Construction: BP_Ruin_Wall_Trim_B_3m_Breakable12_10
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Stone
#   Volume: EMorSimpleShape::OrientedBox, BoxExtent: (18.6, 149.9, 25.1)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (5068.469, 4599.967, 974.8461), (0.0, 0.0, -0.0), (0.3715, 2.9984, 0.5017), "BP_Ruin_Wall_Trim_B_3m_Breakable12_10", _folder)
if a: placed += 1
else: skipped += 1

# Construction: BP_Ruin_Wall_Trim_B_3m_Breakable13
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Stone
#   Volume: EMorSimpleShape::OrientedBox, BoxExtent: (18.6, 149.9, 25.1)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (5068.4697, 4299.9683, 974.8461), (0.0, 0.0, -0.0), (0.3715, 2.9984, 0.5017), "BP_Ruin_Wall_Trim_B_3m_Breakable13", _folder)
if a: placed += 1
else: skipped += 1

# Construction: BP_Ruin_Wall_Trim_B_3m_Breakable14
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Stone
#   Volume: EMorSimpleShape::OrientedBox, BoxExtent: (18.6, 149.9, 25.1)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (5068.4688, 4899.9673, 974.8461), (0.0, 0.0, -0.0), (0.3715, 2.9984, 0.5017), "BP_Ruin_Wall_Trim_B_3m_Breakable14", _folder)
if a: placed += 1
else: skipped += 1

# Construction: BP_Ruin_Wall_Trim_B_3m_Breakable15
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Stone
#   Volume: EMorSimpleShape::OrientedBox, BoxExtent: (149.9, 18.6, 25.1)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (4449.968, 3811.166, 974.8461), (0.0, 0.0, -0.0), (2.9984, 0.3715, 0.5017), "BP_Ruin_Wall_Trim_B_3m_Breakable15", _folder)
if a: placed += 1
else: skipped += 1

# Construction: BP_Ruin_Wall_Trim_B_3m_Breakable16
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Stone
#   Volume: EMorSimpleShape::OrientedBox, BoxExtent: (149.9, 18.6, 25.1)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (4149.969, 3811.1667, 974.8461), (0.0, 0.0, -0.0), (2.9984, 0.3715, 0.5017), "BP_Ruin_Wall_Trim_B_3m_Breakable16", _folder)
if a: placed += 1
else: skipped += 1

# Construction: BP_Ruin_Wall_Trim_B_3m_Breakable17
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Stone
#   Volume: EMorSimpleShape::OrientedBox, BoxExtent: (149.9, 18.6, 25.1)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (4749.9683, 3811.166, 974.8461), (0.0, 0.0, -0.0), (2.9984, 0.3715, 0.5017), "BP_Ruin_Wall_Trim_B_3m_Breakable17", _folder)
if a: placed += 1
else: skipped += 1

# Construction: BP_Ruin_Wall_Trim_B_3m_Breakable18_23
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Stone
#   Volume: EMorSimpleShape::OrientedBox, BoxExtent: (149.9, 18.6, 25.1)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (4400.034, 5318.467, 974.8461), (0.0, 0.0, -0.0), (2.9984, 0.3716, 0.5017), "BP_Ruin_Wall_Trim_B_3m_Breakable18_23", _folder)
if a: placed += 1
else: skipped += 1

# Construction: BP_Ruin_Wall_Trim_B_3m_Breakable19_24
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Stone
#   Volume: EMorSimpleShape::OrientedBox, BoxExtent: (149.9, 18.6, 25.1)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (4700.0337, 5318.467, 974.8461), (0.0, 0.0, -0.0), (2.9984, 0.3716, 0.5017), "BP_Ruin_Wall_Trim_B_3m_Breakable19_24", _folder)
if a: placed += 1
else: skipped += 1

# Construction: BP_Ruin_Wall_Trim_B_3m_Breakable2
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Stone
#   Volume: EMorSimpleShape::OrientedBox, BoxExtent: (149.9, 18.6, 25.1)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (2200.033, 2568.4683, 974.8461), (0.0, 0.0, -0.0), (2.9984, 0.3715, 0.5017), "BP_Ruin_Wall_Trim_B_3m_Breakable2", _folder)
if a: placed += 1
else: skipped += 1

# Construction: BP_Ruin_Wall_Trim_B_3m_Breakable20_25
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Stone
#   Volume: EMorSimpleShape::OrientedBox, BoxExtent: (149.9, 18.6, 25.1)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (4100.0337, 5318.4673, 974.8461), (0.0, 0.0, -0.0), (2.9984, 0.3716, 0.5017), "BP_Ruin_Wall_Trim_B_3m_Breakable20_25", _folder)
if a: placed += 1
else: skipped += 1

# Construction: BP_Ruin_Wall_Trim_B_3m_Breakable5
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Stone
#   Volume: EMorSimpleShape::OrientedBox, BoxExtent: (18.6, 149.9, 25.1)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (3831.5334, 4550.0327, 974.8461), (0.0, 0.0, -0.0), (0.3716, 2.9984, 0.5017), "BP_Ruin_Wall_Trim_B_3m_Breakable5", _folder)
if a: placed += 1
else: skipped += 1

# Construction: BP_Ruin_Wall_Trim_B_3m_Breakable6
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Stone
#   Volume: EMorSimpleShape::OrientedBox, BoxExtent: (18.6, 149.9, 25.1)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (3831.5325, 4850.0327, 974.8461), (0.0, 0.0, -0.0), (0.3716, 2.9984, 0.5017), "BP_Ruin_Wall_Trim_B_3m_Breakable6", _folder)
if a: placed += 1
else: skipped += 1

# Construction: BP_Ruin_Wall_Trim_B_3m_Breakable8
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Stone
#   Volume: EMorSimpleShape::OrientedBox, BoxExtent: (18.6, 149.9, 25.1)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (1381.5315, 1650.033, 974.84607), (0.0, 0.0, -0.0), (0.3715, 2.9984, 0.5017), "BP_Ruin_Wall_Trim_B_3m_Breakable8", _folder)
if a: placed += 1
else: skipped += 1

# Construction: BP_Ruin_Wall_Trim_B_3m_Breakable9
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Stone
#   Volume: EMorSimpleShape::OrientedBox, BoxExtent: (18.6, 149.9, 25.1)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (2717.7732, 1549.9672, 974.84607), (0.0, 0.0, -0.0), (0.3715, 2.9984, 0.5017), "BP_Ruin_Wall_Trim_B_3m_Breakable9", _folder)
if a: placed += 1
else: skipped += 1

# Construction: BP_Suburbs_Wall_Thick_1x3m_A3
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Advanced
#   Volume: EMorSimpleShape::OrientedBox, BoxExtent: (151.5, 50.0, 50.8)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (2200.0, 2538.1587, 900.2109), (0.0, 0.0, -0.0), (3.0300, 1.0000, 1.0150), "BP_Suburbs_Wall_Thick_1x3m_A3", _folder)
if a: placed += 1
else: skipped += 1

# Construction: BP_Suburbs_Wall_Thick_1x3m_A4
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Advanced
#   Volume: EMorSimpleShape::OrientedBox, BoxExtent: (151.5, 50.0, 50.8)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (1900.0, 2538.1587, 900.2109), (0.0, 0.0, -0.0), (3.0300, 1.0000, 1.0150), "BP_Suburbs_Wall_Thick_1x3m_A4", _folder)
if a: placed += 1
else: skipped += 1

# Construction: BP_Suburbs_Wall_Thin_05x3m_A_13
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Stone
#   Volume: EMorSimpleShape::OrientedBox, BoxExtent: (150.0, 25.0, 26.1)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (4300.0, 3817.255, 925.63715), (0.0, 0.0, -0.0), (3.0000, 0.5000, 0.5226), "BP_Suburbs_Wall_Thin_05x3m_A_13", _folder)
if a: placed += 1
else: skipped += 1

# Construction: BP_Suburbs_Wall_Thin_05x3m_A10
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Stone
#   Volume: EMorSimpleShape::OrientedBox, BoxExtent: (25.0, 150.0, 26.1)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (5085.329, 4600.0, 925.63715), (0.0, 0.0, -0.0), (0.5000, 3.0000, 0.5226), "BP_Suburbs_Wall_Thin_05x3m_A10", _folder)
if a: placed += 1
else: skipped += 1

# Construction: BP_Suburbs_Wall_Thin_05x3m_A11
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Stone
#   Volume: EMorSimpleShape::OrientedBox, BoxExtent: (25.0, 150.0, 26.1)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (5085.329, 4300.0, 925.63715), (0.0, 0.0, -0.0), (0.5000, 3.0000, 0.5226), "BP_Suburbs_Wall_Thin_05x3m_A11", _folder)
if a: placed += 1
else: skipped += 1

# Construction: BP_Suburbs_Wall_Thin_05x3m_A12_41
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Stone
#   Volume: EMorSimpleShape::OrientedBox, BoxExtent: (25.0, 150.0, 26.1)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (5035.329, 4900.0, 925.63715), (0.0, 0.0, -0.0), (0.5000, 3.0000, 0.5226), "BP_Suburbs_Wall_Thin_05x3m_A12_41", _folder)
if a: placed += 1
else: skipped += 1

# Construction: BP_Suburbs_Wall_Thin_05x3m_A13_42
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Stone
#   Volume: EMorSimpleShape::OrientedBox, BoxExtent: (25.0, 150.0, 26.1)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (5035.329, 4600.0, 925.63715), (0.0, 0.0, -0.0), (0.5000, 3.0000, 0.5226), "BP_Suburbs_Wall_Thin_05x3m_A13_42", _folder)
if a: placed += 1
else: skipped += 1

# Construction: BP_Suburbs_Wall_Thin_05x3m_A14_43
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Stone
#   Volume: EMorSimpleShape::OrientedBox, BoxExtent: (25.0, 150.0, 26.1)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (5035.329, 4300.0, 925.63715), (0.0, 0.0, -0.0), (0.5000, 3.0000, 0.5226), "BP_Suburbs_Wall_Thin_05x3m_A14_43", _folder)
if a: placed += 1
else: skipped += 1

# Construction: BP_Suburbs_Wall_Thin_05x3m_A16
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Stone
#   Volume: EMorSimpleShape::OrientedBox, BoxExtent: (150.0, 25.0, 26.1)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (4585.3296, 5263.5654, 925.63715), (0.0, 0.0, -0.0), (3.0000, 0.5000, 0.5226), "BP_Suburbs_Wall_Thin_05x3m_A16", _folder)
if a: placed += 1
else: skipped += 1

# Construction: BP_Suburbs_Wall_Thin_05x3m_A17
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Stone
#   Volume: EMorSimpleShape::OrientedBox, BoxExtent: (150.0, 25.0, 26.1)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (4285.329, 5263.5664, 925.63715), (0.0, 0.0, -0.0), (3.0000, 0.5000, 0.5226), "BP_Suburbs_Wall_Thin_05x3m_A17", _folder)
if a: placed += 1
else: skipped += 1

# Construction: BP_Suburbs_Wall_Thin_05x3m_A18
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Stone
#   Volume: EMorSimpleShape::OrientedBox, BoxExtent: (150.0, 25.0, 26.1)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (4585.3296, 5313.5654, 925.63715), (0.0, 0.0, -0.0), (3.0000, 0.5000, 0.5226), "BP_Suburbs_Wall_Thin_05x3m_A18", _folder)
if a: placed += 1
else: skipped += 1

# Construction: BP_Suburbs_Wall_Thin_05x3m_A19
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Stone
#   Volume: EMorSimpleShape::OrientedBox, BoxExtent: (150.0, 25.0, 26.1)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (4285.329, 5313.5664, 925.63715), (0.0, 0.0, -0.0), (3.0000, 0.5000, 0.5226), "BP_Suburbs_Wall_Thin_05x3m_A19", _folder)
if a: placed += 1
else: skipped += 1

# Construction: BP_Suburbs_Wall_Thin_05x3m_A2
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Stone
#   Volume: EMorSimpleShape::OrientedBox, BoxExtent: (150.0, 25.0, 26.1)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (4600.0, 3817.255, 925.63715), (0.0, 0.0, -0.0), (3.0000, 0.5000, 0.5226), "BP_Suburbs_Wall_Thin_05x3m_A2", _folder)
if a: placed += 1
else: skipped += 1

# Construction: BP_Suburbs_Wall_Thin_05x3m_A3_20
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Stone
#   Volume: EMorSimpleShape::OrientedBox, BoxExtent: (25.0, 150.0, 26.1)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (3835.329, 4900.0, 925.63715), (0.0, 0.0, -0.0), (0.5000, 3.0000, 0.5226), "BP_Suburbs_Wall_Thin_05x3m_A3_20", _folder)
if a: placed += 1
else: skipped += 1

# Construction: BP_Suburbs_Wall_Thin_05x3m_A4
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Stone
#   Volume: EMorSimpleShape::OrientedBox, BoxExtent: (25.0, 150.0, 26.1)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (3835.329, 4600.0, 925.63715), (0.0, 0.0, -0.0), (0.5000, 3.0000, 0.5226), "BP_Suburbs_Wall_Thin_05x3m_A4", _folder)
if a: placed += 1
else: skipped += 1

# Construction: BP_Suburbs_Wall_Thin_05x3m_A5
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Stone
#   Volume: EMorSimpleShape::OrientedBox, BoxExtent: (25.0, 150.0, 26.1)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (3835.329, 4300.0, 925.63715), (0.0, 0.0, -0.0), (0.5000, 3.0000, 0.5226), "BP_Suburbs_Wall_Thin_05x3m_A5", _folder)
if a: placed += 1
else: skipped += 1

# Construction: BP_Suburbs_Wall_Thin_05x3m_A6
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Stone
#   Volume: EMorSimpleShape::OrientedBox, BoxExtent: (25.0, 150.0, 26.1)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (3885.329, 4900.0, 925.63715), (0.0, 0.0, -0.0), (0.5000, 3.0000, 0.5226), "BP_Suburbs_Wall_Thin_05x3m_A6", _folder)
if a: placed += 1
else: skipped += 1

# Construction: BP_Suburbs_Wall_Thin_05x3m_A7
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Stone
#   Volume: EMorSimpleShape::OrientedBox, BoxExtent: (25.0, 150.0, 26.1)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (3885.329, 4600.0, 925.63715), (0.0, 0.0, -0.0), (0.5000, 3.0000, 0.5226), "BP_Suburbs_Wall_Thin_05x3m_A7", _folder)
if a: placed += 1
else: skipped += 1

# Construction: BP_Suburbs_Wall_Thin_05x3m_A8
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Stone
#   Volume: EMorSimpleShape::OrientedBox, BoxExtent: (25.0, 150.0, 26.1)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (3885.329, 4300.0, 925.63715), (0.0, 0.0, -0.0), (0.5000, 3.0000, 0.5226), "BP_Suburbs_Wall_Thin_05x3m_A8", _folder)
if a: placed += 1
else: skipped += 1

# Construction: BP_Suburbs_Wall_Thin_05x3m_A9
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Stone
#   Volume: EMorSimpleShape::OrientedBox, BoxExtent: (25.0, 150.0, 26.1)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (5085.329, 4900.0, 925.63715), (0.0, 0.0, -0.0), (0.5000, 3.0000, 0.5226), "BP_Suburbs_Wall_Thin_05x3m_A9", _folder)
if a: placed += 1
else: skipped += 1

# Construction: BP_Suburbs_Wall_Thin_1x2m_A_2
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Stone
#   Volume: EMorSimpleShape::OrientedBox, BoxExtent: (25.0, 100.0, 50.0)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (1387.4695, 1500.0, 899.4687), (0.0, 0.0, -0.0), (0.5000, 2.0000, 1.0000), "BP_Suburbs_Wall_Thin_1x2m_A_2", _folder)
if a: placed += 1
else: skipped += 1

# Construction: Ruin_Wall_Brick_E_Blueprint2_5
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Stone
#   Volume: EMorSimpleShape::OrientedBox, BoxExtent: (33.9, 30.1, 25.2)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (1765.2573, 4008.9573, 915.72833), (0.0, 0.0, -0.0), (0.6786, 0.6021, 0.5037), "Ruin_Wall_Brick_E_Blueprint2_5", _folder)
if a: placed += 1
else: skipped += 1

# Construction: Ruin_Wall_Brick_F_Blueprint_5
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Stone
#   Volume: EMorSimpleShape::OrientedBox, BoxExtent: (15.3, 10.3, 17.8)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (1839.3585, 4002.662, 870.3536), (0.0, 0.0, -0.0), (0.3066, 0.2050, 0.3552), "Ruin_Wall_Brick_F_Blueprint_5", _folder)
if a: placed += 1
else: skipped += 1

# Construction: Suburbs_Wall_Thin_05x3m_A4
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Stone
#   Volume: EMorSimpleShape::OrientedBox, BoxExtent: (25.0, 150.0, 26.1)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (2708.5093, 1600.0, 925.63715), (0.0, 0.0, -0.0), (0.5000, 3.0000, 0.5226), "Suburbs_Wall_Thin_05x3m_A4", _folder)
if a: placed += 1
else: skipped += 1

# Construction: Suburbs_Wall_Thin_05x3m_A5
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Stone
#   Volume: EMorSimpleShape::OrientedBox, BoxExtent: (25.0, 150.0, 26.1)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (2708.5093, 1950.0, 925.63715), (0.0, 0.0, -0.0), (0.5000, 3.0000, 0.5226), "Suburbs_Wall_Thin_05x3m_A5", _folder)
if a: placed += 1
else: skipped += 1

# Construction: Suburbs_Wall_Thin_1x3m_A2
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Advanced
#   Volume: EMorSimpleShape::Empty, BoxExtent: (100.0, 100.0, 100.0)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (1387.6355, 1750.0, 900.0), (-0.0, -90.0001164887758, -0.0), (2.0000, 2.0000, 2.0000), "Suburbs_Wall_Thin_1x3m_A2", _folder)
if a: placed += 1
else: skipped += 1

# Construction: Suburbs_Wall_Thin_1x3m_A3
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Advanced
#   Volume: EMorSimpleShape::Empty, BoxExtent: (100.0, 100.0, 100.0)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (1387.6355, 2050.0, 900.0), (-0.0, -90.0001164887758, -0.0), (2.0000, 2.0000, 2.0000), "Suburbs_Wall_Thin_1x3m_A3", _folder)
if a: placed += 1
else: skipped += 1

# ======================================================================
# PHASE 3: Breakables + DecoVolumes
# ======================================================================
unreal.log(f"[{BUBBLE_NAME}] Phase 3: Placing breakables and deco volumes...")

_folder = "Reconstruction/BD_BB_Sandbox_DwarfHall_Voxels/Breakables"

# Breakable Batch 0: BP_DM_Rubble_Masonry_large_B_Breakable (3 instances)
#   BP Class: /Game/LevelDesign/Deco/Rubble/BP_DM_Rubble_Masonry_large_B_Breakable
_brk_mesh = "/Game/Art/Assets/Kits/Deco/Rubble/Rubble_Masonry_large_B"
_brk_mats = ['/Game/Art/Assets/Kits/Deco_Architecture/Ruins/Materials/Ruin_Wall_Thick/MI_Ruin_Wall_IndStone3', '/Game/Art/Assets/Kits/Deco_Architecture/Ruins/Materials/Ruin_Wall_Thick/MI_Ruin_Wall_IndStone2', '/Game/Art/Assets/Kits/Deco/Rubble/Materials/Rubble_Masonry_Pile/MI_Rubble_Masonry_Pile_06_Inst']
a = spawn_static_mesh(_brk_mesh, _brk_mats, (4550.0, 5200.0, 900.0), (0.0, 0.0, -0.0), (1.0, 1.0, 1.0), "BP_DM_Rubble_Masonry_large_B_Breakable_2", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_brk_mesh, _brk_mats, (3479.3726, 2550.0, 905.373), (0.0, 0.0, -0.0), (1.0, 1.0, 1.0), "BP_DM_Rubble_Masonry_large_B_Breakable2_5", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_brk_mesh, _brk_mats, (4253.191, 5332.5205, 909.4499), (0.0, 0.0, -0.0), (1.0, 1.0, 1.0), "BP_DM_Rubble_Masonry_large_B_Breakable4_14", _folder)
if a: placed += 1
else: skipped += 1

# Breakable Batch 1: BP_DM_Rubble_Masonry_large_C_Breakable (2 instances)
#   BP Class: /Game/LevelDesign/Deco/Rubble/BP_DM_Rubble_Masonry_large_C_Breakable
_brk_mesh = "/Game/Art/Assets/Kits/Deco/Rubble/Rubble_Masonry_large_C"
_brk_mats = ['/Game/Art/Assets/Kits/Deco_Architecture/Ruins/Materials/Ruin_Wall_Thick/MI_Ruin_Wall_IndStone3', '/Game/Art/Assets/Kits/Deco_Architecture/Ruins/Materials/Ruin_Wall_Thick/MI_Ruin_Wall_IndStone2', '/Game/Art/Assets/Kits/Deco_Architecture/Ruins/Materials/Ruin_Wall_Thick/MI_Ruin_Wall_IndStone1', '/Game/Art/Assets/Kits/Deco/Rubble/Materials/Rubble_Masonry_Pile/MI_Rubble_Masonry_Pile_06_Inst']
a = spawn_static_mesh(_brk_mesh, _brk_mats, (2050.0, 2601.3835, 850.0), (0.0, 0.0, -0.0), (1.0, 1.0, 1.0), "BP_DM_Rubble_Masonry_large_C_Breakable_2", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_brk_mesh, _brk_mats, (2763.0515, 1850.1976, 900.14703), (0.0, -115.10557143267211, 0.0), (1.0, 1.0, 1.0), "BP_DM_Rubble_Masonry_large_C_Breakable2", _folder)
if a: placed += 1
else: skipped += 1

# Breakable Batch 2: BP_DM_Rubble_Masonry_large_F_Breakable (3 instances)
#   BP Class: /Game/LevelDesign/Deco/Rubble/BP_DM_Rubble_Masonry_large_F_Breakable
_brk_mesh = "/Game/Art/Assets/Kits/Deco/Rubble/Rubble_Masonry_large_F"
_brk_mats = ['/Game/Art/Assets/Kits/Deco_Architecture/Ruins/Materials/Ruin_Wall_Thick/MI_Ruin_Wall_IndStone1', '/Game/Art/Assets/Kits/Deco_Architecture/Ruins/Materials/Ruin_Wall_Thick/MI_Ruin_Wall_IndStone3', '/Game/Art/Assets/Kits/Deco_Architecture/Ruins/Materials/Ruin_Wall_Thick/MI_Ruin_Wall_IndStone2', '/Game/Art/Assets/Kits/Deco/Rubble/Materials/Rubble_Masonry_Pile/MI_Rubble_Masonry_Pile_06_Inst']
a = spawn_static_mesh(_brk_mesh, _brk_mats, (5100.0, 4250.0, 900.0), (0.0, -90.00005166594045, 0.0), (1.0, 1.0, 1.0), "BP_DM_Rubble_Masonry_large_F_Breakable2_5", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_brk_mesh, _brk_mats, (2238.681, 2613.6836, 850.0), (0.0, 0.0, -0.0), (1.0, 1.0, 1.0), "BP_DM_Rubble_Masonry_large_F_Breakable3_2", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_brk_mesh, _brk_mats, (2009.5688, 2596.7537, 883.9726), (0.0, 0.0, -0.0), (1.0, 1.0, 1.0), "BP_DM_Rubble_Masonry_large_F_Breakable6_6", _folder)
if a: placed += 1
else: skipped += 1

# Breakable Batch 3: BP_DM_Rubble_Masonry_Pile_A_Breakable (1 instances)
#   BP Class: /Game/LevelDesign/Deco/Rubble/BP_DM_Rubble_Masonry_Pile_A_Breakable
_brk_mesh = "/Game/Art/Assets/Kits/Deco/Rubble/Rubble_Masonry_Pile_A"
_brk_mats = ['/Game/Art/Assets/Kits/Deco/Rubble/Materials/Rubble_Masonry_Pile/MI_Rubble_Masonry_Pile_Atlas_Inst_A', '/Game/Art/Assets/Kits/Deco/Rubble/Materials/Rubble_Masonry_Pile/MI_Rubble_Masonry_Pile_Atlas_Inst_A']
a = spawn_static_mesh(_brk_mesh, _brk_mats, (337.24536, 5882.1074, 832.5914), (0.0, 0.0, -0.0), (1.0, 1.0, 1.0), "BP_DM_Rubble_Masonry_Pile_A_Breakable_2", _folder)
if a: placed += 1
else: skipped += 1

# Breakable Batch 4: BP_DM_Rubble_Masonry_Pile_B_Breakable (2 instances)
#   BP Class: /Game/LevelDesign/Deco/Rubble/BP_DM_Rubble_Masonry_Pile_B_Breakable
_brk_mesh = "/Game/Art/Assets/Kits/Deco/Rubble/Rubble_Masonry_Pile_B"
_brk_mats = ['/Game/Art/Assets/Kits/Deco/Rubble/Materials/Rubble_Masonry_Pile/MI_Rubble_Masonry_Pile_Atlas_Inst_A', '/Game/Art/Assets/Kits/Deco/Rubble/Materials/Rubble_Masonry_Pile/MI_Rubble_Masonry_Pile_Atlas_Inst_B']
a = spawn_static_mesh(_brk_mesh, _brk_mats, (2750.0, 2056.3787, 900.0), (0.0, 90.00001925454748, -0.0), (1.0, 1.0, 1.0), "BP_DM_Rubble_Masonry_Pile_B_Breakable_2", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_brk_mesh, _brk_mats, (1489.8716, 2050.0, 850.00006), (0.0, -90.00005166594045, 0.0), (1.0, 1.0, 1.0), "BP_DM_Rubble_Masonry_Pile_B_Breakable2_5", _folder)
if a: placed += 1
else: skipped += 1

# Breakable Batch 5: BP_DM_Rubble_Masonry_Pile_C_Breakable (2 instances)
#   BP Class: /Game/LevelDesign/Deco/Rubble/BP_DM_Rubble_Masonry_Pile_C_Breakable
_brk_mesh = "/Game/Art/Assets/Kits/Deco/Rubble/Rubble_Masonry_Pile_C"
_brk_mats = ['/Game/Art/Assets/Kits/Deco/Rubble/Materials/Rubble_Masonry_Pile/MI_Rubble_Masonry_Pile_Atlas_Inst_B', '/Game/Art/Assets/Kits/Deco/Rubble/Materials/Rubble_Masonry_Pile/MI_Rubble_Masonry_Pile_Atlas_Inst_A']
a = spawn_static_mesh(_brk_mesh, _brk_mats, (1623.6322, 5999.78, 840.6283), (0.0, -127.323630573123, 0.0), (1.0, 1.0, 1.0), "BP_DM_Rubble_Masonry_Pile_C_Breakable3_2", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_brk_mesh, _brk_mats, (2250.0, 2050.0, 850.0), (0.0, 35.00006033507422, -0.0), (1.0, 1.0, 1.0), "BP_DM_Rubble_Masonry_Pile_C_Breakable4_2", _folder)
if a: placed += 1
else: skipped += 1

# Breakable Batch 6: BP_DM_Rubble_Masonry_Pile_D_Breakable (4 instances)
#   BP Class: /Game/LevelDesign/Deco/Rubble/BP_DM_Rubble_Masonry_Pile_D_Breakable
_brk_mesh = "/Game/Art/Assets/Kits/Deco/Rubble/Rubble_Masonry_Pile_D"
_brk_mats = ['/Game/Art/Assets/Kits/Deco/Rubble/Materials/Rubble_Masonry_Pile/MI_Rubble_Masonry_Pile_Atlas_Inst_A', '/Game/Art/Assets/Kits/Deco/Rubble/Materials/Rubble_Masonry_Pile/MI_Rubble_Masonry_Pile_Atlas_Inst_B']
a = spawn_static_mesh(_brk_mesh, _brk_mats, (4250.0, 5200.0, 900.0), (0.0, 0.0, -0.0), (1.0, 1.0, 1.0), "BP_DM_Rubble_Masonry_Pile_D_Breakable2_2", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_brk_mesh, _brk_mats, (1549.0834, 1537.473, 850.0), (0.0, 83.66241259518483, -0.0), (1.0, 1.0, 1.0), "BP_DM_Rubble_Masonry_Pile_D_Breakable5", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_brk_mesh, _brk_mats, (3950.0, 3250.0, 900.0), (0.0, 45.0000434743028, -0.0), (1.0, 1.0, 1.0), "BP_DM_Rubble_Masonry_Pile_D_Breakable6_5", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_brk_mesh, _brk_mats, (2550.0, 1650.0, 900.0), (0.0, -90.0001164887758, 0.0), (1.0, 1.0, 1.0), "BP_DM_Rubble_Masonry_Pile_D_Breakable7_8", _folder)
if a: placed += 1
else: skipped += 1

# Breakable Batch 7: BP_DM_Rubble_Masonry_Pile_E_Breakable (10 instances)
#   BP Class: /Game/LevelDesign/Deco/Rubble/BP_DM_Rubble_Masonry_Pile_E_Breakable
_brk_mesh = "/Game/Art/Assets/Kits/Deco/Rubble/Rubble_Masonry_Pile_E_Optimized"
_brk_mats = ['/Game/Art/Assets/Kits/Deco/Rubble/Materials/Rubble_Masonry_Pile/MI_Rubble_Masonry_Pile_Atlas_Inst_A', '/Game/Art/Assets/Kits/Deco/Rubble/Materials/Rubble_Masonry_Pile/MI_Rubble_Masonry_Pile_Atlas_Inst_B']
a = spawn_static_mesh(_brk_mesh, _brk_mats, (4200.0, 3800.0, 900.0), (0.0, 0.0, -0.0), (1.0, 1.0, 1.0), "BP_DM_Rubble_Masonry_Pile_E_Breakable_5", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_brk_mesh, _brk_mats, (1870.4073, 1214.3458, 887.5039), (0.0, 0.0, -0.0), (1.0, 1.0, 1.0), "BP_DM_Rubble_Masonry_Pile_E_Breakable10_2", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_brk_mesh, _brk_mats, (3100.0, 1900.0, 850.0), (0.0, 0.0, -0.0), (1.0, 1.0, 1.0), "BP_DM_Rubble_Masonry_Pile_E_Breakable12_11", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_brk_mesh, _brk_mats, (4350.0, 5200.0, 900.0), (0.0, 0.0, -0.0), (1.0, 1.0, 1.0), "BP_DM_Rubble_Masonry_Pile_E_Breakable3_5", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_brk_mesh, _brk_mats, (3350.0, 4850.0, 850.0), (0.0, 0.0, -0.0), (1.0, 1.0, 1.0), "BP_DM_Rubble_Masonry_Pile_E_Breakable4_14", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_brk_mesh, _brk_mats, (2700.0, 1650.0, 900.0), (0.0, -90.00005166594045, 0.0), (1.0, 1.0, 1.0), "BP_DM_Rubble_Masonry_Pile_E_Breakable5_2", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_brk_mesh, _brk_mats, (3250.0, 2950.0, 850.0), (0.0, 0.0, -0.0), (1.0, 1.0, 1.0), "BP_DM_Rubble_Masonry_Pile_E_Breakable6_8", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_brk_mesh, _brk_mats, (1182.8927, 4698.3687, 850.0), (0.0, -25.000089077421823, 0.0), (1.0, 1.0, 1.0), "BP_DM_Rubble_Masonry_Pile_E_Breakable7_17", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_brk_mesh, _brk_mats, (1900.0, 1100.0, 850.0), (0.0, 0.0, -0.0), (1.0, 1.0, 1.0), "BP_DM_Rubble_Masonry_Pile_E_Breakable8_14", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_brk_mesh, _brk_mats, (1250.0, 5100.0, 850.0), (0.0, 0.0, -0.0), (1.0, 1.0, 1.0), "BP_DM_Rubble_Masonry_Pile_E_Breakable9_20", _folder)
if a: placed += 1
else: skipped += 1

# Breakable Batch 8: BP_DM_Rubble_Masonry_Pile_F_Breakable (28 instances)
#   BP Class: /Game/LevelDesign/Deco/Rubble/BP_DM_Rubble_Masonry_Pile_F_Breakable
_brk_mesh = "/Game/Art/Assets/Kits/Deco/Rubble/Rubble_Masonry_Pile_F_Optimized"
_brk_mats = ['/Game/Art/Assets/Kits/Deco/Rubble/Materials/Rubble_Masonry_Pile/MI_Rubble_Masonry_Pile_Atlas_Inst_B', '/Game/Art/Assets/Kits/Deco/Rubble/Materials/Rubble_Masonry_Pile/MI_Rubble_Masonry_Pile_Atlas_Inst_A']
a = spawn_static_mesh(_brk_mesh, _brk_mats, (1650.0, 5450.0, 850.0), (0.0, 95.00002760264337, -0.0), (1.0, 1.0, 1.0), "BP_DM_Rubble_Masonry_Pile_F_Breakable10", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_brk_mesh, _brk_mats, (4906.2456, 4513.6875, 906.26953), (0.0, -107.67010835262299, 0.0), (1.0, 1.0, 1.0), "BP_DM_Rubble_Masonry_Pile_F_Breakable11_6", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_brk_mesh, _brk_mats, (4850.0, 2100.0, 900.0), (0.0, 0.0, -0.0), (1.0, 1.0, 1.0), "BP_DM_Rubble_Masonry_Pile_F_Breakable12_2", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_brk_mesh, _brk_mats, (4900.0, 1400.0, 900.0), (0.0, 0.0, -0.0), (1.0, 1.0, 1.0), "BP_DM_Rubble_Masonry_Pile_F_Breakable13_5", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_brk_mesh, _brk_mats, (4650.0, 3150.0, 900.0), (0.0, 0.0, -0.0), (1.0, 1.0, 1.0), "BP_DM_Rubble_Masonry_Pile_F_Breakable14_8", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_brk_mesh, _brk_mats, (5100.0, 2900.0, 800.0), (0.0, -90.00005166594045, 0.0), (1.0, 1.0, 1.0), "BP_DM_Rubble_Masonry_Pile_F_Breakable15_11", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_brk_mesh, _brk_mats, (3250.0, 2000.0, 850.0), (0.0, 0.0, -0.0), (1.0, 1.0, 1.0), "BP_DM_Rubble_Masonry_Pile_F_Breakable16_14", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_brk_mesh, _brk_mats, (3150.1902, 1645.6422, 850.0), (0.0, 94.99998926081646, -0.0), (1.0, 1.0, 1.0), "BP_DM_Rubble_Masonry_Pile_F_Breakable17_17", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_brk_mesh, _brk_mats, (3633.6519, 3175.8218, 900.0), (0.0, -105.00007707772225, 0.0), (1.0, 1.0, 1.0), "BP_DM_Rubble_Masonry_Pile_F_Breakable18", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_brk_mesh, _brk_mats, (2450.0, 1850.0, 850.0), (0.0, 0.0, -0.0), (1.0, 1.0, 1.0), "BP_DM_Rubble_Masonry_Pile_F_Breakable19_21", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_brk_mesh, _brk_mats, (4649.2524, 5221.9746, 906.3343), (0.0, 0.0, -0.0), (1.0, 1.0, 1.0), "BP_DM_Rubble_Masonry_Pile_F_Breakable2_9", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_brk_mesh, _brk_mats, (4050.0, 4700.0, 900.0), (0.0, 0.0, -0.0), (1.0, 1.0, 1.0), "BP_DM_Rubble_Masonry_Pile_F_Breakable20_24", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_brk_mesh, _brk_mats, (3069.588, 3892.098, 850.0), (0.0, -160.00005976545398, 0.0), (1.0, 1.0, 1.0), "BP_DM_Rubble_Masonry_Pile_F_Breakable21", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_brk_mesh, _brk_mats, (1865.0878, 3400.488, 800.0), (0.0, -160.00005976545398, 0.0), (1.0, 1.0, 1.0), "BP_DM_Rubble_Masonry_Pile_F_Breakable22", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_brk_mesh, _brk_mats, (3040.4902, 5442.7646, 850.0), (0.0, -160.00005976545398, 0.0), (1.0, 1.0, 1.0), "BP_DM_Rubble_Masonry_Pile_F_Breakable23", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_brk_mesh, _brk_mats, (3288.5413, 4418.869, 850.0), (0.0, 99.99988498550958, -0.0), (1.0, 1.0, 1.0), "BP_DM_Rubble_Masonry_Pile_F_Breakable24", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_brk_mesh, _brk_mats, (3291.3833, 5037.004, 850.0), (0.0, 109.99985128056142, -0.0), (1.0, 1.0, 1.0), "BP_DM_Rubble_Masonry_Pile_F_Breakable25", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_brk_mesh, _brk_mats, (2283.6318, 3712.4524, 850.0), (0.0, -160.00005976545398, 0.0), (1.0, 1.0, 1.0), "BP_DM_Rubble_Masonry_Pile_F_Breakable26", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_brk_mesh, _brk_mats, (2301.3464, 5415.4556, 850.0), (0.0, -160.00005976545398, 0.0), (1.0, 1.0, 1.0), "BP_DM_Rubble_Masonry_Pile_F_Breakable27", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_brk_mesh, _brk_mats, (1453.0168, 5389.546, 850.0), (0.0, -130.00011171588335, 0.0), (1.0, 1.0, 1.0), "BP_DM_Rubble_Masonry_Pile_F_Breakable28", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_brk_mesh, _brk_mats, (1050.0, 4900.0, 850.0), (0.0, -25.000061959545324, 0.0), (1.0, 1.0, 1.0), "BP_DM_Rubble_Masonry_Pile_F_Breakable29_48", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_brk_mesh, _brk_mats, (2250.0, 2600.0, 850.0), (0.0, 0.0, -0.0), (1.0, 1.0, 1.0), "BP_DM_Rubble_Masonry_Pile_F_Breakable3_5", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_brk_mesh, _brk_mats, (2115.088, 2950.488, 800.0), (0.0, 84.999812013364, -0.0), (1.0, 1.0, 1.0), "BP_DM_Rubble_Masonry_Pile_F_Breakable30", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_brk_mesh, _brk_mats, (1050.0, 4000.0, 850.0), (0.0, 0.0, -0.0), (1.0, 1.0, 1.0), "BP_DM_Rubble_Masonry_Pile_F_Breakable4_38", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_brk_mesh, _brk_mats, (2763.1394, 1860.819, 850.0), (0.0, 0.0, -0.0), (1.0, 1.0, 1.0), "BP_DM_Rubble_Masonry_Pile_F_Breakable5_5", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_brk_mesh, _brk_mats, (1850.0, 2585.378, 850.0), (0.0, 0.0, -0.0), (1.0, 1.0, 1.0), "BP_DM_Rubble_Masonry_Pile_F_Breakable6_8", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_brk_mesh, _brk_mats, (2300.0, 1271.4486, 850.0), (0.0, 90.00002735739477, -0.0), (1.0, 1.0, 1.0), "BP_DM_Rubble_Masonry_Pile_F_Breakable7_11", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_brk_mesh, _brk_mats, (844.55383, 4800.97, 850.0), (0.0, -65.00012172744646, 0.0), (1.0, 1.0, 1.0), "BP_DM_Rubble_Masonry_Pile_F_Breakable8_41", _folder)
if a: placed += 1
else: skipped += 1

# Breakable Batch 9: BP_DM_Rubble_Masonry_Pile_H_Breakable (13 instances)
#   BP Class: /Game/LevelDesign/Deco/Rubble/BP_DM_Rubble_Masonry_Pile_H_Breakable
_brk_mesh = "/Game/Art/Assets/Kits/Deco/Rubble/Rubble_Masonry_Pile_H_Optimized"
_brk_mats = ['/Game/Art/Assets/Kits/Deco/Rubble/Materials/Rubble_Masonry_Pile/MI_Rubble_Masonry_Pile_Atlas_Inst_B', '/Game/Art/Assets/Kits/Deco/Rubble/Materials/Rubble_Masonry_Pile/MI_Rubble_Masonry_Pile_Atlas_Inst_A']
a = spawn_static_mesh(_brk_mesh, _brk_mats, (2791.4202, 2007.1882, 850.0001), (0.0, -41.40023989064483, 0.0), (1.0, 1.0, 1.0), "BP_DM_Rubble_Masonry_Pile_H_Breakable11", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_brk_mesh, _brk_mats, (2050.0, 2650.0, 850.0), (0.0, 0.0, -0.0), (1.0, 1.0, 1.0), "BP_DM_Rubble_Masonry_Pile_H_Breakable13_2", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_brk_mesh, _brk_mats, (1000.0, 4350.0, 850.0), (0.0, 0.0, -0.0), (1.0, 1.0, 1.0), "BP_DM_Rubble_Masonry_Pile_H_Breakable14_29", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_brk_mesh, _brk_mats, (3500.0, 1150.0, 850.0), (0.0, 0.0, -0.0), (1.0, 1.0, 1.0), "BP_DM_Rubble_Masonry_Pile_H_Breakable15_11", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_brk_mesh, _brk_mats, (1500.0, 3300.0, 800.0), (0.0, -165.00006780117724, 0.0), (1.0, 1.0, 1.0), "BP_DM_Rubble_Masonry_Pile_H_Breakable16", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_brk_mesh, _brk_mats, (4600.0, 1400.0, 900.0), (0.0, 115.0000760444433, -0.0), (1.0, 1.0, 1.0), "BP_DM_Rubble_Masonry_Pile_H_Breakable17_17", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_brk_mesh, _brk_mats, (4300.0, 5250.0, 900.0), (0.0, 0.0, -0.0), (1.0, 1.0, 1.0), "BP_DM_Rubble_Masonry_Pile_H_Breakable3_5", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_brk_mesh, _brk_mats, (3250.0, 3950.0, 850.0), (0.0, 0.0, -0.0), (1.0, 1.0, 1.0), "BP_DM_Rubble_Masonry_Pile_H_Breakable4_23", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_brk_mesh, _brk_mats, (4200.0, 1200.0, 900.0), (0.0, 0.0, -0.0), (1.0, 1.0, 1.0), "BP_DM_Rubble_Masonry_Pile_H_Breakable5_2", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_brk_mesh, _brk_mats, (4600.0, 3950.0, 900.0), (0.0, 0.0, -0.0), (1.0, 1.0, 1.0), "BP_DM_Rubble_Masonry_Pile_H_Breakable6_20", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_brk_mesh, _brk_mats, (5000.0, 1750.0, 900.0), (0.0, 0.0, -0.0), (1.0, 1.0, 1.0), "BP_DM_Rubble_Masonry_Pile_H_Breakable7_5", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_brk_mesh, _brk_mats, (1519.7509, 1579.6581, 856.33435), (0.0, 0.0, -0.0), (1.0, 1.0, 1.0), "BP_DM_Rubble_Masonry_Pile_H_Breakable8_5", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_brk_mesh, _brk_mats, (900.0, 4100.0, 850.0), (0.0, 0.0, -0.0), (1.0, 1.0, 1.0), "BP_DM_Rubble_Masonry_Pile_H_Breakable9_26", _folder)
if a: placed += 1
else: skipped += 1

# Breakable Batch 10: BP_DM_Rubble_Masonry_Pile_I_Breakable (4 instances)
#   BP Class: /Game/LevelDesign/Deco/Rubble/BP_DM_Rubble_Masonry_Pile_I_Breakable
_brk_mesh = "/Game/Art/Assets/Kits/Deco/Rubble/Rubble_Masonry_Pile_I"
_brk_mats = ['/Game/Art/Assets/Kits/Deco/Rubble/Materials/Rubble_Masonry_Pile/MI_Rubble_Masonry_Pile_Atlas_Inst_B', '/Game/Art/Assets/Kits/Deco/Rubble/Materials/Rubble_Masonry_Pile/MI_Rubble_Masonry_Pile_Atlas_Inst_A']
a = spawn_static_mesh(_brk_mesh, _brk_mats, (4950.0, 1950.0, 900.0), (0.0, 89.99997063746636, -0.0), (1.0, 1.0, 1.0), "BP_DM_Rubble_Masonry_Pile_I_Breakable2_2", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_brk_mesh, _brk_mats, (3800.0, 4300.0, 900.0), (0.0, -89.99984099200987, 0.0), (1.0, 1.0, 1.0), "BP_DM_Rubble_Masonry_Pile_I_Breakable3", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_brk_mesh, _brk_mats, (5100.0, 3150.0, 800.0), (0.0, -90.00005166594045, 0.0), (1.0, 1.0, 1.0), "BP_DM_Rubble_Masonry_Pile_I_Breakable4_8", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_brk_mesh, _brk_mats, (3950.0, 4400.0, 900.0), (0.0, -90.00002735739477, 0.0), (1.0, 1.0, 1.0), "BP_DM_Rubble_Masonry_Pile_I_Breakable5_11", _folder)
if a: placed += 1
else: skipped += 1

# Breakable Batch 11: BP_Ruin_Column_Large_A_Base_2_Breakable (4 instances)
#   BP Class: /Game/LevelDesign/Deco_Architecture/Ruins/BP_Ruin_Column_Large_A_Base_2_Breakable
_brk_mesh = "/Game/Art/Assets/Kits/Architecture/Suburbs/Suburbs_Column_Large_A_A_Base_Ruined"
_brk_mats = ['/Game/Art/Assets/Kits/Architecture/Suburbs/Materials/Suburbs_Column_Large_A_Ruined/MI_Suburbs_Column_Large_A_Base_Ruined']
a = spawn_static_mesh(_brk_mesh, _brk_mats, (3950.0, 1200.0, 900.0), (0.0, -45.000056798727684, 0.0), (1.0, 1.0, 1.0), "BP_Ruin_Column_Large_A_Base_2_Breakable_2", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_brk_mesh, _brk_mats, (4950.0, 2400.0, 900.0), (0.0, 135.0000447640938, -0.0), (1.0, 1.0, 1.0), "BP_Ruin_Column_Large_A_Base_2_Breakable2", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_brk_mesh, _brk_mats, (1350.0, 4000.0, 900.0), (0.0, 45.00008324390098, -0.0), (1.0, 1.0, 1.0), "BP_Ruin_Column_Large_A_Base_2_Breakable3_6", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_brk_mesh, _brk_mats, (1550.0, 3800.0, 900.0), (0.0, -135.00001466939858, 0.0), (1.0, 1.0, 1.0), "BP_Ruin_Column_Large_A_Base_2_Breakable4_9", _folder)
if a: placed += 1
else: skipped += 1

# Breakable Batch 12: BP_Ruin_Column_Large_A_Capital_1_Breakable (2 instances)
#   BP Class: /Game/LevelDesign/Deco_Architecture/Ruins/BP_Ruin_Column_Large_A_Capital_1_Breakable
_brk_mesh = "/Game/Art/Assets/Kits/Architecture/Suburbs/Suburbs_Column_Large_A_B_Capitol_Ruined"
_brk_mats = ['/Game/Art/Assets/Kits/Architecture/Suburbs/Materials/Suburbs_Column_Large_A_Ruined/MI_Suburbs_Column_Large_A_Capitol_Ruined']
a = spawn_static_mesh(_brk_mesh, _brk_mats, (3150.0, 4250.0, 850.0), (-29.999905941598193, -105.00008132794179, 1.1471620356608803e-06), (1.0, 1.0, 1.0), "BP_Ruin_Column_Large_A_Capital_1_Breakable_5", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_brk_mesh, _brk_mats, (1550.0, 4000.0, 1700.0), (0.0, 45.000056798727684, -0.0), (1.0, 1.0, 1.0), "BP_Ruin_Column_Large_A_Capital_1_Breakable2_8", _folder)
if a: placed += 1
else: skipped += 1

# Breakable Batch 13: BP_Ruin_Column_Large_A_Capital_2_Breakable (4 instances)
#   BP Class: /Game/LevelDesign/Deco_Architecture/Ruins/BP_Ruin_Column_Large_A_Capital_2_Breakable
_brk_mesh = "/Game/Art/Assets/Kits/Architecture/Suburbs/Suburbs_Column_Large_A_A_Capitol_Ruined"
_brk_mats = ['/Game/Art/Assets/Kits/Architecture/Suburbs/Materials/Suburbs_Column_Large_A_Ruined/MI_Suburbs_Column_Large_A_Capitol_Ruined']
a = spawn_static_mesh(_brk_mesh, _brk_mats, (5121.9824, 2780.3818, 943.969), (28.87893169187197, -146.4993703487563, -72.80517560207379), (1.0, 1.0, 1.0), "BP_Ruin_Column_Large_A_Capital_2_Breakable_2", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_brk_mesh, _brk_mats, (2850.0, 1900.0, 1000.0), (61.09534973601862, -60.96761992474439, -57.62334375381931), (1.0, 1.0, 1.0), "BP_Ruin_Column_Large_A_Capital_2_Breakable2_5", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_brk_mesh, _brk_mats, (1150.0, 4250.0, 850.0), (60.00000001588208, 0.0, -0.0), (1.0, 1.0, 1.0), "BP_Ruin_Column_Large_A_Capital_2_Breakable3_8", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_brk_mesh, _brk_mats, (2200.0, 5000.0, 950.0), (78.30575857610373, 60.49062261949625, 21.227308358227756), (1.0, 1.0, 1.0), "BP_Ruin_Column_Large_A_Capital_2_Breakable4_11", _folder)
if a: placed += 1
else: skipped += 1

# Breakable Batch 14: BP_Ruin_Column_Large_A_Capital_4_Breakable (2 instances)
#   BP Class: /Game/LevelDesign/Deco_Architecture/Ruins/BP_Ruin_Column_Large_A_Capital_4_Breakable
_brk_mesh = "/Game/Art/Assets/Kits/Architecture/Suburbs/Suburbs_Column_Large_A_C_Capitol_Ruined"
_brk_mats = ['/Game/Art/Assets/Kits/Architecture/Suburbs/Materials/Suburbs_Column_Large_A_Ruined/MI_Suburbs_Column_Large_A_Shaft_Ruined', '/Game/Art/Assets/Kits/Architecture/Suburbs/Materials/Suburbs_Column_Large_A_Ruined/MI_Suburbs_Column_Large_A_Capitol_Ruined']
a = spawn_static_mesh(_brk_mesh, _brk_mats, (3096.4902, 5101.4624, 850.0), (0.0, -40.00018323255635, 0.0), (1.0, 1.0, 1.0), "BP_Ruin_Column_Large_A_Capital_4_Breakable_5", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_brk_mesh, _brk_mats, (1800.0, 2850.0, 950.0), (-69.99901973839171, -144.9990369488687, 89.9996454276422), (1.0, 1.0, 1.0), "BP_Ruin_Column_Large_A_Capital_4_Breakable2_8", _folder)
if a: placed += 1
else: skipped += 1

# Breakable Batch 15: BP_Ruin_Column_Large_A_Shaft_2_Breakable (4 instances)
#   BP Class: /Game/LevelDesign/Deco_Architecture/Ruins/BP_Ruin_Column_Large_A_Shaft_2_Breakable
_brk_mesh = "/Game/Art/Assets/Kits/Architecture/Suburbs/Suburbs_Column_Large_A_A_Shaft_Ruined"
_brk_mats = ['/Game/Art/Assets/Kits/Architecture/Suburbs/Materials/Suburbs_Column_Large_A_Ruined/MI_Suburbs_Column_Large_A_Shaft_Ruined']
a = spawn_static_mesh(_brk_mesh, _brk_mats, (3450.0, 1750.0, 900.0), (-7.599881787205144e-07, 64.99994765736304, 90.00002418784254), (1.0, 1.0, 1.0), "BP_Ruin_Column_Large_A_Shaft_2_Breakable_2", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_brk_mesh, _brk_mats, (1050.0, 4650.0, 900.0), (64.99999715647601, -65.00017991988028, 1.7080258749068567e-05), (1.0, 1.0, 1.0), "BP_Ruin_Column_Large_A_Shaft_2_Breakable2_5", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_brk_mesh, _brk_mats, (2550.0, 5200.0, 1300.0), (0.0, -89.99975996369572, 0.0), (1.0, 1.0, 1.0), "BP_Ruin_Column_Large_A_Shaft_2_Breakable3_8", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_brk_mesh, _brk_mats, (1700.0, 3258.5193, 914.7058), (0.0, 0.0, 105.00024249443403), (1.0, 1.0, 1.0), "BP_Ruin_Column_Large_A_Shaft_2_Breakable4_11", _folder)
if a: placed += 1
else: skipped += 1

# Breakable Batch 16: BP_Ruin_Column_Large_A_Shaft_3_Breakable (3 instances)
#   BP Class: /Game/LevelDesign/Deco_Architecture/Ruins/BP_Ruin_Column_Large_A_Shaft_3_Breakable
_brk_mesh = "/Game/Art/Assets/Kits/Architecture/Suburbs/Suburbs_Column_Large_A_B_Shaft_Ruined"
_brk_mats = ['/Game/Art/Assets/Kits/Architecture/Suburbs/Materials/Suburbs_Column_Large_A_Ruined/MI_Suburbs_Column_Large_A_Shaft_Ruined']
a = spawn_static_mesh(_brk_mesh, _brk_mats, (1119.4998, 4562.423, 850.0), (0.0, 74.99988068433873, -0.0), (1.0, 1.0, 1.0), "BP_Ruin_Column_Large_A_Shaft_3_Breakable_2", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_brk_mesh, _brk_mats, (2550.0, 4000.0, 1300.0), (0.0, -179.9999590188648, 0.0), (1.0, 1.0, 1.0), "BP_Ruin_Column_Large_A_Shaft_3_Breakable2_5", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_brk_mesh, _brk_mats, (1691.2856, 3249.6196, 900.0), (90.0, 0.0, -94.9992642822034), (1.0, 1.0, 1.0), "BP_Ruin_Column_Large_A_Shaft_3_Breakable3_8", _folder)
if a: placed += 1
else: skipped += 1

# Breakable Batch 17: BP_Ruins_Column_Single_A_A_Breakable (18 instances)
#   BP Class: /Game/LevelDesign/Deco_Architecture/Ruins/BP_Ruins_Column_Single_A_A_Breakable
_brk_mesh = "/Game/Art/Assets/Kits/Deco_Architecture/Ruins/Ruins_Column_Single_A_A"
_brk_mats = ['/Game/Art/Assets/Kits/Deco_Architecture/Ruins/Materials/Ruins_Column_Single_A/MI_Ruins_Column_Single_A_A_Inst']
a = spawn_static_mesh(_brk_mesh, _brk_mats, (4200.0, 3800.0, 950.0), (0.0, 179.99976777351753, -0.0), (1.0, 1.0, 1.0), "BP_Ruins_Column_Single_A_A_Breakable12", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_brk_mesh, _brk_mats, (4450.0, 3800.0, 950.0), (0.0, 179.99976777351753, -0.0), (1.0, 1.0, 1.0), "BP_Ruins_Column_Single_A_A_Breakable13", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_brk_mesh, _brk_mats, (4700.0, 3800.0, 950.0), (0.0, 179.99976777351753, -0.0), (1.0, 1.0, 1.0), "BP_Ruins_Column_Single_A_A_Breakable14", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_brk_mesh, _brk_mats, (4650.0, 5300.0, 950.0), (0.0, 179.99976777351753, -0.0), (1.0, 1.0, 1.0), "BP_Ruins_Column_Single_A_A_Breakable15", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_brk_mesh, _brk_mats, (4250.0, 5300.0, 950.0), (0.0, 0.0, -0.0), (1.0, 1.0, 1.0), "BP_Ruins_Column_Single_A_A_Breakable16", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_brk_mesh, _brk_mats, (4450.0, 5300.0, 950.0), (0.0, 179.99976777351753, -0.0), (1.0, 1.0, 1.0), "BP_Ruins_Column_Single_A_A_Breakable17", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_brk_mesh, _brk_mats, (5050.0, 4900.0, 950.0), (0.0, 89.99999818714215, -0.0), (1.0, 1.0, 1.0), "BP_Ruins_Column_Single_A_A_Breakable18", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_brk_mesh, _brk_mats, (5050.0, 4600.0, 950.0), (0.0, -90.00005166594045, 0.0), (1.0, 1.0, 1.0), "BP_Ruins_Column_Single_A_A_Breakable19", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_brk_mesh, _brk_mats, (1400.0, 1550.0, 950.0), (0.0, 89.99999818714215, -0.0), (1.0, 1.0, 1.0), "BP_Ruins_Column_Single_A_A_Breakable2", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_brk_mesh, _brk_mats, (3850.0, 4850.0, 950.0), (0.0, -90.00005166594045, 0.0), (1.0, 1.0, 1.0), "BP_Ruins_Column_Single_A_A_Breakable20_22", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_brk_mesh, _brk_mats, (3850.0, 4600.0, 950.0), (0.0, 89.99999818714215, -0.0), (1.0, 1.0, 1.0), "BP_Ruins_Column_Single_A_A_Breakable21", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_brk_mesh, _brk_mats, (3850.0, 4350.0, 950.0), (0.0, -90.00005166594045, 0.0), (1.0, 1.0, 1.0), "BP_Ruins_Column_Single_A_A_Breakable22", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_brk_mesh, _brk_mats, (1400.0, 1800.0, 950.0), (0.0, -89.99999818714215, 0.0), (1.0, 1.0, 1.0), "BP_Ruins_Column_Single_A_A_Breakable3", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_brk_mesh, _brk_mats, (1850.0, 2550.0, 950.0), (0.0, -0.0001525878854640202, 0.0), (1.0, 1.0, 1.0), "BP_Ruins_Column_Single_A_A_Breakable4", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_brk_mesh, _brk_mats, (2250.0, 2550.0, 950.0), (0.0, -0.0001525878854640202, 0.0), (1.0, 1.0, 1.0), "BP_Ruins_Column_Single_A_A_Breakable6", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_brk_mesh, _brk_mats, (2050.0, 2550.0, 950.0), (0.0, -179.99998633961752, -0.0), (1.0, 1.0, 1.0), "BP_Ruins_Column_Single_A_A_Breakable7", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_brk_mesh, _brk_mats, (2700.0, 2050.0, 950.0), (0.0, -90.00022020536449, 0.0), (1.0, 1.0, 1.0), "BP_Ruins_Column_Single_A_A_Breakable8", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_brk_mesh, _brk_mats, (2700.0, 1550.0, 950.0), (0.0, -90.00022020536449, 0.0), (1.0, 1.0, 1.0), "BP_Ruins_Column_Single_A_A_Breakable9", _folder)
if a: placed += 1
else: skipped += 1

# Breakable Batch 18: BP_Ruins_Column_Single_A_B_Breakable (2 instances)
#   BP Class: /Game/LevelDesign/Deco_Architecture/Ruins/BP_Ruins_Column_Single_A_B_Breakable
_brk_mesh = "/Game/Art/Assets/Kits/Deco_Architecture/Ruins/Ruins_Column_Single_A_B"
_brk_mats = ['/Game/Art/Assets/Kits/Deco_Architecture/Ruins/Materials/Ruins_Column_Single_A/MI_Ruins_Column_Single_A_B_Inst']
a = spawn_static_mesh(_brk_mesh, _brk_mats, (2700.0, 1800.0, 950.0), (0.0, 89.99999818714215, -0.0), (1.0, 1.0, 1.0), "BP_Ruins_Column_Single_A_B_Breakable_2", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_brk_mesh, _brk_mats, (5050.0, 4300.0, 1000.0), (0.0, 89.99999818714215, -0.0), (1.0, 1.0, 1.0), "BP_Ruins_Column_Single_A_B_Breakable2_5", _folder)
if a: placed += 1
else: skipped += 1

# Breakable Batch 19: BP_Ruins_Column_Single_A_C_Breakable (1 instances)
#   BP Class: /Game/LevelDesign/Deco_Architecture/Ruins/BP_Ruins_Column_Single_A_C_Breakable
_brk_mesh = "/Game/Art/Assets/Kits/Deco_Architecture/Ruins/Ruins_Column_Single_A_C"
_brk_mats = ['/Game/Art/Assets/Kits/Deco_Architecture/Ruins/Materials/Ruins_Column_Single_A/MI_Ruins_Column_Single_A_B_Inst']
a = spawn_static_mesh(_brk_mesh, _brk_mats, (3850.0, 4850.0, 1850.0), (0.0, 89.99999818714215, -0.0), (1.0, 1.0, 1.0), "BP_Ruins_Column_Single_A_C_Breakable_2", _folder)
if a: placed += 1
else: skipped += 1

# Breakable Batch 20: BP_Ruins_Column_Single_A_E (17 instances)
#   BP Class: /Game/LevelDesign/Deco_Architecture/Ruins/BP_Ruins_Column_Single_A_E
_brk_mesh = "/Game/Art/Assets/Kits/Deco_Architecture/Ruins/Ruins_Column_Single_A_E"
_brk_mats = ['/Game/Art/Assets/Kits/Deco_Architecture/Ruins/Materials/Ruins_Column_Single_A/MI_Ruins_Column_Single_A_A_Inst']
a = spawn_static_mesh(_brk_mesh, _brk_mats, (4200.0, 3800.0, 1350.0), (-2.4641258715537203e-18, -0.0004272460422088457, -179.99995901885745), (1.0, 1.0, 1.0), "BP_Ruins_Column_Single_A_E12", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_brk_mesh, _brk_mats, (4700.0, 3800.0, 1350.0), (-2.4641258715537203e-18, -0.0004272460422088457, -179.99995901885745), (1.0, 1.0, 1.0), "BP_Ruins_Column_Single_A_E16", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_brk_mesh, _brk_mats, (4700.0, 3800.0, 1350.0), (0.0, 179.99992486791828, -0.0), (1.0, 1.0, 1.0), "BP_Ruins_Column_Single_A_E17", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_brk_mesh, _brk_mats, (4650.0, 5300.0, 1350.0), (-2.4641258715537203e-18, -0.0004272460422088457, -179.99995901885745), (1.0, 1.0, 1.0), "BP_Ruins_Column_Single_A_E18", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_brk_mesh, _brk_mats, (4650.0, 5300.0, 1350.0), (0.0, 179.99992486791828, -0.0), (1.0, 1.0, 1.0), "BP_Ruins_Column_Single_A_E19", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_brk_mesh, _brk_mats, (3850.0, 4850.0, 1350.0), (8.737473446535151e-13, 89.99962059504914, -179.99995901885453), (1.0, 1.0, 1.0), "BP_Ruins_Column_Single_A_E20_42", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_brk_mesh, _brk_mats, (3850.0, 4850.0, 1350.0), (0.0, -89.9998815062137, 0.0), (1.0, 1.0, 1.0), "BP_Ruins_Column_Single_A_E21_43", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_brk_mesh, _brk_mats, (5050.0, 4600.0, 1350.0), (8.737473446535151e-13, 89.99962059504914, -179.99995901885453), (1.0, 1.0, 1.0), "BP_Ruins_Column_Single_A_E22_36", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_brk_mesh, _brk_mats, (3850.0, 4600.0, 1350.0), (-1.4489018616737198e-12, 89.99998684316093, -179.9999590188483), (1.0, 1.0, 1.0), "BP_Ruins_Column_Single_A_E23_46", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_brk_mesh, _brk_mats, (3850.0, 4350.0, 1350.0), (8.737473446535151e-13, 89.99962059504914, -179.99995901885453), (1.0, 1.0, 1.0), "BP_Ruins_Column_Single_A_E25_50", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_brk_mesh, _brk_mats, (3850.0, 4350.0, 1350.0), (0.0, -89.9998815062137, 0.0), (1.0, 1.0, 1.0), "BP_Ruins_Column_Single_A_E26", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_brk_mesh, _brk_mats, (3850.0, 4850.0, 1700.0), (-1.3660378220197669e-05, 90.00011648877661, -179.9999999999999), (1.0, 1.0, 1.0), "BP_Ruins_Column_Single_A_E27", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_brk_mesh, _brk_mats, (3850.0, 4850.0, 1650.0), (0.0, 90.00010028305118, -0.0), (1.0, 1.0, 1.0), "BP_Ruins_Column_Single_A_E28", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_brk_mesh, _brk_mats, (2250.0, 2550.0, 1350.0), (-3.9621429878797446e-20, -179.9999590188609, -179.99995901885745), (1.0, 1.0, 1.0), "BP_Ruins_Column_Single_A_E4", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_brk_mesh, _brk_mats, (2250.0, 2550.0, 1350.0), (0.0, 0.0, -0.0), (1.0, 1.0, 1.0), "BP_Ruins_Column_Single_A_E5", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_brk_mesh, _brk_mats, (2050.0, 2550.0, 1350.0), (9.995060138959777e-18, 0.0004405974591841167, -179.99995901885745), (1.0, 1.0, 1.0), "BP_Ruins_Column_Single_A_E6", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_brk_mesh, _brk_mats, (2050.0, 2550.0, 1350.0), (0.0, -179.99988388675877, 0.0), (1.0, 1.0, 1.0), "BP_Ruins_Column_Single_A_E7", _folder)
if a: placed += 1
else: skipped += 1

# --- Extra DecoVolumes (not construction blocks) ---
_folder = "Reconstruction/BD_BB_Sandbox_DwarfHall_Voxels/DecoVolumes"

# DecoVolume: BP_DM_Rubble_Masonry_large_B_Breakable_2 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (4553.1143, 5203.6094, 949.1534), (0.0, 0.0, -0.0), (2.0936, 0.9710, 1.1261), "DV_BP_DM_Rubble_Masonry_large_B_Breakable_2_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_DM_Rubble_Masonry_large_B_Breakable2_5 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (3482.4868, 2553.6094, 954.52637), (0.0, 0.0, -0.0), (2.0936, 0.9710, 1.1261), "DV_BP_DM_Rubble_Masonry_large_B_Breakable2_5_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_DM_Rubble_Masonry_large_B_Breakable4_14 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (4256.305, 5336.13, 958.6033), (0.0, 0.0, -0.0), (2.0936, 0.9710, 1.1261), "DV_BP_DM_Rubble_Masonry_large_B_Breakable4_14_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_DM_Rubble_Masonry_large_C_Breakable_2 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (2051.4658, 2604.7266, 891.71765), (0.0, 0.0, -0.0), (2.0188, 1.1666, 0.9324), "DV_BP_DM_Rubble_Masonry_large_C_Breakable_2_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_DM_Rubble_Masonry_large_C_Breakable2 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (2765.4568, 1847.4519, 941.8647), (0.0, 0.0, -0.0), (1.9129, 2.3231, 0.9324), "DV_BP_DM_Rubble_Masonry_large_C_Breakable2_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_DM_Rubble_Masonry_large_F_Breakable2_5 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (5084.54, 4265.606, 952.1968), (0.0, 0.0, -0.0), (1.4717, 2.1632, 1.1332), "DV_BP_DM_Rubble_Masonry_large_F_Breakable2_5_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_DM_Rubble_Masonry_large_F_Breakable3_2 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (2223.0752, 2598.2239, 902.1968), (0.0, 0.0, -0.0), (2.1632, 1.4717, 1.1332), "DV_BP_DM_Rubble_Masonry_large_F_Breakable3_2_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_DM_Rubble_Masonry_large_F_Breakable6_6 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (1993.9631, 2581.294, 936.1693), (0.0, 0.0, -0.0), (2.1632, 1.4717, 1.1332), "DV_BP_DM_Rubble_Masonry_large_F_Breakable6_6_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_DM_Rubble_Masonry_Mound_Pile_D_Breakable4_2 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (1065.4235, 4065.94, 868.9673), (0.0, 0.0, -0.0), (1.1287, 1.1287, 0.4337), "DV_BP_DM_Rubble_Masonry_Mound_Pile_D_Breakable4_2_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_DM_Rubble_Masonry_Mound_Pile_E_Breakable4_5 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (1082.0576, 4142.6226, 862.3909), (0.0, 0.0, -0.0), (1.0107, 1.0107, 0.3734), "DV_BP_DM_Rubble_Masonry_Mound_Pile_E_Breakable4_5_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_DM_Rubble_Masonry_Mound_Pile_F_Breakable10_9 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (2294.0962, 1645.7769, 865.7245), (0.0, 0.0, -0.0), (1.4028, 1.2372, 0.4616), "DV_BP_DM_Rubble_Masonry_Mound_Pile_F_Breakable10_9_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_DM_Rubble_Masonry_Mound_Pile_F_Breakable12_19 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (5439.834, 2453.4963, 922.25525), (0.0, 0.0, -0.0), (1.4028, 1.2372, 0.4616), "DV_BP_DM_Rubble_Masonry_Mound_Pile_F_Breakable12_19_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_DM_Rubble_Masonry_Mound_Pile_F_Breakable5_14 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (3512.4485, 2376.8108, 917.5242), (0.0, 0.0, -0.0), (1.4028, 1.2372, 0.4616), "DV_BP_DM_Rubble_Masonry_Mound_Pile_F_Breakable5_14_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_DM_Rubble_Masonry_Mound_Pile_F_Breakable6_5 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (500.6754, 5423.4805, 870.92706), (0.0, 0.0, -0.0), (1.4028, 1.2372, 0.4616), "DV_BP_DM_Rubble_Masonry_Mound_Pile_F_Breakable6_5_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_DM_Rubble_Masonry_Mound_Pile_F_Breakable7 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (482.08923, 5241.4766, 917.10706), (0.0, 0.0, -0.0), (1.4192, 1.5603, 0.4616), "DV_BP_DM_Rubble_Masonry_Mound_Pile_F_Breakable7_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_DM_Rubble_Masonry_Mound_Pile_F_Breakable8_9 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (1122.8607, 4194.3296, 870.72974), (0.0, 0.0, -0.0), (1.8695, 1.8474, 0.4616), "DV_BP_DM_Rubble_Masonry_Mound_Pile_F_Breakable8_9_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_DM_Rubble_Masonry_Mound_Pile_F_Breakable9_2 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (4294.096, 3445.7769, 915.7245), (0.0, 0.0, -0.0), (1.4028, 1.2372, 0.4616), "DV_BP_DM_Rubble_Masonry_Mound_Pile_F_Breakable9_2_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_DM_Rubble_Masonry_Mound_Pile_G_Breakable_8 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (3091.3835, 3592.98, 862.813), (0.0, 0.0, -0.0), (1.3415, 1.3304, 0.8591), "DV_BP_DM_Rubble_Masonry_Mound_Pile_G_Breakable_8_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_DM_Rubble_Masonry_Mound_Pile_G_Breakable10_5 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (3469.9153, 2462.789, 919.0824), (0.0, 0.0, -0.0), (1.3415, 1.3304, 0.8591), "DV_BP_DM_Rubble_Masonry_Mound_Pile_G_Breakable10_5_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_DM_Rubble_Masonry_Mound_Pile_G_Breakable11 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (3461.1064, 1179.3411, 867.11926), (0.0, 0.0, -0.0), (1.5790, 1.5876, 0.8591), "DV_BP_DM_Rubble_Masonry_Mound_Pile_G_Breakable11_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_DM_Rubble_Masonry_Mound_Pile_G_Breakable13_2 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (442.98596, 5480.8115, 867.99005), (0.0, 0.0, -0.0), (1.3415, 1.3304, 0.8591), "DV_BP_DM_Rubble_Masonry_Mound_Pile_G_Breakable13_2_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_DM_Rubble_Masonry_Mound_Pile_G_Breakable14 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (489.44037, 5944.6113, 867.99005), (0.0, 0.0, -0.0), (1.3415, 1.3304, 0.8591), "DV_BP_DM_Rubble_Masonry_Mound_Pile_G_Breakable14_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_DM_Rubble_Masonry_Mound_Pile_G_Breakable15_9 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (1822.3997, 4139.673, 867.81824), (0.0, 0.0, -0.0), (1.7665, 1.7720, 0.8591), "DV_BP_DM_Rubble_Masonry_Mound_Pile_G_Breakable15_9_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_DM_Rubble_Masonry_Mound_Pile_G_Breakable2_11 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (491.3836, 3692.98, 862.813), (0.0, 0.0, -0.0), (1.3415, 1.3304, 0.8591), "DV_BP_DM_Rubble_Masonry_Mound_Pile_G_Breakable2_11_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_DM_Rubble_Masonry_Mound_Pile_G_Breakable3_6 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (3403.396, 1005.5596, 867.11926), (0.0, 0.0, -0.0), (1.5790, 1.5876, 0.8591), "DV_BP_DM_Rubble_Masonry_Mound_Pile_G_Breakable3_6_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_DM_Rubble_Masonry_Mound_Pile_G_Breakable4_2 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (5241.384, 3192.98, 812.813), (0.0, 0.0, -0.0), (1.3415, 1.3304, 0.8591), "DV_BP_DM_Rubble_Masonry_Mound_Pile_G_Breakable4_2_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_DM_Rubble_Masonry_Mound_Pile_G_Breakable9_5 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (2041.3835, 1942.98, 862.813), (0.0, 0.0, -0.0), (1.3415, 1.3304, 0.8591), "DV_BP_DM_Rubble_Masonry_Mound_Pile_G_Breakable9_5_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_DM_Rubble_Masonry_Mound_Pile_H_Breakable_8 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (3258.6165, 3442.02, 851.7144), (0.0, 0.0, -0.0), (1.3415, 1.3304, 0.8082), "DV_BP_DM_Rubble_Masonry_Mound_Pile_H_Breakable_8_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_DM_Rubble_Masonry_Mound_Pile_H_Breakable10_5 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (1810.2377, 4191.7866, 856.71967), (0.0, 0.0, -0.0), (1.3415, 1.3304, 0.8082), "DV_BP_DM_Rubble_Masonry_Mound_Pile_H_Breakable10_5_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_DM_Rubble_Masonry_Mound_Pile_H_Breakable2_11 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (2058.6165, 3042.02, 801.7144), (0.0, 0.0, -0.0), (1.3415, 1.3304, 0.8082), "DV_BP_DM_Rubble_Masonry_Mound_Pile_H_Breakable2_11_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_DM_Rubble_Masonry_Mound_Pile_H_Breakable3_2 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (5458.6167, 3092.02, 801.7144), (0.0, 0.0, -0.0), (1.3415, 1.3304, 0.8082), "DV_BP_DM_Rubble_Masonry_Mound_Pile_H_Breakable3_2_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_DM_Rubble_Masonry_Mound_Pile_H_Breakable5_12 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (1983.1538, 2990.9294, 808.0488), (0.0, 0.0, -0.0), (1.3415, 1.3304, 0.8082), "DV_BP_DM_Rubble_Masonry_Mound_Pile_H_Breakable5_12_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_DM_Rubble_Masonry_Mound_Pile_H_Breakable8_22 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (3519.3296, 2622.3298, 907.9839), (0.0, 0.0, -0.0), (1.3415, 1.3304, 0.8082), "DV_BP_DM_Rubble_Masonry_Mound_Pile_H_Breakable8_22_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_DM_Rubble_Masonry_Mound_Pile_H_Breakable9_5 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (5545.448, 3489.1738, 801.7144), (0.0, 0.0, -0.0), (1.7090, 1.7156, 0.8082), "DV_BP_DM_Rubble_Masonry_Mound_Pile_H_Breakable9_5_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_DM_Rubble_Masonry_Pile_A_Breakable_2 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (351.54993, 5886.93, 902.01904), (0.0, 0.0, -0.0), (1.2743, 1.1677, 1.4244), "DV_BP_DM_Rubble_Masonry_Pile_A_Breakable_2_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_DM_Rubble_Masonry_Pile_B_Breakable_2 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (2739.5112, 2071.986, 954.08527), (0.0, 0.0, -0.0), (1.8422, 3.3418, 1.1191), "DV_BP_DM_Rubble_Masonry_Pile_B_Breakable_2_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_DM_Rubble_Masonry_Pile_B_Breakable2_5 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (1500.3604, 2034.3925, 904.0853), (0.0, 0.0, -0.0), (1.8422, 3.3418, 1.1191), "DV_BP_DM_Rubble_Masonry_Pile_B_Breakable2_5_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_DM_Rubble_Masonry_Pile_C_Breakable3_2 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (1636.4537, 6008.792, 884.51904), (0.0, 0.0, -0.0), (2.6538, 2.6688, 0.9351), "DV_BP_DM_Rubble_Masonry_Pile_C_Breakable3_2_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_DM_Rubble_Masonry_Pile_C_Breakable4_2 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (2235.0474, 2045.3066, 893.89075), (0.0, 0.0, -0.0), (2.6543, 2.6348, 0.9351), "DV_BP_DM_Rubble_Masonry_Pile_C_Breakable4_2_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_DM_Rubble_Masonry_Pile_D_Breakable2_2 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (4222.336, 5237.528, 990.45514), (0.0, 0.0, -0.0), (1.9349, 2.1855, 1.8381), "DV_BP_DM_Rubble_Masonry_Pile_D_Breakable2_2_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_DM_Rubble_Masonry_Pile_D_Breakable5 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (1508.7311, 1514.1206, 940.45514), (0.0, 0.0, -0.0), (2.3858, 2.1643, 1.8381), "DV_BP_DM_Rubble_Masonry_Pile_D_Breakable5_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_DM_Rubble_Masonry_Pile_D_Breakable6_5 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (3903.9023, 3256.9749, 990.45514), (0.0, 0.0, -0.0), (2.9136, 2.9136, 1.8381), "DV_BP_DM_Rubble_Masonry_Pile_D_Breakable6_5_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_DM_Rubble_Masonry_Pile_D_Breakable7_8 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (2587.528, 1677.664, 990.45514), (0.0, 0.0, -0.0), (2.1855, 1.9349, 1.8381), "DV_BP_DM_Rubble_Masonry_Pile_D_Breakable7_8_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_DM_Rubble_Masonry_Pile_E_Breakable_5 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (4185.6187, 3812.0522, 923.3407), (0.0, 0.0, -0.0), (2.5083, 2.2457, 1.3025), "DV_BP_DM_Rubble_Masonry_Pile_E_Breakable_5_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_DM_Rubble_Masonry_Pile_E_Breakable10_2 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (1856.026, 1226.3982, 910.8446), (0.0, 0.0, -0.0), (2.5083, 2.2457, 1.3025), "DV_BP_DM_Rubble_Masonry_Pile_E_Breakable10_2_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_DM_Rubble_Masonry_Pile_E_Breakable12_11 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (3085.6187, 1912.0524, 873.3407), (0.0, 0.0, -0.0), (2.5083, 2.2457, 1.3025), "DV_BP_DM_Rubble_Masonry_Pile_E_Breakable12_11_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_DM_Rubble_Masonry_Pile_E_Breakable3_5 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (4335.6187, 5212.0522, 923.3407), (0.0, 0.0, -0.0), (2.5083, 2.2457, 1.3025), "DV_BP_DM_Rubble_Masonry_Pile_E_Breakable3_5_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_DM_Rubble_Masonry_Pile_E_Breakable4_14 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (3335.6187, 4862.0522, 873.3407), (0.0, 0.0, -0.0), (2.5083, 2.2457, 1.3025), "DV_BP_DM_Rubble_Masonry_Pile_E_Breakable4_14_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_DM_Rubble_Masonry_Pile_E_Breakable5_2 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (2712.0522, 1664.3813, 923.3407), (0.0, 0.0, -0.0), (2.2457, 2.5083, 1.3025), "DV_BP_DM_Rubble_Masonry_Pile_E_Breakable5_2_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_DM_Rubble_Masonry_Pile_E_Breakable6_8 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (3235.6187, 2962.0522, 873.3407), (0.0, 0.0, -0.0), (2.5083, 2.2457, 1.3025), "DV_BP_DM_Rubble_Masonry_Pile_E_Breakable6_8_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_DM_Rubble_Masonry_Pile_E_Breakable7_17 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (1174.9524, 4715.3696, 873.3407), (0.0, 0.0, -0.0), (3.2224, 3.0953, 1.3025), "DV_BP_DM_Rubble_Masonry_Pile_E_Breakable7_17_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_DM_Rubble_Masonry_Pile_E_Breakable8_14 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (1885.6187, 1112.0524, 873.3407), (0.0, 0.0, -0.0), (2.5083, 2.2457, 1.3025), "DV_BP_DM_Rubble_Masonry_Pile_E_Breakable8_14_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_DM_Rubble_Masonry_Pile_E_Breakable9_20 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (1235.6187, 5112.0522, 873.3407), (0.0, 0.0, -0.0), (2.5083, 2.2457, 1.3025), "DV_BP_DM_Rubble_Masonry_Pile_E_Breakable9_20_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_DM_Rubble_Masonry_Pile_F_Breakable10 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (1626.1881, 5448.4897, 902.851), (0.0, 0.0, -0.0), (4.4144, 4.7657, 1.3764), "DV_BP_DM_Rubble_Masonry_Pile_F_Breakable10_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_DM_Rubble_Masonry_Pile_F_Breakable11_6 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (4928.8, 4505.9033, 959.1206), (0.0, 0.0, -0.0), (5.1976, 5.4485, 1.3764), "DV_BP_DM_Rubble_Masonry_Pile_F_Breakable11_6_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_DM_Rubble_Masonry_Pile_F_Breakable12_2 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (4850.571, 2123.853, 952.851), (0.0, 0.0, -0.0), (4.4301, 4.0437, 1.3764), "DV_BP_DM_Rubble_Masonry_Pile_F_Breakable12_2_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_DM_Rubble_Masonry_Pile_F_Breakable13_5 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (4900.571, 1423.8529, 952.851), (0.0, 0.0, -0.0), (4.4301, 4.0437, 1.3764), "DV_BP_DM_Rubble_Masonry_Pile_F_Breakable13_5_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_DM_Rubble_Masonry_Pile_F_Breakable14_8 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (4650.571, 3173.853, 952.851), (0.0, 0.0, -0.0), (4.4301, 4.0437, 1.3764), "DV_BP_DM_Rubble_Masonry_Pile_F_Breakable14_8_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_DM_Rubble_Masonry_Pile_F_Breakable15_11 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (5123.853, 2899.4292, 852.851), (0.0, 0.0, -0.0), (4.0437, 4.4301, 1.3764), "DV_BP_DM_Rubble_Masonry_Pile_F_Breakable15_11_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_DM_Rubble_Masonry_Pile_F_Breakable16_14 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (3250.5708, 2023.8528, 902.851), (0.0, 0.0, -0.0), (4.4301, 4.0437, 1.3764), "DV_BP_DM_Rubble_Masonry_Pile_F_Breakable16_14_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_DM_Rubble_Masonry_Pile_F_Breakable17_17 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (3126.3782, 1644.132, 902.851), (0.0, 0.0, -0.0), (4.4144, 4.7657, 1.3764), "DV_BP_DM_Rubble_Masonry_Pile_F_Breakable17_17_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_DM_Rubble_Masonry_Pile_F_Breakable18 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (3656.5442, 3169.097, 952.851), (0.0, 0.0, -0.0), (5.0525, 5.3258, 1.3764), "DV_BP_DM_Rubble_Masonry_Pile_F_Breakable18_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_DM_Rubble_Masonry_Pile_F_Breakable19_21 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (2450.5708, 1873.8528, 902.851), (0.0, 0.0, -0.0), (4.4301, 4.0437, 1.3764), "DV_BP_DM_Rubble_Masonry_Pile_F_Breakable19_21_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_DM_Rubble_Masonry_Pile_F_Breakable2_9 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (4649.823, 5245.8276, 959.1853), (0.0, 0.0, -0.0), (4.4301, 4.0437, 1.3764), "DV_BP_DM_Rubble_Masonry_Pile_F_Breakable2_9_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_DM_Rubble_Masonry_Pile_F_Breakable20_24 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (4050.5708, 4723.853, 952.851), (0.0, 0.0, -0.0), (4.4301, 4.0437, 1.3764), "DV_BP_DM_Rubble_Masonry_Pile_F_Breakable20_24_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_DM_Rubble_Masonry_Pile_F_Breakable21 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (3077.2097, 3869.4883, 902.851), (0.0, 0.0, -0.0), (5.5460, 5.3150, 1.3764), "DV_BP_DM_Rubble_Masonry_Pile_F_Breakable21_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_DM_Rubble_Masonry_Pile_F_Breakable22 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (1872.7096, 3377.8784, 852.851), (0.0, 0.0, -0.0), (5.5460, 5.3150, 1.3764), "DV_BP_DM_Rubble_Masonry_Pile_F_Breakable22_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_DM_Rubble_Masonry_Pile_F_Breakable23 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (3048.112, 5420.155, 902.851), (0.0, 0.0, -0.0), (5.5460, 5.3150, 1.3764), "DV_BP_DM_Rubble_Masonry_Pile_F_Breakable23_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_DM_Rubble_Masonry_Pile_F_Breakable24 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (3264.9517, 4415.289, 902.851), (0.0, 0.0, -0.0), (4.7515, 5.0650, 1.3764), "DV_BP_DM_Rubble_Masonry_Pile_F_Breakable24_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_DM_Rubble_Masonry_Pile_F_Breakable25 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (3268.7737, 5029.3823, 902.851), (0.0, 0.0, -0.0), (5.3150, 5.5460, 1.3764), "DV_BP_DM_Rubble_Masonry_Pile_F_Breakable25_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_DM_Rubble_Masonry_Pile_F_Breakable26 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (2291.2537, 3689.8428, 902.851), (0.0, 0.0, -0.0), (5.5460, 5.3150, 1.3764), "DV_BP_DM_Rubble_Masonry_Pile_F_Breakable26_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_DM_Rubble_Masonry_Pile_F_Breakable27 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (2308.9683, 5392.8457, 902.851), (0.0, 0.0, -0.0), (5.5460, 5.3150, 1.3764), "DV_BP_DM_Rubble_Masonry_Pile_F_Breakable27_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_DM_Rubble_Masonry_Pile_F_Breakable28 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (1470.9224, 5373.7764, 902.851), (0.0, 0.0, -0.0), (5.9453, 5.9929, 1.3764), "DV_BP_DM_Rubble_Masonry_Pile_F_Breakable28_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_DM_Rubble_Masonry_Pile_F_Breakable29_48 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (1060.598, 4921.377, 902.851), (0.0, 0.0, -0.0), (5.7240, 5.5371, 1.3764), "DV_BP_DM_Rubble_Masonry_Pile_F_Breakable29_48_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_DM_Rubble_Masonry_Pile_F_Breakable3_5 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (2250.5708, 2623.853, 902.851), (0.0, 0.0, -0.0), (4.4301, 4.0437, 1.3764), "DV_BP_DM_Rubble_Masonry_Pile_F_Breakable3_5_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_DM_Rubble_Masonry_Pile_F_Breakable30 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (2091.3755, 2953.1357, 852.851), (0.0, 0.0, -0.0), (4.4144, 4.7657, 1.3764), "DV_BP_DM_Rubble_Masonry_Pile_F_Breakable30_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_DM_Rubble_Masonry_Pile_F_Breakable4_38 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (1050.5708, 4023.853, 902.851), (0.0, 0.0, -0.0), (4.4301, 4.0437, 1.3764), "DV_BP_DM_Rubble_Masonry_Pile_F_Breakable4_38_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_DM_Rubble_Masonry_Pile_F_Breakable5_5 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (2763.7102, 1884.6719, 902.851), (0.0, 0.0, -0.0), (4.4301, 4.0437, 1.3764), "DV_BP_DM_Rubble_Masonry_Pile_F_Breakable5_5_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_DM_Rubble_Masonry_Pile_F_Breakable6_8 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (1850.5708, 2609.231, 902.851), (0.0, 0.0, -0.0), (4.4301, 4.0437, 1.3764), "DV_BP_DM_Rubble_Masonry_Pile_F_Breakable6_8_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_DM_Rubble_Masonry_Pile_F_Breakable7_11 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (2276.147, 1272.0194, 902.851), (0.0, 0.0, -0.0), (4.0437, 4.4301, 1.3764), "DV_BP_DM_Rubble_Masonry_Pile_F_Breakable7_11_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_DM_Rubble_Masonry_Pile_F_Breakable8_41 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (866.4132, 4810.5337, 902.851), (0.0, 0.0, -0.0), (5.5371, 5.7240, 1.3764), "DV_BP_DM_Rubble_Masonry_Pile_F_Breakable8_41_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_DM_Rubble_Masonry_Pile_H_Breakable11 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (2802.7815, 2037.4326, 891.54803), (0.0, 0.0, -0.0), (4.0375, 3.9916, 1.3071), "DV_BP_DM_Rubble_Masonry_Pile_H_Breakable11_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_DM_Rubble_Masonry_Pile_H_Breakable13_2 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (2038.5212, 2680.2, 891.5479), (0.0, 0.0, -0.0), (3.1028, 2.5859, 1.3071), "DV_BP_DM_Rubble_Masonry_Pile_H_Breakable13_2_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_DM_Rubble_Masonry_Pile_H_Breakable14_29 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (988.52124, 4380.2, 891.5479), (0.0, 0.0, -0.0), (3.1028, 2.5859, 1.3071), "DV_BP_DM_Rubble_Masonry_Pile_H_Breakable14_29_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_DM_Rubble_Masonry_Pile_H_Breakable15_11 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (3488.5212, 1180.2, 891.5479), (0.0, 0.0, -0.0), (3.1028, 2.5859, 1.3071), "DV_BP_DM_Rubble_Masonry_Pile_H_Breakable15_11_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_DM_Rubble_Masonry_Pile_H_Breakable16 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (1518.9039, 3273.8, 841.5479), (0.0, 0.0, -0.0), (3.6663, 3.3009, 1.3071), "DV_BP_DM_Rubble_Masonry_Pile_H_Breakable16_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_DM_Rubble_Masonry_Pile_H_Breakable17_17 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (4577.4805, 1376.8336, 941.5479), (0.0, 0.0, -0.0), (3.6549, 3.9049, 1.3071), "DV_BP_DM_Rubble_Masonry_Pile_H_Breakable17_17_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_DM_Rubble_Masonry_Pile_H_Breakable3_5 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (4288.5215, 5280.2, 941.5479), (0.0, 0.0, -0.0), (3.1028, 2.5859, 1.3071), "DV_BP_DM_Rubble_Masonry_Pile_H_Breakable3_5_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_DM_Rubble_Masonry_Pile_H_Breakable4_23 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (3238.5212, 3980.1997, 891.5479), (0.0, 0.0, -0.0), (3.1028, 2.5859, 1.3071), "DV_BP_DM_Rubble_Masonry_Pile_H_Breakable4_23_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_DM_Rubble_Masonry_Pile_H_Breakable5_2 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (4188.5215, 1230.2, 941.5479), (0.0, 0.0, -0.0), (3.1028, 2.5859, 1.3071), "DV_BP_DM_Rubble_Masonry_Pile_H_Breakable5_2_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_DM_Rubble_Masonry_Pile_H_Breakable6_20 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (4588.5215, 3980.1997, 941.5479), (0.0, 0.0, -0.0), (3.1028, 2.5859, 1.3071), "DV_BP_DM_Rubble_Masonry_Pile_H_Breakable6_20_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_DM_Rubble_Masonry_Pile_H_Breakable7_5 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (4988.5215, 1780.2, 941.5479), (0.0, 0.0, -0.0), (3.1028, 2.5859, 1.3071), "DV_BP_DM_Rubble_Masonry_Pile_H_Breakable7_5_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_DM_Rubble_Masonry_Pile_H_Breakable8_5 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (1508.2721, 1609.8582, 897.88226), (0.0, 0.0, -0.0), (3.1028, 2.5859, 1.3071), "DV_BP_DM_Rubble_Masonry_Pile_H_Breakable8_5_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_DM_Rubble_Masonry_Pile_H_Breakable9_26 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (888.52124, 4130.2, 891.5479), (0.0, 0.0, -0.0), (3.1028, 2.5859, 1.3071), "DV_BP_DM_Rubble_Masonry_Pile_H_Breakable9_26_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_DM_Rubble_Masonry_Pile_I_Breakable2_2 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (4939.3384, 1935.1735, 951.5136), (0.0, 0.0, -0.0), (1.8409, 3.9423, 1.1909), "DV_BP_DM_Rubble_Masonry_Pile_I_Breakable2_2_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_DM_Rubble_Masonry_Pile_I_Breakable3 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (3810.6614, 4314.8267, 951.5136), (0.0, 0.0, -0.0), (1.8409, 3.9423, 1.1909), "DV_BP_DM_Rubble_Masonry_Pile_I_Breakable3_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_DM_Rubble_Masonry_Pile_I_Breakable4_8 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (5110.6616, 3164.8264, 851.5136), (0.0, 0.0, -0.0), (1.8409, 3.9423, 1.1909), "DV_BP_DM_Rubble_Masonry_Pile_I_Breakable4_8_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_DM_Rubble_Masonry_Pile_I_Breakable5_11 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (3960.6614, 4414.8267, 951.5136), (0.0, 0.0, -0.0), (1.8409, 3.9423, 1.1909), "DV_BP_DM_Rubble_Masonry_Pile_I_Breakable5_11_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_DM_Rubble_Masonry_Pile_J_Breakable_2 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (4465.6074, 1227.8975, 990.24634), (0.0, 0.0, -0.0), (3.3418, 2.4940, 1.8423), "DV_BP_DM_Rubble_Masonry_Pile_J_Breakable_2_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_DM_Rubble_Masonry_Pile_J_Breakable2_5 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (3939.196, 4876.841, 990.24634), (0.0, 0.0, -0.0), (2.6735, 3.4896, 1.8423), "DV_BP_DM_Rubble_Masonry_Pile_J_Breakable2_5_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_DM_Warren_Lighting_Torch_Breakable4_11 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (2654.8801, 5695.0103, 964.8237), (0.0, 0.0, -0.0), (1.0112, 1.0765, 1.9128), "DV_BP_DM_Warren_Lighting_Torch_Breakable4_11_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_Ruin_Column_Large_A_Base_2_Breakable_2 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (3950.0, 1200.0, 1092.3254), (0.0, 0.0, -0.0), (5.5228, 5.5228, 3.8465), "DV_BP_Ruin_Column_Large_A_Base_2_Breakable_2_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_Ruin_Column_Large_A_Base_2_Breakable2 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (4950.0, 2400.0, 1092.3254), (0.0, 0.0, -0.0), (5.5228, 5.5228, 3.8465), "DV_BP_Ruin_Column_Large_A_Base_2_Breakable2_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_Ruin_Column_Large_A_Base_2_Breakable3_6 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (1350.0, 4000.0, 1092.3254), (0.0, 0.0, -0.0), (5.5228, 5.5228, 3.8465), "DV_BP_Ruin_Column_Large_A_Base_2_Breakable3_6_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_Ruin_Column_Large_A_Base_2_Breakable4_9 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (1550.0, 3800.0, 1092.3254), (0.0, 0.0, -0.0), (5.5228, 5.5228, 3.8465), "DV_BP_Ruin_Column_Large_A_Base_2_Breakable4_9_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_Ruin_Column_Large_A_Capital_1_Breakable_5 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (3133.439, 4188.194, 960.828), (0.0, 0.0, -0.0), (4.7415, 5.3241, 4.0880), "DV_BP_Ruin_Column_Large_A_Capital_1_Breakable_5_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_Ruin_Column_Large_A_Capital_1_Breakable2_8 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (1550.0, 4000.0, 1827.973), (0.0, 0.0, -0.0), (5.2610, 5.2610, 2.5595), "DV_BP_Ruin_Column_Large_A_Capital_1_Breakable2_8_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_Ruin_Column_Large_A_Capital_2_Breakable_2 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (5040.315, 2955.5142, 995.7555), (0.0, 0.0, -0.0), (6.4605, 5.3508, 6.0301), "DV_BP_Ruin_Column_Large_A_Capital_2_Breakable_2_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_Ruin_Column_Large_A_Capital_2_Breakable2_5 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (2656.7605, 1900.002, 1051.7802), (0.0, 0.0, -0.0), (5.1625, 5.0327, 5.8780), "DV_BP_Ruin_Column_Large_A_Capital_2_Breakable2_5_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_Ruin_Column_Large_A_Capital_2_Breakable3_8 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (976.7457, 4250.0, 950.0284), (0.0, 0.0, -0.0), (5.3450, 3.7998, 5.2566), "DV_BP_Ruin_Column_Large_A_Capital_2_Breakable3_8_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_Ruin_Column_Large_A_Capital_2_Breakable4_11 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (2047.0135, 4876.756, 987.79816), (0.0, 0.0, -0.0), (5.8541, 6.0453, 4.7164), "DV_BP_Ruin_Column_Large_A_Capital_2_Breakable4_11_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_Ruin_Column_Large_A_Capital_4_Breakable_5 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (3092.8843, 5100.153, 1047.2767), (0.0, 0.0, -0.0), (7.0784, 7.2235, 4.0479), "DV_BP_Ruin_Column_Large_A_Capital_4_Breakable_5_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_Ruin_Column_Large_A_Capital_4_Breakable2_8 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (1911.1367, 2686.9883, 952.9411), (0.0, 0.0, -0.0), (7.9390, 7.2491, 6.1541), "DV_BP_Ruin_Column_Large_A_Capital_4_Breakable2_8_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_Ruin_Column_Large_A_Shaft_2_Breakable_2 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (3268.651, 1834.5647, 899.99994), (0.0, 0.0, -0.0), (5.1421, 4.9375, 3.5809), "DV_BP_Ruin_Column_Large_A_Shaft_2_Breakable_2_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_Ruin_Column_Large_A_Shaft_2_Breakable2_5 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (973.35913, 4814.3584, 984.5645), (0.0, 0.0, -0.0), (4.7790, 4.8020, 4.9375), "DV_BP_Ruin_Column_Large_A_Shaft_2_Breakable2_5_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_Ruin_Column_Large_A_Shaft_2_Breakable3_8 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (2550.0, 5200.0, 1500.0967), (0.0, 0.0, -0.0), (3.5809, 3.5809, 4.0039), "DV_BP_Ruin_Column_Large_A_Shaft_2_Breakable3_8_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_Ruin_Column_Large_A_Shaft_2_Breakable4_11 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (1700.0, 3451.7976, 862.91614), (0.0, 0.0, -0.0), (3.5809, 4.7943, 4.4951), "DV_BP_Ruin_Column_Large_A_Shaft_2_Breakable4_11_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_Ruin_Column_Large_A_Shaft_3_Breakable_2 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (1119.4998, 4562.423, 919.1053), (0.0, 0.0, -0.0), (3.4533, 3.4535, 1.3896), "DV_BP_Ruin_Column_Large_A_Shaft_3_Breakable_2_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_Ruin_Column_Large_A_Shaft_3_Breakable2_5 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (2550.0, 4000.0, 1369.1052), (0.0, 0.0, -0.0), (3.5752, 3.5752, 1.3896), "DV_BP_Ruin_Column_Large_A_Shaft_3_Breakable2_5_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_Ruin_Column_Large_A_Shaft_3_Breakable3_8 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (1697.3077, 3180.7773, 900.0), (0.0, 0.0, -0.0), (3.6827, 1.6958, 3.5752), "DV_BP_Ruin_Column_Large_A_Shaft_3_Breakable3_8_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_Ruins_Column_Single_A_A_Breakable12 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (4200.8115, 3800.0105, 1064.4292), (0.0, 0.0, -0.0), (0.9437, 0.9084, 2.2808), "DV_BP_Ruins_Column_Single_A_A_Breakable12_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_Ruins_Column_Single_A_A_Breakable13 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (4450.8115, 3800.0105, 1064.4292), (0.0, 0.0, -0.0), (0.9437, 0.9084, 2.2808), "DV_BP_Ruins_Column_Single_A_A_Breakable13_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_Ruins_Column_Single_A_A_Breakable14 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (4700.8115, 3800.0105, 1064.4292), (0.0, 0.0, -0.0), (0.9437, 0.9084, 2.2808), "DV_BP_Ruins_Column_Single_A_A_Breakable14_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_Ruins_Column_Single_A_A_Breakable15 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (4650.8115, 5300.0107, 1064.4292), (0.0, 0.0, -0.0), (0.9437, 0.9084, 2.2808), "DV_BP_Ruins_Column_Single_A_A_Breakable15_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_Ruins_Column_Single_A_A_Breakable16 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (4249.1885, 5299.9893, 1064.4292), (0.0, 0.0, -0.0), (0.9437, 0.9084, 2.2808), "DV_BP_Ruins_Column_Single_A_A_Breakable16_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_Ruins_Column_Single_A_A_Breakable17 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (4450.8115, 5300.0107, 1064.4292), (0.0, 0.0, -0.0), (0.9437, 0.9084, 2.2808), "DV_BP_Ruins_Column_Single_A_A_Breakable17_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_Ruins_Column_Single_A_A_Breakable18 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (5050.0107, 4899.1885, 1064.4292), (0.0, 0.0, -0.0), (0.9084, 0.9437, 2.2808), "DV_BP_Ruins_Column_Single_A_A_Breakable18_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_Ruins_Column_Single_A_A_Breakable19 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (5049.9893, 4600.8115, 1064.4292), (0.0, 0.0, -0.0), (0.9084, 0.9437, 2.2808), "DV_BP_Ruins_Column_Single_A_A_Breakable19_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_Ruins_Column_Single_A_A_Breakable2 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (1400.0105, 1549.1885, 1064.4292), (0.0, 0.0, -0.0), (0.9084, 0.9437, 2.2808), "DV_BP_Ruins_Column_Single_A_A_Breakable2_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_Ruins_Column_Single_A_A_Breakable20_22 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (3849.9895, 4850.8115, 1064.4292), (0.0, 0.0, -0.0), (0.9084, 0.9437, 2.2808), "DV_BP_Ruins_Column_Single_A_A_Breakable20_22_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_Ruins_Column_Single_A_A_Breakable21 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (3850.0105, 4599.1885, 1064.4292), (0.0, 0.0, -0.0), (0.9084, 0.9437, 2.2808), "DV_BP_Ruins_Column_Single_A_A_Breakable21_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_Ruins_Column_Single_A_A_Breakable22 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (3849.9895, 4350.8115, 1064.4292), (0.0, 0.0, -0.0), (0.9084, 0.9437, 2.2808), "DV_BP_Ruins_Column_Single_A_A_Breakable22_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_Ruins_Column_Single_A_A_Breakable3 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (1399.9895, 1800.8115, 1064.4292), (0.0, 0.0, -0.0), (0.9084, 0.9437, 2.2808), "DV_BP_Ruins_Column_Single_A_A_Breakable3_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_Ruins_Column_Single_A_A_Breakable4 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (1849.1885, 2549.9895, 1064.4292), (0.0, 0.0, -0.0), (0.9437, 0.9084, 2.2808), "DV_BP_Ruins_Column_Single_A_A_Breakable4_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_Ruins_Column_Single_A_A_Breakable6 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (2249.1885, 2549.9895, 1064.4292), (0.0, 0.0, -0.0), (0.9437, 0.9084, 2.2808), "DV_BP_Ruins_Column_Single_A_A_Breakable6_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_Ruins_Column_Single_A_A_Breakable7 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (2050.8115, 2550.0105, 1064.4292), (0.0, 0.0, -0.0), (0.9437, 0.9084, 2.2808), "DV_BP_Ruins_Column_Single_A_A_Breakable7_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_Ruins_Column_Single_A_A_Breakable8 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (2699.9895, 2050.8115, 1064.4292), (0.0, 0.0, -0.0), (0.9084, 0.9437, 2.2808), "DV_BP_Ruins_Column_Single_A_A_Breakable8_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_Ruins_Column_Single_A_A_Breakable9 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (2699.9895, 1550.8115, 1064.4292), (0.0, 0.0, -0.0), (0.9084, 0.9437, 2.2808), "DV_BP_Ruins_Column_Single_A_A_Breakable9_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_Ruins_Column_Single_A_B_Breakable_2 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (2700.0, 1800.0, 1000.5016), (0.0, 0.0, -0.0), (0.9079, 0.9706, 1.0044), "DV_BP_Ruins_Column_Single_A_B_Breakable_2_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_Ruins_Column_Single_A_B_Breakable2_5 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (5050.0, 4300.0, 1050.5016), (0.0, 0.0, -0.0), (0.9079, 0.9706, 1.0044), "DV_BP_Ruins_Column_Single_A_B_Breakable2_5_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_Ruins_Column_Single_A_C_Breakable_2 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (3849.9456, 4850.0986, 1908.6327), (0.0, 0.0, -0.0), (0.8430, 0.7647, 1.4676), "DV_BP_Ruins_Column_Single_A_C_Breakable_2_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_Ruins_Column_Single_A_E12 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (4203.5327, 3800.0593, 1252.4316), (0.0, 0.0, -0.0), (0.5123, 0.6185, 2.1837), "DV_BP_Ruins_Column_Single_A_E12_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_Ruins_Column_Single_A_E16 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (4703.5327, 3800.0593, 1252.4316), (0.0, 0.0, -0.0), (0.5123, 0.6185, 2.1837), "DV_BP_Ruins_Column_Single_A_E16_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_Ruins_Column_Single_A_E17 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (4696.4673, 3800.0593, 1447.5684), (0.0, 0.0, -0.0), (0.5123, 0.6185, 2.1837), "DV_BP_Ruins_Column_Single_A_E17_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_Ruins_Column_Single_A_E18 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (4653.5327, 5300.059, 1252.4316), (0.0, 0.0, -0.0), (0.5123, 0.6185, 2.1837), "DV_BP_Ruins_Column_Single_A_E18_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_Ruins_Column_Single_A_E19 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (4646.4673, 5300.0596, 1447.5684), (0.0, 0.0, -0.0), (0.5123, 0.6185, 2.1837), "DV_BP_Ruins_Column_Single_A_E19_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_Ruins_Column_Single_A_E20_42 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (3849.9407, 4853.5327, 1252.4316), (0.0, 0.0, -0.0), (0.6185, 0.5123, 2.1837), "DV_BP_Ruins_Column_Single_A_E20_42_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_Ruins_Column_Single_A_E21_43 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (3849.9407, 4846.4673, 1447.5684), (0.0, 0.0, -0.0), (0.6185, 0.5123, 2.1837), "DV_BP_Ruins_Column_Single_A_E21_43_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_Ruins_Column_Single_A_E22_36 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (5049.941, 4603.5327, 1252.4316), (0.0, 0.0, -0.0), (0.6185, 0.5123, 2.1837), "DV_BP_Ruins_Column_Single_A_E22_36_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_Ruins_Column_Single_A_E23_46 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (3849.9407, 4603.5327, 1252.4316), (0.0, 0.0, -0.0), (0.6185, 0.5123, 2.1837), "DV_BP_Ruins_Column_Single_A_E23_46_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_Ruins_Column_Single_A_E25_50 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (3849.9407, 4353.5327, 1252.4316), (0.0, 0.0, -0.0), (0.6185, 0.5123, 2.1837), "DV_BP_Ruins_Column_Single_A_E25_50_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_Ruins_Column_Single_A_E26 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (3849.9407, 4346.4673, 1447.5684), (0.0, 0.0, -0.0), (0.6185, 0.5123, 2.1837), "DV_BP_Ruins_Column_Single_A_E26_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_Ruins_Column_Single_A_E27 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (3849.9407, 4853.5327, 1602.4316), (0.0, 0.0, -0.0), (0.6185, 0.5123, 2.1837), "DV_BP_Ruins_Column_Single_A_E27_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_Ruins_Column_Single_A_E28 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (3850.0593, 4853.5327, 1747.5684), (0.0, 0.0, -0.0), (0.6185, 0.5123, 2.1837), "DV_BP_Ruins_Column_Single_A_E28_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_Ruins_Column_Single_A_E4 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (2246.4675, 2549.9407, 1252.4316), (0.0, 0.0, -0.0), (0.5123, 0.6185, 2.1837), "DV_BP_Ruins_Column_Single_A_E4_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_Ruins_Column_Single_A_E5 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (2253.5325, 2549.9407, 1447.5684), (0.0, 0.0, -0.0), (0.5123, 0.6185, 2.1837), "DV_BP_Ruins_Column_Single_A_E5_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_Ruins_Column_Single_A_E6 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (2053.5325, 2550.0593, 1252.4316), (0.0, 0.0, -0.0), (0.5123, 0.6185, 2.1837), "DV_BP_Ruins_Column_Single_A_E6_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_Ruins_Column_Single_A_E7 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (2046.4675, 2550.0593, 1447.5684), (0.0, 0.0, -0.0), (0.5123, 0.6185, 2.1837), "DV_BP_Ruins_Column_Single_A_E7_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: DecorationBlockingVolume_1 (EMorSimpleShape::Empty)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (4450.0, 3700.0, 1200.0), (0.0, 0.0, -0.0), (2.0000, 2.0000, 2.0000), "DV_DecorationBlockingVolume_1", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: DecorationBlockingVolume4 (EMorSimpleShape::Empty)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (2850.0, 1800.0, 1200.0), (-0.0, -89.99999818714215, -0.0), (2.0000, 2.0000, 2.0000), "DV_DecorationBlockingVolume4", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: Rubble_Masonry_Mound_Pile_B_Blueprint_2 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (4500.042, 3661.2095, 918.41003), (0.0, 0.0, -0.0), (2.6965, 2.4601, 0.5041), "DV_Rubble_Masonry_Mound_Pile_B_Blueprint_2_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: Rubble_Masonry_Mound_Pile_B_Blueprint2_2 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (2698.841, 1787.1299, 918.41003), (0.0, 0.0, -0.0), (2.6489, 2.2365, 0.5041), "DV_Rubble_Masonry_Mound_Pile_B_Blueprint2_2_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: Rubble_Masonry_Mound_Pile_C_Blueprint3_2 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (3757.9229, 4256.6436, 926.251), (0.0, 0.0, -0.0), (2.4071, 2.3856, 0.7422), "DV_Rubble_Masonry_Mound_Pile_C_Blueprint3_2_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: Rubble_Masonry_Mound_Pile_C_Blueprint5_8 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (4457.923, 5256.6436, 926.251), (0.0, 0.0, -0.0), (2.4071, 2.3856, 0.7422), "DV_Rubble_Masonry_Mound_Pile_C_Blueprint5_8_BRK", _folder)
if a: placed += 1
else: skipped += 1

# ======================================================================
# SUMMARY
# ======================================================================
unreal.log(f"[{BUBBLE_NAME}] Reconstruction complete: {placed} placed, {skipped} skipped, {errors} errors")
