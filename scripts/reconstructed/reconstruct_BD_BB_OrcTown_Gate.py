"""Auto-generated level reconstruction script.
Bubble: BD_BB_OrcTown_Gate
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

BUBBLE_NAME = "BD_BB_OrcTown_Gate"
placed = 0
skipped = 0
errors = 0

# ======================================================================
# PHASE 1: InstancedMeshCatalog  (static mesh placement)
# ======================================================================
unreal.log(f"[{BUBBLE_NAME}] Phase 1: Placing static meshes...")

# Batch 0: StaticMesh'Cube' (5 instances)
_mesh_path = "/Engine/BasicShapes/Cube"
_materials = ['/Game/Art/Assets/Kits/Architecture/Suburbs/Destructable/Materials/MI_Suburbs_Wall_Non_Dest']
_folder = "Reconstruction/BD_BB_OrcTown_Gate/Meshes"
a = spawn_static_mesh(_mesh_path, _materials, (5000.0, 400.0, 850.0), (0.0, 0.0, -0.0), (11.0, 1.0, 3.0), "Cube_2", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4000.0, 1250.0, 1046.6298), (0.0, 0.0, -0.0), (6.0, 4.0, 1.0), "Cube2_5", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4600.0, 1250.0, 1046.6298), (0.0, 0.0, -0.0), (6.0, 4.0, 1.0), "Cube3_108", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4000.0, 1650.0, 1046.6298), (0.0, 0.0, -0.0), (6.0, 4.0, 1.0), "Cube4", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4600.0, 1650.0, 1046.6298), (0.0, 0.0, -0.0), (6.0, 4.0, 1.0), "Cube5", _folder)
if a: placed += 1
else: skipped += 1

# Batch 1: StaticMesh'City_Floor_3x3m_Detail_A' (2 instances)
_mesh_path = "/Game/Art/Assets/Kits/Architecture/City/City_Floor_3x3m_Detail_A"
_materials = ['/Game/Environments/ProcTexturing/GuideMeshFloor/M_GuideMeshFloor_CityFloor_Darker']
_folder = "Reconstruction/BD_BB_OrcTown_Gate/Meshes"
a = spawn_static_mesh(_mesh_path, _materials, (3220.0, 3025.0, 1195.0), (0.0, 0.0, -0.0), (1.0, 1.0, 1.0), "City_Floor_3x3m_Detail_A2_42", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3330.0, 2945.0, 1190.0), (0.0, -100.00008183358206, 0.0), (1.0, 1.0, 1.0), "City_Floor_3x3m_Detail_A3_48", _folder)
if a: placed += 1
else: skipped += 1

# Batch 2: StaticMesh'City_Floor_3x3m_Detail_B' (5 instances)
_mesh_path = "/Game/Art/Assets/Kits/Architecture/City/City_Floor_3x3m_Detail_B"
_materials = ['/Game/Environments/ProcTexturing/GuideMeshFloor/M_GuideMeshFloor_CityFloor_Darker']
_folder = "Reconstruction/BD_BB_OrcTown_Gate/Meshes"
a = spawn_static_mesh(_mesh_path, _materials, (3335.0, 3930.0, 1200.0), (0.0, 0.0, -0.0), (1.0, 1.0, 1.0), "City_Floor_3x3m_Detail_B_30", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3005.0, 3645.0, 1196.3713), (0.0, 0.0, -0.0), (1.0, 1.0, 1.0), "City_Floor_3x3m_Detail_B2_36", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3220.0, 2885.0, 1200.0), (0.0, 0.0, -0.0), (1.0, 1.0, 1.0), "City_Floor_3x3m_Detail_B3_39", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3385.0, 3100.0, 1200.0), (0.0, 0.0, -0.0), (1.0, 1.0, 1.0), "City_Floor_3x3m_Detail_B4_45", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3220.0, 3009.9714, 1192.2681), (0.0, 0.0, -0.0), (1.0, 1.0, 1.0), "City_Floor_3x3m_Detail_B5", _folder)
if a: placed += 1
else: skipped += 1

# Batch 3: StaticMesh'City_Trim_A_0_5m' (47 instances)
_mesh_path = "/Game/Art/Assets/Kits/Architecture/City/City_Trim_A_0_5m"
_materials = ['/Game/Art/Assets/Kits/Architecture/Suburbs/Materials/Suburbs_Trim_B/MI_Suburbs_Trim_B_Dest']
_folder = "Reconstruction/BD_BB_OrcTown_Gate/Meshes"
a = spawn_static_mesh(_mesh_path, _materials, (3835.6355, 2586.9841, 2892.5488), (9.562264440610835e-05, 0.00013318867461626206, 2.048984278315888e-05), (0.74999976, 0.74999976, 0.46875057), "BP_Trim_B_0-5m_Breakable_1", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3835.6292, 4226.9844, 2892.5488), (9.562264440610835e-05, 0.00013318867461626206, 2.048984278315888e-05), (0.74999976, 0.74999976, 0.46875057), "BP_Trim_B_0-5m_Breakable_2", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2606.8435, 331.751, 2892.5383), (-3.0517578031716448e-05, -179.99963116980015, 0.0004371324365920463), (0.74999976, 0.74999976, 0.46875057), "BP_Trim_B_0-5m_Breakable_3", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3835.636, 1776.9819, 2892.5493), (9.562264440610835e-05, 0.00013318867461626206, 2.048984278315888e-05), (0.74999976, 0.74999976, 0.46875057), "BP_Trim_B_0-5m_Breakable_4", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2569.308, 4179.3477, 2892.549), (2.7320755585614844e-05, 0.0004883582975894641, -0.00042724608892752327), (0.74999976, 0.74999976, 0.46874934), "BP_Trim_B_0-5m_Breakable_19", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3873.135, 3629.394, 2892.5488), (-9.155273396700406e-05, -179.9995970188423, -3.0517578197921365e-05), (0.74999976, 0.74999976, 0.46874934), "BP_Trim_B_0-5m_Breakable_40", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2606.81, 3581.7546, 2892.5513), (-3.0517578031716448e-05, -179.99963116980015, 0.0004371324365920463), (0.74999976, 0.74999976, 0.46875057), "BP_Trim_B_0-5m_Breakable_54", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2569.308, 3369.3477, 2892.549), (2.7320755585871193e-05, 0.0004883583663443994, -0.00042724608892750695), (0.74999976, 0.74999976, 0.46874934), "BP_Trim_B_0-5m_Breakable_56", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2606.813, 2771.7512, 2892.546), (-3.0517578031716448e-05, -179.99963116980015, 0.0004371324365920463), (0.74999976, 0.74999976, 0.46875057), "BP_Trim_B_0-5m_Breakable_59", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2569.3167, 1729.3441, 2892.539), (2.7320755585871193e-05, 0.0004883583663443994, -0.00042724608892750695), (0.74999976, 0.74999976, 0.46874934), "BP_Trim_B_0-5m_Breakable_61", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3873.1316, 2809.3882, 2892.5488), (-9.155273396700406e-05, -179.9995970188423, -3.0517578197921365e-05), (0.74999976, 0.74999976, 0.46874934), "BP_Trim_B_0-5m_Breakable_64", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3835.6292, 3406.9841, 2892.5488), (9.562264440610835e-05, 0.00013318867461626206, 2.048984278315888e-05), (0.74999976, 0.74999976, 0.46875057), "BP_Trim_B_0-5m_Breakable_67", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3873.1443, 1179.3882, 2892.5493), (-9.155273396700406e-05, -179.9995970188423, -3.0517578197921365e-05), (0.74999976, 0.74999976, 0.46874934), "BP_Trim_B_0-5m_Breakable_69", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2569.3103, 2549.3477, 2892.547), (2.7320755585614844e-05, 0.0004883582975894641, -0.00042724608892752327), (0.74999976, 0.74999976, 0.46874934), "BP_Trim_B_0-5m_Breakable_72", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2606.8308, 1951.7511, 2892.544), (-3.0517578031716448e-05, -179.99963116980015, 0.0004371324365920463), (0.74999976, 0.74999976, 0.46875057), "BP_Trim_B_0-5m_Breakable_75", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2569.3293, 909.3441, 2892.5334), (2.7320755585614844e-05, 0.0004883582975894641, -0.00042724608892752327), (0.74999976, 0.74999976, 0.46874934), "BP_Trim_B_0-5m_Breakable_77", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2606.8435, 1131.7511, 2892.5383), (-3.0517578031716448e-05, -179.99963116980015, 0.0004371324365920463), (0.74999976, 0.74999976, 0.46875057), "BP_Trim_B_0-5m_Breakable_80", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3835.6438, 956.98206, 2892.5496), (9.562264440610835e-05, 0.00013318867461626206, 2.048984278315888e-05), (0.74999976, 0.74999976, 0.46875057), "BP_Trim_B_0-5m_Breakable_82", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3873.152, 359.38818, 2892.5496), (-9.155273396700406e-05, -179.9995970188423, -3.0517578197921365e-05), (0.74999976, 0.74999976, 0.46874934), "BP_Trim_B_0-5m_Breakable_84", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2340.559, 4085.5999, 2662.8608), (2.7320755585614844e-05, 0.0004883582975894641, -0.00042724608892752327), (0.74999976, 0.74999976, 0.46874934), "BP_Trim_B_0-5m_Breakable2_20", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4101.885, 3723.143, 2662.8618), (-9.155273396700406e-05, -179.9995970188423, -3.0517578197921365e-05), (0.74999976, 0.74999976, 0.46874934), "BP_Trim_B_0-5m_Breakable2_41", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2340.559, 3275.5999, 2662.8608), (2.7320755585871193e-05, 0.0004883583663443994, -0.00042724608892750695), (0.74999976, 0.74999976, 0.46874934), "BP_Trim_B_0-5m_Breakable2_57", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2340.5676, 1635.5963, 2662.8508), (2.7320755585871193e-05, 0.0004883583663443994, -0.00042724608892750695), (0.74999976, 0.74999976, 0.46874934), "BP_Trim_B_0-5m_Breakable2_62", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4101.881, 2903.1372, 2662.8618), (-9.155273396700406e-05, -179.9995970188423, -3.0517578197921365e-05), (0.74999976, 0.74999976, 0.46874934), "BP_Trim_B_0-5m_Breakable2_65", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4101.8936, 1273.1372, 2662.8623), (-9.155273396700406e-05, -179.9995970188423, -3.0517578197921365e-05), (0.74999976, 0.74999976, 0.46874934), "BP_Trim_B_0-5m_Breakable2_70", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2340.5613, 2455.5999, 2662.859), (2.7320755585614844e-05, 0.0004883582975894641, -0.00042724608892752327), (0.74999976, 0.74999976, 0.46874934), "BP_Trim_B_0-5m_Breakable2_73", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2340.5803, 815.5963, 2662.8452), (2.7320755585614844e-05, 0.0004883582975894641, -0.00042724608892752327), (0.74999976, 0.74999976, 0.46874934), "BP_Trim_B_0-5m_Breakable2_78", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4101.9014, 453.13724, 2662.8625), (-9.155273396700406e-05, -179.9995970188423, -3.0517578197921365e-05), (0.74999976, 0.74999976, 0.46874934), "BP_Trim_B_0-5m_Breakable2_85", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4026.8884, 2418.236, 2662.862), (-3.0517570245353094e-05, 90.00046167098196, 9.155275667309818e-05), (0.74999976, 0.74999976, 0.46875057), "BP_Trim_B_0-5m_Breakable3_3", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4026.882, 4058.236, 2662.862), (-3.0517570245353094e-05, 90.00046167098196, 9.155275667309818e-05), (0.74999976, 0.74999976, 0.46875057), "BP_Trim_B_0-5m_Breakable3_4", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2415.5903, 500.50012, 2662.852), (-0.00042724612344131137, -89.99926407230726, -3.051757488797057e-05), (0.74999976, 0.74999976, 0.46875057), "BP_Trim_B_0-5m_Breakable3_5", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4026.889, 1608.2338, 2662.8625), (-3.0517570245353094e-05, 90.00046167098196, 9.155275667309818e-05), (0.74999976, 0.74999976, 0.46875057), "BP_Trim_B_0-5m_Breakable3_6", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2415.5593, 4048.103, 2662.8606), (-0.0004272461097297585, -89.99951687977065, -3.051758844424183e-05), (0.74999976, 0.74999976, 0.46874934), "BP_Trim_B_0-5m_Breakable3_21", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4026.8843, 3760.64, 2662.8616), (-3.051757831708132e-05, 90.00034336893043, 9.155276693488434e-05), (0.74999976, 0.74999976, 0.46874934), "BP_Trim_B_0-5m_Breakable3_42", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2415.557, 3750.5034, 2662.8647), (-0.00042724612344131137, -89.99926407230726, -3.051757488797057e-05), (0.74999976, 0.74999976, 0.46875057), "BP_Trim_B_0-5m_Breakable3_55", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2415.5593, 3238.103, 2662.8606), (-0.0004272461097297585, -89.99951687977065, -3.051758844424183e-05), (0.74999976, 0.74999976, 0.46874934), "BP_Trim_B_0-5m_Breakable3_58", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2415.5598, 2940.5, 2662.8594), (-0.00042724612344131137, -89.99926407230726, -3.051757488797057e-05), (0.74999976, 0.74999976, 0.46875057), "BP_Trim_B_0-5m_Breakable3_60", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2415.5679, 1598.0996, 2662.8506), (-0.0004272461097297585, -89.99951687977065, -3.051758844424183e-05), (0.74999976, 0.74999976, 0.46874934), "BP_Trim_B_0-5m_Breakable3_63", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4026.8809, 2940.634, 2662.8616), (-3.051757831708132e-05, 90.00034336893043, 9.155276693488434e-05), (0.74999976, 0.74999976, 0.46874934), "BP_Trim_B_0-5m_Breakable3_66", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4026.882, 3238.236, 2662.862), (-3.0517570245353094e-05, 90.00046167098196, 9.155275667309818e-05), (0.74999976, 0.74999976, 0.46875057), "BP_Trim_B_0-5m_Breakable3_68", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4026.8936, 1310.634, 2662.862), (-3.051757831708132e-05, 90.00034336893043, 9.155276693488434e-05), (0.74999976, 0.74999976, 0.46874934), "BP_Trim_B_0-5m_Breakable3_71", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2415.5615, 2418.103, 2662.8586), (-0.0004272461097297585, -89.99951687977065, -3.051758844424183e-05), (0.74999976, 0.74999976, 0.46874934), "BP_Trim_B_0-5m_Breakable3_74", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2415.5776, 2120.5, 2662.8574), (-0.00042724612344131137, -89.99926407230726, -3.051757488797057e-05), (0.74999976, 0.74999976, 0.46875057), "BP_Trim_B_0-5m_Breakable3_76", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2415.5806, 778.0996, 2662.845), (-0.0004272461097297585, -89.99951687977065, -3.051758844424183e-05), (0.74999976, 0.74999976, 0.46874934), "BP_Trim_B_0-5m_Breakable3_79", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2415.5903, 1300.5001, 2662.852), (-0.00042724612344131137, -89.99926407230726, -3.051757488797057e-05), (0.74999976, 0.74999976, 0.46875057), "BP_Trim_B_0-5m_Breakable3_81", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4026.8967, 788.23376, 2662.8628), (-3.0517570245353094e-05, 90.00046167098196, 9.155275667309818e-05), (0.74999976, 0.74999976, 0.46875057), "BP_Trim_B_0-5m_Breakable3_83", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4026.9014, 490.63416, 2662.8623), (-3.051757831708132e-05, 90.00034336893043, 9.155276693488434e-05), (0.74999976, 0.74999976, 0.46874934), "BP_Trim_B_0-5m_Breakable3_86", _folder)
if a: placed += 1
else: skipped += 1

# Batch 4: StaticMesh'City_Trim_A_1m' (19 instances)
_mesh_path = "/Game/Art/Assets/Kits/Architecture/City/City_Trim_A_1m"
_materials = ['/Game/Art/Assets/Kits/Architecture/Suburbs/Materials/Suburbs_Trim_B/MI_Suburbs_Trim_B_Dest']
_folder = "Reconstruction/BD_BB_OrcTown_Gate/Meshes"
a = spawn_static_mesh(_mesh_path, _materials, (3498.1382, 1653.2285, 2892.5488), (-3.0517570245353094e-05, 90.00046167098196, 9.155275667309818e-05), (0.8671872, 0.74999976, 0.46875057), "BP_Trim_B_1m_Breakable_0", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3498.1313, 4103.2305, 2892.5483), (-3.0517570245353094e-05, 90.00046167098196, 9.155275667309818e-05), (0.8671872, 0.74999976, 0.46875057), "BP_Trim_B_1m_Breakable_2", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3498.1377, 2463.2307, 2892.5483), (-3.0517570245353094e-05, 90.00046167098196, 9.155275667309818e-05), (0.8671872, 0.74999976, 0.46875057), "BP_Trim_B_1m_Breakable_3", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2944.3408, 455.5061, 2892.5393), (-0.00042724612344131137, -89.99926407230726, -3.051757488797057e-05), (0.8671872, 0.74999976, 0.46875057), "BP_Trim_B_1m_Breakable_4", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2944.3083, 4141.851, 2892.549), (-0.0004272461097297585, -89.99951687977065, -3.051758844424183e-05), (0.74999976, 0.74999976, 0.46874934), "BP_Trim_B_1m_Breakable_7", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3498.1348, 3666.891, 2892.5483), (-3.051757831708132e-05, 90.00034336893043, 9.155276693488434e-05), (0.74999976, 0.74999976, 0.46874934), "BP_Trim_B_1m_Breakable_19", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2944.3074, 3705.5095, 2892.5522), (-0.00042724612344131137, -89.99926407230726, -3.051757488797057e-05), (0.8671872, 0.74999976, 0.46875057), "BP_Trim_B_1m_Breakable_31", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2944.3083, 3331.8513, 2892.549), (-0.0004272461097297585, -89.99951687977065, -3.051758844424183e-05), (0.74999976, 0.74999976, 0.46874934), "BP_Trim_B_1m_Breakable_32", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2944.3103, 2895.506, 2892.5469), (-0.00042724612344131137, -89.99926407230726, -3.051757488797057e-05), (0.8671872, 0.74999976, 0.46875057), "BP_Trim_B_1m_Breakable_33", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2944.317, 1691.8477, 2892.539), (-0.0004272461097297585, -89.99951687977065, -3.051758844424183e-05), (0.74999976, 0.74999976, 0.46874934), "BP_Trim_B_1m_Breakable_34", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3498.1313, 2846.8853, 2892.5483), (-3.051757831708132e-05, 90.00034336893043, 9.155276693488434e-05), (0.74999976, 0.74999976, 0.46874934), "BP_Trim_B_1m_Breakable_35", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3498.1313, 3283.2307, 2892.5483), (-3.0517570245353094e-05, 90.00046167098196, 9.155275667309818e-05), (0.8671872, 0.74999976, 0.46875057), "BP_Trim_B_1m_Breakable_36", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3498.144, 1216.8851, 2892.5488), (-3.051757831708132e-05, 90.00034336893043, 9.155276693488434e-05), (0.74999976, 0.74999976, 0.46874934), "BP_Trim_B_1m_Breakable_37", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2944.3105, 2511.8513, 2892.547), (-0.0004272461097297585, -89.99951687977065, -3.051758844424183e-05), (0.74999976, 0.74999976, 0.46874934), "BP_Trim_B_1m_Breakable_38", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2944.3281, 2075.506, 2892.545), (-0.00042724612344131137, -89.99926407230726, -3.051757488797057e-05), (0.8671872, 0.74999976, 0.46875057), "BP_Trim_B_1m_Breakable_39", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2944.3296, 871.84766, 2892.5334), (-0.0004272461097297585, -89.99951687977065, -3.051758844424183e-05), (0.74999976, 0.74999976, 0.46874934), "BP_Trim_B_1m_Breakable_40", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2944.3408, 1255.506, 2892.5393), (-0.00042724612344131137, -89.99926407230726, -3.051757488797057e-05), (0.8671872, 0.74999976, 0.46875057), "BP_Trim_B_1m_Breakable_41", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3498.146, 833.2285, 2892.549), (-3.0517570245353094e-05, 90.00046167098196, 9.155275667309818e-05), (0.8671872, 0.74999976, 0.46875057), "BP_Trim_B_1m_Breakable_42", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3498.1519, 396.88525, 2892.549), (-3.051757831708132e-05, 90.00034336893043, 9.155276693488434e-05), (0.74999976, 0.74999976, 0.46874934), "BP_Trim_B_1m_Breakable_43", _folder)
if a: placed += 1
else: skipped += 1

# Batch 5: StaticMesh'City_Trim_A_2m' (38 instances)
_mesh_path = "/Game/Art/Assets/Kits/Architecture/City/City_Trim_A_2m"
_materials = ['/Game/Art/Assets/Kits/Architecture/Suburbs/Materials/Suburbs_Trim_B/MI_Suburbs_Trim_B_Dest']
_folder = "Reconstruction/BD_BB_OrcTown_Gate/Meshes"
a = spawn_static_mesh(_mesh_path, _materials, (3685.637, 2586.9827, 2892.5486), (9.56226426119479e-05, 0.0003995660354925387, 2.049027820625621e-05), (0.74999976, 0.74999976, 0.46875057), "BP_Trim_B_2m_Breakable2_1", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3685.6306, 4226.9824, 2892.5486), (9.562264261197585e-05, 0.000399566035492532, 2.049027018484708e-05), (0.74999976, 0.74999976, 0.46875057), "BP_Trim_B_2m_Breakable2_2", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2756.842, 331.75317, 2892.5383), (-3.0517585389247004e-05, -179.99936479259551, 0.00043713229478201755), (0.74999976, 0.74999976, 0.46875057), "BP_Trim_B_2m_Breakable2_3", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3685.6375, 1776.9803, 2892.549), (9.56226426119479e-05, 0.0003995660354925387, 2.049027820625621e-05), (0.74999976, 0.74999976, 0.46875057), "BP_Trim_B_2m_Breakable2_10", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2756.808, 4179.3496, 2892.5493), (2.7320755585614844e-05, 0.0004883582975894641, -0.00042724608892752327), (0.74999976, 0.74999976, 0.46874934), "BP_Trim_B_2m_Breakable2_12", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3685.635, 3629.3926, 2892.5486), (-9.155273396700406e-05, -179.9995970188423, -3.0517578197921365e-05), (0.74999976, 0.74999976, 0.46874934), "BP_Trim_B_2m_Breakable2_31", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2756.8086, 3581.7566, 2892.5513), (-3.0517585389247004e-05, -179.99936479259551, 0.00043713229478201755), (0.74999976, 0.74999976, 0.46875057), "BP_Trim_B_2m_Breakable2_40", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2756.808, 3369.3494, 2892.5493), (2.7320755585871193e-05, 0.0004883583663443994, -0.00042724608892750695), (0.74999976, 0.74999976, 0.46874934), "BP_Trim_B_2m_Breakable2_42", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2756.8115, 2771.7532, 2892.546), (-3.0517585389247004e-05, -179.99936479259551, 0.00043713229478201755), (0.74999976, 0.74999976, 0.46875057), "BP_Trim_B_2m_Breakable2_44", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2756.8167, 1729.346, 2892.5393), (2.7320755585871193e-05, 0.0004883583663443994, -0.00042724608892750695), (0.74999976, 0.74999976, 0.46874934), "BP_Trim_B_2m_Breakable2_46", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3685.6316, 2809.3867, 2892.5486), (-9.155273396700406e-05, -179.9995970188423, -3.0517578197921365e-05), (0.74999976, 0.74999976, 0.46874934), "BP_Trim_B_2m_Breakable2_48", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3685.6306, 3406.9827, 2892.5486), (9.562264261197585e-05, 0.000399566035492532, 2.049027018484708e-05), (0.74999976, 0.74999976, 0.46875057), "BP_Trim_B_2m_Breakable2_50", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3685.6443, 1179.3866, 2892.549), (-9.155273396700406e-05, -179.9995970188423, -3.0517578197921365e-05), (0.74999976, 0.74999976, 0.46874934), "BP_Trim_B_2m_Breakable2_52", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2756.8103, 2549.3494, 2892.5474), (2.7320755585614844e-05, 0.0004883582975894641, -0.00042724608892752327), (0.74999976, 0.74999976, 0.46874934), "BP_Trim_B_2m_Breakable2_54", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2756.8293, 1951.7532, 2892.544), (-3.0517585389247004e-05, -179.99936479259551, 0.00043713229478201755), (0.74999976, 0.74999976, 0.46875057), "BP_Trim_B_2m_Breakable2_56", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2756.8293, 909.3458, 2892.5337), (2.7320755585614844e-05, 0.0004883582975894641, -0.00042724608892752327), (0.74999976, 0.74999976, 0.46874934), "BP_Trim_B_2m_Breakable2_58", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2756.842, 1131.7533, 2892.5383), (-3.0517585389247004e-05, -179.99936479259551, 0.00043713229478201755), (0.74999976, 0.74999976, 0.46875057), "BP_Trim_B_2m_Breakable2_60", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3685.6453, 956.98047, 2892.5493), (9.562264261197585e-05, 0.000399566035492532, 2.049027018484708e-05), (0.74999976, 0.74999976, 0.46875057), "BP_Trim_B_2m_Breakable2_62", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3685.652, 359.3867, 2892.5493), (-9.155273396700406e-05, -179.9995970188423, -3.0517578197921365e-05), (0.74999976, 0.74999976, 0.46874934), "BP_Trim_B_2m_Breakable2_64", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3535.6372, 2586.981, 2892.5483), (9.56226426119479e-05, 0.0003995660354925387, 2.049027820625621e-05), (0.74999976, 0.74999976, 0.46875057), "BP_Trim_B_2m_Breakable3_2", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3535.6309, 4226.981, 2892.5483), (9.562264261197585e-05, 0.000399566035492532, 2.049027018484708e-05), (0.74999976, 0.74999976, 0.46875057), "BP_Trim_B_2m_Breakable3_3", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2906.8418, 331.75537, 2892.5383), (-3.0517585389247004e-05, -179.99936479259551, 0.00043713229478201755), (0.74999976, 0.74999976, 0.46875057), "BP_Trim_B_2m_Breakable3_4", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3535.6377, 1776.979, 2892.5488), (9.56226426119479e-05, 0.0003995660354925387, 2.049027820625621e-05), (0.74999976, 0.74999976, 0.46875057), "BP_Trim_B_2m_Breakable3_11", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2606.808, 4179.3486, 2892.5493), (2.7320755585614844e-05, 0.0004883582975894641, -0.00042724608892752327), (0.74999976, 0.74999976, 0.46874934), "BP_Trim_B_2m_Breakable3_13", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3835.635, 3629.3938, 2892.5488), (-9.155273396700406e-05, -179.9995970188423, -3.0517578197921365e-05), (0.74999976, 0.74999976, 0.46874934), "BP_Trim_B_2m_Breakable3_32", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2906.8083, 3581.7588, 2892.5513), (-3.0517585389247004e-05, -179.99936479259551, 0.00043713229478201755), (0.74999976, 0.74999976, 0.46875057), "BP_Trim_B_2m_Breakable3_41", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2606.808, 3369.348, 2892.5493), (2.7320755585871193e-05, 0.0004883583663443994, -0.00042724608892750695), (0.74999976, 0.74999976, 0.46874934), "BP_Trim_B_2m_Breakable3_43", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2906.8113, 2771.7554, 2892.546), (-3.0517585389247004e-05, -179.99936479259551, 0.00043713229478201755), (0.74999976, 0.74999976, 0.46875057), "BP_Trim_B_2m_Breakable3_45", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2606.8167, 1729.3445, 2892.5393), (2.7320755585871193e-05, 0.0004883583663443994, -0.00042724608892750695), (0.74999976, 0.74999976, 0.46874934), "BP_Trim_B_2m_Breakable3_47", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3835.6316, 2809.388, 2892.5488), (-9.155273396700406e-05, -179.9995970188423, -3.0517578197921365e-05), (0.74999976, 0.74999976, 0.46874934), "BP_Trim_B_2m_Breakable3_49", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3535.6309, 3406.981, 2892.5483), (9.562264261197585e-05, 0.000399566035492532, 2.049027018484708e-05), (0.74999976, 0.74999976, 0.46875057), "BP_Trim_B_2m_Breakable3_51", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3835.6443, 1179.3878, 2892.5493), (-9.155273396700406e-05, -179.9995970188423, -3.0517578197921365e-05), (0.74999976, 0.74999976, 0.46874934), "BP_Trim_B_2m_Breakable3_53", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2606.8103, 2549.348, 2892.5474), (2.7320755585614844e-05, 0.0004883582975894641, -0.00042724608892752327), (0.74999976, 0.74999976, 0.46874934), "BP_Trim_B_2m_Breakable3_55", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2906.829, 1951.7554, 2892.544), (-3.0517585389247004e-05, -179.99936479259551, 0.00043713229478201755), (0.74999976, 0.74999976, 0.46875057), "BP_Trim_B_2m_Breakable3_57", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2606.8293, 909.3445, 2892.5337), (2.7320755585614844e-05, 0.0004883582975894641, -0.00042724608892752327), (0.74999976, 0.74999976, 0.46874934), "BP_Trim_B_2m_Breakable3_59", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2906.8418, 1131.7555, 2892.5383), (-3.0517585389247004e-05, -179.99936479259551, 0.00043713229478201755), (0.74999976, 0.74999976, 0.46875057), "BP_Trim_B_2m_Breakable3_61", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3535.6455, 956.9789, 2892.549), (9.562264261197585e-05, 0.000399566035492532, 2.049027018484708e-05), (0.74999976, 0.74999976, 0.46875057), "BP_Trim_B_2m_Breakable3_63", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3835.652, 359.38788, 2892.5496), (-9.155273396700406e-05, -179.9995970188423, -3.0517578197921365e-05), (0.74999976, 0.74999976, 0.46874934), "BP_Trim_B_2m_Breakable3_65", _folder)
if a: placed += 1
else: skipped += 1

# Batch 6: StaticMesh'City_Trim_A_3m' (73 instances)
_mesh_path = "/Game/Art/Assets/Kits/Architecture/City/City_Trim_A_3m"
_materials = ['/Game/Art/Assets/Kits/Architecture/Suburbs/Materials/Suburbs_Trim_B/MI_Suburbs_Trim_B_Dest']
_folder = "Reconstruction/BD_BB_OrcTown_Gate/Meshes"
a = spawn_static_mesh(_mesh_path, _materials, (4187.2715, 3123.633, 2307.4268), (0.0016460753950717066, 90.00084578908333, 0.0014179998726190045), (1.0, 1.0, 1.0), "BP_Trim_B_3m_B_Breakable100", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4187.2656, 3423.633, 2307.4355), (0.0016460753950717066, 90.00084578908333, 0.0014179998726190045), (1.0, 1.0, 1.0), "BP_Trim_B_3m_B_Breakable101", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4187.258, 3823.633, 2307.4473), (0.0016460753950717066, 90.00084578908333, 0.0014179998726190045), (1.0, 1.0, 1.0), "BP_Trim_B_3m_B_Breakable102", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4125.226, 1535.129, 2387.372), (1.3660372835109785e-05, 90.00014890026316, 9.46083703487228e-05), (1.0, 1.0, 1.0), "BP_Trim_B_3m_B_Breakable21", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4125.2246, 1835.1294, 2387.3718), (1.3660372835109785e-05, 90.00014890026316, 9.46083703487228e-05), (1.0, 1.0, 1.0), "BP_Trim_B_3m_B_Breakable22", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4125.229, 2135.1304, 2387.3718), (1.3660372835109785e-05, 90.00014890026316, 9.46083703487228e-05), (1.0, 1.0, 1.0), "BP_Trim_B_3m_B_Breakable23_14", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4125.2246, 2435.1294, 2387.3718), (1.3660372835109785e-05, 90.00014890026316, 9.46083703487228e-05), (1.0, 1.0, 1.0), "BP_Trim_B_3m_B_Breakable24", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4125.225, 2735.1296, 2387.3718), (1.3660372835109785e-05, 90.00014890026316, 9.46083703487228e-05), (1.0, 1.0, 1.0), "BP_Trim_B_3m_B_Breakable25", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2317.22, 3823.6099, 2387.377), (-6.10351567204183e-05, -89.99963031861111, 0.0001155911450248884), (1.0, 1.0, 1.0), "BP_Trim_B_3m_B_Breakable26_67", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2317.2227, 3523.6086, 2387.3716), (-6.10351567204183e-05, -89.99963031861111, 0.0001155911450248884), (1.0, 1.0, 1.0), "BP_Trim_B_3m_B_Breakable27_68", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2317.2236, 2923.6084, 2387.3696), (-6.10351567204183e-05, -89.99963031861111, 0.0001155911450248884), (1.0, 1.0, 1.0), "BP_Trim_B_3m_B_Breakable28_69", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2317.2239, 2623.6077, 2387.0146), (-6.10351567204183e-05, -89.99963031861111, 0.0001155911450248884), (1.0, 1.0, 1.0), "BP_Trim_B_3m_B_Breakable29_70", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2317.2192, 3223.6077, 2387.3696), (-6.10351567204183e-05, -89.99963031861111, 0.0001155911450248884), (1.0, 1.0, 1.0), "BP_Trim_B_3m_B_Breakable30_71", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2497.2239, 2503.6077, 2387.3696), (-6.103515689188501e-05, -179.99952188676656, 0.00011600001278235784), (1.0, 1.0, 1.0), "BP_Trim_B_3m_B_Breakable31", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2797.2239, 2503.6077, 2387.3696), (-6.103515689188501e-05, -179.99952188676656, 0.00011600001278235784), (1.0, 1.0, 1.0), "BP_Trim_B_3m_B_Breakable32", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4125.226, 3035.1287, 2387.3718), (1.3660372835109785e-05, 90.00014890026316, 9.46083703487228e-05), (1.0, 1.0, 1.0), "BP_Trim_B_3m_B_Breakable33", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4125.2256, 3335.129, 2387.3718), (1.3660372835109785e-05, 90.00014890026316, 9.46083703487228e-05), (1.0, 1.0, 1.0), "BP_Trim_B_3m_B_Breakable34", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2317.2234, 2323.6108, 2387.368), (-6.10351567204183e-05, -89.99963031861111, 0.0001155911450248884), (1.0, 1.0, 1.0), "BP_Trim_B_3m_B_Breakable35_72", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2317.225, 2023.6108, 2387.3647), (-6.10351567204183e-05, -89.99963031861111, 0.0001155911450248884), (1.0, 1.0, 1.0), "BP_Trim_B_3m_B_Breakable36_73", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3827.2239, 2503.6077, 2387.3696), (-6.103515689188501e-05, -179.99952188676656, 0.00011600001278235784), (1.0, 1.0, 1.0), "BP_Trim_B_3m_B_Breakable39", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4127.2236, 2503.6077, 2387.3696), (-6.103515689188501e-05, -179.99952188676656, 0.00011600001278235784), (1.0, 1.0, 1.0), "BP_Trim_B_3m_B_Breakable40", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3937.2231, 2653.6072, 2387.3696), (-6.103515472077006e-05, 0.0003967284748017688, 0.00011600006758903726), (1.0, 1.0, 1.0), "BP_Trim_B_3m_B_Breakable41", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3637.2236, 2653.6077, 2387.3696), (-6.103515472077006e-05, 0.0003967284748017688, 0.00011600006758903726), (1.0, 1.0, 1.0), "BP_Trim_B_3m_B_Breakable42", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3487.2231, 2653.6072, 2387.3696), (-6.103515499538292e-05, 0.00039699998804176867, 0.00011599999868948609), (1.0, 1.0, 1.0), "BP_Trim_B_3m_B_Breakable43", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4125.2266, 3635.1318, 2387.3718), (1.3660372835109785e-05, 90.00014890026316, 9.46083703487228e-05), (1.0, 1.0, 1.0), "BP_Trim_B_3m_B_Breakable44", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2317.224, 1723.6077, 2387.3613), (-6.10351567204183e-05, -89.99963031861111, 0.0001155911450248884), (1.0, 1.0, 1.0), "BP_Trim_B_3m_B_Breakable45_74", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2317.227, 1423.6077, 2387.3613), (-6.10351547889268e-05, -89.99963031861175, 0.00011600000170280526), (1.0, 1.0, 1.0), "BP_Trim_B_3m_B_Breakable46_81", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2317.2297, 1123.6077, 2387.3613), (-6.10351547889268e-05, -89.99963031861175, 0.00011600000170280526), (1.0, 1.0, 1.0), "BP_Trim_B_3m_B_Breakable47_83", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2317.2317, 823.60767, 2387.3613), (-6.10351547889268e-05, -89.99963031861175, 0.00011600000170280526), (1.0, 1.0, 1.0), "BP_Trim_B_3m_B_Breakable48_85", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4125.2266, 3935.1318, 2387.3718), (1.3660374728760628e-05, 90.00014890026353, 9.499997847756346e-05), (1.0, 1.0, 1.0), "BP_Trim_B_3m_B_Breakable49", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4125.2266, 4235.132, 2387.3718), (1.3660374728760628e-05, 90.00014890026353, 9.499997847756346e-05), (1.0, 1.0, 1.0), "BP_Trim_B_3m_B_Breakable50", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4125.2217, 1235.1309, 2387.372), (1.3660372835109785e-05, 90.00014890026316, 9.46083703487228e-05), (1.0, 1.0, 1.0), "BP_Trim_B_3m_B_Breakable51", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2317.2236, 4123.607, 2387.3787), (-6.10351567204183e-05, -89.99963031861111, 0.0001155911450248884), (1.0, 1.0, 1.0), "BP_Trim_B_3m_B_Breakable52_75", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4125.2217, 935.13086, 2387.372), (1.3660374728760628e-05, 90.00014890026353, 9.499997847756346e-05), (1.0, 1.0, 1.0), "BP_Trim_B_3m_B_Breakable53_77", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4125.2217, 635.13086, 2387.372), (1.3660374728760628e-05, 90.00014890026353, 9.499997847756346e-05), (1.0, 1.0, 1.0), "BP_Trim_B_3m_B_Breakable54_79", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2317.234, 523.60767, 2387.3613), (-6.10351547889268e-05, -89.99963031861175, 0.00011600000170280526), (1.0, 1.0, 1.0), "BP_Trim_B_3m_B_Breakable55", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2487.2236, 2653.6077, 2387.3696), (-6.103515499538292e-05, 0.00039699998804176867, 0.00011599999868948609), (1.0, 1.0, 1.0), "BP_Trim_B_3m_B_Breakable58", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2187.2236, 2653.6077, 2387.3696), (-6.103515499538292e-05, 0.00039699998804176867, 0.00011599999868948609), (1.0, 1.0, 1.0), "BP_Trim_B_3m_B_Breakable59", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2497.2239, 4313.6074, 2387.3696), (-6.1035146282043195e-05, -179.99950822622802, 0.00011599998244734826), (1.0, 1.0, 1.0), "BP_Trim_B_3m_B_Breakable60", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2797.2239, 4313.6074, 2387.3696), (-6.1035146282043195e-05, -179.99950822622802, 0.00011599998244734826), (1.0, 1.0, 1.0), "BP_Trim_B_3m_B_Breakable61", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3827.2239, 4313.6074, 2387.3696), (-6.1035146282043195e-05, -179.99950822622802, 0.00011599998244734826), (1.0, 1.0, 1.0), "BP_Trim_B_3m_B_Breakable64", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4127.2236, 4313.608, 2387.3696), (-6.1035146282043195e-05, -179.99950822622802, 0.00011599998244734826), (1.0, 1.0, 1.0), "BP_Trim_B_3m_B_Breakable65", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3837.223, 4463.6074, 2387.3696), (-6.103515249150058e-05, 0.0004024505126286802, 0.00011599999578640845), (1.0, 1.0, 1.0), "BP_Trim_B_3m_B_Breakable66", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3537.2236, 4463.6074, 2387.3696), (-6.103515249150058e-05, 0.0004024505126286802, 0.00011599999578640845), (1.0, 1.0, 1.0), "BP_Trim_B_3m_B_Breakable67", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2487.2236, 4463.6074, 2387.3696), (-6.103515249150058e-05, 0.0004024505126286802, 0.00011599999578640845), (1.0, 1.0, 1.0), "BP_Trim_B_3m_B_Breakable71", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2187.2236, 4463.6074, 2387.3696), (-6.103515249150058e-05, 0.0004024505126286802, 0.00011599999578640845), (1.0, 1.0, 1.0), "BP_Trim_B_3m_B_Breakable72", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4125.2217, 335.13086, 2387.372), (1.3660374728760628e-05, 90.00014890026353, 9.499997847756346e-05), (1.0, 1.0, 1.0), "BP_Trim_B_3m_B_Breakable73", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4125.2217, 35.130863, 2387.372), (1.3660374728760628e-05, 90.00014890026353, 9.499997847756346e-05), (1.0, 1.0, 1.0), "BP_Trim_B_3m_B_Breakable74", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2317.2366, 223.60767, 2387.3613), (-6.10351547889268e-05, -89.99963031861175, 0.00011600000170280526), (1.0, 1.0, 1.0), "BP_Trim_B_3m_B_Breakable75", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2247.2234, 2373.6108, 2307.368), (-6.10351547889268e-05, -89.99963031861175, 0.00011600000170280526), (1.0, 1.0, 1.0), "BP_Trim_B_3m_B_Breakable76", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2247.2234, 2073.6108, 2307.368), (-6.10351547889268e-05, -89.99963031861175, 0.00011600000170280526), (1.0, 1.0, 1.0), "BP_Trim_B_3m_B_Breakable77", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2247.2234, 2973.6108, 2307.368), (-6.10351547889268e-05, -89.99963031861175, 0.00011600000170280526), (1.0, 1.0, 1.0), "BP_Trim_B_3m_B_Breakable78", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2247.2234, 2673.6108, 2307.368), (-6.10351547889268e-05, -89.99963031861175, 0.00011600000170280526), (1.0, 1.0, 1.0), "BP_Trim_B_3m_B_Breakable79", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2247.2234, 3573.6108, 2307.368), (-6.10351547889268e-05, -89.99963031861175, 0.00011600000170280526), (1.0, 1.0, 1.0), "BP_Trim_B_3m_B_Breakable80", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2247.2234, 3273.6108, 2307.368), (-6.10351547889268e-05, -89.99963031861175, 0.00011600000170280526), (1.0, 1.0, 1.0), "BP_Trim_B_3m_B_Breakable81", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2247.2234, 4173.611, 2307.368), (-6.10351547889268e-05, -89.99963031861175, 0.00011600000170280526), (1.0, 1.0, 1.0), "BP_Trim_B_3m_B_Breakable82", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2247.2234, 3873.6108, 2307.368), (-6.10351547889268e-05, -89.99963031861175, 0.00011600000170280526), (1.0, 1.0, 1.0), "BP_Trim_B_3m_B_Breakable83", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2247.2234, 1773.6108, 2307.368), (-6.10351547889268e-05, -89.99963031861175, 0.00011600000170280526), (1.0, 1.0, 1.0), "BP_Trim_B_3m_B_Breakable84", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2247.2234, 1473.6108, 2307.368), (-6.10351547889268e-05, -89.99963031861175, 0.00011600000170280526), (1.0, 1.0, 1.0), "BP_Trim_B_3m_B_Breakable85", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2247.2234, 1173.6108, 2307.368), (-6.10351547889268e-05, -89.99963031861175, 0.00011600000170280526), (1.0, 1.0, 1.0), "BP_Trim_B_3m_B_Breakable86", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2247.2234, 873.61084, 2307.368), (-6.10351547889268e-05, -89.99963031861175, 0.00011600000170280526), (1.0, 1.0, 1.0), "BP_Trim_B_3m_B_Breakable87", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2247.2234, 573.61084, 2307.368), (-6.10351547889268e-05, -89.99963031861175, 0.00011600000170280526), (1.0, 1.0, 1.0), "BP_Trim_B_3m_B_Breakable88", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2247.2234, 273.61084, 2307.368), (-6.10351547889268e-05, -89.99963031861175, 0.00011600000170280526), (1.0, 1.0, 1.0), "BP_Trim_B_3m_B_Breakable89", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4187.3003, 1623.633, 2307.3828), (0.0016460753954952371, 90.0008457890818, 0.0014179428285796877), (1.0, 1.0, 1.0), "BP_Trim_B_3m_B_Breakable90_15", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4187.306, 1323.633, 2307.374), (0.0016460753950717066, 90.00084578908333, 0.0014179998726190045), (1.0, 1.0, 1.0), "BP_Trim_B_3m_B_Breakable91_17", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4187.312, 1023.63306, 2307.3652), (0.0016460753950717066, 90.00084578908333, 0.0014179998726190045), (1.0, 1.0, 1.0), "BP_Trim_B_3m_B_Breakable92", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4187.318, 723.63306, 2307.3564), (0.0016460753950717066, 90.00084578908333, 0.0014179998726190045), (1.0, 1.0, 1.0), "BP_Trim_B_3m_B_Breakable93", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4187.3237, 423.63306, 2307.3477), (0.0016460753950717066, 90.00084578908333, 0.0014179998726190045), (1.0, 1.0, 1.0), "BP_Trim_B_3m_B_Breakable94", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4187.3296, 123.63306, 2307.3389), (0.0016460753950717066, 90.00084578908333, 0.0014179998726190045), (1.0, 1.0, 1.0), "BP_Trim_B_3m_B_Breakable95", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4187.2944, 1923.633, 2307.3916), (0.0016460753950717066, 90.00084578908333, 0.0014179998726190045), (1.0, 1.0, 1.0), "BP_Trim_B_3m_B_Breakable96", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4187.2886, 2223.633, 2307.4004), (0.0016460753950717066, 90.00084578908333, 0.0014179998726190045), (1.0, 1.0, 1.0), "BP_Trim_B_3m_B_Breakable97", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4187.283, 2523.633, 2307.4092), (0.0016460753950717066, 90.00084578908333, 0.0014179998726190045), (1.0, 1.0, 1.0), "BP_Trim_B_3m_B_Breakable98", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4187.2773, 2823.633, 2307.418), (0.0016460753950717066, 90.00084578908333, 0.0014179998726190045), (1.0, 1.0, 1.0), "BP_Trim_B_3m_B_Breakable99", _folder)
if a: placed += 1
else: skipped += 1

# Batch 7: StaticMesh'City_Trim_A_Corner_0_5m' (57 instances)
_mesh_path = "/Game/Art/Assets/Kits/Architecture/City/City_Trim_A_Corner_0_5m"
_materials = ['/Game/Art/Assets/Kits/Architecture/Suburbs/Materials/Suburbs_Trim_B/MI_Suburbs_Trim_B_Dest']
_folder = "Reconstruction/BD_BB_OrcTown_Gate/Meshes"
a = spawn_static_mesh(_mesh_path, _materials, (3498.1377, 2549.4807, 2892.5483), (-3.051758006242164e-05, 90.00037578044967, 9.155280093117228e-05), (0.74999976, 0.74999976, 0.46875057), "BP_Trim_B_Corner_0_5m_Breakable_1", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3498.1313, 4189.4805, 2892.5483), (-3.051758006242164e-05, 90.00037578044967, 9.155280093117228e-05), (0.74999976, 0.74999976, 0.46875057), "BP_Trim_B_Corner_0_5m_Breakable_2", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2944.3413, 369.25122, 2892.5388), (-0.00042724607956581324, -89.99938723476131, -3.0517585690276625e-05), (0.74999976, 0.74999976, 0.46875057), "BP_Trim_B_Corner_0_5m_Breakable_3", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3498.1382, 1739.4785, 2892.5488), (-3.051758006242164e-05, 90.00037578044967, 9.155280093117228e-05), (0.74999976, 0.74999976, 0.46875057), "BP_Trim_B_Corner_0_5m_Breakable_8", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2906.808, 4179.351, 2892.5493), (2.7320755585614844e-05, 0.0004883582975894641, -0.00042724608892752327), (0.74999976, 0.74999976, 0.46874934), "BP_Trim_B_Corner_0_5m_Breakable_19", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3535.635, 3629.3914, 2892.5483), (-9.155273396700406e-05, -179.9995970188423, -3.0517578197921365e-05), (0.74999976, 0.74999976, 0.46874934), "BP_Trim_B_Corner_0_5m_Breakable_47", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2944.3079, 3619.2593, 2892.5518), (-0.00042724607956581324, -89.99938723476131, -3.0517585690276625e-05), (0.74999976, 0.74999976, 0.46875057), "BP_Trim_B_Corner_0_5m_Breakable_57", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2906.808, 3369.3508, 2892.5493), (2.7320755585871193e-05, 0.0004883583663443994, -0.00042724608892750695), (0.74999976, 0.74999976, 0.46874934), "BP_Trim_B_Corner_0_5m_Breakable_60", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2944.3108, 2809.2559, 2892.5464), (-0.00042724607956581324, -89.99938723476131, -3.0517585690276625e-05), (0.74999976, 0.74999976, 0.46875057), "BP_Trim_B_Corner_0_5m_Breakable_63", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2906.8164, 1729.3473, 2892.5393), (2.7320755585871193e-05, 0.0004883583663443994, -0.00042724608892750695), (0.74999976, 0.74999976, 0.46874934), "BP_Trim_B_Corner_0_5m_Breakable_66", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3535.6316, 2809.3855, 2892.5483), (-9.155273396700406e-05, -179.9995970188423, -3.0517578197921365e-05), (0.74999976, 0.74999976, 0.46874934), "BP_Trim_B_Corner_0_5m_Breakable_69", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3498.1313, 3369.4807, 2892.5483), (-3.051758006242164e-05, 90.00037578044967, 9.155280093117228e-05), (0.74999976, 0.74999976, 0.46875057), "BP_Trim_B_Corner_0_5m_Breakable_72", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3535.6443, 1179.3855, 2892.5488), (-9.155273396700406e-05, -179.9995970188423, -3.0517578197921365e-05), (0.74999976, 0.74999976, 0.46874934), "BP_Trim_B_Corner_0_5m_Breakable_75", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2906.81, 2549.3508, 2892.5474), (2.7320755585614844e-05, 0.0004883582975894641, -0.00042724608892752327), (0.74999976, 0.74999976, 0.46874934), "BP_Trim_B_Corner_0_5m_Breakable_78", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2944.3286, 1989.2561, 2892.5444), (-0.00042724607956581324, -89.99938723476131, -3.0517585690276625e-05), (0.74999976, 0.74999976, 0.46875057), "BP_Trim_B_Corner_0_5m_Breakable_81", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2906.829, 909.3473, 2892.5337), (2.7320755585614844e-05, 0.0004883582975894641, -0.00042724608892752327), (0.74999976, 0.74999976, 0.46874934), "BP_Trim_B_Corner_0_5m_Breakable_84", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2944.3413, 1169.2559, 2892.5388), (-0.00042724607956581324, -89.99938723476131, -3.0517585690276625e-05), (0.74999976, 0.74999976, 0.46875057), "BP_Trim_B_Corner_0_5m_Breakable_87", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3498.146, 919.4785, 2892.549), (-3.051758006242164e-05, 90.00037578044967, 9.155280093117228e-05), (0.74999976, 0.74999976, 0.46875057), "BP_Trim_B_Corner_0_5m_Breakable_90", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3535.652, 359.3855, 2892.549), (-9.155273396700406e-05, -179.9995970188423, -3.0517578197921365e-05), (0.74999976, 0.74999976, 0.46874934), "BP_Trim_B_Corner_0_5m_Breakable_93", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4026.8877, 2455.736, 2662.8616), (-3.0517579461092403e-05, 90.00079713058769, 9.155267202413428e-05), (0.74999976, 0.74999976, 0.46875057), "BP_Trim_B_Corner_0_5m_Breakable2_2", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4026.8813, 4095.736, 2662.8616), (-3.0517579461092403e-05, 90.00079713058769, 9.155267202413428e-05), (0.74999976, 0.74999976, 0.46875057), "BP_Trim_B_Corner_0_5m_Breakable2_3", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2415.5913, 463.00012, 2662.852), (-0.00042724607863737856, -89.99896588978906, -3.051758468288616e-05), (0.74999976, 0.74999976, 0.46875057), "BP_Trim_B_Corner_0_5m_Breakable2_4", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4026.8882, 1645.7338, 2662.862), (-3.0517579461092403e-05, 90.00079713058769, 9.155267202413428e-05), (0.74999976, 0.74999976, 0.46875057), "BP_Trim_B_Corner_0_5m_Breakable2_9", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2378.059, 4085.6, 2662.8608), (2.7320755585614844e-05, 0.0004883582975894641, -0.00042724608892752327), (0.74999976, 0.74999976, 0.46874934), "BP_Trim_B_Corner_0_5m_Breakable2_20", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4064.3848, 3723.1428, 2662.8616), (-9.155273396700406e-05, -179.9995970188423, -3.0517578197921365e-05), (0.74999976, 0.74999976, 0.46874934), "BP_Trim_B_Corner_0_5m_Breakable2_48", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2415.5579, 3713.0034, 2662.865), (-0.00042724607863737856, -89.99896588978906, -3.051758468288616e-05), (0.74999976, 0.74999976, 0.46875057), "BP_Trim_B_Corner_0_5m_Breakable2_58", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2378.059, 3275.6, 2662.8608), (2.7320755585871193e-05, 0.0004883583663443994, -0.00042724608892750695), (0.74999976, 0.74999976, 0.46874934), "BP_Trim_B_Corner_0_5m_Breakable2_61", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2415.5608, 2903.0, 2662.8596), (-0.00042724607863737856, -89.99896588978906, -3.051758468288616e-05), (0.74999976, 0.74999976, 0.46875057), "BP_Trim_B_Corner_0_5m_Breakable2_64", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2378.0676, 1635.5967, 2662.8508), (2.7320755585871193e-05, 0.0004883583663443994, -0.00042724608892750695), (0.74999976, 0.74999976, 0.46874934), "BP_Trim_B_Corner_0_5m_Breakable2_67", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4064.3813, 2903.137, 2662.8618), (-9.155273396700406e-05, -179.9995970188423, -3.0517578197921365e-05), (0.74999976, 0.74999976, 0.46874934), "BP_Trim_B_Corner_0_5m_Breakable2_70", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4026.8813, 3275.736, 2662.8616), (-3.0517579461092403e-05, 90.00079713058769, 9.155267202413428e-05), (0.74999976, 0.74999976, 0.46875057), "BP_Trim_B_Corner_0_5m_Breakable2_73", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4064.394, 1273.137, 2662.8623), (-9.155273396700406e-05, -179.9995970188423, -3.0517578197921365e-05), (0.74999976, 0.74999976, 0.46874934), "BP_Trim_B_Corner_0_5m_Breakable2_76", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2378.0613, 2455.6, 2662.859), (2.7320755585614844e-05, 0.0004883582975894641, -0.00042724608892752327), (0.74999976, 0.74999976, 0.46874934), "BP_Trim_B_Corner_0_5m_Breakable2_79", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2415.5786, 2083.0, 2662.8577), (-0.00042724607863737856, -89.99896588978906, -3.051758468288616e-05), (0.74999976, 0.74999976, 0.46875057), "BP_Trim_B_Corner_0_5m_Breakable2_82", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2378.0803, 815.5967, 2662.8452), (2.7320755585614844e-05, 0.0004883582975894641, -0.00042724608892752327), (0.74999976, 0.74999976, 0.46874934), "BP_Trim_B_Corner_0_5m_Breakable2_85", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2415.5913, 1263.0001, 2662.852), (-0.00042724607863737856, -89.99896588978906, -3.051758468288616e-05), (0.74999976, 0.74999976, 0.46875057), "BP_Trim_B_Corner_0_5m_Breakable2_88", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4026.896, 825.73376, 2662.8623), (-3.0517579461092403e-05, 90.00079713058769, 9.155267202413428e-05), (0.74999976, 0.74999976, 0.46875057), "BP_Trim_B_Corner_0_5m_Breakable2_91", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4064.4019, 453.13693, 2662.8623), (-9.155273396700406e-05, -179.9995970188423, -3.0517578197921365e-05), (0.74999976, 0.74999976, 0.46874934), "BP_Trim_B_Corner_0_5m_Breakable2_94", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3975.1414, 2286.2354, 2613.6428), (-3.0517579461092403e-05, 90.00079713058769, 9.155267202413428e-05), (0.87479144, 0.87479144, 0.546745), "BP_Trim_B_Corner_0_5m_Breakable3_3", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3975.135, 3926.2354, 2613.6428), (-3.0517579461092403e-05, 90.00079713058769, 9.155267202413428e-05), (0.87479144, 0.87479144, 0.546745), "BP_Trim_B_Corner_0_5m_Breakable3_4", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2467.3372, 632.5012, 2613.6348), (-0.00042724607863737856, -89.99896588978906, -3.051758468288616e-05), (0.87479144, 0.87479144, 0.546745), "BP_Trim_B_Corner_0_5m_Breakable3_5", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3975.1418, 1476.2333, 2613.6433), (-3.0517579461092403e-05, 90.00079713058769, 9.155267202413428e-05), (0.87479144, 0.87479144, 0.546745), "BP_Trim_B_Corner_0_5m_Breakable3_10", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2423.0605, 3924.3535, 2613.6409), (2.7320755585614844e-05, 0.0004883582975894641, -0.00042724608892752327), (0.87479156, 0.87479156, 0.5467446), "BP_Trim_B_Corner_0_5m_Breakable3_21", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4019.3838, 3884.39, 2613.6428), (-9.155273396700406e-05, -179.9995970188423, -3.0517578197921365e-05), (0.87479156, 0.87479156, 0.5467446), "BP_Trim_B_Corner_0_5m_Breakable3_49", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2467.3037, 3882.5046, 2613.6477), (-0.00042724607863737856, -89.99896588978906, -3.051758468288616e-05), (0.87479144, 0.87479144, 0.546745), "BP_Trim_B_Corner_0_5m_Breakable3_59", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2423.0605, 3114.3535, 2613.6409), (2.7320755585871193e-05, 0.0004883583663443994, -0.00042724608892750695), (0.87479156, 0.87479156, 0.5467446), "BP_Trim_B_Corner_0_5m_Breakable3_62", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2467.3066, 3072.5012, 2613.6423), (-0.00042724607863737856, -89.99896588978906, -3.051758468288616e-05), (0.87479144, 0.87479144, 0.546745), "BP_Trim_B_Corner_0_5m_Breakable3_65", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2423.069, 1474.35, 2613.6309), (2.7320755585871193e-05, 0.0004883583663443994, -0.00042724608892750695), (0.87479156, 0.87479156, 0.5467446), "BP_Trim_B_Corner_0_5m_Breakable3_68", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4019.38, 3064.384, 2613.6428), (-9.155273396700406e-05, -179.9995970188423, -3.0517578197921365e-05), (0.87479156, 0.87479156, 0.5467446), "BP_Trim_B_Corner_0_5m_Breakable3_71", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3975.135, 3106.2354, 2613.6428), (-3.0517579461092403e-05, 90.00079713058769, 9.155267202413428e-05), (0.87479144, 0.87479144, 0.546745), "BP_Trim_B_Corner_0_5m_Breakable3_74", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4019.393, 1434.384, 2613.6433), (-9.155273396700406e-05, -179.9995970188423, -3.0517578197921365e-05), (0.87479156, 0.87479156, 0.5467446), "BP_Trim_B_Corner_0_5m_Breakable3_77", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2423.0627, 2294.3535, 2613.639), (2.7320755585614844e-05, 0.0004883582975894641, -0.00042724608892752327), (0.87479156, 0.87479156, 0.5467446), "BP_Trim_B_Corner_0_5m_Breakable3_80", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2467.3245, 2252.5012, 2613.6404), (-0.00042724607863737856, -89.99896588978906, -3.051758468288616e-05), (0.87479144, 0.87479144, 0.546745), "BP_Trim_B_Corner_0_5m_Breakable3_83", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2423.0818, 654.3502, 2613.6252), (2.7320755585614844e-05, 0.0004883582975894641, -0.00042724608892752327), (0.87479156, 0.87479156, 0.5467446), "BP_Trim_B_Corner_0_5m_Breakable3_86", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2467.3372, 1432.5012, 2613.6348), (-0.00042724607863737856, -89.99896588978906, -3.051758468288616e-05), (0.87479144, 0.87479144, 0.546745), "BP_Trim_B_Corner_0_5m_Breakable3_89", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3975.1497, 656.23315, 2613.6436), (-3.0517579461092403e-05, 90.00079713058769, 9.155267202413428e-05), (0.87479144, 0.87479144, 0.546745), "BP_Trim_B_Corner_0_5m_Breakable3_92", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4019.4004, 614.38403, 2613.6436), (-9.155273396700406e-05, -179.9995970188423, -3.0517578197921365e-05), (0.87479156, 0.87479156, 0.5467446), "BP_Trim_B_Corner_0_5m_Breakable3_95", _folder)
if a: placed += 1
else: skipped += 1

# Batch 8: StaticMesh'NonD_Stairs_Trim_A_L' (7 instances)
_mesh_path = "/Game/Art/Assets/Kits/Architecture/Non_D/NonD_Stairs_Trim_A_L"
_materials = ['/Game/Art/Assets/Kits/Architecture/Suburbs/Materials/Suburbs_Trim_Sheet_A/MI_Suburbs_Trim_Sheet_A', '/Game/Environments/Materials/MI_Suburbs_Non_Destructible']
_folder = "Reconstruction/BD_BB_OrcTown_Gate/Meshes"
a = spawn_static_mesh(_mesh_path, _materials, (5150.0, 1600.0, 900.0), (0.0, 0.0, -0.0), (1.0, 1.0, 1.0), "NonD_Stairs_Trim_A_L_49", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3600.0, 2350.0, 1000.0), (0.0, -89.99999818714215, 0.0), (1.0, 1.0, 1.0), "NonD_Stairs_Trim_A_L3", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2800.0, 2350.0, 1000.0), (0.0, -89.99999818714215, 0.0), (1.0, 1.0, 1.0), "NonD_Stairs_Trim_A_L4", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2750.0, 2500.0, 1100.0), (0.0, -89.99999818714215, 0.0), (1.0, 1.0, 1.0), "NonD_Stairs_Trim_A_L5", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3650.0, 2500.0, 1100.0), (0.0, -89.99999818714215, 0.0), (1.0, 1.0, 1.0), "NonD_Stairs_Trim_A_L6", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4400.0, 2500.0, 1100.0), (0.0, -89.99999818714215, 0.0), (1.0, 1.0, 1.0), "NonD_Stairs_Trim_A_L7", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2750.0, 3700.0, 1100.0), (0.0, 7.772445218862483e-05, -0.0), (1.0, 1.0, 1.0), "NonD_Stairs_Trim_A_L8", _folder)
if a: placed += 1
else: skipped += 1

# Batch 9: StaticMesh'NonD_Stairs_Trim_A_R' (2 instances)
_mesh_path = "/Game/Art/Assets/Kits/Architecture/Non_D/NonD_Stairs_Trim_A_R"
_materials = ['/Game/Art/Assets/Kits/Architecture/Suburbs/Materials/Suburbs_Trim_Sheet_A/MI_Suburbs_Trim_Sheet_A', '/Game/Environments/Materials/MI_Suburbs_Non_Destructible']
_folder = "Reconstruction/BD_BB_OrcTown_Gate/Meshes"
a = spawn_static_mesh(_mesh_path, _materials, (3650.0, 3700.0002, 1100.0), (0.0, -179.99978826413437, 0.0), (1.0, 1.0, 1.0), "NonD_Stairs_Trim_A_L9", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2000.0, 2500.0, 1100.0), (0.0, -89.99999818714215, 0.0), (1.0, 1.0, 1.0), "NonD_Stairs_Trim_A_R2_201", _folder)
if a: placed += 1
else: skipped += 1

# Batch 10: StaticMesh'NonDest_Boundry_3m_Trim_A' (2 instances)
_mesh_path = "/Game/Art/Assets/Kits/Architecture/Non_D/NonDest_Boundry_3m_Trim_A"
_materials = ['/Game/Art/Assets/Kits/Architecture/Suburbs/Materials/Suburbs_Trim_Sheet_A/MI_Suburbs_Trim_Sheet_A']
_folder = "Reconstruction/BD_BB_OrcTown_Gate/Meshes"
a = spawn_static_mesh(_mesh_path, _materials, (3540.0002, 6385.0, 800.0), (0.0, 179.99980192457332, -0.0), (1.0, 0.5, 1.0), "Suburbs_Floor_3x9m_B17", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3240.0002, 6385.0, 800.0), (0.0, 179.99980192457332, -0.0), (1.0, 0.5, 1.0), "Suburbs_Floor_3x9m_B18", _folder)
if a: placed += 1
else: skipped += 1

# Batch 11: StaticMesh'NonDest_Boundry_Trim_A' (41 instances)
_mesh_path = "/Game/Art/Assets/Kits/Architecture/Non_D/NonDest_Boundry_Trim_A"
_materials = ['/Game/Art/Assets/Kits/Architecture/Suburbs/Materials/Suburbs_Trim_Sheet_A/MI_Suburbs_Trim_Sheet_A', '/Game/Environments/Materials/MI_Suburbs_Non_Destructible']
_folder = "Reconstruction/BD_BB_OrcTown_Gate/Meshes"
a = spawn_static_mesh(_mesh_path, _materials, (4105.2085, 1910.2534, 2487.3718), (1.366037020878057e-05, 90.00023965226737, 9.460840862767858e-05), (0.375, 0.375, 0.375), "NonDest_Boundry_Trim_A_75", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4105.2075, 3590.2568, 2487.3718), (1.366037020878057e-05, 90.00023965226737, 9.460840862767858e-05), (0.375, 0.375, 0.375), "NonDest_Boundry_Trim_A10", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2337.2432, 1768.4827, 2487.3623), (-6.103514811332609e-05, -89.99959790732373, 0.00012159028939938925), (0.375, 0.375, 0.375), "NonDest_Boundry_Trim_A11_295", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3415.2092, 1940.2534, 2931.3718), (1.4000000234780479e-05, 90.00023965226806, 9.50000118245437e-05), (0.375, 0.375, 0.375), "NonDest_Boundry_Trim_A12_317", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3415.21, 1380.2534, 2931.3718), (1.4000000234780479e-05, 90.00023965226806, 9.50000118245437e-05), (0.375, 0.375, 0.375), "NonDest_Boundry_Trim_A13_319", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3415.2083, 3060.2534, 2931.3718), (1.4000000234780479e-05, 90.00023965226806, 9.50000118245437e-05), (0.375, 0.375, 0.375), "NonDest_Boundry_Trim_A14_321", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3415.2075, 3620.2534, 2931.3718), (1.4000000234780479e-05, 90.00023965226806, 9.50000118245437e-05), (0.375, 0.375, 0.375), "NonDest_Boundry_Trim_A15_323", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3035.2776, 2500.2412, 2931.3682), (0.00010971956611547654, -89.99820423156388, -0.00024414063301231206), (0.375, 0.375, 0.375), "NonDest_Boundry_Trim_A16_329", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3035.278, 3060.2412, 2931.369), (0.00010971956611547654, -89.99820423156388, -0.00024414063301231206), (0.375, 0.375, 0.375), "NonDest_Boundry_Trim_A17_330", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3035.2795, 3620.2432, 2931.3699), (0.00010971956611547654, -89.99820423156388, -0.00024414063301231206), (0.375, 0.375, 0.375), "NonDest_Boundry_Trim_A18_331", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3035.2776, 1940.2402, 2931.3723), (0.00010971956611547654, -89.99820423156388, -0.00024414063301231206), (0.375, 0.375, 0.375), "NonDest_Boundry_Trim_A19_332", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4105.209, 2470.2537, 2487.3718), (1.366037020878057e-05, 90.00023965226737, 9.460840862767858e-05), (0.375, 0.375, 0.375), "NonDest_Boundry_Trim_A2", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3035.2773, 1380.2412, 2931.3713), (0.00010971956611547654, -89.99820423156388, -0.00024414063301231206), (0.375, 0.375, 0.375), "NonDest_Boundry_Trim_A20_333", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4105.209, 790.2534, 2487.3718), (1.4000000234780479e-05, 90.00023965226806, 9.50000118245437e-05), (0.375, 0.375, 0.375), "NonDest_Boundry_Trim_A21_353", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3415.213, 821.2135, 2914.335), (3.2248776003497883, 90.00028029722839, 9.717900558624844e-05), (0.375, 0.375, 0.375), "NonDest_Boundry_Trim_A22_359", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2337.2485, 1208.4827, 2487.3623), (-6.103515682544351e-05, -89.99959790732439, 0.00012199999443662468), (0.375, 0.375, 0.375), "NonDest_Boundry_Trim_A23", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2337.2512, 648.48267, 2487.3623), (-6.103515682544351e-05, -89.99959790732439, 0.00012199999443662468), (0.375, 0.375, 0.375), "NonDest_Boundry_Trim_A24", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4105.2075, 4150.257, 2487.3718), (1.4000000234780479e-05, 90.00023965226806, 9.50000118245437e-05), (0.375, 0.375, 0.375), "NonDest_Boundry_Trim_A25", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3035.2795, 4180.243, 2931.3699), (0.00010999998134358987, -89.99820423156473, -0.00024414062050757347), (0.375, 0.375, 0.375), "NonDest_Boundry_Trim_A26", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3415.2075, 4180.2534, 2931.3718), (1.4000000234780479e-05, 90.00023965226806, 9.50000118245437e-05), (0.375, 0.375, 0.375), "NonDest_Boundry_Trim_A27", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2337.256, 88.482666, 2487.3623), (-6.103515682544351e-05, -89.99959790732439, 0.00012199999443662468), (0.375, 0.375, 0.375), "NonDest_Boundry_Trim_A28", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3035.2961, 820.4058, 2924.4844), (-1.3694459020233387, -89.99816769657266, -0.00024419903454836933), (0.375, 0.375, 0.375), "NonDest_Boundry_Trim_A29", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2337.239, 3448.484, 2487.3713), (-6.103514811332609e-05, -89.99959790732373, 0.00012159028939938925), (0.375, 0.375, 0.375), "NonDest_Boundry_Trim_A3_280", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3825.209, 2510.2537, 2487.3718), (1.3999997805389169e-05, -179.9998155848601, 9.500004035679873e-05), (0.375, 0.375, 0.375), "NonDest_Boundry_Trim_A30", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3805.209, 2690.2537, 2487.3718), (1.3999999525483329e-05, 9.489058873447908e-05, 9.500000074167012e-05), (0.375, 0.375, 0.375), "NonDest_Boundry_Trim_A31", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2585.209, 2510.2537, 2487.3718), (1.3999997805462933e-05, -179.9998155848601, 9.499999452017788e-05), (0.375, 0.375, 0.375), "NonDest_Boundry_Trim_A34", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2595.209, 2670.2537, 2487.3718), (1.3999999434777338e-05, 9.50000007550374e-05, 9.50000007550374e-05), (0.375, 0.375, 0.375), "NonDest_Boundry_Trim_A35", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2025.209, 2450.2537, 2487.3718), (1.3999997805462933e-05, -179.9998155848601, 9.499999452017788e-05), (0.375, 0.375, 0.375), "NonDest_Boundry_Trim_A36", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2025.209, 2710.2537, 2487.3718), (1.3999999434777338e-05, 9.50000007550374e-05, 9.50000007550374e-05), (0.375, 0.375, 0.375), "NonDest_Boundry_Trim_A37", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3885.209, 4260.254, 2487.3718), (1.4000003617490693e-05, -179.99980192457318, 9.500002284830537e-05), (0.375, 0.375, 0.375), "NonDest_Boundry_Trim_A38", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3825.209, 4520.254, 2467.3718), (1.3999999760701686e-05, 0.00010013579962495116, 9.500000138250109e-05), (0.375, 0.375, 0.375), "NonDest_Boundry_Trim_A39", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4105.2085, 1350.2534, 2487.3718), (1.4000000234780479e-05, 90.00023965226806, 9.50000118245437e-05), (0.375, 0.375, 0.375), "NonDest_Boundry_Trim_A4_351", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2515.209, 4260.254, 2487.3718), (1.4000003617490693e-05, -179.99980192457318, 9.500002284830537e-05), (0.375, 0.375, 0.375), "NonDest_Boundry_Trim_A42", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2515.209, 4520.254, 2467.3718), (1.3999999760701686e-05, 0.00010013579962495116, 9.500000138250109e-05), (0.375, 0.375, 0.375), "NonDest_Boundry_Trim_A43", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2145.209, 4520.254, 2467.3718), (1.3999999760701686e-05, 0.00010013579962495116, 9.500000138250109e-05), (0.375, 0.375, 0.375), "NonDest_Boundry_Trim_A45", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4105.2144, 240.25342, 2487.374), (1.4000000234780479e-05, 90.00023965226806, 9.50000118245437e-05), (0.375, 0.375, 0.375), "NonDest_Boundry_Trim_A46", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2337.2393, 2888.484, 2487.3696), (-6.103514811332609e-05, -89.99959790732373, 0.00012159028939938925), (0.375, 0.375, 0.375), "NonDest_Boundry_Trim_A5_284", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2337.229, 4013.484, 2487.3777), (-6.103514811332609e-05, -89.99959790732373, 0.00012159028939938925), (0.375, 0.375, 0.375), "NonDest_Boundry_Trim_A6_296", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4105.2075, 3030.2542, 2487.3718), (1.366037020878057e-05, 90.00023965226737, 9.460840862767858e-05), (0.375, 0.375, 0.375), "NonDest_Boundry_Trim_A7", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2337.2422, 2328.4854, 2487.3677), (-6.103514811332609e-05, -89.99959790732373, 0.00012159028939938925), (0.375, 0.375, 0.375), "NonDest_Boundry_Trim_A8_289", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3415.209, 2500.2534, 2931.3718), (1.4000000234780479e-05, 90.00023965226806, 9.50000118245437e-05), (0.375, 0.375, 0.375), "NonDest_Boundry_Trim_A9_315", _folder)
if a: placed += 1
else: skipped += 1

# Batch 12: StaticMesh'NonDest_Floor_Trim_6M' (5 instances)
_mesh_path = "/Game/Art/Assets/Kits/Architecture/Non_D/NonDest_Floor_Trim_6M"
_materials = ['/Game/Art/Assets/Kits/Architecture/Suburbs/Materials/Suburbs_Trim_Sheet_A/MI_Suburbs_Trim_Sheet_A']
_folder = "Reconstruction/BD_BB_OrcTown_Gate/Meshes"
a = spawn_static_mesh(_mesh_path, _materials, (3500.0, 2200.0, 1100.0), (0.0, -179.9998360754275, 0.0), (1.0, 1.0, 1.0), "NonDest_Floor_Trim_6M2", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2900.0, 2200.0, 1100.0), (0.0, -179.9998360754275, 0.0), (1.0, 1.0, 1.0), "NonDest_Floor_Trim_6M3", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2300.0, 2200.0, 1100.0), (0.0, -179.9998360754275, 0.0), (1.0, 1.0, 1.0), "NonDest_Floor_Trim_6M4", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1850.0, 2350.0, 1100.0), (0.0, -179.9998360754275, 0.0), (1.0, 1.0, 1.0), "NonDest_Floor_Trim_6M5", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4100.0, 2200.0, 1100.0), (0.0, -179.9998360754275, 0.0), (1.0, 1.0, 1.0), "NonDest_Floor_Trim_6M6_343", _folder)
if a: placed += 1
else: skipped += 1

# Batch 13: StaticMesh'NonDest_Floor_Trim_Cap_C' (7 instances)
_mesh_path = "/Game/Art/Assets/Kits/Architecture/Non_D/NonDest_Floor_Trim_Cap_C"
_materials = ['/Game/Art/Assets/Kits/Architecture/Suburbs/Materials/Suburbs_Trim_Sheet_A/MI_Suburbs_Trim_Sheet_A']
_folder = "Reconstruction/BD_BB_OrcTown_Gate/Meshes"
a = spawn_static_mesh(_mesh_path, _materials, (5350.0, 1600.0, 1000.0), (0.0, -89.99999818714215, 0.0), (1.0, 1.0, 1.0), "NonDest_Floor_Trim_Cap_C2", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4400.0, 2150.0, 1100.0), (0.0, -179.99998633961752, -0.0), (1.0, 1.0, 1.0), "NonDest_Floor_Trim_Cap_C3_207", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3600.0, 2150.0, 1100.0), (0.0, -179.99998633961752, -0.0), (1.0, 1.0, 1.0), "NonDest_Floor_Trim_Cap_C4", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2800.0, 2150.0, 1100.0), (0.0, -179.99998633961752, -0.0), (1.0, 1.0, 1.0), "NonDest_Floor_Trim_Cap_C5", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2000.0, 2150.0, 1100.0), (0.0, -179.99998633961752, -0.0), (1.0, 1.0, 1.0), "NonDest_Floor_Trim_Cap_C6", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2750.0, 2150.0, 1100.0), (0.0, -179.99998633961752, -0.0), (1.0, 1.0, 1.0), "NonDest_Floor_Trim_Cap_C7", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3650.0, 2150.0, 1100.0), (0.0, -179.99998633961752, -0.0), (1.0, 1.0, 1.0), "NonDest_Floor_Trim_Cap_C8", _folder)
if a: placed += 1
else: skipped += 1

# Batch 14: StaticMesh'NonDest_Floor_Trim_Corner_M' (2 instances)
_mesh_path = "/Game/Art/Assets/Kits/Architecture/Non_D/NonDest_Floor_Trim_Corner_M"
_materials = ['/Game/Art/Assets/Kits/Architecture/Suburbs/Materials/Suburbs_Trim_Sheet_A/MI_Suburbs_Trim_Sheet_A']
_folder = "Reconstruction/BD_BB_OrcTown_Gate/Meshes"
a = spawn_static_mesh(_mesh_path, _materials, (5300.0, 578.6739, 997.571), (0.0, -90.0001164887758, 0.0), (1.0, 1.0, 1.0), "NonDest_Floor_Trim_Corner_M_53", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2150.0, 700.0, 1097.1555), (0.0, 90.00011648875932, -0.0), (1.0, 1.0, 1.0), "NonDest_Floor_Trim_Corner_M4", _folder)
if a: placed += 1
else: skipped += 1

# Batch 15: StaticMesh'NonDest_Floor_Trim_Thin_1_5M_A' (5 instances)
_mesh_path = "/Game/Art/Assets/Kits/Architecture/Non_D/NonDest_Floor_Trim_Thin_1_5M_A"
_materials = ['/Game/Art/Assets/Kits/Architecture/Suburbs/Materials/Suburbs_Trim_Sheet_A/MI_Suburbs_Trim_Sheet_A']
_folder = "Reconstruction/BD_BB_OrcTown_Gate/Meshes"
a = spawn_static_mesh(_mesh_path, _materials, (2150.3223, 250.0, 1100.0), (0.0, 90.00011648875932, -0.0), (1.0, 1.0, 1.0), "NonDest_Floor_Trim_Thin_1_5M_A_169", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1550.0, 99.48455, 1100.0), (0.0, -3.051757709276941e-05, 0.0), (1.0, 1.0, 1.0), "NonDest_Floor_Trim_Thin_1_5M_A2", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1700.0, 99.48455, 1100.0), (0.0, -3.051757709276941e-05, 0.0), (1.0, 1.0, 1.0), "NonDest_Floor_Trim_Thin_1_5M_A3", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1850.0, 99.48455, 1100.0), (0.0, -3.051757709276941e-05, 0.0), (1.0, 1.0, 1.0), "NonDest_Floor_Trim_Thin_1_5M_A4", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4750.2056, 698.71515, 1097.1729), (0.0, 0.0, -0.0), (1.0, 1.0, 1.0), "NonDest_Floor_Trim_Thin_3M_A91", _folder)
if a: placed += 1
else: skipped += 1

# Batch 16: StaticMesh'NonDest_Floor_Trim_Thin_1M_A' (1 instances)
_mesh_path = "/Game/Art/Assets/Kits/Architecture/Non_D/NonDest_Floor_Trim_Thin_1M_A"
_materials = ['/Game/Art/Assets/Kits/Architecture/Suburbs/Materials/Suburbs_Trim_Sheet_A/MI_Suburbs_Trim_Sheet_A']
_folder = "Reconstruction/BD_BB_OrcTown_Gate/Meshes"
a = spawn_static_mesh(_mesh_path, _materials, (4900.2056, 698.71515, 1097.1729), (0.0, 0.0, -0.0), (1.0, 1.0, 1.0), "NonDest_Floor_Trim_Thin_3M_A108", _folder)
if a: placed += 1
else: skipped += 1

# Batch 17: StaticMesh'NonDest_Floor_Trim_Thin_2M_A' (2 instances)
_mesh_path = "/Game/Art/Assets/Kits/Architecture/Non_D/NonDest_Floor_Trim_Thin_2M_A"
_materials = ['/Game/Art/Assets/Kits/Architecture/Suburbs/Materials/Suburbs_Trim_Sheet_A/MI_Suburbs_Trim_Sheet_A']
_folder = "Reconstruction/BD_BB_OrcTown_Gate/Meshes"
a = spawn_static_mesh(_mesh_path, _materials, (4550.2056, 698.71515, 1097.1729), (0.0, 0.0, -0.0), (1.0, 1.0, 1.0), "NonDest_Floor_Trim_Thin_3M_A90", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5300.251, 578.7241, 997.17285), (0.0, -179.99994535848643, 0.0), (1.0, 1.0, 1.0), "NonDest_Floor_Trim_Thin_3M_A94_55", _folder)
if a: placed += 1
else: skipped += 1

# Batch 18: StaticMesh'NonDest_Floor_Trim_Thin_3M_A' (80 instances)
_mesh_path = "/Game/Art/Assets/Kits/Architecture/Non_D/NonDest_Floor_Trim_Thin_3M_A"
_materials = ['/Game/Art/Assets/Kits/Architecture/Suburbs/Materials/Suburbs_Trim_Sheet_A/MI_Suburbs_Trim_Sheet_A']
_folder = "Reconstruction/BD_BB_OrcTown_Gate/Meshes"
a = spawn_static_mesh(_mesh_path, _materials, (3900.251, 578.71954, 997.17285), (0.0, -179.99994535848643, 0.0), (1.0, 1.0, 1.0), "NonDest_Floor_Trim_Thin_3M_A100", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2400.2495, 578.7129, 997.17285), (0.0, -179.99994535848643, 0.0), (1.0, 1.0, 1.0), "NonDest_Floor_Trim_Thin_3M_A101", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2700.2495, 578.71375, 997.17285), (0.0, -179.99994535848643, 0.0), (1.0, 1.0, 1.0), "NonDest_Floor_Trim_Thin_3M_A102", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3000.25, 578.71515, 997.17285), (0.0, -179.99994535848643, 0.0), (1.0, 1.0, 1.0), "NonDest_Floor_Trim_Thin_3M_A103", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5300.251, 878.7241, 997.17285), (0.0, -89.99968865881478, 0.0), (1.0, 1.0, 1.0), "NonDest_Floor_Trim_Thin_3M_A104", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5300.251, 1178.7241, 997.17285), (0.0, -89.99968865881478, 0.0), (1.0, 1.0, 1.0), "NonDest_Floor_Trim_Thin_3M_A105", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5300.251, 1478.7241, 997.17285), (0.0, -89.99968865881478, 0.0), (1.0, 1.0, 1.0), "NonDest_Floor_Trim_Thin_3M_A106", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5300.251, 1778.7241, 997.17285), (0.0, -89.99968865881478, 0.0), (1.0, 1.0, 1.0), "NonDest_Floor_Trim_Thin_3M_A107", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5150.2056, 848.71515, 1097.1729), (0.0, 90.00002735739477, -0.0), (1.0, 1.0, 1.0), "NonDest_Floor_Trim_Thin_3M_A109", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5150.2056, 1148.7151, 1097.1729), (0.0, 90.00002735739477, -0.0), (1.0, 1.0, 1.0), "NonDest_Floor_Trim_Thin_3M_A110", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5150.2056, 1448.7151, 1097.1729), (0.0, 90.00002735739477, -0.0), (1.0, 1.0, 1.0), "NonDest_Floor_Trim_Thin_3M_A111", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2700.6396, 3848.917, 1397.4673), (0.0, 89.99999818714215, -0.0), (1.0, 1.0, 1.0), "NonDest_Floor_Trim_Thin_3M_A112", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2250.6396, 3698.917, 1397.4673), (0.0, -0.0001525878854640202, 0.0), (1.0, 1.0, 1.0), "NonDest_Floor_Trim_Thin_3M_A113", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1950.6396, 3698.917, 1397.4673), (0.0, -0.0001525878854640202, 0.0), (1.0, 1.0, 1.0), "NonDest_Floor_Trim_Thin_3M_A114", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2700.6396, 4148.917, 1397.4673), (0.0, 89.99999818714215, -0.0), (1.0, 1.0, 1.0), "NonDest_Floor_Trim_Thin_3M_A115", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3849.6394, 3699.918, 1397.4673), (0.0, -0.0001525878854640202, 0.0), (1.0, 1.0, 1.0), "NonDest_Floor_Trim_Thin_3M_A116", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3699.6409, 4149.918, 1397.4673), (0.0, -90.00023965222978, 0.0), (1.0, 1.0, 1.0), "NonDest_Floor_Trim_Thin_3M_A118", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3699.641, 4449.9175, 1397.4673), (0.0, -90.00023965222978, 0.0), (1.0, 1.0, 1.0), "NonDest_Floor_Trim_Thin_3M_A119", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4149.6396, 3699.917, 1397.4673), (0.0, -0.0001525878854640202, 0.0), (1.0, 1.0, 1.0), "NonDest_Floor_Trim_Thin_3M_A120", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2450.2056, 698.71515, 1097.1729), (0.0, -6.103515418554748e-05, 0.0), (1.0, 1.0, 1.0), "NonDest_Floor_Trim_Thin_3M_A15", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2150.2498, 698.71515, 1097.1729), (0.0, -6.103515418554748e-05, 0.0), (1.0, 1.0, 1.0), "NonDest_Floor_Trim_Thin_3M_A16", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2150.2498, 398.71515, 1097.1729), (0.0, 90.00004680423052, -0.0), (1.0, 1.0, 1.0), "NonDest_Floor_Trim_Thin_3M_A18", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4400.0, 2348.917, 1197.1729), (0.0, 0.0, -0.0), (1.0, 1.0, 1.0), "NonDest_Floor_Trim_Thin_3M_A19_270", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3950.0, 2498.917, 1297.1729), (0.0, 0.0, -0.0), (1.0, 1.0, 1.0), "NonDest_Floor_Trim_Thin_3M_A20_272", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1250.2498, 98.71515, 1097.1729), (0.0, -6.103515418554748e-05, 0.0), (1.0, 1.0, 1.0), "NonDest_Floor_Trim_Thin_3M_A21", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (950.24976, 98.71515, 1097.1729), (0.0, -6.103515418554748e-05, 0.0), (1.0, 1.0, 1.0), "NonDest_Floor_Trim_Thin_3M_A22", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (650.24976, 98.71515, 1097.1729), (0.0, -6.103515418554748e-05, 0.0), (1.0, 1.0, 1.0), "NonDest_Floor_Trim_Thin_3M_A23", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3650.0, 2498.917, 1297.1729), (0.0, 0.0, -0.0), (1.0, 1.0, 1.0), "NonDest_Floor_Trim_Thin_3M_A24", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3500.0, 2348.917, 1197.1729), (0.0, 0.0, -0.0), (1.0, 1.0, 1.0), "NonDest_Floor_Trim_Thin_3M_A25", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3200.0, 2348.917, 1197.1729), (0.0, 0.0, -0.0), (1.0, 1.0, 1.0), "NonDest_Floor_Trim_Thin_3M_A26", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2900.0, 2348.917, 1197.1729), (0.0, 0.0, -0.0), (1.0, 1.0, 1.0), "NonDest_Floor_Trim_Thin_3M_A27", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2600.0, 2348.917, 1197.1729), (0.0, 0.0, -0.0), (1.0, 1.0, 1.0), "NonDest_Floor_Trim_Thin_3M_A28", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2450.0, 2498.917, 1297.1729), (0.0, 0.0, -0.0), (1.0, 1.0, 1.0), "NonDest_Floor_Trim_Thin_3M_A29", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2150.0, 2498.917, 1297.1729), (0.0, 0.0, -0.0), (1.0, 1.0, 1.0), "NonDest_Floor_Trim_Thin_3M_A30", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1850.0, 2498.917, 1297.1729), (0.0, 0.0, -0.0), (1.0, 1.0, 1.0), "NonDest_Floor_Trim_Thin_3M_A31", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3050.0, 5050.4116, 1197.1729), (0.0, 179.99976777351753, -0.0), (1.0, 1.0, 1.0), "NonDest_Floor_Trim_Thin_3M_A48", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3350.0, 5050.4116, 1197.1729), (0.0, 179.99976777351753, -0.0), (1.0, 1.0, 1.0), "NonDest_Floor_Trim_Thin_3M_A49", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3650.0, 5050.4116, 1197.1729), (0.0, 179.99976777351753, -0.0), (1.0, 1.0, 1.0), "NonDest_Floor_Trim_Thin_3M_A50", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3050.0, 5650.4116, 997.17285), (0.0, 179.99976777351753, -0.0), (1.0, 1.0, 1.0), "NonDest_Floor_Trim_Thin_3M_A51", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3350.0, 5650.4116, 997.17285), (0.0, 179.99976777351753, -0.0), (1.0, 1.0, 1.0), "NonDest_Floor_Trim_Thin_3M_A52", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3650.0, 5650.4116, 997.17285), (0.0, 179.99976777351753, -0.0), (1.0, 1.0, 1.0), "NonDest_Floor_Trim_Thin_3M_A53", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2400.2498, 348.71515, 997.17285), (0.0, -6.103515418554748e-05, 0.0), (1.0, 1.0, 1.0), "NonDest_Floor_Trim_Thin_3M_A54", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2100.2498, 348.71515, 997.17285), (0.0, -6.103515418554748e-05, 0.0), (1.0, 1.0, 1.0), "NonDest_Floor_Trim_Thin_3M_A55", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1800.2498, 348.71515, 997.17285), (0.0, -6.103515418554748e-05, 0.0), (1.0, 1.0, 1.0), "NonDest_Floor_Trim_Thin_3M_A56", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3300.2498, 348.71515, 997.17285), (0.0, -6.103515418554748e-05, 0.0), (1.0, 1.0, 1.0), "NonDest_Floor_Trim_Thin_3M_A57", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3000.2498, 348.71515, 997.17285), (0.0, -6.103515418554748e-05, 0.0), (1.0, 1.0, 1.0), "NonDest_Floor_Trim_Thin_3M_A58", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2700.2498, 348.71515, 997.17285), (0.0, -6.103515418554748e-05, 0.0), (1.0, 1.0, 1.0), "NonDest_Floor_Trim_Thin_3M_A59", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5150.0, 1598.9171, 1097.1729), (0.0, 90.00009542133918, -0.0), (1.0, 1.0, 1.0), "NonDest_Floor_Trim_Thin_3M_A6", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4200.25, 348.71515, 997.17285), (0.0, -6.103515418554748e-05, 0.0), (1.0, 1.0, 1.0), "NonDest_Floor_Trim_Thin_3M_A60", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3900.2498, 348.71515, 997.17285), (0.0, -6.103515418554748e-05, 0.0), (1.0, 1.0, 1.0), "NonDest_Floor_Trim_Thin_3M_A61", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3600.2498, 348.71515, 997.17285), (0.0, -6.103515418554748e-05, 0.0), (1.0, 1.0, 1.0), "NonDest_Floor_Trim_Thin_3M_A62", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5100.25, 348.71515, 997.17285), (0.0, -6.103515418554748e-05, 0.0), (1.0, 1.0, 1.0), "NonDest_Floor_Trim_Thin_3M_A63", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4800.25, 348.71515, 997.17285), (0.0, -6.103515418554748e-05, 0.0), (1.0, 1.0, 1.0), "NonDest_Floor_Trim_Thin_3M_A64", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4500.25, 348.71515, 997.17285), (0.0, -6.103515418554748e-05, 0.0), (1.0, 1.0, 1.0), "NonDest_Floor_Trim_Thin_3M_A65", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5400.25, 348.71515, 997.17285), (0.0, -6.103515418554748e-05, 0.0), (1.0, 1.0, 1.0), "NonDest_Floor_Trim_Thin_3M_A66", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2750.0, 2498.917, 1297.1729), (0.0, 89.99999818714215, -0.0), (1.0, 1.0, 1.0), "NonDest_Floor_Trim_Thin_3M_A67", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2750.0, 2798.917, 1297.1729), (0.0, 89.99999818714215, -0.0), (1.0, 1.0, 1.0), "NonDest_Floor_Trim_Thin_3M_A72", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2750.0, 3098.917, 1297.1729), (0.0, 89.99999818714215, -0.0), (1.0, 1.0, 1.0), "NonDest_Floor_Trim_Thin_3M_A73", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2750.0, 3398.917, 1297.1729), (0.0, 89.99999818714215, -0.0), (1.0, 1.0, 1.0), "NonDest_Floor_Trim_Thin_3M_A74", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2750.0, 3698.917, 1297.1729), (0.0, 89.99999818714215, -0.0), (1.0, 1.0, 1.0), "NonDest_Floor_Trim_Thin_3M_A75", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2750.0, 3998.917, 1297.1729), (0.0, 89.99999818714215, -0.0), (1.0, 1.0, 1.0), "NonDest_Floor_Trim_Thin_3M_A76", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3650.001, 4298.9175, 1297.1729), (0.0, -90.00009542133918, 0.0), (1.0, 1.0, 1.0), "NonDest_Floor_Trim_Thin_3M_A77", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3650.0005, 3998.9177, 1297.1729), (0.0, -90.00009542133918, 0.0), (1.0, 1.0, 1.0), "NonDest_Floor_Trim_Thin_3M_A78", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3650.0, 3698.917, 1297.1729), (0.0, -90.00009542133918, 0.0), (1.0, 1.0, 1.0), "NonDest_Floor_Trim_Thin_3M_A79", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3649.9995, 3398.9163, 1297.1729), (0.0, -90.00009542133918, 0.0), (1.0, 1.0, 1.0), "NonDest_Floor_Trim_Thin_3M_A80", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3649.999, 3098.9165, 1297.1729), (0.0, -90.00009542133918, 0.0), (1.0, 1.0, 1.0), "NonDest_Floor_Trim_Thin_3M_A81", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3649.9985, 2798.916, 1297.1729), (0.0, -90.00009542133918, 0.0), (1.0, 1.0, 1.0), "NonDest_Floor_Trim_Thin_3M_A82", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4250.0, 2498.917, 1297.1729), (0.0, 0.0, -0.0), (1.0, 1.0, 1.0), "NonDest_Floor_Trim_Thin_3M_A83", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3350.2056, 698.71515, 1097.1729), (0.0, -6.103515418554748e-05, 0.0), (1.0, 1.0, 1.0), "NonDest_Floor_Trim_Thin_3M_A84", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3050.2498, 698.71515, 1097.1729), (0.0, -6.103515418554748e-05, 0.0), (1.0, 1.0, 1.0), "NonDest_Floor_Trim_Thin_3M_A85", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2750.2498, 698.71515, 1097.1729), (0.0, -6.103515418554748e-05, 0.0), (1.0, 1.0, 1.0), "NonDest_Floor_Trim_Thin_3M_A86", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4250.2056, 698.71515, 1097.1729), (0.0, -6.103515418554748e-05, 0.0), (1.0, 1.0, 1.0), "NonDest_Floor_Trim_Thin_3M_A87", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3950.2498, 698.71515, 1097.1729), (0.0, -6.103515418554748e-05, 0.0), (1.0, 1.0, 1.0), "NonDest_Floor_Trim_Thin_3M_A88", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3650.2498, 698.71515, 1097.1729), (0.0, -6.103515418554748e-05, 0.0), (1.0, 1.0, 1.0), "NonDest_Floor_Trim_Thin_3M_A89", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5100.251, 578.7241, 997.17285), (0.0, -179.99994535848643, 0.0), (1.0, 1.0, 1.0), "NonDest_Floor_Trim_Thin_3M_A93", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4200.2515, 578.72046, 997.17285), (0.0, -179.99994535848643, 0.0), (1.0, 1.0, 1.0), "NonDest_Floor_Trim_Thin_3M_A95", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4500.25, 578.7212, 997.17285), (0.0, -179.99994535848643, 0.0), (1.0, 1.0, 1.0), "NonDest_Floor_Trim_Thin_3M_A96", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4800.2505, 578.7232, 997.17285), (0.0, -179.99994535848643, 0.0), (1.0, 1.0, 1.0), "NonDest_Floor_Trim_Thin_3M_A97", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3300.2505, 578.71655, 997.17285), (0.0, -179.99994535848643, 0.0), (1.0, 1.0, 1.0), "NonDest_Floor_Trim_Thin_3M_A98", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3600.2505, 578.7171, 997.17285), (0.0, -179.99994535848643, 0.0), (1.0, 1.0, 1.0), "NonDest_Floor_Trim_Thin_3M_A99", _folder)
if a: placed += 1
else: skipped += 1

# Batch 19: StaticMesh'NonDest_Floor_Trim_Thin_Corner_A' (4 instances)
_mesh_path = "/Game/Art/Assets/Kits/Architecture/Non_D/NonDest_Floor_Trim_Thin_Corner_A"
_materials = ['/Game/Art/Assets/Kits/Architecture/Suburbs/Materials/Suburbs_Trim_Sheet_A/MI_Suburbs_Trim_Sheet_A']
_folder = "Reconstruction/BD_BB_OrcTown_Gate/Meshes"
a = spawn_static_mesh(_mesh_path, _materials, (3699.6396, 3849.918, 1397.4673), (0.0, -90.00022020536449, 0.0), (1.0, 1.0, 1.0), "NonDest_Floor_Trim_Thin_3M_A117", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2550.6396, 3698.917, 1397.4673), (0.0, -0.00012207030837116422, 0.0), (1.0, 1.0, 1.0), "NonDest_Floor_Trim_Thin_3M_A92", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2000.3125, 100.0, 1100.0), (0.0, 0.0, -0.0), (1.0, 1.0, 1.0), "NonDest_Floor_Trim_Thin_Corner_A_163", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5000.5156, 698.72156, 1097.5533), (0.0, 0.0, -0.0), (1.0, 1.0, 1.0), "NonDest_Floor_Trim_Thin_Corner_A2_67", _folder)
if a: placed += 1
else: skipped += 1

# Batch 20: StaticMesh'NonDest_Trim_3_5M_A_R' (1 instances)
_mesh_path = "/Game/Art/Assets/Kits/Architecture/Non_D/NonDest_Trim_3_5M_A_R"
_materials = ['/Game/Art/Assets/Kits/Architecture/Suburbs/Materials/Suburbs_Trim_Sheet_A/MI_Suburbs_Trim_Sheet_A', '/Game/Environments/Materials/MI_Suburbs_Non_Destructible']
_folder = "Reconstruction/BD_BB_OrcTown_Gate/Meshes"
a = spawn_static_mesh(_mesh_path, _materials, (2150.0, 400.0, 850.0), (0.0, -90.0001164887758, 0.0), (1.0, 1.0, 1.0), "NonDest_Trim_3_5M_A_R_108", _folder)
if a: placed += 1
else: skipped += 1

# Batch 21: StaticMesh'NonDest_Trim_3M_A_L' (1 instances)
_mesh_path = "/Game/Art/Assets/Kits/Architecture/Non_D/NonDest_Trim_3M_A_L"
_materials = ['/Game/Environments/Materials/MI_Suburbs_Non_Destructible', '/Game/Art/Assets/Kits/Architecture/Suburbs/Materials/Suburbs_Trim_Sheet_A/MI_Suburbs_Trim_Sheet_A']
_folder = "Reconstruction/BD_BB_OrcTown_Gate/Meshes"
a = spawn_static_mesh(_mesh_path, _materials, (5150.0, 1600.0, 1000.0), (0.0, -89.99959790717821, 0.0), (1.0, 1.0, 1.0), "NonDest_Trim_3M_A_L3", _folder)
if a: placed += 1
else: skipped += 1

# Batch 22: StaticMesh'NonDest_Trim_3M_B' (18 instances)
_mesh_path = "/Game/Art/Assets/Kits/Architecture/Non_D/NonDest_Trim_3M_B"
_materials = ['/Game/Environments/Materials/MI_Suburbs_Non_Destructible', '/Game/Art/Assets/Kits/Architecture/Suburbs/Materials/Suburbs_Trim_Sheet_A/MI_Suburbs_Trim_Sheet_A']
_folder = "Reconstruction/BD_BB_OrcTown_Gate/Meshes"
a = spawn_static_mesh(_mesh_path, _materials, (2751.629, 3847.0786, 1200.0), (0.0, 89.99999818714215, -0.0), (1.0, 1.0, 1.0), "NonDest_Trim_3M_B16", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2751.629, 4147.0786, 1200.0), (0.0, 89.99999818714215, -0.0), (1.0, 1.0, 1.0), "NonDest_Trim_3M_B17", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3648.3718, 4150.757, 1200.0), (0.0, -90.00009542133918, 0.0), (1.0, 1.0, 1.0), "NonDest_Trim_3M_B18", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3648.3704, 3850.755, 1200.0), (0.0, -90.00009542133918, 0.0), (1.0, 1.0, 1.0), "NonDest_Trim_3M_B19", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3648.3704, 3550.7551, 1200.0), (0.0, -90.00009542133918, 0.0), (1.0, 1.0, 1.0), "NonDest_Trim_3M_B20", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3648.3704, 3250.7544, 1200.0), (0.0, -90.00009542133918, 0.0), (1.0, 1.0, 1.0), "NonDest_Trim_3M_B21", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3648.3691, 2950.755, 1200.0), (0.0, -90.00009542133918, 0.0), (1.0, 1.0, 1.0), "NonDest_Trim_3M_B22", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3648.3696, 2650.7534, 1200.0), (0.0, -90.00009542133918, 0.0), (1.0, 1.0, 1.0), "NonDest_Trim_3M_B23", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2701.629, 3847.0786, 1300.0), (0.0, 89.99999818714215, -0.0), (1.0, 1.0, 1.0), "NonDest_Trim_3M_B24", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2551.629, 3697.0786, 1300.0), (0.0, -6.103515418554748e-05, 0.0), (1.0, 1.0, 1.0), "NonDest_Trim_3M_B25", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2251.629, 3697.0786, 1300.0), (0.0, -6.103515418554748e-05, 0.0), (1.0, 1.0, 1.0), "NonDest_Trim_3M_B28", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2701.629, 4147.0786, 1300.0), (0.0, 89.99999818714215, -0.0), (1.0, 1.0, 1.0), "NonDest_Trim_3M_B30", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3701.6343, 4147.082, 1300.0), (0.0, -89.99913766804917, 0.0), (1.0, 1.0, 1.0), "NonDest_Trim_3M_B31", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4151.629, 3697.0786, 1300.0), (0.0, -6.103515418554748e-05, 0.0), (1.0, 1.0, 1.0), "NonDest_Trim_3M_B32", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3851.629, 3697.0786, 1300.0), (0.0, -6.103515418554748e-05, 0.0), (1.0, 1.0, 1.0), "NonDest_Trim_3M_B34", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3701.6333, 3847.0798, 1300.0), (0.0, -89.99913766804917, 0.0), (1.0, 1.0, 1.0), "NonDest_Trim_3M_B36", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2151.629, 547.07874, 1000.0), (0.0, 89.99999818714215, -0.0), (1.0, 1.0, 1.0), "NonDest_Trim_3M_B7", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2151.629, 247.07874, 1000.0), (0.0, 89.99999818714215, -0.0), (1.0, 1.0, 1.0), "NonDest_Trim_3M_B8", _folder)
if a: placed += 1
else: skipped += 1

# Batch 23: StaticMesh'NonDest_Wall_3M_B' (5 instances)
_mesh_path = "/Game/Art/Assets/Kits/Architecture/Non_D/NonDest_Wall_3M_B"
_materials = ['/Game/Environments/Materials/MI_Suburbs_Non_Destructible', '/Game/Art/Assets/Kits/Architecture/Suburbs/Materials/Suburbs_Trim_Sheet_A/MI_Suburbs_Trim_Sheet_A']
_folder = "Reconstruction/BD_BB_OrcTown_Gate/Meshes"
a = spawn_static_mesh(_mesh_path, _materials, (1850.0, 100.0, 800.0), (0.0, -179.99998633961752, -0.0), (1.0, 1.0, 1.0), "NonDest_Wall_3M_B_94", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1550.0, 100.0, 800.0), (0.0, -179.99998633961752, -0.0), (1.0, 1.0, 1.0), "NonDest_Wall_3M_B2", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1250.0, 100.0, 800.0), (0.0, -179.99998633961752, -0.0), (1.0, 1.0, 1.0), "NonDest_Wall_3M_B3", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (950.0, 100.0, 800.0), (0.0, -179.99998633961752, -0.0), (1.0, 1.0, 1.0), "NonDest_Wall_3M_B4", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2150.0, 100.0, 800.0), (0.0, -179.99998633961752, -0.0), (1.0, 1.0, 1.0), "NonDest_Wall_3M_B5", _folder)
if a: placed += 1
else: skipped += 1

# Batch 24: StaticMesh'City_Column_Large_A_Base' (2 instances)
_mesh_path = "/Game/Art/Assets/Kits/Architecture/Suburbs/City_Column_Large_A_Base"
_materials = ['/Game/Art/Assets/Kits/Architecture/Suburbs/Materials/SM_AR_City_Column_C/MI_SM_AR_City_Column_C_Base']
_folder = "Reconstruction/BD_BB_OrcTown_Gate/Meshes"
a = spawn_static_mesh(_mesh_path, _materials, (2800.0, 2575.0, 1200.0), (0.0, 0.0, -0.0), (1.25, 1.25, 1.25), "City_Column_Large_A_Base11", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3580.0, 2575.0, 1200.0), (0.0, 0.0, -0.0), (1.25, 1.25, 1.25), "City_Column_Large_A_Base12", _folder)
if a: placed += 1
else: skipped += 1

# Batch 25: StaticMesh'City_Column_Large_A_Capital' (2 instances)
_mesh_path = "/Game/Art/Assets/Kits/Architecture/Suburbs/City_Column_Large_A_Capital"
_materials = ['/Game/Art/Assets/Kits/Architecture/Suburbs/Materials/SM_AR_City_Column_C/MI_SM_AR_City_Column_C_Capital']
_folder = "Reconstruction/BD_BB_OrcTown_Gate/Meshes"
a = spawn_static_mesh(_mesh_path, _materials, (3580.0, 2575.0, 2210.313), (0.0, 0.0, -0.0), (1.25, 1.25, 1.25), "City_Column_Large_A_Base19", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2800.0, 2575.0, 2210.313), (0.0, 0.0, -0.0), (1.25, 1.25, 1.25), "City_Column_Large_A_Base20", _folder)
if a: placed += 1
else: skipped += 1

# Batch 26: StaticMesh'City_Column_Large_A_Shaft' (6 instances)
_mesh_path = "/Game/Art/Assets/Kits/Architecture/Suburbs/City_Column_Large_A_Shaft"
_materials = ['/Game/Art/Assets/Kits/Architecture/Suburbs/Materials/SM_AR_City_Column_C/MI_SM_AR_City_Column_C_Shaft']
_folder = "Reconstruction/BD_BB_OrcTown_Gate/Meshes"
a = spawn_static_mesh(_mesh_path, _materials, (2800.0, 2575.0, 1450.0), (0.0, 0.0, -0.0), (1.25, 1.25, 1.25), "City_Column_Large_A_Base13", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2800.0, 2575.0, 1700.1564), (0.0, 0.0, -0.0), (1.25, 1.25, 1.25), "City_Column_Large_A_Base14", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3580.0, 2575.0, 1450.0), (0.0, 0.0, -0.0), (1.25, 1.25, 1.25), "City_Column_Large_A_Base16", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3580.0, 2575.0, 1700.1564), (0.0, 0.0, -0.0), (1.25, 1.25, 1.25), "City_Column_Large_A_Base17", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3580.0, 2575.0, 1950.3129), (0.0, 0.0, -0.0), (1.25, 1.25, 1.3125), "City_Column_Large_A_Base18", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2800.0, 2575.0, 1950.3129), (0.0, 0.0, -0.0), (1.25, 1.25, 1.3125), "City_Column_Large_A_Base5", _folder)
if a: placed += 1
else: skipped += 1

# Batch 27: StaticMesh'SM_AR_City_Column_100x100x200_A_Base' (4 instances)
_mesh_path = "/Game/Art/Assets/Kits/Architecture/Suburbs/SM_AR_City_Column_100x100x200_A_Base"
_materials = ['/Game/Art/Assets/Kits/Architecture/Suburbs/Destructable/Materials/MI_Suburbs_Wall_Non_Dest']
_folder = "Reconstruction/BD_BB_OrcTown_Gate/Meshes"
a = spawn_static_mesh(_mesh_path, _materials, (2900.0, 2670.0, 2448.75), (0.0, 0.0, -0.0), (1.0, 1.0, 0.65625), "SM_AR_City_Column_100x100x200_A_Base_166", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3500.0, 2670.0, 2448.75), (0.0, 0.0, -0.0), (1.0, 1.0, 0.65625), "SM_AR_City_Column_100x100x200_A_Base2", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2900.0, 2500.0, 2448.75), (0.0, 0.0, -0.0), (1.0, 1.0, 0.65625), "SM_AR_City_Column_100x100x200_A_Base3", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3500.0, 2500.0, 2448.75), (0.0, 0.0, -0.0), (1.0, 1.0, 0.65625), "SM_AR_City_Column_100x100x200_A_Base4", _folder)
if a: placed += 1
else: skipped += 1

# Batch 28: StaticMesh'SM_AR_City_Column_100x100x200_A_Capital' (4 instances)
_mesh_path = "/Game/Art/Assets/Kits/Architecture/Suburbs/SM_AR_City_Column_100x100x200_A_Capital"
_materials = ['/Game/Art/Assets/Kits/Architecture/Suburbs/Destructable/Materials/MI_Suburbs_Wall_Non_Dest']
_folder = "Reconstruction/BD_BB_OrcTown_Gate/Meshes"
a = spawn_static_mesh(_mesh_path, _materials, (2900.0, 2670.0, 2580.0), (0.0, 0.0, -0.0), (1.0, 1.0, 0.65625), "SM_AR_City_Column_100x100x200_A_Capital_169", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3500.0, 2670.0, 2580.0), (0.0, 0.0, -0.0), (1.0, 1.0, 0.65625), "SM_AR_City_Column_100x100x200_A_Capital2", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2900.0, 2500.0, 2580.0), (0.0, 0.0, -0.0), (1.0, 1.0, 0.65625), "SM_AR_City_Column_100x100x200_A_Capital3", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3500.0, 2500.0, 2580.0), (0.0, 0.0, -0.0), (1.0, 1.0, 0.65625), "SM_AR_City_Column_100x100x200_A_Capital4", _folder)
if a: placed += 1
else: skipped += 1

# Batch 29: StaticMesh'Suburb_Stairs_Trim_3M_B' (38 instances)
_mesh_path = "/Game/Art/Assets/Kits/Architecture/Suburbs/Suburb_Stairs_Trim_3M_B"
_materials = ['/Game/Art/Assets/Kits/Architecture/Suburbs/Materials/Suburb_Stairs_Trim/MI_Suburb_Stairs_Trim_3M']
_folder = "Reconstruction/BD_BB_OrcTown_Gate/Meshes"
a = spawn_static_mesh(_mesh_path, _materials, (3693.1404, 2305.7327, 2878.4863), (3.669730366608069e-18, -179.99928283006557, 179.99988388675877), (0.5624999, 0.74999976, 0.46875057), "BP_Suburb_Stairs_Trim_3M_Breakable_1", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3693.134, 3945.7327, 2878.4863), (3.669730366608069e-18, -179.99928283006557, 179.99988388675877), (0.5624999, 0.74999976, 0.46875057), "BP_Suburb_Stairs_Trim_3M_Breakable_3", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3693.1409, 1495.7305, 2878.4868), (3.669730366608069e-18, -179.99928283006557, 179.99988388675877), (0.5624999, 0.74999976, 0.46875057), "BP_Suburb_Stairs_Trim_3M_Breakable_4", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2749.3376, 613.0033, 2878.478), (0.00012977357838205234, 0.0009493957267356445, 179.999460415035), (0.5624999, 0.74999976, 0.46875057), "BP_Suburb_Stairs_Trim_3M_Breakable_5", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2749.3108, 3898.1047, 2878.4846), (0.00011611319338810493, 0.0006659429127577387, 179.99946041503566), (0.5624999, 0.74999976, 0.46874934), "BP_Suburb_Stairs_Trim_3M_Breakable_12", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3693.1328, 3910.6375, 2878.486), (6.83018790306208e-06, -179.9994604150155, 179.999883886768), (0.5624999, 0.74999976, 0.46874934), "BP_Suburb_Stairs_Trim_3M_Breakable_33", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2749.3042, 3863.0068, 2878.4912), (0.00012977357838205234, 0.0009493957267356445, 179.999460415035), (0.5624999, 0.74999976, 0.46875057), "BP_Suburb_Stairs_Trim_3M_Breakable_40", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2749.3108, 3088.1047, 2878.4846), (0.00011611319338810493, 0.0006659429127577387, 179.99946041503566), (0.5624999, 0.74999976, 0.46874934), "BP_Suburb_Stairs_Trim_3M_Breakable_42", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2749.3071, 3053.0034, 2878.4858), (0.00012977357838205234, 0.0009493957267356445, 179.999460415035), (0.5624999, 0.74999976, 0.46875057), "BP_Suburb_Stairs_Trim_3M_Breakable_44", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2749.3193, 1448.1011, 2878.4746), (0.00011611319338810493, 0.0006659429127577387, 179.99946041503566), (0.5624999, 0.74999976, 0.46874934), "BP_Suburb_Stairs_Trim_3M_Breakable_46", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3693.1294, 3090.6316, 2878.486), (6.83018790306208e-06, -179.9994604150155, 179.999883886768), (0.5624999, 0.74999976, 0.46874934), "BP_Suburb_Stairs_Trim_3M_Breakable_48", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3693.134, 3125.7327, 2878.4863), (3.669730366608069e-18, -179.99928283006557, 179.99988388675877), (0.5624999, 0.74999976, 0.46875057), "BP_Suburb_Stairs_Trim_3M_Breakable_50", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3693.142, 1460.6315, 2878.4866), (6.83018790306208e-06, -179.9994604150155, 179.999883886768), (0.5624999, 0.74999976, 0.46874934), "BP_Suburb_Stairs_Trim_3M_Breakable_52", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2749.313, 2268.1047, 2878.4827), (0.00011611319338810493, 0.0006659429127577387, 179.99946041503566), (0.5624999, 0.74999976, 0.46874934), "BP_Suburb_Stairs_Trim_3M_Breakable_54", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2749.325, 2233.0034, 2878.484), (0.00012977357838205234, 0.0009493957267356445, 179.999460415035), (0.5624999, 0.74999976, 0.46875057), "BP_Suburb_Stairs_Trim_3M_Breakable_56", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2749.332, 628.1013, 2878.469), (0.00011611319338810493, 0.0006659429127577387, 179.99946041503566), (0.5624999, 0.74999976, 0.46874934), "BP_Suburb_Stairs_Trim_3M_Breakable_58", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2749.3376, 1413.0033, 2878.478), (0.00012977357838205234, 0.0009493957267356445, 179.999460415035), (0.5624999, 0.74999976, 0.46875057), "BP_Suburb_Stairs_Trim_3M_Breakable_60", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3693.1487, 675.7305, 2878.4868), (3.669730366608069e-18, -179.99928283006557, 179.99988388675877), (0.5624999, 0.74999976, 0.46875057), "BP_Suburb_Stairs_Trim_3M_Breakable_62", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3693.15, 640.6316, 2878.4868), (6.83018790306208e-06, -179.9994604150155, 179.999883886768), (0.5624999, 0.74999976, 0.46874934), "BP_Suburb_Stairs_Trim_3M_Breakable_64", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3861.8901, 2305.7344, 2878.4863), (3.669730366608069e-18, -179.99928283006557, 179.99988388675877), (0.5624999, 0.74999976, 0.46875057), "BP_Suburb_Stairs_Trim_3M_Breakable3_2", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3861.8838, 3945.7344, 2878.4866), (3.669730366608069e-18, -179.99928283006557, 179.99988388675877), (0.5624999, 0.74999976, 0.46875057), "BP_Suburb_Stairs_Trim_3M_Breakable3_4", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3861.8906, 1495.7322, 2878.4868), (3.669730366608069e-18, -179.99928283006557, 179.99988388675877), (0.5624999, 0.74999976, 0.46875057), "BP_Suburb_Stairs_Trim_3M_Breakable3_5", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2580.5876, 613.00085, 2878.478), (0.00012977357838205234, 0.0009493957267356445, 179.999460415035), (0.5624999, 0.74999976, 0.46875057), "BP_Suburb_Stairs_Trim_3M_Breakable3_6", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2580.5608, 3898.103, 2878.4846), (0.00011611319338810493, 0.0006659429127577387, 179.99946041503566), (0.5624999, 0.74999976, 0.46874934), "BP_Suburb_Stairs_Trim_3M_Breakable3_13", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3861.8826, 3910.6387, 2878.4863), (6.83018790306208e-06, -179.9994604150155, 179.999883886768), (0.5624999, 0.74999976, 0.46874934), "BP_Suburb_Stairs_Trim_3M_Breakable3_34", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2580.5542, 3863.0044, 2878.4907), (0.00012977357838205234, 0.0009493957267356445, 179.999460415035), (0.5624999, 0.74999976, 0.46875057), "BP_Suburb_Stairs_Trim_3M_Breakable3_41", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2580.5608, 3088.103, 2878.4846), (0.00011611319338810493, 0.0006659429127577387, 179.99946041503566), (0.5624999, 0.74999976, 0.46874934), "BP_Suburb_Stairs_Trim_3M_Breakable3_43", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2580.5571, 3053.001, 2878.4854), (0.00012977357838205234, 0.0009493957267356445, 179.999460415035), (0.5624999, 0.74999976, 0.46875057), "BP_Suburb_Stairs_Trim_3M_Breakable3_45", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2580.5693, 1448.0996, 2878.4746), (0.00011611319338810493, 0.0006659429127577387, 179.99946041503566), (0.5624999, 0.74999976, 0.46874934), "BP_Suburb_Stairs_Trim_3M_Breakable3_47", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3861.8796, 3090.6328, 2878.4863), (6.83018790306208e-06, -179.9994604150155, 179.999883886768), (0.5624999, 0.74999976, 0.46874934), "BP_Suburb_Stairs_Trim_3M_Breakable3_49", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3861.8838, 3125.7344, 2878.4866), (3.669730366608069e-18, -179.99928283006557, 179.99988388675877), (0.5624999, 0.74999976, 0.46875057), "BP_Suburb_Stairs_Trim_3M_Breakable3_51", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3861.8923, 1460.6328, 2878.4868), (6.83018790306208e-06, -179.9994604150155, 179.999883886768), (0.5624999, 0.74999976, 0.46874934), "BP_Suburb_Stairs_Trim_3M_Breakable3_53", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2580.563, 2268.103, 2878.4827), (0.00011611319338810493, 0.0006659429127577387, 179.99946041503566), (0.5624999, 0.74999976, 0.46874934), "BP_Suburb_Stairs_Trim_3M_Breakable3_55", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2580.575, 2233.001, 2878.4834), (0.00012977357838205234, 0.0009493957267356445, 179.999460415035), (0.5624999, 0.74999976, 0.46875057), "BP_Suburb_Stairs_Trim_3M_Breakable3_57", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2580.582, 628.0996, 2878.469), (0.00011611319338810493, 0.0006659429127577387, 179.99946041503566), (0.5624999, 0.74999976, 0.46874934), "BP_Suburb_Stairs_Trim_3M_Breakable3_59", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2580.5876, 1413.0009, 2878.478), (0.00012977357838205234, 0.0009493957267356445, 179.999460415035), (0.5624999, 0.74999976, 0.46875057), "BP_Suburb_Stairs_Trim_3M_Breakable3_61", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3861.8984, 675.7322, 2878.4873), (3.669730366608069e-18, -179.99928283006557, 179.99988388675877), (0.5624999, 0.74999976, 0.46875057), "BP_Suburb_Stairs_Trim_3M_Breakable3_63", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3861.9, 640.63293, 2878.487), (6.83018790306208e-06, -179.9994604150155, 179.999883886768), (0.5624999, 0.74999976, 0.46874934), "BP_Suburb_Stairs_Trim_3M_Breakable3_65", _folder)
if a: placed += 1
else: skipped += 1

# Batch 30: StaticMesh'Suburb_Stairs_Trim_Angle_B' (39 instances)
_mesh_path = "/Game/Art/Assets/Kits/Architecture/Suburbs/Suburb_Stairs_Trim_Angle_B"
_materials = ['/Game/Art/Assets/Kits/Architecture/Suburbs/Materials/Suburb_Stairs_Trim/MI_Suburbs_Stairs_Trim_Angle']
_folder = "Reconstruction/BD_BB_OrcTown_Gate/Meshes"
a = spawn_static_mesh(_mesh_path, _materials, (2379.3071, 4291.847, 2667.5498), (0.0004371320936584063, 90.00053783891171, 2.600000864464145e-05), (0.74999976, 0.74999976, 0.46874934), "BP_Suburb_Stairs_Trim_Angle_B_Breakable_12", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4063.1362, 3516.8955, 2667.5493), (2.0490570620033804e-05, -89.99954442868432, -9.155273515911724e-05), (0.74999976, 0.74999976, 0.46874934), "BP_Suburb_Stairs_Trim_Angle_B_Breakable_32", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2379.3071, 3481.8474, 2667.5498), (0.00043713209236119314, 90.00053783891285, 2.627796871023012e-05), (0.74999976, 0.74999976, 0.46874934), "BP_Suburb_Stairs_Trim_Angle_B_Breakable_45", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2379.3157, 1841.8438, 2667.54), (0.00043713209236119314, 90.00053783891285, 2.627796871023012e-05), (0.74999976, 0.74999976, 0.46874934), "BP_Suburb_Stairs_Trim_Angle_B_Breakable_49", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4063.1328, 2696.8896, 2667.5493), (2.0490570620033804e-05, -89.99954442868432, -9.155273515911724e-05), (0.74999976, 0.74999976, 0.46874934), "BP_Suburb_Stairs_Trim_Angle_B_Breakable_51", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4063.1455, 1066.8898, 2667.5498), (2.0490570620033804e-05, -89.99954442868432, -9.155273515911724e-05), (0.74999976, 0.74999976, 0.46874934), "BP_Suburb_Stairs_Trim_Angle_B_Breakable_55", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2379.3093, 2661.8474, 2667.5479), (0.0004371320936584063, 90.00053783891171, 2.600000864464145e-05), (0.74999976, 0.74999976, 0.46874934), "BP_Suburb_Stairs_Trim_Angle_B_Breakable_57", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2379.3284, 1021.84375, 2667.5342), (0.0004371320936584063, 90.00053783891171, 2.600000864464145e-05), (0.74999976, 0.74999976, 0.46874934), "BP_Suburb_Stairs_Trim_Angle_B_Breakable_61", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4063.1533, 246.88991, 2667.55), (2.0490570620033804e-05, -89.99954442868432, -9.155273515911724e-05), (0.74999976, 0.74999976, 0.46874934), "BP_Suburb_Stairs_Trim_Angle_B_Breakable_67", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4003.7104, 2338.235, 2731.5574), (9.562262870182897e-05, 0.000597641319858382, 179.9999590188577), (1.587143, 1.2907403, 0.94240904), "BP_Suburb_Stairs_Trim_Angle_B_Breakable2_0", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4003.7046, 1513.2329, 2731.5583), (9.562262870182897e-05, 0.000597641319858382, 179.9999590188577), (1.587143, 1.2907403, 0.94240904), "BP_Suburb_Stairs_Trim_Angle_B_Breakable2_1", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4003.7131, 3962.6333, 2731.558), (9.562262870182897e-05, 0.000597641319858382, 179.9999590188577), (1.5650048, 1.2686023, 0.9202709), "BP_Suburb_Stairs_Trim_Angle_B_Breakable2_3", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2438.8948, 585.5005, 2727.553), (-3.051757905706913e-05, -179.99915988675102, -179.99963116977), (1.4765972, 1.2907403, 0.88129586), "BP_Suburb_Stairs_Trim_Angle_B_Breakable2_4", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2439.115, 3880.603, 2733.5642), (-3.0517574191304315e-05, -179.99940577342986, -179.99963116974124), (1.3328546, 1.2907364, 0.89750546), "BP_Suburb_Stairs_Trim_Angle_B_Breakable2_13", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4003.7097, 3928.1392, 2731.553), (0.00010245283308802073, 0.0004644527179145772, 179.99994535848458), (1.5650017, 1.2685984, 0.9202707), "BP_Suburb_Stairs_Trim_Angle_B_Breakable2_33", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2439.1035, 3845.504, 2733.5737), (-3.051757905706913e-05, -179.99915988675102, -179.99963116977), (1.3328577, 1.2907403, 0.8975058), "BP_Suburb_Stairs_Trim_Angle_B_Breakable2_43", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2439.0928, 3070.603, 2733.5676), (-3.0517574191304315e-05, -179.99940577342986, -179.99963116974124), (1.3328546, 1.2907364, 0.89750546), "BP_Suburb_Stairs_Trim_Angle_B_Breakable2_46", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2439.086, 3035.5005, 2733.5684), (-3.051757905706913e-05, -179.99915988675102, -179.99963116977), (1.3328577, 1.2907403, 0.8975058), "BP_Suburb_Stairs_Trim_Angle_B_Breakable2_47", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2439.0642, 1425.5994, 2733.5576), (-3.0517574191304315e-05, -179.99940577342986, -179.99963116974124), (1.3328546, 1.2907364, 0.89750546), "BP_Suburb_Stairs_Trim_Angle_B_Breakable2_50", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4003.6934, 3108.1333, 2731.5576), (0.00010245283308802073, 0.0004644527179145772, 179.99994535848458), (1.5871398, 1.2907364, 0.94240856), "BP_Suburb_Stairs_Trim_Angle_B_Breakable2_52", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4003.7107, 3143.2354, 2731.5579), (9.562262870182897e-05, 0.000597641319858382, 179.9999590188577), (1.587143, 1.2907403, 0.94240904), "BP_Suburb_Stairs_Trim_Angle_B_Breakable2_53", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4003.7058, 1478.1335, 2731.5574), (0.00010245283308802073, 0.0004644527179145772, 179.99994535848458), (1.5871398, 1.2907364, 0.94240856), "BP_Suburb_Stairs_Trim_Angle_B_Breakable2_56", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2439.0754, 2250.603, 2733.566), (-3.0517574191304315e-05, -179.99940577342986, -179.99963116974124), (1.3328546, 1.2907364, 0.89750546), "BP_Suburb_Stairs_Trim_Angle_B_Breakable2_58", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2439.0906, 2215.5005, 2733.567), (-3.051757905706913e-05, -179.99915988675102, -179.99963116977), (1.3328577, 1.2907403, 0.8975058), "BP_Suburb_Stairs_Trim_Angle_B_Breakable2_59", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2438.8904, 610.59937, 2727.5388), (-3.0517574191304315e-05, -179.99940577342986, -179.99963116974124), (1.4765941, 1.2907364, 0.8812955), "BP_Suburb_Stairs_Trim_Angle_B_Breakable2_62", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2439.085, 1390.5005, 2733.5615), (-3.051757905706913e-05, -179.99915988675102, -179.99963116977), (1.3328577, 1.2907403, 0.8975058), "BP_Suburb_Stairs_Trim_Angle_B_Breakable2_63", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4003.7124, 688.233, 2731.5586), (9.562262870182897e-05, 0.000597641319858382, 179.9999590188577), (1.587143, 1.2907403, 0.94240904), "BP_Suburb_Stairs_Trim_Angle_B_Breakable2_65", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4003.7136, 653.1332, 2731.558), (0.00010245283308802073, 0.0004644527179145772, 179.99994535848458), (1.5871398, 1.2907364, 0.94240856), "BP_Suburb_Stairs_Trim_Angle_B_Breakable2_68", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4063.1328, 1886.8896, 2667.5493), (2.00000023916706e-05, -89.99954442868383, -9.155273468122048e-05), (0.75, 0.75, 0.468749), "BP_Suburb_Stairs_Trim_Angle_B_Breakable3", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4083.1377, 1889.4844, 2667.55), (-3.051758006242164e-05, 90.00037578044967, 9.155280093117228e-05), (0.74999976, 0.74999976, 0.46875057), "BP_Suburb_Stairs_Trim_Angle_B_Breakable9", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4083.137, 2699.4866, 2667.5496), (-3.051758006242164e-05, 90.00037578044967, 9.155280093117228e-05), (0.74999976, 0.74999976, 0.46875057), "BP_Suburb_Stairs_Trim_Angle_B_Breakable9_1", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4083.1309, 4339.4863, 2667.5496), (-3.051758006242164e-05, 90.00037578044967, 9.155280093117228e-05), (0.74999976, 0.74999976, 0.46875057), "BP_Suburb_Stairs_Trim_Angle_B_Breakable9_4", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2359.3433, 219.2493, 2667.5374), (-0.00042724607956581324, -89.99938723476131, -3.0517585690276625e-05), (0.74999976, 0.74999976, 0.46875057), "BP_Suburb_Stairs_Trim_Angle_B_Breakable9_5", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2359.3098, 3469.2527, 2667.5508), (-0.00042724607956581324, -89.99938723476131, -3.0517585690276625e-05), (0.74999976, 0.74999976, 0.46875057), "BP_Suburb_Stairs_Trim_Angle_B_Breakable9_44", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2359.3127, 2659.2493, 2667.5454), (-0.00042724607956581324, -89.99938723476131, -3.0517585690276625e-05), (0.74999976, 0.74999976, 0.46875057), "BP_Suburb_Stairs_Trim_Angle_B_Breakable9_48", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4083.1306, 3519.4866, 2667.5496), (-3.051758006242164e-05, 90.00037578044967, 9.155280093117228e-05), (0.74999976, 0.74999976, 0.46875057), "BP_Suburb_Stairs_Trim_Angle_B_Breakable9_54", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2359.3306, 1839.2493, 2667.5435), (-0.00042724607956581324, -89.99938723476131, -3.0517585690276625e-05), (0.74999976, 0.74999976, 0.46875057), "BP_Suburb_Stairs_Trim_Angle_B_Breakable9_60", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2359.3433, 1019.24927, 2667.5374), (-0.00042724607956581324, -89.99938723476131, -3.0517585690276625e-05), (0.74999976, 0.74999976, 0.46875057), "BP_Suburb_Stairs_Trim_Angle_B_Breakable9_64", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4083.1453, 1069.4844, 2667.5503), (-3.051758006242164e-05, 90.00037578044967, 9.155280093117228e-05), (0.74999976, 0.74999976, 0.46875057), "BP_Suburb_Stairs_Trim_Angle_B_Breakable9_66", _folder)
if a: placed += 1
else: skipped += 1

# Batch 31: StaticMesh'Suburb_Stairs_Trim_Pillar_A' (19 instances)
_mesh_path = "/Game/Art/Assets/Kits/Architecture/Suburbs/Suburb_Stairs_Trim_Pillar_A"
_materials = ['/Game/Art/Assets/Kits/Architecture/Suburbs/Materials/Suburb_Stairs_Trim/MI_Suburb_Stairs_Trim_Pillar_A']
_folder = "Reconstruction/BD_BB_OrcTown_Gate/Meshes"
a = spawn_static_mesh(_mesh_path, _materials, (3531.8906, 1491.9788, 2887.8613), (-0.0009460448717566993, -0.0019531249994513527, 179.99959701883404), (0.74999976, 0.74999976, 0.46875057), "BP_Suburb_Stairs_Trim_Pillar_A_Breakable_0", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3531.8838, 3941.981, 2887.8608), (-0.0009460448717566993, -0.0019531249994513527, 179.99959701883404), (0.74999976, 0.74999976, 0.46875057), "BP_Suburb_Stairs_Trim_Pillar_A_Breakable_2", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3531.8901, 2301.981, 2887.8608), (-0.0009460448717566993, -0.0019531249994513527, 179.99959701883404), (0.74999976, 0.74999976, 0.46875057), "BP_Suburb_Stairs_Trim_Pillar_A_Breakable_3", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2910.588, 616.75555, 2887.853), (-0.0010681150370139023, 179.9982856223829, -179.99995901885632), (0.74999976, 0.74999976, 0.46875057), "BP_Suburb_Stairs_Trim_Pillar_A_Breakable_4", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2910.5605, 3901.8564, 2887.8596), (0.0007376603726472672, 0.0007274126957788809, 179.99963116978267), (0.74999976, 0.74999976, 0.46874934), "BP_Suburb_Stairs_Trim_Pillar_A_Breakable_7", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3531.8828, 3906.886, 2887.8608), (0.0006147171242746336, -179.99936479262144, -179.9999453584941), (0.74999976, 0.74999976, 0.46874934), "BP_Suburb_Stairs_Trim_Pillar_A_Breakable_19", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2910.5542, 3866.7593, 2887.866), (-0.0010681150370139023, 179.9982856223829, -179.99995901885632), (0.74999976, 0.74999976, 0.46875057), "BP_Suburb_Stairs_Trim_Pillar_A_Breakable_31", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2910.5605, 3091.8562, 2887.8596), (0.0007376603726472672, 0.0007274126957788809, 179.99963116978267), (0.74999976, 0.74999976, 0.46874934), "BP_Suburb_Stairs_Trim_Pillar_A_Breakable_32", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2910.5571, 3056.7556, 2887.8606), (-0.0010681150370139023, 179.9982856223829, -179.99995901885632), (0.74999976, 0.74999976, 0.46875057), "BP_Suburb_Stairs_Trim_Pillar_A_Breakable_33", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2910.5693, 1451.8525, 2887.8496), (0.0007376603726472672, 0.0007274126957788809, 179.99963116978267), (0.74999976, 0.74999976, 0.46874934), "BP_Suburb_Stairs_Trim_Pillar_A_Breakable_34", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3531.8794, 3086.8801, 2887.8608), (0.0006147171242746336, -179.99936479262144, -179.9999453584941), (0.74999976, 0.74999976, 0.46874934), "BP_Suburb_Stairs_Trim_Pillar_A_Breakable_35", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3531.8838, 3121.981, 2887.8608), (-0.0009460448717566993, -0.0019531249994513527, 179.99959701883404), (0.74999976, 0.74999976, 0.46875057), "BP_Suburb_Stairs_Trim_Pillar_A_Breakable_36", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3531.892, 1456.8801, 2887.8613), (0.0006147171242746336, -179.99936479262144, -179.9999453584941), (0.74999976, 0.74999976, 0.46874934), "BP_Suburb_Stairs_Trim_Pillar_A_Breakable_37", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2910.563, 2271.8562, 2887.8577), (0.0007376603726472672, 0.0007274126957788809, 179.99963116978267), (0.74999976, 0.74999976, 0.46874934), "BP_Suburb_Stairs_Trim_Pillar_A_Breakable_38", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2910.5752, 2236.7556, 2887.8586), (-0.0010681150370139023, 179.9982856223829, -179.99995901885632), (0.74999976, 0.74999976, 0.46875057), "BP_Suburb_Stairs_Trim_Pillar_A_Breakable_39", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2910.582, 631.85266, 2887.844), (0.0007376603726472672, 0.0007274126957788809, 179.99963116978267), (0.74999976, 0.74999976, 0.46874934), "BP_Suburb_Stairs_Trim_Pillar_A_Breakable_40", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2910.588, 1416.7555, 2887.853), (-0.0010681150370139023, 179.9982856223829, -179.99995901885632), (0.74999976, 0.74999976, 0.46875057), "BP_Suburb_Stairs_Trim_Pillar_A_Breakable_41", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3531.8984, 671.97876, 2887.8616), (-0.0009460448717566993, -0.0019531249994513527, 179.99959701883404), (0.74999976, 0.74999976, 0.46875057), "BP_Suburb_Stairs_Trim_Pillar_A_Breakable_42", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3531.9, 636.8784, 2887.8616), (0.0006147171242746336, -179.99936479262144, -179.9999453584941), (0.74999976, 0.74999976, 0.46874934), "BP_Suburb_Stairs_Trim_Pillar_A_Breakable_43", _folder)
if a: placed += 1
else: skipped += 1

# Batch 32: StaticMesh'Suburbs_Column_Large_A_A_Base_Ruined' (1 instances)
_mesh_path = "/Game/Art/Assets/Kits/Architecture/Suburbs/Suburbs_Column_Large_A_A_Base_Ruined"
_materials = ['/Game/Art/Assets/Kits/Architecture/Suburbs/Materials/Suburbs_Column_Large_A_Ruined/MI_Suburbs_Column_Large_A_Base_Ruined']
_folder = "Reconstruction/BD_BB_OrcTown_Gate/Meshes"
a = spawn_static_mesh(_mesh_path, _materials, (4354.1567, 1519.1278, 1100.9489), (0.0, -89.99984099200987, 0.0), (1.0, 1.0, 1.0), "Suburbs_Column_Large_A_A_Base_Ruined2_180", _folder)
if a: placed += 1
else: skipped += 1

# Batch 33: StaticMesh'Suburbs_Column_Large_A_A_Shaft_Ruined' (2 instances)
_mesh_path = "/Game/Art/Assets/Kits/Architecture/Suburbs/Suburbs_Column_Large_A_A_Shaft_Ruined"
_materials = ['/Game/Art/Assets/Kits/Architecture/Suburbs/Materials/Suburbs_Column_Large_A_Ruined/MI_Suburbs_Column_Large_A_Shaft_Ruined']
_folder = "Reconstruction/BD_BB_OrcTown_Gate/Meshes"
a = spawn_static_mesh(_mesh_path, _materials, (4640.1694, 1669.3179, 1676.2246), (31.62216105185953, 162.844116876143, 150.92461375717454), (1.0, 1.0, 1.0), "Suburbs_Column_Large_A_A_Shaft_Ruined3", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4690.7344, 1680.9998, 1677.8817), (14.568956075540232, -95.73003181068854, 13.563844058273903), (1.0, 1.0, 1.0), "Suburbs_Column_Large_A_A_Shaft_Ruined5", _folder)
if a: placed += 1
else: skipped += 1

# Batch 34: StaticMesh'Suburbs_Column_Large_A_Base' (36 instances)
_mesh_path = "/Game/Art/Assets/Kits/Architecture/Suburbs/Suburbs_Column_Large_A_Base"
_materials = ['/Game/Art/Assets/Kits/Architecture/Suburbs/Materials/Suburbs_Column_Large/MI_Suburbs_Column_Large_A_Base']
_folder = "Reconstruction/BD_BB_OrcTown_Gate/Meshes"
a = spawn_static_mesh(_mesh_path, _materials, (1930.6084, 474.3506, 1100.0), (0.0, 140.0001469222118, -0.0), (1.0, 1.0, 1.0), "Suburbs_Column_Large_A_Base10", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3793.3005, 5450.0015, 1200.0), (0.0, -9.155273700792082e-05, 0.0), (1.0, 1.0, 1.0), "Suburbs_Column_Large_A_Base10_1112", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1930.6084, 474.3506, 1100.0), (0.0, -129.99989450513715, 0.0), (1.0, 1.0, 1.0), "Suburbs_Column_Large_A_Base11", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3793.3013, 5450.0015, 1113.7216), (0.0, -89.99984099200987, 0.0), (1.0, 1.0, 1.0718989), "Suburbs_Column_Large_A_Base11_1119", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1930.6084, 474.3506, 1100.0), (0.0, 49.99997085178047, -0.0), (1.0, 1.0, 1.0), "Suburbs_Column_Large_A_Base12", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3793.3013, 5450.0015, 1113.7216), (0.0, -179.9998975471592, 0.0), (1.0, 1.0, 1.0718989), "Suburbs_Column_Large_A_Base12_1120", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2593.2993, 5449.9927, 1200.0), (0.0, -89.99984099200987, 0.0), (1.0, 1.0, 1.0), "Suburbs_Column_Large_A_Base13_1127", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2593.2993, 5449.9927, 1200.0), (0.0, -179.9998975471592, 0.0), (1.0, 1.0, 1.0), "Suburbs_Column_Large_A_Base14_1128", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2593.2993, 5449.9927, 1115.8064), (0.0, -9.155273700792082e-05, 0.0), (1.0, 1.0, 1.0701616), "Suburbs_Column_Large_A_Base15_1129", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2593.2993, 5449.9927, 1115.8064), (0.0, 89.99993822608693, -0.0), (1.0, 1.0, 1.0701616), "Suburbs_Column_Large_A_Base16_1130", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1945.6084, 2634.3506, 1100.0), (0.0, -40.00005923828246, 0.0), (1.0, 1.0, 1.0), "Suburbs_Column_Large_A_Base17_111", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1945.6084, 2634.3506, 1100.0), (0.0, 140.0001469222118, -0.0), (1.0, 1.0, 1.0), "Suburbs_Column_Large_A_Base18_112", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1945.6084, 2634.3506, 1100.0), (0.0, -129.99989450513715, 0.0), (1.0, 1.0, 1.0), "Suburbs_Column_Large_A_Base19_113", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1945.6084, 2634.3506, 1100.0), (0.0, 49.99997085178047, -0.0), (1.0, 1.0, 1.0), "Suburbs_Column_Large_A_Base20_114", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1950.0, 3740.0, 1286.25), (0.0, 50.00005877099974, -0.0), (1.0, 1.0, 0.9375), "Suburbs_Column_Large_A_Base21", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1950.002, 3740.0002, 1286.25), (0.0, -129.9997744363527, 0.0), (1.0, 1.0, 0.9375), "Suburbs_Column_Large_A_Base22", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1950.0002, 3740.0, 1286.25), (0.0, -39.999878070029396, 0.0), (1.0, 1.0, 0.9375), "Suburbs_Column_Large_A_Base23", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1950.0, 3740.0, 1286.25), (0.0, 140.00001793552548, -0.0), (1.0, 1.0, 0.9375), "Suburbs_Column_Large_A_Base24", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4380.0, 2670.0, 1286.25), (0.0, -45.000056798727684, 0.0), (1.0, 1.0, 0.9375), "Suburbs_Column_Large_A_Base25", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4380.0, 2670.0, 1286.25), (0.0, 135.00014775251523, -0.0), (1.0, 1.0, 0.9375), "Suburbs_Column_Large_A_Base26", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4380.0, 2669.996, 1286.25), (0.0, -134.9999263430944, 0.0), (1.0, 1.0, 0.9375), "Suburbs_Column_Large_A_Base27", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4380.0, 2670.0, 1286.25), (0.0, 44.99994040916364, -0.0), (1.0, 1.0, 0.9375), "Suburbs_Column_Large_A_Base28", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4360.0, 3739.9995, 1286.25), (0.0, -45.000056798727684, 0.0), (1.0, 1.0, 0.9375), "Suburbs_Column_Large_A_Base29", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4360.0, 3740.0, 1286.25), (0.0, 135.00014775251523, -0.0), (1.0, 1.0, 0.9375), "Suburbs_Column_Large_A_Base30", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4360.0, 3739.996, 1286.25), (0.0, -134.9999263430944, 0.0), (1.0, 1.0, 0.9375), "Suburbs_Column_Large_A_Base31", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4360.0, 3740.0, 1286.25), (0.0, 44.99994040916364, -0.0), (1.0, 1.0, 0.9375), "Suburbs_Column_Large_A_Base32", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4380.0, 480.0, 1006.25), (0.0, -45.000056798727684, 0.0), (1.0, 1.0, 0.9375), "Suburbs_Column_Large_A_Base37", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4380.0, 480.0, 1006.25), (0.0, 135.00014775251523, -0.0), (1.0, 1.0, 0.9375), "Suburbs_Column_Large_A_Base38", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4380.0, 479.9961, 1006.25), (0.0, -134.9999263430944, 0.0), (1.0, 1.0, 0.9375), "Suburbs_Column_Large_A_Base39", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4380.0, 480.0, 1006.25), (0.0, 44.99994040916364, -0.0), (1.0, 1.0, 0.9375), "Suburbs_Column_Large_A_Base40", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1945.6084, 1554.3506, 1100.0), (0.0, -40.00005923828246, 0.0), (1.0, 1.0, 1.0), "Suburbs_Column_Large_A_Base5", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1945.6084, 1554.3506, 1100.0), (0.0, 140.0001469222118, -0.0), (1.0, 1.0, 1.0), "Suburbs_Column_Large_A_Base6", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1945.6084, 1554.3506, 1100.0), (0.0, -129.99989450513715, 0.0), (1.0, 1.0, 1.0), "Suburbs_Column_Large_A_Base7", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1945.6084, 1554.3506, 1100.0), (0.0, 49.99997085178047, -0.0), (1.0, 1.0, 1.0), "Suburbs_Column_Large_A_Base8", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1930.6084, 474.3506, 1100.0), (0.0, -40.00005923828246, 0.0), (1.0, 1.0, 1.0), "Suburbs_Column_Large_A_Base9", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3793.3013, 5450.0015, 1200.0), (0.0, 90.0002137230564, -0.0), (1.0, 1.0, 1.0), "Suburbs_Column_Large_A_Base9_1111", _folder)
if a: placed += 1
else: skipped += 1

# Batch 35: StaticMesh'Suburbs_Column_Large_A_C_Capitol_Ruined' (1 instances)
_mesh_path = "/Game/Art/Assets/Kits/Architecture/Suburbs/Suburbs_Column_Large_A_C_Capitol_Ruined"
_materials = ['/Game/Art/Assets/Kits/Architecture/Suburbs/Materials/Suburbs_Column_Large_A_Ruined/MI_Suburbs_Column_Large_A_Shaft_Ruined', '/Game/Art/Assets/Kits/Architecture/Suburbs/Materials/Suburbs_Column_Large_A_Ruined/MI_Suburbs_Column_Large_A_Capitol_Ruined']
_folder = "Reconstruction/BD_BB_OrcTown_Gate/Meshes"
a = spawn_static_mesh(_mesh_path, _materials, (4463.732, 1862.489, 1071.7252), (-2.8740233920519453, 49.667457366371174, -5.620056679961344), (1.0, 1.0, 1.0), "Suburbs_Column_Large_A_C_Capitol_Ruined2_172", _folder)
if a: placed += 1
else: skipped += 1

# Batch 36: StaticMesh'Suburbs_Column_Large_A_Capitol' (36 instances)
_mesh_path = "/Game/Art/Assets/Kits/Architecture/Suburbs/Suburbs_Column_Large_A_Capitol"
_materials = ['/Game/Art/Assets/Kits/Architecture/Suburbs/Materials/Suburbs_Column_Large/MI_Suburbs_Column_Large_A_Capitol']
_folder = "Reconstruction/BD_BB_OrcTown_Gate/Meshes"
a = spawn_static_mesh(_mesh_path, _materials, (1930.6084, 474.3506, 1920.0), (0.0, -129.99989450513715, 0.0), (1.0, 1.0, 1.0), "Suburbs_Column_Large_A_Capitol10", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3793.3013, 5450.0015, 2400.0), (0.0, 0.00020149055520549277, -0.0), (1.0, 1.0, 1.0), "Suburbs_Column_Large_A_Capitol10_1118", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1930.6084, 474.3506, 1920.0), (0.0, 50.00020766400425, -0.0), (1.0, 1.0, 1.0), "Suburbs_Column_Large_A_Capitol11", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3793.3013, 5450.0015, 2400.0), (0.0, -89.99984099200987, 0.0), (1.0, 1.0, 1.0), "Suburbs_Column_Large_A_Capitol11_1125", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1930.6084, 474.3506, 1920.0), (0.0, 140.00001793552548, -0.0), (1.0, 1.0, 1.0), "Suburbs_Column_Large_A_Capitol12", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3793.3013, 5450.0015, 2400.0), (0.0, -179.9998975471592, 0.0), (1.0, 1.0, 1.0), "Suburbs_Column_Large_A_Capitol12_1126", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2593.2993, 5449.9927, 2400.0), (0.0, -89.99984099200987, 0.0), (1.0, 1.0, 1.0), "Suburbs_Column_Large_A_Capitol13_1139", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2593.2993, 5449.9927, 2400.0), (0.0, -179.9998975471592, 0.0), (1.0, 1.0, 1.0), "Suburbs_Column_Large_A_Capitol14_1140", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2593.2993, 5449.9927, 2400.0), (0.0, 90.00005166594045, -0.0), (1.0, 1.0, 1.0), "Suburbs_Column_Large_A_Capitol15_1141", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2593.2993, 5449.9927, 2400.0), (0.0, -9.155273700792082e-05, 0.0), (1.0, 1.0, 1.0), "Suburbs_Column_Large_A_Capitol16_1142", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1938.5991, 2636.2275, 1922.5), (0.0, -40.00005923828246, 0.0), (1.0, 1.0, 0.9375), "Suburbs_Column_Large_A_Capitol17", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1938.5991, 2636.2275, 1922.5), (0.0, -129.99989450513715, 0.0), (1.0, 1.0, 0.9375), "Suburbs_Column_Large_A_Capitol18", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1938.5991, 2636.2275, 1922.5), (0.0, 50.00020766400425, -0.0), (1.0, 1.0, 0.9375), "Suburbs_Column_Large_A_Capitol19", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1938.5991, 2636.2275, 1922.5), (0.0, 140.00001793552548, -0.0), (1.0, 1.0, 0.9375), "Suburbs_Column_Large_A_Capitol20", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1950.0, 3740.0, 1942.5), (0.0, 50.00005877099974, -0.0), (1.0, 1.0, 0.9375), "Suburbs_Column_Large_A_Capitol21", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1950.0002, 3740.0, 1942.5), (0.0, -39.999878070029396, 0.0), (1.0, 1.0, 0.9375), "Suburbs_Column_Large_A_Capitol22", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1950.0, 3740.0, 1942.5), (0.0, 140.0001469222118, -0.0), (1.0, 1.0, 0.9375), "Suburbs_Column_Large_A_Capitol23", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1950.0, 3740.0, 1942.5), (0.0, -129.99986167950343, 0.0), (1.0, 1.0, 0.9375), "Suburbs_Column_Large_A_Capitol24", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4380.0, 2670.0, 1947.5), (0.0, -45.000056798727684, 0.0), (1.0, 1.0, 0.9375), "Suburbs_Column_Large_A_Capitol25", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4380.0, 2669.996, 1947.5), (0.0, -134.9999263430944, 0.0), (1.0, 1.0, 0.9375), "Suburbs_Column_Large_A_Capitol26", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4380.0, 2670.0, 1947.5), (0.0, 45.00019222274276, -0.0), (1.0, 1.0, 0.9375), "Suburbs_Column_Large_A_Capitol27", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4380.0, 2670.0, 1947.5), (0.0, 135.00001466939858, -0.0), (1.0, 1.0, 0.9375), "Suburbs_Column_Large_A_Capitol28", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4360.0, 3739.9995, 1947.5), (0.0, -45.000056798727684, 0.0), (1.0, 1.0, 0.9375), "Suburbs_Column_Large_A_Capitol29", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4360.0, 3739.996, 1947.5), (0.0, -134.9999263430944, 0.0), (1.0, 1.0, 0.9375), "Suburbs_Column_Large_A_Capitol30", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4360.0, 3740.0, 1947.5), (0.0, 45.00019222274276, -0.0), (1.0, 1.0, 0.9375), "Suburbs_Column_Large_A_Capitol31", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4360.0, 3740.0, 1947.5), (0.0, 135.00001466939858, -0.0), (1.0, 1.0, 0.9375), "Suburbs_Column_Large_A_Capitol32", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4380.0, 480.0, 1947.5), (0.0, -45.000056798727684, 0.0), (1.0, 1.0, 0.9375), "Suburbs_Column_Large_A_Capitol37", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4380.0, 479.9961, 1947.5), (0.0, -134.9999263430944, 0.0), (1.0, 1.0, 0.9375), "Suburbs_Column_Large_A_Capitol38", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4380.0, 480.0, 1947.5), (0.0, 45.00019222274276, -0.0), (1.0, 1.0, 0.9375), "Suburbs_Column_Large_A_Capitol39", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4380.0, 480.0, 1947.5), (0.0, 135.00001466939858, -0.0), (1.0, 1.0, 0.9375), "Suburbs_Column_Large_A_Capitol40", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1945.6084, 1554.3506, 1920.0), (0.0, -40.00005923828246, 0.0), (1.0, 1.0, 1.0), "Suburbs_Column_Large_A_Capitol5", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1945.6084, 1554.3506, 1920.0), (0.0, -129.99989450513715, 0.0), (1.0, 1.0, 1.0), "Suburbs_Column_Large_A_Capitol6", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1945.6084, 1554.3506, 1920.0), (0.0, 50.00020766400425, -0.0), (1.0, 1.0, 1.0), "Suburbs_Column_Large_A_Capitol7", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1945.6084, 1554.3506, 1920.0), (0.0, 140.00001793552548, -0.0), (1.0, 1.0, 1.0), "Suburbs_Column_Large_A_Capitol8", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1930.6084, 474.3506, 1920.0), (0.0, -40.00005923828246, 0.0), (1.0, 1.0, 1.0), "Suburbs_Column_Large_A_Capitol9", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3793.3013, 5450.0015, 2400.0), (0.0, 90.0002137230564, -0.0), (1.0, 1.0, 1.0), "Suburbs_Column_Large_A_Capitol9_1117", _folder)
if a: placed += 1
else: skipped += 1

# Batch 37: StaticMesh'Suburbs_Column_Large_A_Shaft' (48 instances)
_mesh_path = "/Game/Art/Assets/Kits/Architecture/Suburbs/Suburbs_Column_Large_A_Shaft"
_materials = ['/Game/Art/Assets/Kits/Architecture/Suburbs/Materials/Suburbs_Column_Large/MI_Suburbs_Column_Large_A_Shaft']
_folder = "Reconstruction/BD_BB_OrcTown_Gate/Meshes"
a = spawn_static_mesh(_mesh_path, _materials, (1930.6084, 474.3506, 1497.5), (0.0, -130.00002992803184, 0.0), (1.0, 1.0, 1.0625), "Suburbs_Column_Large_A_Shaft10", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3793.3013, 5450.0015, 1600.0), (0.0, 0.0002288113142805212, -0.0), (1.0, 1.0, 1.0), "Suburbs_Column_Large_A_Shaft10_1114", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1930.6084, 474.3506, 1497.5), (0.0, 139.99994676084953, -0.0), (1.0, 1.0, 1.0625), "Suburbs_Column_Large_A_Shaft11", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3793.3013, 5450.0015, 1971.2402), (0.0, 90.0002137230564, -0.0), (1.0, 1.0, 1.0718989), "Suburbs_Column_Large_A_Shaft11_1115", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1930.6084, 474.3506, 1497.5), (0.0, 49.99981615650917, -0.0), (1.0, 1.0, 1.0625), "Suburbs_Column_Large_A_Shaft12", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3793.3013, 5450.0015, 2000.0), (0.0, 0.00020149055520549277, -0.0), (1.0, 1.0, 1.0), "Suburbs_Column_Large_A_Shaft12_1116", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3793.3013, 5450.0015, 1600.0), (0.0, -89.99984099200987, 0.0), (1.0, 1.0, 1.0), "Suburbs_Column_Large_A_Shaft13_1121", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3793.3013, 5450.0015, 1542.4813), (0.0, -179.9998975471592, 0.0), (1.0, 1.0, 1.0718989), "Suburbs_Column_Large_A_Shaft14_1122", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3793.3013, 5450.0015, 2000.0), (0.0, -89.99984099200987, 0.0), (1.0, 1.0, 1.0), "Suburbs_Column_Large_A_Shaft15_1123", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3793.3013, 5450.0015, 1971.2402), (0.0, -179.9998975471592, 0.0), (1.0, 1.0, 1.0718989), "Suburbs_Column_Large_A_Shaft16_1124", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2593.2993, 5449.9927, 1543.8708), (0.0, -89.99984099200987, 0.0), (1.0, 1.0, 1.0701616), "Suburbs_Column_Large_A_Shaft17_1131", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2593.2993, 5449.9927, 1600.0), (0.0, -179.9998975471592, 0.0), (1.0, 1.0, 1.0), "Suburbs_Column_Large_A_Shaft18_1132", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2593.2993, 5449.9927, 1600.0), (0.0, 90.00060266115494, -0.0), (1.0, 1.0, 1.0), "Suburbs_Column_Large_A_Shaft19_1133", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2593.2993, 5449.9927, 1543.8708), (0.0, 0.0002800377289519776, -0.0), (1.0, 1.0, 1.0701616), "Suburbs_Column_Large_A_Shaft20_1134", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2593.2993, 5449.9927, 1971.9353), (0.0, -89.99984099200987, 0.0), (1.0, 1.0, 1.0701616), "Suburbs_Column_Large_A_Shaft21_1135", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2593.2993, 5449.9927, 2000.0), (0.0, -179.9998975471592, 0.0), (1.0, 1.0, 1.0), "Suburbs_Column_Large_A_Shaft22_1136", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2593.2993, 5449.9927, 2000.0), (0.0, 90.00060266115494, -0.0), (1.0, 1.0, 1.0), "Suburbs_Column_Large_A_Shaft23_1137", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2593.2993, 5449.9927, 1971.9353), (0.0, 0.0002800377289519776, -0.0), (1.0, 1.0, 1.0701616), "Suburbs_Column_Large_A_Shaft24_1138", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1945.6084, 2634.3506, 1497.5), (0.0, -40.00005923828246, 0.0), (1.0, 1.0, 1.0625), "Suburbs_Column_Large_A_Shaft25_115", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1945.6084, 2634.3506, 1497.5), (0.0, -130.00002992803184, 0.0), (1.0, 1.0, 1.0625), "Suburbs_Column_Large_A_Shaft26_116", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1945.6084, 2634.3506, 1497.5), (0.0, 139.99994676084953, -0.0), (1.0, 1.0, 1.0625), "Suburbs_Column_Large_A_Shaft27_117", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1945.6084, 2634.3506, 1497.5), (0.0, 49.99981615650917, -0.0), (1.0, 1.0, 1.0625), "Suburbs_Column_Large_A_Shaft28_118", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1950.0, 3740.0, 1659.754), (0.0, 50.00005877099974, -0.0), (1.0, 1.0, 0.71875), "Suburbs_Column_Large_A_Shaft29", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1950.0, 3740.0, 1659.754), (0.0, -39.99997124769887, 0.0), (1.0, 1.0, 0.71875), "Suburbs_Column_Large_A_Shaft30", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1950.0, 3740.0, 1659.754), (0.0, -129.99999598831678, 0.0), (1.0, 1.0, 0.71875), "Suburbs_Column_Large_A_Shaft31", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1950.0, 3740.0, 1659.754), (0.0, 139.99985897116102, -0.0), (1.0, 1.0, 0.71875), "Suburbs_Column_Large_A_Shaft32", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4380.0, 2670.0, 1660.7483), (0.0, -45.000056798727684, 0.0), (1.0, 1.0, 0.71875), "Suburbs_Column_Large_A_Shaft33", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4380.0, 2670.0, 1660.7483), (0.0, -135.0000537473682, 0.0), (1.0, 1.0, 0.71875), "Suburbs_Column_Large_A_Shaft34", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4380.0, 2670.004, 1660.7483), (0.0, 134.9999263430944, -0.0), (1.0, 1.0, 0.71875), "Suburbs_Column_Large_A_Shaft35", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4380.0, 2670.0, 1660.7483), (0.0, 44.99981929321228, -0.0), (1.0, 1.0, 0.71875), "Suburbs_Column_Large_A_Shaft36", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4360.0, 3739.9995, 1660.7483), (0.0, -45.000056798727684, 0.0), (1.0, 1.0, 0.71875), "Suburbs_Column_Large_A_Shaft37", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4360.0, 3740.0, 1660.7483), (0.0, -135.0000537473682, 0.0), (1.0, 1.0, 0.71875), "Suburbs_Column_Large_A_Shaft38", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4360.0, 3740.0042, 1660.7483), (0.0, 134.9999263430944, -0.0), (1.0, 1.0, 0.71875), "Suburbs_Column_Large_A_Shaft39", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4360.0, 3740.0, 1660.7483), (0.0, 44.99981929321228, -0.0), (1.0, 1.0, 0.71875), "Suburbs_Column_Large_A_Shaft40", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4380.0, 480.0, 1660.7483), (0.0, -45.000056798727684, 0.0), (1.0, 1.0, 0.71875), "Suburbs_Column_Large_A_Shaft45", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4380.0, 480.0, 1660.7483), (0.0, -135.0000537473682, 0.0), (1.0, 1.0, 0.71875), "Suburbs_Column_Large_A_Shaft46", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4380.0, 480.0039, 1660.7483), (0.0, 134.9999263430944, -0.0), (1.0, 1.0, 0.71875), "Suburbs_Column_Large_A_Shaft47", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4380.0, 480.0, 1660.7483), (0.0, 44.99981929321228, -0.0), (1.0, 1.0, 0.71875), "Suburbs_Column_Large_A_Shaft48", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4380.0, 480.0, 1380.7483), (0.0, -45.000056798727684, 0.0), (1.0, 1.0, 0.71875), "Suburbs_Column_Large_A_Shaft49", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1945.6084, 1554.3506, 1497.5), (0.0, -40.00005923828246, 0.0), (1.0, 1.0, 1.0625), "Suburbs_Column_Large_A_Shaft5", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4380.0, 480.0, 1380.7483), (0.0, -135.0000537473682, 0.0), (1.0, 1.0, 0.71875), "Suburbs_Column_Large_A_Shaft50", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4380.0, 480.0039, 1380.7483), (0.0, 134.9999263430944, -0.0), (1.0, 1.0, 0.71875), "Suburbs_Column_Large_A_Shaft51", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4380.0, 480.0, 1380.7483), (0.0, 44.99981929321228, -0.0), (1.0, 1.0, 0.71875), "Suburbs_Column_Large_A_Shaft52", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1945.6084, 1554.3506, 1497.5), (0.0, -130.00002992803184, 0.0), (1.0, 1.0, 1.0625), "Suburbs_Column_Large_A_Shaft6", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1945.6084, 1554.3506, 1497.5), (0.0, 139.99994676084953, -0.0), (1.0, 1.0, 1.0625), "Suburbs_Column_Large_A_Shaft7", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1945.6084, 1554.3506, 1497.5), (0.0, 49.99981615650917, -0.0), (1.0, 1.0, 1.0625), "Suburbs_Column_Large_A_Shaft8", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1930.6084, 474.3506, 1497.5), (0.0, -40.00005923828246, 0.0), (1.0, 1.0, 1.0625), "Suburbs_Column_Large_A_Shaft9", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3793.3013, 5450.0015, 1542.4813), (0.0, 90.0002623402507, -0.0), (1.0, 1.0, 1.0718989), "Suburbs_Column_Large_A_Shaft9_1113", _folder)
if a: placed += 1
else: skipped += 1

# Batch 38: StaticMesh'Suburbs_Column_X_Large_A_ArchL' (19 instances)
_mesh_path = "/Game/Art/Assets/Kits/Architecture/Suburbs/Suburbs_Column_X_Large_A_ArchL"
_materials = ['/Game/Art/Assets/Kits/Architecture/Suburbs/Materials/Suburbs_Trim_Sheet_A/MI_Suburbs_Trim_Sheet_A']
_folder = "Reconstruction/BD_BB_OrcTown_Gate/Meshes"
a = spawn_static_mesh(_mesh_path, _materials, (2344.311, 3879.3525, 2662.8594), (-3.051757756716536e-05, -179.99941260373905, 0.0004371319544025748), (0.6093749, 0.28124994, 0.2929685), "Suburbs_Column_X_Large_A_Arch5_12", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4098.133, 3929.3904, 2662.8616), (0.00010245283223657324, 0.00046445278508782355, 2.0490593802391306e-05), (0.6093749, 0.28124994, 0.2929685), "Suburbs_Column_X_Large_A_Arch5_74", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2344.311, 3069.3525, 2662.8594), (-3.051757756716536e-05, -179.99941260373905, 0.0004371319544025748), (0.6093749, 0.28124994, 0.2929685), "Suburbs_Column_X_Large_A_Arch5_278", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2344.3196, 1429.3489, 2662.8494), (-3.051757756716536e-05, -179.99941260373905, 0.0004371319544025748), (0.6093749, 0.28124994, 0.2929685), "Suburbs_Column_X_Large_A_Arch5_290", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4098.13, 3109.3845, 2662.8616), (0.00010245283223662898, 0.0004644527850878113, 2.0490580051404226e-05), (0.6093749, 0.28124994, 0.2929685), "Suburbs_Column_X_Large_A_Arch5_298", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4098.1426, 1479.3845, 2662.862), (0.00010245283223662898, 0.0004644527850878113, 2.0490580051404226e-05), (0.6093749, 0.28124994, 0.2929685), "Suburbs_Column_X_Large_A_Arch5_302", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2344.3132, 2249.3525, 2662.8574), (-3.051757756716536e-05, -179.99941260373905, 0.0004371319544025748), (0.6093749, 0.28124994, 0.2929685), "Suburbs_Column_X_Large_A_Arch5_310", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2344.3323, 609.3491, 2662.8438), (-3.051757756716536e-05, -179.99941260373905, 0.0004371319544025748), (0.6093749, 0.28124994, 0.2929685), "Suburbs_Column_X_Large_A_Arch5_342", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4098.1504, 659.3845, 2662.8623), (0.00010245283223662898, 0.0004644527850878113, 2.0490580051404226e-05), (0.6093749, 0.28124994, 0.2929685), "Suburbs_Column_X_Large_A_Arch5_348", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4210.6353, 1889.4851, 2592.5503), (9.562264166108786e-05, 0.0006932642127500338, 2.0490743303387203e-05), (0.74999976, 0.54730487, 0.46875057), "Suburbs_Column_X_Large_A_Arch52_1", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4210.635, 2699.4868, 2592.55), (9.562264166108786e-05, 0.0006932642127500338, 2.0490743303387203e-05), (0.74999976, 0.54730487, 0.46875057), "Suburbs_Column_X_Large_A_Arch52_3", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4210.6284, 4339.4863, 2592.55), (9.562264166106707e-05, 0.0006932642127500366, 2.049074674113397e-05), (0.74999976, 0.54730487, 0.46875057), "Suburbs_Column_X_Large_A_Arch52_76", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2231.8452, 219.24924, 2592.5374), (-3.0517578262402215e-05, -179.99906426412394, 0.00043713201062080904), (0.74999976, 0.54730487, 0.46875057), "Suburbs_Column_X_Large_A_Arch52_111", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2231.812, 3469.2527, 2592.5508), (-3.0517578261840775e-05, -179.99906426412394, 0.00043713194186587354), (0.74999976, 0.54730487, 0.46875057), "Suburbs_Column_X_Large_A_Arch52_277", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2231.815, 2659.2493, 2592.5454), (-3.0517578261840775e-05, -179.99906426412394, 0.00043713194186587354), (0.74999976, 0.54730487, 0.46875057), "Suburbs_Column_X_Large_A_Arch52_283", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4210.628, 3519.4868, 2592.55), (9.562264166106707e-05, 0.0006932642127500366, 2.049074674113397e-05), (0.74999976, 0.54730487, 0.46875057), "Suburbs_Column_X_Large_A_Arch52_301", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2231.8325, 1839.2493, 2592.5435), (-3.0517578262402215e-05, -179.99906426412394, 0.00043713201062080904), (0.74999976, 0.54730487, 0.46875057), "Suburbs_Column_X_Large_A_Arch52_313", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2231.8452, 1019.24927, 2592.5378), (-3.0517578262402215e-05, -179.99906426412394, 0.00043713201062080904), (0.74999976, 0.54730487, 0.46875057), "Suburbs_Column_X_Large_A_Arch52_345", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4210.643, 1069.4851, 2592.5508), (9.562264166106707e-05, 0.0006932642127500366, 2.049074674113397e-05), (0.74999976, 0.54730487, 0.46875057), "Suburbs_Column_X_Large_A_Arch52_347", _folder)
if a: placed += 1
else: skipped += 1

# Batch 39: StaticMesh'Suburbs_Column_X_Large_A_ArchR' (20 instances)
_mesh_path = "/Game/Art/Assets/Kits/Architecture/Suburbs/Suburbs_Column_X_Large_A_ArchR"
_materials = ['/Game/Art/Assets/Kits/Architecture/Suburbs/Materials/Suburbs_Trim_Sheet_A/MI_Suburbs_Trim_Sheet_A']
_folder = "Reconstruction/BD_BB_OrcTown_Gate/Meshes"
a = spawn_static_mesh(_mesh_path, _materials, (4098.1406, 1476.9845, 2662.8628), (9.562264157107006e-05, 0.0005976415216043656, 2.0490590170810414e-05), (0.6093748, 0.28124994, 0.29296893), "Suburbs_Column_X_Large_A_Arch5_0", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4098.14, 2286.9868, 2662.8623), (9.562264157107006e-05, 0.0005976415216043656, 2.0490590170810414e-05), (0.6093748, 0.28124994, 0.29296893), "Suburbs_Column_X_Large_A_Arch5_2", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4098.134, 3926.9868, 2662.8623), (9.562264157107006e-05, 0.0005976415216043656, 2.0490590170810414e-05), (0.6093748, 0.28124994, 0.29296893), "Suburbs_Column_X_Large_A_Arch5_75", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2344.3384, 631.749, 2662.8528), (-3.0517577891988754e-05, -179.9991598867692, 0.0004371320360810097), (0.6093748, 0.28124994, 0.29296893), "Suburbs_Column_X_Large_A_Arch5_110", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2344.305, 3881.7524, 2662.8657), (-3.0517577891988754e-05, -179.9991598867692, 0.0004371320360810097), (0.6093748, 0.28124994, 0.29296893), "Suburbs_Column_X_Large_A_Arch5_276", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2344.3079, 3071.749, 2662.8604), (-3.0517577891988754e-05, -179.9991598867692, 0.0004371320360810097), (0.6093748, 0.28124994, 0.29296893), "Suburbs_Column_X_Large_A_Arch5_282", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4098.134, 3106.9868, 2662.8623), (9.562264157107006e-05, 0.0005976415216043656, 2.0490590170810414e-05), (0.6093748, 0.28124994, 0.29296893), "Suburbs_Column_X_Large_A_Arch5_300", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2344.3257, 2251.749, 2662.8584), (-3.0517577891988754e-05, -179.9991598867692, 0.0004371320360810097), (0.6093748, 0.28124994, 0.29296893), "Suburbs_Column_X_Large_A_Arch5_312", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2344.3384, 1431.749, 2662.8528), (-3.0517577891988754e-05, -179.9991598867692, 0.0004371320360810097), (0.6093748, 0.28124994, 0.29296893), "Suburbs_Column_X_Large_A_Arch5_344", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4098.1484, 656.98456, 2662.863), (9.562264157107006e-05, 0.0005976415216043656, 2.0490590170810414e-05), (0.6093748, 0.28124994, 0.29296893), "Suburbs_Column_X_Large_A_Arch5_346", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2231.807, 4291.848, 2592.55), (-3.0517585387976584e-05, -179.99936479259551, 0.00043713206559887655), (0.74999976, 0.547305, 0.46874934), "Suburbs_Column_X_Large_A_Arch52_13", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4210.6367, 3516.8953, 2592.5498), (0.00010245283438494039, 0.0005293396824311746, 2.049068619337355e-05), (0.74999976, 0.547305, 0.46874934), "Suburbs_Column_X_Large_A_Arch52_75", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2231.807, 3481.848, 2592.55), (-3.051758538835771e-05, -179.99936479259551, 0.00043713213435381894), (0.74999976, 0.547305, 0.46874934), "Suburbs_Column_X_Large_A_Arch52_279", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2231.8154, 1841.8444, 2592.54), (-3.051758538835771e-05, -179.99936479259551, 0.00043713213435381894), (0.74999976, 0.547305, 0.46874934), "Suburbs_Column_X_Large_A_Arch52_291", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4210.6333, 2696.8894, 2592.5498), (0.00010245283438495096, 0.0005293396824311725, 2.049068390154237e-05), (0.74999976, 0.547305, 0.46874934), "Suburbs_Column_X_Large_A_Arch52_299", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4210.646, 1066.8896, 2592.5503), (0.00010245283438495096, 0.0005293396824311725, 2.049068390154237e-05), (0.74999976, 0.547305, 0.46874934), "Suburbs_Column_X_Large_A_Arch52_303", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2231.809, 2661.848, 2592.548), (-3.0517585387976584e-05, -179.99936479259551, 0.00043713206559887655), (0.74999976, 0.547305, 0.46874934), "Suburbs_Column_X_Large_A_Arch52_311", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2231.8281, 1021.84436, 2592.5344), (-3.0517585387976584e-05, -179.99936479259551, 0.00043713206559887655), (0.74999976, 0.547305, 0.46874934), "Suburbs_Column_X_Large_A_Arch52_343", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4210.654, 246.8965, 2592.5503), (0.00010245283438495096, 0.0005293396824311725, 2.049068390154237e-05), (0.74999976, 0.547305, 0.46874934), "Suburbs_Column_X_Large_A_Arch52_349", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4210.6353, 1889.4851, 2592.5503), (9.600000728511107e-05, 0.0006929999642712555, 1.9999997846151393e-05), (0.75, 0.547305, 0.468751), "Suburbs_Column_X_Large_A_Arch53", _folder)
if a: placed += 1
else: skipped += 1

# Batch 40: StaticMesh'Suburbs_Column_X_Large_A_Base_A' (2 instances)
_mesh_path = "/Game/Art/Assets/Kits/Architecture/Suburbs/Suburbs_Column_X_Large_A_Base_A"
_materials = ['/Game/Art/Assets/Kits/Architecture/Suburbs/Materials/Suburbs_Trim_Sheet_A/MI_Suburbs_Trim_Sheet_A']
_folder = "Reconstruction/BD_BB_OrcTown_Gate/Meshes"
a = spawn_static_mesh(_mesh_path, _materials, (2443.3018, 5249.998, 1008.7899), (0.0, -179.9998975471592, 0.0), (1.0, 1.0, 1.0701616), "Suburbs_Column_X_Large_A_Base_1101", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3943.3018, 5250.0024, 1006.5316), (0.0, -89.99968865881478, 0.0), (1.0, 1.0, 1.0718989), "Suburbs_Column_X_Large_A_Base2_1102", _folder)
if a: placed += 1
else: skipped += 1

# Batch 41: StaticMesh'Suburbs_Column_X_Large_A_CapitalL' (4 instances)
_mesh_path = "/Game/Art/Assets/Kits/Architecture/Suburbs/Suburbs_Column_X_Large_A_CapitalL"
_materials = ['/Game/Art/Assets/Kits/Architecture/Suburbs/Materials/Suburbs_Trim_Sheet_A/MI_Suburbs_Trim_Sheet_A']
_folder = "Reconstruction/BD_BB_OrcTown_Gate/Meshes"
a = spawn_static_mesh(_mesh_path, _materials, (2720.0, 2580.0, 2450.0), (0.0, 90.00001925454748, -0.0), (0.71, 0.627, 0.71), "Suburbs_Column_X_Large_A_CapitalL_128", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3660.0, 2580.0, 2450.0), (0.0, 90.00001925454748, -0.0), (0.71, 0.71, 0.71), "Suburbs_Column_X_Large_A_CapitalL2", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3660.0, 2580.0, 2450.0), (0.0, -89.99999818714215, 0.0), (0.71, 0.627, 0.71), "Suburbs_Column_X_Large_A_CapitalL3", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2719.9993, 2579.9985, 2450.0), (0.0, -89.99999818714215, 0.0), (0.71, 0.71, 0.71), "Suburbs_Column_X_Large_A_CapitalL4", _folder)
if a: placed += 1
else: skipped += 1

# Batch 42: StaticMesh'Suburbs_Column_X_Large_A_CapitalL_colum_E' (7 instances)
_mesh_path = "/Game/Art/Assets/Kits/Architecture/Suburbs/Suburbs_Column_X_Large_A_CapitalL_colum_E"
_materials = ['/Game/Art/Assets/Kits/Architecture/Suburbs/Materials/Suburbs_Trim_Sheet_A/MI_Suburbs_Trim_Sheet_A']
_folder = "Reconstruction/BD_BB_OrcTown_Gate/Meshes"
a = spawn_static_mesh(_mesh_path, _materials, (4400.0015, 2722.504, 1790.0), (0.0, 0.00012207030837116422, -0.0), (0.75, 0.8125, 0.75), "Suburbs_Column_X_Large_A_Captol10", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4400.0015, 3792.504, 1790.0), (0.0, 0.00012207030837116422, -0.0), (0.75, 0.8125, 0.75), "Suburbs_Column_X_Large_A_Captol11_16", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4410.0015, 532.5039, 1790.0), (0.0, 0.00012207030837116422, -0.0), (0.75, 0.8125, 0.75), "Suburbs_Column_X_Large_A_Captol22", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1926.1216, 422.5029, 1790.0), (0.0, -179.99988388675877, 0.0), (0.75, 0.8125, 0.75), "Suburbs_Column_X_Large_A_Captol25_81", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1926.1216, 1502.5029, 1790.0), (0.0, -179.99988388675877, 0.0), (0.75, 0.8125, 0.75), "Suburbs_Column_X_Large_A_Captol27_92", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1926.1216, 2582.503, 1790.0), (0.0, -179.99988388675877, 0.0), (0.75, 0.8125, 0.75), "Suburbs_Column_X_Large_A_Captol30", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1926.1216, 3662.503, 1790.0), (0.0, -179.99988388675877, 0.0), (0.75, 0.8125, 0.75), "Suburbs_Column_X_Large_A_Captol32", _folder)
if a: placed += 1
else: skipped += 1

# Batch 43: StaticMesh'Suburbs_Column_X_Large_A_CapitalL_column_F' (14 instances)
_mesh_path = "/Game/Art/Assets/Kits/Architecture/Suburbs/Suburbs_Column_X_Large_A_CapitalL_column_F"
_materials = ['/Game/Art/Assets/Kits/Architecture/Suburbs/Materials/Suburbs_Trim_Sheet_A/MI_Suburbs_Trim_Sheet_A']
_folder = "Reconstruction/BD_BB_OrcTown_Gate/Meshes"
a = spawn_static_mesh(_mesh_path, _materials, (4400.0015, 2722.504, 1340.0), (0.0, 0.0, -0.0), (0.75, 0.8125, 0.75), "Suburbs_Column_X_Large_A_CapitalL_column_F_4", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4410.0015, 532.5039, 890.0), (0.0, 0.0, -0.0), (0.75, 0.8125, 0.75), "Suburbs_Column_X_Large_A_CapitalL_column_F10", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1926.1216, 422.5029, 1340.0), (0.0, -179.99998633961752, -0.0), (0.75, 0.8125, 0.75), "Suburbs_Column_X_Large_A_CapitalL_column_F17", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1926.1216, 422.5029, 890.0), (0.0, -179.99998633961752, -0.0), (0.75, 0.8125, 0.75), "Suburbs_Column_X_Large_A_CapitalL_column_F18", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4400.0015, 2722.504, 890.0), (0.0, 0.0, -0.0), (0.75, 0.8125, 0.75), "Suburbs_Column_X_Large_A_CapitalL_column_F2", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1926.1216, 1502.5029, 1340.0), (0.0, -179.99998633961752, -0.0), (0.75, 0.8125, 0.75), "Suburbs_Column_X_Large_A_CapitalL_column_F21", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1926.1216, 1502.5029, 890.0), (0.0, -179.99998633961752, -0.0), (0.75, 0.8125, 0.75), "Suburbs_Column_X_Large_A_CapitalL_column_F22", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1926.1216, 2582.503, 1340.0), (0.0, -179.99998633961752, -0.0), (0.75, 0.8125, 0.75), "Suburbs_Column_X_Large_A_CapitalL_column_F25", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1926.1216, 2582.503, 890.0), (0.0, -179.99998633961752, -0.0), (0.75, 0.8125, 0.75), "Suburbs_Column_X_Large_A_CapitalL_column_F26", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1926.1216, 3662.503, 1340.0), (0.0, -179.99998633961752, -0.0), (0.75, 0.8125, 0.75), "Suburbs_Column_X_Large_A_CapitalL_column_F29", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1926.1216, 3662.503, 890.0), (0.0, -179.99998633961752, -0.0), (0.75, 0.8125, 0.75), "Suburbs_Column_X_Large_A_CapitalL_column_F30", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4400.0015, 3792.504, 1340.0), (0.0, 0.0, -0.0), (0.75, 0.8125, 0.75), "Suburbs_Column_X_Large_A_CapitalL_column_F5", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4400.0015, 3792.504, 890.0), (0.0, 0.0, -0.0), (0.75, 0.8125, 0.75), "Suburbs_Column_X_Large_A_CapitalL_column_F6", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4410.0015, 532.5039, 1340.0), (0.0, 0.0, -0.0), (0.75, 0.8125, 0.75), "Suburbs_Column_X_Large_A_CapitalL_column_F9", _folder)
if a: placed += 1
else: skipped += 1

# Batch 44: StaticMesh'Suburbs_Column_X_Large_A_CapitalR1' (7 instances)
_mesh_path = "/Game/Art/Assets/Kits/Architecture/Suburbs/Suburbs_Column_X_Large_A_CapitalR1"
_materials = ['/Game/Art/Assets/Kits/Architecture/Suburbs/Materials/Suburbs_Trim_Sheet_A/MI_Suburbs_Trim_Sheet_A']
_folder = "Reconstruction/BD_BB_OrcTown_Gate/Meshes"
a = spawn_static_mesh(_mesh_path, _materials, (3660.0, 2580.0, 2450.0), (0.0, 90.00010028305118, -0.0), (0.71, 0.627, 0.71), "Suburbs_Column_X_Large_A_CapitalR1_137", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2720.0, 2580.0, 2450.0), (0.0, 90.00010028305118, -0.0), (0.71, 0.71, 0.71), "Suburbs_Column_X_Large_A_CapitalR2", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2719.9993, 2579.9985, 2450.0), (0.0, -89.99984099200987, 0.0), (0.71, 0.627, 0.71), "Suburbs_Column_X_Large_A_CapitalR3", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3660.0, 2580.0, 2450.0), (0.0, -89.99984099200987, 0.0), (0.71, 0.71, 0.71), "Suburbs_Column_X_Large_A_CapitalR4", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4400.1, 2612.5034, 1790.0), (0.0, 6.103515418554748e-05, -0.0), (0.75, 0.8125, 0.75), "Suburbs_Column_X_Large_A_Captol12", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4400.1, 3682.5034, 1790.0), (0.0, 6.103515418554748e-05, -0.0), (0.75, 0.8125, 0.75), "Suburbs_Column_X_Large_A_Captol13_18", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4590.001, 1802.5034, 1230.0), (-34.91982769522364, 10.568266898621278, -1.057616814560935), (0.75, 0.8125, 0.75), "Suburbs_Column_X_Large_A_Captol23", _folder)
if a: placed += 1
else: skipped += 1

# Batch 45: StaticMesh'Suburbs_Column_X_Large_A_CapitalR_column_E' (5 instances)
_mesh_path = "/Game/Art/Assets/Kits/Architecture/Suburbs/Suburbs_Column_X_Large_A_CapitalR_column_E"
_materials = ['/Game/Art/Assets/Kits/Architecture/Suburbs/Materials/Suburbs_Trim_Sheet_A/MI_Suburbs_Trim_Sheet_A']
_folder = "Reconstruction/BD_BB_OrcTown_Gate/Meshes"
a = spawn_static_mesh(_mesh_path, _materials, (4410.1, 422.50342, 1790.0), (0.0, 6.103515418554748e-05, -0.0), (0.75, 0.8125, 0.75), "Suburbs_Column_X_Large_A_Captol26", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1926.5, 532.5034, 1790.0), (0.0, -179.99994535848643, 0.0), (0.75, 0.8125, 0.75), "Suburbs_Column_X_Large_A_Captol28", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1926.5, 1612.5034, 1790.0), (0.0, -179.99994535848643, 0.0), (0.75, 0.8125, 0.75), "Suburbs_Column_X_Large_A_Captol29", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1926.5, 2692.5034, 1790.0), (0.0, -179.99994535848643, 0.0), (0.75, 0.8125, 0.75), "Suburbs_Column_X_Large_A_Captol31", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1926.5, 3772.5034, 1790.0), (0.0, -179.99994535848643, 0.0), (0.75, 0.8125, 0.75), "Suburbs_Column_X_Large_A_Captol33", _folder)
if a: placed += 1
else: skipped += 1

# Batch 46: StaticMesh'Suburbs_Column_X_Large_A_CapitalR_column_F' (14 instances)
_mesh_path = "/Game/Art/Assets/Kits/Architecture/Suburbs/Suburbs_Column_X_Large_A_CapitalR_column_F"
_materials = ['/Game/Art/Assets/Kits/Architecture/Suburbs/Materials/Suburbs_Trim_Sheet_A/MI_Suburbs_Trim_Sheet_A']
_folder = "Reconstruction/BD_BB_OrcTown_Gate/Meshes"
a = spawn_static_mesh(_mesh_path, _materials, (4410.0015, 422.5039, 1340.0), (0.0, 0.0, -0.0), (0.75, 0.8125, 0.75), "Suburbs_Column_X_Large_A_CapitalL_column_F11", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4410.0015, 422.5039, 890.0), (0.0, 0.0, -0.0), (0.75, 0.8125, 0.75), "Suburbs_Column_X_Large_A_CapitalL_column_F12", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1926.1216, 532.5029, 1340.0), (0.0, -179.99998633961752, -0.0), (0.75, 0.8125, 0.75), "Suburbs_Column_X_Large_A_CapitalL_column_F19", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1926.1216, 532.5029, 890.0), (0.0, -179.99998633961752, -0.0), (0.75, 0.8125, 0.75), "Suburbs_Column_X_Large_A_CapitalL_column_F20", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1926.1216, 1612.5029, 1340.0), (0.0, -179.99998633961752, -0.0), (0.75, 0.8125, 0.75), "Suburbs_Column_X_Large_A_CapitalL_column_F23", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1926.1216, 1612.5029, 890.0), (0.0, -179.99998633961752, -0.0), (0.75, 0.8125, 0.75), "Suburbs_Column_X_Large_A_CapitalL_column_F24", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1926.1216, 2692.503, 1340.0), (0.0, -179.99998633961752, -0.0), (0.75, 0.8125, 0.75), "Suburbs_Column_X_Large_A_CapitalL_column_F27", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1926.1216, 2692.503, 890.0), (0.0, -179.99998633961752, -0.0), (0.75, 0.8125, 0.75), "Suburbs_Column_X_Large_A_CapitalL_column_F28", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4400.0015, 2612.504, 1340.0), (0.0, 0.0, -0.0), (0.75, 0.8125, 0.75), "Suburbs_Column_X_Large_A_CapitalL_column_F3", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1926.1216, 3772.503, 1340.0), (0.0, -179.99998633961752, -0.0), (0.75, 0.8125, 0.75), "Suburbs_Column_X_Large_A_CapitalL_column_F31", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1926.1216, 3772.503, 890.0), (0.0, -179.99998633961752, -0.0), (0.75, 0.8125, 0.75), "Suburbs_Column_X_Large_A_CapitalL_column_F32", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4400.0015, 2612.504, 890.0), (0.0, 0.0, -0.0), (0.75, 0.8125, 0.75), "Suburbs_Column_X_Large_A_CapitalL_column_F4", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4400.0015, 3682.504, 1340.0), (0.0, 0.0, -0.0), (0.75, 0.8125, 0.75), "Suburbs_Column_X_Large_A_CapitalL_column_F7", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4400.0015, 3682.504, 890.0), (0.0, 0.0, -0.0), (0.75, 0.8125, 0.75), "Suburbs_Column_X_Large_A_CapitalL_column_F8", _folder)
if a: placed += 1
else: skipped += 1

# Batch 47: StaticMesh'Suburbs_Column_X_Large_A_Shaft' (38 instances)
_mesh_path = "/Game/Art/Assets/Kits/Architecture/Suburbs/Suburbs_Column_X_Large_A_Shaft"
_materials = ['/Game/Art/Assets/Kits/Architecture/Suburbs/Materials/Suburbs_Column_X_Large_A/MI_Suburbs_Column_X_Large_A_Shaft']
_folder = "Reconstruction/BD_BB_OrcTown_Gate/Meshes"
a = spawn_static_mesh(_mesh_path, _materials, (3498.1387, 1476.9785, 2897.2363), (-90.0, -2.726345675812131, 92.7267272657533), (0.74999976, 0.74999976, 0.46875057), "BP_Suburbs_Column_X_Large_A_Shaft22_0", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3498.1382, 2286.9807, 2897.2358), (-90.0, -2.726345675812131, 92.7267272657533), (0.74999976, 0.74999976, 0.46875057), "BP_Suburbs_Column_X_Large_A_Shaft22_2", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3498.1318, 3926.9805, 2897.2358), (-90.0, -2.202616324423668, 92.20306781516624), (0.74999976, 0.74999976, 0.46875057), "BP_Suburbs_Column_X_Large_A_Shaft22_3", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2944.3394, 631.75574, 2897.2283), (-90.0, 14.036414680862572, -104.03624852309369), (0.74999976, 0.74999976, 0.46875057), "BP_Suburbs_Column_X_Large_A_Shaft22_4", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2944.309, 4179.351, 2897.2368), (-90.0, 7.125167986968981, 262.8744137538197), (0.74999976, 0.74999976, 0.46874934), "BP_Suburbs_Column_X_Large_A_Shaft22_12", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3498.134, 3629.391, 2897.2358), (-90.0, 0.0, 90.00048701415021), (0.74999976, 0.74999976, 0.46874934), "BP_Suburbs_Column_X_Large_A_Shaft22_33", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2944.3062, 3881.7593, 2897.2412), (-90.0, 14.036414680862572, -104.03624852309369), (0.74999976, 0.74999976, 0.46875057), "BP_Suburbs_Column_X_Large_A_Shaft22_40", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2944.309, 3369.351, 2897.2368), (-90.0, 7.125167986968981, 262.8744137538197), (0.74999976, 0.74999976, 0.46874934), "BP_Suburbs_Column_X_Large_A_Shaft22_42", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2944.309, 3071.7559, 2897.2358), (-90.0, 14.036414680862572, -104.03624852309369), (0.74999976, 0.74999976, 0.46875057), "BP_Suburbs_Column_X_Large_A_Shaft22_44", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2944.3176, 1729.3478, 2897.2268), (-90.0, 7.125167986968981, 262.8744137538197), (0.74999976, 0.74999976, 0.46874934), "BP_Suburbs_Column_X_Large_A_Shaft22_46", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3498.1306, 2809.3853, 2897.2358), (-90.0, 0.0, 90.00048701415021), (0.74999976, 0.74999976, 0.46874934), "BP_Suburbs_Column_X_Large_A_Shaft22_48", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3498.1318, 3106.9807, 2897.2358), (-90.0, -2.202616324423668, 92.20306781516624), (0.74999976, 0.74999976, 0.46875057), "BP_Suburbs_Column_X_Large_A_Shaft22_50", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3498.1433, 1179.3851, 2897.2363), (-90.0, 0.0, 90.00048701415021), (0.74999976, 0.74999976, 0.46874934), "BP_Suburbs_Column_X_Large_A_Shaft22_52", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2944.3113, 2549.351, 2897.2349), (-90.0, 7.125167986968981, 262.8744137538197), (0.74999976, 0.74999976, 0.46874934), "BP_Suburbs_Column_X_Large_A_Shaft22_54", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2944.3267, 2251.7559, 2897.234), (-90.0, 14.036414680862572, -104.03624852309369), (0.74999976, 0.74999976, 0.46875057), "BP_Suburbs_Column_X_Large_A_Shaft22_56", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2944.3303, 909.34753, 2897.2212), (-90.0, 7.125167986968981, 262.8744137538197), (0.74999976, 0.74999976, 0.46874934), "BP_Suburbs_Column_X_Large_A_Shaft22_58", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2944.3394, 1431.756, 2897.2283), (-90.0, 14.036414680862572, -104.03624852309369), (0.74999976, 0.74999976, 0.46875057), "BP_Suburbs_Column_X_Large_A_Shaft22_60", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3498.1465, 656.9783, 2897.2366), (-90.0, -2.202616324423668, 92.20306781516624), (0.74999976, 0.74999976, 0.46875057), "BP_Suburbs_Column_X_Large_A_Shaft22_62", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3498.1511, 359.38522, 2897.2366), (-90.0, 0.0, 90.00048701415021), (0.74999976, 0.74999976, 0.46874934), "BP_Suburbs_Column_X_Large_A_Shaft22_64", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3760.6387, 1476.9758, 2897.2368), (-90.0, -2.726345675812131, 92.7267272657533), (0.74999976, 0.74999976, 0.46875057), "BP_Suburbs_Column_X_Large_A_Shaft40_1", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3760.6382, 2286.978, 2897.2363), (-90.0, -2.726345675812131, 92.7267272657533), (0.74999976, 0.74999976, 0.46875057), "BP_Suburbs_Column_X_Large_A_Shaft40_3", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3760.6318, 3926.978, 2897.2363), (-90.0, -2.202616324423668, 92.20306781516624), (0.74999976, 0.74999976, 0.46875057), "BP_Suburbs_Column_X_Large_A_Shaft40_4", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2681.8396, 631.75745, 2897.228), (-90.0, 14.036414680862572, -104.03624852309369), (0.74999976, 0.74999976, 0.46875057), "BP_Suburbs_Column_X_Large_A_Shaft40_5", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2681.809, 4179.354, 2897.2368), (-90.0, 7.125167986968981, 262.8744137538197), (0.74999976, 0.74999976, 0.46874934), "BP_Suburbs_Column_X_Large_A_Shaft40_13", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3760.634, 3629.388, 2897.2363), (-90.0, 0.0, 90.00048701415021), (0.74999976, 0.74999976, 0.46874934), "BP_Suburbs_Column_X_Large_A_Shaft40_34", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2681.8062, 3881.7607, 2897.241), (-90.0, 14.036414680862572, -104.03624852309369), (0.74999976, 0.74999976, 0.46875057), "BP_Suburbs_Column_X_Large_A_Shaft40_41", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2681.809, 3369.354, 2897.2368), (-90.0, 7.125167986968981, 262.8744137538197), (0.74999976, 0.74999976, 0.46874934), "BP_Suburbs_Column_X_Large_A_Shaft40_43", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2681.809, 3071.7573, 2897.2356), (-90.0, 14.036414680862572, -104.03624852309369), (0.74999976, 0.74999976, 0.46875057), "BP_Suburbs_Column_X_Large_A_Shaft40_45", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2681.8176, 1729.3503, 2897.2268), (-90.0, 7.125167986968981, 262.8744137538197), (0.74999976, 0.74999976, 0.46874934), "BP_Suburbs_Column_X_Large_A_Shaft40_47", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3760.6306, 2809.382, 2897.2363), (-90.0, 0.0, 90.00048701415021), (0.74999976, 0.74999976, 0.46874934), "BP_Suburbs_Column_X_Large_A_Shaft40_49", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3760.6318, 3106.978, 2897.2363), (-90.0, -2.202616324423668, 92.20306781516624), (0.74999976, 0.74999976, 0.46875057), "BP_Suburbs_Column_X_Large_A_Shaft40_51", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3760.6433, 1179.382, 2897.2368), (-90.0, 0.0, 90.00048701415021), (0.74999976, 0.74999976, 0.46874934), "BP_Suburbs_Column_X_Large_A_Shaft40_53", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2681.8113, 2549.354, 2897.2349), (-90.0, 7.125167986968981, 262.8744137538197), (0.74999976, 0.74999976, 0.46874934), "BP_Suburbs_Column_X_Large_A_Shaft40_55", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2681.827, 2251.7573, 2897.2336), (-90.0, 14.036414680862572, -104.03624852309369), (0.74999976, 0.74999976, 0.46875057), "BP_Suburbs_Column_X_Large_A_Shaft40_57", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2681.8303, 909.35034, 2897.2212), (-90.0, 7.125167986968981, 262.8744137538197), (0.74999976, 0.74999976, 0.46874934), "BP_Suburbs_Column_X_Large_A_Shaft40_59", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2681.8396, 1431.7573, 2897.228), (-90.0, 14.036414680862572, -104.03624852309369), (0.74999976, 0.74999976, 0.46875057), "BP_Suburbs_Column_X_Large_A_Shaft40_61", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3760.6465, 656.9757, 2897.237), (-90.0, -2.202616324423668, 92.20306781516624), (0.74999976, 0.74999976, 0.46875057), "BP_Suburbs_Column_X_Large_A_Shaft40_63", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3760.6511, 359.38208, 2897.237), (-90.0, 0.0, 90.00048701415021), (0.74999976, 0.74999976, 0.46874934), "BP_Suburbs_Column_X_Large_A_Shaft40_65", _folder)
if a: placed += 1
else: skipped += 1

# Batch 48: StaticMesh'Suburbs_Floor_35_Stairs_Cap' (5 instances)
_mesh_path = "/Game/Art/Assets/Kits/Architecture/Suburbs/Suburbs_Floor_35_Stairs_Cap"
_materials = ['/Game/Environments/ProcTexturing/GuideMeshFloor/M_GuideMeshFloor_Urban']
_folder = "Reconstruction/BD_BB_OrcTown_Gate/Meshes"
a = spawn_static_mesh(_mesh_path, _materials, (4077.7588, 2043.4868, 1097.3511), (0.0, 0.0, -0.0), (1.0, 2.125, 1.0), "Suburbs_Floor_35_Stairs_Cap_12", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4243.405, 2099.868, 1097.3511), (0.0, 0.0, -0.0), (1.0, 2.125, 1.0), "Suburbs_Floor_35_Stairs_Cap2_103", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2626.1487, 1646.4019, 1097.3511), (0.0, 0.0, -0.0), (1.90625, 4.0625, 1.0), "Suburbs_Floor_35_Stairs_Cap3", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3211.7017, 3224.4253, 1187.5854), (0.0, 0.0, -0.0), (1.90625, 4.0625, 1.0), "Suburbs_Floor_35_Stairs_Cap4", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3211.7017, 4117.664, 1187.5854), (0.0, 0.0, -0.0), (1.90625, 4.0625, 1.0), "Suburbs_Floor_35_Stairs_Cap5", _folder)
if a: placed += 1
else: skipped += 1

# Batch 49: StaticMesh'Suburbs_Floor_3x3m_A' (20 instances)
_mesh_path = "/Game/Art/Assets/Kits/Architecture/Suburbs/Suburbs_Floor_3x3m_A"
_materials = ['/Game/Art/Assets/Kits/Architecture/Suburbs/Suburbs_Floor/Materials/Subrubs_Floor_Tileable_A/MI_Suburbs_Floor_A_inst']
_folder = "Reconstruction/BD_BB_OrcTown_Gate/Meshes"
a = spawn_static_mesh(_mesh_path, _materials, (2329.5627, 1528.4553, 2664.889), (0.0, 90.00007597449323, -0.0), (0.635437, 0.635437, 0.444087), "Suburbs_Floor_3x3m_A114", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2328.5774, 524.011, 2664.889), (0.0, 0.0, -0.0), (0.635437, 0.635437, 0.444087), "Suburbs_Floor_3x3m_A121", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2329.563, 713.4553, 2664.889), (0.0, 90.00007597449323, -0.0), (0.635437, 0.635437, 0.444087), "Suburbs_Floor_3x3m_A122", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2328.5762, 2979.011, 2664.889), (0.0, 0.0, -0.0), (0.635437, 0.635437, 0.444087), "Suburbs_Floor_3x3m_A123", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2329.5618, 3168.4553, 2664.889), (0.0, 90.00007597449323, -0.0), (0.635437, 0.635437, 0.444087), "Suburbs_Floor_3x3m_A124", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2328.5752, 3789.011, 2664.889), (0.0, 0.0, -0.0), (0.635437, 0.635437, 0.444087), "Suburbs_Floor_3x3m_A125", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2329.5608, 3978.4553, 2664.889), (0.0, 90.00007597449323, -0.0), (0.635437, 0.635437, 0.444087), "Suburbs_Floor_3x3m_A126", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4115.116, 4019.5454, 2664.889), (0.0, 179.9999590188648, -0.0), (0.635437, 0.635437, 0.444087), "Suburbs_Floor_3x3m_A127", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4114.131, 3830.101, 2664.889), (0.0, -89.99999818714215, 0.0), (0.635437, 0.635437, 0.444087), "Suburbs_Floor_3x3m_A128", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4115.116, 3199.5454, 2664.889), (0.0, 179.9999590188648, -0.0), (0.635437, 0.635437, 0.444087), "Suburbs_Floor_3x3m_A129", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4114.131, 3010.101, 2664.889), (0.0, -89.99999818714215, 0.0), (0.635437, 0.635437, 0.444087), "Suburbs_Floor_3x3m_A130", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4115.116, 2574.5454, 2664.889), (0.0, 179.9999590188648, -0.0), (0.635437, 0.635437, 0.444087), "Suburbs_Floor_3x3m_A131", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4114.131, 2385.101, 2664.889), (0.0, -89.99999818714215, 0.0), (0.635437, 0.635437, 0.444087), "Suburbs_Floor_3x3m_A132", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4115.116, 1569.5454, 2664.889), (0.0, 179.9999590188648, -0.0), (0.635437, 0.635437, 0.444087), "Suburbs_Floor_3x3m_A134", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4114.131, 1380.1011, 2664.889), (0.0, -89.99999818714215, 0.0), (0.635437, 0.635437, 0.444087), "Suburbs_Floor_3x3m_A135", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4115.116, 749.5454, 2664.889), (0.0, 179.9999590188648, -0.0), (0.635437, 0.635437, 0.444087), "Suburbs_Floor_3x3m_A136", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4114.131, 560.1011, 2664.889), (0.0, -89.99999818714215, 0.0), (0.635437, 0.635437, 0.444087), "Suburbs_Floor_3x3m_A137", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2328.5767, 2154.011, 2664.889), (0.0, 0.0, -0.0), (0.635437, 0.635437, 0.444087), "Suburbs_Floor_3x3m_A17_17", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2329.5623, 2343.4553, 2664.889), (0.0, 90.00007597449323, -0.0), (0.635437, 0.635437, 0.444087), "Suburbs_Floor_3x3m_A79", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2328.5771, 1339.011, 2664.889), (0.0, 0.0, -0.0), (0.635437, 0.635437, 0.444087), "Suburbs_Floor_3x3m_A96", _folder)
if a: placed += 1
else: skipped += 1

# Batch 50: StaticMesh'Suburbs_Floor_3x9m_B' (15 instances)
_mesh_path = "/Game/Art/Assets/Kits/Architecture/Suburbs/Suburbs_Floor_3x9m_B"
_materials = ['/Game/Art/Assets/Kits/Architecture/Suburbs/Materials/Suburbs_Trim_Sheet_A/MI_Suburbs_Trim_Sheet_A', '/Game/Art/Assets/Kits/Architecture/Suburbs/Materials/Suburbs_Trim_Sheet_A/MI_Suburbs_Trim_Sheet_A']
_folder = "Reconstruction/BD_BB_OrcTown_Gate/Meshes"
a = spawn_static_mesh(_mesh_path, _materials, (2650.0, 2800.0, 1200.0), (0.0, 89.99997063746636, -0.0), (1.0, 1.0, 1.0), "Suburbs_Floor_3x9m_B_429", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2950.0, 4600.0, 1200.0), (0.0, -89.99997063746636, 0.0), (1.0, 1.0, 1.0), "Suburbs_Floor_3x9m_B10_70", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3200.0, 6050.0, 800.0), (0.0, -0.0002136230511090266, 0.0), (1.0, 1.0, 1.0), "Suburbs_Floor_3x9m_B11", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3450.0, 2800.0, 1200.0), (0.0, 89.9998815062137, -0.0), (1.0, 1.0, 1.0), "Suburbs_Floor_3x9m_B12_39", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2950.0, 2800.0, 1200.0), (0.0, -89.99999818714215, 0.0), (1.0, 1.0, 1.0), "Suburbs_Floor_3x9m_B13_41", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3450.0, 3700.0, 1200.0), (0.0, 89.9998815062137, -0.0), (1.0, 1.0, 1.0), "Suburbs_Floor_3x9m_B14", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2950.0, 3700.0, 1200.0), (0.0, -89.99999818714215, 0.0), (1.0, 1.0, 1.0), "Suburbs_Floor_3x9m_B15", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2650.0, 3700.0, 1200.0), (0.0, 89.99997063746636, -0.0), (1.0, 1.0, 1.0), "Suburbs_Floor_3x9m_B2", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2650.0, 4600.0, 1200.0), (0.0, 89.99997063746636, -0.0), (1.0, 1.0, 1.0), "Suburbs_Floor_3x9m_B3", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3750.0, 4600.0, 1200.0), (0.0, -89.99997063746636, 0.0), (1.0, 1.0, 1.0), "Suburbs_Floor_3x9m_B4", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3750.0, 3700.0, 1200.0), (0.0, -89.99997063746636, 0.0), (1.0, 1.0, 1.0), "Suburbs_Floor_3x9m_B5", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3750.0, 2800.0, 1200.0), (0.0, -89.99997063746636, 0.0), (1.0, 1.0, 1.0), "Suburbs_Floor_3x9m_B6", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2750.0, 5500.0, 1000.0), (0.0, -0.0002136230511090266, 0.0), (1.0, 1.0, 1.0), "Suburbs_Floor_3x9m_B7", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3650.0, 5500.0, 1000.0), (0.0, -0.0002136230511090266, 0.0), (1.0, 1.0, 1.0), "Suburbs_Floor_3x9m_B8", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3450.0, 4600.0, 1200.0), (0.0, 90.00011648875932, -0.0), (1.0, 1.0, 1.0), "Suburbs_Floor_3x9m_B9_68", _folder)
if a: placed += 1
else: skipped += 1

# Batch 51: StaticMesh'Suburbs_Floor_Stone_IND_A' (1 instances)
_mesh_path = "/Game/Art/Assets/Kits/Architecture/Suburbs/Suburbs_Floor_Stone_IND_A"
_materials = ['/Game/Art/Assets/Kits/Architecture/Suburbs/Materials/Suburbs_Floor_Stone_IND/MI_Suburbs_Floor_Stone_IND_MAT_Inst_Dest']
_folder = "Reconstruction/BD_BB_OrcTown_Gate/Meshes"
a = spawn_static_mesh(_mesh_path, _materials, (2820.7534, 1523.9408, 1106.3344), (0.0, 0.0, -0.0), (1.0, 1.0, 1.0), "Suburbs_Floor_Stone_IND_A_41", _folder)
if a: placed += 1
else: skipped += 1

# Batch 52: StaticMesh'Suburbs_Floor_Stone_IND_B' (1 instances)
_mesh_path = "/Game/Art/Assets/Kits/Architecture/Suburbs/Suburbs_Floor_Stone_IND_B"
_materials = ['/Game/Art/Assets/Kits/Architecture/Suburbs/Materials/Suburbs_Floor_Stone_IND/MI_Suburbs_Floor_Stone_IND_MAT_Inst_Dest']
_folder = "Reconstruction/BD_BB_OrcTown_Gate/Meshes"
a = spawn_static_mesh(_mesh_path, _materials, (4035.882, 1806.6864, 1111.5369), (0.0, -179.99976777351753, 0.0), (1.0, 1.0, 1.0), "Suburbs_Floor_Stone_IND_B8", _folder)
if a: placed += 1
else: skipped += 1

# Batch 53: StaticMesh'Suburbs_Floor_Stone_IND_C' (3 instances)
_mesh_path = "/Game/Art/Assets/Kits/Architecture/Suburbs/Suburbs_Floor_Stone_IND_C"
_materials = ['/Game/Art/Assets/Kits/Architecture/Suburbs/Materials/Suburbs_Floor_Stone_IND/MI_Suburbs_Floor_Stone_IND_MAT_Inst_Dest', '/Game/Art/Assets/Kits/Architecture/Suburbs/Materials/Suburbs_Floor_Stone_IND/MI_Suburbs_Floor_Stone_IND_MAT_Inst_Dest']
_folder = "Reconstruction/BD_BB_OrcTown_Gate/Meshes"
a = spawn_static_mesh(_mesh_path, _materials, (4843.8975, 1457.1078, 1107.6371), (0.0, 0.0, -0.0), (1.0, 1.0, 1.0), "Suburbs_Floor_Stone_IND_C_73", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4146.009, 2040.6876, 1110.5369), (0.0, -179.99976777351753, 0.0), (1.0, 1.0, 1.0), "Suburbs_Floor_Stone_IND_C10", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4237.6333, 1102.2606, 1106.3344), (0.0, 0.0, -0.0), (1.0, 1.0, 1.0), "Suburbs_Floor_Stone_IND_C2_102", _folder)
if a: placed += 1
else: skipped += 1

# Batch 54: StaticMesh'Suburbs_Floor_Stone_IND_D' (2 instances)
_mesh_path = "/Game/Art/Assets/Kits/Architecture/Suburbs/Suburbs_Floor_Stone_IND_D"
_materials = ['/Game/Art/Assets/Kits/Architecture/Suburbs/Materials/Suburbs_Floor_Stone_IND/MI_Suburbs_Floor_Stone_IND_MAT_Inst_Dest']
_folder = "Reconstruction/BD_BB_OrcTown_Gate/Meshes"
a = spawn_static_mesh(_mesh_path, _materials, (3849.5867, 1126.9597, 1106.3342), (0.0, 0.0, -0.0), (1.0, 1.0, 1.0), "Suburbs_Floor_Stone_IND_D_111", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2619.4404, 1408.1682, 1106.3345), (0.0, 0.0, -0.0), (1.0, 1.0, 1.0), "Suburbs_Floor_Stone_IND_D2_35", _folder)
if a: placed += 1
else: skipped += 1

# Batch 55: StaticMesh'Suburbs_Floor_Stone_IND_E' (3 instances)
_mesh_path = "/Game/Art/Assets/Kits/Architecture/Suburbs/Suburbs_Floor_Stone_IND_E"
_materials = ['/Game/Art/Assets/Kits/Architecture/Suburbs/Materials/Suburbs_Floor_Stone_IND/MI_Suburbs_Floor_Stone_IND_MAT_Inst_Dest']
_folder = "Reconstruction/BD_BB_OrcTown_Gate/Meshes"
a = spawn_static_mesh(_mesh_path, _materials, (4762.8184, 1514.2684, 1110.0658), (0.0, 0.0, -0.0), (1.0, 1.0, 1.0), "Suburbs_Floor_Stone_IND_E_70", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4002.7556, 1077.5016, 1109.0698), (0.0, 0.0, -0.0), (1.0, 1.0, 1.0), "Suburbs_Floor_Stone_IND_E2_114", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2747.0334, 1294.4673, 1107.6877), (0.0, 0.0, -0.0), (1.0, 1.0, 1.0), "Suburbs_Floor_Stone_IND_E3_29", _folder)
if a: placed += 1
else: skipped += 1

# Batch 56: StaticMesh'Suburbs_Floor_Stone_IND_F' (7 instances)
_mesh_path = "/Game/Art/Assets/Kits/Architecture/Suburbs/Suburbs_Floor_Stone_IND_F"
_materials = ['/Game/Art/Assets/Kits/Architecture/Suburbs/Materials/Suburbs_Floor_Stone_IND/MI_Suburbs_Floor_Stone_IND_MAT_Inst_Dest']
_folder = "Reconstruction/BD_BB_OrcTown_Gate/Meshes"
a = spawn_static_mesh(_mesh_path, _materials, (4641.412, 1450.0, 1110.0), (0.0, 0.0, -0.0), (1.0, 1.0, 1.0), "Suburbs_Floor_Stone_IND_F_67", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3941.7014, 1254.0067, 1106.4958), (0.0, 65.00006093247498, -0.0), (1.0, 1.0, 1.0), "Suburbs_Floor_Stone_IND_F2_105", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3822.462, 1365.3778, 1105.4907), (0.0, -4.999938748570566, 0.0), (1.0, 1.0, 1.0), "Suburbs_Floor_Stone_IND_F3", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4023.9966, 1208.5636, 1106.919), (0.0, 75.00011048257807, -0.0), (1.0, 1.0, 1.0), "Suburbs_Floor_Stone_IND_F4", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3773.7737, 1608.3711, 1105.4907), (0.0, -4.999938748570566, 0.0), (1.0, 1.0, 1.0), "Suburbs_Floor_Stone_IND_F5_120", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2897.5723, 1356.5651, 1106.4957), (0.0, 65.00006093247498, -0.0), (1.0, 1.0, 1.0), "Suburbs_Floor_Stone_IND_F6", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2516.4866, 1341.2472, 1106.3344), (0.0, 0.0, -0.0), (1.0, 1.0, 1.0), "Suburbs_Floor_Stone_IND_F7_32", _folder)
if a: placed += 1
else: skipped += 1

# Batch 57: StaticMesh'Suburbs_Floor_Trim_A_2m' (40 instances)
_mesh_path = "/Game/Art/Assets/Kits/Architecture/Suburbs/Suburbs_Floor_Trim_A_2m"
_materials = ['/Game/Art/Assets/Kits/Architecture/Suburbs/Materials/Suburbs_Floor_A/MI_Suburbs_Floor_A_2_Inst']
_folder = "Reconstruction/BD_BB_OrcTown_Gate/Meshes"
a = spawn_static_mesh(_mesh_path, _materials, (2425.5627, 1435.4551, 2664.889), (0.0, 0.00018200000924614436, -0.0), (0.635437, 0.644615, 0.444087), "Suburbs_Floor_Trim_A_Corner_Int11", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2362.5627, 1627.456, 2664.889), (0.0, 90.00029475174199, -0.0), (0.635437, 0.644615, 0.444087), "Suburbs_Floor_Trim_A_Corner_Int12", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2235.5774, 428.011, 2664.889), (0.0, -90.00002735739477, 0.0), (0.635437, 0.644615, 0.444087), "Suburbs_Floor_Trim_A_Corner_Int14", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2427.5774, 491.011, 2664.889), (0.0, 0.0001460000052764277, -0.0), (0.635437, 0.644615, 0.444087), "Suburbs_Floor_Trim_A_Corner_Int15", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2425.563, 620.4551, 2664.889), (0.0, 0.00018200000924614436, -0.0), (0.635437, 0.644615, 0.444087), "Suburbs_Floor_Trim_A_Corner_Int17", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2362.563, 812.45605, 2664.889), (0.0, 90.00029475174199, -0.0), (0.635437, 0.644615, 0.444087), "Suburbs_Floor_Trim_A_Corner_Int18", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2235.5767, 2058.011, 2664.889), (0.0, -90.00002735739477, 0.0), (0.635437, 0.6446145, 0.444087), "Suburbs_Floor_Trim_A_Corner_Int2", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2235.5762, 2883.011, 2664.889), (0.0, -90.00002735739477, 0.0), (0.635437, 0.644615, 0.444087), "Suburbs_Floor_Trim_A_Corner_Int20", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2427.5762, 2946.011, 2664.889), (0.0, 0.0001460000052764277, -0.0), (0.635437, 0.644615, 0.444087), "Suburbs_Floor_Trim_A_Corner_Int21", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2425.5618, 3075.455, 2664.889), (0.0, 0.00018200000924614436, -0.0), (0.635437, 0.644615, 0.444087), "Suburbs_Floor_Trim_A_Corner_Int23", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2362.5618, 3267.456, 2664.889), (0.0, 90.00029475174199, -0.0), (0.635437, 0.644615, 0.444087), "Suburbs_Floor_Trim_A_Corner_Int24", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2235.5752, 3693.011, 2664.889), (0.0, -90.00002735739477, 0.0), (0.635437, 0.644615, 0.444087), "Suburbs_Floor_Trim_A_Corner_Int26", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2427.5752, 3756.011, 2664.889), (0.0, 0.0001460000052764277, -0.0), (0.635437, 0.644615, 0.444087), "Suburbs_Floor_Trim_A_Corner_Int27", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2425.5608, 3885.455, 2664.889), (0.0, 0.00018200000924614436, -0.0), (0.635437, 0.644615, 0.444087), "Suburbs_Floor_Trim_A_Corner_Int29", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2427.5767, 2121.011, 2664.889), (0.0, 0.00014638900924185514, -0.0), (0.635437, 0.644615, 0.444087), "Suburbs_Floor_Trim_A_Corner_Int3", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2362.5608, 4077.456, 2664.889), (0.0, 90.00029475174199, -0.0), (0.635437, 0.644615, 0.444087), "Suburbs_Floor_Trim_A_Corner_Int30", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4208.1167, 4115.5454, 2664.889), (0.0, 89.99993822608693, -0.0), (0.635437, 0.644615, 0.444087), "Suburbs_Floor_Trim_A_Corner_Int32", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4016.1167, 4052.546, 2664.889), (0.0, -179.9998360754275, 0.0), (0.635437, 0.644615, 0.444087), "Suburbs_Floor_Trim_A_Corner_Int33", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4018.1304, 3923.102, 2664.889), (0.0, -179.9998360754275, 0.0), (0.635437, 0.644615, 0.444087), "Suburbs_Floor_Trim_A_Corner_Int35", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4081.1304, 3731.1006, 2664.889), (0.0, -89.99975996369572, 0.0), (0.635437, 0.644615, 0.444087), "Suburbs_Floor_Trim_A_Corner_Int36", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4208.1167, 3295.5454, 2664.889), (0.0, 89.99993822608693, -0.0), (0.635437, 0.644615, 0.444087), "Suburbs_Floor_Trim_A_Corner_Int38", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4016.1167, 3232.546, 2664.889), (0.0, -179.9998360754275, 0.0), (0.635437, 0.644615, 0.444087), "Suburbs_Floor_Trim_A_Corner_Int39", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4018.1304, 3103.102, 2664.889), (0.0, -179.9998360754275, 0.0), (0.635437, 0.644615, 0.444087), "Suburbs_Floor_Trim_A_Corner_Int41", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4081.1304, 2911.1006, 2664.889), (0.0, -89.99975996369572, 0.0), (0.635437, 0.644615, 0.444087), "Suburbs_Floor_Trim_A_Corner_Int42", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4208.1167, 2670.5454, 2664.889), (0.0, 89.99993822608693, -0.0), (0.635437, 0.644615, 0.444087), "Suburbs_Floor_Trim_A_Corner_Int44", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4016.1167, 2607.546, 2664.889), (0.0, -179.9998360754275, 0.0), (0.635437, 0.644615, 0.444087), "Suburbs_Floor_Trim_A_Corner_Int45", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4018.1304, 2478.102, 2664.889), (0.0, -179.9998360754275, 0.0), (0.635437, 0.644615, 0.444087), "Suburbs_Floor_Trim_A_Corner_Int47", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4081.1304, 2286.1006, 2664.889), (0.0, -89.99975996369572, 0.0), (0.635437, 0.644615, 0.444087), "Suburbs_Floor_Trim_A_Corner_Int48", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2425.5623, 2250.455, 2664.889), (0.0, 0.0001816749588298091, -0.0), (0.635437, 0.644615, 0.444087), "Suburbs_Floor_Trim_A_Corner_Int5", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4208.1167, 1665.5454, 2664.889), (0.0, 89.99993822608693, -0.0), (0.635437, 0.644615, 0.444087), "Suburbs_Floor_Trim_A_Corner_Int50", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4016.1167, 1602.5459, 2664.889), (0.0, -179.9998360754275, 0.0), (0.635437, 0.644615, 0.444087), "Suburbs_Floor_Trim_A_Corner_Int51", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4018.1304, 1473.102, 2664.889), (0.0, -179.9998360754275, 0.0), (0.635437, 0.644615, 0.444087), "Suburbs_Floor_Trim_A_Corner_Int53", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4081.1304, 1281.1006, 2664.889), (0.0, -89.99975996369572, 0.0), (0.635437, 0.644615, 0.444087), "Suburbs_Floor_Trim_A_Corner_Int54", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4208.1167, 845.5454, 2664.889), (0.0, 89.99993822608693, -0.0), (0.635437, 0.644615, 0.444087), "Suburbs_Floor_Trim_A_Corner_Int56", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4016.1167, 782.5459, 2664.889), (0.0, -179.9998360754275, 0.0), (0.635437, 0.644615, 0.444087), "Suburbs_Floor_Trim_A_Corner_Int57", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4018.1304, 653.10205, 2664.889), (0.0, -179.9998360754275, 0.0), (0.635437, 0.644615, 0.444087), "Suburbs_Floor_Trim_A_Corner_Int59", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2362.5623, 2442.456, 2664.889), (0.0, 90.00029475174199, -0.0), (0.635437, 0.644615, 0.444087), "Suburbs_Floor_Trim_A_Corner_Int6", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4081.1304, 461.1006, 2664.889), (0.0, -89.99975996369572, 0.0), (0.635437, 0.644615, 0.444087), "Suburbs_Floor_Trim_A_Corner_Int60", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2235.5771, 1243.011, 2664.889), (0.0, -90.00002735739477, 0.0), (0.635437, 0.644615, 0.444087), "Suburbs_Floor_Trim_A_Corner_Int8", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2427.5771, 1306.011, 2664.889), (0.0, 0.0001460000052764277, -0.0), (0.635437, 0.644615, 0.444087), "Suburbs_Floor_Trim_A_Corner_Int9", _folder)
if a: placed += 1
else: skipped += 1

# Batch 58: StaticMesh'Suburbs_Floor_Trim_A_Corner_Int' (20 instances)
_mesh_path = "/Game/Art/Assets/Kits/Architecture/Suburbs/Suburbs_Floor_Trim_A_Corner_Int"
_materials = ['/Game/Art/Assets/Kits/Architecture/Suburbs/Materials/Suburbs_Floor_A/MI_Suburbs_Floor_A_2_Inst']
_folder = "Reconstruction/BD_BB_OrcTown_Gate/Meshes"
a = spawn_static_mesh(_mesh_path, _materials, (2363.5767, 2058.011, 2664.889), (0.0, -90.00002735739477, 0.0), (0.635437, 0.635437, 0.444087), "Suburbs_Floor_Trim_A_Corner_Int_8", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2425.5627, 1563.4563, 2664.889), (0.0, 0.00018200000924614436, -0.0), (0.635437, 0.635437, 0.444087), "Suburbs_Floor_Trim_A_Corner_Int10", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2363.5774, 428.011, 2664.889), (0.0, -90.00002735739477, 0.0), (0.635437, 0.635437, 0.444087), "Suburbs_Floor_Trim_A_Corner_Int13", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2425.563, 748.4563, 2664.889), (0.0, 0.00018200000924614436, -0.0), (0.635437, 0.635437, 0.444087), "Suburbs_Floor_Trim_A_Corner_Int16", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2363.5762, 2883.011, 2664.889), (0.0, -90.00002735739477, 0.0), (0.635437, 0.635437, 0.444087), "Suburbs_Floor_Trim_A_Corner_Int19", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2425.5618, 3203.4563, 2664.889), (0.0, 0.00018200000924614436, -0.0), (0.635437, 0.635437, 0.444087), "Suburbs_Floor_Trim_A_Corner_Int22", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2363.5752, 3693.011, 2664.889), (0.0, -90.00002735739477, 0.0), (0.635437, 0.635437, 0.444087), "Suburbs_Floor_Trim_A_Corner_Int25", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2425.5608, 4013.4563, 2664.889), (0.0, 0.00018200000924614436, -0.0), (0.635437, 0.635437, 0.444087), "Suburbs_Floor_Trim_A_Corner_Int28", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4080.1165, 4115.546, 2664.889), (0.0, 89.99993822608693, -0.0), (0.635437, 0.635437, 0.444087), "Suburbs_Floor_Trim_A_Corner_Int31", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4018.1306, 3795.1006, 2664.889), (0.0, -179.9998360754275, 0.0), (0.635437, 0.635437, 0.444087), "Suburbs_Floor_Trim_A_Corner_Int34", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4080.1165, 3295.546, 2664.889), (0.0, 89.99993822608693, -0.0), (0.635437, 0.635437, 0.444087), "Suburbs_Floor_Trim_A_Corner_Int37", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2425.5623, 2378.4563, 2664.889), (0.0, 0.0001816749588298091, -0.0), (0.635437, 0.635437, 0.444087), "Suburbs_Floor_Trim_A_Corner_Int4", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4018.1306, 2975.1006, 2664.889), (0.0, -179.9998360754275, 0.0), (0.635437, 0.635437, 0.444087), "Suburbs_Floor_Trim_A_Corner_Int40", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4080.1165, 2670.546, 2664.889), (0.0, 89.99993822608693, -0.0), (0.635437, 0.635437, 0.444087), "Suburbs_Floor_Trim_A_Corner_Int43", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4018.1306, 2350.1006, 2664.889), (0.0, -179.9998360754275, 0.0), (0.635437, 0.635437, 0.444087), "Suburbs_Floor_Trim_A_Corner_Int46", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4080.1165, 1665.5459, 2664.889), (0.0, 89.99993822608693, -0.0), (0.635437, 0.635437, 0.444087), "Suburbs_Floor_Trim_A_Corner_Int49", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4018.1306, 1345.1006, 2664.889), (0.0, -179.9998360754275, 0.0), (0.635437, 0.635437, 0.444087), "Suburbs_Floor_Trim_A_Corner_Int52", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4080.1165, 845.5459, 2664.889), (0.0, 89.99993822608693, -0.0), (0.635437, 0.635437, 0.444087), "Suburbs_Floor_Trim_A_Corner_Int55", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4018.1306, 525.1006, 2664.889), (0.0, -179.9998360754275, 0.0), (0.635437, 0.635437, 0.444087), "Suburbs_Floor_Trim_A_Corner_Int58", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2363.5771, 1243.011, 2664.889), (0.0, -90.00002735739477, 0.0), (0.635437, 0.635437, 0.444087), "Suburbs_Floor_Trim_A_Corner_Int7", _folder)
if a: placed += 1
else: skipped += 1

# Batch 59: StaticMesh'Suburbs_Gate_A_Arch' (2 instances)
_mesh_path = "/Game/Art/Assets/Kits/Architecture/Suburbs/Suburbs_Gate_A_Arch"
_materials = ['/Game/Art/Assets/Kits/Architecture/Suburbs/Materials/Suburbs_Trim_Sheet_A/MI_Suburbs_Trim_Sheet_A']
_folder = "Reconstruction/BD_BB_OrcTown_Gate/Meshes"
a = spawn_static_mesh(_mesh_path, _materials, (2661.544, 4222.1772, 2027.4585), (0.0, 0.00012207030837116422, -0.0), (1.65625, 1.65625, 1.65625), "Suburbs_Gate_A_Pillar_Base77", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3741.544, 4392.1772, 2027.4585), (0.0, -179.99988388675877, 0.0), (1.65625, 1.65625, 1.65625), "Suburbs_Gate_A_Pillar_Base81_1", _folder)
if a: placed += 1
else: skipped += 1

# Batch 60: StaticMesh'Suburbs_Gate_A_Pillar_Base' (4 instances)
_mesh_path = "/Game/Art/Assets/Kits/Architecture/Suburbs/Suburbs_Gate_A_Pillar_Base"
_materials = ['/Game/Art/Assets/Kits/Architecture/Suburbs/Materials/Suburbs_Trim_Sheet_A/MI_Suburbs_Trim_Sheet_A']
_folder = "Reconstruction/BD_BB_OrcTown_Gate/Meshes"
a = spawn_static_mesh(_mesh_path, _materials, (2827.171, 4387.799, 1199.3333), (0.0, 179.9998975471592, -0.0), (1.65625, 1.65625, 1.65625), "Suburbs_Gate_A_Pillar_Base74", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3572.4849, 4387.799, 1199.3333), (0.0, 179.9998975471592, -0.0), (1.65625, 1.65625, 1.65625), "Suburbs_Gate_A_Pillar_Base78", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2827.171, 4387.799, 2027.4585), (0.0, 179.9998975471592, -0.0), (1.65625, 1.65625, 1.65625), "Suburbs_Gate_A_Pillar_Base82", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3572.4849, 4387.799, 2027.4585), (0.0, 179.9998975471592, -0.0), (1.65625, 1.65625, 1.65625), "Suburbs_Gate_A_Pillar_Base84", _folder)
if a: placed += 1
else: skipped += 1

# Batch 61: StaticMesh'Suburbs_Gate_A_Pillar_Capitol' (4 instances)
_mesh_path = "/Game/Art/Assets/Kits/Architecture/Suburbs/Suburbs_Gate_A_Pillar_Capitol"
_materials = ['/Game/Art/Assets/Kits/Architecture/Suburbs/Materials/Suburbs_Trim_Sheet_A/MI_Suburbs_Trim_Sheet_A']
_folder = "Reconstruction/BD_BB_OrcTown_Gate/Meshes"
a = spawn_static_mesh(_mesh_path, _materials, (2827.171, 4387.799, 2027.4585), (0.0, 179.9998975471592, -0.0), (1.65625, 1.65625, 1.65625), "Suburbs_Gate_A_Pillar_Base76", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3572.4849, 4387.799, 2027.4585), (0.0, 179.9998975471592, -0.0), (1.65625, 1.65625, 1.65625), "Suburbs_Gate_A_Pillar_Base80", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2827.171, 4387.799, 2689.961), (0.0, 179.9998975471592, -0.0), (1.65625, 1.65625, 1.65625), "Suburbs_Gate_A_Pillar_Base83", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3572.4849, 4387.799, 2689.961), (0.0, 179.9998975471592, -0.0), (1.65625, 1.65625, 1.65625), "Suburbs_Gate_A_Pillar_Base85", _folder)
if a: placed += 1
else: skipped += 1

# Batch 62: StaticMesh'Suburbs_Gate_A_Pillar_Shaft' (2 instances)
_mesh_path = "/Game/Art/Assets/Kits/Architecture/Suburbs/Suburbs_Gate_A_Pillar_Shaft"
_materials = ['/Game/Art/Assets/Kits/Architecture/Suburbs/Materials/Suburbs_Trim_Sheet_A/MI_Suburbs_Trim_Sheet_A']
_folder = "Reconstruction/BD_BB_OrcTown_Gate/Meshes"
a = spawn_static_mesh(_mesh_path, _materials, (2827.171, 4387.799, 1696.2085), (0.0, 179.9998975471592, -0.0), (1.65625, 1.65625, 1.65625), "Suburbs_Gate_A_Pillar_Base75", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3572.4849, 4387.799, 1696.2085), (0.0, 179.9998975471592, -0.0), (1.65625, 1.65625, 1.65625), "Suburbs_Gate_A_Pillar_Base79", _folder)
if a: placed += 1
else: skipped += 1

# Batch 63: StaticMesh'Suburbs_Gate_Side_Trim_3M_A' (16 instances)
_mesh_path = "/Game/Art/Assets/Kits/Architecture/Suburbs/Suburbs_Gate_Side_Trim_3M_A"
_materials = ['/Game/Art/Assets/Kits/Architecture/Suburbs/Materials/Suburbs_Wall/MI_Suburbs_Wall_Tile_A_Inst', '/Game/Art/Assets/Kits/Architecture/Suburbs/Materials/Suburbs_Gate_A_Sides/MI_Suburbs_Gate_A_Sides_Trim_A_Inst']
_folder = "Reconstruction/BD_BB_OrcTown_Gate/Meshes"
a = spawn_static_mesh(_mesh_path, _materials, (2710.0, 4270.0, 2597.0), (0.0, 179.99976777355934, -0.0), (1.0, 1.0, 1.0), "Suburbs_Gate_Side_Trim_3M_A32", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2410.0, 4270.0, 2597.0), (0.0, 179.99976777355934, -0.0), (1.0, 1.0, 1.0), "Suburbs_Gate_Side_Trim_3M_A33", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3800.0, 4270.0, 2597.0), (0.0, 179.99976777355934, -0.0), (1.0, 1.0, 1.0), "Suburbs_Gate_Side_Trim_3M_A35", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4100.0, 4270.0, 2597.0), (0.0, 179.99976777355934, -0.0), (1.0, 1.0, 1.0), "Suburbs_Gate_Side_Trim_3M_A36", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3500.0005, 4509.998, 2577.0), (0.0, -0.0002441406282020384, 0.0), (1.0, 1.0, 1.0), "Suburbs_Gate_Side_Trim_3M_A38", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3800.001, 4509.995, 2577.0), (0.0, -0.0002441406282020384, 0.0), (1.0, 1.0, 1.0), "Suburbs_Gate_Side_Trim_3M_A39", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2600.0015, 4510.0, 2577.0), (0.0, -0.0002441406282020384, 0.0), (1.0, 1.0, 1.0), "Suburbs_Gate_Side_Trim_3M_A41", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2300.001, 4510.0, 2577.0), (0.0, -0.0002441406282020384, 0.0), (1.0, 1.0, 1.0), "Suburbs_Gate_Side_Trim_3M_A42", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2900.0, 2480.0, 2597.0), (0.0, 179.99976777355934, -0.0), (1.0, 1.0, 1.0), "Suburbs_Gate_Side_Trim_3M_A44", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2600.0, 2480.0, 2597.0), (0.0, 179.99976777355934, -0.0), (1.0, 1.0, 1.0), "Suburbs_Gate_Side_Trim_3M_A45", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3800.0, 2480.0, 2597.0), (0.0, 179.99976777355934, -0.0), (1.0, 1.0, 1.0), "Suburbs_Gate_Side_Trim_3M_A47", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4100.0, 2480.0, 2597.0), (0.0, 179.99976777355934, -0.0), (1.0, 1.0, 1.0), "Suburbs_Gate_Side_Trim_3M_A48", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3500.0005, 2679.9978, 2597.0), (0.0, -0.0002441406282020384, 0.0), (1.0, 1.0, 1.0), "Suburbs_Gate_Side_Trim_3M_A50", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3800.001, 2679.9954, 2597.0), (0.0, -0.0002441406282020384, 0.0), (1.0, 1.0, 1.0), "Suburbs_Gate_Side_Trim_3M_A51", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2600.0015, 2679.9998, 2597.0), (0.0, -0.0002441406282020384, 0.0), (1.0, 1.0, 1.0), "Suburbs_Gate_Side_Trim_3M_A53", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2300.001, 2679.9998, 2597.0), (0.0, -0.0002441406282020384, 0.0), (1.0, 1.0, 1.0), "Suburbs_Gate_Side_Trim_3M_A54", _folder)
if a: placed += 1
else: skipped += 1

# Batch 64: StaticMesh'Suburbs_Gate_Trim_A_2m' (40 instances)
_mesh_path = "/Game/Art/Assets/Kits/Architecture/Suburbs/Suburbs_Gate_Trim_A_2m"
_materials = ['/Game/Art/Assets/Kits/Architecture/Suburbs/Materials/Suburbs_Trim_A_2m/MI_Suburbs_Gate_Trim_B']
_folder = "Reconstruction/BD_BB_OrcTown_Gate/Meshes"
a = spawn_static_mesh(_mesh_path, _materials, (2361.3394, 2076.0, 2595.0), (0.0, 179.99986339621609, -0.0), (0.631388, 0.5192338, 0.6657982), "Suburbs_Gate_Trim_A_2m_2", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2407.5732, 1561.2185, 2595.0), (0.0, -89.99991067642716, 0.0), (0.631388, 0.519234, 0.665798), "Suburbs_Gate_Trim_A_2m10", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2233.365, 1607.5557, 2595.0), (0.0, 0.00019799999318513147, -0.0), (0.631388, 0.519234, 0.665798), "Suburbs_Gate_Trim_A_2m12", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2361.34, 446.0, 2595.0), (0.0, 179.99986339621609, -0.0), (0.631388, 0.519234, 0.665798), "Suburbs_Gate_Trim_A_2m13", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2407.6777, 620.20874, 2595.0), (0.0, -89.99999818714215, 0.0), (0.631388, 0.519234, 0.665798), "Suburbs_Gate_Trim_A_2m15", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2407.5735, 746.2185, 2595.0), (0.0, -89.99991067642716, 0.0), (0.631388, 0.519234, 0.665798), "Suburbs_Gate_Trim_A_2m16", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2233.3652, 792.55566, 2595.0), (0.0, 0.00019799999318513147, -0.0), (0.631388, 0.519234, 0.665798), "Suburbs_Gate_Trim_A_2m18", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2361.3389, 2901.0, 2595.0), (0.0, 179.99986339621609, -0.0), (0.631388, 0.519234, 0.665798), "Suburbs_Gate_Trim_A_2m19", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2407.6765, 3075.2087, 2595.0), (0.0, -89.99999818714215, 0.0), (0.631388, 0.519234, 0.665798), "Suburbs_Gate_Trim_A_2m21", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2407.5723, 3201.2185, 2595.0), (0.0, -89.99991067642716, 0.0), (0.631388, 0.519234, 0.665798), "Suburbs_Gate_Trim_A_2m22", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2233.364, 3247.5557, 2595.0), (0.0, 0.00019799999318513147, -0.0), (0.631388, 0.519234, 0.665798), "Suburbs_Gate_Trim_A_2m24", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2361.338, 3711.0, 2595.0), (0.0, 179.99986339621609, -0.0), (0.631388, 0.519234, 0.665798), "Suburbs_Gate_Trim_A_2m25", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2407.6755, 3885.2087, 2595.0), (0.0, -89.99999818714215, 0.0), (0.631388, 0.519234, 0.665798), "Suburbs_Gate_Trim_A_2m27", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2407.5713, 4011.2185, 2595.0), (0.0, -89.99991067642716, 0.0), (0.631388, 0.519234, 0.665798), "Suburbs_Gate_Trim_A_2m28", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2407.677, 2250.2087, 2595.0), (0.0, -89.99999818714215, 0.0), (0.631388, 0.519234, 0.665798), "Suburbs_Gate_Trim_A_2m3", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2233.363, 4057.5557, 2595.0), (0.0, 0.00019799999318513147, -0.0), (0.631388, 0.519234, 0.665798), "Suburbs_Gate_Trim_A_2m30", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4082.3538, 4097.5566, 2595.0), (0.0, -0.00030517577092912265, 0.0), (0.631388, 0.519234, 0.665798), "Suburbs_Gate_Trim_A_2m31", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4036.016, 3923.3484, 2595.0), (0.0, 89.99999818714215, -0.0), (0.631388, 0.519234, 0.665798), "Suburbs_Gate_Trim_A_2m33", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4036.12, 3797.338, 2595.0), (0.0, 90.0001164887758, -0.0), (0.631388, 0.519234, 0.665798), "Suburbs_Gate_Trim_A_2m34", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4210.3276, 3751.001, 2595.0), (0.0, -179.99980192457332, 0.0), (0.631388, 0.519234, 0.665798), "Suburbs_Gate_Trim_A_2m36", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4082.3538, 3277.5566, 2595.0), (0.0, -0.00030517577092912265, 0.0), (0.631388, 0.519234, 0.665798), "Suburbs_Gate_Trim_A_2m37", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4036.016, 3103.3484, 2595.0), (0.0, 89.99999818714215, -0.0), (0.631388, 0.519234, 0.665798), "Suburbs_Gate_Trim_A_2m39", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2407.5728, 2376.2185, 2595.0), (0.0, -89.99991067642716, 0.0), (0.631388, 0.519234, 0.665798), "Suburbs_Gate_Trim_A_2m4", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4036.12, 2977.338, 2595.0), (0.0, 90.0001164887758, -0.0), (0.631388, 0.519234, 0.665798), "Suburbs_Gate_Trim_A_2m40", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4210.3276, 2931.001, 2595.0), (0.0, -179.99980192457332, 0.0), (0.631388, 0.519234, 0.665798), "Suburbs_Gate_Trim_A_2m42", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4082.3538, 2652.5566, 2595.0), (0.0, -0.00030517577092912265, 0.0), (0.631388, 0.519234, 0.665798), "Suburbs_Gate_Trim_A_2m43", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4036.016, 2478.3484, 2595.0), (0.0, 89.99999818714215, -0.0), (0.631388, 0.519234, 0.665798), "Suburbs_Gate_Trim_A_2m45", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4036.12, 2352.338, 2595.0), (0.0, 90.0001164887758, -0.0), (0.631388, 0.519234, 0.665798), "Suburbs_Gate_Trim_A_2m46", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4210.3276, 2306.001, 2595.0), (0.0, -179.99980192457332, 0.0), (0.631388, 0.519234, 0.665798), "Suburbs_Gate_Trim_A_2m48", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4082.3538, 1647.5566, 2595.0), (0.0, -0.00030517577092912265, 0.0), (0.631388, 0.519234, 0.665798), "Suburbs_Gate_Trim_A_2m49", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4036.016, 1473.3484, 2595.0), (0.0, 89.99999818714215, -0.0), (0.631388, 0.519234, 0.665798), "Suburbs_Gate_Trim_A_2m51", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4036.12, 1347.3379, 2595.0), (0.0, 90.0001164887758, -0.0), (0.631388, 0.519234, 0.665798), "Suburbs_Gate_Trim_A_2m52", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4210.3276, 1301.001, 2595.0), (0.0, -179.99980192457332, 0.0), (0.631388, 0.519234, 0.665798), "Suburbs_Gate_Trim_A_2m54", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4082.3538, 827.55664, 2595.0), (0.0, -0.00030517577092912265, 0.0), (0.631388, 0.519234, 0.665798), "Suburbs_Gate_Trim_A_2m55", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4036.016, 653.3484, 2595.0), (0.0, 89.99999818714215, -0.0), (0.631388, 0.519234, 0.665798), "Suburbs_Gate_Trim_A_2m57", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4036.12, 527.3379, 2595.0), (0.0, 90.0001164887758, -0.0), (0.631388, 0.519234, 0.665798), "Suburbs_Gate_Trim_A_2m58", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2233.3645, 2422.5557, 2595.0), (0.0, 0.00019788741843754348, -0.0), (0.631388, 0.519234, 0.665798), "Suburbs_Gate_Trim_A_2m6", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4210.3276, 481.00098, 2595.0), (0.0, -179.99980192457332, 0.0), (0.631388, 0.519234, 0.665798), "Suburbs_Gate_Trim_A_2m60", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2361.3398, 1261.0, 2595.0), (0.0, 179.99986339621609, -0.0), (0.631388, 0.519234, 0.665798), "Suburbs_Gate_Trim_A_2m7", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2407.6775, 1435.2087, 2595.0), (0.0, -89.99999818714215, 0.0), (0.631388, 0.519234, 0.665798), "Suburbs_Gate_Trim_A_2m9", _folder)
if a: placed += 1
else: skipped += 1

# Batch 65: StaticMesh'Suburbs_Gate_Trim_A_Corner' (20 instances)
_mesh_path = "/Game/Art/Assets/Kits/Architecture/Suburbs/Suburbs_Gate_Trim_A_Corner"
_materials = ['/Game/Art/Assets/Kits/Architecture/Suburbs/Materials/Suburbs_Trim_A_Corner/MI_Suburbs_Gate_Trim_A_Corner_NonDest']
_folder = "Reconstruction/BD_BB_OrcTown_Gate/Meshes"
a = spawn_static_mesh(_mesh_path, _materials, (2359.504, 1607.6191, 2595.0), (0.0, 0.00015399999724590466, -0.0), (0.482072, 0.463604, 0.665798), "Suburbs_Gate_Trim_A_2m11", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2407.741, 494.06958, 2595.0), (0.0, -90.00002735739477, 0.0), (0.482072, 0.463604, 0.665798), "Suburbs_Gate_Trim_A_2m14", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2359.5042, 792.61914, 2595.0), (0.0, 0.00015399999724590466, -0.0), (0.482072, 0.463604, 0.665798), "Suburbs_Gate_Trim_A_2m17", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2407.7402, 2124.0696, 2595.0), (0.0, -90.00002735739477, 0.0), (0.48207152, 0.4636036, 0.665798), "Suburbs_Gate_Trim_A_2m2", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2407.7397, 2949.0696, 2595.0), (0.0, -90.00002735739477, 0.0), (0.482072, 0.463604, 0.665798), "Suburbs_Gate_Trim_A_2m20", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2359.503, 3247.6191, 2595.0), (0.0, 0.00015399999724590466, -0.0), (0.482072, 0.463604, 0.665798), "Suburbs_Gate_Trim_A_2m23", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2407.7388, 3759.0696, 2595.0), (0.0, -90.00002735739477, 0.0), (0.482072, 0.463604, 0.665798), "Suburbs_Gate_Trim_A_2m26", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2359.502, 4057.6191, 2595.0), (0.0, 0.00015399999724590466, -0.0), (0.482072, 0.463604, 0.665798), "Suburbs_Gate_Trim_A_2m29", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4035.953, 4049.487, 2595.0), (0.0, 89.99993822608693, -0.0), (0.482072, 0.463604, 0.665798), "Suburbs_Gate_Trim_A_2m32", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4084.1892, 3750.9375, 2595.0), (0.0, -179.9998360754275, 0.0), (0.482072, 0.463604, 0.665798), "Suburbs_Gate_Trim_A_2m35", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4035.953, 3229.487, 2595.0), (0.0, 89.99993822608693, -0.0), (0.482072, 0.463604, 0.665798), "Suburbs_Gate_Trim_A_2m38", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4084.1892, 2930.9375, 2595.0), (0.0, -179.9998360754275, 0.0), (0.482072, 0.463604, 0.665798), "Suburbs_Gate_Trim_A_2m41", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4035.953, 2604.487, 2595.0), (0.0, 89.99993822608693, -0.0), (0.482072, 0.463604, 0.665798), "Suburbs_Gate_Trim_A_2m44", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4084.1892, 2305.9375, 2595.0), (0.0, -179.9998360754275, 0.0), (0.482072, 0.463604, 0.665798), "Suburbs_Gate_Trim_A_2m47", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2359.5034, 2422.6191, 2595.0), (0.0, 0.00015401840065028434, -0.0), (0.482072, 0.463604, 0.665798), "Suburbs_Gate_Trim_A_2m5", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4035.953, 1599.487, 2595.0), (0.0, 89.99993822608693, -0.0), (0.482072, 0.463604, 0.665798), "Suburbs_Gate_Trim_A_2m50", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4084.1892, 1300.9375, 2595.0), (0.0, -179.9998360754275, 0.0), (0.482072, 0.463604, 0.665798), "Suburbs_Gate_Trim_A_2m53", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4035.953, 779.48706, 2595.0), (0.0, 89.99993822608693, -0.0), (0.482072, 0.463604, 0.665798), "Suburbs_Gate_Trim_A_2m56", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4084.1892, 480.9375, 2595.0), (0.0, -179.9998360754275, 0.0), (0.482072, 0.463604, 0.665798), "Suburbs_Gate_Trim_A_2m59", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2407.7407, 1309.0696, 2595.0), (0.0, -90.00002735739477, 0.0), (0.482072, 0.463604, 0.665798), "Suburbs_Gate_Trim_A_2m8", _folder)
if a: placed += 1
else: skipped += 1

# Batch 66: StaticMesh'Suburbs_Platform_Small_3x3' (20 instances)
_mesh_path = "/Game/Art/Assets/Kits/Architecture/Suburbs/Suburbs_Platform_Small_3x3"
_materials = ['/Game/Art/Assets/Kits/Architecture/Suburbs/Destructable/Materials/MI_Suburbs_Wall_Non_Dest']
_folder = "Reconstruction/BD_BB_OrcTown_Gate/Meshes"
a = spawn_static_mesh(_mesh_path, _materials, (2330.5615, 3168.4553, 2594.889), (0.0, 90.00007597449323, -0.0), (0.635437, 0.635437, 0.444087), "Suburbs_Platform_Small_3x10", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2328.5752, 3788.011, 2594.889), (0.0, 0.0, -0.0), (0.635437, 0.635437, 0.444087), "Suburbs_Platform_Small_3x11", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2330.5605, 3978.4553, 2594.889), (0.0, 90.00007597449323, -0.0), (0.635437, 0.635437, 0.444087), "Suburbs_Platform_Small_3x12", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4115.116, 4020.5454, 2594.889), (0.0, 179.9999590188648, -0.0), (0.635437, 0.635437, 0.444087), "Suburbs_Platform_Small_3x13", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4113.131, 3830.1013, 2594.889), (0.0, -89.99999818714215, 0.0), (0.635437, 0.635437, 0.444087), "Suburbs_Platform_Small_3x14", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4115.116, 3200.5454, 2594.889), (0.0, 179.9999590188648, -0.0), (0.635437, 0.635437, 0.444087), "Suburbs_Platform_Small_3x15", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4113.131, 3010.1013, 2594.889), (0.0, -89.99999818714215, 0.0), (0.635437, 0.635437, 0.444087), "Suburbs_Platform_Small_3x16", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4115.116, 2575.5454, 2594.889), (0.0, 179.9999590188648, -0.0), (0.635437, 0.635437, 0.444087), "Suburbs_Platform_Small_3x17", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4113.131, 2385.1013, 2594.889), (0.0, -89.99999818714215, 0.0), (0.635437, 0.635437, 0.444087), "Suburbs_Platform_Small_3x18", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4115.116, 1570.5454, 2594.889), (0.0, 179.9999590188648, -0.0), (0.635437, 0.635437, 0.444087), "Suburbs_Platform_Small_3x19", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4113.131, 1380.1013, 2594.889), (0.0, -89.99999818714215, 0.0), (0.635437, 0.635437, 0.444087), "Suburbs_Platform_Small_3x20", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4115.116, 750.5454, 2594.889), (0.0, 179.9999590188648, -0.0), (0.635437, 0.635437, 0.444087), "Suburbs_Platform_Small_3x21", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4113.131, 560.1013, 2594.889), (0.0, -89.99999818714215, 0.0), (0.635437, 0.635437, 0.444087), "Suburbs_Platform_Small_3x22", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2328.5767, 2153.011, 2594.889), (0.0, 0.0, -0.0), (0.635437, 0.635437, 0.444087), "Suburbs_Platform_Small_3x3_14", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2330.562, 2343.4553, 2594.889), (0.0, 90.00007597449323, -0.0), (0.635437, 0.635437, 0.444087), "Suburbs_Platform_Small_3x4", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2328.5771, 1338.011, 2594.889), (0.0, 0.0, -0.0), (0.635437, 0.635437, 0.444087), "Suburbs_Platform_Small_3x5", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2330.5625, 1528.4553, 2594.889), (0.0, 90.00007597449323, -0.0), (0.635437, 0.635437, 0.444087), "Suburbs_Platform_Small_3x6", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2328.5774, 523.011, 2594.889), (0.0, 0.0, -0.0), (0.635437, 0.635437, 0.444087), "Suburbs_Platform_Small_3x7", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2330.5627, 713.4553, 2594.889), (0.0, 90.00007597449323, -0.0), (0.635437, 0.635437, 0.444087), "Suburbs_Platform_Small_3x8", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2328.5762, 2978.011, 2594.889), (0.0, 0.0, -0.0), (0.635437, 0.635437, 0.444087), "Suburbs_Platform_Small_3x9", _folder)
if a: placed += 1
else: skipped += 1

# Batch 67: StaticMesh'Suburbs_Stairs_Medium_C_NonDest' (22 instances)
_mesh_path = "/Game/Art/Assets/Kits/Architecture/Suburbs/Suburbs_Stairs_Medium_C_NonDest"
_materials = ['/Game/Art/Assets/Kits/Architecture/Suburbs/Materials/Stairs_Medium_C_NonDest/MI_Stairs_Medium_C_NonDes', '/Game/Art/Assets/Kits/Architecture/Suburbs/Destructable/Materials/MI_Suburbs_Wall_Non_Dest']
_folder = "Reconstruction/BD_BB_OrcTown_Gate/Meshes"
a = spawn_static_mesh(_mesh_path, _materials, (3450.0, 350.0, 800.0), (0.0, 179.99986339621609, -0.0), (1.0, 1.0, 1.0), "Suburbs_Stairs_Medium_c1_315", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3500.0, 5650.0, 800.0), (0.0, 0.0, -0.0), (1.0, 1.0, 1.0), "Suburbs_Stairs_Medium_c10", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3800.0, 5650.0, 800.0), (0.0, 0.0, -0.0), (1.0, 1.0, 1.0), "Suburbs_Stairs_Medium_c11", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3150.0, 350.0, 800.0), (0.0, -179.99994535848643, 0.0), (1.0, 1.0, 1.0), "Suburbs_Stairs_Medium_c12_312", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2550.0, 350.0, 800.0), (0.0, -179.99994535848643, 0.0), (1.0, 1.0, 1.0), "Suburbs_Stairs_Medium_c13", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2850.0, 350.0, 800.0), (0.0, 179.99986339621609, -0.0), (1.0, 1.0, 1.0), "Suburbs_Stairs_Medium_c14", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2250.0, 350.0, 800.0), (0.0, 179.99986339621609, -0.0), (1.0, 1.0, 1.0), "Suburbs_Stairs_Medium_c15", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4050.0, 350.0, 800.0), (0.0, -179.99994535848643, 0.0), (1.0, 1.0, 1.0), "Suburbs_Stairs_Medium_c16", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4350.0, 350.0, 800.0), (0.0, 179.99986339621609, -0.0), (1.0, 1.0, 1.0), "Suburbs_Stairs_Medium_c17", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3750.0, 350.0, 800.0), (0.0, 179.99986339621609, -0.0), (1.0, 1.0, 1.0), "Suburbs_Stairs_Medium_c18", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3200.0, 5050.0, 1000.0), (0.0, 0.0, -0.0), (1.0, 1.0, 1.0), "Suburbs_Stairs_Medium_c2_35", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4650.0, 350.0, 800.0), (0.0, 179.99986339621609, -0.0), (1.0, 1.0, 1.0), "Suburbs_Stairs_Medium_c28_176", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4950.0, 350.0, 800.0), (0.0, -179.99994535848643, 0.0), (1.0, 1.0, 1.0), "Suburbs_Stairs_Medium_c29_177", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2600.0, 5050.0, 1000.0), (0.0, 0.0, -0.0), (1.0, 1.0, 1.0), "Suburbs_Stairs_Medium_c3", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5250.0, 350.0, 800.0), (0.0, 179.99986339621609, -0.0), (1.0, 1.0, 1.0), "Suburbs_Stairs_Medium_c30", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5550.0, 350.0, 800.0), (0.0, 179.99986339621609, -0.0), (1.0, 1.0, 1.0), "Suburbs_Stairs_Medium_c31", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2900.0, 5050.0, 1000.0), (0.0, 0.0, -0.0), (1.0, 1.0, 1.0), "Suburbs_Stairs_Medium_c4", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3500.0, 5050.0, 1000.0), (0.0, 0.0, -0.0), (1.0, 1.0, 1.0), "Suburbs_Stairs_Medium_c5", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3800.0, 5050.0, 1000.0), (0.0, 0.0, -0.0), (1.0, 1.0, 1.0), "Suburbs_Stairs_Medium_c6_86", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3200.0, 5650.0, 800.0), (0.0, 0.0, -0.0), (1.0, 1.0, 1.0), "Suburbs_Stairs_Medium_c7", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2600.0, 5650.0, 800.0), (0.0, 0.0, -0.0), (1.0, 1.0, 1.0), "Suburbs_Stairs_Medium_c8", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2900.0, 5650.0, 800.0), (0.0, 0.0, -0.0), (1.0, 1.0, 1.0), "Suburbs_Stairs_Medium_c9", _folder)
if a: placed += 1
else: skipped += 1

# Batch 68: StaticMesh'Suburbs_Stairs_Small_C_CornerExt_NonDest' (1 instances)
_mesh_path = "/Game/Art/Assets/Kits/Architecture/Suburbs/Suburbs_Stairs_Small_C_CornerExt_NonDest"
_materials = ['/Game/Art/Assets/Kits/Architecture/Suburbs/Destructable/Materials/MI_Suburbs_Wall_Non_Dest', '/Game/Art/Assets/Kits/Architecture/Suburbs/Materials/Stairs_Medium_C_NonDest/MI_Stairs_Medium_C_NonDes']
_folder = "Reconstruction/BD_BB_OrcTown_Gate/Meshes"
a = spawn_static_mesh(_mesh_path, _materials, (5150.0, 700.0, 1000.0), (0.0, 179.99994535848643, -0.0), (1.0, 1.0, 1.0), "Suburbs_Stairs_Small_C_CornerExt_NonDest2_92", _folder)
if a: placed += 1
else: skipped += 1

# Batch 69: StaticMesh'Suburbs_Stairs_Small_C_NonDest' (38 instances)
_mesh_path = "/Game/Art/Assets/Kits/Architecture/Suburbs/Suburbs_Stairs_Small_C_NonDest"
_materials = ['/Game/Art/Assets/Kits/Architecture/Suburbs/Destructable/Materials/MI_Suburbs_Wall_Non_Dest', '/Game/Art/Assets/Kits/Architecture/Suburbs/Materials/Stairs_Medium_C_NonDest/MI_Stairs_Medium_C_NonDes']
_folder = "Reconstruction/BD_BB_OrcTown_Gate/Meshes"
a = spawn_static_mesh(_mesh_path, _materials, (3650.0, 2350.0, 1100.0), (0.0, 179.99988388675877, -0.0), (1.0, 1.0, 1.0), "Suburbs_Stairs_Small_C10", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2600.0, 2500.0, 1200.0), (0.0, 179.99988388675877, -0.0), (1.0, 1.0, 1.0), "Suburbs_Stairs_Small_C11", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2300.0, 2500.0, 1200.0), (0.0, 179.99988388675877, -0.0), (1.0, 1.0, 1.0), "Suburbs_Stairs_Small_C13", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2750.0, 2630.0, 1210.0), (0.0, -90.00005166594045, 0.0), (1.0, 1.0, 1.0), "Suburbs_Stairs_Small_C14", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3350.0, 2350.0, 1100.0), (0.0, 179.99988388675877, -0.0), (1.0, 1.0, 1.0), "Suburbs_Stairs_Small_C2_12", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2599.9055, 700.0, 1000.0), (0.0, -179.99995901885745, 0.0), (1.0, 1.0, 1.0), "Suburbs_Stairs_Small_C21_267", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2299.9055, 700.0, 1000.0), (0.0, -179.99995901885745, 0.0), (1.0, 1.0, 1.0), "Suburbs_Stairs_Small_C22_285", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3050.0, 2350.0, 1100.0), (0.0, 179.99988388675877, -0.0), (1.0, 1.0, 1.0), "Suburbs_Stairs_Small_C3", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2000.0, 2500.0, 1200.0), (0.0, 179.99988388675877, -0.0), (1.0, 1.0, 1.0), "Suburbs_Stairs_Small_C31", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4100.0, 2500.0, 1200.0), (0.0, 179.99988388675877, -0.0), (1.0, 1.0, 1.0), "Suburbs_Stairs_Small_C32", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3800.0, 2500.0, 1200.0), (0.0, 179.99988388675877, -0.0), (1.0, 1.0, 1.0), "Suburbs_Stairs_Small_C33", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4400.0, 2500.0, 1200.0), (0.0, 179.99988388675877, -0.0), (1.0, 1.0, 1.0), "Suburbs_Stairs_Small_C34", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3499.9055, 700.0, 1000.0), (0.0, -179.99995901885745, 0.0), (1.0, 1.0, 1.0), "Suburbs_Stairs_Small_C35", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3199.9055, 700.0, 1000.0), (0.0, -179.99995901885745, 0.0), (1.0, 1.0, 1.0), "Suburbs_Stairs_Small_C36", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2900.0, 700.0, 1000.0), (0.0, -179.99995901885745, 0.0), (1.0, 1.0, 1.0), "Suburbs_Stairs_Small_C37", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4399.9053, 700.0, 1000.0), (0.0, -179.99995901885745, 0.0), (1.0, 1.0, 1.0), "Suburbs_Stairs_Small_C38", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4099.9053, 700.0, 1000.0), (0.0, -179.99995901885745, 0.0), (1.0, 1.0, 1.0), "Suburbs_Stairs_Small_C39", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2750.0, 2350.0, 1100.0), (0.0, 179.99988388675877, -0.0), (1.0, 1.0, 1.0), "Suburbs_Stairs_Small_C4", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3800.0, 700.0, 1000.0), (0.0, -179.99995901885745, 0.0), (1.0, 1.0, 1.0), "Suburbs_Stairs_Small_C40", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4699.9053, 700.0, 1000.0), (0.0, -179.99995901885745, 0.0), (1.0, 1.0, 1.0), "Suburbs_Stairs_Small_C41", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4999.9053, 700.0, 1000.0), (0.0, -179.99995901885745, 0.0), (1.0, 1.0, 1.0), "Suburbs_Stairs_Small_C42", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5149.9053, 850.0, 1000.0), (0.0, -89.9998815062137, 0.0), (1.0, 1.0, 1.0), "Suburbs_Stairs_Small_C43", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5149.9053, 1150.0, 1000.0), (0.0, -89.9998815062137, 0.0), (1.0, 1.0, 1.0), "Suburbs_Stairs_Small_C44", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5149.9053, 1450.0, 1000.0), (0.0, -89.9998815062137, 0.0), (1.0, 1.0, 1.0), "Suburbs_Stairs_Small_C45", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2750.0, 2930.0, 1210.0), (0.0, -90.00005166594045, 0.0), (1.0, 1.0, 1.0), "Suburbs_Stairs_Small_C46", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2750.0, 3230.0, 1210.0), (0.0, -90.00005166594045, 0.0), (1.0, 1.0, 1.0), "Suburbs_Stairs_Small_C47", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3649.998, 3240.001, 1210.0), (0.0, 89.99997063746636, -0.0), (1.0, 1.0, 1.0), "Suburbs_Stairs_Small_C48", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3649.999, 2940.0002, 1210.0), (0.0, 89.99997063746636, -0.0), (1.0, 1.0, 1.0), "Suburbs_Stairs_Small_C49", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2450.0, 2350.0, 1100.0), (0.0, 179.99988388675877, -0.0), (1.0, 1.0, 1.0), "Suburbs_Stairs_Small_C5", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3650.0, 2640.0, 1210.0), (0.0, 89.99997063746636, -0.0), (1.0, 1.0, 1.0), "Suburbs_Stairs_Small_C50", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2750.0, 3530.0, 1210.0), (0.0, -90.00005166594045, 0.0), (1.0, 1.0, 1.0), "Suburbs_Stairs_Small_C51", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3649.998, 3540.001, 1210.0), (0.0, 89.99997063746636, -0.0), (1.0, 1.0, 1.0), "Suburbs_Stairs_Small_C52", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2150.0, 2350.0, 1100.0), (0.0, 179.99988388675877, -0.0), (1.0, 1.0, 1.0), "Suburbs_Stairs_Small_C6", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5150.0, 1750.0, 1000.0), (0.0, -89.99997063746636, 0.0), (1.0, 1.0, 1.0), "Suburbs_Stairs_Small_C7", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4250.0, 2350.0, 1100.0), (0.0, 179.99988388675877, -0.0), (1.0, 1.0, 1.0), "Suburbs_Stairs_Small_C8", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3950.0, 2350.0, 1100.0), (0.0, 179.99988388675877, -0.0), (1.0, 1.0, 1.0), "Suburbs_Stairs_Small_C9", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2243.275, 2580.1387, 2414.46), (0.0001366037460709673, 90.00131571787922, 179.99997950943478), (0.53125, 1.0, 1.0), "Suburbs_Stairs_Small_C_NonDest_19", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4183.275, 2580.1387, 2414.46), (0.00013699997900674658, -89.99877142271598, 179.99997950943336), (0.53125, 1.0, 1.0), "Suburbs_Stairs_Small_C_NonDest2_51", _folder)
if a: placed += 1
else: skipped += 1

# Batch 70: StaticMesh'Suburbs_Wall_Thick_1x1m_A' (19 instances)
_mesh_path = "/Game/Art/Assets/Kits/Architecture/Suburbs/Suburbs_Wall_Thick_1x1m_A"
_materials = ['/Game/Art/Assets/Kits/Architecture/Suburbs/Destructable/Materials/MI_Suburbs_Wall_Base_Dest']
_folder = "Reconstruction/BD_BB_OrcTown_Gate/Meshes"
a = spawn_static_mesh(_mesh_path, _materials, (3997.6404, 1499.4834, 2613.6438), (2.0490568166181256e-05, -89.99941964543291, -9.155274433495314e-05), (0.48750743, 0.46438116, 0.29023752), "BP_Suburbs_Wall_Thick_1x1m_A_Breakable_0", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3997.6335, 3949.4856, 2613.6433), (2.0490568166181256e-05, -89.99941964543291, -9.155274433495314e-05), (0.48750743, 0.46438116, 0.29023752), "BP_Suburbs_Wall_Thick_1x1m_A_Breakable_2", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3997.64, 2309.4856, 2613.6433), (2.0490568166181256e-05, -89.99941964543291, -9.155274433495314e-05), (0.48750743, 0.46438116, 0.29023752), "BP_Suburbs_Wall_Thick_1x1m_A_Breakable_3", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2444.8386, 609.251, 2613.6345), (0.00043713207236236953, 90.00082954318046, 4.0000069950739784e-05), (0.48750743, 0.46438116, 0.29023752), "BP_Suburbs_Wall_Thick_1x1m_A_Breakable_4", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2445.5608, 3905.6038, 2613.6409), (0.0004371320936584063, 90.00053783891171, 2.600000864464145e-05), (0.48750606, 0.4643797, 0.29023713), "BP_Suburbs_Wall_Thick_1x1m_A_Breakable_7", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3996.883, 3903.1396, 2613.6428), (2.0490570620033804e-05, -89.99954442868432, -9.155273515911724e-05), (0.48750606, 0.4643797, 0.29023713), "BP_Suburbs_Wall_Thick_1x1m_A_Breakable_19", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2444.8052, 3859.2544, 2613.6475), (0.0004371321057682016, 90.00082954317988, 3.9862191905379485e-05), (0.48750743, 0.46438116, 0.29023752), "BP_Suburbs_Wall_Thick_1x1m_A_Breakable_31", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2445.5608, 3095.6038, 2613.6409), (0.00043713209236119314, 90.00053783891285, 2.627796871023012e-05), (0.48750606, 0.4643797, 0.29023713), "BP_Suburbs_Wall_Thick_1x1m_A_Breakable_32", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2444.808, 3049.251, 2613.642), (0.0004371321057682016, 90.00082954317988, 3.9862191905379485e-05), (0.48750743, 0.46438116, 0.29023752), "BP_Suburbs_Wall_Thick_1x1m_A_Breakable_33", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2445.5693, 1455.6003, 2613.6309), (0.00043713209236119314, 90.00053783891285, 2.627796871023012e-05), (0.48750606, 0.4643797, 0.29023713), "BP_Suburbs_Wall_Thick_1x1m_A_Breakable_34", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3996.88, 3083.1338, 2613.6428), (2.0490570620033804e-05, -89.99954442868432, -9.155273515911724e-05), (0.48750606, 0.4643797, 0.29023713), "BP_Suburbs_Wall_Thick_1x1m_A_Breakable_35", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3997.6335, 3129.4856, 2613.6433), (2.0490568166181256e-05, -89.99941964543291, -9.155274433495314e-05), (0.48750743, 0.46438116, 0.29023752), "BP_Suburbs_Wall_Thick_1x1m_A_Breakable_36", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3996.8926, 1453.1338, 2613.6433), (2.0490570620033804e-05, -89.99954442868432, -9.155273515911724e-05), (0.48750606, 0.4643797, 0.29023713), "BP_Suburbs_Wall_Thick_1x1m_A_Breakable_37", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2445.563, 2275.6038, 2613.639), (0.0004371320936584063, 90.00053783891171, 2.600000864464145e-05), (0.48750606, 0.4643797, 0.29023713), "BP_Suburbs_Wall_Thick_1x1m_A_Breakable_38", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2444.826, 2229.251, 2613.6401), (0.00043713207236236953, 90.00082954318046, 4.0000069950739784e-05), (0.48750743, 0.46438116, 0.29023752), "BP_Suburbs_Wall_Thick_1x1m_A_Breakable_39", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2445.582, 635.6003, 2613.6252), (0.0004371320936584063, 90.00053783891171, 2.600000864464145e-05), (0.48750606, 0.4643797, 0.29023713), "BP_Suburbs_Wall_Thick_1x1m_A_Breakable_40", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2444.8386, 1409.2507, 2613.6345), (0.00043713207236236953, 90.00082954318046, 4.0000069950739784e-05), (0.48750743, 0.46438116, 0.29023752), "BP_Suburbs_Wall_Thick_1x1m_A_Breakable_41", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3997.6482, 679.4834, 2613.644), (2.0490568166181256e-05, -89.99941964543291, -9.155274433495314e-05), (0.48750743, 0.46438116, 0.29023752), "BP_Suburbs_Wall_Thick_1x1m_A_Breakable_42", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3996.9006, 633.13385, 2613.6436), (2.0490570620033804e-05, -89.99954442868432, -9.155273515911724e-05), (0.48750606, 0.4643797, 0.29023713), "BP_Suburbs_Wall_Thick_1x1m_A_Breakable_43", _folder)
if a: placed += 1
else: skipped += 1

# Batch 71: StaticMesh'Suburbs_Wall_Thick_3x3m_A' (111 instances)
_mesh_path = "/Game/Art/Assets/Kits/Architecture/Suburbs/Suburbs_Wall_Thick_3x3m_A"
_materials = ['/Game/Art/Assets/Kits/Architecture/Suburbs/Destructable/Materials/MI_Suburbs_Wall_Non_Dest']
_folder = "Reconstruction/BD_BB_OrcTown_Gate/Meshes"
a = spawn_static_mesh(_mesh_path, _materials, (4575.315, 1860.1292, 2437.358), (0.0003552334677259794, -89.99951298722546, -89.99991405643874), (1.0, 1.0, 1.4375), "Suburbs_Wall_Thin_3x3m_A159", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4575.1826, 2760.13, 2437.38), (0.00035523360792801033, -89.99953705139899, -89.99994270427665), (1.0, 1.0, 1.4375), "Suburbs_Wall_Thin_3x3m_A160", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4575.2686, 2160.1296, 2437.365), (0.00035523360792801033, -89.99953705139899, -89.99994270427665), (1.0, 1.0, 1.4375), "Suburbs_Wall_Thin_3x3m_A161", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4575.226, 2460.1296, 2437.3716), (0.00035523360792801033, -89.99953705139899, -89.99994270427665), (1.0, 1.0, 1.4375), "Suburbs_Wall_Thin_3x3m_A162", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1867.2253, 3498.6077, 2437.368), (0.0008199014083492366, 90.00064171919833, -89.99978456822535), (1.0, 1.0, 1.4375), "Suburbs_Wall_Thin_3x3m_A163_281", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1867.2512, 2598.6077, 2437.3376), (0.0008405270260585058, 90.00048473099463, -89.99951413336552), (1.0, 1.0, 1.4375), "Suburbs_Wall_Thin_3x3m_A164_285", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4575.354, 1560.1289, 2437.3508), (0.0003552334677259794, -89.99951298722546, -89.99991405643874), (1.0, 1.0, 1.4375), "Suburbs_Wall_Thin_3x3m_A165", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4575.354, 1260.1289, 2437.3508), (0.0003552334677259794, -89.99951298722546, -89.99991405643874), (1.0, 1.0, 1.4375), "Suburbs_Wall_Thin_3x3m_A166_26", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1867.231, 3198.607, 2437.3547), (0.0008405270260585058, 90.00048473099463, -89.99951413336552), (1.0, 1.0, 1.4375), "Suburbs_Wall_Thin_3x3m_A167_286", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1867.2406, 2898.6074, 2437.346), (0.0008405270260585058, 90.00048473099463, -89.99951413336552), (1.0, 1.0, 1.4375), "Suburbs_Wall_Thin_3x3m_A168_287", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1867.2183, 3798.609, 2437.376), (0.0008199014083492366, 90.00064171919833, -89.99978456822535), (1.0, 1.0, 1.4375), "Suburbs_Wall_Thin_3x3m_A169_288", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2017.2141, 4098.6074, 2437.3792), (0.0008199014083492366, 90.00064171919833, -89.99978456822535), (1.0, 1.0, 1.0), "Suburbs_Wall_Thin_3x3m_A170_297", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4575.354, 960.1289, 2437.3508), (0.0003552334677259794, -89.99951298722546, -89.99991405643874), (1.0, 1.0, 1.4375), "Suburbs_Wall_Thin_3x3m_A171", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4575.354, 660.1289, 2437.3508), (0.0003552334677259794, -89.99951298722546, -89.99991405643874), (1.0, 1.0, 1.4375), "Suburbs_Wall_Thin_3x3m_A172", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4575.36, 60.12891, 2437.3533), (0.0003552334677259794, -89.99951298722546, -89.99991405643874), (1.0, 1.0, 1.4375), "Suburbs_Wall_Thin_3x3m_A173", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4575.357, 360.1289, 2437.3518), (0.0003552334677259794, -89.99951298722546, -89.99991405643874), (1.0, 1.0, 1.4375), "Suburbs_Wall_Thin_3x3m_A174", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4575.139, 3060.1294, 2437.3823), (0.00035523360792801033, -89.99953705139899, -89.99994270427665), (1.0, 1.0, 1.4375), "Suburbs_Wall_Thin_3x3m_A176", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4575.097, 3360.13, 2437.3892), (0.00035523360792801033, -89.99953705139899, -89.99994270427665), (1.0, 1.0, 1.4375), "Suburbs_Wall_Thin_3x3m_A177", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4575.097, 3660.13, 2437.3892), (0.00035523360792801033, -89.99953705139899, -89.99994270427665), (1.0, 1.0, 1.4375), "Suburbs_Wall_Thin_3x3m_A178_20", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1867.2612, 2298.6106, 2437.328), (0.0008405270260585058, 90.00048473099463, -89.99951413336552), (1.0, 1.0, 1.4375), "Suburbs_Wall_Thin_3x3m_A179_292", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1867.2704, 1998.6106, 2437.317), (0.0008405270260585058, 90.00048473099463, -89.99951413336552), (1.0, 1.0, 1.4375), "Suburbs_Wall_Thin_3x3m_A180_293", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1867.2842, 1698.6072, 2437.3018), (0.0008405270260585058, 90.00048473099463, -89.99951413336552), (1.0, 1.0, 1.4375), "Suburbs_Wall_Thin_3x3m_A181_294", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1867.2941, 1398.6072, 2437.2908), (0.0008405270260585058, 90.00048473099463, -89.99951413336552), (1.0, 1.0, 1.4375), "Suburbs_Wall_Thin_3x3m_A182_367", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1867.305, 1098.6072, 2437.277), (0.0008405270260585058, 90.00048473099463, -89.99951413336552), (1.0, 1.0, 1.4375), "Suburbs_Wall_Thin_3x3m_A183_370", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1867.3158, 798.6072, 2437.264), (0.0008405270260585058, 90.00048473099463, -89.99951413336552), (1.0, 1.0, 1.4375), "Suburbs_Wall_Thin_3x3m_A184_372", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4575.097, 3960.13, 2437.3892), (0.00035523360792801033, -89.99953705139899, -89.99994270427665), (1.0, 1.0, 1.4375), "Suburbs_Wall_Thin_3x3m_A185_22", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4575.097, 4260.13, 2437.3892), (0.00035523360792801033, -89.99953705139899, -89.99994270427665), (1.0, 1.0, 1.4375), "Suburbs_Wall_Thin_3x3m_A186_24", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1867.3182, 498.60718, 2437.2593), (0.0008405270260585058, 90.00048473099463, -89.99951413336552), (1.0, 1.0, 1.4375), "Suburbs_Wall_Thin_3x3m_A187", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1867.3209, 198.60718, 2437.2542), (0.0008405270260585058, 90.00048473099463, -89.99951413336552), (1.0, 1.0, 1.4375), "Suburbs_Wall_Thin_3x3m_A188", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1817.2612, 2298.6106, 2357.328), (0.0008405270260585058, 90.00048473099463, -89.99951413336552), (1.0, 1.0, 1.4375), "Suburbs_Wall_Thin_3x3m_A189", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1817.2612, 1998.6106, 2357.328), (0.0008405270260585058, 90.00048473099463, -89.99951413336552), (1.0, 1.0, 1.4375), "Suburbs_Wall_Thin_3x3m_A190", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1817.2612, 1698.6106, 2357.328), (0.0008405270260585058, 90.00048473099463, -89.99951413336552), (1.0, 1.0, 1.4375), "Suburbs_Wall_Thin_3x3m_A191", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1817.2612, 1398.6106, 2357.328), (0.0008405270260585058, 90.00048473099463, -89.99951413336552), (1.0, 1.0, 1.4375), "Suburbs_Wall_Thin_3x3m_A192", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1817.2612, 1098.6106, 2357.328), (0.0008405270260585058, 90.00048473099463, -89.99951413336552), (1.0, 1.0, 1.4375), "Suburbs_Wall_Thin_3x3m_A193", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1817.2612, 798.6106, 2357.328), (0.0008405270260585058, 90.00048473099463, -89.99951413336552), (1.0, 1.0, 1.4375), "Suburbs_Wall_Thin_3x3m_A194", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1817.2612, 498.6106, 2357.328), (0.0008405270260585058, 90.00048473099463, -89.99951413336552), (1.0, 1.0, 1.4375), "Suburbs_Wall_Thin_3x3m_A195", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1817.2612, 198.6106, 2357.328), (0.0008405270260585058, 90.00048473099463, -89.99951413336552), (1.0, 1.0, 1.4375), "Suburbs_Wall_Thin_3x3m_A196", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1817.2612, 2598.6106, 2357.328), (0.0008405270260585058, 90.00048473099463, -89.99951413336552), (1.0, 1.0, 1.4375), "Suburbs_Wall_Thin_3x3m_A197", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3373.824, 3176.459, 3057.364), (0.0003575256916624967, -89.99956455347234, -90.00000687551899), (1.0, 1.0, 1.0), "Suburbs_Wall_Thin_3x3m_A198", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3373.8293, 2876.4592, 3057.3645), (0.0003575256916624967, -89.99956455347234, -90.00000687551899), (1.0, 1.0, 1.0), "Suburbs_Wall_Thin_3x3m_A199", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3373.8228, 3776.461, 3057.3582), (0.0003575256916624967, -89.99956455347234, -90.00000687551899), (1.0, 1.0, 1.0), "Suburbs_Wall_Thin_3x3m_A200", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3373.8276, 3476.4614, 3057.3584), (0.0003575256916624967, -89.99956455347234, -90.00000687551899), (1.0, 1.0, 1.0), "Suburbs_Wall_Thin_3x3m_A201", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3392.5862, 1976.464, 3057.371), (0.0003575256916624967, -89.99956455347234, -90.00000687551899), (1.0, 1.0, 1.125), "Suburbs_Wall_Thin_3x3m_A202_338", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3392.602, 1676.4646, 3057.3716), (0.0003575256916624967, -89.99956455347234, -90.00000687551899), (1.0, 1.0, 1.125), "Suburbs_Wall_Thin_3x3m_A203_339", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3392.5654, 2576.4656, 3057.3652), (0.0003575256916624967, -89.99956455347234, -90.00000687551899), (1.0, 1.0, 1.125), "Suburbs_Wall_Thin_3x3m_A204_340", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3392.5806, 2276.4663, 3057.3655), (0.0003575256916624967, -89.99956455347234, -90.00000687551899), (1.0, 1.0, 1.125), "Suburbs_Wall_Thin_3x3m_A205_341", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3392.6467, 774.5299, 2981.0857), (-8.850556454950619, -89.99950883505728, -89.999546207562), (1.0, 1.0, 1.125), "Suburbs_Wall_Thin_3x3m_A206_364", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3392.6636, 478.10522, 2934.9097), (-8.850556454950619, -89.99950883505728, -89.999546207562), (1.0, 1.0, 1.125), "Suburbs_Wall_Thin_3x3m_A207_365", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3392.6172, 1372.0908, 3041.9546), (-5.0324390998494435, -89.99951325320255, -89.99981918784898), (1.0, 1.0, 1.125), "Suburbs_Wall_Thin_3x3m_A208", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3392.633, 1073.3206, 3015.6345), (-5.0324390998494435, -89.99951325320255, -89.99981918784898), (1.0, 1.0, 1.125), "Suburbs_Wall_Thin_3x3m_A209", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3373.8228, 4076.461, 3057.3582), (0.0003575256916624967, -89.99956455347234, -90.00000687551899), (1.0, 1.0, 1.0), "Suburbs_Wall_Thin_3x3m_A210", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1817.2612, 2898.6106, 2357.328), (0.0008405270260585058, 90.00048473099463, -89.99951413336552), (1.0, 1.0, 1.4375), "Suburbs_Wall_Thin_3x3m_A211", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1817.2612, 3198.6106, 2357.328), (0.0008405270260585058, 90.00048473099463, -89.99951413336552), (1.0, 1.0, 1.4375), "Suburbs_Wall_Thin_3x3m_A212", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2633.8281, 4326.462, 2757.3582), (90.0, -0.00013075039271071245, -0.0005064108567899109), (1.0, 1.0, 1.0), "Suburbs_Wall_Thin_3x3m_A213", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2763.8252, 4326.5615, 2457.3552), (90.0, -0.0010962029616638966, -0.0014692910518482503), (1.0, 1.0, 1.375), "Suburbs_Wall_Thin_3x3m_A214", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2763.8281, 4326.532, 2157.358), (90.0, -0.002134738600488133, -0.002516638067663341), (1.0, 1.0, 1.375), "Suburbs_Wall_Thin_3x3m_A215", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2763.8281, 4326.509, 1857.3567), (90.0, -0.004937183960130541, -0.005309197645111234), (1.0, 1.0, 1.375), "Suburbs_Wall_Thin_3x3m_A216", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2763.8281, 4326.4854, 1557.3582), (90.0, -0.009557562051841752, -0.009935378477817112), (1.0, 1.0, 1.375), "Suburbs_Wall_Thin_3x3m_A217", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2763.8281, 4326.462, 1257.3582), (90.0, -0.03798023216640636, -0.03834988142420041), (1.0, 1.0, 1.375), "Suburbs_Wall_Thin_3x3m_A218_73", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1817.2612, 3498.6106, 2357.328), (0.0008405270260585058, 90.00048473099463, -89.99951413336552), (1.0, 1.0, 1.4375), "Suburbs_Wall_Thin_3x3m_A219", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4083.825, 4326.5913, 2457.358), (90.0, -0.002134738600488133, -0.002516638067663341), (1.0, 1.0, 1.34375), "Suburbs_Wall_Thin_3x3m_A220", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4083.8281, 4326.562, 2157.3545), (90.0, -0.004937183960130541, -0.005309197645111234), (1.0, 1.0, 1.34375), "Suburbs_Wall_Thin_3x3m_A221", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4083.8281, 4326.5327, 1857.3563), (90.0, -0.009557562051841752, -0.009935378477817112), (1.0, 1.0, 1.34375), "Suburbs_Wall_Thin_3x3m_A222", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4083.8281, 4326.5034, 1557.3582), (90.0, -0.03798023216640636, -0.03834988142420041), (1.0, 1.0, 1.34375), "Suburbs_Wall_Thin_3x3m_A223", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4083.8281, 4326.474, 1257.3582), (90.0, -0.056402055315231264, -0.05675795250080895), (1.0, 1.0, 1.34375), "Suburbs_Wall_Thin_3x3m_A224", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2563.8281, 2576.462, 2414.3582), (-2.6355913958227538e-05, 90.00005500444897, 89.99969289504277), (0.53125, 0.53125, 1.0), "Suburbs_Wall_Thin_3x3m_A225", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2863.8281, 2576.462, 2414.3582), (-2.6355913958227538e-05, 90.00005500444897, 89.99969289504277), (0.53125, 0.53125, 1.0), "Suburbs_Wall_Thin_3x3m_A226", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1817.2612, 3798.6106, 2357.328), (0.0008405270260585058, 90.00048473099463, -89.99951413336552), (1.0, 1.0, 1.4375), "Suburbs_Wall_Thin_3x3m_A227", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1817.2612, 4098.6104, 2357.328), (0.0008405270260585058, 90.00048473099463, -89.99951413336552), (1.0, 1.0, 1.4375), "Suburbs_Wall_Thin_3x3m_A228", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4617.261, 1698.6311, 2357.3552), (-0.0007288006508744637, -89.9995805960423, -90.00046983212474), (1.0, 1.0, 1.4375), "Suburbs_Wall_Thin_3x3m_A229_22", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3963.8281, 2576.462, 2414.3582), (-2.6355913958227538e-05, 90.00005500444897, 89.99969289504277), (0.53125, 0.53125, 1.0), "Suburbs_Wall_Thin_3x3m_A230", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4263.828, 2576.462, 2414.3582), (-2.6355913958227538e-05, 90.00005500444897, 89.99969289504277), (0.53125, 0.53125, 1.0), "Suburbs_Wall_Thin_3x3m_A231", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2563.8281, 4386.462, 2414.3582), (-2.6355913958227538e-05, 90.00005500444897, 89.99969289504277), (0.53125, 0.53125, 1.0), "Suburbs_Wall_Thin_3x3m_A232", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2863.8281, 4386.462, 2414.3582), (-2.6355913958227538e-05, 90.00005500444897, 89.99969289504277), (0.53125, 0.53125, 1.0), "Suburbs_Wall_Thin_3x3m_A233", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4617.264, 1398.6311, 2357.3508), (-0.0007288006508744637, -89.9995805960423, -90.00046983212474), (1.0, 1.0, 1.4375), "Suburbs_Wall_Thin_3x3m_A234", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4617.2666, 1098.6311, 2357.3467), (-0.0007288006508744637, -89.9995805960423, -90.00046983212474), (1.0, 1.0, 1.4375), "Suburbs_Wall_Thin_3x3m_A235", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4617.2695, 798.6311, 2357.3425), (-0.0007288006508744637, -89.9995805960423, -90.00046983212474), (1.0, 1.0, 1.4375), "Suburbs_Wall_Thin_3x3m_A236", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4013.8281, 4386.462, 2414.3582), (-2.6355913958227538e-05, 90.00005500444897, 89.99969289504277), (0.53125, 0.53125, 1.0), "Suburbs_Wall_Thin_3x3m_A237", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4313.828, 4386.462, 2414.3582), (-2.6355913958227538e-05, 90.00005500444897, 89.99969289504277), (0.53125, 0.53125, 1.0), "Suburbs_Wall_Thin_3x3m_A238", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3200.0, 4300.0, 3027.0), (90.0, -0.004937183960130541, -0.005309197645111234), (1.0, 1.0, 1.0), "Suburbs_Wall_Thin_3x3m_A239", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2900.0, 4300.0, 3027.0), (90.0, -0.009557562051841752, -0.009935378477817112), (1.0, 1.0, 1.0), "Suburbs_Wall_Thin_3x3m_A240_189", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2690.0, 4300.0, 2867.0), (90.0, -0.03798023216640636, -0.03834988142420041), (1.0, 1.0, 1.0), "Suburbs_Wall_Thin_3x3m_A241", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3500.0, 4300.0, 3027.0), (90.0, -0.009557562051841752, -0.009935378477817112), (1.0, 1.0, 1.0), "Suburbs_Wall_Thin_3x3m_A242", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3800.0, 4300.0, 3027.0), (90.0, -0.03798023216640636, -0.03834988142420041), (1.0, 1.0, 1.0), "Suburbs_Wall_Thin_3x3m_A243_191", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4010.0, 4300.0, 2867.0), (90.0, -0.056402055315231264, -0.05675795250080895), (1.0, 1.0, 1.0), "Suburbs_Wall_Thin_3x3m_A244_194", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4617.2725, 498.6311, 2357.3381), (-0.0007288006508744637, -89.9995805960423, -90.00046983212474), (1.0, 1.0, 1.4375), "Suburbs_Wall_Thin_3x3m_A245", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4617.2754, 198.6311, 2357.334), (-0.0007288006508744637, -89.9995805960423, -90.00046983212474), (1.0, 1.0, 1.4375), "Suburbs_Wall_Thin_3x3m_A246", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3800.001, 4479.9966, 2867.0), (90.0, 14.031347933260626, 194.0308272340692), (1.0, 1.0, 1.0), "Suburbs_Wall_Thin_3x3m_A247", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4617.2583, 1998.6311, 2357.3594), (-0.0007288006508744637, -89.9995805960423, -90.00046983212474), (1.0, 1.0, 1.4375), "Suburbs_Wall_Thin_3x3m_A248", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4617.2554, 2298.631, 2357.3638), (-0.0007288006508744637, -89.9995805960423, -90.00046983212474), (1.0, 1.0, 1.4375), "Suburbs_Wall_Thin_3x3m_A249", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2300.0, 4480.0, 2867.0), (90.0, 2.3847534080829136, 182.38441450088305), (1.0, 1.0, 1.0), "Suburbs_Wall_Thin_3x3m_A250", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3963.8281, 2576.462, 2464.3582), (-2.6355913958227538e-05, 90.00005500444897, 89.99969289504277), (0.53125, 0.53125, 1.0), "Suburbs_Wall_Thin_3x3m_A251_174", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2900.0, 2490.0, 2867.0), (90.0, -0.03798023216640636, -0.03834988142420041), (1.0, 1.0, 1.0), "Suburbs_Wall_Thin_3x3m_A252", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2600.0, 2490.0, 2867.0), (90.0, -0.056402055315231264, -0.05675795250080895), (1.0, 1.0, 1.0), "Suburbs_Wall_Thin_3x3m_A253", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4263.828, 2576.462, 2464.3582), (-2.6355913958227538e-05, 90.00005500444897, 89.99969289504277), (0.53125, 0.53125, 1.0), "Suburbs_Wall_Thin_3x3m_A254_175", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3800.0, 2490.0, 2867.0), (90.0, -0.056402055315231264, -0.05675795250080895), (1.0, 1.0, 1.0), "Suburbs_Wall_Thin_3x3m_A255", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4100.0, 2490.0, 2867.0), (90.0, 0.00019544738640171852, -0.00017076352517291334), (1.0, 1.0, 1.0), "Suburbs_Wall_Thin_3x3m_A256", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2563.8281, 2576.462, 2464.3582), (-2.6355913958227538e-05, 90.00005500444897, 89.99969289504277), (0.53125, 0.53125, 1.0), "Suburbs_Wall_Thin_3x3m_A257_178", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3500.001, 2669.998, 2867.0), (90.0, -0.3286864810088668, -180.32903534948485), (1.0, 1.0, 1.0), "Suburbs_Wall_Thin_3x3m_A258", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3800.001, 2669.9966, 2867.0), (90.0, 18.429618932914938, 198.4290810280069), (1.0, 1.0, 1.0), "Suburbs_Wall_Thin_3x3m_A259", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2863.8281, 2576.462, 2464.3582), (-2.6355913958227538e-05, 90.00005500444897, 89.99969289504277), (0.53125, 0.53125, 1.0), "Suburbs_Wall_Thin_3x3m_A260_179", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2600.0, 2669.9993, 2867.0), (90.0, 18.429618932914938, 198.4290810280069), (1.0, 1.0, 1.0), "Suburbs_Wall_Thin_3x3m_A261", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2300.0, 2670.0, 2867.0), (90.0, 1.1922510281542895, 181.19190781947734), (1.0, 1.0, 1.0), "Suburbs_Wall_Thin_3x3m_A262", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4100.0, 4300.0, 3027.0), (90.0, -0.056402055315231264, -0.05675795250080895), (1.0, 1.0, 1.0), "Suburbs_Wall_Thin_3x3m_A263", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4310.0, 4300.0, 2867.0), (90.0, 0.00019544738640171852, -0.00017076352517291334), (1.0, 1.0, 1.0), "Suburbs_Wall_Thin_3x3m_A264", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4617.2524, 2598.631, 2357.368), (-0.0007288006508744637, -89.9995805960423, -90.00046983212474), (1.0, 1.0, 1.4375), "Suburbs_Wall_Thin_3x3m_A265", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4617.2495, 2898.631, 2357.3723), (-0.0007288006508744637, -89.9995805960423, -90.00046983212474), (1.0, 1.0, 1.4375), "Suburbs_Wall_Thin_3x3m_A266", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4617.2466, 3198.631, 2357.3765), (-0.0007288006508744637, -89.9995805960423, -90.00046983212474), (1.0, 1.0, 1.4375), "Suburbs_Wall_Thin_3x3m_A267", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4617.2437, 3498.631, 2357.3809), (-0.0007288006508744637, -89.9995805960423, -90.00046983212474), (1.0, 1.0, 1.4375), "Suburbs_Wall_Thin_3x3m_A268", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4617.241, 3798.6309, 2357.385), (-0.0007288006508744637, -89.9995805960423, -90.00046983212474), (1.0, 1.0, 1.4375), "Suburbs_Wall_Thin_3x3m_A269", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4617.2383, 4098.631, 2357.3892), (-0.0007288006508744637, -89.9995805960423, -90.00046983212474), (1.0, 1.0, 1.4375), "Suburbs_Wall_Thin_3x3m_A270", _folder)
if a: placed += 1
else: skipped += 1

# Batch 72: StaticMesh'Defiled_Statues_H_B' (1 instances)
_mesh_path = "/Game/Art/Assets/Kits/Deco/Defiled/Defiled_Statues_H_B"
_materials = ['/Game/Art/Assets/Kits/Deco/Defiled/Materials/Defiled_Statues_H/MI_Defiled_Statues_H']
_folder = "Reconstruction/BD_BB_OrcTown_Gate/Meshes"
a = spawn_static_mesh(_mesh_path, _materials, (2429.998, 3959.997, 1390.0), (0.0, -179.99978826413437, 0.0), (3.5, 3.5, 3.5), "Defiled_Statues_H2", _folder)
if a: placed += 1
else: skipped += 1

# Batch 73: StaticMesh'Defiled_Statues_H_R' (1 instances)
_mesh_path = "/Game/Art/Assets/Kits/Deco/Defiled/Defiled_Statues_H_R"
_materials = ['/Game/Art/Assets/Kits/Architecture/City/Materials/Defiled_Statues/MI_Defiled_Statues_H_Granite']
_folder = "Reconstruction/BD_BB_OrcTown_Gate/Meshes"
a = spawn_static_mesh(_mesh_path, _materials, (3929.998, 3960.0042, 1390.0), (0.0, -179.99978826413437, 0.0), (3.5, 3.5, 3.5), "Defiled_Statues_H_2", _folder)
if a: placed += 1
else: skipped += 1

# Batch 74: StaticMesh'OrcBanner_B' (1 instances)
_mesh_path = "/Game/Art/Assets/Kits/Deco/Orc/OrcBanner_B"
_materials = ['/Game/Art/Assets/Kits/Deco/Orc/Materials/Orc_Banners/MI_OrcBanners']
_folder = "Reconstruction/BD_BB_OrcTown_Gate/Meshes"
a = spawn_static_mesh(_mesh_path, _materials, (4180.0, 2650.0, 2100.0), (0.0, 90.00001925454477, -0.0), (3.0, 3.0, 3.0), "OrcBanner_E3", _folder)
if a: placed += 1
else: skipped += 1

# Batch 75: StaticMesh'OrcBanner_E' (1 instances)
_mesh_path = "/Game/Art/Assets/Kits/Deco/Orc/OrcBanner_E"
_materials = ['/Game/Art/Assets/Kits/Deco/Orc/Materials/Orc_Banners/MI_OrcBanners']
_folder = "Reconstruction/BD_BB_OrcTown_Gate/Meshes"
a = spawn_static_mesh(_mesh_path, _materials, (2120.0, 1550.0, 2100.0), (0.0, 90.00001925454748, -0.0), (2.0, 2.0, 2.0), "OrcBanner_E_8", _folder)
if a: placed += 1
else: skipped += 1

# Batch 76: StaticMesh'OrcBanner_F' (1 instances)
_mesh_path = "/Game/Art/Assets/Kits/Deco/Orc/OrcBanner_F"
_materials = ['/Game/Art/Assets/Kits/Deco/Orc/Materials/Orc_Banners/MI_OrcBanners']
_folder = "Reconstruction/BD_BB_OrcTown_Gate/Meshes"
a = spawn_static_mesh(_mesh_path, _materials, (2120.0, 2650.0, 2100.0), (0.0, 90.00001925454477, -0.0), (2.0, 2.0, 2.0), "OrcBanner_E2", _folder)
if a: placed += 1
else: skipped += 1

# Batch 77: StaticMesh'Dirt_Mound_A' (8 instances)
_mesh_path = "/Game/Art/Assets/Kits/Misc/Dirt_Mounds/Dirt_Mound_A"
_materials = ['/Game/Art/Assets/Kits/Misc/Dirt_Mounds/Materials/Sururbs_Dirt_DarkELQ_Inst']
_folder = "Reconstruction/BD_BB_OrcTown_Gate/Meshes"
a = spawn_static_mesh(_mesh_path, _materials, (4424.204, 2362.1145, 1207.3556), (32.22168753286567, 90.0000008989356, 2.1143943424908203e-05), (1.0, 1.0, 1.0), "Dirt_Mound_A_73", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1937.741, 2346.015, 1189.2195), (-37.38195680306674, -90.88812646180337, 1.8967375633491583e-05), (1.0, 1.3125, 1.28125), "Dirt_Mound_A2_113", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2146.1384, 503.15524, 981.69104), (-29.512026810033074, -89.99988095916082, 2.0439870858756905e-05), (1.0, 1.0, 1.0), "Dirt_Mound_A3_21", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2146.4526, 189.76378, 888.87787), (-29.436489962386023, -94.48232913495934, 2.2070468040283706), (1.0, 1.0, 1.0), "Dirt_Mound_A4", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2597.2915, 5189.5405, 1088.0646), (26.85037307003957, -90.52111871612917, 1.6747164004579717e-05), (1.0, 1.34375, 1.21875), "Dirt_Mound_A5_48", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3881.5088, 5194.7974, 1104.3086), (-33.05026269857563, 85.39085466609615, 2.850483664773118), (1.0, 1.6875, 1.0), "Dirt_Mound_A6_51", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3779.453, 5832.2935, 885.5327), (-33.05026269857563, 85.39085466609615, 2.850483664773118), (1.0, 1.6875, 1.0), "Dirt_Mound_A7", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2681.8264, 5779.2417, 918.6269), (31.269102586630844, -90.52102470511296, 2.7646355773848976e-05), (1.0, 1.15625, 1.21875), "Dirt_Mound_A8", _folder)
if a: placed += 1
else: skipped += 1

# Batch 78: StaticMesh'Dirt_Mound_D' (1 instances)
_mesh_path = "/Game/Art/Assets/Kits/Misc/Dirt_Mounds/Dirt_Mound_D"
_materials = ['/Game/Art/Assets/Kits/Misc/Dirt_Mounds/Materials/Sururbs_Dirt_DarkELQ_Inst']
_folder = "Reconstruction/BD_BB_OrcTown_Gate/Meshes"
a = spawn_static_mesh(_mesh_path, _materials, (1634.4974, 1432.858, 1102.9576), (0.0, -59.13919270963033, 0.0), (1.0, 1.0, 0.3125), "Dirt_Mound_D_41", _folder)
if a: placed += 1
else: skipped += 1

# Batch 79: StaticMesh'Dirt_Mound_E' (1 instances)
_mesh_path = "/Game/Art/Assets/Kits/Misc/Dirt_Mounds/Dirt_Mound_E"
_materials = ['/Game/Art/Assets/Kits/Misc/Dirt_Mounds/Materials/Sururbs_Dirt_DarkELQ_Inst']
_folder = "Reconstruction/BD_BB_OrcTown_Gate/Meshes"
a = spawn_static_mesh(_mesh_path, _materials, (5620.6333, 1097.1162, 1006.33435), (0.0, 0.0, -0.0), (1.0, 1.0, 0.15625), "Dirt_Mound_E_7", _folder)
if a: placed += 1
else: skipped += 1

# Batch 80: StaticMesh'Dirt_Mound_G' (1 instances)
_mesh_path = "/Game/Art/Assets/Kits/Misc/Dirt_Mounds/Dirt_Mound_G"
_materials = ['/Game/Art/Assets/Kits/Misc/Dirt_Mounds/Materials/Sururbs_Dirt_DarkELQ_Inst']
_folder = "Reconstruction/BD_BB_OrcTown_Gate/Meshes"
a = spawn_static_mesh(_mesh_path, _materials, (5987.3833, 1031.3567, 1000.7323), (0.0, -9.035400830377727, 0.0), (1.0, 1.125, 1.5625), "Dirt_Mound_G_2", _folder)
if a: placed += 1
else: skipped += 1

# Batch 81: StaticMesh'Dirt_Mound_H' (36 instances)
_mesh_path = "/Game/Art/Assets/Kits/Misc/Dirt_Mounds/Dirt_Mound_H"
_materials = ['/Game/Art/Assets/Kits/Misc/Dirt_Mounds/Materials/Sururbs_Dirt_DarkELQ_Inst']
_folder = "Reconstruction/BD_BB_OrcTown_Gate/Meshes"
a = spawn_static_mesh(_mesh_path, _materials, (5495.1104, 499.6546, 1006.33435), (0.0, 0.0, -0.0), (1.0, 1.0, 0.5625), "Dirt_Mound_H_13", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4355.6997, 1701.9767, 1105.463), (0.0, -25.000061959545324, 0.0), (1.46875, 1.78125, 0.375), "Dirt_Mound_H10", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4401.814, 2037.4884, 1105.463), (0.0, -75.00006049627947, 0.0), (1.46875, 1.78125, 0.8125), "Dirt_Mound_H11", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3981.568, 1399.0505, 1098.9692), (0.0, -65.00012172744646, 0.0), (1.0, 1.0, 1.53125), "Dirt_Mound_H12_96", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4117.0215, 1281.1592, 1100.0571), (0.0, -75.00006049627947, 0.0), (1.0, 1.0, 0.53125), "Dirt_Mound_H13_99", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3507.927, 2512.6384, 1206.3344), (0.0, -25.000061959545324, 0.0), (1.0, 1.0, 1.0), "Dirt_Mound_H14_21", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3600.4783, 2555.8118, 1206.3344), (0.0, 175.00008259598715, -0.0), (1.0, 1.0, 1.8125), "Dirt_Mound_H15", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2869.631, 1437.8375, 1105.0571), (0.0, -75.00006049627947, 0.0), (1.5143709, 1.0, 0.19183151), "Dirt_Mound_H16", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2685.4705, 1504.7135, 1100.0571), (0.0, 105.00015274156611, -0.0), (1.0, 1.0, 0.3125), "Dirt_Mound_H17", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2896.3894, 1592.3936, 1105.8071), (0.0, -140.0000576472962, 0.0), (1.0, 1.5, 0.13208783), "Dirt_Mound_H18", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2200.0, 1400.0, 1105.8431), (0.0, 0.0, -0.0), (1.0, 1.0, 1.25), "Dirt_Mound_H19", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5322.006, 845.2034, 1006.33435), (0.0, -25.000061959545324, 0.0), (1.34375, 1.53125, 0.375), "Dirt_Mound_H2", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2243.4805, 1490.7644, 1105.8431), (0.0, 51.51295794804622, -0.0), (1.0, 1.0, 1.25), "Dirt_Mound_H20", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4724.5645, 2052.6504, 1412.8285), (26.638305282148043, -11.726562369679424, -5.3168643584966295), (1.25, 1.84375, 1.15625), "Dirt_Mound_H21_81", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2365.961, 4180.7954, 1406.3344), (0.0, -10.166991488536862, 0.0), (1.0, 1.0, 1.5625), "Dirt_Mound_H22_86", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2235.2651, 3749.6873, 1306.3344), (0.0, 0.0, -0.0), (1.5, 1.125, 1.625), "Dirt_Mound_H23_34", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4604.5645, 2052.6504, 1412.8285), (36.40732722667872, -13.045591424007979, -7.8301993551101), (1.25, 1.84375, 2.25), "Dirt_Mound_H24", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4089.7656, 4120.9766, 1405.9688), (0.0, 0.0, -0.0), (1.0, 1.0, 1.0), "Dirt_Mound_H25", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3902.4004, 4231.629, 1405.9688), (0.0, 0.0, -0.0), (1.0, 1.0, 1.0), "Dirt_Mound_H26", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4215.2466, 525.8127, 1006.33435), (0.0, 0.0, -0.0), (1.0, 1.0, 1.46875), "Dirt_Mound_H27_132", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2040.2703, 1222.1133, 1097.6779), (0.0, -32.81524753138993, 0.0), (1.71875, 1.0, 0.59375), "Dirt_Mound_H28", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2860.5745, 1293.0734, 1105.0571), (0.0, -26.253448767046226, 0.0), (1.0, 1.580255, 0.19330494), "Dirt_Mound_H29", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2691.4312, 2595.9766, 1306.3344), (0.0, -51.767181509947456, 0.0), (0.59375, 0.75, 0.5625), "Dirt_Mound_H3_90", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2564.0952, 1289.218, 1105.0571), (0.0, -53.362091494230626, 0.0), (1.0, 1.0, 0.17260952), "Dirt_Mound_H30", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4272.6846, 305.20465, 941.7017), (0.0, 0.0, -28.62790024959601), (1.0, 1.0, 1.8981313), "Dirt_Mound_H31", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4436.347, 305.20477, 941.7017), (0.0, 0.0, -28.62790024959601), (1.0, 1.0, 1.898131), "Dirt_Mound_H32", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4368.8086, 275.46973, 941.7018), (0.0, 0.0, -33.836090364895185), (1.0, 1.0, 1.898131), "Dirt_Mound_H33", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4336.294, 193.42674, 871.57825), (-27.32605440217263, -122.39893056503583, 17.81091285832692), (0.65235114, 0.65235114, 0.90854436), "Dirt_Mound_H34", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2877.4155, 3410.2334, 1233.6039), (14.216149331731845, 167.62721676704152, -3.0833128050910195), (0.9099561, 0.9099561, 1.0), "Dirt_Mound_H35", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1908.53, 3379.2173, 1306.3344), (0.0, -116.04945755595213, 0.0), (1.5625, 1.21875, 1.4375), "Dirt_Mound_H36", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2758.9421, 2492.9023, 1206.3517), (0.0, -30.461881226510933, 0.0), (1.0, 1.0, 1.71875), "Dirt_Mound_H4_102", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4097.7324, 3660.9207, 1306.3344), (0.0, -54.88711853349015, 0.0), (1.25, 1.0, 1.34375), "Dirt_Mound_H5_117", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4455.402, 2787.3535, 1306.3344), (0.0, 0.0, -0.0), (1.0625, 1.28125, 1.65625), "Dirt_Mound_H6_120", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2235.2651, 3649.6873, 1304.9336), (0.0, 0.0, -0.0), (1.5, 1.125, 1.625), "Dirt_Mound_H7_123", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1888.53, 2824.2173, 1306.3344), (0.0, -82.29958857472928, 0.0), (1.5625, 1.21875, 1.4375), "Dirt_Mound_H8_163", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4757.1514, 1658.2146, 1102.2125), (0.0, -25.000061959545324, 0.0), (1.46875, 1.78125, 0.375), "Dirt_Mound_H9", _folder)
if a: placed += 1
else: skipped += 1

# Batch 82: StaticMesh'Dirt_Mound_I' (23 instances)
_mesh_path = "/Game/Art/Assets/Kits/Misc/Dirt_Mounds/Dirt_Mound_I"
_materials = ['/Game/Art/Assets/Kits/Misc/Dirt_Mounds/Materials/Sururbs_Dirt_DarkELQ_Inst']
_folder = "Reconstruction/BD_BB_OrcTown_Gate/Meshes"
a = spawn_static_mesh(_mesh_path, _materials, (5268.94, 1606.4171, 998.3867), (0.0, -15.000058335092751, 0.0), (1.0, 1.0, 1.09375), "Dirt_Mound_I_10", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4441.0493, 1614.4688, 1097.7345), (0.0, 0.0, -0.0), (1.0, 1.0, 1.1875), "Dirt_Mound_I10_18", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1667.6562, 579.48444, 1006.33435), (0.0, -21.51583888438345, 0.0), (1.0, 1.0, 0.6875), "Dirt_Mound_I11_25", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1391.4111, 1553.5464, 1106.3344), (0.0, 6.070561153662415, -0.0), (1.0, 1.0, 1.0), "Dirt_Mound_I12_28", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1216.7063, 1265.7247, 1106.3344), (0.0, 21.469281696021664, -0.0), (1.0, 1.0, 1.0), "Dirt_Mound_I13", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3847.9844, 5316.01, 1009.3988), (0.0, 0.0, -0.0), (1.0, 1.0, 1.0), "Dirt_Mound_I14_10", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2565.355, 5159.022, 1009.3988), (0.0, 0.0, -0.0), (1.0, 1.0, 1.0), "Dirt_Mound_I15", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2778.7769, 5780.4736, 806.3343), (0.0, 0.0, -0.0), (1.0, 1.0, 1.0), "Dirt_Mound_I16_14", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3728.328, 5874.9863, 806.3343), (0.0, 0.0, -0.0), (1.0, 1.0, 1.0), "Dirt_Mound_I17", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3172.517, 5040.17, 1007.8758), (0.0, -30.000063894566395, 0.0), (1.0, 1.0, 1.0), "Dirt_Mound_I18_18", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4698.1914, 1667.778, 1090.0), (0.0, 0.0, -0.0), (1.5, 1.0, 2.21875), "Dirt_Mound_I19_19", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3671.9785, 2387.3994, 1100.0048), (0.0, -59.019561096778844, 0.0), (1.0, 1.0, 1.0), "Dirt_Mound_I2_79", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4576.2783, 797.72076, 1006.33453), (0.0, 0.0, -0.0), (1.0, 1.0, 0.84375), "Dirt_Mound_I21_141", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5937.722, 699.7659, 1006.6443), (0.0, 135.66042381446454, -0.0), (1.0, 1.0, 0.1875), "Dirt_Mound_I26_34", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (6051.579, 1537.757, 1006.6443), (0.0, 135.66042381446454, -0.0), (1.0, 1.0, 0.1875), "Dirt_Mound_I27", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5961.5786, 1262.8564, 1006.6443), (0.0, 149.51175094281734, -0.0), (0.65625, 0.78125, 0.125), "Dirt_Mound_I28", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3650.4387, 3504.8706, 1204.7863), (0.0, 0.0, -0.0), (0.65625, 0.71875, 0.90625), "Dirt_Mound_I3_82", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2705.983, 2612.8472, 1205.0139), (0.0, -36.610717880620584, 0.0), (0.6875, 0.71875, 1.0), "Dirt_Mound_I4_96", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2890.1018, 2478.37, 1104.914), (0.0, 0.0, -0.0), (1.0, 0.78125, 1.0), "Dirt_Mound_I5_99", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1895.1866, 2319.5308, 1100.7041), (0.0, -8.247100897725394, 0.0), (1.0, 1.0, 1.03125), "Dirt_Mound_I6_105", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2737.8967, 3504.8706, 1204.7863), (0.0, 0.0, -0.0), (0.65625, 0.71875, 0.90625), "Dirt_Mound_I7", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2686.7468, 4208.772, 1203.9385), (0.0, 0.0, -0.0), (1.0, 1.0, 1.3125), "Dirt_Mound_I8_150", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3787.232, 4250.349, 1203.9385), (0.0, 37.483213793765465, -0.0), (1.0, 1.0, 1.3125), "Dirt_Mound_I9", _folder)
if a: placed += 1
else: skipped += 1

# Batch 83: StaticMesh'Suburbs_Dirt_Mound_A' (12 instances)
_mesh_path = "/Game/Art/Assets/Kits/Misc/Dirt_Mounds/Suburbs_Dirt_Mound_A"
_materials = ['/Game/Art/Assets/Kits/Misc/Dirt_Mounds/Materials/Sururbs_Dirt_DarkELQ_Inst']
_folder = "Reconstruction/BD_BB_OrcTown_Gate/Meshes"
a = spawn_static_mesh(_mesh_path, _materials, (3251.6929, 2746.9143, 1195.2166), (0.0, 0.0, -0.0), (1.4444183, 1.7836499, 0.5710677), "Suburbs_Dirt_Mound_A_95", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3325.0808, 4057.7659, 1196.4648), (0.0, 101.26171339933968, -0.0), (1.444418, 1.78365, 0.30335996), "Suburbs_Dirt_Mound_A10", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3126.0808, 3937.3762, 1196.245), (0.0, 101.26171339933968, -0.0), (1.444418, 1.78365, 0.744681), "Suburbs_Dirt_Mound_A11", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2999.0808, 3619.3762, 1195.8041), (0.0, 101.26171339933968, -0.0), (2.2562253, 1.78365, 0.34829855), "Suburbs_Dirt_Mound_A12", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2956.0808, 3887.3762, 1200.6827), (0.0, 101.26171339933968, -0.0), (2.256225, 1.78365, 0.29493397), "Suburbs_Dirt_Mound_A13", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3148.207, 3763.3762, 1201.5829), (0.0, 101.26178760730913, -0.0), (1.7071007, 1.9956554, 0.5054455), "Suburbs_Dirt_Mound_A14", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3374.9517, 3231.3862, 1195.5878), (0.0, 0.0, -0.0), (1.444418, 1.78365, 1.0), "Suburbs_Dirt_Mound_A3", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3401.0503, 3036.4907, 1195.5878), (0.0, 0.0, -0.0), (1.444418, 1.78365, 1.0), "Suburbs_Dirt_Mound_A4", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3367.9343, 2880.5408, 1179.9283), (0.0, -50.620052775115276, 0.0), (1.8180279, 1.78365, 1.4310709), "Suburbs_Dirt_Mound_A5", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3292.8171, 3106.2344, 1195.5878), (0.0, -50.620052775115276, 0.0), (1.444418, 1.78365, 1.0), "Suburbs_Dirt_Mound_A6", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3303.0808, 2707.3762, 1194.9877), (0.0, 101.26171339933968, -0.0), (1.444418, 1.78365, 0.919236), "Suburbs_Dirt_Mound_A7", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3325.0808, 3878.3762, 1190.8141), (0.0, 101.26171339933968, -0.0), (1.444418, 1.78365, 0.6558299), "Suburbs_Dirt_Mound_A9", _folder)
if a: placed += 1
else: skipped += 1

# Batch 84: StaticMesh'Dimril_Gate_Ornament_A' (2 instances)
_mesh_path = "/Game/Art/Assets/Landmarks/Dimril_Gate/Dimril_Gate_Ornament_A"
_materials = ['/Game/Art/Assets/Kits/Architecture/Suburbs/Materials/Suburbs_Trim_Sheet_A/MI_Suburbs_Trim_Sheet_A']
_folder = "Reconstruction/BD_BB_OrcTown_Gate/Meshes"
a = spawn_static_mesh(_mesh_path, _materials, (3200.0, 4320.0, 2600.0), (0.0, 90.00001925454748, -0.0), (0.625, 0.625, 0.625), "Dimril_Gate_Ornament_A_132", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3200.0, 4380.0, 2600.0), (0.0, 90.00001925454748, -0.0), (0.625, 0.625, 0.625), "Dimril_Gate_Ornament_A2_197", _folder)
if a: placed += 1
else: skipped += 1

# Batch 85: StaticMesh'PWM_Nordic_8x8x8_A' (25 instances)
_mesh_path = "/Game/Unshippable/Whitebox/Rocks/Meshes/PWM_Nordic_8x8x8_A"
_materials = ['/Game/Environments/ProcTexturing/ProcMaterial_Quarry_2mx5m_B2']
_folder = "Reconstruction/BD_BB_OrcTown_Gate/Meshes"
a = spawn_static_mesh(_mesh_path, _materials, (4930.8486, 3133.7537, 1266.0684), (-13.811858723515165, -0.5768432470751341, 2.828463993922177), (1.0, 1.0, 1.0), "PWM_Nordic_8x8x8_A37_147", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4680.8486, 3133.7537, 2846.0684), (0.915905020407222, -0.9336242614896368, 0.25739099027746765), (1.0, 1.0, 1.0), "PWM_Nordic_8x8x8_A38", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1032.8059, 1375.4468, 1266.8545), (15.806397040916439, -15.123011796923663, -4.41940238904162), (1.0, 1.0, 1.0), "PWM_Nordic_8x8x8_A39", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (709.9886, 785.0107, 1253.0813), (-15.806822977204146, 164.87762526215923, 4.419444241551864), (1.0, 1.0, 1.0), "PWM_Nordic_8x8x8_A40", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1554.609, 879.7167, 2909.2544), (70.31233433830172, -91.94873292851565, 102.36250851652439), (1.0, 1.0, 1.0), "PWM_Nordic_8x8x8_A41", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1749.1132, 1505.1775, 2928.4343), (-19.99310175261187, 15.895657857711456, -5.635894475503373), (1.0, 1.0, 1.0), "PWM_Nordic_8x8x8_A42", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4680.8486, 2623.7537, 2866.0684), (0.9159077978227466, 179.06622095384935, 0.25739132908852824), (1.0, 1.0, 1.0), "PWM_Nordic_8x8x8_A43", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1809.9885, 4285.0107, 1253.0813), (-14.795989157278976, 139.56202423769957, 7.14915222407937), (1.0, 1.0, 1.0), "PWM_Nordic_8x8x8_A44", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4548.4062, 4310.894, 1425.7327), (-13.686035885678143, 35.17096609042503, -3.39035031973837), (1.0, 1.0, 1.0), "PWM_Nordic_8x8x8_A45", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4980.7505, 1039.3433, 2721.1636), (15.915750044119376, 174.8103065027162, 0.2676151648898597), (1.0, 1.0, 1.0), "PWM_Nordic_8x8x8_A46", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3892.4038, 72.98369, 2926.865), (52.904980202652716, -96.69968477367453, -2.3303855326415843), (1.0, 1.0, 1.0), "PWM_Nordic_8x8x8_A47", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4094.8438, 5984.658, 970.5171), (-4.066925130063504, 14.90596376386343, 2.8456168996121978), (1.0, 1.0, 1.0), "PWM_Nordic_8x8x8_A48", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2484.8438, 5984.658, 970.5171), (15.25018258431401, -4.576537398391013, 8.077800346333776), (1.0, 1.0, 1.0), "PWM_Nordic_8x8x8_A49", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3799.0955, 5989.2534, 2874.79), (60.80191666551794, 20.198696281311484, 5.82635347145385), (1.0, 1.0, 1.0), "PWM_Nordic_8x8x8_A50", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2869.0955, 5989.2534, 2674.79), (51.61483659177081, 154.26087448843285, 155.56455759179929), (1.0, 1.0, 1.375), "PWM_Nordic_8x8x8_A51", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (6030.8486, 233.75366, 1236.0684), (-6.723387746230895, -59.294152170606665, -4.345184466933295), (1.0, 1.0, 1.0), "PWM_Nordic_8x8x8_A52", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (6280.8486, 903.75366, 1236.0684), (-6.723388553388317, -179.29406132951948, -4.345184797977589), (1.0, 1.0, 1.0), "PWM_Nordic_8x8x8_A53", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4297.8755, 4829.177, 1400.8735), (-2.8489989235368367, -5.0939634407864745, 4.064497778662082), (1.0, 1.0, 1.0), "PWM_Nordic_8x8x8_A54", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4100.013, 4952.159, 2839.189), (-0.5631701942552669, -78.75474999900534, -51.08119548471652), (1.5, 1.0, 1.0), "PWM_Nordic_8x8x8_A55", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2594.1877, 5214.227, 2799.2373), (-4.199434297633309, 82.29084173642468, -75.84135902452253), (1.5, 1.0, 1.0), "PWM_Nordic_8x8x8_A56", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5820.221, 1839.0688, 1414.6261), (-6.723388677571037, -94.29393871629554, -4.345185795855744), (1.0, 1.0, 1.0), "PWM_Nordic_8x8x8_A57", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4664.8896, 203.03932, 2816.7944), (-61.798918707438226, 99.20030023575902, -10.470346143465225), (1.0, 1.0, 1.0), "PWM_Nordic_8x8x8_A58", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5464.592, 244.81535, 2587.396), (-6.06576613546162, -97.06509487708061, -160.35477085021716), (1.21875, 1.0, 1.0), "PWM_Nordic_8x8x8_A59", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1467.2593, 224.2768, 2875.8853), (9.017842150991754, 87.57049964225105, -94.9359964870735), (1.0, 1.0, 1.375), "PWM_Nordic_8x8x8_A60", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1432.8059, 3325.4468, 1716.8545), (5.956181226226775, 170.2102437232189, -2.6609497119703476), (1.0, 1.0, 1.125), "PWM_Nordic_8x8x8_A61", _folder)
if a: placed += 1
else: skipped += 1

# Batch 86: StaticMesh'PWM_Quarry_1x1x1_A' (33 instances)
_mesh_path = "/Game/Unshippable/Whitebox/Rocks/Meshes/PWM_Quarry_1x1x1_A"
_materials = ['/Game/Environments/ProcTexturing/ProcMaterial_Quarry_Atlas_1']
_folder = "Reconstruction/BD_BB_OrcTown_Gate/Meshes"
a = spawn_static_mesh(_mesh_path, _materials, (1700.0, 2150.0, 1550.0), (0.0, -20.000060948281234, 0.0), (1.0, 1.90625, 1.78125), "PWM_Quarry_1x1x1_A_32", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3609.4941, 4564.923, 2968.7383), (29.437985507744745, -81.6824568611206, -4.411497473788777), (1.5625, 1.5625, 1.125), "PWM_Quarry_1x1x1_A10", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (910.59033, 285.3746, 1475.1482), (0.0, -23.447418868997875, 0.0), (1.5, 2.15625, 1.40625), "PWM_Quarry_1x1x1_A11_108", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3004.212, 524.499, 2900.3079), (0.0, 0.0, -0.0), (1.0, 1.0, 1.0), "PWM_Quarry_1x1x1_A12_132", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3496.686, 524.499, 2911.691), (78.9983920507455, 0.0, -0.0), (1.5625, 1.4375, 1.96875), "PWM_Quarry_1x1x1_A13", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5561.5635, 319.347, 1688.1864), (0.0, 0.0, -0.0), (1.0, 1.21875, 1.9375), "PWM_Quarry_1x1x1_A14_138", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1742.4814, 494.67075, 2440.2402), (0.0, 170.8749586832108, -0.0), (1.75, 2.46875, 1.0), "PWM_Quarry_1x1x1_A15_147", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4526.444, 2525.1482, 1326.6637), (-5.419553481739114, 79.64145507132207, -9.703245428048168), (2.731225, 1.0, 1.625478), "PWM_Quarry_1x1x1_A152_436", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4645.834, 2364.167, 874.8921), (-78.8974135340278, -146.44393432179888, -119.37368810103618), (1.732566, 1.0, 2.056599), "PWM_Quarry_1x1x1_A153_445", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1720.4148, 1576.009, 1326.6637), (-5.419555318104248, -145.3585810660558, -9.703245082132707), (2.731225, 1.0, 1.625478), "PWM_Quarry_1x1x1_A154", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1713.8137, 2017.0325, 874.8921), (-78.89690878769653, -1.4437750208747713, -119.37350501752185), (1.732566, 1.0, 2.056599), "PWM_Quarry_1x1x1_A155", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1173.8298, 1351.5066, 2128.4106), (-3.6622931178723896, -115.48239029690738, -10.487365271287995), (2.731225, 1.25, 2.6875), "PWM_Quarry_1x1x1_A156", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1154.0525, 1345.5453, 2481.3596), (-1.7971801257365263, -105.64618117396978, -10.957091950684518), (3.9375, 1.25, 2.6875), "PWM_Quarry_1x1x1_A157", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1073.3337, 1114.9623, 2108.4543), (-0.3422240231816754, 58.69200644371397, 175.5392039396159), (2.731225, 1.25, 3.15625), "PWM_Quarry_1x1x1_A158", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (886.8116, 605.44147, 1742.3961), (-3.6622931178723896, -115.48239029690738, -10.487365271287995), (3.1875, 1.40625, 2.6875), "PWM_Quarry_1x1x1_A159", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3600.6743, 4453.49, 2848.0688), (-0.29953010873792296, -82.76215435640552, -4.151612016110844), (1.5625, 2.34375, 2.2834044), "PWM_Quarry_1x1x1_A16", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4739.372, 2395.2344, 1486.819), (3.7369543884562098, -75.88724032767678, 10.46208868897653), (3.96875, 1.0, 1.9375), "PWM_Quarry_1x1x1_A167", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1404.1952, 1581.5123, 1486.819), (3.7369533894364912, 54.11272441434272, 10.462677068675822), (3.96875, 1.0, 1.9375), "PWM_Quarry_1x1x1_A168", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1087.7543, 1171.8837, 1924.1067), (1.8750030782627864, 63.95031558603531, 0.9466567168482298), (3.96875, 1.0, 2.875), "PWM_Quarry_1x1x1_A169", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2847.75, 4454.232, 2797.6345), (-0.927612001581714, -82.81553951463466, -3.5986933154918233), (2.37125, 2.34375, 2.1136174), "PWM_Quarry_1x1x1_A17", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (975.6815, 633.8655, 2486.5222), (1.6821316101426147, 73.95252066307263, -7.143006412385554), (3.96875, 1.34375, 3.46875), "PWM_Quarry_1x1x1_A170", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4809.372, 2395.2344, 2586.8188), (4.941238174207242, -76.25566603662556, 5.5952359571036485), (3.96875, 1.0, 2.71875), "PWM_Quarry_1x1x1_A171", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2487.9565, 5330.0825, 1486.819), (3.7369540378454627, 59.11270204557675, 10.4627483703199), (3.96875, 1.0, 1.9375), "PWM_Quarry_1x1x1_A172", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2638.3267, 5936.354, 1492.1749), (-4.848236191500433, 59.0622582281092, -4.404296384312886), (3.96875, 1.4375, 2.90625), "PWM_Quarry_1x1x1_A173", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4716.57, 1696.5685, 1120.0), (0.0, 45.00007048643773, -0.0), (2.34375, 2.34375, 2.34375), "PWM_Quarry_1x1x1_A18_23", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4600.0, 2333.998, 1316.9785), (0.0, 0.0, -0.0), (1.375, 1.46875, 1.625), "PWM_Quarry_1x1x1_A2_36", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4360.0, 4010.0, 2020.0), (0.0, 10.000387298346714, -0.0), (1.0, 2.15625, 2.125), "PWM_Quarry_1x1x1_A3_211", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4507.08, 3578.9937, 2120.0), (0.0, -169.99964066856705, 0.0), (1.0, 2.15625, 2.4375), "PWM_Quarry_1x1x1_A4", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4524.4434, 3480.5122, 2370.0), (0.0, -169.99964066856705, 0.0), (1.0, 2.5625, 2.4375), "PWM_Quarry_1x1x1_A5", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2421.6946, 4500.9277, 2736.6528), (35.00001253493685, 0.0, -0.0), (1.75, 2.09375, 1.6875), "PWM_Quarry_1x1x1_A6_93", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3396.1277, 5229.585, 2864.312), (-9.999909140988397, -0.00012207031708694684, 179.99995901886874), (4.2532287, 4.7902117, 1.625), "PWM_Quarry_1x1x1_A7_98", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2984.9634, 4437.5127, 2968.7383), (15.000002689379617, 0.0, -0.0), (1.5625, 1.5625, 1.0), "PWM_Quarry_1x1x1_A8_101", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3494.1882, 4437.5127, 2968.7383), (29.437986727377986, -16.68234282383148, -4.411498635895653), (1.5625, 1.5625, 1.125), "PWM_Quarry_1x1x1_A9", _folder)
if a: placed += 1
else: skipped += 1

# Batch 87: StaticMesh'PWM_Quarry_1X1x1_C' (17 instances)
_mesh_path = "/Game/Unshippable/Whitebox/Rocks/Meshes/PWM_Quarry_1X1x1_C"
_materials = ['/Game/Environments/ProcTexturing/ProcMaterial_Quarry_Atlas_1']
_folder = "Reconstruction/BD_BB_OrcTown_Gate/Meshes"
a = spawn_static_mesh(_mesh_path, _materials, (4520.0, 2300.0, 1150.0), (1.0501800349966712e-07, -74.99998645981223, -89.99999314361202), (2.46875, 1.65625, 1.65625), "PWM_Quarry_1X1x1_C_64", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4670.0, 2050.0, 1150.0), (-5.701251387605026e-07, -129.99993931511375, -89.99994298344558), (2.46875, 2.6875, 1.65625), "PWM_Quarry_1X1x1_C11", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4875.9893, 1859.5364, 1123.3077), (-17.009615387740947, 38.67716183459843, -3.418183556671456), (1.482634, 3.223155, 2.106272), "PWM_Quarry_1X1x1_C12_405", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1793.8796, 2179.6968, 1123.3077), (-17.009613537022343, 163.6771026393606, -3.4181823142728387), (1.482634, 3.223155, 2.106272), "PWM_Quarry_1X1x1_C13", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5230.871, 1079.9609, 2095.0466), (-13.082550799577948, 27.844300732031062, -0.21264642792172894), (1.482634, 3.223155, 2.106272), "PWM_Quarry_1X1x1_C14", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5330.871, 729.96094, 2095.0466), (-13.082550799577948, 27.844300732031062, -0.21264642792172894), (1.482634, 3.223155, 2.106272), "PWM_Quarry_1X1x1_C15", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4580.0, 2170.0, 1150.0), (-5.701251387605026e-07, -129.99993931511375, -89.99994298344558), (2.46875, 2.34375, 1.65625), "PWM_Quarry_1X1x1_C16", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4520.0, 2210.0, 1150.0), (1.0501800349966712e-07, -74.99998645981223, -89.99999314361202), (3.03125, 2.625, 2.0625), "PWM_Quarry_1X1x1_C17", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3575.0, 6359.0, 912.0), (-9.8465574602413, -100.1512074919476, 1.753807256273651), (1.0, 1.0, 2.7516952), "PWM_Quarry_1X1x1_C18_123", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3575.0, 6359.0, 1184.0), (-9.846558204988481, -100.15120765630272, 1.7538081481679548), (1.0, 1.0, 2.751695), "PWM_Quarry_1X1x1_C19", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1870.0, 870.0, 2570.0), (0.0, 0.0, -89.99999818714215), (1.21875, 1.5625, 2.5), "PWM_Quarry_1X1x1_C2_130", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5690.0, 440.0, 1620.0), (0.0, 0.0, -0.0), (1.9375, 1.0, 1.71875), "PWM_Quarry_1X1x1_C3_197", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5508.4795, 1591.576, 1716.026), (0.0, 0.0, -20.000060948281234), (1.96875, 1.0, 1.90625), "PWM_Quarry_1X1x1_C4_3", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4060.0, 1410.0, 1110.0), (0.0, -10.000030597161448, 0.0), (1.0, 1.0, 1.0), "PWM_Quarry_1X1x1_C5_83", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3712.5305, 1596.6549, 1110.0), (0.0, -80.0000667145408, 0.0), (0.375, 0.375, 0.375), "PWM_Quarry_1X1x1_C6", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3638.4553, 1653.1586, 1081.6041), (10.000023241498342, -124.99988650901793, -89.99994869060656), (0.53125, 0.53125, 0.53125), "PWM_Quarry_1X1x1_C7", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3660.6785, 1586.7152, 1069.7538), (-29.888060088969787, 130.65567790932548, 73.76452137719058), (0.53125, 0.53125, 0.53125), "PWM_Quarry_1X1x1_C8", _folder)
if a: placed += 1
else: skipped += 1

# Batch 88: StaticMesh'PWM_Quarry_2x2x2_A' (89 instances)
_mesh_path = "/Game/Unshippable/Whitebox/Rocks/Meshes/PWM_Quarry_2x2x2_A"
_materials = ['/Game/Environments/ProcTexturing/ProcMaterial_Quarry_Atlas_1']
_folder = "Reconstruction/BD_BB_OrcTown_Gate/Meshes"
a = spawn_static_mesh(_mesh_path, _materials, (1910.0, 3740.0, 2330.0), (-25.00000055343977, 0.0, -0.0), (1.0, 1.0, 1.4375), "PWM_Quarry_2x2x2_A_114", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5667.21, 1263.8926, 1866.3286), (75.86617431171018, 45.110237750544115, 45.10996879957646), (1.0, 2.15625, 2.71875), "PWM_Quarry_2x2x2_A10_205", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5718.5576, 753.3452, 1821.5923), (73.59212660224637, -37.007411398798595, 120.01328541800265), (1.0, 2.15625, 2.71875), "PWM_Quarry_2x2x2_A11", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (6104.1724, 840.0287, 1593.2406), (18.562410581447292, -26.383790651911966, 7.896772240826563), (0.9375, 2.5, 0.96875), "PWM_Quarry_2x2x2_A12", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4912.1963, 394.95288, 2444.7583), (-16.959261419233016, 3.898904153083273, -84.79513807730399), (1.84375, 1.0, 2.28125), "PWM_Quarry_2x2x2_A13_143", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3980.0, 1550.0, 1110.0), (0.0, 0.0, -0.0), (1.0, 1.0, 1.0), "PWM_Quarry_2x2x2_A14_77", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1510.999, 1641.0469, 1115.7047), (0.0, 30.000038820411323, -0.0), (2.21875, 1.6875, 1.0), "PWM_Quarry_2x2x2_A15_63", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4833.3896, 2238.1104, 1873.3185), (-0.4812317500023561, 110.10499460824099, 0.19274617783776568), (2.5625, 0.716357, 1.34375), "PWM_Quarry_2x2x2_A156_378", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1393.8096, 1620.4038, 1953.046), (-0.4812011363259636, -129.8948912843441, 0.19274626096839234), (2.091547, 0.716357, 1.0), "PWM_Quarry_2x2x2_A157", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4583.3896, 3318.1104, 1673.3185), (-0.48123172643893175, 100.10500013602523, 0.19274600118090177), (2.5625, 0.716357, 2.09375), "PWM_Quarry_2x2x2_A158", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4823.3896, 2288.1104, 2293.3184), (-0.4812316715238288, 105.10498649269351, 0.19274598973798393), (2.5625, 0.716357, 1.34375), "PWM_Quarry_2x2x2_A159", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1762.6973, 1701.008, 1514.9745), (0.0, 40.00004110866871, -0.0), (1.0, 1.0, 1.21875), "PWM_Quarry_2x2x2_A16_69", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4846.0547, 2013.3228, 1371.039), (-3.6607361015856124, 104.52282394359445, -10.488618748462242), (1.887893, 1.0, 1.0), "PWM_Quarry_2x2x2_A160_402", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4730.298, 2096.134, 953.09467), (-0.84112564447414, 119.26219507384516, -11.06963922143802), (1.630768, 1.0, 1.0), "PWM_Quarry_2x2x2_A161_408", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4879.126, 2283.1885, 1535.0835), (3.660742453145694, -75.4771862176676, -169.51206987486773), (2.673416, 1.0, 1.0), "PWM_Quarry_2x2x2_A162", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1805.6078, 2009.7538, 1361.1487), (-3.660674215493893, -95.47716044799989, -10.488952111595827), (2.0625, 1.0, 1.21875), "PWM_Quarry_2x2x2_A163", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4739.298, 2605.538, 1723.2561), (-78.89719858380217, -146.44562431546245, -119.37197118736428), (1.0, 1.0, 1.740382), "PWM_Quarry_2x2x2_A164_424", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1798.3608, 2285.039, 953.09467), (-0.8410647075657243, -95.73784984616802, -11.07016027689335), (1.630768, 1.0, 1.0), "PWM_Quarry_2x2x2_A165", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1643.218, 1757.1792, 1535.0835), (3.6607412134718706, 64.52285988780659, -169.51206790441861), (2.673416, 1.0, 1.0), "PWM_Quarry_2x2x2_A166", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4687.8896, 2431.6443, 1117.3256), (2.154836067749654, -96.06384518656985, 9.431673001286729), (1.0, 0.378956, 1.0), "PWM_Quarry_2x2x2_A167_442", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1258.6326, 1441.7366, 1698.2214), (-78.89720543071397, -16.445631623726356, -119.37187995266623), (1.21875, 1.0, 1.740382), "PWM_Quarry_2x2x2_A168", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1640.6603, 1985.8799, 1117.3256), (2.1548353989209468, 48.93621548337476, 9.432100166093043), (1.0, 0.378956, 1.0), "PWM_Quarry_2x2x2_A169", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1553.0286, 1668.3145, 1935.3442), (0.0, 40.00002696525857, -0.0), (1.9375, 1.0, 2.4375), "PWM_Quarry_2x2x2_A17_72", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1157.9597, 1262.6477, 1371.039), (-3.660674737357025, -130.47717046633693, -10.488952584470155), (1.887893, 1.0, 1.5625), "PWM_Quarry_2x2x2_A170", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1029.0715, 1140.3616, 1633.2561), (-78.89711985720962, -171.44596078171725, -119.37196779419087), (1.0, 1.0, 1.740382), "PWM_Quarry_2x2x2_A171", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1569.628, 2126.631, 1908.2981), (-1.7951359189168548, -105.64095822450057, -10.959868184685991), (2.65625, 1.0, 1.1875), "PWM_Quarry_2x2x2_A172", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1450.1316, 1977.2825, 2346.8708), (-3.6606747224950626, -115.47716017923973, -10.488950647145112), (3.3125, 1.0, 1.6875), "PWM_Quarry_2x2x2_A173", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1254.0809, 1208.8345, 2543.7024), (-5.469482551758867, 61.221010554622985, 151.3853755378043), (3.3125, 1.0, 3.03125), "PWM_Quarry_2x2x2_A174", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1660.8439, 2626.9634, 2074.061), (5.723904448150409, 80.2444808815356, -168.43488299048647), (2.673416, 1.0, 1.25), "PWM_Quarry_2x2x2_A175", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4745.071, 2767.5618, 1938.2351), (-82.827479227917, -126.42149739696599, -139.15800706849845), (1.375, 1.0, 1.740382), "PWM_Quarry_2x2x2_A176_45", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1638.5491, 1907.8319, 2482.2676), (-0.025879211903765374, 66.19396009159047, -40.787537006697946), (3.3125, 1.0, 2.5625), "PWM_Quarry_2x2x2_A177", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4739.298, 2975.538, 1613.2561), (83.13817925356167, -33.28674481183771, -117.80249427592922), (1.5, 1.0, 1.740382), "PWM_Quarry_2x2x2_A178", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5176.0547, 1483.3228, 1961.039), (-6.104064976323554, 103.69224789498583, -0.7555543329155562), (1.887893, 1.0, 1.53125), "PWM_Quarry_2x2x2_A179", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1597.3303, 1770.235, 2291.7021), (0.0, 60.000011912675895, -0.0), (1.40625, 1.09375, 1.0), "PWM_Quarry_2x2x2_A18_75", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5206.9453, 1240.3385, 2339.2263), (-4.899963261618664, 94.16002550613506, -5.6309818118688995), (1.887893, 1.0, 1.0), "PWM_Quarry_2x2x2_A180", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4993.3896, 1798.1104, 2203.3184), (-0.4812316715238288, 105.10498649269351, 0.19274598973798393), (2.5625, 0.716357, 1.34375), "PWM_Quarry_2x2x2_A181", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4593.3896, 3398.1104, 2143.3184), (4.44111111393154, -79.8646523861493, 1.0715655233752768), (2.5625, 0.716357, 2.09375), "PWM_Quarry_2x2x2_A182", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4745.071, 2837.5618, 2298.235), (-82.827479227917, -126.42149739696599, -139.15800706849845), (1.9375, 1.0, 1.740382), "PWM_Quarry_2x2x2_A183", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2153.8196, 4124.403, 1873.4642), (-0.44030760466335467, -129.89503560861476, 0.27337787657079976), (2.5625, 0.716357, 2.09375), "PWM_Quarry_2x2x2_A184", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4433.3896, 3668.1104, 1373.3185), (-0.48123172643893175, 100.10500013602523, 0.19274600118090177), (2.5625, 0.716357, 2.09375), "PWM_Quarry_2x2x2_A185", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4393.3896, 3948.1104, 1743.3184), (4.441111306603096, -79.86465237431594, 1.0715661114406267), (2.5625, 0.716357, 2.09375), "PWM_Quarry_2x2x2_A186", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2153.0273, 4130.9688, 2263.1707), (-0.4403075800922032, 55.10481054366348, 0.27337466484729483), (2.5625, 0.716357, 2.09375), "PWM_Quarry_2x2x2_A187", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1764.5258, 2993.3198, 2316.4792), (5.723904448150409, 80.2444808815356, -168.43488299048647), (2.673416, 1.0, 1.25), "PWM_Quarry_2x2x2_A188", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3985.8713, 5156.7573, 1661.9519), (-85.00675070158631, -82.18477811726292, -178.174788491376), (1.375, 1.0, 2.34375), "PWM_Quarry_2x2x2_A189", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3777.4458, 5790.4727, 1464.5834), (-0.49890150127573746, 105.48125836063046, 4.740424239510328), (2.5625, 0.716357, 2.09375), "PWM_Quarry_2x2x2_A190", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3743.833, 5861.2207, 1934.9713), (4.44880876835011, -74.80203275469664, -3.4896847534251316), (2.5625, 0.716357, 2.09375), "PWM_Quarry_2x2x2_A191", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3935.7224, 5314.2036, 2093.641), (-85.00675070158631, -82.18477811726292, -178.174788491376), (1.9375, 1.0, 1.740382), "PWM_Quarry_2x2x2_A192", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3956.5247, 5250.0947, 1244.3336), (4.44880876835011, -74.80203275469664, -3.4896847534251316), (2.5625, 0.716357, 2.21875), "PWM_Quarry_2x2x2_A193", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2532.579, 5507.667, 1873.3185), (-0.4812011889299311, -114.894832728951, 0.1927463164240897), (2.5625, 0.716357, 1.34375), "PWM_Quarry_2x2x2_A194", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2552.3257, 5541.1694, 1208.4852), (-3.660675996690917, -120.47717555613887, -10.489014847825363), (1.887893, 1.0, 1.8125), "PWM_Quarry_2x2x2_A195", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2468.364, 5508.132, 1535.0835), (1.795629566872552, 69.35906652975761, -169.04221749698291), (2.673416, 1.0, 1.0), "PWM_Quarry_2x2x2_A196", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2492.579, 5347.667, 2323.3184), (-0.48120120165543423, -114.89483272718421, 0.19274599560595804), (2.5625, 0.716357, 1.78125), "PWM_Quarry_2x2x2_A197", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2715.94, 6038.403, 1074.3689), (-0.8086242582861196, 58.69152454520076, 5.055374047676932), (1.887893, 1.0, 1.8125), "PWM_Quarry_2x2x2_A198", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2585.6416, 5782.7817, 1760.9463), (1.795629864995018, 69.35900497852309, 175.95779324611186), (2.673416, 1.0, 1.875), "PWM_Quarry_2x2x2_A199", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1923.9565, 3485.3757, 2330.0), (18.67445214243681, -129.22239264306464, 22.719086778758804), (1.0, 1.0, 1.4375), "PWM_Quarry_2x2x2_A2", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2606.524, 5792.223, 2139.8145), (-1.4366454745415427, -125.62887269877683, -175.81690517970952), (2.673416, 1.0, 2.125), "PWM_Quarry_2x2x2_A200", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3055.2136, 6176.6895, 2089.601), (0.9157060254295566, -0.9751890465334127, -177.96290470411088), (3.53125, 1.0, 1.59375), "PWM_Quarry_2x2x2_A201", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3482.9038, 5939.1543, 2505.8054), (23.681641304439616, 168.53701741811844, -172.10639091284116), (2.6875, 1.0, 1.875), "PWM_Quarry_2x2x2_A202", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3665.7224, 5994.2036, 2093.641), (-6.377624035935512, -34.110688429849176, 173.15686568439594), (1.9375, 1.0, 1.740382), "PWM_Quarry_2x2x2_A203", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3727.4458, 5790.4727, 2304.5835), (-4.4444577498612645, 104.85277429281504, 19.228680217405827), (2.5625, 0.716357, 2.03125), "PWM_Quarry_2x2x2_A204", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (6193.3896, 1228.1104, 1653.3185), (-0.481231702827704, 95.10498597999683, 0.19274602278694822), (2.5625, 0.716357, 1.53125), "PWM_Quarry_2x2x2_A205", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5943.3896, 508.11035, 1523.3185), (-0.48117061623877055, 35.10530151351787, 5.1929142380883695), (2.5625, 0.716357, 2.0625), "PWM_Quarry_2x2x2_A206", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5351.948, 1328.8733, 1882.6643), (-8.995237638594192, 102.19576287799231, -10.706052632313591), (2.5625, 1.1875, 1.34375), "PWM_Quarry_2x2x2_A207", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (6039.9756, 1275.4246, 1733.7782), (9.65467407412288, 86.5279744780679, 71.70121221176142), (2.5625, 0.90625, 1.34375), "PWM_Quarry_2x2x2_A208", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4245.416, 4215.6094, 1757.8478), (3.309947158210784, -64.81431408235191, 3.1503965783761556), (2.5625, 0.716357, 2.21875), "PWM_Quarry_2x2x2_A209", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4048.2388, 4584.97, 2055.3298), (-4.440490333789936, 100.13643664516891, -1.0716856306999936), (2.5625, 0.716357, 1.90625), "PWM_Quarry_2x2x2_A210", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4446.031, 3859.3523, 2191.544), (-4.186950798262046, 110.16170277584419, -1.8276974245351962), (2.5625, 0.716357, 1.90625), "PWM_Quarry_2x2x2_A211", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4153.0483, 4283.2676, 2229.3662), (3.5714315766663605, -54.81597345122282, -177.15021268325162), (2.5625, 0.716357, 1.90625), "PWM_Quarry_2x2x2_A212", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2345.1545, 4733.6895, 1975.8564), (-0.4811706909092074, -99.89486348113206, 0.19274605248434232), (2.5625, 0.716357, 1.78125), "PWM_Quarry_2x2x2_A213", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2307.61, 4733.6895, 1507.6687), (-0.48120118876845114, -99.89486365819033, 0.19274598474596866), (2.5625, 0.716357, 2.375), "PWM_Quarry_2x2x2_A214", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2345.1543, 4733.6895, 2357.0132), (-4.4440309872500166, 99.92489849375207, 179.3318329862863), (2.5625, 0.716357, 2.34375), "PWM_Quarry_2x2x2_A215", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3090.2556, 4793.542, 3012.8772), (4.485894350579154, 95.30471459352707, 94.69391501073738), (2.5625, 0.716357, 2.34375), "PWM_Quarry_2x2x2_A216", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3538.4014, 4793.542, 3012.8772), (4.485899347359067, -89.69530359260168, 94.69393328567935), (2.5625, 0.716357, 2.34375), "PWM_Quarry_2x2x2_A217", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (956.948, 153.26923, 1213.5267), (-3.660674737357025, -130.47717046633693, -10.488952584470155), (1.887893, 1.0, 1.5625), "PWM_Quarry_2x2x2_A218", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (833.35565, 172.90149, 1709.0405), (-86.2121163444168, -38.00518321090095, -58.14703427542192), (2.4375, 1.0, 2.6875), "PWM_Quarry_2x2x2_A219", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2823.0703, 189.0931, 2713.8306), (1.9728996915607224, -176.54069382177138, 150.40600633560973), (3.3125, 1.0, 3.03125), "PWM_Quarry_2x2x2_A220", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3339.968, 220.34254, 2695.9905), (1.9728996915607224, -176.54069382177138, 150.40600633560973), (3.3125, 1.0, 3.03125), "PWM_Quarry_2x2x2_A221", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5457.519, 705.40186, 1971.3849), (-0.4812316715238288, 105.10498649269351, 0.19274598973798393), (2.5625, 0.716357, 1.625), "PWM_Quarry_2x2x2_A222", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1749.9332, 2126.631, 1908.2981), (-3.660674825673543, -90.47673931532047, -10.490751224565123), (2.65625, 1.0, 1.1875), "PWM_Quarry_2x2x2_A223", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1665.8226, 2028.1841, 2067.3413), (-5.176848958764606, 99.58078853085094, -167.14379722857367), (2.65625, 1.0, 1.1875), "PWM_Quarry_2x2x2_A224", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3876.5857, 5243.3403, 1159.1443), (3.234438157165069, -60.7987306827539, -2.8916016497805237), (1.375, 1.0, 2.34375), "PWM_Quarry_2x2x2_A225", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2526.0986, 5243.3403, 1299.1946), (3.2344385250813596, -92.72155212652024, -2.891601835617347), (1.375, 1.0, 2.34375), "PWM_Quarry_2x2x2_A226", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1797.2887, 3502.6658, 2124.7297), (-12.156004399029408, 71.84944642904017, -11.778287851744892), (1.0, 1.0, 1.4375), "PWM_Quarry_2x2x2_A3", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1752.4137, 2299.3389, 2460.6704), (-54.999843748650704, 0.0, -0.0), (1.0, 1.65625, 1.0), "PWM_Quarry_2x2x2_A4_123", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4780.3037, 1812.7925, 2554.6067), (1.3660377461677657e-05, 10.001449094049644, -9.155273682155704e-05), (1.75, 2.3125, 1.375), "PWM_Quarry_2x2x2_A5_134", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3150.0, 6090.0, 2300.0), (6.734896440003557e-06, -5.000000110790674, -25.00000347584325), (2.4375, 1.0, 2.28125), "PWM_Quarry_2x2x2_A6_173", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5620.0, 360.0, 1070.0), (0.0, -20.000060948281234, 0.0), (1.0, 1.0, 1.4375), "PWM_Quarry_2x2x2_A7_190", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5613.275, 323.88275, 1378.9775), (4.0749500906276733e-07, 59.99995685158093, 15.001841251177828), (1.0, 1.0, 1.75), "PWM_Quarry_2x2x2_A8", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (6073.8574, 767.4647, 1693.5159), (38.337520064883634, -22.950866345364542, 9.55738955345508), (0.6875, 2.5, 1.75), "PWM_Quarry_2x2x2_A9_200", _folder)
if a: placed += 1
else: skipped += 1

# Batch 89: StaticMesh'PWM_Quarry_2x2x5_A' (6 instances)
_mesh_path = "/Game/Unshippable/Whitebox/Rocks/Meshes/PWM_Quarry_2x2x5_A"
_materials = ['/Game/Environments/ProcTexturing/ProcMaterial_Quarry_Atlas_2']
_folder = "Reconstruction/BD_BB_OrcTown_Gate/Meshes"
a = spawn_static_mesh(_mesh_path, _materials, (1017.57367, 876.8632, 2000.0), (0.0, -35.00006033507422, 0.0), (1.53125, 1.96875, 2.0625), "PWM_Quarry_2x2x5_A_33", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5660.0, 120.0, 980.0), (0.0, 0.0, -0.0), (2.1875, 2.1875, 2.1875), "PWM_Quarry_2x2x5_A2_187", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4870.0, 1760.0, 1180.0), (0.0, 100.000052253256, -0.0), (1.46875, 1.46875, 1.90625), "PWM_Quarry_2x2x5_A3_47", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5059.0728, 1730.794, 1425.0973), (3.6801311414589617, -170.7066605680845, -7.889282490901291), (1.890957, 1.890957, 1.890957), "PWM_Quarry_2x2x5_A7_342", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1836.3827, 2446.0034, 1425.0973), (3.680130950353164, -45.70650454166313, -7.889282434540608), (1.890957, 1.890957, 1.890957), "PWM_Quarry_2x2x5_A8", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1886.3827, 3796.0034, 1425.0973), (-3.313720946104292, -70.6836534269606, -0.7373353269973834), (1.890957, 1.890957, 1.890957), "PWM_Quarry_2x2x5_A9", _folder)
if a: placed += 1
else: skipped += 1

# Batch 90: StaticMesh'PWM_Quarry_2x2x5_B' (17 instances)
_mesh_path = "/Game/Unshippable/Whitebox/Rocks/Meshes/PWM_Quarry_2x2x5_B"
_materials = ['/Game/Environments/ProcTexturing/ProcMaterial_Quarry_Atlas_2']
_folder = "Reconstruction/BD_BB_OrcTown_Gate/Meshes"
a = spawn_static_mesh(_mesh_path, _materials, (5080.0, 1890.0, 2120.0), (0.0, -35.00006033507422, 0.0), (2.5625, 2.5625, 2.5625), "PWM_Quarry_2x2x5_B_20", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (6250.0, 1610.0, 1270.0), (0.0, -150.00007181093972, 0.0), (1.65625, 1.6875, 1.875), "PWM_Quarry_2x2x5_B10", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5560.0, 390.0, 1690.0), (6.82111148161806, -60.328709436469644, -1.850738642673132), (1.0, 1.0, 1.25), "PWM_Quarry_2x2x5_B11_194", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2234.001, 4881.8213, 1640.0), (0.0, -110.00001199018955, 0.0), (2.65625, 2.65625, 2.65625), "PWM_Quarry_2x2x5_B12", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5632.87, 105.39424, 1866.969), (2.4092258962523094, -45.60119154863333, -2.163360637944232), (1.8125, 1.8125, 2.0625), "PWM_Quarry_2x2x5_B13", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5632.87, 341.92535, 2230.8447), (2.4092256404532852, -45.6011915405412, -2.1633606544828203), (1.8125, 1.8125, 2.0625), "PWM_Quarry_2x2x5_B14", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1723.9497, 2700.755, 1600.5314), (0.0, 60.00010751950892, -0.0), (2.03125, 2.03125, 2.03125), "PWM_Quarry_2x2x5_B15_16", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1833.0107, 2284.4358, 1359.9419), (0.0, -79.99999917458362, 0.0), (1.625, 1.375, 1.84375), "PWM_Quarry_2x2x5_B16_55", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1293.5575, 1359.9922, 1385.138), (0.0, -30.000063894566395, 0.0), (1.0, 1.5625, 2.03125), "PWM_Quarry_2x2x5_B17_66", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4810.0, 3030.0, 2120.0), (0.0, 154.99986873250592, -0.0), (2.5625, 2.5625, 2.5625), "PWM_Quarry_2x2x5_B2", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5260.0, 1710.0, 1330.0), (0.0, 0.0, -0.0), (2.1875, 2.1875, 2.1875), "PWM_Quarry_2x2x5_B3_59", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3995.5405, 5515.554, 1923.6472), (-3.7300413397247247, 160.32987772372482, 2.6031693841906582), (2.5625, 2.5625, 2.5625), "PWM_Quarry_2x2x5_B4", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4075.5405, 5055.554, 2273.6472), (-3.7300412111602697, 160.32987774029198, 2.603168778792832), (2.5625, 2.5625, 2.5625), "PWM_Quarry_2x2x5_B5", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2330.0, 5150.0, 1640.0), (0.0, 50.0000431017326, -0.0), (2.65625, 2.65625, 2.65625), "PWM_Quarry_2x2x5_B6_155", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2662.982, 6196.066, 1640.0), (-1.4879475579516376e-07, -105.00002701094712, 10.000711074245595), (2.65625, 2.65625, 2.65625), "PWM_Quarry_2x2x5_B7", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3724.8625, 6288.7266, 1246.9685), (-0.4064330685566457, 110.3982831794972, 4.529415465943827), (2.5625, 2.5625, 3.5), "PWM_Quarry_2x2x5_B8", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (6250.0, 1370.0, 1270.0), (0.0, -40.00005923828246, 0.0), (1.65625, 1.6875, 1.4375), "PWM_Quarry_2x2x5_B9_183", _folder)
if a: placed += 1
else: skipped += 1

# Batch 91: StaticMesh'PWM_Quarry_3x3x2' (3 instances)
_mesh_path = "/Game/Unshippable/Whitebox/Rocks/Meshes/PWM_Quarry_3x3x2"
_materials = ['/Game/Environments/ProcTexturing/ProcMaterial_Quarry_Atlas_A']
_folder = "Reconstruction/BD_BB_OrcTown_Gate/Meshes"
a = spawn_static_mesh(_mesh_path, _materials, (4950.0, 2210.0, 2130.0), (-7.644287029533639, -59.56761997691779, -6.466339365354916), (1.84375, 1.84375, 1.84375), "PWM_Quarry_3x3x2_23", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4860.0, 2600.0, 2130.0), (-7.644286312774176, -74.5676243759375, -6.466339067246268), (1.84375, 1.84375, 1.84375), "PWM_Quarry_3x3x3", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2470.0, 5610.0, 2130.0), (-7.6442873582451485, 75.43253727075626, -6.466340028483665), (1.84375, 1.84375, 1.84375), "PWM_Quarry_3x3x4", _folder)
if a: placed += 1
else: skipped += 1

# Batch 92: StaticMesh'PWM_Quarry_8x8x8_A' (20 instances)
_mesh_path = "/Game/Unshippable/Whitebox/Rocks/Meshes/PWM_Quarry_8x8x8_A"
_materials = ['/Game/Environments/ProcTexturing/ProcMaterial_Quarry_Atlas_2']
_folder = "Reconstruction/BD_BB_OrcTown_Gate/Meshes"
a = spawn_static_mesh(_mesh_path, _materials, (4867.1006, 2227.6497, 1727.4905), (-1.0822449509194059, 113.49645692191666, -6.00952192366065), (0.66454, 0.242456, 0.257641), "PWM_Quarry_8x8x8_A53_399", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4740.855, 2099.5842, 1113.1195), (-3.510040099169793, 104.1412817374393, -13.040159343911442), (0.460004, 0.19389, 0.32009), "PWM_Quarry_8x8x8_A54_414", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1729.7275, 1949.4202, 1727.4905), (-1.0822144079425433, -101.50360149494728, -6.009521304180205), (0.65625, 0.242456, 0.257641), "PWM_Quarry_8x8x8_A55", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1905.1583, 1808.9491, 1113.1195), (-3.510040653385702, -100.85876789638584, -13.041412022477628), (0.460004, 0.19389, 0.32009), "PWM_Quarry_8x8x8_A56", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1442.1385, 1805.3341, 2132.0251), (-1.0822143561619377, -106.50360088526563, -6.0095209149756315), (0.66454, 0.242456, 0.34375), "PWM_Quarry_8x8x8_A57", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1766.5634, 3075.3638, 2151.5352), (-1.0820924133092675, -106.50377953523217, 13.992015340471257), (0.8125, 0.242456, 0.34375), "PWM_Quarry_8x8x8_A58", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1571.523, 2122.266, 2101.8157), (-1.0822143561619377, -106.50360088526563, -6.0095209149756315), (0.66454, 0.242456, 0.257641), "PWM_Quarry_8x8x8_A59", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1704.1359, 2508.299, 2328.1208), (4.553761727075157, -105.91569117955609, 13.196662990479698), (0.66454, 0.242456, 0.53125), "PWM_Quarry_8x8x8_A60", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (904.2526, 643.44086, 2052.0244), (-0.3733519665938489, -116.4780387349552, 4.117650480767697), (0.66454, 0.242456, 0.59375), "PWM_Quarry_8x8x8_A61", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5300.8555, 1019.5842, 1923.1195), (-2.1451109172708165, 102.7005880760602, 2.7136624125942053), (0.460004, 0.19389, 0.32009), "PWM_Quarry_8x8x8_A62", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (824.2526, 243.44086, 2192.0244), (0.24350290754564746, 93.53321826410159, -5.86331140337622), (0.66454, 0.242456, 0.59375), "PWM_Quarry_8x8x8_A63", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5140.855, 1339.5842, 2073.1196), (-4.717559537064956, 93.79209924603613, -8.175537348791776), (0.460004, 0.19389, 0.32009), "PWM_Quarry_8x8x8_A64", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1992.1385, 4055.334, 1632.0251), (3.375383869092149, -116.3238276615279, 2.946069994416496), (0.66454, 0.242456, 0.34375), "PWM_Quarry_8x8x8_A65", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1900.3652, 3746.8538, 2106.6433), (1.760433264683815, -106.44671854597439, 3.5790916132181203), (0.66454, 0.242456, 0.53125), "PWM_Quarry_8x8x8_A66", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1553.4604, 2009.4948, 1727.4905), (-1.0822140747578606, -116.50359179950547, -6.009520724541096), (0.66454, 0.242456, 0.257641), "PWM_Quarry_8x8x8_A67", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2516.139, 5538.9014, 1727.4905), (-1.082213963935309, -111.50356273823385, -6.0095213393392), (0.66454, 0.242456, 0.257641), "PWM_Quarry_8x8x8_A68", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2640.2249, 5708.7656, 2601.2266), (-1.0821534943115543, -111.50333449939811, -1.0095216521480024), (0.875, 0.242456, 0.625), "PWM_Quarry_8x8x8_A69", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1074.2527, 243.44086, 2542.0244), (-5.4750668543070935, 176.54468474880125, -65.68438679220202), (0.66454, 0.242456, 0.59375), "PWM_Quarry_8x8x8_A70", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1905.1582, 2110.6685, 1113.1195), (-3.5100405598807067, -80.85870289884947, -13.04144145453382), (0.460004, 0.19389, 0.32009), "PWM_Quarry_8x8x8_A71", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1580.6625, 1608.3328, 1727.4905), (-1.082184075693778, -141.50358429638533, -6.009521489950206), (0.75, 0.242456, 0.257641), "PWM_Quarry_8x8x8_A72", _folder)
if a: placed += 1
else: skipped += 1

# Batch 93: StaticMesh'PWM_Quarry_RockDebris_A' (20 instances)
_mesh_path = "/Game/Unshippable/Whitebox/Rocks/Meshes/PWM_Quarry_RockDebris_A"
_materials = ['/Game/Environments/ProcTexturing/ProcMaterial_Quarry_Atlas_5']
_folder = "Reconstruction/BD_BB_OrcTown_Gate/Meshes"
a = spawn_static_mesh(_mesh_path, _materials, (4089.249, 1936.4277, 1098.4479), (0.0, 0.0, -0.0), (1.0, 1.0, 1.0), "PWM_Quarry_RockDebris_A_62", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3330.0, 3236.5432, 1189.0447), (0.0, 0.0, -0.0), (1.0, 1.0, 1.0), "PWM_Quarry_RockDebris_A10_18", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3330.0007, 2760.0007, 1189.5778), (0.0, 0.0, -0.0), (1.0, 1.0, 1.0), "PWM_Quarry_RockDebris_A11", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3330.0007, 3190.0007, 1176.103), (0.0, -40.00005923828246, 0.0), (1.0, 1.0, 1.0), "PWM_Quarry_RockDebris_A12", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3274.5427, 3815.3843, 1186.4954), (0.0, -40.00005923828246, 0.0), (1.0, 1.0, 1.0), "PWM_Quarry_RockDebris_A13", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3040.0002, 3680.0002, 1183.7709), (0.0, -40.00005923828246, 0.0), (1.0, 1.0, 1.0), "PWM_Quarry_RockDebris_A14", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3039.5427, 3825.3843, 1190.9396), (-0.04797353557797187, 70.01044677641791, 2.6861221168819203), (1.0, 1.0, 1.0), "PWM_Quarry_RockDebris_A15", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3284.999, 3985.0, 1187.0779), (0.0, 70.00000891014233, -0.0), (1.0, 1.0, 1.0), "PWM_Quarry_RockDebris_A16", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3199.543, 2890.459, 1188.4758), (0.0, -135.0000236526688, 0.0), (1.0, 1.0, 1.0), "PWM_Quarry_RockDebris_A17", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2596.3027, 1460.7618, 1094.6477), (0.0, -29.99987961849943, 0.0), (1.0, 1.0, 1.0), "PWM_Quarry_RockDebris_A18", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2779.2866, 1489.0137, 1094.6477), (0.0, -29.99987961849943, 0.0), (1.0, 1.0, 1.0), "PWM_Quarry_RockDebris_A19", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4089.249, 2104.7417, 1098.4479), (0.0, 0.0, -0.0), (1.0, 1.0, 1.0), "PWM_Quarry_RockDebris_A2", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4989.9907, 1399.0399, 1098.448), (0.0, -139.99983844365445, 0.0), (1.0, 1.0, 1.0), "PWM_Quarry_RockDebris_A20", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4780.0127, 1358.9751, 1098.448), (0.0, 0.0, -0.0), (1.0, 1.0, 1.0), "PWM_Quarry_RockDebris_A3", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3866.7712, 1491.4777, 1098.6976), (0.0, 0.0, -0.0), (1.0, 1.0, 1.0), "PWM_Quarry_RockDebris_A4_90", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4012.7314, 1347.9386, 1099.8094), (0.0, 40.00004110866871, -0.0), (1.0, 1.0, 1.0), "PWM_Quarry_RockDebris_A5", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4012.7314, 1710.0614, 1102.6079), (0.0, 40.00004110866871, -0.0), (1.0, 1.0, 1.0), "PWM_Quarry_RockDebris_A6", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4124.7954, 1138.1643, 1094.6478), (0.0, 40.00004110866871, -0.0), (1.0, 1.0, 1.0), "PWM_Quarry_RockDebris_A7", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3923.2246, 1138.385, 1094.6478), (0.0, -29.99987961849943, 0.0), (1.0, 1.0, 1.0), "PWM_Quarry_RockDebris_A8", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3754.8647, 1369.4855, 1094.6478), (0.0, -29.99987961849943, 0.0), (1.0, 1.0, 1.0), "PWM_Quarry_RockDebris_A9", _folder)
if a: placed += 1
else: skipped += 1

# Batch 94: StaticMesh'PWM_Quarry_RockDebris_C' (22 instances)
_mesh_path = "/Game/Unshippable/Whitebox/Rocks/Meshes/PWM_Quarry_RockDebris_C"
_materials = ['/Game/Unshippable/Cinematics/Cine002/Environments/Materials/ProcMaterial_Quarry_RockDebris_A']
_folder = "Reconstruction/BD_BB_OrcTown_Gate/Meshes"
a = spawn_static_mesh(_mesh_path, _materials, (1195.3708, 837.3698, 1101.9012), (0.0, -70.07870811992126, 0.0), (1.0, 1.0, 1.0), "PWM_Quarry_RockDebris_C10", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1263.1814, 1000.12854, 1101.9012), (0.0, -70.07870811992126, 0.0), (1.0, 1.0, 1.0), "PWM_Quarry_RockDebris_C11", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4564.589, 2908.7507, 1301.5522), (0.0, 0.0, -0.0), (1.0, 1.0, 1.0), "PWM_Quarry_RockDebris_C18_27", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4588.5728, 3119.4468, 1301.5522), (0.0, -50.75277565791118, 0.0), (1.0, 1.0, 1.0), "PWM_Quarry_RockDebris_C19", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4552.4165, 3327.6047, 1301.5522), (0.0, -50.75277565791118, 0.0), (1.0, 1.0, 1.0), "PWM_Quarry_RockDebris_C20", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4448.2056, 3532.861, 1301.5522), (0.0, -50.75277565791118, 0.0), (1.0, 1.0, 1.0), "PWM_Quarry_RockDebris_C21", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3852.461, 4632.603, 1206.3344), (0.0, 0.0, -0.0), (1.0, 1.0, 1.0), "PWM_Quarry_RockDebris_C22_33", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3917.714, 4814.5117, 1206.3344), (0.0, -24.4559637879606, 0.0), (1.0, 1.0, 1.0), "PWM_Quarry_RockDebris_C23", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3877.3315, 4896.297, 1208.6078), (0.0, -24.4559637879606, 0.0), (1.0, 1.0, 1.0), "PWM_Quarry_RockDebris_C24", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2556.6714, 4673.1055, 1206.3344), (0.0, 0.0, -0.0), (1.0, 1.0, 1.0), "PWM_Quarry_RockDebris_C25", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3598.975, 6214.6064, 811.84827), (0.0, 0.0, -0.0), (1.0, 1.0, 1.0), "PWM_Quarry_RockDebris_C28", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2822.851, 6214.6064, 805.17737), (0.0, 0.0, -0.0), (1.0, 1.0, 1.0), "PWM_Quarry_RockDebris_C29", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2822.851, 5969.666, 805.17737), (0.0, 0.0, 7.413614575166894), (1.0, 1.0, 1.0), "PWM_Quarry_RockDebris_C30", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2516.4612, 4936.989, 1206.3344), (0.0, 0.0, -0.0), (1.0, 1.0, 1.0), "PWM_Quarry_RockDebris_C33_50", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2380.9353, 4666.0845, 1206.3344), (0.0, 0.0, -0.0), (1.0, 1.0, 1.0), "PWM_Quarry_RockDebris_C34", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2455.3328, 4508.646, 1206.3344), (0.0, 0.0, -0.0), (1.0, 1.0, 1.0), "PWM_Quarry_RockDebris_C35", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4006.3828, 1426.359, 1099.9661), (0.0, 0.0, -0.0), (1.0, 1.0, 1.0), "PWM_Quarry_RockDebris_C36_86", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3909.0537, 1541.9955, 1099.9661), (0.0, -99.99996778044596, 0.0), (1.0, 0.78125, 1.0), "PWM_Quarry_RockDebris_C37", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5080.856, 1637.4911, 1099.2765), (0.0, 102.297688208232, -0.0), (1.0, 1.0, 1.0), "PWM_Quarry_RockDebris_C4", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1128.6279, 645.5812, 1103.858), (0.0, 0.0, -0.0), (1.0, 1.0, 1.0), "PWM_Quarry_RockDebris_C7_14", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1074.8948, 411.30746, 1103.858), (0.0, 0.0, -0.0), (1.0, 1.0, 1.0), "PWM_Quarry_RockDebris_C8", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1074.8948, 227.92813, 1101.9462), (0.0, -26.43628073570686, 0.0), (1.0, 1.0, 1.0), "PWM_Quarry_RockDebris_C9", _folder)
if a: placed += 1
else: skipped += 1

# ======================================================================
# PHASE 2: ConstructionCatalog  (construction blocks)
# ======================================================================
unreal.log(f"[{BUBBLE_NAME}] Phase 2: Placing construction blocks...")

# Construction blocks use DecoVolume transforms (matched by Name)
_folder = "Reconstruction/BD_BB_OrcTown_Gate/Construction"

# Construction: AB_Orc_Scaffolding_Balcony_C_5
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Wood
#   Volume: EMorSimpleShape::OrientedBox, BoxExtent: (182.4, 77.8, 168.8)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (2545.0, 1310.1288, 1252.8894), (0.0, 0.0, -0.0), (3.6488, 1.5552, 3.3760), "AB_Orc_Scaffolding_Balcony_C_5", _folder)
if a: placed += 1
else: skipped += 1

# Construction: AB_Orc_Scaffolding_Balcony_C2
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Wood
#   Volume: EMorSimpleShape::OrientedBox, BoxExtent: (182.4, 77.8, 168.8)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (2195.0, 1310.1288, 1252.8894), (0.0, 0.0, -0.0), (3.6488, 1.5552, 3.3760), "AB_Orc_Scaffolding_Balcony_C2", _folder)
if a: placed += 1
else: skipped += 1

# Construction: AB_Orc_Scaffolding_Balcony_C3
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Wood
#   Volume: EMorSimpleShape::OrientedBox, BoxExtent: (182.4, 77.8, 168.8)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (3880.0, 1310.1288, 1252.8894), (0.0, 0.0, -0.0), (3.6488, 1.5552, 3.3760), "AB_Orc_Scaffolding_Balcony_C3", _folder)
if a: placed += 1
else: skipped += 1

# Construction: AB_Orc_Scaffolding_Balcony_C4
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Wood
#   Volume: EMorSimpleShape::OrientedBox, BoxExtent: (182.4, 77.8, 168.8)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (4230.0, 1310.1288, 1272.8894), (0.0, 0.0, -0.0), (3.6488, 1.5552, 3.3760), "AB_Orc_Scaffolding_Balcony_C4", _folder)
if a: placed += 1
else: skipped += 1

# Construction: AB_Orc_Scaffolding_Foundation_3x1m24_4
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Stone
#   Volume: EMorSimpleShape::OrientedBox, BoxExtent: (172.7, 85.2, 169.2)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (2800.2222, 1486.1329, 1103.346), (0.0, 0.0, -0.0), (3.4533, 1.7049, 3.3833), "AB_Orc_Scaffolding_Foundation_3x1m24_4", _folder)
if a: placed += 1
else: skipped += 1

# Construction: AB_Orc_Scaffolding_Foundation_3x1m25_5
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Stone
#   Volume: EMorSimpleShape::OrientedBox, BoxExtent: (172.7, 85.2, 169.2)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (2799.7805, 1593.8672, 1103.346), (0.0, 0.0, -0.0), (3.4533, 1.7049, 3.3833), "AB_Orc_Scaffolding_Foundation_3x1m25_5", _folder)
if a: placed += 1
else: skipped += 1

# Construction: AB_Orc_Scaffolding_Foundation_3x1m26
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Stone
#   Volume: EMorSimpleShape::OrientedBox, BoxExtent: (172.7, 85.2, 169.2)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (3599.7793, 1593.8661, 1103.346), (0.0, 0.0, -0.0), (3.4533, 1.7049, 3.3833), "AB_Orc_Scaffolding_Foundation_3x1m26", _folder)
if a: placed += 1
else: skipped += 1

# Construction: AB_Orc_Scaffolding_Foundation_3x1m27
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Stone
#   Volume: EMorSimpleShape::OrientedBox, BoxExtent: (172.7, 85.2, 169.2)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (3600.2207, 1486.1329, 1103.346), (0.0, 0.0, -0.0), (3.4533, 1.7049, 3.3833), "AB_Orc_Scaffolding_Foundation_3x1m27", _folder)
if a: placed += 1
else: skipped += 1

# Construction: AB_Orc_Scaffolding_Foundation_3x3m16
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Stone
#   Volume: EMorSimpleShape::OrientedBox, BoxExtent: (204.7, 213.0, 169.2)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (4195.074, 1516.8728, 1098.346), (0.0, 0.0, -0.0), (4.0937, 4.2590, 3.3833), "AB_Orc_Scaffolding_Foundation_3x3m16", _folder)
if a: placed += 1
else: skipped += 1

# Construction: AB_Orc_Scaffolding_Foundation_3x3m17
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Stone
#   Volume: EMorSimpleShape::OrientedBox, BoxExtent: (204.7, 213.0, 169.2)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (3904.9258, 1563.1266, 1098.346), (0.0, 0.0, -0.0), (4.0937, 4.2590, 3.3833), "AB_Orc_Scaffolding_Foundation_3x3m17", _folder)
if a: placed += 1
else: skipped += 1

# Construction: AB_Orc_Scaffolding_Platform_1x1_No_Legs_2
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Stone
#   Volume: EMorSimpleShape::OrientedBox, BoxExtent: (56.0, 61.0, 9.0)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (2547.4512, 1705.1238, 1392.7867), (0.0, 0.0, -0.0), (1.1196, 1.2206, 0.1790), "AB_Orc_Scaffolding_Platform_1x1_No_Legs_2", _folder)
if a: placed += 1
else: skipped += 1

# Construction: AB_Orc_Scaffolding_Platform_1x1_No_Legs2
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Stone
#   Volume: EMorSimpleShape::OrientedBox, BoxExtent: (56.0, 61.0, 9.0)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (2560.8289, 1789.5144, 1392.7867), (0.0, 0.0, -0.0), (1.1196, 1.2206, 0.1790), "AB_Orc_Scaffolding_Platform_1x1_No_Legs2", _folder)
if a: placed += 1
else: skipped += 1

# Construction: AB_Orc_Scaffolding_Platform_1x3x2m_2
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Stone
#   Volume: EMorSimpleShape::OrientedBox, BoxExtent: (85.3, 168.2, 123.6)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (2146.6006, 1585.2869, 1309.8368), (0.0, 0.0, -0.0), (1.7055, 3.3634, 2.4715), "AB_Orc_Scaffolding_Platform_1x3x2m_2", _folder)
if a: placed += 1
else: skipped += 1

# Construction: AB_Orc_Scaffolding_Platform_1x3x3m_7
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Stone
#   Volume: EMorSimpleShape::OrientedBox, BoxExtent: (80.3, 64.8, 172.5)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (2254.114, 1487.898, 1239.6206), (0.0, 0.0, -0.0), (1.6053, 1.2963, 3.4493), "AB_Orc_Scaffolding_Platform_1x3x3m_7", _folder)
if a: placed += 1
else: skipped += 1

# Construction: AB_Orc_Scaffolding_Platform_1x3x3m2
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Stone
#   Volume: EMorSimpleShape::OrientedBox, BoxExtent: (80.3, 64.8, 172.5)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (2245.8867, 1592.102, 1239.6206), (0.0, 0.0, -0.0), (1.6053, 1.2963, 3.4493), "AB_Orc_Scaffolding_Platform_1x3x3m2", _folder)
if a: placed += 1
else: skipped += 1

# Construction: AB_Orc_Scaffolding_Platform_1x3x3m3
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Stone
#   Volume: EMorSimpleShape::OrientedBox, BoxExtent: (80.3, 64.8, 172.5)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (2345.887, 1592.1016, 1239.6206), (0.0, 0.0, -0.0), (1.6053, 1.2963, 3.4493), "AB_Orc_Scaffolding_Platform_1x3x3m3", _folder)
if a: placed += 1
else: skipped += 1

# Construction: AB_Orc_Scaffolding_Platform_1x3x3m30
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Stone
#   Volume: EMorSimpleShape::OrientedBox, BoxExtent: (64.8, 80.3, 172.5)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (4147.898, 1835.8866, 1239.6206), (0.0, 0.0, -0.0), (1.2963, 1.6053, 3.4493), "AB_Orc_Scaffolding_Platform_1x3x3m30", _folder)
if a: placed += 1
else: skipped += 1

# Construction: AB_Orc_Scaffolding_Platform_1x3x3m31
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Stone
#   Volume: EMorSimpleShape::OrientedBox, BoxExtent: (64.8, 80.3, 172.5)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (4152.1016, 1744.1134, 1239.6206), (0.0, 0.0, -0.0), (1.2963, 1.6053, 3.4493), "AB_Orc_Scaffolding_Platform_1x3x3m31", _folder)
if a: placed += 1
else: skipped += 1

# Construction: AB_Orc_Scaffolding_Platform_1x3x3m4
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Stone
#   Volume: EMorSimpleShape::OrientedBox, BoxExtent: (80.3, 64.8, 172.5)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (2354.114, 1487.8982, 1239.6206), (0.0, 0.0, -0.0), (1.6053, 1.2963, 3.4493), "AB_Orc_Scaffolding_Platform_1x3x3m4", _folder)
if a: placed += 1
else: skipped += 1

# Construction: AB_Orc_Scaffolding_Platform_1x3x3m7
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Stone
#   Volume: EMorSimpleShape::OrientedBox, BoxExtent: (80.3, 64.8, 172.5)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (2154.114, 1797.898, 1239.6206), (0.0, 0.0, -0.0), (1.6053, 1.2963, 3.4493), "AB_Orc_Scaffolding_Platform_1x3x3m7", _folder)
if a: placed += 1
else: skipped += 1

# Construction: AB_Orc_Scaffolding_Platform_3x2x3m28_8
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Stone
#   Volume: EMorSimpleShape::OrientedBox, BoxExtent: (170.3, 132.8, 167.7)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (2802.8054, 1540.1294, 1305.1663), (0.0, 0.0, -0.0), (3.4054, 2.6552, 3.3536), "AB_Orc_Scaffolding_Platform_3x2x3m28_8", _folder)
if a: placed += 1
else: skipped += 1

# Construction: AB_Orc_Scaffolding_Platform_3x2x3m29_7
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Stone
#   Volume: EMorSimpleShape::OrientedBox, BoxExtent: (170.3, 132.8, 167.7)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (4197.194, 1539.8696, 1255.1664), (0.0, 0.0, -0.0), (3.4054, 2.6552, 3.3536), "AB_Orc_Scaffolding_Platform_3x2x3m29_7", _folder)
if a: placed += 1
else: skipped += 1

# Construction: AB_Orc_Scaffolding_Platform_3x2x3m30
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Stone
#   Volume: EMorSimpleShape::OrientedBox, BoxExtent: (170.3, 132.8, 167.7)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (2352.8054, 1740.1294, 1255.1663), (0.0, 0.0, -0.0), (3.4054, 2.6552, 3.3536), "AB_Orc_Scaffolding_Platform_3x2x3m30", _folder)
if a: placed += 1
else: skipped += 1

# Construction: AB_Orc_Scaffolding_Platform_3x2x3m31_12
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Stone
#   Volume: EMorSimpleShape::OrientedBox, BoxExtent: (170.3, 132.8, 167.7)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (2497.1934, 1539.8707, 1255.1663), (0.0, 0.0, -0.0), (3.4054, 2.6552, 3.3536), "AB_Orc_Scaffolding_Platform_3x2x3m31_12", _folder)
if a: placed += 1
else: skipped += 1

# Construction: AB_Orc_Scaffolding_Platform_3x2x3m32
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Stone
#   Volume: EMorSimpleShape::OrientedBox, BoxExtent: (170.3, 132.8, 167.7)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (3947.1943, 1789.87, 1255.1663), (0.0, 0.0, -0.0), (3.4054, 2.6552, 3.3536), "AB_Orc_Scaffolding_Platform_3x2x3m32", _folder)
if a: placed += 1
else: skipped += 1

# Construction: AB_Orc_Scaffolding_Platform_3x2x3m33
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Stone
#   Volume: EMorSimpleShape::OrientedBox, BoxExtent: (170.3, 132.8, 167.7)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (3897.1948, 1539.8711, 1255.1664), (0.0, 0.0, -0.0), (3.4054, 2.6552, 3.3536), "AB_Orc_Scaffolding_Platform_3x2x3m33", _folder)
if a: placed += 1
else: skipped += 1

# Construction: AB_Orc_Scaffolding_Platform_3x2x3m34
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Stone
#   Volume: EMorSimpleShape::OrientedBox, BoxExtent: (170.3, 132.8, 167.7)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (3597.1948, 1539.8716, 1305.1664), (0.0, 0.0, -0.0), (3.4054, 2.6552, 3.3536), "AB_Orc_Scaffolding_Platform_3x2x3m34", _folder)
if a: placed += 1
else: skipped += 1

# Construction: AB_Orc_Scaffolding_Platform_3x2x3m35
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Stone
#   Volume: EMorSimpleShape::OrientedBox, BoxExtent: (170.3, 132.8, 167.7)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (2797.1938, 1539.8711, 1605.1664), (0.0, 0.0, -0.0), (3.4054, 2.6552, 3.3536), "AB_Orc_Scaffolding_Platform_3x2x3m35", _folder)
if a: placed += 1
else: skipped += 1

# Construction: AB_Orc_Scaffolding_Platform_3x2x3m36
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Stone
#   Volume: EMorSimpleShape::OrientedBox, BoxExtent: (170.3, 132.8, 167.7)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (3602.8052, 1540.1287, 1605.1664), (0.0, 0.0, -0.0), (3.4054, 2.6552, 3.3536), "AB_Orc_Scaffolding_Platform_3x2x3m36", _folder)
if a: placed += 1
else: skipped += 1

# Construction: AB_Orc_Scaffolding_Stairs_3M6_2
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Stone
#   Volume: EMorSimpleShape::OrientedBox, BoxExtent: (253.8, 130.6, 181.7)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (2831.2715, 1796.4708, 1229.8889), (0.0, 0.0, -0.0), (5.0754, 2.6126, 3.6341), "AB_Orc_Scaffolding_Stairs_3M6_2", _folder)
if a: placed += 1
else: skipped += 1

# Construction: AB_Orc_Scaffolding_Stairs_3M8_4
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Stone
#   Volume: EMorSimpleShape::OrientedBox, BoxExtent: (253.8, 130.6, 181.7)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (3568.7285, 1733.5295, 1229.8889), (0.0, 0.0, -0.0), (5.0754, 2.6126, 3.6341), "AB_Orc_Scaffolding_Stairs_3M8_4", _folder)
if a: placed += 1
else: skipped += 1

# Construction: Orc_Palissade_Gate_A_L2_2
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Wood
#   Volume: EMorSimpleShape::OrientedBox, BoxExtent: (134.1, 97.3, 244.2)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (3344.308, 1468.7462, 1346.2346), (0.0, 0.0, -0.0), (2.6822, 1.9467, 4.8835), "Orc_Palissade_Gate_A_L2_2", _folder)
if a: placed += 1
else: skipped += 1

# Construction: Orc_Palissade_Gate_A_R2_2
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Wood
#   Volume: EMorSimpleShape::OrientedBox, BoxExtent: (134.2, 97.8, 244.2)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (3075.2197, 1476.9004, 1350.0529), (0.0, 0.0, -0.0), (2.6833, 1.9552, 4.8835), "Orc_Palissade_Gate_A_R2_2", _folder)
if a: placed += 1
else: skipped += 1

# Construction: Orc_Palissade_Gate_B_2
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Wood
#   Volume: EMorSimpleShape::OrientedBox, BoxExtent: (284.3, 40.5, 265.3)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (3174.3267, 1324.0046, 1417.7334), (0.0, 0.0, -0.0), (5.6870, 0.8106, 5.3064), "Orc_Palissade_Gate_B_2", _folder)
if a: placed += 1
else: skipped += 1

# Construction: Orc_Palissade_Gate_B2_2
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Wood
#   Volume: EMorSimpleShape::OrientedBox, BoxExtent: (284.3, 40.5, 265.3)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (3175.358, 1387.655, 1338.5078), (0.0, 0.0, -0.0), (5.6870, 0.8106, 5.3064), "Orc_Palissade_Gate_B2_2", _folder)
if a: placed += 1
else: skipped += 1

# Construction: Orc_Palissade_Post_A_5
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Wood
#   Volume: EMorSimpleShape::OrientedBox, BoxExtent: (83.1, 169.7, 332.0)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (5633.1357, 623.91296, 1295.749), (0.0, 0.0, -0.0), (1.6629, 3.3950, 6.6396), "Orc_Palissade_Post_A_5", _folder)
if a: placed += 1
else: skipped += 1

# Construction: Orc_Palissade_Post_A17
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Wood
#   Volume: EMorSimpleShape::OrientedBox, BoxExtent: (57.8, 118.1, 200.4)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (3747.8186, 1290.7563, 1277.5277), (0.0, 0.0, -0.0), (1.1568, 2.3617, 4.0088), "Orc_Palissade_Post_A17", _folder)
if a: placed += 1
else: skipped += 1

# Construction: Orc_Palissade_Post_A18
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Wood
#   Volume: EMorSimpleShape::OrientedBox, BoxExtent: (57.8, 118.1, 200.4)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (4047.8186, 1290.7563, 1277.5277), (0.0, 0.0, -0.0), (1.1568, 2.3617, 4.0088), "Orc_Palissade_Post_A18", _folder)
if a: placed += 1
else: skipped += 1

# Construction: Orc_Palissade_Post_A19_9
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Wood
#   Volume: EMorSimpleShape::OrientedBox, BoxExtent: (57.8, 118.1, 200.4)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (2947.818, 1290.7563, 1272.5277), (0.0, 0.0, -0.0), (1.1568, 2.3617, 4.0088), "Orc_Palissade_Post_A19_9", _folder)
if a: placed += 1
else: skipped += 1

# Construction: Orc_Palissade_Post_A2
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Wood
#   Volume: EMorSimpleShape::OrientedBox, BoxExtent: (167.5, 186.0, 332.0)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (5916.654, 1113.4246, 1295.749), (0.0, 0.0, -0.0), (3.3504, 3.7204, 6.6396), "Orc_Palissade_Post_A2", _folder)
if a: placed += 1
else: skipped += 1

# Construction: Orc_Palissade_Post_A20_10
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Wood
#   Volume: EMorSimpleShape::OrientedBox, BoxExtent: (57.8, 118.1, 200.4)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (2347.8186, 1290.7563, 1272.5277), (0.0, 0.0, -0.0), (1.1568, 2.3617, 4.0088), "Orc_Palissade_Post_A20_10", _folder)
if a: placed += 1
else: skipped += 1

# Construction: Orc_Palissade_Post_A21_11
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Wood
#   Volume: EMorSimpleShape::OrientedBox, BoxExtent: (57.8, 118.1, 200.4)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (2647.8186, 1290.7563, 1277.5277), (0.0, 0.0, -0.0), (1.1568, 2.3617, 4.0088), "Orc_Palissade_Post_A21_11", _folder)
if a: placed += 1
else: skipped += 1

# Construction: Orc_Palissade_Post_A3_2
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Wood
#   Volume: EMorSimpleShape::OrientedBox, BoxExtent: (57.8, 118.1, 200.4)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (4332.8184, 1280.7563, 1277.5277), (0.0, 0.0, -0.0), (1.1568, 2.3617, 4.0088), "Orc_Palissade_Post_A3_2", _folder)
if a: placed += 1
else: skipped += 1

# Construction: Orc_Palissade_Post_A4
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Wood
#   Volume: EMorSimpleShape::OrientedBox, BoxExtent: (57.8, 118.1, 200.4)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (2052.818, 1280.7563, 1277.5277), (0.0, 0.0, -0.0), (1.1568, 2.3617, 4.0088), "Orc_Palissade_Post_A4", _folder)
if a: placed += 1
else: skipped += 1

# Construction: Orc_Palissade_Post_A7_3
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Wood
#   Volume: EMorSimpleShape::OrientedBox, BoxExtent: (57.8, 118.1, 200.4)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (3447.8184, 1290.7563, 1272.5277), (0.0, 0.0, -0.0), (1.1568, 2.3617, 4.0088), "Orc_Palissade_Post_A7_3", _folder)
if a: placed += 1
else: skipped += 1

# Construction: Orc_Palissade_Wall_3X1M_A13_2
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Scaffolding
#   Volume: EMorSimpleShape::OrientedBox, BoxExtent: (160.0, 30.4, 108.5)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (4205.2964, 1405.0237, 1769.4935), (0.0, 0.0, -0.0), (3.2004, 0.6083, 2.1694), "Orc_Palissade_Wall_3X1M_A13_2", _folder)
if a: placed += 1
else: skipped += 1

# Construction: Orc_Palissade_Wall_3X1M_A14_2
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Scaffolding
#   Volume: EMorSimpleShape::OrientedBox, BoxExtent: (160.0, 30.4, 108.5)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (2805.2969, 1405.0237, 1769.4935), (0.0, 0.0, -0.0), (3.2004, 0.6083, 2.1694), "Orc_Palissade_Wall_3X1M_A14_2", _folder)
if a: placed += 1
else: skipped += 1

# Construction: Orc_Palissade_Wall_3X1M_B3_3
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Scaffolding
#   Volume: EMorSimpleShape::OrientedBox, BoxExtent: (187.6, 34.1, 123.2)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (3577.6616, 1383.7355, 1764.0109), (0.0, 0.0, -0.0), (3.7524, 0.6817, 2.4647), "Orc_Palissade_Wall_3X1M_B3_3", _folder)
if a: placed += 1
else: skipped += 1

# Construction: Orc_Palissade_Wall_3X1M_B4_4
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Scaffolding
#   Volume: EMorSimpleShape::OrientedBox, BoxExtent: (187.6, 34.1, 123.2)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (2177.6616, 1383.7355, 1764.0109), (0.0, 0.0, -0.0), (3.7524, 0.6817, 2.4647), "Orc_Palissade_Wall_3X1M_B4_4", _folder)
if a: placed += 1
else: skipped += 1

# Construction: Orc_Palissade_Wall_3X1M_B8
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Scaffolding
#   Volume: EMorSimpleShape::OrientedBox, BoxExtent: (187.6, 34.1, 123.2)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (3877.6628, 1383.736, 1764.0109), (0.0, 0.0, -0.0), (3.7524, 0.6817, 2.4647), "Orc_Palissade_Wall_3X1M_B8", _folder)
if a: placed += 1
else: skipped += 1

# Construction: Orc_Palissade_Wall_3X1M_B9_5
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Scaffolding
#   Volume: EMorSimpleShape::OrientedBox, BoxExtent: (187.6, 34.1, 123.2)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (2477.6628, 1383.736, 1764.0109), (0.0, 0.0, -0.0), (3.7524, 0.6817, 2.4647), "Orc_Palissade_Wall_3X1M_B9_5", _folder)
if a: placed += 1
else: skipped += 1

# Construction: Orc_Palissade_Wall_3X3M_A26_6
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Scaffolding
#   Volume: EMorSimpleShape::OrientedBox, BoxExtent: (186.9, 35.3, 211.2)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (3603.6763, 1389.9995, 1621.2737), (0.0, 0.0, -0.0), (3.7388, 0.7061, 4.2240), "Orc_Palissade_Wall_3X3M_A26_6", _folder)
if a: placed += 1
else: skipped += 1

# Construction: Orc_Palissade_Wall_3X3M_A27
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Scaffolding
#   Volume: EMorSimpleShape::OrientedBox, BoxExtent: (186.9, 35.3, 211.2)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (3896.325, 1390.0004, 1578.7263), (0.0, 0.0, -0.0), (3.7388, 0.7061, 4.2240), "Orc_Palissade_Wall_3X3M_A27", _folder)
if a: placed += 1
else: skipped += 1

# Construction: Orc_Palissade_Wall_3X3M_A28
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Scaffolding
#   Volume: EMorSimpleShape::OrientedBox, BoxExtent: (186.9, 35.3, 211.2)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (4203.676, 1389.9995, 1321.2737), (0.0, 0.0, -0.0), (3.7388, 0.7061, 4.2240), "Orc_Palissade_Wall_3X3M_A28", _folder)
if a: placed += 1
else: skipped += 1

# Construction: Orc_Palissade_Wall_3X3M_A29_6
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Scaffolding
#   Volume: EMorSimpleShape::OrientedBox, BoxExtent: (186.9, 35.3, 211.2)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (2203.6763, 1389.9995, 1621.2737), (0.0, 0.0, -0.0), (3.7388, 0.7061, 4.2240), "Orc_Palissade_Wall_3X3M_A29_6", _folder)
if a: placed += 1
else: skipped += 1

# Construction: Orc_Palissade_Wall_3X3M_A30_7
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Scaffolding
#   Volume: EMorSimpleShape::OrientedBox, BoxExtent: (186.9, 35.3, 211.2)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (2496.325, 1390.0004, 1578.7263), (0.0, 0.0, -0.0), (3.7388, 0.7061, 4.2240), "Orc_Palissade_Wall_3X3M_A30_7", _folder)
if a: placed += 1
else: skipped += 1

# Construction: Orc_Palissade_Wall_3X3M_A31_8
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Scaffolding
#   Volume: EMorSimpleShape::OrientedBox, BoxExtent: (186.9, 35.3, 211.2)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (2803.6765, 1389.9995, 1321.2737), (0.0, 0.0, -0.0), (3.7388, 0.7061, 4.2240), "Orc_Palissade_Wall_3X3M_A31_8", _folder)
if a: placed += 1
else: skipped += 1

# Construction: Orc_Palissade_Wall_3X3M_A32
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Scaffolding
#   Volume: EMorSimpleShape::OrientedBox, BoxExtent: (35.3, 186.9, 211.2)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (2050.0002, 1486.3236, 1721.2737), (0.0, 0.0, -0.0), (0.7061, 3.7388, 4.2240), "Orc_Palissade_Wall_3X3M_A32", _folder)
if a: placed += 1
else: skipped += 1

# Construction: Orc_Palissade_Wall_3X3M_C10
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Scaffolding
#   Volume: EMorSimpleShape::OrientedBox, BoxExtent: (154.9, 25.6, 199.2)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (3898.089, 1391.6554, 1299.3085), (0.0, 0.0, -0.0), (3.0971, 0.5121, 3.9831), "Orc_Palissade_Wall_3X3M_C10", _folder)
if a: placed += 1
else: skipped += 1

# Construction: Orc_Palissade_Wall_3X3M_C11_7
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Scaffolding
#   Volume: EMorSimpleShape::OrientedBox, BoxExtent: (154.9, 25.6, 199.2)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (2498.089, 1391.6554, 1299.3085), (0.0, 0.0, -0.0), (3.0971, 0.5121, 3.9831), "Orc_Palissade_Wall_3X3M_C11_7", _folder)
if a: placed += 1
else: skipped += 1

# Construction: Orc_Palissade_Wall_3X3M_C3_6
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Scaffolding
#   Volume: EMorSimpleShape::OrientedBox, BoxExtent: (154.9, 25.6, 199.2)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (3598.088, 1391.6549, 1299.3085), (0.0, 0.0, -0.0), (3.0971, 0.5121, 3.9831), "Orc_Palissade_Wall_3X3M_C3_6", _folder)
if a: placed += 1
else: skipped += 1

# Construction: Orc_Palissade_Wall_3X3M_C4_9
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Scaffolding
#   Volume: EMorSimpleShape::OrientedBox, BoxExtent: (154.9, 25.6, 199.2)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (4198.088, 1391.6549, 1599.3085), (0.0, 0.0, -0.0), (3.0971, 0.5121, 3.9831), "Orc_Palissade_Wall_3X3M_C4_9", _folder)
if a: placed += 1
else: skipped += 1

# Construction: Orc_Palissade_Wall_3X3M_C5_6
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Scaffolding
#   Volume: EMorSimpleShape::OrientedBox, BoxExtent: (154.9, 25.6, 199.2)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (2198.088, 1391.6549, 1299.3085), (0.0, 0.0, -0.0), (3.0971, 0.5121, 3.9831), "Orc_Palissade_Wall_3X3M_C5_6", _folder)
if a: placed += 1
else: skipped += 1

# Construction: Orc_Palissade_Wall_3X3M_C6_8
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Scaffolding
#   Volume: EMorSimpleShape::OrientedBox, BoxExtent: (154.9, 25.6, 199.2)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (2798.0881, 1391.6549, 1599.3085), (0.0, 0.0, -0.0), (3.0971, 0.5121, 3.9831), "Orc_Palissade_Wall_3X3M_C6_8", _folder)
if a: placed += 1
else: skipped += 1

# Construction: Orc_Palissade_Wall_3X3M_C7
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Scaffolding
#   Volume: EMorSimpleShape::OrientedBox, BoxExtent: (25.6, 154.9, 199.2)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (2048.3447, 1498.0876, 1399.3085), (0.0, 0.0, -0.0), (0.5121, 3.0971, 3.9831), "Orc_Palissade_Wall_3X3M_C7", _folder)
if a: placed += 1
else: skipped += 1

# Construction: Orc_Post_Large_A2
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Wood
#   Volume: EMorSimpleShape::OrientedBox, BoxExtent: (21.9, 238.0, 21.7)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (5649.837, 891.96484, 1671.3003), (0.0, 0.0, -0.0), (0.4374, 4.7597, 0.4332), "Orc_Post_Large_A2", _folder)
if a: placed += 1
else: skipped += 1

# Construction: Orc_Scaffolding_Beam_3m_2
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Scaffolding
#   Volume: EMorSimpleShape::OrientedBox, BoxExtent: (161.5, 23.8, 69.6)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (3590.0928, 1363.9705, 1455.0964), (0.0, 0.0, -0.0), (3.2305, 0.4769, 1.3918), "Orc_Scaffolding_Beam_3m_2", _folder)
if a: placed += 1
else: skipped += 1

# Construction: Orc_Scaffolding_Beam_3m10_15
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Scaffolding
#   Volume: EMorSimpleShape::OrientedBox, BoxExtent: (161.5, 23.8, 69.6)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (2809.908, 1363.9705, 1744.9025), (0.0, 0.0, -0.0), (3.2305, 0.4769, 1.3918), "Orc_Scaffolding_Beam_3m10_15", _folder)
if a: placed += 1
else: skipped += 1

# Construction: Orc_Scaffolding_Beam_3m11_16
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Scaffolding
#   Volume: EMorSimpleShape::OrientedBox, BoxExtent: (161.5, 23.8, 69.6)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (2509.9094, 1366.029, 1755.0955), (0.0, 0.0, -0.0), (3.2305, 0.4769, 1.3918), "Orc_Scaffolding_Beam_3m11_16", _folder)
if a: placed += 1
else: skipped += 1

# Construction: Orc_Scaffolding_Beam_3m12_17
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Scaffolding
#   Volume: EMorSimpleShape::OrientedBox, BoxExtent: (161.5, 23.8, 69.6)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (2190.0925, 1363.9705, 1755.0966), (0.0, 0.0, -0.0), (3.2305, 0.4769, 1.3918), "Orc_Scaffolding_Beam_3m12_17", _folder)
if a: placed += 1
else: skipped += 1

# Construction: Orc_Scaffolding_Beam_3m2_4
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Scaffolding
#   Volume: EMorSimpleShape::OrientedBox, BoxExtent: (161.5, 23.8, 69.6)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (3890.094, 1366.029, 1444.9034), (0.0, 0.0, -0.0), (3.2305, 0.4769, 1.3918), "Orc_Scaffolding_Beam_3m2_4", _folder)
if a: placed += 1
else: skipped += 1

# Construction: Orc_Scaffolding_Beam_3m3
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Scaffolding
#   Volume: EMorSimpleShape::OrientedBox, BoxExtent: (161.5, 23.8, 69.6)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (4209.9077, 1363.9705, 1444.9034), (0.0, 0.0, -0.0), (3.2305, 0.4769, 1.3918), "Orc_Scaffolding_Beam_3m3", _folder)
if a: placed += 1
else: skipped += 1

# Construction: Orc_Scaffolding_Beam_3m4
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Scaffolding
#   Volume: EMorSimpleShape::OrientedBox, BoxExtent: (161.5, 23.8, 69.6)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (4209.9077, 1363.9705, 1744.9025), (0.0, 0.0, -0.0), (3.2305, 0.4769, 1.3918), "Orc_Scaffolding_Beam_3m4", _folder)
if a: placed += 1
else: skipped += 1

# Construction: Orc_Scaffolding_Beam_3m5
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Scaffolding
#   Volume: EMorSimpleShape::OrientedBox, BoxExtent: (161.5, 23.8, 69.6)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (3909.9094, 1366.029, 1755.0955), (0.0, 0.0, -0.0), (3.2305, 0.4769, 1.3918), "Orc_Scaffolding_Beam_3m5", _folder)
if a: placed += 1
else: skipped += 1

# Construction: Orc_Scaffolding_Beam_3m6
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Scaffolding
#   Volume: EMorSimpleShape::OrientedBox, BoxExtent: (161.5, 23.8, 69.6)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (3590.0925, 1363.9705, 1755.0966), (0.0, 0.0, -0.0), (3.2305, 0.4769, 1.3918), "Orc_Scaffolding_Beam_3m6", _folder)
if a: placed += 1
else: skipped += 1

# Construction: Orc_Scaffolding_Beam_3m7_12
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Scaffolding
#   Volume: EMorSimpleShape::OrientedBox, BoxExtent: (161.5, 23.8, 69.6)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (2190.0928, 1363.9705, 1455.0964), (0.0, 0.0, -0.0), (3.2305, 0.4769, 1.3918), "Orc_Scaffolding_Beam_3m7_12", _folder)
if a: placed += 1
else: skipped += 1

# Construction: Orc_Scaffolding_Beam_3m8_13
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Scaffolding
#   Volume: EMorSimpleShape::OrientedBox, BoxExtent: (161.5, 23.8, 69.6)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (2490.094, 1366.029, 1444.9034), (0.0, 0.0, -0.0), (3.2305, 0.4769, 1.3918), "Orc_Scaffolding_Beam_3m8_13", _folder)
if a: placed += 1
else: skipped += 1

# Construction: Orc_Scaffolding_Beam_3m9_14
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Scaffolding
#   Volume: EMorSimpleShape::OrientedBox, BoxExtent: (161.5, 23.8, 69.6)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (2809.908, 1363.9705, 1444.9034), (0.0, 0.0, -0.0), (3.2305, 0.4769, 1.3918), "Orc_Scaffolding_Beam_3m9_14", _folder)
if a: placed += 1
else: skipped += 1

# Construction: Orc_Scaffolding_Ladder_2
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Scaffolding
#   Volume: EMorSimpleShape::OrientedBox, BoxExtent: (41.2, 71.2, 223.2)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (3778.865, 1539.2571, 1591.3065), (0.0, 0.0, -0.0), (0.8239, 1.4245, 4.4644), "Orc_Scaffolding_Ladder_2", _folder)
if a: placed += 1
else: skipped += 1

# Construction: Orc_Scaffolding_Ladder2
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Scaffolding
#   Volume: EMorSimpleShape::OrientedBox, BoxExtent: (41.2, 71.2, 223.2)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (2621.136, 1540.7429, 1591.3066), (0.0, 0.0, -0.0), (0.8239, 1.4245, 4.4644), "Orc_Scaffolding_Ladder2", _folder)
if a: placed += 1
else: skipped += 1

# Construction: Orc_Scaffolding_Post_Deco_D_2
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Scaffolding
#   Volume: EMorSimpleShape::OrientedBox, BoxExtent: (99.1, 96.5, 94.0)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (5905.5615, 1117.3942, 1472.5482), (0.0, 0.0, -0.0), (1.9818, 1.9302, 1.8793), "Orc_Scaffolding_Post_Deco_D_2", _folder)
if a: placed += 1
else: skipped += 1

# Construction: Orc_Scaffolding_Post_Deco_D2_2
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Scaffolding
#   Volume: EMorSimpleShape::OrientedBox, BoxExtent: (29.3, 109.0, 94.0)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (5635.3774, 872.178, 1589.2421), (0.0, 0.0, -0.0), (0.5868, 2.1801, 1.8793), "Orc_Scaffolding_Post_Deco_D2_2", _folder)
if a: placed += 1
else: skipped += 1

# Construction: Orc_Scaffolding_Support_Post3
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Scaffolding
#   Volume: EMorSimpleShape::OrientedBox, BoxExtent: (56.0, 206.3, 246.9)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (5642.895, 622.2532, 1649.6776), (0.0, 0.0, -0.0), (1.1192, 4.1256, 4.9381), "Orc_Scaffolding_Support_Post3", _folder)
if a: placed += 1
else: skipped += 1

# ======================================================================
# PHASE 3: Breakables + DecoVolumes
# ======================================================================
unreal.log(f"[{BUBBLE_NAME}] Phase 3: Placing breakables and deco volumes...")

_folder = "Reconstruction/BD_BB_OrcTown_Gate/Breakables"

# Breakable Batch 0: BP_DM_Defiled_Statues_H_A_Deco_D_Breakable (1 instances)
#   BP Class: /Game/LevelDesign/Deco/Defiled/BP_DM_Defiled_Statues_H_A_Deco_D_Breakable
_brk_mesh = "/Game/Art/Assets/Kits/Deco/Defiled/Defiled_Statues_H_A_Deco_D"
_brk_mats = ['/Game/Art/Assets/Kits/Deco/Orc/Materials/Orc_Lighting/MI_Orc_Lighting']
a = spawn_static_mesh(_brk_mesh, _brk_mats, (5725.6733, 1297.9517, 1008.2765), (6.1956772135145, -104.49147684736472, 5.728900886204067), (1.0, 1.0, 1.0), "BP_DM_Defiled_Statues_H_A_Deco_D_Breakable4", _folder)
if a: placed += 1
else: skipped += 1

# Breakable Batch 1: BP_DM_Defiled_Statues_H_A_Deco_E_Breakable (1 instances)
#   BP Class: /Game/LevelDesign/Deco/Defiled/BP_DM_Defiled_Statues_H_A_Deco_E_Breakable
_brk_mesh = "/Game/Art/Assets/Kits/Deco/Defiled/Defiled_Statues_H_A_Deco_E"
_brk_mats = ['/Game/Art/Assets/Kits/Deco/Orc/Materials/Orc_Lighting/MI_Orc_Lighting']
a = spawn_static_mesh(_brk_mesh, _brk_mats, (5502.7993, 514.9523, 1024.5815), (0.0, -60.000067159027765, 0.0), (1.0, 1.0, 1.0), "BP_DM_Defiled_Statues_H_A_Deco_E_Breakable2_2", _folder)
if a: placed += 1
else: skipped += 1

# Breakable Batch 2: BP_DM_Warren_Animal_Meat_A_Breakable (3 instances)
#   BP Class: /Game/LevelDesign/Deco/GoblinWarren/BP_DM_Warren_Animal_Meat_A_Breakable
_brk_mesh = "/Game/Art/Assets/Kits/Deco/Orc/Warren_Animal_Meat_A"
_brk_mats = ['/Game/Art/Assets/Kits/Deco/Orc/Materials/Orc_Lighting/MI_Orc_Lighting']
a = spawn_static_mesh(_brk_mesh, _brk_mats, (5970.041, 702.2332, 1473.7395), (0.0, 149.99999400439492, -0.0), (1.0, 1.0, 1.0), "BP_DM_Warren_Animal_Meat_A_Breakable10", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_brk_mesh, _brk_mats, (5980.0464, 807.2344, 1447.673), (0.0, 90.00001925454748, -0.0), (1.0, 1.0, 1.0), "BP_DM_Warren_Animal_Meat_A_Breakable8", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_brk_mesh, _brk_mats, (6062.708, 836.7135, 1455.2788), (0.0, 149.99999400439492, -0.0), (1.0, 1.0, 1.0), "BP_DM_Warren_Animal_Meat_A_Breakable9", _folder)
if a: placed += 1
else: skipped += 1

# Breakable Batch 3: BP_DM_Warren_Cage_A_Breakable (1 instances)
#   BP Class: /Game/LevelDesign/Deco/GoblinWarren/BP_DM_Warren_Cage_A_Breakable
_brk_mesh = "/Game/Art/Assets/Kits/Deco/Orc/Warren_Cage_A"
_brk_mats = ['/Game/Art/Assets/Kits/Deco/Orc/Materials/Orc_Lighting/MI_Orc_Lighting', '/Game/Art/Assets/Kits/Deco_Architecture/Orc_Camp/Materials/MI_Orc_Scaffolding_Platforms']
a = spawn_static_mesh(_brk_mesh, _brk_mats, (5530.0, 1400.0, 1020.0), (0.0, 95.00001100271638, -0.0), (1.0, 1.0, 1.0), "BP_DM_Warren_Cage_A_Breakable_2", _folder)
if a: placed += 1
else: skipped += 1

# Breakable Batch 4: BP_DM_Warren_lighting_Banner_A_Breakable (1 instances)
#   BP Class: /Game/LevelDesign/Deco/GoblinWarren/BP_DM_Warren_lighting_Banner_A_Breakable
_brk_mesh = "/Game/Art/Assets/Kits/Deco/Orc/Warren_lighting_Banner_A"
_brk_mats = ['/Game/Art/Assets/Kits/Deco/Orc/Materials/Orc_Lighting/Rubble_Masonry_Pile_Base_Inst', '/Game/Art/Assets/Kits/Deco/Orc/Materials/Orc_Lighting/MI_Orc_Lighting', '/Game/Art/Assets/Kits/Deco/Orc/Materials/Orc_Banners/MI_OrcBanners_B']
a = spawn_static_mesh(_brk_mesh, _brk_mats, (5770.267, 685.6963, 1013.94336), (0.0, 40.00012558574677, -0.0), (1.0, 1.0, 1.0), "BP_DM_Warren_lighting_Banner_A_Breakable_2", _folder)
if a: placed += 1
else: skipped += 1

# Breakable Batch 5: BP_DM_Warren_Prison_Door_Breakable (1 instances)
#   BP Class: /Game/LevelDesign/Deco/GoblinWarren/BP_DM_Warren_Prison_Door_Breakable
_brk_mesh = "/Game/Art/Assets/Kits/Deco/Orc/Warren_Prison_Door"
_brk_mats = ['/Game/Art/Assets/Kits/Deco/Orc/Materials/Orc_Lighting/MI_Orc_Lighting']
a = spawn_static_mesh(_brk_mesh, _brk_mats, (5460.0, 1270.0, 990.0), (0.0, -45.000056798727684, 0.0), (1.0, 1.0, 1.0), "BP_DM_Warren_Prison_Door_Breakable_2", _folder)
if a: placed += 1
else: skipped += 1

# Breakable Batch 6: BP_DM_Rubble_Masonry_Pile_A_Breakable (1 instances)
#   BP Class: /Game/LevelDesign/Deco/Rubble/BP_DM_Rubble_Masonry_Pile_A_Breakable
_brk_mesh = "/Game/Art/Assets/Kits/Deco/Rubble/Rubble_Masonry_Pile_A"
_brk_mats = ['/Game/Art/Assets/Kits/Deco/Rubble/Materials/Rubble_Masonry_Pile/MI_Rubble_Masonry_Pile_Atlas_Inst_A', '/Game/Art/Assets/Kits/Deco/Rubble/Materials/Rubble_Masonry_Pile/MI_Rubble_Masonry_Pile_Atlas_Inst_A']
a = spawn_static_mesh(_brk_mesh, _brk_mats, (4529.194, 1381.4122, 1105.8298), (0.0, 0.0, -0.0), (1.0, 1.0, 1.0), "BP_DM_Rubble_Masonry_Pile_A_Breakable_2", _folder)
if a: placed += 1
else: skipped += 1

# Breakable Batch 7: BP_DM_Rubble_Masonry_Pile_C_Breakable (1 instances)
#   BP Class: /Game/LevelDesign/Deco/Rubble/BP_DM_Rubble_Masonry_Pile_C_Breakable
_brk_mesh = "/Game/Art/Assets/Kits/Deco/Rubble/Rubble_Masonry_Pile_C"
_brk_mats = ['/Game/Art/Assets/Kits/Deco/Rubble/Materials/Rubble_Masonry_Pile/MI_Rubble_Masonry_Pile_Atlas_Inst_B', '/Game/Art/Assets/Kits/Deco/Rubble/Materials/Rubble_Masonry_Pile/MI_Rubble_Masonry_Pile_Atlas_Inst_A']
a = spawn_static_mesh(_brk_mesh, _brk_mats, (4904.4673, 1600.0261, 1095.5759), (0.0, 0.0, -0.0), (1.0, 1.0, 1.0), "BP_DM_Rubble_Masonry_Pile_C_Breakable_2", _folder)
if a: placed += 1
else: skipped += 1

# Breakable Batch 8: BP_DM_Rubble_Masonry_Pile_E_Breakable (1 instances)
#   BP Class: /Game/LevelDesign/Deco/Rubble/BP_DM_Rubble_Masonry_Pile_E_Breakable
_brk_mesh = "/Game/Art/Assets/Kits/Deco/Rubble/Rubble_Masonry_Pile_E_Optimized"
_brk_mats = ['/Game/Art/Assets/Kits/Deco/Rubble/Materials/Rubble_Masonry_Pile/MI_Rubble_Masonry_Pile_Atlas_Inst_A', '/Game/Art/Assets/Kits/Deco/Rubble/Materials/Rubble_Masonry_Pile/MI_Rubble_Masonry_Pile_Atlas_Inst_B']
a = spawn_static_mesh(_brk_mesh, _brk_mats, (4699.808, 1381.5743, 1119.6196), (0.0, 0.0, -0.0), (1.0, 1.0, 1.0), "BP_DM_Rubble_Masonry_Pile_E_Breakable_2", _folder)
if a: placed += 1
else: skipped += 1

# --- Extra DecoVolumes (not construction blocks) ---
_folder = "Reconstruction/BD_BB_OrcTown_Gate/DecoVolumes"

# DecoVolume: BP_Bonfire_TutorialOrc_2 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (3204.3962, 2969.8523, 1324.1664), (0.0, 0.0, -0.0), (2.6152, 2.4132, 3.1461), "DV_BP_Bonfire_TutorialOrc_2_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_DM_Defiled_Statues_H_A_Deco_D_Breakable4 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (5727.0044, 1298.803, 1018.93726), (0.0, 0.0, -0.0), (0.8614, 0.8149, 0.4608), "DV_BP_DM_Defiled_Statues_H_A_Deco_D_Breakable4_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_DM_Defiled_Statues_H_A_Deco_E_Breakable2_2 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (5502.7993, 514.9523, 1039.0919), (0.0, 0.0, -0.0), (0.8757, 0.8329, 1.5070), "DV_BP_DM_Defiled_Statues_H_A_Deco_E_Breakable2_2_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_DM_Orc_Shanty_Midden_A_C_Breakable2_8 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (5860.8613, 946.64954, 1015.98834), (0.0, 0.0, -0.0), (1.7930, 1.6573, 0.4328), "DV_BP_DM_Orc_Shanty_Midden_A_C_Breakable2_8_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_DM_Rubble_Masonry_Pile_A_Breakable_2 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (4543.4985, 1386.2347, 1175.2574), (0.0, 0.0, -0.0), (1.2743, 1.1677, 1.4244), "DV_BP_DM_Rubble_Masonry_Pile_A_Breakable_2_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_DM_Rubble_Masonry_Pile_C_Breakable_2 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (4889.527, 1604.7579, 1139.4667), (0.0, 0.0, -0.0), (1.9384, 1.8593, 0.9351), "DV_BP_DM_Rubble_Masonry_Pile_C_Breakable_2_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_DM_Rubble_Masonry_Pile_E_Breakable_2 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (4685.427, 1393.6267, 1142.9603), (0.0, 0.0, -0.0), (2.5083, 2.2457, 1.3025), "DV_BP_DM_Rubble_Masonry_Pile_E_Breakable_2_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_DM_Warehouse_Barrel_Breakable_2 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (5910.9214, 734.58624, 1017.4929), (0.0, 0.0, -0.0), (0.8936, 0.7818, 0.6967), "DV_BP_DM_Warehouse_Barrel_Breakable_2_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_DM_Warehouse_Crate_A_Broken_Breakable_2 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (5907.2363, 857.4509, 1032.8081), (0.0, 0.0, -0.0), (1.0364, 1.0364, 0.5570), "DV_BP_DM_Warehouse_Crate_A_Broken_Breakable_2_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_DM_Warren_Animal_Meat_A_Breakable10 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (5969.6304, 703.63403, 1446.4203), (0.0, 0.0, -0.0), (0.4523, 0.4493, 0.7360), "DV_BP_DM_Warren_Animal_Meat_A_Breakable10_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_DM_Warren_Animal_Meat_A_Breakable8 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (5981.054, 808.2905, 1420.3538), (0.0, 0.0, -0.0), (0.3259, 0.3341, 0.7360), "DV_BP_DM_Warren_Animal_Meat_A_Breakable8_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_DM_Warren_Animal_Meat_A_Breakable9 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (6062.2974, 838.1143, 1427.9596), (0.0, 0.0, -0.0), (0.4523, 0.4493, 0.7360), "DV_BP_DM_Warren_Animal_Meat_A_Breakable9_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_DM_Warren_Cage_A_Breakable_2 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (5529.9736, 1391.8586, 1142.9622), (0.0, 0.0, -0.0), (3.2635, 3.5917, 2.9836), "DV_BP_DM_Warren_Cage_A_Breakable_2_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_DM_Warren_lighting_Banner_A_Breakable_2 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (5773.73, 688.409, 1210.508), (0.0, 0.0, -0.0), (3.5545, 3.5296, 4.3417), "DV_BP_DM_Warren_lighting_Banner_A_Breakable_2_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_DM_Warren_Lighting_Firepit_Pig_B_Breakable_2 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (5841.7666, 1434.7137, 1072.253), (0.0, 0.0, -0.0), (2.4801, 1.2354, 1.4880), "DV_BP_DM_Warren_Lighting_Firepit_Pig_B_Breakable_2_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_DM_Warren_Lighting_Torch_Breakable4 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (5411.527, 757.28937, 1075.4235), (0.0, 0.0, -0.0), (1.0765, 1.0112, 1.9128), "DV_BP_DM_Warren_Lighting_Torch_Breakable4_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_DM_Warren_Prison_Door_Breakable_2 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (5527.615, 1203.0188, 1132.9868), (0.0, 0.0, -0.0), (1.8393, 1.8393, 3.0219), "DV_BP_DM_Warren_Prison_Door_Breakable_2_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: DecorationBlockingVolume_1 (EMorSimpleShape::Empty)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (3210.0, 2820.0, 1380.0), (0.0, 0.0, -0.0), (2.0000, 2.0000, 2.0000), "DV_DecorationBlockingVolume_1", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: Orc_Palissade_Barricade_A10_11 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (2200.0005, 1319.864, 1100.6648), (0.0, 0.0, -0.0), (3.7911, 1.5157, 2.1414), "DV_Orc_Palissade_Barricade_A10_11_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: Orc_Palissade_Barricade_A5_3 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (3900.001, 1319.8635, 1120.6648), (0.0, 0.0, -0.0), (3.7911, 1.5157, 2.1414), "DV_Orc_Palissade_Barricade_A5_3_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: Orc_Palissade_Barricade_A6_5 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (4200.0, 1319.864, 1120.6648), (0.0, 0.0, -0.0), (3.7911, 1.5157, 2.1414), "DV_Orc_Palissade_Barricade_A6_5_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: Orc_Palissade_Barricade_A8_9 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (2500.001, 1319.8635, 1100.6648), (0.0, 0.0, -0.0), (3.7911, 1.5157, 2.1414), "DV_Orc_Palissade_Barricade_A8_9_BRK", _folder)
if a: placed += 1
else: skipped += 1

# ======================================================================
# SUMMARY
# ======================================================================
unreal.log(f"[{BUBBLE_NAME}] Reconstruction complete: {placed} placed, {skipped} skipped, {errors} errors")
