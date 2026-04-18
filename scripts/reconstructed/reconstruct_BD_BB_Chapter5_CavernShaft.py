"""Auto-generated level reconstruction script.
Bubble: BD_BB_Chapter5_CavernShaft
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

BUBBLE_NAME = "BD_BB_Chapter5_CavernShaft"
placed = 0
skipped = 0
errors = 0

# ======================================================================
# PHASE 1: InstancedMeshCatalog  (static mesh placement)
# ======================================================================
unreal.log(f"[{BUBBLE_NAME}] Phase 1: Placing static meshes...")

# Batch 0: StaticMesh'Cube' (9 instances)
_mesh_path = "/Engine/BasicShapes/Cube"
_materials = ['/Game/Unshippable/WhiteboxMaterials/MI_WB_Grid_DarkGrey']
_folder = "Reconstruction/BD_BB_Chapter5_CavernShaft/Meshes"
a = spawn_static_mesh(_mesh_path, _materials, (3199.9998, 6400.0, 1600.0), (0.0, -179.99998633961752, -0.0), (64.0, 1.0, 32.0), "Cube10", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (6399.998, 3200.0002, 8000.0), (0.0, 90.0000030488508, -0.0), (64.0, 1.0, 32.0), "Cube2", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (0.0, 3199.9998, 4800.0), (0.0, 90.0000030488508, -0.0), (64.0, 1.0, 32.0), "Cube3", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (0.0, 3199.9998, 8000.0), (0.0, 90.0000030488508, -0.0), (64.0, 1.0, 32.0), "Cube4", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3200.0002, 0.0, 4800.0), (0.0, -179.99998633961752, -0.0), (64.0, 1.0, 32.0), "Cube5", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3200.0002, 0.0, 8000.0), (0.0, -179.99998633961752, -0.0), (64.0, 1.0, 32.0), "Cube6", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3200.0002, 0.0, 1600.0), (0.0, -179.99998633961752, -0.0), (64.0, 1.0, 32.0), "Cube7", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3199.9998, 6400.0, 4800.0), (0.0, -179.99998633961752, -0.0), (64.0, 1.0, 32.0), "Cube8", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3199.9998, 6400.0, 8000.0), (0.0, -179.99998633961752, -0.0), (64.0, 1.0, 32.0), "Cube9", _folder)
if a: placed += 1
else: skipped += 1

# Batch 1: StaticMesh'Cube' (4 instances)
_mesh_path = "/Engine/BasicShapes/Cube"
_materials = ['/Game/Environments/ProcTexturing/ProcMaterial_Quarry_Atlas_A']
_folder = "Reconstruction/BD_BB_Chapter5_CavernShaft/Meshes"
a = spawn_static_mesh(_mesh_path, _materials, (1147.7827, 3767.002, 6418.0), (0.0, -50.000125382845866, 0.0), (7.5, 7.75, 0.75), "Cube11_5", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5094.0, 1109.0, 5603.0), (0.0, 130.00004372587597, -0.0), (8.0, 7.5, 1.0), "Cube12", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1461.0, 1515.0, 7067.0), (0.0, 120.00004894605553, -0.0), (8.5, 8.75, 1.0), "Cube13", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4907.0, 5211.0, 7191.0), (0.0, 90.0000030488508, -0.0), (9.0, 7.0, 1.0), "Cube18", _folder)
if a: placed += 1
else: skipped += 1

# Batch 2: StaticMesh'Cube' (1 instances)
_mesh_path = "/Engine/BasicShapes/Cube"
_materials = ['/Game/Environments/ProcTexturing/ProcMaterial_Quarry_Ceilling_Fissure_8x8']
_folder = "Reconstruction/BD_BB_Chapter5_CavernShaft/Meshes"
a = spawn_static_mesh(_mesh_path, _materials, (3199.9995, 3200.002, 9400.0), (0.0, 90.0000030488508, -0.0), (64.0, 64.0, 2.021348), "staticMeshFloor2", _folder)
if a: placed += 1
else: skipped += 1

# Batch 3: StaticMesh'Deep_BoneHoard_E' (15 instances)
_mesh_path = "/Game/Art/Assets/Kits/Architecture/Deep/Deep_BoneHoard_E"
_materials = ['/Game/Art/Assets/Kits/Misc/Dirt_Mounds/Materials/MI_DirtMound_Mines']
_folder = "Reconstruction/BD_BB_Chapter5_CavernShaft/Meshes"
a = spawn_static_mesh(_mesh_path, _materials, (1922.9434, 2180.934, 800.0), (0.0, 21.566084339159136, -0.0), (1.0, 1.0, 1.0), "Deep_BoneHoard_E_258", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3732.2515, 5351.189, 804.12805), (0.0, -107.6154252392431, 0.0), (1.0, 1.0, 1.4123731), "Deep_BoneHoard_E11", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4854.329, 2192.0625, 805.0), (0.0, -31.487123662190097, 0.0), (1.0, 1.0, 1.599609), "Deep_BoneHoard_E12", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4423.9233, 1872.3304, 805.0), (0.0, -26.026307521728487, 0.0), (1.0, 1.0, 2.010011), "Deep_BoneHoard_E13", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3503.5134, 1611.0901, 805.0), (0.0, -56.63442728378231, 0.0), (1.0, 1.0, 1.599609), "Deep_BoneHoard_E14", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1521.2384, 1641.6152, 802.27246), (0.0, 44.8495482750572, -0.0), (1.0, 1.0, 2.1828353), "Deep_BoneHoard_E15", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5677.018, 1618.5243, 850.0), (0.0, 137.93264170569756, -0.0), (1.0, 1.0, 1.599609), "Deep_BoneHoard_E17_320", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (6013.5576, 1531.4497, 850.0), (0.0, 51.029497717746686, -0.0), (1.0, 1.0, 1.599609), "Deep_BoneHoard_E18_322", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2369.062, 1842.7261, 805.0), (0.0, 78.26349334589507, -0.0), (1.0, 1.0, 1.3540077), "Deep_BoneHoard_E2", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2906.8193, 1076.0444, 799.63574), (0.0, 33.54731215438259, -0.0), (1.0, 1.0, 1.0), "Deep_BoneHoard_E3", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3458.8599, 856.18945, 800.0), (0.0, 21.2355952479442, -0.0), (1.0, 1.0, 2.1503875), "Deep_BoneHoard_E5", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3821.0977, 790.999, 817.7744), (0.0, 112.93254216697629, -0.0), (1.0, 1.0, 2.8614788), "Deep_BoneHoard_E6", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5494.243, 1331.6874, 856.63477), (0.0, 137.93264170569756, -0.0), (1.0, 1.0, 1.5996089), "Deep_BoneHoard_E7", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (889.92285, 4392.023, 805.0), (0.0, -44.55358720670315, 0.0), (1.0, 1.0, 1.0), "Deep_BoneHoard_E8", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2580.0923, 5224.9844, 803.61816), (0.0, -79.68777477951231, 0.0), (1.0, 1.0, 1.1448618), "Deep_BoneHoard_E9", _folder)
if a: placed += 1
else: skipped += 1

# Batch 4: StaticMesh'Deep_BoneHoard_F' (17 instances)
_mesh_path = "/Game/Art/Assets/Kits/Architecture/Deep/Deep_BoneHoard_F"
_materials = ['/Game/Art/Assets/Kits/Misc/Dirt_Mounds/Materials/MI_DirtMound_Mines']
_folder = "Reconstruction/BD_BB_Chapter5_CavernShaft/Meshes"
a = spawn_static_mesh(_mesh_path, _materials, (819.9487, 2289.5728, 797.6748), (0.0, 55.913015729681234, -0.0), (0.93545306, 0.93545306, 0.93545306), "Deep_BoneHoard_F_255", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5455.788, 4835.195, 828.87146), (-2.7444762742424, -143.50670999513326, 0.02365941458243803), (0.935453, 0.935453, 1.325467), "Deep_BoneHoard_F10", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3067.1672, 5654.7197, 848.8766), (-2.7444762306140054, -84.9709731054889, 0.023660054005373594), (0.935453, 0.935453, 1.7030258), "Deep_BoneHoard_F11", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1296.3824, 4961.411, 818.87463), (-2.7444765500907606, -27.871580753307327, 0.02366532809576775), (0.935453, 0.935453, 1.9825902), "Deep_BoneHoard_F12", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2229.65, 3718.4062, 813.8765), (-2.7444766166727037, 135.8483480245211, 0.023665668112076994), (0.935453, 0.935453, 1.82344), "Deep_BoneHoard_F13", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3299.6912, 4092.4116, 805.9031), (0.2081705013932459, -63.46105673431309, -0.10760497630176809), (0.935453, 0.935453, 1.82344), "Deep_BoneHoard_F14", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3595.75, 6091.059, 3707.358), (0.7781442803348274, -83.1597252442847, 0.4464427595094185), (0.6027629, 0.7938343, 1.898034), "Deep_BoneHoard_F15", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2513.1042, 6091.059, 3707.358), (0.7781439974543763, -83.15972524274602, 0.4464430104757591), (0.602763, 0.793834, 1.898034), "Deep_BoneHoard_F16", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1724.6412, 5933.4165, 3723.7542), (0.7781439829573159, -64.09696002706312, 0.4464434894786392), (0.602763, 0.793834, 1.898034), "Deep_BoneHoard_F17", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5179.781, 5302.253, 3607.358), (0.7781439970263168, -137.6578759063461, 0.4464440802086696), (1.0980016, 1.2890726, 2.3932729), "Deep_BoneHoard_F18", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1966.5999, 676.13086, 875.28906), (-1.3386839918516575, 55.41872571926839, 0.050619877501671205), (1.0, 1.0, 3.4514632), "Deep_BoneHoard_F2", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4263.0796, 589.09656, 863.8788), (-4.3841245360724335, 145.80937069056952, -1.9267878274163197), (0.935453, 0.935453, 1.3254668), "Deep_BoneHoard_F3", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3400.504, 623.6082, 815.52734), (-2.200561371667991, 86.45489965630058, -1.5321964376959993), (0.935453, 0.935453, 1.325467), "Deep_BoneHoard_F4", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4958.672, 5478.3477, 838.6034), (-3.403168067976381, -91.60401150182106, 0.27260826868724286), (1.0, 1.0, 1.0), "Deep_BoneHoard_F5", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5441.433, 1511.4609, 823.8756), (-4.384093956423499, 171.55035854807346, -1.926787774142193), (0.935453, 0.935453, 1.325467), "Deep_BoneHoard_F7", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5939.0117, 2699.1665, 833.8729), (-2.7444761137738265, 172.44618563830787, 0.023658169868300653), (0.80753016, 0.935453, 1.325467), "Deep_BoneHoard_F8", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5891.872, 3900.9167, 828.8727), (-2.7444763073559075, -166.76170280733558, 0.023658661080884876), (0.935453, 0.935453, 1.325467), "Deep_BoneHoard_F9", _folder)
if a: placed += 1
else: skipped += 1

# Batch 5: StaticMesh'Remains_Bones_Humerus' (1 instances)
_mesh_path = "/Game/Art/Assets/Kits/Deco/Warrens_Tomb/Remains_Bones_Humerus"
_materials = ['/Game/Art/Assets/Kits/Deco/Orc/Shanty/Material/Orc_Shanty_Midden/MI_Orc_Shanty_Midden_Mat_Inst']
_folder = "Reconstruction/BD_BB_Chapter5_CavernShaft/Meshes"
a = spawn_static_mesh(_mesh_path, _materials, (2002.5674, 3310.0076, 1295.2588), (2.408352070936312, -35.27548588039651, -13.930634493740877), (2.38796, 2.38796, 2.38796), "Remains_Bones_Humerus_137", _folder)
if a: placed += 1
else: skipped += 1

# Batch 6: StaticMesh'Remains_Bones_Radius' (2 instances)
_mesh_path = "/Game/Art/Assets/Kits/Deco/Warrens_Tomb/Remains_Bones_Radius"
_materials = ['/Game/Art/Assets/Kits/Deco/Orc/Shanty/Material/Orc_Shanty_Midden/MI_Orc_Shanty_Midden_Mat_Inst']
_folder = "Reconstruction/BD_BB_Chapter5_CavernShaft/Meshes"
a = spawn_static_mesh(_mesh_path, _materials, (1895.0034, 3230.141, 1279.7262), (11.046271493838605, -23.927854617014606, -52.825800171305715), (2.2131257, 2.2131257, 2.2131257), "Remains_Bones_Radius_140", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1992.3136, 3171.4216, 1277.1698), (2.4629809674928045, -163.61768065571343, -5.764556569460914), (2.213126, 2.213126, 2.213126), "Remains_Bones_Radius2", _folder)
if a: placed += 1
else: skipped += 1

# Batch 7: StaticMesh'Dirt_Mound_D' (2 instances)
_mesh_path = "/Game/Art/Assets/Kits/Misc/Dirt_Mounds/Dirt_Mound_D"
_materials = ['/Game/Art/Assets/Kits/Misc/Dirt_Mounds/Materials/MI_DirtMound_Mines']
_folder = "Reconstruction/BD_BB_Chapter5_CavernShaft/Meshes"
a = spawn_static_mesh(_mesh_path, _materials, (2465.5986, 2060.657, 783.2344), (0.0, 51.04219807324796, -0.0), (1.0, 1.0, 1.0), "Dirt_Mound_D3_88", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2902.8752, 1781.7683, 777.3994), (1.4247157016819616, -113.83178756061523, -0.6292114098328939), (1.0, 1.0, 0.85402256), "Dirt_Mound_D4", _folder)
if a: placed += 1
else: skipped += 1

# Batch 8: StaticMesh'Dirt_Mound_E' (4 instances)
_mesh_path = "/Game/Art/Assets/Kits/Misc/Dirt_Mounds/Dirt_Mound_E"
_materials = ['/Game/Art/Assets/Kits/Misc/Dirt_Mounds/Materials/MI_DirtMound_Mines']
_folder = "Reconstruction/BD_BB_Chapter5_CavernShaft/Meshes"
a = spawn_static_mesh(_mesh_path, _materials, (1882.8511, 2520.0637, 792.1953), (0.0, -147.57806834086978, 0.0), (1.0, 1.0, 1.0), "Dirt_Mound_E_26", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3912.936, 2018.6606, 788.7326), (0.0, 109.53910082527237, -0.0), (1.4572104, 1.4572104, 1.4572104), "Dirt_Mound_E2_121", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3189.376, 4649.846, 800.0), (0.0, 106.41039540347842, -0.0), (1.0, 1.0, 0.08490486), "Dirt_Mound_E4_246", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4191.322, 2581.4243, 1168.3353), (0.0, -38.02383312699096, 0.0), (0.9914977, 0.9914977, 2.5921018), "Dirt_Mound_E5", _folder)
if a: placed += 1
else: skipped += 1

# Batch 9: StaticMesh'Dirt_Mound_F' (1 instances)
_mesh_path = "/Game/Art/Assets/Kits/Misc/Dirt_Mounds/Dirt_Mound_F"
_materials = ['/Game/Art/Assets/Kits/Misc/Dirt_Mounds/Materials/MI_DirtMound_Mines']
_folder = "Reconstruction/BD_BB_Chapter5_CavernShaft/Meshes"
a = spawn_static_mesh(_mesh_path, _materials, (1577.9492, 3152.6401, 794.95215), (0.0, 107.56374259662437, -0.0), (1.0, 1.0, 0.3379826), "Dirt_Mound_F_48", _folder)
if a: placed += 1
else: skipped += 1

# Batch 10: StaticMesh'Dirt_Mound_G' (1 instances)
_mesh_path = "/Game/Art/Assets/Kits/Misc/Dirt_Mounds/Dirt_Mound_G"
_materials = ['/Game/Art/Assets/Kits/Misc/Dirt_Mounds/Materials/MI_DirtMound_Mines']
_folder = "Reconstruction/BD_BB_Chapter5_CavernShaft/Meshes"
a = spawn_static_mesh(_mesh_path, _materials, (4914.215, 2737.4338, 805.0), (0.0, 24.489897592003445, -0.0), (1.0, 1.0, 1.0), "Dirt_Mound_G2_139", _folder)
if a: placed += 1
else: skipped += 1

# Batch 11: StaticMesh'Dirt_Mound_H' (1 instances)
_mesh_path = "/Game/Art/Assets/Kits/Misc/Dirt_Mounds/Dirt_Mound_H"
_materials = ['/Game/Art/Assets/Kits/Misc/Dirt_Mounds/Materials/MI_DirtMound_Mines']
_folder = "Reconstruction/BD_BB_Chapter5_CavernShaft/Meshes"
a = spawn_static_mesh(_mesh_path, _materials, (1498.7427, 2996.1633, 795.6201), (0.0, -84.91466822584435, 0.0), (1.0, 1.0, 1.0), "Dirt_Mound_H_29", _folder)
if a: placed += 1
else: skipped += 1

# Batch 12: StaticMesh'Dirt_Mound_I' (32 instances)
_mesh_path = "/Game/Art/Assets/Kits/Misc/Dirt_Mounds/Dirt_Mound_I"
_materials = ['/Game/Art/Assets/Kits/Misc/Dirt_Mounds/Materials/MI_DirtMound_Mines']
_folder = "Reconstruction/BD_BB_Chapter5_CavernShaft/Meshes"
a = spawn_static_mesh(_mesh_path, _materials, (2593.9216, 2666.2424, 1118.4292), (-0.7405700488869668, -136.77376654945417, -3.4082341247004155), (1.0, 1.0, 1.0010232), "Dirt_Mound_I10", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1902.0215, 3061.1746, 1030.2758), (-1.1634973729125326e-07, -139.59510499843967, 2.6284832168362797), (0.69716823, 0.69716823, 0.69716823), "Dirt_Mound_I11", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2246.3982, 3265.375, 1290.2203), (-3.248596059331858, -150.9939434946502, 9.336513366532081), (0.4455629, 0.4455629, 0.6), "Dirt_Mound_I12", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5863.7676, 4888.743, 845.1133), (0.004671993022049182, 88.9651244520384, 0.13960108135766536), (1.0, 1.0, 1.0), "Dirt_Mound_I13", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3166.7478, 2490.9626, 1681.8856), (-1.9536767743244965e-08, 19.377429188532577, 2.628510675280079), (0.7914279, 0.7914279, 0.7914279), "Dirt_Mound_I14", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4528.6025, 4484.0684, 789.1279), (0.44969962934345203, -77.17142790287483, -0.7812500769428503), (1.0, 1.0, 0.19919097), "Dirt_Mound_I15", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4141.8623, 5264.0396, 793.541), (-1.6492920079695987, -7.020416075332952, -1.9756165117206348), (1.0, 1.0, 0.26045623), "Dirt_Mound_I16", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2361.3982, 3570.375, 1295.2203), (-3.0321044683678444, 156.01699940154518, -2.604614195269139), (0.5, 0.5, 0.6), "Dirt_Mound_I17_59", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2089.104, 3343.9038, 1272.6002), (0.459296029030784, -103.7319701390854, 2.0888671835060855), (0.445563, 0.402285, 0.452829), "Dirt_Mound_I18", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5917.2637, 4508.131, 846.08105), (-0.09225463957226682, 44.03450836479471, -0.5110168021757988), (1.0, 1.0, 0.11097), "Dirt_Mound_I19", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2371.1877, 3067.0947, 1121.8198), (1.0101590180353286e-07, 90.00001421429829, 2.6284607500719255), (1.0, 1.0, 1.0), "Dirt_Mound_I2_39", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4858.086, 3183.568, 788.374), (0.0, -158.52025456318398, 0.0), (1.0, 1.0, 0.3920648), "Dirt_Mound_I20_252", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4901.58, 3002.1873, 805.66895), (1.4120935604445968, -158.51344176735523, 0.55579486414708), (1.0, 1.0, 0.053054), "Dirt_Mound_I21", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3007.837, 3643.7336, 1299.4078), (6.431425388849914e-09, -8.161925688735465, 2.6285600416626385), (0.791428, 0.791428, 0.791428), "Dirt_Mound_I22", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3086.134, 3549.59, 1528.2252), (11.18259820802205, -48.85787712072196, -1.8779906447227455), (0.71132064, 0.66804266, 0.5), "Dirt_Mound_I23", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2864.8801, 3041.223, 1520.6486), (0.9020197830986657, -73.63716669779107, -2.233642645078863), (1.0, 1.0, 1.0), "Dirt_Mound_I24", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3740.2402, 3144.1663, 2095.7566), (1.1411506006289516, 128.4915997399504, 4.224035687888725), (1.18809, 1.18809, 0.8507302), "Dirt_Mound_I25", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3740.936, 3423.4172, 2152.0022), (2.1961071849801854, -77.02154442780727, -1.4366758003502378), (0.70953625, 0.70953625, 1.1721541), "Dirt_Mound_I26", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3608.196, 3455.484, 2145.2346), (1.7443891402147815, -83.05309339836657, -4.487456806523209), (0.709536, 0.709536, 1.172154), "Dirt_Mound_I27", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4021.4124, 3551.4658, 2175.7737), (4.608055451455469, -19.581118494256803, -2.1501774360113592), (0.709536, 0.709536, 1.172154), "Dirt_Mound_I28", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3740.0586, 3662.9988, 2526.582), (-1.5375367764822847, -51.526975194229784, -4.6286009047924335), (0.709536, 0.709536, 0.5), "Dirt_Mound_I29", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3509.2712, 1841.1423, 764.88477), (6.04822026086497, -55.10017744136894, 1.9770899519379468), (1.0, 1.0, 1.0), "Dirt_Mound_I3_124", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2998.1045, 2344.3232, 1721.7639), (6.235182973986746, -10.874114121773184, -0.706207170459533), (0.711321, 0.668043, 0.5), "Dirt_Mound_I31", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3311.8274, 2304.1748, 1983.041), (8.437502336100577, 67.49991703736009, 8.4378724760754), (0.5, 0.5, 0.5), "Dirt_Mound_I32", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3263.1304, 2955.7542, 1726.6945), (3.9451508874754557, 31.348922669841286, 11.807481548772685), (1.0, 1.0, 1.0), "Dirt_Mound_I33", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3816.5208, 3360.5398, 2268.3193), (-4.782928037912531, -75.90835636578097, -2.0251765088475446), (0.8125, 0.90625, 1.0), "Dirt_Mound_I34", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3789.6938, 3205.611, 2257.0496), (-6.776946125862292, -87.62306397880397, -3.8559559376730017), (0.711321, 0.84375, 0.5), "Dirt_Mound_I35_118", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4273.942, 4519.3105, 3405.7744), (0.0, 121.91665470945796, -0.0), (1.0, 1.0, 0.5), "Dirt_Mound_I36", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5979.841, 4597.273, 812.64746), (0.0, 90.00444349483203, -0.0), (1.0, 1.0, 1.0), "Dirt_Mound_I4_133", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4560.528, 4265.894, 794.10547), (0.0, 90.0000030488508, -0.0), (1.0, 1.0, 1.0), "Dirt_Mound_I5_145", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (376.66016, 4603.678, 779.208), (0.0, -77.5271056362015, 0.0), (1.0, 1.0, 1.0), "Dirt_Mound_I8_189", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4752.1772, 3831.7085, 781.46484), (0.0, -146.0715512957601, 0.0), (1.0, 1.0, 1.0), "Dirt_Mound_I9", _folder)
if a: placed += 1
else: skipped += 1

# Batch 13: StaticMesh'Suburbs_Dirt_Mound_A' (1 instances)
_mesh_path = "/Game/Art/Assets/Kits/Misc/Dirt_Mounds/Suburbs_Dirt_Mound_A"
_materials = ['/Game/Art/Assets/Kits/Misc/Dirt_Mounds/Materials/MI_DirtMound_Mines']
_folder = "Reconstruction/BD_BB_Chapter5_CavernShaft/Meshes"
a = spawn_static_mesh(_mesh_path, _materials, (3393.0315, 167.11438, 852.8873), (0.0, -39.31497347766364, 0.0), (7.7886667, 7.7886667, 7.7886667), "Suburbs_Dirt_Mound_A_126", _folder)
if a: placed += 1
else: skipped += 1

# Batch 14: StaticMesh'Bone02' (1 instances)
_mesh_path = "/Game/Unshippable/ThirdParty/FantasyDungeon/meshes/Bones/Bone02"
_materials = ['/Game/Unshippable/ThirdParty/FantasyDungeon/Materials/Bones/Bones']
_folder = "Reconstruction/BD_BB_Chapter5_CavernShaft/Meshes"
a = spawn_static_mesh(_mesh_path, _materials, (2040.7318, 3227.5476, 1287.1626), (34.59361850635159, 0.40920470064758946, -7.460631813766676), (2.3656387, 2.3656387, 2.3656387), "Bone02_144", _folder)
if a: placed += 1
else: skipped += 1

# Batch 15: StaticMesh'PWM_Nordic_8x8x8_A' (33 instances)
_mesh_path = "/Game/Unshippable/Whitebox/Rocks/Meshes/PWM_Nordic_8x8x8_A"
_materials = ['/Game/Environments/ProcTexturing/ProcMaterial_Quarry_2mx5m_B2']
_folder = "Reconstruction/BD_BB_Chapter5_CavernShaft/Meshes"
a = spawn_static_mesh(_mesh_path, _materials, (1941.2589, 133.6582, 2500.3105), (-8.030822787508592, 90.00001434316377, 2.589637504607897e-07), (1.0, 1.0, 1.0), "PWM_Nordic_8x8x8_A_31", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3995.7336, 46.925293, 1292.0156), (-3.7621154684135463, 111.42966213321894, -2.931976107442883), (1.0, 1.0, 1.0), "PWM_Nordic_8x8x8_A10", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4931.9854, 396.79785, 1085.1201), (2.5738897533283747, 116.98792558465769, 1.1663177613621356), (1.0, 1.0, 0.878112), "PWM_Nordic_8x8x8_A11", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5901.3066, 866.8137, 1022.31836), (-2.100555045766803, -45.39897914439727, -1.8902887867853937), (1.0, 1.0, 1.0973041), "PWM_Nordic_8x8x8_A12", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5781.75, 5294.588, 1125.1406), (1.104080883211538, -116.30471752616562, 3.9892660398844244), (1.0, 1.0, 0.878112), "PWM_Nordic_8x8x8_A13_107", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4250.746, 2952.3552, 948.2972), (1.0438239323344807, 152.57984565796983, 3.8338397938048367), (1.0, 1.0, 1.1814634), "PWM_Nordic_8x8x8_A14_239", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (919.96875, 3358.0938, 8364.482), (37.62877615160842, 175.98577360218184, 9.945922108919966), (1.1023773, 1.8242073, 1.875252), "PWM_Nordic_8x8x8_A16", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2229.963, 6050.9824, 1245.1641), (-6.063110042215715, -86.8160371589806, -3.060241647976169), (1.0, 1.0, 1.0), "PWM_Nordic_8x8x8_A17", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1193.7065, 5885.923, 1043.3076), (2.573881448095409, -64.83367095413978, 1.166318709221935), (1.1873242, 1.1873242, 1.065436), "PWM_Nordic_8x8x8_A18", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4409.668, 6030.0845, 840.13086), (-10.638121940026808, -4.50042696375051, -0.46084593991243095), (1.4090475, 1.0, 0.878112), "PWM_Nordic_8x8x8_A19", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (773.09033, 5295.744, 985.63086), (5.1979784712678185, -45.26265628403141, 7.168120303222342), (1.0, 1.0, 0.878112), "PWM_Nordic_8x8x8_A20", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3875.747, 6390.6646, 5186.13), (-0.6325681499824022, 88.76855434698977, 174.76437541995335), (0.734155, 1.165157, 2.154549), "PWM_Nordic_8x8x8_A21", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1365.0802, 1404.4185, 8136.16), (-32.01323911823765, 36.90185514433343, -12.944273448628286), (1.443234, 2.227686, 2.462306), "PWM_Nordic_8x8x8_A23", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3276.3171, 691.6172, 8342.247), (-36.205929121985214, 90.66570496748179, 3.943512898423678), (1.1685479, 2.227686, 2.462306), "PWM_Nordic_8x8x8_A24", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5007.959, 1153.1771, 8179.1455), (-34.01168651330786, 142.54475636097166, -30.083526995335387), (0.8719063, 2.227686, 2.462306), "PWM_Nordic_8x8x8_A25", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5588.686, 2872.9214, 8544.077), (-35.290130842551264, 177.30828297715072, -7.284760759087407), (1.0402614, 2.227686, 1.8436282), "PWM_Nordic_8x8x8_A26", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4913.7417, 4768.815, 8467.744), (-47.53778365535694, -138.7534156918965, 178.4744555638927), (1.1624016, 2.227686, 1.8768167), "PWM_Nordic_8x8x8_A27", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2332.7104, 4796.5093, 8745.466), (-35.28955359718305, -55.6548697408879, -7.284759990805791), (1.296171, 2.227686, 1.5840933), "PWM_Nordic_8x8x8_A28", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3540.3452, 4799.99, 8935.541), (-56.232662354662324, -86.41988314115427, 0.7469411153504413), (0.940484, 2.227686, 1.3805969), "PWM_Nordic_8x8x8_A29", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2975.8035, -24.53711, 2995.5166), (-8.022247898029786, 87.33257693117991, 0.37255629799188134), (0.7341546, 1.195072, 1.345229), "PWM_Nordic_8x8x8_A3", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2542.8442, 1454.7437, 8481.857), (58.658095062740514, -118.42339784138684, -152.71161727173234), (0.74743754, 2.227686, 2.462306), "PWM_Nordic_8x8x8_A30", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2229.963, 5983.8037, 2604.1538), (6.100819297602483, -82.40732912102897, 177.62926333395998), (1.0, 1.0, 1.0), "PWM_Nordic_8x8x8_A31", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4519.466, 1924.4749, 8479.1455), (-62.29381676085405, 138.728796807621, -34.281249139982705), (0.19623324, 2.227686, 2.462306), "PWM_Nordic_8x8x8_A32_233", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4519.466, 3288.7542, 8757.003), (-84.96006619698956, 166.63037587751236, 59.73753474798632), (0.196233, 2.227686, 2.462306), "PWM_Nordic_8x8x8_A33_235", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3952.3308, 3884.6472, 8757.003), (-84.95954557690956, -64.75782659658802, 59.736892810525916), (0.196233, 2.227686, 2.462306), "PWM_Nordic_8x8x8_A34", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1338.5248, 3810.2551, 8500.601), (-17.72411794745826, -28.382627175960486, -172.49376657701592), (1.1348203, 3.0317938, 1.6662499), "PWM_Nordic_8x8x8_A35", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5219.361, 4230.3203, 8728.367), (-46.74366948261801, -154.42133657378372, -170.00660376298651), (1.443234, 2.227686, 1.2899522), "PWM_Nordic_8x8x8_A36_238", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2262.5596, -16.918457, 3673.8184), (-8.030730571352128, 81.55658229157365, 1.5811047866911967e-06), (0.734155, 1.1651574, 1.195072), "PWM_Nordic_8x8x8_A4_37", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2250.2935, -225.16992, 4367.125), (8.92824602227742, -95.42907459429512, -2.079315639020925), (0.734155, 1.165157, 1.195072), "PWM_Nordic_8x8x8_A5", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2914.2769, 6325.638, 2682.5117), (4.106997865920109, 90.65774973179509, -2.2814945945358263), (0.8350196, 1.165157, 1.246753), "PWM_Nordic_8x8x8_A6_129", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1916.3467, 206.74756, 1156.7637), (-8.020049881417963, 87.0151695630891, 0.41683092759673873), (1.1209447, 1.1209447, 1.1034007), "PWM_Nordic_8x8x8_A7", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1533.8976, 222.2207, 3151.0952), (-16.462795534398822, 90.32692544417687, 1.5498871258089308), (1.0, 1.0, 1.0), "PWM_Nordic_8x8x8_A8", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (821.0303, 1230.3379, 1186.5938), (1.0438236287627745, 61.71989258772401, 3.8338016590943798), (1.0, 1.0, 0.87811166), "PWM_Nordic_8x8x8_A9", _folder)
if a: placed += 1
else: skipped += 1

# Batch 16: StaticMesh'PWM_Quarry_1x1x1_A' (14 instances)
_mesh_path = "/Game/Unshippable/Whitebox/Rocks/Meshes/PWM_Quarry_1x1x1_A"
_materials = ['/Game/Environments/ProcTexturing/ProcMaterial_Quarry_Atlas_1']
_folder = "Reconstruction/BD_BB_Chapter5_CavernShaft/Meshes"
a = spawn_static_mesh(_mesh_path, _materials, (4078.1494, 315.8272, 6467.884), (0.0, 0.0, -0.0), (1.0, 1.0, 1.9610428), "PWM_Quarry_1x1x1_A_2", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2528.2695, 3794.9675, 1095.0), (0.0, 42.187413915257146, -0.0), (1.28125, 1.28125, 1.75), "PWM_Quarry_1x1x1_A10", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2643.2695, 3759.9675, 1190.0), (-7.512632514568759, -175.78068664886393, 173.43302944325745), (1.5, 1.65625, 2.0), "PWM_Quarry_1x1x1_A11", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3522.0, 2141.0, 1943.0), (0.0, -74.79860968187218, 0.0), (1.15625, 1.34375, 1.28125), "PWM_Quarry_1x1x1_A12_80", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4100.0, 2620.0, 2000.0), (-4.331145926886768, -29.054444572908952, 2.4024243821196207), (1.28125, 1.28125, 1.6875), "PWM_Quarry_1x1x1_A13_108", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3196.234, 3496.8518, 1647.2429), (0.0, -92.81256265472086, 0.0), (1.65625, 1.4375, 1.4375), "PWM_Quarry_1x1x1_A14", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2557.101, 5753.661, 6735.712), (0.0, 0.0, -0.0), (1.7903862, 1.7903862, 1.7903862), "PWM_Quarry_1x1x1_A2_5", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (205.72174, 2216.7969, 5055.2896), (0.0, 0.0, -0.0), (1.0, 1.0, 2.095027), "PWM_Quarry_1x1x1_A3_8", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3335.232, 5287.8438, 3189.0933), (0.0, 0.0, -0.0), (1.5504868, 1.0, 1.0), "PWM_Quarry_1x1x1_A4_23", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3809.4846, 4500.795, 3293.9626), (0.0, 0.0, -0.0), (1.0, 1.0, 1.5599648), "PWM_Quarry_1x1x1_A5_26", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2382.208, 5957.557, 3049.8), (-6.027017657347544e-08, 22.037502882244933, -8.072754221028623), (1.0, 1.0, 2.5803022), "PWM_Quarry_1x1x1_A6_29", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2507.8171, 1889.4716, 825.0), (0.16914910708665115, -67.03802402782856, -1.375610243875773), (1.0, 1.0, 1.0), "PWM_Quarry_1x1x1_A7_26", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1923.2697, 2139.9675, 845.0), (-7.622345528298229, 154.4458602934172, 3.6289234977732576), (1.0, 1.0, 1.0), "PWM_Quarry_1x1x1_A8", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2389.234, 3112.8518, 1294.2429), (-17.758636943837036, 172.98657065314745, 0.4579359627004053), (1.34375, 1.34375, 1.34375), "PWM_Quarry_1x1x1_A9", _folder)
if a: placed += 1
else: skipped += 1

# Batch 17: StaticMesh'PWM_Quarry_1x1x1_B' (9 instances)
_mesh_path = "/Game/Unshippable/Whitebox/Rocks/Meshes/PWM_Quarry_1x1x1_B"
_materials = ['/Game/Environments/ProcTexturing/ProcMaterial_Quarry_Atlas_1']
_folder = "Reconstruction/BD_BB_Chapter5_CavernShaft/Meshes"
a = spawn_static_mesh(_mesh_path, _materials, (2399.9126, 2015.0393, 874.9996), (0.000860189902416165, -47.8137878427353, -89.9997867427418), (1.34375, 1.34375, 1.34375), "PWM_Quarry_1x1x1_B_29", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2353.24, 1952.7484, 855.0), (0.00033447879695845597, 14.061675112170592, -89.99907995990478), (1.34375, 1.34375, 1.34375), "PWM_Quarry_1x1x1_B2", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2306.2642, 1892.7014, 834.9997), (-0.0003064679154612716, -162.3043480989397, 89.99968122193387), (1.34375, 1.34375, 1.34375), "PWM_Quarry_1x1x1_B3", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1971.8562, 2236.0098, 874.9996), (-5.585783699108611, -126.00953908283427, -92.86096564975227), (1.34375, 1.34375, 1.34375), "PWM_Quarry_1x1x1_B4", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1911.2642, 2352.7014, 834.9997), (-0.0003679173760889063, 126.56510964670551, 89.99982216508137), (1.34375, 1.34375, 1.71875), "PWM_Quarry_1x1x1_B5", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2121.8562, 2141.0098, 879.9996), (0.0009070917411961566, -45.00106673733068, -89.99913649466927), (1.59375, 1.8125, 1.59375), "PWM_Quarry_1x1x1_B6", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1911.8562, 2511.0098, 879.9996), (-5.869690086361504, 13.707215778977826, 2.0549552240038245), (1.59375, 1.8125, 1.59375), "PWM_Quarry_1x1x1_B7", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1911.8562, 2661.0098, 914.9996), (0.0, 0.0, -0.0), (1.5, 1.5, 1.5), "PWM_Quarry_1x1x1_B8", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3651.8562, 2171.0098, 1269.9995), (0.0009019717796604947, 1.025970434497061, -89.99844583706097), (2.03125, 2.25, 2.03125), "PWM_Quarry_1x1x1_B9", _folder)
if a: placed += 1
else: skipped += 1

# Batch 18: StaticMesh'PWM_Quarry_1X1x1_C' (9 instances)
_mesh_path = "/Game/Unshippable/Whitebox/Rocks/Meshes/PWM_Quarry_1X1x1_C"
_materials = ['/Game/Environments/ProcTexturing/ProcMaterial_Quarry_Atlas_1']
_folder = "Reconstruction/BD_BB_Chapter5_CavernShaft/Meshes"
a = spawn_static_mesh(_mesh_path, _materials, (731.56006, 2616.5063, 789.5508), (-3.294494566856547, -11.57900834873195, -15.6682148178784), (1.0, 1.0, 1.0), "PWM_Quarry_1X1x1_C_313", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3831.1838, 751.01294, 796.375), (0.0, 0.0, -0.0), (1.0, 1.0, 1.0), "PWM_Quarry_1X1x1_C10", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1893.8087, 1402.074, 814.2129), (-24.228633664264947, -13.53805386163655, -45.17748404378326), (1.0, 1.0, 1.0), "PWM_Quarry_1X1x1_C3", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2385.49, 2160.0, 849.97595), (-5.625000157300274, 0.0, -0.0), (2.0, 2.0, 2.0), "PWM_Quarry_1X1x1_C4_34", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3611.242, 657.9829, 846.8115), (0.0, 0.0, -0.0), (1.0, 1.0, 1.0), "PWM_Quarry_1X1x1_C5", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4371.343, 1067.1299, 798.5176), (-10.829010065938643, 37.007032606459056, -30.176848604775792), (1.0, 1.0, 1.0), "PWM_Quarry_1X1x1_C6", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4859.1855, 3044.8057, 796.16406), (0.0, 90.0000030488508, -0.0), (1.0, 1.0, 1.0), "PWM_Quarry_1X1x1_C7_337", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5036.145, 2732.6833, 796.19666), (0.9932515999127802, -51.46057186514183, -79.54851757184271), (1.0, 0.43014666, 1.0), "PWM_Quarry_1X1x1_C8_340", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3550.2651, 6069.15, 3176.625), (0.0, 0.0, -0.0), (1.0, 1.0, 1.5797133), "PWM_Quarry_1X1x1_C9_20", _folder)
if a: placed += 1
else: skipped += 1

# Batch 19: StaticMesh'PWM_Quarry_2x2x2_A' (15 instances)
_mesh_path = "/Game/Unshippable/Whitebox/Rocks/Meshes/PWM_Quarry_2x2x2_A"
_materials = ['/Game/Environments/ProcTexturing/ProcMaterial_Quarry_Atlas_1']
_folder = "Reconstruction/BD_BB_Chapter5_CavernShaft/Meshes"
a = spawn_static_mesh(_mesh_path, _materials, (5448.609, 5445.062, 7810.7676), (0.0, 0.0, -0.0), (1.0, 1.0, 1.63085), "PWM_Quarry_2x2x2_A_11", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4715.8887, 237.08862, 7436.214), (-3.962797893241795, 118.13280870293934, 163.925415996393), (3.666711, 5.488449, 8.042368), "PWM_Quarry_2x2x2_A10_212", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5377.002, 5123.21, 8851.796), (8.182731937505483, 45.915558710598894, 174.19922473333767), (3.666711, 5.488449, 8.042368), "PWM_Quarry_2x2x2_A11", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4361.468, 5464.2896, 9135.242), (-6.824339086470854, -109.73007918786108, -174.603234144777), (3.666711, 5.488449, 3.5711904), "PWM_Quarry_2x2x2_A12", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5372.9985, 3704.81, 3788.868), (0.0, -104.06256359119939, 0.0), (1.40625, 1.125, 1.96875), "PWM_Quarry_2x2x2_A13", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3931.6267, 287.63574, 8529.752), (9.319458312047612, -119.25433528722715, 175.35778732249324), (3.666711, 5.488449, 8.042368), "PWM_Quarry_2x2x2_A14", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (151.4209, 4469.3086, 8475.849), (2.5577644589521067, 173.8497526602118, -173.14841276658962), (3.666711, 5.488449, 5.488449), "PWM_Quarry_2x2x2_A17", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3335.556, 6138.241, 3176.2332), (0.0, 0.0, -0.0), (1.0, 1.0, 1.1446688), "PWM_Quarry_2x2x2_A2_14", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2309.255, 2307.247, 947.99963), (0.00013660375929806914, -47.80685058547765, -179.99995901886666), (1.3125, 1.15625, 1.375), "PWM_Quarry_2x2x2_A3_17", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1962.1016, 2856.7659, 977.99567), (0.00045762262073638084, -14.05636584324658, 0.00039672850149264017), (1.3125, 1.15625, 1.375), "PWM_Quarry_2x2x2_A4", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2567.1016, 3861.7656, 897.99567), (-1.0878602410975309, 72.83944261025766, 8.824769373322221), (1.4, 1.4, 1.4), "PWM_Quarry_2x2x2_A5", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3160.4016, 2251.0789, 1778.5392), (0.0, -112.01170973005284, 0.0), (1.15625, 1.125, 1.0), "PWM_Quarry_2x2x2_A6_74", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3064.5945, 2147.479, 1642.0974), (0.0, 51.17162584097345, -0.0), (1.40625, 1.125, 1.0), "PWM_Quarry_2x2x2_A7", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3308.2312, 3329.8367, 2025.6245), (5.419584594657753, 80.04623913510467, 13.612213735988783), (1.40625, 1.125, 1.96875), "PWM_Quarry_2x2x2_A8", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3677.8945, 96.35449, 7436.214), (1.787719738743166, -118.84715566633733, 179.5562824236855), (3.666711, 5.488449, 8.042368), "PWM_Quarry_2x2x2_A9", _folder)
if a: placed += 1
else: skipped += 1

# Batch 20: StaticMesh'PWM_Quarry_2x2x5_A' (22 instances)
_mesh_path = "/Game/Unshippable/Whitebox/Rocks/Meshes/PWM_Quarry_2x2x5_A"
_materials = ['/Game/Environments/ProcTexturing/ProcMaterial_Quarry_Atlas_2']
_folder = "Reconstruction/BD_BB_Chapter5_CavernShaft/Meshes"
a = spawn_static_mesh(_mesh_path, _materials, (3303.438, 2101.9797, 1515.5028), (-9.216421238288894e-08, 64.6878449381601, 2.8125082328824926), (1.75, 1.75, 1.75), "PWM_Quarry_2x2x5_A_70", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1347.0006, 409.4541, 2151.1494), (-1.0712889704445705, 100.5956976805425, -178.6124676850089), (2.91827, 2.91827, 2.91827), "PWM_Quarry_2x2x5_A14_163", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3355.8027, 2247.5903, 1547.1738), (1.2336554985843196, -95.71523738757678, -11.160034101343133), (1.75, 1.75, 1.75), "PWM_Quarry_2x2x5_A2", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3141.3218, 2476.6772, 1840.0), (0.0, -160.3125829166266, 0.0), (1.28125, 1.28125, 1.28125), "PWM_Quarry_2x2x5_A3", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3841.3218, 3726.6772, 2670.0), (0.0, 175.00682094197853, -0.0), (1.0, 1.0, 1.0), "PWM_Quarry_2x2x5_A4", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (123.72461, 3371.3271, 3956.9731), (-0.9652097576099452, 38.70788058700896, 177.20009469572835), (7.199294, 6.7159166, 4.141889), "PWM_Quarry_2x2x5_A49", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3351.3218, 3881.6772, 2965.0), (0.0, -9.525237369088796, 0.0), (1.0, 1.0, 1.0), "PWM_Quarry_2x2x5_A5", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (352.01025, 1126.8765, 3628.3525), (-0.965240297294326, 31.888272417545153, 177.20009444584986), (4.141889, 4.141889, 4.141889), "PWM_Quarry_2x2x5_A50_79", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (6200.804, 1124.9539, 938.0762), (-1.0949095178868908, -152.81794800425493, 179.35468700013038), (4.141889, 4.141889, 4.141889), "PWM_Quarry_2x2x5_A51_177", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (6063.1733, 2789.7227, 980.312), (-4.573822610776554, -152.72967674378495, 177.5625798236067), (3.3159335, 3.8549814, 4.141889), "PWM_Quarry_2x2x5_A52_182", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (6123.6836, 1585.2394, 2843.7617), (-4.044433580432895, 152.88605692558284, 5.994634063720435), (2.7988138, 4.141889, 4.141889), "PWM_Quarry_2x2x5_A53_192", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (255.97949, 4904.922, 3831.9727), (-0.9649045708670874, 17.053129208217747, 177.20009492833205), (4.496616, 5.239779, 4.141889), "PWM_Quarry_2x2x5_A54_196", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (6023.6836, 2635.2393, 2843.7617), (-4.044433496887768, -177.11399411988057, 5.994682334963001), (2.798814, 4.141889, 4.141889), "PWM_Quarry_2x2x5_A55", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (412.92773, 1604.5479, 5787.623), (0.44259151326414325, 50.71505882855206, 175.76943189014733), (4.141889, 4.141889, 4.141889), "PWM_Quarry_2x2x5_A56", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1750.8385, 924.4021, 7836.69), (-3.9771724052312427, 102.2042991633245, 176.36840844240805), (4.141889, 4.141889, 4.141889), "PWM_Quarry_2x2x5_A57", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4020.2832, 6029.4546, 2178.456), (1.0169604151062592, -41.56225181766765, -177.39941383051215), (4.141889, 4.141889, 4.4411507), "PWM_Quarry_2x2x5_A58_122", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1457.456, 5394.374, 6343.828), (-0.7734985112723405, -108.81553551382424, 2.8167906856326277), (4.141889, 4.141889, 4.141889), "PWM_Quarry_2x2x5_A59", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3821.3218, 4126.6772, 3470.0), (0.0, -82.65021314445258, 0.0), (1.0, 1.0, 1.0), "PWM_Quarry_2x2x5_A6_4", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (6122.615, 5166.9814, 2954.8743), (-0.03390521263969362, -59.52878410735202, -3.0960996089435717), (4.141889, 4.141889, 4.141889), "PWM_Quarry_2x2x5_A61", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (372.01025, 1406.8765, 3728.3525), (-0.9652099470530371, -28.11175330183631, 177.20009505843962), (4.141889, 4.141889, 4.141889), "PWM_Quarry_2x2x5_A68", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (422.01025, 1501.8765, 3533.3525), (-7.517395199256037, -87.19271721468327, 2.5094608568117462), (4.141889, 4.141889, 4.141889), "PWM_Quarry_2x2x5_A69", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (335.9795, 5019.922, 2791.9727), (-5.744233201374858, 17.13935231852868, 175.72810753851536), (4.496616, 5.239779, 4.141889), "PWM_Quarry_2x2x5_A70", _folder)
if a: placed += 1
else: skipped += 1

# Batch 21: StaticMesh'PWM_Quarry_2x2x5_B' (2 instances)
_mesh_path = "/Game/Unshippable/Whitebox/Rocks/Meshes/PWM_Quarry_2x2x5_B"
_materials = ['/Game/Environments/ProcTexturing/ProcMaterial_Quarry_Atlas_2']
_folder = "Reconstruction/BD_BB_Chapter5_CavernShaft/Meshes"
a = spawn_static_mesh(_mesh_path, _materials, (4110.0, 2570.0, 1570.0), (0.0, 8.934015189826496, -0.0), (1.59375, 1.59375, 1.75), "PWM_Quarry_2x2x5_B_105", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3530.0, 2120.0, 1460.0), (0.15874803759974107, 178.98991122450622, 179.7354187298221), (1.59375, 1.59375, 1.75), "PWM_Quarry_2x2x5_B2", _folder)
if a: placed += 1
else: skipped += 1

# Batch 22: StaticMesh'PWM_Quarry_4x3x10_A' (369 instances)
_mesh_path = "/Game/Unshippable/Whitebox/Rocks/Meshes/PWM_Quarry_4x3x10_A"
_materials = ['/Game/Environments/ProcTexturing/ProcMaterial_Quarry_Atlas_A']
_folder = "Reconstruction/BD_BB_Chapter5_CavernShaft/Meshes"
a = spawn_static_mesh(_mesh_path, _materials, (5682.9375, 5221.278, 5988.367), (0.8749611063109574, -133.99916012431507, 178.19348390308332), (1.200631, 1.21927, 1.1468143), "PWM_Quarry_4x3x101", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (637.35156, 4806.5464, 773.14355), (1.8472044413681332, -171.04432283824107, 178.99357939364938), (1.032604, 1.051243, 0.642244), "PWM_Quarry_4x3x103", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2376.3135, 5741.015, 774.047), (1.8472046831091247, 160.96180179058547, 178.9935795360994), (1.032604, 1.051243, 0.642244), "PWM_Quarry_4x3x104", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (176.3086, 3578.5583, 3962.7402), (1.3584288071761181, 1.6756209856574005, -5.135864137698318), (1.393807, 1.393807, 1.393807), "PWM_Quarry_4x3x105", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4158.019, 5603.365, 773.14453), (1.8472046831091247, 160.96180179058547, 178.9935795360994), (1.032604, 1.051243, 0.642244), "PWM_Quarry_4x3x106", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (6080.9263, 862.5144, 3997.9795), (-1.1166077131625853, 177.1468309617022, -7.207183865352431), (1.393807, 1.8098354, 2.1347642), "PWM_Quarry_4x3x107_178", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (408.2705, 5178.6143, 4362.74), (1.358428921639015, -13.160522486591468, -5.13589505859191), (1.393807, 1.393807, 1.393807), "PWM_Quarry_4x3x108_197", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (295.31982, 2551.0059, 6156.296), (-2.5526125468963228, -96.4223098900785, -3.8375858096820927), (2.043059, 2.061698, 2.061698), "PWM_Quarry_4x3x109_71", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (703.3286, 1647.4426, 7046.7886), (-2.552612395692514, -96.42230685785306, 3.345253160707436), (2.043059, 2.061698, 2.061698), "PWM_Quarry_4x3x110_73", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (6087.629, 5138.3203, 7082.726), (2.5297798178888, 112.86211831826398, -1.490418000868288), (2.4804406, 2.4990792, 2.4990792), "PWM_Quarry_4x3x111_157", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (142.33789, 1248.1655, 4635.357), (-0.8096006851542049, 45.92598139836095, -3.780609247696175), (1.42174, 1.440379, 1.440379), "PWM_Quarry_4x3x112_814", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (348.43555, 2002.7805, 5918.193), (0.3560440897903983, -0.8490295985834596, -2.6282958541761077), (1.42174, 1.440379, 1.440379), "PWM_Quarry_4x3x113", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (250.06885, 2223.197, 4299.912), (0.35604407958753614, -0.8492736982021991, -2.6284178754073273), (1.42174, 1.440379, 1.440379), "PWM_Quarry_4x3x114", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (6243.3506, 2168.766, 1443.2305), (1.4104405618867746, 174.51349944343167, -0.7448424601589215), (1.42174, 1.440379, 1.440379), "PWM_Quarry_4x3x115_179", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (605.3677, 2008.1167, 6961.4204), (0.7187681519074568, -0.8875122730796269, -2.6144411452116545), (1.42174, 1.440379, 1.440379), "PWM_Quarry_4x3x116", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4956.1587, 5681.7085, 773.14453), (1.8472044132613537, 89.37605999302097, 178.99357953131533), (1.032604, 1.051243, 0.642244), "PWM_Quarry_4x3x117", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (50.0, 2250.3223, 3581.6123), (0.7187681237426452, -0.8873290815731193, -2.6143188229721117), (1.924987, 1.943626, 1.440379), "PWM_Quarry_4x3x118_817", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (28.464111, 815.1621, 3885.9858), (0.7187681237426452, -0.8873290815731193, -2.6143188229721117), (1.42174, 1.440379, 1.440379), "PWM_Quarry_4x3x119_819", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1436.2452, 495.96582, 6954.4595), (-5.9464418873523055, 114.88736660144299, -4.148681861834987), (1.42174, 1.440379, 1.440379), "PWM_Quarry_4x3x12_548", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (6080.9263, 862.5144, 2291.3667), (-1.1166077131625853, 177.1468309617022, -7.207183865352431), (1.393807, 1.809835, 2.134764), "PWM_Quarry_4x3x120", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (6434.089, 2235.5266, 583.72754), (1.774107222112405, 174.48728281061526, -0.7311400087472977), (1.42174, 1.440379, 1.440379), "PWM_Quarry_4x3x121_180", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (6187.2544, 2506.7388, 951.38947), (1.8472043152986974, 57.10371850785304, 178.99357944960514), (1.032604, 1.051243, 0.642244), "PWM_Quarry_4x3x122", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (234.95557, 2659.101, 3920.192), (2.8268987720668863, 114.20759023526179, 174.5760266733832), (2.043059, 2.4383373, 2.061698), "PWM_Quarry_4x3x123_76", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (104.994385, 990.9824, 4141.573), (2.8268987720668863, 114.20759023526179, 174.5760266733832), (2.348046, 2.3159735, 2.061698), "PWM_Quarry_4x3x124_80", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (6176.8193, 1738.9133, 881.2705), (0.6745245813615823, -70.45387605272828, 174.73370162357622), (2.043059, 2.061698, 2.061698), "PWM_Quarry_4x3x125_181", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (454.8518, 637.3833, 4012.0322), (4.903570482950534, 165.60071354960218, -178.48583988426276), (1.7276245, 1.7462636, 2.0369704), "PWM_Quarry_4x3x126_82", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (6144.393, 1235.465, 2510.542), (2.066787606522846, -65.91915150728491, -176.49838860058912), (2.043059, 2.061698, 2.061698), "PWM_Quarry_4x3x127", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (6094.7754, 3403.6824, 923.5005), (0.6745245813615823, -70.45387605272828, 174.73370162357622), (2.043059, 1.7934576, 2.061698), "PWM_Quarry_4x3x128_183", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2084.3767, 111.06494, 2944.081), (-3.179382472365465, 68.6350461502097, 178.44585246104572), (1.691052, 2.431368, 1.813447), "PWM_Quarry_4x3x129_25", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (6176.0703, 3788.725, 812.0322), (0.45637280108052547, -19.145448543368612, -179.03622843341702), (1.727625, 1.746264, 1.746264), "PWM_Quarry_4x3x130_184", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (6243.727, 3850.5784, 2023.2432), (3.435113548707519, -19.18069341215808, 179.92820098021824), (1.727625, 2.5429313, 1.746264), "PWM_Quarry_4x3x132_188", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (72.157715, 4316.4766, 3755.1938), (2.826898359235942, 99.37280884159621, 174.57602555010342), (2.043059, 3.1056063, 2.061698), "PWM_Quarry_4x3x133_198", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (391.21826, 5292.1777, 3870.538), (7.737722976881338, 99.4486944053596, 175.3929839250611), (2.043059, 2.061698, 2.061698), "PWM_Quarry_4x3x134_200", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (66.91016, 3929.0, 4140.214), (4.316121917949354, 108.87867357352589, 174.82236879961485), (2.043059, 2.061698, 2.061698), "PWM_Quarry_4x3x135_202", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (221.91016, 3929.0, 3490.2139), (4.316122557928441, 108.87867356686446, 174.8223689066963), (1.5416585, 2.4223886, 1.2288642), "PWM_Quarry_4x3x136", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (369.9944, 800.9824, 3196.5732), (2.8268987720668863, 114.20759023526179, 174.5760266733832), (2.348046, 2.315974, 2.061698), "PWM_Quarry_4x3x137", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3175.6545, -1.1513672, 1719.5576), (3.5076842396893735, 92.84675458346344, 176.98482762761435), (1.5688331, 2.309149, 1.6912285), "PWM_Quarry_4x3x138", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3638.3037, -13.483398, 1359.7754), (-3.3020929464979525, 56.683266216043506, -179.83679941304672), (1.42174, 1.440379, 1.440379), "PWM_Quarry_4x3x139_5", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1929.8287, 269.2798, 7422.162), (0.5882225985819101, 13.422766068614042, 1.5179386048425934), (3.511567, 2.6519656, 2.1238525), "PWM_Quarry_4x3x14", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2941.799, 116.92285, 4476.5947), (-0.9571534131383875, 109.20318599531562, -3.854431610979106), (1.691052, 2.431368, 2.4524477), "PWM_Quarry_4x3x140", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1457.5383, -125.762695, 4101.7593), (4.244519401726191, 95.94537367084385, 176.47159439301413), (1.691052, 3.461914, 2.0412142), "PWM_Quarry_4x3x141", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2496.5886, 60.52954, 5445.993), (3.319717473337542, 95.23688078521671, 177.05235307968934), (1.691052, 2.431368, 1.813447), "PWM_Quarry_4x3x142", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1694.9783, 211.37451, 5755.5312), (-3.639922382513267, 79.82768445039767, 176.63467779188375), (1.691052, 3.9649024, 1.813447), "PWM_Quarry_4x3x143", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3445.7783, 178.99316, 5755.5312), (2.0435997552387106, 88.05567690541795, 176.4416585775042), (1.691052, 3.964902, 1.813447), "PWM_Quarry_4x3x144_59", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2888.8123, 289.74, 7078.38), (-0.09216298265234986, 93.46094066582243, 176.50101302771307), (1.691052, 3.44029, 1.813447), "PWM_Quarry_4x3x145", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (890.4514, 538.74854, 5827.4365), (0.9070488211836018, -145.3360264585395, -175.17423924874427), (1.691052, 3.964902, 2.3177154), "PWM_Quarry_4x3x146_63", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1053.4929, 724.87256, 1280.5654), (1.5586628627391934, -90.29928546336272, 178.24143717193576), (2.1133857, 2.431368, 1.813447), "PWM_Quarry_4x3x147", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (983.6985, 313.4126, 2551.7627), (1.4374345367461365, 79.59075674647218, 179.61261820587103), (1.691052, 2.431368, 1.813447), "PWM_Quarry_4x3x148", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (687.7351, 433.9712, 2616.1025), (-2.5396118868244333, -41.16448855115459, 2.5461018830127404), (1.691052, 2.431368, 1.813447), "PWM_Quarry_4x3x149", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (947.9856, 849.0078, 6151.8516), (-0.9891051944809455, -52.101867240486065, 1.3959065788564933), (1.42174, 1.440379, 1.440379), "PWM_Quarry_4x3x15", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (822.17114, 127.89453, 3912.5938), (0.1957600172687891, 42.936112662446725, 178.353778535626), (1.691052, 2.431368, 1.813447), "PWM_Quarry_4x3x150", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1264.0426, 933.6421, 949.60254), (-3.3020929464979525, 56.683266216043506, -179.83679941304672), (1.42174, 1.440379, 1.440379), "PWM_Quarry_4x3x151", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (454.2964, 1708.208, 862.5), (3.3006953673092143, -117.19499669544416, -179.81000456461987), (1.42174, 1.440379, 1.440379), "PWM_Quarry_4x3x152", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4109.359, -67.02783, 2278.2725), (-2.2418517322466736, 104.74192255566827, -0.39505001168385123), (1.691052, 3.461914, 2.041214), "PWM_Quarry_4x3x153", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3824.849, -176.3479, 3368.462), (-1.702453716464385, 80.23106389320724, 174.1994699100107), (1.691052, 2.431368, 1.813447), "PWM_Quarry_4x3x154", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3564.3809, -3.5563965, 4508.7), (2.9578199951494266, -110.7719312065643, -176.72306992046506), (1.691052, 2.431368, 2.0340216), "PWM_Quarry_4x3x155", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5414.539, 593.2273, 822.42285), (-2.00680504936627, 112.16485310382456, 177.37237295872836), (1.42174, 1.440379, 1.440379), "PWM_Quarry_4x3x156", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4517.894, 227.5918, 817.0918), (1.7157771261243278, -61.72703115001566, -177.17337997655102), (1.42174, 1.440379, 1.440379), "PWM_Quarry_4x3x157", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4745.543, 50.00049, 2088.3154), (-2.006805168021192, 112.16457941208067, 177.59326669306105), (1.42174, 1.440379, 1.919286), "PWM_Quarry_4x3x158", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5260.6504, 291.39502, 2055.5654), (2.1894548966062266, -42.979251513438996, 0.7314758201479117), (1.691052, 3.461914, 2.041214), "PWM_Quarry_4x3x159", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4645.3643, 206.51367, 5670.8525), (6.039525936492076, -92.3931304305193, -175.89943336268854), (1.691052, 3.573455, 2.041214), "PWM_Quarry_4x3x160", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4451.708, -91.80713, 3964.961), (1.0556873651329748, 99.57831322492942, 177.55597221738248), (1.691052, 3.461914, 2.041214), "PWM_Quarry_4x3x161", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5528.552, 968.10864, 6556.107), (-14.907958318125962, 136.10845857629806, -10.473663235858547), (1.691052, 3.461914, 2.041214), "PWM_Quarry_4x3x162", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2143.5083, 206.93799, 1319.9092), (-2.425780505902615, -110.55896058930188, -179.3328571734077), (1.691052, 2.431368, 1.813447), "PWM_Quarry_4x3x163", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2441.039, 306.66797, 451.68066), (1.5586631787803347, -90.29928547277062, 178.2414371630763), (2.113386, 2.431368, 1.813447), "PWM_Quarry_4x3x164", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5959.5796, 785.09424, 5523.626), (1.2763096589096696, -5.009979253329571, 1.923614514052598), (1.691052, 3.461914, 2.041214), "PWM_Quarry_4x3x165", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5528.0566, 219.94922, 5039.179), (-7.436797043662294, 108.49591063726136, -1.4393918431019248), (1.691052, 3.461914, 2.041214), "PWM_Quarry_4x3x166", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5988.492, 400.5266, 2072.2012), (2.2401912415016185, 106.30371867940468, 176.37025420663724), (1.691052, 2.431368, 2.034022), "PWM_Quarry_4x3x167_23", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (6127.959, 414.48853, 3801.1016), (-7.250976223287456, 125.01092034797844, 175.80196387611304), (1.691052, 2.431368, 2.034022), "PWM_Quarry_4x3x168", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5582.9404, 162.02954, 3694.8125), (-7.436797043662294, 108.49591063726136, -1.4393918431019248), (1.691052, 3.461914, 2.041214), "PWM_Quarry_4x3x169", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1199.8989, 5055.6797, 6954.4595), (-7.626466003150829, 14.099946235964111, -6.682984094099306), (1.42174, 1.440379, 1.440379), "PWM_Quarry_4x3x17", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (362.46387, 3299.7078, 5710.435), (2.513712603306567, 177.60311872875423, 179.7890426547761), (1.691052, 3.964902, 2.317715), "PWM_Quarry_4x3x171_65", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3320.558, 2585.8625, 8046.2197), (5.736831484713204, 93.12639135297268, -179.3379527832881), (2.113386, 2.431368, 1.813447), "PWM_Quarry_4x3x172", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (164.95557, 2124.101, 3870.192), (2.8268986892194747, -5.792632973969457, 174.57602721376492), (2.5346956, 2.7761552, 2.061698), "PWM_Quarry_4x3x174", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3334.9624, 4342.183, 2591.6477), (1.6073109701659836, -114.45983471887135, 179.4252713410528), (1.2700322, 0.96963096, 0.9763378), "PWM_Quarry_4x3x177", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3310.549, 3047.7964, 6789.8833), (-2.1962889925532783, 137.61554585317722, -177.03775873175726), (1.691052, 2.431368, 1.813447), "PWM_Quarry_4x3x178_40", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5887.629, 5337.7964, 6073.479), (4.499829825313968, 112.57246981921794, -6.20202585057558), (2.480441, 2.499079, 2.499079), "PWM_Quarry_4x3x179", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (798.36914, 4666.9424, 7424.674), (-1.5381163347671705, -87.68408338862469, 3.6704390228049126), (3.511567, 2.651966, 2.123852), "PWM_Quarry_4x3x18_138", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5429.525, 595.2186, 4949.7236), (-16.29754593385867, 108.97795684939804, -4.008268788340582), (1.691052, 2.8233244, 1.3613185), "PWM_Quarry_4x3x180", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3437.9438, 2927.6426, 6215.667), (1.252758989872892, -66.92204750647335, 175.20784628301536), (2.2517219, 2.431368, 1.813447), "PWM_Quarry_4x3x181", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5030.7124, 359.7605, 4732.7856), (0.03701585247873244, 69.0678043892737, 177.14584704268492), (1.691052, 1.6526921, 1.361318), "PWM_Quarry_4x3x184", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4922.303, 798.40906, 5185.425), (0.03701594684843031, 69.0678043854611, 177.14584710754622), (1.2074292, 1.1690693, 1.0172644), "PWM_Quarry_4x3x185", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3556.9917, 2807.4119, 6509.282), (-6.102080879427662, -174.69024338647048, -179.6234100308351), (2.251722, 2.431368, 1.813447), "PWM_Quarry_4x3x186", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5495.018, 1540.0023, 7170.1885), (0.03701602612737467, 99.54629654454044, 177.14584740751502), (1.4330055, 1.3946455, 0.5541017), "PWM_Quarry_4x3x187", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5756.8525, 595.2184, 4238.5166), (-10.60336297783589, 108.51540446406435, -2.0222164909649507), (1.691052, 2.823324, 2.0357), "PWM_Quarry_4x3x188", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (714.00684, 3716.081, 7444.447), (-2.5158388084988266, 156.05707990270454, -179.81868562950766), (1.691052, 3.964902, 2.317715), "PWM_Quarry_4x3x189", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (6099.2837, 1240.3319, 6494.677), (-10.105835352058355, 88.60116526923701, 3.8791891549966966), (3.0423927, 2.9623036, 2.123852), "PWM_Quarry_4x3x19_158", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (528.3076, 2115.9468, 7165.34), (1.9340700160822657, 142.44557634773642, 178.38022746355486), (2.5026276, 3.964902, 2.317715), "PWM_Quarry_4x3x190", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (929.21436, 1152.6172, 7237.533), (-2.0120850147888087, 39.51013424466113, 178.478394003132), (1.691052, 3.964902, 2.317715), "PWM_Quarry_4x3x191", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (633.43823, 1129.668, 5689.6387), (4.431822696337586, 133.10430606299806, 175.7830455765847), (2.043059, 2.061698, 2.061698), "PWM_Quarry_4x3x192", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2273.551, 573.4988, 7770.969), (3.2412246918235317, -175.67886706855558, 171.47493084425432), (2.043059, 2.061698, 2.061698), "PWM_Quarry_4x3x193", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (220.61816, 5231.5474, 1080.6445), (-0.5575254448468043, 162.49329252996455, 173.35613176882842), (2.113386, 2.431368, 1.813447), "PWM_Quarry_4x3x194_119", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2959.7473, 6011.482, 1523.6328), (-1.9042968436391445, -84.48837025529318, 176.98872850988803), (1.568833, 2.5602074, 1.691229), "PWM_Quarry_4x3x195", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5532.3027, 5791.7295, 1219.9639), (1.578265549214956, 91.66813839516777, 178.07582492664173), (2.113386, 2.431368, 1.813447), "PWM_Quarry_4x3x196", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5328.1045, 5575.923, 889.5342), (-3.2283025864516888, -121.35335685119432, -179.68704716999096), (1.42174, 1.440379, 1.440379), "PWM_Quarry_4x3x197", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (6163.7715, 4829.705, 799.8174), (3.2433356367768806, 64.76858308212658, -179.96666195930436), (1.42174, 1.440379, 1.440379), "PWM_Quarry_4x3x198", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2039.7842, 6075.3765, 2205.454), (-4.706817578334558, -77.31326328099121, -3.1809383269524045), (2.054031, 3.461914, 2.041214), "PWM_Quarry_4x3x199", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (6181.8115, 2223.504, 1979.59), (-0.3243102807973497, 100.18811526125651, 0.7062595317163536), (3.3313844, 1.427732, 2.123852), "PWM_Quarry_4x3x20", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1661.6177, 6024.414, 1871.7422), (-2.0068052712609625, -69.65701486894397, 177.59326699372068), (1.42174, 1.440379, 1.440379), "PWM_Quarry_4x3x200", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1139.0957, 5799.5186, 2000.3359), (-0.932373032290116, 135.161625520779, 1.0947604876791637), (1.691052, 3.461914, 2.041214), "PWM_Quarry_4x3x201", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4425.227, 6059.109, 1629.9712), (3.612589655037266, 71.39930014037787, 178.4620413927611), (1.691052, 2.431368, 1.813447), "PWM_Quarry_4x3x202", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3633.2642, 5959.0854, 609.9375), (-1.1806639048201717, 16.189454297073425, 177.96827420128037), (2.113386, 2.431368, 1.813447), "PWM_Quarry_4x3x203", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (471.7168, 5555.0557, 2090.3047), (-1.3607784925603061, -75.28897456497182, 176.37196050919567), (2.040468, 2.431368, 2.034022), "PWM_Quarry_4x3x204", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (361.0078, 4939.401, 776.6719), (1.1341322686484623, -50.536336974839635, -176.89365207741787), (1.42174, 1.440379, 1.440379), "PWM_Quarry_4x3x205", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1341.0762, 5474.5654, 649.0244), (-0.7971494645130037, 135.56462443860386, 176.7911387876523), (1.42174, 1.440379, 1.440379), "PWM_Quarry_4x3x206", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3401.1501, 6069.4604, 2137.9072), (-2.2613214798202725, 27.589035795149417, 177.25906953914918), (2.043059, 2.061698, 2.061698), "PWM_Quarry_4x3x207", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2959.7476, 5858.8667, 2479.4644), (6.534046526810421, 46.35774893153438, 172.69208432347455), (1.568833, 2.239986, 1.691229), "PWM_Quarry_4x3x208_32", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3262.6787, 6434.818, 3936.795), (-1.6684569578671518, -88.73388570137104, -178.82494102788615), (1.810262, 3.461914, 2.041214), "PWM_Quarry_4x3x209", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (336.30078, 4269.5195, 5867.7744), (-3.2627258640626833, -87.68102236693638, 3.600557385083205), (3.9530642, 2.651966, 2.343774), "PWM_Quarry_4x3x21", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3100.9429, 5866.994, 6464.8154), (-5.053680697314076, -89.36642490090081, 174.61743771151131), (1.691052, 2.431368, 1.3249756), "PWM_Quarry_4x3x210", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3427.7415, 6042.7764, 6453.558), (-5.451049667870835, -85.25446106618607, 179.14577438283905), (1.691052, 3.964902, 1.813447), "PWM_Quarry_4x3x211", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3993.172, 6223.418, 3718.6025), (-0.7064206967508546, -118.61316027441363, -178.4999924511171), (1.4332763, 2.431368, 1.813447), "PWM_Quarry_4x3x212", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2266.6714, 6142.959, 4025.1821), (-4.706817578334558, -77.31326328099121, -3.1809383269524045), (1.4927683, 3.461914, 2.041214), "PWM_Quarry_4x3x213", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2990.2144, 6155.6807, 5722.2646), (1.5493419720753994, 108.01638109086996, -1.143157864384194), (2.054031, 3.461914, 2.041214), "PWM_Quarry_4x3x214", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1306.264, 5803.203, 3627.8047), (5.1561160814922875, 132.1108884783268, 1.2888225043010073), (0.99490887, 3.6869109, 2.317715), "PWM_Quarry_4x3x215", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (691.4019, 5627.7993, 3627.8047), (-2.4159851369581546, -52.13125183101183, -4.606597958786067), (2.2937934, 3.4722784, 2.317715), "PWM_Quarry_4x3x216", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1850.2192, 5485.7583, 7227.82), (-4.867735812288983, -61.63873063741075, 179.47938061732532), (1.691052, 3.964902, 2.317715), "PWM_Quarry_4x3x217", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3149.5503, 5535.627, 7780.1895), (-5.743925987834524, -91.32170037337065, 178.67960552417824), (1.691052, 2.431368, 1.813447), "PWM_Quarry_4x3x218_152", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1959.3447, 5672.867, 6447.2666), (2.559654458154934, -162.6063843355319, -2.8704835995904294), (2.4416091, 2.061698, 2.061698), "PWM_Quarry_4x3x219", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5900.036, 1139.7363, 7200.8433), (2.6921831079448575, -12.418092030953364, 8.07856235890174), (1.42174, 1.440379, 1.440379), "PWM_Quarry_4x3x22_591", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (822.5503, 5079.615, 5868.1436), (-2.4295959869007038, -56.742499331952494, -3.9569394127352373), (2.159153, 3.79929, 2.381779), "PWM_Quarry_4x3x220", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1447.7754, 5781.057, 5316.6064), (0.9233662270390335, -150.08959238635356, 6.94458323690761), (2.441609, 2.061698, 2.061698), "PWM_Quarry_4x3x221", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2003.1445, 6011.97, 5367.948), (2.559653600222185, 135.20365123287053, -2.8704832563044804), (1.8872892, 2.061698, 2.061698), "PWM_Quarry_4x3x222", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (763.1738, 5462.3564, 5013.6313), (-10.96887155548082, 19.037656385271116, -19.977722059305115), (3.0888083, 2.061698, 1.5852561), "PWM_Quarry_4x3x223", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5396.791, 5471.7217, 2724.008), (-1.672760033973674, -111.21189130777512, 178.62157984957344), (2.113386, 2.431368, 1.813447), "PWM_Quarry_4x3x224", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2535.8208, 5656.511, 7850.913), (2.5596537578569256, 172.9672868001335, -2.8704832619430363), (2.441609, 2.061698, 2.061698), "PWM_Quarry_4x3x225", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5980.856, 2603.6833, 7104.2256), (-2.451171512924883, 174.55767982719954, -179.13728403864852), (1.691052, 7.355039, 2.317715), "PWM_Quarry_4x3x226", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5918.391, 3777.023, 6958.8843), (1.4831425485605536, -41.263516018861104, 177.86596137222634), (1.7008008, 3.0645761, 2.0010443), "PWM_Quarry_4x3x227", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1410.216, 5963.5566, 2873.1729), (-1.713684310719434, -75.19174670151196, 176.8788664591789), (1.568833, 2.239986, 1.3664343), "PWM_Quarry_4x3x228_34", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (6131.8174, 5188.7744, 2536.7988), (3.9274118373284455, -170.91720310443506, -2.3754266985100636), (2.159153, 3.79929, 2.381779), "PWM_Quarry_4x3x229", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (577.5298, 4077.8071, 6007.4365), (8.148850497237746, 132.56096761148737, 179.66397446739313), (3.586712, 2.651966, 0.8875364), "PWM_Quarry_4x3x23", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (6305.882, 5963.913, 5665.046), (1.0862274681184672, -179.87482311821626, -1.181976482304888), (2.113386, 2.431368, 1.813447), "PWM_Quarry_4x3x230", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (6134.7686, 4381.636, 7168.242), (-5.17160007991967, -171.68201524927923, -2.2445676599363296), (1.5364497, 5.6501675, 2.381779), "PWM_Quarry_4x3x231", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (6287.7803, 5475.581, 4107.5103), (0.9959849802076518, -4.769653110034383, -175.1063619925205), (2.159448, 3.461914, 2.041214), "PWM_Quarry_4x3x232", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5977.7637, 5791.252, 5047.7065), (-2.520141658384807, -4.83810412374849, -179.42171951223307), (2.159448, 3.461914, 2.041214), "PWM_Quarry_4x3x233", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5977.754, 6060.157, 3157.5117), (-2.5198666053527474, 178.18407657945852, -179.42171938717235), (2.159448, 3.461914, 2.374805), "PWM_Quarry_4x3x234", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (6318.0254, 3266.426, 2658.1025), (-2.450988620909282, 173.2027273297412, -179.13726352357358), (1.691052, 3.964902, 2.317715), "PWM_Quarry_4x3x235", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (6250.0, 4518.1797, 1795.3027), (2.0262162190905673, -170.93245257644494, -2.6794124350363546), (2.159153, 3.79929, 2.381779), "PWM_Quarry_4x3x236", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (6099.9873, 4396.0537, 1037.4458), (2.0262168299179573, -173.84881023168788, -2.6794124818665015), (2.159153, 4.288413, 2.381779), "PWM_Quarry_4x3x237", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (528.3076, 2867.9927, 7425.9873), (1.9340704612655408, -3.8574824221545065, 178.38022781035883), (2.502628, 3.964902, 2.317715), "PWM_Quarry_4x3x238", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3953.8503, 5810.927, 7657.128), (-1.4253840452141862, -74.03831162326685, 178.7566757894936), (2.0572245, 3.964902, 1.813447), "PWM_Quarry_4x3x239", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (459.40723, 3278.9016, 5795.2524), (8.14885068116404, 163.53069994501988, 179.66397483248537), (3.1252363, 3.3749707, 1.4989667), "PWM_Quarry_4x3x24", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2299.4453, 5284.842, 8596.941), (2.5596537578569256, 172.9672868001335, -2.8704832619430363), (3.0006595, 2.6207485, 2.0814016), "PWM_Quarry_4x3x240", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1312.1152, 4925.416, 8481.843), (2.559654172142231, -139.38603893778208, -2.870483553584877), (3.000659, 2.620749, 2.620749), "PWM_Quarry_4x3x241", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3600.7886, 3939.097, 579.03265), (0.9498812430848715, -119.51895384751587, 177.85068008815207), (2.113386, 2.431368, 1.3725649), "PWM_Quarry_4x3x247", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1959.3447, 5947.9663, 6107.2666), (2.559654107564079, 131.7410463521647, -2.8704834821074168), (2.441609, 2.061698, 2.061698), "PWM_Quarry_4x3x248_144", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1712.9578, 5639.2466, 3024.216), (-2.7845150265822722, -21.47079098553192, 174.16204671025488), (2.058424, 2.239986, 1.2808), "PWM_Quarry_4x3x249_36", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3686.246, 2190.0142, 508.4082), (0.37870001553899535, 94.10539143924758, -176.51507474611032), (1.691052, 2.431368, 1.395963), "PWM_Quarry_4x3x250", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4058.2512, 2458.936, 553.21875), (0.3786998597291388, -76.89739107695696, -176.5150755561174), (1.691052, 2.431368, 1.395963), "PWM_Quarry_4x3x251", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3668.5654, 2747.9243, 7694.0254), (4.750194879115252, -19.074525157737323, 176.8525948868358), (2.251722, 2.431368, 1.813447), "PWM_Quarry_4x3x252", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3665.9504, 3091.8682, 7817.6357), (-1.9967647993133346, 178.01471924215141, -177.51184551572564), (2.251722, 2.431368, 1.813447), "PWM_Quarry_4x3x253", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3240.9517, 2967.515, 8065.096), (-1.9967647993133346, 178.01471924215141, -177.51184551572564), (2.6235561, 2.8032022, 2.1852808), "PWM_Quarry_4x3x254", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4659.6177, 4155.267, 707.4873), (4.757506709782522, 80.20500114487591, 6.928885237030501), (1.2541429, 1.5721251, 0.5060802), "PWM_Quarry_4x3x259", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (775.93115, 4678.816, 6121.469), (4.015549792557185, 135.27507059586438, 179.9958883867789), (2.5669336, 2.6570609, 1.3455309), "PWM_Quarry_4x3x26_153", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4481.588, 3491.559, 660.5742), (-2.4730526560718737, -135.88061424610484, 2.5558009768469923), (1.721284, 2.039266, 1.421345), "PWM_Quarry_4x3x260", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5980.856, 2603.6833, 6199.2256), (-2.451171512924883, 174.55767982719954, -179.13728403864852), (1.691052, 3.767812, 0.41931102), "PWM_Quarry_4x3x262", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5981.1006, 4390.2104, 7672.162), (-5.171600422644914, -171.68203797724792, 0.008618005871407828), (0.754098, 3.047526, 2.381779), "PWM_Quarry_4x3x263", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3693.2185, 2872.8633, 6210.6514), (-4.720916585239394, 153.9188909126513, 176.43859625146087), (2.3146977, 2.431368, 1.813447), "PWM_Quarry_4x3x264", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3665.9504, 3358.406, 8913.76), (-2.2211601724188355, 178.26941633176028, 175.57348152107562), (2.251722, 2.431368, 1.813447), "PWM_Quarry_4x3x265_228", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (532.83386, 1129.668, 4787.631), (4.431822696337586, 133.10430606299806, 175.7830455765847), (2.043059, 2.061698, 2.061698), "PWM_Quarry_4x3x266", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2939.9316, 2686.9514, 8577.728), (5.736831800828082, 93.12639785081934, -179.33795284088689), (2.113386, 2.431368, 1.813447), "PWM_Quarry_4x3x267", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3029.9453, 3889.3188, 9057.304), (5.7368326808390036, 41.53447211634013, -179.33795282898805), (2.113386, 2.431368, 1.813447), "PWM_Quarry_4x3x268", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2972.9167, 3477.2737, 9079.133), (-0.5604249401136951, -57.332702864159764, -7.4767153960746064), (2.113386, 2.431368, 1.813447), "PWM_Quarry_4x3x269", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5125.5527, 94.54663, 3574.6372), (2.4730063848547195, -56.564875529022984, 3.224030846380494), (1.42174, 1.440379, 1.7404392), "PWM_Quarry_4x3x27", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1732.6475, 3060.654, 787.68945), (2.1633189678673936, 137.3688334287577, 172.0591587019486), (1.2314206, 1.3667171, 0.5108073), "PWM_Quarry_4x3x273", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (100.659294, 2241.5842, 2702.5981), (2.8268986892194747, -5.792632973969457, 174.57602721376492), (2.534696, 3.3777256, 1.1193566), "PWM_Quarry_4x3x277", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3026.0562, 4208.086, 811.05176), (-1.0090943226927132, -2.6430967257619975, -4.002044607647062), (1.0, 1.0, 0.747163), "PWM_Quarry_4x3x278", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2845.0994, 4151.931, 750.03516), (-1.0089721280043162, 114.37659103040306, -4.0020453395858295), (1.0, 1.0, 0.67777103), "PWM_Quarry_4x3x279", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1730.0806, 687.37085, 6692.428), (5.720754133420785, 132.02884611239875, -176.71725571263798), (3.125236, 3.026537, 0.638545), "PWM_Quarry_4x3x28", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3918.5447, 3901.3354, 942.0508), (-1.2969665905778371, -158.20745468225363, -179.8078052020829), (2.113386, 2.431368, 1.0), "PWM_Quarry_4x3x281", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1679.1709, 2916.4946, 555.09766), (0.8870577011105555, -88.7437479083433, 13.01977418187561), (1.0, 1.0, 0.7175731), "PWM_Quarry_4x3x285", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1949.4209, 3443.675, 595.5488), (6.305711391009922, -177.1184969546219, 4.199462680659273), (1.0, 1.0, 0.717573), "PWM_Quarry_4x3x286", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1831.6836, 3595.2134, 521.2217), (6.305712158769185, 89.77422815411403, 4.199463260454212), (1.0, 1.0, 0.717573), "PWM_Quarry_4x3x287", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1019.5796, 1635.2129, 730.49414), (6.675867820392158, 70.32965360622532, -2.6760557741436055), (1.0, 1.0, 0.54801977), "PWM_Quarry_4x3x288", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1675.9557, 1107.5579, 757.35547), (7.804972494664302, 70.73546938075404, 0.5428778609568313), (1.0, 1.0, 0.54802), "PWM_Quarry_4x3x289", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1154.7306, 1545.3002, 6818.4146), (6.264635061362262, -174.08165826568512, 177.75216306202648), (3.125236, 3.026537, 0.638545), "PWM_Quarry_4x3x29", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1675.9557, 1033.1638, 888.3584), (-2.4159848995056943, -33.12985528223227, -8.015900258194144), (1.0, 1.0, 0.54802), "PWM_Quarry_4x3x290", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1541.7867, 874.53735, 1072.5117), (-0.5610661123863511, -113.62001853134265, 5.402516992556728), (1.0, 1.2037076, 0.728753), "PWM_Quarry_4x3x291", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2344.7432, 651.1858, 910.7461), (-2.4461364552463523, -33.70947641855664, -0.19082649519709954), (1.0, 1.0, 0.54802), "PWM_Quarry_4x3x292", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2274.3271, 771.59375, 753.13574), (7.804973514669834, 70.73546946274908, 0.5428780198990086), (1.0, 1.0, 0.54802), "PWM_Quarry_4x3x293", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2529.8037, 1043.6177, 594.41016), (7.804973514669834, 70.73546946274908, 0.5428780198990086), (1.0, 1.0, 0.54802), "PWM_Quarry_4x3x294", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3080.9211, 447.2146, 740.6211), (7.804973514669834, 70.73546946274908, 0.5428780198990086), (1.0, 1.0, 0.54802), "PWM_Quarry_4x3x295", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3094.215, 184.646, 977.9541), (3.6452310417634846, 18.25787305977918, -7.845550979801757), (1.2207642, 1.2207642, 0.76878405), "PWM_Quarry_4x3x296", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1149.458, 1261.0449, 1003.5508), (-4.737304764582921, -174.02874334595433, 0.5631408114130168), (0.86688405, 0.91234, 0.91234), "PWM_Quarry_4x3x297", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (724.82983, 4177.4707, 5782.745), (4.015550392227437, 112.6996986854413, 179.99588830451657), (2.566934, 2.657061, 1.1730258), "PWM_Quarry_4x3x30_155", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4090.793, 1939.1165, 661.2627), (0.48340709249469865, -42.6790800168366, -0.4678649947061168), (1.0, 1.0, 0.615091), "PWM_Quarry_4x3x300", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4439.9844, 2329.0906, 615.8281), (6.397345559436523, -16.04754376988615, 177.19829160959148), (1.4215997, 1.7395821, 1.1216612), "PWM_Quarry_4x3x301", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4219.0264, 1939.1165, 771.6094), (5.354089166175355, -47.58068827976844, 179.5279641334912), (1.0, 1.0, 0.615091), "PWM_Quarry_4x3x302", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4852.757, 2535.6436, 663.03906), (4.0962887627333116, -68.62548035916707, -1.7833556178621532), (1.0, 1.2430236, 0.615091), "PWM_Quarry_4x3x303", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4664.6816, 4038.3298, 839.5869), (4.0962958819067055, -15.580932523368284, -1.7833557429749745), (1.0, 1.243024, 0.615091), "PWM_Quarry_4x3x304", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4768.6543, 3731.2944, 737.7822), (-8.324583751937991, -143.63683184136028, -4.567259786157454), (1.0, 1.243024, 0.615091), "PWM_Quarry_4x3x305", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (909.48975, 4990.5273, 699.7422), (-1.0090943226927132, -2.6430967257619975, -4.002044607647062), (1.2458178, 1.2458178, 0.7675277), "PWM_Quarry_4x3x307", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1119.5752, 5279.3, 857.8467), (1.102419611011866, 86.58817211925796, 5.394250733876957), (1.245818, 1.245818, 0.767528), "PWM_Quarry_4x3x308", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1410.8257, 5181.854, 754.1847), (-5.67813105310341, 62.01391727791334, 2.7620558922554777), (1.245818, 1.245818, 0.767528), "PWM_Quarry_4x3x309", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1279.6211, 4914.3555, 551.21875), (-5.678039133260463, 105.29088840835101, 2.762082972949569), (1.245818, 1.245818, 0.767528), "PWM_Quarry_4x3x310", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1078.9043, 4769.095, 592.0303), (-5.677947222811987, 139.94048524363737, 2.7621016051290876), (1.245818, 1.245818, 0.767528), "PWM_Quarry_4x3x311", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (485.99658, 4660.6562, 588.084), (-5.6778861929562705, 137.3851934472747, 2.762139540554688), (1.245818, 1.245818, 0.767528), "PWM_Quarry_4x3x312", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2702.967, 5775.731, 700.6456), (-1.0090637466780195, -30.637268468673078, -4.002045464673516), (1.245818, 1.245818, 0.767528), "PWM_Quarry_4x3x313", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3024.0159, 5932.108, 857.8496), (1.1024199845685005, 58.593935250907975, 5.394300017250712), (1.245818, 1.245818, 0.767528), "PWM_Quarry_4x3x314", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3235.4504, 5709.3555, 753.28613), (-5.67810100221758, 34.01977559546953, 2.7620637247260773), (1.245818, 1.245818, 0.767528), "PWM_Quarry_4x3x315", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2748.624, 5500.6885, 592.9337), (-5.677917738543524, 111.94617192679335, 2.762106134188409), (1.245818, 1.245818, 0.767528), "PWM_Quarry_4x3x316", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2000.9111, 5500.6885, 544.48047), (-5.677917738543524, 111.94617192679335, 2.762106134188409), (1.245818, 1.245818, 0.767528), "PWM_Quarry_4x3x317", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4484.673, 5638.081, 699.74316), (-1.0090331749895471, -30.637269398029975, -4.002045259890456), (1.245818, 1.245818, 0.767528), "PWM_Quarry_4x3x318", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4530.3296, 5363.0386, 592.0322), (-5.677917738543524, 111.94617192679335, 2.762106134188409), (1.245818, 1.245818, 0.767528), "PWM_Quarry_4x3x319", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5092.283, 5382.7476, 699.74316), (-1.0089416894774492, -102.22302233364226, -4.002045028861987), (1.245818, 1.245818, 0.767528), "PWM_Quarry_4x3x320", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4845.7456, 5252.547, 592.03125), (-5.677886635428878, 40.361139330268514, 2.7621216809372355), (1.245818, 1.245818, 0.767528), "PWM_Quarry_4x3x321", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5691.7314, 5014.9204, 690.8428), (-1.0089418034192743, -81.52346157926172, -4.002045020247786), (1.245818, 1.245818, 0.767528), "PWM_Quarry_4x3x322", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4542.078, 443.74072, 649.0283), (-0.7971498027678796, -60.19097281720902, 176.79116011530994), (1.42174, 1.440379, 1.440379), "PWM_Quarry_4x3x323", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5088.884, 792.3999, 699.7451), (-1.0089415206757981, 161.60070113219294, -4.002044337756126), (1.245818, 1.245818, 0.767528), "PWM_Quarry_4x3x324", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4554.432, 744.39307, 753.2871), (-5.678039890731598, -133.74203876755473, 2.762087036397026), (1.245818, 1.245818, 0.767528), "PWM_Quarry_4x3x325", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4753.343, 966.2141, 551.2217), (-5.677886828451391, -90.46554808652812, 2.762104646324769), (1.245818, 1.245818, 0.767528), "PWM_Quarry_4x3x326", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4348.85, 797.06445, 605.0215), (-5.677886408050393, -32.46996974308618, 2.762117142345734), (1.245818, 1.245818, 0.767528), "PWM_Quarry_4x3x327", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5825.146, 1390.1344, 755.5322), (-5.677886510291016, -83.07653967565705, 2.7621206967709355), (1.245818, 1.245818, 0.767528), "PWM_Quarry_4x3x328", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5730.042, 1259.4993, 893.3926), (-5.677886367488609, -5.230956624630837, 2.762126159944047), (1.245818, 1.245818, 0.767528), "PWM_Quarry_4x3x329", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (6117.69, 4607.2344, 651.4619), (-1.0089417021802598, -49.484129340154645, -4.00204526584076), (1.245818, 1.245818, 0.767528), "PWM_Quarry_4x3x330", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5999.0527, 1124.8625, 671.26074), (-0.7971497522936941, -50.50287058773179, 176.79116053706275), (1.42174, 1.440379, 1.0949415), "PWM_Quarry_4x3x332", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5961.3906, 1424.3236, 753.5947), (-5.678009199069414, -124.05442509946735, 2.7620943002514244), (1.245818, 1.245818, 0.4220903), "PWM_Quarry_4x3x333", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2008.2429, 5510.644, 3161.8765), (-3.0296631225590405, -47.170802730495865, 173.93441125900802), (2.058424, 2.239986, 1.0709093), "PWM_Quarry_4x3x337", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2373.9846, 5963.1973, 2889.4956), (3.1700477894305306, 32.251280930029225, 174.29202021366632), (2.058424, 2.239986, 1.070909), "PWM_Quarry_4x3x338", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2609.264, 5979.5884, 5567.8936), (-0.4173583976008879, 18.385255458380037, -178.78998909210657), (1.691052, 2.431368, 1.4488575), "PWM_Quarry_4x3x339", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2822.7854, 5960.3896, 5793.4785), (3.8546719042975552, 59.93410811618367, 175.6631400604347), (2.081868, 3.4815805, 2.0543823), "PWM_Quarry_4x3x340", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3518.5117, 6046.2354, 6051.0835), (-3.002868579241537, -13.824797491957808, 173.17312899102566), (1.691052, 2.431368, 1.324976), "PWM_Quarry_4x3x341", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1918.872, 6034.4404, 1295.0905), (3.041210666497707, 135.4914189307448, 173.0236793707094), (1.7418013, 1.8085518, 2.125047), "PWM_Quarry_4x3x342_42", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1602.6692, 5920.745, 1686.7722), (0.7779585345619019, 86.4999459098593, 0.026352491948980636), (1.9304858, 1.9304858, 1.4521958), "PWM_Quarry_4x3x343_43", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2036.8716, 5770.3496, 794.19714), (-8.178678831825628, 62.5932784415961, -2.0335378606372085), (1.9304858, 1.9304858, 1.4521958), "PWM_Quarry_4x3x354_44", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3195.4148, 4950.3022, 3307.2756), (-3.13714593350324, 179.5229371914275, -172.07432293458163), (1.691052, 2.431368, 0.715012), "PWM_Quarry_4x3x355", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1777.8877, 2846.5928, 893.1719), (-2.6222536121996947, -16.198394709001775, 2.2763616265207007), (0.431508, 0.431508, 0.37998593), "PWM_Quarry_4x3x357", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2860.9946, 223.11621, 5984.1245), (6.017813666290097, 61.441320762922984, 174.38574333524068), (1.42174, 1.440379, 1.440379), "PWM_Quarry_4x3x36", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1632.331, 2994.0835, 848.4834), (-0.04794281357451493, 113.99884783943017, -3.4714965317486968), (0.431508, 0.431508, 0.363007), "PWM_Quarry_4x3x374", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1732.7231, 2825.0146, 816.49316), (3.3693454226618913, -169.18201095770576, -0.8377378001179547), (0.431508, 0.431508, 0.363007), "PWM_Quarry_4x3x375", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1654.5571, 2967.2095, 817.1826), (-2.0294188283824703, 79.05023464724064, -2.8173828852548626), (0.431508, 0.431508, 0.363007), "PWM_Quarry_4x3x376", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1612.4077, 3124.9912, 890.2617), (-3.295715450037416, 43.12476028755005, -1.091583281550999), (0.431508, 0.431508, 0.363007), "PWM_Quarry_4x3x377", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1799.0916, 5578.5728, 591.6001), (-0.7971493004780994, 98.67589601950037, 176.79113909173233), (2.1763065, 2.1949453, 1.2845976), "PWM_Quarry_4x3x378_48", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5985.118, 3860.4011, 3382.0586), (-3.1232911590000487, 164.43780259349347, 179.48779563797714), (1.691052, 2.431368, 1.134916), "PWM_Quarry_4x3x380", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2183.8633, 6006.2686, 2560.854), (10.680462360085595, 136.4438425114756, -179.03593528877772), (1.8246092, 1.8432478, 1.4157188), "PWM_Quarry_4x3x381_51", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (-2.3395097, 4340.7915, 3023.6316), (2.826898359235942, 99.37280884159621, 174.57602555010342), (3.1617715, 3.105606, 1.9924048), "PWM_Quarry_4x3x382_10", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2420.2488, 6176.6357, 2169.1465), (3.8588973884452127, 103.28189805807057, 179.3287184039745), (1.824609, 1.843248, 1.415719), "PWM_Quarry_4x3x383_53", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5474.9897, 2941.9102, 3721.2095), (1.7749884760565016, 12.344349944678262, -179.58144504898794), (1.691052, 2.431368, 0.537168), "PWM_Quarry_4x3x384", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5745.4033, 2549.9985, 3592.9976), (3.6200607203263853, -12.778044473259275, 177.03111694915972), (1.691052, 3.080242, 0.763475), "PWM_Quarry_4x3x385", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5922.9907, 3180.4795, 3725.3577), (-3.707366482147244, 164.62842255526357, 178.14399230912042), (1.691052, 2.431368, 0.537168), "PWM_Quarry_4x3x386", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1332.1425, 5902.542, 2931.449), (1.7648322861417036, 145.23449589541912, 176.30061870617956), (1.824609, 1.843248, 1.415719), "PWM_Quarry_4x3x387_55", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4889.472, 4695.0913, 3465.4043), (-0.7399291404820433, 59.79620087264091, -179.82500366147394), (2.159153, 3.79929, 0.530917), "PWM_Quarry_4x3x389", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5172.3486, 150.57275, 4859.071), (-8.210236026764301, 77.20841922923874, -179.98880552892433), (1.42174, 1.440379, 1.440379), "PWM_Quarry_4x3x39", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5337.028, 4071.7344, 3536.876), (2.327980636938274, 3.5380605337256794, -178.58407920685562), (1.691052, 2.431368, 0.537168), "PWM_Quarry_4x3x390", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5778.858, 4594.166, 3552.0527), (-2.3224481624803563, -51.39491180412888, 176.62314307108977), (1.691052, 2.431368, 0.537168), "PWM_Quarry_4x3x391_26", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2504.6301, 5266.6914, 3179.1353), (-6.420534319730529, -109.81333015608558, 170.5082422144212), (1.691052, 2.6488404, 0.715012), "PWM_Quarry_4x3x392", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2795.4148, 5150.3022, 3257.2756), (-12.748775540115007, -128.94534042231135, 177.85801599064897), (1.691052, 2.431368, 0.715012), "PWM_Quarry_4x3x393", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2480.3904, 5699.799, 3207.0984), (5.788685635584334, -99.26448865434791, 170.62682059353514), (1.691052, 2.507724, 0.715012), "PWM_Quarry_4x3x394", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2806.973, 5643.924, 3257.7058), (2.248798315802346, -118.9703855961636, 178.13114249755006), (1.7816015, 2.555511, 0.715012), "PWM_Quarry_4x3x395", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2480.3904, 6249.799, 3207.0984), (5.788685635584334, -99.26448865434791, 170.62682059353514), (1.691052, 2.431368, 0.715012), "PWM_Quarry_4x3x396", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2795.4148, 6200.3022, 3257.2756), (2.2487987107850773, -118.97038560149808, 178.13114273039673), (1.691052, 2.431368, 0.715012), "PWM_Quarry_4x3x397", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1582.8743, 1657.8873, 6743.141), (-2.012054425993303, 1.2298278597850163, 178.4783938857453), (1.2281723, 1.9995407, 0.37157735), "PWM_Quarry_4x3x398", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1119.7958, 1561.32, 6364.2715), (2.6558574279861613, -88.50564880598274, -176.43879449232546), (1.5208342, 2.2922032, 0.7825819), "PWM_Quarry_4x3x399", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1185.4474, 770.1841, 6297.786), (8.095897007210356, -103.33823069489102, -177.7273450115407), (2.7591758, 2.8640609, 1.9747108), "PWM_Quarry_4x3x400", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1290.7214, 1217.9794, 6364.2715), (2.6558571118360628, -151.05024844367097, -176.43879422661732), (1.520834, 2.292203, 0.782582), "PWM_Quarry_4x3x401", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3810.3247, 4070.757, 2264.9836), (3.850682891244429, -134.88106455469625, 176.90602652262453), (1.721284, 2.039266, 1.34375), "PWM_Quarry_4x3x413", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5484.107, 3573.0603, 3583.0806), (2.446211720157221, -11.618560085051904, 179.4804872577015), (1.691052, 2.431368, 0.537168), "PWM_Quarry_4x3x417", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3136.917, 5662.9053, 3161.8765), (-3.029571921328027, 121.8654797481598, 173.93441229194346), (2.058424, 2.239986, 1.070909), "PWM_Quarry_4x3x418", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3932.4834, 5803.2383, 2965.2915), (-8.244414362741667, -109.14984877914328, 165.3141802481584), (1.691052, 2.64884, 0.715012), "PWM_Quarry_4x3x419", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4534.09, 5803.2383, 2965.2915), (-5.6675428574244355, -119.15788485804566, 172.59732887425972), (2.5535817, 3.5113692, 1.5775418), "PWM_Quarry_4x3x420", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5125.3677, 5270.5493, 3255.4858), (11.686342905612335, 68.83000679265432, 176.59594029714472), (2.6666284, 3.511369, 0.8747628), "PWM_Quarry_4x3x421", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4944.798, 5974.1084, 2532.1162), (-1.258605574363952, -154.1978852872413, 177.7127449973807), (2.553582, 3.511369, 1.577542), "PWM_Quarry_4x3x422_63", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5987.0483, 4737.18, 2887.824), (-3.1994016176524713, -142.25377989171494, -179.7832027997726), (2.553582, 3.0228171, 1.577542), "PWM_Quarry_4x3x423", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5987.0483, 4144.823, 3155.5986), (-3.199218486500519, 178.3453018332602, -179.7831823183348), (2.553582, 3.022817, 0.89010644), "PWM_Quarry_4x3x424", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (6114.7227, 3526.6611, 3155.5986), (6.572605663513622, 1.990078080117517, 176.1987880191139), (2.553582, 3.022817, 0.890106), "PWM_Quarry_4x3x425", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5734.4795, 3123.8481, 3271.0098), (6.572606414393762, -35.37429819819342, 176.19878745685074), (2.553582, 3.022817, 1.1793898), "PWM_Quarry_4x3x426", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5615.5654, 4565.5576, 3113.516), (-1.1732484797028169, -61.780268273202104, -174.48545104222342), (1.245818, 1.245818, 0.767528), "PWM_Quarry_4x3x427", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4287.3696, 4723.307, 3113.516), (-5.8731994625098976, -118.23570520173845, -177.01947421435574), (1.245818, 1.245818, 0.767528), "PWM_Quarry_4x3x428", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5415.427, 4348.173, 3260.2488), (-6.529206116918521, -118.10254939049544, -178.25161526083815), (1.245818, 1.245818, 0.53701806), "PWM_Quarry_4x3x429", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5536.8667, 4216.6924, 3260.2488), (8.168426183471125, 116.86871821784639, 175.870900003623), (1.245818, 1.245818, 0.537018), "PWM_Quarry_4x3x430", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (6176.522, 3575.663, 826.3669), (-0.7971495283074447, 31.706590638576287, 176.79113931749643), (1.42174, 1.440379, 1.440379), "PWM_Quarry_4x3x431", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (6039.991, 3837.4875, 1035.1892), (1.1024198888177341, -17.269990612481386, 5.39438070928082), (1.245818, 1.245818, 0.767528), "PWM_Quarry_4x3x432", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5875.623, 3578.0552, 931.52716), (-5.678040014791365, -41.84451500366882, 2.7620748976582385), (1.245818, 1.245818, 0.767528), "PWM_Quarry_4x3x433", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (6142.72, 2181.2798, 877.9881), (-1.0089416214626055, -134.49548438636916, -4.0020451526947465), (1.245818, 1.245818, 0.767528), "PWM_Quarry_4x3x434", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5864.7476, 2202.8308, 770.2762), (-5.677885873779164, 8.087982385986761, 2.76211108168951), (1.245818, 1.245818, 0.767528), "PWM_Quarry_4x3x435", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (6167.797, 3106.069, 768.94257), (-0.7971495525213756, -5.182493953877203, 176.7911390752345), (2.176306, 2.194945, 1.284598), "PWM_Quarry_4x3x436", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (6105.8237, 1735.3285, 694.79144), (-0.7971495379159338, -17.639827007026632, 176.79113938753684), (2.176306, 2.194945, 1.284598), "PWM_Quarry_4x3x437", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (6105.8237, 2479.961, 407.17517), (-0.7971494262868893, -46.168540352715695, 176.79113968536234), (2.176306, 2.194945, 1.284598), "PWM_Quarry_4x3x438", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5753.841, 1935.2754, 699.74524), (-1.0089414758405955, -119.27804057990883, -4.002045281862898), (1.245818, 1.245818, 0.767528), "PWM_Quarry_4x3x439", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1851.3878, 160.21387, 2619.1729), (-0.49520851220080275, -83.65405693275986, 178.19431613401844), (1.42174, 1.440379, 1.440379), "PWM_Quarry_4x3x44", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5700.1177, 1401.3685, 753.28723), (-5.678008349777316, -54.62060165153807, 2.762097074223235), (1.245818, 1.245818, 0.767528), "PWM_Quarry_4x3x440", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5519.823, 1638.5688, 551.2218), (-5.677885954267683, -11.344573110474732, 2.762112717173387), (1.245818, 1.245818, 0.767528), "PWM_Quarry_4x3x441", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5680.0444, 4824.4766, 699.7457), (-1.0089412861882658, -106.10087897120704, -4.002044656866494), (1.245818, 1.245818, 0.767528), "PWM_Quarry_4x3x442", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5749.4414, 4292.38, 753.2877), (-5.677916980988221, -41.443840543997496, 2.7621046140540195), (1.245818, 1.245818, 0.767528), "PWM_Quarry_4x3x443", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5519.823, 4482.2373, 551.2223), (-5.67788655851492, 1.8320313460234614, 2.7621257131897896), (1.245818, 1.245818, 0.767528), "PWM_Quarry_4x3x444", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5363.644, 5250.649, 6689.676), (10.05603815323211, 25.202139646184182, 169.34541232939821), (1.691052, 2.431368, 1.0949991), "PWM_Quarry_4x3x445", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5016.661, 5215.9087, 6891.218), (-10.54681408002257, -108.7832789444884, 172.54612933873486), (1.691052, 2.431368, 0.40898004), "PWM_Quarry_4x3x446", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4626.5977, 5484.6836, 6818.065), (-6.387052523485978, -165.17740433633918, -174.3382350220744), (1.691052, 2.431368, 0.81252235), "PWM_Quarry_4x3x447", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4911.9805, 516.85754, 5177.429), (10.967915957557837, -100.04577310331324, 174.34510085161634), (1.691052, 2.431368, 1.094999), "PWM_Quarry_4x3x448", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4987.2183, 824.42914, 5299.727), (-7.052520783740845, 134.5957396955145, 168.92682408140826), (1.691052, 2.431368, 0.586814), "PWM_Quarry_4x3x449", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2611.9128, 53.0083, 1898.5732), (-1.9921869349099837, -132.84047467693395, -178.46333846764122), (1.691052, 2.431368, 1.8134472), "PWM_Quarry_4x3x45_20", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5656.592, 1038.6495, 5241.169), (-6.773743674450902, 82.95307472444995, 172.70651463734873), (1.691052, 2.431368, 0.812522), "PWM_Quarry_4x3x450", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4149.6426, 5511.2583, 2733.9106), (-10.900359987414449, -99.42583201073846, 175.57186819424743), (1.8218806, 2.7796676, 0.8458405), "PWM_Quarry_4x3x451", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3540.113, 5511.2583, 2962.3044), (20.85675174818236, 51.3344351528819, 168.6042663399028), (2.2451649, 2.3919904, 0.845841), "PWM_Quarry_4x3x452", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3334.9624, 4342.183, 1976.0857), (1.6073108400376686, -132.97629318176092, 179.42527137794124), (1.270032, 0.969631, 0.976338), "PWM_Quarry_4x3x453", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3334.9624, 4342.183, 1068.4722), (1.6073108400376686, -132.97629318176092, 179.42527137794124), (1.270032, 0.969631, 0.976338), "PWM_Quarry_4x3x454", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3792.5513, 4257.434, 2286.5923), (1.1693421697207191, -67.87212606064882, 172.3339374036171), (1.4179411, 2.039266, 0.9852849), "PWM_Quarry_4x3x456", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3661.897, 4243.919, 2170.6477), (1.169341986450895, -164.93837800952286, 172.33394058613587), (1.417941, 2.039266, 0.985285), "PWM_Quarry_4x3x457", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4562.8267, 5106.3276, 2997.3547), (-5.8731994625098976, -118.23570520173845, -177.01947421435574), (1.245818, 1.245818, 0.767528), "PWM_Quarry_4x3x458", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4127.611, 5181.2666, 2855.8848), (-5.873198764746281, -164.53209898229704, -177.01947407843068), (1.245818, 1.245818, 0.767528), "PWM_Quarry_4x3x459", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2842.0203, 80.38257, 1489.7676), (-3.3020929464979525, 56.683266216043506, -179.83679941304672), (1.42174, 1.440379, 1.440379), "PWM_Quarry_4x3x46_21", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3931.4976, 4928.8774, 2855.8848), (9.89884174676675, 128.03436531583313, -173.35996279630783), (1.245818, 1.245818, 0.6402487), "PWM_Quarry_4x3x460", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3741.9697, 5028.3115, 2855.8848), (9.89884174676675, 128.03436531583313, -173.35996279630783), (1.245818, 1.245818, 0.640249), "PWM_Quarry_4x3x461", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3482.6487, 5107.533, 2896.2612), (13.726504806704334, 16.97363149843761, 174.78487241480457), (1.5155643, 1.626485, 0.63760877), "PWM_Quarry_4x3x463", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2542.3352, 5364.3613, 3241.4521), (4.380310577477326, 122.47339366843455, -175.84257678350096), (2.058424, 2.239986, 0.8895676), "PWM_Quarry_4x3x464", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1389.636, 5827.218, 2527.6926), (1.5473451586584372, 61.06894397857378, 175.51091869001405), (2.058424, 2.239986, 1.2808), "PWM_Quarry_4x3x465", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5799.65, 3121.3928, 7186.755), (7.949115912464462, 45.79003756248757, 179.49838195325876), (1.7023066, 1.6639467, 0.67766064), "PWM_Quarry_4x3x469", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2555.3635, 258.8733, 1016.3174), (-1.4364621450717, -177.96387439248772, -178.25569330527767), (1.42174, 1.440379, 1.440379), "PWM_Quarry_4x3x47_22", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5790.528, 1893.5044, 7174.8413), (10.786810228991747, 19.05545441515218, 177.6780280552457), (2.693611, 2.6552508, 0.82384235), "PWM_Quarry_4x3x470", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5614.5435, 2489.723, 7276.975), (10.7868079728603, 85.81383711613604, 177.6780271909754), (2.693611, 2.655251, 0.50203615), "PWM_Quarry_4x3x471", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5614.5435, 2816.5771, 7276.975), (12.00960187383257, 49.38076122146725, 179.12489416368427), (2.0738187, 2.1585882, 0.5116363), "PWM_Quarry_4x3x472", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5901.168, 2795.6826, 6828.5327), (9.454121358815383, -26.276001502473882, -178.66103385840015), (2.073819, 2.158588, 0.7237184), "PWM_Quarry_4x3x473", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5910.734, 3083.4321, 6828.5327), (9.454120888249335, -35.95522959392875, -178.66103402203316), (2.073819, 2.158588, 0.723718), "PWM_Quarry_4x3x474", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4967.8145, 5632.716, 6509.342), (9.454120869063908, 11.831665015109193, -178.66103381884506), (2.073819, 2.158588, 0.723718), "PWM_Quarry_4x3x475", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5756.8525, 595.2184, 2630.0154), (-10.60336297783589, 108.51540446406435, -2.0222164909649507), (1.691052, 2.823324, 2.0357), "PWM_Quarry_4x3x476", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1101.8439, 3892.782, 6044.2295), (-7.052490457940526, 43.53237790288102, 168.9268242121025), (1.691052, 2.431368, 0.586814), "PWM_Quarry_4x3x477", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1026.8073, 3315.637, 6044.2295), (3.3981558222763515, -84.2552299253761, 169.98012497477566), (1.691052, 2.431368, 0.586814), "PWM_Quarry_4x3x478", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (603.10474, 912.28906, 1064.6816), (-6.635375326272545, 104.7887764081364, 173.30722766676843), (1.42174, 1.440379, 1.440379), "PWM_Quarry_4x3x48", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (6205.1084, 5475.581, 3864.9128), (0.9959849802076518, -4.769653110034383, -175.1063619925205), (2.159448, 3.461914, 2.041214), "PWM_Quarry_4x3x480", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5975.5713, 808.2646, 3639.5122), (2.834172464398141, -12.76812756079788, 177.20954408896307), (1.691052, 3.080242, 0.763475), "PWM_Quarry_4x3x481", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2451.3784, 6142.4224, 3575.4973), (1.8472043090141237, 91.47748174176455, 178.9935793721789), (1.032604, 1.051243, 0.642244), "PWM_Quarry_4x3x482", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2775.8591, 6091.236, 3502.096), (-1.0090028161873852, -45.668273935583805, -4.0020452456700895), (1.245818, 1.245818, 0.767528), "PWM_Quarry_4x3x483", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2748.624, 5813.7627, 3394.384), (-5.6778858255075795, 96.91495565159971, 2.762109773845193), (1.245818, 1.245818, 0.767528), "PWM_Quarry_4x3x484", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3873.5308, 6142.4224, 3575.4973), (1.8472037334393836, 145.93077251831676, 178.9935791806436), (1.032604, 1.051243, 0.642244), "PWM_Quarry_4x3x485", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4198.0117, 6091.236, 3502.096), (-1.0090028161873852, -45.668273935583805, -4.0020452456700895), (1.245818, 1.245818, 0.767528), "PWM_Quarry_4x3x486", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4170.7764, 5813.7627, 3394.384), (-5.677885595129455, 96.91495565696304, 2.762109338414739), (1.245818, 1.245818, 0.767528), "PWM_Quarry_4x3x487", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3580.751, 6171.334, 3666.4119), (-5.677886133559478, -50.8514941253592, 2.762122104532212), (1.245818, 1.245818, 0.767528), "PWM_Quarry_4x3x488", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1682.4526, 5945.104, 3502.096), (-1.0089417146513158, -21.708587198700123, -4.002045464748431), (1.245818, 1.245818, 0.767528), "PWM_Quarry_4x3x489", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (425.80396, 661.4248, 1579.5732), (-5.7617799765149105, 111.85928552145134, 172.54249496401954), (1.42174, 1.440379, 1.440379), "PWM_Quarry_4x3x49", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1976.0881, 3361.3003, 695.6783), (2.1633189678673936, 137.3688334287577, 172.0591587019486), (1.231421, 1.366717, 0.510807), "PWM_Quarry_4x3x490", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3990.689, 2847.0889, 8913.76), (-2.221069382885255, 122.20964611190578, 175.5734821310548), (2.251722, 2.431368, 1.813447), "PWM_Quarry_4x3x492", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3625.0386, 2185.4548, 8913.76), (-2.22100801310924, 92.94019580651404, 175.57348219696382), (2.251722, 2.431368, 0.96650237), "PWM_Quarry_4x3x493", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3071.5105, 2185.4548, 8575.704), (-2.22100801310924, 92.94019580651404, 175.57348219696382), (2.251722, 2.431368, 0.966502), "PWM_Quarry_4x3x494", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5121.057, 5175.97, 631.1402), (2.053216010246775, -58.30264532176429, -3.580871281578827), (1.245818, 1.245818, 0.767528), "PWM_Quarry_4x3x495", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (73.053665, 3685.5461, 2995.0967), (4.506762365871861, 119.29893158262442, 174.34977134706267), (3.161772, 3.105606, 1.992405), "PWM_Quarry_4x3x496", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (326.42566, 3077.7056, 2951.1304), (1.7051689010008495, 94.43202558437471, 172.97931081461118), (3.161772, 1.443131, 1.992405), "PWM_Quarry_4x3x497", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (6042.8564, 2250.278, 3603.7717), (3.6200607203263853, -12.778044473259275, 177.03111694915972), (1.691052, 3.080242, 0.763475), "PWM_Quarry_4x3x498", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (6066.967, 2262.3613, 3274.3945), (4.354928307052702, 5.081024118402986, 178.28307212694784), (1.691052, 3.080242, 0.763475), "PWM_Quarry_4x3x499", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (421.99634, 967.6094, 1227.0723), (-5.491729869917758, 118.27910830217222, -2.7324215900487356), (1.42174, 1.440379, 1.440379), "PWM_Quarry_4x3x50", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5988.246, 5619.9795, 1002.7129), (-6.697296336449657, -73.25683765777912, 173.46276347962285), (1.42174, 1.440379, 1.440379), "PWM_Quarry_4x3x51_105", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (6158.3022, 5876.662, 1517.1816), (-5.842254053854247, -66.18343760010883, 172.68888966216443), (1.42174, 1.440379, 1.440379), "PWM_Quarry_4x3x52_106", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4684.292, 5685.4863, 538.3672), (0.5376861297489518, -73.24030104384404, -179.87354586915785), (1.42174, 1.440379, 1.440379), "PWM_Quarry_4x3x53_110", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (342.64697, 5875.0146, 1322.4902), (-5.622405028846376, 4.164695351404773, 177.88974126314116), (1.42174, 1.440379, 1.440379), "PWM_Quarry_4x3x54_117", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (671.17285, 5591.8096, 989.8779), (-5.948576825966669, 10.583563721085467, 2.5974124059605828), (1.42174, 1.440379, 1.440379), "PWM_Quarry_4x3x56_118", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (806.1279, 2107.6006, 603.5078), (-6.149932409378736, -62.276058803551926, 179.76836780376937), (1.032604, 1.051243, 0.642244), "PWM_Quarry_4x3x63", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (399.03174, 2175.3276, 781.98047), (0.6144916322003664, -149.28455210417755, -1.1432802353600713), (0.7351848, 0.75382376, 0.3448246), "PWM_Quarry_4x3x64", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (733.8628, 2322.2256, 742.2705), (0.5328775446985861, -117.3076217034746, 4.907791338969396), (0.58816695, 0.753824, 0.36358175), "PWM_Quarry_4x3x65", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5546.127, 5449.0107, 6693.1777), (-1.8251955376869975, -119.6521287158353, 3.2764949816876907), (1.42174, 1.440379, 1.440379), "PWM_Quarry_4x3x66", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5506.957, 5113.277, 7524.0337), (-1.8251956294645144, -119.65212897698376, 3.2765013027467), (1.42174, 1.440379, 1.440379), "PWM_Quarry_4x3x67", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5179.051, 5746.085, 7564.059), (3.7282651093011996, 117.28281607214856, -0.4060060654543244), (1.42174, 1.440379, 1.440379), "PWM_Quarry_4x3x68", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5643.383, 5012.1494, 7705.916), (4.118569562070409, 85.61397227615379, -4.471435915839494), (1.42174, 1.77383, 1.440379), "PWM_Quarry_4x3x71", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4520.7334, 5907.1284, 8468.124), (-1.825011951241451, -117.39683146195517, -179.1590388411814), (1.42174, 1.440379, 1.440379), "PWM_Quarry_4x3x72", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5102.029, 5544.9077, 7090.3594), (3.7104045603935125, 112.91854538937065, -0.5434266483653929), (1.42174, 1.440379, 1.440379), "PWM_Quarry_4x3x74_717", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5099.3013, 5501.55, 7725.9614), (-1.7549744716663866, -49.29907029981461, -6.684265096475767), (2.8922176, 1.440379, 1.440379), "PWM_Quarry_4x3x75", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1029.0405, 5154.3403, 8256.027), (-2.6158748954578814, -70.07857467801233, -4.295745624726899), (1.42174, 1.440379, 1.440379), "PWM_Quarry_4x3x79", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3866.711, 5521.2266, 8885.719), (-4.038971001434621, -92.14114946182846, -2.9993285812322394), (1.42174, 1.440379, 1.440379), "PWM_Quarry_4x3x80", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1617.3511, 435.0337, 1327.8018), (2.1573172758302475, 53.84346384930616, 178.70558285951338), (1.691052, 2.431368, 1.813447), "PWM_Quarry_4x3x83_51", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (850.2827, 4410.2983, 7163.6836), (1.9315910113579267, -18.54516858884616, -4.797699415439922), (1.42174, 1.440379, 1.440379), "PWM_Quarry_4x3x84", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (677.09863, 5335.3564, 7524.0337), (-2.596191488167837, -22.220212020019176, -2.949066073845906), (1.42174, 1.440379, 1.440379), "PWM_Quarry_4x3x85", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4958.947, 5981.252, 1268.9316), (2.2382567582473523, -124.17907772219444, 178.85129282470956), (1.691052, 2.431368, 1.813447), "PWM_Quarry_4x3x87", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4249.3315, 6103.2964, 6290.103), (-5.52108799033496, -101.59716290118195, 0.29619608960696775), (1.42174, 1.440379, 1.440379), "PWM_Quarry_4x3x90_748", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3633.8892, 6147.755, 5274.8696), (-4.798705914852234, -128.37937976316138, 2.7494131248792053), (1.42174, 1.440379, 1.440379), "PWM_Quarry_4x3x91", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3570.8542, 5852.0356, 6289.077), (-3.8104243004149456, -145.04383830867687, 4.009133265867585), (1.42174, 1.440379, 1.440379), "PWM_Quarry_4x3x92", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5340.118, 5721.789, 5398.139), (-1.0417479656172015, 112.89462136999683, -5.386962694192997), (1.42174, 1.440379, 1.440379), "PWM_Quarry_4x3x94", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4544.556, 6036.165, 5938.233), (-3.2193599471534404, -104.64458226590145, -179.19745956012633), (1.42174, 1.440379, 1.440379), "PWM_Quarry_4x3x95", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4827.9126, 6020.797, 4928.8735), (-3.2193599471534404, -104.64458226590145, -179.19745956012633), (1.42174, 1.440379, 1.440379), "PWM_Quarry_4x3x96", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4483.2847, 6236.0967, 4654.5894), (1.8115914780177251, 146.2939655051536, -177.21968991710864), (1.42174, 1.440379, 1.440379), "PWM_Quarry_4x3x97", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5186.6025, 6060.3955, 4731.1133), (0.19390912014805115, -15.856900608820288, 173.51278673865525), (1.42174, 1.440379, 1.440379), "PWM_Quarry_4x3x98", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5513.596, 5600.958, 5613.5244), (7.359084528817193, 112.67870365218596, 1.6189741690183175), (1.42174, 1.440379, 1.440379), "PWM_Quarry_4x3x99", _folder)
if a: placed += 1
else: skipped += 1

# Batch 23: StaticMesh'PWM_Quarry_4x4x4_A' (18 instances)
_mesh_path = "/Game/Unshippable/Whitebox/Rocks/Meshes/PWM_Quarry_4x4x4_A"
_materials = ['/Game/Environments/ProcTexturing/ProcMaterial_Quarry_Atlas_2']
_folder = "Reconstruction/BD_BB_Chapter5_CavernShaft/Meshes"
a = spawn_static_mesh(_mesh_path, _materials, (2609.729, 2204.0671, 948.0), (0.0, 123.27400648864506, -0.0), (1.0, 1.0, 1.0), "PWM_Quarry_4x4x4_A_14", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3730.0, 4500.0, 3420.0), (0.0, 156.83116373173732, -0.0), (1.34375, 1.34375, 1.6875), "PWM_Quarry_4x4x4_A10_129", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4155.234, 3752.9756, 762.6924), (2.2801626409369162, 21.99475124727708, -2.367431562954653), (2.355198, 2.355198, 1.749187), "PWM_Quarry_4x4x4_A11", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3793.01, 3912.7615, 733.977), (2.2801631787603585, -106.33247043479305, -2.367431740026641), (2.355198, 2.355198, 1.749187), "PWM_Quarry_4x4x4_A12", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3630.0, 4200.0, 2890.0), (0.40044718998992856, -130.14866110909855, -179.57223798171518), (1.34375, 1.34375, 1.6875), "PWM_Quarry_4x4x4_A13", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3480.0, 4440.0, 3420.0), (0.0, -38.188662284355416, 0.0), (1.78125, 1.59375, 1.6875), "PWM_Quarry_4x4x4_A14", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2683.7, 2927.5352, 1400.0), (0.0, 3.998748702345607, -0.0), (1.0, 1.0, 1.09375), "PWM_Quarry_4x4x4_A15", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3306.3523, 4456.266, 2481.6382), (22.50876190792424, -22.172513211109507, 18.75955060640149), (0.9375, 0.84375, 2.0), "PWM_Quarry_4x4x4_A16", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2030.0, 3275.0, 1055.0), (-3.957244388949246, -129.2921040159549, -0.392791709472216), (1.09375, 1.09375, 1.0), "PWM_Quarry_4x4x4_A2_46", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2220.0, 3570.0, 990.0), (0.0, 11.249878005266776, -0.0), (1.09375, 1.09375, 1.0), "PWM_Quarry_4x4x4_A3", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5044.147, 5874.2876, 5654.005), (4.716593542772484, 62.12317814850899, -0.09866319937896581), (1.2181544, 2.612556, 3.333876), "PWM_Quarry_4x4x4_A33", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5059.6606, 5921.515, 4256.55), (4.716593542772484, 62.12317814850899, -0.09866319937896581), (1.0731566, 2.607933, 3.333876), "PWM_Quarry_4x4x4_A35", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3101.1328, 2296.7144, 456.36816), (1.5357541702011828, 126.75949335540737, -0.34783934028447827), (2.18113, 2.18113, 2.18113), "PWM_Quarry_4x4x4_A4", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2855.0, 3930.0, 1045.0), (4.902662276181501, -28.632747441728203, 5.58478730373866), (1.09375, 1.09375, 1.25), "PWM_Quarry_4x4x4_A5", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4239.729, 3494.0671, 2178.0), (0.0, 150.18502424362325, -0.0), (1.0, 1.0, 1.0), "PWM_Quarry_4x4x4_A6", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3320.0, 4220.0, 2160.0), (0.0, 0.0, -0.0), (1.0, 1.0, 2.0), "PWM_Quarry_4x4x4_A7_121", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3310.0, 4180.0, 2940.0), (-0.888000243599618, 29.80077569972932, -179.99998633797236), (1.0, 1.0, 2.0), "PWM_Quarry_4x4x4_A8", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3190.0, 4570.0, 3010.0), (-0.8880001827323346, -35.33140888535427, -179.9999863461784), (1.0, 1.0, 1.5625), "PWM_Quarry_4x4x4_A9", _folder)
if a: placed += 1
else: skipped += 1

# Batch 24: StaticMesh'PWM_Quarry_4x5x10' (8 instances)
_mesh_path = "/Game/Unshippable/Whitebox/Rocks/Meshes/PWM_Quarry_4x5x10"
_materials = ['/Game/Environments/ProcTexturing/ProcMaterial_Quarry_Atlas_A']
_folder = "Reconstruction/BD_BB_Chapter5_CavernShaft/Meshes"
a = spawn_static_mesh(_mesh_path, _materials, (597.0571, 4188.445, 7980.5703), (1.518794925404695, -97.77998875305065, 1.4024481626621477), (2.031961, 1.787539, 1.708476), "PWM_Quarry_4x5x125", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3255.265, 2909.9192, 7633.207), (3.060533070697697, -117.95148345414245, 4.723252249171002), (1.0, 1.0, 1.0), "PWM_Quarry_4x5x162", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4507.9536, 3316.5532, 637.25684), (1.8258530733818383, 93.11177721336213, -6.039306347319936), (1.0, 1.0, 1.0), "PWM_Quarry_4x5x189", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (537.50073, 143.72803, 4941.7397), (8.780113260222537, -160.41671281232357, -7.44921797462681), (2.191735, 1.892617, 1.9041146), "PWM_Quarry_4x5x240_500", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5416.8325, 5959.8223, 6825.426), (1.216811868754069, 162.6478100676328, 179.8553980126465), (2.191735, 1.892617, 1.904115), "PWM_Quarry_4x5x244", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4519.095, 5688.736, 8387.005), (-3.201568150078436, -7.077147528202345, 170.5512585108117), (2.191735, 1.892617, 1.904115), "PWM_Quarry_4x5x262", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4697.0146, 5951.1943, 7256.65), (-3.970825568277021, -179.389876843072, -178.52174902944589), (2.191735, 1.892617, 1.904115), "PWM_Quarry_4x5x271", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (-123.37598, 2599.522, 5369.965), (-6.69305507561699, -71.7517876157018, 177.1786158364249), (2.191735, 1.892617, 1.904115), "PWM_Quarry_4x5x276", _folder)
if a: placed += 1
else: skipped += 1

# Batch 25: StaticMesh'PWM_Quarry_8x8x8_A' (12 instances)
_mesh_path = "/Game/Unshippable/Whitebox/Rocks/Meshes/PWM_Quarry_8x8x8_A"
_materials = ['/Game/Environments/ProcTexturing/ProcMaterial_Quarry_Atlas_2']
_folder = "Reconstruction/BD_BB_Chapter5_CavernShaft/Meshes"
a = spawn_static_mesh(_mesh_path, _materials, (365.0, 920.0, 3315.0), (0.0, 0.0, -0.0), (0.50862426, 0.7803165, 0.9911236), "PWM_Quarry_8x8x8_A_2", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4205.548, 3450.8884, 1655.0), (0.0, -64.57284390978452, 0.0), (0.75, 0.8125, 1.0), "PWM_Quarry_8x8x8_A10", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3096.2966, 4991.25, 3139.159), (-87.3683449095164, 138.99593711518793, -17.063402733962462), (0.8125, 1.0, 1.0), "PWM_Quarry_8x8x8_A11", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3346.2966, 4391.25, 3409.159), (0.0, 55.44469795681145, -0.0), (0.65625, 0.84375, 0.84375), "PWM_Quarry_8x8x8_A12", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (365.0, 395.0, 3360.0), (0.0, 0.0, -0.0), (0.508624, 0.780316, 0.991124), "PWM_Quarry_8x8x8_A2", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3435.0, 4050.0, 1300.0), (0.0, 8.436898705086243, -0.0), (1.0, 1.0, 1.09375), "PWM_Quarry_8x8x8_A3_63", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2974.7676, 2387.6343, 1250.0), (-4.5308535687959335, 109.37567765745408, 4.363035246898164), (1.0, 1.0, 1.0), "PWM_Quarry_8x8x8_A4", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3714.161, 2595.1355, 1685.0), (0.0, -25.31222480721985, 0.0), (0.75, 0.8125, 1.0), "PWM_Quarry_8x8x8_A5_84", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3501.55, 2763.6843, 1807.0), (90.0, 0.4392133238499412, -92.37379366194597), (0.75, 0.8125, 1.0), "PWM_Quarry_8x8x8_A6", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3626.2966, 3841.25, 2089.159), (-89.55851754569878, -179.99988388196394, -179.99998633836063), (0.75, 0.8125, 1.0), "PWM_Quarry_8x8x8_A7", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3566.2966, 3951.25, 2349.159), (87.41712443054698, -1.4131365264634987, 168.35261142914416), (0.75, 0.8125, 1.0), "PWM_Quarry_8x8x8_A8", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4140.445, 3001.4136, 1755.0), (0.0, 66.89276649354126, -0.0), (0.75, 0.8125, 1.0), "PWM_Quarry_8x8x8_A9", _folder)
if a: placed += 1
else: skipped += 1

# Batch 26: StaticMesh'PWM_Quarry_Ceilling_Fissure_8x4_A' (10 instances)
_mesh_path = "/Game/Unshippable/Whitebox/Rocks/Meshes/PWM_Quarry_Ceilling_Fissure_8x4_A"
_materials = ['/Game/Environments/ProcTexturing/ProcMaterial_Quarry_Floor_8x4x1']
_folder = "Reconstruction/BD_BB_Chapter5_CavernShaft/Meshes"
a = spawn_static_mesh(_mesh_path, _materials, (2669.641, 5066.5435, 3538.9226), (0.27206004164506586, -35.40227899624651, 0.38241623278504844), (2.7044182, 2.7044182, 2.7044182), "PWM_Quarry_Ceilling_Fissure_8x4_A_19", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3453.6892, 5328.5444, 3240.0986), (0.0, -35.403198436492026, 0.0), (4.485649, 4.382154, 2.704418), "PWM_Quarry_Ceilling_Fissure_8x4_A10", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5764.213, 3601.6611, 3867.7585), (-0.14114373629977012, 82.69354421216532, -1.102905099431083), (3.00546, 3.342164, 2.154499), "PWM_Quarry_Ceilling_Fissure_8x4_A11", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5983.7827, 5007.1357, 3771.9949), (0.3154617888657983, 82.6889328594003, -3.5165707071729764), (3.00546, 3.342164, 3.5896614), "PWM_Quarry_Ceilling_Fissure_8x4_A12", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1977.4492, 5742.44, 3543.8105), (-1.2337952421750962, -22.707856263266535, 0.516280377491921), (2.704418, 2.704418, 2.704418), "PWM_Quarry_Ceilling_Fissure_8x4_A2", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3435.5374, 5316.1387, 3532.7349), (0.0, -35.403198436492026, 0.0), (2.704418, 2.704418, 2.704418), "PWM_Quarry_Ceilling_Fissure_8x4_A3", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3673.7693, 5498.8164, 3532.7349), (0.0, -25.40319790002439, 0.0), (4.1956973, 4.155221, 2.704418), "PWM_Quarry_Ceilling_Fissure_8x4_A4", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3049.743, 5343.6284, 3532.7349), (0.0, -35.403198436492026, 0.0), (3.672761, 3.5930371, 2.704418), "PWM_Quarry_Ceilling_Fissure_8x4_A5", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4870.2896, 5294.296, 3566.3262), (1.4257324974032732, -35.714658331766884, -2.3678282369580037), (4.00061, 4.1123486, 2.704418), "PWM_Quarry_Ceilling_Fissure_8x4_A6", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5947.053, 1983.8148, 3864.692), (-0.3063658671654297, 95.85860359871015, -0.9541931110051344), (3.00546, 2.9019537, 2.154499), "PWM_Quarry_Ceilling_Fissure_8x4_A8", _folder)
if a: placed += 1
else: skipped += 1

# Batch 27: StaticMesh'PWM_Quarry_Ceilling_Fissure_8x4_B' (4 instances)
_mesh_path = "/Game/Unshippable/Whitebox/Rocks/Meshes/PWM_Quarry_Ceilling_Fissure_8x4_B"
_materials = ['/Game/Environments/ProcTexturing/ProcMaterial_Quarry_Ceilling_Fissure_8x8']
_folder = "Reconstruction/BD_BB_Chapter5_CavernShaft/Meshes"
a = spawn_static_mesh(_mesh_path, _materials, (2509.944, 589.7925, 863.3965), (0.8157804947020664, -29.544373432154313, 8.196210578313416), (1.469796, 1.469796, 1.1052941), "PWM_Quarry_Ceilling_Fissure_8x4_B10", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3854.1582, 460.8506, 811.5713), (-1.4389037261877469, 8.819213130639852, 8.345213111608533), (1.469796, 1.469796, 1.469796), "PWM_Quarry_Ceilling_Fissure_8x4_B16", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2348.1023, 3505.3386, 797.5879), (-0.8734130785563803, 58.296888290148324, 0.34242443967135655), (1.378198, 1.3781984, 0.9272304), "PWM_Quarry_Ceilling_Fissure_8x4_B7", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1057.832, 1714.4282, 799.9688), (-0.4896543304333936, -35.39047555283813, 12.140059702348134), (1.469796, 1.469796, 1.469796), "PWM_Quarry_Ceilling_Fissure_8x4_B9", _folder)
if a: placed += 1
else: skipped += 1

# Batch 28: StaticMesh'PWM_Quarry_Floor_2x2x2_A' (7 instances)
_mesh_path = "/Game/Unshippable/Whitebox/Rocks/Meshes/PWM_Quarry_Floor_2x2x2_A"
_materials = ['/Game/Environments/ProcTexturing/ProcMaterial_Quarry_Atlas_3']
_folder = "Reconstruction/BD_BB_Chapter5_CavernShaft/Meshes"
a = spawn_static_mesh(_mesh_path, _materials, (4290.0, 3090.0, 2020.0), (0.0, 82.08248864370157, -0.0), (1.84375, 1.6875, 1.4375), "PWM_Quarry_Floor_2x2x2_A_111", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3500.0, 3610.0, 2560.0), (0.0, 18.813396257801596, -0.0), (1.8125, 1.0, 1.0), "PWM_Quarry_Floor_2x2x2_A2_140", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3500.0, 3790.0, 2650.0), (0.0, 176.6644426372004, -0.0), (2.3125, 1.1875, 1.0), "PWM_Quarry_Floor_2x2x2_A3", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1950.0, 2070.0, 785.0), (0.0, 47.369407371624035, -0.0), (1.0, 1.0, 1.0), "PWM_Quarry_Floor_2x2x2_A4_2", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2280.0, 1900.0, 790.0), (0.0, 80.77112717546385, -0.0), (1.0, 1.0, 1.0), "PWM_Quarry_Floor_2x2x2_A5", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3146.3293, 2231.507, 1750.0), (0.0, -24.792601969646103, 0.0), (1.84375, 1.6875, 1.4375), "PWM_Quarry_Floor_2x2x2_A6", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4110.0, 4550.0, 3530.0), (0.0, 39.89485488719407, -0.0), (1.84375, 1.6875, 1.4375), "PWM_Quarry_Floor_2x2x2_A7", _folder)
if a: placed += 1
else: skipped += 1

# Batch 29: StaticMesh'PWM_Quarry_Floor_4x4x4_A' (8 instances)
_mesh_path = "/Game/Unshippable/Whitebox/Rocks/Meshes/PWM_Quarry_Floor_4x4x4_A"
_materials = ['/Game/Environments/ProcTexturing/ProcMaterial_Quarry_Atlas_4']
_folder = "Reconstruction/BD_BB_Chapter5_CavernShaft/Meshes"
a = spawn_static_mesh(_mesh_path, _materials, (2239.2466, 2410.7861, 895.0), (0.0, -36.56243944014067, 0.0), (1.0, 1.0, 1.0), "PWM_Quarry_Floor_4x4x4_A_20", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2097.2244, 2657.1152, 895.0), (0.0, 0.00037670135835600645, -0.0), (1.0, 1.21875, 1.0), "PWM_Quarry_Floor_4x4x4_A2", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3489.3184, 2432.0789, 1987.0), (0.0, -30.937593110196605, 0.0), (1.28125, 1.0, 1.0), "PWM_Quarry_Floor_4x4x4_A3_88", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4239.3184, 4322.079, 3267.0), (0.0, -24.012389674572667, 0.0), (1.28125, 1.0, 0.75), "PWM_Quarry_Floor_4x4x4_A4", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4139.3184, 4322.079, 2867.0), (10.107298126635973, 154.00665293361345, 173.75074911246128), (1.28125, 0.90625, 1.34375), "PWM_Quarry_Floor_4x4x4_A5", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4649.3184, 4682.079, 3537.0), (0.0, -20.820771846882447, 0.0), (2.09375, 1.25, 1.0), "PWM_Quarry_Floor_4x4x4_A6", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3689.2466, 3960.7861, 2795.0), (0.0, -30.642179880646093, 0.0), (1.25, 1.0, 0.6875), "PWM_Quarry_Floor_4x4x4_A7", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3959.2466, 4050.7861, 2725.0), (0.0, 38.18823752160506, -0.0), (1.34375, 1.125, 1.0), "PWM_Quarry_Floor_4x4x4_A8", _folder)
if a: placed += 1
else: skipped += 1

# Batch 30: StaticMesh'PWM_Quarry_Floor_6x2x1_A' (7 instances)
_mesh_path = "/Game/Unshippable/Whitebox/Rocks/Meshes/PWM_Quarry_Floor_6x2x1_A"
_materials = ['/Game/Environments/ProcTexturing/ProcMaterial_Quarry_Atlas_4']
_folder = "Reconstruction/BD_BB_Chapter5_CavernShaft/Meshes"
a = spawn_static_mesh(_mesh_path, _materials, (1960.4618, 2676.121, 1068.0), (0.0, -92.11987602191641, 0.0), (1.0, 1.0, 1.0), "PWM_Quarry_Floor_6x2x1_A_5", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2195.1304, 2979.1384, 1155.2206), (6.836077428100264e-06, 6.318697373640499, -22.499877606730273), (1.21875, 1.46875, 1.0), "PWM_Quarry_Floor_6x2x1_A2", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1660.1304, 2724.1384, 835.2206), (-5.344512577900611, -64.30860182739633, 1.5954891644601292), (1.0, 1.0, 1.15625), "PWM_Quarry_Floor_6x2x1_A3", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2262.184, 3378.6047, 1267.5913), (-3.9674072491450163, -100.04529684661053, -8.184784276372488), (1.0, 1.625, 1.40625), "PWM_Quarry_Floor_6x2x1_A4", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3793.9197, 3309.1807, 2246.3196), (-2.6213379860662194, 160.2145763765777, 15.248512429708157), (1.59375, 1.875, 1.34375), "PWM_Quarry_Floor_6x2x1_A5", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3490.0, 4470.0, 1700.0), (-6.497741781806263, -21.30377148382561, 4.3672738250172065e-06), (1.0, 1.0, 1.0), "PWM_Quarry_Floor_6x2x1_A6_6", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3190.0, 4500.0, 1710.0), (-6.497740519787254, -172.65121705451597, 7.679928398607053e-06), (1.0, 1.0, 1.0), "PWM_Quarry_Floor_6x2x1_A7_9", _folder)
if a: placed += 1
else: skipped += 1

# Batch 31: StaticMesh'PWM_Quarry_Floor_8x4x1_A' (19 instances)
_mesh_path = "/Game/Unshippable/Whitebox/Rocks/Meshes/PWM_Quarry_Floor_8x4x1_A"
_materials = ['/Game/Environments/ProcTexturing/ProcMaterial_Quarry_Atlas_6']
_folder = "Reconstruction/BD_BB_Chapter5_CavernShaft/Meshes"
a = spawn_static_mesh(_mesh_path, _materials, (922.9801, 4217.4956, 6299.5933), (0.0, -44.99999866815529, 0.0), (2.4682631, 2.4682631, 2.4682631), "PWM_Quarry_Floor_8x4x1_A_5", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4700.9727, 5596.9517, 7090.1377), (0.0, 93.18637000470372, -0.0), (2.468263, 2.468263, 2.468263), "PWM_Quarry_Floor_8x4x1_A10", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5313.369, 693.0198, 5499.8833), (0.0, 22.735733890495393, -0.0), (2.8194823, 3.292231, 2.468263), "PWM_Quarry_Floor_8x4x1_A11", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (21.0, 3390.0, 740.0), (0.0, 89.99991067642716, -0.0), (1.09375, 1.0, 1.0), "PWM_Quarry_Floor_8x4x1_A12_6", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2240.3723, 2351.5745, 1071.0), (0.0, -28.42160170088671, 0.0), (1.0, 1.0, 1.0), "PWM_Quarry_Floor_8x4x1_A13_2", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2235.3723, 3606.5745, 1226.0), (0.0, -160.60918778437332, 0.0), (1.0, 1.0, 1.0), "PWM_Quarry_Floor_8x4x1_A14", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2653.4954, 3293.529, 1436.934), (2.500784875720421, 19.293169121878364, 3.007841312884365), (1.0, 1.0, 1.28125), "PWM_Quarry_Floor_8x4x1_A15_52", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2650.5225, 3532.6812, 1381.928), (-1.319030721097273, -149.51302298786746, -3.3813784137533163), (1.15625, 1.0, 1.65625), "PWM_Quarry_Floor_8x4x1_A16", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3587.7593, 2472.977, 2122.6436), (0.0, -25.31243662145636, 0.0), (1.0, 1.0, 1.28125), "PWM_Quarry_Floor_8x4x1_A17", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3985.829, 2696.7483, 2149.9429), (3.840211682597256, 53.48836801054525, 2.8154977769994876), (1.0, 1.40625, 1.4375), "PWM_Quarry_Floor_8x4x1_A18", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4590.0, 4700.0, 3690.0), (0.0, -16.20663204488754, 0.0), (1.28125, 1.15625, 0.90625), "PWM_Quarry_Floor_8x4x1_A19_135", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1065.5775, 3120.4324, 6299.5933), (0.0, -118.84956695308985, 0.0), (2.468263, 2.468263, 2.468263), "PWM_Quarry_Floor_8x4x1_A2", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (711.37317, 1921.3029, 6967.323), (0.0, -8.966857152382229, 0.0), (2.468263, 2.468263, 2.468263), "PWM_Quarry_Floor_8x4x1_A3", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1796.907, 1300.3373, 6967.323), (0.0, -62.440120142852244, 0.0), (2.468263, 2.468263, 2.468263), "PWM_Quarry_Floor_8x4x1_A4", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4656.052, 270.87317, 5499.8833), (0.0, 76.20890044780029, -0.0), (2.468263, 2.468263, 2.468263), "PWM_Quarry_Floor_8x4x1_A5", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5366.1113, 1300.3367, 5499.8833), (0.0, 22.735733890495393, -0.0), (2.468263, 2.468263, 2.468263), "PWM_Quarry_Floor_8x4x1_A6", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5467.868, 1879.4724, 7491.0693), (0.0, 112.55167414688495, -0.0), (2.468263, 2.468263, 2.468263), "PWM_Quarry_Floor_8x4x1_A7", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5491.941, 2838.048, 7491.0693), (0.0, 54.13273265296226, -0.0), (1.9622229, 2.468263, 2.468263), "PWM_Quarry_Floor_8x4x1_A8", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5638.083, 5081.29, 7090.1377), (0.0, -171.99428531982088, 0.0), (2.468263, 2.468263, 2.468263), "PWM_Quarry_Floor_8x4x1_A9", _folder)
if a: placed += 1
else: skipped += 1

# Batch 32: StaticMesh'PWM_Quarry_Floor_8x8x8_A' (4 instances)
_mesh_path = "/Game/Unshippable/Whitebox/Rocks/Meshes/PWM_Quarry_Floor_8x8x8_A"
_materials = ['/Game/Environments/ProcTexturing/ProcMaterial_Quarry_Atlas_6']
_folder = "Reconstruction/BD_BB_Chapter5_CavernShaft/Meshes"
a = spawn_static_mesh(_mesh_path, _materials, (2517.0735, 2665.3308, 682.0), (0.0, -39.10989355770461, 0.0), (1.0, 1.0, 1.0), "PWM_Quarry_Floor_8x8x8_A_11", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3046.6838, 2899.4949, 1242.0095), (0.0, -64.92590176491639, 0.0), (1.0, 1.0, 1.0), "PWM_Quarry_Floor_8x8x8_A2", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3712.144, 3017.5017, 1792.6658), (0.4125297333483403, -16.61969016617768, -2.7821045595291363), (0.90625, 1.1875, 1.0), "PWM_Quarry_Floor_8x8x8_A3", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3896.4692, 3733.7922, 2053.122), (-0.20831300146921375, 159.1966704712996, 2.8043287449162237), (0.90625, 0.9375, 1.0496948), "PWM_Quarry_Floor_8x8x8_A4", _folder)
if a: placed += 1
else: skipped += 1

# Batch 33: StaticMesh'PWM_Quarry_RockDebris_A' (56 instances)
_mesh_path = "/Game/Unshippable/Whitebox/Rocks/Meshes/PWM_Quarry_RockDebris_A"
_materials = ['/Game/Environments/ProcTexturing/ProcMaterial_Quarry_Atlas_5']
_folder = "Reconstruction/BD_BB_Chapter5_CavernShaft/Meshes"
a = spawn_static_mesh(_mesh_path, _materials, (1750.9844, 2530.1482, 793.27344), (0.9890659983227432, 90.00000935308638, 2.4992144097581318e-08), (1.7187119, 1.7187119, 1.7187119), "PWM_Quarry_RockDebris_A_60", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2458.8086, 1099.0605, 794.0078), (0.06289402696199482, -55.61883390179198, 0.9683969796553499), (1.868208, 1.868208, 1.868208), "PWM_Quarry_RockDebris_A10", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2743.787, 1029.6794, 794.11426), (0.06289404838733134, -37.825313526796485, 0.968397011636542), (1.868208, 1.868208, 1.868208), "PWM_Quarry_RockDebris_A11", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2169.9238, 2083.1372, 792.08594), (0.17081620308652973, 174.55235429436874, 0.10798322994213451), (2.280443, 2.280443, 2.280443), "PWM_Quarry_RockDebris_A13", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2785.5493, 1739.4292, 784.0674), (0.17081620418580712, 174.5523542940254, 0.10798301191858066), (1.838582, 1.838582, 1.838582), "PWM_Quarry_RockDebris_A14", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2385.5232, 1907.4888, 804.0556), (1.0374646762893318, 37.091856691869665, -1.037994377657644), (1.838582, 1.838582, 1.838582), "PWM_Quarry_RockDebris_A15", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4686.9746, 2063.338, 795.292), (0.17081620418580712, 174.5523542940254, 0.10798301191858066), (1.838582, 1.838582, 1.838582), "PWM_Quarry_RockDebris_A16", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4918.9053, 2395.2388, 795.37695), (0.17081618971066928, -129.07012750567662, 0.10798303346970514), (1.838582, 1.838582, 1.838582), "PWM_Quarry_RockDebris_A17", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4455.3125, 1905.7804, 794.48047), (0.2726680097728502, -131.79595326677057, 0.22198278585778713), (1.7360795, 1.7360795, 1.7360795), "PWM_Quarry_RockDebris_A18", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4068.9849, 1726.7966, 791.88184), (0.3597649156655222, -85.49634056163933, -0.8834838568313262), (1.736079, 1.736079, 1.736079), "PWM_Quarry_RockDebris_A19", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1517.5015, 3040.9304, 788.25586), (-0.8386840670213599, 89.93710187909842, -1.214081018474765), (1.718712, 1.718712, 1.718712), "PWM_Quarry_RockDebris_A2", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3730.1736, 1715.6544, 806.3535), (-4.159820774040185, -85.54758411482497, -0.36257941530551013), (1.736079, 1.736079, 1.736079), "PWM_Quarry_RockDebris_A20", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3427.7493, 1577.8817, 795.51465), (0.0, 90.0000030488508, -0.0), (1.2176902, 1.2176902, 1.2176902), "PWM_Quarry_RockDebris_A21", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4829.038, 3358.1484, 801.2705), (4.9497520087442953e-08, 90.00000762175158, -1.2729492608411115), (1.838582, 1.838582, 1.838582), "PWM_Quarry_RockDebris_A22", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4965.301, 2895.611, 795.1201), (-0.2933349812885443, -61.797461067143324, -0.04693603637310328), (1.838582, 1.838582, 1.838582), "PWM_Quarry_RockDebris_A23", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5036.247, 2353.7495, 789.06445), (-0.293334933764006, 179.56385723687183, -0.04693603925594497), (1.838582, 1.838582, 1.838582), "PWM_Quarry_RockDebris_A24", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4991.75, 3976.9927, 787.6367), (0.0, -75.02612791624641, 0.0), (1.838582, 1.838582, 1.838582), "PWM_Quarry_RockDebris_A25", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4128.481, 4488.5337, 795.00195), (0.0, 22.023337704496733, -0.0), (1.838582, 1.838582, 1.4636256), "PWM_Quarry_RockDebris_A26", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4563.73, 4424.1567, 795.1865), (0.002998455119192462, -89.39388777053863, -0.28280638759022564), (1.838582, 1.838582, 1.463626), "PWM_Quarry_RockDebris_A27", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4772.7197, 4380.208, 793.7471), (0.002998443111627236, -26.514708228394444, -0.2828063497624773), (1.838582, 1.838582, 1.463626), "PWM_Quarry_RockDebris_A28", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3571.6309, 4613.0674, 795.0), (0.002998452153767122, 23.390260023197847, -0.28280641046235533), (1.838582, 1.838582, 1.463626), "PWM_Quarry_RockDebris_A29", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1733.8413, 3390.1343, 791.72363), (0.0, 90.0000030488508, -0.0), (2.270096, 2.270096, 2.270096), "PWM_Quarry_RockDebris_A3", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2994.7695, 4430.661, 794.30176), (0.002998447785271037, 16.113494921698944, -0.2828064077741727), (1.838582, 1.838582, 1.463626), "PWM_Quarry_RockDebris_A30", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2215.4795, 4108.716, 789.38184), (0.002998447785271037, 16.113494921698944, -0.2828064077741727), (1.838582, 1.838582, 1.463626), "PWM_Quarry_RockDebris_A31", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2478.0417, 4275.0933, 793.29785), (0.0029984461505212587, 41.70276113404843, -0.2828063912646866), (1.838582, 1.838582, 1.463626), "PWM_Quarry_RockDebris_A32", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1892.2427, 3862.185, 795.37305), (0.0029984562018248754, 75.1994428858515, -0.2828063917564013), (1.5357429, 1.5357429, 1.1607869), "PWM_Quarry_RockDebris_A33", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2637.7676, 4458.338, 797.2549), (0.0029984507520002053, -84.7028828456968, -0.2828063802721452), (1.14519, 1.14519, 0.77023417), "PWM_Quarry_RockDebris_A34", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1204.7769, 4765.7505, 803.14355), (0.8218697024720982, 149.98480443531625, 1.2752526788767935), (1.785002, 1.785002, 1.785002), "PWM_Quarry_RockDebris_A35", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1086.9927, 4373.998, 794.50684), (0.0, 101.5343915515587, -0.0), (1.4602865, 1.4602865, 1.4602865), "PWM_Quarry_RockDebris_A36", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3125.67, 1537.2981, 791.1193), (-6.767468210668364e-10, 15.7713788415052, -1.2581788163555663), (1.21769, 1.21769, 1.21769), "PWM_Quarry_RockDebris_A37_1", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5716.3228, 2820.2622, 792.188), (-0.29333499007087077, 90.20508829132226, -0.04693606460608576), (1.838582, 1.838582, 1.838582), "PWM_Quarry_RockDebris_A38", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1929.0635, 5235.41, 794.24414), (0.8218699796793493, 149.9848044429831, 1.2752529606218659), (1.785002, 1.785002, 1.785002), "PWM_Quarry_RockDebris_A39", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1372.7153, 3148.9895, 786.3096), (0.0, 149.97705785280039, -0.0), (1.7850019, 1.7850019, 1.7850019), "PWM_Quarry_RockDebris_A4", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5586.3228, 2150.2622, 792.188), (-0.29333494665871707, 61.759976278191395, -0.04693602473147606), (1.838582, 1.838582, 1.838582), "PWM_Quarry_RockDebris_A40", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1495.4922, 4763.5674, 800.77356), (0.5166766962359646, 51.08261212748987, -3.3739014267935508), (1.785002, 1.785002, 1.785002), "PWM_Quarry_RockDebris_A41", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3318.241, 5388.3936, 800.22656), (2.288414579897532, 55.31554776252083, -1.1770020658571831), (1.785002, 1.785002, 1.785002), "PWM_Quarry_RockDebris_A42", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2898.0254, 5232.5835, 798.4219), (1.7835522797270824, 55.29384446490386, -1.8036193524657982), (1.785002, 1.785002, 1.785002), "PWM_Quarry_RockDebris_A43", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5495.619, 4074.4395, 794.76013), (-0.29333496975221035, 141.49745158374546, -0.046936045077998194), (1.838582, 1.838582, 1.838582), "PWM_Quarry_RockDebris_A44", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4067.94, 5286.6416, 795.541), (1.783552231856879, 51.11626387364162, -1.803619671087661), (1.785002, 1.785002, 1.785002), "PWM_Quarry_RockDebris_A45", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3527.9536, 5324.3735, 794.3594), (0.0, 94.17746207537267, -0.0), (1.785002, 1.785002, 1.785002), "PWM_Quarry_RockDebris_A46", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4838.339, 5150.2617, 807.80743), (2.489842882733012, 51.09635128544439, -2.37341327686152), (1.785002, 1.785002, 1.785002), "PWM_Quarry_RockDebris_A47", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4351.1284, 5184.69, 800.0), (1.379670833256981, 51.144465252007635, -0.5866089175652832), (1.785002, 1.785002, 1.785002), "PWM_Quarry_RockDebris_A48", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (138.27094, 3132.1116, 794.0), (0.002998466118626065, 80.80102705663285, -0.2828063875741771), (1.6, 1.6, 1.0), "PWM_Quarry_RockDebris_A49", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (552.2715, 2332.7283, 794.125), (0.0, 32.90236920986243, -0.0), (1.8682076, 1.8682076, 1.8682076), "PWM_Quarry_RockDebris_A5_66", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5709.46, 4678.79, 848.98145), (2.6127795704560386, 51.15651146145692, -0.7737427509083236), (1.785002, 1.785002, 1.785002), "PWM_Quarry_RockDebris_A50", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2426.2974, 5473.6226, 835.4053), (8.057540901127359, 50.82385132787563, -3.682281292740092), (1.785002, 1.785002, 2.3370073), "PWM_Quarry_RockDebris_A52", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (556.2954, 2379.782, 796.5801), (-3.2243343886591087, 90.0000028770847, 1.5048195787115017e-08), (1.718712, 1.718712, 2.3844988), "PWM_Quarry_RockDebris_A53_328", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (68.76758, 3708.338, 794.0), (0.00299845296071077, -20.015198756814147, -0.28280638103268674), (1.2, 1.2, 1.0), "PWM_Quarry_RockDebris_A54", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4259.78, 1033.5281, 807.65234), (3.748421431750753, -85.78192224187327, -1.5204466608326892), (1.736079, 1.736079, 1.947032), "PWM_Quarry_RockDebris_A55", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4970.453, 1195.5515, 807.2207), (3.6812337973437192, -85.72308014216799, -0.6140747066923818), (1.736079, 1.736079, 1.947032), "PWM_Quarry_RockDebris_A56", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5252.7036, 1391.769, 801.1869), (1.8474089576547255, -85.83981065968754, -2.4509890065017657), (1.736079, 1.736079, 1.947032), "PWM_Quarry_RockDebris_A57", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5875.8687, 1636.3464, 841.62695), (-0.170837362841877, -85.73188626589781, -0.901916375893843), (1.736079, 1.736079, 1.947032), "PWM_Quarry_RockDebris_A58", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (930.7822, 2363.933, 791.33594), (0.0, -11.0066534903019, 0.0), (1.868208, 1.868208, 1.868208), "PWM_Quarry_RockDebris_A6", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1078.314, 1928.7478, 797.19434), (0.06289381928201224, -11.005159113232935, 0.9683971717225516), (1.868208, 1.868208, 1.868208), "PWM_Quarry_RockDebris_A7", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1994.8619, 1144.4326, 795.4834), (0.06289401090187417, -11.005159111613972, 0.9683971532629738), (1.868208, 1.868208, 1.868208), "PWM_Quarry_RockDebris_A8", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1649.3073, 1521.124, 792.33105), (0.06289402696199482, -55.61883390179198, 0.9683969796553499), (1.868208, 1.868208, 1.868208), "PWM_Quarry_RockDebris_A9", _folder)
if a: placed += 1
else: skipped += 1

# Batch 34: StaticMesh'PWM_Quarry_RockDebris_A_Optimized' (19 instances)
_mesh_path = "/Game/Unshippable/Whitebox/Rocks/Meshes/PWM_Quarry_RockDebris_A_Optimized"
_materials = ['/Game/Environments/ProcTexturing/ProcMaterial_Quarry_RockDebris_A']
_folder = "Reconstruction/BD_BB_Chapter5_CavernShaft/Meshes"
a = spawn_static_mesh(_mesh_path, _materials, (5421.668, 5138.006, 3734.804), (2.2200445322036013, 0.0, -0.0), (1.5806041, 1.5806041, 1.5806041), "PWM_Quarry_RockDebris_A_Optimized_174", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5239.2744, 4662.909, 3731.1763), (-2.8273619176822193, 159.87493721305373, -1.3884580102664879), (1.8863312, 1.8863312, 1.8863312), "PWM_Quarry_RockDebris_A_Optimized10", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5975.6353, 1986.8623, 3994.6062), (1.005321970384857, -57.19201962400988, -0.36523443951243134), (1.6695766, 1.6695766, 1.6695766), "PWM_Quarry_RockDebris_A_Optimized11", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5800.88, 2327.3782, 3994.6062), (1.0053219625193288, -31.286681849310156, -0.36523435825720635), (1.4203572, 1.4203572, 1.4203572), "PWM_Quarry_RockDebris_A_Optimized12", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5972.7046, 1513.2955, 3998.1016), (-0.01007079791471202, -31.281432730432723, 0.251806833352651), (1.420357, 1.420357, 1.420357), "PWM_Quarry_RockDebris_A_Optimized13", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5756.052, 4204.35, 4000.5078), (0.29954475626756016, 73.28242673535685, 1.5061918330899154e-07), (1.2852827, 1.2852827, 0.902079), "PWM_Quarry_RockDebris_A_Optimized15", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5761.8423, 4544.7354, 4002.2314), (-0.23895265034194554, -69.63689088862593, -0.1805114622396308), (1.285283, 1.285283, 0.902079), "PWM_Quarry_RockDebris_A_Optimized17_1", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1704.3939, 5934.0674, 3711.657), (-1.6654662619614564, -29.403747045281268, 0.9385302198678953), (2.289594, 2.101826, 2.289594), "PWM_Quarry_RockDebris_A_Optimized18", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5696.688, 3561.69, 4000.9414), (-0.11499022086573354, -39.28171480742513, -0.27655027230482276), (1.285283, 1.285283, 0.902079), "PWM_Quarry_RockDebris_A_Optimized19", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (6087.582, 4946.221, 3990.7246), (-1.1379394756297945, 0.0, -0.0), (2.342839, 2.342839, 2.342839), "PWM_Quarry_RockDebris_A_Optimized2", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5699.9727, 3859.3328, 4002.429), (-0.25195309890332374, -73.98300424592604, -0.16189573010928776), (1.285283, 1.285283, 0.902079), "PWM_Quarry_RockDebris_A_Optimized20", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5696.336, 2829.2986, 4001.8037), (-0.25195309890332374, -73.98300424592604, -0.16189573010928776), (1.285283, 1.285283, 0.902079), "PWM_Quarry_RockDebris_A_Optimized21", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (6131.523, 1270.4935, 3996.2695), (-1.1379394756297945, 0.0, -0.0), (1.591809, 1.591809, 1.591809), "PWM_Quarry_RockDebris_A_Optimized3", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4441.6304, 5583.1343, 3697.49), (0.0, 159.79743846239384, -0.0), (2.289594, 2.289594, 2.289594), "PWM_Quarry_RockDebris_A_Optimized4_179", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4018.5847, 5840.3574, 3703.3962), (0.0, 159.79743846239384, -0.0), (2.289594, 2.289594, 2.289594), "PWM_Quarry_RockDebris_A_Optimized5", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2842.2305, 4918.1006, 3701.5852), (0.40804227866844744, -37.00726129340794, 0.5413628303719457), (1.8592567, 1.6714892, 1.8592567), "PWM_Quarry_RockDebris_A_Optimized6", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2461.718, 5249.093, 3693.6968), (0.0, -29.390137731732455, 0.0), (2.289594, 2.101826, 2.289594), "PWM_Quarry_RockDebris_A_Optimized7", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2103.0022, 5835.0913, 3698.3235), (0.0, 94.97652178778984, -0.0), (2.289594, 2.101826, 2.289594), "PWM_Quarry_RockDebris_A_Optimized8", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4001.1614, 4815.1357, 3698.0996), (-0.4912109358522207, -15.998992439479132, -1.713104072157736), (1.8377295, 1.8377295, 1.8377295), "PWM_Quarry_RockDebris_A_Optimized9", _folder)
if a: placed += 1
else: skipped += 1

# Batch 35: StaticMesh'PWM_Quarry_RockDebris_C' (1 instances)
_mesh_path = "/Game/Unshippable/Whitebox/Rocks/Meshes/PWM_Quarry_RockDebris_C"
_materials = ['/Game/Environments/ProcTexturing/ProcMaterial_Quarry_RockDebris_A']
_folder = "Reconstruction/BD_BB_Chapter5_CavernShaft/Meshes"
a = spawn_static_mesh(_mesh_path, _materials, (5508.6523, 5559.7856, 3730.584), (0.0, 0.0, -0.0), (1.6531526, 1.6531526, 1.6531526), "PWM_Quarry_RockDebris_C_171", _folder)
if a: placed += 1
else: skipped += 1

# Batch 36: StaticMesh'SM_Debris_Floor_01' (2 instances)
_mesh_path = "/Game/Unshippable/Whitebox/Rocks/Meshes/SM_Debris_Floor_01"
_materials = ['/Game/Environments/ProcTexturing/ProcMaterial_Quarry_RockDebris_A']
_folder = "Reconstruction/BD_BB_Chapter5_CavernShaft/Meshes"
a = spawn_static_mesh(_mesh_path, _materials, (2346.9524, 5843.521, 3703.3484), (4.272869713499951, 120.70092670873406, 2.5332900319628564), (2.831676, 2.831676, 2.831676), "SM_Debris_Floor_2", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3439.0112, 5934.656, 3696.803), (0.0, -32.04464490071689, 0.0), (2.8316755, 2.8316755, 2.8316755), "SM_Debris_Floor_01_209", _folder)
if a: placed += 1
else: skipped += 1

# ======================================================================
# PHASE 2: ConstructionCatalog  (construction blocks)
# ======================================================================
unreal.log(f"[{BUBBLE_NAME}] Phase 2: Placing construction blocks...")

# Construction blocks use DecoVolume transforms (matched by Name)
_folder = "Reconstruction/BD_BB_Chapter5_CavernShaft/Construction"

# Construction: AB_Mines_Scaffolding_Beam_Panels_3m_Broken_A_2
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Scaffolding
#   Volume: EMorSimpleShape::Empty, BoxExtent: (100.0, 100.0, 100.0)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (3645.7605, 5391.0303, 865.0), (0.0, 104.9999077325177, -0.0), (2.0000, 2.0000, 2.0000), "AB_Mines_Scaffolding_Beam_Panels_3m_Broken_A_2", _folder)
if a: placed += 1
else: skipped += 1

# Construction: AB_Mines_Scaffolding_Beam_Panels_3m_Broken_A3_2
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Scaffolding
#   Volume: EMorSimpleShape::Empty, BoxExtent: (100.0, 100.0, 100.0)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (5421.989, 4927.0264, 899.0), (0.0, 168.74973743329258, -0.0), (2.0000, 2.0000, 2.0000), "AB_Mines_Scaffolding_Beam_Panels_3m_Broken_A3_2", _folder)
if a: placed += 1
else: skipped += 1

# Construction: AB_Mines_Scaffolding_Broken_Segment_A_2
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Scaffolding
#   Volume: EMorSimpleShape::Empty, BoxExtent: (100.0, 100.0, 100.0)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (3304.0125, 5349.039, 849.594), (-11.24997147319374, -104.06275112119981, 3.261395662148281e-06), (2.0000, 2.0000, 2.0000), "AB_Mines_Scaffolding_Broken_Segment_A_2", _folder)
if a: placed += 1
else: skipped += 1

# Construction: AB_Mines_Scaffolding_Broken_Segment_A10
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Scaffolding
#   Volume: EMorSimpleShape::Empty, BoxExtent: (100.0, 100.0, 100.0)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (395.0, 1400.0007, 1590.0), (0.0, 179.99981558486024, -0.0), (2.0000, 2.0000, 2.0000), "AB_Mines_Scaffolding_Broken_Segment_A10", _folder)
if a: placed += 1
else: skipped += 1

# Construction: AB_Mines_Scaffolding_Broken_Segment_A11
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Scaffolding
#   Volume: EMorSimpleShape::Empty, BoxExtent: (100.0, 100.0, 100.0)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (395.0011, 1700.0009, 1590.0), (0.0, 179.99981558486024, -0.0), (2.0000, 2.0000, 2.0000), "AB_Mines_Scaffolding_Broken_Segment_A11", _folder)
if a: placed += 1
else: skipped += 1

# Construction: AB_Mines_Scaffolding_Broken_Segment_A12
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Scaffolding
#   Volume: EMorSimpleShape::Empty, BoxExtent: (100.0, 100.0, 100.0)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (563.9763, 1974.9633, 918.8541), (-28.576354963271342, 84.74207020723222, 2.829230261789583), (2.0000, 2.0000, 2.0000), "AB_Mines_Scaffolding_Broken_Segment_A12", _folder)
if a: placed += 1
else: skipped += 1

# Construction: AB_Mines_Scaffolding_Broken_Segment_A13_2
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Scaffolding
#   Volume: EMorSimpleShape::Empty, BoxExtent: (100.0, 100.0, 100.0)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (5297.6636, 4931.998, 837.5267), (-10.97625673647394, 175.1126990484422, 3.660467136850467), (2.0000, 2.0000, 2.0000), "AB_Mines_Scaffolding_Broken_Segment_A13_2", _folder)
if a: placed += 1
else: skipped += 1

# Construction: AB_Mines_Scaffolding_Broken_Segment_A14
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Scaffolding
#   Volume: EMorSimpleShape::Empty, BoxExtent: (100.0, 100.0, 100.0)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (4963.5776, 4892.8677, 809.85846), (-6.985869485836914, -117.43599984563896, -2.547485094870799), (2.0000, 2.0000, 2.0000), "AB_Mines_Scaffolding_Broken_Segment_A14", _folder)
if a: placed += 1
else: skipped += 1

# Construction: AB_Mines_Scaffolding_Broken_Segment_A15
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Scaffolding
#   Volume: EMorSimpleShape::Empty, BoxExtent: (100.0, 100.0, 100.0)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (4378.245, 3967.7737, 1174.5461), (-5.286378368965032, 48.1016907183828, -8.991699881218699), (2.0000, 2.0000, 2.0000), "AB_Mines_Scaffolding_Broken_Segment_A15", _folder)
if a: placed += 1
else: skipped += 1

# Construction: AB_Mines_Scaffolding_Broken_Segment_A2
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Scaffolding
#   Volume: EMorSimpleShape::Empty, BoxExtent: (100.0, 100.0, 100.0)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (1813.5535, 3810.2268, 807.594), (-11.249940016738806, 106.87465968961672, 6.083208886376871e-06), (2.0000, 2.0000, 2.0000), "AB_Mines_Scaffolding_Broken_Segment_A2", _folder)
if a: placed += 1
else: skipped += 1

# Construction: AB_Mines_Scaffolding_Broken_Segment_A3
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Scaffolding
#   Volume: EMorSimpleShape::Empty, BoxExtent: (100.0, 100.0, 100.0)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (1479.2162, 2751.844, 798.59406), (-11.249909604281282, -171.56217662124064, 3.167897038640777e-05), (2.0000, 2.0000, 2.0000), "AB_Mines_Scaffolding_Broken_Segment_A3", _folder)
if a: placed += 1
else: skipped += 1

# Construction: AB_Mines_Scaffolding_Broken_Segment_A4_7
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Scaffolding
#   Volume: EMorSimpleShape::Empty, BoxExtent: (100.0, 100.0, 100.0)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (1923.4196, 749.09607, 948.7487), (-4.483276569906288, 58.25604098499188, 1.1007472164501093), (2.0000, 2.0000, 2.0000), "AB_Mines_Scaffolding_Broken_Segment_A4_7", _folder)
if a: placed += 1
else: skipped += 1

# Construction: AB_Mines_Scaffolding_Broken_Segment_A5
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Scaffolding
#   Volume: EMorSimpleShape::Empty, BoxExtent: (100.0, 100.0, 100.0)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (1955.5872, 870.45026, 938.3338), (-3.133483898233049, -124.81144710939901, -9.973632636673996), (2.0000, 2.0000, 2.0000), "AB_Mines_Scaffolding_Broken_Segment_A5", _folder)
if a: placed += 1
else: skipped += 1

# Construction: AB_Mines_Scaffolding_Broken_Segment_A6
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Scaffolding
#   Volume: EMorSimpleShape::Empty, BoxExtent: (100.0, 100.0, 100.0)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (805.0, 1700.0, 1590.0), (0.0, 0.0, -0.0), (2.0000, 2.0000, 2.0000), "AB_Mines_Scaffolding_Broken_Segment_A6", _folder)
if a: placed += 1
else: skipped += 1

# Construction: AB_Mines_Scaffolding_Broken_Segment_A7
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Scaffolding
#   Volume: EMorSimpleShape::Empty, BoxExtent: (100.0, 100.0, 100.0)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (805.0, 1400.0, 1590.0), (0.0, 0.0, -0.0), (2.0000, 2.0000, 2.0000), "AB_Mines_Scaffolding_Broken_Segment_A7", _folder)
if a: placed += 1
else: skipped += 1

# Construction: AB_Mines_Scaffolding_Broken_Segment_A8
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Scaffolding
#   Volume: EMorSimpleShape::Empty, BoxExtent: (100.0, 100.0, 100.0)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (599.99976, 1904.9996, 1590.0), (0.0, 90.00007597449323, -0.0), (2.0000, 2.0000, 2.0000), "AB_Mines_Scaffolding_Broken_Segment_A8", _folder)
if a: placed += 1
else: skipped += 1

# Construction: AB_Mines_Scaffolding_Broken_Segment_A9
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Scaffolding
#   Volume: EMorSimpleShape::Empty, BoxExtent: (100.0, 100.0, 100.0)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (966.11053, 1787.8224, 969.19495), (30.70827746758489, -150.94160903134798, -24.476320698023283), (2.0000, 2.0000, 2.0000), "AB_Mines_Scaffolding_Broken_Segment_A9", _folder)
if a: placed += 1
else: skipped += 1

# Construction: AB_Mines_Scaffolding_Broken_Segment_B_2
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Scaffolding
#   Volume: EMorSimpleShape::Empty, BoxExtent: (100.0, 100.0, 100.0)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (1251.7819, 4602.162, 896.9813), (1.324125758699469e-05, 39.375524420590004, -47.811554245260275), (2.0000, 2.0000, 2.0000), "AB_Mines_Scaffolding_Broken_Segment_B_2", _folder)
if a: placed += 1
else: skipped += 1

# Construction: AB_Mines_Scaffolding_Broken_Segment_B2_2
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Scaffolding
#   Volume: EMorSimpleShape::Empty, BoxExtent: (100.0, 100.0, 100.0)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (3860.8704, 5409.1294, 878.046), (4.135383810130521e-05, 45.00001614744163, -39.999908396906925), (2.0000, 2.0000, 2.0000), "AB_Mines_Scaffolding_Broken_Segment_B2_2", _folder)
if a: placed += 1
else: skipped += 1

# Construction: AB_Mines_Scaffolding_Broken_Segment_C_2
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Scaffolding
#   Volume: EMorSimpleShape::Empty, BoxExtent: (100.0, 100.0, 100.0)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (2201.0896, 1212.9098, 823.10754), (-16.686890693843107, 50.251014174038616, 2.5485759727321766), (2.0000, 2.0000, 2.0000), "AB_Mines_Scaffolding_Broken_Segment_C_2", _folder)
if a: placed += 1
else: skipped += 1

# Construction: AB_Mines_Scaffolding_Broken_Segment_C2
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Scaffolding
#   Volume: EMorSimpleShape::Empty, BoxExtent: (100.0, 100.0, 100.0)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (3151.7664, 645.6252, 894.15106), (54.80792663906279, -143.48269046867125, -15.085536699931232), (2.0000, 2.0000, 2.0000), "AB_Mines_Scaffolding_Broken_Segment_C2", _folder)
if a: placed += 1
else: skipped += 1

# Construction: AB_Mines_Scaffolding_Foundation_3x3x1m_2
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Scaffolding
#   Volume: EMorSimpleShape::Empty, BoxExtent: (100.0, 100.0, 100.0)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (600.0, 1700.0, 1550.0), (0.0, 0.0, -0.0), (2.0000, 2.0000, 2.0000), "AB_Mines_Scaffolding_Foundation_3x3x1m_2", _folder)
if a: placed += 1
else: skipped += 1

# Construction: AB_Mines_Scaffolding_Foundation_3x3x1m2
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Scaffolding
#   Volume: EMorSimpleShape::Empty, BoxExtent: (100.0, 100.0, 100.0)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (599.9994, 1395.0, 1550.0), (0.0, 179.99988388675877, -0.0), (2.0000, 2.0000, 2.0000), "AB_Mines_Scaffolding_Foundation_3x3x1m2", _folder)
if a: placed += 1
else: skipped += 1

# Construction: BP_DM_Mines_Scaffolding_Platform_3X3M_A_2
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Stone
#   Volume: EMorSimpleShape::OrientedBox, BoxExtent: (186.4, 185.5, 13.6)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (3764.899, 416.24323, 1269.1195), (0.0, 0.0, -0.0), (3.7272, 3.7101, 0.2714), "BP_DM_Mines_Scaffolding_Platform_3X3M_A_2", _folder)
if a: placed += 1
else: skipped += 1

# ======================================================================
# PHASE 3: Breakables + DecoVolumes
# ======================================================================
unreal.log(f"[{BUBBLE_NAME}] Phase 3: Placing breakables and deco volumes...")

_folder = "Reconstruction/BD_BB_Chapter5_CavernShaft/Breakables"

# Breakable Batch 0: BP_DM_Workshop_Scatter_Sandbags_A_Breakable (2 instances)
#   BP Class: /Game/LevelDesign/Deco/Urban/Workshop/BP_DM_Workshop_Scatter_Sandbags_A_Breakable
_brk_mesh = "/Game/Art/Assets/Kits/Deco/Urban/Workshop/Scatter/Workshop_Scatter_Sandbags_A"
_brk_mats = ['/Game/Art/Assets/Kits/Deco/Urban/Workshop/Materials/Workshop_Scatter_Sandbags/MI_Workshop_Scatter_Sandbags']
a = spawn_static_mesh(_brk_mesh, _brk_mats, (4933.0, 5025.0, 811.0), (0.0, 0.0, -0.0), (1.0, 1.0, 1.0), "BP_DM_Workshop_Scatter_Sandbags_A_Breakable_2", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_brk_mesh, _brk_mats, (5242.836, 1022.2938, 824.9929), (-3.43502834743052, -69.65375779390979, 4.885649432870366e-07), (1.0, 1.0, 1.0), "BP_DM_Workshop_Scatter_Sandbags_A_Breakable2_5", _folder)
if a: placed += 1
else: skipped += 1

# Breakable Batch 1: BP_DM_Mines_Plank_3M_A (4 instances)
#   BP Class: /Game/LevelDesign/Deco_Architecture/Mines/BP_DM_Mines_Plank_3M_A
_brk_mesh = "/Game/Art/Assets/Kits/Deco_Architecture/Mines/Mines_Plank_3M_A"
_brk_mats = ['/Game/Art/Assets/Kits/Deco_Architecture/Mines/Materials/Mines_Scaffolding/MI_Mines_Scaffolding_E_Deco']
a = spawn_static_mesh(_brk_mesh, _brk_mats, (5604.342, 3285.3894, 813.85706), (2.7820252716653884, -59.47320483130646, -8.447571670016885), (1.0, 1.0, 1.0), "BP_DM_Mines_Plank_3M_A_2", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_brk_mesh, _brk_mats, (5550.9272, 4848.5576, 1046.1041), (-0.8370666265915145, 59.061640348386824, 1.3207322691978237e-05), (1.0, 1.0, 1.0), "BP_DM_Mines_Plank_3M_A2_5", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_brk_mesh, _brk_mats, (5689.297, 2441.5989, 842.85706), (-3.0620117234503454, 85.37740066322945, 1.945406730098649), (1.0, 1.0, 1.0), "BP_DM_Mines_Plank_3M_A3", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_brk_mesh, _brk_mats, (3772.4565, 1631.9875, 815.2536), (2.279843450659998, -0.1676025702923919, 2.0031018175485067), (1.0, 1.0, 1.0), "BP_DM_Mines_Plank_3M_A4", _folder)
if a: placed += 1
else: skipped += 1

# Breakable Batch 2: BP_DM_Mines_Plank_3M_B (8 instances)
#   BP Class: /Game/LevelDesign/Deco_Architecture/Mines/BP_DM_Mines_Plank_3M_B
_brk_mesh = "/Game/Art/Assets/Kits/Deco_Architecture/Mines/Mines_Plank_3M_B"
_brk_mats = ['/Game/Art/Assets/Kits/Deco_Architecture/Mines/Materials/Mines_Scaffolding/MI_Mines_Scaffolding_E_Deco']
a = spawn_static_mesh(_brk_mesh, _brk_mats, (5495.049, 3535.0, 804.0012), (2.8124942673185087, 0.0, -0.0), (1.0, 1.0, 1.0), "BP_DM_Mines_Plank_3M_B_2", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_brk_mesh, _brk_mats, (5535.6025, 3187.7402, 801.9877), (-1.3644713829746182, 58.974441610022346, 2.41279205160739), (1.0, 1.0, 1.0), "BP_DM_Mines_Plank_3M_B2", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_brk_mesh, _brk_mats, (5569.823, 5029.5195, 1035.1841), (5.992295181385597, -19.2975729085577, 2.387343692355694), (1.0, 1.0, 1.0), "BP_DM_Mines_Plank_3M_B3_6", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_brk_mesh, _brk_mats, (5290.4663, 4725.4336, 837.5742), (9.950594308311057, 12.454838998512189, 11.426233411592687), (1.0, 1.0, 1.0), "BP_DM_Mines_Plank_3M_B4", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_brk_mesh, _brk_mats, (5597.263, 2290.681, 833.0012), (0.04371719437564188, -54.18100064282629, -11.190553104128362), (1.0, 1.0, 1.0), "BP_DM_Mines_Plank_3M_B5", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_brk_mesh, _brk_mats, (5628.6025, 2560.7402, 825.9877), (2.438103405802558, 64.15329061004554, 9.08096581934205), (1.0, 1.0, 1.0), "BP_DM_Mines_Plank_3M_B6", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_brk_mesh, _brk_mats, (3824.2822, 1694.7211, 818.6007), (-4.796447193308638, 24.724554242104965, -7.606140978711635), (1.0, 1.0, 1.0), "BP_DM_Mines_Plank_3M_B7", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_brk_mesh, _brk_mats, (3775.1313, 1529.3457, 809.80316), (8.661452725413541, 146.71935789918183, -0.008942000558212848), (1.0, 1.0, 1.0), "BP_DM_Mines_Plank_3M_B8", _folder)
if a: placed += 1
else: skipped += 1

# Breakable Batch 3: BP_DM_Mines_Scaffolding_Beam_2M_B (3 instances)
#   BP Class: /Game/LevelDesign/Deco_Architecture/Mines/BP_DM_Mines_Scaffolding_Beam_2M_B
_brk_mesh = "/Game/Art/Assets/Kits/Deco_Architecture/Mines/Mines_Scaffolding_Beam_2M_C"
_brk_mats = ['/Game/Art/Assets/Kits/Deco_Architecture/Mines/Materials/Mines_Scaffolding/MI_Mines_Scaffolding_B_Deco']
a = spawn_static_mesh(_brk_mesh, _brk_mats, (1312.8495, 4960.355, 900.33057), (2.434052646175579e-06, -56.24963562759379, -77.95492636868634), (1.0, 1.0, 1.0), "BP_DM_Mines_Scaffolding_Beam_2M_B4_2", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_brk_mesh, _brk_mats, (2028.9224, 1097.6615, 873.3306), (1.20224370965009, -177.45679554272684, -103.24029528013844), (1.0, 1.0, 1.0), "BP_DM_Mines_Scaffolding_Beam_2M_B5", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_brk_mesh, _brk_mats, (800.7157, 2007.9424, 920.425), (0.54850511893117, 146.19643616211056, -92.00347541119478), (1.0, 1.0, 1.0), "BP_DM_Mines_Scaffolding_Beam_2M_B6", _folder)
if a: placed += 1
else: skipped += 1

# Breakable Batch 4: BP_DM_Mines_Scaffolding_Beam_3M_C (3 instances)
#   BP Class: /Game/LevelDesign/Deco_Architecture/Mines/BP_DM_Mines_Scaffolding_Beam_3M_C
_brk_mesh = "/Game/Art/Assets/Kits/Deco_Architecture/Mines/Mines_Scaffolding_Beam_3M_C"
_brk_mats = ['/Game/Art/Assets/Kits/Deco_Architecture/Mines/Materials/Mines_Scaffolding/MI_Mines_Scaffolding_B_Deco']
a = spawn_static_mesh(_brk_mesh, _brk_mats, (5607.0, 4585.125, 904.4086), (-14.495909328677959, -2.650451523610537, 13.48183662537678), (1.0, 1.0, 1.0), "BP_DM_Mines_Scaffolding_Beam_3M_C_2", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_brk_mesh, _brk_mats, (5607.0, 4542.125, 900.4086), (-24.11044330211334, -58.612641785154814, 3.5713272533015887), (1.0, 1.0, 1.0), "BP_DM_Mines_Scaffolding_Beam_3M_C2", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_brk_mesh, _brk_mats, (1530.7795, 4776.346, 789.6172), (44.293614416992824, -11.250276251235684, 4.086879661709592e-05), (1.0, 1.0, 1.0), "BP_DM_Mines_Scaffolding_Beam_3M_C7_6", _folder)
if a: placed += 1
else: skipped += 1

# Breakable Batch 5: BP_DM_Mines_Scaffolding_Platform_3X1M_A (1 instances)
#   BP Class: /Game/LevelDesign/Deco_Architecture/Mines/BP_DM_Mines_Scaffolding_Platform_3X1M_A
_brk_mesh = "/Game/Art/Assets/Kits/Deco_Architecture/Mines/Mines_Scaffolding_Platform_3X1M_A"
_brk_mats = ['/Game/Art/Assets/Kits/Deco_Architecture/Mines/Materials/Mines_Scaffolding/MI_Mines_Scaffolding_D_Deco', '/Game/Art/Assets/Kits/Deco_Architecture/Mines/Materials/Mines_Scaffolding/MI_Mines_Scaffolding_E_Deco']
a = spawn_static_mesh(_brk_mesh, _brk_mats, (791.4531, 4563.547, 861.14746), (-6.092345568704642, -114.108129420771, 5.999187066265087), (1.0, 1.0, 1.0), "BP_DM_Mines_Scaffolding_Platform_3X1M_A5_2", _folder)
if a: placed += 1
else: skipped += 1

# Breakable Batch 6: BP_DM_Mines_Scaffolding_Platform_3X3M_B (3 instances)
#   BP Class: /Game/LevelDesign/Deco_Architecture/Mines/BP_DM_Mines_Scaffolding_Platform_3X3M_B
_brk_mesh = "/Game/Art/Assets/Kits/Deco_Architecture/Mines/Mines_Scaffolding_Platform_3X3M_B"
_brk_mats = ['/Game/Art/Assets/Kits/Deco_Architecture/Mines/Materials/Mines_Scaffolding/MI_Mines_Scaffolding_D_Deco', '/Game/Art/Assets/Kits/Deco_Architecture/Mines/Materials/Mines_Scaffolding/MI_Mines_Scaffolding_E_Deco']
a = spawn_static_mesh(_brk_mesh, _brk_mats, (3461.9856, 277.4378, 1280.0), (0.0, 14.062317107648976, -0.0), (1.0, 1.0, 1.0), "BP_DM_Mines_Scaffolding_Platform_3X3M_B_2", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_brk_mesh, _brk_mats, (4119.1973, 411.13135, 1280.0), (0.0, 14.062317107648976, -0.0), (1.0, 1.0, 1.0), "BP_DM_Mines_Scaffolding_Platform_3X3M_B3", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_brk_mesh, _brk_mats, (3767.7195, 1874.0436, 865.00165), (0.10067686584492988, -170.72085108878272, 12.310016587685112), (1.0, 1.0, 1.0), "BP_DM_Mines_Scaffolding_Platform_3X3M_B4", _folder)
if a: placed += 1
else: skipped += 1

# Breakable Batch 7: BP_DM_Mines_Scaffolding_Post_2M_B (1 instances)
#   BP Class: /Game/LevelDesign/Deco_Architecture/Mines/BP_DM_Mines_Scaffolding_Post_2M_B
_brk_mesh = "/Game/Art/Assets/Kits/Deco_Architecture/Mines/Mines_Scaffolding_Post_2M_B"
_brk_mats = ['/Game/Art/Assets/Kits/Deco_Architecture/Mines/Materials/Mines_Scaffolding/MI_Mines_Scaffolding_C_Deco']
a = spawn_static_mesh(_brk_mesh, _brk_mats, (1476.9219, 4880.861, 826.65674), (74.58368056515188, -93.88669437025287, -93.45862544795733), (1.0, 1.0, 1.0), "BP_DM_Mines_Scaffolding_Post_2M_B_2", _folder)
if a: placed += 1
else: skipped += 1

# Breakable Batch 8: BP_DM_Mines_Scaffolding_Support_2M (6 instances)
#   BP Class: /Game/LevelDesign/Deco_Architecture/Mines/BP_DM_Mines_Scaffolding_Support_2M
_brk_mesh = "/Game/Art/Assets/Kits/Deco_Architecture/Mines/Mines_Scaffolding_Support_2M"
_brk_mats = ['/Game/Art/Assets/Kits/Deco_Architecture/Mines/Materials/Mines_Scaffolding/MI_Mines_Scaffolding_D_Deco']
a = spawn_static_mesh(_brk_mesh, _brk_mats, (1044.0692, 4711.19, 961.457), (85.55650278007946, -0.4588957753516068, 25.931998923764464), (1.0, 1.0, 1.0), "BP_DM_Mines_Scaffolding_Support_2M12", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_brk_mesh, _brk_mats, (1972.182, 1417.491, 790.8219), (2.087865492638678, 68.06778149802791, -177.1344835188832), (1.0, 1.0, 1.0), "BP_DM_Mines_Scaffolding_Support_2M13", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_brk_mesh, _brk_mats, (3259.5251, 912.63336, 814.97345), (11.30690628504132, -43.787591127743184, -174.682517142814), (1.0, 1.0, 1.0), "BP_DM_Mines_Scaffolding_Support_2M14", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_brk_mesh, _brk_mats, (3596.5251, 1852.6333, 863.97345), (-7.00265364996532, -39.33663319354301, 167.33251653403912), (1.0, 1.0, 1.0), "BP_DM_Mines_Scaffolding_Support_2M15", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_brk_mesh, _brk_mats, (1188.9248, 4397.3535, 813.8032), (70.23827492166053, -90.00009970037718, 8.459516297703873), (1.0, 1.0, 1.0), "BP_DM_Mines_Scaffolding_Support_2M7_2", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_brk_mesh, _brk_mats, (1617.27, 3696.8464, 811.7723), (70.59737203436134, -170.97455392428907, 0.1303415722331136), (1.0, 1.0, 1.0), "BP_DM_Mines_Scaffolding_Support_2M8", _folder)
if a: placed += 1
else: skipped += 1

# --- Extra DecoVolumes (not construction blocks) ---
_folder = "Reconstruction/BD_BB_Chapter5_CavernShaft/DecoVolumes"

# DecoVolume: BP_DM_Mine_tailings_Debris_1x1_A_2 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (3158.436, 5092.94, 811.1879), (0.0, 0.0, -0.0), (1.2259, 1.2259, 0.4337), "DV_BP_DM_Mine_tailings_Debris_1x1_A_2_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_DM_Mine_tailings_Debris_1x1_A2_5 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (1783.7327, 4800.165, 813.33685), (0.0, 0.0, -0.0), (1.1884, 1.1884, 0.4337), "DV_BP_DM_Mine_tailings_Debris_1x1_A2_5_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_DM_Mine_tailings_Debris_1x1_A3 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (2334.1968, 4040.7498, 820.1147), (0.0, 0.0, -0.0), (1.1301, 1.1191, 0.5289), "DV_BP_DM_Mine_tailings_Debris_1x1_A3_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_DM_Mine_tailings_Debris_1x1_A4 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (4149.4595, 3871.0767, 1434.2133), (0.0, 0.0, -0.0), (1.3543, 1.3639, 0.4828), "DV_BP_DM_Mine_tailings_Debris_1x1_A4_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_DM_Mine_tailings_Debris_1x1_A5 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (3963.4734, 3962.6555, 1452.2367), (0.0, 0.0, -0.0), (1.2972, 1.3117, 0.4879), "DV_BP_DM_Mine_tailings_Debris_1x1_A5_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_DM_Mine_tailings_Debris_2x2_B_2 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (3036.3796, 5196.9795, 838.8144), (0.0, 0.0, -0.0), (2.6067, 2.6103, 0.9793), "DV_BP_DM_Mine_tailings_Debris_2x2_B_2_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_DM_Mine_tailings_Debris_2x2_B2 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (4046.0564, 3870.643, 1477.8314), (0.0, 0.0, -0.0), (2.6044, 2.5430, 1.6109), "DV_BP_DM_Mine_tailings_Debris_2x2_B2_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_DM_Mines_Fence_A_5 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (5660.813, 4834.056, 1137.272), (0.0, 0.0, -0.0), (1.2708, 3.0954, 2.3298), "DV_BP_DM_Mines_Fence_A_5_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_DM_Mines_Fence_Brace_C_2 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (3741.134, 516.7397, 1067.8271), (0.0, 0.0, -0.0), (4.1969, 5.2249, 4.1621), "DV_BP_DM_Mines_Fence_Brace_C_2_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_DM_Mines_Fence_Brace_F_2 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (4081.3367, 523.63495, 1067.8271), (0.0, 0.0, -0.0), (3.9890, 3.7105, 4.1621), "DV_BP_DM_Mines_Fence_Brace_F_2_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_DM_Mines_Fence_Brace_F3 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (3431.417, 360.83777, 1067.8271), (0.0, 0.0, -0.0), (3.9890, 3.7105, 4.1621), "DV_BP_DM_Mines_Fence_Brace_F3_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_DM_Mines_Fence_Roof_2 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (5699.0234, 3290.4248, 1041.1562), (0.0, 0.0, -0.0), (2.8786, 6.6965, 4.9237), "DV_BP_DM_Mines_Fence_Roof_2_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_DM_Mines_Machine_Whim_Lift_C_Breakable_2 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (596.23737, 1807.7927, 1851.6327), (0.0, 0.0, -0.0), (3.0196, 5.7620, 5.0499), "DV_BP_DM_Mines_Machine_Whim_Lift_C_Breakable_2_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_DM_Mines_Plank_3M_A_2 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (5604.342, 3285.3894, 813.85706), (0.0, 0.0, -0.0), (1.7708, 2.7382, 0.2386), "DV_BP_DM_Mines_Plank_3M_A_2_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_DM_Mines_Plank_3M_A2_5 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (5550.9272, 4848.5576, 1046.1041), (0.0, 0.0, -0.0), (1.7860, 2.7304, 0.0968), "DV_BP_DM_Mines_Plank_3M_A2_5_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_DM_Mines_Plank_3M_A3 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (5689.297, 2441.5989, 842.85706), (0.0, 0.0, -0.0), (0.5156, 3.0300, 0.2231), "DV_BP_DM_Mines_Plank_3M_A3_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_DM_Mines_Plank_3M_A4 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (3772.4565, 1631.9875, 815.2536), (0.0, 0.0, -0.0), (3.0206, 0.2825, 0.1823), "DV_BP_DM_Mines_Plank_3M_A4_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_DM_Mines_Plank_3M_B_2 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (5494.445, 3535.5469, 803.88666), (0.0, 0.0, -0.0), (1.2101, 0.2713, 0.1337), "DV_BP_DM_Mines_Plank_3M_B_2_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_DM_Mines_Plank_3M_B2 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (5534.8223, 3187.4963, 801.8945), (0.0, 0.0, -0.0), (0.8566, 1.1775, 0.1146), "DV_BP_DM_Mines_Plank_3M_B2_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_DM_Mines_Plank_3M_B3_6 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (5569.442, 5030.228, 1035.0137), (0.0, 0.0, -0.0), (1.2308, 0.6580, 0.2114), "DV_BP_DM_Mines_Plank_3M_B3_6_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_DM_Mines_Plank_3M_B4 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (5289.8013, 4725.8184, 837.2805), (0.0, 0.0, -0.0), (1.2256, 0.5300, 0.3336), "DV_BP_DM_Mines_Plank_3M_B4_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_DM_Mines_Plank_3M_B5 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (5597.3555, 2291.498, 833.0237), (0.0, 0.0, -0.0), (0.9345, 1.1437, 0.1267), "DV_BP_DM_Mines_Plank_3M_B5_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_DM_Mines_Plank_3M_B6 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (5627.8667, 2560.429, 825.79193), (0.0, 0.0, -0.0), (0.7784, 1.2069, 0.1677), "DV_BP_DM_Mines_Plank_3M_B6_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_DM_Mines_Plank_3M_B7 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (3823.499, 1694.9695, 818.63995), (0.0, 0.0, -0.0), (1.2129, 0.7554, 0.2104), "DV_BP_DM_Mines_Plank_3M_B7_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_DM_Mines_Plank_3M_B8 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (3775.3237, 1528.5654, 809.62775), (0.0, 0.0, -0.0), (1.1566, 0.8883, 0.2556), "DV_BP_DM_Mines_Plank_3M_B8_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_DM_Mines_Scaffolding_Beam_2M_B4_2 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (1243.4127, 4913.9385, 928.0928), (0.0, 0.0, -0.0), (1.6093, 1.1916, 0.6130), "DV_BP_DM_Mines_Scaffolding_Beam_2M_B4_2_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_DM_Mines_Scaffolding_Beam_2M_B5 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (2024.8073, 1184.9429, 862.76105), (0.0, 0.0, -0.0), (0.3389, 1.7733, 0.6526), "DV_BP_DM_Mines_Scaffolding_Beam_2M_B5_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_DM_Mines_Scaffolding_Beam_2M_B6 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (849.58185, 2080.8428, 927.08215), (0.0, 0.0, -0.0), (1.1907, 1.6023, 0.3163), "DV_BP_DM_Mines_Scaffolding_Beam_2M_B6_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_DM_Mines_Scaffolding_Beam_3M_C_2 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (5641.9062, 4625.1597, 1031.9474), (0.0, 0.0, -0.0), (0.9491, 0.8698, 2.7184), "DV_BP_DM_Mines_Scaffolding_Beam_3M_C_2_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_DM_Mines_Scaffolding_Beam_3M_C2 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (5651.785, 4503.8755, 1025.383), (0.0, 0.0, -0.0), (1.0657, 1.2055, 2.6315), "DV_BP_DM_Mines_Scaffolding_Beam_3M_C2_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_DM_Mines_Scaffolding_Beam_3M_C7_6 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (1438.3202, 4804.674, 888.28906), (0.0, 0.0, -0.0), (2.1172, 0.6599, 2.1519), "DV_BP_DM_Mines_Scaffolding_Beam_3M_C7_6_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_DM_Mines_Scaffolding_Platform_3X1M_A5_2 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (928.4043, 4506.398, 834.4011), (0.0, 0.0, -0.0), (3.2325, 2.2104, 0.7136), "DV_BP_DM_Mines_Scaffolding_Platform_3X1M_A5_2_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_DM_Mines_Scaffolding_Platform_3X3M_B_2 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (3435.0242, 385.7834, 1270.2897), (0.0, 0.0, -0.0), (3.5004, 2.9287, 0.2631), "DV_BP_DM_Mines_Scaffolding_Platform_3X3M_B_2_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_DM_Mines_Scaffolding_Platform_3X3M_B3 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (4092.2358, 519.4769, 1270.2897), (0.0, 0.0, -0.0), (3.5004, 2.9287, 0.2631), "DV_BP_DM_Mines_Scaffolding_Platform_3X3M_B3_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_DM_Mines_Scaffolding_Platform_3X3M_B4 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (3784.7473, 1768.3943, 831.7111), (0.0, 0.0, -0.0), (3.3676, 2.7223, 0.7436), "DV_BP_DM_Mines_Scaffolding_Platform_3X3M_B4_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_DM_Mines_Scaffolding_Post_2M_B_2 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (1477.3606, 4876.1113, 829.37427), (0.0, 0.0, -0.0), (0.2125, 2.0613, 0.6390), "DV_BP_DM_Mines_Scaffolding_Post_2M_B_2_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_DM_Mines_Scaffolding_Support_2M12 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (1097.9617, 4796.0205, 958.30804), (0.0, 0.0, -0.0), (1.1000, 1.8925, 0.3465), "DV_BP_DM_Mines_Scaffolding_Support_2M12_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_DM_Mines_Scaffolding_Support_2M13 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (2064.4717, 1380.7758, 806.47723), (0.0, 0.0, -0.0), (1.9694, 1.0004, 0.3224), "DV_BP_DM_Mines_Scaffolding_Support_2M13_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_DM_Mines_Scaffolding_Support_2M14 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (3189.2043, 843.50684, 834.64545), (0.0, 0.0, -0.0), (1.6126, 1.6398, 0.4421), "DV_BP_DM_Mines_Scaffolding_Support_2M14_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_DM_Mines_Scaffolding_Support_2M15 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (3532.8792, 1775.6544, 852.4004), (0.0, 0.0, -0.0), (1.4957, 1.6989, 0.6752), "DV_BP_DM_Mines_Scaffolding_Support_2M15_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_DM_Mines_Scaffolding_Support_2M7_2 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (1286.2521, 4373.27, 806.19543), (0.0, 0.0, -0.0), (2.0163, 0.5654, 0.4199), "DV_BP_DM_Mines_Scaffolding_Support_2M7_2_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_DM_Mines_Scaffolding_Support_2M8 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (1622.5, 3596.4675, 809.0877), (0.0, 0.0, -0.0), (0.5957, 2.0274, 0.3217), "DV_BP_DM_Mines_Scaffolding_Support_2M8_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_DM_Mines_Wagon_B_Breakable_2 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (1901.5349, 5074.7275, 867.7478), (0.0, 0.0, -0.0), (5.7342, 5.6450, 1.4542), "DV_BP_DM_Mines_Wagon_B_Breakable_2_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_DM_Sluice_Angled_B_Breakable_2 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (3087.538, 5271.926, 877.3058), (0.0, 0.0, -0.0), (3.8600, 3.4812, 1.7609), "DV_BP_DM_Sluice_Angled_B_Breakable_2_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_DM_Warehouse_Crate_A_Broken_Breakable_2 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (2197.0312, 5192.259, 826.2152), (0.0, 0.0, -0.0), (1.0603, 1.0603, 0.5570), "DV_BP_DM_Warehouse_Crate_A_Broken_Breakable_2_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_DM_Warehouse_Crate_A_Broken_Breakable2 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (707.03125, 1372.2588, 1626.2152), (0.0, 0.0, -0.0), (0.9708, 0.9708, 0.5570), "DV_BP_DM_Warehouse_Crate_A_Broken_Breakable2_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_DM_Warehouse_Crate_A_Broken_Breakable3 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (5468.3804, 1295.5062, 887.16565), (0.0, 0.0, -0.0), (0.9621, 0.9362, 0.6150), "DV_BP_DM_Warehouse_Crate_A_Broken_Breakable3_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_DM_Warehouse_Crate_B_Broken_Breakable_2 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (5431.7046, 1375.0, 884.6581), (0.0, 0.0, -0.0), (1.4245, 1.2410, 0.6616), "DV_BP_DM_Warehouse_Crate_B_Broken_Breakable_2_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_DM_Warren_Lighting_Torch_Breakable_2 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (585.65497, 4300.4185, 859.82385), (0.0, 0.0, -0.0), (1.0112, 1.0765, 1.9128), "DV_BP_DM_Warren_Lighting_Torch_Breakable_2_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_DM_Warren_Lighting_Torch_Breakable10 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (3479.4265, 1625.2316, 873.545), (0.0, 0.0, -0.0), (1.0112, 1.0765, 1.9128), "DV_BP_DM_Warren_Lighting_Torch_Breakable10_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_DM_Warren_Lighting_Torch_Breakable2_5 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (576.5827, 2345.3271, 878.1064), (0.0, 0.0, -0.0), (1.0112, 1.0765, 1.9128), "DV_BP_DM_Warren_Lighting_Torch_Breakable2_5_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_DM_Warren_Lighting_Torch_Breakable3_8 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (5035.9604, 1328.5409, 878.48126), (0.0, 0.0, -0.0), (1.0112, 1.0765, 1.9128), "DV_BP_DM_Warren_Lighting_Torch_Breakable3_8_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_DM_Warren_Lighting_Torch_Breakable4_11 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (5141.9653, 4741.0967, 863.7301), (0.0, 0.0, -0.0), (1.0112, 1.0765, 1.9128), "DV_BP_DM_Warren_Lighting_Torch_Breakable4_11_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_DM_Warren_Lighting_Torch_Breakable6_17 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (5121.852, 3254.8853, 862.6312), (0.0, 0.0, -0.0), (1.0112, 1.0765, 1.9128), "DV_BP_DM_Warren_Lighting_Torch_Breakable6_17_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_DM_Warren_Lighting_Torch_Breakable7 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (4668.0137, 4522.3315, 870.7501), (0.0, 0.0, -0.0), (1.3912, 1.3575, 1.9128), "DV_BP_DM_Warren_Lighting_Torch_Breakable7_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_DM_Warren_Lighting_Torch_Breakable8 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (2111.0264, 3956.453, 859.82336), (0.0, 0.0, -0.0), (1.0112, 1.0765, 1.9128), "DV_BP_DM_Warren_Lighting_Torch_Breakable8_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_DM_Warren_Lighting_Torch_Breakable9 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (2385.0376, 5212.1816, 867.24225), (0.0, 0.0, -0.0), (1.0112, 1.0765, 1.9128), "DV_BP_DM_Warren_Lighting_Torch_Breakable9_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_DM_Workshop_Barrel_Breakable_2 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (1632.9929, 4802.408, 813.19586), (0.0, 0.0, -0.0), (1.1605, 1.1763, 0.8610), "DV_BP_DM_Workshop_Barrel_Breakable_2_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_DM_Workshop_Barrel_Breakable2_5 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (1531.1511, 4776.312, 839.6437), (0.0, 0.0, -0.0), (0.9280, 0.8750, 0.8538), "DV_BP_DM_Workshop_Barrel_Breakable2_5_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_DM_Workshop_Barrel_Breakable3 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (542.9929, 1362.4082, 1618.1958), (0.0, 0.0, -0.0), (1.1605, 1.1763, 0.8610), "DV_BP_DM_Workshop_Barrel_Breakable3_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_DM_Workshop_Barrel_Breakable4 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (456.15115, 1336.312, 1639.6437), (0.0, 0.0, -0.0), (0.9280, 0.8750, 0.8538), "DV_BP_DM_Workshop_Barrel_Breakable4_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_DM_Workshop_Barrel_Breakable5 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (4068.8635, 738.5743, 872.66003), (0.0, 0.0, -0.0), (1.2964, 1.1788, 1.0070), "DV_BP_DM_Workshop_Barrel_Breakable5_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_DM_Workshop_Barrel_Breakable6 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (3391.9707, 542.44946, 932.65717), (0.0, 0.0, -0.0), (1.0756, 0.9952, 1.1177), "DV_BP_DM_Workshop_Barrel_Breakable6_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_DM_Workshop_Barrel_Breakable7_4 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (5442.434, 1143.0718, 879.31964), (0.0, 0.0, -0.0), (1.1609, 1.2120, 1.0711), "DV_BP_DM_Workshop_Barrel_Breakable7_4_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_DM_Workshop_Barrel_Broken_Breakable_2 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (3185.0, 5150.4517, 842.65753), (0.0, 0.0, -0.0), (0.8004, 0.7330, 0.8528), "DV_BP_DM_Workshop_Barrel_Broken_Breakable_2_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_DM_Workshop_Barrel_Broken_Breakable2_2 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (2300.2322, 3921.3872, 863.65753), (0.0, 0.0, -0.0), (1.0633, 1.0402, 0.8528), "DV_BP_DM_Workshop_Barrel_Broken_Breakable2_2_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_DM_Workshop_Barrel_Broken_Breakable3_3 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (5376.0, 1107.4515, 894.65753), (0.0, 0.0, -0.0), (0.8004, 0.7330, 0.8528), "DV_BP_DM_Workshop_Barrel_Broken_Breakable3_3_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_DM_Workshop_Barrel_Broken_Breakable4 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (3693.794, 5310.8374, 855.65753), (0.0, 0.0, -0.0), (1.0499, 1.0217, 0.8528), "DV_BP_DM_Workshop_Barrel_Broken_Breakable4_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_DM_Workshop_Barrel_Broken_Breakable5 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (4567.614, 5145.1016, 860.65753), (0.0, 0.0, -0.0), (0.8265, 0.7615, 0.8528), "DV_BP_DM_Workshop_Barrel_Broken_Breakable5_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_DM_Workshop_Barrel_Broken_Breakable6 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (3975.3887, 4027.2146, 1485.2908), (0.0, 0.0, -0.0), (1.0752, 1.1039, 0.9945), "DV_BP_DM_Workshop_Barrel_Broken_Breakable6_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_DM_Workshop_Scatter_Bucket_Wood_Breakable_2 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (2323.0168, 3991.49, 830.0185), (0.0, 0.0, -0.0), (0.7438, 0.4497, 0.7318), "DV_BP_DM_Workshop_Scatter_Bucket_Wood_Breakable_2_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_DM_Workshop_Scatter_Sandbags_A_Breakable_2 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (4932.195, 5021.854, 821.335), (0.0, 0.0, -0.0), (0.5348, 0.8178, 0.2107), "DV_BP_DM_Workshop_Scatter_Sandbags_A_Breakable_2_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_DM_Workshop_Scatter_Sandbags_A_Breakable2_5 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (5239.822, 1021.37274, 835.3576), (0.0, 0.0, -0.0), (0.9568, 0.7967, 0.2424), "DV_BP_DM_Workshop_Scatter_Sandbags_A_Breakable2_5_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_DM_Workshop_Scatter_Sandbags_B_Breakable_2 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (3604.1177, 5308.1587, 840.2028), (0.0, 0.0, -0.0), (1.1895, 1.1336, 0.4049), "DV_BP_DM_Workshop_Scatter_Sandbags_B_Breakable_2_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_DM_Workshop_Scatter_Sandbags_B_Breakable2_2 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (2210.8386, 3904.6694, 832.1336), (0.0, 0.0, -0.0), (1.1899, 1.1440, 0.4468), "DV_BP_DM_Workshop_Scatter_Sandbags_B_Breakable2_2_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_DM_Workshop_Scatter_Sandbags_B_Breakable3 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (4649.497, 5117.112, 836.2028), (0.0, 0.0, -0.0), (1.1580, 1.2107, 0.4049), "DV_BP_DM_Workshop_Scatter_Sandbags_B_Breakable3_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_DM_Workshop_Scatter_Sandbags_B_Breakable4 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (5406.878, 4726.4478, 863.0582), (0.0, 0.0, -0.0), (1.2433, 1.3126, 0.5457), "DV_BP_DM_Workshop_Scatter_Sandbags_B_Breakable4_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_DM_Workshop_Scatter_Sandbags_B_Breakable5_4 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (5318.003, 1048.6659, 862.2831), (0.0, 0.0, -0.0), (1.3899, 1.3895, 0.5526), "DV_BP_DM_Workshop_Scatter_Sandbags_B_Breakable5_4_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_DM_Workshop_Scatter_Sandbags_C_Breakable_2 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (5156.8354, 4926.113, 845.33875), (0.0, 0.0, -0.0), (0.6238, 0.7947, 0.8879), "DV_BP_DM_Workshop_Scatter_Sandbags_C_Breakable_2_BRK", _folder)
if a: placed += 1
else: skipped += 1

# ======================================================================
# SUMMARY
# ======================================================================
unreal.log(f"[{BUBBLE_NAME}] Reconstruction complete: {placed} placed, {skipped} skipped, {errors} errors")
