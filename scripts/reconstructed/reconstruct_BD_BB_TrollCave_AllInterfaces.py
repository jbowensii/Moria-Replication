"""Auto-generated level reconstruction script.
Bubble: BD_BB_TrollCave_AllInterfaces
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

BUBBLE_NAME = "BD_BB_TrollCave_AllInterfaces"
placed = 0
skipped = 0
errors = 0

# ======================================================================
# PHASE 1: InstancedMeshCatalog  (static mesh placement)
# ======================================================================
unreal.log(f"[{BUBBLE_NAME}] Phase 1: Placing static meshes...")

# Batch 0: StaticMesh'Cavern_Stalactites_A' (4 instances)
_mesh_path = "/Game/Art/Assets/Kits/Deco/Caveren/Cavern_Stalactites_A"
_materials = ['/Game/Art/Assets/Kits/Deco/Caveren/Materials/Cavern_Stalactites/Cavern_Stalactites_Mat_C']
_folder = "Reconstruction/BD_BB_TrollCave_AllInterfaces/Meshes"
a = spawn_static_mesh(_mesh_path, _materials, (2765.0, 3680.0, 1820.0), (0.0, 0.0, -0.0), (1.0, 1.0, 1.0), "Cavern_Stalactites_A_13", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2445.0, 2450.0, 1705.0), (0.0, 0.0, -0.0), (1.0, 1.0, 1.0), "Cavern_Stalactites_A2_28", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2030.0, 4745.0, 1440.0), (0.0, 0.0, -0.0), (1.0, 1.0, 1.0), "Cavern_Stalactites_A3_38", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5645.0, 3180.0, 2390.0), (0.0, 0.0, -0.0), (1.0, 1.0, 1.0), "Cavern_Stalactites_A4_125", _folder)
if a: placed += 1
else: skipped += 1

# Batch 1: StaticMesh'Cavern_Stalactites_B' (4 instances)
_mesh_path = "/Game/Art/Assets/Kits/Deco/Caveren/Cavern_Stalactites_B"
_materials = ['/Game/Art/Assets/Kits/Deco/Caveren/Materials/Cavern_Stalactites/Cavern_Stalactites_Mat_C']
_folder = "Reconstruction/BD_BB_TrollCave_AllInterfaces/Meshes"
a = spawn_static_mesh(_mesh_path, _materials, (2255.0, 4720.0, 1370.0), (0.0, 0.0, -0.0), (1.0, 1.0, 1.0), "Cavern_Stalactites_B_41", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4720.0, 1805.0, 1650.0), (0.0, 0.0, -0.0), (1.0, 1.0, 1.0), "Cavern_Stalactites_B2_94", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1190.0, 2595.0, 1580.0), (0.0, 0.0, -0.0), (1.0, 1.0, 1.0), "Cavern_Stalactites_B3_119", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5805.0, 3225.0, 2380.0), (0.0, 0.0, -0.0), (1.0, 1.0, 1.0), "Cavern_Stalactites_B4_128", _folder)
if a: placed += 1
else: skipped += 1

# Batch 2: StaticMesh'Cavern_Stalactites_C' (4 instances)
_mesh_path = "/Game/Art/Assets/Kits/Deco/Caveren/Cavern_Stalactites_C"
_materials = ['/Game/Art/Assets/Kits/Deco/Caveren/Materials/Cavern_Stalactites/Cavern_Stalactites_Mat_C']
_folder = "Reconstruction/BD_BB_TrollCave_AllInterfaces/Meshes"
a = spawn_static_mesh(_mesh_path, _materials, (2430.0, 4485.0, 1615.0), (0.0, 0.0, -0.0), (1.0, 1.0, 1.0), "Cavern_Stalactites_C_53", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5520.0, 1765.0, 2040.0), (0.0, 0.0, -0.0), (1.0, 1.0, 1.0), "Cavern_Stalactites_C2_82", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4845.0, 1685.0, 1675.0), (0.0, 0.0, -0.0), (1.0, 1.0, 1.0), "Cavern_Stalactites_C3_97", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4515.0, 2340.0, 1950.0), (0.0, 0.0, -0.0), (1.0, 1.0, 1.0), "Cavern_Stalactites_C4_146", _folder)
if a: placed += 1
else: skipped += 1

# Batch 3: StaticMesh'Cavern_Stalactites_D' (3 instances)
_mesh_path = "/Game/Art/Assets/Kits/Deco/Caveren/Cavern_Stalactites_D"
_materials = ['/Game/Art/Assets/Kits/Deco/Caveren/Materials/Cavern_Stalactites/Cavern_Stalactites_Mat_D']
_folder = "Reconstruction/BD_BB_TrollCave_AllInterfaces/Meshes"
a = spawn_static_mesh(_mesh_path, _materials, (2565.0, 2570.0, 1800.0), (0.0, 0.0, -0.0), (1.0, 1.0, 1.0), "Cavern_Stalactites_D_31", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5260.0, 2735.0, 2400.0), (0.0, 0.0, -0.0), (2.0, 2.0, 2.0), "Cavern_Stalactites_D2_73", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5740.0, 3310.0, 2385.0), (0.0, 0.0, -0.0), (1.0, 1.0, 1.0), "Cavern_Stalactites_D3_131", _folder)
if a: placed += 1
else: skipped += 1

# Batch 4: StaticMesh'Cavern_Stalactites_E' (4 instances)
_mesh_path = "/Game/Art/Assets/Kits/Deco/Caveren/Cavern_Stalactites_E"
_materials = ['/Game/Art/Assets/Kits/Deco/Caveren/Materials/Cavern_Stalactites/Cavern_Stalactites_Mat_D']
_folder = "Reconstruction/BD_BB_TrollCave_AllInterfaces/Meshes"
a = spawn_static_mesh(_mesh_path, _materials, (5400.0, 4120.0, 2410.0), (0.0, 0.0, -0.0), (2.0, 2.0, 2.0), "Cavern_Stalactites_E_67", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5445.0, 2585.0, 2415.0), (0.0, 0.0, -0.0), (2.0, 2.0, 2.0), "Cavern_Stalactites_E2_76", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5070.0, 1695.0, 1865.0), (0.0, 0.0, -0.0), (1.0, 1.0, 1.0), "Cavern_Stalactites_E3_85", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2490.0, 2155.0, 1340.0), (0.0, 0.0, -0.0), (1.0, 1.0, 1.0), "Cavern_Stalactites_E4_103", _folder)
if a: placed += 1
else: skipped += 1

# Batch 5: StaticMesh'Cavern_Stalactites_F' (6 instances)
_mesh_path = "/Game/Art/Assets/Kits/Deco/Caveren/Cavern_Stalactites_F"
_materials = ['/Game/Art/Assets/Kits/Deco/Caveren/Materials/Cavern_Stalactites/Cavern_Stalactites_Mat_D']
_folder = "Reconstruction/BD_BB_TrollCave_AllInterfaces/Meshes"
a = spawn_static_mesh(_mesh_path, _materials, (2675.0, 2490.0, 1795.0), (0.0, 0.0, -0.0), (1.0, 1.0, 1.0), "Cavern_Stalactites_F_19", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4445.0, 4905.0, 1990.0), (0.0, 165.00004804796816, -0.0), (1.0, 1.0, 1.0), "Cavern_Stalactites_F2_50", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3935.5457, 1856.6095, 1440.0), (0.0, -170.00004533427662, 0.0), (1.0, 1.0, 1.0), "Cavern_Stalactites_F3_100", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2640.0, 2120.0, 1450.0), (0.0, 0.0, -0.0), (1.0, 1.0, 1.0), "Cavern_Stalactites_F4_106", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1330.0, 3560.0, 1760.0), (0.0, 0.0, -0.0), (1.0, 1.0, 1.0), "Cavern_Stalactites_F5_116", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5895.0, 3000.0, 2395.0), (0.0, 0.0, -0.0), (1.0, 1.0, 1.0), "Cavern_Stalactites_F6_134", _folder)
if a: placed += 1
else: skipped += 1

# Batch 6: StaticMesh'Cavern_Stalactites_G' (7 instances)
_mesh_path = "/Game/Art/Assets/Kits/Deco/Caveren/Cavern_Stalactites_G"
_materials = ['/Game/Art/Assets/Kits/Deco/Caveren/Materials/Cavern_Stalactites/Cavern_Stalactites_Mat_B']
_folder = "Reconstruction/BD_BB_TrollCave_AllInterfaces/Meshes"
a = spawn_static_mesh(_mesh_path, _materials, (2470.0, 4275.0, 1810.0), (0.0, 0.0, -0.0), (1.0, 1.0, 1.0), "Cavern_Stalactites_G_10", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2730.0, 3785.0, 1905.0), (0.0, 60.000067159027765, -0.0), (1.0, 1.0, 1.0), "Cavern_Stalactites_G2_16", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1970.0, 4435.0, 1850.0), (0.0, 0.0, -0.0), (1.0, 1.0, 1.0), "Cavern_Stalactites_G3_35", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5185.0, 3400.0, 2415.0), (0.0, 0.0, -0.0), (1.0, 1.0, 1.0), "Cavern_Stalactites_G4_58", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5805.0, 1740.0, 2025.0), (0.0, 0.0, -0.0), (1.0, 1.0, 1.0), "Cavern_Stalactites_G5_79", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5540.0, 3130.0, 2410.0), (0.0, 0.0, -0.0), (1.0, 1.0, 1.0), "Cavern_Stalactites_G6_137", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5320.0, 1995.0, 2290.0), (0.0, 0.0, -0.0), (1.0, 1.0, 1.0), "Cavern_Stalactites_G7_143", _folder)
if a: placed += 1
else: skipped += 1

# Batch 7: StaticMesh'Cavern_Stalactites_H' (14 instances)
_mesh_path = "/Game/Art/Assets/Kits/Deco/Caveren/Cavern_Stalactites_H"
_materials = ['/Game/Art/Assets/Kits/Deco/Caveren/Materials/Cavern_Stalactites/Cavern_Stalactites_Mat_A']
_folder = "Reconstruction/BD_BB_TrollCave_AllInterfaces/Meshes"
a = spawn_static_mesh(_mesh_path, _materials, (2560.0, 3885.0, 1915.0), (0.0, -120.000082340695, 0.0), (1.0, 1.0, 1.0), "Cavern_Stalactites_H_5", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5535.0, 1555.0, 1990.0), (0.0, 0.0, -0.0), (1.0, 1.0, 1.0), "Cavern_Stalactites_H10_88", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4457.465, 2012.8947, 1725.0), (0.0, -54.99999707414993, 0.0), (1.0, 1.0, 1.0), "Cavern_Stalactites_H11_91", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1570.0, 3060.0, 1920.0), (0.0, 50.00006722821837, -0.0), (1.0, 1.0, 1.0), "Cavern_Stalactites_H12_112", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1453.1498, 3147.9138, 1920.0), (0.0, -54.999966222610674, 0.0), (1.1677272, 1.1677272, 1.1677272), "Cavern_Stalactites_H13", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4154.7495, 2200.2515, 1895.0), (0.0, 45.00006501135359, -0.0), (1.0, 1.0, 1.0), "Cavern_Stalactites_H14_122", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2875.0, 3995.0, 1915.0), (0.0, 114.9998400821187, -0.0), (1.0, 1.0, 1.0), "Cavern_Stalactites_H2", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3850.0, 4085.0, 2170.0), (0.0, 119.9998794919872, -0.0), (1.5, 1.5, 1.5), "Cavern_Stalactites_H3", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2670.0, 3020.0, 1995.0), (0.0, 0.0, -0.0), (1.0, 1.0, 1.0), "Cavern_Stalactites_H4_25", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2210.0, 3970.0, 2020.0), (0.0, 79.99999917458362, -0.0), (1.0, 1.0, 1.0), "Cavern_Stalactites_H5", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4615.0, 4580.0, 2130.0), (0.0, 64.99994332207724, -0.0), (1.0, 1.0, 1.0), "Cavern_Stalactites_H6_47", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5486.746, 3397.663, 2420.0), (0.0, 44.999928090234064, -0.0), (1.5963151, 1.5963151, 1.5963151), "Cavern_Stalactites_H7", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5464.685, 3521.7908, 2420.0), (0.0, -54.99987602838861, 0.0), (1.2568008, 1.2568008, 1.2568008), "Cavern_Stalactites_H8", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5338.641, 4296.3076, 2400.0), (0.0, -50.00006299960901, 0.0), (1.0, 1.0, 1.0), "Cavern_Stalactites_H9_70", _folder)
if a: placed += 1
else: skipped += 1

# Batch 8: StaticMesh'Cavern_Stalactites_I' (1 instances)
_mesh_path = "/Game/Art/Assets/Kits/Deco/Caveren/Cavern_Stalactites_I"
_materials = ['/Game/Art/Assets/Kits/Deco/Caveren/Materials/Cavern_Stalactites/Cavern_Stalactites_Mat_D']
_folder = "Reconstruction/BD_BB_TrollCave_AllInterfaces/Meshes"
a = spawn_static_mesh(_mesh_path, _materials, (2325.0, 2310.0, 1535.0), (0.0, 0.0, -0.0), (1.0, 1.0, 1.0), "Cavern_Stalactites_I_64", _folder)
if a: placed += 1
else: skipped += 1

# Batch 9: StaticMesh'Cavern_Stalactites_J' (2 instances)
_mesh_path = "/Game/Art/Assets/Kits/Deco/Caveren/Cavern_Stalactites_J"
_materials = ['/Game/Art/Assets/Kits/Deco/Caveren/Materials/Cavern_Stalactites/Cavern_Stalactites_Mat_B']
_folder = "Reconstruction/BD_BB_TrollCave_AllInterfaces/Meshes"
a = spawn_static_mesh(_mesh_path, _materials, (1000.0, 2775.0, 1505.0), (0.0, 0.0, -0.0), (1.0, 1.0, 1.0), "Cavern_Stalactites_J_109", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5805.0, 3445.0, 2390.0), (0.0, 0.0, -0.0), (1.0, 1.0, 1.0), "Cavern_Stalactites_J2_140", _folder)
if a: placed += 1
else: skipped += 1

# Batch 10: StaticMesh'PWM_Nordic_1x1x1_A' (7 instances)
_mesh_path = "/Game/Unshippable/Whitebox/Rocks/Meshes/PWM_Nordic_1x1x1_A"
_materials = ['/Game/Unshippable/Whitebox/Rocks/Materials/PWM_Nordic_Atlas_A']
_folder = "Reconstruction/BD_BB_TrollCave_AllInterfaces/Meshes"
a = spawn_static_mesh(_mesh_path, _materials, (3180.1733, 3227.6216, 928.4519), (0.0, 0.0, -0.0), (1.0, 1.0, 1.0), "PWM_Nordic_1x1x1_A_59", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (870.81116, 2646.64, 735.02246), (19.66283779814366, -121.94336093768304, -92.98669497171252), (1.0, 1.0, 1.0), "PWM_Nordic_1x1x1_A13", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (986.903, 2611.8408, 738.3576), (9.17205346402239, -127.55834783375265, 93.5285120827585), (0.625, 0.625, 0.625), "PWM_Nordic_1x1x1_A14", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (977.1246, 2776.5427, 716.7483), (-23.20595915083569, 64.6256707188326, -3.7902504456208934), (0.53125, 0.53125, 0.53125), "PWM_Nordic_1x1x1_A15", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5103.8076, 4841.7925, 685.0), (0.0, 78.74991862450624, -0.0), (0.65625, 0.65625, 0.65625), "PWM_Nordic_1x1x1_A22", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4458.335, 1295.2812, 1632.8966), (-69.24006081877863, 122.45075012315276, -174.87341991827728), (1.0, 1.0, 1.0), "PWM_Nordic_1x1x1_A5_85", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2067.3042, 5298.091, 836.5426), (19.645751617099698, 59.107524445860896, 91.77810308471686), (1.25, 1.25, 1.25), "PWM_Nordic_1x1x1_A9", _folder)
if a: placed += 1
else: skipped += 1

# Batch 11: StaticMesh'PWM_Nordic_1X1x1_C' (3 instances)
_mesh_path = "/Game/Unshippable/Whitebox/Rocks/Meshes/PWM_Nordic_1X1x1_C"
_materials = ['/Game/Unshippable/Whitebox/Rocks/Materials/PWM_Nordic_Atlas_A']
_folder = "Reconstruction/BD_BB_TrollCave_AllInterfaces/Meshes"
a = spawn_static_mesh(_mesh_path, _materials, (2879.8591, 4641.9053, 1988.9899), (13.445703811544035, 9.903807093223103, -124.24115042989102), (1.53125, 1.53125, 1.53125), "PWM_Nordic_1X1x1_C16_233", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5703.9673, 5131.6963, 855.0), (0.0, 163.1250808889642, -0.0), (1.0, 1.0, 1.0), "PWM_Nordic_1X1x1_C22", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5774.929, 4477.159, 825.259), (-13.13253709515907, 117.38790855643893, 0.4256031472647932), (0.75, 0.75, 0.75), "PWM_Nordic_1X1x1_C23", _folder)
if a: placed += 1
else: skipped += 1

# Batch 12: StaticMesh'PWM_Nordic_1X1x1_D' (1 instances)
_mesh_path = "/Game/Unshippable/Whitebox/Rocks/Meshes/PWM_Nordic_1X1x1_D"
_materials = ['/Game/Unshippable/Whitebox/Rocks/Materials/PWM_Nordic_Atlas_A']
_folder = "Reconstruction/BD_BB_TrollCave_AllInterfaces/Meshes"
a = spawn_static_mesh(_mesh_path, _materials, (5856.069, 4407.129, 777.8413), (3.8883702691528015, -168.6184002626919, 159.9240436039827), (0.5625, 0.5625, 0.4375), "PWM_Nordic_1X1x1_D12", _folder)
if a: placed += 1
else: skipped += 1

# Batch 13: StaticMesh'PWM_Nordic_2x2x2_A' (5 instances)
_mesh_path = "/Game/Unshippable/Whitebox/Rocks/Meshes/PWM_Nordic_2x2x2_A"
_materials = ['/Game/Unshippable/Whitebox/Rocks/Materials/PWM_Nordic_Atlas_B']
_folder = "Reconstruction/BD_BB_TrollCave_AllInterfaces/Meshes"
a = spawn_static_mesh(_mesh_path, _materials, (6150.0, 2750.0, 2350.0), (0.0, 0.0, -179.99995901885745), (2.2535331, 4.216879, 1.0), "PWM_Nordic_2x2x2_A_18", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1197.8186, 4303.766, 1670.0), (64.18922884033952, 169.38778965864398, 7.474712732438459), (1.40625, 1.40625, 1.40625), "PWM_Nordic_2x2x2_A10", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (6250.0, 1899.9998, 2350.0002), (-3.0517568642437468e-05, 179.9999112075241, -179.99995901885524), (2.253533, 4.216879, 1.0), "PWM_Nordic_2x2x2_A2", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2875.0, 225.0, 1534.9998), (-0.0002136229441721783, -179.99998633961317, -179.99998633961317), (3.5831633, 2.7452087, 1.0), "PWM_Nordic_2x2x2_A3_31", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3450.0, 225.00015, 1590.0016), (-0.0002136229441721783, -179.99998633961317, -179.99998633961317), (5.250682, 2.745209, 1.0), "PWM_Nordic_2x2x2_A4", _folder)
if a: placed += 1
else: skipped += 1

# Batch 14: StaticMesh'PWM_Nordic_4x4x4_A' (18 instances)
_mesh_path = "/Game/Unshippable/Whitebox/Rocks/Meshes/PWM_Nordic_4x4x4_A"
_materials = ['/Game/Unshippable/Whitebox/Rocks/Materials/PWM_Nordic_Atlas_B']
_folder = "Reconstruction/BD_BB_TrollCave_AllInterfaces/Meshes"
a = spawn_static_mesh(_mesh_path, _materials, (350.0, 3900.0, 1250.0), (0.0, 0.0, -0.0), (1.500039, 1.0, 2.478358), "PWM_Nordic_4x4x4_A_5", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (6193.879, 5151.166, 1906.4321), (-4.99996968531594, -79.99847821827, 1.0559061555003338e-06), (1.533746, 1.533746, 3.281985), "PWM_Nordic_4x4x4_A10", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5950.0015, 4750.0, 2500.0015), (0.0007579996641944295, -179.9999590188473, -179.9999863396144), (1.890689, 2.209067, 1.0), "PWM_Nordic_4x4x4_A11", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4274.505, 1704.4961, 2309.051), (3.5368555767494056, -6.409545689451951, -175.3204294113572), (1.67966, 1.009065, 1.291214), "PWM_Nordic_4x4x4_A118", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2876.0796, 2503.5715, 2308.657), (-6.946867520424525, -76.63597626496073, -171.5072724473252), (1.291214, 1.009065, 1.291214), "PWM_Nordic_4x4x4_A119", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2700.0, 250.0, 1150.0), (-5.000000000253746, 0.0, -0.0), (0.6597851, 1.2934501, 2.389508), "PWM_Nordic_4x4x4_A12_27", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5126.8564, 5243.0728, 1994.1846), (-19.90252636633224, -100.73378909974828, 91.92100351766126), (1.0, 1.0, 1.0), "PWM_Nordic_4x4x4_A122", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3800.6995, 250.0, 1161.514), (6.6757203471416295e-06, 0.0, -0.0), (0.659785, 1.29345, 2.389508), "PWM_Nordic_4x4x4_A13", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5236.37, 5096.0693, 2030.4854), (-5.311003862810884, -86.94344693468614, -178.32952250828862), (1.291214, 1.159436, 1.291214), "PWM_Nordic_4x4x4_A134", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (600.0, 3900.0, 1700.0), (0.0, 0.0, -0.0), (1.500039, 1.0, 3.097526), "PWM_Nordic_4x4x4_A2", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (600.0, 3850.0, 2050.0), (0.0, 0.0, -0.0), (1.500039, 1.0, 3.097526), "PWM_Nordic_4x4x4_A3", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2362.4138, 5167.5376, 897.74927), (9.416758778673616, 170.14892094284818, -3.4326471212131056), (1.0, 1.0, 1.0), "PWM_Nordic_4x4x4_A31", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (350.0, 3850.0, 2050.0), (0.0, 0.0, -0.0), (1.500039, 1.0, 3.097526), "PWM_Nordic_4x4x4_A4", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (399.80972, 2500.0, 1245.6422), (-5.000000000253746, 0.0, -0.0), (1.8268534, 1.0, 2.478358), "PWM_Nordic_4x4x4_A5", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (443.3876, 2500.0, 1743.7393), (-5.000000000253746, 0.0, -0.0), (1.826853, 1.0, 2.478358), "PWM_Nordic_4x4x4_A6", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5950.0015, 4050.0, 2500.0015), (0.0007581506385432647, -179.99995901884728, -179.99998633961434), (1.8906891, 2.209067, 1.0), "PWM_Nordic_4x4x4_A7_14", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5950.0015, 3350.0, 2500.0015), (0.0007579996641944295, -179.9999590188473, -179.9999863396144), (1.890689, 2.209067, 1.0), "PWM_Nordic_4x4x4_A8", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (6202.0986, 5104.5586, 1300.0), (-4.999969611448089, -79.99847821893754, 1.1439408087648928e-06), (1.5337455, 1.5337455, 3.2819846), "PWM_Nordic_4x4x4_A9_22", _folder)
if a: placed += 1
else: skipped += 1

# Batch 15: StaticMesh'PWM_Nordic_8x8x8_A' (149 instances)
_mesh_path = "/Game/Unshippable/Whitebox/Rocks/Meshes/PWM_Nordic_8x8x8_A"
_materials = ['/Game/Unshippable/Whitebox/Rocks/Materials/PWM_Nordic_Atlas_B']
_folder = "Reconstruction/BD_BB_TrollCave_AllInterfaces/Meshes"
a = spawn_static_mesh(_mesh_path, _materials, (3087.385, 3455.26, 481.2295), (0.0, 105.09361616731266, -0.0), (0.716173, 0.716173, 0.585617), "PWM_Nordic_8x8x8_A10", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3653.7227, 1242.24, 2294.7593), (5.116057545222782, -54.999148985936515, 178.74688802914358), (1.164826, 0.916686, 1.044235), "PWM_Nordic_8x8x8_A106_229", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2739.373, 1928.3596, 2402.7866), (9.167293693826215, -144.51822035130155, -178.3609648760422), (1.164826, 0.916686, 1.044235), "PWM_Nordic_8x8x8_A107", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3322.2493, 1933.6113, 2621.461), (9.167293627945835, -104.6184761631162, -178.36096483520302), (1.164826, 0.916686, 1.044235), "PWM_Nordic_8x8x8_A108", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3322.2493, 1532.9336, 2453.5881), (38.64707487391558, -93.73820994820568, -179.93560579185714), (1.164826, 0.916686, 1.044235), "PWM_Nordic_8x8x8_A109", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1013.8141, 4213.832, 2286.5505), (62.70605792901982, -88.72550402293537, 33.97257004328874), (1.0, 1.0, 1.0), "PWM_Nordic_8x8x8_A117", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2856.4058, 3742.6306, 2205.861), (-13.646332621792258, 153.8266812419163, -178.71997557028476), (0.8903745, 0.875643, 0.825709), "PWM_Nordic_8x8x8_A12", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4067.709, 2033.7844, 2207.5847), (-16.362699639100203, 124.41850097758436, 179.86096524772955), (0.9063328, 0.875643, 0.8655588), "PWM_Nordic_8x8x8_A13", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4240.6084, 1497.2075, 2339.2542), (29.150579137526154, 87.46701123636798, -172.05928244179975), (1.164826, 0.916686, 1.044235), "PWM_Nordic_8x8x8_A134", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3261.1326, 3622.648, 2320.8137), (1.4645087596899438, -2.799865449224144, -165.8808096080217), (0.9047756, 0.875643, 0.825709), "PWM_Nordic_8x8x8_A14", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4944.7207, 5540.964, 2419.9136), (14.148031771131492, 171.2061435451799, -169.07308733784842), (1.135899, 0.650977, 0.930144), "PWM_Nordic_8x8x8_A142", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4984.6465, 5299.0303, 764.0188), (2.949241150247021, -150.8549370391396, -1.5553590251270084), (0.828117, 0.8380555, 0.828117), "PWM_Nordic_8x8x8_A147", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (831.35364, 2179.6145, 700.56146), (1.0296780744609755, -3.412628353699302, 4.550048278997839), (0.85784894, 1.0, 1.0), "PWM_Nordic_8x8x8_A148_323", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2609.0, 5008.0347, 646.51404), (-1.5428823449028635e-08, -125.68739674070902, 4.664960628795637), (0.84375, 1.0, 1.0), "PWM_Nordic_8x8x8_A149", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3523.6008, 3309.826, 2371.5222), (-5.8081664392015435, 38.27369636588675, -173.02882646759508), (0.876314, 0.90988535, 0.8541286), "PWM_Nordic_8x8x8_A15_46", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2596.0718, 5123.2354, 1192.0131), (3.3307962301653706, 19.790388066935762, 175.05119253715873), (0.6402, 0.83755976, 0.79645), "PWM_Nordic_8x8x8_A150", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2761.8762, 4939.1445, 1408.92), (-13.023313347375847, -69.03644420926594, 176.54587414151686), (0.6402, 0.79645, 0.857066), "PWM_Nordic_8x8x8_A151", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (807.7643, 1553.0048, 740.7755), (-1.2220766154583953, 24.468479865771627, 4.5022298751545895), (0.84375, 1.0, 1.0), "PWM_Nordic_8x8x8_A152", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1201.7484, 1185.6593, 942.6431), (-3.7640684369137243, 63.05146573848311, 2.7572678855439485), (0.84375, 1.0, 1.0), "PWM_Nordic_8x8x8_A153", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2223.2063, 1665.6434, 561.1689), (0.7978430019841215, -36.272855739068994, -2.874542363924636), (0.84375, 1.0, 1.0), "PWM_Nordic_8x8x8_A154_12", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (751.55707, 2214.9604, 1136.5695), (-6.33251967613638, -21.48947271277309, 12.933696749486947), (0.682413, 0.8569631, 0.838663), "PWM_Nordic_8x8x8_A155", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1508.2854, 1780.9564, 2111.1106), (-23.626585510176902, 13.673437730058897, -167.64005085908073), (0.84375, 1.0, 1.0), "PWM_Nordic_8x8x8_A156", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (812.3656, 1978.9628, 1473.6693), (-11.739258871339565, 0.07372895663064448, -176.30512236294163), (0.87290454, 1.0, 1.0291545), "PWM_Nordic_8x8x8_A157", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (815.21893, 1315.49, 1582.3656), (3.6703244373792647, -160.36455473411775, 177.0059458621603), (0.84375, 1.0, 1.0), "PWM_Nordic_8x8x8_A158", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1677.169, 1298.4391, 716.7424), (0.7978428967351383, 121.72780525770219, -2.8745422897227404), (0.86213255, 1.0, 1.0), "PWM_Nordic_8x8x8_A159", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4409.3794, 3440.3499, 517.9391), (0.0, 104.6296247367404, -0.0), (0.572817, 0.572817, 0.442261), "PWM_Nordic_8x8x8_A16", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2484.1887, 2124.4214, 2174.048), (-7.496917207391012, 17.184792838892132, -168.59058031807433), (0.84375, 1.0, 1.0), "PWM_Nordic_8x8x8_A160_16", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1392.0754, 1233.438, 1363.0177), (-19.122282429084553, 85.4805030938158, -8.0297240163029), (0.84375, 1.0, 1.0), "PWM_Nordic_8x8x8_A161", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2098.9517, 1480.2903, 1391.5251), (17.023447277861244, -49.38849192501099, 10.076862551326023), (0.8491874, 1.0, 1.0), "PWM_Nordic_8x8x8_A162", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1039.5189, 2181.465, 485.03082), (0.963824047092287, 12.880597329938592, -3.582855686364997), (0.596456, 0.752706, 0.752706), "PWM_Nordic_8x8x8_A163", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2586.3914, 1501.7552, 740.64026), (2.348625318725163, 0.14170897961598397, -1.8395995387527235), (0.84375, 1.0, 1.0), "PWM_Nordic_8x8x8_A164", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2991.2354, 4937.707, 2165.1445), (-16.028135467177474, 5.8889335367481195, 159.22605803953357), (0.962839, 1.0222704, 1.0), "PWM_Nordic_8x8x8_A165_58", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2646.571, 853.48413, 643.3241), (2.159992324687505, -5.399688908628513, -2.0578304682615176), (0.84375, 1.0, 1.0), "PWM_Nordic_8x8x8_A166", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2850.4902, 1540.1417, 2232.51), (-2.7617798963510727, 35.34948287501582, 179.4193151764636), (0.84375, 1.0, 1.0), "PWM_Nordic_8x8x8_A167", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3228.0837, 1155.2269, 2187.7883), (-2.257293227513698, 60.37371717913277, 165.37298782960406), (0.84375, 1.0, 1.0), "PWM_Nordic_8x8x8_A168", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2285.8462, 1856.8842, 1731.306), (-0.026641873195814993, -37.40213300801502, 178.25768827762448), (0.715722, 0.8970275, 0.871972), "PWM_Nordic_8x8x8_A169", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3201.962, 3254.15, 557.79047), (9.769819534084544, -126.60950294432014, 2.6136777892560867), (0.742293, 0.651087, 0.691688), "PWM_Nordic_8x8x8_A17", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2628.7556, 1737.2542, 1821.3652), (-1.742095500934793, -125.59019794261526, 179.97133368390365), (0.715722, 0.89241296, 0.89241296), "PWM_Nordic_8x8x8_A170", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4011.971, 1468.8695, 491.97385), (-2.6207575746592515, 152.17071361954928, -3.064147470348416), (0.84375, 1.0, 1.0), "PWM_Nordic_8x8x8_A171", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3977.8203, 634.864, 947.0068), (7.754587966633054, 59.43634229149276, 4.415248651954634), (0.893067, 1.0154265, 1.0399783), "PWM_Nordic_8x8x8_A172", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3872.0625, 1096.4443, 1544.8712), (-2.654876281523292, 138.87843465166387, -176.21233846559724), (0.715722, 0.871972, 0.871972), "PWM_Nordic_8x8x8_A173", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3564.2715, 690.85925, 1638.6096), (-19.11159816216728, 177.72657933648242, -169.49161259215788), (0.715722, 0.871972, 0.871972), "PWM_Nordic_8x8x8_A174", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2851.1072, 835.02893, 1878.8289), (-21.90637249702447, 24.532992841747944, 173.44059162992846), (0.84375, 1.0, 1.0), "PWM_Nordic_8x8x8_A175", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2775.0986, 1290.727, 1751.4103), (-10.182983196697844, -9.39877322315735, -174.79843181742052), (0.66267, 0.81892, 0.81892), "PWM_Nordic_8x8x8_A176", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3374.9272, 5049.8657, 2010.9797), (-21.714785025767842, -51.10238869066678, -176.07535788315275), (1.0028436, 1.0, 1.0), "PWM_Nordic_8x8x8_A177", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5063.219, 5210.5015, 1984.7852), (6.832426582237475, 122.23820428449413, 178.71739967549053), (0.828117, 0.86527497, 0.905907), "PWM_Nordic_8x8x8_A179", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (903.32227, 4027.9639, 836.73694), (-2.1509702089064158, -7.988555242257786, 6.11009025005668), (0.8187, 1.0136709, 1.0286), "PWM_Nordic_8x8x8_A18", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3794.7607, 6165.877, 1038.5267), (0.0, 0.0, 3.513528507609396), (0.6875, 0.625, 0.828117), "PWM_Nordic_8x8x8_A180", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3703.2544, 1263.0964, 1910.4269), (-11.335448649382108, 142.8735082842508, -168.46648207105054), (0.715722, 0.871972, 0.871972), "PWM_Nordic_8x8x8_A181", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4501.9785, 4988.9424, 2351.9128), (-25.723906520174147, -95.76817679378637, -161.5511233310181), (0.927388, 0.927388, 0.97533464), "PWM_Nordic_8x8x8_A182", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4602.2446, 5495.901, 1941.7869), (0.9638217091279025, -134.39272238119946, -164.65343881553815), (0.927388, 0.927388, 0.9632157), "PWM_Nordic_8x8x8_A183", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4187.7607, 5450.0547, 1960.8804), (-13.728270368706237, -85.17052702512412, -177.08063904374035), (0.95491964, 0.927388, 0.9717991), "PWM_Nordic_8x8x8_A184", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4449.954, 5626.391, 765.0106), (3.0628269446578216, -99.74823061083245, 1.3172499560312971), (0.94934064, 0.930051, 0.930051), "PWM_Nordic_8x8x8_A185", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4489.1543, 5765.5303, 1413.7197), (1.3652107469185468, 80.14822195121774, 178.68399814645318), (0.930051, 0.930051, 1.0206652), "PWM_Nordic_8x8x8_A186", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5297.6675, 5235.1943, 1620.5902), (-10.033292261605586, -83.03324573415007, -175.91526022418003), (0.828117, 0.828117, 0.869545), "PWM_Nordic_8x8x8_A187_87", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3804.587, 4706.4854, 2421.4966), (-27.50610441669262, -63.25890189228491, -171.5457443970887), (0.927388, 1.134796, 0.9837068), "PWM_Nordic_8x8x8_A188", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5774.249, 5093.0146, 946.80914), (3.318708109307629, -128.50579783343952, -0.317840598663854), (0.84644425, 0.944889, 0.828117), "PWM_Nordic_8x8x8_A189", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1077.6993, 3889.4648, 736.9717), (-2.150878788719007, -1.8796997008429246, 6.11027092435146), (0.533895, 0.715195, 0.604851), "PWM_Nordic_8x8x8_A19", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5683.879, 4825.523, 2184.096), (-17.5806891796418, -119.54673849771075, -175.10483090333545), (0.828117, 0.944889, 0.828117), "PWM_Nordic_8x8x8_A190", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5777.093, 5093.9834, 1480.1621), (0.6518219253316739, 51.29339086891849, -179.87990476181986), (0.491014, 1.0, 1.0), "PWM_Nordic_8x8x8_A191", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4432.6084, 1382.2122, 720.4499), (3.0628273848581746, 27.431571306976878, 1.3172640944934595), (0.930051, 0.930051, 0.97785854), "PWM_Nordic_8x8x8_A192", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5929.01, 702.1663, 900.63043), (3.320783196683558, -53.895757973269134, 0.2937547030106372), (0.930051, 0.930051, 0.930051), "PWM_Nordic_8x8x8_A193", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5708.2593, 1088.0885, 2343.8467), (-18.198696204072213, 133.64808633907427, 171.25117536897181), (0.930051, 0.930051, 0.930051), "PWM_Nordic_8x8x8_A194", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5144.083, 704.50586, 798.26056), (3.062827386946314, 61.51540888929546, 1.317281370222335), (0.930051, 0.930051, 0.930051), "PWM_Nordic_8x8x8_A195", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5166.485, 959.48425, 2435.7402), (-11.330779182797412, 97.47338467774789, -174.0420744029868), (0.930051, 0.930051, 0.930051), "PWM_Nordic_8x8x8_A196", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4793.8237, 1191.6077, 2425.686), (-11.330749733031453, 48.365979304649095, -174.04207488466537), (0.930051, 0.930051, 0.930051), "PWM_Nordic_8x8x8_A197", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4674.8135, 835.7089, 1340.621), (3.517054317705281, 53.9142477148426, 0.5178222935081599), (0.9769572, 0.930051, 1.3883166), "PWM_Nordic_8x8x8_A198", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3097.097, 707.9248, 1850.962), (-20.20281993983508, 52.97795408785576, 169.1571264824437), (0.60337394, 0.75962394, 0.75962394), "PWM_Nordic_8x8x8_A199", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3703.2046, 3361.7427, 498.3415), (0.0, 25.356594836678447, -0.0), (0.716173, 0.716173, 0.716173), "PWM_Nordic_8x8x8_A2_38", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3611.8738, 2828.9702, 2676.6926), (-14.299315329799382, -29.113951001433197, -168.85679214618438), (0.876314, 0.875643, 0.825709), "PWM_Nordic_8x8x8_A20", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2635.2307, 1333.0961, 1365.7268), (-3.7624513708551803, -1.829681336363541, -176.14786687151715), (0.66267, 0.81892, 0.81892), "PWM_Nordic_8x8x8_A200", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2656.2239, 752.4962, 1023.6426), (-2.3682251201419833, 0.06072997619810658, 0.5933989736321861), (0.5533515, 0.69565916, 0.69565916), "PWM_Nordic_8x8x8_A201", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4525.033, 1872.1858, 2260.211), (-6.799559997427502, 46.89491997793775, -173.36694787529592), (0.84375, 1.0, 1.0), "PWM_Nordic_8x8x8_A202", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4986.9854, 5625.5503, 1408.3029), (7.763930832670578, 128.28567257567403, 176.38383920960487), (0.930051, 0.97008264, 0.930051), "PWM_Nordic_8x8x8_A203", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4682.735, 4680.149, 2525.3093), (-22.51089334306827, -73.09918551585898, -171.22624070529514), (1.097971, 1.1433954, 1.0194693), "PWM_Nordic_8x8x8_A204", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4469.748, 1388.2404, 1830.6543), (-0.6387023936880415, 0.3843113100698311, -173.47746548291892), (0.9605619, 0.9783594, 1.0620904), "PWM_Nordic_8x8x8_A205_48", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3712.4817, 3823.4717, 2595.2776), (-14.63613744858183, -22.65520931450812, 172.05993183883464), (1.4270873, 1.097971, 1.0274544), "PWM_Nordic_8x8x8_A206", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4850.311, 5124.427, 405.18643), (2.936231472621135, -151.32806316811067, -1.5796509111258517), (0.828117, 0.944889, 0.8541938), "PWM_Nordic_8x8x8_A207", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4208.7456, 2952.9714, 2758.4155), (-14.44726420044639, 17.78680749853923, 174.8027675774375), (1.097971, 1.097971, 0.975502), "PWM_Nordic_8x8x8_A208", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5950.447, 881.97864, 2205.7063), (10.84216112182629, -40.03624679566168, -173.13851335106898), (0.930051, 0.9431938, 0.930051), "PWM_Nordic_8x8x8_A209", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5045.1475, 728.6491, 1852.7839), (-12.498897740875778, 72.37447924234782, -179.3926621572634), (1.0, 1.0, 1.0), "PWM_Nordic_8x8x8_A210", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5668.1475, 644.889, 1849.8088), (13.239761261543537, -49.18517817383931, -176.5506165515261), (1.0196443, 1.0, 1.0626129), "PWM_Nordic_8x8x8_A211", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5351.254, 627.1726, 1163.2286), (-4.3681332542458735, 89.4112971915798, 2.6135615782403008), (0.930051, 0.930051, 1.1917176), "PWM_Nordic_8x8x8_A212", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (6065.826, 689.07825, 1185.408), (1.0575862115490637, 18.38607415436724, 9.151588969837677), (0.930051, 0.95723134, 1.191718), "PWM_Nordic_8x8x8_A213", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5861.2607, 1750.5503, 2431.939), (-30.558138476283933, 126.18767193222311, 173.5139652353435), (1.0, 1.0, 1.0638183), "PWM_Nordic_8x8x8_A214", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4741.0854, 2085.7256, 2670.7534), (-25.29138183130616, 46.28106729500719, -171.82019942576778), (1.0, 1.0, 1.0), "PWM_Nordic_8x8x8_A215", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3686.63, 5568.9873, 598.0499), (0.05314584670377822, -50.658135366425235, 3.333131640670854), (0.8756175, 0.8277332, 0.53578085), "PWM_Nordic_8x8x8_A216", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3259.3733, 5853.954, 1601.7322), (0.0, -85.68487447796103, 0.0), (1.125, 1.0, 0.828117), "PWM_Nordic_8x8x8_A217", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1530.7004, 5392.443, 875.3414), (0.0, -78.10543906466837, 0.0), (1.0, 1.0, 0.78017), "PWM_Nordic_8x8x8_A22", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1011.72797, 4999.632, 705.8142), (-1.7734068377698997, -24.085144608193954, -7.223632714361667), (1.0, 1.0, 0.78017), "PWM_Nordic_8x8x8_A23", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1017.38306, 4479.0776, 864.28174), (-9.063995499707639, 4.451722707613764, -12.390686894445176), (0.774347, 0.774347, 0.774347), "PWM_Nordic_8x8x8_A25", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1095.6906, 5015.551, 1067.3293), (-13.433807215858256, -20.65768190343244, -7.412444532308918), (0.774347, 0.774347, 0.774347), "PWM_Nordic_8x8x8_A26_11", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1585.9489, 4956.085, 2136.6506), (-23.60094990198456, -62.80913020921444, -175.18680591620844), (1.323908, 1.323908, 1.35512), "PWM_Nordic_8x8x8_A28_17", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2367.7659, 4313.3765, 2250.3687), (-55.188209139144746, -29.358768310830985, -148.26101910907266), (1.0, 1.0, 1.0), "PWM_Nordic_8x8x8_A29", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2115.902, 5366.9233, 699.94476), (0.0, -110.74154694578753, 0.0), (1.0, 1.0, 0.78017), "PWM_Nordic_8x8x8_A3_5", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2632.528, 4714.925, 2051.063), (-19.991513861885707, -48.79320836701635, 164.33278183310233), (1.0099134, 1.0, 1.0), "PWM_Nordic_8x8x8_A30_4", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5782.103, 3394.9763, 2771.0808), (-2.7846982633508905, 1.0123822855426905, 0.6278685619673058), (1.447527, 1.510502, 0.953836), "PWM_Nordic_8x8x8_A306", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5797.509, 2427.587, 2736.3403), (-2.78469825309873, 1.0123825868176963, -8.52166706082415), (1.447527, 1.510502, 0.953836), "PWM_Nordic_8x8x8_A307", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4955.125, 3380.3635, 2811.3125), (-2.7846982620448393, 1.0123820561321668, 0.6278685675309994), (1.4202985, 1.4832734, 0.953836), "PWM_Nordic_8x8x8_A308", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4969.3887, 2596.8198, 2819.8994), (-2.7846984022354975, 1.0123824794963943, -7.155700921616882), (1.447527, 1.510502, 0.953836), "PWM_Nordic_8x8x8_A309", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2485.699, 5854.4688, 1124.001), (0.2642979607656437, -175.2498818916431, -4.092803827883999), (1.0, 1.0, 1.0), "PWM_Nordic_8x8x8_A31", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5638.423, 4574.8774, 2640.7297), (-23.919068571506322, -4.9802858430787, -163.77636033286768), (1.447527, 1.510502, 0.953836), "PWM_Nordic_8x8x8_A310", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5862.243, 4589.8027, 2648.3071), (-5.781158180626959, -8.221863767920828, -165.12757053436698), (1.447527, 1.510502, 0.953836), "PWM_Nordic_8x8x8_A311", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2616.5518, 4806.3086, 2551.2253), (76.67787802526942, 54.33767395468147, -126.2867507451305), (1.15625, 1.594072, 1.499538), "PWM_Nordic_8x8x8_A313_296", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3669.6387, 3729.3096, 2778.802), (8.056056748226775, 2.265732624592785, 179.61839659213678), (1.447527, 1.510502, 0.953836), "PWM_Nordic_8x8x8_A314", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3648.8613, 4804.379, 2505.217), (8.05605533469629, 2.2658684321765454, -169.95287858872862), (1.4947426, 1.510502, 0.953836), "PWM_Nordic_8x8x8_A315", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2059.0464, 2897.6736, 2576.5684), (65.70006726098521, -130.98984009510522, -138.26000412134013), (1.2117823, 1.510502, 1.499538), "PWM_Nordic_8x8x8_A316", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1041.6924, 2841.5435, 2354.2576), (81.86756984420857, -38.50447170034081, 152.58495218385207), (1.1772101, 1.510502, 1.5862442), "PWM_Nordic_8x8x8_A317", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (608.75305, 2975.1462, 2414.5576), (81.86787768973852, -38.50417776524953, 147.58497318975662), (1.17721, 1.510502, 1.586244), "PWM_Nordic_8x8x8_A318", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2206.8977, 5283.7334, 1339.444), (-18.796937273560108, -114.98988959530298, 8.927459022066563), (1.0, 1.0, 1.0), "PWM_Nordic_8x8x8_A32_19", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1934.2666, 3669.8286, 2492.7866), (64.348498321878, 102.43042783744623, -130.9658197039213), (1.15625, 1.510502, 1.499538), "PWM_Nordic_8x8x8_A320", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1288.3881, 4179.372, 2098.9397), (-13.191651365870362, -0.159851058232397, 171.57432632857126), (1.0387527, 1.139548, 1.0), "PWM_Nordic_8x8x8_A33", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4956.1436, 5172.954, 2098.2993), (7.938961686525155, 167.39454682601706, -149.35889064609387), (0.977762, 0.578004, 0.857171), "PWM_Nordic_8x8x8_A331", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (939.32904, 4594.3223, 1025.6792), (-7.80722000926297, -7.139281710895196, -2.1012575398385938), (1.0329452, 1.005522, 1.005522), "PWM_Nordic_8x8x8_A34", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1566.3923, 5559.761, 1493.9277), (-1.4540711975828267, 9.728332609649536, -26.0005505342621), (1.169642, 1.0, 1.0), "PWM_Nordic_8x8x8_A35_21", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3082.1108, 3757.1343, 2502.8481), (-55.01812013262298, 0.7779534881687411, -173.5137985867292), (1.045717, 1.045717, 1.045717), "PWM_Nordic_8x8x8_A372", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1928.0703, 4550.208, 2287.806), (-28.716589501378103, -117.26399265689285, -164.10494920474392), (1.183271, 1.0796679, 1.183271), "PWM_Nordic_8x8x8_A38", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2338.1646, 5249.9155, 1876.0461), (19.679478468469195, 138.02342369297966, -161.9712730002033), (1.183271, 1.183271, 1.183271), "PWM_Nordic_8x8x8_A39", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3917.436, 3437.4211, 527.85046), (0.0, 68.33639208669814, -0.0), (0.716173, 0.71987355, 0.58561707), "PWM_Nordic_8x8x8_A4", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1629.8063, 3522.109, 2438.783), (-25.761989620114125, -19.87069453038501, 178.4876765317826), (1.183271, 1.2139395, 1.2422229), "PWM_Nordic_8x8x8_A43", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1286.7451, 3644.6885, 2147.7896), (-33.37115048360422, -10.180054463218939, -160.5135202981532), (1.0, 1.139548, 1.0), "PWM_Nordic_8x8x8_A44", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (808.0499, 4681.485, 1423.5557), (-2.1520686221975565, 79.86546889576506, -179.33932544978848), (1.005522, 1.031312, 1.005522), "PWM_Nordic_8x8x8_A45_30", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2999.781, 3342.804, 1966.3198), (-7.49923727497054, -142.36261079249746, 172.77807343885618), (0.7826326, 0.651087, 0.691688), "PWM_Nordic_8x8x8_A46_49", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4289.2314, 781.4863, 957.1162), (0.0, 132.2497384722338, -0.0), (0.649982, 0.649982, 0.550583), "PWM_Nordic_8x8x8_A47", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1154.9491, 4029.6147, 1810.8605), (-13.19149845750274, 9.005311459501929, 171.57429732205716), (0.764995, 0.813146, 0.764995), "PWM_Nordic_8x8x8_A48", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1116.8687, 2232.3433, 2287.7349), (-25.802336502182317, -23.8583993159102, -179.77794264487287), (1.183271, 1.183271, 1.183271), "PWM_Nordic_8x8x8_A49", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3415.3896, 3492.4897, 498.3415), (0.0, 87.65657023941883, -0.0), (0.716173, 0.716173, 0.716173), "PWM_Nordic_8x8x8_A5_40", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (980.2824, 4112.1465, 1467.3494), (-11.250212477608612, -6.069335112757599, 179.94469593558998), (0.7940052, 0.813146, 0.95262), "PWM_Nordic_8x8x8_A50", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (925.51074, 2219.1797, 1854.0668), (-10.091278868688136, -13.773071121259523, 178.64453792881756), (0.764995, 0.813146, 0.764995), "PWM_Nordic_8x8x8_A51", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (768.00464, 2325.6555, 1727.1108), (-13.292631019903807, -29.811395372480092, -173.8630441214659), (0.80300975, 0.8558162, 0.854397), "PWM_Nordic_8x8x8_A52", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1209.2922, 2233.867, 2052.2114), (10.742500253066149, -141.40398814139863, -170.02364546116485), (0.764995, 0.813146, 0.854397), "PWM_Nordic_8x8x8_A53", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1929.1393, 2237.9028, 2180.0962), (-5.053192306236713, 99.52752614065349, 176.6129761392958), (0.9796526, 0.837912, 0.854397), "PWM_Nordic_8x8x8_A54", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1917.887, 1773.4862, 2000.2034), (-17.88897058754223, 109.53715419506791, 175.28431926940456), (1.5019339, 1.1651049, 0.88158053), "PWM_Nordic_8x8x8_A55", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1260.6544, 1591.7015, 1838.5356), (-23.392022924497173, 53.675159479742106, -174.23273515220532), (1.0, 1.0, 1.0), "PWM_Nordic_8x8x8_A56", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1400.5863, 1816.8235, 1993.4844), (13.420183177895893, -160.90576178305784, -174.14301324222893), (0.764995, 0.813146, 0.854397), "PWM_Nordic_8x8x8_A57", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2601.06, 2659.2754, 2230.9011), (-10.671811810832661, 129.41040482901005, -177.30031576211977), (0.764995, 0.813146, 0.854397), "PWM_Nordic_8x8x8_A58", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2646.4553, 3138.6458, 2371.9915), (-7.745087698836209, -178.74134160443685, -179.8082013804834), (0.764995, 0.813146, 0.854397), "PWM_Nordic_8x8x8_A59", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3434.8555, 2474.8462, 2833.0742), (75.93744891053751, -145.366681668103, -21.106785085540125), (1.045717, 1.045717, 1.045717), "PWM_Nordic_8x8x8_A6_427", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3109.3984, 3460.9202, 1810.3081), (5.4405862263764, 50.566562149250444, -165.04918974551515), (0.61306, 0.521854, 0.691688), "PWM_Nordic_8x8x8_A60", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3272.7983, 4332.711, 2394.2483), (-16.084104345464542, -8.627745478785478, -178.68796687404188), (1.0, 1.0, 1.0), "PWM_Nordic_8x8x8_A61", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4607.9546, 1747.9823, 2504.9534), (14.323291343551878, -144.9620920727565, -171.87735635265756), (0.764995, 0.813146, 0.854397), "PWM_Nordic_8x8x8_A62", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5288.061, 1232.6001, 2430.202), (-19.942013769218647, 107.25841857080916, 177.4876275052946), (1.436024, 1.118003, 0.89387035), "PWM_Nordic_8x8x8_A63", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4769.4067, 4196.895, 2879.9976), (7.193877513531302, 174.8962915613595, -0.003540025071160631), (1.323453, 1.38103, 1.0486826), "PWM_Nordic_8x8x8_A64_3", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2322.0054, 3136.1973, 2551.329), (-32.39611853949881, -178.52264383334122, 179.56977220334954), (0.764995, 0.813146, 0.854397), "PWM_Nordic_8x8x8_A65", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4774.422, 1318.0574, 2467.2495), (16.182389071052313, -164.83026884443473, -177.15315863749703), (0.764995, 0.813146, 0.854397), "PWM_Nordic_8x8x8_A66", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2164.0364, 3628.4888, 2421.806), (-32.39606534208431, -133.2807652509179, 179.5697720292712), (0.764995, 0.813146, 0.854397), "PWM_Nordic_8x8x8_A67", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2955.8115, 3193.791, 481.2295), (0.0, -116.77416893206471, 0.0), (0.716173, 0.716173, 0.585617), "PWM_Nordic_8x8x8_A7", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2537.241, 3649.7446, 2342.7485), (-10.209470099928952, -158.37420388835994, 170.80997944468402), (0.876314, 0.875643, 0.87024564), "PWM_Nordic_8x8x8_A8", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3076.7358, 3029.7954, 2597.1765), (-24.361022108993513, -176.48176310685025, 179.22206271362742), (1.479404, 1.0, 0.705441), "PWM_Nordic_8x8x8_A9_437", _folder)
if a: placed += 1
else: skipped += 1

# Batch 16: StaticMesh'PWM_Nordic_Blend_A' (6 instances)
_mesh_path = "/Game/Unshippable/Whitebox/Rocks/Meshes/PWM_Nordic_Blend_A"
_materials = ['/Game/Art/Assets/Kits/Misc/Dirt_Mounds/Materials/MI_DirtMound_Cavern']
_folder = "Reconstruction/BD_BB_TrollCave_AllInterfaces/Meshes"
a = spawn_static_mesh(_mesh_path, _materials, (4877.7583, 4895.4473, 664.96484), (-5.110748798093559, 101.34218356826528, 4.29009545158158), (1.0, 1.0, 1.0), "PWM_Nordic_Blend_A_85", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5044.322, 4793.423, 687.6307), (-3.8943167642224235, -164.16194945369617, -5.418059622737982), (1.0, 1.0, 0.9556331), "PWM_Nordic_Blend_A2", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3739.0432, 5031.931, 619.5985), (0.0, 47.87896987649675, -0.0), (1.0, 1.0, 1.0), "PWM_Nordic_Blend_A3_93", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1846.2585, 1741.1165, 705.5331), (1.7931229698151603, -119.46156610395585, 1.4725066603786332), (1.0, 1.0, 1.0), "PWM_Nordic_Blend_A4_111", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3554.7595, 604.6755, 824.64496), (-4.943298655392334, -64.37154780108256, 2.0014671696132345e-06), (1.0, 1.0, 1.0), "PWM_Nordic_Blend_A5_123", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4085.8013, 3595.2512, 642.60986), (0.0, -18.91269009383058, 0.0), (1.0, 1.0, 1.0), "PWM_Nordic_Blend_A6_152", _folder)
if a: placed += 1
else: skipped += 1

# Batch 17: StaticMesh'PWM_Nordic_Blend_B' (46 instances)
_mesh_path = "/Game/Unshippable/Whitebox/Rocks/Meshes/PWM_Nordic_Blend_B"
_materials = ['/Game/Art/Assets/Kits/Misc/Dirt_Mounds/Materials/MI_DirtMound_Cavern']
_folder = "Reconstruction/BD_BB_TrollCave_AllInterfaces/Meshes"
a = spawn_static_mesh(_mesh_path, _materials, (5636.9316, 4867.614, 755.21454), (11.184338091635354, 1.2620742838475782, 6.480125045303067), (1.0, 1.0, 1.0), "PWM_Nordic_Blend_B_80", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1769.9072, 5138.26, 724.0316), (4.667631882911332, 22.306911805153437, -3.353362947475019), (1.0, 1.0, 1.0), "PWM_Nordic_Blend_B10", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1369.9943, 4966.356, 665.6162), (-0.3461610078164782, 74.80230073475293, 1.6609359718643766), (1.0, 1.0, 1.0), "PWM_Nordic_Blend_B11", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1240.9797, 4193.95, 659.5301), (-1.305206160123167, 113.3129682814549, 1.0840794678082015), (1.0, 1.0, 1.0), "PWM_Nordic_Blend_B12", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1243.308, 4595.5195, 653.89105), (-1.8712459555159056, 120.59721216674073, 5.564221415772033), (1.0, 1.0, 1.0), "PWM_Nordic_Blend_B13", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1084.3083, 1668.2972, 720.6969), (0.0, 118.03669117323365, -0.0), (1.0, 1.0, 1.0), "PWM_Nordic_Blend_B14_103", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1100.6305, 2313.436, 720.6482), (-4.166995983195857e-08, 109.81703622673503, -2.9159238309023183), (1.0, 1.0, 1.0), "PWM_Nordic_Blend_B15", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (824.7343, 2544.6184, 718.7656), (0.07127295157613915, 43.56308270033508, -5.884429721454847), (1.0, 1.0, 1.0), "PWM_Nordic_Blend_B16", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2003.2994, 1953.941, 645.5784), (-3.76232735178689e-08, -106.64783082280952, 8.269023382034764), (1.0, 1.0, 1.0), "PWM_Nordic_Blend_B17", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1354.2483, 1426.3647, 753.6167), (8.39243010907767, -135.62834551991867, 3.4269598006034823), (1.0, 1.0, 1.0), "PWM_Nordic_Blend_B18", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1641.4113, 1512.4371, 729.0579), (2.069876294709291, -117.91668301459089, 4.476886245854997), (1.0, 1.0, 1.0), "PWM_Nordic_Blend_B19", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5329.067, 4974.446, 716.6254), (5.454000412929822, 36.28216162675077, 11.714746560759089), (1.0, 1.0, 1.0), "PWM_Nordic_Blend_B2", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2357.4724, 2181.8171, 589.5252), (0.0, -177.047139991019, 0.0), (1.0, 1.0, 1.0), "PWM_Nordic_Blend_B20_114", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2652.413, 2060.8657, 602.6436), (2.9149823412546647e-10, -177.04714019570295, 5.615828024472703), (1.0, 1.0, 1.0), "PWM_Nordic_Blend_B21", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2887.6973, 1738.896, 653.7908), (-7.512451072202856, 98.9149882323272, -9.3718562260542), (1.0, 1.0, 1.0), "PWM_Nordic_Blend_B22", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2871.9634, 1344.8604, 699.6483), (-0.9385063600813074, 132.8742809133972, -11.955564418229873), (1.0, 1.0, 1.0), "PWM_Nordic_Blend_B23", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3818.4639, 1680.0913, 618.8356), (2.490648929129447, -91.1780702741165, 0.7897140874937065), (1.0, 1.0, 1.0), "PWM_Nordic_Blend_B24", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3637.5059, 1215.6868, 678.8518), (12.159371637443137, -91.5464658345923, 10.684729069666114), (1.0, 1.0, 1.1120026), "PWM_Nordic_Blend_B25", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3640.43, 796.19775, 761.67584), (5.787245616550132, 120.57744686055689, -11.446288718974554), (0.7824401, 0.8026593, 1.0889387), "PWM_Nordic_Blend_B26", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2792.3796, 753.42957, 830.09863), (0.0, 92.7120401955283, -0.0), (0.9066556, 1.0, 1.0), "PWM_Nordic_Blend_B27_126", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4186.579, 1859.312, 673.1539), (0.0, -159.8325494105676, 0.0), (1.0, 1.0, 1.0), "PWM_Nordic_Blend_B28_129", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4730.608, 1405.9037, 685.908), (0.0, 163.0771872475364, -0.0), (1.0, 1.0, 1.0), "PWM_Nordic_Blend_B29_132", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4626.896, 5265.3403, 696.40686), (3.08236898245343, -20.898682770207763, -7.312438590019309), (1.0, 1.0, 1.0), "PWM_Nordic_Blend_B3", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4602.7837, 1693.063, 659.9636), (0.0, 146.34829448838482, -0.0), (1.0, 1.0, 1.0), "PWM_Nordic_Blend_B30", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5393.822, 931.62286, 706.04926), (-4.046385966314375, -166.59249514798543, 8.675443895807162e-07), (1.0, 1.0, 1.0), "PWM_Nordic_Blend_B31", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5078.5186, 1115.3502, 678.6557), (-3.269043077350143, 157.26086271973693, 2.3854539547623568), (1.0, 1.0, 1.0), "PWM_Nordic_Blend_B32", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5725.13, 999.97894, 729.5229), (-2.697387554931905, -112.5201768186872, 1.068551116443366), (1.0, 1.0, 1.2745583), "PWM_Nordic_Blend_B33", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (6098.121, 1095.1041, 764.7028), (-0.20242307314213331, 11.046438839974552, 0.2554161544628997), (1.0, 1.0, 1.274558), "PWM_Nordic_Blend_B34", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5954.352, 4806.559, 802.1489), (0.0, -73.120847474859, 0.0), (1.0, 1.0, 1.0), "PWM_Nordic_Blend_B35_140", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4094.4084, 3199.2715, 650.27405), (0.0, 83.36039247497557, -0.0), (1.0, 1.0, 0.76719314), "PWM_Nordic_Blend_B36_143", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3753.4824, 2853.1401, 604.4849), (4.096678014152851e-08, 28.921348145323922, 6.504073033848631), (1.0, 1.0, 0.767193), "PWM_Nordic_Blend_B37", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3203.511, 2908.9255, 602.3408), (0.6346339034792238, 23.344006454175073, 5.1323792609001355), (1.0, 1.0, 0.8148131), "PWM_Nordic_Blend_B38", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2808.4514, 3067.6104, 599.5986), (3.619051381548992, -17.88867376451743, 3.6964389523013166), (1.0, 1.0, 0.814813), "PWM_Nordic_Blend_B39", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4322.2554, 5405.721, 693.1418), (7.388693106239088, 24.906468294816495, 0.24004179237999562), (1.0, 1.0, 1.0), "PWM_Nordic_Blend_B4", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2783.7014, 3448.8723, 622.88983), (1.1189751072340999, -112.04267476429447, -0.8315430223266613), (1.0, 1.0, 0.73006), "PWM_Nordic_Blend_B40", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3199.0503, 3635.8474, 646.5787), (-0.9306642641032252, -159.96609910037998, -5.087096581618372), (1.0, 1.0, 0.543558), "PWM_Nordic_Blend_B41", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3686.0828, 3686.0378, 614.64276), (-0.9306642641032252, -159.96609910037998, -5.087096581618372), (1.0, 1.0, 0.6822051), "PWM_Nordic_Blend_B42", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1211.7456, 3857.702, 659.53015), (-1.3052062115044951, 108.22301305064825, 1.0840816700511162), (1.0, 1.0, 1.0), "PWM_Nordic_Blend_B43_157", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1021.2572, 3493.3943, 664.6913), (-1.305206223176327, 39.52260318118202, 1.084085245707367), (1.0, 1.0, 1.0), "PWM_Nordic_Blend_B44", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3508.1184, 6049.082, 674.2397), (0.0, -88.03511965924548, 0.0), (1.0, 1.0, 0.5), "PWM_Nordic_Blend_B45", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2797.365, 5932.5527, 667.457), (0.0, -88.03511965924548, 0.0), (1.0, 1.0, 0.5), "PWM_Nordic_Blend_B46", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3900.0205, 5328.681, 678.11273), (6.091278228160606, 69.1224863702861, 3.062369043441763), (1.0, 1.0, 0.5), "PWM_Nordic_Blend_B5", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3352.8179, 4875.36, 600.29), (0.14352951330323138, 26.81126770366799, 3.7392484126775876), (1.0, 1.0, 1.0), "PWM_Nordic_Blend_B6", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2573.5696, 4724.5176, 639.5677), (-0.6142272570397195, -4.26464848463652, 3.131415827692897), (1.0, 1.0, 1.0), "PWM_Nordic_Blend_B7", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3000.413, 4791.518, 605.93744), (-2.2883297100961606, 68.87898354608008, 4.59556647018404), (1.0, 1.0, 1.0), "PWM_Nordic_Blend_B8", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2265.5408, 4938.761, 686.0059), (-8.261260120734523, -16.464717924096288, -9.94842365528406), (1.0, 1.0, 1.0), "PWM_Nordic_Blend_B9", _folder)
if a: placed += 1
else: skipped += 1

# Batch 18: StaticMesh'PWM_Quarry_2x2x2_A' (17 instances)
_mesh_path = "/Game/Unshippable/Whitebox/Rocks/Meshes/PWM_Quarry_2x2x2_A"
_materials = ['/Game/Art/Assets/Landmarks/CrystalDescent/Materials/Rock_Materials/ProcMaterial_Quarry_2m_Nordic']
_folder = "Reconstruction/BD_BB_TrollCave_AllInterfaces/Meshes"
a = spawn_static_mesh(_mesh_path, _materials, (3810.1462, 1149.3156, 806.94476), (0.0, 15.009344260701418, -0.0), (1.576518, 1.576518, 1.576518), "PWM_Quarry_2x2x2_A_24", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3264.2632, 5018.181, 1616.818), (6.074142025803237, 74.37637249941926, 177.76911896955698), (2.0208595, 1.695827, 2.7098274), "PWM_Quarry_2x2x2_A10", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4163.6826, 5753.8604, 1022.796), (0.3510854986962765, -71.17971708448971, -177.41191003469282), (1.981949, 1.695827, 2.161899), "PWM_Quarry_2x2x2_A11", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3677.7566, 5349.344, 1675.9664), (3.144625819028424, 33.567726147018206, 174.34323527820447), (1.981949, 1.695827, 2.161899), "PWM_Quarry_2x2x2_A12", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4550.452, 1799.3048, 2157.943), (5.277207610747837, 143.2846188879106, 165.04230078218205), (1.576518, 1.046619, 1.576518), "PWM_Quarry_2x2x2_A13", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5166.2324, 1662.8372, 2225.5112), (12.677450375209384, 176.73426906124774, 170.42243989958413), (1.576518, 1.046619, 1.576518), "PWM_Quarry_2x2x2_A14", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5425.509, 1726.7394, 2230.5308), (15.785443750391027, -115.682167920298, -170.59807534368733), (1.17972, 1.7091554, 1.576518), "PWM_Quarry_2x2x2_A15", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2669.3696, 864.91455, 1366.4176), (4.204847804157145, -104.61549916428446, -172.98318242575425), (1.576518, 1.3502156, 1.756468), "PWM_Quarry_2x2x2_A16", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2635.0886, 490.39203, 1386.1279), (4.204847804157145, -104.61549916428446, -172.98318242575425), (2.3404086, 1.5700822, 1.756468), "PWM_Quarry_2x2x2_A17", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3887.0005, 1114.1226, 1107.2959), (4.9365268514578435, -5.540160657298976, 2.2449829767603062), (1.576518, 1.576518, 1.576518), "PWM_Quarry_2x2x2_A2", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (997.12683, 1678.9999, 1400.741), (4.070747904157928, 147.17931409798982, 169.0597606671413), (1.576518, 1.046619, 1.576518), "PWM_Quarry_2x2x2_A3", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1159.2117, 2303.9482, 1707.3386), (5.875961537721323, 146.8281840869785, 169.02893542509557), (1.576518, 1.046619, 1.576518), "PWM_Quarry_2x2x2_A4", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1776.722, 2231.0796, 1889.0269), (10.9775950063017, -179.3488541492273, 174.13602487359236), (1.576518, 1.046619, 1.576518), "PWM_Quarry_2x2x2_A5", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2031.7588, 2308.442, 1906.4845), (11.776487055632531, -112.566033036189, -170.7600764644877), (1.17972, 1.624607, 1.576518), "PWM_Quarry_2x2x2_A6", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2509.229, 1978.1451, 1330.9365), (3.267811963560591, -161.31545881642785, 174.81073227648372), (0.959271, 1.5435411, 1.708786), "PWM_Quarry_2x2x2_A7", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2212.0645, 1937.2198, 1439.5852), (3.577924327287949, -95.52418963424275, -173.41847790801523), (1.576518, 1.148125, 1.576518), "PWM_Quarry_2x2x2_A8", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2715.595, 1201.031, 976.2497), (3.918478868310054, -101.44507405276698, 5.290159474232548), (1.6382234, 1.3402325, 1.8181734), "PWM_Quarry_2x2x2_A9", _folder)
if a: placed += 1
else: skipped += 1

# Batch 19: StaticMesh'PWM_Quarry_4x3x10_A' (99 instances)
_mesh_path = "/Game/Unshippable/Whitebox/Rocks/Meshes/PWM_Quarry_4x3x10_A"
_materials = ['/Game/Art/Assets/Landmarks/CrystalDescent/Materials/Rock_Materials/ProcMaterial_Quarry_2m_Nordic']
_folder = "Reconstruction/BD_BB_TrollCave_AllInterfaces/Meshes"
a = spawn_static_mesh(_mesh_path, _materials, (3085.6514, 3269.057, 1729.7439), (7.806114780192213, -17.951724547108594, -179.16545300985828), (1.0, 1.0, 0.837841), "PWM_Quarry_4x3x10_A559", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3209.016, 3262.7937, 916.2119), (-2.194793794198326, 91.28124333462526, 3.7505191360794408), (1.0, 1.0, 0.837841), "PWM_Quarry_4x3x10_A560", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3511.3657, 3436.7922, 966.80054), (-4.080658053827626, 47.24792439250636, -1.066314820126071), (1.0, 1.0, 0.538012), "PWM_Quarry_4x3x10_A561", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3314.9568, 3546.5244, 1859.6436), (0.755705855536568, -178.15179976938583, 177.8910526160868), (1.0, 1.0, 0.538012), "PWM_Quarry_4x3x10_A562", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3610.3813, 3342.7666, 784.7112), (1.750694265980216, -149.91436025433669, 2.219674289110126), (1.5481585, 1.60384, 0.44229972), "PWM_Quarry_4x3x10_A563", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3418.632, 3100.8738, 685.3434), (-3.909790064365258, -141.53131666923062, 1.6579972349759933), (1.493269, 1.648795, 0.4423539), "PWM_Quarry_4x3x10_A564", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3307.8977, 3196.0674, 795.3096), (2.099122272295449, 1.056274524535237, -3.691649935487348), (1.5155272, 1.6697897, 0.422377), "PWM_Quarry_4x3x10_A565", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3399.5085, 3380.827, 872.8713), (2.3876089386054655, 125.95250942573664, -1.5133055558033133), (1.493269, 1.60384, 0.422377), "PWM_Quarry_4x3x10_A566", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3345.7417, 3460.5308, 1636.7378), (2.8257143825964506, -1.8034053134515546, -177.8432671103275), (1.0, 1.0, 0.538012), "PWM_Quarry_4x3x10_A567", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3604.2068, 3259.4712, 941.65735), (2.3391338929736882, -129.48990457121516, 2.2245176875976753), (1.0, 1.0, 0.538012), "PWM_Quarry_4x3x10_A568", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3383.6548, 3241.6553, 1015.0252), (-3.464934810154351, -83.17455359784664, -2.455139171540308), (1.293931, 1.484016, 0.422377), "PWM_Quarry_4x3x10_A569", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3332.9236, 3152.417, 1164.2842), (2.359028877382152, -130.00832937227761, 2.203185874737158), (1.0, 1.0, 0.5625), "PWM_Quarry_4x3x10_A570", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3280.7244, 3210.0645, 1869.4722), (2.459557593366289, 83.24282473004008, -177.8543682147157), (1.066254, 1.1409131, 0.538012), "PWM_Quarry_4x3x10_A571", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3250.3142, 3219.354, 1425.098), (1.8548756433396165, -135.69113454701832, -179.87439281706935), (0.8950378, 0.865033, 0.610426), "PWM_Quarry_4x3x10_A572", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2363.3865, 1843.8628, 1142.4692), (-2.7344054456740636, -36.34308008861306, 0.7158809988431918), (1.5441976, 1.6338711, 0.689533), "PWM_Quarry_4x3x10_A573_21", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3983.2048, 1784.5486, 1753.9473), (1.3671579886654215, -171.52669112064925, 177.98492192476965), (1.0411963, 1.0308677, 0.716295), "PWM_Quarry_4x3x10_A574", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3956.8555, 1378.7227, 1173.9086), (2.6342269349348935, 8.61532523439416, 2.016601640556939), (1.0, 1.0, 0.716295), "PWM_Quarry_4x3x10_A575", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4053.6199, 1572.8545, 1135.8), (2.970446143342225, -2.3906250598629946, 1.476806589563509), (1.0, 1.1113013, 0.716295), "PWM_Quarry_4x3x10_A576", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (950.9556, 2636.693, 1811.8198), (-0.06356811992041402, 177.94884656926433, -174.67493513064832), (1.0299962, 1.0299962, 0.716295), "PWM_Quarry_4x3x10_A577", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1113.333, 2602.9268, 2037.1296), (-2.534514931439358, -31.087149778105857, 179.1831091275277), (1.0, 1.0, 0.716295), "PWM_Quarry_4x3x10_A578", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1327.929, 2499.129, 2072.7292), (-2.651641932139547, -54.20702501150194, -179.75659238066086), (1.0, 1.0, 0.716295), "PWM_Quarry_4x3x10_A579", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1468.0122, 2350.9976, 2061.3518), (7.280747171533027, -169.99756390784617, -177.70618772842835), (1.0700612, 1.0700612, 0.716295), "PWM_Quarry_4x3x10_A580", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1099.5063, 2530.9873, 1921.53), (6.133462502704266, 163.95385500840635, -177.85016038821698), (1.0292534, 1.0, 0.7245281), "PWM_Quarry_4x3x10_A581", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (949.02094, 2609.5295, 698.52795), (-8.32528642832607, -79.20226710702684, 2.627928986170761), (1.0, 1.0, 0.393695), "PWM_Quarry_4x3x10_A582", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1543.5577, 1563.9851, 1692.6907), (5.40905064912519, 110.82957186751123, 176.39380128152484), (1.050015, 1.0, 0.7359204), "PWM_Quarry_4x3x10_A583", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1690.9557, 1676.7639, 1756.3848), (2.17531326265879, -69.04486347710493, -174.35388956553598), (1.0195788, 1.0, 0.72898346), "PWM_Quarry_4x3x10_A584", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1262.3434, 1978.9813, 1750.4048), (24.552253228977943, -126.98400788858449, -171.38324174581737), (1.0315909, 1.0, 0.7246957), "PWM_Quarry_4x3x10_A585", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2431.843, 2011.3566, 663.1792), (-4.396209682053643, -66.34116198587101, 3.3587512297121713), (1.216027, 1.326599, 0.42268145), "PWM_Quarry_4x3x10_A586", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2681.0754, 1970.8893, 586.387), (-6.182249896429125, -117.14218337807436, 8.436294942500444), (1.216027, 1.326599, 0.412291), "PWM_Quarry_4x3x10_A587", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2627.8328, 1664.5374, 1189.896), (7.132867359594163, -173.82246725842748, 0.35220897483700797), (1.216027, 1.326599, 0.412291), "PWM_Quarry_4x3x10_A588", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2719.4248, 2045.7166, 1785.2887), (7.002643757038276, -174.07116837764107, 174.64910882715822), (1.0958586, 1.0430652, 0.73934084), "PWM_Quarry_4x3x10_A589_50", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2939.3113, 1974.3569, 1903.7351), (7.3266070782089825, -170.44144161542494, 175.10071553735224), (1.0403202, 1.0196097, 0.73733175), "PWM_Quarry_4x3x10_A590", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2738.301, 1749.6688, 1416.9767), (3.469753053381257, -130.56333454673168, -176.25778497207762), (1.0021894, 1.1016153, 0.369592), "PWM_Quarry_4x3x10_A591", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3264.6748, 5064.427, 1016.0201), (6.452168118139661, 156.80834023074482, 1.01943974634883), (1.0, 1.0, 0.705696), "PWM_Quarry_4x3x10_A592_63", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3084.5479, 5008.668, 1234.34), (-4.866790248722861, 18.390989044060536, 175.07019010274945), (1.0, 1.0, 0.705696), "PWM_Quarry_4x3x10_A593", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2950.1064, 4889.1167, 1399.7543), (9.369891313599657, 96.98861095234219, 178.1583311769465), (1.0, 1.0, 0.756312), "PWM_Quarry_4x3x10_A594", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3549.264, 5226.7617, 1622.7101), (3.2765239960066936, 56.036174438315555, -178.39647879174692), (1.0, 1.0, 0.705696), "PWM_Quarry_4x3x10_A595", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3464.3428, 5156.235, 1072.1301), (5.2784181776608134, -175.98295738023722, 3.8530876979834168), (1.0, 1.0, 0.8125), "PWM_Quarry_4x3x10_A596", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3832.047, 5498.189, 1421.3036), (3.413133914542064, 38.39659880124343, 169.00820514658747), (1.0, 1.0, 0.4375), "PWM_Quarry_4x3x10_A597", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3691.543, 5427.5537, 1391.6218), (0.7818098546274003, -162.4908801978448, -168.5203426007958), (1.0, 1.0, 0.4375), "PWM_Quarry_4x3x10_A598", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5154.7046, 5152.3364, 1403.9092), (4.614037342139196, 100.3480121267326, -178.59584860242705), (1.0, 1.0, 0.705696), "PWM_Quarry_4x3x10_A599", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5331.6797, 5213.284, 1328.4678), (-4.57504234612464, -78.11150661665863, 178.47240321635846), (1.0, 1.0, 0.705696), "PWM_Quarry_4x3x10_A600", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3484.1497, 3343.8137, 1268.5902), (2.3391338929736882, -129.48990457121516, 2.2245176875976753), (1.0275248, 1.0, 0.538012), "PWM_Quarry_4x3x10_A601", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3841.4414, 3062.1724, 572.9761), (-7.454864023906969, 169.8737668380609, -1.1858826506744036), (1.5131154, 1.60384, 0.43567184), "PWM_Quarry_4x3x10_A602", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4741.352, 2006.9506, 2505.0906), (-0.6770630471201868, -57.46373868973842, -176.26208945658882), (1.0, 1.0, 0.716295), "PWM_Quarry_4x3x10_A603_22", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4872.7847, 1850.7933, 2499.0413), (9.55651517454677, -173.64165826300695, 178.95312955923293), (1.0, 1.0, 0.716295), "PWM_Quarry_4x3x10_A604", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4648.4663, 1489.2618, 2232.573), (28.47063660302373, -130.56914300904975, -172.34656231963862), (1.0, 1.0, 0.716295), "PWM_Quarry_4x3x10_A605", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4989.719, 5149.34, 1160.0446), (5.514352265089794, 91.69736111835705, 5.570918982580418), (1.0, 1.0, 0.705696), "PWM_Quarry_4x3x10_A606", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3523.6572, 3488.2095, 2092.667), (1.098136691280857, -168.5157497486777, 178.0472905529468), (1.0700396, 1.1630056, 0.4445356), "PWM_Quarry_4x3x10_A607", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3719.7786, 3290.2434, 2114.3457), (0.7362054691003262, -178.67823324961768, 177.88415343051832), (1.07004, 1.163006, 0.444536), "PWM_Quarry_4x3x10_A608", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5212.481, 4722.203, 2205.6316), (8.20735602314112, 53.687388528136104, 177.4276844135568), (1.0090485, 1.0, 0.57359624), "PWM_Quarry_4x3x10_A609_40", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4957.1387, 4600.492, 2460.4211), (7.477314593589215, 41.38671334518386, 171.56739437275064), (1.3788123, 1.0, 0.57961047), "PWM_Quarry_4x3x10_A610", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5343.5776, 5144.638, 850.3403), (-8.47579962514068, 149.281560299279, -2.516601050988141), (1.1669441, 1.1669441, 0.62668437), "PWM_Quarry_4x3x10_A611_44", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5568.168, 5002.9854, 728.0527), (-8.438812696944302, 115.24329750228627, 2.638549588854121), (1.166944, 1.166944, 0.609014), "PWM_Quarry_4x3x10_A612", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5216.921, 4980.9067, 703.7916), (-7.691405594919409, 162.39151776337195, -4.3682552360726365), (1.143817, 1.2432785, 0.46236414), "PWM_Quarry_4x3x10_A613", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4320.32, 1623.4276, 1166.3007), (3.7442200960519476, -167.42614769036857, 179.35987116177552), (1.0, 1.0, 0.716295), "PWM_Quarry_4x3x10_A614", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4490.476, 1408.5394, 1190.176), (-4.126160036474553, 12.570617242413169, 0.64044182454678), (1.1151954, 1.0300118, 0.716295), "PWM_Quarry_4x3x10_A615", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (6047.383, 1010.1987, 1601.21), (-7.322935316449037, 77.31908534704495, 179.45283809652202), (1.0736017, 1.0300314, 0.8095929), "PWM_Quarry_4x3x10_A616", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (6219.942, 1047.0913, 2074.8555), (-6.810759997744214, 50.9733822527826, -177.2481251578507), (1.0, 1.0, 0.809593), "PWM_Quarry_4x3x10_A617", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (6222.7056, 914.8369, 1477.7096), (-1.8370359693980147, -6.158019842183078, -177.46963934408126), (1.0, 1.0, 0.809593), "PWM_Quarry_4x3x10_A618", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4473.965, 2313.6416, 2271.5652), (5.321241488789861, 164.10728278329861, 175.39410425095042), (1.0, 1.0, 0.716295), "PWM_Quarry_4x3x10_A619", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4745.551, 1704.1519, 1962.3307), (-6.1526484746325325, 64.94339046428269, 179.47748170386794), (1.0, 1.0, 0.716295), "PWM_Quarry_4x3x10_A620", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4450.0186, 2015.5377, 2043.6025), (2.3831959502706677, 172.70192180924795, 174.3016365170797), (1.0, 1.0, 0.716295), "PWM_Quarry_4x3x10_A621", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4630.294, 1980.1759, 2234.8762), (3.148990462339739, -179.36127838922422, 174.68480835602392), (1.0, 1.0, 0.716295), "PWM_Quarry_4x3x10_A622", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4995.339, 1639.7568, 2219.3665), (3.148990233148671, -179.36127837855133, 174.68480835446073), (1.1251074, 1.0, 0.716295), "PWM_Quarry_4x3x10_A623", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4757.6187, 1242.1367, 2047.7894), (0.2744573811252478, 152.61466091173781, 173.83074625604482), (1.0434366, 1.0, 0.716295), "PWM_Quarry_4x3x10_A624", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5712.7256, 1118.6659, 2030.0544), (-15.645386142315013, 89.24070230826547, 176.9466002708654), (1.0, 1.0, 0.716295), "PWM_Quarry_4x3x10_A625", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5588.416, 1368.5459, 2218.794), (-8.52691353170318, 136.37137823302353, 166.48914252474043), (1.0, 1.0, 0.716295), "PWM_Quarry_4x3x10_A626", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4345.4805, 4219.1997, 2432.6887), (-11.135343701333568, -104.02148488182863, -176.6211065500976), (1.0, 1.0, 0.538012), "PWM_Quarry_4x3x10_A627", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4257.727, 4089.4153, 2503.1426), (-4.042755313687649, -156.93929815488625, -169.0855276572109), (1.0, 1.0, 0.538012), "PWM_Quarry_4x3x10_A628", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5886.166, 4391.22, 2277.22), (3.243130515604231, 3.166311518078102, 172.0319293022839), (1.0, 1.0, 0.538012), "PWM_Quarry_4x3x10_A629", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (6155.2383, 4381.9355, 2266.508), (8.530514527319285, 63.87350705378629, 178.9133066701186), (1.0, 1.0, 0.538012), "PWM_Quarry_4x3x10_A630", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (6099.2817, 4668.986, 2082.1062), (-8.545074244814428, -102.36503800477712, 179.03350981549434), (1.0, 1.0, 0.62215525), "PWM_Quarry_4x3x10_A631", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5061.073, 4825.3174, 2026.0752), (12.453461300195919, 107.9401271671563, -175.90094325037958), (1.0, 1.0, 0.76543075), "PWM_Quarry_4x3x10_A632", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3110.964, 3419.714, 1437.8937), (-0.7894588984168838, -125.92003802713184, 177.32714494075955), (0.80334425, 0.93834406, 0.35443017), "PWM_Quarry_4x3x10_A633", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3224.107, 3548.708, 837.63245), (-0.7894589320998486, -109.33323942621247, 177.3271448554269), (0.803344, 0.961742, 0.35443), "PWM_Quarry_4x3x10_A634", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3296.4907, 3447.8364, 1186.8827), (-0.7952270828910437, 15.683472762641628, 2.6808476205562957), (0.803344, 0.97939205, 0.5872259), "PWM_Quarry_4x3x10_A635", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3207.3528, 3361.7456, 1186.8827), (-0.7951964168618302, 29.679710375972455, 2.6808471840268853), (0.803344, 0.938344, 0.587226), "PWM_Quarry_4x3x10_A636", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3479.5225, 3530.8896, 2145.628), (-2.37133799625905, 32.7485962914908, -178.48778665187214), (1.0, 1.0, 0.62877995), "PWM_Quarry_4x3x10_A637", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3395.7493, 3477.859, 1186.8827), (-0.795196323637925, -36.34887742998395, 2.6808470049777284), (0.803344, 0.938344, 0.587226), "PWM_Quarry_4x3x10_A638", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (6274.816, 1705.0088, 2269.7104), (-6.810759997744214, 50.9733822527826, -177.2481251578507), (1.0, 1.0, 0.809593), "PWM_Quarry_4x3x10_A639", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (6100.9463, 1466.2002, 2286.184), (-6.810729542383281, 28.71044517502245, -177.248125196755), (1.0492203, 1.0313581, 0.809593), "PWM_Quarry_4x3x10_A640", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (6166.5923, 1696.1946, 2318.5923), (-6.810697987936898, 86.30558538891233, -177.24812518684377), (1.0, 1.0, 0.809593), "PWM_Quarry_4x3x10_A641", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (6281.7075, 1312.9414, 2300.2695), (-6.810697987936898, 86.30558538891233, -177.24812518684377), (1.8267998, 1.0, 0.809593), "PWM_Quarry_4x3x10_A642", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5887.3145, 1180.7412, 2036.1572), (-15.645386142315013, 89.24070230826547, 176.9466002708654), (1.0, 1.0, 0.716295), "PWM_Quarry_4x3x10_A643", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4753.467, 1389.6615, 2007.0713), (-15.645295789787435, 89.24075619984296, 175.51141132994982), (1.0, 1.0522836, 0.716295), "PWM_Quarry_4x3x10_A644", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4441.51, 2537.024, 2478.7437), (5.321249865661446, 150.15128292175723, 175.39410480919938), (1.0, 1.0, 0.716295), "PWM_Quarry_4x3x10_A645", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4457.0947, 2757.1921, 2591.5315), (-2.9088137343456606, -54.214474769006635, -173.18285963798525), (1.0, 1.0, 0.716295), "PWM_Quarry_4x3x10_A646", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4119.8164, 3447.5522, 2628.0706), (-2.9088137343456606, -54.214474769006635, -173.18285963798525), (1.0, 1.0, 0.716295), "PWM_Quarry_4x3x10_A647", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3761.8835, 1962.1777, 2260.232), (1.3671578973394287, -109.79494813294544, 177.9849213509377), (1.0, 1.0, 0.716295), "PWM_Quarry_4x3x10_A648", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3279.1304, 3037.6016, 2147.888), (2.459557593366289, 83.24282473004008, -177.8543682147157), (1.109711, 1.1322955, 0.55752236), "PWM_Quarry_4x3x10_A649", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3018.7585, 2866.032, 2178.7688), (-4.264099548652677, -43.70579040219583, 178.93114895489748), (1.1750474, 1.2172207, 0.538012), "PWM_Quarry_4x3x10_A650", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3389.0498, 2906.934, 2361.7905), (-4.264099484894705, -117.72027544166276, 178.93114860304632), (1.1004206, 1.09624, 0.5721786), "PWM_Quarry_4x3x10_A651", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2560.0981, 2448.3774, 2010.8839), (-4.264099548652677, -43.70579040219583, 178.93114895489748), (1.066254, 1.09624, 0.538012), "PWM_Quarry_4x3x10_A652", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3936.5322, 1457.1903, 1565.6957), (2.6342269349348935, 8.61532523439416, 2.016601640556939), (1.0, 1.0, 0.32684517), "PWM_Quarry_4x3x10_A653", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3034.1265, 5421.9976, 1089.8567), (-9.684784153257116, 64.05770473437971, 2.7991635134814343), (1.0, 1.0, 0.705696), "PWM_Quarry_4x3x10_A654", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3464.3428, 5315.284, 1054.628), (-3.9169607602205576, 86.99834384964997, 1.2971496593979452), (1.0, 1.0, 0.8125), "PWM_Quarry_4x3x10_A655", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3256.7036, 5337.3887, 1054.628), (-8.941222796312262, -74.30590486097539, -0.11526540387279678), (1.0, 1.0, 0.8125), "PWM_Quarry_4x3x10_A656", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3499.724, 5173.6562, 728.4939), (-3.916961190588663, 30.735230886531163, 1.2971495892995688), (1.0, 1.0, 0.375), "PWM_Quarry_4x3x10_A657", _folder)
if a: placed += 1
else: skipped += 1

# Batch 20: StaticMesh'PWM_Quarry_Floor_8x8x8_A' (1 instances)
_mesh_path = "/Game/Unshippable/Whitebox/Rocks/Meshes/PWM_Quarry_Floor_8x8x8_A"
_materials = ['/Game/Art/Assets/Landmarks/CrystalDescent/Materials/Rock_Materials/ProcMaterial_Quarry_8m_Nordic']
_folder = "Reconstruction/BD_BB_TrollCave_AllInterfaces/Meshes"
a = spawn_static_mesh(_mesh_path, _materials, (3235.699, 5950.788, 391.10855), (0.2642979607656437, -175.2498818916431, -4.092803827883999), (1.0, 1.0, 1.0), "PWM_Nordic_8x8x8_A36", _folder)
if a: placed += 1
else: skipped += 1

# ======================================================================
# PHASE 2: ConstructionCatalog  (construction blocks)
# ======================================================================
unreal.log(f"[{BUBBLE_NAME}] Phase 2: Placing construction blocks...")

# Construction blocks use DecoVolume transforms (matched by Name)
_folder = "Reconstruction/BD_BB_TrollCave_AllInterfaces/Construction"

# Construction: AB_Orc_Scaffolding_Platform_3x1_No_Legs_2
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Scaffolding
#   Volume: EMorSimpleShape::OrientedBox, BoxExtent: (145.3, 169.3, 60.2)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (5620.6416, 1121.1648, 793.51044), (0.0, 0.0, -0.0), (2.9056, 3.3854, 1.2040), "AB_Orc_Scaffolding_Platform_3x1_No_Legs_2", _folder)
if a: placed += 1
else: skipped += 1

# Construction: AB_Orc_Scaffolding_Platform_3x1_No_Legs2_5
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Scaffolding
#   Volume: EMorSimpleShape::OrientedBox, BoxExtent: (96.8, 162.1, 81.9)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (4977.41, 1453.0205, 715.1919), (0.0, 0.0, -0.0), (1.9350, 3.2424, 1.6371), "AB_Orc_Scaffolding_Platform_3x1_No_Legs2_5", _folder)
if a: placed += 1
else: skipped += 1

# Construction: AB_Orc_Scaffolding_Platform_3x1_No_Legs3_8
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Scaffolding
#   Volume: EMorSimpleShape::OrientedBox, BoxExtent: (94.1, 159.7, 65.5)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (2674.3337, 3559.947, 658.97424), (0.0, 0.0, -0.0), (1.8828, 3.1933, 1.3091), "AB_Orc_Scaffolding_Platform_3x1_No_Legs3_8", _folder)
if a: placed += 1
else: skipped += 1

# Construction: AB_Orc_Scaffolding_Platform_3x3_No_Legs_2
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Stone
#   Volume: EMorSimpleShape::OrientedBox, BoxExtent: (247.3, 253.2, 95.2)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (5358.408, 1117.3102, 761.9442), (0.0, 0.0, -0.0), (4.9470, 5.0639, 1.9036), "AB_Orc_Scaffolding_Platform_3x3_No_Legs_2", _folder)
if a: placed += 1
else: skipped += 1

# Construction: AB_Orc_Scaffolding_Platform_3x3_No_Legs2_2
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Stone
#   Volume: EMorSimpleShape::OrientedBox, BoxExtent: (247.1, 260.1, 30.7)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (2733.918, 2375.5862, 626.13885), (0.0, 0.0, -0.0), (4.9423, 5.2024, 0.6147), "AB_Orc_Scaffolding_Platform_3x3_No_Legs2_2", _folder)
if a: placed += 1
else: skipped += 1

# Construction: AB_Orc_Scaffolding_Platform_3x3_No_Legs3_7
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Stone
#   Volume: EMorSimpleShape::OrientedBox, BoxExtent: (245.4, 206.5, 26.3)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (2428.6458, 2999.6216, 636.681), (0.0, 0.0, -0.0), (4.9077, 4.1292, 0.5252), "AB_Orc_Scaffolding_Platform_3x3_No_Legs3_7", _folder)
if a: placed += 1
else: skipped += 1

# Construction: Orc_Palissade_Wall_3X1M_A_2
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Scaffolding
#   Volume: EMorSimpleShape::OrientedBox, BoxExtent: (190.5, 165.3, 77.3)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (4797.6167, 1833.4172, 689.4656), (0.0, 0.0, -0.0), (3.8104, 3.3063, 1.5465), "Orc_Palissade_Wall_3X1M_A_2", _folder)
if a: placed += 1
else: skipped += 1

# Construction: Orc_Palissade_Wall_3X1M_A3_2
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Scaffolding
#   Volume: EMorSimpleShape::OrientedBox, BoxExtent: (178.1, 138.4, 55.5)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (3167.8794, 3814.854, 668.84515), (0.0, 0.0, -0.0), (3.5618, 2.7687, 1.1100), "Orc_Palissade_Wall_3X1M_A3_2", _folder)
if a: placed += 1
else: skipped += 1

# Construction: Orc_Palissade_Wall_3X1M_A4_5
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Scaffolding
#   Volume: EMorSimpleShape::OrientedBox, BoxExtent: (194.6, 174.7, 54.1)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (3641.4343, 4600.353, 610.725), (0.0, 0.0, -0.0), (3.8925, 3.4945, 1.0814), "Orc_Palissade_Wall_3X1M_A4_5", _folder)
if a: placed += 1
else: skipped += 1

# Construction: Orc_Palissade_Wall_3X1M_A5
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Scaffolding
#   Volume: EMorSimpleShape::OrientedBox, BoxExtent: (153.2, 185.6, 88.6)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (3027.9053, 2793.3418, 660.6923), (0.0, 0.0, -0.0), (3.0637, 3.7111, 1.7727), "Orc_Palissade_Wall_3X1M_A5", _folder)
if a: placed += 1
else: skipped += 1

# Construction: Orc_Palissade_Wall_3X3M_C_2
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Scaffolding
#   Volume: EMorSimpleShape::OrientedBox, BoxExtent: (209.6, 162.7, 204.9)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (2609.9575, 2265.9062, 738.89246), (0.0, 0.0, -0.0), (4.1920, 3.2537, 4.0990), "Orc_Palissade_Wall_3X3M_C_2", _folder)
if a: placed += 1
else: skipped += 1

# Construction: Orc_Palissade_Wall_3X3M_C2_5
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Scaffolding
#   Volume: EMorSimpleShape::OrientedBox, BoxExtent: (209.8, 221.3, 174.4)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (3093.0156, 4671.2266, 738.09644), (0.0, 0.0, -0.0), (4.1969, 4.4260, 3.4890), "Orc_Palissade_Wall_3X3M_C2_5", _folder)
if a: placed += 1
else: skipped += 1

# Construction: Orc_Palissade_Wall_3X3M_C3
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Scaffolding
#   Volume: EMorSimpleShape::OrientedBox, BoxExtent: (230.2, 230.2, 145.7)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (3216.9429, 2787.9236, 715.2721), (0.0, 0.0, -0.0), (4.6031, 4.6041, 2.9139), "Orc_Palissade_Wall_3X3M_C3", _folder)
if a: placed += 1
else: skipped += 1

# Construction: Orc_Scaffolding_Beam_3m_5
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Scaffolding
#   Volume: EMorSimpleShape::OrientedBox, BoxExtent: (167.1, 161.8, 42.6)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (3336.0398, 4668.438, 639.86957), (0.0, 0.0, -0.0), (3.3427, 3.2354, 0.8521), "Orc_Scaffolding_Beam_3m_5", _folder)
if a: placed += 1
else: skipped += 1

# Construction: Orc_Scaffolding_Beam_3m2_8
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Scaffolding
#   Volume: EMorSimpleShape::OrientedBox, BoxExtent: (174.9, 115.2, 59.4)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (4099.3726, 2098.2227, 690.0794), (0.0, 0.0, -0.0), (3.4978, 2.3050, 1.1871), "Orc_Scaffolding_Beam_3m2_8", _folder)
if a: placed += 1
else: skipped += 1

# Construction: Orc_Scaffolding_Ladder2_2
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Scaffolding
#   Volume: EMorSimpleShape::OrientedBox, BoxExtent: (102.8, 151.0, 199.2)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (3577.9333, 3746.9993, 775.29254), (0.0, 0.0, -0.0), (2.0566, 3.0200, 3.9848), "Orc_Scaffolding_Ladder2_2", _folder)
if a: placed += 1
else: skipped += 1

# ======================================================================
# PHASE 3: Breakables + DecoVolumes
# ======================================================================
unreal.log(f"[{BUBBLE_NAME}] Phase 3: Placing breakables and deco volumes...")

_folder = "Reconstruction/BD_BB_TrollCave_AllInterfaces/Breakables"

# Breakable Batch 0: BP_Orc_Scaffolding_Post_1m_A (6 instances)
#   BP Class: /Game/LevelDesign/Architecture/Orc/BP_Orc_Scaffolding_Post_1m_A
_brk_mesh = "/Game/Art/Assets/Kits/Deco_Architecture/Orc_Camp/Orc_Scaffolding_Post_1m_A"
_brk_mats = ['/Game/Art/Assets/Kits/Deco_Architecture/Orc_Camp/Materials/MI_Orc_Scaffolding_Poles']
a = spawn_static_mesh(_brk_mesh, _brk_mats, (5682.132, 4332.671, 790.7196), (1.1034588594785446, 75.27482899704503, 91.90855844319965), (1.0, 1.0, 1.0), "BP_Orc_Scaffolding_Post_1m_A_2", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_brk_mesh, _brk_mats, (5937.422, 4274.057, 799.2084), (7.2150300346995975, -115.68417460707857, -96.55566736403425), (1.0, 1.0, 1.0), "BP_Orc_Scaffolding_Post_1m_A2", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_brk_mesh, _brk_mats, (5598.0, 4388.923, 787.11426), (0.0, 0.0, 87.18745651312373), (1.0, 1.0, 1.0), "BP_Orc_Scaffolding_Post_1m_A3_8", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_brk_mesh, _brk_mats, (3454.868, 3830.6099, 643.12354), (-0.8498540682793516, 72.60944368152926, -74.74053935822894), (1.0, 1.0, 1.0), "BP_Orc_Scaffolding_Post_1m_A4_6", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_brk_mesh, _brk_mats, (4210.4985, 2200.9329, 678.0729), (2.8252683926751994, 133.5795248327919, -90.17061787329715), (1.0, 1.0, 1.0), "BP_Orc_Scaffolding_Post_1m_A5_9", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_brk_mesh, _brk_mats, (2275.868, 3341.0193, 646.796), (-6.473820810145692e-07, 37.164594765713275, -90.99362848905702), (1.0, 1.0, 1.0), "BP_Orc_Scaffolding_Post_1m_A6_12", _folder)
if a: placed += 1
else: skipped += 1

# Breakable Batch 1: BP_Orc_Scaffolding_Post_1m_C (3 instances)
#   BP Class: /Game/LevelDesign/Architecture/Orc/BP_Orc_Scaffolding_Post_1m_C
_brk_mesh = "/Game/Art/Assets/Kits/Deco_Architecture/Orc_Camp/Orc_Scaffolding_Post_1m_C"
_brk_mats = ['/Game/Art/Assets/Kits/Deco_Architecture/Orc_Camp/Materials/MI_Orc_Scaffolding_Poles']
a = spawn_static_mesh(_brk_mesh, _brk_mats, (3559.5427, 3848.5015, 636.3123), (-7.155211271607925, -130.23302153198168, -86.12262060687706), (1.0, 1.0, 1.0), "BP_Orc_Scaffolding_Post_1m_C_2", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_brk_mesh, _brk_mats, (5549.336, 4476.2007, 778.0264), (3.893339710642693e-06, -59.06118730964057, 81.56235157915393), (1.0, 1.0, 1.0), "BP_Orc_Scaffolding_Post_1m_C2_5", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_brk_mesh, _brk_mats, (2316.8171, 3457.0537, 647.59576), (0.5811874998468479, 125.26844487655464, -91.84967095112822), (1.0, 1.0, 1.0), "BP_Orc_Scaffolding_Post_1m_C3_5", _folder)
if a: placed += 1
else: skipped += 1

# Breakable Batch 2: BP_Orc_Scaffolding_Post_1m_D (9 instances)
#   BP Class: /Game/LevelDesign/Architecture/Orc/BP_Orc_Scaffolding_Post_1m_D
_brk_mesh = "/Game/Art/Assets/Kits/Deco_Architecture/Orc_Camp/Orc_Scaffolding_Post_1m_D"
_brk_mats = ['/Game/Art/Assets/Kits/Deco_Architecture/Orc_Camp/Materials/MI_Orc_Scaffolding_Poles']
a = spawn_static_mesh(_brk_mesh, _brk_mats, (4917.826, 1881.6259, 670.3337), (84.03973185660418, 79.28448613248759, 149.27893920320727), (1.0, 1.0, 1.0), "BP_Orc_Scaffolding_Post_1m_D_2", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_brk_mesh, _brk_mats, (1028.3018, 3269.7517, 726.39636), (-86.5384220418474, -179.9999590186681, -179.9999590186681), (1.0, 1.0, 1.0), "BP_Orc_Scaffolding_Post_1m_D10", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_brk_mesh, _brk_mats, (4867.8857, 1943.5527, 663.03564), (82.38495475274905, 129.78272845979063, 136.48201199027375), (1.0, 1.0, 1.0), "BP_Orc_Scaffolding_Post_1m_D2", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_brk_mesh, _brk_mats, (4773.17, 2028.6248, 655.68646), (89.0549389309124, -16.400784243156853, 99.96937964547695), (1.0, 1.0, 1.0), "BP_Orc_Scaffolding_Post_1m_D4", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_brk_mesh, _brk_mats, (4097.4375, 2180.8596, 669.62354), (-85.92925549207095, -7.89073593393339e-12, 7.629490265767431e-05), (1.0, 1.0, 1.0), "BP_Orc_Scaffolding_Post_1m_D5_8", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_brk_mesh, _brk_mats, (1252.3967, 2788.7034, 695.8093), (-86.53885545361705, -179.99998633955465, -179.99995901861385), (1.0, 1.0, 1.0), "BP_Orc_Scaffolding_Post_1m_D6_11", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_brk_mesh, _brk_mats, (1139.3851, 2888.217, 713.66235), (-80.39878151674804, 141.77141473744308, -179.9998192832025), (1.0, 1.0, 1.0), "BP_Orc_Scaffolding_Post_1m_D7", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_brk_mesh, _brk_mats, (2330.3806, 3230.8674, 637.93744), (-88.2129327327501, -118.59155609633254, 179.99803832831518), (1.0, 1.0, 1.0), "BP_Orc_Scaffolding_Post_1m_D8_15", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_brk_mesh, _brk_mats, (2375.294, 3154.7285, 635.6937), (-88.204514335765, 133.22502802758368, 179.99864567601702), (1.0, 1.0, 1.0), "BP_Orc_Scaffolding_Post_1m_D9", _folder)
if a: placed += 1
else: skipped += 1

# Breakable Batch 3: BP_Orc_Scaffolding_Post_2m_A (3 instances)
#   BP Class: /Game/LevelDesign/Architecture/Orc/BP_Orc_Scaffolding_Post_2m_A
_brk_mesh = "/Game/Art/Assets/Kits/Deco_Architecture/Orc_Camp/Orc_Scaffolding_Post_2m_A"
_brk_mats = ['/Game/Art/Assets/Kits/Deco_Architecture/Orc_Camp/Materials/MI_Orc_Scaffolding_Poles']
a = spawn_static_mesh(_brk_mesh, _brk_mats, (6084.7373, 4451.742, 801.4176), (84.19685376869893, -42.959468447207364, -89.7189697099401), (1.0, 1.0, 1.0), "BP_Orc_Scaffolding_Post_2m_A_2", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_brk_mesh, _brk_mats, (3534.6404, 3868.335, 640.76514), (89.51525314108733, -179.99998474127395, -179.99998474127395), (1.0, 1.0, 1.0), "BP_Orc_Scaffolding_Post_2m_A2_8", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_brk_mesh, _brk_mats, (3479.499, 4623.4634, 622.2105), (89.03238270077274, -14.627089590932082, -43.372439191059435), (1.0, 1.0, 1.0), "BP_Orc_Scaffolding_Post_2m_A3", _folder)
if a: placed += 1
else: skipped += 1

# Breakable Batch 4: BP_Orc_Scaffolding_Post_2m_D (3 instances)
#   BP Class: /Game/LevelDesign/Architecture/Orc/BP_Orc_Scaffolding_Post_2m_D
_brk_mesh = "/Game/Art/Assets/Kits/Deco_Architecture/Orc_Camp/Orc_Scaffolding_Post_2m_D"
_brk_mats = ['/Game/Art/Assets/Kits/Deco_Architecture/Orc_Camp/Materials/MI_Orc_Scaffolding_Poles']
a = spawn_static_mesh(_brk_mesh, _brk_mats, (5241.743, 4608.7715, 722.3545), (-63.235588431309445, -54.32155901598364, 57.336648244962774), (1.0, 1.0, 1.0), "BP_Orc_Scaffolding_Post_2m_D_2", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_brk_mesh, _brk_mats, (2554.5598, 3103.0718, 627.7627), (-82.71539712823389, -7.476471438733279, -49.92620112033876), (1.0, 1.0, 1.0), "BP_Orc_Scaffolding_Post_2m_D2_5", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_brk_mesh, _brk_mats, (3095.2734, 2629.312, 624.1576), (-82.71508583994907, -155.20742882671942, -49.92656523950036), (1.0, 1.0, 1.0), "BP_Orc_Scaffolding_Post_2m_D3", _folder)
if a: placed += 1
else: skipped += 1

# Breakable Batch 5: BP_Orc_Scaffolding_Post_3m_B (3 instances)
#   BP Class: /Game/LevelDesign/Architecture/Orc/BP_Orc_Scaffolding_Post_3m_B
_brk_mesh = "/Game/Art/Assets/Kits/Deco_Architecture/Orc_Camp/Orc_Scaffolding_Post_3m_B"
_brk_mats = ['/Game/Art/Assets/Kits/Deco_Architecture/Orc_Camp/Materials/MI_Orc_Scaffolding_Poles']
a = spawn_static_mesh(_brk_mesh, _brk_mats, (4691.2827, 2007.7882, 647.3256), (-17.86633461039263, -61.87366019104451, -33.237213169875474), (1.0, 1.0, 1.0), "BP_Orc_Scaffolding_Post_3m_B_2", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_brk_mesh, _brk_mats, (5694.0, 4426.0, 792.0), (0.0, 0.0, 87.18743754883175), (1.0, 1.0, 1.0), "BP_Orc_Scaffolding_Post_3m_B3_8", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_brk_mesh, _brk_mats, (5602.4165, 4426.823, 779.1225), (-56.24975713836975, 1.0356331562706875e-05, 14.062731241158309), (1.0, 1.0, 1.0), "BP_Orc_Scaffolding_Post_3m_B4_11", _folder)
if a: placed += 1
else: skipped += 1

# Breakable Batch 6: BP_Orc_Scaffolding_Post_3m_C (2 instances)
#   BP Class: /Game/LevelDesign/Architecture/Orc/BP_Orc_Scaffolding_Post_3m_C
_brk_mesh = "/Game/Art/Assets/Kits/Deco_Architecture/Orc_Camp/Orc_Scaffolding_Post_3m_C"
_brk_mats = ['/Game/Art/Assets/Kits/Deco_Architecture/Orc_Camp/Materials/MI_Orc_Scaffolding_Poles']
a = spawn_static_mesh(_brk_mesh, _brk_mats, (5168.2847, 1435.339, 673.742), (-30.155703990240802, -119.53434173847005, -63.31862788027742), (1.0, 1.0, 1.0), "BP_Orc_Scaffolding_Post_3m_C_2", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_brk_mesh, _brk_mats, (5364.076, 4631.2646, 735.7148), (-46.51102192602662, 91.60507359232206, 16.578139085788077), (1.0, 1.0, 1.0), "BP_Orc_Scaffolding_Post_3m_C4_11", _folder)
if a: placed += 1
else: skipped += 1

# Breakable Batch 7: BP_Orc_Scaffolding_Post_3m_d (5 instances)
#   BP Class: /Game/LevelDesign/Architecture/Orc/BP_Orc_Scaffolding_Post_3m_d
_brk_mesh = "/Game/Art/Assets/Kits/Deco_Architecture/Orc_Camp/Orc_Scaffolding_Post_3m_D"
_brk_mats = ['/Game/Art/Assets/Kits/Deco_Architecture/Orc_Camp/Materials/MI_Orc_Scaffolding_Poles']
a = spawn_static_mesh(_brk_mesh, _brk_mats, (4571.049, 2320.6707, 318.1883), (12.483591132857741, -19.81631559061709, -28.38168247366306), (1.0, 1.0, 1.0), "BP_Orc_Scaffolding_Post_3m_D_2", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_brk_mesh, _brk_mats, (2198.2927, 2313.0828, 651.00964), (9.926102389198633, -119.27261235521875, -80.90353082421719), (1.0, 1.0, 1.0), "BP_Orc_Scaffolding_Post_3m_D2_2", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_brk_mesh, _brk_mats, (5216.7866, 4508.3, 728.5372), (-5.387542690521911, 6.849169649576474, 82.45974407899794), (1.0, 1.0, 1.0), "BP_Orc_Scaffolding_Post_3m_D3_8", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_brk_mesh, _brk_mats, (4247.903, 2073.468, 671.7157), (0.0, 0.0, -62.424890458868845), (1.0, 1.0, 1.0), "BP_Orc_Scaffolding_Post_3m_D4_5", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_brk_mesh, _brk_mats, (1025.0415, 2845.9263, 730.36774), (-1.2420070373418228, -37.3222061452327, -49.102820035671826), (1.0, 1.0, 1.0), "BP_Orc_Scaffolding_Post_3m_D5_8", _folder)
if a: placed += 1
else: skipped += 1

# Breakable Batch 8: BP_Orc_Scaffolding_Post_4m_A (3 instances)
#   BP Class: /Game/LevelDesign/Architecture/Orc/BP_Orc_Scaffolding_Post_4m_A
_brk_mesh = "/Game/Art/Assets/Kits/Deco_Architecture/Orc_Camp/Orc_Scaffolding_Post_4m_A"
_brk_mats = ['/Game/Art/Assets/Kits/Deco_Architecture/Orc_Camp/Materials/MI_Orc_Scaffolding_Poles']
a = spawn_static_mesh(_brk_mesh, _brk_mats, (5655.9204, 1229.2739, 759.6913), (-8.350096952680408, -4.014831910774763, -26.064389429232072), (1.0, 1.0, 1.0), "BP_Orc_Scaffolding_Post_4m_A_2", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_brk_mesh, _brk_mats, (4100.401, 2782.6772, 664.29126), (88.68321168181524, -155.28633159906772, -179.99949797775605), (1.0, 1.0, 1.0), "BP_Orc_Scaffolding_Post_4m_A2_2", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_brk_mesh, _brk_mats, (1232.045, 3291.02, 704.9765), (-87.84631247648093, -155.0563461885474, -171.56917077654523), (1.0, 1.0, 1.0), "BP_Orc_Scaffolding_Post_4m_A3_5", _folder)
if a: placed += 1
else: skipped += 1

# Breakable Batch 9: BP_Orc_Scaffolding_Post_4m_B (2 instances)
#   BP Class: /Game/LevelDesign/Architecture/Orc/BP_Orc_Scaffolding_Post_4m_B
_brk_mesh = "/Game/Art/Assets/Kits/Deco_Architecture/Orc_Camp/Orc_Scaffolding_Post_4m_B"
_brk_mats = ['/Game/Art/Assets/Kits/Deco_Architecture/Orc_Camp/Materials/MI_Orc_Scaffolding_Poles']
a = spawn_static_mesh(_brk_mesh, _brk_mats, (5661.19, 1243.0093, 761.91754), (-14.029663164150257, 22.183480464549387, -29.16803118389303), (1.0, 1.0, 1.0), "BP_Orc_Scaffolding_Post_4m_B_2", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_brk_mesh, _brk_mats, (1069.3031, 3353.4287, 739.2443), (0.0, 0.0, 38.28722936888577), (1.0, 1.0, 1.0), "BP_Orc_Scaffolding_Post_4m_B2_2", _folder)
if a: placed += 1
else: skipped += 1

# Breakable Batch 10: BP_Orc_Scaffolding_Post_5m_D (3 instances)
#   BP Class: /Game/LevelDesign/Architecture/Orc/BP_Orc_Scaffolding_Post_5m_D
_brk_mesh = "/Game/Art/Assets/Kits/Deco_Architecture/Orc_Camp/Orc_Scaffolding_Post_5m_D"
_brk_mats = ['/Game/Art/Assets/Kits/Deco_Architecture/Orc_Camp/Materials/MI_Orc_Scaffolding_Poles']
a = spawn_static_mesh(_brk_mesh, _brk_mats, (4511.58, 2110.2847, 580.6917), (15.172385542504609, 174.15071349195367, 37.62488512162004), (1.0, 1.0, 1.0), "BP_Orc_Scaffolding_Post_5m_D_2", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_brk_mesh, _brk_mats, (3794.8416, 3809.8499, 641.14844), (-1.034588447059388e-06, -38.346402126451956, -35.31039279004616), (1.0, 1.0, 1.0), "BP_Orc_Scaffolding_Post_5m_D2_2", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_brk_mesh, _brk_mats, (2476.8755, 3138.6492, 618.0886), (-37.51745554053113, -50.68032752523696, 52.26918624984545), (1.0, 1.0, 1.0), "BP_Orc_Scaffolding_Post_5m_D4_11", _folder)
if a: placed += 1
else: skipped += 1

# Breakable Batch 11: BP_DM_Deco_Orc_Banner_2x2_B_Breakable (1 instances)
#   BP Class: /Game/LevelDesign/Deco/GoblinWarren/BP_DM_Deco_Orc_Banner_2x2_B_Breakable
_brk_mesh = "/Game/Art/Assets/Kits/Deco/Orc/Effigy_A"
_brk_mats = ['/Game/Art/Assets/Kits/Deco/Orc/Materials/Orc_Lighting/MI_Orc_Lighting', '/Game/Art/Assets/Kits/Deco_Architecture/Orc_Camp/Materials/MI_Orc_Scaffolding_Platforms']
a = spawn_static_mesh(_brk_mesh, _brk_mats, (2754.6907, 3337.625, 752.2767), (0.0, -85.19292595510277, 0.0), (1.0, 1.0, 1.0), "BP_DM_Deco_Orc_Banner_2x2_B_Breakable_5", _folder)
if a: placed += 1
else: skipped += 1

# Breakable Batch 12: BP_DM_Mines_Lift_Prop_horizontal_broken_Breakable (1 instances)
#   BP Class: /Game/LevelDesign/Deco/MinesDressing/BP_DM_Mines_Lift_Prop_horizontal_broken_Breakable
_brk_mesh = "/Game/Art/Assets/Kits/Deco/Mines/Machine/Mines_Machine_Lift_Pieces/Mines_Lift_Prop_horizontal_broken"
_brk_mats = ['/Game/Art/Assets/Kits/Deco/Mines/Machine/Mines_Machine_Lift_Pieces/Materials/Mi_Mines_Machine_Lift_L']
a = spawn_static_mesh(_brk_mesh, _brk_mats, (5639.768, 1285.3312, 755.2634), (15.982507000408848, -0.5265197971556312, -2.9115906459378533), (1.0, 1.0, 1.0), "BP_DM_Mines_Lift_Prop_horizontal_broken_Breakable_2", _folder)
if a: placed += 1
else: skipped += 1

# Breakable Batch 13: BP_DM_Mines_Wagon_Broken_B (1 instances)
#   BP Class: /Game/LevelDesign/Deco/MinesDressing/BP_DM_Mines_Wagon_Broken_B
_brk_mesh = "/Game/Art/Assets/Kits/Deco/Mines/Mines_Wagon_Broken_B"
_brk_mats = ['/Game/Art/Assets/Kits/Deco/Mines/Materials/Mines_WagonCart/MI_Mines_WagonCart_Trim', '/Game/Art/Assets/Kits/Deco/Mines/Materials/Mines_WagonCart/MI_Mines_WagonCart']
a = spawn_static_mesh(_brk_mesh, _brk_mats, (1433.8179, 3688.4114, 690.1936), (-0.8114319274756766, 110.86199840334088, 2.7363201423195873), (1.0, 1.0, 1.0), "BP_DM_Mines_Wagon_Broken_B_2", _folder)
if a: placed += 1
else: skipped += 1

# Breakable Batch 14: BP_DM_Orc_Shanty_Midden_C_B_Breakable (2 instances)
#   BP Class: /Game/LevelDesign/Deco/Orc_Shanty/BP_DM_Orc_Shanty_Midden_C_B_Breakable
_brk_mesh = "/Game/Art/Assets/Kits/Deco/Orc/Shanty/Orc_Shanty_Midden_C_B"
_brk_mats = ['/Game/Art/Assets/Kits/Deco/Orc/Shanty/Material/Orc_Shanty_Midden/MI_Orc_Shanty_Midden_Mat_Inst', '/Game/Art/Assets/Kits/Deco/Orc/Shanty/Material/Orc_Shanty_Midden/MI_Orc_Shanty_Midden_Tileable_C_Mat_Inst']
a = spawn_static_mesh(_brk_mesh, _brk_mats, (2008.2561, 2401.0664, 653.81415), (1.9725634808331027, -58.785805356214134, 4.625149748210923), (1.0, 1.0, 1.0), "BP_DM_Orc_Shanty_Midden_C_B_Breakable_5", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_brk_mesh, _brk_mats, (2496.9468, 3286.6797, 632.5875), (0.0, 0.0, -0.0), (1.0, 1.0, 1.0), "BP_DM_Orc_Shanty_Midden_C_B_Breakable2_8", _folder)
if a: placed += 1
else: skipped += 1

# Breakable Batch 15: BP_DM_Orc_Shanty_Midden_C_C_Breakable (2 instances)
#   BP Class: /Game/LevelDesign/Deco/Orc_Shanty/BP_DM_Orc_Shanty_Midden_C_C_Breakable
_brk_mesh = "/Game/Art/Assets/Kits/Deco/Orc/Shanty/Orc_Shanty_Midden_C_C"
_brk_mats = ['/Game/Art/Assets/Kits/Deco/Orc/Shanty/Material/Orc_Shanty_Midden/MI_Orc_Shanty_Midden_Mat_Inst', '/Game/Art/Assets/Kits/Deco/Orc/Shanty/Material/Orc_Shanty_Midden/MI_Orc_Shanty_Midden_Tileable_C_Mat_Inst']
a = spawn_static_mesh(_brk_mesh, _brk_mats, (2067.1306, 2327.44, 653.82245), (0.5344147761154598, -58.90234287041695, 4.622574582552526), (1.0, 1.0, 1.0), "BP_DM_Orc_Shanty_Midden_C_C_Breakable_5", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_brk_mesh, _brk_mats, (2520.4553, 3193.0845, 627.16565), (0.0, 0.0, -0.0), (1.0, 1.0, 1.0), "BP_DM_Orc_Shanty_Midden_C_C_Breakable2_8", _folder)
if a: placed += 1
else: skipped += 1

# Breakable Batch 16: BP_Orc_Remains_B (2 instances)
#   BP Class: /Game/LevelDesign/Deco/Warren-Tomb/Orc_Remains/BP_Orc_Remains_B
_brk_mesh = "/Game/Art/Assets/Kits/Deco/Warrens_Tomb/Orc_Remains/Orc_Remains_B"
_brk_mats = ['/Game/CharacterArt/Orcs/Gundabad/MI_Orc_Gundabad_Rusted_Inst', '/Game/CharacterArt/Uruks/RedEye/MI_UrukRedEye_Rusted_Inst', '/Game/CharacterArt/Orcs/Native/MI_OrcNative_Rusted_Inst', '/Game/CharacterArt/Goblins/Native/MI_Goblin_Native_Rusted_Inst']
a = spawn_static_mesh(_brk_mesh, _brk_mats, (5775.0, 1470.0, 785.0), (5.624994866963602, 0.0, -0.0), (1.0, 1.0, 1.0), "BP_Orc_Remains_B_2", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_brk_mesh, _brk_mats, (1443.9049, 3957.6494, 690.0), (0.0, 132.18758053980275, -0.0), (1.0, 1.0, 1.0), "BP_Orc_Remains_B2_5", _folder)
if a: placed += 1
else: skipped += 1

# --- Extra DecoVolumes (not construction blocks) ---
_folder = "Reconstruction/BD_BB_TrollCave_AllInterfaces/DecoVolumes"

# DecoVolume: AB_Orc_Scaffolding_Pallet_2x2m_A_2 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (5185.391, 4649.7607, 735.80994), (0.0, 0.0, -0.0), (3.2029, 3.1438, 0.8538), "DV_AB_Orc_Scaffolding_Pallet_2x2m_A_2_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: AB_Orc_Scaffolding_Pallet_2x2m_A2_2 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (2107.836, 2482.9314, 649.48755), (0.0, 0.0, -0.0), (3.1982, 3.2110, 0.5957), "DV_AB_Orc_Scaffolding_Pallet_2x2m_A2_2_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: AB_Orc_Scaffolding_Pallet_2x2m_A3 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (2534.332, 3414.0278, 670.6717), (0.0, 0.0, -0.0), (3.1346, 3.0529, 1.0063), "DV_AB_Orc_Scaffolding_Pallet_2x2m_A3_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: AB_Orc_Scaffolding_Pallet_2x2m_A4 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (1350.5105, 2661.7793, 684.6815), (0.0, 0.0, -0.0), (3.1294, 3.0655, 0.7922), "DV_AB_Orc_Scaffolding_Pallet_2x2m_A4_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: AB_Orc_Scaffolding_Pallet_2x2m_A5 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (1245.3074, 2619.9707, 735.1881), (0.0, 0.0, -0.0), (3.1417, 3.1419, 1.3292), "DV_AB_Orc_Scaffolding_Pallet_2x2m_A5_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: AB_Orc_Scaffolding_Pallet_2x2m_B_2 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (5030.161, 1856.2212, 673.00903), (0.0, 0.0, -0.0), (2.3490, 2.4931, 0.6628), "DV_AB_Orc_Scaffolding_Pallet_2x2m_B_2_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: AB_Orc_Scaffolding_Pallet_2x2m_B2_2 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (3085.9702, 4502.0293, 626.8235), (0.0, 0.0, -0.0), (2.3230, 2.4753, 0.4600), "DV_AB_Orc_Scaffolding_Pallet_2x2m_B2_2_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_DM_Deco_Orc_3x3_B_Breakable_2 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (5608.0396, 4613.4053, 829.14636), (0.0, 0.0, -0.0), (3.9895, 4.4288, 1.9026), "DV_BP_DM_Deco_Orc_3x3_B_Breakable_2_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_DM_Deco_Orc_3x3_B_Breakable2_5 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (5845.736, 1356.2882, 849.66516), (0.0, 0.0, -0.0), (4.4028, 4.0396, 2.0465), "DV_BP_DM_Deco_Orc_3x3_B_Breakable2_5_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_DM_Deco_Orc_3x3_B_Breakable3_2 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (5298.8784, 1417.1531, 744.4597), (0.0, 0.0, -0.0), (4.4352, 3.9857, 1.7947), "DV_BP_DM_Deco_Orc_3x3_B_Breakable3_2_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_DM_Deco_Orc_3x3_B_Breakable4_5 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (4372.355, 2150.2766, 721.05835), (0.0, 0.0, -0.0), (4.1180, 3.9456, 1.7873), "DV_BP_DM_Deco_Orc_3x3_B_Breakable4_5_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_DM_Deco_Orc_Banner_2x2_B_Breakable_5 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (2768.7844, 3327.4265, 883.8074), (0.0, 0.0, -0.0), (1.7098, 1.7193, 3.2667), "DV_BP_DM_Deco_Orc_Banner_2x2_B_Breakable_5_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_DM_Mines_Lift_Prop_horizontal_broken_Breakable_2 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (5563.285, 1320.6704, 748.5), (0.0, 0.0, -0.0), (1.8649, 2.3336, 0.9275), "DV_BP_DM_Mines_Lift_Prop_horizontal_broken_Breakable_2_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_DM_Mines_Wagon_Broken_B_2 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (1417.8196, 3720.1665, 717.3139), (0.0, 0.0, -0.0), (4.1033, 5.1386, 0.8127), "DV_BP_DM_Mines_Wagon_Broken_B_2_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_DM_Orc_Shanty_Midden_A_A_Breakable_2 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (4864.4536, 1656.4001, 672.2795), (0.0, 0.0, -0.0), (2.6174, 2.6422, 1.1782), "DV_BP_DM_Orc_Shanty_Midden_A_A_Breakable_2_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_DM_Orc_Shanty_Midden_A_A_Breakable2_11 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (5425.4688, 4775.9946, 775.55884), (0.0, 0.0, -0.0), (2.6090, 2.6282, 1.1059), "DV_BP_DM_Orc_Shanty_Midden_A_A_Breakable2_11_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_DM_Orc_Shanty_Midden_A_A_Breakable3_14 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (3541.6086, 4689.5166, 646.10876), (0.0, 0.0, -0.0), (2.5364, 2.5987, 0.6708), "DV_BP_DM_Orc_Shanty_Midden_A_A_Breakable3_14_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_DM_Orc_Shanty_Midden_A_A_Breakable4_17 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (992.6039, 3382.384, 767.5658), (0.0, 0.0, -0.0), (2.6943, 2.7525, 0.6708), "DV_BP_DM_Orc_Shanty_Midden_A_A_Breakable4_17_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_DM_Orc_Shanty_Midden_A_A_Breakable7_25 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (1151.5043, 3409.4048, 743.5399), (0.0, 0.0, -0.0), (2.7477, 2.7558, 0.9162), "DV_BP_DM_Orc_Shanty_Midden_A_A_Breakable7_25_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_DM_Orc_Shanty_Midden_A_B_Breakable_2 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (4947.1855, 1625.4424, 682.45795), (0.0, 0.0, -0.0), (2.2535, 2.3793, 0.8411), "DV_BP_DM_Orc_Shanty_Midden_A_B_Breakable_2_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_DM_Orc_Shanty_Midden_A_B_Breakable2_5 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (5961.7837, 1414.2356, 829.2555), (0.0, 0.0, -0.0), (3.2460, 3.1996, 0.7228), "DV_BP_DM_Orc_Shanty_Midden_A_B_Breakable2_5_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_DM_Orc_Shanty_Midden_A_B_Breakable3_8 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (6049.2417, 1419.4393, 835.63776), (0.0, 0.0, -0.0), (2.2051, 2.3645, 0.5886), "DV_BP_DM_Orc_Shanty_Midden_A_B_Breakable3_8_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_DM_Orc_Shanty_Midden_A_B_Breakable4_17 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (1246.8645, 3460.5842, 733.1723), (0.0, 0.0, -0.0), (3.0175, 3.0682, 0.9058), "DV_BP_DM_Orc_Shanty_Midden_A_B_Breakable4_17_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_DM_Orc_Shanty_Midden_A_B_Breakable5_14 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (5131.89, 4534.165, 722.43646), (0.0, 0.0, -0.0), (2.6887, 2.5889, 0.8121), "DV_BP_DM_Orc_Shanty_Midden_A_B_Breakable5_14_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_DM_Orc_Shanty_Midden_A_B_Breakable6_17 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (1132.6473, 2766.3284, 734.941), (0.0, 0.0, -0.0), (2.2567, 2.3645, 0.8291), "DV_BP_DM_Orc_Shanty_Midden_A_B_Breakable6_17_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_DM_Orc_Shanty_Midden_A_B_Breakable7_23 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (2344.4707, 2368.1086, 671.4679), (0.0, 0.0, -0.0), (2.2051, 2.3645, 0.5886), "DV_BP_DM_Orc_Shanty_Midden_A_B_Breakable7_23_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_DM_Orc_Shanty_Midden_A_B_Breakable8 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (2436.142, 2280.647, 646.6922), (0.0, 0.0, -0.0), (2.2051, 2.3811, 0.6593), "DV_BP_DM_Orc_Shanty_Midden_A_B_Breakable8_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_DM_Orc_Shanty_Midden_A_B_Breakable9 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (2461.4863, 2366.182, 652.6297), (0.0, 0.0, -0.0), (2.2542, 2.4051, 0.9336), "DV_BP_DM_Orc_Shanty_Midden_A_B_Breakable9_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_DM_Orc_Shanty_Midden_A_C_Breakable_2 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (4833.039, 1746.8062, 663.94293), (0.0, 0.0, -0.0), (1.6740, 1.8179, 0.5700), "DV_BP_DM_Orc_Shanty_Midden_A_C_Breakable_2_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_DM_Orc_Shanty_Midden_A_C_Breakable10_24 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (1203.9454, 3433.4873, 742.9316), (0.0, 0.0, -0.0), (1.6999, 1.8363, 0.7790), "DV_BP_DM_Orc_Shanty_Midden_A_C_Breakable10_24_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_DM_Orc_Shanty_Midden_A_C_Breakable11 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (1091.3351, 3345.3674, 740.1777), (0.0, 0.0, -0.0), (1.6998, 1.8363, 0.7790), "DV_BP_DM_Orc_Shanty_Midden_A_C_Breakable11_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_DM_Orc_Shanty_Midden_A_C_Breakable12 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (1064.1075, 2898.7227, 736.0802), (0.0, 0.0, -0.0), (1.6998, 1.8363, 0.7790), "DV_BP_DM_Orc_Shanty_Midden_A_C_Breakable12_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_DM_Orc_Shanty_Midden_A_C_Breakable13_29 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (2276.0842, 2348.5488, 666.9699), (0.0, 0.0, -0.0), (1.6573, 1.7930, 0.4328), "DV_BP_DM_Orc_Shanty_Midden_A_C_Breakable13_29_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_DM_Orc_Shanty_Midden_A_C_Breakable14_32 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (2417.8157, 2349.1301, 666.7531), (0.0, 0.0, -0.0), (1.6649, 1.7930, 0.4625), "DV_BP_DM_Orc_Shanty_Midden_A_C_Breakable14_32_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_DM_Orc_Shanty_Midden_A_C_Breakable15 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (2352.3413, 2478.847, 636.815), (0.0, 0.0, -0.0), (2.4400, 2.4468, 0.4625), "DV_BP_DM_Orc_Shanty_Midden_A_C_Breakable15_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_DM_Orc_Shanty_Midden_A_C_Breakable16 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (2566.7676, 2378.5386, 621.9819), (0.0, 0.0, -0.0), (2.4719, 2.4468, 0.7807), "DV_BP_DM_Orc_Shanty_Midden_A_C_Breakable16_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_DM_Orc_Shanty_Midden_A_C_Breakable17 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (2788.215, 2785.7625, 640.89496), (0.0, 0.0, -0.0), (2.4400, 2.4468, 0.4625), "DV_BP_DM_Orc_Shanty_Midden_A_C_Breakable17_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_DM_Orc_Shanty_Midden_A_C_Breakable2 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (5131.3867, 1495.8575, 685.8065), (0.0, 0.0, -0.0), (1.7092, 1.8208, 0.7646), "DV_BP_DM_Orc_Shanty_Midden_A_C_Breakable2_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_DM_Orc_Shanty_Midden_A_C_Breakable3_6 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (6223.9644, 1371.1647, 823.7969), (0.0, 0.0, -0.0), (1.6573, 1.7930, 0.4328), "DV_BP_DM_Orc_Shanty_Midden_A_C_Breakable3_6_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_DM_Orc_Shanty_Midden_A_C_Breakable5_10 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (5328.346, 4706.7163, 752.874), (0.0, 0.0, -0.0), (1.6979, 1.7930, 0.6326), "DV_BP_DM_Orc_Shanty_Midden_A_C_Breakable5_10_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_DM_Orc_Shanty_Midden_A_C_Breakable6_19 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (1210.6229, 2705.0886, 710.36536), (0.0, 0.0, -0.0), (1.6854, 1.8023, 0.5877), "DV_BP_DM_Orc_Shanty_Midden_A_C_Breakable6_19_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_DM_Orc_Shanty_Midden_A_C_Breakable7_13 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (5046.41, 4556.688, 707.79913), (0.0, 0.0, -0.0), (1.6573, 1.8214, 0.5719), "DV_BP_DM_Orc_Shanty_Midden_A_C_Breakable7_13_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_DM_Orc_Shanty_Midden_A_C_Breakable8_16 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (3676.613, 4743.3354, 635.7438), (0.0, 0.0, -0.0), (1.6673, 1.7930, 0.4724), "DV_BP_DM_Orc_Shanty_Midden_A_C_Breakable8_16_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_DM_Orc_Shanty_Midden_A_C_Breakable9 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (1154.4203, 2695.6394, 729.1793), (0.0, 0.0, -0.0), (1.6854, 1.8023, 0.5877), "DV_BP_DM_Orc_Shanty_Midden_A_C_Breakable9_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_DM_Orc_Shanty_Midden_C_B_Breakable_5 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (2008.8875, 2403.574, 674.4766), (0.0, 0.0, -0.0), (3.3903, 3.2993, 0.9804), "DV_BP_DM_Orc_Shanty_Midden_C_B_Breakable_5_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_DM_Orc_Shanty_Midden_C_B_Breakable2_8 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (2495.8416, 3286.843, 653.3812), (0.0, 0.0, -0.0), (2.2650, 2.5547, 0.6993), "DV_BP_DM_Orc_Shanty_Midden_C_B_Breakable2_8_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_DM_Orc_Shanty_Midden_C_C_Breakable_5 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (2062.849, 2326.356, 665.84796), (0.0, 0.0, -0.0), (2.6508, 2.6375, 0.6870), "DV_BP_DM_Orc_Shanty_Midden_C_C_Breakable_5_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_DM_Orc_Shanty_Midden_C_C_Breakable2_8 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (2519.2844, 3187.902, 638.8229), (0.0, 0.0, -0.0), (1.8994, 1.9167, 0.5166), "DV_BP_DM_Orc_Shanty_Midden_C_C_Breakable2_8_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_DM_Orc_Shanty_Midden_C_D_Breakable_2 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (5785.248, 4381.8125, 803.55084), (0.0, 0.0, -0.0), (2.0482, 2.1102, 0.6161), "DV_BP_DM_Orc_Shanty_Midden_C_D_Breakable_2_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_DM_Orc_Shanty_Midden_C_D_Breakable2_5 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (5900.4775, 4410.5547, 809.2172), (0.0, 0.0, -0.0), (2.4716, 2.4285, 0.6288), "DV_BP_DM_Orc_Shanty_Midden_C_D_Breakable2_5_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_DM_Orc_Shanty_Midden_C_D_Breakable3_8 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (2134.6174, 2414.063, 663.5219), (0.0, 0.0, -0.0), (2.7968, 2.8179, 0.7173), "DV_BP_DM_Orc_Shanty_Midden_C_D_Breakable3_8_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_DM_Orc_Shanty_Midden_D_B_Breakable_5 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (2552.4705, 3108.7214, 636.471), (0.0, 0.0, -0.0), (1.6678, 1.5490, 0.1871), "DV_BP_DM_Orc_Shanty_Midden_D_B_Breakable_5_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_DM_Orc_Shanty_Midden_D_C_Breakable_2 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (2684.2651, 2884.037, 641.83374), (0.0, 0.0, -0.0), (2.0231, 2.1182, 0.3469), "DV_BP_DM_Orc_Shanty_Midden_D_C_Breakable_2_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_DM_Warren_Lighting_Torch_Breakable_2 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (2473.2686, 2971.7612, 697.8237), (0.0, 0.0, -0.0), (1.4140, 1.4379, 1.9128), "DV_BP_DM_Warren_Lighting_Torch_Breakable_2_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_Orc_Remains_B_2 (EMorSimpleShape::Empty)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (5775.0, 1470.0, 785.0), (5.624994866963602, 0.0, -0.0), (2.0000, 2.0000, 2.0000), "DV_BP_Orc_Remains_B_2", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_Orc_Remains_B2_5 (EMorSimpleShape::Empty)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (1443.9049, 3957.6494, 690.0), (0.0, 132.18758053980275, -0.0), (2.0000, 2.0000, 2.0000), "DV_BP_Orc_Remains_B2_5", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_Orc_Remains_E_2 (EMorSimpleShape::Empty)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (1394.6299, 4106.931, 740.0), (-0.0, -140.6251236981185, -0.0), (2.0000, 2.0000, 2.0000), "DV_BP_Orc_Remains_E_2", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_Orc_Remains_F_2 (EMorSimpleShape::Empty)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (5257.9897, 1631.2638, 685.73505), (8.299219142252944, 38.97705499068446, 3.1463501266065608), (2.0000, 2.0000, 2.0000), "DV_BP_Orc_Remains_F_2", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_Orc_Remains_G_2 (EMorSimpleShape::Empty)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (5450.8423, 4555.934, 805.8639), (-2.0431516619338637, 103.91650098141594, 8.188236976799493), (2.0000, 2.0000, 2.0000), "DV_BP_Orc_Remains_G_2", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_Orc_Scaffolding_Post_1m_A_2 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (5628.023, 4350.0576, 788.9432), (0.0, 0.0, -0.0), (1.1536, 0.5120, 0.2276), "DV_BP_Orc_Scaffolding_Post_1m_A_2_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_Orc_Scaffolding_Post_1m_A2 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (5884.9336, 4295.056, 793.1021), (0.0, 0.0, -0.0), (1.1233, 0.7068, 0.3397), "DV_BP_Orc_Scaffolding_Post_1m_A2_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_Orc_Scaffolding_Post_1m_A3_8 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (5601.0273, 4445.633, 789.95636), (0.0, 0.0, -0.0), (0.2310, 1.1335, 0.2408), "DV_BP_Orc_Scaffolding_Post_1m_A3_8_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_Orc_Scaffolding_Post_1m_A4_6 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (3508.128, 3817.3325, 657.9671), (0.0, 0.0, -0.0), (1.1526, 0.5580, 0.4789), "DV_BP_Orc_Scaffolding_Post_1m_A4_6_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_Orc_Scaffolding_Post_1m_A5_9 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (4249.539, 2242.2737, 677.99725), (0.0, 0.0, -0.0), (0.9812, 0.9496, 0.2003), "DV_BP_Orc_Scaffolding_Post_1m_A5_9_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_Orc_Scaffolding_Post_1m_A6_12 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (2312.5767, 3297.607, 645.7553), (0.0, 0.0, -0.0), (0.8660, 1.0391, 0.2053), "DV_BP_Orc_Scaffolding_Post_1m_A6_12_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_Orc_Scaffolding_Post_1m_C_2 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (3518.6064, 3882.5503, 639.81976), (0.0, 0.0, -0.0), (1.4116, 1.2688, 0.3007), "DV_BP_Orc_Scaffolding_Post_1m_C_2_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_Orc_Scaffolding_Post_1m_C2_5 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (5594.6035, 4503.3267, 785.92816), (0.0, 0.0, -0.0), (1.5092, 1.0929, 0.3812), "DV_BP_Orc_Scaffolding_Post_1m_C2_5_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_Orc_Scaffolding_Post_1m_C3_5 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (2360.3452, 3487.8677, 645.8009), (0.0, 0.0, -0.0), (1.4659, 1.1752, 0.2091), "DV_BP_Orc_Scaffolding_Post_1m_C3_5_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_Orc_Scaffolding_Post_1m_D_2 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (4899.7676, 1932.3481, 665.8625), (0.0, 0.0, -0.0), (0.5474, 1.0874, 0.2149), "DV_BP_Orc_Scaffolding_Post_1m_D_2_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_Orc_Scaffolding_Post_1m_D10 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (1082.2031, 3270.2446, 722.75604), (0.0, 0.0, -0.0), (1.0885, 0.1848, 0.1742), "DV_BP_Orc_Scaffolding_Post_1m_D10_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_Orc_Scaffolding_Post_1m_D2 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (4814.48, 1950.1152, 658.1754), (0.0, 0.0, -0.0), (1.1036, 0.3149, 0.2290), "DV_BP_Orc_Scaffolding_Post_1m_D2_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_Orc_Scaffolding_Post_1m_D4 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (4797.6113, 2076.806, 655.90356), (0.0, 0.0, -0.0), (0.6487, 1.0537, 0.1150), "DV_BP_Orc_Scaffolding_Post_1m_D4_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_Orc_Scaffolding_Post_1m_D5_8 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (4151.351, 2181.3525, 673.0801), (0.0, 0.0, -0.0), (1.0889, 0.1848, 0.1856), "DV_BP_Orc_Scaffolding_Post_1m_D5_8_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_Orc_Scaffolding_Post_1m_D6_11 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (1306.2981, 2789.1963, 692.1695), (0.0, 0.0, -0.0), (1.0885, 0.1848, 0.1742), "DV_BP_Orc_Scaffolding_Post_1m_D6_11_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_Orc_Scaffolding_Post_1m_D7 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (1181.4835, 2855.6824, 704.2779), (0.0, 0.0, -0.0), (0.9682, 0.8178, 0.2882), "DV_BP_Orc_Scaffolding_Post_1m_D7_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_Orc_Scaffolding_Post_1m_D8_15 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (2355.7852, 3278.5037, 635.87415), (0.0, 0.0, -0.0), (0.6824, 1.0427, 0.1427), "DV_BP_Orc_Scaffolding_Post_1m_D8_15_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_Orc_Scaffolding_Post_1m_D9 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (2412.6243, 3115.7285, 633.6222), (0.0, 0.0, -0.0), (0.8790, 0.9185, 0.1429), "DV_BP_Orc_Scaffolding_Post_1m_D9_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_Orc_Scaffolding_Post_2m_A_2 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (6010.403, 4372.976, 801.7984), (0.0, 0.0, -0.0), (1.5806, 1.6694, 0.1241), "DV_BP_Orc_Scaffolding_Post_2m_A_2_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_Orc_Scaffolding_Post_2m_A2_8 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (3426.3381, 3868.5615, 640.1549), (0.0, 0.0, -0.0), (2.1728, 0.1166, 0.1302), "DV_BP_Orc_Scaffolding_Post_2m_A2_8_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_Orc_Scaffolding_Post_2m_A3 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (3384.449, 4571.573, 623.84875), (0.0, 0.0, -0.0), (1.9619, 1.1473, 0.1398), "DV_BP_Orc_Scaffolding_Post_2m_A3_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_Orc_Scaffolding_Post_2m_D_2 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (5346.679, 4616.775, 746.50885), (0.0, 0.0, -0.0), (2.1655, 0.6320, 0.9934), "DV_BP_Orc_Scaffolding_Post_2m_D_2_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_Orc_Scaffolding_Post_2m_D2_5 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (2611.065, 3011.2297, 633.36035), (0.0, 0.0, -0.0), (1.4340, 1.9602, 0.6070), "DV_BP_Orc_Scaffolding_Post_2m_D2_5_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_Orc_Scaffolding_Post_2m_D3 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (2998.462, 2676.802, 629.7555), (0.0, 0.0, -0.0), (2.0906, 1.1962, 0.6070), "DV_BP_Orc_Scaffolding_Post_2m_D3_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_Orc_Scaffolding_Post_3m_B_2 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (4642.761, 1940.4706, 753.6234), (0.0, 0.0, -0.0), (1.4509, 1.8634, 2.8249), "DV_BP_Orc_Scaffolding_Post_3m_B_2_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_Orc_Scaffolding_Post_3m_B3_8 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (5696.1226, 4560.635, 799.3599), (0.0, 0.0, -0.0), (0.2371, 3.3573, 0.3224), "DV_BP_Orc_Scaffolding_Post_3m_B3_8_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_Orc_Scaffolding_Post_3m_B4_11 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (5712.496, 4458.8633, 850.1233), (0.0, 0.0, -0.0), (2.8685, 0.9682, 2.0258), "DV_BP_Orc_Scaffolding_Post_3m_B4_11_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_Orc_Scaffolding_Post_3m_C_2 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (5029.87, 1469.8855, 732.53986), (0.0, 0.0, -0.0), (2.9660, 1.1344, 1.5433), "DV_BP_Orc_Scaffolding_Post_3m_C_2_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_Orc_Scaffolding_Post_3m_C4_11 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (5316.2095, 4739.4463, 834.7846), (0.0, 0.0, -0.0), (1.1666, 2.4277, 2.3451), "DV_BP_Orc_Scaffolding_Post_3m_C4_11_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_Orc_Scaffolding_Post_3m_D_2 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (4521.18, 2270.5366, 438.04727), (0.0, 0.0, -0.0), (1.6972, 1.7344, 3.0443), "DV_BP_Orc_Scaffolding_Post_3m_D_2_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_Orc_Scaffolding_Post_3m_D2_2 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (2082.4377, 2386.5564, 674.3708), (0.0, 0.0, -0.0), (3.0744, 2.1473, 0.9565), "DV_BP_Orc_Scaffolding_Post_3m_D2_2_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_Orc_Scaffolding_Post_3m_D3_8 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (5198.525, 4645.3076, 744.7193), (0.0, 0.0, -0.0), (0.9548, 3.2660, 0.8358), "DV_BP_Orc_Scaffolding_Post_3m_D3_8_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_Orc_Scaffolding_Post_3m_D4_5 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (4244.599, 1951.2441, 738.17554), (0.0, 0.0, -0.0), (0.5828, 3.0055, 1.8068), "DV_BP_Orc_Scaffolding_Post_3m_D4_5_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_Orc_Scaffolding_Post_3m_D5_8 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (961.18994, 2764.3057, 823.2523), (0.0, 0.0, -0.0), (2.0439, 2.4914, 2.3843), "DV_BP_Orc_Scaffolding_Post_3m_D5_8_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_Orc_Scaffolding_Post_4m_A_2 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (5676.6616, 1143.3062, 933.0215), (0.0, 0.0, -0.0), (0.6126, 2.1027, 3.9813), "DV_BP_Orc_Scaffolding_Post_4m_A_2_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_Orc_Scaffolding_Post_4m_A2_2 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (3923.1104, 2702.5413, 661.0751), (0.0, 0.0, -0.0), (4.0438, 1.9665, 0.2613), "DV_BP_Orc_Scaffolding_Post_4m_A2_2_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_Orc_Scaffolding_Post_4m_A3_5 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (1393.642, 3399.0874, 696.4975), (0.0, 0.0, -0.0), (3.7424, 2.5344, 0.3242), "DV_BP_Orc_Scaffolding_Post_4m_A3_5_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_Orc_Scaffolding_Post_4m_B_2 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (5738.7305, 1175.161, 923.6707), (0.0, 0.0, -0.0), (2.0123, 1.9465, 3.9580), "DV_BP_Orc_Scaffolding_Post_4m_B_2_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_Orc_Scaffolding_Post_4m_B2_2 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (1074.8959, 3473.3918, 888.7688), (0.0, 0.0, -0.0), (0.2977, 2.9332, 3.6380), "DV_BP_Orc_Scaffolding_Post_4m_B2_2_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_Orc_Scaffolding_Post_5m_D_2 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (4522.7495, 1941.2, 782.1146), (0.0, 0.0, -0.0), (2.2696, 3.8925, 4.7710), "DV_BP_Orc_Scaffolding_Post_5m_D_2_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_Orc_Scaffolding_Post_5m_D2_2 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (3725.4492, 3681.251, 860.0837), (0.0, 0.0, -0.0), (3.2994, 3.6376, 4.6671), "DV_BP_Orc_Scaffolding_Post_5m_D2_2_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_Orc_Scaffolding_Post_5m_D4_11 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (2713.1943, 3185.743, 724.0188), (0.0, 0.0, -0.0), (5.3643, 2.3923, 3.7876), "DV_BP_Orc_Scaffolding_Post_5m_D4_11_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: DecorationBlockingVolume_1 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (5900.0, 3200.0, 1050.0), (0.0, 0.0, -0.0), (14.0000, 5.0000, 5.0000), "DV_DecorationBlockingVolume_1", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: DecorationBlockingVolume_2 (EMorSimpleShape::Empty)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (1980.6294, 3462.135, 631.7761), (-0.0, -9.155273700792082e-05, -0.0), (2.0000, 2.0000, 2.0000), "DV_DecorationBlockingVolume_2", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: DecorationBlockingVolume_3 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (500.0, 3200.0, 1050.0), (0.0, 0.0, -0.0), (2.0000, 2.0000, 2.0000), "DV_DecorationBlockingVolume_3", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: DecorationBlockingVolume_4 (EMorSimpleShape::Empty)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (4850.1704, 1438.1598, 737.44135), (0.0, 50.00005877099974, -0.0), (2.0000, 2.0000, 2.0000), "DV_DecorationBlockingVolume_4", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: DecorationBlockingVolume_6 (EMorSimpleShape::Empty)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (1093.8864, 2739.6365, 731.62256), (0.0, 40.00004110866871, -0.0), (2.0000, 2.0000, 2.0000), "DV_DecorationBlockingVolume_6", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: DecorationBlockingVolume10 (EMorSimpleShape::Empty)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (3995.2222, 4179.6655, 631.7699), (0.0, 4.9999087549408685, -0.0), (2.0000, 2.0000, 2.0000), "DV_DecorationBlockingVolume10", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: DecorationBlockingVolume11 (EMorSimpleShape::Empty)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (5439.4883, 3329.0396, 631.7705), (-0.0, -9.155273700792082e-05, -0.0), (2.0000, 2.0000, 2.0000), "DV_DecorationBlockingVolume11", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: DecorationBlockingVolume12 (EMorSimpleShape::Empty)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (3470.4673, 2455.119, 631.7744), (-0.0, -10.00021368168033, -0.0), (2.0000, 2.0000, 2.0000), "DV_DecorationBlockingVolume12", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: DecorationBlockingVolume4_14 (EMorSimpleShape::Empty)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (3796.8289, 3359.8464, 970.0), (-0.0, -10.000060728507771, -0.0), (2.0000, 2.0000, 2.0000), "DV_DecorationBlockingVolume4_14", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: DecorationBlockingVolume5 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (3200.0, 500.0, 1050.0), (0.0, 89.99999818714215, -0.0), (14.0000, 5.0000, 5.0000), "DV_DecorationBlockingVolume5", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: DecorationBlockingVolume6 (EMorSimpleShape::Sphere)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (3153.4004, 4154.324, 662.1012), (0.0, 0.0, -0.0), (2.0000, 2.0000, 2.0000), "DV_DecorationBlockingVolume6", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: DecorationBlockingVolume7_8 (EMorSimpleShape::Empty)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (1093.8864, 3410.9663, 731.6198), (-0.0, -40.00005923828246, -0.0), (2.0000, 2.0000, 2.0000), "DV_DecorationBlockingVolume7_8", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: DecorationBlockingVolume8 (EMorSimpleShape::Empty)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (2366.1316, 2371.4375, 680.32227), (-0.0, -90.00005166594045, -0.0), (2.0000, 2.0000, 2.0000), "DV_DecorationBlockingVolume8", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: DecorationBlockingVolume9 (EMorSimpleShape::Sphere)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (3560.2598, 4816.703, 662.101), (0.0, 0.0, -0.0), (2.0000, 2.0000, 2.0000), "DV_DecorationBlockingVolume9", _folder)
if a: placed += 1
else: skipped += 1

# ======================================================================
# SUMMARY
# ======================================================================
unreal.log(f"[{BUBBLE_NAME}] Reconstruction complete: {placed} placed, {skipped} skipped, {errors} errors")
