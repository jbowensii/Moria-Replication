"""Auto-generated level reconstruction script.
Bubble: BD_BB_Chapter5_BrokenSeal
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

BUBBLE_NAME = "BD_BB_Chapter5_BrokenSeal"
placed = 0
skipped = 0
errors = 0

# ======================================================================
# PHASE 1: InstancedMeshCatalog  (static mesh placement)
# ======================================================================
unreal.log(f"[{BUBBLE_NAME}] Phase 1: Placing static meshes...")

# Batch 0: StaticMesh'Deep_MetalCage' (3 instances)
_mesh_path = "/Game/Art/Assets/Kits/Architecture/Deep/Deep_MetalCage"
_materials = ['/Game/Art/Assets/Kits/Architecture/Suburbs/Materials/Suburbs_Trim_Sheet_B/MI_Suburbs_Trim_Sheet_B']
_folder = "Reconstruction/BD_BB_Chapter5_BrokenSeal/Meshes"
a = spawn_static_mesh(_mesh_path, _materials, (2495.0, 4330.0, 1520.0), (0.0, -119.99996892809061, 0.0), (2.84375, 2.84375, 2.84375), "Deep_MetalCage_8", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3902.55, 4301.8047, 1625.0018), (0.0, -65.06634191510427, 0.0), (2.84375, 2.84375, 2.84375), "Deep_MetalCage2", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3983.5322, 2322.42, 1523.0461), (0.0, 120.89270590590608, -0.0), (2.84375, 2.84375, 2.84375), "Deep_MetalCage3", _folder)
if a: placed += 1
else: skipped += 1

# Batch 1: StaticMesh'Deep_WoodenBeam_A' (3 instances)
_mesh_path = "/Game/Art/Assets/Kits/Architecture/Deep/Deep_WoodenBeam_A"
_materials = ['/Game/Art/Assets/Kits/Architecture/Deep/Materials/Deep_WoodTrim/MI_Deep_WoodTrim']
_folder = "Reconstruction/BD_BB_Chapter5_BrokenSeal/Meshes"
a = spawn_static_mesh(_mesh_path, _materials, (2500.0, 4450.0, 950.0), (0.0, -179.99998633961752, -0.0), (1.5, 1.5, 1.875), "Deep_WoodenBeam_A_2", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3914.48, 4412.53, 950.0), (0.0, -114.73918850122507, 0.0), (1.5, 1.5, 1.875), "Deep_WoodenBeam_A4", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4069.8252, 2236.9531, 914.43286), (0.0, 60.8923371018963, -0.0), (1.5, 1.5, 2.25), "Deep_WoodenBeam_A5", _folder)
if a: placed += 1
else: skipped += 1

# Batch 2: StaticMesh'NonD_Stairs_Trim_A_L' (10 instances)
_mesh_path = "/Game/Art/Assets/Kits/Architecture/Non_D/NonD_Stairs_Trim_A_L"
_materials = ['/Game/Art/Assets/Kits/Architecture/Suburbs/Materials/Suburbs_Trim_Sheet_A/MI_Suburbs_Trim_Sheet_A', '/Game/Environments/Materials/MI_Suburbs_Non_Destructible']
_folder = "Reconstruction/BD_BB_Chapter5_BrokenSeal/Meshes"
a = spawn_static_mesh(_mesh_path, _materials, (4406.8984, 1322.1285, 1205.0), (0.0, 40.000080625833, -0.0), (1.0, 0.9375, 1.0), "NonD_Stairs_Trim_A_L_26", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4636.096, 1507.9207, 1010.0), (0.0, 40.000080625833, -0.0), (1.0, 1.0, 1.0), "NonD_Stairs_Trim_A_L2", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2696.463, 5419.826, 1125.0), (0.0, -159.99981473322237, 0.0), (1.0, 0.9375, 1.0), "NonD_Stairs_Trim_A_L3", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2419.2527, 5318.93, 930.0), (0.0, -159.99981473322237, 0.0), (1.0, 1.0, 1.0), "NonD_Stairs_Trim_A_L4", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2221.9175, 5247.105, 795.0), (0.0, -159.99981473322237, 0.0), (1.0, 1.0, 1.0), "NonD_Stairs_Trim_A_L5_259", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (913.9883, 2795.955, 1200.0), (0.0, -64.99996310340273, 0.0), (1.0, 1.0, 1.0), "NonD_Stairs_Trim_A_L6_321", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1045.0002, 2514.9998, 965.0), (0.0, -64.99996310340273, 0.0), (1.09375, 1.0, 1.15625), "NonD_Stairs_Trim_A_L7", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1171.7855, 2243.1074, 760.0), (0.0, -64.99996310340273, 0.0), (1.09375, 1.0, 1.15625), "NonD_Stairs_Trim_A_L8", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4670.0, 3520.0, 985.001), (0.0, 0.0, -0.0), (1.0, 1.0, 1.0), "NonD_Stairs_Trim_A_R5", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4955.0, 3520.0, 785.0), (0.0, 0.0, -0.0), (1.0625, 1.0, 1.03125), "NonD_Stairs_Trim_A_R6", _folder)
if a: placed += 1
else: skipped += 1

# Batch 3: StaticMesh'NonD_Stairs_Trim_A_R' (10 instances)
_mesh_path = "/Game/Art/Assets/Kits/Architecture/Non_D/NonD_Stairs_Trim_A_R"
_materials = ['/Game/Art/Assets/Kits/Architecture/Suburbs/Materials/Suburbs_Trim_Sheet_A/MI_Suburbs_Trim_Sheet_A', '/Game/Environments/Materials/MI_Suburbs_Non_Destructible']
_folder = "Reconstruction/BD_BB_Chapter5_BrokenSeal/Meshes"
a = spawn_static_mesh(_mesh_path, _materials, (2741.7363, 954.77893, 1200.0), (0.0, 159.99993763246997, -0.0), (1.0, 1.0, 1.0), "NonD_Stairs_Trim_A_R_101", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2003.1527, 5042.4023, 735.0), (0.0, 140.00001793552548, -0.0), (1.0, 1.0, 1.0), "NonD_Stairs_Trim_A_R10_262", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (846.16034, 3621.8435, 1205.0), (0.0, 60.000067159027765, -0.0), (1.0, 1.0, 1.0), "NonD_Stairs_Trim_A_R11_305", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (991.82996, 3884.1511, 1005.0), (0.0, 60.942066987492765, -0.0), (1.0, 1.0, 1.0), "NonD_Stairs_Trim_A_R12", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2450.4314, 1060.8057, 970.0), (0.0, 159.99993763246997, -0.0), (1.09375, 1.0, 1.125), "NonD_Stairs_Trim_A_R2", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4670.0, 2890.0, 985.0), (0.0, 0.0, -0.0), (1.0, 1.0, 1.0), "NonD_Stairs_Trim_A_R3_165", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4955.0, 2890.0, 785.0), (0.0, 0.0, -0.0), (1.0625, 1.0, 1.03125), "NonD_Stairs_Trim_A_R4", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4438.6816, 5172.176, 1210.0), (0.0, -45.000056798727684, 0.0), (1.0, 1.0, 1.0), "NonD_Stairs_Trim_A_R7_224", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4654.3486, 4956.5083, 1005.0), (0.0, -45.000056798727684, 0.0), (1.0, 1.0, 1.0), "NonD_Stairs_Trim_A_R8", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4870.015, 4740.8413, 800.0), (0.0, -45.000056798727684, 0.0), (1.0, 1.0, 1.0), "NonD_Stairs_Trim_A_R9", _folder)
if a: placed += 1
else: skipped += 1

# Batch 4: StaticMesh'NonD_Stairs_Trim_C_L' (8 instances)
_mesh_path = "/Game/Art/Assets/Kits/Architecture/Non_D/NonD_Stairs_Trim_C_L"
_materials = ['/Game/Art/Assets/Kits/Architecture/Suburbs/Materials/Suburbs_Trim_Sheet_A/MI_Suburbs_Trim_Sheet_A']
_folder = "Reconstruction/BD_BB_Chapter5_BrokenSeal/Meshes"
a = spawn_static_mesh(_mesh_path, _materials, (5050.0, 4410.0, 725.0), (0.0, 0.0, -0.0), (1.0, 1.0, 1.0), "NonD_Stairs_Trim_C_L_2", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4981.081, 869.7068, 1100.0), (0.0, 35.00004379987181, -0.0), (1.0, 1.0, 1.0), "NonD_Stairs_Trim_C_L2_8", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (423.934, 2227.7585, 1000.0), (0.0, -70.00002222525863, 0.0), (1.0, 1.0, 1.0), "NonD_Stairs_Trim_C_L3_15", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (526.5398, 1945.8508, 800.0), (0.0, -70.00002222525863, 0.0), (1.0, 1.0, 1.0), "NonD_Stairs_Trim_C_L4", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (321.3281, 2509.6663, 1200.0), (0.0, -70.00002222525863, 0.0), (1.0, 1.0, 1.0), "NonD_Stairs_Trim_C_L5", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (354.66425, 3873.4304, 1195.0), (0.0, 74.06257595365656, -0.0), (1.0, 1.0, 1.0), "NonD_Stairs_Trim_C_L6_20", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (437.04047, 4161.8984, 995.0), (0.0, 74.06257595365656, -0.0), (1.0, 1.0, 1.0), "NonD_Stairs_Trim_C_L7", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (519.4167, 4450.367, 795.0), (0.0, 74.06257595365656, -0.0), (1.0, 1.0, 1.0), "NonD_Stairs_Trim_C_L8_24", _folder)
if a: placed += 1
else: skipped += 1

# Batch 5: StaticMesh'NonDest_Boundry_2m_Trim_A' (3 instances)
_mesh_path = "/Game/Art/Assets/Kits/Architecture/Non_D/NonDest_Boundry_2m_Trim_A"
_materials = ['/Game/Art/Assets/Kits/Architecture/Suburbs/Materials/Suburbs_Trim_Sheet_A/MI_Suburbs_Trim_Sheet_A']
_folder = "Reconstruction/BD_BB_Chapter5_BrokenSeal/Meshes"
a = spawn_static_mesh(_mesh_path, _materials, (3428.171, 1464.89, 965.99945), (2.7000009116519333e-05, -0.0006103515424015983, 89.9999706389512), (1.375, 1.0, 1.0), "NonDest_Boundry_3m_Trim_A18", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1194.0786, 2211.073, 985.0), (0.0, -65.00014701274256, 0.0), (1.0, 1.0, 1.0), "NonDest_Boundry_3m_Trim_A40", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1939.0983, 5139.9585, 984.99536), (0.00046099998859444727, 20.001282378646355, -179.9995833584328), (1.0, 1.0, 1.0), "NonDest_Boundry_3m_Trim_B11", _folder)
if a: placed += 1
else: skipped += 1

# Batch 6: StaticMesh'NonDest_Boundry_3m_Trim_A' (48 instances)
_mesh_path = "/Game/Art/Assets/Kits/Architecture/Non_D/NonDest_Boundry_3m_Trim_A"
_materials = ['/Game/Art/Assets/Kits/Architecture/Suburbs/Materials/Suburbs_Trim_Sheet_A/MI_Suburbs_Trim_Sheet_A']
_folder = "Reconstruction/BD_BB_Chapter5_BrokenSeal/Meshes"
a = spawn_static_mesh(_mesh_path, _materials, (3811.0352, 1110.7743, 995.0), (0.0, 20.00007399814644, -0.0), (1.0, 1.0, 1.0), "NonDest_Boundry_3m_Trim_A_46", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4918.3877, 1747.4227, 1095.05), (0.0, -49.99997085178047, 0.0), (1.125, 1.0, 1.0), "NonDest_Boundry_3m_Trim_A10", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5136.9355, 1486.9679, 1095.05), (0.0, -49.99997085178047, 0.0), (1.25, 1.0, 1.0), "NonDest_Boundry_3m_Trim_A11", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2227.8633, 1152.5117, 985.0), (0.0, -20.000029202010403, 0.0), (1.375, 1.0, 1.0), "NonDest_Boundry_3m_Trim_A12", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1912.0394, 1264.2687, 985.0), (0.0, -20.000029202010403, 0.0), (1.125, 1.0, 1.0), "NonDest_Boundry_3m_Trim_A13", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2793.171, 1464.8848, 966.0), (2.0490563166240013e-05, 179.99995901885129, 89.99999818714386), (1.46875, 1.0, 1.0), "NonDest_Boundry_3m_Trim_A14", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2362.912, 1465.8507, 966.05), (2.0002982795309364e-05, -164.9995383156962, 89.99995143290862), (1.46875, 1.0, 1.0), "NonDest_Boundry_3m_Trim_A15", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3702.171, 1464.89, 965.99945), (2.732074410040128e-05, -0.0006103515181724374, 89.99997063894955), (1.375, 1.0, 1.0), "NonDest_Boundry_3m_Trim_A16", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4111.171, 1465.89, 965.0), (3.382151277926148e-05, -15.00067245337628, 89.99994603296777), (1.46875, 1.0, 1.0), "NonDest_Boundry_3m_Trim_A17", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4670.0, 2885.0, 990.0), (0.0, 0.0, -9.155273700792082e-05), (1.03125, 1.03125, 1.0), "NonDest_Boundry_3m_Trim_A19_193", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4092.9426, 1213.3807, 995.0), (0.0, 20.00007399814644, -0.0), (1.0, 1.0, 1.0), "NonDest_Boundry_3m_Trim_A2", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4670.0, 2880.0, 960.0), (0.0, 0.0, -9.155273700792082e-05), (1.03125, 1.03125, 1.0), "NonDest_Boundry_3m_Trim_A20", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4335.0, 2900.0, 960.0), (0.0, 0.0, -9.155273700792082e-05), (1.03125, 1.03125, 1.0), "NonDest_Boundry_3m_Trim_A21", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4980.0, 3520.0022, 990.001), (1.3660377253713492e-05, -179.99963116977906, 6.550585834115898e-05), (1.03125, 1.03125, 1.0), "NonDest_Boundry_3m_Trim_A22", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4980.0, 3525.0024, 960.001), (1.3660377253713492e-05, -179.99963116977906, 6.550585834115898e-05), (1.03125, 1.03125, 1.0), "NonDest_Boundry_3m_Trim_A23", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4660.0, 3524.9988, 960.0009), (9.28962602083848e-18, 179.9998224150775, 8.184920973343992e-05), (1.03125, 1.03125, 1.0), "NonDest_Boundry_3m_Trim_A24", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4660.0, 3529.9988, 920.0009), (6.7228575872801905e-18, 179.9998224150775, 8.200000076596295e-05), (1.03125, 1.03125, 1.21875), "NonDest_Boundry_3m_Trim_A25", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4335.0, 2895.0, 920.0), (0.0, 0.0, -9.155273700792082e-05), (1.03125, 1.03125, 1.15625), "NonDest_Boundry_3m_Trim_A26", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4335.0, 3524.9985, 840.00085), (-9.155272984018488e-05, -89.99993822610317, -3.051757402625963e-05), (1.03125, 1.03125, 1.0), "NonDest_Boundry_3m_Trim_A27", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4335.0, 3214.9985, 840.0002), (-9.155272984018488e-05, -89.99993822610317, -3.051757402625963e-05), (1.03125, 1.03125, 1.0), "NonDest_Boundry_3m_Trim_A28", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2808.1729, 4914.885, 960.9999), (1.999999580020357e-05, 179.99995901885288, 89.99999818714394), (1.75, 1.0, 1.0), "NonDest_Boundry_3m_Trim_A29", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4406.277, 1341.5056, 950.0), (0.0, 40.00006853942215, -0.0), (1.0, 1.0, 1.0), "NonDest_Boundry_3m_Trim_A3", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2295.1182, 4914.1016, 961.00006), (4.192711474674142e-05, 154.999977509509, 89.9999857521901), (1.25, 1.0, 1.0), "NonDest_Boundry_3m_Trim_A30", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1957.0398, 5093.021, 1021.00006), (-90.0, -2.9666092929527172, -162.03260185315156), (1.25, 1.0, 1.0), "NonDest_Boundry_3m_Trim_A31", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (830.9809, 3582.9675, 1015.0), (0.0, 60.000011912675895, -0.0), (1.0625, 1.0, 1.0), "NonDest_Boundry_3m_Trim_A32", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1069.4069, 2478.4343, 985.0), (0.0, -65.00014701274256, 0.0), (1.0, 1.0, 1.0), "NonDest_Boundry_3m_Trim_A33_329", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1648.1702, 2459.8872, 961.0003), (1.7761600663120725e-05, 89.99962757802021, 89.99996906082171), (1.1574723, 1.0, 1.0), "NonDest_Boundry_3m_Trim_A35", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1648.1722, 2804.8872, 961.00037), (1.7761600663120725e-05, 89.99962757802021, 89.99996906082171), (1.46875, 1.0, 1.0), "NonDest_Boundry_3m_Trim_A36", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1648.175, 3244.8872, 966.0004), (1.7761600663120725e-05, 89.99962757802021, 89.99996906082171), (1.46875, 1.0, 1.0), "NonDest_Boundry_3m_Trim_A37", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1648.1785, 3684.8872, 966.0005), (1.7761600663120725e-05, 89.99962757802021, 89.99996906082171), (1.09375, 1.0, 1.0), "NonDest_Boundry_3m_Trim_A38", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1673.081, 2463.1873, 961.0003), (7.502342600734208e-05, -125.00018151959176, 90.00006890301256), (1.7923535, 1.0, 1.0), "NonDest_Boundry_3m_Trim_A39", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4651.4106, 1547.1976, 950.0), (0.0, 40.00006853942215, -0.0), (1.125, 1.0, 1.0), "NonDest_Boundry_3m_Trim_A4", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1655.5564, 3995.6362, 965.09), (4.202067661491731e-05, 124.99966592038686, 89.99995653037367), (1.09375, 1.0, 1.0), "NonDest_Boundry_3m_Trim_A41", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1469.146, 4261.8613, 966.0006), (4.202067661491731e-05, 124.99966592038686, 89.99995653037367), (0.78125, 1.0, 1.0), "NonDest_Boundry_3m_Trim_A42", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1157.4597, 4182.009, 966.0007), (3.748610912341483e-05, 64.99962917496835, 89.99997706259137), (0.875, 1.0, 1.0), "NonDest_Boundry_3m_Trim_A43", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1328.3998, 4429.714, 983.339), (-90.0, -39.10695681901642, -35.89242876961036), (0.78125, 1.0, 1.0), "NonDest_Boundry_3m_Trim_A44", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1477.3376, 4267.5967, 891.0006), (4.202067661491731e-05, 124.99966592038686, 89.99995653037367), (0.78125, 1.0, 1.0), "NonDest_Boundry_3m_Trim_A45", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1000.98083, 3877.4167, 1015.0), (0.0, 60.000011912675895, -0.0), (1.0625, 1.0, 1.0), "NonDest_Boundry_3m_Trim_A5_314", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2127.0352, 5208.3677, 984.997), (0.00046099998859444727, 20.001282378646355, -179.9995833584328), (1.0, 1.0, 1.0), "NonDest_Boundry_3m_Trim_B10", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3537.943, 4904.858, 961.9888), (0.0008606036680083876, -0.0004272460531466923, -89.99981507018387), (1.8339325, 1.0, 1.0), "NonDest_Boundry_3m_Trim_B12", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4081.1157, 4904.5176, 962.05), (0.0007447491977065204, 24.998076587039442, -89.99951972922929), (1.788639, 1.0, 1.0), "NonDest_Boundry_3m_Trim_B13", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4643.1367, 4950.145, 940.00305), (-0.0006408690816282971, 134.99971660226853, -179.99989754714835), (1.0, 1.0, 1.0), "NonDest_Boundry_3m_Trim_B3", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4855.2676, 4738.0117, 940.0064), (-0.0006408690816282971, 134.99971660226853, -179.99989754714835), (1.0, 1.0, 1.0), "NonDest_Boundry_3m_Trim_B4", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4409.324, 5152.3013, 984.9995), (-0.0006408690311112829, 154.9997295166353, 179.9998838867498), (1.0, 1.0, 1.0), "NonDest_Boundry_3m_Trim_B5", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4137.434, 5279.0874, 984.99615), (-0.0006408690311112829, 154.9997295166353, 179.9998838867498), (1.0, 1.0, 1.0), "NonDest_Boundry_3m_Trim_B6", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3840.2588, 5403.4526, 984.99243), (-0.000549316312624415, 179.9997063018035, 179.99956969794258), (1.0, 1.0, 1.0), "NonDest_Boundry_3m_Trim_B7", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2417.0593, 5303.296, 984.9995), (0.00046099998859444727, 20.001282378646355, -179.9995833584328), (1.0, 1.0, 1.0), "NonDest_Boundry_3m_Trim_B9", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5471.99, 1223.8108, 1089.2734), (5.464150398807553e-05, -143.6668404804409, -179.99989754716353), (1.15625, 1.0, 1.0), "Trim_A_3m43", _folder)
if a: placed += 1
else: skipped += 1

# Batch 7: StaticMesh'NonDest_Boundry_3m_Trim_B' (70 instances)
_mesh_path = "/Game/Art/Assets/Kits/Architecture/Non_D/NonDest_Boundry_3m_Trim_B"
_materials = ['/Game/Art/Assets/Kits/Architecture/Suburbs/Materials/Suburbs_Trim_Sheet_A/MI_Suburbs_Trim_Sheet_A']
_folder = "Reconstruction/BD_BB_Chapter5_BrokenSeal/Meshes"
a = spawn_static_mesh(_mesh_path, _materials, (4643.1353, 4950.1455, 1200.003), (-0.0006408690816282971, 134.99971660226853, -179.99989754714835), (1.0, 1.0, 1.0), "NonDest_Boundry_3m_Trim_B_233", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4869.4106, 4723.8687, 995.0059), (-0.0006408690816282971, 134.99971660226853, -179.99989754714835), (1.0, 1.0, 1.0), "NonDest_Boundry_3m_Trim_B2", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2417.058, 5303.296, 1119.9995), (0.000461255980697613, 20.001282378647634, -179.99958335843903), (1.0, 1.0, 1.0), "NonDest_Boundry_3m_Trim_B8_249", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2005.0905, 462.51138, 1270.0024), (-0.0005493162721761174, 154.35184815317962, -179.99995901884466), (1.0, 1.0, 1.0), "Trim_A_3m24_58", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2275.5195, 332.6415, 1270.0001), (-9.155273140132974e-05, 154.35186526590917, 179.99997950942947), (1.0, 1.0, 1.0), "Trim_A_3m25", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2545.9512, 202.76471, 1270.0027), (-0.0006103514114906193, 154.35173535239346, -179.9999590188615), (1.0, 1.0, 1.0), "Trim_A_3m26", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5218.2246, 1037.1906, 1284.2754), (-0.0003662109132484194, -143.66812018137776, 179.99989754714218), (1.0, 1.0, 1.0), "Trim_A_3m28", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5459.906, 1214.9233, 1284.2734), (4.0981127856720585e-05, -143.66673234600313, -179.9998975471581), (1.0, 1.0, 1.0), "Trim_A_3m29", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4912.1836, 5662.7827, 1379.2712), (-0.0007629394213629583, -44.06692408064392, 179.99969264143775), (1.0, 1.0, 1.0), "Trim_A_3m30", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5127.746, 5454.147, 1379.2712), (-0.0002136230572268906, -44.06796371503808, -179.99976777357148), (1.0, 1.0, 1.0), "Trim_A_3m31", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5343.313, 5245.5024, 1379.2712), (-0.000396728540639479, -44.06854040695845, 179.99995901887112), (1.0, 1.0, 1.0), "Trim_A_3m32", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1714.068, 5799.4272, 1374.2738), (0.00022539621782868827, 18.56210221596472, 179.99995901886518), (1.0, 1.0, 1.0), "Trim_A_3m33", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1998.452, 5894.9414, 1374.2738), (0.00014352795404125516, 18.561336883819095, 179.99995901885742), (1.0, 1.0, 1.0), "Trim_A_3m34", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2282.8433, 5990.4624, 1374.2742), (0.0002322264089313999, 18.560178115620708, 179.9999590188562), (1.0, 1.0, 1.0), "Trim_A_3m35", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (322.2572, 3848.4883, 1379.273), (0.0002663772907752416, 73.21200442038815, 179.99950822615588), (1.0, 1.0, 1.0), "Trim_A_3m36", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (408.8817, 4135.708, 1379.273), (0.00020490566759703185, 73.21220900334683, 179.99969264153702), (1.0, 1.0, 1.0), "Trim_A_3m37", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (495.51053, 4422.935, 1379.2739), (0.00014400482100624166, 73.21136595029787, -179.99989754716603), (1.0, 1.0, 1.0), "Trim_A_3m38", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (593.65063, 1700.8547, 1379.2742), (1.1395873893535257e-11, 109.37779376533261, 179.99943309405435), (1.0, 1.0, 1.0), "Trim_A_3m39", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (494.10132, 1983.8563, 1379.2738), (-3.051757315454284e-05, 109.37792053471085, 179.99976777349661), (1.0, 1.0, 1.0), "Trim_A_3m40", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (394.5496, 2266.8623, 1379.2734), (6.147168312478766e-05, 109.37786023820793, -179.99995901885498), (1.0, 1.0, 1.0), "Trim_A_3m41", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4976.817, 856.27625, 1284.2738), (-0.0003662108823588177, -142.04356804431598, 179.99991120751693), (1.0, 1.0, 1.0), "Trim_A_3m42", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5209.463, 956.26886, 1929.2754), (-0.00036621097142384437, -143.66794939478152, 179.999897547168), (1.0, 1.0, 1.0), "Trim_A_3m44", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5451.1484, 1134.0012, 1929.2734), (5.464150398807553e-05, -143.6668404804409, -179.99989754716353), (1.0, 1.0, 1.0), "Trim_A_3m45", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4967.788, 778.5281, 1929.2728), (-0.00036621097142384437, -143.66794939478152, 179.999897547168), (1.0625, 1.0, 1.0), "Trim_A_3m46", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2261.995, 284.2077, 1929.2548), (-0.00021362305626118663, 154.20343769865727, -179.9996311697776), (1.0, 1.0, 1.0), "Trim_A_3m47", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5479.7046, 1086.7319, 1614.2734), (5.464150398807553e-05, -143.6668404804409, -179.99989754716353), (1.0, 1.0, 1.0), "Trim_A_3m48", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4998.031, 739.65826, 1614.2728), (-0.0003662108823588177, -142.04356804431598, 179.99991120751693), (1.0, 1.0, 1.0), "Trim_A_3m49", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3498.8618, 1471.916, 1310.5132), (0.00018441507808088426, -179.99943992440413, 179.99995901886155), (2.1875, 1.5, 1.9375), "Trim_A_3m5", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2532.0989, 153.64938, 1929.2523), (0.00021173582951284945, 154.20566053693048, -179.99924184886865), (1.0, 1.0, 1.0), "Trim_A_3m50", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1991.8882, 414.7574, 1929.2528), (-0.00021362305626118663, 154.20343769865727, -179.9996311697776), (1.0625, 1.0, 1.0), "Trim_A_3m51", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2503.8162, 95.12837, 1614.2523), (0.00021199997679762124, 154.20566053693244, -179.99924184883423), (1.0, 1.0, 1.0), "Trim_A_3m52", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1963.6038, 356.2364, 1614.2528), (-0.00021362305626118663, 154.20343769865727, -179.9996311697776), (1.0625, 1.0, 1.0), "Trim_A_3m53", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4635.1055, 1515.1501, 1209.9465), (-0.0003662108823588177, -142.04356804431598, 179.99991120751693), (1.0, 1.0, 1.0), "Trim_A_3m54", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4889.7593, 1732.8137, 1079.9489), (-0.00030517570147365003, -140.12847265040566, 179.99991120752497), (1.0, 1.0, 1.0), "Trim_A_3m55", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4925.2905, 5726.642, 2014.2715), (-0.0007629394213629583, -44.06692408064392, 179.99969264143775), (1.0, 1.0, 1.0), "Trim_A_3m56", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5140.853, 5518.0063, 2014.2715), (-0.0002136230572268906, -44.06796371503808, -179.99976777357148), (1.0, 1.0, 1.0), "Trim_A_3m57", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5356.42, 5309.362, 2014.2715), (-0.000396728540639479, -44.06854040695845, 179.99995901887112), (1.0, 1.0, 1.0), "Trim_A_3m58", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4981.7363, 5734.6313, 1729.2712), (-0.0007629394213629583, -44.06692408064392, 179.99969264143775), (1.0, 1.0, 1.0), "Trim_A_3m59", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3498.8276, 4971.916, 1310.5109), (0.00018399998164236037, -179.999439924404, 179.9999590188618), (2.1875, 1.5, 1.9375), "Trim_A_3m6", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5412.8657, 5317.351, 1729.2712), (-0.000396728540639479, -44.06854040695845, 179.99995901887112), (1.0, 1.0, 1.0), "Trim_A_3m60", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1761.3622, 5862.776, 2034.2739), (0.0002249999986083513, 18.562102215964615, 179.99995901886598), (1.0, 1.0, 1.0), "Trim_A_3m61", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2045.746, 5958.29, 2034.2739), (0.00014399999368637983, 18.56133688381912, 179.9999590188559), (1.0, 1.0, 1.0), "Trim_A_3m62", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2330.1377, 6053.811, 2034.2742), (0.00023199999069575445, 18.560178115620644, 179.99995901886422), (1.0, 1.0, 1.0), "Trim_A_3m63", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1747.0393, 5905.4346, 1724.2739), (0.0002249999986083513, 18.562102215964615, 179.99995901886598), (1.0, 1.0, 1.0), "Trim_A_3m64", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2315.815, 6096.4697, 1724.2742), (0.00023199999069575445, 18.560178115620644, 179.99995901886422), (1.0, 1.0, 1.0), "Trim_A_3m65", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (528.49457, 1720.3401, 2029.2742), (1.1395873893535257e-11, 109.37779376533261, 179.99943309405435), (1.0, 1.0, 1.0), "Trim_A_3m66", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (428.945, 2003.3417, 2029.2738), (-3.051757315454284e-05, 109.37792053471085, 179.99976777349661), (1.0, 1.0, 1.0), "Trim_A_3m67", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (329.39328, 2286.3481, 2029.2734), (6.099999077909853e-05, 109.37786023820753, -179.99995901884938), (1.0, 1.0, 1.0), "Trim_A_3m68", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (471.89346, 1700.4329, 1724.2742), (1.1395873893535257e-11, 109.37779376533261, 179.99943309405435), (1.0, 1.0, 1.0), "Trim_A_3m69", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (272.7921, 2266.441, 1724.2734), (6.099999077909853e-05, 109.37786023820753, -179.99995901884938), (1.0, 1.0, 1.0), "Trim_A_3m70", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (258.50058, 3810.275, 2034.2728), (0.0002659999358632374, 73.21200442038894, 179.99950822614565), (1.0, 1.0, 1.0), "Trim_A_3m71", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (345.1253, 4097.492, 2034.2728), (0.00020500002408317732, 73.21220900334674, 179.9996926415101), (1.0, 1.0, 1.0), "Trim_A_3m72", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (431.75412, 4384.719, 2034.2738), (0.00014400000413784014, 73.21136595029786, -179.99989754715756), (1.0, 1.0, 1.0), "Trim_A_3m73", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (203.94699, 3837.1782, 1714.2728), (0.0002659999358632374, 73.21200442038894, 179.99950822614565), (1.0, 1.0, 1.0), "Trim_A_3m74", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (378.6447, 4416.412, 1714.2738), (0.00014400000413784014, 73.21136595029786, -179.99989754715756), (1.0, 1.0, 1.0), "Trim_A_3m75", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3293.989, 101.53933, 1929.2604), (-0.0003662109214661271, 179.20341588410804, -179.99967898103955), (1.0, 1.0, 1.0), "Trim_A_3m76_400", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3593.9626, 97.36427, 1929.2587), (6.873844291840224e-05, 179.2056223091293, -179.9992828302426), (1.0, 1.0, 1.0), "Trim_A_3m77_401", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2994.0164, 105.70541, 1929.2577), (-0.0003662109214661271, 179.20341588410804, -179.99967898103955), (1.0625, 1.0, 1.0), "Trim_A_3m78_402", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4252.9053, 350.27585, 1929.2622), (-0.0002441406394933131, -160.1464220903048, -179.9996311698021), (1.0, 1.0, 1.0), "Trim_A_3m79_431", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4535.078, 452.17575, 1929.2601), (0.00015709429414617385, -160.1440323855447, -179.9992418488372), (1.0, 1.0, 1.0), "Trim_A_3m80_432", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3970.7317, 248.37054, 1929.2599), (-0.0002441406394933131, -160.1464220903048, -179.9996311698021), (1.0625, 1.0, 1.0), "Trim_A_3m81", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (124.407715, 2726.923, 2034.2728), (0.0002663772911680652, 85.98574820688869, 179.99950822622114), (1.0, 1.0, 1.0), "Trim_A_3m82", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (145.3727, 3026.185, 2034.2728), (0.00020490562390797324, 85.98606161892017, 179.999665320662), (1.0, 1.0, 1.0), "Trim_A_3m83", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (166.34737, 3325.4575, 2034.2738), (0.0001434339549969012, 85.98537718523416, -179.9998975471451), (1.0, 1.0, 1.0), "Trim_A_3m84", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3812.872, 6114.294, 2014.2783), (-0.0007019042364821017, -18.794890684829877, 179.99941260365455), (1.120085, 1.0, 1.0), "Trim_A_3m85", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4130.9805, 6006.0586, 2014.2786), (-0.00015258788101939007, -18.795654457806457, -179.99989754716583), (1.120085, 1.0, 1.0), "Trim_A_3m86", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4449.0947, 5897.8086, 2014.2789), (-0.00030517576576724153, -18.79623362162025, 179.9997677735497), (1.120085, 1.0, 1.0), "Trim_A_3m87", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2740.5505, 6221.5283, 2014.2788), (-0.0007934572178304774, -2.514984484443422, 179.9993647926116), (1.120085, 1.0, 1.0), "Trim_A_3m88", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3076.2454, 6206.808, 2014.2788), (-0.0002441406280897352, -2.5157776113577124, -179.99989754715764), (1.120085, 1.0, 1.0), "Trim_A_3m89", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3411.95, 6192.076, 2014.2787), (-0.0003967285066042216, -2.51635749671752, 179.99976777355786), (1.120085, 1.0, 1.0), "Trim_A_3m90", _folder)
if a: placed += 1
else: skipped += 1

# Batch 8: StaticMesh'NonDest_Boundry_Trim_A' (11 instances)
_mesh_path = "/Game/Art/Assets/Kits/Architecture/Non_D/NonDest_Boundry_Trim_A"
_materials = ['/Game/Art/Assets/Kits/Architecture/Suburbs/Materials/Suburbs_Trim_Sheet_A/MI_Suburbs_Trim_Sheet_A', '/Game/Environments/Materials/MI_Suburbs_Non_Destructible']
_folder = "Reconstruction/BD_BB_Chapter5_BrokenSeal/Meshes"
a = spawn_static_mesh(_mesh_path, _materials, (2265.3381, 279.05957, 2150.0), (0.0, -26.202758530262, 0.0), (1.0, 1.0, 1.0), "NonDest_Boundry_Trim_A_31", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3385.5928, 141.7334, 2150.0), (0.0, -0.353881836392662, 0.0), (1.0, 1.0, 1.0), "NonDest_Boundry_Trim_A10", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3476.0005, 6193.1865, 2128.5837), (6.147170596867892e-05, 177.37824950024523, 4.291041504299845e-05), (1.0, 1.0, 1.0), "NonDest_Boundry_Trim_A11", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (338.83887, 2249.8003, 2150.0), (0.0, -68.6752076836683, 0.0), (1.0, 1.0, 1.0), "NonDest_Boundry_Trim_A2", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (465.6001, 4476.3066, 2150.0), (0.0, -107.05674407043666, 0.0), (1.0, 1.0, 1.0), "NonDest_Boundry_Trim_A3", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2003.0249, 5943.6934, 2150.0), (0.0, -161.3360608690017, 0.0), (1.0, 1.0, 1.0), "NonDest_Boundry_Trim_A4", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4510.888, 5880.92, 2128.581), (0.0, 161.09841413072334, -0.0), (1.0, 1.0, 1.0), "NonDest_Boundry_Trim_A5", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5353.583, 5319.5684, 2150.0), (0.0, 136.30941626323258, -0.0), (1.0, 1.0, 1.0), "NonDest_Boundry_Trim_A6", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5180.817, 947.8823, 2150.0), (0.0, 36.43651956762115, -0.0), (1.0, 1.0, 1.0), "NonDest_Boundry_Trim_A7", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (190.01611, 3327.4458, 2150.0), (0.0, -93.49017194015953, 0.0), (1.0, 1.0, 1.0), "NonDest_Boundry_Trim_A8", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3892.9746, 246.51172, 2150.0), (0.0, 20.03137257083847, -0.0), (1.0, 1.0, 1.0), "NonDest_Boundry_Trim_A9", _folder)
if a: placed += 1
else: skipped += 1

# Batch 9: StaticMesh'NonDest_Floor_Trim_Corner_M' (2 instances)
_mesh_path = "/Game/Art/Assets/Kits/Architecture/Non_D/NonDest_Floor_Trim_Corner_M"
_materials = ['/Game/Art/Assets/Kits/Architecture/Suburbs/Materials/Suburbs_Trim_Sheet_A/MI_Suburbs_Trim_Sheet_A']
_folder = "Reconstruction/BD_BB_Chapter5_BrokenSeal/Meshes"
a = spawn_static_mesh(_mesh_path, _materials, (5221.1123, 4435.047, 795.0), (0.0, 0.00012207030837116422, -0.0), (1.0, 1.0, 1.0), "NonDest_Floor_Trim_Thin_3M_A56", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5221.1123, 4435.047, 795.0), (0.0, 90.00009542133918, -0.0), (1.0, 1.0, 1.0), "NonDest_Floor_Trim_Thin_3M_A57", _folder)
if a: placed += 1
else: skipped += 1

# Batch 10: StaticMesh'NonDest_Floor_Trim_Thin_3M_A' (52 instances)
_mesh_path = "/Game/Art/Assets/Kits/Architecture/Non_D/NonDest_Floor_Trim_Thin_3M_A"
_materials = ['/Game/Art/Assets/Kits/Architecture/Suburbs/Materials/Suburbs_Trim_Sheet_A/MI_Suburbs_Trim_Sheet_A']
_folder = "Reconstruction/BD_BB_Chapter5_BrokenSeal/Meshes"
a = spawn_static_mesh(_mesh_path, _materials, (2545.7554, 440.839, 1390.05), (0.0, -110.000392111319, 0.0), (1.0, 1.0, 1.0), "NonDest_Boundry_3m_Trim_A34", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4416.6865, 1308.8899, 1390.0), (0.0, -159.99985532110392, 0.0), (1.125, 1.0, 1.0), "NonDest_Boundry_3m_Trim_A46", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4627.8135, 1071.6943, 1390.0), (0.0, 130.00011956088582, -0.0), (1.125, 1.0, 1.0), "NonDest_Boundry_3m_Trim_A47", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4843.1475, 815.07007, 1390.0), (0.0, 130.00011956088582, -0.0), (1.125, 1.0, 1.0), "NonDest_Boundry_3m_Trim_A48", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5058.4824, 558.44543, 1390.0), (0.0, 130.00011956088582, -0.0), (1.125, 1.0, 1.0), "NonDest_Boundry_3m_Trim_A49", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4101.8896, 1194.3124, 1390.0), (0.0, -159.99985532110392, 0.0), (1.125, 1.0, 1.0), "NonDest_Boundry_3m_Trim_A7", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2750.971, 1004.65405, 1390.05), (0.0, -110.000392111319, 0.0), (1.0, 1.0, 1.0), "NonDest_Boundry_3m_Trim_A8", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2648.3633, 722.7459, 1390.05), (0.0, -110.000392111319, 0.0), (1.0, 1.0, 1.0), "NonDest_Boundry_3m_Trim_A9", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (860.031, 3202.0864, 1442.1298), (0.0, -90.00002735739477, 0.0), (1.0, 1.0, 1.0), "NonDest_Floor_Trim_Thin_3M_A10", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (860.031, 3502.0864, 1442.1298), (0.0, -90.00002735739477, 0.0), (1.0, 1.0, 1.0), "NonDest_Floor_Trim_Thin_3M_A11", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (596.8738, 2631.5479, 1395.0), (0.0, 25.00001037024192, -0.0), (1.0420191, 1.0, 1.0), "NonDest_Floor_Trim_Thin_3M_A12_482", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1017.759, 1872.4341, 795.0), (0.0, -154.6876632220656, 0.0), (1.0, 1.0, 1.0), "NonDest_Floor_Trim_Thin_3M_A13_108", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1288.9558, 2000.7, 795.0), (0.0, -154.6876632220656, 0.0), (1.0, 1.0, 1.0), "NonDest_Floor_Trim_Thin_3M_A14", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (746.5618, 1744.1682, 795.0), (0.0, -154.6876632220656, 0.0), (1.0, 1.0, 1.0), "NonDest_Floor_Trim_Thin_3M_A15", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1393.7908, 1781.858, 790.0), (0.0, 129.9999919829063, -0.0), (1.0, 1.0, 1.0), "NonDest_Floor_Trim_Thin_3M_A16_113", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1586.6272, 1552.0446, 790.0), (0.0, 129.9999919829063, -0.0), (1.0, 1.0, 1.0), "NonDest_Floor_Trim_Thin_3M_A17", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1779.4636, 1322.2311, 790.0), (0.0, 129.9999919829063, -0.0), (1.0, 1.0, 1.0), "NonDest_Floor_Trim_Thin_3M_A18", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1856.3688, 1104.0807, 795.0), (0.0, 69.0824702710149, -0.0), (1.0, 1.0, 1.0), "NonDest_Floor_Trim_Thin_3M_A19", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1749.2598, 823.8523, 795.0), (0.0, 69.08182174602305, -0.0), (1.0, 1.0, 1.0), "NonDest_Floor_Trim_Thin_3M_A20_120", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1642.1506, 543.62427, 795.0), (0.0, 69.08182174602305, -0.0), (1.0, 1.0, 1.0), "NonDest_Floor_Trim_Thin_3M_A21_122", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (313.55704, 2499.4336, 1395.0), (0.0, 25.00001037024192, -0.0), (1.0420191, 1.0, 1.0), "NonDest_Floor_Trim_Thin_3M_A22", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1972.2997, 1092.4177, 790.0), (0.0, 129.9999919829063, -0.0), (1.0, 1.0, 1.0), "NonDest_Floor_Trim_Thin_3M_A23", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5637.739, 1613.2306, 795.0), (0.0, -50.626098778534775, 0.0), (1.0, 1.0, 1.0), "NonDest_Floor_Trim_Thin_3M_A28", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5447.4233, 1845.136, 795.0), (0.0, -50.626098778534775, 0.0), (1.0, 1.0, 1.0), "NonDest_Floor_Trim_Thin_3M_A29", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5257.1084, 2077.0427, 795.0), (0.0, -50.626098778534775, 0.0), (1.0, 1.0, 1.0), "NonDest_Floor_Trim_Thin_3M_A30", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5117.84, 2286.1572, 795.0), (0.0, -50.626098778534775, 0.0), (1.0, 1.0, 1.0), "NonDest_Floor_Trim_Thin_3M_A31", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5221.1123, 2635.0469, 795.0), (0.0, -89.99993822608693, 0.0), (1.0, 1.0, 1.0), "NonDest_Floor_Trim_Thin_3M_A32", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5221.1123, 2335.0469, 795.0), (0.0, -89.99993822608693, 0.0), (1.0, 1.0, 1.0), "NonDest_Floor_Trim_Thin_3M_A33_160", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5221.1123, 2935.0469, 795.0), (0.0, -89.99993822608693, 0.0), (1.0, 1.0, 1.0), "NonDest_Floor_Trim_Thin_3M_A34_162", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5221.1123, 3235.0469, 795.0), (0.0, -89.99993822608693, 0.0), (1.0, 1.0, 1.0), "NonDest_Floor_Trim_Thin_3M_A35_164", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5221.1123, 3535.0469, 795.0), (0.0, -89.99993822608693, 0.0), (1.0, 1.0, 1.0), "NonDest_Floor_Trim_Thin_3M_A36_166", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5221.1123, 3835.0469, 795.0), (0.0, -89.99993822608693, 0.0), (1.0, 1.0, 1.0), "NonDest_Floor_Trim_Thin_3M_A37_168", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5221.1123, 4135.047, 795.0), (0.0, -89.99993822608693, 0.0), (1.0, 1.0, 1.0), "NonDest_Floor_Trim_Thin_3M_A38", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5221.1123, 4435.047, 795.0), (0.0, -89.99993822608693, 0.0), (1.0, 1.0, 1.0), "NonDest_Floor_Trim_Thin_3M_A39", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5327.9453, 4769.626, 795.0), (0.0, -135.62515674238472, 0.0), (1.0, 1.0, 1.0), "NonDest_Floor_Trim_Thin_3M_A40_173", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5542.3784, 4979.43, 795.0), (0.0, -135.62515674238472, 0.0), (1.0, 1.0, 1.0), "NonDest_Floor_Trim_Thin_3M_A41", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4637.666, 5340.542, 1392.5934), (0.0, 44.374722391312496, -0.0), (1.0, 1.0, 1.0), "NonDest_Floor_Trim_Thin_3M_A42_177", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4423.231, 5130.738, 1392.5934), (0.0, 44.374722391312496, -0.0), (1.0, 1.0, 1.0), "NonDest_Floor_Trim_Thin_3M_A43", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4852.101, 5550.3467, 1397.0), (0.0, 44.374722391312496, -0.0), (1.0, 1.0, 1.0), "NonDest_Floor_Trim_Thin_3M_A44", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2548.9912, 6105.578, 1395.0), (0.0, -70.3125629343707, 0.0), (1.0, 1.0, 1.0), "NonDest_Floor_Trim_Thin_3M_A45_182", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2650.058, 5823.115, 1395.0), (0.0, -70.3125629343707, 0.0), (1.0, 1.0, 1.0), "NonDest_Floor_Trim_Thin_3M_A46", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2751.1248, 5540.6523, 1395.0), (0.0, -70.3125629343707, 0.0), (1.0, 1.0, 1.0), "NonDest_Floor_Trim_Thin_3M_A47", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1847.6794, 5408.966, 795.0), (0.0, 109.68755816276153, -0.0), (1.0, 1.0, 1.0), "NonDest_Floor_Trim_Thin_3M_A48_187", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1948.7465, 5126.503, 795.0), (0.0, 109.68755816276153, -0.0), (1.0, 1.0, 1.0), "NonDest_Floor_Trim_Thin_3M_A49", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3855.5618, 5416.1284, 1392.5934), (0.0, -25.625395717071214, 0.0), (1.0, 1.0, 1.0), "NonDest_Floor_Trim_Thin_3M_A50", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4126.054, 5286.3833, 1392.5934), (0.0, -25.625395717071214, 0.0), (1.0, 1.0, 1.0), "NonDest_Floor_Trim_Thin_3M_A51", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3564.143, 5418.2075, 1392.5934), (0.0, -0.6254272492242167, 0.0), (1.0, 1.0, 1.0), "NonDest_Floor_Trim_Thin_3M_A52", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1026.4464, 4544.4946, 791.5534), (0.0, -25.937437576359322, 0.0), (1.0, 1.0, 1.0), "NonDest_Floor_Trim_Thin_3M_A53", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (756.6646, 4675.712, 791.5534), (0.0, -25.937437576359322, 0.0), (1.0, 1.0, 1.0), "NonDest_Floor_Trim_Thin_3M_A54", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (499.2754, 4800.9, 800.0), (0.0, -25.937437576359322, 0.0), (1.0, 1.0, 1.0), "NonDest_Floor_Trim_Thin_3M_A55", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (578.4382, 3770.9355, 1395.0), (0.0, 154.99993893929087, -0.0), (1.0, 1.0, 1.0), "NonDest_Floor_Trim_Thin_3M_A8_471", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (850.3303, 3644.15, 1395.0), (0.0, 154.99993893929087, -0.0), (1.0, 1.0, 1.0), "NonDest_Floor_Trim_Thin_3M_A9", _folder)
if a: placed += 1
else: skipped += 1

# Batch 11: StaticMesh'NonDest_Pillar_1_5M_A' (3 instances)
_mesh_path = "/Game/Art/Assets/Kits/Architecture/Non_D/NonDest_Pillar_1_5M_A"
_materials = ['/Game/Art/Assets/Kits/Architecture/Suburbs/Materials/Suburbs_Trim_Sheet_A/MI_Suburbs_Trim_Sheet_A']
_folder = "Reconstruction/BD_BB_Chapter5_BrokenSeal/Meshes"
a = spawn_static_mesh(_mesh_path, _materials, (4860.0, 4710.0, 900.0), (0.0, -50.00006299960901, 0.0), (1.0, 1.0, 1.0), "NonDest_Pillar_1_5M_A_237", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1166.1736, 4167.744, 890.0), (0.0, 65.00001278016504, -0.0), (1.0, 1.0, 1.0), "NonDest_Pillar_1_5M_A2_317", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2394.785, 5305.925, 990.0), (0.0, -159.99981473322237, 0.0), (1.0, 1.0, 1.09375), "NonDest_Pillar_3M_B3", _folder)
if a: placed += 1
else: skipped += 1

# Batch 12: StaticMesh'NonDest_Pillar_25M_A' (9 instances)
_mesh_path = "/Game/Art/Assets/Kits/Architecture/Non_D/NonDest_Pillar_25M_A"
_materials = ['/Game/Art/Assets/Kits/Architecture/Suburbs/Materials/Suburbs_Trim_Sheet_A/MI_Suburbs_Trim_Sheet_A']
_folder = "Reconstruction/BD_BB_Chapter5_BrokenSeal/Meshes"
a = spawn_static_mesh(_mesh_path, _materials, (4655.0, 2880.0, 940.0), (0.0, 0.0, -0.0), (1.0, 1.0, 1.0), "NonDest_Pillar_25M_A_184", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4985.0, 2880.0, 780.0), (0.0, 0.0, -0.0), (1.0, 1.0, 1.0), "NonDest_Pillar_25M_A2", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4985.0, 3525.0, 780.0), (0.0, 0.0, -0.0), (1.0, 1.0, 1.0), "NonDest_Pillar_25M_A3", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4655.0, 3525.0, 940.0), (0.0, 0.0, -0.0), (1.0, 1.0, 1.0), "NonDest_Pillar_25M_A4", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1275.5112, 4421.118, 740.0), (0.0, -74.9999306705529, 0.0), (1.0, 1.0, 1.0), "NonDest_Pillar_25M_A5_365", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1357.615, 4443.1187, 740.0), (0.0, -74.9999306705529, 0.0), (1.0, 1.0, 1.0), "NonDest_Pillar_25M_A6", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2439.4702, 1072.0447, 985.0), (0.0, -20.000060948281234, 0.0), (1.0, 1.0, 1.0), "NonDest_Pillar_3M_B2_105", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1948.4313, 5143.4644, 805.0), (0.0, -159.99981473322237, 0.0), (1.0, 1.0, 0.90625), "NonDest_Pillar_3M_B7_257", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1977.5032, 5063.592, 805.0), (0.0, -159.99981473322237, 0.0), (1.0, 1.0, 0.90625), "NonDest_Pillar_3M_B8", _folder)
if a: placed += 1
else: skipped += 1

# Batch 13: StaticMesh'NonDest_Pillar_3M_B' (4 instances)
_mesh_path = "/Game/Art/Assets/Kits/Architecture/Non_D/NonDest_Pillar_3M_B"
_materials = ['/Game/Art/Assets/Kits/Architecture/Suburbs/Materials/Suburbs_Trim_Sheet_A/MI_Suburbs_Trim_Sheet_A']
_folder = "Reconstruction/BD_BB_Chapter5_BrokenSeal/Meshes"
a = spawn_static_mesh(_mesh_path, _materials, (4648.214, 1536.1698, 940.0), (0.0, 40.00006853942215, -0.0), (1.0, 1.0625, 1.0), "NonDest_Pillar_3M_B_33", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1058.426, 2495.641, 985.0), (0.0, 110.00014960145684, -0.0), (1.0, 1.0, 0.875), "NonDest_Pillar_3M_B10_326", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4647.0713, 4947.0713, 935.0), (0.0, -44.999970287262066, 0.0), (1.0, 1.03125, 1.09375), "NonDest_Pillar_3M_B6_229", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1002.3422, 3880.5652, 985.0), (0.0, 65.00011819485806, -0.0), (1.0, 1.0, 0.9375), "NonDest_Pillar_3M_B9_310", _folder)
if a: placed += 1
else: skipped += 1

# Batch 14: StaticMesh'NonDest_Pillar_4M_A' (6 instances)
_mesh_path = "/Game/Art/Assets/Kits/Architecture/Non_D/NonDest_Pillar_4M_A"
_materials = ['/Game/Art/Assets/Kits/Architecture/Suburbs/Materials/Suburbs_Trim_Sheet_A/MI_Suburbs_Trim_Sheet_A']
_folder = "Reconstruction/BD_BB_Chapter5_BrokenSeal/Meshes"
a = spawn_static_mesh(_mesh_path, _materials, (4392.9673, 1325.4412, 990.0), (0.0, 35.00008473423376, -0.0), (1.0, 1.0, 1.0), "NonDest_Pillar_4M_A_23", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3791.0063, 1099.6821, 990.0), (0.0, 20.00127400040344, -0.0), (1.0, 1.0, 1.0), "NonDest_Pillar_4M_A2", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4330.0, 2905.0, 730.0), (0.0, -90.00005166594045, 0.0), (1.0, 1.0, 1.0), "NonDest_Pillar_4M_A3_174", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4330.0, 3530.0, 730.0), (0.0, -90.00005166594045, 0.0), (1.0, 1.0, 1.0), "NonDest_Pillar_4M_A4", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3838.5586, 5398.66, 990.0), (0.0, 170.00006180583077, -0.0), (1.0, 1.0, 1.0), "NonDest_Pillar_4M_A5", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4423.8447, 5132.6475, 990.0), (0.0, 155.00131671641822, -0.0), (1.0, 1.0, 1.0), "NonDest_Pillar_4M_A6", _folder)
if a: placed += 1
else: skipped += 1

# Batch 15: StaticMesh'NonDest_Pillar_5M_A' (6 instances)
_mesh_path = "/Game/Art/Assets/Kits/Architecture/Non_D/NonDest_Pillar_5M_A"
_materials = ['/Game/Art/Assets/Kits/Architecture/Suburbs/Materials/Suburbs_Trim_Sheet_A/MI_Suburbs_Trim_Sheet_A']
_folder = "Reconstruction/BD_BB_Chapter5_BrokenSeal/Meshes"
a = spawn_static_mesh(_mesh_path, _materials, (1500.0015, 3540.0, 980.0), (0.0, -89.99999818714215, 0.0), (1.0, 1.0, 1.0), "NonDest_Pillar_6M_A13", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1500.0, 2835.0, 980.0), (0.0, -89.99999818714215, 0.0), (1.0, 1.0, 1.0), "NonDest_Pillar_6M_A14", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3002.692, 64.01821, 1405.005), (0.00016392453445475934, 0.9119264014364518, 0.00013114991691793372), (1.0666667, 1.0666667, 1.0098963), "NonDest_Pillar_6M_A19", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3277.6577, 68.39508, 1405.0056), (0.00016392453445475934, 0.9119264014364518, 0.00013114991691793372), (1.0666667, 1.0666667, 1.0098963), "NonDest_Pillar_6M_A20", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3993.5508, 212.42383, 1400.0073), (0.00019124528150939044, 21.56108906717131, 0.00019015496313787075), (1.066667, 1.066667, 1.0299153), "NonDest_Pillar_6M_A21", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4249.311, 313.49832, 1405.0074), (0.00019124528150939044, 21.56108906717131, 0.00019015496313787075), (1.066667, 1.066667, 1.009896), "NonDest_Pillar_6M_A22", _folder)
if a: placed += 1
else: skipped += 1

# Batch 16: StaticMesh'NonDest_Pillar_6M_A' (22 instances)
_mesh_path = "/Game/Art/Assets/Kits/Architecture/Non_D/NonDest_Pillar_6M_A"
_materials = ['/Game/Art/Assets/Kits/Architecture/Suburbs/Materials/Suburbs_Trim_Sheet_A/MI_Suburbs_Trim_Sheet_A']
_folder = "Reconstruction/BD_BB_Chapter5_BrokenSeal/Meshes"
a = spawn_static_mesh(_mesh_path, _materials, (4999.5806, 758.92035, 1350.0), (0.0, 38.37404833444936, -0.0), (1.0, 1.0, 0.9375), "NonDest_Pillar_6M_A_81", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5198.2593, 5506.881, 1455.0), (0.0, -45.0000865484073, 0.0), (1.0, 1.0, 0.90625), "NonDest_Pillar_6M_A10", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2309.8694, 6089.0947, 1455.0), (0.0, 20.000045392948085, -0.0), (1.0, 1.0, 1.03125), "NonDest_Pillar_6M_A11_288", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2051.4536, 5995.0386, 1455.0), (0.0, 20.000045392948085, -0.0), (1.0, 1.0, 1.03125), "NonDest_Pillar_6M_A12", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (301.50772, 2271.449, 1455.0), (0.0, -70.00006109847311, 0.0), (1.0, 1.0, 0.9375), "NonDest_Pillar_6M_A15_345", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (392.1428, 2022.4303, 1455.0), (0.0, -70.00006109847311, 0.0), (1.0, 1.0, 0.9375), "NonDest_Pillar_6M_A16", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (405.6815, 4400.1763, 1455.0), (0.0, 75.00009718089603, -0.0), (1.0, 1.0, 0.9375), "NonDest_Pillar_6M_A17_355", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (335.80078, 4139.3774, 1455.0), (0.0, 75.00009718089603, -0.0), (1.0, 1.0, 0.9375), "NonDest_Pillar_6M_A18", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5211.2485, 926.5408, 1354.8387), (0.0, 37.87684735687586, -0.0), (1.0, 1.0, 0.9375), "NonDest_Pillar_6M_A2", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (137.50223, 3334.767, 1455.0), (0.0, 87.7739805461376, -0.0), (1.0, 1.0, 0.9375), "NonDest_Pillar_6M_A23", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (127.01769, 3064.972, 1455.0), (0.0, 87.7739805461376, -0.0), (1.0, 1.0, 0.9375), "NonDest_Pillar_6M_A24", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4452.207, 5932.061, 1395.0), (0.0, -19.578002083804968, 0.0), (1.0, 1.0, 1.0112478), "NonDest_Pillar_6M_A25", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4200.852, 6016.147, 1395.0), (0.0, -19.578002083804968, 0.0), (1.0, 1.0, 1.0112478), "NonDest_Pillar_6M_A26", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3405.335, 6225.8276, 1394.9999), (-6.10351649106485e-05, -3.2981262846117354, -6.103516338014431e-05), (1.0, 1.0, 1.011248), "NonDest_Pillar_6M_A27", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3139.9114, 6226.0957, 1395.0001), (-6.10351649106485e-05, -3.2981262846117354, -6.103516338014431e-05), (1.0, 1.0, 1.011248), "NonDest_Pillar_6M_A28", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2820.0, 4930.0, 810.0), (0.0, 0.0, -0.0), (1.0, 1.0, 1.0), "NonDest_Pillar_6M_A3_129", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3525.0, 4930.0, 810.0), (0.0, 0.0, -0.0), (1.0, 1.0, 1.0), "NonDest_Pillar_6M_A4", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1960.0, 385.0, 1345.0), (0.0, -24.088102982188733, 0.0), (1.0, 1.0, 0.9375), "NonDest_Pillar_6M_A5_136", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2211.053, 272.76123, 1345.0), (0.0, -24.088102982188733, 0.0), (1.0, 1.0, 0.9375), "NonDest_Pillar_6M_A6", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2820.0, 1505.0, 810.0), (0.0, 0.0, -0.0), (1.0, 1.0, 1.0), "NonDest_Pillar_6M_A7", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3525.0, 1505.0, 810.0), (0.0, 0.0, -0.0), (1.0, 1.0, 1.0), "NonDest_Pillar_6M_A8", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5389.1777, 5323.0327, 1455.0), (0.0, -45.0000865484073, 0.0), (1.0, 1.0, 0.90625), "NonDest_Pillar_6M_A9_274", _folder)
if a: placed += 1
else: skipped += 1

# Batch 17: StaticMesh'NonDest_Wall_3M_A' (1 instances)
_mesh_path = "/Game/Art/Assets/Kits/Architecture/Non_D/NonDest_Wall_3M_A"
_materials = ['/Game/Environments/Materials/MI_Suburbs_Non_Destructible', '/Game/Art/Assets/Kits/Architecture/Suburbs/Materials/Suburbs_Trim_Sheet_A/MI_Suburbs_Trim_Sheet_A']
_folder = "Reconstruction/BD_BB_Chapter5_BrokenSeal/Meshes"
a = spawn_static_mesh(_mesh_path, _materials, (2471.4194, 1069.3864, 865.0), (0.0, -15.000058335092751, 0.0), (1.0, 1.0, 1.0), "NonDest_Wall_3M_A2", _folder)
if a: placed += 1
else: skipped += 1

# Batch 18: StaticMesh'NonDest_Wall_3M_B' (2 instances)
_mesh_path = "/Game/Art/Assets/Kits/Architecture/Non_D/NonDest_Wall_3M_B"
_materials = ['/Game/Environments/Materials/MI_Suburbs_Non_Destructible', '/Game/Art/Assets/Kits/Architecture/Suburbs/Materials/Suburbs_Trim_Sheet_A/MI_Suburbs_Trim_Sheet_A']
_folder = "Reconstruction/BD_BB_Chapter5_BrokenSeal/Meshes"
a = spawn_static_mesh(_mesh_path, _materials, (4630.0, 2890.0, 890.0), (0.0, 179.9998224150775, -0.0), (1.0, 1.0, 1.0), "NonDest_Wall_3M_B2_171", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4344.999, 3535.0002, 890.0006), (0.0001092830267698799, -0.0005493164071481526, -0.00015258789367459904), (1.0, 1.0, 1.0), "NonDest_Wall_3M_B3_203", _folder)
if a: placed += 1
else: skipped += 1

# Batch 19: StaticMesh'NonDest_Wall_6x4M_A' (3 instances)
_mesh_path = "/Game/Art/Assets/Kits/Architecture/Non_D/NonDest_Wall_6x4M_A"
_materials = ['/Game/Art/Assets/Kits/Architecture/Suburbs/Materials/Suburbs_Trim_Sheet_A/MI_Suburbs_Trim_Sheet_A', '/Game/Environments/Materials/MI_Suburbs_Non_Destructible']
_folder = "Reconstruction/BD_BB_Chapter5_BrokenSeal/Meshes"
a = spawn_static_mesh(_mesh_path, _materials, (4089.19, 1204.5299, 1005.0), (0.0, 20.00007171735876, -0.0), (1.0, 1.0, 1.0), "NonDest_Wall_6x4M_A_5", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4315.0, 3220.0, 790.0), (0.0, 90.00011648875932, -0.0), (1.0, 1.0, 1.0), "NonDest_Wall_6x4M_A2_168", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4138.859, 5269.3555, 1005.0), (0.0, 155.0000485549448, -0.0), (1.0, 1.0, 1.0), "NonDest_Wall_6x4M_A3", _folder)
if a: placed += 1
else: skipped += 1

# Batch 20: StaticMesh'SM_AR_City_Column_B_Half_Base' (6 instances)
_mesh_path = "/Game/Art/Assets/Kits/Architecture/Suburbs/SM_AR_City_Column_B_Half_Base"
_materials = ['/Game/Art/Assets/Kits/Architecture/Suburbs/Materials/SM_AR_City_Column_B/MI_SM_AR_City_Column_B_Base']
_folder = "Reconstruction/BD_BB_Chapter5_BrokenSeal/Meshes"
a = spawn_static_mesh(_mesh_path, _materials, (5128.674, 4437.4307, 769.99927), (0.00016400000398570348, 140.00065532678144, -3.0517578568703085e-05), (2.0, 2.0, 2.0), "SM_AR_City_Column_B_Half_Base17_56", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5128.674, 4437.4307, 769.99927), (-9.155271887131937e-05, -39.99969510067033, 7.799999849851432e-05), (2.0, 2.0, 2.0), "SM_AR_City_Column_B_Half_Base18_57", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5128.6753, 4437.4307, 1250.0024), (0.00019807541211988905, 140.001596443585, -179.99950822617865), (2.0, 2.0, 2.0), "SM_AR_City_Column_B_Half_Base19_60", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5128.6753, 4437.4307, 1250.0024), (-9.155272232357931e-05, -39.99968961336728, -179.99988388676314), (2.0, 2.0, 2.0), "SM_AR_City_Column_B_Half_Base20_61", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4911.5723, 1709.259, 790.0266), (0.0009972076914027278, 39.24201080881515, 0.0003364661985831498), (2.0, 2.1875, 2.0), "SM_AR_City_Column_B_Half_Base33", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4911.5723, 1709.259, 790.0266), (-0.0007629395042684387, -140.75965486300126, -3.05175941031026e-05), (2.0, 2.1875, 2.0), "SM_AR_City_Column_B_Half_Base34", _folder)
if a: placed += 1
else: skipped += 1

# Batch 21: StaticMesh'SM_AR_City_Column_B_Half_Shaft' (2 instances)
_mesh_path = "/Game/Art/Assets/Kits/Architecture/Suburbs/SM_AR_City_Column_B_Half_Shaft"
_materials = ['/Game/Art/Assets/Kits/Architecture/Suburbs/Materials/SM_AR_City_Column_B/MI_SM_AR_City_Column_B_Shaft']
_folder = "Reconstruction/BD_BB_Chapter5_BrokenSeal/Meshes"
a = spawn_static_mesh(_mesh_path, _materials, (5128.674, 4437.4307, 970.00244), (-9.155271887131937e-05, -39.99969510067033, 7.799999849851432e-05), (2.0, 2.0, 0.8125), "SM_AR_City_Column_B_Half_Shaft10_59", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5128.674, 4437.4307, 970.00244), (0.00016400000398570348, 140.00065532678144, -3.0517578568703085e-05), (2.0, 2.0, 0.8125), "SM_AR_City_Column_B_Half_Shaft9_58", _folder)
if a: placed += 1
else: skipped += 1

# Batch 22: StaticMesh'SM_BrokenSeal' (1 instances)
_mesh_path = "/Game/Art/Assets/Kits/Architecture/Suburbs/SM_BrokenSeal"
_materials = ['/Game/Art/Assets/Kits/Architecture/Deep/Materials/Deep_TrimSheet/MI_Deep_TrimSheet', '/Game/Art/Assets/Kits/Architecture/Suburbs/Destructable/Materials/MI_Suburbs_Wall_Non_Dest', '/Game/Art/Assets/Kits/Architecture/Suburbs/Destructable/Materials/MI_ProcRock_Quarry_2x2x5_A_DMG_A']
_folder = "Reconstruction/BD_BB_Chapter5_BrokenSeal/Meshes"
a = spawn_static_mesh(_mesh_path, _materials, (3156.28, 3246.9963, 758.4425), (0.0, 90.0001164887758, -0.0), (1.1972655, 1.1972655, 1.1972655), "SM_BrokenSeal_3", _folder)
if a: placed += 1
else: skipped += 1

# Batch 23: StaticMesh'SM_BrokenSeal_Stairs' (2 instances)
_mesh_path = "/Game/Art/Assets/Kits/Architecture/Suburbs/SM_BrokenSeal_Stairs"
_materials = ['/Game/Art/Assets/Kits/Architecture/Suburbs/Materials/Stairs_Medium_C_NonDest/MI_Stairs_Medium_C_NonDes_Suburbs']
_folder = "Reconstruction/BD_BB_Chapter5_BrokenSeal/Meshes"
a = spawn_static_mesh(_mesh_path, _materials, (2450.7927, 3244.9968, 857.3064), (0.0, 6.103515418554748e-05, -0.0), (0.8125, 0.8125, 0.8125), "SM_BrokenSeal_Stairs_7", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3912.6792, 3244.9937, 857.3064), (0.0, -179.99998633961752, -0.0), (0.8125, 0.8125, 0.8125), "SM_BrokenSeal_Stairs1", _folder)
if a: placed += 1
else: skipped += 1

# Batch 24: StaticMesh'Suburb_Stairs_Trim_3M_B' (8 instances)
_mesh_path = "/Game/Art/Assets/Kits/Architecture/Suburbs/Suburb_Stairs_Trim_3M_B"
_materials = ['/Game/Art/Assets/Kits/Architecture/Suburbs/Materials/Suburb_Stairs_Trim/MI_Suburb_Stairs_Trim_3M']
_folder = "Reconstruction/BD_BB_Chapter5_BrokenSeal/Meshes"
a = spawn_static_mesh(_mesh_path, _materials, (2357.174, 5989.0146, 1024.2734), (0.0, 18.558274250963276, -0.0), (1.0, 1.0, 1.0), "Suburb_Stairs_Trim_3M_B10", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (323.54883, 3801.0964, 1024.2734), (0.0, 73.21170309170374, -0.0), (1.0, 1.0, 1.0), "Suburb_Stairs_Trim_3M_B15", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (392.37793, 2303.205, 1024.2734), (0.0, 109.37948815157466, -0.0), (1.0, 1.0, 1.0), "Suburb_Stairs_Trim_3M_B16", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2275.3328, 343.79736, 915.0), (0.0, 154.35291837231205, -0.0), (1.0, 1.0, 1.0), "Suburb_Stairs_Trim_3M_B2", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2545.7627, 213.93555, 915.0), (0.0, 154.35109281374284, -0.0), (1.0, 1.0, 1.0), "Suburb_Stairs_Trim_3M_B3", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4927.3003, 830.33154, 1024.2734), (0.0, -142.04311640445187, 0.0), (1.0, 1.0, 1.0), "Suburb_Stairs_Trim_3M_B4", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5163.852, 1014.8423, 1024.2734), (0.0, -142.04159257239658, 0.0), (1.0, 1.0, 1.0), "Suburb_Stairs_Trim_3M_B5", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4894.612, 5659.009, 1024.2734), (0.0, -44.07171660902188, 0.0), (1.0, 1.0, 1.0), "Suburb_Stairs_Trim_3M_B9", _folder)
if a: placed += 1
else: skipped += 1

# Batch 25: StaticMesh'Suburbs_Column_Large_A_Base' (59 instances)
_mesh_path = "/Game/Art/Assets/Kits/Architecture/Suburbs/Suburbs_Column_Large_A_Base"
_materials = ['/Game/Art/Assets/Kits/Architecture/Suburbs/Materials/Suburbs_Column_Large/MI_Suburbs_Column_Large_A_Base']
_folder = "Reconstruction/BD_BB_Chapter5_BrokenSeal/Meshes"
a = spawn_static_mesh(_mesh_path, _materials, (5970.0005, 3699.4397, 900.0), (-0.0, -179.99976777357483, -0.0), (1.0, 1.0, 1.0), "Suburbs_Column_Large_A_Base_13", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2746.591, 6162.9434, 1350.0), (-0.0, -90.31197610055823, -0.0), (1.0, 1.0, 1.0), "Suburbs_Column_Large_A_Base_50", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4879.366, 5801.09, 1365.0), (0.0, 95.00028227170726, -0.0), (1.0, 1.0, 1.0), "Suburbs_Column_Large_A_Base10", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4879.366, 5801.09, 1365.0), (0.0, -175.00041561292193, 0.0), (1.0, 1.0, 1.0), "Suburbs_Column_Large_A_Base11", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4879.366, 5801.09, 1365.0), (0.0, -84.999812013364, 0.0), (1.0, 1.0, 1.0), "Suburbs_Column_Large_A_Base12", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5665.03, 4962.263, 815.0), (0.0, 75.00012450645619, -0.0), (1.0, 1.0, 1.0), "Suburbs_Column_Large_A_Base13", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5665.03, 4962.263, 815.0), (0.0, 165.00021599688904, -0.0), (1.0, 1.0, 1.0), "Suburbs_Column_Large_A_Base14", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5665.03, 4962.263, 815.0), (0.0, -105.00036900992035, 0.0), (1.0, 1.0, 1.0), "Suburbs_Column_Large_A_Base15", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5665.03, 4962.263, 815.0), (0.0, -14.999815811835294, 0.0), (1.0, 1.0, 1.0), "Suburbs_Column_Large_A_Base16", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1633.7715, 5838.3867, 865.0), (0.0, 5.000282396002133, -0.0), (1.0, 1.0, 1.0), "Suburbs_Column_Large_A_Base17", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1633.7715, 5838.3867, 865.0), (0.0, 95.00028227170726, -0.0), (1.0, 1.0, 1.0), "Suburbs_Column_Large_A_Base18", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1633.7715, 5838.3867, 865.0), (0.0, -175.00041561292193, 0.0), (1.0, 1.0, 1.0), "Suburbs_Column_Large_A_Base19", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5970.0005, 3699.4397, 900.0), (-0.0, -89.99963031845931, -0.0), (1.0, 1.0, 1.0), "Suburbs_Column_Large_A_Base2_14", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2746.591, 6162.9434, 1350.0), (-0.0, -0.3118599960683572, -0.0), (1.0, 1.0, 1.0), "Suburbs_Column_Large_A_Base2_51", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1633.7715, 5838.3867, 865.0), (0.0, -84.999812013364, 0.0), (1.0, 1.0, 1.0), "Suburbs_Column_Large_A_Base20", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (556.5371, 4795.5415, 795.0), (0.0, 5.000282396002133, -0.0), (1.0, 1.0, 1.0), "Suburbs_Column_Large_A_Base21", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (556.5371, 4795.5415, 795.0), (0.0, 95.00028227170726, -0.0), (1.0, 1.0, 1.0), "Suburbs_Column_Large_A_Base22", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (556.5371, 4795.5415, 795.0), (0.0, -175.00041561292193, 0.0), (1.0, 1.0, 1.0), "Suburbs_Column_Large_A_Base23", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (556.5371, 4795.5415, 795.0), (0.0, -84.999812013364, 0.0), (1.0, 1.0, 1.0), "Suburbs_Column_Large_A_Base24", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5970.0005, 3699.4397, 900.0), (-0.0, -0.00019124526767201947, -0.0), (1.0, 1.0, 1.0), "Suburbs_Column_Large_A_Base3_15", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2746.591, 6162.9434, 1350.0), (0.0, 89.68761000310737, -0.0), (1.0, 1.0, 1.0), "Suburbs_Column_Large_A_Base3_52", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4639.954, 516.084, 1395.0), (0.0, -9.999755981163082, 0.0), (1.0, 1.0, 1.0), "Suburbs_Column_Large_A_Base33", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4639.954, 516.084, 1395.0), (0.0, 80.00024381112391, -0.0), (1.0, 1.0, 1.0), "Suburbs_Column_Large_A_Base34", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4639.954, 516.084, 1395.0), (0.0, 169.99957079689236, -0.0), (1.0, 1.0, 1.0), "Suburbs_Column_Large_A_Base35", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4639.954, 516.084, 1395.0), (0.0, -99.99983954701518, 0.0), (1.0, 1.0, 1.0), "Suburbs_Column_Large_A_Base36", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (145.53711, 2663.7522, 1385.0), (0.0, -29.999758042420478, 0.0), (1.0, 1.0, 1.0), "Suburbs_Column_Large_A_Base37", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (145.53711, 2663.7522, 1385.0), (0.0, 60.000457648051665, -0.0), (1.0, 1.0, 1.0), "Suburbs_Column_Large_A_Base38", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (145.53711, 2663.7522, 1385.0), (0.0, 149.99968089611104, -0.0), (1.0, 1.0, 1.0), "Suburbs_Column_Large_A_Base39", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5970.0005, 3699.4397, 900.0), (0.0, 90.00013269448853, 0.0), (1.0, 1.0, 1.0), "Suburbs_Column_Large_A_Base4_16", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2746.591, 6162.9434, 1350.0), (0.0, 179.68797944641008, 0.0), (1.0, 1.0, 1.0), "Suburbs_Column_Large_A_Base4_53", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (145.53711, 2663.7522, 1385.0), (0.0, -119.9998794919872, 0.0), (1.0, 1.0, 1.0), "Suburbs_Column_Large_A_Base40", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (557.7261, 1606.8867, 795.0), (0.0, 75.00031946796146, -0.0), (1.0, 1.0, 1.0), "Suburbs_Column_Large_A_Base41", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (557.7261, 1606.8867, 795.0), (0.0, 165.00032540974598, -0.0), (1.0, 1.0, 1.0), "Suburbs_Column_Large_A_Base42", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (557.7261, 1606.8867, 795.0), (0.0, -105.00040758352254, 0.0), (1.0, 1.0, 1.0), "Suburbs_Column_Large_A_Base43", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (557.7261, 1606.8867, 795.0), (0.0, -14.999908208512407, 0.0), (1.0, 1.0, 1.0), "Suburbs_Column_Large_A_Base44", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1620.6705, 609.8013, 795.0), (0.0, 100.00040264673142, -0.0), (1.0, 1.0, 1.0), "Suburbs_Column_Large_A_Base45", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1620.6705, 609.8013, 795.0), (0.0, -169.99957079689236, 0.0), (1.0, 1.0, 1.0), "Suburbs_Column_Large_A_Base46", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1620.6705, 609.8013, 795.0), (0.0, -80.0003724785027, 0.0), (1.0, 1.0, 1.0), "Suburbs_Column_Large_A_Base47", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1620.6705, 609.8013, 795.0), (0.0, 10.000152850215558, -0.0), (1.0, 1.0, 1.0), "Suburbs_Column_Large_A_Base48", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2637.381, 135.1206, 1385.0), (0.0, -59.99969647782352, 0.0), (1.0, 1.0, 1.0), "Suburbs_Column_Large_A_Base49", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5969.9995, 2700.5605, 900.0), (-0.0, -179.99976777357483, -0.0), (1.0, 1.0, 1.0), "Suburbs_Column_Large_A_Base5_25", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3746.578, 6157.4927, 1350.0), (-0.0, -90.31197610055823, -0.0), (1.0, 1.0, 1.0), "Suburbs_Column_Large_A_Base5_62", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2637.381, 135.1206, 1385.0), (0.0, 30.00057906869548, -0.0), (1.0, 1.0, 1.0), "Suburbs_Column_Large_A_Base50", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2637.381, 135.1206, 1385.0), (0.0, 119.99993883827582, -0.0), (1.0, 1.0, 1.0), "Suburbs_Column_Large_A_Base51", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2637.381, 135.1206, 1385.0), (0.0, -149.9998519732493, 0.0), (1.0, 1.0, 1.0), "Suburbs_Column_Large_A_Base52", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3625.226, 114.65283, 1395.0), (0.0, -45.64416337357977, 0.0), (1.0, 1.0, 1.0), "Suburbs_Column_Large_A_Base53", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3625.226, 129.65283, 1395.0), (0.0, 54.35662930673483, -0.0), (1.0, 1.0, 1.0), "Suburbs_Column_Large_A_Base54", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3625.226, 129.65283, 1395.0), (0.0, 144.35565012492413, -0.0), (1.0, 1.0, 1.0), "Suburbs_Column_Large_A_Base55", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3625.226, 129.65283, 1395.0), (0.0, -125.64419932291783, 0.0), (1.0, 1.0, 1.0), "Suburbs_Column_Large_A_Base56", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (185.53711, 3718.7522, 1385.0), (0.0, -59.99975486978887, 0.0), (1.0, 1.0, 1.0), "Suburbs_Column_Large_A_Base57_477", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (185.53711, 3718.7522, 1385.0), (0.0, 30.000421378425173, -0.0), (1.0, 1.0, 1.0), "Suburbs_Column_Large_A_Base58", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (185.53711, 3718.7522, 1385.0), (0.0, 119.99975257943763, -0.0), (1.0, 1.0, 1.0), "Suburbs_Column_Large_A_Base59", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5969.9995, 2700.5605, 900.0), (-0.0, -89.99963031845931, -0.0), (1.0, 1.0, 1.0), "Suburbs_Column_Large_A_Base6_26", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3746.578, 6157.4927, 1350.0), (-0.0, -0.3118599960683572, -0.0), (1.0, 1.0, 1.0), "Suburbs_Column_Large_A_Base6_63", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5969.9995, 2700.5605, 900.0), (-0.0, -0.00019124526767201947, -0.0), (1.0, 1.0, 1.0), "Suburbs_Column_Large_A_Base7_27", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3746.578, 6157.4927, 1350.0), (0.0, 89.68761000310737, -0.0), (1.0, 1.0, 1.0), "Suburbs_Column_Large_A_Base7_64", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5969.9995, 2700.5605, 900.0), (0.0, 90.00013269448853, 0.0), (1.0, 1.0, 1.0), "Suburbs_Column_Large_A_Base8_28", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3746.578, 6157.4927, 1350.0), (0.0, 179.68797944641008, 0.0), (1.0, 1.0, 1.0), "Suburbs_Column_Large_A_Base8_65", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4879.366, 5801.09, 1365.0), (0.0, 5.000282396002133, -0.0), (1.0, 1.0, 1.0), "Suburbs_Column_Large_A_Base9", _folder)
if a: placed += 1
else: skipped += 1

# Batch 26: StaticMesh'Suburbs_Column_Large_A_Capitol' (60 instances)
_mesh_path = "/Game/Art/Assets/Kits/Architecture/Suburbs/Suburbs_Column_Large_A_Capitol"
_materials = ['/Game/Art/Assets/Kits/Architecture/Suburbs/Materials/Suburbs_Column_Large/MI_Suburbs_Column_Large_A_Capitol']
_folder = "Reconstruction/BD_BB_Chapter5_BrokenSeal/Meshes"
a = spawn_static_mesh(_mesh_path, _materials, (5970.0005, 3699.4397, 1700.0), (-0.0, -6.83018793977605e-05, -0.0), (1.0, 1.0, 1.0), "Suburbs_Column_Large_A_Capitol_21", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2746.591, 6162.9434, 2150.0), (0.0, 89.68770202212632, -0.0), (1.0, 1.0, 1.0), "Suburbs_Column_Large_A_Capitol_58", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4879.366, 5801.09, 2165.0), (0.0, 94.99969499892006, -0.0), (1.0, 1.0, 1.0), "Suburbs_Column_Large_A_Capitol10", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4879.366, 5801.09, 2165.0), (0.0, 4.999595626029819, -0.0), (1.0, 1.0, 1.0), "Suburbs_Column_Large_A_Capitol11", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4879.366, 5801.09, 2165.0), (0.0, -85.00047993979611, 0.0), (1.0, 1.0, 1.0), "Suburbs_Column_Large_A_Capitol12", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5665.03, 4962.263, 2195.0), (0.0, -105.00012818567036, 0.0), (1.0, 1.0, 1.0), "Suburbs_Column_Large_A_Capitol13", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5665.03, 4962.263, 2195.0), (0.0, 164.9996527510408, -0.0), (1.0, 1.0, 1.0), "Suburbs_Column_Large_A_Capitol14", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5665.03, 4962.263, 2195.0), (0.0, 74.99951925578414, -0.0), (1.0, 1.0, 1.0), "Suburbs_Column_Large_A_Capitol15", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5665.03, 4962.263, 2195.0), (0.0, -15.000457581712093, 0.0), (1.0, 1.0, 1.0), "Suburbs_Column_Large_A_Capitol16", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1633.7715, 5838.3867, 2185.0), (0.0, -175.0000600492453, 0.0), (1.0, 1.0, 1.0), "Suburbs_Column_Large_A_Capitol17", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1633.7715, 5838.3867, 2185.0), (0.0, 94.99969499892006, -0.0), (1.0, 1.0, 1.0), "Suburbs_Column_Large_A_Capitol18", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1633.7715, 5838.3867, 2185.0), (0.0, 4.999595626029819, -0.0), (1.0, 1.0, 1.0), "Suburbs_Column_Large_A_Capitol19", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5970.0005, 3699.4397, 1700.0), (-0.0, -90.0001813116405, -0.0), (1.0, 1.0, 1.0), "Suburbs_Column_Large_A_Capitol2_22", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2746.591, 6162.9434, 2150.0), (-0.0, -0.31240982395222655, -0.0), (1.0, 1.0, 1.0), "Suburbs_Column_Large_A_Capitol2_59", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1633.7715, 5838.3867, 2185.0), (0.0, -85.00047993979611, 0.0), (1.0, 1.0, 1.0), "Suburbs_Column_Large_A_Capitol20", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (556.5371, 4795.5415, 2115.0), (0.0, -175.0000600492453, 0.0), (1.0, 1.0, 1.0), "Suburbs_Column_Large_A_Capitol21", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (556.5371, 4795.5415, 2115.0), (0.0, 94.99969499892006, -0.0), (1.0, 1.0, 1.0), "Suburbs_Column_Large_A_Capitol22", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (556.5371, 4795.5415, 2115.0), (0.0, 4.999595626029819, -0.0), (1.0, 1.0, 1.0), "Suburbs_Column_Large_A_Capitol23", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (556.5371, 4795.5415, 2115.0), (0.0, -85.00047993979611, 0.0), (1.0, 1.0, 1.0), "Suburbs_Column_Large_A_Capitol24", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (187.3208, 3715.49, 2165.0), (0.0, 33.96410333153031, -0.0), (1.0, 1.0, 1.0), "Suburbs_Column_Large_A_Capitol25", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (187.3208, 3715.49, 2165.0), (0.0, -56.038696429425904, 0.0), (1.0, 1.0, 1.0), "Suburbs_Column_Large_A_Capitol26", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (187.3208, 3715.49, 2165.0), (0.0, -146.03955571610553, 0.0), (1.0, 1.0, 1.0), "Suburbs_Column_Large_A_Capitol27", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (187.3208, 3715.49, 2165.0), (0.0, 123.96222607647213, -0.0), (1.0, 1.0, 1.0), "Suburbs_Column_Large_A_Capitol28", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5970.0005, 3699.4397, 1700.0), (0.0, 179.99971531476433, 0.0), (1.0, 1.0, 1.0), "Suburbs_Column_Large_A_Capitol3_23", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2746.591, 6162.9434, 2150.0), (-0.0, -90.31250909369892, -0.0), (1.0, 1.0, 1.0), "Suburbs_Column_Large_A_Capitol3_60", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4639.954, 516.084, 2195.0), (0.0, 169.9998496531952, -0.0), (1.0, 1.0, 1.0), "Suburbs_Column_Large_A_Capitol33", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4639.954, 516.084, 2195.0), (0.0, 79.99966949139761, -0.0), (1.0, 1.0, 1.0), "Suburbs_Column_Large_A_Capitol34", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4639.954, 516.084, 2195.0), (0.0, -10.000487602513461, 0.0), (1.0, 1.0, 1.0), "Suburbs_Column_Large_A_Capitol35", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4639.954, 516.084, 2195.0), (0.0, -100.00054445149247, 0.0), (1.0, 1.0, 1.0), "Suburbs_Column_Large_A_Capitol36", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (145.53711, 2663.7522, 2185.0), (0.0, 149.99995949562742, -0.0), (1.0, 1.0, 1.0), "Suburbs_Column_Large_A_Capitol37", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (145.53711, 2663.7522, 2185.0), (0.0, 59.999762312719895, -0.0), (1.0, 1.0, 1.0), "Suburbs_Column_Large_A_Capitol38", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (145.53711, 2663.7522, 2185.0), (0.0, -30.00055174100497, 0.0), (1.0, 1.0, 1.0), "Suburbs_Column_Large_A_Capitol39", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5970.0005, 3699.4397, 1700.0), (0.0, 89.99952498181582, 0.0), (1.0, 1.0, 1.0), "Suburbs_Column_Large_A_Capitol4_24", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2746.591, 6162.9434, 2150.0), (0.0, 179.68731357758693, 0.0), (1.0, 1.0, 1.0), "Suburbs_Column_Large_A_Capitol4_61", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (145.53711, 2663.7522, 2185.0), (0.0, -120.00055444465106, 0.0), (1.0, 1.0, 1.0), "Suburbs_Column_Large_A_Capitol40", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (557.7261, 1606.8867, 2115.0), (0.0, -105.00007425414854, 0.0), (1.0, 1.0, 1.0), "Suburbs_Column_Large_A_Capitol41", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (557.7261, 1606.8867, 2115.0), (0.0, 164.99973620000208, -0.0), (1.0, 1.0, 1.0), "Suburbs_Column_Large_A_Capitol42", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (557.7261, 1606.8867, 2115.0), (0.0, 74.99967169970527, -0.0), (1.0, 1.0, 1.0), "Suburbs_Column_Large_A_Capitol43", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (557.7261, 1606.8867, 2115.0), (0.0, -15.000548659215577, 0.0), (1.0, 1.0, 1.0), "Suburbs_Column_Large_A_Capitol44", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1620.6705, 609.8013, 2115.0), (0.0, -79.99999917458362, 0.0), (1.0, 1.0, 1.0), "Suburbs_Column_Large_A_Capitol45", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1620.6705, 609.8013, 2115.0), (0.0, -170.0001588797845, 0.0), (1.0, 1.0, 1.0), "Suburbs_Column_Large_A_Capitol46", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1620.6705, 609.8013, 2115.0), (0.0, 99.99978778103929, -0.0), (1.0, 1.0, 1.0), "Suburbs_Column_Large_A_Capitol47", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1620.6705, 609.8013, 2115.0), (0.0, 9.999504149790164, -0.0), (1.0, 1.0, 1.0), "Suburbs_Column_Large_A_Capitol48", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2637.381, 135.1206, 2185.0), (0.0, 120.00024556922763, -0.0), (1.0, 1.0, 1.0), "Suburbs_Column_Large_A_Capitol49", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5969.9995, 2700.5605, 1700.0), (-0.0, -6.83018793977605e-05, -0.0), (1.0, 1.0, 1.0), "Suburbs_Column_Large_A_Capitol5_33", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3746.578, 6157.4927, 2150.0), (0.0, 89.68770202212632, -0.0), (1.0, 1.0, 1.0), "Suburbs_Column_Large_A_Capitol5_70", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2637.381, 135.1206, 2185.0), (0.0, 29.999807647889444, -0.0), (1.0, 1.0, 1.0), "Suburbs_Column_Large_A_Capitol50", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2637.381, 135.1206, 2185.0), (0.0, -60.000490509480684, 0.0), (1.0, 1.0, 1.0), "Suburbs_Column_Large_A_Capitol51", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2637.381, 135.1206, 2185.0), (0.0, -150.00058229493052, 0.0), (1.0, 1.0, 1.0), "Suburbs_Column_Large_A_Capitol52", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3625.226, 129.65283, 2195.0), (0.0, 144.35606626540175, -0.0), (1.0, 1.0, 1.0), "Suburbs_Column_Large_A_Capitol53", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3625.226, 129.65283, 2195.0), (0.0, 54.356145478969566, -0.0), (1.0, 1.0, 1.0), "Suburbs_Column_Large_A_Capitol54", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3625.226, 129.65283, 2195.0), (0.0, -35.644893967706494, 0.0), (1.0, 1.0, 1.0), "Suburbs_Column_Large_A_Capitol55", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3625.226, 114.65283, 2195.0), (0.0, -135.64494486276368, 0.0), (1.0, 1.0, 1.0), "Suburbs_Column_Large_A_Capitol56", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5969.9995, 2700.5605, 1700.0), (-0.0, -90.0001813116405, -0.0), (1.0, 1.0, 1.0), "Suburbs_Column_Large_A_Capitol6_34", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3746.578, 6157.4927, 2150.0), (-0.0, -0.31240982395222655, -0.0), (1.0, 1.0, 1.0), "Suburbs_Column_Large_A_Capitol6_71", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5969.9995, 2700.5605, 1700.0), (0.0, 179.99971531476433, 0.0), (1.0, 1.0, 1.0), "Suburbs_Column_Large_A_Capitol7_35", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3746.578, 6157.4927, 2150.0), (-0.0, -90.31250909369892, -0.0), (1.0, 1.0, 1.0), "Suburbs_Column_Large_A_Capitol7_72", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5969.9995, 2700.5605, 1700.0), (0.0, 89.99952498181582, 0.0), (1.0, 1.0, 1.0), "Suburbs_Column_Large_A_Capitol8_36", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3746.578, 6157.4927, 2150.0), (0.0, 179.68731357758693, 0.0), (1.0, 1.0, 1.0), "Suburbs_Column_Large_A_Capitol8_73", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4879.366, 5801.09, 2165.0), (0.0, -175.0000600492453, 0.0), (1.0, 1.0, 1.0), "Suburbs_Column_Large_A_Capitol9", _folder)
if a: placed += 1
else: skipped += 1

# Batch 27: StaticMesh'Suburbs_Column_Large_A_Shaft' (84 instances)
_mesh_path = "/Game/Art/Assets/Kits/Architecture/Suburbs/Suburbs_Column_Large_A_Shaft"
_materials = ['/Game/Art/Assets/Kits/Architecture/Suburbs/Materials/Suburbs_Column_Large/MI_Suburbs_Column_Large_A_Shaft']
_folder = "Reconstruction/BD_BB_Chapter5_BrokenSeal/Meshes"
a = spawn_static_mesh(_mesh_path, _materials, (5970.0005, 3699.4397, 1300.0), (-0.0, -6.83018793977605e-05, -0.0), (1.0, 1.0, 1.0), "Suburbs_Column_Large_A_Shaft_17", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2746.591, 6162.9434, 1750.0), (0.0, 89.68770202212632, -0.0), (1.0, 1.0, 1.0), "Suburbs_Column_Large_A_Shaft_54", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4879.366, 5801.09, 1765.0), (0.0, 94.99969499892006, -0.0), (1.0, 1.0, 1.0), "Suburbs_Column_Large_A_Shaft10", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4879.366, 5801.09, 1765.0), (0.0, 4.999595626029819, -0.0), (1.0, 1.0, 1.0), "Suburbs_Column_Large_A_Shaft11", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4879.366, 5801.09, 1765.0), (0.0, -85.00047993979611, 0.0), (1.0, 1.0, 1.0), "Suburbs_Column_Large_A_Shaft12", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5665.03, 4962.263, 1215.0), (0.0, -105.00012818567036, 0.0), (1.0, 1.0, 1.0), "Suburbs_Column_Large_A_Shaft13", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5665.03, 4962.263, 1215.0), (0.0, 164.9996527510408, -0.0), (1.0, 1.0, 1.0), "Suburbs_Column_Large_A_Shaft14", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5665.03, 4962.263, 1215.0), (0.0, 74.99951925578414, -0.0), (1.0, 1.0, 1.0), "Suburbs_Column_Large_A_Shaft15", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5665.03, 4962.263, 1215.0), (0.0, -15.000457581712093, 0.0), (1.0, 1.0, 1.0), "Suburbs_Column_Large_A_Shaft16", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5665.03, 4962.263, 1615.0), (0.0, -105.00012818567036, 0.0), (1.0, 1.0, 1.0), "Suburbs_Column_Large_A_Shaft17", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5665.03, 4962.263, 1615.0), (0.0, 164.9996527510408, -0.0), (1.0, 1.0, 1.0), "Suburbs_Column_Large_A_Shaft18", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5665.03, 4962.263, 1615.0), (0.0, 74.99951925578414, -0.0), (1.0, 1.0, 1.0), "Suburbs_Column_Large_A_Shaft19", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5970.0005, 3699.4397, 1300.0), (-0.0, -90.0001813116405, -0.0), (1.0, 1.0, 1.0), "Suburbs_Column_Large_A_Shaft2_18", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2746.591, 6162.9434, 1750.0), (-0.0, -0.31240982395222655, -0.0), (1.0, 1.0, 1.0), "Suburbs_Column_Large_A_Shaft2_55", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5665.03, 4962.263, 1615.0), (0.0, -15.000457581712093, 0.0), (1.0, 1.0, 1.0), "Suburbs_Column_Large_A_Shaft20", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5665.03, 4962.263, 2015.0), (0.0, -105.00012818567036, 0.0), (1.0, 1.0, 0.46875), "Suburbs_Column_Large_A_Shaft21", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5665.03, 4962.263, 2015.0), (0.0, 164.9996527510408, -0.0), (1.0, 1.0, 0.46875), "Suburbs_Column_Large_A_Shaft22", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5665.03, 4962.263, 2015.0), (0.0, 74.99951925578414, -0.0), (1.0, 1.0, 0.46875), "Suburbs_Column_Large_A_Shaft23", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5665.03, 4962.263, 2015.0), (0.0, -15.000457581712093, 0.0), (1.0, 1.0, 0.46875), "Suburbs_Column_Large_A_Shaft24", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1633.7715, 5838.3867, 1265.0), (0.0, -175.0000600492453, 0.0), (1.0, 1.0, 1.0), "Suburbs_Column_Large_A_Shaft25", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1633.7715, 5838.3867, 1265.0), (0.0, 94.99969499892006, -0.0), (1.0, 1.0, 1.0), "Suburbs_Column_Large_A_Shaft26", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1633.7715, 5838.3867, 1265.0), (0.0, 4.999595626029819, -0.0), (1.0, 1.0, 1.0), "Suburbs_Column_Large_A_Shaft27", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1633.7715, 5838.3867, 1265.0), (0.0, -85.00047993979611, 0.0), (1.0, 1.0, 1.0), "Suburbs_Column_Large_A_Shaft28", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1633.7715, 5838.3867, 1665.0), (0.0, -175.0000600492453, 0.0), (1.0, 1.0, 1.3125), "Suburbs_Column_Large_A_Shaft29", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5970.0005, 3699.4397, 1300.0), (0.0, 179.99971531476433, 0.0), (1.0, 1.0, 1.0), "Suburbs_Column_Large_A_Shaft3_19", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2746.591, 6162.9434, 1750.0), (-0.0, -90.31250909369892, -0.0), (1.0, 1.0, 1.0), "Suburbs_Column_Large_A_Shaft3_56", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1633.7715, 5838.3867, 1665.0), (0.0, 94.99969499892006, -0.0), (1.0, 1.0, 1.3125), "Suburbs_Column_Large_A_Shaft30", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1633.7715, 5838.3867, 1665.0), (0.0, 4.999595626029819, -0.0), (1.0, 1.0, 1.3125), "Suburbs_Column_Large_A_Shaft31", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1633.7715, 5838.3867, 1665.0), (0.0, -85.00047993979611, 0.0), (1.0, 1.0, 1.3125), "Suburbs_Column_Large_A_Shaft32", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (556.5371, 4795.5415, 1195.0), (0.0, -175.0000600492453, 0.0), (1.0, 1.0, 1.0), "Suburbs_Column_Large_A_Shaft33", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (556.5371, 4795.5415, 1195.0), (0.0, 94.99969499892006, -0.0), (1.0, 1.0, 1.0), "Suburbs_Column_Large_A_Shaft34", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (556.5371, 4795.5415, 1195.0), (0.0, 4.999595626029819, -0.0), (1.0, 1.0, 1.0), "Suburbs_Column_Large_A_Shaft35", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (556.5371, 4795.5415, 1195.0), (0.0, -85.00047993979611, 0.0), (1.0, 1.0, 1.0), "Suburbs_Column_Large_A_Shaft36", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (556.5371, 4795.5415, 1595.0), (0.0, -175.0000600492453, 0.0), (1.0, 1.0, 1.3125), "Suburbs_Column_Large_A_Shaft37", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (556.5371, 4795.5415, 1595.0), (0.0, 94.99969499892006, -0.0), (1.0, 1.0, 1.3125), "Suburbs_Column_Large_A_Shaft38", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (556.5371, 4795.5415, 1595.0), (0.0, 4.999595626029819, -0.0), (1.0, 1.0, 1.3125), "Suburbs_Column_Large_A_Shaft39", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5970.0005, 3699.4397, 1300.0), (0.0, 89.99952498181582, 0.0), (1.0, 1.0, 1.0), "Suburbs_Column_Large_A_Shaft4_20", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2746.591, 6162.9434, 1750.0), (0.0, 179.68731357758693, 0.0), (1.0, 1.0, 1.0), "Suburbs_Column_Large_A_Shaft4_57", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (556.5371, 4795.5415, 1595.0), (0.0, -85.00047993979611, 0.0), (1.0, 1.0, 1.3125), "Suburbs_Column_Large_A_Shaft40", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (187.3208, 3715.49, 1785.0), (0.0, 33.96410333153031, -0.0), (1.0, 1.0, 1.0), "Suburbs_Column_Large_A_Shaft41", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (187.3208, 3715.49, 1785.0), (0.0, -56.038696429425904, 0.0), (1.0, 1.0, 1.0), "Suburbs_Column_Large_A_Shaft42", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (187.3208, 3715.49, 1785.0), (0.0, -146.03955571610553, 0.0), (1.0, 1.0, 1.0), "Suburbs_Column_Large_A_Shaft43", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (187.3208, 3715.49, 1765.0), (0.0, 123.96222607647213, -0.0), (1.0, 1.0, 1.0), "Suburbs_Column_Large_A_Shaft44", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4639.954, 516.084, 1795.0), (0.0, 169.9998496531952, -0.0), (1.0, 1.0, 1.0), "Suburbs_Column_Large_A_Shaft49_127", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5969.9995, 2700.5605, 1300.0), (-0.0, -6.83018793977605e-05, -0.0), (1.0, 1.0, 1.0), "Suburbs_Column_Large_A_Shaft5_29", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3746.578, 6157.4927, 1750.0), (0.0, 89.68770202212632, -0.0), (1.0, 1.0, 1.0), "Suburbs_Column_Large_A_Shaft5_66", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4639.954, 516.084, 1795.0), (0.0, 79.99966949139761, -0.0), (1.0, 1.0, 1.0), "Suburbs_Column_Large_A_Shaft50_128", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4639.954, 516.084, 1795.0), (0.0, -10.000487602513461, 0.0), (1.0, 1.0, 1.0), "Suburbs_Column_Large_A_Shaft51_129", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4639.954, 516.084, 1795.0), (0.0, -100.00054445149247, 0.0), (1.0, 1.0, 1.0), "Suburbs_Column_Large_A_Shaft52_130", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3625.226, 129.65283, 1795.0), (0.0, 144.35606626540175, -0.0), (1.0, 1.0, 1.0), "Suburbs_Column_Large_A_Shaft53", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3625.226, 129.65283, 1795.0), (0.0, 54.356145478969566, -0.0), (1.0, 1.0, 1.0), "Suburbs_Column_Large_A_Shaft54", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3625.226, 129.65283, 1795.0), (0.0, -35.64495417308881, 0.0), (1.0, 1.0, 1.0), "Suburbs_Column_Large_A_Shaft55", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3625.226, 114.65283, 1795.0), (0.0, -135.64494486276368, 0.0), (1.0, 1.0, 1.0), "Suburbs_Column_Large_A_Shaft56", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (145.53711, 2663.7522, 1785.0), (0.0, 149.99995949562742, -0.0), (1.0, 1.0, 1.0), "Suburbs_Column_Large_A_Shaft57", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (145.53711, 2663.7522, 1785.0), (0.0, 59.999762312719895, -0.0), (1.0, 1.0, 1.0), "Suburbs_Column_Large_A_Shaft58", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (145.53711, 2663.7522, 1785.0), (0.0, -30.00055174100497, 0.0), (1.0, 1.0, 1.0), "Suburbs_Column_Large_A_Shaft59", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5969.9995, 2700.5605, 1300.0), (-0.0, -90.0001813116405, -0.0), (1.0, 1.0, 1.0), "Suburbs_Column_Large_A_Shaft6_30", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3746.578, 6157.4927, 1750.0), (-0.0, -0.31240982395222655, -0.0), (1.0, 1.0, 1.0), "Suburbs_Column_Large_A_Shaft6_67", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (145.53711, 2663.7522, 1785.0), (0.0, -120.00055444465106, 0.0), (1.0, 1.0, 1.0), "Suburbs_Column_Large_A_Shaft60", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (557.7261, 1606.8867, 1195.0), (0.0, -105.00007425414854, 0.0), (1.0, 1.0, 1.0), "Suburbs_Column_Large_A_Shaft61", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (557.7261, 1606.8867, 1195.0), (0.0, 164.99973620000208, -0.0), (1.0, 1.0, 1.0), "Suburbs_Column_Large_A_Shaft62", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (557.7261, 1606.8867, 1195.0), (0.0, 74.99967169970527, -0.0), (1.0, 1.0, 1.0), "Suburbs_Column_Large_A_Shaft63", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (557.7261, 1606.8867, 1195.0), (0.0, -15.000548659215577, 0.0), (1.0, 1.0, 1.0), "Suburbs_Column_Large_A_Shaft64", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (557.7261, 1606.8867, 1595.0), (0.0, -105.00007425414854, 0.0), (1.0, 1.0, 1.3125), "Suburbs_Column_Large_A_Shaft65", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (557.7261, 1606.8867, 1595.0), (0.0, 164.99973620000208, -0.0), (1.0, 1.0, 1.3125), "Suburbs_Column_Large_A_Shaft66", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (557.7261, 1606.8867, 1595.0), (0.0, 74.99967169970527, -0.0), (1.0, 1.0, 1.3125), "Suburbs_Column_Large_A_Shaft67", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (557.7261, 1606.8867, 1595.0), (0.0, -15.000548659215577, 0.0), (1.0, 1.0, 1.3125), "Suburbs_Column_Large_A_Shaft68", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1620.6705, 609.8013, 1195.0), (0.0, -79.99999917458362, 0.0), (1.0, 1.0, 1.0), "Suburbs_Column_Large_A_Shaft69", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5969.9995, 2700.5605, 1300.0), (0.0, 179.99971531476433, 0.0), (1.0, 1.0, 1.0), "Suburbs_Column_Large_A_Shaft7_31", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3746.578, 6157.4927, 1750.0), (-0.0, -90.31250909369892, -0.0), (1.0, 1.0, 1.0), "Suburbs_Column_Large_A_Shaft7_68", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1620.6705, 609.8013, 1195.0), (0.0, -170.0001588797845, 0.0), (1.0, 1.0, 1.0), "Suburbs_Column_Large_A_Shaft70", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1620.6705, 609.8013, 1195.0), (0.0, 99.99978778103929, -0.0), (1.0, 1.0, 1.0), "Suburbs_Column_Large_A_Shaft71", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1620.6705, 609.8013, 1195.0), (0.0, 9.999504149790164, -0.0), (1.0, 1.0, 1.0), "Suburbs_Column_Large_A_Shaft72", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1620.6705, 609.8013, 1595.0), (0.0, -79.99999917458362, 0.0), (1.0, 1.0, 1.3125), "Suburbs_Column_Large_A_Shaft73", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1620.6705, 609.8013, 1595.0), (0.0, -170.0001588797845, 0.0), (1.0, 1.0, 1.3125), "Suburbs_Column_Large_A_Shaft74", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1620.6705, 609.8013, 1595.0), (0.0, 99.99978778103929, -0.0), (1.0, 1.0, 1.3125), "Suburbs_Column_Large_A_Shaft75", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1620.6705, 609.8013, 1595.0), (0.0, 9.999504149790164, -0.0), (1.0, 1.0, 1.3125), "Suburbs_Column_Large_A_Shaft76", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2637.381, 135.1206, 1785.0), (0.0, 120.00024556922763, -0.0), (1.0, 1.0, 1.0), "Suburbs_Column_Large_A_Shaft77", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2637.381, 135.1206, 1785.0), (0.0, 29.999807647889444, -0.0), (1.0, 1.0, 1.0), "Suburbs_Column_Large_A_Shaft78", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2637.381, 135.1206, 1785.0), (0.0, -60.000490509480684, 0.0), (1.0, 1.0, 1.0), "Suburbs_Column_Large_A_Shaft79", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5969.9995, 2700.5605, 1300.0), (0.0, 89.99952498181582, 0.0), (1.0, 1.0, 1.0), "Suburbs_Column_Large_A_Shaft8_32", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3746.578, 6157.4927, 1750.0), (0.0, 179.68731357758693, 0.0), (1.0, 1.0, 1.0), "Suburbs_Column_Large_A_Shaft8_69", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2637.381, 135.1206, 1785.0), (0.0, -150.00058229493052, 0.0), (1.0, 1.0, 1.0), "Suburbs_Column_Large_A_Shaft80", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4879.366, 5801.09, 1765.0), (0.0, -175.0000600492453, 0.0), (1.0, 1.0, 1.0), "Suburbs_Column_Large_A_Shaft9", _folder)
if a: placed += 1
else: skipped += 1

# Batch 28: StaticMesh'Suburbs_Column_Single_Half_Base_A' (12 instances)
_mesh_path = "/Game/Art/Assets/Kits/Architecture/Suburbs/Suburbs_Column_Single_Half_Base_A"
_materials = ['/Game/Art/Assets/Kits/Architecture/Suburbs/Materials/Suburbs_Column_Single/MI_Suburbs_Column_Single_Half_Base_Dest']
_folder = "Reconstruction/BD_BB_Chapter5_BrokenSeal/Meshes"
a = spawn_static_mesh(_mesh_path, _materials, (5221.3877, 5349.588, 1009.27344), (0.0, 135.9289850913951, -0.0), (1.0, 1.0, 1.0), "Suburbs_Column_Single_Half_Base_A12", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5005.8545, 5558.2666, 1009.27344), (0.0, 135.92980587527035, -0.0), (1.0, 1.0, 1.0), "Suburbs_Column_Single_Half_Base_A13", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2497.782, 6041.4907, 1009.27344), (0.0, -161.44185646674234, 0.0), (1.0, 1.0, 1.0), "Suburbs_Column_Single_Half_Base_A14", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2213.3796, 5946.0254, 1009.27344), (0.0, -161.44145981033108, 0.0), (1.0, 1.0, 1.0), "Suburbs_Column_Single_Half_Base_A15", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (448.77246, 4233.359, 1009.27344), (0.0, -106.79085755639628, 0.0), (1.0, 1.0, 1.0), "Suburbs_Column_Single_Half_Base_A18", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (362.09668, 3946.1472, 1009.27344), (0.0, -106.78851104565209, 0.0), (1.0, 1.0, 1.0), "Suburbs_Column_Single_Half_Base_A19", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2137.9531, 404.22754, 900.0), (0.0, -25.648438916826585, 0.0), (1.0, 1.0, 1.0), "Suburbs_Column_Single_Half_Base_A2", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (337.89062, 2443.0493, 1009.27344), (0.0, -70.62377463825956, 0.0), (1.0, 1.0, 1.0), "Suburbs_Column_Single_Half_Base_A20", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (437.42334, 2160.0435, 1009.27344), (0.0, -70.62445869264327, 0.0), (1.0, 1.0, 1.0), "Suburbs_Column_Single_Half_Base_A21", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2408.3848, 274.35498, 900.0), (0.0, -25.648438916826585, 0.0), (1.0, 1.0, 1.0), "Suburbs_Column_Single_Half_Base_A7", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4812.1035, 734.1333, 1009.27344), (0.0, 37.95672765743992, -0.0), (1.0, 1.0, 1.0), "Suburbs_Column_Single_Half_Base_A8", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5048.6523, 918.64404, 1009.27344), (0.0, 37.95672765743992, -0.0), (1.0, 1.0, 1.0), "Suburbs_Column_Single_Half_Base_A9", _folder)
if a: placed += 1
else: skipped += 1

# Batch 29: StaticMesh'Suburbs_Column_Single_Half_Capitol_A' (2 instances)
_mesh_path = "/Game/Art/Assets/Kits/Architecture/Suburbs/Suburbs_Column_Single_Half_Capitol_A"
_materials = ['/Game/Art/Assets/Kits/Architecture/Suburbs/Materials/Suburbs_Column_Single/MI_Suburbs_Column_Single_Half_Shaft_A_NonDest']
_folder = "Reconstruction/BD_BB_Chapter5_BrokenSeal/Meshes"
a = spawn_static_mesh(_mesh_path, _materials, (2408.3848, 274.35498, 1190.0), (0.0, -25.648438916826585, 0.0), (1.0, 1.0, 1.0), "Suburbs_Column_Single_Half_Capitol_A7", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4812.1035, 734.1333, 1299.2734), (0.0, 37.95672765743992, -0.0), (1.0, 1.0, 1.0), "Suburbs_Column_Single_Half_Capitol_A8", _folder)
if a: placed += 1
else: skipped += 1

# Batch 30: StaticMesh'Suburbs_Column_Single_Half_Shaft_A' (14 instances)
_mesh_path = "/Game/Art/Assets/Kits/Architecture/Suburbs/Suburbs_Column_Single_Half_Shaft_A"
_materials = ['/Game/Art/Assets/Kits/Architecture/Suburbs/Materials/Suburbs_Column_Single/MI_Suburbs_Column_Single_Half_Shaft_A_NonDest']
_folder = "Reconstruction/BD_BB_Chapter5_BrokenSeal/Meshes"
a = spawn_static_mesh(_mesh_path, _materials, (2408.3848, 274.35498, 1100.0), (0.0, -25.648438916826585, 0.0), (1.0, 1.0, 1.0), "Suburbs_Column_Single_Half_Shaft_A10", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4812.1035, 734.1333, 1109.2734), (0.0, 37.95672765743992, -0.0), (1.0, 1.0, 1.0), "Suburbs_Column_Single_Half_Shaft_A11", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4812.1035, 734.1333, 1209.2734), (0.0, 37.95672765743992, -0.0), (1.0, 1.0, 1.0), "Suburbs_Column_Single_Half_Shaft_A12", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5048.6523, 918.64404, 1109.2734), (0.0, 37.95672765743992, -0.0), (1.0, 1.0, 1.0), "Suburbs_Column_Single_Half_Shaft_A13", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5005.8545, 5558.2666, 1109.2734), (0.0, 135.92980587527035, -0.0), (1.0, 1.0, 1.0), "Suburbs_Column_Single_Half_Shaft_A21", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5005.8545, 5558.2666, 1209.2734), (0.0, 135.92980587527035, -0.0), (1.0, 1.0, 1.0), "Suburbs_Column_Single_Half_Shaft_A22", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2497.782, 6041.4907, 1109.2734), (0.0, -161.44185646674234, 0.0), (1.0, 1.0, 1.0), "Suburbs_Column_Single_Half_Shaft_A23", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2497.782, 6041.4907, 1209.2734), (0.0, -161.44185646674234, 0.0), (1.0, 1.0, 1.0), "Suburbs_Column_Single_Half_Shaft_A24", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (362.09668, 3946.1472, 1109.2734), (0.0, -106.78851104565209, 0.0), (1.0, 1.0, 1.0), "Suburbs_Column_Single_Half_Shaft_A33", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (362.09668, 3946.1472, 1209.2734), (0.0, -106.78851104565209, 0.0), (1.0, 1.0, 1.0), "Suburbs_Column_Single_Half_Shaft_A34", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (337.89062, 2443.0493, 1109.2734), (0.0, -70.62377463825956, 0.0), (1.0, 1.0, 1.0), "Suburbs_Column_Single_Half_Shaft_A35", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (337.89062, 2443.0493, 1209.2734), (0.0, -70.62377463825956, 0.0), (1.0, 1.0, 1.0), "Suburbs_Column_Single_Half_Shaft_A36", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2137.9531, 404.22754, 1000.0), (0.0, -25.648438916826585, 0.0), (1.0, 1.0, 1.0), "Suburbs_Column_Single_Half_Shaft_A7", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2408.3848, 274.35498, 1000.0), (0.0, -25.648438916826585, 0.0), (1.0, 1.0, 1.0), "Suburbs_Column_Single_Half_Shaft_A9", _folder)
if a: placed += 1
else: skipped += 1

# Batch 31: StaticMesh'Suburbs_Column_X_Large_A_Base_1' (2 instances)
_mesh_path = "/Game/Art/Assets/Kits/Architecture/Suburbs/Suburbs_Column_X_Large_A_Base_1"
_materials = ['/Game/Art/Assets/Kits/Architecture/Suburbs/Materials/Suburbs_Trim_Sheet_A/MI_Suburbs_Trim_Sheet_A']
_folder = "Reconstruction/BD_BB_Chapter5_BrokenSeal/Meshes"
a = spawn_static_mesh(_mesh_path, _materials, (6120.001, 3848.9414, 900.0), (-0.0, -6.83018793977605e-05, -0.0), (1.0, 1.0, 1.0), "Suburbs_Column_X_Large_A_Base_1", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (6119.999, 2551.035, 1699.9012), (1.3660369076366731e-05, 3.41509276216381e-05, -179.99998633961212), (1.0, 1.0, 1.0), "Suburbs_Column_X_Large_A_Base_11", _folder)
if a: placed += 1
else: skipped += 1

# Batch 32: StaticMesh'Suburbs_Column_X_Large_A_Base_1_R' (2 instances)
_mesh_path = "/Game/Art/Assets/Kits/Architecture/Suburbs/Suburbs_Column_X_Large_A_Base_1_R"
_materials = ['/Game/Art/Assets/Kits/Architecture/Suburbs/Materials/Suburbs_Trim_Sheet_A/MI_Suburbs_Trim_Sheet_A']
_folder = "Reconstruction/BD_BB_Chapter5_BrokenSeal/Meshes"
a = spawn_static_mesh(_mesh_path, _materials, (6119.998, 3849.102, 1699.9655), (-2.5174915203238984e-19, 3.41509294309403e-05, -179.9999863396116), (1.0, 1.0, 1.0), "Suburbs_Column_X_Large_A_Base_2", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (6119.999, 2550.8457, 900.0), (-0.0, -6.83018793977605e-05, -0.0), (1.0, 1.0, 1.0), "Suburbs_Column_X_Large_A_Base_3", _folder)
if a: placed += 1
else: skipped += 1

# Batch 33: StaticMesh'Suburbs_Column_X_Large_A_Base_Corner' (5 instances)
_mesh_path = "/Game/Art/Assets/Kits/Architecture/Suburbs/Suburbs_Column_X_Large_A_Base_Corner"
_materials = ['/Game/Art/Assets/Kits/Architecture/Suburbs/Materials/Suburbs_Trim_Sheet_A/MI_Suburbs_Trim_Sheet_A']
_folder = "Reconstruction/BD_BB_Chapter5_BrokenSeal/Meshes"
a = spawn_static_mesh(_mesh_path, _materials, (6120.001, 3848.9414, 800.0), (-0.0, -6.83018793977605e-05, -0.0), (1.0, 1.0, 1.0), "Suburbs_Column_X_Large_A_Base_Corner_7", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2597.4111, 6313.759, 1250.0), (0.0, 89.68770202212632, -0.0), (1.0, 1.0, 1.0), "Suburbs_Column_X_Large_A_Base_Corner_43", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (6120.005, 2562.9736, 800.0), (-0.0, -89.99995929347138, -0.0), (1.0, 1.0, 1.0), "Suburbs_Column_X_Large_A_Base_Corner2_10", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5007.419, 4469.0674, 932.333), (0.0, -49.650513495309255, 0.0), (0.46875, 0.5, 0.5), "Suburbs_Column_X_Large_A_Base_Corner3_268", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5007.419, 4469.0674, 932.333), (0.0, 40.350651435001716, -0.0), (0.5, 0.4375, 0.5), "Suburbs_Column_X_Large_A_Base_Corner4", _folder)
if a: placed += 1
else: skipped += 1

# Batch 34: StaticMesh'Suburbs_Column_X_Large_A_CapitalL' (2 instances)
_mesh_path = "/Game/Art/Assets/Kits/Architecture/Suburbs/Suburbs_Column_X_Large_A_CapitalL"
_materials = ['/Game/Art/Assets/Kits/Architecture/Suburbs/Materials/Suburbs_Trim_Sheet_A/MI_Suburbs_Trim_Sheet_A']
_folder = "Reconstruction/BD_BB_Chapter5_BrokenSeal/Meshes"
a = spawn_static_mesh(_mesh_path, _materials, (6120.001, 3848.9414, 1700.0), (-0.0, -6.83018793977605e-05, -0.0), (1.0, 1.0, 1.0), "Suburbs_Column_X_Large_A_Captol_8", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2597.4111, 6313.759, 2150.0), (0.0, 89.68770202212632, -0.0), (1.0, 1.0, 1.0), "Suburbs_Column_X_Large_A_Captol_44", _folder)
if a: placed += 1
else: skipped += 1

# Batch 35: StaticMesh'Suburbs_Column_X_Large_A_CapitalL_colum_E' (1 instances)
_mesh_path = "/Game/Art/Assets/Kits/Architecture/Suburbs/Suburbs_Column_X_Large_A_CapitalL_colum_E"
_materials = ['/Game/Art/Assets/Kits/Architecture/Suburbs/Materials/Suburbs_Trim_Sheet_A/MI_Suburbs_Trim_Sheet_A']
_folder = "Reconstruction/BD_BB_Chapter5_BrokenSeal/Meshes"
a = spawn_static_mesh(_mesh_path, _materials, (6023.863, 2551.126, 1700.0), (-0.0, -179.9999795094293, -0.0), (1.0, 1.0, 1.0), "Suburbs_Column_X_Large_A_Captol2_12", _folder)
if a: placed += 1
else: skipped += 1

# Batch 36: StaticMesh'Suburbs_Floor_Stone_IND_A' (1 instances)
_mesh_path = "/Game/Art/Assets/Kits/Architecture/Suburbs/Suburbs_Floor_Stone_IND_A"
_materials = ['/Game/Art/Assets/Kits/Architecture/Suburbs/Materials/Suburbs_Floor_Stone_IND/MI_Suburbs_Floor_Stone_IND_MAT_Inst_Dest']
_folder = "Reconstruction/BD_BB_Chapter5_BrokenSeal/Meshes"
a = spawn_static_mesh(_mesh_path, _materials, (1178.4692, 5369.13, 800.0), (0.0, -179.99998633961752, -0.0), (1.0, 1.0, 1.0), "Suburbs_Floor_Stone_IND_A_72", _folder)
if a: placed += 1
else: skipped += 1

# Batch 37: StaticMesh'Suburbs_Floor_Stone_IND_D' (2 instances)
_mesh_path = "/Game/Art/Assets/Kits/Architecture/Suburbs/Suburbs_Floor_Stone_IND_D"
_materials = ['/Game/Art/Assets/Kits/Architecture/Suburbs/Materials/Suburbs_Floor_Stone_IND/MI_Suburbs_Floor_Stone_IND_MAT_Inst_Dest']
_folder = "Reconstruction/BD_BB_Chapter5_BrokenSeal/Meshes"
a = spawn_static_mesh(_mesh_path, _materials, (2204.373, 2389.2656, 936.3345), (0.0, -179.99998633961752, -0.0), (1.0, 1.0, 1.0), "Suburbs_Floor_Stone_IND_D_18", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2163.7622, 2432.9922, 935.48145), (0.0, -179.99998633961752, -0.0), (1.0, 1.0, 1.0), "Suburbs_Floor_Stone_IND_D2_21", _folder)
if a: placed += 1
else: skipped += 1

# Batch 38: StaticMesh'Suburbs_Floor_Trim_A_1_5m' (2 instances)
_mesh_path = "/Game/Art/Assets/Kits/Architecture/Suburbs/Suburbs_Floor_Trim_A_1_5m"
_materials = ['/Game/Art/Assets/Kits/Architecture/Suburbs/Materials/Suburbs_Floor_A/MI_Suburbs_Floor_A_2_Inst']
_folder = "Reconstruction/BD_BB_Chapter5_BrokenSeal/Meshes"
a = spawn_static_mesh(_mesh_path, _materials, (2012.8984, 1392.72, 934.0), (0.0, -74.99990873202879, 0.0), (1.0, 0.78125, 1.0), "Suburbs_Floor_Trim_A_3m46", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3536.0, 1468.001, 934.0), (0.0, -89.99993822608693, 0.0), (1.0, 0.78125, 1.0), "Suburbs_Floor_Trim_A_3m51_157", _folder)
if a: placed += 1
else: skipped += 1

# Batch 39: StaticMesh'Suburbs_Floor_Trim_A_1_5m' (1 instances)
_mesh_path = "/Game/Art/Assets/Kits/Architecture/Suburbs/Suburbs_Floor_Trim_A_1_5m"
_materials = ['/Game/Art/Assets/Kits/Architecture/Suburbs/Materials/Suburbs_Floor_A/MI_Suburbs_Floor_A_2_NonDest_Dark']
_folder = "Reconstruction/BD_BB_Chapter5_BrokenSeal/Meshes"
a = spawn_static_mesh(_mesh_path, _materials, (2074.8489, 5005.874, 934.0), (0.0, 65.3142887648547, -0.0), (1.0, 0.78125, 1.0), "Suburbs_Floor_Trim_A_3m53", _folder)
if a: placed += 1
else: skipped += 1

# Batch 40: StaticMesh'Suburbs_Floor_Trim_A_3m' (62 instances)
_mesh_path = "/Game/Art/Assets/Kits/Architecture/Suburbs/Suburbs_Floor_Trim_A_3m"
_materials = ['/Game/Art/Assets/Kits/Architecture/Suburbs/Materials/Suburbs_Floor_A/MI_Suburbs_Floor_A_2_NonDest_Dark']
_folder = "Reconstruction/BD_BB_Chapter5_BrokenSeal/Meshes"
a = spawn_static_mesh(_mesh_path, _materials, (5048.7764, 4061.3481, 934.0), (0.0, 0.0001525878854640202, -0.0), (1.0, 1.0, 1.0), "NonDest_Floor_Trim_Thin_3M_A64", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5048.7764, 3761.3481, 934.0), (0.0, 0.0001525878854640202, -0.0), (1.0, 1.0, 1.0), "NonDest_Floor_Trim_Thin_3M_A65_501", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5048.777, 3461.3481, 934.0), (0.0, 0.0001525878854640202, -0.0), (1.0, 1.0, 1.0), "NonDest_Floor_Trim_Thin_3M_A66_503", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5048.7783, 2671.3481, 930.0), (0.0, 0.0001525878854640202, -0.0), (1.0, 1.0, 1.0), "NonDest_Floor_Trim_Thin_3M_A67_507", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5048.7783, 2371.3481, 930.0), (0.0, 0.0001525878854640202, -0.0), (1.0, 1.0, 1.0), "NonDest_Floor_Trim_Thin_3M_A68_508", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5048.779, 2071.3481, 930.0), (0.0, 0.0001525878854640202, -0.0), (1.0, 1.0, 1.0), "NonDest_Floor_Trim_Thin_3M_A69_509", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1530.0, 2810.8652, 1455.1279), (0.0, -0.0002136230511090266, 0.0), (1.5, 1.25, 1.5625), "Suburbs_Floor_Trim_A_3m_51", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2800.6199, 5527.0527, 1402.0701), (0.0, 179.9995696979556, -0.0), (1.5, 1.0, 1.9375), "Suburbs_Floor_Trim_A_3m10", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3550.6196, 4922.0513, 1397.0701), (0.0, -3.051757709276941e-05, 0.0), (1.5, 1.0, 1.9375), "Suburbs_Floor_Trim_A_3m12", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3548.8623, 1521.915, 1393.4314), (0.0, 89.99967893541628, -0.0), (1.5, 1.25, 1.9375), "Suburbs_Floor_Trim_A_3m13", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3173.862, 1521.9165, 1393.4314), (0.0, 89.99967893541628, -0.0), (1.5, 1.25, 1.9375), "Suburbs_Floor_Trim_A_3m14", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3548.8613, 1206.915, 1393.1184), (0.0, -0.00039672851366830966, 0.0), (1.5, 1.0, 1.9375), "Suburbs_Floor_Trim_A_3m15", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3548.8608, 910.91504, 1393.1184), (0.0, -0.00039672851366830966, 0.0), (1.5, 1.0, 1.9375), "Suburbs_Floor_Trim_A_3m16", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2798.8604, 1515.916, 1393.1184), (0.0, 179.9999795094293, -0.0), (1.5, 1.0, 1.9375), "Suburbs_Floor_Trim_A_3m18", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3581.1028, 4660.033, 936.3345), (0.0, -179.99998633961752, -0.0), (0.8125, 0.8125, 0.8125), "Suburbs_Floor_Trim_A_3m19_2", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1530.0005, 3185.8652, 1455.1279), (0.0, -0.0002136230511090266, 0.0), (1.5, 1.25, 1.5625), "Suburbs_Floor_Trim_A_3m2", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3581.1028, 4904.033, 936.3345), (0.0, -179.99998633961752, -0.0), (0.8125, 0.8125, 0.8125), "Suburbs_Floor_Trim_A_3m20", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2781.1023, 4658.0337, 936.3345), (0.0, 0.00012207030837116422, -0.0), (0.8125, 0.8125, 0.8125), "Suburbs_Floor_Trim_A_3m21", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2781.1028, 4414.033, 936.3345), (0.0, 0.00012207030837116422, -0.0), (0.8125, 0.8125, 0.8125), "Suburbs_Floor_Trim_A_3m22", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3577.7874, 1830.0557, 936.3345), (0.0, 179.2215026795375, -0.0), (0.8125, 0.8125, 0.8125), "Suburbs_Floor_Trim_A_3m23", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3581.1028, 2074.0332, 936.3345), (0.0, 179.2215026795375, -0.0), (0.8125, 0.8125, 0.8125), "Suburbs_Floor_Trim_A_3m24", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2781.1023, 1828.0337, 936.3345), (0.0, 0.00012207030837116422, -0.0), (0.8125, 0.8125, 0.8125), "Suburbs_Floor_Trim_A_3m25", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2781.1028, 1584.0332, 936.3345), (0.0, 0.00012207030837116422, -0.0), (0.8125, 0.8125, 0.8125), "Suburbs_Floor_Trim_A_3m26", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2781.103, 1343.0332, 936.3345), (0.0, 0.00012207030837116422, -0.0), (0.8125, 0.8125, 0.8125), "Suburbs_Floor_Trim_A_3m27", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2577.0, 1484.0, 934.0), (0.0, -89.99993822608693, 0.0), (1.0, 0.78125, 1.0), "Suburbs_Floor_Trim_A_3m28_24", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2345.0, 1484.0, 934.0), (0.0, -89.99993822608693, 0.0), (1.0, 0.78125, 1.0), "Suburbs_Floor_Trim_A_3m29", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1215.0, 2810.8652, 1454.876), (0.0, -90.00026882257364, 0.0), (1.5, 1.0, 1.5625), "Suburbs_Floor_Trim_A_3m3", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2123.9795, 1422.4843, 934.0), (0.0, -74.99990873202879, 0.0), (1.0, 0.78125, 1.0), "Suburbs_Floor_Trim_A_3m30", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1655.493, 2422.4521, 934.0), (0.0, 144.99998898772822, -0.0), (1.0, 0.6670534, 1.0), "Suburbs_Floor_Trim_A_3m31", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1540.4055, 2258.0894, 934.0), (0.0, 144.99998898772822, -0.0), (1.0, 0.6670534, 1.0), "Suburbs_Floor_Trim_A_3m32_464", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3574.513, 1589.0779, 936.3345), (0.0, 179.2215026795375, -0.0), (0.8125, 0.8125, 0.8125), "Suburbs_Floor_Trim_A_3m33", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1668.374, 3567.269, 934.0), (0.0, -179.99991120752276, 0.0), (1.0, 0.78125, 1.0), "Suburbs_Floor_Trim_A_3m36", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1668.374, 3799.269, 934.0), (0.0, -179.99991120752276, 0.0), (1.0, 0.78125, 1.0), "Suburbs_Floor_Trim_A_3m37", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1668.374, 4032.269, 934.0), (0.0, -179.99991120752276, 0.0), (1.0, 0.78125, 1.0), "Suburbs_Floor_Trim_A_3m38", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1547.2145, 4203.473, 934.0), (0.0, -143.66202748939145, 0.0), (1.0, 0.72139275, 1.0), "Suburbs_Floor_Trim_A_3m39", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1419.7393, 4376.7866, 934.0), (0.0, -143.6621529124353, 0.0), (1.0, 0.72139275, 1.0), "Suburbs_Floor_Trim_A_3m40", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2749.649, 4912.067, 934.0), (0.0, 90.31427388305323, -0.0), (1.0, 0.78125, 1.0), "Suburbs_Floor_Trim_A_3m41", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2517.6514, 4910.794, 934.0), (0.0, 90.31427388305323, -0.0), (1.0, 0.78125, 1.0), "Suburbs_Floor_Trim_A_3m42", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3847.4985, 4903.7866, 934.0), (0.0, 89.44308419505151, -0.0), (1.0, 0.78125, 1.0), "Suburbs_Floor_Trim_A_3m43", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4080.4888, 4901.5215, 934.0), (0.0, 89.44308419505151, -0.0), (1.0, 0.78125, 1.0), "Suburbs_Floor_Trim_A_3m44", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4293.6943, 5000.773, 934.0), (0.0, 114.6524980337065, -0.0), (1.0, 0.78125, 1.0), "Suburbs_Floor_Trim_A_3m45", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3886.0, 1468.0011, 934.0), (0.0, -89.99993822608693, 0.0), (1.0, 0.78125, 1.0), "Suburbs_Floor_Trim_A_3m47", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3653.0, 1468.0011, 934.0), (0.0, -89.99993822608693, 0.0), (1.0, 0.78125, 1.0), "Suburbs_Floor_Trim_A_3m48", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4116.0, 1468.0012, 934.0), (0.0, -104.99996276911699, 0.0), (1.0, 0.78125, 1.0), "Suburbs_Floor_Trim_A_3m49_153", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4338.166, 1408.472, 934.0), (0.0, -104.99996276911699, 0.0), (1.0, 0.78125, 1.0), "Suburbs_Floor_Trim_A_3m50", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2288.3728, 4907.7275, 934.0), (0.0, 65.3142887648547, -0.0), (1.0, 0.78125, 1.0), "Suburbs_Floor_Trim_A_3m52", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4502.731, 5096.709, 934.0), (0.0, 114.6524980337065, -0.0), (1.0, 0.78125, 1.0), "Suburbs_Floor_Trim_A_3m54", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1668.3748, 3102.269, 934.0), (0.0, -179.99991120752276, 0.0), (1.0, 0.78125, 1.0), "Suburbs_Floor_Trim_A_3m55", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1668.3748, 3334.269, 934.0), (0.0, -179.99991120752276, 0.0), (1.0, 0.78125, 1.0), "Suburbs_Floor_Trim_A_3m56", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1668.3755, 2625.4395, 934.0), (0.0, -179.99991120752276, 0.0), (1.0, 0.82108617, 1.0), "Suburbs_Floor_Trim_A_3m57", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1668.3755, 2869.269, 934.0), (0.0, -179.99991120752276, 0.0), (1.0, 0.82108617, 1.0), "Suburbs_Floor_Trim_A_3m58", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1805.5925, 1616.049, 934.0), (0.0, -139.99987619914492, 0.0), (1.0, 1.0, 1.0), "Suburbs_Floor_Trim_A_3m59", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1524.0005, 3560.8665, 1454.876), (0.0, 89.99995929348692, -0.0), (1.5, 1.0, 1.5625), "Suburbs_Floor_Trim_A_3m6", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1612.756, 1845.8619, 934.0), (0.0, -139.99987619914492, 0.0), (1.0, 1.0, 1.0), "Suburbs_Floor_Trim_A_3m60_9", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1419.9193, 2075.6748, 934.0), (0.0, -139.99987619914492, 0.0), (1.0, 1.0, 1.0), "Suburbs_Floor_Trim_A_3m61_11", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1560.3601, 4541.1895, 934.0), (0.0, 140.00002700924287, -0.0), (1.0, 0.721393, 1.0), "Suburbs_Floor_Trim_A_3m64", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1698.5593, 4705.8887, 934.0), (0.0, 140.00002700924287, -0.0), (1.0, 0.721393, 1.0), "Suburbs_Floor_Trim_A_3m65", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1836.7585, 4870.5884, 934.0), (0.0, 140.00002700924287, -0.0), (1.0, 0.721393, 1.0), "Suburbs_Floor_Trim_A_3m66", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1974.9578, 5035.2876, 934.0), (0.0, 140.00002700924287, -0.0), (1.0, 0.721393, 1.0), "Suburbs_Floor_Trim_A_3m67", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2800.6182, 4916.0522, 1392.3833), (0.0, -90.00029475174199, 0.0), (1.5, 1.25, 1.9375), "Suburbs_Floor_Trim_A_3m7", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3175.6184, 4916.0513, 1392.3833), (0.0, -90.00029475174199, 0.0), (1.5, 1.25, 1.9375), "Suburbs_Floor_Trim_A_3m8", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2800.6191, 5231.053, 1397.0701), (0.0, 179.9995696979556, -0.0), (1.5, 1.0, 1.9375), "Suburbs_Floor_Trim_A_3m9", _folder)
if a: placed += 1
else: skipped += 1

# Batch 41: StaticMesh'Suburbs_Gate_A_Arch' (10 instances)
_mesh_path = "/Game/Art/Assets/Kits/Architecture/Suburbs/Suburbs_Gate_A_Arch"
_materials = ['/Game/Art/Assets/Kits/Architecture/Suburbs/Materials/Suburbs_Trim_Sheet_A/MI_Suburbs_Trim_Sheet_A']
_folder = "Reconstruction/BD_BB_Chapter5_BrokenSeal/Meshes"
a = spawn_static_mesh(_mesh_path, _materials, (2570.6387, 5074.4395, 1870.0786), (0.0, 0.0001831054740160754, -0.0), (1.875, 1.875, 1.875), "Suburbs_Gate_A_Pillar_Base42", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3789.3882, 5265.6016, 1870.0786), (0.0, -179.99998633961752, -0.0), (1.875, 1.875, 1.875), "Suburbs_Gate_A_Pillar_Base45", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1367.5127, 2587.564, 1870.0786), (0.0, 90.00023965222978, -0.0), (1.875, 1.875, 1.875), "Suburbs_Gate_A_Pillar_Base49", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1176.8243, 3806.313, 1870.0786), (0.0, -89.99999818714215, 0.0), (1.875, 1.875, 1.875), "Suburbs_Gate_A_Pillar_Base53", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3774.3872, 1355.3, 1870.0786), (0.0, -179.99963116978688, 0.0), (1.875, 1.875, 1.875), "Suburbs_Gate_A_Pillar_Base57", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2551.3638, 1164.2269, 1870.0786), (0.0, 0.0, -0.0), (1.875, 1.875, 1.875), "Suburbs_Gate_A_Pillar_Base61", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5003.884, 4216.8706, 1730.0786), (0.0, 40.00021091893493, -0.0), (1.875, 1.875, 1.875), "Suburbs_Gate_A_Pillar_Base77", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5821.0503, 5146.8584, 1730.0786), (0.0, -140.3199895153597, 0.0), (1.875, 1.875, 1.875), "Suburbs_Gate_A_Pillar_Base81", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4768.093, 1931.5051, 1730.0786), (0.0, -49.99987822834905, 0.0), (1.875, 1.875, 1.875), "Suburbs_Gate_A_Pillar_Base89_550", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5688.9976, 1106.447, 1730.0786), (0.0, 128.48835853783626, -0.0), (1.875, 1.875, 1.875), "Suburbs_Gate_A_Pillar_Base93_554", _folder)
if a: placed += 1
else: skipped += 1

# Batch 42: StaticMesh'Suburbs_Gate_A_Pillar_Base' (20 instances)
_mesh_path = "/Game/Art/Assets/Kits/Architecture/Suburbs/Suburbs_Gate_A_Pillar_Base"
_materials = ['/Game/Art/Assets/Kits/Architecture/Suburbs/Materials/Suburbs_Trim_Sheet_A/MI_Suburbs_Trim_Sheet_A']
_folder = "Reconstruction/BD_BB_Chapter5_BrokenSeal/Meshes"
a = spawn_static_mesh(_mesh_path, _materials, (2758.1406, 5261.938, 932.57837), (0.0, -179.99998633961752, -0.0), (1.875, 1.875, 1.875), "Suburbs_Gate_A_Pillar_Base38_287", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3601.8901, 5261.938, 932.57837), (0.0, -179.99998633961752, -0.0), (1.875, 1.875, 1.875), "Suburbs_Gate_A_Pillar_Base40_295", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1180.0127, 2775.065, 932.57837), (0.0, -89.99993822608693, 0.0), (1.875, 1.875, 1.875), "Suburbs_Gate_A_Pillar_Base46", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1180.0137, 3618.816, 932.57837), (0.0, -89.99993822608693, 0.0), (1.875, 1.875, 1.875), "Suburbs_Gate_A_Pillar_Base50", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3586.8862, 1166.937, 932.57837), (0.0, -3.051757709276941e-05, 0.0), (1.875, 1.875, 1.875), "Suburbs_Gate_A_Pillar_Base54", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2743.1348, 1166.9385, 932.57837), (0.0, -3.051757709276941e-05, 0.0), (1.875, 1.875, 1.875), "Suburbs_Gate_A_Pillar_Base58", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2758.1406, 5261.938, 1870.0786), (0.0, -179.99998633961752, -0.0), (1.875, 1.875, 1.875), "Suburbs_Gate_A_Pillar_Base62_75", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3601.8901, 5261.938, 1870.0786), (0.0, -179.99998633961752, -0.0), (1.875, 1.875, 1.875), "Suburbs_Gate_A_Pillar_Base64", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1180.0127, 2775.065, 1870.0786), (0.0, -89.99993822608693, 0.0), (1.875, 1.875, 1.875), "Suburbs_Gate_A_Pillar_Base66", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1180.0137, 3618.816, 1870.0786), (0.0, -89.99993822608693, 0.0), (1.875, 1.875, 1.875), "Suburbs_Gate_A_Pillar_Base68", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3586.8862, 1166.937, 1870.0786), (0.0, -3.051757709276941e-05, 0.0), (1.875, 1.875, 1.875), "Suburbs_Gate_A_Pillar_Base70", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2743.1348, 1166.9385, 1870.0786), (0.0, -3.051757709276941e-05, 0.0), (1.875, 1.875, 1.875), "Suburbs_Gate_A_Pillar_Base72", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5026.997, 4481.0254, 792.57837), (0.0, -139.9999551042143, 0.0), (1.875, 1.875, 1.875), "Suburbs_Gate_A_Pillar_Base74", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5673.347, 5023.378, 792.57837), (0.0, -139.9999551042143, 0.0), (1.875, 1.875, 1.875), "Suburbs_Gate_A_Pillar_Base78", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5026.997, 4481.0254, 1730.0786), (0.0, -139.9999551042143, 0.0), (1.875, 1.875, 1.875), "Suburbs_Gate_A_Pillar_Base82", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5673.347, 5023.378, 1730.0786), (0.0, -139.9999551042143, 0.0), (1.875, 1.875, 1.875), "Suburbs_Gate_A_Pillar_Base84", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5032.2437, 1908.3909, 792.57837), (0.0, 129.99997629291383, -0.0), (1.875, 1.875, 1.875), "Suburbs_Gate_A_Pillar_Base86_547", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5574.595, 1262.0447, 792.57837), (0.0, 129.99997629291383, -0.0), (1.875, 1.875, 1.875), "Suburbs_Gate_A_Pillar_Base90_551", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5032.2437, 1908.3909, 1730.0786), (0.0, 129.99997629291383, -0.0), (1.875, 1.875, 1.875), "Suburbs_Gate_A_Pillar_Base94_555", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5574.595, 1262.0447, 1730.0786), (0.0, 129.99997629291383, -0.0), (1.875, 1.875, 1.875), "Suburbs_Gate_A_Pillar_Base96_557", _folder)
if a: placed += 1
else: skipped += 1

# Batch 43: StaticMesh'Suburbs_Gate_A_Pillar_Capitol' (22 instances)
_mesh_path = "/Game/Art/Assets/Kits/Architecture/Suburbs/Suburbs_Gate_A_Pillar_Capitol"
_materials = ['/Game/Art/Assets/Kits/Architecture/Suburbs/Materials/Suburbs_Trim_Sheet_A/MI_Suburbs_Trim_Sheet_A']
_folder = "Reconstruction/BD_BB_Chapter5_BrokenSeal/Meshes"
a = spawn_static_mesh(_mesh_path, _materials, (2758.1406, 5261.938, 1870.0786), (0.0, -179.99998633961752, -0.0), (1.875, 1.875, 1.875), "Suburbs_Gate_A_Pillar_Base41", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3601.8901, 5261.938, 1870.0786), (0.0, -179.99998633961752, -0.0), (1.875, 1.875, 1.875), "Suburbs_Gate_A_Pillar_Base44", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1180.0127, 2775.065, 1870.0786), (0.0, -89.99993822608693, 0.0), (1.875, 1.875, 1.875), "Suburbs_Gate_A_Pillar_Base48", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1180.0137, 3618.816, 1870.0786), (0.0, -89.99993822608693, 0.0), (1.875, 1.875, 1.875), "Suburbs_Gate_A_Pillar_Base52", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3586.8862, 1166.937, 1870.0786), (0.0, -3.051757709276941e-05, 0.0), (1.875, 1.875, 1.875), "Suburbs_Gate_A_Pillar_Base56", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2743.1348, 1166.9385, 1870.0786), (0.0, -3.051757709276941e-05, 0.0), (1.875, 1.875, 1.875), "Suburbs_Gate_A_Pillar_Base60", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2758.1406, 5261.938, 2620.0808), (0.0, -179.99998633961752, -0.0), (1.875, 1.875, 1.875), "Suburbs_Gate_A_Pillar_Base63_76", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3601.8901, 5261.938, 2620.0808), (0.0, -179.99998633961752, -0.0), (1.875, 1.875, 1.875), "Suburbs_Gate_A_Pillar_Base65", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1180.0127, 2775.065, 2620.0808), (0.0, -89.99993822608693, 0.0), (1.875, 1.875, 1.875), "Suburbs_Gate_A_Pillar_Base67", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1180.0137, 3618.816, 2620.0808), (0.0, -89.99993822608693, 0.0), (1.875, 1.875, 1.875), "Suburbs_Gate_A_Pillar_Base69", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3586.8862, 1166.937, 2620.0808), (0.0, -3.051757709276941e-05, 0.0), (1.875, 1.875, 1.875), "Suburbs_Gate_A_Pillar_Base71", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2743.1348, 1166.9385, 2620.0808), (0.0, -3.051757709276941e-05, 0.0), (1.875, 1.875, 1.875), "Suburbs_Gate_A_Pillar_Base73", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5026.997, 4481.0254, 1730.0786), (0.0, -139.9999551042143, 0.0), (1.875, 1.875, 1.875), "Suburbs_Gate_A_Pillar_Base76", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5673.347, 5023.378, 1730.0786), (0.0, -139.9999551042143, 0.0), (1.875, 1.875, 1.875), "Suburbs_Gate_A_Pillar_Base80", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5026.997, 4481.0254, 2480.0808), (0.0, -139.9999551042143, 0.0), (1.875, 1.875, 1.875), "Suburbs_Gate_A_Pillar_Base83", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5673.347, 5023.378, 2480.0808), (0.0, -139.9999551042143, 0.0), (1.875, 1.875, 1.875), "Suburbs_Gate_A_Pillar_Base85", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5032.2437, 1908.3909, 1730.0786), (0.0, 129.99997629291383, -0.0), (1.875, 1.875, 1.875), "Suburbs_Gate_A_Pillar_Base88_549", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5574.595, 1262.0447, 1730.0786), (0.0, 129.99997629291383, -0.0), (1.875, 1.875, 1.875), "Suburbs_Gate_A_Pillar_Base92_553", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5032.2437, 1908.3909, 2480.0808), (0.0, 129.99997629291383, -0.0), (1.875, 1.875, 1.875), "Suburbs_Gate_A_Pillar_Base95_556", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5574.595, 1262.0447, 2480.0808), (0.0, 129.99997629291383, -0.0), (1.875, 1.875, 1.875), "Suburbs_Gate_A_Pillar_Base97_558", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1964.7534, 1307.1658, 1000.0), (0.0, 90.00055404382421, -0.0), (1.0, 1.0, 1.0), "Suburbs_Gate_A_Pillar_Capitol_11", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1314.7534, 2062.1658, 1000.0), (0.0, 0.0005178451337932662, -0.0), (1.0, 1.0, 1.0), "Suburbs_Gate_A_Pillar_Capitol2", _folder)
if a: placed += 1
else: skipped += 1

# Batch 44: StaticMesh'Suburbs_Gate_A_Pillar_Shaft' (10 instances)
_mesh_path = "/Game/Art/Assets/Kits/Architecture/Suburbs/Suburbs_Gate_A_Pillar_Shaft"
_materials = ['/Game/Art/Assets/Kits/Architecture/Suburbs/Materials/Suburbs_Trim_Sheet_A/MI_Suburbs_Trim_Sheet_A']
_folder = "Reconstruction/BD_BB_Chapter5_BrokenSeal/Meshes"
a = spawn_static_mesh(_mesh_path, _materials, (2758.1406, 5261.938, 1495.0786), (0.0, -179.99998633961752, -0.0), (1.875, 1.875, 1.875), "Suburbs_Gate_A_Pillar_Base39", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3601.8901, 5261.938, 1495.0786), (0.0, -179.99998633961752, -0.0), (1.875, 1.875, 1.875), "Suburbs_Gate_A_Pillar_Base43", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1180.0127, 2775.065, 1495.0786), (0.0, -89.99993822608693, 0.0), (1.875, 1.875, 1.875), "Suburbs_Gate_A_Pillar_Base47", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1180.0137, 3618.816, 1495.0786), (0.0, -89.99993822608693, 0.0), (1.875, 1.875, 1.875), "Suburbs_Gate_A_Pillar_Base51", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3586.8862, 1166.937, 1495.0786), (0.0, -3.051757709276941e-05, 0.0), (1.875, 1.875, 1.875), "Suburbs_Gate_A_Pillar_Base55", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2743.1348, 1166.9385, 1495.0786), (0.0, -3.051757709276941e-05, 0.0), (1.875, 1.875, 1.875), "Suburbs_Gate_A_Pillar_Base59", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5026.997, 4481.0254, 1355.0786), (0.0, -139.9999551042143, 0.0), (1.875, 1.875, 1.875), "Suburbs_Gate_A_Pillar_Base75", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5673.347, 5023.378, 1355.0786), (0.0, -139.9999551042143, 0.0), (1.875, 1.875, 1.875), "Suburbs_Gate_A_Pillar_Base79", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5032.2437, 1908.3909, 1355.0786), (0.0, 129.99997629291383, -0.0), (1.875, 1.875, 1.875), "Suburbs_Gate_A_Pillar_Base87_548", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5574.595, 1262.0447, 1355.0786), (0.0, 129.99997629291383, -0.0), (1.875, 1.875, 1.875), "Suburbs_Gate_A_Pillar_Base91_552", _folder)
if a: placed += 1
else: skipped += 1

# Batch 45: StaticMesh'Suburbs_Gate_D_Arch' (6 instances)
_mesh_path = "/Game/Art/Assets/Kits/Architecture/Suburbs/Suburbs_Gate_D_Arch"
_materials = ['/Game/Art/Assets/Kits/Architecture/Suburbs/Materials/Suburbs_Trim_Sheet_A/MI_Suburbs_Trim_Sheet_A']
_folder = "Reconstruction/BD_BB_Chapter5_BrokenSeal/Meshes"
a = spawn_static_mesh(_mesh_path, _materials, (1490.0, 3080.0, 1160.0), (0.0, -89.99993822608693, 0.0), (1.0, 1.0, 1.0), "Suburbs_Gate_D_Arch_485", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1490.0, 3265.0, 1160.0), (0.0, 90.0001164887758, -0.0), (1.0, 1.0, 1.0), "Suburbs_Gate_D_Arch2", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3265.004, 1485.0024, 1040.0), (0.0, 0.0, -0.0), (1.0, 1.0, 1.09375), "Suburbs_Gate_D_Arch3", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3080.004, 1485.0024, 1040.0), (0.0, -179.99998633961752, -0.0), (1.0, 1.0, 1.09375), "Suburbs_Gate_D_Arch4", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3264.9956, 4955.0024, 1040.0), (0.0, 0.0, -0.0), (1.0, 1.0, 1.09375), "Suburbs_Gate_D_Arch5", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3079.9946, 4955.003, 1040.0), (0.0, -179.99988388675877, 0.0), (1.0, 1.0, 1.09375), "Suburbs_Gate_D_Arch6", _folder)
if a: placed += 1
else: skipped += 1

# Batch 46: StaticMesh'Suburbs_Stairs_Medium_C_NonDest' (58 instances)
_mesh_path = "/Game/Art/Assets/Kits/Architecture/Suburbs/Suburbs_Stairs_Medium_C_NonDest"
_materials = ['/Game/Art/Assets/Kits/Architecture/Suburbs/Materials/Stairs_Medium_C_NonDest/MI_Stairs_Medium_C_NonDes_Suburbs', '/Game/Art/Assets/Kits/Architecture/Suburbs/Destructable/Materials/MI_Suburbs_Wall_Non_Dest']
_folder = "Reconstruction/BD_BB_Chapter5_BrokenSeal/Meshes"
a = spawn_static_mesh(_mesh_path, _materials, (2481.3677, 257.2945, 1200.0), (0.0, 69.73390236701766, -0.0), (1.0, 1.0, 1.0), "BP_Suburbs_Stairs_Large_A1_Breakable10", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2199.9392, 361.20178, 1000.0), (0.0, 69.73390236701766, -0.0), (1.0, 1.0, 1.0), "BP_Suburbs_Stairs_Large_A1_Breakable11_48", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2585.2847, 538.72314, 1200.0), (0.0, 69.73390236701766, -0.0), (1.0, 1.0, 1.0), "BP_Suburbs_Stairs_Large_A1_Breakable12", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2689.1992, 820.1471, 1200.0), (0.0, 69.73390236701766, -0.0), (1.0, 1.0, 1.0), "BP_Suburbs_Stairs_Large_A1_Breakable13", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2303.8567, 642.6305, 1000.0), (0.0, 69.73390236701766, -0.0), (1.0, 1.0, 1.0), "BP_Suburbs_Stairs_Large_A1_Breakable14_46", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2407.771, 924.05475, 1000.0), (0.0, 69.73390236701766, -0.0), (1.0, 1.0, 1.0), "BP_Suburbs_Stairs_Large_A1_Breakable17_47", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (465.33398, 3816.5986, 1200.0), (0.0, -25.937437576359322, 0.0), (1.0, 1.0, 1.0), "BP_Suburbs_Stairs_Large_A1_Breakable18", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (735.1157, 3685.3823, 1200.0), (0.0, -25.937437576359322, 0.0), (1.0, 1.0, 1.0), "BP_Suburbs_Stairs_Large_A1_Breakable19_2", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (596.5507, 4086.3804, 1000.0), (0.0, -25.937437576359322, 0.0), (1.0, 1.0, 1.0), "BP_Suburbs_Stairs_Large_A1_Breakable20_5", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2022.4277, 746.5454, 800.0), (0.0, 69.73390236701766, -0.0), (1.0, 1.0, 1.0), "BP_Suburbs_Stairs_Large_A1_Breakable21_52", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (777.1113, 2732.078, 1200.0), (0.0, -154.6876632220656, 0.0), (1.0, 1.0, 1.0), "BP_Suburbs_Stairs_Large_A1_Breakable22", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2126.3423, 1027.9692, 800.0), (0.0, 69.73390236701766, -0.0), (1.0, 1.0, 1.0), "BP_Suburbs_Stairs_Large_A1_Breakable23_53", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (505.91418, 2603.8118, 1200.0), (0.0, -154.6876632220656, 0.0), (1.0, 1.0, 1.0), "BP_Suburbs_Stairs_Large_A1_Breakable24_10", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (234.71704, 2475.5457, 1200.0), (0.0, -154.6876632220656, 0.0), (1.0, 1.0, 1.0), "BP_Suburbs_Stairs_Large_A1_Breakable25_12", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1918.5116, 465.1167, 800.0), (0.0, 69.73390236701766, -0.0), (1.0, 1.0, 1.0), "BP_Suburbs_Stairs_Large_A1_Breakable26_54", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (195.55234, 3947.8152, 1200.0), (0.0, -25.937437576359322, 0.0), (1.0, 1.0, 1.0), "BP_Suburbs_Stairs_Large_A1_Breakable27_58", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4966.624, 5676.3833, 1200.0), (0.0, -135.62515674238472, 0.0), (1.0, 1.0, 1.0), "BP_Suburbs_Stairs_Large_A1_Breakable28", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5176.428, 5461.95, 1000.0), (0.0, -135.62515674238472, 0.0), (1.0, 1.0, 1.0), "BP_Suburbs_Stairs_Large_A1_Breakable29_36", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5043.8438, 1643.3046, 900.0), (0.0, -50.625366284801885, 0.0), (1.0, 1.0, 1.0), "BP_Suburbs_Stairs_Large_A1_Breakable3_4", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4752.1875, 5466.58, 1200.0), (0.0, -135.62515674238472, 0.0), (1.0, 1.0, 1.0), "BP_Suburbs_Stairs_Large_A1_Breakable30", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4537.756, 5256.7793, 1200.0), (0.0, -135.62515674238472, 0.0), (1.0, 1.0, 1.0), "BP_Suburbs_Stairs_Large_A1_Breakable31", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4747.56, 5042.346, 1000.0), (0.0, -135.62515674238472, 0.0), (1.0, 1.0, 1.0), "BP_Suburbs_Stairs_Large_A1_Breakable32_34", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4961.9917, 5252.147, 1000.0), (0.0, -135.62515674238472, 0.0), (1.0, 1.0, 1.0), "BP_Suburbs_Stairs_Large_A1_Breakable33_35", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2728.202, 5619.5537, 1200.0), (0.0, 109.68755816276153, -0.0), (1.0599602, 1.0, 1.0), "BP_Suburbs_Stairs_Large_A1_Breakable34", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2445.739, 5518.486, 1000.0), (0.0, 109.68755816276153, -0.0), (1.05996, 1.0, 1.0), "BP_Suburbs_Stairs_Large_A1_Breakable35_28", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2621.077, 5918.954, 1200.0), (0.0, 109.68755816276153, -0.0), (1.0599602, 1.0, 1.0), "BP_Suburbs_Stairs_Large_A1_Breakable36", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (866.3324, 3955.164, 1000.0), (0.0, -25.937437576359322, 0.0), (1.0, 1.0, 1.0), "BP_Suburbs_Stairs_Large_A1_Breakable37", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (727.76746, 4356.161, 800.0), (0.0, -25.937437576359322, 0.0), (1.0, 1.0, 1.0), "BP_Suburbs_Stairs_Large_A1_Breakable38", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4514.3335, 1208.7512, 1200.0), (0.0, -50.62548606624552, 0.0), (1.0, 1.0, 1.0), "BP_Suburbs_Stairs_Large_A1_Breakable4_5", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (997.54913, 4224.9453, 800.0), (0.0, -25.937437576359322, 0.0), (1.0, 1.0, 1.0), "BP_Suburbs_Stairs_Large_A1_Breakable42", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (905.3771, 2460.881, 1000.0), (0.0, -154.6876632220656, 0.0), (1.0, 1.0, 1.0), "BP_Suburbs_Stairs_Large_A1_Breakable43", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (634.17993, 2332.615, 1000.0), (0.0, -154.6876632220656, 0.0), (1.0, 1.0, 1.0), "BP_Suburbs_Stairs_Large_A1_Breakable44", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (362.9828, 2204.3489, 1000.0), (0.0, -154.6876632220656, 0.0), (1.0, 1.0, 1.0), "BP_Suburbs_Stairs_Large_A1_Breakable45", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1033.6428, 2189.6843, 800.0), (0.0, -154.6876632220656, 0.0), (1.0, 1.0, 1.0), "BP_Suburbs_Stairs_Large_A1_Breakable46", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (762.4457, 2061.4182, 800.0), (0.0, -154.6876632220656, 0.0), (1.0, 1.0, 1.0), "BP_Suburbs_Stairs_Large_A1_Breakable47", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (491.24854, 1933.1521, 800.0), (0.0, -154.6876632220656, 0.0), (1.0, 1.0, 1.0), "BP_Suburbs_Stairs_Large_A1_Breakable48", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2338.614, 5817.886, 1000.0), (0.0, 109.68755816276153, -0.0), (1.05996, 1.0, 1.0), "BP_Suburbs_Stairs_Large_A1_Breakable49", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5234.162, 1411.4012, 900.0), (0.0, -50.625366284801885, 0.0), (1.0, 1.0, 1.0), "BP_Suburbs_Stairs_Large_A1_Breakable5", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2163.2761, 5417.418, 800.0), (0.0, 109.68755816276153, -0.0), (1.05996, 1.0, 1.0), "BP_Suburbs_Stairs_Large_A1_Breakable50", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2056.1511, 5716.8184, 800.0), (0.0, 109.68755816276153, -0.0), (1.05996, 1.0, 1.0), "BP_Suburbs_Stairs_Large_A1_Breakable51", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4957.3643, 4827.913, 800.0), (0.0, -135.62515674238472, 0.0), (1.0, 1.0, 1.0), "BP_Suburbs_Stairs_Large_A1_Breakable52", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5171.796, 5037.714, 800.0), (0.0, -135.62515674238472, 0.0), (1.0, 1.0, 1.0), "BP_Suburbs_Stairs_Large_A1_Breakable53", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5386.2324, 5247.517, 800.0), (0.0, -135.62515674238472, 0.0), (1.0, 1.0, 1.0), "BP_Suburbs_Stairs_Large_A1_Breakable54", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (326.76904, 4217.5977, 1000.0), (0.0, -25.937437576359322, 0.0), (1.0, 1.0, 1.0), "BP_Suburbs_Stairs_Large_A1_Breakable55", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (457.98578, 4487.3784, 800.0), (0.0, -25.937437576359322, 0.0), (1.0, 1.0, 1.0), "BP_Suburbs_Stairs_Large_A1_Breakable56", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4704.652, 976.84766, 1200.0), (0.0, -50.62548606624552, 0.0), (1.0, 1.0, 1.0), "BP_Suburbs_Stairs_Large_A1_Breakable6", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4894.968, 744.9424, 1200.0), (0.0, -50.62548606624552, 0.0), (1.0, 1.0, 1.0), "BP_Suburbs_Stairs_Large_A1_Breakable7_11", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5424.4785, 1179.4974, 900.0), (0.0, -50.625366284801885, 0.0), (1.0, 1.0, 1.0), "BP_Suburbs_Stairs_Large_A1_Breakable8", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5045.0, 4260.0, 734.5757), (0.0, -89.99993822608693, 0.0), (1.0, 1.0, 1.0), "Suburbs_Stairs_Medium_C_NonDest_20", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4670.0, 3360.0, 986.5757), (0.0, -89.99993822608693, 0.0), (1.0, 1.0, 1.0), "Suburbs_Stairs_Medium_C_NonDest10", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4670.0, 3045.742, 986.5757), (0.0, -89.99993822608693, 0.0), (1.125, 1.0, 1.0), "Suburbs_Stairs_Medium_C_NonDest11", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5045.0, 3960.0, 734.5757), (0.0, -89.99993822608693, 0.0), (1.0, 1.0, 1.0), "Suburbs_Stairs_Medium_C_NonDest2", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5045.0, 3660.0, 734.5757), (0.0, -89.99993822608693, 0.0), (1.0, 1.0, 1.0), "Suburbs_Stairs_Medium_C_NonDest3", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4965.9526, 3360.0, 785.4773), (0.0, -89.99993822608693, 0.0), (1.0, 1.0, 1.0), "Suburbs_Stairs_Medium_C_NonDest5", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4965.953, 3045.742, 785.4773), (0.0, -89.99993822608693, 0.0), (1.125, 1.0, 1.0), "Suburbs_Stairs_Medium_C_NonDest6", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5037.0444, 2760.0, 734.5757), (0.0, -89.99993822608693, 0.0), (1.0, 1.0, 1.0), "Suburbs_Stairs_Medium_C_NonDest7", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5037.0444, 2460.0, 734.5757), (0.0, -89.99993822608693, 0.0), (1.0, 1.0, 1.0), "Suburbs_Stairs_Medium_C_NonDest8", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5037.045, 2160.0, 734.5757), (0.0, -89.99993822608693, 0.0), (1.0, 1.0, 1.0), "Suburbs_Stairs_Medium_C_NonDest9", _folder)
if a: placed += 1
else: skipped += 1

# Batch 47: StaticMesh'Suburbs_Stairs_Small_B_NonDest' (22 instances)
_mesh_path = "/Game/Art/Assets/Kits/Architecture/Suburbs/Suburbs_Stairs_Small_B_NonDest"
_materials = ['/Game/Art/Assets/Kits/Architecture/Suburbs/Destructable/Materials/MI_Suburbs_Wall_Non_Dest', '/Game/Art/Assets/Kits/Architecture/Suburbs/Materials/Stairs_Medium_C_NonDest/MI_Stairs_Medium_C_NonDes_Suburbs']
_folder = "Reconstruction/BD_BB_Chapter5_BrokenSeal/Meshes"
a = spawn_static_mesh(_mesh_path, _materials, (1791.6609, 1633.0624, 838.4866), (0.0, 129.99989450513715, -0.0), (1.0, 1.0, 1.0), "Ruins_Stairs_Medium_B_30", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1805.311, 1383.4353, 738.4866), (0.0, 129.99989450513715, -0.0), (1.0, 1.0, 1.0), "Ruins_Stairs_Medium_B10", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1933.8682, 1230.2262, 738.4866), (0.0, 129.99989450513715, -0.0), (1.0, 1.0, 1.0), "Ruins_Stairs_Medium_B11", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1291.0823, 1996.2716, 738.4866), (0.0, 129.99989450513715, -0.0), (1.0, 1.0, 1.0), "Ruins_Stairs_Medium_B12", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1419.6394, 1843.0627, 738.4866), (0.0, 129.99989450513715, -0.0), (1.0, 1.0, 1.0), "Ruins_Stairs_Medium_B13", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1548.1965, 1689.854, 738.4866), (0.0, 129.99989450513715, -0.0), (1.0, 1.0, 1.0), "Ruins_Stairs_Medium_B14", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1920.218, 1479.8533, 838.4866), (0.0, 129.99989450513715, -0.0), (1.0, 1.0, 1.0), "Ruins_Stairs_Medium_B2_86", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2048.7751, 1326.6442, 838.4866), (0.0, 129.99989450513715, -0.0), (1.0, 1.0, 1.0), "Ruins_Stairs_Medium_B5_88", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1405.9891, 2092.6897, 838.4866), (0.0, 129.99989450513715, -0.0), (1.0, 1.0, 1.0), "Ruins_Stairs_Medium_B6", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1534.5463, 1939.4807, 838.4866), (0.0, 129.99989450513715, -0.0), (1.0, 1.0, 1.0), "Ruins_Stairs_Medium_B7", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1663.1034, 1786.272, 838.4866), (0.0, 129.99989450513715, -0.0), (1.0, 1.0, 1.0), "Ruins_Stairs_Medium_B8", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1676.7539, 1536.6444, 738.4866), (0.0, 129.99989450513715, -0.0), (1.0, 1.0, 1.0), "Ruins_Stairs_Medium_B9", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1421.5555, 4350.3164, 837.8291), (0.0, 49.99994436445624, -0.0), (1.0, 1.0, 1.0), "Suburbs_Stairs_Medium_B10", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1306.6488, 4446.7354, 737.8291), (0.0, 49.99994436445624, -0.0), (1.0, 1.0, 1.0), "Suburbs_Stairs_Medium_B11", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1550.1133, 4503.526, 837.8291), (0.0, 49.99994436445624, -0.0), (1.0, 1.0, 1.0), "Suburbs_Stairs_Medium_B2", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1678.6709, 4656.735, 837.8291), (0.0, 49.99994436445624, -0.0), (1.0, 1.0, 1.0), "Suburbs_Stairs_Medium_B3_194", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1435.2065, 4599.945, 737.8291), (0.0, 49.99994436445624, -0.0), (1.0, 1.0, 1.0), "Suburbs_Stairs_Medium_B4", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1563.7642, 4753.154, 737.8291), (0.0, 49.99994436445624, -0.0), (1.0, 1.0, 1.0), "Suburbs_Stairs_Medium_B5", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1807.2285, 4809.944, 837.8291), (0.0, 49.99994436445624, -0.0), (1.0, 1.0, 1.0), "Suburbs_Stairs_Medium_B6", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1692.3218, 4906.363, 737.8291), (0.0, 49.99994436445624, -0.0), (1.0, 1.0, 1.0), "Suburbs_Stairs_Medium_B7", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1935.7861, 4963.153, 837.8291), (0.0, 49.99994436445624, -0.0), (1.0, 1.0, 1.0), "Suburbs_Stairs_Medium_B8", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1820.8794, 5059.572, 737.8291), (0.0, 49.99994436445624, -0.0), (1.0, 1.0, 1.0), "Suburbs_Stairs_Medium_B9", _folder)
if a: placed += 1
else: skipped += 1

# Batch 48: StaticMesh'Suburbs_Stairs_Small_C_CornerExt_NonDest' (2 instances)
_mesh_path = "/Game/Art/Assets/Kits/Architecture/Suburbs/Suburbs_Stairs_Small_C_CornerExt_NonDest"
_materials = ['/Game/Art/Assets/Kits/Architecture/Suburbs/Destructable/Materials/MI_Suburbs_Wall_Non_Dest', '/Game/Art/Assets/Kits/Architecture/Suburbs/Materials/Stairs_Medium_C_NonDest/MI_Stairs_Medium_C_NonDes_Suburbs']
_folder = "Reconstruction/BD_BB_Chapter5_BrokenSeal/Meshes"
a = spawn_static_mesh(_mesh_path, _materials, (875.0001, 2890.0, 1350.0), (0.0, 90.00001925454477, -0.0), (1.0, 1.0, 1.0), "Suburbs_Stairs_Small_C_CornerExt_NonDest_104", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (875.0, 3490.0, 1350.0), (0.0, 3.1471253883608903e-05, -0.0), (1.0, 1.0, 1.0), "Suburbs_Stairs_Small_C_CornerExt_NonDest2", _folder)
if a: placed += 1
else: skipped += 1

# Batch 49: StaticMesh'Suburbs_Stairs_Small_C_NonDest' (6 instances)
_mesh_path = "/Game/Art/Assets/Kits/Architecture/Suburbs/Suburbs_Stairs_Small_C_NonDest"
_materials = ['/Game/Art/Assets/Kits/Architecture/Suburbs/Destructable/Materials/MI_Suburbs_Wall_Non_Dest', '/Game/Art/Assets/Kits/Architecture/Suburbs/Materials/Stairs_Medium_C_NonDest/MI_Stairs_Medium_C_NonDes_Suburbs']
_folder = "Reconstruction/BD_BB_Chapter5_BrokenSeal/Meshes"
a = spawn_static_mesh(_mesh_path, _materials, (4936.557, 1167.1638, 1100.0), (0.0, -50.62548606624552, 0.0), (1.0, 1.0, 1.0), "Suburbs_Stairs_Small_C_NonDest_11", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4746.2417, 1399.0685, 1100.0), (0.0, -50.62548606624552, 0.0), (1.0, 1.0, 1.0), "Suburbs_Stairs_Small_C_NonDest2", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5126.873, 935.2591, 1100.0), (0.0, -50.62548606624552, 0.0), (1.0, 1.0, 1.0), "Suburbs_Stairs_Small_C_NonDest3", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5466.0737, 1601.7189, 800.0), (0.0, -50.62548606624552, 0.0), (1.0, 1.0, 1.0), "Suburbs_Stairs_Small_C_NonDest4", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5275.7583, 1833.6235, 800.0), (0.0, -50.62548606624552, 0.0), (1.0, 1.0, 1.0), "Suburbs_Stairs_Small_C_NonDest5", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5656.3896, 1369.8141, 800.0), (0.0, -50.62548606624552, 0.0), (1.0, 1.0, 1.0), "Suburbs_Stairs_Small_C_NonDest6", _folder)
if a: placed += 1
else: skipped += 1

# Batch 50: StaticMesh'Suburbs_Stairs_Small_D_NonDest' (45 instances)
_mesh_path = "/Game/Art/Assets/Kits/Architecture/Suburbs/Suburbs_Stairs_Small_D_NonDest"
_materials = ['/Game/Art/Assets/Kits/Architecture/Suburbs/Destructable/Materials/MI_Suburbs_Wall_Non_Dest', '/Game/Art/Assets/Kits/Architecture/Suburbs/Materials/Stairs_Medium_C_NonDest/MI_Stairs_Medium_C_NonDes_Suburbs', '/Game/Art/Assets/Kits/Architecture/Suburbs/Destructable/Materials/MI_Suburbs_Wall_Non_Dest']
_folder = "Reconstruction/BD_BB_Chapter5_BrokenSeal/Meshes"
a = spawn_static_mesh(_mesh_path, _materials, (1806.915, 407.8976, 1925.0), (-2.273010664415862e-12, 154.35291837241388, -179.99976777355775), (1.0, 1.0, 1.0), "Suburbs_Stairs_Small_D_NonDest_29", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5333.2773, 1041.0923, 1303.2734), (0.0, 36.333225664498556, -0.0), (1.0, 1.0, 1.0), "Suburbs_Stairs_Small_D_NonDest10", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5530.821, 5237.8994, 2009.2736), (6.602606357227712e-12, -44.072113597532606, -179.9997677735812), (1.0, 1.0, 1.0), "Suburbs_Stairs_Small_D_NonDest11", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5099.761, 5655.255, 2009.2736), (7.603645213230005e-12, -44.07046431543114, -179.99976777355494), (1.0, 1.0, 1.0), "Suburbs_Stairs_Small_D_NonDest12", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5485.6094, 5191.201, 1403.2734), (0.0, 135.92851443232846, -0.0), (1.0, 1.0, 1.0), "Suburbs_Stairs_Small_D_NonDest13", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5270.077, 5399.877, 1403.2734), (0.0, 135.9289850913951, -0.0), (1.0, 1.0, 1.0), "Suburbs_Stairs_Small_D_NonDest14", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5054.5464, 5608.5596, 1403.2734), (0.0, 135.92980587527035, -0.0), (1.0, 1.0, 1.0), "Suburbs_Stairs_Small_D_NonDest15", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2453.2341, 6174.209, 2029.2736), (-3.3122781876086606e-12, 18.557824336428233, -179.99976777354624), (1.0, 1.0, 1.0), "Suburbs_Stairs_Small_D_NonDest16", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1886.0132, 5978.544, 2029.2736), (3.217082625950187e-12, 18.559066378383775, -179.99976777359612), (1.0, 1.0, 1.0), "Suburbs_Stairs_Small_D_NonDest17", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2475.51, 6107.8496, 1403.2734), (0.0, -161.44185646674234, 0.0), (1.0, 1.0, 1.0), "Suburbs_Stairs_Small_D_NonDest18", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2191.1052, 6012.385, 1403.2734), (0.0, -161.44036979232652, 0.0), (1.0, 1.0, 1.0), "Suburbs_Stairs_Small_D_NonDest19", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2349.9429, 152.66087, 1925.0), (-2.273010664415862e-12, 154.35291837241388, -179.99976777355775), (1.0, 1.0, 1.0), "Suburbs_Stairs_Small_D_NonDest2", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1906.6929, 5916.924, 1403.2734), (0.0, -161.44052014760408, 0.0), (1.0, 1.0, 1.0), "Suburbs_Stairs_Small_D_NonDest20", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (410.99664, 4558.119, 2029.2736), (-1.052205044252654e-11, 73.21066748122561, -179.99976777359), (1.0, 1.0, 1.0), "Suburbs_Stairs_Small_D_NonDest21", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (237.6402, 3983.7097, 2029.2736), (9.357260253626564e-12, 73.21286400871695, -179.99976777354632), (1.0, 1.0, 1.0), "Suburbs_Stairs_Small_D_NonDest22", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (468.43652, 4540.786, 1403.2734), (0.0, -106.79085755639628, 0.0), (1.0, 1.0, 1.0), "Suburbs_Stairs_Small_D_NonDest23", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (381.75928, 4253.581, 1403.2734), (0.0, -106.78857750675016, 0.0), (1.0, 1.0, 1.0), "Suburbs_Stairs_Small_D_NonDest24", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (295.07715, 3966.3708, 1403.2734), (0.0, -106.78851104565209, 0.0), (1.0, 1.0, 1.0), "Suburbs_Stairs_Small_D_NonDest25", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (215.2612, 2399.9194, 2029.2736), (2.6300823250576726e-12, 109.3794294061619, -179.99976777355462), (1.0, 1.0, 1.0), "Suburbs_Stairs_Small_D_NonDest26", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (414.3159, 1833.9034, 2029.2736), (-6.350242500119642e-12, 109.38152271379613, -179.99976777355076), (1.0, 1.0, 1.0), "Suburbs_Stairs_Small_D_NonDest27", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (271.86035, 2419.8267, 1403.2734), (0.0, -70.62445869264327, 0.0), (1.0, 1.0, 1.0), "Suburbs_Stairs_Small_D_NonDest28", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (371.38916, 2136.817, 1403.2734), (0.0, -70.62212631230469, 0.0), (1.0, 1.0, 1.0), "Suburbs_Stairs_Small_D_NonDest29", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1837.2164, 470.99805, 1294.0), (0.0, -25.648438916826585, 0.0), (1.0, 1.0, 1.0), "Suburbs_Stairs_Small_D_NonDest3_46", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (470.91846, 1853.8052, 1403.2734), (0.0, -70.62195200071199, 0.0), (1.0, 1.0, 1.0), "Suburbs_Stairs_Small_D_NonDest30", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (875.0001, 3040.0, 1400.0), (0.0, 90.00009542133918, -0.0), (1.0, 1.0, 1.0), "Suburbs_Stairs_Small_D_NonDest31_100", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (874.9997, 3340.0, 1400.0), (0.0, 90.00009542133918, -0.0), (1.0, 1.0, 1.0), "Suburbs_Stairs_Small_D_NonDest32", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3469.2864, 18.89268, 1925.0062), (-0.00015258791288046353, 179.35297286043527, -179.99980192457681), (1.0, 1.0, 1.0), "Suburbs_Stairs_Small_D_NonDest33", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2839.3264, 26.006966, 1925.0046), (-0.00015258791288046353, 179.35297286043527, -179.99980192457681), (1.0, 1.0, 1.0), "Suburbs_Stairs_Small_D_NonDest34", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4446.0854, 334.77286, 1925.008), (-6.103515029449487e-05, -159.99698654170217, -179.99976777354505), (1.0, 1.0, 1.0), "Suburbs_Stairs_Small_D_NonDest35", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3854.1006, 119.23665, 1925.007), (-6.103515029449487e-05, -159.99698654170217, -179.99976777354505), (1.0, 1.0, 1.0), "Suburbs_Stairs_Small_D_NonDest36", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (107.75754, 3489.9763, 2029.2736), (8.148109586966663e-12, 85.98471480079044, -179.99976777356974), (1.0, 1.0, 1.0), "Suburbs_Stairs_Small_D_NonDest37", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (65.712395, 2891.4536, 2029.2736), (4.1521466537208635e-12, 85.98682508067796, -179.99976777356434), (1.0, 1.0, 1.0), "Suburbs_Stairs_Small_D_NonDest38", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (176.93213, 3456.696, 1403.2734), (4.098112841517545e-05, -93.70363789222067, 1.6915099079979597e-06), (1.0, 1.0, 1.0), "Suburbs_Stairs_Small_D_NonDest39", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2107.6504, 341.12842, 1294.0), (0.0, -25.648438916826585, 0.0), (1.0, 1.0, 1.0), "Suburbs_Stairs_Small_D_NonDest4", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (157.5596, 3157.3225, 1403.2734), (4.0999995613686666e-05, -93.70363789222068, 1.6914219968248091e-06), (1.0, 1.0, 1.0), "Suburbs_Stairs_Small_D_NonDest40", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (138.18794, 2857.948, 1403.2734), (4.0999995613686666e-05, -93.70363789222068, 1.6914219968248091e-06), (1.0, 1.0, 1.0), "Suburbs_Stairs_Small_D_NonDest41", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4627.9634, 5912.6924, 2010.162), (-0.00012207030686111679, -19.593721023919073, -179.99976777359743), (1.0, 1.0, 1.0), "Suburbs_Stairs_Small_D_NonDest42", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4035.8005, 6112.8643, 2010.1635), (-0.00012207029373924352, -19.11969038656308, -179.99976777354283), (1.230001, 1.0, 1.0), "Suburbs_Stairs_Small_D_NonDest43", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3579.474, 6256.505, 2010.1616), (-0.00018310547794202531, -3.3138123054151865, -179.99976777358822), (1.0, 1.0, 1.0), "Suburbs_Stairs_Small_D_NonDest44", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2954.9412, 6282.6494, 2010.1637), (-0.00018310550272252483, -2.839782781834142, -179.99976777358094), (1.230001, 1.0, 1.0), "Suburbs_Stairs_Small_D_NonDest45", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2378.0815, 211.25244, 1294.0), (0.0, -25.648438916826585, 0.0), (1.0, 1.0, 1.0), "Suburbs_Stairs_Small_D_NonDest5", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4891.3784, 629.2372, 1929.2736), (-3.822595646843297e-12, -143.6673342914027, -179.99976777355397), (1.0, 1.0, 1.0), "Suburbs_Stairs_Small_D_NonDest6", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5371.7837, 988.7308, 1929.2736), (-2.8370016582339435e-12, -143.66567568881948, -179.99976777352853), (1.0, 1.0, 1.0), "Suburbs_Stairs_Small_D_NonDest7", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4855.156, 678.9366, 1303.2734), (0.0, 37.95672765743992, -0.0), (1.0, 1.0, 1.0), "Suburbs_Stairs_Small_D_NonDest8", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5091.59, 863.3658, 1303.2734), (0.0, 36.33102500001365, -0.0), (1.0, 1.0, 1.0), "Suburbs_Stairs_Small_D_NonDest9", _folder)
if a: placed += 1
else: skipped += 1

# Batch 51: StaticMesh'Suburbs_Wall_Thick_3x1m_B' (8 instances)
_mesh_path = "/Game/Art/Assets/Kits/Architecture/Suburbs/Suburbs_Wall_Thick_3x1m_B"
_materials = ['/Game/Art/Assets/Kits/Architecture/Suburbs/Destructable/Materials/MI_Suburbs_Wall_Non_Dest']
_folder = "Reconstruction/BD_BB_Chapter5_BrokenSeal/Meshes"
a = spawn_static_mesh(_mesh_path, _materials, (1430.0, 3485.8652, 980.9614), (0.0, -179.99998633961752, -0.0), (1.5, 1.5, 1.5625), "Suburbs_Wall_Thick_3x1m_B_24", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3473.8628, 1421.9155, 799.2644), (0.0, -90.0001164887758, 0.0), (1.5, 1.5, 1.9375), "Suburbs_Wall_Thick_3x1m_B10", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1430.0, 2885.8652, 980.9614), (0.0, -179.99998633961752, -0.0), (1.5, 1.5, 1.5625), "Suburbs_Wall_Thick_3x1m_B2_27", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1280.0, 3485.0, 980.9614), (0.0, -179.99998633961752, -0.0), (1.5, 1.5, 1.5625), "Suburbs_Wall_Thick_3x1m_B3", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1280.0, 2885.0, 980.9614), (0.0, -179.99998633961752, -0.0), (1.5, 1.5, 1.5625), "Suburbs_Wall_Thick_3x1m_B4", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3475.6187, 5016.052, 808.2163), (0.0, 89.99988960903808, -0.0), (1.5, 1.5, 1.9375), "Suburbs_Wall_Thick_3x1m_B5", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2875.6182, 5016.0527, 808.2163), (0.0, 89.99988960903808, -0.0), (1.5, 1.5, 1.9375), "Suburbs_Wall_Thick_3x1m_B6", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2873.8613, 1421.916, 799.2644), (0.0, -90.0001164887758, 0.0), (1.5, 1.5, 1.9375), "Suburbs_Wall_Thick_3x1m_B9", _folder)
if a: placed += 1
else: skipped += 1

# Batch 52: StaticMesh'Suburbs_Wall_Thick_3x3m_A' (6 instances)
_mesh_path = "/Game/Art/Assets/Kits/Architecture/Suburbs/Suburbs_Wall_Thick_3x3m_A"
_materials = ['/Game/Art/Assets/Kits/Architecture/Suburbs/Destructable/Materials/MI_Suburbs_Wall_Non_Dest']
_folder = "Reconstruction/BD_BB_Chapter5_BrokenSeal/Meshes"
a = spawn_static_mesh(_mesh_path, _materials, (1240.2561, 2166.1528, 671.9882), (0.0, -65.00014701274256, 0.0), (1.0, 1.0, 1.0), "NonDest_Boundry_3m_Trim_A50", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2093.3435, 1224.4471, 670.5278), (0.0, -20.000029202010403, 0.0), (1.125, 1.0, 1.0), "NonDest_Boundry_3m_Trim_A51", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2873.8613, 1201.915, 799.2644), (0.0, -90.0001164887758, 0.0), (1.59375, 1.1612903, 1.9375), "Suburbs_Wall_Thick_3x1m_B11", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3210.0, 805.0, 1300.0), (0.0, 0.0, 90.00001925454748), (2.0000002, 1.0, 2.0), "Suburbs_Wall_Thick_3x3m_A_149", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3210.0, 210.0, 1300.0), (0.0, 0.0, 90.00001925454748), (2.0, 1.0, 2.0), "Suburbs_Wall_Thick_3x3m_A2", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3474.0664, 5269.299, 1343.8004), (5.729558642325519e-07, -90.0000000000132, -90.0000504203007), (2.0, 1.0, 2.0), "Suburbs_Wall_Thick_3x3m_A3_173", _folder)
if a: placed += 1
else: skipped += 1

# Batch 53: StaticMesh'Suburbs_Wall_Thick_Arch' (3 instances)
_mesh_path = "/Game/Art/Assets/Kits/Architecture/Suburbs/Suburbs_Wall_Thick_Arch"
_materials = ['/Game/Art/Assets/Kits/Architecture/Suburbs/Destructable/Materials/MI_Suburbs_Wall_Non_Dest']
_folder = "Reconstruction/BD_BB_Chapter5_BrokenSeal/Meshes"
a = spawn_static_mesh(_mesh_path, _materials, (1430.0, 3185.8652, 980.9614), (0.0, 89.99992202041271, -0.0), (1.5, 1.5, 1.5625), "Suburbs_Wall_Thick_Arch_21", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3175.6182, 5016.0522, 808.2163), (0.0, -3.051757709276941e-05, 0.0), (1.5, 1.5, 1.9375), "Suburbs_Wall_Thick_Arch2", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3173.8625, 1421.916, 799.2644), (0.0, 179.9999795094293, -0.0), (1.5, 1.5, 1.9375), "Suburbs_Wall_Thick_Arch3", _folder)
if a: placed += 1
else: skipped += 1

# Batch 54: StaticMesh'Suburbs_Wall_Thin_1x3m_A' (17 instances)
_mesh_path = "/Game/Art/Assets/Kits/Architecture/Suburbs/Suburbs_Wall_Thin_1x3m_A"
_materials = ['/Game/Art/Assets/Kits/Architecture/Suburbs/Destructable/Materials/MI_Suburbs_Wall_Non_Dest']
_folder = "Reconstruction/BD_BB_Chapter5_BrokenSeal/Meshes"
a = spawn_static_mesh(_mesh_path, _materials, (1858.8615, 516.0718, 1195.0), (0.0, 154.35291837231205, -0.0), (1.0, 1.0, 1.0), "Suburbs_Wall_Thin_1x3m_A_63", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2434.5403, 6041.3535, 1304.2734), (0.0, 18.55782433635334, -0.0), (1.0, 1.0, 1.0), "Suburbs_Wall_Thin_1x3m_A10", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2150.137, 5945.8853, 1304.2734), (0.0, 18.559380073660837, -0.0), (1.0, 1.0, 1.0), "Suburbs_Wall_Thin_1x3m_A11", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1865.7256, 5850.424, 1304.2734), (0.0, 18.55912887211676, -0.0), (1.0, 1.0, 1.0), "Suburbs_Wall_Thin_1x3m_A12", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (516.3013, 4526.344, 1304.2734), (0.0, 73.21042298078633, -0.0), (1.0, 1.0, 1.0), "Suburbs_Wall_Thin_1x3m_A13", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (429.63232, 4239.1357, 1304.2734), (0.0, 73.21286400849166, -0.0), (1.0, 1.0, 1.0), "Suburbs_Wall_Thin_1x3m_A14", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (342.95166, 3951.9275, 1304.2734), (0.0, 73.2126083023384, -0.0), (1.0, 1.0, 1.0), "Suburbs_Wall_Thin_1x3m_A15", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (319.02344, 2436.417, 1304.2734), (0.0, 109.37916659535561, -0.0), (1.0, 1.0, 1.0), "Suburbs_Wall_Thin_1x3m_A16", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (418.5625, 2153.4106, 1304.2734), (0.0, 109.38152271357416, -0.0), (1.0, 1.0, 1.0), "Suburbs_Wall_Thin_1x3m_A17", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (518.08984, 1870.397, 1304.2734), (0.0, 109.38152271357416, -0.0), (1.0, 1.0, 1.0), "Suburbs_Wall_Thin_1x3m_A18", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2129.2925, 386.20215, 1195.0), (0.0, 154.35291837231205, -0.0), (1.0, 1.0, 1.0), "Suburbs_Wall_Thin_1x3m_A2", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2399.7266, 256.32617, 1195.0), (0.0, 154.35291837231205, -0.0), (1.0, 1.0, 1.0), "Suburbs_Wall_Thin_1x3m_A3", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5061.9663, 903.6458, 1204.2734), (0.0, -143.66741222861563, 0.0), (1.0, 1.0, 1.0), "Suburbs_Wall_Thin_1x3m_A5", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5303.654, 1081.3757, 1204.2734), (0.0, -143.66567568868004, 0.0), (1.0, 1.0, 1.0), "Suburbs_Wall_Thin_1x3m_A6", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5450.83, 5155.2783, 1304.2734), (0.0, -44.07211359736894, 0.0), (1.0, 1.0, 1.0), "Suburbs_Wall_Thin_1x3m_A7", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5235.2983, 5363.952, 1304.2734), (0.0, -44.07183511641015, 0.0), (1.0, 1.0, 1.0), "Suburbs_Wall_Thin_1x3m_A8", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5019.767, 5572.635, 1304.2734), (0.0, -44.070464315267465, 0.0), (1.0, 1.0, 1.0), "Suburbs_Wall_Thin_1x3m_A9", _folder)
if a: placed += 1
else: skipped += 1

# Batch 55: StaticMesh'Suburbs_Wall_Thin_3x3m_A' (203 instances)
_mesh_path = "/Game/Art/Assets/Kits/Architecture/Suburbs/Suburbs_Wall_Thin_3x3m_A"
_materials = ['/Game/Art/Assets/Kits/Architecture/Suburbs/Destructable/Materials/MI_Suburbs_Wall_Non_Dest']
_folder = "Reconstruction/BD_BB_Chapter5_BrokenSeal/Meshes"
a = spawn_static_mesh(_mesh_path, _materials, (6000.0, 4190.0, 1850.0), (0.0, -89.99993822608693, 0.0), (1.0, 1.0, 1.0), "Suburbs_Wall_Thin_3x3m_A100", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (6000.0, 4490.0, 1550.0), (0.0, -89.99993822608693, 0.0), (1.0, 1.0, 1.0), "Suburbs_Wall_Thin_3x3m_A101", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (6000.0, 4490.0, 1850.0), (0.0, -89.99993822608693, 0.0), (1.0, 1.0, 1.0), "Suburbs_Wall_Thin_3x3m_A102", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (6000.0, 2430.0005, 1250.0), (0.0, -89.99993822608693, 0.0), (1.0, 1.0, 1.0), "Suburbs_Wall_Thin_3x3m_A103", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (6000.0, 2130.0, 1250.0), (0.0, -89.99993822608693, 0.0), (1.0, 1.0, 1.0), "Suburbs_Wall_Thin_3x3m_A104", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (6000.0, 2430.0005, 1550.0), (0.0, -89.99993822608693, 0.0), (1.0, 1.0, 1.0), "Suburbs_Wall_Thin_3x3m_A105", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (6000.0, 2130.0, 1550.0), (0.0, -89.99993822608693, 0.0), (1.0, 1.0, 1.0), "Suburbs_Wall_Thin_3x3m_A106", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (6000.0, 2430.0005, 1850.0), (0.0, -89.99993822608693, 0.0), (1.0, 1.0, 1.0), "Suburbs_Wall_Thin_3x3m_A107", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (6000.0, 2130.0, 1850.0), (0.0, -89.99993822608693, 0.0), (1.0, 1.0, 1.0), "Suburbs_Wall_Thin_3x3m_A108", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (6000.0, 2430.0005, 950.0), (0.0, -89.99993822608693, 0.0), (1.0, 1.0, 1.0), "Suburbs_Wall_Thin_3x3m_A109", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (6000.0, 2130.0, 950.0), (0.0, -89.99993822608693, 0.0), (1.0, 1.0, 1.0), "Suburbs_Wall_Thin_3x3m_A110", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (6000.0, 2430.0005, 650.0), (0.0, -89.99993822608693, 0.0), (1.0, 1.0, 1.0), "Suburbs_Wall_Thin_3x3m_A111", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (6000.0, 2130.0, 650.0), (0.0, -89.99993822608693, 0.0), (1.0, 1.0, 1.0), "Suburbs_Wall_Thin_3x3m_A112", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5772.9814, 4829.2837, 1380.0), (0.0, -50.000000322548, 0.0), (1.0, 1.0, 1.0), "Suburbs_Wall_Thin_3x3m_A113_25", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5965.8174, 4599.4707, 1380.0), (0.0, -50.000000322548, 0.0), (1.0, 1.0, 1.0), "Suburbs_Wall_Thin_3x3m_A114", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5772.9814, 4829.2837, 1080.0), (0.0, -50.000000322548, 0.0), (1.0, 1.0, 1.0), "Suburbs_Wall_Thin_3x3m_A115", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5965.8174, 4599.4707, 1080.0), (0.0, -50.000000322548, 0.0), (1.0, 1.0, 1.0), "Suburbs_Wall_Thin_3x3m_A116", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5772.9814, 4829.2837, 780.0), (0.0, -50.000000322548, 0.0), (1.0, 1.0, 1.0), "Suburbs_Wall_Thin_3x3m_A117", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5965.8174, 4599.4707, 780.0), (0.0, -50.000000322548, 0.0), (1.0, 1.0, 1.0), "Suburbs_Wall_Thin_3x3m_A118", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5772.9814, 4829.2837, 1680.0), (0.0, -50.000000322548, 0.0), (1.0, 1.0, 1.0), "Suburbs_Wall_Thin_3x3m_A119", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5965.8174, 4599.4707, 1680.0), (0.0, -50.000000322548, 0.0), (1.0, 1.0, 1.0), "Suburbs_Wall_Thin_3x3m_A120", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1806.9127, 407.89648, 1620.0), (0.0, 154.35291837231205, -0.0), (1.0, 1.0, 1.0), "Suburbs_Wall_Thin_3x3m_A121_16", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2083.8394, 291.5464, 1620.0), (0.0, 154.35291837231205, -0.0), (1.0, 1.0, 1.0), "Suburbs_Wall_Thin_3x3m_A122", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2349.9392, 152.66064, 1620.0), (0.0, 154.35291837231205, -0.0), (1.0, 1.0, 1.0), "Suburbs_Wall_Thin_3x3m_A123", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1793.9254, 380.85547, 1320.0), (0.0, 154.35291837231205, -0.0), (1.0, 1.0, 1.0), "Suburbs_Wall_Thin_3x3m_A124", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2083.8394, 291.5464, 1320.0), (0.0, 154.35291837231205, -0.0), (1.0, 1.0, 1.0), "Suburbs_Wall_Thin_3x3m_A125", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2334.7878, 121.11035, 1320.0), (0.0, 154.35291837231205, -0.0), (1.0, 1.0, 1.0), "Suburbs_Wall_Thin_3x3m_A126", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1839.381, 475.5078, 1920.0), (0.0, 154.35291837231205, -0.0), (1.0, 1.0, 1.0), "Suburbs_Wall_Thin_3x3m_A127", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2380.245, 215.75977, 1920.0), (0.0, 154.35291837231205, -0.0), (1.0, 1.0, 1.0), "Suburbs_Wall_Thin_3x3m_A128", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2109.8135, 345.63574, 1920.0), (0.0, 154.35291837231205, -0.0), (1.0, 1.0, 1.0), "Suburbs_Wall_Thin_3x3m_A129", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1837.2164, 470.99805, 1320.0), (-1.354616829177425e-07, 154.35382442428715, 90.00001973276518), (1.0, 1.0, 1.0), "Suburbs_Wall_Thin_3x3m_A130", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2107.6504, 341.12842, 1320.0), (-1.354616829177425e-07, 154.35382442428715, 90.00001973276518), (1.0, 1.0, 1.0), "Suburbs_Wall_Thin_3x3m_A131", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2378.0815, 211.25244, 1320.0), (-1.354616829177425e-07, 154.35382442428715, 90.00001973276518), (1.0, 1.0, 1.0), "Suburbs_Wall_Thin_3x3m_A132", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1858.8615, 516.0718, 895.0), (0.0, 154.35291837231205, -0.0), (1.0, 1.0, 1.0), "Suburbs_Wall_Thin_3x3m_A133", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2129.2925, 386.20215, 895.0), (0.0, 154.35291837231205, -0.0), (1.0, 1.0, 1.0), "Suburbs_Wall_Thin_3x3m_A134", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2399.7266, 256.32617, 895.0), (0.0, 154.35291837231205, -0.0), (1.0, 1.0, 1.0), "Suburbs_Wall_Thin_3x3m_A135", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4891.3784, 629.2352, 1629.2736), (0.0, -143.66567568868004, 0.0), (1.0, 1.0, 1.0), "Suburbs_Wall_Thin_3x3m_A136", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5125.5327, 820.08453, 1629.2736), (0.0, -142.04311640445187, 0.0), (1.0, 1.0, 1.0), "Suburbs_Wall_Thin_3x3m_A137", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5387.894, 1000.5782, 1629.2736), (0.0, -143.66567568868004, 0.0), (1.0625, 1.0, 1.0), "Suburbs_Wall_Thin_3x3m_A138", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4909.1504, 605.06714, 1329.2734), (0.0, -143.66567568868004, 0.0), (1.0, 1.0, 1.0), "Suburbs_Wall_Thin_3x3m_A139", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5124.1772, 819.0576, 1329.2734), (0.0, -143.66741222861563, 0.0), (1.0, 1.0, 1.0), "Suburbs_Wall_Thin_3x3m_A140", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5392.523, 960.5295, 1329.2734), (0.0, -143.66567568868004, 0.0), (1.0, 1.0, 1.0), "Suburbs_Wall_Thin_3x3m_A141", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4846.9443, 689.66205, 1929.2736), (0.0, -143.6673342912633, 0.0), (1.0, 1.0, 1.0), "Suburbs_Wall_Thin_3x3m_A142", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5330.3145, 1045.1202, 1929.2736), (0.0, -143.66567568868004, 0.0), (1.0, 1.0, 1.0), "Suburbs_Wall_Thin_3x3m_A143", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5088.6284, 867.3931, 1929.2736), (0.0, -143.66741222861563, 0.0), (1.0, 1.0, 1.0), "Suburbs_Wall_Thin_3x3m_A144", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4855.156, 678.9366, 1329.2734), (-4.5806222572472185e-07, -142.04254600342625, 90.0000105554112), (1.0, 1.0, 1.0), "Suburbs_Wall_Thin_3x3m_A145", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5091.59, 863.3658, 1329.2734), (-1.479740626401542e-06, -143.66722278386283, 90.00001261889618), (1.0, 1.0, 1.0), "Suburbs_Wall_Thin_3x3m_A146", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5333.2773, 1041.0923, 1329.2734), (-1.3230248661513143e-06, -143.66505189064821, 89.99999170015325), (1.0, 1.0, 1.0), "Suburbs_Wall_Thin_3x3m_A147", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4824.4023, 718.3623, 1004.27344), (0.0, -142.04311640445187, 0.0), (1.0, 1.0, 1.0), "Suburbs_Wall_Thin_3x3m_A148", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5061.9663, 903.6458, 904.27344), (0.0, -143.66741222861563, 0.0), (1.0, 1.0, 1.0), "Suburbs_Wall_Thin_3x3m_A149", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5303.654, 1081.3757, 904.27344), (0.0, -143.66567568868004, 0.0), (1.0, 1.0, 1.0), "Suburbs_Wall_Thin_3x3m_A150", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5534.3027, 5241.4893, 1729.2736), (0.0, -44.070464315267465, 0.0), (1.0, 1.0, 1.0), "Suburbs_Wall_Thin_3x3m_A151", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5308.3335, 5439.3926, 1729.2736), (0.0, -44.07183511641015, 0.0), (1.0, 1.0, 1.0), "Suburbs_Wall_Thin_3x3m_A152", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5099.7646, 5655.2554, 1729.2736), (0.0, -44.070464315267465, 0.0), (1.0, 1.0, 1.0), "Suburbs_Wall_Thin_3x3m_A153", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5555.1694, 5263.042, 1429.2734), (0.0, -44.06982270099668, 0.0), (1.0, 1.0, 1.0), "Suburbs_Wall_Thin_3x3m_A154", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5308.3335, 5439.3926, 1429.2734), (0.0, -44.07183511641015, 0.0), (1.0, 1.0, 1.0), "Suburbs_Wall_Thin_3x3m_A155", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5124.1123, 5680.4033, 1429.2734), (0.0, -44.070464315267465, 0.0), (1.0, 1.0, 1.0), "Suburbs_Wall_Thin_3x3m_A156", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5482.129, 5187.6074, 2029.2736), (0.0, -44.07211359736894, 0.0), (1.0, 1.0, 1.0), "Suburbs_Wall_Thin_3x3m_A157", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5051.0684, 5604.967, 2029.2736), (0.0, -44.070464315267465, 0.0), (1.0, 1.0, 1.0), "Suburbs_Wall_Thin_3x3m_A158", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5266.5986, 5396.284, 2029.2736), (0.0, -44.07183511641015, 0.0), (1.0, 1.0, 1.0), "Suburbs_Wall_Thin_3x3m_A159", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5485.6094, 5191.201, 1429.2734), (3.218779700819484e-07, -44.07204369798413, 89.99999732825738), (1.0, 1.0, 1.0), "Suburbs_Wall_Thin_3x3m_A160", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5270.077, 5399.877, 1429.2734), (4.327933421692121e-06, -44.07189858965363, 89.99995276418926), (1.0, 1.0, 1.0), "Suburbs_Wall_Thin_3x3m_A161", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5054.5464, 5608.5596, 1429.2734), (-6.426783014461686e-07, -44.06972999172262, 89.99994574911737), (1.0, 1.0, 1.0), "Suburbs_Wall_Thin_3x3m_A162", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5450.83, 5155.2783, 1004.27344), (0.0, -44.07211359736894, 0.0), (1.0, 1.0, 1.0), "Suburbs_Wall_Thin_3x3m_A163", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5235.2983, 5363.952, 1004.27344), (0.0, -44.07183511641015, 0.0), (1.0, 1.0, 1.0), "Suburbs_Wall_Thin_3x3m_A164", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5019.767, 5572.635, 1004.27344), (0.0, -44.070464315267465, 0.0), (1.0, 1.0, 1.0), "Suburbs_Wall_Thin_3x3m_A165", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2453.2388, 6174.212, 1729.2736), (0.0, 18.559066378308874, -0.0), (1.0, 1.0, 1.0), "Suburbs_Wall_Thin_3x3m_A166", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2173.6006, 6064.5254, 1729.2736), (0.0, 18.559509156115947, -0.0), (1.0, 1.0, 1.0), "Suburbs_Wall_Thin_3x3m_A167", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1886.0137, 5978.548, 1729.2736), (0.0, 18.559066378308874, -0.0), (1.0, 1.0, 1.0), "Suburbs_Wall_Thin_3x3m_A168", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2443.6938, 6202.652, 1429.2734), (0.0, 18.55956993473789, -0.0), (1.0, 1.0, 1.0), "Suburbs_Wall_Thin_3x3m_A169", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2173.6006, 6064.5254, 1429.2734), (0.0, 18.559509156115947, -0.0), (1.0, 1.0, 1.0), "Suburbs_Wall_Thin_3x3m_A170", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1874.876, 6011.7314, 1429.2734), (0.0, 18.559066378308874, -0.0), (1.0, 1.0, 1.0), "Suburbs_Wall_Thin_3x3m_A171", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2477.1023, 6103.1064, 2029.2736), (0.0, 18.55782433635334, -0.0), (1.0, 1.0, 1.0), "Suburbs_Wall_Thin_3x3m_A172", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1908.2842, 5912.1836, 2029.2736), (0.0, 18.55912887211676, -0.0), (1.0, 1.0, 1.0), "Suburbs_Wall_Thin_3x3m_A173", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2192.697, 6007.6436, 2029.2736), (0.0, 18.559509156115947, -0.0), (1.0, 1.0, 1.0), "Suburbs_Wall_Thin_3x3m_A174", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2475.51, 6107.8496, 1429.2734), (7.039364695436084e-06, 18.557822728214788, 89.99994545774612), (1.0, 1.0, 1.0), "Suburbs_Wall_Thin_3x3m_A175", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2191.1052, 6012.385, 1429.2734), (7.039970012241951e-06, 18.55926431853026, 89.99994458121263), (1.0, 1.0, 1.0), "Suburbs_Wall_Thin_3x3m_A176", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1906.6929, 5916.924, 1429.2734), (-1.9193285430089988e-07, 18.559792879539298, 89.9999633424188), (1.0, 1.0, 1.0), "Suburbs_Wall_Thin_3x3m_A177", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2434.5403, 6041.3535, 1004.27344), (0.0, 18.55782433635334, -0.0), (1.0, 1.0, 1.0), "Suburbs_Wall_Thin_3x3m_A178", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2150.137, 5945.8853, 1004.27344), (0.0, 18.559380073660837, -0.0), (1.0, 1.0, 1.0), "Suburbs_Wall_Thin_3x3m_A179", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1865.7256, 5850.424, 1004.27344), (0.0, 18.55912887211676, -0.0), (1.0, 1.0, 1.0), "Suburbs_Wall_Thin_3x3m_A180", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (401.4204, 4561.0146, 1729.2736), (0.0, 73.21286400849166, -0.0), (1.0, 1.0, 1.0), "Suburbs_Wall_Thin_3x3m_A181", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (329.104, 4269.4688, 1729.2736), (0.0, 73.21258744924131, -0.0), (1.0, 1.0, 1.0), "Suburbs_Wall_Thin_3x3m_A182", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (232.85107, 3985.157, 1729.2736), (0.0, 73.21286400849166, -0.0), (1.0, 1.0, 1.0), "Suburbs_Wall_Thin_3x3m_A183", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4526.6865, 1424.6223, 929.27344), (0.0, -142.58209968414653, 0.0), (1.0, 1.0, 1.0), "Suburbs_Wall_Thin_3x3m_A184", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (329.104, 4269.4688, 1429.2734), (0.0, 73.21258744924131, -0.0), (1.0, 1.0, 1.0), "Suburbs_Wall_Thin_3x3m_A185", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (199.34277, 3995.27, 1429.2734), (0.0, 73.21286400849166, -0.0), (1.0, 1.0, 1.0), "Suburbs_Wall_Thin_3x3m_A186", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (473.2246, 4539.341, 2029.2736), (0.0, 73.21066748100033, -0.0), (1.0, 1.0, 1.0), "Suburbs_Wall_Thin_3x3m_A187", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (299.8628, 3964.9265, 2029.2736), (0.0, 73.2126083023384, -0.0), (1.0, 1.0, 1.0), "Suburbs_Wall_Thin_3x3m_A188", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (386.5503, 4252.136, 2029.2736), (0.0, 73.21258744924131, -0.0), (1.0, 1.0, 1.0), "Suburbs_Wall_Thin_3x3m_A189", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (468.43652, 4540.786, 1429.2734), (1.4858112302609737e-06, 73.21047494077618, 89.99996374885812), (1.0, 1.0, 1.0), "Suburbs_Wall_Thin_3x3m_A190", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (381.75928, 4253.581, 1429.2734), (3.048110716778935e-06, 73.21300437516518, 90.00002112136418), (1.0, 1.0, 1.0), "Suburbs_Wall_Thin_3x3m_A191", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (295.07764, 3966.3704, 1429.2734), (1.2043772978307175e-05, 73.21303122128693, 90.00011237008951), (1.0, 1.0, 1.0), "Suburbs_Wall_Thin_3x3m_A192", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (516.3013, 4526.344, 1004.27344), (0.0, 73.21042298078633, -0.0), (1.0, 1.0, 1.0), "Suburbs_Wall_Thin_3x3m_A193", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (429.63232, 4239.1357, 1004.27344), (0.0, 73.21286400849166, -0.0), (1.0, 1.0, 1.0), "Suburbs_Wall_Thin_3x3m_A194", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (342.95166, 3951.9275, 1004.27344), (0.0, 73.2126083023384, -0.0), (1.0, 1.0, 1.0), "Suburbs_Wall_Thin_3x3m_A195", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (205.82178, 2396.6042, 1729.2736), (0.0, 109.38152271357416, -0.0), (1.0, 1.0, 1.0), "Suburbs_Wall_Thin_3x3m_A196", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (319.50732, 2118.5664, 1729.2736), (0.0, 109.38091821743961, -0.0), (1.0, 1.0, 1.0), "Suburbs_Wall_Thin_3x3m_A197", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (409.59717, 1832.2466, 1729.2736), (0.0, 109.38152271357416, -0.0), (1.0, 1.0, 1.0), "Suburbs_Wall_Thin_3x3m_A198", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (177.52295, 2386.6553, 1429.2734), (0.0, 109.38152271357416, -0.0), (1.0, 1.0, 1.0), "Suburbs_Wall_Thin_3x3m_A199", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (319.50732, 2118.5664, 1429.2734), (0.0, 109.38091821743961, -0.0), (1.0, 1.0, 1.0), "Suburbs_Wall_Thin_3x3m_A200", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (376.5786, 1820.6328, 1429.2734), (0.0, 109.38152271357416, -0.0), (1.0, 1.0, 1.0), "Suburbs_Wall_Thin_3x3m_A201", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (276.57715, 2421.4849, 2029.2736), (0.0, 109.37942940593994, -0.0), (1.0, 1.0, 1.0), "Suburbs_Wall_Thin_3x3m_A202", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (475.63623, 1855.4634, 2029.2736), (0.0, 109.38152271357416, -0.0), (1.0, 1.0, 1.0), "Suburbs_Wall_Thin_3x3m_A203", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (376.11133, 2138.479, 2029.2736), (0.0, 109.38091821743961, -0.0), (1.0, 1.0, 1.0), "Suburbs_Wall_Thin_3x3m_A204", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (271.86035, 2419.8267, 1429.2734), (2.727937663950657e-06, 109.37864773053319, 89.99995216040509), (1.0, 1.0, 1.0), "Suburbs_Wall_Thin_3x3m_A205", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (371.38916, 2136.817, 1429.2734), (3.785428818048055e-05, 109.38165249374538, 90.0000006080546), (1.0, 1.0, 1.0), "Suburbs_Wall_Thin_3x3m_A206", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (470.91846, 1853.8052, 1429.2734), (3.75208006164919e-05, 109.38153179280897, 90.00009052844153), (1.0, 1.0, 1.0), "Suburbs_Wall_Thin_3x3m_A207", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (319.02344, 2436.417, 1004.27344), (0.0, 109.37916659535561, -0.0), (1.0, 1.0, 1.0), "Suburbs_Wall_Thin_3x3m_A208", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (418.5625, 2153.4106, 1004.27344), (0.0, 109.38152271357416, -0.0), (1.0, 1.0, 1.0), "Suburbs_Wall_Thin_3x3m_A209", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (518.08984, 1870.397, 1004.27344), (0.0, 109.38152271357416, -0.0), (1.0, 1.0, 1.0), "Suburbs_Wall_Thin_3x3m_A210", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (97.778015, 3490.6824, 1729.2736), (0.0, 85.98682508044324, -0.0), (1.0, 1.0, 1.0), "Suburbs_Wall_Thin_3x3m_A211_568", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (91.72169, 3190.3628, 1729.2736), (0.0, 85.98670434887875, -0.0), (1.0, 1.0, 1.0), "Suburbs_Wall_Thin_3x3m_A212_569", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (60.721767, 2891.8057, 1729.2736), (0.0, 85.98682508044324, -0.0), (1.0, 1.0, 1.0), "Suburbs_Wall_Thin_3x3m_A213_570", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (91.72169, 3190.3628, 1429.2734), (0.0, 85.98670434887875, -0.0), (1.0, 1.0, 1.0), "Suburbs_Wall_Thin_3x3m_A214_571", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (60.721767, 2891.8057, 1429.2736), (0.0, 85.98682508044324, -0.0), (1.0, 1.0, 1.0), "Suburbs_Wall_Thin_3x3m_A215_577", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (172.59734, 3485.4214, 2029.2736), (0.0, 85.98471480055572, -0.0), (1.0, 1.0, 1.0), "Suburbs_Wall_Thin_3x3m_A216_573", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (130.54774, 2886.8933, 2029.2736), (0.0, 85.98647889862636, -0.0), (1.0, 1.0, 1.0), "Suburbs_Wall_Thin_3x3m_A217_574", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (151.57852, 3186.1611, 2029.2736), (0.0, 85.98729937279174, -0.0), (1.0, 1.0, 1.0), "Suburbs_Wall_Thin_3x3m_A218_575", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (176.93262, 3456.6956, 1429.2734), (1.7890262461664188e-05, 86.29715309936373, 90.00011759724558), (1.0, 1.0, 1.0), "Suburbs_Wall_Thin_3x3m_A219_580", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2884.2668, 20.550102, 1620.0045), (-0.0001525878756786659, 179.35297262703813, -0.00015258787173613), (1.0, 1.0, 1.0), "Suburbs_Wall_Thin_3x3m_A220_392", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3184.4194, 32.13533, 1620.0055), (-0.0001525878756786659, 179.35297262703813, -0.00015258787173613), (1.0, 1.0, 1.0), "Suburbs_Wall_Thin_3x3m_A221_393", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3484.2834, 18.720901, 1620.0062), (-0.0001525878756786659, 179.35297262703813, -0.00015258787173613), (1.0, 1.0, 1.0), "Suburbs_Wall_Thin_3x3m_A222_394", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2884.2673, 20.549295, 1320.0045), (-0.0001525878756786659, 179.35297262703813, -0.00015258787173613), (1.0, 1.0, 1.0), "Suburbs_Wall_Thin_3x3m_A223_407", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3184.4202, 32.13462, 1320.0055), (-0.0001525878756786659, 179.35297262703813, -0.00015258787173613), (1.0, 1.0, 1.0), "Suburbs_Wall_Thin_3x3m_A224_396", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2885.119, 95.54924, 1920.0044), (-0.0001525878756786659, 179.35297262703813, -0.00015258787173613), (1.0, 1.0, 1.0), "Suburbs_Wall_Thin_3x3m_A225_397", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3485.082, 88.71653, 1920.0061), (-0.0001525878756786659, 179.35297262703813, -0.00015258787173613), (1.0, 1.0, 1.0), "Suburbs_Wall_Thin_3x3m_A226_398", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3185.1, 92.13476, 1920.0051), (-0.0001525878756786659, 179.35297262703813, -0.00015258787173613), (1.0, 1.0, 1.0), "Suburbs_Wall_Thin_3x3m_A227_399", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3484.284, 18.72011, 1325.0062), (-0.0001525878756786659, 179.35297262703813, -0.00015258787173613), (1.0, 1.0, 1.0), "Suburbs_Wall_Thin_3x3m_A228_404", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3879.2842, 123.13879, 1620.0068), (-6.103514839686022e-05, -159.99698654145146, -0.00015258787421847903), (1.0, 1.0, 1.0), "Suburbs_Wall_Thin_3x3m_A229_424", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4156.0576, 239.84552, 1620.0077), (-6.103514046406084e-05, -159.99224601682084, -0.00015258785893126686), (1.0, 1.0, 1.0), "Suburbs_Wall_Thin_3x3m_A230_425", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4441.3857, 333.05902, 1620.008), (-6.103514839686022e-05, -159.99698654145146, -0.00015258787421847903), (1.0, 1.0, 1.0), "Suburbs_Wall_Thin_3x3m_A231_426", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4156.0576, 239.84497, 1320.0073), (-6.103514997692173e-05, -159.9928890265726, -0.00015258787956216175), (1.0, 1.0, 1.0), "Suburbs_Wall_Thin_3x3m_A232_427", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3872.4126, 200.4604, 1920.0067), (-6.103514839686022e-05, -159.99698654145146, -0.00015258787421847903), (1.0, 1.0, 1.0), "Suburbs_Wall_Thin_3x3m_A233_428", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4436.2427, 405.67938, 1920.0072), (-6.103514839686022e-05, -159.99698654145146, -0.00015258787421847903), (1.0, 1.0, 1.0), "Suburbs_Wall_Thin_3x3m_A234_429", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4154.328, 303.07172, 1920.0074), (-6.103515409332075e-05, -159.991392173024, -0.00015258788259995266), (1.0, 1.0, 1.0), "Suburbs_Wall_Thin_3x3m_A235_430", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4441.3857, 333.05804, 1325.008), (-6.103514839686022e-05, -159.99698654145146, -0.00015258787421847903), (1.0, 1.0, 1.0), "Suburbs_Wall_Thin_3x3m_A236_433", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3879.2842, 123.13796, 1320.0068), (-6.103514839686022e-05, -159.99698654145146, -0.00015258787421847903), (1.0, 1.0, 1.0), "Suburbs_Wall_Thin_3x3m_A237_434", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (516.3013, 4526.344, 704.27344), (0.0, 73.21042298078633, -0.0), (1.0, 1.0, 1.0), "Suburbs_Wall_Thin_3x3m_A238", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1259.9419, 2151.4028, 649.27344), (0.0, 104.38149983578057, -0.0), (1.0, 1.0, 1.0), "Suburbs_Wall_Thin_3x3m_A239", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4782.8267, 1604.7693, 658.69385), (0.0, -145.61994491424824, 0.0), (1.0, 1.0, 1.0), "Suburbs_Wall_Thin_3x3m_A24", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (401.38974, 4561.016, 1429.2734), (0.0, 73.21258744924131, -0.0), (1.0, 1.0, 1.0), "Suburbs_Wall_Thin_3x3m_A240", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4759.8115, 1621.8607, 789.27344), (0.0, -139.6393419794498, 0.0), (1.0, 1.0, 1.0), "Suburbs_Wall_Thin_3x3m_A241", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5450.83, 5155.2783, 709.27344), (0.0, -44.07211359736894, 0.0), (1.0, 1.0, 1.0), "Suburbs_Wall_Thin_3x3m_A242", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (927.3555, 3707.7122, 929.27344), (0.0, 73.21042298078633, -0.0), (1.0, 1.0, 1.0), "Suburbs_Wall_Thin_3x3m_A243", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1010.0487, 2626.5054, 909.27344), (0.0, 109.38152271357416, -0.0), (1.0, 1.0, 1.0), "Suburbs_Wall_Thin_3x3m_A244", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (518.08984, 1870.397, 704.27344), (0.0, 109.38152271357416, -0.0), (1.0, 1.0, 1.0), "Suburbs_Wall_Thin_3x3m_A245", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1230.0413, 4287.9897, 674.27344), (0.0, 65.539739098078, -0.0), (1.0, 1.0, 1.0), "Suburbs_Wall_Thin_3x3m_A246", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (97.74778, 3490.6775, 1429.2734), (0.0, 85.98664183010519, -0.0), (1.0, 1.0, 1.0), "Suburbs_Wall_Thin_3x3m_A247", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (157.56009, 3157.322, 1429.2734), (1.434316646389313e-05, 86.29722646671156, 90.00011537595664), (1.0, 1.0, 1.0), "Suburbs_Wall_Thin_3x3m_A248", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (138.18839, 2857.948, 1429.2734), (1.434316646389313e-05, 86.29722646671156, 90.00011537595664), (1.0, 1.0, 1.0), "Suburbs_Wall_Thin_3x3m_A249", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4618.286, 5920.716, 1729.2736), (0.0, -18.648377334402984, 0.0), (1.0, 1.0, 1.0), "Suburbs_Wall_Thin_3x3m_A250", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4329.239, 6002.4487, 1729.2736), (0.0, -18.649750661400187, 0.0), (1.0, 1.0, 1.0), "Suburbs_Wall_Thin_3x3m_A251", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4029.2495, 6114.265, 1729.2736), (0.0, -18.648377334402984, 0.0), (1.0901121, 1.0, 1.0), "Suburbs_Wall_Thin_3x3m_A252", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4618.286, 5920.716, 1429.2736), (0.0, -18.648377334402984, 0.0), (1.0, 1.0, 1.0), "Suburbs_Wall_Thin_3x3m_A253_73", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4329.239, 6002.4487, 1429.2734), (0.0, -18.649750661400187, 0.0), (1.0, 1.0, 1.0), "Suburbs_Wall_Thin_3x3m_A254", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4029.2495, 6114.265, 1429.2736), (0.0, -18.648377334402984, 0.0), (1.0901121, 1.0, 1.0), "Suburbs_Wall_Thin_3x3m_A255_74", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4651.4346, 5830.3696, 2029.2736), (0.0, -18.65002481003585, 0.0), (1.1005107, 1.0, 1.0), "Suburbs_Wall_Thin_3x3m_A256", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4025.8066, 6041.547, 2029.2736), (0.0, -18.648377334402984, 0.0), (1.1005107, 1.0, 1.0), "Suburbs_Wall_Thin_3x3m_A257", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4338.6216, 5935.9546, 2029.2736), (0.0, -18.649750661400187, 0.0), (1.1005107, 1.0, 1.0), "Suburbs_Wall_Thin_3x3m_A258", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4328.296, 6002.7715, 1124.2734), (0.0, -18.649750661400187, 0.0), (1.0, 1.0, 1.0), "Suburbs_Wall_Thin_3x3m_A259", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3567.9353, 6261.494, 1729.2733), (-6.103516154882312e-05, -2.368469355379805, -6.103515889632294e-05), (1.0, 1.0, 1.0), "Suburbs_Wall_Thin_3x3m_A260", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3267.5657, 6258.921, 1729.2734), (-6.103514859376623e-05, -2.369842561301466, -6.103515698826668e-05), (1.0, 1.0, 1.0), "Suburbs_Wall_Thin_3x3m_A261", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2948.2593, 6282.1577, 1729.2738), (-6.103516154882312e-05, -2.368469355379805, -6.103515889632294e-05), (1.090112, 1.0, 1.0), "Suburbs_Wall_Thin_3x3m_A262", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3267.5657, 6258.9214, 1389.2736), (-6.103514859376623e-05, -2.369842561301466, -6.103515698826668e-05), (1.0, 1.0, 1.1403384), "Suburbs_Wall_Thin_3x3m_A263", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3625.0815, 6184.063, 2029.2731), (-6.103515870247014e-05, -2.3701172987595225, -6.103515880534695e-05), (1.100511, 1.0, 1.0), "Suburbs_Wall_Thin_3x3m_A264", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2965.3403, 6211.3896, 2029.2738), (-6.103516154882312e-05, -2.368469355379805, -6.103515889632294e-05), (1.100511, 1.0, 1.0), "Suburbs_Wall_Thin_3x3m_A265", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3295.213, 6197.723, 2029.2734), (-6.103514859376623e-05, -2.369842561301466, -6.103515698826668e-05), (1.100511, 1.0, 1.0), "Suburbs_Wall_Thin_3x3m_A266", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3567.9348, 6261.494, 1389.2731), (-6.103516154882312e-05, -2.368469355379805, -6.103515889632294e-05), (1.0, 1.0, 1.1403384), "Suburbs_Wall_Thin_3x3m_A267", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2948.2593, 6282.1577, 1389.2738), (-6.103516154882312e-05, -2.368469355379805, -6.103515889632294e-05), (1.090112, 1.0, 1.1394044), "Suburbs_Wall_Thin_3x3m_A268", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2515.8354, 5347.8247, 846.5657), (0.0, 20.04783660039813, -0.0), (1.0, 1.0, 1.0), "Suburbs_Wall_Thin_3x3m_A30", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2088.4053, 5191.848, 711.5657), (0.0, 20.04783660039813, -0.0), (1.0, 1.0, 1.0), "Suburbs_Wall_Thin_3x3m_A31", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4615.0835, 5902.118, 2319.8687), (0.0, 163.21051677767082, -0.0), (1.0, 1.0, 1.0), "Suburbs_Wall_Thin_3x3m_A54", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4327.872, 5988.7764, 2319.8687), (3.2986230832603047e-09, 163.2105148654048, 0.1999759781704137), (1.0, 1.0, 1.0), "Suburbs_Wall_Thin_3x3m_A55", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4040.661, 6075.435, 2319.8687), (0.0, 163.21051677767082, -0.0), (1.0, 1.0, 1.0), "Suburbs_Wall_Thin_3x3m_A56", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2241.378, 1413.7163, 681.54395), (0.0, 17.622283416412454, -0.0), (0.90625, 1.0, 1.0), "Suburbs_Wall_Thin_3x3m_A64", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4533.9326, 5064.949, 927.0106), (0.0, 134.73616556417446, -0.0), (1.0, 1.0, 1.0), "Suburbs_Wall_Thin_3x3m_A65", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2766.4448, 1452.1265, 681.54395), (0.0, 0.03421020641062308, -0.0), (0.90625, 1.0, 1.0), "Suburbs_Wall_Thin_3x3m_A66", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2494.5664, 1451.9663, 681.54395), (0.0, 0.03421020641062308, -0.0), (0.90625, 1.0, 1.0), "Suburbs_Wall_Thin_3x3m_A67", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3959.3906, 1442.2656, 681.54395), (0.0, 1.4807739558072504, -0.0), (0.9770027, 1.0, 1.0), "Suburbs_Wall_Thin_3x3m_A68_216", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3666.383, 1434.7139, 681.54395), (0.0, 1.4807739558072504, -0.0), (0.9770027, 1.0, 1.0), "Suburbs_Wall_Thin_3x3m_A69_217", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2247.8496, 1389.5366, 681.54395), (0.0, 12.347411537187114, -0.0), (0.90625, 1.0, 1.0), "Suburbs_Wall_Thin_3x3m_A70_234", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4769.72, 4826.9805, 697.0106), (0.0, 134.73616556417446, -0.0), (1.0, 1.0, 1.0), "Suburbs_Wall_Thin_3x3m_A71", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4488.2344, 1338.1086, 681.54395), (0.0, -15.688080279660195, 0.0), (0.90625, 1.0, 1.0), "Suburbs_Wall_Thin_3x3m_A72", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4226.484, 1411.6272, 681.54395), (0.0, -15.688080279660195, 0.0), (0.90625, 1.0, 1.0), "Suburbs_Wall_Thin_3x3m_A73", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2427.9648, 4931.771, 681.54395), (0.0, 179.65482897575976, -0.0), (0.9000228, 1.0, 1.0), "Suburbs_Wall_Thin_3x3m_A74", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2694.4712, 4930.125, 681.54395), (0.0, 179.65323757570985, -0.0), (0.9000228, 1.0, 1.0), "Suburbs_Wall_Thin_3x3m_A75", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2132.521, 5008.8584, 681.54395), (0.0, 154.8679213216121, -0.0), (1.26104, 1.0, 1.0), "Suburbs_Wall_Thin_3x3m_A77", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (900.88525, 3393.1504, 1141.544), (0.0, -89.65420210532449, 0.0), (0.90625, 1.0, 1.0), "Suburbs_Wall_Thin_3x3m_A79", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (902.5166, 3123.1555, 1141.544), (0.0, -89.65420210532449, 0.0), (0.90625, 1.0, 1.0), "Suburbs_Wall_Thin_3x3m_A80", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (900.88525, 3393.1504, 841.54395), (0.0, -89.65420210532449, 0.0), (0.90625, 1.0, 1.0), "Suburbs_Wall_Thin_3x3m_A81", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (902.5166, 3123.1555, 841.54395), (0.0, -89.65420210532449, 0.0), (0.90625, 1.0, 1.0), "Suburbs_Wall_Thin_3x3m_A82", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1172.903, 3059.7876, 1426.544), (4.372073614380792e-06, -89.65417060250478, 89.9998766956464), (0.90625, 1.0, 1.0), "Suburbs_Wall_Thin_3x3m_A83", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1171.261, 3331.782, 1426.544), (1.0655559453862896e-05, -89.65417059905691, 89.99988244248303), (0.90625, 1.0, 1.0), "Suburbs_Wall_Thin_3x3m_A84", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (6000.0, 3890.0005, 1250.0), (0.0, -89.99993822608693, 0.0), (1.0, 1.0, 1.0), "Suburbs_Wall_Thin_3x3m_A85_2", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (6000.0, 4190.0, 1250.0), (0.0, -89.99993822608693, 0.0), (1.0, 1.0, 1.0), "Suburbs_Wall_Thin_3x3m_A86", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (872.9083, 3057.977, 1426.5432), (1.0655559453862896e-05, -89.65417059905691, 89.99988244248303), (0.90625, 1.0, 1.0), "Suburbs_Wall_Thin_3x3m_A87", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (871.26636, 3329.9714, 1426.5432), (1.0655559453862896e-05, -89.65417059905691, 89.99988244248303), (0.90625, 1.0, 1.0), "Suburbs_Wall_Thin_3x3m_A88", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (6000.0, 3890.0005, 950.0), (0.0, -89.99993822608693, 0.0), (1.0, 1.0, 1.0), "Suburbs_Wall_Thin_3x3m_A95", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (6000.0, 4190.0, 950.0), (0.0, -89.99993822608693, 0.0), (1.0, 1.0, 1.0), "Suburbs_Wall_Thin_3x3m_A96", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (6000.0, 3890.0005, 1550.0), (0.0, -89.99993822608693, 0.0), (1.0, 1.0, 1.0), "Suburbs_Wall_Thin_3x3m_A97", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (6000.0, 4190.0, 1550.0), (0.0, -89.99993822608693, 0.0), (1.0, 1.0, 1.0), "Suburbs_Wall_Thin_3x3m_A98", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (6000.0, 3890.0005, 1850.0), (0.0, -89.99993822608693, 0.0), (1.0, 1.0, 1.0), "Suburbs_Wall_Thin_3x3m_A99", _folder)
if a: placed += 1
else: skipped += 1

# Batch 56: StaticMesh'Suburbs_Wall_Thin_Arch_E' (18 instances)
_mesh_path = "/Game/Art/Assets/Kits/Architecture/Suburbs/Suburbs_Wall_Thin_Arch_E"
_materials = ['/Game/Art/Assets/Kits/Architecture/Suburbs/Materials/Suburbs_Trim_Sheet_A/MI_Suburbs_Trim_Sheet_A']
_folder = "Reconstruction/BD_BB_Chapter5_BrokenSeal/Meshes"
a = spawn_static_mesh(_mesh_path, _materials, (1815.5704, 425.93115, 1320.0), (0.0, 154.3529317952912, -0.0), (1.0, 1.0, 1.0), "Suburbs_Wall_Thin_Arch_B_24", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2459.6025, 6155.2485, 1429.2734), (0.0, 18.55783028498341, -0.0), (1.0, 1.0, 1.0), "Suburbs_Wall_Thin_Arch_B10", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1890.7881, 5964.3267, 1429.2734), (0.0, 18.55913174062638, -0.0), (1.0, 1.0, 1.0), "Suburbs_Wall_Thin_Arch_B11", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2179.9675, 6045.5674, 1729.2736), (0.0, 18.559387175577125, -0.0), (1.0, 1.0, 1.0), "Suburbs_Wall_Thin_Arch_B12", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (420.57227, 4555.2334, 1429.2734), (0.0, 73.21063049753907, -0.0), (1.0, 1.0, 1.0), "Suburbs_Wall_Thin_Arch_B13", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (247.21338, 3980.8232, 1429.2734), (0.0, 73.21258744924131, -0.0), (1.0, 1.0, 1.0), "Suburbs_Wall_Thin_Arch_B14", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (355.9267, 4271.8237, 1729.2736), (0.0, 73.21285024114876, -0.0), (1.0, 1.0, 1.0), "Suburbs_Wall_Thin_Arch_B15", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (224.69531, 2403.2402, 1429.2734), (0.0, 109.37942012517512, -0.0), (1.0, 1.0, 1.0), "Suburbs_Wall_Thin_Arch_B16", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (423.74902, 1837.2222, 1429.2734), (0.0, 109.38152271357416, -0.0), (1.0, 1.0, 1.0), "Suburbs_Wall_Thin_Arch_B17", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (336.45108, 2145.7332, 1729.2736), (0.0, 109.38152271357416, -0.0), (1.0, 1.0, 1.0), "Suburbs_Wall_Thin_Arch_B18", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2356.4326, 166.18115, 1320.0), (0.0, 154.3529317952912, -0.0), (1.0, 1.0, 1.0), "Suburbs_Wall_Thin_Arch_B2", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2085.648, 318.41095, 1625.0), (0.0, 154.3529317952912, -0.0), (1.0, 1.0, 1.0), "Suburbs_Wall_Thin_Arch_B3", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4879.5264, 645.35077, 1329.2734), (0.0, -143.6673488261799, 0.0), (1.0, 1.0, 1.0), "Suburbs_Wall_Thin_Arch_B4", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5362.896, 1000.81287, 1329.2734), (0.0, -143.66567568868004, 0.0), (1.0, 1.0, 1.0), "Suburbs_Wall_Thin_Arch_B5", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5109.3643, 839.19403, 1629.2736), (0.0, -143.66741222861563, 0.0), (1.0, 1.0, 1.0), "Suburbs_Wall_Thin_Arch_B6", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5520.3877, 5227.12, 1429.2734), (0.0, -44.07208111054722, 0.0), (1.0, 1.0, 1.0), "Suburbs_Wall_Thin_Arch_B7", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5089.3306, 5644.4775, 1429.2734), (0.0, -44.070431577423406, 0.0), (1.0, 1.0, 1.0), "Suburbs_Wall_Thin_Arch_B8", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5294.4263, 5425.0225, 1729.2736), (0.0, -44.07180535214129, 0.0), (1.0, 1.0, 1.0), "Suburbs_Wall_Thin_Arch_B9", _folder)
if a: placed += 1
else: skipped += 1

# Batch 57: StaticMesh'Trim_A_3m' (3 instances)
_mesh_path = "/Game/Art/Assets/Kits/Architecture/Suburbs/Trim_A_3m"
_materials = ['/Game/Art/Assets/Kits/Architecture/Suburbs/Materials/Suburbs_Trim_A/MI_Trim_A_3m']
_folder = "Reconstruction/BD_BB_Chapter5_BrokenSeal/Meshes"
a = spawn_static_mesh(_mesh_path, _materials, (4174.5483, 5215.244, 935.5342), (0.0, 155.01637617779485, -0.0), (1.0, 1.0, 1.0), "Trim_A_3m10", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2216.933, 1184.9282, 940.0), (0.0, -19.978332759605095, 0.0), (1.0, 1.0, 1.0), "Trim_A_3m19", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4446.477, 5088.5366, 935.5342), (0.0, 155.01637617779485, -0.0), (1.0, 1.0, 1.0), "Trim_A_3m9", _folder)
if a: placed += 1
else: skipped += 1

# Batch 58: StaticMesh'Trim_A_3m_B' (3 instances)
_mesh_path = "/Game/Art/Assets/Kits/Architecture/Suburbs/Trim_A_3m_B"
_materials = ['/Game/Art/Assets/Kits/Architecture/Suburbs/Materials/Suburbs_Trim_A/MI_Trim_A_3m']
_folder = "Reconstruction/BD_BB_Chapter5_BrokenSeal/Meshes"
a = spawn_static_mesh(_mesh_path, _materials, (1354.9995, 3038.9187, 986.0376), (0.0, -3.051757709276941e-05, 0.0), (0.5, 1.5, 1.5), "Trim_A_3m_B3", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1504.9995, 3332.5735, 986.0376), (0.0, -179.99988388675877, 0.0), (0.5, 1.5, 1.5), "Trim_A_3m_B4", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3024.9995, 5093.0537, 805.78394), (0.0, -89.99999818714215, 0.0), (0.5, 1.5, 1.5), "Trim_A_3m_B8", _folder)
if a: placed += 1
else: skipped += 1

# Batch 59: StaticMesh'Defiled_Statues_B' (2 instances)
_mesh_path = "/Game/Art/Assets/Kits/Deco/Defiled/Defiled_Statues_B"
_materials = ['/Game/Art/Assets/Kits/Deco/Defiled/Materials/Defiled_Statues_A/MI_Defiled_Statues_A']
_folder = "Reconstruction/BD_BB_Chapter5_BrokenSeal/Meshes"
a = spawn_static_mesh(_mesh_path, _materials, (1278.3647, 3217.4006, 1458.8408), (0.0, -94.99994731507765, 0.0), (2.6079257, 2.6079257, 2.65625), "Defiled_Statues_B2", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3154.6257, 1259.3964, 1396.6799), (0.0, -4.999999999933509, 0.0), (2.607926, 2.607926, 2.607926), "Defiled_Statues_B6", _folder)
if a: placed += 1
else: skipped += 1

# Batch 60: StaticMesh'Defiled_Statues_A_Damaged_A' (1 instances)
_mesh_path = "/Game/Art/Assets/Kits/Deco/Defiled/Defiled_Statues_Damaged/Defiled_Statues_A_Damaged_A"
_materials = ['/Game/Art/Assets/Kits/Deco/Defiled/Materials/Defiled_Statues_A/MI_Defiled_Statues_A', '/Game/Environments/Models/Architecture/Materials/MI_ArchSimple_Stone_Damaged_A_MAT']
_folder = "Reconstruction/BD_BB_Chapter5_BrokenSeal/Meshes"
a = spawn_static_mesh(_mesh_path, _materials, (3260.2805, 4607.4497, 983.8176), (65.24894686988625, 142.34021178486347, 82.00171048458884), (2.607926, 2.607926, 2.607926), "Defiled_Statues_A_Damaged_A_37", _folder)
if a: placed += 1
else: skipped += 1

# Batch 61: StaticMesh'Defiled_Statues_A_Damaged_B' (1 instances)
_mesh_path = "/Game/Art/Assets/Kits/Deco/Defiled/Defiled_Statues_Damaged/Defiled_Statues_A_Damaged_B"
_materials = ['/Game/Art/Assets/Kits/Deco/Defiled/Materials/Defiled_Statues_A/MI_Defiled_Statues_A', '/Game/Environments/Models/Architecture/Materials/MI_ArchSimple_Stone_Damaged_A_MAT']
_folder = "Reconstruction/BD_BB_Chapter5_BrokenSeal/Meshes"
a = spawn_static_mesh(_mesh_path, _materials, (3118.6082, 4555.3184, 769.3286), (-14.56395911349705, 169.62486571375467, 64.79514057358017), (2.607926, 2.607926, 2.607926), "Defiled_Statues_A_Damaged_B_28", _folder)
if a: placed += 1
else: skipped += 1

# Batch 62: StaticMesh'Defiled_Statues_A_Damaged_C' (1 instances)
_mesh_path = "/Game/Art/Assets/Kits/Deco/Defiled/Defiled_Statues_Damaged/Defiled_Statues_A_Damaged_C"
_materials = ['/Game/Art/Assets/Kits/Deco/Defiled/Materials/Defiled_Statues_A/MI_Defiled_Statues_A', '/Game/Environments/Models/Architecture/Materials/MI_ArchSimple_Stone_Damaged_A_MAT']
_folder = "Reconstruction/BD_BB_Chapter5_BrokenSeal/Meshes"
a = spawn_static_mesh(_mesh_path, _materials, (2868.3843, 4295.3184, 741.427), (-11.938843259590435, -91.49818725569816, 78.29137207906017), (2.607926, 2.607926, 2.607926), "Defiled_Statues_A_Damaged_C_31", _folder)
if a: placed += 1
else: skipped += 1

# Batch 63: StaticMesh'Defiled_Statues_A_Damaged_D' (1 instances)
_mesh_path = "/Game/Art/Assets/Kits/Deco/Defiled/Defiled_Statues_Damaged/Defiled_Statues_A_Damaged_D"
_materials = ['/Game/Environments/Models/Architecture/Materials/MI_ArchSimple_Stone_Damaged_A_MAT', '/Game/Art/Assets/Kits/Deco/Defiled/Materials/Defiled_Statues_A/MI_Defiled_Statues_A']
_folder = "Reconstruction/BD_BB_Chapter5_BrokenSeal/Meshes"
a = spawn_static_mesh(_mesh_path, _materials, (3068.383, 4526.377, 668.31085), (-21.995362791969207, -125.67136635895504, 75.72001663430507), (2.607926, 2.607926, 2.607926), "Defiled_Statues_A_Damaged_D_41", _folder)
if a: placed += 1
else: skipped += 1

# Batch 64: StaticMesh'Defiled_Statues_A_Damaged_E' (1 instances)
_mesh_path = "/Game/Art/Assets/Kits/Deco/Defiled/Defiled_Statues_Damaged/Defiled_Statues_A_Damaged_E"
_materials = ['/Game/Art/Assets/Kits/Deco/Defiled/Materials/Defiled_Statues_A/MI_Defiled_Statues_A', '/Game/Environments/Models/Architecture/Materials/MI_ArchSimple_Stone_Damaged_A_MAT']
_folder = "Reconstruction/BD_BB_Chapter5_BrokenSeal/Meshes"
a = spawn_static_mesh(_mesh_path, _materials, (2975.419, 4405.2397, 578.6023), (-0.6292431766906247, -105.32293853176348, 60.95088956458879), (2.607926, 2.607926, 2.607926), "Defiled_Statues_A_Damaged_E_34", _folder)
if a: placed += 1
else: skipped += 1

# Batch 65: StaticMesh'Remains_Bones_Cranium' (3 instances)
_mesh_path = "/Game/Art/Assets/Kits/Deco/Remains/Remains_Bones_Cranium"
_materials = ['/Game/Art/Assets/Kits/Deco/Remains/Materials/Remains_Bones_Cranium_Orc/MI_Remains_Bones_Cranium_Orc']
_folder = "Reconstruction/BD_BB_Chapter5_BrokenSeal/Meshes"
a = spawn_static_mesh(_mesh_path, _materials, (2501.3806, 4360.515, 1236.9844), (76.55647687637152, 179.99995901886678, 6.26344580808959e-07), (1.0, 1.0, 1.0), "Remains_Bones_Cranium_11", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3881.24, 4324.5586, 1341.9861), (76.5564192218388, -125.0662573979371, 0.00013540877900365556), (1.0, 1.0, 1.0), "Remains_Bones_Cranium2", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4007.0889, 2302.002, 1240.0303), (76.55618408628646, 60.89257553599193, 0.00011687531186096448), (1.0, 1.0, 1.0), "Remains_Bones_Cranium3", _folder)
if a: placed += 1
else: skipped += 1

# Batch 66: StaticMesh'Remains_Bones_Assemblage_B' (3 instances)
_mesh_path = "/Game/Art/Assets/Kits/Deco/Warrens_Tomb/Remains_Bones_Assemblage_B"
_materials = ['/Game/Art/Assets/Kits/Deco/Orc/Shanty/Material/Orc_Shanty_Midden/MI_Orc_Shanty_Midden_Mat_Inst']
_folder = "Reconstruction/BD_BB_Chapter5_BrokenSeal/Meshes"
a = spawn_static_mesh(_mesh_path, _materials, (2479.7695, 4313.923, 1232.7654), (0.0, -179.99998633961752, -0.0), (1.0, 1.0, 1.0), "Remains_Bones_Assemblage_B_14", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3906.9595, 4280.102, 1337.7671), (0.0, -125.06640553826546, 0.0), (1.0, 1.0, 1.0), "Remains_Bones_Assemblage_B2", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3976.8933, 2343.5479, 1235.8115), (0.0, 60.8923371018963, -0.0), (1.0, 1.0, 1.0), "Remains_Bones_Assemblage_B3", _folder)
if a: placed += 1
else: skipped += 1

# Batch 67: StaticMesh'Ruin_Wall_Brick_A' (3 instances)
_mesh_path = "/Game/Art/Assets/Kits/Deco_Architecture/Ruins/Ruin_Wall_Brick_A"
_materials = ['/Game/Art/Assets/Kits/Architecture/Suburbs/Destructable/Materials/MI_Suburbs_Wall_Dest']
_folder = "Reconstruction/BD_BB_Chapter5_BrokenSeal/Meshes"
a = spawn_static_mesh(_mesh_path, _materials, (1464.062, 3526.2424, 1290.5312), (0.0, 177.193610284422, -0.0), (2.2473605, 1.787007, 1.787007), "Ruin_Wall_Brick_A2", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1381.6626, 3526.2422, 1289.4971), (0.0, 177.193610284422, -0.0), (1.787007, 1.787007, 1.787007), "Ruin_Wall_Brick_A3", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1434.9751, 3518.4636, 1359.5039), (0.00019124525345298564, 179.79398085271754, 179.99997950942867), (3.9048133, 1.787007, 2.6109505), "Ruin_Wall_Brick_A4", _folder)
if a: placed += 1
else: skipped += 1

# Batch 68: StaticMesh'Ruin_Wall_Brick_D' (1 instances)
_mesh_path = "/Game/Art/Assets/Kits/Deco_Architecture/Ruins/Ruin_Wall_Brick_D"
_materials = ['/Game/Art/Assets/Kits/Architecture/Suburbs/Destructable/Materials/MI_Suburbs_Wall_Dest']
_folder = "Reconstruction/BD_BB_Chapter5_BrokenSeal/Meshes"
a = spawn_static_mesh(_mesh_path, _materials, (1711.6631, 4026.8179, 950.3657), (0.0, 134.99997422266742, -0.0), (1.0015874, 1.0015874, 1.0015874), "Ruin_Wall_Brick_D_33", _folder)
if a: placed += 1
else: skipped += 1

# Batch 69: StaticMesh'Ruin_Wall_Brick_E' (1 instances)
_mesh_path = "/Game/Art/Assets/Kits/Deco_Architecture/Ruins/Ruin_Wall_Brick_E"
_materials = ['/Game/Art/Assets/Kits/Architecture/Suburbs/Destructable/Materials/MI_Suburbs_Wall_Dest']
_folder = "Reconstruction/BD_BB_Chapter5_BrokenSeal/Meshes"
a = spawn_static_mesh(_mesh_path, _materials, (1690.608, 4102.8525, 941.08716), (0.0, -179.99998633961752, -0.0), (1.0, 1.0, 1.0), "Ruin_Wall_Brick_E_36", _folder)
if a: placed += 1
else: skipped += 1

# Batch 70: StaticMesh'Dirt_Mound_A' (14 instances)
_mesh_path = "/Game/Art/Assets/Kits/Misc/Dirt_Mounds/Dirt_Mound_A"
_materials = ['/Game/Art/Assets/Kits/Misc/Dirt_Mounds/Materials/MI_Mines_Dirt']
_folder = "Reconstruction/BD_BB_Chapter5_BrokenSeal/Meshes"
a = spawn_static_mesh(_mesh_path, _materials, (519.69403, 1902.8359, 970.1277), (-34.39898356709693, -71.62353479330167, 8.358770194739487), (1.21875, 1.0, 1.0), "Dirt_Mound_A_2", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3442.885, 4942.659, 843.29785), (-33.86761905763131, -179.99995901886723, -3.0240823826618413e-13), (0.689186, 0.9842334, 1.0), "Dirt_Mound_A10", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5107.4893, 1773.1139, 1006.9245), (29.07883818719665, -140.2026401662648, -4.067231471249566), (0.54755265, 0.71291924, 1.3808327), "Dirt_Mound_A14_36", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1983.0947, 460.78818, 1034.0742), (32.13569473240971, -26.028076532605006, 2.6363086643116618), (1.9229301, 3.25, 1.0), "Dirt_Mound_A15", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3174.8823, 31.063538, 1388.9753), (0.0, 0.0, -0.0), (1.92293, 3.25, 1.0), "Dirt_Mound_A16", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4191.966, 236.72473, 1399.0238), (0.0, 21.62347130567584, -0.0), (1.92293, 1.9029847, 1.0), "Dirt_Mound_A17", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (370.70633, 2161.9236, 1173.2529), (-34.471650463198365, -67.11349540666605, 6.0458307198157435), (1.21875, 1.84375, 1.0), "Dirt_Mound_A2", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (367.40283, 2291.395, 1248.2227), (-33.831361826412625, -72.99603418983833, 8.921620141927246), (1.2437506, 3.25, 1.0), "Dirt_Mound_A3", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1045.4585, 2506.2217, 936.3345), (0.0, -64.99993826502799, 0.0), (1.0, 1.0, 2.0591667), "Dirt_Mound_A4_33", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1111.9658, 2671.0264, 936.3345), (0.0, -179.11690232456655, 0.0), (0.9360953, 0.94449407, 1.8090147), "Dirt_Mound_A5", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1321.0391, 3593.5093, 928.95386), (0.0, -31.26455524288444, 0.0), (1.0, 1.34375, 2.107574), "Dirt_Mound_A6_16", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2654.0112, 5291.0664, 934.84546), (0.0, 91.25473589108732, -0.0), (1.0, 1.0, 1.1631095), "Dirt_Mound_A7_5", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3739.708, 5321.776, 934.84546), (0.0, -129.7926348467252, 0.0), (1.4039236, 1.2643716, 1.6763425), "Dirt_Mound_A8", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2878.0986, 4940.8677, 866.19214), (32.01040035104671, -179.9999863333814, -1.6331476436017005), (0.5, 0.84375, 1.0), "Dirt_Mound_A9_33", _folder)
if a: placed += 1
else: skipped += 1

# Batch 71: StaticMesh'Dirt_Mound_B' (14 instances)
_mesh_path = "/Game/Art/Assets/Kits/Misc/Dirt_Mounds/Dirt_Mound_B"
_materials = ['/Game/Art/Assets/Kits/Misc/Dirt_Mounds/Materials/MI_Mines_Dirt']
_folder = "Reconstruction/BD_BB_Chapter5_BrokenSeal/Meshes"
a = spawn_static_mesh(_mesh_path, _materials, (1318.6592, 2782.4624, 936.3345), (0.0, -142.74872947511966, 0.0), (1.0, 2.1310008, 1.0), "Dirt_Mound_B_40", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4122.5674, 6078.4478, 1386.3347), (0.0, 167.303446577967, -0.0), (1.59375, 1.0, 1.625), "Dirt_Mound_B11_111", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2126.2356, 5936.2695, 1083.1412), (-35.89617693082159, -164.167662090493, 2.0959334988211897), (1.40625, 1.0, 1.5), "Dirt_Mound_B13_126", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2446.9138, 6055.552, 1305.9131), (-30.869932101017184, -155.3853614964932, -2.427001224357681), (1.40625, 1.0, 1.5), "Dirt_Mound_B14", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (431.67172, 4219.135, 1136.4147), (32.37605295149575, -104.51882354936735, -0.4454033720057643), (1.0, 2.033505, 1.304773), "Dirt_Mound_B17", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (395.33395, 4078.8145, 1228.3174), (32.37605295149575, -104.51882354936735, -0.4454033720057643), (1.0, 2.033505, 1.304773), "Dirt_Mound_B18", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1088.104, 3965.73, 936.3345), (0.0, -112.97027454960354, 0.0), (1.4376563, 1.0, 1.0), "Dirt_Mound_B2_6", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1097.1167, 3709.48, 936.84717), (0.0, 0.07995605507787443, -0.0), (1.0182486, 1.3442484, 1.0), "Dirt_Mound_B3", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1499.4849, 2931.9636, 936.3345), (0.0, -92.1514225006382, 0.0), (0.5251653, 1.3156229, 0.8623351), "Dirt_Mound_B4", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (550.98926, 4579.602, 888.6667), (32.019276072803294, -113.83246092044224, -4.727053732134605), (1.0, 2.0335052, 1.3047732), "Dirt_Mound_B5_114", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (429.87, 4256.084, 1119.3295), (31.611878245852363, -113.94558021660852, -4.455050466294559), (1.751868, 2.1220794, 1.304773), "Dirt_Mound_B6", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4092.836, 5306.226, 981.3345), (0.0, 159.28375141733898, -0.0), (1.7700809, 1.303842, 1.4339892), "Dirt_Mound_B7_16", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4713.4746, 4850.4116, 931.3345), (0.0, 134.18179641002493, -0.0), (2.0488338, 1.303842, 1.433989), "Dirt_Mound_B8", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5114.628, 944.5813, 1202.144), (-30.164090920711608, 41.54980750949461, 0.00011986275123149335), (1.0, 1.0, 1.0), "Dirt_Mound_B9_80", _folder)
if a: placed += 1
else: skipped += 1

# Batch 72: StaticMesh'Dirt_Mound_C' (10 instances)
_mesh_path = "/Game/Art/Assets/Kits/Misc/Dirt_Mounds/Dirt_Mound_C"
_materials = ['/Game/Art/Assets/Kits/Misc/Dirt_Mounds/Materials/MI_Mines_Dirt']
_folder = "Reconstruction/BD_BB_Chapter5_BrokenSeal/Meshes"
a = spawn_static_mesh(_mesh_path, _materials, (5477.299, 5117.3784, 887.2697), (29.999978987988097, 130.00087818255687, 0.00035169201708865565), (1.8779129, 1.1525362, 2.0981266), "Dirt_Mound_C10_182", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5351.316, 5311.4004, 1041.7764), (34.19086713059801, 139.16723065443946, 4.582888222056036), (1.6961827, 1.388803, 1.3089722), "Dirt_Mound_C11", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5117.3496, 5427.27, 1143.383), (-37.22244157673415, -45.2939809494735, -76.3705466467687), (1.877913, 1.152536, 2.098127), "Dirt_Mound_C13", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3596.3228, 5387.2236, 1395.4202), (0.0, 15.171508742250998, -0.0), (0.53125, 1.53125, 1.40625), "Dirt_Mound_C17_123", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2909.869, 1488.9907, 851.176), (-25.177460126857554, 0.5805052769023022, 5.0920358028525285), (0.6312668, 1.5422355, 0.73997736), "Dirt_Mound_C18_187", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3448.091, 1488.6069, 842.7007), (26.889217540785918, 5.093871898122353, 5.167391721038209), (0.631267, 1.0, 0.739977), "Dirt_Mound_C19", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2752.9194, 5105.0083, 936.3345), (0.0, 124.64503581703129, -0.0), (0.8710198, 1.574692, 1.0), "Dirt_Mound_C6_11", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3612.8916, 5104.0967, 934.87695), (0.0, -118.96587952046899, 0.0), (1.0, 1.4058617, 1.2097504), "Dirt_Mound_C7_20", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3599.2412, 5333.398, 1397.4053), (0.0, 32.91740564629375, -0.0), (0.69346046, 1.8318808, 1.1875), "Dirt_Mound_C8_66", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2799.3906, 5288.702, 1396.6333), (0.0, -82.24263900988569, 0.0), (0.8262264, 1.0560467, 1.1101439), "Dirt_Mound_C9_84", _folder)
if a: placed += 1
else: skipped += 1

# Batch 73: StaticMesh'Dirt_Mound_D' (3 instances)
_mesh_path = "/Game/Art/Assets/Kits/Misc/Dirt_Mounds/Dirt_Mound_D"
_materials = ['/Game/Art/Assets/Kits/Misc/Dirt_Mounds/Materials/MI_Mines_Dirt']
_folder = "Reconstruction/BD_BB_Chapter5_BrokenSeal/Meshes"
a = spawn_static_mesh(_mesh_path, _materials, (4349.175, 1323.7639, 928.73126), (0.0, -66.93813665915863, 0.0), (1.0, 1.2449344, 1.0), "Dirt_Mound_D_90", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5147.2393, 911.7567, 1191.426), (4.09714826584202e-05, 127.34767960841128, -31.038147820353462), (0.875, 0.6875, 0.8125), "Dirt_Mound_D2_71", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2424.0303, 1429.5323, 936.33606), (0.0, -95.85629310476014, 0.0), (0.6981737, 0.6981737, 0.6078235), "Dirt_Mound_D3_31", _folder)
if a: placed += 1
else: skipped += 1

# Batch 74: StaticMesh'Dirt_Mound_F' (8 instances)
_mesh_path = "/Game/Art/Assets/Kits/Misc/Dirt_Mounds/Dirt_Mound_F"
_materials = ['/Game/Art/Assets/Kits/Misc/Dirt_Mounds/Materials/MI_Mines_Dirt']
_folder = "Reconstruction/BD_BB_Chapter5_BrokenSeal/Meshes"
a = spawn_static_mesh(_mesh_path, _materials, (3526.9458, 5271.135, 1396.498), (0.0, -179.99998633961752, -0.0), (0.6663937, 0.46395057, 0.78086823), "Dirt_Mound_F_72", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4718.1206, 593.2803, 1400.0), (0.0, -91.33172777287928, 0.0), (1.0, 1.0, 1.0), "Dirt_Mound_F2_83", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4894.924, 4615.0503, 933.7207), (0.0, -158.93753152462418, 0.0), (1.0, 1.0, 1.0), "Dirt_Mound_F3_167", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4854.8037, 4647.2256, 937.01025), (0.0, -148.9483095377506, 0.0), (1.31939, 1.0, 1.0), "Dirt_Mound_F4_5", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4491.2764, 5933.998, 1396.3652), (0.0, -108.36020544111118, 0.0), (1.31939, 1.0, 1.1914124), "Dirt_Mound_F5", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4064.1829, 6075.744, 1396.3652), (0.0, -108.36020544111118, 0.0), (1.31939, 1.0, 1.191412), "Dirt_Mound_F6", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3437.3022, 6237.5425, 1399.9998), (0.0, -98.118102002649, 0.0), (1.31939, 1.0, 1.191412), "Dirt_Mound_F7", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3055.8757, 6259.2607, 1399.9998), (0.0, -70.57500962741216, 0.0), (1.31939, 1.0, 1.191412), "Dirt_Mound_F8", _folder)
if a: placed += 1
else: skipped += 1

# Batch 75: StaticMesh'Dirt_Mound_G' (9 instances)
_mesh_path = "/Game/Art/Assets/Kits/Misc/Dirt_Mounds/Dirt_Mound_G"
_materials = ['/Game/Art/Assets/Kits/Misc/Dirt_Mounds/Materials/MI_Mines_Dirt']
_folder = "Reconstruction/BD_BB_Chapter5_BrokenSeal/Meshes"
a = spawn_static_mesh(_mesh_path, _materials, (1679.0132, 3190.0132, 936.92676), (0.0, -179.99998633961752, -0.0), (1.0, 1.0, 0.47987142), "Dirt_Mound_G_111", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4363.237, 3222.3875, 793.58344), (0.0, -179.99998633961752, -0.0), (1.4966018, 1.3704317, 1.5079944), "Dirt_Mound_G10_185", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1090.0387, 3909.7253, 987.6763), (0.0, 155.37813494427823, -0.0), (0.84310216, 1.0, 0.6875), "Dirt_Mound_G11_2", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (201.97998, 2921.2083, 1397.0059), (0.0, -179.99998633961752, -0.0), (1.0, 1.0, 1.4318491), "Dirt_Mound_G12_417", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2433.276, 5329.0854, 987.67615), (0.0, -69.58966455940573, 0.0), (0.8754412, 1.0004412, 0.9919473), "Dirt_Mound_G13_8", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (201.9801, 3243.163, 1397.0059), (0.0, 175.24401792194305, -0.0), (1.0, 1.0, 1.431849), "Dirt_Mound_G14", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4665.7417, 2934.8416, 936.70825), (0.0, -101.06402838166392, 0.0), (1.1905758, 0.833408, 1.7238231), "Dirt_Mound_G2_156", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4648.7856, 3569.3982, 935.5642), (0.0, -91.0170861362207, 0.0), (1.0, 0.6679525, 1.0), "Dirt_Mound_G3_168", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5194.415, 4532.9243, 799.3635), (0.0, -154.99995719010084, 0.0), (1.0, 0.72952527, 1.3125), "Dirt_Mound_G5_170", _folder)
if a: placed += 1
else: skipped += 1

# Batch 76: StaticMesh'Dirt_Mound_H' (32 instances)
_mesh_path = "/Game/Art/Assets/Kits/Misc/Dirt_Mounds/Dirt_Mound_H"
_materials = ['/Game/Art/Assets/Kits/Misc/Dirt_Mounds/Materials/MI_Mines_Dirt']
_folder = "Reconstruction/BD_BB_Chapter5_BrokenSeal/Meshes"
a = spawn_static_mesh(_mesh_path, _materials, (4858.9404, 2939.6177, 936.9326), (0.0, -179.99998633961752, -0.0), (1.0, 1.0, 1.0), "Dirt_Mound_H_162", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5174.0625, 1853.562, 930.4716), (14.826582273354353, 178.66289881605792, -15.288665502520468), (0.47591782, 0.47591782, 1.7799294), "Dirt_Mound_H10_40", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1766.6776, 5097.764, 800.98096), (0.0, -146.4019767411747, 0.0), (1.53125, 1.001959, 0.25), "Dirt_Mound_H13", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3523.0, 5470.0, 1402.0), (0.0, -179.8428987923843, 0.0), (1.0, 1.0, 1.0), "Dirt_Mound_H14_2", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2875.0, 5470.0, 1402.0), (0.0, -149.9999007336502, 0.0), (1.0, 1.0, 1.0), "Dirt_Mound_H15", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2269.3364, 4972.138, 935.0), (0.0, 94.58678818648985, -0.0), (1.0, 1.0, 1.0), "Dirt_Mound_H16_2", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3754.4568, 5425.221, 987.6761), (0.0, -159.7322763558109, 0.0), (1.6488396, 1.6488396, 1.6488396), "Dirt_Mound_H17_11", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1656.3901, 2424.0244, 924.90356), (0.0, -179.99998633961752, -0.0), (1.0, 1.0, 1.0), "Dirt_Mound_H18_14", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1634.2979, 4006.3848, 936.3345), (0.0, -179.99998633961752, -0.0), (1.0, 1.0, 1.125), "Dirt_Mound_H19_17", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4850.1074, 1910.7644, 938.4514), (0.0, -179.99998633961752, -0.0), (1.0, 1.0, 1.0), "Dirt_Mound_H2_171", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2756.0, 1517.0, 938.0), (0.0, -179.99998633961752, -0.0), (0.34375, 0.34375, 0.34375), "Dirt_Mound_H20_18", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2721.7756, 5169.9272, 985.40765), (0.0, 81.22969316827896, -0.0), (1.2223878, 1.2223878, 1.2223878), "Dirt_Mound_H21_115", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2745.0, 4942.0, 935.0), (0.0, -179.99998633961752, -0.0), (0.375, 0.59375, 1.0), "Dirt_Mound_H22", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4978.0454, 3602.954, 936.9326), (0.0, -89.24456352587322, 0.0), (0.625, 0.40625, 0.5625), "Dirt_Mound_H23", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3820.0986, 5200.267, 987.67615), (0.0, -6.006927025205677, 0.0), (1.64884, 1.64884, 1.64884), "Dirt_Mound_H24", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3585.0059, 5416.347, 1400.0), (0.0, -34.33422694921789, 0.0), (1.0, 1.0, 1.0), "Dirt_Mound_H25", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2925.9229, 2119.9202, 795.0), (0.0, 163.12556805869986, -0.0), (1.0, 1.25, 1.0), "Dirt_Mound_H26_93", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2438.0, 4096.0, 789.0), (0.0, -179.99998633961752, -0.0), (1.0, 1.0, 1.0), "Dirt_Mound_H27_106", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3903.5542, 4176.459, 799.0), (0.0, 138.04614056963177, -0.0), (1.0, 1.0, 1.0), "Dirt_Mound_H29_113", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5262.012, 1101.6349, 1101.84), (0.0, 175.70745895829918, -0.0), (0.95925254, 1.0, 1.3125), "Dirt_Mound_H3_77", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4286.9556, 3675.1643, 799.0), (0.0, -131.19623732893405, 0.0), (1.0, 1.0, 1.0), "Dirt_Mound_H30", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2928.9495, 5315.412, 1402.0), (0.0, 45.99005078293658, -0.0), (1.0, 1.0, 1.0), "Dirt_Mound_H31_113", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (703.60236, 1659.2561, 787.4862), (0.0, -125.55516980324126, 0.0), (1.0, 1.0, 1.3007358), "Dirt_Mound_H32", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (778.90875, 1565.7917, 793.07684), (0.0, -161.26481199062283, 0.0), (1.0, 1.0, 1.000771), "Dirt_Mound_H33", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2104.0667, 4948.149, 935.0), (0.0, -67.52978051745603, 0.0), (0.8943723, 0.81620604, 0.8943723), "Dirt_Mound_H34", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2959.9558, 1533.535, 795.0), (0.0, -158.98667434486254, 0.0), (1.0, 1.25, 1.0), "Dirt_Mound_H35", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1460.38, 2247.129, 936.3347), (0.0, 151.60036324978813, -0.0), (1.0, 1.0, 1.0), "Dirt_Mound_H5_181", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (682.7757, 4788.956, 798.7561), (0.0, 136.05914225535025, -0.0), (1.6010624, 1.7868568, 1.5693067), "Dirt_Mound_H8_240", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (928.8154, 2968.0178, 1405.8076), (0.0, -166.9934174589252, 0.0), (1.0, 1.0, 0.41623074), "Dirt_Mound_H9_264", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3167.2217, 4239.732, 790.39825), (0.0, -53.173892557946616, 0.0), (2.681879, 2.681879, 1.564303), "Dirt_Mound_I21_138", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3167.2217, 4042.997, 783.59436), (-0.6759032475142694, 140.04354266182776, 0.5662671195213064), (2.681879, 2.681879, 1.3933295), "Dirt_Mound_I22", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3511.4387, 4172.288, 779.543), (-0.6759032396689105, 140.0435426621436, 0.5662670069237937), (2.681879, 2.681879, 1.39333), "Dirt_Mound_I25", _folder)
if a: placed += 1
else: skipped += 1

# Batch 77: StaticMesh'Dirt_Mound_I' (37 instances)
_mesh_path = "/Game/Art/Assets/Kits/Misc/Dirt_Mounds/Dirt_Mound_I"
_materials = ['/Game/Art/Assets/Kits/Misc/Dirt_Mounds/Materials/MI_Mines_Dirt']
_folder = "Reconstruction/BD_BB_Chapter5_BrokenSeal/Meshes"
a = spawn_static_mesh(_mesh_path, _materials, (3618.0781, 1938.4694, 776.8253), (1.8699477340713384e-07, -130.0794296545351, 2.379914132026067), (1.0, 1.0, 1.126969), "Dirt_Mound_I10_35", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4821.419, 1747.4349, 935.0), (0.0, -173.44782827474373, 0.0), (1.0, 1.0, 0.53125), "Dirt_Mound_I11_2", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3820.262, 1171.2097, 935.0), (0.0, 60.03703050400581, -0.0), (1.0, 1.0, 1.0), "Dirt_Mound_I12_8", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1389.3258, 2082.9492, 806.7964), (4.783065537201153, 69.61422558467109, -1.7451783088629829), (1.0, 1.0625, 1.28125), "Dirt_Mound_I13_11", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2054.7224, 1326.2773, 761.63043), (1.6374966946802583, 33.29002682938125, -2.20324683132087), (1.25, 1.0625, 1.40625), "Dirt_Mound_I14", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1992.0569, 1363.5153, 863.09766), (1.3630025952068577e-05, -95.2637373043699, -23.565887699910082), (0.7119236, 0.6164499, 0.800626), "Dirt_Mound_I15_29", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2402.094, 106.24143, 1315.766), (5.490235096580985, -77.97054934420379, -24.399809123180187), (0.6867564, 0.49925604, 0.84300613), "Dirt_Mound_I18_42", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3642.5579, 4367.5728, 796.4878), (0.0, -74.94735652305718, 0.0), (1.0, 1.0, 1.0), "Dirt_Mound_I19_68", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3677.5068, 4437.177, 790.1218), (0.0, -30.048520814655603, 0.0), (1.1208167, 1.1481348, 1.1208167), "Dirt_Mound_I20", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2334.3623, 252.61029, 1250.1439), (1.174648491256038, -95.97538841488911, -26.064273299022926), (0.686756, 0.499256, 0.843006), "Dirt_Mound_I23", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1333.1833, 4431.703, 793.60645), (0.0, 142.32641700947005, -0.0), (0.625, 0.625, 0.73516935), "Dirt_Mound_I24_229", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2861.5312, 6221.358, 1400.2954), (0.0, 170.69957122636393, -0.0), (0.4271357, 0.7059534, 0.7059534), "Dirt_Mound_I26_277", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4761.869, 3463.358, 936.33276), (0.0, -56.36358433196207, 0.0), (0.5750222, 0.6943796, 0.40436625), "Dirt_Mound_I27_299", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3902.3838, 4439.6143, 937.01025), (0.0, -179.99998633961752, -0.0), (0.34375, 0.34375, 0.38928097), "Dirt_Mound_I28_2", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2489.524, 4439.6143, 934.96387), (0.0, -140.96135729501216, 0.0), (0.34375, 0.21875, 0.21875), "Dirt_Mound_I29", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3971.2505, 1070.8535, 931.3357), (0.0, -85.95586010823162, 0.0), (1.0, 1.0, 1.0), "Dirt_Mound_I3_87", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4045.3738, 2238.4834, 937.46655), (0.0, 169.52174452142415, -0.0), (0.25, 0.25, 0.21875), "Dirt_Mound_I30", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2075.6367, 5102.2085, 796.9243), (0.0, 164.99923006628993, -0.0), (1.0, 1.0, 1.497881), "Dirt_Mound_I31_153", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1362.1056, 4306.8843, 795.13086), (0.0, -179.99998633961752, -0.0), (1.0, 1.0, 1.25), "Dirt_Mound_I32_158", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (111.6379, 3573.567, 1385.5568), (0.0, 92.15416443862107, -0.0), (0.78125, 0.71875, 1.0), "Dirt_Mound_I33_414", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2776.9688, 932.0, 1274.3071), (-12.964477649081182, -179.9999590188671, 3.158505365097978e-13), (0.99879634, 0.46875, 1.21875), "Dirt_Mound_I34_69", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1107.9524, 2649.9487, 977.9732), (1.8320282427884462, 148.65454845258142, 2.08120995666921), (1.0, 1.0, 0.5984517), "Dirt_Mound_I35", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2103.6887, 1488.4757, 923.64844), (15.091913245084578, -47.92986894369051, 12.229569131827818), (0.32472247, 0.29347247, 0.32206553), "Dirt_Mound_I36", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2723.45, 92.45453, 1392.6016), (0.0, -136.5253584274267, 0.0), (0.79269785, 0.79269785, 0.79269785), "Dirt_Mound_I37", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3554.5845, 48.17731, 1392.6016), (0.0, 24.98435374096006, -0.0), (0.792698, 0.792698, 0.792698), "Dirt_Mound_I38", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5218.709, 1986.5728, 781.753), (6.319512041199245e-08, 155.13757222007592, -14.274138461877873), (1.0, 1.0, 1.0), "Dirt_Mound_I39", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2591.5208, 1025.3236, 987.6763), (0.0, -58.745365975833224, 0.0), (0.84375, 0.8125, 0.84109277), "Dirt_Mound_I4_99", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5058.345, 2138.0803, 802.6602), (5.106802197036648, 74.58874941074254, -15.363676201294153), (1.0, 1.0, 1.0), "Dirt_Mound_I40", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5080.4775, 2114.647, 795.07214), (9.260117970082057, -104.12959301575336, 2.536171118129551), (1.0, 1.0, 1.0), "Dirt_Mound_I41", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4065.1567, 1083.4106, 982.56885), (0.0, -64.95757908409198, 0.0), (0.7313626, 0.7313626, 0.7313626), "Dirt_Mound_I42", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4069.5315, 4906.8174, 931.1213), (0.0, 116.82785437326312, -0.0), (0.34375, 0.34375, 0.21875), "Dirt_Mound_I43", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (305.2823, 3826.9966, 1314.0782), (16.269790967472463, -151.45852659345383, -3.0811757488503178), (0.78125, 0.71875, 1.1543108), "Dirt_Mound_I44", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5910.659, 3972.763, 796.0044), (0.0, -179.99998633961752, -0.0), (1.0, 1.0, 1.0), "Dirt_Mound_I5_115", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5916.7295, 3723.6995, 796.0044), (0.0, -111.31253162112519, 0.0), (1.0, 1.0, 1.0), "Dirt_Mound_I6", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5854.493, 4901.6626, 795.88257), (0.0, -179.99998633961752, -0.0), (1.0, 0.93934226, 1.1774914), "Dirt_Mound_I7_122", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5969.414, 2618.202, 799.8281), (0.0, -179.99998633961752, -0.0), (1.0, 0.78996766, 1.0), "Dirt_Mound_I8_125", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3582.7207, 1838.31, 794.48047), (0.0, -137.36376635641577, 0.0), (1.0, 1.0, 1.126969), "Dirt_Mound_I9_33", _folder)
if a: placed += 1
else: skipped += 1

# Batch 78: StaticMesh'Suburbs_Dirt_Mound_A' (1 instances)
_mesh_path = "/Game/Art/Assets/Kits/Misc/Dirt_Mounds/Suburbs_Dirt_Mound_A"
_materials = ['/Game/Art/Assets/Kits/Misc/Dirt_Mounds/Materials/MI_Mines_Dirt']
_folder = "Reconstruction/BD_BB_Chapter5_BrokenSeal/Meshes"
a = spawn_static_mesh(_mesh_path, _materials, (3884.8376, 5467.732, 1402.5178), (0.0, -30.422910989289573, 0.0), (1.0, 1.0, 1.0), "Suburbs_Dirt_Mound_A_111", _folder)
if a: placed += 1
else: skipped += 1

# Batch 79: StaticMesh'Suburbs_Dirt_Mound_C' (1 instances)
_mesh_path = "/Game/Art/Assets/Kits/Misc/Dirt_Mounds/Suburbs_Dirt_Mound_C"
_materials = ['/Game/Art/Assets/Kits/Misc/Dirt_Mounds/Materials/MI_Mines_Dirt']
_folder = "Reconstruction/BD_BB_Chapter5_BrokenSeal/Meshes"
a = spawn_static_mesh(_mesh_path, _materials, (3004.4558, 4516.9346, 774.10223), (0.0, -118.41183608245191, 0.0), (4.8924675, 4.8924675, 4.8924675), "Dirt_Mound_I_8", _folder)
if a: placed += 1
else: skipped += 1

# Batch 80: StaticMesh'Suburbs_Dirt_Mound_D' (1 instances)
_mesh_path = "/Game/Art/Assets/Kits/Misc/Dirt_Mounds/Suburbs_Dirt_Mound_D"
_materials = ['/Game/Art/Assets/Kits/Misc/Dirt_Mounds/Materials/Suburbs_Dirt_Inst']
_folder = "Reconstruction/BD_BB_Chapter5_BrokenSeal/Meshes"
a = spawn_static_mesh(_mesh_path, _materials, (1526.69, 3501.013, 935.53687), (0.0, -123.41732800420205, 0.0), (3.7623606, 4.1291757, 2.5191202), "Suburbs_Dirt_Mound_D_92", _folder)
if a: placed += 1
else: skipped += 1

# Batch 81: StaticMesh'SM_AR_City_Column_050x100x200_A_Shaft' (12 instances)
_mesh_path = "/Game/Environments/Models/Architecture/Meshes/SM_AR_City_Column_050x100x200_A_Shaft"
_materials = ['/Game/Environments/Models/Architecture/Materials/MI_Column_GreyStone_A_MAT_Inst']
_folder = "Reconstruction/BD_BB_Chapter5_BrokenSeal/Meshes"
a = spawn_static_mesh(_mesh_path, _materials, (4965.0728, 790.0381, 2229.2744), (0.0, -142.04311640445187, 0.0), (1.0, 1.0, 1.0), "SM_AR_City_Column_050x100x200_A_Shaft12", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5201.621, 974.5508, 2229.2744), (0.0, -142.04159257239658, 0.0), (1.0, 1.0, 1.0), "SM_AR_City_Column_050x100x200_A_Shaft16", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5360.339, 5284.6504, 2229.2744), (0.0, -44.0711045707933, 0.0), (1.0, 1.0, 1.0), "SM_AR_City_Column_050x100x200_A_Shaft20", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5144.808, 5493.325, 2229.2744), (0.0, -44.070464315267465, 0.0), (1.0, 1.0, 1.0), "SM_AR_City_Column_050x100x200_A_Shaft24", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2334.9292, 6039.5654, 2229.2744), (0.0, 18.558274250963276, -0.0), (1.0, 1.0, 1.0), "SM_AR_City_Column_050x100x200_A_Shaft28", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2050.525, 5944.1016, 2229.2744), (0.0, 18.55912887211676, -0.0), (1.0, 1.0, 1.0), "SM_AR_City_Column_050x100x200_A_Shaft32", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (442.7998, 4386.615, 2229.2744), (0.0, 73.21109371689414, -0.0), (1.0, 1.0, 1.0), "SM_AR_City_Column_050x100x200_A_Shaft36", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1985.5973, 421.92578, 2120.0), (0.0, 154.35291837231205, -0.0), (1.0, 1.0, 1.0), "SM_AR_City_Column_050x100x200_A_Shaft4", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (356.12402, 4099.411, 2229.2744), (0.0, 73.2126083023384, -0.0), (1.0, 1.0, 1.0), "SM_AR_City_Column_050x100x200_A_Shaft40", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (342.15283, 2280.2388, 2229.2744), (0.0, 109.37969068655943, -0.0), (1.0, 1.0, 1.0), "SM_AR_City_Column_050x100x200_A_Shaft44", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (441.68164, 1997.2319, 2229.2744), (0.0, 109.38152271357416, -0.0), (1.0, 1.0, 1.0), "SM_AR_City_Column_050x100x200_A_Shaft48", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2256.029, 292.05566, 2120.0), (0.0, 154.35291837231205, -0.0), (1.0, 1.0, 1.0), "SM_AR_City_Column_050x100x200_A_Shaft8", _folder)
if a: placed += 1
else: skipped += 1

# Batch 82: StaticMesh'SM_BrokenSeal_Trim' (2 instances)
_mesh_path = "/Game/Environments/Models/Architecture/Meshes/SM_BrokenSeal_Trim"
_materials = ['/Game/Art/Assets/Kits/Architecture/Suburbs/Materials/Suburbs_Floor_A/MI_Suburbs_Floor_A_2_NonDest_Dark']
_folder = "Reconstruction/BD_BB_Chapter5_BrokenSeal/Meshes"
a = spawn_static_mesh(_mesh_path, _materials, (2301.8584, 3243.3, 933.12646), (0.0, 3.051757709276941e-05, -0.0), (0.8125, 0.81249994, 0.81249994), "SM_BrokenSeal_Trim_5", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4054.5898, 3243.3, 933.126), (0.0, 179.99969264148905, -0.0), (0.8125, 0.8125, 0.8125), "SM_BrokenSeal_Trim2", _folder)
if a: placed += 1
else: skipped += 1

# Batch 83: StaticMesh'BrokenSeal_PaintableFloor_A_01' (1 instances)
_mesh_path = "/Game/LevelDesign/GuideMeshes/Chapter5/BrokenSeal/BrokenSeal_PaintableFloor_A_01"
_materials = ['/Game/Environments/ProcTexturing/GuideMeshFloor/M_GuideMeshFloor_Urban_Dirt']
_folder = "Reconstruction/BD_BB_Chapter5_BrokenSeal/Meshes"
a = spawn_static_mesh(_mesh_path, _materials, (0.0, 0.0, 0.0), (0.0, 0.0, -0.0), (1.0, 1.0, 1.0), "BrokenSeal_PaintableFloor_A_01_5", _folder)
if a: placed += 1
else: skipped += 1

# Batch 84: StaticMesh'BrokenSeal_PaintableFloor_A_02' (1 instances)
_mesh_path = "/Game/LevelDesign/GuideMeshes/Chapter5/BrokenSeal/BrokenSeal_PaintableFloor_A_02"
_materials = ['/Game/Environments/ProcTexturing/GuideMeshFloor/M_GuideMeshFloor_Urban_Dirt']
_folder = "Reconstruction/BD_BB_Chapter5_BrokenSeal/Meshes"
a = spawn_static_mesh(_mesh_path, _materials, (0.0, 0.0, 0.0), (0.0, 0.0, -0.0), (1.0, 1.0, 1.0), "BrokenSeal_PaintableFloor_A_02_7", _folder)
if a: placed += 1
else: skipped += 1

# Batch 85: StaticMesh'BrokenSeal_PaintableFloor_A_03' (1 instances)
_mesh_path = "/Game/LevelDesign/GuideMeshes/Chapter5/BrokenSeal/BrokenSeal_PaintableFloor_A_03"
_materials = ['/Game/Environments/ProcTexturing/GuideMeshFloor/M_GuideMeshFloor_Urban_Dirt']
_folder = "Reconstruction/BD_BB_Chapter5_BrokenSeal/Meshes"
a = spawn_static_mesh(_mesh_path, _materials, (0.0, 0.0, 0.0), (0.0, 0.0, -0.0), (1.0, 1.0, 1.0), "BrokenSeal_PaintableFloor_A_03_9", _folder)
if a: placed += 1
else: skipped += 1

# Batch 86: StaticMesh'BrokenSeal_PaintableFloor_A_04' (1 instances)
_mesh_path = "/Game/LevelDesign/GuideMeshes/Chapter5/BrokenSeal/BrokenSeal_PaintableFloor_A_04"
_materials = ['/Game/Environments/ProcTexturing/GuideMeshFloor/M_GuideMeshFloor_Urban_Dirt']
_folder = "Reconstruction/BD_BB_Chapter5_BrokenSeal/Meshes"
a = spawn_static_mesh(_mesh_path, _materials, (0.0, 0.0, 0.0), (0.0, 0.0, -0.0), (1.0, 1.0, 1.0), "BrokenSeal_PaintableFloor_A_04_11", _folder)
if a: placed += 1
else: skipped += 1

# Batch 87: StaticMesh'BrokenSeal_PaintableFloor_B_01' (1 instances)
_mesh_path = "/Game/LevelDesign/GuideMeshes/Chapter5/BrokenSeal/BrokenSeal_PaintableFloor_B_01"
_materials = ['/Game/Environments/ProcTexturing/GuideMeshFloor/M_GuideMeshFloor_Urban_Dirt']
_folder = "Reconstruction/BD_BB_Chapter5_BrokenSeal/Meshes"
a = spawn_static_mesh(_mesh_path, _materials, (0.0, 0.0, 0.0), (0.0, 0.0, -0.0), (1.0, 1.0, 1.0), "BrokenSeal_PaintableFloor_B_01_21", _folder)
if a: placed += 1
else: skipped += 1

# Batch 88: StaticMesh'BrokenSeal_PaintableFloor_B_02' (1 instances)
_mesh_path = "/Game/LevelDesign/GuideMeshes/Chapter5/BrokenSeal/BrokenSeal_PaintableFloor_B_02"
_materials = ['/Game/Environments/ProcTexturing/GuideMeshFloor/M_GuideMeshFloor_Urban_Dirt']
_folder = "Reconstruction/BD_BB_Chapter5_BrokenSeal/Meshes"
a = spawn_static_mesh(_mesh_path, _materials, (0.0, 0.0, 0.0), (0.0, 0.0, -0.0), (1.0, 1.0, 1.0), "BrokenSeal_PaintableFloor_B_02_23", _folder)
if a: placed += 1
else: skipped += 1

# Batch 89: StaticMesh'BrokenSeal_PaintableFloor_B_03' (1 instances)
_mesh_path = "/Game/LevelDesign/GuideMeshes/Chapter5/BrokenSeal/BrokenSeal_PaintableFloor_B_03"
_materials = ['/Game/Environments/ProcTexturing/GuideMeshFloor/M_GuideMeshFloor_Urban_Dirt']
_folder = "Reconstruction/BD_BB_Chapter5_BrokenSeal/Meshes"
a = spawn_static_mesh(_mesh_path, _materials, (0.0, 0.0, 0.0), (0.0, 0.0, -0.0), (1.0, 1.0, 1.0), "BrokenSeal_PaintableFloor_B_03_25", _folder)
if a: placed += 1
else: skipped += 1

# Batch 90: StaticMesh'BrokenSeal_PaintableFloor_B_04' (1 instances)
_mesh_path = "/Game/LevelDesign/GuideMeshes/Chapter5/BrokenSeal/BrokenSeal_PaintableFloor_B_04"
_materials = ['/Game/Environments/ProcTexturing/GuideMeshFloor/M_GuideMeshFloor_Urban_Dirt']
_folder = "Reconstruction/BD_BB_Chapter5_BrokenSeal/Meshes"
a = spawn_static_mesh(_mesh_path, _materials, (0.0, 0.0, 0.0), (0.0, 0.0, -0.0), (1.0, 1.0, 1.0), "BrokenSeal_PaintableFloor_B_04_27", _folder)
if a: placed += 1
else: skipped += 1

# Batch 91: StaticMesh'BrokenSeal_PaintableFloor_C_02' (1 instances)
_mesh_path = "/Game/LevelDesign/GuideMeshes/Chapter5/BrokenSeal/BrokenSeal_PaintableFloor_C_02"
_materials = ['/Game/Environments/ProcTexturing/GuideMeshFloor/M_GuideMeshFloor_Urban_Dirt']
_folder = "Reconstruction/BD_BB_Chapter5_BrokenSeal/Meshes"
a = spawn_static_mesh(_mesh_path, _materials, (0.0, 0.0, 0.0), (0.0, 0.0, -0.0), (1.0, 1.0, 1.0), "BrokenSeal_PaintableFloor_C_02_34", _folder)
if a: placed += 1
else: skipped += 1

# Batch 92: StaticMesh'PWM_Nordic_8x8x8_A' (13 instances)
_mesh_path = "/Game/Unshippable/Whitebox/Rocks/Meshes/PWM_Nordic_8x8x8_A"
_materials = ['/Game/Environments/ProcTexturing/ProcMaterial_Quarry_2mx5m_B2']
_folder = "Reconstruction/BD_BB_Chapter5_BrokenSeal/Meshes"
a = spawn_static_mesh(_mesh_path, _materials, (3420.4517, 3194.3113, 2718.7021), (-76.86379458518418, -23.240165130563874, 26.196770397674655), (1.136463, 1.201167, 1.477917), "PWM_Nordic_8x8x8_A15_143", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2569.9023, 3283.2324, 2678.5415), (81.70351700724461, 148.50751595766675, 150.25157604275458), (1.2464247, 1.3853344, 1.477917), "PWM_Nordic_8x8x8_A16", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5954.38, 4458.956, 2523.3933), (24.805514070040505, 8.317749144433728, -174.54327471559827), (0.9207399, 1.1923336, 1.401583), "PWM_Nordic_8x8x8_A29", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5513.5557, 5457.593, 2515.62), (-15.01711669035127, -150.76134542853265, -179.7361422792633), (1.094264, 0.875, 1.1875), "PWM_Nordic_8x8x8_A30", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5138.868, 4878.999, 2705.1194), (19.982726267947527, -150.60031536596549, 0.2711179579172028), (1.1548715, 0.938858, 1.401583), "PWM_Nordic_8x8x8_A31", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4736.2, 5944.695, 2709.0737), (-15.01711669035127, -150.76134542853265, -179.7361422792633), (1.094264, 0.6431298, 0.92318124), "PWM_Nordic_8x8x8_A32_62", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4521.16, 3046.7979, 2734.749), (58.10874512239739, -3.992674751171433, 173.82172054938115), (0.942814, 1.247377, 1.258672), "PWM_Nordic_8x8x8_A35", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5874.1084, 3233.2405, 2561.249), (58.10874512239739, -3.992674751171433, 173.82172054938115), (0.942814, 1.247377, 1.297056), "PWM_Nordic_8x8x8_A36", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (6280.2207, 2372.8372, 1040.946), (3.9907082303716743, 108.48931262894445, 0.2150824836719711), (0.717532, 0.26522997, 0.717532), "PWM_Nordic_8x8x8_A37", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (540.3618, 5491.085, 1967.3424), (-1.5655517219962727, -141.569958485806, -1.3224486130711615), (0.717532, 0.717532, 0.717532), "PWM_Nordic_8x8x8_A38", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (927.9837, 5798.6436, 1980.8662), (-1.5655517219962727, -141.569958485806, -1.3224486130711615), (0.717532, 0.717532, 0.717532), "PWM_Nordic_8x8x8_A39", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3839.2449, 3919.604, 2629.2725), (82.23863883933122, 143.5107364327347, -128.81923609717532), (0.789896, 1.201167, 1.477917), "PWM_Nordic_8x8x8_A42", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2998.6843, 4619.0864, 2627.7583), (-83.75577808219943, 176.65084737339308, 91.29077771406101), (0.789896, 1.201167, 1.477917), "PWM_Nordic_8x8x8_A43", _folder)
if a: placed += 1
else: skipped += 1

# Batch 93: StaticMesh'PWM_Quarry_1x1x1_A' (21 instances)
_mesh_path = "/Game/Unshippable/Whitebox/Rocks/Meshes/PWM_Quarry_1x1x1_A"
_materials = ['/Game/Environments/ProcTexturing/ProcMaterial_Quarry_Atlas_1']
_folder = "Reconstruction/BD_BB_Chapter5_BrokenSeal/Meshes"
a = spawn_static_mesh(_mesh_path, _materials, (5590.0, 2065.0, 2600.0), (0.0, -179.99998633961752, -0.0), (3.6258109, 3.281592, 2.21875), "PWM_Quarry_1x1x1_A_19", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3600.2954, 1018.5366, 1431.9468), (0.0, -179.99998633961752, -0.0), (1.0, 1.375, 1.0), "PWM_Quarry_1x1x1_A10_172", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1730.2754, 2267.916, 2600.091), (-34.428738955058606, -41.04961606229083, 166.09155495961969), (2.0625, 1.71875, 2.25), "PWM_Quarry_1x1x1_A11_654", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1500.0, 3740.0, 2570.0), (0.0, -179.99998633961752, -0.0), (2.28125, 2.28125, 2.28125), "PWM_Quarry_1x1x1_A12_694", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5831.009, 4770.0566, 878.0891), (0.0, 154.99997904505435, -0.0), (2.3354418, 2.6147084, 2.5625), "PWM_Quarry_1x1x1_A13_3", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4534.6846, 1541.2502, 2464.1829), (0.0, 90.55723161722675, -0.0), (1.875, 1.875, 2.5625), "PWM_Quarry_1x1x1_A14", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3393.9077, 771.8039, 1233.2207), (0.0, -179.99998633961752, -0.0), (1.03125, 0.90625, 0.78125), "PWM_Quarry_1x1x1_A15_89", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3503.3813, 802.4201, 1210.1809), (-0.3324278981102763, 12.56976027234748, -179.99995901939943), (1.03125, 0.90625, 0.78125), "PWM_Quarry_1x1x1_A16", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3509.6152, 5396.6226, 1220.6143), (0.0, -179.99998633961752, -0.0), (1.5172464, 1.5172464, 2.1853025), "PWM_Quarry_1x1x1_A17_107", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4890.0, 1990.0002, 989.7927), (-1.4552000437306896, 62.42578556645079, -2.784118375405369), (1.3871022, 1.0, 1.5692784), "PWM_Quarry_1x1x1_A18_18", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2462.1487, 2546.5906, 2678.7048), (0.0, -179.99998633961752, -0.0), (2.0737352, 2.0737352, 1.7390553), "PWM_Quarry_1x1x1_A19_66", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1043.9775, 3422.2349, 2315.0), (0.0, 164.99991169031665, -0.0), (1.53125, 1.59375, 1.40625), "PWM_Quarry_1x1x1_A2_182", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2884.9265, 5561.0547, 1196.5076), (0.0, 0.0, -0.0), (1.2817556, 0.9875704, 0.8558347), "PWM_Quarry_1x1x1_A20_19", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5876.666, 4406.281, 798.1159), (0.0, 156.46268225908332, -0.0), (2.335442, 2.9560695, 2.5625), "PWM_Quarry_1x1x1_A21", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3725.8472, 1008.0281, 1141.2991), (1.3999985667882193e-05, -68.4577592253618, 179.99939211311832), (1.316437, 1.252725, 2.273713), "PWM_Quarry_1x1x1_A22", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1090.4526, 3228.6106, 2305.0), (0.0, -15.000152484550428, 0.0), (1.53125, 2.0625, 1.40625), "PWM_Quarry_1x1x1_A3", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2855.7021, 799.5153, 914.1244), (0.0, -179.99998633961752, -0.0), (1.0, 1.3507721, 1.8622751), "PWM_Quarry_1x1x1_A4_154", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2911.7002, 5149.186, 873.52246), (0.0, -179.99998633961752, -0.0), (1.3125, 1.59375, 1.5), "PWM_Quarry_1x1x1_A5_259", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3591.8145, 717.6011, 1168.8096), (0.0, 164.99991169031665, -0.0), (0.72330123, 2.4197102, 1.0), "PWM_Quarry_1x1x1_A7_162", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3603.544, 996.1284, 1041.5513), (0.0, -179.99998633961752, -0.0), (1.0, 1.4550595, 2.2109125), "PWM_Quarry_1x1x1_A8_168", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3725.8452, 1008.02734, 1341.2991), (1.366035459896919e-05, -68.45775922535996, 179.99939211309905), (1.3164365, 1.252725, 1.6737264), "PWM_Quarry_1x1x1_A9", _folder)
if a: placed += 1
else: skipped += 1

# Batch 94: StaticMesh'PWM_Quarry_1X1x1_C' (101 instances)
_mesh_path = "/Game/Unshippable/Whitebox/Rocks/Meshes/PWM_Quarry_1X1x1_C"
_materials = ['/Game/Environments/ProcTexturing/ProcMaterial_Quarry_Atlas_1']
_folder = "Reconstruction/BD_BB_Chapter5_BrokenSeal/Meshes"
a = spawn_static_mesh(_mesh_path, _materials, (1167.8458, 564.82025, 1567.6158), (4.276149543328673, -49.731689329766986, 101.95602075464996), (2.9696288, 2.9696288, 2.9696288), "PWM_Quarry_1X1x1_C_536", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3386.6763, 1212.5796, 806.88904), (13.1720877569299, 19.371156242831905, -93.16318987618878), (1.236357, 1.4293135, 1.3220843), "PWM_Quarry_1X1x1_C10_165", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4531.466, 476.84216, 2577.7407), (-0.28430565881061154, -98.50969879584001, 96.60581320321482), (2.600545, 2.600545, 2.600545), "PWM_Quarry_1X1x1_C100", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4921.938, 1782.9674, 1118.0769), (3.928924291161776, -60.71087400747948, -92.81521691577505), (1.0, 1.0, 1.0), "PWM_Quarry_1X1x1_C101", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3417.5508, 1318.2212, 905.68756), (13.1720877569299, 19.371156242831905, -93.16318987618878), (1.236357, 1.5792714, 1.322084), "PWM_Quarry_1X1x1_C11", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3075.172, 512.17725, 1219.4443), (0.0, -179.99998633961752, -0.0), (1.15625, 1.34375, 0.6875), "PWM_Quarry_1X1x1_C12_46", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3214.4263, 122.24707, 1200.0), (0.0, -179.99998633961752, -0.0), (1.34375, 1.34375, 1.34375), "PWM_Quarry_1X1x1_C13_62", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3081.3506, 108.788574, 1205.2075), (12.484981782663239, 167.91844099623398, 158.4699158786011), (1.65625, 1.53125, 1.34375), "PWM_Quarry_1X1x1_C14", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3596.5688, 783.22363, 1037.7231), (-13.553676023690794, 167.75661620777552, 1.789876410712863e-06), (1.125, 1.75, 1.40625), "PWM_Quarry_1X1x1_C15_79", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3182.5205, 5848.4766, 1232.0049), (0.0, -179.99998633961752, -0.0), (2.25, 1.6875, 1.6875), "PWM_Quarry_1X1x1_C16_106", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3113.2585, 5526.0933, 1326.6484), (0.0, -179.99998633961752, -0.0), (1.96875, 0.71875, 0.8802837), "PWM_Quarry_1X1x1_C17_116", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3501.7202, 5455.697, 815.3406), (0.0, 134.16250593997015, -0.0), (2.074752, 2.074752, 2.3960335), "PWM_Quarry_1X1x1_C18_113", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2943.0518, 1276.294, 796.6426), (0.0, -179.99998633961752, -0.0), (1.2690226, 1.2690226, 1.2690226), "PWM_Quarry_1X1x1_C19_172", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2320.9414, 4648.2734, 936.3347), (0.0, -179.99998633961752, -0.0), (0.49885342, 0.49885342, 0.49885342), "PWM_Quarry_1X1x1_C2_53", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (919.64307, 3540.812, 1414.4001), (0.0, 147.21633701553492, -0.0), (1.0, 1.0, 1.0), "PWM_Quarry_1X1x1_C20_252", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (932.2993, 2793.7568, 1404.7261), (-18.1344850033411, 9.155271882611844e-05, -179.9999863396161), (1.0, 0.8515656, 0.7019382), "PWM_Quarry_1X1x1_C21", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (942.92773, 2816.0425, 1437.1743), (-18.133818624294655, 6.0727203176551473e-05, -77.34832874257887), (0.74697685, 0.5985428, 0.7282926), "PWM_Quarry_1X1x1_C22", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3428.1753, 5120.896, 847.304), (-1.258700784380156, 48.44463743310298, -90.09442066452078), (1.5575213, 2.0980232, 1.2583169), "PWM_Quarry_1X1x1_C23", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (960.001, 2882.2568, 1388.1621), (0.0, -90.60015093456731, 0.0), (1.40625, 1.46875, 1.125), "PWM_Quarry_1X1x1_C24_259", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4907.7207, 1971.9192, 2184.928), (30.000018897182187, -179.99995901886308, 4.102202357909023e-07), (1.6875, 1.6875, 1.6875), "PWM_Quarry_1X1x1_C25_427", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5031.0034, 1991.2449, 2243.8567), (18.747193126133613, 126.00554072392862, -78.85766023150343), (1.6875, 2.75, 1.6875), "PWM_Quarry_1X1x1_C26", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5079.916, 1953.4397, 2282.605), (21.705397663955285, 94.13478563563243, -90.13675445962852), (2.40625, 3.34375, 1.6875), "PWM_Quarry_1X1x1_C27", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5093.0303, 1967.1531, 2437.409), (-2.4976528748748175, -130.0940927599954, -85.66659573515736), (1.75, 2.21875, 3.65625), "PWM_Quarry_1X1x1_C28_435", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1390.0, 3473.5044, 2349.9026), (2.871588373500086e-13, -179.99998633961602, -59.28004708454275), (1.5080034, 2.0080032, 2.0392532), "PWM_Quarry_1X1x1_C29", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5072.113, 2045.8665, 1100.0), (-3.429902969461783e-13, -179.99998633961954, -85.00004497912211), (1.0, 1.0, 1.0), "PWM_Quarry_1X1x1_C3_24", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1350.5093, 2796.1611, 2349.9026), (6.960353942851505e-06, -10.501738453821341, -59.278347617812486), (1.508003, 2.008003, 2.5364153), "PWM_Quarry_1X1x1_C30", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3986.1719, 3870.8027, 2622.622), (0.0, -149.9999007336502, 0.0), (2.1318154, 1.6993597, 1.2491335), "PWM_Quarry_1X1x1_C31_48", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2503.2092, 3889.312, 2722.2795), (0.0, -129.99994346725336, 0.0), (2.981113, 2.981113, 2.981113), "PWM_Quarry_1X1x1_C32_63", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2895.0005, 195.0, 2470.0), (9.017641790343101e-13, -179.9999863396181, -80.43691259841198), (2.125, 1.46875, 1.0), "PWM_Quarry_1X1x1_C33_43", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3131.5156, 698.5917, 1230.4766), (0.0, 0.0, -0.0), (1.0, 1.0, 1.0), "PWM_Quarry_1X1x1_C34_5", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2932.377, 535.12805, 1220.3079), (0.0, 0.0, -0.0), (1.0, 1.0, 1.0), "PWM_Quarry_1X1x1_C35_8", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (101.615845, 869.6878, 1615.9072), (0.0, 0.0, -0.0), (1.5008581, 1.5008581, 1.7117825), "PWM_Quarry_1X1x1_C36_11", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3286.0244, -5.0789185, 1176.828), (0.0, 0.0, -0.0), (1.0, 1.0, 1.0), "PWM_Quarry_1X1x1_C37_14", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1945.0, 5905.0, 970.0), (-1.0109555068089198, -21.641571289910903, -97.21582268719372), (2.3125, 2.3125, 2.3125), "PWM_Quarry_1X1x1_C38_294", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4153.2515, 3211.0786, 2888.6917), (-10.281707467691954, 68.93173409502732, 89.98562994340254), (5.316176, 3.034287, 3.305658), "PWM_Quarry_1X1x1_C39", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4654.425, 5780.6543, 1400.8059), (0.0, -179.99998633961752, -0.0), (1.1623454, 1.1623454, 1.1623454), "PWM_Quarry_1X1x1_C4_105", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1841.5242, 5873.545, 962.95996), (3.6724997095736986, 136.15909354191015, -83.70266362845793), (2.3125, 2.3125, 2.3125), "PWM_Quarry_1X1x1_C40", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4999.1943, 2010.1599, 1045.8533), (0.0, 0.0, -95.00964523553186), (1.4750608, 1.4750608, 1.4750608), "PWM_Quarry_1X1x1_C41_512", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5200.569, 2013.5895, 898.0144), (-2.7034119524327485e-14, -179.99998633961704, -87.81737381533547), (1.4593523, 1.4593523, 1.4593523), "PWM_Quarry_1X1x1_C42", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5139.774, 1908.5057, 976.07465), (-0.615052317378537, -16.37081759928053, -92.09349863930122), (1.459352, 2.0877528, 1.459352), "PWM_Quarry_1X1x1_C43", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4870.3022, 1782.9674, 1160.2157), (-6.1987316159941255, -35.85473053289745, -98.49822887106151), (1.0, 1.0, 1.0), "PWM_Quarry_1X1x1_C44_517", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (956.19135, 3735.4226, 1065.6458), (0.5248257156848938, 143.0170880060434, -82.88921670119973), (1.9484218, 1.9484218, 1.9484218), "PWM_Quarry_1X1x1_C45", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (993.701, 3683.1553, 1218.898), (0.5248257156848938, 143.0170880060434, -82.88921670119973), (1.948422, 1.948422, 1.948422), "PWM_Quarry_1X1x1_C46", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (983.0958, 3617.1135, 1306.975), (-1.2752984042716833, 157.46920218519688, -82.98406297202376), (1.948422, 1.948422, 1.948422), "PWM_Quarry_1X1x1_C47", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1375.8181, 5800.249, 1385.5764), (0.12081386616210221, 166.89488425174932, 90.51938194127415), (1.3849206, 1.3849206, 1.3849206), "PWM_Quarry_1X1x1_C48_606", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1263.0419, 5858.416, 1386.1173), (0.36100545792593314, 137.37743053541038, 90.39241009258136), (1.9024836, 1.9425766, 1.5970758), "PWM_Quarry_1X1x1_C49", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2057.1082, 4957.122, 941.1154), (12.568832493218848, -152.69974596714255, -22.860718882096624), (0.498853, 0.498853, 0.498853), "PWM_Quarry_1X1x1_C5", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1096.6761, 5821.981, 1653.7437), (2.673137557521252, -31.498531077849805, 40.5637761534601), (1.902484, 1.942577, 1.597076), "PWM_Quarry_1X1x1_C50", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (537.59674, 4966.6206, 925.34564), (3.195789921080341, 32.430886089674935, -95.01434638330899), (2.5514452, 2.5514452, 2.5514452), "PWM_Quarry_1X1x1_C51_615", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (704.8061, 4882.6953, 2446.4668), (-13.378663931261801, -49.62490363658363, 78.86886087118016), (3.5180693, 3.5180693, 3.5180693), "PWM_Quarry_1X1x1_C52_618", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1013.5753, 5096.688, 2513.2773), (-17.109343414310022, -80.38889031222519, 87.14767887339966), (3.518069, 3.518069, 3.518069), "PWM_Quarry_1X1x1_C53", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1970.6598, 5866.641, 2476.8572), (-17.109282957962122, -80.38863866005303, 94.76358281142032), (3.518069, 3.518069, 3.518069), "PWM_Quarry_1X1x1_C54", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2293.9338, 6024.8315, 2478.1543), (-17.109282957962122, -80.38863866005303, 94.76358281142032), (3.518069, 3.518069, 3.518069), "PWM_Quarry_1X1x1_C55", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2524.0498, 6034.874, 2570.81), (-17.109282957962122, -80.38863866005303, 94.76358281142032), (3.518069, 3.518069, 3.518069), "PWM_Quarry_1X1x1_C56", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3009.2205, 6184.32, 2729.662), (-36.5030757630515, -99.45113232164879, 106.19013451939523), (3.9013262, 3.3423865, 4.7539062), "PWM_Quarry_1X1x1_C57", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4952.6885, 5524.7837, 2496.989), (-6.819641069498921, -155.35638979696876, 103.39731577118091), (3.901326, 3.342386, 4.753906), "PWM_Quarry_1X1x1_C58", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4672.2676, 4804.2666, 2656.2705), (-6.819641069498921, -155.35638979696876, 103.39731577118091), (3.901326, 3.342386, 4.753906), "PWM_Quarry_1X1x1_C59", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2570.0, 1852.7997, 2658.171), (0.0, -179.99998633961752, -0.0), (3.1877255, 3.3987556, 2.84375), "PWM_Quarry_1X1x1_C6_666", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5986.5303, 3845.556, 1864.3418), (2.7769836778178996, 116.18607384257369, 91.36486574304229), (2.1178467, 2.1178467, 2.1178467), "PWM_Quarry_1X1x1_C60_628", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5993.8564, 3994.0154, 1867.116), (4.909992346638444, 67.48211588137681, 95.17391999146689), (2.117847, 2.117847, 2.117847), "PWM_Quarry_1X1x1_C61", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5699.1855, 4721.727, 2068.769), (4.909992346638444, 67.48211588137681, 95.17391999146689), (2.117847, 2.117847, 2.117847), "PWM_Quarry_1X1x1_C62", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5928.584, 2459.7012, 2193.9607), (6.999457036244645, 9.905395729501258, 88.64751710386184), (2.117847, 2.5075834, 2.117847), "PWM_Quarry_1X1x1_C63", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5773.0933, 1383.7701, 892.4684), (4.769728060723494, 124.5066467858502, -97.21080213178999), (2.5825357, 2.9722717, 2.5825357), "PWM_Quarry_1X1x1_C64", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5988.0054, 2494.7764, 1984.4808), (1.3192508705332058, 124.0090302810574, 98.1879484244238), (2.582536, 2.972272, 2.582536), "PWM_Quarry_1X1x1_C65", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (6028.208, 2103.919, 1949.8337), (1.3192508705332058, 124.0090302810574, 98.1879484244238), (2.582536, 2.972272, 2.582536), "PWM_Quarry_1X1x1_C66", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5584.138, 1400.402, 2169.7173), (1.3192508705332058, 124.0090302810574, 98.1879484244238), (2.582536, 2.972272, 2.582536), "PWM_Quarry_1X1x1_C67", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5365.9688, 1471.8674, 2321.4475), (2.7069969828140996, 83.35533677699398, 107.17241391098844), (2.582536, 2.4839685, 2.582536), "PWM_Quarry_1X1x1_C68", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5386.0327, 1244.9724, 2281.465), (9.27507228329107, 85.40828338779315, 107.38713654388943), (2.582536, 2.6135447, 2.582536), "PWM_Quarry_1X1x1_C69", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1390.0, 3705.0, 2349.9026), (-2.68685121439387e-13, -179.9999590188611, 30.00013657763609), (1.8125, 2.3125, 2.34375), "PWM_Quarry_1X1x1_C7_697", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5025.4785, 1736.8724, 2227.6416), (-24.46322754357641, -170.23717815946733, 99.47372690930018), (2.582536, 2.613545, 2.582536), "PWM_Quarry_1X1x1_C70", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4837.303, 877.21576, 2456.6438), (-5.649841923360499, 84.72085980846259, 112.07352836631054), (2.582536, 2.9925013, 2.582536), "PWM_Quarry_1X1x1_C71", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2801.955, 211.23299, 2573.9543), (-5.649841923360499, 84.72085980846259, 112.07352836631054), (2.582536, 2.992501, 2.582536), "PWM_Quarry_1X1x1_C72", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2476.1377, 436.77203, 2618.4578), (-5.347594989207573, 22.73808094836132, 116.18674066229633), (2.582536, 2.992501, 2.582536), "PWM_Quarry_1X1x1_C73", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (689.60046, 1505.9827, 2428.6038), (-5.347596727370189, 22.73777488937783, 101.84491258438739), (2.582536, 2.992501, 2.582536), "PWM_Quarry_1X1x1_C74", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (738.6893, 1811.9644, 2538.3013), (-33.28832994964788, -25.700620565234527, 123.20150169643556), (3.465159, 3.8751242, 3.465159), "PWM_Quarry_1X1x1_C75", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1608.6807, 5572.3403, 2369.4722), (-3.697508671975151, -82.08966761588884, 89.4865686004674), (2.6872468, 2.6872468, 2.6872468), "PWM_Quarry_1X1x1_C76_650", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (556.72864, 5993.7637, 1516.5808), (-3.6791333004001285, -99.74267638652593, 90.63122780743537), (2.687247, 2.687247, 2.924851), "PWM_Quarry_1X1x1_C77", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2827.3352, 5180.716, 2349.073), (-0.05136202503018386, -83.09854273857069, 89.99365694408823), (2.5479872, 2.5479872, 2.5479872), "PWM_Quarry_1X1x1_C78_654", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2982.0396, 6225.1636, 2632.3064), (-10.702481044874194, -100.39533013067295, 83.66569345086212), (3.901326, 3.342386, 4.753906), "PWM_Quarry_1X1x1_C79", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4109.9995, 5820.0, 2700.0), (-3.9563012608247704e-15, -179.9999863396171, -15.000087146814387), (1.96875, 1.96875, 1.96875), "PWM_Quarry_1X1x1_C8_79", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3430.0076, 6198.1934, 2583.7742), (-12.180235764848032, -108.1782725288449, 90.35197998516558), (3.901326, 3.342386, 5.686159), "PWM_Quarry_1X1x1_C80", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (908.90436, 3591.4429, 1301.6179), (0.39523266255666856, 142.49725850152566, -78.92785074795678), (1.948422, 1.7148181, 1.948422), "PWM_Quarry_1X1x1_C81", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3561.4705, 889.9447, 886.28326), (-4.0758067312058825, -43.14874169882789, -85.38552619055645), (1.236357, 1.429314, 1.322084), "PWM_Quarry_1X1x1_C82", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3481.412, 5252.18, 847.304), (-1.258482343669659, -93.57286374190626, -90.0939322525197), (1.9004719, 2.098023, 1.258317), "PWM_Quarry_1X1x1_C83", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2914.8777, 5429.2515, 1227.186), (-13.40832464051699, -10.531708405770768, 84.90084706162523), (1.493396, 1.493396, 1.493396), "PWM_Quarry_1X1x1_C84_190", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2943.9104, 5254.7173, 1227.186), (-13.408234388088074, -13.17505041022291, 84.90087131783092), (1.493396, 1.493396, 1.9129295), "PWM_Quarry_1X1x1_C85", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4065.8318, 2280.3042, 2781.3557), (0.0, 0.0, 96.25025345979623), (2.6941276, 2.6941276, 2.6941276), "PWM_Quarry_1X1x1_C86_204", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4065.8318, 2081.4358, 2781.3555), (0.0, 0.0, 96.25025345979623), (4.211707, 4.211707, 4.211707), "PWM_Quarry_1X1x1_C87", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4165.049, 1778.5728, 2778.5884), (3.83393562892668e-06, -62.170033333501394, 96.25030711983922), (4.211707, 4.211707, 4.211707), "PWM_Quarry_1X1x1_C88", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3857.9675, 1717.8387, 2781.3555), (3.83393562892668e-06, -62.170033333501394, 96.25030711983922), (4.594379, 4.211707, 4.9199195), "PWM_Quarry_1X1x1_C89", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4750.2515, 540.66455, 2233.0535), (-43.35779172088158, 5.92034987732023, 117.13627599092496), (1.9375, 1.9375, 1.9375), "PWM_Quarry_1X1x1_C9_8", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3573.2458, 1377.158, 2707.766), (3.83393562892668e-06, -62.170033333501394, 96.25030711983922), (4.594379, 4.211707, 4.919919), "PWM_Quarry_1X1x1_C90", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3679.4146, 2117.9048, 2759.663), (3.83393562892668e-06, -62.170033333501394, 96.25030711983922), (4.211707, 4.211707, 4.211707), "PWM_Quarry_1X1x1_C91", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3415.8572, 2117.9048, 2759.663), (2.4883332455079802e-06, 65.76797417011515, 96.25035590759332), (4.211707, 4.211707, 4.211707), "PWM_Quarry_1X1x1_C92", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3659.9438, 2530.0068, 2759.663), (2.4883332455079802e-06, 65.76797417011515, 96.25035590759332), (6.9677863, 3.089826, 7.816419), "PWM_Quarry_1X1x1_C93", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3659.9438, 2050.1863, 2759.663), (2.4883332455079802e-06, 65.76797417011515, 96.25035590759332), (6.967786, 3.089826, 7.816419), "PWM_Quarry_1X1x1_C94", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4419.2915, 2173.8748, 2759.663), (19.58952530779401, 64.17368082923174, 87.03314464667423), (6.967786, 3.089826, 7.816419), "PWM_Quarry_1X1x1_C95", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2011.277, 3473.0884, 2428.2036), (1.1608268047883163e-05, -52.51381985118478, 83.55481407660834), (3.5641985, 2.2281394, 3.5641985), "PWM_Quarry_1X1x1_C96_219", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2011.277, 3767.8416, 2532.1023), (1.1608268047883163e-05, -52.51381985118478, 83.55481407660834), (3.564198, 2.228139, 3.564198), "PWM_Quarry_1X1x1_C97", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4300.829, 403.70422, 2577.7407), (0.0, 0.0, 98.50497077393952), (2.6005454, 2.6005454, 2.6005454), "PWM_Quarry_1X1x1_C98_223", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4128.7407, 336.28827, 2577.7407), (-0.28430565881061154, -98.50969879584001, 96.60581320321482), (2.600545, 2.600545, 2.600545), "PWM_Quarry_1X1x1_C99", _folder)
if a: placed += 1
else: skipped += 1

# Batch 95: StaticMesh'PWM_Quarry_2x2x2_A' (50 instances)
_mesh_path = "/Game/Unshippable/Whitebox/Rocks/Meshes/PWM_Quarry_2x2x2_A"
_materials = ['/Game/Environments/ProcTexturing/ProcMaterial_Quarry_Atlas_1']
_folder = "Reconstruction/BD_BB_Chapter5_BrokenSeal/Meshes"
a = spawn_static_mesh(_mesh_path, _materials, (2798.9773, 5680.497, 956.3916), (0.0, -179.99998633961752, -0.0), (1.0, 1.5150788, 2.1221113), "PWM_Quarry_2x2x2_A_99", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3544.6611, 5338.5156, 1012.62573), (-2.271636541492212, 172.38490146529125, 6.748522889780893), (0.36317775, 1.28125, 1.0), "PWM_Quarry_2x2x2_A10", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3572.226, 465.6504, 1176.5354), (14.99985443394368, -10.000183033076588, -6.111619352411201e-05), (0.682606, 1.471106, 0.680199), "PWM_Quarry_2x2x2_A11", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3602.5776, 1053.9575, 800.23706), (0.0, -74.99990873202879, 0.0), (1.2603288, 1.0, 1.0), "PWM_Quarry_2x2x2_A12_165", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5390.0, 4530.0, 2690.0), (0.0, 4.99995437743562, -0.0), (1.625, 1.71875, 1.0), "PWM_Quarry_2x2x2_A13", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3778.6133, 4906.1235, 2756.5623), (65.3762333314952, 156.58624258325042, -24.53097086234073), (1.9375, 1.90625, 2.6574125), "PWM_Quarry_2x2x2_A14_82", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3765.8481, 5265.4077, 2617.3481), (19.92038883762693, 91.81689418213156, -84.68062719460374), (2.09375, 1.90625, 1.96875), "PWM_Quarry_2x2x2_A15", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2580.2263, 2361.7842, 2823.1758), (-0.0019531247854335427, 155.0002081562549, 179.99598384855537), (3.617314, 3.8497112, 2.4920907), "PWM_Quarry_2x2x2_A16_663", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (6035.1323, 1927.4689, 884.2429), (2.412258609722693, 30.847997906138993, 1.9478647230874446), (1.65625, 1.65625, 1.65625), "PWM_Quarry_2x2x2_A17", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (6174.7827, 1901.3689, 1428.9736), (2.6391166282825127, -44.46512152929098, 176.4311954987089), (2.15625, 2.9035156, 2.15625), "PWM_Quarry_2x2x2_A18", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (6126.7583, 1876.6042, 1867.1995), (2.5647236886743388, 85.67765589642212, -178.61373833690513), (2.15625, 2.15625, 2.15625), "PWM_Quarry_2x2x2_A19", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5260.0, 1660.0002, 2480.0), (0.0, -179.99998633961752, -0.0), (1.5, 1.78125, 1.0), "PWM_Quarry_2x2x2_A2_36", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4032.3042, 1223.2222, 2660.801), (-10.79287735243707, 82.22829501322508, -163.35669523609943), (1.53125, 2.071208, 2.071208), "PWM_Quarry_2x2x2_A20", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3758.794, 5724.926, 2808.4072), (69.40875582500993, -166.53091881946918, -75.64766761045396), (1.53125, 1.53125, 2.25), "PWM_Quarry_2x2x2_A21_92", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2283.4722, 5069.3184, 2477.5908), (-74.99926609827934, -179.99978878838513, 15.000313440748622), (1.59375, 1.59375, 1.625), "PWM_Quarry_2x2x2_A22_107", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1930.0, 5910.0, 2420.0), (0.0, -179.99998633961752, -0.0), (1.0, 1.0, 1.1875), "PWM_Quarry_2x2x2_A23_110", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2156.6416, 5946.644, 2418.5054), (1.0986426312157581e-08, 5.000091551166266, 175.00010799202045), (1.34375, 0.78125, 1.5625), "PWM_Quarry_2x2x2_A24", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1328.0186, 5803.494, 1886.0615), (2.916004188130295, 152.29662366793715, 3.8677773301261342), (1.65625, 1.65625, 1.65625), "PWM_Quarry_2x2x2_A25", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1141.0078, 5625.866, 1988.4736), (9.19936115526755, 110.93318429391984, -177.1435572762596), (1.46875, 2.75, 2.15625), "PWM_Quarry_2x2x2_A26", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (855.5654, 5342.968, 2797.1816), (-1.2150574634582147, -164.39002247928929, -173.2681539651239), (2.15625, 2.15625, 2.15625), "PWM_Quarry_2x2x2_A27", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (567.27783, 3600.352, 2635.326), (64.53590249794952, -79.41159354446006, 101.6976123166374), (1.90625, 1.90625, 2.84375), "PWM_Quarry_2x2x2_A28_130", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (210.0, 3479.9995, 2420.0), (0.0, -179.99998633961752, -0.0), (1.0, 1.0, 1.0), "PWM_Quarry_2x2x2_A29_140", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5070.0, 4160.0, 2730.0), (0.0, -179.99998633961752, -0.0), (1.625, 1.71875, 1.0), "PWM_Quarry_2x2x2_A3_48", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (210.0, 3219.9995, 2490.0), (0.0, -109.99977172843964, 0.0), (1.59375, 1.0, 1.5), "PWM_Quarry_2x2x2_A30", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (397.6721, 3195.3738, 2625.1917), (19.291012064542077, -115.38034231321362, 74.08365429438075), (2.59375, 1.5238899, 1.7532501), "PWM_Quarry_2x2x2_A31", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1678.2646, 5653.279, 780.374), (0.0, 155.58591657908119, -0.0), (1.0, 1.0, 1.0), "PWM_Quarry_2x2x2_A32_45", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2725.9922, 970.1914, 844.7471), (0.0, -144.99985487380692, 0.0), (1.0, 1.0, 1.0), "PWM_Quarry_2x2x2_A33", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3048.947, 286.49414, 1217.1265), (0.0, -179.99998633961752, -0.0), (0.9375, 1.0, 0.46875), "PWM_Quarry_2x2x2_A34_43", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3342.47, 214.76514, 1207.9917), (3.3651339950134833, -98.86230578251036, -91.82739855148496), (1.0, 0.6386703, 0.875), "PWM_Quarry_2x2x2_A35_59", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3674.5054, 813.8198, 888.78613), (0.0, -179.99998633961752, -0.0), (1.09375, 1.15625, 1.0), "PWM_Quarry_2x2x2_A36_76", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2987.0168, 802.1909, 1286.085), (8.024672537901335, -0.2545471558710614, 178.1775402461585), (1.0, 1.2955297, 0.52493477), "PWM_Quarry_2x2x2_A37_85", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2497.9563, 6098.1787, 2454.2068), (-10.178036118837886, -148.58043015904352, -175.47955583999928), (1.34375, 0.78125, 1.5625), "PWM_Quarry_2x2x2_A39", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5781.163, 4957.167, 813.9585), (0.0, -149.41090352872948, 0.0), (1.0, 1.0, 1.0), "PWM_Quarry_2x2x2_A4_141", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5080.0, 1998.4813, 950.0), (0.0, -173.65029510004155, 0.0), (1.0, 1.0, 1.0), "PWM_Quarry_2x2x2_A40_2", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5389.236, 5338.119, 2493.9177), (0.0, -39.99993584456101, 0.0), (1.0, 1.0, 0.75), "PWM_Quarry_2x2x2_A41_108", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5265.397, 5445.7295, 2475.6238), (0.0, 125.00002095232185, -0.0), (1.0, 1.0, 0.625), "PWM_Quarry_2x2x2_A42", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5515.615, 5192.757, 2475.6238), (0.0, 154.99997904505435, -0.0), (1.0, 1.0, 0.75), "PWM_Quarry_2x2x2_A43", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5155.6816, 5534.0967, 2493.9177), (0.0, -39.99993584456101, 0.0), (1.0, 1.0, 0.75), "PWM_Quarry_2x2x2_A44", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5030.071, 5639.4863, 2472.5723), (5.00000801725472, 140.00081417678513, 2.1315189963301567e-05), (1.0, 1.0, 0.75), "PWM_Quarry_2x2x2_A45", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (531.10156, 1824.1328, 2440.927), (0.0, -144.99988024512786, 0.0), (1.0, 1.0, 1.0), "PWM_Quarry_2x2x2_A46_115", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (265.76172, 2483.7402, 2492.329), (0.0, 105.0003194987811, -0.0), (1.0, 1.0, 1.0), "PWM_Quarry_2x2x2_A47_118", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (6088.455, 1858.0599, 1087.3517), (2.724047216793744, 20.44697837971416, 1.4804825178531158), (1.65625, 1.65625, 3.104197), "PWM_Quarry_2x2x2_A48", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5907.105, 2539.659, 872.71), (1.4505203638045496, 54.03350845883021, 2.740112052840115), (1.1915263, 1.65625, 1.65625), "PWM_Quarry_2x2x2_A49", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2868.1953, 1069.7583, 844.7471), (0.0, -144.99985487380692, 0.0), (1.0, 1.0, 1.0), "PWM_Quarry_2x2x2_A5_151", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (6106.3965, 2215.7795, 869.9404), (6.7923874206955, 163.09562817478033, -7.597685808846396), (1.191526, 1.65625, 1.65625), "PWM_Quarry_2x2x2_A50", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (6053.61, 2270.614, 859.95966), (2.6951308935744978, 21.545367075063922, 1.5324202038376211), (1.191526, 1.65625, 1.65625), "PWM_Quarry_2x2x2_A51", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3491.0078, 136.14062, 1170.4355), (-14.999787462719073, 169.99990221083735, 1.21562078987449e-05), (0.6826062, 1.4711062, 0.6801987), "PWM_Quarry_2x2x2_A6_158", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3659.9995, 5720.0, 860.0), (0.0, -179.99998633961752, -0.0), (1.0, 1.28125, 1.0), "PWM_Quarry_2x2x2_A7_5", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3660.0005, 5720.0, 1050.0), (-0.0006103514431808098, 6.866453816255017e-05, -179.99998633961656), (1.0, 1.7310413, 1.0), "PWM_Quarry_2x2x2_A8", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3614.2559, 5335.2783, 847.02905), (-1.698891016958527e-08, 153.8650059520007, 7.118722779763823), (1.0, 1.28125, 1.0), "PWM_Quarry_2x2x2_A9", _folder)
if a: placed += 1
else: skipped += 1

# Batch 96: StaticMesh'PWM_Quarry_2x2x5_A' (54 instances)
_mesh_path = "/Game/Unshippable/Whitebox/Rocks/Meshes/PWM_Quarry_2x2x5_A"
_materials = ['/Game/Environments/ProcTexturing/ProcMaterial_Quarry_Atlas_2']
_folder = "Reconstruction/BD_BB_Chapter5_BrokenSeal/Meshes"
a = spawn_static_mesh(_mesh_path, _materials, (1461.1436, 6056.6543, 1230.0), (0.0, 45.461967552829485, -0.0), (2.21875, 2.8504987, 2.8504987), "PWM_Quarry_2x2x5_A_310", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (289.75684, 5085.5, 1100.0), (0.0, 149.95477168336336, -0.0), (2.850499, 2.850499, 2.850499), "PWM_Quarry_2x2x5_A10", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (6065.1772, 4311.53, 1494.1246), (-3.8800033842326846, 145.0419310839635, 5.163074559256353), (2.3272457, 2.6256545, 2.3272457), "PWM_Quarry_2x2x5_A11_618", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5328.1235, 4237.1016, 2656.607), (-59.58102129179971, 165.37340108469252, 6.473446881571766), (3.625, 2.375, 2.15625), "PWM_Quarry_2x2x5_A12", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (479.63818, 1486.6055, 1185.0), (0.0, 113.50405865507155, -0.0), (1.5625, 2.0704322, 2.2202387), "PWM_Quarry_2x2x5_A13_376", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5412.1855, 3782.8296, 2779.7249), (-65.0564826379491, 150.5056391092391, 32.7479819094849), (4.6798563, 2.375, 2.15625), "PWM_Quarry_2x2x5_A14_42", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5120.0, 2170.0, 2760.0), (-9.155271987169911e-05, -134.9995256506266, -179.99995901886058), (3.96875, 2.4375, 2.03125), "PWM_Quarry_2x2x5_A15", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1071.6982, 2888.5874, 2586.506), (0.0, 170.3923449459674, -0.0), (2.375, 2.09375, 1.639091), "PWM_Quarry_2x2x5_A16", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (6125.225, 2238.688, 1524.0374), (-5.21823135129904, -173.76043560970243, 176.88998999390623), (1.572146, 1.572146, 1.572146), "PWM_Quarry_2x2x5_A17", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (6125.225, 3978.688, 1664.0374), (-5.21823135129904, -173.76043560970243, 176.88998999390623), (1.572146, 1.572146, 1.572146), "PWM_Quarry_2x2x5_A18", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4599.863, 5419.189, 2798.4912), (4.091153122482574, 95.23047331100048, 79.19552494380402), (3.625, 2.375, 2.15625), "PWM_Quarry_2x2x5_A19", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1473.1818, 421.65674, 1033.0603), (0.0, -124.99880042650526, 0.0), (2.21875, 2.21875, 2.375), "PWM_Quarry_2x2x5_A2_48", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4009.838, 5076.2563, 2896.3213), (-25.346889451023888, 101.18439374293868, 78.05841568076887), (3.625, 2.375, 2.375), "PWM_Quarry_2x2x5_A20", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5070.2676, 5603.1587, 2513.3267), (-18.74682837214511, -132.90427817133786, -21.17208982176747), (1.84375, 2.65625, 1.625), "PWM_Quarry_2x2x5_A21_65", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4330.4253, 5877.318, 2779.2202), (1.9606873835270295, 148.4160428251354, 23.82466378553502), (1.84375, 1.90625, 1.625), "PWM_Quarry_2x2x5_A22", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4145.152, 5928.574, 2783.7825), (18.525242763006403, 74.44077217924395, -5.349884561437335), (1.84375, 1.90625, 1.625), "PWM_Quarry_2x2x5_A23", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1833.1769, 415.18604, 2488.8987), (8.64946477604044, -120.38059799191602, -5.040894841575521), (1.5, 1.53125, 1.0), "PWM_Quarry_2x2x5_A24_196", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1988.9694, 373.25635, 2503.0923), (8.363133375582072, -105.215606443542, -177.78444818097321), (1.5, 1.53125, 1.0), "PWM_Quarry_2x2x5_A25", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2899.8413, 401.35938, 798.9353), (0.0, -179.99998633961752, -0.0), (1.0, 1.0, 1.0), "PWM_Quarry_2x2x5_A26_36", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2945.7996, 268.26758, 971.8262), (0.0, 23.687316875922193, -0.0), (1.0, 1.0, 1.0), "PWM_Quarry_2x2x5_A27", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3414.0757, 535.0464, 1210.8416), (-79.01480698844212, 24.086492259256513, 55.20486807847383), (1.0, 1.0, 1.0), "PWM_Quarry_2x2x5_A28_56", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2369.5015, 1369.4971, 2444.481), (-6.812346825675688, 163.62495929637228, 89.44103712126004), (1.53834, 1.53834, 1.1875), "PWM_Quarry_2x2x5_A29_198", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4280.0, 1820.0002, 2826.0898), (0.0, -179.99998633961752, -0.0), (3.21875, 2.4375, 2.03125), "PWM_Quarry_2x2x5_A3_13", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3234.2544, 415.3125, 1213.2324), (-57.994392098340924, -166.76105089800123, 75.8826883102997), (1.0, 1.0, 1.0), "PWM_Quarry_2x2x5_A30_66", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5180.0, 1950.0002, 910.0), (-0.00018310544966117548, 5.340575547901483e-05, -179.99997950942983), (1.0, 1.0, 1.0), "PWM_Quarry_2x2x5_A31_11", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1307.0359, 567.0905, 1116.2866), (0.20176375638583877, 129.5885575055757, -178.9917893760681), (1.937129, 1.937129, 1.937129), "PWM_Quarry_2x2x5_A32_522", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1361.62, 609.82306, 1642.386), (-11.893186178777933, 131.73999704320926, 172.50892680106017), (1.937129, 1.937129, 1.937129), "PWM_Quarry_2x2x5_A33", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (515.9262, 1430.9283, 1075.3297), (0.20176397106904492, 129.58855750797454, -178.9917893504773), (1.937129, 1.937129, 1.937129), "PWM_Quarry_2x2x5_A34", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1055.37, 443.27032, 1108.2782), (4.510246237455357, 164.8016223050661, -178.40155394847403), (1.937129, 1.937129, 1.937129), "PWM_Quarry_2x2x5_A35", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (929.75446, 356.77612, 1108.9283), (1.4298183054716576, 158.1334928177495, -178.04423797149127), (1.937129, 1.937129, 1.937129), "PWM_Quarry_2x2x5_A36", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (413.92987, 1267.2491, 950.0), (0.0, -110.01969417798502, 0.0), (1.8555495, 1.8555495, 1.8555495), "PWM_Quarry_2x2x5_A37_531", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3314.0295, 239.9143, 2557.5264), (-6.23513721235216, 88.1788408021407, 92.23752175363101), (2.1963048, 2.1963048, 2.1963048), "PWM_Quarry_2x2x5_A38_644", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3786.279, 5401.243, 1185.3822), (3.2308492417009154, -44.180291962681665, -176.01550233081497), (1.0, 1.0, 1.0), "PWM_Quarry_2x2x5_A39_57", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (877.5044, 4144.714, 2736.8425), (-4.844636014535795, 80.44675559177227, 99.53555691046711), (5.780712, 1.9781288, 4.131462), "PWM_Quarry_2x2x5_A4", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2905.232, 1024.13, 1062.9338), (0.0, -16.85473722440808, 0.0), (1.0, 1.0, 1.0), "PWM_Quarry_2x2x5_A40_153", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3435.4314, 1281.1791, 1000.0166), (0.0, 168.26669792692246, -0.0), (1.1900334, 1.1900334, 1.1900334), "PWM_Quarry_2x2x5_A41_156", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3512.1055, 994.4728, 996.23456), (0.0, -174.07107921405583, 0.0), (1.190033, 1.190033, 1.190033), "PWM_Quarry_2x2x5_A42", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3493.6714, 1109.8961, 1010.21893), (0.0, 18.550124380250846, -0.0), (1.190033, 1.190033, 1.190033), "PWM_Quarry_2x2x5_A43", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3472.1855, 1233.6583, 1010.21893), (0.0, 7.520095619174702, -0.0), (1.190033, 1.190033, 1.190033), "PWM_Quarry_2x2x5_A44", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3178.897, 693.5821, 1244.4374), (-87.23651722850248, 122.84323206823353, -130.52212324756027), (1.0, 1.3037188, 1.2864969), "PWM_Quarry_2x2x5_A45_170", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3407.3672, 5111.51, 1066.8638), (0.0, 105.34276455751923, -0.0), (1.0, 1.0, 1.0), "PWM_Quarry_2x2x5_A46_177", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3514.8906, 5439.6445, 1027.0955), (0.0, 103.73455654840895, -0.0), (1.9152236, 1.4953355, 1.2346748), "PWM_Quarry_2x2x5_A47", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3514.8906, 5226.7007, 1027.0955), (0.0, -97.48004186177647, 0.0), (1.915224, 1.495335, 1.234675), "PWM_Quarry_2x2x5_A48", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3545.6243, 5539.807, 1027.0955), (0.0, -97.48004186177647, 0.0), (1.915224, 1.495335, 1.234675), "PWM_Quarry_2x2x5_A49", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1389.1528, 2462.274, 2328.1375), (27.0520809895162, -157.13791009084974, 55.91989270888283), (2.5, 1.84375, 1.5625), "PWM_Quarry_2x2x5_A5_651", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3593.167, 5714.734, 1027.0955), (0.0, -110.47418351006375, 0.0), (1.915224, 1.495335, 1.234675), "PWM_Quarry_2x2x5_A50", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2811.067, 5342.1133, 1027.0955), (0.0, -128.5056778290868, 0.0), (1.915224, 1.495335, 1.234675), "PWM_Quarry_2x2x5_A51", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2891.5625, 5074.0864, 1027.0955), (0.0, -128.5056778290868, 0.0), (1.915224, 1.495335, 1.234675), "PWM_Quarry_2x2x5_A52", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2862.6956, 5253.104, 1027.0955), (0.0, -18.488128536911702, 0.0), (1.915224, 1.495335, 1.234675), "PWM_Quarry_2x2x5_A53", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2569.8542, 3924.947, 2542.4004), (-70.19991875046388, 93.27867234397235, -93.0847051993788), (2.750872, 2.750872, 2.750872), "PWM_Quarry_2x2x5_A55_216", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1259.9961, 2347.8516, 2485.4946), (61.61785102676285, 120.38582361232068, -153.55288535884608), (2.5, 2.59375, 1.875), "PWM_Quarry_2x2x5_A6", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5460.0, 1600.0002, 2820.0), (0.0, 74.99998993184444, -0.0), (4.5, 2.4375, 2.03125), "PWM_Quarry_2x2x5_A7", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5410.0, 1810.0002, 2790.0), (-9.155272832695435e-05, 105.00037971219223, -179.99995901885978), (3.96875, 3.71875, 2.03125), "PWM_Quarry_2x2x5_A8", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (724.5654, 6403.889, 1230.0), (0.0, 19.712751708004102, -0.0), (2.850499, 1.3630104, 2.850499), "PWM_Quarry_2x2x5_A9", _folder)
if a: placed += 1
else: skipped += 1

# Batch 97: StaticMesh'PWM_Quarry_2x2x5_B' (23 instances)
_mesh_path = "/Game/Unshippable/Whitebox/Rocks/Meshes/PWM_Quarry_2x2x5_B"
_materials = ['/Game/Environments/ProcTexturing/ProcMaterial_Quarry_Atlas_2']
_folder = "Reconstruction/BD_BB_Chapter5_BrokenSeal/Meshes"
a = spawn_static_mesh(_mesh_path, _materials, (1072.0068, 4564.5938, 2582.1226), (-78.87887518118939, -162.06481750773136, -82.33841437175666), (2.1875, 2.4375, 3.59375), "PWM_Quarry_2x2x5_B_688", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3976.137, 582.5785, 2797.728), (6.469130778197647, -64.6367435302311, -95.39531939015748), (1.9496939, 2.1875, 2.28125), "PWM_Quarry_2x2x5_B10", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1885.7563, 5798.8, 800.83093), (-13.765656359436177, -134.25417173675328, 6.686796392171767e-06), (1.611053, 1.3014388, 1.0), "PWM_Quarry_2x2x5_B11_55", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (704.53516, 5052.2236, 583.9712), (5.552588401530805, -179.99995901886493, 2.144497901262688e-07), (1.4920241, 1.9464213, 1.3733879), "PWM_Quarry_2x2x5_B12_128", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3415.109, 71.239746, 877.5925), (0.0, -179.99998633961752, -0.0), (1.0, 1.0, 1.0), "PWM_Quarry_2x2x5_B13_69", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3545.3716, 542.6626, 960.3972), (0.0, 101.69982001475316, -0.0), (1.40625, 1.25, 1.0), "PWM_Quarry_2x2x5_B14", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3421.6296, 6001.1387, 1177.6729), (-2.3306887155824439e-07, -167.46443677831266, 91.11857554545982), (1.46875, 1.0, 1.40625), "PWM_Quarry_2x2x5_B15_99", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3013.234, 6160.01, 1177.6729), (0.7439848912757936, -6.906554087873564, 97.23702769274362), (1.46875, 1.0, 2.03125), "PWM_Quarry_2x2x5_B16", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3219.0854, 5666.3296, 1224.5127), (-81.74053496878783, -176.96567531296378, 2.107560172747909e-05), (1.0, 1.8509203, 1.853966), "PWM_Quarry_2x2x5_B17_110", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5250.0, 2090.0, 800.0), (0.0, -179.99998633961752, -0.0), (1.0, 1.0, 1.0), "PWM_Quarry_2x2x5_B18_8", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4820.5176, 1770.0002, 1030.0), (0.0, -109.99988554136719, 0.0), (1.0, 1.0, 1.0), "PWM_Quarry_2x2x5_B19_21", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3641.6182, 1320.0, 2596.2166), (-24.515173509742368, 152.32377242136246, 12.278725816397596), (1.71875, 1.875, 1.625), "PWM_Quarry_2x2x5_B2_32", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4885.5825, 1887.9153, 1003.02246), (0.0, -137.63917706339993, 0.0), (1.0, 1.0, 1.0), "PWM_Quarry_2x2x5_B20_27", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (993.5493, 3489.9575, 1211.3042), (0.0, -121.44125517451212, 0.0), (1.28125, 1.0, 1.0), "PWM_Quarry_2x2x5_B21_262", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1599.8892, 2968.621, 2827.1304), (-8.563323544718948, -179.9999590188673, 6.054096916478633e-07), (4.2265983, 3.1752355, 2.1974022), "PWM_Quarry_2x2x5_B22_4", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1496.9238, 3409.144, 2750.003), (-0.00030517577159813963, 6.103515987765707e-05, -169.98096612240852), (4.348686, 4.662855, 2.1974027), "PWM_Quarry_2x2x5_B23", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (131.35889, 4162.7285, 2323.3772), (31.321332703972846, 163.51534472385057, -24.650660751408136), (2.03125, 2.03125, 2.03125), "PWM_Quarry_2x2x5_B3_133", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (170.35791, 3983.6602, 2303.4695), (18.570020085195477, 106.35092591960517, -25.008512812676262), (2.03125, 2.03125, 2.03125), "PWM_Quarry_2x2x5_B4", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (610.0, 1440.0, 1970.0), (0.0, -179.99998633961752, -0.0), (1.5, 1.25, 1.25), "PWM_Quarry_2x2x5_B5_171", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5275.0, 995.0005, 2705.0), (0.0, -179.99998633961752, -0.0), (1.65625, 1.65625, 1.65625), "PWM_Quarry_2x2x5_B6_3", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5126.0503, 836.4219, 2624.6602), (-3.8273616494113294, 40.108056375198245, 176.78192239067099), (2.1875, 2.5625, 1.65625), "PWM_Quarry_2x2x5_B7", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4869.581, 623.76855, 2569.8516), (-4.166473359744585, -55.02514084856904, 169.1492863008671), (2.1875, 2.8125, 1.65625), "PWM_Quarry_2x2x5_B8", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4145.0, 889.37305, 2736.3667), (-24.93743790552022, 88.57508104659424, 95.43164019426744), (1.78125, 1.0, 2.46875), "PWM_Quarry_2x2x5_B9_16", _folder)
if a: placed += 1
else: skipped += 1

# Batch 98: StaticMesh'PWM_Quarry_3x3x2' (24 instances)
_mesh_path = "/Game/Unshippable/Whitebox/Rocks/Meshes/PWM_Quarry_3x3x2"
_materials = ['/Game/Environments/ProcTexturing/ProcMaterial_Quarry_Atlas_A']
_folder = "Reconstruction/BD_BB_Chapter5_BrokenSeal/Meshes"
a = spawn_static_mesh(_mesh_path, _materials, (797.9546, 4933.8525, 759.9302), (57.93517893680719, 161.6702950388333, -15.682468184135413), (1.0, 1.2930332, 1.321843), "PWM_Quarry_3x3x10_131", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4231.4673, 1508.8352, 2582.369), (12.903545709032437, -164.59478165657376, -79.26574444599296), (2.5499847, 1.9407417, 2.2305279), "PWM_Quarry_3x3x11_199", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2034.13, 1758.2163, 2641.5996), (-1.3250428931481397, -161.93405153551865, 8.314784426496663), (2.84375, 3.4893658, 2.84375), "PWM_Quarry_3x3x12", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1900.0001, 2036.7065, 2601.9329), (1.0799537073914258e-13, -179.99998633961638, -34.99980860051719), (2.46875, 1.78125, 4.125), "PWM_Quarry_3x3x13_660", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1705.0, 2570.0, 2615.0), (-12.24050797775555, 144.06121852748961, -171.26269055757774), (2.96875, 2.273663, 2.8723743), "PWM_Quarry_3x3x14_673", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1526.3491, 2243.9229, 2323.3284), (-12.900145823919265, 95.48278598598296, 162.15383965877515), (1.84375, 1.65625, 2.125), "PWM_Quarry_3x3x15_679", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2826.159, 408.4795, 1140.8428), (0.0, -179.99998633961752, -0.0), (1.0, 1.15625, 1.1875), "PWM_Quarry_3x3x16_40", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3541.7917, 869.2261, 1267.7119), (0.0, -160.39978385910118, 0.0), (1.0896317, 1.0, 1.21875), "PWM_Quarry_3x3x17_93", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3127.8523, 5592.1665, 1258.418), (-8.886811565472522, -149.12566881752235, -4.874939518966653), (1.0, 1.0, 1.0), "PWM_Quarry_3x3x18_112", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2841.392, 5326.198, 880.0), (0.0, -144.99985487380692, 0.0), (0.78125, 1.59375, 1.03125), "PWM_Quarry_3x3x2_256", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3465.4277, 1059.8647, 831.8384), (0.0, 155.54425287614825, -0.0), (1.0, 1.0, 1.7709231), "PWM_Quarry_3x3x20_155", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4860.0, 1730.0002, 950.0), (0.0, -179.99998633961752, -0.0), (1.0, 1.0, 1.0), "PWM_Quarry_3x3x21_14", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4860.0, 1910.0002, 980.0), (0.0, 54.99992353619846, -0.0), (1.0, 1.0, 1.0), "PWM_Quarry_3x3x22", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4429.9404, 5888.414, 2464.5298), (0.0, -169.9999013770341, 0.0), (1.0, 1.0, 1.0), "PWM_Quarry_3x3x23_104", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4648.0527, 5824.3877, 2464.5298), (0.0, -169.9999013770341, 0.0), (1.0, 1.0, 1.0), "PWM_Quarry_3x3x24", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3997.9014, 314.5039, 2570.351), (-26.079133982303606, 31.280482042620836, 6.962057039181523), (2.375, 1.0, 3.0625), "PWM_Quarry_3x3x25", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3317.9014, 144.5039, 2570.351), (-26.079103616554583, -178.74848659497937, 6.96300491615343), (2.375, 1.0, 3.0625), "PWM_Quarry_3x3x26", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2406.63, 323.92627, 2439.4768), (-3.8408816166157047, 165.4830578007317, -44.511718231564906), (1.25, 1.0, 2.401663), "PWM_Quarry_3x3x3_203", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2126.102, 362.26758, 2460.3374), (16.9614236271429, -172.62933108175142, -41.93884449326865), (1.625, 1.0, 3.024143), "PWM_Quarry_3x3x4", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (643.52246, 1473.5425, 890.79834), (0.0, -179.99998633961752, -0.0), (1.0, 1.0, 1.0), "PWM_Quarry_3x3x5_5", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4272.63, 402.10986, 2621.2603), (-40.30038252728283, 40.24817983215542, 2.70553581405017), (2.375, 1.0, 3.0625), "PWM_Quarry_3x3x6_20", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1528.9116, 5660.7256, 752.9617), (39.22435735906045, -179.99995901886567, 5.728243681840525e-07), (1.0, 1.0, 1.4470025), "PWM_Quarry_3x3x7_42", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5367.423, 2506.9294, 2747.7783), (16.558756684865752, 132.01365254635317, 171.18361354362565), (4.848586, 5.333303, 5.333303), "PWM_Quarry_3x3x8", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2743.2754, 5428.8213, 1416.3452), (-2.7554928711745923, -120.91048888901888, -4.5911252926865735), (0.8147632, 0.70187724, 1.0), "PWM_Quarry_3x3x9_71", _folder)
if a: placed += 1
else: skipped += 1

# Batch 99: StaticMesh'PWM_Quarry_4x3x10_A' (41 instances)
_mesh_path = "/Game/Unshippable/Whitebox/Rocks/Meshes/PWM_Quarry_4x3x10_A"
_materials = ['/Game/Environments/ProcTexturing/ProcMaterial_Quarry_Atlas_A']
_folder = "Reconstruction/BD_BB_Chapter5_BrokenSeal/Meshes"
a = spawn_static_mesh(_mesh_path, _materials, (4840.0, 2150.0, 2670.0), (-3.881100475047989e-09, -159.99993778930278, -90.00002733451493), (1.1875, 1.0, 1.21875), "PWM_Quarry_4x3x10_A_22", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1003.2959, 3354.5098, 2560.0), (1.3000726381952432e-07, -174.99991582684675, 90.00008926317616), (1.0, 1.34375, 1.0), "PWM_Quarry_4x3x10_A2_127", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (980.7766, 1058.9873, 2348.7139), (1.3103322148159566e-05, 130.00010790102957, -19.999906952509953), (1.5625, 1.0239997, 1.0), "PWM_Quarry_4x3x10_A3_165", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1347.5377, 677.80994, 2261.1418), (13.995808557287464, -93.21788876896319, 14.435746613312912), (1.5625, 1.512921, 1.0), "PWM_Quarry_4x3x10_A4_185", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2745.8848, 906.52136, 1033.083), (0.0, -179.99998633961752, -0.0), (1.125, 1.0, 0.5409273), "PWM_Quarry_4x3x10_A5_96", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (421.5874, 5004.0703, 1363.5571), (0.0, -179.99998633961752, -0.0), (1.0, 1.0, 1.0), "PWM_Quarry_4x3x10_A6_49", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5958.125, 3923.36, 2247.1191), (2.136551735869078, -66.44290213721942, 179.20561561255394), (1.0, 1.0, 0.72845), "PWM_Quarry_4x3x161", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (6081.8022, 4564.745, 1513.4712), (-0.9674683196057963, 110.61029070133111, 176.92193967272888), (1.23943, 1.0, 1.0), "PWM_Quarry_4x3x162", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2399.2383, 5252.328, 2839.145), (17.711081375177873, 111.68301018481522, -175.81728684168658), (1.23943, 1.0, 0.6875), "PWM_Quarry_4x3x163", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5748.2817, 4581.0244, 2319.653), (-7.052304268939167, -122.97102723224972, 172.84288053536812), (1.0, 1.0, 0.72845), "PWM_Quarry_4x3x164", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5641.717, 4757.5337, 2307.331), (15.707757491253771, 46.5249010362595, -174.19438363505358), (1.0, 1.0, 0.72845), "PWM_Quarry_4x3x165", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5502.9575, 4373.54, 2403.7556), (-7.052304268939167, -122.97102723224972, 172.84288053536812), (1.3492329, 1.6319553, 0.339453), "PWM_Quarry_4x3x166", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5193.7764, 4055.8447, 2519.788), (-7.052304268939167, -122.97102723224972, 172.84288053536812), (1.349233, 1.631955, 0.339453), "PWM_Quarry_4x3x167", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5405.8438, 3913.5864, 2551.608), (-7.052276020233644, -122.97106726723074, -176.32541792940287), (1.349233, 1.631955, 0.339453), "PWM_Quarry_4x3x168", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5097.2085, 3837.8516, 2515.1753), (-7.052276020233644, -122.97106726723074, -176.32541792940287), (1.349233, 1.631955, 0.339453), "PWM_Quarry_4x3x169", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1754.4028, 5647.93, 2655.5352), (1.3393180012412398, 42.28179410797325, 160.94089364168644), (1.0, 1.0, 1.0), "PWM_Quarry_4x3x181", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2294.0942, 1014.79395, 2618.5823), (11.94472947945566, -33.05212797336244, 142.44128377044288), (1.0, 1.0, 1.0), "PWM_Quarry_4x3x186", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5884.506, 4798.508, 1967.7396), (1.6830205411048338, -46.24316119105181, 165.50927002386973), (1.23943, 1.0, 1.0), "PWM_Quarry_4x3x199_140", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4680.24, 2752.9578, 2875.474), (0.6698479985142474, -5.809813656363829, 179.9019662744696), (1.0, 1.673448, 1.0), "PWM_Quarry_4x3x201", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5981.8843, 4024.5457, 2339.817), (-1.809173439088685, 94.14594512311295, 1.6980301038789198), (1.0, 1.0, 0.72845), "PWM_Quarry_4x3x259", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5943.3867, 4648.2144, 2186.058), (1.121459953518929, -124.21725588951016, 178.50146853057487), (1.0, 1.0, 0.72845), "PWM_Quarry_4x3x260", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (6150.233, 3867.2478, 1228.1465), (-2.795837522993072, 44.67546965613046, 3.0829102171936413), (0.783559, 0.783559, 0.89894), "PWM_Quarry_4x3x291", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (6163.0728, 4052.689, 959.0293), (-10.910094402127296, -35.05935807686249, 7.840386613614312), (0.781408, 0.781408, 0.63183796), "PWM_Quarry_4x3x292", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3907.4497, 1277.7656, 2416.889), (16.09878115727842, -93.04282082588313, 48.25989950175061), (0.781408, 0.781408, 0.75631243), "PWM_Quarry_4x3x293", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5894.3374, 1678.4845, 1980.6588), (0.4331363262674686, -62.247639979655865, -178.96987043731357), (1.2158802, 1.0, 1.0), "PWM_Quarry_4x3x50_136", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (6255.032, 2444.4944, 1611.1951), (-0.8198241834458461, 7.742919851178526, -179.24058666854518), (1.09375, 1.09375, 1.09375), "PWM_Quarry_4x3x51", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (627.45215, 5072.7314, 2253.069), (3.618879548118882, 117.72967213665017, -174.4270388085391), (1.09375, 1.09375, 1.09375), "PWM_Quarry_4x3x52", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (839.56836, 5182.5737, 2276.3298), (6.575757875681327, 52.500857502618196, 164.06298126998502), (1.09375, 1.09375, 1.09375), "PWM_Quarry_4x3x53", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5755.2764, 1260.802, 1162.8992), (2.0191469359305083, 87.3515603775358, 172.7943138341033), (1.1724819, 1.0, 0.72845), "PWM_Quarry_4x3x54", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5654.4863, 1312.6262, 2082.5435), (-2.286376636746629, 119.34342568991934, 179.90248542700508), (1.0, 1.0, 0.72845), "PWM_Quarry_4x3x55", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5794.4863, 1312.6262, 1692.5435), (-2.2862542879198173, 34.34362551045991, 179.9024854139714), (1.0, 1.0, 0.72845), "PWM_Quarry_4x3x56", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5965.2764, 1530.8021, 1062.8992), (2.0191469359305083, 87.3515603775358, 172.7943138341033), (1.0, 1.0, 1.0), "PWM_Quarry_4x3x57", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5753.8105, 1645.1194, 2128.9565), (4.953054996468787, -51.606877790899205, 177.2945364186738), (1.0, 1.0, 0.72845), "PWM_Quarry_4x3x62", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5996.917, 2383.3516, 2273.4102), (-20.217435167374674, 167.8594945696595, -177.9863498248329), (1.0, 1.0, 0.72845), "PWM_Quarry_4x3x63", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5959.1436, 2032.9797, 2203.4524), (3.346873688014527, -76.62297863520892, 175.45484618081795), (1.0, 1.0, 0.72845), "PWM_Quarry_4x3x64", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5793.2656, 2612.0696, 2387.1514), (3.346873495445382, -76.62301235998981, 145.45499905298954), (1.0, 1.0, 0.72845), "PWM_Quarry_4x3x65", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5835.9883, 1950.9878, 2295.4397), (3.346873185908845, -76.62297859394062, 175.45484628429003), (1.0, 1.0, 0.72845), "PWM_Quarry_4x3x66", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5986.0625, 2198.74, 2309.1472), (1.9201164744826344, 70.76690136903449, -174.3645652112158), (1.0, 1.0, 0.72845), "PWM_Quarry_4x3x67", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5856.382, 2732.5781, 2382.3445), (-1.3437500741935768, 102.5232633058625, -174.20042948263895), (1.0, 1.0, 0.72845), "PWM_Quarry_4x3x68", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2498.13, 1234.5011, 2478.3057), (6.552829151188643, 74.10180908264856, -155.65996839535475), (1.0442348, 1.0, 1.0), "PWM_Quarry_4x3x93", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2613.4985, 1482.7241, 2557.125), (-5.379485092346466, -100.9977640033071, -178.69127971541806), (1.0, 1.0, 0.72845), "PWM_Quarry_4x3x96", _folder)
if a: placed += 1
else: skipped += 1

# Batch 100: StaticMesh'PWM_Quarry_4x3x10_B' (4 instances)
_mesh_path = "/Game/Unshippable/Whitebox/Rocks/Meshes/PWM_Quarry_4x3x10_B"
_materials = ['/Game/Environments/ProcTexturing/ProcMaterial_Quarry_Atlas_A']
_folder = "Reconstruction/BD_BB_Chapter5_BrokenSeal/Meshes"
a = spawn_static_mesh(_mesh_path, _materials, (2439.9995, 5780.0, 2480.0), (6.830188457404346e-06, -179.99998633961638, 102.14269501120336), (1.375, 1.0, 1.2520183), "PWM_Quarry_4x3x10_B3", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2186.483, 4981.6567, 2773.888), (0.6947389027579145, -45.91901079121052, -90.33280077273412), (1.0, 1.125, 1.0), "PWM_Quarry_4x3x10_B4", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1673.7207, 4586.625, 2745.4832), (-44.083328170842165, -58.44365331879456, -96.91984719233402), (1.270017, 1.0706973, 1.0), "PWM_Quarry_4x3x10_B5", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2230.0, 3956.964, 2639.4993), (-2.1105047148747826, 155.08443071186184, 85.46627947611886), (1.9635001, 1.0, 1.3083318), "PWM_Quarry_4x3x10_B6_6", _folder)
if a: placed += 1
else: skipped += 1

# Batch 101: StaticMesh'PWM_Quarry_4x3x10_C' (6 instances)
_mesh_path = "/Game/Unshippable/Whitebox/Rocks/Meshes/PWM_Quarry_4x3x10_C"
_materials = ['/Game/Environments/ProcTexturing/ProcMaterial_Quarry_Atlas_A']
_folder = "Reconstruction/BD_BB_Chapter5_BrokenSeal/Meshes"
a = spawn_static_mesh(_mesh_path, _materials, (4700.0, 4600.0, 2740.0), (90.0, 158.40138679324392, 158.40093038912516), (1.4375, 1.59375, 1.0), "PWM_Quarry_4x3x10_C_42", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4164.2954, 4197.86, 2934.6685), (14.99989116668183, -130.00001793729237, -90.00024781543128), (1.4375, 1.59375, 1.0), "PWM_Quarry_4x3x10_C2", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3930.0, 5550.4595, 2779.875), (-1.2014916908191243e-13, -179.99998633961627, 65.00007246076393), (1.0, 1.0, 1.34375), "PWM_Quarry_4x3x10_C3_76", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3119.9995, 5430.0, 2760.0), (-90.0, 1.970998764853515, -181.97106758769692), (1.25, 1.0, 1.0), "PWM_Quarry_4x3x10_C4_95", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3915.0005, 260.0, 2735.0), (-89.1274480526807, 94.94236518368876, 95.01656201984802), (1.0, 1.4375, 1.0), "PWM_Quarry_4x3x10_C5_23", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (878.13086, 2849.1982, 899.22266), (0.0, 48.48910486862135, -0.0), (1.0, 1.0, 1.0), "PWM_Quarry_4x3x10_C8_252", _folder)
if a: placed += 1
else: skipped += 1

# Batch 102: StaticMesh'PWM_Quarry_4x4x4_A' (44 instances)
_mesh_path = "/Game/Unshippable/Whitebox/Rocks/Meshes/PWM_Quarry_4x4x4_A"
_materials = ['/Game/Environments/ProcTexturing/ProcMaterial_Quarry_Atlas_2']
_folder = "Reconstruction/BD_BB_Chapter5_BrokenSeal/Meshes"
a = spawn_static_mesh(_mesh_path, _materials, (4660.0, 4290.0, 2790.0), (0.0, -179.99998633961752, -0.0), (1.0, 1.0, 1.0), "PWM_Quarry_4x4x4_A_45", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (6144.5195, 4402.5, 1009.1533), (0.0, 7.533568756809106, -0.0), (0.9139058, 1.368173, 1.368173), "PWM_Quarry_4x4x4_A10", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3144.8606, 5784.4316, 2780.0), (0.0, 100.00013504832181, -0.0), (1.0, 1.0, 1.0), "PWM_Quarry_4x4x4_A11", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2825.057, 5698.8403, 2780.0), (0.0, 40.000135742960076, -0.0), (1.0, 1.0, 1.0), "PWM_Quarry_4x4x4_A12", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (6148.3364, 3636.2605, 2365.5618), (-3.2471317011389735, 108.95874700926802, -170.77295891330547), (1.619864, 1.0, 1.750818), "PWM_Quarry_4x4x4_A13", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2550.0, 5150.0, 2460.0), (-90.0, -122.26319517426289, 302.2632241523011), (1.1875, 1.1875, 1.0), "PWM_Quarry_4x4x4_A14_103", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (620.0, 4280.0, 2620.0), (0.0, -179.99998633961752, -0.0), (1.875, 1.78125, 1.0), "PWM_Quarry_4x4x4_A15_124", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (450.0, 4350.0, 2520.0), (-20.254760669166508, 142.31025358426677, -165.02587807309294), (1.0, 1.59375, 1.0), "PWM_Quarry_4x4x4_A16_136", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2340.4468, 236.52832, 2438.7432), (14.99999258815603, 149.99989601641968, -24.99847437786707), (1.0, 0.59375, 1.0), "PWM_Quarry_4x4x4_A17_200", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (681.5449, 1166.477, 2284.999), (-0.00018296111257796983, -65.00195161797514, 9.999327948257498), (1.125, 1.0, 1.15625), "PWM_Quarry_4x4x4_A18_168", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (400.0, 2150.0, 2515.0), (0.0, -179.99998633961752, -0.0), (1.0, 1.0, 1.0), "PWM_Quarry_4x4x4_A19_174", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3657.3318, 6220.9644, 849.16626), (0.0, 95.19130131861434, -0.0), (1.443508, 1.0, 1.7525834), "PWM_Quarry_4x4x4_A2_92", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (859.7622, 2271.1157, 2480.0), (0.0, 120.00405222519727, -0.0), (1.0, 1.34375, 1.0), "PWM_Quarry_4x4x4_A20", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4555.0, 835.0, 2830.0), (0.0, -179.99998633961752, -0.0), (1.0, 1.875, 1.0), "PWM_Quarry_4x4x4_A21_13", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4909.58, 1550.5789, 2445.8845), (7.210165410100155e-06, -46.911132153718775, 29.097602787440838), (1.368173, 1.368173, 0.80809104), "PWM_Quarry_4x4x4_A22", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2654.7764, 652.22705, 1019.0925), (0.0, -167.78992353786296, 0.0), (1.0, 1.0, 1.09375), "PWM_Quarry_4x4x4_A23_33", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3124.353, 6173.274, 1190.2124), (0.0, -179.99998633961752, -0.0), (1.0, 1.0, 0.40625), "PWM_Quarry_4x4x4_A24_103", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3134.248, 2172.092, 2675.149), (-56.57279389387611, -73.37520344457681, 76.90797446730673), (1.6740321, 2.0270767, 2.1862798), "PWM_Quarry_4x4x4_A25_8", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3092.5396, 1855.0317, 2742.5264), (39.57284138588691, -89.99802573808242, 79.76763778825755), (1.674032, 2.027077, 2.9559011), "PWM_Quarry_4x4x4_A26", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1318.3336, 6050.566, 1001.99194), (0.0, 61.60909998253596, -0.0), (0.84578407, 1.3451546, 1.3451546), "PWM_Quarry_4x4x4_A27_602", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1349.6543, 5897.688, 1673.1654), (11.201960014431434, 58.05279830946882, -86.67300020216905), (1.0, 1.0, 1.0), "PWM_Quarry_4x4x4_A28_11", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (429.4082, 6080.3955, 1200.8398), (-5.7131653776405935, -156.5310458761605, 12.914058205817739), (1.0, 1.0, 1.0), "PWM_Quarry_4x4x4_A29_14", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (6159.24, 2957.3406, 2367.996), (0.6971374243396066, 85.68380724236982, -170.25077870526), (1.619864, 1.0, 1.750818), "PWM_Quarry_4x4x4_A3", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (226.53603, 5519.66, 1500.1654), (20.276325650188266, -179.99998633961565, 1.151987040396997e-13), (0.6009333, 1.0, 1.9525955), "PWM_Quarry_4x4x4_A30_17", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1306.3219, 6028.3413, 1503.425), (3.2707857856579308, 61.60915260771857, 2.3999885093882304e-06), (0.845784, 1.345155, 1.345155), "PWM_Quarry_4x4x4_A31", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3955.244, 1786.4609, 2788.869), (0.0, 0.0, -0.0), (2.0018203, 2.4227636, 0.27871186), "PWM_Quarry_4x4x4_A32_199", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (48.84352, 896.6464, 867.50476), (-7.210357397430231, 163.96836797129149, 4.829557315447372), (1.0, 1.7095432, 1.3535128), "PWM_Quarry_4x4x4_A33_26", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (525.95447, 372.85727, 1675.4905), (-17.495329495452573, 178.7890807091192, 23.96199615684891), (1.0, 1.0, 1.0), "PWM_Quarry_4x4x4_A34_29", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1123.3098, 437.4541, 1579.213), (29.762805283497382, -20.329527423918083, -155.41791208954157), (1.0, 1.0, 1.0), "PWM_Quarry_4x4x4_A35_38", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (416.6714, 1245.7666, 1581.6158), (-26.202575098976222, -179.999958268744, -33.58999320836797), (1.0452749, 1.0, 1.0), "PWM_Quarry_4x4x4_A36_41", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (31.629023, 891.081, 986.13306), (-7.210357397430231, 163.96836797129149, 4.829557315447372), (1.0, 1.709543, 1.353513), "PWM_Quarry_4x4x4_A37", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (6111.9087, 4851.6885, 739.1533), (0.0, 72.53364362430992, -0.0), (1.368173, 1.368173, 1.368173), "PWM_Quarry_4x4x4_A38", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (-29.338987, 871.3704, 1406.2749), (1.0069590840379918, 164.19180657449974, -1.2832024945281537), (1.0, 1.709543, 1.353513), "PWM_Quarry_4x4x4_A39", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2727.8896, 6106.867, 849.16626), (0.0, -105.92348814164205, 0.0), (1.443508, 1.0, 1.752583), "PWM_Quarry_4x4x4_A4", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (389.2612, 754.62665, 1806.3845), (15.322838260440777, 115.56713273337662, 20.055084978201375), (1.0, 1.0, 1.0), "PWM_Quarry_4x4x4_A40", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (817.37195, 412.99414, 1642.5739), (2.778869093779578, -172.43210114343435, 40.04074848839084), (1.0, 1.0, 1.0), "PWM_Quarry_4x4x4_A41", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (344.6078, 1000.02625, 1728.052), (-26.202575098976222, -179.999958268744, -33.58999320836797), (1.045275, 1.0, 1.0), "PWM_Quarry_4x4x4_A42", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3955.244, 2260.9102, 2788.869), (0.0, 0.0, -0.0), (2.00182, 2.422764, 0.278712), "PWM_Quarry_4x4x4_A43", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4567.1895, 2111.455, 2759.5881), (0.0, 0.0, -0.0), (2.00182, 2.422764, 0.278712), "PWM_Quarry_4x4x4_A44", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4193.08, 5643.0537, 2949.0898), (78.83021214663327, -116.30363945982832, 63.25821162435242), (1.0, 1.0, 1.59375), "PWM_Quarry_4x4x4_A5_73", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (890.39734, 2199.1572, 2776.1558), (-7.756530190742472, -148.9328292017356, 93.89536482790851), (2.3408322, 0.8966402, 3.6051798), "PWM_Quarry_4x4x4_A6_14", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (76.34732, 5484.5728, 975.5362), (-6.062620406755727, -178.28526461393767, 1.9110561243344493), (1.060853, 1.2778342, 1.2778342), "PWM_Quarry_4x4x4_A7_5", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1377.608, 1259.9907, 2747.7234), (-3.2420668732014977, 123.33094502287585, 105.60230034183793), (2.141182, 0.798128, 2.9146075), "PWM_Quarry_4x4x4_A8", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3459.9995, 5840.0, 2780.0), (0.0, -179.99998633961752, -0.0), (1.0, 1.5, 1.0), "PWM_Quarry_4x4x4_A9_98", _folder)
if a: placed += 1
else: skipped += 1

# Batch 103: StaticMesh'PWM_Quarry_4x5x10' (1 instances)
_mesh_path = "/Game/Unshippable/Whitebox/Rocks/Meshes/PWM_Quarry_4x5x10"
_materials = ['/Game/Environments/ProcTexturing/ProcMaterial_Quarry_Atlas_A']
_folder = "Reconstruction/BD_BB_Chapter5_BrokenSeal/Meshes"
a = spawn_static_mesh(_mesh_path, _materials, (1290.5446, 217.65283, 1185.0), (0.0, 143.88109334020194, -0.0), (1.0, 1.7475792, 1.577117), "PWM_Quarry_4x5x14_379", _folder)
if a: placed += 1
else: skipped += 1

# Batch 104: StaticMesh'PWM_Quarry_5x4x10' (3 instances)
_mesh_path = "/Game/Unshippable/Whitebox/Rocks/Meshes/PWM_Quarry_5x4x10"
_materials = ['/Game/Environments/ProcTexturing/ProcMaterial_Quarry_Atlas_A']
_folder = "Reconstruction/BD_BB_Chapter5_BrokenSeal/Meshes"
a = spawn_static_mesh(_mesh_path, _materials, (4858.398, 5886.369, 2693.9988), (1.692308814554984, 147.32932011753923, 16.366987288849444), (1.9020329, 1.524634, 0.79596716), "PWM_Quarry_5x4x18", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1145.1846, 6343.8438, 1041.6816), (-3.453673879478337, -127.63728817699767, 4.797407205934014), (0.85884595, 1.781998, 1.6867111), "PWM_Quarry_5x4x21", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (440.85556, 5899.9614, 1776.2251), (86.03719199249603, -167.38607586396964, -35.1182741071257), (0.7062102, 1.0, 0.82042927), "PWM_Quarry_5x4x22_327", _folder)
if a: placed += 1
else: skipped += 1

# Batch 105: StaticMesh'PWM_Quarry_8x8x8_A' (42 instances)
_mesh_path = "/Game/Unshippable/Whitebox/Rocks/Meshes/PWM_Quarry_8x8x8_A"
_materials = ['/Game/Environments/ProcTexturing/ProcMaterial_Quarry_Atlas_2']
_folder = "Reconstruction/BD_BB_Chapter5_BrokenSeal/Meshes"
a = spawn_static_mesh(_mesh_path, _materials, (3990.0, 1520.0, 2960.0933), (4.1889689533601486e-13, -179.9999590188657, -90.0000273574021), (1.0, 0.59375, 1.0), "PWM_Quarry_8x8x8_A_27", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3281.1082, 737.1956, 2750.2322), (-9.131008667710262e-05, -170.00036964763314, -89.99969486749549), (1.131565, 0.25, 0.90625), "PWM_Quarry_8x8x8_A10", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3105.465, 377.1626, 2695.417), (-4.999785933567498, -10.00018326793082, 79.99991534533739), (1.0, 0.25, 0.625), "PWM_Quarry_8x8x8_A11", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4381.745, 3800.0, 2816.6067), (4.1889689533601486e-13, -179.9999590188657, -90.0000273574021), (0.5625, 1.0, 0.59375), "PWM_Quarry_8x8x8_A12", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4508.793, 4246.764, 2886.738), (4.1889689533601486e-13, -179.9999590188657, -90.0000273574021), (1.0079004, 1.0, 1.0254613), "PWM_Quarry_8x8x8_A13", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (208.14656, 5883.058, 1215.0), (0.0, 137.26868897190485, -0.0), (0.5115471, 0.5836075, 1.4204855), "PWM_Quarry_8x8x8_A14_313", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4221.4785, 5181.4795, 2835.2422), (4.1889689533601486e-13, -179.9999590188657, -90.0000273574021), (1.427586, 0.5253288, 1.6158326), "PWM_Quarry_8x8x8_A15", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (739.40924, 6164.2817, 1253.7346), (0.0, 176.397123589903, -0.0), (1.3, 0.5, 1.0825), "PWM_Quarry_8x8x8_A16", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (190.79684, 498.2436, 1215.0), (0.0, 137.26868897190485, -0.0), (0.73161596, 0.4517863, 1.420485), "PWM_Quarry_8x8x8_A18", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (610.9253, 153.83406, 1219.0901), (0.0, -36.23696775477504, 0.0), (0.5936032, 0.4517863, 1.420485), "PWM_Quarry_8x8x8_A19", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4620.0, 2000.0002, 2951.0945), (5.581678288049898e-06, 54.9999396183587, -89.99993624251533), (1.0, 0.59375, 1.0), "PWM_Quarry_8x8x8_A2", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (195.98657, 1006.1748, 1236.696), (2.6458923719569056, -45.23785641649875, -0.4189454939378779), (0.002403, 1.319946, 1.420485), "PWM_Quarry_8x8x8_A20", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (773.4009, 552.9237, 2158.4854), (4.2643270286551, 123.11305223982184, -179.99989746157468), (0.8706177, 1.19019, 1.1300008), "PWM_Quarry_8x8x8_A21_382", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (389.49197, 985.2344, 1987.7543), (-5.8106374232538025, 46.10233331816278, -179.99536909573249), (0.9609237, 1.0, 0.7663924), "PWM_Quarry_8x8x8_A22", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (551.2317, 1119.6025, 2448.9683), (-1.0118103129533655, 126.15362331368347, 174.2778448529779), (1.161823, 0.75, 0.766392), "PWM_Quarry_8x8x8_A23", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (805.68677, 253.26562, 1215.0), (0.0, -179.37616157709306, 0.0), (0.884808, 0.39499998, 1.420485), "PWM_Quarry_8x8x8_A24", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (265.74292, 1780.408, 2437.954), (8.048851735091787, -154.09001505181493, -2.008910976544207), (0.6875, 1.15625, 0.34375), "PWM_Quarry_8x8x8_A25", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (145.50159, 2673.7544, 2685.7668), (7.161704775401144, -172.01521453456493, -0.7164611643155017), (0.5880456, 1.15625, 0.766392), "PWM_Quarry_8x8x8_A26", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1575.4092, 6022.2207, 2737.4885), (15.021388433603152, 134.30976221182118, 91.52059838554854), (0.815415, 0.815415, 0.815415), "PWM_Quarry_8x8x8_A29_1", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4060.0, 2240.0, 3020.0684), (6.881969271324031e-06, -169.99981337297476, -89.99993986324132), (1.0, 0.59375, 1.0), "PWM_Quarry_8x8x8_A3", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1917.7617, 5985.1187, 2848.2637), (-25.882049787364075, -52.81011650040086, 93.92990256908548), (0.9685889, 0.815415, 0.943568), "PWM_Quarry_8x8x8_A30", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2396.004, 4827.9717, 2862.098), (-25.882049787364075, -52.81011650040086, 93.92990256908548), (0.815415, 0.815415, 0.943568), "PWM_Quarry_8x8x8_A31", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (6045.519, 4072.2524, 694.8963), (87.86781816904129, -73.256694356684, -151.229008863695), (0.49167293, 0.813264, 0.813264), "PWM_Quarry_8x8x8_A32", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1763.5073, 4323.2524, 2937.4297), (-1.4571536364757771, 25.630305414875227, 89.38237416897701), (0.815415, 0.815415, 1.09375), "PWM_Quarry_8x8x8_A34", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5070.8516, 1116.0815, 2688.4136), (-25.882049787364075, -52.81011650040086, 93.92990256908548), (0.815415, 0.815415, 0.943568), "PWM_Quarry_8x8x8_A35", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4264.266, 1283.489, 2802.7046), (60.404659508280496, 97.46344534433054, 93.42280453505938), (0.6542486, 0.6875, 1.0039493), "PWM_Quarry_8x8x8_A36", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5085.8833, 3319.2742, 2816.2695), (-6.941345602665316, -172.3480555753179, 92.86215359434811), (0.815415, 0.815415, 0.943568), "PWM_Quarry_8x8x8_A37", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2566.1472, 4323.2524, 2829.8347), (-4.487762591173549, 25.7053976096757, 87.9242398176549), (1.606049, 0.815415, 1.7202255), "PWM_Quarry_8x8x8_A38", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1578.7456, 4222.3735, 2941.4438), (-4.487762591173549, 25.7053976096757, 87.9242398176549), (1.606049, 0.815415, 1.720225), "PWM_Quarry_8x8x8_A39", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4730.0, 3800.0, 2840.0), (4.1889689533601486e-13, -179.9999590188657, -90.0000273574021), (0.5625, 1.0, 0.59375), "PWM_Quarry_8x8x8_A4_39", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3980.0, 4295.784, 2819.7993), (-2.634094459434228e-14, -179.99998633961843, -85.00001979655099), (0.9375, 0.46875, 1.0), "PWM_Quarry_8x8x8_A5_53", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1171.2983, 5602.0957, 2564.6777), (-25.574919960460925, -43.737176992295666, 89.1330782399677), (0.94432616, 0.815415, 0.815415), "PWM_Quarry_8x8x8_A56", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (650.27246, 3382.8887, 2738.0417), (8.445479579851908, -3.9286497100447986, 179.94916292913723), (1.5093554, 1.7910116, 0.209707), "PWM_Quarry_8x8x8_A6", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1072.813, 4787.167, 2767.878), (-26.732232467379625, -56.19212663175105, 94.50285626817512), (0.815415, 0.815415, 0.815415), "PWM_Quarry_8x8x8_A60", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1558.0312, 5398.5605, 2887.8943), (15.743038267442381, 126.40306726159962, 82.59144596712599), (0.815415, 0.815415, 0.815415), "PWM_Quarry_8x8x8_A61_408", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1980.0001, 777.603, 2675.2273), (-2.9935463275563194e-19, -179.99998633961457, -179.99976777345438), (1.0359194, 1.0, 0.46875), "PWM_Quarry_8x8x8_A7_191", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2232.31, 1179.4282, 2745.2273), (0.00010928303991277651, 150.0001488763822, -179.9997677736033), (0.65625, 1.0, 0.46875), "PWM_Quarry_8x8x8_A8", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2643.2498, 397.00488, 2935.2268), (-0.0003074837519574782, -125.00036603172126, -89.99980718503232), (1.0, 0.71875, 0.90625), "PWM_Quarry_8x8x8_A9", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1548.25, 5015.46, 2866.1113), (-17.33196606626518, -51.05810486113967, 93.58242542822794), (0.815415, 0.815415, 0.815415), "PWM_Quarry_8x8x8_A90_216", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1879.6714, 5209.963, 2843.0884), (0.6758230724465294, 38.62280554165422, -8.928131319600228), (0.815415, 0.815415, 0.9674817), "PWM_Quarry_8x8x8_A91", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2503.3027, 4612.13, 2707.7888), (-4.285829370787939, -48.12042053339678, 78.11053489991384), (0.9218229, 0.815415, 0.815415), "PWM_Quarry_8x8x8_A92", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4554.521, 1498.0735, 2919.4043), (0.6758232880550037, 38.62280552237595, -8.928131243415947), (0.815415, 0.815415, 0.815415), "PWM_Quarry_8x8x8_A93", _folder)
if a: placed += 1
else: skipped += 1

# Batch 106: StaticMesh'PWM_Quarry_Collapsed_Wall' (1 instances)
_mesh_path = "/Game/Unshippable/Whitebox/Rocks/Meshes/PWM_Quarry_Collapsed_Wall"
_materials = ['/Game/Environments/ProcTexturing/ProcMaterial_Quarry_1m_C', '/Game/Environments/ProcTexturing/ProcMaterial_Quarry_2m']
_folder = "Reconstruction/BD_BB_Chapter5_BrokenSeal/Meshes"
a = spawn_static_mesh(_mesh_path, _materials, (3334.267, 306.28662, 800.0), (0.0, 74.53636000947793, -0.0), (1.0, 1.0, 1.0), "PWM_Quarry_Collapsed_Wall_73", _folder)
if a: placed += 1
else: skipped += 1

# Batch 107: StaticMesh'PWM_Quarry_Floor_4x4x4_A' (1 instances)
_mesh_path = "/Game/Unshippable/Whitebox/Rocks/Meshes/PWM_Quarry_Floor_4x4x4_A"
_materials = ['/Game/Environments/ProcTexturing/ProcMaterial_Quarry_Atlas_4']
_folder = "Reconstruction/BD_BB_Chapter5_BrokenSeal/Meshes"
a = spawn_static_mesh(_mesh_path, _materials, (725.84576, 879.5526, 730.0), (0.0, 24.639893752351412, -0.0), (2.1491094, 2.4434273, 0.36526266), "PWM_Quarry_Floor_4x4x4_A_546", _folder)
if a: placed += 1
else: skipped += 1

# Batch 108: StaticMesh'PWM_Quarry_Floor_8x8x8_A' (1 instances)
_mesh_path = "/Game/Unshippable/Whitebox/Rocks/Meshes/PWM_Quarry_Floor_8x8x8_A"
_materials = ['/Game/Environments/ProcTexturing/ProcMaterial_Quarry_Atlas_6']
_folder = "Reconstruction/BD_BB_Chapter5_BrokenSeal/Meshes"
a = spawn_static_mesh(_mesh_path, _materials, (802.2544, 5589.2646, 694.25073), (4.4027336302052695e-13, -141.04572236684402, 179.99995901885248), (1.580529, 1.0, 0.25184187), "PWM_Quarry_Floor_8x8x8_A_593", _folder)
if a: placed += 1
else: skipped += 1

# Batch 109: StaticMesh'PWM_Quarry_RockDebris_A' (81 instances)
_mesh_path = "/Game/Unshippable/Whitebox/Rocks/Meshes/PWM_Quarry_RockDebris_A"
_materials = ['/Game/Environments/ProcTexturing/ProcMaterial_Quarry_Atlas_5']
_folder = "Reconstruction/BD_BB_Chapter5_BrokenSeal/Meshes"
a = spawn_static_mesh(_mesh_path, _materials, (543.8032, 1284.1787, 798.07324), (0.0, -179.99998633961752, -0.0), (1.0, 1.0, 1.0), "PWM_Quarry_RockDebris_A_8", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2405.272, 4697.8135, 920.604), (0.0, -153.12085012810226, 0.0), (0.8313422, 0.9563422, 0.7688422), "PWM_Quarry_RockDebris_A11", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2297.4897, 4604.671, 932.3589), (0.0, 32.915585873578536, -0.0), (0.831342, 0.956342, 0.768842), "PWM_Quarry_RockDebris_A12", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3433.8867, 5256.5415, 1393.4263), (0.0, -5.541564821133664, 0.0), (0.831342, 0.956342, 0.768842), "PWM_Quarry_RockDebris_A13", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2198.4963, 4878.6963, 933.76105), (0.0, 32.915585873578536, -0.0), (0.831342, 0.956342, 0.768842), "PWM_Quarry_RockDebris_A14", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4601.111, 5796.3003, 1396.9243), (0.0, 0.0, -0.0), (1.0, 1.0, 1.0), "PWM_Quarry_RockDebris_A15", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4714.77, 5701.747, 1397.9863), (0.0, 60.321808655790555, -0.0), (0.831342, 0.956342, 0.768842), "PWM_Quarry_RockDebris_A16", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5688.158, 4599.8447, 795.7571), (0.0, -179.99998633961752, -0.0), (1.0, 1.0, 1.0), "PWM_Quarry_RockDebris_A17_147", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5659.115, 4225.022, 795.7573), (0.0, -107.2740296221715, 0.0), (1.0, 1.0, 1.0), "PWM_Quarry_RockDebris_A18", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3512.8325, 980.4082, 1392.0222), (0.0, 164.99991169031665, -0.0), (1.0, 1.0, 1.0), "PWM_Quarry_RockDebris_A19_178", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3745.569, 5574.8325, 1393.408), (0.0, 0.0, -0.0), (1.0, 1.0, 1.0), "PWM_Quarry_RockDebris_A2_108", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3536.1724, 922.3916, 1397.1162), (0.0, -5.000061101918499, 0.0), (0.8018938, 0.8018938, 0.8018938), "PWM_Quarry_RockDebris_A20", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3808.5078, 977.2881, 1399.3333), (0.0, -80.00011847821676, 0.0), (0.801894, 0.801894, 0.801894), "PWM_Quarry_RockDebris_A21", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3676.1726, 887.3916, 1397.1162), (0.0, -35.00018495260194, 0.0), (0.801894, 0.801894, 0.801894), "PWM_Quarry_RockDebris_A22", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1500.9609, 5496.6035, 796.6089), (0.0, -179.99998633961752, -0.0), (1.0, 1.0, 1.0), "PWM_Quarry_RockDebris_A23_52", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1939.335, 5830.06, 929.18054), (-37.42672777511289, 179.88045122534388, 6.50804909362108), (1.0, 1.0, 1.0), "PWM_Quarry_RockDebris_A24_65", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1922.7686, 5763.7764, 922.41815), (-4.099515829859064, 115.28475460688807, 29.956900588179895), (1.0, 1.0, 1.0), "PWM_Quarry_RockDebris_A25", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1884.503, 5721.6953, 896.48773), (-1.6644901580087292, 116.01725907587227, 28.22617821210037), (1.0, 1.0, 1.0), "PWM_Quarry_RockDebris_A26", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2844.6196, 5439.1855, 1402.237), (0.0, 139.54009583285122, -0.0), (0.88064444, 0.76980156, 1.0), "PWM_Quarry_RockDebris_A27_74", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2818.2432, 5460.154, 1402.237), (0.0, -71.7503606394154, 0.0), (0.880644, 0.58503836, 1.0), "PWM_Quarry_RockDebris_A28_83", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2088.8748, 4925.203, 933.76105), (0.0, -122.54162279750292, 0.0), (0.831342, 0.956342, 0.768842), "PWM_Quarry_RockDebris_A29", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1122.7994, 3870.8994, 982.85657), (0.0, -40.12243462712415, 0.0), (1.4051533, 1.4051533, 1.4051533), "PWM_Quarry_RockDebris_A3_590", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5598.5713, 4030.33, 793.136), (0.0, -107.2740296221715, 0.0), (1.0, 1.0, 1.0), "PWM_Quarry_RockDebris_A32_119", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (860.8252, 5106.769, 793.6787), (0.0, -179.99998633961752, -0.0), (1.0, 1.0, 1.0), "PWM_Quarry_RockDebris_A33_140", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (932.27637, 4918.4883, 793.6787), (0.0, 110.7778652477538, -0.0), (1.0, 1.0, 1.0), "PWM_Quarry_RockDebris_A34", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (667.6538, 5153.208, 793.6787), (0.0, 110.7778652477538, -0.0), (1.0, 1.0, 1.0), "PWM_Quarry_RockDebris_A35", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5792.988, 2312.1667, 795.757), (0.0, -107.2740296221715, 0.0), (1.0, 1.0, 1.0), "PWM_Quarry_RockDebris_A36", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5762.3516, 2081.0352, 793.45483), (0.0, -57.89288260444431, 0.0), (1.0, 1.0, 1.0), "PWM_Quarry_RockDebris_A37", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (665.21155, 1162.0034, 795.584), (0.0, -104.9999077325177, 0.0), (1.0, 1.0, 1.0), "PWM_Quarry_RockDebris_A38_539", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (392.8331, 976.16766, 795.584), (0.0, -104.9999077325177, 0.0), (1.6475791, 1.6475791, 1.6475791), "PWM_Quarry_RockDebris_A39", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (813.5679, 1513.5708, 795.584), (0.0, -179.99998633961752, -0.0), (1.0, 1.0, 1.0), "PWM_Quarry_RockDebris_A4_20", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2924.882, 5614.7295, 794.53784), (0.0, 117.09779470339662, -0.0), (1.0, 1.0, 1.0), "PWM_Quarry_RockDebris_A40_125", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2959.859, 5874.374, 794.53784), (0.0, 117.09779470339662, -0.0), (1.0, 1.0, 1.0), "PWM_Quarry_RockDebris_A41", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3061.343, 5996.414, 794.53784), (0.0, -132.07475653541792, 0.0), (1.0, 1.0, 1.0), "PWM_Quarry_RockDebris_A42", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3061.343, 6286.2065, 794.53784), (0.0, -132.07475653541792, 0.0), (1.0, 1.0, 1.0), "PWM_Quarry_RockDebris_A43", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3379.652, 6286.2065, 794.53784), (0.0, -65.638601994291, 0.0), (1.0, 1.0, 1.0), "PWM_Quarry_RockDebris_A44", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3476.4797, 5873.7803, 794.53784), (0.0, -65.638601994291, 0.0), (1.0, 1.0, 1.0), "PWM_Quarry_RockDebris_A45", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3313.3098, 6107.1304, 794.53784), (0.0, 102.39346583685705, -0.0), (1.0, 1.0, 1.0), "PWM_Quarry_RockDebris_A46", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3401.6199, 5774.5234, 794.53784), (0.0, -99.71871552758655, 0.0), (1.0, 1.0, 1.0), "PWM_Quarry_RockDebris_A47", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3401.6199, 5635.2354, 794.53784), (0.0, -4.279906829996478, 0.0), (1.0, 1.0, 1.0), "PWM_Quarry_RockDebris_A48", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3401.62, 5310.3926, 794.53784), (0.0, -4.279906829996478, 0.0), (1.0, 1.0, 1.0), "PWM_Quarry_RockDebris_A49", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (395.71198, 3577.0571, 1392.7972), (0.0, -79.87786128619913, 0.0), (1.0, 1.0, 1.0), "PWM_Quarry_RockDebris_A5_130", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3401.6199, 5456.972, 794.53784), (0.0, -75.89096543794587, 0.0), (1.0, 1.0, 1.0), "PWM_Quarry_RockDebris_A50", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3000.306, 5456.972, 794.53784), (0.0, -75.89096543794587, 0.0), (1.0, 1.0, 1.0), "PWM_Quarry_RockDebris_A51", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3000.3062, 5245.769, 794.53784), (0.0, -75.89096543794587, 0.0), (1.0, 1.0, 1.0), "PWM_Quarry_RockDebris_A52", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3345.1758, 959.44824, 794.33496), (0.0, -179.99998633961752, -0.0), (1.0, 1.0, 1.0), "PWM_Quarry_RockDebris_A53_161", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3406.8457, 521.20654, 792.0066), (0.0, -87.70016432390476, 0.0), (1.0, 1.0, 1.0), "PWM_Quarry_RockDebris_A54", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3406.8457, 748.04736, 792.0066), (0.0, -24.19000255465292, 0.0), (1.0, 1.0, 1.0), "PWM_Quarry_RockDebris_A55", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3346.1223, 247.60742, 792.0066), (0.0, -54.87121386817656, 0.0), (1.0, 1.0, 1.0), "PWM_Quarry_RockDebris_A56", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3034.3428, 447.91553, 792.0066), (0.0, 148.83874964023968, -0.0), (1.0495644, 1.0, 1.0), "PWM_Quarry_RockDebris_A58", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2967.2148, 699.65234, 792.0066), (0.0, 148.83874964023968, -0.0), (1.049564, 1.0, 1.0), "PWM_Quarry_RockDebris_A59", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (307.618, 3010.9177, 1395.3846), (0.0, -41.266448910036516, 0.0), (1.0, 1.0, 1.0), "PWM_Quarry_RockDebris_A6", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2967.2148, 964.8916, 792.0066), (0.0, 166.2240354022661, -0.0), (1.049564, 1.1678063, 1.0), "PWM_Quarry_RockDebris_A60", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3005.8064, 846.54443, 792.0066), (0.0, -21.313659247851103, 0.0), (1.049564, 1.167806, 1.0), "PWM_Quarry_RockDebris_A61", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3069.5073, 1136.938, 790.68555), (0.0, -179.99998633961752, -0.0), (1.0, 1.0, 1.0), "PWM_Quarry_RockDebris_A62_178", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (487.9151, 619.44086, 795.584), (0.0, -40.761198615197195, 0.0), (1.647579, 1.647579, 1.647579), "PWM_Quarry_RockDebris_A63", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (680.6091, 499.48282, 795.584), (0.0, -3.0850217194800105, 0.0), (1.647579, 1.647579, 1.647579), "PWM_Quarry_RockDebris_A64", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (838.31616, 2907.7048, 1395.4215), (0.4992525994648745, -118.59557657180116, -0.2722472988348051), (0.79312325, 1.0, 1.0), "PWM_Quarry_RockDebris_A65", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1400.3167, 5459.5537, 796.6089), (0.0, -150.7805543829676, 0.0), (1.0, 1.0, 1.0), "PWM_Quarry_RockDebris_A66_595", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1004.9893, 5157.3364, 795.0571), (0.0, -100.00775574568517, 0.0), (1.0, 1.0, 1.0), "PWM_Quarry_RockDebris_A68", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (988.14453, 535.93604, 795.584), (0.0, 12.602873966375839, -0.0), (1.647579, 1.647579, 1.647579), "PWM_Quarry_RockDebris_A69", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (800.3709, 3512.6963, 1397.5944), (0.0, 167.11340552272384, -0.0), (0.7138343, 0.7138343, 0.7138343), "PWM_Quarry_RockDebris_A7", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1221.1337, 811.91113, 795.6191), (0.0, -40.761198615197195, 0.0), (1.4771351, 1.4771351, 1.4771351), "PWM_Quarry_RockDebris_A70", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (921.2871, 1402.0924, 794.6819), (0.0, 175.10976684457216, -0.0), (1.257117, 1.257117, 1.257117), "PWM_Quarry_RockDebris_A71", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (905.0407, 1212.206, 794.6819), (0.0, 117.3184282823482, -0.0), (1.257117, 1.257117, 1.257117), "PWM_Quarry_RockDebris_A72", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (994.0229, 1039.9424, 794.6819), (0.0, 117.3184282823482, -0.0), (1.257117, 1.257117, 1.257117), "PWM_Quarry_RockDebris_A73", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1761.8657, 1238.7151, 795.13574), (0.0, 117.02916969571712, -0.0), (1.0, 1.0, 1.0), "PWM_Quarry_RockDebris_A74", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1039.6188, 5353.5747, 795.0571), (0.0, 56.25648309553024, -0.0), (1.0, 1.0, 1.0), "PWM_Quarry_RockDebris_A75", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1191.448, 5444.353, 795.0571), (0.0, 56.25648309553024, -0.0), (1.0, 1.0, 1.0), "PWM_Quarry_RockDebris_A76", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (931.72217, 4742.1436, 795.9877), (0.0, -100.00775574568517, 0.0), (1.0, 1.0, 1.0), "PWM_Quarry_RockDebris_A77", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1263.175, 5991.414, 797.6238), (0.0, 147.62094917768982, -0.0), (2.1449316, 2.1449316, 2.1449316), "PWM_Quarry_RockDebris_A78", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (851.7625, 6006.793, 797.6238), (0.0, 147.62094917768982, -0.0), (2.144932, 2.144932, 2.144932), "PWM_Quarry_RockDebris_A79", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1379.7106, 736.2529, 795.13574), (0.0, -179.99998633961752, -0.0), (1.0, 1.0, 1.0), "PWM_Quarry_RockDebris_A8_52", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (456.12357, 5894.6934, 797.6238), (0.0, -118.7853106290624, 0.0), (2.144932, 2.144932, 2.144932), "PWM_Quarry_RockDebris_A80", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (290.70694, 5593.6216, 797.6238), (0.0, -118.7853106290624, 0.0), (2.144932, 2.144932, 2.144932), "PWM_Quarry_RockDebris_A81", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (526.10254, 5268.18, 797.6236), (0.0, -36.7724935524019, 0.0), (2.144932, 2.144932, 2.144932), "PWM_Quarry_RockDebris_A82", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1270.3435, 1908.0804, 795.84424), (-3.934904657554073e-09, -4.594543101142074, -0.7193298208485046), (1.257117, 1.257117, 1.257117), "PWM_Quarry_RockDebris_A83", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5329.2163, 2128.7612, 795.82776), (0.0, -56.56618939052264, 0.0), (1.0, 1.0, 1.0), "PWM_Quarry_RockDebris_A84", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5416.344, 1996.7942, 796.8816), (0.0, -95.17175272403291, 0.0), (1.0, 1.0, 1.0), "PWM_Quarry_RockDebris_A85", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5769.128, 1637.6942, 798.2044), (2.3397219087972365, -95.1717511700509, -8.175263901007841e-08), (1.0, 1.0, 1.0), "PWM_Quarry_RockDebris_A86", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (813.5679, 1329.3076, 795.584), (0.0, -104.9999077325177, 0.0), (1.0, 1.0, 1.0), "PWM_Quarry_RockDebris_A9", _folder)
if a: placed += 1
else: skipped += 1

# Batch 110: StaticMesh'PWM_Quarry_RockDebris_A_Optimized' (4 instances)
_mesh_path = "/Game/Unshippable/Whitebox/Rocks/Meshes/PWM_Quarry_RockDebris_A_Optimized"
_materials = ['/Game/Environments/ProcTexturing/ProcMaterial_Quarry_RockDebris_A']
_folder = "Reconstruction/BD_BB_Chapter5_BrokenSeal/Meshes"
a = spawn_static_mesh(_mesh_path, _materials, (3158.9463, 4664.178, 796.6178), (0.0, -21.73654130613027, 0.0), (1.2938424, 1.2938424, 1.2938424), "PWM_Quarry_RockDebris_A_Optimized_141", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2825.819, 4159.711, 796.6178), (0.0, 176.82584479204326, -0.0), (1.293842, 1.293842, 1.293842), "PWM_Quarry_RockDebris_A_Optimized2", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3075.8071, 4113.308, 796.61774), (0.0, 176.82584479204326, -0.0), (1.293842, 1.293842, 1.293842), "PWM_Quarry_RockDebris_A_Optimized3", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3661.3113, 4050.1982, 796.6177), (0.0, -128.9215685322164, 0.0), (1.293842, 1.293842, 1.293842), "PWM_Quarry_RockDebris_A_Optimized4", _folder)
if a: placed += 1
else: skipped += 1

# Batch 111: StaticMesh'PWM_Quarry_RockDebris_C' (42 instances)
_mesh_path = "/Game/Unshippable/Whitebox/Rocks/Meshes/PWM_Quarry_RockDebris_C"
_materials = ['/Game/Environments/ProcTexturing/ProcMaterial_Quarry_RockDebris_A']
_folder = "Reconstruction/BD_BB_Chapter5_BrokenSeal/Meshes"
a = spawn_static_mesh(_mesh_path, _materials, (666.38135, 1463.5415, 791.0508), (0.0, 166.69520240523, -0.0), (1.15625, 1.34375, 1.0), "PWM_Quarry_RockDebris_C_2", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3556.3848, 981.89307, 1394.5742), (0.0, -179.99998633961752, -0.0), (0.70597905, 0.70597905, 0.70597905), "PWM_Quarry_RockDebris_C10_175", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3716.3848, 981.89307, 1401.5742), (0.0, -179.99998633961752, -0.0), (0.705979, 0.705979, 0.705979), "PWM_Quarry_RockDebris_C11", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1555.3779, 5610.5474, 798.2197), (0.0, -179.99998633961752, -0.0), (1.0, 1.0, 1.0), "PWM_Quarry_RockDebris_C12_48", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1511.7588, 5696.3613, 798.2197), (0.0, -179.99998633961752, -0.0), (1.0, 1.0, 1.0), "PWM_Quarry_RockDebris_C13", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1825.3578, 5760.0845, 868.99805), (-29.048491856936366, -179.62492631226314, 8.591571454676497), (1.0, 1.0, 1.0), "PWM_Quarry_RockDebris_C14_61", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2705.609, 5488.162, 1362.686), (-28.157740258026685, -160.9622305101026, -0.13784748260689905), (0.529446, 0.5772603, 0.885739), "PWM_Quarry_RockDebris_C15_78", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5726.1787, 3824.3599, 795.19653), (0.0, -179.99998633961752, -0.0), (1.0, 1.0, 1.0), "PWM_Quarry_RockDebris_C16", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (763.5703, 5033.096, 800.3225), (0.0, -179.99998633961752, -0.0), (1.0, 1.0, 1.0), "PWM_Quarry_RockDebris_C17_134", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (805.2803, 4944.59, 800.3225), (0.0, -179.99998633961752, -0.0), (1.0, 1.0, 1.0), "PWM_Quarry_RockDebris_C18", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5833.8853, 2134.2593, 787.8186), (0.0, -179.99998633961752, -0.0), (1.0, 1.0, 1.0), "PWM_Quarry_RockDebris_C19", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (701.22406, 1611.6271, 813.0489), (12.168864407420871, -171.2862298186091, -3.63647465704158), (0.78125, 0.78125, 0.78125), "PWM_Quarry_RockDebris_C2_14", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5845.466, 2373.432, 787.8186), (0.0, -115.93880162471372, 0.0), (1.0, 1.2310283, 1.0), "PWM_Quarry_RockDebris_C20", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5808.1597, 2556.3247, 792.4585), (0.0, -115.93880162471372, 0.0), (1.0, 1.231028, 1.0), "PWM_Quarry_RockDebris_C21", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3519.7263, 5682.4824, 799.1172), (0.0, -179.99998633961752, -0.0), (1.0, 1.0, 1.0), "PWM_Quarry_RockDebris_C22_116", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3468.038, 6199.313, 799.1172), (0.0, -97.06218707569259, 0.0), (1.0, 1.0, 1.0), "PWM_Quarry_RockDebris_C23", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3468.038, 6075.83, 793.08264), (0.0, -72.34961516628566, 0.0), (1.0, 1.0, 0.67083585), "PWM_Quarry_RockDebris_C24", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2948.2175, 6199.3125, 799.1172), (0.0, -97.06218707569259, 0.0), (1.0, 1.0, 1.0), "PWM_Quarry_RockDebris_C25", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2876.1287, 5960.966, 797.61475), (0.0, -97.06218707569259, 0.0), (1.0, 1.0, 1.0), "PWM_Quarry_RockDebris_C26", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2876.1287, 5730.4927, 797.61475), (0.0, -156.88513344999643, 0.0), (1.0, 1.0, 1.0), "PWM_Quarry_RockDebris_C27", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2876.129, 5350.588, 797.61475), (0.0, -156.88513344999643, 0.0), (1.0, 1.0, 1.0), "PWM_Quarry_RockDebris_C28", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2957.6558, 404.44336, 800.4375), (0.0, -179.99998633961752, -0.0), (0.7908287, 0.7908287, 0.7908287), "PWM_Quarry_RockDebris_C29_140", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1437.2955, 586.0376, 796.0735), (0.0, -179.99998633961752, -0.0), (1.0, 1.0, 1.0), "PWM_Quarry_RockDebris_C3_45", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2898.0562, 585.18115, 800.4375), (0.0, -179.99998633961752, -0.0), (0.790829, 0.790829, 0.69154334), "PWM_Quarry_RockDebris_C30", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2862.1958, 840.751, 789.8027), (0.0, -128.60063319344852, 0.0), (0.9113477, 0.9113477, 0.8120616), "PWM_Quarry_RockDebris_C31", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2957.6558, 294.93994, 800.4375), (0.0, -179.99998633961752, -0.0), (0.790829, 0.790829, 0.790829), "PWM_Quarry_RockDebris_C32", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2941.1223, 103.16797, 800.4375), (0.0, -135.63471572253457, 0.0), (0.790829, 0.790829, 0.790829), "PWM_Quarry_RockDebris_C33", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3351.4436, 103.16797, 800.4375), (0.0, -135.63471572253457, 0.0), (0.790829, 0.790829, 0.790829), "PWM_Quarry_RockDebris_C34", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3441.4968, 287.70996, 797.0796), (0.0, -135.63471572253457, 0.0), (0.790829, 0.790829, 0.790829), "PWM_Quarry_RockDebris_C35", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3500.6401, 652.8262, 797.0796), (0.0, -30.893708195542473, 0.0), (0.790829, 0.790829, 0.790829), "PWM_Quarry_RockDebris_C36", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3500.6401, 846.8198, 797.0796), (0.0, -30.893708195542473, 0.0), (0.790829, 0.790829, 0.790829), "PWM_Quarry_RockDebris_C37", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3500.6396, 962.8042, 797.0796), (0.0, -66.31778054982617, 0.0), (1.0684135, 0.790829, 0.790829), "PWM_Quarry_RockDebris_C38", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3437.0425, 1140.3389, 793.91406), (0.0, -179.99998633961752, -0.0), (1.0, 1.0, 1.0), "PWM_Quarry_RockDebris_C39_158", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1551.8033, 655.72314, 796.07324), (0.0, -179.99998633961752, -0.0), (1.0, 1.0, 1.0), "PWM_Quarry_RockDebris_C4", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2949.7385, 1268.0728, 792.60815), (0.0, -179.99998633961752, -0.0), (1.0, 1.0, 1.0), "PWM_Quarry_RockDebris_C40_175", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5554.2583, 4861.8774, 798.0615), (0.0, 123.09803620640902, -0.0), (1.1649929, 1.1649929, 0.741578), "PWM_Quarry_RockDebris_C41", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2836.3848, 981.893, 1394.5742), (0.0, -179.99998633961752, -0.0), (0.705979, 0.705979, 0.705979), "PWM_Quarry_RockDebris_C42", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4745.7866, 5801.126, 1405.6328), (0.0, -179.99998633961752, -0.0), (1.0, 1.0, 1.0), "PWM_Quarry_RockDebris_C5_121", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5732.1104, 4102.438, 793.3777), (0.0, -179.99998633961752, -0.0), (1.0, 1.0, 1.0), "PWM_Quarry_RockDebris_C6_127", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5811.574, 4358.0034, 796.76245), (0.0, 123.09803620640902, -0.0), (1.0, 1.0, 1.0), "PWM_Quarry_RockDebris_C7", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5820.4067, 4581.7646, 798.0615), (0.0, 123.09803620640902, -0.0), (1.0, 1.0, 0.5765848), "PWM_Quarry_RockDebris_C8", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5672.7627, 4808.2686, 798.0615), (0.0, 123.09803620640902, -0.0), (1.0, 1.0, 0.576585), "PWM_Quarry_RockDebris_C9", _folder)
if a: placed += 1
else: skipped += 1

# Batch 112: StaticMesh'SM_Debris_Floor_01' (1 instances)
_mesh_path = "/Game/Unshippable/Whitebox/Rocks/Meshes/SM_Debris_Floor_01"
_materials = ['/Game/Environments/ProcTexturing/ProcMaterial_Quarry_RockDebris_A']
_folder = "Reconstruction/BD_BB_Chapter5_BrokenSeal/Meshes"
a = spawn_static_mesh(_mesh_path, _materials, (3382.4968, 4034.5706, 794.9185), (0.0, -179.99998633961752, -0.0), (1.0, 1.0, 1.0), "SM_Debris_Floor_16", _folder)
if a: placed += 1
else: skipped += 1

# Batch 113: StaticMesh'SM_Debris_Floor_02' (7 instances)
_mesh_path = "/Game/Unshippable/Whitebox/Rocks/Meshes/SM_Debris_Floor_02"
_materials = ['/Game/Environments/ProcTexturing/ProcMaterial_Quarry_RockDebris_A']
_folder = "Reconstruction/BD_BB_Chapter5_BrokenSeal/Meshes"
a = spawn_static_mesh(_mesh_path, _materials, (1682.2241, 3794.6104, 936.0542), (0.0, -93.89886422742985, 0.0), (1.0, 1.274348, 1.0), "SM_Debris_Floor_5", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2048.9917, 1553.2112, 929.80927), (0.0, -160.75777459270182, 0.0), (1.0, 1.0, 1.0), "SM_Debris_Floor_17", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2317.6675, 1590.9656, 930.1502), (0.0, -160.75777459270182, 0.0), (1.0, 1.0, 1.0), "SM_Debris_Floor_18", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2633.6013, 3939.4082, 788.9966), (0.0, -67.19805237347093, 0.0), (1.0, 1.0, 1.0), "SM_Debris_Floor_19", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1353.1951, 900.93933, 785.3541), (-1.7844237214372913, 154.10629297436813, 0.764433645289766), (1.4397774, 1.4397774, 1.4397774), "SM_Debris_Floor_20", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2363.9307, 1215.5087, 985.15247), (0.0, -150.82654227782234, 0.0), (1.2860851, 1.2860851, 1.2860851), "SM_Debris_Floor_36", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1452.0381, 4429.781, 936.0542), (0.0, -179.99998633961752, -0.0), (1.0, 1.2743483, 1.0), "SM_Debris_Floor_45", _folder)
if a: placed += 1
else: skipped += 1

# ======================================================================
# PHASE 2: ConstructionCatalog  (construction blocks)
# ======================================================================
unreal.log(f"[{BUBBLE_NAME}] Phase 2: Placing construction blocks...")

# Construction blocks use DecoVolume transforms (matched by Name)
_folder = "Reconstruction/BD_BB_Chapter5_BrokenSeal/Construction"

# Construction: AB_Orc_Scaffolding_Balcony_A10
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Stone
#   Volume: EMorSimpleShape::OrientedBox, BoxExtent: (198.3, 181.7, 125.9)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (2717.699, 1243.7623, 1211.4727), (0.0, 0.0, -0.0), (3.9659, 3.6347, 2.5174), "AB_Orc_Scaffolding_Balcony_A10", _folder)
if a: placed += 1
else: skipped += 1

# Construction: AB_Orc_Scaffolding_Balcony_A16_13
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Stone
#   Volume: EMorSimpleShape::OrientedBox, BoxExtent: (196.2, 178.1, 125.9)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (4179.462, 5107.168, 1211.4727), (0.0, 0.0, -0.0), (3.9230, 3.5614, 2.5174), "AB_Orc_Scaffolding_Balcony_A16_13", _folder)
if a: placed += 1
else: skipped += 1

# Construction: AB_Orc_Scaffolding_Balcony_A17
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Stone
#   Volume: EMorSimpleShape::OrientedBox, BoxExtent: (183.6, 156.6, 125.9)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (3898.6948, 5161.831, 1211.4727), (0.0, 0.0, -0.0), (3.6722, 3.1315, 2.5174), "AB_Orc_Scaffolding_Balcony_A17", _folder)
if a: placed += 1
else: skipped += 1

# Construction: AB_Orc_Scaffolding_Balcony_A18_1
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Stone
#   Volume: EMorSimpleShape::OrientedBox, BoxExtent: (175.2, 194.9, 126.4)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (3668.2554, 5040.5986, 1211.5283), (0.0, 0.0, -0.0), (3.5031, 3.8976, 2.5273), "AB_Orc_Scaffolding_Balcony_A18_1", _folder)
if a: placed += 1
else: skipped += 1

# Construction: AB_Orc_Scaffolding_Balcony_A20
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Stone
#   Volume: EMorSimpleShape::OrientedBox, BoxExtent: (172.0, 135.2, 125.9)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (1375.5021, 3651.4976, 1161.4727), (0.0, 0.0, -0.0), (3.4402, 2.7047, 2.5174), "AB_Orc_Scaffolding_Balcony_A20", _folder)
if a: placed += 1
else: skipped += 1

# Construction: AB_Orc_Scaffolding_Balcony_A9_2
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Stone
#   Volume: EMorSimpleShape::OrientedBox, BoxExtent: (198.3, 181.7, 125.9)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (2439.5447, 1356.1456, 1211.4727), (0.0, 0.0, -0.0), (3.9659, 3.6347, 2.5174), "AB_Orc_Scaffolding_Balcony_A9_2", _folder)
if a: placed += 1
else: skipped += 1

# Construction: AB_Orc_Scaffolding_Foundation_3x1m11
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Stone
#   Volume: EMorSimpleShape::OrientedBox, BoxExtent: (176.9, 133.8, 169.2)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (2667.6675, 1101.2338, 1153.346), (0.0, 0.0, -0.0), (3.5383, 2.6754, 3.3833), "AB_Orc_Scaffolding_Foundation_3x1m11", _folder)
if a: placed += 1
else: skipped += 1

# Construction: AB_Orc_Scaffolding_Foundation_3x1m14
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Stone
#   Volume: EMorSimpleShape::OrientedBox, BoxExtent: (142.4, 176.1, 169.2)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (1091.1206, 3780.5303, 953.346), (0.0, 0.0, -0.0), (2.8488, 3.5215, 3.3833), "AB_Orc_Scaffolding_Foundation_3x1m14", _folder)
if a: placed += 1
else: skipped += 1

# Construction: AB_Orc_Scaffolding_Foundation_3x1m15
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Stone
#   Volume: EMorSimpleShape::OrientedBox, BoxExtent: (157.5, 172.5, 169.2)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (4466.8994, 4943.4976, 953.346), (0.0, 0.0, -0.0), (3.1490, 3.4508, 3.3833), "AB_Orc_Scaffolding_Foundation_3x1m15", _folder)
if a: placed += 1
else: skipped += 1

# Construction: AB_Orc_Scaffolding_Foundation_3x1m2
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Stone
#   Volume: EMorSimpleShape::OrientedBox, BoxExtent: (139.6, 176.5, 169.2)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (2201.0527, 1343.0714, 953.346), (0.0, 0.0, -0.0), (2.7927, 3.5302, 3.3833), "AB_Orc_Scaffolding_Foundation_3x1m2", _folder)
if a: placed += 1
else: skipped += 1

# Construction: AB_Orc_Scaffolding_Foundation_3x1m21
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Stone
#   Volume: EMorSimpleShape::OrientedBox, BoxExtent: (133.8, 176.9, 169.2)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (1214.0609, 3876.941, 1103.346), (0.0, 0.0, -0.0), (2.6754, 3.5383, 3.3833), "AB_Orc_Scaffolding_Foundation_3x1m21", _folder)
if a: placed += 1
else: skipped += 1

# Construction: AB_Orc_Scaffolding_Foundation_3x1m23
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Stone
#   Volume: EMorSimpleShape::OrientedBox, BoxExtent: (133.8, 176.9, 169.2)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (1335.8973, 4178.49, 1103.346), (0.0, 0.0, -0.0), (2.6754, 3.5383, 3.3833), "AB_Orc_Scaffolding_Foundation_3x1m23", _folder)
if a: placed += 1
else: skipped += 1

# Construction: AB_Orc_Scaffolding_Foundation_3x1m25
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Stone
#   Volume: EMorSimpleShape::OrientedBox, BoxExtent: (209.3, 164.2, 200.7)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (1707.96, 2063.2542, 1071.3827), (0.0, 0.0, -0.0), (4.1858, 3.2834, 4.0148), "AB_Orc_Scaffolding_Foundation_3x1m25", _folder)
if a: placed += 1
else: skipped += 1

# Construction: AB_Orc_Scaffolding_Foundation_3x1m3
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Stone
#   Volume: EMorSimpleShape::OrientedBox, BoxExtent: (176.9, 133.8, 169.2)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (2389.5127, 1213.6171, 953.346), (0.0, 0.0, -0.0), (3.5383, 2.6754, 3.3833), "AB_Orc_Scaffolding_Foundation_3x1m3", _folder)
if a: placed += 1
else: skipped += 1

# Construction: AB_Orc_Scaffolding_Foundation_3x1m4_9
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Stone
#   Volume: EMorSimpleShape::OrientedBox, BoxExtent: (176.9, 133.8, 169.2)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (2374.0762, 1199.0781, 1153.346), (0.0, 0.0, -0.0), (3.5383, 2.6754, 3.3833), "AB_Orc_Scaffolding_Foundation_3x1m4_9", _folder)
if a: placed += 1
else: skipped += 1

# Construction: AB_Orc_Scaffolding_Foundation_3x1m5
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Stone
#   Volume: EMorSimpleShape::OrientedBox, BoxExtent: (176.9, 133.8, 169.2)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (2667.6675, 1101.2338, 953.346), (0.0, 0.0, -0.0), (3.5383, 2.6754, 3.3833), "AB_Orc_Scaffolding_Foundation_3x1m5", _folder)
if a: placed += 1
else: skipped += 1

# Construction: AB_Orc_Scaffolding_Foundation_3x3m21_1
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Stone
#   Volume: EMorSimpleShape::OrientedBox, BoxExtent: (237.9, 215.9, 169.2)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (3900.1055, 1379.4314, 1039.1082), (0.0, 0.0, -0.0), (4.7571, 4.3179, 3.3833), "AB_Orc_Scaffolding_Foundation_3x3m21_1", _folder)
if a: placed += 1
else: skipped += 1

# Construction: AB_Orc_Scaffolding_Foundation_3x3m22
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Stone
#   Volume: EMorSimpleShape::OrientedBox, BoxExtent: (213.0, 204.7, 169.2)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (2594.8726, 4904.9263, 1057.346), (0.0, 0.0, -0.0), (4.2590, 4.0937, 3.3833), "AB_Orc_Scaffolding_Foundation_3x3m22", _folder)
if a: placed += 1
else: skipped += 1

# Construction: AB_Orc_Scaffolding_Foundation_3x3m_C_2
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Stone
#   Volume: EMorSimpleShape::OrientedBox, BoxExtent: (242.0, 159.5, 167.7)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (712.98566, 4862.6055, 943.0322), (0.0, 0.0, -0.0), (4.8398, 3.1901, 3.3536), "AB_Orc_Scaffolding_Foundation_3x3m_C_2", _folder)
if a: placed += 1
else: skipped += 1

# Construction: AB_Orc_Scaffolding_Platform_1x1_No_Legs_6
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Stone
#   Volume: EMorSimpleShape::OrientedBox, BoxExtent: (9.5, 56.0, 61.1)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (2462.7026, 5007.316, 1456.1843), (0.0, 0.0, -0.0), (0.1904, 1.1196, 1.2222), "AB_Orc_Scaffolding_Platform_1x1_No_Legs_6", _folder)
if a: placed += 1
else: skipped += 1

# Construction: AB_Orc_Scaffolding_Platform_1x1_No_Legs2
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Stone
#   Volume: EMorSimpleShape::OrientedBox, BoxExtent: (9.7, 56.0, 61.1)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (2771.34, 4989.464, 1459.1829), (0.0, 0.0, -0.0), (0.1939, 1.1197, 1.2226), "AB_Orc_Scaffolding_Platform_1x1_No_Legs2", _folder)
if a: placed += 1
else: skipped += 1

# Construction: AB_Orc_Scaffolding_Platform_1x1x2m3
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Stone
#   Volume: EMorSimpleShape::OrientedBox, BoxExtent: (77.5, 64.3, 123.6)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (2593.3784, 5213.878, 1829.8068), (0.0, 0.0, -0.0), (1.5496, 1.2862, 2.4715), "AB_Orc_Scaffolding_Platform_1x1x2m3", _folder)
if a: placed += 1
else: skipped += 1

# Construction: AB_Orc_Scaffolding_Platform_1x1x2m4
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Stone
#   Volume: EMorSimpleShape::OrientedBox, BoxExtent: (88.2, 88.0, 123.6)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (1302.3854, 2202.148, 896.0626), (0.0, 0.0, -0.0), (1.7644, 1.7604, 2.4715), "AB_Orc_Scaffolding_Platform_1x1x2m4", _folder)
if a: placed += 1
else: skipped += 1

# Construction: AB_Orc_Scaffolding_Platform_1x1x2m5
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Stone
#   Volume: EMorSimpleShape::OrientedBox, BoxExtent: (78.4, 64.7, 123.6)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (2589.018, 5104.614, 1831.8502), (0.0, 0.0, -0.0), (1.5689, 1.2947, 2.4715), "AB_Orc_Scaffolding_Platform_1x1x2m5", _folder)
if a: placed += 1
else: skipped += 1

# Construction: AB_Orc_Scaffolding_Platform_1x3x2m_7
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Stone
#   Volume: EMorSimpleShape::OrientedBox, BoxExtent: (176.9, 132.7, 123.6)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (4200.7793, 5196.1357, 1209.8368), (0.0, 0.0, -0.0), (3.5386, 2.6534, 2.4715), "AB_Orc_Scaffolding_Platform_1x3x2m_7", _folder)
if a: placed += 1
else: skipped += 1

# Construction: AB_Orc_Scaffolding_Platform_1x3x2m2
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Stone
#   Volume: EMorSimpleShape::OrientedBox, BoxExtent: (176.9, 132.7, 123.6)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (3933.6782, 5299.1514, 1209.8368), (0.0, 0.0, -0.0), (3.5386, 2.6534, 2.4715), "AB_Orc_Scaffolding_Platform_1x3x2m2", _folder)
if a: placed += 1
else: skipped += 1

# Construction: AB_Orc_Scaffolding_Platform_1x3x2m3_5
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Stone
#   Volume: EMorSimpleShape::OrientedBox, BoxExtent: (124.8, 176.3, 123.6)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (2513.4214, 1239.7527, 1407.6693), (0.0, 0.0, -0.0), (2.4957, 3.5264, 2.4715), "AB_Orc_Scaffolding_Platform_1x3x2m3_5", _folder)
if a: placed += 1
else: skipped += 1

# Construction: AB_Orc_Scaffolding_Platform_1x3x2m4_2
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Stone
#   Volume: EMorSimpleShape::OrientedBox, BoxExtent: (176.9, 132.7, 123.6)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (3895.4648, 5222.115, 1394.1173), (0.0, 0.0, -0.0), (3.5386, 2.6534, 2.4715), "AB_Orc_Scaffolding_Platform_1x3x2m4_2", _folder)
if a: placed += 1
else: skipped += 1

# Construction: AB_Orc_Scaffolding_Platform_1x3x2m5_13
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Stone
#   Volume: EMorSimpleShape::OrientedBox, BoxExtent: (156.8, 173.5, 123.6)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (4468.6206, 4944.7124, 1209.8368), (0.0, 0.0, -0.0), (3.1352, 3.4695, 2.4715), "AB_Orc_Scaffolding_Platform_1x3x2m5_13", _folder)
if a: placed += 1
else: skipped += 1

# Construction: AB_Orc_Scaffolding_Platform_1x3x2m6_16
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Stone
#   Volume: EMorSimpleShape::OrientedBox, BoxExtent: (178.1, 124.6, 123.6)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (2256.591, 5105.7227, 1066.0521), (0.0, 0.0, -0.0), (3.5630, 2.4920, 2.4715), "AB_Orc_Scaffolding_Platform_1x3x2m6_16", _folder)
if a: placed += 1
else: skipped += 1

# Construction: AB_Orc_Scaffolding_Platform_1x3x2m7_2
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Stone
#   Volume: EMorSimpleShape::OrientedBox, BoxExtent: (175.2, 152.5, 123.6)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (4649.4336, 1622.1075, 1049.8368), (0.0, 0.0, -0.0), (3.5034, 3.0501, 2.4715), "AB_Orc_Scaffolding_Platform_1x3x2m7_2", _folder)
if a: placed += 1
else: skipped += 1

# Construction: AB_Orc_Scaffolding_Platform_1x3x3m_2
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Stone
#   Volume: EMorSimpleShape::OrientedBox, BoxExtent: (147.1, 129.3, 315.3)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (1207.2933, 2571.563, 1190.26), (0.0, 0.0, -0.0), (2.9426, 2.5858, 6.3062), "AB_Orc_Scaffolding_Platform_1x3x3m_2", _folder)
if a: placed += 1
else: skipped += 1

# Construction: AB_Orc_Scaffolding_Platform_1x3x3m3_2
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Stone
#   Volume: EMorSimpleShape::OrientedBox, BoxExtent: (80.3, 64.8, 172.5)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (1385.8865, 3647.102, 1074.6206), (0.0, 0.0, -0.0), (1.6053, 1.2963, 3.4493), "AB_Orc_Scaffolding_Platform_1x3x3m3_2", _folder)
if a: placed += 1
else: skipped += 1

# Construction: AB_Orc_Scaffolding_Platform_1x3x3m32
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Stone
#   Volume: EMorSimpleShape::OrientedBox, BoxExtent: (100.2, 94.6, 145.5)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (1781.3365, 2121.255, 1354.5496), (0.0, 0.0, -0.0), (2.0032, 1.8911, 2.9104), "AB_Orc_Scaffolding_Platform_1x3x3m32", _folder)
if a: placed += 1
else: skipped += 1

# Construction: AB_Orc_Scaffolding_Platform_1x3x3m33
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Stone
#   Volume: EMorSimpleShape::OrientedBox, BoxExtent: (93.2, 89.1, 155.6)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (2194.928, 1616.7847, 1343.9025), (0.0, 0.0, -0.0), (1.8646, 1.7830, 3.1115), "AB_Orc_Scaffolding_Platform_1x3x3m33", _folder)
if a: placed += 1
else: skipped += 1

# Construction: AB_Orc_Scaffolding_Platform_1x3x3m5
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Stone
#   Volume: EMorSimpleShape::OrientedBox, BoxExtent: (146.7, 118.5, 315.3)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (1454.8031, 2592.7673, 1190.2601), (0.0, 0.0, -0.0), (2.9349, 2.3700, 6.3062), "AB_Orc_Scaffolding_Platform_1x3x3m5", _folder)
if a: placed += 1
else: skipped += 1

# Construction: AB_Orc_Scaffolding_Platform_3x1_No_Legs10_2
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Scaffolding
#   Volume: EMorSimpleShape::OrientedBox, BoxExtent: (77.8, 183.8, 21.2)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (2540.2239, 5219.2007, 1513.1724), (0.0, 0.0, -0.0), (1.5552, 3.6763, 0.4244), "AB_Orc_Scaffolding_Platform_3x1_No_Legs10_2", _folder)
if a: placed += 1
else: skipped += 1

# Construction: AB_Orc_Scaffolding_Platform_3x1_No_Legs11_5
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Scaffolding
#   Volume: EMorSimpleShape::OrientedBox, BoxExtent: (153.7, 83.8, 21.2)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (2622.1484, 4986.0815, 1516.0063), (0.0, 0.0, -0.0), (3.0740, 1.6763, 0.4244), "AB_Orc_Scaffolding_Platform_3x1_No_Legs11_5", _folder)
if a: placed += 1
else: skipped += 1

# Construction: AB_Orc_Scaffolding_Platform_3x1_No_Legs2_13
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Scaffolding
#   Volume: EMorSimpleShape::OrientedBox, BoxExtent: (150.7, 102.1, 21.2)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (2871.6482, 1618.0908, 1246.2104), (0.0, 0.0, -0.0), (3.0133, 2.0412, 0.4244), "AB_Orc_Scaffolding_Platform_3x1_No_Legs2_13", _folder)
if a: placed += 1
else: skipped += 1

# Construction: AB_Orc_Scaffolding_Platform_3x1_No_Legs26_19
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Scaffolding
#   Volume: EMorSimpleShape::OrientedBox, BoxExtent: (165.7, 114.1, 21.2)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (4353.869, 4986.08, 1306.2104), (0.0, 0.0, -0.0), (3.3131, 2.2821, 0.4244), "AB_Orc_Scaffolding_Platform_3x1_No_Legs26_19", _folder)
if a: placed += 1
else: skipped += 1

# Construction: AB_Orc_Scaffolding_Platform_3x1_No_Legs28
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Scaffolding
#   Volume: EMorSimpleShape::OrientedBox, BoxExtent: (169.4, 134.1, 21.2)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (4361.2886, 5083.391, 1301.2104), (0.0, 0.0, -0.0), (3.3882, 2.6829, 0.4244), "AB_Orc_Scaffolding_Platform_3x1_No_Legs28", _folder)
if a: placed += 1
else: skipped += 1

# Construction: AB_Orc_Scaffolding_Platform_3x1_No_Legs3
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Scaffolding
#   Volume: EMorSimpleShape::OrientedBox, BoxExtent: (150.7, 102.1, 21.2)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (3166.6482, 1618.0908, 1246.2104), (0.0, 0.0, -0.0), (3.0133, 2.0412, 0.4244), "AB_Orc_Scaffolding_Platform_3x1_No_Legs3", _folder)
if a: placed += 1
else: skipped += 1

# Construction: AB_Orc_Scaffolding_Platform_3x1_No_Legs35
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Scaffolding
#   Volume: EMorSimpleShape::OrientedBox, BoxExtent: (148.8, 71.5, 77.8)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (3724.6978, 5375.938, 1290.1293), (0.0, 0.0, -0.0), (2.9767, 1.4294, 1.5552), "AB_Orc_Scaffolding_Platform_3x1_No_Legs35", _folder)
if a: placed += 1
else: skipped += 1

# Construction: AB_Orc_Scaffolding_Platform_3x1_No_Legs36
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Scaffolding
#   Volume: EMorSimpleShape::OrientedBox, BoxExtent: (148.8, 71.5, 77.8)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (3722.4548, 5376.7544, 1179.8717), (0.0, 0.0, -0.0), (2.9767, 1.4294, 1.5552), "AB_Orc_Scaffolding_Platform_3x1_No_Legs36", _folder)
if a: placed += 1
else: skipped += 1

# Construction: AB_Orc_Scaffolding_Platform_3x1_No_Legs38
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Scaffolding
#   Volume: EMorSimpleShape::OrientedBox, BoxExtent: (24.2, 151.1, 77.8)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (4443.8667, 3743.4739, 990.12823), (0.0, 0.0, -0.0), (0.4849, 3.0212, 1.5552), "AB_Orc_Scaffolding_Platform_3x1_No_Legs38", _folder)
if a: placed += 1
else: skipped += 1

# Construction: AB_Orc_Scaffolding_Platform_3x1_No_Legs4
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Scaffolding
#   Volume: EMorSimpleShape::OrientedBox, BoxExtent: (150.7, 102.1, 21.2)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (3432.5415, 1605.6094, 1247.98), (0.0, 0.0, -0.0), (3.0133, 2.0412, 0.4244), "AB_Orc_Scaffolding_Platform_3x1_No_Legs4", _folder)
if a: placed += 1
else: skipped += 1

# Construction: AB_Orc_Scaffolding_Platform_3x1_No_Legs40
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Scaffolding
#   Volume: EMorSimpleShape::OrientedBox, BoxExtent: (97.4, 105.4, 77.8)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (4253.199, 2480.2866, 990.12866), (0.0, 0.0, -0.0), (1.9482, 2.1081, 1.5552), "AB_Orc_Scaffolding_Platform_3x1_No_Legs40", _folder)
if a: placed += 1
else: skipped += 1

# Construction: AB_Orc_Scaffolding_Platform_3x1_No_Legs41
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Scaffolding
#   Volume: EMorSimpleShape::OrientedBox, BoxExtent: (99.1, 138.3, 77.8)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (4374.5176, 2677.9177, 990.1287), (0.0, 0.0, -0.0), (1.9817, 2.7668, 1.5552), "AB_Orc_Scaffolding_Platform_3x1_No_Legs41", _folder)
if a: placed += 1
else: skipped += 1

# Construction: AB_Orc_Scaffolding_Platform_3x1_No_Legs5_2
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Scaffolding
#   Volume: EMorSimpleShape::OrientedBox, BoxExtent: (178.8, 205.9, 25.9)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (1561.9962, 2449.159, 1487.9199), (0.0, 0.0, -0.0), (3.5758, 4.1177, 0.5175), "AB_Orc_Scaffolding_Platform_3x1_No_Legs5_2", _folder)
if a: placed += 1
else: skipped += 1

# Construction: AB_Orc_Scaffolding_Platform_3x1_No_Legs6
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Scaffolding
#   Volume: EMorSimpleShape::OrientedBox, BoxExtent: (185.9, 204.0, 25.9)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (1734.2775, 2188.3914, 1489.669), (0.0, 0.0, -0.0), (3.7179, 4.0791, 0.5175), "AB_Orc_Scaffolding_Platform_3x1_No_Legs6", _folder)
if a: placed += 1
else: skipped += 1

# Construction: AB_Orc_Scaffolding_Platform_3x1_No_Legs7
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Scaffolding
#   Volume: EMorSimpleShape::OrientedBox, BoxExtent: (185.9, 204.0, 25.9)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (1911.7922, 1950.5835, 1492.1096), (0.0, 0.0, -0.0), (3.7179, 4.0791, 0.5175), "AB_Orc_Scaffolding_Platform_3x1_No_Legs7", _folder)
if a: placed += 1
else: skipped += 1

# Construction: AB_Orc_Scaffolding_Platform_3x1_No_Legs8
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Scaffolding
#   Volume: EMorSimpleShape::OrientedBox, BoxExtent: (199.8, 213.2, 25.9)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (2098.3835, 1704.0612, 1492.1096), (0.0, 0.0, -0.0), (3.9961, 4.2631, 0.5175), "AB_Orc_Scaffolding_Platform_3x1_No_Legs8", _folder)
if a: placed += 1
else: skipped += 1

# Construction: AB_Orc_Scaffolding_Platform_3x1_No_Legs9
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Scaffolding
#   Volume: EMorSimpleShape::OrientedBox, BoxExtent: (233.2, 231.1, 25.9)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (2343.7212, 1439.0607, 1495.8855), (0.0, 0.0, -0.0), (4.6648, 4.6228, 0.5175), "AB_Orc_Scaffolding_Platform_3x1_No_Legs9", _folder)
if a: placed += 1
else: skipped += 1

# Construction: AB_Orc_Scaffolding_Platform_3x1x3m_2
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Stone
#   Volume: EMorSimpleShape::OrientedBox, BoxExtent: (108.9, 174.8, 167.7)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (3964.248, 4928.2354, 1035.1664), (0.0, 0.0, -0.0), (2.1775, 3.4952, 3.3536), "AB_Orc_Scaffolding_Platform_3x1x3m_2", _folder)
if a: placed += 1
else: skipped += 1

# Construction: AB_Orc_Scaffolding_Platform_3x1x3m10
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Stone
#   Volume: EMorSimpleShape::OrientedBox, BoxExtent: (172.1, 100.5, 167.7)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (2563.67, 5162.796, 1124.5265), (0.0, 0.0, -0.0), (3.4420, 2.0096, 3.3536), "AB_Orc_Scaffolding_Platform_3x1x3m10", _folder)
if a: placed += 1
else: skipped += 1

# Construction: AB_Orc_Scaffolding_Platform_3x1x3m15
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Stone
#   Volume: EMorSimpleShape::OrientedBox, BoxExtent: (85.2, 169.4, 167.7)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (3616.672, 1536.9019, 1085.6373), (0.0, 0.0, -0.0), (1.7035, 3.3872, 3.3536), "AB_Orc_Scaffolding_Platform_3x1x3m15", _folder)
if a: placed += 1
else: skipped += 1

# Construction: AB_Orc_Scaffolding_Platform_3x1x3m16
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Stone
#   Volume: EMorSimpleShape::OrientedBox, BoxExtent: (85.2, 169.4, 167.7)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (2707.907, 1543.9518, 1100.2665), (0.0, 0.0, -0.0), (1.7035, 3.3872, 3.3536), "AB_Orc_Scaffolding_Platform_3x1x3m16", _folder)
if a: placed += 1
else: skipped += 1

# Construction: AB_Orc_Scaffolding_Platform_3x1x3m2_8
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Stone
#   Volume: EMorSimpleShape::OrientedBox, BoxExtent: (174.8, 108.9, 167.7)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (3726.0825, 4893.998, 1035.1664), (0.0, 0.0, -0.0), (3.4952, 2.1775, 3.3536), "AB_Orc_Scaffolding_Platform_3x1x3m2_8", _folder)
if a: placed += 1
else: skipped += 1

# Construction: AB_Orc_Scaffolding_Platform_3x1x3m3
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Stone
#   Volume: EMorSimpleShape::OrientedBox, BoxExtent: (174.8, 108.9, 167.7)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (3749.5264, 5026.9463, 1035.1664), (0.0, 0.0, -0.0), (3.4952, 2.1775, 3.3536), "AB_Orc_Scaffolding_Platform_3x1x3m3", _folder)
if a: placed += 1
else: skipped += 1

# Construction: AB_Orc_Scaffolding_Platform_3x1x3m5_2
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Stone
#   Volume: EMorSimpleShape::OrientedBox, BoxExtent: (174.8, 108.9, 167.7)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (3700.0283, 5354.3994, 955.1664), (0.0, 0.0, -0.0), (3.4952, 2.1775, 3.3536), "AB_Orc_Scaffolding_Platform_3x1x3m5_2", _folder)
if a: placed += 1
else: skipped += 1

# Construction: AB_Orc_Scaffolding_Platform_3x1x3m6
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Stone
#   Volume: EMorSimpleShape::OrientedBox, BoxExtent: (174.8, 108.9, 167.7)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (3682.6064, 5247.1196, 955.1664), (0.0, 0.0, -0.0), (3.4952, 2.1775, 3.3536), "AB_Orc_Scaffolding_Platform_3x1x3m6", _folder)
if a: placed += 1
else: skipped += 1

# Construction: AB_Orc_Scaffolding_Platform_3x1x3m7_5
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Stone
#   Volume: EMorSimpleShape::OrientedBox, BoxExtent: (169.5, 84.3, 167.7)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (705.2357, 4930.2715, 1227.7694), (0.0, 0.0, -0.0), (3.3896, 1.6860, 3.3536), "AB_Orc_Scaffolding_Platform_3x1x3m7_5", _folder)
if a: placed += 1
else: skipped += 1

# Construction: AB_Orc_Scaffolding_Platform_3x1x3m9
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Stone
#   Volume: EMorSimpleShape::OrientedBox, BoxExtent: (172.1, 100.5, 167.7)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (2545.6855, 5259.237, 955.1664), (0.0, 0.0, -0.0), (3.4420, 2.0096, 3.3536), "AB_Orc_Scaffolding_Platform_3x1x3m9", _folder)
if a: placed += 1
else: skipped += 1

# Construction: AB_Orc_Scaffolding_Platform_3x1x3m_B_2
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Stone
#   Volume: EMorSimpleShape::OrientedBox, BoxExtent: (103.7, 184.7, 166.2)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (4084.9497, 4915.126, 1039.6139), (0.0, 0.0, -0.0), (2.0743, 3.6941, 3.3242), "AB_Orc_Scaffolding_Platform_3x1x3m_B_2", _folder)
if a: placed += 1
else: skipped += 1

# Construction: AB_Orc_Scaffolding_Platform_3x1x3m_B2_6
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Stone
#   Volume: EMorSimpleShape::OrientedBox, BoxExtent: (163.4, 175.5, 166.2)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (4753.414, 1858.704, 1069.6138), (0.0, 0.0, -0.0), (3.2675, 3.5098, 3.3242), "AB_Orc_Scaffolding_Platform_3x1x3m_B2_6", _folder)
if a: placed += 1
else: skipped += 1

# Construction: AB_Orc_Scaffolding_Platform_3x1x3m_B3
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Stone
#   Volume: EMorSimpleShape::OrientedBox, BoxExtent: (163.4, 175.5, 166.2)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (4960.121, 2228.459, 1069.6138), (0.0, 0.0, -0.0), (3.2675, 3.5098, 3.3242), "AB_Orc_Scaffolding_Platform_3x1x3m_B3", _folder)
if a: placed += 1
else: skipped += 1

# Construction: AB_Orc_Scaffolding_Platform_3x1x3m_B4_2
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Stone
#   Volume: EMorSimpleShape::OrientedBox, BoxExtent: (172.8, 167.6, 166.2)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (4919.548, 2072.1636, 1375.0361), (0.0, 0.0, -0.0), (3.4565, 3.3512, 3.3242), "AB_Orc_Scaffolding_Platform_3x1x3m_B4_2", _folder)
if a: placed += 1
else: skipped += 1

# Construction: AB_Orc_Scaffolding_Platform_3x1x3m_B5_2
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Stone
#   Volume: EMorSimpleShape::OrientedBox, BoxExtent: (184.7, 103.7, 166.2)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (3707.1086, 5355.5635, 1149.6138), (0.0, 0.0, -0.0), (3.6941, 2.0743, 3.3242), "AB_Orc_Scaffolding_Platform_3x1x3m_B5_2", _folder)
if a: placed += 1
else: skipped += 1

# Construction: AB_Orc_Scaffolding_Platform_3x1x3m_B6
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Stone
#   Volume: EMorSimpleShape::OrientedBox, BoxExtent: (184.7, 103.7, 166.2)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (3675.5264, 5245.956, 1149.6138), (0.0, 0.0, -0.0), (3.6941, 2.0743, 3.3242), "AB_Orc_Scaffolding_Platform_3x1x3m_B6", _folder)
if a: placed += 1
else: skipped += 1

# Construction: AB_Orc_Scaffolding_Platform_3x2x3m4_2
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Stone
#   Volume: EMorSimpleShape::OrientedBox, BoxExtent: (132.8, 170.3, 167.7)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (4559.415, 3756.0913, 1080.1647), (0.0, 0.0, -0.0), (2.6552, 3.4054, 3.3536), "AB_Orc_Scaffolding_Platform_3x2x3m4_2", _folder)
if a: placed += 1
else: skipped += 1

# Construction: AB_Orc_Scaffolding_Platform_3x2x3m6_5
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Stone
#   Volume: EMorSimpleShape::OrientedBox, BoxExtent: (217.5, 212.5, 178.3)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (2148.6152, 1523.1897, 1073.732), (0.0, 0.0, -0.0), (4.3493, 4.2491, 3.5662), "AB_Orc_Scaffolding_Platform_3x2x3m6_5", _folder)
if a: placed += 1
else: skipped += 1

# Construction: AB_Orc_Scaffolding_Platform_3x2x3m7_2
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Stone
#   Volume: EMorSimpleShape::OrientedBox, BoxExtent: (132.8, 170.3, 167.7)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (2623.1167, 5125.149, 1600.163), (0.0, 0.0, -0.0), (2.6552, 3.4054, 3.3536), "AB_Orc_Scaffolding_Platform_3x2x3m7_2", _folder)
if a: placed += 1
else: skipped += 1

# Construction: AB_Orc_Scaffolding_Platform_3x3_No_Legs_0
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Stone
#   Volume: EMorSimpleShape::OrientedBox, BoxExtent: (152.6, 210.0, 18.5)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (4827.25, 3729.066, 950.13556), (0.0, 0.0, -0.0), (3.0511, 4.1994, 0.3699), "AB_Orc_Scaffolding_Platform_3x3_No_Legs_0", _folder)
if a: placed += 1
else: skipped += 1

# Construction: AB_Orc_Scaffolding_Platform_3x3_No_Legs10
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Stone
#   Volume: EMorSimpleShape::OrientedBox, BoxExtent: (85.7, 144.3, 210.0)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (1068.2021, 3792.7805, 953.8906), (0.0, 0.0, -0.0), (1.7147, 2.8865, 4.1994), "AB_Orc_Scaffolding_Platform_3x3_No_Legs10", _folder)
if a: placed += 1
else: skipped += 1

# Construction: AB_Orc_Scaffolding_Platform_3x3_No_Legs11
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Stone
#   Volume: EMorSimpleShape::OrientedBox, BoxExtent: (85.7, 144.3, 210.0)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (1180.4783, 4066.8862, 976.1094), (0.0, 0.0, -0.0), (1.7148, 2.8865, 4.1994), "AB_Orc_Scaffolding_Platform_3x3_No_Legs11", _folder)
if a: placed += 1
else: skipped += 1

# Construction: AB_Orc_Scaffolding_Platform_3x3_No_Legs12
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Stone
#   Volume: EMorSimpleShape::OrientedBox, BoxExtent: (76.6, 147.7, 210.0)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (997.3445, 2655.7961, 1175.6357), (0.0, 0.0, -0.0), (1.5326, 2.9531, 4.1994), "AB_Orc_Scaffolding_Platform_3x3_No_Legs12", _folder)
if a: placed += 1
else: skipped += 1

# Construction: AB_Orc_Scaffolding_Platform_3x3_No_Legs13
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Stone
#   Volume: EMorSimpleShape::OrientedBox, BoxExtent: (97.8, 153.8, 210.8)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (1117.0042, 2393.0264, 1015.0598), (0.0, 0.0, -0.0), (1.9552, 3.0757, 4.2156), "AB_Orc_Scaffolding_Platform_3x3_No_Legs13", _folder)
if a: placed += 1
else: skipped += 1

# Construction: AB_Orc_Scaffolding_Platform_3x3_No_Legs14
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Stone
#   Volume: EMorSimpleShape::OrientedBox, BoxExtent: (85.7, 144.3, 210.0)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (1261.9265, 4250.2915, 976.1094), (0.0, 0.0, -0.0), (1.7148, 2.8865, 4.1994), "AB_Orc_Scaffolding_Platform_3x3_No_Legs14", _folder)
if a: placed += 1
else: skipped += 1

# Construction: AB_Orc_Scaffolding_Platform_3x3_No_Legs19
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Stone
#   Volume: EMorSimpleShape::OrientedBox, BoxExtent: (81.9, 145.8, 210.0)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (1050.131, 2642.13, 967.85376), (0.0, 0.0, -0.0), (1.6389, 2.9163, 4.1994), "AB_Orc_Scaffolding_Platform_3x3_No_Legs19", _folder)
if a: placed += 1
else: skipped += 1

# Construction: AB_Orc_Scaffolding_Platform_3x3_No_Legs20_12
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Stone
#   Volume: EMorSimpleShape::OrientedBox, BoxExtent: (148.4, 74.2, 210.0)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (2168.3638, 5140.9717, 1035.197), (0.0, 0.0, -0.0), (2.9681, 1.4838, 4.1994), "AB_Orc_Scaffolding_Platform_3x3_No_Legs20_12", _folder)
if a: placed += 1
else: skipped += 1

# Construction: AB_Orc_Scaffolding_Platform_3x3_No_Legs21_15
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Stone
#   Volume: EMorSimpleShape::OrientedBox, BoxExtent: (150.3, 66.9, 210.0)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (2430.6594, 5302.773, 1023.8906), (0.0, 0.0, -0.0), (3.0063, 1.3386, 4.1994), "AB_Orc_Scaffolding_Platform_3x3_No_Legs21_15", _folder)
if a: placed += 1
else: skipped += 1

# Construction: AB_Orc_Scaffolding_Platform_3x3_No_Legs22
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Stone
#   Volume: EMorSimpleShape::OrientedBox, BoxExtent: (150.3, 66.9, 210.0)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (2668.725, 5394.301, 1196.1094), (0.0, 0.0, -0.0), (3.0063, 1.3387, 4.1994), "AB_Orc_Scaffolding_Platform_3x3_No_Legs22", _folder)
if a: placed += 1
else: skipped += 1

# Construction: AB_Orc_Scaffolding_Platform_3x3_No_Legs23_19
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Stone
#   Volume: EMorSimpleShape::OrientedBox, BoxExtent: (153.4, 44.7, 210.0)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (3707.227, 5373.6514, 966.1094), (0.0, 0.0, -0.0), (3.0690, 0.8941, 4.1994), "AB_Orc_Scaffolding_Platform_3x3_No_Legs23_19", _folder)
if a: placed += 1
else: skipped += 1

# Construction: AB_Orc_Scaffolding_Platform_3x3_No_Legs24
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Stone
#   Volume: EMorSimpleShape::OrientedBox, BoxExtent: (149.9, 68.8, 210.0)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (4250.892, 5221.169, 1203.8906), (0.0, 0.0, -0.0), (2.9973, 1.3762, 4.1994), "AB_Orc_Scaffolding_Platform_3x3_No_Legs24", _folder)
if a: placed += 1
else: skipped += 1

# Construction: AB_Orc_Scaffolding_Platform_3x3_No_Legs25
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Stone
#   Volume: EMorSimpleShape::OrientedBox, BoxExtent: (149.9, 68.8, 210.0)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (3952.94, 5319.7104, 1203.8906), (0.0, 0.0, -0.0), (2.9973, 1.3762, 4.1994), "AB_Orc_Scaffolding_Platform_3x3_No_Legs25", _folder)
if a: placed += 1
else: skipped += 1

# Construction: AB_Orc_Scaffolding_Platform_3x3_No_Legs26
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Stone
#   Volume: EMorSimpleShape::OrientedBox, BoxExtent: (112.2, 128.8, 210.0)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (4541.412, 5014.173, 976.1094), (0.0, 0.0, -0.0), (2.2445, 2.5750, 4.1994), "AB_Orc_Scaffolding_Platform_3x3_No_Legs26", _folder)
if a: placed += 1
else: skipped += 1

# Construction: AB_Orc_Scaffolding_Platform_3x3_No_Legs27
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Stone
#   Volume: EMorSimpleShape::OrientedBox, BoxExtent: (122.4, 119.5, 210.0)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (4728.4565, 4777.808, 1008.17334), (0.0, 0.0, -0.0), (2.4483, 2.3891, 4.1994), "AB_Orc_Scaffolding_Platform_3x3_No_Legs27", _folder)
if a: placed += 1
else: skipped += 1

# Construction: AB_Orc_Scaffolding_Platform_3x3_No_Legs29
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Stone
#   Volume: EMorSimpleShape::OrientedBox, BoxExtent: (153.4, 44.7, 210.0)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (3942.6191, 4771.9297, 1063.8906), (0.0, 0.0, -0.0), (3.0690, 0.8942, 4.1994), "AB_Orc_Scaffolding_Platform_3x3_No_Legs29", _folder)
if a: placed += 1
else: skipped += 1

# Construction: AB_Orc_Scaffolding_Platform_3x3_No_Legs30
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Stone
#   Volume: EMorSimpleShape::OrientedBox, BoxExtent: (153.4, 44.7, 210.0)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (3690.4236, 4831.6367, 1088.5542), (0.0, 0.0, -0.0), (3.0690, 0.8942, 4.1994), "AB_Orc_Scaffolding_Platform_3x3_No_Legs30", _folder)
if a: placed += 1
else: skipped += 1

# Construction: AB_Orc_Scaffolding_Platform_3x3_No_Legs5_2
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Stone
#   Volume: EMorSimpleShape::OrientedBox, BoxExtent: (148.4, 74.3, 210.0)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (2353.155, 1152.8267, 923.8906), (0.0, 0.0, -0.0), (2.9675, 1.4859, 4.1994), "AB_Orc_Scaffolding_Platform_3x3_No_Legs5_2", _folder)
if a: placed += 1
else: skipped += 1

# Construction: AB_Orc_Scaffolding_Platform_3x3_No_Legs6
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Stone
#   Volume: EMorSimpleShape::OrientedBox, BoxExtent: (148.4, 74.3, 210.0)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (2049.694, 1254.2251, 976.1094), (0.0, 0.0, -0.0), (2.9675, 1.4859, 4.1994), "AB_Orc_Scaffolding_Platform_3x3_No_Legs6", _folder)
if a: placed += 1
else: skipped += 1

# Construction: AB_Orc_Scaffolding_Platform_3x3x3m_B_2
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Stone
#   Volume: EMorSimpleShape::OrientedBox, BoxExtent: (258.5, 252.9, 167.7)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (4774.4, 2087.1826, 1089.8337), (0.0, 0.0, -0.0), (5.1707, 5.0585, 3.3536), "AB_Orc_Scaffolding_Platform_3x3x3m_B_2", _folder)
if a: placed += 1
else: skipped += 1

# Construction: AB_Orc_Scaffolding_Platform_3x3x3m_B10_4
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Stone
#   Volume: EMorSimpleShape::OrientedBox, BoxExtent: (167.1, 210.0, 167.7)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (1274.0808, 2633.895, 1888.8496), (0.0, 0.0, -0.0), (3.3422, 4.1994, 3.3536), "AB_Orc_Scaffolding_Platform_3x3x3m_B10_4", _folder)
if a: placed += 1
else: skipped += 1

# Construction: AB_Orc_Scaffolding_Platform_3x3x3m_B11
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Stone
#   Volume: EMorSimpleShape::OrientedBox, BoxExtent: (167.1, 210.0, 167.7)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (1274.0803, 2638.894, 1593.8497), (0.0, 0.0, -0.0), (3.3422, 4.1994, 3.3536), "AB_Orc_Scaffolding_Platform_3x3x3m_B11", _folder)
if a: placed += 1
else: skipped += 1

# Construction: AB_Orc_Scaffolding_Platform_3x3x3m_B12
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Stone
#   Volume: EMorSimpleShape::OrientedBox, BoxExtent: (211.2, 237.1, 167.7)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (1453.9431, 3890.7144, 1032.5273), (0.0, 0.0, -0.0), (4.2235, 4.7430, 3.3536), "AB_Orc_Scaffolding_Platform_3x3x3m_B12", _folder)
if a: placed += 1
else: skipped += 1

# Construction: AB_Orc_Scaffolding_Platform_3x3x3m_B13
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Stone
#   Volume: EMorSimpleShape::OrientedBox, BoxExtent: (251.4, 259.0, 167.7)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (4966.688, 4394.0444, 1325.9844), (0.0, 0.0, -0.0), (5.0288, 5.1802, 3.3536), "AB_Orc_Scaffolding_Platform_3x3x3m_B13", _folder)
if a: placed += 1
else: skipped += 1

# Construction: AB_Orc_Scaffolding_Platform_3x3x3m_B14
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Stone
#   Volume: EMorSimpleShape::OrientedBox, BoxExtent: (251.4, 259.0, 167.7)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (4963.4956, 4397.894, 1030.9841), (0.0, 0.0, -0.0), (5.0288, 5.1802, 3.3536), "AB_Orc_Scaffolding_Platform_3x3x3m_B14", _folder)
if a: placed += 1
else: skipped += 1

# Construction: AB_Orc_Scaffolding_Platform_3x3x3m_B7_1
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Stone
#   Volume: EMorSimpleShape::OrientedBox, BoxExtent: (236.0, 191.1, 167.7)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (3901.732, 1389.714, 1240.596), (0.0, 0.0, -0.0), (4.7208, 3.8229, 3.3536), "AB_Orc_Scaffolding_Platform_3x3x3m_B7_1", _folder)
if a: placed += 1
else: skipped += 1

# Construction: AB_Orc_Scaffolding_Platform_3x3x3m_B8
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Stone
#   Volume: EMorSimpleShape::OrientedBox, BoxExtent: (210.0, 167.1, 167.7)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (2591.8892, 4908.927, 1258.8337), (0.0, 0.0, -0.0), (4.1994, 3.3422, 3.3536), "AB_Orc_Scaffolding_Platform_3x3x3m_B8", _folder)
if a: placed += 1
else: skipped += 1

# Construction: AB_Orc_Scaffolding_Platform_3x3x3m_B9
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Stone
#   Volume: EMorSimpleShape::OrientedBox, BoxExtent: (215.2, 249.5, 167.7)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (1383.0942, 2280.6077, 1083.8516), (0.0, 0.0, -0.0), (4.3034, 4.9896, 3.3536), "AB_Orc_Scaffolding_Platform_3x3x3m_B9", _folder)
if a: placed += 1
else: skipped += 1

# Construction: AB_Orc_Scaffolding_Platform_3x3x3m_watchtower_1
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Stone
#   Volume: EMorSimpleShape::OrientedBox, BoxExtent: (189.9, 204.1, 167.7)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (3882.3938, 1382.3467, 1540.596), (0.0, 0.0, -0.0), (3.7987, 4.0819, 3.3536), "AB_Orc_Scaffolding_Platform_3x3x3m_watchtower_1", _folder)
if a: placed += 1
else: skipped += 1

# Construction: AB_Orc_Scaffolding_Stairs_1M_2
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Stone
#   Volume: EMorSimpleShape::OrientedBox, BoxExtent: (144.6, 138.2, 81.2)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (3867.811, 4947.286, 1217.5016), (0.0, 0.0, -0.0), (2.8920, 2.7630, 1.6242), "AB_Orc_Scaffolding_Stairs_1M_2", _folder)
if a: placed += 1
else: skipped += 1

# Construction: AB_Orc_Scaffolding_Stairs_2M_3
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Stone
#   Volume: EMorSimpleShape::OrientedBox, BoxExtent: (263.7, 223.0, 155.8)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (4299.577, 4822.648, 1051.8207), (0.0, 0.0, -0.0), (5.2742, 4.4596, 3.1163), "AB_Orc_Scaffolding_Stairs_2M_3", _folder)
if a: placed += 1
else: skipped += 1

# Construction: AB_Orc_Scaffolding_Storage_3x3x3m_C_0
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Scaffolding
#   Volume: EMorSimpleShape::OrientedBox, BoxExtent: (210.0, 165.8, 171.9)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (4835.2256, 3753.184, 1071.4073), (0.0, 0.0, -0.0), (4.1994, 3.3165, 3.4384), "AB_Orc_Scaffolding_Storage_3x3x3m_C_0", _folder)
if a: placed += 1
else: skipped += 1

# Construction: Balustrade_1m_broken_2
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Stone
#   Volume: EMorSimpleShape::OrientedBox, BoxExtent: (15.8, 50.0, 40.2)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (4339.682, 3304.8975, 1224.9382), (0.0, 0.0, -0.0), (0.3157, 0.9999, 0.8049), "Balustrade_1m_broken_2", _folder)
if a: placed += 1
else: skipped += 1

# Construction: Balustrade_1m_broken2
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Stone
#   Volume: EMorSimpleShape::OrientedBox, BoxExtent: (15.8, 50.0, 40.2)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (4340.318, 3405.1025, 1224.9382), (0.0, 0.0, -0.0), (0.3157, 0.9999, 0.8049), "Balustrade_1m_broken2", _folder)
if a: placed += 1
else: skipped += 1

# Construction: BP_Suburbs_Balustrade_3m_C24
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Stone
#   Volume: EMorSimpleShape::OrientedBox, BoxExtent: (17.4, 150.2, 40.2)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (4334.608, 3103.4053, 1225.9382), (0.0, 0.0, -0.0), (0.3484, 3.0032, 0.8049), "BP_Suburbs_Balustrade_3m_C24", _folder)
if a: placed += 1
else: skipped += 1

# Construction: BP_Suburbs_Balustrade_3m_C25
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Stone
#   Volume: EMorSimpleShape::OrientedBox, BoxExtent: (150.2, 17.4, 40.2)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (3016.7468, 1445.5948, 1434.0552), (0.0, 0.0, -0.0), (3.0032, 0.3485, 0.8049), "BP_Suburbs_Balustrade_3m_C25", _folder)
if a: placed += 1
else: skipped += 1

# Construction: BP_Suburbs_Balustrade_3m_C26
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Stone
#   Volume: EMorSimpleShape::OrientedBox, BoxExtent: (150.2, 17.4, 40.2)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (3316.9277, 1441.6824, 1434.0552), (0.0, 0.0, -0.0), (3.0032, 0.3485, 0.8049), "BP_Suburbs_Balustrade_3m_C26", _folder)
if a: placed += 1
else: skipped += 1

# Construction: BP_Suburbs_Wall_Thin_3x3m_E74_31
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Advanced
#   Volume: EMorSimpleShape::OrientedBox, BoxExtent: (94.2, 150.4, 159.5)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (274.73724, 3995.3726, 1120.1956), (0.0, 0.0, -0.0), (1.8831, 3.0086, 3.1897), "BP_Suburbs_Wall_Thin_3x3m_E74_31", _folder)
if a: placed += 1
else: skipped += 1

# Construction: Orc_Palissade_Gate_B_5
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Wood
#   Volume: EMorSimpleShape::OrientedBox, BoxExtent: (284.3, 40.5, 265.3)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (3200.1543, 4928.1587, 1165.2458), (0.0, 0.0, -0.0), (5.6870, 0.8106, 5.3064), "Orc_Palissade_Gate_B_5", _folder)
if a: placed += 1
else: skipped += 1

# Construction: Orc_Palissade_Post_A5_16
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Wood
#   Volume: EMorSimpleShape::OrientedBox, BoxExtent: (57.8, 118.1, 200.4)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (2992.2976, 4833.584, 969.5978), (0.0, 0.0, -0.0), (1.1568, 2.3617, 4.0088), "Orc_Palissade_Post_A5_16", _folder)
if a: placed += 1
else: skipped += 1

# Construction: Orc_Palissade_Post_A6
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Wood
#   Volume: EMorSimpleShape::OrientedBox, BoxExtent: (57.8, 118.1, 200.4)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (3342.2988, 4824.27, 955.8244), (0.0, 0.0, -0.0), (1.1568, 2.3617, 4.0088), "Orc_Palissade_Post_A6", _folder)
if a: placed += 1
else: skipped += 1

# Construction: Orc_Palissade_Wall_3X1M_A11_11
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Scaffolding
#   Volume: EMorSimpleShape::OrientedBox, BoxExtent: (160.0, 30.4, 108.5)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (3446.9285, 4879.221, 1113.1969), (0.0, 0.0, -0.0), (3.2004, 0.6083, 2.1694), "Orc_Palissade_Wall_3X1M_A11_11", _folder)
if a: placed += 1
else: skipped += 1

# Construction: Orc_Palissade_Wall_3X1M_A12
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Scaffolding
#   Volume: EMorSimpleShape::OrientedBox, BoxExtent: (30.4, 160.0, 108.5)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (1533.174, 3083.2544, 1244.0067), (0.0, 0.0, -0.0), (0.6083, 3.2004, 2.1694), "Orc_Palissade_Wall_3X1M_A12", _folder)
if a: placed += 1
else: skipped += 1

# Construction: Orc_Palissade_Wall_3X1M_A13
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Scaffolding
#   Volume: EMorSimpleShape::OrientedBox, BoxExtent: (30.4, 160.0, 108.5)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (1533.171, 3373.2534, 1244.0067), (0.0, 0.0, -0.0), (0.6083, 3.2004, 2.1694), "Orc_Palissade_Wall_3X1M_A13", _folder)
if a: placed += 1
else: skipped += 1

# Construction: Orc_Palissade_Wall_3X1M_A14
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Scaffolding
#   Volume: EMorSimpleShape::OrientedBox, BoxExtent: (160.0, 30.4, 108.5)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (2860.313, 4881.566, 1135.5543), (0.0, 0.0, -0.0), (3.2004, 0.6083, 2.1694), "Orc_Palissade_Wall_3X1M_A14", _folder)
if a: placed += 1
else: skipped += 1

# Construction: Orc_Palissade_Wall_3X1M_A2_1
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Scaffolding
#   Volume: EMorSimpleShape::OrientedBox, BoxExtent: (61.5, 162.9, 108.5)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (3745.4492, 1349.8308, 1410.2557), (0.0, 0.0, -0.0), (1.2305, 3.2575, 2.1694), "Orc_Palissade_Wall_3X1M_A2_1", _folder)
if a: placed += 1
else: skipped += 1

# Construction: Orc_Palissade_Wall_3X1M_A3_2
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Scaffolding
#   Volume: EMorSimpleShape::OrientedBox, BoxExtent: (61.5, 162.9, 108.5)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (3745.2612, 1350.7673, 1710.2559), (0.0, 0.0, -0.0), (1.2305, 3.2575, 2.1694), "Orc_Palissade_Wall_3X1M_A3_2", _folder)
if a: placed += 1
else: skipped += 1

# Construction: Orc_Palissade_Wall_3X1M_A4_3
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Scaffolding
#   Volume: EMorSimpleShape::OrientedBox, BoxExtent: (162.9, 61.5, 108.5)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (3908.4517, 1251.462, 1710.2559), (0.0, 0.0, -0.0), (3.2575, 1.2305, 2.1694), "Orc_Palissade_Wall_3X1M_A4_3", _folder)
if a: placed += 1
else: skipped += 1

# Construction: Orc_Palissade_Wall_3X1M_B14_2
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Scaffolding
#   Volume: EMorSimpleShape::OrientedBox, BoxExtent: (70.6, 190.7, 123.2)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (4034.2905, 1390.8387, 1405.0021), (0.0, 0.0, -0.0), (1.4120, 3.8131, 2.4647), "Orc_Palissade_Wall_3X1M_B14_2", _folder)
if a: placed += 1
else: skipped += 1

# Construction: Orc_Palissade_Wall_3X1M_B17
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Scaffolding
#   Volume: EMorSimpleShape::OrientedBox, BoxExtent: (187.6, 34.1, 123.2)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (2640.3372, 5056.265, 1412.9781), (0.0, 0.0, -0.0), (3.7524, 0.6817, 2.4647), "Orc_Palissade_Wall_3X1M_B17", _folder)
if a: placed += 1
else: skipped += 1

# Construction: Orc_Palissade_Wall_3X1M_B18
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Scaffolding
#   Volume: EMorSimpleShape::OrientedBox, BoxExtent: (188.2, 37.5, 123.2)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (2595.7134, 4932.933, 1414.2784), (0.0, 0.0, -0.0), (3.7641, 0.7491, 2.4647), "Orc_Palissade_Wall_3X1M_B18", _folder)
if a: placed += 1
else: skipped += 1

# Construction: Orc_Palissade_Wall_3X3M_A11
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Scaffolding
#   Volume: EMorSimpleShape::OrientedBox, BoxExtent: (186.9, 35.3, 211.2)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (4689.2915, 2818.4216, 1065.9402), (0.0, 0.0, -0.0), (3.7388, 0.7061, 4.2240), "Orc_Palissade_Wall_3X3M_A11", _folder)
if a: placed += 1
else: skipped += 1

# Construction: Orc_Palissade_Wall_3X3M_A13
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Scaffolding
#   Volume: EMorSimpleShape::OrientedBox, BoxExtent: (41.9, 222.0, 250.8)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (4289.832, 2997.865, 1012.19543), (0.0, 0.0, -0.0), (0.8386, 4.4399, 5.0160), "Orc_Palissade_Wall_3X3M_A13", _folder)
if a: placed += 1
else: skipped += 1

# Construction: Orc_Palissade_Wall_3X3M_A18_15
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Scaffolding
#   Volume: EMorSimpleShape::OrientedBox, BoxExtent: (35.3, 186.9, 211.2)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (1568.8862, 3054.6213, 1110.2734), (0.0, 0.0, -0.0), (0.7061, 3.7388, 4.2240), "Orc_Palissade_Wall_3X3M_A18_15", _folder)
if a: placed += 1
else: skipped += 1

# Construction: Orc_Palissade_Wall_3X3M_A19
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Scaffolding
#   Volume: EMorSimpleShape::OrientedBox, BoxExtent: (35.3, 186.9, 211.2)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (1568.8833, 3369.6204, 1110.2734), (0.0, 0.0, -0.0), (0.7061, 3.7388, 4.2240), "Orc_Palissade_Wall_3X3M_A19", _folder)
if a: placed += 1
else: skipped += 1

# Construction: Orc_Palissade_Wall_3X3M_A2
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Scaffolding
#   Volume: EMorSimpleShape::OrientedBox, BoxExtent: (186.9, 35.3, 211.2)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (4524.3955, 3577.5698, 1054.2515), (0.0, 0.0, -0.0), (3.7388, 0.7061, 4.2240), "Orc_Palissade_Wall_3X3M_A2", _folder)
if a: placed += 1
else: skipped += 1

# Construction: Orc_Palissade_Wall_3X3M_A5
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Scaffolding
#   Volume: EMorSimpleShape::OrientedBox, BoxExtent: (189.0, 71.4, 209.8)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (3909.8174, 1236.4098, 1260.894), (0.0, 0.0, -0.0), (3.7802, 1.4283, 4.1958), "Orc_Palissade_Wall_3X3M_A5", _folder)
if a: placed += 1
else: skipped += 1

# Construction: Orc_Palissade_Wall_3X3M_A6
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Scaffolding
#   Volume: EMorSimpleShape::OrientedBox, BoxExtent: (186.9, 35.3, 211.2)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (2614.3225, 5050.001, 1280.2737), (0.0, 0.0, -0.0), (3.7388, 0.7061, 4.2240), "Orc_Palissade_Wall_3X3M_A6", _folder)
if a: placed += 1
else: skipped += 1

# Construction: Orc_Palissade_Wall_3X3M_A7
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Scaffolding
#   Volume: EMorSimpleShape::OrientedBox, BoxExtent: (97.1, 187.7, 211.2)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (1232.7117, 2249.747, 1105.2927), (0.0, 0.0, -0.0), (1.9424, 3.7549, 4.2240), "Orc_Palissade_Wall_3X3M_A7", _folder)
if a: placed += 1
else: skipped += 1

# Construction: Orc_Palissade_Wall_3X3M_C11
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Scaffolding
#   Volume: EMorSimpleShape::OrientedBox, BoxExtent: (154.9, 25.6, 199.2)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (3492.5684, 4883.8193, 954.09143), (0.0, 0.0, -0.0), (3.0971, 0.5121, 3.9831), "Orc_Palissade_Wall_3X3M_C11", _folder)
if a: placed += 1
else: skipped += 1

# Construction: Orc_Palissade_Wall_3X3M_C12
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Scaffolding
#   Volume: EMorSimpleShape::OrientedBox, BoxExtent: (154.9, 25.6, 199.2)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (4442.5635, 2831.827, 1038.223), (0.0, 0.0, -0.0), (3.0971, 0.5121, 3.9831), "Orc_Palissade_Wall_3X3M_C12", _folder)
if a: placed += 1
else: skipped += 1

# Construction: Orc_Palissade_Wall_3X3M_C14
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Scaffolding
#   Volume: EMorSimpleShape::OrientedBox, BoxExtent: (30.4, 183.9, 236.5)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (4294.4473, 3376.8416, 986.2301), (0.0, 0.0, -0.0), (0.6082, 3.6778, 4.7300), "Orc_Palissade_Wall_3X3M_C14", _folder)
if a: placed += 1
else: skipped += 1

# Construction: Orc_Palissade_Wall_3X3M_C15
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Scaffolding
#   Volume: EMorSimpleShape::OrientedBox, BoxExtent: (108.3, 25.6, 199.2)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (2864.3547, 4901.118, 954.09143), (0.0, 0.0, -0.0), (2.1667, 0.5121, 3.9831), "Orc_Palissade_Wall_3X3M_C15", _folder)
if a: placed += 1
else: skipped += 1

# Construction: Orc_Palissade_Wall_3X3M_C22_1
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Scaffolding
#   Volume: EMorSimpleShape::OrientedBox, BoxExtent: (55.8, 156.9, 199.2)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (3730.9167, 1354.247, 1240.0707), (0.0, 0.0, -0.0), (1.1158, 3.1371, 3.9831), "Orc_Palissade_Wall_3X3M_C22_1", _folder)
if a: placed += 1
else: skipped += 1

# Construction: Orc_Palissade_Wall_3X3M_C23_2
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Scaffolding
#   Volume: EMorSimpleShape::OrientedBox, BoxExtent: (55.8, 156.9, 199.2)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (4022.4775, 1409.3015, 1240.0707), (0.0, 0.0, -0.0), (1.1158, 3.1371, 3.9831), "Orc_Palissade_Wall_3X3M_C23_2", _folder)
if a: placed += 1
else: skipped += 1

# Construction: Orc_Palissade_Wall_3X3M_C24
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Scaffolding
#   Volume: EMorSimpleShape::OrientedBox, BoxExtent: (25.6, 154.9, 199.2)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (2766.3433, 4898.089, 1258.3085), (0.0, 0.0, -0.0), (0.5121, 3.0971, 3.9831), "Orc_Palissade_Wall_3X3M_C24", _folder)
if a: placed += 1
else: skipped += 1

# Construction: Orc_Palissade_Wall_3X3M_C25
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Scaffolding
#   Volume: EMorSimpleShape::OrientedBox, BoxExtent: (25.6, 154.9, 199.2)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (2469.6545, 4901.914, 1258.3085), (0.0, 0.0, -0.0), (0.5121, 3.0971, 3.9831), "Orc_Palissade_Wall_3X3M_C25", _folder)
if a: placed += 1
else: skipped += 1

# Construction: Orc_Palissade_Wall_3X3M_C26
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Scaffolding
#   Volume: EMorSimpleShape::OrientedBox, BoxExtent: (154.3, 77.0, 199.2)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (1323.469, 2444.556, 1083.3256), (0.0, 0.0, -0.0), (3.0855, 1.5405, 3.9832), "Orc_Palissade_Wall_3X3M_C26", _folder)
if a: placed += 1
else: skipped += 1

# Construction: Orc_Palissade_Wall_3X3M_C27
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Scaffolding
#   Volume: EMorSimpleShape::OrientedBox, BoxExtent: (154.3, 77.0, 199.2)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (1421.3477, 2164.4524, 1083.326), (0.0, 0.0, -0.0), (3.0854, 1.5405, 3.9831), "Orc_Palissade_Wall_3X3M_C27", _folder)
if a: placed += 1
else: skipped += 1

# Construction: Orc_Post_Large_A_2
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Wood
#   Volume: EMorSimpleShape::OrientedBox, BoxExtent: (5.1, 41.1, 44.8)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (2524.6943, 4407.921, 1066.4307), (0.0, 0.0, -0.0), (0.1014, 0.8224, 0.8962), "Orc_Post_Large_A_2", _folder)
if a: placed += 1
else: skipped += 1

# Construction: Orc_Post_Large_A10
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Wood
#   Volume: EMorSimpleShape::OrientedBox, BoxExtent: (24.1, 47.7, 34.4)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (2519.6936, 4398.33, 1592.3269), (0.0, 0.0, -0.0), (0.4821, 0.9541, 0.6888), "Orc_Post_Large_A10", _folder)
if a: placed += 1
else: skipped += 1

# Construction: Orc_Post_Large_A11
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Wood
#   Volume: EMorSimpleShape::OrientedBox, BoxExtent: (32.6, 43.6, 34.4)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (2528.7563, 4508.5654, 1592.329), (0.0, 0.0, -0.0), (0.6528, 0.8717, 0.6888), "Orc_Post_Large_A11", _folder)
if a: placed += 1
else: skipped += 1

# Construction: Orc_Post_Large_A12
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Wood
#   Volume: EMorSimpleShape::OrientedBox, BoxExtent: (22.8, 45.0, 38.9)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (2500.8213, 4493.684, 1537.4539), (0.0, 0.0, -0.0), (0.4561, 0.9001, 0.7778), "Orc_Post_Large_A12", _folder)
if a: placed += 1
else: skipped += 1

# Construction: Orc_Post_Large_A13
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Wood
#   Volume: EMorSimpleShape::OrientedBox, BoxExtent: (41.8, 30.0, 38.9)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (2447.7454, 4478.2725, 1433.5308), (0.0, 0.0, -0.0), (0.8357, 0.6004, 0.7778), "Orc_Post_Large_A13", _folder)
if a: placed += 1
else: skipped += 1

# Construction: Orc_Post_Large_A14
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Wood
#   Volume: EMorSimpleShape::OrientedBox, BoxExtent: (6.4, 49.4, 37.2)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (2502.1836, 4512.026, 1367.5248), (0.0, 0.0, -0.0), (0.1285, 0.9871, 0.7443), "Orc_Post_Large_A14", _folder)
if a: placed += 1
else: skipped += 1

# Construction: Orc_Post_Large_A15
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Wood
#   Volume: EMorSimpleShape::OrientedBox, BoxExtent: (49.7, 15.1, 34.4)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (2451.9343, 4461.4917, 1724.4592), (0.0, 0.0, -0.0), (0.9934, 0.3022, 0.6889), "Orc_Post_Large_A15", _folder)
if a: placed += 1
else: skipped += 1

# Construction: Orc_Post_Large_A16
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Wood
#   Volume: EMorSimpleShape::OrientedBox, BoxExtent: (15.6, 49.6, 34.4)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (2507.171, 4403.537, 1724.4597), (0.0, 0.0, -0.0), (0.3120, 0.9923, 0.6889), "Orc_Post_Large_A16", _folder)
if a: placed += 1
else: skipped += 1

# Construction: Orc_Post_Large_A17
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Wood
#   Volume: EMorSimpleShape::OrientedBox, BoxExtent: (49.8, 13.9, 34.4)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (2566.8674, 4440.399, 1792.3195), (0.0, 0.0, -0.0), (0.9950, 0.2771, 0.6889), "Orc_Post_Large_A17", _folder)
if a: placed += 1
else: skipped += 1

# Construction: Orc_Post_Large_A18
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Wood
#   Volume: EMorSimpleShape::OrientedBox, BoxExtent: (48.6, 21.2, 34.4)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (2565.1887, 4475.9497, 1710.1675), (0.0, 0.0, -0.0), (0.9715, 0.4233, 0.6889), "Orc_Post_Large_A18", _folder)
if a: placed += 1
else: skipped += 1

# Construction: Orc_Post_Large_A19
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Wood
#   Volume: EMorSimpleShape::OrientedBox, BoxExtent: (39.5, 21.8, 44.8)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (3963.0317, 4417.3477, 1066.4304), (0.0, 0.0, -0.0), (0.7894, 0.4363, 0.8962), "Orc_Post_Large_A19", _folder)
if a: placed += 1
else: skipped += 1

# Construction: Orc_Post_Large_A2
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Wood
#   Volume: EMorSimpleShape::OrientedBox, BoxExtent: (38.7, 23.7, 44.8)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (2557.769, 4461.813, 1043.619), (0.0, 0.0, -0.0), (0.7745, 0.4742, 0.8962), "Orc_Post_Large_A2", _folder)
if a: placed += 1
else: skipped += 1

# Construction: Orc_Post_Large_A20
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Wood
#   Volume: EMorSimpleShape::OrientedBox, BoxExtent: (7.3, 41.3, 44.8)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (3927.9272, 4469.9404, 1043.6189), (0.0, 0.0, -0.0), (0.1462, 0.8268, 0.8962), "Orc_Post_Large_A20", _folder)
if a: placed += 1
else: skipped += 1

# Construction: Orc_Post_Large_A21
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Wood
#   Volume: EMorSimpleShape::OrientedBox, BoxExtent: (23.0, 39.0, 44.8)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (3885.038, 4453.6426, 1134.8315), (0.0, 0.0, -0.0), (0.4609, 0.7801, 0.8962), "Orc_Post_Large_A21", _folder)
if a: placed += 1
else: skipped += 1

# Construction: Orc_Post_Large_A22
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Wood
#   Volume: EMorSimpleShape::OrientedBox, BoxExtent: (18.6, 40.4, 44.8)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (3888.712, 4385.88, 1134.8306), (0.0, 0.0, -0.0), (0.3715, 0.8088, 0.8962), "Orc_Post_Large_A22", _folder)
if a: placed += 1
else: skipped += 1

# Construction: Orc_Post_Large_A23
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Wood
#   Volume: EMorSimpleShape::OrientedBox, BoxExtent: (48.4, 19.0, 37.2)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (3857.6267, 4408.669, 1274.3425), (0.0, 0.0, -0.0), (0.9678, 0.3806, 0.7443), "Orc_Post_Large_A23", _folder)
if a: placed += 1
else: skipped += 1

# Construction: Orc_Post_Large_A24
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Wood
#   Volume: EMorSimpleShape::OrientedBox, BoxExtent: (47.0, 23.7, 37.2)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (3887.7173, 4390.8037, 1367.5249), (0.0, 0.0, -0.0), (0.9396, 0.4748, 0.7443), "Orc_Post_Large_A24", _folder)
if a: placed += 1
else: skipped += 1

# Construction: Orc_Post_Large_A25
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Wood
#   Volume: EMorSimpleShape::OrientedBox, BoxExtent: (23.6, 47.0, 37.2)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (3938.0708, 4368.954, 1200.6697), (0.0, 0.0, -0.0), (0.4714, 0.9408, 0.7443), "Orc_Post_Large_A25", _folder)
if a: placed += 1
else: skipped += 1

# Construction: Orc_Post_Large_A26
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Wood
#   Volume: EMorSimpleShape::OrientedBox, BoxExtent: (33.9, 31.3, 44.8)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (3940.1106, 4439.9365, 1282.8923), (0.0, 0.0, -0.0), (0.6782, 0.6267, 0.8962), "Orc_Post_Large_A26", _folder)
if a: placed += 1
else: skipped += 1

# Construction: Orc_Post_Large_A27
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Wood
#   Volume: EMorSimpleShape::OrientedBox, BoxExtent: (24.4, 47.6, 34.4)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (3931.2979, 4457.9766, 1441.2502), (0.0, 0.0, -0.0), (0.4873, 0.9517, 0.6888), "Orc_Post_Large_A27", _folder)
if a: placed += 1
else: skipped += 1

# Construction: Orc_Post_Large_A28
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Wood
#   Volume: EMorSimpleShape::OrientedBox, BoxExtent: (49.8, 6.5, 34.4)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (3969.6492, 4408.793, 1592.3271), (0.0, 0.0, -0.0), (0.9954, 0.1306, 0.6888), "Orc_Post_Large_A28", _folder)
if a: placed += 1
else: skipped += 1

# Construction: Orc_Post_Large_A29
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Wood
#   Volume: EMorSimpleShape::OrientedBox, BoxExtent: (29.4, 45.5, 34.4)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (3873.3235, 4463.156, 1592.3293), (0.0, 0.0, -0.0), (0.5882, 0.9092, 0.6888), "Orc_Post_Large_A29", _folder)
if a: placed += 1
else: skipped += 1

# Construction: Orc_Post_Large_A3
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Wood
#   Volume: EMorSimpleShape::OrientedBox, BoxExtent: (29.6, 35.3, 44.8)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (2525.0183, 4493.9443, 1134.8317), (0.0, 0.0, -0.0), (0.5914, 0.7068, 0.8962), "Orc_Post_Large_A3", _folder)
if a: placed += 1
else: skipped += 1

# Construction: Orc_Post_Large_A30
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Wood
#   Volume: EMorSimpleShape::OrientedBox, BoxExtent: (35.3, 38.0, 38.9)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (3875.149, 4431.5576, 1537.4537), (0.0, 0.0, -0.0), (0.7058, 0.7606, 0.7778), "Orc_Post_Large_A30", _folder)
if a: placed += 1
else: skipped += 1

# Construction: Orc_Post_Large_A31
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Wood
#   Volume: EMorSimpleShape::OrientedBox, BoxExtent: (46.9, 8.3, 38.9)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (3860.831, 4423.499, 1433.5303), (0.0, 0.0, -0.0), (0.9380, 0.1657, 0.7777), "Orc_Post_Large_A31", _folder)
if a: placed += 1
else: skipped += 1

# Construction: Orc_Post_Large_A32
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Wood
#   Volume: EMorSimpleShape::OrientedBox, BoxExtent: (45.9, 24.1, 37.2)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (3859.06, 4440.47, 1367.5248), (0.0, 0.0, -0.0), (0.9175, 0.4826, 0.7442), "Orc_Post_Large_A32", _folder)
if a: placed += 1
else: skipped += 1

# Construction: Orc_Post_Large_A33
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Wood
#   Volume: EMorSimpleShape::OrientedBox, BoxExtent: (16.1, 49.5, 34.4)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (3883.928, 4373.685, 1724.4595), (0.0, 0.0, -0.0), (0.3215, 0.9903, 0.6889), "Orc_Post_Large_A33", _folder)
if a: placed += 1
else: skipped += 1

# Construction: Orc_Post_Large_A34
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Wood
#   Volume: EMorSimpleShape::OrientedBox, BoxExtent: (49.6, 15.6, 34.4)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (3959.679, 4399.598, 1724.46), (0.0, 0.0, -0.0), (0.9916, 0.3117, 0.6889), "Orc_Post_Large_A34", _folder)
if a: placed += 1
else: skipped += 1

# Construction: Orc_Post_Large_A35
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Wood
#   Volume: EMorSimpleShape::OrientedBox, BoxExtent: (32.7, 43.6, 34.4)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (3951.1829, 4469.242, 1792.3198), (0.0, 0.0, -0.0), (0.6532, 0.8713, 0.6889), "Orc_Post_Large_A35", _folder)
if a: placed += 1
else: skipped += 1

# Construction: Orc_Post_Large_A36
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Wood
#   Volume: EMorSimpleShape::OrientedBox, BoxExtent: (9.8, 49.9, 34.4)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (3918.1926, 4482.595, 1710.1678), (0.0, 0.0, -0.0), (0.1958, 0.9980, 0.6889), "Orc_Post_Large_A36", _folder)
if a: placed += 1
else: skipped += 1

# Construction: Orc_Post_Large_A37
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Wood
#   Volume: EMorSimpleShape::OrientedBox, BoxExtent: (38.4, 24.4, 44.8)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (4021.0483, 2235.847, 1053.4176), (0.0, 0.0, -0.0), (0.7679, 0.4887, 0.8962), "Orc_Post_Large_A37", _folder)
if a: placed += 1
else: skipped += 1

# Construction: Orc_Post_Large_A38
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Wood
#   Volume: EMorSimpleShape::OrientedBox, BoxExtent: (6.0, 41.2, 44.8)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (4052.0457, 2180.7324, 1030.606), (0.0, 0.0, -0.0), (0.1191, 0.8245, 0.8962), "Orc_Post_Large_A38", _folder)
if a: placed += 1
else: skipped += 1

# Construction: Orc_Post_Large_A39
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Wood
#   Volume: EMorSimpleShape::OrientedBox, BoxExtent: (20.4, 40.0, 44.8)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (4096.051, 2193.7168, 1121.8184), (0.0, 0.0, -0.0), (0.4071, 0.7991, 0.8962), "Orc_Post_Large_A39", _folder)
if a: placed += 1
else: skipped += 1

# Construction: Orc_Post_Large_A4
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Wood
#   Volume: EMorSimpleShape::OrientedBox, BoxExtent: (41.4, 8.7, 44.8)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (2465.0127, 4462.2505, 1134.8307), (0.0, 0.0, -0.0), (0.8283, 0.1747, 0.8962), "Orc_Post_Large_A4", _folder)
if a: placed += 1
else: skipped += 1

# Construction: Orc_Post_Large_A40
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Wood
#   Volume: EMorSimpleShape::OrientedBox, BoxExtent: (21.3, 39.6, 44.8)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (4097.549, 2261.563, 1121.8174), (0.0, 0.0, -0.0), (0.4268, 0.7928, 0.8962), "Orc_Post_Large_A40", _folder)
if a: placed += 1
else: skipped += 1

# Construction: Orc_Post_Large_A41
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Wood
#   Volume: EMorSimpleShape::OrientedBox, BoxExtent: (49.0, 15.6, 37.2)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (4126.808, 2236.4722, 1261.33), (0.0, 0.0, -0.0), (0.9806, 0.3124, 0.7443), "Orc_Post_Large_A41", _folder)
if a: placed += 1
else: skipped += 1

# Construction: Orc_Post_Large_A42
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Wood
#   Volume: EMorSimpleShape::OrientedBox, BoxExtent: (19.5, 47.2, 37.2)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (4069.1243, 2286.2666, 1354.5122), (0.0, 0.0, -0.0), (0.3907, 0.9445, 0.7443), "Orc_Post_Large_A42", _folder)
if a: placed += 1
else: skipped += 1

# Construction: Orc_Post_Large_A43
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Wood
#   Volume: EMorSimpleShape::OrientedBox, BoxExtent: (20.3, 48.1, 37.2)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (4049.6216, 2282.1985, 1187.6571), (0.0, 0.0, -0.0), (0.4063, 0.9614, 0.7442), "Orc_Post_Large_A43", _folder)
if a: placed += 1
else: skipped += 1

# Construction: Orc_Post_Large_A44
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Wood
#   Volume: EMorSimpleShape::OrientedBox, BoxExtent: (35.6, 29.2, 44.8)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (4042.1829, 2211.5764, 1269.8794), (0.0, 0.0, -0.0), (0.7125, 0.5836, 0.8962), "Orc_Post_Large_A44", _folder)
if a: placed += 1
else: skipped += 1

# Construction: Orc_Post_Large_A45
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Wood
#   Volume: EMorSimpleShape::OrientedBox, BoxExtent: (27.6, 46.3, 34.4)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (4049.597, 2192.9182, 1428.2386), (0.0, 0.0, -0.0), (0.5523, 0.9260, 0.6888), "Orc_Post_Large_A45", _folder)
if a: placed += 1
else: skipped += 1

# Construction: Orc_Post_Large_A46
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Wood
#   Volume: EMorSimpleShape::OrientedBox, BoxExtent: (49.9, 10.3, 34.4)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (4015.1025, 2244.8794, 1579.3154), (0.0, 0.0, -0.0), (0.9980, 0.2057, 0.6888), "Orc_Post_Large_A46", _folder)
if a: placed += 1
else: skipped += 1

# Construction: Orc_Post_Large_A47
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Wood
#   Volume: EMorSimpleShape::OrientedBox, BoxExtent: (26.3, 46.9, 34.4)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (4107.0063, 2183.3384, 1579.3176), (0.0, 0.0, -0.0), (0.5251, 0.9381, 0.6889), "Orc_Post_Large_A47", _folder)
if a: placed += 1
else: skipped += 1

# Construction: Orc_Post_Large_A48
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Wood
#   Volume: EMorSimpleShape::OrientedBox, BoxExtent: (32.8, 40.1, 38.9)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (4107.5938, 2214.9836, 1524.4406), (0.0, 0.0, -0.0), (0.6566, 0.8011, 0.7777), "Orc_Post_Large_A48", _folder)
if a: placed += 1
else: skipped += 1

# Construction: Orc_Post_Large_A49
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Wood
#   Volume: EMorSimpleShape::OrientedBox, BoxExtent: (44.0, 26.1, 38.9)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (4119.9478, 2268.8547, 1420.5176), (0.0, 0.0, -0.0), (0.8796, 0.5221, 0.7777), "Orc_Post_Large_A49", _folder)
if a: placed += 1
else: skipped += 1

# Construction: Orc_Post_Large_A5
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Wood
#   Volume: EMorSimpleShape::OrientedBox, BoxExtent: (35.7, 39.7, 37.2)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (2472.7012, 4500.0195, 1274.3425), (0.0, 0.0, -0.0), (0.7143, 0.7934, 0.7443), "Orc_Post_Large_A5", _folder)
if a: placed += 1
else: skipped += 1

# Construction: Orc_Post_Large_A50
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Wood
#   Volume: EMorSimpleShape::OrientedBox, BoxExtent: (44.7, 26.9, 37.2)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (4122.9575, 2204.8713, 1354.512), (0.0, 0.0, -0.0), (0.8934, 0.5377, 0.7442), "Orc_Post_Large_A50", _folder)
if a: placed += 1
else: skipped += 1

# Construction: Orc_Post_Large_A51
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Wood
#   Volume: EMorSimpleShape::OrientedBox, BoxExtent: (19.6, 48.9, 34.4)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (4103.2485, 2273.357, 1711.4478), (0.0, 0.0, -0.0), (0.3925, 0.9781, 0.6889), "Orc_Post_Large_A51", _folder)
if a: placed += 1
else: skipped += 1

# Construction: Orc_Post_Large_A52
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Wood
#   Volume: EMorSimpleShape::OrientedBox, BoxExtent: (49.0, 19.2, 34.4)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (4025.7434, 2253.2878, 1711.4484), (0.0, 0.0, -0.0), (0.9800, 0.3831, 0.6889), "Orc_Post_Large_A52", _folder)
if a: placed += 1
else: skipped += 1

# Construction: Orc_Post_Large_A53
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Wood
#   Volume: EMorSimpleShape::OrientedBox, BoxExtent: (35.4, 41.6, 34.4)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (4028.9114, 2183.2012, 1779.3082), (0.0, 0.0, -0.0), (0.7089, 0.8317, 0.6889), "Orc_Post_Large_A53", _folder)
if a: placed += 1
else: skipped += 1

# Construction: Orc_Post_Large_A54
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Wood
#   Volume: EMorSimpleShape::OrientedBox, BoxExtent: (13.5, 49.8, 34.4)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (4060.7874, 2167.3738, 1697.1561), (0.0, 0.0, -0.0), (0.2699, 0.9955, 0.6889), "Orc_Post_Large_A54", _folder)
if a: placed += 1
else: skipped += 1

# Construction: Orc_Post_Large_A6
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Wood
#   Volume: EMorSimpleShape::OrientedBox, BoxExtent: (49.0, 15.5, 37.2)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (2457.2551, 4425.397, 1367.525), (0.0, 0.0, -0.0), (0.9808, 0.3110, 0.7443), "Orc_Post_Large_A6", _folder)
if a: placed += 1
else: skipped += 1

# Construction: Orc_Post_Large_A7
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Wood
#   Volume: EMorSimpleShape::OrientedBox, BoxExtent: (36.3, 38.9, 37.2)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (2470.296, 4410.338, 1200.6697), (0.0, 0.0, -0.0), (0.7266, 0.7779, 0.7443), "Orc_Post_Large_A7", _folder)
if a: placed += 1
else: skipped += 1

# Construction: Orc_Post_Large_A8
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Wood
#   Volume: EMorSimpleShape::OrientedBox, BoxExtent: (39.8, 20.8, 44.8)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (2535.6172, 4438.1914, 1282.8925), (0.0, 0.0, -0.0), (0.7961, 0.4167, 0.8962), "Orc_Post_Large_A8", _folder)
if a: placed += 1
else: skipped += 1

# Construction: Orc_Post_Large_A9
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Wood
#   Volume: EMorSimpleShape::OrientedBox, BoxExtent: (49.8, 6.3, 34.4)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (2548.3137, 4453.7446, 1441.2501), (0.0, 0.0, -0.0), (0.9958, 0.1251, 0.6888), "Orc_Post_Large_A9", _folder)
if a: placed += 1
else: skipped += 1

# Construction: Orc_Scaffolding_Ladder13_1
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Scaffolding
#   Volume: EMorSimpleShape::OrientedBox, BoxExtent: (74.2, 35.6, 271.6)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (3940.3958, 1559.723, 1177.8513), (0.0, 0.0, -0.0), (1.4831, 0.7120, 5.4328), "Orc_Scaffolding_Ladder13_1", _folder)
if a: placed += 1
else: skipped += 1

# Construction: Orc_Scaffolding_Ladder14
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Scaffolding
#   Volume: EMorSimpleShape::OrientedBox, BoxExtent: (71.2, 21.9, 263.8)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (2618.7415, 4738.16, 1193.0415), (0.0, 0.0, -0.0), (1.4245, 0.4383, 5.2762), "Orc_Scaffolding_Ladder14", _folder)
if a: placed += 1
else: skipped += 1

# Construction: Orc_Scaffolding_Ladder15
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Scaffolding
#   Volume: EMorSimpleShape::OrientedBox, BoxExtent: (45.0, 74.4, 222.2)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (1513.1321, 2356.513, 1126.2463), (0.0, 0.0, -0.0), (0.8992, 1.4886, 4.4431), "Orc_Scaffolding_Ladder15", _folder)
if a: placed += 1
else: skipped += 1

# Construction: Orc_Scaffolding_Ladder21_2
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Scaffolding
#   Volume: EMorSimpleShape::OrientedBox, BoxExtent: (35.6, 74.2, 222.2)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (3925.64, 1391.8859, 1532.9927), (0.0, 0.0, -0.0), (0.7120, 1.4831, 4.4431), "Orc_Scaffolding_Ladder21_2", _folder)
if a: placed += 1
else: skipped += 1

# Construction: Orc_Scaffolding_Post_Deco_A4
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Scaffolding
#   Volume: EMorSimpleShape::OrientedBox, BoxExtent: (130.2, 189.2, 112.4)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (4287.196, 2499.0498, 1123.3281), (0.0, 0.0, -0.0), (2.6038, 3.7837, 2.2475), "Orc_Scaffolding_Post_Deco_A4", _folder)
if a: placed += 1
else: skipped += 1

# Construction: Orc_Scaffolding_Support_Post13
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Scaffolding
#   Volume: EMorSimpleShape::OrientedBox, BoxExtent: (203.4, 68.0, 246.9)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (4066.8198, 1428.2272, 1162.8337), (0.0, 0.0, -0.0), (4.0682, 1.3594, 4.9381), "Orc_Scaffolding_Support_Post13", _folder)
if a: placed += 1
else: skipped += 1

# ======================================================================
# PHASE 3: Breakables + DecoVolumes
# ======================================================================
unreal.log(f"[{BUBBLE_NAME}] Phase 3: Placing breakables and deco volumes...")

_folder = "Reconstruction/BD_BB_Chapter5_BrokenSeal/Breakables"

# Breakable Batch 0: BP_Orc_Scaffolding_Post_1m_A (3 instances)
#   BP Class: /Game/LevelDesign/Architecture/Orc/BP_Orc_Scaffolding_Post_1m_A
_brk_mesh = "/Game/Art/Assets/Kits/Deco_Architecture/Orc_Camp/Orc_Scaffolding_Post_1m_A"
_brk_mats = ['/Game/Art/Assets/Kits/Deco_Architecture/Orc_Camp/Materials/MI_Orc_Scaffolding_Poles']
a = spawn_static_mesh(_brk_mesh, _brk_mats, (2505.0, 4410.0, 1485.0), (8.541512245554819e-13, -179.99995901886822, 70.00006109848), (1.0, 1.0, 1.0), "BP_Orc_Scaffolding_Post_1m_A_2", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_brk_mesh, _brk_mats, (3913.5305, 4395.8906, 1595.7736), (8.541512245554819e-13, -179.99995901886822, 70.00006109848), (1.0, 1.0, 1.0), "BP_Orc_Scaffolding_Post_1m_A2", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_brk_mesh, _brk_mats, (4050.4636, 2261.3052, 1490.9922), (4.110255868084532e-06, 53.61931822902289, 70.00008720763992), (1.0, 1.0, 1.0), "BP_Orc_Scaffolding_Post_1m_A3", _folder)
if a: placed += 1
else: skipped += 1

# Breakable Batch 1: BP_Orc_Scaffolding_Post_1m_C (4 instances)
#   BP Class: /Game/LevelDesign/Architecture/Orc/BP_Orc_Scaffolding_Post_1m_C
_brk_mesh = "/Game/Art/Assets/Kits/Deco_Architecture/Orc_Camp/Orc_Scaffolding_Post_1m_C"
_brk_mats = ['/Game/Art/Assets/Kits/Deco_Architecture/Orc_Camp/Materials/MI_Orc_Scaffolding_Poles']
a = spawn_static_mesh(_brk_mesh, _brk_mats, (3017.2285, 1559.4185, 952.83057), (-5.080358306834234e-13, -179.99995901886763, -90.00014890018984), (1.0, 1.0, 1.0), "BP_Orc_Scaffolding_Post_1m_C_2", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_brk_mesh, _brk_mats, (3017.2285, 1570.2378, 1123.8872), (1.920075882081261e-12, -179.99995901886456, -120.00020776496703), (1.0, 1.0, 1.0), "BP_Orc_Scaffolding_Post_1m_C2", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_brk_mesh, _brk_mats, (3334.514, 1559.4185, 979.88574), (-5.080358306834234e-13, -179.99995901886763, -90.00014890018984), (1.0, 1.0, 1.125), "BP_Orc_Scaffolding_Post_1m_C3", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_brk_mesh, _brk_mats, (3322.308, 1552.2041, 1192.6626), (7.063595895395698e-06, 177.20869720981005, -90.00009553495288), (1.0, 1.0, 1.125), "BP_Orc_Scaffolding_Post_1m_C4", _folder)
if a: placed += 1
else: skipped += 1

# Breakable Batch 2: BP_Orc_Scaffolding_Post_1m_D (2 instances)
#   BP Class: /Game/LevelDesign/Architecture/Orc/BP_Orc_Scaffolding_Post_1m_D
_brk_mesh = "/Game/Art/Assets/Kits/Deco_Architecture/Orc_Camp/Orc_Scaffolding_Post_1m_D"
_brk_mats = ['/Game/Art/Assets/Kits/Deco_Architecture/Orc_Camp/Materials/MI_Orc_Scaffolding_Poles']
a = spawn_static_mesh(_brk_mesh, _brk_mats, (3082.9753, 5245.477, 1397.9978), (83.73016135673586, 122.84268885767895, -6.179300451618109e-05), (1.15625, 1.15625, 1.15625), "BP_Orc_Scaffolding_Post_1m_D2_0", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_brk_mesh, _brk_mats, (3055.225, 5147.196, 1397.9978), (-50.71700888960788, 89.99990587144836, 1.8471955804997184e-05), (1.15625, 1.15625, 1.15625), "BP_Orc_Scaffolding_Post_1m_D3_1", _folder)
if a: placed += 1
else: skipped += 1

# Breakable Batch 3: BP_Orc_Scaffolding_Post_2m_C (1 instances)
#   BP Class: /Game/LevelDesign/Architecture/Orc/BP_Orc_Scaffolding_Post_2m_C
_brk_mesh = "/Game/Art/Assets/Kits/Deco_Architecture/Orc_Camp/Orc_Scaffolding_Post_2m_C"
_brk_mats = ['/Game/Art/Assets/Kits/Deco_Architecture/Orc_Camp/Materials/MI_Orc_Scaffolding_Poles']
a = spawn_static_mesh(_brk_mesh, _brk_mats, (3037.8816, 5233.76, 1578.8615), (20.560212791935175, 81.43895469730323, -45.023321575124136), (1.15625, 1.15625, 1.15625), "BP_Orc_Scaffolding_Post_2m_C4_0", _folder)
if a: placed += 1
else: skipped += 1

# Breakable Batch 4: BP_Orc_Scaffolding_Post_2m_D (2 instances)
#   BP Class: /Game/LevelDesign/Architecture/Orc/BP_Orc_Scaffolding_Post_2m_D
_brk_mesh = "/Game/Art/Assets/Kits/Deco_Architecture/Orc_Camp/Orc_Scaffolding_Post_2m_D"
_brk_mats = ['/Game/Art/Assets/Kits/Deco_Architecture/Orc_Camp/Materials/MI_Orc_Scaffolding_Poles']
a = spawn_static_mesh(_brk_mesh, _brk_mats, (3311.812, 5199.227, 1581.8748), (20.77216785277362, 89.99992887920106, 49.390863764037654), (1.15625, 1.15625, 1.15625), "BP_Orc_Scaffolding_Post_2m_D4_0", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_brk_mesh, _brk_mats, (3300.5928, 4972.8936, 1398.6624), (-81.80329416560026, 109.6356945798612, 16.914549357771957), (1.15625, 1.15625, 1.15625), "BP_Orc_Scaffolding_Post_2m_D5_1", _folder)
if a: placed += 1
else: skipped += 1

# Breakable Batch 5: BP_Orc_Scaffolding_Post_3m_C (2 instances)
#   BP Class: /Game/LevelDesign/Architecture/Orc/BP_Orc_Scaffolding_Post_3m_C
_brk_mesh = "/Game/Art/Assets/Kits/Deco_Architecture/Orc_Camp/Orc_Scaffolding_Post_3m_C"
_brk_mats = ['/Game/Art/Assets/Kits/Deco_Architecture/Orc_Camp/Materials/MI_Orc_Scaffolding_Poles']
a = spawn_static_mesh(_brk_mesh, _brk_mats, (4214.906, 2396.0725, 945.0), (0.0, -34.99963324864271, 0.0), (1.0, 1.0, 1.0), "BP_Orc_Scaffolding_Post_3m_C4", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_brk_mesh, _brk_mats, (3040.1938, 5214.2583, 1403.779), (0.0, 89.99992202041271, -0.0), (1.15625, 1.15625, 1.15625), "BP_Orc_Scaffolding_Post_3m_C6_1", _folder)
if a: placed += 1
else: skipped += 1

# Breakable Batch 6: BP_Orc_Scaffolding_Post_3m_d (1 instances)
#   BP Class: /Game/LevelDesign/Architecture/Orc/BP_Orc_Scaffolding_Post_3m_d
_brk_mesh = "/Game/Art/Assets/Kits/Deco_Architecture/Orc_Camp/Orc_Scaffolding_Post_3m_D"
_brk_mats = ['/Game/Art/Assets/Kits/Deco_Architecture/Orc_Camp/Materials/MI_Orc_Scaffolding_Poles']
a = spawn_static_mesh(_brk_mesh, _brk_mats, (3300.35, 5210.7896, 1395.6853), (0.0, 89.99992202041271, -0.0), (1.15625, 1.15625, 1.15625), "BP_Orc_Scaffolding_Post_3m_D_0", _folder)
if a: placed += 1
else: skipped += 1

# Breakable Batch 7: BP_Orc_Scaffolding_Post_4m_A (1 instances)
#   BP Class: /Game/LevelDesign/Architecture/Orc/BP_Orc_Scaffolding_Post_4m_A
_brk_mesh = "/Game/Art/Assets/Kits/Deco_Architecture/Orc_Camp/Orc_Scaffolding_Post_4m_A"
_brk_mats = ['/Game/Art/Assets/Kits/Deco_Architecture/Orc_Camp/Materials/MI_Orc_Scaffolding_Poles']
a = spawn_static_mesh(_brk_mesh, _brk_mats, (3015.908, 1678.584, 799.60986), (0.0, -179.99998633961752, -0.0), (1.9375, 2.28125, 1.125), "BP_Orc_Scaffolding_Post_4m_A_5", _folder)
if a: placed += 1
else: skipped += 1

# Breakable Batch 8: BP_Orc_Scaffolding_Post_4m_B (3 instances)
#   BP Class: /Game/LevelDesign/Architecture/Orc/BP_Orc_Scaffolding_Post_4m_B
_brk_mesh = "/Game/Art/Assets/Kits/Deco_Architecture/Orc_Camp/Orc_Scaffolding_Post_4m_B"
_brk_mats = ['/Game/Art/Assets/Kits/Deco_Architecture/Orc_Camp/Materials/MI_Orc_Scaffolding_Poles']
a = spawn_static_mesh(_brk_mesh, _brk_mats, (4384.9585, 2669.398, 945.0), (0.0, 105.00004236159195, -0.0), (1.0, 1.0, 1.0), "BP_Orc_Scaffolding_Post_4m_B2", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_brk_mesh, _brk_mats, (3335.0723, 1536.8516, 798.1489), (0.0, -179.99998633961752, -0.0), (1.15625, 1.15625, 1.15625), "BP_Orc_Scaffolding_Post_4m_B3_4", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_brk_mesh, _brk_mats, (3335.0723, 1699.6841, 798.146), (0.0, -114.99986316697712, 0.0), (1.15625, 1.15625, 1.15625), "BP_Orc_Scaffolding_Post_4m_B4", _folder)
if a: placed += 1
else: skipped += 1

# Breakable Batch 9: BP_Orc_Scaffolding_Post_5m_D (1 instances)
#   BP Class: /Game/LevelDesign/Architecture/Orc/BP_Orc_Scaffolding_Post_5m_D
_brk_mesh = "/Game/Art/Assets/Kits/Deco_Architecture/Orc_Camp/Orc_Scaffolding_Post_5m_D"
_brk_mats = ['/Game/Art/Assets/Kits/Deco_Architecture/Orc_Camp/Materials/MI_Orc_Scaffolding_Poles']
a = spawn_static_mesh(_brk_mesh, _brk_mats, (3003.6223, 1543.1665, 751.3567), (0.0, -3.051757709276941e-05, 0.0), (1.0, 1.0, 1.0), "BP_Orc_Scaffolding_Post_5m_D_3", _folder)
if a: placed += 1
else: skipped += 1

# Breakable Batch 10: BP_Orc_Scaffolding_Post_Deco_D (1 instances)
#   BP Class: /Game/LevelDesign/Architecture/Orc/BP_Orc_Scaffolding_Post_Deco_D
_brk_mesh = "/Game/Art/Assets/Kits/Deco_Architecture/Orc_Camp/Orc_Scaffolding_Post_Deco_D"
_brk_mats = ['/Game/Art/Assets/Kits/Deco/Orc/Materials/Orc_Lighting/MI_Orc_Lighting', '/Game/Art/Assets/Kits/Deco_Architecture/Orc_Camp/Materials/MI_Orc_Scaffolding_Platforms']
a = spawn_static_mesh(_brk_mesh, _brk_mats, (4373.175, 2605.996, 1125.0), (0.0, 59.99999239245047, -0.0), (1.0, 1.0, 1.0), "BP_Orc_Scaffolding_Post_Deco_D2", _folder)
if a: placed += 1
else: skipped += 1

# Breakable Batch 11: BP_DM_Defiled_Statues_H_A_Deco_Breakable (1 instances)
#   BP Class: /Game/LevelDesign/Deco/Defiled/BP_DM_Defiled_Statues_H_A_Deco_Breakable
_brk_mesh = "/Game/Art/Assets/Kits/Deco/Defiled/Defiled_Statues_H_A_Deco"
_brk_mats = ['/Game/Art/Assets/Kits/Deco/Orc/Materials/Orc_Lighting/MI_Orc_Lighting']
a = spawn_static_mesh(_brk_mesh, _brk_mats, (1234.7031, 3206.8645, 1437.1978), (0.0, 170.00004533427662, -0.0), (1.0, 1.0, 1.0), "BP_DM_Defiled_Statues_H_A_Deco_Breakable2", _folder)
if a: placed += 1
else: skipped += 1

# Breakable Batch 12: BP_DM_Mines_Machine_Whim_Boar_PullBar_Broken (1 instances)
#   BP Class: /Game/LevelDesign/Deco/MinesDressing/BP_DM_Mines_Machine_Whim_Boar_PullBar_Broken
_brk_mesh = "/Game/Art/Assets/Kits/Deco/Mines/Machine/Mines_Machine_Whim_Pieces/Mines_Machine_Whim_Boar_PullBar_Broken"
_brk_mats = ['/Game/Art/Assets/Kits/Deco/Mines/Materials/Mines_Machine_Whim/MI_Mines_Machine_Whim_Uniq', '/Game/Art/Assets/Kits/Deco/Mines/Materials/Mines_Machine_Whim/MI_Mines_Machine_Whim_Trim']
a = spawn_static_mesh(_brk_mesh, _brk_mats, (3249.0696, 5078.599, 1393.3728), (0.0, -100.7815580551229, -0.0), (1.15625, 1.15625, 1.15625), "BP_DM_Mines_Machine_Whim_Boar_PullBar_Broken2_0", _folder)
if a: placed += 1
else: skipped += 1

# Breakable Batch 13: BP_DM_Mines_Machine_Whim_Rope_Bracket_Broken (1 instances)
#   BP Class: /Game/LevelDesign/Deco/MinesDressing/BP_DM_Mines_Machine_Whim_Rope_Bracket_Broken
_brk_mesh = "/Game/Art/Assets/Kits/Deco/Mines/Machine/Mines_Machine_Whim_Pieces/Mines_Machine_Whim_Rope_Bracket_Broken_A"
_brk_mats = ['/Game/Art/Assets/Kits/Deco/Mines/Materials/Mines_Machine_Whim/MI_Mines_Machine_Whim_Trim', '/Game/Art/Assets/Kits/Deco/Mines/Materials/Mines_Machine_Whim/MI_Mines_Machine_Whim_Uniq']
a = spawn_static_mesh(_brk_mesh, _brk_mats, (3061.0066, 5232.7583, 1393.3728), (0.0, 114.0746110932137, -0.0), (1.15625, 1.15625, 1.15625), "BP_DM_Mines_Machine_Whim_Rope_Bracket_Broken_0", _folder)
if a: placed += 1
else: skipped += 1

# Breakable Batch 14: BP_DM_Mines_Machine_Whim_Rope_Support_Broken_B (1 instances)
#   BP Class: /Game/LevelDesign/Deco/MinesDressing/BP_DM_Mines_Machine_Whim_Rope_Support_Broken_B
_brk_mesh = "/Game/Art/Assets/Kits/Deco/Mines/Machine/Mines_Machine_Whim_Pieces/Mines_Machine_Whim_Rope_Support_Broken_B"
_brk_mats = ['/Game/Art/Assets/Kits/Deco/Mines/Materials/Mines_Machine_Whim/MI_Mines_Machine_Whim_Trim', '/Game/Art/Assets/Kits/Deco/Mines/Materials/Mines_Machine_Whim/MI_Mines_Machine_Whim_Uniq']
a = spawn_static_mesh(_brk_mesh, _brk_mats, (3300.35, 5183.0396, 1393.3728), (15.68175247838773, 134.70930916984645, 66.21006097589598), (1.15625, 1.15625, 1.15625), "BP_DM_Mines_Machine_Whim_Rope_Support_Broken_B2_0", _folder)
if a: placed += 1
else: skipped += 1

# Breakable Batch 15: BP_DM_Workshop_Scatter_Rope_E_Breakable (1 instances)
#   BP Class: /Game/LevelDesign/Deco/Urban/Workshop/BP_DM_Workshop_Scatter_Rope_E_Breakable
_brk_mesh = "/Game/Art/Assets/Kits/Deco/Urban/Workshop/Scatter/Workshop_Scatter_Rope_E"
_brk_mats = ['/Game/Art/Assets/Kits/Deco_Architecture/Mines/Materials/Mines_Scaffolding/MI_Mines_Scaffolding_Rope_A']
a = spawn_static_mesh(_brk_mesh, _brk_mats, (4865.116, 3842.1753, 943.33276), (-0.0, -179.9999795094293, -0.0), (1.0, 1.0, 1.0), "BP_DM_Workshop_Scatter_Rope_E_Breakable_0", _folder)
if a: placed += 1
else: skipped += 1

# Breakable Batch 16: BP_DM_Workshop_Scatter_Rope_H_Breakable (1 instances)
#   BP Class: /Game/LevelDesign/Deco/Urban/Workshop/BP_DM_Workshop_Scatter_Rope_H_Breakable
_brk_mesh = "/Game/Art/Assets/Kits/Deco/Urban/Workshop/Scatter/Workshop_Scatter_Rope_H"
_brk_mats = ['/Game/Art/Assets/Kits/Deco_Architecture/Mines/Materials/Mines_Scaffolding/MI_Mines_Scaffolding_Rope_A']
a = spawn_static_mesh(_brk_mesh, _brk_mats, (4844.116, 3722.1753, 948.33276), (-0.0, -169.99982021904918, -0.0), (1.0, 1.0, 1.0), "BP_DM_Workshop_Scatter_Rope_H_Breakable_0", _folder)
if a: placed += 1
else: skipped += 1

# Breakable Batch 17: Suburbs_Dirt_Mound_A_Blueprint (1 instances)
#   BP Class: /Game/LevelDesign/Deco_Architecture/Mounds/Suburbs_Dirt_Mound_A_Blueprint
_brk_mesh = "/Game/Art/Assets/Kits/Misc/Dirt_Mounds/Suburbs_Dirt_Mound_A"
_brk_mats = ['/Game/Art/Assets/Kits/Misc/Dirt_Mounds/Materials/Suburbs_Dirt_Inst']
a = spawn_static_mesh(_brk_mesh, _brk_mats, (3187.0376, 5112.5083, 1397.9978), (0.0, 57.608623037026305, -0.0), (1.9540582, 1.9540582, 0.98272926), "Suburbs_Dirt_Mound_A_Blueprint8_0", _folder)
if a: placed += 1
else: skipped += 1

# Breakable Batch 18: Suburbs_Dirt_Mound_B_Blueprint (1 instances)
#   BP Class: /Game/LevelDesign/Deco_Architecture/Mounds/Suburbs_Dirt_Mound_B_Blueprint
_brk_mesh = "/Game/Art/Assets/Kits/Misc/Dirt_Mounds/Suburbs_Dirt_Mound_B"
_brk_mats = ['/Game/Art/Assets/Kits/Misc/Dirt_Mounds/Materials/Suburbs_Dirt_Inst']
a = spawn_static_mesh(_brk_mesh, _brk_mats, (3087.6, 5207.321, 1393.3728), (0.0, 89.99992202041271, -0.0), (1.15625, 1.15625, 1.15625), "Suburbs_Dirt_Mound_B_Blueprint5_0", _folder)
if a: placed += 1
else: skipped += 1

# --- Extra DecoVolumes (not construction blocks) ---
_folder = "Reconstruction/BD_BB_Chapter5_BrokenSeal/DecoVolumes"

# DecoVolume: AB_Orc_Scaffolding_Storage_2x2x3m_B_5 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (2539.7288, 1601.7327, 1070.5037), (0.0, 0.0, -0.0), (2.6998, 2.8973, 3.4250), "DV_AB_Orc_Scaffolding_Storage_2x2x3m_B_5_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_DM_Deco_Orc_3x3_B_Breakable_0 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (1510.3905, 5479.035, 846.5797), (0.0, 0.0, -0.0), (4.3829, 4.0437, 1.8710), "DV_BP_DM_Deco_Orc_3x3_B_Breakable_0_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_DM_Deco_Orc_3x3_B_Breakable2_6 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (5633.286, 3761.274, 852.27826), (0.0, 0.0, -0.0), (3.7833, 4.2044, 1.9376), "DV_BP_DM_Deco_Orc_3x3_B_Breakable2_6_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_DM_Deco_Orc_Banner_3x3_A_Breakable_2 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (4727.9043, 4617.1045, 1220.5967), (0.0, 0.0, -0.0), (3.7650, 3.9011, 6.5588), "DV_BP_DM_Deco_Orc_Banner_3x3_A_Breakable_2_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_DM_Deco_Orc_Banner_3x3_A_Breakable2_2 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (3790.7314, 1673.0071, 1242.0234), (0.0, 0.0, -0.0), (3.1495, 3.3034, 6.5588), "DV_BP_DM_Deco_Orc_Banner_3x3_A_Breakable2_2_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_DM_Defiled_Statues_H_A_Deco_Breakable2 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (1196.3182, 3204.618, 1715.5627), (0.0, 0.0, -0.0), (2.7534, 2.7406, 6.8974), "DV_BP_DM_Defiled_Statues_H_A_Deco_Breakable2_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_DM_Mines_Lift_Barrel_A_Breakable12_0 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (4913.116, 3840.1753, 998.33276), (0.0, 0.0, -0.0), (0.8390, 0.8390, 1.0146), "DV_BP_DM_Mines_Lift_Barrel_A_Breakable12_0_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_DM_Mines_Lift_Barrel_A_Breakable14_8 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (2551.2441, 1560.8081, 1001.1582), (0.0, 0.0, -0.0), (0.9216, 0.9216, 1.0146), "DV_BP_DM_Mines_Lift_Barrel_A_Breakable14_8_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_DM_Mines_Machine_Whim_Boar_PullBar_Broken2_0 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (3259.7502, 5080.2715, 1390.6598), (0.0, 0.0, -0.0), (0.9501, 0.3414, 0.0966), "DV_BP_DM_Mines_Machine_Whim_Boar_PullBar_Broken2_0_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_DM_Mines_Machine_Whim_Rope_Bracket_Broken_0 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (3098.2207, 5145.8525, 1402.9274), (0.0, 0.0, -0.0), (1.1123, 1.9021, 0.1907), "DV_BP_DM_Mines_Machine_Whim_Rope_Bracket_Broken_0_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_DM_Mines_Machine_Whim_Rope_Support_Broken_B2_0 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (3206.1113, 5203.0684, 1391.4227), (0.0, 0.0, -0.0), (2.2838, 2.1639, 1.6906), "DV_BP_DM_Mines_Machine_Whim_Rope_Support_Broken_B2_0_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_DM_Orc_Flag3_0 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (3172.9165, 5150.1553, 1747.791), (0.0, 0.0, -0.0), (2.3475, 1.9558, 7.4516), "DV_BP_DM_Orc_Flag3_0_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_DM_Warehouse_Crate_A_Breakable10_1 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (1505.7114, 5356.6055, 833.6741), (0.0, 0.0, -0.0), (0.9490, 0.9456, 0.7555), "DV_BP_DM_Warehouse_Crate_A_Breakable10_1_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_DM_Warehouse_Crate_A_Breakable36_6 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (4750.022, 3680.5398, 984.00684), (0.0, 0.0, -0.0), (1.0299, 1.0318, 0.7555), "DV_BP_DM_Warehouse_Crate_A_Breakable36_6_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_DM_Warehouse_Crate_A_Breakable38_7 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (4744.6836, 3812.133, 989.00684), (0.0, 0.0, -0.0), (1.0041, 1.0016, 0.7555), "DV_BP_DM_Warehouse_Crate_A_Breakable38_7_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_DM_Warehouse_Crate_A_Breakable43_8 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (4891.7534, 3661.276, 982.00684), (0.0, 0.0, -0.0), (0.7573, 0.7520, 0.7555), "DV_BP_DM_Warehouse_Crate_A_Breakable43_8_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_DM_Warehouse_Crate_A_open_Breakable5_0 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (1564.0463, 5480.8203, 866.27606), (0.0, 0.0, -0.0), (0.8824, 0.8327, 0.8854), "DV_BP_DM_Warehouse_Crate_A_open_Breakable5_0_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_DM_Warehouse_Crate_A_open_Breakable6_0 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (4881.036, 3659.138, 1053.3263), (0.0, 0.0, -0.0), (0.9983, 0.9974, 0.6938), "DV_BP_DM_Warehouse_Crate_A_open_Breakable6_0_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_DM_Warehouse_Crate_A_open_Breakable7_1 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (4727.044, 3792.2258, 1081.3263), (0.0, 0.0, -0.0), (1.0460, 1.0456, 0.6938), "DV_BP_DM_Warehouse_Crate_A_open_Breakable7_1_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_DM_Warehouse_Crate_A_open_Breakable8_9 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (2581.6636, 1646.2434, 986.15173), (0.0, 0.0, -0.0), (0.8942, 0.8929, 0.6938), "DV_BP_DM_Warehouse_Crate_A_open_Breakable8_9_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_DM_Warehouse_Crate_A_open_Breakable9 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (2497.7727, 1614.2803, 1139.1582), (0.0, 0.0, -0.0), (0.8048, 0.7517, 0.7500), "DV_BP_DM_Warehouse_Crate_A_open_Breakable9_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_DM_Warren_Lighting_Torch_Breakable_2 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (1426.803, 4131.7046, 1052.5), (0.0, 0.0, -0.0), (1.0112, 1.0765, 1.9128), "DV_BP_DM_Warren_Lighting_Torch_Breakable_2_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_DM_Warren_Lighting_Torch_Breakable10 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (4627.1377, 2951.4185, 1247.5), (0.0, 0.0, -0.0), (1.1606, 1.1011, 1.9128), "DV_BP_DM_Warren_Lighting_Torch_Breakable10_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_DM_Warren_Lighting_Torch_Breakable2 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (2701.803, 4471.7046, 997.5), (0.0, 0.0, -0.0), (1.0112, 1.0765, 1.9128), "DV_BP_DM_Warren_Lighting_Torch_Breakable2_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_DM_Warren_Lighting_Torch_Breakable3 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (3671.803, 2026.7045, 997.5), (0.0, 0.0, -0.0), (1.0112, 1.0765, 1.9128), "DV_BP_DM_Warren_Lighting_Torch_Breakable3_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_DM_Warren_Lighting_Torch_Breakable4 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (2696.803, 2026.7045, 997.5), (0.0, 0.0, -0.0), (1.0112, 1.0765, 1.9128), "DV_BP_DM_Warren_Lighting_Torch_Breakable4_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_DM_Warren_Lighting_Torch_Breakable5_6 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (2876.803, 5431.7046, 1452.5), (0.0, 0.0, -0.0), (1.0112, 1.0765, 1.9128), "DV_BP_DM_Warren_Lighting_Torch_Breakable5_6_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_DM_Warren_Lighting_Torch_Breakable6 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (4626.8027, 3451.7046, 1247.5), (0.0, 0.0, -0.0), (1.0112, 1.0765, 1.9128), "DV_BP_DM_Warren_Lighting_Torch_Breakable6_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_DM_Warren_Lighting_Torch_Breakable7 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (4376.8027, 5231.7046, 1452.5), (0.0, 0.0, -0.0), (1.0112, 1.0765, 1.9128), "DV_BP_DM_Warren_Lighting_Torch_Breakable7_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_DM_Warren_Lighting_Torch_Breakable8 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (3426.803, 981.70447, 1452.5), (0.0, 0.0, -0.0), (1.0112, 1.0765, 1.9128), "DV_BP_DM_Warren_Lighting_Torch_Breakable8_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_DM_Warren_Lighting_Torch_Breakable9 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (3677.4443, 4470.6543, 997.5), (0.0, 0.0, -0.0), (1.2358, 1.1827, 1.9128), "DV_BP_DM_Warren_Lighting_Torch_Breakable9_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_DM_Workshop_Barrel_Broken_Breakable_5 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (4684.859, 4749.84, 983.9401), (0.0, 0.0, -0.0), (0.8004, 1.0134, 0.9287), "DV_BP_DM_Workshop_Barrel_Broken_Breakable_5_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_DM_Workshop_Scatter_Bucket_Wood_Breakable7_0 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (3182.5835, 5012.0356, 1408.085), (0.0, 0.0, -0.0), (0.9932, 0.9913, 0.7093), "DV_BP_DM_Workshop_Scatter_Bucket_Wood_Breakable7_0_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_DM_Workshop_Scatter_Rope_E_Breakable_0 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (4862.773, 3837.5496, 953.3448), (0.0, 0.0, -0.0), (0.5356, 0.4805, 0.2075), "DV_BP_DM_Workshop_Scatter_Rope_E_Breakable_0_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_DM_Workshop_Scatter_Rope_H_Breakable_0 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (4854.588, 3726.494, 964.4568), (0.0, 0.0, -0.0), (0.9702, 0.8419, 0.3567), "DV_BP_DM_Workshop_Scatter_Rope_H_Breakable_0_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_DM_Workshop_Scatter_Sandbags_B_Breakable2_10 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (2564.0933, 1668.4907, 1121.361), (0.0, 0.0, -0.0), (1.3548, 1.3475, 0.4049), "DV_BP_DM_Workshop_Scatter_Sandbags_B_Breakable2_10_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_DM_Workshop_Scatter_Sandbags_C_Breakable3_0 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (4795.0137, 3788.285, 985.3224), (0.0, 0.0, -0.0), (1.0316, 0.8772, 0.9998), "DV_BP_DM_Workshop_Scatter_Sandbags_C_Breakable3_0_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_DM_Workshop_Scatter_Sandbags_C_Breakable4_9 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (2526.4788, 1639.2704, 982.61847), (0.0, 0.0, -0.0), (0.9102, 0.7528, 1.0682), "DV_BP_DM_Workshop_Scatter_Sandbags_C_Breakable4_9_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_DM_Workshop_Scatter_Sandbags_D_Breakable2_0 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (4769.413, 3763.1016, 1083.6464), (0.0, 0.0, -0.0), (0.7105, 0.7490, 0.8731), "DV_BP_DM_Workshop_Scatter_Sandbags_D_Breakable2_0_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_DM_Workshop_Scatter_Sandbags_D_Breakable3_1 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (4766.3696, 3631.5134, 1060.0148), (0.0, 0.0, -0.0), (0.9681, 0.8785, 0.3816), "DV_BP_DM_Workshop_Scatter_Sandbags_D_Breakable3_1_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_Orc_Barricade_Palisade_Barricade_B12 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (1406.7434, 3189.3901, 1450.2166), (0.0, 0.0, -0.0), (1.6389, 3.8386, 2.1414), "DV_BP_Orc_Barricade_Palisade_Barricade_B12_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_Orc_Scaffolding_Post_1m_A_2 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (2501.9727, 4356.6626, 1504.4728), (0.0, 0.0, -0.0), (0.2310, 1.1214, 0.5596), "DV_BP_Orc_Scaffolding_Post_1m_A_2_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_Orc_Scaffolding_Post_1m_A2 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (3910.5032, 4342.553, 1615.2463), (0.0, 0.0, -0.0), (0.2310, 1.1214, 0.5596), "DV_BP_Orc_Scaffolding_Post_1m_A2_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_Orc_Scaffolding_Post_1m_A3 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (4009.3176, 2295.3796, 1510.465), (0.0, 0.0, -0.0), (1.0399, 0.8512, 0.5596), "DV_BP_Orc_Scaffolding_Post_1m_A3_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_Orc_Scaffolding_Post_1m_C_2 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (3017.222, 1612.7795, 952.75775), (0.0, 0.0, -0.0), (0.3426, 1.5481, 0.1558), "DV_BP_Orc_Scaffolding_Post_1m_C_2_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_Orc_Scaffolding_Post_1m_C2 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (3017.222, 1616.4133, 1097.1436), (0.0, 0.0, -0.0), (0.3426, 1.4186, 0.9089), "DV_BP_Orc_Scaffolding_Post_1m_C2_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_Orc_Scaffolding_Post_1m_C3 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (3334.5073, 1619.4497, 979.81287), (0.0, 0.0, -0.0), (0.3426, 1.7416, 0.1558), "DV_BP_Orc_Scaffolding_Post_1m_C3_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_Orc_Scaffolding_Post_1m_C4 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (3325.2249, 1612.1644, 1192.5898), (0.0, 0.0, -0.0), (0.4270, 1.7562, 0.1558), "DV_BP_Orc_Scaffolding_Post_1m_C4_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_Orc_Scaffolding_Post_1m_D2_0 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (3116.1445, 5193.0425, 1405.2556), (0.0, 0.0, -0.0), (0.8626, 1.1741, 0.2621), "DV_BP_Orc_Scaffolding_Post_1m_D2_0_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_Orc_Scaffolding_Post_1m_D3_1 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (3054.6555, 5195.8223, 1437.2073), (0.0, 0.0, -0.0), (0.2137, 1.0498, 0.8910), "DV_BP_Orc_Scaffolding_Post_1m_D3_1_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_Orc_Scaffolding_Post_2m_C4_0 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (3116.8337, 5177.062, 1657.5878), (0.0, 0.0, -0.0), (1.9528, 1.3403, 2.0235), "DV_BP_Orc_Scaffolding_Post_2m_C4_0_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_Orc_Scaffolding_Post_2m_D4_0 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (3218.3992, 5173.1924, 1660.5096), (0.0, 0.0, -0.0), (2.0925, 1.1013, 1.9082), "DV_BP_Orc_Scaffolding_Post_2m_D4_0_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_Orc_Scaffolding_Post_2m_D5_1 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (3228.15, 5073.6626, 1412.2574), (0.0, 0.0, -0.0), (1.7552, 2.2224, 0.8172), "DV_BP_Orc_Scaffolding_Post_2m_D5_1_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_Orc_Scaffolding_Post_3m_C4 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (4218.229, 2394.769, 1099.2614), (0.0, 0.0, -0.0), (0.3789, 0.3538, 3.1467), "DV_BP_Orc_Scaffolding_Post_3m_C4_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_Orc_Scaffolding_Post_3m_C6_1 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (3039.2246, 5218.2705, 1582.1437), (0.0, 0.0, -0.0), (0.2450, 0.3633, 3.6383), "DV_BP_Orc_Scaffolding_Post_3m_C6_1_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_Orc_Scaffolding_Post_3m_D_0 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (3297.6543, 5206.969, 1556.5253), (0.0, 0.0, -0.0), (0.4255, 0.6738, 3.6983), "DV_BP_Orc_Scaffolding_Post_3m_D_0_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_Orc_Scaffolding_Post_4m_A_5 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (3013.4766, 1675.5636, 1018.5103), (0.0, 0.0, -0.0), (0.3114, 0.3360, 4.9288), "DV_BP_Orc_Scaffolding_Post_4m_A_5_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_Orc_Scaffolding_Post_4m_B2 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (4382.048, 2674.408, 1136.6936), (0.0, 0.0, -0.0), (0.2774, 0.3412, 4.4713), "DV_BP_Orc_Scaffolding_Post_4m_B2_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_Orc_Scaffolding_Post_4m_B3_4 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (3328.6057, 1535.1, 1019.7947), (0.0, 0.0, -0.0), (0.3442, 0.2398, 5.1699), "DV_BP_Orc_Scaffolding_Post_4m_B3_4_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_Orc_Scaffolding_Post_4m_B4 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (3333.9268, 1693.0831, 1019.79175), (0.0, 0.0, -0.0), (0.3628, 0.4133, 5.1699), "DV_BP_Orc_Scaffolding_Post_4m_B4_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_Orc_Scaffolding_Post_5m_D_3 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (3028.9844, 1552.278, 1013.1951), (0.0, 0.0, -0.0), (1.4372, 0.4808, 5.3787), "DV_BP_Orc_Scaffolding_Post_5m_D_3_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_Orc_Scaffolding_Post_Deco_D2 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (4368.268, 2617.1204, 1137.5482), (0.0, 0.0, -0.0), (1.5983, 2.1814, 1.8793), "DV_BP_Orc_Scaffolding_Post_Deco_D2_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: CBP_Repairable_StoryStone_WellofShadow_2 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (1132.4785, 1140.6978, 950.0017), (-0.0, -45.000120586048595, -0.0), (2.0000, 2.0000, 3.2482), "DV_CBP_Repairable_StoryStone_WellofShadow_2", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: DecoBlockingVolume1 (EMorSimpleShape::Empty)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (4921.7803, 1306.7009, 1100.0), (0.0, 129.37502650612197, -0.0), (2.0000, 2.0000, 2.0000), "DV_DecoBlockingVolume1", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: DecoBlockingVolume9 (EMorSimpleShape::Empty)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (3143.9663, 3170.5059, 989.14795), (-0.0, -92.20684981583845, -0.0), (2.0000, 2.0000, 2.0000), "DV_DecoBlockingVolume9", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: DecorationBlockingVolume_1 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (5146.777, 3242.106, 945.00885), (0.0, 0.0, -0.0), (2.0000, 2.0000, 2.0000), "DV_DecorationBlockingVolume_1", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: DecorationBlockingVolume_2 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (3221.3352, 5977.7695, 940.6006), (0.0, -179.99998633961752, -0.0), (2.0000, 2.0000, 2.0000), "DV_DecorationBlockingVolume_2", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: DecorationBlockingVolume3 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (3450.877, 4635.807, 877.3261), (0.0, -179.99998633961752, -0.0), (2.0000, 2.0000, 2.0000), "DV_DecorationBlockingVolume3", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: DecorationBlockingVolume4 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (2859.19, 4635.8325, 877.3261), (0.0, -179.99998633961752, -0.0), (2.0000, 2.0000, 2.0000), "DV_DecorationBlockingVolume4", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: Orc_Palissade_Barricade_A10_16 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (1594.7605, 3065.9438, 982.1218), (0.0, 0.0, -0.0), (1.5157, 3.7911, 2.1414), "DV_Orc_Palissade_Barricade_A10_16_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: Orc_Palissade_Barricade_A12 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (1594.7576, 3380.9429, 980.9741), (0.0, 0.0, -0.0), (1.5157, 3.7911, 2.1414), "DV_Orc_Palissade_Barricade_A12_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: Orc_Palissade_Barricade_A4_15 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (4787.181, 4487.279, 933.9009), (0.0, 0.0, -0.0), (4.0159, 4.1484, 2.5129), "DV_Orc_Palissade_Barricade_A4_15_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: RockBlockingVolume0 (EMorSimpleShape::Empty)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (5966.547, 3206.1475, 1081.3633), (0.0, -179.99998633961752, -0.0), (2.0000, 2.0000, 2.0000), "DV_RockBlockingVolume0", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: RockBlockingVolume1 (EMorSimpleShape::Empty)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (4990.064, 1223.4978, 1100.0), (0.0, 129.37502650612197, -0.0), (2.0000, 2.0000, 2.0000), "DV_RockBlockingVolume1", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: RockBlockingVolume10 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (2163.202, 796.7312, 1157.5005), (0.0, 157.50001379721112, -0.0), (2.0000, 2.0000, 2.0000), "DV_RockBlockingVolume10", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: RockBlockingVolume11 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (4768.2524, 1045.165, 1154.0339), (-0.0, -140.62501818853673, -0.0), (2.0000, 2.0000, 2.0000), "DV_RockBlockingVolume11", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: RockBlockingVolume12 (EMorSimpleShape::Empty)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (6211.547, 3206.1475, 1361.3633), (0.0, -179.99998633961752, -0.0), (2.0000, 2.0000, 2.0000), "DV_RockBlockingVolume12", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: RockBlockingVolume12_1 (EMorSimpleShape::Empty)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (4027.0688, 838.5991, 1100.0), (0.0, 106.87507845526758, -0.0), (2.0000, 2.0000, 2.0000), "DV_RockBlockingVolume12_1", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: RockBlockingVolume13 (EMorSimpleShape::Empty)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (3204.2239, 616.8457, 1100.0), (0.0, 90.00007597449323, -0.0), (2.0000, 2.0000, 2.0000), "DV_RockBlockingVolume13", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: RockBlockingVolume14 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (1665.2056, 1655.6555, 907.87585), (0.0, 130.5993509204427, -0.0), (2.0000, 2.0000, 2.0000), "DV_RockBlockingVolume14", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: RockBlockingVolume15 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (1640.9764, 4778.187, 907.87585), (0.0, 50.149031234978786, -0.0), (2.0000, 2.0000, 2.0000), "DV_RockBlockingVolume15", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: RockBlockingVolume2 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (3189.753, 452.76367, 953.0857), (-0.0, -91.3149939643166, -0.0), (2.0000, 2.0000, 2.0000), "DV_RockBlockingVolume2", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: RockBlockingVolume3 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (3178.229, 563.8096, 1313.0989), (0.0, -179.99998633961752, -0.0), (2.0000, 2.0000, 2.0000), "DV_RockBlockingVolume3", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: RockBlockingVolume4 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (3738.2773, 5663.5435, 1163.0989), (-0.0, -103.45983751993613, -0.0), (2.0000, 2.0000, 2.0000), "DV_RockBlockingVolume4", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: RockBlockingVolume5 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (572.041, 3215.0051, 1142.7261), (-0.0, -91.62298465582101, -0.0), (2.0000, 2.0000, 2.0000), "DV_RockBlockingVolume5", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: RockBlockingVolume6 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (718.26904, 4184.777, 1081.708), (0.0, 157.8536712640787, -0.0), (2.0000, 2.0000, 2.0000), "DV_RockBlockingVolume6", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: RockBlockingVolume7 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (776.118, 2228.7507, 1140.8362), (0.0, 117.18746939518505, -0.0), (2.0000, 2.0000, 2.0000), "DV_RockBlockingVolume7", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: RockBlockingVolume8 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (5124.5986, 5175.2617, 1116.9087), (0.0, 129.37495229820811, -0.0), (2.0000, 2.0000, 2.0000), "DV_RockBlockingVolume8", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: RockBlockingVolume9 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (2307.208, 5577.231, 1174.9458), (0.0, 20.501327140354274, -0.0), (14.6005, 8.0421, 11.2136), "DV_RockBlockingVolume9", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: Suburbs_Dirt_Mound_A_Blueprint8_0 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (3169.116, 5086.392, 1405.368), (0.0, 0.0, -0.0), (4.5184, 4.8093, 0.2697), "DV_Suburbs_Dirt_Mound_A_Blueprint8_0_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: Suburbs_Dirt_Mound_B_Blueprint5_0 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (3080.9204, 5188.932, 1399.8933), (0.0, 0.0, -0.0), (1.4305, 1.6220, 0.1406), "DV_Suburbs_Dirt_Mound_B_Blueprint5_0_BRK", _folder)
if a: placed += 1
else: skipped += 1

# ======================================================================
# SUMMARY
# ======================================================================
unreal.log(f"[{BUBBLE_NAME}] Reconstruction complete: {placed} placed, {skipped} skipped, {errors} errors")
