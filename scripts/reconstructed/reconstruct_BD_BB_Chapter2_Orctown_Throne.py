"""Auto-generated level reconstruction script.
Bubble: BD_BB_Chapter2_Orctown_Throne
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

BUBBLE_NAME = "BD_BB_Chapter2_Orctown_Throne"
placed = 0
skipped = 0
errors = 0

# ======================================================================
# PHASE 1: InstancedMeshCatalog  (static mesh placement)
# ======================================================================
unreal.log(f"[{BUBBLE_NAME}] Phase 1: Placing static meshes...")

# Batch 0: StaticMesh'City_Stairs_Trim_3M' (3 instances)
_mesh_path = "/Game/Art/Assets/Kits/Architecture/City/City_Stairs_Trim_3M"
_materials = ['/Game/Art/Assets/Kits/Architecture/Suburbs/Materials/Suburb_Stairs_Trim/MI_Suburb_Stairs_Trim_3M']
_folder = "Reconstruction/BD_BB_Chapter2_Orctown_Throne/Meshes"
a = spawn_static_mesh(_mesh_path, _materials, (6073.8696, 3203.3325, 1800.0), (0.0, -92.81207564060665, 0.0), (1.0, 1.0, 1.0), "BP_Suburb_Stairs_Trim_3M_Breakable18", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (6088.5894, 3502.9712, 1800.0), (0.0, -92.81207564060665, 0.0), (1.0, 1.0, 1.0), "BP_Suburb_Stairs_Trim_3M_Breakable19", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (6089.221, 3748.2869, 2700.0024), (3.415093837254397e-05, -92.81199832233538, 179.9999112075143), (1.0, 1.0, 1.0), "City_Stairs_Trim_3M_184", _folder)
if a: placed += 1
else: skipped += 1

# Batch 1: StaticMesh'Deep_WoodenBeam_C' (8 instances)
_mesh_path = "/Game/Art/Assets/Kits/Architecture/Deep/Deep_WoodenBeam_C"
_materials = ['/Game/Art/Assets/Kits/Architecture/Deep/Materials/Deep_WoodTrim/MI_Deep_WoodTrim']
_folder = "Reconstruction/BD_BB_Chapter2_Orctown_Throne/Meshes"
a = spawn_static_mesh(_mesh_path, _materials, (3650.6804, 4256.338, 641.03174), (0.0, 0.0, -0.0), (1.0, 1.0, 1.0), "Deep_WoodenBeam_C_320", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4273.688, 3632.085, 641.03174), (0.0, 0.0, -0.0), (1.0, 1.0, 1.0), "Deep_WoodenBeam_C3", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4278.695, 2740.4087, 641.03174), (0.0, 0.0, -0.0), (1.0, 1.0, 1.0), "Deep_WoodenBeam_C4", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2763.597, 4283.9844, 641.03174), (0.0, 0.0, -0.0), (1.0, 1.0, 1.0), "Deep_WoodenBeam_C5", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2121.6921, 3658.8862, 641.03174), (0.0, 0.0, -0.0), (1.0, 1.0, 1.0), "Deep_WoodenBeam_C6", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2115.3428, 2762.4102, 641.03125), (0.0, 0.0, -0.0), (1.0, 1.0, 1.0), "Deep_WoodenBeam_C7", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3638.2034, 2110.7732, 641.03174), (0.0, 0.0, -0.0), (1.0, 1.0, 1.0), "Deep_WoodenBeam_C8", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2827.8018, 2133.1653, 654.1757), (0.0, 0.0, -0.0), (1.0, 1.0, 1.0), "Deep_WoodenBeam_C9", _folder)
if a: placed += 1
else: skipped += 1

# Batch 2: StaticMesh'NonD_Arch_Half_2m_A' (4 instances)
_mesh_path = "/Game/Art/Assets/Kits/Architecture/Non_D/NonD_Arch_Half_2m_A"
_materials = ['/Game/Art/Assets/Kits/Architecture/Suburbs/Materials/Suburbs_Trim_Sheet_A/MI_Suburbs_Trim_Sheet_Gray']
_folder = "Reconstruction/BD_BB_Chapter2_Orctown_Throne/Meshes"
a = spawn_static_mesh(_mesh_path, _materials, (1566.6996, 4726.8525, 1160.0004), (0.0004712830288677052, 39.68735892231044, -179.999945358493), (1.0, 1.0, 1.0), "NonD_Arch_Half_1m_A_1154", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5505.0, 2915.0, 1489.9996), (6.83020605919736e-06, 90.00007597510897, -179.9996311697969), (1.0, 1.0, 1.0), "NonD_Arch_Half_3m_A10", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2835.0, 914.9993, 1490.0054), (0.0006215470672027653, -179.99994535848006, -179.99997950942858), (1.0, 1.0, 1.0), "NonD_Arch_Half_3m_A13", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2056.9797, 1164.7936, 1490.0144), (0.0005942263990950592, 160.00002795136567, 179.99976777357963), (1.0, 1.0, 1.0), "NonD_Arch_Half_3m_A16", _folder)
if a: placed += 1
else: skipped += 1

# Batch 3: StaticMesh'NonD_Arch_Half_3m_A' (16 instances)
_mesh_path = "/Game/Art/Assets/Kits/Architecture/Non_D/NonD_Arch_Half_3m_A"
_materials = ['/Game/Art/Assets/Kits/Architecture/Suburbs/Materials/Suburbs_Trim_Sheet_A/MI_Suburbs_Trim_Sheet_Gray']
_folder = "Reconstruction/BD_BB_Chapter2_Orctown_Throne/Meshes"
a = spawn_static_mesh(_mesh_path, _materials, (3200.0, 5480.0, 1080.0), (0.0, 0.0, -0.0), (1.0, 1.0, 1.0), "BP_Suburbs_Wall_Thin_Arch_Half_E_3m2", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3200.0, 5520.0, 1050.0), (0.0, 0.0, -0.0), (1.0, 1.0, 1.0), "BP_Suburbs_Wall_Thin_Arch_Half_E_3m3", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3149.9993, 910.00024, 1080.0), (0.0, -179.9998975471592, 0.0), (1.0, 1.0, 1.0), "BP_Suburbs_Wall_Thin_Arch_Half_E_3m4", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3150.0, 870.0, 1050.0), (0.0, -179.9998975471592, 0.0), (1.0, 1.0, 1.0), "BP_Suburbs_Wall_Thin_Arch_Half_E_3m5", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5505.0, 3465.0, 1489.9996), (6.83020605919736e-06, 90.00007597510897, -179.9996311697969), (1.0, 1.0, 1.0), "NonD_Arch_Half_3m_A_1207", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3385.0, 915.0, 1490.0), (0.0006227492484416643, -179.99994535847716, -179.9999863396178), (1.0, 1.0, 1.0), "NonD_Arch_Half_3m_A11_1215", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3085.0, 914.99963, 1490.0029), (0.0006229999289111367, -179.99994535847713, -179.9999863396177), (1.0, 1.0, 1.0), "NonD_Arch_Half_3m_A12_1218", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2573.8123, 976.68286, 1490.0083), (0.0005942264008705669, -19.999968852361455, 179.99976777358228), (1.0, 1.0, 1.0), "NonD_Arch_Half_3m_A14", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2291.9033, 1079.2888, 1490.0116), (0.0005939999757879289, 160.00002795136572, 179.99976777358125), (1.0, 1.0, 1.0), "NonD_Arch_Half_3m_A15", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5505.0, 3165.0, 1489.9996), (6.999993116513521e-06, 90.00007597510954, -179.99963116979677), (1.0, 1.0, 1.0), "NonD_Arch_Half_3m_A2_1209", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2602.0771, 5479.139, 1449.9949), (0.00039615080205765717, -179.99950822615202, 179.99981558480988), (1.0, 1.0, 1.0), "NonD_Arch_Half_3m_A3", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3202.0771, 5479.146, 1449.9904), (0.00039599983916798506, -179.9995082261518, 179.9998155848092), (1.0, 1.0, 1.0), "NonD_Arch_Half_3m_A5", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3502.0771, 5479.148, 1449.9879), (0.00039599983916798506, -179.9995082261518, 179.9998155848092), (1.0, 1.0, 1.0), "NonD_Arch_Half_3m_A6", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2902.0771, 5479.145, 1449.9929), (0.00039599983916798506, -179.9995082261518, 179.9998155848092), (1.0, 1.0, 1.0), "NonD_Arch_Half_3m_A7", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2334.1804, 5378.363, 1449.9982), (0.0004371320129374873, -139.99931250698506, -179.99988388676755), (1.0, 1.0, 1.0), "NonD_Arch_Half_3m_A8", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2104.3687, 5185.5264, 1450.0007), (0.00043699998910891867, -139.9993125069849, -179.9998838867537), (1.0, 1.0, 1.0), "NonD_Arch_Half_3m_A9", _folder)
if a: placed += 1
else: skipped += 1

# Batch 4: StaticMesh'NonD_Arch_Half_3m_C' (8 instances)
_mesh_path = "/Game/Art/Assets/Kits/Architecture/Non_D/NonD_Arch_Half_3m_C"
_materials = ['/Game/Art/Assets/Kits/Architecture/Suburbs/Materials/Suburbs_Trim_Sheet_A/MI_Suburbs_Trim_Sheet_Gray']
_folder = "Reconstruction/BD_BB_Chapter2_Orctown_Throne/Meshes"
a = spawn_static_mesh(_mesh_path, _materials, (2800.0, 5480.0, 580.0), (0.0, 0.0, -0.0), (1.0, 1.0, 1.0), "BP_Suburbs_Wall_Thin_Arch_Half_C3", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3600.0, 5480.0, 580.0), (0.0, 179.99988388675877, -0.0), (1.0, 1.0, 1.0), "BP_Suburbs_Wall_Thin_Arch_Half_C4", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2800.0, 5520.0, 550.0), (0.0, 0.0, -0.0), (1.0, 1.0, 1.0), "BP_Suburbs_Wall_Thin_Arch_Half_C5", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3600.0, 5520.0, 550.0), (0.0, 179.99988388675877, -0.0), (1.0, 1.0, 1.0), "BP_Suburbs_Wall_Thin_Arch_Half_C6", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2750.0, 909.99854, 628.82654), (0.0, 0.0, -0.0), (1.0, 1.0, 1.0), "NonD_Arch_Half_3m_C_375", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2763.523, 869.9989, 628.82654), (0.0, 0.0, -0.0), (1.0, 1.0, 1.0), "NonD_Arch_Half_3m_C2", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3550.0, 909.99854, 628.82654), (0.0, -179.99998633961752, -0.0), (1.0, 1.0, 1.0), "NonD_Arch_Half_3m_C3", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3533.523, 869.9989, 628.82654), (0.0, -179.99998633961752, -0.0), (1.0, 1.0, 1.0), "NonD_Arch_Half_3m_C4", _folder)
if a: placed += 1
else: skipped += 1

# Batch 5: StaticMesh'NonD_Arch_Half_A' (8 instances)
_mesh_path = "/Game/Art/Assets/Kits/Architecture/Non_D/NonD_Arch_Half_A"
_materials = ['/Game/Art/Assets/Kits/Architecture/Suburbs/Materials/Suburbs_Trim_Sheet_A/MI_Suburbs_Trim_Sheet_Gray']
_folder = "Reconstruction/BD_BB_Chapter2_Orctown_Throne/Meshes"
a = spawn_static_mesh(_mesh_path, _materials, (2750.0, 869.9989, 850.0), (0.0, 0.0001235008235574265, -0.0), (1.0, 1.0, 1.0), "BP_Suburbs_Wall_Thin_Arch_Half_D10", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2800.0, 5480.0, 880.0), (0.0, 0.0, -0.0), (1.0, 1.0, 1.0), "BP_Suburbs_Wall_Thin_Arch_Half_D3", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3600.0, 5480.0, 880.0), (0.0, 179.99988388675877, -0.0), (1.0, 1.0, 1.0), "BP_Suburbs_Wall_Thin_Arch_Half_D4", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2800.0, 5520.0, 850.0), (0.0, 0.0, -0.0), (1.0, 1.0, 1.0), "BP_Suburbs_Wall_Thin_Arch_Half_D5", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3600.0, 5520.0, 850.0), (0.0, 179.99988388675877, -0.0), (1.0, 1.0, 1.0), "BP_Suburbs_Wall_Thin_Arch_Half_D6", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3549.9998, 910.00134, 880.0), (0.0, -179.9998975471592, 0.0), (1.0, 1.0, 1.0), "BP_Suburbs_Wall_Thin_Arch_Half_D7", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2749.9995, 909.99854, 880.0), (0.0, 0.0001235008235574265, -0.0), (1.0, 1.0, 1.0), "BP_Suburbs_Wall_Thin_Arch_Half_D8", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3550.0, 870.0016, 850.0), (0.0, -179.9998975471592, 0.0), (1.0, 1.0, 1.0), "BP_Suburbs_Wall_Thin_Arch_Half_D9", _folder)
if a: placed += 1
else: skipped += 1

# Batch 6: StaticMesh'NonD_Stairs_Trim_A_L' (6 instances)
_mesh_path = "/Game/Art/Assets/Kits/Architecture/Non_D/NonD_Stairs_Trim_A_L"
_materials = ['/Game/Art/Assets/Kits/Architecture/Suburbs/Materials/Suburbs_Trim_Sheet_A/MI_Suburbs_Trim_Sheet_Gray', '/Game/Environments/Materials/MI_ArchitectureBase_NonDestructible']
_folder = "Reconstruction/BD_BB_Chapter2_Orctown_Throne/Meshes"
a = spawn_static_mesh(_mesh_path, _materials, (5527.321, 2764.7544, 1060.0), (0.0, -115.93749026062889, 0.0), (1.519172, 1.519172, 1.519172), "NonD_Stairs_Trim_A_R_1068", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4240.181, 5265.268, 670.0), (0.0, -22.50012302225854, 0.0), (1.519172, 1.519172, 1.519172), "NonD_Stairs_Trim_A_R10", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5262.095, 2219.4475, 687.80414), (0.0, -115.93749026062889, 0.0), (1.519172, 1.519172, 1.519172), "NonD_Stairs_Trim_A_R2", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1921.2068, 1195.3987, 1060.0), (0.0, 129.37415750648682, -0.0), (1.519172, 1.519172, 1.519172), "NonD_Stairs_Trim_A_R7", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1522.7341, 1683.3799, 660.0), (0.0, 129.37415750648682, -0.0), (1.519172, 1.519172, 1.519172), "NonD_Stairs_Trim_A_R8", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3658.1382, 5506.359, 1070.0), (0.0, -22.50012302225854, 0.0), (1.519172, 1.519172, 1.519172), "NonD_Stairs_Trim_A_R9", _folder)
if a: placed += 1
else: skipped += 1

# Batch 7: StaticMesh'NonD_Stairs_Trim_A_R' (4 instances)
_mesh_path = "/Game/Art/Assets/Kits/Architecture/Non_D/NonD_Stairs_Trim_A_R"
_materials = ['/Game/Art/Assets/Kits/Architecture/Suburbs/Materials/Suburbs_Trim_Sheet_A/MI_Suburbs_Trim_Sheet_A', '/Game/Environments/Materials/MI_ArchitectureBase_NonDestructible']
_folder = "Reconstruction/BD_BB_Chapter2_Orctown_Throne/Meshes"
a = spawn_static_mesh(_mesh_path, _materials, (1984.5428, 5097.936, 1070.1298), (0.0, -140.31249567079587, 0.0), (1.56, 1.56, 1.56), "NonD_Stairs_Trim_A_R11", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1461.2562, 4663.686, 750.12976), (0.0, -140.31249567079587, 0.0), (1.56, 1.56, 1.56), "NonD_Stairs_Trim_A_R12", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3590.1345, 903.52374, 1075.4364), (0.0, 19.68755902233709, -0.0), (1.56, 1.56, 1.56), "NonD_Stairs_Trim_A_R5", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4160.2153, 1107.5142, 650.3293), (0.0, 19.68755902233709, -0.0), (1.56, 1.56, 1.56), "NonD_Stairs_Trim_A_R6", _folder)
if a: placed += 1
else: skipped += 1

# Batch 8: StaticMesh'NonD_Stairs_Trim_A_R' (2 instances)
_mesh_path = "/Game/Art/Assets/Kits/Architecture/Non_D/NonD_Stairs_Trim_A_R"
_materials = ['/Game/Art/Assets/Kits/Architecture/Suburbs/Materials/Suburbs_Trim_Sheet_A/MI_Suburbs_Trim_Sheet_Gray', '/Game/Environments/Materials/MI_ArchitectureBase_NonDestructible']
_folder = "Reconstruction/BD_BB_Chapter2_Orctown_Throne/Meshes"
a = spawn_static_mesh(_mesh_path, _materials, (5521.09, 3649.9448, 1075.4364), (0.0, 115.3123360223098, -0.0), (1.56, 1.56, 1.56), "NonD_Stairs_Trim_A_R3_1074", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5285.044, 4149.0625, 685.2891), (0.0, 115.3123360223098, -0.0), (1.56, 1.56, 1.56), "NonD_Stairs_Trim_A_R4", _folder)
if a: placed += 1
else: skipped += 1

# Batch 9: StaticMesh'NonD_Stairs_Trim_C_L' (12 instances)
_mesh_path = "/Game/Art/Assets/Kits/Architecture/Non_D/NonD_Stairs_Trim_C_L"
_materials = ['/Game/Art/Assets/Kits/Architecture/Suburbs/Materials/Suburbs_Trim_Sheet_A/MI_Suburbs_Trim_Sheet_A']
_folder = "Reconstruction/BD_BB_Chapter2_Orctown_Throne/Meshes"
a = spawn_static_mesh(_mesh_path, _materials, (919.99054, 1201.8251, 795.0), (0.0, 129.37473535286728, -0.0), (1.0, 1.5921148, 1.0), "NonD_Stairs_Trim_C_L21_4", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1110.3077, 969.9224, 995.0), (0.0, 129.37473535286728, -0.0), (1.0, 1.5921148, 1.0), "NonD_Stairs_Trim_C_L22", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1300.6246, 738.0185, 1195.0), (0.0, 129.37473535286728, -0.0), (1.0, 1.5921148, 1.0), "NonD_Stairs_Trim_C_L23", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1522.9415, 1696.6492, 795.0), (0.0, 129.37473535286728, -0.0), (1.0, 1.0, 1.0), "NonD_Stairs_Trim_C_L24_13", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1713.2588, 1464.7465, 995.0), (0.0, 129.37473535286728, -0.0), (1.0, 1.0, 1.0), "NonD_Stairs_Trim_C_L25_14", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1903.5757, 1232.8427, 1195.0), (0.0, 129.37473535286728, -0.0), (1.0, 1.0, 1.0), "NonD_Stairs_Trim_C_L26_15", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3628.0972, 905.01636, 1195.0), (0.0, 19.37460402580194, -0.0), (1.0, 1.0, 1.0), "NonD_Stairs_Trim_C_L32", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3911.108, 1004.5393, 995.0), (0.0, 19.37460402580194, -0.0), (1.0, 1.0, 1.0), "NonD_Stairs_Trim_C_L33", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4194.1187, 1104.0623, 795.0), (0.0, 19.37460402580194, -0.0), (1.0, 1.0, 1.0), "NonD_Stairs_Trim_C_L34", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3823.8254, 348.428, 1195.0), (0.0, 19.37460402580194, -0.0), (1.0, 1.5, 1.0), "NonD_Stairs_Trim_C_L35", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4106.8364, 447.9509, 995.0), (0.0, 19.37460402580194, -0.0), (1.0, 1.5, 1.0), "NonD_Stairs_Trim_C_L36", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4389.845, 547.4739, 795.0), (0.0, 19.37460402580194, -0.0), (1.0, 1.5, 1.0), "NonD_Stairs_Trim_C_L37", _folder)
if a: placed += 1
else: skipped += 1

# Batch 10: StaticMesh'NonD_Stairs_Trim_D' (24 instances)
_mesh_path = "/Game/Art/Assets/Kits/Architecture/Non_D/NonD_Stairs_Trim_D"
_materials = ['/Game/Art/Assets/Kits/Architecture/Suburbs/Materials/Suburbs_Trim_Sheet_A/MI_Suburbs_Trim_Sheet_Gray']
_folder = "Reconstruction/BD_BB_Chapter2_Orctown_Throne/Meshes"
a = spawn_static_mesh(_mesh_path, _materials, (5500.5903, 3629.309, 1385.0), (0.0, 115.3123360223098, -0.0), (1.0, 1.0, 1.0), "NonD_Stairs_Trim_C_L_205", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3843.5256, 1016.50934, 1200.0), (0.0, 19.68755902233709, -0.0), (1.0, 1.0, 1.0), "NonD_Stairs_Trim_C_L10", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4125.9883, 1117.5757, 1000.0), (0.0, 19.68755902233709, -0.0), (1.0, 1.0, 1.0), "NonD_Stairs_Trim_C_L11", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4408.451, 1218.6426, 800.0), (0.0, 19.68755902233709, -0.0), (1.0, 1.0, 1.0), "NonD_Stairs_Trim_C_L12", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1914.8828, 1238.2844, 1370.0), (0.0, 129.37484546840184, -0.0), (1.0, 1.0, 1.0), "NonD_Stairs_Trim_C_L13", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1724.5652, 1470.1882, 1170.0), (0.0, 129.37484546840184, -0.0), (1.0, 1.0, 1.0), "NonD_Stairs_Trim_C_L14", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1534.2476, 1702.092, 970.0), (0.0, 129.37484546840184, -0.0), (1.0, 1.0, 1.0), "NonD_Stairs_Trim_C_L15", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1343.9299, 1933.9958, 770.0), (0.0, 129.37484546840184, -0.0), (1.0, 1.0, 1.0), "NonD_Stairs_Trim_C_L16", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3684.5876, 5462.5225, 1360.0), (0.0, -22.499999128211993, 0.0), (1.0, 1.0, 1.0), "NonD_Stairs_Trim_C_L17_691", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3961.7522, 5347.717, 1160.0), (0.0, -22.499999128211993, 0.0), (1.0, 1.0, 1.0), "NonD_Stairs_Trim_C_L18", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4238.917, 5232.911, 960.0), (0.0, -22.499999128211993, 0.0), (1.0, 1.0, 1.0), "NonD_Stairs_Trim_C_L19", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5372.3257, 3900.5059, 1185.0), (0.0, 115.3123360223098, -0.0), (1.0, 1.0, 1.0), "NonD_Stairs_Trim_C_L2", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4516.08, 5118.1055, 760.0), (0.0, -22.499999128211993, 0.0), (1.0, 1.0, 1.0), "NonD_Stairs_Trim_C_L20", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5244.061, 4171.703, 985.0), (0.0, 115.3123360223098, -0.0), (1.0, 1.0, 1.0), "NonD_Stairs_Trim_C_L3", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5115.7964, 4442.9014, 785.0), (0.0, 115.3123360223098, -0.0), (1.0, 1.0, 1.0), "NonD_Stairs_Trim_C_L4", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5514.149, 2801.4075, 1405.0), (0.0, -115.93750191659933, 0.0), (1.0, 1.0, 1.0), "NonD_Stairs_Trim_C_L5", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5382.931, 2531.6257, 1205.0), (0.0, -115.93750191659933, 0.0), (1.0, 1.0, 1.0), "NonD_Stairs_Trim_C_L6_214", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5251.7134, 2261.844, 1005.0), (0.0, -115.93750191659933, 0.0), (1.0, 1.0, 1.0), "NonD_Stairs_Trim_C_L7_216", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5120.4956, 1992.0623, 805.0), (0.0, -115.93750191659933, 0.0), (1.0, 1.0, 1.0), "NonD_Stairs_Trim_C_L8_218", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3561.0627, 915.4421, 1400.0), (0.0, 19.68755902233709, -0.0), (1.0, 1.0, 1.0), "NonD_Stairs_Trim_C_L9_425", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1966.8672, 5067.0405, 1350.0), (0.0, -140.31249567079587, 0.0), (1.0, 1.0, 1.0), "NonD_Stairs_Trim_D_1132", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1736.0056, 4875.4595, 1150.0), (0.0, -140.31249567079587, 0.0), (1.0, 1.0, 1.0), "NonD_Stairs_Trim_D2", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1466.6672, 4651.9478, 1050.0), (0.0, -140.31249567079587, 0.0), (1.0, 1.0, 1.0), "NonD_Stairs_Trim_D3", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1235.8057, 4460.3667, 850.0), (0.0, -140.31249567079587, 0.0), (1.0, 1.0, 1.0), "NonD_Stairs_Trim_D4", _folder)
if a: placed += 1
else: skipped += 1

# Batch 11: StaticMesh'NonDest_Boundry_3m_Trim_B' (11 instances)
_mesh_path = "/Game/Art/Assets/Kits/Architecture/Non_D/NonDest_Boundry_3m_Trim_B"
_materials = ['/Game/Art/Assets/Kits/Architecture/Suburbs/Materials/Suburbs_Trim_Sheet_A/MI_Suburbs_Trim_Sheet_Gray']
_folder = "Reconstruction/BD_BB_Chapter2_Orctown_Throne/Meshes"
a = spawn_static_mesh(_mesh_path, _materials, (3509.6626, 5826.764, 1121.3146), (0.0006283772568948824, 104.06237727611672, -179.99998633967078), (1.0, 1.0, 1.0), "NonDest_Boundry_3m_Trim_B_750", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3353.536, 5541.7734, 1121.3125), (-6.1035145942447825e-05, 1.6698846494747162e-17, -179.99924184886228), (1.0, 1.0, 1.0), "NonDest_Boundry_3m_Trim_B10", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3444.0007, 854.9999, 1131.325), (-0.0001831053744034445, -179.99998633961414, -179.99998633961414), (1.0, 1.0, 1.0), "NonDest_Boundry_3m_Trim_B11", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3582.5562, 5535.7554, 1121.3116), (0.0006279999132297826, 104.06237727611466, -179.99998633966698), (1.0, 1.0, 1.0), "NonDest_Boundry_3m_Trim_B2", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3436.769, 6117.773, 1121.3175), (0.0006279999132297826, 104.06237727611466, -179.99998633966698), (1.0, 1.0, 1.0), "NonDest_Boundry_3m_Trim_B3", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3144.0007, 854.9999, 1131.325), (-0.0001831053744034445, -179.99998633961414, -179.99998633961414), (1.0, 1.0, 1.0), "NonDest_Boundry_3m_Trim_B4_815", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2903.536, 5826.7734, 1121.3087), (0.0006279999383026254, -104.06272249906745, -179.9999863395691), (1.0, 1.0, 1.0), "NonDest_Boundry_3m_Trim_B5", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2976.431, 6117.782, 1121.3058), (0.0006279999383026254, -104.06272249906745, -179.9999863395691), (1.0, 1.0, 1.0), "NonDest_Boundry_3m_Trim_B6_757", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3049.326, 6408.791, 1121.3029), (0.0006279999383026254, -104.06272249906745, -179.9999863395691), (1.0, 1.0, 1.0), "NonDest_Boundry_3m_Trim_B7", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2753.536, 5541.7734, 1121.3125), (-6.1035145942447825e-05, 1.6698846494747162e-17, -179.99924184886228), (1.0, 1.0, 1.0), "NonDest_Boundry_3m_Trim_B8", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3053.536, 5541.7734, 1121.3125), (-6.1035145942447825e-05, 1.6698846494747162e-17, -179.99924184886228), (1.0, 1.0, 1.0), "NonDest_Boundry_3m_Trim_B9", _folder)
if a: placed += 1
else: skipped += 1

# Batch 12: StaticMesh'NonDest_Floor_Trim_Corner_M' (4 instances)
_mesh_path = "/Game/Art/Assets/Kits/Architecture/Non_D/NonDest_Floor_Trim_Corner_M"
_materials = ['/Game/Art/Assets/Kits/Architecture/Suburbs/Materials/Suburbs_Trim_Sheet_A/MI_Suburbs_Trim_Sheet_A']
_folder = "Reconstruction/BD_BB_Chapter2_Orctown_Throne/Meshes"
a = spawn_static_mesh(_mesh_path, _materials, (4516.06, 5126.6426, 800.0), (0.0, -112.49999787930444, 0.0), (1.0, 1.0, 1.0), "NonDest_Floor_Trim_Thin_3M_A33", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4516.06, 5126.6426, 800.0), (0.0, 157.50010355466222, -0.0), (1.0, 1.0, 1.0), "NonDest_Floor_Trim_Thin_3M_A34_79", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4457.8687, 1255.021, 800.0), (0.0, 19.687582923231698, -0.0), (1.0, 1.0, 1.0), "NonDest_Floor_Trim_Thin_3M_A43", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4457.8687, 1255.021, 800.0), (0.0, 109.68757978616826, -0.0), (1.0, 1.0, 1.0), "NonDest_Floor_Trim_Thin_3M_A44", _folder)
if a: placed += 1
else: skipped += 1

# Batch 13: StaticMesh'NonDest_Floor_Trim_Thin_1_5M_A' (1 instances)
_mesh_path = "/Game/Art/Assets/Kits/Architecture/Non_D/NonDest_Floor_Trim_Thin_1_5M_A"
_materials = ['/Game/Art/Assets/Kits/Architecture/Suburbs/Materials/Suburbs_Trim_Sheet_A/MI_Suburbs_Trim_Sheet_Gray']
_folder = "Reconstruction/BD_BB_Chapter2_Orctown_Throne/Meshes"
a = spawn_static_mesh(_mesh_path, _materials, (5510.0, 3178.0, 1395.0), (0.0, -90.0001164887758, 0.0), (1.0, 1.0, 1.0), "NonDest_Floor_Trim_Thin_1_5M_A2_315", _folder)
if a: placed += 1
else: skipped += 1

# Batch 14: StaticMesh'NonDest_Floor_Trim_Thin_2M_A' (1 instances)
_mesh_path = "/Game/Art/Assets/Kits/Architecture/Non_D/NonDest_Floor_Trim_Thin_2M_A"
_materials = ['/Game/Art/Assets/Kits/Architecture/Suburbs/Materials/Suburbs_Trim_Sheet_A/MI_Suburbs_Trim_Sheet_Gray']
_folder = "Reconstruction/BD_BB_Chapter2_Orctown_Throne/Meshes"
a = spawn_static_mesh(_mesh_path, _materials, (5510.0, 3378.0, 1395.0), (0.0, -90.0001164887758, 0.0), (1.0, 1.0, 1.0), "NonDest_Floor_Trim_Thin_1_5M_A_310", _folder)
if a: placed += 1
else: skipped += 1

# Batch 15: StaticMesh'NonDest_Floor_Trim_Thin_3M_A' (10 instances)
_mesh_path = "/Game/Art/Assets/Kits/Architecture/Non_D/NonDest_Floor_Trim_Thin_3M_A"
_materials = ['/Game/Art/Assets/Kits/Architecture/Suburbs/Materials/Suburbs_Trim_Sheet_A/MI_Suburbs_Trim_Sheet_A']
_folder = "Reconstruction/BD_BB_Chapter2_Orctown_Throne/Meshes"
a = spawn_static_mesh(_mesh_path, _materials, (4630.8657, 5403.806, 800.0), (0.0, -112.49999787930444, 0.0), (1.0, 1.0, 1.0), "NonDest_Floor_Trim_Thin_3M_A31_72", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4745.6714, 5680.9697, 800.0), (0.0, -112.49999787930444, 0.0), (1.0, 1.0, 1.0), "NonDest_Floor_Trim_Thin_3M_A32", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1647.2476, 4788.465, 1090.0), (0.0, 129.37447933253276, -0.0), (1.0, 1.0, 1.0), "NonDest_Floor_Trim_Thin_3M_A35_82", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1456.9315, 5020.37, 1090.0), (0.0, 129.37447933253276, -0.0), (1.0, 1.0, 1.0), "NonDest_Floor_Trim_Thin_3M_A36", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1266.6154, 5252.2754, 1090.0), (0.0, 129.37447933253276, -0.0), (1.0, 1.0, 1.0), "NonDest_Floor_Trim_Thin_3M_A37", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1294.5978, 4887.1494, 1090.0), (0.0, -50.62573346366143, 0.0), (1.0, 1.0, 1.0), "NonDest_Floor_Trim_Thin_3M_A38", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1104.283, 5119.0547, 1090.0), (0.0, -50.62573346366143, 0.0), (1.0, 1.0, 1.0), "NonDest_Floor_Trim_Thin_3M_A39", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (913.96796, 5350.96, 1090.0), (0.0, -50.62573346366143, 0.0), (1.0, 1.0, 1.0), "NonDest_Floor_Trim_Thin_3M_A40", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4457.8687, 1255.021, 800.0), (0.0, -70.3124375972685, 0.0), (1.0, 1.0, 1.0), "NonDest_Floor_Trim_Thin_3M_A41_90", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4558.9365, 972.55786, 800.0), (0.0, -70.3124375972685, 0.0), (1.0, 1.0, 1.0), "NonDest_Floor_Trim_Thin_3M_A42", _folder)
if a: placed += 1
else: skipped += 1

# Batch 16: StaticMesh'NonDest_Floor_Trim_Thin_3M_A' (29 instances)
_mesh_path = "/Game/Art/Assets/Kits/Architecture/Non_D/NonDest_Floor_Trim_Thin_3M_A"
_materials = ['/Game/Art/Assets/Kits/Architecture/Suburbs/Materials/Suburbs_Trim_Sheet_A/MI_Suburbs_Trim_Sheet_Gray']
_folder = "Reconstruction/BD_BB_Chapter2_Orctown_Throne/Meshes"
a = spawn_static_mesh(_mesh_path, _materials, (5510.7495, 2729.7761, 1395.7316), (0.0, -25.937836919930906, 0.0), (1.0, 1.0, 1.0), "NonDest_Floor_Trim_Thin_3M_A_250", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5509.799, 3028.2202, 1395.7316), (0.0, -90.0001164887758, 0.0), (1.0, 1.0, 1.0), "NonDest_Floor_Trim_Thin_3M_A10", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1457.3833, 863.8131, 1395.0135), (0.0, -140.00012387272128, 0.0), (1.0, 1.0, 1.0), "NonDest_Floor_Trim_Thin_3M_A11", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2197.3745, 1142.6355, 1391.9238), (0.0, 159.99983330822857, -0.0), (1.0, 1.0, 1.0), "NonDest_Floor_Trim_Thin_3M_A12", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2479.2822, 1040.0283, 1391.9238), (0.0, 159.99983330822857, -0.0), (1.0, 1.0, 1.0), "NonDest_Floor_Trim_Thin_3M_A13", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2761.19, 937.42, 1391.9238), (0.0, 159.99983330822857, -0.0), (1.0, 1.0, 1.0), "NonDest_Floor_Trim_Thin_3M_A14", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3026.5957, 942.15045, 1391.9238), (0.0, -179.99998633961752, -0.0), (1.0, 1.0, 1.0), "NonDest_Floor_Trim_Thin_3M_A15", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3326.5957, 942.15045, 1391.9238), (0.0, -179.99998633961752, -0.0), (1.0, 1.0, 1.0), "NonDest_Floor_Trim_Thin_3M_A16", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3626.5957, 942.15045, 1391.9238), (0.0, -179.99998633961752, -0.0), (1.0, 1.0, 1.0), "NonDest_Floor_Trim_Thin_3M_A17", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3734.519, 645.63367, 1391.9238), (0.0, 109.999908055275, -0.0), (1.0, 1.0, 1.0), "NonDest_Floor_Trim_Thin_3M_A18", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3837.124, 363.72556, 1391.9238), (0.0, 109.999908055275, -0.0), (1.0, 1.0, 1.0), "NonDest_Floor_Trim_Thin_3M_A19", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5780.53, 2598.557, 1395.7316), (0.0, -25.937836919930906, 0.0), (1.0, 1.0, 1.0), "NonDest_Floor_Trim_Thin_3M_A2", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1794.427, 5295.3423, 1393.419), (0.0, -50.000093879931846, 0.0), (1.0, 1.0, 1.0), "NonDest_Floor_Trim_Thin_3M_A20_767", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1601.5913, 5525.156, 1393.419), (0.0, -50.000093879931846, 0.0), (1.0, 1.0, 1.0), "NonDest_Floor_Trim_Thin_3M_A21", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1408.7556, 5754.969, 1393.419), (0.0, -50.000093879931846, 0.0), (1.0, 1.0, 1.0), "NonDest_Floor_Trim_Thin_3M_A22", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1987.2615, 5065.531, 1392.9714), (0.0, 40.000080625833, -0.0), (1.0, 1.0, 1.0), "NonDest_Floor_Trim_Thin_3M_A23", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2217.0747, 5258.3687, 1392.9714), (0.0, 40.000080625833, -0.0), (1.0, 1.0, 1.0), "NonDest_Floor_Trim_Thin_3M_A24", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2446.8882, 5451.2065, 1392.9714), (0.0, 0.0007209777745920096, -0.0), (1.0, 1.0, 1.0), "NonDest_Floor_Trim_Thin_3M_A25", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2746.8882, 5451.2095, 1392.9714), (0.0, 0.0007210000053544624, -0.0), (1.0, 1.0, 1.0), "NonDest_Floor_Trim_Thin_3M_A26", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3046.8882, 5451.2124, 1392.9714), (0.0, 0.0007210000053544624, -0.0), (1.0, 1.0, 1.0), "NonDest_Floor_Trim_Thin_3M_A27", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3346.8882, 5451.2153, 1392.9714), (0.0, 0.0007210000053544624, -0.0), (1.0, 1.0, 1.0), "NonDest_Floor_Trim_Thin_3M_A28", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3697.7197, 5471.048, 1392.9714), (0.0, 67.50017447326923, -0.0), (1.0, 1.0, 1.0), "NonDest_Floor_Trim_Thin_3M_A29", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3812.524, 5748.211, 1392.9714), (0.0, 67.50017447326923, -0.0), (1.0, 1.0, 1.0), "NonDest_Floor_Trim_Thin_3M_A30", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1917.0096, 1249.4839, 1395.2552), (0.0, -140.00012387272128, 0.0), (1.0, 1.0, 1.0), "NonDest_Floor_Trim_Thin_3M_A4_444", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5780.994, 3806.4863, 1395.7316), (0.0, -154.68745436454066, 0.0), (1.0, 1.0, 1.0), "NonDest_Floor_Trim_Thin_3M_A5", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (6052.1895, 3934.7524, 1395.7316), (0.0, -154.68745436454066, 0.0), (1.0, 1.0, 1.0), "NonDest_Floor_Trim_Thin_3M_A6", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (6323.385, 4063.0186, 1395.7316), (0.0, -154.68745436454066, 0.0), (1.0, 1.0, 1.0), "NonDest_Floor_Trim_Thin_3M_A7", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5509.799, 3678.2202, 1395.7316), (0.0, -90.0001164887758, 0.0), (1.0, 1.0, 1.0), "NonDest_Floor_Trim_Thin_3M_A8", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1687.1962, 1056.6482, 1395.2552), (0.0, -140.00012387272128, 0.0), (1.0, 1.0, 1.0), "NonDest_Floor_Trim_Thin_3M_A9", _folder)
if a: placed += 1
else: skipped += 1

# Batch 17: StaticMesh'NonDest_Pillar_1_5M_A' (6 instances)
_mesh_path = "/Game/Art/Assets/Kits/Architecture/Non_D/NonDest_Pillar_1_5M_A"
_materials = ['/Game/Art/Assets/Kits/Architecture/Suburbs/Materials/Suburbs_Trim_Sheet_A/MI_Suburbs_Trim_Sheet_Gray']
_folder = "Reconstruction/BD_BB_Chapter2_Orctown_Throne/Meshes"
a = spawn_static_mesh(_mesh_path, _materials, (1367.6682, 1931.6498, 800.0), (0.0, -50.62585655685561, 0.0), (1.0, 1.0, 1.01), "NonDest_Pillar_6M_A14", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4426.605, 1226.6632, 800.0), (0.0, 19.687500288539987, -0.0), (1.0, 1.0, 1.01), "NonDest_Pillar_6M_A17", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1159.5804, 4378.7544, 800.0), (0.0, -140.31262668689934, 0.0), (1.0, 1.0, 1.01), "NonDest_Pillar_6M_A18_647", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4505.153, 5119.898, 799.99994), (0.0, 157.4998666243266, -0.0), (1.0, 1.0, 1.01), "NonDest_Pillar_6M_A25", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5119.4653, 4419.76, 800.0), (0.0, 115.31245074341636, -0.0), (1.0, 1.0, 1.0), "NonDest_Pillar_6M_A5", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5091.541, 1959.159, 800.0), (0.0, 64.06241662194408, -0.0), (1.0, 1.0, 1.0), "NonDest_Pillar_6M_A8", _folder)
if a: placed += 1
else: skipped += 1

# Batch 18: StaticMesh'NonDest_Pillar_25M_A' (10 instances)
_mesh_path = "/Game/Art/Assets/Kits/Architecture/Non_D/NonDest_Pillar_25M_A"
_materials = ['/Game/Art/Assets/Kits/Architecture/Suburbs/Materials/Suburbs_Trim_Sheet_A/MI_Suburbs_Trim_Sheet_Gray']
_folder = "Reconstruction/BD_BB_Chapter2_Orctown_Throne/Meshes"
a = spawn_static_mesh(_mesh_path, _materials, (5500.0, 3600.0, 1250.0), (0.0, 89.99999818714215, -0.0), (1.0, 1.0, 1.0), "NonDest_Pillar_25M_A_1055", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2449.3955, 5463.755, 1250.0), (0.0, -152.8264894524347, 0.0), (1.0, 1.0, 1.0), "NonDest_Pillar_25M_A10", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5500.0, 2800.0, 1250.0), (0.0, 89.99999818714215, -0.0), (1.0, 1.0, 1.0), "NonDest_Pillar_25M_A2", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3550.0, 923.2099, 1250.0), (0.0, -9.155273700792082e-05, 0.0), (1.0, 1.0, 1.0), "NonDest_Pillar_25M_A3", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2730.0, 928.2111, 1250.0), (0.0, -9.155273700792082e-05, 0.0), (1.0, 1.0, 1.0), "NonDest_Pillar_25M_A4", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1935.759, 1222.4417, 1250.0), (0.0, -50.00015062503336, 0.0), (1.0, 1.0, 1.0), "NonDest_Pillar_25M_A5", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3669.3955, 5461.7466, 1250.0), (0.0, 179.99980192457332, -0.0), (1.0, 1.0, 1.0), "NonDest_Pillar_25M_A6", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2749.3955, 5462.9463, 1250.0), (0.0, 179.99980192457332, -0.0), (1.0, 1.0, 1.0), "NonDest_Pillar_25M_A7", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2243.2917, 5285.887, 1250.0), (0.0, -140.00007744451636, 0.0), (1.0, 1.0, 1.0), "NonDest_Pillar_25M_A8", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1967.5159, 5054.4844, 1250.0), (0.0, -140.00007744451636, 0.0), (1.0, 1.0, 1.0), "NonDest_Pillar_25M_A9", _folder)
if a: placed += 1
else: skipped += 1

# Batch 19: StaticMesh'NonDest_Pillar_4M_A' (9 instances)
_mesh_path = "/Game/Art/Assets/Kits/Architecture/Non_D/NonDest_Pillar_4M_A"
_materials = ['/Game/Art/Assets/Kits/Architecture/Suburbs/Materials/Suburbs_Trim_Sheet_A/MI_Suburbs_Trim_Sheet_Gray']
_folder = "Reconstruction/BD_BB_Chapter2_Orctown_Throne/Meshes"
a = spawn_static_mesh(_mesh_path, _materials, (5490.0, 3600.0, 800.0), (0.0, 89.99998684315639, -0.0), (1.0, 1.0, 1.01), "NonDest_Pillar_6M_A_191", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5490.0, 2800.0, 800.0), (0.0, 89.99998684315639, -0.0), (1.0, 1.0, 1.01), "NonDest_Pillar_6M_A28", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3550.0002, 933.2101, 800.0), (0.0, -0.00012207030837116422, 0.0), (1.0, 1.0, 1.01), "NonDest_Pillar_6M_A29", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2730.0002, 938.2113, 800.0), (0.0, -0.00012207030837116422, 0.0), (1.0, 1.0, 1.01), "NonDest_Pillar_6M_A30", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1943.4202, 1228.8696, 800.0), (0.0, -50.00021205698621, 0.0), (1.0, 1.0, 1.01), "NonDest_Pillar_6M_A31", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3669.395, 5451.746, 800.0), (0.0, 179.99970630186863, -0.0), (1.0, 1.0, 1.01), "NonDest_Pillar_6M_A32", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2749.395, 5451.746, 800.0), (0.0, 179.99970630186863, -0.0), (1.0, 1.0, 1.01), "NonDest_Pillar_6M_A33", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2249.7195, 5278.2266, 800.0), (0.0, -140.0001469222118, 0.0), (1.0, 1.0, 1.01), "NonDest_Pillar_6M_A34", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1973.9436, 5046.8237, 800.0), (0.0, -140.0001469222118, 0.0), (1.0, 1.0, 1.01), "NonDest_Pillar_6M_A35", _folder)
if a: placed += 1
else: skipped += 1

# Batch 20: StaticMesh'NonDest_Pillar_4M_B' (7 instances)
_mesh_path = "/Game/Art/Assets/Kits/Architecture/Non_D/NonDest_Pillar_4M_B"
_materials = ['/Game/Art/Assets/Kits/Architecture/Suburbs/Materials/Suburbs_Trim_Sheet_A/MI_Suburbs_Trim_Sheet_Gray']
_folder = "Reconstruction/BD_BB_Chapter2_Orctown_Throne/Meshes"
a = spawn_static_mesh(_mesh_path, _materials, (1557.9833, 1699.7433, 800.0), (0.0, -50.62585655685561, 0.0), (1.0, 1.0, 0.8080342), "NonDest_Pillar_6M_A13", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4144.142, 1125.5963, 800.0), (0.0, 19.687500288539987, -0.0), (1.0, 1.0, 0.7883941), "NonDest_Pillar_6M_A16", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1490.4833, 4653.35, 800.0), (0.0, -140.31262668689934, 0.0), (1.0, 1.0, 1.01), "NonDest_Pillar_6M_A21", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1644.3915, 4781.069, 800.0), (0.0, -140.31262668689934, 0.0), (1.0, 1.0, 1.01), "NonDest_Pillar_6M_A22_1145", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4200.2734, 5246.1836, 799.99994), (0.0, 157.4998666243266, -0.0), (1.0, 1.0, 0.79981446), "NonDest_Pillar_6M_A26", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5247.73, 4148.5615, 800.0), (0.0, 115.31245074341636, -0.0), (1.0, 1.0, 1.0), "NonDest_Pillar_6M_A4", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5227.1343, 2237.9326, 800.0), (0.0, 64.06239536977155, -0.0), (1.0, 1.0, 1.0), "NonDest_Pillar_6M_A7", _folder)
if a: placed += 1
else: skipped += 1

# Batch 21: StaticMesh'NonDest_Pillar_6M_A' (5 instances)
_mesh_path = "/Game/Art/Assets/Kits/Architecture/Non_D/NonDest_Pillar_6M_A"
_materials = ['/Game/Art/Assets/Kits/Architecture/Suburbs/Materials/Suburbs_Trim_Sheet_A/MI_Suburbs_Trim_Sheet_Gray']
_folder = "Reconstruction/BD_BB_Chapter2_Orctown_Throne/Meshes"
a = spawn_static_mesh(_mesh_path, _materials, (1748.2983, 1467.8369, 800.0), (0.0, -50.62585655685561, 0.0), (1.0, 1.0, 0.8492218), "NonDest_Pillar_6M_A12", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3861.6794, 1024.5293, 800.0), (0.0, 19.687500288539987, -0.0), (1.0, 1.0, 0.85999805), "NonDest_Pillar_6M_A15", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3950.8267, 5349.5093, 799.99994), (0.0, 157.4998666243266, -0.0), (1.0, 1.0, 0.8283664), "NonDest_Pillar_6M_A27", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5375.995, 3877.364, 800.0), (0.0, 115.31245074341636, -0.0), (1.0, 1.0, 1.0), "NonDest_Pillar_6M_A3", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5358.354, 2507.713, 800.0), (0.0, 64.06238212748727, -0.0), (1.0, 1.0, 1.0), "NonDest_Pillar_6M_A6", _folder)
if a: placed += 1
else: skipped += 1

# Batch 22: StaticMesh'NonDest_Wall_3M_A' (6 instances)
_mesh_path = "/Game/Art/Assets/Kits/Architecture/Non_D/NonDest_Wall_3M_A"
_materials = ['/Game/Environments/Materials/MI_ArchitectureBase_NonDestructible', '/Game/Environments/Materials/MI_ArchitectureBase_NonDestructible']
_folder = "Reconstruction/BD_BB_Chapter2_Orctown_Throne/Meshes"
a = spawn_static_mesh(_mesh_path, _materials, (3582.5557, 5535.761, 800.0), (0.0, 104.06239989650693, -0.0), (1.0, 1.0, 1.0), "NonDest_Wall_3M_A_719", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3509.662, 5826.77, 800.0), (0.0, 104.06239989650693, -0.0), (1.0, 1.0, 1.0), "NonDest_Wall_3M_A2", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3436.7686, 6117.779, 800.0), (0.0, 104.06239989650693, -0.0), (1.0, 1.0, 1.0), "NonDest_Wall_3M_A3", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2903.536, 5826.7734, 800.0), (0.0, -104.06273699350777, 0.0), (1.0, 1.0, 1.0), "NonDest_Wall_3M_A4", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2976.431, 6117.782, 800.0), (0.0, -104.06273699350777, 0.0), (1.0, 1.0, 1.0), "NonDest_Wall_3M_A5", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3049.326, 6408.791, 800.0), (0.0, -104.06273699350777, 0.0), (1.0, 1.0, 1.0), "NonDest_Wall_3M_A6", _folder)
if a: placed += 1
else: skipped += 1

# Batch 23: StaticMesh'NonDest_Wall_3M_B' (31 instances)
_mesh_path = "/Game/Art/Assets/Kits/Architecture/Non_D/NonDest_Wall_3M_B"
_materials = ['/Game/Environments/Materials/MI_ArchitectureBase_NonDestructible', '/Game/Art/Assets/Kits/Architecture/Suburbs/Materials/Suburbs_Trim_Sheet_A/MI_Suburbs_Trim_Sheet_Gray']
_folder = "Reconstruction/BD_BB_Chapter2_Orctown_Throne/Meshes"
a = spawn_static_mesh(_mesh_path, _materials, (3000.0024, 940.0, 1105.0), (0.0, -3.051757709276941e-05, 0.0), (1.0, 1.0, 1.0), "NonDest_Wall_2M35_A13_368", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2700.0024, 940.0, 1105.0), (0.0, -3.051757709276941e-05, 0.0), (1.0, 1.0, 1.0), "NonDest_Wall_2M35_A14", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3300.0024, 940.0, 1105.0), (0.0, -3.051757709276941e-05, 0.0), (1.0, 1.0, 1.0), "NonDest_Wall_2M35_A15", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3349.998, 5444.999, 1110.0), (0.0, -179.99978826413437, 0.0), (1.0, 1.0, 1.0), "NonDest_Wall_2M35_A16_558", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3649.998, 5444.999, 1110.0), (0.0, -179.99978826413437, 0.0), (1.0, 1.0, 1.0), "NonDest_Wall_2M35_A17", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3049.998, 5444.999, 1110.0), (0.0, -179.99978826413437, 0.0), (1.0, 1.0, 1.0), "NonDest_Wall_2M35_A18", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5480.0, 3325.0, 1100.0), (0.0, 90.0001326944829, -0.0), (1.0, 1.0, 1.0), "NonDest_Wall_2M35_A2", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5480.0, 3025.0, 1100.0), (0.0, 90.0001326944829, -0.0), (1.0, 1.0, 1.0), "NonDest_Wall_2M35_A3", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5480.0, 2725.0, 1100.0), (0.0, 90.0001326944829, -0.0), (1.0, 1.0, 1.0), "NonDest_Wall_2M35_A4", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5480.0, 3325.0, 800.0), (0.0, 90.0001326944829, -0.0), (1.0, 1.0, 1.0), "NonDest_Wall_2M35_A5", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5480.0, 3025.0, 800.0), (0.0, 90.0001326944829, -0.0), (1.0, 1.0, 1.0), "NonDest_Wall_2M35_A6", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5480.0, 2725.0, 800.0), (0.0, 90.0001326944829, -0.0), (1.0, 1.0, 1.0), "NonDest_Wall_2M35_A7", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5498.7476, 3601.6655, 800.0), (0.0, 115.31245074341636, -0.0), (1.0, 1.0, 1.0), "NonDest_Wall_2M35_A8", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5370.48, 3872.8623, 800.0), (0.0, 115.31245074341636, -0.0), (1.0, 1.0, 1.0), "NonDest_Wall_2M35_A9", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1752.9761, 1469.0851, 800.0), (0.0, -50.62585655685561, 0.0), (1.0, 1.0, 1.0), "NonDest_Wall_3M_B16", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1556.8519, 1696.2233, 800.0), (0.0, -50.62585655685561, 0.0), (1.0, 1.0, 1.0), "NonDest_Wall_3M_B17_385", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1893.594, 1241.6968, 1100.0), (0.0, -19.68765222798992, 0.0), (1.0, 1.0, 1.0), "NonDest_Wall_3M_B21", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2176.0583, 1140.6292, 1100.0), (0.0, -19.68765222798992, 0.0), (1.0, 1.0, 1.0), "NonDest_Wall_3M_B22", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2458.5212, 1039.5615, 1100.0), (0.0, -19.68765222798992, 0.0), (1.0, 1.0, 1.0), "NonDest_Wall_3M_B23", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3858.054, 1036.8124, 800.0), (0.0, 19.687500288539987, -0.0), (1.0, 1.0, 1.0), "NonDest_Wall_3M_B29", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3575.591, 935.7454, 800.0), (0.0, 19.687500288539987, -0.0), (1.0, 1.0, 1.0), "NonDest_Wall_3M_B30", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2225.4502, 5254.188, 800.0), (0.0, -140.31249567079587, 0.0), (1.0, 1.0, 1.0), "NonDest_Wall_3M_B37", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1956.1115, 5030.6772, 800.0), (0.0, -140.31249567079587, 0.0), (1.2898692, 1.0, 1.0), "NonDest_Wall_3M_B38", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1478.9963, 4634.7383, 800.0), (0.0, 39.68761969629575, -0.0), (0.80029005, 1.0, 1.0), "NonDest_Wall_3M_B39_1139", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2225.4502, 5254.188, 1100.0), (0.0, -140.31249567079587, 0.0), (1.0, 1.0, 1.0), "NonDest_Wall_3M_B42", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2014.7888, 5116.56, 1100.0), (0.0, 39.68761969629575, -0.0), (1.0, 1.0, 1.0), "NonDest_Wall_3M_B45", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4196.0825, 5238.2935, 800.00073), (0.0, 157.4998666243266, -0.0), (1.0, 1.0, 1.0), "NonDest_Wall_3M_B51_678", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3918.919, 5353.099, 800.00073), (0.0, 157.4998666243266, -0.0), (1.0, 1.0, 1.0), "NonDest_Wall_3M_B52", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3959.496, 5372.6665, 800.00073), (0.0, -22.50006219630275, 0.0), (1.0, 1.0, 1.0), "NonDest_Wall_3M_B55", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5357.0137, 2508.748, 800.0), (0.0, 64.06238212748727, -0.0), (1.0, 1.0, 1.0), "NonDest_Wall_3M_B8", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5225.7935, 2238.9678, 800.0), (0.0, 64.06238212748727, -0.0), (1.0, 1.0, 1.0), "NonDest_Wall_3M_B9", _folder)
if a: placed += 1
else: skipped += 1

# Batch 24: StaticMesh'NonDest_Wall_6M_C' (13 instances)
_mesh_path = "/Game/Art/Assets/Kits/Architecture/Non_D/NonDest_Wall_6M_C"
_materials = ['/Game/Environments/Materials/MI_ArchitectureBase_NonDestructible', '/Game/Environments/Materials/MI_ArchitectureBase_NonDestructible', '/Game/Art/Assets/Kits/Architecture/Suburbs/Materials/Suburbs_Trim_Sheet_A/MI_Suburbs_Trim_Sheet_Gray', '/Game/Environments/Materials/MI_ArchitectureBase_NonDestructible']
_folder = "Reconstruction/BD_BB_Chapter2_Orctown_Throne/Meshes"
a = spawn_static_mesh(_mesh_path, _materials, (5904.477, 4629.033, 1152.3932), (0.0, -61.405275182410016, 0.0), (1.0, 1.0, 1.0), "NonDest_Wall_6M_C_1265", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5821.042, 1666.8282, 1152.3894), (0.0, -114.4801304961971, 0.0), (1.0, 1.0, 1.0), "NonDest_Wall_6M_C13_487", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4626.7163, 5848.634, 1152.3932), (0.0, -23.317077280848256, 0.0), (1.0, 1.0, 1.0), "NonDest_Wall_6M_C29", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4626.7163, 5848.634, 802.3932), (0.0, -23.317077280848256, 0.0), (1.0, 1.0, 1.0), "NonDest_Wall_6M_C33", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4009.9653, 5997.214, 1152.3932), (0.0, -1.4052124152556669, 0.0), (1.0, 1.0, 1.0), "NonDest_Wall_6M_C41", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (6125.2227, 4038.45, 1152.3894), (0.0, -78.86676119989215, 0.0), (1.0, 1.0, 1.0), "NonDest_Wall_6M_C5", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1013.9712, 5299.5923, 1152.3932), (0.0, 48.29538490049707, -0.0), (1.0, 1.0, 1.0), "NonDest_Wall_6M_C53", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (838.1403, 1246.4065, 1152.3932), (0.0, 125.23073669831547, -0.0), (1.0, 1.0, 1.0), "NonDest_Wall_6M_C57", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1283.2299, 793.85754, 1152.3932), (0.0, 146.34768983930167, -0.0), (1.0, 1.0, 1.0), "NonDest_Wall_6M_C61", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4645.947, 549.4038, 1152.3932), (0.0, -160.6877101952664, 0.0), (1.0, 1.0, 1.0), "NonDest_Wall_6M_C69", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4024.4456, 413.85822, 1152.3932), (0.0, -172.2977804514365, 0.0), (1.0, 1.0, 1.0), "NonDest_Wall_6M_C73", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (838.1403, 1246.4065, 802.3932), (0.0, 125.23073669831547, -0.0), (1.0, 1.0, 1.0), "NonDest_Wall_6M_C77", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (6018.4224, 2268.4717, 1152.3894), (0.0, -100.16174287111791, 0.0), (1.0, 1.0, 1.0), "NonDest_Wall_6M_C9_419", _folder)
if a: placed += 1
else: skipped += 1

# Batch 25: StaticMesh'NonDest_Wall_6x4M_A' (42 instances)
_mesh_path = "/Game/Art/Assets/Kits/Architecture/Non_D/NonDest_Wall_6x4M_A"
_materials = ['/Game/Art/Assets/Kits/Architecture/Suburbs/Materials/Suburbs_Trim_Sheet_A/MI_Suburbs_Trim_Sheet_Gray', '/Game/Environments/Materials/MI_ArchitectureBase_NonDestructible']
_folder = "Reconstruction/BD_BB_Chapter2_Orctown_Throne/Meshes"
a = spawn_static_mesh(_mesh_path, _materials, (6037.087, 2315.9207, 1302.3894), (0.0, -100.16174287111791, 0.0), (1.0, 1.0, 1.0), "NonDest_Wall_6M_C10_420", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (6037.085, 2315.9163, 1701.1882), (0.0, -100.16174287111791, 0.0), (1.0, 1.0, 1.0), "NonDest_Wall_6M_C11_421", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (6037.085, 2315.9153, 2099.9116), (0.0, -100.16174287111791, 0.0), (1.0, 1.0, 1.0), "NonDest_Wall_6M_C12_422", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5850.863, 1708.1863, 1302.3894), (0.0, -114.4801304961971, 0.0), (1.0, 1.0, 1.0), "NonDest_Wall_6M_C14_488", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5850.86, 1708.1823, 1701.1882), (0.0, -114.4801304961971, 0.0), (1.0, 1.0, 1.0), "NonDest_Wall_6M_C15_489", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5850.8594, 1708.1813, 2099.9116), (0.0, -114.4801304961971, 0.0), (1.0, 1.0, 1.0), "NonDest_Wall_6M_C16_490", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5889.327, 4677.7207, 1302.3932), (0.0, -61.405244345519144, 0.0), (1.0, 1.0, 1.0), "NonDest_Wall_6M_C2", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5889.327, 4677.717, 1701.192), (0.0, -61.405244345519144, 0.0), (1.0, 1.0, 1.0), "NonDest_Wall_6M_C3", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4584.758, 5877.609, 1302.3932), (0.0, -23.317047783149746, 0.0), (1.0, 1.0, 1.0), "NonDest_Wall_6M_C30", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4584.7603, 5877.6055, 1701.192), (0.0, -23.317047783149746, 0.0), (1.0, 1.0, 1.0), "NonDest_Wall_6M_C31", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4584.7617, 5877.6035, 2099.912), (0.0, -23.317047783149746, 0.0), (1.0, 1.0, 1.0), "NonDest_Wall_6M_C32", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5889.327, 4677.715, 2099.912), (0.0, -61.405244345519144, 0.0), (1.0, 1.0, 1.0), "NonDest_Wall_6M_C4", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3960.2246, 6008.438, 1302.3932), (0.0, -1.4051819270259611, 0.0), (1.0, 1.0, 1.0), "NonDest_Wall_6M_C42", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3960.2285, 6008.436, 1701.192), (0.0, -1.4051819270259611, 0.0), (1.0, 1.0, 1.0), "NonDest_Wall_6M_C43", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3960.2305, 6008.4346, 2099.912), (0.0, -1.4051819270259611, 0.0), (1.0, 1.0, 1.0), "NonDest_Wall_6M_C44", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2040.4487, 5951.584, 1302.3932), (0.0, 16.633246285845942, -0.0), (1.0, 1.0, 1.0), "NonDest_Wall_6M_C46", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2040.4535, 5951.583, 1701.192), (0.0, 16.633246285845942, -0.0), (1.0, 1.0, 1.0), "NonDest_Wall_6M_C47", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2040.4554, 5951.583, 2099.912), (0.0, 16.633246285845942, -0.0), (1.0, 1.0, 1.0), "NonDest_Wall_6M_C48", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1460.6771, 5681.598, 1302.3932), (0.0, 31.357296942737932, -0.0), (1.0, 1.0, 1.0), "NonDest_Wall_6M_C50", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1460.6816, 5681.5986, 1701.192), (0.0, 31.357296942737932, -0.0), (1.0, 1.0, 1.0), "NonDest_Wall_6M_C51", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1460.6836, 5681.599, 2099.912), (0.0, 31.357296942737932, -0.0), (1.0, 1.0, 1.0), "NonDest_Wall_6M_C52", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (973.2365, 5268.9194, 1302.3932), (0.0, 48.29540040051587, -0.0), (1.0, 1.0, 1.0), "NonDest_Wall_6M_C54", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (973.2405, 5268.922, 1701.192), (0.0, 48.29540040051587, -0.0), (1.0, 1.0, 1.0), "NonDest_Wall_6M_C55", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (973.2421, 5268.924, 2099.912), (0.0, 48.29540040051587, -0.0), (1.0, 1.0, 1.0), "NonDest_Wall_6M_C56", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (858.8129, 1199.793, 1302.3932), (0.0, 125.23073669831547, -0.0), (1.0, 1.0, 1.0), "NonDest_Wall_6M_C58", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (858.81085, 1199.7972, 1701.192), (0.0, 125.23073669831547, -0.0), (1.0, 1.0, 1.0), "NonDest_Wall_6M_C59", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (6125.3823, 4089.4385, 1302.3894), (0.0, -78.86676119989215, 0.0), (1.0, 1.0, 1.0), "NonDest_Wall_6M_C6", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (858.80994, 1199.7996, 2099.912), (0.0, 125.23073669831547, -0.0), (1.0, 1.0, 1.0), "NonDest_Wall_6M_C60", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1319.309, 757.8223, 1302.3932), (0.0, 146.34768983930167, -0.0), (1.0, 1.0, 1.0), "NonDest_Wall_6M_C62", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1319.3052, 757.8257, 1701.192), (0.0, 146.34768983930167, -0.0), (1.0, 1.0, 1.0), "NonDest_Wall_6M_C63", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1319.3038, 757.8277, 2099.912), (0.0, 146.34768983930167, -0.0), (1.0, 1.0, 1.0), "NonDest_Wall_6M_C64", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2207.6414, 415.694, 1302.3932), (0.0, 169.64239511976322, -0.0), (1.0, 1.0, 1.0), "NonDest_Wall_6M_C66", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2207.6362, 415.6955, 1701.192), (0.0, 169.64239511976322, -0.0), (1.0, 1.0, 1.0), "NonDest_Wall_6M_C67", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2207.634, 415.69693, 2099.912), (0.0, 169.64239511976322, -0.0), (1.0, 1.0, 1.0), "NonDest_Wall_6M_C68", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (6125.382, 4089.4336, 1701.1882), (0.0, -78.86676119989215, 0.0), (1.0, 1.0, 1.0), "NonDest_Wall_6M_C7", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4696.4443, 556.4992, 1302.3932), (0.0, -160.6877101952664, 0.0), (1.0, 1.0, 1.0), "NonDest_Wall_6M_C70", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4696.439, 556.49774, 1701.192), (0.0, -160.6877101952664, 0.0), (1.0, 1.0, 1.0), "NonDest_Wall_6M_C71", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4696.4355, 556.49774, 2099.912), (0.0, -160.6877101952664, 0.0), (1.0, 1.0, 1.0), "NonDest_Wall_6M_C72", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4075.3394, 410.64444, 1302.3932), (0.0, -172.29734798585116, 0.0), (1.0, 1.0, 1.0), "NonDest_Wall_6M_C74", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4075.334, 410.644, 1701.192), (0.0, -172.29724714783194, 0.0), (1.0, 1.0, 1.0), "NonDest_Wall_6M_C75", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4075.331, 410.64474, 2099.912), (0.0, -172.29734798585116, 0.0), (1.0, 1.0, 1.0), "NonDest_Wall_6M_C76", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (6125.382, 4089.4326, 2099.9116), (0.0, -78.86676119989215, 0.0), (1.0, 1.0, 1.0), "NonDest_Wall_6M_C8", _folder)
if a: placed += 1
else: skipped += 1

# Batch 26: StaticMesh'SM_AR_City_Column_100x100x200_A_Base' (3 instances)
_mesh_path = "/Game/Art/Assets/Kits/Architecture/Suburbs/SM_AR_City_Column_100x100x200_A_Base"
_materials = ['/Game/Art/Assets/Kits/Architecture/Suburbs/Materials/City_Columns/MI_Suburbs_City_Columns_Dest']
_folder = "Reconstruction/BD_BB_Chapter2_Orctown_Throne/Meshes"
a = spawn_static_mesh(_mesh_path, _materials, (5861.418, 3464.0679, 2150.0), (0.0, 177.18761226169238, -0.0), (1.0, 1.0, 1.0), "BP_Column_1x2m_A_Base24_12", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5828.7153, 2964.4126, 2150.0), (0.0, 177.18761226169238, -0.0), (1.0, 1.0, 1.0), "BP_Column_1x2m_A_Base25", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5849.152, 3214.3718, 2150.0), (0.0, 177.18761226169238, -0.0), (1.0, 1.0, 1.0), "BP_Column_1x2m_A_Base65_29", _folder)
if a: placed += 1
else: skipped += 1

# Batch 27: StaticMesh'SM_AR_City_Column_100x100x200_A_Capital' (5 instances)
_mesh_path = "/Game/Art/Assets/Kits/Architecture/Suburbs/SM_AR_City_Column_100x100x200_A_Capital"
_materials = ['/Game/Art/Assets/Kits/Architecture/Suburbs/Materials/City_Columns/MI_Suburbs_City_Columns_Dest']
_folder = "Reconstruction/BD_BB_Chapter2_Orctown_Throne/Meshes"
a = spawn_static_mesh(_mesh_path, _materials, (6034.1797, 2904.9204, 2400.0), (0.0, 177.18761226169238, -0.0), (1.0, 1.0, 1.0), "BP_Column_1x2m_A_Capital43_9", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (6063.619, 3504.1973, 2400.0), (0.0, 177.18761226169238, -0.0), (1.0, 1.0, 1.0), "BP_Column_1x2m_A_Capital44", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5828.7153, 2964.4126, 2550.0), (0.0, 177.18761226169238, -0.0), (1.0, 1.0, 1.0), "BP_Column_1x2m_A_Capital45_16", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5861.418, 3464.0679, 2550.0), (0.0, 177.18761226169238, -0.0), (1.0, 1.0, 1.0), "BP_Column_1x2m_A_Capital46", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5849.152, 3214.3718, 2550.0), (0.0, 177.18761226169238, -0.0), (1.0, 1.0, 1.0), "BP_Column_1x2m_A_Capital47_5", _folder)
if a: placed += 1
else: skipped += 1

# Batch 28: StaticMesh'SM_AR_City_Column_100x100x200_A_Shaft' (13 instances)
_mesh_path = "/Game/Art/Assets/Kits/Architecture/Suburbs/SM_AR_City_Column_100x100x200_A_Shaft"
_materials = ['/Game/Art/Assets/Kits/Architecture/Suburbs/Materials/City_Columns/MI_Suburbs_City_Columns_Dest']
_folder = "Reconstruction/BD_BB_Chapter2_Orctown_Throne/Meshes"
a = spawn_static_mesh(_mesh_path, _materials, (5849.152, 3214.3718, 2350.0), (0.0, 177.18761226169238, -0.0), (1.0, 1.0, 1.0), "BP_Column_1x2m_A_Shaft179", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (6034.1797, 2904.9204, 1600.0), (0.0, 177.18761226169238, -0.0), (1.0, 1.0, 1.0), "BP_Column_1x2m_A_Shaft63", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (6063.619, 3504.1973, 1600.0), (0.0, 177.18761226169238, -0.0), (1.0, 1.0, 1.0), "BP_Column_1x2m_A_Shaft64_18", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (6034.1797, 2904.9204, 1800.0), (0.0, 177.18761226169238, -0.0), (1.0, 1.0, 1.0), "BP_Column_1x2m_A_Shaft65", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (6034.1797, 2904.9204, 2000.0), (0.0, 177.18761226169238, -0.0), (1.0, 1.0, 1.0), "BP_Column_1x2m_A_Shaft66", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (6034.1797, 2904.9204, 2200.0), (0.0, 177.18761226169238, -0.0), (1.0, 1.0, 1.0), "BP_Column_1x2m_A_Shaft67", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (6034.1797, 2904.9204, 1400.0), (0.0, 177.18761226169238, -0.0), (1.0, 1.0, 1.0), "BP_Column_1x2m_A_Shaft68", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (6063.619, 3504.1973, 1800.0), (0.0, 177.18761226169238, -0.0), (1.0, 1.0, 1.0), "BP_Column_1x2m_A_Shaft69", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (6063.619, 3504.1973, 2000.0), (0.0, 177.18761226169238, -0.0), (1.0, 1.0, 1.0), "BP_Column_1x2m_A_Shaft70", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (6063.619, 3504.1973, 2200.0), (0.0, 177.18761226169238, -0.0), (1.0, 1.0, 1.0), "BP_Column_1x2m_A_Shaft71", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (6063.619, 3504.1973, 1400.0), (0.0, 177.18761226169238, -0.0), (1.0, 1.0, 1.0), "BP_Column_1x2m_A_Shaft72", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5828.7153, 2964.4126, 2350.0), (0.0, 177.18761226169238, -0.0), (1.0, 1.0, 1.0), "BP_Column_1x2m_A_Shaft73_21", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5861.418, 3464.0679, 2350.0), (0.0, 177.18761226169238, -0.0), (1.0, 1.0, 1.0), "BP_Column_1x2m_A_Shaft74", _folder)
if a: placed += 1
else: skipped += 1

# Batch 29: StaticMesh'Suburb_Stairs_Trim_Angle_A' (8 instances)
_mesh_path = "/Game/Art/Assets/Kits/Architecture/Suburbs/Suburb_Stairs_Trim_Angle_A"
_materials = ['/Game/Art/Assets/Kits/Architecture/Suburbs/Materials/Suburb_Stairs_Trim/MI_Suburbs_Stairs_Trim_Angle']
_folder = "Reconstruction/BD_BB_Chapter2_Orctown_Throne/Meshes"
a = spawn_static_mesh(_mesh_path, _materials, (4034.4429, 4567.9067, 2825.0), (-90.0, 149.43095646031074, -14.43095846106948), (1.0, 1.0, 1.0), "Suburb_Stairs_Trim_Angle_A_1198", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4597.101, 4055.6895, 2825.0), (-90.0, 150.16409389096148, -195.16312240801528), (1.0, 1.0, 1.0), "Suburb_Stairs_Trim_Angle_A2_1218", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2337.422, 4593.11, 2825.0), (-90.0, 0.9816711184611365, 44.01869300525033), (1.0, 1.0, 1.0), "Suburb_Stairs_Trim_Angle_A4_1224", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1825.2043, 4030.4548, 2825.0), (-90.0, 10.070859504856916, -145.06981910830172), (1.0, 1.0, 1.0), "Suburb_Stairs_Trim_Angle_A5", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1807.0702, 2333.4368, 2825.0), (-90.0, -178.31817021077063, 313.31820125505726), (1.0, 1.0, 1.0), "Suburb_Stairs_Trim_Angle_A6", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2369.7266, 1821.2191, 2825.0), (-90.0, 150.16409389096148, -195.16312240801528), (1.0, 1.0, 1.0), "Suburb_Stairs_Trim_Angle_A7", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4557.764, 2372.8208, 2825.0), (-90.0, 175.68709663490085, -130.6867960765606), (1.0, 1.0, 1.0), "Suburb_Stairs_Trim_Angle_A8", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4045.5461, 1810.1636, 2825.0), (-90.0, 9.558010280883074, -144.55704057243238), (1.0, 1.0, 1.0), "Suburb_Stairs_Trim_Angle_A9", _folder)
if a: placed += 1
else: skipped += 1

# Batch 30: StaticMesh'Suburb_Stairs_Trim_Angle_B' (8 instances)
_mesh_path = "/Game/Art/Assets/Kits/Architecture/Suburbs/Suburb_Stairs_Trim_Angle_B"
_materials = ['/Game/Art/Assets/Kits/Architecture/Suburbs/Materials/Suburb_Stairs_Trim/MI_Suburbs_Stairs_Trim_Angle']
_folder = "Reconstruction/BD_BB_Chapter2_Orctown_Throne/Meshes"
a = spawn_static_mesh(_mesh_path, _materials, (4192.0273, 4414.327, 2580.0), (90.0, -8.141010800150669, 36.85898980980071), (1.0, 1.0, 1.0), "Suburb_Stairs_Trim_Angle_B_1201", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4439.5166, 4209.2695, 2580.0), (90.0, 2.1365915053001876, -132.86367127991778), (1.0, 1.0, 1.0), "Suburb_Stairs_Trim_Angle_B2_1219", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2183.8433, 4435.526, 2580.0), (90.0, 49.22078376815975, 184.22048770144752), (1.0, 1.0, 1.0), "Suburb_Stairs_Trim_Angle_B4_1225", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1978.7855, 4188.0366, 2580.0), (90.0, -44.62650519866579, -89.62721461277283), (1.0, 1.0, 1.0), "Suburb_Stairs_Trim_Angle_B5", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1964.6544, 2179.8567, 2580.0), (90.0, -5.775746805031809, 39.22417738482473), (1.0, 1.0, 1.0), "Suburb_Stairs_Trim_Angle_B6", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2212.1423, 1974.7991, 2580.0), (90.0, 10.923918125985493, -124.07639552033248), (1.0, 1.0, 1.0), "Suburb_Stairs_Trim_Angle_B7", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4404.185, 2215.2368, 2580.0), (90.0, 14.633078587635506, 149.63287029852012), (1.0, 1.0, 1.0), "Suburb_Stairs_Trim_Angle_B8", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4199.1274, 1967.7456, 2580.0), (90.0, 13.993091239897439, 328.99244286653277), (1.0, 1.0, 1.0), "Suburb_Stairs_Trim_Angle_B9", _folder)
if a: placed += 1
else: skipped += 1

# Batch 31: StaticMesh'Suburbs_Column_Large_A_Base' (18 instances)
_mesh_path = "/Game/Art/Assets/Kits/Architecture/Suburbs/Suburbs_Column_Large_A_Base"
_materials = ['/Game/Art/Assets/Kits/Architecture/Suburbs/Materials/Suburbs_Column_Large/MI_Suburbs_Column_Large_A_Base']
_folder = "Reconstruction/BD_BB_Chapter2_Orctown_Throne/Meshes"
a = spawn_static_mesh(_mesh_path, _materials, (349.9995, 2700.0, 900.0), (0.0, 0.00021899999645578192, -0.0), (1.0, 1.0, 1.0), "Suburbs_Column_Large_A_Base_13", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (349.9995, 4000.0, 900.0), (0.0, 0.00021899999645578192, -0.0), (1.0, 1.0, 1.0), "Suburbs_Column_Large_A_Base_41", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3620.96, 337.91833, 1350.0), (0.0, 89.68802047836834, -0.0), (1.0, 1.0, 1.0), "Suburbs_Column_Large_A_Base_50", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (349.9995, 2700.0, 900.0), (0.0, 90.0003595746567, -0.0), (1.0, 1.0, 1.0), "Suburbs_Column_Large_A_Base2_14", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3620.96, 337.91833, 1350.0), (0.0, 179.68815366705493, -0.0), (1.0, 1.0, 1.0), "Suburbs_Column_Large_A_Base2_51", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (349.9995, 2700.0, 900.0), (0.0, 179.99980192457332, -0.0), (1.0, 1.0, 1.0), "Suburbs_Column_Large_A_Base3_15", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3620.96, 337.91833, 1350.0), (0.0, -90.31238231852934, 0.0), (1.0, 1.0, 1.0), "Suburbs_Column_Large_A_Base3_52", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (349.9995, 4000.0, 900.0), (0.0, -89.99984099200987, 0.0), (1.0, 1.0, 1.0), "Suburbs_Column_Large_A_Base4_44", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (352.7207, 2400.8086, 900.0), (0.0, -0.31124876937694784, 0.0), (1.0, 1.0, 1.0), "Suburbs_Column_Large_A_Base5_21", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (350.0005, 3700.0005, 900.0), (0.0, 0.00021899999645578192, -0.0), (1.0, 1.0, 1.0), "Suburbs_Column_Large_A_Base5_25", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2620.974, 343.36957, 1350.0), (0.0, 89.68802047836834, -0.0), (1.0, 1.0, 1.0), "Suburbs_Column_Large_A_Base5_62", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (352.7207, 2400.8086, 900.0), (0.0, 89.68887060348588, -0.0), (1.0, 1.0, 1.0), "Suburbs_Column_Large_A_Base6_22", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (350.0005, 3700.0005, 900.0), (0.0, 90.0003595746567, -0.0), (1.0, 1.0, 1.0), "Suburbs_Column_Large_A_Base6_26", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2620.974, 343.36957, 1350.0), (0.0, 179.68815366705493, -0.0), (1.0, 1.0, 1.0), "Suburbs_Column_Large_A_Base6_63", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (352.7207, 2400.8086, 900.0), (0.0, 179.68834486073018, -0.0), (1.0, 1.0, 1.0), "Suburbs_Column_Large_A_Base7_23", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (350.0005, 3700.0005, 900.0), (0.0, -89.99984099200987, 0.0), (1.0, 1.0, 1.0), "Suburbs_Column_Large_A_Base8_28", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2620.974, 343.36957, 1350.0), (0.0, -0.3120422215921377, 0.0), (1.0, 1.0, 1.0), "Suburbs_Column_Large_A_Base8_65", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (349.9995, 4000.0, 900.0), (0.0, 90.00022020536449, -0.0), (1.0, 1.0, 1.0), "Suburbs_Column_Large_A_Base9", _folder)
if a: placed += 1
else: skipped += 1

# Batch 32: StaticMesh'Suburbs_Column_Large_A_Capitol' (20 instances)
_mesh_path = "/Game/Art/Assets/Kits/Architecture/Suburbs/Suburbs_Column_Large_A_Capitol"
_materials = ['/Game/Art/Assets/Kits/Architecture/Suburbs/Materials/Suburbs_Column_Large/MI_Suburbs_Column_Large_A_Capitol']
_folder = "Reconstruction/BD_BB_Chapter2_Orctown_Throne/Meshes"
a = spawn_static_mesh(_mesh_path, _materials, (352.7207, 2400.8086, 2100.0), (0.0, -90.31255622264266, 0.0), (1.0, 1.0, 1.0), "Suburbs_Column_Large_A_Capitol10", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (352.7207, 2700.8086, 2100.0), (0.0, -0.3125305016711084, 0.0), (1.0, 1.0, 1.0), "Suburbs_Column_Large_A_Capitol11", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (352.7207, 2700.8086, 2100.0), (0.0, -90.31255622264266, 0.0), (1.0, 1.0, 1.0), "Suburbs_Column_Large_A_Capitol12", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (352.7207, 3700.8086, 2100.0), (0.0, -0.3125305016711084, 0.0), (1.0, 1.0, 1.0), "Suburbs_Column_Large_A_Capitol13", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (352.7207, 3700.8086, 2100.0), (0.0, -90.31255622264266, 0.0), (1.0, 1.0, 1.0), "Suburbs_Column_Large_A_Capitol14", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (352.7207, 4000.8086, 2100.0), (0.0, -0.3125305016711084, 0.0), (1.0, 1.0, 1.0), "Suburbs_Column_Large_A_Capitol15", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (352.7207, 4000.8086, 2100.0), (0.0, -90.31255622264266, 0.0), (1.0, 1.0, 1.0), "Suburbs_Column_Large_A_Capitol16", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (352.7207, 4000.8086, 2100.0), (0.0, 179.68744329384467, -0.0), (1.0, 1.0, 1.0), "Suburbs_Column_Large_A_Capitol17", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (352.7207, 3700.8086, 2100.0), (0.0, 89.68744835783163, -0.0), (1.0, 1.0, 1.0), "Suburbs_Column_Large_A_Capitol18", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (352.7207, 3700.8086, 2100.0), (0.0, 179.68744329384467, -0.0), (1.0, 1.0, 1.0), "Suburbs_Column_Large_A_Capitol19", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3620.96, 337.91833, 2150.0), (0.0, 179.68756628163672, -0.0), (1.0, 1.0, 1.0), "Suburbs_Column_Large_A_Capitol2_59", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (352.7207, 2400.8086, 2100.0), (0.0, 89.68744835783163, -0.0), (1.0, 1.0, 1.0), "Suburbs_Column_Large_A_Capitol20", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (352.7207, 2700.8086, 2100.0), (0.0, 179.68744329384467, -0.0), (1.0, 1.0, 1.0), "Suburbs_Column_Large_A_Capitol21", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (352.7207, 2700.8086, 2100.0), (0.0, 89.68744190648346, -0.0), (1.0, 1.0, 1.0), "Suburbs_Column_Large_A_Capitol22", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3620.96, 337.91833, 2150.0), (0.0, 89.6874968465454, -0.0), (1.0, 1.0, 1.0), "Suburbs_Column_Large_A_Capitol3_60", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3620.96, 337.91833, 2150.0), (0.0, -0.31268309349767126, 0.0), (1.0, 1.0, 1.0), "Suburbs_Column_Large_A_Capitol4_61", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2620.974, 343.36957, 2150.0), (0.0, -90.3122588466141, 0.0), (1.0, 1.0, 1.0), "Suburbs_Column_Large_A_Capitol5_70", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2620.974, 343.36957, 2150.0), (0.0, 89.6874968465454, -0.0), (1.0, 1.0, 1.0), "Suburbs_Column_Large_A_Capitol7_72", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2620.974, 343.36957, 2150.0), (0.0, -0.31268309349767126, 0.0), (1.0, 1.0, 1.0), "Suburbs_Column_Large_A_Capitol8_73", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (352.7207, 2400.8086, 2100.0), (0.0, -0.3125305016711084, 0.0), (1.0, 1.0, 1.0), "Suburbs_Column_Large_A_Capitol9", _folder)
if a: placed += 1
else: skipped += 1

# Batch 33: StaticMesh'Suburbs_Column_Large_A_Shaft' (33 instances)
_mesh_path = "/Game/Art/Assets/Kits/Architecture/Suburbs/Suburbs_Column_Large_A_Shaft"
_materials = ['/Game/Art/Assets/Kits/Architecture/Suburbs/Materials/Suburbs_Column_Large/MI_Suburbs_Column_Large_A_Shaft']
_folder = "Reconstruction/BD_BB_Chapter2_Orctown_Throne/Meshes"
a = spawn_static_mesh(_mesh_path, _materials, (349.9995, 4000.0, 1300.0), (0.0, 179.99992486791828, -0.0), (1.0, 1.0, 1.0), "Suburbs_Column_Large_A_Shaft_45", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (349.9995, 4000.0, 1300.0), (0.0, -0.00048828124494935374, 0.0), (1.0, 1.0, 1.0), "Suburbs_Column_Large_A_Shaft10", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (349.9995, 2700.0, 1700.0), (0.0, -0.00030517577092912265, 0.0), (1.0, 1.0, 1.0), "Suburbs_Column_Large_A_Shaft11", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (349.9995, 2700.0, 1700.0), (0.0, -90.00048922067948, 0.0), (1.0, 1.0, 1.0), "Suburbs_Column_Large_A_Shaft12", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (350.0005, 3700.0005, 1700.0), (0.0, -0.00030517577092912265, 0.0), (1.0, 1.0, 1.0), "Suburbs_Column_Large_A_Shaft13", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (350.0005, 3700.0005, 1700.0), (0.0, -90.00048922067948, 0.0), (1.0, 1.0, 1.0), "Suburbs_Column_Large_A_Shaft14", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (352.7207, 2400.8086, 1700.0), (0.0, -0.31176757694937113, 0.0), (1.0, 1.0, 1.0), "Suburbs_Column_Large_A_Shaft15", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (349.9995, 4000.0, 1700.0), (0.0, -90.00048922067948, 0.0), (1.0, 1.0, 1.0), "Suburbs_Column_Large_A_Shaft16", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (352.7207, 2400.8086, 1700.0), (0.0, -90.31180382234848, 0.0), (1.0, 1.0, 1.0), "Suburbs_Column_Large_A_Shaft17", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (349.9995, 4000.0, 1700.0), (0.0, -0.00048828124494935374, 0.0), (1.0, 1.0, 1.0), "Suburbs_Column_Large_A_Shaft18", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (350.0005, 3700.0005, 1300.0), (0.0, 89.99992202041271, -0.0), (1.0, 1.0, 1.0), "Suburbs_Column_Large_A_Shaft19", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (349.9995, 2700.0, 1300.0), (0.0, 89.99979237503166, -0.0), (1.0, 1.0, 1.0), "Suburbs_Column_Large_A_Shaft2_18", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3620.96, 337.91833, 1750.0), (0.0, 179.68756628163672, -0.0), (1.0, 1.0, 1.0), "Suburbs_Column_Large_A_Shaft2_55", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (350.0005, 3700.0005, 1700.0), (0.0, 179.99992486791828, -0.0), (1.0, 1.0, 1.0), "Suburbs_Column_Large_A_Shaft20", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (349.9995, 4000.0, 1700.0), (0.0, 179.99992486791828, -0.0), (1.0, 1.0, 1.0), "Suburbs_Column_Large_A_Shaft21", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (350.0005, 3700.0005, 1700.0), (0.0, 89.99992202041271, -0.0), (1.0, 1.0, 1.0), "Suburbs_Column_Large_A_Shaft22", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (352.7207, 2400.8086, 1700.0), (0.0, 89.6882241268108, -0.0), (1.0, 1.0, 1.0), "Suburbs_Column_Large_A_Shaft23", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (349.9995, 2700.0, 1700.0), (0.0, 179.99969264148905, -0.0), (1.0, 1.0, 1.0), "Suburbs_Column_Large_A_Shaft24", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (349.9995, 2700.0, 1700.0), (0.0, 89.99948446776658, -0.0), (1.0, 1.0, 1.0), "Suburbs_Column_Large_A_Shaft25", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (349.9995, 2700.0, 1300.0), (0.0, -0.00030517577092912265, 0.0), (1.0, 1.0, 1.0), "Suburbs_Column_Large_A_Shaft3_19", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3620.96, 337.91833, 1750.0), (0.0, 89.6874968465454, -0.0), (1.0, 1.0, 1.0), "Suburbs_Column_Large_A_Shaft3_56", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (349.9995, 2700.0, 1300.0), (0.0, -90.00048922067948, 0.0), (1.0, 1.0, 1.0), "Suburbs_Column_Large_A_Shaft4_20", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (349.9995, 4000.0, 1300.0), (0.0, -90.00048922067948, 0.0), (1.0, 1.0, 1.0), "Suburbs_Column_Large_A_Shaft4_48", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3620.96, 337.91833, 1750.0), (0.0, -0.31268309349767126, 0.0), (1.0, 1.0, 1.0), "Suburbs_Column_Large_A_Shaft4_57", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (350.0005, 3700.0005, 1300.0), (0.0, 179.99992486791828, -0.0), (1.0, 1.0, 1.0), "Suburbs_Column_Large_A_Shaft5_29", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2620.974, 343.36957, 1750.0), (0.0, -90.3122588466141, 0.0), (1.0, 1.0, 1.0), "Suburbs_Column_Large_A_Shaft5_66", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (352.7207, 2400.8086, 1300.0), (0.0, 89.68827904089491, -0.0), (1.0, 1.0, 1.0), "Suburbs_Column_Large_A_Shaft6_26", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (352.7207, 2400.8086, 1300.0), (0.0, -0.31176757694937113, 0.0), (1.0, 1.0, 1.0), "Suburbs_Column_Large_A_Shaft7_27", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (350.0005, 3700.0005, 1300.0), (0.0, -0.00030517577092912265, 0.0), (1.0, 1.0, 1.0), "Suburbs_Column_Large_A_Shaft7_31", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2620.974, 343.36957, 1750.0), (0.0, 89.6874968465454, -0.0), (1.0, 1.0, 1.0), "Suburbs_Column_Large_A_Shaft7_68", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (350.0005, 3700.0005, 1300.0), (0.0, -90.00048922067948, 0.0), (1.0, 1.0, 1.0), "Suburbs_Column_Large_A_Shaft8_32", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2620.974, 343.36957, 1750.0), (0.0, -0.31268309349767126, 0.0), (1.0, 1.0, 1.0), "Suburbs_Column_Large_A_Shaft8_69", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (352.7207, 2400.8086, 1300.0), (0.0, -90.31180382234848, 0.0), (1.0, 1.0, 1.0), "Suburbs_Column_Large_A_Shaft9", _folder)
if a: placed += 1
else: skipped += 1

# Batch 34: StaticMesh'Suburbs_Column_Single_Capitol_A' (4 instances)
_mesh_path = "/Game/Art/Assets/Kits/Architecture/Suburbs/Suburbs_Column_Single_Capitol_A"
_materials = ['/Game/Art/Assets/Kits/Architecture/Suburbs/Materials/Suburbs_Column_Single/MI_Suburbs_Column_Single_Capitol_A_Dest']
_folder = "Reconstruction/BD_BB_Chapter2_Orctown_Throne/Meshes"
a = spawn_static_mesh(_mesh_path, _materials, (5986.6934, 2957.3188, 1855.0), (0.0, 87.18759735891204, -0.0), (1.0, 1.0, 1.0), "BP_Suburbs_Column_Single_Capitol_A_Breakable55", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (6011.226, 3456.7053, 1855.0), (0.0, 87.18759735891204, -0.0), (1.0, 1.0, 1.0), "BP_Suburbs_Column_Single_Capitol_A_Breakable56", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5998.9595, 3207.012, 1855.0), (0.0, 87.18759735891204, -0.0), (1.0, 1.0, 1.0), "BP_Suburbs_Column_Single_Capitol_A_Breakable59", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (6110.1733, 3202.0498, 1750.0), (0.0, 87.18753075119642, -0.0), (1.0, 1.0, 1.0), "Suburbs_Column_Single_Capitol_A_163", _folder)
if a: placed += 1
else: skipped += 1

# Batch 35: StaticMesh'Suburbs_Column_Single_Half_Base_A' (6 instances)
_mesh_path = "/Game/Art/Assets/Kits/Architecture/Suburbs/Suburbs_Column_Single_Half_Base_A"
_materials = ['/Game/Art/Assets/Kits/Architecture/Suburbs/Materials/Suburbs_Column_Single/MI_Suburbs_Column_Single_Half_Base_Dest']
_folder = "Reconstruction/BD_BB_Chapter2_Orctown_Throne/Meshes"
a = spawn_static_mesh(_mesh_path, _materials, (6056.521, 3054.0034, 1500.0), (0.0, -2.812500002205128, 0.0), (1.0, 1.0, 1.0), "Suburbs_Column_Single_Half_Shaft_A10", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (6071.242, 3353.6418, 1500.0), (0.0, 177.18761226169238, -0.0), (1.0, 1.0, 1.0), "Suburbs_Column_Single_Half_Shaft_A11", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (6071.242, 3353.6418, 1500.0), (0.0, 87.18743754883175, -0.0), (1.0, 1.0, 1.0), "Suburbs_Column_Single_Half_Shaft_A12", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (6051.7905, 2753.8745, 1500.0), (0.0, 87.18753075119642, -0.0), (1.0, 1.0, 1.0), "Suburbs_Column_Single_Half_Shaft_A4", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (6095.949, 3652.7903, 1500.0), (0.0, 87.18753075119642, -0.0), (1.0, 1.0, 1.0), "Suburbs_Column_Single_Half_Shaft_A7", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (6056.521, 3054.0034, 1500.0), (0.0, 87.18753075119642, -0.0), (1.0, 1.0, 1.0), "Suburbs_Column_Single_Half_Shaft_A9", _folder)
if a: placed += 1
else: skipped += 1

# Batch 36: StaticMesh'Suburbs_Column_Single_Half_Capitol_A' (7 instances)
_mesh_path = "/Game/Art/Assets/Kits/Architecture/Suburbs/Suburbs_Column_Single_Half_Capitol_A"
_materials = ['/Game/Art/Assets/Kits/Architecture/Suburbs/Materials/Suburbs_Column_Single/MI_Suburbs_Column_Single_Half_Shaft_A-Damaged-Capitol']
_folder = "Reconstruction/BD_BB_Chapter2_Orctown_Throne/Meshes"
a = spawn_static_mesh(_mesh_path, _materials, (6081.296, 3053.348, 2150.0), (0.0, 87.18746121542567, -0.0), (1.0, 1.0, 1.0), "Suburbs_Column_Single_Half_Capitol_A_140", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (6066.5747, 2753.7095, 2150.0), (0.0, 87.18746121542567, -0.0), (1.0, 1.0, 1.0), "Suburbs_Column_Single_Half_Capitol_A2", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (6096.0156, 3352.987, 2150.0), (0.0, 87.18746121542567, -0.0), (1.0, 1.0, 1.0), "Suburbs_Column_Single_Half_Capitol_A3", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (6110.737, 3652.6255, 2150.0), (0.0, 87.18746121542567, -0.0), (1.0, 1.0, 1.0), "Suburbs_Column_Single_Half_Capitol_A4", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (6050.593, 2754.4949, 1800.0), (0.0, 87.18746121542567, -0.0), (1.0, 1.0, 1.0), "Suburbs_Column_Single_Half_Capitol_A5", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (6094.752, 3653.411, 1800.0), (0.0, 87.18746121542567, -0.0), (1.0, 1.0, 1.0), "Suburbs_Column_Single_Half_Capitol_A6", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (6056.523, 3054.0034, 1700.0), (0.0, 87.18746121542567, -0.0), (1.0, 1.0, 1.0), "Suburbs_Column_Single_Half_Capitol_A7", _folder)
if a: placed += 1
else: skipped += 1

# Batch 37: StaticMesh'Suburbs_Column_Single_Half_Shaft_A' (8 instances)
_mesh_path = "/Game/Art/Assets/Kits/Architecture/Suburbs/Suburbs_Column_Single_Half_Shaft_A"
_materials = ['/Game/Art/Assets/Kits/Architecture/Suburbs/Materials/Suburbs_Column_Single/MI_Suburbs_Column_Single_Half_Shaft_A-Damaged-Capitol_NonDest']
_folder = "Reconstruction/BD_BB_Chapter2_Orctown_Throne/Meshes"
a = spawn_static_mesh(_mesh_path, _materials, (6051.7905, 2753.8745, 1700.0), (0.0, 87.18753075119642, -0.0), (1.0, 1.0, 1.0), "Suburbs_Column_Single_Half_Shaft_A_169", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (6071.242, 3353.6418, 1600.0), (0.0, 87.18753075119642, -0.0), (1.0, 1.0, 1.0), "Suburbs_Column_Single_Half_Shaft_A13", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (6071.242, 3353.6418, 1600.0), (0.0, 177.18761997012828, -0.0), (1.0, 1.0, 1.0), "Suburbs_Column_Single_Half_Shaft_A14", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (6056.523, 3054.0034, 1600.0), (0.0, 87.18753075119642, -0.0), (1.0, 1.0, 1.0), "Suburbs_Column_Single_Half_Shaft_A15", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (6056.523, 3054.0034, 1600.0), (0.0, -2.812560905269256, 0.0), (1.0, 1.0, 1.0), "Suburbs_Column_Single_Half_Shaft_A16", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (6051.7905, 2753.8745, 1600.0), (0.0, 87.18753075119642, -0.0), (1.0, 1.0, 1.0), "Suburbs_Column_Single_Half_Shaft_A2", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (6095.949, 3652.7903, 1700.0), (0.0, 87.18753075119642, -0.0), (1.0, 1.0, 1.0), "Suburbs_Column_Single_Half_Shaft_A5", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (6095.949, 3652.7903, 1600.0), (0.0, 87.18753075119642, -0.0), (1.0, 1.0, 1.0), "Suburbs_Column_Single_Half_Shaft_A6", _folder)
if a: placed += 1
else: skipped += 1

# Batch 38: StaticMesh'Suburbs_Column_X_Large_A_Base_1' (6 instances)
_mesh_path = "/Game/Art/Assets/Kits/Architecture/Suburbs/Suburbs_Column_X_Large_A_Base_1"
_materials = ['/Game/Art/Assets/Kits/Architecture/Suburbs/Materials/Suburbs_Trim_Sheet_A/MI_Suburbs_Trim_Sheet_A']
_folder = "Reconstruction/BD_BB_Chapter2_Orctown_Throne/Meshes"
a = spawn_static_mesh(_mesh_path, _materials, (199.99902, 2550.0005, 900.0), (0.0, 179.99992486791828, -0.0), (1.0, 1.0, 1.0), "Suburbs_Column_X_Large_A_Base_1", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (203.53885, 2551.627, 2500.0), (8.771569028641269e-15, 179.68841315303618, 179.99995901885418), (1.0, 1.0, 1.0), "Suburbs_Column_X_Large_A_Base_7", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (200.00098, 3850.0059, 2500.0), (4.739041906805228e-19, 179.99989754715222, 179.99995901885745), (1.0, 1.0, 1.0), "Suburbs_Column_X_Large_A_Base_11", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (199.99902, 3850.0005, 900.0), (0.0, 179.99992486791828, -0.0), (1.0, 1.0, 1.0), "Suburbs_Column_X_Large_A_Base_33", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3770.1401, 187.10272, 1350.0), (0.0, -90.3122588466141, 0.0), (1.0, 1.0, 1.0), "Suburbs_Column_X_Large_A_Base_42", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2470.1538, 194.18832, 2150.0), (-2.2319416356160731e-13, -90.31224266324598, 179.99995901885208), (1.0, 1.0, 1.0), "Suburbs_Column_X_Large_A_Base_48", _folder)
if a: placed += 1
else: skipped += 1

# Batch 39: StaticMesh'Suburbs_Column_X_Large_A_Base_1_R' (6 instances)
_mesh_path = "/Game/Art/Assets/Kits/Architecture/Suburbs/Suburbs_Column_X_Large_A_Base_1_R"
_materials = ['/Game/Art/Assets/Kits/Architecture/Suburbs/Materials/Suburbs_Trim_Sheet_A/MI_Suburbs_Trim_Sheet_A']
_folder = "Reconstruction/BD_BB_Chapter2_Orctown_Throne/Meshes"
a = spawn_static_mesh(_mesh_path, _materials, (200.00146, 2550.0122, 2500.0), (-4.739041906805228e-19, 179.99989754715222, -179.99995901885745), (1.0, 1.0, 1.0), "Suburbs_Column_X_Large_A_Base_2", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (200.00098, 3850.0059, 900.0), (0.0, 179.99992486791828, -0.0), (1.0, 1.0, 1.0), "Suburbs_Column_X_Large_A_Base_3", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (203.53885, 2551.627, 900.0), (0.0, 179.68846790445647, -0.0), (1.0, 1.0, 1.0), "Suburbs_Column_X_Large_A_Base_6", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (200.00146, 3850.0122, 2500.0), (-4.739041906805228e-19, 179.99989754715222, -179.99995901885745), (1.0, 1.0, 1.0), "Suburbs_Column_X_Large_A_Base_36", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3770.1282, 187.10522, 2150.0), (2.2319416356160731e-13, -90.31224266324598, -179.99995901885208), (1.0, 1.0, 1.0), "Suburbs_Column_X_Large_A_Base_45", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2470.1538, 194.18832, 1350.0), (0.0, -90.3122588466141, 0.0), (1.0, 1.0, 1.0), "Suburbs_Column_X_Large_A_Base_47", _folder)
if a: placed += 1
else: skipped += 1

# Batch 40: StaticMesh'Suburbs_Column_X_Large_A_Base_Corner' (4 instances)
_mesh_path = "/Game/Art/Assets/Kits/Architecture/Suburbs/Suburbs_Column_X_Large_A_Base_Corner"
_materials = ['/Game/Art/Assets/Kits/Architecture/Suburbs/Materials/Suburbs_Trim_Sheet_A/MI_Suburbs_Trim_Sheet_A']
_folder = "Reconstruction/BD_BB_Chapter2_Orctown_Throne/Meshes"
a = spawn_static_mesh(_mesh_path, _materials, (199.99902, 2550.0005, 800.0), (0.0, 179.99992486791828, -0.0), (1.0, 1.0, 1.0), "Suburbs_Column_X_Large_A_Base_Corner_7", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (199.99902, 3850.0005, 800.0), (0.0, 179.99992486791828, -0.0), (1.0, 1.0, 1.0), "Suburbs_Column_X_Large_A_Base_Corner_34", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (203.53885, 2551.627, 800.0), (0.0, 89.68832106533198, -0.0), (1.0, 1.0, 1.0), "Suburbs_Column_X_Large_A_Base_Corner2_5", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (200.00098, 3850.0059, 800.0), (0.0, 89.99981506294705, -0.0), (1.0, 1.0, 1.0), "Suburbs_Column_X_Large_A_Base_Corner2_10", _folder)
if a: placed += 1
else: skipped += 1

# Batch 41: StaticMesh'Suburbs_Column_X_Large_A_CapitalL' (1 instances)
_mesh_path = "/Game/Art/Assets/Kits/Architecture/Suburbs/Suburbs_Column_X_Large_A_CapitalL"
_materials = ['/Game/Art/Assets/Kits/Architecture/Suburbs/Materials/Suburbs_Trim_Sheet_A/MI_Suburbs_Trim_Sheet_A']
_folder = "Reconstruction/BD_BB_Chapter2_Orctown_Throne/Meshes"
a = spawn_static_mesh(_mesh_path, _materials, (3770.1401, 187.10272, 2150.0), (0.0, -90.3122588466141, 0.0), (1.0, 1.0, 1.0), "Suburbs_Column_X_Large_A_Captol_44", _folder)
if a: placed += 1
else: skipped += 1

# Batch 42: StaticMesh'Suburbs_Column_X_Large_A_CapitalR1' (1 instances)
_mesh_path = "/Game/Art/Assets/Kits/Architecture/Suburbs/Suburbs_Column_X_Large_A_CapitalR1"
_materials = ['/Game/Art/Assets/Kits/Architecture/Suburbs/Materials/Suburbs_Trim_Sheet_A/MI_Suburbs_Trim_Sheet_A']
_folder = "Reconstruction/BD_BB_Chapter2_Orctown_Throne/Meshes"
a = spawn_static_mesh(_mesh_path, _materials, (2470.1538, 194.18832, 2150.0), (0.0, -90.3122588466141, 0.0), (1.0, 1.0, 1.0), "Suburbs_Column_X_Large_A_Captol2_49", _folder)
if a: placed += 1
else: skipped += 1

# Batch 43: StaticMesh'Suburbs_Column_X_Large_A_Shaft' (8 instances)
_mesh_path = "/Game/Art/Assets/Kits/Architecture/Suburbs/Suburbs_Column_X_Large_A_Shaft"
_materials = ['/Game/Art/Assets/Kits/Architecture/Suburbs/Materials/Suburbs_Column_X_Large_A/MI_Suburbs_Column_X_Large_A_Shaft']
_folder = "Reconstruction/BD_BB_Chapter2_Orctown_Throne/Meshes"
a = spawn_static_mesh(_mesh_path, _materials, (300.0, 3850.0, 1300.0), (0.0, 0.0, -0.0), (1.0, 1.0, 1.0), "Suburbs_Column_X_Large_A_Shaft_260", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (300.0, 4200.0, 1300.0), (0.0, 0.0, -0.0), (1.0, 1.0, 1.0), "Suburbs_Column_X_Large_A_Shaft2", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (300.0, 3850.0, 1700.0), (0.0, 0.0, -0.0), (1.0, 1.0, 1.0), "Suburbs_Column_X_Large_A_Shaft3", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (300.0, 4200.0, 1700.0), (0.0, 0.0, -0.0), (1.0, 1.0, 1.0), "Suburbs_Column_X_Large_A_Shaft4", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (300.0, 2550.0, 1300.0), (0.0, 0.0, -0.0), (1.0, 1.0, 1.0), "Suburbs_Column_X_Large_A_Shaft5", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (300.0, 2900.0, 1300.0), (0.0, 0.0, -0.0), (1.0, 1.0, 1.0), "Suburbs_Column_X_Large_A_Shaft6", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (300.0, 2550.0, 1700.0), (0.0, 0.0, -0.0), (1.0, 1.0, 1.0), "Suburbs_Column_X_Large_A_Shaft7", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (300.0, 2900.0, 1700.0), (0.0, 0.0, -0.0), (1.0, 1.0, 1.0), "Suburbs_Column_X_Large_A_Shaft8", _folder)
if a: placed += 1
else: skipped += 1

# Batch 44: StaticMesh'Suburbs_Gate_A_Pillar_Base' (11 instances)
_mesh_path = "/Game/Art/Assets/Kits/Architecture/Suburbs/Suburbs_Gate_A_Pillar_Base"
_materials = ['/Game/Art/Assets/Kits/Architecture/Suburbs/Materials/Suburbs_Trim_Sheet_A/MI_Suburbs_Trim_Sheet_Gray']
_folder = "Reconstruction/BD_BB_Chapter2_Orctown_Throne/Meshes"
a = spawn_static_mesh(_mesh_path, _materials, (2086.3608, 2080.797, 800.0), (0.0, 45.0000434743028, -0.0), (1.0, 1.0, 1.0), "BP_Suburbs_Gate_A_Pillar_Base_2", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4317.286, 4311.725, 800.0), (0.0, 45.0000434743028, -0.0), (1.0, 1.0, 1.0), "BP_Suburbs_Gate_A_Pillar_Base2", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2082.828, 4311.731, 800.0), (0.0, -44.99990991090605, 0.0), (1.0, 1.0, 1.0), "BP_Suburbs_Gate_A_Pillar_Base3", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4303.1465, 2091.4124, 800.0), (0.0, -44.99990991090605, 0.0), (1.0, 1.0, 1.0), "BP_Suburbs_Gate_A_Pillar_Base4", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5794.3555, 4883.705, 802.3932), (0.0, -61.40539497196487, 0.0), (1.0, 1.0, 1.0), "Suburbs_Gate_A_Pillar_Base_1239", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4842.103, 5783.2236, 802.3932), (0.0, -23.317107930497365, 0.0), (1.0, 1.0, 1.0), "Suburbs_Gate_A_Pillar_Base16", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (811.309, 5110.0933, 802.3932), (0.0, 48.292735185616124, -0.0), (1.0, 1.0, 1.0), "Suburbs_Gate_A_Pillar_Base27", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (688.54956, 1414.6007, 802.3932), (0.0, 125.22933924820616, -0.0), (1.0, 1.0, 1.0), "Suburbs_Gate_A_Pillar_Base30", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2427.5225, 360.02313, 802.3932), (0.0, 169.64131655281435, -0.0), (1.0, 1.0, 1.0), "Suburbs_Gate_A_Pillar_Base33", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4915.054, 616.967, 802.3932), (0.0, -160.68884514924872, 0.0), (1.0, 1.0, 1.0), "Suburbs_Gate_A_Pillar_Base35", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5751.2637, 1452.8163, 802.3894), (0.0, -114.47987896720926, 0.0), (1.0, 1.0, 1.0), "Suburbs_Gate_A_Pillar_Base8_477", _folder)
if a: placed += 1
else: skipped += 1

# Batch 45: StaticMesh'Suburbs_Gate_A_Pillar_Capitol' (32 instances)
_mesh_path = "/Game/Art/Assets/Kits/Architecture/Suburbs/Suburbs_Gate_A_Pillar_Capitol"
_materials = ['/Game/Art/Assets/Kits/Architecture/Suburbs/Materials/Suburbs_Trim_Sheet_A/MI_Suburbs_Trim_Sheet_Gray']
_folder = "Reconstruction/BD_BB_Chapter2_Orctown_Throne/Meshes"
a = spawn_static_mesh(_mesh_path, _materials, (2086.3608, 2080.797, 2800.0), (0.0, 45.0000434743028, -0.0), (1.0, 1.0, 1.0), "BP_Suburbs_Gate_A_Pillar_Capital_2", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4317.286, 4311.725, 2800.0), (0.0, 45.0000434743028, -0.0), (1.0, 1.0, 1.0), "BP_Suburbs_Gate_A_Pillar_Capital2", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2082.828, 4311.731, 2800.0), (0.0, -44.99990991090605, 0.0), (1.0, 1.0, 1.0), "BP_Suburbs_Gate_A_Pillar_Capital3", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4303.1465, 2091.4124, 2800.0), (0.0, -44.99990991090605, 0.0), (1.0, 1.0, 1.0), "BP_Suburbs_Gate_A_Pillar_Capital4", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5794.3555, 4883.705, 2202.394), (0.0, -61.40539497196487, 0.0), (1.0, 1.0, 1.0), "Suburbs_Gate_A_Pillar_Capitol_1245", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4382.943, 5981.1455, 2202.394), (0.0, -23.317107930497365, 0.0), (1.0, 1.0, 1.0), "Suburbs_Gate_A_Pillar_Capitol15", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4842.103, 5783.2236, 2202.394), (0.0, -23.317107930497365, 0.0), (1.0, 1.0, 1.0), "Suburbs_Gate_A_Pillar_Capitol16", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (6033.649, 4444.6846, 2202.394), (0.0, -61.40539497196487, 0.0), (1.0, 1.0, 1.0), "Suburbs_Gate_A_Pillar_Capitol2", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3734.3518, 6029.182, 2202.394), (0.0, -1.4053344839095196, 0.0), (1.0, 1.0, 1.0), "Suburbs_Gate_A_Pillar_Capitol21", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4234.198, 6016.9062, 2202.394), (0.0, -1.4053344839095196, 0.0), (1.0, 1.0, 1.0), "Suburbs_Gate_A_Pillar_Capitol22", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1819.2482, 5901.3955, 2202.394), (0.0, 16.633018401922776, -0.0), (1.0, 1.0, 1.0), "Suburbs_Gate_A_Pillar_Capitol23", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2298.3494, 6044.4404, 2202.394), (0.0, 16.633018401922776, -0.0), (1.0, 1.0, 1.0), "Suburbs_Gate_A_Pillar_Capitol24", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1259.5024, 5576.841, 2202.394), (0.0, 31.35413366225017, -0.0), (1.0, 1.0, 1.0), "Suburbs_Gate_A_Pillar_Capitol25", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1686.5027, 5836.952, 2202.394), (0.0, 31.35413366225017, -0.0), (1.0, 1.0, 1.0), "Suburbs_Gate_A_Pillar_Capitol26", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (811.309, 5110.0933, 2202.394), (0.0, 48.292735185616124, -0.0), (1.0, 1.0, 1.0), "Suburbs_Gate_A_Pillar_Capitol27", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1144.0029, 5483.3286, 2202.394), (0.0, 48.292735185616124, -0.0), (1.0, 1.0, 1.0), "Suburbs_Gate_A_Pillar_Capitol28", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (976.9271, 1006.15717, 2202.394), (0.0, 125.22933924820616, -0.0), (1.0, 1.0, 1.0), "Suburbs_Gate_A_Pillar_Capitol29", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (6096.601, 4314.425, 2202.3936), (0.0, -78.86670200924122, 0.0), (1.0, 1.0, 1.0), "Suburbs_Gate_A_Pillar_Capitol3", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (688.54956, 1414.6007, 2202.394), (0.0, 125.22933924820616, -0.0), (1.0, 1.0, 1.0), "Suburbs_Gate_A_Pillar_Capitol30", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1499.2539, 619.74426, 2202.394), (0.0, 146.34639554076125, -0.0), (1.0, 1.0, 1.0), "Suburbs_Gate_A_Pillar_Capitol31", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1083.0892, 896.8623, 2202.394), (0.0, 146.34625296062157, -0.0), (1.0, 1.0, 1.0), "Suburbs_Gate_A_Pillar_Capitol32", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2427.5225, 360.02313, 2202.394), (0.0, 169.64131655281435, -0.0), (1.0, 1.0, 1.0), "Suburbs_Gate_A_Pillar_Capitol33", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1935.691, 449.99496, 2202.394), (0.0, 169.64131655281435, -0.0), (1.0, 1.0, 1.0), "Suburbs_Gate_A_Pillar_Capitol34", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4915.054, 616.967, 2202.394), (0.0, -160.68884514924872, 0.0), (1.0, 1.0, 1.0), "Suburbs_Gate_A_Pillar_Capitol35", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4443.1655, 451.68658, 2202.394), (0.0, -160.68884514924872, 0.0), (1.0, 1.0, 1.0), "Suburbs_Gate_A_Pillar_Capitol36", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4301.645, 425.87326, 2202.394), (0.0, -172.2991444559567, 0.0), (1.0, 1.0, 1.0), "Suburbs_Gate_A_Pillar_Capitol37", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3806.1475, 358.956, 2202.394), (0.0, -172.2991444559567, 0.0), (1.0, 1.0, 1.0), "Suburbs_Gate_A_Pillar_Capitol38", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (6193.1226, 3823.8342, 2202.3936), (0.0, -78.86670200924122, 0.0), (1.0, 1.0, 1.0), "Suburbs_Gate_A_Pillar_Capitol4", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (6091.9746, 2535.9963, 2202.3936), (0.0, -100.16161761252525, 0.0), (1.0, 1.0, 1.0), "Suburbs_Gate_A_Pillar_Capitol5_401", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (6003.747, 2043.8492, 2202.3936), (0.0, -100.16161761252525, 0.0), (1.0, 1.0, 1.0), "Suburbs_Gate_A_Pillar_Capitol6_411", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5958.4795, 1907.8461, 2202.3936), (0.0, -114.47987896720926, 0.0), (1.0, 1.0, 1.0), "Suburbs_Gate_A_Pillar_Capitol7_469", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5751.2637, 1452.8163, 2202.3936), (0.0, -114.47987896720926, 0.0), (1.0, 1.0, 1.0), "Suburbs_Gate_A_Pillar_Capitol8_479", _folder)
if a: placed += 1
else: skipped += 1

# Batch 46: StaticMesh'Suburbs_Gate_A_Pillar_Shaft' (304 instances)
_mesh_path = "/Game/Art/Assets/Kits/Architecture/Suburbs/Suburbs_Gate_A_Pillar_Shaft"
_materials = ['/Game/Art/Assets/Kits/Architecture/Suburbs/Materials/Suburbs_Trim_Sheet_A/MI_Suburbs_Trim_Sheet_Gray']
_folder = "Reconstruction/BD_BB_Chapter2_Orctown_Throne/Meshes"
a = spawn_static_mesh(_mesh_path, _materials, (2086.3608, 2080.797, 1900.0), (0.0, 45.0000434743028, -0.0), (1.0, 1.0, 1.0), "BP_Suburbs_Gate_A_Pillar_Shaft_2", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2086.3608, 2080.797, 2400.0), (0.0, 45.0000434743028, -0.0), (1.0, 1.0, 1.0), "BP_Suburbs_Gate_A_Pillar_Shaft10", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2086.3608, 2080.797, 2300.0), (0.0, 45.0000434743028, -0.0), (1.0, 1.0, 1.0), "BP_Suburbs_Gate_A_Pillar_Shaft11", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2086.3608, 2080.797, 2200.0), (0.0, 45.0000434743028, -0.0), (1.0, 1.0, 1.0), "BP_Suburbs_Gate_A_Pillar_Shaft12", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2086.3608, 2080.797, 2100.0), (0.0, 45.0000434743028, -0.0), (1.0, 1.0, 1.0), "BP_Suburbs_Gate_A_Pillar_Shaft13", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2086.3608, 2080.797, 2000.0), (0.0, 45.0000434743028, -0.0), (1.0, 1.0, 1.0), "BP_Suburbs_Gate_A_Pillar_Shaft14", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2086.3608, 2080.797, 2600.0), (0.0, 45.0000434743028, -0.0), (1.0, 1.0, 1.0), "BP_Suburbs_Gate_A_Pillar_Shaft15", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2086.3608, 2080.797, 2500.0), (0.0, 45.0000434743028, -0.0), (1.0, 1.0, 1.0), "BP_Suburbs_Gate_A_Pillar_Shaft16", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4317.286, 4311.725, 1900.0), (0.0, 45.0000434743028, -0.0), (1.0, 1.0, 1.0), "BP_Suburbs_Gate_A_Pillar_Shaft17", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4317.286, 4311.725, 1800.0), (0.0, 45.0000434743028, -0.0), (1.0, 1.0, 1.0), "BP_Suburbs_Gate_A_Pillar_Shaft18", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4317.286, 4311.725, 1700.0), (0.0, 45.0000434743028, -0.0), (1.0, 1.0, 1.0), "BP_Suburbs_Gate_A_Pillar_Shaft19", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2086.3608, 2080.797, 1800.0), (0.0, 45.0000434743028, -0.0), (1.0, 1.0, 1.0), "BP_Suburbs_Gate_A_Pillar_Shaft2", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4317.286, 4311.725, 1600.0), (0.0, 45.0000434743028, -0.0), (1.0, 1.0, 1.0), "BP_Suburbs_Gate_A_Pillar_Shaft20", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4317.286, 4311.725, 1500.0), (0.0, 45.0000434743028, -0.0), (1.0, 1.0, 1.0), "BP_Suburbs_Gate_A_Pillar_Shaft21", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4317.286, 4311.725, 1400.0), (0.0, 45.0000434743028, -0.0), (1.0, 1.0, 1.0), "BP_Suburbs_Gate_A_Pillar_Shaft22", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4317.286, 4311.725, 1300.0), (0.0, 45.0000434743028, -0.0), (1.0, 1.0, 1.0), "BP_Suburbs_Gate_A_Pillar_Shaft23", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4317.286, 4311.725, 1200.0), (0.0, 45.0000434743028, -0.0), (1.0, 1.0, 1.0), "BP_Suburbs_Gate_A_Pillar_Shaft24", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4317.286, 4311.725, 1100.0), (0.0, 45.0000434743028, -0.0), (1.0, 1.0, 1.0), "BP_Suburbs_Gate_A_Pillar_Shaft25", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4317.286, 4311.725, 2400.0), (0.0, 45.0000434743028, -0.0), (1.0, 1.0, 1.0), "BP_Suburbs_Gate_A_Pillar_Shaft26", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4317.286, 4311.725, 2300.0), (0.0, 45.0000434743028, -0.0), (1.0, 1.0, 1.0), "BP_Suburbs_Gate_A_Pillar_Shaft27", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4317.286, 4311.725, 2200.0), (0.0, 45.0000434743028, -0.0), (1.0, 1.0, 1.0), "BP_Suburbs_Gate_A_Pillar_Shaft28", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4317.286, 4311.725, 2100.0), (0.0, 45.0000434743028, -0.0), (1.0, 1.0, 1.0), "BP_Suburbs_Gate_A_Pillar_Shaft29", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2086.3608, 2080.797, 1700.0), (0.0, 45.0000434743028, -0.0), (1.0, 1.0, 1.0), "BP_Suburbs_Gate_A_Pillar_Shaft3", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4317.286, 4311.725, 2000.0), (0.0, 45.0000434743028, -0.0), (1.0, 1.0, 1.0), "BP_Suburbs_Gate_A_Pillar_Shaft30", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4317.286, 4311.725, 2500.0), (0.0, 45.0000434743028, -0.0), (1.0, 1.0, 1.0), "BP_Suburbs_Gate_A_Pillar_Shaft31_1", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4317.286, 4311.725, 2600.0), (0.0, 45.0000434743028, -0.0), (1.0, 1.0, 1.0), "BP_Suburbs_Gate_A_Pillar_Shaft32_3", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2082.828, 4311.731, 1900.0), (0.0, -44.99990991090605, 0.0), (1.0, 1.0, 1.0), "BP_Suburbs_Gate_A_Pillar_Shaft33", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2082.828, 4311.731, 1800.0), (0.0, -44.99990991090605, 0.0), (1.0, 1.0, 1.0), "BP_Suburbs_Gate_A_Pillar_Shaft34", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2082.828, 4311.731, 1700.0), (0.0, -44.99990991090605, 0.0), (1.0, 1.0, 1.0), "BP_Suburbs_Gate_A_Pillar_Shaft35", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2082.828, 4311.731, 1600.0), (0.0, -44.99990991090605, 0.0), (1.0, 1.0, 1.0), "BP_Suburbs_Gate_A_Pillar_Shaft36", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2082.828, 4311.731, 1500.0), (0.0, -44.99990991090605, 0.0), (1.0, 1.0, 1.0), "BP_Suburbs_Gate_A_Pillar_Shaft37", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2082.828, 4311.731, 1400.0), (0.0, -44.99990991090605, 0.0), (1.0, 1.0, 1.0), "BP_Suburbs_Gate_A_Pillar_Shaft38", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2082.828, 4311.731, 1300.0), (0.0, -44.99990991090605, 0.0), (1.0, 1.0, 1.0), "BP_Suburbs_Gate_A_Pillar_Shaft39", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2086.3608, 2080.797, 1600.0), (0.0, 45.0000434743028, -0.0), (1.0, 1.0, 1.0), "BP_Suburbs_Gate_A_Pillar_Shaft4", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2082.828, 4311.731, 1200.0), (0.0, -44.99990991090605, 0.0), (1.0, 1.0, 1.0), "BP_Suburbs_Gate_A_Pillar_Shaft40", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2082.828, 4311.731, 1100.0), (0.0, -44.99990991090605, 0.0), (1.0, 1.0, 1.0), "BP_Suburbs_Gate_A_Pillar_Shaft41", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2082.828, 4311.731, 2400.0), (0.0, -44.99990991090605, 0.0), (1.0, 1.0, 1.0), "BP_Suburbs_Gate_A_Pillar_Shaft42", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2082.828, 4311.731, 2300.0), (0.0, -44.99990991090605, 0.0), (1.0, 1.0, 1.0), "BP_Suburbs_Gate_A_Pillar_Shaft43", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2082.828, 4311.731, 2200.0), (0.0, -44.99990991090605, 0.0), (1.0, 1.0, 1.0), "BP_Suburbs_Gate_A_Pillar_Shaft44", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2082.828, 4311.731, 2100.0), (0.0, -44.99990991090605, 0.0), (1.0, 1.0, 1.0), "BP_Suburbs_Gate_A_Pillar_Shaft45", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2082.828, 4311.731, 2000.0), (0.0, -44.99990991090605, 0.0), (1.0, 1.0, 1.0), "BP_Suburbs_Gate_A_Pillar_Shaft46", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2082.828, 4311.731, 2600.0), (0.0, -44.99990991090605, 0.0), (1.0, 1.0, 1.0), "BP_Suburbs_Gate_A_Pillar_Shaft47", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2082.828, 4311.731, 2500.0), (0.0, -44.99990991090605, 0.0), (1.0, 1.0, 1.0), "BP_Suburbs_Gate_A_Pillar_Shaft48", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4303.1465, 2091.4124, 1900.0), (0.0, -44.99990991090605, 0.0), (1.0, 1.0, 1.0), "BP_Suburbs_Gate_A_Pillar_Shaft49", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2086.3608, 2080.797, 1500.0), (0.0, 45.0000434743028, -0.0), (1.0, 1.0, 1.0), "BP_Suburbs_Gate_A_Pillar_Shaft5", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4303.1465, 2091.4124, 1800.0), (0.0, -44.99990991090605, 0.0), (1.0, 1.0, 1.0), "BP_Suburbs_Gate_A_Pillar_Shaft50", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4303.1465, 2091.4124, 1700.0), (0.0, -44.99990991090605, 0.0), (1.0, 1.0, 1.0), "BP_Suburbs_Gate_A_Pillar_Shaft51", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4303.1465, 2091.4124, 1600.0), (0.0, -44.99990991090605, 0.0), (1.0, 1.0, 1.0), "BP_Suburbs_Gate_A_Pillar_Shaft52", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4303.1465, 2091.4124, 1500.0), (0.0, -44.99990991090605, 0.0), (1.0, 1.0, 1.0), "BP_Suburbs_Gate_A_Pillar_Shaft53", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4303.1465, 2091.4124, 1400.0), (0.0, -44.99990991090605, 0.0), (1.0, 1.0, 1.0), "BP_Suburbs_Gate_A_Pillar_Shaft54", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4303.1465, 2091.4124, 1300.0), (0.0, -44.99990991090605, 0.0), (1.0, 1.0, 1.0), "BP_Suburbs_Gate_A_Pillar_Shaft55", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4303.1465, 2091.4124, 1200.0), (0.0, -44.99990991090605, 0.0), (1.0, 1.0, 1.0), "BP_Suburbs_Gate_A_Pillar_Shaft56", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4303.1465, 2091.4124, 1100.0), (0.0, -44.99990991090605, 0.0), (1.0, 1.0, 1.0), "BP_Suburbs_Gate_A_Pillar_Shaft57", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4303.1465, 2091.4124, 2400.0), (0.0, -44.99990991090605, 0.0), (1.0, 1.0, 1.0), "BP_Suburbs_Gate_A_Pillar_Shaft58", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4303.1465, 2091.4124, 2300.0), (0.0, -44.99990991090605, 0.0), (1.0, 1.0, 1.0), "BP_Suburbs_Gate_A_Pillar_Shaft59", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2086.3608, 2080.797, 1400.0), (0.0, 45.0000434743028, -0.0), (1.0, 1.0, 1.0), "BP_Suburbs_Gate_A_Pillar_Shaft6", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4303.1465, 2091.4124, 2200.0), (0.0, -44.99990991090605, 0.0), (1.0, 1.0, 1.0), "BP_Suburbs_Gate_A_Pillar_Shaft60", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4303.1465, 2091.4124, 2100.0), (0.0, -44.99990991090605, 0.0), (1.0, 1.0, 1.0), "BP_Suburbs_Gate_A_Pillar_Shaft61", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4303.1465, 2091.4124, 2000.0), (0.0, -44.99990991090605, 0.0), (1.0, 1.0, 1.0), "BP_Suburbs_Gate_A_Pillar_Shaft62", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4303.1465, 2091.4124, 2600.0), (0.0, -44.99990991090605, 0.0), (1.0, 1.0, 1.0), "BP_Suburbs_Gate_A_Pillar_Shaft63", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4303.1465, 2091.4124, 2500.0), (0.0, -44.99990991090605, 0.0), (1.0, 1.0, 1.0), "BP_Suburbs_Gate_A_Pillar_Shaft64", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2086.3608, 2080.797, 1300.0), (0.0, 45.0000434743028, -0.0), (1.0, 1.0, 1.0), "BP_Suburbs_Gate_A_Pillar_Shaft7", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2086.3608, 2080.797, 1200.0), (0.0, 45.0000434743028, -0.0), (1.0, 1.0, 1.0), "BP_Suburbs_Gate_A_Pillar_Shaft8", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2086.3608, 2080.797, 1100.0), (0.0, 45.0000434743028, -0.0), (1.0, 1.0, 1.0), "BP_Suburbs_Gate_A_Pillar_Shaft9", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5794.3555, 4883.705, 1302.3932), (0.0, -61.40539497196487, 0.0), (1.0, 1.0, 1.0), "Suburbs_Gate_A_Pillar_Shaft_1242", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (6033.649, 4444.6846, 1402.3932), (0.0, -61.40539497196487, 0.0), (1.0, 1.0, 1.0), "Suburbs_Gate_A_Pillar_Shaft10", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (6033.649, 4444.6846, 1502.3932), (0.0, -61.40539497196487, 0.0), (1.0, 1.0, 1.0), "Suburbs_Gate_A_Pillar_Shaft11", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5794.3555, 4883.705, 1102.3932), (0.0, -61.40539497196487, 0.0), (1.0, 1.0, 1.0), "Suburbs_Gate_A_Pillar_Shaft113_1661", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5794.3555, 4883.705, 1202.3932), (0.0, -61.40539497196487, 0.0), (1.0, 1.0, 1.0), "Suburbs_Gate_A_Pillar_Shaft114_1663", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (6033.649, 4444.6846, 1202.3932), (0.0, -61.40539497196487, 0.0), (1.0, 1.0, 1.0), "Suburbs_Gate_A_Pillar_Shaft115_1665", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (6033.649, 4444.6846, 1102.3932), (0.0, -61.40539497196487, 0.0), (1.0, 1.0, 1.0), "Suburbs_Gate_A_Pillar_Shaft116_1667", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (6096.601, 4314.425, 1202.3894), (0.0, -78.86670200924122, 0.0), (1.0, 1.0, 1.0), "Suburbs_Gate_A_Pillar_Shaft118_1705", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (6033.649, 4444.6846, 1602.3932), (0.0, -61.40539497196487, 0.0), (1.0, 1.0, 1.0), "Suburbs_Gate_A_Pillar_Shaft12", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4382.943, 5981.1455, 1302.3932), (0.0, -23.317107930497365, 0.0), (1.0, 1.0, 1.0), "Suburbs_Gate_A_Pillar_Shaft121", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4382.943, 5981.1455, 1402.3932), (0.0, -23.317107930497365, 0.0), (1.0, 1.0, 1.0), "Suburbs_Gate_A_Pillar_Shaft122", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4382.943, 5981.1455, 1502.3932), (0.0, -23.317107930497365, 0.0), (1.0, 1.0, 1.0), "Suburbs_Gate_A_Pillar_Shaft123", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4382.943, 5981.1455, 1602.3932), (0.0, -23.317107930497365, 0.0), (1.0, 1.0, 1.0), "Suburbs_Gate_A_Pillar_Shaft124", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4382.943, 5981.1455, 1702.3932), (0.0, -23.317107930497365, 0.0), (1.0, 1.0, 1.0), "Suburbs_Gate_A_Pillar_Shaft125", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4382.943, 5981.1455, 1802.3932), (0.0, -23.317107930497365, 0.0), (1.0, 1.0, 1.0), "Suburbs_Gate_A_Pillar_Shaft126", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4382.943, 5981.1455, 1902.3932), (0.0, -23.317107930497365, 0.0), (1.0, 1.0, 1.0), "Suburbs_Gate_A_Pillar_Shaft127", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4382.943, 5981.1455, 2002.3932), (0.0, -23.317107930497365, 0.0), (1.0, 1.0, 1.0), "Suburbs_Gate_A_Pillar_Shaft128", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (6033.649, 4444.6846, 1702.3932), (0.0, -61.40539497196487, 0.0), (1.0, 1.0, 1.0), "Suburbs_Gate_A_Pillar_Shaft13", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (6003.747, 2043.8492, 1202.3894), (0.0, -100.16161761252525, 0.0), (1.0, 1.0, 1.0), "Suburbs_Gate_A_Pillar_Shaft131", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (6003.747, 2043.8492, 1102.3894), (0.0, -100.16161761252525, 0.0), (1.0, 1.0, 1.0), "Suburbs_Gate_A_Pillar_Shaft132", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5958.4795, 1907.8461, 1102.3894), (0.0, -114.47987896720926, 0.0), (1.0, 1.0, 1.0), "Suburbs_Gate_A_Pillar_Shaft133", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5958.4795, 1907.8461, 1202.3894), (0.0, -114.47987896720926, 0.0), (1.0, 1.0, 1.0), "Suburbs_Gate_A_Pillar_Shaft134", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5751.2637, 1452.8163, 1202.3894), (0.0, -114.47987896720926, 0.0), (1.0, 1.0, 1.0), "Suburbs_Gate_A_Pillar_Shaft135", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5751.2637, 1452.8163, 1102.3894), (0.0, -114.47987896720926, 0.0), (1.0, 1.0, 1.0), "Suburbs_Gate_A_Pillar_Shaft136", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (6033.649, 4444.6846, 1802.3932), (0.0, -61.40539497196487, 0.0), (1.0, 1.0, 1.0), "Suburbs_Gate_A_Pillar_Shaft14", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (6033.649, 4444.6846, 1902.3932), (0.0, -61.40539497196487, 0.0), (1.0, 1.0, 1.0), "Suburbs_Gate_A_Pillar_Shaft15", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (6033.649, 4444.6846, 2002.3932), (0.0, -61.40539497196487, 0.0), (1.0, 1.0, 1.0), "Suburbs_Gate_A_Pillar_Shaft16", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4842.103, 5783.2236, 1302.3932), (0.0, -23.317107930497365, 0.0), (1.0, 1.0, 1.0), "Suburbs_Gate_A_Pillar_Shaft161", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4842.103, 5783.2236, 1402.3932), (0.0, -23.317107930497365, 0.0), (1.0, 1.0, 1.0), "Suburbs_Gate_A_Pillar_Shaft162", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4842.103, 5783.2236, 1502.3932), (0.0, -23.317107930497365, 0.0), (1.0, 1.0, 1.0), "Suburbs_Gate_A_Pillar_Shaft163", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4842.103, 5783.2236, 1602.3932), (0.0, -23.317107930497365, 0.0), (1.0, 1.0, 1.0), "Suburbs_Gate_A_Pillar_Shaft164", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4842.103, 5783.2236, 1702.3932), (0.0, -23.317107930497365, 0.0), (1.0, 1.0, 1.0), "Suburbs_Gate_A_Pillar_Shaft165", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4842.103, 5783.2236, 1802.3932), (0.0, -23.317107930497365, 0.0), (1.0, 1.0, 1.0), "Suburbs_Gate_A_Pillar_Shaft166", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4842.103, 5783.2236, 1902.3932), (0.0, -23.317107930497365, 0.0), (1.0, 1.0, 1.0), "Suburbs_Gate_A_Pillar_Shaft167", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4842.103, 5783.2236, 2002.3932), (0.0, -23.317107930497365, 0.0), (1.0, 1.0, 1.0), "Suburbs_Gate_A_Pillar_Shaft168", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4382.943, 5981.1455, 1102.3932), (0.0, -23.317107930497365, 0.0), (1.0, 1.0, 1.0), "Suburbs_Gate_A_Pillar_Shaft169", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (6096.601, 4314.425, 1302.3894), (0.0, -78.86670200924122, 0.0), (1.0, 1.0, 1.0), "Suburbs_Gate_A_Pillar_Shaft17", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4382.943, 5981.1455, 1202.3932), (0.0, -23.317107930497365, 0.0), (1.0, 1.0, 1.0), "Suburbs_Gate_A_Pillar_Shaft170", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4842.103, 5783.2236, 1202.3932), (0.0, -23.317107930497365, 0.0), (1.0, 1.0, 1.0), "Suburbs_Gate_A_Pillar_Shaft171", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4842.103, 5783.2236, 1102.3932), (0.0, -23.317107930497365, 0.0), (1.0, 1.0, 1.0), "Suburbs_Gate_A_Pillar_Shaft172", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3734.3518, 6029.182, 1302.3932), (0.0, -1.4053344839095196, 0.0), (1.0, 1.0, 1.0), "Suburbs_Gate_A_Pillar_Shaft173", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3734.3518, 6029.182, 1402.3932), (0.0, -1.4053344839095196, 0.0), (1.0, 1.0, 1.0), "Suburbs_Gate_A_Pillar_Shaft174", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3734.3518, 6029.182, 1502.3932), (0.0, -1.4053344839095196, 0.0), (1.0, 1.0, 1.0), "Suburbs_Gate_A_Pillar_Shaft175", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3734.3518, 6029.182, 1602.3932), (0.0, -1.4053344839095196, 0.0), (1.0, 1.0, 1.0), "Suburbs_Gate_A_Pillar_Shaft176", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3734.3518, 6029.182, 1702.3932), (0.0, -1.4053344839095196, 0.0), (1.0, 1.0, 1.0), "Suburbs_Gate_A_Pillar_Shaft177", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3734.3518, 6029.182, 1802.3932), (0.0, -1.4053344839095196, 0.0), (1.0, 1.0, 1.0), "Suburbs_Gate_A_Pillar_Shaft178", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3734.3518, 6029.182, 1902.3932), (0.0, -1.4053344839095196, 0.0), (1.0, 1.0, 1.0), "Suburbs_Gate_A_Pillar_Shaft179", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (6096.601, 4314.425, 1402.3894), (0.0, -78.86670200924122, 0.0), (1.0, 1.0, 1.0), "Suburbs_Gate_A_Pillar_Shaft18", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3734.3518, 6029.182, 2002.3932), (0.0, -1.4053344839095196, 0.0), (1.0, 1.0, 1.0), "Suburbs_Gate_A_Pillar_Shaft180", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4234.198, 6016.9062, 1302.3932), (0.0, -1.4053344839095196, 0.0), (1.0, 1.0, 1.0), "Suburbs_Gate_A_Pillar_Shaft181", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4234.198, 6016.9062, 1402.3932), (0.0, -1.4053344839095196, 0.0), (1.0, 1.0, 1.0), "Suburbs_Gate_A_Pillar_Shaft182", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4234.198, 6016.9062, 1502.3932), (0.0, -1.4053344839095196, 0.0), (1.0, 1.0, 1.0), "Suburbs_Gate_A_Pillar_Shaft183", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4234.198, 6016.9062, 1602.3932), (0.0, -1.4053344839095196, 0.0), (1.0, 1.0, 1.0), "Suburbs_Gate_A_Pillar_Shaft184", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4234.198, 6016.9062, 1702.3932), (0.0, -1.4053344839095196, 0.0), (1.0, 1.0, 1.0), "Suburbs_Gate_A_Pillar_Shaft185", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4234.198, 6016.9062, 1802.3932), (0.0, -1.4053344839095196, 0.0), (1.0, 1.0, 1.0), "Suburbs_Gate_A_Pillar_Shaft186", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4234.198, 6016.9062, 1902.3932), (0.0, -1.4053344839095196, 0.0), (1.0, 1.0, 1.0), "Suburbs_Gate_A_Pillar_Shaft187", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4234.198, 6016.9062, 2002.3932), (0.0, -1.4053344839095196, 0.0), (1.0, 1.0, 1.0), "Suburbs_Gate_A_Pillar_Shaft188", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (6096.601, 4314.425, 1502.3894), (0.0, -78.86670200924122, 0.0), (1.0, 1.0, 1.0), "Suburbs_Gate_A_Pillar_Shaft19", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3734.3518, 6029.182, 1202.3932), (0.0, -1.4053344839095196, 0.0), (1.0, 1.0, 1.0), "Suburbs_Gate_A_Pillar_Shaft190", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4234.198, 6016.9062, 1202.3932), (0.0, -1.4053344839095196, 0.0), (1.0, 1.0, 1.0), "Suburbs_Gate_A_Pillar_Shaft191", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4234.198, 6016.9062, 1102.3932), (0.0, -1.4053344839095196, 0.0), (1.0, 1.0, 1.0), "Suburbs_Gate_A_Pillar_Shaft192", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1819.2482, 5901.3955, 1502.3932), (0.0, 16.633018401922776, -0.0), (1.0, 1.0, 1.0), "Suburbs_Gate_A_Pillar_Shaft195", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1819.2482, 5901.3955, 1602.3932), (0.0, 16.633018401922776, -0.0), (1.0, 1.0, 1.0), "Suburbs_Gate_A_Pillar_Shaft196", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1819.2482, 5901.3955, 1702.3932), (0.0, 16.633018401922776, -0.0), (1.0, 1.0, 1.0), "Suburbs_Gate_A_Pillar_Shaft197", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1819.2482, 5901.3955, 1802.3932), (0.0, 16.633018401922776, -0.0), (1.0, 1.0, 1.0), "Suburbs_Gate_A_Pillar_Shaft198", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1819.2482, 5901.3955, 1902.3932), (0.0, 16.633018401922776, -0.0), (1.0, 1.0, 1.0), "Suburbs_Gate_A_Pillar_Shaft199", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5794.3555, 4883.705, 1402.3932), (0.0, -61.40539497196487, 0.0), (1.0, 1.0, 1.0), "Suburbs_Gate_A_Pillar_Shaft2", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (6096.601, 4314.425, 1602.3894), (0.0, -78.86670200924122, 0.0), (1.0, 1.0, 1.0), "Suburbs_Gate_A_Pillar_Shaft20", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1819.2482, 5901.3955, 2002.3932), (0.0, 16.633018401922776, -0.0), (1.0, 1.0, 1.0), "Suburbs_Gate_A_Pillar_Shaft200", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2298.3494, 6044.4404, 1502.3932), (0.0, 16.633018401922776, -0.0), (1.0, 1.0, 1.0), "Suburbs_Gate_A_Pillar_Shaft203", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2298.3494, 6044.4404, 1602.3932), (0.0, 16.633018401922776, -0.0), (1.0, 1.0, 1.0), "Suburbs_Gate_A_Pillar_Shaft204", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2298.3494, 6044.4404, 1702.3932), (0.0, 16.633018401922776, -0.0), (1.0, 1.0, 1.0), "Suburbs_Gate_A_Pillar_Shaft205", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2298.3494, 6044.4404, 1802.3932), (0.0, 16.633018401922776, -0.0), (1.0, 1.0, 1.0), "Suburbs_Gate_A_Pillar_Shaft206", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2298.3494, 6044.4404, 1902.3932), (0.0, 16.633018401922776, -0.0), (1.0, 1.0, 1.0), "Suburbs_Gate_A_Pillar_Shaft207", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2298.3494, 6044.4404, 2002.3932), (0.0, 16.633018401922776, -0.0), (1.0, 1.0, 1.0), "Suburbs_Gate_A_Pillar_Shaft208", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (6096.601, 4314.425, 1702.3894), (0.0, -78.86670200924122, 0.0), (1.0, 1.0, 1.0), "Suburbs_Gate_A_Pillar_Shaft21", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1259.5024, 5576.841, 1302.3932), (0.0, 31.35413366225017, -0.0), (1.0, 1.0, 1.0), "Suburbs_Gate_A_Pillar_Shaft213", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1259.5024, 5576.841, 1402.3932), (0.0, 31.35413366225017, -0.0), (1.0, 1.0, 1.0), "Suburbs_Gate_A_Pillar_Shaft214", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1259.5024, 5576.841, 1502.3932), (0.0, 31.35413366225017, -0.0), (1.0, 1.0, 1.0), "Suburbs_Gate_A_Pillar_Shaft215", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1259.5024, 5576.841, 1602.3932), (0.0, 31.35413366225017, -0.0), (1.0, 1.0, 1.0), "Suburbs_Gate_A_Pillar_Shaft216", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1259.5024, 5576.841, 1702.3932), (0.0, 31.35413366225017, -0.0), (1.0, 1.0, 1.0), "Suburbs_Gate_A_Pillar_Shaft217", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1259.5024, 5576.841, 1802.3932), (0.0, 31.35413366225017, -0.0), (1.0, 1.0, 1.0), "Suburbs_Gate_A_Pillar_Shaft218", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1259.5024, 5576.841, 1902.3932), (0.0, 31.35413366225017, -0.0), (1.0, 1.0, 1.0), "Suburbs_Gate_A_Pillar_Shaft219", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (6096.601, 4314.425, 1802.3894), (0.0, -78.86670200924122, 0.0), (1.0, 1.0, 1.0), "Suburbs_Gate_A_Pillar_Shaft22", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1259.5024, 5576.841, 2002.3932), (0.0, 31.35413366225017, -0.0), (1.0, 1.0, 1.0), "Suburbs_Gate_A_Pillar_Shaft220", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1686.5027, 5836.952, 1502.3932), (0.0, 31.35413366225017, -0.0), (1.0, 1.0, 1.0), "Suburbs_Gate_A_Pillar_Shaft223", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1686.5027, 5836.952, 1602.3932), (0.0, 31.35413366225017, -0.0), (1.0, 1.0, 1.0), "Suburbs_Gate_A_Pillar_Shaft224", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1686.5027, 5836.952, 1702.3932), (0.0, 31.35413366225017, -0.0), (1.0, 1.0, 1.0), "Suburbs_Gate_A_Pillar_Shaft225", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1686.5027, 5836.952, 1802.3932), (0.0, 31.35413366225017, -0.0), (1.0, 1.0, 1.0), "Suburbs_Gate_A_Pillar_Shaft226", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1686.5027, 5836.952, 1902.3932), (0.0, 31.35413366225017, -0.0), (1.0, 1.0, 1.0), "Suburbs_Gate_A_Pillar_Shaft227", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1686.5027, 5836.952, 2002.3932), (0.0, 31.35413366225017, -0.0), (1.0, 1.0, 1.0), "Suburbs_Gate_A_Pillar_Shaft228", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (6096.601, 4314.425, 1902.3894), (0.0, -78.86670200924122, 0.0), (1.0, 1.0, 1.0), "Suburbs_Gate_A_Pillar_Shaft23", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (811.309, 5110.0933, 1302.3932), (0.0, 48.292735185616124, -0.0), (1.0, 1.0, 1.0), "Suburbs_Gate_A_Pillar_Shaft233", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (811.309, 5110.0933, 1402.3932), (0.0, 48.292735185616124, -0.0), (1.0, 1.0, 1.0), "Suburbs_Gate_A_Pillar_Shaft234", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (811.309, 5110.0933, 1502.3932), (0.0, 48.292735185616124, -0.0), (1.0, 1.0, 1.0), "Suburbs_Gate_A_Pillar_Shaft235", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (811.309, 5110.0933, 1602.3932), (0.0, 48.292735185616124, -0.0), (1.0, 1.0, 1.0), "Suburbs_Gate_A_Pillar_Shaft236", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (811.309, 5110.0933, 1702.3932), (0.0, 48.292735185616124, -0.0), (1.0, 1.0, 1.0), "Suburbs_Gate_A_Pillar_Shaft237", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (811.309, 5110.0933, 1802.3932), (0.0, 48.292735185616124, -0.0), (1.0, 1.0, 1.0), "Suburbs_Gate_A_Pillar_Shaft238", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (811.309, 5110.0933, 1902.3932), (0.0, 48.292735185616124, -0.0), (1.0, 1.0, 1.0), "Suburbs_Gate_A_Pillar_Shaft239", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (6096.601, 4314.425, 2002.3894), (0.0, -78.86670200924122, 0.0), (1.0, 1.0, 1.0), "Suburbs_Gate_A_Pillar_Shaft24", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (811.309, 5110.0933, 2002.3932), (0.0, 48.292735185616124, -0.0), (1.0, 1.0, 1.0), "Suburbs_Gate_A_Pillar_Shaft240", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1144.0029, 5483.3286, 1302.3932), (0.0, 48.292735185616124, -0.0), (1.0, 1.0, 1.0), "Suburbs_Gate_A_Pillar_Shaft241", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1144.0029, 5483.3286, 1402.3932), (0.0, 48.292735185616124, -0.0), (1.0, 1.0, 1.0), "Suburbs_Gate_A_Pillar_Shaft242", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1144.0029, 5483.3286, 1502.3932), (0.0, 48.292735185616124, -0.0), (1.0, 1.0, 1.0), "Suburbs_Gate_A_Pillar_Shaft243", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1144.0029, 5483.3286, 1602.3932), (0.0, 48.292735185616124, -0.0), (1.0, 1.0, 1.0), "Suburbs_Gate_A_Pillar_Shaft244", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1144.0029, 5483.3286, 1702.3932), (0.0, 48.292735185616124, -0.0), (1.0, 1.0, 1.0), "Suburbs_Gate_A_Pillar_Shaft245", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1144.0029, 5483.3286, 1802.3932), (0.0, 48.292735185616124, -0.0), (1.0, 1.0, 1.0), "Suburbs_Gate_A_Pillar_Shaft246", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1144.0029, 5483.3286, 1902.3932), (0.0, 48.292735185616124, -0.0), (1.0, 1.0, 1.0), "Suburbs_Gate_A_Pillar_Shaft247", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1144.0029, 5483.3286, 2002.3932), (0.0, 48.292735185616124, -0.0), (1.0, 1.0, 1.0), "Suburbs_Gate_A_Pillar_Shaft248", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (811.309, 5110.0933, 1102.3932), (0.0, 48.292735185616124, -0.0), (1.0, 1.0, 1.0), "Suburbs_Gate_A_Pillar_Shaft249", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (811.309, 5110.0933, 1202.3932), (0.0, 48.292735185616124, -0.0), (1.0, 1.0, 1.0), "Suburbs_Gate_A_Pillar_Shaft250", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1144.0029, 5483.3286, 1202.3932), (0.0, 48.292735185616124, -0.0), (1.0, 1.0, 1.0), "Suburbs_Gate_A_Pillar_Shaft251", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1144.0029, 5483.3286, 1102.3932), (0.0, 48.292735185616124, -0.0), (1.0, 1.0, 1.0), "Suburbs_Gate_A_Pillar_Shaft252", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (976.9271, 1006.15717, 1302.3932), (0.0, 125.22933924820616, -0.0), (1.0, 1.0, 1.0), "Suburbs_Gate_A_Pillar_Shaft253", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (976.9271, 1006.15717, 1402.3932), (0.0, 125.22933924820616, -0.0), (1.0, 1.0, 1.0), "Suburbs_Gate_A_Pillar_Shaft254", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (976.9271, 1006.15717, 1502.3932), (0.0, 125.22933924820616, -0.0), (1.0, 1.0, 1.0), "Suburbs_Gate_A_Pillar_Shaft255", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (976.9271, 1006.15717, 1602.3932), (0.0, 125.22933924820616, -0.0), (1.0, 1.0, 1.0), "Suburbs_Gate_A_Pillar_Shaft256", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (976.9271, 1006.15717, 1702.3932), (0.0, 125.22933924820616, -0.0), (1.0, 1.0, 1.0), "Suburbs_Gate_A_Pillar_Shaft257", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (976.9271, 1006.15717, 1802.3932), (0.0, 125.22933924820616, -0.0), (1.0, 1.0, 1.0), "Suburbs_Gate_A_Pillar_Shaft258", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (976.9271, 1006.15717, 1902.3932), (0.0, 125.22933924820616, -0.0), (1.0, 1.0, 1.0), "Suburbs_Gate_A_Pillar_Shaft259", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (976.9271, 1006.15717, 2002.3932), (0.0, 125.22933924820616, -0.0), (1.0, 1.0, 1.0), "Suburbs_Gate_A_Pillar_Shaft260", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (688.54956, 1414.6007, 1302.3932), (0.0, 125.22933924820616, -0.0), (1.0, 1.0, 1.0), "Suburbs_Gate_A_Pillar_Shaft261", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (688.54956, 1414.6007, 1402.3932), (0.0, 125.22933924820616, -0.0), (1.0, 1.0, 1.0), "Suburbs_Gate_A_Pillar_Shaft262", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (688.54956, 1414.6007, 1502.3932), (0.0, 125.22933924820616, -0.0), (1.0, 1.0, 1.0), "Suburbs_Gate_A_Pillar_Shaft263", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (688.54956, 1414.6007, 1602.3932), (0.0, 125.22933924820616, -0.0), (1.0, 1.0, 1.0), "Suburbs_Gate_A_Pillar_Shaft264", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (688.54956, 1414.6007, 1702.3932), (0.0, 125.22933924820616, -0.0), (1.0, 1.0, 1.0), "Suburbs_Gate_A_Pillar_Shaft265", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (688.54956, 1414.6007, 1802.3932), (0.0, 125.22933924820616, -0.0), (1.0, 1.0, 1.0), "Suburbs_Gate_A_Pillar_Shaft266", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (688.54956, 1414.6007, 1902.3932), (0.0, 125.22933924820616, -0.0), (1.0, 1.0, 1.0), "Suburbs_Gate_A_Pillar_Shaft267", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (688.54956, 1414.6007, 2002.3932), (0.0, 125.22933924820616, -0.0), (1.0, 1.0, 1.0), "Suburbs_Gate_A_Pillar_Shaft268", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (976.9271, 1006.15717, 1102.3932), (0.0, 125.22933924820616, -0.0), (1.0, 1.0, 1.0), "Suburbs_Gate_A_Pillar_Shaft269", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (6193.1226, 3823.8342, 1502.3894), (0.0, -78.86670200924122, 0.0), (1.0, 1.0, 1.0), "Suburbs_Gate_A_Pillar_Shaft27", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (976.9271, 1006.15717, 1202.3932), (0.0, 125.22933924820616, -0.0), (1.0, 1.0, 1.0), "Suburbs_Gate_A_Pillar_Shaft270", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (688.54956, 1414.6007, 1202.3932), (0.0, 125.22933924820616, -0.0), (1.0, 1.0, 1.0), "Suburbs_Gate_A_Pillar_Shaft271", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (688.54956, 1414.6007, 1102.3932), (0.0, 125.22933924820616, -0.0), (1.0, 1.0, 1.0), "Suburbs_Gate_A_Pillar_Shaft272", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1499.2539, 619.74426, 1502.3932), (0.0, 146.34639554076125, -0.0), (1.0, 1.0, 1.0), "Suburbs_Gate_A_Pillar_Shaft275", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1499.2539, 619.74426, 1602.3932), (0.0, 146.34639554076125, -0.0), (1.0, 1.0, 1.0), "Suburbs_Gate_A_Pillar_Shaft276", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1499.2539, 619.74426, 1702.3932), (0.0, 146.34639554076125, -0.0), (1.0, 1.0, 1.0), "Suburbs_Gate_A_Pillar_Shaft277", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1499.2539, 619.74426, 1802.3932), (0.0, 146.34639554076125, -0.0), (1.0, 1.0, 1.0), "Suburbs_Gate_A_Pillar_Shaft278", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1499.2539, 619.74426, 1902.3932), (0.0, 146.34639554076125, -0.0), (1.0, 1.0, 1.0), "Suburbs_Gate_A_Pillar_Shaft279", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (6193.1226, 3823.8342, 1602.3894), (0.0, -78.86670200924122, 0.0), (1.0, 1.0, 1.0), "Suburbs_Gate_A_Pillar_Shaft28", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1499.2539, 619.74426, 2002.3932), (0.0, 146.34639554076125, -0.0), (1.0, 1.0, 1.0), "Suburbs_Gate_A_Pillar_Shaft280", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1083.0892, 896.8623, 1302.3932), (0.0, 146.34625296062157, -0.0), (1.0, 1.0, 1.0), "Suburbs_Gate_A_Pillar_Shaft281", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1083.0892, 896.8623, 1402.3932), (0.0, 146.34625296062157, -0.0), (1.0, 1.0, 1.0), "Suburbs_Gate_A_Pillar_Shaft282", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1083.0892, 896.8623, 1502.3932), (0.0, 146.34625296062157, -0.0), (1.0, 1.0, 1.0), "Suburbs_Gate_A_Pillar_Shaft283", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1083.0892, 896.8623, 1602.3932), (0.0, 146.34625296062157, -0.0), (1.0, 1.0, 1.0), "Suburbs_Gate_A_Pillar_Shaft284", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1083.0892, 896.8623, 1702.3932), (0.0, 146.34625296062157, -0.0), (1.0, 1.0, 1.0), "Suburbs_Gate_A_Pillar_Shaft285", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1083.0892, 896.8623, 1802.3932), (0.0, 146.34625296062157, -0.0), (1.0, 1.0, 1.0), "Suburbs_Gate_A_Pillar_Shaft286", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1083.0892, 896.8623, 1902.3932), (0.0, 146.34625296062157, -0.0), (1.0, 1.0, 1.0), "Suburbs_Gate_A_Pillar_Shaft287", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1083.0892, 896.8623, 2002.3932), (0.0, 146.34625296062157, -0.0), (1.0, 1.0, 1.0), "Suburbs_Gate_A_Pillar_Shaft288", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (6193.1226, 3823.8342, 1702.3894), (0.0, -78.86670200924122, 0.0), (1.0, 1.0, 1.0), "Suburbs_Gate_A_Pillar_Shaft29", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2427.5225, 360.02313, 1502.3932), (0.0, 169.64131655281435, -0.0), (1.0, 1.0, 1.0), "Suburbs_Gate_A_Pillar_Shaft295", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2427.5225, 360.02313, 1602.3932), (0.0, 169.64131655281435, -0.0), (1.0, 1.0, 1.0), "Suburbs_Gate_A_Pillar_Shaft296", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2427.5225, 360.02313, 1702.3932), (0.0, 169.64131655281435, -0.0), (1.0, 1.0, 1.0), "Suburbs_Gate_A_Pillar_Shaft297", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2427.5225, 360.02313, 1802.3932), (0.0, 169.64131655281435, -0.0), (1.0, 1.0, 1.0), "Suburbs_Gate_A_Pillar_Shaft298", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2427.5225, 360.02313, 1902.3932), (0.0, 169.64131655281435, -0.0), (1.0, 1.0, 1.0), "Suburbs_Gate_A_Pillar_Shaft299", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5794.3555, 4883.705, 1502.3932), (0.0, -61.40539497196487, 0.0), (1.0, 1.0, 1.0), "Suburbs_Gate_A_Pillar_Shaft3", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (6193.1226, 3823.8342, 1802.3894), (0.0, -78.86670200924122, 0.0), (1.0, 1.0, 1.0), "Suburbs_Gate_A_Pillar_Shaft30", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2427.5225, 360.02313, 2002.3932), (0.0, 169.64131655281435, -0.0), (1.0, 1.0, 1.0), "Suburbs_Gate_A_Pillar_Shaft300", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1935.691, 449.99496, 1502.3932), (0.0, 169.64131655281435, -0.0), (1.0, 1.0, 1.0), "Suburbs_Gate_A_Pillar_Shaft303", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1935.691, 449.99496, 1602.3932), (0.0, 169.64131655281435, -0.0), (1.0, 1.0, 1.0), "Suburbs_Gate_A_Pillar_Shaft304", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1935.691, 449.99496, 1702.3932), (0.0, 169.64131655281435, -0.0), (1.0, 1.0, 1.0), "Suburbs_Gate_A_Pillar_Shaft305", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1935.691, 449.99496, 1802.3932), (0.0, 169.64131655281435, -0.0), (1.0, 1.0, 1.0), "Suburbs_Gate_A_Pillar_Shaft306", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1935.691, 449.99496, 1902.3932), (0.0, 169.64131655281435, -0.0), (1.0, 1.0, 1.0), "Suburbs_Gate_A_Pillar_Shaft307", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1935.691, 449.99496, 2002.3932), (0.0, 169.64131655281435, -0.0), (1.0, 1.0, 1.0), "Suburbs_Gate_A_Pillar_Shaft308", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2427.5225, 360.02313, 1102.3932), (0.0, 169.64131655281435, -0.0), (1.0, 1.0, 1.0), "Suburbs_Gate_A_Pillar_Shaft309", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (6193.1226, 3823.8342, 1902.3894), (0.0, -78.86670200924122, 0.0), (1.0, 1.0, 1.0), "Suburbs_Gate_A_Pillar_Shaft31", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4915.054, 616.967, 1302.3932), (0.0, -160.68884514924872, 0.0), (1.0, 1.0, 1.0), "Suburbs_Gate_A_Pillar_Shaft313", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4915.054, 616.967, 1402.3932), (0.0, -160.68884514924872, 0.0), (1.0, 1.0, 1.0), "Suburbs_Gate_A_Pillar_Shaft314", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4915.054, 616.967, 1502.3932), (0.0, -160.68884514924872, 0.0), (1.0, 1.0, 1.0), "Suburbs_Gate_A_Pillar_Shaft315", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4915.054, 616.967, 1602.3932), (0.0, -160.68884514924872, 0.0), (1.0, 1.0, 1.0), "Suburbs_Gate_A_Pillar_Shaft316", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4915.054, 616.967, 1702.3932), (0.0, -160.68884514924872, 0.0), (1.0, 1.0, 1.0), "Suburbs_Gate_A_Pillar_Shaft317", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4915.054, 616.967, 1802.3932), (0.0, -160.68884514924872, 0.0), (1.0, 1.0, 1.0), "Suburbs_Gate_A_Pillar_Shaft318", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4915.054, 616.967, 1902.3932), (0.0, -160.68884514924872, 0.0), (1.0, 1.0, 1.0), "Suburbs_Gate_A_Pillar_Shaft319", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (6193.1226, 3823.8342, 2002.3894), (0.0, -78.86670200924122, 0.0), (1.0, 1.0, 1.0), "Suburbs_Gate_A_Pillar_Shaft32", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4915.054, 616.967, 2002.3932), (0.0, -160.68884514924872, 0.0), (1.0, 1.0, 1.0), "Suburbs_Gate_A_Pillar_Shaft320", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4443.1655, 451.68658, 1302.3932), (0.0, -160.68884514924872, 0.0), (1.0, 1.0, 1.0), "Suburbs_Gate_A_Pillar_Shaft321", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4443.1655, 451.68658, 1402.3932), (0.0, -160.68884514924872, 0.0), (1.0, 1.0, 1.0), "Suburbs_Gate_A_Pillar_Shaft322", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4443.1655, 451.68658, 1502.3932), (0.0, -160.68884514924872, 0.0), (1.0, 1.0, 1.0), "Suburbs_Gate_A_Pillar_Shaft323", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4443.1655, 451.68658, 1602.3932), (0.0, -160.68884514924872, 0.0), (1.0, 1.0, 1.0), "Suburbs_Gate_A_Pillar_Shaft324", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4443.1655, 451.68658, 1702.3932), (0.0, -160.68884514924872, 0.0), (1.0, 1.0, 1.0), "Suburbs_Gate_A_Pillar_Shaft325", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4443.1655, 451.68658, 1802.3932), (0.0, -160.68884514924872, 0.0), (1.0, 1.0, 1.0), "Suburbs_Gate_A_Pillar_Shaft326", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4443.1655, 451.68658, 1902.3932), (0.0, -160.68884514924872, 0.0), (1.0, 1.0, 1.0), "Suburbs_Gate_A_Pillar_Shaft327", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4443.1655, 451.68658, 2002.3932), (0.0, -160.68884514924872, 0.0), (1.0, 1.0, 1.0), "Suburbs_Gate_A_Pillar_Shaft328", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4915.054, 616.967, 1102.3932), (0.0, -160.68884514924872, 0.0), (1.0, 1.0, 1.0), "Suburbs_Gate_A_Pillar_Shaft329", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4915.054, 616.967, 1202.3932), (0.0, -160.68884514924872, 0.0), (1.0, 1.0, 1.0), "Suburbs_Gate_A_Pillar_Shaft330", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4443.1655, 451.68658, 1202.3932), (0.0, -160.68884514924872, 0.0), (1.0, 1.0, 1.0), "Suburbs_Gate_A_Pillar_Shaft331", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4443.1655, 451.68658, 1102.3932), (0.0, -160.68884514924872, 0.0), (1.0, 1.0, 1.0), "Suburbs_Gate_A_Pillar_Shaft332", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4301.645, 425.87326, 1302.3932), (0.0, -172.2991444559567, 0.0), (1.0, 1.0, 1.0), "Suburbs_Gate_A_Pillar_Shaft333", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4301.645, 425.87326, 1402.3932), (0.0, -172.2991444559567, 0.0), (1.0, 1.0, 1.0), "Suburbs_Gate_A_Pillar_Shaft334", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4301.645, 425.87326, 1502.3932), (0.0, -172.2991444559567, 0.0), (1.0, 1.0, 1.0), "Suburbs_Gate_A_Pillar_Shaft335", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4301.645, 425.87326, 1602.3932), (0.0, -172.2991444559567, 0.0), (1.0, 1.0, 1.0), "Suburbs_Gate_A_Pillar_Shaft336", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4301.645, 425.87326, 1702.3932), (0.0, -172.2991444559567, 0.0), (1.0, 1.0, 1.0), "Suburbs_Gate_A_Pillar_Shaft337", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4301.645, 425.87326, 1802.3932), (0.0, -172.2991444559567, 0.0), (1.0, 1.0, 1.0), "Suburbs_Gate_A_Pillar_Shaft338", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4301.645, 425.87326, 1902.3932), (0.0, -172.2991444559567, 0.0), (1.0, 1.0, 1.0), "Suburbs_Gate_A_Pillar_Shaft339", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4301.645, 425.87326, 2002.3932), (0.0, -172.2991444559567, 0.0), (1.0, 1.0, 1.0), "Suburbs_Gate_A_Pillar_Shaft340", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3806.1475, 358.956, 1402.3932), (0.0, -172.2991444559567, 0.0), (1.0, 1.0, 1.0), "Suburbs_Gate_A_Pillar_Shaft342", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3806.1475, 358.956, 1502.3932), (0.0, -172.2991444559567, 0.0), (1.0, 1.0, 1.0), "Suburbs_Gate_A_Pillar_Shaft343", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3806.1475, 358.956, 1602.3932), (0.0, -172.2991444559567, 0.0), (1.0, 1.0, 1.0), "Suburbs_Gate_A_Pillar_Shaft344", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3806.1475, 358.956, 1702.3932), (0.0, -172.2991444559567, 0.0), (1.0, 1.0, 1.0), "Suburbs_Gate_A_Pillar_Shaft345", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3806.1475, 358.956, 1802.3932), (0.0, -172.2991444559567, 0.0), (1.0, 1.0, 1.0), "Suburbs_Gate_A_Pillar_Shaft346", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3806.1475, 358.956, 1902.3932), (0.0, -172.2991444559567, 0.0), (1.0, 1.0, 1.0), "Suburbs_Gate_A_Pillar_Shaft347", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3806.1475, 358.956, 2002.3932), (0.0, -172.2991444559567, 0.0), (1.0, 1.0, 1.0), "Suburbs_Gate_A_Pillar_Shaft348", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4301.645, 425.87326, 1102.3932), (0.0, -172.2991444559567, 0.0), (1.0, 1.0, 1.0), "Suburbs_Gate_A_Pillar_Shaft349", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (6091.9746, 2535.9963, 1502.3894), (0.0, -100.16161761252525, 0.0), (1.0, 1.0, 1.0), "Suburbs_Gate_A_Pillar_Shaft35_403", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4301.645, 425.87326, 1202.3932), (0.0, -172.2991444559567, 0.0), (1.0, 1.0, 1.0), "Suburbs_Gate_A_Pillar_Shaft350", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (6091.9746, 2535.9963, 1602.3894), (0.0, -100.16161761252525, 0.0), (1.0, 1.0, 1.0), "Suburbs_Gate_A_Pillar_Shaft36_404", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (6091.9746, 2535.9963, 1702.3894), (0.0, -100.16161761252525, 0.0), (1.0, 1.0, 1.0), "Suburbs_Gate_A_Pillar_Shaft37_405", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (6091.9746, 2535.9963, 1802.3894), (0.0, -100.16161761252525, 0.0), (1.0, 1.0, 1.0), "Suburbs_Gate_A_Pillar_Shaft38_406", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (6091.9746, 2535.9963, 1902.3894), (0.0, -100.16161761252525, 0.0), (1.0, 1.0, 1.0), "Suburbs_Gate_A_Pillar_Shaft39_407", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5794.3555, 4883.705, 1602.3932), (0.0, -61.40539497196487, 0.0), (1.0, 1.0, 1.0), "Suburbs_Gate_A_Pillar_Shaft4", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (6091.9746, 2535.9963, 2002.3894), (0.0, -100.16161761252525, 0.0), (1.0, 1.0, 1.0), "Suburbs_Gate_A_Pillar_Shaft40_408", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (6003.747, 2043.8492, 1302.3894), (0.0, -100.16161761252525, 0.0), (1.0, 1.0, 1.0), "Suburbs_Gate_A_Pillar_Shaft41_410", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (6003.747, 2043.8492, 1402.3894), (0.0, -100.16161761252525, 0.0), (1.0, 1.0, 1.0), "Suburbs_Gate_A_Pillar_Shaft42_412", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (6003.747, 2043.8492, 1502.3894), (0.0, -100.16161761252525, 0.0), (1.0, 1.0, 1.0), "Suburbs_Gate_A_Pillar_Shaft43_413", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (6003.747, 2043.8492, 1602.3894), (0.0, -100.16161761252525, 0.0), (1.0, 1.0, 1.0), "Suburbs_Gate_A_Pillar_Shaft44_414", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (6003.747, 2043.8492, 1702.3894), (0.0, -100.16161761252525, 0.0), (1.0, 1.0, 1.0), "Suburbs_Gate_A_Pillar_Shaft45_415", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (6003.747, 2043.8492, 1802.3894), (0.0, -100.16161761252525, 0.0), (1.0, 1.0, 1.0), "Suburbs_Gate_A_Pillar_Shaft46_416", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (6003.747, 2043.8492, 1902.3894), (0.0, -100.16161761252525, 0.0), (1.0, 1.0, 1.0), "Suburbs_Gate_A_Pillar_Shaft47_417", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (6003.747, 2043.8492, 2002.3894), (0.0, -100.16161761252525, 0.0), (1.0, 1.0, 1.0), "Suburbs_Gate_A_Pillar_Shaft48_418", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5958.4795, 1907.8461, 1302.3894), (0.0, -114.47987896720926, 0.0), (1.0, 1.0, 1.0), "Suburbs_Gate_A_Pillar_Shaft49_468", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5794.3555, 4883.705, 1702.3932), (0.0, -61.40539497196487, 0.0), (1.0, 1.0, 1.0), "Suburbs_Gate_A_Pillar_Shaft5", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5958.4795, 1907.8461, 1402.3894), (0.0, -114.47987896720926, 0.0), (1.0, 1.0, 1.0), "Suburbs_Gate_A_Pillar_Shaft50_470", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5958.4795, 1907.8461, 1502.3894), (0.0, -114.47987896720926, 0.0), (1.0, 1.0, 1.0), "Suburbs_Gate_A_Pillar_Shaft51_471", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5958.4795, 1907.8461, 1602.3894), (0.0, -114.47987896720926, 0.0), (1.0, 1.0, 1.0), "Suburbs_Gate_A_Pillar_Shaft52_472", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5958.4795, 1907.8461, 1702.3894), (0.0, -114.47987896720926, 0.0), (1.0, 1.0, 1.0), "Suburbs_Gate_A_Pillar_Shaft53_473", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5958.4795, 1907.8461, 1802.3894), (0.0, -114.47987896720926, 0.0), (1.0, 1.0, 1.0), "Suburbs_Gate_A_Pillar_Shaft54_474", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5958.4795, 1907.8461, 1902.3894), (0.0, -114.47987896720926, 0.0), (1.0, 1.0, 1.0), "Suburbs_Gate_A_Pillar_Shaft55_475", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5958.4795, 1907.8461, 2002.3894), (0.0, -114.47987896720926, 0.0), (1.0, 1.0, 1.0), "Suburbs_Gate_A_Pillar_Shaft56_476", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5751.2637, 1452.8163, 1302.3894), (0.0, -114.47987896720926, 0.0), (1.0, 1.0, 1.0), "Suburbs_Gate_A_Pillar_Shaft57_478", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5751.2637, 1452.8163, 1402.3894), (0.0, -114.47987896720926, 0.0), (1.0, 1.0, 1.0), "Suburbs_Gate_A_Pillar_Shaft58_480", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5751.2637, 1452.8163, 1502.3894), (0.0, -114.47987896720926, 0.0), (1.0, 1.0, 1.0), "Suburbs_Gate_A_Pillar_Shaft59_481", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5794.3555, 4883.705, 1802.3932), (0.0, -61.40539497196487, 0.0), (1.0, 1.0, 1.0), "Suburbs_Gate_A_Pillar_Shaft6", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5751.2637, 1452.8163, 1602.3894), (0.0, -114.47987896720926, 0.0), (1.0, 1.0, 1.0), "Suburbs_Gate_A_Pillar_Shaft60_482", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5751.2637, 1452.8163, 1702.3894), (0.0, -114.47987896720926, 0.0), (1.0, 1.0, 1.0), "Suburbs_Gate_A_Pillar_Shaft61_483", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5751.2637, 1452.8163, 1802.3894), (0.0, -114.47987896720926, 0.0), (1.0, 1.0, 1.0), "Suburbs_Gate_A_Pillar_Shaft62_484", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5751.2637, 1452.8163, 1902.3894), (0.0, -114.47987896720926, 0.0), (1.0, 1.0, 1.0), "Suburbs_Gate_A_Pillar_Shaft63_485", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5751.2637, 1452.8163, 2002.3894), (0.0, -114.47987896720926, 0.0), (1.0, 1.0, 1.0), "Suburbs_Gate_A_Pillar_Shaft64_486", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5794.3555, 4883.705, 1902.3932), (0.0, -61.40539497196487, 0.0), (1.0, 1.0, 1.0), "Suburbs_Gate_A_Pillar_Shaft7", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5794.3555, 4883.705, 2002.3932), (0.0, -61.40539497196487, 0.0), (1.0, 1.0, 1.0), "Suburbs_Gate_A_Pillar_Shaft8", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (6033.649, 4444.6846, 1302.3932), (0.0, -61.40539497196487, 0.0), (1.0, 1.0, 1.0), "Suburbs_Gate_A_Pillar_Shaft9", _folder)
if a: placed += 1
else: skipped += 1

# Batch 47: StaticMesh'Suburbs_Gate_C_Arch' (28 instances)
_mesh_path = "/Game/Art/Assets/Kits/Architecture/Suburbs/Suburbs_Gate_C_Arch"
_materials = ['/Game/Art/Assets/Kits/Architecture/Suburbs/Materials/Suburbs_Trim_Sheet_A/MI_Suburbs_Trim_Sheet_Gray', '/Game/Art/Assets/Kits/Architecture/Suburbs/Materials/Suburbs_Trim_Sheet_A/MI_Suburbs_Trim_Sheet_Gray']
_folder = "Reconstruction/BD_BB_Chapter2_Orctown_Throne/Meshes"
a = spawn_static_mesh(_mesh_path, _materials, (6026.6597, 4359.543, 2202.394), (0.0, 118.59409742997603, -0.0), (1.0, 1.0, 1.0), "Suburbs_Gate_C_Arch_1235", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4889.1235, 5711.8936, 2202.394), (0.0, 156.68211269021506, -0.0), (1.0, 1.0, 1.0), "Suburbs_Gate_C_Arch15", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4292.209, 5969.197, 2202.394), (0.0, -23.316101013813984, 0.0), (1.0, 1.0, 1.0), "Suburbs_Gate_C_Arch16", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5715.5684, 4930.2686, 2202.394), (0.0, -61.40478299543522, 0.0), (1.0, 1.0, 1.0), "Suburbs_Gate_C_Arch2", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4304.4385, 5968.282, 2202.394), (0.0, 178.5940384579303, -0.0), (1.0, 1.0, 1.0), "Suburbs_Gate_C_Arch21", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3654.6333, 5984.2314, 2202.394), (0.0, -1.4047240305411686, 0.0), (1.0, 1.0, 1.0), "Suburbs_Gate_C_Arch22", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2380.1902, 6019.9634, 2202.394), (0.0, -163.3691491665155, 0.0), (1.0, 1.0, 1.0), "Suburbs_Gate_C_Arch23", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1757.3665, 5833.959, 2202.394), (0.0, 16.62987184662422, -0.0), (1.0, 1.0, 1.0), "Suburbs_Gate_C_Arch24", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1771.8784, 5834.0815, 2202.394), (0.0, -148.64702799513125, 0.0), (1.0, 1.0, 1.0), "Suburbs_Gate_C_Arch25", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1216.7921, 5495.888, 2202.394), (0.0, 31.351468796560944, -0.0), (1.0, 1.0, 1.0), "Suburbs_Gate_C_Arch26", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1226.5126, 5505.4478, 2202.394), (0.0, -131.70802842984082, 0.0), (1.0, 1.0, 1.0), "Suburbs_Gate_C_Arch27", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (794.0359, 5020.211, 2202.394), (0.0, 48.290103183389434, -0.0), (1.0, 1.0, 1.0), "Suburbs_Gate_C_Arch28", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (685.65247, 1499.9751, 2202.394), (0.0, -54.77127035175581, 0.0), (1.0, 1.0, 1.0), "Suburbs_Gate_C_Arch29", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (6160.9, 3744.7144, 2202.3936), (0.0, 101.13287735158576, -0.0), (1.0, 1.0, 1.0), "Suburbs_Gate_C_Arch3", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1060.5786, 969.01447, 2202.394), (0.0, 125.22691950525218, -0.0), (1.0, 1.0, 1.0), "Suburbs_Gate_C_Arch30", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1049.6279, 975.4602, 2202.394), (0.0, -33.653806706353514, 0.0), (1.0, 1.0, 1.0), "Suburbs_Gate_C_Arch31", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1590.6696, 615.2349, 2202.394), (0.0, 146.34404438293777, -0.0), (1.0, 1.0, 1.0), "Suburbs_Gate_C_Arch32", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1873.8802, 508.95737, 2202.394), (0.0, -10.358398648349283, 0.0), (1.0, 1.0, 1.0), "Suburbs_Gate_C_Arch33", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2513.269, 392.02713, 2202.394), (0.0, 169.63898289042118, -0.0), (1.0, 1.0, 1.0), "Suburbs_Gate_C_Arch34", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4360.273, 472.32343, 2202.394), (0.0, 19.311049507169603, -0.0), (1.0, 1.0, 1.0), "Suburbs_Gate_C_Arch35", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4973.716, 687.2223, 2202.394), (0.0, -160.69131861492966, 0.0), (1.0, 1.0, 1.0), "Suburbs_Gate_C_Arch36", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3729.1045, 395.8545, 2202.394), (0.0, 7.7001625196437065, -0.0), (1.0, 1.0, 1.0), "Suburbs_Gate_C_Arch37", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4373.246, 482.88416, 2202.394), (0.0, -172.30169088282594, 0.0), (1.0, 1.0, 1.0), "Suburbs_Gate_C_Arch38", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (6035.418, 4382.4844, 2202.3936), (0.0, -78.86644883303175, 0.0), (1.0, 1.0, 1.0), "Suburbs_Gate_C_Arch4", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5945.0, 1981.8314, 2202.3936), (0.0, 79.83670038482639, -0.0), (1.0, 1.0, 1.0), "Suburbs_Gate_C_Arch5_397", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (6059.6787, 2621.6282, 2202.3936), (0.0, -100.16174287111791, 0.0), (1.0, 1.0, 1.0), "Suburbs_Gate_C_Arch6_398", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5679.0, 1407.2579, 2202.3936), (0.0, 65.51742444535566, -0.0), (1.0, 1.0, 1.0), "Suburbs_Gate_C_Arch7_465", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5948.3706, 1998.8059, 2202.3936), (0.0, -114.48016443274643, 0.0), (1.0, 1.0, 1.0), "Suburbs_Gate_C_Arch8_466", _folder)
if a: placed += 1
else: skipped += 1

# Batch 48: StaticMesh'Suburbs_Gate_Pillar_B' (71 instances)
_mesh_path = "/Game/Art/Assets/Kits/Architecture/Suburbs/Suburbs_Gate_Pillar_B"
_materials = ['/Game/Art/Assets/Kits/Architecture/Suburbs/Materials/Suburbs_Trim_Sheet_A/MI_Suburbs_Trim_Sheet_Gray', '/Game/Art/Assets/Kits/Architecture/Suburbs/Materials/Suburbs_Trim_Sheet_A/MI_Suburbs_Trim_Sheet_Gray']
_folder = "Reconstruction/BD_BB_Chapter2_Orctown_Throne/Meshes"
a = spawn_static_mesh(_mesh_path, _materials, (5767.8555, 4897.949, 1742.3937), (0.0, -61.405275182410016, 0.0), (1.0, 1.0, 1.0), "Suburbs_Gate_Pillar_B_1273", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (6181.7715, 3796.314, 1742.3899), (0.0, 101.13241892274971, -0.0), (1.0, 1.0, 1.0), "Suburbs_Gate_Pillar_B10", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1914.2375, 470.63324, 1742.3937), (0.0, -10.356658222499002, 0.0), (1.0, 1.0, 1.0), "Suburbs_Gate_Pillar_B100", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1914.2375, 470.63324, 1142.3937), (0.0, -10.356658222499002, 0.0), (1.0, 1.0, 1.0), "Suburbs_Gate_Pillar_B101", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4933.3823, 640.8276, 1742.3937), (0.0, -160.69014777382228, 0.0), (1.0, 1.0, 1.0), "Suburbs_Gate_Pillar_B103", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4933.3823, 640.8276, 1142.3937), (0.0, -160.69014777382228, 0.0), (1.0, 1.0, 1.0), "Suburbs_Gate_Pillar_B104", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4933.3823, 640.8276, 542.3937), (0.0, -160.69014777382228, 0.0), (1.0, 1.0, 1.0), "Suburbs_Gate_Pillar_B105", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4414.3105, 458.9998, 1742.3937), (0.0, 19.31284399139739, -0.0), (1.0, 1.0, 1.0), "Suburbs_Gate_Pillar_B106", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4414.3105, 458.9998, 1142.3937), (0.0, 19.31284399139739, -0.0), (1.0, 1.0, 1.0), "Suburbs_Gate_Pillar_B107", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4414.3105, 458.9998, 542.3937), (0.0, 19.31284399139739, -0.0), (1.0, 1.0, 1.0), "Suburbs_Gate_Pillar_B108", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4324.4033, 445.5566, 1742.3937), (0.0, -172.3006550541581, 0.0), (1.0, 1.0, 1.0), "Suburbs_Gate_Pillar_B109", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (6181.7715, 3796.314, 1142.3899), (0.0, 101.13241892274971, -0.0), (1.0, 1.0, 1.0), "Suburbs_Gate_Pillar_B11", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4324.4033, 445.5566, 1142.3937), (0.0, -172.3006550541581, 0.0), (1.0, 1.0, 1.0), "Suburbs_Gate_Pillar_B110", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4324.4033, 445.5566, 542.3937), (0.0, -172.3006550541581, 0.0), (1.0, 1.0, 1.0), "Suburbs_Gate_Pillar_B111", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3779.354, 371.9269, 1742.3937), (0.0, 7.7019268860128065, -0.0), (1.0, 1.0, 1.0), "Suburbs_Gate_Pillar_B112", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3779.354, 371.9269, 1142.3937), (0.0, 7.7019268860128065, -0.0), (1.0, 1.0, 1.0), "Suburbs_Gate_Pillar_B113", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (6181.7715, 3796.314, 542.3899), (0.0, 101.13241892274971, -0.0), (1.0, 1.0, 1.0), "Suburbs_Gate_Pillar_B12", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (6080.221, 2563.691, 1742.3899), (0.0, -100.16201895100896, 0.0), (1.0, 1.0, 1.0), "Suburbs_Gate_Pillar_B13_423", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (6080.221, 2563.691, 1142.3899), (0.0, -100.16201895100896, 0.0), (1.0, 1.0, 1.0), "Suburbs_Gate_Pillar_B14_424", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5983.1836, 2022.3304, 1742.3899), (0.0, 79.83605275556268, -0.0), (1.0, 1.0, 1.0), "Suburbs_Gate_Pillar_B16_426", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5983.1836, 2022.3304, 1142.3899), (0.0, 79.83605275556268, -0.0), (1.0, 1.0, 1.0), "Suburbs_Gate_Pillar_B17_427", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5953.943, 1937.588, 1742.3899), (0.0, -114.48032872551393, 0.0), (1.0, 1.0, 1.0), "Suburbs_Gate_Pillar_B19_491", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5767.8555, 4897.949, 1142.3937), (0.0, -61.405275182410016, 0.0), (1.0, 1.0, 1.0), "Suburbs_Gate_Pillar_B2", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5953.943, 1937.588, 1142.3899), (0.0, -114.48032872551393, 0.0), (1.0, 1.0, 1.0), "Suburbs_Gate_Pillar_B20_492", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5953.943, 1937.588, 542.3899), (0.0, -114.48032872551393, 0.0), (1.0, 1.0, 1.0), "Suburbs_Gate_Pillar_B21_493", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5726.016, 1437.0532, 1742.3899), (0.0, 65.51687114320963, -0.0), (1.0, 1.0, 1.0), "Suburbs_Gate_Pillar_B22_494", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5726.016, 1437.0532, 1142.3899), (0.0, 65.51687114320963, -0.0), (1.0, 1.0, 1.0), "Suburbs_Gate_Pillar_B23_495", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5726.016, 1437.0532, 542.3899), (0.0, 65.51687114320963, -0.0), (1.0, 1.0, 1.0), "Suburbs_Gate_Pillar_B24_496", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5767.8555, 4897.949, 542.3937), (0.0, -61.405275182410016, 0.0), (1.0, 1.0, 1.0), "Suburbs_Gate_Pillar_B3", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (6031.081, 4415.0264, 1742.3937), (0.0, 118.5939690270411, -0.0), (1.0, 1.0, 1.0), "Suburbs_Gate_Pillar_B4", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4353.299, 5976.007, 1742.3937), (0.0, -23.317077280848256, 0.0), (1.0, 1.0, 1.0), "Suburbs_Gate_Pillar_B43", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4353.299, 5976.007, 1142.3937), (0.0, -23.317077280848256, 0.0), (1.0, 1.0, 1.0), "Suburbs_Gate_Pillar_B44", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4353.299, 5976.007, 542.3937), (0.0, -23.317077280848256, 0.0), (1.0, 1.0, 1.0), "Suburbs_Gate_Pillar_B45", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4858.3774, 5758.2983, 1742.3937), (0.0, 156.6811777273936, -0.0), (1.0, 1.0, 1.0), "Suburbs_Gate_Pillar_B46", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4858.3774, 5758.2983, 1142.3937), (0.0, 156.6811777273936, -0.0), (1.0, 1.0, 1.0), "Suburbs_Gate_Pillar_B47", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4858.3774, 5758.2983, 542.3937), (0.0, 156.6811777273936, -0.0), (1.0, 1.0, 1.0), "Suburbs_Gate_Pillar_B48", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (6031.081, 4415.0264, 1142.3937), (0.0, 118.5939690270411, -0.0), (1.0, 1.0, 1.0), "Suburbs_Gate_Pillar_B5", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (6031.081, 4415.0264, 542.3937), (0.0, 118.5939690270411, -0.0), (1.0, 1.0, 1.0), "Suburbs_Gate_Pillar_B6", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3708.7664, 6013.3545, 1742.3937), (0.0, -1.4052124152556669, 0.0), (1.0, 1.0, 1.0), "Suburbs_Gate_Pillar_B61", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3708.7664, 6013.3545, 1142.3937), (0.0, -1.4052124152556669, 0.0), (1.0, 1.0, 1.0), "Suburbs_Gate_Pillar_B62", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4258.599, 5999.853, 1742.3937), (0.0, 178.59401096942793, -0.0), (1.0, 1.0, 1.0), "Suburbs_Gate_Pillar_B64", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4258.599, 5999.853, 1142.3937), (0.0, 178.59401096942793, -0.0), (1.0, 1.0, 1.0), "Suburbs_Gate_Pillar_B65", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1799.8201, 5878.419, 1742.3937), (0.0, 16.63213619132662, -0.0), (1.0, 1.0, 1.0), "Suburbs_Gate_Pillar_B67", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1799.8201, 5878.419, 1142.3937), (0.0, 16.63213619132662, -0.0), (1.0, 1.0, 1.0), "Suburbs_Gate_Pillar_B68", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (6075.5986, 4335.963, 1742.3899), (0.0, -78.86667199229265, 0.0), (1.0, 1.0, 1.0), "Suburbs_Gate_Pillar_B7", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2326.8293, 6035.784, 1742.3937), (0.0, -163.36759557302807, 0.0), (1.0, 1.0, 1.0), "Suburbs_Gate_Pillar_B70", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2326.8293, 6035.784, 1142.3937), (0.0, -163.36759557302807, 0.0), (1.0, 1.0, 1.0), "Suburbs_Gate_Pillar_B71", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1246.5559, 5549.6772, 1742.3937), (0.0, 31.352300985226105, -0.0), (1.0, 1.0, 1.0), "Suburbs_Gate_Pillar_B73", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1246.5559, 5549.6772, 1142.3937), (0.0, 31.352300985226105, -0.0), (1.0, 1.0, 1.0), "Suburbs_Gate_Pillar_B74", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1716.2495, 5835.823, 1742.3937), (0.0, -148.64557177721588, 0.0), (1.0, 1.0, 1.0), "Suburbs_Gate_Pillar_B76", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1716.2495, 5835.823, 1142.3937), (0.0, -148.64557177721588, 0.0), (1.0, 1.0, 1.0), "Suburbs_Gate_Pillar_B77", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (806.83765, 5080.338, 1742.3937), (0.0, 48.290887951745844, -0.0), (1.0, 1.0, 1.0), "Suburbs_Gate_Pillar_B79", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (6075.5986, 4335.963, 1142.3899), (0.0, -78.86667199229265, 0.0), (1.0, 1.0, 1.0), "Suburbs_Gate_Pillar_B8", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (806.83765, 5080.338, 1142.3937), (0.0, 48.290887951745844, -0.0), (1.0, 1.0, 1.0), "Suburbs_Gate_Pillar_B80", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (806.83765, 5080.338, 542.3937), (0.0, 48.290887951745844, -0.0), (1.0, 1.0, 1.0), "Suburbs_Gate_Pillar_B81", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1172.7885, 5490.9146, 1742.3937), (0.0, -131.70650863972023, 0.0), (1.0, 1.0, 1.0), "Suburbs_Gate_Pillar_B82", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1172.7885, 5490.9146, 1142.3937), (0.0, -131.70650863972023, 0.0), (1.0, 1.0, 1.0), "Suburbs_Gate_Pillar_B83", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1172.7885, 5490.9146, 542.3937), (0.0, -131.70650863972023, 0.0), (1.0, 1.0, 1.0), "Suburbs_Gate_Pillar_B84", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1004.9011, 995.07623, 1742.3937), (0.0, 125.22770444998453, -0.0), (1.0, 1.0, 1.0), "Suburbs_Gate_Pillar_B85", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1004.9011, 995.07623, 1142.3937), (0.0, 125.22770444998453, -0.0), (1.0, 1.0, 1.0), "Suburbs_Gate_Pillar_B86", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1004.9011, 995.07623, 542.3937), (0.0, 125.22770444998453, -0.0), (1.0, 1.0, 1.0), "Suburbs_Gate_Pillar_B87", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (687.66736, 1444.3558, 1742.3937), (0.0, -54.769623925631805, 0.0), (1.0, 1.0, 1.0), "Suburbs_Gate_Pillar_B88", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (687.66736, 1444.3558, 1142.3937), (0.0, -54.769623925631805, 0.0), (1.0, 1.0, 1.0), "Suburbs_Gate_Pillar_B89", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (6075.5986, 4335.963, 542.3899), (0.0, -78.86667199229265, 0.0), (1.0, 1.0, 1.0), "Suburbs_Gate_Pillar_B9", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (687.66736, 1444.3558, 542.3937), (0.0, -54.769623925631805, 0.0), (1.0, 1.0, 1.0), "Suburbs_Gate_Pillar_B90", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1529.3414, 619.4867, 1742.3937), (0.0, 146.3449431494951, -0.0), (1.0, 1.0, 1.0), "Suburbs_Gate_Pillar_B91", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1529.3414, 619.4867, 1142.3937), (0.0, 146.3449431494951, -0.0), (1.0, 1.0, 1.0), "Suburbs_Gate_Pillar_B92", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1071.5463, 924.30115, 1742.3937), (0.0, -33.652036464377495, 0.0), (1.0, 1.0, 1.0), "Suburbs_Gate_Pillar_B94", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1071.5463, 924.30115, 1142.3937), (0.0, -33.652036464377495, 0.0), (1.0, 1.0, 1.0), "Suburbs_Gate_Pillar_B95", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2455.2598, 371.68265, 1742.3937), (0.0, 169.64004113436775, -0.0), (1.0, 1.0, 1.0), "Suburbs_Gate_Pillar_B97", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2455.2598, 371.68265, 1142.3937), (0.0, 169.64004113436775, -0.0), (1.0, 1.0, 1.0), "Suburbs_Gate_Pillar_B98", _folder)
if a: placed += 1
else: skipped += 1

# Batch 49: StaticMesh'Suburbs_Stairs_Medium_C_NonDest' (2 instances)
_mesh_path = "/Game/Art/Assets/Kits/Architecture/Suburbs/Suburbs_Stairs_Medium_C_NonDest"
_materials = ['/Game/Art/Assets/Kits/Architecture/Suburbs/Materials/Stairs_Medium_C_NonDest/MI_Stairs_Medium_C_NonDes_Gray', '/Game/Environments/Materials/MI_ArchitectureBase_NonDestructible']
_folder = "Reconstruction/BD_BB_Chapter2_Orctown_Throne/Meshes"
a = spawn_static_mesh(_mesh_path, _materials, (5374.0166, 2133.2869, 800.0), (0.0, 154.06246180342524, -0.0), (1.0, 1.0, 1.0), "BP_Suburbs_Stairs_Large_A1_Breakable23_71", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5385.2173, 4274.545, 800.0), (0.0, 25.312346803534467, -0.0), (1.0, 1.0, 1.0), "BP_Suburbs_Stairs_Large_A1_Breakable61", _folder)
if a: placed += 1
else: skipped += 1

# Batch 50: StaticMesh'Suburbs_Stairs_Medium_C_NonDest' (53 instances)
_mesh_path = "/Game/Art/Assets/Kits/Architecture/Suburbs/Suburbs_Stairs_Medium_C_NonDest"
_materials = ['/Game/Art/Assets/Kits/Architecture/Suburbs/Materials/Stairs_Medium_C_NonDest/MI_Stairs_Medium_C_NonDes_Gray', '/Game/Art/Assets/Kits/Architecture/Suburbs/Destructable/Materials/MI_Suburbs_Wall_Non_Dest']
_folder = "Reconstruction/BD_BB_Chapter2_Orctown_Throne/Meshes"
a = spawn_static_mesh(_mesh_path, _materials, (3751.3962, 5609.5127, 1200.0), (0.0, -112.49999787930444, 0.0), (1.0, 1.0, 1.0), "BP_Suburbs_Stairs_Large_A1_Breakable13", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3866.202, 5886.676, 1200.0), (0.0, -112.49999787930444, 0.0), (1.0, 1.0, 1.0), "BP_Suburbs_Stairs_Large_A1_Breakable14_52", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3981.0076, 6163.839, 1200.0), (0.0, -112.49999787930444, 0.0), (1.0, 1.0, 1.0), "BP_Suburbs_Stairs_Large_A1_Breakable15", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5636.452, 2672.8503, 1200.0), (0.0, 154.06246180342524, -0.0), (1.0, 1.0, 1.0), "BP_Suburbs_Stairs_Large_A1_Breakable19", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5906.2324, 2541.6326, 1200.0), (0.0, 154.06246180342524, -0.0), (1.0, 1.0, 1.0), "BP_Suburbs_Stairs_Large_A1_Breakable20_75", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5505.2344, 2403.0686, 1000.0), (0.0, 154.06246180342524, -0.0), (1.0, 1.0, 1.0), "BP_Suburbs_Stairs_Large_A1_Breakable21_69", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5641.747, 3732.1504, 1200.0), (0.0, 25.312346803534467, -0.0), (1.0, 1.0, 1.0), "BP_Suburbs_Stairs_Large_A1_Breakable22", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5912.9453, 3860.4165, 1200.0), (0.0, 25.312346803534467, -0.0), (1.0, 1.0, 1.0), "BP_Suburbs_Stairs_Large_A1_Breakable24_58", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (6184.143, 3988.6826, 1200.0), (0.0, 25.312346803534467, -0.0), (1.0, 1.0, 1.0), "BP_Suburbs_Stairs_Large_A1_Breakable25_60", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5775.0146, 2271.8508, 1000.0), (0.0, 154.06246180342524, -0.0), (1.0, 1.0, 1.0), "BP_Suburbs_Stairs_Large_A1_Breakable26_76", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1653.7621, 5000.9336, 1000.0), (0.0, 129.37447933253276, -0.0), (1.0, 1.0, 1.0), "BP_Suburbs_Stairs_Large_A1_Breakable27_25", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1463.4459, 5232.839, 1000.0), (0.0, 129.37447933253276, -0.0), (1.0, 1.0, 1.0), "BP_Suburbs_Stairs_Large_A1_Breakable28_29", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1273.1298, 5464.744, 1000.0), (0.0, 129.37447933253276, -0.0), (1.0, 1.0, 1.0), "BP_Suburbs_Stairs_Large_A1_Breakable29_32", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1383.2114, 4778.899, 900.0), (0.0, 129.37462918037983, -0.0), (1.0, 1.0, 1.0), "BP_Suburbs_Stairs_Large_A1_Breakable3_4", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1151.3069, 4588.5835, 700.0), (0.0, 129.37462918037983, -0.0), (1.0, 1.0, 1.0), "BP_Suburbs_Stairs_Large_A1_Breakable30_35", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (960.9905, 4820.489, 700.0), (0.0, 129.37462918037983, -0.0), (1.0, 1.0, 1.0), "BP_Suburbs_Stairs_Large_A1_Breakable31_39", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1792.6509, 1143.8137, 1200.0), (0.0, 39.37487715894419, -0.0), (1.0, 1.0, 1.0), "BP_Suburbs_Stairs_Large_A1_Breakable32", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (770.67395, 5052.394, 700.0), (0.0, 129.37462918037983, -0.0), (1.0, 1.0, 1.0), "BP_Suburbs_Stairs_Large_A1_Breakable33_43", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3677.8586, 763.5108, 1200.0), (0.0, -70.3124375972685, 0.0), (1.0, 1.0, 1.0), "BP_Suburbs_Stairs_Large_A1_Breakable34", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4028.5608, 5494.707, 1000.0), (0.0, -112.49999787930444, 0.0), (1.0, 1.0, 1.0), "BP_Suburbs_Stairs_Large_A1_Breakable35_46", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3778.9255, 481.04758, 1200.0), (0.0, -70.3124375972685, 0.0), (1.0, 1.0, 1.0), "BP_Suburbs_Stairs_Large_A1_Breakable36_14", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4305.7227, 5379.9014, 800.0), (0.0, -112.49999787930444, 0.0), (1.0, 1.0, 1.0), "BP_Suburbs_Stairs_Large_A1_Breakable38_48", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1602.3333, 1375.7175, 1000.0), (0.0, 39.37487715894419, -0.0), (1.0, 1.0, 1.0), "BP_Suburbs_Stairs_Large_A1_Breakable39", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1885.6666, 5191.249, 1200.0), (0.0, 129.37447933253276, -0.0), (1.0, 1.0, 1.0), "BP_Suburbs_Stairs_Large_A1_Breakable4_5", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1412.0156, 1607.6213, 800.0), (0.0, 39.37487715894419, -0.0), (1.0, 1.0, 1.0), "BP_Suburbs_Stairs_Large_A1_Breakable40", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1560.7472, 953.4963, 1200.0), (0.0, 39.37487715894419, -0.0), (1.0, 1.0, 1.0), "BP_Suburbs_Stairs_Large_A1_Breakable41", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1370.4296, 1185.3999, 1000.0), (0.0, 39.37487715894419, -0.0), (1.0, 1.0, 1.0), "BP_Suburbs_Stairs_Large_A1_Breakable42", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1180.1119, 1417.3037, 800.0), (0.0, 39.37487715894419, -0.0), (1.0, 1.0, 1.0), "BP_Suburbs_Stairs_Large_A1_Breakable43", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1328.8434, 763.17865, 1200.0), (0.0, 39.37487715894419, -0.0), (1.0, 1.0, 1.0), "BP_Suburbs_Stairs_Large_A1_Breakable44", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1138.5258, 995.08246, 1000.0), (0.0, 39.37487715894419, -0.0), (1.0, 1.0, 1.0), "BP_Suburbs_Stairs_Large_A1_Breakable45", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (948.2083, 1226.9861, 800.0), (0.0, 39.37487715894419, -0.0), (1.0, 1.0, 1.0), "BP_Suburbs_Stairs_Large_A1_Breakable46", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3960.3215, 864.57806, 1000.0), (0.0, -70.3124375972685, 0.0), (1.0, 1.0, 1.0), "BP_Suburbs_Stairs_Large_A1_Breakable47", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4061.3887, 582.11487, 1000.0), (0.0, -70.3124375972685, 0.0), (1.0, 1.0, 1.0), "BP_Suburbs_Stairs_Large_A1_Breakable48", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4242.7847, 965.6453, 800.0), (0.0, -70.3124375972685, 0.0), (1.0, 1.0, 1.0), "BP_Suburbs_Stairs_Large_A1_Breakable49", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1192.8953, 5010.804, 900.0), (0.0, 129.37462918037983, -0.0), (1.0, 1.0, 1.0), "BP_Suburbs_Stairs_Large_A1_Breakable5_38", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4343.8516, 683.1821, 800.0), (0.0, -70.3124375972685, 0.0), (1.0, 1.0, 1.0), "BP_Suburbs_Stairs_Large_A1_Breakable50", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4444.92, 400.71896, 800.0), (0.0, -70.3124375972685, 0.0), (1.0, 1.0, 1.0), "BP_Suburbs_Stairs_Large_A1_Breakable52", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4143.3647, 5771.87, 1000.0), (0.0, -112.49999787930444, 0.0), (1.0, 1.0, 1.0), "BP_Suburbs_Stairs_Large_A1_Breakable53", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4420.5283, 5657.0645, 800.0), (0.0, -112.49999787930444, 0.0), (1.0, 1.0, 1.0), "BP_Suburbs_Stairs_Large_A1_Breakable54", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4258.1704, 6049.033, 1000.0), (0.0, -112.49999787930444, 0.0), (1.0, 1.0, 1.0), "BP_Suburbs_Stairs_Large_A1_Breakable56", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4535.334, 5934.2275, 800.0), (0.0, -112.49999787930444, 0.0), (1.0, 1.0, 1.0), "BP_Suburbs_Stairs_Large_A1_Breakable57", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5513.482, 4003.3474, 1000.0), (0.0, 25.312346803534467, -0.0), (1.0, 1.0, 1.0), "BP_Suburbs_Stairs_Large_A1_Breakable58", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5784.68, 4131.614, 1000.0), (0.0, 25.312346803534467, -0.0), (1.0, 1.0, 1.0), "BP_Suburbs_Stairs_Large_A1_Breakable59", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1695.3505, 5423.1543, 1200.0), (0.0, 129.37447933253276, -0.0), (1.0, 1.0, 1.0), "BP_Suburbs_Stairs_Large_A1_Breakable6_28", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (6055.878, 4259.8804, 1000.0), (0.0, 25.312346803534467, -0.0), (1.0, 1.0, 1.0), "BP_Suburbs_Stairs_Large_A1_Breakable60", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5656.4155, 4402.812, 800.0), (0.0, 25.312346803534467, -0.0), (1.0, 1.0, 1.0), "BP_Suburbs_Stairs_Large_A1_Breakable62", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5927.6133, 4531.0786, 800.0), (0.0, 25.312346803534467, -0.0), (1.0, 1.0, 1.0), "BP_Suburbs_Stairs_Large_A1_Breakable63", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5643.797, 2002.0701, 800.0), (0.0, 154.06246180342524, -0.0), (1.0, 1.0, 1.0), "BP_Suburbs_Stairs_Large_A1_Breakable64", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (6176.0127, 2410.4148, 1200.0), (0.0, 154.06246180342524, -0.0), (1.0, 1.0, 1.0), "BP_Suburbs_Stairs_Large_A1_Breakable65", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (6044.795, 2140.633, 1000.0), (0.0, 154.06246180342524, -0.0), (1.0, 1.0, 1.0), "BP_Suburbs_Stairs_Large_A1_Breakable66", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5913.577, 1870.853, 800.0), (0.0, 154.06246180342524, -0.0), (1.0, 1.0, 1.0), "BP_Suburbs_Stairs_Large_A1_Breakable67", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1505.0343, 5655.0596, 1200.0), (0.0, 129.37447933253276, -0.0), (1.0, 1.0, 1.0), "BP_Suburbs_Stairs_Large_A1_Breakable7", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1002.579, 5242.7095, 900.0), (0.0, 129.37462918037983, -0.0), (1.0, 1.0, 1.0), "BP_Suburbs_Stairs_Large_A1_Breakable8_42", _folder)
if a: placed += 1
else: skipped += 1

# Batch 51: StaticMesh'Suburbs_Stairs_Small_C_CornerExt_NonDest' (2 instances)
_mesh_path = "/Game/Art/Assets/Kits/Architecture/Suburbs/Suburbs_Stairs_Small_C_CornerExt_NonDest"
_materials = ['/Game/Art/Assets/Kits/Architecture/Suburbs/Destructable/Materials/MI_Suburbs_Wall_Non_Dest', '/Game/Art/Assets/Kits/Architecture/Suburbs/Materials/Stairs_Medium_C_NonDest/MI_Stairs_Medium_C_NonDes']
_folder = "Reconstruction/BD_BB_Chapter2_Orctown_Throne/Meshes"
a = spawn_static_mesh(_mesh_path, _materials, (6026.821, 2755.1118, 1400.0), (0.0, 87.18778577080539, -0.0), (1.0, 1.0, 1.0), "BP_Suburbs_Stairs_CornerExt_01_Breakable_2", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (6070.9785, 3654.0112, 1400.0), (0.0, -2.812408360877314, 0.0), (1.0, 1.0, 1.0), "BP_Suburbs_Stairs_CornerExt_01_Breakable2", _folder)
if a: placed += 1
else: skipped += 1

# Batch 52: StaticMesh'Suburbs_Stairs_Small_C_NonDest' (3 instances)
_mesh_path = "/Game/Art/Assets/Kits/Architecture/Suburbs/Suburbs_Stairs_Small_C_NonDest"
_materials = ['/Game/Art/Assets/Kits/Architecture/Suburbs/Destructable/Materials/MI_Suburbs_Wall_Non_Dest', '/Game/Art/Assets/Kits/Architecture/Suburbs/Materials/Stairs_Medium_C_NonDest/MI_Stairs_Medium_C_NonDes']
_folder = "Reconstruction/BD_BB_Chapter2_Orctown_Throne/Meshes"
a = spawn_static_mesh(_mesh_path, _materials, (6034.18, 2904.9204, 1400.0), (0.0, 87.18778577080539, -0.0), (1.0, 1.0, 1.0), "BP_Suburbs_Stairs_Small_C1_Breakable_2", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (6063.6187, 3504.1982, 1400.0), (0.0, 87.18778577080539, -0.0), (1.0, 1.0, 1.0), "BP_Suburbs_Stairs_Small_C1_Breakable2_5", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (6048.8994, 3204.5588, 1400.0), (0.0, 87.18778577080539, -0.0), (1.0, 1.0, 1.0), "BP_Suburbs_Stairs_Small_C1_Breakable3", _folder)
if a: placed += 1
else: skipped += 1

# Batch 53: StaticMesh'Suburbs_Wall_Thick_3x1m_A' (12 instances)
_mesh_path = "/Game/Art/Assets/Kits/Architecture/Suburbs/Suburbs_Wall_Thick_3x1m_A"
_materials = ['/Game/Art/Assets/Kits/Architecture/Suburbs/Destructable/Materials/MI_Suburbs_Wall_Non_Dest']
_folder = "Reconstruction/BD_BB_Chapter2_Orctown_Throne/Meshes"
a = spawn_static_mesh(_mesh_path, _materials, (5949.02, 3209.4653, 2300.0), (0.0, 177.18761226169238, -0.0), (1.0, 1.0, 1.0), "BP_Suburbs_Wall_Thick_3x1m_A_2", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5953.9263, 3309.3447, 2300.0), (0.0, -92.81236999532442, 0.0), (1.0, 1.0, 1.0), "BP_Suburbs_Wall_Thick_3x1m_A10", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (6058.7124, 3404.3123, 2300.0), (0.0, -92.81236999532442, 0.0), (1.0, 1.0, 1.0), "BP_Suburbs_Wall_Thick_3x1m_A12", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (6053.806, 3304.4382, 2300.0), (0.0, -92.81236999532442, 0.0), (1.0, 1.0, 1.0), "BP_Suburbs_Wall_Thick_3x1m_A23", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (6089.0264, 3002.352, 1500.0), (0.0, 177.18761226169238, -0.0), (1.0, 1.0, 1.0), "BP_Suburbs_Wall_Thick_3x1m_A26_3", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (6108.6523, 3401.862, 1500.0), (0.0, 177.18761226169238, -0.0), (1.0, 1.0, 1.0), "BP_Suburbs_Wall_Thick_3x1m_A27", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5944.1133, 3109.5857, 2300.0), (0.0, -92.81236999532442, 0.0), (1.0, 1.0, 1.0), "BP_Suburbs_Wall_Thick_3x1m_A3", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5939.207, 3009.7065, 2300.0), (0.0, -92.81236999532442, 0.0), (1.0, 1.0, 1.0), "BP_Suburbs_Wall_Thick_3x1m_A4", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (6048.8994, 3204.5588, 2300.0), (0.0, -92.81236999532442, 0.0), (1.0, 1.0, 1.0), "BP_Suburbs_Wall_Thick_3x1m_A5", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (6043.9927, 3104.6792, 2300.0), (0.0, -92.81236999532442, 0.0), (1.0, 1.0, 1.0), "BP_Suburbs_Wall_Thick_3x1m_A6", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (6039.0864, 3004.7998, 2300.0), (0.0, -92.81236999532442, 0.0), (1.0, 1.0, 1.0), "BP_Suburbs_Wall_Thick_3x1m_A7", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5958.833, 3409.2188, 2300.0), (0.0, -92.81236999532442, 0.0), (1.0, 1.0, 1.0), "BP_Suburbs_Wall_Thick_3x1m_A9", _folder)
if a: placed += 1
else: skipped += 1

# Batch 54: StaticMesh'Suburbs_Wall_Thin_1x3m_A' (8 instances)
_mesh_path = "/Game/Art/Assets/Kits/Architecture/Suburbs/Suburbs_Wall_Thin_1x3m_A"
_materials = ['/Game/Art/Assets/Kits/Architecture/Suburbs/Destructable/Materials/MI_Suburbs_Wall_Non_Dest']
_folder = "Reconstruction/BD_BB_Chapter2_Orctown_Throne/Meshes"
a = spawn_static_mesh(_mesh_path, _materials, (6026.82, 2755.1123, 1400.0), (0.0, -92.81236999532442, 0.0), (1.0, 1.0, 1.0), "BP_Suburbs_Wall_Thin_1x3m_A18_2", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (6070.979, 3654.0068, 1400.0), (0.0, -92.81236999532442, 0.0), (1.0, 1.0, 1.0), "BP_Suburbs_Wall_Thin_1x3m_A23", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (6076.76, 2752.6567, 1800.0), (0.0, 87.18759735891204, -0.0), (1.0, 1.0, 1.0), "BP_Suburbs_Wall_Thin_1x3m_E_2", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (6120.919, 3651.5828, 1800.0), (0.0, 87.18759735891204, -0.0), (1.0, 1.0, 1.0), "BP_Suburbs_Wall_Thin_1x3m_E2_160", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (6091.272, 3050.0671, 2200.0), (0.0, 87.18746121542567, -0.0), (1.0, 1.0, 1.0), "Suburbs_Wall_Thin_1x3m_A_134", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (6076.551, 2750.4287, 2200.0), (0.0, 87.18746121542567, -0.0), (1.0, 1.0, 1.0), "Suburbs_Wall_Thin_1x3m_A2", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (6105.9917, 3349.7063, 2200.0), (0.0, 87.18746121542567, -0.0), (1.0, 1.0, 1.0), "Suburbs_Wall_Thin_1x3m_A3", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (6120.713, 3649.3447, 2200.0), (0.0, 87.18746121542567, -0.0), (1.0, 1.0, 1.0), "Suburbs_Wall_Thin_1x3m_A4", _folder)
if a: placed += 1
else: skipped += 1

# Batch 55: StaticMesh'Suburbs_Wall_Thin_1x3m_A' (7 instances)
_mesh_path = "/Game/Art/Assets/Kits/Architecture/Suburbs/Suburbs_Wall_Thin_1x3m_A"
_materials = ['/Game/Art/Assets/Kits/Architecture/Suburbs/Materials/Suburbs_Wall/MI_Suburbs_Wall_Tile_A_Inst']
_folder = "Reconstruction/BD_BB_Chapter2_Orctown_Throne/Meshes"
a = spawn_static_mesh(_mesh_path, _materials, (6091.4795, 3052.2861, 1800.0), (0.0, 87.18757831705581, -0.0), (1.0, 1.0, 1.0), "BP_Suburbs_Wall_Thin_1x3m_A19", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (6106.199, 3351.9248, 1800.0), (0.0, 87.18757831705581, -0.0), (1.0, 1.0, 1.0), "BP_Suburbs_Wall_Thin_1x3m_A20", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (6041.5396, 3054.7395, 1400.0), (0.0, -92.81236999532442, 0.0), (1.0, 1.0, 1.0), "BP_Suburbs_Wall_Thin_1x3m_A21", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (6056.2593, 3354.3782, 1400.0), (0.0, -92.81236999532442, 0.0), (1.0, 1.0, 1.0), "BP_Suburbs_Wall_Thin_1x3m_A22", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (6011.226, 3456.7053, 2200.0), (0.0, 177.18761226169238, -0.0), (1.0, 1.0, 1.0), "BP_Suburbs_Wall_Thin_1x3m_A4_2", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5998.9595, 3207.012, 2200.0), (0.0, 177.18761226169238, -0.0), (1.0, 1.0, 1.0), "BP_Suburbs_Wall_Thin_1x3m_A7_20", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5986.6934, 2957.3188, 2200.0), (0.0, 177.18761226169238, -0.0), (1.0, 1.0, 1.0), "BP_Suburbs_Wall_Thin_1x3m_A8_21", _folder)
if a: placed += 1
else: skipped += 1

# Batch 56: StaticMesh'Suburbs_Wall_Thin_3x3m_A' (3 instances)
_mesh_path = "/Game/Art/Assets/Kits/Architecture/Suburbs/Suburbs_Wall_Thin_3x3m_A"
_materials = ['/Game/Art/Assets/Kits/Architecture/Suburbs/Destructable/Materials/MI_Suburbs_Wall_Non_Dest']
_folder = "Reconstruction/BD_BB_Chapter2_Orctown_Throne/Meshes"
a = spawn_static_mesh(_mesh_path, _materials, (6076.76, 2752.648, 1500.0), (0.0, 87.18753075119642, -0.0), (1.0, 1.0, 1.0), "Suburbs_Wall_Thin_3x3m_A_166", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (6120.9185, 3651.5637, 1500.0), (0.0, 87.18753075119642, -0.0), (1.0, 1.0, 1.0), "Suburbs_Wall_Thin_3x3m_A2", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (6101.8345, 3201.9583, 1500.0), (0.0, 87.18753075119642, -0.0), (1.0, 1.0, 1.0), "Suburbs_Wall_Thin_3x3m_A3", _folder)
if a: placed += 1
else: skipped += 1

# Batch 57: StaticMesh'Suburbs_Wall_Thin_Arch_Half_B' (3 instances)
_mesh_path = "/Game/Art/Assets/Kits/Architecture/Suburbs/Suburbs_Wall_Thin_Arch_Half_B"
_materials = ['/Game/Art/Assets/Kits/Architecture/Suburbs/Destructable/Materials/MI_Suburbs_Wall_Base_Dest']
_folder = "Reconstruction/BD_BB_Chapter2_Orctown_Throne/Meshes"
a = spawn_static_mesh(_mesh_path, _materials, (5849.152, 3214.3718, 1900.0), (0.0, 177.18761226169238, -0.0), (1.0, 1.0, 1.0), "BP_Suburbs_Wall_Thin_Arch_Half_B23", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5836.8853, 2964.6772, 1900.0), (0.0, 177.18761226169238, -0.0), (1.0, 1.0, 1.0), "BP_Suburbs_Wall_Thin_Arch_Half_B3_2", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5861.418, 3464.0679, 1900.0), (0.0, 177.18761226169238, -0.0), (1.0, 1.0, 1.0), "BP_Suburbs_Wall_Thin_Arch_Half_B4_5", _folder)
if a: placed += 1
else: skipped += 1

# Batch 58: StaticMesh'Suburbs_Wall_Thin_Arch_Half_C' (3 instances)
_mesh_path = "/Game/Art/Assets/Kits/Architecture/Suburbs/Suburbs_Wall_Thin_Arch_Half_C"
_materials = ['/Game/Art/Assets/Kits/Architecture/Suburbs/Destructable/Materials/MI_Suburbs_Wall_Base_Dest']
_folder = "Reconstruction/BD_BB_Chapter2_Orctown_Throne/Meshes"
a = spawn_static_mesh(_mesh_path, _materials, (6061.166, 3454.252, 1900.0), (0.0, -2.812469493326736, 0.0), (1.0, 1.0, 1.0), "BP_Suburbs_Wall_Thin_Arch_Half_C14_4", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (6048.8994, 3204.5588, 1900.0), (0.0, -2.812469493326736, 0.0), (1.0, 1.0, 1.0), "BP_Suburbs_Wall_Thin_Arch_Half_C15_6", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (6036.6333, 2954.8655, 1900.0), (0.0, -2.812469493326736, 0.0), (1.0, 1.0, 1.0), "BP_Suburbs_Wall_Thin_Arch_Half_C3_2", _folder)
if a: placed += 1
else: skipped += 1

# Batch 59: StaticMesh'Suburbs_Wall_Thin_Corner_A' (1 instances)
_mesh_path = "/Game/Art/Assets/Kits/Architecture/Suburbs/Suburbs_Wall_Thin_Corner_A"
_materials = ['/Game/Art/Assets/Kits/Architecture/Suburbs/Destructable/Materials/MI_Suburbs_Wall_Base_Dest']
_folder = "Reconstruction/BD_BB_Chapter2_Orctown_Throne/Meshes"
a = spawn_static_mesh(_mesh_path, _materials, (6113.5586, 3501.7441, 2300.0), (0.0, 87.18790429805797, -0.0), (1.0, 1.0, 1.0), "BP_Suburbs_Wall_Thin_Corner_A_Breakable12", _folder)
if a: placed += 1
else: skipped += 1

# Batch 60: StaticMesh'Suburbs_Wall_Thin_Corner_A' (2 instances)
_mesh_path = "/Game/Art/Assets/Kits/Architecture/Suburbs/Suburbs_Wall_Thin_Corner_A"
_materials = ['/Game/Art/Assets/Kits/Architecture/Suburbs/Destructable/Materials/MI_Suburbs_Wall_Non_Dest']
_folder = "Reconstruction/BD_BB_Chapter2_Orctown_Throne/Meshes"
a = spawn_static_mesh(_mesh_path, _materials, (6084.1196, 2902.4668, 1500.0), (0.0, 177.1874614149522, -0.0), (1.0, 1.0, 1.0), "BP_Suburbs_Wall_Thin_Corner_A_Breakable5_2", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (6113.5586, 3501.7441, 1500.0), (0.0, 87.18790429805797, -0.0), (1.0, 1.0, 1.0), "BP_Suburbs_Wall_Thin_Corner_A_Breakable6", _folder)
if a: placed += 1
else: skipped += 1

# Batch 61: StaticMesh'Suburbs_Wall_Thin_Window_Large_A' (2 instances)
_mesh_path = "/Game/Art/Assets/Kits/Architecture/Suburbs/Suburbs_Wall_Thin_Window_Large_A"
_materials = ['/Game/Art/Assets/Kits/Architecture/Suburbs/Destructable/Materials/MI_Suburbs_Wall_Non_Dest', '/Game/Art/Assets/Kits/Architecture/Suburbs/Materials/MI_Suburbs_Double_Window_A/MI_Suburbs_Wall_Thick_Window_Large_A']
_folder = "Reconstruction/BD_BB_Chapter2_Orctown_Throne/Meshes"
a = spawn_static_mesh(_mesh_path, _materials, (6120.9185, 3651.5522, 1900.0), (0.0, 87.18757831705581, -0.0), (1.0, 1.0, 1.0), "BP_Suburbs_Wall_Thin_Window_Large_B23", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (6076.76, 2752.6567, 1900.0), (0.0, 87.18757831705581, -0.0), (1.0, 1.0, 1.0), "BP_Suburbs_Wall_Thin_Window_Large_B33", _folder)
if a: placed += 1
else: skipped += 1

# Batch 62: StaticMesh'Suburbs_Wall_Thin_Window_Small_A' (2 instances)
_mesh_path = "/Game/Art/Assets/Kits/Architecture/Suburbs/Suburbs_Wall_Thin_Window_Small_A"
_materials = ['/Game/Art/Assets/Kits/Architecture/Suburbs/Destructable/Materials/MI_Suburbs_Wall_Non_Dest', '/Game/Art/Assets/Kits/Architecture/Suburbs/Materials/MI_Suburbs_Single_Window_A/MI_Suburbs_Single_Window_A']
_folder = "Reconstruction/BD_BB_Chapter2_Orctown_Throne/Meshes"
a = spawn_static_mesh(_mesh_path, _materials, (6091.4795, 3052.2861, 1900.0), (0.0, 87.18760344773338, -0.0), (1.0, 1.0, 1.0), "BP_Suburbs_Wall_Thin_Window_Small_C3_6", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (6106.2007, 3351.9246, 1900.0), (0.0, 87.18760344773338, -0.0), (1.0, 1.0, 1.0), "BP_Suburbs_Wall_Thin_Window_Small_C4_70", _folder)
if a: placed += 1
else: skipped += 1

# Batch 63: StaticMesh'Suburbs_Wall_Thin_Window_Small_C' (6 instances)
_mesh_path = "/Game/Art/Assets/Kits/Architecture/Suburbs/Suburbs_Wall_Thin_Window_Small_C"
_materials = ['/Game/Art/Assets/Kits/Architecture/Suburbs/Destructable/Materials/MI_Suburbs_Wall_Base_Dest']
_folder = "Reconstruction/BD_BB_Chapter2_Orctown_Throne/Meshes"
a = spawn_static_mesh(_mesh_path, _materials, (5843.253, 3094.5166, 2300.0), (0.0, 87.18757831705581, -0.0), (1.0, 1.0, 1.0), "BP_Suburbs_Wall_Thin_Window_Small_C_Breakable10_2", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5855.2734, 3339.2212, 2300.0), (0.0, 87.18757831705581, -0.0), (1.0, 1.0, 1.0), "BP_Suburbs_Wall_Thin_Window_Small_C_Breakable11", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5936.7534, 2959.7722, 2300.0), (0.0, 177.1875850299506, -0.0), (1.0, 1.0, 1.0), "BP_Suburbs_Wall_Thin_Window_Small_C_Breakable12_9", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (6120.9185, 3651.5522, 2300.0), (0.0, 87.18757831705581, -0.0), (1.0, 1.0, 1.0), "BP_Suburbs_Wall_Thin_Window_Small_C_Breakable13", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5961.286, 3459.1584, 2300.0), (0.0, -2.812500002205128, 0.0), (1.0, 1.0, 1.0), "BP_Suburbs_Wall_Thin_Window_Small_C_Breakable14_11", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (6077.5435, 2768.7793, 2300.0), (0.0, 87.18757831705581, -0.0), (1.0, 1.0, 1.0), "BP_Suburbs_Wall_Thin_Window_Small_C_Breakable15", _folder)
if a: placed += 1
else: skipped += 1

# Batch 64: StaticMesh'Trim_A_3m' (8 instances)
_mesh_path = "/Game/Art/Assets/Kits/Architecture/Suburbs/Trim_A_3m"
_materials = ['/Game/Art/Assets/Kits/Architecture/Suburbs/Materials/Suburbs_Trim_A/MI_Trim_A_3m']
_folder = "Reconstruction/BD_BB_Chapter2_Orctown_Throne/Meshes"
a = spawn_static_mesh(_mesh_path, _materials, (6044.431, 2604.0554, 1500.0), (0.0, 87.18753075119642, -0.0), (1.0, 1.0, 1.0), "Suburbs_Column_Single_Half_Shaft_A3", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (6088.59, 3502.9712, 1500.0), (0.0, 87.18753075119642, -0.0), (1.0, 1.0, 1.0), "Suburbs_Column_Single_Half_Shaft_A8", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (6074.9707, 3198.7732, 2300.0), (-9.155273682534808e-05, -92.81236999548855, -179.99989754715656), (1.0, 1.0, 1.0), "Trim_A_3m_137", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (6060.2495, 2899.1348, 2300.0), (-9.155273682534808e-05, -92.81236999548855, -179.99989754715656), (1.0, 1.0, 1.0), "Trim_A_3m2", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (6089.6904, 3498.4124, 2300.0), (-9.155273682534808e-05, -92.81236999548855, -179.99989754715656), (1.0, 1.0, 1.0), "Trim_A_3m3", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (6104.4116, 3798.0508, 2300.0), (-9.155273682534808e-05, -92.81236999548855, -179.99989754715656), (1.0, 1.0, 1.0), "Trim_A_3m4", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (6062.5107, 2904.692, 1900.0018), (-0.00036621097586648913, -92.81207564106747, 179.999959018845), (1.0, 1.0, 1.0), "Trim_A_3m5_155", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (6106.67, 3803.608, 1900.0018), (-0.00036621097586648913, -92.81207564106747, 179.999959018845), (1.0, 1.0, 1.0), "Trim_A_3m6", _folder)
if a: placed += 1
else: skipped += 1

# Batch 65: StaticMesh'Trim_A_3m_B' (4 instances)
_mesh_path = "/Game/Art/Assets/Kits/Architecture/Suburbs/Trim_A_3m_B"
_materials = ['/Game/Art/Assets/Kits/Architecture/Suburbs/Materials/Suburbs_Trim_A/MI_Trim_A_3m']
_folder = "Reconstruction/BD_BB_Chapter2_Orctown_Throne/Meshes"
a = spawn_static_mesh(_mesh_path, _materials, (6047.5464, 2899.7952, 1900.0), (0.0, 87.18746121542567, -0.0), (1.0, 1.0, 1.0), "Trim_A_3m_B_67", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (6062.2676, 3199.4336, 1900.0), (0.0, 87.18746121542567, -0.0), (1.0, 1.0, 1.0), "Trim_A_3m_B2", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (6032.825, 2600.1567, 1900.0), (0.0, 87.18746121542567, -0.0), (1.0, 1.0, 1.0), "Trim_A_3m_B3", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (6076.989, 3499.072, 1900.0), (0.0, 87.18746121542567, -0.0), (1.0, 1.0, 1.0), "Trim_A_3m_B4", _folder)
if a: placed += 1
else: skipped += 1

# Batch 66: StaticMesh'Mines_Lift_Beam_B' (24 instances)
_mesh_path = "/Game/Art/Assets/Kits/Deco/Mines/Machine/Mines_Machine_Lift_Pieces/Mines_Lift_Beam_B"
_materials = ['/Game/Art/Assets/Kits/Deco/Mines/Machine/Mines_Machine_Lift_Pieces/Materials/Mi_Mines_Machine_Lift_E']
_folder = "Reconstruction/BD_BB_Chapter2_Orctown_Throne/Meshes"
a = spawn_static_mesh(_mesh_path, _materials, (2428.85, 3783.2212, 1235.0), (0.0, -44.999875563225665, 0.0), (1.0, 1.0, 1.0), "Mines_Lift_Beam_B_215", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4026.8687, 2572.1716, 1195.0), (2.0490570851413735e-05, 135.00077584615937, -179.99963116974567), (1.0, 1.0, 1.0), "Mines_Lift_Beam_B10_653", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3778.8342, 2425.2034, 1235.0), (0.0, 135.00014775251523, -0.0), (1.0, 1.0, 1.0), "Mines_Lift_Beam_B11_654", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3831.869, 2372.1714, 1195.0), (2.0490570851413735e-05, 135.00077584615937, -179.99963116974567), (1.0, 1.0, 1.0), "Mines_Lift_Beam_B12_655", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2354.871, 2116.9607, 1379.1595), (-44.99306263769251, -134.99986913070774, -179.99998610351275), (1.0, 1.0, 1.0), "Mines_Lift_Beam_B13", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2120.8184, 2351.0144, 1379.1595), (-44.99306263769251, -134.99986913070774, -179.99998610351275), (1.0, 1.0, 1.0), "Mines_Lift_Beam_B14", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2623.932, 2422.1208, 1235.0), (0.0, 44.999970287262066, -0.0), (1.0, 1.0, 1.0), "Mines_Lift_Beam_B15", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2570.8982, 2369.0872, 1195.0), (2.0490564414000273e-05, 45.00070344405206, -179.99963116981672), (1.0, 1.0, 1.0), "Mines_Lift_Beam_B16", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2423.93, 2617.121, 1235.0), (0.0, 44.999970287262066, -0.0), (1.0, 1.0, 1.0), "Mines_Lift_Beam_B17", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2370.8984, 2564.0867, 1195.0), (2.0490564414000273e-05, 45.00070344405206, -179.99963116981672), (1.0, 1.0, 1.0), "Mines_Lift_Beam_B18", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4047.4746, 4275.799, 1379.1595), (-44.992667379715186, 44.99983322478779, -179.99998440925586), (1.0, 1.0, 1.0), "Mines_Lift_Beam_B19", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2375.8154, 3836.2537, 1195.0), (2.0490577358738125e-05, -44.999239305197534, -179.9996311697641), (1.0, 1.0, 1.0), "Mines_Lift_Beam_B2_217", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4281.5283, 4041.7449, 1379.1595), (-44.992667379715186, 44.99983322478779, -179.99998440925586), (1.0, 1.0, 1.0), "Mines_Lift_Beam_B20", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3778.413, 3970.6392, 1235.0), (0.0, -134.9999263430944, 0.0), (1.0, 1.0, 1.0), "Mines_Lift_Beam_B21", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3831.4473, 4023.673, 1195.0), (2.0490560814398246e-05, -134.99933165271054, -179.9996311698036), (1.0, 1.0, 1.0), "Mines_Lift_Beam_B22", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3978.4153, 3775.6392, 1235.0), (0.0, -134.9999263430944, 0.0), (1.0, 1.0, 1.0), "Mines_Lift_Beam_B23", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4031.4468, 3828.6729, 1195.0), (2.0490560814398246e-05, -134.99933165271054, -179.9996311698036), (1.0, 1.0, 1.0), "Mines_Lift_Beam_B24", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2623.85, 3983.2212, 1235.0), (0.0, -44.999875563225665, 0.0), (1.0, 1.0, 1.0), "Mines_Lift_Beam_B3", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2123.6914, 4052.2808, 1379.1595), (-44.993704554412034, 134.9996880303679, -179.9999844292484), (1.0, 1.0, 1.0), "Mines_Lift_Beam_B4", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2357.7434, 4286.3335, 1379.1595), (-44.993704554412034, 134.9996880303679, -179.9999844292484), (1.0, 1.0, 1.0), "Mines_Lift_Beam_B5", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2570.8154, 4036.2537, 1195.0), (2.0000012476409417e-05, -44.999239305199055, -179.999631169772), (1.0, 1.0, 1.0), "Mines_Lift_Beam_B6", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4278.994, 2356.1443, 1379.1595), (-44.99345351440318, -45.00026515584274, -179.9999817198584), (1.0, 1.0, 1.0), "Mines_Lift_Beam_B7_627", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4044.9412, 2122.0916, 1379.1595), (-44.99345351440318, -45.00026515584274, -179.9999817198584), (1.0, 1.0, 1.0), "Mines_Lift_Beam_B8_628", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3973.834, 2625.2046, 1235.0), (0.0, 135.00014775251523, -0.0), (1.0, 1.0, 1.0), "Mines_Lift_Beam_B9_652", _folder)
if a: placed += 1
else: skipped += 1

# Batch 67: StaticMesh'Mines_Lift_Beam_D' (8 instances)
_mesh_path = "/Game/Art/Assets/Kits/Deco/Mines/Machine/Mines_Machine_Lift_Pieces/Mines_Lift_Beam_D"
_materials = ['/Game/Art/Assets/Kits/Deco/Mines/Machine/Mines_Machine_Lift_Pieces/Materials/Mi_Mines_Machine_Lift_C']
_folder = "Reconstruction/BD_BB_Chapter2_Orctown_Throne/Meshes"
a = spawn_static_mesh(_mesh_path, _materials, (4432.718, 2165.6516, 1274.9991), (-2.027367615958555e-14, 44.9999986681553, 1.9999999711953134e-06), (1.0, 1.0, 1.0), "Mines_Lift_Beam_D10_597", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1962.8533, 2164.7646, 1274.9991), (-4.157553655978672e-14, -44.999940409163656, 1.9999998775045824e-06), (1.0, 1.0, 1.0), "Mines_Lift_Beam_D11", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2164.3782, 1963.2378, 1274.9991), (-4.157553655978672e-14, -44.999940409163656, 1.9999998775045824e-06), (1.0, 1.0, 1.0), "Mines_Lift_Beam_D12", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4439.4937, 4227.995, 1274.9991), (1.484029442475768e-14, 135.00012978593256, 2.000000463718785e-06), (1.0, 1.0, 1.0), "Mines_Lift_Beam_D13", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4237.9688, 4429.521, 1274.9991), (1.484029442475768e-14, 135.00012978593256, 2.000000463718785e-06), (1.0, 1.0, 1.0), "Mines_Lift_Beam_D14", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2171.494, 4444.2983, 1274.9991), (9.54854394090884e-15, -135.00000119449857, 1.81112847571185e-06), (1.0, 1.0, 1.0), "Mines_Lift_Beam_D7", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1969.9683, 4242.7744, 1274.9991), (9.54854394090884e-15, -135.00000119449857, 1.81112847571185e-06), (1.0, 1.0, 1.0), "Mines_Lift_Beam_D8", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4231.1914, 1964.1268, 1274.9991), (-2.027367615958555e-14, 44.9999986681553, 1.9999999711953134e-06), (1.0, 1.0, 1.0), "Mines_Lift_Beam_D9_596", _folder)
if a: placed += 1
else: skipped += 1

# Batch 68: StaticMesh'Mines_Machine_Whim_Cross_Beam' (15 instances)
_mesh_path = "/Game/Art/Assets/Kits/Deco/Mines/Machine/Mines_Machine_Whim_Pieces/Mines_Machine_Whim_Cross_Beam"
_materials = ['/Game/Art/Assets/Kits/Deco/Mines/Materials/Mines_Machine_Whim/MI_Mines_Machine_Whim_Trim', '/Game/Art/Assets/Kits/Deco/Mines/Materials/Mines_Machine_Whim/MI_Mines_Machine_Whim_Uniq']
_folder = "Reconstruction/BD_BB_Chapter2_Orctown_Throne/Meshes"
a = spawn_static_mesh(_mesh_path, _materials, (2173.7136, 1987.7146, 1197.9991), (3.415093841927044e-05, 45.00002294276241, -179.99995901885939), (1.0, 1.0, 1.0), "Mines_Machine_Whim_Cross_Beam10", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2190.6836, 1970.7427, 1261.9991), (7.513207515426818e-05, 45.00094536694211, 0.00012207030907526614), (1.0, 1.0, 1.0), "Mines_Machine_Whim_Cross_Beam11", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1975.7239, 2185.7058, 1197.9991), (3.415093841927044e-05, 45.00002294276241, -179.99995901885939), (1.0, 1.0, 1.0), "Mines_Machine_Whim_Cross_Beam12", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1992.6941, 2168.7346, 1261.9991), (7.513207515426818e-05, 45.00094536694211, 0.00012207030907526614), (1.0, 1.0, 1.0), "Mines_Machine_Whim_Cross_Beam13", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4228.633, 4405.0444, 1197.9991), (3.415093661656526e-05, -134.9997971847915, -179.99995901885634), (1.0, 1.0, 1.0), "Mines_Machine_Whim_Cross_Beam14", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4211.6626, 4422.0166, 1261.9991), (7.513208422074027e-05, -134.99893627691225, 0.000122070314216509), (1.0, 1.0, 1.0), "Mines_Machine_Whim_Cross_Beam15", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4426.6226, 4207.0537, 1197.9991), (3.415093661656526e-05, -134.9997971847915, -179.99995901885634), (1.0, 1.0, 1.0), "Mines_Machine_Whim_Cross_Beam16", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4409.653, 4224.025, 1261.9991), (7.513208422074027e-05, -134.99893627691225, 0.000122070314216509), (1.0, 1.0, 1.0), "Mines_Machine_Whim_Cross_Beam17", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1994.445, 4233.4375, 1197.9991), (3.415093496174466e-05, -44.99956437938897, -179.99995901885737), (1.0, 1.0, 1.0), "Mines_Machine_Whim_Cross_Beam2", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1977.4734, 4216.4688, 1261.9991), (7.513206690720864e-05, -44.99890067175212, 0.00012207030295212622), (1.0, 1.0, 1.0), "Mines_Machine_Whim_Cross_Beam3", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2192.4355, 4431.4277, 1197.9991), (3.399999181990317e-05, -44.999564379389, -179.9999590188578), (1.0, 1.0, 1.0), "Mines_Machine_Whim_Cross_Beam4", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4408.241, 2174.9875, 1197.9991), (3.41509354309722e-05, 135.00042153363898, -179.99995901885927), (1.0, 1.0, 1.0), "Mines_Machine_Whim_Cross_Beam6_638", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4425.2124, 2191.9565, 1261.9991), (7.513206830025423e-05, 135.00110256644194, 0.00012207030057902731), (1.0, 1.0, 1.0), "Mines_Machine_Whim_Cross_Beam7_639", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4210.25, 1976.9977, 1197.9991), (3.41509354309722e-05, 135.00042153363898, -179.99995901885927), (1.0, 1.0, 1.0), "Mines_Machine_Whim_Cross_Beam8_643", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4227.221, 1993.9672, 1261.9991), (7.513206830025423e-05, 135.00110256644194, 0.00012207030057902731), (1.0, 1.0, 1.0), "Mines_Machine_Whim_Cross_Beam9_644", _folder)
if a: placed += 1
else: skipped += 1

# Batch 69: StaticMesh'Mines_Machine_Whim_CrossBeam_Support' (10 instances)
_mesh_path = "/Game/Art/Assets/Kits/Deco/Mines/Machine/Mines_Machine_Whim_Pieces/Mines_Machine_Whim_CrossBeam_Support"
_materials = ['/Game/Art/Assets/Kits/Deco/Mines/Materials/Mines_Machine_Whim/MI_Mines_Machine_Whim_Trim', '/Game/Art/Assets/Kits/Deco/Mines/Materials/Mines_Machine_Whim/MI_Mines_Machine_Whim_Uniq']
_folder = "Reconstruction/BD_BB_Chapter2_Orctown_Throne/Meshes"
a = spawn_static_mesh(_mesh_path, _materials, (2702.8438, 3640.233, 1870.8213), (-19.686709972254103, 134.99961262452513, 90.00002762330216), (2.0, 2.0, 2.0), "Mines_Machine_Whim_CrossBeam_Support_189", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3160.0627, 2744.613, 2836.986), (0.0001375675366259211, 38.51153233356342, -0.000366210962377346), (3.0, 3.0, 3.0), "Mines_Machine_Whim_CrossBeam_Support17", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2773.3328, 3230.502, 2836.9922), (-0.00018310547726837635, -51.48587115687178, -0.00012207030597270785), (3.0, 3.0, 3.0), "Mines_Machine_Whim_CrossBeam_Support18", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2774.8582, 3688.4263, 1823.7432), (-19.68646000661948, 134.9996176231134, -89.99975602409397), (2.0, 2.0, 2.0), "Mines_Machine_Whim_CrossBeam_Support2", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3699.8406, 2768.1929, 1870.8213), (-19.686674960416607, -45.00027200887138, 89.99998464071498), (2.0, 2.0, 2.0), "Mines_Machine_Whim_CrossBeam_Support3_648", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3627.8262, 2719.9993, 1823.7432), (-19.686465995508314, -45.00036208757278, -89.99975989524224), (2.0, 2.0, 2.0), "Mines_Machine_Whim_CrossBeam_Support4_649", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2765.8071, 2697.2278, 1870.8214), (-19.686580689251567, -135.0001776625631, 89.99995544458984), (2.0, 2.0, 2.0), "Mines_Machine_Whim_CrossBeam_Support5", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2718.7249, 2768.1287, 1823.7432), (-19.68640446633548, -135.0002436162951, -89.99974753584655), (2.0, 2.0, 2.0), "Mines_Machine_Whim_CrossBeam_Support6", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3635.4253, 3696.6455, 1870.8213), (-19.686523326401883, 44.99987898672376, 89.99996169099312), (2.0, 2.0, 2.0), "Mines_Machine_Whim_CrossBeam_Support7", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3683.62, 3624.6316, 1823.7432), (-19.686306843318516, 44.99975329514075, -89.99975568663993), (2.0, 2.0, 2.0), "Mines_Machine_Whim_CrossBeam_Support8", _folder)
if a: placed += 1
else: skipped += 1

# Batch 70: StaticMesh'Mines_Machine_Whim_Heavy_Beam' (17 instances)
_mesh_path = "/Game/Art/Assets/Kits/Deco/Mines/Machine/Mines_Machine_Whim_Pieces/Mines_Machine_Whim_Heavy_Beam"
_materials = ['/Game/Art/Assets/Kits/Deco/Mines/Materials/Mines_Machine_Whim/MI_Mines_Machine_Whim_Trim', '/Game/Art/Assets/Kits/Deco/Mines/Materials/Mines_Machine_Whim/MI_Mines_Machine_Whim_Uniq']
_folder = "Reconstruction/BD_BB_Chapter2_Orctown_Throne/Meshes"
a = spawn_static_mesh(_mesh_path, _materials, (2107.698, 4094.372, 1224.9991), (0.0, -134.99997422266742, 0.0), (1.0, 1.0, 1.0), "Mines_Machine_Whim_Heavy_Beam_164", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2305.6887, 4292.364, 1224.9991), (0.0, -134.99997422266742, 0.0), (1.0, 1.0, 1.0), "Mines_Machine_Whim_Heavy_Beam2_180", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3267.4429, 3207.258, 2212.9902), (0.00029540064991876456, 85.90954869259649, -0.0002136230786766586), (3.0, 3.0, 3.0), "Mines_Machine_Whim_Heavy_Beam27", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4294.988, 2314.0535, 1224.9991), (0.0, 44.99999866815529, -0.0), (1.0, 1.0, 1.0), "Mines_Machine_Whim_Heavy_Beam3_640", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3260.551, 3172.2046, 2212.9902), (0.00026929377806601476, 38.65884372686585, -0.00018310545803280456), (3.0, 3.0, 3.0), "Mines_Machine_Whim_Heavy_Beam39", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4096.996, 2116.0618, 1224.9991), (0.0, 44.99999866815529, -0.0), (1.0, 1.0, 1.0), "Mines_Machine_Whim_Heavy_Beam4_645", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3242.5608, 3127.6335, 2212.9893), (0.00011786816870227756, -8.590545623380553, -0.0004272460955451407), (3.0, 3.0, 3.0), "Mines_Machine_Whim_Heavy_Beam40", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3242.8403, 3241.7288, 2212.9917), (-4.476050800173274e-12, 115.28383369264873, 0.00016999244330646719), (3.0, 3.0, 3.0), "Mines_Machine_Whim_Heavy_Beam41", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3189.7937, 3111.464, 2212.9922), (-3.051757591995758e-05, -54.83862280586633, 1.549720874142074e-06), (3.0, 3.0, 3.0), "Mines_Machine_Whim_Heavy_Beam42", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3138.3323, 3167.0615, 2212.9912), (3.695485677965023e-05, -96.71608557969797, 0.0006414651880606299), (3.0, 3.0, 3.0), "Mines_Machine_Whim_Heavy_Beam43", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3125.673, 3213.9465, 2212.9902), (8.034705471176827e-05, -141.71557708199097, 0.00038838386577922084), (3.0, 3.0, 3.0), "Mines_Machine_Whim_Heavy_Beam44", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3183.5366, 3262.986, 2212.9922), (0.00016081331090114426, 177.15972984619486, 0.0005064010140321772), (3.0, 3.0, 3.0), "Mines_Machine_Whim_Heavy_Beam45", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3245.0654, 3243.7444, 2212.9902), (6.747244821698377e-05, 132.15994790034694, 0.0004098414986578254), (3.0, 3.0, 3.0), "Mines_Machine_Whim_Heavy_Beam46", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2312.7798, 2100.9675, 1224.9991), (0.0, -44.99994040916364, 0.0), (1.0, 1.0, 1.0), "Mines_Machine_Whim_Heavy_Beam5", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2114.7886, 2298.9592, 1224.9991), (0.0, -44.99994040916364, 0.0), (1.0, 1.0, 1.0), "Mines_Machine_Whim_Heavy_Beam6", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4089.5654, 4291.792, 1224.9991), (0.0, 135.00012978593256, -0.0), (1.0, 1.0, 1.0), "Mines_Machine_Whim_Heavy_Beam7", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4287.5576, 4093.8, 1224.9991), (0.0, 135.00012978593256, -0.0), (1.0, 1.0, 1.0), "Mines_Machine_Whim_Heavy_Beam8", _folder)
if a: placed += 1
else: skipped += 1

# Batch 71: StaticMesh'Mines_Machine_Whim_Main_Beam' (16 instances)
_mesh_path = "/Game/Art/Assets/Kits/Deco/Mines/Machine/Mines_Machine_Whim_Pieces/Mines_Machine_Whim_Main_Beam"
_materials = ['/Game/Art/Assets/Kits/Deco/Mines/Materials/Mines_Machine_Whim/MI_Mines_Machine_Whim_Trim']
_folder = "Reconstruction/BD_BB_Chapter2_Orctown_Throne/Meshes"
a = spawn_static_mesh(_mesh_path, _materials, (4318.8477, 4263.0527, 1739.424), (-0.5612182242244189, -45.11770637838938, -0.5455016963553463), (1.0, 1.0, 1.0), "Mines_Machine_Whim_Main_Beam10", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2143.3909, 2013.775, 1608.8461), (-0.5452880994867849, 134.87155976710403, 0.5614620596939576), (1.0, 1.0, 1.0), "Mines_Machine_Whim_Main_Beam11", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2037.1282, 2120.504, 1607.4126), (-0.5452880994867849, 134.87155976710403, 0.5614620596939576), (1.0, 1.0, 1.0), "Mines_Machine_Whim_Main_Beam12", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2153.802, 2057.1814, 1710.0583), (-0.5452880994867849, 134.87155976710403, 0.5614620596939576), (1.0, 1.0, 1.0), "Mines_Machine_Whim_Main_Beam13", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2082.968, 2126.1562, 1710.1344), (-0.5452880994867849, 134.87155976710403, 0.5614620596939576), (1.0, 1.0, 1.0), "Mines_Machine_Whim_Main_Beam14", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4367.8433, 2154.222, 1624.8743), (-1.1067200793876741, -135.12322972887114, 0.015990746486558516), (1.0, 1.0, 1.0), "Mines_Machine_Whim_Main_Beam15", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4261.171, 2048.005, 1621.967), (-1.1067200793876741, -135.12322972887114, 0.015990746486558516), (1.0, 1.0, 1.0), "Mines_Machine_Whim_Main_Beam16", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4321.5684, 2163.1404, 1725.4462), (-1.1067200793876741, -135.12322972887114, 0.015990746486558516), (1.0, 1.0, 1.0), "Mines_Machine_Whim_Main_Beam17", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4252.234, 2092.1086, 1724.5581), (-1.1067200793876741, -135.12322972887114, 0.015990746486558516), (1.0, 1.0, 1.0), "Mines_Machine_Whim_Main_Beam18", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2020.0537, 4250.9473, 1623.4366), (4.100000297833053e-05, 44.87697677653254, -7.449410253446028e-13), (1.0, 1.0, 1.0), "Mines_Machine_Whim_Main_Beam3", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2126.9492, 4357.3945, 1623.4369), (4.100000297833053e-05, 44.87697677653254, -7.449410253446028e-13), (1.0, 1.0, 1.0), "Mines_Machine_Whim_Main_Beam4", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2065.419, 4241.0913, 1724.4896), (4.100000297833053e-05, 44.87697677653254, -7.449410253446028e-13), (1.0, 1.0, 1.0), "Mines_Machine_Whim_Main_Beam5", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2139.831, 4317.3364, 1725.5187), (4.100000297833053e-05, 44.87697677653254, -7.449410253446028e-13), (1.0, 1.0, 1.0), "Mines_Machine_Whim_Main_Beam6", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4245.581, 4368.72, 1638.7906), (-0.5612182242244189, -45.11770637838938, -0.5455016963553463), (1.0, 1.0, 1.0), "Mines_Machine_Whim_Main_Beam7", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4352.0327, 4261.84, 1637.313), (-0.5612182242244189, -45.11770637838938, -0.5455016963553463), (1.0, 1.0, 1.0), "Mines_Machine_Whim_Main_Beam8", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4247.483, 4332.566, 1739.3578), (-0.5612182242244189, -45.11770637838938, -0.5455016963553463), (1.0, 1.0, 1.0), "Mines_Machine_Whim_Main_Beam9", _folder)
if a: placed += 1
else: skipped += 1

# Batch 72: StaticMesh'Mines_Machine_Whim_Main_Post_B' (10 instances)
_mesh_path = "/Game/Art/Assets/Kits/Deco/Mines/Machine/Mines_Machine_Whim_Pieces/Mines_Machine_Whim_Main_post_B"
_materials = ['/Game/Art/Assets/Kits/Deco/Mines/Materials/Mines_Machine_Whim/MI_Mines_Machine_Whim_Trim', '/Game/Art/Assets/Kits/Deco/Mines/Materials/Mines_Machine_Whim/MI_Mines_Machine_Whim_Uniq']
_folder = "Reconstruction/BD_BB_Chapter2_Orctown_Throne/Meshes"
a = spawn_static_mesh(_mesh_path, _materials, (2394.9397, 4178.4277, 1409.9991), (-5.6968616496447634e-08, -45.00002940667403, -89.99994459691897), (1.0, 1.0, 1.0), "Mines_Machine_Whim_Main_Post_B15", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2230.1836, 4013.6704, 1409.9991), (1.7408293736620362e-07, -44.99999975053782, 90.0001215429926), (1.0, 1.0, 1.0), "Mines_Machine_Whim_Main_Post_B16", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3204.9158, 3196.6155, 2317.991), (0.00017075473157909658, 55.28390042649823, -179.99959701882702), (3.0, 3.0, 3.0), "Mines_Machine_Whim_Main_Post_B20", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3204.9204, 3196.6152, 2512.992), (0.0001366138448646053, 50.28460675793765, -0.0001831054783409031), (3.0, 3.0, 3.0), "Mines_Machine_Whim_Main_Post_B21", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4007.7446, 2229.9973, 1409.9991), (3.992370762051606e-06, 134.9999752330455, -89.99988139489624), (1.0, 1.0, 1.0), "Mines_Machine_Whim_Main_Post_B22_604", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4172.501, 2394.7546, 1409.9991), (4.271236717176501e-06, 135.00002307122398, 90.00009431804652), (1.0, 1.0, 1.0), "Mines_Machine_Whim_Main_Post_B23_605", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2228.7246, 2388.2107, 1409.9991), (7.546976930439122e-06, 44.999848534989376, -89.9998764229895), (1.0, 1.0, 1.0), "Mines_Machine_Whim_Main_Post_B24", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2393.4817, 2223.4539, 1409.9991), (3.290240501999803e-06, 44.99978208435728, 90.00010840261122), (1.0, 1.0, 1.0), "Mines_Machine_Whim_Main_Post_B25", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4173.621, 4004.5488, 1409.9991), (3.501542318873485e-06, -135.00013237580302, -89.99976267921338), (1.0, 1.0, 1.0), "Mines_Machine_Whim_Main_Post_B26", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4008.8643, 4169.3066, 1409.9991), (4.924808310267826e-06, -135.00000189744185, 90.0000929895426), (1.0, 1.0, 1.0), "Mines_Machine_Whim_Main_Post_B27", _folder)
if a: placed += 1
else: skipped += 1

# Batch 73: StaticMesh'Mines_Machine_Whim_Main_Post_C' (1 instances)
_mesh_path = "/Game/Art/Assets/Kits/Deco/Mines/Machine/Mines_Machine_Whim_Pieces/Mines_Machine_Whim_Main_Post_C"
_materials = ['/Game/Art/Assets/Kits/Deco/Mines/Materials/Mines_Machine_Whim/MI_Mines_Machine_Whim_Trim', '/Game/Art/Assets/Kits/Deco/Mines/Materials/Mines_Machine_Whim/MI_Mines_Machine_Whim_Uniq']
_folder = "Reconstruction/BD_BB_Chapter2_Orctown_Throne/Meshes"
a = spawn_static_mesh(_mesh_path, _materials, (3204.9167, 3196.6152, 2092.99), (0.0004098111617686342, -179.9999590188464, -179.99998633961468), (3.0, 3.0, 3.0), "Mines_Machine_Whim_Main_Post_C_146", _folder)
if a: placed += 1
else: skipped += 1

# Batch 74: StaticMesh'Mines_Machine_Whim_Main_Post_D' (10 instances)
_mesh_path = "/Game/Art/Assets/Kits/Deco/Mines/Machine/Mines_Machine_Whim_Pieces/Mines_Machine_Whim_Main_Post_D"
_materials = ['/Game/Art/Assets/Kits/Deco/Mines/Materials/Mines_Machine_Whim/MI_Mines_Machine_Whim_Trim', '/Game/Art/Assets/Kits/Deco/Mines/Materials/Mines_Machine_Whim/MI_Mines_Machine_Whim_Uniq']
_folder = "Reconstruction/BD_BB_Chapter2_Orctown_Throne/Meshes"
a = spawn_static_mesh(_mesh_path, _materials, (2387.1184, 2229.818, 1409.9991), (2.8924351750665632e-05, 44.999913616892, -89.99988382085519), (1.0, 1.0, 1.0), "Mines_Machine_Whim_Main_Post_D10", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4167.2583, 4010.912, 1409.9991), (2.267853311531663e-06, -135.0000035762737, 90.0000162061414), (1.0, 1.0, 1.0), "Mines_Machine_Whim_Main_Post_D11", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4015.2273, 4162.942, 1409.9991), (4.449449805171974e-05, -135.00000870365372, -89.99989675612059), (1.0, 1.0, 1.0), "Mines_Machine_Whim_Main_Post_D12", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3204.92, 3196.6138, 2809.9915), (0.00019145013887952842, 65.28439685109716, -0.0004272461143642095), (3.0, 3.0, 3.0), "Mines_Machine_Whim_Main_Post_D15", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3204.92, 3196.6147, 2266.9915), (0.0002491474252737003, 60.285153823623375, 0.00021362305854919015), (3.0, 3.0, 3.0), "Mines_Machine_Whim_Main_Post_D16", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2388.576, 4172.0645, 1409.9991), (3.1919684517989634e-07, -44.99993739053641, 90.00002207034504), (1.0, 1.0, 1.0), "Mines_Machine_Whim_Main_Post_D5", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2236.5476, 4020.0344, 1409.9991), (-4.864222617501542e-07, -44.99993848686329, -89.99991611342887), (1.0, 1.0, 1.0), "Mines_Machine_Whim_Main_Post_D6", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4014.1082, 2236.3606, 1409.9991), (4.062210946580085e-06, 135.00012062368404, 90.00002034212628), (1.0, 1.0, 1.0), "Mines_Machine_Whim_Main_Post_D7_606", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4166.137, 2388.3909, 1409.9991), (-1.9836399852374636e-06, 135.0000673480192, -89.99991177227716), (1.0, 1.0, 1.0), "Mines_Machine_Whim_Main_Post_D8_607", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2235.0874, 2381.8472, 1409.9991), (4.172451424047271e-06, 44.999872966433635, 90.00001957147363), (1.0, 1.0, 1.0), "Mines_Machine_Whim_Main_Post_D9", _folder)
if a: placed += 1
else: skipped += 1

# Batch 75: StaticMesh'Mines_Machine_Whim_Main_Post_E' (5 instances)
_mesh_path = "/Game/Art/Assets/Kits/Deco/Mines/Machine/Mines_Machine_Whim_Pieces/Mines_Machine_Whim_Main_Post_E"
_materials = ['/Game/Art/Assets/Kits/Deco/Mines/Materials/Mines_Machine_Whim/MI_Mines_Machine_Whim_Uniq']
_folder = "Reconstruction/BD_BB_Chapter2_Orctown_Throne/Meshes"
a = spawn_static_mesh(_mesh_path, _materials, (4368.3706, 2324.751, 1299.9991), (5.966806899499068e-06, 135.0000030469303, 90.00001310531604), (1.815606, 1.815606, 5.672873), "Mines_Machine_Whim_Main_Post_E10_629", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2323.4783, 2027.5841, 1299.9991), (4.38525166066193e-06, 44.999753872193715, 90.0000087354638), (1.815606, 1.815606, 5.672873), "Mines_Machine_Whim_Main_Post_E11", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4078.8674, 4365.1753, 1299.9991), (4.172452044255433e-06, -135.00012009433732, 90.00002406310779), (1.815606, 1.815606, 5.672873), "Mines_Machine_Whim_Main_Post_E12", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2034.3152, 4083.6746, 1299.9991), (-6.110373483362992e-07, -44.9999920983774, 90.0000149658148), (1.815606, 1.815606, 5.672873), "Mines_Machine_Whim_Main_Post_E7", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3204.611, 3204.352, 3020.7515), (0.00015425682395745348, -44.99938898346569, -0.00027465823401272527), (3.0, 3.0, 3.0), "Mines_Machine_Whim_Main_Post_E9", _folder)
if a: placed += 1
else: skipped += 1

# Batch 76: StaticMesh'Mines_Machine_Whim_Pole_Support' (8 instances)
_mesh_path = "/Game/Art/Assets/Kits/Deco/Mines/Machine/Mines_Machine_Whim_Pieces/Mines_Machine_Whim_Pole_Support"
_materials = ['/Game/Art/Assets/Kits/Deco/Mines/Materials/Mines_Machine_Whim/MI_Mines_Machine_Whim_Trim', '/Game/Art/Assets/Kits/Deco/Mines/Materials/Mines_Machine_Whim/MI_Mines_Machine_Whim_Uniq']
_folder = "Reconstruction/BD_BB_Chapter2_Orctown_Throne/Meshes"
a = spawn_static_mesh(_mesh_path, _materials, (3234.656, 3248.2905, 2836.9856), (4.768370673231917e-05, 35.56640635723586, -0.0003967284874346883), (3.0, 3.0, 3.0), "Mines_Machine_Whim_Pole_Support35", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3179.4167, 3263.523, 2836.9902), (0.0003190040871521373, 80.57233034894686, -0.00021362307444789522), (3.0, 3.0, 3.0), "Mines_Machine_Whim_Pole_Support36", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3265.1006, 3212.997, 2836.9856), (6.899238012669506e-05, -9.425352765433693, -0.0005187987866886527), (3.0, 3.0, 3.0), "Mines_Machine_Whim_Pole_Support37", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3256.621, 3165.7422, 2836.9912), (-9.155273041000207e-05, -52.65911695574177, -0.00012207030474339026), (3.0, 3.0, 3.0), "Mines_Machine_Whim_Pole_Support38", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3213.3105, 3127.7993, 2836.9856), (-3.051756154283838e-05, -95.29608327645006, 0.0004036426137054901), (3.0, 3.0, 3.0), "Mines_Machine_Whim_Pole_Support39", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3159.5405, 3128.9067, 2836.9893), (6.091595698890942e-05, -139.432062929622, 0.0005087852290388527), (3.0, 3.0, 3.0), "Mines_Machine_Whim_Pole_Support40", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3144.2834, 3180.853, 2836.9856), (0.0001022815687010343, 175.5712269138475, 0.0005836486433234783), (3.0, 3.0, 3.0), "Mines_Machine_Whim_Pole_Support41", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3149.8838, 3240.346, 2836.9893), (0.00029087065277703483, 130.56659173067064, 0.0003428458653125203), (3.0, 3.0, 3.0), "Mines_Machine_Whim_Pole_Support42", _folder)
if a: placed += 1
else: skipped += 1

# Batch 77: StaticMesh'Mines_Machine_Whim_Rope_Support' (4 instances)
_mesh_path = "/Game/Art/Assets/Kits/Deco/Mines/Machine/Mines_Machine_Whim_Pieces/Mines_Machine_Whim_Rope_Support"
_materials = ['/Game/Art/Assets/Kits/Deco/Mines/Materials/Mines_Machine_Whim/MI_Mines_Machine_Whim_Trim', '/Game/Art/Assets/Kits/Deco/Mines/Materials/Mines_Machine_Whim/MI_Mines_Machine_Whim_Uniq']
_folder = "Reconstruction/BD_BB_Chapter2_Orctown_Throne/Meshes"
a = spawn_static_mesh(_mesh_path, _materials, (2881.8813, 3732.3735, 2671.9927), (9.10759059145071e-05, -149.37587095464494, 0.000541925383318728), (3.0, 3.0, 3.0), "Mines_Machine_Whim_Rope_Support21", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3511.4663, 2666.8677, 2671.9907), (-3.0517566343694204e-05, 30.627042122546886, -0.00027465822812189106), (3.0, 3.0, 3.0), "Mines_Machine_Whim_Rope_Support22", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2663.5603, 2884.076, 2671.9832), (-0.00015258789543457228, -59.37121403904471, 2.133846778250144e-05), (3.0, 3.0, 3.0), "Mines_Machine_Whim_Rope_Support23", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3730.4065, 3515.9932, 2671.992), (-0.00030517577748707725, 120.62396050635658, 0.0005321502508704674), (3.0, 3.0, 3.0), "Mines_Machine_Whim_Rope_Support24", _folder)
if a: placed += 1
else: skipped += 1

# Batch 78: StaticMesh'Mines_Machine_Whim_Side_Support' (8 instances)
_mesh_path = "/Game/Art/Assets/Kits/Deco/Mines/Machine/Mines_Machine_Whim_Pieces/Mines_Machine_Whim_Side_Support"
_materials = ['/Game/Art/Assets/Kits/Deco/Mines/Materials/Mines_Machine_Whim/MI_Mines_Machine_Whim_Trim', '/Game/Art/Assets/Kits/Deco/Mines/Materials/Mines_Machine_Whim/MI_Mines_Machine_Whim_Uniq']
_folder = "Reconstruction/BD_BB_Chapter2_Orctown_Throne/Meshes"
a = spawn_static_mesh(_mesh_path, _materials, (2349.8198, 3861.6995, 805.0), (0.0, 45.000351921505654, -0.0), (1.0, 1.0, 1.0), "Mines_Machine_Whim_Side_Support_197", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2547.8086, 4059.69, 805.0), (0.0, 45.000351921505654, -0.0), (1.0, 1.0, 1.0), "Mines_Machine_Whim_Side_Support2", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4050.0754, 2549.4675, 805.0), (0.0, -134.99960987047803, 0.0), (1.0, 1.0, 1.0), "Mines_Machine_Whim_Side_Support3_650", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3852.0867, 2351.476, 805.0), (0.0, -134.99960987047803, 0.0), (1.0, 1.0, 1.0), "Mines_Machine_Whim_Side_Support4_651", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2544.5093, 2342.191, 805.0), (0.0, 135.00026261227782, -0.0), (1.0, 1.0, 1.0), "Mines_Machine_Whim_Side_Support5", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2346.518, 2540.182, 805.0), (0.0, 135.00026261227782, -0.0), (1.0, 1.0, 1.0), "Mines_Machine_Whim_Side_Support6", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3854.775, 4047.5103, 805.0), (0.0, -44.999723200496135, 0.0), (1.0, 1.0, 1.0), "Mines_Machine_Whim_Side_Support7", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4052.767, 3849.519, 805.0), (0.0, -44.999723200496135, 0.0), (1.0, 1.0, 1.0), "Mines_Machine_Whim_Side_Support8", _folder)
if a: placed += 1
else: skipped += 1

# Batch 79: StaticMesh'Mines_Machine_Whim_Side_Support_Beam' (16 instances)
_mesh_path = "/Game/Art/Assets/Kits/Deco/Mines/Machine/Mines_Machine_Whim_Pieces/Mines_Machine_Whim_Side_Support_Beam"
_materials = ['/Game/Art/Assets/Kits/Deco/Mines/Materials/Mines_Machine_Whim/MI_Mines_Machine_Whim_Trim', '/Game/Art/Assets/Kits/Deco/Mines/Materials/Mines_Machine_Whim/MI_Mines_Machine_Whim_Uniq']
_folder = "Reconstruction/BD_BB_Chapter2_Orctown_Throne/Meshes"
a = spawn_static_mesh(_mesh_path, _materials, (2471.7053, 4049.9802, 1605.6268), (12.808966842048019, 124.90001976132906, 7.896675451939985), (1.0, 1.0, 1.0), "Mines_Machine_Whim_Side_Support_Beam16", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2494.0205, 4017.9895, 1596.7585), (-12.80718988589466, -55.09533489245914, 172.1098510382258), (1.0, 1.0, 1.0), "Mines_Machine_Whim_Side_Support_Beam17", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2338.6628, 3902.5334, 1612.3246), (12.808673050763803, 145.09981857840907, -7.896849372959571), (1.0, 1.0, 1.0), "Mines_Machine_Whim_Side_Support_Beam18", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2370.652, 3880.22, 1603.4531), (-12.808349453617549, -34.90045094844467, -172.10921329613794), (1.0, 1.0, 1.0), "Mines_Machine_Whim_Side_Support_Beam19", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3930.979, 2358.445, 1605.6268), (12.808966768927315, -55.09991877047116, 7.896781571649718), (1.0, 1.0, 1.0), "Mines_Machine_Whim_Side_Support_Beam21_590", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3908.6638, 2390.4353, 1596.7585), (-12.807188903053012, 124.90473172645532, 172.10985111390895), (1.0, 1.0, 1.0), "Mines_Machine_Whim_Side_Support_Beam22_591", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4064.0212, 2505.8914, 1612.3246), (12.808641831031661, -34.90030083761065, -7.897003543145111), (1.0, 1.0, 1.0), "Mines_Machine_Whim_Side_Support_Beam23_592", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4032.0312, 2528.2058, 1603.4535), (-12.808256685157874, 145.10077418874715, -172.10817964690912), (1.0, 1.0, 1.0), "Mines_Machine_Whim_Side_Support_Beam24_593", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2357.1719, 2464.9763, 1605.6268), (12.808968182068474, -145.09979071336699, 7.896983712944839), (1.0, 1.0, 1.0), "Mines_Machine_Whim_Side_Support_Beam25", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2389.1624, 2487.291, 1596.7585), (-12.807189462833467, 34.90481922380726, 172.10985240584884), (1.0, 1.0, 1.0), "Mines_Machine_Whim_Side_Support_Beam26", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2504.6187, 2331.9338, 1612.325), (12.8084539752232, -124.90031534086515, -7.897856885215055), (1.0, 1.0, 1.0), "Mines_Machine_Whim_Side_Support_Beam27", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2526.9326, 2363.9238, 1603.4531), (-12.808501706336894, 55.10058024008574, -172.10921319057593), (1.0, 1.0, 1.0), "Mines_Machine_Whim_Side_Support_Beam28", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4045.1733, 3927.7832, 1605.6268), (12.80896725621566, 34.90026906594073, 7.897153757054798), (1.0, 1.0, 1.0), "Mines_Machine_Whim_Side_Support_Beam29", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4013.1829, 3905.469, 1596.7585), (-12.807189404758935, -145.0950918675474, 172.10985152494771), (1.0, 1.0, 1.0), "Mines_Machine_Whim_Side_Support_Beam30", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3897.7266, 4060.8262, 1612.325), (12.808438941777377, 55.09960662443907, -7.897399378540932), (1.0, 1.0, 1.0), "Mines_Machine_Whim_Side_Support_Beam31", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3875.412, 4028.8364, 1603.4531), (-12.808502046302932, -124.89940199994669, -172.10908332024184), (1.0, 1.0, 1.0), "Mines_Machine_Whim_Side_Support_Beam32", _folder)
if a: placed += 1
else: skipped += 1

# Batch 80: StaticMesh'Mines_Machine_Whim_Wheel' (8 instances)
_mesh_path = "/Game/Art/Assets/Kits/Deco/Mines/Machine/Mines_Machine_Whim_Pieces/Mines_Machine_Whim_Wheel"
_materials = ['/Game/Art/Assets/Kits/Deco/Mines/Materials/Mines_Machine_Whim/MI_Mines_Machine_Whim_Trim', '/Game/Art/Assets/Kits/Deco/Mines/Materials/Mines_Machine_Whim/MI_Mines_Machine_Whim_Uniq']
_folder = "Reconstruction/BD_BB_Chapter2_Orctown_Throne/Meshes"
a = spawn_static_mesh(_mesh_path, _materials, (2169.3723, 3952.8591, 1409.9991), (8.670955594257206e-14, -45.00008654840737, 4.22597487518104e-06), (1.0, 1.0, 1.0), "Mines_Machine_Whim_Wheel18", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2455.751, 4239.239, 1409.9991), (1.1481544622450006e-14, -45.00008654840733, 2.4148399133874883e-06), (1.0, 1.0, 1.0), "Mines_Machine_Whim_Wheel19", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4233.313, 2455.5664, 1409.9991), (4.218643557869376e-14, 134.99987621772053, 3.999999702224419e-06), (1.0, 1.0, 1.0), "Mines_Machine_Whim_Wheel20_608", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3946.9333, 2169.186, 1409.9991), (1.0506343224931243e-14, 134.9998762177205, 1.9999998554974484e-06), (1.0, 1.0, 1.0), "Mines_Machine_Whim_Wheel21_611", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2454.2922, 2162.6426, 1409.9991), (-9.241719817097653e-15, 44.99972320049619, 3.999999788308096e-06), (1.0, 1.0, 1.0), "Mines_Machine_Whim_Wheel22", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2167.9133, 2449.0225, 1409.9991), (5.966030295872948e-15, 44.999723200496156, 1.99999989853925e-06), (1.0, 1.0, 1.0), "Mines_Machine_Whim_Wheel23", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3948.0532, 4230.1177, 1409.9991), (-2.3662038465151412e-14, -135.00012978593261, 4.00000043379869e-06), (1.0, 1.0, 1.0), "Mines_Machine_Whim_Wheel24", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4234.432, 3943.7378, 1409.9991), (-2.2417904223662103e-14, -135.00012978593256, 2.000000212514126e-06), (1.0, 1.0, 1.0), "Mines_Machine_Whim_Wheel25", _folder)
if a: placed += 1
else: skipped += 1

# Batch 81: StaticMesh'Mines_Machine_Whim_Wheel_Large' (4 instances)
_mesh_path = "/Game/Art/Assets/Kits/Deco/Mines/Machine/Mines_Machine_Whim_Pieces/Mines_Machine_Whim_Wheel_Large"
_materials = ['/Game/Art/Assets/Kits/Deco/Mines/Materials/Mines_Machine_Whim/MI_Mines_Machine_Whim_Trim', '/Game/Art/Assets/Kits/Deco/Mines/Materials/Mines_Machine_Whim/MI_Mines_Machine_Whim_Uniq']
_folder = "Reconstruction/BD_BB_Chapter2_Orctown_Throne/Meshes"
a = spawn_static_mesh(_mesh_path, _materials, (2724.151, 3678.0896, 1858.1315), (11.249970017052677, -44.99975304293986, -0.0002133856306798971), (1.0, 1.0, 1.0), "Mines_Machine_Whim_Wheel_Large2_83", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3678.5332, 2730.3367, 1858.1315), (11.249969787171477, 135.00029909679702, -0.00018303592911640776), (1.0, 1.0, 1.0), "Mines_Machine_Whim_Wheel_Large3_635", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2729.0637, 2717.422, 1858.1315), (11.249970318035386, 45.00030536267477, -0.0001832144825079892), (1.0, 1.0, 1.0), "Mines_Machine_Whim_Wheel_Large4", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3673.281, 3675.3381, 1858.1315), (11.249969833559478, -134.9996314139216, -0.00018261954567264308), (1.0, 1.0, 1.0), "Mines_Machine_Whim_Wheel_Large5", _folder)
if a: placed += 1
else: skipped += 1

# Batch 82: StaticMesh'Mines_Machine_Whim_Wheel_Pole' (16 instances)
_mesh_path = "/Game/Art/Assets/Kits/Deco/Mines/Machine/Mines_Machine_Whim_Pieces/Mines_Machine_Whim_Wheel_Pole"
_materials = ['/Game/Art/Assets/Kits/Deco/Mines/Materials/Mines_Machine_Whim/MI_Mines_Machine_Whim_Trim', '/Game/Art/Assets/Kits/Deco/Mines/Materials/Mines_Machine_Whim/MI_Mines_Machine_Whim_Uniq']
_folder = "Reconstruction/BD_BB_Chapter2_Orctown_Throne/Meshes"
a = spawn_static_mesh(_mesh_path, _materials, (2148.159, 3931.6455, 1409.9991), (8.089984836114097e-14, -45.000086548407396, 5.433398247567911e-06), (1.0, 1.0, 1.0), "Mines_Machine_Whim_Wheel_Pole10", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4254.526, 2476.7793, 1409.9991), (-4.4832457884069837e-14, 134.99987621772053, 4.999999916259722e-06), (1.0, 1.0, 1.0), "Mines_Machine_Whim_Wheel_Pole11_609", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2476.9646, 4260.4526, 1409.9991), (3.2096431971221195e-14, -44.99993506252903, -179.99995901885765), (1.0, 1.0, 1.0), "Mines_Machine_Whim_Wheel_Pole12", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3925.7195, 2147.9727, 1409.9991), (-2.3792082670661737e-13, 135.0000187757218, -179.99995901885126), (1.0, 1.0, 1.0), "Mines_Machine_Whim_Wheel_Pole13_610", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2475.5056, 2141.4294, 1409.9991), (6.408834054917836e-14, 44.99972320049622, 5.00000007679844e-06), (1.0, 1.0, 1.0), "Mines_Machine_Whim_Wheel_Pole14", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2146.6992, 2470.236, 1409.9991), (2.2961796095068863e-12, 44.99971586493512, -179.99995901885825), (1.0, 1.0, 1.0), "Mines_Machine_Whim_Wheel_Pole15_764", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3926.8398, 4251.3306, 1409.9991), (1.5881105761771402e-13, -135.00012978593264, 5.000002108676757e-06), (1.0, 1.0, 1.0), "Mines_Machine_Whim_Wheel_Pole16_857", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4255.647, 3922.524, 1409.9991), (2.522485677033075e-13, -135.00009406569842, -179.99995901885455), (1.0, 1.0, 1.0), "Mines_Machine_Whim_Wheel_Pole17_858", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4455.8223, 4163.951, 1381.9991), (0.0, 44.999875563225665, -0.0), (1.0, 1.0, 1.0), "Mines_Machine_Whim_Wheel_Pole18_860", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1950.571, 4175.671, 1381.9991), (0.0, -45.00002828938376, 0.0), (1.0, 1.0, 1.0), "Mines_Machine_Whim_Wheel_Pole3_172", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2235.5374, 4460.6284, 1381.9991), (0.0, 134.9997121099358, -0.0), (1.0, 1.0, 1.0), "Mines_Machine_Whim_Wheel_Pole4_182", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4452.1147, 2232.7544, 1381.9991), (0.0, 134.99998245732414, -0.0), (1.0, 1.0, 1.0), "Mines_Machine_Whim_Wheel_Pole5_642", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4167.1475, 1947.7974, 1381.9991), (0.0, -45.000301640182265, 0.0), (1.0, 1.0, 1.0), "Mines_Machine_Whim_Wheel_Pole6_647", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2231.4797, 1943.8416, 1381.9991), (0.0, 44.99978357678187, -0.0), (1.0, 1.0, 1.0), "Mines_Machine_Whim_Wheel_Pole7", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1946.5239, 2228.8083, 1381.9991), (0.0, -135.0002528803546, 0.0), (1.0, 1.0, 1.0), "Mines_Machine_Whim_Wheel_Pole8_767", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4170.8667, 4448.917, 1381.9991), (0.0, -135.00012978593256, 0.0), (1.0, 1.0, 1.0), "Mines_Machine_Whim_Wheel_Pole9_859", _folder)
if a: placed += 1
else: skipped += 1

# Batch 83: StaticMesh'Mines_Machine_Whim_Wheel_Pole_B' (99 instances)
_mesh_path = "/Game/Art/Assets/Kits/Deco/Mines/Machine/Mines_Machine_Whim_Pieces/Mines_Machine_Whim_Wheel_Pole_B"
_materials = ['/Game/Art/Assets/Kits/Deco/Mines/Materials/Mines_Machine_Whim/MI_Mines_Machine_Whim_Trim', '/Game/Art/Assets/Kits/Deco/Mines/Materials/Mines_Machine_Whim/MI_Mines_Machine_Whim_Uniq']
_folder = "Reconstruction/BD_BB_Chapter2_Orctown_Throne/Meshes"
a = spawn_static_mesh(_mesh_path, _materials, (2609.4453, 4119.9824, 1026.9984), (0.0, 135.0000447640938, -0.0), (1.0, 1.0, 1.0), "Mines_Machine_Whim_Wheel_Pole_B_238", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3677.313, 2404.3235, 1191.9984), (0.0, -44.99994040916364, 0.0), (1.0, 1.0, 1.0), "Mines_Machine_Whim_Wheel_Pole_B10_658", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4285.917, 2404.3774, 1365.8949), (3.3059857870615113e-07, 44.999996968203995, -29.999813875057317), (1.0, 1.0, 1.0), "Mines_Machine_Whim_Wheel_Pole_B100", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4234.2983, 2455.996, 1323.8948), (4.1469667350861494e-05, 44.99997791340434, -89.99951908600137), (1.0, 1.0, 1.0), "Mines_Machine_Whim_Wheel_Pole_B101", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4182.416, 2507.8787, 1366.9795), (4.198122704702286e-05, 44.99998550346082, -149.9993402950578), (1.0, 1.0, 1.0), "Mines_Machine_Whim_Wheel_Pole_B102", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4285.912, 3996.7036, 1365.8947), (5.401280927092659e-06, 134.99999827813858, -29.999818763249053), (1.0, 1.0, 1.0), "Mines_Machine_Whim_Wheel_Pole_B103", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4234.294, 3945.0852, 1323.8945), (4.105481755320531e-05, 135.000016810888, -89.99948075294226), (1.0, 1.0, 1.0), "Mines_Machine_Whim_Wheel_Pole_B104", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4182.4106, 3893.203, 1366.9792), (4.1583171183980475e-05, 135.0000167164475, -149.99929286709005), (1.0, 1.0, 1.0), "Mines_Machine_Whim_Wheel_Pole_B105", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3999.53, 4283.083, 1365.8947), (5.401280927092659e-06, 134.99999827813858, -29.999818763249053), (1.0, 1.0, 1.0), "Mines_Machine_Whim_Wheel_Pole_B106", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3947.9111, 4231.465, 1323.8945), (4.105481755320531e-05, 135.000016810888, -89.99948075294226), (1.0, 1.0, 1.0), "Mines_Machine_Whim_Wheel_Pole_B107", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3896.0283, 4179.5825, 1366.9792), (4.1583171183980475e-05, 135.0000167164475, -149.99929286709005), (1.0, 1.0, 1.0), "Mines_Machine_Whim_Wheel_Pole_B108", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2407.205, 4293.0786, 1365.8947), (6.848817922094532e-06, -134.99997596908375, -29.999816386910254), (1.0, 1.0, 1.0), "Mines_Machine_Whim_Wheel_Pole_B109", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3871.7695, 2605.8506, 1191.9984), (0.0, -44.99994040916364, 0.0), (1.0, 1.0, 1.0), "Mines_Machine_Whim_Wheel_Pole_B11_659", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2458.8237, 4241.46, 1323.8945), (4.559254840213029e-05, -135.00000083954706, -89.99942367228518), (1.0, 1.0, 1.0), "Mines_Machine_Whim_Wheel_Pole_B110", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2510.707, 4189.577, 1366.9792), (4.084266185440651e-05, -134.99998033864648, -149.99929851198996), (1.0, 1.0, 1.0), "Mines_Machine_Whim_Wheel_Pole_B111", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2120.8254, 4006.6956, 1365.8947), (6.848817922094532e-06, -134.99997596908375, -29.999816386910254), (1.0, 1.0, 1.0), "Mines_Machine_Whim_Wheel_Pole_B112", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2172.4446, 3955.0762, 1323.8945), (4.559254840213029e-05, -135.00000083954706, -89.99942367228518), (1.0, 1.0, 1.0), "Mines_Machine_Whim_Wheel_Pole_B113", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2224.3264, 3903.1934, 1366.9792), (4.084266185440651e-05, -134.99998033864648, -149.99929851198996), (1.0, 1.0, 1.0), "Mines_Machine_Whim_Wheel_Pole_B114", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2115.8298, 2394.371, 1365.8947), (6.579383968669164e-06, -44.99978627023952, -29.999813065372443), (1.0, 1.0, 1.0), "Mines_Machine_Whim_Wheel_Pole_B115", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2167.4497, 2445.9888, 1323.8945), (4.1719859571852795e-05, -44.99984756812332, -89.99935275345743), (1.0, 1.0, 1.0), "Mines_Machine_Whim_Wheel_Pole_B116", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2219.3315, 2497.8735, 1366.9792), (4.155056364440012e-05, -44.999916563773255, -149.99929834287602), (1.0, 1.0, 1.0), "Mines_Machine_Whim_Wheel_Pole_B117", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2402.2139, 2107.991, 1365.8947), (6.579383968669164e-06, -44.99978627023952, -29.999813065372443), (1.0, 1.0, 1.0), "Mines_Machine_Whim_Wheel_Pole_B118", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2453.8333, 2159.61, 1323.8945), (4.1719859571852795e-05, -44.99984756812332, -89.99935275345743), (1.0, 1.0, 1.0), "Mines_Machine_Whim_Wheel_Pole_B119", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2786.0486, 3738.3604, 1857.9984), (0.0, 135.0000447640938, -0.0), (1.0, 1.0, 1.0), "Mines_Machine_Whim_Wheel_Pole_B12", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2505.7163, 2211.4924, 1366.9792), (4.155056364440012e-05, -44.999916563773255, -149.99929834287602), (1.0, 1.0, 1.0), "Mines_Machine_Whim_Wheel_Pole_B120", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2641.0918, 3883.3171, 1862.9984), (0.0, 135.0000447640938, -0.0), (1.0, 1.0, 1.0), "Mines_Machine_Whim_Wheel_Pole_B13", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2496.132, 3908.065, 1692.9984), (0.0, 135.0000447640938, -0.0), (1.0, 1.0, 1.0), "Mines_Machine_Whim_Wheel_Pole_B14", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2496.132, 3908.065, 1692.9984), (4.098112061513931e-05, 135.00003513884388, 179.99967898102517), (1.0, 1.0, 1.0), "Mines_Machine_Whim_Wheel_Pole_B15", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2124.1902, 4173.9404, 1299.9984), (0.0, 135.0000447640938, -0.0), (1.0, 1.0, 1.0), "Mines_Machine_Whim_Wheel_Pole_B16", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2239.448, 4289.199, 1299.9987), (4.098114288457847e-05, 135.00002679775045, -179.99980192459108), (1.0, 1.0, 1.0), "Mines_Machine_Whim_Wheel_Pole_B17", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2331.5518, 3842.0867, 1279.9984), (2.219216572449639e-05, 135.00004201471114, 89.99996723138109), (1.0, 1.0, 1.0), "Mines_Machine_Whim_Wheel_Pole_B18", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2369.0293, 3879.5652, 1279.9984), (2.219216572449639e-05, 135.00004201471114, 89.99996723138109), (1.0, 1.0, 1.0), "Mines_Machine_Whim_Wheel_Pole_B19", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2411.4531, 3921.988, 1026.9984), (0.0, 135.0000447640938, -0.0), (1.0, 1.0, 1.0), "Mines_Machine_Whim_Wheel_Pole_B2", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2530.2505, 4040.787, 1279.9984), (2.219216572449639e-05, 135.00004201471114, 89.99996723138109), (1.0, 1.0, 1.0), "Mines_Machine_Whim_Wheel_Pole_B20", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2567.021, 4077.5557, 1279.9984), (2.219216572449639e-05, 135.00004201471114, 89.99996723138109), (1.0, 1.0, 1.0), "Mines_Machine_Whim_Wheel_Pole_B21", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2014.5933, 4234.041, 1301.9984), (2.219216572449639e-05, 135.00004201471114, 89.99996723138109), (1.0, 1.0, 1.0), "Mines_Machine_Whim_Wheel_Pole_B22", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2212.5874, 4432.0312, 1301.9984), (2.219216572449639e-05, 135.00004201471114, 89.99996723138109), (1.0, 1.0, 1.0), "Mines_Machine_Whim_Wheel_Pole_B23", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2176.5198, 4395.9673, 1301.9985), (2.219216572449639e-05, 135.00004201471114, 89.99996723138109), (1.0, 1.0, 1.0), "Mines_Machine_Whim_Wheel_Pole_B24", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1977.8276, 4197.2744, 1301.9985), (2.219216572449639e-05, 135.00004201471114, 89.99996723138109), (1.0, 1.0, 1.0), "Mines_Machine_Whim_Wheel_Pole_B25", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3616.6357, 2670.0652, 1857.9984), (0.0, -44.99994040916364, 0.0), (1.0, 1.0, 1.0), "Mines_Machine_Whim_Wheel_Pole_B26_660", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3761.5925, 2525.1084, 1862.9984), (0.0, -44.99994040916364, 0.0), (1.0, 1.0, 1.0), "Mines_Machine_Whim_Wheel_Pole_B27_661", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3906.5522, 2500.3604, 1692.9984), (0.0, -44.99994040916364, 0.0), (1.0, 1.0, 1.0), "Mines_Machine_Whim_Wheel_Pole_B28_662", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3906.5522, 2500.3604, 1692.9984), (4.100000423591928e-05, -44.99990531331002, 179.9996789810786), (1.0, 1.0, 1.0), "Mines_Machine_Whim_Wheel_Pole_B29_663", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4278.495, 2234.485, 1299.9984), (0.0, -44.99994040916364, 0.0), (1.0, 1.0, 1.0), "Mines_Machine_Whim_Wheel_Pole_B30_664", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4163.2373, 2119.2258, 1299.9987), (4.1000009778722605e-05, -45.00001135042945, -179.9998019245787), (1.0, 1.0, 1.0), "Mines_Machine_Whim_Wheel_Pole_B31_665", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4134.575, 2502.8333, 1294.8987), (2.531505097014244e-05, -44.99987652782594, 89.99996054185942), (1.0, 1.0, 1.0), "Mines_Machine_Whim_Wheel_Pole_B32_666", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4097.1016, 2465.3547, 1294.8987), (2.531505097014244e-05, -44.99987652782594, 89.99996054185942), (1.0, 1.0, 1.0), "Mines_Machine_Whim_Wheel_Pole_B33_667", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3935.8833, 2304.133, 1294.8987), (2.531505097014244e-05, -44.99987652782594, 89.99996054185942), (1.0, 1.0, 1.0), "Mines_Machine_Whim_Wheel_Pole_B34_668", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3899.113, 2267.3647, 1294.8987), (2.531505097014244e-05, -44.99987652782594, 89.99996054185942), (1.0, 1.0, 1.0), "Mines_Machine_Whim_Wheel_Pole_B35_669", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4388.093, 2174.384, 1301.9984), (2.531505097014244e-05, -44.99987652782594, 89.99996054185942), (1.0, 1.0, 1.0), "Mines_Machine_Whim_Wheel_Pole_B36_670", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4190.098, 1976.3939, 1301.9984), (2.531505097014244e-05, -44.99987652782594, 89.99996054185942), (1.0, 1.0, 1.0), "Mines_Machine_Whim_Wheel_Pole_B37_671", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4226.166, 2012.4584, 1301.9985), (2.531505097014244e-05, -44.99987652782594, 89.99996054185942), (1.0, 1.0, 1.0), "Mines_Machine_Whim_Wheel_Pole_B38_672", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4424.859, 2211.1511, 1301.9985), (2.531505097014244e-05, -44.99987652782594, 89.99996054185942), (1.0, 1.0, 1.0), "Mines_Machine_Whim_Wheel_Pole_B39_673", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2286.2283, 2601.8176, 1026.9984), (0.0, -134.99998245732414, 0.0), (1.0, 1.0, 1.0), "Mines_Machine_Whim_Wheel_Pole_B40", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2484.2207, 2403.8245, 1026.9984), (0.0, -134.99998245732414, 0.0), (1.0, 1.0, 1.0), "Mines_Machine_Whim_Wheel_Pole_B41", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2399.3652, 2714.9546, 1191.9984), (0.0, -134.99998245732414, 0.0), (1.0, 1.0, 1.0), "Mines_Machine_Whim_Wheel_Pole_B42", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2600.893, 2520.4985, 1191.9984), (0.0, -134.99998245732414, 0.0), (1.0, 1.0, 1.0), "Mines_Machine_Whim_Wheel_Pole_B43", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2668.7922, 2779.3196, 1857.9984), (0.0, -134.99998245732414, 0.0), (1.0, 1.0, 1.0), "Mines_Machine_Whim_Wheel_Pole_B44", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2523.8357, 2634.3628, 1862.9984), (0.0, -134.99998245732414, 0.0), (1.0, 1.0, 1.0), "Mines_Machine_Whim_Wheel_Pole_B45", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2499.0876, 2489.403, 1692.9984), (0.0, -134.99998245732414, 0.0), (1.0, 1.0, 1.0), "Mines_Machine_Whim_Wheel_Pole_B46", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2499.0876, 2489.403, 1692.9984), (4.099998764722302e-05, -134.99977258766546, 179.99967898100817), (1.0, 1.0, 1.0), "Mines_Machine_Whim_Wheel_Pole_B47", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2233.2114, 2117.4602, 1299.9984), (0.0, -134.99998245732414, 0.0), (1.0, 1.0, 1.0), "Mines_Machine_Whim_Wheel_Pole_B48", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2117.9524, 2232.7178, 1299.9987), (4.100001249205625e-05, -135.00030832130054, -179.99980192458844), (1.0, 1.0, 1.0), "Mines_Machine_Whim_Wheel_Pole_B49", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2501.4785, 2261.2761, 1294.0654), (4.178971785055687e-05, -134.99989921763566, 89.9999456169479), (1.0, 1.0, 1.0), "Mines_Machine_Whim_Wheel_Pole_B50", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2463.9995, 2298.754, 1294.0654), (4.178971785055687e-05, -134.99989921763566, 89.9999456169479), (1.0, 1.0, 1.0), "Mines_Machine_Whim_Wheel_Pole_B51", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2303.814, 2461.0066, 1294.1832), (4.178971785055687e-05, -134.99989921763566, 89.9999456169479), (1.0, 1.0, 1.0), "Mines_Machine_Whim_Wheel_Pole_B52", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2267.0464, 2497.777, 1294.1832), (4.178971785055687e-05, -134.99989921763566, 89.9999456169479), (1.0, 1.0, 1.0), "Mines_Machine_Whim_Wheel_Pole_B53", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2173.1113, 2007.8625, 1301.9984), (4.178971785055687e-05, -134.99989921763566, 89.9999456169479), (1.0, 1.0, 1.0), "Mines_Machine_Whim_Wheel_Pole_B54", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1975.1204, 2205.8572, 1301.9984), (4.178971785055687e-05, -134.99989921763566, 89.9999456169479), (1.0, 1.0, 1.0), "Mines_Machine_Whim_Wheel_Pole_B55", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2011.1852, 2169.7898, 1301.9985), (4.178971785055687e-05, -134.99989921763566, 89.9999456169479), (1.0, 1.0, 1.0), "Mines_Machine_Whim_Wheel_Pole_B56", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2209.8774, 1971.0964, 1301.9985), (4.178971785055687e-05, -134.99989921763566, 89.9999456169479), (1.0, 1.0, 1.0), "Mines_Machine_Whim_Wheel_Pole_B57", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4113.0527, 3787.8835, 1026.9984), (0.0, 45.00002828938376, -0.0), (1.0, 1.0, 1.0), "Mines_Machine_Whim_Wheel_Pole_B58", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3915.0637, 3985.8772, 1026.9984), (0.0, 45.00002828938376, -0.0), (1.0, 1.0, 1.0), "Mines_Machine_Whim_Wheel_Pole_B59", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2722.5825, 4006.843, 1191.9984), (0.0, 135.0000447640938, -0.0), (1.0, 1.0, 1.0), "Mines_Machine_Whim_Wheel_Pole_B6", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3999.9192, 3674.7468, 1191.9984), (0.0, 45.00002828938376, -0.0), (1.0, 1.0, 1.0), "Mines_Machine_Whim_Wheel_Pole_B60", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3798.3914, 3869.203, 1191.9984), (0.0, 45.00002828938376, -0.0), (1.0, 1.0, 1.0), "Mines_Machine_Whim_Wheel_Pole_B61", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3733.5527, 3613.4407, 1857.9984), (0.0, 45.00002828938376, -0.0), (1.0, 1.0, 1.0), "Mines_Machine_Whim_Wheel_Pole_B62", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3878.509, 3758.3977, 1862.9984), (0.0, 45.00002828938376, -0.0), (1.0, 1.0, 1.0), "Mines_Machine_Whim_Wheel_Pole_B63", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3903.2576, 3903.357, 1692.9984), (0.0, 45.00002828938376, -0.0), (1.0, 1.0, 1.0), "Mines_Machine_Whim_Wheel_Pole_B64", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3903.2576, 3903.357, 1692.9984), (4.0999994057137696e-05, 45.00011629830068, 179.99967898104958), (1.0, 1.0, 1.0), "Mines_Machine_Whim_Wheel_Pole_B65", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4169.135, 4275.299, 1299.9984), (0.0, 45.00002828938376, -0.0), (1.0, 1.0, 1.0), "Mines_Machine_Whim_Wheel_Pole_B66", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4284.3936, 4160.042, 1299.9987), (4.100000992551233e-05, 44.999888117193144, -179.99980192456798), (1.0, 1.0, 1.0), "Mines_Machine_Whim_Wheel_Pole_B67", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3900.8113, 4131.4287, 1296.0546), (4.628136426552198e-05, 45.000125475952956, 89.99995926062769), (1.0, 1.0, 1.0), "Mines_Machine_Whim_Wheel_Pole_B68", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3938.2913, 4093.9507, 1296.0546), (4.628136426552198e-05, 45.000125475952956, 89.99995926062769), (1.0, 1.0, 1.0), "Mines_Machine_Whim_Wheel_Pole_B69", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2528.126, 3805.316, 1191.9984), (0.0, 135.0000447640938, -0.0), (1.0, 1.0, 1.0), "Mines_Machine_Whim_Wheel_Pole_B7", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4099.5107, 3932.7285, 1296.0546), (4.628136426552198e-05, 45.000125475952956, 89.99995926062769), (1.0, 1.0, 1.0), "Mines_Machine_Whim_Wheel_Pole_B70", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4136.278, 3895.9583, 1296.0546), (4.628136426552198e-05, 45.000125475952956, 89.99995926062769), (1.0, 1.0, 1.0), "Mines_Machine_Whim_Wheel_Pole_B71", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4229.2354, 4384.897, 1301.9984), (4.628136426552198e-05, 45.000125475952956, 89.99995926062769), (1.0, 1.0, 1.0), "Mines_Machine_Whim_Wheel_Pole_B72", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4427.2266, 4186.902, 1301.9984), (4.628136426552198e-05, 45.000125475952956, 89.99995926062769), (1.0, 1.0, 1.0), "Mines_Machine_Whim_Wheel_Pole_B73", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4391.162, 4222.9697, 1301.9985), (4.628136426552198e-05, 45.000125475952956, 89.99995926062769), (1.0, 1.0, 1.0), "Mines_Machine_Whim_Wheel_Pole_B74", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4192.469, 4421.6626, 1301.9985), (4.628136426552198e-05, 45.000125475952956, 89.99995926062769), (1.0, 1.0, 1.0), "Mines_Machine_Whim_Wheel_Pole_B75", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3790.4507, 2291.1865, 1026.9984), (0.0, -44.99994040916364, 0.0), (1.0, 1.0, 1.0), "Mines_Machine_Whim_Wheel_Pole_B8_656", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2738.0598, 2165.2861, 1226.9991), (0.0, -109.68752248089828, 0.0), (1.0, 1.0, 1.0), "Mines_Machine_Whim_Wheel_Pole_B81", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3988.443, 2489.1787, 1026.9984), (0.0, -44.99994040916364, 0.0), (1.0, 1.0, 1.0), "Mines_Machine_Whim_Wheel_Pole_B9_657", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4286.257, 3538.392, 1226.9991), (0.0, 22.499877299615083, -0.0), (1.0, 1.0, 1.0), "Mines_Machine_Whim_Wheel_Pole_B90", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3728.7515, 4206.571, 1226.9991), (0.0, 67.49996866527295, -0.0), (1.0, 1.0, 1.0), "Mines_Machine_Whim_Wheel_Pole_B93_893", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3999.5366, 2117.9968, 1365.8949), (3.3059857870615113e-07, 44.999996968203995, -29.999813875057317), (1.0, 1.0, 1.0), "Mines_Machine_Whim_Wheel_Pole_B97_176", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3947.918, 2169.6155, 1323.8948), (4.1469667350861494e-05, 44.99997791340434, -89.99951908600137), (1.0, 1.0, 1.0), "Mines_Machine_Whim_Wheel_Pole_B98", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3896.0354, 2221.498, 1366.9795), (4.198122704702286e-05, 44.99998550346082, -149.9993402950578), (1.0, 1.0, 1.0), "Mines_Machine_Whim_Wheel_Pole_B99", _folder)
if a: placed += 1
else: skipped += 1

# Batch 84: StaticMesh'Mines_Machine_Whim_Wheel_Support_A' (8 instances)
_mesh_path = "/Game/Art/Assets/Kits/Deco/Mines/Machine/Mines_Machine_Whim_Pieces/Mines_Machine_Whim_Wheel_Support_A"
_materials = ['/Game/Art/Assets/Kits/Deco/Mines/Materials/Mines_Machine_Whim/MI_Mines_Machine_Whim_Uniq']
_folder = "Reconstruction/BD_BB_Chapter2_Orctown_Throne/Meshes"
a = spawn_static_mesh(_mesh_path, _materials, (1984.2391, 4208.6914, 1361.9991), (0.0, 134.99985910618437, -0.0), (1.0, 1.0, 1.0), "Mines_Machine_Whim_Wheel_Support_A_168", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2202.0283, 4426.4795, 1361.9991), (0.0, -45.000301640182265, 0.0), (1.0, 1.0, 1.0), "Mines_Machine_Whim_Wheel_Support_A2", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4418.4463, 2199.7341, 1361.9991), (0.0, -45.00018401011068, 0.0), (1.0, 1.0, 1.0), "Mines_Machine_Whim_Wheel_Support_A3_641", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4200.657, 1981.9462, 1361.9991), (0.0, 134.9996538784942, -0.0), (1.0, 1.0, 1.0), "Mines_Machine_Whim_Wheel_Support_A4_646", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2198.4607, 1977.5088, 1361.9991), (0.0, -135.00017684175396, 0.0), (1.0, 1.0, 1.0), "Mines_Machine_Whim_Wheel_Support_A5", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1980.6721, 2195.2986, 1361.9991), (0.0, 44.99944966903147, -0.0), (1.0, 1.0, 1.0), "Mines_Machine_Whim_Wheel_Support_A6", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4203.8857, 4415.2505, 1361.9991), (0.0, 44.99975506748688, -0.0), (1.0, 1.0, 1.0), "Mines_Machine_Whim_Wheel_Support_A7", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4421.675, 4197.461, 1361.9991), (0.0, -135.00036410367022, 0.0), (1.0, 1.0, 1.0), "Mines_Machine_Whim_Wheel_Support_A8", _folder)
if a: placed += 1
else: skipped += 1

# Batch 85: StaticMesh'Mines_Lift_CentralPlatform_A' (1 instances)
_mesh_path = "/Game/Art/Assets/Kits/Deco/Mines/ThrownRoom_Lift/Mines_Lift_CentralPlatform_A"
_materials = ['/Game/Art/Assets/Kits/Deco/Mines/Machine/Mines_Machine_Lift_Pieces/Materials/Mi_Mines_Machine_Lift_A']
_folder = "Reconstruction/BD_BB_Chapter2_Orctown_Throne/Meshes"
a = spawn_static_mesh(_mesh_path, _materials, (3200.0, 3200.0, 800.0), (0.0, -44.99994040916364, 0.0), (1.0, 1.0, 1.0), "Mines_Lift_CentralPlatform_A_2", _folder)
if a: placed += 1
else: skipped += 1

# Batch 86: StaticMesh'Mines_Lift_OuterRingPath_A_Single_Mines_Lift_OuterRingPath_A_Single' (24 instances)
_mesh_path = "/Game/Art/Assets/Kits/Deco/Mines/ThrownRoom_Lift/Mines_Lift_OuterRingPath_A_Single_Mines_Lift_OuterRingPath_A_Single"
_materials = ['/Game/Art/Assets/Kits/Deco/Mines/Machine/Mines_Machine_Lift_Pieces/Materials/Mi_Mines_Machine_Lift_C']
_folder = "Reconstruction/BD_BB_Chapter2_Orctown_Throne/Meshes"
a = spawn_static_mesh(_mesh_path, _materials, (3200.0, 3200.0, 800.0), (0.0, -179.99981558486024, 0.0), (1.0, 1.0, 1.0), "Mines_Lift_OuterRingPath_A_Single_Mines_Lift_OuterRingPath_A_Single_2", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3199.9648, 3199.9648, 3600.0), (-0.00030517576439925177, 45.00109336729052, -179.99976777354357), (1.0, 1.0, 7.90625), "Mines_Lift_OuterRingPath_A_Single_Mines_Lift_OuterRingPath_A_Single10", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3199.9648, 3199.9648, 3600.0), (-0.00024414061043763623, 0.0006103515421226013, 179.99939211316817), (1.0, 1.0, 7.90625), "Mines_Lift_OuterRingPath_A_Single_Mines_Lift_OuterRingPath_A_Single11", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3199.9648, 3199.9648, 3600.0), (0.00021856602198420586, -44.99916960447802, 179.99997950942824), (1.0, 1.0, 7.90625), "Mines_Lift_OuterRingPath_A_Single_Mines_Lift_OuterRingPath_A_Single12", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3199.9648, 3199.9648, 3600.0), (0.00011611321160356229, -89.99859316254077, 179.99976777353984), (1.0, 1.0, 7.90625), "Mines_Lift_OuterRingPath_A_Single_Mines_Lift_OuterRingPath_A_Single13", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3199.9648, 3199.9648, 3600.0), (0.001298188948416541, -134.9987931267096, -179.9988320373544), (1.0, 1.0, 7.90625), "Mines_Lift_OuterRingPath_A_Single_Mines_Lift_OuterRingPath_A_Single14", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3199.9648, 3199.9648, 3600.0), (0.00016392450170644467, -179.99950822626488, -179.99950822620758), (1.0, 1.0, 7.90625), "Mines_Lift_OuterRingPath_A_Single_Mines_Lift_OuterRingPath_A_Single15", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3199.9648, 3199.9648, 3600.0), (4.09810986931436e-05, 135.0006625419386, -179.99868860325162), (1.0, 1.0, 7.90625), "Mines_Lift_OuterRingPath_A_Single_Mines_Lift_OuterRingPath_A_Single16", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3200.0, 3200.0, 1152.9395), (0.0, -179.99981558486024, 0.0), (1.34375, 1.34375, 1.0), "Mines_Lift_OuterRingPath_A_Single_Mines_Lift_OuterRingPath_A_Single17", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3200.0, 3200.0, 1152.9395), (0.0, -134.9997166015419, 0.0), (1.34375, 1.34375, 1.0), "Mines_Lift_OuterRingPath_A_Single_Mines_Lift_OuterRingPath_A_Single18", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3200.0, 3200.0, 1152.9395), (0.0, -89.99959790717821, 0.0), (1.34375, 1.34375, 1.0), "Mines_Lift_OuterRingPath_A_Single_Mines_Lift_OuterRingPath_A_Single19", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3200.0, 3200.0, 800.0), (0.0, -134.9997166015419, 0.0), (1.0, 1.0, 1.0), "Mines_Lift_OuterRingPath_A_Single_Mines_Lift_OuterRingPath_A_Single2", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3200.0, 3200.0, 1152.9395), (0.0, -44.99954028651891, 0.0), (1.34375, 1.34375, 1.0), "Mines_Lift_OuterRingPath_A_Single_Mines_Lift_OuterRingPath_A_Single20", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3200.0, 3200.0, 1152.9395), (0.0, 0.0005187988105841447, -0.0), (1.34375, 1.34375, 1.0), "Mines_Lift_OuterRingPath_A_Single_Mines_Lift_OuterRingPath_A_Single21", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3200.0, 3200.0, 1152.9395), (0.0, 45.00057896932595, -0.0), (1.34375, 1.34375, 1.0), "Mines_Lift_OuterRingPath_A_Single_Mines_Lift_OuterRingPath_A_Single22", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3200.0, 3200.0, 1152.9395), (0.0, 90.00060266115494, -0.0), (1.34375, 1.34375, 1.0), "Mines_Lift_OuterRingPath_A_Single_Mines_Lift_OuterRingPath_A_Single23", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3200.0, 3200.0, 1152.9395), (0.0, 135.00066622588886, -0.0), (1.34375, 1.34375, 1.0), "Mines_Lift_OuterRingPath_A_Single_Mines_Lift_OuterRingPath_A_Single24", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3200.0, 3200.0, 800.0), (0.0, -89.99959790717821, 0.0), (1.0, 1.0, 1.0), "Mines_Lift_OuterRingPath_A_Single_Mines_Lift_OuterRingPath_A_Single3", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3200.0, 3200.0, 800.0), (0.0, -44.99954028651891, 0.0), (1.0, 1.0, 1.0), "Mines_Lift_OuterRingPath_A_Single_Mines_Lift_OuterRingPath_A_Single4", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3200.0, 3200.0, 800.0), (0.0, 0.0005187988105841447, -0.0), (1.0, 1.0, 1.0), "Mines_Lift_OuterRingPath_A_Single_Mines_Lift_OuterRingPath_A_Single5", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3200.0, 3200.0, 800.0), (0.0, 45.00057896932595, -0.0), (1.0, 1.0, 1.0), "Mines_Lift_OuterRingPath_A_Single_Mines_Lift_OuterRingPath_A_Single6", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3200.0, 3200.0, 800.0), (0.0, 90.00060266115494, -0.0), (1.0, 1.0, 1.0), "Mines_Lift_OuterRingPath_A_Single_Mines_Lift_OuterRingPath_A_Single7", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3200.0, 3200.0, 800.0), (0.0, 135.00066622588886, -0.0), (1.0, 1.0, 1.0), "Mines_Lift_OuterRingPath_A_Single_Mines_Lift_OuterRingPath_A_Single8", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3199.9648, 3199.9648, 3600.0), (-0.00045776361373625537, 90.00144537120731, -179.99833343366967), (1.0, 1.0, 7.90625), "Mines_Lift_OuterRingPath_A_Single_Mines_Lift_OuterRingPath_A_Single9", _folder)
if a: placed += 1
else: skipped += 1

# Batch 87: StaticMesh'Mines_Lift_OuterRingRamp_A_Single' (4 instances)
_mesh_path = "/Game/Art/Assets/Kits/Deco/Mines/ThrownRoom_Lift/Mines_Lift_OuterRingRamp_A_Single"
_materials = ['/Game/Art/Assets/Kits/Deco/Mines/Machine/Mines_Machine_Lift_Pieces/Materials/Mi_Mines_Machine_Lift_C', '/Game/Art/Assets/Kits/Deco/Mines/Machine/Mines_Machine_Lift_Pieces/Materials/Mi_Mines_Machine_Lift_A']
_folder = "Reconstruction/BD_BB_Chapter2_Orctown_Throne/Meshes"
a = spawn_static_mesh(_mesh_path, _materials, (3200.0, 3200.0, 800.0), (0.0, 1.335144069428335e-05, -0.0), (1.0, 1.0, 1.0), "Mines_Lift_OuterRingRamp_A_Single2", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3200.0, 3200.0, 800.0), (0.0, -86.50012086985444, 0.0), (1.0, 1.0, 1.0), "Mines_Lift_OuterRingRamp_A_Single3", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3200.0, 3200.0, 800.0), (0.0, -179.99998633961752, -0.0), (1.0, 1.0, 1.0), "Mines_Lift_OuterRingRamp_A_Single4", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3200.0, 3200.0, 800.0), (0.0, 90.0000030488508, -0.0), (1.0, 1.0, 1.0), "Mines_Lift_OuterRingRamp_A_Single5", _folder)
if a: placed += 1
else: skipped += 1

# Batch 88: StaticMesh'Mines_Lift_OuterRingWall_A_Single' (8 instances)
_mesh_path = "/Game/Art/Assets/Kits/Deco/Mines/ThrownRoom_Lift/Mines_Lift_OuterRingWall_A_Single"
_materials = ['/Game/Art/Assets/Kits/Deco/Mines/Machine/Mines_Machine_Lift_Pieces/Materials/Mi_Mines_Machine_Lift_F']
_folder = "Reconstruction/BD_BB_Chapter2_Orctown_Throne/Meshes"
a = spawn_static_mesh(_mesh_path, _materials, (3200.0, 3200.0, 800.0), (0.0, 90.00007597449323, -0.0), (1.0, 1.0, 1.0), "Mines_Lift_OuterRingWall_A_Single_15", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3200.0, 3200.0, 800.0), (0.0, 44.99998273463503, -0.0), (1.0, 1.0, 1.0), "Mines_Lift_OuterRingWall_A_Single2", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3200.0, 3200.0, 800.0), (0.0, -9.155273700792082e-05, 0.0), (1.0, 1.0, 1.0), "Mines_Lift_OuterRingWall_A_Single3", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3200.0, 3200.0, 800.0), (0.0, -45.000120586048595, 0.0), (1.0, 1.0, 1.0), "Mines_Lift_OuterRingWall_A_Single4", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3200.0, 3200.0, 800.0), (0.0, -90.00018131163026, 0.0), (1.0, 1.0, 1.0), "Mines_Lift_OuterRingWall_A_Single5", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3200.0, 3200.0, 800.0), (0.0, -135.00014775251523, 0.0), (1.0, 1.0, 1.0), "Mines_Lift_OuterRingWall_A_Single6", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3200.0, 3200.0, 800.0), (0.0, 179.99967898105174, -0.0), (1.0, 1.0, 1.0), "Mines_Lift_OuterRingWall_A_Single7", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3200.0, 3200.0, 800.0), (0.0, 134.99970312672568, -0.0), (1.0, 1.0, 1.0), "Mines_Lift_OuterRingWall_A_Single8", _folder)
if a: placed += 1
else: skipped += 1

# Batch 89: StaticMesh'SM_Metal_Hanging_Chain_long' (4 instances)
_mesh_path = "/Game/Art/Assets/Kits/Deco/Mines/ThrownRoom_Lift/SM_Metal_Hanging_Chain_long"
_materials = ['/Game/Unshippable/ThirdParty/Medieval_Props/Medieval_Props_Vol4/Materials/MI_Medieval_Camp_Atlas_01']
_folder = "Reconstruction/BD_BB_Chapter2_Orctown_Throne/Meshes"
a = spawn_static_mesh(_mesh_path, _materials, (2591.7056, 2571.2944, 1504.3098), (0.0, -44.99999866815529, 0.0), (1.0, 1.0, 1.0), "SM_Metal_Hanging_Chain_long_301", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3812.3945, 3819.829, 1504.3098), (0.0, 135.00000119449854, -0.0), (1.0, 1.0, 1.0), "SM_Metal_Hanging_Chain_long2", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2577.174, 3817.1284, 1503.5763), (0.0, -134.99997422266742, 0.0), (1.0, 1.0, 1.0), "SM_Metal_Hanging_Chain_long3", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3825.4504, 2592.4812, 1504.3098), (0.0, 45.00000277446678, -0.0), (1.0, 1.0, 1.0), "SM_Metal_Hanging_Chain_long4", _folder)
if a: placed += 1
else: skipped += 1

# Batch 90: StaticMesh'Mines_Scaffolding_Arch_B' (32 instances)
_mesh_path = "/Game/Art/Assets/Kits/Deco_Architecture/Mines/Mines_Scaffolding_Arch_B"
_materials = ['/Game/Art/Assets/Kits/Deco_Architecture/Mines/Materials/Mines_Scaffolding/MI_Mines_Scaffolding_A_Mat']
_folder = "Reconstruction/BD_BB_Chapter2_Orctown_Throne/Meshes"
a = spawn_static_mesh(_mesh_path, _materials, (2061.0688, 4227.025, 1625.3807), (0.0, -134.3076768224725, 0.0), (1.0, 1.0, 1.0), "Mines_Scaffolding_Arch_B_243", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4341.3047, 4232.9717, 1638.8636), (0.553586737905036, 135.69780112936112, 0.5534197680696191), (1.0, 1.0, 1.0), "Mines_Scaffolding_Arch_B10", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4233.602, 4337.709, 1667.8375), (-6.104004349971144e-05, -44.30123422218009, 179.44651336319347), (1.0, 1.0, 1.0), "Mines_Scaffolding_Arch_B11", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4342.1157, 4231.8057, 1666.535), (0.040325473527086556, -44.30455496522057, 179.44650657025463), (1.0, 1.0, 1.0), "Mines_Scaffolding_Arch_B12", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4227.725, 4296.781, 1740.8168), (0.553586737905036, 135.69780112936112, 0.5534197680696191), (1.0, 1.0, 1.0), "Mines_Scaffolding_Arch_B13", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4228.481, 4295.665, 1768.3263), (-6.104004349971144e-05, -44.30123422218009, 179.44651336319347), (1.0, 1.0, 1.0), "Mines_Scaffolding_Arch_B14", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4303.9727, 4222.365, 1740.8165), (0.553586737905036, 135.69780112936112, 0.5534197680696191), (1.0, 1.0, 1.0), "Mines_Scaffolding_Arch_B15", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4304.729, 4221.2495, 1768.326), (-6.104004349971144e-05, -44.30123422218009, 179.44651336319347), (1.0, 1.0, 1.0), "Mines_Scaffolding_Arch_B16", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2167.2856, 2054.7898, 1611.1237), (0.5533408722685267, -44.311885609540525, -0.5536498560739442), (1.0, 1.0, 1.0), "Mines_Scaffolding_Arch_B17", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2059.2393, 2161.064, 1609.6655), (0.5533408722685267, -44.311885609540525, -0.5536498560739442), (1.0, 1.0, 1.0), "Mines_Scaffolding_Arch_B18", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2166.1584, 2055.5247, 1638.6334), (6.828956194362703e-05, 135.6969360878458, -179.44650655986658), (1.0, 1.0, 1.0), "Mines_Scaffolding_Arch_B19", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2166.936, 4335.48, 1625.3807), (0.0, -134.3076768224725, 0.0), (1.0, 1.0, 1.0), "Mines_Scaffolding_Arch_B2", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2058.0552, 2161.8477, 1637.337), (0.040537188668401246, 135.694409565474, -179.4464929834958), (1.0, 1.0, 1.0), "Mines_Scaffolding_Arch_B20", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2171.0464, 2095.4387, 1712.2443), (0.5533408722685267, -44.311885609540525, -0.5536498560739442), (1.0, 1.0, 1.0), "Mines_Scaffolding_Arch_B21", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2175.6252, 2102.0232, 1739.8325), (6.828956194362703e-05, 135.6969360878458, -179.44650655986658), (1.0, 1.0, 1.0), "Mines_Scaffolding_Arch_B22", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2100.377, 2164.4075, 1712.3164), (0.5533408722685267, -44.311885609540525, -0.5536498560739442), (1.0, 1.0, 1.0), "Mines_Scaffolding_Arch_B23", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2104.672, 2170.7002, 1739.9011), (6.828956194362703e-05, 135.6969360878458, -179.44650655986658), (1.0, 1.0, 1.0), "Mines_Scaffolding_Arch_B24", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4326.802, 2178.1182, 1626.5955), (1.1069481813447168, 45.694282484448806, -0.0002135810952605884), (1.0, 1.0, 1.0), "Mines_Scaffolding_Arch_B25", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4221.16, 2069.8965, 1623.6743), (1.1069481813447168, 45.694282484448806, -0.0002135810952605884), (1.0, 1.0, 1.0), "Mines_Scaffolding_Arch_B26", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4325.691, 2176.9863, 1654.0925), (-0.5534972198665432, -134.3021914031872, -179.9998975489926), (1.0, 1.0, 1.0), "Mines_Scaffolding_Arch_B27", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4219.9985, 2068.7083, 1651.3323), (-0.5130004660685527, -134.30543055753085, -179.99989758221787), (1.0, 1.0, 1.0), "Mines_Scaffolding_Arch_B28", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4285.228, 2182.3208, 1727.1654), (1.1069481813447168, 45.694282484448806, -0.0002135810952605884), (1.0, 1.0, 1.0), "Mines_Scaffolding_Arch_B29", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2061.8083, 4227.7764, 1652.9031), (0.553502167272083, 45.69686702243719, 179.99992488187453), (1.0, 1.0, 1.0), "Mines_Scaffolding_Arch_B3", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4284.117, 2181.189, 1754.6622), (-0.5534972198665432, -134.3021914031872, -179.9998975489926), (1.0, 1.0, 1.0), "Mines_Scaffolding_Arch_B30", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4214.6543, 2112.4993, 1726.2776), (1.1069481813447168, 45.694282484448806, -0.0002135810952605884), (1.0, 1.0, 1.0), "Mines_Scaffolding_Arch_B31", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4213.528, 2111.3809, 1753.7744), (-0.5534972198665432, -134.3021914031872, -179.9998975489926), (1.0, 1.0, 1.0), "Mines_Scaffolding_Arch_B32", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2167.724, 4336.286, 1653.0657), (0.5939121040465628, 45.69402290758544, 179.99991117725364), (1.0, 1.0, 1.0), "Mines_Scaffolding_Arch_B4", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2101.7354, 4221.8853, 1726.4337), (0.0, -134.3076768224725, 0.0), (1.0, 1.0, 1.0), "Mines_Scaffolding_Arch_B5", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2102.4749, 4222.6367, 1753.956), (0.5535020483191728, 45.696867021964174, 179.99992486905884), (1.0, 1.0, 1.0), "Mines_Scaffolding_Arch_B6", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2176.1475, 4298.1304, 1727.4628), (0.0, -134.3076768224725, 0.0), (1.0, 1.0, 1.0), "Mines_Scaffolding_Arch_B7", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2176.887, 4298.882, 1754.9851), (0.5535020483191728, 45.696867021964174, 179.99992486905884), (1.0, 1.0, 1.0), "Mines_Scaffolding_Arch_B8", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4232.8457, 4338.824, 1640.3279), (0.553586737905036, 135.69780112936112, 0.5534197680696191), (1.0, 1.0, 1.0), "Mines_Scaffolding_Arch_B9", _folder)
if a: placed += 1
else: skipped += 1

# Batch 91: StaticMesh'Mines_Scaffolding_Beam_1M_C' (8 instances)
_mesh_path = "/Game/Art/Assets/Kits/Deco_Architecture/Mines/Mines_Scaffolding_Beam_1M_C"
_materials = ['/Game/Art/Assets/Kits/Deco_Architecture/Mines/Materials/Mines_Scaffolding/MI_Mines_Scaffolding_B_Mat']
_folder = "Reconstruction/BD_BB_Chapter2_Orctown_Throne/Meshes"
a = spawn_static_mesh(_mesh_path, _materials, (2215.3342, 3983.2634, 1274.9991), (-90.0, -12.056693856932949, -32.943112912044924), (1.0, 1.0, 1.0), "Mines_Scaffolding_Beam_1M_C34", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4187.3506, 2425.1614, 1274.9991), (-90.0, -8.701341049080268, 143.7018635084955), (1.0, 1.0, 1.0), "Mines_Scaffolding_Beam_1M_C35_602", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2423.8884, 2208.6047, 1274.9991), (-90.0, 4.289359224198993, 40.71100562611363), (1.0, 1.0, 1.0), "Mines_Scaffolding_Beam_1M_C36", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3978.4568, 4184.155, 1274.9991), (-90.0, -2.944690160260009, 227.94476605638087), (1.0, 1.0, 1.0), "Mines_Scaffolding_Beam_1M_C37", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2416.8582, 4184.79, 1274.9991), (-90.0, -12.056693856932949, -32.943112912044924), (1.0, 1.0, 1.0), "Mines_Scaffolding_Beam_1M_C72", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3985.8264, 2223.6353, 1274.9991), (-90.0, -8.701341049080268, 143.7018635084955), (1.0, 1.0, 1.0), "Mines_Scaffolding_Beam_1M_C73_603", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2222.362, 2410.1287, 1274.9991), (-90.0, 4.289359224198993, 40.71100562611363), (1.0, 1.0, 1.0), "Mines_Scaffolding_Beam_1M_C75", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4179.984, 3982.6304, 1274.9991), (-90.0, -2.944690160260009, 227.94476605638087), (1.0, 1.0, 1.0), "Mines_Scaffolding_Beam_1M_C76", _folder)
if a: placed += 1
else: skipped += 1

# Batch 92: StaticMesh'Mines_Scaffolding_Post_1M_A' (16 instances)
_mesh_path = "/Game/Art/Assets/Kits/Deco_Architecture/Mines/Mines_Scaffolding_Post_1M_A"
_materials = ['/Game/Art/Assets/Kits/Deco_Architecture/Mines/Materials/Mines_Scaffolding/MI_Mines_Scaffolding_B_Mat']
_folder = "Reconstruction/BD_BB_Chapter2_Orctown_Throne/Meshes"
a = spawn_static_mesh(_mesh_path, _materials, (3878.329, 3961.4539, 1666.8416), (0.0, 135.00000119449854, -0.0), (1.0, 1.0, 1.0), "Mines_Scaffolding_Post_1M_A_310", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2531.7412, 3799.7861, 1763.4642), (-46.24847165556675, -44.999575980568395, 89.99979347909694), (1.0, 1.0, 1.0), "Mines_Scaffolding_Post_1M_A142", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3870.943, 2608.6396, 1763.4642), (-46.24841607973704, 135.00053424990958, 89.99978275803926), (1.0, 1.0, 1.0), "Mines_Scaffolding_Post_1M_A143_594", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2607.367, 2525.0117, 1763.4642), (-46.2481613393628, 45.00042671299633, 89.99975335905022), (1.0, 1.0, 1.0), "Mines_Scaffolding_Post_1M_A144", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3794.9778, 3867.7485, 1763.4642), (-46.24798546636736, -134.999485053791, 89.99967979154835), (1.0, 1.0, 1.0), "Mines_Scaffolding_Post_1M_A145", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2522.974, 3808.5544, 1811.1226), (-46.24847165556675, -44.999575980568395, 89.99979347909694), (1.0, 1.0, 1.0), "Mines_Scaffolding_Post_1M_A155", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3879.7097, 2599.871, 1811.1226), (-46.24841607973704, 135.00053424990958, 89.99978275803926), (1.0, 1.0, 1.0), "Mines_Scaffolding_Post_1M_A156_633", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2598.5984, 2516.2454, 1811.1226), (-46.2481613393628, 45.00042671299633, 89.99975335905022), (1.0, 1.0, 1.0), "Mines_Scaffolding_Post_1M_A157", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3803.7463, 3876.5146, 1811.1226), (-46.24798546636736, -134.999485053791, 89.99967979154835), (1.0, 1.0, 1.0), "Mines_Scaffolding_Post_1M_A158", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3971.1548, 3868.5994, 1666.8416), (0.0, 135.00000119449854, -0.0), (1.0, 1.0, 1.0), "Mines_Scaffolding_Post_1M_A2", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2440.6921, 3876.2908, 1666.8416), (0.0, -134.99997422266742, 0.0), (1.0, 1.0, 1.0), "Mines_Scaffolding_Post_1M_A3", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2533.547, 3969.1165, 1666.8416), (0.0, -134.99997422266742, 0.0), (1.0, 1.0, 1.0), "Mines_Scaffolding_Post_1M_A4", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2526.331, 2428.6692, 1666.8416), (0.0, -44.99999866815529, 0.0), (1.0, 1.0, 1.0), "Mines_Scaffolding_Post_1M_A5", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2433.2576, 2521.7722, 1666.8416), (0.0, -44.99999866815529, 0.0), (1.0, 1.0, 1.0), "Mines_Scaffolding_Post_1M_A6", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3962.7727, 2524.237, 1666.8416), (0.0, 44.99999866815529, -0.0), (1.0, 1.0, 1.0), "Mines_Scaffolding_Post_1M_A7", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3868.046, 2429.537, 1666.8416), (0.0, 44.99999866815529, -0.0), (1.0, 1.0, 1.0), "Mines_Scaffolding_Post_1M_A8", _folder)
if a: placed += 1
else: skipped += 1

# Batch 93: StaticMesh'Mines_Scaffolding_Post_2M_A' (8 instances)
_mesh_path = "/Game/Art/Assets/Kits/Deco_Architecture/Mines/Mines_Scaffolding_Post_2M_A"
_materials = ['/Game/Art/Assets/Kits/Deco_Architecture/Mines/Materials/Mines_Scaffolding/MI_Mines_Scaffolding_B_Mat']
_folder = "Reconstruction/BD_BB_Chapter2_Orctown_Throne/Meshes"
a = spawn_static_mesh(_mesh_path, _materials, (2574.5977, 3933.7063, 1705.2086), (-46.24832812403024, -44.99951435867131, -89.99891290124998), (1.0, 1.0, 0.749385), "Mines_Scaffolding_Post_2M_A120", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2570.7476, 3930.487, 1761.3287), (-46.24832812403024, -44.99951435867131, -89.99891290124998), (1.0, 1.0, 0.749385), "Mines_Scaffolding_Post_2M_A121", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3828.087, 2474.7188, 1705.2086), (-46.24818868651199, 135.0003874887215, -89.99889537904335), (1.0, 1.0, 0.749385), "Mines_Scaffolding_Post_2M_A122_587", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3831.9365, 2477.938, 1761.3287), (-46.24818868651199, 135.0003874887215, -89.99889537904335), (1.0, 1.0, 0.749385), "Mines_Scaffolding_Post_2M_A123_630", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2473.4446, 2567.8687, 1705.2086), (-46.24807759642907, 45.00028060614404, -89.99878242267448), (1.0, 1.0, 0.749385), "Mines_Scaffolding_Post_2M_A124", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2476.6648, 2564.0183, 1761.3287), (-46.24807759642907, 45.00028060614404, -89.99878242267448), (1.0, 1.0, 0.749385), "Mines_Scaffolding_Post_2M_A125", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3928.9006, 3824.8916, 1705.2086), (-46.24795575999393, -134.9996987851687, -89.99862681757585), (1.0, 1.0, 0.749385), "Mines_Scaffolding_Post_2M_A126", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3925.6794, 3828.7417, 1761.3287), (-46.24795575999393, -134.9996987851687, -89.99862681757585), (1.0, 1.0, 0.749385), "Mines_Scaffolding_Post_2M_A127", _folder)
if a: placed += 1
else: skipped += 1

# Batch 94: StaticMesh'Mines_Scaffolding_Post_2M_B' (8 instances)
_mesh_path = "/Game/Art/Assets/Kits/Deco_Architecture/Mines/Mines_Scaffolding_Post_2M_B"
_materials = ['/Game/Art/Assets/Kits/Deco_Architecture/Mines/Materials/Mines_Scaffolding/MI_Mines_Scaffolding_C_Mat']
_folder = "Reconstruction/BD_BB_Chapter2_Orctown_Throne/Meshes"
a = spawn_static_mesh(_mesh_path, _materials, (2455.5227, 3953.7866, 1612.1288), (-51.24823462794345, -44.99932837819, 0.0001555278481336212), (1.0, 1.028021, 1.0), "Mines_Scaffolding_Post_2M_B102", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2459.714, 3942.5247, 1673.4647), (-51.24823462794345, -44.99932837819, 0.0001555278481336212), (1.0, 1.028021, 1.0), "Mines_Scaffolding_Post_2M_B103", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3947.1614, 2454.6384, 1612.1288), (-51.248161521653614, 135.00068602750343, 0.00017250542039190061), (1.0, 1.028021, 1.0), "Mines_Scaffolding_Post_2M_B104_588", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3942.9705, 2465.9004, 1673.4647), (-51.248161521653614, 135.00068602750343, 0.00017250542039190061), (1.0, 1.028021, 1.0), "Mines_Scaffolding_Post_2M_B105_631", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2453.3645, 2448.7937, 1612.1288), (-51.24802455625075, 45.0005210737189, 0.00018719800935506215), (1.0, 1.028021, 1.0), "Mines_Scaffolding_Post_2M_B106", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2464.6272, 2452.9854, 1673.4647), (-51.24802455625075, 45.0005210737189, 0.00018719800935506215), (1.0, 1.028021, 1.0), "Mines_Scaffolding_Post_2M_B107", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3948.9807, 3943.9666, 1612.1288), (-51.24786629270015, -134.9993350927797, 0.00021265097656547428), (1.0, 1.028021, 1.0), "Mines_Scaffolding_Post_2M_B108", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3937.7175, 3939.775, 1673.4647), (-51.24786629270015, -134.9993350927797, 0.00021265097656547428), (1.0, 1.028021, 1.0), "Mines_Scaffolding_Post_2M_B109", _folder)
if a: placed += 1
else: skipped += 1

# Batch 95: StaticMesh'Mines_Scaffolding_Post_3M_A' (28 instances)
_mesh_path = "/Game/Art/Assets/Kits/Deco_Architecture/Mines/Mines_Scaffolding_Post_3M_A"
_materials = ['/Game/Art/Assets/Kits/Deco_Architecture/Mines/Materials/Mines_Scaffolding/MI_Mines_Scaffolding_B_Mat']
_folder = "Reconstruction/BD_BB_Chapter2_Orctown_Throne/Meshes"
a = spawn_static_mesh(_mesh_path, _materials, (2485.1033, 4137.7554, 1508.7352), (-46.24847263614399, -44.9992942315965, -89.99920820878214), (1.0, 1.0, 1.018908), "Mines_Scaffolding_Post_3M_A194", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2420.7156, 4223.3584, 1469.9039), (-46.24899821528471, -44.99948169672535, -89.99954946849013), (1.0, 1.0, 1.178943), "Mines_Scaffolding_Post_3M_A195", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2121.2878, 4082.9656, 1269.9991), (90.0, -3.1122915949181196, -228.11194464664817), (1.0, 1.0, 1.0), "Mines_Scaffolding_Post_3M_A196", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1976.3324, 4227.926, 1284.9991), (90.0, 1.3119419256601068, 136.31221059334482), (1.0, 1.0, 1.0), "Mines_Scaffolding_Post_3M_A197", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3917.5808, 2270.6694, 1508.7352), (-46.248422428973164, 135.00068833149334, -89.99914905644299), (1.0, 1.0, 1.018908), "Mines_Scaffolding_Post_3M_A198_589", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3981.9688, 2185.0667, 1469.9039), (-46.24889758664676, 135.00055608623907, -89.99950214587524), (1.0, 1.0, 1.178943), "Mines_Scaffolding_Post_3M_A199_595", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4281.3975, 2325.4592, 1269.9991), (90.0, 35.794373252427555, -9.204823076992135), (1.0, 1.0, 1.0), "Mines_Scaffolding_Post_3M_A200_598", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4429.8896, 2176.9639, 1284.9991), (90.0, 144.3500067946052, 99.35074664296192), (1.0, 1.0, 1.0), "Mines_Scaffolding_Post_3M_A201_599", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2269.3967, 2478.3745, 1508.7352), (-46.24817190420578, 45.00040302783394, -89.99893808865173), (1.0, 1.0, 1.018908), "Mines_Scaffolding_Post_3M_A202", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2183.794, 2413.9866, 1469.9039), (-46.24872314472321, 45.00036720877116, -89.99938853067118), (1.0, 1.0, 1.178943), "Mines_Scaffolding_Post_3M_A203", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2324.1858, 2114.5574, 1269.9991), (90.0, 1.778237830662893, -313.2204151089691), (1.0, 1.0, 1.0), "Mines_Scaffolding_Post_3M_A204", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2175.6904, 1966.0659, 1284.9991), (90.0, -22.22255357338492, 22.77888560578205), (1.0, 1.0, 1.0), "Mines_Scaffolding_Post_3M_A205", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4132.948, 3914.385, 1508.7352), (-46.24801683799887, -134.99950570334505, -89.9988650413299), (1.0, 1.0, 1.018908), "Mines_Scaffolding_Post_3M_A206", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4218.552, 3978.7734, 1469.9039), (-46.248568855028445, -134.99957764797074, -89.99923466950995), (1.0, 1.0, 1.178943), "Mines_Scaffolding_Post_3M_A207", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4078.1597, 4278.202, 1269.9991), (90.0, -14.90457964801504, -149.90376500357624), (1.0, 1.0, 1.0), "Mines_Scaffolding_Post_3M_A208", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4226.6562, 4426.694, 1284.9991), (90.0, -6.912132976577161, -141.91120540284456), (1.0, 1.0, 1.0), "Mines_Scaffolding_Post_3M_A209", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2188.4631, 4015.791, 1269.9991), (90.0, -8.32065272166386, -233.32031811436664), (1.0, 1.0, 1.0), "Mines_Scaffolding_Post_3M_A293", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2047.0433, 4157.2153, 1284.9991), (90.0, -8.32065272166386, -233.32031811436664), (1.0, 1.0, 1.0), "Mines_Scaffolding_Post_3M_A294", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2493.7827, 4114.9316, 1589.5853), (-46.24847263614399, -44.9992942315965, -89.99920820878214), (1.0, 1.0, 1.018908), "Mines_Scaffolding_Post_3M_A295", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4214.2217, 2392.6345, 1269.9991), (90.0, 35.794373252427555, -9.204823076992135), (1.0, 1.0, 1.0), "Mines_Scaffolding_Post_3M_A296_600", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4352.106, 2254.7458, 1284.9991), (90.0, 35.794373252427555, -9.204823076992135), (1.0, 1.0, 1.0), "Mines_Scaffolding_Post_3M_A297_601", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3908.9016, 2293.4934, 1589.5853), (-46.248422428973164, 135.00068833149334, -89.99914905644299), (1.0, 1.0, 1.018908), "Mines_Scaffolding_Post_3M_A298_632", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2391.361, 2181.733, 1269.9991), (90.0, 1.778237830662893, -313.2204151089691), (1.0, 1.0, 1.0), "Mines_Scaffolding_Post_3M_A299", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2249.9368, 2040.313, 1284.9991), (90.0, 1.778237830662893, -313.2204151089691), (1.0, 1.0, 1.0), "Mines_Scaffolding_Post_3M_A300", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2292.2202, 2487.0537, 1589.5853), (-46.24817190420578, 45.00040302783394, -89.99893808865173), (1.0, 1.0, 1.018908), "Mines_Scaffolding_Post_3M_A301", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4010.9846, 4211.027, 1269.9991), (90.0, -14.90457964801504, -149.90376500357624), (1.0, 1.0, 1.0), "Mines_Scaffolding_Post_3M_A302", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4155.945, 4355.981, 1284.9991), (90.0, -14.90457964801504, -149.90376500357624), (1.0, 1.0, 1.0), "Mines_Scaffolding_Post_3M_A303", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4110.1255, 3905.7058, 1589.5853), (-46.24801683799887, -134.99950570334505, -89.9988650413299), (1.0, 1.0, 1.018908), "Mines_Scaffolding_Post_3M_A304", _folder)
if a: placed += 1
else: skipped += 1

# Batch 96: StaticMesh'Suburbs_RoofTile_Slope3_200x100x300_A' (1 instances)
_mesh_path = "/Game/Art/Assets/Kits/Deco_Architecture/Suburbs/Suburbs_RoofTile_Slope3_200x100x300_A"
_materials = ['/Game/Art/Assets/Kits/Deco_Architecture/Suburbs/Materials/Suburbs_RoofTiles/MI_Suburbs_RoofTiles', '/Game/Art/Assets/Kits/Architecture/Deep/Materials/Deep_WoodTrim/MI_Deep_WoodTrim']
_folder = "Reconstruction/BD_BB_Chapter2_Orctown_Throne/Meshes"
a = spawn_static_mesh(_mesh_path, _materials, (5899.08, 3211.9187, 2900.0), (0.0, -92.81236999532442, 0.0), (1.0, 1.0, 1.0), "BP_DM_Suburbs_RoofTile_Slope3_200x100x300_A_Breakable73_246", _folder)
if a: placed += 1
else: skipped += 1

# Batch 97: StaticMesh'Suburbs_RoofTile_Slope3_200x200x300_CornerAngle_B' (2 instances)
_mesh_path = "/Game/Art/Assets/Kits/Deco_Architecture/Suburbs/Suburbs_RoofTile_Slope3_200x200x300_CornerAngle_B"
_materials = ['/Game/Art/Assets/Kits/Deco_Architecture/Suburbs/Materials/Suburbs_RoofTiles/MI_Suburbs_RoofTiles', '/Game/Art/Assets/Kits/Architecture/Deep/Materials/Deep_WoodTrim/MI_Deep_WoodTrim']
_folder = "Reconstruction/BD_BB_Chapter2_Orctown_Throne/Meshes"
a = spawn_static_mesh(_mesh_path, _materials, (5891.72, 3062.0994, 2900.0), (0.0, -2.812347509298898, 0.0), (1.0, 1.0, 1.0), "BP_DM_Suburbs_RoofTile_Slope3_200x200x300_CornerAngle_B_Breakable76_209", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5906.44, 3361.7378, 2900.0), (0.0, -92.81236999532442, 0.0), (1.0, 1.0, 1.0), "BP_DM_Suburbs_RoofTile_Slope3_200x200x300_CornerAngle_B_Breakable77", _folder)
if a: placed += 1
else: skipped += 1

# Batch 98: StaticMesh'Dirt_Mound_D' (5 instances)
_mesh_path = "/Game/Art/Assets/Kits/Misc/Dirt_Mounds/Dirt_Mound_D"
_materials = ['/Game/Art/Assets/Kits/Misc/Dirt_Mounds/Materials/Sururbs_Dirt_DarkELQ_Inst']
_folder = "Reconstruction/BD_BB_Chapter2_Orctown_Throne/Meshes"
a = spawn_static_mesh(_mesh_path, _materials, (5344.7153, 4075.273, 801.0), (0.0, -160.00883366485834, 0.0), (1.0, 1.0, 1.0), "Dirt_Mound_D_40", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5563.2485, 3326.4556, 801.00073), (0.0, 5.946830541289924, -0.0), (1.0, 1.0, 0.7601635), "Dirt_Mound_D2", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (722.44305, 4862.1313, 778.08936), (-0.6563114276034706, 129.24941943137108, 34.07989640569116), (1.0, 1.0, 1.0), "Dirt_Mound_D3_84", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1923.0078, 5949.5786, 1394.5045), (2.0040585565075712e-14, -64.46777139689364, 2.137058456969018e-06), (1.0, 1.0, 0.55952746), "Dirt_Mound_D4_98", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4365.0923, 400.77026, 1053.6561), (3.3225872060477704, -67.27634543402596, 32.12704193685136), (1.0, 1.0, 1.0), "Dirt_Mound_D5_131", _folder)
if a: placed += 1
else: skipped += 1

# Batch 99: StaticMesh'Dirt_Mound_E' (1 instances)
_mesh_path = "/Game/Art/Assets/Kits/Misc/Dirt_Mounds/Dirt_Mound_E"
_materials = ['/Game/Art/Assets/Kits/Misc/Dirt_Mounds/Materials/Sururbs_Dirt_DarkELQ_Inst']
_folder = "Reconstruction/BD_BB_Chapter2_Orctown_Throne/Meshes"
a = spawn_static_mesh(_mesh_path, _materials, (1007.49146, 1042.6821, 1095.4673), (8.174437708903698, -124.30435345076206, -32.637819877185066), (1.0, 1.0, 1.0), "Dirt_Mound_E_107", _folder)
if a: placed += 1
else: skipped += 1

# Batch 100: StaticMesh'Dirt_Mound_F' (5 instances)
_mesh_path = "/Game/Art/Assets/Kits/Misc/Dirt_Mounds/Dirt_Mound_F"
_materials = ['/Game/Art/Assets/Kits/Misc/Dirt_Mounds/Materials/Sururbs_Dirt_DarkELQ_Inst']
_folder = "Reconstruction/BD_BB_Chapter2_Orctown_Throne/Meshes"
a = spawn_static_mesh(_mesh_path, _materials, (5290.2827, 2269.6614, 800.35034), (0.0, -24.726255867590417, 0.0), (1.0518413, 1.5954609, 0.76694405), "Dirt_Mound_F_49", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5973.541, 2068.4312, 1135.7576), (4.4305728124209365, -22.126282443904, -34.48949884562862), (1.0, 1.595461, 1.0), "Dirt_Mound_F2", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5973.3535, 1203.6868, 788.7709), (0.0, 56.76615304281853, -0.0), (1.4635632, 1.4928818, 1.1641148), "Dirt_Mound_F3_71", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5360.3037, 405.3974, 783.22595), (0.0, 107.76307987458534, -0.0), (1.463563, 1.7820998, 1.10748), "Dirt_Mound_F4", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5880.999, 604.5522, 788.7722), (0.0, 139.6357549342432, -0.0), (1.463563, 1.492882, 1.099854), "Dirt_Mound_F5", _folder)
if a: placed += 1
else: skipped += 1

# Batch 101: StaticMesh'Dirt_Mound_G' (6 instances)
_mesh_path = "/Game/Art/Assets/Kits/Misc/Dirt_Mounds/Dirt_Mound_G"
_materials = ['/Game/Art/Assets/Kits/Misc/Dirt_Mounds/Materials/Sururbs_Dirt_DarkELQ_Inst']
_folder = "Reconstruction/BD_BB_Chapter2_Orctown_Throne/Meshes"
a = spawn_static_mesh(_mesh_path, _materials, (5955.281, 5879.0483, 797.7865), (0.0, 37.557356958696786, -0.0), (1.0, 1.0, 1.0), "Dirt_Mound_G_11", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5890.5176, 4595.8916, 957.2612), (0.39731863925601946, 28.7340643911061, 34.67677860153225), (1.2388996, 1.0, 1.0), "Dirt_Mound_G2_26", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (6027.3193, 4343.0933, 1160.212), (2.787132697614225, 30.3899648740268, 34.723928267860536), (1.2389, 1.0, 1.0), "Dirt_Mound_G3", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4491.0386, 5765.54, 991.97644), (1.3151232679545262, 67.47944756666891, -33.89248136682204), (1.0, 1.0, 1.0), "Dirt_Mound_G4_63", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4139.2686, 5880.3706, 1232.7893), (4.954824661035945, 75.97561140972887, -32.77599723993614), (1.0, 1.0, 1.0), "Dirt_Mound_G5", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1284.3358, 5508.969, 1246.316), (-11.881042270888225, -44.74975707612039, -33.59173041541224), (1.0, 1.0, 0.25353903), "Dirt_Mound_G6_95", _folder)
if a: placed += 1
else: skipped += 1

# Batch 102: StaticMesh'Dirt_Mound_H' (24 instances)
_mesh_path = "/Game/Art/Assets/Kits/Misc/Dirt_Mounds/Dirt_Mound_H"
_materials = ['/Game/Art/Assets/Kits/Misc/Dirt_Mounds/Materials/Sururbs_Dirt_DarkELQ_Inst']
_folder = "Reconstruction/BD_BB_Chapter2_Orctown_Throne/Meshes"
a = spawn_static_mesh(_mesh_path, _materials, (3699.8875, 2604.0107, 914.43036), (0.0, 36.29553700988952, -0.0), (1.0, 0.3905522, 0.024085272), "Dirt_Mound_H_1268", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3705.495, 3801.0503, 914.43036), (0.0, 140.87080334557518, -0.0), (1.289842, 0.44114807, 0.04215113), "Dirt_Mound_H10", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3870.1577, 3601.0503, 914.43036), (0.0, 123.03460135773244, -0.0), (1.121239, 0.3519991, 0.073586516), "Dirt_Mound_H11", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3930.7146, 3477.503, 914.43036), (0.0, 123.03460135773244, -0.0), (1.289842, 0.520602, 0.124624), "Dirt_Mound_H12", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3987.097, 3438.5366, 914.43036), (0.0, 103.53447403963752, -0.0), (1.289842, 0.3578637, 0.124624), "Dirt_Mound_H13", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3942.27, 2879.5427, 914.43036), (0.0, 63.283573935047286, -0.0), (1.289842, 0.357864, 0.08136304), "Dirt_Mound_H14", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5793.2534, 6132.383, 794.9062), (0.0, 162.69727244902825, -0.0), (1.2116511, 1.1287091, 1.3305047), "Dirt_Mound_H15_5", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5188.789, 4456.306, 799.26373), (0.0, 103.89825345009551, -0.0), (1.0, 1.0, 1.0), "Dirt_Mound_H16_36", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5752.8657, 4955.388, 799.26373), (0.0, -173.55568065520694, 0.0), (0.9232024, 0.9175458, 1.0), "Dirt_Mound_H17", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1133.0311, 5408.3735, 1097.0), (0.0, 0.0, -0.0), (1.0, 1.0, 1.0), "Dirt_Mound_H18_91", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (881.6285, 5184.5635, 1100.0), (0.0, 0.0, -0.0), (1.0, 1.0, 1.0), "Dirt_Mound_H19", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3848.4915, 2739.4968, 914.43036), (0.0, 46.122433042762985, -0.0), (1.3052843, 0.46080154, 0.03897611), "Dirt_Mound_H2", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1322.982, 764.33057, 1380.9962), (-29.821041011381197, 100.28913711866412, 7.2503966478160855), (1.0, 1.0, 1.0), "Dirt_Mound_H20_110", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3478.9565, 868.09937, 1402.5), (0.0, -8.09988391721341, 0.0), (0.675516, 0.29366827, 0.675516), "Dirt_Mound_H22_124", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4222.725, 5269.7974, 803.9944), (0.0, 68.38932098130755, -0.0), (1.0, 1.3913751, 1.0), "Dirt_Mound_H23_181", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5079.7744, 2116.227, 792.0), (0.0, 45.00005168692799, -0.0), (2.9750972, 2.3599403, 0.47315124), "Dirt_Mound_H24_99", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5143.2466, 2683.1077, 792.0), (0.0, -144.99994323543976, 0.0), (2.975097, 2.35994, 0.38725793), "Dirt_Mound_H25", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2798.0928, 2537.2617, 914.43036), (0.0, -37.37863210593237, 0.0), (1.8019202, 0.51344264, 0.034393232), "Dirt_Mound_H3", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2581.5254, 2744.2437, 914.43036), (0.0, -55.372405762677616, 0.0), (1.289842, 0.520602, 0.0362722), "Dirt_Mound_H4", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2499.3376, 2802.3523, 914.43036), (0.0, -55.372405762677616, 0.0), (1.289842, 0.520602, 0.08337495), "Dirt_Mound_H5", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2546.7231, 3537.874, 914.43036), (0.0, 44.459527703831526, -0.0), (1.289842, 0.520602, 0.025296383), "Dirt_Mound_H6", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2685.6985, 3723.8682, 914.43036), (0.0, 29.32832462985391, -0.0), (1.289842, 0.5109173, 0.057170294), "Dirt_Mound_H7", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2861.892, 3889.1997, 914.43036), (0.0, -146.51493488487583, 0.0), (1.289842, 0.520602, 0.048193455), "Dirt_Mound_H8", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3530.6543, 3914.8982, 914.43036), (0.0, 140.87080334557518, -0.0), (1.289842, 0.520602, 0.037672784), "Dirt_Mound_H9", _folder)
if a: placed += 1
else: skipped += 1

# Batch 103: StaticMesh'Dirt_Mound_H' (1 instances)
_mesh_path = "/Game/Art/Assets/Kits/Misc/Dirt_Mounds/Dirt_Mound_H"
_materials = ['/Game/Art/Assets/Kits/Misc/Dirt_Mounds/Materials/Sururbs_Dirt_DarkELQ_Inst']
_folder = "Reconstruction/BD_BB_Chapter2_Orctown_Throne/Meshes"
a = spawn_static_mesh(_mesh_path, _materials, (2133.387, 1428.3843, 796.6008), (0.0, -154.44275277721067, 0.0), (0.73947394, 0.73947394, 0.3459501), "Dirt_Mound_H21_64", _folder)
if a: placed += 1
else: skipped += 1

# Batch 104: StaticMesh'Dirt_Mound_I' (46 instances)
_mesh_path = "/Game/Art/Assets/Kits/Misc/Dirt_Mounds/Dirt_Mound_I"
_materials = ['/Game/Art/Assets/Kits/Misc/Dirt_Mounds/Materials/Sururbs_Dirt_DarkELQ_Inst']
_folder = "Reconstruction/BD_BB_Chapter2_Orctown_Throne/Meshes"
a = spawn_static_mesh(_mesh_path, _materials, (5362.3237, 6029.1836, 776.4366), (-0.24920680719948846, 118.04882994770229, -4.2892453166050215), (0.775642, 1.0, 0.44457397), "Dirt_Mound_I_8", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1523.6666, 502.34848, 1393.5619), (0.0, 2.377821340716744, -0.0), (1.0, 1.0, 0.8216217), "Dirt_Mound_I10_114", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2087.0095, 293.3472, 1400.1705), (0.0, -51.05523404162594, 0.0), (1.0, 1.0, 0.4629546), "Dirt_Mound_I11", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5694.4795, 1623.8136, 762.6218), (0.0, 8.348579917086875, -0.0), (1.0, 1.0, 1.0702692), "Dirt_Mound_I12_134", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4207.2944, 1086.5751, 746.49713), (0.0, -58.42986931258427, 0.0), (1.0, 1.3927845, 1.070269), "Dirt_Mound_I13", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3747.1755, 958.79346, 794.455), (0.0, 115.97790744702375, -0.0), (1.4890776, 1.132501, 0.44274732), "Dirt_Mound_I14", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2681.4797, 912.9214, 794.4551), (0.0, -129.41605233752287, 0.0), (1.0, 1.132501, 0.284074), "Dirt_Mound_I15", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1937.4829, 1107.7048, 794.4551), (0.0, -151.86827317288768, 0.0), (1.0, 0.78389585, 0.284074), "Dirt_Mound_I16", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2420.687, 629.63586, 794.4551), (0.0, -16.18084638320386, 0.0), (0.72565967, 0.85816056, 0.284074), "Dirt_Mound_I17", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2032.6683, 639.48975, 794.4551), (0.0, -135.65115211651755, 0.0), (1.0, 0.783896, 0.284074), "Dirt_Mound_I18", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1769.2996, 1422.2681, 794.4551), (0.0, 71.34732472735767, -0.0), (1.0, 0.783896, 0.284074), "Dirt_Mound_I19", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5499.895, 2884.3362, 799.5788), (0.0, 0.0, -0.0), (0.63940245, 1.0709975, 0.46988577), "Dirt_Mound_I2_46", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1398.1561, 1872.7037, 794.4551), (0.0, 71.34732472735767, -0.0), (1.0, 0.783896, 0.33398932), "Dirt_Mound_I20", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2143.8997, 2101.3943, 794.4551), (0.0, 71.34732472735767, -0.0), (0.67576194, 0.61284494, 0.333989), "Dirt_Mound_I21", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4243.515, 2055.4316, 791.68066), (0.0, 71.34732472735767, -0.0), (0.66918474, 0.56274986, 0.333989), "Dirt_Mound_I22", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4396.628, 2193.137, 791.68066), (0.0, 104.42421378848123, -0.0), (0.669185, 0.56275, 0.333989), "Dirt_Mound_I23", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4333.0156, 4291.774, 791.68066), (0.0, 104.42421378848123, -0.0), (0.74557793, 0.63914293, 0.333989), "Dirt_Mound_I24", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2133.149, 4376.5923, 791.68066), (0.0, 104.42421378848123, -0.0), (0.745578, 0.639143, 0.333989), "Dirt_Mound_I25", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2025.2604, 4248.5444, 791.68066), (0.0, -122.9363975294783, 0.0), (0.745578, 0.639143, 0.333989), "Dirt_Mound_I26", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2084.3633, 2058.2524, 794.4551), (0.0, 71.34732472735767, -0.0), (0.675762, 0.612845, 0.333989), "Dirt_Mound_I27", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4925.0337, 458.8521, 792.3965), (0.0, -106.02765533268321, 0.0), (1.0, 1.0, 1.0), "Dirt_Mound_I3_76", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5223.49, 347.26746, 796.56354), (0.0, -106.02765533268321, 0.0), (0.6981723, 0.7993741, 0.73151755), "Dirt_Mound_I4", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2831.378, 2110.0737, 788.88574), (0.0, -111.60430843847703, 0.0), (1.109864, 1.003429, 0.333989), "Dirt_Mound_I43", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1325.0786, 4704.753, 806.16425), (0.0, 0.0, -0.0), (1.0, 1.0, 1.0), "Dirt_Mound_I45_170", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2502.2217, 5462.1167, 796.4421), (0.0, -36.41287229696785, 0.0), (1.0, 1.0, 1.0), "Dirt_Mound_I46", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3883.835, 5435.532, 796.5106), (0.0, -72.22775918497094, 0.0), (1.0, 1.0, 0.6270939), "Dirt_Mound_I47", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4449.203, 5138.761, 796.5106), (0.0, -87.08242399242508, 0.0), (0.5211206, 0.5211206, 0.3470148), "Dirt_Mound_I48", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4833.9604, 5703.3823, 796.5106), (0.0, -34.962705937605314, 0.0), (0.88160825, 0.88160825, 0.347015), "Dirt_Mound_I49", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (751.2621, 4842.032, 806.16425), (0.0, 0.0, -0.0), (1.0, 1.0, 1.0), "Dirt_Mound_I5_87", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (464.86694, 4243.338, 798.16425), (0.0, 0.0, -0.0), (1.0, 1.0, 1.0), "Dirt_Mound_I50", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2843.9062, 2142.0012, 812.1101), (0.0, 0.0, -0.0), (0.27648196, 0.21865365, 0.3184256), "Dirt_Mound_I51_360", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4264.9478, 3611.0024, 796.6176), (0.0, -7.636504630219337, 0.0), (0.491692, 0.218654, 0.339064), "Dirt_Mound_I54", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3645.075, 4243.0605, 796.6176), (0.0, -7.636504630219337, 0.0), (0.491692, 0.218654, 0.339064), "Dirt_Mound_I55", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2786.125, 4273.352, 796.6176), (0.0, -7.636504630219337, 0.0), (0.491692, 0.218654, 0.339064), "Dirt_Mound_I56", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2143.38, 3652.8384, 796.6176), (0.0, -7.636504630219337, 0.0), (0.491692, 0.218654, 0.339064), "Dirt_Mound_I57", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2141.674, 2781.7017, 796.6176), (0.0, -7.636504630219337, 0.0), (0.491692, 0.218654, 0.339064), "Dirt_Mound_I58", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2842.8872, 2380.8596, 788.88574), (0.0, -111.60430843847703, 0.0), (1.4660596, 1.003429, 1.0096374), "Dirt_Mound_I59", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (542.0062, 4532.9023, 803.16425), (0.0, 0.0, -0.0), (1.0, 1.0, 1.0), "Dirt_Mound_I6", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2615.0986, 2471.0674, 788.88574), (0.0, -111.60430843847703, 0.0), (1.46606, 1.003429, 1.009637), "Dirt_Mound_I60", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2358.7056, 2725.3308, 788.88574), (0.0, -111.60430843847703, 0.0), (1.46606, 1.003429, 0.8041399), "Dirt_Mound_I61", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3637.4814, 2488.883, 788.88574), (0.0, -111.60430843847703, 0.0), (1.46606, 1.003429, 1.009637), "Dirt_Mound_I62", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3855.3262, 2615.2654, 788.88574), (0.0, 48.39575155864973, -0.0), (1.46606, 1.003429, 0.7809957), "Dirt_Mound_I63", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3994.6785, 2773.7039, 788.88574), (0.0, 48.39575155864973, -0.0), (1.46606, 1.003429, 0.780996), "Dirt_Mound_I64", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3720.0625, 6039.4756, 1397.594), (0.0, 21.958256590271752, -0.0), (0.49478802, 0.49478802, 0.5865975), "Dirt_Mound_I7_102", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (692.5936, 1505.9967, 762.01886), (1.383252360674901e-05, 46.539705876681865, 5.69967317369269), (1.151879, 1.7188945, 1.0), "Dirt_Mound_I8", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (855.37305, 1146.9794, 936.733), (-1.3441169139280658, 49.18331098693011, 26.921821300808016), (1.151879, 1.0, 0.95579267), "Dirt_Mound_I9", _folder)
if a: placed += 1
else: skipped += 1

# Batch 105: StaticMesh'Dirt_Mound_I' (22 instances)
_mesh_path = "/Game/Art/Assets/Kits/Misc/Dirt_Mounds/Dirt_Mound_I"
_materials = ['/Game/Art/Assets/Kits/Misc/Dirt_Mounds/Materials/Sururbs_Dirt_DarkELQ_Inst']
_folder = "Reconstruction/BD_BB_Chapter2_Orctown_Throne/Meshes"
a = spawn_static_mesh(_mesh_path, _materials, (3624.9763, 2259.717, 791.68066), (0.0, 133.96289234893712, -0.0), (1.1098642, 1.0034293, 0.333989), "Dirt_Mound_I28", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3864.562, 2490.7825, 791.68066), (0.0, 133.96289234893712, -0.0), (1.109864, 1.003429, 0.333989), "Dirt_Mound_I29", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4167.717, 2871.4248, 791.68066), (0.0, 169.310791036706, -0.0), (1.109864, 1.003429, 0.333989), "Dirt_Mound_I30", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4235.555, 3409.89, 791.68066), (0.0, 169.310791036706, -0.0), (1.109864, 1.003429, 0.333989), "Dirt_Mound_I31", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4162.5103, 3634.8872, 791.68066), (0.0, -132.398428872585, 0.0), (1.109864, 1.003429, 0.333989), "Dirt_Mound_I32", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3869.3225, 3924.149, 791.68066), (0.0, -132.398428872585, 0.0), (1.109864, 1.003429, 0.333989), "Dirt_Mound_I33", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3745.6902, 4137.099, 788.88574), (0.0, -95.53051664176941, 0.0), (1.109864, 1.003429, 0.333989), "Dirt_Mound_I34", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3560.3164, 4247.8716, 788.88574), (0.0, -95.53051664176941, 0.0), (1.109864, 1.003429, 0.333989), "Dirt_Mound_I35", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2896.462, 4229.8066, 788.88574), (0.0, -72.53540012596805, 0.0), (1.109864, 1.003429, 0.333989), "Dirt_Mound_I36", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2528.0547, 4060.524, 788.88574), (0.0, -31.067203188199976, 0.0), (1.109864, 1.003429, 0.333989), "Dirt_Mound_I37", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2304.05, 3765.5686, 788.88574), (0.0, -31.067203188199976, 0.0), (1.109864, 1.003429, 0.333989), "Dirt_Mound_I38", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2189.9868, 3480.2168, 788.88574), (0.0, -31.067203188199976, 0.0), (1.109864, 1.003429, 0.333989), "Dirt_Mound_I39", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2160.7292, 2744.5894, 788.88574), (0.0, -133.57861071574428, 0.0), (1.109864, 1.003429, 0.333989), "Dirt_Mound_I40", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2343.6306, 2448.537, 788.88574), (0.0, -111.60430843847703, 0.0), (1.109864, 1.003429, 0.333989), "Dirt_Mound_I41", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2547.8088, 2282.182, 788.88574), (0.0, -111.60430843847703, 0.0), (1.109864, 1.003429, 0.333989), "Dirt_Mound_I42", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3143.53, 2138.2324, 788.88574), (0.0, -111.60430843847703, 0.0), (1.109864, 1.003429, 0.333989), "Dirt_Mound_I44", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3646.9346, 2124.192, 799.0008), (0.0, 11.415060793523281, -0.0), (0.49169195, 0.218654, 0.33906353), "Dirt_Mound_I52", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4269.0625, 2727.6023, 796.6176), (0.0, -7.636504630219337, 0.0), (0.491692, 0.218654, 0.339064), "Dirt_Mound_I53", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2489.5535, 3699.7031, 802.88574), (0.0, -111.60430843847703, 0.0), (1.109864, 1.003429, 0.60249144), "Dirt_Mound_I65", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2721.5344, 3960.9326, 802.88574), (0.0, -171.6042466111078, 0.0), (1.109864, 1.003429, 0.7710286), "Dirt_Mound_I66", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3737.8955, 4014.607, 788.88574), (0.0, -86.06725738674787, 0.0), (1.109864, 1.003429, 0.6918954), "Dirt_Mound_I67", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3978.195, 3741.4448, 788.88574), (0.0, -86.06725738674787, 0.0), (1.109864, 1.003429, 0.691895), "Dirt_Mound_I68", _folder)
if a: placed += 1
else: skipped += 1

# Batch 106: StaticMesh'Dirt_Mound_L' (1 instances)
_mesh_path = "/Game/Art/Assets/Kits/Misc/Dirt_Mounds/Dirt_Mound_L"
_materials = ['/Game/Art/Assets/Kits/Misc/Dirt_Mounds/Materials/Sururbs_Dirt_DarkELQ_Inst']
_folder = "Reconstruction/BD_BB_Chapter2_Orctown_Throne/Meshes"
a = spawn_static_mesh(_mesh_path, _materials, (6015.383, 5129.7173, 788.2189), (0.0, -33.26190072544705, 0.0), (1.0, 1.0, 0.57145375), "Dirt_Mound_L_14", _folder)
if a: placed += 1
else: skipped += 1

# Batch 107: StaticMesh'Orc_Fort_9X9_Mound' (18 instances)
_mesh_path = "/Game/Art/Assets/Kits/Misc/Dirt_Mounds/Orc_Fort_9X9_Mound"
_materials = ['/Game/Art/Assets/Kits/Misc/Dirt_Mounds/Materials/Sururbs_Dirt_DarkELQ_Inst']
_folder = "Reconstruction/BD_BB_Chapter2_Orctown_Throne/Meshes"
a = spawn_static_mesh(_mesh_path, _materials, (5328.0884, 4240.802, 984.6112), (-19.98007437278722, 10.86919623789232, 36.15490083289591), (1.0, 1.0, 1.0), "Orc_Fort_9X9_Mound_33", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1228.4711, 4467.502, 899.40063), (3.034950140100879, -50.53158277236034, -32.94915699593336), (1.0, 0.964654, 1.0), "Orc_Fort_9X9_Mound10", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1473.7719, 1737.3965, 969.276), (6.99208331285626, 42.405907419529285, 33.87072574924288), (1.0, 1.0, 1.0), "Orc_Fort_9X9_Mound11_118", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1690.1744, 1467.0117, 1200.2141), (6.072516108242783, 43.78068279851125, 34.02775914596801), (1.0, 1.0, 1.0), "Orc_Fort_9X9_Mound12", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2300.1223, 1060.7731, 1412.1276), (9.578998905053242, 69.90652249094438, 5.9182207280234655e-06), (1.0, 1.0, 1.0), "Orc_Fort_9X9_Mound13", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3102.8274, 900.18134, 1410.1855), (9.008971554115845, 89.94411582012626, 0.9264616815592674), (1.0, 1.0, 1.0), "Orc_Fort_9X9_Mound14", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4225.7744, 1126.7627, 983.38293), (1.9993123175149896, 109.25665412969741, -33.5856296221899), (1.0, 1.0, 1.0), "Orc_Fort_9X9_Mound15_127", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3518.0322, 5904.4077, 813.0403), (16.351696173838793, 16.21581548871054, 1.6354063553343448), (1.0, 1.0, 1.0), "Orc_Fort_9X9_Mound17_177", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2882.4824, 5888.181, 814.7166), (14.399965129590253, 172.9581796076036, 0.7145722478575867), (1.0, 1.0, 1.0), "Orc_Fort_9X9_Mound18", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1925.1201, 5027.637, 807.5), (0.0, 132.3824787808064, -0.0), (1.0, 1.0, 1.0), "Orc_Fort_9X9_Mound19_184", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5317.724, 2133.799, 972.9038), (-12.35604788796539, -17.860289710843514, -33.44726655377639), (1.0, 1.0, 1.0), "Orc_Fort_9X9_Mound2_53", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5453.922, 2406.536, 1182.688), (-10.8854062535246, -18.848266138446313, -33.68323085639079), (1.0, 1.0, 1.0), "Orc_Fort_9X9_Mound3", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5529.2437, 3167.5708, 1398.5), (0.0, 179.8595303187821, -0.0), (1.0, 1.0, 1.820503), "Orc_Fort_9X9_Mound4_60", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4134.57, 5314.653, 1098.1252), (6.632111828162895, -108.02801276162899, 34.35746867247554), (1.0, 1.0, 1.0), "Orc_Fort_9X9_Mound5_67", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3278.608, 5492.993, 1403.5511), (6.067079366629982, -88.64076054274867, -0.09219381312471883), (1.0, 1.0, 1.0), "Orc_Fort_9X9_Mound6", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2746.2783, 5480.271, 1402.6984), (6.067079366629982, -88.64076054274867, -0.09219381312471883), (1.0, 1.0, 1.0), "Orc_Fort_9X9_Mound7", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2272.7698, 5352.0376, 1397.4402), (4.670701574259088, -47.99506013465694, 1.939069318096208), (1.0, 1.0, 1.0), "Orc_Fort_9X9_Mound8", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1729.2402, 4901.196, 1210.3057), (3.034950140100879, -50.53158277236034, -32.94915699593336), (1.0, 0.9196074, 1.0), "Orc_Fort_9X9_Mound9", _folder)
if a: placed += 1
else: skipped += 1

# Batch 108: StaticMesh'Orc_Fort_9X9_Mound' (1 instances)
_mesh_path = "/Game/Art/Assets/Kits/Misc/Dirt_Mounds/Orc_Fort_9X9_Mound"
_materials = ['/Game/Art/Assets/Kits/Misc/Dirt_Mounds/Materials/Sururbs_Dirt_DarkELQ_Inst']
_folder = "Reconstruction/BD_BB_Chapter2_Orctown_Throne/Meshes"
a = spawn_static_mesh(_mesh_path, _materials, (3940.3027, 1005.6346, 1189.4883), (1.9993123175149896, 109.25665412969741, -33.5856296221899), (1.0, 1.0, 1.0), "Orc_Fort_9X9_Mound16", _folder)
if a: placed += 1
else: skipped += 1

# Batch 109: StaticMesh'Suburbs_Dirt_Mound_A' (6 instances)
_mesh_path = "/Game/Art/Assets/Kits/Misc/Dirt_Mounds/Suburbs_Dirt_Mound_A"
_materials = ['/Game/Art/Assets/Kits/Misc/Dirt_Mounds/Materials/Sururbs_Dirt_DarkELQ_Inst']
_folder = "Reconstruction/BD_BB_Chapter2_Orctown_Throne/Meshes"
a = spawn_static_mesh(_mesh_path, _materials, (3556.866, 2526.4346, 914.43036), (0.0, 31.786108338492713, -0.0), (1.0, 1.0, 0.06117078), "Suburbs_Dirt_Mound_A_1264", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3622.4353, 2567.0671, 914.43036), (0.0, -127.33220874368676, 0.0), (1.0, 1.0, 0.10707287), "Suburbs_Dirt_Mound_A2", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3507.9812, 2482.6758, 914.59717), (0.0, 31.786108338492713, -0.0), (1.1297314, 1.4679393, 0.099046245), "Suburbs_Dirt_Mound_A3", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2970.48, 2450.2605, 914.59717), (0.0, 31.786108338492713, -0.0), (1.129731, 1.467939, 0.08544057), "Suburbs_Dirt_Mound_A4", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3472.2903, 2455.0378, 914.59717), (0.0, 31.786108338492713, -0.0), (1.8192271, 1.2681642, 0.05445622), "Suburbs_Dirt_Mound_A5", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3066.377, 2424.6167, 914.59717), (0.0, -2.5932005819821, 0.0), (1.819227, 1.268164, 0.05665806), "Suburbs_Dirt_Mound_A6", _folder)
if a: placed += 1
else: skipped += 1

# Batch 110: StaticMesh'NonD_Boundary_Door_False_C' (1 instances)
_mesh_path = "/Game/Developers/wforl/NonD_Boundary_Door_False_C"
_materials = ['/Game/Art/Assets/Kits/Architecture/Suburbs/Destructable/Materials/MI_Suburbs_Wall_Non_Dest', '/Game/Art/Assets/Kits/Architecture/Suburbs/Materials/Suburbs_Trim_Sheet_A/MI_Suburbs_Trim_Sheet_A']
_folder = "Reconstruction/BD_BB_Chapter2_Orctown_Throne/Meshes"
a = spawn_static_mesh(_mesh_path, _materials, (6098.7188, 3197.199, 1500.0), (0.0, -2.8120729270716494, 0.0), (1.0, 1.0, 1.0), "NonD_Boundary_Door_False_C_5", _folder)
if a: placed += 1
else: skipped += 1

# Batch 111: StaticMesh'SM_AR_City_Column_050x100x200_A_Base' (2 instances)
_mesh_path = "/Game/Environments/Models/Architecture/Meshes/SM_AR_City_Column_050x100x200_A_Base"
_materials = ['/Game/Environments/Models/Architecture/Materials/MI_Column_GreyStone_A_MAT_Inst']
_folder = "Reconstruction/BD_BB_Chapter2_Orctown_Throne/Meshes"
a = spawn_static_mesh(_mesh_path, _materials, (6046.875, 2653.9983, 1600.0), (0.0, -92.81249294292995, 0.0), (1.0, 1.0, 1.0), "BP_Column_05x2m_A_Base29_8", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (6100.8584, 3752.666, 1600.0), (0.0, -92.81268539889938, 0.0), (1.0, 1.0, 1.0), "BP_Column_05x2m_A_Base34", _folder)
if a: placed += 1
else: skipped += 1

# Batch 112: StaticMesh'SM_AR_City_Column_050x100x200_A_Capital' (2 instances)
_mesh_path = "/Game/Environments/Models/Architecture/Meshes/SM_AR_City_Column_050x100x200_A_Capital"
_materials = ['/Game/Environments/Models/Architecture/Materials/MI_Column_GreyStone_A_MAT_Inst']
_folder = "Reconstruction/BD_BB_Chapter2_Orctown_Throne/Meshes"
a = spawn_static_mesh(_mesh_path, _materials, (6046.871, 2654.0083, 2400.0), (0.0, -92.81240335426158, 0.0), (1.0, 1.0, 1.0), "BP_Column_05x2m_A_Capital27_2", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (6100.8604, 3752.6619, 2400.0), (0.0, -92.81249294292995, 0.0), (1.0, 1.0, 1.0), "BP_Column_05x2m_A_Capital32", _folder)
if a: placed += 1
else: skipped += 1

# Batch 113: StaticMesh'SM_AR_City_Column_050x100x200_A_Shaft' (6 instances)
_mesh_path = "/Game/Environments/Models/Architecture/Meshes/SM_AR_City_Column_050x100x200_A_Shaft"
_materials = ['/Game/Environments/Models/Architecture/Materials/MI_Column_GreyStone_A_MAT_Inst']
_folder = "Reconstruction/BD_BB_Chapter2_Orctown_Throne/Meshes"
a = spawn_static_mesh(_mesh_path, _materials, (6046.871, 2654.0088, 2200.0), (0.0, -92.81236999532442, 0.0), (1.0, 1.0, 1.0), "BP_Column_05x2m_A_Shaft29_2", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (6046.871, 2654.0088, 2000.0), (0.0, -92.81236999532442, 0.0), (1.0, 1.0, 1.0), "BP_Column_05x2m_A_Shaft30", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (6046.8716, 2654.002, 1800.0), (0.0, -92.81236999532442, 0.0), (1.0, 1.0, 1.0), "BP_Column_05x2m_A_Shaft39", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (6100.861, 3752.6702, 2200.0), (0.0, -92.81225372777013, 0.0), (1.0, 1.0, 1.0), "BP_Column_05x2m_A_Shaft40_9", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (6100.861, 3752.6702, 2000.0), (0.0, -92.81225372777013, 0.0), (1.0, 1.0, 1.0), "BP_Column_05x2m_A_Shaft41", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (6100.861, 3752.6702, 1800.0), (0.0, -92.81225372777013, 0.0), (1.0, 1.0, 1.0), "BP_Column_05x2m_A_Shaft42", _folder)
if a: placed += 1
else: skipped += 1

# Batch 114: StaticMesh'SM_AR_Foundation_Stone_4x4x4m_A' (6 instances)
_mesh_path = "/Game/Environments/Models/Architecture/Meshes/SM_AR_Foundation_Stone_4x4x4m_A"
_materials = ['/Game/Art/Assets/Kits/Architecture/Suburbs/Destructable/Materials/MI_Suburbs_Foundation_Stone_Base']
_folder = "Reconstruction/BD_BB_Chapter2_Orctown_Throne/Meshes"
a = spawn_static_mesh(_mesh_path, _materials, (6298.598, 3192.2925, 2200.0), (0.0, 177.18761226169238, -0.0), (1.0, 1.0, 1.0), "BP_Foundation_Stone_4x4x4m_A2", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (6298.598, 3192.2925, 2600.0), (0.0, 177.18761226169238, -0.0), (1.0, 1.0, 1.0), "BP_Foundation_Stone_4x4x4m_A3", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (6278.972, 2792.7798, 2200.0), (0.0, 177.18761226169238, -0.0), (1.0, 1.0, 1.0), "BP_Foundation_Stone_4x4x4m_A5", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (6278.972, 2792.7798, 2600.0), (0.0, 177.18761226169238, -0.0), (1.0, 1.0, 1.0), "BP_Foundation_Stone_4x4x4m_A6", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (6318.2246, 3591.805, 2200.0), (0.0, 177.18761226169238, -0.0), (1.0, 1.0, 1.0), "BP_Foundation_Stone_4x4x4m_A8", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (6318.2246, 3591.805, 2600.0), (0.0, 177.18761226169238, -0.0), (1.0, 1.0, 1.0), "BP_Foundation_Stone_4x4x4m_A9", _folder)
if a: placed += 1
else: skipped += 1

# Batch 115: StaticMesh'SM_AR_Foundation_Stone_Rough_300x300x100_A' (15 instances)
_mesh_path = "/Game/Environments/Models/Architecture/Meshes/SM_AR_Foundation_Stone_Rough_300x300x100_A"
_materials = ['/Game/Environments/Materials/MI_ArchitectureBase_NonDestructible']
_folder = "Reconstruction/BD_BB_Chapter2_Orctown_Throne/Meshes"
a = spawn_static_mesh(_mesh_path, _materials, (3500.0, 5650.0, 1250.0), (0.0, 0.0, -0.0), (1.0, 1.0, 1.0), "SM_AR_Foundation_Stone_Rough_300x300x100_A_733", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3500.0, 750.0, 1250.0), (0.0, 0.0, -0.0), (1.0, 1.0, 1.0), "SM_AR_Foundation_Stone_Rough_300x300x100_A10", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3200.0, 750.0, 1250.0), (0.0, 0.0, -0.0), (1.0, 1.0, 1.0), "SM_AR_Foundation_Stone_Rough_300x300x100_A11", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2900.0, 750.0, 1250.0), (0.0, 0.0, -0.0), (1.0, 1.0, 1.0), "SM_AR_Foundation_Stone_Rough_300x300x100_A12", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3500.0, 450.0, 1250.0), (0.0, 0.0, -0.0), (1.0, 1.0, 1.0), "SM_AR_Foundation_Stone_Rough_300x300x100_A13", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3200.0, 450.0, 1250.0), (0.0, 0.0, -0.0), (1.0, 1.0, 1.0), "SM_AR_Foundation_Stone_Rough_300x300x100_A14", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2900.0, 450.0, 1250.0), (0.0, 0.0, -0.0), (1.0, 1.0, 1.0), "SM_AR_Foundation_Stone_Rough_300x300x100_A15", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3200.0, 5650.0, 1250.0), (0.0, 0.0, -0.0), (1.0, 1.0, 1.0), "SM_AR_Foundation_Stone_Rough_300x300x100_A2", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2900.0, 5650.0, 1250.0), (0.0, 0.0, -0.0), (1.0, 1.0, 1.0), "SM_AR_Foundation_Stone_Rough_300x300x100_A3", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3500.0, 5950.0, 1250.0), (0.0, 0.0, -0.0), (1.0, 1.0, 1.0), "SM_AR_Foundation_Stone_Rough_300x300x100_A4", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3200.0, 5950.0, 1250.0), (0.0, 0.0, -0.0), (1.0, 1.0, 1.0), "SM_AR_Foundation_Stone_Rough_300x300x100_A5", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2900.0, 5950.0, 1250.0), (0.0, 0.0, -0.0), (1.0, 1.0, 1.0), "SM_AR_Foundation_Stone_Rough_300x300x100_A6", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3500.0, 6250.0, 1250.0), (0.0, 0.0, -0.0), (1.0, 1.0, 1.0), "SM_AR_Foundation_Stone_Rough_300x300x100_A7", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3200.0, 6250.0, 1250.0), (0.0, 0.0, -0.0), (1.0, 1.0, 1.0), "SM_AR_Foundation_Stone_Rough_300x300x100_A8", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2900.0, 6250.0, 1250.0), (0.0, 0.0, -0.0), (1.0, 1.0, 1.0), "SM_AR_Foundation_Stone_Rough_300x300x100_A9", _folder)
if a: placed += 1
else: skipped += 1

# Batch 116: StaticMesh'SM_AR_Suburbs_Slope3_200x100x300_A' (2 instances)
_mesh_path = "/Game/Environments/Models/Architecture/Meshes/SM_AR_Suburbs_Slope3_200x100x300_A"
_materials = ['/Game/Environments/Models/Architecture/Materials/MI_ArchSimple_Stone_Wall_E_MAT']
_folder = "Reconstruction/BD_BB_Chapter2_Orctown_Throne/Meshes"
a = spawn_static_mesh(_mesh_path, _materials, (5998.9595, 3207.012, 2600.0), (0.0, -92.81231995694225, 0.0), (1.0, 1.0, 1.0), "BP_Suburbs_Slope3_2x1x3m_A_2", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (6051.3525, 3254.4985, 2600.0), (0.0, 177.1873391493061, -0.0), (1.0, 1.0, 1.0), "BP_Suburbs_Slope3_2x1x3m_A3", _folder)
if a: placed += 1
else: skipped += 1

# Batch 117: StaticMesh'SM_AR_Suburbs_Slope3_200x200x300_CornerAngle_B' (2 instances)
_mesh_path = "/Game/Environments/Models/Architecture/Meshes/SM_AR_Suburbs_Slope3_200x200x300_CornerAngle_B"
_materials = ['/Game/Environments/Models/Architecture/Materials/MI_ArchSimple_Stone_Wall_E_MAT']
_folder = "Reconstruction/BD_BB_Chapter2_Orctown_Throne/Meshes"
a = spawn_static_mesh(_mesh_path, _materials, (6001.413, 3256.952, 2600.0), (0.0, -92.81231995694225, 0.0), (1.0, 1.0, 1.0), "BP_Suburbs_Slope3_2x2x3m_CornerAngle_B_2", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5996.5063, 3157.0723, 2600.0), (0.0, -2.812316885726422, 0.0), (1.0, 1.0, 1.0), "BP_Suburbs_Slope3_2x2x3m_CornerAngle_B2", _folder)
if a: placed += 1
else: skipped += 1

# Batch 118: StaticMesh'PWM_Quarry_1x1x1_A' (19 instances)
_mesh_path = "/Game/Unshippable/Whitebox/Rocks/Meshes/PWM_Quarry_1x1x1_A"
_materials = ['/Game/Environments/ProcTexturing/ProcMaterial_Quarry_Atlas_1']
_folder = "Reconstruction/BD_BB_Chapter2_Orctown_Throne/Meshes"
a = spawn_static_mesh(_mesh_path, _materials, (2830.0, 5510.0, 1250.0), (0.0, 0.0, -0.0), (1.0, 1.0, 1.0), "PWM_Quarry_1x1x1_A_426", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (6016.116, 4473.4287, 2572.6006), (0.6007356751404186, -74.61807411640892, -12.018277990392445), (1.0, 1.0, 1.0), "PWM_Quarry_1x1x1_A10_702", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (991.22345, 5381.431, 2568.2363), (4.038179913894195, -128.54234793497952, -78.85992368924876), (2.3760118, 1.7023169, 1.7023169), "PWM_Quarry_1x1x1_A11_761", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (370.84854, 3023.2712, 2471.5977), (-1.5266414603787855, 87.3356370716167, -7.049651465434426), (1.5714521, 1.0, 1.0), "PWM_Quarry_1x1x1_A12_773", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (589.69403, 1497.4609, 1551.1396), (-11.910643361612557, 2.1844322774947066e-07, 2.910866547264535), (1.0, 1.0, 2.100326), "PWM_Quarry_1x1x1_A13_776", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2918.6216, 4491.323, 2901.439), (0.0, 0.0, -0.0), (1.6744232, 1.6744232, 0.9052113), "PWM_Quarry_1x1x1_A14_876", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1367.7871, 731.59656, 2623.8682), (-3.5180363265650385, 131.21408827495057, 158.88999884311448), (1.9866968, 1.5637573, 1.6500632), "PWM_Quarry_1x1x1_A15_985", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (832.5305, 1325.272, 2568.866), (-13.273834836322187, -31.366127157205064, 24.679579399824064), (1.0, 1.0, 1.0), "PWM_Quarry_1x1x1_A16_997", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (780.1693, 1547.2362, 2662.0466), (39.11598063226187, -159.38776617670922, -22.520602517120413), (1.0, 1.0, 1.0), "PWM_Quarry_1x1x1_A17_1003", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4432.1323, 473.0438, 2554.5571), (0.0, 11.29382655450009, -0.0), (1.6910373, 1.0, 1.4892924), "PWM_Quarry_1x1x1_A18_1016", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (6084.055, 4191.595, 2580.2751), (0.0, 5.731550329628563, -0.0), (1.0, 2.2762735, 1.3797578), "PWM_Quarry_1x1x1_A19_1056", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2730.0, 5430.0, 1240.0), (0.0, -118.12490992083346, 0.0), (1.0, 1.0, 1.0), "PWM_Quarry_1x1x1_A2", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2750.0, 5500.0, 1120.0), (0.0, 146.25003133230928, -0.0), (1.0, 1.0, 1.0), "PWM_Quarry_1x1x1_A3", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1356.6665, 4572.472, 860.0), (0.0, 106.87516796582565, -0.0), (1.0, 1.0, 1.0), "PWM_Quarry_1x1x1_A4", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4194.4395, 3198.0159, 2860.0479), (-2.2308958994156796, -123.2113510029758, 4.1976646353741325), (1.5581205, 1.5581205, 0.4959775), "PWM_Quarry_1x1x1_A5_625", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4354.04, 3401.7405, 2868.4773), (-2.2308958994156796, -123.2113510029758, 4.1976646353741325), (1.5798314, 1.8365701, 0.86084604), "PWM_Quarry_1x1x1_A6", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (6293.0, 3694.0, 2070.0), (0.0, 0.0, -0.0), (1.0, 1.0, 1.6879894), "PWM_Quarry_1x1x1_A7_652", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (6337.0, 5501.0, 1640.0), (0.0, 0.0, -0.0), (1.0, 1.0, 1.0), "PWM_Quarry_1x1x1_A8_672", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4963.0, 5902.128, 1628.0916), (-9.11587456693674, 2.0038607806836115, -12.453764870654377), (1.0, 1.0, 2.00516), "PWM_Quarry_1x1x1_A9_679", _folder)
if a: placed += 1
else: skipped += 1

# Batch 119: StaticMesh'PWM_Quarry_1X1x1_C' (78 instances)
_mesh_path = "/Game/Unshippable/Whitebox/Rocks/Meshes/PWM_Quarry_1X1x1_C"
_materials = ['/Game/Environments/ProcTexturing/ProcMaterial_Quarry_Atlas_1']
_folder = "Reconstruction/BD_BB_Chapter2_Orctown_Throne/Meshes"
a = spawn_static_mesh(_mesh_path, _materials, (3685.3928, 6024.6055, 1418.0), (0.0, 120.00015926914853, -0.0), (1.0, 1.0, 1.0), "PWM_Quarry_1X1x1_C_147", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1976.4778, 836.76294, 800.0), (0.0, 0.0, -0.0), (1.0, 1.0, 1.0), "PWM_Quarry_1X1x1_C10_801", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2375.465, 632.0134, 800.0), (0.0, 0.0, -0.0), (1.0, 1.0, 1.0), "PWM_Quarry_1X1x1_C11", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2578.7935, 949.5949, 800.0), (0.0, 7.1362374576274465, -0.0), (1.0, 1.3079722, 1.0), "PWM_Quarry_1X1x1_C12", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2511.6997, 974.77747, 1211.2195), (0.0, 171.79418114241676, -0.0), (1.0, 1.0, 1.0), "PWM_Quarry_1X1x1_C13_806", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5083.0, 350.1963, 1661.565), (0.0, 0.0, -75.17369757890515), (1.458719, 1.458719, 1.458719), "PWM_Quarry_1X1x1_C14_505", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5128.0, 592.0, 1749.0), (0.0, 0.0, -0.0), (1.3268898, 1.3268898, 1.3268898), "PWM_Quarry_1X1x1_C15_527", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5338.327, 990.14923, 2501.0), (0.0, -33.58285143034338, 0.0), (0.8311992, 1.4377723, 1.4377723), "PWM_Quarry_1X1x1_C16_543", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5085.0, 1109.0, 2719.0), (-1.7841516135616102e-07, -110.9048388414186, 9.912828671147661), (1.6282096, 1.8292735, 0.53728276), "PWM_Quarry_1X1x1_C17_546", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (390.13928, 3217.853, 2465.2227), (-74.36447805389743, -45.20813509742427, 44.12813010692584), (1.0, 1.6295803, 1.0), "PWM_Quarry_1X1x1_C18_602", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (6010.0, 2572.0, 2596.0), (-29.439266049024877, 143.32831434368114, 1.700833430960866e-05), (0.39536005, 1.0, 1.3872867), "PWM_Quarry_1X1x1_C19_647", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3485.6577, 6067.4507, 1381.7625), (1.6654702731572307e-07, -139.99985785565454, -15.000058796122008), (1.0, 1.0, 1.0), "PWM_Quarry_1X1x1_C2", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (6082.711, 5972.817, 1670.0), (0.0, -56.349666544241444, 0.0), (1.7974926, 1.4578993, 1.0), "PWM_Quarry_1X1x1_C20_675", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5876.2266, 6176.532, 1670.0), (0.0, -31.929688047986897, 0.0), (1.797493, 1.457899, 1.0), "PWM_Quarry_1X1x1_C21", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (6225.717, 5460.1587, 800.0), (-1.431334169656176e-07, 74.15608629699578, -11.708037606320188), (2.4384212, 1.2723442, 1.2723442), "PWM_Quarry_1X1x1_C22_685", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (6132.0, 2972.0, 2659.0), (0.0, 0.0, -0.0), (1.0, 1.8552094, 1.0), "PWM_Quarry_1X1x1_C23_705", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5642.0, 2801.0, 2823.0), (0.0, 0.0, -0.0), (1.0, 1.0, 1.0), "PWM_Quarry_1X1x1_C24_708", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5432.441, 5548.239, 1765.0), (0.6852318304237817, -41.99127362111029, 0.026415609862115812), (2.0056863, 1.5222253, 1.0), "PWM_Quarry_1X1x1_C25_716", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5786.7295, 5138.4146, 1742.0979), (-9.191957209289127, -54.637396509575716, 2.079451555567459), (2.005686, 1.522225, 1.3349751), "PWM_Quarry_1X1x1_C26", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (507.57236, 4232.386, 2610.1006), (-1.0620643620361311e-06, 72.35487138064535, -14.105224501949282), (1.5517156, 1.5517156, 1.7292565), "PWM_Quarry_1X1x1_C27_727", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4429.0947, 5932.8413, 2643.8682), (-16.082245883039626, -8.923005557283293, -22.718016164085537), (1.7200309, 1.1507887, 1.9095913), "PWM_Quarry_1X1x1_C28_743", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1910.718, 5932.5615, 2569.2986), (4.914057369118267e-09, 17.97724539430151, -8.296996782658857), (1.0, 1.0, 1.205753), "PWM_Quarry_1X1x1_C29_754", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2434.3652, 5981.9585, 1364.0483), (-2.2696473988163821e-07, -29.999815752093326, -15.000610439820354), (1.0, 1.0, 1.0), "PWM_Quarry_1X1x1_C3", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1277.7821, 5581.3145, 2599.7427), (-1.0449217961567099, 37.65859652669734, -17.022977197219355), (2.1368835, 1.0, 2.062162), "PWM_Quarry_1X1x1_C30_764", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1068.2771, 5395.447, 2697.0), (0.0, -60.15726364892023, 0.0), (1.6635766, 2.322254, 1.9766055), "PWM_Quarry_1X1x1_C31_767", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1357.9817, 770.2872, 2579.1787), (0.0, -14.813568782535993, 0.0), (1.64153, 0.36153182, 1.0099689), "PWM_Quarry_1X1x1_C32_791", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1153.8535, 840.0467, 2578.884), (-1.6287534623554174, 155.63515812215635, -9.142362387134453), (1.0, 1.0, 1.0), "PWM_Quarry_1X1x1_C33_797", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1195.066, 871.3547, 2666.829), (-27.89886430499907, 41.0201516836015, 5.60599551390533), (1.0, 1.0, 1.0), "PWM_Quarry_1X1x1_C34", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4108.173, 401.87155, 2624.4988), (-32.040619341924575, 70.53180061074312, 8.161479714953265), (2.228203, 1.8190293, 1.8190293), "PWM_Quarry_1X1x1_C35_826", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4078.4136, 5331.7603, 2880.2793), (0.0, 0.0, -83.04769870145999), (1.7198858, 1.0951797, 1.7198858), "PWM_Quarry_1X1x1_C36_852", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (431.00848, 2220.1953, 2176.147), (0.0, 0.0, -0.0), (1.0, 1.0, 1.0), "PWM_Quarry_1X1x1_C37_929", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5736.3735, 4799.1377, 802.18567), (-1.79530160459455e-07, 78.90725495328374, 7.8350772178048125), (1.0, 1.0, 1.0), "PWM_Quarry_1X1x1_C38_947", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (6198.716, 3534.1602, 2599.1904), (8.204415755722097, 7.19777330860144, 1.6762763706993422e-07), (1.0, 1.6397867, 1.5701697), "PWM_Quarry_1X1x1_C39_950", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2965.3928, 6020.6055, 1385.4639), (0.0, -179.99981558486024, 0.0), (1.0, 1.0, 1.0), "PWM_Quarry_1X1x1_C4", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (948.5739, 5095.7773, 2651.3096), (-79.9773164017147, -29.54889686780508, 0.00011967104082680503), (1.1456664, 2.1031926, 1.1456664), "PWM_Quarry_1X1x1_C40_962", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1251.5826, 798.11316, 2559.2063), (0.0, -15.259828239915526, 0.0), (2.1934788, 1.0, 1.0), "PWM_Quarry_1X1x1_C41_1010", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4379.314, 501.6543, 2637.301), (0.0, 0.0, 22.267980149632237), (1.7899541, 1.0, 1.2057832), "PWM_Quarry_1X1x1_C42_1019", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4890.9585, 662.9565, 2545.448), (6.243828066636241, 25.505148762633066, 25.94581803937763), (2.191481, 1.0, 1.0), "PWM_Quarry_1X1x1_C43_1028", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5947.476, 1966.9271, 2548.0808), (0.0, 0.0, -0.0), (1.0, 1.6499797, 1.2101533), "PWM_Quarry_1X1x1_C44_1031", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (6008.8857, 2234.3381, 2546.2334), (75.95519828327714, 12.669415600974704, 12.302349880285856), (1.0, 2.449162, 1.210153), "PWM_Quarry_1X1x1_C45", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (6080.2773, 2576.9634, 2515.8296), (0.0, 0.0, -0.0), (1.0, 1.0, 1.0), "PWM_Quarry_1X1x1_C46_1035", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5701.9976, 1411.1726, 2518.4338), (0.0, 0.0, -0.0), (1.0, 1.0, 1.0), "PWM_Quarry_1X1x1_C47_1038", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (6036.4863, 2927.6543, 2658.4429), (0.0, 0.0, -0.0), (1.0, 1.0, 1.0), "PWM_Quarry_1X1x1_C48_1041", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (6003.983, 4461.023, 2585.8784), (19.015841913852434, 27.090127731251147, 1.6012709691314483e-05), (1.1273026, 1.8110358, 1.75147), "PWM_Quarry_1X1x1_C49_1044", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2046.4761, 5840.806, 1350.6052), (4.453979771457414, -25.730041188076353, 12.359410528966277), (1.0, 1.0, 1.0), "PWM_Quarry_1X1x1_C5", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (6053.1753, 3906.7786, 2700.9592), (-9.322143812532703, 0.0, -0.0), (1.3195268, 2.4528894, 0.753246), "PWM_Quarry_1X1x1_C50_1059", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5758.2266, 4909.0728, 2561.557), (0.0, -23.76159728865054, 0.0), (1.0, 1.0, 1.0), "PWM_Quarry_1X1x1_C51_1065", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5712.363, 4913.698, 2492.0344), (0.0, 124.64368355905106, -0.0), (1.0806009, 0.6401712, 0.9203724), "PWM_Quarry_1X1x1_C52", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4890.7183, 5757.8955, 2613.8096), (-8.190642862073855, -18.488492054854408, -23.077511952185457), (1.5513898, 1.5513898, 1.5513898), "PWM_Quarry_1X1x1_C53_1072", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4663.8896, 5847.2905, 2638.727), (10.14154060821713, 162.35579226803927, -156.7884042570427), (2.1226625, 1.55139, 1.7820542), "PWM_Quarry_1X1x1_C54", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4370.963, 5917.3213, 2639.8105), (-0.16323854447955616, -93.56012721930472, 179.62147711521152), (1.5831428, 2.3012576, 2.0207052), "PWM_Quarry_1X1x1_C55", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4275.7056, 5970.1567, 2539.295), (0.0, 0.0, -0.0), (1.0, 1.0, 1.0), "PWM_Quarry_1X1x1_C56_1077", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3693.6228, 6013.9233, 2537.7175), (0.0, 0.0, -0.0), (1.0, 1.0, 1.0), "PWM_Quarry_1X1x1_C57_1080", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3660.6128, 5944.525, 2707.779), (0.0, 0.0, -39.92236441867888), (2.1004906, 1.0, 1.3131219), "PWM_Quarry_1X1x1_C58", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4154.9717, 5913.3384, 2670.4583), (0.0, 0.0, -168.61892951569968), (2.100491, 1.0, 1.313122), "PWM_Quarry_1X1x1_C59", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2893.3535, 571.3677, 1168.7682), (30.766978124013516, 0.0, -0.0), (1.0, 1.0, 1.0), "PWM_Quarry_1X1x1_C6_787", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4725.124, 5819.743, 2540.373), (-3.468505872028536, -23.4647501133139, -3.85232594485035), (1.0, 1.0, 1.0), "PWM_Quarry_1X1x1_C60_1085", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4493.616, 5905.9814, 2544.3442), (-0.7789612578797204, -10.864868783613959, -2.210510410722004), (1.0, 1.0, 1.0), "PWM_Quarry_1X1x1_C61_1088", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3986.61, 5948.7676, 2537.3777), (3.8786040402653565, 177.651350300977, -164.62945139922206), (2.0511446, 0.35938355, 0.7855906), "PWM_Quarry_1X1x1_C62_1091", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3806.0198, 5993.7725, 2512.7764), (0.0, 0.0, -4.777954021484684), (1.0984305, 0.7277935, 0.7277935), "PWM_Quarry_1X1x1_C63_1094", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3714.453, 5425.0396, 1300.3474), (0.0, -19.985534539528224, 0.0), (1.0, 1.0, 1.0), "PWM_Quarry_1X1x1_C64_1112", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3736.8442, 5412.9263, 1148.2769), (0.0, 115.04989204025506, -0.0), (1.0, 1.0, 1.0), "PWM_Quarry_1X1x1_C65", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4320.0, 4400.0, 2861.3867), (0.0, 0.0, -0.0), (1.5224257, 1.5224257, 1.0), "PWM_Quarry_1X1x1_C66_1236", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4224.827, 4330.947, 2861.3867), (-1.5274353167110708, 122.36086252870058, -0.9675292860467208), (1.522426, 1.522426, 1.0), "PWM_Quarry_1X1x1_C67", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4298.7983, 4214.2725, 2865.0713), (-1.5274352935494169, 122.36086190481767, -0.9674988111947606), (1.522426, 1.522426, 1.0), "PWM_Quarry_1X1x1_C68", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4406.556, 4282.5005, 2862.9177), (-1.5274352935494169, 122.36086190481767, -0.9674988111947606), (1.522426, 1.522426, 1.0), "PWM_Quarry_1X1x1_C69", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2893.3535, 787.876, 1168.7678), (-30.745270202073414, -177.64490761911185, -1.204833944757295), (1.0, 1.0, 1.0), "PWM_Quarry_1X1x1_C7", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4298.7207, 2159.3157, 2817.3557), (0.0, 0.0, -0.0), (1.0, 1.0, 0.4807394), "PWM_Quarry_1X1x1_C70_1245", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4251.109, 2086.7454, 2817.3557), (0.0, -135.6989028506422, 0.0), (1.0, 1.0, 0.55168045), "PWM_Quarry_1X1x1_C71", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4274.1074, 2002.0261, 2818.8118), (2.419409935246192, -98.85165445144118, 176.7754454978614), (1.0, 1.0, 0.55168), "PWM_Quarry_1X1x1_C72", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4363.95, 2076.4175, 2825.0237), (3.93981039280417, -33.50427046686161, -179.14943557819743), (1.0, 1.0, 0.55168), "PWM_Quarry_1X1x1_C73", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4370.3267, 2117.6663, 2830.2615), (3.93981039280417, -33.50427046686161, -179.14943557819743), (1.0, 1.0, 0.55168), "PWM_Quarry_1X1x1_C74", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2078.6367, 4219.5513, 2856.766), (0.0, 0.0, -0.0), (1.0, 1.0, 1.0), "PWM_Quarry_1X1x1_C75_1252", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2023.9834, 4324.734, 2853.6685), (0.0, 136.1258291357233, -0.0), (1.0, 1.0, 1.0), "PWM_Quarry_1X1x1_C76", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2032.2023, 4288.6997, 2855.5288), (0.0, -39.67468417948156, 0.0), (1.0, 1.0, 1.0), "PWM_Quarry_1X1x1_C77", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2110.865, 4383.548, 2858.6895), (0.0, 21.148803276792705, -0.0), (1.0, 1.0, 1.0), "PWM_Quarry_1X1x1_C78", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3534.1235, 764.23926, 1152.2256), (-20.02163874805416, -2.1541747733817966, -179.2626965512583), (1.8573928, 1.5721585, 1.2200764), "PWM_Quarry_1X1x1_C8", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2142.823, 1097.3083, 1222.7905), (0.0, 0.0, -0.0), (1.0, 1.0, 1.0), "PWM_Quarry_1X1x1_C9_798", _folder)
if a: placed += 1
else: skipped += 1

# Batch 120: StaticMesh'PWM_Quarry_2x2x2_A' (49 instances)
_mesh_path = "/Game/Unshippable/Whitebox/Rocks/Meshes/PWM_Quarry_2x2x2_A"
_materials = ['/Game/Environments/ProcTexturing/ProcMaterial_Quarry_Atlas_1']
_folder = "Reconstruction/BD_BB_Chapter2_Orctown_Throne/Meshes"
a = spawn_static_mesh(_mesh_path, _materials, (5750.0, 1500.0, 850.0), (0.0, 171.56242832611773, -0.0), (1.0, 1.0, 1.0), "PWM_Quarry_2x2x2_A_1113", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4606.6655, 475.3703, 862.8233), (87.4100091919345, 171.75161158401914, 154.20810822773302), (1.0, 1.0, 1.0), "PWM_Quarry_2x2x2_A10", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4461.073, 418.7925, 856.6726), (87.41004968093492, 171.75155999965227, 154.20814634642608), (1.0, 1.0, 1.0), "PWM_Quarry_2x2x2_A11", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4824.4526, 521.60394, 949.51105), (86.61782034730865, 30.939411992899025, 0.001103615578341815), (1.0, 1.0, 1.0), "PWM_Quarry_2x2x2_A12", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5326.357, 914.35614, 2538.1743), (5.397045484726087, -135.07590626956974, 169.82406780976558), (1.681746, 0.97009194, 1.4921649), "PWM_Quarry_2x2x2_A13_530", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (338.81842, 3204.8977, 2671.9326), (-27.489221857979118, 1.3149851564350912, 177.15291138447213), (1.2481856, 2.2700508, 1.9432952), "PWM_Quarry_2x2x2_A14_584", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (443.0476, 2098.0, 2579.6213), (-11.918090863393076, 0.0, -0.0), (1.0, 1.0, 1.0), "PWM_Quarry_2x2x2_A15_616", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (6038.4497, 5033.138, 1677.2054), (6.090471509124206e-06, -138.64939466814081, -28.332946734028233), (1.4908077, 1.0, 1.1791843), "PWM_Quarry_2x2x2_A16_662", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2626.335, 6071.896, 2679.5637), (26.43817145109614, 111.37569979976067, 5.3731489967420536e-05), (1.0, 1.0, 1.2850791), "PWM_Quarry_2x2x2_A17_748", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (791.6978, 1392.3201, 2622.7192), (-14.776551546080665, 27.823881877894678, 0.4591626567374029), (0.3501821, 1.1474274, 1.0), "PWM_Quarry_2x2x2_A18_779", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5051.2715, 639.9799, 2574.8835), (5.397044200638241, -135.07590236740754, 169.82402476570056), (1.492165, 0.970092, 1.492165), "PWM_Quarry_2x2x2_A19", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5723.363, 1678.2986, 850.0), (0.0, 30.9373715235579, -0.0), (1.0, 1.0, 1.0), "PWM_Quarry_2x2x2_A2", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4856.421, 588.2273, 2667.7764), (1.7020552743422175, -154.3359717256588, 168.61927300153377), (1.492165, 0.970092, 1.492165), "PWM_Quarry_2x2x2_A20", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3901.924, 399.83847, 2686.5073), (-0.27954121884625743, -164.10278047801748, 168.49725367461113), (1.492165, 0.970092, 1.5998236), "PWM_Quarry_2x2x2_A21", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2168.8865, 506.37006, 2760.8235), (28.062987308058393, -110.77371725464441, 175.55687448864398), (1.0, 2.9572048, 1.320162), "PWM_Quarry_2x2x2_A22_837", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3258.2092, 4946.423, 2968.1628), (0.0, 0.0, -0.0), (1.6487787, 1.6487787, 1.2185786), "PWM_Quarry_2x2x2_A23_856", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1465.8541, 4795.3877, 2867.774), (7.147792193781614, 0.0, -0.0), (1.6687258, 1.6687258, 0.95718926), "PWM_Quarry_2x2x2_A24_861", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1370.7682, 4162.3066, 2858.6394), (4.534965562976952, 0.0, -0.0), (1.2883531, 1.2883531, 0.78728026), "PWM_Quarry_2x2x2_A25_864", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2083.3599, 4324.3125, 2920.0305), (0.0, 0.0, -0.0), (1.0, 1.0, 1.0), "PWM_Quarry_2x2x2_A26_871", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2083.3599, 4549.874, 2958.6567), (0.0, 0.0, -0.0), (1.4504013, 1.6845131, 1.0), "PWM_Quarry_2x2x2_A27", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2148.9155, 3993.6274, 2958.6567), (0.0, 0.0, -0.0), (2.1332781, 2.4255166, 1.0), "PWM_Quarry_2x2x2_A28", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2106.4128, 2088.399, 2909.0457), (0.0, 0.0, -0.0), (1.3223469, 1.3223469, 1.0), "PWM_Quarry_2x2x2_A29_880", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4303.836, 5998.339, 1160.0), (0.0, 25.00004727668659, -0.0), (1.0, 1.0, 1.0), "PWM_Quarry_2x2x2_A3_81", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2133.9927, 2421.833, 2932.145), (0.0, 0.0, -0.0), (1.5157845, 1.5157845, 0.7660521), "PWM_Quarry_2x2x2_A30_887", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2299.7617, 2163.8906, 2932.145), (0.0, 0.0, -0.0), (1.515785, 1.515785, 0.766052), "PWM_Quarry_2x2x2_A31", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1832.271, 1779.8597, 2960.3538), (0.0, 121.41117625009205, -0.0), (2.5730674, 2.5730674, 1.2591196), "PWM_Quarry_2x2x2_A32", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5143.817, 2186.781, 2859.042), (7.487300523052826, 180.0, -180.0), (1.483616, 1.7428284, 0.8568221), "PWM_Quarry_2x2x2_A33_893", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4655.0938, 2467.1826, 2904.3335), (5.828028403556326, -179.99995901497118, -178.02491157562034), (2.1510813, 2.1123416, 0.856822), "PWM_Quarry_2x2x2_A34", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4494.592, 2647.1145, 2926.9531), (5.828028403556326, -179.99995901497118, -178.02491157562034), (1.483616, 1.742828, 0.856822), "PWM_Quarry_2x2x2_A35", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4484.5654, 1589.404, 2887.6592), (-5.993682784120788, 0.0, -0.0), (1.7262033, 1.6256473, 0.5864452), "PWM_Quarry_2x2x2_A36_898", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2101.9524, 1187.6462, 2960.3538), (0.0, 121.41117625009205, -0.0), (2.573067, 2.573067, 1.25912), "PWM_Quarry_2x2x2_A37", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3741.186, 1187.6462, 2960.3535), (0.0, 121.41117625009205, -0.0), (2.573067, 2.573067, 1.25912), "PWM_Quarry_2x2x2_A38", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3215.9521, 1139.52, 2971.464), (0.9983771862518187, -7.046936163408126, -177.69845416460635), (3.0125759, 2.573067, 1.25912), "PWM_Quarry_2x2x2_A39", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4016.873, 6031.713, 1290.0), (0.0, -84.9998429854697, 0.0), (1.0, 1.25, 1.0), "PWM_Quarry_2x2x2_A4", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2754.7463, 1138.5149, 2957.4558), (0.0, 0.0, -0.0), (1.9293742, 1.8500218, 1.1187695), "PWM_Quarry_2x2x2_A40_904", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1642.5327, 626.8499, 2711.212), (3.9665446659846584, -17.59753288538496, 45.21354015087122), (1.964072, 1.0, 1.8125366), "PWM_Quarry_2x2x2_A41_907", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3353.5461, 1779.8597, 2977.3555), (2.1526771229999815, 121.43185175537127, 0.18352435379968712), (2.573067, 2.573067, 1.25912), "PWM_Quarry_2x2x2_A42", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2603.8313, 1779.8624, 3001.3193), (2.1526775229938937, 121.4318517579032, 0.1835241295109517), (2.8906066, 2.8608024, 1.4117502), "PWM_Quarry_2x2x2_A43", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3830.1543, 2103.0095, 2905.0417), (0.0, 0.0, -0.0), (1.608922, 1.608922, 0.503729), "PWM_Quarry_2x2x2_A44_913", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5919.1265, 4834.5103, 891.2001), (0.0, 0.0, -0.0), (1.0, 1.0, 1.0), "PWM_Quarry_2x2x2_A45_940", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5957.8286, 4712.882, 898.26135), (0.0, -44.85796740968373, 0.0), (1.0, 1.0, 1.0), "PWM_Quarry_2x2x2_A46", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4425.2656, 5944.8, 1000.35925), (0.0, -18.91149970152176, 0.0), (1.3603141, 1.0, 1.0), "PWM_Quarry_2x2x2_A47", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4651.8574, 5867.1714, 926.1154), (-25.76522838698399, -18.91150167131839, 1.749049249343262e-06), (1.360314, 1.0, 1.1688447), "PWM_Quarry_2x2x2_A48", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4627.241, 5833.833, 806.2358), (-20.375819056570304, -41.611988932832745, -161.21581984128372), (1.360314, 1.0285463, 1.2560718), "PWM_Quarry_2x2x2_A49", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (886.14124, 5100.901, 995.0), (0.0, 45.0004274829829, -0.0), (1.0, 1.0, 1.0), "PWM_Quarry_2x2x2_A5", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5881.086, 1749.9114, 905.0), (0.0, 17.13782095284447, -0.0), (1.0, 1.0, 1.0), "PWM_Quarry_2x2x2_A6", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2060.63, 1073.8875, 1238.2571), (2.310153410018802, 0.0, -0.0), (0.499218, 1.0, 1.0), "PWM_Quarry_2x2x2_A7_792", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5788.77, 1584.358, 903.0), (0.0, 17.13782095284447, -0.0), (1.0, 1.0, 1.0), "PWM_Quarry_2x2x2_A8", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4765.0186, 544.2769, 851.0), (0.0, 30.9373715235579, -0.0), (1.0, 1.0, 1.0), "PWM_Quarry_2x2x2_A9", _folder)
if a: placed += 1
else: skipped += 1

# Batch 121: StaticMesh'PWM_Quarry_2x2x5_A' (39 instances)
_mesh_path = "/Game/Unshippable/Whitebox/Rocks/Meshes/PWM_Quarry_2x2x5_A"
_materials = ['/Game/Environments/ProcTexturing/ProcMaterial_Quarry_Atlas_2']
_folder = "Reconstruction/BD_BB_Chapter2_Orctown_Throne/Meshes"
a = spawn_static_mesh(_mesh_path, _materials, (2019.7189, 1145.3408, 1070.0), (0.0, -44.999723200496135, 0.0), (1.0, 1.0, 1.1703402), "PWM_Quarry_2x2x5_A_417", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2603.893, 929.91003, 1075.6464), (0.9804392562357688, 163.1936003674366, 0.7582014062157598), (1.0, 1.0, 1.2273942), "PWM_Quarry_2x2x5_A10", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1104.7188, 4656.1987, 765.0), (-75.93729163348378, 56.2507729381101, 89.9992693430505), (1.0, 1.0, 1.3), "PWM_Quarry_2x2x5_A11_361", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1554.3206, 4803.797, 849.8739), (-2.602236459401002, 137.17276932090053, -90.66181647437769), (1.0, 1.0, 1.3), "PWM_Quarry_2x2x5_A12", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2541.354, 1001.04626, 1224.8884), (0.0, 0.0, -0.0), (0.59907556, 0.59907556, 0.5689328), "PWM_Quarry_2x2x5_A13_795", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2892.1357, 564.16956, 963.6839), (0.0, -12.049042202371162, 0.0), (1.0, 1.0, 1.0), "PWM_Quarry_2x2x5_A14_809", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (378.2024, 4254.5435, 1133.0), (0.0, 60.851259452854634, -0.0), (2.094418, 1.40226, 1.40226), "PWM_Quarry_2x2x5_A15_572", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (357.24792, 4232.415, 1822.0), (0.0, -51.24456420703744, 0.0), (1.40226, 1.40226, 1.40226), "PWM_Quarry_2x2x5_A16", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (434.7908, 4211.4243, 1822.0), (0.0, 136.99732719329612, -0.0), (1.40226, 1.40226, 1.40226), "PWM_Quarry_2x2x5_A17", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (6285.1875, 2627.3906, 1791.7145), (0.0, -30.134493517329478, 0.0), (1.5, 1.5, 1.95), "PWM_Quarry_2x2x5_A18", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (6138.0, 5242.1587, 1670.0138), (16.411304999820235, 2.6477746669007356, 9.29621683057662), (1.0, 1.0, 1.0), "PWM_Quarry_2x2x5_A19_665", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2319.7188, 5311.1987, 1070.0), (0.0, 75.93784477991429, -0.0), (1.0, 1.0, 1.3), "PWM_Quarry_2x2x5_A2", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (434.7908, 4211.4243, 2149.0), (8.30179321140925, 136.99729545542667, 1.0275204879548418e-05), (1.40226, 1.40226, 1.40226), "PWM_Quarry_2x2x5_A20", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4901.26, 5870.8184, 972.0), (0.0, 46.84921631877369, -0.0), (1.0, 1.0, 1.0), "PWM_Quarry_2x2x5_A21_730", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4901.26, 5870.8184, 1413.0), (0.0, 46.84921631877369, -0.0), (1.0, 1.0, 1.0), "PWM_Quarry_2x2x5_A22", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1859.133, 521.10223, 1624.3975), (0.0, -44.91534422362216, 0.0), (1.0, 1.0, 1.0), "PWM_Quarry_2x2x5_A23_785", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (519.8709, 4211.552, 1405.8422), (0.0, -61.10681547232431, 0.0), (1.0, 1.0, 1.0), "PWM_Quarry_2x2x5_A24_922", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (983.6225, 1192.1073, 2646.0808), (-73.52856100397746, 15.293686782465254, -73.3107724171695), (1.0, 1.0, 1.195116), "PWM_Quarry_2x2x5_A25_925", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (679.33575, 1691.9121, 2598.2769), (-73.52856100397746, 15.293686782465254, -73.3107724171695), (1.0, 1.0, 1.195116), "PWM_Quarry_2x2x5_A26", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (556.2214, 2100.4731, 2482.3198), (-21.232634845398263, 0.0, -0.0), (1.0, 1.0, 1.0), "PWM_Quarry_2x2x5_A27_932", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (719.3712, 1821.2267, 2600.5867), (-62.48743292737772, 2.664480100134637, -72.44192673110177), (1.0, 1.0, 1.0), "PWM_Quarry_2x2x5_A28", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (768.0774, 4662.7715, 2626.5833), (-60.77151266273741, -24.343833841055886, -79.24324264665383), (1.464758, 1.464758, 1.464758), "PWM_Quarry_2x2x5_A29_953", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2509.7188, 5351.1987, 1070.0), (0.0, -92.81212592316798, 0.0), (1.0, 1.0, 1.3), "PWM_Quarry_2x2x5_A3", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (675.6763, 4303.3086, 2630.2607), (-23.279172788313605, -42.436586058247286, 19.86674638763061), (1.0, 1.0, 1.0), "PWM_Quarry_2x2x5_A30_959", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1384.2365, 5589.162, 2646.659), (87.9112934564925, 179.99827235137076, 152.57902280906407), (1.0, 1.0, 1.0), "PWM_Quarry_2x2x5_A31_965", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1753.248, 5775.0713, 2660.1086), (87.89653653861373, -179.9975821926191, -33.92477964628371), (1.0, 1.0, 1.0), "PWM_Quarry_2x2x5_A32", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1123.8712, 939.53076, 2577.6584), (84.15684651148787, 42.956600190730846, 86.03855419533183), (1.0, 1.0, 1.0), "PWM_Quarry_2x2x5_A33_1006", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1142.8477, 958.5057, 2692.6194), (63.51606132340965, 46.089008216793154, 89.09600498091591), (1.6703867, 1.0, 1.0), "PWM_Quarry_2x2x5_A34", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4349.7007, 561.1577, 2646.608), (0.0, 0.0, 51.01129212984899), (1.5545311, 1.0, 1.0), "PWM_Quarry_2x2x5_A35_1025", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5730.086, 4987.305, 2385.5217), (-20.61358087663201, 177.65065211390984, -174.5641543727581), (1.0, 1.0, 1.0), "PWM_Quarry_2x2x5_A36_1062", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2615.7837, 5373.965, 1010.548), (0.0, -102.54363370465832, 0.0), (1.0, 1.0, 1.5242901), "PWM_Quarry_2x2x5_A37_1100", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2415.8132, 5295.362, 1129.2349), (0.0, -75.94683333813549, 0.0), (0.62882316, 0.58991444, 0.670628), "PWM_Quarry_2x2x5_A38_1106", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3752.6946, 5395.796, 988.4826), (1.5344715071970002e-08, 153.15056319815727, -5.5260915045424825), (1.0, 0.90292495, 1.0), "PWM_Quarry_2x2x5_A39_1109", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2659.7188, 5441.1987, 1070.0), (0.0, 53.437986469202855, -0.0), (1.0, 1.0, 1.3), "PWM_Quarry_2x2x5_A4", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3820.4412, 5381.827, 1070.0), (6.271659155610435, 22.614321539255027, -0.43835476974020393), (0.7266629, 0.7266629, 1.3), "PWM_Quarry_2x2x5_A5", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3684.6882, 5411.6445, 1053.6165), (0.0, -134.49744120408792, 0.0), (1.0, 1.0, 1.3), "PWM_Quarry_2x2x5_A6", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5136.768, 657.3196, 2039.0), (0.0, -42.129732630648114, 0.0), (1.0, 1.0, 1.0), "PWM_Quarry_2x2x5_A7_524", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (695.0, 5105.0, 1530.0), (0.0, -90.00009542133918, 0.0), (1.0, 1.0, 1.0), "PWM_Quarry_2x2x5_A8_141", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (6262.9365, 2478.6292, 1791.7145), (0.0, -40.189726491611665, 0.0), (1.5, 1.5, 1.95), "PWM_Quarry_2x2x5_A9", _folder)
if a: placed += 1
else: skipped += 1

# Batch 122: StaticMesh'PWM_Quarry_2x2x5_B' (19 instances)
_mesh_path = "/Game/Unshippable/Whitebox/Rocks/Meshes/PWM_Quarry_2x2x5_B"
_materials = ['/Game/Environments/ProcTexturing/ProcMaterial_Quarry_Atlas_2']
_folder = "Reconstruction/BD_BB_Chapter2_Orctown_Throne/Meshes"
a = spawn_static_mesh(_mesh_path, _materials, (682.8614, 5095.7905, 1110.5111), (14.999998221152174, -134.999857921603, 2.219840356751301e-06), (1.0, 1.0, 1.0), "PWM_Quarry_2x2x5_B_138", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (391.0, 2167.0, 2245.0), (0.0, -22.22479154464803, 0.0), (1.6419834, 1.6419834, 1.6419834), "PWM_Quarry_2x2x5_B10_609", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (563.3332, 1588.0172, 2197.2466), (-1.4592286305110456, 133.52187161102054, 176.76546921148508), (1.641983, 1.7676729, 1.641983), "PWM_Quarry_2x2x5_B11", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (6287.176, 5447.604, 1042.1888), (-6.168671612839986, -53.87616371876974, 5.944510376943963), (1.0, 1.0, 1.0), "PWM_Quarry_2x2x5_B12_688", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4944.748, 5839.943, 1825.3643), (4.917633929217573, 34.3450428486753, -7.151184045050317), (1.0, 1.0, 1.0), "PWM_Quarry_2x2x5_B13_734", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (677.0, 5010.0, 1260.0), (0.0, 0.0, -0.0), (1.0, 1.0, 1.3900867), "PWM_Quarry_2x2x5_B14_770", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (461.641, 4220.5312, 1076.0131), (0.0, 0.0, -0.0), (1.4538338, 1.4401686, 1.5020062), "PWM_Quarry_2x2x5_B15_919", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (536.2575, 3844.6672, 2644.2974), (-22.276670275344383, 2.8970777486781154, -97.60394333251152), (1.0, 1.3635987, 1.4870716), "PWM_Quarry_2x2x5_B16_936", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (467.51883, 3300.0933, 2605.7341), (-22.276670275344383, 2.8970777486781154, -97.60394333251152), (1.0, 1.363599, 1.487072), "PWM_Quarry_2x2x5_B17", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5850.2456, 4813.178, 900.73425), (-7.261682924021759e-09, -170.35825617580537, 4.102329500218557), (1.0887815, 1.123345, 1.0), "PWM_Quarry_2x2x5_B18_944", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5818.9014, 5003.2935, 1937.1643), (9.163360121713763, 2.1108859333114628e-07, 0.23587440457044054), (1.0, 1.0, 1.0), "PWM_Quarry_2x2x5_B19_1069", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4933.256, 516.2293, 1090.0), (0.0, -95.0000906276283, 0.0), (1.46875, 1.46875, 1.46875), "PWM_Quarry_2x2x5_B2_206", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4927.533, 501.46304, 1470.0), (0.0003620000949558389, 167.0929866084181, 179.99980192457517), (1.46875, 1.46875, 1.46875), "PWM_Quarry_2x2x5_B3", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5015.78, 530.08966, 2010.0), (0.0, 84.99978912167116, -0.0), (1.46875, 1.46875, 1.46875), "PWM_Quarry_2x2x5_B4", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5095.2563, 688.3104, 2360.8176), (-6.389708430895504, -146.89309559069702, 172.93541806137273), (1.4038295, 1.0, 1.0), "PWM_Quarry_2x2x5_B5_536", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (742.0, 5017.0, 907.0), (0.0, 0.0, -0.0), (1.0, 1.0, 1.0), "PWM_Quarry_2x2x5_B6_566", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (692.52155, 4897.523, 775.0), (0.0, 119.23429877492221, -0.0), (1.4860817, 1.4860817, 1.1681317), "PWM_Quarry_2x2x5_B7", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (622.4198, 4672.64, 689.0), (0.0, -80.50097958139102, 0.0), (1.486082, 1.486082, 1.168132), "PWM_Quarry_2x2x5_B8", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (378.0, 4206.0, 1642.0), (0.0, 0.0, -0.0), (1.0, 1.0, 1.0), "PWM_Quarry_2x2x5_B9_576", _folder)
if a: placed += 1
else: skipped += 1

# Batch 123: StaticMesh'PWM_Quarry_3x3x2' (1 instances)
_mesh_path = "/Game/Unshippable/Whitebox/Rocks/Meshes/PWM_Quarry_3x3x2"
_materials = ['/Game/Environments/ProcTexturing/ProcMaterial_Quarry_Atlas_A']
_folder = "Reconstruction/BD_BB_Chapter2_Orctown_Throne/Meshes"
a = spawn_static_mesh(_mesh_path, _materials, (1178.6454, 818.1025, 2555.1785), (-9.26605166181838, 3.9421524716321095, -4.625487659175206), (1.0, 1.0, 1.0), "PWM_Quarry_3x3x2_1013", _folder)
if a: placed += 1
else: skipped += 1

# Batch 124: StaticMesh'PWM_Quarry_4x4x4_A' (52 instances)
_mesh_path = "/Game/Unshippable/Whitebox/Rocks/Meshes/PWM_Quarry_4x4x4_A"
_materials = ['/Game/Environments/ProcTexturing/ProcMaterial_Quarry_Atlas_2']
_folder = "Reconstruction/BD_BB_Chapter2_Orctown_Throne/Meshes"
a = spawn_static_mesh(_mesh_path, _materials, (2648.6365, 648.335, 1008.0999), (-8.436157904347649, 65.51924494969953, -0.12112452690090408), (1.0, 1.0, 1.0), "PWM_Quarry_4x4x4_A_394", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1625.1046, 483.6613, 2217.7773), (-1.9591671457325595, 163.20660397784584, -164.98597623714093), (0.840395, 1.0, 1.0), "PWM_Quarry_4x4x4_A10", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3632.3362, 212.57912, 980.0), (0.0, -0.9375610970281315, 0.0), (1.0, 1.0, 1.0), "PWM_Quarry_4x4x4_A11", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2775.3433, 201.60071, 980.0), (0.0, 89.06243281681215, -0.0), (1.0, 1.0, 1.0), "PWM_Quarry_4x4x4_A12", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1597.4784, 459.42236, 2539.4878), (-1.959136616875403, 163.2066047779054, 174.5720395357383), (0.949966, 1.0, 1.0), "PWM_Quarry_4x4x4_A13", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5345.131, 823.4196, 2180.2866), (-19.481053017653828, 145.76337620423203, 5.254415420692514e-05), (0.4235939, 1.0, 1.2467449), "PWM_Quarry_4x4x4_A14_533", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (391.06342, 4086.624, 2571.0), (-2.0420587056687212e-07, -94.72597544194397, 18.52307830228767), (1.0890814, 0.7173834, 1.0), "PWM_Quarry_4x4x4_A15_580", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (434.89786, 3664.7817, 2600.0554), (-2.70129366145072, 87.93271473379153, -18.53683409984325), (1.089081, 0.717383, 1.0), "PWM_Quarry_4x4x4_A16", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (473.1835, 1638.918, 1831.1823), (-5.027602654406379e-07, -65.7243561612109, 14.51757600797588), (1.0, 0.6849337, 1.0), "PWM_Quarry_4x4x4_A17_597", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (350.3641, 2083.3472, 1812.8618), (-6.025878976449173, 90.21544679029279, -2.91210959778578), (1.0, 0.684934, 1.0), "PWM_Quarry_4x4x4_A18", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (204.60948, 2624.0078, 2615.0), (0.0, 26.892010581165923, -0.0), (1.3944023, 1.3944023, 1.123941), "PWM_Quarry_4x4x4_A19_605", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1705.7123, 982.4695, 960.0), (0.0, -106.87490538106198, 0.0), (1.0, 1.0, 1.0), "PWM_Quarry_4x4x4_A2", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (209.65115, 2289.0674, 2615.0), (0.0, 26.892010581165923, -0.0), (1.394402, 1.394402, 1.123941), "PWM_Quarry_4x4x4_A20", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (800.225, 5141.16, 2644.8564), (-18.655087540906372, -20.60042960774782, -7.680205943711739), (0.4894123, 1.0, 0.5517706), "PWM_Quarry_4x4x4_A21_757", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (691.6707, 4863.6934, 2637.3154), (-20.366332898716237, -19.785491569893214, -179.94826816355985), (0.489412, 1.0, 0.551771), "PWM_Quarry_4x4x4_A22", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4434.6445, 3804.509, 2875.4463), (-1.910034341145404, 49.59982223909841, -1.79833984850949), (1.2788452, 1.2965931, 0.2551112), "PWM_Quarry_4x4x4_A23_807", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3559.9287, 4551.43, 2936.4028), (-2.4920961491281863, 24.502337178896653, 1.0349946113249797), (1.4887938, 1.5065417, 0.4650599), "PWM_Quarry_4x4x4_A24", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4250.42, 5007.656, 2914.013), (-2.492096022441351, 24.50233716995151, 1.0349951082234856), (1.488794, 1.506542, 0.46506), "PWM_Quarry_4x4x4_A25", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4043.7979, 5663.763, 2829.8845), (-8.63775553913787, 23.03871046040011, -168.56988561883253), (1.488794, 1.506542, 0.46506), "PWM_Quarry_4x4x4_A26", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3314.1423, 5663.763, 2829.8845), (18.846450855616578, -94.06201515863323, 175.33820840627956), (1.488794, 1.506542, 0.46506), "PWM_Quarry_4x4x4_A27", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2693.651, 5694.471, 2796.7698), (-78.41481634409948, -95.09401879418013, -178.39633741396156), (0.42217755, 1.506542, 2.0958228), "PWM_Quarry_4x4x4_A28", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3287.1528, 5211.9214, 2918.3787), (10.259413029903135, -93.35277916998982, 175.51673481906664), (1.488794, 1.506542, 0.46506), "PWM_Quarry_4x4x4_A29", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2069.3267, 506.9919, 960.0), (0.0, -19.68621858310701, 0.0), (1.0, 1.0, 1.0), "PWM_Quarry_4x4x4_A3", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4793.5664, 874.2774, 2771.0396), (-4.785612626978819, 30.650193031142404, 160.60474404932438), (1.2532841, 1.2748182, 0.4475495), "PWM_Quarry_4x4x4_A30_829", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4248.9146, 701.7288, 2809.2192), (-1.8970943310161796, 20.583497033291906, 162.64579789033002), (1.7921933, 1.274818, 0.447549), "PWM_Quarry_4x4x4_A31", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3497.1018, 599.31055, 2874.7988), (1.3926121359349657, -161.85744217841832, -162.7364912008318), (1.792193, 1.274818, 0.447549), "PWM_Quarry_4x4x4_A32", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2271.3748, 617.1262, 2845.668), (-7.609005590760379, -166.39191859848393, -165.98198106786955), (1.792193, 1.274818, 0.447549), "PWM_Quarry_4x4x4_A33", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1724.3516, 738.44476, 2817.9539), (-14.799717067828931, -82.25428413315392, 172.6067791486006), (1.792193, 1.274818, 0.447549), "PWM_Quarry_4x4x4_A34", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3000.109, 632.8749, 2878.5872), (-2.2935481446008206, -165.12679211818212, -166.95099514657184), (1.792193, 1.274818, 0.447549), "PWM_Quarry_4x4x4_A35", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1335.8561, 966.83154, 2807.3865), (7.356229191067468, -0.88677989436531, -6.8930668178174805), (1.1406617, 1.1406617, 0.5719157), "PWM_Quarry_4x4x4_A36_842", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (991.0027, 4456.9756, 2842.5623), (8.7007452301532, 2.0764811749667353e-06, 2.2392276930253665), (1.4298997, 1.4298997, 0.6294907), "PWM_Quarry_4x4x4_A37_845", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1087.538, 5077.3726, 2817.274), (-8.768889832782978, 135.24214886735012, 3.495691316421374), (1.4299, 1.4299, 0.629491), "PWM_Quarry_4x4x4_A38", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1552.4044, 5479.9565, 2818.2803), (12.341776708511892, -44.42221414288396, -174.75148074135728), (1.4299, 1.4299, 0.629491), "PWM_Quarry_4x4x4_A39", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3603.8188, 401.00977, 980.0), (0.0, 59.062743517676566, -0.0), (1.0, 1.0, 1.0), "PWM_Quarry_4x4x4_A4", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2183.4531, 5662.107, 2835.2258), (-3.383697684521777, 36.69561199613832, -167.02941927890805), (2.0524025, 2.0196595, 0.629491), "PWM_Quarry_4x4x4_A40", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3585.136, 5109.84, 2949.5625), (0.8823137406376622, -0.3048095554994744, 2.21375195618973), (1.4299, 1.4299, 0.629491), "PWM_Quarry_4x4x4_A41", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2635.3428, 4924.6895, 2910.9663), (-86.76382199669544, -99.23669929630567, 11.332150597529422), (0.422178, 1.741513, 2.095823), "PWM_Quarry_4x4x4_A42", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1820.8783, 4286.4214, 2977.6936), (8.700745232529606, 1.990052374770156e-06, 2.2392279164343294), (1.4299, 1.4299, 0.629491), "PWM_Quarry_4x4x4_A43", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1917.4135, 4906.822, 2952.4053), (-8.76889017748329, 135.24214885450425, 3.495691698534231), (1.4299, 1.4299, 0.629491), "PWM_Quarry_4x4x4_A44", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2319.853, 4703.041, 2942.0166), (85.63226643439508, -10.05672057145228, -96.72588784157215), (0.3354685, 1.0, 1.0), "PWM_Quarry_4x4x4_A45_868", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4310.6704, 1219.4559, 2908.5518), (-4.7855832198073225, 30.65048962526746, 174.54198742501086), (1.253284, 1.274818, 0.447549), "PWM_Quarry_4x4x4_A46", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1628.3142, 2226.5413, 2948.9639), (0.0, 0.0, -0.0), (1.3261849, 1.3261849, 0.69086784), "PWM_Quarry_4x4x4_A47_883", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1535.1636, 1449.1941, 2948.9639), (0.0, 94.94447561095085, -0.0), (1.6348251, 1.326185, 0.690868), "PWM_Quarry_4x4x4_A48", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3994.1638, 1757.9692, 2927.1033), (1.472076332956466, -154.07968843742643, 179.17486498718586), (1.253284, 1.274818, 0.447549), "PWM_Quarry_4x4x4_A49", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3733.7668, 734.2919, 980.0002), (0.0, 105.19869651452663, -0.0), (0.77088475, 0.7709098, 1.0), "PWM_Quarry_4x4x4_A5", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5338.9463, 876.75916, 2578.2512), (1.942254464724471, 42.72102810914737, -27.431701909424625), (1.0, 1.0, 0.590141), "PWM_Quarry_4x4x4_A50_981", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5002.3916, 641.94556, 2617.977), (-2.8623046237982686, 45.214424413871, -27.451107383123613), (1.0, 1.0, 0.590141), "PWM_Quarry_4x4x4_A51", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (917.549, 1207.1034, 2611.7434), (-29.950652109723517, 37.3431813303608, 3.5388745036004516e-05), (0.2775963, 0.7051546, 0.49780175), "PWM_Quarry_4x4x4_A52_994", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1170.5128, 3664.3594, 2919.8936), (0.0, 0.0, -0.0), (1.0, 1.0, 1.0), "PWM_Quarry_4x4x4_A53_1119", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2746.326, 285.54077, 980.0), (0.0, -66.87478349427276, 0.0), (1.0, 1.0, 1.0), "PWM_Quarry_4x4x4_A6", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1624.5391, 437.43985, 1575.332), (-8.420959152348633, 91.13540947565372, 0.5215373165105113), (1.0, 1.0777078, 1.0), "PWM_Quarry_4x4x4_A8", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1617.0184, 445.47183, 1927.2991), (-1.8498532184874157, -41.529326319193906, 13.538641266662262), (0.9003188, 1.0, 1.0), "PWM_Quarry_4x4x4_A9", _folder)
if a: placed += 1
else: skipped += 1

# Batch 125: StaticMesh'PWM_Quarry_4x5x10' (9 instances)
_mesh_path = "/Game/Unshippable/Whitebox/Rocks/Meshes/PWM_Quarry_4x5x10"
_materials = ['/Game/Environments/ProcTexturing/ProcMaterial_Quarry_Atlas_A']
_folder = "Reconstruction/BD_BB_Chapter2_Orctown_Throne/Meshes"
a = spawn_static_mesh(_mesh_path, _materials, (5818.5054, 1319.1516, 1889.0483), (10.154926573834434, -0.6746215157384395, -3.8206473869274755), (0.713486, 0.713486, 1.0), "PWM_Quarry_4x5x10_508", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (342.54715, 2108.675, 1263.0), (0.0, 21.43782970303538, -0.0), (1.0, 1.0, 1.0), "PWM_Quarry_4x5x11_594", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (424.0, 1833.0, 2282.0), (-6.338439535992678, 19.164459555714533, 1.053687918564717e-05), (1.0, 1.0, 1.0), "PWM_Quarry_4x5x12_613", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (6447.8794, 3652.1316, 1565.0338), (8.9288526438487, 16.830479090700354, 2.68794799749543), (1.0, 1.0, 1.0), "PWM_Quarry_4x5x13_641", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (6378.772, 3595.018, 2249.8845), (15.487079088544975, 12.837530356191769, 2.0748453624633894), (1.0, 1.0, 1.0), "PWM_Quarry_4x5x14", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (6030.944, 4954.5635, 1162.0), (3.9845339450095185, -51.56781071554438, 6.071518732920171e-06), (1.0, 1.0, 1.0), "PWM_Quarry_4x5x15_659", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5605.653, 5260.5747, 2324.93), (3.2913365020597054e-08, -54.17981416491565, -9.061278810896775), (1.0, 0.41861248, 1.0), "PWM_Quarry_4x5x16_694", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5724.4595, 5095.969, 2324.93), (3.2913365020597054e-08, -54.17981416491565, -9.061278810896775), (1.0, 0.418612, 1.0), "PWM_Quarry_4x5x17", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4619.6514, 589.5097, 2552.0554), (45.70395008448838, -67.00809796010496, 94.68909742514802), (0.3180861, 1.3076545, 0.6022921), "PWM_Quarry_4x5x18_1022", _folder)
if a: placed += 1
else: skipped += 1

# Batch 126: StaticMesh'PWM_Quarry_8x8x8_A' (45 instances)
_mesh_path = "/Game/Unshippable/Whitebox/Rocks/Meshes/PWM_Quarry_8x8x8_A"
_materials = ['/Game/Environments/ProcTexturing/ProcMaterial_Quarry_Atlas_2']
_folder = "Reconstruction/BD_BB_Chapter2_Orctown_Throne/Meshes"
a = spawn_static_mesh(_mesh_path, _materials, (322.18997, 4706.464, 1200.0), (0.0, -3.246429648757626, 0.0), (0.65625, 1.0, 1.0), "PWM_Quarry_8x8x8_A_1102", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5079.049, 6220.3447, 1150.0), (0.0, 39.68725649420377, -0.0), (1.0, 0.53125, 1.0), "PWM_Quarry_8x8x8_A10", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5796.722, 769.59143, 2068.7366), (3.714698840728652, -134.18481444142574, -6.503264784608738), (1.0, 1.0, 0.94683677), "PWM_Quarry_8x8x8_A11_521", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5513.7764, 1131.2416, 2625.847), (3.7146999749302076, -134.1831439999379, -66.3206778922521), (1.0, 1.0, 0.946837), "PWM_Quarry_8x8x8_A12", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5083.0044, 1538.7755, 2902.9968), (2.4622902943252853, -123.29101697773764, -83.15521258851065), (1.0, 0.36243817, 0.946837), "PWM_Quarry_8x8x8_A13", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4513.658, 2032.6323, 2987.313), (2.3965383357787036, -134.16723804610334, 89.71879551198752), (1.0, 0.362438, 0.946837), "PWM_Quarry_8x8x8_A14", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3987.4106, 2577.8381, 2990.5762), (-2.4030121430041, 47.49752530999306, 90.21152708131493), (1.0, 0.362438, 0.946837), "PWM_Quarry_8x8x8_A15", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (322.18997, 4706.464, 1948.0), (0.0, -3.246429648757626, 0.0), (0.65625, 1.0, 1.0), "PWM_Quarry_8x8x8_A16", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (386.7464, 4957.872, 1948.0), (0.0, -27.313202006963436, 0.0), (0.65625, 1.0, 1.0), "PWM_Quarry_8x8x8_A17", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (888.408, 3727.0, 2781.887), (-77.39987643360963, 0.0, -0.0), (0.17070451, 1.0, 1.0), "PWM_Quarry_8x8x8_A18_590", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1553.1174, 3706.0, 2920.078), (-86.54053030442569, 7.629463861347795e-05, -1.1813400040335573e-11), (0.28316855, 1.0, 1.0), "PWM_Quarry_8x8x8_A19", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (308.92105, 1685.1587, 1200.0), (0.0, -76.87496689310434, 0.0), (1.0, 0.6875, 1.0), "PWM_Quarry_8x8x8_A2", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5724.7183, 2206.5408, 2862.127), (2.774173724326992, -112.86458532708703, -82.31586080594369), (1.0, 0.362438, 0.946837), "PWM_Quarry_8x8x8_A20", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5124.178, 2661.1619, 2950.6184), (3.626624924403196, -130.20200967665872, 89.96918079583351), (1.0, 0.362438, 0.946837), "PWM_Quarry_8x8x8_A21", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (6142.799, 2701.2375, 2821.0735), (4.944839844871366, -130.20848139346475, -83.49264278746446), (1.0, 0.362438, 0.946837), "PWM_Quarry_8x8x8_A22", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5542.259, 3155.8586, 2909.565), (3.626624924403196, -130.20200967665872, 89.96918079583351), (1.0, 0.362438, 0.946837), "PWM_Quarry_8x8x8_A23", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5021.3613, 3455.7974, 2938.8386), (-0.998623918900405, 49.562807667465805, 90.04591640264199), (1.0, 0.44440672, 0.946837), "PWM_Quarry_8x8x8_A24", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4618.8936, 2983.5615, 2973.3938), (-3.6260984696455325, 49.56049223169149, 87.7723201544741), (1.0, 0.362438, 0.946837), "PWM_Quarry_8x8x8_A25", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5492.555, 5993.9697, 1864.6378), (-0.39245608596868214, 47.823429492051304, -177.20101040521735), (1.0, 1.0, 0.4495409), "PWM_Quarry_8x8x8_A26_668", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5997.1753, 5479.239, 1869.467), (0.271998355134093, 36.02974635412803, 174.03897614195245), (1.0, 1.0, 0.449541), "PWM_Quarry_8x8x8_A27", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5322.127, 5657.3716, 2361.9426), (2.0424520884975004, -35.63656692565751, -12.243988941102463), (0.9231454, 0.43547508, 0.798752), "PWM_Quarry_8x8x8_A28_691", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5801.3374, 3753.5496, 2823.2717), (3.897560526163268e-06, -92.20008710190052, -75.65008755821155), (1.0, 0.18842117, 1.0), "PWM_Quarry_8x8x8_A29_711", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5897.97, 255.4763, 1200.0), (0.0, -53.12496432923651, 0.0), (0.625, 1.0, 1.0), "PWM_Quarry_8x8x8_A3", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5808.854, 4424.2217, 2751.9956), (1.4436423183061464, -69.2006530540796, -73.90386738273345), (1.0, 0.188421, 1.0), "PWM_Quarry_8x8x8_A30", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5078.1157, 4151.908, 2947.0632), (-0.9107054847567817, -168.76769782483817, -91.30953328343134), (1.0, 0.2809704, 1.0), "PWM_Quarry_8x8x8_A31", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4088.0044, 6169.2324, 2716.524), (-1.0800474716431263, 177.13048784505972, -162.084336297291), (1.0, 0.67192376, 0.41685545), "PWM_Quarry_8x8x8_A32_740", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3175.313, 6214.9805, 2724.3997), (-1.0800474716431263, 177.13048784505972, -162.084336297291), (1.0, 0.671924, 0.416855), "PWM_Quarry_8x8x8_A33", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2258.0566, 6161.217, 2748.6064), (1.4512306529336665, -169.06478387258755, 31.999748743301026), (1.0, 0.671924, 0.416855), "PWM_Quarry_8x8x8_A34", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (881.5708, 2895.9133, 2812.4653), (77.05064093598554, -166.46268485175767, 13.20448129415836), (0.45123762, 1.0, 1.0), "PWM_Quarry_8x8x8_A35", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1678.7798, 2897.9458, 2904.9297), (88.07890462813, -171.85401677110357, -83.0919099192599), (0.260567, 1.0, 1.0), "PWM_Quarry_8x8x8_A36", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5275.302, 5001.5845, 2795.032), (-1.3307496473088498, 124.04003531429458, -106.36928448747162), (1.0, 0.28055438, 1.0), "PWM_Quarry_8x8x8_A37", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4644.6606, 5597.2197, 2799.504), (74.47663064310458, 34.89903027228684, 169.54274770709776), (0.23004493, 0.83033025, 1.0), "PWM_Quarry_8x8x8_A38", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4685.5376, 4607.0205, 2931.9268), (1.5618574721976446, -55.93991467739507, 94.51032112921054), (1.0, 0.280554, 1.0), "PWM_Quarry_8x8x8_A39", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (6317.1562, 723.19104, 1200.0), (0.0, -127.49967506854311, 0.0), (1.0, 0.59375, 1.0), "PWM_Quarry_8x8x8_A4", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4139.582, 4238.7764, 2956.9868), (1.5618615394206494, -55.93908882201374, 90.55609390226583), (1.0, 0.280554, 1.0), "PWM_Quarry_8x8x8_A40", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2397.6333, 281.79453, 2673.6108), (1.6446958584303604, -4.7944035189798875, 18.89175807936357), (0.55847704, 0.40821028, 0.40821028), "PWM_Quarry_8x8x8_A41_819", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (880.0837, 2200.993, 2770.6484), (-77.3968573456662, -0.3841838283820942, 8.522570945939476), (0.33818892, 1.0, 1.0), "PWM_Quarry_8x8x8_A42", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (978.46875, 1461.8718, 2793.687), (80.82012976105922, 174.5148461927577, 162.61036352403667), (0.260567, 1.0, 1.0), "PWM_Quarry_8x8x8_A43", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3452.102, 6272.1826, 2680.7905), (-1.0800474716431263, 177.13048784505972, -162.084336297291), (1.0, 0.671924, 0.416855), "PWM_Quarry_8x8x8_A44", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2660.65, 6272.1826, 2680.7905), (-1.0800171558072567, -169.66647560712966, -162.0841786171619), (1.0, 0.671924, 0.416855), "PWM_Quarry_8x8x8_A45", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5311.4043, 162.45618, 1200.0), (0.0, -92.49908988123724, 0.0), (0.5625, 1.163341, 1.7304744), "PWM_Quarry_8x8x8_A5", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (6144.923, 1439.0663, 1228.3954), (0.0, -27.636840304791658, 0.0), (0.6271043, 0.6271043, 1.1003894), "PWM_Quarry_8x8x8_A6", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (6202.318, 5108.019, 1199.9995), (0.0, -40.312438760705845, 0.0), (0.3891703, 0.7641703, 1.3293406), "PWM_Quarry_8x8x8_A7", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (6150.87, 5946.265, 1188.0), (0.0, -51.562438350312675, 0.0), (1.0, 0.5083237, 1.0), "PWM_Quarry_8x8x8_A8", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5488.1157, 6416.38, 1200.0), (0.0, -91.87493125921762, 0.0), (0.65625, 1.0, 1.0), "PWM_Quarry_8x8x8_A9", _folder)
if a: placed += 1
else: skipped += 1

# Batch 127: StaticMesh'PWM_Quarry_Ceilling_Fissure_8x4_A' (4 instances)
_mesh_path = "/Game/Unshippable/Whitebox/Rocks/Meshes/PWM_Quarry_Ceilling_Fissure_8x4_A"
_materials = ['/Game/Environments/ProcTexturing/ProcMaterial_Quarry_Floor_8x4x1']
_folder = "Reconstruction/BD_BB_Chapter2_Orctown_Throne/Meshes"
a = spawn_static_mesh(_mesh_path, _materials, (5385.0, 412.0, 1677.0), (2.265778445060996, 0.0, -0.0), (1.0, 1.0, 1.0), "PWM_Quarry_Ceilling_Fissure_8x4_A_511", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (6019.7207, 1066.0231, 1680.802), (2.0320151294109277, -26.26022243796003, 5.422901035999704), (1.0, 1.0, 1.0), "PWM_Quarry_Ceilling_Fissure_8x4_A2", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1719.9358, 5797.0522, 2623.3743), (-1.721711682801109, 28.448714803731995, -107.5786963234294), (1.0, 1.0, 1.0), "PWM_Quarry_Ceilling_Fissure_8x4_A3_751", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5746.3857, 1850.4653, 2684.9148), (1.4374911651731302e-05, 60.01766904899709, -32.56939567129574), (1.0, 1.0, 1.0), "PWM_Quarry_Ceilling_Fissure_8x4_A4_978", _folder)
if a: placed += 1
else: skipped += 1

# Batch 128: StaticMesh'PWM_Quarry_Ceilling_Fissure_8x4_B' (1 instances)
_mesh_path = "/Game/Unshippable/Whitebox/Rocks/Meshes/PWM_Quarry_Ceilling_Fissure_8x4_B"
_materials = ['/Game/Environments/ProcTexturing/ProcMaterial_Quarry_Ceilling_Fissure_8x8']
_folder = "Reconstruction/BD_BB_Chapter2_Orctown_Throne/Meshes"
a = spawn_static_mesh(_mesh_path, _materials, (5753.089, 4874.9673, 2578.8599), (-0.03991553518771185, 123.30999238921832, 141.02096351405842), (1.0, 1.0, 1.0), "PWM_Quarry_Ceilling_Fissure_8x4_B_975", _folder)
if a: placed += 1
else: skipped += 1

# Batch 129: StaticMesh'PWM_Quarry_Collapsed_Wall' (12 instances)
_mesh_path = "/Game/Unshippable/Whitebox/Rocks/Meshes/PWM_Quarry_Collapsed_Wall"
_materials = ['/Game/Environments/ProcTexturing/ProcMaterial_Quarry_1m_C', '/Game/Environments/ProcTexturing/ProcMaterial_Quarry_2m']
_folder = "Reconstruction/BD_BB_Chapter2_Orctown_Throne/Meshes"
a = spawn_static_mesh(_mesh_path, _materials, (6007.7637, 2249.9868, 2580.2695), (-3.145628604985644e-07, -101.38167629770045, -12.00460714775447), (1.0, 0.73954767, 1.0), "PWM_Quarry_Collapsed_Wall_629", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5354.5864, 5413.6777, 2396.1213), (-7.614867681109234, 127.55631796806848, 54.372081364079115), (1.4541738, 1.0, 1.0), "PWM_Quarry_Collapsed_Wall10_972", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2404.2476, 5438.397, 659.4091), (0.0, 15.991322184828167, -0.0), (0.5763459, 1.0, 1.0), "PWM_Quarry_Collapsed_Wall11_1103", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (683.5368, 4637.203, 1689.1854), (3.07136890296342e-08, -98.51733859584505, 4.204739974705126), (1.4611664, 1.0, 2.1616359), "PWM_Quarry_Collapsed_Wall12_1116", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5836.1177, 4817.886, 2514.0), (0.0, -67.1776120285647, 0.0), (0.620861, 0.620861, 0.620861), "PWM_Quarry_Collapsed_Wall2_698", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5976.7866, 4563.535, 2514.0), (0.0, -67.1776120285647, 0.0), (0.620861, 0.620861, 0.620861), "PWM_Quarry_Collapsed_Wall3", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5334.0166, 5602.319, 1910.1787), (-0.5622863557280054, -41.346830381275495, -4.340850094036823), (1.0, 0.7274599, 1.5231572), "PWM_Quarry_Collapsed_Wall4_720", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4762.1323, 5857.87, 2562.4814), (6.843230961331334e-08, -26.84078758715422, -7.149657763389929), (1.0, 1.0, 1.0), "PWM_Quarry_Collapsed_Wall5_737", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (734.6628, 1629.7141, 2545.6506), (2.90033469423852e-07, -67.91588407132394, 17.629424066051694), (0.61825657, 0.61825657, 0.61825657), "PWM_Quarry_Collapsed_Wall6_782", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1386.2953, 832.8755, 2675.9685), (4.018087283927485, 143.09687387179872, 170.9773440658803), (0.5826288, 0.5826288, 0.5826288), "PWM_Quarry_Collapsed_Wall7_788", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (555.69635, 4738.0615, 1436.0056), (-0.26119999636847846, -97.52479755929407, 179.8610125071229), (1.0, 1.0, 2.0071752), "PWM_Quarry_Collapsed_Wall8_916", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2273.1404, 5982.8545, 2642.9985), (-2.6761475330023634, 4.2501349624834885, -41.920716492136265), (1.2309904, 1.0, 0.80570734), "PWM_Quarry_Collapsed_Wall9_969", _folder)
if a: placed += 1
else: skipped += 1

# Batch 130: StaticMesh'PWM_Quarry_Floor_2x2x2_A' (9 instances)
_mesh_path = "/Game/Unshippable/Whitebox/Rocks/Meshes/PWM_Quarry_Floor_2x2x2_A"
_materials = ['/Game/Environments/ProcTexturing/ProcMaterial_Quarry_Atlas_3']
_folder = "Reconstruction/BD_BB_Chapter2_Orctown_Throne/Meshes"
a = spawn_static_mesh(_mesh_path, _materials, (684.7607, 4871.118, 2383.0977), (-19.550017752948143, -26.03194908522265, -3.4862961822121177), (0.49473333, 1.5388898, 1.5388898), "PWM_Quarry_Floor_2x2x2_A_587", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5701.6655, 1517.9745, 2563.2036), (34.311297343809684, -23.993379289725933, -3.2117009222193005), (0.3628444, 1.0, 1.0), "PWM_Quarry_Floor_2x2x2_A2_632", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5906.832, 2021.1737, 2588.3777), (34.402974548900396, -21.43987561663155, -1.7706906461249068), (0.362844, 1.445792, 1.0), "PWM_Quarry_Floor_2x2x2_A3", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5960.7627, 2207.3215, 2597.7727), (22.521423912809663, -13.537476021325526, 2.756069876503399), (0.362844, 1.445792, 1.0), "PWM_Quarry_Floor_2x2x2_A4", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5983.273, 2389.5366, 2603.484), (22.521426701677484, -13.538147329530767, -0.3059998374255731), (0.362844, 1.445792, 1.0), "PWM_Quarry_Floor_2x2x2_A5", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5749.5137, 1760.6909, 2628.3938), (34.2559316525546, -25.078796706915895, -3.824432074369855), (0.362844, 2.027426, 1.3400209), "PWM_Quarry_Floor_2x2x2_A6", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (6057.831, 2701.7725, 2656.6035), (72.2859531513601, -23.976629489624873, -3.814000439806004), (0.362844, 1.8758533, 1.6889173), "PWM_Quarry_Floor_2x2x2_A7", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (965.1129, 995.6674, 2596.1301), (-18.09192084618745, 37.62458836196001, 2.134863487939026e-05), (1.0091702, 2.5720348, 1.4040421), "PWM_Quarry_Floor_2x2x2_A8_794", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2022.6146, 435.9432, 2655.8936), (-12.352019422222057, 77.54069446116713, 1.7012530816871654), (1.00917, 2.572035, 1.404042), "PWM_Quarry_Floor_2x2x2_A9", _folder)
if a: placed += 1
else: skipped += 1

# Batch 131: StaticMesh'PWM_Quarry_Floor_4x4x4_A' (18 instances)
_mesh_path = "/Game/Unshippable/Whitebox/Rocks/Meshes/PWM_Quarry_Floor_4x4x4_A"
_materials = ['/Game/Environments/ProcTexturing/ProcMaterial_Quarry_Atlas_4']
_folder = "Reconstruction/BD_BB_Chapter2_Orctown_Throne/Meshes"
a = spawn_static_mesh(_mesh_path, _materials, (5543.3623, 1192.1035, 2292.3052), (12.205229108412324, -41.70504465729301, 0.8973083295885238), (0.20820987, 1.3599427, 1.6557022), "PWM_Quarry_Floor_4x4x4_A_540", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1992.0645, 3286.4524, 2888.0), (0.0, -50.994843309843084, 0.0), (1.588609, 1.474596, 0.192065), "PWM_Quarry_Floor_4x4x4_A10", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3999.8916, 3360.715, 2888.0), (0.0, -50.994843309843084, 0.0), (1.588609, 1.474596, 0.192065), "PWM_Quarry_Floor_4x4x4_A11", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3615.9626, 3834.7393, 2888.0), (0.0, -50.994843309843084, 0.0), (1.588609, 1.474596, 0.192065), "PWM_Quarry_Floor_4x4x4_A12", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3240.8455, 4297.8843, 2888.0), (0.0, -50.994843309843084, 0.0), (1.588609, 1.474596, 0.192065), "PWM_Quarry_Floor_4x4x4_A13", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (6123.1562, 3879.5613, 2606.5605), (10.826792109416438, 10.937742912154258, 4.988855810180337e-06), (0.26530832, 0.9769526, 0.5558124), "PWM_Quarry_Floor_4x4x4_A14_655", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (6081.5, 4232.6523, 2594.8242), (9.666664990222571, 14.389798941298166, 0.5802973215676108), (0.265308, 0.976953, 0.555812), "PWM_Quarry_Floor_4x4x4_A15", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (558.34485, 4540.2334, 2490.1611), (-22.91363635471209, -13.07006919944927, -2.6615906427340175), (0.5753562, 1.4302864, 1.3430908), "PWM_Quarry_Floor_4x4x4_A16_724", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2461.689, 4408.2646, 2888.0), (0.0, -50.994843309843084, 0.0), (1.588609, 1.474596, 0.192065), "PWM_Quarry_Floor_4x4x4_A17", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3371.3728, 2253.2966, 2888.0), (0.0, -50.994843309843084, 0.0), (1.588609, 1.474596, 0.192065), "PWM_Quarry_Floor_4x4x4_A18", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3583.3728, 3023.3596, 2888.0), (0.0, -50.994843309843084, 0.0), (1.5886087, 1.4745957, 0.19206476), "PWM_Quarry_Floor_4x4x4_A2_552", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3199.4436, 3497.3838, 2888.0), (0.0, -50.994843309843084, 0.0), (1.588609, 1.474596, 0.192065), "PWM_Quarry_Floor_4x4x4_A3", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2824.3264, 3960.5288, 2888.0), (0.0, -50.994843309843084, 0.0), (1.588609, 1.474596, 0.192065), "PWM_Quarry_Floor_4x4x4_A4", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3157.5283, 2678.4543, 2888.0), (0.0, -50.994843309843084, 0.0), (1.588609, 1.474596, 0.192065), "PWM_Quarry_Floor_4x4x4_A5", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2773.599, 3152.4785, 2888.0), (0.0, -50.994843309843084, 0.0), (1.588609, 1.474596, 0.192065), "PWM_Quarry_Floor_4x4x4_A6", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2398.482, 3615.6235, 2888.0), (0.0, -50.994843309843084, 0.0), (1.588609, 1.474596, 0.192065), "PWM_Quarry_Floor_4x4x4_A7", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2751.1106, 2349.2834, 2888.0), (0.0, -50.994843309843084, 0.0), (1.588609, 1.474596, 0.192065), "PWM_Quarry_Floor_4x4x4_A8", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2367.1814, 2823.3074, 2888.0), (0.0, -50.994843309843084, 0.0), (1.588609, 1.474596, 0.192065), "PWM_Quarry_Floor_4x4x4_A9", _folder)
if a: placed += 1
else: skipped += 1

# Batch 132: StaticMesh'PWM_Quarry_Floor_8x4x1_A' (5 instances)
_mesh_path = "/Game/Unshippable/Whitebox/Rocks/Meshes/PWM_Quarry_Floor_8x4x1_A"
_materials = ['/Game/Environments/ProcTexturing/ProcMaterial_Quarry_Atlas_6']
_folder = "Reconstruction/BD_BB_Chapter2_Orctown_Throne/Meshes"
a = spawn_static_mesh(_mesh_path, _materials, (2375.6323, 919.65643, 1120.0), (0.0, 171.56244177836916, -0.0), (1.0, 1.0, 1.0), "PWM_Quarry_Floor_8x4x1_A_409", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2220.0, 700.0, 1210.0), (0.0, -14.062865954320413, 0.0), (1.0, 1.0, 1.0), "PWM_Quarry_Floor_8x4x1_A2", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3109.9995, 410.0, 1180.0), (0.0, -165.93791768333702, 0.0), (1.0, 1.0, 1.0), "PWM_Quarry_Floor_8x4x1_A3", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4531.0405, 533.7338, 2610.0823), (-5.030395102783292, 18.65420311534654, -75.43798540689446), (1.0, 1.1435595, 1.0), "PWM_Quarry_Floor_8x4x1_A4_823", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2264.4634, 977.16425, 1120.0), (0.0, 157.49947902179517, -0.0), (1.0, 1.0, 1.0), "PWM_Quarry_Floor_8x4x1_A6", _folder)
if a: placed += 1
else: skipped += 1

# Batch 133: StaticMesh'PWM_Quarry_Floor_8x8x8_A' (2 instances)
_mesh_path = "/Game/Unshippable/Whitebox/Rocks/Meshes/PWM_Quarry_Floor_8x8x8_A"
_materials = ['/Game/Environments/ProcTexturing/ProcMaterial_Quarry_Atlas_6']
_folder = "Reconstruction/BD_BB_Chapter2_Orctown_Throne/Meshes"
a = spawn_static_mesh(_mesh_path, _materials, (6380.346, 2993.345, 1577.0352), (6.183411298566437, -5.228210557535965, -0.3385620337507773), (0.20888372, 1.0, 1.0), "PWM_Quarry_Floor_8x8x8_A_638", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (6269.0703, 2993.3445, 2254.9636), (16.30012400735579, -7.175170742035255, -0.8786926844862295), (0.208884, 1.0, 1.0), "PWM_Quarry_Floor_8x8x8_A2", _folder)
if a: placed += 1
else: skipped += 1

# Batch 134: StaticMesh'PWM_Quarry_RockDebris_A' (105 instances)
_mesh_path = "/Game/Unshippable/Whitebox/Rocks/Meshes/PWM_Quarry_RockDebris_A"
_materials = ['/Game/Environments/ProcTexturing/ProcMaterial_Quarry_Atlas_5']
_folder = "Reconstruction/BD_BB_Chapter2_Orctown_Throne/Meshes"
a = spawn_static_mesh(_mesh_path, _materials, (3647.0, 2038.0, 798.0), (0.0, 0.0, -0.0), (1.0, 1.0, 1.0), "PWM_Quarry_RockDebris_A_17", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4152.0, 4062.0, 794.0), (0.0, -15.000428211065243, 0.0), (1.0, 1.0, 1.0), "PWM_Quarry_RockDebris_A10", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5048.0, 3808.0, 800.0), (0.0, -160.00009742851447, 0.0), (1.0, 1.0, 1.0), "PWM_Quarry_RockDebris_A100", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4818.0, 4274.0, 794.0), (0.0, 134.9999263430944, -0.0), (1.0, 1.0, 1.0), "PWM_Quarry_RockDebris_A101", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4682.0, 4232.0, 795.0), (0.0, 34.99975125183201, -0.0), (1.0, 1.0, 1.0), "PWM_Quarry_RockDebris_A102", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3886.204, 4857.7153, 800.0), (7.000000635210417e-06, 15.00024385095131, 7.0000021195207775e-06), (1.0, 1.0, 1.0), "PWM_Quarry_RockDebris_A103", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2920.204, 4594.7153, 800.0), (7.000000261601242e-06, 15.00024385095131, 7.0000005677882e-06), (1.0, 1.0, 1.0), "PWM_Quarry_RockDebris_A104", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2477.204, 4907.7153, 800.0), (7.0000002228256564e-06, 145.000261253996, 7.000002413620026e-06), (1.0, 1.0, 1.0), "PWM_Quarry_RockDebris_A105", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4341.0, 4632.0, 798.0), (0.0, -175.00023147669577, 0.0), (1.0, 1.0, 1.0), "PWM_Quarry_RockDebris_A106", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4386.0, 3607.0, 802.0), (0.0, -15.000428211065243, 0.0), (1.0, 1.0, 1.0), "PWM_Quarry_RockDebris_A11_30", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4442.0, 3258.0, 793.0), (0.0, 59.99969647782352, -0.0), (1.0, 1.0, 1.0), "PWM_Quarry_RockDebris_A12", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4311.0, 2743.0, 797.0), (0.0, 89.99975996369572, -0.0), (1.0, 1.0, 1.0), "PWM_Quarry_RockDebris_A13", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2387.1814, 5976.4023, 1398.0), (0.0, 109.99951254230659, -0.0), (1.0, 1.0, 1.0), "PWM_Quarry_RockDebris_A14", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2381.7412, 5731.01, 1398.0), (0.0, 164.99951114003952, -0.0), (1.0, 1.0, 1.0), "PWM_Quarry_RockDebris_A15", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2433.4722, 5602.7207, 1398.2354), (0.0, -15.000488579615682, 0.0), (1.0, 1.0, 1.0), "PWM_Quarry_RockDebris_A16", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3706.0151, 6027.9917, 1398.0), (0.0, -90.0005702495585, 0.0), (1.0, 1.0, 1.0), "PWM_Quarry_RockDebris_A17", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4841.0, 5707.0, 803.0), (0.0, 0.0, -0.0), (1.0, 1.0, 1.0), "PWM_Quarry_RockDebris_A18_106", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3850.1436, 5325.412, 803.0), (0.0, 45.00005168692799, -0.0), (1.0, 1.0, 1.0), "PWM_Quarry_RockDebris_A19", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2847.0, 1995.0, 795.0), (-0.016143911041613807, 60.002403827473024, -0.9303282523535326), (1.0, 1.0, 1.0), "PWM_Quarry_RockDebris_A2", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3647.204, 5365.7163, 793.25555), (6.830189162594522e-06, -84.9998806918081, 6.67572076757874e-06), (1.0, 1.0, 1.3403451), "PWM_Quarry_RockDebris_A20", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2676.119, 5347.3013, 803.0), (0.0, 95.00004479164929, -0.0), (1.0, 1.0, 1.0), "PWM_Quarry_RockDebris_A21", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2534.8706, 5246.418, 803.0), (6.9999996845631406e-06, -34.999633248642525, 7.000001456401772e-06), (1.0, 1.0, 1.0), "PWM_Quarry_RockDebris_A22", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2306.2903, 5172.899, 803.0), (6.999999950110695e-06, -179.99963116978645, 7.0000003205148e-06), (1.0, 1.0, 1.0), "PWM_Quarry_RockDebris_A23", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1547.0615, 4646.821, 803.0), (6.999999969024581e-06, 55.00037926325424, 7.000001937570456e-06), (1.0, 1.0, 1.0), "PWM_Quarry_RockDebris_A24", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1382.1343, 4457.4185, 803.0), (1.3660376739157286e-05, -169.9988791167625, 2.3671236061730277e-05), (1.0, 1.0, 1.0), "PWM_Quarry_RockDebris_A25", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1263.3652, 4324.7734, 802.99976), (1.399999884416816e-05, -169.99887911676242, 2.4000000103459173e-05), (1.0, 1.0, 1.0), "PWM_Quarry_RockDebris_A26", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3189.219, 5276.7437, 797.0), (0.0, 95.00004479164929, -0.0), (1.0, 1.0, 1.0), "PWM_Quarry_RockDebris_A28", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2977.3088, 5342.9653, 797.0), (0.0, 19.999961671167853, -0.0), (1.0, 1.0, 1.0), "PWM_Quarry_RockDebris_A29", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3351.0, 2004.0, 798.0), (0.0, 29.999512351053546, -0.0), (1.0, 1.0, 1.0), "PWM_Quarry_RockDebris_A3", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3413.363, 5296.355, 794.0), (0.0, -20.000060948281234, 0.0), (1.0, 1.0, 1.0), "PWM_Quarry_RockDebris_A30", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3467.8914, 6065.14, 1398.0), (0.0, 169.99952414215744, -0.0), (1.0, 1.0, 1.0), "PWM_Quarry_RockDebris_A31", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3517.4019, 5625.4185, 1398.6093), (0.0, -55.000485945860966, 0.0), (1.0, 1.0, 1.0), "PWM_Quarry_RockDebris_A32", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3593.5608, 5806.983, 1399.0), (0.0, 84.99957925053056, -0.0), (1.0, 1.0, 1.0), "PWM_Quarry_RockDebris_A33", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2436.8914, 6006.14, 1398.0), (0.0, -80.00039659510229, 0.0), (1.0, 1.0, 1.0), "PWM_Quarry_RockDebris_A34", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3244.5608, 6052.983, 1396.1448), (0.0, 84.99957925053056, -0.0), (1.0, 1.0, 1.0), "PWM_Quarry_RockDebris_A35", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2644.5608, 6052.983, 1397.4807), (0.0, 4.999511640029441, -0.0), (1.0, 1.0, 1.0), "PWM_Quarry_RockDebris_A36", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2154.7412, 5833.01, 1398.0), (0.0, 39.99951114742062, -0.0), (1.0, 1.0, 1.0), "PWM_Quarry_RockDebris_A37", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1905.7412, 5623.01, 1398.0), (0.0, -55.000485945860966, 0.0), (1.0, 1.0, 1.0), "PWM_Quarry_RockDebris_A38", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1132.4445, 4306.446, 802.99994), (6.999999826072086e-06, -34.99941918131016, 2.4343665687711728e-05), (1.0, 1.0, 1.0), "PWM_Quarry_RockDebris_A39", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2063.0, 2812.0, 798.0), (0.0, 29.999512351053546, -0.0), (1.0, 1.0, 1.0), "PWM_Quarry_RockDebris_A4", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (943.0421, 4471.3735, 803.0), (4.0981128601231104e-05, 100.00099837949584, 2.4000016110443804e-05), (1.0, 1.0, 1.0), "PWM_Quarry_RockDebris_A40", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (810.39685, 4590.143, 802.99976), (4.0981128601231104e-05, 100.00099837949584, 2.4000016110443804e-05), (1.0, 1.0, 1.0), "PWM_Quarry_RockDebris_A41", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1019.88965, 4535.8564, 822.41907), (4.078867190211228e-05, 130.00091436139104, 24.998080508126545), (1.0, 1.0, 1.0), "PWM_Quarry_RockDebris_A42", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (833.29675, 4757.8545, 822.9195), (4.208224180021396, -40.91952038079932, -24.66180382136171), (1.0, 1.0, 1.0), "PWM_Quarry_RockDebris_A43", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (884.19794, 1629.0906, 803.0091), (0.0006147169696051965, -149.9990512995321, 9.021856501204528e-05), (1.0, 1.0, 1.0), "PWM_Quarry_RockDebris_A44", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1147.925, 1826.477, 803.0059), (4.0999998983011464e-05, 0.001373290979453065, 0.0001884860849292964), (1.0, 1.0, 1.0), "PWM_Quarry_RockDebris_A45", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1287.9236, 1936.4825, 803.00415), (-0.00012207030653449256, 75.00149830892319, 0.00021965239098067918), (1.0, 1.0, 1.0), "PWM_Quarry_RockDebris_A46", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1046.307, 1679.5006, 825.5659), (-9.99957289373361, 130.00098181409547, -0.0006102535323576461), (1.0, 1.0, 1.0), "PWM_Quarry_RockDebris_A47", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2212.2795, 1122.956, 791.25806), (7.000000693771189e-06, -74.99901800642546, 1.8849236794366574e-05), (1.0, 1.0, 1.8945879), "PWM_Quarry_RockDebris_A48", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1989.9152, 1213.5652, 802.99976), (6.999999332308517e-06, 140.00028566576609, 1.037961997452568e-05), (1.0, 1.0, 1.0), "PWM_Quarry_RockDebris_A49", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2037.0, 3587.0, 795.09875), (0.0, -90.0005702495585, 0.0), (1.0, 1.0, 1.0), "PWM_Quarry_RockDebris_A5", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2600.302, 1075.366, 802.99976), (7.00000349804366e-06, 105.00087846005833, 6.745569122365147e-05), (1.0, 1.0, 1.0), "PWM_Quarry_RockDebris_A50", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2822.663, 984.75525, 795.2875), (1.3660377375023637e-05, -39.99981879435383, 1.0000002660438265e-05), (1.0, 1.0, 1.6316146), "PWM_Quarry_RockDebris_A51", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4689.356, 994.5007, 796.89905), (4.098113161505728e-05, -99.99917291857764, 6.700000528478651e-05), (1.1551723, 1.1551723, 1.5797521), "PWM_Quarry_RockDebris_A52", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4526.125, 1170.594, 802.99976), (1.3999999878208258e-05, 115.00013467968122, 4.365012718653741e-05), (1.0, 1.0, 1.0), "PWM_Quarry_RockDebris_A53", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4815.9756, 823.8706, 802.99976), (4.099999554154404e-05, -19.998779621966925, 0.00011746526104676747), (1.0, 1.0, 1.0), "PWM_Quarry_RockDebris_A54", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5342.633, 1707.0287, 795.4994), (4.099999787364282e-05, -64.99901961631417, 0.00014772941555643291), (1.0, 1.0, 1.2812407), "PWM_Quarry_RockDebris_A55", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5092.9434, 1801.3489, 796.62946), (4.098112703423821e-05, 150.0000890653684, 4.400012132391487e-05), (1.0, 1.0, 1.1500375), "PWM_Quarry_RockDebris_A56", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5562.9336, 1587.9227, 795.9659), (4.1000003018367925e-05, 15.001418692875184, 0.00013863894805850752), (1.0, 1.0, 1.1720221), "PWM_Quarry_RockDebris_A57", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5600.57, 1732.6895, 855.08997), (24.999987636791715, 65.00411779544416, 10.000686355366584), (1.0, 1.0, 1.0), "PWM_Quarry_RockDebris_A58", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4577.0005, 5155.551, 803.0), (-5.487307907264645e-13, -50.00006299960988, 1.608201113023267e-05), (1.0, 1.0, 1.0), "PWM_Quarry_RockDebris_A59", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2017.0, 3335.0, 798.0), (0.0, -90.0005702495585, 0.0), (1.0, 1.0, 1.0), "PWM_Quarry_RockDebris_A6", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4611.839, 5283.2065, 802.0), (7.000001913504515e-06, -179.9998019245729, 7.000026685995237e-06), (1.0, 1.0, 1.0), "PWM_Quarry_RockDebris_A60", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4744.7725, 5482.999, 803.0), (-2.1179407853670298e-13, 100.00013657266743, 1.6000002798816486e-05), (1.0, 1.0, 1.0), "PWM_Quarry_RockDebris_A61", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5174.16, 4523.7603, 802.99994), (-3.6002454991513595e-13, -79.99929074058461, 1.5999999138104497e-05), (1.0, 1.0, 1.0), "PWM_Quarry_RockDebris_A62", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5341.9683, 4724.335, 801.99994), (6.9999996517088815e-06, 90.00029475174414, 1.517640021860137e-05), (1.0, 1.0, 1.0), "PWM_Quarry_RockDebris_A63", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5665.2817, 4846.4004, 802.99994), (-2.0487884356672615e-13, 84.99989914013322, 1.5999999898085642e-05), (1.0, 1.0, 1.0), "PWM_Quarry_RockDebris_A64", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5348.035, 4497.118, 846.32446), (-1.7358407054497074e-07, 20.001044699773683, 24.99929693624748), (1.0, 1.0, 1.0), "PWM_Quarry_RockDebris_A65", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5383.0, 3107.0, 804.0), (0.0, 90.00001925454748, -0.0), (1.0, 1.0, 1.0), "PWM_Quarry_RockDebris_A66", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5383.0, 2830.0, 802.0), (0.0, -135.0000537473682, 0.0), (1.0, 1.0, 1.0), "PWM_Quarry_RockDebris_A67", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (618.0443, 2229.0154, 796.12213), (0.0005942263719850727, 105.00090680712067, 0.00048737153855360856), (1.0, 1.0, 1.0), "PWM_Quarry_RockDebris_A68", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (687.38666, 1957.2837, 795.1167), (6.147168572060304e-05, -104.99868509120864, -0.0003967284910801118), (1.0, 1.0, 1.0), "PWM_Quarry_RockDebris_A69", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1981.0, 3081.0, 801.0), (0.0, -30.000427654248686, 0.0), (1.0, 1.0, 1.0), "PWM_Quarry_RockDebris_A7", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (673.3951, 1700.0596, 803.00244), (0.00027320752368925703, -29.998443070013224, 3.3827876268434454e-05), (1.0, 1.0, 1.0), "PWM_Quarry_RockDebris_A70", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (660.38605, 4501.941, 802.9998), (4.100000354588005e-05, -89.99886865587993, 0.000135199893956991), (1.0, 1.0, 1.0), "PWM_Quarry_RockDebris_A71", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (636.41815, 4217.886, 802.9996), (4.0999996794714585e-05, -129.9988412814747, 0.0001103159520696888), (1.0, 1.0, 1.0), "PWM_Quarry_RockDebris_A72", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5334.4326, 3693.9138, 800.0), (0.0, -10.000030597161448, 0.0), (1.0, 1.0, 1.0), "PWM_Quarry_RockDebris_A73_250", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5369.0156, 3443.239, 803.0), (0.0, -139.99998729747986, 0.0), (1.0, 1.0, 1.0), "PWM_Quarry_RockDebris_A74", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2971.6023, 6109.3555, 1410.3333), (3.49047207859776, -176.96472442599628, -9.916288565877558), (0.5364848, 0.5364848, 1.4425566), "PWM_Quarry_RockDebris_A75", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2894.1077, 6027.452, 1416.7013), (2.5356445791658, -176.13118542029449, 5.832819107542101), (0.536485, 0.536485, 1.1336722), "PWM_Quarry_RockDebris_A76", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5839.0947, 2479.8374, 1321.3613), (29.73167689227708, 67.49491570534998, 1.2241083575053235), (1.0, 1.0, 1.0), "PWM_Quarry_RockDebris_A77", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5836.9634, 1915.428, 1018.73584), (-29.689877958536407, -108.20674992861986, -16.928340833112028), (1.0, 1.0, 1.0), "PWM_Quarry_RockDebris_A78", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5294.051, 1917.3412, 847.55237), (0.00010291519612489475, -24.99691970441091, -29.999451657932), (1.0, 1.0, 1.0), "PWM_Quarry_RockDebris_A79", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2821.0, 4348.0, 798.0), (0.0, -90.0005702495585, 0.0), (1.0, 1.0, 1.0), "PWM_Quarry_RockDebris_A8", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (760.02374, 3391.3765, 797.02075), (0.0005939999151083783, 105.00090680711513, 0.0004870000030722036), (1.0, 1.0, 1.0), "PWM_Quarry_RockDebris_A80", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1195.9338, 3932.9492, 795.02966), (-0.0005187988161216955, -159.99907097312638, 0.0005854563746581027), (1.0, 1.0, 1.0), "PWM_Quarry_RockDebris_A81", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1516.4814, 3686.7334, 789.35406), (0.0, -159.99907096956258, 0.0), (1.0, 1.0, 1.1612253), "PWM_Quarry_RockDebris_A82", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1185.643, 2986.9412, 797.0), (6.999999693366414e-06, 55.00037926325424, 6.999999985429257e-06), (1.0, 1.0, 1.0), "PWM_Quarry_RockDebris_A83", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (947.314, 2949.2144, 797.0), (1.3660378565643549e-05, -174.9991175213375, 2.1904660881487728e-05), (1.0, 1.0, 1.0), "PWM_Quarry_RockDebris_A84", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (949.7078, 2483.4421, 795.7042), (1.399999906278694e-05, -89.99902260853631, 3.983734086956687e-05), (1.0, 1.0, 1.0), "PWM_Quarry_RockDebris_A85", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (768.8941, 2656.7666, 795.9999), (1.399999886273643e-05, 30.001187780643004, 6.238231227727025e-05), (1.0, 1.0, 1.0), "PWM_Quarry_RockDebris_A86", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1862.7012, 2897.4573, 796.9994), (1.3999997676877201e-05, -89.99902260853634, 3.999999417457995e-05), (1.0, 1.0, 1.0), "PWM_Quarry_RockDebris_A87", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1536.4712, 2919.1704, 799.99963), (1.4000001359619468e-05, 25.001160020098983, 6.135543372292655e-05), (1.0, 1.0, 1.0), "PWM_Quarry_RockDebris_A88", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1353.8169, 2416.962, 796.00006), (8.879245788997027e-05, -144.99892023119577, -0.00015258788903332288), (1.0, 1.0, 1.0), "PWM_Quarry_RockDebris_A89", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3620.0, 4350.0, 805.0), (0.0, -15.000428211065243, 0.0), (1.0, 1.0, 1.0), "PWM_Quarry_RockDebris_A9", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1202.5522, 3415.4365, 794.9988), (0.00010245283024509158, -44.99865402514166, 0.000226879504606297), (1.0, 1.0, 1.0), "PWM_Quarry_RockDebris_A90", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2490.33, 1464.5677, 794.88885), (7.000000032059626e-06, -19.998902717619785, 2.465889833838459e-05), (1.0, 1.0, 1.2202593), "PWM_Quarry_RockDebris_A91", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3056.9692, 1921.9883, 792.48846), (7.000000883409362e-06, 40.00091708129983, 3.089202499936727e-05), (1.0, 1.0, 1.4480714), "PWM_Quarry_RockDebris_A92", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3471.698, 1277.4445, 794.07385), (6.999999513799935e-06, 120.00086068094959, 3.845174470811167e-05), (1.0, 1.0, 1.2807893), "PWM_Quarry_RockDebris_A93", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3145.3694, 1287.0049, 798.73224), (1.366037700643047e-05, -119.99901634683127, 4.726971955008071e-05), (1.0, 1.0, 1.2504703), "PWM_Quarry_RockDebris_A94", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4129.698, 1491.4463, 795.94855), (7.000000690283305e-06, -154.99909544522816, 3.8000005076735184e-05), (1.0, 1.0, 1.2690743), "PWM_Quarry_RockDebris_A95", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4702.698, 1596.4459, 796.9998), (0.0, -24.998748982141926, 0.0), (1.0, 1.0, 1.0), "PWM_Quarry_RockDebris_A96", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4989.7437, 2391.935, 795.9998), (6.999999520253639e-06, -169.99917522755192, 3.80000059011473e-05), (1.0, 1.0, 1.0), "PWM_Quarry_RockDebris_A97", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5119.698, 3179.4458, 793.9998), (7.000000451693068e-06, -84.99901952852652, 3.799999746037158e-05), (1.0, 1.0, 1.0), "PWM_Quarry_RockDebris_A98", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4864.7437, 2097.935, 793.9998), (0.0, -104.999153607135, 0.0), (1.0, 1.0, 1.0), "PWM_Quarry_RockDebris_A99", _folder)
if a: placed += 1
else: skipped += 1

# Batch 135: StaticMesh'PWM_Quarry_RockDebris_A_Optimized' (18 instances)
_mesh_path = "/Game/Unshippable/Whitebox/Rocks/Meshes/PWM_Quarry_RockDebris_A_Optimized"
_materials = ['/Game/Environments/ProcTexturing/ProcMaterial_Quarry_RockDebris_A']
_folder = "Reconstruction/BD_BB_Chapter2_Orctown_Throne/Meshes"
a = spawn_static_mesh(_mesh_path, _materials, (1922.0, 2190.0, 796.0), (0.0, 0.0, -0.0), (1.0, 1.0, 1.0), "BP_DM_PWM_Quarry_RockDebris_A_Breakable_2", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2305.7603, 443.94736, 1398.0), (0.0, 74.99955205217042, -0.0), (1.0, 1.0, 1.0), "BP_DM_PWM_Quarry_RockDebris_A_Breakable10", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2827.3818, 377.67734, 1398.0), (0.0, -15.000579204700644, 0.0), (1.0, 1.0, 1.0), "BP_DM_PWM_Quarry_RockDebris_A_Breakable11", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2592.1296, 423.11856, 1398.0), (0.0, 164.99966902522178, -0.0), (1.0, 1.0, 1.0), "BP_DM_PWM_Quarry_RockDebris_A_Breakable12", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2471.0415, 434.86057, 1399.0), (0.0, 74.99955205217042, -0.0), (1.0, 1.0, 1.0), "BP_DM_PWM_Quarry_RockDebris_A_Breakable13", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1773.9358, 812.14417, 1398.0), (0.0, -15.000579204700644, 0.0), (1.0, 1.0, 1.0), "BP_DM_PWM_Quarry_RockDebris_A_Breakable14", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3062.3123, 327.1537, 1398.0), (0.0, 74.99955205217042, -0.0), (1.0, 1.0, 1.0), "BP_DM_PWM_Quarry_RockDebris_A_Breakable15", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3667.897, 392.6414, 1398.0), (0.0, -15.000579204700644, 0.0), (1.0, 1.0, 1.0), "BP_DM_PWM_Quarry_RockDebris_A_Breakable16", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3262.4177, 297.346, 1398.0), (0.0, 164.99966902522178, -0.0), (1.0, 1.0, 1.0), "BP_DM_PWM_Quarry_RockDebris_A_Breakable17", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2662.7346, 664.534, 1394.0), (0.0, -25.0004255320871, 0.0), (1.0, 1.0, 1.0), "BP_DM_PWM_Quarry_RockDebris_A_Breakable18", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2215.0, 1953.0, 793.3117), (0.0, -90.0001164887758, 0.0), (1.0, 1.0, 1.2317336), "BP_DM_PWM_Quarry_RockDebris_A_Breakable2", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4410.9395, 2229.065, 796.0), (0.0, -90.0001164887758, 0.0), (1.0, 1.0, 1.0), "BP_DM_PWM_Quarry_RockDebris_A_Breakable3", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4173.939, 1936.0651, 796.0), (0.0, 179.99976777355934, -0.0), (1.0, 1.0, 1.0), "BP_DM_PWM_Quarry_RockDebris_A_Breakable4", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4172.0, 4390.0, 796.0), (0.0, 0.0, -0.0), (1.0, 1.0, 1.0), "BP_DM_PWM_Quarry_RockDebris_A_Breakable5", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4465.0, 4153.0, 796.0), (0.0, -90.00009542133918, 0.0), (1.0, 1.0, 1.0), "BP_DM_PWM_Quarry_RockDebris_A_Breakable6", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2210.9395, 4479.065, 796.0), (0.0, -90.00002735739477, 0.0), (1.0, 1.0, 1.0), "BP_DM_PWM_Quarry_RockDebris_A_Breakable7", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1973.939, 4186.0654, 796.0), (0.0, 179.99976777355934, -0.0), (1.0, 1.0, 1.0), "BP_DM_PWM_Quarry_RockDebris_A_Breakable8", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2073.939, 506.06506, 1398.0), (0.0, 164.99966902522178, -0.0), (1.0, 1.0, 1.0), "BP_DM_PWM_Quarry_RockDebris_A_Breakable9", _folder)
if a: placed += 1
else: skipped += 1

# Batch 136: StaticMesh'PWM_Quarry_RockDebris_B' (5 instances)
_mesh_path = "/Game/Unshippable/Whitebox/Rocks/Meshes/PWM_Quarry_RockDebris_B"
_materials = ['/Game/Unshippable/Cinematics/Cine002/Environments/Materials/ProcMaterial_Quarry_RockDebris_A']
_folder = "Reconstruction/BD_BB_Chapter2_Orctown_Throne/Meshes"
a = spawn_static_mesh(_mesh_path, _materials, (2076.408, 1223.3004, 794.03687), (0.0, 0.0, -0.0), (1.0, 1.0, 1.0), "PWM_Quarry_RockDebris_B_60", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2703.9111, 1131.0928, 809.9258), (0.0, 0.0, -0.0), (1.1701372, 1.2841542, 0.9005458), "PWM_Quarry_RockDebris_B2", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2566.8018, 1032.5674, 809.9258), (0.0, 0.0, -0.0), (1.170137, 1.284154, 0.900546), "PWM_Quarry_RockDebris_B3", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3553.0479, 1071.9559, 809.13086), (0.0, 173.9055469435897, -0.0), (0.85990345, 0.9739203, 0.5903124), "PWM_Quarry_RockDebris_B4", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5356.9824, 2853.618, 808.50006), (0.0, 0.0, -0.0), (1.0, 1.0, 0.33618927), "PWM_Quarry_RockDebris_B5_69", _folder)
if a: placed += 1
else: skipped += 1

# Batch 137: StaticMesh'PWM_Quarry_RockDebris_C' (14 instances)
_mesh_path = "/Game/Unshippable/Whitebox/Rocks/Meshes/PWM_Quarry_RockDebris_C"
_materials = ['/Game/Environments/ProcTexturing/ProcMaterial_Quarry_RockDebris_A']
_folder = "Reconstruction/BD_BB_Chapter2_Orctown_Throne/Meshes"
a = spawn_static_mesh(_mesh_path, _materials, (4000.0, 3650.0, 800.0), (0.0, -60.000092633621556, 0.0), (2.0, 2.0, 2.0), "PWM_Quarry_RockDebris_C_3", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3899.9985, 2650.0005, 800.0), (0.0, 90.00060266115494, -0.0), (2.0, 2.0, 2.0), "PWM_Quarry_RockDebris_C11", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3700.0, 2450.0, 800.0), (0.0, 150.00023288679367, -0.0), (2.0, 2.0, 2.0), "PWM_Quarry_RockDebris_C12", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3934.527, 5872.572, 1317.6603), (-13.67962567022176, -106.20218148527373, 29.099875679389914), (1.0, 1.0, 1.0), "PWM_Quarry_RockDebris_C13", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (600.0, 4795.0, 805.0), (0.0, 0.0, -0.0), (1.0, 1.0, 1.0), "PWM_Quarry_RockDebris_C16_127", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3700.0, 3950.0, 800.0), (0.0, 75.00009718089603, -0.0), (2.0, 2.0, 2.0), "PWM_Quarry_RockDebris_C2", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3045.9985, 6061.3257, 1398.1509), (0.0, 0.0, -0.0), (1.0, 1.0, 1.0), "PWM_Quarry_RockDebris_C20", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2860.9985, 6061.3257, 1398.1509), (0.0, -140.0000576472962, 0.0), (1.0, 1.0, 1.0), "PWM_Quarry_RockDebris_C21", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2749.9995, 4000.0, 800.0), (0.0, 60.0000059583233, -0.0), (2.0, 2.0, 2.0), "PWM_Quarry_RockDebris_C4", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2450.0005, 3700.0, 800.0), (0.0, 165.0001896592494, -0.0), (2.0, 2.0, 2.0), "PWM_Quarry_RockDebris_C5", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2600.0, 3850.0, 800.0), (0.0, -29.99999868431647, 0.0), (2.0, 2.0, 2.0), "PWM_Quarry_RockDebris_C6", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2449.9995, 2699.9988, 800.0), (0.0, 150.0000766038294, -0.0), (2.0, 2.0, 2.0), "PWM_Quarry_RockDebris_C7", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2750.0005, 2400.0012, 800.0), (0.0, -104.99963376897347, 0.0), (2.0, 2.0, 2.0), "PWM_Quarry_RockDebris_C8", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2600.0, 2550.0, 800.0), (0.0, 60.00012555116613, -0.0), (2.0, 2.0, 2.0), "PWM_Quarry_RockDebris_C9", _folder)
if a: placed += 1
else: skipped += 1

# Batch 138: StaticMesh'SM_Debris_Floor_01' (27 instances)
_mesh_path = "/Game/Unshippable/Whitebox/Rocks/Meshes/SM_Debris_Floor_01"
_materials = ['/Game/Environments/ProcTexturing/ProcMaterial_Quarry_RockDebris_A']
_folder = "Reconstruction/BD_BB_Chapter2_Orctown_Throne/Meshes"
a = spawn_static_mesh(_mesh_path, _materials, (1998.0, 1969.0, 799.0), (0.0, -60.000067159027765, 0.0), (1.0, 1.0, 1.0), "BP_DM_SM_Debris_Floor_01_Breakable_2", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1989.939, 4403.065, 799.0), (0.0, -149.9999007336502, 0.0), (1.0, 1.0, 1.0), "BP_DM_SM_Debris_Floor_01_Breakable10", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1866.3074, 4173.412, 799.0), (0.0, -75.00042893844187, 0.0), (1.0, 1.0, 1.0), "BP_DM_SM_Debris_Floor_01_Breakable11", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1936.002, 4065.0635, 799.0), (0.0, -15.000520299921085, 0.0), (1.0, 1.0, 1.0), "BP_DM_SM_Debris_Floor_01_Breakable12", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3436.5657, 369.15173, 1397.0), (0.0, 164.99942353505804, -0.0), (1.0, 1.0, 1.0), "BP_DM_SM_Debris_Floor_01_Breakable13", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2227.6545, 1845.3687, 799.0), (0.0, 14.999713275187286, -0.0), (1.0, 1.0, 1.0), "BP_DM_SM_Debris_Floor_01_Breakable2", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2336.0017, 1915.0635, 799.0), (0.0, 74.9997210056534, -0.0), (1.0, 1.0, 1.0), "BP_DM_SM_Debris_Floor_01_Breakable3", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4189.9395, 2153.0652, 799.0), (0.0, -150.0000766038294, 0.0), (1.0, 1.0, 1.0), "BP_DM_SM_Debris_Floor_01_Breakable4", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4066.3071, 1923.4113, 799.0), (0.0, -75.00042893844187, 0.0), (1.0, 1.0, 1.0), "BP_DM_SM_Debris_Floor_01_Breakable5", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4136.002, 1815.0635, 799.0), (0.0, -15.000428211065243, 0.0), (1.0, 1.0, 1.0), "BP_DM_SM_Debris_Floor_01_Breakable6", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4248.0, 4169.0, 799.0), (0.0, -59.99994149950426, 0.0), (1.0, 1.0, 1.0), "BP_DM_SM_Debris_Floor_01_Breakable7", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4477.6543, 4045.3684, 799.0), (0.0, 14.999713275187286, -0.0), (1.0, 1.0, 1.0), "BP_DM_SM_Debris_Floor_01_Breakable8", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4586.002, 4115.0635, 799.0), (0.0, 74.99966310486506, -0.0), (1.0, 1.0, 1.0), "BP_DM_SM_Debris_Floor_01_Breakable9", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3963.2803, 5222.175, 804.0), (0.0, 45.00005168692799, -0.0), (1.0, 1.0, 1.0), "SM_Debris_Floor_2", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3636.026, 5310.525, 801.0), (0.0, -29.99966276659282, 0.0), (1.0, 1.0, 1.0), "SM_Debris_Floor_3", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2827.9246, 5367.61, 804.0), (0.0, 95.00004479164929, -0.0), (1.0, 1.0, 1.0), "SM_Debris_Floor_4", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2549.8896, 5173.7085, 801.0), (0.0, 20.000581414915704, -0.0), (1.0, 1.0, 1.0), "SM_Debris_Floor_5", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1619.771, 4661.8403, 801.0), (0.0, 170.0004826024724, -0.0), (1.0, 1.0, 1.0), "SM_Debris_Floor_6", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1378.1372, 4377.4526, 801.0), (0.0, -104.9993912778419, 0.0), (1.0, 1.0, 1.0), "SM_Debris_Floor_7", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3445.3025, 5962.1553, 1398.0), (0.0, -49.99938924740375, 0.0), (1.0, 1.0, 1.0), "SM_Debris_Floor_8", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2494.4062, 5953.036, 1398.0), (0.0, 60.000607294182124, -0.0), (1.0, 1.0, 1.0), "SM_Debris_Floor_9", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3388.3025, 5598.1553, 1396.0), (0.0, 70.00061068551787, -0.0), (1.0, 1.0, 1.0), "SM_Debris_Floor_10", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1147.464, 4233.7363, 800.99927), (-4.763056590783263e-19, 80.0004327700095, 3.38170415491721e-11), (1.0, 1.0, 1.0), "SM_Debris_Floor_11", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (863.0751, 4475.3706, 801.0), (4.0981127119294094e-05, 165.00060470986244, 5.897348311574356e-06), (1.0, 1.0, 1.0), "SM_Debris_Floor_12", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1570.6732, 3574.6567, 792.0), (0.0, 0.0, -0.0), (1.0, 1.0, 1.0), "SM_Debris_Floor_13", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1638.9166, 3806.6362, 787.0), (0.0, 139.9999551042143, -0.0), (1.0, 1.0, 1.0), "SM_Debris_Floor_14", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4848.0, 5554.0, 804.0), (0.0, 0.0, -0.0), (1.0, 1.0, 1.0), "SM_Debris_Floor_01_109", _folder)
if a: placed += 1
else: skipped += 1

# Batch 139: StaticMesh'SM_Debris_Floor_02' (4 instances)
_mesh_path = "/Game/Unshippable/Whitebox/Rocks/Meshes/SM_Debris_Floor_02"
_materials = ['/Game/Environments/ProcTexturing/ProcMaterial_Quarry_RockDebris_A']
_folder = "Reconstruction/BD_BB_Chapter2_Orctown_Throne/Meshes"
a = spawn_static_mesh(_mesh_path, _materials, (2203.0, 2164.0, 799.0), (0.0, 120.00015926914853, -0.0), (1.0, 1.0, 1.0), "BP_DM_SM_Debris_Floor_02_Breakable_2", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4384.9385, 1948.0652, 799.0), (0.0, 30.000013746259135, -0.0), (1.0, 1.0, 1.0), "BP_DM_SM_Debris_Floor_02_Breakable2", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4453.0, 4364.0, 799.0), (0.0, 120.00011821633156, -0.0), (1.0, 1.0, 1.0), "BP_DM_SM_Debris_Floor_02_Breakable3", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2184.9392, 4198.065, 799.0), (0.0, 29.99995934786625, -0.0), (1.0, 1.0, 1.0), "BP_DM_SM_Debris_Floor_02_Breakable4", _folder)
if a: placed += 1
else: skipped += 1

# ======================================================================
# PHASE 2: ConstructionCatalog  (construction blocks)
# ======================================================================
unreal.log(f"[{BUBBLE_NAME}] Phase 2: Placing construction blocks...")

# Construction blocks use DecoVolume transforms (matched by Name)
_folder = "Reconstruction/BD_BB_Chapter2_Orctown_Throne/Construction"

# Construction: AB_Mines_Scaffolding_Platform_Pillar_3M3
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Scaffolding
#   Volume: EMorSimpleShape::Empty, BoxExtent: (100.0, 100.0, 100.0)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (3946.0632, 3940.4854, 2700.0), (90.0, -15.168082561050612, -60.169332390829034), (2.0000, 2.0000, 2.0000), "AB_Mines_Scaffolding_Platform_Pillar_3M3", _folder)
if a: placed += 1
else: skipped += 1

# Construction: AB_Mines_Scaffolding_Platform_Pillar_3M4
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Scaffolding
#   Volume: EMorSimpleShape::Empty, BoxExtent: (100.0, 100.0, 100.0)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (2458.7104, 2451.1003, 2700.0017), (90.0, -29.891955604534186, 105.10936803461928), (2.0000, 2.0000, 2.0000), "AB_Mines_Scaffolding_Platform_Pillar_3M4", _folder)
if a: placed += 1
else: skipped += 1

# Construction: AB_Mines_Scaffolding_Platform_Pillar_3M5
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Scaffolding
#   Volume: EMorSimpleShape::Empty, BoxExtent: (100.0, 100.0, 100.0)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (2450.6187, 3939.4727, 2700.0046), (90.0, -6.928315443612304, -141.9302861819401), (2.0000, 2.0000, 2.0000), "AB_Mines_Scaffolding_Platform_Pillar_3M5", _folder)
if a: placed += 1
else: skipped += 1

# Construction: AB_Mines_Scaffolding_Platform_Pillar_3M6
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Scaffolding
#   Volume: EMorSimpleShape::Empty, BoxExtent: (100.0, 100.0, 100.0)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (3929.3984, 2462.7244, 2700.0012), (90.0, -42.063670597475785, 2.936968022062608), (2.0000, 2.0000, 2.0000), "AB_Mines_Scaffolding_Platform_Pillar_3M6", _folder)
if a: placed += 1
else: skipped += 1

# Construction: AB_Mines_Scaffolding_Platform_Pillar_3M_Top_B_2
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Scaffolding
#   Volume: EMorSimpleShape::Empty, BoxExtent: (100.0, 100.0, 100.0)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (4158.192, 4152.6216, 2630.001), (0.000564738927677989, -44.998806279989765, 90.00022197562049), (2.0000, 2.0000, 2.0000), "AB_Mines_Scaffolding_Platform_Pillar_3M_Top_B_2", _folder)
if a: placed += 1
else: skipped += 1

# Construction: AB_Mines_Scaffolding_Platform_Pillar_3M_Top_B2_7
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Scaffolding
#   Volume: EMorSimpleShape::Empty, BoxExtent: (100.0, 100.0, 100.0)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (2246.5752, 2238.9712, 2630.0027), (0.0015961849185624755, 135.00090181181682, 90.0002129450984), (2.0000, 2.0000, 2.0000), "AB_Mines_Scaffolding_Platform_Pillar_3M_Top_B2_7", _folder)
if a: placed += 1
else: skipped += 1

# Construction: AB_Mines_Scaffolding_Platform_Pillar_3M_Top_B3
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Scaffolding
#   Volume: EMorSimpleShape::Empty, BoxExtent: (100.0, 100.0, 100.0)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (2238.4807, 4151.5996, 2630.006), (0.0013412006130845613, 45.00149446669684, 90.00002789446434), (2.0000, 2.0000, 2.0000), "AB_Mines_Scaffolding_Platform_Pillar_3M_Top_B3", _folder)
if a: placed += 1
else: skipped += 1

# Construction: AB_Mines_Scaffolding_Platform_Pillar_3M_Top_B4
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Scaffolding
#   Volume: EMorSimpleShape::Empty, BoxExtent: (100.0, 100.0, 100.0)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (4141.5303, 2250.5918, 2630.0022), (0.0007590009398779328, -134.99867600101902, 90.00018029430372), (2.0000, 2.0000, 2.0000), "AB_Mines_Scaffolding_Platform_Pillar_3M_Top_B4", _folder)
if a: placed += 1
else: skipped += 1

# Construction: AB_Mines_Scaffolding_Platform_Pillar_3M_Top_D_2
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Scaffolding
#   Volume: EMorSimpleShape::Empty, BoxExtent: (100.0, 100.0, 100.0)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (3889.973, 3882.7524, 2660.0), (-90.0, 114.78604259112367, -253.22614404287208), (2.0000, 2.0000, 2.0000), "AB_Mines_Scaffolding_Platform_Pillar_3M_Top_D_2", _folder)
if a: placed += 1
else: skipped += 1

# Construction: AB_Mines_Scaffolding_Platform_Pillar_3M_Top_D10
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Scaffolding
#   Volume: EMorSimpleShape::Empty, BoxExtent: (100.0, 100.0, 100.0)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (3871.6616, 2518.8115, 2660.0024), (-90.0, 135.95708708743942, -4.3974964456566), (2.0000, 2.0000, 2.0000), "AB_Mines_Scaffolding_Platform_Pillar_3M_Top_D10", _folder)
if a: placed += 1
else: skipped += 1

# Construction: AB_Mines_Scaffolding_Platform_Pillar_3M_Top_D11
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Scaffolding
#   Volume: EMorSimpleShape::Empty, BoxExtent: (100.0, 100.0, 100.0)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (4178.195, 2212.9243, 1849.9999), (0.0005395848157605793, 134.99989937065016, -0.0004577636176275473), (2.0000, 2.0000, 2.0000), "AB_Mines_Scaffolding_Platform_Pillar_3M_Top_D11", _folder)
if a: placed += 1
else: skipped += 1

# Construction: AB_Mines_Scaffolding_Platform_Pillar_3M_Top_D12
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Scaffolding
#   Volume: EMorSimpleShape::Empty, BoxExtent: (100.0, 100.0, 100.0)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (4178.1943, 2212.9253, 2030.0002), (0.0005737356700444705, 135.00021915333852, -179.99950822614275), (2.0000, 2.0000, 2.0000), "AB_Mines_Scaffolding_Platform_Pillar_3M_Top_D12", _folder)
if a: placed += 1
else: skipped += 1

# Construction: AB_Mines_Scaffolding_Platform_Pillar_3M_Top_D14
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Scaffolding
#   Volume: EMorSimpleShape::Empty, BoxExtent: (100.0, 100.0, 100.0)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (1961.9277, 4433.72, 2030.0076), (0.00022583282504344868, 135.00053703818546, -179.99936479265693), (2.0000, 2.0000, 2.0000), "AB_Mines_Scaffolding_Platform_Pillar_3M_Top_D14", _folder)
if a: placed += 1
else: skipped += 1

# Construction: AB_Mines_Scaffolding_Platform_Pillar_3M_Top_D15_30
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Scaffolding
#   Volume: EMorSimpleShape::Empty, BoxExtent: (100.0, 100.0, 100.0)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (1961.927, 4433.7183, 1850.0076), (0.00023222640823428457, 135.0005296574254, 0.0003814697473126818), (2.0000, 2.0000, 2.0000), "AB_Mines_Scaffolding_Platform_Pillar_3M_Top_D15_30", _folder)
if a: placed += 1
else: skipped += 1

# Construction: AB_Mines_Scaffolding_Platform_Pillar_3M_Top_D16_36
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Scaffolding
#   Volume: EMorSimpleShape::Empty, BoxExtent: (100.0, 100.0, 100.0)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (4422.641, 1966.8389, 2030.0076), (0.00023222648715297135, -44.999581349650114, -179.99936479256442), (2.0000, 2.0000, 2.0000), "AB_Mines_Scaffolding_Platform_Pillar_3M_Top_D16_36", _folder)
if a: placed += 1
else: skipped += 1

# Construction: AB_Mines_Scaffolding_Platform_Pillar_3M_Top_D17
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Scaffolding
#   Volume: EMorSimpleShape::Empty, BoxExtent: (100.0, 100.0, 100.0)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (4422.642, 1966.8411, 1850.0071), (0.00023222639704168472, -44.99942010095668, 0.0003871446075441455), (2.0000, 2.0000, 2.0000), "AB_Mines_Scaffolding_Platform_Pillar_3M_Top_D17", _folder)
if a: placed += 1
else: skipped += 1

# Construction: AB_Mines_Scaffolding_Platform_Pillar_3M_Top_D18
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Scaffolding
#   Volume: EMorSimpleShape::Empty, BoxExtent: (100.0, 100.0, 100.0)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (1962.7101, 1959.085, 2030.0076), (0.00022599998085623635, -134.9995113742597, -179.9993647926063), (2.0000, 2.0000, 2.0000), "AB_Mines_Scaffolding_Platform_Pillar_3M_Top_D18", _folder)
if a: placed += 1
else: skipped += 1

# Construction: AB_Mines_Scaffolding_Platform_Pillar_3M_Top_D19
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Scaffolding
#   Volume: EMorSimpleShape::Empty, BoxExtent: (100.0, 100.0, 100.0)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (1962.712, 1959.0842, 1850.0076), (0.00023222642332289433, -134.99938683601775, 0.0003809999908023859), (2.0000, 2.0000, 2.0000), "AB_Mines_Scaffolding_Platform_Pillar_3M_Top_D19", _folder)
if a: placed += 1
else: skipped += 1

# Construction: AB_Mines_Scaffolding_Platform_Pillar_3M_Top_D2_5
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Scaffolding
#   Volume: EMorSimpleShape::Empty, BoxExtent: (100.0, 100.0, 100.0)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (4195.859, 4189.2886, 1850.0), (-0.0, -134.9998330866963, -0.0), (2.0000, 2.0000, 2.0000), "AB_Mines_Scaffolding_Platform_Pillar_3M_Top_D2_5", _folder)
if a: placed += 1
else: skipped += 1

# Construction: AB_Mines_Scaffolding_Platform_Pillar_3M_Top_D20
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Scaffolding
#   Volume: EMorSimpleShape::Empty, BoxExtent: (100.0, 100.0, 100.0)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (4436.661, 4433.9434, 2030.0076), (0.0002322264899179331, 45.00056314484305, -179.9993647927273), (2.0000, 2.0000, 2.0000), "AB_Mines_Scaffolding_Platform_Pillar_3M_Top_D20", _folder)
if a: placed += 1
else: skipped += 1

# Construction: AB_Mines_Scaffolding_Platform_Pillar_3M_Top_D21
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Scaffolding
#   Volume: EMorSimpleShape::Empty, BoxExtent: (100.0, 100.0, 100.0)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (4436.658, 4433.945, 1850.0071), (0.00023222640645463927, 45.0005505897437, 0.0003870000774996198), (2.0000, 2.0000, 2.0000), "AB_Mines_Scaffolding_Platform_Pillar_3M_Top_D21", _folder)
if a: placed += 1
else: skipped += 1

# Construction: AB_Mines_Scaffolding_Platform_Pillar_3M_Top_D3
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Scaffolding
#   Volume: EMorSimpleShape::Empty, BoxExtent: (100.0, 100.0, 100.0)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (4195.8594, 4189.2886, 2030.0), (1.3660380885505305e-05, -134.99970312710204, -179.9996311697994), (2.0000, 2.0000, 2.0000), "AB_Mines_Scaffolding_Platform_Pillar_3M_Top_D3", _folder)
if a: placed += 1
else: skipped += 1

# Construction: AB_Mines_Scaffolding_Platform_Pillar_3M_Top_D4
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Scaffolding
#   Volume: EMorSimpleShape::Empty, BoxExtent: (100.0, 100.0, 100.0)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (2514.7983, 2508.8367, 2660.0017), (-90.0, -22.832275303171954, 64.39074864871752), (2.0000, 2.0000, 2.0000), "AB_Mines_Scaffolding_Platform_Pillar_3M_Top_D4", _folder)
if a: placed += 1
else: skipped += 1

# Construction: AB_Mines_Scaffolding_Platform_Pillar_3M_Top_D5
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Scaffolding
#   Volume: EMorSimpleShape::Empty, BoxExtent: (100.0, 100.0, 100.0)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (2208.899, 2202.313, 1850.0007), (0.0003014013885110791, 44.99984705558126, -0.0012207031007793365), (2.0000, 2.0000, 2.0000), "AB_Mines_Scaffolding_Platform_Pillar_3M_Top_D5", _folder)
if a: placed += 1
else: skipped += 1

# Construction: AB_Mines_Scaffolding_Platform_Pillar_3M_Top_D6
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Scaffolding
#   Volume: EMorSimpleShape::Empty, BoxExtent: (100.0, 100.0, 100.0)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (2208.9019, 2202.3115, 2030.0006), (0.00032189196439226145, 45.00024942283939, 179.99963116975368), (2.0000, 2.0000, 2.0000), "AB_Mines_Scaffolding_Platform_Pillar_3M_Top_D6", _folder)
if a: placed += 1
else: skipped += 1

# Construction: AB_Mines_Scaffolding_Platform_Pillar_3M_Top_D7
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Scaffolding
#   Volume: EMorSimpleShape::Empty, BoxExtent: (100.0, 100.0, 100.0)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (2508.3503, 3883.3796, 2660.0042), (-90.0, 7.659114155388557, -56.09823661686015), (2.0000, 2.0000, 2.0000), "AB_Mines_Scaffolding_Platform_Pillar_3M_Top_D7", _folder)
if a: placed += 1
else: skipped += 1

# Construction: AB_Mines_Scaffolding_Platform_Pillar_3M_Top_D8
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Scaffolding
#   Volume: EMorSimpleShape::Empty, BoxExtent: (100.0, 100.0, 100.0)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (2191.215, 4199.8813, 1850.0043), (-0.00018310547155928368, -44.99972320148695, -0.0008544921925373436), (2.0000, 2.0000, 2.0000), "AB_Mines_Scaffolding_Platform_Pillar_3M_Top_D8", _folder)
if a: placed += 1
else: skipped += 1

# Construction: AB_Mines_Scaffolding_Platform_Pillar_3M_Top_D9
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Scaffolding
#   Volume: EMorSimpleShape::Empty, BoxExtent: (100.0, 100.0, 100.0)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (2201.8186, 4189.275, 2030.0044), (-0.00018310549246948333, -44.99926861585463, 179.99955603772207), (2.0000, 2.0000, 2.0000), "AB_Mines_Scaffolding_Platform_Pillar_3M_Top_D9", _folder)
if a: placed += 1
else: skipped += 1

# Construction: AB_Orc_Scaffolding_Balcony_A_5
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Stone
#   Volume: EMorSimpleShape::OrientedBox, BoxExtent: (210.1, 198.2, 125.9)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (3584.2812, 2631.967, 1111.4727), (0.0, 0.0, -0.0), (4.2012, 3.9645, 2.5174), "AB_Orc_Scaffolding_Balcony_A_5", _folder)
if a: placed += 1
else: skipped += 1

# Construction: AB_Orc_Scaffolding_Balcony_A10
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Stone
#   Volume: EMorSimpleShape::OrientedBox, BoxExtent: (198.3, 181.7, 125.9)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (3686.399, 5134.209, 1211.4727), (0.0, 0.0, -0.0), (3.9659, 3.6347, 2.5174), "AB_Orc_Scaffolding_Balcony_A10", _folder)
if a: placed += 1
else: skipped += 1

# Construction: AB_Orc_Scaffolding_Balcony_A11
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Stone
#   Volume: EMorSimpleShape::OrientedBox, BoxExtent: (205.5, 183.6, 125.9)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (2736.1243, 5107.1416, 1211.4727), (0.0, 0.0, -0.0), (4.1097, 3.6723, 2.5174), "AB_Orc_Scaffolding_Balcony_A11", _folder)
if a: placed += 1
else: skipped += 1

# Construction: AB_Orc_Scaffolding_Balcony_A12
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Stone
#   Volume: EMorSimpleShape::OrientedBox, BoxExtent: (205.5, 183.6, 125.9)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (2459.9724, 4989.923, 1211.4727), (0.0, 0.0, -0.0), (4.1097, 3.6723, 2.5174), "AB_Orc_Scaffolding_Balcony_A12", _folder)
if a: placed += 1
else: skipped += 1

# Construction: AB_Orc_Scaffolding_Balcony_A13
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Stone
#   Volume: EMorSimpleShape::OrientedBox, BoxExtent: (172.0, 135.2, 125.9)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (3509.498, 5293.502, 1211.4727), (0.0, 0.0, -0.0), (3.4402, 2.7047, 2.5174), "AB_Orc_Scaffolding_Balcony_A13", _folder)
if a: placed += 1
else: skipped += 1

# Construction: AB_Orc_Scaffolding_Balcony_A14
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Stone
#   Volume: EMorSimpleShape::OrientedBox, BoxExtent: (172.0, 135.2, 125.9)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (3209.498, 5293.502, 1211.4727), (0.0, 0.0, -0.0), (3.4402, 2.7047, 2.5174), "AB_Orc_Scaffolding_Balcony_A14", _folder)
if a: placed += 1
else: skipped += 1

# Construction: AB_Orc_Scaffolding_Balcony_A15
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Stone
#   Volume: EMorSimpleShape::OrientedBox, BoxExtent: (172.0, 135.2, 125.9)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (2959.498, 5293.502, 1211.4727), (0.0, 0.0, -0.0), (3.4402, 2.7047, 2.5174), "AB_Orc_Scaffolding_Balcony_A15", _folder)
if a: placed += 1
else: skipped += 1

# Construction: AB_Orc_Scaffolding_Balcony_A16_13
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Stone
#   Volume: EMorSimpleShape::OrientedBox, BoxExtent: (196.2, 178.1, 125.9)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (2241.0608, 1349.2136, 1211.4727), (0.0, 0.0, -0.0), (3.9230, 3.5614, 2.5174), "AB_Orc_Scaffolding_Balcony_A16_13", _folder)
if a: placed += 1
else: skipped += 1

# Construction: AB_Orc_Scaffolding_Balcony_A17
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Stone
#   Volume: EMorSimpleShape::OrientedBox, BoxExtent: (196.2, 178.1, 125.9)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (2522.9685, 1246.6072, 1211.4727), (0.0, 0.0, -0.0), (3.9230, 3.5614, 2.5174), "AB_Orc_Scaffolding_Balcony_A17", _folder)
if a: placed += 1
else: skipped += 1

# Construction: AB_Orc_Scaffolding_Balcony_A18
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Stone
#   Volume: EMorSimpleShape::OrientedBox, BoxExtent: (172.0, 135.2, 125.9)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (2988.2505, 1160.158, 1211.4727), (0.0, 0.0, -0.0), (3.4402, 2.7047, 2.5174), "AB_Orc_Scaffolding_Balcony_A18", _folder)
if a: placed += 1
else: skipped += 1

# Construction: AB_Orc_Scaffolding_Balcony_A19
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Stone
#   Volume: EMorSimpleShape::OrientedBox, BoxExtent: (172.0, 135.2, 125.9)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (3288.251, 1160.1575, 1211.4727), (0.0, 0.0, -0.0), (3.4402, 2.7047, 2.5174), "AB_Orc_Scaffolding_Balcony_A19", _folder)
if a: placed += 1
else: skipped += 1

# Construction: AB_Orc_Scaffolding_Balcony_A2
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Stone
#   Volume: EMorSimpleShape::OrientedBox, BoxExtent: (201.6, 207.3, 125.9)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (3791.5613, 2828.6667, 1111.4727), (0.0, 0.0, -0.0), (4.0329, 4.1451, 2.5174), "AB_Orc_Scaffolding_Balcony_A2", _folder)
if a: placed += 1
else: skipped += 1

# Construction: AB_Orc_Scaffolding_Balcony_A20
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Stone
#   Volume: EMorSimpleShape::OrientedBox, BoxExtent: (135.2, 172.0, 125.9)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (5143.502, 2840.502, 1161.4727), (0.0, 0.0, -0.0), (2.7047, 3.4402, 2.5174), "AB_Orc_Scaffolding_Balcony_A20", _folder)
if a: placed += 1
else: skipped += 1

# Construction: AB_Orc_Scaffolding_Balcony_A21_8
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Stone
#   Volume: EMorSimpleShape::OrientedBox, BoxExtent: (135.2, 172.0, 125.9)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (5143.502, 3140.502, 1161.4727), (0.0, 0.0, -0.0), (2.7047, 3.4402, 2.5174), "AB_Orc_Scaffolding_Balcony_A21_8", _folder)
if a: placed += 1
else: skipped += 1

# Construction: AB_Orc_Scaffolding_Balcony_A22_10
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Stone
#   Volume: EMorSimpleShape::OrientedBox, BoxExtent: (135.2, 172.0, 125.9)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (5143.502, 3440.502, 1161.4727), (0.0, 0.0, -0.0), (2.7047, 3.4402, 2.5174), "AB_Orc_Scaffolding_Balcony_A22_10", _folder)
if a: placed += 1
else: skipped += 1

# Construction: AB_Orc_Scaffolding_Balcony_A3
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Stone
#   Volume: EMorSimpleShape::OrientedBox, BoxExtent: (195.0, 209.6, 125.9)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (3799.7144, 3542.1797, 1111.4727), (0.0, 0.0, -0.0), (3.8997, 4.1915, 2.5174), "AB_Orc_Scaffolding_Balcony_A3", _folder)
if a: placed += 1
else: skipped += 1

# Construction: AB_Orc_Scaffolding_Balcony_A4
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Stone
#   Volume: EMorSimpleShape::OrientedBox, BoxExtent: (207.3, 201.6, 125.9)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (3579.2056, 3768.7825, 1111.4727), (0.0, 0.0, -0.0), (4.1451, 4.0329, 2.5174), "AB_Orc_Scaffolding_Balcony_A4", _folder)
if a: placed += 1
else: skipped += 1

# Construction: AB_Orc_Scaffolding_Balcony_A5
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Stone
#   Volume: EMorSimpleShape::OrientedBox, BoxExtent: (209.6, 195.0, 125.9)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (2846.363, 3800.5464, 1111.4727), (0.0, 0.0, -0.0), (4.1915, 3.8997, 2.5174), "AB_Orc_Scaffolding_Balcony_A5", _folder)
if a: placed += 1
else: skipped += 1

# Construction: AB_Orc_Scaffolding_Balcony_A6
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Stone
#   Volume: EMorSimpleShape::OrientedBox, BoxExtent: (201.6, 207.3, 125.9)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (2624.5923, 3593.6692, 1111.4727), (0.0, 0.0, -0.0), (4.0329, 4.1451, 2.5174), "AB_Orc_Scaffolding_Balcony_A6", _folder)
if a: placed += 1
else: skipped += 1

# Construction: AB_Orc_Scaffolding_Balcony_A7
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Stone
#   Volume: EMorSimpleShape::OrientedBox, BoxExtent: (195.0, 209.6, 125.9)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (2589.7212, 2817.6501, 1111.4727), (0.0, 0.0, -0.0), (3.8997, 4.1915, 2.5174), "AB_Orc_Scaffolding_Balcony_A7", _folder)
if a: placed += 1
else: skipped += 1

# Construction: AB_Orc_Scaffolding_Balcony_A8
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Stone
#   Volume: EMorSimpleShape::OrientedBox, BoxExtent: (207.3, 201.6, 125.9)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (2818.1753, 2611.4502, 1111.4727), (0.0, 0.0, -0.0), (4.1451, 4.0329, 2.5174), "AB_Orc_Scaffolding_Balcony_A8", _folder)
if a: placed += 1
else: skipped += 1

# Construction: AB_Orc_Scaffolding_Balcony_A9_2
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Stone
#   Volume: EMorSimpleShape::OrientedBox, BoxExtent: (198.3, 181.7, 125.9)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (3964.5535, 5021.826, 1211.4727), (0.0, 0.0, -0.0), (3.9659, 3.6347, 2.5174), "AB_Orc_Scaffolding_Balcony_A9_2", _folder)
if a: placed += 1
else: skipped += 1

# Construction: AB_Orc_Scaffolding_Foundation_3x1m_21
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Stone
#   Volume: EMorSimpleShape::OrientedBox, BoxExtent: (153.0, 174.9, 169.2)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (1711.4087, 1674.0979, 953.346), (0.0, 0.0, -0.0), (3.0601, 3.4974, 3.3833), "AB_Orc_Scaffolding_Foundation_3x1m_21", _folder)
if a: placed += 1
else: skipped += 1

# Construction: AB_Orc_Scaffolding_Foundation_3x1m10
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Stone
#   Volume: EMorSimpleShape::OrientedBox, BoxExtent: (175.6, 151.3, 169.2)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (2094.2603, 4968.71, 953.346), (0.0, 0.0, -0.0), (3.5120, 3.0253, 3.3833), "AB_Orc_Scaffolding_Foundation_3x1m10", _folder)
if a: placed += 1
else: skipped += 1

# Construction: AB_Orc_Scaffolding_Foundation_3x1m11
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Stone
#   Volume: EMorSimpleShape::OrientedBox, BoxExtent: (176.9, 131.9, 169.2)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (3723.02, 5241.4434, 1153.346), (0.0, 0.0, -0.0), (3.5385, 2.6374, 3.3833), "AB_Orc_Scaffolding_Foundation_3x1m11", _folder)
if a: placed += 1
else: skipped += 1

# Construction: AB_Orc_Scaffolding_Foundation_3x1m12
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Stone
#   Volume: EMorSimpleShape::OrientedBox, BoxExtent: (142.4, 176.1, 169.2)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (5175.356, 2337.0347, 953.3442), (0.0, 0.0, -0.0), (2.8488, 3.5215, 3.3833), "AB_Orc_Scaffolding_Foundation_3x1m12", _folder)
if a: placed += 1
else: skipped += 1

# Construction: AB_Orc_Scaffolding_Foundation_3x1m13
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Stone
#   Volume: EMorSimpleShape::OrientedBox, BoxExtent: (134.7, 180.9, 169.2)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (5300.7085, 3733.1938, 953.346), (0.0, 0.0, -0.0), (2.6942, 3.6188, 3.3833), "AB_Orc_Scaffolding_Foundation_3x1m13", _folder)
if a: placed += 1
else: skipped += 1

# Construction: AB_Orc_Scaffolding_Foundation_3x1m14
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Stone
#   Volume: EMorSimpleShape::OrientedBox, BoxExtent: (142.4, 176.1, 169.2)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (5308.879, 2619.4697, 953.346), (0.0, 0.0, -0.0), (2.8488, 3.5215, 3.3833), "AB_Orc_Scaffolding_Foundation_3x1m14", _folder)
if a: placed += 1
else: skipped += 1

# Construction: AB_Orc_Scaffolding_Foundation_3x1m15
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Stone
#   Volume: EMorSimpleShape::OrientedBox, BoxExtent: (155.3, 173.8, 169.2)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (1902.2048, 1432.6917, 953.346), (0.0, 0.0, -0.0), (3.1052, 3.4756, 3.3833), "AB_Orc_Scaffolding_Foundation_3x1m15", _folder)
if a: placed += 1
else: skipped += 1

# Construction: AB_Orc_Scaffolding_Foundation_3x1m16
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Stone
#   Volume: EMorSimpleShape::OrientedBox, BoxExtent: (134.7, 180.9, 169.2)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (5180.2295, 4012.5088, 953.346), (0.0, 0.0, -0.0), (2.6942, 3.6188, 3.3833), "AB_Orc_Scaffolding_Foundation_3x1m16", _folder)
if a: placed += 1
else: skipped += 1

# Construction: AB_Orc_Scaffolding_Foundation_3x1m2
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Stone
#   Volume: EMorSimpleShape::OrientedBox, BoxExtent: (176.9, 133.8, 169.2)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (4308.176, 5066.51, 953.346), (0.0, 0.0, -0.0), (3.5383, 2.6754, 3.3833), "AB_Orc_Scaffolding_Foundation_3x1m2", _folder)
if a: placed += 1
else: skipped += 1

# Construction: AB_Orc_Scaffolding_Foundation_3x1m21
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Stone
#   Volume: EMorSimpleShape::OrientedBox, BoxExtent: (142.4, 176.1, 169.2)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (5308.8794, 2619.4697, 1103.346), (0.0, 0.0, -0.0), (2.8488, 3.5215, 3.3833), "AB_Orc_Scaffolding_Foundation_3x1m21", _folder)
if a: placed += 1
else: skipped += 1

# Construction: AB_Orc_Scaffolding_Foundation_3x1m24
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Stone
#   Volume: EMorSimpleShape::OrientedBox, BoxExtent: (134.7, 180.9, 169.2)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (5319.885, 3746.2693, 1103.346), (0.0, 0.0, -0.0), (2.6942, 3.6188, 3.3833), "AB_Orc_Scaffolding_Foundation_3x1m24", _folder)
if a: placed += 1
else: skipped += 1

# Construction: AB_Orc_Scaffolding_Foundation_3x1m3
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Stone
#   Volume: EMorSimpleShape::OrientedBox, BoxExtent: (176.9, 133.8, 169.2)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (4014.5854, 5164.354, 953.346), (0.0, 0.0, -0.0), (3.5383, 2.6754, 3.3833), "AB_Orc_Scaffolding_Foundation_3x1m3", _folder)
if a: placed += 1
else: skipped += 1

# Construction: AB_Orc_Scaffolding_Foundation_3x1m4_9
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Stone
#   Volume: EMorSimpleShape::OrientedBox, BoxExtent: (176.9, 133.8, 169.2)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (4030.0217, 5178.893, 1153.346), (0.0, 0.0, -0.0), (3.5383, 2.6754, 3.3833), "AB_Orc_Scaffolding_Foundation_3x1m4_9", _folder)
if a: placed += 1
else: skipped += 1

# Construction: AB_Orc_Scaffolding_Foundation_3x1m5
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Stone
#   Volume: EMorSimpleShape::OrientedBox, BoxExtent: (176.9, 131.9, 169.2)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (3723.02, 5241.4434, 953.34576), (0.0, 0.0, -0.0), (3.5385, 2.6374, 3.3833), "AB_Orc_Scaffolding_Foundation_3x1m5", _folder)
if a: placed += 1
else: skipped += 1

# Construction: AB_Orc_Scaffolding_Foundation_3x1m6
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Stone
#   Volume: EMorSimpleShape::OrientedBox, BoxExtent: (181.4, 130.4, 169.2)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (2675.0276, 5248.329, 953.346), (0.0, 0.0, -0.0), (3.6283, 2.6089, 3.3833), "AB_Orc_Scaffolding_Foundation_3x1m6", _folder)
if a: placed += 1
else: skipped += 1

# Construction: AB_Orc_Scaffolding_Foundation_3x1m7
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Stone
#   Volume: EMorSimpleShape::OrientedBox, BoxExtent: (181.4, 130.4, 169.2)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (2398.8755, 5131.1104, 953.346), (0.0, 0.0, -0.0), (3.6283, 2.6089, 3.3833), "AB_Orc_Scaffolding_Foundation_3x1m7", _folder)
if a: placed += 1
else: skipped += 1

# Construction: AB_Orc_Scaffolding_Foundation_3x1m8
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Stone
#   Volume: EMorSimpleShape::OrientedBox, BoxExtent: (181.6, 126.2, 169.2)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (2651.2402, 5258.8374, 1153.346), (0.0, 0.0, -0.0), (3.6318, 2.5232, 3.3833), "AB_Orc_Scaffolding_Foundation_3x1m8", _folder)
if a: placed += 1
else: skipped += 1

# Construction: AB_Orc_Scaffolding_Foundation_3x1m9
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Stone
#   Volume: EMorSimpleShape::OrientedBox, BoxExtent: (181.4, 130.4, 169.2)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (2372.0347, 5143.642, 1153.346), (0.0, 0.0, -0.0), (3.6283, 2.6089, 3.3833), "AB_Orc_Scaffolding_Foundation_3x1m9", _folder)
if a: placed += 1
else: skipped += 1

# Construction: AB_Orc_Scaffolding_Foundation_3x3m_2
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Stone
#   Volume: EMorSimpleShape::OrientedBox, BoxExtent: (213.0, 204.7, 169.2)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (5323.126, 3145.0747, 948.346), (0.0, 0.0, -0.0), (4.2590, 4.0937, 3.3833), "AB_Orc_Scaffolding_Foundation_3x3m_2", _folder)
if a: placed += 1
else: skipped += 1

# Construction: AB_Orc_Scaffolding_Foundation_3x3m2
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Stone
#   Volume: EMorSimpleShape::OrientedBox, BoxExtent: (204.7, 213.0, 169.2)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (5304.9253, 2873.1262, 948.346), (0.0, 0.0, -0.0), (4.0937, 4.2590, 3.3833), "AB_Orc_Scaffolding_Foundation_3x3m2", _folder)
if a: placed += 1
else: skipped += 1

# Construction: AB_Orc_Scaffolding_Foundation_3x3m3_6
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Stone
#   Volume: EMorSimpleShape::OrientedBox, BoxExtent: (213.0, 204.7, 169.2)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (5276.874, 3454.9253, 948.346), (0.0, 0.0, -0.0), (4.2590, 4.0937, 3.3833), "AB_Orc_Scaffolding_Foundation_3x3m3_6", _folder)
if a: placed += 1
else: skipped += 1

# Construction: AB_Orc_Scaffolding_Platform_1x1x2m_2
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Stone
#   Volume: EMorSimpleShape::OrientedBox, BoxExtent: (89.2, 96.9, 123.6)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (4496.2207, 4977.6313, 895.14417), (0.0, 0.0, -0.0), (1.7834, 1.9378, 2.4715), "AB_Orc_Scaffolding_Platform_1x1x2m_2", _folder)
if a: placed += 1
else: skipped += 1

# Construction: AB_Orc_Scaffolding_Platform_1x1x2m2
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Stone
#   Volume: EMorSimpleShape::OrientedBox, BoxExtent: (95.7, 90.1, 123.6)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (1912.9478, 4841.3867, 895.144), (0.0, 0.0, -0.0), (1.9138, 1.8029, 2.4715), "AB_Orc_Scaffolding_Platform_1x1x2m2", _folder)
if a: placed += 1
else: skipped += 1

# Construction: AB_Orc_Scaffolding_Platform_1x1x2m3
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Stone
#   Volume: EMorSimpleShape::OrientedBox, BoxExtent: (94.7, 82.2, 123.6)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (5062.6055, 2161.5679, 896.0609), (0.0, 0.0, -0.0), (1.8945, 1.6443, 2.4715), "AB_Orc_Scaffolding_Platform_1x1x2m3", _folder)
if a: placed += 1
else: skipped += 1

# Construction: AB_Orc_Scaffolding_Platform_1x1x2m4
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Stone
#   Volume: EMorSimpleShape::OrientedBox, BoxExtent: (88.2, 88.0, 123.6)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (5093.0483, 4200.798, 896.06274), (0.0, 0.0, -0.0), (1.7644, 1.7604, 2.4715), "AB_Orc_Scaffolding_Platform_1x1x2m4", _folder)
if a: placed += 1
else: skipped += 1

# Construction: AB_Orc_Scaffolding_Platform_1x1x2m5_5
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Stone
#   Volume: EMorSimpleShape::OrientedBox, BoxExtent: (88.8, 89.3, 123.6)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (1575.0322, 1851.1404, 895.14417), (0.0, 0.0, -0.0), (1.7761, 1.7867, 2.4715), "AB_Orc_Scaffolding_Platform_1x1x2m5_5", _folder)
if a: placed += 1
else: skipped += 1

# Construction: AB_Orc_Scaffolding_Platform_1x3x2m_7
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Stone
#   Volume: EMorSimpleShape::OrientedBox, BoxExtent: (176.9, 132.7, 123.6)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (2199.2207, 1203.8645, 1209.8368), (0.0, 0.0, -0.0), (3.5386, 2.6534, 2.4715), "AB_Orc_Scaffolding_Platform_1x3x2m_7", _folder)
if a: placed += 1
else: skipped += 1

# Construction: AB_Orc_Scaffolding_Platform_1x3x2m2
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Stone
#   Volume: EMorSimpleShape::OrientedBox, BoxExtent: (176.9, 132.7, 123.6)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (2466.3218, 1100.8491, 1209.8368), (0.0, 0.0, -0.0), (3.5386, 2.6534, 2.4715), "AB_Orc_Scaffolding_Platform_1x3x2m2", _folder)
if a: placed += 1
else: skipped += 1

# Construction: AB_Orc_Scaffolding_Platform_1x3x2m3
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Stone
#   Volume: EMorSimpleShape::OrientedBox, BoxExtent: (168.2, 85.3, 123.6)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (2993.0352, 1007.05884, 1209.8368), (0.0, 0.0, -0.0), (3.3634, 1.7055, 2.4715), "AB_Orc_Scaffolding_Platform_1x3x2m3", _folder)
if a: placed += 1
else: skipped += 1

# Construction: AB_Orc_Scaffolding_Platform_1x3x2m4
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Stone
#   Volume: EMorSimpleShape::OrientedBox, BoxExtent: (168.2, 85.3, 123.6)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (3279.2617, 1001.61, 1209.8368), (0.0, 0.0, -0.0), (3.3634, 1.7055, 2.4715), "AB_Orc_Scaffolding_Platform_1x3x2m4", _folder)
if a: placed += 1
else: skipped += 1

# Construction: AB_Orc_Scaffolding_Platform_1x3x2m5_13
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Stone
#   Volume: EMorSimpleShape::OrientedBox, BoxExtent: (154.7, 174.4, 123.6)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (1901.1055, 1431.8452, 1209.8368), (0.0, 0.0, -0.0), (3.0940, 3.4871, 2.4715), "AB_Orc_Scaffolding_Platform_1x3x2m5_13", _folder)
if a: placed += 1
else: skipped += 1

# Construction: AB_Orc_Scaffolding_Platform_1x3x2m6_16
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Stone
#   Volume: EMorSimpleShape::OrientedBox, BoxExtent: (178.1, 124.6, 123.6)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (4258.499, 1322.2296, 909.83685), (0.0, 0.0, -0.0), (3.5630, 2.4920, 2.4715), "AB_Orc_Scaffolding_Platform_1x3x2m6_16", _folder)
if a: placed += 1
else: skipped += 1

# Construction: AB_Orc_Scaffolding_Platform_3x1_No_Legs_2
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Scaffolding
#   Volume: EMorSimpleShape::OrientedBox, BoxExtent: (106.4, 153.8, 108.5)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (3888.1794, 3622.3848, 999.4937), (0.0, 0.0, -0.0), (2.1270, 3.0758, 2.1694), "AB_Orc_Scaffolding_Platform_3x1_No_Legs_2", _folder)
if a: placed += 1
else: skipped += 1

# Construction: AB_Orc_Scaffolding_Platform_3x1_No_Legs10
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Scaffolding
#   Volume: EMorSimpleShape::OrientedBox, BoxExtent: (160.4, 99.0, 21.2)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (3350.7827, 2471.9873, 1236.2104), (0.0, 0.0, -0.0), (3.2089, 1.9805, 0.4244), "AB_Orc_Scaffolding_Platform_3x1_No_Legs10", _folder)
if a: placed += 1
else: skipped += 1

# Construction: AB_Orc_Scaffolding_Platform_3x1_No_Legs11
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Scaffolding
#   Volume: EMorSimpleShape::OrientedBox, BoxExtent: (112.0, 165.0, 21.2)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (3924.9143, 3042.433, 1236.2104), (0.0, 0.0, -0.0), (2.2407, 3.3009, 0.4244), "AB_Orc_Scaffolding_Platform_3x1_No_Legs11", _folder)
if a: placed += 1
else: skipped += 1

# Construction: AB_Orc_Scaffolding_Platform_3x1_No_Legs12
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Scaffolding
#   Volume: EMorSimpleShape::OrientedBox, BoxExtent: (99.0, 160.4, 21.2)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (3937.374, 3313.2275, 1231.2104), (0.0, 0.0, -0.0), (1.9805, 3.2089, 0.4244), "AB_Orc_Scaffolding_Platform_3x1_No_Legs12", _folder)
if a: placed += 1
else: skipped += 1

# Construction: AB_Orc_Scaffolding_Platform_3x1_No_Legs13
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Scaffolding
#   Volume: EMorSimpleShape::OrientedBox, BoxExtent: (166.7, 118.1, 21.2)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (3359.526, 3920.426, 1226.2104), (0.0, 0.0, -0.0), (3.3350, 2.3629, 0.4244), "AB_Orc_Scaffolding_Platform_3x1_No_Legs13", _folder)
if a: placed += 1
else: skipped += 1

# Construction: AB_Orc_Scaffolding_Platform_3x1_No_Legs14
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Scaffolding
#   Volume: EMorSimpleShape::OrientedBox, BoxExtent: (160.4, 99.0, 21.2)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (3086.052, 3933.703, 1231.2104), (0.0, 0.0, -0.0), (3.2089, 1.9805, 0.4244), "AB_Orc_Scaffolding_Platform_3x1_No_Legs14", _folder)
if a: placed += 1
else: skipped += 1

# Construction: AB_Orc_Scaffolding_Platform_3x1_No_Legs15_2
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Scaffolding
#   Volume: EMorSimpleShape::OrientedBox, BoxExtent: (150.7, 21.2, 77.8)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (3501.1934, 5398.7896, 1140.1288), (0.0, 0.0, -0.0), (3.0133, 0.4244, 1.5552), "AB_Orc_Scaffolding_Platform_3x1_No_Legs15_2", _folder)
if a: placed += 1
else: skipped += 1

# Construction: AB_Orc_Scaffolding_Platform_3x1_No_Legs16
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Scaffolding
#   Volume: EMorSimpleShape::OrientedBox, BoxExtent: (150.7, 21.2, 77.8)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (2951.1934, 5398.7896, 1140.1288), (0.0, 0.0, -0.0), (3.0133, 0.4244, 1.5552), "AB_Orc_Scaffolding_Platform_3x1_No_Legs16", _folder)
if a: placed += 1
else: skipped += 1

# Construction: AB_Orc_Scaffolding_Platform_3x1_No_Legs17
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Scaffolding
#   Volume: EMorSimpleShape::OrientedBox, BoxExtent: (150.7, 21.2, 77.8)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (3248.8066, 5398.7896, 1159.8712), (0.0, 0.0, -0.0), (3.0133, 0.4244, 1.5552), "AB_Orc_Scaffolding_Platform_3x1_No_Legs17", _folder)
if a: placed += 1
else: skipped += 1

# Construction: AB_Orc_Scaffolding_Platform_3x1_No_Legs18
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Scaffolding
#   Volume: EMorSimpleShape::OrientedBox, BoxExtent: (150.7, 21.2, 77.8)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (2998.807, 5398.7876, 1259.8704), (0.0, 0.0, -0.0), (3.0133, 0.4244, 1.5552), "AB_Orc_Scaffolding_Platform_3x1_No_Legs18", _folder)
if a: placed += 1
else: skipped += 1

# Construction: AB_Orc_Scaffolding_Platform_3x1_No_Legs19
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Scaffolding
#   Volume: EMorSimpleShape::OrientedBox, BoxExtent: (150.7, 21.2, 77.8)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (3548.8066, 5398.7925, 1259.8723), (0.0, 0.0, -0.0), (3.0133, 0.4244, 1.5552), "AB_Orc_Scaffolding_Platform_3x1_No_Legs19", _folder)
if a: placed += 1
else: skipped += 1

# Construction: AB_Orc_Scaffolding_Platform_3x1_No_Legs2
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Scaffolding
#   Volume: EMorSimpleShape::OrientedBox, BoxExtent: (169.6, 141.3, 123.2)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (3647.1611, 3884.3057, 994.0111), (0.0, 0.0, -0.0), (3.3921, 2.8251, 2.4647), "AB_Orc_Scaffolding_Platform_3x1_No_Legs2", _folder)
if a: placed += 1
else: skipped += 1

# Construction: AB_Orc_Scaffolding_Platform_3x1_No_Legs20
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Scaffolding
#   Volume: EMorSimpleShape::OrientedBox, BoxExtent: (150.7, 21.2, 77.8)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (3251.1934, 5398.7896, 1240.1288), (0.0, 0.0, -0.0), (3.0133, 0.4244, 1.5552), "AB_Orc_Scaffolding_Platform_3x1_No_Legs20", _folder)
if a: placed += 1
else: skipped += 1

# Construction: AB_Orc_Scaffolding_Platform_3x1_No_Legs21_8
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Scaffolding
#   Volume: EMorSimpleShape::OrientedBox, BoxExtent: (142.7, 169.4, 21.2)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (5178.751, 2646.2627, 1251.2104), (0.0, 0.0, -0.0), (2.8535, 3.3872, 0.4244), "AB_Orc_Scaffolding_Platform_3x1_No_Legs21_8", _folder)
if a: placed += 1
else: skipped += 1

# Construction: AB_Orc_Scaffolding_Platform_3x1_No_Legs22
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Scaffolding
#   Volume: EMorSimpleShape::OrientedBox, BoxExtent: (142.7, 169.4, 21.2)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (5265.365, 2730.4329, 1251.2104), (0.0, 0.0, -0.0), (2.8535, 3.3872, 0.4244), "AB_Orc_Scaffolding_Platform_3x1_No_Legs22", _folder)
if a: placed += 1
else: skipped += 1

# Construction: AB_Orc_Scaffolding_Platform_3x1_No_Legs23
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Scaffolding
#   Volume: EMorSimpleShape::OrientedBox, BoxExtent: (134.1, 169.4, 21.2)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (5203.7007, 3688.5413, 1251.2104), (0.0, 0.0, -0.0), (2.6829, 3.3882, 0.4244), "AB_Orc_Scaffolding_Platform_3x1_No_Legs23", _folder)
if a: placed += 1
else: skipped += 1

# Construction: AB_Orc_Scaffolding_Platform_3x1_No_Legs24
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Scaffolding
#   Volume: EMorSimpleShape::OrientedBox, BoxExtent: (124.6, 168.2, 21.2)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (5300.7866, 3592.2375, 1251.2104), (0.0, 0.0, -0.0), (2.4920, 3.3635, 0.4244), "AB_Orc_Scaffolding_Platform_3x1_No_Legs24", _folder)
if a: placed += 1
else: skipped += 1

# Construction: AB_Orc_Scaffolding_Platform_3x1_No_Legs25_14
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Scaffolding
#   Volume: EMorSimpleShape::OrientedBox, BoxExtent: (21.2, 150.7, 77.8)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (5238.7896, 2861.3218, 1140.1288), (0.0, 0.0, -0.0), (0.4244, 3.0133, 1.5552), "AB_Orc_Scaffolding_Platform_3x1_No_Legs25_14", _folder)
if a: placed += 1
else: skipped += 1

# Construction: AB_Orc_Scaffolding_Platform_3x1_No_Legs26_19
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Scaffolding
#   Volume: EMorSimpleShape::OrientedBox, BoxExtent: (156.9, 90.6, 21.2)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (2045.6941, 1418.8436, 1301.2104), (0.0, 0.0, -0.0), (3.1374, 1.8119, 0.4244), "AB_Orc_Scaffolding_Platform_3x1_No_Legs26_19", _folder)
if a: placed += 1
else: skipped += 1

# Construction: AB_Orc_Scaffolding_Platform_3x1_No_Legs27
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Scaffolding
#   Volume: EMorSimpleShape::OrientedBox, BoxExtent: (21.2, 150.7, 77.8)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (5241.21, 3447.7437, 1159.8712), (0.0, 0.0, -0.0), (0.4244, 3.0133, 1.5552), "AB_Orc_Scaffolding_Platform_3x1_No_Legs27", _folder)
if a: placed += 1
else: skipped += 1

# Construction: AB_Orc_Scaffolding_Platform_3x1_No_Legs28
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Scaffolding
#   Volume: EMorSimpleShape::OrientedBox, BoxExtent: (169.4, 134.1, 21.2)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (2038.7112, 1316.6089, 1301.2104), (0.0, 0.0, -0.0), (3.3882, 2.6830, 0.4244), "AB_Orc_Scaffolding_Platform_3x1_No_Legs28", _folder)
if a: placed += 1
else: skipped += 1

# Construction: AB_Orc_Scaffolding_Platform_3x1_No_Legs29
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Scaffolding
#   Volume: EMorSimpleShape::OrientedBox, BoxExtent: (156.9, 90.6, 21.2)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (3466.6946, 1014.9608, 1301.2104), (0.0, 0.0, -0.0), (3.1374, 1.8119, 0.4244), "AB_Orc_Scaffolding_Platform_3x1_No_Legs29", _folder)
if a: placed += 1
else: skipped += 1

# Construction: AB_Orc_Scaffolding_Platform_3x1_No_Legs3_6
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Scaffolding
#   Volume: EMorSimpleShape::OrientedBox, BoxExtent: (174.9, 132.6, 123.2)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (2717.3428, 2500.624, 994.0107), (0.0, 0.0, -0.0), (3.4988, 2.6516, 2.4647), "AB_Orc_Scaffolding_Platform_3x1_No_Legs3_6", _folder)
if a: placed += 1
else: skipped += 1

# Construction: AB_Orc_Scaffolding_Platform_3x1_No_Legs30
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Scaffolding
#   Volume: EMorSimpleShape::OrientedBox, BoxExtent: (165.7, 114.1, 21.2)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (3471.3916, 1157.3241, 1301.2104), (0.0, 0.0, -0.0), (3.3131, 2.2821, 0.4244), "AB_Orc_Scaffolding_Platform_3x1_No_Legs30", _folder)
if a: placed += 1
else: skipped += 1

# Construction: AB_Orc_Scaffolding_Platform_3x1_No_Legs31_25
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Scaffolding
#   Volume: EMorSimpleShape::OrientedBox, BoxExtent: (150.7, 21.2, 77.8)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (3296.9202, 942.3621, 1160.1288), (0.0, 0.0, -0.0), (3.0133, 0.4244, 1.5552), "AB_Orc_Scaffolding_Platform_3x1_No_Legs31_25", _folder)
if a: placed += 1
else: skipped += 1

# Construction: AB_Orc_Scaffolding_Platform_3x1_No_Legs32
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Scaffolding
#   Volume: EMorSimpleShape::OrientedBox, BoxExtent: (150.7, 21.2, 77.8)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (3299.307, 942.36206, 1289.8712), (0.0, 0.0, -0.0), (3.0133, 0.4244, 1.5552), "AB_Orc_Scaffolding_Platform_3x1_No_Legs32", _folder)
if a: placed += 1
else: skipped += 1

# Construction: AB_Orc_Scaffolding_Platform_3x1_No_Legs33
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Scaffolding
#   Volume: EMorSimpleShape::OrientedBox, BoxExtent: (150.7, 21.2, 77.8)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (2999.3064, 949.002, 1289.8717), (0.0, 0.0, -0.0), (3.0133, 0.4244, 1.5552), "AB_Orc_Scaffolding_Platform_3x1_No_Legs33", _folder)
if a: placed += 1
else: skipped += 1

# Construction: AB_Orc_Scaffolding_Platform_3x1_No_Legs34
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Scaffolding
#   Volume: EMorSimpleShape::OrientedBox, BoxExtent: (150.7, 21.2, 77.8)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (2996.9202, 942.364, 1160.1288), (0.0, 0.0, -0.0), (3.0133, 0.4244, 1.5552), "AB_Orc_Scaffolding_Platform_3x1_No_Legs34", _folder)
if a: placed += 1
else: skipped += 1

# Construction: AB_Orc_Scaffolding_Platform_3x1_No_Legs35
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Scaffolding
#   Volume: EMorSimpleShape::OrientedBox, BoxExtent: (148.8, 71.5, 77.8)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (2675.3022, 1024.062, 1290.1293), (0.0, 0.0, -0.0), (2.9767, 1.4294, 1.5552), "AB_Orc_Scaffolding_Platform_3x1_No_Legs35", _folder)
if a: placed += 1
else: skipped += 1

# Construction: AB_Orc_Scaffolding_Platform_3x1_No_Legs36
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Scaffolding
#   Volume: EMorSimpleShape::OrientedBox, BoxExtent: (148.8, 71.5, 77.8)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (2677.5452, 1023.2456, 1179.8717), (0.0, 0.0, -0.0), (2.9767, 1.4294, 1.5552), "AB_Orc_Scaffolding_Platform_3x1_No_Legs36", _folder)
if a: placed += 1
else: skipped += 1

# Construction: AB_Orc_Scaffolding_Platform_3x1_No_Legs4
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Scaffolding
#   Volume: EMorSimpleShape::OrientedBox, BoxExtent: (114.2, 149.9, 108.5)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (2503.8772, 2755.5151, 999.4936), (0.0, 0.0, -0.0), (2.2841, 2.9989, 2.1694), "AB_Orc_Scaffolding_Platform_3x1_No_Legs4", _folder)
if a: placed += 1
else: skipped += 1

# Construction: AB_Orc_Scaffolding_Platform_3x1_No_Legs5_17
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Scaffolding
#   Volume: EMorSimpleShape::OrientedBox, BoxExtent: (162.9, 105.7, 21.2)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (3078.2883, 2479.6465, 1231.2104), (0.0, 0.0, -0.0), (3.2588, 2.1132, 0.4244), "AB_Orc_Scaffolding_Platform_3x1_No_Legs5_17", _folder)
if a: placed += 1
else: skipped += 1

# Construction: AB_Orc_Scaffolding_Platform_3x1_No_Legs6
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Scaffolding
#   Volume: EMorSimpleShape::OrientedBox, BoxExtent: (179.5, 123.3, 123.2)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (3652.5833, 2494.2246, 989.01117), (0.0, 0.0, -0.0), (3.5905, 2.4668, 2.4647), "AB_Orc_Scaffolding_Platform_3x1_No_Legs6", _folder)
if a: placed += 1
else: skipped += 1

# Construction: AB_Orc_Scaffolding_Platform_3x1_No_Legs7
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Scaffolding
#   Volume: EMorSimpleShape::OrientedBox, BoxExtent: (116.1, 148.9, 108.5)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (3916.1519, 2744.422, 994.4936), (0.0, 0.0, -0.0), (2.3215, 2.9778, 2.1694), "AB_Orc_Scaffolding_Platform_3x1_No_Legs7", _folder)
if a: placed += 1
else: skipped += 1

# Construction: AB_Orc_Scaffolding_Platform_3x1_No_Legs8
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Scaffolding
#   Volume: EMorSimpleShape::OrientedBox, BoxExtent: (114.2, 149.9, 108.5)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (2512.842, 3665.8345, 994.4934), (0.0, 0.0, -0.0), (2.2838, 2.9990, 2.1694), "AB_Orc_Scaffolding_Platform_3x1_No_Legs8", _folder)
if a: placed += 1
else: skipped += 1

# Construction: AB_Orc_Scaffolding_Platform_3x1_No_Legs9
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Scaffolding
#   Volume: EMorSimpleShape::OrientedBox, BoxExtent: (178.5, 125.7, 123.2)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (2789.3826, 3933.428, 994.0106), (0.0, 0.0, -0.0), (3.5690, 2.5140, 2.4647), "AB_Orc_Scaffolding_Platform_3x1_No_Legs9", _folder)
if a: placed += 1
else: skipped += 1

# Construction: AB_Orc_Scaffolding_Platform_3x1x3m_2
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Stone
#   Volume: EMorSimpleShape::OrientedBox, BoxExtent: (142.7, 175.7, 167.7)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (3845.6592, 3581.609, 1065.1664), (0.0, 0.0, -0.0), (2.8535, 3.5131, 3.3536), "AB_Orc_Scaffolding_Platform_3x1x3m_2", _folder)
if a: placed += 1
else: skipped += 1

# Construction: AB_Orc_Scaffolding_Platform_3x1x3m10
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Stone
#   Volume: EMorSimpleShape::OrientedBox, BoxExtent: (177.4, 124.6, 167.7)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (3934.0483, 1284.4535, 955.1664), (0.0, 0.0, -0.0), (3.5490, 2.4920, 3.3536), "AB_Orc_Scaffolding_Platform_3x1x3m10", _folder)
if a: placed += 1
else: skipped += 1

# Construction: AB_Orc_Scaffolding_Platform_3x1x3m2
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Stone
#   Volume: EMorSimpleShape::OrientedBox, BoxExtent: (175.7, 142.7, 167.7)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (2781.9565, 3862.9736, 1065.1664), (0.0, 0.0, -0.0), (3.5131, 2.8535, 3.3536), "AB_Orc_Scaffolding_Platform_3x1x3m2", _folder)
if a: placed += 1
else: skipped += 1

# Construction: AB_Orc_Scaffolding_Platform_3x1x3m3
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Stone
#   Volume: EMorSimpleShape::OrientedBox, BoxExtent: (147.0, 174.2, 167.7)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (2546.9014, 2783.8125, 1065.1664), (0.0, 0.0, -0.0), (2.9399, 3.4837, 3.3536), "AB_Orc_Scaffolding_Platform_3x1x3m3", _folder)
if a: placed += 1
else: skipped += 1

# Construction: AB_Orc_Scaffolding_Platform_3x1x3m4
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Stone
#   Volume: EMorSimpleShape::OrientedBox, BoxExtent: (174.2, 147.0, 167.7)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (3634.8677, 2575.653, 1065.1664), (0.0, 0.0, -0.0), (3.4837, 2.9399, 3.3536), "AB_Orc_Scaffolding_Platform_3x1x3m4", _folder)
if a: placed += 1
else: skipped += 1

# Construction: AB_Orc_Scaffolding_Platform_3x1x3m5_2
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Stone
#   Volume: EMorSimpleShape::OrientedBox, BoxExtent: (174.8, 108.9, 167.7)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (2699.9717, 1045.6001, 955.1664), (0.0, 0.0, -0.0), (3.4952, 2.1775, 3.3536), "AB_Orc_Scaffolding_Platform_3x1x3m5_2", _folder)
if a: placed += 1
else: skipped += 1

# Construction: AB_Orc_Scaffolding_Platform_3x1x3m6
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Stone
#   Volume: EMorSimpleShape::OrientedBox, BoxExtent: (174.8, 108.9, 167.7)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (2717.3936, 1152.8806, 955.1664), (0.0, 0.0, -0.0), (3.4952, 2.1775, 3.3536), "AB_Orc_Scaffolding_Platform_3x1x3m6", _folder)
if a: placed += 1
else: skipped += 1

# Construction: AB_Orc_Scaffolding_Platform_3x1x3m7_7
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Stone
#   Volume: EMorSimpleShape::OrientedBox, BoxExtent: (177.4, 124.6, 167.7)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (3705.4727, 1062.9318, 955.1664), (0.0, 0.0, -0.0), (3.5490, 2.4920, 3.3536), "AB_Orc_Scaffolding_Platform_3x1x3m7_7", _folder)
if a: placed += 1
else: skipped += 1

# Construction: AB_Orc_Scaffolding_Platform_3x1x3m8
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Stone
#   Volume: EMorSimpleShape::OrientedBox, BoxExtent: (177.4, 124.6, 167.7)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (3635.3135, 1168.0378, 955.1663), (0.0, 0.0, -0.0), (3.5490, 2.4920, 3.3536), "AB_Orc_Scaffolding_Platform_3x1x3m8", _folder)
if a: placed += 1
else: skipped += 1

# Construction: AB_Orc_Scaffolding_Platform_3x1x3m9
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Stone
#   Volume: EMorSimpleShape::OrientedBox, BoxExtent: (177.4, 124.6, 167.7)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (3982.9338, 1178.7186, 955.1664), (0.0, 0.0, -0.0), (3.5490, 2.4920, 3.3536), "AB_Orc_Scaffolding_Platform_3x1x3m9", _folder)
if a: placed += 1
else: skipped += 1

# Construction: AB_Orc_Scaffolding_Platform_3x1x3m_B_2
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Stone
#   Volume: EMorSimpleShape::OrientedBox, BoxExtent: (181.9, 156.0, 166.2)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (3624.771, 3816.458, 1059.6138), (0.0, 0.0, -0.0), (3.6372, 3.1197, 3.3242), "AB_Orc_Scaffolding_Platform_3x1x3m_B_2", _folder)
if a: placed += 1
else: skipped += 1

# Construction: AB_Orc_Scaffolding_Platform_3x1x3m_B2
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Stone
#   Volume: EMorSimpleShape::OrientedBox, BoxExtent: (156.0, 181.9, 166.2)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (2553.5146, 3652.3198, 1059.6138), (0.0, 0.0, -0.0), (3.1197, 3.6372, 3.3242), "AB_Orc_Scaffolding_Platform_3x1x3m_B2", _folder)
if a: placed += 1
else: skipped += 1

# Construction: AB_Orc_Scaffolding_Platform_3x1x3m_B3
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Stone
#   Volume: EMorSimpleShape::OrientedBox, BoxExtent: (184.0, 151.1, 166.2)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (2781.5283, 2558.9265, 1059.6139), (0.0, 0.0, -0.0), (3.6799, 3.0216, 3.3242), "AB_Orc_Scaffolding_Platform_3x1x3m_B3", _folder)
if a: placed += 1
else: skipped += 1

# Construction: AB_Orc_Scaffolding_Platform_3x1x3m_B4
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Stone
#   Volume: EMorSimpleShape::OrientedBox, BoxExtent: (156.0, 181.9, 166.2)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (3866.5112, 2788.9678, 1059.6139), (0.0, 0.0, -0.0), (3.1197, 3.6372, 3.3242), "AB_Orc_Scaffolding_Platform_3x1x3m_B4", _folder)
if a: placed += 1
else: skipped += 1

# Construction: AB_Orc_Scaffolding_Platform_3x1x3m_B5_2
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Stone
#   Volume: EMorSimpleShape::OrientedBox, BoxExtent: (184.7, 103.7, 166.2)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (2692.8914, 1044.4368, 1149.6138), (0.0, 0.0, -0.0), (3.6941, 2.0743, 3.3242), "AB_Orc_Scaffolding_Platform_3x1x3m_B5_2", _folder)
if a: placed += 1
else: skipped += 1

# Construction: AB_Orc_Scaffolding_Platform_3x1x3m_B6
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Stone
#   Volume: EMorSimpleShape::OrientedBox, BoxExtent: (184.7, 103.7, 166.2)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (2724.4736, 1154.044, 1149.6138), (0.0, 0.0, -0.0), (3.6941, 2.0743, 3.3242), "AB_Orc_Scaffolding_Platform_3x1x3m_B6", _folder)
if a: placed += 1
else: skipped += 1

# Construction: AB_Orc_Scaffolding_Platform_3x1x3m_B7_7
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Stone
#   Volume: EMorSimpleShape::OrientedBox, BoxExtent: (184.4, 124.7, 166.2)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (3698.6655, 1063.206, 1149.6139), (0.0, 0.0, -0.0), (3.6879, 2.4938, 3.3242), "AB_Orc_Scaffolding_Platform_3x1x3m_B7_7", _folder)
if a: placed += 1
else: skipped += 1

# Construction: AB_Orc_Scaffolding_Platform_3x1x3m_B8
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Stone
#   Volume: EMorSimpleShape::OrientedBox, BoxExtent: (184.4, 124.7, 166.2)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (3642.2593, 1168.7639, 1149.6138), (0.0, 0.0, -0.0), (3.6879, 2.4938, 3.3242), "AB_Orc_Scaffolding_Platform_3x1x3m_B8", _folder)
if a: placed += 1
else: skipped += 1

# Construction: AB_Orc_Scaffolding_Platform_3x2x3m_2
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Stone
#   Volume: EMorSimpleShape::OrientedBox, BoxExtent: (132.8, 170.3, 167.7)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (5350.1294, 2897.1938, 1105.1664), (0.0, 0.0, -0.0), (2.6552, 3.4054, 3.3536), "AB_Orc_Scaffolding_Platform_3x2x3m_2", _folder)
if a: placed += 1
else: skipped += 1

# Construction: AB_Orc_Scaffolding_Platform_3x2x3m2
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Stone
#   Volume: EMorSimpleShape::OrientedBox, BoxExtent: (132.8, 170.3, 167.7)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (5349.871, 3202.8057, 1105.1664), (0.0, 0.0, -0.0), (2.6552, 3.4054, 3.3536), "AB_Orc_Scaffolding_Platform_3x2x3m2", _folder)
if a: placed += 1
else: skipped += 1

# Construction: AB_Orc_Scaffolding_Platform_3x2x3m3
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Stone
#   Volume: EMorSimpleShape::OrientedBox, BoxExtent: (132.8, 170.3, 167.7)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (5350.1294, 3497.1938, 1105.1664), (0.0, 0.0, -0.0), (2.6552, 3.4054, 3.3536), "AB_Orc_Scaffolding_Platform_3x2x3m3", _folder)
if a: placed += 1
else: skipped += 1

# Construction: AB_Orc_Scaffolding_Platform_3x3_No_Legs_2
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Stone
#   Volume: EMorSimpleShape::OrientedBox, BoxExtent: (238.5, 205.9, 92.8)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (4231.468, 3422.89, 873.9376), (0.0, 0.0, -0.0), (4.7697, 4.1189, 1.8569), "AB_Orc_Scaffolding_Platform_3x3_No_Legs_2", _folder)
if a: placed += 1
else: skipped += 1

# Construction: AB_Orc_Scaffolding_Platform_3x3_No_Legs10
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Stone
#   Volume: EMorSimpleShape::OrientedBox, BoxExtent: (83.3, 145.3, 210.0)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (5355.097, 2593.6125, 953.8906), (0.0, 0.0, -0.0), (1.6667, 2.9057, 4.1994), "AB_Orc_Scaffolding_Platform_3x3_No_Legs10", _folder)
if a: placed += 1
else: skipped += 1

# Construction: AB_Orc_Scaffolding_Platform_3x3_No_Legs11
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Stone
#   Volume: EMorSimpleShape::OrientedBox, BoxExtent: (88.0, 143.4, 210.0)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (5243.859, 2333.0396, 976.1094), (0.0, 0.0, -0.0), (1.7590, 2.8676, 4.1994), "AB_Orc_Scaffolding_Platform_3x3_No_Legs11", _folder)
if a: placed += 1
else: skipped += 1

# Construction: AB_Orc_Scaffolding_Platform_3x3_No_Legs12
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Stone
#   Volume: EMorSimpleShape::OrientedBox, BoxExtent: (76.6, 147.7, 210.0)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (5395.233, 3746.451, 1175.6357), (0.0, 0.0, -0.0), (1.5326, 2.9531, 4.1994), "AB_Orc_Scaffolding_Platform_3x3_No_Legs12", _folder)
if a: placed += 1
else: skipped += 1

# Construction: AB_Orc_Scaffolding_Platform_3x3_No_Legs13
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Stone
#   Volume: EMorSimpleShape::OrientedBox, BoxExtent: (97.8, 153.8, 210.8)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (5264.939, 3998.5544, 1013.3158), (0.0, 0.0, -0.0), (1.9552, 3.0757, 4.2156), "AB_Orc_Scaffolding_Platform_3x3_No_Legs13", _folder)
if a: placed += 1
else: skipped += 1

# Construction: AB_Orc_Scaffolding_Platform_3x3_No_Legs14
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Stone
#   Volume: EMorSimpleShape::OrientedBox, BoxExtent: (18.5, 152.6, 210.0)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (5452.877, 2972.6682, 1194.6709), (0.0, 0.0, -0.0), (0.3699, 3.0511, 4.1994), "AB_Orc_Scaffolding_Platform_3x3_No_Legs14", _folder)
if a: placed += 1
else: skipped += 1

# Construction: AB_Orc_Scaffolding_Platform_3x3_No_Legs15
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Stone
#   Volume: EMorSimpleShape::OrientedBox, BoxExtent: (22.1, 152.9, 210.0)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (5456.9927, 3358.8462, 1192.4521), (0.0, 0.0, -0.0), (0.4418, 3.0590, 4.1994), "AB_Orc_Scaffolding_Platform_3x3_No_Legs15", _folder)
if a: placed += 1
else: skipped += 1

# Construction: AB_Orc_Scaffolding_Platform_3x3_No_Legs16
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Stone
#   Volume: EMorSimpleShape::OrientedBox, BoxExtent: (80.8, 146.2, 210.0)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (5144.5444, 4273.2188, 977.3116), (0.0, 0.0, -0.0), (1.6165, 2.9245, 4.1994), "AB_Orc_Scaffolding_Platform_3x3_No_Legs16", _folder)
if a: placed += 1
else: skipped += 1

# Construction: AB_Orc_Scaffolding_Platform_3x3_No_Legs17
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Stone
#   Volume: EMorSimpleShape::OrientedBox, BoxExtent: (18.5, 152.6, 210.0)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (5445.2715, 2968.9353, 944.6709), (0.0, 0.0, -0.0), (0.3699, 3.0511, 4.1994), "AB_Orc_Scaffolding_Platform_3x3_No_Legs17", _folder)
if a: placed += 1
else: skipped += 1

# Construction: AB_Orc_Scaffolding_Platform_3x3_No_Legs18
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Stone
#   Volume: EMorSimpleShape::OrientedBox, BoxExtent: (18.5, 152.6, 210.0)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (5445.2715, 3362.6682, 942.45215), (0.0, 0.0, -0.0), (0.3699, 3.0511, 4.1994), "AB_Orc_Scaffolding_Platform_3x3_No_Legs18", _folder)
if a: placed += 1
else: skipped += 1

# Construction: AB_Orc_Scaffolding_Platform_3x3_No_Legs19
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Stone
#   Volume: EMorSimpleShape::OrientedBox, BoxExtent: (81.9, 145.8, 210.0)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (5349.869, 3757.8699, 967.85376), (0.0, 0.0, -0.0), (1.6389, 2.9163, 4.1994), "AB_Orc_Scaffolding_Platform_3x3_No_Legs19", _folder)
if a: placed += 1
else: skipped += 1

# Construction: AB_Orc_Scaffolding_Platform_3x3_No_Legs2
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Stone
#   Volume: EMorSimpleShape::OrientedBox, BoxExtent: (236.1, 201.3, 91.3)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (4244.6006, 2986.2026, 861.6398), (0.0, 0.0, -0.0), (4.7227, 4.0256, 1.8253), "AB_Orc_Scaffolding_Platform_3x3_No_Legs2", _folder)
if a: placed += 1
else: skipped += 1

# Construction: AB_Orc_Scaffolding_Platform_3x3_No_Legs20_12
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Stone
#   Volume: EMorSimpleShape::OrientedBox, BoxExtent: (150.9, 64.2, 210.0)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (4288.6294, 1250.7352, 976.1094), (0.0, 0.0, -0.0), (3.0185, 1.2832, 4.1994), "AB_Orc_Scaffolding_Platform_3x3_No_Legs20_12", _folder)
if a: placed += 1
else: skipped += 1

# Construction: AB_Orc_Scaffolding_Platform_3x3_No_Legs21_15
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Stone
#   Volume: EMorSimpleShape::OrientedBox, BoxExtent: (150.3, 66.9, 210.0)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (4012.1946, 1126.6117, 1023.8906), (0.0, 0.0, -0.0), (3.0063, 1.3386, 4.1994), "AB_Orc_Scaffolding_Platform_3x3_No_Legs21_15", _folder)
if a: placed += 1
else: skipped += 1

# Construction: AB_Orc_Scaffolding_Platform_3x3_No_Legs22
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Stone
#   Volume: EMorSimpleShape::OrientedBox, BoxExtent: (148.6, 80.1, 212.2)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (3734.736, 1010.9047, 1196.1863), (0.0, 0.0, -0.0), (2.9724, 1.6013, 4.2437), "AB_Orc_Scaffolding_Platform_3x3_No_Legs22", _folder)
if a: placed += 1
else: skipped += 1

# Construction: AB_Orc_Scaffolding_Platform_3x3_No_Legs23_19
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Stone
#   Volume: EMorSimpleShape::OrientedBox, BoxExtent: (153.4, 44.7, 210.0)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (2692.773, 1026.3484, 966.1094), (0.0, 0.0, -0.0), (3.0690, 0.8941, 4.1994), "AB_Orc_Scaffolding_Platform_3x3_No_Legs23_19", _folder)
if a: placed += 1
else: skipped += 1

# Construction: AB_Orc_Scaffolding_Platform_3x3_No_Legs24
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Stone
#   Volume: EMorSimpleShape::OrientedBox, BoxExtent: (153.0, 70.5, 165.2)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (2168.515, 1168.5889, 1274.42), (0.0, 0.0, -0.0), (3.0602, 1.4094, 3.3030), "AB_Orc_Scaffolding_Platform_3x3_No_Legs24", _folder)
if a: placed += 1
else: skipped += 1

# Construction: AB_Orc_Scaffolding_Platform_3x3_No_Legs25
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Stone
#   Volume: EMorSimpleShape::OrientedBox, BoxExtent: (149.9, 68.8, 159.5)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (2432.9534, 1082.8402, 1239.5168), (0.0, 0.0, -0.0), (2.9973, 1.3762, 3.1893), "AB_Orc_Scaffolding_Platform_3x3_No_Legs25", _folder)
if a: placed += 1
else: skipped += 1

# Construction: AB_Orc_Scaffolding_Platform_3x3_No_Legs26
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Stone
#   Volume: EMorSimpleShape::OrientedBox, BoxExtent: (112.2, 128.8, 210.0)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (1858.5878, 1385.8275, 976.1094), (0.0, 0.0, -0.0), (2.2445, 2.5750, 4.1994), "AB_Orc_Scaffolding_Platform_3x3_No_Legs26", _folder)
if a: placed += 1
else: skipped += 1

# Construction: AB_Orc_Scaffolding_Platform_3x3_No_Legs27
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Stone
#   Volume: EMorSimpleShape::OrientedBox, BoxExtent: (112.2, 128.8, 210.0)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (1659.9277, 1610.7543, 943.8906), (0.0, 0.0, -0.0), (2.2445, 2.5751, 4.1994), "AB_Orc_Scaffolding_Platform_3x3_No_Legs27", _folder)
if a: placed += 1
else: skipped += 1

# Construction: AB_Orc_Scaffolding_Platform_3x3_No_Legs3
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Stone
#   Volume: EMorSimpleShape::OrientedBox, BoxExtent: (220.5, 245.0, 96.8)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (3477.3447, 2129.5894, 854.34937), (0.0, 0.0, -0.0), (4.4101, 4.8993, 1.9363), "AB_Orc_Scaffolding_Platform_3x3_No_Legs3", _folder)
if a: placed += 1
else: skipped += 1

# Construction: AB_Orc_Scaffolding_Platform_3x3_No_Legs4
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Stone
#   Volume: EMorSimpleShape::OrientedBox, BoxExtent: (193.0, 231.6, 89.4)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (3046.864, 2133.0876, 857.00934), (0.0, 0.0, -0.0), (3.8596, 4.6317, 1.7872), "AB_Orc_Scaffolding_Platform_3x3_No_Legs4", _folder)
if a: placed += 1
else: skipped += 1

# Construction: AB_Orc_Scaffolding_Platform_3x3_No_Legs5_2
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Stone
#   Volume: EMorSimpleShape::OrientedBox, BoxExtent: (148.4, 74.3, 210.0)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (4046.845, 5247.1733, 923.8906), (0.0, 0.0, -0.0), (2.9675, 1.4859, 4.1994), "AB_Orc_Scaffolding_Platform_3x3_No_Legs5_2", _folder)
if a: placed += 1
else: skipped += 1

# Construction: AB_Orc_Scaffolding_Platform_3x3_No_Legs6
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Stone
#   Volume: EMorSimpleShape::OrientedBox, BoxExtent: (146.2, 80.9, 210.0)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (4344.141, 5134.2607, 976.1094), (0.0, 0.0, -0.0), (2.9239, 1.6183, 4.1994), "AB_Orc_Scaffolding_Platform_3x3_No_Legs6", _folder)
if a: placed += 1
else: skipped += 1

# Construction: AB_Orc_Scaffolding_Platform_3x3_No_Legs7
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Stone
#   Volume: EMorSimpleShape::OrientedBox, BoxExtent: (189.9, 232.1, 78.6)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (2972.1917, 4245.096, 863.4655), (0.0, 0.0, -0.0), (3.7975, 4.6420, 1.5729), "AB_Orc_Scaffolding_Platform_3x3_No_Legs7", _folder)
if a: placed += 1
else: skipped += 1

# Construction: AB_Orc_Scaffolding_Platform_3x3_No_Legs8
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Stone
#   Volume: EMorSimpleShape::OrientedBox, BoxExtent: (147.7, 76.6, 210.0)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (2378.8652, 5186.3306, 923.8906), (0.0, 0.0, -0.0), (2.9531, 1.5326, 4.1994), "AB_Orc_Scaffolding_Platform_3x3_No_Legs8", _folder)
if a: placed += 1
else: skipped += 1

# Construction: AB_Orc_Scaffolding_Platform_3x3_No_Legs9
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Stone
#   Volume: EMorSimpleShape::OrientedBox, BoxExtent: (129.4, 111.4, 210.0)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (2063.4895, 5013.1846, 976.1094), (0.0, 0.0, -0.0), (2.5877, 2.2285, 4.1994), "AB_Orc_Scaffolding_Platform_3x3_No_Legs9", _folder)
if a: placed += 1
else: skipped += 1

# Construction: BP_Suburbs_Balustrade_2m_A_2
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Stone
#   Volume: EMorSimpleShape::OrientedBox, BoxExtent: (72.0, 107.7, 15.8)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (5266.658, 2656.5225, 818.2033), (0.0, 0.0, -0.0), (1.4404, 2.1547, 0.3158), "BP_Suburbs_Balustrade_2m_A_2", _folder)
if a: placed += 1
else: skipped += 1

# Construction: BP_Suburbs_Balustrade_2m_B_2
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Stone
#   Volume: EMorSimpleShape::OrientedBox, BoxExtent: (106.7, 84.9, 15.8)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (2868.3423, 5308.7637, 805.31805), (0.0, 0.0, -0.0), (2.1345, 1.6971, 0.3157), "BP_Suburbs_Balustrade_2m_B_2", _folder)
if a: placed += 1
else: skipped += 1

# Construction: BP_Suburbs_Balustrade_2m_B2_5
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Stone
#   Volume: EMorSimpleShape::OrientedBox, BoxExtent: (57.0, 105.5, 15.8)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (5375.9395, 3118.8755, 806.682), (0.0, 0.0, -0.0), (1.1400, 2.1094, 0.3157), "BP_Suburbs_Balustrade_2m_B2_5", _folder)
if a: placed += 1
else: skipped += 1

# Construction: BP_Suburbs_Balustrade_3m_B7
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Stone
#   Volume: EMorSimpleShape::OrientedBox, BoxExtent: (82.1, 155.2, 16.1)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (5289.293, 3682.8706, 806.99976), (0.0, 0.0, -0.0), (1.6411, 3.1045, 0.3221), "BP_Suburbs_Balustrade_3m_B7", _folder)
if a: placed += 1
else: skipped += 1

# Construction: BP_Suburbs_Balustrade_3m_C4_2
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Stone
#   Volume: EMorSimpleShape::OrientedBox, BoxExtent: (146.0, 119.0, 16.1)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (3198.434, 5228.0703, 805.0003), (0.0, 0.0, -0.0), (2.9191, 2.3801, 0.3221), "BP_Suburbs_Balustrade_3m_C4_2", _folder)
if a: placed += 1
else: skipped += 1

# Construction: Orc_Palissade_Gate_A_L_5
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Wood
#   Volume: EMorSimpleShape::OrientedBox, BoxExtent: (124.1, 120.8, 169.1)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (3714.0576, 4084.7195, 962.4625), (0.0, 0.0, -0.0), (2.4818, 2.4163, 3.3821), "Orc_Palissade_Gate_A_L_5", _folder)
if a: placed += 1
else: skipped += 1

# Construction: Orc_Palissade_Gate_A_L2
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Wood
#   Volume: EMorSimpleShape::OrientedBox, BoxExtent: (120.7, 124.2, 170.1)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (4104.499, 3727.7026, 978.9345), (0.0, 0.0, -0.0), (2.4136, 2.4842, 3.4025), "Orc_Palissade_Gate_A_L2", _folder)
if a: placed += 1
else: skipped += 1

# Construction: Orc_Palissade_Gate_E_L_2
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Wood
#   Volume: EMorSimpleShape::OrientedBox, BoxExtent: (113.6, 129.3, 173.9)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (2329.009, 3719.148, 982.04663), (0.0, 0.0, -0.0), (2.2711, 2.5851, 3.4782), "Orc_Palissade_Gate_E_L_2", _folder)
if a: placed += 1
else: skipped += 1

# Construction: Orc_Palissade_Gate_E_L2
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Wood
#   Volume: EMorSimpleShape::OrientedBox, BoxExtent: (123.1, 127.4, 168.3)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (2706.3154, 4115.1514, 981.3071), (0.0, 0.0, -0.0), (2.4612, 2.5487, 3.3656), "Orc_Palissade_Gate_E_L2", _folder)
if a: placed += 1
else: skipped += 1

# Construction: Orc_Palissade_Gate_E_L3_6
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Wood
#   Volume: EMorSimpleShape::OrientedBox, BoxExtent: (137.0, 129.4, 168.8)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (2474.88, 2465.6074, 987.74164), (0.0, 0.0, -0.0), (2.7400, 2.5883, 3.3757), "Orc_Palissade_Gate_E_L3_6", _folder)
if a: placed += 1
else: skipped += 1

# Construction: Orc_Palissade_Gate_E_L4_11
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Wood
#   Volume: EMorSimpleShape::OrientedBox, BoxExtent: (124.7, 123.0, 169.1)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (3736.5676, 2305.9702, 993.05786), (0.0, 0.0, -0.0), (2.4938, 2.4610, 3.3821), "Orc_Palissade_Gate_E_L4_11", _folder)
if a: placed += 1
else: skipped += 1

# Construction: Orc_Palissade_Gate_E_L5_14
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Wood
#   Volume: EMorSimpleShape::OrientedBox, BoxExtent: (151.1, 134.4, 158.0)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (4113.256, 2673.6455, 978.95245), (0.0, 0.0, -0.0), (3.0219, 2.6883, 3.1608), "Orc_Palissade_Gate_E_L5_14", _folder)
if a: placed += 1
else: skipped += 1

# Construction: Orc_Palissade_Gate_E_R_2
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Wood
#   Volume: EMorSimpleShape::OrientedBox, BoxExtent: (124.4, 124.4, 169.1)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (2480.1204, 3905.449, 979.5663), (0.0, 0.0, -0.0), (2.4879, 2.4879, 3.3826), "Orc_Palissade_Gate_E_R_2", _folder)
if a: placed += 1
else: skipped += 1

# Construction: Orc_Palissade_Gate_E_R2_5
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Wood
#   Volume: EMorSimpleShape::OrientedBox, BoxExtent: (131.2, 123.9, 168.8)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (2313.643, 2672.0488, 981.1881), (0.0, 0.0, -0.0), (2.6239, 2.4774, 3.3768), "Orc_Palissade_Gate_E_R2_5", _folder)
if a: placed += 1
else: skipped += 1

# Construction: Orc_Palissade_Gate_E_R3
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Wood
#   Volume: EMorSimpleShape::OrientedBox, BoxExtent: (133.5, 121.0, 172.2)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (2682.21, 2292.141, 982.0751), (0.0, 0.0, -0.0), (2.6692, 2.4200, 3.4438), "Orc_Palissade_Gate_E_R3", _folder)
if a: placed += 1
else: skipped += 1

# Construction: Orc_Palissade_Gate_E_R4_12
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Wood
#   Volume: EMorSimpleShape::OrientedBox, BoxExtent: (133.6, 133.6, 165.4)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (3960.461, 2448.6436, 966.09973), (0.0, 0.0, -0.0), (2.6712, 2.6712, 3.3081), "Orc_Palissade_Gate_E_R4_12", _folder)
if a: placed += 1
else: skipped += 1

# Construction: Orc_Palissade_Gate_E_R5_15
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Wood
#   Volume: EMorSimpleShape::OrientedBox, BoxExtent: (133.1, 133.0, 165.4)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (3917.5269, 3915.3745, 979.9546), (0.0, 0.0, -0.0), (2.6615, 2.6607, 3.3081), "Orc_Palissade_Gate_E_R5_15", _folder)
if a: placed += 1
else: skipped += 1

# Construction: Orc_Palissade_Wall_3X3M_A_2
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Scaffolding
#   Volume: EMorSimpleShape::OrientedBox, BoxExtent: (88.1, 189.1, 211.2)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (2970.6807, 2428.8608, 1056.2737), (0.0, 0.0, -0.0), (1.7611, 3.7828, 4.2240), "Orc_Palissade_Wall_3X3M_A_2", _folder)
if a: placed += 1
else: skipped += 1

# Construction: Orc_Palissade_Wall_3X3M_A2
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Scaffolding
#   Volume: EMorSimpleShape::OrientedBox, BoxExtent: (88.1, 189.1, 211.2)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (3488.5464, 3971.8257, 1056.2737), (0.0, 0.0, -0.0), (1.7611, 3.7828, 4.2240), "Orc_Palissade_Wall_3X3M_A2", _folder)
if a: placed += 1
else: skipped += 1

# Construction: Orc_Palissade_Wall_3X3M_A3
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Scaffolding
#   Volume: EMorSimpleShape::OrientedBox, BoxExtent: (187.9, 96.2, 211.2)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (3966.1523, 2911.5815, 1056.2737), (0.0, 0.0, -0.0), (3.7582, 1.9244, 4.2240), "Orc_Palissade_Wall_3X3M_A3", _folder)
if a: placed += 1
else: skipped += 1

# Construction: Orc_Palissade_Wall_3X3M_A4
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Scaffolding
#   Volume: EMorSimpleShape::OrientedBox, BoxExtent: (189.1, 88.1, 211.2)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (2406.0957, 2929.2761, 1056.2737), (0.0, 0.0, -0.0), (3.7828, 1.7610, 4.2240), "Orc_Palissade_Wall_3X3M_A4", _folder)
if a: placed += 1
else: skipped += 1

# Construction: Orc_Palissade_Wall_3X3M_C_2
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Scaffolding
#   Volume: EMorSimpleShape::OrientedBox, BoxExtent: (89.4, 150.9, 199.2)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (3523.9424, 2422.7761, 1064.3085), (0.0, 0.0, -0.0), (1.7871, 3.0187, 3.9831), "Orc_Palissade_Wall_3X3M_C_2", _folder)
if a: placed += 1
else: skipped += 1

# Construction: Orc_Palissade_Wall_3X3M_C2
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Scaffolding
#   Volume: EMorSimpleShape::OrientedBox, BoxExtent: (89.4, 150.9, 199.2)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (2930.2837, 3987.9116, 1064.3085), (0.0, 0.0, -0.0), (1.7871, 3.0187, 3.9831), "Orc_Palissade_Wall_3X3M_C2", _folder)
if a: placed += 1
else: skipped += 1

# Construction: Orc_Palissade_Wall_3X3M_C3
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Scaffolding
#   Volume: EMorSimpleShape::OrientedBox, BoxExtent: (152.9, 82.9, 199.2)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (3994.6118, 3468.3838, 1064.3085), (0.0, 0.0, -0.0), (3.0573, 1.6583, 3.9831), "Orc_Palissade_Wall_3X3M_C3", _folder)
if a: placed += 1
else: skipped += 1

# Construction: Orc_Palissade_Wall_3X3M_C4
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Scaffolding
#   Volume: EMorSimpleShape::OrientedBox, BoxExtent: (156.9, 55.3, 199.2)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (2415.4595, 3529.5828, 1064.3085), (0.0, 0.0, -0.0), (3.1375, 1.1065, 3.9831), "Orc_Palissade_Wall_3X3M_C4", _folder)
if a: placed += 1
else: skipped += 1

# Construction: Orc_Palissade_Wall_3X3M_C5_9
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Scaffolding
#   Volume: EMorSimpleShape::OrientedBox, BoxExtent: (196.1, 154.9, 91.2)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (4270.354, 3188.0874, 858.529), (0.0, 0.0, -0.0), (3.9228, 3.0971, 1.8241), "Orc_Palissade_Wall_3X3M_C5_9", _folder)
if a: placed += 1
else: skipped += 1

# Construction: Orc_Palissade_Wall_3X3M_C6
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Scaffolding
#   Volume: EMorSimpleShape::OrientedBox, BoxExtent: (204.9, 164.5, 84.8)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (2119.7822, 3210.3716, 854.9274), (0.0, 0.0, -0.0), (4.0989, 3.2898, 1.6959), "Orc_Palissade_Wall_3X3M_C6", _folder)
if a: placed += 1
else: skipped += 1

# Construction: Orc_Palissade_Wall_3X3M_C7
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Scaffolding
#   Volume: EMorSimpleShape::OrientedBox, BoxExtent: (155.9, 200.2, 89.6)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (3323.321, 4277.715, 853.115), (0.0, 0.0, -0.0), (3.1185, 4.0042, 1.7912), "Orc_Palissade_Wall_3X3M_C7", _folder)
if a: placed += 1
else: skipped += 1

# Construction: Orc_Scaffolding_Beam_3m_2
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Scaffolding
#   Volume: EMorSimpleShape::OrientedBox, BoxExtent: (102.5, 171.3, 86.0)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (3255.421, 2099.3462, 862.4155), (0.0, 0.0, -0.0), (2.0502, 3.4260, 1.7192), "Orc_Scaffolding_Beam_3m_2", _folder)
if a: placed += 1
else: skipped += 1

# Construction: Orc_Scaffolding_Beam_3m2_8
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Scaffolding
#   Volume: EMorSimpleShape::OrientedBox, BoxExtent: (175.9, 116.1, 71.7)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (2150.3887, 2854.8953, 851.2335), (0.0, 0.0, -0.0), (3.5175, 2.3222, 1.4341), "Orc_Scaffolding_Beam_3m2_8", _folder)
if a: placed += 1
else: skipped += 1

# Construction: Orc_Scaffolding_Beam_3m3
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Scaffolding
#   Volume: EMorSimpleShape::OrientedBox, BoxExtent: (175.1, 121.5, 73.4)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (2175.2417, 3587.2559, 857.05145), (0.0, 0.0, -0.0), (3.5011, 2.4291, 1.4679), "Orc_Scaffolding_Beam_3m3", _folder)
if a: placed += 1
else: skipped += 1

# Construction: Orc_Scaffolding_Ladder_2
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Scaffolding
#   Volume: EMorSimpleShape::OrientedBox, BoxExtent: (62.1, 69.0, 222.2)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (3711.595, 2893.7302, 1082.2305), (0.0, 0.0, -0.0), (1.2425, 1.3792, 4.4431), "Orc_Scaffolding_Ladder_2", _folder)
if a: placed += 1
else: skipped += 1

# Construction: Orc_Scaffolding_Post_Deco_A_2
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Scaffolding
#   Volume: EMorSimpleShape::OrientedBox, BoxExtent: (36.3, 197.5, 112.4)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (2558.2507, 3321.3086, 1218.3281), (0.0, 0.0, -0.0), (0.7261, 3.9499, 2.2475), "Orc_Scaffolding_Post_Deco_A_2", _folder)
if a: placed += 1
else: skipped += 1

# Construction: Orc_Scaffolding_Post_Deco_D_2
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Scaffolding
#   Volume: EMorSimpleShape::OrientedBox, BoxExtent: (34.7, 110.3, 94.0)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (2558.376, 3111.654, 1242.5482), (0.0, 0.0, -0.0), (0.6931, 2.2063, 1.8793), "Orc_Scaffolding_Post_Deco_D_2", _folder)
if a: placed += 1
else: skipped += 1

# Construction: Orc_Scaffolding_Support_Post2
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Scaffolding
#   Volume: EMorSimpleShape::OrientedBox, BoxExtent: (54.2, 205.7, 247.0)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (2540.3174, 3064.3364, 1289.6869), (0.0, 0.0, -0.0), (1.0847, 4.1149, 4.9403), "Orc_Scaffolding_Support_Post2", _folder)
if a: placed += 1
else: skipped += 1

# Construction: Orc_Scaffolding_Support_Post3
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Scaffolding
#   Volume: EMorSimpleShape::OrientedBox, BoxExtent: (246.3, 72.3, 206.3)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (3452.9744, 2553.779, 1142.7466), (0.0, 0.0, -0.0), (4.9260, 1.4456, 4.1256), "Orc_Scaffolding_Support_Post3", _folder)
if a: placed += 1
else: skipped += 1

# Construction: Orc_Scaffolding_Support_Post4_10
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Scaffolding
#   Volume: EMorSimpleShape::OrientedBox, BoxExtent: (246.7, 62.7, 206.3)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (3025.6006, 2532.8716, 1142.7466), (0.0, 0.0, -0.0), (4.9345, 1.2543, 4.1256), "Orc_Scaffolding_Support_Post4_10", _folder)
if a: placed += 1
else: skipped += 1

# Construction: Orc_Scaffolding_Support_Post5
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Scaffolding
#   Volume: EMorSimpleShape::OrientedBox, BoxExtent: (62.8, 247.1, 206.3)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (3840.153, 3384.1812, 1142.7466), (0.0, 0.0, -0.0), (1.2557, 4.9419, 4.1256), "Orc_Scaffolding_Support_Post5", _folder)
if a: placed += 1
else: skipped += 1

# Construction: Orc_Scaffolding_Support_Post6
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Scaffolding
#   Volume: EMorSimpleShape::OrientedBox, BoxExtent: (62.7, 246.7, 206.3)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (3866.4956, 2972.4805, 1142.7466), (0.0, 0.0, -0.0), (1.2543, 4.9345, 4.1256), "Orc_Scaffolding_Support_Post6", _folder)
if a: placed += 1
else: skipped += 1

# Construction: Orc_Scaffolding_Support_Post7
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Scaffolding
#   Volume: EMorSimpleShape::OrientedBox, BoxExtent: (247.1, 62.8, 206.3)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (3005.1865, 3837.0332, 1147.7466), (0.0, 0.0, -0.0), (4.9419, 1.2557, 4.1256), "Orc_Scaffolding_Support_Post7", _folder)
if a: placed += 1
else: skipped += 1

# Construction: Orc_Scaffolding_Support_Post8
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Scaffolding
#   Volume: EMorSimpleShape::OrientedBox, BoxExtent: (246.7, 62.7, 206.3)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (3426.8867, 3863.3755, 1147.7466), (0.0, 0.0, -0.0), (4.9345, 1.2543, 4.1256), "Orc_Scaffolding_Support_Post8", _folder)
if a: placed += 1
else: skipped += 1

# Construction: Orc_Scaffolding_Support_Post9
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Scaffolding
#   Volume: EMorSimpleShape::OrientedBox, BoxExtent: (54.2, 205.7, 247.0)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (2544.7346, 3399.2007, 1289.687), (0.0, 0.0, -0.0), (1.0847, 4.1149, 4.9403), "Orc_Scaffolding_Support_Post9", _folder)
if a: placed += 1
else: skipped += 1

# ======================================================================
# PHASE 3: Breakables + DecoVolumes
# ======================================================================
unreal.log(f"[{BUBBLE_NAME}] Phase 3: Placing breakables and deco volumes...")

_folder = "Reconstruction/BD_BB_Chapter2_Orctown_Throne/Breakables"

# Breakable Batch 0: BP_Suburb_Stairs_Trim_Pillar_C_Breakable (4 instances)
#   BP Class: /Game/LevelDesign/Architecture/Suburbs/BP_Suburb_Stairs_Trim_Pillar_C_Breakable
_brk_mesh = "/Game/Art/Assets/Kits/Architecture/Suburbs/Suburb_Stairs_Trim_Pillar_C"
_brk_mats = ['/Game/Art/Assets/Kits/Architecture/Suburbs/Materials/Suburb_Stairs_Trim/MI_Suburb_Stairs_Trim_Pillar_C_Dest']
a = spawn_static_mesh(_brk_mesh, _brk_mats, (5976.006, 3758.7913, 1350.0), (0.0, 177.18761226169238, -0.0), (1.0, 1.0, 1.0), "BP_Suburb_Stairs_Trim_Pillar_C_Breakable3_2", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_brk_mesh, _brk_mats, (6075.8853, 3753.8853, 1400.0), (0.0, 87.18757831705581, -0.0), (1.0, 1.0, 1.0), "BP_Suburb_Stairs_Trim_Pillar_C_Breakable4", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_brk_mesh, _brk_mats, (6021.913, 2655.2305, 1400.0), (0.0, -2.812469493326736, 0.0), (1.0, 1.0, 1.0), "BP_Suburb_Stairs_Trim_Pillar_C_Breakable5", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_brk_mesh, _brk_mats, (5922.034, 2660.1392, 1350.0), (0.0, -92.81243614310894, 0.0), (1.0, 1.0, 1.0), "BP_Suburb_Stairs_Trim_Pillar_C_Breakable6", _folder)
if a: placed += 1
else: skipped += 1

# Breakable Batch 1: BP_DM_Warren_lighting_Banner_A_Breakable (2 instances)
#   BP Class: /Game/LevelDesign/Deco/GoblinWarren/BP_DM_Warren_lighting_Banner_A_Breakable
_brk_mesh = "/Game/Art/Assets/Kits/Deco/Orc/Warren_lighting_Banner_A"
_brk_mats = ['/Game/Art/Assets/Kits/Deco/Orc/Materials/Orc_Lighting/Rubble_Masonry_Pile_Base_Inst', '/Game/Art/Assets/Kits/Deco/Orc/Materials/Orc_Lighting/MI_Orc_Lighting', '/Game/Art/Assets/Kits/Deco/Orc/Materials/Orc_Banners/MI_OrcBanners_B']
a = spawn_static_mesh(_brk_mesh, _brk_mats, (2205.0, 3730.0, 805.0), (0.0, 89.99995443177896, -0.0), (1.0, 1.0, 1.0), "BP_DM_Warren_lighting_Banner_A_Breakable_2", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_brk_mesh, _brk_mats, (2205.0, 2680.0, 805.0), (0.0, 89.99995443177896, -0.0), (1.0, 1.0, 1.0), "BP_DM_Warren_lighting_Banner_A_Breakable2", _folder)
if a: placed += 1
else: skipped += 1

# Breakable Batch 2: BP_DM_Mine_tailings_Debris_2x2_C (4 instances)
#   BP Class: /Game/LevelDesign/Deco/MinesDressing/BP_DM_Mine_tailings_Debris_2x2_C
_brk_mesh = "/Game/Art/Assets/Kits/Deco/Mines/Mine_tailings_Debris_2x2_C"
_brk_mats = ['/Game/Art/Assets/Kits/Misc/Dirt_Mounds/Materials/MI_DirtMound_Mines', '/Game/Art/Assets/Kits/Deco/Rubble/Materials/Rubble_Masonry_Pile/MI_Rubble_Masonry_Pile_Base_Inst', '/Game/Art/Assets/Kits/Deco/Rubble/Materials/Rubble_Masonry_Pile/MI_Rubble_Masonry_Pile_06_Inst']
a = spawn_static_mesh(_brk_mesh, _brk_mats, (2223.0, 1950.0, 796.0), (0.0, 45.000017339218374, -0.0), (1.0, 1.0, 1.0), "BP_DM_Mine_tailings_Debris_2x2_C_2", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_brk_mesh, _brk_mats, (4170.9385, 1928.0656, 796.0), (0.0, -45.0000865484073, 0.0), (1.0, 1.0, 1.0), "BP_DM_Mine_tailings_Debris_2x2_C2", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_brk_mesh, _brk_mats, (4473.0, 4150.0, 796.0), (0.0, 45.00003526167798, -0.0), (1.0, 1.0, 1.0), "BP_DM_Mine_tailings_Debris_2x2_C3", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_brk_mesh, _brk_mats, (1970.9387, 4178.0654, 796.0), (0.0, -45.000056798727684, 0.0), (1.0, 1.0, 1.0), "BP_DM_Mine_tailings_Debris_2x2_C4", _folder)
if a: placed += 1
else: skipped += 1

# Breakable Batch 3: BP_DM_Mine_tailings_Debris_3x3_B (4 instances)
#   BP Class: /Game/LevelDesign/Deco/MinesDressing/BP_DM_Mine_tailings_Debris_3x3_B
_brk_mesh = "/Game/Art/Assets/Kits/Deco/Mines/Mine_tailings_Debris_3x3_B"
_brk_mats = ['/Game/Art/Assets/Kits/Misc/Dirt_Mounds/Materials/MI_DirtMound_Mines', '/Game/Art/Assets/Kits/Deco/Rubble/Materials/Rubble_Masonry_Pile/MI_Rubble_Masonry_Pile_06_Inst']
a = spawn_static_mesh(_brk_mesh, _brk_mats, (1955.0, 2244.0, 797.0), (0.0, 44.976866768275436, -0.0), (1.0, 1.0, 1.0), "BP_DM_Mine_tailings_Debris_3x3_B_5", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_brk_mesh, _brk_mats, (4464.939, 2196.065, 797.0), (0.0, -45.02328966634664, 0.0), (1.0, 1.0, 1.0), "BP_DM_Mine_tailings_Debris_3x3_B2", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_brk_mesh, _brk_mats, (4205.0, 4443.9995, 797.0), (0.0, 44.97683173022856, -0.0), (1.0, 1.0, 1.0), "BP_DM_Mine_tailings_Debris_3x3_B3", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_brk_mesh, _brk_mats, (2264.939, 4446.065, 797.0), (0.0, -45.02328966634664, 0.0), (1.0, 1.0, 1.0), "BP_DM_Mine_tailings_Debris_3x3_B4", _folder)
if a: placed += 1
else: skipped += 1

# Breakable Batch 4: BP_Mines_Lift_Beam_B (120 instances)
#   BP Class: /Game/LevelDesign/Deco/MinesDressing/BP_Mines_Lift_Beam_B
_brk_mesh = "/Game/Art/Assets/Kits/Deco/Mines/Machine/Mines_Machine_Lift_Pieces/Mines_Lift_Beam_B"
_brk_mats = ['/Game/Art/Assets/Kits/Deco/Mines/Machine/Mines_Machine_Lift_Pieces/Materials/Mi_Mines_Machine_Lift_E']
a = spawn_static_mesh(_brk_mesh, _brk_mats, (4111.8457, 2796.0994, 1235.0), (4.099998551741078e-05, 70.31883401126476, 179.999767773514), (1.0, 1.0, 1.0), "BP_Mines_Lift_Beam_B10", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_brk_mesh, _brk_mats, (4348.3955, 2001.2325, 2665.0068), (-90.0, -22.999327276664356, -22.001466920592048), (1.0, 1.0, 1.0), "BP_Mines_Lift_Beam_B100", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_brk_mesh, _brk_mats, (2035.9863, 1994.4373, 930.00433), (90.0, 1.2391073331146547, -43.76219346426673), (1.0, 1.0, 1.0), "BP_Mines_Lift_Beam_B101", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_brk_mesh, _brk_mats, (1997.094, 2033.3296, 930.0041), (-90.0, -7.855212964245859, 232.85418401117954), (1.0, 1.0, 1.0), "BP_Mines_Lift_Beam_B102", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_brk_mesh, _brk_mats, (2035.9868, 1994.438, 1220.0054), (90.0, 1.6359106536221744, -43.36595586153097), (1.0, 1.0, 1.0), "BP_Mines_Lift_Beam_B103", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_brk_mesh, _brk_mats, (1997.0942, 2033.3284, 1220.0056), (-90.0, 157.62004620331012, -292.6208543655363), (1.0, 1.0, 1.0), "BP_Mines_Lift_Beam_B104", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_brk_mesh, _brk_mats, (2035.9868, 1994.438, 1510.0052), (90.0, 1.6359106536221744, -43.36595586153097), (1.0, 1.0, 1.0), "BP_Mines_Lift_Beam_B105", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_brk_mesh, _brk_mats, (1997.0955, 2033.3298, 1510.0055), (-90.0, 157.62004620331012, -292.6208543655363), (1.0, 1.0, 1.0), "BP_Mines_Lift_Beam_B106", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_brk_mesh, _brk_mats, (2035.99, 1994.4387, 1800.0054), (90.0, 1.2391073331146547, -43.76219346426673), (1.0, 1.0, 1.0), "BP_Mines_Lift_Beam_B107", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_brk_mesh, _brk_mats, (1997.0989, 2033.3306, 1800.0054), (-90.0, -7.855212964245859, 232.85418401117954), (1.0, 1.0, 1.0), "BP_Mines_Lift_Beam_B108", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_brk_mesh, _brk_mats, (2035.9937, 1994.4412, 2090.0073), (90.0, 1.6359106536221744, -43.36595586153097), (1.0, 1.0, 1.0), "BP_Mines_Lift_Beam_B109", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_brk_mesh, _brk_mats, (4121.2617, 2792.7324, 829.0), (-0.00024414061948345263, -19.68048102423862, -0.00021362305149204863), (1.0, 1.0, 1.0), "BP_Mines_Lift_Beam_B11", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_brk_mesh, _brk_mats, (1997.0991, 2033.3315, 2090.0059), (-90.0, 157.62004620331012, -292.6208543655363), (1.0, 1.0, 1.0), "BP_Mines_Lift_Beam_B110", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_brk_mesh, _brk_mats, (2035.9934, 1994.4409, 2380.007), (90.0, 1.2391073331146547, -43.76219346426673), (1.0, 1.0, 1.0), "BP_Mines_Lift_Beam_B111", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_brk_mesh, _brk_mats, (1997.1013, 2033.3308, 2380.0068), (-90.0, 157.62004620331012, -292.6208543655363), (1.0, 1.0, 1.0), "BP_Mines_Lift_Beam_B112", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_brk_mesh, _brk_mats, (2035.9934, 1994.4409, 2665.007), (90.0, 1.2391073331146547, -43.76219346426673), (1.0, 1.0, 1.0), "BP_Mines_Lift_Beam_B113", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_brk_mesh, _brk_mats, (1997.1013, 2033.3308, 2665.0068), (-90.0, -4.700485902709613, 229.69966328214295), (1.0, 1.0, 1.0), "BP_Mines_Lift_Beam_B114", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_brk_mesh, _brk_mats, (4363.3833, 4398.5947, 930.00385), (90.0, -0.3002177713890531, 134.6987342395456), (1.0, 1.0, 1.0), "BP_Mines_Lift_Beam_B115", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_brk_mesh, _brk_mats, (4402.2734, 4359.6997, 930.0036), (-90.0, -56.292782446967976, 101.29192838487475), (1.0, 1.0, 1.0), "BP_Mines_Lift_Beam_B116", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_brk_mesh, _brk_mats, (4363.383, 4398.5923, 1220.0049), (90.0, -2.3465622017281733, -227.34853018226528), (1.0, 1.0, 1.0), "BP_Mines_Lift_Beam_B117", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_brk_mesh, _brk_mats, (4402.2725, 4359.6997, 1220.0051), (-90.0, 1.4787260136992755, -316.4795050023384), (1.0, 1.0, 1.0), "BP_Mines_Lift_Beam_B118", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_brk_mesh, _brk_mats, (4363.383, 4398.592, 1510.0048), (90.0, -2.3465622017281733, -227.34853018226528), (1.0, 1.0, 1.0), "BP_Mines_Lift_Beam_B119", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_brk_mesh, _brk_mats, (4123.347, 3567.9873, 1235.0), (4.0999997266063246e-05, 112.5060874258738, 179.99976777351182), (1.0, 1.0, 1.0), "BP_Mines_Lift_Beam_B12", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_brk_mesh, _brk_mats, (4402.272, 4359.6987, 1510.005), (-90.0, 1.4787260136992755, -316.4795050023384), (1.0, 1.0, 1.0), "BP_Mines_Lift_Beam_B120", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_brk_mesh, _brk_mats, (4363.379, 4398.591, 1800.0049), (90.0, -0.3002177713890531, 134.6987342395456), (1.0, 1.0, 1.0), "BP_Mines_Lift_Beam_B121", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_brk_mesh, _brk_mats, (4402.2686, 4359.6987, 1800.0049), (-90.0, -56.292782446967976, 101.29192838487475), (1.0, 1.0, 1.0), "BP_Mines_Lift_Beam_B122", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_brk_mesh, _brk_mats, (4363.3755, 4398.589, 2090.0068), (90.0, -2.3465622017281733, -227.34853018226528), (1.0, 1.0, 1.0), "BP_Mines_Lift_Beam_B123", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_brk_mesh, _brk_mats, (4402.2686, 4359.6978, 2090.0054), (-90.0, 1.4787260136992755, -316.4795050023384), (1.0, 1.0, 1.0), "BP_Mines_Lift_Beam_B124", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_brk_mesh, _brk_mats, (4363.3765, 4398.59, 2380.007), (90.0, -0.3002177713890531, 134.6987342395456), (1.0, 1.0, 1.0), "BP_Mines_Lift_Beam_B125", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_brk_mesh, _brk_mats, (4402.2656, 4359.6978, 2380.0068), (-90.0, 1.4787260136992755, -316.4795050023384), (1.0, 1.0, 1.0), "BP_Mines_Lift_Beam_B126", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_brk_mesh, _brk_mats, (4363.3765, 4398.5894, 2665.007), (90.0, -0.3002177713890531, 134.6987342395456), (1.0, 1.0, 1.0), "BP_Mines_Lift_Beam_B127", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_brk_mesh, _brk_mats, (4402.265, 4359.6978, 2665.0068), (-90.0, 1.4787260136992755, -316.4795050023384), (1.0, 1.0, 1.0), "BP_Mines_Lift_Beam_B128", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_brk_mesh, _brk_mats, (4132.584, 3571.8154, 829.0), (-0.00024414062827582276, 22.50695775994957, -0.00021362305856347265), (1.0, 1.0, 1.0), "BP_Mines_Lift_Beam_B13", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_brk_mesh, _brk_mats, (3592.6304, 4112.3027, 1235.0), (4.099999611199258e-05, 157.50598483837192, 179.9997677735482), (1.0, 1.0, 1.0), "BP_Mines_Lift_Beam_B14_24", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_brk_mesh, _brk_mats, (3596.4543, 4121.543, 829.0), (-0.0002441406207026343, 67.50697634928744, -0.0002136230522181159), (1.0, 1.0, 1.0), "BP_Mines_Lift_Beam_B15_25", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_brk_mesh, _brk_mats, (2833.238, 4121.9697, 1235.0), (4.099998738526191e-05, -157.49400987930764, 179.9997677735286), (1.0, 1.0, 1.0), "BP_Mines_Lift_Beam_B16_28", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_brk_mesh, _brk_mats, (2829.4087, 4131.2065, 829.0), (-0.00024414062265196677, 112.50691693943767, -0.00021362305646427295), (1.0, 1.0, 1.0), "BP_Mines_Lift_Beam_B17_29", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_brk_mesh, _brk_mats, (2285.3762, 3588.795, 1235.0), (4.09811115500282e-05, -112.49373274070214, 179.99976777352225), (1.0, 1.0, 1.0), "BP_Mines_Lift_Beam_B2_2", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_brk_mesh, _brk_mats, (4269.1426, 4224.6436, 930.0), (90.0, 29.76387621173386, -15.234989755326858), (1.0, 1.0, 1.0), "BP_Mines_Lift_Beam_B25", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_brk_mesh, _brk_mats, (4230.2505, 4263.5356, 930.0), (-90.0, 16.11952685022126, -151.12127472468313), (1.0, 1.0, 1.0), "BP_Mines_Lift_Beam_B26", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_brk_mesh, _brk_mats, (4269.1426, 4224.6436, 1220.0), (90.0, 29.76387621173386, -15.234989755326858), (1.0, 1.0, 1.0), "BP_Mines_Lift_Beam_B27", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_brk_mesh, _brk_mats, (4230.2505, 4263.5356, 1220.0), (-90.0, -12.371569383358022, -122.63024479388669), (1.0, 1.0, 1.0), "BP_Mines_Lift_Beam_B28", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_brk_mesh, _brk_mats, (4269.1426, 4224.6436, 1510.0), (90.0, 29.76387621173386, -15.234989755326858), (1.0, 1.0, 1.0), "BP_Mines_Lift_Beam_B29", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_brk_mesh, _brk_mats, (2276.1377, 3592.6206, 829.0), (-0.0002441406153298336, 157.50704156905627, -0.0002136230481253032), (1.0, 1.0, 1.0), "BP_Mines_Lift_Beam_B3", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_brk_mesh, _brk_mats, (4230.2505, 4263.5356, 1510.0), (-90.0, -12.371569383358022, -122.63024479388669), (1.0, 1.0, 1.0), "BP_Mines_Lift_Beam_B30", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_brk_mesh, _brk_mats, (4269.1426, 4224.6436, 1800.0), (90.0, 29.76387621173386, -15.234989755326858), (1.0, 1.0, 1.0), "BP_Mines_Lift_Beam_B31", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_brk_mesh, _brk_mats, (4230.2505, 4263.5356, 1800.0), (-90.0, -12.371569383358022, -122.63024479388669), (1.0, 1.0, 1.0), "BP_Mines_Lift_Beam_B32", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_brk_mesh, _brk_mats, (4269.1426, 4224.6436, 2090.0), (90.0, 29.76387621173386, -15.234989755326858), (1.0, 1.0, 1.0), "BP_Mines_Lift_Beam_B33", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_brk_mesh, _brk_mats, (4230.2505, 4263.5356, 2090.0), (-90.0, -12.371569383358022, -122.63024479388669), (1.0, 1.0, 1.0), "BP_Mines_Lift_Beam_B34", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_brk_mesh, _brk_mats, (4269.1426, 4224.6436, 2380.0), (90.0, 29.76387621173386, -15.234989755326858), (1.0, 1.0, 1.0), "BP_Mines_Lift_Beam_B35", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_brk_mesh, _brk_mats, (4230.2505, 4263.5356, 2380.0), (-90.0, -12.371569383358022, -122.63024479388669), (1.0, 1.0, 1.0), "BP_Mines_Lift_Beam_B36", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_brk_mesh, _brk_mats, (2135.6042, 2166.9702, 930.0006), (90.0, -1.7438098779034155, 133.25973781149216), (1.0, 1.0, 1.0), "BP_Mines_Lift_Beam_B37", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_brk_mesh, _brk_mats, (2174.4958, 2128.0776, 930.0001), (-90.0, 143.58062175974223, -98.58399042968259), (1.0, 1.0, 1.0), "BP_Mines_Lift_Beam_B38", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_brk_mesh, _brk_mats, (2135.6082, 2166.9658, 1220.0004), (90.0, -1.7438098779034155, 133.25973781149216), (1.0, 1.0, 1.0), "BP_Mines_Lift_Beam_B39", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_brk_mesh, _brk_mats, (2274.7095, 2830.4026, 1235.0), (4.0999991583887474e-05, -67.49361290513941, 179.9997677735361), (1.0, 1.0, 1.0), "BP_Mines_Lift_Beam_B4_8", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_brk_mesh, _brk_mats, (2174.4998, 2128.074, 1220.0004), (-90.0, 143.58062175974223, -98.58399042968259), (1.0, 1.0, 1.0), "BP_Mines_Lift_Beam_B40", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_brk_mesh, _brk_mats, (2135.6113, 2166.9626, 1510.0004), (90.0, -1.7438098779034155, 133.25973781149216), (1.0, 1.0, 1.0), "BP_Mines_Lift_Beam_B41", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_brk_mesh, _brk_mats, (2174.5032, 2128.0706, 1510.0004), (-90.0, 143.58062175974223, -98.58399042968259), (1.0, 1.0, 1.0), "BP_Mines_Lift_Beam_B42", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_brk_mesh, _brk_mats, (2135.6147, 2166.9592, 1800.0004), (90.0, -1.7438098779034155, 133.25973781149216), (1.0, 1.0, 1.0), "BP_Mines_Lift_Beam_B43", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_brk_mesh, _brk_mats, (2174.507, 2128.0674, 1800.0001), (-90.0, 143.58062175974223, -98.58399042968259), (1.0, 1.0, 1.0), "BP_Mines_Lift_Beam_B44", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_brk_mesh, _brk_mats, (2135.6191, 2166.956, 2090.0002), (90.0, -1.7438098779034155, 133.25973781149216), (1.0, 1.0, 1.0), "BP_Mines_Lift_Beam_B45", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_brk_mesh, _brk_mats, (2174.5105, 2128.0635, 2090.0002), (-90.0, 143.58062175974223, -98.58399042968259), (1.0, 1.0, 1.0), "BP_Mines_Lift_Beam_B46", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_brk_mesh, _brk_mats, (2135.6226, 2166.952, 2380.0002), (90.0, -1.7438098779034155, 133.25973781149216), (1.0, 1.0, 1.0), "BP_Mines_Lift_Beam_B47", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_brk_mesh, _brk_mats, (2174.514, 2128.0598, 2380.0002), (-90.0, 143.58062175974223, -98.58399042968259), (1.0, 1.0, 1.0), "BP_Mines_Lift_Beam_B48", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_brk_mesh, _brk_mats, (2166.4734, 4262.57, 930.0043), (90.0, 6.711109415173179, -128.2881255611381), (1.0, 1.0, 1.0), "BP_Mines_Lift_Beam_B49", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_brk_mesh, _brk_mats, (2265.4722, 2826.575, 829.0), (-0.0002441406308957245, -157.4930467583113, -0.00021362306136825404), (1.0, 1.0, 1.0), "BP_Mines_Lift_Beam_B5_9", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_brk_mesh, _brk_mats, (2127.5808, 4223.678, 930.00305), (-90.0, -162.73243619352448, 117.73095674019295), (1.0, 1.0, 1.0), "BP_Mines_Lift_Beam_B50", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_brk_mesh, _brk_mats, (2166.4702, 4262.567, 1220.005), (90.0, 27.894474589139875, 252.89479760561812), (1.0, 1.0, 1.0), "BP_Mines_Lift_Beam_B51", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_brk_mesh, _brk_mats, (2127.5786, 4223.6743, 1220.0043), (-90.0, -7.755613232301025, -37.24569954271252), (1.0, 1.0, 1.0), "BP_Mines_Lift_Beam_B52", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_brk_mesh, _brk_mats, (2166.469, 4262.561, 1510.005), (90.0, 27.894474589139875, 252.89479760561812), (1.0, 1.0, 1.0), "BP_Mines_Lift_Beam_B53", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_brk_mesh, _brk_mats, (2127.5764, 4223.671, 1510.0043), (-90.0, -7.755613232301025, -37.24569954271252), (1.0, 1.0, 1.0), "BP_Mines_Lift_Beam_B54", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_brk_mesh, _brk_mats, (2166.4666, 4262.5596, 1800.0051), (90.0, 6.711109415173179, -128.2881255611381), (1.0, 1.0, 1.0), "BP_Mines_Lift_Beam_B55", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_brk_mesh, _brk_mats, (2127.574, 4223.6675, 1800.0043), (-90.0, -162.73243619352448, 117.73095674019295), (1.0, 1.0, 1.0), "BP_Mines_Lift_Beam_B56", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_brk_mesh, _brk_mats, (2166.463, 4262.557, 2090.0051), (90.0, 27.894474589139875, 252.89479760561812), (1.0, 1.0, 1.0), "BP_Mines_Lift_Beam_B57", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_brk_mesh, _brk_mats, (2127.5713, 4223.6636, 2090.0042), (-90.0, -7.755613232301025, -37.24569954271252), (1.0, 1.0, 1.0), "BP_Mines_Lift_Beam_B58", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_brk_mesh, _brk_mats, (2166.4604, 4262.553, 2380.0051), (90.0, 6.711109415173179, -128.2881255611381), (1.0, 1.0, 1.0), "BP_Mines_Lift_Beam_B59", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_brk_mesh, _brk_mats, (2869.3916, 2266.1199, 1235.0), (4.099999543491864e-05, -19.68093600798548, 179.99976777354374), (1.0, 1.0, 1.0), "BP_Mines_Lift_Beam_B6", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_brk_mesh, _brk_mats, (2127.569, 4223.6616, 2380.0042), (-90.0, -7.755613232301025, -37.24569954271252), (1.0, 1.0, 1.0), "BP_Mines_Lift_Beam_B60", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_brk_mesh, _brk_mats, (4213.545, 2139.6396, 929.99866), (90.0, 84.32992745095008, 129.33249207674862), (1.0, 1.0, 1.0), "BP_Mines_Lift_Beam_B61", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_brk_mesh, _brk_mats, (4252.4375, 2178.5308, 929.99817), (-90.0, 13.141140679335829, 121.85578886500589), (1.0, 1.0, 1.0), "BP_Mines_Lift_Beam_B62", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_brk_mesh, _brk_mats, (4213.5464, 2139.6406, 1219.9991), (90.0, 84.32992745095008, 129.33249207674862), (1.0, 1.0, 1.0), "BP_Mines_Lift_Beam_B63", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_brk_mesh, _brk_mats, (4252.4385, 2178.5322, 1219.9994), (-90.0, 13.141140679335829, 121.85578886500589), (1.0, 1.0, 1.0), "BP_Mines_Lift_Beam_B64", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_brk_mesh, _brk_mats, (4213.5474, 2139.6401, 1509.9991), (90.0, 84.32992745095008, 129.33249207674862), (1.0, 1.0, 1.0), "BP_Mines_Lift_Beam_B65", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_brk_mesh, _brk_mats, (4252.44, 2178.5322, 1509.9994), (-90.0, 13.141140679335829, 121.85578886500589), (1.0, 1.0, 1.0), "BP_Mines_Lift_Beam_B66", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_brk_mesh, _brk_mats, (4213.549, 2139.6406, 1799.9991), (90.0, 84.32992745095008, 129.33249207674862), (1.0, 1.0, 1.0), "BP_Mines_Lift_Beam_B67", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_brk_mesh, _brk_mats, (4252.4404, 2178.5327, 1799.9991), (-90.0, 13.141140679335829, 121.85578886500589), (1.0, 1.0, 1.0), "BP_Mines_Lift_Beam_B68", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_brk_mesh, _brk_mats, (4213.5493, 2139.6416, 2089.9995), (90.0, 84.32992745095008, 129.33249207674862), (1.0, 1.0, 1.0), "BP_Mines_Lift_Beam_B69", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_brk_mesh, _brk_mats, (2866.025, 2256.7053, 829.0), (-0.00024414061744797814, -109.68049212666126, -0.00021362305936007306), (1.0, 1.0, 1.0), "BP_Mines_Lift_Beam_B7", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_brk_mesh, _brk_mats, (4252.4414, 2178.5337, 2089.9995), (-90.0, 13.141140679335829, 121.85578886500589), (1.0, 1.0, 1.0), "BP_Mines_Lift_Beam_B70", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_brk_mesh, _brk_mats, (4213.552, 2139.6426, 2379.9995), (90.0, 84.32992745095008, 129.33249207674862), (1.0, 1.0, 1.0), "BP_Mines_Lift_Beam_B71", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_brk_mesh, _brk_mats, (4252.443, 2178.5332, 2379.9995), (-90.0, 13.141140679335829, 121.85578886500589), (1.0, 1.0, 1.0), "BP_Mines_Lift_Beam_B72", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_brk_mesh, _brk_mats, (1997.279, 4360.4434, 930.00433), (90.0, 169.6082578236083, 214.60715074057504), (1.0, 1.0, 1.0), "BP_Mines_Lift_Beam_B73", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_brk_mesh, _brk_mats, (2036.172, 4399.3354, 930.0041), (-90.0, -21.818872959116405, 156.8179184356773), (1.0, 1.0, 1.0), "BP_Mines_Lift_Beam_B74", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_brk_mesh, _brk_mats, (1997.28, 4360.442, 1220.0054), (90.0, -14.261517506187172, 30.736677299892886), (1.0, 1.0, 1.0), "BP_Mines_Lift_Beam_B75", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_brk_mesh, _brk_mats, (2036.1718, 4399.3345, 1220.0056), (-90.0, 31.07218984978592, 103.92704213211155), (1.0, 1.0, 1.0), "BP_Mines_Lift_Beam_B76", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_brk_mesh, _brk_mats, (1997.28, 4360.4424, 1510.0052), (90.0, -14.261517506187172, 30.736677299892886), (1.0, 1.0, 1.0), "BP_Mines_Lift_Beam_B77", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_brk_mesh, _brk_mats, (2036.173, 4399.333, 1510.0055), (-90.0, 31.07218984978592, 103.92704213211155), (1.0, 1.0, 1.0), "BP_Mines_Lift_Beam_B78", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_brk_mesh, _brk_mats, (1997.2808, 4360.4395, 1800.0054), (90.0, 169.6082578236083, 214.60715074057504), (1.0, 1.0, 1.0), "BP_Mines_Lift_Beam_B79", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_brk_mesh, _brk_mats, (3622.8176, 2305.4678, 1235.0), (4.099998486447656e-05, 25.319016747047744, 179.99976777355113), (1.0, 1.0, 1.0), "BP_Mines_Lift_Beam_B8", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_brk_mesh, _brk_mats, (2036.1732, 4399.3306, 1800.0054), (-90.0, -21.818872959116405, 156.8179184356773), (1.0, 1.0, 1.0), "BP_Mines_Lift_Beam_B80", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_brk_mesh, _brk_mats, (1997.283, 4360.436, 2090.0073), (90.0, -14.261517506187172, 30.736677299892886), (1.0, 1.0, 1.0), "BP_Mines_Lift_Beam_B81", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_brk_mesh, _brk_mats, (2036.174, 4399.33, 2090.0059), (-90.0, 31.07218984978592, 103.92704213211155), (1.0, 1.0, 1.0), "BP_Mines_Lift_Beam_B82", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_brk_mesh, _brk_mats, (1997.2827, 4360.4365, 2380.007), (90.0, 169.6082578236083, 214.60715074057504), (1.0, 1.0, 1.0), "BP_Mines_Lift_Beam_B83", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_brk_mesh, _brk_mats, (2036.1742, 4399.327, 2380.0068), (-90.0, 31.07218984978592, 103.92704213211155), (1.0, 1.0, 1.0), "BP_Mines_Lift_Beam_B84", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_brk_mesh, _brk_mats, (1997.2827, 4360.4365, 2665.007), (90.0, 169.6082578236083, 214.60715074057504), (1.0, 1.0, 1.0), "BP_Mines_Lift_Beam_B85_120", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_brk_mesh, _brk_mats, (2036.1742, 4399.327, 2665.0068), (-90.0, 28.57481116176582, 106.42448391574906), (1.0, 1.0, 1.0), "BP_Mines_Lift_Beam_B86_121", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_brk_mesh, _brk_mats, (4387.292, 2040.1156, 930.00385), (90.0, -17.539470276408466, -152.5405441017097), (1.0, 1.0, 1.0), "BP_Mines_Lift_Beam_B87_160", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_brk_mesh, _brk_mats, (4348.398, 2001.2238, 930.0036), (-90.0, -11.625963559314904, -33.37489420333863), (1.0, 1.0, 1.0), "BP_Mines_Lift_Beam_B88_161", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_brk_mesh, _brk_mats, (4387.2896, 2040.1171, 1220.0049), (90.0, 12.371569383358022, -122.63024479388669), (1.0, 1.0, 1.0), "BP_Mines_Lift_Beam_B89_162", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_brk_mesh, _brk_mats, (3627.0935, 2296.4294, 829.0), (-0.00024414062969634206, -64.68047870541469, -0.00021362305074100309), (1.0, 1.0, 1.0), "BP_Mines_Lift_Beam_B9", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_brk_mesh, _brk_mats, (4348.3975, 2001.225, 1220.0051), (-90.0, 141.97837532293855, -186.97923060488682), (1.0, 1.0, 1.0), "BP_Mines_Lift_Beam_B90_163", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_brk_mesh, _brk_mats, (4387.2896, 2040.1166, 1510.0048), (90.0, 12.371569383358022, -122.63024479388669), (1.0, 1.0, 1.0), "BP_Mines_Lift_Beam_B91_164", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_brk_mesh, _brk_mats, (4348.396, 2001.2262, 1510.005), (-90.0, 141.97837532293855, -186.97923060488682), (1.0, 1.0, 1.0), "BP_Mines_Lift_Beam_B92_165", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_brk_mesh, _brk_mats, (4387.289, 2040.1198, 1800.0049), (90.0, -17.539470276408466, -152.5405441017097), (1.0, 1.0, 1.0), "BP_Mines_Lift_Beam_B93_166", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_brk_mesh, _brk_mats, (4348.397, 2001.2286, 1800.0049), (-90.0, -11.625963559314904, -33.37489420333863), (1.0, 1.0, 1.0), "BP_Mines_Lift_Beam_B94_167", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_brk_mesh, _brk_mats, (4387.286, 2040.1239, 2090.0068), (90.0, 12.371569383358022, -122.63024479388669), (1.0, 1.0, 1.0), "BP_Mines_Lift_Beam_B95_168", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_brk_mesh, _brk_mats, (4348.3965, 2001.2294, 2090.0054), (-90.0, 141.97837532293855, -186.97923060488682), (1.0, 1.0, 1.0), "BP_Mines_Lift_Beam_B96_169", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_brk_mesh, _brk_mats, (4387.287, 2040.1227, 2380.007), (90.0, -17.539470276408466, -152.5405441017097), (1.0, 1.0, 1.0), "BP_Mines_Lift_Beam_B97", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_brk_mesh, _brk_mats, (4348.3955, 2001.2323, 2380.0068), (-90.0, 141.97837532293855, -186.97923060488682), (1.0, 1.0, 1.0), "BP_Mines_Lift_Beam_B98", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_brk_mesh, _brk_mats, (4387.287, 2040.1229, 2665.007), (90.0, -17.539470276408466, -152.5405441017097), (1.0, 1.0, 1.0), "BP_Mines_Lift_Beam_B99", _folder)
if a: placed += 1
else: skipped += 1

# Breakable Batch 5: BP_Mines_Lift_Beam_D (16 instances)
#   BP Class: /Game/LevelDesign/Deco/MinesDressing/BP_Mines_Lift_Beam_D
_brk_mesh = "/Game/Art/Assets/Kits/Deco/Mines/Machine/Mines_Machine_Lift_Pieces/Mines_Lift_Beam_D"
_brk_mats = ['/Game/Art/Assets/Kits/Deco/Mines/Machine/Mines_Machine_Lift_Pieces/Materials/Mi_Mines_Machine_Lift_C']
a = spawn_static_mesh(_brk_mesh, _brk_mats, (2306.2837, 3873.668, 986.151), (3.883093617983857e-05, -134.99997407910467, -44.998593354470735), (1.0, 1.0, 1.0), "BP_Mines_Lift_Beam_D_2", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_brk_mesh, _brk_mats, (2500.7192, 2330.4766, 986.151), (3.993368226460438e-05, -45.00012078086767, -44.99850847817955), (1.0, 1.0, 1.0), "BP_Mines_Lift_Beam_D10", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_brk_mesh, _brk_mats, (2332.5408, 2493.6555, 986.151), (3.993368226460438e-05, -45.00012078086767, -44.99850847817955), (1.0, 1.0, 1.0), "BP_Mines_Lift_Beam_D11", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_brk_mesh, _brk_mats, (2300.7195, 2525.4775, 986.151), (3.993368226460438e-05, -45.00012078086767, -44.99850847817955), (1.0, 1.0, 1.0), "BP_Mines_Lift_Beam_D12", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_brk_mesh, _brk_mats, (3866.7432, 4091.044, 986.151), (4.0771202042378684e-05, 135.00000582190316, -44.99848167582967), (1.0, 1.0, 1.0), "BP_Mines_Lift_Beam_D13", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_brk_mesh, _brk_mats, (3898.5657, 4059.2239, 986.151), (4.0771202042378684e-05, 135.00000582190316, -44.99848167582967), (1.0, 1.0, 1.0), "BP_Mines_Lift_Beam_D14", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_brk_mesh, _brk_mats, (4066.7441, 3896.0454, 986.151), (4.0771202042378684e-05, 135.00000582190316, -44.99848167582967), (1.0, 1.0, 1.0), "BP_Mines_Lift_Beam_D15", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_brk_mesh, _brk_mats, (4098.5625, 3864.2244, 986.151), (4.0771202042378684e-05, 135.00000582190316, -44.99848167582967), (1.0, 1.0, 1.0), "BP_Mines_Lift_Beam_D16", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_brk_mesh, _brk_mats, (2338.1045, 3905.4888, 986.151), (3.883093617983857e-05, -134.99997407910467, -44.998593354470735), (1.0, 1.0, 1.0), "BP_Mines_Lift_Beam_D2", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_brk_mesh, _brk_mats, (2501.2837, 4073.668, 986.151), (3.883093617983857e-05, -134.99997407910467, -44.998593354470735), (1.0, 1.0, 1.0), "BP_Mines_Lift_Beam_D3", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_brk_mesh, _brk_mats, (2533.1045, 4105.491, 986.151), (3.883093617983857e-05, -134.99997407910467, -44.998593354470735), (1.0, 1.0, 1.0), "BP_Mines_Lift_Beam_D4", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_brk_mesh, _brk_mats, (4093.6099, 2537.4988, 986.151), (4.010426127870442e-05, 44.999992762119525, -44.998531719285005), (1.0, 1.0, 1.0), "BP_Mines_Lift_Beam_D5_26", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_brk_mesh, _brk_mats, (4061.79, 2505.6777, 986.151), (4.010426127870442e-05, 44.999992762119525, -44.998531719285005), (1.0, 1.0, 1.0), "BP_Mines_Lift_Beam_D6_27", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_brk_mesh, _brk_mats, (3898.6123, 2337.4985, 986.151), (4.010426127870442e-05, 44.999992762119525, -44.998531719285005), (1.0, 1.0, 1.0), "BP_Mines_Lift_Beam_D7_28", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_brk_mesh, _brk_mats, (3866.7913, 2305.6777, 986.151), (4.010426127870442e-05, 44.999992762119525, -44.998531719285005), (1.0, 1.0, 1.0), "BP_Mines_Lift_Beam_D8_29", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_brk_mesh, _brk_mats, (2532.541, 2298.6565, 986.151), (3.993368226460438e-05, -45.00012078086767, -44.99850847817955), (1.0, 1.0, 1.0), "BP_Mines_Lift_Beam_D9", _folder)
if a: placed += 1
else: skipped += 1

# Breakable Batch 6: BP_Mines_Machine_Whim_Side_Bracket (16 instances)
#   BP Class: /Game/LevelDesign/Deco/MinesDressing/BP_Mines_Machine_Whim_Side_Bracket
_brk_mesh = "/Game/Art/Assets/Kits/Deco/Mines/Machine/Mines_Machine_Whim_Pieces/Mines_Machine_Whim_Side_Bracket"
_brk_mats = ['/Game/Art/Assets/Kits/Deco/Mines/Materials/Mines_Machine_Whim/MI_Mines_Machine_Whim_Trim', '/Game/Art/Assets/Kits/Deco/Mines/Materials/Mines_Machine_Whim/MI_Mines_Machine_Whim_Uniq']
a = spawn_static_mesh(_brk_mesh, _brk_mats, (2317.7478, 3573.5413, 1030.0), (0.0, 67.50001780578428, -0.0), (1.0, 1.0, 1.0), "BP_Mines_Machine_Whim_Side_Bracket_2", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_brk_mesh, _brk_mats, (4149.381, 2784.4814, 1030.0), (0.0, 70.31233296278056, -0.0), (1.0, 1.0, 1.0), "BP_Mines_Machine_Whim_Side_Bracket10", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_brk_mesh, _brk_mats, (4089.669, 3555.8823, 1030.0), (0.0, -67.50018225731912, 0.0), (1.0, 1.0, 1.0), "BP_Mines_Machine_Whim_Side_Bracket11", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_brk_mesh, _brk_mats, (4158.9604, 3584.5862, 1030.0), (0.0, 112.49968794040448, -0.0), (1.0, 1.0, 1.0), "BP_Mines_Machine_Whim_Side_Bracket12", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_brk_mesh, _brk_mats, (3577.3752, 4079.9297, 1030.0), (0.0, -22.499999128211993, 0.0), (1.0, 1.0, 1.0), "BP_Mines_Machine_Whim_Side_Bracket13_24", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_brk_mesh, _brk_mats, (3606.0757, 4149.2227, 1030.0), (0.0, 157.4995995822639, -0.0), (1.0, 1.0, 1.0), "BP_Mines_Machine_Whim_Side_Bracket14_25", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_brk_mesh, _brk_mats, (2845.3423, 4088.291, 1030.0), (0.0, 22.499999128211993, -0.0), (1.0, 1.0, 1.0), "BP_Mines_Machine_Whim_Side_Bracket15_28", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_brk_mesh, _brk_mats, (2816.6387, 4157.5825, 1030.0), (0.0, -157.50040859056813, 0.0), (1.0, 1.0, 1.0), "BP_Mines_Machine_Whim_Side_Bracket16_29", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_brk_mesh, _brk_mats, (2248.457, 3602.2412, 1030.0), (0.0, -112.50002179918758, 0.0), (1.0, 1.0, 1.0), "BP_Mines_Machine_Whim_Side_Bracket2", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_brk_mesh, _brk_mats, (2308.3862, 2842.5068, 1030.0), (0.0, 112.49989578163905, -0.0), (1.0, 1.0, 1.0), "BP_Mines_Machine_Whim_Side_Bracket3_8", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_brk_mesh, _brk_mats, (2239.096, 2813.8047, 1030.0), (0.0, -67.50012484543348, 0.0), (1.0, 1.0, 1.0), "BP_Mines_Machine_Whim_Side_Bracket4_9", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_brk_mesh, _brk_mats, (2883.0393, 2299.2017, 1030.0), (0.0, 160.31223324233, -0.0), (1.0, 1.0, 1.0), "BP_Mines_Machine_Whim_Side_Bracket5", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_brk_mesh, _brk_mats, (2857.7734, 2228.5857, 1030.0), (0.0, -19.687592483590347, 0.0), (1.0, 1.0, 1.0), "BP_Mines_Machine_Whim_Side_Bracket6", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_brk_mesh, _brk_mats, (3609.0754, 2338.5103, 1030.0), (0.0, -154.68777673968043, 0.0), (1.0, 1.0, 1.0), "BP_Mines_Machine_Whim_Side_Bracket7", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_brk_mesh, _brk_mats, (3641.1436, 2270.7117, 1030.0), (0.0, 25.312366410227874, -0.0), (1.0, 1.0, 1.0), "BP_Mines_Machine_Whim_Side_Bracket8", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_brk_mesh, _brk_mats, (4078.7637, 2809.7466, 1030.0), (0.0, -109.68773639127592, 0.0), (1.0, 1.0, 1.0), "BP_Mines_Machine_Whim_Side_Bracket9", _folder)
if a: placed += 1
else: skipped += 1

# Breakable Batch 7: BP_Mines_Machine_Whim_Side_Support (8 instances)
#   BP Class: /Game/LevelDesign/Deco/MinesDressing/BP_Mines_Machine_Whim_Side_Support
_brk_mesh = "/Game/Art/Assets/Kits/Deco/Mines/Machine/Mines_Machine_Whim_Pieces/Mines_Machine_Whim_Side_Support"
_brk_mats = ['/Game/Art/Assets/Kits/Deco/Mines/Materials/Mines_Machine_Whim/MI_Mines_Machine_Whim_Trim', '/Game/Art/Assets/Kits/Deco/Mines/Materials/Mines_Machine_Whim/MI_Mines_Machine_Whim_Uniq']
a = spawn_static_mesh(_brk_mesh, _brk_mats, (2285.473, 3586.8374, 840.0), (0.0, -22.499938715362745, 0.0), (1.0, 1.0, 1.0), "BP_Mines_Machine_Whim_Side_Support_2", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_brk_mesh, _brk_mats, (3624.0605, 2306.9836, 840.0), (0.0, 115.31212055596835, -0.0), (1.0, 1.0, 1.0), "BP_Mines_Machine_Whim_Side_Support10", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_brk_mesh, _brk_mats, (4111.654, 2798.0503, 840.0), (0.0, 160.31200422935922, -0.0), (1.0, 1.0, 1.0), "BP_Mines_Machine_Whim_Side_Support11", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_brk_mesh, _brk_mats, (4121.8936, 3569.3035, 840.0), (0.0, -157.50047742796428, 0.0), (1.0, 1.0, 1.0), "BP_Mines_Machine_Whim_Side_Support12", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_brk_mesh, _brk_mats, (3590.6714, 4112.2056, 840.0), (0.0, -112.50033646488657, 0.0), (1.0, 1.0, 1.0), "BP_Mines_Machine_Whim_Side_Support13_11", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_brk_mesh, _brk_mats, (2831.9214, 4120.515, 840.0), (0.0, -67.50024275117556, 0.0), (1.0, 1.0, 1.0), "BP_Mines_Machine_Whim_Side_Support14_13", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_brk_mesh, _brk_mats, (2276.1626, 2829.0864, 840.0), (0.0, 22.49985915789503, -0.0), (1.0, 1.0, 1.0), "BP_Mines_Machine_Whim_Side_Support2_2", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_brk_mesh, _brk_mats, (2871.3425, 2266.313, 840.0), (0.0, 70.31224947754946, -0.0), (1.0, 1.0, 1.0), "BP_Mines_Machine_Whim_Side_Support9_4", _folder)
if a: placed += 1
else: skipped += 1

# Breakable Batch 8: BP_Mines_Machine_Whim_Wheel_Middle_Bracket (8 instances)
#   BP Class: /Game/LevelDesign/Deco/MinesDressing/BP_Mines_Machine_Whim_Wheel_Middle_Bracket
_brk_mesh = "/Game/Art/Assets/Kits/Deco/Mines/Machine/Mines_Machine_Whim_Pieces/Mines_Machine_Whim_Wheel_Middle_Bracket"
_brk_mats = ['/Game/Art/Assets/Kits/Deco/Mines/Materials/Mines_Machine_Whim/MI_Mines_Machine_Whim_Trim', '/Game/Art/Assets/Kits/Deco/Mines/Materials/Mines_Machine_Whim/MI_Mines_Machine_Whim_Uniq']
a = spawn_static_mesh(_brk_mesh, _brk_mats, (1994.0854, 4218.0796, 999.99945), (0.0, 45.00001098709003, -0.0), (1.0, 1.0, 1.0), "BP_Mines_Machine_Whim_Wheel_Middle_Bracket_2", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_brk_mesh, _brk_mats, (2192.075, 4416.0728, 999.99945), (0.0, 45.00001098709003, -0.0), (1.0, 1.0, 1.0), "BP_Mines_Machine_Whim_Wheel_Middle_Bracket2_2", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_brk_mesh, _brk_mats, (4408.6, 2190.346, 999.99945), (0.0, -134.9999263430944, 0.0), (1.0, 1.0, 1.0), "BP_Mines_Machine_Whim_Wheel_Middle_Bracket3_11", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_brk_mesh, _brk_mats, (4210.6104, 1992.3524, 999.99945), (0.0, -134.9999263430944, 0.0), (1.0, 1.0, 1.0), "BP_Mines_Machine_Whim_Wheel_Middle_Bracket4_12", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_brk_mesh, _brk_mats, (2189.072, 1987.3552, 999.99945), (0.0, 134.9999263430944, -0.0), (1.0, 1.0, 1.0), "BP_Mines_Machine_Whim_Wheel_Middle_Bracket5", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_brk_mesh, _brk_mats, (1991.0791, 2185.345, 999.99945), (0.0, 134.9999263430944, -0.0), (1.0, 1.0, 1.0), "BP_Mines_Machine_Whim_Wheel_Middle_Bracket6", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_brk_mesh, _brk_mats, (4213.274, 4405.404, 999.99945), (0.0, -45.00002828938376, 0.0), (1.0, 1.0, 1.0), "BP_Mines_Machine_Whim_Wheel_Middle_Bracket7", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_brk_mesh, _brk_mats, (4411.2676, 4207.4146, 999.99945), (0.0, -45.00002828938376, 0.0), (1.0, 1.0, 1.0), "BP_Mines_Machine_Whim_Wheel_Middle_Bracket8", _folder)
if a: placed += 1
else: skipped += 1

# Breakable Batch 9: BP_DM_Orc_Shanty_Midden_C_A_Breakable (1 instances)
#   BP Class: /Game/LevelDesign/Deco/Orc_Shanty/BP_DM_Orc_Shanty_Midden_C_A_Breakable
_brk_mesh = "/Game/Art/Assets/Kits/Deco/Orc/Shanty/Orc_Shanty_Midden_C_A"
_brk_mats = ['/Game/Art/Assets/Kits/Deco/Orc/Shanty/Material/Orc_Shanty_Midden/MI_Orc_Shanty_Midden_Mat_Inst', '/Game/Art/Assets/Kits/Deco/Orc/Shanty/Material/Orc_Shanty_Midden/MI_Orc_Shanty_Midden_Tileable_B_Mat_Inst']
a = spawn_static_mesh(_brk_mesh, _brk_mats, (2454.0, 2465.0, 822.0), (0.0, 0.0, -0.0), (1.0, 1.0, 1.0), "BP_DM_Orc_Shanty_Midden_C_A_Breakable_2", _folder)
if a: placed += 1
else: skipped += 1

# Breakable Batch 10: BP_DM_Orc_Shanty_Midden_C_B_Breakable (2 instances)
#   BP Class: /Game/LevelDesign/Deco/Orc_Shanty/BP_DM_Orc_Shanty_Midden_C_B_Breakable
_brk_mesh = "/Game/Art/Assets/Kits/Deco/Orc/Shanty/Orc_Shanty_Midden_C_B"
_brk_mats = ['/Game/Art/Assets/Kits/Deco/Orc/Shanty/Material/Orc_Shanty_Midden/MI_Orc_Shanty_Midden_Mat_Inst', '/Game/Art/Assets/Kits/Deco/Orc/Shanty/Material/Orc_Shanty_Midden/MI_Orc_Shanty_Midden_Tileable_C_Mat_Inst']
a = spawn_static_mesh(_brk_mesh, _brk_mats, (2654.0, 2297.0, 832.0), (0.0, 0.0, -0.0), (1.0, 1.0, 1.0), "BP_DM_Orc_Shanty_Midden_C_B_Breakable_2", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_brk_mesh, _brk_mats, (3733.0, 2294.0, 824.0), (5.3399572489317775, 7.07208290166085e-08, -2.1528625989780816), (1.0, 1.0, 1.0), "BP_DM_Orc_Shanty_Midden_C_B_Breakable2_5", _folder)
if a: placed += 1
else: skipped += 1

# --- Extra DecoVolumes (not construction blocks) ---
_folder = "Reconstruction/BD_BB_Chapter2_Orctown_Throne/DecoVolumes"

# DecoVolume: BP_DM_Mine_tailings_Debris_2x2_C_2 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (2222.685, 1948.3262, 822.75964), (0.0, 0.0, -0.0), (2.9824, 2.9824, 0.7345), "DV_BP_DM_Mine_tailings_Debris_2x2_C_2_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_DM_Mine_tailings_Debris_2x2_C2 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (4169.2646, 1928.3805, 822.75964), (0.0, 0.0, -0.0), (2.9824, 2.9824, 0.7345), "DV_BP_DM_Mine_tailings_Debris_2x2_C2_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_DM_Mine_tailings_Debris_2x2_C3 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (4472.685, 4148.326, 822.75964), (0.0, 0.0, -0.0), (2.9824, 2.9824, 0.7345), "DV_BP_DM_Mine_tailings_Debris_2x2_C3_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_DM_Mine_tailings_Debris_2x2_C4 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (1969.2649, 4178.3804, 822.75964), (0.0, 0.0, -0.0), (2.9824, 2.9824, 0.7345), "DV_BP_DM_Mine_tailings_Debris_2x2_C4_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_DM_Mine_tailings_Debris_3x3_B_5 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (1953.0764, 2250.0774, 815.01996), (0.0, 0.0, -0.0), (4.1941, 4.1942, 0.6855), "DV_BP_DM_Mine_tailings_Debris_3x3_B_5_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_DM_Mine_tailings_Debris_3x3_B2 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (4471.016, 2197.9885, 815.01996), (0.0, 0.0, -0.0), (4.1942, 4.1941, 0.6855), "DV_BP_DM_Mine_tailings_Debris_3x3_B2_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_DM_Mine_tailings_Debris_3x3_B3 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (4203.076, 4450.0767, 815.01996), (0.0, 0.0, -0.0), (4.1941, 4.1942, 0.6855), "DV_BP_DM_Mine_tailings_Debris_3x3_B3_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_DM_Mine_tailings_Debris_3x3_B4 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (2271.0164, 4447.989, 815.01996), (0.0, 0.0, -0.0), (4.1942, 4.1941, 0.6855), "DV_BP_DM_Mine_tailings_Debris_3x3_B4_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_DM_Orc_Flag_2 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (2557.849, 3238.9185, 1522.2561), (0.0, 0.0, -0.0), (1.5481, 2.1519, 6.4553), "DV_BP_DM_Orc_Flag_2_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_DM_Orc_Shanty_Midden_A_A_Breakable_2 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (4227.2715, 3731.38, 828.57874), (0.0, 0.0, -0.0), (2.5364, 2.5987, 0.6708), "DV_BP_DM_Orc_Shanty_Midden_A_A_Breakable_2_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_DM_Orc_Shanty_Midden_A_A_Breakable2_5 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (2763.9263, 2286.489, 873.2051), (0.0, 0.0, -0.0), (2.5482, 2.6556, 0.9775), "DV_BP_DM_Orc_Shanty_Midden_A_A_Breakable2_5_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_DM_Orc_Shanty_Midden_A_B_Breakable_2 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (4090.8428, 3734.0256, 863.3532), (0.0, 0.0, -0.0), (2.2051, 2.4036, 0.7731), "DV_BP_DM_Orc_Shanty_Midden_A_B_Breakable_2_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_DM_Orc_Shanty_Midden_A_B_Breakable2_5 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (2286.8428, 3794.182, 846.3614), (0.0, 0.0, -0.0), (2.2051, 2.3645, 0.5886), "DV_BP_DM_Orc_Shanty_Midden_A_B_Breakable2_5_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_DM_Orc_Shanty_Midden_A_B_Breakable3 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (2456.2678, 3949.2827, 853.5228), (0.0, 0.0, -0.0), (2.7835, 2.6455, 0.8954), "DV_BP_DM_Orc_Shanty_Midden_A_B_Breakable3_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_DM_Orc_Shanty_Midden_A_B_Breakable4_9 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (3753.625, 4036.1816, 867.50073), (0.0, 0.0, -0.0), (2.2235, 2.3905, 0.7619), "DV_BP_DM_Orc_Shanty_Midden_A_B_Breakable4_9_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_DM_Orc_Shanty_Midden_C_A_Breakable_2 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (2463.9946, 2465.737, 846.83496), (0.0, 0.0, -0.0), (2.4698, 2.5982, 0.7801), "DV_BP_DM_Orc_Shanty_Midden_C_A_Breakable_2_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_DM_Orc_Shanty_Midden_C_B_Breakable_2 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (2652.8948, 2297.1633, 852.7937), (0.0, 0.0, -0.0), (2.2650, 2.5547, 0.6993), "DV_BP_DM_Orc_Shanty_Midden_C_B_Breakable_2_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_DM_Orc_Shanty_Midden_C_B_Breakable2_5 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (3729.9653, 2293.382, 844.5921), (0.0, 0.0, -0.0), (2.3292, 2.5792, 1.0021), "DV_BP_DM_Orc_Shanty_Midden_C_B_Breakable2_5_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_DM_Orc_Shanty_Midden_C_D_Breakable_2 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (2670.7817, 4229.404, 819.3863), (0.0, 0.0, -0.0), (2.3125, 2.5173, 0.6920), "DV_BP_DM_Orc_Shanty_Midden_C_D_Breakable_2_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_DM_Orc_Shanty_Midden_C_D_Breakable2_5 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (2318.2556, 2578.491, 845.6572), (0.0, 0.0, -0.0), (2.0396, 2.1102, 0.5166), "DV_BP_DM_Orc_Shanty_Midden_C_D_Breakable2_5_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_DM_Orc_Shanty_Midden_C_D_Breakable3_8 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (3879.4048, 2257.5186, 816.2531), (0.0, 0.0, -0.0), (2.8832, 2.7499, 0.6988), "DV_BP_DM_Orc_Shanty_Midden_C_D_Breakable3_8_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_DM_Orc_Shanty_Midden_D_A_Breakable_2 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (2727.6887, 4202.7295, 839.8221), (0.0, 0.0, -0.0), (2.0483, 2.0958, 0.6607), "DV_BP_DM_Orc_Shanty_Midden_D_A_Breakable_2_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_DM_Orc_Shanty_Midden_D_A_Breakable2_5 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (3998.662, 2387.0637, 823.57336), (0.0, 0.0, -0.0), (1.9940, 2.1318, 0.6844), "DV_BP_DM_Orc_Shanty_Midden_D_A_Breakable2_5_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_DM_Orc_Shanty_Midden_D_B_Breakable_2 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (2622.0947, 4144.489, 842.62177), (0.0, 0.0, -0.0), (1.4269, 1.2430, 0.4872), "DV_BP_DM_Orc_Shanty_Midden_D_B_Breakable_2_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_DM_Orc_Shanty_Midden_D_C_Breakable_2 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (4191.483, 2638.248, 812.7306), (0.0, 0.0, -0.0), (1.8893, 1.9741, 0.3650), "DV_BP_DM_Orc_Shanty_Midden_D_C_Breakable_2_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_DM_Orc_Shanty_Midden_D_C_Breakable2_5 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (4152.0596, 2692.6304, 831.4481), (0.0, 0.0, -0.0), (2.0728, 2.0329, 0.7338), "DV_BP_DM_Orc_Shanty_Midden_D_C_Breakable2_5_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_DM_Warren_lighting_Banner_A_Breakable_2 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (2205.1477, 3734.3962, 1001.56464), (0.0, 0.0, -0.0), (2.4132, 2.6152, 4.3417), "DV_BP_DM_Warren_lighting_Banner_A_Breakable_2_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_DM_Warren_lighting_Banner_A_Breakable2 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (2205.1477, 2684.3962, 1001.56464), (0.0, 0.0, -0.0), (2.4132, 2.6152, 4.3417), "DV_BP_DM_Warren_lighting_Banner_A_Breakable2_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_DM_Warren_lighting_Fireplace_A_Small_Breakable_Burning_2 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (3190.7522, 3216.044, 978.9774), (0.0, 0.0, -0.0), (2.3681, 2.2207, 1.8108), "DV_BP_DM_Warren_lighting_Fireplace_A_Small_Breakable_Burning_2_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_DM_Warren_Lighting_Torch_Breakable_5 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (2769.9226, 2118.021, 869.8237), (0.0, 0.0, -0.0), (1.4762, 1.4762, 1.9128), "DV_BP_DM_Warren_Lighting_Torch_Breakable_5_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_DM_Warren_Lighting_Torch_Breakable2 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (3735.2146, 2170.7883, 869.8237), (0.0, 0.0, -0.0), (1.1582, 1.2133, 1.9128), "DV_BP_DM_Warren_Lighting_Torch_Breakable2_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_Mines_Lift_Beam_B10 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (4111.8447, 2796.0999, 1234.6392), (0.0, 0.0, -0.0), (1.2685, 2.8667, 0.4114), "DV_BP_Mines_Lift_Beam_B10_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_Mines_Lift_Beam_B100 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (4348.65, 2000.9766, 2665.0068), (0.0, 0.0, -0.0), (0.5003, 0.5003, 2.9386), "DV_BP_Mines_Lift_Beam_B100_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_Mines_Lift_Beam_B101 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (2035.7319, 1994.1813, 930.00433), (0.0, 0.0, -0.0), (0.5003, 0.5003, 2.9386), "DV_BP_Mines_Lift_Beam_B101_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_Mines_Lift_Beam_B102 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (1996.838, 2033.0753, 930.0041), (0.0, 0.0, -0.0), (0.5003, 0.5003, 2.9386), "DV_BP_Mines_Lift_Beam_B102_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_Mines_Lift_Beam_B103 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (2035.7325, 1994.182, 1220.0054), (0.0, 0.0, -0.0), (0.5003, 0.5003, 2.9386), "DV_BP_Mines_Lift_Beam_B103_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_Mines_Lift_Beam_B104 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (1996.8383, 2033.074, 1220.0056), (0.0, 0.0, -0.0), (0.5003, 0.5003, 2.9386), "DV_BP_Mines_Lift_Beam_B104_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_Mines_Lift_Beam_B105 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (2035.7325, 1994.182, 1510.0052), (0.0, 0.0, -0.0), (0.5003, 0.5003, 2.9386), "DV_BP_Mines_Lift_Beam_B105_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_Mines_Lift_Beam_B106 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (1996.8395, 2033.0754, 1510.0055), (0.0, 0.0, -0.0), (0.5003, 0.5003, 2.9386), "DV_BP_Mines_Lift_Beam_B106_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_Mines_Lift_Beam_B107 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (2035.7356, 1994.1827, 1800.0054), (0.0, 0.0, -0.0), (0.5003, 0.5003, 2.9386), "DV_BP_Mines_Lift_Beam_B107_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_Mines_Lift_Beam_B108 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (1996.8429, 2033.0763, 1800.0054), (0.0, 0.0, -0.0), (0.5003, 0.5003, 2.9386), "DV_BP_Mines_Lift_Beam_B108_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_Mines_Lift_Beam_B109 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (2035.7394, 1994.1852, 2090.0073), (0.0, 0.0, -0.0), (0.5003, 0.5003, 2.9386), "DV_BP_Mines_Lift_Beam_B109_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_Mines_Lift_Beam_B11 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (4121.261, 2792.7314, 829.36084), (0.0, 0.0, -0.0), (2.8667, 1.2684, 0.4114), "DV_BP_Mines_Lift_Beam_B11_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_Mines_Lift_Beam_B110 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (1996.8431, 2033.0771, 2090.0059), (0.0, 0.0, -0.0), (0.5003, 0.5003, 2.9386), "DV_BP_Mines_Lift_Beam_B110_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_Mines_Lift_Beam_B111 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (2035.739, 1994.1849, 2380.007), (0.0, 0.0, -0.0), (0.5003, 0.5003, 2.9386), "DV_BP_Mines_Lift_Beam_B111_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_Mines_Lift_Beam_B112 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (1996.8453, 2033.0764, 2380.0068), (0.0, 0.0, -0.0), (0.5003, 0.5003, 2.9386), "DV_BP_Mines_Lift_Beam_B112_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_Mines_Lift_Beam_B113 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (2035.739, 1994.1849, 2665.007), (0.0, 0.0, -0.0), (0.5003, 0.5003, 2.9386), "DV_BP_Mines_Lift_Beam_B113_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_Mines_Lift_Beam_B114 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (1996.8453, 2033.0764, 2665.0068), (0.0, 0.0, -0.0), (0.5003, 0.5003, 2.9386), "DV_BP_Mines_Lift_Beam_B114_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_Mines_Lift_Beam_B115 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (4363.6377, 4398.8506, 930.00385), (0.0, 0.0, -0.0), (0.5003, 0.5003, 2.9386), "DV_BP_Mines_Lift_Beam_B115_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_Mines_Lift_Beam_B116 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (4402.5293, 4359.954, 930.0036), (0.0, 0.0, -0.0), (0.5003, 0.5003, 2.9386), "DV_BP_Mines_Lift_Beam_B116_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_Mines_Lift_Beam_B117 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (4363.637, 4398.848, 1220.0049), (0.0, 0.0, -0.0), (0.5003, 0.5003, 2.9386), "DV_BP_Mines_Lift_Beam_B117_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_Mines_Lift_Beam_B118 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (4402.5283, 4359.954, 1220.0051), (0.0, 0.0, -0.0), (0.5003, 0.5003, 2.9386), "DV_BP_Mines_Lift_Beam_B118_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_Mines_Lift_Beam_B119 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (4363.637, 4398.8477, 1510.0048), (0.0, 0.0, -0.0), (0.5003, 0.5003, 2.9386), "DV_BP_Mines_Lift_Beam_B119_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_Mines_Lift_Beam_B12 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (4123.346, 3567.9868, 1234.6392), (0.0, 0.0, -0.0), (1.3984, 2.8281, 0.4114), "DV_BP_Mines_Lift_Beam_B12_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_Mines_Lift_Beam_B120 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (4402.528, 4359.953, 1510.005), (0.0, 0.0, -0.0), (0.5003, 0.5003, 2.9386), "DV_BP_Mines_Lift_Beam_B120_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_Mines_Lift_Beam_B121 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (4363.6333, 4398.8467, 1800.0049), (0.0, 0.0, -0.0), (0.5003, 0.5003, 2.9386), "DV_BP_Mines_Lift_Beam_B121_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_Mines_Lift_Beam_B122 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (4402.5244, 4359.953, 1800.0049), (0.0, 0.0, -0.0), (0.5003, 0.5003, 2.9386), "DV_BP_Mines_Lift_Beam_B122_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_Mines_Lift_Beam_B123 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (4363.63, 4398.8447, 2090.0068), (0.0, 0.0, -0.0), (0.5003, 0.5003, 2.9386), "DV_BP_Mines_Lift_Beam_B123_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_Mines_Lift_Beam_B124 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (4402.5244, 4359.952, 2090.0054), (0.0, 0.0, -0.0), (0.5003, 0.5003, 2.9386), "DV_BP_Mines_Lift_Beam_B124_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_Mines_Lift_Beam_B125 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (4363.631, 4398.8457, 2380.007), (0.0, 0.0, -0.0), (0.5003, 0.5003, 2.9386), "DV_BP_Mines_Lift_Beam_B125_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_Mines_Lift_Beam_B126 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (4402.5215, 4359.952, 2380.0068), (0.0, 0.0, -0.0), (0.5003, 0.5003, 2.9386), "DV_BP_Mines_Lift_Beam_B126_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_Mines_Lift_Beam_B127 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (4363.631, 4398.845, 2665.007), (0.0, 0.0, -0.0), (0.5003, 0.5003, 2.9386), "DV_BP_Mines_Lift_Beam_B127_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_Mines_Lift_Beam_B128 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (4402.521, 4359.952, 2665.0068), (0.0, 0.0, -0.0), (0.5003, 0.5003, 2.9386), "DV_BP_Mines_Lift_Beam_B128_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_Mines_Lift_Beam_B13 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (4132.5845, 3571.8145, 829.36084), (0.0, 0.0, -0.0), (2.8281, 1.3984, 0.4114), "DV_BP_Mines_Lift_Beam_B13_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_Mines_Lift_Beam_B14_24 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (3592.63, 4112.302, 1234.6392), (0.0, 0.0, -0.0), (2.8283, 1.3978, 0.4114), "DV_BP_Mines_Lift_Beam_B14_24_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_Mines_Lift_Beam_B15_25 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (3596.4553, 4121.5425, 829.36084), (0.0, 0.0, -0.0), (1.3978, 2.8283, 0.4114), "DV_BP_Mines_Lift_Beam_B15_25_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_Mines_Lift_Beam_B16_28 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (2833.2385, 4121.9688, 1234.6392), (0.0, 0.0, -0.0), (2.8281, 1.3984, 0.4114), "DV_BP_Mines_Lift_Beam_B16_28_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_Mines_Lift_Beam_B17_29 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (2829.4097, 4131.207, 829.36084), (0.0, 0.0, -0.0), (1.3984, 2.8281, 0.4114), "DV_BP_Mines_Lift_Beam_B17_29_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_Mines_Lift_Beam_B2_2 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (2285.3772, 3588.7944, 1234.6392), (0.0, 0.0, -0.0), (1.3978, 2.8283, 0.4114), "DV_BP_Mines_Lift_Beam_B2_2_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_Mines_Lift_Beam_B25 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (4268.888, 4224.3877, 930.0), (0.0, 0.0, -0.0), (0.5003, 0.5003, 2.9386), "DV_BP_Mines_Lift_Beam_B25_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_Mines_Lift_Beam_B26 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (4229.9946, 4263.2812, 930.0), (0.0, 0.0, -0.0), (0.5003, 0.5003, 2.9386), "DV_BP_Mines_Lift_Beam_B26_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_Mines_Lift_Beam_B27 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (4268.888, 4224.3877, 1220.0), (0.0, 0.0, -0.0), (0.5003, 0.5003, 2.9386), "DV_BP_Mines_Lift_Beam_B27_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_Mines_Lift_Beam_B28 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (4229.9946, 4263.2812, 1220.0), (0.0, 0.0, -0.0), (0.5003, 0.5003, 2.9386), "DV_BP_Mines_Lift_Beam_B28_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_Mines_Lift_Beam_B29 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (4268.888, 4224.3877, 1510.0), (0.0, 0.0, -0.0), (0.5003, 0.5003, 2.9386), "DV_BP_Mines_Lift_Beam_B29_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_Mines_Lift_Beam_B3 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (2276.1382, 3592.6216, 829.36084), (0.0, 0.0, -0.0), (2.8283, 1.3978, 0.4114), "DV_BP_Mines_Lift_Beam_B3_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_Mines_Lift_Beam_B30 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (4229.9946, 4263.2812, 1510.0), (0.0, 0.0, -0.0), (0.5003, 0.5003, 2.9386), "DV_BP_Mines_Lift_Beam_B30_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_Mines_Lift_Beam_B31 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (4268.888, 4224.3877, 1800.0), (0.0, 0.0, -0.0), (0.5003, 0.5003, 2.9386), "DV_BP_Mines_Lift_Beam_B31_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_Mines_Lift_Beam_B32 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (4229.9946, 4263.2812, 1800.0), (0.0, 0.0, -0.0), (0.5003, 0.5003, 2.9386), "DV_BP_Mines_Lift_Beam_B32_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_Mines_Lift_Beam_B33 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (4268.888, 4224.3877, 2090.0), (0.0, 0.0, -0.0), (0.5003, 0.5003, 2.9386), "DV_BP_Mines_Lift_Beam_B33_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_Mines_Lift_Beam_B34 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (4229.9946, 4263.2812, 2090.0), (0.0, 0.0, -0.0), (0.5003, 0.5003, 2.9386), "DV_BP_Mines_Lift_Beam_B34_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_Mines_Lift_Beam_B35 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (4268.888, 4224.3877, 2380.0), (0.0, 0.0, -0.0), (0.5003, 0.5003, 2.9386), "DV_BP_Mines_Lift_Beam_B35_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_Mines_Lift_Beam_B36 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (4229.9946, 4263.2812, 2380.0), (0.0, 0.0, -0.0), (0.5003, 0.5003, 2.9386), "DV_BP_Mines_Lift_Beam_B36_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_Mines_Lift_Beam_B37 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (2135.8586, 2167.226, 930.0006), (0.0, 0.0, -0.0), (0.5003, 0.5003, 2.9386), "DV_BP_Mines_Lift_Beam_B37_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_Mines_Lift_Beam_B38 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (2174.7517, 2128.332, 930.0001), (0.0, 0.0, -0.0), (0.5003, 0.5003, 2.9386), "DV_BP_Mines_Lift_Beam_B38_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_Mines_Lift_Beam_B39 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (2135.8625, 2167.2217, 1220.0004), (0.0, 0.0, -0.0), (0.5003, 0.5003, 2.9386), "DV_BP_Mines_Lift_Beam_B39_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_Mines_Lift_Beam_B4_8 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (2274.7104, 2830.403, 1234.6392), (0.0, 0.0, -0.0), (1.3984, 2.8281, 0.4114), "DV_BP_Mines_Lift_Beam_B4_8_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_Mines_Lift_Beam_B40 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (2174.7556, 2128.3284, 1220.0004), (0.0, 0.0, -0.0), (0.5003, 0.5003, 2.9386), "DV_BP_Mines_Lift_Beam_B40_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_Mines_Lift_Beam_B41 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (2135.8657, 2167.2185, 1510.0004), (0.0, 0.0, -0.0), (0.5003, 0.5003, 2.9386), "DV_BP_Mines_Lift_Beam_B41_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_Mines_Lift_Beam_B42 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (2174.759, 2128.325, 1510.0004), (0.0, 0.0, -0.0), (0.5003, 0.5003, 2.9386), "DV_BP_Mines_Lift_Beam_B42_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_Mines_Lift_Beam_B43 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (2135.8691, 2167.215, 1800.0004), (0.0, 0.0, -0.0), (0.5003, 0.5003, 2.9386), "DV_BP_Mines_Lift_Beam_B43_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_Mines_Lift_Beam_B44 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (2174.763, 2128.3218, 1800.0001), (0.0, 0.0, -0.0), (0.5003, 0.5003, 2.9386), "DV_BP_Mines_Lift_Beam_B44_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_Mines_Lift_Beam_B45 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (2135.8735, 2167.212, 2090.0002), (0.0, 0.0, -0.0), (0.5003, 0.5003, 2.9386), "DV_BP_Mines_Lift_Beam_B45_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_Mines_Lift_Beam_B46 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (2174.7664, 2128.3179, 2090.0002), (0.0, 0.0, -0.0), (0.5003, 0.5003, 2.9386), "DV_BP_Mines_Lift_Beam_B46_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_Mines_Lift_Beam_B47 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (2135.877, 2167.2078, 2380.0002), (0.0, 0.0, -0.0), (0.5003, 0.5003, 2.9386), "DV_BP_Mines_Lift_Beam_B47_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_Mines_Lift_Beam_B48 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (2174.7698, 2128.3142, 2380.0002), (0.0, 0.0, -0.0), (0.5003, 0.5003, 2.9386), "DV_BP_Mines_Lift_Beam_B48_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_Mines_Lift_Beam_B49 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (2166.7292, 4262.3154, 930.0043), (0.0, 0.0, -0.0), (0.5003, 0.5003, 2.9386), "DV_BP_Mines_Lift_Beam_B49_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_Mines_Lift_Beam_B5_9 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (2265.4717, 2826.576, 829.36084), (0.0, 0.0, -0.0), (2.8281, 1.3984, 0.4114), "DV_BP_Mines_Lift_Beam_B5_9_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_Mines_Lift_Beam_B50 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (2127.8352, 4223.4224, 930.00305), (0.0, 0.0, -0.0), (0.5003, 0.5003, 2.9386), "DV_BP_Mines_Lift_Beam_B50_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_Mines_Lift_Beam_B51 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (2166.726, 4262.3125, 1220.005), (0.0, 0.0, -0.0), (0.5003, 0.5003, 2.9386), "DV_BP_Mines_Lift_Beam_B51_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_Mines_Lift_Beam_B52 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (2127.833, 4223.4185, 1220.0043), (0.0, 0.0, -0.0), (0.5003, 0.5003, 2.9386), "DV_BP_Mines_Lift_Beam_B52_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_Mines_Lift_Beam_B53 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (2166.7249, 4262.3066, 1510.005), (0.0, 0.0, -0.0), (0.5003, 0.5003, 2.9386), "DV_BP_Mines_Lift_Beam_B53_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_Mines_Lift_Beam_B54 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (2127.8308, 4223.415, 1510.0043), (0.0, 0.0, -0.0), (0.5003, 0.5003, 2.9386), "DV_BP_Mines_Lift_Beam_B54_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_Mines_Lift_Beam_B55 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (2166.7224, 4262.305, 1800.0051), (0.0, 0.0, -0.0), (0.5003, 0.5003, 2.9386), "DV_BP_Mines_Lift_Beam_B55_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_Mines_Lift_Beam_B56 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (2127.8284, 4223.4116, 1800.0043), (0.0, 0.0, -0.0), (0.5003, 0.5003, 2.9386), "DV_BP_Mines_Lift_Beam_B56_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_Mines_Lift_Beam_B57 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (2166.7188, 4262.3027, 2090.0051), (0.0, 0.0, -0.0), (0.5003, 0.5003, 2.9386), "DV_BP_Mines_Lift_Beam_B57_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_Mines_Lift_Beam_B58 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (2127.8257, 4223.4077, 2090.0042), (0.0, 0.0, -0.0), (0.5003, 0.5003, 2.9386), "DV_BP_Mines_Lift_Beam_B58_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_Mines_Lift_Beam_B59 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (2166.7163, 4262.299, 2380.0051), (0.0, 0.0, -0.0), (0.5003, 0.5003, 2.9386), "DV_BP_Mines_Lift_Beam_B59_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_Mines_Lift_Beam_B6 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (2869.392, 2266.1208, 1234.6392), (0.0, 0.0, -0.0), (2.8667, 1.2685, 0.4114), "DV_BP_Mines_Lift_Beam_B6_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_Mines_Lift_Beam_B60 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (2127.8235, 4223.406, 2380.0042), (0.0, 0.0, -0.0), (0.5003, 0.5003, 2.9386), "DV_BP_Mines_Lift_Beam_B60_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_Mines_Lift_Beam_B61 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (4213.289, 2139.894, 929.99866), (0.0, 0.0, -0.0), (0.5003, 0.5003, 2.9386), "DV_BP_Mines_Lift_Beam_B61_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_Mines_Lift_Beam_B62 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (4252.183, 2178.7866, 929.99817), (0.0, 0.0, -0.0), (0.5003, 0.5003, 2.9386), "DV_BP_Mines_Lift_Beam_B62_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_Mines_Lift_Beam_B63 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (4213.2905, 2139.895, 1219.9991), (0.0, 0.0, -0.0), (0.5003, 0.5003, 2.9386), "DV_BP_Mines_Lift_Beam_B63_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_Mines_Lift_Beam_B64 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (4252.184, 2178.788, 1219.9994), (0.0, 0.0, -0.0), (0.5003, 0.5003, 2.9386), "DV_BP_Mines_Lift_Beam_B64_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_Mines_Lift_Beam_B65 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (4213.2915, 2139.8945, 1509.9991), (0.0, 0.0, -0.0), (0.5003, 0.5003, 2.9386), "DV_BP_Mines_Lift_Beam_B65_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_Mines_Lift_Beam_B66 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (4252.1855, 2178.788, 1509.9994), (0.0, 0.0, -0.0), (0.5003, 0.5003, 2.9386), "DV_BP_Mines_Lift_Beam_B66_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_Mines_Lift_Beam_B67 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (4213.293, 2139.895, 1799.9991), (0.0, 0.0, -0.0), (0.5003, 0.5003, 2.9386), "DV_BP_Mines_Lift_Beam_B67_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_Mines_Lift_Beam_B68 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (4252.186, 2178.7886, 1799.9991), (0.0, 0.0, -0.0), (0.5003, 0.5003, 2.9386), "DV_BP_Mines_Lift_Beam_B68_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_Mines_Lift_Beam_B69 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (4213.2935, 2139.896, 2089.9995), (0.0, 0.0, -0.0), (0.5003, 0.5003, 2.9386), "DV_BP_Mines_Lift_Beam_B69_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_Mines_Lift_Beam_B7 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (2866.024, 2256.7058, 829.36084), (0.0, 0.0, -0.0), (1.2684, 2.8667, 0.4114), "DV_BP_Mines_Lift_Beam_B7_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_Mines_Lift_Beam_B70 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (4252.187, 2178.7896, 2089.9995), (0.0, 0.0, -0.0), (0.5003, 0.5003, 2.9386), "DV_BP_Mines_Lift_Beam_B70_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_Mines_Lift_Beam_B71 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (4213.296, 2139.897, 2379.9995), (0.0, 0.0, -0.0), (0.5003, 0.5003, 2.9386), "DV_BP_Mines_Lift_Beam_B71_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_Mines_Lift_Beam_B72 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (4252.1885, 2178.789, 2379.9995), (0.0, 0.0, -0.0), (0.5003, 0.5003, 2.9386), "DV_BP_Mines_Lift_Beam_B72_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_Mines_Lift_Beam_B73 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (1997.0231, 4360.6978, 930.0043), (0.0, 0.0, -0.0), (0.5003, 0.5003, 2.9386), "DV_BP_Mines_Lift_Beam_B73_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_Mines_Lift_Beam_B74 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (2035.9177, 4399.5913, 930.0041), (0.0, 0.0, -0.0), (0.5003, 0.5003, 2.9386), "DV_BP_Mines_Lift_Beam_B74_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_Mines_Lift_Beam_B75 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (1997.024, 4360.6963, 1220.0054), (0.0, 0.0, -0.0), (0.5003, 0.5003, 2.9386), "DV_BP_Mines_Lift_Beam_B75_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_Mines_Lift_Beam_B76 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (2035.9174, 4399.5903, 1220.0056), (0.0, 0.0, -0.0), (0.5003, 0.5003, 2.9386), "DV_BP_Mines_Lift_Beam_B76_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_Mines_Lift_Beam_B77 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (1997.024, 4360.697, 1510.0052), (0.0, 0.0, -0.0), (0.5003, 0.5003, 2.9386), "DV_BP_Mines_Lift_Beam_B77_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_Mines_Lift_Beam_B78 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (2035.9186, 4399.589, 1510.0055), (0.0, 0.0, -0.0), (0.5003, 0.5003, 2.9386), "DV_BP_Mines_Lift_Beam_B78_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_Mines_Lift_Beam_B79 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (1997.0248, 4360.694, 1800.0054), (0.0, 0.0, -0.0), (0.5003, 0.5003, 2.9386), "DV_BP_Mines_Lift_Beam_B79_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_Mines_Lift_Beam_B8 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (3622.8171, 2305.4688, 1234.6392), (0.0, 0.0, -0.0), (2.7830, 1.5244, 0.4114), "DV_BP_Mines_Lift_Beam_B8_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_Mines_Lift_Beam_B80 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (2035.919, 4399.5864, 1800.0054), (0.0, 0.0, -0.0), (0.5003, 0.5003, 2.9386), "DV_BP_Mines_Lift_Beam_B80_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_Mines_Lift_Beam_B81 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (1997.027, 4360.6904, 2090.0073), (0.0, 0.0, -0.0), (0.5003, 0.5003, 2.9386), "DV_BP_Mines_Lift_Beam_B81_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_Mines_Lift_Beam_B82 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (2035.9196, 4399.586, 2090.0059), (0.0, 0.0, -0.0), (0.5003, 0.5003, 2.9386), "DV_BP_Mines_Lift_Beam_B82_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_Mines_Lift_Beam_B83 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (1997.0267, 4360.691, 2380.007), (0.0, 0.0, -0.0), (0.5003, 0.5003, 2.9386), "DV_BP_Mines_Lift_Beam_B83_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_Mines_Lift_Beam_B84 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (2035.9198, 4399.583, 2380.0068), (0.0, 0.0, -0.0), (0.5003, 0.5003, 2.9386), "DV_BP_Mines_Lift_Beam_B84_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_Mines_Lift_Beam_B85_120 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (1997.0267, 4360.691, 2665.007), (0.0, 0.0, -0.0), (0.5003, 0.5003, 2.9386), "DV_BP_Mines_Lift_Beam_B85_120_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_Mines_Lift_Beam_B86_121 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (2035.9197, 4399.583, 2665.0068), (0.0, 0.0, -0.0), (0.5003, 0.5003, 2.9386), "DV_BP_Mines_Lift_Beam_B86_121_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_Mines_Lift_Beam_B87_160 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (4387.548, 2039.8613, 930.00385), (0.0, 0.0, -0.0), (0.5003, 0.5003, 2.9386), "DV_BP_Mines_Lift_Beam_B87_160_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_Mines_Lift_Beam_B88_161 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (4348.6523, 2000.9678, 930.0036), (0.0, 0.0, -0.0), (0.5003, 0.5003, 2.9386), "DV_BP_Mines_Lift_Beam_B88_161_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_Mines_Lift_Beam_B89_162 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (4387.5454, 2039.8628, 1220.0049), (0.0, 0.0, -0.0), (0.5003, 0.5003, 2.9386), "DV_BP_Mines_Lift_Beam_B89_162_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_Mines_Lift_Beam_B9 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (3627.0925, 2296.429, 829.36084), (0.0, 0.0, -0.0), (1.5244, 2.7830, 0.4114), "DV_BP_Mines_Lift_Beam_B9_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_Mines_Lift_Beam_B90_163 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (4348.652, 2000.969, 1220.0051), (0.0, 0.0, -0.0), (0.5003, 0.5003, 2.9386), "DV_BP_Mines_Lift_Beam_B90_163_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_Mines_Lift_Beam_B91_164 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (4387.5454, 2039.8623, 1510.0048), (0.0, 0.0, -0.0), (0.5003, 0.5003, 2.9386), "DV_BP_Mines_Lift_Beam_B91_164_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_Mines_Lift_Beam_B92_165 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (4348.6504, 2000.9702, 1510.005), (0.0, 0.0, -0.0), (0.5003, 0.5003, 2.9386), "DV_BP_Mines_Lift_Beam_B92_165_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_Mines_Lift_Beam_B93_166 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (4387.545, 2039.8655, 1800.0049), (0.0, 0.0, -0.0), (0.5003, 0.5003, 2.9386), "DV_BP_Mines_Lift_Beam_B93_166_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_Mines_Lift_Beam_B94_167 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (4348.6514, 2000.9727, 1800.0049), (0.0, 0.0, -0.0), (0.5003, 0.5003, 2.9386), "DV_BP_Mines_Lift_Beam_B94_167_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_Mines_Lift_Beam_B95_168 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (4387.542, 2039.8696, 2090.0068), (0.0, 0.0, -0.0), (0.5003, 0.5003, 2.9386), "DV_BP_Mines_Lift_Beam_B95_168_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_Mines_Lift_Beam_B96_169 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (4348.651, 2000.9734, 2090.0054), (0.0, 0.0, -0.0), (0.5003, 0.5003, 2.9386), "DV_BP_Mines_Lift_Beam_B96_169_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_Mines_Lift_Beam_B97 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (4387.543, 2039.8684, 2380.007), (0.0, 0.0, -0.0), (0.5003, 0.5003, 2.9386), "DV_BP_Mines_Lift_Beam_B97_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_Mines_Lift_Beam_B98 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (4348.65, 2000.9763, 2380.0068), (0.0, 0.0, -0.0), (0.5003, 0.5003, 2.9386), "DV_BP_Mines_Lift_Beam_B98_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_Mines_Lift_Beam_B99 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (4387.543, 2039.8687, 2665.007), (0.0, 0.0, -0.0), (0.5003, 0.5003, 2.9386), "DV_BP_Mines_Lift_Beam_B99_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_Mines_Lift_Beam_D_2 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (2395.7126, 3784.192, 1112.6497), (0.0, 0.0, -0.0), (2.0628, 2.0628, 2.6901), "DV_BP_Mines_Lift_Beam_D_2_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_Mines_Lift_Beam_D10 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (2590.1956, 2419.9055, 1112.6495), (0.0, 0.0, -0.0), (2.0628, 2.0628, 2.6901), "DV_BP_Mines_Lift_Beam_D10_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_Mines_Lift_Beam_D11 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (2422.017, 2583.0845, 1112.6495), (0.0, 0.0, -0.0), (2.0628, 2.0628, 2.6901), "DV_BP_Mines_Lift_Beam_D11_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_Mines_Lift_Beam_D12 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (2390.1958, 2614.9065, 1112.6495), (0.0, 0.0, -0.0), (2.0628, 2.0628, 2.6901), "DV_BP_Mines_Lift_Beam_D12_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_Mines_Lift_Beam_D13 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (3777.267, 4001.6147, 1112.6494), (0.0, 0.0, -0.0), (2.0628, 2.0628, 2.6901), "DV_BP_Mines_Lift_Beam_D13_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_Mines_Lift_Beam_D14 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (3809.0896, 3969.7947, 1112.6494), (0.0, 0.0, -0.0), (2.0628, 2.0628, 2.6901), "DV_BP_Mines_Lift_Beam_D14_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_Mines_Lift_Beam_D15 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (3977.268, 3806.6162, 1112.6494), (0.0, 0.0, -0.0), (2.0628, 2.0628, 2.6901), "DV_BP_Mines_Lift_Beam_D15_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_Mines_Lift_Beam_D16 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (4009.0864, 3774.7952, 1112.6494), (0.0, 0.0, -0.0), (2.0628, 2.0628, 2.6901), "DV_BP_Mines_Lift_Beam_D16_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_Mines_Lift_Beam_D2 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (2427.5334, 3816.0127, 1112.6497), (0.0, 0.0, -0.0), (2.0628, 2.0628, 2.6901), "DV_BP_Mines_Lift_Beam_D2_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_Mines_Lift_Beam_D3 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (2590.7126, 3984.192, 1112.6497), (0.0, 0.0, -0.0), (2.0628, 2.0628, 2.6901), "DV_BP_Mines_Lift_Beam_D3_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_Mines_Lift_Beam_D4 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (2622.5334, 4016.0151, 1112.6497), (0.0, 0.0, -0.0), (2.0628, 2.0628, 2.6901), "DV_BP_Mines_Lift_Beam_D4_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_Mines_Lift_Beam_D5_26 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (4004.181, 2626.9749, 1112.6495), (0.0, 0.0, -0.0), (2.0628, 2.0628, 2.6901), "DV_BP_Mines_Lift_Beam_D5_26_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_Mines_Lift_Beam_D6_27 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (3972.361, 2595.1538, 1112.6495), (0.0, 0.0, -0.0), (2.0628, 2.0628, 2.6901), "DV_BP_Mines_Lift_Beam_D6_27_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_Mines_Lift_Beam_D7_28 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (3809.1833, 2426.9746, 1112.6495), (0.0, 0.0, -0.0), (2.0628, 2.0628, 2.6901), "DV_BP_Mines_Lift_Beam_D7_28_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_Mines_Lift_Beam_D8_29 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (3777.3623, 2395.1538, 1112.6495), (0.0, 0.0, -0.0), (2.0628, 2.0628, 2.6901), "DV_BP_Mines_Lift_Beam_D8_29_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_Mines_Lift_Beam_D9 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (2622.0173, 2388.0854, 1112.6495), (0.0, 0.0, -0.0), (2.0628, 2.0628, 2.6901), "DV_BP_Mines_Lift_Beam_D9_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_Mines_Machine_Whim_Side_Bracket_2 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (2214.5762, 3615.1636, 1143.5305), (0.0, 0.0, -0.0), (2.2553, 1.4144, 2.2422), "DV_BP_Mines_Machine_Whim_Side_Bracket_2_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_Mines_Machine_Whim_Side_Bracket10 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (4044.291, 2820.9917, 1143.5305), (0.0, 0.0, -0.0), (2.2651, 1.3256, 2.2422), "DV_BP_Mines_Machine_Whim_Side_Bracket10_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_Mines_Machine_Whim_Side_Bracket11 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (4192.0537, 3599.404, 1143.5305), (0.0, 0.0, -0.0), (2.2553, 1.4144, 2.2422), "DV_BP_Mines_Machine_Whim_Side_Bracket11_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_Mines_Machine_Whim_Side_Bracket12 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (4056.5752, 3541.0647, 1143.5305), (0.0, 0.0, -0.0), (2.2553, 1.4144, 2.2422), "DV_BP_Mines_Machine_Whim_Side_Bracket12_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_Mines_Machine_Whim_Side_Bracket13_24 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (3618.9976, 4183.1016, 1143.5305), (0.0, 0.0, -0.0), (1.4144, 2.2553, 2.2422), "DV_BP_Mines_Machine_Whim_Side_Bracket13_24_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_Mines_Machine_Whim_Side_Bracket14_25 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (3564.4524, 4046.0513, 1143.5305), (0.0, 0.0, -0.0), (1.4144, 2.2553, 2.2422), "DV_BP_Mines_Machine_Whim_Side_Bracket14_25_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_Mines_Machine_Whim_Side_Bracket15_28 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (2801.8203, 4190.676, 1143.5305), (0.0, 0.0, -0.0), (1.4144, 2.2553, 2.2422), "DV_BP_Mines_Machine_Whim_Side_Bracket15_28_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_Mines_Machine_Whim_Side_Bracket16_29 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (2860.1597, 4055.1973, 1143.5305), (0.0, 0.0, -0.0), (1.4144, 2.2553, 2.2422), "DV_BP_Mines_Machine_Whim_Side_Bracket16_29_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_Mines_Machine_Whim_Side_Bracket2 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (2351.6287, 3560.6187, 1143.5305), (0.0, 0.0, -0.0), (2.2553, 1.4144, 2.2422), "DV_BP_Mines_Machine_Whim_Side_Bracket2_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_Mines_Machine_Whim_Side_Bracket3_8 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (2206.001, 2798.985, 1143.5305), (0.0, 0.0, -0.0), (2.2553, 1.4144, 2.2422), "DV_BP_Mines_Machine_Whim_Side_Bracket3_8_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_Mines_Machine_Whim_Side_Bracket4_9 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (2341.4812, 2857.3264, 1143.5305), (0.0, 0.0, -0.0), (2.2553, 1.4144, 2.2422), "DV_BP_Mines_Machine_Whim_Side_Bracket4_9_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_Mines_Machine_Whim_Side_Bracket5 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (2846.5288, 2194.112, 1143.5305), (0.0, 0.0, -0.0), (1.3256, 2.2651, 2.2422), "DV_BP_Mines_Machine_Whim_Side_Bracket5_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_Mines_Machine_Whim_Side_Bracket6 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (2894.2834, 2333.6753, 1143.5305), (0.0, 0.0, -0.0), (1.3256, 2.2651, 2.2422), "DV_BP_Mines_Machine_Whim_Side_Bracket6_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_Mines_Machine_Whim_Side_Bracket7 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (3657.568, 2238.384, 1143.5305), (0.0, 0.0, -0.0), (1.4998, 2.2400, 2.2422), "DV_BP_Mines_Machine_Whim_Side_Bracket7_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_Mines_Machine_Whim_Side_Bracket8 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (3592.6506, 2370.838, 1143.5305), (0.0, 0.0, -0.0), (1.4998, 2.2400, 2.2422), "DV_BP_Mines_Machine_Whim_Side_Bracket8_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_Mines_Machine_Whim_Side_Bracket9 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (4183.8535, 2773.236, 1143.5305), (0.0, 0.0, -0.0), (2.2651, 1.3256, 2.2422), "DV_BP_Mines_Machine_Whim_Side_Bracket9_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_Mines_Machine_Whim_Side_Support_2 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (2285.2515, 3586.9229, 1047.4114), (0.0, 0.0, -0.0), (3.0481, 1.7795, 4.1538), "DV_BP_Mines_Machine_Whim_Side_Support_2_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_Mines_Machine_Whim_Side_Support10 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (3624.1672, 2306.7717, 1047.4114), (0.0, 0.0, -0.0), (1.9015, 3.0184, 4.1538), "DV_BP_Mines_Machine_Whim_Side_Support10_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_Mines_Machine_Whim_Side_Support11 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (4111.879, 2797.9758, 1047.4114), (0.0, 0.0, -0.0), (3.0706, 1.6531, 4.1538), "DV_BP_Mines_Machine_Whim_Side_Support11_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_Mines_Machine_Whim_Side_Support12 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (4122.1104, 3569.3997, 1047.4114), (0.0, 0.0, -0.0), (3.0482, 1.7794, 4.1538), "DV_BP_Mines_Machine_Whim_Side_Support12_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_Mines_Machine_Whim_Side_Support13_11 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (3590.7568, 4112.427, 1047.4114), (0.0, 0.0, -0.0), (1.7795, 3.0481, 4.1538), "DV_BP_Mines_Machine_Whim_Side_Support13_11_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_Mines_Machine_Whim_Side_Support14_13 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (2831.8252, 4120.732, 1047.4114), (0.0, 0.0, -0.0), (1.7795, 3.0482, 4.1538), "DV_BP_Mines_Machine_Whim_Side_Support14_13_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_Mines_Machine_Whim_Side_Support2_2 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (2275.9458, 2828.9902, 1047.4114), (0.0, 0.0, -0.0), (3.0481, 1.7795, 4.1538), "DV_BP_Mines_Machine_Whim_Side_Support2_2_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_Mines_Machine_Whim_Side_Support9_4 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (2871.268, 2266.0876, 1047.4114), (0.0, 0.0, -0.0), (1.6531, 3.0706, 4.1538), "DV_BP_Mines_Machine_Whim_Side_Support9_4_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_Mines_Machine_Whim_Wheel_Middle_Bracket_2 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (1994.0853, 4218.0796, 1193.6832), (0.0, 0.0, -0.0), (0.9551, 0.9551, 3.8737), "DV_BP_Mines_Machine_Whim_Wheel_Middle_Bracket_2_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_Mines_Machine_Whim_Wheel_Middle_Bracket2_2 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (2192.0747, 4416.0728, 1193.6832), (0.0, 0.0, -0.0), (0.9551, 0.9551, 3.8737), "DV_BP_Mines_Machine_Whim_Wheel_Middle_Bracket2_2_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_Mines_Machine_Whim_Wheel_Middle_Bracket3_11 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (4408.6, 2190.346, 1193.6832), (0.0, 0.0, -0.0), (0.9551, 0.9551, 3.8737), "DV_BP_Mines_Machine_Whim_Wheel_Middle_Bracket3_11_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_Mines_Machine_Whim_Wheel_Middle_Bracket4_12 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (4210.6104, 1992.3524, 1193.6832), (0.0, 0.0, -0.0), (0.9551, 0.9551, 3.8737), "DV_BP_Mines_Machine_Whim_Wheel_Middle_Bracket4_12_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_Mines_Machine_Whim_Wheel_Middle_Bracket5 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (2189.072, 1987.3551, 1193.6832), (0.0, 0.0, -0.0), (0.9551, 0.9551, 3.8737), "DV_BP_Mines_Machine_Whim_Wheel_Middle_Bracket5_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_Mines_Machine_Whim_Wheel_Middle_Bracket6 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (1991.0791, 2185.3447, 1193.6832), (0.0, 0.0, -0.0), (0.9551, 0.9551, 3.8737), "DV_BP_Mines_Machine_Whim_Wheel_Middle_Bracket6_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_Mines_Machine_Whim_Wheel_Middle_Bracket7 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (4213.274, 4405.404, 1193.6832), (0.0, 0.0, -0.0), (0.9551, 0.9551, 3.8737), "DV_BP_Mines_Machine_Whim_Wheel_Middle_Bracket7_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_Mines_Machine_Whim_Wheel_Middle_Bracket8 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (4411.2676, 4207.4146, 1193.6832), (0.0, 0.0, -0.0), (0.9551, 0.9551, 3.8737), "DV_BP_Mines_Machine_Whim_Wheel_Middle_Bracket8_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_Mines_Scaffoldfing_Support_Bracket_2 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (2218.9746, 4446.337, 908.59406), (0.0, 0.0, -0.0), (2.1152, 2.1095, 2.2134), "DV_BP_Mines_Scaffoldfing_Support_Bracket_2_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_Mines_Scaffoldfing_Support_Bracket2 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (1962.811, 4187.6514, 908.59406), (0.0, 0.0, -0.0), (2.1152, 2.1095, 2.2134), "DV_BP_Mines_Scaffoldfing_Support_Bracket2_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_Mines_Scaffoldfing_Support_Bracket3_9 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (4183.7104, 1962.0884, 908.59406), (0.0, 0.0, -0.0), (2.1152, 2.1095, 2.2134), "DV_BP_Mines_Scaffoldfing_Support_Bracket3_9_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_Mines_Scaffoldfing_Support_Bracket5 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (1960.815, 2212.2456, 908.59406), (0.0, 0.0, -0.0), (2.1095, 2.1152, 2.2134), "DV_BP_Mines_Scaffoldfing_Support_Bracket5_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_Mines_Scaffoldfing_Support_Bracket6 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (2219.5002, 1956.0806, 908.59406), (0.0, 0.0, -0.0), (2.1095, 2.1152, 2.2134), "DV_BP_Mines_Scaffoldfing_Support_Bracket6_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_Mines_Scaffoldfing_Support_Bracket7 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (4441.532, 4180.5137, 908.59406), (0.0, 0.0, -0.0), (2.1095, 2.1152, 2.2134), "DV_BP_Mines_Scaffoldfing_Support_Bracket7_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_Mines_Scaffoldfing_Support_Bracket8 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (4182.846, 4436.678, 908.59406), (0.0, 0.0, -0.0), (2.1095, 2.1152, 2.2134), "DV_BP_Mines_Scaffoldfing_Support_Bracket8_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_Mines_Scaffoldfing_Support_Bracket9 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (4443.411, 2217.2358, 908.59406), (0.0, 0.0, -0.0), (2.1152, 2.1095, 2.2134), "DV_BP_Mines_Scaffoldfing_Support_Bracket9_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_Suburb_Stairs_Trim_Pillar_C_Breakable3_2 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (5976.071, 3758.8157, 1459.316), (0.0, 0.0, -0.0), (0.9416, 0.9510, 2.1902), "DV_BP_Suburb_Stairs_Trim_Pillar_C_Breakable3_2_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_Suburb_Stairs_Trim_Pillar_C_Breakable4 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (6075.9097, 3753.8203, 1509.316), (0.0, 0.0, -0.0), (0.9510, 0.9416, 2.1902), "DV_BP_Suburb_Stairs_Trim_Pillar_C_Breakable4_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_Suburb_Stairs_Trim_Pillar_C_Breakable5 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (6021.848, 2655.206, 1509.316), (0.0, 0.0, -0.0), (0.9416, 0.9510, 2.1902), "DV_BP_Suburb_Stairs_Trim_Pillar_C_Breakable5_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_Suburb_Stairs_Trim_Pillar_C_Breakable6 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (5922.01, 2660.204, 1459.316), (0.0, 0.0, -0.0), (0.9510, 0.9416, 2.1902), "DV_BP_Suburb_Stairs_Trim_Pillar_C_Breakable6_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_Suburbs_Ladder_C_2 (EMorSimpleShape::Empty)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (2690.0, 2146.9614, 1030.0), (-0.0, -30.000063894566395, -0.0), (2.0000, 2.0000, 2.0000), "DV_BP_Suburbs_Ladder_C_2", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: DecoBlockingVolume1 (EMorSimpleShape::Empty)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (1478.2197, 5093.2993, 1100.0), (-0.0, -50.62493662814806, -0.0), (2.0000, 2.0000, 2.0000), "DV_DecoBlockingVolume1", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: DecoBlockingVolume9 (EMorSimpleShape::Empty)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (3256.0337, 3229.4941, 989.14795), (0.0, 87.79310973297383, -0.0), (2.0000, 2.0000, 2.0000), "DV_DecoBlockingVolume9", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: DecorationBlockingVolume_2 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (3178.6643, 422.2306, 940.6006), (0.0, 0.0, -0.0), (2.0000, 2.0000, 2.0000), "DV_DecorationBlockingVolume_2", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: Orc_Palissade_Barricade_A_2 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (3674.8623, 2526.1577, 915.6648), (0.0, 0.0, -0.0), (3.9479, 3.4757, 2.1414), "DV_Orc_Palissade_Barricade_A_2_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: Orc_Palissade_Barricade_A10 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (3823.7441, 2369.4888, 829.6648), (0.0, 0.0, -0.0), (4.0410, 3.2081, 2.1414), "DV_Orc_Palissade_Barricade_A10_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: Orc_Palissade_Barricade_A11_12 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (2652.089, 2332.9597, 845.6648), (0.0, 0.0, -0.0), (3.9748, 3.4160, 2.1414), "DV_Orc_Palissade_Barricade_A11_12_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: Orc_Palissade_Barricade_A12 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (2398.6526, 2559.602, 845.6648), (0.0, 0.0, -0.0), (3.5979, 3.8784, 2.1414), "DV_Orc_Palissade_Barricade_A12_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: Orc_Palissade_Barricade_A13_16 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (2355.494, 3769.7603, 840.6648), (0.0, 0.0, -0.0), (3.7524, 3.7524, 2.1414), "DV_Orc_Palissade_Barricade_A13_16_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: Orc_Palissade_Barricade_A14 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (2619.7144, 4043.14, 848.6648), (0.0, 0.0, -0.0), (3.9748, 3.4160, 2.1414), "DV_Orc_Palissade_Barricade_A14_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: Orc_Palissade_Barricade_A15_20 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (3766.8926, 4041.5981, 838.6648), (0.0, 0.0, -0.0), (3.8784, 3.5979, 2.1414), "DV_Orc_Palissade_Barricade_A15_20_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: Orc_Palissade_Barricade_A16 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (4006.04, 3804.0862, 838.6648), (0.0, 0.0, -0.0), (3.5979, 3.8784, 2.1414), "DV_Orc_Palissade_Barricade_A16_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: Orc_Palissade_Barricade_A2 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (3908.2227, 2764.1814, 915.6648), (0.0, 0.0, -0.0), (3.1238, 4.0579, 2.1414), "DV_Orc_Palissade_Barricade_A2_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: Orc_Palissade_Barricade_A3_6 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (3900.246, 3634.635, 915.6648), (0.0, 0.0, -0.0), (3.3664, 3.9942, 2.1414), "DV_Orc_Palissade_Barricade_A3_6_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: Orc_Palissade_Barricade_A4 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (3670.2815, 3876.6953, 915.6648), (0.0, 0.0, -0.0), (3.9479, 3.4757, 2.1414), "DV_Orc_Palissade_Barricade_A4_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: Orc_Palissade_Barricade_A5 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (2763.0417, 3893.6277, 915.6648), (0.0, 0.0, -0.0), (3.9942, 3.3664, 2.1414), "DV_Orc_Palissade_Barricade_A5_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: Orc_Palissade_Barricade_A6 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (2520.9812, 3663.6628, 915.6648), (0.0, 0.0, -0.0), (3.4757, 3.9479, 2.1414), "DV_Orc_Palissade_Barricade_A6_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: Orc_Palissade_Barricade_A7 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (2522.057, 2748.991, 915.6648), (0.0, 0.0, -0.0), (3.3664, 3.9942, 2.1414), "DV_Orc_Palissade_Barricade_A7_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: Orc_Palissade_Barricade_A8 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (2756.1792, 2509.7078, 915.6648), (0.0, 0.0, -0.0), (3.9479, 3.4757, 2.1414), "DV_Orc_Palissade_Barricade_A8_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: Orc_Palissade_Barricade_A9_8 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (4029.1543, 2625.422, 829.6648), (0.0, 0.0, -0.0), (3.4160, 3.9748, 2.1414), "DV_Orc_Palissade_Barricade_A9_8_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: RockBlockingVolume1 (EMorSimpleShape::Empty)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (1409.9362, 5176.5024, 1100.0), (-0.0, -50.62493662814806, -0.0), (2.0000, 2.0000, 2.0000), "DV_RockBlockingVolume1", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: RockBlockingVolume10 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (4296.112, 5746.4697, 1157.5005), (-0.0, -22.499999128211993, -0.0), (2.0000, 2.0000, 2.0000), "DV_RockBlockingVolume10", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: RockBlockingVolume11 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (1284.0854, 5069.582, 1154.034), (0.0, 39.37500072009061, -0.0), (2.0000, 2.0000, 2.0000), "DV_RockBlockingVolume11", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: RockBlockingVolume12_1 (EMorSimpleShape::Empty)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (2372.9312, 5561.401, 1100.0), (-0.0, -73.12497115963035, -0.0), (2.0000, 2.0000, 2.0000), "DV_RockBlockingVolume12_1", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: RockBlockingVolume13 (EMorSimpleShape::Empty)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (3195.7766, 5783.1543, 1100.0), (-0.0, -89.99993822608693, -0.0), (2.0000, 2.0000, 2.0000), "DV_RockBlockingVolume13", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: RockBlockingVolume2 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (3210.2476, 5947.2363, 953.0857), (0.0, 88.68494728519529, -0.0), (2.0000, 2.0000, 2.0000), "DV_RockBlockingVolume2", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: RockBlockingVolume3 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (3221.7715, 5836.1904, 1313.0989), (0.0, 0.0, -0.0), (2.0000, 2.0000, 2.0000), "DV_RockBlockingVolume3", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: RockBlockingVolume4 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (2661.7224, 736.4566, 1163.0989), (0.0, 76.54018334573989, -0.0), (2.0000, 2.0000, 2.0000), "DV_RockBlockingVolume4", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: RockBlockingVolume5 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (5827.959, 3184.9944, 1142.7261), (0.0, 88.37700065524085, -0.0), (2.0000, 2.0000, 2.0000), "DV_RockBlockingVolume5", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: RockBlockingVolume6 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (5681.731, 2215.223, 1081.708), (-0.0, -22.146391668799428, -0.0), (2.0000, 2.0000, 2.0000), "DV_RockBlockingVolume6", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: RockBlockingVolume7 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (5712.8335, 4216.9385, 1140.8362), (-0.0, -62.81250794889214, -0.0), (2.0000, 2.0000, 2.0000), "DV_RockBlockingVolume7", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: RockBlockingVolume8 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (1275.4012, 1224.7383, 1116.9088), (-0.0, -50.6250334005913, -0.0), (2.0000, 2.0000, 2.0000), "DV_RockBlockingVolume8", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: RockBlockingVolume9 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (4145.326, 682.26935, 1109.9457), (-0.0, -159.4986856702403, -0.0), (2.0000, 2.0000, 2.0000), "DV_RockBlockingVolume9", _folder)
if a: placed += 1
else: skipped += 1

# ======================================================================
# SUMMARY
# ======================================================================
unreal.log(f"[{BUBBLE_NAME}] Reconstruction complete: {placed} placed, {skipped} skipped, {errors} errors")
