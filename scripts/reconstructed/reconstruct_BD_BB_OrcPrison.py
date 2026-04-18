"""Auto-generated level reconstruction script.
Bubble: BD_BB_OrcPrison
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

BUBBLE_NAME = "BD_BB_OrcPrison"
placed = 0
skipped = 0
errors = 0

# ======================================================================
# PHASE 1: InstancedMeshCatalog  (static mesh placement)
# ======================================================================
unreal.log(f"[{BUBBLE_NAME}] Phase 1: Placing static meshes...")

# Batch 0: StaticMesh'City_Floor_Trim_A_1m' (1 instances)
_mesh_path = "/Game/Art/Assets/Kits/Architecture/City/City_Floor_Trim_A_1m"
_materials = ['/Game/Art/Assets/Kits/Architecture/Suburbs/Materials/Suburbs_Trim_Sheet_B/MI_Suburbs_Trim_Sheet_B']
_folder = "Reconstruction/BD_BB_OrcPrison/Meshes"
a = spawn_static_mesh(_mesh_path, _materials, (1908.0, 3696.0, 700.0), (0.0, 89.99999818714215, -0.0), (1.0, 1.0, 1.0), "City_Floor_Trim_A_05m12", _folder)
if a: placed += 1
else: skipped += 1

# Batch 1: StaticMesh'City_Floor_Trim_A_3m' (11 instances)
_mesh_path = "/Game/Art/Assets/Kits/Architecture/City/City_Floor_Trim_A_3m"
_materials = ['/Game/Art/Assets/Kits/Architecture/Suburbs/Materials/Suburbs_Trim_Sheet_B/MI_Suburbs_Trim_Sheet_B']
_folder = "Reconstruction/BD_BB_OrcPrison/Meshes"
a = spawn_static_mesh(_mesh_path, _materials, (3205.0, 2983.0, 702.0), (0.0, -179.99998633961752, -0.0), (1.0, 1.0, 1.0), "City_Floor_Trim_A_05m_38", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1908.0, 5196.0, 700.0), (0.0, 89.99999818714215, -0.0), (1.0, 1.0, 1.0), "City_Floor_Trim_A_05m10", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1908.0, 3996.0, 700.0), (0.0, 89.99999818714215, -0.0), (1.0, 1.0, 1.0), "City_Floor_Trim_A_05m11", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2905.0, 2983.0, 702.0), (0.0, -179.99998633961752, -0.0), (1.0, 1.0, 1.0), "City_Floor_Trim_A_05m2", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3225.0, 1786.0, 800.0), (0.0, -179.99998633961752, -0.0), (1.0, 1.0, 1.0), "City_Floor_Trim_A_05m3", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2925.0, 1786.0, 800.0), (0.0, -179.99998633961752, -0.0), (1.0, 1.0, 1.0), "City_Floor_Trim_A_05m4", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1198.0, 3156.0, 800.0), (0.0, 89.99999818714215, -0.0), (1.0, 1.0, 1.0), "City_Floor_Trim_A_05m5", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1198.0, 3456.0, 800.0), (0.0, 89.99999818714215, -0.0), (1.0, 1.0, 1.0), "City_Floor_Trim_A_05m6", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1908.0, 4296.0, 700.0), (0.0, 89.99999818714215, -0.0), (1.0, 1.0, 1.0), "City_Floor_Trim_A_05m7", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1908.0, 4596.0, 700.0), (0.0, 89.99999818714215, -0.0), (1.0, 1.0, 1.0), "City_Floor_Trim_A_05m8", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1908.0, 4896.0, 700.0), (0.0, 89.99999818714215, -0.0), (1.0, 1.0, 1.0), "City_Floor_Trim_A_05m9", _folder)
if a: placed += 1
else: skipped += 1

# Batch 2: StaticMesh'City_Trim_C_3m' (20 instances)
_mesh_path = "/Game/Art/Assets/Kits/Architecture/City/City_Trim_C_3m"
_materials = ['/Game/Art/Assets/Kits/Architecture/Suburbs/Materials/Suburbs_Trim_Sheet_A/MI_Suburbs_Trim_Sheet_A']
_folder = "Reconstruction/BD_BB_OrcPrison/Meshes"
a = spawn_static_mesh(_mesh_path, _materials, (1155.0, 2910.0, 1300.0), (0.0, 0.0, -0.0), (1.0, 1.0, 1.0), "City_Trim_C_3m_956", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (295.00452, 3764.9922, 1300.0), (0.0, 89.99999818714215, -0.0), (1.0, 1.0, 1.0), "City_Trim_C_3m10", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (-4.9956055, 3764.992, 1300.0), (0.0, 89.99999818714215, -0.0), (1.0, 1.0, 1.0), "City_Trim_C_3m11", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (895.004, 3764.9917, 1300.0), (0.0, 89.99999818714215, -0.0), (1.0, 1.0, 1.0), "City_Trim_C_3m12", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3490.013, 615.0099, 1299.943), (0.0013796979951564388, 89.99998684573902, -0.0006103514336138705), (1.0, 1.0, 1.0), "City_Trim_C_3m13", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3190.013, 615.0099, 1299.9462), (0.0013796979951564388, 89.99998684573902, -0.0006103514336138705), (1.0, 1.0, 1.0), "City_Trim_C_3m14", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2890.0132, 615.00995, 1299.9492), (0.0013796979951564388, 89.99998684573902, -0.0006103514336138705), (1.0, 1.0, 1.0), "City_Trim_C_3m15", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2590.0132, 615.00995, 1299.9523), (0.0013796979951564388, 89.99998684573902, -0.0006103514336138705), (1.0, 1.0, 1.0), "City_Trim_C_3m16", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3785.0059, 300.00427, 1299.9357), (-3.051757709276941e-05, 2.3446338272994156e-20, 1.0983785425068692e-06), (1.0, 1.0, 1.0), "City_Trim_C_3m17", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3785.0059, 600.0046, 1299.9358), (-3.051757709276941e-05, 2.3446338272994156e-20, 1.0983785425068692e-06), (1.0, 1.0, 1.0), "City_Trim_C_3m18", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2605.0059, 300.01434, 1299.9557), (0.00210413478007773, -179.9998633962208, -0.00018310547530916906), (1.0, 1.0, 1.0), "City_Trim_C_3m19", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1155.0, 3210.0, 1300.0), (0.0, 0.0, -0.0), (1.0, 1.0, 1.0), "City_Trim_C_3m2", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2605.006, 0.013841808, 1299.9568), (0.00210413478007773, -179.9998633962208, -0.00018310547530916906), (1.0, 1.0, 1.0), "City_Trim_C_3m20", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1155.0, 3510.0, 1300.0), (0.0, 0.0, -0.0), (1.0, 1.0, 1.0), "City_Trim_C_3m3", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1155.0, 3810.0, 1300.0), (0.0, 0.0, -0.0), (1.0, 1.0, 1.0), "City_Trim_C_3m4", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (604.99585, 2635.008, 1300.0), (0.0, -89.99999818714215, 0.0), (1.0, 1.0, 1.0), "City_Trim_C_3m5_999", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (904.99567, 2635.0078, 1300.0), (0.0, -89.99999818714215, 0.0), (1.0, 1.0, 1.0), "City_Trim_C_3m6_1000", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1204.9957, 2635.008, 1300.0), (0.0, -89.99999818714215, 0.0), (1.0, 1.0, 1.0), "City_Trim_C_3m7_1001", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (304.99585, 2635.008, 1300.0), (0.0, -89.99999818714215, 0.0), (1.0, 1.0, 1.0), "City_Trim_C_3m8_1020", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (595.00415, 3764.992, 1300.0), (0.0, 89.99999818714215, -0.0), (1.0, 1.0, 1.0), "City_Trim_C_3m9", _folder)
if a: placed += 1
else: skipped += 1

# Batch 3: StaticMesh'NonD_Arch_Half_3m_A' (2 instances)
_mesh_path = "/Game/Art/Assets/Kits/Architecture/Non_D/NonD_Arch_Half_3m_A"
_materials = ['/Game/Art/Assets/Kits/Architecture/Suburbs/Materials/Suburbs_Trim_Sheet_A/MI_Suburbs_Trim_Sheet_A']
_folder = "Reconstruction/BD_BB_OrcPrison/Meshes"
a = spawn_static_mesh(_mesh_path, _materials, (3545.0, 2450.0, 1200.0), (0.0, -89.99999818714215, 0.0), (1.0, 1.0, 1.0), "NonD_Arch_Half_A7", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2905.0, 2450.0, 1200.0), (0.0, -89.99999818714215, 0.0), (1.0, 1.0, 1.0), "NonD_Arch_Half_A9", _folder)
if a: placed += 1
else: skipped += 1

# Batch 4: StaticMesh'NonD_Arch_Half_3m_C' (10 instances)
_mesh_path = "/Game/Art/Assets/Kits/Architecture/Non_D/NonD_Arch_Half_3m_C"
_materials = ['/Game/Art/Assets/Kits/Architecture/Suburbs/Materials/Suburbs_Trim_Sheet_A/MI_Suburbs_Trim_Sheet_A']
_folder = "Reconstruction/BD_BB_OrcPrison/Meshes"
a = spawn_static_mesh(_mesh_path, _materials, (1220.0, 3415.0, 700.0), (0.0, -89.99999818714215, 0.0), (1.0, 1.0, 1.0), "BP_Suburbs_Wall_Thin_Arch_Half_C10", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2965.0, 670.0, 730.0), (0.0, 0.0, -0.0), (1.0, 1.0, 1.0), "BP_Suburbs_Wall_Thin_Arch_Half_C11", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3465.0, 670.0, 730.0), (0.0, -179.9999795094293, 0.0), (1.0, 1.0, 1.0), "BP_Suburbs_Wall_Thin_Arch_Half_C12_753", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2955.0, 2965.0, 700.0), (0.0, 0.0, -0.0), (1.0, 1.0, 1.0), "BP_Suburbs_Wall_Thin_Arch_Half_C7", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3455.0, 2965.0, 700.0), (0.0, -179.9999795094293, 0.0), (1.0, 1.0, 1.0), "BP_Suburbs_Wall_Thin_Arch_Half_C8_391", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1220.0, 2915.0, 700.0), (0.0, 90.0000030488508, -0.0), (1.0, 1.0, 1.0), "BP_Suburbs_Wall_Thin_Arch_Half_C9", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2905.0, 2050.0, 700.0), (0.0, 89.99999818714215, -0.0), (1.0, 1.0, 1.0), "NonD_Arch_Half_A10", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2905.0, 2850.0, 700.0), (0.0, -89.99997063746636, 0.0), (1.0, 1.0, 1.0), "NonD_Arch_Half_A11", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3545.0, 2050.0, 700.0), (0.0, 89.99999818714215, -0.0), (1.0, 1.0, 1.0), "NonD_Arch_Half_A6_703", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3545.0, 2850.0, 700.0), (0.0, -89.99997063746636, 0.0), (1.0, 1.0, 1.0), "NonD_Arch_Half_A8_705", _folder)
if a: placed += 1
else: skipped += 1

# Batch 5: StaticMesh'NonD_Arch_Half_A' (10 instances)
_mesh_path = "/Game/Art/Assets/Kits/Architecture/Non_D/NonD_Arch_Half_A"
_materials = ['/Game/Art/Assets/Kits/Architecture/Suburbs/Materials/Suburbs_Trim_Sheet_A/MI_Suburbs_Trim_Sheet_A']
_folder = "Reconstruction/BD_BB_OrcPrison/Meshes"
a = spawn_static_mesh(_mesh_path, _materials, (1220.0, 3415.0, 1000.0), (0.0, -89.99999818714215, 0.0), (1.0, 1.0, 1.0), "BP_Suburbs_Wall_Thin_Arch_Half_D10", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2965.0, 670.0, 1030.0), (0.0, 0.0, -0.0), (1.0, 1.0, 1.0), "BP_Suburbs_Wall_Thin_Arch_Half_D11", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3465.0, 670.0, 1030.0), (0.0, -179.9999590188648, 0.0), (1.0, 1.0, 1.0), "BP_Suburbs_Wall_Thin_Arch_Half_D12", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3545.0, 2050.0, 1000.0), (0.0, 90.0000030488508, -0.0), (1.0, 1.0, 1.0), "BP_Suburbs_Wall_Thin_Arch_Half_D3_6", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3545.0, 2850.0, 1000.0), (0.0, -89.99999818714215, 0.0), (1.0, 1.0, 1.0), "BP_Suburbs_Wall_Thin_Arch_Half_D4", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2905.0, 2850.0, 1000.0), (0.0, -89.99999818714215, 0.0), (1.0, 1.0, 1.0), "BP_Suburbs_Wall_Thin_Arch_Half_D5", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2905.0, 2050.0, 1000.0), (0.0, 90.0000030488508, -0.0), (1.0, 1.0, 1.0), "BP_Suburbs_Wall_Thin_Arch_Half_D6", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2955.0, 2965.0, 1000.0), (0.0, 0.0, -0.0), (1.0, 1.0, 1.0), "BP_Suburbs_Wall_Thin_Arch_Half_D7", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3455.0, 2965.0, 1000.0), (0.0, -179.9999590188648, 0.0), (1.0, 1.0, 1.0), "BP_Suburbs_Wall_Thin_Arch_Half_D8", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1220.0, 2915.0, 1000.0), (0.0, 90.0000030488508, -0.0), (1.0, 1.0, 1.0), "BP_Suburbs_Wall_Thin_Arch_Half_D9", _folder)
if a: placed += 1
else: skipped += 1

# Batch 6: StaticMesh'NonD_Stairs_Trim_A_L' (1 instances)
_mesh_path = "/Game/Art/Assets/Kits/Architecture/Non_D/NonD_Stairs_Trim_A_L"
_materials = ['/Game/Art/Assets/Kits/Architecture/Suburbs/Materials/Suburbs_Trim_Sheet_A/MI_Suburbs_Trim_Sheet_A', '/Game/Environments/Materials/MI_Suburbs_Non_Destructible']
_folder = "Reconstruction/BD_BB_OrcPrison/Meshes"
a = spawn_static_mesh(_mesh_path, _materials, (1930.0, 4520.0, 590.0), (0.0, 0.0, -0.0), (0.5, 0.625, 0.5), "NonD_Stairs_Trim_A_R2", _folder)
if a: placed += 1
else: skipped += 1

# Batch 7: StaticMesh'NonD_Stairs_Trim_A_R' (1 instances)
_mesh_path = "/Game/Art/Assets/Kits/Architecture/Non_D/NonD_Stairs_Trim_A_R"
_materials = ['/Game/Art/Assets/Kits/Architecture/Suburbs/Materials/Suburbs_Trim_Sheet_A/MI_Suburbs_Trim_Sheet_A', '/Game/Environments/Materials/MI_Suburbs_Non_Destructible']
_folder = "Reconstruction/BD_BB_OrcPrison/Meshes"
a = spawn_static_mesh(_mesh_path, _materials, (1930.0, 4230.0, 590.0), (0.0, 0.0, -0.0), (0.5, 0.625, 0.5), "NonD_Stairs_Trim_A_R_129", _folder)
if a: placed += 1
else: skipped += 1

# Batch 8: StaticMesh'NonDest_Boundry_1m_Trim_A' (18 instances)
_mesh_path = "/Game/Art/Assets/Kits/Architecture/Non_D/NonDest_Boundry_1m_Trim_A"
_materials = ['/Game/Art/Assets/Kits/Architecture/Suburbs/Materials/Suburbs_Trim_Sheet_A/MI_Suburbs_Trim_Sheet_A']
_folder = "Reconstruction/BD_BB_OrcPrison/Meshes"
a = spawn_static_mesh(_mesh_path, _materials, (2389.995, 5139.993, 705.01), (-0.00042724611278045625, 0.00012207035209686198, -89.99920897394861), (1.0, 0.375, 1.0), "Suburb_Stairs_Trim_3M_B100", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2029.9973, 3630.0007, 1015.0107), (-0.00042724601064604925, -179.99988388673574, -89.99922517928317), (1.0, 0.625, 1.0), "Suburb_Stairs_Trim_3M_B115_355", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2049.996, 3644.997, 1285.0109), (-0.00042724601064604925, -179.99988388673574, -89.99922517928317), (1.0, 0.625, 1.0), "Suburb_Stairs_Trim_3M_B116", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2939.9968, 2955.004, 1285.0156), (-0.00042513553631806276, 90.00012032181498, -89.99919786315024), (1.0, 0.625, 1.0), "Suburb_Stairs_Trim_3M_B117", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2884.998, 2969.9932, 1250.015), (-0.00039362316539664826, -89.9998395787758, -89.99913598416192), (1.0, 0.625, 1.0), "Suburb_Stairs_Trim_3M_B197", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2949.9968, 715.0039, 1295.0156), (-0.00042513553631806276, 90.00012032181498, -89.99919786315024), (1.40625, 0.625, 1.0), "Suburb_Stairs_Trim_3M_B218", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3059.9946, 5119.993, 1015.0107), (-0.00042724611278045625, 0.00012207035209686198, -89.99920897394861), (1.40625, 0.625, 1.0), "Suburb_Stairs_Trim_3M_B85_224", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3069.9946, 5209.993, 1015.0107), (-0.0003964876555005003, -89.99988312289973, -89.99920703038926), (1.0, 0.625, 1.0), "Suburb_Stairs_Trim_3M_B86_227", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3099.995, 5129.993, 1030.0106), (-0.00042724611278045625, 0.00012207035209686198, -89.99920897394861), (1.0, 0.625, 1.0), "Suburb_Stairs_Trim_3M_B87", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3109.995, 5129.993, 1005.0106), (-0.00042724611278045625, 0.00012207035209686198, -89.99920897394861), (1.0, 0.625, 1.0), "Suburb_Stairs_Trim_3M_B88", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3099.996, 5129.997, 1250.0103), (-0.00042724611278045625, 0.00012207035209686198, -89.99920897394861), (1.0, 0.625, 1.0), "Suburb_Stairs_Trim_3M_B89", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3099.995, 5139.993, 695.0106), (-0.00042724611278045625, 0.00012207035209686198, -89.99920897394861), (1.0, 0.21875, 1.0), "Suburb_Stairs_Trim_3M_B90", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3099.995, 5139.993, 605.0106), (-0.00042724611278045625, 0.00012207035209686198, -89.99920897394861), (1.0, 0.625, 1.0), "Suburb_Stairs_Trim_3M_B91", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2299.9946, 5119.993, 1015.0107), (-0.00042724611278045625, 0.00012207035209686198, -89.99920897394861), (1.40625, 0.625, 1.0), "Suburb_Stairs_Trim_3M_B92", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2339.995, 5129.993, 1005.0106), (-0.00042724611278045625, 0.00012207035209686198, -89.99920897394861), (1.0, 0.625, 1.0), "Suburb_Stairs_Trim_3M_B93", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2309.996, 5129.997, 1250.0103), (-0.00042724611278045625, 0.00012207035209686198, -89.99920897394861), (1.0, 0.625, 1.0), "Suburb_Stairs_Trim_3M_B94", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2309.995, 5139.993, 695.0106), (-0.00042724611278045625, 0.00012207035209686198, -89.99920897394861), (1.0, 0.21875, 1.0), "Suburb_Stairs_Trim_3M_B95", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2409.9946, 5209.993, 1015.0107), (-0.0003964876555005003, -89.99988312289973, -89.99920703038926), (1.0, 0.625, 1.0), "Suburb_Stairs_Trim_3M_B97", _folder)
if a: placed += 1
else: skipped += 1

# Batch 9: StaticMesh'NonDest_Boundry_2m_Trim_A' (5 instances)
_mesh_path = "/Game/Art/Assets/Kits/Architecture/Non_D/NonDest_Boundry_2m_Trim_A"
_materials = ['/Game/Art/Assets/Kits/Architecture/Suburbs/Materials/Suburbs_Trim_Sheet_A/MI_Suburbs_Trim_Sheet_A']
_folder = "Reconstruction/BD_BB_OrcPrison/Meshes"
a = spawn_static_mesh(_mesh_path, _materials, (2925.0007, 1525.0027, 1025.015), (-0.00042513553631806276, 90.00012032181498, -89.99919786315024), (1.0, 0.625, 1.0), "Suburb_Stairs_Trim_3M_B201", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3520.9927, 2022.0051, 1025.015), (-0.0003964876555005003, -89.99988312289973, -89.99920703038926), (0.96875, 0.625, 1.0), "Suburb_Stairs_Trim_3M_B210", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2925.0007, 715.0027, 1025.015), (-0.00042513553631806276, 90.00012032181498, -89.99919786315024), (0.8125, 0.625, 1.0), "Suburb_Stairs_Trim_3M_B225", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3526.0007, 1165.0027, 1025.015), (-0.0003964876555005003, -89.99988312289973, -89.99920703038926), (0.8125, 0.625, 1.0), "Suburb_Stairs_Trim_3M_B232", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1955.0012, 5115.0024, 715.0103), (-0.00039672843504230264, -179.99988388673557, -89.99901450669435), (0.981542, 0.625, 1.0), "Suburb_Stairs_Trim_3M_B343", _folder)
if a: placed += 1
else: skipped += 1

# Batch 10: StaticMesh'NonDest_Boundry_3m_Trim_A' (328 instances)
_mesh_path = "/Game/Art/Assets/Kits/Architecture/Non_D/NonDest_Boundry_3m_Trim_A"
_materials = ['/Game/Art/Assets/Kits/Architecture/Suburbs/Materials/Suburbs_Trim_Sheet_A/MI_Suburbs_Trim_Sheet_A']
_folder = "Reconstruction/BD_BB_OrcPrison/Meshes"
a = spawn_static_mesh(_mesh_path, _materials, (2000.0005, 5169.9995, 700.0125), (-0.0004577636793152382, 0.00012207030837304698, 1.633245757340137e-11), (1.0, 1.0, 1.0), "Suburb_Stairs_Trim_3M_B10", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3200.0005, 5169.9995, 700.0125), (-0.0004577636793152208, 0.0001220703083731122, 9.14377842814236e-18), (1.0, 1.0, 1.0), "Suburb_Stairs_Trim_3M_B101", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3545.0005, 5124.9995, 700.0125), (-0.0004577637052479612, -89.99988150712804, -4.226869378473826e-12), (1.0, 1.0, 1.0), "Suburb_Stairs_Trim_3M_B102", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3545.0005, 4824.9995, 700.0125), (-0.0004577637052479612, -89.99988150712804, -4.226869378473826e-12), (1.0, 1.0, 1.0), "Suburb_Stairs_Trim_3M_B103", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1954.9995, 4514.9995, 700.01245), (-0.00045776365180751316, 90.00011648969011, -1.5566598688098243e-11), (1.0, 1.0, 1.0), "Suburb_Stairs_Trim_3M_B104", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1954.9995, 4834.9995, 700.01245), (-0.00045776365180751316, 90.00011648969011, -1.5566598688098243e-11), (1.0, 1.0, 1.0), "Suburb_Stairs_Trim_3M_B105", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2925.0007, 3340.0027, 1015.0127), (-0.00042513553631806276, 90.00012032181498, -89.99919786315024), (1.0, 0.625, 1.0), "Suburb_Stairs_Trim_3M_B106", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2925.0007, 3040.0027, 1015.015), (-0.00042513553631806276, 90.00012032181498, -89.99919786315024), (1.0, 0.625, 1.0), "Suburb_Stairs_Trim_3M_B107", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2915.0007, 3305.003, 1030.0127), (-0.00042513553631806276, 90.00012032181498, -89.99919786315024), (1.0, 0.625, 1.0), "Suburb_Stairs_Trim_3M_B108", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2915.0005, 3005.003, 1030.015), (-0.00042513553631806276, 90.00012032181498, -89.99919786315024), (1.0, 0.625, 1.0), "Suburb_Stairs_Trim_3M_B109", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2915.0007, 3305.003, 1005.0127), (-0.00042513553631806276, 90.00012032181498, -89.99919786315024), (1.0, 0.625, 1.0), "Suburb_Stairs_Trim_3M_B110", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2914.9973, 3305.004, 1250.0127), (-0.00042513553631806276, 90.00012032181498, -89.99919786315024), (1.0, 0.625, 1.0), "Suburb_Stairs_Trim_3M_B111", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2914.997, 3005.004, 1250.015), (-0.00042513553631806276, 90.00012032181498, -89.99919786315024), (1.0, 0.625, 1.0), "Suburb_Stairs_Trim_3M_B112", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2939.997, 3355.004, 1285.0133), (-0.00042513553631806276, 90.00012032181498, -89.99919786315024), (1.0, 0.625, 1.0), "Suburb_Stairs_Trim_3M_B113", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2939.9968, 3055.004, 1285.0156), (-0.00042513553631806276, 90.00012032181498, -89.99919786315024), (1.0, 0.625, 1.0), "Suburb_Stairs_Trim_3M_B114", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3495.9995, 3606.997, 1015.0103), (-0.0003964876555005003, -89.99988312289973, -89.99920703038926), (1.0, 0.625, 1.0), "Suburb_Stairs_Trim_3M_B118", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3499.9998, 3604.997, 1030.0103), (-0.0003964876555005003, -89.99988312289973, -89.99920703038926), (1.0, 0.625, 1.0), "Suburb_Stairs_Trim_3M_B119", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3499.9998, 3604.997, 1005.01025), (-0.0003964876555005003, -89.99988312289973, -89.99920703038926), (1.0, 0.625, 1.0), "Suburb_Stairs_Trim_3M_B120", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3495.003, 3609.996, 1250.0099), (-0.0003964876555005003, -89.99988312289973, -89.99920703038926), (1.0, 0.625, 1.0), "Suburb_Stairs_Trim_3M_B121", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3470.0034, 3609.996, 1285.0105), (-0.0003964876555005003, -89.99988312289973, -89.99920703038926), (1.0, 0.625, 1.0), "Suburb_Stairs_Trim_3M_B122", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3495.9998, 3306.997, 1015.0103), (-0.0003964876555005003, -89.99988312289973, -89.99920703038926), (1.0, 0.625, 1.0), "Suburb_Stairs_Trim_3M_B123", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3499.9995, 3319.997, 1030.0103), (-0.0003964876555005003, -89.99988312289973, -89.99920703038926), (1.0, 0.625, 1.0), "Suburb_Stairs_Trim_3M_B124", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3495.003, 3309.9956, 1250.0099), (-0.0003964876555005003, -89.99988312289973, -89.99920703038926), (1.0, 0.625, 1.0), "Suburb_Stairs_Trim_3M_B125", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3470.003, 3309.996, 1285.0105), (-0.0003964876555005003, -89.99988312289973, -89.99920703038926), (1.0, 0.625, 1.0), "Suburb_Stairs_Trim_3M_B126", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3545.0005, 3609.9995, 700.0125), (-0.0004577637052479612, -89.99988150712804, -4.226869378473826e-12), (1.0, 1.0, 1.0), "Suburb_Stairs_Trim_3M_B127", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3545.0005, 3324.9995, 700.0125), (-0.0004577637052479612, -89.99988150712804, -4.226869378473826e-12), (1.0, 1.0, 1.0), "Suburb_Stairs_Trim_3M_B128", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3495.9995, 3906.997, 1015.0103), (-0.0003964876555005003, -89.99988312289973, -89.99920703038926), (1.0, 0.625, 1.0), "Suburb_Stairs_Trim_3M_B129", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3499.9998, 3904.997, 1030.0103), (-0.0003964876555005003, -89.99988312289973, -89.99920703038926), (1.0, 0.625, 1.0), "Suburb_Stairs_Trim_3M_B130", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3499.9998, 3904.997, 1005.01025), (-0.0003964876555005003, -89.99988312289973, -89.99920703038926), (1.0, 0.625, 1.0), "Suburb_Stairs_Trim_3M_B131", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3495.003, 3909.996, 1250.0099), (-0.0003964876555005003, -89.99988312289973, -89.99920703038926), (1.0, 0.625, 1.0), "Suburb_Stairs_Trim_3M_B132", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3470.0034, 3909.996, 1285.0105), (-0.0003964876555005003, -89.99988312289973, -89.99920703038926), (1.0, 0.625, 1.0), "Suburb_Stairs_Trim_3M_B133", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3545.0005, 3909.9995, 700.0125), (-0.0004577637052479612, -89.99988150712804, -4.226869378473826e-12), (1.0, 1.0, 1.0), "Suburb_Stairs_Trim_3M_B134", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3470.0034, 4209.996, 1285.0105), (-0.0003964876555005003, -89.99988312289973, -89.99920703038926), (1.0, 0.625, 1.0), "Suburb_Stairs_Trim_3M_B135", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3470.0034, 4509.996, 1285.0105), (-0.0003964876555005003, -89.99988312289973, -89.99920703038926), (1.0, 0.625, 1.0), "Suburb_Stairs_Trim_3M_B136", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3189.9968, 3005.004, 1285.0156), (-0.0004272460422339232, -179.99988388675175, -89.99919276818058), (1.0, 0.625, 1.0), "Suburb_Stairs_Trim_3M_B137_434", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3489.9968, 3005.004, 1285.0156), (-0.0004272460422339232, -179.99988388675175, -89.99919276818058), (1.0, 0.625, 1.0), "Suburb_Stairs_Trim_3M_B138", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3200.003, 4839.996, 1310.0105), (-0.0003964876555005003, -89.99988312289973, -89.99920703038926), (1.0, 0.625, 1.0), "Suburb_Stairs_Trim_3M_B139", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3200.003, 4539.996, 1310.0105), (-0.0003964876555005003, -89.99988312289973, -89.99920703038926), (1.0, 0.625, 1.0), "Suburb_Stairs_Trim_3M_B140", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3200.003, 4239.996, 1310.0105), (-0.0003964876555005003, -89.99988312289973, -89.99920703038926), (1.125, 0.625, 1.0), "Suburb_Stairs_Trim_3M_B141", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3200.003, 4839.996, 1380.0105), (-0.0003964876555005003, -89.99988312289973, -89.99920703038926), (1.0, 0.625, 1.0), "Suburb_Stairs_Trim_3M_B142", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3200.003, 4539.996, 1380.0105), (-0.0003964876555005003, -89.99988312289973, -89.99920703038926), (1.0, 0.625, 1.0), "Suburb_Stairs_Trim_3M_B143", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3200.003, 4239.996, 1380.0105), (-0.0003964876555005003, -89.99988312289973, -89.99920703038926), (1.125, 0.625, 1.0), "Suburb_Stairs_Trim_3M_B144", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3160.003, 4839.996, 1410.0105), (-0.0003964876555005003, -89.99988312289973, -89.99920703038926), (1.0, 0.625, 1.0), "Suburb_Stairs_Trim_3M_B145", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3160.003, 4539.996, 1410.0105), (-0.0003964876555005003, -89.99988312289973, -89.99920703038926), (1.0, 0.625, 1.0), "Suburb_Stairs_Trim_3M_B146", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3160.003, 4239.996, 1410.0105), (-0.0003964876555005003, -89.99988312289973, -89.99920703038926), (1.125, 0.625, 1.0), "Suburb_Stairs_Trim_3M_B147", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2300.003, 3899.996, 1310.0105), (-0.00039706063174892154, 90.00011230072788, -89.99913254620981), (1.0, 0.625, 1.0), "Suburb_Stairs_Trim_3M_B148", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2300.003, 4199.996, 1310.0105), (-0.00039706063174892154, 90.00011230072788, -89.99913254620981), (1.0, 0.625, 1.0), "Suburb_Stairs_Trim_3M_B149", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2300.0032, 4499.996, 1310.0105), (-0.00039706063174892154, 90.00011230072788, -89.99913254620981), (1.125, 0.625, 1.0), "Suburb_Stairs_Trim_3M_B150", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2300.003, 3899.996, 1380.0105), (-0.00039706063174892154, 90.00011230072788, -89.99913254620981), (1.0, 0.625, 1.0), "Suburb_Stairs_Trim_3M_B151", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2300.003, 4199.996, 1380.0105), (-0.00039706063174892154, 90.00011230072788, -89.99913254620981), (1.0, 0.625, 1.0), "Suburb_Stairs_Trim_3M_B152", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2300.0032, 4499.996, 1380.0105), (-0.00039706063174892154, 90.00011230072788, -89.99913254620981), (1.125, 0.625, 1.0), "Suburb_Stairs_Trim_3M_B153", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2340.003, 3899.996, 1410.0105), (-0.00039706063174892154, 90.00011230072788, -89.99913254620981), (1.0, 0.625, 1.0), "Suburb_Stairs_Trim_3M_B154", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2340.003, 4199.996, 1410.0105), (-0.00039706063174892154, 90.00011230072788, -89.99913254620981), (1.0, 0.625, 1.0), "Suburb_Stairs_Trim_3M_B155", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2340.003, 4499.996, 1410.0105), (-0.00039706063174892154, 90.00011230072788, -89.99913254620981), (1.125, 0.625, 1.0), "Suburb_Stairs_Trim_3M_B156", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3220.003, 3929.996, 1310.03), (-0.00039672842542676337, -179.9998838867399, -89.99912794565678), (1.0, 0.625, 1.0), "Suburb_Stairs_Trim_3M_B157", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2920.003, 3929.996, 1310.03), (-0.00039672842542676337, -179.9998838867399, -89.99912794565678), (1.0, 0.625, 1.0), "Suburb_Stairs_Trim_3M_B158", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2620.003, 3929.996, 1310.03), (-0.00039672842542676337, -179.9998838867399, -89.99912794565678), (1.125, 0.625, 1.0), "Suburb_Stairs_Trim_3M_B159", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3220.003, 3929.996, 1380.03), (-0.00039672842542676337, -179.9998838867399, -89.99912794565678), (1.0, 0.625, 1.0), "Suburb_Stairs_Trim_3M_B160", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2920.003, 3929.996, 1380.03), (-0.00039672842542676337, -179.9998838867399, -89.99912794565678), (1.0, 0.625, 1.0), "Suburb_Stairs_Trim_3M_B161", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2620.003, 3929.996, 1380.03), (-0.00039672842542676337, -179.9998838867399, -89.99912794565678), (1.125, 0.625, 1.0), "Suburb_Stairs_Trim_3M_B162", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3220.003, 3969.996, 1410.03), (-0.00039672842542676337, -179.9998838867399, -89.99912794565678), (1.0, 0.625, 1.0), "Suburb_Stairs_Trim_3M_B163", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2920.003, 3969.996, 1410.03), (-0.00039672842542676337, -179.9998838867399, -89.99912794565678), (1.0, 0.625, 1.0), "Suburb_Stairs_Trim_3M_B164", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2620.003, 3969.996, 1410.03), (-0.00039672842542676337, -179.9998838867399, -89.99912794565678), (1.125, 0.625, 1.0), "Suburb_Stairs_Trim_3M_B165", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2280.003, 4829.996, 1310.03), (-0.0003967284966345788, 0.0001220702984819684, -89.99907932914093), (1.0, 0.625, 1.0), "Suburb_Stairs_Trim_3M_B166", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2580.003, 4829.996, 1310.03), (-0.0003967284966345788, 0.0001220702984819684, -89.99907932914093), (1.0, 0.625, 1.0), "Suburb_Stairs_Trim_3M_B167", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2880.003, 4829.996, 1310.03), (-0.0003967284966345788, 0.0001220702984819684, -89.99907932914093), (1.125, 0.625, 1.0), "Suburb_Stairs_Trim_3M_B168", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2280.003, 4829.996, 1380.03), (-0.0003967284966345788, 0.0001220702984819684, -89.99907932914093), (1.0, 0.625, 1.0), "Suburb_Stairs_Trim_3M_B169", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2580.003, 4829.996, 1380.03), (-0.0003967284966345788, 0.0001220702984819684, -89.99907932914093), (1.0, 0.625, 1.0), "Suburb_Stairs_Trim_3M_B170", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2880.003, 4829.996, 1380.03), (-0.0003967284966345788, 0.0001220702984819684, -89.99907932914093), (1.125, 0.625, 1.0), "Suburb_Stairs_Trim_3M_B171", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2280.003, 4789.996, 1410.03), (-0.0003967284966345788, 0.0001220702984819684, -89.99907932914093), (1.0, 0.625, 1.0), "Suburb_Stairs_Trim_3M_B172", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2580.003, 4789.996, 1410.03), (-0.0003967284966345788, 0.0001220702984819684, -89.99907932914093), (1.0, 0.625, 1.0), "Suburb_Stairs_Trim_3M_B173", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2880.003, 4789.996, 1410.03), (-0.0003967284966345788, 0.0001220702984819684, -89.99907932914093), (1.125, 0.625, 1.0), "Suburb_Stairs_Trim_3M_B174", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2915.0007, 3005.003, 1005.0127), (-0.00042513553631806276, 90.00012032181498, -89.99919786315024), (1.0, 0.625, 1.0), "Suburb_Stairs_Trim_3M_B175", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2444.9973, 2945.0042, 700.0125), (-0.0004577636793152263, 0.00012207030837309164, 5.1495819192400755e-12), (1.0, 1.0, 1.0), "Suburb_Stairs_Trim_3M_B176", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2925.0007, 1685.0027, 1025.015), (-0.00042513553631806276, 90.00012032181498, -89.99919786315024), (1.0, 0.625, 1.0), "Suburb_Stairs_Trim_3M_B177_680", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2920.0005, 1565.0029, 1040.015), (-0.00042513553631806276, 90.00012032181498, -89.99919786315024), (1.2700297, 0.625, 1.0), "Suburb_Stairs_Trim_3M_B178_681", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2595.0017, 2930.0066, 1250.015), (-0.00042724611278045625, 0.00012207035209686198, -89.99920897394861), (1.0, 0.625, 1.0), "Suburb_Stairs_Trim_3M_B179", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2595.0017, 2905.0068, 1285.0156), (-0.00042724611278045625, 0.00012207035209686198, -89.99920897394861), (1.0, 0.625, 1.0), "Suburb_Stairs_Trim_3M_B180", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2594.9983, 1999.9932, 1250.015), (-0.00039672843293137006, -179.99988388677218, -89.9991668390883), (1.0, 0.625, 1.0), "Suburb_Stairs_Trim_3M_B181_589", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2594.9983, 2024.9929, 1285.0156), (-0.00039672843293137006, -179.99988388677218, -89.9991668390883), (1.0, 0.625, 1.0), "Suburb_Stairs_Trim_3M_B182_590", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2864.998, 2294.9932, 1285.0156), (-0.00039362316539664826, -89.9998395787758, -89.99913598416192), (1.0, 0.625, 1.0), "Suburb_Stairs_Trim_3M_B183_607", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2295.0017, 2930.0066, 1250.015), (-0.00042724611278045625, 0.00012207035209686198, -89.99920897394861), (1.0, 0.625, 1.0), "Suburb_Stairs_Trim_3M_B184", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2295.0017, 2905.0068, 1285.0156), (-0.00042724611278045625, 0.00012207035209686198, -89.99920897394861), (1.0, 0.625, 1.0), "Suburb_Stairs_Trim_3M_B185", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2894.998, 1999.9932, 1250.015), (-0.00039672843293137006, -179.99988388677218, -89.9991668390883), (1.0, 0.625, 1.0), "Suburb_Stairs_Trim_3M_B186_591", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2594.9995, 2950.0005, 780.0125), (-0.0004577636793152263, 0.00012207030837309164, 5.1495819192400755e-12), (1.0, 1.0, 1.0), "Suburb_Stairs_Trim_3M_B187", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2294.9995, 2985.0005, 780.0125), (-0.0004577636793152263, 0.00012207030837309164, 5.1495819192400755e-12), (1.0, 1.0, 1.0), "Suburb_Stairs_Trim_3M_B188", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2894.998, 2024.9929, 1285.0156), (-0.00039672843293137006, -179.99988388677218, -89.9991668390883), (1.0, 0.625, 1.0), "Suburb_Stairs_Trim_3M_B189", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2300.0005, 3579.9995, 700.01245), (-0.00045776360601272966, -179.99988388675877, -1.442703368811174e-18), (1.0, 1.0, 1.0), "Suburb_Stairs_Trim_3M_B19", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2595.0005, 1979.9995, 780.0125), (-0.0004577636060127343, -179.99988388675877, 4.534649836613382e-12), (1.0, 1.0, 1.0), "Suburb_Stairs_Trim_3M_B190", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2895.0005, 1979.9995, 780.0125), (-0.0004577636060127343, -179.99988388675877, 4.534649836613382e-12), (1.0, 1.0, 1.0), "Suburb_Stairs_Trim_3M_B191", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2864.998, 2594.993, 1285.0156), (-0.00039362316539664826, -89.9998395787758, -89.99913598416192), (1.0, 0.625, 1.0), "Suburb_Stairs_Trim_3M_B192", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2864.998, 2894.993, 1285.0156), (-0.00039362316539664826, -89.9998395787758, -89.99913598416192), (1.0, 0.625, 1.0), "Suburb_Stairs_Trim_3M_B193", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2884.998, 2269.9932, 1250.015), (-0.00039362316539664826, -89.9998395787758, -89.99913598416192), (1.0, 0.625, 1.0), "Suburb_Stairs_Trim_3M_B194_612", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2884.998, 2569.9932, 1250.015), (-0.00039362316539664826, -89.9998395787758, -89.99913598416192), (1.0, 0.625, 1.0), "Suburb_Stairs_Trim_3M_B195", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2884.998, 2869.9932, 1250.015), (-0.00039362316539664826, -89.9998395787758, -89.99913598416192), (1.0, 0.625, 1.0), "Suburb_Stairs_Trim_3M_B196", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2919.997, 1560.0039, 1260.015), (-0.00042513553631806276, 90.00012032181498, -89.99919786315024), (1.28125, 0.625, 1.0), "Suburb_Stairs_Trim_3M_B198", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2949.9968, 1755.0039, 1295.0156), (-0.00042513553631806276, 90.00012032181498, -89.99919786315024), (1.0, 0.625, 1.0), "Suburb_Stairs_Trim_3M_B199", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2629.9973, 3630.0007, 1015.0127), (-0.00042724601064604925, -179.99988388673574, -89.99922517928317), (1.0, 0.625, 1.0), "Suburb_Stairs_Trim_3M_B20_1", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2920.0059, 1565.0106, 1015.0127), (-0.00042513553631806276, 90.00012032181498, -89.99919786315024), (1.2700297, 0.625, 1.0), "Suburb_Stairs_Trim_3M_B200", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2949.9968, 1455.0039, 1295.0156), (-0.00042513553631806276, 90.00012032181498, -89.99919786315024), (1.0, 0.625, 1.0), "Suburb_Stairs_Trim_3M_B202", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2949.9968, 1155.0039, 1295.0156), (-0.00042513553631806276, 90.00012032181498, -89.99919786315024), (1.0, 0.625, 1.0), "Suburb_Stairs_Trim_3M_B203", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2949.9968, 855.0039, 1295.0156), (-0.00042513553631806276, 90.00012032181498, -89.99919786315024), (1.0, 0.625, 1.0), "Suburb_Stairs_Trim_3M_B204", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3520.9934, 1828.2551, 1025.0122), (-0.0003964876555005003, -89.99988312289973, -89.99920703038926), (0.96875, 0.625, 1.0), "Suburb_Stairs_Trim_3M_B205", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3524.9932, 1935.0049, 1040.015), (-0.0003964876555005003, -89.99988312289973, -89.99920703038926), (1.27003, 0.625, 1.0), "Suburb_Stairs_Trim_3M_B206", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3524.9966, 1940.0039, 1260.015), (-0.0003964876555005003, -89.99988312289973, -89.99920703038926), (1.28125, 0.625, 1.0), "Suburb_Stairs_Trim_3M_B207", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3499.9968, 1795.0039, 1295.0156), (-0.0003964876555005003, -89.99988312289973, -89.99920703038926), (1.0, 0.625, 1.0), "Suburb_Stairs_Trim_3M_B208", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3524.9878, 1934.9973, 1015.0127), (-0.0003964876555005003, -89.99988312289973, -89.99920703038926), (1.27003, 0.625, 1.0), "Suburb_Stairs_Trim_3M_B209", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2929.9973, 3630.0007, 1015.015), (-0.00042724601064604925, -179.99988388673574, -89.99922517928317), (1.0, 0.625, 1.0), "Suburb_Stairs_Trim_3M_B21_11", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3499.9968, 2095.004, 1295.0156), (-0.0003964876555005003, -89.99988312289973, -89.99920703038926), (1.0, 0.625, 1.0), "Suburb_Stairs_Trim_3M_B211", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3499.9968, 2395.004, 1295.0156), (-0.0003964876555005003, -89.99988312289973, -89.99920703038926), (1.0, 0.625, 1.0), "Suburb_Stairs_Trim_3M_B212", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3499.9968, 2695.004, 1295.0156), (-0.0003964876555005003, -89.99988312289973, -89.99920703038926), (1.0, 0.625, 1.0), "Suburb_Stairs_Trim_3M_B213", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3499.9968, 2995.004, 1295.0156), (-0.0003964876555005003, -89.99988312289973, -89.99920703038926), (1.0, 0.625, 1.0), "Suburb_Stairs_Trim_3M_B214", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2949.9968, 2055.004, 1295.0156), (-0.00042513553631806276, 90.00012032181498, -89.99919786315024), (1.0, 0.625, 1.0), "Suburb_Stairs_Trim_3M_B215", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2949.9968, 2355.004, 1295.0156), (-0.00042513553631806276, 90.00012032181498, -89.99919786315024), (1.0, 0.625, 1.0), "Suburb_Stairs_Trim_3M_B216", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2949.9968, 2655.004, 1295.0156), (-0.00042513553631806276, 90.00012032181498, -89.99919786315024), (1.0, 0.625, 1.0), "Suburb_Stairs_Trim_3M_B217", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3224.9968, 2925.004, 1295.0156), (-0.00039672850205489885, 0.0001220703009568705, -89.9991765625792), (1.0, 0.625, 1.0), "Suburb_Stairs_Trim_3M_B219", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2329.9973, 3630.0007, 1015.0107), (-0.00042724601064604925, -179.99988388673574, -89.99922517928317), (1.0, 0.625, 1.0), "Suburb_Stairs_Trim_3M_B22_13", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2924.9968, 2925.004, 1295.0156), (-0.00039672850205489885, 0.0001220703009568705, -89.9991765625792), (1.0, 0.625, 1.0), "Suburb_Stairs_Trim_3M_B220", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2925.0007, 875.0027, 1025.015), (-0.00042513553631806276, 90.00012032181498, -89.99919786315024), (1.0, 0.625, 1.0), "Suburb_Stairs_Trim_3M_B221", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2920.0005, 755.0029, 1040.015), (-0.00042513553631806276, 90.00012032181498, -89.99919786315024), (1.27003, 0.625, 1.0), "Suburb_Stairs_Trim_3M_B222", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2919.997, 750.0039, 1260.015), (-0.00042513553631806276, 90.00012032181498, -89.99919786315024), (1.28125, 0.625, 1.0), "Suburb_Stairs_Trim_3M_B223", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2920.0059, 755.0106, 1015.0127), (-0.00042513553631806276, 90.00012032181498, -89.99919786315024), (1.27003, 0.625, 1.0), "Suburb_Stairs_Trim_3M_B224", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3500.005, 1195.0015, 1295.0156), (-0.0003964876555005003, -89.99988312289973, -89.99920703038926), (1.0, 0.625, 1.0), "Suburb_Stairs_Trim_3M_B226", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3500.005, 1495.0015, 1295.0156), (-0.0003964876555005003, -89.99988312289973, -89.99920703038926), (1.0, 0.625, 1.0), "Suburb_Stairs_Trim_3M_B227", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3526.0005, 1005.0027, 1025.015), (-0.0003964876555005003, -89.99988312289973, -89.99920703038926), (1.0, 0.625, 1.0), "Suburb_Stairs_Trim_3M_B228", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3530.001, 1125.0024, 1040.015), (-0.0003964876555005003, -89.99988312289973, -89.99920703038926), (1.27003, 0.625, 1.0), "Suburb_Stairs_Trim_3M_B229", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2599.997, 3620.0007, 1030.0127), (-0.00042724601064604925, -179.99988388673574, -89.99922517928317), (1.0, 0.625, 1.0), "Suburb_Stairs_Trim_3M_B23", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3530.0044, 1130.0013, 1260.015), (-0.0003964876555005003, -89.99988312289973, -89.99920703038926), (1.28125, 0.625, 1.0), "Suburb_Stairs_Trim_3M_B230", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3529.9956, 1124.9946, 1015.0127), (-0.0003964876555005003, -89.99988312289973, -89.99920703038926), (1.27003, 0.625, 1.0), "Suburb_Stairs_Trim_3M_B231", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3500.005, 895.00146, 1295.0156), (-0.0003964876555005003, -89.99988312289973, -89.99920703038926), (0.7910873, 0.625, 1.0), "Suburb_Stairs_Trim_3M_B233", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3229.9968, 720.0039, 1295.0156), (-0.0004272460422339232, -179.99988388675175, -89.99919276818058), (1.0, 0.625, 1.0), "Suburb_Stairs_Trim_3M_B234_780", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3529.9968, 720.0039, 1295.0156), (-0.0004272460422339232, -179.99988388675175, -89.99919276818058), (1.0, 0.625, 1.0), "Suburb_Stairs_Trim_3M_B235", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3844.9983, 1999.9932, 1250.015), (-0.00039672843293137006, -179.99988388677218, -89.9991668390883), (1.0, 0.625, 1.0), "Suburb_Stairs_Trim_3M_B236", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3844.9983, 2024.9929, 1285.0156), (-0.00039672843293137006, -179.99988388677218, -89.9991668390883), (1.0, 0.625, 1.0), "Suburb_Stairs_Trim_3M_B237", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4144.998, 1999.9932, 1250.015), (-0.00039672843293137006, -179.99988388677218, -89.9991668390883), (1.0, 0.625, 1.0), "Suburb_Stairs_Trim_3M_B238", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4144.998, 2024.9929, 1285.0156), (-0.00039672843293137006, -179.99988388677218, -89.9991668390883), (1.0, 0.625, 1.0), "Suburb_Stairs_Trim_3M_B239", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2899.997, 3620.0007, 1030.015), (-0.00042724601064604925, -179.99988388673574, -89.99922517928317), (1.0, 0.625, 1.0), "Suburb_Stairs_Trim_3M_B24", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3845.0015, 2930.0068, 1250.015), (-0.00039672849478479175, 0.00012588500524997011, -89.99907932915826), (1.0, 0.625, 1.0), "Suburb_Stairs_Trim_3M_B240", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3845.0015, 2905.0073, 1285.0156), (-0.00039672849478479175, 0.00012588500524997011, -89.99907932915826), (1.0, 0.625, 1.0), "Suburb_Stairs_Trim_3M_B241", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3545.002, 2930.007, 1250.015), (-0.00039672849478479175, 0.00012588500524997011, -89.99907932915826), (1.0, 0.625, 1.0), "Suburb_Stairs_Trim_3M_B242", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3545.002, 2905.0073, 1285.0156), (-0.00039672849478479175, 0.00012588500524997011, -89.99907932915826), (1.0, 0.625, 1.0), "Suburb_Stairs_Trim_3M_B243", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3564.998, 2294.9932, 1285.0156), (-0.00039362316539664826, -89.9998395787758, -89.99913598416192), (1.0, 0.625, 1.0), "Suburb_Stairs_Trim_3M_B244", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3564.998, 2594.993, 1285.0156), (-0.00039362316539664826, -89.9998395787758, -89.99913598416192), (1.0, 0.625, 1.0), "Suburb_Stairs_Trim_3M_B245", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3564.998, 2894.993, 1285.0156), (-0.00039362316539664826, -89.9998395787758, -89.99913598416192), (1.0, 0.625, 1.0), "Suburb_Stairs_Trim_3M_B246", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1975.0067, 3464.998, 1250.015), (-0.00039362316539664826, -89.9998395787758, -89.99913598416192), (1.0, 0.625, 1.0), "Suburb_Stairs_Trim_3M_B247", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1950.007, 3464.998, 1285.0156), (-0.00039362316539664826, -89.9998395787758, -89.99913598416192), (1.0, 0.625, 1.0), "Suburb_Stairs_Trim_3M_B248", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1990.0005, 3459.9995, 780.0125), (-0.0004577636518079074, -89.9998409929242, 4.942659843804191e-11), (1.0, 1.0, 1.0), "Suburb_Stairs_Trim_3M_B249", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2299.997, 3620.0007, 1030.0106), (-0.00042724601064604925, -179.99988388673574, -89.99922517928317), (1.0, 0.625, 1.0), "Suburb_Stairs_Trim_3M_B25", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1280.0018, 3505.0059, 1250.015), (-0.00039672850614423834, 0.0001525878797001843, -89.99907932928315), (1.0, 0.625, 1.0), "Suburb_Stairs_Trim_3M_B250", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1280.0018, 3480.006, 1285.0156), (-0.00039672850614423834, 0.0001525878797001843, -89.99907932928315), (1.0, 0.625, 1.0), "Suburb_Stairs_Trim_3M_B251", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1285.0005, 3519.9995, 780.0125), (-0.00045776367931552823, 0.00015258788546640962, 1.1413565621789297e-11), (1.0, 1.0, 1.0), "Suburb_Stairs_Trim_3M_B252", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1610.0018, 3505.0059, 1250.015), (-0.00039672850614423834, 0.0001525878797001843, -89.99907932928315), (1.0, 0.625, 1.0), "Suburb_Stairs_Trim_3M_B253", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1610.0018, 3480.006, 1285.0156), (-0.00039672850614423834, 0.0001525878797001843, -89.99907932928315), (1.0, 0.625, 1.0), "Suburb_Stairs_Trim_3M_B254", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1240.0021, 3160.006, 1250.015), (-0.0003982068582282861, 90.0001489702853, -89.99908556430758), (1.0, 0.625, 1.0), "Suburb_Stairs_Trim_3M_B255_928", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1255.0018, 3160.006, 1285.0156), (-0.0003982068582282861, 90.0001489702853, -89.99908556430758), (1.0, 0.625, 1.0), "Suburb_Stairs_Trim_3M_B256_929", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1240.0021, 2860.006, 1250.015), (-0.0003982068582282861, 90.0001489702853, -89.99908556430758), (1.0, 0.625, 1.0), "Suburb_Stairs_Trim_3M_B257", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1255.0018, 2860.006, 1285.0156), (-0.0003982068582282861, 90.0001489702853, -89.99908556430758), (1.0, 0.625, 1.0), "Suburb_Stairs_Trim_3M_B258", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1200.0017, 2910.006, 1250.015), (-0.0003987796292386944, -89.99988541675346, -89.99902597708711), (1.0, 0.625, 1.0), "Suburb_Stairs_Trim_3M_B259", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2599.997, 3620.0007, 1005.0127), (-0.00042724601064604925, -179.99988388673574, -89.99922517928317), (1.0, 0.625, 1.0), "Suburb_Stairs_Trim_3M_B26", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1185.0018, 2910.006, 1285.0156), (-0.0003987796292386944, -89.99988541675346, -89.99902597708711), (1.0, 0.625, 1.0), "Suburb_Stairs_Trim_3M_B260", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1200.0016, 3210.006, 1250.015), (-0.0003987796292386944, -89.99988541675346, -89.99902597708711), (1.0, 0.625, 1.0), "Suburb_Stairs_Trim_3M_B261", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1185.0018, 3210.006, 1285.0156), (-0.0003987796292386944, -89.99988541675346, -89.99902597708711), (1.0, 0.625, 1.0), "Suburb_Stairs_Trim_3M_B262", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1200.0017, 3510.006, 1250.015), (-0.0003987796292386944, -89.99988541675346, -89.99902597708711), (1.0, 0.625, 1.0), "Suburb_Stairs_Trim_3M_B263", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1185.0018, 3510.006, 1285.0156), (-0.0003987796292386944, -89.99988541675346, -89.99902597708711), (1.0, 0.625, 1.0), "Suburb_Stairs_Trim_3M_B264", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1200.0016, 3810.006, 1250.015), (-0.0003987796292386944, -89.99988541675346, -89.99902597708711), (1.0, 0.625, 1.0), "Suburb_Stairs_Trim_3M_B265", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1185.0018, 3810.006, 1285.0156), (-0.0003987796292386944, -89.99988541675346, -89.99902597708711), (1.0, 0.625, 1.0), "Suburb_Stairs_Trim_3M_B266", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1145.0018, 2905.006, 1415.0156), (-0.0003987796292386944, -89.99988541675346, -89.99902597708711), (1.0, 0.625, 1.0), "Suburb_Stairs_Trim_3M_B267", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1145.0018, 3205.006, 1415.0156), (-0.0003987796292386944, -89.99988541675346, -89.99902597708711), (1.0, 0.625, 1.0), "Suburb_Stairs_Trim_3M_B268", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1145.0018, 3505.006, 1415.0156), (-0.0003987796292386944, -89.99988541675346, -89.99902597708711), (1.0, 0.625, 1.0), "Suburb_Stairs_Trim_3M_B269", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2899.997, 3620.0007, 1005.015), (-0.00042724601064604925, -179.99988388673574, -89.99922517928317), (1.0, 0.625, 1.0), "Suburb_Stairs_Trim_3M_B27", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1145.0018, 3805.006, 1415.0156), (-0.0003987796292386944, -89.99988541675346, -89.99902597708711), (1.0, 0.625, 1.0), "Suburb_Stairs_Trim_3M_B270", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (424.99902, 2584.9924, 1375.015), (-0.0003967284228898501, -179.99983607544706, -89.99907122645115), (1.0, 0.625, 1.0), "Suburb_Stairs_Trim_3M_B271", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1179.999, 2594.9922, 915.0156), (-0.0003967284228898501, -179.99983607544706, -89.99907122645115), (1.0, 0.625, 1.0), "Suburb_Stairs_Trim_3M_B272", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (420.0005, 2569.9985, 905.0125), (-0.00045776360601319647, -179.9998360754275, 3.299705307263858e-17), (1.0, 1.0, 1.0), "Suburb_Stairs_Trim_3M_B273", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (595.0018, 2590.0063, 1250.015), (-0.00039672843504230264, -179.99988388673557, -89.99901450669435), (1.0, 0.625, 1.0), "Suburb_Stairs_Trim_3M_B274", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (595.00183, 2605.0063, 1285.0156), (-0.00039672843504230264, -179.99988388673557, -89.99901450669435), (1.0, 0.625, 1.0), "Suburb_Stairs_Trim_3M_B275", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (895.00195, 2590.0066, 1250.015), (-0.00039672843504230264, -179.99988388673557, -89.99901450669435), (1.0, 0.625, 1.0), "Suburb_Stairs_Trim_3M_B276", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (895.0017, 2605.006, 1285.0156), (-0.00039672843504230264, -179.99988388673557, -89.99901450669435), (1.0, 0.625, 1.0), "Suburb_Stairs_Trim_3M_B277", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1195.0018, 2590.0063, 1250.015), (-0.00039672843504230264, -179.99988388673557, -89.99901450669435), (1.0, 0.625, 1.0), "Suburb_Stairs_Trim_3M_B278", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1195.0018, 2605.006, 1285.0156), (-0.00039672843504230264, -179.99988388673557, -89.99901450669435), (1.0, 0.625, 1.0), "Suburb_Stairs_Trim_3M_B279", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2299.997, 3620.0007, 1005.0106), (-0.00042724601064604925, -179.99988388673574, -89.99922517928317), (1.0, 0.625, 1.0), "Suburb_Stairs_Trim_3M_B28", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (600.00195, 2645.0063, 1415.0156), (-0.00039672843504230264, -179.99988388673557, -89.99901450669435), (1.0, 0.625, 1.0), "Suburb_Stairs_Trim_3M_B280", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (900.0018, 2645.006, 1415.0156), (-0.00039672843504230264, -179.99988388673557, -89.99901450669435), (1.0, 0.625, 1.0), "Suburb_Stairs_Trim_3M_B281", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1200.0018, 2645.006, 1415.0156), (-0.00039672843504230264, -179.99988388673557, -89.99901450669435), (1.0, 0.625, 1.0), "Suburb_Stairs_Trim_3M_B282", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (879.999, 2594.9922, 915.0156), (-0.0003967284228898501, -179.99983607544706, -89.99907122645115), (1.0, 0.625, 1.0), "Suburb_Stairs_Trim_3M_B283", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (579.999, 2594.9922, 915.0156), (-0.0003967284228898501, -179.99983607544706, -89.99907122645115), (1.0, 0.625, 1.0), "Suburb_Stairs_Trim_3M_B284", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (279.99902, 2594.9922, 915.0156), (-0.0003967284228898501, -179.99983607544706, -89.99907122645115), (1.0, 0.625, 1.0), "Suburb_Stairs_Trim_3M_B285", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (295.00177, 2590.0063, 1250.015), (-0.00039672843504230264, -179.99988388673557, -89.99901450669435), (1.0, 0.625, 1.0), "Suburb_Stairs_Trim_3M_B286", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (295.00183, 2605.0063, 1285.0156), (-0.00039672843504230264, -179.99988388673557, -89.99901450669435), (1.0, 0.625, 1.0), "Suburb_Stairs_Trim_3M_B287", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (300.00195, 2645.0063, 1415.0156), (-0.00039672843504230264, -179.99988388673557, -89.99901450669435), (1.0, 0.625, 1.0), "Suburb_Stairs_Trim_3M_B288", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (20.000916, 3805.0078, 915.0156), (-0.0003967285165177382, 0.0001525878986550695, -89.99902260985003), (0.90625, 0.625, 1.0), "Suburb_Stairs_Trim_3M_B289", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2599.996, 3619.9973, 1250.0127), (-0.00042724601064604925, -179.99988388673574, -89.99922517928317), (1.0, 0.625, 1.0), "Suburb_Stairs_Trim_3M_B29", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (604.99805, 3809.9934, 1250.015), (-0.00039672853571019306, 0.00012207033657593038, -89.99899830144759), (1.0, 0.625, 1.0), "Suburb_Stairs_Trim_3M_B290", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (604.9983, 3794.9934, 1285.0156), (-0.00039672853571019306, 0.00012207033657593038, -89.99899830144759), (1.0, 0.625, 1.0), "Suburb_Stairs_Trim_3M_B291", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (304.99805, 3809.9932, 1250.015), (-0.00039672853571019306, 0.00012207033657593038, -89.99899830144759), (1.0, 0.625, 1.0), "Suburb_Stairs_Trim_3M_B292", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (304.9983, 3794.9937, 1285.0156), (-0.00039672853571019306, 0.00012207033657593038, -89.99899830144759), (1.0, 0.625, 1.0), "Suburb_Stairs_Trim_3M_B293", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4.998047, 3809.9937, 1250.015), (-0.00039672853571019306, 0.00012207033657593038, -89.99899830144759), (1.0, 0.625, 1.0), "Suburb_Stairs_Trim_3M_B294", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4.998108, 3794.994, 1285.0156), (-0.00039672853571019306, 0.00012207033657593038, -89.99899830144759), (1.0, 0.625, 1.0), "Suburb_Stairs_Trim_3M_B295", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (599.99805, 3754.9937, 1415.0156), (-0.00039672853571019306, 0.00012207033657593038, -89.99899830144759), (1.0, 0.625, 1.0), "Suburb_Stairs_Trim_3M_B296", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (299.9983, 3754.994, 1415.0156), (-0.00039672853571019306, 0.00012207033657593038, -89.99899830144759), (1.0, 0.625, 1.0), "Suburb_Stairs_Trim_3M_B297", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (-0.0017089844, 3754.9941, 1415.0156), (-0.00039672853571019306, 0.00012207033657593038, -89.99899830144759), (1.0, 0.625, 1.0), "Suburb_Stairs_Trim_3M_B298", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (580.0031, 3805.0059, 915.0156), (-0.0003967285165177382, 0.0001525878986550695, -89.99902260985003), (1.0, 0.625, 1.0), "Suburb_Stairs_Trim_3M_B299_1135", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2899.996, 3619.9973, 1250.015), (-0.00042724601064604925, -179.99988388673574, -89.99922517928317), (1.0, 0.625, 1.0), "Suburb_Stairs_Trim_3M_B30", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (880.0031, 3805.0059, 915.0156), (-0.0003967285165177382, 0.0001525878986550695, -89.99902260985003), (1.0, 0.625, 1.0), "Suburb_Stairs_Trim_3M_B300_1125", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (280.0031, 3805.0059, 915.0156), (-0.00039672850382349096, 0.0001530000094421711, -89.99902260985199), (1.0, 0.625, 1.0), "Suburb_Stairs_Trim_3M_B301_1141", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (904.99805, 3809.9934, 1250.015), (-0.00039672853571019306, 0.00012207033657593038, -89.99899830144759), (1.0, 0.625, 1.0), "Suburb_Stairs_Trim_3M_B302", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (904.9979, 3794.9937, 1285.0156), (-0.00039672853571019306, 0.00012207033657593038, -89.99899830144759), (1.0, 0.625, 1.0), "Suburb_Stairs_Trim_3M_B303", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (899.99805, 3754.9934, 1415.0156), (-0.00039672853571019306, 0.00012207033657593038, -89.99899830144759), (1.0, 0.625, 1.0), "Suburb_Stairs_Trim_3M_B304", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1904.9991, 4524.997, 1015.0127), (-0.0003964876555005003, -89.99988312289973, -89.99920703038926), (1.0, 0.625, 1.0), "Suburb_Stairs_Trim_3M_B305", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1904.9989, 4224.997, 1015.0107), (-0.0003964876555005003, -89.99988312289973, -89.99920703038926), (1.0, 0.625, 1.0), "Suburb_Stairs_Trim_3M_B306", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1914.9996, 4524.997, 1030.0127), (-0.0003964876555005003, -89.99988312289973, -89.99920703038926), (1.0, 0.625, 1.0), "Suburb_Stairs_Trim_3M_B307", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1904.9991, 4824.997, 1015.0127), (-0.0003964876555005003, -89.99988312289973, -89.99920703038926), (1.0, 0.625, 1.0), "Suburb_Stairs_Trim_3M_B308_1218", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1915.0028, 4524.996, 1250.0127), (-0.0003964876555005003, -89.99988312289973, -89.99920703038926), (1.0, 0.625, 1.0), "Suburb_Stairs_Trim_3M_B309", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2299.996, 3619.9973, 1250.0103), (-0.00042724601064604925, -179.99988388673574, -89.99922517928317), (1.0, 0.625, 1.0), "Suburb_Stairs_Trim_3M_B31", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1915.0023, 4224.996, 1250.0103), (-0.0003964876555005003, -89.99988312289973, -89.99920703038926), (1.0, 0.625, 1.0), "Suburb_Stairs_Trim_3M_B310", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1890.0027, 4524.996, 1285.0133), (-0.0003964876555005003, -89.99988312289973, -89.99920703038926), (1.0, 0.625, 1.0), "Suburb_Stairs_Trim_3M_B311", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1890.0029, 4224.996, 1285.0109), (-0.0003964876555005003, -89.99988312289973, -89.99920703038926), (1.0, 0.625, 1.0), "Suburb_Stairs_Trim_3M_B312", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1904.999, 3924.9976, 1015.0103), (-0.0003964876555005003, -89.99988312289973, -89.99920703038926), (1.0, 0.625, 1.0), "Suburb_Stairs_Trim_3M_B313", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1904.9991, 5124.997, 1015.0127), (-0.0003964876555005003, -89.99988312289973, -89.99920703038926), (1.0, 0.625, 1.0), "Suburb_Stairs_Trim_3M_B314_1220", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1915.0024, 3924.996, 1250.0099), (-0.0003964876555005003, -89.99988312289973, -89.99920703038926), (1.0, 0.625, 1.0), "Suburb_Stairs_Trim_3M_B315", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1890.0028, 3924.996, 1285.0105), (-0.0003964876555005003, -89.99988312289973, -89.99920703038926), (1.0, 0.625, 1.0), "Suburb_Stairs_Trim_3M_B316", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1919.9989, 4224.997, 715.0107), (-0.0003964876555005003, -89.99988312289973, -89.99920703038926), (1.0, 0.625, 1.0), "Suburb_Stairs_Trim_3M_B317", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1919.999, 3924.9976, 715.0103), (-0.0003964876555005003, -89.99988312289973, -89.99920703038926), (1.0, 0.625, 1.0), "Suburb_Stairs_Trim_3M_B318", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1610.0012, 3630.8364, 1015.0107), (-0.00039706063174892154, 90.00011230072788, -89.99913254620981), (1.125, 0.625, 1.0), "Suburb_Stairs_Trim_3M_B319", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2649.996, 3644.997, 1285.0133), (-0.00042724601064604925, -179.99988388673574, -89.99922517928317), (1.0, 0.625, 1.0), "Suburb_Stairs_Trim_3M_B32", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1610.0009, 3965.836, 1015.0103), (-0.00039706063174892154, 90.00011230072788, -89.99913254620981), (1.0, 0.625, 1.0), "Suburb_Stairs_Trim_3M_B320", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1590.0012, 3625.003, 715.0107), (-0.00039706063174892154, 90.00011230072788, -89.99913254620981), (1.0, 0.625, 1.0), "Suburb_Stairs_Trim_3M_B321", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1590.0012, 3925.0024, 715.0103), (-0.00039706063174892154, 90.00011230072788, -89.99913254620981), (1.0, 0.625, 1.0), "Suburb_Stairs_Trim_3M_B322", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1905.0012, 3625.003, 1015.0107), (-0.00039672840047415395, -179.99988388673418, -89.99909553442366), (1.0, 0.625, 1.0), "Suburb_Stairs_Trim_3M_B323", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1610.0009, 4265.836, 1015.0103), (-0.00039706063174892154, 90.00011230072788, -89.99913254620981), (1.0, 0.625, 1.0), "Suburb_Stairs_Trim_3M_B324", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1590.0012, 4225.0024, 715.0103), (-0.00039706063174892154, 90.00011230072788, -89.99913254620981), (1.0, 0.625, 1.0), "Suburb_Stairs_Trim_3M_B325", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1618.4073, 4555.0024, 1015.0103), (-0.00039672840047415395, -179.99988388673418, -89.99909553442366), (1.0, 0.625, 1.0), "Suburb_Stairs_Trim_3M_B326", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1580.0012, 4535.0024, 715.0103), (-0.00039672840047415395, -179.99988388673418, -89.99909553442366), (1.0, 0.625, 1.0), "Suburb_Stairs_Trim_3M_B327", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1318.4073, 4555.0024, 1015.0103), (-0.00039672840047415395, -179.99988388673418, -89.99909553442366), (1.0, 0.625, 1.0), "Suburb_Stairs_Trim_3M_B328", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1018.40735, 4555.0024, 1015.0103), (-0.00039672840047415395, -179.99988388673418, -89.99909553442366), (1.0, 0.625, 1.0), "Suburb_Stairs_Trim_3M_B329", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2949.996, 3644.997, 1285.0156), (-0.00042724601064604925, -179.99988388673574, -89.99922517928317), (1.0, 0.625, 1.0), "Suburb_Stairs_Trim_3M_B33", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1280.0012, 4535.0024, 715.0103), (-0.00039672840047415395, -179.99988388673418, -89.99909553442366), (1.0, 0.625, 1.0), "Suburb_Stairs_Trim_3M_B330", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (980.0012, 4535.0024, 715.0103), (-0.00039672840047415395, -179.99988388673418, -89.99909553442366), (1.0, 0.625, 1.0), "Suburb_Stairs_Trim_3M_B331", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (700.0012, 4525.0024, 1015.0103), (-0.0003987795309213881, 90.00010771731431, -89.9990718131428), (1.0, 0.625, 1.0), "Suburb_Stairs_Trim_3M_B332", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (700.0011, 4825.0024, 1015.0103), (-0.0003987795309213881, 90.00010771731431, -89.9990718131428), (1.0, 0.625, 1.0), "Suburb_Stairs_Trim_3M_B333", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (670.00134, 4525.0024, 715.0103), (-0.0003987795309213881, 90.00010771731431, -89.9990718131428), (1.0, 0.625, 1.0), "Suburb_Stairs_Trim_3M_B334", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (670.0012, 4825.0024, 715.0103), (-0.0003987795309213881, 90.00010771731431, -89.9990718131428), (1.0, 0.625, 1.0), "Suburb_Stairs_Trim_3M_B335", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (700.0011, 5095.0024, 715.0103), (-0.0003967284966345788, 0.0001220702984819684, -89.99907932914093), (1.0, 0.625, 1.0), "Suburb_Stairs_Trim_3M_B336", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1000.0012, 5095.0024, 715.0103), (-0.0003967284966345788, 0.0001220702984819684, -89.99907932914093), (1.0, 0.625, 1.0), "Suburb_Stairs_Trim_3M_B337", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (700.001, 5075.0024, 1015.0103), (-0.0003967284966345788, 0.0001220702984819684, -89.99907932914093), (1.0, 0.625, 1.0), "Suburb_Stairs_Trim_3M_B338", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1000.0011, 5075.0024, 1015.0103), (-0.0003967284966345788, 0.0001220702984819684, -89.99907932914093), (1.0, 0.625, 1.0), "Suburb_Stairs_Trim_3M_B339", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2349.996, 3644.997, 1285.0109), (-0.00042724601064604925, -179.99988388673574, -89.99922517928317), (1.0, 0.625, 1.0), "Suburb_Stairs_Trim_3M_B34", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1245.0012, 5095.0024, 715.0103), (-0.0003967284960713665, 0.00012199999818434496, -89.9990793291406), (0.98154163, 0.625, 1.0), "Suburb_Stairs_Trim_3M_B340", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1300.0011, 5075.0024, 1015.0103), (-0.0003967284960713665, 0.00012199999818434496, -89.9990793291406), (1.0, 0.625, 1.0), "Suburb_Stairs_Trim_3M_B341", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1600.0011, 5075.0024, 1015.0103), (-0.0003967284960713665, 0.00012199999818434496, -89.9990793291406), (1.03125, 0.625, 1.0), "Suburb_Stairs_Trim_3M_B342", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1402.9976, 5138.001, 715.0103), (-0.00039992549765757425, 90.00011000926744, -89.99904431139191), (1.0, 0.625, 1.0), "Suburb_Stairs_Trim_3M_B344", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1402.9977, 5438.001, 715.0103), (-0.00039992549765757425, 90.00011000926744, -89.99904431139191), (1.0, 0.625, 1.0), "Suburb_Stairs_Trim_3M_B345", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1422.9978, 5138.001, 1015.0103), (-0.00039992549765757425, 90.00011000926744, -89.99904431139191), (1.0, 0.625, 1.0), "Suburb_Stairs_Trim_3M_B346", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1422.9976, 5438.001, 1015.0103), (-0.00039992549765757425, 90.00011000926744, -89.99904431139191), (1.0, 0.625, 1.0), "Suburb_Stairs_Trim_3M_B347", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1959.999, 5160.998, 1015.0103), (-0.00039672843504230264, -179.99988388673557, -89.99901450669435), (1.0, 0.625, 1.0), "Suburb_Stairs_Trim_3M_B348", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1659.999, 5160.9976, 1015.0103), (-0.00039672843504230264, -179.99988388673557, -89.99901450669435), (1.0, 0.625, 1.0), "Suburb_Stairs_Trim_3M_B349", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1954.9995, 3624.9995, 700.0125), (-0.0004577636437047098, 90.00011648969011, 2.4947642343335056e-11), (1.0, 1.0, 1.0), "Suburb_Stairs_Trim_3M_B35", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1897.0024, 5727.9985, 715.0103), (-0.0003987796292386944, -89.99988541675346, -89.99902597708711), (1.0, 0.625, 1.0), "Suburb_Stairs_Trim_3M_B350", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1897.0024, 5427.999, 715.0103), (-0.0003987796292386944, -89.99988541675346, -89.99902597708711), (1.0, 0.625, 1.0), "Suburb_Stairs_Trim_3M_B351", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1877.0022, 5727.999, 1015.0103), (-0.0003987796292386944, -89.99988541675346, -89.99902597708711), (1.0, 0.625, 1.0), "Suburb_Stairs_Trim_3M_B352", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1877.0024, 5427.999, 1015.0103), (-0.0003987796292386944, -89.99988541675346, -89.99902597708711), (1.0, 0.625, 1.0), "Suburb_Stairs_Trim_3M_B353", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1350.0011, 5695.0024, 715.0103), (-0.00039672848336815, 0.00012207030890237251, -89.9990226097078), (1.0, 0.625, 1.0), "Suburb_Stairs_Trim_3M_B354", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1650.001, 5695.0024, 715.0103), (-0.00039672848336815, 0.00012207030890237251, -89.9990226097078), (1.0, 0.625, 1.0), "Suburb_Stairs_Trim_3M_B355", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1350.001, 5675.002, 1015.0103), (-0.00039672848336815, 0.00012207030890237251, -89.9990226097078), (1.0, 0.625, 1.0), "Suburb_Stairs_Trim_3M_B356", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1650.001, 5675.0024, 1015.0103), (-0.00039672848336815, 0.00012207030890237251, -89.9990226097078), (1.0, 0.625, 1.0), "Suburb_Stairs_Trim_3M_B357", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3495.008, 605.0092, 1414.9584), (-0.0010070801711714356, 0.00012207035054653315, -90.00040819746121), (1.0, 0.625, 1.0), "Suburb_Stairs_Trim_3M_B358", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3195.008, 605.0093, 1414.9614), (-0.0010070801711714356, 0.00012207035054653315, -90.00040819746121), (1.0, 0.625, 1.0), "Suburb_Stairs_Trim_3M_B359", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1954.9995, 3924.9995, 700.01245), (-0.0004577636437047098, 90.00011648969011, 2.4947642343335056e-11), (1.0, 1.0, 1.0), "Suburb_Stairs_Trim_3M_B36", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2895.008, 605.0092, 1414.9645), (-0.0010070801711714356, 0.00012207035054653315, -90.00040819746121), (1.0, 0.625, 1.0), "Suburb_Stairs_Trim_3M_B360", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2595.008, 605.0092, 1414.9677), (-0.0010070801711714356, 0.00012207035054653315, -90.00040819746121), (1.0, 0.625, 1.0), "Suburb_Stairs_Trim_3M_B361", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3775.008, 295.01025, 1414.9514), (-0.0003936231202105079, -89.99987739600823, -89.99896524406971), (1.0, 0.625, 1.0), "Suburb_Stairs_Trim_3M_B362", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3775.008, 595.01074, 1414.9513), (-0.0003936231202105079, -89.99987739600823, -89.99896524406971), (1.0, 0.625, 1.0), "Suburb_Stairs_Trim_3M_B363", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2615.008, 295.0086, 1414.9713), (-0.0003724217119884212, 90.00011459758883, -90.0007906856236), (1.0, 0.625, 1.0), "Suburb_Stairs_Trim_3M_B364", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2615.008, -4.9917097, 1414.972), (-0.0003724217119884212, 90.00011459758883, -90.0007906856236), (1.0, 0.625, 1.0), "Suburb_Stairs_Trim_3M_B365", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2005.0007, 3625.0027, 1015.0127), (-0.00042513553631806276, 90.00012032181498, -89.99919786315024), (1.0, 0.625, 1.0), "Suburb_Stairs_Trim_3M_B37", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2005.0007, 3925.0027, 1015.0107), (-0.00042513553631806276, 90.00012032181498, -89.99919786315024), (1.0, 0.625, 1.0), "Suburb_Stairs_Trim_3M_B38", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1995.0005, 3625.003, 1030.0127), (-0.00042513553631806276, 90.00012032181498, -89.99919786315024), (1.0, 0.625, 1.0), "Suburb_Stairs_Trim_3M_B39", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1995.0007, 3925.003, 1030.0106), (-0.00042513553631806276, 90.00012032181498, -89.99919786315024), (1.0, 0.625, 1.0), "Suburb_Stairs_Trim_3M_B40", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1995.0005, 3625.003, 1005.0127), (-0.00042513553631806276, 90.00012032181498, -89.99919786315024), (1.0, 0.625, 1.0), "Suburb_Stairs_Trim_3M_B41", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1995.0007, 3925.003, 1005.0106), (-0.00042513553631806276, 90.00012032181498, -89.99919786315024), (1.0, 0.625, 1.0), "Suburb_Stairs_Trim_3M_B42", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1994.9971, 3625.004, 1250.0127), (-0.00042513553631806276, 90.00012032181498, -89.99919786315024), (1.0, 0.625, 1.0), "Suburb_Stairs_Trim_3M_B43", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1994.9973, 3925.004, 1250.0103), (-0.00042513553631806276, 90.00012032181498, -89.99919786315024), (1.0, 0.625, 1.0), "Suburb_Stairs_Trim_3M_B44", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2019.9968, 3625.004, 1285.0133), (-0.00042513553631806276, 90.00012032181498, -89.99919786315024), (1.0, 0.625, 1.0), "Suburb_Stairs_Trim_3M_B45", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2019.9971, 3925.004, 1285.0109), (-0.00042513553631806276, 90.00012032181498, -89.99919786315024), (1.0, 0.625, 1.0), "Suburb_Stairs_Trim_3M_B46", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2005.0006, 4225.003, 1015.0103), (-0.00042513553631806276, 90.00012032181498, -89.99919786315024), (1.0, 0.625, 1.0), "Suburb_Stairs_Trim_3M_B47", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1995.0006, 4225.003, 1030.0103), (-0.00042513553631806276, 90.00012032181498, -89.99919786315024), (1.0, 0.625, 1.0), "Suburb_Stairs_Trim_3M_B48", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1995.0006, 4225.003, 1005.01025), (-0.00042513553631806276, 90.00012032181498, -89.99919786315024), (1.0, 0.625, 1.0), "Suburb_Stairs_Trim_3M_B49", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1994.9972, 4225.004, 1250.0099), (-0.00042513553631806276, 90.00012032181498, -89.99919786315024), (1.0, 0.625, 1.0), "Suburb_Stairs_Trim_3M_B50", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2019.997, 4225.004, 1285.0105), (-0.00042513553631806276, 90.00012032181498, -89.99919786315024), (1.0, 0.625, 1.0), "Suburb_Stairs_Trim_3M_B51", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2005.0006, 4525.003, 1015.0103), (-0.00042513553631806276, 90.00012032181498, -89.99919786315024), (1.0, 0.625, 1.0), "Suburb_Stairs_Trim_3M_B52", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1995.0006, 4525.003, 1030.0103), (-0.00042513553631806276, 90.00012032181498, -89.99919786315024), (1.0, 0.625, 1.0), "Suburb_Stairs_Trim_3M_B53", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1995.0006, 4525.003, 1005.01025), (-0.00042513553631806276, 90.00012032181498, -89.99919786315024), (1.0, 0.625, 1.0), "Suburb_Stairs_Trim_3M_B54", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1994.9972, 4525.004, 1250.0099), (-0.00042513553631806276, 90.00012032181498, -89.99919786315024), (1.0, 0.625, 1.0), "Suburb_Stairs_Trim_3M_B55", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2019.997, 4525.004, 1285.0105), (-0.00042513553631806276, 90.00012032181498, -89.99919786315024), (1.0, 0.625, 1.0), "Suburb_Stairs_Trim_3M_B56", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2005.0006, 4825.003, 1015.0103), (-0.00042513553631806276, 90.00012032181498, -89.99919786315024), (1.0, 0.625, 1.0), "Suburb_Stairs_Trim_3M_B57", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1995.0006, 4825.003, 1030.0103), (-0.00042513553631806276, 90.00012032181498, -89.99919786315024), (1.0, 0.625, 1.0), "Suburb_Stairs_Trim_3M_B58", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1995.0006, 4825.003, 1005.01025), (-0.00042513553631806276, 90.00012032181498, -89.99919786315024), (1.0, 0.625, 1.0), "Suburb_Stairs_Trim_3M_B59", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2600.0005, 3579.9995, 700.0125), (-0.00045776360601272966, -179.99988388675877, -1.442703368811174e-18), (1.0, 1.0, 1.0), "Suburb_Stairs_Trim_3M_B6_17", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1994.9972, 4825.004, 1250.0099), (-0.00042513553631806276, 90.00012032181498, -89.99919786315024), (1.0, 0.625, 1.0), "Suburb_Stairs_Trim_3M_B60", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2019.997, 4825.004, 1285.0105), (-0.00042513553631806276, 90.00012032181498, -89.99919786315024), (1.0, 0.625, 1.0), "Suburb_Stairs_Trim_3M_B61", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1999.9946, 5119.993, 1015.0107), (-0.00042724611278045625, 0.00012207035209686198, -89.99920897394861), (1.0, 0.625, 1.0), "Suburb_Stairs_Trim_3M_B62", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1999.9951, 5129.993, 1030.0106), (-0.00042724611278045625, 0.00012207035209686198, -89.99920897394861), (1.0, 0.625, 1.0), "Suburb_Stairs_Trim_3M_B63", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1999.9951, 5129.993, 1005.0106), (-0.00042724611278045625, 0.00012207035209686198, -89.99920897394861), (1.0, 0.625, 1.0), "Suburb_Stairs_Trim_3M_B64", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1999.9961, 5129.997, 1250.0103), (-0.00042724611278045625, 0.00012207035209686198, -89.99920897394861), (1.0, 0.625, 1.0), "Suburb_Stairs_Trim_3M_B65", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1999.9961, 5104.997, 1285.0109), (-0.00042724611278045625, 0.00012207035209686198, -89.99920897394861), (1.0, 0.625, 1.0), "Suburb_Stairs_Trim_3M_B66", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2299.996, 5104.997, 1285.0109), (-0.00042724611278045625, 0.00012207035209686198, -89.99920897394861), (1.0, 0.625, 1.0), "Suburb_Stairs_Trim_3M_B67", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2599.996, 5104.997, 1285.0109), (-0.00042724611278045625, 0.00012207035209686198, -89.99920897394861), (1.0, 0.625, 1.0), "Suburb_Stairs_Trim_3M_B68", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2899.996, 5104.997, 1285.0109), (-0.00042724611278045625, 0.00012207035209686198, -89.99920897394861), (1.0, 0.625, 1.0), "Suburb_Stairs_Trim_3M_B69", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2900.0005, 3579.9995, 700.0125), (-0.00045776360601272966, -179.99988388675877, -1.442703368811174e-18), (1.0, 1.0, 1.0), "Suburb_Stairs_Trim_3M_B7_21", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3199.996, 5104.997, 1285.0109), (-0.00042724611278045625, 0.00012207035209686198, -89.99920897394861), (1.0, 0.625, 1.0), "Suburb_Stairs_Trim_3M_B70", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3490.9995, 5119.997, 1015.0103), (-0.0003964876555005003, -89.99988312289973, -89.99920703038926), (1.0, 0.625, 1.0), "Suburb_Stairs_Trim_3M_B71", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3499.9998, 5119.997, 1030.0103), (-0.0003964876555005003, -89.99988312289973, -89.99920703038926), (1.0, 0.625, 1.0), "Suburb_Stairs_Trim_3M_B72", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3499.9998, 5119.997, 1005.01025), (-0.0003964876555005003, -89.99988312289973, -89.99920703038926), (1.0, 0.625, 1.0), "Suburb_Stairs_Trim_3M_B73", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3495.003, 5124.996, 1250.0099), (-0.0003964876555005003, -89.99988312289973, -89.99920703038926), (1.0, 0.625, 1.0), "Suburb_Stairs_Trim_3M_B74", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3470.0034, 5109.996, 1285.0105), (-0.0003964876555005003, -89.99988312289973, -89.99920703038926), (1.0, 0.625, 1.0), "Suburb_Stairs_Trim_3M_B75", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3490.9998, 4819.997, 1015.0103), (-0.0003964876555005003, -89.99988312289973, -89.99920703038926), (1.0, 0.625, 1.0), "Suburb_Stairs_Trim_3M_B76", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3499.9995, 4819.997, 1030.0103), (-0.0003964876555005003, -89.99988312289973, -89.99920703038926), (1.0, 0.625, 1.0), "Suburb_Stairs_Trim_3M_B77", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3499.9995, 4819.997, 1005.01025), (-0.0003964876555005003, -89.99988312289973, -89.99920703038926), (1.0, 0.625, 1.0), "Suburb_Stairs_Trim_3M_B78", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3495.003, 4824.9956, 1250.0099), (-0.0003964876555005003, -89.99988312289973, -89.99920703038926), (1.0, 0.625, 1.0), "Suburb_Stairs_Trim_3M_B79", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2874.9995, 3304.9995, 700.0125), (-0.0004577636437047098, 90.00011648969011, 2.4947642343335056e-11), (1.0, 1.0, 1.0), "Suburb_Stairs_Trim_3M_B8_347", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3470.003, 4809.996, 1285.0105), (-0.0003964876555005003, -89.99988312289973, -89.99920703038926), (1.0, 0.625, 1.0), "Suburb_Stairs_Trim_3M_B80", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3199.9946, 5119.993, 1015.0107), (-0.00042724611278045625, 0.00012207035209686198, -89.99920897394861), (1.0, 0.625, 1.0), "Suburb_Stairs_Trim_3M_B81", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3199.995, 5129.993, 1030.0106), (-0.00042724611278045625, 0.00012207035209686198, -89.99920897394861), (1.0, 0.625, 1.0), "Suburb_Stairs_Trim_3M_B82", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3199.995, 5129.993, 1005.0106), (-0.00042724611278045625, 0.00012207035209686198, -89.99920897394861), (1.0, 0.625, 1.0), "Suburb_Stairs_Trim_3M_B83", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3199.996, 5129.997, 1250.0103), (-0.00042724611278045625, 0.00012207035209686198, -89.99920897394861), (1.0, 0.625, 1.0), "Suburb_Stairs_Trim_3M_B84", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2874.9995, 3004.9995, 700.0125), (-0.0004577636437047098, 90.00011648969011, 2.4947642343335056e-11), (1.0, 1.0, 1.0), "Suburb_Stairs_Trim_3M_B9_348", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2789.995, 5139.993, 705.0106), (-0.00042724611278045625, 0.00012207035209686198, -89.99920897394861), (1.0, 0.375, 1.0), "Suburb_Stairs_Trim_3M_B98", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2489.995, 5139.993, 705.01), (-0.00042724611278045625, 0.00012207035209686198, -89.99920897394861), (1.0, 0.375, 1.0), "Suburb_Stairs_Trim_3M_B99", _folder)
if a: placed += 1
else: skipped += 1

# Batch 11: StaticMesh'NonDest_Boundry_Trim_A' (33 instances)
_mesh_path = "/Game/Art/Assets/Kits/Architecture/Non_D/NonDest_Boundry_Trim_A"
_materials = ['/Game/Art/Assets/Kits/Architecture/Suburbs/Materials/Suburbs_Trim_Sheet_A/MI_Suburbs_Trim_Sheet_A', '/Game/Environments/Materials/MI_Suburbs_Non_Destructible']
_folder = "Reconstruction/BD_BB_OrcPrison/Meshes"
a = spawn_static_mesh(_mesh_path, _materials, (1140.0, 2835.0, 1860.0), (0.0, 90.0000030488508, -0.0), (0.46875, 0.46875, 0.46875), "NonDest_Boundry_Trim_A_976", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1900.0, 4850.0, 1040.0), (0.0, 90.0000030488508, -0.0), (0.25, 0.25, 0.25), "NonDest_Boundry_Trim_A10", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1750.0, 3630.0, 1040.0), (0.0, 7.62939484614981e-06, -0.0), (0.25, 0.25, 0.25), "NonDest_Boundry_Trim_A11", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1617.0, 3813.0, 1040.0), (0.0, -89.99999818714215, 0.0), (0.25, 0.25, 0.25), "NonDest_Boundry_Trim_A12", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3601.001, 604.00085, 1859.9938), (1.3660373749679381e-05, -179.9999863396177, 0.00010438044994449063), (0.46875, 0.46875, 0.46875), "NonDest_Boundry_Trim_A13", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1617.0, 4188.0, 1040.0), (0.0, -89.99999818714215, 0.0), (0.25, 0.25, 0.25), "NonDest_Boundry_Trim_A14", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1243.0, 4563.0, 1040.0), (0.0, 1.9073485396501434e-05, -0.0), (0.25, 0.25, 0.25), "NonDest_Boundry_Trim_A15", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (868.0, 4563.0, 1040.0), (0.0, 1.899999897561354e-05, -0.0), (0.25, 0.25, 0.25), "NonDest_Boundry_Trim_A16", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (710.0, 4623.0, 1040.0), (0.0, -89.99997063746636, 0.0), (0.25, 0.25, 0.25), "NonDest_Boundry_Trim_A18", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (710.0, 4998.0, 1040.0), (0.0, -89.99997063746636, 0.0), (0.25, 0.25, 0.25), "NonDest_Boundry_Trim_A19", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1140.0, 3538.0, 1860.0), (0.0, 90.0000030488508, -0.0), (0.46875, 0.46875, 0.46875), "NonDest_Boundry_Trim_A2", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (580.0, 5043.0, 1040.0), (0.0, -179.9999590188648, 0.0), (0.25, 0.25, 0.25), "NonDest_Boundry_Trim_A20", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (955.0, 5043.0, 1040.0), (0.0, -179.9999590188648, 0.0), (0.25, 0.25, 0.25), "NonDest_Boundry_Trim_A21", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1330.0, 5043.0, 1040.0), (0.0, -179.9999590188648, 0.0), (0.25, 0.25, 0.25), "NonDest_Boundry_Trim_A22", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1705.0, 5043.0, 1040.0), (0.0, -179.9999590188648, 0.0), (0.25, 0.25, 0.25), "NonDest_Boundry_Trim_A23", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1455.0, 5263.0, 1040.02), (0.0, -89.99993822608693, 0.0), (0.25, 0.25, 0.25), "NonDest_Boundry_Trim_A24", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1465.0, 5193.0, 1040.0), (0.0, 6.484984988975128e-05, -0.0), (0.25, 0.25, 0.25), "NonDest_Boundry_Trim_A25", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1840.0, 5193.0, 1040.0), (0.0, 6.499999920954336e-05, -0.0), (0.25, 0.25, 0.25), "NonDest_Boundry_Trim_A26", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1455.0, 5638.0, 1040.02), (0.0, -89.99993822608693, 0.0), (0.25, 0.25, 0.25), "NonDest_Boundry_Trim_A27", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1845.0, 5603.0, 1040.02), (0.0, 90.00002735739477, -0.0), (0.25, 0.25, 0.25), "NonDest_Boundry_Trim_A28_86", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1845.0, 5228.0, 1040.02), (0.0, 90.00002735739477, -0.0), (0.25, 0.25, 0.25), "NonDest_Boundry_Trim_A29_87", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (347.00012, 2648.0002, 1860.0), (0.0, 7.62939484614981e-06, -0.0), (0.46875, 0.46875, 0.46875), "NonDest_Boundry_Trim_A3", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1475.0, 5643.0, 1040.02), (0.0, -179.99994535848643, 0.0), (0.25, 0.25, 0.25), "NonDest_Boundry_Trim_A30", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1850.0, 5643.0, 1040.02), (0.0, -179.99994535848643, 0.0), (0.25, 0.25, 0.25), "NonDest_Boundry_Trim_A31", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2898.002, 604.0011, 1859.994), (1.3660373749679381e-05, -179.9999863396177, 0.00010438044994449063), (0.46875, 0.46875, 0.46875), "NonDest_Boundry_Trim_A32", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3741.001, 344.00085, 1859.9938), (0.00010928300550699147, 89.99999818716923, -3.0517569649878425e-05), (0.46875, 0.46875, 0.46875), "NonDest_Boundry_Trim_A33", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2658.002, 354.0011, 1859.9937), (-0.00012207031103248403, -89.99997063754532, 1.2447268870849966e-05), (0.46875, 0.46875, 0.46875), "NonDest_Boundry_Trim_A34", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1050.0, 2648.0, 1860.0), (0.0, 7.62939484614981e-06, -0.0), (0.46875, 0.46875, 0.46875), "NonDest_Boundry_Trim_A4", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (853.0, 3751.9995, 1860.0), (0.0, -179.99998633961752, -0.0), (0.46875, 0.46875, 0.46875), "NonDest_Boundry_Trim_A5", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (150.0, 3752.0, 1860.0), (0.0, -179.99998633961752, -0.0), (0.46875, 0.46875, 0.46875), "NonDest_Boundry_Trim_A6", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1900.0, 3725.0, 1040.0), (0.0, 90.0000030488508, -0.0), (0.25, 0.25, 0.25), "NonDest_Boundry_Trim_A7_1213", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1900.0, 4100.0, 1040.0), (0.0, 90.0000030488508, -0.0), (0.25, 0.25, 0.25), "NonDest_Boundry_Trim_A8", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1900.0, 4475.0, 1040.0), (0.0, 90.0000030488508, -0.0), (0.25, 0.25, 0.25), "NonDest_Boundry_Trim_A9", _folder)
if a: placed += 1
else: skipped += 1

# Batch 12: StaticMesh'NonDest_Boundry_Trim_A_Corner' (1 instances)
_mesh_path = "/Game/Art/Assets/Kits/Architecture/Non_D/NonDest_Boundry_Trim_A_Corner"
_materials = ['/Game/Art/Assets/Kits/Architecture/Suburbs/Materials/Suburbs_Trim_Sheet_A/MI_Suburbs_Trim_Sheet_A', '/Game/Environments/Materials/MI_Suburbs_Non_Destructible']
_folder = "Reconstruction/BD_BB_OrcPrison/Meshes"
a = spawn_static_mesh(_mesh_path, _materials, (1430.0, 4563.0, 1040.0), (0.0, 1.899999897561354e-05, -0.0), (0.25, 0.25, 0.25), "NonDest_Boundry_Trim_A17_151", _folder)
if a: placed += 1
else: skipped += 1

# Batch 13: StaticMesh'NonDest_Floor_Trim_9M_C' (9 instances)
_mesh_path = "/Game/Art/Assets/Kits/Architecture/Non_D/NonDest_Floor_Trim_9M_C"
_materials = ['/Game/Art/Assets/Kits/Architecture/Suburbs/Materials/Suburbs_Trim_Sheet_A/MI_Suburbs_Trim_Sheet_A']
_folder = "Reconstruction/BD_BB_OrcPrison/Meshes"
a = spawn_static_mesh(_mesh_path, _materials, (300.0, 2600.0, 800.0), (0.0, 0.0, -0.0), (1.0, 1.0, 1.0), "NonDest_Floor_Trim_9M_C_2", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3500.0, -0.0011291504, 1900.0), (-0.00039672846611939444, 179.99989754715023, 179.99991120752796), (0.668, 1.0, 1.0), "NonDest_Floor_Trim_9M_C10", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2899.9995, 599.99927, 1899.9985), (-9.155273236881977e-05, 6.1035155987681574e-05, 179.99995901886533), (0.668, 1.0, 1.0), "NonDest_Floor_Trim_9M_C11", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (0.0, 3500.0, 800.0), (0.0, -90.00009542133918, 0.0), (0.668, 1.0, 1.0), "NonDest_Floor_Trim_9M_C2", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1200.0, 3800.0, 800.0), (0.0, -179.99994535848643, 0.0), (1.0, 1.0, 1.0), "NonDest_Floor_Trim_9M_C3", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (150.0, 3800.0, 2000.0), (-8.856026995271082e-12, -89.99997063770167, -179.9997677735701), (1.334, 1.0, 1.0), "NonDest_Floor_Trim_9M_C4_29", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2900.0, -0.0011291504, 800.0), (0.0, 6.580352668059126e-05, -0.0), (0.668, 1.0, 1.0), "NonDest_Floor_Trim_9M_C6_46", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3500.0005, 599.99927, 800.0), (0.0, 179.99991120752276, -0.0), (0.668, 1.0, 1.0), "NonDest_Floor_Trim_9M_C8", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2900.0005, 599.99927, 800.0), (0.0, -0.00030517577092912265, 0.0), (0.668, 1.0, 1.0), "NonDest_Floor_Trim_9M_C9", _folder)
if a: placed += 1
else: skipped += 1

# Batch 14: StaticMesh'NonDest_Floor_Trim_Corner_B' (10 instances)
_mesh_path = "/Game/Art/Assets/Kits/Architecture/Non_D/NonDest_Floor_Trim_Corner_B"
_materials = ['/Game/Art/Assets/Kits/Architecture/Suburbs/Materials/Suburbs_Trim_Sheet_A/MI_Suburbs_Trim_Sheet_A']
_folder = "Reconstruction/BD_BB_OrcPrison/Meshes"
a = spawn_static_mesh(_mesh_path, _materials, (300.0, 3800.0, 800.0), (0.0, 0.0, -0.0), (1.0, 1.0, 1.0), "NonDest_Floor_Trim_Corner_B_12", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2900.0, 600.0, 800.0), (0.0, -0.0002441406282020384, 0.0), (1.0, 1.0, 1.0), "NonDest_Floor_Trim_Corner_B10", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3800.0015, 299.99854, 1900.0005), (-6.103515156402435e-05, 90.00006787165309, -179.99995901885646), (1.0, 1.0, 1.0), "NonDest_Floor_Trim_Corner_B11", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2900.0, 0.0, 1899.9985), (7.39097572011556e-05, -9.155273680591005e-05, -179.99978826412467), (1.0, 1.0, 1.0), "NonDest_Floor_Trim_Corner_B12", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2599.9993, 299.99783, 1899.998), (5.775660656950087e-07, -89.99991067644046, 179.99994535848384), (1.0, 1.0, 1.0), "NonDest_Floor_Trim_Corner_B13", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3500.0, 600.0, 1900.0), (-0.00018310544876953982, -179.99963116975323, -179.99997950942853), (1.0, 1.0, 1.0), "NonDest_Floor_Trim_Corner_B14", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (0.0, 2900.0, 800.0), (0.0, 90.00001925454748, -0.0), (1.0, 1.0, 1.0), "NonDest_Floor_Trim_Corner_B2", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2599.9988, 299.99854, 800.0), (0.0, 90.00010028305118, -0.0), (1.0, 1.0, 1.0), "NonDest_Floor_Trim_Corner_B7", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3500.0, 0.0, 800.0), (0.0, -179.99992486791828, 0.0), (1.0, 1.0, 1.0), "NonDest_Floor_Trim_Corner_B8", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3800.0005, 299.99783, 800.0), (0.0, -90.00018131163026, 0.0), (1.0, 1.0, 1.0), "NonDest_Floor_Trim_Corner_B9", _folder)
if a: placed += 1
else: skipped += 1

# Batch 15: StaticMesh'NonDest_Floor_Trim_Corner_M' (12 instances)
_mesh_path = "/Game/Art/Assets/Kits/Architecture/Non_D/NonDest_Floor_Trim_Corner_M"
_materials = ['/Game/Art/Assets/Kits/Architecture/Suburbs/Materials/Suburbs_Trim_Sheet_A/MI_Suburbs_Trim_Sheet_A']
_folder = "Reconstruction/BD_BB_OrcPrison/Meshes"
a = spawn_static_mesh(_mesh_path, _materials, (650.0, 3200.0, 2020.0), (0.0003800390660168196, -179.99998633961434, -179.99995901884878), (1.9791437, 1.9791437, 3.0), "NonDest_Floor_Trim_Corner_M_35", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3000.0, 300.0, 1900.0), (0.00038199993031340856, -89.99980858116037, -179.99995901884745), (1.5, 1.5, 1.5), "NonDest_Floor_Trim_Corner_M10", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3000.0, 300.0, 1900.0), (0.0003819999525396774, 0.00036621090225113866, -179.99995901885936), (1.5, 1.5, 1.5), "NonDest_Floor_Trim_Corner_M11", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3000.0, 300.0, 1900.0), (0.0003819999620613621, 90.0003595754882, -179.99995901887425), (1.5, 1.5, 1.5), "NonDest_Floor_Trim_Corner_M12", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (650.0, 3200.0, 2020.0), (0.0003824904847219038, -89.99980858116183, -179.99995901888718), (2.0, 2.0, 3.0), "NonDest_Floor_Trim_Corner_M2", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (650.0, 3200.0, 2020.0), (0.00038249051897444527, 0.00036621090242659456, -179.99995901885777), (2.0, 2.0, 3.0), "NonDest_Floor_Trim_Corner_M3", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (650.0, 3200.0, 2020.0), (0.00038249052459340054, 90.00035957549002, -179.99995901885646), (2.0, 2.0, 3.0), "NonDest_Floor_Trim_Corner_M4", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3400.0, 300.0, 1900.0), (0.0003799998527931627, -179.99998633961434, -179.99995901884878), (1.5, 1.5, 1.5), "NonDest_Floor_Trim_Corner_M5", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3400.0, 300.0, 1900.0), (-3.051755928217009e-05, -89.99987340454999, -179.99950822629728), (1.5, 1.5, 1.5), "NonDest_Floor_Trim_Corner_M6_672", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3400.0, 300.0, 1900.0), (0.0003819999525396774, 0.00036621090225113866, -179.99995901885936), (1.5, 1.5, 1.5), "NonDest_Floor_Trim_Corner_M7", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3400.0, 300.0, 1900.0), (0.0003819999620613621, 90.0003595754882, -179.99995901887425), (1.5, 1.5, 1.5), "NonDest_Floor_Trim_Corner_M8", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3000.0, 300.0, 1900.0), (0.0003799998527931627, -179.99998633961434, -179.99995901884878), (1.5, 1.5, 1.5), "NonDest_Floor_Trim_Corner_M9", _folder)
if a: placed += 1
else: skipped += 1

# Batch 16: StaticMesh'NonDest_Floor_Trim_Thin_1M_A' (4 instances)
_mesh_path = "/Game/Art/Assets/Kits/Architecture/Non_D/NonDest_Floor_Trim_Thin_1M_A"
_materials = ['/Game/Art/Assets/Kits/Architecture/Suburbs/Materials/Suburbs_Trim_Sheet_A/MI_Suburbs_Trim_Sheet_A']
_folder = "Reconstruction/BD_BB_OrcPrison/Meshes"
a = spawn_static_mesh(_mesh_path, _materials, (145.00134, 3339.9995, 2000.0), (8.900000130594382e-05, 90.00022020536964, 179.99994535848603), (1.5, 1.5, 1.5), "NonDest_Floor_Trim_9M_C12", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1100.0013, 3489.9995, 2000.0), (8.900000053117831e-05, -89.99975996378575, 179.99994535848515), (1.5, 1.5, 1.5), "NonDest_Floor_Trim_9M_C14", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1100.0013, 3064.9995, 2000.0), (8.900000053117831e-05, -89.99975996378575, 179.99994535848515), (1.5, 1.5, 1.5), "NonDest_Floor_Trim_9M_C15", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (145.00134, 2914.9995, 2000.0), (8.900000130594382e-05, 90.00022020536964, 179.99994535848603), (1.5, 1.5, 1.5), "NonDest_Floor_Trim_9M_C7", _folder)
if a: placed += 1
else: skipped += 1

# Batch 17: StaticMesh'NonDest_Floor_Trim_Thin_2M_A' (2 instances)
_mesh_path = "/Game/Art/Assets/Kits/Architecture/Non_D/NonDest_Floor_Trim_Thin_2M_A"
_materials = ['/Game/Art/Assets/Kits/Architecture/Suburbs/Materials/Suburbs_Trim_Sheet_A/MI_Suburbs_Trim_Sheet_A']
_folder = "Reconstruction/BD_BB_OrcPrison/Meshes"
a = spawn_static_mesh(_mesh_path, _materials, (145.00134, 3064.9995, 2000.0), (8.900000130594382e-05, 90.00022020536964, 179.99994535848603), (1.375, 1.5, 1.5), "NonDest_Floor_Trim_9M_C13", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1100.0013, 3339.9995, 2000.0), (8.900000053117831e-05, -89.99975996378575, 179.99994535848515), (1.375, 1.5, 1.5), "NonDest_Floor_Trim_9M_C16", _folder)
if a: placed += 1
else: skipped += 1

# Batch 18: StaticMesh'NonDest_Floor_Trim_Thin_3M_A' (2 instances)
_mesh_path = "/Game/Art/Assets/Kits/Architecture/Non_D/NonDest_Floor_Trim_Thin_3M_A"
_materials = ['/Game/Art/Assets/Kits/Architecture/Suburbs/Materials/Suburbs_Trim_Sheet_A/MI_Suburbs_Trim_Sheet_A']
_folder = "Reconstruction/BD_BB_OrcPrison/Meshes"
a = spawn_static_mesh(_mesh_path, _materials, (370.00134, 3714.9995, 2000.0), (8.899999986041264e-05, 0.000244140631600359, 179.9999453584881), (1.6875, 1.5, 1.5), "NonDest_Floor_Trim_9M_C19", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (875.00134, 2689.9995, 2000.0), (8.90000010547477e-05, -179.99976777355593, 179.9999453584846), (1.6875, 1.5, 1.5), "NonDest_Floor_Trim_9M_C20", _folder)
if a: placed += 1
else: skipped += 1

# Batch 19: StaticMesh'NonDest_Floor_Trim_Thin_Corner_A' (4 instances)
_mesh_path = "/Game/Art/Assets/Kits/Architecture/Non_D/NonDest_Floor_Trim_Thin_Corner_A"
_materials = ['/Game/Art/Assets/Kits/Architecture/Suburbs/Materials/Suburbs_Trim_Sheet_A/MI_Suburbs_Trim_Sheet_A']
_folder = "Reconstruction/BD_BB_OrcPrison/Meshes"
a = spawn_static_mesh(_mesh_path, _materials, (874.9989, 3714.999, 2000.0005), (0.0005464150650922758, 0.00024414062519806666, -179.99994535848654), (1.5, 1.5, 1.5), "NonDest_Floor_Trim_Corner_B15", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1099.9989, 2914.999, 2000.0005), (0.0005464150781480277, -89.99975996475096, -179.9999453585157), (1.5, 1.5, 1.5), "NonDest_Floor_Trim_Corner_B16", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (370.00366, 2690.0, 2000.0005), (0.0005464150707731715, -179.9997677735738, -179.99994535848606), (1.5, 1.5, 1.5), "NonDest_Floor_Trim_Corner_B5", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (145.00366, 3490.0, 2000.0005), (0.0005464150781480277, 90.00023965380612, -179.9999453585157), (1.5, 1.5, 1.5), "NonDest_Floor_Trim_Corner_B6_1173", _folder)
if a: placed += 1
else: skipped += 1

# Batch 20: StaticMesh'NonDest_Pillar_3M_A' (31 instances)
_mesh_path = "/Game/Art/Assets/Kits/Architecture/Non_D/NonDest_Pillar_3M_A"
_materials = ['/Game/Art/Assets/Kits/Architecture/Suburbs/Materials/Suburbs_Trim_Sheet_A/MI_Suburbs_Trim_Sheet_A']
_folder = "Reconstruction/BD_BB_OrcPrison/Meshes"
a = spawn_static_mesh(_mesh_path, _materials, (1934.9998, 3925.0, 695.0), (0.0, -89.99999818714215, 0.0), (0.84375, 0.84375, 0.84375), "NonDest_Pillar_4M_A101_1188", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1934.9998, 3625.0, 695.0), (0.0, -89.99999818714215, 0.0), (0.84375, 0.84375, 0.84375), "NonDest_Pillar_4M_A104_1189", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1934.9998, 4215.0, 695.0), (0.0, -89.99999818714215, 0.0), (0.84375, 0.84375, 0.84375), "NonDest_Pillar_4M_A105_1208", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1934.9998, 4515.0, 695.0), (0.0, -89.99999818714215, 0.0), (0.84375, 0.84375, 0.84375), "NonDest_Pillar_4M_A106_1222", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1934.9998, 4815.0, 695.0), (0.0, -89.99999818714215, 0.0), (0.84375, 0.84375, 0.84375), "NonDest_Pillar_4M_A107_1224", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1934.9998, 5115.0, 695.0), (0.0, -89.99999818714215, 0.0), (0.84375, 0.84375, 0.84375), "NonDest_Pillar_4M_A108", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1904.9998, 3595.0, 695.0), (0.0, -179.9999590188648, 0.0), (0.84375, 0.84375, 0.84375), "NonDest_Pillar_4M_A109_1229", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1609.9998, 3595.0, 695.0), (0.0, -179.99998633961752, -0.0), (0.84375, 0.84375, 0.84375), "NonDest_Pillar_4M_A110", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1579.9998, 3625.0, 695.0), (0.0, 90.00002735739477, -0.0), (0.84375, 0.84375, 0.84375), "NonDest_Pillar_4M_A111", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1575.0002, 3925.0, 695.0), (0.0, 89.99999818714215, -0.0), (0.84375, 0.84375, 0.84375), "NonDest_Pillar_4M_A112", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1575.0002, 4225.0, 695.0), (0.0, 89.99999818714215, -0.0), (0.84375, 0.84375, 0.84375), "NonDest_Pillar_4M_A113", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1575.0002, 4505.0, 695.0), (0.0, 89.99999818714215, -0.0), (0.84375, 0.84375, 0.84375), "NonDest_Pillar_4M_A114", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1560.0002, 4520.0, 695.0), (0.0, -179.99998633961752, -0.0), (0.84375, 0.84375, 0.84375), "NonDest_Pillar_4M_A115", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1230.0002, 5100.0, 690.0), (0.0, -179.99998633961752, -0.0), (0.84375, 0.84375, 0.84375), "NonDest_Pillar_4M_A117_36", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (680.00024, 4520.0, 695.0), (0.0, -179.99998633961752, -0.0), (0.84375, 0.84375, 0.84375), "NonDest_Pillar_4M_A118", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (650.00024, 4550.0, 695.0), (0.0, 89.99999818714215, -0.0), (0.84375, 0.84375, 0.84375), "NonDest_Pillar_4M_A119", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (660.00037, 5080.0, 695.0), (0.0, 89.99999818714215, -0.0), (0.84375, 0.84375, 0.84375), "NonDest_Pillar_4M_A120", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (690.00024, 5110.0, 695.0), (0.0, 0.0, -0.0), (0.84375, 0.84375, 0.84375), "NonDest_Pillar_4M_A121", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1405.0002, 5110.0, 695.0), (0.0, -179.99998633961752, -0.0), (0.84375, 0.84375, 0.84375), "NonDest_Pillar_4M_A122", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1910.0002, 5110.0, 695.0), (0.0, -179.99998633961752, -0.0), (0.84375, 0.84375, 0.84375), "NonDest_Pillar_4M_A123", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1934.9998, 5085.0, 695.0), (0.0, -89.99999818714215, 0.0), (0.84375, 0.84375, 0.84375), "NonDest_Pillar_4M_A124", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1395.0002, 5160.0, 695.0), (0.0, -89.99997063746636, 0.0), (0.84375, 0.84375, 0.84375), "NonDest_Pillar_4M_A125", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1425.0002, 5130.0, 695.0), (0.0, 5.340576277714065e-05, -0.0), (0.84375, 0.84375, 0.84375), "NonDest_Pillar_4M_A126", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1875.0002, 5135.0, 695.0), (0.0, 5.340576277714065e-05, -0.0), (0.84375, 0.84375, 0.84375), "NonDest_Pillar_4M_A127", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1905.0002, 5165.0, 695.0), (0.0, 90.00005166594045, -0.0), (0.84375, 0.84375, 0.84375), "NonDest_Pillar_4M_A128", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1905.0001, 5670.0, 695.0), (0.0, 90.00005166594045, -0.0), (0.84375, 0.84375, 0.84375), "NonDest_Pillar_4M_A129", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1875.0002, 5700.0, 695.0), (0.0, -179.99994535848643, 0.0), (0.84375, 0.84375, 0.84375), "NonDest_Pillar_4M_A130", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1425.0001, 5700.0, 695.0), (0.0, -179.99994535848643, 0.0), (0.84375, 0.84375, 0.84375), "NonDest_Pillar_4M_A131", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1395.0002, 5670.0, 695.0), (0.0, -89.99991067642716, 0.0), (0.84375, 0.84375, 0.84375), "NonDest_Pillar_4M_A132", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1405.0002, 4520.0, 695.0), (0.0, -179.99998633961752, -0.0), (0.84375, 0.84375, 0.84375), "NonDest_Pillar_4M_A133", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1230.0002, 4520.0, 690.0), (0.0, -179.99998633961752, -0.0), (0.84375, 0.84375, 0.84375), "NonDest_Pillar_4M_A134", _folder)
if a: placed += 1
else: skipped += 1

# Batch 21: StaticMesh'NonDest_Pillar_3M_B' (36 instances)
_mesh_path = "/Game/Art/Assets/Kits/Architecture/Non_D/NonDest_Pillar_3M_B"
_materials = ['/Game/Art/Assets/Kits/Architecture/Suburbs/Materials/Suburbs_Trim_Sheet_A/MI_Suburbs_Trim_Sheet_A']
_folder = "Reconstruction/BD_BB_OrcPrison/Meshes"
a = spawn_static_mesh(_mesh_path, _materials, (2010.0, 3605.0, 990.0), (0.0, 0.0, -0.0), (0.84375, 0.84375, 0.90625), "NonDest_Pillar_4M_A13", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1980.0, 3635.0, 990.0), (0.0, -89.99999818714215, 0.0), (0.84375, 0.84375, 0.90625), "NonDest_Pillar_4M_A14", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1979.9999, 5125.0, 989.99963), (0.0, -89.99999818714215, 0.0), (0.84375, 0.84375, 0.90625), "NonDest_Pillar_4M_A17", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2300.0, 5145.0, 990.0), (0.0, -179.99998633961752, -0.0), (0.84375, 0.84375, 0.90625), "NonDest_Pillar_4M_A20", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2000.0, 5145.0, 990.0), (0.0, -179.99998633961752, -0.0), (0.84375, 0.84375, 0.90625), "NonDest_Pillar_4M_A22", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3515.0, 4820.0, 989.99963), (0.0, 89.99999818714215, -0.0), (0.84375, 0.84375, 0.90625), "NonDest_Pillar_4M_A23", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3509.9995, 4525.0, 989.99963), (0.0, 89.99999818714215, -0.0), (0.84375, 0.84375, 0.90625), "NonDest_Pillar_4M_A25_323", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3200.0, 5145.0, 990.0), (0.0, -179.99998633961752, -0.0), (0.84375, 0.84375, 0.90625), "NonDest_Pillar_4M_A28", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2300.0, 3605.0, 990.0), (0.0, 0.0, -0.0), (0.84375, 0.84375, 0.90625), "NonDest_Pillar_4M_A3", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3100.0, 5145.0, 990.0), (0.0, -179.99998633961752, -0.0), (0.84375, 0.84375, 0.90625), "NonDest_Pillar_4M_A30", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2400.0, 5145.0, 990.0), (0.0, -179.99998633961752, -0.0), (0.84375, 0.84375, 0.90625), "NonDest_Pillar_4M_A32", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3515.0, 5120.0, 989.99963), (0.0, 89.99999818714215, -0.0), (0.84375, 0.84375, 0.90625), "NonDest_Pillar_4M_A33", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3490.0, 5145.0, 990.0), (0.0, -179.99998633961752, -0.0), (0.84375, 0.84375, 0.90625), "NonDest_Pillar_4M_A36", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2900.0, 3305.0, 990.0), (0.0, -89.99999818714215, 0.0), (0.84375, 0.84375, 0.90625), "NonDest_Pillar_4M_A38", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2600.0, 3605.0, 990.0), (0.0, 0.0, -0.0), (0.84375, 0.84375, 0.90625), "NonDest_Pillar_4M_A4", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2890.0, 3605.0, 990.0), (0.0, 0.0, -0.0), (0.84375, 0.84375, 0.90625), "NonDest_Pillar_4M_A41", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2900.0, 3595.0, 990.03), (0.0, -89.99999818714215, 0.0), (0.84375, 0.84375, 0.90625), "NonDest_Pillar_4M_A42", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3515.0, 3305.0, 989.99963), (0.0, 89.99999818714215, -0.0), (0.84375, 0.84375, 0.90625), "NonDest_Pillar_4M_A43", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3515.0, 3605.0, 989.99963), (0.0, 89.99999818714215, -0.0), (0.84375, 0.84375, 0.90625), "NonDest_Pillar_4M_A45", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3509.9995, 3010.0, 989.99963), (0.0, 89.99999818714215, -0.0), (0.84375, 0.84375, 0.90625), "NonDest_Pillar_4M_A47", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3515.0, 3905.0, 989.99963), (0.0, 89.99999818714215, -0.0), (0.84375, 0.84375, 0.90625), "NonDest_Pillar_4M_A49_422", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2900.0, 3005.0, 990.0), (0.0, -89.99999818714215, 0.0), (0.84375, 0.84375, 0.90625), "NonDest_Pillar_4M_A52", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2925.0, 2981.0, 990.0), (0.0, 1.1444092154633197e-05, -0.0), (0.84375, 0.84375, 0.90625), "NonDest_Pillar_4M_A54", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3479.9998, 2981.0002, 989.99963), (0.0, 0.0, -0.0), (0.84375, 0.84375, 0.90625), "NonDest_Pillar_4M_A55", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1980.0, 3925.0, 990.0), (0.0, -89.99999818714215, 0.0), (0.84375, 0.84375, 0.90625), "NonDest_Pillar_4M_A6", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2905.0, 1955.0, 1000.0), (0.0, -89.99999818714215, 0.0), (0.84375, 0.84375, 0.90625), "NonDest_Pillar_4M_A62_682", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2905.0, 1545.0, 1000.0), (0.0, -89.99999818714215, 0.0), (0.84375, 0.84375, 0.90625), "NonDest_Pillar_4M_A64", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3539.9934, 1545.0079, 1000.0), (0.0, 89.99999818714215, -0.0), (0.84375, 0.84375, 0.90625), "NonDest_Pillar_4M_A68", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1979.9999, 4225.0, 989.99963), (0.0, -89.99999818714215, 0.0), (0.84375, 0.84375, 0.90625), "NonDest_Pillar_4M_A7", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3539.9937, 1955.0078, 1000.0), (0.0, 89.99999818714215, -0.0), (0.84375, 0.84375, 0.90625), "NonDest_Pillar_4M_A70", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2905.0, 1145.0, 1000.0), (0.0, -89.99999818714215, 0.0), (0.84375, 0.84375, 0.90625), "NonDest_Pillar_4M_A72", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2905.0, 735.0, 1000.0), (0.0, -89.99999818714215, 0.0), (0.84375, 0.84375, 0.90625), "NonDest_Pillar_4M_A74", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3545.0012, 735.00543, 1000.0), (0.0, 89.99999818714215, -0.0), (0.84375, 0.84375, 0.90625), "NonDest_Pillar_4M_A76", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3545.0015, 1145.0054, 1000.0), (0.0, 89.99999818714215, -0.0), (0.84375, 0.84375, 0.90625), "NonDest_Pillar_4M_A78", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1979.9999, 4525.0, 989.99963), (0.0, -89.99999818714215, 0.0), (0.84375, 0.84375, 0.90625), "NonDest_Pillar_4M_A8", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1979.9999, 4825.0, 989.99963), (0.0, -89.99999818714215, 0.0), (0.84375, 0.84375, 0.90625), "NonDest_Pillar_4M_A9", _folder)
if a: placed += 1
else: skipped += 1

# Batch 22: StaticMesh'NonDest_Pillar_4M_A' (36 instances)
_mesh_path = "/Game/Art/Assets/Kits/Architecture/Non_D/NonDest_Pillar_4M_A"
_materials = ['/Game/Art/Assets/Kits/Architecture/Suburbs/Materials/Suburbs_Trim_Sheet_A/MI_Suburbs_Trim_Sheet_A']
_folder = "Reconstruction/BD_BB_OrcPrison/Meshes"
a = spawn_static_mesh(_mesh_path, _materials, (2600.0, 3600.0, 605.0), (0.0, 0.0, -0.0), (0.84375, 0.84375, 0.84375), "NonDest_Pillar_4M_A_14", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1974.9998, 4825.0, 605.0), (0.0, -89.99999818714215, 0.0), (0.84375, 0.84375, 0.84375), "NonDest_Pillar_4M_A10", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2000.0, 3600.0, 605.0), (0.0, 0.0, -0.0), (0.84375, 0.84375, 0.84375), "NonDest_Pillar_4M_A11_120", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1974.9998, 4225.0, 605.0), (0.0, -89.99999818714215, 0.0), (0.84375, 0.84375, 0.84375), "NonDest_Pillar_4M_A12_122", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1974.9998, 3625.0, 605.0), (0.0, -89.99999818714215, 0.0), (0.84375, 0.84375, 0.84375), "NonDest_Pillar_4M_A15", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1974.9998, 4525.0, 605.0), (0.0, -89.99999818714215, 0.0), (0.84375, 0.84375, 0.84375), "NonDest_Pillar_4M_A16", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1974.9998, 5125.0, 605.0), (0.0, -89.99999818714215, 0.0), (0.84375, 0.84375, 0.84375), "NonDest_Pillar_4M_A18", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2300.0, 5150.0, 605.0), (0.0, -179.99998633961752, -0.0), (0.84375, 0.84375, 0.84375), "NonDest_Pillar_4M_A19", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2300.0, 3600.0, 605.0), (0.0, 0.0, -0.0), (0.84375, 0.84375, 0.84375), "NonDest_Pillar_4M_A2", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2000.0, 5150.0, 605.0), (0.0, -179.99998633961752, -0.0), (0.84375, 0.84375, 0.84375), "NonDest_Pillar_4M_A21", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3520.0, 4820.0, 605.0), (0.0, 89.99999818714215, -0.0), (0.84375, 0.84375, 0.84375), "NonDest_Pillar_4M_A24", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3514.9998, 4525.0, 605.0), (0.0, 89.99999818714215, -0.0), (0.84375, 0.84375, 0.84375), "NonDest_Pillar_4M_A26_324", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3200.0, 5150.0, 605.0), (0.0, -179.99998633961752, -0.0), (0.84375, 0.84375, 0.84375), "NonDest_Pillar_4M_A27", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3100.0, 5150.0, 605.0), (0.0, -179.99998633961752, -0.0), (0.84375, 0.84375, 0.84375), "NonDest_Pillar_4M_A29", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2400.0, 5150.0, 605.0), (0.0, -179.99998633961752, -0.0), (0.84375, 0.84375, 0.84375), "NonDest_Pillar_4M_A31", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3520.0, 5120.0, 605.0), (0.0, 89.99999818714215, -0.0), (0.84375, 0.84375, 0.84375), "NonDest_Pillar_4M_A34", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3490.0, 5150.0, 605.0), (0.0, -179.99998633961752, -0.0), (0.84375, 0.84375, 0.84375), "NonDest_Pillar_4M_A35", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2894.9998, 3305.0, 605.0), (0.0, -89.99999818714215, 0.0), (0.84375, 0.84375, 0.84375), "NonDest_Pillar_4M_A37", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2884.9998, 3605.0, 605.0), (0.0, 1.1444092154633197e-05, -0.0), (0.84375, 0.84375, 0.84375), "NonDest_Pillar_4M_A39", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2894.9998, 3595.0, 605.03), (0.0, -89.99999818714215, 0.0), (0.84375, 0.84375, 0.84375), "NonDest_Pillar_4M_A40", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3520.0, 3305.0, 605.0), (0.0, 89.99999818714215, -0.0), (0.84375, 0.84375, 0.84375), "NonDest_Pillar_4M_A44", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3520.0, 3605.0, 605.0), (0.0, 89.99999818714215, -0.0), (0.84375, 0.84375, 0.84375), "NonDest_Pillar_4M_A46", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3514.9998, 3010.0, 605.0), (0.0, 89.99999818714215, -0.0), (0.84375, 0.84375, 0.84375), "NonDest_Pillar_4M_A48", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1974.9998, 3925.0, 605.0), (0.0, -89.99999818714215, 0.0), (0.84375, 0.84375, 0.84375), "NonDest_Pillar_4M_A5", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3520.0, 3905.0, 605.0), (0.0, 89.99999818714215, -0.0), (0.84375, 0.84375, 0.84375), "NonDest_Pillar_4M_A50", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2894.9998, 3005.0, 605.0), (0.0, -89.99999818714215, 0.0), (0.84375, 0.84375, 0.84375), "NonDest_Pillar_4M_A51", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2930.0, 2976.9998, 605.0), (0.0, 1.1444092154633197e-05, -0.0), (0.84375, 0.84375, 0.84375), "NonDest_Pillar_4M_A53", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3479.9998, 2977.0, 605.0), (0.0, 0.0, -0.0), (0.84375, 0.84375, 0.84375), "NonDest_Pillar_4M_A56", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2899.9998, 1955.0, 615.0), (0.0, -89.99999818714215, 0.0), (0.84375, 0.84375, 0.84375), "NonDest_Pillar_4M_A57_678", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2899.9998, 1545.0, 615.0), (0.0, -89.99999818714215, 0.0), (0.84375, 0.84375, 0.84375), "NonDest_Pillar_4M_A63", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3544.9937, 1545.0079, 615.0), (0.0, 89.99999818714215, -0.0), (0.84375, 0.84375, 0.84375), "NonDest_Pillar_4M_A67", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3544.9937, 1955.0078, 615.0), (0.0, 89.99999818714215, -0.0), (0.84375, 0.84375, 0.84375), "NonDest_Pillar_4M_A69", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2899.9998, 1145.0, 615.0), (0.0, -89.99999818714215, 0.0), (0.84375, 0.84375, 0.84375), "NonDest_Pillar_4M_A71", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2899.9998, 735.0, 615.0), (0.0, -89.99999818714215, 0.0), (0.84375, 0.84375, 0.84375), "NonDest_Pillar_4M_A73", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3550.0015, 735.0055, 615.0), (0.0, 89.99999818714215, -0.0), (0.84375, 0.84375, 0.84375), "NonDest_Pillar_4M_A75", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3550.0017, 1145.0054, 615.0), (0.0, 89.99999818714215, -0.0), (0.84375, 0.84375, 0.84375), "NonDest_Pillar_4M_A77", _folder)
if a: placed += 1
else: skipped += 1

# Batch 23: StaticMesh'NonDest_Pillar_4M_B' (18 instances)
_mesh_path = "/Game/Art/Assets/Kits/Architecture/Non_D/NonDest_Pillar_4M_B"
_materials = ['/Game/Art/Assets/Kits/Architecture/Suburbs/Materials/Suburbs_Trim_Sheet_A/MI_Suburbs_Trim_Sheet_A']
_folder = "Reconstruction/BD_BB_OrcPrison/Meshes"
a = spawn_static_mesh(_mesh_path, _materials, (280.0, 2615.0, 1430.0), (0.0, 179.99991120752276, -0.0), (1.0, 1.0, 1.0), "NonDest_Pillar_5M_A10_1146", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (880.0, 3784.9998, 1430.0), (0.0, -0.00012207030837116422, 0.0), (1.0, 1.0, 1.0), "NonDest_Pillar_5M_A11", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (569.9999, 3784.9998, 1430.0), (0.0, -0.00012207030837116422, 0.0), (1.0, 1.0, 1.0), "NonDest_Pillar_5M_A12", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (270.0, 3795.0, 1430.0), (0.0, -0.00012207030837116422, 0.0), (1.0, 1.0, 1.0), "NonDest_Pillar_5M_A13", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1190.0, 2640.0, 1430.0), (0.0, -90.00009542133918, 0.0), (1.0, 1.0, 1.0), "NonDest_Pillar_5M_A14", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1200.0, 3780.0, 1430.0), (0.0, -90.00009542133918, 0.0), (1.0, 1.0, 1.0), "NonDest_Pillar_5M_A15", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1160.0, 3815.0, 1430.0), (0.0, -9.155273700792082e-05, 0.0), (1.0, 1.0, 1.0), "NonDest_Pillar_5M_A16", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1190.0, 2890.0, 1430.0), (0.0, -90.00009542133918, 0.0), (1.0, 1.0, 1.0), "NonDest_Pillar_5M_A17", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1190.0, 3490.0, 1430.0), (0.0, -90.00009542133918, 0.0), (1.0, 1.0, 1.0), "NonDest_Pillar_5M_A18", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3546.001, 654.0016, 1429.9937), (1.0300772226861994e-18, 4.577636793101723e-05, -9.155273700793543e-05), (1.0, 1.0, 1.0), "NonDest_Pillar_5M_A19", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2926.001, 654.00146, 1429.9937), (7.610669475871322e-19, 4.599999908803495e-05, -9.155273700793556e-05), (1.0, 1.0, 1.0), "NonDest_Pillar_5M_A20", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3776.001, 664.0016, 1429.9937), (7.610669475871322e-19, 4.599999908803495e-05, -9.155273700793556e-05), (1.0, 1.0, 1.0), "NonDest_Pillar_5M_A27", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3816.001, 624.0016, 1429.9937), (-9.155273308046357e-05, -89.99993822612942, 7.1321976537670255e-06), (1.0, 1.0, 1.0), "NonDest_Pillar_5M_A28", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2576.001, 634.00037, 1429.9934), (0.00010245283528352636, 90.00001925459385, 3.6031236973334605e-06), (1.0, 1.0, 1.0), "NonDest_Pillar_5M_A29", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2616.001, 674.0004, 1429.9937), (-3.0530463987002984e-18, 6.866455246952685e-05, -0.00012207030837120805), (1.0, 1.0, 1.0), "NonDest_Pillar_5M_A30", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (580.0, 2615.0, 1430.0), (0.0, 179.99991120752276, -0.0), (1.0, 1.0, 1.0), "NonDest_Pillar_5M_A7", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (885.0, 2615.0, 1430.0), (0.0, 179.99991120752276, -0.0), (1.0, 1.0, 1.0), "NonDest_Pillar_5M_A8", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1155.0, 2600.0, 1430.0), (0.0, 179.99991120752276, -0.0), (1.0, 1.0, 1.0), "NonDest_Pillar_5M_A9", _folder)
if a: placed += 1
else: skipped += 1

# Batch 24: StaticMesh'NonDest_Pillar_5M_A' (6 instances)
_mesh_path = "/Game/Art/Assets/Kits/Architecture/Non_D/NonDest_Pillar_5M_A"
_materials = ['/Game/Art/Assets/Kits/Architecture/Suburbs/Materials/Suburbs_Trim_Sheet_A/MI_Suburbs_Trim_Sheet_A']
_folder = "Reconstruction/BD_BB_OrcPrison/Meshes"
a = spawn_static_mesh(_mesh_path, _materials, (3546.001, 654.0029, 789.99365), (7.610669475871322e-19, 4.599999908803495e-05, -9.155273700793556e-05), (1.0, 1.0, 1.0), "NonDest_Pillar_5M_A21", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2876.001, 654.0025, 789.99365), (7.610669475871322e-19, 4.599999908803495e-05, -9.155273700793556e-05), (1.0, 1.0, 1.0), "NonDest_Pillar_5M_A22", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3776.001, 654.003, 789.99365), (7.610669475871322e-19, 4.599999908803495e-05, -9.155273700793556e-05), (1.0, 1.0, 1.0), "NonDest_Pillar_5M_A23", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3816.001, 614.003, 789.99365), (-9.155273600251854e-05, -89.99993822612747, 4.850529265463955e-06), (1.0, 1.0, 1.0), "NonDest_Pillar_5M_A24", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2586.001, 614.00165, 789.9936), (0.00010245283511913918, 90.00004680428594, 1.0253304004025824e-05), (1.0, 1.0, 1.0), "NonDest_Pillar_5M_A25", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2626.001, 654.0017, 789.9937), (-3.2418089545239385e-18, 5.7220458481408876e-05, -0.00012207030837119466), (1.0, 1.0, 1.0), "NonDest_Pillar_5M_A26", _folder)
if a: placed += 1
else: skipped += 1

# Batch 25: StaticMesh'NonDest_Pillar_6M_A' (30 instances)
_mesh_path = "/Game/Art/Assets/Kits/Architecture/Non_D/NonDest_Pillar_6M_A"
_materials = ['/Game/Art/Assets/Kits/Architecture/Suburbs/Materials/Suburbs_Trim_Sheet_A/MI_Suburbs_Trim_Sheet_A']
_folder = "Reconstruction/BD_BB_OrcPrison/Meshes"
a = spawn_static_mesh(_mesh_path, _materials, (280.0011, 2589.999, 805.0), (0.0, 0.0, -0.0), (1.0, 1.0, 1.0), "NonDest_Pillar_4M_A100_1145", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (880.0011, 3809.999, 805.0), (0.0, 0.0, -0.0), (1.0, 1.0, 1.0), "NonDest_Pillar_4M_A102", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1185.0, 3809.999, 805.0), (0.0, 0.0, -0.0), (1.0, 1.0, 1.0), "NonDest_Pillar_4M_A103", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2595.0, 2925.0, 695.0), (0.0, -179.99998633961752, -0.0), (1.0, 1.0, 1.0), "NonDest_Pillar_4M_A58", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2595.0, 2005.0, 695.0), (0.0, 0.0, -0.0), (1.0, 1.0, 1.0), "NonDest_Pillar_4M_A59", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2910.0, 2005.0, 695.0), (0.0, 0.0, -0.0), (1.0, 1.0, 1.0), "NonDest_Pillar_4M_A60", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2905.0, 2925.0, 695.0), (0.0, -179.99998633961752, -0.0), (1.0, 1.0, 1.0), "NonDest_Pillar_4M_A61", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3540.0, 2925.0, 695.0), (0.0, -179.99998633961752, -0.0), (1.0, 1.0, 1.0), "NonDest_Pillar_4M_A65", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3540.0, 2005.0, 695.0), (0.0, 0.0, -0.0), (1.0, 1.0, 1.0), "NonDest_Pillar_4M_A66", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2920.0, 690.0, 695.0), (0.0, 0.0, -0.0), (1.0, 1.0, 1.0), "NonDest_Pillar_4M_A79", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3530.0, 685.0, 675.0), (0.0, 0.0, -0.0), (1.0, 1.0, 1.0), "NonDest_Pillar_4M_A80", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3845.0, 2005.0, 695.0), (0.0, 0.0, -0.0), (1.0, 1.0, 1.0), "NonDest_Pillar_4M_A81", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3845.0, 2925.0, 695.0), (0.0, -179.99998633961752, -0.0), (1.0, 1.0, 1.0), "NonDest_Pillar_4M_A82", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1970.0, 3165.0, 695.0), (0.0, 89.99999818714215, -0.0), (1.0, 1.0, 1.0), "NonDest_Pillar_4M_A83", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1935.0, 3505.0, 695.0), (0.0, -179.99998633961752, -0.0), (1.0, 1.0, 1.0), "NonDest_Pillar_4M_A84", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1580.0, 3499.999, 695.0), (0.0, -179.99998633961752, -0.0), (1.0, 1.0, 1.0), "NonDest_Pillar_4M_A85", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1270.0001, 3499.999, 695.0), (0.0, -179.99998633961752, -0.0), (1.0, 1.0, 1.0), "NonDest_Pillar_4M_A86", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1970.0, 3469.999, 695.0), (0.0, 89.99999818714215, -0.0), (1.0, 1.0, 1.0), "NonDest_Pillar_4M_A87_909", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1235.0001, 3464.999, 695.0), (0.0, -89.99997063746636, 0.0), (1.0, 1.0, 1.0), "NonDest_Pillar_4M_A88", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1235.0001, 2844.999, 695.0), (0.0, -89.99997063746636, 0.0), (1.0, 1.0, 1.0), "NonDest_Pillar_4M_A89", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1270.0001, 2809.999, 695.0), (0.0, 5.340576277714065e-05, -0.0), (1.0, 1.0, 1.0), "NonDest_Pillar_4M_A90", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (880.0011, 2589.999, 805.0), (0.0, 0.0, -0.0), (1.0, 1.0, 1.0), "NonDest_Pillar_4M_A91_986", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1185.0, 2589.999, 805.0), (0.0, 0.0, -0.0), (1.0, 1.0, 1.0), "NonDest_Pillar_4M_A92", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (580.0011, 2589.999, 805.0), (0.0, 0.0, -0.0), (1.0, 1.0, 1.0), "NonDest_Pillar_4M_A93", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (575.0011, 3809.999, 805.0), (0.0, 0.0, -0.0), (1.0, 1.0, 1.0), "NonDest_Pillar_4M_A94_1128", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (275.0011, 3809.999, 805.0), (0.0, 0.0, -0.0), (1.0, 1.0, 1.0), "NonDest_Pillar_4M_A95_1149", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1225.0, 2629.999, 805.0), (0.0, 89.99999818714215, -0.0), (1.0, 1.0, 1.0), "NonDest_Pillar_4M_A96", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1225.0, 2869.999, 805.0), (0.0, 89.99999818714215, -0.0), (1.0, 1.0, 1.0), "NonDest_Pillar_4M_A97", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1225.0, 3474.999, 805.0), (0.0, 89.99999818714215, -0.0), (1.0, 1.0, 1.0), "NonDest_Pillar_4M_A98", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1215.0, 3769.999, 805.0), (0.0, 89.99999818714215, -0.0), (1.0, 1.0, 1.0), "NonDest_Pillar_4M_A99_1120", _folder)
if a: placed += 1
else: skipped += 1

# Batch 26: StaticMesh'NonDest_Trim_3M_B' (37 instances)
_mesh_path = "/Game/Art/Assets/Kits/Architecture/Non_D/NonDest_Trim_3M_B"
_materials = ['/Game/Environments/Materials/MI_Suburbs_Non_Destructible', '/Game/Art/Assets/Kits/Architecture/Suburbs/Materials/Suburbs_Trim_Sheet_A/MI_Suburbs_Trim_Sheet_A']
_folder = "Reconstruction/BD_BB_OrcPrison/Meshes"
a = spawn_static_mesh(_mesh_path, _materials, (3695.0, 2020.0, 680.0), (0.0, -179.99998633961752, -0.0), (1.0, 1.0, 1.0), "BP_Archway_3m_DoorFalse_A129", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3995.0, 2020.0, 680.0), (0.0, -179.99998633961752, -0.0), (1.0, 1.0, 1.0), "BP_Archway_3m_DoorFalse_A130", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3995.0, 2910.0, 680.0), (0.0, 0.0, -0.0), (1.0, 1.0, 1.0), "BP_Archway_3m_DoorFalse_A135", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3695.0, 2910.0, 680.0), (0.0, 0.0, -0.0), (1.0, 1.0, 1.0), "BP_Archway_3m_DoorFalse_A136", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1955.0, 3315.0, 680.0), (0.0, -89.99997063746636, 0.0), (1.0, 1.0, 1.0), "BP_Archway_3m_DoorFalse_A139", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1430.0, 3484.999, 680.0), (0.0, 3.051757709276941e-05, -0.0), (1.0, 1.0, 1.0), "BP_Archway_3m_DoorFalse_A142", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1030.0011, 2609.999, 805.0), (0.0, -179.99998633961752, -0.0), (1.0, 1.0, 1.0), "BP_Archway_3m_DoorFalse_A149", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2450.0, 3620.0, 600.0), (0.0, -179.99998633961752, -0.0), (1.0, 1.0, 1.0), "BP_Archway_3m_DoorFalse_A15", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (730.0011, 2609.999, 805.0), (0.0, -179.99998633961752, -0.0), (1.0, 1.0, 1.0), "BP_Archway_3m_DoorFalse_A150", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (430.0011, 2609.999, 805.0), (0.0, -179.99998633961752, -0.0), (1.0, 1.0, 1.0), "BP_Archway_3m_DoorFalse_A151", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (130.0011, 2609.999, 805.0), (0.0, -179.99998633961752, -0.0), (1.0, 1.0, 1.0), "BP_Archway_3m_DoorFalse_A152", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (730.0011, 3789.999, 805.0), (0.0, 0.0, -0.0), (1.0, 1.0, 1.0), "BP_Archway_3m_DoorFalse_A154_1136", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1030.0011, 3789.999, 805.0), (0.0, 0.0, -0.0), (1.0, 1.0, 1.0), "BP_Archway_3m_DoorFalse_A155_1126", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (430.0011, 3789.999, 805.0), (0.0, 0.0, -0.0), (1.0, 1.0, 1.0), "BP_Archway_3m_DoorFalse_A156_1142", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (130.0011, 3789.999, 805.0), (0.0, 0.0, -0.0), (1.0, 1.0, 1.0), "BP_Archway_3m_DoorFalse_A157", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2750.0, 3620.0, 600.0), (0.0, -179.99998633961752, -0.0), (1.0, 1.0, 1.0), "BP_Archway_3m_DoorFalse_A16", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2150.0, 3620.0, 599.99994), (0.0, -179.99998633961752, -0.0), (1.0, 1.0, 1.0), "BP_Archway_3m_DoorFalse_A17", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1995.0, 3775.0, 600.0), (0.0, 89.99999818714215, -0.0), (1.0, 1.0, 1.0), "BP_Archway_3m_DoorFalse_A25", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1995.0, 4075.0, 599.99994), (0.0, 89.99999818714215, -0.0), (1.0, 1.0, 1.0), "BP_Archway_3m_DoorFalse_A26", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1995.0, 4675.0, 600.0), (0.0, 89.99999818714215, -0.0), (1.0, 1.0, 1.0), "BP_Archway_3m_DoorFalse_A36", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1995.0, 4975.0, 599.99994), (0.0, 89.99999818714215, -0.0), (1.0, 1.0, 1.0), "BP_Archway_3m_DoorFalse_A37", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2149.9922, 5129.994, 599.99994), (0.0, 0.0, -0.0), (1.0, 1.0, 1.0), "BP_Archway_3m_DoorFalse_A42", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3500.0, 4970.0, 600.0), (0.0, -89.99999818714215, 0.0), (1.0, 1.0, 1.0), "BP_Archway_3m_DoorFalse_A48", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3500.0, 4670.0, 599.99994), (0.0, -89.99999818714215, 0.0), (1.0, 1.0, 1.0), "BP_Archway_3m_DoorFalse_A49", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3349.9922, 5129.994, 599.99994), (0.0, 0.0, -0.0), (1.0, 1.0, 1.0), "BP_Archway_3m_DoorFalse_A52", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2917.4922, 5139.994, 599.99994), (0.0, 0.0, -0.0), (1.125, 1.0, 1.0), "BP_Archway_3m_DoorFalse_A57", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2579.9922, 5139.994, 599.99994), (0.0, 0.0, -0.0), (1.125, 1.0, 1.0), "BP_Archway_3m_DoorFalse_A61", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2915.0, 3455.0, 600.0), (0.0, 89.99999818714215, -0.0), (1.0, 1.0, 1.0), "BP_Archway_3m_DoorFalse_A65", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2915.0, 3155.0, 600.0), (0.0, 89.99999818714215, -0.0), (1.0, 1.0, 1.0), "BP_Archway_3m_DoorFalse_A66", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3500.0, 3455.0, 600.0), (0.0, -89.99999818714215, 0.0), (1.0, 1.0, 1.0), "BP_Archway_3m_DoorFalse_A74", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3500.0, 3155.0, 599.99994), (0.0, -89.99999818714215, 0.0), (1.0, 1.0, 1.0), "BP_Archway_3m_DoorFalse_A75", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3500.0, 3755.0, 600.0), (0.0, -89.99999818714215, 0.0), (1.0, 1.0, 1.0), "BP_Archway_3m_DoorFalse_A80", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2745.0, 2910.0, 680.0), (0.0, 0.0, -0.0), (1.0, 1.0, 1.0), "BP_Archway_3m_DoorFalse_A82_573", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2594.9978, 2905.0037, 600.0), (0.0, 0.0, -0.0), (1.0, 1.0, 1.0), "BP_Archway_3m_DoorFalse_A83", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2445.0, 2910.0, 680.0), (0.0, 0.0, -0.0), (1.0, 1.0, 1.0), "BP_Archway_3m_DoorFalse_A88", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2445.0, 2020.0, 680.0), (0.0, -179.99998633961752, -0.0), (1.0, 1.0, 1.0), "BP_Archway_3m_DoorFalse_A93", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2745.0, 2020.0, 680.0), (0.0, -179.99998633961752, -0.0), (1.0, 1.0, 1.0), "BP_Archway_3m_DoorFalse_A94", _folder)
if a: placed += 1
else: skipped += 1

# Batch 27: StaticMesh'Suburbs_Floor_6x6m_A' (2 instances)
_mesh_path = "/Game/Art/Assets/Kits/Architecture/Suburbs/Suburbs_Floor_6x6m_A"
_materials = ['/Game/Environments/ProcTexturing/ProcMaterial_Quarry_2mx5m_B']
_folder = "Reconstruction/BD_BB_OrcPrison/Meshes"
a = spawn_static_mesh(_mesh_path, _materials, (3825.0, 1330.0, 800.0), (0.0, 0.0, -0.0), (1.0, 1.0, 1.0), "Suburbs_Floor_6x6m_A11", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2625.0, 1330.0, 800.0), (0.0, 0.0, -0.0), (1.0, 1.0, 1.0), "Suburbs_Floor_6x6m_A12", _folder)
if a: placed += 1
else: skipped += 1

# Batch 28: StaticMesh'Suburbs_Stairs_Small_C_NonDest' (8 instances)
_mesh_path = "/Game/Art/Assets/Kits/Architecture/Suburbs/Suburbs_Stairs_Small_C_NonDest"
_materials = ['/Game/Art/Assets/Kits/Architecture/Suburbs/Destructable/Materials/MI_Suburbs_Wall_Non_Dest', '/Game/Art/Assets/Kits/Architecture/Suburbs/Materials/Stairs_Medium_C_NonDest/MI_Stairs_Medium_C_NonDes']
_folder = "Reconstruction/BD_BB_OrcPrison/Meshes"
a = spawn_static_mesh(_mesh_path, _materials, (1200.0, 3040.0, 700.0), (0.0, -90.00005166594045, 0.0), (1.0, 1.0, 1.0), "Suburbs_Stairs_Small_C1_11", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3051.25, 1800.0, 705.0), (0.0, 0.0, -0.0), (1.0625, 1.0, 1.0), "Suburbs_Stairs_Small_C2_6", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3370.0, 1800.0, 705.0), (0.0, 0.0, -0.0), (1.0625, 1.0, 1.0), "Suburbs_Stairs_Small_C3", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1200.0, 3340.0, 700.0), (0.0, -90.0001164887758, 0.0), (1.0, 1.0, 1.0), "Suburbs_Stairs_Small_C4", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1900.0, 4380.0, 600.0), (0.0, -90.0001164887758, 0.0), (1.0, 1.0, 1.0503179), "Suburbs_Stairs_Small_C5", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3050.0, 3000.0, 610.0), (0.0, 0.0, -0.0), (1.125, 1.0, 1.0), "Suburbs_Stairs_Small_C6", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3387.5, 3000.0, 610.0), (0.0, 0.0, -0.0), (1.125, 1.0, 1.0), "Suburbs_Stairs_Small_C7", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1200.0, 2740.0, 700.0), (0.0, -90.00005166594045, 0.0), (1.0, 1.0, 1.0), "Suburbs_Stairs_Small_C8", _folder)
if a: placed += 1
else: skipped += 1

# Batch 29: StaticMesh'Suburbs_Wall_Thick_1x1m_A' (2 instances)
_mesh_path = "/Game/Art/Assets/Kits/Architecture/Suburbs/Suburbs_Wall_Thick_1x1m_A"
_materials = ['/Game/Art/Assets/Kits/Architecture/Suburbs/Destructable/Materials/MI_Suburbs_Wall_Non_Dest']
_folder = "Reconstruction/BD_BB_OrcPrison/Meshes"
a = spawn_static_mesh(_mesh_path, _materials, (3580.0, 4550.0, 1200.0), (0.0, 0.0, -0.0), (1.0, 1.0, 1.0), "Suburbs_Wall_Thick_3x1m_A55", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3580.0, 3880.0, 1200.0), (0.0, 0.0, -0.0), (1.0, 1.0, 1.0), "Suburbs_Wall_Thick_3x1m_A58", _folder)
if a: placed += 1
else: skipped += 1

# Batch 30: StaticMesh'Suburbs_Wall_Thick_1x3_A' (11 instances)
_mesh_path = "/Game/Art/Assets/Kits/Architecture/Suburbs/Suburbs_Wall_Thick_1x3_A"
_materials = ['/Game/Art/Assets/Kits/Architecture/Suburbs/Destructable/Materials/MI_Suburbs_Generic_Stone_DMG_A_Dest']
_folder = "Reconstruction/BD_BB_OrcPrison/Meshes"
a = spawn_static_mesh(_mesh_path, _materials, (3250.0, 5250.0, 1200.0), (0.0, 0.0, -0.0), (1.0, 1.0, 1.0), "Suburbs_Wall_Thick_1x3_A17", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1350.0, 4450.0, 1100.0), (0.0, 0.0, -0.0), (1.0, 1.0, 1.0), "Suburbs_Wall_Thick_1x3_A33_466", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1050.0, 4450.0, 1100.0), (0.0, 0.0, -0.0), (1.0, 1.0, 1.0), "Suburbs_Wall_Thick_1x3_A34", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (750.0, 4450.0, 1100.0), (0.0, 0.0, -0.0), (1.0, 1.0, 1.0), "Suburbs_Wall_Thick_1x3_A35", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (650.0, 4650.0, 1100.0), (0.0, -89.99999818714215, 0.0), (1.0, 1.0, 1.0), "Suburbs_Wall_Thick_1x3_A36_471", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (650.0, 4950.0, 1100.0), (0.0, -89.99999818714215, 0.0), (1.0, 1.0, 1.0), "Suburbs_Wall_Thick_1x3_A37", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2650.0, 5150.0, 1300.0), (0.0, 0.0, -0.0), (1.0, 1.0, 1.0), "Suburbs_Wall_Thick_1x3_A59", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2950.0, 5150.0, 1300.0), (0.0, 0.0, -0.0), (1.0, 1.0, 1.0), "Suburbs_Wall_Thick_1x3_A60", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3550.0, 3750.0, 1300.0), (0.0, 89.99999818714215, -0.0), (1.0, 1.0, 1.0), "Suburbs_Wall_Thick_1x3_A77", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3650.0, 4250.0, 1200.0), (0.0, 89.99999818714215, -0.0), (1.0, 1.0, 1.0), "Suburbs_Wall_Thick_1x3_A87", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3650.0, 3950.0, 1200.0), (0.0, 89.99999818714215, -0.0), (1.0, 1.0, 1.0), "Suburbs_Wall_Thick_1x3_A88", _folder)
if a: placed += 1
else: skipped += 1

# Batch 31: StaticMesh'Suburbs_Wall_Thick_1x3_A' (2 instances)
_mesh_path = "/Game/Art/Assets/Kits/Architecture/Suburbs/Suburbs_Wall_Thick_1x3_A"
_materials = ['/Game/Art/Assets/Kits/Architecture/Suburbs/Destructable/Materials/MI_Suburbs_Wall_Non_Dest']
_folder = "Reconstruction/BD_BB_OrcPrison/Meshes"
a = spawn_static_mesh(_mesh_path, _materials, (3550.0, 4050.0, 1270.0), (0.0, 89.99999818714215, -0.0), (1.0, 1.0, 1.0), "Suburbs_Wall_Thick_1x3_A78", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3550.0, 4350.0, 1270.0), (0.0, 89.99999818714215, -0.0), (1.0, 1.0, 1.0), "Suburbs_Wall_Thick_1x3_A79", _folder)
if a: placed += 1
else: skipped += 1

# Batch 32: StaticMesh'Suburbs_Wall_Thick_3x1m_A' (36 instances)
_mesh_path = "/Game/Art/Assets/Kits/Architecture/Suburbs/Suburbs_Wall_Thick_3x1m_A"
_materials = ['/Game/Art/Assets/Kits/Architecture/Suburbs/Destructable/Materials/MI_Suburbs_Wall_Non_Dest']
_folder = "Reconstruction/BD_BB_OrcPrison/Meshes"
a = spawn_static_mesh(_mesh_path, _materials, (3600.0015, 1125.0054, 780.0), (0.0, -179.99998633961752, -0.0), (1.0, 1.0, 1.0), "BP_Archway_3m_DoorFalse_A115", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3600.0015, 1125.0054, 1080.0), (0.0, -179.99998633961752, -0.0), (1.0, 1.0, 1.0), "BP_Archway_3m_DoorFalse_A116", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3600.0015, 1565.0054, 780.0), (0.0, -179.99998633961752, -0.0), (1.0, 1.0, 1.0), "BP_Archway_3m_DoorFalse_A117", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3600.0015, 1565.0054, 1080.0), (0.0, -179.99998633961752, -0.0), (1.0, 1.0, 1.0), "BP_Archway_3m_DoorFalse_A118", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3560.0015, 1175.0054, 1330.0), (2.0490559643782117e-05, -179.99998633961624, -89.99998684315379), (1.0, 1.0, 1.1884475), "BP_Archway_3m_DoorFalse_A119", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1314.9978, 2765.0027, 700.0), (0.0, -179.99998633961752, -0.0), (1.0, 1.0, 1.0), "BP_Archway_3m_DoorFalse_A145_921", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1314.9978, 2765.0027, 1000.0), (0.0, -179.99998633961752, -0.0), (1.0, 1.0, 1.0), "BP_Archway_3m_DoorFalse_A146", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1414.9978, 2765.0027, 700.0), (0.0, -179.99998633961752, -0.0), (1.0, 1.0, 1.0), "BP_Archway_3m_DoorFalse_A147", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1414.9978, 2765.0027, 1000.0), (0.0, -179.99998633961752, -0.0), (1.0, 1.0, 1.0), "BP_Archway_3m_DoorFalse_A148", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2900.0, 2980.0, 1350.0), (1.2032109569415335e-05, -89.99996906028237, 90.00001375099575), (1.0, 1.0, 1.0), "BP_Suburbs_Ceiling_3x3x1m_A123", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3200.0, 2980.0, 1350.0001), (1.2032109569415335e-05, -89.99996906028237, 90.00001375099575), (1.0, 1.0, 1.0), "BP_Suburbs_Ceiling_3x3x1m_A124", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3200.0, 780.0, 1350.0001), (1.2032109569415335e-05, -89.99996906028237, 90.00001375099575), (1.0, 1.0, 1.0), "BP_Suburbs_Ceiling_3x3x1m_A132", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2900.0, 780.0, 1350.0001), (1.2032109569415335e-05, -89.99996906028237, 90.00001375099575), (1.0, 1.0, 1.0), "BP_Suburbs_Ceiling_3x3x1m_A133", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3200.0, 680.0, 1350.0001), (1.2032109569415335e-05, -89.99996906028237, 90.00001375099575), (1.0, 1.0, 1.0), "BP_Suburbs_Ceiling_3x3x1m_A134", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2900.0, 680.0, 1350.0001), (1.2032109569415335e-05, -89.99996906028237, 90.00001375099575), (1.0, 1.0, 1.0), "BP_Suburbs_Ceiling_3x3x1m_A135", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3200.0, 680.0, 1383.0001), (1.2032109569415335e-05, -89.99996906028237, 90.00001375099575), (1.0, 1.0, 1.0), "BP_Suburbs_Ceiling_3x3x1m_A136_707", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3500.0, 680.0, 1383.0001), (1.2032109569415335e-05, -89.99996906028237, 90.00001375099575), (1.0, 1.0, 1.0), "BP_Suburbs_Ceiling_3x3x1m_A137_711", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2900.0, 680.0, 1383.0001), (1.2032109569415335e-05, -89.99996906028237, 90.00001375099575), (1.0, 1.0, 1.0), "BP_Suburbs_Ceiling_3x3x1m_A138_713", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2600.0, 680.0, 1383.0001), (1.2032109569415335e-05, -89.99996906028237, 90.00001375099575), (1.0, 1.0, 1.0), "BP_Suburbs_Ceiling_3x3x1m_A139_715", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3500.0, 680.0, 1350.0001), (1.2032109569415335e-05, -89.99996906028237, 90.00001375099575), (1.0, 1.0, 1.0), "BP_Suburbs_Ceiling_3x3x1m_A140", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2600.0, 680.0, 1350.0001), (1.2032109569415335e-05, -89.99996906028237, 90.00001375099575), (1.0, 1.0, 1.0), "BP_Suburbs_Ceiling_3x3x1m_A141", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2550.0, 650.0, 1100.0), (0.0, 0.0, -0.0), (1.0, 1.0, 1.0), "Suburbs_Wall_Thick_3x1m_A11", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3850.0, 650.0, 1100.0), (0.0, 0.0, -0.0), (1.0, 1.0, 1.0), "Suburbs_Wall_Thick_3x1m_A12", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2550.0, 650.0, 1400.0), (0.0, 0.0, -0.0), (1.0, 1.0, 1.0), "Suburbs_Wall_Thick_3x1m_A13", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3850.0, 650.0, 1400.0), (0.0, 0.0, -0.0), (1.0, 1.0, 1.0), "Suburbs_Wall_Thick_3x1m_A14", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2550.0, 650.0, 1700.0), (0.0, 0.0, -0.0), (1.0, 1.0, 1.0), "Suburbs_Wall_Thick_3x1m_A15", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3850.0, 650.0, 1700.0), (0.0, 0.0, -0.0), (1.0, 1.0, 1.0), "Suburbs_Wall_Thick_3x1m_A16", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2550.0, 650.0, 800.0), (0.0, 0.0, -0.0), (1.0, 1.0, 1.0), "Suburbs_Wall_Thick_3x1m_A3", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4150.0, 2050.0, 1300.0), (0.0, 0.0, -0.0), (1.0, 1.0, 1.0), "Suburbs_Wall_Thick_3x1m_A31", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4150.0, 2950.0, 1300.0), (0.0, 0.0, -0.0), (1.0, 1.0, 1.0), "Suburbs_Wall_Thick_3x1m_A33", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4150.0, 2850.0, 1300.0), (0.0, 0.0, -0.0), (1.0, 1.0, 1.0), "Suburbs_Wall_Thick_3x1m_A34", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3850.0, 650.0, 800.0), (0.0, 0.0, -0.0), (1.0, 1.0, 1.0), "Suburbs_Wall_Thick_3x1m_A4", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3580.0, 4550.0, 600.0), (0.0, 0.0, -0.0), (1.0, 1.0, 1.0), "Suburbs_Wall_Thick_3x1m_A46", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3580.0, 4550.0, 900.0), (0.0, 0.0, -0.0), (1.0, 1.0, 1.0), "Suburbs_Wall_Thick_3x1m_A47", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3580.0, 3880.0, 600.0), (0.0, 0.0, -0.0), (1.0, 1.0, 1.0), "Suburbs_Wall_Thick_3x1m_A56", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3580.0, 3880.0, 900.0), (0.0, 0.0, -0.0), (1.0, 1.0, 1.0), "Suburbs_Wall_Thick_3x1m_A57", _folder)
if a: placed += 1
else: skipped += 1

# Batch 33: StaticMesh'Suburbs_Wall_Thick_3x3m_A' (2 instances)
_mesh_path = "/Game/Art/Assets/Kits/Architecture/Suburbs/Suburbs_Wall_Thick_3x3m_A"
_materials = ['/Game/Art/Assets/Kits/Architecture/Suburbs/Destructable/Materials/MI_Suburbs_Generic_Stone_DMG_A_Dest']
_folder = "Reconstruction/BD_BB_OrcPrison/Meshes"
a = spawn_static_mesh(_mesh_path, _materials, (3250.0, 5250.0, 600.0), (0.0, -179.99998633961752, -0.0), (1.0, 1.0, 1.0), "Suburbs_Wall_Thick_3x3m_A43", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3250.0, 5250.0, 900.0), (0.0, -179.99998633961752, -0.0), (1.0, 1.0, 1.0), "Suburbs_Wall_Thick_3x3m_A44", _folder)
if a: placed += 1
else: skipped += 1

# Batch 34: StaticMesh'Suburbs_Wall_Thick_3x3m_A' (76 instances)
_mesh_path = "/Game/Art/Assets/Kits/Architecture/Suburbs/Suburbs_Wall_Thick_3x3m_A"
_materials = ['/Game/Environments/Materials/MI_Suburbs_Non_Destructible']
_folder = "Reconstruction/BD_BB_OrcPrison/Meshes"
a = spawn_static_mesh(_mesh_path, _materials, (150.0, 2540.0, 800.0), (0.0, 0.0, -0.0), (1.0, 1.0, 1.0), "Suburbs_Wall_Thick_3x3m_A_106", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1245.0, 3615.0, 1000.0), (0.0, -89.99999818714215, 0.0), (1.0, 1.0, 1.0), "Suburbs_Wall_Thick_3x3m_A108", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1245.0, 2715.0, 700.0), (0.0, -89.99999818714215, 0.0), (1.0, 1.0, 1.0), "Suburbs_Wall_Thick_3x3m_A109", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1245.0, 2715.0, 1000.0), (0.0, -89.99999818714215, 0.0), (1.0, 1.0, 1.0), "Suburbs_Wall_Thick_3x3m_A110", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1235.0, 2715.0, 1820.0), (0.0, -89.99999818714215, 0.0), (1.0, 1.0, 1.0), "Suburbs_Wall_Thick_3x3m_A111", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1235.0, 3015.0, 1820.0), (0.0, -89.99999818714215, 0.0), (1.0, 1.0, 1.0), "Suburbs_Wall_Thick_3x3m_A114_966", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1235.0, 3335.0, 1820.0), (0.0, -89.99999818714215, 0.0), (1.0, 1.0, 1.0), "Suburbs_Wall_Thick_3x3m_A115_968", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1235.0, 3635.0, 1820.0), (0.0, -89.99999818714215, 0.0), (1.0, 1.0, 1.0), "Suburbs_Wall_Thick_3x3m_A118", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (749.9999, 3849.9998, 1400.0), (0.0, -179.99998633961752, -0.0), (1.0, 1.0, 1.0), "Suburbs_Wall_Thick_3x3m_A119", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (449.99988, 3849.9998, 1400.0), (0.0, -179.99998633961752, -0.0), (1.0, 1.0, 1.0), "Suburbs_Wall_Thick_3x3m_A120", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (150.0, 3850.0, 1400.0), (0.0, -179.99998633961752, -0.0), (1.0, 1.0, 1.0), "Suburbs_Wall_Thick_3x3m_A121", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1049.9999, 3849.9995, 1700.0), (0.0, -179.99998633961752, -0.0), (1.0, 1.0, 1.0), "Suburbs_Wall_Thick_3x3m_A122", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (749.9999, 3849.9998, 1700.0), (0.0, -179.99998633961752, -0.0), (1.0, 1.0, 1.0), "Suburbs_Wall_Thick_3x3m_A123", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (449.99988, 3849.9998, 1700.0), (0.0, -179.99998633961752, -0.0), (1.0, 1.0, 1.0), "Suburbs_Wall_Thick_3x3m_A124_1086", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (150.0, 3850.0, 1700.0), (0.0, -179.99998633961752, -0.0), (1.0, 1.0, 1.0), "Suburbs_Wall_Thick_3x3m_A125_1087", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1245.0, 2755.0, 1400.0), (0.0, -89.99999818714215, 0.0), (1.0, 1.0, 1.0), "Suburbs_Wall_Thick_3x3m_A130_1091", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1245.0, 3055.0, 1400.0), (0.0, -89.99999818714215, 0.0), (1.0, 1.0, 1.0), "Suburbs_Wall_Thick_3x3m_A131_1093", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1245.0, 3355.0, 1400.0), (0.0, -89.99999818714215, 0.0), (1.0, 1.0, 1.0), "Suburbs_Wall_Thick_3x3m_A136", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1245.0, 3655.0, 1400.0), (0.0, -89.99999818714215, 0.0), (1.0, 1.0, 1.0), "Suburbs_Wall_Thick_3x3m_A137", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1245.0, 2755.0, 1700.0), (0.0, -89.99999818714215, 0.0), (1.0, 1.0, 1.0), "Suburbs_Wall_Thick_3x3m_A138", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1245.0, 3055.0, 1700.0), (0.0, -89.99999818714215, 0.0), (1.0, 1.0, 1.0), "Suburbs_Wall_Thick_3x3m_A139", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3681.001, 709.0016, 1399.9935), (1.0300772226861994e-18, 4.577636793101723e-05, -9.155273700793543e-05), (1.0, 1.0, 1.0), "Suburbs_Wall_Thick_3x3m_A140", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3381.001, 709.0016, 1399.9939), (1.0300772226861994e-18, 4.577636793101723e-05, -9.155273700793543e-05), (1.0, 1.0, 1.0), "Suburbs_Wall_Thick_3x3m_A141", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3081.001, 709.00183, 1399.9941), (1.0300772226861994e-18, 4.577636793101723e-05, -9.155273700793543e-05), (1.0, 1.0, 1.0), "Suburbs_Wall_Thick_3x3m_A142", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2781.0017, 709.0023, 1399.9939), (1.0300772226861994e-18, 4.577636793101723e-05, -9.155273700793543e-05), (1.0, 1.0, 1.0), "Suburbs_Wall_Thick_3x3m_A143", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3681.001, 709.0011, 1699.9937), (1.0300772226861994e-18, 4.577636793101723e-05, -9.155273700793543e-05), (1.0, 1.0, 1.0), "Suburbs_Wall_Thick_3x3m_A144", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3381.0015, 709.0011, 1699.994), (1.0300772226861994e-18, 4.577636793101723e-05, -9.155273700793543e-05), (1.0, 1.0, 1.0), "Suburbs_Wall_Thick_3x3m_A145", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1245.0, 3355.0, 1700.0), (0.0, -89.99999818714215, 0.0), (1.0, 1.0, 1.0), "Suburbs_Wall_Thick_3x3m_A153_1100", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1245.0, 3655.0, 1700.0), (0.0, -89.99999818714215, 0.0), (1.0, 1.0, 1.0), "Suburbs_Wall_Thick_3x3m_A155_1101", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1095.0, 3605.0, 2050.0), (-5.729578616208919e-07, -89.99998968675763, -89.99998968675763), (1.0, 1.0, 1.0), "Suburbs_Wall_Thick_3x3m_A161", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (795.0, 3605.0, 2050.0), (-5.729578616208919e-07, -89.99998968675763, -89.99998968675763), (1.0, 1.0, 1.0), "Suburbs_Wall_Thick_3x3m_A162", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (495.0, 3605.0, 2050.0), (-5.729578616208919e-07, -89.99998968675763, -89.99998968675763), (1.0, 1.0, 1.0), "Suburbs_Wall_Thick_3x3m_A163", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1095.0, 3305.0, 2050.0), (-5.729578616208919e-07, -89.99998968675763, -89.99998968675763), (1.0, 1.0, 1.0), "Suburbs_Wall_Thick_3x3m_A164", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (795.0, 3305.0, 2050.0), (-5.729578616208919e-07, -89.99998968675763, -89.99998968675763), (1.0, 1.0, 1.0), "Suburbs_Wall_Thick_3x3m_A165", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (495.0, 3305.0, 2050.0), (-5.729578616208919e-07, -89.99998968675763, -89.99998968675763), (1.0, 1.0, 1.0), "Suburbs_Wall_Thick_3x3m_A166", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1095.0, 3005.0, 2050.0), (-5.729578616208919e-07, -89.99998968675763, -89.99998968675763), (1.0, 1.0, 1.0), "Suburbs_Wall_Thick_3x3m_A167", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (795.0, 3005.0, 2050.0), (-5.729578616208919e-07, -89.99998968675763, -89.99998968675763), (1.0, 1.0, 1.0), "Suburbs_Wall_Thick_3x3m_A168", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (495.0, 3005.0, 2050.0), (-5.729578616208919e-07, -89.99998968675763, -89.99998968675763), (1.0, 1.0, 1.0), "Suburbs_Wall_Thick_3x3m_A169", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1095.0, 2705.0, 2050.0), (-5.729578616208919e-07, -89.99998968675763, -89.99998968675763), (1.0, 1.0, 1.0), "Suburbs_Wall_Thick_3x3m_A170", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (795.0, 2705.0, 2050.0), (-5.729578616208919e-07, -89.99998968675763, -89.99998968675763), (1.0, 1.0, 1.0), "Suburbs_Wall_Thick_3x3m_A171", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (495.0, 2705.0, 2050.0), (-5.729578616208919e-07, -89.99998968675763, -89.99998968675763), (1.0, 1.0, 1.0), "Suburbs_Wall_Thick_3x3m_A172", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3081.0012, 709.00134, 1699.9943), (1.0300772226861994e-18, 4.577636793101723e-05, -9.155273700793543e-05), (1.0, 1.0, 1.0), "Suburbs_Wall_Thick_3x3m_A179", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2781.0017, 709.0016, 1699.9941), (1.0300772226861994e-18, 4.577636793101723e-05, -9.155273700793543e-05), (1.0, 1.0, 1.0), "Suburbs_Wall_Thick_3x3m_A180", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2800.0, 650.0, 1950.0), (0.0, 0.0, -90.00002735739477), (1.0, 1.0, 1.0), "Suburbs_Wall_Thick_3x3m_A19", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1050.0, 3859.9998, 800.0), (0.0, -179.99998633961752, -0.0), (1.0, 1.0, 1.0), "Suburbs_Wall_Thick_3x3m_A2_1078", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2800.0, 350.0, 1950.0), (0.0, 0.0, -90.00002735739477), (1.0, 1.0, 1.0), "Suburbs_Wall_Thick_3x3m_A20", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3100.0, 650.0, 1950.0), (0.0, 0.0, -90.00002735739477), (1.0, 1.0, 1.0), "Suburbs_Wall_Thick_3x3m_A21", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3100.0, 350.0, 1950.0), (0.0, 0.0, -90.00002735739477), (1.0, 1.0, 1.0), "Suburbs_Wall_Thick_3x3m_A22", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3400.0, 650.0, 1950.0), (0.0, 0.0, -90.00002735739477), (1.0, 1.0, 1.0), "Suburbs_Wall_Thick_3x3m_A23", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3400.0, 350.0, 1950.0), (0.0, 0.0, -90.00002735739477), (1.0, 1.0, 1.0), "Suburbs_Wall_Thick_3x3m_A24", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3700.0, 650.0, 1950.0), (0.0, 0.0, -90.00002735739477), (1.0, 1.0, 1.0), "Suburbs_Wall_Thick_3x3m_A25", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3700.0, 350.0, 1950.0), (0.0, 0.0, -90.00002735739477), (1.0, 1.0, 1.0), "Suburbs_Wall_Thick_3x3m_A26", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (450.0, 2540.0, 800.0), (0.0, 0.0, -0.0), (1.0, 1.0, 1.0), "Suburbs_Wall_Thick_3x3m_A3", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (750.0, 2540.0, 800.0), (0.0, 0.0, -0.0), (1.0, 1.0, 1.0), "Suburbs_Wall_Thick_3x3m_A4", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1050.0, 2540.0, 800.0), (0.0, 0.0, -0.0), (1.0, 1.0, 1.0), "Suburbs_Wall_Thick_3x3m_A5", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (150.0, 2540.0, 1100.0), (0.0, 0.0, -0.0), (1.0, 1.0, 1.0), "Suburbs_Wall_Thick_3x3m_A53", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1050.0, 3859.9998, 1100.0), (0.0, -179.99998633961752, -0.0), (1.0, 1.0, 1.0), "Suburbs_Wall_Thick_3x3m_A54_1081", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (450.0, 2540.0, 1100.0), (0.0, 0.0, -0.0), (1.0, 1.0, 1.0), "Suburbs_Wall_Thick_3x3m_A55", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (750.0, 2540.0, 1100.0), (0.0, 0.0, -0.0), (1.0, 1.0, 1.0), "Suburbs_Wall_Thick_3x3m_A56", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1050.0, 2540.0, 1100.0), (0.0, 0.0, -0.0), (1.0, 1.0, 1.0), "Suburbs_Wall_Thick_3x3m_A57", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1245.0, 3615.0, 700.0), (0.0, -89.99999818714215, 0.0), (1.0, 1.0, 1.0), "Suburbs_Wall_Thick_3x3m_A58", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (750.0, 3859.9998, 800.0), (0.0, -179.99998633961752, -0.0), (1.0, 1.0, 1.0), "Suburbs_Wall_Thick_3x3m_A6", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (750.0, 3859.9998, 1100.0), (0.0, -179.99998633961752, -0.0), (1.0, 1.0, 1.0), "Suburbs_Wall_Thick_3x3m_A60_1082", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (450.0, 3859.9998, 1100.0), (0.0, -179.99998633961752, -0.0), (1.0, 1.0, 1.0), "Suburbs_Wall_Thick_3x3m_A61_1083", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (150.0, 3860.0, 1100.0), (0.0, -179.99998633961752, -0.0), (1.0, 1.0, 1.0), "Suburbs_Wall_Thick_3x3m_A62_1084", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (150.0, 2550.0, 1400.0), (0.0, 0.0, -0.0), (1.0, 1.0, 1.0), "Suburbs_Wall_Thick_3x3m_A63", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1049.9999, 3849.9995, 1400.0), (0.0, -179.99998633961752, -0.0), (1.0, 1.0, 1.0), "Suburbs_Wall_Thick_3x3m_A64_1085", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (450.0, 2550.0, 1400.0), (0.0, 0.0, -0.0), (1.0, 1.0, 1.0), "Suburbs_Wall_Thick_3x3m_A65", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (750.0, 2550.0, 1400.0), (0.0, 0.0, -0.0), (1.0, 1.0, 1.0), "Suburbs_Wall_Thick_3x3m_A66", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1050.0, 2550.0, 1400.0), (0.0, 0.0, -0.0), (1.0, 1.0, 1.0), "Suburbs_Wall_Thick_3x3m_A67", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (150.0, 2550.0, 1700.0), (0.0, 0.0, -0.0), (1.0, 1.0, 1.0), "Suburbs_Wall_Thick_3x3m_A73", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (450.0, 2550.0, 1700.0), (0.0, 0.0, -0.0), (1.0, 1.0, 1.0), "Suburbs_Wall_Thick_3x3m_A75", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (750.0, 2550.0, 1700.0), (0.0, 0.0, -0.0), (1.0, 1.0, 1.0), "Suburbs_Wall_Thick_3x3m_A76", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1050.0, 2550.0, 1700.0), (0.0, 0.0, -0.0), (1.0, 1.0, 1.0), "Suburbs_Wall_Thick_3x3m_A77", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (450.0, 3859.9998, 800.0), (0.0, -179.99998633961752, -0.0), (1.0, 1.0, 1.0), "Suburbs_Wall_Thick_3x3m_A8_1079", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (150.0, 3860.0, 800.0), (0.0, -179.99998633961752, -0.0), (1.0, 1.0, 1.0), "Suburbs_Wall_Thick_3x3m_A9_1080", _folder)
if a: placed += 1
else: skipped += 1

# Batch 35: StaticMesh'Suburbs_Wall_Thick_3x3m_A' (101 instances)
_mesh_path = "/Game/Art/Assets/Kits/Architecture/Suburbs/Suburbs_Wall_Thick_3x3m_A"
_materials = ['/Game/Art/Assets/Kits/Architecture/Suburbs/Destructable/Materials/MI_Suburbs_Wall_Non_Dest']
_folder = "Reconstruction/BD_BB_OrcPrison/Meshes"
a = spawn_static_mesh(_mesh_path, _materials, (2150.0, 4830.0, 1350.0), (0.0, 0.0, 90.0000030488508), (1.0, 1.0, 1.0), "BP_Suburbs_Ceiling_3x3x1m_A103", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2150.0, 3930.0, 1350.0), (0.0, 0.0, 90.0000030488508), (1.0, 1.0, 1.0), "BP_Suburbs_Ceiling_3x3x1m_A104", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2150.0, 3630.0, 1350.0), (0.0, 0.0, 90.0000030488508), (1.0, 1.0, 1.0), "BP_Suburbs_Ceiling_3x3x1m_A105", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3500.0, 3800.0002, 1350.0), (6.302533138247408e-06, -89.999969060283, 90.00000916733106), (1.0, 1.0, 1.0), "BP_Suburbs_Ceiling_3x3x1m_A106", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2600.0, 3780.0, 1350.0), (6.302533138247408e-06, -89.999969060283, 90.00000916733106), (1.0, 1.0, 1.0), "BP_Suburbs_Ceiling_3x3x1m_A107", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2300.0, 3780.0, 1350.0), (6.302533138247408e-06, -89.999969060283, 90.00000916733106), (1.0, 1.0, 1.0), "BP_Suburbs_Ceiling_3x3x1m_A108", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2450.0, 4830.0, 1350.0), (0.0, 0.0, 90.0000030488508), (1.0, 1.0, 1.0), "BP_Suburbs_Ceiling_3x3x1m_A109", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2750.0, 4830.0, 1350.0), (0.0, 0.0, 90.0000030488508), (1.0, 1.0, 1.0), "BP_Suburbs_Ceiling_3x3x1m_A110", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3050.0, 4830.0, 1350.0), (0.0, 0.0, 90.0000030488508), (1.0, 1.0, 1.0), "BP_Suburbs_Ceiling_3x3x1m_A111", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3350.0, 4830.0, 1350.0), (0.0, 0.0, 90.0000030488508), (1.0, 1.0, 1.0), "BP_Suburbs_Ceiling_3x3x1m_A112", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3200.0, 4680.0, 1350.0001), (1.2032109569415335e-05, -89.99996906028237, 90.00001375099575), (1.0, 1.0, 1.0), "BP_Suburbs_Ceiling_3x3x1m_A113", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2900.0, 4080.0, 1450.0), (1.2032109569415335e-05, -89.99996906028237, 90.00001375099575), (1.0, 1.0, 1.0), "BP_Suburbs_Ceiling_3x3x1m_A114", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2600.0, 4080.0, 1450.0), (1.2032109569415335e-05, -89.99996906028237, 90.00001375099575), (1.0, 1.0, 1.0), "BP_Suburbs_Ceiling_3x3x1m_A115", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2300.0, 4080.0, 1450.0), (1.2032109569415335e-05, -89.99996906028237, 90.00001375099575), (1.0, 1.0, 1.0), "BP_Suburbs_Ceiling_3x3x1m_A116", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2900.0, 4380.0, 1450.0), (1.2032109569415335e-05, -89.99996906028237, 90.00001375099575), (1.0, 1.0, 1.0), "BP_Suburbs_Ceiling_3x3x1m_A117", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2600.0, 4380.0, 1450.0), (1.2032109569415335e-05, -89.99996906028237, 90.00001375099575), (1.0, 1.0, 1.0), "BP_Suburbs_Ceiling_3x3x1m_A118", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2300.0, 4380.0, 1450.0), (1.2032109569415335e-05, -89.99996906028237, 90.00001375099575), (1.0, 1.0, 1.0), "BP_Suburbs_Ceiling_3x3x1m_A119", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2900.0, 4680.0, 1450.0), (1.2032109569415335e-05, -89.99996906028237, 90.00001375099575), (1.0, 1.0, 1.0), "BP_Suburbs_Ceiling_3x3x1m_A120", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2600.0, 4680.0, 1450.0), (1.2032109569415335e-05, -89.99996906028237, 90.00001375099575), (1.0, 1.0, 1.0), "BP_Suburbs_Ceiling_3x3x1m_A121", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2300.0, 4680.0, 1450.0), (1.2032109569415335e-05, -89.99996906028237, 90.00001375099575), (1.0, 1.0, 1.0), "BP_Suburbs_Ceiling_3x3x1m_A122", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2600.0, 2180.0, 1350.0), (1.2032109569415335e-05, -89.99996906028237, 90.00001375099575), (1.0, 1.0, 1.0), "BP_Suburbs_Ceiling_3x3x1m_A125_597", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2300.0, 2780.0, 1350.0), (1.2032109569415335e-05, -89.99996906028237, 90.00001375099575), (1.0, 1.0, 1.0), "BP_Suburbs_Ceiling_3x3x1m_A126_601", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2300.0, 2480.0, 1350.0), (1.2032109569415335e-05, -89.99996906028237, 90.00001375099575), (1.0, 1.0, 1.0), "BP_Suburbs_Ceiling_3x3x1m_A127", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2300.0, 2180.0, 1350.0), (1.2032109569415335e-05, -89.99996906028237, 90.00001375099575), (1.0, 1.0, 1.0), "BP_Suburbs_Ceiling_3x3x1m_A128", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2000.0, 2780.0, 1350.0), (1.2032109569415335e-05, -89.99996906028237, 90.00001375099575), (1.0, 1.0, 1.0), "BP_Suburbs_Ceiling_3x3x1m_A129", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2000.0, 2480.0, 1350.0), (1.2032109569415335e-05, -89.99996906028237, 90.00001375099575), (1.0, 1.0, 1.0), "BP_Suburbs_Ceiling_3x3x1m_A130", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2000.0, 2180.0, 1350.0), (1.2032109569415335e-05, -89.99996906028237, 90.00001375099575), (1.0, 1.0, 1.0), "BP_Suburbs_Ceiling_3x3x1m_A131", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3850.0, 2780.0, 1350.0), (1.2032109569415335e-05, -89.99996906028237, 90.00001375099575), (1.0, 1.0, 1.0), "BP_Suburbs_Ceiling_3x3x1m_A142", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3850.0, 2480.0, 1350.0), (1.2032109569415335e-05, -89.99996906028237, 90.00001375099575), (1.0, 1.0, 1.0), "BP_Suburbs_Ceiling_3x3x1m_A143", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3550.0, 2780.0, 1350.0), (1.2032109569415335e-05, -89.99996906028237, 90.00001375099575), (1.0, 1.0, 1.0), "BP_Suburbs_Ceiling_3x3x1m_A144", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3550.0, 2480.0, 1350.0), (1.2032109569415335e-05, -89.99996906028237, 90.00001375099575), (1.0, 1.0, 1.0), "BP_Suburbs_Ceiling_3x3x1m_A145", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3850.0, 2180.0, 1350.0), (1.2032109569415335e-05, -89.99996906028237, 90.00001375099575), (1.0, 1.0, 1.0), "BP_Suburbs_Ceiling_3x3x1m_A146", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3550.0, 2180.0, 1350.0), (1.2032109569415335e-05, -89.99996906028237, 90.00001375099575), (1.0, 1.0, 1.0), "BP_Suburbs_Ceiling_3x3x1m_A147", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1700.0, 2780.0, 1350.0), (1.2032109569415335e-05, -89.99996906028237, 90.00001375099575), (1.0, 1.0, 1.0), "BP_Suburbs_Ceiling_3x3x1m_A148", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1700.0, 2480.0, 1350.0), (1.2032109569415335e-05, -89.99996906028237, 90.00001375099575), (1.0, 1.0, 1.0), "BP_Suburbs_Ceiling_3x3x1m_A149", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1700.0, 3080.0, 1350.0), (1.2032109569415335e-05, -89.99996906028237, 90.00001375099575), (1.0, 1.0, 1.0), "BP_Suburbs_Ceiling_3x3x1m_A150", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1700.0, 3380.0, 1350.0), (1.2032109569415335e-05, -89.99996906028237, 90.00001375099575), (1.0, 1.0, 1.0), "BP_Suburbs_Ceiling_3x3x1m_A151", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1400.0, 2780.0, 1350.0), (1.2032109569415335e-05, -89.99996906028237, 90.00001375099575), (1.0, 1.0, 1.0), "BP_Suburbs_Ceiling_3x3x1m_A152", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1400.0, 3080.0, 1350.0), (1.2032109569415335e-05, -89.99996906028237, 90.00001375099575), (1.0, 1.0, 1.0), "BP_Suburbs_Ceiling_3x3x1m_A153", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1400.0, 3380.0, 1350.0), (1.2032109569415335e-05, -89.99996906028237, 90.00001375099575), (1.0, 1.0, 1.0), "BP_Suburbs_Ceiling_3x3x1m_A154", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1169.996, 3080.0, 1350.0), (1.2032109569415335e-05, -89.99996906028237, 90.00001375099575), (1.0, 1.0, 0.7712196), "BP_Suburbs_Ceiling_3x3x1m_A155_935", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1169.9922, 3380.0, 1349.9979), (1.2032109569415335e-05, -89.99996906028237, 90.00001375099575), (1.0, 1.0, 0.7712196), "BP_Suburbs_Ceiling_3x3x1m_A156_936", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1170.0, 2780.0, 1350.0), (1.2032109569415335e-05, -89.99996906028237, 90.00001375099575), (1.0, 1.0, 0.7712196), "BP_Suburbs_Ceiling_3x3x1m_A157", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1170.0, 3680.0, 1350.0), (1.2032109569415335e-05, -89.99996906028237, 90.00001375099575), (1.0, 1.0, 1.0), "BP_Suburbs_Ceiling_3x3x1m_A158", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1750.0, 3630.0, 1150.0), (0.0, 0.0, 90.0000030488508), (1.0, 1.0, 1.0), "BP_Suburbs_Ceiling_3x3x1m_A159", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1750.0, 3930.0, 1150.0), (0.0, 0.0, 90.0000030488508), (1.0, 1.0, 1.0), "BP_Suburbs_Ceiling_3x3x1m_A160", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1750.0, 4230.0, 1150.0), (0.0, 0.0, 90.0000030488508), (1.0, 1.0, 1.0), "BP_Suburbs_Ceiling_3x3x1m_A161", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1750.0, 4530.0, 1150.0), (0.0, 0.0, 90.0000030488508), (1.0, 1.0, 1.0), "BP_Suburbs_Ceiling_3x3x1m_A162", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1750.0, 4830.0, 1150.0), (0.0, 0.0, 90.0000030488508), (1.0, 1.0, 1.0), "BP_Suburbs_Ceiling_3x3x1m_A163", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1450.0, 4530.0, 1150.0), (0.0, 0.0, 90.0000030488508), (1.0, 1.0, 1.0), "BP_Suburbs_Ceiling_3x3x1m_A164", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1450.0, 4830.0, 1150.0), (0.0, 0.0, 90.0000030488508), (1.0, 1.0, 1.0), "BP_Suburbs_Ceiling_3x3x1m_A165", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1150.0, 4530.0, 1150.0), (0.0, 0.0, 90.0000030488508), (1.0, 1.0, 1.0), "BP_Suburbs_Ceiling_3x3x1m_A166", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1150.0, 4830.0, 1150.0), (0.0, 0.0, 90.0000030488508), (1.0, 1.0, 1.0), "BP_Suburbs_Ceiling_3x3x1m_A167", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (850.0, 4530.0, 1150.0), (0.0, 0.0, 90.0000030488508), (1.0, 1.0, 1.0), "BP_Suburbs_Ceiling_3x3x1m_A168", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (850.0, 4830.0, 1150.0), (0.0, 0.0, 90.0000030488508), (1.0, 1.0, 1.0), "BP_Suburbs_Ceiling_3x3x1m_A169", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1750.0, 5180.0, 1150.0), (0.0, 0.0, 90.0000030488508), (1.0, 1.0, 1.0), "BP_Suburbs_Ceiling_3x3x1m_A170_97", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1450.0, 5180.0, 1150.0), (0.0, 0.0, 90.0000030488508), (1.0, 1.0, 1.0), "BP_Suburbs_Ceiling_3x3x1m_A171_99", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1750.0, 5480.0, 1150.0), (0.0, 0.0, 90.0000030488508), (1.0, 1.0, 1.0), "BP_Suburbs_Ceiling_3x3x1m_A172_102", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1450.0, 5480.0, 1150.0), (0.0, 0.0, 90.0000030488508), (1.0, 1.0, 1.0), "BP_Suburbs_Ceiling_3x3x1m_A173_103", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2150.0, 4230.0, 1350.0), (0.0, 0.0, 90.0000030488508), (1.0, 1.0, 1.0), "BP_Suburbs_Ceiling_3x3x1m_A33", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2900.0, 3780.0, 1350.0), (6.302533138247408e-06, -89.999969060283, 90.00000916733106), (1.0, 1.0, 1.0), "BP_Suburbs_Ceiling_3x3x1m_A40_141", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2150.0, 4530.0, 1350.0), (0.0, 0.0, 90.0000030488508), (1.0, 1.0, 1.0), "BP_Suburbs_Ceiling_3x3x1m_A41_132", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3200.0, 3780.0, 1350.0001), (6.302533138247408e-06, -89.999969060283, 90.00000916733106), (1.0, 1.0, 1.0), "BP_Suburbs_Ceiling_3x3x1m_A42_142", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3200.0, 4080.0, 1350.0001), (1.2032109569415335e-05, -89.99996906028237, 90.00001375099575), (1.0, 1.0, 1.0), "BP_Suburbs_Ceiling_3x3x1m_A43", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3200.0, 4380.0, 1350.0001), (1.2032109569415335e-05, -89.99996906028237, 90.00001375099575), (1.0, 1.0, 1.0), "BP_Suburbs_Ceiling_3x3x1m_A44", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2900.0, 3480.0, 1350.0), (1.2032109569415335e-05, -89.99996906028237, 90.00001375099575), (1.0, 1.0, 1.0), "BP_Suburbs_Ceiling_3x3x1m_A45_403", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3200.0, 3480.0, 1350.0001), (1.2032109569415335e-05, -89.99996906028237, 90.00001375099575), (1.0, 1.0, 1.0), "BP_Suburbs_Ceiling_3x3x1m_A46_404", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2900.0, 3180.0, 1350.0), (1.2032109569415335e-05, -89.99996906028237, 90.00001375099575), (1.0, 1.0, 1.0), "BP_Suburbs_Ceiling_3x3x1m_A47_407", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3200.0, 3180.0, 1350.0001), (1.2032109569415335e-05, -89.99996906028237, 90.00001375099575), (1.0, 1.0, 1.0), "BP_Suburbs_Ceiling_3x3x1m_A48_408", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2900.0, 2780.0, 1350.0), (1.2032109569415335e-05, -89.99996906028237, 90.00001375099575), (1.0, 1.0, 1.0), "BP_Suburbs_Ceiling_3x3x1m_A49_496", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3200.0, 2780.0, 1350.0001), (1.2032109569415335e-05, -89.99996906028237, 90.00001375099575), (1.0, 1.0, 1.0), "BP_Suburbs_Ceiling_3x3x1m_A50_497", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2900.0, 2480.0, 1350.0), (1.2032109569415335e-05, -89.99996906028237, 90.00001375099575), (1.0, 1.0, 1.0), "BP_Suburbs_Ceiling_3x3x1m_A51_500", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3200.0, 2480.0, 1350.0001), (1.2032109569415335e-05, -89.99996906028237, 90.00001375099575), (1.0, 1.0, 1.0), "BP_Suburbs_Ceiling_3x3x1m_A52_501", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2900.0, 2180.0, 1350.0), (1.2032109569415335e-05, -89.99996906028237, 90.00001375099575), (1.0, 1.0, 1.0), "BP_Suburbs_Ceiling_3x3x1m_A53_506", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3200.0, 2180.0, 1350.0001), (1.2032109569415335e-05, -89.99996906028237, 90.00001375099575), (1.0, 1.0, 1.0), "BP_Suburbs_Ceiling_3x3x1m_A54_507", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2900.0, 1880.0, 1350.0), (1.2032109569415335e-05, -89.99996906028237, 90.00001375099575), (1.0, 1.0, 1.0), "BP_Suburbs_Ceiling_3x3x1m_A55_508", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3200.0, 1880.0, 1350.0001), (1.2032109569415335e-05, -89.99996906028237, 90.00001375099575), (1.0, 1.0, 1.0), "BP_Suburbs_Ceiling_3x3x1m_A56_509", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2900.0, 1580.0, 1350.0), (1.2032109569415335e-05, -89.99996906028237, 90.00001375099575), (1.0, 1.0, 1.0), "BP_Suburbs_Ceiling_3x3x1m_A57_514", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3200.0, 1580.0, 1350.0001), (1.2032109569415335e-05, -89.99996906028237, 90.00001375099575), (1.0, 1.0, 1.0), "BP_Suburbs_Ceiling_3x3x1m_A58_515", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2900.0, 1280.0, 1350.0), (1.2032109569415335e-05, -89.99996906028237, 90.00001375099575), (1.0, 1.0, 1.0), "BP_Suburbs_Ceiling_3x3x1m_A59_516", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3200.0, 1280.0, 1350.0001), (1.2032109569415335e-05, -89.99996906028237, 90.00001375099575), (1.0, 1.0, 1.0), "BP_Suburbs_Ceiling_3x3x1m_A60_517", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2900.0, 980.0, 1350.0), (1.2032109569415335e-05, -89.99996906028237, 90.00001375099575), (1.0, 1.0, 1.0), "BP_Suburbs_Ceiling_3x3x1m_A61_520", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3200.0, 980.0, 1350.0001), (1.2032109569415335e-05, -89.99996906028237, 90.00001375099575), (1.0, 1.0, 1.0), "BP_Suburbs_Ceiling_3x3x1m_A62_521", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2600.0, 2780.0, 1350.0), (1.2032109569415335e-05, -89.99996906028237, 90.00001375099575), (1.0, 1.0, 1.0), "BP_Suburbs_Ceiling_3x3x1m_A71_595", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2600.0, 2480.0, 1350.0), (1.2032109569415335e-05, -89.99996906028237, 90.00001375099575), (1.0, 1.0, 1.0), "BP_Suburbs_Ceiling_3x3x1m_A74_596", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2550.0, 150.0, 800.0), (0.0, 90.0000030488508, -0.0), (1.0, 1.0, 1.0), "Suburbs_Wall_Thick_3x3m_A11", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2550.0, 450.0, 800.0), (0.0, 90.0000030488508, -0.0), (1.0, 1.0, 1.0), "Suburbs_Wall_Thick_3x3m_A12", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3850.0, 150.0, 800.0), (0.0, 90.0000030488508, -0.0), (1.0, 1.0, 1.0), "Suburbs_Wall_Thick_3x3m_A13", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3850.0, 450.0, 800.0), (0.0, 90.0000030488508, -0.0), (1.0, 1.0, 1.0), "Suburbs_Wall_Thick_3x3m_A14", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2550.0, 150.0, 1100.0), (0.0, 90.0000030488508, -0.0), (1.0, 1.0, 1.0), "Suburbs_Wall_Thick_3x3m_A83", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2550.0, 450.0, 1100.0), (0.0, 90.0000030488508, -0.0), (1.0, 1.0, 1.0), "Suburbs_Wall_Thick_3x3m_A84", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3850.0, 150.0, 1100.0), (0.0, 90.0000030488508, -0.0), (1.0, 1.0, 1.0), "Suburbs_Wall_Thick_3x3m_A85", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3850.0, 450.0, 1100.0), (0.0, 90.0000030488508, -0.0), (1.0, 1.0, 1.0), "Suburbs_Wall_Thick_3x3m_A86", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2550.0, 150.0, 1400.0), (0.0, 90.0000030488508, -0.0), (1.0, 1.0, 1.0), "Suburbs_Wall_Thick_3x3m_A89", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2550.0, 450.0, 1400.0), (0.0, 90.0000030488508, -0.0), (1.0, 1.0, 1.0), "Suburbs_Wall_Thick_3x3m_A90", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3850.0, 150.0, 1400.0), (0.0, 90.0000030488508, -0.0), (1.0, 1.0, 1.0), "Suburbs_Wall_Thick_3x3m_A91", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3850.0, 450.0, 1400.0), (0.0, 90.0000030488508, -0.0), (1.0, 1.0, 1.0), "Suburbs_Wall_Thick_3x3m_A92", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2550.0, 150.0, 1700.0), (0.0, 90.0000030488508, -0.0), (1.0, 1.0, 1.0), "Suburbs_Wall_Thick_3x3m_A95", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2550.0, 450.0, 1700.0), (0.0, 90.0000030488508, -0.0), (1.0, 1.0, 1.0), "Suburbs_Wall_Thick_3x3m_A96", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3850.0, 150.0, 1700.0), (0.0, 90.0000030488508, -0.0), (1.0, 1.0, 1.0), "Suburbs_Wall_Thick_3x3m_A97", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3850.0, 450.0, 1700.0), (0.0, 90.0000030488508, -0.0), (1.0, 1.0, 1.0), "Suburbs_Wall_Thick_3x3m_A98", _folder)
if a: placed += 1
else: skipped += 1

# Batch 36: StaticMesh'Suburbs_Wall_Thin_05x05m_A' (3 instances)
_mesh_path = "/Game/Art/Assets/Kits/Architecture/Suburbs/Suburbs_Wall_Thin_05x05m_A"
_materials = ['/Game/Art/Assets/Kits/Architecture/Suburbs/Destructable/Materials/MI_Suburbs_Wall_Non_Dest']
_folder = "Reconstruction/BD_BB_OrcPrison/Meshes"
a = spawn_static_mesh(_mesh_path, _materials, (2349.9922, 5159.994, 600.0), (0.0, 0.0, -0.0), (1.0, 1.0, 1.0), "BP_Archway_3m_DoorFalse_A124", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3149.9922, 5159.994, 650.0), (0.0, 0.0, -0.0), (1.0, 1.0, 1.0), "BP_Archway_3m_DoorFalse_A56", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2349.9922, 5159.994, 650.0), (0.0, 0.0, -0.0), (1.0, 1.0, 1.0), "BP_Archway_3m_DoorFalse_A60", _folder)
if a: placed += 1
else: skipped += 1

# Batch 37: StaticMesh'Suburbs_Wall_Thin_3x1m_A' (19 instances)
_mesh_path = "/Game/Art/Assets/Kits/Architecture/Suburbs/Suburbs_Wall_Thin_3x1m_A"
_materials = ['/Game/Art/Assets/Kits/Architecture/Suburbs/Destructable/Materials/MI_Suburbs_Wall_Non_Dest']
_folder = "Reconstruction/BD_BB_OrcPrison/Meshes"
a = spawn_static_mesh(_mesh_path, _materials, (2900.0, 1605.0, 710.0), (0.0, -89.99999818714215, 0.0), (1.0, 1.0, 1.0), "BP_Archway_3m_DoorFalse_A100", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2835.0, 1545.0, 710.0), (0.0, -179.99998633961752, -0.0), (1.0, 1.0, 1.0), "BP_Archway_3m_DoorFalse_A101", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2835.0, 1545.0, 1010.0), (0.0, -179.99998633961752, -0.0), (1.0, 1.0, 1.0), "BP_Archway_3m_DoorFalse_A102", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3544.9937, 1895.0078, 1010.0), (0.0, 89.99999818714215, -0.0), (1.0, 1.0, 1.0), "BP_Archway_3m_DoorFalse_A105", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3544.9937, 1895.0078, 710.0), (0.0, 89.99999818714215, -0.0), (1.0, 1.0, 1.0), "BP_Archway_3m_DoorFalse_A106", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2900.0, 795.0, 1010.0), (0.0, -89.99999818714215, 0.0), (1.0, 1.0, 1.0), "BP_Archway_3m_DoorFalse_A109", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2900.0, 795.0, 710.0), (0.0, -89.99999818714215, 0.0), (1.0, 1.0, 1.0), "BP_Archway_3m_DoorFalse_A110", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3550.0015, 1085.0054, 1010.0), (0.0, 89.99999818714215, -0.0), (1.0, 1.0, 1.0), "BP_Archway_3m_DoorFalse_A113", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3550.0015, 1085.0054, 710.0), (0.0, 89.99999818714215, -0.0), (1.0, 1.0, 1.0), "BP_Archway_3m_DoorFalse_A114", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2835.0, 1145.0, 710.0), (0.0, -179.99998633961752, -0.0), (1.0, 1.0, 1.0), "BP_Archway_3m_DoorFalse_A120", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2835.0, 1145.0, 1010.0), (0.0, -179.99998633961752, -0.0), (1.0, 1.0, 1.0), "BP_Archway_3m_DoorFalse_A121", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1349.9988, 5120.003, 700.0), (0.0, 0.0, -0.0), (1.0, 1.0, 1.0), "BP_Archway_3m_DoorFalse_A168", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1449.9988, 5120.003, 700.0), (0.0, 0.0, -0.0), (1.0, 1.0, 1.0), "BP_Archway_3m_DoorFalse_A169", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1849.9988, 5120.003, 700.0), (0.0, 0.0, -0.0), (1.0, 1.0, 1.0), "BP_Archway_3m_DoorFalse_A171", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3149.9922, 5159.994, 700.0), (0.0, 0.0, -0.0), (1.0, 1.0, 1.0), "BP_Archway_3m_DoorFalse_A54", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3149.9922, 5159.994, 1000.0), (0.0, -179.99998633961752, -0.0), (1.0, 1.0, 1.0), "BP_Archway_3m_DoorFalse_A55", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2359.9922, 5159.994, 700.0), (0.0, 0.0, -0.0), (1.0, 1.0, 1.0), "BP_Archway_3m_DoorFalse_A58", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2359.9922, 5159.994, 1000.0), (0.0, -179.99998633961752, -0.0), (1.0, 1.0, 1.0), "BP_Archway_3m_DoorFalse_A59", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2900.0, 1605.0, 1010.0), (0.0, -89.99999818714215, 0.0), (1.0, 1.0, 1.0), "BP_Archway_3m_DoorFalse_A99", _folder)
if a: placed += 1
else: skipped += 1

# Batch 38: StaticMesh'Suburbs_Wall_Thin_3x3m_A' (80 instances)
_mesh_path = "/Game/Art/Assets/Kits/Architecture/Suburbs/Suburbs_Wall_Thin_3x3m_A"
_materials = ['/Game/Art/Assets/Kits/Architecture/Suburbs/Destructable/Materials/MI_Suburbs_Wall_Non_Dest']
_folder = "Reconstruction/BD_BB_OrcPrison/Meshes"
a = spawn_static_mesh(_mesh_path, _materials, (2750.0, 3570.0, 700.0), (0.0, 0.0, -0.0), (1.0, 1.0, 1.0), "BP_Archway_3m_DoorFalse_A_2", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3544.9937, 1695.0078, 1010.0), (0.0, 89.99999818714215, -0.0), (1.0, 1.0, 1.0), "BP_Archway_3m_DoorFalse_A103", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3544.9937, 1695.0078, 710.0), (0.0, 89.99999818714215, -0.0), (1.0, 1.0, 1.0), "BP_Archway_3m_DoorFalse_A104", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2900.0, 995.0, 1010.0), (0.0, -89.99999818714215, 0.0), (1.0, 1.0, 1.0), "BP_Archway_3m_DoorFalse_A107", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2900.0, 995.0, 710.0), (0.0, -89.99999818714215, 0.0), (1.0, 1.0, 1.0), "BP_Archway_3m_DoorFalse_A108", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2149.9922, 5179.994, 700.0), (0.0, -179.99998633961752, -0.0), (1.0, 1.0, 1.0), "BP_Archway_3m_DoorFalse_A11_172", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3550.0012, 885.00543, 1010.0), (0.0, 89.99999818714215, -0.0), (1.0, 1.0, 1.0), "BP_Archway_3m_DoorFalse_A111", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3550.0012, 885.00543, 710.0), (0.0, 89.99999818714215, -0.0), (1.0, 1.0, 1.0), "BP_Archway_3m_DoorFalse_A112", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3665.0012, 670.00543, 710.0), (0.0, -179.99998633961752, -0.0), (1.0, 1.0, 1.0), "BP_Archway_3m_DoorFalse_A122", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3665.0012, 670.00543, 1010.0), (0.0, -179.99998633961752, -0.0), (1.0, 1.0, 1.0), "BP_Archway_3m_DoorFalse_A123", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2765.0012, 670.00543, 710.0), (0.0, -179.99998633961752, -0.0), (1.0, 1.0, 1.0), "BP_Archway_3m_DoorFalse_A125", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2765.0012, 670.00543, 1010.0), (0.0, -179.99998633961752, -0.0), (1.0, 1.0, 1.0), "BP_Archway_3m_DoorFalse_A126", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3695.0022, 1979.9966, 700.0), (0.0, 0.0, -0.0), (1.0, 1.0, 1.0), "BP_Archway_3m_DoorFalse_A127", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3995.0022, 1979.9963, 700.0), (0.0, 0.0, -0.0), (1.0, 1.0, 1.0), "BP_Archway_3m_DoorFalse_A128", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3994.9978, 2950.0034, 1000.0), (0.0, -179.99998633961752, -0.0), (1.0, 1.0, 1.0), "BP_Archway_3m_DoorFalse_A131", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3694.9978, 2950.004, 1000.0), (0.0, -179.99998633961752, -0.0), (1.0, 1.0, 1.0), "BP_Archway_3m_DoorFalse_A132", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3994.9978, 2950.0034, 700.0), (0.0, -179.99998633961752, -0.0), (1.0, 1.0, 1.0), "BP_Archway_3m_DoorFalse_A133", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3694.9978, 2950.004, 700.0), (0.0, -179.99998633961752, -0.0), (1.0, 1.0, 1.0), "BP_Archway_3m_DoorFalse_A134", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1995.0037, 3315.0022, 1000.0), (0.0, 89.99999818714215, -0.0), (1.0, 1.0, 1.0), "BP_Archway_3m_DoorFalse_A137_887", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1995.0037, 3315.0022, 700.0), (0.0, 89.99999818714215, -0.0), (1.0, 1.0, 1.0), "BP_Archway_3m_DoorFalse_A138", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1429.9978, 3525.0027, 1000.0), (0.0, -179.99998633961752, -0.0), (1.0, 1.0, 1.0), "BP_Archway_3m_DoorFalse_A140", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1429.9978, 3525.0027, 700.0), (0.0, -179.99998633961752, -0.0), (1.0, 1.0, 1.0), "BP_Archway_3m_DoorFalse_A141", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1759.9978, 3525.0027, 1000.0), (0.0, -179.99998633961752, -0.0), (1.0, 1.0, 1.0), "BP_Archway_3m_DoorFalse_A143", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1934.9993, 4075.0, 1000.0), (0.0, 89.99999818714215, -0.0), (1.0, 1.0, 1.0), "BP_Archway_3m_DoorFalse_A153_1206", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1935.0, 3775.0002, 999.99963), (0.0, 89.99999818714215, -0.0), (1.0, 1.0, 1.0), "BP_Archway_3m_DoorFalse_A158", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1565.0005, 4075.0, 700.0), (0.0, 89.99999818714215, -0.0), (1.0, 1.0, 1.0), "BP_Archway_3m_DoorFalse_A159", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1565.0005, 4375.0, 700.0), (0.0, 89.99999818714215, -0.0), (1.0, 1.0, 1.0), "BP_Archway_3m_DoorFalse_A160", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1430.0037, 4510.002, 700.0), (0.0, -179.99998633961752, -0.0), (1.0, 1.0, 1.0), "BP_Archway_3m_DoorFalse_A161", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1130.0037, 4510.002, 700.0), (0.0, -179.99998633961752, -0.0), (1.0, 1.0, 1.0), "BP_Archway_3m_DoorFalse_A162", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (830.00366, 4510.002, 700.0), (0.0, -179.99998633961752, -0.0), (1.0, 1.0, 1.0), "BP_Archway_3m_DoorFalse_A163", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (645.00085, 4675.0, 700.0), (0.0, 89.99999818714215, -0.0), (1.0, 1.0, 1.0), "BP_Archway_3m_DoorFalse_A164", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (645.00073, 4975.0, 700.0), (0.0, 89.99999818714215, -0.0), (1.0, 1.0, 1.0), "BP_Archway_3m_DoorFalse_A165", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (849.9989, 5120.003, 700.0), (0.0, 0.0, -0.0), (1.0, 1.0, 1.0), "BP_Archway_3m_DoorFalse_A166", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1149.9988, 5120.003, 700.0), (0.0, 0.0, -0.0), (1.0, 1.0, 1.0), "BP_Archway_3m_DoorFalse_A167", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1377.9972, 5287.999, 700.0), (0.0, 89.99999818714215, -0.0), (1.0, 1.0, 1.0), "BP_Archway_3m_DoorFalse_A172", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1377.9968, 5587.999, 700.0), (0.0, 89.99999818714215, -0.0), (1.0, 1.0, 1.0), "BP_Archway_3m_DoorFalse_A173", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1922.0024, 5578.001, 700.0), (0.0, -89.99999818714215, 0.0), (1.0, 1.0, 1.0), "BP_Archway_3m_DoorFalse_A174", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1922.0027, 5278.001, 700.0), (0.0, -89.99999818714215, 0.0), (1.0, 1.0, 1.0), "BP_Archway_3m_DoorFalse_A175", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1499.9989, 5720.0024, 700.0), (0.0, 0.0, -0.0), (1.0, 1.0, 1.0), "BP_Archway_3m_DoorFalse_A176", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1799.9989, 5720.003, 700.0), (0.0, 0.0, -0.0), (1.0, 1.0, 1.0), "BP_Archway_3m_DoorFalse_A177", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2150.0, 3600.0, 1000.0), (0.0, 0.0, -0.0), (1.0, 1.0, 1.0), "BP_Archway_3m_DoorFalse_A18_7", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2450.0, 3600.0, 1000.0), (0.0, 0.0, -0.0), (1.0, 1.0, 1.0), "BP_Archway_3m_DoorFalse_A19_8", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2450.0, 3570.0, 700.0), (0.0, 0.0, -0.0), (1.0, 1.0, 1.0), "BP_Archway_3m_DoorFalse_A2", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2750.0, 3600.0, 1000.0), (0.0, 0.0, -0.0), (1.0, 1.0, 1.0), "BP_Archway_3m_DoorFalse_A20_9", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1564.9998, 3775.0, 700.0), (0.0, 89.99999818714215, -0.0), (1.0, 1.0, 1.0), "BP_Archway_3m_DoorFalse_A23_1241", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1975.0, 4075.0, 1000.0), (0.0, -89.99999818714215, 0.0), (1.0, 1.0, 1.0), "BP_Archway_3m_DoorFalse_A27", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1975.0, 3775.0, 1000.0), (0.0, -89.99999818714215, 0.0), (1.0, 1.0, 1.0), "BP_Archway_3m_DoorFalse_A28", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1974.9999, 4375.0, 999.99963), (0.0, -89.99999818714215, 0.0), (1.0, 1.0, 1.0), "BP_Archway_3m_DoorFalse_A29", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2150.0, 3570.0, 700.0), (0.0, 0.0, -0.0), (1.0, 1.0, 1.0), "BP_Archway_3m_DoorFalse_A3", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1974.9999, 4675.0, 999.99963), (0.0, -89.99999818714215, 0.0), (1.0, 1.0, 1.0), "BP_Archway_3m_DoorFalse_A30", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1974.9999, 4975.0, 999.99963), (0.0, -89.99999818714215, 0.0), (1.0, 1.0, 1.0), "BP_Archway_3m_DoorFalse_A31", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2865.0002, 3455.0, 700.0), (0.0, -89.99999818714215, 0.0), (1.0, 1.0, 1.0), "BP_Archway_3m_DoorFalse_A4_345", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2149.9922, 5149.994, 1000.0), (0.0, -179.99998633961752, -0.0), (1.0, 1.0, 1.0), "BP_Archway_3m_DoorFalse_A43", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3520.0002, 4970.0, 999.99963), (0.0, 89.99999818714215, -0.0), (1.0, 1.0, 1.0), "BP_Archway_3m_DoorFalse_A44", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3520.0, 4670.0, 999.99963), (0.0, 89.99999818714215, -0.0), (1.0, 1.0, 1.0), "BP_Archway_3m_DoorFalse_A45", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2865.0, 3155.0, 700.0), (0.0, -89.99999818714215, 0.0), (1.0, 1.0, 1.0), "BP_Archway_3m_DoorFalse_A5_346", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3349.9922, 5179.994, 700.0), (0.0, -179.99998633961752, -0.0), (1.0, 1.0, 1.0), "BP_Archway_3m_DoorFalse_A50", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3349.9922, 5149.994, 1000.0), (0.0, -179.99998633961752, -0.0), (1.0, 1.0, 1.0), "BP_Archway_3m_DoorFalse_A53", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3550.0002, 4970.0, 699.99963), (0.0, 89.99999818714215, -0.0), (1.0, 1.0, 1.0), "BP_Archway_3m_DoorFalse_A62", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3545.0, 4675.0, 699.99963), (0.0, 89.99999818714215, -0.0), (1.0, 1.0, 1.0), "BP_Archway_3m_DoorFalse_A63", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2895.0, 3455.0, 1000.0), (0.0, -89.99999818714215, 0.0), (1.0, 1.0, 1.0), "BP_Archway_3m_DoorFalse_A67", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2895.0, 3155.0, 1000.0), (0.0, -89.99999818714215, 0.0), (1.0, 1.0, 1.0), "BP_Archway_3m_DoorFalse_A68", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3520.0002, 3455.0, 999.99963), (0.0, 89.99999818714215, -0.0), (1.0, 1.0, 1.0), "BP_Archway_3m_DoorFalse_A70", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3520.0, 3155.0, 999.99963), (0.0, 89.99999818714215, -0.0), (1.0, 1.0, 1.0), "BP_Archway_3m_DoorFalse_A71", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3550.0002, 3455.0, 699.99963), (0.0, 89.99999818714215, -0.0), (1.0, 1.0, 1.0), "BP_Archway_3m_DoorFalse_A76", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3545.0, 3160.0, 699.99963), (0.0, 89.99999818714215, -0.0), (1.0, 1.0, 1.0), "BP_Archway_3m_DoorFalse_A77", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3520.0002, 3755.0, 999.99963), (0.0, 89.99999818714215, -0.0), (1.0, 1.0, 1.0), "BP_Archway_3m_DoorFalse_A78", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3550.0002, 3755.0, 699.99963), (0.0, 89.99999818714215, -0.0), (1.0, 1.0, 1.0), "BP_Archway_3m_DoorFalse_A81", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2744.9978, 2950.0037, 1000.0), (0.0, -179.99998633961752, -0.0), (1.0, 1.0, 1.0), "BP_Archway_3m_DoorFalse_A84", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2744.9978, 2950.0037, 700.0), (0.0, -179.99998633961752, -0.0), (1.0, 1.0, 1.0), "BP_Archway_3m_DoorFalse_A85_556", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2444.9978, 2950.0037, 1000.0), (0.0, -179.99998633961752, -0.0), (1.0, 1.0, 1.0), "BP_Archway_3m_DoorFalse_A86", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2444.9978, 2950.0037, 700.0), (0.0, -179.99998633961752, -0.0), (1.0, 1.0, 1.0), "BP_Archway_3m_DoorFalse_A87", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2445.0022, 1979.9966, 1000.0), (0.0, 0.0, -0.0), (1.0, 1.0, 1.0), "BP_Archway_3m_DoorFalse_A89", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2745.0022, 1979.9963, 1000.0), (0.0, 0.0, -0.0), (1.0, 1.0, 1.0), "BP_Archway_3m_DoorFalse_A90", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2445.0022, 1979.9966, 700.0), (0.0, 0.0, -0.0), (1.0, 1.0, 1.0), "BP_Archway_3m_DoorFalse_A91", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2745.0022, 1979.9963, 700.0), (0.0, 0.0, -0.0), (1.0, 1.0, 1.0), "BP_Archway_3m_DoorFalse_A92", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3695.0022, 1979.9966, 1000.0), (0.0, 0.0, -0.0), (1.0, 1.0, 1.0), "BP_Archway_3m_DoorFalse_A95", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3995.0022, 1979.9963, 1000.0), (0.0, 0.0, -0.0), (1.0, 1.0, 1.0), "BP_Archway_3m_DoorFalse_A96", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2900.0, 1805.0, 1010.0), (0.0, -89.99999818714215, 0.0), (1.0, 1.0, 1.0), "BP_Archway_3m_DoorFalse_A97", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2900.0, 1805.0, 710.0), (0.0, -89.99999818714215, 0.0), (1.0, 1.0, 1.0), "BP_Archway_3m_DoorFalse_A98", _folder)
if a: placed += 1
else: skipped += 1

# Batch 39: StaticMesh'Suburbs_Wall_Thin_Arch_B' (19 instances)
_mesh_path = "/Game/Art/Assets/Kits/Architecture/Suburbs/Suburbs_Wall_Thin_Arch_B"
_materials = ['/Game/Art/Assets/Kits/Architecture/Suburbs/Destructable/Materials/MI_Suburbs_Wall_Non_Dest']
_folder = "Reconstruction/BD_BB_OrcPrison/Meshes"
a = spawn_static_mesh(_mesh_path, _materials, (2150.0, 3590.0, 700.0), (0.0, 0.0, -0.0), (1.0, 1.0, 1.0), "BP_Archway_3m_DoorFalse_A12", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2450.0, 3590.0, 700.0), (0.0, 0.0, -0.0), (1.0, 1.0, 1.0), "BP_Archway_3m_DoorFalse_A13", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2750.0, 3590.0, 700.0), (0.0, 0.0, -0.0), (1.0, 1.0, 1.0), "BP_Archway_3m_DoorFalse_A14", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1759.9978, 3575.0027, 700.0), (0.0, -179.99998633961752, -0.0), (1.0, 1.0, 1.0), "BP_Archway_3m_DoorFalse_A144", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1650.0, 5120.0, 700.0), (0.0, -179.99998633961752, -0.0), (1.0, 1.0, 1.0), "BP_Archway_3m_DoorFalse_A170", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1759.9978, 3525.0027, 700.0), (0.0, -179.99998633961752, -0.0), (1.0, 1.0, 1.0), "BP_Archway_3m_DoorFalse_A178_271", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1965.0, 3775.0, 700.0), (0.0, -89.99999818714215, 0.0), (1.0, 1.0, 1.0), "BP_Archway_3m_DoorFalse_A24", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1965.0, 4975.0, 700.0), (0.0, -89.99999818714215, 0.0), (1.0, 1.0, 1.0), "BP_Archway_3m_DoorFalse_A34", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1965.0, 4675.0, 700.0), (0.0, -89.99999818714215, 0.0), (1.0, 1.0, 1.0), "BP_Archway_3m_DoorFalse_A35", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1965.0, 4375.0, 700.0), (0.0, -89.99999818714215, 0.0), (1.0, 1.0, 1.0), "BP_Archway_3m_DoorFalse_A38", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2149.9924, 5159.994, 700.0), (0.0, -179.99998633961752, -0.0), (1.0, 1.0, 1.0), "BP_Archway_3m_DoorFalse_A41", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3529.9998, 4669.9995, 700.0), (0.0, 89.99999818714215, -0.0), (1.0, 1.0, 1.0), "BP_Archway_3m_DoorFalse_A46", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3530.0, 4970.0, 700.0), (0.0, 89.99999818714215, -0.0), (1.0, 1.0, 1.0), "BP_Archway_3m_DoorFalse_A47", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3349.9924, 5159.994, 700.0), (0.0, -179.99998633961752, -0.0), (1.0, 1.0, 1.0), "BP_Archway_3m_DoorFalse_A51", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2885.0, 3155.0, 700.0), (0.0, -89.99999818714215, 0.0), (1.0, 1.0, 1.0), "BP_Archway_3m_DoorFalse_A64", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2885.0, 3450.0, 700.0), (0.0, -89.99999818714215, 0.0), (1.0, 1.0, 1.0), "BP_Archway_3m_DoorFalse_A69", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3529.9998, 3154.9995, 700.0), (0.0, 89.99999818714215, -0.0), (1.0, 1.0, 1.0), "BP_Archway_3m_DoorFalse_A72", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3530.0, 3470.0, 700.0), (0.0, 89.99999818714215, -0.0), (1.0, 1.0, 1.0), "BP_Archway_3m_DoorFalse_A73", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3530.0, 3755.0, 700.0), (0.0, 89.99999818714215, -0.0), (1.0, 1.0, 1.0), "BP_Archway_3m_DoorFalse_A79", _folder)
if a: placed += 1
else: skipped += 1

# Batch 40: StaticMesh'Suburbs_Wall_Thin_Arch_B_1m' (2 instances)
_mesh_path = "/Game/Art/Assets/Kits/Architecture/Suburbs/Suburbs_Wall_Thin_Arch_B_1m"
_materials = ['/Game/Art/Assets/Kits/Architecture/Suburbs/Destructable/Materials/MI_Suburbs_Wall_Non_Dest']
_folder = "Reconstruction/BD_BB_OrcPrison/Meshes"
a = spawn_static_mesh(_mesh_path, _materials, (1965.0, 4525.0, 600.0), (0.0, -89.99999818714215, 0.0), (1.0, 1.0, 1.0), "BP_Archway_3m_DoorFalse_A39", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1965.0, 4225.0, 600.0), (0.0, 89.99999818714215, -0.0), (1.0, 1.0, 1.0), "BP_Archway_3m_DoorFalse_A40", _folder)
if a: placed += 1
else: skipped += 1

# Batch 41: StaticMesh'Suburbs_Wall_Thin_Window_Small_A' (4 instances)
_mesh_path = "/Game/Art/Assets/Kits/Architecture/Suburbs/Suburbs_Wall_Thin_Window_Small_A"
_materials = ['/Game/Art/Assets/Kits/Architecture/Suburbs/Destructable/Materials/MI_Suburbs_Wall_Non_Dest', '/Game/Art/Assets/Kits/Architecture/Suburbs/Materials/MI_Suburbs_Single_Window_A/MI_Suburbs_Single_Window_A']
_folder = "Reconstruction/BD_BB_OrcPrison/Meshes"
a = spawn_static_mesh(_mesh_path, _materials, (1945.0002, 4075.0, 700.0), (0.0, -89.99999818714215, 0.0), (1.0, 1.0, 1.0), "BP_Archway_3m_DoorFalse_A21", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1945.0, 3775.0, 700.0), (0.0, -89.99999818714215, 0.0), (1.0, 1.0, 1.0), "BP_Archway_3m_DoorFalse_A22", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1945.0002, 4975.0, 700.0), (0.0, -89.99999818714215, 0.0), (1.0, 1.0, 1.0), "BP_Archway_3m_DoorFalse_A32", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1945.0, 4675.0, 700.0), (0.0, -89.99999818714215, 0.0), (1.0, 1.0, 1.0), "BP_Archway_3m_DoorFalse_A33", _folder)
if a: placed += 1
else: skipped += 1

# Batch 42: StaticMesh'OrcBanner_A' (1 instances)
_mesh_path = "/Game/Art/Assets/Kits/Deco/Orc/OrcBanner_A"
_materials = ['/Game/Art/Assets/Kits/Deco/Orc/Materials/Orc_Banners/MI_OrcBanners']
_folder = "Reconstruction/BD_BB_OrcPrison/Meshes"
a = spawn_static_mesh(_mesh_path, _materials, (3151.9202, 5098.1777, 1158.4789), (0.0, 0.0, -0.0), (1.3449361, 1.3449361, 1.3449361), "OrcBanner_A_12", _folder)
if a: placed += 1
else: skipped += 1

# Batch 43: StaticMesh'OrcBanner_B' (1 instances)
_mesh_path = "/Game/Art/Assets/Kits/Deco/Orc/OrcBanner_B"
_materials = ['/Game/Art/Assets/Kits/Deco/Orc/Materials/Orc_Banners/MI_OrcBanners']
_folder = "Reconstruction/BD_BB_OrcPrison/Meshes"
a = spawn_static_mesh(_mesh_path, _materials, (2349.1226, 5095.985, 1157.888), (0.0, 0.0, -0.0), (1.509636, 1.509636, 1.509636), "OrcBanner_B2_9", _folder)
if a: placed += 1
else: skipped += 1

# Batch 44: StaticMesh'OrcBanner_C' (2 instances)
_mesh_path = "/Game/Art/Assets/Kits/Deco/Orc/OrcBanner_C"
_materials = ['/Game/Art/Assets/Kits/Deco/Orc/Materials/Orc_Banners/MI_OrcBanners']
_folder = "Reconstruction/BD_BB_OrcPrison/Meshes"
a = spawn_static_mesh(_mesh_path, _materials, (1160.0, 3615.0, 1295.0), (0.0, 90.00011648875932, -0.0), (1.6875, 1.6875, 1.6875), "OrcBanner_C2", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1160.0, 2745.0, 1295.0), (0.0, 90.00011648875932, -0.0), (1.6875, 1.6875, 1.6875), "OrcBanner_C3_1156", _folder)
if a: placed += 1
else: skipped += 1

# Batch 45: StaticMesh'OrcBanner_F' (2 instances)
_mesh_path = "/Game/Art/Assets/Kits/Deco/Orc/OrcBanner_F"
_materials = ['/Game/Art/Assets/Kits/Deco/Orc/Materials/Orc_Banners/MI_OrcBanners']
_folder = "Reconstruction/BD_BB_OrcPrison/Meshes"
a = spawn_static_mesh(_mesh_path, _materials, (1159.0, 3186.0, 1828.0), (0.0, 90.0000030488508, -0.0), (1.78125, 1.28125, 1.28125), "OrcBanner_F_1117", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3250.001, 623.00134, 1827.9939), (1.3660373749679381e-05, -179.9999863396177, 0.00010438044994449063), (1.78125, 1.28125, 1.28125), "OrcBanner_F2", _folder)
if a: placed += 1
else: skipped += 1

# Batch 46: StaticMesh'Dirt_Mound_D' (7 instances)
_mesh_path = "/Game/Art/Assets/Kits/Misc/Dirt_Mounds/Dirt_Mound_D"
_materials = ['/Game/Art/Assets/Kits/Misc/Dirt_Mounds/Materials/MI_Mines_Dirt']
_folder = "Reconstruction/BD_BB_OrcPrison/Meshes"
a = spawn_static_mesh(_mesh_path, _materials, (3544.4326, 4850.933, 585.4082), (0.0, 179.90024507988093, -0.0), (1.0, 0.87189955, 1.3429468), "Dirt_Mound_D_12", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2415.1182, 3572.4546, 580.77655), (0.0, -99.4389982197792, 0.0), (1.125, 1.125, 0.875), "Dirt_Mound_D3_275", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1965.5929, 3841.9045, 576.9666), (0.0, 179.01864013349677, -0.0), (1.0, 1.0, 0.784163), "Dirt_Mound_D4", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1952.2778, 5000.908, 576.9666), (0.0, 175.30232103904004, -0.0), (1.0, 1.0, 0.784163), "Dirt_Mound_D5", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3232.194, 1901.0985, 717.1017), (-19.9250164758956, 85.28679406804864, 1.609320538553551), (0.90625, 0.75, 0.47241816), "Dirt_Mound_D6_280", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3212.194, 1817.601, 760.47205), (-25.201992945312014, 85.1022414636863, 2.089746632128225), (0.32807246, 0.646368, 0.472418), "Dirt_Mound_D7", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3809.4944, 2949.1357, 706.33435), (0.0, -92.61840986341248, 0.0), (0.6282255, 0.6282255, 0.6282255), "Dirt_Mound_D9_228", _folder)
if a: placed += 1
else: skipped += 1

# Batch 47: StaticMesh'Dirt_Mound_G' (20 instances)
_mesh_path = "/Game/Art/Assets/Kits/Misc/Dirt_Mounds/Dirt_Mound_G"
_materials = ['/Game/Art/Assets/Kits/Misc/Dirt_Mounds/Materials/MI_Mines_Dirt']
_folder = "Reconstruction/BD_BB_OrcPrison/Meshes"
a = spawn_static_mesh(_mesh_path, _materials, (3217.6104, 3085.129, 603.3358), (0.0, -87.46801478333852, 0.0), (1.9657998, 1.0, 1.8696883), "Dirt_Mound_G_67", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1904.7524, 4842.7134, 698.8077), (0.0, 1.5457066569522773, -0.0), (0.5052626, 1.2257124, 0.6764262), "Dirt_Mound_G10_200", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1345.6332, 5479.8945, 706.33435), (0.0, 0.0, -0.0), (1.0, 1.0, 1.0), "Dirt_Mound_G11_212", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1915.9855, 5479.8945, 706.33435), (0.0, 0.0, -0.0), (1.0, 1.0, 1.0), "Dirt_Mound_G12", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1666.3546, 5696.2754, 706.33435), (0.0, 75.62013757571877, -0.0), (1.1825356, 1.2593825, 1.0), "Dirt_Mound_G13", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1887.2372, 5366.983, 703.1755), (0.0, -5.852234198232419, 0.0), (1.0, 1.0, 1.0), "Dirt_Mound_G14", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3489.2366, 3509.9873, 603.3358), (0.0, 0.0, -0.0), (1.0, 1.0, 1.0), "Dirt_Mound_G15", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2876.9238, 3425.7273, 603.3358), (0.0, 0.0, -0.0), (1.0, 1.0, 1.0), "Dirt_Mound_G16", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1319.8605, 3519.8848, 706.3344), (0.0, -67.96442017998608, 0.0), (1.4120595, 1.0, 1.3540355), "Dirt_Mound_G2_80", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4388.314, 3576.9478, 624.0922), (-2.6756286415561124, 23.676363766061478, 6.562149029593388), (1.0297357, 1.0297357, 1.0297357), "Dirt_Mound_G3_108", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4028.1792, 4747.6816, 606.71967), (-2.3920287373230997, 4.002565252291997e-08, -3.0954896382728525), (1.213929, 1.213929, 1.5241841), "Dirt_Mound_G4_114", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4380.9673, 5108.2925, 606.3803), (-2.3919368761258495, 87.73832777489969, -3.0954892033394636), (1.7337971, 1.2127845, 1.7129338), "Dirt_Mound_G6", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4559.551, 4936.7437, 599.7512), (-28.844025423575115, -174.36235543658938, 0.3578609415175668), (1.521013, 1.0, 1.50015), "Dirt_Mound_G7", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (789.9084, 2589.6401, 806.2154), (0.0, 100.1803831456744, -0.0), (1.0, 1.2103337, 1.0), "Dirt_Mound_G8_192", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (836.5325, 3787.738, 806.2154), (0.0, 76.10809001447677, -0.0), (1.0, 1.0, 1.0), "Dirt_Mound_G9", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3873.759, 423.46518, 806.8904), (0.0, -177.11883257186523, 0.0), (1.267498, 1.267498, 1.267498), "Dirt_Mound_H20", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2612.4253, 362.8123, 806.8904), (0.0, 179.09157500429612, -0.0), (1.267498, 1.267498, 1.267498), "Dirt_Mound_H22", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (976.0814, 5081.4673, 706.8857), (0.0, 86.66699155649623, -0.0), (1.0467546, 1.0467546, 1.0467546), "Dirt_Mound_I43", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (669.9155, 4833.6113, 706.8857), (0.0, -179.6378969697395, 0.0), (1.046755, 1.046755, 1.046755), "Dirt_Mound_I44", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1057.9736, 4505.6885, 706.8857), (0.0, -82.10649922722806, 0.0), (1.1944479, 1.1944479, 1.1944479), "Dirt_Mound_I45", _folder)
if a: placed += 1
else: skipped += 1

# Batch 48: StaticMesh'Dirt_Mound_H' (18 instances)
_mesh_path = "/Game/Art/Assets/Kits/Misc/Dirt_Mounds/Dirt_Mound_H"
_materials = ['/Game/Art/Assets/Kits/Misc/Dirt_Mounds/Materials/MI_Mines_Dirt']
_folder = "Reconstruction/BD_BB_OrcPrison/Meshes"
a = spawn_static_mesh(_mesh_path, _materials, (3589.6362, 1947.3511, 695.50916), (0.0, -36.26953221528128, 0.0), (1.1831276, 1.1831276, 1.1831276), "Dirt_Mound_D8", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2883.088, 1210.611, 795.41296), (0.0, -136.77324905559064, 0.0), (1.062008, 1.0, 1.381358), "Dirt_Mound_H10", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2846.8489, 1040.9923, 795.41296), (0.0, -87.24316831705582, 0.0), (1.062008, 1.0, 1.381358), "Dirt_Mound_H11", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2810.0916, 942.6017, 795.41296), (0.0, -87.24316831705582, 0.0), (1.062008, 1.0, 1.381358), "Dirt_Mound_H12", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1041.0636, 2537.7668, 806.33435), (0.0, -4.9914246859326, 0.0), (1.0, 1.0, 1.0), "Dirt_Mound_H13_189", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1506.5609, 3839.1318, 694.64813), (0.0, -92.22320305324853, 0.0), (2.1540346, 1.0, 1.0), "Dirt_Mound_H14_196", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1520.8966, 4294.5107, 694.64813), (0.0, -92.22320305324853, 0.0), (3.7427015, 1.0, 1.0), "Dirt_Mound_H15", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1896.5446, 3839.1318, 694.64813), (-1.7572935242190342, -91.54641940837008, 0.04745822669058983), (2.0055215, 0.40500426, 0.69846624), "Dirt_Mound_H16", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2850.0913, 1807.0062, 735.41296), (9.378578469393679, -105.54771550700725, -5.415038798251642), (1.062008, 1.0, 2.8702288), "Dirt_Mound_H17_230", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3520.0913, 1793.6958, 755.41296), (10.698369695818045, -121.62594137763627, -6.792021558329398), (1.062008, 1.0, 1.756321), "Dirt_Mound_H18", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3657.5693, 740.2337, 806.8904), (0.0, 151.13920430472987, -0.0), (1.2674975, 1.2674975, 1.2674975), "Dirt_Mound_H19", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3560.2961, 3863.9473, 596.57764), (0.0, 74.63614677873989, -0.0), (1.3580437, 1.3184344, 1.3360754), "Dirt_Mound_H2", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3791.753, 666.2802, 815.69055), (0.0, 139.6549085335516, -0.0), (1.267498, 1.267498, 1.267498), "Dirt_Mound_H21", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3601.9312, 4431.1953, 596.57776), (0.0, 77.94981790976723, -0.0), (1.358044, 1.059563, 1.336075), "Dirt_Mound_H3", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3485.8647, 3186.095, 608.7253), (0.0, -124.711586974518, 0.0), (1.0, 1.0, 1.2282408), "Dirt_Mound_H5_59", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3554.2078, 1032.0298, 801.7472), (0.0, 54.94129920427387, -0.0), (1.0, 1.0, 1.0), "Dirt_Mound_H7_86", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3558.4458, 1473.1749, 801.27924), (0.0, 54.94129920427387, -0.0), (1.0620078, 1.0, 1.3813584), "Dirt_Mound_H8", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2850.0913, 1617.0062, 795.41296), (0.0, -116.66974941159664, 0.0), (1.062008, 1.0, 1.381358), "Dirt_Mound_H9", _folder)
if a: placed += 1
else: skipped += 1

# Batch 49: StaticMesh'Dirt_Mound_I' (47 instances)
_mesh_path = "/Game/Art/Assets/Kits/Misc/Dirt_Mounds/Dirt_Mound_I"
_materials = ['/Game/Art/Assets/Kits/Misc/Dirt_Mounds/Materials/MI_Mines_Dirt']
_folder = "Reconstruction/BD_BB_OrcPrison/Meshes"
a = spawn_static_mesh(_mesh_path, _materials, (2600.0, 5179.4844, 600.0), (0.0, -59.99996903561683, 0.0), (1.0, 1.0, 1.0), "Dirt_Mound_I_8", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2891.7256, 3069.2158, 601.41296), (0.0, 8.556185949463353, -0.0), (0.62926996, 0.62926996, 0.9616913), "Dirt_Mound_I10_63", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2879.0588, 3230.5593, 596.45544), (0.0, 20.866435844271578, -0.0), (0.62927, 0.62927, 0.961691), "Dirt_Mound_I11", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1109.657, 3773.3406, 802.541), (0.0, 50.3551338996725, -0.0), (0.4706289, 0.4706289, 0.4706289), "Dirt_Mound_I12_83", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4837.088, 2065.2793, 684.6301), (0.0, -98.20705469650991, 0.0), (1.0, 1.0, 1.109807), "Dirt_Mound_I13", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4577.327, 2017.7604, 684.6301), (0.0, -98.20705469650991, 0.0), (1.0, 1.0, 1.109807), "Dirt_Mound_I14", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5204.9766, 2645.856, 684.6301), (0.0, -133.36508235029413, 0.0), (1.0, 1.0, 1.109807), "Dirt_Mound_I15", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5133.9277, 3132.0203, 670.15533), (1.7305882155475283, -156.6883465257057, -4.506163688933354), (1.0, 1.0, 1.3781679), "Dirt_Mound_I16", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5060.242, 3534.461, 670.1553), (-4.282043876270004, -125.67853309406208, -12.836455608859758), (1.0, 1.0, 1.378168), "Dirt_Mound_I17", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4368.6157, 3132.0203, 670.15533), (4.879785880568673, -120.85403216672366, -2.1148685650296364), (1.0, 1.0, 0.8791089), "Dirt_Mound_I18", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4261.456, 2856.8093, 677.6101), (2.0029524081130266, -27.737852392000352, -2.640289102623773), (1.0, 1.0, 1.0663958), "Dirt_Mound_I19", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2910.3003, 5200.0, 571.8202), (0.0, 110.00014960145684, -0.0), (1.0, 1.0, 1.2396036), "Dirt_Mound_I2", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4602.918, 5019.755, 570.3252), (1.78465961528816, -100.52738024013861, -4.254150207895575), (1.0, 1.0, 1.0080756), "Dirt_Mound_I20_110", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4006.1177, 5058.318, 570.3252), (-3.7246391970845667, -178.84974232863718, -4.364653605259419), (1.0, 1.0, 1.008076), "Dirt_Mound_I21", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3925.584, 4580.7627, 570.3252), (1.78465961528816, -100.52738024013861, -4.254150207895575), (0.7440354, 0.6238988, 0.8721399), "Dirt_Mound_I22", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1378.4529, 5224.0513, 705.1362), (0.0, 49.82568408290801, -0.0), (0.52206266, 0.3961023, 0.43684968), "Dirt_Mound_I23_205", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1225.036, 5085.1177, 705.1362), (0.0, -20.7579951638385, 0.0), (0.425058, 0.425058, 0.19027203), "Dirt_Mound_I24", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (749.7479, 5107.3213, 705.1362), (0.0, 141.27105979289038, -0.0), (0.49216837, 0.49216837, 0.2577538), "Dirt_Mound_I25", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (716.2229, 4521.537, 705.1362), (0.0, -122.16857351820232, 0.0), (0.425058, 0.425058, 0.339845), "Dirt_Mound_I26", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3325.2046, 5179.4844, 600.0), (0.0, -62.638514763407315, 0.0), (0.78130126, 0.78130126, 0.78130126), "Dirt_Mound_I27_160", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3534.9983, 3069.2158, 601.41296), (0.0, 8.556185949463353, -0.0), (0.62927, 0.62927, 0.961691), "Dirt_Mound_I28_164", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2213.2979, 3070.9705, 700.0), (4.4802350718556125, 16.892962438562964, -1.6592100083972174), (1.0, 1.0982805, 1.0), "Dirt_Mound_I29_218", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2138.114, 5179.4844, 600.0), (0.0, -35.40408558518305, 0.0), (0.7008564, 0.7008564, 0.7008564), "Dirt_Mound_I3", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1843.5143, 2344.8125, 662.9927), (4.480234840369062, 77.34975273708655, -1.6591795887404281), (1.0, 1.64803, 1.1607678), "Dirt_Mound_I30", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3436.4233, 5196.1387, 571.8202), (0.0, 68.8863213161704, -0.0), (1.0, 1.0, 1.239604), "Dirt_Mound_I32", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2922.032, 660.66016, 806.33435), (0.0, -66.23519666471368, 0.0), (0.3602122, 0.3602122, 0.3990293), "Dirt_Mound_I36", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1978.1284, 3224.8635, 706.33435), (0.0, 0.0, -0.0), (0.48309535, 0.48309535, 0.37599063), "Dirt_Mound_I37_234", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1947.9165, 3334.5525, 706.33435), (0.0, 0.0, -0.0), (0.483095, 0.483095, 0.375991), "Dirt_Mound_I38", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1283.15, 3270.9983, 698.8246), (0.0, 6.69496161393252, -0.0), (0.483095, 1.1432085, 0.5075207), "Dirt_Mound_I39", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2709.2964, 1946.3811, 695.9105), (0.0, 99.56880023381564, -0.0), (1.0, 1.0, 0.5545662), "Dirt_Mound_I4_31", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1283.15, 2931.197, 698.8246), (0.0, 6.694961959460868, -0.0), (0.483095, 1.143209, 0.507521), "Dirt_Mound_I40", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1566.453, 3504.2417, 702.44604), (0.0, 104.50302597538398, -0.0), (0.483095, 0.483095, 0.375991), "Dirt_Mound_I41", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3747.2844, 4512.314, 570.3252), (1.7846599795589655, -48.590266633320475, -4.254150363321416), (0.744035, 0.623899, 0.87214), "Dirt_Mound_I42", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3710.0256, 4565.861, 595.98975), (1.061854536669831, -23.82113889421412, -0.46881105602272355), (0.8695592, 0.8695592, 0.9797301), "Dirt_Mound_I46", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3723.2607, 3791.0596, 595.98975), (1.0618554521448746, 105.2445978953576, -0.46881108626908563), (0.869559, 0.869559, 0.97973), "Dirt_Mound_I47", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4108.6475, 3751.0078, 589.7912), (1.0618555712416986, 99.9486801292707, -0.4688111335689704), (0.9609264, 0.869559, 0.97973), "Dirt_Mound_I48", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4946.4766, 4030.493, 575.0408), (-0.9987489087116457, 15.007203249496488, 0.8194769604901385), (1.0, 1.0, 1.378168), "Dirt_Mound_I49", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2427.2422, 2943.4182, 695.9105), (0.0, 0.0, -0.0), (1.0, 1.0, 1.109807), "Dirt_Mound_I5", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4831.548, 4654.277, 575.04065), (-0.9987488686741509, 37.29431701923019, 0.8194818114362419), (1.0, 1.0, 1.378168), "Dirt_Mound_I50", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4884.754, 4346.1553, 576.09595), (4.985272949171429, -139.50209091434263, 0.02121846175328857), (0.6898993, 0.6898993, 1.0680671), "Dirt_Mound_I51", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2411.3933, 2027.982, 702.39014), (0.0, -94.09728908105784, 0.0), (1.0, 1.0, 0.659214), "Dirt_Mound_I54", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2712.7925, 2944.1694, 695.9105), (0.0, -75.77622153445074, 0.0), (0.608687, 0.608687, 0.718494), "Dirt_Mound_I55", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2688.026, 712.225, 806.33435), (0.0, 127.18329380412673, -0.0), (0.6875, 0.6875, 0.6875), "Dirt_Mound_I56", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2819.7917, 2948.4216, 695.9105), (0.0, 81.85073955969783, -0.0), (0.6086871, 0.6086871, 0.7184942), "Dirt_Mound_I6_283", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4137.7896, 1875.515, 695.9105), (0.0, -8.24865794553877, 0.0), (1.0, 1.0, 1.109807), "Dirt_Mound_I7", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5105.832, 2254.9695, 684.6301), (0.0, 161.70138591502865, -0.0), (1.0, 1.0, 1.109807), "Dirt_Mound_I8", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4058.5308, 3026.1316, 695.9105), (0.0, 0.0, -0.0), (1.0, 1.0, 1.109807), "Dirt_Mound_I9", _folder)
if a: placed += 1
else: skipped += 1

# Batch 50: StaticMesh'Suburbs_Dirt_Mound_A' (5 instances)
_mesh_path = "/Game/Art/Assets/Kits/Misc/Dirt_Mounds/Suburbs_Dirt_Mound_A"
_materials = ['/Game/Art/Assets/Kits/Misc/Dirt_Mounds/Materials/MI_Mines_Dirt']
_folder = "Reconstruction/BD_BB_OrcPrison/Meshes"
a = spawn_static_mesh(_mesh_path, _materials, (3501.2163, 2924.2803, 706.3345), (0.0, 106.29579326114391, -0.0), (1.5100223, 1.5100223, 1.8424433), "Dirt_Mound_I31", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3483.0151, 3778.956, 600.13525), (0.0, -91.05333510392654, 0.0), (2.5142055, 2.5142055, 2.3047369), "Suburbs_Dirt_Mound_A3", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1341.2339, 2868.7405, 707.5846), (-2.188385103939512, -44.52407845069582, -2.223297139795771), (3.0277183, 2.6891563, 2.6355014), "Suburbs_Dirt_Mound_A5", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1176.2339, 3568.7405, 807.5846), (0.0, 92.65729608292267, -0.0), (1.865309, 1.526747, 1.930046), "Suburbs_Dirt_Mound_A6", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1545.7194, 2699.5952, 707.5846), (-2.188385039582308, 85.02091631127927, -2.2232970162645906), (4.0542583, 3.7156963, 3.6620412), "Suburbs_Dirt_Mound_A7", _folder)
if a: placed += 1
else: skipped += 1

# Batch 51: StaticMesh'Suburbs_Dirt_Mound_B' (2 instances)
_mesh_path = "/Game/Art/Assets/Kits/Misc/Dirt_Mounds/Suburbs_Dirt_Mound_B"
_materials = ['/Game/Art/Assets/Kits/Misc/Dirt_Mounds/Materials/MI_Mines_Dirt']
_folder = "Reconstruction/BD_BB_OrcPrison/Meshes"
a = spawn_static_mesh(_mesh_path, _materials, (4163.9214, 2430.939, 682.7403), (-1.8065490142388894, 93.70463033121287, 1.0720985753220291), (3.3111887, 3.3111887, 2.9389422), "Dirt_Mound_I52", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4133.168, 2606.442, 695.735), (-0.9000244101084287, 65.12951876190975, 3.029714331806047), (3.311189, 3.311189, 1.8504837), "Dirt_Mound_I53", _folder)
if a: placed += 1
else: skipped += 1

# Batch 52: StaticMesh'SM_BannerPole_B' (6 instances)
_mesh_path = "/Game/Environments/Models/NaturalDeco/Meshes/SM_BannerPole_B"
_materials = ['/Game/Environments/Models/NaturalDeco/Materials/MI_ArchSimple_BannerPole_Metal']
_folder = "Reconstruction/BD_BB_OrcPrison/Meshes"
a = spawn_static_mesh(_mesh_path, _materials, (2350.0, 5117.0, 1156.0), (0.0, -89.99999818714215, 0.0), (1.0, 1.0, 1.0), "SM_BannerPole_B_483", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3150.0, 5117.0, 1156.0), (0.0, -89.99999818714215, 0.0), (1.0, 1.0, 1.0), "SM_BannerPole_B2", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1196.0, 3190.0, 1824.0), (4.959105216232155e-05, -179.99998633961795, -179.99994535847787), (1.875, 1.875, 1.875), "SM_BannerPole_B3_1152", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1191.0, 3620.0, 1289.0), (4.999998699671576e-05, -179.99998633961775, -179.99994535847785), (1.53125, 1.53125, 1.53125), "SM_BannerPole_B4", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1191.0, 2750.0, 1289.0), (4.999998699671576e-05, -179.99998633961775, -179.99994535847785), (1.53125, 1.53125, 1.53125), "SM_BannerPole_B5", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3246.001, 660.0011, 1823.9939), (-4.098113982875377e-05, -89.99993822617961, -179.99989318845857), (1.875, 1.875, 1.875), "SM_BannerPole_B6", _folder)
if a: placed += 1
else: skipped += 1

# Batch 53: StaticMesh'PWM_Quarry_1x1x1_A' (46 instances)
_mesh_path = "/Game/Unshippable/Whitebox/Rocks/Meshes/PWM_Quarry_1x1x1_A"
_materials = ['/Game/Environments/ProcTexturing/ProcMaterial_Quarry_Atlas_1']
_folder = "Reconstruction/BD_BB_OrcPrison/Meshes"
a = spawn_static_mesh(_mesh_path, _materials, (5160.8325, 3067.1636, 548.0405), (1.3660376870247608e-05, 11.25105758677886, 4.71832789598946e-13), (1.5625, 3.1875, 1.5), "BP_DM_Quarry_1X1x1_A_Breakable10_11", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4305.174, 2014.8203, 538.0405), (1.3660377269006482e-05, -81.5619488194637, 1.6984371169405634e-13), (1.5625, 3.1875, 1.5), "BP_DM_Quarry_1X1x1_A_Breakable10_88", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5053.502, 3606.5894, 1448.0421), (-9.909820565778462, 9.10823063795404, 4.90252935327214), (1.125, 3.125, 1.0), "BP_DM_Quarry_1X1x1_A_Breakable11_12", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4849.217, 2095.5488, 1438.0421), (-9.909820846808046, -83.70476359397273, 4.902527474347429), (1.125, 3.125, 1.0), "BP_DM_Quarry_1X1x1_A_Breakable11_89", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4828.363, 3969.641, 448.03992), (-0.0004882811214281621, -168.7489198808365, 179.99995901884753), (1.0, 2.375, 1.375), "BP_DM_Quarry_1X1x1_A_Breakable12_13", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5222.88, 2302.5994, 438.03992), (-0.00048828105262771254, 98.4380734799037, 179.99995901885694), (1.0, 2.375, 1.375), "BP_DM_Quarry_1X1x1_A_Breakable12_90", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5017.5195, 4008.6616, 898.03503), (3.8287448493158793, 111.16939099321196, -8.246062570140175), (2.4375, 2.125, 1.8125), "BP_DM_Quarry_1X1x1_A_Breakable6_7", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5252.227, 2104.7644, 888.03503), (3.8287447997969988, 13.557960416980544, -8.244660211047005), (2.4375, 2.125, 1.8125), "BP_DM_Quarry_1X1x1_A_Breakable6_84", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4985.236, 3949.8674, 548.0403), (4.098112684712327e-05, -3.7492198115223254, 1.0906270523272688e-13), (1.75, 3.3125, 2.375), "BP_DM_Quarry_1X1x1_A_Breakable7_8", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5195.4316, 2146.8862, 538.0403), (4.0981135320581956e-05, -96.56216427763067, 7.325297728607399e-12), (1.75, 3.3125, 2.375), "BP_DM_Quarry_1X1x1_A_Breakable7_85", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5014.502, 3802.7502, 748.0421), (3.40488230311607, 105.97078927711898, -9.40804852793682), (2.25, 1.4375, 2.25), "BP_DM_Quarry_1X1x1_A_Breakable8_9", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5047.055, 2124.8752, 738.0421), (3.4048828580188446, 13.157876232003288, -9.408049361404265), (2.25, 1.4375, 2.25), "BP_DM_Quarry_1X1x1_A_Breakable8_86", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5092.545, 3410.4375, 798.0405), (1.3660376870247608e-05, 11.25105758677886, 4.71832789598946e-13), (1.1875, 2.25, 2.1875), "BP_DM_Quarry_1X1x1_A_Breakable9_10", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4651.3853, 2066.1792, 788.0405), (1.3660377269006482e-05, -81.5619488194637, 1.6984371169405634e-13), (1.1875, 2.25, 2.1875), "BP_DM_Quarry_1X1x1_A_Breakable9_87", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3865.0342, 3720.6472, 1107.0242), (-6.736327714382647, -79.97609990832821, -179.99995914072295), (0.678113, 1.0, 1.0), "PWM_Quarry_1x1x1_A_20", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4466.666, 3115.577, 1127.0242), (-6.73632812104632, -155.9134478882826, -179.9999795260615), (0.678113, 1.0, 1.0), "PWM_Quarry_1x1x1_A_29", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4431.2734, 3561.3342, 1067.0242), (-6.736326971116163, 26.898989936773432, -179.9999589382062), (0.678113, 1.0, 1.0), "PWM_Quarry_1x1x1_A_38", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4342.1533, 2864.2344, 1127.0242), (-6.736326859322614, 108.46115294735004, -179.99997893459675), (0.678113, 1.0, 1.0), "PWM_Quarry_1x1x1_A_47", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5270.252, 2424.7786, 1144.6487), (-6.42574977830408, -160.87379679740786, 177.97404639134558), (1.7148361, 2.0367231, 2.0367231), "PWM_Quarry_1x1x1_A_64", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4903.258, 4517.367, 1067.0242), (-6.7363276304462945, 49.3989841026362, -179.99995935886142), (0.678113, 1.0, 1.0), "PWM_Quarry_1x1x1_A_100", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3667.9424, 4296.9307, 1266.0548), (68.44458777643884, 78.73837966132972, -99.46985754670797), (0.678113, 1.0, 1.0), "PWM_Quarry_1x1x1_A_119", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4045.9844, 4016.9326, 1193.946), (-68.4441790038923, 101.26143040587958, 80.5306750786818), (0.678113, 1.0, 1.0), "PWM_Quarry_1x1x1_A_133", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4606.6743, 5021.7373, 1065.8691), (1.573495811426813, 26.83300828331322, -178.53597241322072), (0.678113, 1.0, 1.0), "PWM_Quarry_1x1x1_A_143", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4301.986, 5068.401, 1048.6484), (-17.893970610019974, -82.47258809167151, 178.52541586383023), (0.678113, 1.0, 1.0), "PWM_Quarry_1x1x1_A_152", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4139.717, 4895.6973, 1058.2787), (-15.105403981395886, 7.419090464444211, 178.90681495988022), (0.678113, 1.0, 1.0), "PWM_Quarry_1x1x1_A_161", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4624.745, 5027.222, 1004.0641), (-76.16627584035547, 150.5792421037071, 46.64253672374382), (0.678113, 1.0, 1.0), "PWM_Quarry_1x1x1_A_170", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1953.142, 2194.2832, 1217.0242), (-6.736326628536667, -105.28854566693612, -179.99995908390872), (0.678113, 1.0, 1.0), "PWM_Quarry_1x1x1_A_179", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1641.7687, 2593.1855, 1167.0242), (-6.7363282644433955, 57.83641106828022, -179.99997939450486), (0.678113, 1.0, 1.0), "PWM_Quarry_1x1x1_A_188", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2191.556, 2995.6338, 1127.0242), (-6.73632656961332, 43.77397719803434, -179.99995889445864), (0.678113, 1.0, 1.0), "PWM_Quarry_1x1x1_A_197", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1659.7795, 2308.4136, 1279.3171), (79.12078752682008, -153.5173529498683, -64.75698025538044), (0.678113, 1.0, 1.0), "PWM_Quarry_1x1x1_A_215", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1958.063, 2712.2173, 1426.9302), (77.50032643803385, -80.07198760699265, -172.45177362454203), (0.678113, 1.0, 1.0), "PWM_Quarry_1x1x1_A_224", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4887.447, 3544.5212, 629.645), (-28.997432970115494, 83.63011164397425, -173.01657607619774), (0.611965, 0.611965, 0.856418), "PWM_Quarry_1x1x1_A10", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4514.691, 3365.0698, 628.2353), (-39.93924026718409, 13.669677158343132, -150.3068087395594), (0.70185167, 0.70185167, 0.9463056), "PWM_Quarry_1x1x1_A11", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4581.5503, 3267.1953, 660.7544), (28.84058219834641, 177.83629931884911, 53.57708819996784), (0.701852, 0.701852, 0.946306), "PWM_Quarry_1x1x1_A12", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4986.5483, 3150.9998, 691.44604), (0.0, 10.278859626776743, -0.0), (0.66702944, 0.66702944, 0.66702944), "PWM_Quarry_1x1x1_A13_171", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4958.4043, 3028.02, 680.7599), (20.31577315361868, -179.9999863396129, -179.9999863396129), (0.473498, 0.473498, 0.473498), "PWM_Quarry_1x1x1_A14", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4594.4727, 3081.1611, 684.5535), (-36.667132070239596, 106.85227854960698, -179.9999622647568), (0.667029, 0.667029, 0.667029), "PWM_Quarry_1x1x1_A15", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5234.0083, 2595.0232, 1221.4813), (-16.056239195786596, -160.52075268245378, 177.9047154011872), (1.858827, 2.1807137, 2.1807137), "PWM_Quarry_1x1x1_A16", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2151.5435, 2044.4255, 1320.4937), (-73.78759397300485, 38.25169339317735, 144.0601836285202), (0.678113, 1.0, 1.0), "PWM_Quarry_1x1x1_A2", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5069.624, 2345.7605, 697.1723), (35.01254701012627, 141.1348067912252, -13.117006464189409), (0.9080368, 0.9080368, 0.9080368), "PWM_Quarry_1x1x1_A3_148", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5140.4434, 2662.6245, 705.2649), (35.01257882376151, 158.75212825683573, -13.119478202082185), (1.1897801, 1.1897801, 1.4342344), "PWM_Quarry_1x1x1_A4", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4501.9395, 3135.6702, 693.29913), (0.251808947908187, -114.93543535639493, -17.809233999191814), (1.18978, 1.18978, 1.434234), "PWM_Quarry_1x1x1_A5", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5081.941, 2926.9614, 671.77795), (18.916078262110258, -158.26058128176754, 29.12259309734155), (1.18978, 1.18978, 1.434234), "PWM_Quarry_1x1x1_A6", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5074.0513, 3046.302, 671.77795), (-7.953091998322123, 10.459990993528514, 167.13217184798427), (1.18978, 1.18978, 1.434234), "PWM_Quarry_1x1x1_A7", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4935.2085, 3649.349, 671.77795), (-13.703155586338617, 172.60560740271666, -49.977140460684694), (1.18978, 1.18978, 1.434234), "PWM_Quarry_1x1x1_A8", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4933.6743, 3466.5002, 671.77795), (-30.884119037251498, -166.95516336959065, -6.08233555846693), (0.6119646, 0.6119646, 0.8564185), "PWM_Quarry_1x1x1_A9", _folder)
if a: placed += 1
else: skipped += 1

# Batch 54: StaticMesh'PWM_Quarry_1X1x1_C' (26 instances)
_mesh_path = "/Game/Unshippable/Whitebox/Rocks/Meshes/PWM_Quarry_1X1x1_C"
_materials = ['/Game/Environments/ProcTexturing/ProcMaterial_Quarry_Atlas_1']
_folder = "Reconstruction/BD_BB_OrcPrison/Meshes"
a = spawn_static_mesh(_mesh_path, _materials, (5121.549, 3008.3687, 1048.035), (-3.0517577053065036e-05, 26.25117763360421, -3.0517574754310344e-05), (1.0, 2.4375, 1.625), "BP_DM_Quarry_1X1x1_C_Breakable6_1", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4248.3774, 2056.942, 1038.035), (-3.05175788005936e-05, -66.5617370540106, -3.051758158823126e-05), (1.0, 2.4375, 1.625), "BP_DM_Quarry_1X1x1_C_Breakable6_30", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5144.959, 2311.7827, 778.671), (0.0, 0.0, -0.0), (0.9019789, 0.9019789, 0.9019789), "PWM_Quarry_1X1x1_C_151", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5163.67, 2497.0977, 706.6871), (14.753683761958762, -85.96626102080565, 95.3301961134466), (0.775732, 0.775732, 0.775732), "PWM_Quarry_1X1x1_C10", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4540.847, 5104.2188, 613.5004), (16.986880206819663, -3.9855350943331525, -13.414094242169837), (1.0, 1.0, 1.0), "PWM_Quarry_1X1x1_C11_177", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4113.8755, 5104.2188, 609.47186), (16.986880206819663, -3.9855350943331525, -13.414094242169837), (1.0, 1.0, 1.0), "PWM_Quarry_1X1x1_C12", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4085.9082, 4873.3257, 617.0706), (0.02473902817376091, -13.9267890845194, -58.770202040548284), (0.56027937, 0.56027937, 0.56027937), "PWM_Quarry_1X1x1_C13", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4042.5105, 4501.337, 617.0706), (0.02473902817376091, -13.9267890845194, -58.770202040548284), (0.560279, 0.560279, 0.560279), "PWM_Quarry_1X1x1_C14", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3951.9902, 4501.337, 599.6458), (-12.960909226204167, 5.141081076211964, -170.72805682926725), (0.560279, 0.560279, 0.560279), "PWM_Quarry_1X1x1_C15", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4614.946, 4814.166, 614.62805), (0.02473891735241398, 11.511195961018949, -58.76946930186144), (0.8453867, 0.8453867, 0.8453867), "PWM_Quarry_1X1x1_C16", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4543.982, 4956.2617, 606.0593), (10.156775277006341, -74.6059657368366, -177.0480194367883), (0.560279, 0.560279, 0.560279), "PWM_Quarry_1X1x1_C17", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4382.898, 5173.9253, 601.1499), (16.986880206819663, -3.9855350943331525, -13.414094242169837), (1.0, 1.0, 1.0), "PWM_Quarry_1X1x1_C18", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4592.4253, 4743.0435, 589.5674), (0.02473935700171811, -23.999665124600895, -58.767675795826584), (0.845387, 0.845387, 0.845387), "PWM_Quarry_1X1x1_C19", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4972.0293, 2299.103, 695.916), (0.0, 46.50286667728915, -0.0), (0.77573174, 0.77573174, 0.77573174), "PWM_Quarry_1X1x1_C2", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4583.3936, 4874.298, 579.87164), (-4.06286673868593, 82.40090574543733, 150.5892623830561), (0.845387, 0.845387, 0.845387), "PWM_Quarry_1X1x1_C20", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5101.838, 3583.538, 1137.4082), (-53.139847846349305, -89.99955350997392, -168.93788388793985), (1.0, 1.0, 1.0), "PWM_Quarry_1X1x1_C3_59", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4311.5786, 4773.9375, 1100.8071), (-60.452945981307195, -15.16780505533916, -151.62761032828809), (1.0, 1.0, 1.0), "PWM_Quarry_1X1x1_C3_76", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4238.16, 2301.5986, 1336.1929), (-61.578494423545585, 90.00000436442637, -168.93794565466257), (1.0, 1.0, 1.0), "PWM_Quarry_1X1x1_C3_1043", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5052.371, 2236.2512, 742.8131), (0.0, 168.20943274880426, -0.0), (0.6956352, 0.6956352, 0.6956352), "PWM_Quarry_1X1x1_C4", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5163.67, 2413.7485, 688.0961), (14.753683761958762, -85.96626102080565, 95.3301961134466), (0.775732, 0.775732, 0.775732), "PWM_Quarry_1X1x1_C5", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4289.5127, 2163.0347, 1336.1929), (33.93592709962253, -89.9998603916106, 11.072173990984792), (1.432982, 1.432982, 1.432982), "PWM_Quarry_1X1x1_C6", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5050.4834, 3720.601, 1117.0742), (25.49725837682498, 90.00054394978261, 11.072188252976348), (1.432982, 1.432982, 1.432982), "PWM_Quarry_1X1x1_C6_72", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4173.0166, 4723.1343, 1108.343), (33.519686837483576, 174.3635168905157, 0.9352593800138257), (1.432982, 1.432982, 1.432982), "PWM_Quarry_1X1x1_C6_89", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4779.3647, 2253.8135, 695.916), (0.0, 93.11699711528506, -0.0), (0.775732, 0.775732, 0.775732), "PWM_Quarry_1X1x1_C7", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4353.281, 2734.1677, 701.41187), (0.0, -98.21276455613723, 0.0), (0.838751, 0.838751, 0.838751), "PWM_Quarry_1X1x1_C8_167", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4474.8784, 2726.7346, 681.41187), (0.0, -144.02518964982806, 0.0), (0.64288527, 0.64288527, 0.64288527), "PWM_Quarry_1X1x1_C9", _folder)
if a: placed += 1
else: skipped += 1

# Batch 55: StaticMesh'PWM_Quarry_2x2x2_A' (73 instances)
_mesh_path = "/Game/Unshippable/Whitebox/Rocks/Meshes/PWM_Quarry_2x2x2_A"
_materials = ['/Game/Environments/ProcTexturing/ProcMaterial_Quarry_Atlas_1']
_folder = "Reconstruction/BD_BB_OrcPrison/Meshes"
a = spawn_static_mesh(_mesh_path, _materials, (4354.63, 2022.1787, 1238.0408), (-3.051757804608793e-05, -76.56189582184051, -3.0517573721424307e-05), (1.0, 1.5625, 1.0), "BP_DM_Quarry_2x2x2_A_Breakable10_7", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5151.0557, 3116.199, 1248.0408), (-3.0517575622297748e-05, 16.251093591043784, -3.0517574014872306e-05), (1.0, 1.5625, 1.0), "BP_DM_Quarry_2x2x2_A_Breakable10_12", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4488.3345, 2143.0857, 788.04065), (2.7320755443160517e-05, 18.438151063462296, 3.1161688816474054e-12), (0.625, 0.375, 0.625), "BP_DM_Quarry_2x2x2_A_Breakable11_8", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5023.733, 3243.8088, 798.04065), (2.7320754661278004e-05, 111.25107889446414, -1.1869286513331321e-12), (0.625, 0.375, 0.625), "BP_DM_Quarry_2x2x2_A_Breakable11_13", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4374.208, 2114.15, 788.04065), (2.732075628643572e-05, -171.77788977871552, 6.430582847982561e-11), (0.625, 0.375, 0.625), "BP_DM_Quarry_2x2x2_A_Breakable12", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4942.0083, 3864.5522, 1138.961), (-36.34969931250212, -178.44822140889218, -0.920165325349327), (0.75, 1.4375, 1.267919), "BP_DM_Quarry_2x2x2_A_Breakable13", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5145.9697, 2139.5708, 1388.0405), (4.098113298466144e-05, -91.56201164266102, 3.002362219989897e-12), (0.4375, 2.0625, 1.375), "BP_DM_Quarry_2x2x2_A_Breakable5_1", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4994.9697, 3900.8242, 1398.0405), (4.09811250218959e-05, 1.250931188976392, 9.649731236504834e-13), (0.4375, 2.0625, 1.375), "BP_DM_Quarry_2x2x2_A_Breakable5_7", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4807.1006, 2038.7318, 588.04877), (4.098114083878744e-05, -176.56189160958434, 4.999994156761406e-06), (2.125, 1.625, 1.6875), "BP_DM_Quarry_2x2x2_A_Breakable6_3", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5112.3174, 3567.3125, 598.04877), (4.0981134966617045e-05, -83.74892435219239, 5.000002924516098e-06), (2.125, 1.625, 1.6875), "BP_DM_Quarry_2x2x2_A_Breakable6_8", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4948.1377, 2057.9202, 938.0419), (4.72407228907525, -81.53257965418877, 0.7024227185148778), (1.0, 1.625, 0.9375), "BP_DM_Quarry_2x2x2_A_Breakable7_4", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5052.1514, 3704.672, 948.0419), (9.446442612777947, 11.408916093691547, 1.896864175781769), (1.0, 1.625, 0.9375), "BP_DM_Quarry_2x2x2_A_Breakable7_9", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5294.349, 2161.5603, 1038.0406), (-3.869271204947444e-13, 88.43795824780352, 3.999999051121651e-06), (0.75, 1.4375, 0.8125), "BP_DM_Quarry_2x2x2_A_Breakable8_5", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4962.614, 4047.9458, 1061.5007), (-18.43362191315177, -178.68217180424762, -0.4167785336187521), (0.75, 1.4375, 1.2679187), "BP_DM_Quarry_2x2x2_A_Breakable8_10", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4651.3853, 2066.1792, 688.042), (3.4150944306814076e-05, -1.562249111981596, 1.9999898663299784e-06), (1.6875, 1.0, 0.625), "BP_DM_Quarry_2x2x2_A_Breakable9_6", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5092.545, 3410.4375, 698.042), (3.4150942687630454e-05, 91.25071147242566, 1.9999972099861635e-06), (1.6875, 1.0, 0.625), "BP_DM_Quarry_2x2x2_A_Breakable9_11", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4985.2144, 3949.8635, 1198.0405), (1.3660377204213963e-05, 11.25105443035277, 3.659418872794243e-13), (0.375, 1.625, 0.625), "BP_Quarry_2x2x2_A_Breakable_3", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5195.4287, 2146.9077, 1188.0405), (1.3660377269006482e-05, -81.5619488194637, 1.6984371169405634e-13), (0.375, 1.625, 0.625), "BP_Quarry_2x2x2_A_Breakable_174", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5053.783, 3861.5552, 1098.0352), (2.732075085219475e-05, -88.74915237720147, -3.0517573889151742e-05), (2.125, 1.0, 1.3125), "BP_Quarry_2x2x2_A_Breakable2_4", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5103.862, 2082.755, 1088.0352), (2.7320756456793055e-05, 178.43790108264525, -3.051757726050262e-05), (2.125, 1.0, 1.3125), "BP_Quarry_2x2x2_A_Breakable2_175", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5151.077, 3116.203, 798.04095), (2.7320752489824157e-05, -88.74890547814243, 2.837364236420686e-12), (1.4375, 0.875, 1.25), "BP_Quarry_2x2x2_A_Breakable3_5", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4354.6323, 2022.1572, 788.04095), (2.7320754575564687e-05, 178.43814706932113, 5.838475225776548e-14), (1.4375, 0.875, 1.25), "BP_Quarry_2x2x2_A_Breakable3_176", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4761.9253, 2255.421, 1331.3405), (-6.741118468091099, 1.1976579880370348, -116.21028686456681), (1.130044, 0.457788, 1.689597), "PWM_Quarry_2x2x2_A10", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5176.7344, 2255.421, 1231.3958), (-13.655147675602812, 0.9448547207143534, -114.0210373815842), (1.130044, 0.457788, 1.689597), "PWM_Quarry_2x2x2_A11", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4583.023, 3009.7732, 1184.4645), (-52.588663873517106, 15.11038858641792, 165.31550505749158), (0.43318, 1.0, 1.081333), "PWM_Quarry_2x2x2_A12", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4583.023, 3184.622, 1184.4645), (-52.58860500504258, 15.110401212696143, 165.3154768066046), (0.43318, 1.0, 1.081333), "PWM_Quarry_2x2x2_A13", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4490.3145, 3450.6445, 1184.4645), (-52.58860500504258, 15.110401212696143, 165.3154768066046), (0.43318, 1.0, 1.081333), "PWM_Quarry_2x2x2_A14", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4125.1167, 2054.266, 925.3191), (3.3946441230914703, 13.787808841181285, 0.04207486814333415), (0.76966614, 0.457788, 2.0103574), "PWM_Quarry_2x2x2_A15_222", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4125.1167, 2054.266, 1183.0793), (4.7614339092563975, 17.721900266056288, 8.817553048486802), (0.769666, 0.457788, 1.3352786), "PWM_Quarry_2x2x2_A16", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2090.8518, 3071.9736, 1272.0194), (-1.0881041941444112, 9.746035705805445, -178.63477669749315), (0.7168212, 1.0, 1.081333), "PWM_Quarry_2x2x2_A17", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2164.7969, 2915.96, 1272.0194), (-1.0879821673711094, 12.9695482479207, -178.63477669285098), (0.716821, 1.0, 1.081333), "PWM_Quarry_2x2x2_A18", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2200.1135, 2937.608, 1038.5302), (-1.0879821673711094, 12.9695482479207, -178.63477669285098), (0.716821, 1.0, 1.2622696), "PWM_Quarry_2x2x2_A19", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3779.6116, 3780.7808, 746.97375), (0.0, 1.242664654168697, -0.0), (1.2602704, 0.457788, 1.3399545), "PWM_Quarry_2x2x2_A2_15", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4484.5337, 3232.134, 766.97375), (-0.0, -74.69458618747153, -0.0), (1.0, 0.457788, 1.0), "PWM_Quarry_2x2x2_A2_24", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4404.237, 3443.3088, 706.97375), (0.0, 108.11784125998147, 0.0), (1.0, 0.457788, 1.0), "PWM_Quarry_2x2x2_A2_33", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4407.6567, 2820.1719, 799.6232), (-0.0, -170.31991141570705, -0.0), (1.1300437, 0.457788, 1.0), "PWM_Quarry_2x2x2_A2_42", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5279.6606, 2553.112, 776.97375), (-0.0, -97.19485231659449, -0.0), (1.0, 0.457788, 1.0), "PWM_Quarry_2x2x2_A2_51", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4923.4463, 4397.9795, 706.97375), (0.0, 130.61778811345346, 0.0), (1.0, 0.457788, 1.0), "PWM_Quarry_2x2x2_A2_95", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4029.4478, 4182.127, 1245.292), (-12.477605672308622, 89.37773891691472, 92.88047619148915), (1.0, 0.457788, 1.0), "PWM_Quarry_2x2x2_A2_114", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3684.4795, 3902.1255, 1214.706), (12.47810163303579, 90.62274817627271, -87.11934319294494), (1.0, 0.457788, 1.0), "PWM_Quarry_2x2x2_A2_128", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4630.816, 4919.237, 700.89233), (-0.18230761530089426, 108.10450050873587, 8.435372509991494), (1.0, 0.457788, 1.0), "PWM_Quarry_2x2x2_A2_138", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4199.9683, 5202.608, 708.2396), (-0.3062260715654714, -1.5396247479754428, -11.245883231802251), (1.0, 0.457788, 1.0), "PWM_Quarry_2x2x2_A2_147", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4022.3745, 4793.6797, 711.6946), (-0.2302485124889608, 88.44723317684972, -8.43438056015594), (1.0, 0.457788, 1.0), "PWM_Quarry_2x2x2_A2_156", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4313.956, 4823.1084, 1081.5916), (1.2411475458558099, 106.81592047462047, -92.8163285239452), (1.0, 0.457788, 1.0), "PWM_Quarry_2x2x2_A2_165", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1679.2562, 2478.0525, 806.97375), (0.0, 139.0552710395207, 0.0), (1.0, 0.457788, 1.0), "PWM_Quarry_2x2x2_A2_183", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2199.9448, 2874.8423, 766.97375), (0.0, 124.99280723598112, 0.0), (1.0, 0.457788, 1.0), "PWM_Quarry_2x2x2_A2_192", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1772.3491, 2101.28, 1288.6725), (1.1699864946012248, 90.41848074165968, -70.29406970539114), (1.0, 0.457788, 1.0), "PWM_Quarry_2x2x2_A2_201", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1746.8489, 2677.9927, 1290.5935), (-1.2187108694281175, -177.43052236714982, 101.25447763057291), (1.0, 0.457788, 1.0), "PWM_Quarry_2x2x2_A2_210", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1877.6146, 2357.6218, 1316.9907), (7.109074054856833, 1.6876051763104039, 84.30000328291653), (1.0, 0.457788, 1.0), "PWM_Quarry_2x2x2_A2_219", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4454.934, 2092.8271, 955.9617), (0.5097028462246658, -170.33269509934448, -2.9896846831984862), (1.130044, 0.457788, 1.0), "PWM_Quarry_2x2x2_A3", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4289.9985, 2092.8276, 955.9617), (0.5097028462246658, -170.33269509934448, -2.9896846831984862), (1.130044, 0.457788, 1.0), "PWM_Quarry_2x2x2_A4", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5228.1074, 2333.7847, 1082.0194), (-0.3977355530397885, -13.388516431380681, 177.35792964073198), (0.43318, 1.0, 1.081333), "PWM_Quarry_2x2x2_A5", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3984.457, 3761.967, 1052.0194), (-0.39773558109271656, 85.0489965432625, 177.35793038580002), (0.43318, 1.0, 1.081333), "PWM_Quarry_2x2x2_A5_17", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4518.302, 3009.7732, 1072.0194), (-0.3977355576919225, 9.111741185252667, 177.35792980391432), (0.43318, 1.0, 1.081333), "PWM_Quarry_2x2x2_A5_26", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4357.066, 3663.6204, 1012.0194), (-0.3977354725939593, -168.075778619934, 177.35792947225983), (0.43318, 1.0, 1.081333), "PWM_Quarry_2x2x2_A5_35", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4230.0854, 2805.8384, 1072.0194), (-0.39773558376487944, -86.51359845729499, 177.3579297258311), (0.43318, 1.0, 1.081333), "PWM_Quarry_2x2x2_A5_44", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4795.5557, 4583.469, 1012.0194), (-0.3977355193657663, -145.57582901801564, 177.3579299176926), (0.43318, 1.0, 1.081333), "PWM_Quarry_2x2x2_A5_97", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3726.0115, 4405.998, 1205.0066), (-82.9316230754086, -63.08345744328341, 60.30907879085526), (0.43318, 1.0, 1.081333), "PWM_Quarry_2x2x2_A5_116", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3987.914, 4125.999, 1254.9956), (82.93129018695795, -116.91500476104268, -119.68987723783393), (0.43318, 1.0, 1.081333), "PWM_Quarry_2x2x2_A5_130", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4540.6177, 5126.496, 1005.3969), (-8.803310283507768, -168.1347399477243, 178.09212933851762), (0.43318, 1.0, 1.081333), "PWM_Quarry_2x2x2_A5_140", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4423.293, 5113.862, 1001.60876), (10.747931322823288, 82.09721234667624, 175.82081177134242), (0.43318, 1.0, 1.081333), "PWM_Quarry_2x2x2_A5_149", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4096.618, 5017.004, 1009.0652), (7.961959357483573, 172.1607413390068, 176.21118670966248), (0.43318, 1.0, 1.081333), "PWM_Quarry_2x2x2_A5_158", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4539.445, 5126.141, 1047.8145), (84.49179959955711, 80.92279210944751, 61.26484596502406), (0.43318, 1.0, 1.081333), "PWM_Quarry_2x2x2_A5_167", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2129.0386, 2087.69, 1194.9581), (2.582944956928529, 49.288682826538135, -177.52676750964355), (0.76616603, 1.0, 1.081333), "PWM_Quarry_2x2x2_A5_176", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1525.5334, 2642.769, 1112.0194), (-0.3977356406623391, -137.13836084950378, 177.35793027299184), (0.43318, 1.0, 1.081333), "PWM_Quarry_2x2x2_A5_185", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2090.8518, 3071.9736, 1072.0194), (-0.39773548889534743, -151.2007862698949, 177.35792976947505), (0.43318, 1.0, 1.081333), "PWM_Quarry_2x2x2_A5_194", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2065.8801, 2325.7952, 1373.7981), (69.32286039662351, 165.85270466055337, 164.05467497474626), (0.43318, 1.0, 1.081333), "PWM_Quarry_2x2x2_A5_203", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1537.4594, 2364.4897, 1249.5247), (-77.35379401282283, 116.0282376894435, -25.387383924330774), (0.43318, 1.0, 1.081333), "PWM_Quarry_2x2x2_A5_212", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2084.3179, 2665.028, 1398.1633), (-75.68498394650337, 23.489735647730598, -114.4447051452772), (0.43318, 1.0, 1.081333), "PWM_Quarry_2x2x2_A5_221", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4480.088, 2124.2417, 1147.7384), (1.1307303896487029, -170.3833007113582, -6.645322504407909), (1.130044, 0.457788, 1.689597), "PWM_Quarry_2x2x2_A6", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4647.8154, 2124.2432, 1147.7384), (1.1307303896487029, -170.3833007113582, -6.645322504407909), (1.130044, 0.457788, 1.689597), "PWM_Quarry_2x2x2_A7", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4300.8647, 2132.3633, 1293.6187), (3.1493240775841307, -6.081256205015758, 11.174302335010248), (1.130044, 0.457788, 1.689597), "PWM_Quarry_2x2x2_A8", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4953.632, 2255.421, 1293.6187), (-6.741120940113581, 1.1976566795334695, -116.21029124313712), (1.130044, 0.457788, 1.689597), "PWM_Quarry_2x2x2_A9", _folder)
if a: placed += 1
else: skipped += 1

# Batch 56: StaticMesh'PWM_Quarry_2x2x5_A' (87 instances)
_mesh_path = "/Game/Unshippable/Whitebox/Rocks/Meshes/PWM_Quarry_2x2x5_A"
_materials = ['/Game/Environments/ProcTexturing/ProcMaterial_Quarry_Atlas_2']
_folder = "Reconstruction/BD_BB_OrcPrison/Meshes"
a = spawn_static_mesh(_mesh_path, _materials, (5024.519, 4008.662, 748.03503), (69.9995603411333, 11.25091477731273, -90.00064699247531), (1.25, 1.25, 1.25), "BP_DM_Quarry_2x2x5_A_Breakable8_1", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5252.2275, 2104.7644, 738.03503), (69.99954892837268, -81.56204880612005, -90.00067894618024), (1.25, 1.25, 1.25), "BP_DM_Quarry_2x2x5_A_Breakable8_13", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3942.8423, 3749.5, 861.2235), (-5.59689189585887, -103.44747708924037, 178.19195980273503), (1.1390285, 1.2865951, 1.2865951), "PWM_Quarry_2x2x5_A_19", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4462.7217, 3047.1116, 881.2235), (-5.596891929303235, -144.38705159078128, 178.1919599670616), (0.852433, 1.0, 1.0), "PWM_Quarry_2x2x5_A_28", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4381.0767, 3627.4165, 821.2235), (-5.59689183328375, 38.425362201687456, 178.19195952876626), (0.852433, 1.0, 1.0), "PWM_Quarry_2x2x5_A_37", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4269.4204, 2824.2773, 881.2235), (-5.596893091508924, 119.98762382782961, 178.19195983282336), (0.852433, 1.0, 1.0), "PWM_Quarry_2x2x5_A_46", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5221.8804, 2376.7783, 891.2235), (-5.596892465655542, -166.8872336119502, 178.19197385780473), (0.852433, 1.0, 1.0), "PWM_Quarry_2x2x5_A_57", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4831.5933, 4559.2095, 821.2235), (-5.596891339159365, 60.92537564824032, 178.19197330545427), (0.852433, 1.0, 1.0), "PWM_Quarry_2x2x5_A_99", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3915.5798, 4367.617, 1234.6895), (57.175199548208504, 84.03210531712512, -95.30329877234128), (0.852433, 1.0, 1.0), "PWM_Quarry_2x2x5_A_118", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3798.3464, 4087.6167, 1225.3113), (-57.174748540568984, 95.96800413364174, 84.69697415024741), (0.852433, 1.0, 1.0), "PWM_Quarry_2x2x5_A_132", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4591.2886, 5098.38, 818.4953), (2.2549718363643794, 38.335113888534046, -178.71617121524122), (0.852433, 1.0, 1.0), "PWM_Quarry_2x2x5_A_142", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4381.1167, 5140.8745, 812.44806), (-16.231768416465105, -70.55029145421848, 174.44950254399402), (0.852433, 1.0, 1.0), "PWM_Quarry_2x2x5_A_151", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4078.9207, 4974.8276, 818.80676), (-13.577722454362851, 19.20195402692671, 175.41251696914037), (0.852433, 1.0, 1.0), "PWM_Quarry_2x2x5_A_160", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4368.582, 5030.8164, 1044.7352), (-66.8899878014998, 128.22517225943005, 67.3743162732274), (0.852433, 1.0, 1.0), "PWM_Quarry_2x2x5_A_169", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2035.8159, 2187.0986, 971.2235), (-5.596892645435265, -93.76214450339454, 178.19196004018787), (0.852433, 1.0, 1.0), "PWM_Quarry_2x2x5_A_178", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1564.7406, 2624.0598, 921.2235), (-5.596893541764475, 69.36284937971918, 178.19195974826334), (0.852433, 1.0, 1.0), "PWM_Quarry_2x2x5_A_187", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2124.338, 3044.299, 881.2235), (-5.596892684796368, 55.30037800117535, 178.19195973420608), (0.852433, 1.0, 1.0), "PWM_Quarry_2x2x5_A_196", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1890.4575, 2284.1814, 1297.7393), (-64.736265307238, 58.93190504068215, 124.06865837395321), (0.852433, 1.0, 1.0), "PWM_Quarry_2x2x5_A_205", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1569.9629, 2551.0044, 1298.9806), (67.95653064523725, -164.10375327694598, -75.52570800782995), (0.852433, 1.0, 1.0), "PWM_Quarry_2x2x5_A_214", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2003.3395, 2412.9104, 1350.3933), (63.3101387882351, -155.96139642288128, 106.23451266585963), (0.852433, 1.0, 1.0), "PWM_Quarry_2x2x5_A_223", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5127.3677, 2803.3604, 781.33936), (3.0008156254373293, -106.05458556982357, 2.8605818365883566), (1.095301, 1.095301, 1.164734), "PWM_Quarry_2x2x5_A15_0", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5233.747, 2696.7832, 819.77185), (3.0008166283997335, 31.757889090734473, 2.860582871314559), (1.095301, 1.095301, 1.164734), "PWM_Quarry_2x2x5_A15_5", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4234.985, 3725.3308, 541.33936), (3.0008163022679786, -151.05452248428372, 2.860582420683537), (1.095301, 1.095301, 1.164734), "PWM_Quarry_2x2x5_A15_10", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3957.3018, 4651.3506, 539.24927), (-8.248010409856098, 28.953056268942248, 2.6988276200935912), (1.095301, 1.095301, 1.164734), "PWM_Quarry_2x2x5_A15_90", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4970.0796, 4018.4893, 730.51074), (-8.248010640970262, 76.76582006809667, 2.698807123981875), (1.095301, 1.095301, 1.164734), "PWM_Quarry_2x2x5_A15_104", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3689.0435, 4574.348, 531.5847), (3.0008167164080413, 99.25802412475885, 2.8605812751913913), (1.095301, 1.095301, 1.164734), "PWM_Quarry_2x2x5_A15_109", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3841.8784, 4593.771, 531.5847), (3.000815848080149, 6.445552484759738, 2.8605819126372136), (1.095301, 1.095301, 1.164734), "PWM_Quarry_2x2x5_A15_123", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4703.885, 4735.661, 543.86066), (-8.248010419932822, -151.04706200308416, 2.698834809595099), (1.095301, 1.095301, 1.164734), "PWM_Quarry_2x2x5_A15_131", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4618.4087, 4677.94, 1070.3503), (-8.675003437236054, -145.26376994004707, 0.5229341906802142), (1.095301, 1.095301, 1.164734), "PWM_Quarry_2x2x5_A16", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5138.1304, 2802.2812, 1317.7275), (2.5014272689583037, -100.3335693798661, 1.8112058998041995), (1.095301, 1.095301, 1.164734), "PWM_Quarry_2x2x5_A16_2", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5226.497, 2704.8105, 1356.16), (2.501426836903887, 37.478871691611786, 1.8112051004727918), (1.095301, 1.095301, 1.164734), "PWM_Quarry_2x2x5_A16_7", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4241.832, 3716.9573, 1077.7275), (2.501426850648281, -145.33343295056682, 1.8112053099553722), (1.095301, 1.095301, 1.164734), "PWM_Quarry_2x2x5_A16_12", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4042.7778, 4709.0713, 1065.739), (-8.675002363601413, 34.73635650047735, 0.5229286521899663), (1.095301, 1.095301, 1.164734), "PWM_Quarry_2x2x5_A16_92", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4984.7134, 4120.5854, 1257.0005), (-8.675000361004217, 82.5491188890741, 0.5229082767070958), (1.095301, 1.095301, 1.164734), "PWM_Quarry_2x2x5_A16_106", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3678.8535, 4570.722, 1067.9729), (2.501427110004976, 104.97908023975383, 1.8112054344589597), (1.095301, 1.095301, 1.164734), "PWM_Quarry_2x2x5_A16_111", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3838.7566, 4604.1274, 1067.9729), (2.501427227328955, 12.166587124117246, 1.8112057810362094), (1.095301, 1.095301, 1.164734), "PWM_Quarry_2x2x5_A16_125", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5102.9277, 2803.5918, 1365.5786), (-0.6351318833196093, 78.27727369878306, -176.47408754036098), (1.0, 1.0, 1.069433), "PWM_Quarry_2x2x5_A17_4", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5251.7007, 2680.1985, 1404.0111), (-0.6351317265264559, -143.91023344731107, -176.474088374257), (1.0, 1.0, 1.069433), "PWM_Quarry_2x2x5_A17_9", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4217.8667, 3742.7761, 1125.5786), (-0.6351317205243288, 33.27740697718471, -176.47408912936032), (1.0, 1.0, 1.069433), "PWM_Quarry_2x2x5_A17_14", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4074.8247, 4687.5723, 1110.9216), (10.56890088062016, -146.63363244426225, -175.45286909272605), (1.0, 1.0, 1.069433), "PWM_Quarry_2x2x5_A17_94", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5022.1646, 4129.893, 1302.1831), (10.568899374441283, -98.82084971597628, -175.4528477237735), (1.0, 1.0, 1.069433), "PWM_Quarry_2x2x5_A17_108", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3711.2363, 4584.589, 1115.824), (-0.6351319676032979, -76.41005083119069, -176.47408846701254), (1.0, 1.0, 1.069433), "PWM_Quarry_2x2x5_A17_113", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3851.0173, 4571.1025, 1115.824), (-0.6351317033871694, -169.22248353796638, -176.47408771747106), (1.0, 1.0, 1.069433), "PWM_Quarry_2x2x5_A17_127", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4586.3623, 4699.4395, 1115.533), (10.568900510370248, 33.3662243138864, -175.45287372479135), (1.0, 1.0, 1.069433), "PWM_Quarry_2x2x5_A17_146", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3948.7236, 4571.1025, 1083.736), (-0.635131708042622, -169.2224499432789, -176.47408800969106), (1.0, 1.0, 1.069433), "PWM_Quarry_2x2x5_A18", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3948.7236, 4571.1025, 623.0101), (-0.635131708042622, -169.2224499432789, -176.47408800969106), (1.0, 1.0, 1.069433), "PWM_Quarry_2x2x5_A19", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3014.567, 5256.4653, 1020.81647), (-5.722930844620409, -123.98366311384882, -178.8293809693513), (1.0, 1.0, 1.0), "PWM_Quarry_2x2x5_A2_265", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5088.0303, 3124.5369, 1228.757), (-69.56223136346249, 175.33062217302637, -86.55863816991618), (1.423122, 1.423122, 1.743923), "PWM_Quarry_2x2x5_A27_57", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4779.017, 4763.668, 1125.5858), (-59.50577104858043, -109.04852056760303, -71.3952612068291), (1.423122, 1.423122, 1.743923), "PWM_Quarry_2x2x5_A27_74", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4251.971, 2769.0366, 1359.1943), (-67.32919126939109, -25.45052985711878, -64.25728363145333), (1.423122, 1.423122, 1.743923), "PWM_Quarry_2x2x5_A27_1041", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4972.3594, 2821.0095, 1286.7627), (-64.77142323097225, 95.48754422948849, 84.64260860342827), (1.164529, 1.164529, 1.164529), "PWM_Quarry_2x2x5_A28_58", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5087.775, 4651.141, 1155.2544), (-54.84179734756248, -163.60866437249612, 71.37251175692677), (1.164529, 1.164529, 1.164529), "PWM_Quarry_2x2x5_A28_75", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4367.644, 3077.7908, 1372.0283), (-56.362292874553674, -85.7805607181747, 86.09418546738091), (1.164529, 1.164529, 1.164529), "PWM_Quarry_2x2x5_A28_1042", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4793.1064, 3026.5486, 1284.1819), (70.74236624600798, -92.05320642715266, 89.57663936402903), (1.164529, 1.164529, 1.164529), "PWM_Quarry_2x2x5_A29_60", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4884.087, 4477.8735, 1208.8678), (61.35477742213678, 14.28061414446541, 108.04240541605512), (1.164529, 1.164529, 1.164529), "PWM_Quarry_2x2x5_A29_77", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4546.895, 2874.096, 1399.6387), (62.30746674280333, 88.54264596668402, 90.22498498724838), (1.164529, 1.164529, 1.164529), "PWM_Quarry_2x2x5_A29_1044", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2492.2878, 5257.5483, 1019.0441), (-2.5338132244013623, -14.748628108600522, 179.39213086398232), (1.0, 1.2936424, 1.0), "PWM_Quarry_2x2x5_A3", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4862.712, 3693.4753, 1154.0237), (-22.13691269565832, -91.5167050037545, 96.04100763647595), (1.164529, 1.164529, 1.164529), "PWM_Quarry_2x2x5_A30_61", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4205.2764, 4542.1743, 1168.1113), (-29.96849050927621, -6.552608057966918, 106.04716706856208), (1.164529, 1.164529, 1.164529), "PWM_Quarry_2x2x5_A30_78", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4477.2847, 2195.2878, 1368.7617), (-30.572388984888732, 88.367737630285, 96.29952644338934), (1.164529, 1.164529, 1.164529), "PWM_Quarry_2x2x5_A30_1045", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4972.3594, 2870.6833, 1241.0955), (-59.71415278423527, 122.71733537346587, 54.057055050691346), (1.164529, 1.164529, 1.164529), "PWM_Quarry_2x2x5_A31", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4225.2812, 3491.2207, 1157.3779), (-79.43568271088022, -48.51922109937038, -43.34276089375844), (1.352483, 1.352483, 1.352483), "PWM_Quarry_2x2x5_A32_64", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4405.8535, 3907.7798, 1235.565), (-88.45986790553387, -108.21011894258815, 105.79946020780557), (1.352483, 1.352483, 1.352483), "PWM_Quarry_2x2x5_A32_81", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5114.718, 2395.8418, 1342.631), (-83.00799654184874, -176.0448628350071, -96.33237527988581), (1.352483, 1.352483, 1.352483), "PWM_Quarry_2x2x5_A32_1048", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4495.054, 3722.2468, 1193.6456), (13.308759508726924, -90.13080893274783, -91.52945295965725), (1.0, 1.0, 1.0), "PWM_Quarry_2x2x5_A33_66", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4182.6416, 4184.866, 1265.0037), (4.836056822619028, 0.5916519596127429, -83.0422469737445), (1.0, 1.0, 1.0), "PWM_Quarry_2x2x5_A33_83", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4844.942, 2172.64, 1412.1777), (4.870099613818313, 89.87180758205855, -91.51011254288633), (1.0, 1.0, 1.0), "PWM_Quarry_2x2x5_A33_1050", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4432.8623, 3571.5737, 1227.712), (-8.331929056146262, 85.71894040237956, -85.12499131243682), (1.0, 1.0, 1.0), "PWM_Quarry_2x2x5_A34_67", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4336.6855, 4125.0522, 1285.5902), (-0.5384025370300795, 175.79938699219434, -94.1673856675041), (1.0, 1.0, 1.0), "PWM_Quarry_2x2x5_A34_84", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4907.1357, 2326.6814, 1423.7637), (0.08351808373139391, -94.23617705266446, -85.7526751746021), (1.0, 1.0, 1.0), "PWM_Quarry_2x2x5_A34_1051", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4425.868, 3086.7483, 1229.9075), (-64.06305248921605, 80.75971326299369, 101.04581930880912), (1.0, 1.0, 1.0), "PWM_Quarry_2x2x5_A35_68", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4816.585, 4108.027, 1218.3867), (-55.84788627719942, -174.7086106953158, 83.61814699027329), (1.0, 1.0, 1.0), "PWM_Quarry_2x2x5_A35_85", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4914.1333, 2806.5803, 1354.7871), (-55.70895740910222, -97.16150301973745, 98.64857074515949), (1.0, 1.0, 1.0), "PWM_Quarry_2x2x5_A35_1052", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4425.87, 2810.9087, 1270.8301), (-50.608553899426774, 83.64615745502816, 97.64089758731352), (1.0, 1.0, 1.251034), "PWM_Quarry_2x2x5_A36_70", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5095.444, 4108.037, 1218.387), (-42.44922337394046, -177.73665469852642, 84.96663990518182), (1.0, 1.0, 1.251034), "PWM_Quarry_2x2x5_A36_87", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4914.133, 3085.4397, 1354.7871), (-42.21405176546748, -95.44159126877825, 96.38430251049331), (1.0, 1.0, 1.251034), "PWM_Quarry_2x2x5_A36_1054", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4714.016, 2888.2432, 1236.1206), (-52.24004790653451, 43.85819299801327, 143.4831574191568), (1.164529, 1.164529, 1.164529), "PWM_Quarry_2x2x5_A37", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4972.3594, 3071.9739, 1241.0955), (-59.714155187434315, 122.71734633175616, 54.057080571495014), (1.164529, 1.164529, 1.164529), "PWM_Quarry_2x2x5_A38", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5085.382, 3204.1746, 1158.9604), (11.638510578538764, 67.33382593040008, 16.267395549505533), (1.164529, 1.164529, 1.164529), "PWM_Quarry_2x2x5_A39", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4776.28, 2888.243, 1207.1351), (-64.8937358129656, 89.96432894650617, 90.7457088553494), (1.164529, 1.164529, 1.164529), "PWM_Quarry_2x2x5_A40", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4882.94, 3406.7705, 1203.6045), (-23.907438898625664, -95.13544886151, 98.68729420572834), (1.164529, 1.164529, 1.164529), "PWM_Quarry_2x2x5_A48_71", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4496.154, 4563.215, 1172.0377), (-31.1112301172188, -10.726293091034195, 109.39922559935289), (1.164529, 1.164529, 1.164529), "PWM_Quarry_2x2x5_A48_88", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4457.0586, 2486.1663, 1375.7314), (-32.309580437789265, 84.44337132126641, 99.5778600487868), (1.164529, 1.164529, 1.164529), "PWM_Quarry_2x2x5_A48_1055", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2335.0242, 2869.8599, 1060.7201), (-4.102905444644302, -46.359602856161835, -0.5897823384569993), (1.203323, 1.203323, 1.203323), "PWM_Quarry_2x2x5_B11", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2258.823, 2030.7324, 928.6579), (0.7475914987677637, 67.00894518226998, -178.67379357968838), (1.0, 1.0, 1.0), "PWM_Quarry_2x2x5_B7", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2275.6892, 2030.7324, 1184.8323), (1.1315094890527322, 27.26234989574571, -2.482543568474192), (1.0, 1.0, 1.0), "PWM_Quarry_2x2x5_B8", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2300.0, 2869.8599, 891.9098), (0.7475915267656557, 0.4849378057703329, -178.67379334428583), (1.2033228, 1.2033228, 1.2033228), "PWM_Quarry_2x2x5_B9", _folder)
if a: placed += 1
else: skipped += 1

# Batch 57: StaticMesh'PWM_Quarry_2x2x5_B' (98 instances)
_mesh_path = "/Game/Unshippable/Whitebox/Rocks/Meshes/PWM_Quarry_2x2x5_B"
_materials = ['/Game/Environments/ProcTexturing/ProcMaterial_Quarry_Atlas_2']
_folder = "Reconstruction/BD_BB_OrcPrison/Meshes"
a = spawn_static_mesh(_mesh_path, _materials, (4094.1304, 3776.596, 855.2881), (2.1734545744944715, 76.56111293306348, 0.7229665137457119), (0.8443611, 1.3330994, 1.3330994), "PWM_Quarry_2x2x5_B_18", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4534.217, 2949.2495, 875.2881), (2.173454313504605, 32.463799956352126, 0.7229667154928207), (0.511262, 1.0, 1.0), "PWM_Quarry_2x2x5_B_27", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4323.8906, 3722.5874, 815.2881), (2.173453962060338, -144.7237383898706, 0.7229663079737169), (0.511262, 1.0, 1.0), "PWM_Quarry_2x2x5_B_36", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4196.711, 2805.9731, 875.2881), (4.895626510995649, -57.77793982808068, 2.4381526758696177), (0.84815717, 1.3368953, 1.3368953), "PWM_Quarry_2x2x5_B_45", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5232.885, 2266.295, 885.2881), (2.173461549361678, 9.963586258927329, 0.7229667894766971), (0.511262, 1.0, 1.0), "PWM_Quarry_2x2x5_B_54", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4742.3403, 4625.252, 815.2881), (2.173454011963376, -122.2237945645284, 0.7229663851881837), (0.511262, 1.0, 1.0), "PWM_Quarry_2x2x5_B_98", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3923.8413, 4467.9346, 1187.4558), (-60.37058168815834, -89.45107461963107, -91.14450494665661), (0.511262, 1.0, 1.0), "PWM_Quarry_2x2x5_B_117", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3790.0837, 4187.934, 1272.5455), (60.37010373338221, -90.54858421858883, 88.8551329707257), (0.511262, 1.0, 1.0), "PWM_Quarry_2x2x5_B_131", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4535.217, 5193.888, 808.6483), (-5.831909988691571, -144.63821135577956, -1.945556974236186), (0.511262, 1.0, 1.0), "PWM_Quarry_2x2x5_B_141", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4489.9893, 5163.394, 810.87573), (13.001390829493054, 105.99781209269929, 3.8072706327588928), (0.511262, 1.0, 1.0), "PWM_Quarry_2x2x5_B_150", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4056.505, 5083.7, 816.13153), (10.296701193229438, -164.16118570470317, 3.019821598149976), (0.511262, 1.0, 1.0), "PWM_Quarry_2x2x5_B_159", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4332.924, 5132.516, 1072.0905), (70.9403848589359, -58.13379549110501, 105.81614188225491), (0.511262, 1.0, 1.0), "PWM_Quarry_2x2x5_B_168", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2166.4043, 2125.7678, 884.8226), (2.173454751210614, -31.97557501805478, 0.7229689036062885), (1.0, 1.0, 1.0), "PWM_Quarry_2x2x5_B_177", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1466.7637, 2676.2917, 915.2881), (2.1734548837736236, -113.78626949130528, 0.7229665202956553), (0.511262, 1.0, 1.0), "PWM_Quarry_2x2x5_B_186", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2041.9888, 3118.7715, 875.2881), (2.173454718870629, -127.84871880320446, 0.7229669978196451), (0.511262, 1.0, 1.0), "PWM_Quarry_2x2x5_B_195", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1875.7358, 2391.8547, 1321.2485), (64.88611529937194, -131.99309201086635, 45.168221932270875), (0.511262, 1.0, 1.0), "PWM_Quarry_2x2x5_B_204", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1462.11, 2556.817, 1273.5635), (-69.61309691703272, 27.920052315056388, -116.56120005000973), (0.511262, 1.0, 1.0), "PWM_Quarry_2x2x5_B_213", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4270.839, 2802.4482, 1272.6843), (-49.317837934765045, 74.51012100226478, -59.0522381641643), (0.913002, 0.913002, 0.913002), "PWM_Quarry_2x2x5_B10_62", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5104.0903, 3954.77, 1241.7205), (-42.56016328077486, 174.1054316505064, -73.21093919093794), (0.913002, 0.913002, 0.913002), "PWM_Quarry_2x2x5_B10_79", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5069.165, 3094.0806, 1355.3789), (-41.142898055150994, -103.36663985194419, -62.03552296940574), (0.913002, 0.913002, 0.913002), "PWM_Quarry_2x2x5_B10_1046", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4128.2407, 2885.6233, 982.54315), (4.261573036223822, 15.55806737583981, 0.9602409690756162), (0.848157, 1.336895, 1.336895), "PWM_Quarry_2x2x5_B12", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3695.4736, 3793.648, 962.1752), (2.4513271319094567, 89.8180610057891, 178.50974686371214), (0.560515, 1.0, 1.0), "PWM_Quarry_2x2x5_B2_21", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4488.9297, 3297.7935, 982.1752), (-7.992308351953722, 14.007526670239125, 175.91725229549485), (0.560515, 1.0, 1.0), "PWM_Quarry_2x2x5_B2_30", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4410.637, 3377.8843, 922.1752), (2.4513268729462676, -163.30673290105767, 178.50974685545617), (0.560515, 1.0, 1.0), "PWM_Quarry_2x2x5_B2_39", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4520.5894, 2845.1958, 982.1752), (2.4513270507303133, -81.74448738422554, 178.50974671767514), (0.560515, 1.0, 1.0), "PWM_Quarry_2x2x5_B2_48", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5301.8477, 2614.9915, 992.1752), (2.451327327899544, -8.619413475573458, 178.50974703929896), (0.560515, 1.0, 1.0), "PWM_Quarry_2x2x5_B2_71", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4954.396, 4339.9844, 922.1752), (2.4513269560633524, -140.80678204570415, 178.5097468867961), (0.560515, 1.0, 1.0), "PWM_Quarry_2x2x5_B2_101", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3814.5093, 4116.388, 1234.6903), (-78.93727099468754, -88.38950156752382, 86.3900171759021), (0.560515, 1.0, 1.0), "PWM_Quarry_2x2x5_B2_120", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3899.4194, 3836.3887, 1225.3082), (78.93684690338259, -91.61022077758916, -93.61019167578735), (0.560515, 1.0, 1.0), "PWM_Quarry_2x2x5_B2_134", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4607.133, 4844.6865, 911.8766), (-5.985938731965923, -163.30741641756242, 178.53660319527825), (0.560515, 1.0, 1.0), "PWM_Quarry_2x2x5_B2_144", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4136.2124, 5176.3315, 922.4304), (13.68559126225818, 86.92082522074496, 177.90874696138172), (0.560515, 1.0, 1.0), "PWM_Quarry_2x2x5_B2_153", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4038.1096, 4729.924, 926.91656), (10.877145052454049, 176.95362561997464, 178.06259506309135), (0.560515, 1.0, 1.0), "PWM_Quarry_2x2x5_B2_162", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4538.9595, 4824.005, 1083.8712), (84.72926893372095, 18.85587697747913, 0.48819427658148173), (0.560515, 1.0, 1.0), "PWM_Quarry_2x2x5_B2_171", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1718.3805, 2425.2266, 1022.1752), (2.451327226796701, -132.36931455418488, 178.50974682830147), (0.560515, 1.0, 1.0), "PWM_Quarry_2x2x5_B2_189", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2225.0613, 2814.0928, 1084.0114), (4.821929428609977, 53.37378539667509, -178.30740981768653), (0.6366856, 1.0761708, 1.0761708), "PWM_Quarry_2x2x5_B2_198", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1970.6141, 2036.813, 1373.3356), (72.74865890571337, 179.38694475217218, 177.93254415793675), (0.560515, 1.0, 1.0), "PWM_Quarry_2x2x5_B2_207", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1821.458, 2472.852, 1235.983), (-81.19731732967293, 93.99971772044633, -2.6564427588686783), (0.560515, 1.0, 1.0), "PWM_Quarry_2x2x5_B2_216", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1806.7273, 2571.1807, 1316.1758), (-78.21139757154081, 45.624533453474726, -134.96010972685332), (0.560515, 1.0, 1.0), "PWM_Quarry_2x2x5_B2_225", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4391.941, 3354.2705, 1219.8154), (-5.7647119392283015, -87.97968861805829, 84.35160773347785), (1.149598, 1.0, 1.490437), "PWM_Quarry_2x2x5_B21_63", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4550.4785, 4078.754, 1252.3245), (-14.345307103541893, -0.07479582167596024, 92.751336370771), (1.149598, 1.0, 1.490437), "PWM_Quarry_2x2x5_B21_80", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4948.0586, 2540.473, 1384.0635), (-14.198019031404051, 92.07297718127113, 84.04586137453066), (1.149598, 1.0, 1.490437), "PWM_Quarry_2x2x5_B21_1047", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4152.658, 3051.2485, 1197.5934), (11.731084063091753, 9.095252855246141, 112.66889852421995), (1.0, 1.0, 1.0), "PWM_Quarry_2x2x5_B22_65", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4846.967, 3832.32, 1221.7035), (4.562458008996623, 97.10470766750817, 103.05192080905029), (1.0, 1.0, 1.0), "PWM_Quarry_2x2x5_B22_82", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5186.414, 2836.9517, 1317.6123), (12.93404738716745, -172.73476553056977, 104.1185587475144), (1.0, 1.0, 1.0), "PWM_Quarry_2x2x5_B22_1049", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5242.589, 2524.1338, 1016.37305), (-10.49813572641032, 161.99996534835248, 1.543835348087431), (0.560515, 1.310848, 0.848003), "PWM_Quarry_2x2x5_B3", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5136.7607, 2814.1086, 1297.4619), (2.2359040420570953, -27.865139594597085, 8.593188735233944), (1.088945, 1.088945, 1.158378), "PWM_Quarry_2x2x5_B3_1", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5219.5693, 2695.127, 1335.8944), (2.2359040181440255, 109.94724016004027, 8.593189696779943), (1.088945, 1.088945, 1.158378), "PWM_Quarry_2x2x5_B3_6", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4249.227, 3726.2893, 1057.4619), (2.235904172251266, -72.86502330336927, 8.59318927015691), (1.088945, 1.088945, 1.158378), "PWM_Quarry_2x2x5_B3_11", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3794.0432, 3748.3623, 986.37305), (-10.49813667652595, -99.5625382100037, 1.5438348743803716), (0.560515, 1.310848, 0.848003), "PWM_Quarry_2x2x5_B3_22", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4464.093, 3191.1748, 1006.37305), (-10.498136273134605, -175.49982189319093, 1.5438353661054582), (0.560515, 1.310848, 0.848003), "PWM_Quarry_2x2x5_B3_31", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4425.3594, 3485.355, 946.37305), (-10.498135306274625, 7.312625810070885, 1.5438357972237), (0.560515, 1.310848, 0.848003), "PWM_Quarry_2x2x5_B3_40", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4416.4424, 2847.2354, 1006.37305), (-10.49813539136112, 88.87482777656315, 1.5438357026732021), (0.560515, 1.310848, 0.848003), "PWM_Quarry_2x2x5_B3_49", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4032.0815, 4697.9746, 1047.9934), (0.06309096501963768, 106.9128189615726, -2.4478837138485323), (1.088945, 1.088945, 1.158378), "PWM_Quarry_2x2x5_B3_91", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4926.87, 4444.9087, 946.37305), (-10.498136605877232, 29.812594015498302, 1.5438350095765738), (0.560515, 1.310848, 0.848003), "PWM_Quarry_2x2x5_B3_102", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4985.7524, 4105.208, 1239.2549), (0.06310996681417157, 154.7255881782265, -2.4478888049049274), (1.088945, 1.088945, 1.158378), "PWM_Quarry_2x2x5_B3_105", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3685.1484, 4560.616, 1047.7074), (2.2359034253588717, 177.44747076658933, 8.593171475803775), (1.088945, 1.088945, 1.158378), "PWM_Quarry_2x2x5_B3_110", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3789.1033, 4221.898, 1258.658), (82.13376047259047, 12.216603070268071, 13.955866220063392), (0.560515, 1.310848, 0.848003), "PWM_Quarry_2x2x5_B3_121", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3828.354, 4598.3354, 1047.7073), (2.2359034846370713, 84.63495676202479, 8.593190347075696), (1.088945, 1.088945, 1.158378), "PWM_Quarry_2x2x5_B3_124", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4629.1055, 4689.0366, 1052.6046), (0.06309084667106322, -73.08727754784024, -2.4478828002281223), (1.088945, 1.088945, 1.158378), "PWM_Quarry_2x2x5_B3_135", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3924.8242, 3941.899, 1201.3418), (-82.1338485554831, 167.7803250335172, -166.0405090268765), (0.560515, 1.310848, 0.848003), "PWM_Quarry_2x2x5_B3_136", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4617.9883, 4950.984, 942.4572), (-2.1757582266583775, 7.467453295506533, 0.1461062324580156), (0.560515, 1.310848, 0.848003), "PWM_Quarry_2x2x5_B3_145", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4232.441, 5122.5054, 936.3957), (-21.473403671105373, -103.08754509874525, 4.118911608382468), (0.560515, 1.310848, 0.848003), "PWM_Quarry_2x2x5_B3_154", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4091.1855, 4826.1523, 943.5062), (-18.73272407412101, -12.856395783535126, 3.4466173996485447), (0.560515, 1.310848, 0.848003), "PWM_Quarry_2x2x5_B3_163", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4531.343, 4924.699, 1037.4515), (-73.63305771657086, -127.69546813282801, 145.46987612902254), (0.560515, 1.310848, 0.848003), "PWM_Quarry_2x2x5_B3_172", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1900.8167, 2249.6897, 1096.373), (-10.498137872213196, -124.87490877611482, 1.5438360267512823), (0.560515, 1.310848, 0.848003), "PWM_Quarry_2x2x5_B3_181", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1675.7574, 2524.9758, 1046.373), (-10.498136942423898, 38.250038256475335, 1.543836380925826), (0.560515, 1.310848, 0.848003), "PWM_Quarry_2x2x5_B3_190", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2207.9524, 2921.2095, 1006.37305), (-10.498136235386907, 24.187606166401803, 1.5438358994187278), (0.560515, 1.310848, 0.848003), "PWM_Quarry_2x2x5_B3_199", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2008.6631, 2135.3816, 1338.8591), (-76.97293863373234, -46.439538717433486, 45.47834633259334), (0.560515, 1.310848, 0.848003), "PWM_Quarry_2x2x5_B3_208", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1724.6151, 2435.4868, 1275.6766), (80.57922077674371, -0.8624145491692768, -93.93856814904166), (0.560515, 1.310848, 0.848003), "PWM_Quarry_2x2x5_B3_217", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1896.7938, 2593.2117, 1377.4501), (65.90840234999833, -135.53477284591847, -47.15835689450848), (0.560515, 1.310848, 0.848003), "PWM_Quarry_2x2x5_B3_226", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5227.1504, 2420.0664, 789.45264), (-4.21710175769423, 170.8212134069033, -177.24745566620481), (0.560515, 1.0, 0.709184), "PWM_Quarry_2x2x5_B4", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5087.3813, 2805.2966, 771.605), (2.3979903303053254, -72.2320921596541, 1.6560513411815747), (1.0, 1.0, 1.069433), "PWM_Quarry_2x2x5_B4_3", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5269.0044, 2662.2146, 810.0375), (2.3979901708260867, 65.58027552136527, 1.6560507830613889), (1.0, 1.0, 1.069433), "PWM_Quarry_2x2x5_B4_8", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4201.467, 3761.5876, 531.605), (2.3979905178787884, -117.23206839717949, 1.6560510998361055), (1.0, 1.0, 1.069433), "PWM_Quarry_2x2x5_B4_13", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3899.2493, 3748.3606, 759.45264), (-4.217101216805771, -90.74122848045049, -177.2474556592835), (0.560515, 1.0, 0.709184), "PWM_Quarry_2x2x5_B4_23", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4501.863, 3089.1208, 779.45264), (-4.217101482680118, -166.6785237612245, -177.2474559364256), (0.560515, 1.0, 0.709184), "PWM_Quarry_2x2x5_B4_32", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4394.821, 3586.0315, 719.45264), (-4.217101495688774, 16.133900027490924, -177.24745581083127), (0.560515, 1.0, 0.709184), "PWM_Quarry_2x2x5_B4_41", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4312.374, 2831.8, 779.45264), (-4.217101779069206, 97.69610450865983, -177.24745610492053), (0.560515, 1.0, 0.709184), "PWM_Quarry_2x2x5_B4_50", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3988.9346, 4614.0854, 527.2693), (-6.85316652386521, 63.01836802400218, -4.757222297398971), (1.0, 1.0, 1.069433), "PWM_Quarry_2x2x5_B4_93", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4860.129, 4526.235, 719.45264), (-4.217101541130475, 38.63384704992313, -177.2474560604842), (0.560515, 1.0, 0.709184), "PWM_Quarry_2x2x5_B4_103", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5018.9346, 4016.902, 718.53076), (-6.85315567744585, 110.83113516818314, -4.757239783557647), (1.0, 1.0, 1.069433), "PWM_Quarry_2x2x5_B4_107", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3734.4734, 4593.693, 521.85034), (2.397990321802166, 133.08044609693073, 1.6560515584831368), (1.0, 1.0, 1.069433), "PWM_Quarry_2x2x5_B4_112", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4016.7563, 4325.0854, 1249.2926), (79.41727402738799, 82.07115250568998, -94.53051146362405), (0.560515, 1.0, 0.709184), "PWM_Quarry_2x2x5_B4_122", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3858.9707, 4547.4473, 521.85034), (2.3979902671475997, 40.26795541482173, 1.6560515783413363), (1.0, 1.0, 1.069433), "PWM_Quarry_2x2x5_B4_126", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3697.1704, 4045.084, 1210.7069), (-79.41690126590063, 97.92792023333784, 85.4704153079232), (0.560515, 1.0, 0.709184), "PWM_Quarry_2x2x5_B4_137", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4672.2524, 4772.9263, 531.8807), (-6.853171450937507, -116.98174516758831, -4.757218233186778), (1.0, 1.0, 1.069433), "PWM_Quarry_2x2x5_B4_143", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4619.311, 5061.326, 717.99304), (4.219509098255763, 16.134031287353842, -177.35649187732082), (0.560515, 1.0, 0.709184), "PWM_Quarry_2x2x5_B4_146", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4337.5205, 5161.711, 712.82806), (-15.444827022597131, -93.67706060636058, -176.52858694005232), (0.560515, 1.0, 0.709184), "PWM_Quarry_2x2x5_B4_155", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4062.9973, 4931.2314, 718.2843), (-12.63808276674159, -3.632173732776433, -176.713435891669), (0.560515, 1.0, 0.709184), "PWM_Quarry_2x2x5_B4_164", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4283.9146, 4959.5747, 1048.5974), (-82.92811488286407, -157.10722206915602, -3.2722853427152976), (0.560515, 1.0, 0.709184), "PWM_Quarry_2x2x5_B4_173", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1995.9214, 2204.707, 869.45264), (-4.217101514479271, -116.05361258763726, -177.2474561716342), (0.560515, 1.0, 0.709184), "PWM_Quarry_2x2x5_B4_182", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1597.8057, 2595.6292, 819.45264), (-4.21710191294637, 47.071289182110405, -177.24745598222032), (0.560515, 1.0, 0.709184), "PWM_Quarry_2x2x5_B4_191", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2149.5042, 3008.686, 779.45264), (-4.217102031980653, 33.00890967425612, -177.24745628072824), (0.560515, 1.0, 0.709184), "PWM_Quarry_2x2x5_B4_200", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1795.0281, 2240.5898, 1262.3579), (-74.49855103414893, -2.767220875954162, -174.63573149865366), (0.560515, 1.0, 0.709184), "PWM_Quarry_2x2x5_B4_209", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1608.6173, 2652.6155, 1319.9556), (82.92677362779828, -81.17285782617971, 8.667500167323704), (0.560515, 1.0, 0.709184), "PWM_Quarry_2x2x5_B4_218", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2010.2848, 2370.4324, 1370.3573), (76.56203438534446, -130.51016315280611, 139.9623708008157), (0.560515, 1.0, 0.709184), "PWM_Quarry_2x2x5_B4_227", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3824.2273, 3793.648, 962.1752), (2.4513271319094567, 89.8180610057891, 178.50974686371214), (0.560515, 1.0, 1.0), "PWM_Quarry_2x2x5_B5", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5097.341, 2957.9429, 1001.01025), (7.797034739307211, -79.09207146100998, -23.3562571498387), (1.0, 1.0, 1.069433), "PWM_Quarry_2x2x5_B6", _folder)
if a: placed += 1
else: skipped += 1

# Batch 58: StaticMesh'PWM_Quarry_4x4x4_A' (50 instances)
_mesh_path = "/Game/Unshippable/Whitebox/Rocks/Meshes/PWM_Quarry_4x4x4_A"
_materials = ['/Game/Environments/ProcTexturing/ProcMaterial_Quarry_Atlas_2']
_folder = "Reconstruction/BD_BB_OrcPrison/Meshes"
a = spawn_static_mesh(_mesh_path, _materials, (5161.0947, 3322.1138, 1048.0405), (2.7320753230836935e-05, 6.2510235409343835, 5.399997151819915e-05), (0.5625, 1.25, 0.5), "BP_Quarry_4x4x4_A_Breakable_6", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4559.8037, 2002.0464, 1038.0405), (2.7320758025121313e-05, -86.56195671883866, 5.399999621177533e-05), (0.5625, 1.25, 0.5), "BP_Quarry_4x4x4_A_Breakable_96", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5229.623, 3233.7874, 1448.042), (2.573582303058765e-05, -78.74885454439477, -89.9999447768372), (1.125, 0.5625, 0.5625), "BP_Quarry_4x4x4_A_Breakable2_7", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4468.2207, 1937.9353, 1438.042), (2.7100162794752845e-05, -171.56189403096243, -89.99993789958889), (1.125, 0.5625, 0.5625), "BP_Quarry_4x4x4_A_Breakable2_97", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5092.522, 3410.4436, 1248.0405), (-35.000027490353766, -168.74904979735487, -89.99983921479995), (0.4375, 0.5, 1.0), "BP_Quarry_4x4x4_A_Breakable3_8", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4651.3926, 2066.2014, 1238.0405), (-35.00003452363832, 98.43797757698087, -89.999880460567), (0.4375, 0.5, 1.0), "BP_Quarry_4x4x4_A_Breakable3_98", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5072.4883, 2998.61, 1448.0415), (2.7320754900744325e-05, 96.25103451489339, 2.9934716518650947e-12), (0.6875, 0.5, 0.625), "BP_Quarry_4x4x4_A_Breakable4_9", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4241.038, 2106.422, 1438.0415), (2.7320752982122664e-05, 3.438057594847608, 1.6163872878385354e-12), (0.6875, 0.5, 0.625), "BP_Quarry_4x4x4_A_Breakable4_99", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5082.7896, 3459.4766, 798.0419), (35.00001048160225, -178.7489510529524, 90.00018142530334), (0.4375, 0.5, 1.0), "BP_Quarry_4x4x4_A_Breakable6_11", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4700.8438, 2073.516, 788.0419), (35.00002864962879, 88.43809418272588, 90.00021695339089), (0.4375, 0.5, 1.0), "BP_Quarry_4x4x4_A_Breakable6_101", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2979.7249, 5490.829, 990.3729), (5.156013170395751, 20.69305202815333, 1.9442269295658994), (0.4630975, 1.0, 1.0), "PWM_Quarry_4x4x4_A_269", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3826.061, 1571.1847, 978.02057), (0.0697907442188963, 84.11772279597442, 3.204854088020822), (0.398175, 1.0, 1.0), "PWM_Quarry_4x4x4_A10", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4119.2754, 1330.8523, 978.02057), (0.0, -7.299377873503824, 0.0), (0.5290895, 1.0, 1.0), "PWM_Quarry_4x4x4_A11", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3901.3137, 1116.9598, 1262.683), (17.489954694151304, -90.40191023855128, -6.235015465071354), (0.398175, 1.191707, 1.0), "PWM_Quarry_4x4x4_A12", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3901.3137, 1535.5731, 1262.683), (13.096409953304182, 87.03938622983355, -0.14441034067069247), (0.398175, 1.191707, 1.0), "PWM_Quarry_4x4x4_A13", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2561.6257, 1571.1879, 978.02057), (0.06979092464997579, 98.28928387538365, 3.2048896900804755), (0.398175, 1.0, 1.0), "PWM_Quarry_4x4x4_A14", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4164.871, 1295.0051, 1307.7543), (1.0863963972899535, -22.82018842831676, -1.857727048071979), (1.0, 1.0, 0.609223), "PWM_Quarry_4x4x4_A15", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3752.8662, 1301.5183, 1395.1504), (1.0863964176008885, -92.1870068294495, -1.857696814040333), (1.0, 1.0, 0.609223), "PWM_Quarry_4x4x4_A16", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2314.8186, 1287.1805, 978.02057), (0.06979097294833939, 165.49729053676978, 3.204997005859301), (0.398175, 1.1287657, 1.1657497), "PWM_Quarry_4x4x4_A17", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2599.2214, 1121.906, 978.02057), (0.06979099280899392, -104.58560899233058, 3.204950548155599), (0.398175, 1.0, 1.0), "PWM_Quarry_4x4x4_A18", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2695.0037, 1369.0112, 1397.8324), (1.0863964421909182, 89.07586812128088, -1.8576968780914611), (1.0, 1.0, 0.609223), "PWM_Quarry_4x4x4_A19", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5299.083, 2543.5923, 942.16205), (2.335315933780343, -2.647364475674214, 0.09473091859635895), (0.210967, 0.657378, 0.657378), "PWM_Quarry_4x4x4_A2", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3780.3833, 3801.3896, 912.16205), (2.3353166187754946, 95.7901254210701, 0.09473107721478474), (0.210967, 0.75751185, 0.657378), "PWM_Quarry_4x4x4_A2_16", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4483.1587, 3230.7715, 932.16205), (2.335316440839995, 19.852843291879577, 0.09473098343250001), (0.210967, 0.657378, 0.657378), "PWM_Quarry_4x4x4_A2_25", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4382.609, 3443.6104, 872.16205), (2.335316077137401, -157.3347068857079, 0.09473091274972197), (0.210967, 0.657378, 0.657378), "PWM_Quarry_4x4x4_A2_34", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4435.0815, 2824.8962, 920.2906), (2.3353162787403705, -75.77240846660352, 0.09473133551584537), (0.210967, 0.657378, 0.657378), "PWM_Quarry_4x4x4_A2_43", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4903.3486, 4389.9814, 872.16205), (2.335316381597367, -134.83464186025918, 0.09473080603830973), (0.210967, 0.657378, 0.657378), "PWM_Quarry_4x4x4_A2_96", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3865.5134, 4184.5454, 1215.7191), (-72.97015333819304, -88.791249109598, -91.88407187212229), (0.210967, 0.657378, 0.657378), "PWM_Quarry_4x4x4_A2_115", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3848.4143, 3904.5454, 1244.2799), (72.96969817753579, -91.20847246243014, 88.11523745552564), (0.210967, 0.657378, 0.657378), "PWM_Quarry_4x4x4_A2_129", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4586.207, 4912.5674, 861.2688), (-6.058901499186586, -157.3067863556147, -0.7581794665359342), (0.210967, 0.657378, 0.657378), "PWM_Quarry_4x4x4_A2_139", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4207.538, 5190.2544, 874.20685), (13.56976351002721, 93.06069523631614, 0.6920549781153694), (0.210967, 0.657378, 0.657378), "PWM_Quarry_4x4x4_A2_148", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4026.57, 4801.249, 878.068), (10.761261722732621, -176.97142519576252, 0.5393254761511964), (0.210967, 0.657378, 0.657378), "PWM_Quarry_4x4x4_A2_157", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4470.901, 4877.5854, 1094.0605), (82.25150660072234, -31.511791638992655, 131.72997507754596), (0.210967, 0.657378, 0.657378), "PWM_Quarry_4x4x4_A2_166", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1898.5952, 2253.772, 1128.3541), (2.3353163566581827, -124.50601860428137, 0.09473299909542825), (0.36128652, 0.74766225, 0.74766225), "PWM_Quarry_4x4x4_A2_175", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1660.5502, 2467.1921, 972.16205), (2.3353167254549287, -126.39720969170062, 0.09473106720502583), (0.210967, 0.657378, 0.657378), "PWM_Quarry_4x4x4_A2_184", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2191.2546, 2878.8352, 931.5224), (2.3353161552317596, -140.4596766362832, 0.09473090361833375), (0.210967, 0.657378, 0.657378), "PWM_Quarry_4x4x4_A2_193", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1920.9194, 2107.845, 1363.764), (71.7348052362224, -161.23909031168623, 17.735729843858316), (0.210967, 0.657378, 0.657378), "PWM_Quarry_4x4x4_A2_202", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1748.0411, 2519.869, 1238.1488), (-79.39356096643411, 59.60526595489088, -147.38622331518476), (0.210967, 0.657378, 0.657378), "PWM_Quarry_4x4x4_A2_211", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1880.156, 2524.1724, 1313.9343), (-81.59830797740841, 74.34808960500378, 18.066397747831708), (0.210967, 0.657378, 0.657378), "PWM_Quarry_4x4x4_A2_220", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2517.0786, 1369.0112, 1352.2759), (0.05094723018656682, -101.26567261650939, -7.064696539556036), (1.0, 1.0, 0.609223), "PWM_Quarry_4x4x4_A20", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2611.4084, 1121.906, 1161.423), (19.427928252923294, -105.48835688921481, -2.042878642368875), (0.398175, 1.0, 1.0), "PWM_Quarry_4x4x4_A21", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2558.4375, 1553.3116, 1196.7273), (20.720986888528742, 108.645576903196, 3.8017991771526405), (0.398175, 1.0, 1.0), "PWM_Quarry_4x4x4_A22", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1885.1782, 2270.3848, 865.219), (-4.757690682009088, -124.51920534035742, 0.09500382007658197), (0.361287, 0.747662, 0.747662), "PWM_Quarry_4x4x4_A23", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4416.9326, 2798.8225, 1170.1274), (2.3353163893138045, -75.77240847322633, 0.09473110419752562), (0.210967, 0.7076379, 0.657378), "PWM_Quarry_4x4x4_A3", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4966.0645, 4238.75, 872.16205), (2.3353161022591933, 178.9314596001078, 0.09473243477250382), (0.210967, 0.657378, 0.657378), "PWM_Quarry_4x4x4_A4", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4939.462, 4238.75, 1011.9076), (-30.319730272803678, 178.76401021938437, 0.7625288775492286), (0.210967, 0.657378, 0.657378), "PWM_Quarry_4x4x4_A5", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4943.1934, 4115.6826, 1068.3728), (-30.319730272803678, 178.76401021938437, 0.7625288775492286), (0.35434207, 0.62004316, 0.84374356), "PWM_Quarry_4x4x4_A6", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2513.6802, 5490.829, 990.3729), (-1.0254516267896532, 157.37296677542963, 4.526669599778592), (0.463098, 1.0, 1.0), "PWM_Quarry_4x4x4_A7", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2710.002, 5676.972, 990.3729), (-1.025359838380258, 82.53405712036744, 4.526761148456034), (0.463098, 1.0, 1.0), "PWM_Quarry_4x4x4_A8", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3826.061, 1073.4933, 978.02057), (0.0, -92.64144914013696, 0.0), (0.39817482, 1.0, 1.0), "PWM_Quarry_4x4x4_A9_805", _folder)
if a: placed += 1
else: skipped += 1

# Batch 59: StaticMesh'PWM_Quarry_8x8x8_A' (10 instances)
_mesh_path = "/Game/Unshippable/Whitebox/Rocks/Meshes/PWM_Quarry_8x8x8_A"
_materials = ['/Game/Environments/ProcTexturing/ProcMaterial_Quarry_Atlas_2']
_folder = "Reconstruction/BD_BB_OrcPrison/Meshes"
a = spawn_static_mesh(_mesh_path, _materials, (5112.0337, 3312.3562, 1498.042), (2.7320754322367026e-05, 6.251023540920602, 1.9999993717703518e-06), (0.1875, 0.625, 0.25), "BP_Quarry_8x8x8_A_Breakable2_4", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4552.466, 2051.5269, 1488.042), (2.7320756299498e-05, -86.56195671883837, 1.999999833782684e-06), (0.1875, 0.625, 0.25), "BP_Quarry_8x8x8_A_Breakable2_91", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5102.272, 3449.7207, 998.04095), (11.958813694013763, 4.947769141882245, 0.2649616407466674), (0.25, 0.4375, 0.33390385), "BP_Quarry_8x8x8_A_Breakable3_5", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4693.5063, 2074.1084, 988.04095), (3.415094155378522e-05, -91.56201164265767, 3.999996800403612e-06), (0.25, 0.4375, 0.25), "BP_Quarry_8x8x8_A_Breakable3_92", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4522.686, 3236.9434, 1293.9486), (-5.640741593515456, 90.11270400801293, 91.55869635634487), (0.874373, 0.25286, 0.874373), "PWM_Quarry_8x8x8_A11_56", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4677.4106, 4216.3213, 1288.645), (2.7840558008429093, 179.7019312760666, 83.12759769971102), (0.874373, 0.25286, 0.874373), "PWM_Quarry_8x8x8_A11_73", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4817.3145, 2667.4104, 1440.1758), (2.797933530497985, -89.88807913506882, 91.57514713526709), (0.874373, 0.25286, 0.874373), "PWM_Quarry_8x8x8_A11_1040", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4810.6826, 3302.8147, 1284.1763), (8.349237385292552, -90.1123632684203, -88.44658789547663), (0.874373, 0.248723, 0.874373), "PWM_Quarry_8x8x8_A12_69", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4610.81, 4501.1987, 1246.3864), (-0.07209312299547121, -0.12139484953236945, -79.99246894649288), (0.874373, 0.248723, 0.874373), "PWM_Quarry_8x8x8_A12_86", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4529.317, 2600.82, 1440.1758), (-0.08941701962761957, 89.88832647781291, -88.43002738776173), (0.874373, 0.248723, 0.874373), "PWM_Quarry_8x8x8_A12_1053", _folder)
if a: placed += 1
else: skipped += 1

# Batch 60: StaticMesh'PWM_Quarry_Floor_4x4x4_A' (4 instances)
_mesh_path = "/Game/Unshippable/Whitebox/Rocks/Meshes/PWM_Quarry_Floor_4x4x4_A"
_materials = ['/Game/Environments/ProcTexturing/ProcMaterial_Quarry_Atlas_4']
_folder = "Reconstruction/BD_BB_OrcPrison/Meshes"
a = spawn_static_mesh(_mesh_path, _materials, (3210.0, 5350.0, 983.05225), (0.0, 9.094430469077492, -0.0), (1.0, 1.0, 1.535339), "PWM_Quarry_Floor_4x4x4_A3", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2299.7605, 5366.4336, 983.05225), (0.0, -12.121734800485488, 0.0), (1.0, 1.0, 1.535339), "PWM_Quarry_Floor_4x4x4_A4", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2754.949, 5414.7236, 1392.084), (80.90547315500399, 89.99991964205203, 89.99991720352203), (1.0, 1.4172219, 1.6758583), "PWM_Quarry_Floor_4x4x4_A5", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2754.949, 5403.8857, 621.9031), (83.08885432036762, -89.99957412996211, -89.99951349144582), (1.0, 1.252497, 1.675858), "PWM_Quarry_Floor_4x4x4_A6", _folder)
if a: placed += 1
else: skipped += 1

# Batch 61: StaticMesh'PWM_Quarry_RockDebris_A_Optimized' (60 instances)
_mesh_path = "/Game/Unshippable/Whitebox/Rocks/Meshes/PWM_Quarry_RockDebris_A_Optimized"
_materials = ['/Game/Environments/ProcTexturing/ProcMaterial_Quarry_RockDebris_A']
_folder = "Reconstruction/BD_BB_OrcPrison/Meshes"
a = spawn_static_mesh(_mesh_path, _materials, (4025.0, 4516.0, 596.0), (0.0, 0.0, -0.0), (1.0, 1.0, 1.0), "BP_DM_PWM_Quarry_RockDebris_A_Breakable_2", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4450.0, 2271.0, 697.0), (0.0, 0.0, -0.0), (1.0, 1.0, 1.0), "BP_DM_PWM_Quarry_RockDebris_A_Breakable10", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3527.9275, 4034.0, 602.15826), (0.0, -44.99999866815529, 0.0), (0.8566222, 0.8566222, 0.8566222), "BP_DM_PWM_Quarry_RockDebris_A_Breakable11", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3482.265, 4390.1855, 602.86884), (0.0, -55.88024772282448, 0.0), (0.856622, 0.856622, 0.856622), "BP_DM_PWM_Quarry_RockDebris_A_Breakable13", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3417.8325, 3903.327, 602.1583), (0.0, 70.77006277470717, -0.0), (0.856622, 0.856622, 0.856622), "BP_DM_PWM_Quarry_RockDebris_A_Breakable14", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3810.4785, 4287.037, 597.5304), (-1.4402464257048155, -77.19936170188018, 1.1686453315073384e-06), (1.0, 1.0, 1.0), "BP_DM_PWM_Quarry_RockDebris_A_Breakable15", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4250.0, 3885.0, 598.0), (0.0, 0.0, -0.0), (1.0, 1.0, 1.0), "BP_DM_PWM_Quarry_RockDebris_A_Breakable2_5", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4983.0, 3177.0, 667.0), (0.0, 0.0, 5.000055930602136), (1.0, 1.0, 1.0), "BP_DM_PWM_Quarry_RockDebris_A_Breakable6", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4994.0, 2958.0, 688.0), (0.0, 0.0, 5.00000838895739), (1.0, 1.0, 1.0), "BP_DM_PWM_Quarry_RockDebris_A_Breakable7", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3898.0, 3947.0771, 597.53033), (-1.4404906894055467, 0.0, -0.0), (1.0, 1.0, 1.0), "BP_DM_PWM_Quarry_RockDebris_A_Breakable8_15", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3898.0, 4045.745, 597.53033), (-1.4404906894055467, 0.0, -0.0), (1.0, 1.0, 1.0), "BP_DM_PWM_Quarry_RockDebris_A_Breakable9", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4354.0, 3731.0, 597.0), (0.0, 0.0, -0.0), (1.0, 1.0, 1.0), "BP_DM_PWM_Quarry_RockDebris_C_Breakable_2", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4871.0, 3787.3477, 600.9696), (0.0, 0.0, 10.000066522997752), (1.0, 1.0, 1.0), "BP_DM_PWM_Quarry_RockDebris_C_Breakable2_5", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4500.0, 3376.169, 635.9021), (0.0, 0.0, 10.000066522997752), (1.0, 1.0, 1.0), "BP_DM_PWM_Quarry_RockDebris_C_Breakable3", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4238.712, 2277.0, 703.0), (0.0, 61.87506153955461, -0.0), (1.0, 1.0, 1.0), "PWM_Quarry_RockDebris_A_215", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2426.688, 2291.3489, 698.0), (0.0, -64.68756004716157, 0.0), (1.0, 1.0, 1.0), "PWM_Quarry_RockDebris_A10", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2699.0981, 2814.4214, 703.0), (0.0, -149.06260831355954, 0.0), (1.0, 1.0, 1.0), "PWM_Quarry_RockDebris_A12", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2500.6091, 2801.3354, 707.98553), (5.624995227396749, 126.56201518729327, 3.864910769955865e-06), (1.0, 1.0, 1.0), "PWM_Quarry_RockDebris_A13", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1954.3746, 2962.6365, 698.0), (0.0, 149.06228193649343, -0.0), (1.0, 1.0, 1.0), "PWM_Quarry_RockDebris_A14", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1741.0184, 2870.554, 698.0049), (6.147170018939039e-05, -47.80935851650011, 0.00012993808103349097), (1.0, 1.0, 1.0), "PWM_Quarry_RockDebris_A15", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1535.7087, 2909.0427, 706.3297), (2.8127195981473148, -123.74676202497989, 0.00013760741938328235), (1.0, 1.0, 1.0), "PWM_Quarry_RockDebris_A17", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1917.7147, 3348.1145, 714.9671), (-8.437315833614507, -177.18758516101195, 0.00011366957667574528), (1.0, 1.0, 1.0), "PWM_Quarry_RockDebris_A18", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1926.7196, 3166.6182, 715.77515), (1.5258635398902989, 101.70459798398609, 11.162353466165472), (1.0, 1.0, 1.0), "PWM_Quarry_RockDebris_A19", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1450.0629, 3432.5427, 714.99414), (6.147956022484554e-05, -143.43276460070743, 8.438385968808046), (1.0, 1.0, 1.0), "PWM_Quarry_RockDebris_A20", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4166.035, 2369.7192, 699.53033), (-1.4064636239055872, -44.86504828391898, 0.25727299220716804), (1.0, 1.0, 1.0), "PWM_Quarry_RockDebris_A21", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3973.1597, 2287.1748, 699.5303), (-1.4063721383575958, 74.27899763908245, 0.25727315046664695), (1.0, 1.0, 1.0), "PWM_Quarry_RockDebris_A22", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3973.1597, 2684.155, 702.45935), (-0.06774902931173743, 146.90868476056175, -0.6143187876965062), (1.0, 1.0, 1.0), "PWM_Quarry_RockDebris_A23_217", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4285.414, 2619.7876, 696.5477), (0.0, -118.0580731010508, 0.0), (1.0, 1.0, 1.0), "PWM_Quarry_RockDebris_A24", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2609.0981, 2679.4214, 703.0), (0.0, -96.04693038844333, 0.0), (1.0, 1.0, 1.0), "PWM_Quarry_RockDebris_A25", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2644.0981, 2259.4214, 703.0), (0.0, -29.562805495791277, 0.0), (1.0, 1.0, 1.0), "PWM_Quarry_RockDebris_A26", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2639.0981, 2464.4214, 703.53467), (0.0, -57.29806477650077, 0.0), (0.728058, 0.728058, 0.728058), "PWM_Quarry_RockDebris_A27", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2736.4214, 2109.7776, 703.0), (0.0, -29.562805495791277, 0.0), (1.0, 1.0, 1.0), "PWM_Quarry_RockDebris_A28_247", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4060.0, 2668.0, 701.0), (0.0, 120.93753907979632, -0.0), (1.0, 1.0, 1.0), "PWM_Quarry_RockDebris_A3", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1780.615, 2746.901, 701.33435), (0.0, -50.62524070549466, 0.0), (1.1829964, 1.1829964, 1.1829964), "PWM_Quarry_RockDebris_A31", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2152.9866, 2412.307, 695.9133), (0.0, -11.25030547691671, 0.0), (2.0, 2.0, 2.0), "PWM_Quarry_RockDebris_A32", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1873.1733, 3236.5188, 702.8786), (0.0, 26.413424581893587, -0.0), (0.7558336, 0.7558336, 0.7558336), "PWM_Quarry_RockDebris_A33", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1843.2323, 3236.5188, 702.87854), (0.0, 40.044668283635744, -0.0), (0.755834, 0.755834, 0.755834), "PWM_Quarry_RockDebris_A34", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2924.9866, 871.3069, 802.9133), (0.0, 113.43683595792334, -0.0), (1.0, 1.0, 1.0), "PWM_Quarry_RockDebris_A35", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3470.0244, 932.3049, 802.81256), (0.0, 127.46664078162478, -0.0), (1.0, 1.0, 1.0), "PWM_Quarry_RockDebris_A37", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4156.0, 2167.0, 701.0), (0.0, -95.62516613813719, 0.0), (1.0, 1.0, 1.0), "PWM_Quarry_RockDebris_A4", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3862.0, 2748.0, 701.0), (0.0, 120.93735927922133, -0.0), (1.0, 1.0, 1.0), "PWM_Quarry_RockDebris_A5", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1104.2987, 3677.41, 803.7024), (-0.6246337681512082, -142.18752607141934, 0.00013403457171673753), (1.0, 1.0, 1.0), "PWM_Quarry_RockDebris_A51", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (585.06287, 3682.5427, 802.99414), (0.0, -145.00008414946282, 0.0), (1.0, 1.0, 1.0), "PWM_Quarry_RockDebris_A52", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1086.1976, 2705.3445, 807.81445), (0.0032443227573317425, 44.835573069108825, 2.1371959188362535), (1.0, 1.0, 1.0), "PWM_Quarry_RockDebris_A54", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3687.9873, 439.3058, 803.9133), (0.0, 133.43676845194656, -0.0), (1.0, 1.0, 1.0), "PWM_Quarry_RockDebris_A57", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3458.9873, 561.3058, 803.9133), (0.0, -136.56315105323407, 0.0), (1.0, 1.0, 1.0), "PWM_Quarry_RockDebris_A59", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3857.0, 2111.0, 703.0), (0.0, 36.562426848181616, -0.0), (1.0, 1.0, 1.0), "PWM_Quarry_RockDebris_A6", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3769.9873, 237.30579, 802.9133), (0.0, -111.56311437143214, 0.0), (1.0, 1.0, 1.0), "PWM_Quarry_RockDebris_A60", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3538.9866, 1161.3069, 801.20984), (0.0, -69.2175821974179, 0.0), (1.0, 1.0, 1.0), "PWM_Quarry_RockDebris_A65", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2915.4736, 1498.5532, 803.2382), (0.0, -93.45651382929253, 0.0), (1.0, 1.0, 1.0), "PWM_Quarry_RockDebris_A69", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4597.0, 3035.0, 682.0), (-4.822662727962203, 121.05968922844832, -2.8986820182166184), (1.0, 1.0, 1.0), "PWM_Quarry_RockDebris_A7", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3573.429, 1503.1171, 801.6257), (0.0, -69.2175821974179, 0.0), (1.0, 1.0, 1.0), "PWM_Quarry_RockDebris_A70_797", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3477.2812, 1351.8982, 803.96893), (0.0, 121.18484878672781, -0.0), (1.0, 1.0, 0.6475236), "PWM_Quarry_RockDebris_A74", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2888.9775, 1223.5208, 803.8082), (0.0, -63.489066653521974, 0.0), (1.0, 1.0, 1.0), "PWM_Quarry_RockDebris_A75", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (544.06287, 2754.5427, 802.99414), (0.0, 10.000096064206778, -0.0), (1.0, 1.0, 1.0), "PWM_Quarry_RockDebris_A79", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2426.434, 2661.5713, 699.0), (0.0, -123.7500546001812, 0.0), (1.0, 1.0, 1.0), "PWM_Quarry_RockDebris_A8", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2463.0, 2474.0, 703.0), (0.0, 149.06228193649343, -0.0), (1.0, 1.0, 1.0), "PWM_Quarry_RockDebris_A9", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4515.0, 2829.0, 689.0), (0.0, 0.0, -0.0), (1.5, 1.5, 1.0), "PWM_Quarry_RockDebris_C_231", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5061.0, 2720.0, 689.0), (0.0, -143.43748317460413, 0.0), (1.5, 1.5, 1.0), "PWM_Quarry_RockDebris_C2", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4748.0, 2225.0, 689.0), (0.0, -143.43748317460413, 0.0), (1.5, 1.5, 1.0), "PWM_Quarry_RockDebris_C5", _folder)
if a: placed += 1
else: skipped += 1

# ======================================================================
# PHASE 2: ConstructionCatalog  (construction blocks)
# ======================================================================
unreal.log(f"[{BUBBLE_NAME}] Phase 2: Placing construction blocks...")

# Construction blocks use DecoVolume transforms (matched by Name)
_folder = "Reconstruction/BD_BB_OrcPrison/Construction"

# Construction: AB_Orc_Scaffolding_Balcony_C_2
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Wood
#   Volume: EMorSimpleShape::OrientedBox, BoxExtent: (77.8, 182.4, 168.8)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (2989.8713, 3444.9998, 892.1107), (0.0, 0.0, -0.0), (1.5552, 3.6488, 3.3760), "AB_Orc_Scaffolding_Balcony_C_2", _folder)
if a: placed += 1
else: skipped += 1

# Construction: AB_Orc_Scaffolding_Balcony_C2
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Wood
#   Volume: EMorSimpleShape::OrientedBox, BoxExtent: (77.8, 182.4, 168.8)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (3410.1287, 3454.9998, 892.1107), (0.0, 0.0, -0.0), (1.5552, 3.6488, 3.3760), "AB_Orc_Scaffolding_Balcony_C2", _folder)
if a: placed += 1
else: skipped += 1

# Construction: AB_Orc_Scaffolding_Platform_3x1_No_Legs_2
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Scaffolding
#   Volume: EMorSimpleShape::OrientedBox, BoxExtent: (77.8, 143.8, 87.6)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (3100.1287, 3157.4456, 643.15027), (0.0, 0.0, -0.0), (1.5552, 2.8751, 1.7522), "AB_Orc_Scaffolding_Platform_3x1_No_Legs_2", _folder)
if a: placed += 1
else: skipped += 1

# Construction: BP_Ruin_Wall_Thick_1x1m_B_Breakable_2
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Stone
#   Volume: EMorSimpleShape::OrientedBox, BoxExtent: (49.7, 52.4, 52.7)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (2851.9832, 5174.5063, 749.9584), (0.0, 0.0, -0.0), (0.9934, 1.0488, 1.0542), "BP_Ruin_Wall_Thick_1x1m_B_Breakable_2", _folder)
if a: placed += 1
else: skipped += 1

# Construction: BP_Ruin_Wall_Thick_1x1m_B_Breakable10_2
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Stone
#   Volume: EMorSimpleShape::OrientedBox, BoxExtent: (49.7, 52.4, 52.7)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (2848.0168, 1500.4937, 849.9584), (0.0, 0.0, -0.0), (0.9934, 1.0488, 1.0542), "BP_Ruin_Wall_Thick_1x1m_B_Breakable10_2", _folder)
if a: placed += 1
else: skipped += 1

# Construction: BP_Ruin_Wall_Thick_1x1m_B_Breakable11_11
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Stone
#   Volume: EMorSimpleShape::OrientedBox, BoxExtent: (49.7, 52.4, 52.7)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (3548.0168, 1450.4937, 1149.9584), (0.0, 0.0, -0.0), (0.9934, 1.0488, 1.0542), "BP_Ruin_Wall_Thick_1x1m_B_Breakable11_11", _folder)
if a: placed += 1
else: skipped += 1

# Construction: BP_Ruin_Wall_Thick_1x1m_B_Breakable2
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Stone
#   Volume: EMorSimpleShape::OrientedBox, BoxExtent: (52.4, 49.7, 52.7)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (2549.5063, 5173.017, 749.9584), (0.0, 0.0, -0.0), (1.0488, 0.9934, 1.0542), "BP_Ruin_Wall_Thick_1x1m_B_Breakable2", _folder)
if a: placed += 1
else: skipped += 1

# Construction: BP_Ruin_Wall_Thick_1x1m_B_Breakable6_8
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Stone
#   Volume: EMorSimpleShape::OrientedBox, BoxExtent: (52.4, 49.7, 52.7)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (2349.5063, 2173.0168, 849.9584), (0.0, 0.0, -0.0), (1.0488, 0.9934, 1.0542), "BP_Ruin_Wall_Thick_1x1m_B_Breakable6_8", _folder)
if a: placed += 1
else: skipped += 1

# Construction: BP_Ruin_Wall_Thick_1x1m_B_Breakable8_14
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Stone
#   Volume: EMorSimpleShape::OrientedBox, BoxExtent: (49.7, 52.4, 52.7)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (4048.017, 2750.4937, 749.9584), (0.0, 0.0, -0.0), (0.9934, 1.0488, 1.0542), "BP_Ruin_Wall_Thick_1x1m_B_Breakable8_14", _folder)
if a: placed += 1
else: skipped += 1

# Construction: BP_Ruin_Wall_Thick_1x1m_B_Breakable9_2
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Stone
#   Volume: EMorSimpleShape::OrientedBox, BoxExtent: (49.7, 52.4, 52.7)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (3548.0168, 4450.4937, 854.9584), (0.0, 0.0, -0.0), (0.9934, 1.0488, 1.0542), "BP_Ruin_Wall_Thick_1x1m_B_Breakable9_2", _folder)
if a: placed += 1
else: skipped += 1

# Construction: BP_Ruin_Wall_Thick_1x2m_B_Breakable3_8
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Stone
#   Volume: EMorSimpleShape::OrientedBox, BoxExtent: (53.1, 98.0, 49.3)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (2350.642, 2225.014, 747.7441), (0.0, 0.0, -0.0), (1.0624, 1.9599, 0.9852), "BP_Ruin_Wall_Thick_1x2m_B_Breakable3_8", _folder)
if a: placed += 1
else: skipped += 1

# Construction: BP_Ruin_Wall_Thick_1x2m_B_Breakable4_11
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Stone
#   Volume: EMorSimpleShape::OrientedBox, BoxExtent: (53.1, 98.0, 49.3)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (4049.358, 2200.014, 1352.256), (0.0, 0.0, -0.0), (1.0624, 1.9599, 0.9851), "BP_Ruin_Wall_Thick_1x2m_B_Breakable4_11", _folder)
if a: placed += 1
else: skipped += 1

# Construction: BP_Ruin_Wall_Thick_1x2m_B_Breakable5_5
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Stone
#   Volume: EMorSimpleShape::OrientedBox, BoxExtent: (53.1, 98.0, 49.3)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (2850.642, 1200.0137, 847.7441), (0.0, 0.0, -0.0), (1.0624, 1.9599, 0.9852), "BP_Ruin_Wall_Thick_1x2m_B_Breakable5_5", _folder)
if a: placed += 1
else: skipped += 1

# Construction: BP_Ruin_Wall_Thick_1x2m_C_Breakable_8
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Stone
#   Volume: EMorSimpleShape::OrientedBox, BoxExtent: (107.9, 47.6, 47.0)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (2700.7346, 5172.625, 1259.5549), (0.0, 0.0, -0.0), (2.1571, 0.9517, 0.9394), "BP_Ruin_Wall_Thick_1x2m_C_Breakable_8", _folder)
if a: placed += 1
else: skipped += 1

# Construction: BP_Ruin_Wall_Thick_1x2m_C_Breakable2
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Stone
#   Volume: EMorSimpleShape::OrientedBox, BoxExtent: (107.9, 47.6, 47.0)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (2899.2654, 5177.375, 1259.5549), (0.0, 0.0, -0.0), (2.1571, 0.9517, 0.9394), "BP_Ruin_Wall_Thick_1x2m_C_Breakable2", _folder)
if a: placed += 1
else: skipped += 1

# Construction: BP_Ruin_Wall_Thick_1x2m_C_Breakable3
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Stone
#   Volume: EMorSimpleShape::OrientedBox, BoxExtent: (107.9, 47.6, 47.0)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (2700.7346, 5177.375, 740.4451), (0.0, 0.0, -0.0), (2.1571, 0.9517, 0.9394), "BP_Ruin_Wall_Thick_1x2m_C_Breakable3", _folder)
if a: placed += 1
else: skipped += 1

# Construction: BP_Ruin_Wall_Thick_1x2m_C_Breakable5_7
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Stone
#   Volume: EMorSimpleShape::OrientedBox, BoxExtent: (47.6, 107.9, 47.0)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (4047.625, 2599.2654, 1359.5549), (0.0, 0.0, -0.0), (0.9517, 2.1571, 0.9394), "BP_Ruin_Wall_Thick_1x2m_C_Breakable5_7", _folder)
if a: placed += 1
else: skipped += 1

# Construction: BP_Ruin_Wall_Thick_1x3m_C_Breakable_2
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Stone
#   Volume: EMorSimpleShape::OrientedBox, BoxExtent: (51.2, 150.1, 50.0)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (3548.7102, 4350.0, 643.4293), (0.0, 0.0, -0.0), (1.0250, 3.0018, 0.9991), "BP_Ruin_Wall_Thick_1x3m_C_Breakable_2", _folder)
if a: placed += 1
else: skipped += 1

# Construction: BP_Ruin_Wall_Thick_1x3m_C_Breakable2
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Stone
#   Volume: EMorSimpleShape::OrientedBox, BoxExtent: (51.2, 150.1, 50.0)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (3561.2898, 4060.0, 643.4293), (0.0, 0.0, -0.0), (1.0250, 3.0018, 0.9991), "BP_Ruin_Wall_Thick_1x3m_C_Breakable2", _folder)
if a: placed += 1
else: skipped += 1

# Construction: BP_Ruin_Wall_Thick_3x1m_A_2
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Stone
#   Volume: EMorSimpleShape::OrientedBox, BoxExtent: (51.7, 50.9, 152.1)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (1313.9961, 5049.9785, 850.2669), (0.0, 0.0, -0.0), (1.0339, 1.0178, 3.0420), "BP_Ruin_Wall_Thick_3x1m_A_2", _folder)
if a: placed += 1
else: skipped += 1

# Construction: BP_Ruin_Wall_Thick_3x1m_A2_2
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Stone
#   Volume: EMorSimpleShape::OrientedBox, BoxExtent: (50.9, 51.7, 152.1)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (2349.9783, 2076.004, 850.2669), (0.0, 0.0, -0.0), (1.0178, 1.0339, 3.0420), "BP_Ruin_Wall_Thick_3x1m_A2_2", _folder)
if a: placed += 1
else: skipped += 1

# Construction: BP_Ruin_Wall_Thick_3x1m_A3_5
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Stone
#   Volume: EMorSimpleShape::OrientedBox, BoxExtent: (51.7, 50.9, 152.1)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (3548.996, 1449.9784, 950.2669), (0.0, 0.0, -0.0), (1.0339, 1.0178, 3.0420), "BP_Ruin_Wall_Thick_3x1m_A3_5", _folder)
if a: placed += 1
else: skipped += 1

# Construction: BP_Ruin_Wall_Thick_3x1m_B_Breakable_5
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Stone
#   Volume: EMorSimpleShape::OrientedBox, BoxExtent: (50.9, 51.7, 150.2)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (1315.0, 4952.241, 848.4018), (0.0, 0.0, -0.0), (1.0178, 1.0339, 3.0047), "BP_Ruin_Wall_Thick_3x1m_B_Breakable_5", _folder)
if a: placed += 1
else: skipped += 1

# Construction: BP_Ruin_Wall_Thick_3x1m_B_Breakable10_2
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Stone
#   Volume: EMorSimpleShape::OrientedBox, BoxExtent: (51.7, 50.9, 150.2)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (3547.7585, 3975.0, 808.4018), (0.0, 0.0, -0.0), (1.0339, 1.0178, 3.0047), "BP_Ruin_Wall_Thick_3x1m_B_Breakable10_2", _folder)
if a: placed += 1
else: skipped += 1

# Construction: BP_Ruin_Wall_Thick_3x1m_B_Breakable12_5
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Stone
#   Volume: EMorSimpleShape::OrientedBox, BoxExtent: (50.9, 51.7, 150.2)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (2850.0, 1502.2415, 1048.4019), (0.0, 0.0, -0.0), (1.0178, 1.0339, 3.0047), "BP_Ruin_Wall_Thick_3x1m_B_Breakable12_5", _folder)
if a: placed += 1
else: skipped += 1

# Construction: BP_Ruin_Wall_Thick_3x1m_B_Breakable2
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Stone
#   Volume: EMorSimpleShape::OrientedBox, BoxExtent: (50.9, 51.7, 150.2)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (1315.0, 4577.759, 848.4018), (0.0, 0.0, -0.0), (1.0178, 1.0339, 3.0047), "BP_Ruin_Wall_Thick_3x1m_B_Breakable2", _folder)
if a: placed += 1
else: skipped += 1

# Construction: BP_Ruin_Wall_Thick_3x1m_B_Breakable3_2
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Stone
#   Volume: EMorSimpleShape::OrientedBox, BoxExtent: (51.7, 50.9, 150.2)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (3052.2415, 5175.0, 848.4018), (0.0, 0.0, -0.0), (1.0339, 1.0178, 3.0047), "BP_Ruin_Wall_Thick_3x1m_B_Breakable3_2", _folder)
if a: placed += 1
else: skipped += 1

# Construction: BP_Ruin_Wall_Thick_3x1m_B_Breakable4_8
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Stone
#   Volume: EMorSimpleShape::OrientedBox, BoxExtent: (51.7, 50.9, 150.2)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (2447.7585, 5175.0, 1151.5981), (0.0, 0.0, -0.0), (1.0339, 1.0178, 3.0047), "BP_Ruin_Wall_Thick_3x1m_B_Breakable4_8", _folder)
if a: placed += 1
else: skipped += 1

# Construction: BP_Ruin_Wall_Thick_3x1m_B_Breakable5
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Stone
#   Volume: EMorSimpleShape::OrientedBox, BoxExtent: (50.9, 51.7, 150.2)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (3050.0, 5177.241, 1151.5983), (0.0, 0.0, -0.0), (1.0178, 1.0339, 3.0047), "BP_Ruin_Wall_Thick_3x1m_B_Breakable5", _folder)
if a: placed += 1
else: skipped += 1

# Construction: BP_Ruin_Wall_Thick_3x1m_B_Breakable6
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Stone
#   Volume: EMorSimpleShape::OrientedBox, BoxExtent: (51.7, 50.9, 150.2)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (2447.7585, 5175.0, 848.4018), (0.0, 0.0, -0.0), (1.0339, 1.0178, 3.0047), "BP_Ruin_Wall_Thick_3x1m_B_Breakable6", _folder)
if a: placed += 1
else: skipped += 1

# Construction: BP_Ruin_Wall_Thick_3x1m_B_Breakable8_7
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Stone
#   Volume: EMorSimpleShape::OrientedBox, BoxExtent: (50.9, 51.7, 150.2)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (2350.0, 2797.2415, 848.4018), (0.0, 0.0, -0.0), (1.0178, 1.0339, 3.0047), "BP_Ruin_Wall_Thick_3x1m_B_Breakable8_7", _folder)
if a: placed += 1
else: skipped += 1

# Construction: BP_Ruin_Wall_Thick_3x1m_B_Breakable9_10
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Stone
#   Volume: EMorSimpleShape::OrientedBox, BoxExtent: (50.9, 51.7, 150.2)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (4050.0, 2752.2415, 1251.5983), (0.0, 0.0, -0.0), (1.0178, 1.0339, 3.0047), "BP_Ruin_Wall_Thick_3x1m_B_Breakable9_10", _folder)
if a: placed += 1
else: skipped += 1

# Construction: BP_Ruin_Wall_Thick_3x1m_C_Breakable_2
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Stone
#   Volume: EMorSimpleShape::OrientedBox, BoxExtent: (49.2, 51.7, 95.8)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (2950.0, 5172.759, 793.95264), (0.0, 0.0, -0.0), (0.9840, 1.0339, 1.9157), "BP_Ruin_Wall_Thick_3x1m_C_Breakable_2", _folder)
if a: placed += 1
else: skipped += 1

# Construction: BP_Ruin_Wall_Thick_3x1m_C_Breakable2_5
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Stone
#   Volume: EMorSimpleShape::OrientedBox, BoxExtent: (49.2, 51.7, 95.8)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (2550.0, 5172.759, 1206.0474), (0.0, 0.0, -0.0), (0.9840, 1.0339, 1.9157), "BP_Ruin_Wall_Thick_3x1m_C_Breakable2_5", _folder)
if a: placed += 1
else: skipped += 1

# Construction: BP_Ruin_Wall_Thick_3x1m_C_Breakable3_2
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Stone
#   Volume: EMorSimpleShape::OrientedBox, BoxExtent: (51.7, 49.2, 95.8)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (3552.2415, 3850.0, 1106.0475), (0.0, 0.0, -0.0), (1.0339, 0.9840, 1.9157), "BP_Ruin_Wall_Thick_3x1m_C_Breakable3_2", _folder)
if a: placed += 1
else: skipped += 1

# Construction: BP_Ruin_Wall_Thick_3x1m_C_Breakable6_12
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Stone
#   Volume: EMorSimpleShape::OrientedBox, BoxExtent: (51.7, 49.2, 95.8)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (4047.7585, 2150.0, 793.95264), (0.0, 0.0, -0.0), (1.0339, 0.9840, 1.9157), "BP_Ruin_Wall_Thick_3x1m_C_Breakable6_12", _folder)
if a: placed += 1
else: skipped += 1

# Construction: BP_Ruin_Wall_Thick_3x1m_C_Breakable8_2
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Stone
#   Volume: EMorSimpleShape::OrientedBox, BoxExtent: (51.7, 49.2, 95.8)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (3552.2415, 4450.0, 743.95264), (0.0, 0.0, -0.0), (1.0339, 0.9840, 1.9157), "BP_Ruin_Wall_Thick_3x1m_C_Breakable8_2", _folder)
if a: placed += 1
else: skipped += 1

# Construction: BP_Ruin_Wall_Thick_3x3m_C_Breakable_8
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Stone
#   Volume: EMorSimpleShape::OrientedBox, BoxExtent: (153.0, 52.1, 150.2)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (1610.7224, 2760.0, 847.7528), (0.0, 0.0, -0.0), (3.0591, 1.0424, 3.0045), "BP_Ruin_Wall_Thick_3x3m_C_Breakable_8", _folder)
if a: placed += 1
else: skipped += 1

# Construction: BP_Ruin_Wall_Thick_3x3m_C_Breakable2_11
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Stone
#   Volume: EMorSimpleShape::OrientedBox, BoxExtent: (52.1, 153.0, 150.2)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (2350.0, 2721.1345, 1172.2473), (0.0, 0.0, -0.0), (1.0424, 3.0591, 3.0045), "BP_Ruin_Wall_Thick_3x3m_C_Breakable2_11", _folder)
if a: placed += 1
else: skipped += 1

# Construction: BP_Ruin_Wall_Thick_3x3m_C_Breakable3_2
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Stone
#   Volume: EMorSimpleShape::OrientedBox, BoxExtent: (52.1, 153.0, 150.2)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (3550.0, 4361.135, 1052.2472), (0.0, 0.0, -0.0), (1.0424, 3.0591, 3.0045), "BP_Ruin_Wall_Thick_3x3m_C_Breakable3_2", _folder)
if a: placed += 1
else: skipped += 1

# Construction: BP_Ruin_Wall_Thick_3x3m_C_Breakable4
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Stone
#   Volume: EMorSimpleShape::OrientedBox, BoxExtent: (52.1, 153.0, 150.2)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (3550.0, 4068.8652, 1052.2472), (0.0, 0.0, -0.0), (1.0424, 3.0591, 3.0045), "BP_Ruin_Wall_Thick_3x3m_C_Breakable4", _folder)
if a: placed += 1
else: skipped += 1

# Construction: BP_Ruin_Wall_Thick_Corner_A_3_Breakable_2
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Stone
#   Volume: EMorSimpleShape::OrientedBox, BoxExtent: (110.5, 113.3, 52.7)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (2502.753, 2770.7583, 744.881), (0.0, 0.0, -0.0), (2.2091, 2.2654, 1.0548), "BP_Ruin_Wall_Thick_Corner_A_3_Breakable_2", _folder)
if a: placed += 1
else: skipped += 1

# Construction: BP_Ruin_Wall_Thin_3x1m_B_Breakable_2
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Stone
#   Volume: EMorSimpleShape::OrientedBox, BoxExtent: (50.7, 26.5, 115.6)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (1315.0, 4650.8237, 813.7234), (0.0, 0.0, -0.0), (1.0145, 0.5291, 2.3111), "BP_Ruin_Wall_Thin_3x1m_B_Breakable_2", _folder)
if a: placed += 1
else: skipped += 1

# Construction: BP_Ruin_Wall_Thin_3x1m_C_Breakable_2
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Stone
#   Volume: EMorSimpleShape::OrientedBox, BoxExtent: (50.7, 26.5, 98.0)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (1315.0, 4875.8237, 796.1446), (0.0, 0.0, -0.0), (1.0135, 0.5291, 1.9596), "BP_Ruin_Wall_Thin_3x1m_C_Breakable_2", _folder)
if a: placed += 1
else: skipped += 1

# Construction: BP_Ruin_Wall_Thin_3x1m_C_Breakable2_2
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Stone
#   Volume: EMorSimpleShape::OrientedBox, BoxExtent: (26.5, 50.7, 98.0)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (4028.8237, 2753.0, 897.1446), (0.0, 0.0, -0.0), (0.5291, 1.0135, 1.9596), "BP_Ruin_Wall_Thin_3x1m_C_Breakable2_2", _folder)
if a: placed += 1
else: skipped += 1

# Construction: BP_Suburbs_Wall_Thick_1x2m_A_Breakable5_2
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Stone
#   Volume: EMorSimpleShape::OrientedBox, BoxExtent: (50.0, 100.0, 50.0)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (3550.0, 4200.0, 1249.4686), (0.0, 0.0, -0.0), (1.0000, 2.0000, 1.0000), "BP_Suburbs_Wall_Thick_1x2m_A_Breakable5_2", _folder)
if a: placed += 1
else: skipped += 1

# Construction: BP_Suburbs_Wall_Thick_1x2m_A_Breakable6_1
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Stone
#   Volume: EMorSimpleShape::OrientedBox, BoxExtent: (50.0, 100.0, 50.0)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (3550.0, 4400.0, 1249.4686), (0.0, 0.0, -0.0), (1.0000, 2.0000, 1.0000), "BP_Suburbs_Wall_Thick_1x2m_A_Breakable6_1", _folder)
if a: placed += 1
else: skipped += 1

# Construction: BP_Suburbs_Wall_Thick_1x2m_A_Breakable7
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Stone
#   Volume: EMorSimpleShape::OrientedBox, BoxExtent: (50.0, 100.0, 50.0)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (3550.0, 4000.0, 1249.4686), (0.0, 0.0, -0.0), (1.0000, 2.0000, 1.0000), "BP_Suburbs_Wall_Thick_1x2m_A_Breakable7", _folder)
if a: placed += 1
else: skipped += 1

# Construction: BP_Suburbs_Wall_Thin_Arch_B_1m_5
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Stone
#   Volume: EMorSimpleShape::OrientedBox, BoxExtent: (25.0, 25.8, 50.3)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (1950.0, 4225.78, 649.7254), (0.0, 0.0, -0.0), (0.5000, 0.5156, 1.0055), "BP_Suburbs_Wall_Thin_Arch_B_1m_5", _folder)
if a: placed += 1
else: skipped += 1

# Construction: BP_Suburbs_WallPanel_Wood_010x300x300_C_Breakable_2
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Stone
#   Volume: EMorSimpleShape::OrientedBox, BoxExtent: (150.0, 150.0, 6.3)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (2749.999, 4350.0, 1443.7362), (0.0, 0.0, -0.0), (3.0003, 2.9997, 0.1253), "BP_Suburbs_WallPanel_Wood_010x300x300_C_Breakable_2", _folder)
if a: placed += 1
else: skipped += 1

# Construction: BP_Wooden_Ceiling_Support_4m_C2
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Advanced_Column
#   Volume: EMorSimpleShape::OrientedBox, BoxExtent: (20.0, 20.0, 200.0)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (2346.0356, 5042.2397, 623.50665), (-45.69707325802988, 104.04474869067688, 91.36465275081514), (0.4000, 0.4000, 4.0000), "BP_Wooden_Ceiling_Support_4m_C2", _folder)
if a: placed += 1
else: skipped += 1

# Construction: BP_Wooden_Ceiling_Support_4m_C3
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Advanced_Column
#   Volume: EMorSimpleShape::OrientedBox, BoxExtent: (20.0, 20.0, 200.0)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (3129.168, 5011.742, 624.15027), (-40.67950437385796, -109.78188670360109, 93.37725004227909), (0.4000, 0.4000, 4.0000), "BP_Wooden_Ceiling_Support_4m_C3", _folder)
if a: placed += 1
else: skipped += 1

# Construction: BP_Wooden_Ceiling_Support_6M_A_2
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Advanced_Column
#   Volume: EMorSimpleShape::OrientedBox, BoxExtent: (34.5, 150.0, 343.6)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (2900.0, 3760.0, 943.58264), (0.0, 0.0, -0.0), (0.6898, 3.0000, 6.8717), "BP_Wooden_Ceiling_Support_6M_A_2", _folder)
if a: placed += 1
else: skipped += 1

# Construction: BP_Wooden_Ceiling_Support_6M_A10
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Advanced_Column
#   Volume: EMorSimpleShape::OrientedBox, BoxExtent: (150.0, 34.5, 343.6)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (3365.0, 4530.0, 948.58264), (0.0, 0.0, -0.0), (3.0000, 0.6898, 6.8717), "BP_Wooden_Ceiling_Support_6M_A10", _folder)
if a: placed += 1
else: skipped += 1

# Construction: BP_Wooden_Ceiling_Support_6M_A11
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Advanced_Column
#   Volume: EMorSimpleShape::OrientedBox, BoxExtent: (150.0, 34.5, 343.6)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (3365.0, 3905.0, 948.58264), (0.0, 0.0, -0.0), (3.0000, 0.6898, 6.8717), "BP_Wooden_Ceiling_Support_6M_A11", _folder)
if a: placed += 1
else: skipped += 1

# Construction: BP_Wooden_Ceiling_Support_6M_A12
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Advanced_Column
#   Volume: EMorSimpleShape::OrientedBox, BoxExtent: (150.0, 34.5, 343.6)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (3355.0, 3605.0, 948.58264), (0.0, 0.0, -0.0), (3.0000, 0.6898, 6.8717), "BP_Wooden_Ceiling_Support_6M_A12", _folder)
if a: placed += 1
else: skipped += 1

# Construction: BP_Wooden_Ceiling_Support_6M_A13
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Advanced_Column
#   Volume: EMorSimpleShape::OrientedBox, BoxExtent: (150.0, 34.5, 343.6)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (3355.0, 3305.0, 948.58264), (0.0, 0.0, -0.0), (3.0000, 0.6898, 6.8717), "BP_Wooden_Ceiling_Support_6M_A13", _folder)
if a: placed += 1
else: skipped += 1

# Construction: BP_Wooden_Ceiling_Support_6M_A14
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Advanced_Column
#   Volume: EMorSimpleShape::OrientedBox, BoxExtent: (150.0, 34.5, 343.6)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (3050.0, 3300.0, 943.58264), (0.0, 0.0, -0.0), (3.0000, 0.6898, 6.8717), "BP_Wooden_Ceiling_Support_6M_A14", _folder)
if a: placed += 1
else: skipped += 1

# Construction: BP_Wooden_Ceiling_Support_6M_A2_20
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Advanced_Column
#   Volume: EMorSimpleShape::OrientedBox, BoxExtent: (150.0, 34.5, 343.6)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (3050.0, 3595.0, 943.58264), (0.0, 0.0, -0.0), (3.0000, 0.6898, 6.8717), "BP_Wooden_Ceiling_Support_6M_A2_20", _folder)
if a: placed += 1
else: skipped += 1

# Construction: BP_Wooden_Ceiling_Support_6M_A3_2
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Advanced_Column
#   Volume: EMorSimpleShape::OrientedBox, BoxExtent: (34.5, 150.0, 343.6)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (2300.0, 3770.0, 948.58264), (0.0, 0.0, -0.0), (0.6898, 3.0000, 6.8717), "BP_Wooden_Ceiling_Support_6M_A3_2", _folder)
if a: placed += 1
else: skipped += 1

# Construction: BP_Wooden_Ceiling_Support_6M_A4
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Advanced_Column
#   Volume: EMorSimpleShape::OrientedBox, BoxExtent: (34.5, 150.0, 343.6)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (2600.0, 3770.0, 948.58264), (0.0, 0.0, -0.0), (0.6898, 3.0000, 6.8717), "BP_Wooden_Ceiling_Support_6M_A4", _folder)
if a: placed += 1
else: skipped += 1

# Construction: BP_Wooden_Ceiling_Support_6M_A5
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Advanced_Column
#   Volume: EMorSimpleShape::OrientedBox, BoxExtent: (150.0, 34.5, 343.6)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (2140.0, 3920.0, 948.58264), (0.0, 0.0, -0.0), (3.0000, 0.6898, 6.8717), "BP_Wooden_Ceiling_Support_6M_A5", _folder)
if a: placed += 1
else: skipped += 1

# Construction: BP_Wooden_Ceiling_Support_6M_A6
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Advanced_Column
#   Volume: EMorSimpleShape::OrientedBox, BoxExtent: (150.0, 34.5, 343.6)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (2140.0, 4220.0, 948.58264), (0.0, 0.0, -0.0), (3.0000, 0.6898, 6.8717), "BP_Wooden_Ceiling_Support_6M_A6", _folder)
if a: placed += 1
else: skipped += 1

# Construction: BP_Wooden_Ceiling_Support_6M_A7
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Advanced_Column
#   Volume: EMorSimpleShape::OrientedBox, BoxExtent: (150.0, 34.5, 343.6)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (2140.0, 4530.0, 948.58264), (0.0, 0.0, -0.0), (3.0000, 0.6898, 6.8717), "BP_Wooden_Ceiling_Support_6M_A7", _folder)
if a: placed += 1
else: skipped += 1

# Construction: BP_Wooden_Ceiling_Support_6M_A8
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Advanced_Column
#   Volume: EMorSimpleShape::OrientedBox, BoxExtent: (150.0, 34.5, 343.6)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (2140.0, 4820.0, 948.58264), (0.0, 0.0, -0.0), (3.0000, 0.6898, 6.8717), "BP_Wooden_Ceiling_Support_6M_A8", _folder)
if a: placed += 1
else: skipped += 1

# Construction: BP_Wooden_Ceiling_Support_6M_A9
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Advanced_Column
#   Volume: EMorSimpleShape::OrientedBox, BoxExtent: (150.0, 34.5, 343.6)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (3365.0, 4820.0, 948.58264), (0.0, 0.0, -0.0), (3.0000, 0.6898, 6.8717), "BP_Wooden_Ceiling_Support_6M_A9", _folder)
if a: placed += 1
else: skipped += 1

# Construction: BP_Wooden_Ceiling_Support_6M_B_2
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Advanced_Column
#   Volume: EMorSimpleShape::OrientedBox, BoxExtent: (150.0, 151.2, 343.6)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (2145.0, 4963.245, 945.58264), (0.0, 0.0, -0.0), (3.0000, 3.0249, 6.8717), "BP_Wooden_Ceiling_Support_6M_B_2", _folder)
if a: placed += 1
else: skipped += 1

# Construction: BP_Wooden_Ceiling_Support_6M_B2
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Advanced_Column
#   Volume: EMorSimpleShape::OrientedBox, BoxExtent: (151.2, 150.0, 343.6)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (2151.755, 3785.0, 945.58264), (0.0, 0.0, -0.0), (3.0249, 3.0000, 6.8717), "BP_Wooden_Ceiling_Support_6M_B2", _folder)
if a: placed += 1
else: skipped += 1

# Construction: BP_Wooden_Ceiling_Support_6M_B3_13
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Advanced_Column
#   Volume: EMorSimpleShape::OrientedBox, BoxExtent: (151.2, 150.0, 343.6)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (3348.245, 4980.0, 948.58264), (0.0, 0.0, -0.0), (3.0249, 3.0000, 6.8717), "BP_Wooden_Ceiling_Support_6M_B3_13", _folder)
if a: placed += 1
else: skipped += 1

# Construction: BP_Wooden_Ceiling_Support_6M_E15_22
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Advanced_Column
#   Volume: EMorSimpleShape::OrientedBox, BoxExtent: (34.5, 150.0, 343.6)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (2290.0, 4980.0, 948.58264), (0.0, 0.0, -0.0), (0.6898, 3.0000, 6.8717), "BP_Wooden_Ceiling_Support_6M_E15_22", _folder)
if a: placed += 1
else: skipped += 1

# Construction: BP_Wooden_Ceiling_Support_6M_E16_13
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Advanced_Column
#   Volume: EMorSimpleShape::OrientedBox, BoxExtent: (34.5, 150.0, 343.6)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (3195.0, 4980.0, 948.58264), (0.0, 0.0, -0.0), (0.6898, 3.0000, 6.8717), "BP_Wooden_Ceiling_Support_6M_E16_13", _folder)
if a: placed += 1
else: skipped += 1

# Construction: Orc_Palissade_Gate_B_2
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Wood
#   Volume: EMorSimpleShape::OrientedBox, BoxExtent: (284.3, 40.5, 265.3)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (3194.3267, 2904.0046, 957.73334), (0.0, 0.0, -0.0), (5.6870, 0.8106, 5.3064), "Orc_Palissade_Gate_B_2", _folder)
if a: placed += 1
else: skipped += 1

# Construction: Orc_Palissade_Gate_B2_8
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Wood
#   Volume: EMorSimpleShape::OrientedBox, BoxExtent: (40.5, 284.3, 265.3)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (1154.0048, 3175.6733, 1032.7334), (0.0, 0.0, -0.0), (0.8106, 5.6870, 5.3064), "Orc_Palissade_Gate_B2_8", _folder)
if a: placed += 1
else: skipped += 1

# Construction: Orc_Palissade_Gate_C_2
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Wood
#   Volume: EMorSimpleShape::OrientedBox, BoxExtent: (66.6, 146.1, 261.1)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (3509.4885, 2530.505, 965.0), (0.0, 0.0, -0.0), (1.3324, 2.9219, 5.2224), "Orc_Palissade_Gate_C_2", _folder)
if a: placed += 1
else: skipped += 1

# Construction: Orc_Palissade_Gate_C2_5
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Wood
#   Volume: EMorSimpleShape::OrientedBox, BoxExtent: (35.7, 141.7, 261.1)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (1325.0, 3086.2275, 985.0), (0.0, 0.0, -0.0), (0.7138, 2.8340, 5.2224), "Orc_Palissade_Gate_C2_5", _folder)
if a: placed += 1
else: skipped += 1

# Construction: Orc_Palissade_Gate_D_2
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Wood
#   Volume: EMorSimpleShape::OrientedBox, BoxExtent: (40.5, 190.7, 265.0)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (3527.1746, 2366.4993, 951.77466), (0.0, 0.0, -0.0), (0.8106, 3.8139, 5.2993), "Orc_Palissade_Gate_D_2", _folder)
if a: placed += 1
else: skipped += 1

# Construction: Orc_Palissade_Gate_D2_5
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Wood
#   Volume: EMorSimpleShape::OrientedBox, BoxExtent: (40.5, 190.7, 265.0)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (1319.9999, 3307.6008, 961.77466), (0.0, 0.0, -0.0), (0.8106, 3.8139, 5.2993), "Orc_Palissade_Gate_D2_5", _folder)
if a: placed += 1
else: skipped += 1

# Construction: Orc_Palissade_Gate_E_R_2
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Wood
#   Volume: EMorSimpleShape::OrientedBox, BoxExtent: (24.6, 94.3, 171.0)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (3515.124, 2161.6204, 872.5925), (0.0, 0.0, -0.0), (0.4925, 1.8858, 3.4204), "Orc_Palissade_Gate_E_R_2", _folder)
if a: placed += 1
else: skipped += 1

# Construction: Orc_Palissade_Gate_E_R2
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Wood
#   Volume: EMorSimpleShape::OrientedBox, BoxExtent: (24.6, 94.3, 171.0)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (3524.8762, 2738.3796, 872.5925), (0.0, 0.0, -0.0), (0.4925, 1.8858, 3.4204), "Orc_Palissade_Gate_E_R2", _folder)
if a: placed += 1
else: skipped += 1

# Construction: Orc_Palissade_Gate_E_R3
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Wood
#   Volume: EMorSimpleShape::OrientedBox, BoxExtent: (24.6, 94.3, 171.0)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (2945.124, 2196.6204, 872.5925), (0.0, 0.0, -0.0), (0.4925, 1.8858, 3.4204), "Orc_Palissade_Gate_E_R3", _folder)
if a: placed += 1
else: skipped += 1

# Construction: Orc_Palissade_Gate_E_R4
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Wood
#   Volume: EMorSimpleShape::OrientedBox, BoxExtent: (24.6, 94.3, 171.0)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (2944.8762, 2688.3796, 872.5925), (0.0, 0.0, -0.0), (0.4925, 1.8858, 3.4204), "Orc_Palissade_Gate_E_R4", _folder)
if a: placed += 1
else: skipped += 1

# Construction: Orc_Palissade_Post_A_2
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Wood
#   Volume: EMorSimpleShape::OrientedBox, BoxExtent: (131.2, 109.1, 200.4)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (1431.7837, 2929.2764, 881.0622), (0.0, 0.0, -0.0), (2.6237, 2.1827, 4.0088), "Orc_Palissade_Post_A_2", _folder)
if a: placed += 1
else: skipped += 1

# Construction: Orc_Palissade_Post_A2
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Wood
#   Volume: EMorSimpleShape::OrientedBox, BoxExtent: (131.2, 109.1, 200.4)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (1428.9656, 3433.5845, 882.5277), (0.0, 0.0, -0.0), (2.6237, 2.1827, 4.0088), "Orc_Palissade_Post_A2", _folder)
if a: placed += 1
else: skipped += 1

# Construction: Orc_Palissade_Wall_3X1M_A_8
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Scaffolding
#   Volume: EMorSimpleShape::OrientedBox, BoxExtent: (178.9, 149.8, 109.1)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (1754.6815, 3404.8352, 714.9049), (0.0, 0.0, -0.0), (3.5774, 2.9958, 2.1829), "Orc_Palissade_Wall_3X1M_A_8", _folder)
if a: placed += 1
else: skipped += 1

# Construction: Orc_Scaffolding_Post_Deco_D_2
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Scaffolding
#   Volume: EMorSimpleShape::OrientedBox, BoxExtent: (29.3, 109.0, 94.0)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (2949.8115, 2507.8193, 962.5482), (0.0, 0.0, -0.0), (0.5868, 2.1801, 1.8793), "Orc_Scaffolding_Post_Deco_D_2", _folder)
if a: placed += 1
else: skipped += 1

# Construction: Orc_Scaffolding_Post_Deco_D10
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Scaffolding
#   Volume: EMorSimpleShape::OrientedBox, BoxExtent: (29.3, 109.0, 94.0)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (2044.9675, 4706.8975, 939.62756), (0.0, 0.0, -0.0), (0.5869, 2.1801, 1.8793), "Orc_Scaffolding_Post_Deco_D10", _folder)
if a: placed += 1
else: skipped += 1

# Construction: Orc_Scaffolding_Post_Deco_D2
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Scaffolding
#   Volume: EMorSimpleShape::OrientedBox, BoxExtent: (29.3, 109.0, 94.0)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (2940.1885, 2382.1807, 962.5482), (0.0, 0.0, -0.0), (0.5869, 2.1801, 1.8793), "Orc_Scaffolding_Post_Deco_D2", _folder)
if a: placed += 1
else: skipped += 1

# Construction: Orc_Scaffolding_Post_Deco_D3_6
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Scaffolding
#   Volume: EMorSimpleShape::OrientedBox, BoxExtent: (29.3, 109.0, 94.0)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (3449.7869, 4628.806, 945.5867), (0.0, 0.0, -0.0), (0.5868, 2.1801, 1.8793), "Orc_Scaffolding_Post_Deco_D3_6", _folder)
if a: placed += 1
else: skipped += 1

# Construction: Orc_Scaffolding_Post_Deco_D4
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Scaffolding
#   Volume: EMorSimpleShape::OrientedBox, BoxExtent: (29.3, 109.0, 94.0)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (3464.41, 4704.445, 945.5867), (0.0, 0.0, -0.0), (0.5869, 2.1801, 1.8793), "Orc_Scaffolding_Post_Deco_D4", _folder)
if a: placed += 1
else: skipped += 1

# Construction: Orc_Scaffolding_Post_Deco_D5_12
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Scaffolding
#   Volume: EMorSimpleShape::OrientedBox, BoxExtent: (29.3, 109.0, 94.0)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (3456.0715, 4930.453, 949.30554), (0.0, 0.0, -0.0), (0.5868, 2.1801, 1.8793), "Orc_Scaffolding_Post_Deco_D5_12", _folder)
if a: placed += 1
else: skipped += 1

# Construction: Orc_Scaffolding_Post_Deco_D6_13
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Scaffolding
#   Volume: EMorSimpleShape::OrientedBox, BoxExtent: (29.3, 109.0, 94.0)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (3470.6946, 4961.092, 946.88007), (0.0, 0.0, -0.0), (0.5869, 2.1801, 1.8793), "Orc_Scaffolding_Post_Deco_D6_13", _folder)
if a: placed += 1
else: skipped += 1

# Construction: Orc_Scaffolding_Post_Deco_D7
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Scaffolding
#   Volume: EMorSimpleShape::OrientedBox, BoxExtent: (29.3, 109.0, 94.0)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (2023.3368, 4924.198, 950.32556), (0.0, 0.0, -0.0), (0.5868, 2.1801, 1.8793), "Orc_Scaffolding_Post_Deco_D7", _folder)
if a: placed += 1
else: skipped += 1

# Construction: Orc_Scaffolding_Post_Deco_D8
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Scaffolding
#   Volume: EMorSimpleShape::OrientedBox, BoxExtent: (29.3, 109.0, 94.0)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (2037.9597, 4979.62, 942.5482), (0.0, 0.0, -0.0), (0.5869, 2.1801, 1.8793), "Orc_Scaffolding_Post_Deco_D8", _folder)
if a: placed += 1
else: skipped += 1

# Construction: Orc_Scaffolding_Post_Deco_D9
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Scaffolding
#   Volume: EMorSimpleShape::OrientedBox, BoxExtent: (29.3, 109.0, 94.0)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (2030.3446, 4631.259, 939.62756), (0.0, 0.0, -0.0), (0.5868, 2.1801, 1.8793), "Orc_Scaffolding_Post_Deco_D9", _folder)
if a: placed += 1
else: skipped += 1

# Construction: Orc_Scaffolding_Support_Post_11
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Scaffolding
#   Volume: EMorSimpleShape::OrientedBox, BoxExtent: (206.3, 56.0, 246.9)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (2917.7466, 5102.895, 1242.0717), (0.0, 0.0, -0.0), (4.1256, 1.1192, 4.9381), "Orc_Scaffolding_Support_Post_11", _folder)
if a: placed += 1
else: skipped += 1

# Construction: Orc_Scaffolding_Support_Post2
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Scaffolding
#   Volume: EMorSimpleShape::OrientedBox, BoxExtent: (206.3, 56.0, 246.9)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (2577.2534, 5097.104, 1242.0717), (0.0, 0.0, -0.0), (4.1256, 1.1192, 4.9381), "Orc_Scaffolding_Support_Post2", _folder)
if a: placed += 1
else: skipped += 1

# ======================================================================
# PHASE 3: Breakables + DecoVolumes
# ======================================================================
unreal.log(f"[{BUBBLE_NAME}] Phase 3: Placing breakables and deco volumes...")

_folder = "Reconstruction/BD_BB_OrcPrison/Breakables"

# Breakable Batch 0: BP_Orc_Scaffolding_Post_1m_A (2 instances)
#   BP Class: /Game/LevelDesign/Architecture/Orc/BP_Orc_Scaffolding_Post_1m_A
_brk_mesh = "/Game/Art/Assets/Kits/Deco_Architecture/Orc_Camp/Orc_Scaffolding_Post_1m_A"
_brk_mats = ['/Game/Art/Assets/Kits/Deco_Architecture/Orc_Camp/Materials/MI_Orc_Scaffolding_Poles']
a = spawn_static_mesh(_brk_mesh, _brk_mats, (3044.9949, 5138.9814, 806.019), (1.8460289572959623, -1.8471065721243896, -45.02990476689123), (1.0, 1.0, 1.0), "BP_Orc_Scaffolding_Post_1m_A_5", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_brk_mesh, _brk_mats, (2440.0054, 5051.018, 806.019), (1.8460288775421403, 178.1530363116347, -45.02990081515343), (1.0, 1.0, 1.0), "BP_Orc_Scaffolding_Post_1m_A2", _folder)
if a: placed += 1
else: skipped += 1

# Breakable Batch 1: BP_Orc_Scaffolding_Post_1m_C (3 instances)
#   BP Class: /Game/LevelDesign/Architecture/Orc/BP_Orc_Scaffolding_Post_1m_C
_brk_mesh = "/Game/Art/Assets/Kits/Deco_Architecture/Orc_Camp/Orc_Scaffolding_Post_1m_C"
_brk_mats = ['/Game/Art/Assets/Kits/Deco_Architecture/Orc_Camp/Materials/MI_Orc_Scaffolding_Poles']
a = spawn_static_mesh(_brk_mesh, _brk_mats, (3045.0, 5065.0, 715.0), (0.0, 0.0, 30.000080924048913), (1.0, 1.0, 1.0), "BP_Orc_Scaffolding_Post_1m_C_5", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_brk_mesh, _brk_mats, (2440.0, 5124.9995, 715.0), (6.830185479114717e-06, -179.99976777356287, 30.00009598612991), (1.0, 1.0, 1.0), "BP_Orc_Scaffolding_Post_1m_C2", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_brk_mesh, _brk_mats, (4897.8926, 2570.8184, 699.9999), (9.037025936650295, 32.21865200535626, -85.83810958423072), (1.0, 1.0, 1.0), "BP_Orc_Scaffolding_Post_1m_C3_5", _folder)
if a: placed += 1
else: skipped += 1

# Breakable Batch 2: BP_Orc_Scaffolding_Post_1m_D (4 instances)
#   BP Class: /Game/LevelDesign/Architecture/Orc/BP_Orc_Scaffolding_Post_1m_D
_brk_mesh = "/Game/Art/Assets/Kits/Deco_Architecture/Orc_Camp/Orc_Scaffolding_Post_1m_D"
_brk_mats = ['/Game/Art/Assets/Kits/Deco_Architecture/Orc_Camp/Materials/MI_Orc_Scaffolding_Poles']
a = spawn_static_mesh(_brk_mesh, _brk_mats, (2997.5, 5075.0, 648.3493), (-30.000029965873445, 0.0, -0.0), (1.0, 1.0, 1.0), "BP_Orc_Scaffolding_Post_1m_D_2", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_brk_mesh, _brk_mats, (2997.5, 5125.0, 648.3493), (-30.000029965873445, 0.0, -0.0), (1.0, 1.0, 1.0), "BP_Orc_Scaffolding_Post_1m_D2", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_brk_mesh, _brk_mats, (2487.5, 5115.0, 648.3493), (-29.999968641668453, -179.99976777358006, 1.4787804443614645e-06), (1.0, 1.0, 1.0), "BP_Orc_Scaffolding_Post_1m_D3", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_brk_mesh, _brk_mats, (2487.5, 5065.0, 648.3493), (-29.999968641668453, -179.99976777358006, 1.4787804443614645e-06), (1.0, 1.0, 1.0), "BP_Orc_Scaffolding_Post_1m_D4", _folder)
if a: placed += 1
else: skipped += 1

# Breakable Batch 3: BP_Orc_Scaffolding_Post_2m_B (3 instances)
#   BP Class: /Game/LevelDesign/Architecture/Orc/BP_Orc_Scaffolding_Post_2m_B
_brk_mesh = "/Game/Art/Assets/Kits/Deco_Architecture/Orc_Camp/Orc_Scaffolding_Post_2m_B"
_brk_mats = ['/Game/Art/Assets/Kits/Deco_Architecture/Orc_Camp/Materials/MI_Orc_Scaffolding_Poles']
a = spawn_static_mesh(_brk_mesh, _brk_mats, (2980.0, 5080.0, 1260.0), (-90.0, 1.8848502594162701e-06, -359.99997456409073), (1.0, 1.0, 1.0), "BP_Orc_Scaffolding_Post_2m_B_5", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_brk_mesh, _brk_mats, (2340.0, 5085.0, 1260.0), (-90.0, 1.1029615739881892e-06, 3.093243794535529e-05), (1.0, 1.0, 1.0), "BP_Orc_Scaffolding_Post_2m_B2", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_brk_mesh, _brk_mats, (4910.3955, 2457.2908, 699.9999), (3.8408783414504115, -41.37796296366996, 87.0202413184604), (1.0, 1.0, 1.0), "BP_Orc_Scaffolding_Post_2m_B3_8", _folder)
if a: placed += 1
else: skipped += 1

# Breakable Batch 4: BP_Orc_Scaffolding_Post_2m_D (1 instances)
#   BP Class: /Game/LevelDesign/Architecture/Orc/BP_Orc_Scaffolding_Post_2m_D
_brk_mesh = "/Game/Art/Assets/Kits/Deco_Architecture/Orc_Camp/Orc_Scaffolding_Post_2m_D"
_brk_mats = ['/Game/Art/Assets/Kits/Deco_Architecture/Orc_Camp/Materials/MI_Orc_Scaffolding_Poles']
a = spawn_static_mesh(_brk_mesh, _brk_mats, (4497.4556, 2325.7517, 699.9999), (82.77518998705668, 44.50292888825971, 15.382938014914437), (1.0, 1.0, 1.0), "BP_Orc_Scaffolding_Post_2m_D_5", _folder)
if a: placed += 1
else: skipped += 1

# Breakable Batch 5: BP_Orc_Scaffolding_Post_3m_C (2 instances)
#   BP Class: /Game/LevelDesign/Architecture/Orc/BP_Orc_Scaffolding_Post_3m_C
_brk_mesh = "/Game/Art/Assets/Kits/Deco_Architecture/Orc_Camp/Orc_Scaffolding_Post_3m_C"
_brk_mats = ['/Game/Art/Assets/Kits/Deco_Architecture/Orc_Camp/Materials/MI_Orc_Scaffolding_Poles']
a = spawn_static_mesh(_brk_mesh, _brk_mats, (4445.0205, 2235.8743, 679.7043), (-1.52923581559805, 39.729366127654494, -13.852294156874544), (1.0, 1.0, 1.0), "BP_Orc_Scaffolding_Post_3m_C_2", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_brk_mesh, _brk_mats, (5027.3423, 2415.193, 697.9369), (5.868852677664675, 14.277753466382066, 86.61373315614033), (1.0, 1.0, 1.0), "BP_Orc_Scaffolding_Post_3m_C2_5", _folder)
if a: placed += 1
else: skipped += 1

# Breakable Batch 6: BP_Orc_Scaffolding_Post_4m_B (1 instances)
#   BP Class: /Game/LevelDesign/Architecture/Orc/BP_Orc_Scaffolding_Post_4m_B
_brk_mesh = "/Game/Art/Assets/Kits/Deco_Architecture/Orc_Camp/Orc_Scaffolding_Post_4m_B"
_brk_mats = ['/Game/Art/Assets/Kits/Deco_Architecture/Orc_Camp/Materials/MI_Orc_Scaffolding_Poles']
a = spawn_static_mesh(_brk_mesh, _brk_mats, (3297.4429, 3641.1921, 1069.9987), (-1.3522282023963767e-06, -30.000062899366238, -91.30932115308035), (1.0, 1.0, 1.0), "BP_Orc_Scaffolding_Post_4m_B_5", _folder)
if a: placed += 1
else: skipped += 1

# Breakable Batch 7: BP_Orc_Scaffolding_Post_5m_D (6 instances)
#   BP Class: /Game/LevelDesign/Architecture/Orc/BP_Orc_Scaffolding_Post_5m_D
_brk_mesh = "/Game/Art/Assets/Kits/Deco_Architecture/Orc_Camp/Orc_Scaffolding_Post_5m_D"
_brk_mats = ['/Game/Art/Assets/Kits/Deco_Architecture/Orc_Camp/Materials/MI_Orc_Scaffolding_Poles']
a = spawn_static_mesh(_brk_mesh, _brk_mats, (3055.0, 5075.0, 565.0), (0.0, 179.9998360754275, -0.0), (1.0, 1.0, 1.0), "BP_Orc_Scaffolding_Post_5m_D_10", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_brk_mesh, _brk_mats, (3450.0, 3316.8745, 1055.7648), (-15.000279045420953, -89.99976739775072, -89.99971948022608), (1.0, 1.0, 1.0), "BP_Orc_Scaffolding_Post_5m_D2_5", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_brk_mesh, _brk_mats, (2940.0, 3601.2449, 1073.4755), (-3.449661413062145e-09, -89.99939496003839, 90.00065317533128), (1.0, 1.0, 1.0), "BP_Orc_Scaffolding_Post_5m_D3", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_brk_mesh, _brk_mats, (3055.0, 5125.0, 565.0), (0.0, 179.9998360754275, -0.0), (1.0, 1.0, 1.0), "BP_Orc_Scaffolding_Post_5m_D4_12", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_brk_mesh, _brk_mats, (2429.9998, 5114.9995, 565.0), (0.0, 0.00012683868086621635, -0.0), (1.0, 1.0, 1.0), "BP_Orc_Scaffolding_Post_5m_D5", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_brk_mesh, _brk_mats, (2429.9998, 5064.9995, 565.0), (0.0, 4.294358130878158, -0.0), (1.0, 1.0, 1.0), "BP_Orc_Scaffolding_Post_5m_D6", _folder)
if a: placed += 1
else: skipped += 1

# Breakable Batch 8: BP_Orc_Scaffolding_Post_Deco_D (4 instances)
#   BP Class: /Game/LevelDesign/Architecture/Orc/BP_Orc_Scaffolding_Post_Deco_D
_brk_mesh = "/Game/Art/Assets/Kits/Deco_Architecture/Orc_Camp/Orc_Scaffolding_Post_Deco_D"
_brk_mats = ['/Game/Art/Assets/Kits/Deco/Orc/Materials/Orc_Lighting/MI_Orc_Lighting', '/Game/Art/Assets/Kits/Deco_Architecture/Orc_Camp/Materials/MI_Orc_Scaffolding_Platforms']
a = spawn_static_mesh(_brk_mesh, _brk_mats, (3055.0, 3300.0, 995.0), (0.0, 0.0, -0.0), (1.0, 1.0, 1.0), "BP_Orc_Scaffolding_Post_Deco_D2_5", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_brk_mesh, _brk_mats, (3345.0, 3299.9998, 995.0), (0.0, 179.99991120752276, -0.0), (1.0, 1.0, 1.0), "BP_Orc_Scaffolding_Post_Deco_D3", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_brk_mesh, _brk_mats, (3055.0, 3595.0, 995.0), (0.0, 0.0, -0.0), (1.0, 1.0, 1.0), "BP_Orc_Scaffolding_Post_Deco_D4", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_brk_mesh, _brk_mats, (3345.0, 3594.9998, 995.0), (0.0, 179.99991120752276, -0.0), (1.0, 1.0, 1.0), "BP_Orc_Scaffolding_Post_Deco_D5", _folder)
if a: placed += 1
else: skipped += 1

# Breakable Batch 9: BP_Suburb_Stairs_Trim_3M_Breakable (1 instances)
#   BP Class: /Game/LevelDesign/Architecture/Suburbs/BP_Suburb_Stairs_Trim_3M_Breakable
_brk_mesh = "/Game/Art/Assets/Kits/Architecture/City/City_Stairs_Trim_3M"
_brk_mats = ['/Game/Art/Assets/Kits/Architecture/Suburbs/Materials/Suburb_Stairs_Trim/MI_Suburb_Stairs_Trim_3M_Dest']
a = spawn_static_mesh(_brk_mesh, _brk_mats, (3800.0, 2000.0, 700.0), (0.0, 0.0, -0.0), (1.0, 1.0, 1.0), "BP_Suburb_Stairs_Trim_3M_Breakable39", _folder)
if a: placed += 1
else: skipped += 1

# Breakable Batch 10: SM_Mines_MetalBar_Window_A_Breakable (4 instances)
#   BP Class: /Game/LevelDesign/Deco/Mines/MetalGate/SM_Mines_MetalBar_Window_A_Breakable
_brk_mesh = "/Game/Art/Assets/Kits/Deco/Mines/Metal_Gate/SM_Mines_MetalBar_Window_A"
_brk_mats = ['/Game/Art/Assets/Kits/Deco/Mines/Materials/Mines_Metal_Gate/MI_Metal_Generic_A']
a = spawn_static_mesh(_brk_mesh, _brk_mats, (1920.0, 4510.0, 820.0), (90.0, 5.710586555951443, 95.71055905397398), (1.0, 1.0, 1.0), "SM_Mines_MetalBar_Window_A10", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_brk_mesh, _brk_mats, (1920.0, 3915.0, 820.0), (90.0, 5.710586555951443, 95.71055905397398), (1.0, 1.0, 1.0), "SM_Mines_MetalBar_Window_A4_164", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_brk_mesh, _brk_mats, (1920.0, 3610.0, 820.0), (90.0, 5.710586555951443, 95.71055905397398), (1.0, 1.0, 1.0), "SM_Mines_MetalBar_Window_A7_1", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_brk_mesh, _brk_mats, (1920.0, 4815.0, 820.0), (90.0, 5.710586555951443, 95.71055905397398), (1.0, 1.0, 1.0), "SM_Mines_MetalBar_Window_A9", _folder)
if a: placed += 1
else: skipped += 1

# Breakable Batch 11: SM_Mines_MetalGate_4Bar_3M_A_Breakable (14 instances)
#   BP Class: /Game/LevelDesign/Deco/Mines/MetalGate/SM_Mines_MetalGate_4Bar_3M_A_Breakable
_brk_mesh = "/Game/Art/Assets/Kits/Deco/Mines/Metal_Gate/SM_Mines_MetalGate_4Bar_3M_A"
_brk_mats = ['/Game/Art/Assets/Kits/Deco/Mines/Materials/Mines_Metal_Gate/MI_Metal_Generic_A']
a = spawn_static_mesh(_brk_mesh, _brk_mats, (1370.0, 4960.0, 700.0), (0.0, -90.00005166594045, 0.0), (1.0, 1.0, 1.0), "SM_Mines_MetalGate_4Bar_3M_A_119", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_brk_mesh, _brk_mats, (3570.0, 2660.0, 700.0), (0.0, 112.4998740494964, -0.0), (1.0, 1.0, 1.0), "SM_Mines_MetalGate_4Bar_3M_A10", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_brk_mesh, _brk_mats, (3550.0, 2750.0, 700.0), (0.0, -90.00005166594045, 0.0), (1.0, 1.0, 1.0), "SM_Mines_MetalGate_4Bar_3M_A11", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_brk_mesh, _brk_mats, (2905.0, 2140.0, 705.0), (0.0, -89.99993822608693, 0.0), (1.0, 1.0, 1.0), "SM_Mines_MetalGate_4Bar_3M_A12_205", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_brk_mesh, _brk_mats, (2905.0, 2750.0, 705.0), (0.0, -89.99993822608693, 0.0), (1.0, 1.0, 1.0), "SM_Mines_MetalGate_4Bar_3M_A13", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_brk_mesh, _brk_mats, (1997.0, 4495.0, 1002.99915), (0.0003961509536167593, -89.99981506332342, -179.99989754715293), (1.0, 1.0, 0.4375), "SM_Mines_MetalGate_4Bar_3M_A14_94", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_brk_mesh, _brk_mats, (1997.0006, 4255.0, 1003.0007), (0.000395999957068219, -89.99981506332304, -179.99989754717745), (1.0, 1.0, 0.4375), "SM_Mines_MetalGate_4Bar_3M_A15", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_brk_mesh, _brk_mats, (1370.0, 5060.0, 700.0), (0.0, 89.99974375801533, -0.0), (1.0, 1.0, 1.0), "SM_Mines_MetalGate_4Bar_3M_A2", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_brk_mesh, _brk_mats, (3550.0, 2150.0, 700.0), (0.0, -90.00005166594045, 0.0), (1.0, 1.0, 1.0), "SM_Mines_MetalGate_4Bar_3M_A4_183", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_brk_mesh, _brk_mats, (1370.0, 4560.0, 700.0), (0.0, -90.00005166594045, 0.0), (1.0, 1.0, 1.0), "SM_Mines_MetalGate_4Bar_3M_A5", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_brk_mesh, _brk_mats, (1370.0, 4660.0, 700.0), (0.0, 89.99974375801533, -0.0), (1.0, 1.0, 1.0), "SM_Mines_MetalGate_4Bar_3M_A6", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_brk_mesh, _brk_mats, (3570.0, 2240.0, 700.0), (0.0, 67.49977485646544, -0.0), (1.0, 1.0, 1.0), "SM_Mines_MetalGate_4Bar_3M_A7", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_brk_mesh, _brk_mats, (3640.0, 2290.0, 700.0), (0.0, -165.93731911372126, 0.0), (1.0, 1.0, 1.0), "SM_Mines_MetalGate_4Bar_3M_A8", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_brk_mesh, _brk_mats, (3635.0, 2600.0, 700.0), (0.0, -19.687348349152686, 0.0), (1.0, 1.0, 1.0), "SM_Mines_MetalGate_4Bar_3M_A9_190", _folder)
if a: placed += 1
else: skipped += 1

# Breakable Batch 12: SM_Mines_MetalGate_5Bar_2Cross_A_Breakable (4 instances)
#   BP Class: /Game/LevelDesign/Deco/Mines/MetalGate/SM_Mines_MetalGate_5Bar_2Cross_A_Breakable
_brk_mesh = "/Game/Art/Assets/Kits/Deco/Mines/Metal_Gate/SM_Mines_MetalGate_5Bar_2Cross_A"
_brk_mats = ['/Game/Art/Assets/Kits/Deco/Mines/Materials/Mines_Metal_Gate/MI_Metal_Generic_A']
a = spawn_static_mesh(_brk_mesh, _brk_mats, (1760.0, 3510.0, 705.0), (0.0, 0.0, -0.0), (1.0, 1.0, 1.0), "SM_Mines_MetalGate_5Bar_2Cross_A_277", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_brk_mesh, _brk_mats, (2950.0, 2255.0, 705.0), (0.0, 90.00010028305118, -0.0), (1.0, 1.0, 1.0), "SM_Mines_MetalGate_5Bar_2Cross_A2_202", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_brk_mesh, _brk_mats, (2950.0, 2630.0, 705.0), (0.0, 90.00010028305118, -0.0), (1.0, 1.0, 1.0), "SM_Mines_MetalGate_5Bar_2Cross_A3", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_brk_mesh, _brk_mats, (1957.0005, 4373.9985, 995.9996), (-0.0007629394321625302, 89.99987340768813, 179.99976777354522), (1.0, 1.0, 0.4375), "SM_Mines_MetalGate_5Bar_2Cross_A6", _folder)
if a: placed += 1
else: skipped += 1

# Breakable Batch 13: SM_Mines_MetalGate_5Bar_2M_A_Breakable (2 instances)
#   BP Class: /Game/LevelDesign/Deco/Mines/MetalGate/SM_Mines_MetalGate_5Bar_2M_A_Breakable
_brk_mesh = "/Game/Art/Assets/Kits/Deco/Mines/Metal_Gate/SM_Mines_MetalGate_5Bar_2M_A"
_brk_mats = ['/Game/Art/Assets/Kits/Deco/Mines/Materials/Mines_Metal_Gate/MI_Metal_Generic_A']
a = spawn_static_mesh(_brk_mesh, _brk_mats, (1370.0, 4810.0, 700.0), (0.0, 89.99998684315639, -0.0), (1.0, 1.0, 1.0), "SM_Mines_MetalGate_5Bar_2M_A_Breakable_2", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_brk_mesh, _brk_mats, (1650.0, 5110.0, 700.0), (0.0, 0.0, -0.0), (1.0, 1.0, 1.0), "SM_Mines_MetalGate_5Bar_2M_A_Breakable2", _folder)
if a: placed += 1
else: skipped += 1

# Breakable Batch 14: SM_Mines_MetalGate_5Bar_3M_A_Breakable (7 instances)
#   BP Class: /Game/LevelDesign/Deco/Mines/MetalGate/SM_Mines_MetalGate_5Bar_3M_A_Breakable
_brk_mesh = "/Game/Art/Assets/Kits/Deco/Mines/Metal_Gate/SM_Mines_MetalGate_5Bar_3M_A"
_brk_mats = ['/Game/Art/Assets/Kits/Deco/Mines/Materials/Mines_Metal_Gate/MI_Metal_Generic_A']
a = spawn_static_mesh(_brk_mesh, _brk_mats, (3550.0, 2160.0, 1270.0), (2.732075220615722e-05, 90.00007597467642, 179.99976777357162), (1.0, 1.0, 1.0), "SM_Mines_MetalGate_5Bar_3M_A2_193", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_brk_mesh, _brk_mats, (3550.0, 2355.0, 1270.0), (2.7320773286759034e-05, -90.00005166623438, 179.99976777356696), (1.0, 1.0, 1.0), "SM_Mines_MetalGate_5Bar_3M_A3_195", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_brk_mesh, _brk_mats, (3550.0, 2560.0, 1270.0), (2.732075220615722e-05, 90.00007597467642, 179.99976777357162), (1.0, 1.0, 1.0), "SM_Mines_MetalGate_5Bar_3M_A4_198", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_brk_mesh, _brk_mats, (3550.0, 2755.0, 1270.0), (2.7320773286759034e-05, -90.00005166623438, 179.99976777356696), (1.0, 1.0, 1.0), "SM_Mines_MetalGate_5Bar_3M_A5_199", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_brk_mesh, _brk_mats, (2906.0, 2655.0, 1266.0), (4.098112550261866e-05, 89.99980858068226, -179.99995901885194), (1.0, 1.0, 1.0), "SM_Mines_MetalGate_5Bar_3M_A6_189", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_brk_mesh, _brk_mats, (2905.9998, 2455.0, 1266.0), (4.098112550261866e-05, 89.99980858068226, -179.99995901885194), (1.0, 1.0, 1.0), "SM_Mines_MetalGate_5Bar_3M_A7", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_brk_mesh, _brk_mats, (2906.0007, 2255.0002, 1266.0), (4.098112550261866e-05, 89.99980858068226, -179.99995901885194), (1.0, 1.0, 1.0), "SM_Mines_MetalGate_5Bar_3M_A8", _folder)
if a: placed += 1
else: skipped += 1

# Breakable Batch 15: SM_Mines_MetalGate_SingleBar_3M_A_Breakable (2 instances)
#   BP Class: /Game/LevelDesign/Deco/Mines/MetalGate/SM_Mines_MetalGate_SingleBar_3M_A_Breakable
_brk_mesh = "/Game/Art/Assets/Kits/Deco/Mines/Metal_Gate/SM_Mines_MetalGate_SingleBar_3M_A"
_brk_mats = ['/Game/Art/Assets/Kits/Deco/Mines/Materials/Mines_Metal_Gate/MI_Metal_Generic_A']
a = spawn_static_mesh(_brk_mesh, _brk_mats, (1855.0, 3550.0, 705.0), (0.0, 0.0, -0.0), (1.0, 1.0, 1.0), "SM_Mines_MetalGate_SingleBar_3M_A_280", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_brk_mesh, _brk_mats, (1660.0, 3550.0, 705.0), (0.0, 0.0, -0.0), (1.0, 1.0, 1.0), "SM_Mines_MetalGate_SingleBar_3M_A2", _folder)
if a: placed += 1
else: skipped += 1

# Breakable Batch 16: BP_DM_Orc_Shanty_Midden_C_A_Breakable (1 instances)
#   BP Class: /Game/LevelDesign/Deco/Orc_Shanty/BP_DM_Orc_Shanty_Midden_C_A_Breakable
_brk_mesh = "/Game/Art/Assets/Kits/Deco/Orc/Shanty/Orc_Shanty_Midden_C_A"
_brk_mats = ['/Game/Art/Assets/Kits/Deco/Orc/Shanty/Material/Orc_Shanty_Midden/MI_Orc_Shanty_Midden_Mat_Inst', '/Game/Art/Assets/Kits/Deco/Orc/Shanty/Material/Orc_Shanty_Midden/MI_Orc_Shanty_Midden_Tileable_B_Mat_Inst']
a = spawn_static_mesh(_brk_mesh, _brk_mats, (4665.3174, 4524.83, 597.70276), (0.0, 33.92040918598553, -0.0), (1.0, 1.0, 1.0), "BP_DM_Orc_Shanty_Midden_C_A_Breakable_2", _folder)
if a: placed += 1
else: skipped += 1

# Breakable Batch 17: BP_DM_Rubble_Masonry_large_A_Breakable (12 instances)
#   BP Class: /Game/LevelDesign/Deco/Rubble/BP_DM_Rubble_Masonry_large_A_Breakable
_brk_mesh = "/Game/Art/Assets/Kits/Deco/Rubble/Rubble_Masonry_large_A"
_brk_mats = ['/Game/Art/Assets/Kits/Deco_Architecture/Ruins/Materials/Ruin_Wall_Thick/MI_Ruin_Wall_IndStone2', '/Game/Art/Assets/Kits/Deco_Architecture/Ruins/Materials/Ruin_Wall_Thick/MI_Ruin_Wall_IndStone3', '/Game/Art/Assets/Kits/Deco_Architecture/Ruins/Materials/Ruin_Wall_Thick/MI_Ruin_Wall_IndStone1', '/Game/Art/Assets/Kits/Deco/Rubble/Materials/Rubble_Masonry_Pile/MI_Rubble_Masonry_Pile_06_Inst']
a = spawn_static_mesh(_brk_mesh, _brk_mats, (2851.4148, 5065.973, 606.0), (3.992497824946626, 147.39673244672065, 1.5975807568893379), (1.0, 1.0, 1.0), "BP_DM_Rubble_Masonry_large_A_Breakable_5", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_brk_mesh, _brk_mats, (3444.4194, 3186.512, 606.33435), (-1.5244445243737401, 61.944111337858835, 0.7460754432939606), (1.0, 1.0, 1.0), "BP_DM_Rubble_Masonry_large_A_Breakable10", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_brk_mesh, _brk_mats, (1451.7175, 2853.5068, 702.9945), (0.0, -15.000031747560248, 0.0), (1.0, 1.0, 1.0), "BP_DM_Rubble_Masonry_large_A_Breakable12_24", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_brk_mesh, _brk_mats, (1445.3579, 3458.847, 702.9945), (0.0, 167.88214589482146, -0.0), (1.0, 1.0, 1.0), "BP_DM_Rubble_Masonry_large_A_Breakable13", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_brk_mesh, _brk_mats, (1121.3005, 3706.8938, 801.8889), (0.0, 100.83464047061389, -0.0), (1.0, 1.0, 1.0), "BP_DM_Rubble_Masonry_large_A_Breakable14", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_brk_mesh, _brk_mats, (1654.7002, 2874.7695, 702.9945), (0.0, -175.95182621108623, 0.0), (1.0, 1.0, 1.0), "BP_DM_Rubble_Masonry_large_A_Breakable15", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_brk_mesh, _brk_mats, (2950.0, 1200.0, 800.0), (0.0, -90.00005166594045, 0.0), (1.0, 1.0, 1.0), "BP_DM_Rubble_Masonry_large_A_Breakable3_2", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_brk_mesh, _brk_mats, (2700.0, 1149.9994, 800.0), (0.0, 7.247924817365332e-05, -0.0), (1.0, 1.0, 1.0), "BP_DM_Rubble_Masonry_large_A_Breakable4", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_brk_mesh, _brk_mats, (2700.836, 5025.2485, 601.88354), (0.0, 50.000079784565294, -0.0), (1.0, 1.0, 1.0), "BP_DM_Rubble_Masonry_large_A_Breakable6_2", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_brk_mesh, _brk_mats, (3476.1628, 4402.4937, 592.1006), (0.0, 98.70765039411278, -0.0), (1.0, 1.0, 1.0), "BP_DM_Rubble_Masonry_large_A_Breakable7_8", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_brk_mesh, _brk_mats, (3879.9138, 2052.0474, 710.86536), (0.0, -12.0090328625972, 0.0), (1.0, 1.0, 1.0), "BP_DM_Rubble_Masonry_large_A_Breakable8_14", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_brk_mesh, _brk_mats, (2995.2827, 3233.0312, 594.1242), (-1.5245666442788972, 67.9605673850825, 0.7460756229691851), (1.0, 1.0, 1.0), "BP_DM_Rubble_Masonry_large_A_Breakable9_17", _folder)
if a: placed += 1
else: skipped += 1

# Breakable Batch 18: BP_DM_Rubble_Masonry_large_C_Breakable (3 instances)
#   BP Class: /Game/LevelDesign/Deco/Rubble/BP_DM_Rubble_Masonry_large_C_Breakable
_brk_mesh = "/Game/Art/Assets/Kits/Deco/Rubble/Rubble_Masonry_large_C"
_brk_mats = ['/Game/Art/Assets/Kits/Deco_Architecture/Ruins/Materials/Ruin_Wall_Thick/MI_Ruin_Wall_IndStone3', '/Game/Art/Assets/Kits/Deco_Architecture/Ruins/Materials/Ruin_Wall_Thick/MI_Ruin_Wall_IndStone2', '/Game/Art/Assets/Kits/Deco_Architecture/Ruins/Materials/Ruin_Wall_Thick/MI_Ruin_Wall_IndStone1', '/Game/Art/Assets/Kits/Deco/Rubble/Materials/Rubble_Masonry_Pile/MI_Rubble_Masonry_Pile_06_Inst']
a = spawn_static_mesh(_brk_mesh, _brk_mats, (2615.492, 5079.9824, 639.4131), (0.0, 160.00017681518196, -0.0), (1.0, 1.0, 1.0), "BP_DM_Rubble_Masonry_large_C_Breakable2_2", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_brk_mesh, _brk_mats, (3684.1177, 4396.087, 598.87854), (0.0, 118.9734619581392, -0.0), (1.0, 1.0, 1.0), "BP_DM_Rubble_Masonry_large_C_Breakable3_8", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_brk_mesh, _brk_mats, (3676.5515, 3922.2993, 602.17365), (0.0, -134.84785099737095, 0.0), (1.0, 1.0, 1.0), "BP_DM_Rubble_Masonry_large_C_Breakable4_11", _folder)
if a: placed += 1
else: skipped += 1

# Breakable Batch 19: BP_DM_Rubble_Masonry_large_D_Breakable (3 instances)
#   BP Class: /Game/LevelDesign/Deco/Rubble/BP_DM_Rubble_Masonry_large_D_Breakable
_brk_mesh = "/Game/Art/Assets/Kits/Deco/Rubble/Rubble_Masonry_large_D"
_brk_mats = ['/Game/Art/Assets/Kits/Deco_Architecture/Ruins/Materials/Ruin_Wall_Thick/MI_Ruin_Wall_IndStone2', '/Game/Art/Assets/Kits/Deco_Architecture/Ruins/Materials/Ruin_Wall_Thick/MI_Ruin_Wall_IndStone3', '/Game/Art/Assets/Kits/Deco/Rubble/Materials/Rubble_Masonry_Pile/MI_Rubble_Masonry_Pile_06_Inst']
a = spawn_static_mesh(_brk_mesh, _brk_mats, (2619.0, 5043.0, 606.0), (0.0, -0.0005187988105841447, 0.0), (1.0, 1.0, 1.0), "BP_DM_Rubble_Masonry_large_D_Breakable_2", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_brk_mesh, _brk_mats, (4128.534, 2175.7732, 702.59766), (0.0, 139.76828142475281, -0.0), (1.0, 1.0, 1.0), "BP_DM_Rubble_Masonry_large_D_Breakable2_8", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_brk_mesh, _brk_mats, (3486.9387, 1061.6312, 797.755), (0.0, 78.77546678376862, -0.0), (1.0, 1.0, 1.0), "BP_DM_Rubble_Masonry_large_D_Breakable3_14", _folder)
if a: placed += 1
else: skipped += 1

# Breakable Batch 20: BP_DM_Rubble_Masonry_large_E_Breakable (1 instances)
#   BP Class: /Game/LevelDesign/Deco/Rubble/BP_DM_Rubble_Masonry_large_E_Breakable
_brk_mesh = "/Game/Art/Assets/Kits/Deco/Rubble/Rubble_Masonry_large_E"
_brk_mats = ['/Game/Art/Assets/Kits/Deco_Architecture/Ruins/Materials/Ruin_Wall_Thick/MI_Ruin_Wall_IndStone1', '/Game/Art/Assets/Kits/Deco_Architecture/Ruins/Materials/Ruin_Wall_Thick/MI_Ruin_Wall_IndStone3', '/Game/Art/Assets/Kits/Deco_Architecture/Ruins/Materials/Ruin_Wall_Thick/MI_Ruin_Wall_IndStone2', '/Game/Art/Assets/Kits/Deco/Rubble/Materials/Rubble_Masonry_Pile/MI_Rubble_Masonry_Pile_06_Inst']
a = spawn_static_mesh(_brk_mesh, _brk_mats, (3936.5574, 2135.665, 706.0), (0.0, 87.18739009934427, -0.0), (1.0, 1.0, 1.0), "BP_DM_Rubble_Masonry_large_E_Breakable_2", _folder)
if a: placed += 1
else: skipped += 1

# Breakable Batch 21: BP_DM_Rubble_Masonry_large_F_Breakable (2 instances)
#   BP Class: /Game/LevelDesign/Deco/Rubble/BP_DM_Rubble_Masonry_large_F_Breakable
_brk_mesh = "/Game/Art/Assets/Kits/Deco/Rubble/Rubble_Masonry_large_F"
_brk_mats = ['/Game/Art/Assets/Kits/Deco_Architecture/Ruins/Materials/Ruin_Wall_Thick/MI_Ruin_Wall_IndStone1', '/Game/Art/Assets/Kits/Deco_Architecture/Ruins/Materials/Ruin_Wall_Thick/MI_Ruin_Wall_IndStone3', '/Game/Art/Assets/Kits/Deco_Architecture/Ruins/Materials/Ruin_Wall_Thick/MI_Ruin_Wall_IndStone2', '/Game/Art/Assets/Kits/Deco/Rubble/Materials/Rubble_Masonry_Pile/MI_Rubble_Masonry_Pile_06_Inst']
a = spawn_static_mesh(_brk_mesh, _brk_mats, (3936.0, 2797.0, 701.0), (0.0, -67.49981621287719, 0.0), (1.0, 1.0, 1.0), "BP_DM_Rubble_Masonry_large_F_Breakable2_5", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_brk_mesh, _brk_mats, (3464.807, 3950.4746, 587.3508), (0.0, -89.62752996000602, 0.0), (1.0, 1.0, 1.0), "BP_DM_Rubble_Masonry_large_F_Breakable3_2", _folder)
if a: placed += 1
else: skipped += 1

# Breakable Batch 22: BP_DM_Rubble_Masonry_Pile_A_Breakable (1 instances)
#   BP Class: /Game/LevelDesign/Deco/Rubble/BP_DM_Rubble_Masonry_Pile_A_Breakable
_brk_mesh = "/Game/Art/Assets/Kits/Deco/Rubble/Rubble_Masonry_Pile_A"
_brk_mats = ['/Game/Art/Assets/Kits/Deco/Rubble/Materials/Rubble_Masonry_Pile/MI_Rubble_Masonry_Pile_Atlas_Inst_A', '/Game/Art/Assets/Kits/Deco/Rubble/Materials/Rubble_Masonry_Pile/MI_Rubble_Masonry_Pile_Atlas_Inst_A']
a = spawn_static_mesh(_brk_mesh, _brk_mats, (3450.0, 1450.0012, 800.0), (0.0, -90.0001164887758, 0.0), (1.0, 1.0, 1.0), "BP_DM_Rubble_Masonry_Pile_A_Breakable_2", _folder)
if a: placed += 1
else: skipped += 1

# Breakable Batch 23: BP_DM_Rubble_Masonry_Pile_C_Breakable (4 instances)
#   BP Class: /Game/LevelDesign/Deco/Rubble/BP_DM_Rubble_Masonry_Pile_C_Breakable
_brk_mesh = "/Game/Art/Assets/Kits/Deco/Rubble/Rubble_Masonry_Pile_C"
_brk_mats = ['/Game/Art/Assets/Kits/Deco/Rubble/Materials/Rubble_Masonry_Pile/MI_Rubble_Masonry_Pile_Atlas_Inst_B', '/Game/Art/Assets/Kits/Deco/Rubble/Materials/Rubble_Masonry_Pile/MI_Rubble_Masonry_Pile_Atlas_Inst_A']
a = spawn_static_mesh(_brk_mesh, _brk_mats, (3427.559, 3700.6072, 595.88464), (0.0, 105.52335456536487, -0.0), (1.0, 1.0, 1.0), "BP_DM_Rubble_Masonry_Pile_C_Breakable_17", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_brk_mesh, _brk_mats, (2230.7036, 2306.4387, 688.1888), (-4.090729063692468, -22.407686842289348, 4.043015955159256), (1.0, 1.0, 1.0), "BP_DM_Rubble_Masonry_Pile_C_Breakable2_20", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_brk_mesh, _brk_mats, (3879.1462, 2753.3943, 694.3989), (0.0, 158.23597905655797, -0.0), (1.0, 1.0, 1.0), "BP_DM_Rubble_Masonry_Pile_C_Breakable3_23", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_brk_mesh, _brk_mats, (1768.2561, 2604.4214, 693.13916), (0.0, -38.77533055628702, 0.0), (1.0, 1.0, 1.0), "BP_DM_Rubble_Masonry_Pile_C_Breakable4_27", _folder)
if a: placed += 1
else: skipped += 1

# Breakable Batch 24: BP_DM_Rubble_Masonry_Pile_E_Breakable (1 instances)
#   BP Class: /Game/LevelDesign/Deco/Rubble/BP_DM_Rubble_Masonry_Pile_E_Breakable
_brk_mesh = "/Game/Art/Assets/Kits/Deco/Rubble/Rubble_Masonry_Pile_E_Optimized"
_brk_mats = ['/Game/Art/Assets/Kits/Deco/Rubble/Materials/Rubble_Masonry_Pile/MI_Rubble_Masonry_Pile_Atlas_Inst_A', '/Game/Art/Assets/Kits/Deco/Rubble/Materials/Rubble_Masonry_Pile/MI_Rubble_Masonry_Pile_Atlas_Inst_B']
a = spawn_static_mesh(_brk_mesh, _brk_mats, (2979.579, 5111.2246, 644.567), (0.0, 0.0, -20.000029202010403), (1.0, 1.0, 1.0), "BP_DM_Rubble_Masonry_Pile_E_Breakable_2", _folder)
if a: placed += 1
else: skipped += 1

# Breakable Batch 25: BP_DM_Rubble_Masonry_Pile_F_Breakable (1 instances)
#   BP Class: /Game/LevelDesign/Deco/Rubble/BP_DM_Rubble_Masonry_Pile_F_Breakable
_brk_mesh = "/Game/Art/Assets/Kits/Deco/Rubble/Rubble_Masonry_Pile_F_Optimized"
_brk_mats = ['/Game/Art/Assets/Kits/Deco/Rubble/Materials/Rubble_Masonry_Pile/MI_Rubble_Masonry_Pile_Atlas_Inst_B', '/Game/Art/Assets/Kits/Deco/Rubble/Materials/Rubble_Masonry_Pile/MI_Rubble_Masonry_Pile_Atlas_Inst_A']
a = spawn_static_mesh(_brk_mesh, _brk_mats, (2512.2158, 2128.1885, 682.7608), (0.0, -49.776274618225315, 0.0), (1.0, 1.0, 1.0), "BP_DM_Rubble_Masonry_Pile_F_Breakable_17", _folder)
if a: placed += 1
else: skipped += 1

# Breakable Batch 26: BP_DM_Rubble_Masonry_Pile_H_Breakable (1 instances)
#   BP Class: /Game/LevelDesign/Deco/Rubble/BP_DM_Rubble_Masonry_Pile_H_Breakable
_brk_mesh = "/Game/Art/Assets/Kits/Deco/Rubble/Rubble_Masonry_Pile_H_Optimized"
_brk_mats = ['/Game/Art/Assets/Kits/Deco/Rubble/Materials/Rubble_Masonry_Pile/MI_Rubble_Masonry_Pile_Atlas_Inst_B', '/Game/Art/Assets/Kits/Deco/Rubble/Materials/Rubble_Masonry_Pile/MI_Rubble_Masonry_Pile_Atlas_Inst_A']
a = spawn_static_mesh(_brk_mesh, _brk_mats, (2470.454, 4981.7876, 594.3791), (0.0, 0.0, -0.0), (1.0, 1.0, 1.0), "BP_DM_Rubble_Masonry_Pile_H_Breakable_2", _folder)
if a: placed += 1
else: skipped += 1

# Breakable Batch 27: BP_DM_Remains_Bones_Assemblage_A_Breakable (2 instances)
#   BP Class: /Game/LevelDesign/Deco/Warrens_Tomb/BP_DM_Remains_Bones_Assemblage_A_Breakable
_brk_mesh = "/Game/Art/Assets/Kits/Deco/Warrens_Tomb/Remains_Bones_Assemblage_A"
_brk_mats = ['/Game/Art/Assets/Kits/Deco/Orc/Shanty/Material/Orc_Shanty_Midden/MI_Orc_Shanty_Midden_Mat_Inst']
a = spawn_static_mesh(_brk_mesh, _brk_mats, (4600.0, 3950.0, 600.0), (0.0, 0.0, -0.0), (1.0, 1.0, 1.0), "BP_DM_Remains_Bones_Assemblage_A_Breakable_2", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_brk_mesh, _brk_mats, (4056.1208, 3954.4607, 602.6028), (2.485355523439316, -48.60535126375107, 6.312967919564958), (1.0, 1.0, 1.0), "BP_DM_Remains_Bones_Assemblage_A_Breakable2_5", _folder)
if a: placed += 1
else: skipped += 1

# Breakable Batch 28: BP_DM_Remains_Bones_Assemblage_B_Breakable (4 instances)
#   BP Class: /Game/LevelDesign/Deco/Warrens_Tomb/BP_DM_Remains_Bones_Assemblage_B_Breakable
_brk_mesh = "/Game/Art/Assets/Kits/Deco/Warrens_Tomb/Remains_Bones_Assemblage_B"
_brk_mats = ['/Game/Art/Assets/Kits/Deco/Orc/Shanty/Material/Orc_Shanty_Midden/MI_Orc_Shanty_Midden_Mat_Inst']
a = spawn_static_mesh(_brk_mesh, _brk_mats, (4600.0, 4050.0, 600.0), (0.0, 0.0, -0.0), (1.0, 1.0, 1.0), "BP_DM_Remains_Bones_Assemblage_B_Breakable_2", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_brk_mesh, _brk_mats, (4600.0, 4000.0, 600.0), (0.0, -60.000067159027765, 0.0), (1.0, 1.0, 1.0), "BP_DM_Remains_Bones_Assemblage_B_Breakable2_5", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_brk_mesh, _brk_mats, (4094.283, 3928.343, 611.3308), (0.0, 0.0, 10.42991723829839), (1.0, 1.0, 1.0), "BP_DM_Remains_Bones_Assemblage_B_Breakable3_8", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_brk_mesh, _brk_mats, (930.29694, 5024.478, 704.88385), (0.0, 58.87877294400366, -0.0), (1.0, 1.0, 1.0), "BP_DM_Remains_Bones_Assemblage_B_Breakable6_8", _folder)
if a: placed += 1
else: skipped += 1

# Breakable Batch 29: BP_DM_Remains_Bones_Assemblage_C_Breakable (5 instances)
#   BP Class: /Game/LevelDesign/Deco/Warrens_Tomb/BP_DM_Remains_Bones_Assemblage_C_Breakable
_brk_mesh = "/Game/Art/Assets/Kits/Deco/Warrens_Tomb/Remains_Bones_Assemblage_C"
_brk_mats = ['/Game/Art/Assets/Kits/Deco/Orc/Shanty/Material/Orc_Shanty_Midden/MI_Orc_Shanty_Midden_Mat_Inst']
a = spawn_static_mesh(_brk_mesh, _brk_mats, (4650.0, 4100.0, 600.0), (0.0, 0.0, -0.0), (1.0, 1.0, 1.0), "BP_DM_Remains_Bones_Assemblage_C_Breakable_2", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_brk_mesh, _brk_mats, (3827.2288, 3911.2554, 617.8795), (-5.753752702480341, -0.12872310558697533, 17.551215981328056), (1.0, 1.0, 1.0), "BP_DM_Remains_Bones_Assemblage_C_Breakable2_5", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_brk_mesh, _brk_mats, (1049.8672, 5014.6274, 703.67175), (-3.4762875196584755, -148.81313263864448, 1.40303971932764), (1.0, 1.0, 1.0), "BP_DM_Remains_Bones_Assemblage_C_Breakable4_5", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_brk_mesh, _brk_mats, (1791.0254, 5597.8228, 705.47394), (0.8992078912019073, 137.1743279008594, -1.9503783284274738), (1.0, 1.0, 1.0), "BP_DM_Remains_Bones_Assemblage_C_Breakable6", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_brk_mesh, _brk_mats, (740.8397, 5014.6274, 713.598), (-0.9958493481342873, -149.57887884424017, 10.68366069865719), (1.0, 1.0, 1.0), "BP_DM_Remains_Bones_Assemblage_C_Breakable7", _folder)
if a: placed += 1
else: skipped += 1

# Breakable Batch 30: BP_DM_Building_Arch_Thin_A (2 instances)
#   BP Class: /Game/LevelDesign/Deco_Architecture/Suburbs/BP_DM_Building_Arch_Thin_A
_brk_mesh = "/Game/Art/Assets/Kits/Deco_Architecture/Suburbs/Building_Arch_Thin_A"
_brk_mats = ['/Game/Art/Assets/Kits/Deco_Architecture/Suburbs/Materials/Building_Wood_Interior/MI_Building_Wood_Interior_A_Mat_Dest']
a = spawn_static_mesh(_brk_mesh, _brk_mats, (2940.0002, 750.0, 1360.0), (0.0, 179.99991120752276, -0.0), (1.0, 1.0, 1.0), "BP_DM_Building_Arch_Thin_A10", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_brk_mesh, _brk_mats, (2940.0002, 1049.9999, 1360.0), (0.0, 179.99991120752276, -0.0), (1.0, 1.0, 1.0), "BP_DM_Building_Arch_Thin_A4", _folder)
if a: placed += 1
else: skipped += 1

# Breakable Batch 31: BP_DM_Building_Beam_Horizontal_3M_A (13 instances)
#   BP Class: /Game/LevelDesign/Deco_Architecture/Suburbs/BP_DM_Building_Beam_Horizontal_3M_A
_brk_mesh = "/Game/Art/Assets/Kits/Deco_Architecture/Suburbs/Building_Beam_Horizontal_3M_A"
_brk_mats = ['/Game/Art/Assets/Kits/Deco_Architecture/Suburbs/Materials/Building_Wood_Interior/MI_Building_Wood_Interior_C_Mat']
a = spawn_static_mesh(_brk_mesh, _brk_mats, (3050.0, 750.0, 1350.0), (0.0, 0.0, -0.0), (1.0, 1.0, 1.0), "BP_DM_Building_Beam_Horizontal_3M_A10", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_brk_mesh, _brk_mats, (3200.0, 4665.0, 1280.0), (0.0, 90.0000030488508, -0.0), (1.0, 1.0, 1.0), "BP_DM_Building_Beam_Horizontal_3M_A13", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_brk_mesh, _brk_mats, (2450.0, 3920.0, 1280.0), (0.0, 7.62939484614981e-06, -0.0), (1.0, 1.0, 1.0), "BP_DM_Building_Beam_Horizontal_3M_A14", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_brk_mesh, _brk_mats, (2750.0, 3920.0, 1280.0), (0.0, 7.999999990858693e-06, -0.0), (1.0, 1.0, 1.0), "BP_DM_Building_Beam_Horizontal_3M_A15", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_brk_mesh, _brk_mats, (3050.0, 3920.0, 1280.0), (0.0, 7.999999990858693e-06, -0.0), (1.0, 1.0, 1.0), "BP_DM_Building_Beam_Horizontal_3M_A16", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_brk_mesh, _brk_mats, (2290.0, 4075.0, 1280.0), (0.0, -89.99999818714215, 0.0), (1.0, 1.0, 1.0), "BP_DM_Building_Beam_Horizontal_3M_A17", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_brk_mesh, _brk_mats, (2290.0, 4375.0, 1280.0), (0.0, -89.99999818714215, 0.0), (1.0, 1.0, 1.0), "BP_DM_Building_Beam_Horizontal_3M_A18", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_brk_mesh, _brk_mats, (2290.0, 4675.0, 1280.0), (0.0, -89.99999818714215, 0.0), (1.0, 1.0, 1.0), "BP_DM_Building_Beam_Horizontal_3M_A19", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_brk_mesh, _brk_mats, (3350.0, 1050.0, 1350.0), (0.0, 0.0, -0.0), (1.0, 1.0, 1.0), "BP_DM_Building_Beam_Horizontal_3M_A5", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_brk_mesh, _brk_mats, (3050.0, 1050.0, 1350.0), (0.0, 0.0, -0.0), (1.0, 1.0, 1.0), "BP_DM_Building_Beam_Horizontal_3M_A6", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_brk_mesh, _brk_mats, (3350.0, 750.0, 1350.0), (0.0, 0.0, -0.0), (1.0, 1.0, 1.0), "BP_DM_Building_Beam_Horizontal_3M_A9", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_brk_mesh, _brk_mats, (1220.0, 3050.0, 1290.0), (8.021399989875836e-06, 89.99999656232319, 90.0001077161388), (1.0, 1.0, 1.0), "Building_Beam_Thin_3m_A_15", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_brk_mesh, _brk_mats, (1220.0, 3350.0, 1290.0), (4.5836275220185264e-06, 90.00002291839935, 90.00012605080452), (1.0, 1.0, 1.0), "Building_Beam_Thin_3m_A2", _folder)
if a: placed += 1
else: skipped += 1

# Breakable Batch 32: BP_DM_Building_Beam_Horizontal_3M_B (25 instances)
#   BP Class: /Game/LevelDesign/Deco_Architecture/Suburbs/BP_DM_Building_Beam_Horizontal_3M_B
_brk_mesh = "/Game/Art/Assets/Kits/Deco_Architecture/Suburbs/Building_Beam_Horizontal_3M_B"
_brk_mats = ['/Game/Art/Assets/Kits/Deco_Architecture/Suburbs/Materials/Building_Wood_Interior/MI_Building_Wood_Interior_C_Mat']
a = spawn_static_mesh(_brk_mesh, _brk_mats, (2450.0, 3660.0, 1020.0), (0.0, 0.0006103514960302793, -0.0), (1.0, 1.0, 1.0), "Building_Beam_Horizontal_3M_B11", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_brk_mesh, _brk_mats, (2750.0, 3660.0, 1020.0), (0.0, 0.0006103514960302793, -0.0), (1.0, 1.0, 1.0), "Building_Beam_Horizontal_3M_B12_32", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_brk_mesh, _brk_mats, (2175.0, 3660.0, 1020.0), (0.0, 0.0006103514960302793, -0.0), (1.0, 1.0, 1.0), "Building_Beam_Horizontal_3M_B13", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_brk_mesh, _brk_mats, (2450.0, 3660.0, 1280.0), (0.0, 0.0006103515418669031, -0.0), (1.0, 1.0, 1.0), "Building_Beam_Horizontal_3M_B15", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_brk_mesh, _brk_mats, (2750.0, 3660.0, 1280.0), (0.0, 0.0006100000093412585, -0.0), (1.0, 1.0, 1.0), "Building_Beam_Horizontal_3M_B16", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_brk_mesh, _brk_mats, (2950.0, 3450.0, 1030.0), (0.0, -89.99945205658098, 0.0), (1.0, 1.0, 1.0), "Building_Beam_Horizontal_3M_B21", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_brk_mesh, _brk_mats, (3460.0, 4675.0, 1020.0), (0.0, 90.00072258395141, -0.0), (1.0, 1.0, 1.0), "Building_Beam_Horizontal_3M_B22", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_brk_mesh, _brk_mats, (3460.0, 4950.0, 1020.0), (0.0, 90.00072258395141, -0.0), (1.0, 1.0, 1.0), "Building_Beam_Horizontal_3M_B23", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_brk_mesh, _brk_mats, (3460.0, 4675.0, 1275.0), (0.0, 90.00072258395141, -0.0), (1.0, 1.0, 1.0), "Building_Beam_Horizontal_3M_B24", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_brk_mesh, _brk_mats, (2040.0, 3795.0, 1020.0), (0.0, -89.99945205658098, 0.0), (1.0, 1.0, 1.0), "Building_Beam_Horizontal_3M_B25", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_brk_mesh, _brk_mats, (2040.0, 4070.0, 1020.0), (0.0, -89.99945205658098, 0.0), (1.0, 1.0, 1.0), "Building_Beam_Horizontal_3M_B26_3", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_brk_mesh, _brk_mats, (2040.0, 4375.0, 1020.0), (0.0, -89.99945205658098, 0.0), (1.0, 1.0, 1.0), "Building_Beam_Horizontal_3M_B27_5", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_brk_mesh, _brk_mats, (2040.0, 4675.0, 1020.0), (0.0, -89.99945205658098, 0.0), (1.0, 1.0, 1.0), "Building_Beam_Horizontal_3M_B28_7", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_brk_mesh, _brk_mats, (2045.0, 4950.0, 1020.0), (0.0, -89.99945205658098, 0.0), (1.0, 1.0, 1.0), "Building_Beam_Horizontal_3M_B29_9", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_brk_mesh, _brk_mats, (2035.0, 4070.0, 1275.0), (0.0, -89.99945205658098, 0.0), (1.0, 1.0, 1.0), "Building_Beam_Horizontal_3M_B30_13", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_brk_mesh, _brk_mats, (2035.0, 4375.0, 1275.0), (0.0, -89.99945205658098, 0.0), (1.0, 1.0, 1.0), "Building_Beam_Horizontal_3M_B31", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_brk_mesh, _brk_mats, (2035.0, 4675.0, 1275.0), (0.0, -89.99945205658098, 0.0), (1.0, 1.0, 1.0), "Building_Beam_Horizontal_3M_B32", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_brk_mesh, _brk_mats, (3460.0, 3755.0, 1275.0), (0.0, 90.00072258395141, -0.0), (1.0, 1.0, 1.0), "Building_Beam_Horizontal_3M_B33", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_brk_mesh, _brk_mats, (3460.0, 3455.0, 1275.0), (0.0, 90.00072258395141, -0.0), (1.0, 1.0, 1.0), "Building_Beam_Horizontal_3M_B34", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_brk_mesh, _brk_mats, (2950.0, 3450.0, 1270.0), (0.0, -89.99945205658098, 0.0), (1.0, 1.0, 1.0), "Building_Beam_Horizontal_3M_B35", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_brk_mesh, _brk_mats, (3460.0, 3755.0, 1025.0), (0.0, 90.00072258395141, -0.0), (1.0, 1.0, 1.0), "Building_Beam_Horizontal_3M_B36", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_brk_mesh, _brk_mats, (3460.0, 3455.0, 1025.0), (0.0, 90.00072258395141, -0.0), (1.0, 1.0, 1.0), "Building_Beam_Horizontal_3M_B37_22", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_brk_mesh, _brk_mats, (3412.456, 4453.586, 615.0796), (0.056756057396827715, 90.56855377187775, -68.70303778555983), (1.0, 1.0, 1.0), "Building_Beam_Horizontal_3M_B38_24", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_brk_mesh, _brk_mats, (2160.0, 5080.0, 1020.0), (0.0, -179.99950822623498, 0.0), (1.0, 1.0, 1.0), "Building_Beam_Horizontal_3M_B44", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_brk_mesh, _brk_mats, (3325.0, 5080.0, 1020.0), (0.0, -179.99950822623498, 0.0), (1.0, 1.0, 1.0), "Building_Beam_Horizontal_3M_B45", _folder)
if a: placed += 1
else: skipped += 1

# Breakable Batch 33: BP_DM_Building_Beam_Thick_Base_A_B (2 instances)
#   BP Class: /Game/LevelDesign/Deco_Architecture/Suburbs/BP_DM_Building_Beam_Thick_Base_A_B
_brk_mesh = "/Game/Art/Assets/Kits/Deco_Architecture/Suburbs/Building_Beam_Thick_Base_A_B"
_brk_mats = ['/Game/Art/Assets/Kits/Deco_Architecture/Suburbs/Materials/Building_Wood_Interior/MI_Building_Wood_Interior_B_Mat']
a = spawn_static_mesh(_brk_mesh, _brk_mats, (2920.0, 750.0, 1300.0), (0.0, 0.0, -0.0), (1.0, 1.0, 1.0), "BP_DM_Building_Beam_Thick_Base_A_B10", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_brk_mesh, _brk_mats, (2920.0, 1050.0, 1300.0), (0.0, 0.0, -0.0), (1.0, 1.0, 1.0), "BP_DM_Building_Beam_Thick_Base_A_B4", _folder)
if a: placed += 1
else: skipped += 1

# Breakable Batch 34: BP_DM_Building_Beam_Thick_Deco_A_C (6 instances)
#   BP Class: /Game/LevelDesign/Deco_Architecture/Suburbs/BP_DM_Building_Beam_Thick_Deco_A_C
_brk_mesh = "/Game/Art/Assets/Kits/Deco_Architecture/Suburbs/Building_Beam_Thick_Deco_A_C"
_brk_mats = ['/Game/Art/Assets/Kits/Deco_Architecture/Suburbs/Materials/Building_Wood_Interior/MI_Building_Wood_Interior_B_Mat']
a = spawn_static_mesh(_brk_mesh, _brk_mats, (3200.0, 750.0, 1355.0), (90.0, 0.0, 0.0), (0.78125, 0.78125, 1.0), "BP_DM_Building_Beam_Thick_Deco_A_C13", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_brk_mesh, _brk_mats, (2990.0, 750.0, 1355.0), (90.0, 0.0, 0.0), (0.78125, 0.78125, 1.0), "BP_DM_Building_Beam_Thick_Deco_A_C14", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_brk_mesh, _brk_mats, (3410.0, 750.0, 1355.0), (90.0, 0.0, 0.0), (0.78125, 0.78125, 1.0), "BP_DM_Building_Beam_Thick_Deco_A_C15", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_brk_mesh, _brk_mats, (3200.0, 1050.0, 1355.0), (90.0, 0.0, 0.0), (0.78125, 0.78125, 1.0), "BP_DM_Building_Beam_Thick_Deco_A_C7", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_brk_mesh, _brk_mats, (2990.0, 1050.0, 1355.0), (90.0, 0.0, 0.0), (0.78125, 0.78125, 1.0), "BP_DM_Building_Beam_Thick_Deco_A_C8", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_brk_mesh, _brk_mats, (3410.0, 1050.0, 1355.0), (90.0, 0.0, 0.0), (0.78125, 0.78125, 1.0), "BP_DM_Building_Beam_Thick_Deco_A_C9", _folder)
if a: placed += 1
else: skipped += 1

# Breakable Batch 35: BP_DM_Building_Ceiling_Post_Arch (2 instances)
#   BP Class: /Game/LevelDesign/Deco_Architecture/Suburbs/BP_DM_Building_Ceiling_Post_Arch
_brk_mesh = "/Game/Art/Assets/Kits/Deco_Architecture/Suburbs/Building_Ceiling_Post_Arch"
_brk_mats = ['/Game/Art/Assets/Kits/Deco_Architecture/Suburbs/Materials/Building_Wood_Interior/MI_Building_Wood_Interior_C_Mat']
a = spawn_static_mesh(_brk_mesh, _brk_mats, (1220.0, 3480.0, 1280.0), (0.0, 90.00007597449323, -0.0), (1.0, 1.0, 1.0), "Building_Ceiling_Post_Arch_19", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_brk_mesh, _brk_mats, (1220.0, 2920.0, 1280.0), (0.0, -90.00018131163026, 0.0), (1.0, 1.0, 1.0), "Building_Ceiling_Post_Arch2", _folder)
if a: placed += 1
else: skipped += 1

# --- Extra DecoVolumes (not construction blocks) ---
_folder = "Reconstruction/BD_BB_OrcPrison/DecoVolumes"

# DecoVolume: AB_Orc_Scaffolding_Pallet_2x2m_B_2 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (3269.9995, 3118.337, 659.7124), (0.0, 0.0, -0.0), (2.3230, 2.2786, 1.3047), "DV_AB_Orc_Scaffolding_Pallet_2x2m_B_2_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_DM_Building_Arch_Thin_A10 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (2969.1304, 750.0651, 1325.9841), (0.0, 0.0, -0.0), (0.5935, 0.1500, 0.6803), "DV_BP_DM_Building_Arch_Thin_A10_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_DM_Building_Arch_Thin_A4 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (2969.1304, 1050.065, 1325.9841), (0.0, 0.0, -0.0), (0.5935, 0.1500, 0.6803), "DV_BP_DM_Building_Arch_Thin_A4_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_DM_Building_Beam_Horizontal_3M_A10 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (3050.0, 750.0, 1351.5245), (0.0, 0.0, -0.0), (3.0000, 0.3112, 0.2065), "DV_BP_DM_Building_Beam_Horizontal_3M_A10_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_DM_Building_Beam_Horizontal_3M_A13 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (3200.0, 4665.0, 1281.5245), (0.0, 0.0, -0.0), (0.3112, 3.0000, 0.2065), "DV_BP_DM_Building_Beam_Horizontal_3M_A13_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_DM_Building_Beam_Horizontal_3M_A14 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (2450.0, 3920.0, 1281.5245), (0.0, 0.0, -0.0), (3.0000, 0.3112, 0.2065), "DV_BP_DM_Building_Beam_Horizontal_3M_A14_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_DM_Building_Beam_Horizontal_3M_A15 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (2750.0, 3920.0, 1281.5245), (0.0, 0.0, -0.0), (3.0000, 0.3112, 0.2065), "DV_BP_DM_Building_Beam_Horizontal_3M_A15_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_DM_Building_Beam_Horizontal_3M_A16 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (3050.0, 3920.0, 1281.5245), (0.0, 0.0, -0.0), (3.0000, 0.3112, 0.2065), "DV_BP_DM_Building_Beam_Horizontal_3M_A16_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_DM_Building_Beam_Horizontal_3M_A17 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (2290.0, 4075.0, 1281.5245), (0.0, 0.0, -0.0), (0.3112, 3.0000, 0.2065), "DV_BP_DM_Building_Beam_Horizontal_3M_A17_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_DM_Building_Beam_Horizontal_3M_A18 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (2290.0, 4375.0, 1281.5245), (0.0, 0.0, -0.0), (0.3112, 3.0000, 0.2065), "DV_BP_DM_Building_Beam_Horizontal_3M_A18_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_DM_Building_Beam_Horizontal_3M_A19 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (2290.0, 4675.0, 1281.5245), (0.0, 0.0, -0.0), (0.3112, 3.0000, 0.2065), "DV_BP_DM_Building_Beam_Horizontal_3M_A19_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_DM_Building_Beam_Horizontal_3M_A5 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (3350.0, 1050.0, 1351.5245), (0.0, 0.0, -0.0), (3.0000, 0.3112, 0.2065), "DV_BP_DM_Building_Beam_Horizontal_3M_A5_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_DM_Building_Beam_Horizontal_3M_A6 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (3050.0, 1050.0, 1351.5245), (0.0, 0.0, -0.0), (3.0000, 0.3112, 0.2065), "DV_BP_DM_Building_Beam_Horizontal_3M_A6_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_DM_Building_Beam_Horizontal_3M_A9 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (3350.0, 750.0, 1351.5245), (0.0, 0.0, -0.0), (3.0000, 0.3112, 0.2065), "DV_BP_DM_Building_Beam_Horizontal_3M_A9_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_DM_Building_Beam_Thick_Base_A_B10 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (2920.0, 750.0, 1350.0), (0.0, 0.0, -0.0), (0.6306, 0.6898, 1.0000), "DV_BP_DM_Building_Beam_Thick_Base_A_B10_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_DM_Building_Beam_Thick_Base_A_B4 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (2920.0, 1050.0, 1350.0), (0.0, 0.0, -0.0), (0.6306, 0.6898, 1.0000), "DV_BP_DM_Building_Beam_Thick_Base_A_B4_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_DM_Building_Beam_Thick_Deco_A_C13 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (3200.0, 750.0, 1355.0), (0.0, 0.0, -0.0), (0.1841, 0.3546, 0.3546), "DV_BP_DM_Building_Beam_Thick_Deco_A_C13_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_DM_Building_Beam_Thick_Deco_A_C14 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (2990.0, 750.0, 1355.0), (0.0, 0.0, -0.0), (0.1841, 0.3546, 0.3546), "DV_BP_DM_Building_Beam_Thick_Deco_A_C14_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_DM_Building_Beam_Thick_Deco_A_C15 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (3410.0, 750.0, 1355.0), (0.0, 0.0, -0.0), (0.1841, 0.3546, 0.3546), "DV_BP_DM_Building_Beam_Thick_Deco_A_C15_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_DM_Building_Beam_Thick_Deco_A_C7 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (3200.0, 1050.0, 1355.0), (0.0, 0.0, -0.0), (0.1841, 0.3546, 0.3546), "DV_BP_DM_Building_Beam_Thick_Deco_A_C7_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_DM_Building_Beam_Thick_Deco_A_C8 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (2990.0, 1050.0, 1355.0), (0.0, 0.0, -0.0), (0.1841, 0.3546, 0.3546), "DV_BP_DM_Building_Beam_Thick_Deco_A_C8_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_DM_Building_Beam_Thick_Deco_A_C9 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (3410.0, 1050.0, 1355.0), (0.0, 0.0, -0.0), (0.1841, 0.3546, 0.3546), "DV_BP_DM_Building_Beam_Thick_Deco_A_C9_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_DM_Deco_Orc_3x3_A_Breakable_2 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (4187.3496, 2270.2568, 778.659), (0.0, 0.0, -0.0), (3.7016, 4.1042, 1.6768), "DV_BP_DM_Deco_Orc_3x3_A_Breakable_2_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_DM_Deco_Orc_3x3_B_Breakable_8 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (4697.649, 4361.8604, 639.6704), (0.0, 0.0, -0.0), (3.6398, 3.5329, 1.8710), "DV_BP_DM_Deco_Orc_3x3_B_Breakable_8_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_DM_Orc_Shanty_Midden_A_A_Breakable_2 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (4798.907, 4061.0698, 626.57874), (0.0, 0.0, -0.0), (3.8047, 3.8980, 0.6708), "DV_BP_DM_Orc_Shanty_Midden_A_A_Breakable_2_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_DM_Orc_Shanty_Midden_A_B_Breakable_2 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (4793.764, 4248.773, 623.3614), (0.0, 0.0, -0.0), (3.3076, 3.5468, 0.5886), "DV_BP_DM_Orc_Shanty_Midden_A_B_Breakable_2_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_DM_Orc_Shanty_Midden_A_C_Breakable_2 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (4806.165, 4397.272, 614.09576), (0.0, 0.0, -0.0), (2.4860, 2.6895, 0.4328), "DV_BP_DM_Orc_Shanty_Midden_A_C_Breakable_2_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_DM_Orc_Shanty_Midden_C_A_Breakable_2 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (4673.1997, 4531.019, 622.5377), (0.0, 0.0, -0.0), (3.4994, 3.5343, 0.7801), "DV_BP_DM_Orc_Shanty_Midden_C_A_Breakable_2_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_DM_Orc_Shanty_Midden_C_D_Breakable10 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (4892.3076, 2386.4546, 709.5896), (0.0, 0.0, -0.0), (2.7898, 2.8239, 0.5166), "DV_BP_DM_Orc_Shanty_Midden_C_D_Breakable10_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_DM_Orc_Shanty_Midden_C_D_Breakable14 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (1162.6849, 5070.883, 716.2233), (0.0, 0.0, -0.0), (2.8172, 2.8981, 0.5166), "DV_BP_DM_Orc_Shanty_Midden_C_D_Breakable14_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_DM_Orc_Shanty_Midden_C_D_Breakable18 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (1770.1353, 5652.0317, 714.6307), (0.0, 0.0, -0.0), (2.1188, 2.0601, 0.7488), "DV_BP_DM_Orc_Shanty_Midden_C_D_Breakable18_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_DM_Orc_Shanty_Midden_C_D_Breakable19 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (1849.5337, 5619.4175, 718.1174), (0.0, 0.0, -0.0), (2.8208, 2.8013, 0.6559), "DV_BP_DM_Orc_Shanty_Midden_C_D_Breakable19_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_DM_Orc_Shanty_Midden_C_D_Breakable2_5 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (3821.2556, 4423.491, 608.6572), (0.0, 0.0, -0.0), (2.0396, 2.1102, 0.5166), "DV_BP_DM_Orc_Shanty_Midden_C_D_Breakable2_5_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_DM_Orc_Shanty_Midden_C_D_Breakable3_8 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (4596.7285, 4600.5615, 611.6572), (0.0, 0.0, -0.0), (2.8515, 2.8087, 0.5166), "DV_BP_DM_Orc_Shanty_Midden_C_D_Breakable3_8_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_DM_Orc_Shanty_Midden_C_D_Breakable6_2 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (4357.7324, 2227.9517, 711.3069), (0.0, 0.0, -0.0), (2.8059, 2.8947, 0.5166), "DV_BP_DM_Orc_Shanty_Midden_C_D_Breakable6_2_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_DM_Orc_Shanty_Midden_C_D_Breakable7 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (4286.7915, 2336.7036, 709.5896), (0.0, 0.0, -0.0), (2.4168, 2.2158, 0.5166), "DV_BP_DM_Orc_Shanty_Midden_C_D_Breakable7_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_DM_Orc_Shanty_Midden_C_D_Breakable8 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (4872.564, 2336.7036, 709.5896), (0.0, 0.0, -0.0), (2.4168, 2.2158, 0.5166), "DV_BP_DM_Orc_Shanty_Midden_C_D_Breakable8_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_DM_Orc_Shanty_Midden_C_D_Breakable9 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (4787.203, 2305.7598, 709.5896), (0.0, 0.0, -0.0), (2.7425, 2.8595, 0.5166), "DV_BP_DM_Orc_Shanty_Midden_C_D_Breakable9_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_DM_Orc_Shanty_Midden_D_A_Breakable_2 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (4646.9155, 4137.932, 603.8209), (0.0, 0.0, -0.0), (1.6833, 1.4846, 0.2038), "DV_BP_DM_Orc_Shanty_Midden_D_A_Breakable_2_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_DM_Orc_Shanty_Midden_D_A_Breakable2_2 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (4538.511, 4496.663, 603.8209), (0.0, 0.0, -0.0), (1.8158, 1.9664, 0.2038), "DV_BP_DM_Orc_Shanty_Midden_D_A_Breakable2_2_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_DM_Orc_Shanty_Midden_D_A_Breakable4_2 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (4382.4727, 2289.5503, 708.1467), (0.0, 0.0, -0.0), (1.6833, 1.4846, 0.2038), "DV_BP_DM_Orc_Shanty_Midden_D_A_Breakable4_2_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_DM_Orc_Shanty_Midden_D_B_Breakable_2 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (4644.096, 4240.777, 600.28644), (0.0, 0.0, -0.0), (1.4028, 1.2372, 0.1871), "DV_BP_DM_Orc_Shanty_Midden_D_B_Breakable_2_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_DM_Orc_Shanty_Midden_D_B_Breakable2_5 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (4664.096, 4413.777, 608.11096), (0.0, 0.0, -0.0), (1.4028, 1.2372, 0.1871), "DV_BP_DM_Orc_Shanty_Midden_D_B_Breakable2_5_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_DM_Orc_Shanty_Midden_D_C_Breakable2_5 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (3902.0422, 4333.4893, 606.5438), (0.0, 0.0, -0.0), (2.0410, 2.0417, 0.3356), "DV_BP_DM_Orc_Shanty_Midden_D_C_Breakable2_5_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_DM_Remains_Bones_Assemblage_A_Breakable_2 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (4601.5923, 3947.6821, 608.1855), (0.0, 0.0, -0.0), (0.4808, 0.7146, 0.1824), "DV_BP_DM_Remains_Bones_Assemblage_A_Breakable_2_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_DM_Remains_Bones_Assemblage_A_Breakable2_5 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (4055.8794, 3952.612, 611.0547), (0.0, 0.0, -0.0), (0.8626, 0.8466, 0.2805), "DV_BP_DM_Remains_Bones_Assemblage_A_Breakable2_5_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_DM_Remains_Bones_Assemblage_B_Breakable_2 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (4601.1514, 4048.3567, 603.9221), (0.0, 0.0, -0.0), (0.3187, 0.4137, 0.0986), "DV_BP_DM_Remains_Bones_Assemblage_B_Breakable_2_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_DM_Remains_Bones_Assemblage_B_Breakable2_5 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (4599.1523, 3998.1814, 603.9221), (0.0, 0.0, -0.0), (0.5176, 0.4828, 0.0986), "DV_BP_DM_Remains_Bones_Assemblage_B_Breakable2_5_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_DM_Remains_Bones_Assemblage_B_Breakable3_8 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (4095.434, 3927.4368, 615.4856), (0.0, 0.0, -0.0), (0.3187, 0.4247, 0.1719), "DV_BP_DM_Remains_Bones_Assemblage_B_Breakable3_8_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_DM_Remains_Bones_Assemblage_B_Breakable6_8 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (932.29877, 5024.6143, 708.80597), (0.0, 0.0, -0.0), (0.5189, 0.4866, 0.0986), "DV_BP_DM_Remains_Bones_Assemblage_B_Breakable6_8_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_DM_Remains_Bones_Assemblage_C_Breakable_2 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (4647.9053, 4102.029, 608.8794), (0.0, 0.0, -0.0), (0.7663, 0.7594, 0.1992), "DV_BP_DM_Remains_Bones_Assemblage_C_Breakable_2_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_DM_Remains_Bones_Assemblage_C_Breakable2_5 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (3825.9424, 3915.87, 625.90424), (0.0, 0.0, -0.0), (0.8029, 0.7858, 0.4936), "DV_BP_DM_Remains_Bones_Assemblage_C_Breakable2_5_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_DM_Remains_Bones_Assemblage_C_Breakable4_5 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (1052.3607, 5013.512, 712.6096), (0.0, 0.0, -0.0), (1.0562, 1.0554, 0.2638), "DV_BP_DM_Remains_Bones_Assemblage_C_Breakable4_5_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_DM_Remains_Bones_Assemblage_C_Breakable6 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (1791.4917, 5595.038, 714.38324), (0.0, 0.0, -0.0), (1.0844, 1.0806, 0.2369), "DV_BP_DM_Remains_Bones_Assemblage_C_Breakable6_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_DM_Remains_Bones_Assemblage_C_Breakable7 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (744.3635, 5012.476, 721.98254), (0.0, 0.0, -0.0), (1.0564, 1.0637, 0.3498), "DV_BP_DM_Remains_Bones_Assemblage_C_Breakable7_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_DM_Rubble_Masonry_large_A_Breakable_5 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (2844.3093, 5050.5356, 634.8286), (0.0, 0.0, -0.0), (3.0374, 2.7533, 0.8714), "DV_BP_DM_Rubble_Masonry_large_A_Breakable_5_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_DM_Rubble_Masonry_large_A_Breakable10 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (3430.16, 3194.6292, 635.50055), (0.0, 0.0, -0.0), (2.6082, 3.0232, 0.7394), "DV_BP_DM_Rubble_Masonry_large_A_Breakable10_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_DM_Rubble_Masonry_large_A_Breakable12_24 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (1455.5554, 2869.0642, 732.37366), (0.0, 0.0, -0.0), (2.8818, 2.1999, 0.6509), "DV_BP_DM_Rubble_Masonry_large_A_Breakable12_24_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_DM_Rubble_Masonry_large_A_Breakable13 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (1442.3071, 3443.1162, 732.37366), (0.0, 0.0, -0.0), (2.8341, 2.0937, 0.6509), "DV_BP_DM_Rubble_Masonry_large_A_Breakable13_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_DM_Rubble_Masonry_large_A_Breakable14 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (1105.6256, 3703.5686, 831.26807), (0.0, 0.0, -0.0), (2.0447, 2.8105, 0.6509), "DV_BP_DM_Rubble_Masonry_large_A_Breakable14_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_DM_Rubble_Masonry_large_A_Breakable15 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (1656.1498, 2858.8115, 732.37366), (0.0, 0.0, -0.0), (2.6628, 1.7690, 0.6509), "DV_BP_DM_Rubble_Masonry_large_A_Breakable15_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_DM_Rubble_Masonry_large_A_Breakable3_2 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (2966.0205, 1200.3195, 829.37915), (0.0, 0.0, -0.0), (1.5925, 2.5568, 0.6509), "DV_BP_DM_Rubble_Masonry_large_A_Breakable3_2_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_DM_Rubble_Masonry_large_A_Breakable4 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (2699.6807, 1166.0199, 829.37915), (0.0, 0.0, -0.0), (2.5568, 1.5925, 0.6509), "DV_BP_DM_Rubble_Masonry_large_A_Breakable4_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_DM_Rubble_Masonry_large_A_Breakable6_2 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (2688.3582, 5035.302, 631.2627), (0.0, 0.0, -0.0), (2.8634, 2.9822, 0.6509), "DV_BP_DM_Rubble_Masonry_large_A_Breakable6_2_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_DM_Rubble_Masonry_large_A_Breakable7_8 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (3460.3752, 4399.7524, 621.47974), (0.0, 0.0, -0.0), (1.9612, 2.7684, 0.6509), "DV_BP_DM_Rubble_Masonry_large_A_Breakable7_8_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_DM_Rubble_Masonry_large_A_Breakable8_14 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (3882.9348, 2067.7837, 740.2445), (0.0, 0.0, -0.0), (2.8321, 2.0896, 0.6509), "DV_BP_DM_Rubble_Masonry_large_A_Breakable8_14_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_DM_Rubble_Masonry_large_A_Breakable9_17 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (2980.251, 3239.6091, 623.2904), (0.0, 0.0, -0.0), (2.4366, 2.9853, 0.7394), "DV_BP_DM_Rubble_Masonry_large_A_Breakable9_17_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_DM_Rubble_Masonry_large_C_Breakable2_2 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (2612.9712, 5077.3423, 681.13074), (0.0, 0.0, -0.0), (2.2961, 1.7867, 0.9324), "DV_BP_DM_Rubble_Masonry_large_C_Breakable2_2_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_DM_Rubble_Masonry_large_C_Breakable3_8 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (3680.4832, 4395.75, 640.5962), (0.0, 0.0, -0.0), (1.9985, 2.3313, 0.9324), "DV_BP_DM_Rubble_Masonry_large_C_Breakable3_8_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_DM_Rubble_Masonry_large_C_Breakable4_11 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (3677.888, 3918.9026, 643.8913), (0.0, 0.0, -0.0), (2.2508, 2.2540, 0.9324), "DV_BP_DM_Rubble_Masonry_large_C_Breakable4_11_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_DM_Rubble_Masonry_large_D_Breakable_2 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (2637.223, 5040.3335, 635.07227), (0.0, 0.0, -0.0), (1.9676, 1.1175, 0.7186), "DV_BP_DM_Rubble_Masonry_large_D_Breakable_2_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_DM_Rubble_Masonry_large_D_Breakable2_8 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (4116.344, 2189.5786, 731.6699), (0.0, 0.0, -0.0), (2.2239, 2.1240, 0.7186), "DV_BP_DM_Rubble_Masonry_large_D_Breakable2_8_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_DM_Rubble_Masonry_large_D_Breakable3_14 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (3493.101, 1078.9866, 826.8273), (0.0, 0.0, -0.0), (1.4792, 2.1475, 0.7186), "DV_BP_DM_Rubble_Masonry_large_D_Breakable3_14_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_DM_Rubble_Masonry_large_E_Breakable_2 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (3933.8171, 2123.3687, 738.203), (0.0, 0.0, -0.0), (1.6346, 2.5781, 0.7478), "DV_BP_DM_Rubble_Masonry_large_E_Breakable_2_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_DM_Rubble_Masonry_large_F_Breakable2_5 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (3915.7449, 2805.5015, 753.1968), (0.0, 0.0, -0.0), (2.1875, 2.5617, 1.1332), "DV_BP_DM_Rubble_Masonry_large_F_Breakable2_5_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_DM_Rubble_Masonry_large_F_Breakable3_2 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (3449.246, 3965.9795, 639.5476), (0.0, 0.0, -0.0), (1.4857, 2.1727, 1.1332), "DV_BP_DM_Rubble_Masonry_large_F_Breakable3_2_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_DM_Rubble_Masonry_Mound_Pile_F_Breakable_8 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (3356.9736, 3793.663, 622.8193), (0.0, 0.0, -0.0), (1.4080, 1.2372, 0.4827), "DV_BP_DM_Rubble_Masonry_Mound_Pile_F_Breakable_8_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_DM_Rubble_Masonry_Pile_A_Breakable_2 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (3454.8225, 1435.6967, 869.4277), (0.0, 0.0, -0.0), (1.1677, 1.2743, 1.4244), "DV_BP_DM_Rubble_Masonry_Pile_A_Breakable_2_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_DM_Rubble_Masonry_Pile_C_Breakable_17 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (3426.9983, 3684.9453, 639.7754), (0.0, 0.0, -0.0), (2.3102, 2.3653, 0.9351), "DV_BP_DM_Rubble_Masonry_Pile_C_Breakable_17_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_DM_Rubble_Masonry_Pile_C_Breakable2_20 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (2222.7708, 2318.1626, 732.5918), (0.0, 0.0, -0.0), (2.5724, 2.4908, 1.1994), "DV_BP_DM_Rubble_Masonry_Pile_C_Breakable2_20_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_DM_Rubble_Masonry_Pile_C_Breakable3_23 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (3891.267, 2743.46, 738.2897), (0.0, 0.0, -0.0), (2.4896, 2.4455, 0.9351), "DV_BP_DM_Rubble_Masonry_Pile_C_Breakable3_23_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_DM_Rubble_Masonry_Pile_C_Breakable4_27 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (1759.5719, 2617.467, 737.0299), (0.0, 0.0, -0.0), (2.6756, 2.6635, 0.9351), "DV_BP_DM_Rubble_Masonry_Pile_C_Breakable4_27_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_DM_Rubble_Masonry_Pile_E_Breakable_2 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (2965.1978, 5114.567, 670.62225), (0.0, 0.0, -0.0), (2.5083, 2.5557, 1.9920), "DV_BP_DM_Rubble_Masonry_Pile_E_Breakable_2_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_DM_Rubble_Masonry_Pile_F_Breakable_17 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (2530.7969, 2143.1562, 735.6118), (0.0, 0.0, -0.0), (5.9483, 5.9938, 1.3764), "DV_BP_DM_Rubble_Masonry_Pile_F_Breakable_17_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_DM_Rubble_Masonry_Pile_H_Breakable_2 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (2458.9753, 5011.988, 635.927), (0.0, 0.0, -0.0), (3.1028, 2.5859, 1.3071), "DV_BP_DM_Rubble_Masonry_Pile_H_Breakable_2_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_DM_Warren_Lighting_Torch_A_B_Breakable_2 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (3429.0776, 1733.8542, 841.83966), (0.0, 0.0, -0.0), (1.0784, 1.3013, 0.8036), "DV_BP_DM_Warren_Lighting_Torch_A_B_Breakable_2_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_DM_Warren_Lighting_Torch_A_B_Breakable2 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (2999.275, 1720.4783, 840.3659), (0.0, 0.0, -0.0), (0.9789, 1.1167, 0.8036), "DV_BP_DM_Warren_Lighting_Torch_A_B_Breakable2_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_DM_Warren_Lighting_Torch_B_Breakable_2 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (1842.5293, 4987.5938, 746.1473), (0.0, 0.0, -0.0), (1.3059, 1.3062, 0.9678), "DV_BP_DM_Warren_Lighting_Torch_B_Breakable_2_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_DM_Warren_Lighting_Torch_B_Breakable2 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (1377.4783, 5022.5938, 746.1473), (0.0, 0.0, -0.0), (1.3059, 1.3062, 0.9678), "DV_BP_DM_Warren_Lighting_Torch_B_Breakable2_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_DM_Warren_Lighting_Torch_B_Breakable3 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (1377.4783, 4567.5938, 746.1473), (0.0, 0.0, -0.0), (1.3059, 1.3062, 0.9678), "DV_BP_DM_Warren_Lighting_Torch_B_Breakable3_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_DM_Warren_Lighting_Torch_Breakable_5 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (3452.8801, 2808.0103, 764.9399), (0.0, 0.0, -0.0), (1.0112, 1.0765, 1.9128), "DV_BP_DM_Warren_Lighting_Torch_Breakable_5_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_DM_Warren_Lighting_Torch_Breakable2 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (1127.0774, 3002.979, 872.8237), (0.0, 0.0, -0.0), (1.4762, 1.4762, 1.9128), "DV_BP_DM_Warren_Lighting_Torch_Breakable2_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_DM_Warren_Lighting_Torch_Breakable3 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (1853.8801, 4533.0103, 767.8237), (0.0, 0.0, -0.0), (1.0112, 1.0765, 1.9128), "DV_BP_DM_Warren_Lighting_Torch_Breakable3_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_DM_Warren_Lighting_Torch_Breakable4 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (3886.8801, 4398.0103, 664.8237), (0.0, 0.0, -0.0), (1.0112, 1.0765, 1.9128), "DV_BP_DM_Warren_Lighting_Torch_Breakable4_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_DM_Warren_Lighting_Torch_Breakable5 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (2995.281, 2816.5688, 767.714), (0.0, 0.0, -0.0), (1.2537, 1.3001, 1.9128), "DV_BP_DM_Warren_Lighting_Torch_Breakable5_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_DM_Warren_Lighting_Torch_Breakable6 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (1141.8801, 3406.0103, 872.8237), (0.0, 0.0, -0.0), (1.0112, 1.0765, 1.9128), "DV_BP_DM_Warren_Lighting_Torch_Breakable6_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_DM_Warren_Lighting_Torch_D_Breakable_2 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (1906.1101, 3228.1707, 738.3296), (0.0, 0.0, -0.0), (1.3695, 1.4668, 0.7864), "DV_BP_DM_Warren_Lighting_Torch_D_Breakable_2_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_DM_Warren_Lighting_Torch_D_Breakable2_2 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (4936.345, 2401.2683, 731.45593), (0.0, 0.0, -0.0), (1.3695, 1.4668, 0.7864), "DV_BP_DM_Warren_Lighting_Torch_D_Breakable2_2_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_Orc_Scaffolding_Post_1m_A_5 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (3045.4324, 5098.736, 846.1853), (0.0, 0.0, -0.0), (0.2821, 0.9340, 0.9340), "DV_BP_Orc_Scaffolding_Post_1m_A_5_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_Orc_Scaffolding_Post_1m_A2 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (2439.5679, 5091.2637, 846.1853), (0.0, 0.0, -0.0), (0.2821, 0.9340, 0.9340), "DV_BP_Orc_Scaffolding_Post_1m_A2_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_Orc_Scaffolding_Post_1m_C_5 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (3045.0066, 5091.6177, 761.24835), (0.0, 0.0, -0.0), (0.3426, 0.9089, 1.4186), "DV_BP_Orc_Scaffolding_Post_1m_C_5_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_Orc_Scaffolding_Post_1m_C2 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (2439.9937, 5098.382, 761.24835), (0.0, 0.0, -0.0), (0.3426, 0.9089, 1.4186), "DV_BP_Orc_Scaffolding_Post_1m_C2_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_Orc_Scaffolding_Post_1m_C3_5 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (4925.7705, 2525.4736, 703.7539), (0.0, 0.0, -0.0), (1.1212, 1.4995, 0.3182), "DV_BP_Orc_Scaffolding_Post_1m_C3_5_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_Orc_Scaffolding_Post_1m_D_2 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (3024.84, 5075.4927, 694.9447), (0.0, 0.0, -0.0), (0.6363, 0.1848, 0.9932), "DV_BP_Orc_Scaffolding_Post_1m_D_2_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_Orc_Scaffolding_Post_1m_D2 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (3024.84, 5125.4927, 694.9447), (0.0, 0.0, -0.0), (0.6363, 0.1848, 0.9932), "DV_BP_Orc_Scaffolding_Post_1m_D2_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_Orc_Scaffolding_Post_1m_D3 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (2460.1602, 5114.5073, 694.9447), (0.0, 0.0, -0.0), (0.6363, 0.1848, 0.9932), "DV_BP_Orc_Scaffolding_Post_1m_D3_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_Orc_Scaffolding_Post_1m_D4 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (2460.1602, 5064.5073, 694.9447), (0.0, 0.0, -0.0), (0.6363, 0.1848, 0.9932), "DV_BP_Orc_Scaffolding_Post_1m_D4_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_Orc_Scaffolding_Post_2m_B_5 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (3070.144, 5080.0225, 1259.6193), (0.0, 0.0, -0.0), (2.4715, 0.1382, 0.1461), "DV_BP_Orc_Scaffolding_Post_2m_B_5_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_Orc_Scaffolding_Post_2m_B2 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (2430.1443, 5085.0225, 1259.6193), (0.0, 0.0, -0.0), (2.4715, 0.1382, 0.1461), "DV_BP_Orc_Scaffolding_Post_2m_B2_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_Orc_Scaffolding_Post_2m_B3_8 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (4969.9536, 2524.7966, 704.6786), (0.0, 0.0, -0.0), (1.7462, 1.9548, 0.2756), "DV_BP_Orc_Scaffolding_Post_2m_B3_8_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_Orc_Scaffolding_Post_2m_D_5 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (4404.8955, 2272.5564, 716.18665), (0.0, 0.0, -0.0), (2.0312, 1.3175, 0.6730), "DV_BP_Orc_Scaffolding_Post_2m_D_5_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_Orc_Scaffolding_Post_3m_C_2 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (4473.8525, 2212.871, 829.53375), (0.0, 0.0, -0.0), (0.9163, 0.8871, 3.1131), "DV_BP_Orc_Scaffolding_Post_3m_C_2_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_Orc_Scaffolding_Post_3m_C2_5 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (4991.8774, 2565.1191, 706.52325), (0.0, 0.0, -0.0), (1.1139, 3.1340, 0.4274), "DV_BP_Orc_Scaffolding_Post_3m_C2_5_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_Orc_Scaffolding_Post_4m_B_5 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (3206.447, 3472.3977, 1067.1329), (0.0, 0.0, -0.0), (2.4952, 4.0241, 0.3095), "DV_BP_Orc_Scaffolding_Post_4m_B_5_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_Orc_Scaffolding_Post_5m_D_10 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (3029.638, 5065.8887, 826.83844), (0.0, 0.0, -0.0), (1.4372, 0.4808, 5.3787), "DV_BP_Orc_Scaffolding_Post_5m_D_10_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_Orc_Scaffolding_Post_5m_D2_5 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (3188.1616, 3290.017, 1058.0028), (0.0, 0.0, -0.0), (5.3787, 1.5127, 0.8365), "DV_BP_Orc_Scaffolding_Post_5m_D2_5_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_Orc_Scaffolding_Post_5m_D3 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (3201.8386, 3575.8857, 1064.361), (0.0, 0.0, -0.0), (5.3787, 1.4373, 0.4809), "DV_BP_Orc_Scaffolding_Post_5m_D3_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_Orc_Scaffolding_Post_5m_D4_12 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (3029.638, 5115.8887, 826.83844), (0.0, 0.0, -0.0), (1.4372, 0.4808, 5.3787), "DV_BP_Orc_Scaffolding_Post_5m_D4_12_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_Orc_Scaffolding_Post_5m_D5 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (2455.3616, 5124.111, 826.83844), (0.0, 0.0, -0.0), (1.4372, 0.4808, 5.3787), "DV_BP_Orc_Scaffolding_Post_5m_D5_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_Orc_Scaffolding_Post_5m_D6 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (2454.6082, 5075.9844, 826.83844), (0.0, 0.0, -0.0), (1.4692, 0.5871, 5.3787), "DV_BP_Orc_Scaffolding_Post_5m_D6_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_Orc_Scaffolding_Post_Deco_D2_5 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (3062.1807, 3309.8115, 1007.5482), (0.0, 0.0, -0.0), (2.1801, 0.5868, 1.8793), "DV_BP_Orc_Scaffolding_Post_Deco_D2_5_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_Orc_Scaffolding_Post_Deco_D3 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (3337.8193, 3290.1882, 1007.5482), (0.0, 0.0, -0.0), (2.1801, 0.5868, 1.8793), "DV_BP_Orc_Scaffolding_Post_Deco_D3_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_Orc_Scaffolding_Post_Deco_D4 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (3062.1807, 3604.8115, 1007.5482), (0.0, 0.0, -0.0), (2.1801, 0.5868, 1.8793), "DV_BP_Orc_Scaffolding_Post_Deco_D4_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_Orc_Scaffolding_Post_Deco_D5 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (3337.8193, 3585.1882, 1007.5482), (0.0, 0.0, -0.0), (2.1801, 0.5868, 1.8793), "DV_BP_Orc_Scaffolding_Post_Deco_D5_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_Suburb_Stairs_Trim_3M_Breakable39 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (3950.1401, 1999.4042, 735.5397), (0.0, 0.0, -0.0), (3.0034, 0.4693, 1.2966), "DV_BP_Suburb_Stairs_Trim_3M_Breakable39_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: Building_Beam_Horizontal_3M_B11 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (2450.0, 3658.2366, 1016.92554), (0.0, 0.0, -0.0), (3.0000, 0.3112, 0.4048), "DV_Building_Beam_Horizontal_3M_B11_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: Building_Beam_Horizontal_3M_B12_32 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (2750.0, 3658.2366, 1016.92554), (0.0, 0.0, -0.0), (3.0000, 0.3112, 0.4048), "DV_Building_Beam_Horizontal_3M_B12_32_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: Building_Beam_Horizontal_3M_B13 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (2175.0, 3658.2366, 1016.92554), (0.0, 0.0, -0.0), (3.0000, 0.3112, 0.4048), "DV_Building_Beam_Horizontal_3M_B13_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: Building_Beam_Horizontal_3M_B15 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (2450.0, 3658.2366, 1276.9255), (0.0, 0.0, -0.0), (3.0000, 0.3112, 0.4048), "DV_Building_Beam_Horizontal_3M_B15_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: Building_Beam_Horizontal_3M_B16 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (2750.0, 3658.2366, 1276.9255), (0.0, 0.0, -0.0), (3.0000, 0.3112, 0.4048), "DV_Building_Beam_Horizontal_3M_B16_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: Building_Beam_Horizontal_3M_B21 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (2948.2366, 3450.0, 1026.9255), (0.0, 0.0, -0.0), (0.3112, 3.0000, 0.4048), "DV_Building_Beam_Horizontal_3M_B21_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: Building_Beam_Horizontal_3M_B22 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (3461.7634, 4675.0, 1016.92554), (0.0, 0.0, -0.0), (0.3112, 3.0000, 0.4048), "DV_Building_Beam_Horizontal_3M_B22_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: Building_Beam_Horizontal_3M_B23 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (3461.7634, 4950.0, 1016.92554), (0.0, 0.0, -0.0), (0.3112, 3.0000, 0.4048), "DV_Building_Beam_Horizontal_3M_B23_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: Building_Beam_Horizontal_3M_B24 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (3461.7634, 4675.0, 1271.9255), (0.0, 0.0, -0.0), (0.3112, 3.0000, 0.4048), "DV_Building_Beam_Horizontal_3M_B24_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: Building_Beam_Horizontal_3M_B25 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (2038.2367, 3795.0, 1016.92554), (0.0, 0.0, -0.0), (0.3112, 3.0000, 0.4048), "DV_Building_Beam_Horizontal_3M_B25_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: Building_Beam_Horizontal_3M_B26_3 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (2038.2367, 4070.0, 1016.92554), (0.0, 0.0, -0.0), (0.3112, 3.0000, 0.4048), "DV_Building_Beam_Horizontal_3M_B26_3_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: Building_Beam_Horizontal_3M_B27_5 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (2038.2367, 4375.0, 1016.92554), (0.0, 0.0, -0.0), (0.3112, 3.0000, 0.4048), "DV_Building_Beam_Horizontal_3M_B27_5_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: Building_Beam_Horizontal_3M_B28_7 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (2038.2367, 4675.0, 1016.92554), (0.0, 0.0, -0.0), (0.3112, 3.0000, 0.4048), "DV_Building_Beam_Horizontal_3M_B28_7_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: Building_Beam_Horizontal_3M_B29_9 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (2043.2367, 4950.0, 1016.92554), (0.0, 0.0, -0.0), (0.3112, 3.0000, 0.4048), "DV_Building_Beam_Horizontal_3M_B29_9_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: Building_Beam_Horizontal_3M_B30_13 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (2033.2367, 4070.0, 1271.9255), (0.0, 0.0, -0.0), (0.3112, 3.0000, 0.4048), "DV_Building_Beam_Horizontal_3M_B30_13_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: Building_Beam_Horizontal_3M_B31 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (2033.2367, 4375.0, 1271.9255), (0.0, 0.0, -0.0), (0.3112, 3.0000, 0.4048), "DV_Building_Beam_Horizontal_3M_B31_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: Building_Beam_Horizontal_3M_B32 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (2033.2367, 4675.0, 1271.9255), (0.0, 0.0, -0.0), (0.3112, 3.0000, 0.4048), "DV_Building_Beam_Horizontal_3M_B32_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: Building_Beam_Horizontal_3M_B33 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (3461.7634, 3755.0, 1271.9255), (0.0, 0.0, -0.0), (0.3112, 3.0000, 0.4048), "DV_Building_Beam_Horizontal_3M_B33_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: Building_Beam_Horizontal_3M_B34 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (3461.7634, 3455.0, 1271.9255), (0.0, 0.0, -0.0), (0.3112, 3.0000, 0.4048), "DV_Building_Beam_Horizontal_3M_B34_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: Building_Beam_Horizontal_3M_B35 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (2948.2366, 3450.0, 1266.9255), (0.0, 0.0, -0.0), (0.3112, 3.0000, 0.4048), "DV_Building_Beam_Horizontal_3M_B35_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: Building_Beam_Horizontal_3M_B36 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (3461.7634, 3755.0, 1021.92554), (0.0, 0.0, -0.0), (0.3112, 3.0000, 0.4048), "DV_Building_Beam_Horizontal_3M_B36_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: Building_Beam_Horizontal_3M_B37_22 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (3461.7634, 3455.0, 1021.92554), (0.0, 0.0, -0.0), (0.3112, 3.0000, 0.4048), "DV_Building_Beam_Horizontal_3M_B37_22_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: Building_Beam_Horizontal_3M_B38_24 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (3410.2322, 4453.5664, 612.32), (0.0, 0.0, -0.0), (0.5199, 3.0049, 0.4399), "DV_Building_Beam_Horizontal_3M_B38_24_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: Building_Beam_Horizontal_3M_B44 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (2160.0, 5081.763, 1016.92554), (0.0, 0.0, -0.0), (3.0000, 0.3112, 0.4048), "DV_Building_Beam_Horizontal_3M_B44_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: Building_Beam_Horizontal_3M_B45 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (3325.0, 5081.763, 1016.92554), (0.0, 0.0, -0.0), (3.0000, 0.3112, 0.4048), "DV_Building_Beam_Horizontal_3M_B45_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: Building_Beam_Thin_3m_A_15 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (1218.4755, 3050.0, 1290.0), (0.0, 0.0, -0.0), (0.2065, 3.0000, 0.3112), "DV_Building_Beam_Thin_3m_A_15_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: Building_Beam_Thin_3m_A2 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (1218.4755, 3350.0, 1290.0), (0.0, 0.0, -0.0), (0.2065, 3.0000, 0.3112), "DV_Building_Beam_Thin_3m_A2_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: Building_Ceiling_Post_Arch_19 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (1220.0001, 3418.121, 1203.5397), (0.0, 0.0, -0.0), (0.1556, 1.2448, 1.5292), "DV_Building_Ceiling_Post_Arch_19_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: Building_Ceiling_Post_Arch2 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (1220.0002, 2981.879, 1203.5397), (0.0, 0.0, -0.0), (0.1556, 1.2448, 1.5292), "DV_Building_Ceiling_Post_Arch2_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: Orc_Palissade_Barricade_A_8 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (1094.864, 2820.0, 805.6648), (0.0, 0.0, -0.0), (1.5157, 3.7911, 2.1414), "DV_Orc_Palissade_Barricade_A_8_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: Orc_Palissade_Barricade_A2 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (1094.864, 3545.0, 805.6648), (0.0, 0.0, -0.0), (1.5157, 3.7911, 2.1414), "DV_Orc_Palissade_Barricade_A2_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: Orc_Palissade_Barricade_A3_2 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (3030.136, 3460.0, 585.18243), (0.0, 0.0, -0.0), (1.5157, 3.7911, 2.1414), "DV_Orc_Palissade_Barricade_A3_2_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: Orc_Palissade_Barricade_A4 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (3457.0815, 3460.0, 596.23376), (0.0, 0.0, -0.0), (1.5157, 3.7911, 2.1414), "DV_Orc_Palissade_Barricade_A4_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: SM_Mines_MetalBar_Window_A10 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (1975.0065, 4668.0293, 820.89087), (0.0, 0.0, -0.0), (0.1691, 1.7273, 2.2144), "DV_SM_Mines_MetalBar_Window_A10_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: SM_Mines_MetalBar_Window_A4_164 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (1975.0065, 4073.0298, 820.89087), (0.0, 0.0, -0.0), (0.1691, 1.7273, 2.2144), "DV_SM_Mines_MetalBar_Window_A4_164_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: SM_Mines_MetalBar_Window_A7_1 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (1975.0065, 3768.0295, 820.89087), (0.0, 0.0, -0.0), (0.1691, 1.7273, 2.2144), "DV_SM_Mines_MetalBar_Window_A7_1_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: SM_Mines_MetalBar_Window_A9 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (1975.0065, 4973.0293, 820.89087), (0.0, 0.0, -0.0), (0.1691, 1.7273, 2.2144), "DV_SM_Mines_MetalBar_Window_A9_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: SM_Mines_MetalGate_4Bar_3M_A_119 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (1370.0, 4960.0, 850.0), (0.0, 0.0, -0.0), (0.1335, 1.0000, 3.0000), "DV_SM_Mines_MetalGate_4Bar_3M_A_119_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: SM_Mines_MetalGate_4Bar_3M_A10 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (3570.0, 2660.0, 850.0), (0.0, 0.0, -0.0), (0.5060, 0.9750, 3.0000), "DV_SM_Mines_MetalGate_4Bar_3M_A10_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: SM_Mines_MetalGate_4Bar_3M_A11 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (3550.0, 2750.0, 850.0), (0.0, 0.0, -0.0), (0.1335, 1.0000, 3.0000), "DV_SM_Mines_MetalGate_4Bar_3M_A11_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: SM_Mines_MetalGate_4Bar_3M_A12_205 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (2905.0, 2140.0, 855.0), (0.0, 0.0, -0.0), (0.1335, 1.0000, 3.0000), "DV_SM_Mines_MetalGate_4Bar_3M_A12_205_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: SM_Mines_MetalGate_4Bar_3M_A13 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (2905.0, 2750.0, 855.0), (0.0, 0.0, -0.0), (0.1335, 1.0000, 3.0000), "DV_SM_Mines_MetalGate_4Bar_3M_A13_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: SM_Mines_MetalGate_4Bar_3M_A14_94 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (1996.9999, 4494.9995, 937.37415), (0.0, 0.0, -0.0), (0.1335, 1.0000, 1.3125), "DV_SM_Mines_MetalGate_4Bar_3M_A14_94_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: SM_Mines_MetalGate_4Bar_3M_A15 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (1997.0005, 4254.9995, 937.3757), (0.0, 0.0, -0.0), (0.1335, 1.0000, 1.3125), "DV_SM_Mines_MetalGate_4Bar_3M_A15_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: SM_Mines_MetalGate_4Bar_3M_A2 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (1370.0, 5060.0, 850.0), (0.0, 0.0, -0.0), (0.1335, 1.0000, 3.0000), "DV_SM_Mines_MetalGate_4Bar_3M_A2_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: SM_Mines_MetalGate_4Bar_3M_A4_183 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (3550.0, 2150.0, 850.0), (0.0, 0.0, -0.0), (0.1335, 1.0000, 3.0000), "DV_SM_Mines_MetalGate_4Bar_3M_A4_183_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: SM_Mines_MetalGate_4Bar_3M_A5 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (1370.0, 4560.0, 850.0), (0.0, 0.0, -0.0), (0.1335, 1.0000, 3.0000), "DV_SM_Mines_MetalGate_4Bar_3M_A5_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: SM_Mines_MetalGate_4Bar_3M_A6 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (1370.0, 4660.0, 850.0), (0.0, 0.0, -0.0), (0.1335, 1.0000, 3.0000), "DV_SM_Mines_MetalGate_4Bar_3M_A6_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: SM_Mines_MetalGate_4Bar_3M_A7 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (3570.0, 2240.0, 850.0), (0.0, 0.0, -0.0), (0.5060, 0.9750, 3.0000), "DV_SM_Mines_MetalGate_4Bar_3M_A7_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: SM_Mines_MetalGate_4Bar_3M_A8 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (3640.0, 2290.0, 850.0), (0.0, 0.0, -0.0), (1.0025, 0.3725, 3.0000), "DV_SM_Mines_MetalGate_4Bar_3M_A8_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: SM_Mines_MetalGate_4Bar_3M_A9_190 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (3635.0, 2600.0, 850.0), (0.0, 0.0, -0.0), (0.9865, 0.4626, 3.0000), "DV_SM_Mines_MetalGate_4Bar_3M_A9_190_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: SM_Mines_MetalGate_5Bar_2Cross_A_277 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (1760.0, 3551.6667, 834.9038), (0.0, 0.0, -0.0), (1.9693, 0.0800, 2.6381), "DV_SM_Mines_MetalGate_5Bar_2Cross_A_277_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: SM_Mines_MetalGate_5Bar_2Cross_A2_202 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (2908.3333, 2255.0, 834.9038), (0.0, 0.0, -0.0), (0.0800, 1.9693, 2.6381), "DV_SM_Mines_MetalGate_5Bar_2Cross_A2_202_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: SM_Mines_MetalGate_5Bar_2Cross_A3 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (2908.3333, 2630.0, 834.9038), (0.0, 0.0, -0.0), (0.0800, 1.9693, 2.6381), "DV_SM_Mines_MetalGate_5Bar_2Cross_A3_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: SM_Mines_MetalGate_5Bar_2Cross_A6 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (1998.6669, 4373.9976, 939.1665), (0.0, 0.0, -0.0), (0.0800, 1.9693, 1.1542), "DV_SM_Mines_MetalGate_5Bar_2Cross_A6_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: SM_Mines_MetalGate_5Bar_2M_A_Breakable_2 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (1370.0, 4810.0, 810.8584), (0.0, 0.0, -0.0), (0.1335, 2.0000, 2.3397), "DV_SM_Mines_MetalGate_5Bar_2M_A_Breakable_2_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: SM_Mines_MetalGate_5Bar_2M_A_Breakable2 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (1650.0, 5110.0, 810.8584), (0.0, 0.0, -0.0), (2.0000, 0.1335, 2.3397), "DV_SM_Mines_MetalGate_5Bar_2M_A_Breakable2_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: SM_Mines_MetalGate_5Bar_3M_A2_193 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (3550.301, 2160.0, 1120.0), (0.0, 0.0, -0.0), (0.1227, 2.0354, 3.0000), "DV_SM_Mines_MetalGate_5Bar_3M_A2_193_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: SM_Mines_MetalGate_5Bar_3M_A3_195 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (3549.699, 2355.0, 1120.0), (0.0, 0.0, -0.0), (0.1227, 2.0354, 3.0000), "DV_SM_Mines_MetalGate_5Bar_3M_A3_195_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: SM_Mines_MetalGate_5Bar_3M_A4_198 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (3550.301, 2560.0, 1120.0), (0.0, 0.0, -0.0), (0.1227, 2.0354, 3.0000), "DV_SM_Mines_MetalGate_5Bar_3M_A4_198_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: SM_Mines_MetalGate_5Bar_3M_A5_199 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (3549.699, 2755.0, 1120.0), (0.0, 0.0, -0.0), (0.1227, 2.0354, 3.0000), "DV_SM_Mines_MetalGate_5Bar_3M_A5_199_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: SM_Mines_MetalGate_5Bar_3M_A6_189 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (2906.3018, 2655.0, 1116.0001), (0.0, 0.0, -0.0), (0.1227, 2.0354, 3.0000), "DV_SM_Mines_MetalGate_5Bar_3M_A6_189_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: SM_Mines_MetalGate_5Bar_3M_A7 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (2906.3015, 2455.0, 1116.0001), (0.0, 0.0, -0.0), (0.1227, 2.0354, 3.0000), "DV_SM_Mines_MetalGate_5Bar_3M_A7_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: SM_Mines_MetalGate_5Bar_3M_A8 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (2906.3025, 2255.0002, 1116.0001), (0.0, 0.0, -0.0), (0.1227, 2.0354, 3.0000), "DV_SM_Mines_MetalGate_5Bar_3M_A8_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: SM_Mines_MetalGate_SingleBar_3M_A_280 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (1855.0, 3550.0, 855.0), (0.0, 0.0, -0.0), (0.0800, 0.0800, 3.0000), "DV_SM_Mines_MetalGate_SingleBar_3M_A_280_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: SM_Mines_MetalGate_SingleBar_3M_A2 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (1660.0, 3550.0, 855.0), (0.0, 0.0, -0.0), (0.0800, 0.0800, 3.0000), "DV_SM_Mines_MetalGate_SingleBar_3M_A2_BRK", _folder)
if a: placed += 1
else: skipped += 1

# ======================================================================
# SUMMARY
# ======================================================================
unreal.log(f"[{BUBBLE_NAME}] Reconstruction complete: {placed} placed, {skipped} skipped, {errors} errors")
