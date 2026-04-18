"""Auto-generated level reconstruction script.
Bubble: BD_BB_Outdoor_ExpeditionStart
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

BUBBLE_NAME = "BD_BB_Outdoor_ExpeditionStart"
placed = 0
skipped = 0
errors = 0

# ======================================================================
# PHASE 1: InstancedMeshCatalog  (static mesh placement)
# ======================================================================
unreal.log(f"[{BUBBLE_NAME}] Phase 1: Placing static meshes...")

# Batch 0: StaticMesh'GPI_Bedroll' (1 instances)
_mesh_path = "/Game/Art/Assets/GPI/Base/GPI_Bedroll"
_materials = ['/Game/Art/Assets/GPI/Base/Materials/MI_GPI_Bedroll']
_folder = "Reconstruction/BD_BB_Outdoor_ExpeditionStart/Meshes"
a = spawn_static_mesh(_mesh_path, _materials, (5640.258, 4815.1885, 339.8702), (0.0, 68.51935489205232, -0.0), (1.0, 1.0, 1.0), "GPI_Bedroll_205", _folder)
if a: placed += 1
else: skipped += 1

# Batch 1: StaticMesh'GPI_Bedroll_Unrolled_A' (1 instances)
_mesh_path = "/Game/Art/Assets/GPI/Base/GPI_Bedroll_Unrolled_A"
_materials = ['/Game/Art/Assets/GPI/Base/Materials/MI_GPI_Bedroll']
_folder = "Reconstruction/BD_BB_Outdoor_ExpeditionStart/Meshes"
a = spawn_static_mesh(_mesh_path, _materials, (5544.9414, 4847.317, 339.87015), (0.0, -105.80743027774822, 0.0), (1.0, 1.0, 1.0), "GPI_Bedroll_Unrolled_A_199", _folder)
if a: placed += 1
else: skipped += 1

# Batch 2: StaticMesh'GPI_Bedroll_Unrolled_B' (1 instances)
_mesh_path = "/Game/Art/Assets/GPI/Base/GPI_Bedroll_Unrolled_B"
_materials = ['/Game/Art/Assets/GPI/Base/Materials/MI_GPI_Bedroll']
_folder = "Reconstruction/BD_BB_Outdoor_ExpeditionStart/Meshes"
a = spawn_static_mesh(_mesh_path, _materials, (5697.812, 5004.5913, 345.8453), (-1.558990166801516, -143.6506869793546, 0.5602676062480797), (1.0, 1.0, 1.0), "GPI_Bedroll_Unrolled_B_202", _folder)
if a: placed += 1
else: skipped += 1

# Batch 3: StaticMesh'Bottles_medicinal_decoction_1_SM' (1 instances)
_mesh_path = "/Game/Art/Assets/GPI/FoodStoreroom/Meshes/Bottles_medicinal_decoction_1_SM"
_materials = ['/Game/Art/Assets/GPI/FoodStoreroom/Materials/Bottle_M']
_folder = "Reconstruction/BD_BB_Outdoor_ExpeditionStart/Meshes"
a = spawn_static_mesh(_mesh_path, _materials, (5753.1904, 4912.0264, 346.49097), (0.0, 0.0, -0.0), (1.0, 1.0, 1.0), "Bottles_medicinal_decoction_1_SM_208", _folder)
if a: placed += 1
else: skipped += 1

# Batch 4: StaticMesh'GPI_Cranberries' (1 instances)
_mesh_path = "/Game/Art/Assets/GPI/OrganicMaterials/GPI_Cranberries"
_materials = ['/Game/Art/Assets/GPI/OrganicMaterials/Materials/MI_GPI_Ingredients_A']
_folder = "Reconstruction/BD_BB_Outdoor_ExpeditionStart/Meshes"
a = spawn_static_mesh(_mesh_path, _materials, (5678.068, 5008.202, 358.26413), (0.0, 168.66092424211666, -0.0), (1.0, 1.0, 1.0), "GPI_Cranberries_8", _folder)
if a: placed += 1
else: skipped += 1

# Batch 5: StaticMesh'GPI_Cutting_ElvenTree' (1 instances)
_mesh_path = "/Game/Art/Assets/GPI/OrganicMaterials/GPI_Cutting_ElvenTree"
_materials = ['/Game/Art/Assets/GPI/Generator/Materials/MI_GPI_Tree_Bark', '/Game/Art/Assets/GPI/Generator/Materials/MI_Tree_Branches_Pickup_Mat', '/Game/Art/Assets/GPI/OrganicMaterials/Materials/MI_GPI_Ingredients_A']
_folder = "Reconstruction/BD_BB_Outdoor_ExpeditionStart/Meshes"
a = spawn_static_mesh(_mesh_path, _materials, (5445.292, 5028.9253, 346.5516), (2.3372339472558807e-07, -19.329834160134755, 57.133128753250844), (2.0252802, 2.0252802, 2.0252802), "GPI_Cutting_ElvenTree_11", _folder)
if a: placed += 1
else: skipped += 1

# Batch 6: StaticMesh'SM_Lantern1A' (1 instances)
_mesh_path = "/Game/Art/Assets/GPI/Props/Meshes/Props/SM_Lantern1A"
_materials = ['/Game/Art/Assets/GPI/Props/Materials/M_Lantern']
_folder = "Reconstruction/BD_BB_Outdoor_ExpeditionStart/Meshes"
a = spawn_static_mesh(_mesh_path, _materials, (5624.288, 4767.6104, 344.66293), (0.0, 0.0, -0.0), (1.0, 1.0, 1.0), "SM_Lantern1A_2", _folder)
if a: placed += 1
else: skipped += 1

# Batch 7: StaticMesh'SM_LeatherBag' (1 instances)
_mesh_path = "/Game/Art/Assets/GPI/Props/Meshes/Props/SM_LeatherBag"
_materials = ['/Game/Art/Assets/GPI/Props/Materials/M_LeatherBag']
_folder = "Reconstruction/BD_BB_Outdoor_ExpeditionStart/Meshes"
a = spawn_static_mesh(_mesh_path, _materials, (5648.964, 4935.464, 344.3703), (0.0, -27.045653100087563, 0.0), (1.0, 1.0, 1.0), "SM_LeatherBag_5", _folder)
if a: placed += 1
else: skipped += 1

# Batch 8: StaticMesh'Kitchen_FoodRack_Cup_A' (1 instances)
_mesh_path = "/Game/Art/Assets/Kits/Deco/Urban/Kitchen/Kitchen_FoodRack_Cup_A"
_materials = ['/Game/Art/Assets/Kits/Deco/Urban/Kitchen/Material/Kitchen_FoodRack/MI_Kitchen_FoodRack']
_folder = "Reconstruction/BD_BB_Outdoor_ExpeditionStart/Meshes"
a = spawn_static_mesh(_mesh_path, _materials, (5701.4463, 4911.799, 342.58716), (0.0, 20.78312506740351, -0.0), (1.0, 1.0, 1.0), "Kitchen_FoodRack_Cup_A_116", _folder)
if a: placed += 1
else: skipped += 1

# Batch 9: StaticMesh'Kitchen_FoodRack_Pan_A' (1 instances)
_mesh_path = "/Game/Art/Assets/Kits/Deco/Urban/Kitchen/Kitchen_FoodRack_Pan_A"
_materials = ['/Game/Art/Assets/Kits/Deco/Urban/Kitchen/Material/Kitchen_FoodRack/MI_Kitchen_FoodRack']
_folder = "Reconstruction/BD_BB_Outdoor_ExpeditionStart/Meshes"
a = spawn_static_mesh(_mesh_path, _materials, (5513.5317, 5132.477, 350.0183), (0.0, 17.344592489565496, -0.0), (1.0, 1.0, 1.0), "Kitchen_FoodRack_Pan_A_214", _folder)
if a: placed += 1
else: skipped += 1

# Batch 10: StaticMesh'Tavern_Scatter_Bowl_B' (1 instances)
_mesh_path = "/Game/Art/Assets/Kits/Deco/Urban/Tavern/Tavern_Scatter_Bowl_B"
_materials = ['/Game/Art/Assets/Kits/Deco/Urban/Tavern/Materials/Tavern_Scatter_Bowl/MI_Tavern_Scatter_Bowl']
_folder = "Reconstruction/BD_BB_Outdoor_ExpeditionStart/Meshes"
a = spawn_static_mesh(_mesh_path, _materials, (5537.9346, 5105.817, 349.4355), (0.0, 0.0, -0.0), (1.0, 1.0, 1.0), "Tavern_Scatter_Bowl_B_217", _folder)
if a: placed += 1
else: skipped += 1

# Batch 11: StaticMesh'Tavern_Scatter_Bowl_C' (1 instances)
_mesh_path = "/Game/Art/Assets/Kits/Deco/Urban/Tavern/Tavern_Scatter_Bowl_C"
_materials = ['/Game/Art/Assets/Kits/Deco/Urban/Tavern/Materials/Tavern_Scatter_Bowl/MI_Tavern_Scatter_Bowl']
_folder = "Reconstruction/BD_BB_Outdoor_ExpeditionStart/Meshes"
a = spawn_static_mesh(_mesh_path, _materials, (5666.2666, 4871.9243, 342.38208), (0.0, 0.0, -0.0), (1.0, 1.0, 1.0), "Tavern_Scatter_Bowl_C_220", _folder)
if a: placed += 1
else: skipped += 1

# Batch 12: StaticMesh'Workshop_Scatter_Bucket_Wood' (1 instances)
_mesh_path = "/Game/Art/Assets/Kits/Deco/Urban/Workshop/Scatter/Workshop_Scatter_Bucket_Wood"
_materials = ['/Game/Art/Assets/Kits/Deco/Urban/Workshop/Materials/Workshop_Scatter_Bucket_Wood/MI_Workshop_Scatter_Bucket_Wood']
_folder = "Reconstruction/BD_BB_Outdoor_ExpeditionStart/Meshes"
a = spawn_static_mesh(_mesh_path, _materials, (5358.206, 5451.319, 356.02515), (-1.4976498436768537, -11.070035839038423, -14.133362014321047), (1.0, 1.0, 1.0), "Workshop_Scatter_Bucket_Wood6_53", _folder)
if a: placed += 1
else: skipped += 1

# Batch 13: StaticMesh'Workshop_Scatter_Rope_A' (1 instances)
_mesh_path = "/Game/Art/Assets/Kits/Deco/Urban/Workshop/Scatter/Workshop_Scatter_Rope_A"
_materials = ['/Game/Art/Assets/Kits/Deco_Architecture/Mines/Materials/Mines_Scaffolding/MI_Mines_Scaffolding_Rope_A']
_folder = "Reconstruction/BD_BB_Outdoor_ExpeditionStart/Meshes"
a = spawn_static_mesh(_mesh_path, _materials, (5796.6494, 4954.9375, 349.56323), (0.0, 0.0, -0.0), (1.0, 1.0, 1.0), "Workshop_Scatter_Rope_A_12", _folder)
if a: placed += 1
else: skipped += 1

# Batch 14: StaticMesh'Workshop_Scatter_Rope_E' (1 instances)
_mesh_path = "/Game/Art/Assets/Kits/Deco/Urban/Workshop/Scatter/Workshop_Scatter_Rope_E"
_materials = ['/Game/Art/Assets/Kits/Deco_Architecture/Mines/Materials/Mines_Scaffolding/MI_Mines_Scaffolding_Rope_A']
_folder = "Reconstruction/BD_BB_Outdoor_ExpeditionStart/Meshes"
a = spawn_static_mesh(_mesh_path, _materials, (5799.4077, 4956.8647, 349.56323), (0.0, 0.0, -0.0), (1.0, 1.0, 1.0), "Workshop_Scatter_Rope_E_14", _folder)
if a: placed += 1
else: skipped += 1

# Batch 15: StaticMesh'Workshop_Tool_Shovel_Scatter_A' (2 instances)
_mesh_path = "/Game/Art/Assets/Kits/Deco/Urban/Workshop/Scatter/Workshop_Tool_Shovel_Scatter_A"
_materials = ['/Game/Art/Assets/Kits/Deco/Urban/Workshop/Materials/Workshop_Scatter_Shovel/MI_Workshop_Scatter_Shovel_Deco']
_folder = "Reconstruction/BD_BB_Outdoor_ExpeditionStart/Meshes"
a = spawn_static_mesh(_mesh_path, _materials, (5014.651, 5516.318, 433.36557), (0.49805735333227513, 32.53124179598638, 26.62030982168318), (1.0, 1.0, 1.0), "Workshop_Tool_Shovel_Scatter_A_98", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (810.68964, 5555.0327, 589.7766), (37.31285902806159, -143.81943189789564, -2.190645077654325), (1.0, 1.0, 1.0), "Workshop_Tool_Shovel_Scatter_B2", _folder)
if a: placed += 1
else: skipped += 1

# Batch 16: StaticMesh'Workshop_Tool_Shovel_Scatter_B' (2 instances)
_mesh_path = "/Game/Art/Assets/Kits/Deco/Urban/Workshop/Scatter/Workshop_Tool_Shovel_Scatter_B"
_materials = ['/Game/Art/Assets/Kits/Deco/Urban/Workshop/Materials/Workshop_Scatter_Shovel/MI_Workshop_Scatter_Shovel_Deco']
_folder = "Reconstruction/BD_BB_Outdoor_ExpeditionStart/Meshes"
a = spawn_static_mesh(_mesh_path, _materials, (798.6846, 5545.0386, 569.3231), (37.31285902806159, -143.81943189789564, -2.190645077654325), (1.0, 1.0, 1.0), "Workshop_Tool_Shovel_Scatter_B_245", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5021.458, 5505.9854, 410.31165), (-0.4979243358405968, -147.4686741840432, -26.62023842240227), (1.0, 1.0, 1.0), "Workshop_Tool_Shovel_Scatter_B3", _folder)
if a: placed += 1
else: skipped += 1

# Batch 17: StaticMesh'Ruins_Stairs_Medium_B' (3 instances)
_mesh_path = "/Game/Art/Assets/Kits/Deco_Architecture/Ruins/Ruins_Stairs_Medium_B"
_materials = ['/Game/Art/Assets/Kits/Architecture/Suburbs/Materials/Suburbs_Stairs/MI_OutdoorSnow_Stairs_02', '/Game/Art/Assets/Kits/Architecture/Suburbs/Materials/Suburbs_Stairs/MI_OutdoorSnow_Stairs_01', '/Game/Art/Assets/Kits/Deco/Rubble/Materials/Rubble_Masonry_Pile/MI_OutdoorSnowRubble_Masonry_Pile_Base_Inst']
_folder = "Reconstruction/BD_BB_Outdoor_ExpeditionStart/Meshes"
a = spawn_static_mesh(_mesh_path, _materials, (3259.2385, 3484.0999, 605.2112), (0.0, 0.0, -15.43270807261074), (1.238508, 1.0, 1.0), "Ruins_Stairs_Medium_C2", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2953.7444, 3976.9175, 426.5346), (0.0, 0.0, -18.714904886084202), (1.0, 1.0, 1.0), "Ruins_Stairs_Medium_C5", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3257.1743, 3984.4724, 429.09384), (6.5776420796467585, 2.6402601054228896, -18.780333896734053), (1.0, 1.0, 1.0), "Ruins_Stairs_Medium_C6", _folder)
if a: placed += 1
else: skipped += 1

# Batch 18: StaticMesh'Ruins_Stairs_Medium_C' (1 instances)
_mesh_path = "/Game/Art/Assets/Kits/Deco_Architecture/Ruins/Ruins_Stairs_Medium_C"
_materials = ['/Game/Art/Assets/Kits/Architecture/Suburbs/Materials/Suburbs_Stairs/MI_OutdoorSnow_Stairs_02', '/Game/Art/Assets/Kits/Architecture/Suburbs/Materials/Suburbs_Stairs/MI_OutdoorSnow_Stairs_01', '/Game/Art/Assets/Kits/Deco/Rubble/Materials/Rubble_Masonry_Pile/MI_OutdoorSnowRubble_Masonry_Pile_Base_Inst']
_folder = "Reconstruction/BD_BB_Outdoor_ExpeditionStart/Meshes"
a = spawn_static_mesh(_mesh_path, _materials, (2983.732, 3470.963, 603.43256), (0.0, 0.0, -15.599914674251009), (1.0, 1.0, 1.0), "Ruins_Stairs_Medium_C_139", _folder)
if a: placed += 1
else: skipped += 1

# Batch 19: StaticMesh'Ruins_Stairs_Small_B' (1 instances)
_mesh_path = "/Game/Art/Assets/Kits/Deco_Architecture/Ruins/Ruins_Stairs_Small_B"
_materials = ['/Game/Art/Assets/Kits/Architecture/Suburbs/Materials/Suburbs_Stairs/MI_OutdoorSnow_Stairs_02', '/Game/Art/Assets/Kits/Architecture/Suburbs/Materials/Suburbs_Stairs/MI_OutdoorSnow_Stairs_01', '/Game/Art/Assets/Kits/Deco/Rubble/Materials/Rubble_Masonry_Pile/MI_OutdoorSnowRubble_Masonry_Pile_Base_Inst']
_folder = "Reconstruction/BD_BB_Outdoor_ExpeditionStart/Meshes"
a = spawn_static_mesh(_mesh_path, _materials, (3256.1633, 3789.5566, 586.0851), (1.6462393444875056, -0.41247559351771257, -13.416655749630436), (1.0, 1.0, 1.0), "Ruins_Stairs_Medium_C3", _folder)
if a: placed += 1
else: skipped += 1

# Batch 20: StaticMesh'Ruins_Stairs_Small_C' (1 instances)
_mesh_path = "/Game/Art/Assets/Kits/Deco_Architecture/Ruins/Ruins_Stairs_Small_C"
_materials = ['/Game/Art/Assets/Kits/Architecture/Suburbs/Materials/Suburbs_Stairs/MI_OutdoorSnow_Stairs_01', '/Game/Art/Assets/Kits/Architecture/Suburbs/Materials/Suburbs_Stairs/MI_OutdoorSnow_Stairs_02', '/Game/Art/Assets/Kits/Deco/Rubble/Materials/Rubble_Masonry_Pile/MI_OutdoorSnowRubble_Masonry_Pile_Base_Inst']
_folder = "Reconstruction/BD_BB_Outdoor_ExpeditionStart/Meshes"
a = spawn_static_mesh(_mesh_path, _materials, (2995.9668, 3778.3137, 583.0668), (0.0, 0.0, -10.712035676465653), (1.0, 1.0, 1.0), "Ruins_Stairs_Medium_C4", _folder)
if a: placed += 1
else: skipped += 1

# Batch 21: StaticMesh'Dirt_Mound_B' (2 instances)
_mesh_path = "/Game/Art/Assets/Kits/Misc/Dirt_Mounds/Dirt_Mound_B"
_materials = ['/Game/Art/Assets/Kits/Misc/Dirt_Mounds/Materials/Outdoor_Snow_Inst']
_folder = "Reconstruction/BD_BB_Outdoor_ExpeditionStart/Meshes"
a = spawn_static_mesh(_mesh_path, _materials, (3739.3835, 4991.9053, 419.08066), (-6.4104927916910155, 0.02150661501204689, -3.4206854096847077), (2.0, 2.6549191, 2.0), "Dirt_Mound_D8", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3355.358, 5444.5034, 464.743), (3.700980015719577, -149.12494562072138, -0.9834900702404282), (1.3742355, 2.7762403, 3.0937467), "Dirt_Mound_D9", _folder)
if a: placed += 1
else: skipped += 1

# Batch 22: StaticMesh'Dirt_Mound_D' (9 instances)
_mesh_path = "/Game/Art/Assets/Kits/Misc/Dirt_Mounds/Dirt_Mound_D"
_materials = ['/Game/Art/Assets/Kits/Misc/Dirt_Mounds/Materials/Outdoor_Snow_Inst']
_folder = "Reconstruction/BD_BB_Outdoor_ExpeditionStart/Meshes"
a = spawn_static_mesh(_mesh_path, _materials, (4599.4785, 4725.755, 331.67435), (0.0, 77.32217433536778, -0.0), (1.2385136, 1.2385136, 1.2385136), "Dirt_Mound_D_2", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3599.3982, 5521.1987, 438.6843), (-12.936827682300148, -80.65622916477606, 11.68185604376209), (1.211069, 1.211069, 0.5863887), "Dirt_Mound_D2_16", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3821.5757, 5621.6304, 382.70895), (-3.5305181267337873, -93.52338653650106, 6.626467007119089), (1.0, 1.0, 1.0), "Dirt_Mound_D3_19", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4223.149, 5226.5913, 336.33783), (-11.755857867675852, -27.62893391204014, 5.866318793871498), (1.0, 1.0, 0.8059249), "Dirt_Mound_D4", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (526.27893, 5265.436, 477.17307), (0.3282120164756941, -19.647062672483287, -1.5275267061895728), (1.4048861, 1.2200722, 1.3806485), "Dirt_Mound_D5_106", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4282.9556, 3577.7634, 804.4591), (0.0, 137.53751775694204, -0.0), (1.4426942, 1.238514, 1.5280637), "Dirt_Mound_D6", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5654.5903, 5555.3813, 332.5517), (0.0, 76.84076065919866, -0.0), (1.0, 1.0, 0.6755796), "Dirt_Mound_D7_8", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1147.9908, 4786.8076, 505.12463), (3.438378112683605, -89.99553730277134, -0.394988795051032), (1.0, 1.0, 1.0), "Dirt_Mound_E4_109", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1517.9006, 5746.299, 489.4062), (0.25627358506031644, 80.02233854414929, 1.8460551422697218), (1.0, 1.0, 1.029023), "Dirt_Mound_E5", _folder)
if a: placed += 1
else: skipped += 1

# Batch 23: StaticMesh'Dirt_Mound_E' (6 instances)
_mesh_path = "/Game/Art/Assets/Kits/Misc/Dirt_Mounds/Dirt_Mound_E"
_materials = ['/Game/Art/Assets/Kits/Misc/Dirt_Mounds/Materials/Outdoor_Snow_Inst']
_folder = "Reconstruction/BD_BB_Outdoor_ExpeditionStart/Meshes"
a = spawn_static_mesh(_mesh_path, _materials, (5222.166, 4621.2876, 337.77698), (0.0, 75.62474963609223, -0.0), (1.0533969, 1.0533969, 1.0533969), "Dirt_Mound_E_5", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5187.337, 5740.799, 339.73065), (-0.17300417043179808, 108.54656898488045, -0.23190309197921133), (1.3531355, 1.1672674, 1.4852711), "Dirt_Mound_E2", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3655.6062, 4912.099, 398.052), (2.64037314147969, -54.20956573397246, 8.95741375323143), (1.1382767, 1.087411, 0.9337253), "Dirt_Mound_E3_13", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1995.2904, 3656.8164, 798.09503), (0.0, 24.548838126685858, -0.0), (2.1838148, 1.2917304, 1.8376184), "Dirt_Mound_E6_133", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4065.603, 3630.7952, 801.51044), (0.0, -31.908845352016304, 0.0), (1.8556379, 1.0, 0.38596913), "Dirt_Mound_E7_42", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1576.5988, 3424.0815, 1796.8317), (-0.43627929348980327, -168.04990686238582, 2.0602200145125593), (0.9012471, 0.8892321, 2.018781), "Dirt_Mound_H24", _folder)
if a: placed += 1
else: skipped += 1

# Batch 24: StaticMesh'Dirt_Mound_F' (6 instances)
_mesh_path = "/Game/Art/Assets/Kits/Misc/Dirt_Mounds/Dirt_Mound_F"
_materials = ['/Game/Art/Assets/Kits/Misc/Dirt_Mounds/Materials/Outdoor_Snow_Inst']
_folder = "Reconstruction/BD_BB_Outdoor_ExpeditionStart/Meshes"
a = spawn_static_mesh(_mesh_path, _materials, (3896.9993, 5207.4014, 377.14615), (-0.29855343524409417, -168.85795746396042, -0.7151793988518967), (1.4085473, 1.0, 0.13095614), "Dirt_Mound_F_61", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2036.9818, 4691.0474, 484.31042), (0.0, -105.8412959625323, 0.0), (2.0426323, 2.017056, 1.7932869), "Dirt_Mound_F2_103", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3357.9434, 3729.5198, 678.10425), (3.0380134039127507, 4.407469427685804, 14.81690371823617), (1.5089266, 1.1935519, 0.94701016), "Dirt_Mound_F3_151", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2931.7405, 3762.746, 663.6079), (-4.715424437176363, 6.319115368556562, 18.607691171529673), (1.508927, 1.193552, 0.84526706), "Dirt_Mound_F4", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3330.151, 5072.5986, 424.67795), (-4.875580370932298, 30.536331809701984, -5.2056281282722106), (2.487698, 1.5937916, 1.0480083), "Dirt_Mound_F5_165", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1773.9648, 3078.0276, 1784.1068), (-2.0880431741092513, -97.46435900297064, 0.273439681167008), (1.636009, 1.1812676, 2.367352), "Dirt_Mound_H23", _folder)
if a: placed += 1
else: skipped += 1

# Batch 25: StaticMesh'Dirt_Mound_G' (9 instances)
_mesh_path = "/Game/Art/Assets/Kits/Misc/Dirt_Mounds/Dirt_Mound_G"
_materials = ['/Game/Art/Assets/Kits/Misc/Dirt_Mounds/Materials/Outdoor_Snow_Inst']
_folder = "Reconstruction/BD_BB_Outdoor_ExpeditionStart/Meshes"
a = spawn_static_mesh(_mesh_path, _materials, (911.8884, 5680.146, 512.26245), (1.140539100170534, 99.6619949053724, 0.060097595751096806), (1.4297482, 1.3317587, 1.504561), "Dirt_Mound_E8_15", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (812.8232, 5886.9717, 517.30756), (11.210799287261043, -68.88971477075417, 11.887546230518026), (1.4810255, 1.4898431, 1.4695654), "Dirt_Mound_E9_129", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4484.383, 4540.8677, 663.92365), (0.37290783266779787, -99.65690920556662, 1.569741787008508), (1.5294161, 1.5294161, 2.5679677), "Dirt_Mound_G2_54", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2031.5333, 4347.268, 601.2591), (12.137440365168956, 66.63146142944677, -0.13061567929845558), (1.9690353, 1.7794074, 2.9345489), "Dirt_Mound_G3_121", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3236.8389, 4192.2266, 555.16144), (3.795794946049598, 14.539625718203938, 8.262612347704614), (1.350377, 1.350377, 1.3128885), "Dirt_Mound_G4_148", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2899.7068, 4063.0225, 572.19745), (5.502974697201093, 179.03554545445243, -19.278962612521845), (1.6771573, 1.0, 1.509552), "Dirt_Mound_G5", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2238.4656, 4257.964, 600.7552), (7.848837865231159, 66.6415912800309, -1.3394473022651023), (1.969035, 1.779407, 2.934549), "Dirt_Mound_G6", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5375.524, 4286.554, 722.9115), (0.0, -88.93963695450446, 0.0), (1.155907, 1.0, 2.387892), "Dirt_Mound_G7", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2697.3284, 4509.811, 517.2018), (-4.381561068698552, 26.08109214571299, 4.515993274297889), (1.0, 0.92500347, 0.88716936), "Dirt_Mound_G8_5", _folder)
if a: placed += 1
else: skipped += 1

# Batch 26: StaticMesh'Dirt_Mound_H' (30 instances)
_mesh_path = "/Game/Art/Assets/Kits/Misc/Dirt_Mounds/Dirt_Mound_H"
_materials = ['/Game/Art/Assets/Kits/Misc/Dirt_Mounds/Materials/Outdoor_Snow_Inst']
_folder = "Reconstruction/BD_BB_Outdoor_ExpeditionStart/Meshes"
a = spawn_static_mesh(_mesh_path, _materials, (4411.2275, 5620.8315, 359.00797), (-2.3554992363639444, -67.58605700827543, 0.7327745501107871), (1.4694788, 1.4694788, 1.4694788), "Dirt_Mound_G_9", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4645.2056, 4437.042, 660.7478), (-2.0014645604173187, 160.76608357671387, -12.38659542234446), (2.2647004, 1.5636296, 1.8796592), "Dirt_Mound_H_94", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3899.222, 2788.037, 793.34375), (1.659872418394326, 51.99729654617235, -1.296539137010467), (2.6319861, 1.815119, 1.815119), "Dirt_Mound_H10", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2129.9565, 3609.481, 795.9686), (-2.0614623261646097, -78.18633730978937, -0.43109129162819126), (3.635512, 2.2934613, 1.815119), "Dirt_Mound_H11", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4179.462, 3670.5532, 805.0182), (0.0, 38.17479795405455, -0.0), (1.4668372, 1.319964, 0.8501049), "Dirt_Mound_H12_45", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5467.558, 5468.6343, 331.7425), (0.0, -23.28827012098441, 0.0), (1.0, 1.0, 1.8165252), "Dirt_Mound_H14_8", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2700.7632, 4489.247, 513.5262), (-4.110901014368472, 108.21117561031883, -1.3510435254746664), (1.4962689, 1.4962689, 1.9272339), "Dirt_Mound_H16_73", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1865.8188, 4627.0264, 667.86334), (4.0481120772395086e-08, 103.94830308799155, -1.7087705293080568), (0.99979246, 1.1547638, 1.5844356), "Dirt_Mound_H17_118", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2171.585, 5409.083, 490.74835), (-4.67584251456059, -45.39484062744472, -4.073547777867869), (1.7435575, 1.2918326, 1.1575592), "Dirt_Mound_H2_100", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5009.4673, 5600.025, 345.02994), (0.35078437962588904, -157.4207719061756, 0.5846093343666386), (1.516992, 1.605431, 0.96357393), "Dirt_Mound_H20", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1574.6389, 3178.2705, 1804.782), (-1.177581737725576, -33.988857025906476, -1.7460327554124733), (1.636009, 1.5769845, 2.367352), "Dirt_Mound_H21_8", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (993.4194, 5687.041, 517.60785), (1.423072271788107, -173.76177665950735, 7.290531365787574), (1.268554, 1.268554, 1.6381278), "Dirt_Mound_H22", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1765.2826, 3438.248, 1829.684), (2.058640127021119, 77.84136518254523, -0.4433593223778297), (0.901247, 0.889232, 0.553136), "Dirt_Mound_H25", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1733.0284, 3685.1157, 1832.306), (-0.33319090685668895, -170.90214732079508, 2.079259732397067), (0.901247, 0.889232, 0.44783178), "Dirt_Mound_H26", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2052.693, 3233.7036, 1826.9307), (0.10071796983389095, 69.37660735943425, 0.326127232239411), (0.901247, 0.5994693, 0.38139677), "Dirt_Mound_H27", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1944.8496, 3200.9382, 1827.867), (0.32836128089046923, 12.364469336983413, 0.09306540295728156), (0.901247, 0.599469, 0.53216994), "Dirt_Mound_H28", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1807.8256, 3403.1914, 1826.9817), (0.06278379753153342, -82.86333821626089, -0.3354491902928688), (0.901247, 0.599469, 0.53217), "Dirt_Mound_H29", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2543.567, 5364.463, 498.10446), (-3.1247562019107495, -56.778295067033596, -3.6453247451209663), (1.5802397, 1.2643012, 1.2643012), "Dirt_Mound_H3_116", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1984.926, 3425.367, 1828.0269), (0.06278399920484938, -82.86333821688945, -0.3354491695986354), (0.901247, 0.511869, 0.53217), "Dirt_Mound_H30", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1964.2806, 3597.0864, 1827.8422), (0.06207552977903306, 76.05804226445578, 0.3355474136446235), (0.75301427, 0.511869, 0.53217), "Dirt_Mound_H31", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1704.441, 3808.6821, 1826.2214), (0.06278399920484938, -82.86333821688945, -0.3354491695986354), (0.9683657, 0.6665877, 0.5992887), "Dirt_Mound_H32", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1245.7999, 4563.192, 639.5819), (-6.819215030516192, 148.57440413519024, 2.419471134484549), (1.7343191, 1.4807203, 3.393888), "Dirt_Mound_H6_130", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2292.1614, 3105.005, 804.9997), (-1.6815185845980982, -52.96539467560168, -1.2683412647436543), (1.815119, 1.815119, 1.815119), "Dirt_Mound_H7_136", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3887.7715, 5533.7114, 404.1474), (4.143151958159603, 140.56613328913934, 6.279901642250534), (1.261204, 1.261204, 1.261204), "Dirt_Mound_H8_162", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5080.159, 4689.0195, 334.99734), (-0.6817932657254715, -36.45708769003434, -1.1421238727128383e-08), (1.5169922, 1.6054312, 0.8255262), "Dirt_Mound_H9_15", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5505.3623, 4663.311, 335.0221), (0.0, 135.96622146022148, -0.0), (1.3901719, 1.0619718, 1.2612606), "Dirt_Mound_I10", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3235.02, 4746.5225, 487.28503), (-3.3066707185722897, 76.86201692039538, -2.6333615827061014), (1.4946201, 1.170016, 1.1824901), "Dirt_Mound_I12", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3100.0435, 5011.371, 472.48114), (1.8796410716712828, -78.07258148024384, 1.3972191099186702), (1.49462, 1.170016, 1.18249), "Dirt_Mound_I13", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3754.5134, 2711.5093, 800.3058), (0.0, 44.10537875817438, -0.0), (2.1877463, 1.6207223, 1.6207223), "Dirt_Mound_I6", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3778.2585, 3058.769, 810.3058), (0.0, -121.89459156217526, 0.0), (2.187746, 1.620722, 1.620722), "Dirt_Mound_I8", _folder)
if a: placed += 1
else: skipped += 1

# Batch 27: StaticMesh'Dirt_Mound_I' (12 instances)
_mesh_path = "/Game/Art/Assets/Kits/Misc/Dirt_Mounds/Dirt_Mound_I"
_materials = ['/Game/Art/Assets/Kits/Misc/Dirt_Mounds/Materials/Outdoor_Snow_Inst']
_folder = "Reconstruction/BD_BB_Outdoor_ExpeditionStart/Meshes"
a = spawn_static_mesh(_mesh_path, _materials, (3401.9172, 4483.4043, 476.72552), (4.869125154773702, -79.05413316725108, 3.464090445989149), (1.4721892, 1.1562512, 1.0067532), "Dirt_Mound_H13", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2158.0354, 4688.7466, 494.15488), (2.659955681991797, -73.0896114499284, 0.8910407248239254), (0.95397115, 0.8265521, 0.8210873), "Dirt_Mound_H19_141", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2451.5684, 5451.59, 502.9707), (-3.4965207447675817, -62.9180613124778, -3.2904052698540927), (1.315938, 1.0, 0.37033245), "Dirt_Mound_H4", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2510.2847, 4315.6987, 531.4478), (4.869125331759332, -79.05413317116462, 3.4640903002137273), (1.315938, 1.0, 0.85050184), "Dirt_Mound_H5", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4675.837, 5396.5347, 341.67526), (-1.4714965866061114, -87.58173070041482, -0.2631529645565595), (0.6198524, 0.7269508, 0.36985505), "Dirt_Mound_I_22", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2555.0684, 4560.6665, 498.8317), (-1.0638107344407352e-08, -10.83154343948509, 3.389028434027368), (0.7814017, 0.45679775, 0.46927214), "Dirt_Mound_I11_91", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5782.364, 5351.515, 341.39722), (0.0, 112.6798846884354, -0.0), (0.57171226, 0.44357783, 0.37732106), "Dirt_Mound_I2_24", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5536.548, 5678.945, 284.88943), (-1.9347232071605098, 84.87241912849656, 3.480788517964388), (1.0, 1.403632, 1.0), "Dirt_Mound_I3", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1719.9684, 4513.6035, 652.09845), (1.528562133419669, -87.79577975920814, -0.5338745919255891), (0.77776706, 0.77776706, 0.77776706), "Dirt_Mound_I4_127", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2620.9277, 2822.3623, 800.0), (0.0, 50.13308484149321, -0.0), (1.1149963, 1.1149963, 1.1149963), "Dirt_Mound_I5_319", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4494.0063, 3869.1836, 800.0), (0.0, -68.94030686267438, 0.0), (1.3119972, 1.3119972, 1.3119972), "Dirt_Mound_I7_327", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4387.014, 5436.119, 340.29907), (-0.002502510822458228, -102.08019218982756, 2.5289979975226613), (0.619852, 0.726951, 0.55175), "Dirt_Mound_I9", _folder)
if a: placed += 1
else: skipped += 1

# Batch 28: StaticMesh'Mining_Dirt_Mound_C' (1 instances)
_mesh_path = "/Game/Art/Assets/Kits/Misc/Dirt_Mounds/Mining_Dirt_Mound_C"
_materials = ['/Game/Art/Assets/Kits/Misc/Dirt_Mounds/Materials/Outdoor_Snow_Inst']
_folder = "Reconstruction/BD_BB_Outdoor_ExpeditionStart/Meshes"
a = spawn_static_mesh(_mesh_path, _materials, (2883.1462, 5230.694, 475.6267), (0.0, 69.01282907642735, -0.0), (3.2208652, 2.833863, 2.2982187), "Mining_Dirt_Mound_C_113", _folder)
if a: placed += 1
else: skipped += 1

# Batch 29: StaticMesh'Orc_Fort_9X9_Mound' (1 instances)
_mesh_path = "/Game/Art/Assets/Kits/Misc/Dirt_Mounds/Orc_Fort_9X9_Mound"
_materials = ['/Game/Art/Assets/Kits/Misc/Dirt_Mounds/Materials/Outdoor_Snow_Inst']
_folder = "Reconstruction/BD_BB_Outdoor_ExpeditionStart/Meshes"
a = spawn_static_mesh(_mesh_path, _materials, (905.6748, 5696.251, 551.66876), (13.974027503061214, 108.00775408279823, -3.5548705395246674), (1.4487232, 1.0, 1.0), "Orc_Fort_9X9_Mound_132", _folder)
if a: placed += 1
else: skipped += 1

# Batch 30: StaticMesh'OEE_Terrain_Segment_A' (1 instances)
_mesh_path = "/Game/Art/Assets/Misc/Levels/Expedition_Entrance/OEE_Terrain_Segment_A"
_materials = ['/Game/FX/IcePlug/MI_GuideMeshFloor_Snow_Base']
_folder = "Reconstruction/BD_BB_Outdoor_ExpeditionStart/Meshes"
a = spawn_static_mesh(_mesh_path, _materials, (0.0, 0.0, 0.0), (0.0, 0.0, -0.0), (1.0, 1.0, 1.0), "OEE_Terrain_Segment_A_240", _folder)
if a: placed += 1
else: skipped += 1

# Batch 31: StaticMesh'OEE_Terrain_Segment_B' (1 instances)
_mesh_path = "/Game/Art/Assets/Misc/Levels/Expedition_Entrance/OEE_Terrain_Segment_B"
_materials = ['/Game/FX/IcePlug/MI_GuideMeshFloor_Snow_Base']
_folder = "Reconstruction/BD_BB_Outdoor_ExpeditionStart/Meshes"
a = spawn_static_mesh(_mesh_path, _materials, (121.441895, 0.0, 0.0), (0.0, 0.0, -0.0), (1.0, 1.0, 1.0), "OEE_Terrain_Segment_B_242", _folder)
if a: placed += 1
else: skipped += 1

# Batch 32: StaticMesh'Dwarf_Armor_Helmet_TravelersHelmet' (1 instances)
_mesh_path = "/Game/CharacterArt/Dwarfs/Dwarf_Armor/Helmets/Dwarf_Armor_Helmet_TravelersHelmet"
_materials = ['/Game/CharacterArt/Dwarfs/Dwarf_Armor/Helmets/Materials/Helmet_TravelersHelmet/MI_Helmet_TravelersHelmet']
_folder = "Reconstruction/BD_BB_Outdoor_ExpeditionStart/Meshes"
a = spawn_static_mesh(_mesh_path, _materials, (5757.5347, 4775.622, 328.67627), (0.0, 0.0, 13.64176984694748), (1.0, 1.0, 1.0), "Dwarf_Armor_Helmet_TravelersHelmet_30", _folder)
if a: placed += 1
else: skipped += 1

# Batch 33: StaticMesh'Dwarf_Pack03_Static' (1 instances)
_mesh_path = "/Game/CharacterArt/Dwarfs/Dwarf_Backpacks/Dwarf_Pack03_Static"
_materials = ['/Game/CharacterArt/Dwarfs/Dwarf_Backpacks/Materials/Mountaineer/MI_D_Backpack_Mountaineer_v3']
_folder = "Reconstruction/BD_BB_Outdoor_ExpeditionStart/Meshes"
a = spawn_static_mesh(_mesh_path, _materials, (5671.238, 5035.555, 365.26007), (7.311840282323337e-05, -94.80655491697092, 90.00003551915988), (1.0, 1.0, 1.0), "Dwarf_Pack03_Static_223", _folder)
if a: placed += 1
else: skipped += 1

# Batch 34: StaticMesh'D_Weapon_Rohan_Spear1h' (1 instances)
_mesh_path = "/Game/DLC/RohanPack/Spear/D_Weapon_Rohan_Spear1h"
_materials = ['/Game/Items/Weapons/Models/Dwarf_Weapons/Materials/D_Weapon_Rohan_Spear1h/MI_D_Weapon_Rohan_Spear1h']
_folder = "Reconstruction/BD_BB_Outdoor_ExpeditionStart/Meshes"
a = spawn_static_mesh(_mesh_path, _materials, (5871.7656, 5097.703, 467.72867), (24.004477010912364, -0.6092834070633631, 178.50254040253773), (1.0, 1.0, 1.0), "D_Weapon_Rohan_Spear1h_36", _folder)
if a: placed += 1
else: skipped += 1

# Batch 35: StaticMesh'D_Weapon_IronHills_WarAxe1h' (1 instances)
_mesh_path = "/Game/Items/Weapons/Models/Dwarf_Weapons/D_Weapon_IronHills_WarAxe1h"
_materials = ['/Game/Items/Weapons/Models/Dwarf_Weapons/Materials/D_Weapon_IronHills_WarAxe1h/MI_D_Weapon_IronHills_WarAxe1h']
_folder = "Reconstruction/BD_BB_Outdoor_ExpeditionStart/Meshes"
a = spawn_static_mesh(_mesh_path, _materials, (5605.7183, 5453.1914, 369.16238), (-81.93746207254262, -125.50499428908965, 155.5400762973989), (1.0, 1.0, 1.0), "D_Weapon_IronHills_WarAxe1h_767", _folder)
if a: placed += 1
else: skipped += 1

# Batch 36: StaticMesh'Snow_08' (3 instances)
_mesh_path = "/Game/Unshippable/Cinematics/Cine001/Environment/Snow_08"
_materials = ['/Game/Art/Assets/Kits/Misc/Dirt_Mounds/Materials/Outdoor_Snow_Inst']
_folder = "Reconstruction/BD_BB_Outdoor_ExpeditionStart/Meshes"
a = spawn_static_mesh(_mesh_path, _materials, (6047.4985, 4984.771, 354.10388), (0.2941694227403986, 84.19822077679935, 3.298241598556246), (1.5655024, 2.5010357, 1.1006488), "Snow_10", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5858.5273, 5390.93, 353.20013), (0.2941693181000636, 135.24313236101202, 2.590332273004879), (0.78883636, 2.081893, 0.68150556), "Snow_11", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4655.196, 4733.879, 318.66998), (-0.2593993824751554, -25.57482644332432, -1.5278929323093033), (2.4745574, 2.1834073, 2.3376207), "Snow_09_232", _folder)
if a: placed += 1
else: skipped += 1

# Batch 37: StaticMesh'SM_Coal_01a' (1 instances)
_mesh_path = "/Game/Unshippable/ThirdParty/AncientTreasures/Meshes/SM_Coal_01a"
_materials = ['/Game/Unshippable/ThirdParty/AncientTreasures/Materials/Instances/MI_Coals_01a']
_folder = "Reconstruction/BD_BB_Outdoor_ExpeditionStart/Meshes"
a = spawn_static_mesh(_mesh_path, _materials, (5491.2812, 5075.2554, 345.27902), (0.0, 0.0, -0.0), (1.0, 1.0, 1.0), "SM_Coal_01a_11", _folder)
if a: placed += 1
else: skipped += 1

# Batch 38: StaticMesh'SM_Brick_03' (6 instances)
_mesh_path = "/Game/Unshippable/ThirdParty/Lordenfel/Environment/Architecture/Trims/Bricks/SM_Brick_03"
_materials = ['/Game/Unshippable/ThirdParty/Lordenfel/Environment/Materials/MI_Bricks_01']
_folder = "Reconstruction/BD_BB_Outdoor_ExpeditionStart/Meshes"
a = spawn_static_mesh(_mesh_path, _materials, (5477.9014, 5105.525, 353.37045), (1.3017110361579993, -0.03097536871233695, 88.63587366841796), (0.36, 0.36, 0.36), "SM_Brick_4", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5506.196, 5107.7275, 351.8404), (0.0, -34.20092875221447, 0.0), (0.36, 0.36, 0.36), "SM_Brick_5", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5527.682, 5056.761, 351.8404), (0.0, -123.16713947420018, 0.0), (0.36, 0.36, 0.36), "SM_Brick_6", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5499.07, 5039.2437, 353.37045), (1.301710954155094, -0.03097544878525652, 88.63587366662081), (0.36, 0.36, 0.36), "SM_Brick_7", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5466.3833, 5048.2505, 351.8404), (0.0, -37.363892346785896, 0.0), (0.36, 0.36, 0.36), "SM_Brick_8", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5458.1064, 5088.4785, 351.8404), (0.0, 66.6372149780251, -0.0), (0.36, 0.36, 0.36), "SM_Brick_03_2", _folder)
if a: placed += 1
else: skipped += 1

# Batch 39: StaticMesh'PWM_Quarry_1x1x1_A' (7 instances)
_mesh_path = "/Game/Unshippable/Whitebox/Rocks/Meshes/PWM_Quarry_1x1x1_A"
_materials = ['/Game/Environments/ProcTexturing/ProcMaterial_Quarry_Atlas_A_Snow_v2']
_folder = "Reconstruction/BD_BB_Outdoor_ExpeditionStart/Meshes"
a = spawn_static_mesh(_mesh_path, _materials, (1055.0, 4590.0, 755.0), (0.0, 20.000045392948085, -0.0), (1.0, 1.0, 1.0), "PWM_Quarry_1x1x1_A_190", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5432.775, 5472.671, 381.6805), (0.0, 9.228420502915725, -0.0), (0.57952064, 0.57952064, 0.57952064), "PWM_Quarry_1x1x1_A10_28", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4199.7524, 4621.005, 414.51498), (-9.838321336994018e-08, -27.651062936574778, -7.643646594629222), (3.402581, 2.5, 2.5), "PWM_Quarry_1x1x1_A2_3", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3414.8745, 4937.4478, 456.61273), (-4.888030393631429, 41.825401719643075, -17.50903172933188), (1.9966372, 1.0819204, 1.1693385), "PWM_Quarry_1x1x1_A4_159", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3444.1677, 4160.3564, 611.021), (6.630903221682827, -65.95384688178531, -0.15866117963498408), (3.402581, 2.5, 2.6187365), "PWM_Quarry_1x1x1_A5", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5499.3765, 4691.4375, 395.8745), (1.5023820121904956, 10.095912203369044, 3.296805904736928), (1.0107234, 0.88276154, 0.7512549), "PWM_Quarry_1x1x1_A8_14", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2792.7349, 4295.899, 570.5281), (-0.474548094017141, -73.62777985910333, -3.399841169448185), (1.9412816, 1.0, 1.4849036), "PWM_Quarry_3x3x20_431", _folder)
if a: placed += 1
else: skipped += 1

# Batch 40: StaticMesh'PWM_Quarry_1x1x1_B' (3 instances)
_mesh_path = "/Game/Unshippable/Whitebox/Rocks/Meshes/PWM_Quarry_1x1x1_B"
_materials = ['/Game/Environments/ProcTexturing/ProcMaterial_Quarry_Atlas_A_Snow_v2']
_folder = "Reconstruction/BD_BB_Outdoor_ExpeditionStart/Meshes"
a = spawn_static_mesh(_mesh_path, _materials, (990.0, 4605.0, 680.0), (0.0, 0.0, -0.0), (1.0, 1.0, 1.0), "PWM_Quarry_1x1x1_B_187", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4391.131, 4674.4863, 587.25903), (0.0, -42.16891345799042, 0.0), (0.49633023, 0.49633023, 0.49633023), "PWM_Quarry_1x1x1_B11_42", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3813.3452, 3247.3423, 814.19354), (2.705099136667758, -104.1488339392663, 89.31825805729363), (1.4471096, 1.4471096, 1.4471096), "PWM_Quarry_1x1x1_B2_51", _folder)
if a: placed += 1
else: skipped += 1

# Batch 41: StaticMesh'PWM_Quarry_1X1x1_C' (2 instances)
_mesh_path = "/Game/Unshippable/Whitebox/Rocks/Meshes/PWM_Quarry_1X1x1_C"
_materials = ['/Game/Environments/ProcTexturing/ProcMaterial_Quarry_Atlas_A_Snow_v2']
_folder = "Reconstruction/BD_BB_Outdoor_ExpeditionStart/Meshes"
a = spawn_static_mesh(_mesh_path, _materials, (4283.075, 3725.7874, 809.8011), (0.0, 0.0, -0.0), (1.0, 1.0, 1.0), "PWM_Quarry_1X1x1_C3_48", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3614.1145, 4662.073, 624.35645), (8.705881032967035, 0.0, -0.0), (0.95871246, 0.9323418, 0.9323418), "PWM_Quarry_1X1x1_C6_45", _folder)
if a: placed += 1
else: skipped += 1

# Batch 42: StaticMesh'PWM_Quarry_2x2x2_A' (3 instances)
_mesh_path = "/Game/Unshippable/Whitebox/Rocks/Meshes/PWM_Quarry_2x2x2_A"
_materials = ['/Game/Environments/ProcTexturing/M_Proc_Rock_Snow']
_folder = "Reconstruction/BD_BB_Outdoor_ExpeditionStart/Meshes"
a = spawn_static_mesh(_mesh_path, _materials, (3788.6716, 4429.692, 220.29816), (5.468139032203208, 40.275574936053154, -9.874908889876705), (3.713445, 2.312944, 2.5), "PWM_Quarry_2x2x2_A19", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5200.8335, 4203.1885, 518.82166), (0.0, -5.431091198498919, 0.0), (2.529378, 2.1603425, 1.8285118), "PWM_Quarry_2x2x2_A7_90", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (6047.1665, 4241.9653, 462.46606), (0.0, 0.0, -0.0), (1.9119467, 1.9119467, 1.9119467), "PWM_Quarry_2x2x2_A8_96", _folder)
if a: placed += 1
else: skipped += 1

# Batch 43: StaticMesh'PWM_Quarry_2x2x2_A' (4 instances)
_mesh_path = "/Game/Unshippable/Whitebox/Rocks/Meshes/PWM_Quarry_2x2x2_A"
_materials = ['/Game/Environments/ProcTexturing/M_Proc_Rock_Snow_v2']
_folder = "Reconstruction/BD_BB_Outdoor_ExpeditionStart/Meshes"
a = spawn_static_mesh(_mesh_path, _materials, (4625.5254, 4002.1995, 524.6851), (0.0, -174.63910476795914, 0.0), (2.7694404, 2.678737, 2.5306962), "PWM_Quarry_2x2x2_A_25", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4101.4326, 2879.1174, 705.2907), (5.008502931448731, 34.077604387088456, -9.105802794562212), (3.055792, 2.523359, 1.5656888), "PWM_Quarry_2x2x2_A32", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4050.6538, 4203.7896, 494.97052), (0.3345731707517923, -8.821593920794996, -9.20947236566715), (3.387797, 3.063711, 2.5), "PWM_Quarry_2x2x2_A4", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4576.4443, 4279.9756, 449.62988), (0.6725682957005225, -23.065854656780207, -11.52954164592622), (3.055792, 2.5233586, 2.989225), "PWM_Quarry_2x2x2_A5", _folder)
if a: placed += 1
else: skipped += 1

# Batch 44: StaticMesh'PWM_Quarry_2x2x2_A' (9 instances)
_mesh_path = "/Game/Unshippable/Whitebox/Rocks/Meshes/PWM_Quarry_2x2x2_A"
_materials = ['/Game/Environments/ProcTexturing/ProcMaterial_Quarry_Atlas_1']
_folder = "Reconstruction/BD_BB_Outdoor_ExpeditionStart/Meshes"
a = spawn_static_mesh(_mesh_path, _materials, (4023.7732, 1130.6808, 842.3924), (0.0, -43.114957858090804, 0.0), (2.1284642, 2.1284642, 2.1284642), "PWM_Quarry_2x2x2_A36_380", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2389.8123, 564.34033, 724.7551), (0.0, 0.0, -0.0), (2.1556537, 1.8563696, 1.5124835), "PWM_Quarry_2x2x2_A37_386", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2439.8123, 214.34033, 674.7551), (0.0, 0.0, -0.0), (2.155654, 1.85637, 1.512483), "PWM_Quarry_2x2x2_A53", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2989.8123, 214.34033, 674.7551), (0.0, 5.000023098478975, -0.0), (2.155654, 1.85637, 1.512483), "PWM_Quarry_2x2x2_A54", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3489.8123, 214.34033, 674.7551), (0.0, 0.0, -0.0), (2.155654, 1.85637, 1.512483), "PWM_Quarry_2x2x2_A55", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3989.8125, 214.34033, 674.7551), (0.0, 5.000023098478975, -0.0), (2.155654, 1.85637, 1.512483), "PWM_Quarry_2x2x2_A56", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1989.8123, 164.34033, 674.7551), (0.0, -179.9999590188648, 0.0), (2.155654, 1.85637, 1.512483), "PWM_Quarry_2x2x2_A57", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1489.8123, 164.34033, 674.7551), (0.0, -179.9999590188648, 0.0), (2.155654, 1.85637, 1.512483), "PWM_Quarry_2x2x2_A58", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4539.8125, 214.34033, 674.7551), (0.0, 5.000023098478975, -0.0), (2.155654, 1.85637, 1.512483), "PWM_Quarry_2x2x2_A59", _folder)
if a: placed += 1
else: skipped += 1

# Batch 45: StaticMesh'PWM_Quarry_2x2x2_A' (28 instances)
_mesh_path = "/Game/Unshippable/Whitebox/Rocks/Meshes/PWM_Quarry_2x2x2_A"
_materials = ['/Game/Environments/ProcTexturing/ProcMaterial_Quarry_Atlas_A_Snow_v2']
_folder = "Reconstruction/BD_BB_Outdoor_ExpeditionStart/Meshes"
a = spawn_static_mesh(_mesh_path, _materials, (3951.9553, 5853.5474, 164.88652), (10.848368235107557, 99.64257519215083, 16.33343513079642), (1.137574, 1.382231, 2.9543881), "PWM_Quarry_2x2x2_A11", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1093.1001, 4138.667, 687.5088), (-0.9172972494648534, -176.38723416691133, 14.222318564152342), (2.5071492, 2.4746127, 2.194766), "PWM_Quarry_2x2x2_A13", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (563.60443, 5889.0396, 279.09198), (8.746691978852025, 159.3308919482764, -173.7241748855789), (2.081309, 1.382231, 3.92892), "PWM_Quarry_2x2x2_A14", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (6288.605, 5514.0503, 276.81906), (-2.441223332646401, -170.97293793026023, 14.337790064973898), (1.2666864, 2.1956732, 3.9870825), "PWM_Quarry_2x2x2_A15", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (723.3453, 4174.849, 645.47266), (-0.2138061064636011, -178.9864618049828, 23.11514567766709), (2.649453, 2.5873957, 2.4921002), "PWM_Quarry_2x2x2_A16_206", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2058.3936, 4581.871, 479.21176), (-0.83813474647005, -26.136781574057423, -5.749115506049872), (3.065495, 1.5050501, 1.5050501), "PWM_Quarry_2x2x2_A17_218", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1737.176, 4712.008, 497.437), (0.0, -40.14141713306089, 0.0), (2.1021488, 1.50505, 1.50505), "PWM_Quarry_2x2x2_A18", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4848.5723, 4520.303, 401.2311), (6.76714642119846, 173.28768830381, 7.603688482962382), (3.2146838, 1.6827146, 2.5751467), "PWM_Quarry_2x2x2_A20_9", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3578.7383, 4492.1216, 375.7815), (-4.94052079057478, -138.87593165999377, 5.467286440815435), (2.0894365, 1.6202482, 1.6202482), "PWM_Quarry_2x2x2_A22_27", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (6105.108, 5603.4795, 400.07193), (-5.633361689058169, -23.399259649813477, -12.78173859065111), (1.1545887, 1.1545887, 1.6349727), "PWM_Quarry_2x2x2_A24_52", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3453.3638, 4566.0815, 609.867), (-2.5007322579488522, 61.397933559960755, -3.307067432320245), (2.2266953, 1.4657415, 1.2055333), "PWM_Quarry_2x2x2_A25", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (317.55536, 4983.0957, 642.1622), (-4.145414843278924, -28.72118916273808, -39.56853887819528), (1.1576236, 1.8203921, 2.985583), "PWM_Quarry_2x2x2_A26_58", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3694.8347, 4132.02, 447.10138), (-0.038207945087224304, -135.4085453891404, 3.536409612520447), (2.4533026, 2.312944, 2.5), "PWM_Quarry_2x2x2_A3", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3229.6912, 5435.347, 427.40408), (-2.8251040736521382, -149.90503545757517, -179.472284188742), (1.0, 1.0, 1.0), "PWM_Quarry_2x2x2_A30", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4579.9175, 3911.772, 826.0389), (-2.8160402332098515, -50.06546665119566, -1.4984743327102843), (1.347558, 2.064589, 1.1808143), "PWM_Quarry_2x2x2_A33_180", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3631.963, 4002.9243, 419.93762), (0.807116506315716, 42.192292278235364, -12.93115182409901), (3.055792, 2.523359, 2.989225), "PWM_Quarry_2x2x2_A34", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2150.8809, 4109.976, 918.3264), (-0.7907106461736804, -66.92249385796389, 3.448967018299163), (0.65932184, 0.65932184, 0.65932184), "PWM_Quarry_2x2x2_A35_330", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3474.4902, 3782.2874, 665.8757), (-0.3104248271442536, -81.44903126700811, 4.9904856957680765), (1.4254949, 1.2483021, 1.1694925), "PWM_Quarry_2x2x2_A38_425", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2856.7964, 3559.3713, 692.4604), (-0.5380249436752846, -102.93334688234965, -0.7113647272067994), (1.4810945, 1.0, 1.0), "PWM_Quarry_2x2x2_A39_434", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3894.8108, 2897.8586, 807.87854), (19.940187463454986, 33.62565638422893, -5.29943867506953), (1.7262847, 1.4198695, 1.4198695), "PWM_Quarry_2x2x2_A41_103", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1184.6963, 4558.4727, 870.0), (0.0, 5.000068801434048, -0.0), (0.64638734, 0.64638734, 0.64638734), "PWM_Quarry_2x2x2_A43_181", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (995.41925, 4541.9136, 870.0), (0.0, 179.99995901885745, -0.0), (0.646387, 0.646387, 0.646387), "PWM_Quarry_2x2x2_A44", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (820.41925, 4596.9136, 685.0), (0.0, 179.99995901885745, -0.0), (0.646387, 0.56825334, 0.646387), "PWM_Quarry_2x2x2_A45", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5860.6055, 4704.6235, 366.3307), (0.0, 0.0, -0.0), (1.5468488, 1.3544289, 0.7452428), "PWM_Quarry_2x2x2_A46_33", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2462.347, 4399.8394, 489.83588), (1.01613487584579, -33.96453698483917, -0.2750244187306158), (2.2347069, 1.50505, 1.50505), "PWM_Quarry_2x2x2_A48", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4929.6475, 4087.0273, 830.2467), (-0.5178528020432313, -33.96792152435558, 0.3254492496614956), (1.612896, 1.5412855, 1.3660756), "PWM_Quarry_2x2x2_A52_121", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1578.8779, 4032.5364, 655.94165), (2.061979118379909, -0.32824702818870016, -16.069579767006378), (2.205141, 1.5076607, 1.5076607), "PWM_Quarry_2x2x2_A6_73", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5972.634, 5615.3945, 450.505), (12.447432094312473, 78.33541688595506, -3.3411257734850652), (0.84195614, 1.5943393, 3.7633672), "PWM_Quarry_2x2x5_A12_2", _folder)
if a: placed += 1
else: skipped += 1

# Batch 46: StaticMesh'PWM_Quarry_2x2x5_A' (16 instances)
_mesh_path = "/Game/Unshippable/Whitebox/Rocks/Meshes/PWM_Quarry_2x2x5_A"
_materials = ['/Game/Environments/ProcTexturing/ProcMaterial_Quarry_Atlas_2']
_folder = "Reconstruction/BD_BB_Outdoor_ExpeditionStart/Meshes"
a = spawn_static_mesh(_mesh_path, _materials, (2296.3726, 1015.9733, 1168.977), (-4.194091421384101, -91.39562983029207, 2.4865460190836672), (2.7145457, 2.7145457, 2.7145457), "PWM_Quarry_2x2x5_A17_352", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2142.5774, 624.38324, 1143.654), (-2.6067505118076637, -2.960143967876769, -5.881622320319022), (2.714546, 2.8834696, 2.714546), "PWM_Quarry_2x2x5_A18", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4350.86, 552.4071, 1048.1146), (-2.6067506844063715, -2.9601440194587108, -6.801574706589296), (3.0715444, 3.0715444, 3.0715444), "PWM_Quarry_2x2x5_A19", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4376.133, 994.6384, 1100.8905), (5.185297502346667, 165.18108518699975, 6.122417724705763), (3.071544, 3.071544, 3.071544), "PWM_Quarry_2x2x5_A20", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4359.6743, 628.00696, 2025.1415), (3.285270980386756, 151.4831190779646, 3.163487272030538), (3.071544, 3.071544, 3.071544), "PWM_Quarry_2x2x5_A21_362", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2336.1946, 484.00943, 2348.2068), (-2.197357144688317, 2.5670472165651343, -4.352294546369244), (2.714546, 2.714546, 2.714546), "PWM_Quarry_2x2x5_A22", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1820.8771, 242.58673, 1116.3503), (-5.875213616336626, -93.22738445658675, -2.379547489820863), (2.714546, 2.88347, 2.714546), "PWM_Quarry_2x2x5_A25", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1320.8771, 242.58673, 1116.3503), (-5.875214164955271, 81.77284229001943, -2.3795476728610367), (2.714546, 2.88347, 2.714546), "PWM_Quarry_2x2x5_A26", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (820.8771, 242.58673, 1116.3503), (-5.875212517554428, -168.2273517187386, -2.3795469644684437), (2.714546, 2.88347, 2.714546), "PWM_Quarry_2x2x5_A27", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5320.877, 242.58673, 1116.3503), (-5.875214164955271, 81.77284229001943, -2.3795476728610367), (2.714546, 2.88347, 2.714546), "PWM_Quarry_2x2x5_A28", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4820.877, 242.58673, 1116.3503), (-5.875213784363431, -123.22734282425489, -2.3795472435343545), (2.714546, 2.88347, 2.714546), "PWM_Quarry_2x2x5_A29", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5320.877, 242.58673, 2216.3503), (-5.875214164955271, 81.77284229001943, -2.3795476728610367), (2.714546, 2.88347, 2.714546), "PWM_Quarry_2x2x5_A30", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4820.877, 242.58673, 2216.3503), (-5.875213784363431, -123.22734282425489, -2.3795472435343545), (2.714546, 2.88347, 2.714546), "PWM_Quarry_2x2x5_A31", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1820.8771, 242.58673, 2316.3503), (-5.875213616336626, -93.22738445658675, -2.379547489820863), (2.714546, 2.88347, 2.714546), "PWM_Quarry_2x2x5_A32", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1320.8771, 242.58673, 2316.3503), (-5.875214164955271, 81.77284229001943, -2.3795476728610367), (2.714546, 2.88347, 2.714546), "PWM_Quarry_2x2x5_A33", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (820.8771, 242.58673, 2316.3503), (-5.875212517554428, -168.2273517187386, -2.3795469644684437), (2.714546, 2.88347, 2.714546), "PWM_Quarry_2x2x5_A34", _folder)
if a: placed += 1
else: skipped += 1

# Batch 47: StaticMesh'PWM_Quarry_2x2x5_A' (7 instances)
_mesh_path = "/Game/Unshippable/Whitebox/Rocks/Meshes/PWM_Quarry_2x2x5_A"
_materials = ['/Game/Environments/ProcTexturing/ProcMaterial_Quarry_Atlas_2_Snow_v2']
_folder = "Reconstruction/BD_BB_Outdoor_ExpeditionStart/Meshes"
a = spawn_static_mesh(_mesh_path, _materials, (5684.954, 3605.4165, 1786.268), (24.535625426063888, 97.90361446756796, 0.5460553139833663), (2.860024, 2.860024, 2.860024), "PWM_Quarry_2x2x5_A13_82", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4843.7363, 3695.033, 1229.7711), (25.54274693974723, 82.05775648687492, -5.901612821924664), (2.860024, 3.5401952, 2.860024), "PWM_Quarry_2x2x5_A14", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4208.5522, 3074.188, 1061.887), (24.411499694147174, 118.08752534776329, 9.737619441305663), (2.860024, 2.860024, 2.860024), "PWM_Quarry_2x2x5_A15", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1639.891, 4260.8955, 1088.3839), (27.257324961388804, 59.98590148342623, -17.82586902112438), (2.860024, 2.860024, 3.0261862), "PWM_Quarry_2x2x5_A16", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4031.865, 2867.6338, 1287.6401), (12.792574941579495, 108.35318612606103, 2.473657428390148), (1.6398765, 1.6398765, 1.6398765), "PWM_Quarry_2x2x5_A23_437", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (506.2886, 5750.6406, 558.79456), (4.547074230110683, -2.0538937586122246, -24.340237035575147), (1.5154994, 1.473052, 1.1323321), "PWM_Quarry_2x2x5_A24_109", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3979.3098, 5688.1963, 196.30043), (-5.9747932969797795, 89.58402298173007, 18.508181083351538), (1.8023204, 1.6336967, 1.6563659), "PWM_Quarry_4x3x10_C8_141", _folder)
if a: placed += 1
else: skipped += 1

# Batch 48: StaticMesh'PWM_Quarry_2x2x5_A' (2 instances)
_mesh_path = "/Game/Unshippable/Whitebox/Rocks/Meshes/PWM_Quarry_2x2x5_A"
_materials = ['/Game/Environments/ProcTexturing/ProcMaterial_Quarry_Atlas_A_Snow_v2']
_folder = "Reconstruction/BD_BB_Outdoor_ExpeditionStart/Meshes"
a = spawn_static_mesh(_mesh_path, _materials, (4691.8184, 5680.3403, 407.6829), (-6.93469277774479, -97.73846129226071, -15.727812996600683), (1.145499, 1.2710975, 1.0), "PWM_Quarry_2x2x2_A10", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3701.9973, 4956.5303, 471.3605), (0.9257296384106455, 10.80190552691623, -9.184967595977223), (1.7434977, 1.278351, 1.3993579), "PWM_Quarry_2x2x2_A28_64", _folder)
if a: placed += 1
else: skipped += 1

# Batch 49: StaticMesh'PWM_Quarry_2x2x5_B' (1 instances)
_mesh_path = "/Game/Unshippable/Whitebox/Rocks/Meshes/PWM_Quarry_2x2x5_B"
_materials = ['/Game/Environments/ProcTexturing/ProcMaterial_Quarry_Atlas_A_Snow_v2']
_folder = "Reconstruction/BD_BB_Outdoor_ExpeditionStart/Meshes"
a = spawn_static_mesh(_mesh_path, _materials, (3939.1038, 5017.7524, 493.36862), (1.871056332956317, -0.1755370983998106, -13.42547601690114), (1.0067528, 0.7529906, 1.1201081), "PWM_Quarry_4x8x15_41", _folder)
if a: placed += 1
else: skipped += 1

# Batch 50: StaticMesh'PWM_Quarry_3x3x2' (2 instances)
_mesh_path = "/Game/Unshippable/Whitebox/Rocks/Meshes/PWM_Quarry_3x3x2"
_materials = ['/Game/Environments/ProcTexturing/ProcMaterial_Quarry_Atlas_A']
_folder = "Reconstruction/BD_BB_Outdoor_ExpeditionStart/Meshes"
a = spawn_static_mesh(_mesh_path, _materials, (4021.722, 551.11096, 844.14197), (0.0, -104.62297560177053, 0.0), (2.0754116, 2.7156835, 1.8676589), "PWM_Quarry_3x3x16_374", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2474.9844, 1070.0762, 811.3972), (0.0, -73.82342720558886, 0.0), (2.460775, 2.460775, 2.460775), "PWM_Quarry_3x3x17_383", _folder)
if a: placed += 1
else: skipped += 1

# Batch 51: StaticMesh'PWM_Quarry_3x3x2' (10 instances)
_mesh_path = "/Game/Unshippable/Whitebox/Rocks/Meshes/PWM_Quarry_3x3x2"
_materials = ['/Game/Environments/ProcTexturing/ProcMaterial_Quarry_Atlas_A_Snow_v2']
_folder = "Reconstruction/BD_BB_Outdoor_ExpeditionStart/Meshes"
a = spawn_static_mesh(_mesh_path, _materials, (5760.259, 4377.9976, 397.90805), (-4.733581411485187, 20.8143125983116, -5.332733172366898), (2.001817, 2.001817, 1.7638147), "PWM_Quarry_3x3x11", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4450.3643, 4636.767, 548.34357), (-15.593901870356103, 3.188662476829466, -19.92566180100518), (2.405674, 1.643059, 3.3869505), "PWM_Quarry_3x3x13", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4516.053, 3463.231, 796.39655), (-1.2809950907645955e-07, 91.32055077677578, -6.7215878728953635), (3.0461197, 3.5892346, 1.758478), "PWM_Quarry_3x3x14_177", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4827.358, 3470.4072, 775.9454), (-1.2809950907645955e-07, 91.32055077677578, -6.7215878728953635), (3.04612, 3.589235, 1.758478), "PWM_Quarry_3x3x15", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2798.109, 3856.8486, 701.12976), (-5.081389990767622, -57.90325116112688, -7.472930202131755), (2.617146, 1.4188392, 1.72376), "PWM_Quarry_3x3x18", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3422.1228, 3546.1045, 730.93115), (-2.1312867168363994, -93.51632791206644, -0.27105703120729824), (1.4945786, 1.0, 1.0), "PWM_Quarry_3x3x19_428", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2375.0742, 3788.0205, 586.1448), (-5.845397660283445, 8.132298232693946, -12.353333215818251), (2.0, 2.0, 3.0814595), "PWM_Quarry_3x3x2_53", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2333.6265, 4079.9858, 624.0137), (-11.02060009407028, 3.3042407852379614, -16.412263022327778), (2.4307632, 2.4307632, 3.0936503), "PWM_Quarry_3x3x3_70", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1828.9916, 4200.7915, 673.1195), (-11.262359622672586, 1.3933909338939872, -18.728423321050784), (2.7301247, 2.7301247, 2.7301247), "PWM_Quarry_3x3x4_215", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4571.0894, 4510.399, 371.85583), (-4.647583219612703, 5.214620817521355, -13.376128137851056), (2.1140318, 2.1140318, 2.1140318), "PWM_Quarry_3x3x5_6", _folder)
if a: placed += 1
else: skipped += 1

# Batch 52: StaticMesh'PWM_Quarry_4x3x10_A' (1 instances)
_mesh_path = "/Game/Unshippable/Whitebox/Rocks/Meshes/PWM_Quarry_4x3x10_A"
_materials = ['/Game/Environments/ProcTexturing/ProcMaterial_Quarry_Atlas_A']
_folder = "Reconstruction/BD_BB_Outdoor_ExpeditionStart/Meshes"
a = spawn_static_mesh(_mesh_path, _materials, (3869.6309, 1968.8055, 1352.5494), (14.662155243411274, 77.82697439039562, -4.926330432977054), (1.3952471, 1.3952471, 1.3952471), "PWM_Quarry_4x3x10_A45_35", _folder)
if a: placed += 1
else: skipped += 1

# Batch 53: StaticMesh'PWM_Quarry_4x3x10_A' (8 instances)
_mesh_path = "/Game/Unshippable/Whitebox/Rocks/Meshes/PWM_Quarry_4x3x10_A"
_materials = ['/Game/Environments/ProcTexturing/ProcMaterial_Quarry_Atlas_A_Snow_v2']
_folder = "Reconstruction/BD_BB_Outdoor_ExpeditionStart/Meshes"
a = spawn_static_mesh(_mesh_path, _materials, (469.13974, 3695.3142, 1131.595), (-24.032864995213192, -142.8813204503829, 24.08527164279069), (2.4167666, 3.0, 2.4410584), "PWM_Quarry_4x3x10_A13", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5462.4175, 6045.3486, 211.14632), (-12.475005712276975, -12.8204335039812, -24.488126907027763), (1.0, 1.0, 0.92022663), "PWM_Quarry_4x3x10_A16_117", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5875.3896, 5988.8633, 388.40253), (-11.01150606629244, 0.4312491902464293, -27.247743661828043), (1.0, 1.0, 1.0), "PWM_Quarry_4x3x10_A17_129", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1216.3303, 3049.3508, 1499.9958), (-18.927795988514585, -157.01406999250466, 23.72783086421116), (3.0, 3.0, 3.2078264), "PWM_Quarry_4x3x10_A3", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5185.979, 2574.7266, 2334.079), (-19.17361524893036, -127.51363781261776, 5.957419524375955), (3.0, 4.1388416, 1.4342686), "PWM_Quarry_4x3x10_A4", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (8899.959, 9507.342, -10738.015), (-15.055145983957333, -25.977629639450207, 4.129161115941186), (3.1263134, 3.1263134, 3.1263134), "PWM_Quarry_4x3x10_A44_158", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1484.8114, 2456.2563, 2809.8806), (20.47648814990923, 121.62294911298962, 1.5466500601677977), (1.0, 1.3916473, 0.53855383), "PWM_Quarry_4x3x10_A46_75", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2966.5315, 5678.1304, 595.9877), (7.12817742578421, 0.49235187325045926, -20.446439894336226), (0.8100915, 0.6158321, 0.6158321), "PWM_Quarry_4x3x10_A52_82", _folder)
if a: placed += 1
else: skipped += 1

# Batch 54: StaticMesh'PWM_Quarry_4x3x10_C' (3 instances)
_mesh_path = "/Game/Unshippable/Whitebox/Rocks/Meshes/PWM_Quarry_4x3x10_C"
_materials = ['/Game/Environments/ProcTexturing/ProcMaterial_Quarry_Atlas_A']
_folder = "Reconstruction/BD_BB_Outdoor_ExpeditionStart/Meshes"
a = spawn_static_mesh(_mesh_path, _materials, (2495.8757, 1909.7389, 1300.1038), (-16.960389863818758, -87.72581023338648, -3.9440308140701426), (2.2984023, 1.5362343, 1.6294023), "PWM_Quarry_4x3x10_C26_29", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2115.1887, 829.5717, 2366.3635), (0.0, 0.0, -14.430448499997933), (1.3319893, 1.3319893, 1.3319893), "PWM_Quarry_4x3x10_C35_365", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3960.0, 551.55286, 2892.9487), (0.0, 0.0, -4.395812859084391), (3.0047438, 2.0418494, 0.2925844), "PWM_Quarry_4x3x10_C36_153", _folder)
if a: placed += 1
else: skipped += 1

# Batch 55: StaticMesh'PWM_Quarry_4x3x10_C' (17 instances)
_mesh_path = "/Game/Unshippable/Whitebox/Rocks/Meshes/PWM_Quarry_4x3x10_C"
_materials = ['/Game/Environments/ProcTexturing/ProcMaterial_Quarry_Atlas_A_Snow_v2']
_folder = "Reconstruction/BD_BB_Outdoor_ExpeditionStart/Meshes"
a = spawn_static_mesh(_mesh_path, _materials, (3855.9106, 2316.4546, 2319.2134), (11.363452860970671, 103.70742348852632, 3.9154951768522106), (1.200053, 1.200053, 1.200053), "PWM_Quarry_4x3x10_C_11", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5933.3228, 5798.695, 305.9441), (-3.311889480939335, 1.0050846706197367, -25.820706566160784), (1.6152617, 1.2624459, 1.218242), "PWM_Quarry_4x3x10_C19_173", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5979.439, 4038.775, 825.624), (-23.84444954886109, -74.06498646717245, -8.263795536483654), (2.0525262, 2.0525262, 2.0525262), "PWM_Quarry_4x3x10_C20_176", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2910.661, 5914.818, 299.6513), (-0.4051819017237151, -1.4852904707836065, -26.01217683213091), (1.587122, 0.9872954, 0.98813444), "PWM_Quarry_4x3x10_C21", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (644.1612, 3234.5317, 2186.519), (1.755420398367641, 11.549674503446086, -31.08734357440438), (2.138889, 2.8537037, 1.1485752), "PWM_Quarry_4x3x10_C22_193", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1840.4227, 2556.5408, 2851.0308), (8.54103952333685, 45.23314148992887, -19.896207569548366), (1.3304735, 1.2292112, 0.36709374), "PWM_Quarry_4x3x10_C27_69", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5157.954, 3738.1318, 1344.6699), (-3.083099223029147, 1.6365515591621635, -31.111266423356838), (2.6562848, 1.1962551, 1.8795217), "PWM_Quarry_4x3x10_C28_79", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (195.45789, 2731.385, 2152.3523), (18.87134186197283, 104.30864969930332, 4.5046160574108685), (1.5, 1.5, 2.0), "PWM_Quarry_4x3x10_C3", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4215.149, 2637.925, 2226.7144), (-1.8955686646379806, -0.6238098987670629, -14.481292250275258), (1.200053, 1.200053, 1.200053), "PWM_Quarry_4x3x10_C30", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2198.1882, 2723.9248, 2108.6885), (-14.719880429372441, -124.32547405870008, 9.282726912260905), (1.075236, 1.5213708, 1.4244896), "PWM_Quarry_4x3x10_C31", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1377.4552, 4056.899, 1035.1753), (6.197741489537308, 15.287652973624011, -35.95123405622599), (1.2555556, 1.5040272, 1.42449), "PWM_Quarry_4x3x10_C32", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (549.43445, 3484.303, 2373.35), (-18.703094039714117, -37.72049009463422, -23.932704211856475), (1.075236, 1.200053, 1.2811949), "PWM_Quarry_4x3x10_C33", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2888.4478, 2316.4546, 2678.8818), (-5.270629384686144, 177.2407874261335, 15.179110090353719), (1.200053, 0.75454193, 1.0007745), "PWM_Quarry_4x3x10_C37", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1126.2803, 3609.7246, 2083.9365), (6.197741654784861, 15.28756590463639, -34.65576095276064), (1.075236, 1.200053, 0.97702396), "PWM_Quarry_4x3x10_C38", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1321.7943, 4037.6934, 1436.5597), (-21.633847780512603, -36.068263956591544, -28.170343699288846), (0.7278093, 0.85262626, 0.7390113), "PWM_Quarry_4x3x10_C39", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5215.429, 2387.5222, 2128.9348), (22.3800754935001, 103.71071608814569, 179.33744037098478), (1.5, 2.5, 2.0), "PWM_Quarry_4x3x10_C4", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4080.4226, 5979.129, 231.87488), (-4.150329301546104, 3.1853161535741146, -17.170562398564716), (1.0, 0.7406569, 0.74372834), "PWM_Quarry_4x3x10_C7_135", _folder)
if a: placed += 1
else: skipped += 1

# Batch 56: StaticMesh'PWM_Quarry_4x4x4_A' (1 instances)
_mesh_path = "/Game/Unshippable/Whitebox/Rocks/Meshes/PWM_Quarry_4x4x4_A"
_materials = ['/Game/Environments/ProcTexturing/ProcMaterial_Quarry_Atlas_2']
_folder = "Reconstruction/BD_BB_Outdoor_ExpeditionStart/Meshes"
a = spawn_static_mesh(_mesh_path, _materials, (2509.0886, 1488.0398, 1222.7288), (-8.630402780544957, -97.08340493483657, 4.641788185266922), (1.422303, 1.1051624, 3.4424849), "PWM_Quarry_4x4x4_A16_32", _folder)
if a: placed += 1
else: skipped += 1

# Batch 57: StaticMesh'PWM_Quarry_4x4x4_A' (18 instances)
_mesh_path = "/Game/Unshippable/Whitebox/Rocks/Meshes/PWM_Quarry_4x4x4_A"
_materials = ['/Game/Environments/ProcTexturing/ProcMaterial_Quarry_Atlas_2_Snow_v2']
_folder = "Reconstruction/BD_BB_Outdoor_ExpeditionStart/Meshes"
a = spawn_static_mesh(_mesh_path, _materials, (1762.9038, 3760.2654, 532.3561), (0.07480419144235628, 174.62155301470997, 13.580542023825654), (2.1047428, 1.4282678, 1.0), "PWM_Quarry_4x4x4_A12_56", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1999.0521, 4083.9482, 645.6949), (15.93341668638077, 90.44605718202767, -2.878083108333559), (1.3430634, 1.3414402, 0.84484184), "PWM_Quarry_4x4x4_A14_76", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2144.2356, 2605.4504, 1401.4266), (-16.603547049912265, -122.58149416020119, 13.70772249924497), (1.566216, 1.566216, 3.488274), "PWM_Quarry_4x4x4_A2", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1456.3671, 4559.5063, 521.25256), (2.1951830575906297, -15.75811526065656, 4.307219492182512), (1.343063, 0.9691441, 0.652923), "PWM_Quarry_4x4x4_A21", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2060.233, 2330.4834, 2641.4888), (-16.603514015699464, -122.58156852651815, 9.367026666811219), (1.1351519, 1.1351519, 1.959182), "PWM_Quarry_4x4x4_A22", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1617.143, 2964.0742, 1684.0591), (0.0, 0.0, -21.53598258660273), (1.0, 1.2390121, 1.0), "PWM_Quarry_4x4x4_A23_72", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3967.3613, 4626.46, 501.28076), (0.34196294819290374, 0.04766489913121608, -7.9718334113359575), (1.2392584, 1.5323159, 1.496096), "PWM_Quarry_4x4x4_A24_3", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5290.117, 4155.5493, 342.12146), (5.158913450211512, 143.37295153956504, 4.00266428034989), (2.5, 2.0, 2.229333), "PWM_Quarry_4x4x4_A25", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1195.0, 4575.0, 720.0), (0.0, 0.0, -0.0), (0.43265197, 0.36280572, 0.46278334), "PWM_Quarry_4x4x4_A26_178", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (820.0, 4565.042, 825.0), (0.0, 0.0, -0.0), (0.432652, 0.362806, 0.462783), "PWM_Quarry_4x4x4_A27", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3583.93, 5677.764, 142.4029), (12.88993436843887, 14.057688324532117, 7.313154893094139), (1.6012641, 0.7663579, 1.7865882), "PWM_Quarry_4x4x4_A28_35", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (6137.4077, 4971.9844, 374.46646), (-9.116699808328578, -115.27581362240426, -0.9933167542042968), (0.9664407, 0.5192343, 0.5192343), "PWM_Quarry_4x4x4_A29_47", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4957.9536, 2581.856, 1290.9814), (11.847703074839986, 94.0162994950266, -1.4372243177196844), (1.566216, 1.566216, 3.488274), "PWM_Quarry_4x4x4_A3", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2866.3013, 1980.4071, 2449.592), (-10.319396994783217, -121.13316743165343, 6.749686347465844), (1.5908855, 1.566216, 2.1386437), "PWM_Quarry_4x4x4_A4", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1261.8931, 2459.854, 1401.7614), (0.0, 0.0, -15.000058335092751), (1.566216, 1.566216, 3.488274), "PWM_Quarry_4x4x4_A5", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5955.568, 4253.312, 276.77518), (-1.2030024992523238, -158.0158005817287, 15.78778362347641), (2.5, 2.0, 2.2293334), "PWM_Quarry_4x4x4_A6_88", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1099.6119, 2408.4856, 2429.1301), (-4.668945100909056, -146.28418535097765, 10.995035147233246), (1.566216, 1.566216, 2.915755), "PWM_Quarry_4x4x4_A8", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1575.8701, 5871.0234, 425.9843), (4.137938841830222, 164.40998835041557, 107.47417465195942), (1.2914478, 0.5769739, 1.0), "PWM_Quarry_4x5x50", _folder)
if a: placed += 1
else: skipped += 1

# Batch 58: StaticMesh'PWM_Quarry_4x5x10' (1 instances)
_mesh_path = "/Game/Unshippable/Whitebox/Rocks/Meshes/PWM_Quarry_4x5x10"
_materials = ['/Game/Environments/ProcTexturing/ProcMaterial_Quarry_Atlas_2_Snow_v2']
_folder = "Reconstruction/BD_BB_Outdoor_ExpeditionStart/Meshes"
a = spawn_static_mesh(_mesh_path, _materials, (6209.278, 4575.1665, 186.84238), (12.920321215986121, 89.94475031303203, 4.481869785980599), (1.5108567, 0.94279873, 0.925974), "PWM_Quarry_8x8x8_A57", _folder)
if a: placed += 1
else: skipped += 1

# Batch 59: StaticMesh'PWM_Quarry_4x5x10' (34 instances)
_mesh_path = "/Game/Unshippable/Whitebox/Rocks/Meshes/PWM_Quarry_4x5x10"
_materials = ['/Game/Environments/ProcTexturing/ProcMaterial_Quarry_Atlas_A_Snow_v2']
_folder = "Reconstruction/BD_BB_Outdoor_ExpeditionStart/Meshes"
a = spawn_static_mesh(_mesh_path, _materials, (885.7115, 2387.954, 1600.4541), (14.62432832719521, 126.39853749535665, 2.2033461955955116), (2.5, 2.5, 2.5), "PWM_Quarry_4x3x10_A_108", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3322.5981, 5695.388, 587.8144), (24.593198508883127, 11.051089701266163, -1.2911980577096867), (1.0, 1.0, 0.7296998), "PWM_Quarry_4x3x10_C29_58", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3959.0, 2483.3179, 1194.8412), (4.2460342289077735, -0.422912627145408, -15.02996970328506), (1.4774582, 1.4774582, 1.8155315), "PWM_Quarry_4x5x10_2", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2393.8765, 2502.2644, 1366.1421), (3.035602223236258, -3.28991699255028, -15.330416364245393), (1.5937895, 1.7705697, 1.6086333), "PWM_Quarry_4x5x11", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2364.1082, 2002.5533, 2461.5232), (10.510042022044006, 89.08636163488926, -176.4682741036275), (3.1240811, 2.190891, 1.066485), "PWM_Quarry_4x5x12", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1773.5435, 2633.265, 1195.8195), (9.527058068248552, 25.270822824766896, -12.85992343928255), (1.477458, 1.477458, 1.815531), "PWM_Quarry_4x5x13", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3574.3745, 1939.213, 2466.8372), (18.256379767572994, 54.14471196366136, -7.338379417721973), (1.8199438, 1.9970309, 1.0523027), "PWM_Quarry_4x5x14", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1650.0, 2225.2988, 2374.9539), (0.0, 0.0, -15.87914988473164), (1.6580324, 1.6580324, 1.384783), "PWM_Quarry_4x5x15_79", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (409.47937, 2590.7737, 2304.703), (19.822684273542688, 119.32020909078196, -2.0681462991885025), (1.658032, 1.658032, 1.658032), "PWM_Quarry_4x5x16", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4526.423, 2580.7458, 1155.0682), (16.3227667482117, 30.380213885682068, -14.023867779420227), (1.819944, 1.997031, 1.535337), "PWM_Quarry_4x5x18", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3877.0437, 4265.7515, 377.88), (-81.84055994150128, 77.10462975355713, -51.331735874121385), (1.2580307, 1.2580307, 1.0297904), "PWM_Quarry_4x5x21_28", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (326.75317, 5590.2227, 374.66034), (25.488172480390464, 51.99588342644583, -15.332305276000618), (1.3934109, 1.0678025, 0.9507592), "PWM_Quarry_4x5x22_59", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5751.3013, 6070.044, 386.21173), (-2.2436218886507686, 12.505814502356055, -32.14581080355267), (1.0, 0.69617003, 0.80644464), "PWM_Quarry_4x5x23_114", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4694.4946, 5841.768, 377.56348), (30.87556050945018, -4.4263005449253, -8.92550858774588), (1.0, 0.5364918, 0.583533), "PWM_Quarry_4x5x24", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2804.7358, 5875.8486, 344.95798), (4.780413329183234, 6.881900738247864, -17.36706543674056), (1.0, 0.69617, 0.806445), "PWM_Quarry_4x5x25", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2328.303, 4205.094, 377.88), (-81.84041898541062, 10.6148801969075, -51.33149225311673), (1.258031, 1.258031, 1.02979), "PWM_Quarry_4x5x33", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (875.6124, 4581.7793, 377.88), (-81.84035931647426, 50.099511227977814, -51.331837491212525), (1.258031, 1.2010759, 1.02979), "PWM_Quarry_4x5x34", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3979.3105, 1571.3975, 1308.143), (7.976542788823527, 2.964437718707183, -19.91723750175247), (1.819944, 1.997031, 1.7415985), "PWM_Quarry_4x5x36", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3089.6738, 1250.0591, 2423.295), (-0.14483635103526835, 167.4801086215314, -162.9863450740718), (3.124081, 2.309771, 1.066485), "PWM_Quarry_4x5x37", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4414.5728, 2698.7349, 2270.2925), (-0.7647092356148812, -29.32924975017466, -13.546659976706596), (1.2265491, 1.2265491, 1.3113245), "PWM_Quarry_4x5x38_184", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4196.838, 1054.4109, 2299.374), (6.737633556960327, -2.0585326607133174, -16.26376159677358), (1.477458, 1.2376087, 1.1909907), "PWM_Quarry_4x5x39_359", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2922.7607, 500.7848, 2624.365), (-0.14483652103627714, 167.48010899689814, -173.02797139473253), (3.124081, 1.9420981, 1.066485), "PWM_Quarry_4x5x40", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5943.455, 4381.8164, 619.9754), (21.684669424005204, 45.21996298194234, -18.517425167308833), (1.4633964, 1.0, 1.4461027), "PWM_Quarry_4x5x41_12", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4367.864, 5643.0117, 339.9121), (-9.914824549420299, -166.0563737209475, -17.34899779512368), (0.6522181, 0.6522181, 0.6522181), "PWM_Quarry_4x5x42_44", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3038.4072, 5506.0225, 567.1422), (30.224331495238836, 0.9575631071402099, 6.620547322077591), (0.73605067, 0.73605067, 0.80268025), "PWM_Quarry_4x5x43_61", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2915.6165, 5398.918, 498.7964), (12.708788668559796, -102.28740099090338, -13.09020784672941), (1.0, 1.0, 1.0), "PWM_Quarry_4x5x44_64", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5970.0, 5588.6753, 536.6906), (0.0, 0.0, -15.446441414672657), (0.6234815, 0.68857795, 0.8078946), "PWM_Quarry_4x5x45_74", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (6174.829, 5333.0786, 530.2858), (16.932784361623877, 15.69058542924329, -10.982422312039066), (0.51213557, 0.51213557, 0.6437761), "PWM_Quarry_4x5x46_83", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (175.0, 5357.825, 229.00546), (0.0, 0.0, -23.75021340479526), (1.2710975, 1.557782, 1.2710975), "PWM_Quarry_4x5x48_92", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1830.0, 5935.8696, 163.10231), (0.0, 0.0, -18.157135413344772), (1.0, 1.0, 1.0), "PWM_Quarry_4x5x49_95", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5510.0, 4105.1675, 1006.5389), (0.0, 0.0, -34.75930680445678), (1.6581498, 1.0, 1.0), "PWM_Quarry_4x5x52_105", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4650.7363, 5854.08, 492.27518), (-27.114312532223117, -176.6922048982388, 5.337554432973999), (1.0, 0.72335345, 0.583533), "PWM_Quarry_4x5x53", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4563.127, 5548.0337, 423.2164), (24.116566960934435, -1.7681885482486346, 2.5820182365673223), (0.5558092, 0.5558092, 0.5558092), "PWM_Quarry_4x8x14_38", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (6205.399, 5020.748, 373.4735), (2.935597655812533, -8.280271035223704, -8.410370393320823), (0.79505616, 1.4123782, 0.45487666), "PWM_Quarry_8x8x8_A56", _folder)
if a: placed += 1
else: skipped += 1

# Batch 60: StaticMesh'PWM_Quarry_4x8x3' (1 instances)
_mesh_path = "/Game/Unshippable/Whitebox/Rocks/Meshes/PWM_Quarry_4x8x3"
_materials = ['/Game/Environments/ProcTexturing/ProcMaterial_Quarry_Atlas_A']
_folder = "Reconstruction/BD_BB_Outdoor_ExpeditionStart/Meshes"
a = spawn_static_mesh(_mesh_path, _materials, (4099.0366, 1136.6978, 752.36975), (0.0, 0.0, -87.90564052564292), (2.188838, 1.5085126, 1.5085126), "PWM_Quarry_4x8x7_377", _folder)
if a: placed += 1
else: skipped += 1

# Batch 61: StaticMesh'PWM_Quarry_4x8x3' (9 instances)
_mesh_path = "/Game/Unshippable/Whitebox/Rocks/Meshes/PWM_Quarry_4x8x3"
_materials = ['/Game/Environments/ProcTexturing/ProcMaterial_Quarry_Atlas_A_Snow_v2']
_folder = "Reconstruction/BD_BB_Outdoor_ExpeditionStart/Meshes"
a = spawn_static_mesh(_mesh_path, _materials, (252.29768, 5085.185, 688.6694), (35.152242993489025, 77.0424818721976, -14.29806849126643), (1.0, 1.0, 1.0), "PWM_Quarry_4x8x10_144", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (347.6061, 4357.8633, 1076.2589), (-5.864471104540993, 5.266916205817797, -33.4705825138112), (1.3397233, 1.3397233, 1.5205172), "PWM_Quarry_4x8x11_147", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5286.079, 5798.466, 436.7152), (25.285711229736787, -173.09010875107978, 15.572251005976751), (1.0, 1.0, 1.0), "PWM_Quarry_4x8x13_24", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5278.018, 5798.0044, 67.60837), (-8.511292295768182, 145.08541714667888, 15.451561702920555), (1.217997, 1.217997, 1.217997), "PWM_Quarry_4x8x16", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5868.995, 5507.924, 504.92523), (-15.797943102982822, -0.4729004933542318, 8.4485835090478), (0.8198518, 0.79032195, 0.79032195), "PWM_Quarry_4x8x17_71", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5656.079, 5718.466, 576.7152), (18.2102758534896, -173.4241603362109, 14.672343569517817), (1.0, 1.0, 1.0), "PWM_Quarry_4x8x18", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (960.77216, 3268.9465, 2247.1677), (3.294473202854347, -0.7259521958354981, -24.272520852700136), (2.6017332, 2.7395177, 1.7657081), "PWM_Quarry_4x8x3_62", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5947.4873, 3407.9038, 732.1577), (-7.75308117086841, -8.339110249530707, -20.994171881461636), (2.4965973, 2.4965973, 2.4965973), "PWM_Quarry_4x8x4_107", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1660.6655, 4711.949, 803.7411), (13.58855112329627, 29.81447960248548, -23.89361310199958), (0.5169811, 0.5169811, 0.64696777), "PWM_Quarry_4x8x9_126", _folder)
if a: placed += 1
else: skipped += 1

# Batch 62: StaticMesh'PWM_Quarry_5x4x10' (1 instances)
_mesh_path = "/Game/Unshippable/Whitebox/Rocks/Meshes/PWM_Quarry_5x4x10"
_materials = ['/Game/Environments/ProcTexturing/ProcMaterial_Quarry_Atlas_A']
_folder = "Reconstruction/BD_BB_Outdoor_ExpeditionStart/Meshes"
a = spawn_static_mesh(_mesh_path, _materials, (3185.2034, 2267.0796, 2411.277), (-0.07513426803574969, -1.1798399377729814, -3.642089436391925), (1.319024, 1.5505722, 0.5006938), "PWM_Quarry_5x4x16_395", _folder)
if a: placed += 1
else: skipped += 1

# Batch 63: StaticMesh'PWM_Quarry_5x4x10' (20 instances)
_mesh_path = "/Game/Unshippable/Whitebox/Rocks/Meshes/PWM_Quarry_5x4x10"
_materials = ['/Game/Environments/ProcTexturing/ProcMaterial_Quarry_Atlas_A_Snow_v2']
_folder = "Reconstruction/BD_BB_Outdoor_ExpeditionStart/Meshes"
a = spawn_static_mesh(_mesh_path, _materials, (5110.1685, 5916.2666, 120.51306), (-25.987089086072437, -165.073187244262, -0.8942870233382872), (1.35027, 1.332414, 0.9343798), "PWM_Quarry_2x2x2_A9_121", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4555.801, 5714.4204, 338.29105), (-4.369293989974578, 100.86609706202046, 17.05458480337881), (1.0002316, 1.0002316, 1.0002316), "PWM_Quarry_4x8x12_18", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3194.3872, 5582.6562, 567.16376), (-13.280515786754739, -167.15927589896208, 4.616310301930642), (1.0, 1.4677902, 1.0), "PWM_Quarry_4x8x6_55", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5583.63, 3585.4553, 789.243), (15.809470515999422, 58.26064468767753, -14.197206497392077), (1.492741, 1.8229958, 1.8229958), "PWM_Quarry_5x4x10_104", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4362.5557, 5882.643, 253.75554), (2.4440871566487594e-09, -1.0316771593613612, -15.169829370242288), (0.9102581, 0.73035634, 0.6570435), "PWM_Quarry_5x4x11_126", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2661.7217, 5712.4854, 506.40244), (13.718291841300704, -13.958615713407854, -2.373657176177669), (1.0, 1.0, 1.1581498), "PWM_Quarry_5x4x13_189", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1015.91284, 5957.5117, 157.39668), (10.350458551439171, -177.37146365122797, -167.0815184357813), (1.4533684, 1.1486279, 0.95974785), "PWM_Quarry_5x4x14", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2606.941, 3810.298, 605.5074), (-0.43826277252090406, 7.774008755471114, -86.79369353749976), (1.0, 1.0, 0.72576034), "PWM_Quarry_5x4x15_209", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3663.6997, 4369.594, 618.1285), (-1.5058282846941156, -19.583463131403853, -92.00520675013153), (1.425286, 0.86643547, 0.9308633), "PWM_Quarry_5x4x17_6", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4279.3716, 5898.0186, 180.93668), (-8.412750655648813, -170.06382223339472, 11.057992613445876), (1.2279452, 1.2279452, 1.2279452), "PWM_Quarry_5x4x18_15", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2891.6719, 5730.003, 651.76697), (16.15242130502116, 10.935773911424482, -15.89923151091425), (0.6961207, 1.0074973, 0.8440802), "PWM_Quarry_5x4x19_79", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1695.094, 4607.1064, 808.49835), (6.437343677337276, 13.058468341798143, -25.798183846767056), (0.62688744, 0.62688744, 0.62688744), "PWM_Quarry_5x4x20_115", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (774.60864, 3710.3193, 2070.2224), (6.43734438522768, 13.058469394307071, -25.798183777150257), (0.74937093, 0.74937093, 0.74937093), "PWM_Quarry_5x4x21", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (615.2543, 3983.5662, 1405.3274), (-14.033691078526772, -162.3208809246808, -148.57096345394334), (0.9484808, 0.8131618, 1.4973009), "PWM_Quarry_5x4x22", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5136.7515, 4262.5205, 900.7313), (4.182377514647192, 19.93258285887615, -31.866765905890258), (0.94861025, 0.9179759, 0.9179759), "PWM_Quarry_5x4x24_30", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1817.773, 4476.318, 728.92), (-14.358823990253473, -47.980978943142645, -18.740811694633784), (0.6502497, 0.6502497, 0.6502497), "PWM_Quarry_5x4x26_68", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (6137.1553, 5376.706, 390.5387), (17.116523966095123, 4.494061757568485, -16.814301077630386), (0.5460323, 0.5460323, 0.5460323), "PWM_Quarry_5x4x27_80", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2203.1165, 5727.5073, 381.214), (-62.85143367847051, -26.715480157862828, -166.1557385877851), (1.227945, 1.227945, 1.227945), "PWM_Quarry_5x4x28", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5910.0, 5600.0, 635.0), (-0.7851562536425284, 11.276098842185297, -8.259642601765455), (0.84928423, 0.84928423, 0.84928423), "PWM_Quarry_5x4x29_3", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2474.5752, 4486.9683, 438.79688), (85.18513185086329, -139.39478237567556, 11.279970225736976), (0.60974485, 0.84493256, 0.60974485), "PWM_Quarry_5x4x30_2", _folder)
if a: placed += 1
else: skipped += 1

# Batch 64: StaticMesh'PWM_Quarry_8x8x8_A' (2 instances)
_mesh_path = "/Game/Unshippable/Whitebox/Rocks/Meshes/PWM_Quarry_8x8x8_A"
_materials = ['/Game/Environments/ProcTexturing/ProcMaterial_Quarry_Atlas_2']
_folder = "Reconstruction/BD_BB_Outdoor_ExpeditionStart/Meshes"
a = spawn_static_mesh(_mesh_path, _materials, (3280.5989, 1958.532, 352.67938), (0.0, 0.0, -0.0), (1.3634536, 1.2027305, 1.0), "PWM_Quarry_8x8x8_A68_370", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3280.5728, 920.20557, 314.4477), (0.0, -90.03710389396957, 0.0), (1.7900976, 1.5641516, 1.0), "PWM_Quarry_8x8x8_A69", _folder)
if a: placed += 1
else: skipped += 1

# Batch 65: StaticMesh'PWM_Quarry_8x8x8_A' (18 instances)
_mesh_path = "/Game/Unshippable/Whitebox/Rocks/Meshes/PWM_Quarry_8x8x8_A"
_materials = ['/Game/Environments/ProcTexturing/ProcMaterial_Quarry_Atlas_2_Snow_v2']
_folder = "Reconstruction/BD_BB_Outdoor_ExpeditionStart/Meshes"
a = spawn_static_mesh(_mesh_path, _materials, (4616.072, 5864.128, 304.49768), (26.304973615487786, 4.263377784600812e-06, -10.717284237747789), (0.34761927, 0.34761927, 1.0138313), "PWM_Quarry_5x4x23_21", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (393.95343, 2728.7139, 1420.4934), (-8.031922007980041, -143.06945768571003, 12.133253638672688), (0.718939, 1.198523, 2.0), "PWM_Quarry_8x8x8_A11", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (849.40814, 2980.878, 1421.4781), (-29.43323385775601, -112.55298565191886, 16.271565319419032), (1.0257002, 1.0954162, 2.3309455), "PWM_Quarry_8x8x8_A14", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4355.8633, 2033.6812, 2041.3696), (-0.970825231182234, -172.33768491096808, 14.485015356453403), (1.1390542, 1.1985232, 2.0088685), "PWM_Quarry_8x8x8_A2", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1772.3815, 3354.306, 1002.1647), (-5.357117185682564, -160.746495363026, 20.36667573043625), (1.0152087, 1.6504475, 1.2560949), "PWM_Quarry_8x8x8_A20", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5585.212, 5870.808, 310.17065), (14.178165890710222, 89.88107496088853, -11.800780485964667), (0.36025724, 0.56571937, 1.0414311), "PWM_Quarry_8x8x8_A21_132", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4718.2217, 2424.2173, 2317.51), (-3.269226165380797, -4.297729937904873, -18.71737882248515), (0.427786, 0.497502, 1.092057), "PWM_Quarry_8x8x8_A3", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5590.9927, 2819.6472, 1427.8695), (15.34368464524507, 53.605997583394576, -11.036773941390454), (1.5, 0.5, 2.0), "PWM_Quarry_8x8x8_A4_40", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5902.185, 3050.8904, 1436.5684), (22.22538460863621, 96.56716450980676, -176.6524574581694), (1.387959, 1.1393589, 3.508136), "PWM_Quarry_8x8x8_A48", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1924.7347, 2647.3054, 1034.5231), (-0.970825231182234, -172.33768491096808, 14.485015356453403), (0.8805363, 1.198523, 1.509086), "PWM_Quarry_8x8x8_A5", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5507.095, 3793.3748, 700.8106), (68.90052228639587, -91.54195712722046, -91.43849316197847), (1.2714442, 1.0, 1.3896599), "PWM_Quarry_8x8x8_A53_182", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2243.4502, 5978.34, 136.6265), (20.23563493474781, -7.9042960500139925, -21.86996321452799), (0.52218795, 0.47358644, 1.0838221), "PWM_Quarry_8x8x8_A54_196", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3261.0203, 1930.8079, 2508.4392), (2.9211516297960625, 10.857488339248999, -16.552274558343434), (1.1624885, 1.0836751, 0.99225295), "PWM_Quarry_8x8x8_A58_225", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5456.697, 3099.7778, 460.1848), (-90.0, 22.147082216070164, -115.69483906694204), (1.0275525, 1.8792737, 2.5035741), "PWM_Quarry_8x8x8_A6", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5587.6934, 3222.0132, 1095.4811), (0.0, 0.0, -16.042084186842587), (1.271444, 1.0, 2.1155133), "PWM_Quarry_8x8x8_A62", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1762.1243, 3308.554, 1174.2318), (4.433857322401985, -162.9108110718139, -89.36842842704228), (0.8929812, 1.2673019, 0.9751451), "PWM_Quarry_8x8x8_A67", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (6101.384, 5463.108, 545.95636), (-12.847564793051754, -65.89281607829922, -18.087003970629382), (0.3242114, 0.3242114, 0.7755623), "PWM_Quarry_8x8x8_A71_77", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (6138.6533, 5292.6646, 396.8593), (-13.725767918633332, -90.07766782782322, -8.53546092692822), (0.14071447, 0.14071447, 0.3365533), "PWM_Quarry_8x8x8_A73", _folder)
if a: placed += 1
else: skipped += 1

# Batch 66: StaticMesh'PWM_Quarry_8x8x8_A' (2 instances)
_mesh_path = "/Game/Unshippable/Whitebox/Rocks/Meshes/PWM_Quarry_8x8x8_A"
_materials = ['/Game/Environments/ProcTexturing/ProcMaterial_Quarry_Atlas_A_Snow_v2']
_folder = "Reconstruction/BD_BB_Outdoor_ExpeditionStart/Meshes"
a = spawn_static_mesh(_mesh_path, _materials, (5205.5405, 3927.3733, 1385.7773), (5.337868035099509, 19.211016113892295, -32.26632521934305), (0.30118105, 0.27054712, 0.83929574), "PWM_Quarry_5x4x25", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3222.3262, 5767.658, 389.55817), (20.97731585680167, 5.13623656605554, -16.290039750675952), (0.3280588, 0.3280588, 1.1245246), "PWM_Quarry_8x8x8_A70_51", _folder)
if a: placed += 1
else: skipped += 1

# Batch 67: StaticMesh'PWM_Quarry_Floor_6x2x1_A' (2 instances)
_mesh_path = "/Game/Unshippable/Whitebox/Rocks/Meshes/PWM_Quarry_Floor_6x2x1_A"
_materials = ['/Game/Environments/ProcTexturing/ProcMaterial_Quarry_Atlas_A_Snow_v2']
_folder = "Reconstruction/BD_BB_Outdoor_ExpeditionStart/Meshes"
a = spawn_static_mesh(_mesh_path, _materials, (3463.6055, 5252.2856, 446.8682), (-4.354858573682802, -70.50577169708163, -1.936126802919813), (1.266882, 1.308542, 0.672921), "PWM_Quarry_2x2x2_A31", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3712.8423, 5295.6763, 407.08658), (-5.260071120609963, -83.91721407673825, 0.1586609968660009), (1.130425, 1.38811, 0.672921), "PWM_Quarry_2x2x2_A47", _folder)
if a: placed += 1
else: skipped += 1

# Batch 68: StaticMesh'PWM_Quarry_Floor_8x4x1_A' (1 instances)
_mesh_path = "/Game/Unshippable/Whitebox/Rocks/Meshes/PWM_Quarry_Floor_8x4x1_A"
_materials = ['/Game/Environments/ProcTexturing/ProcMaterial_Quarry_Atlas_2_Snow_v2']
_folder = "Reconstruction/BD_BB_Outdoor_ExpeditionStart/Meshes"
a = spawn_static_mesh(_mesh_path, _materials, (4082.0352, 5374.627, 345.44165), (0.0, 77.18316780925974, -0.0), (1.0, 1.0, 1.0), "PWM_Quarry_8x8x8_A60_52", _folder)
if a: placed += 1
else: skipped += 1

# Batch 69: StaticMesh'PWM_Quarry_Floor_8x4x1_A' (4 instances)
_mesh_path = "/Game/Unshippable/Whitebox/Rocks/Meshes/PWM_Quarry_Floor_8x4x1_A"
_materials = ['/Game/Environments/ProcTexturing/ProcMaterial_Quarry_Atlas_A_Snow_v2']
_folder = "Reconstruction/BD_BB_Outdoor_ExpeditionStart/Meshes"
a = spawn_static_mesh(_mesh_path, _materials, (3270.6226, 5103.951, 473.232), (-0.9981690402464835, -56.49848246635502, -3.7219241175762012), (1.2668818, 1.3085417, 0.85503995), "PWM_Quarry_2x2x2_A29_156", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3290.927, 5196.2324, 464.92972), (2.861855648063971, 126.5914540027943, 2.1180416007685867), (1.266882, 1.308542, 0.672921), "PWM_Quarry_2x2x2_A40", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3570.4182, 5237.781, 420.3358), (-3.376037661036994, -75.43362516369301, -0.5308530616380772), (1.1304252, 1.039393, 0.672921), "PWM_Quarry_2x2x2_A42", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3799.325, 5307.141, 372.47293), (-1.939758290913712, -93.10150190131381, -2.41766333904582), (1.130425, 1.38811, 0.80399966), "PWM_Quarry_2x2x2_A49", _folder)
if a: placed += 1
else: skipped += 1

# Batch 70: StaticMesh'PWM_Quarry_Floor_8x8x8_A' (1 instances)
_mesh_path = "/Game/Unshippable/Whitebox/Rocks/Meshes/PWM_Quarry_Floor_8x8x8_A"
_materials = ['/Game/Environments/ProcTexturing/ProcMaterial_Quarry_8m_Floor_Snow']
_folder = "Reconstruction/BD_BB_Outdoor_ExpeditionStart/Meshes"
a = spawn_static_mesh(_mesh_path, _materials, (1794.2231, 3432.9229, 1745.0), (0.0, 15.000088880529146, -0.0), (0.6606661, 0.6606661, 0.20726864), "PWM_Quarry_Floor_8x8x8_A2_334", _folder)
if a: placed += 1
else: skipped += 1

# Batch 71: StaticMesh'PWM_Quarry_Floor_8x8x8_A' (15 instances)
_mesh_path = "/Game/Unshippable/Whitebox/Rocks/Meshes/PWM_Quarry_Floor_8x8x8_A"
_materials = ['/Game/Environments/ProcTexturing/ProcMaterial_Quarry_Atlas_6_Snow_v2']
_folder = "Reconstruction/BD_BB_Outdoor_ExpeditionStart/Meshes"
a = spawn_static_mesh(_mesh_path, _materials, (3240.7043, 2911.4414, 630.0), (0.0, 0.0, -0.0), (3.1697845, 1.2192628, 0.40483952), "PWM_Quarry_Floor_8x8x8_A_31", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4386.457, 3396.1995, 550.0), (0.0, 137.61967207902538, -0.0), (0.630351, 1.509249, 0.5), "PWM_Quarry_Floor_8x8x8_A10", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3955.936, 3371.3623, 585.0), (0.0, -56.44897183135667, 0.0), (0.9211958, 1.509249, 0.5), "PWM_Quarry_Floor_8x8x8_A11", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1154.6735, 3607.7341, 450.0), (0.0, -179.4716625610082, 0.0), (2.3574831, 1.509249, 0.5), "PWM_Quarry_Floor_8x8x8_A12", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3771.8254, 4005.5205, 590.0), (0.0, -33.73968408121071, 0.0), (0.630351, 0.70232946, 0.5), "PWM_Quarry_Floor_8x8x8_A13", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2417.8804, 3333.167, 614.99634), (-0.6746521106885269, 15.079653120948622, -1.0632934098753888), (1.104673, 1.509249, 0.45198074), "PWM_Quarry_Floor_8x8x8_A14", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2601.6123, 3248.5225, 575.202), (0.0, 48.08466709104439, -0.0), (0.630351, 1.509249, 0.517647), "PWM_Quarry_Floor_8x8x8_A15", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2366.942, 3544.4485, 436.72577), (0.0, 35.95695257605366, -0.0), (1.0, 1.5, 0.5), "PWM_Quarry_Floor_8x8x8_A16", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1878.9617, 4036.7244, 436.72577), (0.0, 46.84142315422999, -0.0), (1.0, 1.5, 0.5), "PWM_Quarry_Floor_8x8x8_A20", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4509.178, 3970.2856, 695.0043), (0.0, -92.63086378214709, 0.0), (0.630351, 1.509249, 0.26335347), "PWM_Quarry_Floor_8x8x8_A22", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4253.338, 3027.6401, 590.0), (0.0, 0.0, -0.0), (1.969216, 2.117533, 0.5), "PWM_Quarry_Floor_8x8x8_A4", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4962.837, 3661.0579, 550.0), (0.0, 80.64599609171223, -0.0), (1.0337185, 1.692871, 0.5), "PWM_Quarry_Floor_8x8x8_A5", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1180.7041, 3170.5498, 573.923), (0.0, 0.0, -0.0), (2.5594833, 1.692871, 0.517647), "PWM_Quarry_Floor_8x8x8_A6", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1030.7041, 4035.079, 393.92297), (0.0, 0.0, -0.0), (2.0, 1.692871, 0.517647), "PWM_Quarry_Floor_8x8x8_A8_43", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4966.6343, 3453.1565, 575.2031), (0.0, -56.06637539911954, 0.0), (0.630351, 1.509249, 0.517647), "PWM_Quarry_Floor_8x8x8_A9", _folder)
if a: placed += 1
else: skipped += 1

# ======================================================================
# PHASE 2: ConstructionCatalog  (construction blocks)
# ======================================================================
unreal.log(f"[{BUBBLE_NAME}] Phase 2: Placing construction blocks...")

# Construction blocks use DecoVolume transforms (matched by Name)
_folder = "Reconstruction/BD_BB_Outdoor_ExpeditionStart/Construction"

# Construction: AB_Mines_Scaffolding_Balcony_Broken_B_2
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Scaffolding
#   Volume: EMorSimpleShape::OrientedBox, BoxExtent: (146.2, 177.8, 108.3)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (2196.003, 3306.3472, 1744.9651), (0.0, 0.0, -0.0), (2.9236, 3.5552, 2.1661), "AB_Mines_Scaffolding_Balcony_Broken_B_2", _folder)
if a: placed += 1
else: skipped += 1

# Construction: AB_Mines_Scaffolding_Balcony_Single_A_Broken_B_2
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Scaffolding
#   Volume: EMorSimpleShape::Empty, BoxExtent: (100.0, 100.0, 100.0)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (2073.6157, 3582.324, 1800.0), (0.0, 15.00011254051074, -0.0), (2.0000, 2.0000, 2.0000), "AB_Mines_Scaffolding_Balcony_Single_A_Broken_B_2", _folder)
if a: placed += 1
else: skipped += 1

# Construction: AB_Mines_Scaffolding_Broken_Segment_A2_14
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Scaffolding
#   Volume: EMorSimpleShape::Empty, BoxExtent: (100.0, 100.0, 100.0)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (1959.3247, 4010.2434, 1839.8881), (0.0, 15.000148960076068, -0.0), (2.0000, 2.0000, 2.0000), "AB_Mines_Scaffolding_Broken_Segment_A2_14", _folder)
if a: placed += 1
else: skipped += 1

# Construction: AB_Mines_Scaffolding_Broken_Segment_A3_17
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Scaffolding
#   Volume: EMorSimpleShape::Empty, BoxExtent: (100.0, 100.0, 100.0)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (2372.3762, 3488.0608, 852.5209), (25.039116769058058, 17.72127734227335, 5.312136012900524e-06), (2.0000, 2.0000, 2.0000), "AB_Mines_Scaffolding_Broken_Segment_A3_17", _folder)
if a: placed += 1
else: skipped += 1

# Construction: AB_Mines_Scaffolding_Broken_Segment_A4_20
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Scaffolding
#   Volume: EMorSimpleShape::Empty, BoxExtent: (100.0, 100.0, 100.0)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (1792.8344, 3453.1704, 1839.8881), (0.0, 15.000262648153798, -0.0), (2.0000, 2.0000, 2.0000), "AB_Mines_Scaffolding_Broken_Segment_A4_20", _folder)
if a: placed += 1
else: skipped += 1

# Construction: AB_Mines_Scaffolding_Broken_Segment_A5
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Scaffolding
#   Volume: EMorSimpleShape::Empty, BoxExtent: (100.0, 100.0, 100.0)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (1976.3602, 3502.3467, 1839.8881), (-0.0, -164.99968877838714, -0.0), (2.0000, 2.0000, 2.0000), "AB_Mines_Scaffolding_Broken_Segment_A5", _folder)
if a: placed += 1
else: skipped += 1

# Construction: AB_Mines_Scaffolding_Broken_Segment_A7_2
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Scaffolding
#   Volume: EMorSimpleShape::Empty, BoxExtent: (100.0, 100.0, 100.0)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (4247.0684, 3885.8157, 813.7905), (-10.912598558792803, 165.17221675783313, -2.089874704694492), (2.0000, 2.0000, 2.0000), "AB_Mines_Scaffolding_Broken_Segment_A7_2", _folder)
if a: placed += 1
else: skipped += 1

# Construction: AB_Mines_Scaffolding_Broken_Segment_A8_5
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Scaffolding
#   Volume: EMorSimpleShape::Empty, BoxExtent: (100.0, 100.0, 100.0)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (1129.091, 4902.274, 547.3113), (13.615898431744453, 99.36360493843765, -10.006468760432329), (2.0000, 2.0000, 2.0000), "AB_Mines_Scaffolding_Broken_Segment_A8_5", _folder)
if a: placed += 1
else: skipped += 1

# Construction: AB_Mines_Scaffolding_Broken_Segment_A_Snow_2
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Scaffolding
#   Volume: EMorSimpleShape::Empty, BoxExtent: (100.0, 100.0, 100.0)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (1916.8439, 4898.571, 528.90735), (-11.833953795060895, 72.58004527166786, 7.598183779243139), (2.0000, 2.0000, 2.0000), "AB_Mines_Scaffolding_Broken_Segment_A_Snow_2", _folder)
if a: placed += 1
else: skipped += 1

# Construction: AB_Mines_Scaffolding_Broken_Segment_B_2
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Scaffolding
#   Volume: EMorSimpleShape::Empty, BoxExtent: (100.0, 100.0, 100.0)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (1423.3086, 3992.8547, 1839.8881), (0.0, 15.000124288757021, -0.0), (2.0000, 2.0000, 2.0000), "AB_Mines_Scaffolding_Broken_Segment_B_2", _folder)
if a: placed += 1
else: skipped += 1

# Construction: AB_Mines_Scaffolding_Broken_Segment_B2_7
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Scaffolding
#   Volume: EMorSimpleShape::Empty, BoxExtent: (100.0, 100.0, 100.0)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (2251.8752, 3749.0078, 925.2666), (-10.050965310373115, 91.83150314530667, -59.6514432394928), (2.0000, 2.0000, 2.0000), "AB_Mines_Scaffolding_Broken_Segment_B2_7", _folder)
if a: placed += 1
else: skipped += 1

# Construction: AB_Mines_Scaffolding_Broken_Segment_B3_10
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Scaffolding
#   Volume: EMorSimpleShape::Empty, BoxExtent: (100.0, 100.0, 100.0)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (1822.4054, 3710.0361, 1840.0), (-0.0, -164.99968877838714, -0.0), (2.0000, 2.0000, 2.0000), "AB_Mines_Scaffolding_Broken_Segment_B3_10", _folder)
if a: placed += 1
else: skipped += 1

# Construction: AB_Mines_Scaffolding_Broken_Segment_B4
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Scaffolding
#   Volume: EMorSimpleShape::Empty, BoxExtent: (100.0, 100.0, 100.0)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (1959.6564, 3197.6396, 1839.8881), (0.0, 15.000277650928311, -0.0), (2.0000, 2.0000, 2.0000), "AB_Mines_Scaffolding_Broken_Segment_B4", _folder)
if a: placed += 1
else: skipped += 1

# Construction: AB_Mines_Scaffolding_Broken_Segment_B6_5
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Scaffolding
#   Volume: EMorSimpleShape::Empty, BoxExtent: (100.0, 100.0, 100.0)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (4593.1543, 4190.5063, 832.5159), (-1.7195735868846178, 36.510732382395695, 11.75004797137631), (2.0000, 2.0000, 2.0000), "AB_Mines_Scaffolding_Broken_Segment_B6_5", _folder)
if a: placed += 1
else: skipped += 1

# Construction: AB_Mines_Scaffolding_Broken_Segment_B7_8
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Scaffolding
#   Volume: EMorSimpleShape::Empty, BoxExtent: (100.0, 100.0, 100.0)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (578.4634, 5022.9277, 528.8744), (2.0730367386317297, -92.04016472593052, -10.431366441733738), (2.0000, 2.0000, 2.0000), "AB_Mines_Scaffolding_Broken_Segment_B7_8", _folder)
if a: placed += 1
else: skipped += 1

# Construction: AB_Mines_Scaffolding_Broken_Segment_B8_2
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Scaffolding
#   Volume: EMorSimpleShape::Empty, BoxExtent: (100.0, 100.0, 100.0)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (3889.996, 3733.843, 808.73914), (2.2629987722798676e-09, 36.17044648515787, -0.4437561104466473), (2.0000, 2.0000, 2.0000), "AB_Mines_Scaffolding_Broken_Segment_B8_2", _folder)
if a: placed += 1
else: skipped += 1

# Construction: AB_Mines_Scaffolding_Broken_Segment_C_2
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Scaffolding
#   Volume: EMorSimpleShape::Empty, BoxExtent: (100.0, 100.0, 100.0)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (2650.5188, 3155.2163, 817.7537), (12.558143869243724, 8.692895413069699e-07, -9.836365624383598), (2.0000, 2.0000, 2.0000), "AB_Mines_Scaffolding_Broken_Segment_C_2", _folder)
if a: placed += 1
else: skipped += 1

# Construction: AB_Mines_Scaffolding_Broken_Segment_C2_2
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Scaffolding
#   Volume: EMorSimpleShape::Empty, BoxExtent: (100.0, 100.0, 100.0)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (4341.6025, 3745.2627, 890.0), (-0.0, -30.000063894566395, -0.0), (2.0000, 2.0000, 2.0000), "AB_Mines_Scaffolding_Broken_Segment_C2_2", _folder)
if a: placed += 1
else: skipped += 1

# Construction: AB_Mines_Scaffolding_Foundation_3x1m_Broken_B_2
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Scaffolding
#   Volume: EMorSimpleShape::Empty, BoxExtent: (100.0, 100.0, 100.0)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (1790.5015, 4232.04, 1700.0), (0.0, 15.00011254051074, -0.0), (2.0000, 2.0000, 2.0000), "AB_Mines_Scaffolding_Foundation_3x1m_Broken_B_2", _folder)
if a: placed += 1
else: skipped += 1

# Construction: AB_Mines_Scaffolding_Foundation_3x3m_2
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Scaffolding
#   Volume: EMorSimpleShape::Empty, BoxExtent: (100.0, 100.0, 100.0)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (1755.1112, 3961.1765, 1700.0), (0.0, 15.000148960076068, -0.0), (2.0000, 2.0000, 2.0000), "AB_Mines_Scaffolding_Foundation_3x3m_2", _folder)
if a: placed += 1
else: skipped += 1

# Construction: AB_Mines_Scaffolding_Foundation_3x3m3
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Scaffolding
#   Volume: EMorSimpleShape::Empty, BoxExtent: (100.0, 100.0, 100.0)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (1504.1567, 3738.6414, 1700.0), (0.0, 15.000148960076068, -0.0), (2.0000, 2.0000, 2.0000), "AB_Mines_Scaffolding_Foundation_3x3m3", _folder)
if a: placed += 1
else: skipped += 1

# Construction: AB_Mines_Scaffolding_Foundation_3x3m4
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Scaffolding
#   Volume: EMorSimpleShape::Empty, BoxExtent: (100.0, 100.0, 100.0)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (1581.803, 3448.863, 1700.0), (0.0, 15.000148960076068, -0.0), (2.0000, 2.0000, 2.0000), "AB_Mines_Scaffolding_Foundation_3x3m4", _folder)
if a: placed += 1
else: skipped += 1

# Construction: AB_Mines_Scaffolding_Foundation_3x3m5_9
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Scaffolding
#   Volume: EMorSimpleShape::Empty, BoxExtent: (100.0, 100.0, 100.0)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (1659.4492, 3159.0854, 1700.0), (0.0, 15.000148960076068, -0.0), (2.0000, 2.0000, 2.0000), "AB_Mines_Scaffolding_Foundation_3x3m5_9", _folder)
if a: placed += 1
else: skipped += 1

# Construction: AB_Mines_Scaffolding_Foundation_3x3m6
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Scaffolding
#   Volume: EMorSimpleShape::Empty, BoxExtent: (100.0, 100.0, 100.0)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (2026.873, 2946.9539, 1700.0), (0.0, 15.000130162880376, -0.0), (2.0000, 2.0000, 2.0000), "AB_Mines_Scaffolding_Foundation_3x3m6", _folder)
if a: placed += 1
else: skipped += 1

# Construction: AB_Mines_Scaffolding_Foundation_3x3x1m_2
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Scaffolding
#   Volume: EMorSimpleShape::Empty, BoxExtent: (100.0, 100.0, 100.0)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (4118.3013, 3581.6987, 850.0), (-0.0, -30.000063894566395, -0.0), (2.0000, 2.0000, 2.0000), "AB_Mines_Scaffolding_Foundation_3x3x1m_2", _folder)
if a: placed += 1
else: skipped += 1

# Construction: AB_Mines_Scaffolding_Foundation_3x3x1m_B_5
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Scaffolding
#   Volume: EMorSimpleShape::Empty, BoxExtent: (100.0, 100.0, 100.0)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (1160.0, 4520.0, 938.0), (0.0, 0.0, -0.0), (2.0000, 2.0000, 2.0000), "AB_Mines_Scaffolding_Foundation_3x3x1m_B_5", _folder)
if a: placed += 1
else: skipped += 1

# Construction: AB_Mines_Scaffolding_Foundation_3x3x1m_B2
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Scaffolding
#   Volume: EMorSimpleShape::Empty, BoxExtent: (100.0, 100.0, 100.0)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (860.0, 4520.0, 938.0), (0.0, 0.0, -0.0), (2.0000, 2.0000, 2.0000), "AB_Mines_Scaffolding_Foundation_3x3x1m_B2", _folder)
if a: placed += 1
else: skipped += 1

# ======================================================================
# PHASE 3: Breakables + DecoVolumes
# ======================================================================
unreal.log(f"[{BUBBLE_NAME}] Phase 3: Placing breakables and deco volumes...")

_folder = "Reconstruction/BD_BB_Outdoor_ExpeditionStart/Breakables"

# Breakable Batch 0: BP_DM_Mines_Lift_Prop_horizontal_broken_Breakable (1 instances)
#   BP Class: /Game/LevelDesign/Deco/MinesDressing/BP_DM_Mines_Lift_Prop_horizontal_broken_Breakable
_brk_mesh = "/Game/Art/Assets/Kits/Deco/Mines/Machine/Mines_Machine_Lift_Pieces/Mines_Lift_Prop_horizontal_broken"
_brk_mats = ['/Game/Art/Assets/Kits/Deco/Mines/Machine/Mines_Machine_Lift_Pieces/Materials/Mi_Mines_Machine_Lift_L']
a = spawn_static_mesh(_brk_mesh, _brk_mats, (1597.9431, 5645.087, 519.7702), (5.099111421292968, 145.45781336038277, 8.231586555781835), (1.0, 1.0, 1.0), "BP_DM_Mines_Lift_Prop_horizontal_broken_Breakable_4", _folder)
if a: placed += 1
else: skipped += 1

# Breakable Batch 1: BP_DM_Mines_Machine_Whim_Boar_PullBar_Broken (2 instances)
#   BP Class: /Game/LevelDesign/Deco/MinesDressing/BP_DM_Mines_Machine_Whim_Boar_PullBar_Broken
_brk_mesh = "/Game/Art/Assets/Kits/Deco/Mines/Machine/Mines_Machine_Whim_Pieces/Mines_Machine_Whim_Boar_PullBar_Broken"
_brk_mats = ['/Game/Art/Assets/Kits/Deco/Mines/Materials/Mines_Machine_Whim/MI_Mines_Machine_Whim_Uniq', '/Game/Art/Assets/Kits/Deco/Mines/Materials/Mines_Machine_Whim/MI_Mines_Machine_Whim_Trim']
a = spawn_static_mesh(_brk_mesh, _brk_mats, (1899.8348, 5007.4663, 506.43314), (1.1654167790213188e-08, -55.06225616709637, 7.325415140336914), (1.0, 1.0, 1.0), "BP_DM_Mines_Machine_Whim_Boar_PullBar_Broken_2", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_brk_mesh, _brk_mats, (2742.0286, 3092.8713, 824.1737), (0.0, -34.46472096093086, 0.0), (1.0, 1.0, 1.0), "BP_DM_Mines_Machine_Whim_Boar_PullBar_Broken2_5", _folder)
if a: placed += 1
else: skipped += 1

# Breakable Batch 2: BP_DM_Mines_Machine_Whim_Heavy_Beam_Broken (1 instances)
#   BP Class: /Game/LevelDesign/Deco/MinesDressing/BP_DM_Mines_Machine_Whim_Heavy_Beam_Broken
_brk_mesh = "/Game/Art/Assets/Kits/Deco/Mines/Machine/Mines_Machine_Whim_Pieces/Mines_Machine_Whim_Heavy_Beam_Broken"
_brk_mats = ['/Game/Art/Assets/Kits/Deco/Mines/Materials/Mines_Machine_Whim/MI_Mines_Machine_Whim_Trim', '/Game/Art/Assets/Kits/Deco/Mines/Materials/Mines_Machine_Whim/MI_Mines_Machine_Whim_Uniq']
a = spawn_static_mesh(_brk_mesh, _brk_mats, (2748.8552, 2992.294, 818.62885), (-83.05828965258456, 28.566183739128032, -123.11481196238047), (1.0, 1.0, 1.0), "BP_DM_Mines_Machine_Whim_Heavy_Beam_Broken2_5", _folder)
if a: placed += 1
else: skipped += 1

# Breakable Batch 3: BP_DM_Mines_Machine_Whim_Side_Support_Beam_Broken_B (2 instances)
#   BP Class: /Game/LevelDesign/Deco/MinesDressing/BP_DM_Mines_Machine_Whim_Side_Support_Beam_Broken_B
_brk_mesh = "/Game/Art/Assets/Kits/Deco/Mines/Machine/Mines_Machine_Whim_Pieces/Mines_Machine_Whim_Side_Support_Beam_Broken_B"
_brk_mats = ['/Game/Art/Assets/Kits/Deco/Mines/Materials/Mines_Machine_Whim/MI_Mines_Machine_Whim_Trim']
a = spawn_static_mesh(_brk_mesh, _brk_mats, (1343.8335, 4875.1733, 496.8647), (-4.936555537339571, 89.67336742509507, 88.13168206609716), (1.0, 1.0, 1.0), "BP_DM_Mines_Machine_Whim_Side_Support_Beam_Broken_B_2", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_brk_mesh, _brk_mats, (2155.3875, 3862.3467, 824.8789), (-3.2436536482328644, 16.759541415086638, 90.58741708527344), (1.0, 1.0, 1.0), "BP_DM_Mines_Machine_Whim_Side_Support_Beam_Broken_B3", _folder)
if a: placed += 1
else: skipped += 1

# Breakable Batch 4: BP_DM_Mines_Machine_Whim_Side_Support_Beam_Broken_C (2 instances)
#   BP Class: /Game/LevelDesign/Deco/MinesDressing/BP_DM_Mines_Machine_Whim_Side_Support_Beam_Broken_C
_brk_mesh = "/Game/Art/Assets/Kits/Deco/Mines/Machine/Mines_Machine_Whim_Pieces/Mines_Machine_Whim_Side_Support_Beam_Broken_C"
_brk_mats = ['/Game/Art/Assets/Kits/Deco/Mines/Materials/Mines_Machine_Whim/MI_Mines_Machine_Whim_Trim']
a = spawn_static_mesh(_brk_mesh, _brk_mats, (2361.503, 3298.8137, 826.2125), (1.948188113910482, -97.25812152077665, 89.75186853738225), (1.0, 1.0, 1.0), "BP_DM_Mines_Machine_Whim_Side_Support_Beam_Broken_C_2", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_brk_mesh, _brk_mats, (2409.5383, 3393.9497, 842.09827), (2.055676655482575, -32.24447761824964, 178.52625005108118), (1.0, 1.0, 1.0), "BP_DM_Mines_Machine_Whim_Side_Support_Beam_Broken_C2", _folder)
if a: placed += 1
else: skipped += 1

# Breakable Batch 5: BP_DM_OutdoorSnow_Machine_Whim_Rope_Bracket_Broken (3 instances)
#   BP Class: /Game/LevelDesign/Deco/MinesDressing/BP_DM_OutdoorSnow_Machine_Whim_Rope_Bracket_Broken
_brk_mesh = "/Game/Art/Assets/Kits/Deco/Mines/Machine/Mines_Machine_Whim_Pieces/Mines_Machine_Whim_Rope_Bracket_Broken_A"
_brk_mats = ['/Game/Art/Assets/Kits/Deco/Mines/Materials/Mines_Machine_Whim/MI_Mines_Machine_Whim_Trim_Snow', '/Game/Art/Assets/Kits/Deco/Mines/Materials/Mines_Machine_Whim/MI_Mines_Machine_Whim_Uniq_Snow']
a = spawn_static_mesh(_brk_mesh, _brk_mats, (1654.1088, 5561.3384, 514.8735), (6.25876195024957, 39.089920234617225, 2.4568366351632312e-06), (1.0, 1.0, 1.0), "BP_DM_OutdoorSnow_Machine_Whim_Rope_Bracket_Broken_2", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_brk_mesh, _brk_mats, (1340.8867, 4739.3657, 657.8835), (0.0, -25.98062093448749, 0.0), (1.0, 1.0, 1.0), "BP_DM_OutdoorSnow_Machine_Whim_Rope_Bracket_Broken2_5", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_brk_mesh, _brk_mats, (2881.4763, 2972.8618, 821.85583), (0.0, 0.0, -0.0), (1.0, 1.0, 1.0), "BP_DM_OutdoorSnow_Machine_Whim_Rope_Bracket_Broken3_8", _folder)
if a: placed += 1
else: skipped += 1

# Breakable Batch 6: BP_DM_Snow_Wagon_Broken_A (4 instances)
#   BP Class: /Game/LevelDesign/Deco/MinesDressing/BP_DM_Snow_Wagon_Broken_A
_brk_mesh = "/Game/Art/Assets/Kits/Deco/Mines/Mines_Wagon_Broken_B"
_brk_mats = ['/Game/Art/Assets/Kits/Deco/Mines/Materials/Mines_WagonCart/MI_OutdoorsSnow_WagonCart_Trim', '/Game/Art/Assets/Kits/Deco/Mines/Materials/Mines_WagonCart/MI_OutdoorsSnow_WagonCart']
a = spawn_static_mesh(_brk_mesh, _brk_mats, (2154.96, 5359.8276, 486.12885), (0.0, -15.18859896078467, 0.0), (1.0, 1.0, 1.0), "BP_DM_Snow_Wagon_Broken_A_2", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_brk_mesh, _brk_mats, (651.522, 5198.878, 486.1286), (0.0, 61.38021463434831, -0.0), (1.0, 1.0, 1.0), "BP_DM_Snow_Wagon_Broken_A2", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_brk_mesh, _brk_mats, (2381.3025, 3687.1348, 826.17), (0.5294985541687802, 93.01035273357766, 3.3258694970491094), (1.0, 1.0, 1.0), "BP_DM_Snow_Wagon_Broken_A3", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_brk_mesh, _brk_mats, (1620.6726, 5036.548, 486.5856), (0.1777693198959481, 171.97230089129252, 1.5684196129176127), (1.0, 1.0, 1.0), "BP_DM_Snow_Wagon_Broken_A4", _folder)
if a: placed += 1
else: skipped += 1

# Breakable Batch 7: BP_DM_Rubble_Masonry_Pile_B_Snow (3 instances)
#   BP Class: /Game/LevelDesign/Deco/Rubble/BP_DM_Rubble_Masonry_Pile_B_Snow
_brk_mesh = "/Game/Art/Assets/Kits/Deco/Rubble/Rubble_Masonry_Pile_B"
_brk_mats = ['/Game/Art/Assets/Kits/Deco/Rubble/Materials/Rubble_Masonry_Pile/MI_Rubble_Masonry_Pile_Atlas_Inst_A_Snow', '/Game/Art/Assets/Kits/Deco/Rubble/Materials/Rubble_Masonry_Pile/MI_Rubble_Masonry_Pile_Atlas_Inst_B_Snow']
a = spawn_static_mesh(_brk_mesh, _brk_mats, (3691.9507, 5504.48, 399.55603), (-13.749968905845336, 10.776223153270852, -2.5901485560720032), (1.0, 1.0, 1.0), "BP_DM_Rubble_Masonry_Pile_B_Snow_5", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_brk_mesh, _brk_mats, (2395.0376, 4346.594, 650.8673), (0.0, -29.85968132030832, 0.0), (1.0, 1.0, 1.0), "BP_DM_Rubble_Masonry_Pile_B_Snow2_8", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_brk_mesh, _brk_mats, (1069.7528, 5639.358, 509.708), (2.5572441168156774, -159.39923670330768, 3.9060968039854522), (1.0, 1.0, 1.0), "BP_DM_Rubble_Masonry_Pile_B_Snow3_11", _folder)
if a: placed += 1
else: skipped += 1

# Breakable Batch 8: BP_DM_Rubble_Masonry_Pile_C_Snow (6 instances)
#   BP Class: /Game/LevelDesign/Deco/Rubble/BP_DM_Rubble_Masonry_Pile_C_Snow
_brk_mesh = "/Game/Art/Assets/Kits/Deco/Rubble/Rubble_Masonry_Pile_C"
_brk_mats = ['/Game/Art/Assets/Kits/Deco/Rubble/Materials/Rubble_Masonry_Pile/MI_Rubble_Masonry_Pile_Atlas_Inst_B_Snow', '/Game/Art/Assets/Kits/Deco/Rubble/Materials/Rubble_Masonry_Pile/MI_Rubble_Masonry_Pile_Atlas_Inst_A_Snow']
a = spawn_static_mesh(_brk_mesh, _brk_mats, (4842.8, 4851.067, 344.8549), (4.182483873123445e-09, -35.36938706299265, 5.247706243590644), (1.0, 1.0, 1.0), "BP_DM_Rubble_Masonry_Pile_C_Snow_2", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_brk_mesh, _brk_mats, (3570.6892, 5671.835, 538.1967), (-11.408629397971287, -168.121974279317, 5.034873202113768e-06), (1.0, 1.0, 1.0), "BP_DM_Rubble_Masonry_Pile_C_Snow2_5", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_brk_mesh, _brk_mats, (2436.0793, 5307.9434, 491.1517), (-1.9148992006824503e-09, 179.442101174367, 5.814346265801499), (1.0, 1.0, 1.0), "BP_DM_Rubble_Masonry_Pile_C_Snow3_8", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_brk_mesh, _brk_mats, (1381.2393, 4916.4233, 500.5254), (-13.783356098148326, 131.8519765318152, -5.562560943519003), (1.0, 1.0, 1.0), "BP_DM_Rubble_Masonry_Pile_C_Snow4_11", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_brk_mesh, _brk_mats, (1912.0089, 4664.121, 671.8827), (0.0, -107.07931103964641, 0.0), (1.0, 1.0, 1.0), "BP_DM_Rubble_Masonry_Pile_C_Snow5_2", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_brk_mesh, _brk_mats, (5925.5625, 5292.5996, 372.3351), (2.143380165491619, 118.74566366009796, 8.669300308479565), (1.0, 1.0, 1.0), "BP_DM_Rubble_Masonry_Pile_C_Snow6_5", _folder)
if a: placed += 1
else: skipped += 1

# Breakable Batch 9: BP_DM_Rubble_Masonry_Pile_D_Snow (1 instances)
#   BP Class: /Game/LevelDesign/Deco/Rubble/BP_DM_Rubble_Masonry_Pile_D_Snow
_brk_mesh = "/Game/Art/Assets/Kits/Deco/Rubble/Rubble_Masonry_Pile_D"
_brk_mats = ['/Game/Art/Assets/Kits/Deco/Rubble/Materials/Rubble_Masonry_Pile/MI_Rubble_Masonry_Pile_Atlas_Inst_A_Snow', '/Game/Art/Assets/Kits/Deco/Rubble/Materials/Rubble_Masonry_Pile/MI_Rubble_Masonry_Pile_Atlas_Inst_B_Snow']
a = spawn_static_mesh(_brk_mesh, _brk_mats, (3228.2168, 4736.5024, 505.88376), (0.0, 67.79349001208575, -0.0), (1.0, 1.0, 1.0), "BP_DM_Rubble_Masonry_Pile_D_Snow_2", _folder)
if a: placed += 1
else: skipped += 1

# Breakable Batch 10: BP_DM_Rubble_Masonry_Pile_E_Snow (3 instances)
#   BP Class: /Game/LevelDesign/Deco/Rubble/BP_DM_Rubble_Masonry_Pile_E_Snow
_brk_mesh = "/Game/Art/Assets/Kits/Deco/Rubble/Rubble_Masonry_Pile_E_Optimized"
_brk_mats = ['/Game/Art/Assets/Kits/Deco/Rubble/Materials/Rubble_Masonry_Pile/MI_Rubble_Masonry_Pile_Atlas_Inst_A_Snow', '/Game/Art/Assets/Kits/Deco/Rubble/Materials/Rubble_Masonry_Pile/MI_Rubble_Masonry_Pile_Atlas_Inst_B_Snow']
a = spawn_static_mesh(_brk_mesh, _brk_mats, (4869.0977, 5676.4346, 389.2618), (0.0, 0.0, -14.289124026247757), (1.0, 1.0, 1.0), "BP_DM_Rubble_Masonry_Pile_E_Snow_2", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_brk_mesh, _brk_mats, (918.0083, 4911.1724, 508.55344), (0.0, 0.0, 8.450481230880845), (1.0, 1.0, 1.0), "BP_DM_Rubble_Masonry_Pile_E_Snow2_5", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_brk_mesh, _brk_mats, (2386.0308, 4695.484, 535.55707), (-11.078369878027926, -3.005035413655404, 18.9263188374553), (1.0, 1.0, 1.0), "BP_DM_Rubble_Masonry_Pile_E_Snow3_2", _folder)
if a: placed += 1
else: skipped += 1

# Breakable Batch 11: BP_DM_Rubble_Masonry_Pile_F_Snow (1 instances)
#   BP Class: /Game/LevelDesign/Deco/Rubble/BP_DM_Rubble_Masonry_Pile_F_Snow
_brk_mesh = "/Game/Art/Assets/Kits/Deco/Rubble/Rubble_Masonry_Pile_F_Optimized"
_brk_mats = ['/Game/Art/Assets/Kits/Deco/Rubble/Materials/Rubble_Masonry_Pile/MI_Rubble_Masonry_Pile_Atlas_Inst_B_Snow', '/Game/Art/Assets/Kits/Deco/Rubble/Materials/Rubble_Masonry_Pile/MI_Rubble_Masonry_Pile_Atlas_Inst_A_Snow']
a = spawn_static_mesh(_brk_mesh, _brk_mats, (1667.664, 5684.8374, 487.73322), (0.0, 0.0, -0.0), (1.0, 1.0, 1.0), "BP_DM_Rubble_Masonry_Pile_F_Snow_2", _folder)
if a: placed += 1
else: skipped += 1

# Breakable Batch 12: BP_DM_Rubble_Masonry_Pile_I_Snow (1 instances)
#   BP Class: /Game/LevelDesign/Deco/Rubble/BP_DM_Rubble_Masonry_Pile_I_Snow
_brk_mesh = "/Game/Art/Assets/Kits/Deco/Rubble/Rubble_Masonry_Pile_I"
_brk_mats = ['/Game/Art/Assets/Kits/Deco/Rubble/Materials/Rubble_Masonry_Pile/MI_Rubble_Masonry_Pile_Atlas_Inst_B_Snow', '/Game/Art/Assets/Kits/Deco/Rubble/Materials/Rubble_Masonry_Pile/MI_Rubble_Masonry_Pile_Atlas_Inst_A_Snow']
a = spawn_static_mesh(_brk_mesh, _brk_mats, (5304.2056, 5617.834, 349.35767), (0.0, 169.24320202696794, -0.0), (1.0, 1.0, 1.0), "BP_DM_Rubble_Masonry_Pile_I_Snow_2", _folder)
if a: placed += 1
else: skipped += 1

# Breakable Batch 13: BP_DM_Workshop_Scatter_Rope_A_Breakable (1 instances)
#   BP Class: /Game/LevelDesign/Deco/Urban/Workshop/BP_DM_Workshop_Scatter_Rope_A_Breakable
_brk_mesh = "/Game/Art/Assets/Kits/Deco/Urban/Workshop/Scatter/Workshop_Scatter_Rope_A"
_brk_mats = ['/Game/Art/Assets/Kits/Deco_Architecture/Mines/Materials/Mines_Scaffolding/MI_Mines_Scaffolding_Rope_A']
a = spawn_static_mesh(_brk_mesh, _brk_mats, (786.4772, 4894.2876, 514.44366), (0.0, 0.0, 4.977723653157679), (1.0, 1.0, 1.0), "BP_DM_Workshop_Scatter_Rope_A_Breakable_2", _folder)
if a: placed += 1
else: skipped += 1

# Breakable Batch 14: BP_DM_Workshop_Scatter_Rope_F_Breakable (1 instances)
#   BP Class: /Game/LevelDesign/Deco/Urban/Workshop/BP_DM_Workshop_Scatter_Rope_F_Breakable
_brk_mesh = "/Game/Art/Assets/Kits/Deco/Urban/Workshop/Scatter/Workshop_Scatter_Rope_F"
_brk_mats = ['/Game/Art/Assets/Kits/Deco_Architecture/Mines/Materials/Mines_Scaffolding/MI_Mines_Scaffolding_Rope_A']
a = spawn_static_mesh(_brk_mesh, _brk_mats, (1163.7717, 4943.423, 516.16534), (0.5652790768903972, 0.302700938571957, 11.96379242539931), (1.0, 1.0, 1.0), "BP_DM_Workshop_Scatter_Rope_F_Breakable_2", _folder)
if a: placed += 1
else: skipped += 1

# Breakable Batch 15: BP_DM_GPI_Fabric_Station_Upgrade_Broken_Breakable (1 instances)
#   BP Class: /Game/LevelDesign/GPI/Converter/BP_DM_GPI_Fabric_Station_Upgrade_Broken_Breakable
_brk_mesh = "/Game/Art/Assets/GPI/Convertor/GPI_Fabric_Station_Upgrade_Broken"
_brk_mats = ['/Game/Art/Assets/GPI/Convertor/Materials/GPI_Fabric_Station_Upgrade/MI_GPI_Fabric_Station_Upgrade_Deco']
a = spawn_static_mesh(_brk_mesh, _brk_mats, (1821.1244, 5050.0, 502.62997), (0.0, 0.0, -0.0), (1.0, 1.0, 1.0), "BP_DM_GPI_Fabric_Station_Upgrade_Broken_Breakable_2", _folder)
if a: placed += 1
else: skipped += 1

# --- Extra DecoVolumes (not construction blocks) ---
_folder = "Reconstruction/BD_BB_Outdoor_ExpeditionStart/DecoVolumes"

# DecoVolume: BP_DM_GPI_Fabric_Station_Upgrade_Broken_Breakable_2 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (1824.508, 5022.88, 510.40887), (0.0, 0.0, -0.0), (0.9124, 0.9081, 0.2181), "DV_BP_DM_GPI_Fabric_Station_Upgrade_Broken_Breakable_2_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_DM_Mines_Fence_Brace_D_2 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (1004.32666, 4662.7656, 730.4585), (0.0, 0.0, -0.0), (6.3553, 4.5927, 4.1621), "DV_BP_DM_Mines_Fence_Brace_D_2_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_DM_Mines_Lift_Pillar_B_Broken_Breakable_2 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (2660.0686, 2996.6384, 863.4273), (0.0, 0.0, -0.0), (0.3641, 0.5734, 0.8725), "DV_BP_DM_Mines_Lift_Pillar_B_Broken_Breakable_2_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_DM_Mines_Lift_Prop_horizontal_broken_Breakable_4 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (1639.7382, 5571.6255, 520.6878), (0.0, 0.0, -0.0), (2.8267, 2.9532, 0.8095), "DV_BP_DM_Mines_Lift_Prop_horizontal_broken_Breakable_4_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_DM_Mines_Machine_Whim_Boar_PullBar_Broken_2 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (1904.9445, 5014.877, 502.9834), (0.0, 0.0, -0.0), (0.7501, 0.5855, 0.1860), "DV_BP_DM_Mines_Machine_Whim_Boar_PullBar_Broken_2_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_DM_Mines_Machine_Whim_Boar_PullBar_Broken2_5 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (2744.4146, 3101.9116, 821.82733), (0.0, 0.0, -0.0), (0.5784, 0.7496, 0.0835), "DV_BP_DM_Mines_Machine_Whim_Boar_PullBar_Broken2_5_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_DM_Mines_Machine_Whim_Heavy_Beam_Broken2_5 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (2792.8489, 3034.9243, 825.7431), (0.0, 0.0, -0.0), (1.1045, 1.1495, 0.3708), "DV_BP_DM_Mines_Machine_Whim_Heavy_Beam_Broken2_5_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_DM_Mines_Machine_Whim_Lift_B_Breakable_5 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (1611.2256, 4088.9097, 2179.1328), (0.0, 0.0, -0.0), (3.3411, 6.9741, 6.4999), "DV_BP_DM_Mines_Machine_Whim_Lift_B_Breakable_5_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_DM_Mines_Machine_Whim_Side_Support_Beam_Broken_B_2 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (1331.767, 4882.795, 584.30914), (0.0, 0.0, -0.0), (0.3509, 0.4782, 1.7768), "DV_BP_DM_Mines_Machine_Whim_Side_Support_Beam_Broken_B_2_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_DM_Mines_Machine_Whim_Side_Support_Beam_Broken_B3 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (2155.537, 3878.9546, 911.90985), (0.0, 0.0, -0.0), (0.4863, 0.4187, 1.7652), "DV_BP_DM_Mines_Machine_Whim_Side_Support_Beam_Broken_B3_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_DM_Mines_Machine_Whim_Side_Support_Beam_Broken_C_2 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (2376.4106, 3299.5493, 903.0316), (0.0, 0.0, -0.0), (0.3324, 0.4202, 1.5477), "DV_BP_DM_Mines_Machine_Whim_Side_Support_Beam_Broken_C_2_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_DM_Mines_Machine_Whim_Side_Support_Beam_Broken_C2 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (2451.1018, 3458.9604, 829.05865), (0.0, 0.0, -0.0), (1.1128, 1.4780, 0.3438), "DV_BP_DM_Mines_Machine_Whim_Side_Support_Beam_Broken_C2_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_DM_OutdoorSnow_Machine_Whim_Rope_Bracket_Broken_2 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (1589.5308, 5510.5186, 514.17505), (0.0, 0.0, -0.0), (1.4929, 1.2948, 0.3453), "DV_BP_DM_OutdoorSnow_Machine_Whim_Rope_Bracket_Broken_2_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_DM_OutdoorSnow_Machine_Whim_Rope_Bracket_Broken2_5 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (1267.9541, 4776.325, 666.1469), (0.0, 0.0, -0.0), (1.6310, 1.0078, 0.1650), "DV_BP_DM_OutdoorSnow_Machine_Whim_Rope_Bracket_Broken2_5_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_DM_OutdoorSnow_Machine_Whim_Rope_Bracket_Broken3_8 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (2799.7234, 2974.1367, 830.11926), (0.0, 0.0, -0.0), (1.6629, 0.3107, 0.1650), "DV_BP_DM_OutdoorSnow_Machine_Whim_Rope_Bracket_Broken3_8_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_DM_Rubble_Masonry_Pile_B_Snow_5 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (3718.0679, 5517.629, 448.7884), (0.0, 0.0, -0.0), (3.7839, 2.4185, 1.9611), "DV_BP_DM_Rubble_Masonry_Pile_B_Snow_5_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_DM_Rubble_Masonry_Pile_B_Snow2_8 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (2413.7952, 4347.92, 704.9526), (0.0, 0.0, -0.0), (3.8154, 3.2615, 1.1191), "DV_BP_DM_Rubble_Masonry_Pile_B_Snow2_8_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_DM_Rubble_Masonry_Pile_B_Snow3_11 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (1062.36, 5621.464, 563.5965), (0.0, 0.0, -0.0), (3.8399, 2.9509, 1.3899), "DV_BP_DM_Rubble_Masonry_Pile_B_Snow3_11_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_DM_Rubble_Masonry_Pile_C_Snow_2 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (4835.668, 4866.831, 388.1289), (0.0, 0.0, -0.0), (2.7019, 2.7015, 1.1012), "DV_BP_DM_Rubble_Masonry_Pile_C_Snow_2_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_DM_Rubble_Masonry_Pile_C_Snow2_5 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (3577.4988, 5668.4316, 584.17554), (0.0, 0.0, -0.0), (2.4231, 2.2486, 1.3000), "DV_BP_DM_Rubble_Masonry_Pile_C_Snow2_5_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_DM_Rubble_Masonry_Pile_C_Snow3_8 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (2450.93, 5298.6445, 534.33734), (0.0, 0.0, -0.0), (1.9572, 1.9632, 1.1186), "DV_BP_DM_Rubble_Masonry_Pile_C_Snow3_8_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_DM_Rubble_Masonry_Pile_C_Snow4_11 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (1383.5645, 4913.1455, 546.95654), (0.0, 0.0, -0.0), (2.7435, 2.8306, 1.5407), "DV_BP_DM_Rubble_Masonry_Pile_C_Snow4_11_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_DM_Rubble_Masonry_Pile_C_Snow5_2 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (1920.92, 4677.0127, 715.77344), (0.0, 0.0, -0.0), (2.3466, 2.3990, 0.9351), "DV_BP_DM_Rubble_Masonry_Pile_C_Snow5_2_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_DM_Rubble_Masonry_Pile_C_Snow6_5 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (5923.6084, 5272.6787, 414.42255), (0.0, 0.0, -0.0), (2.6551, 2.6712, 1.2763), "DV_BP_DM_Rubble_Masonry_Pile_C_Snow6_5_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_DM_Rubble_Masonry_Pile_D_Snow_2 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (3183.0168, 4725.0737, 596.3389), (0.0, 0.0, -0.0), (2.7547, 2.6174, 1.8381), "DV_BP_DM_Rubble_Masonry_Pile_D_Snow_2_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_DM_Rubble_Masonry_Pile_E_Snow_2 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (4854.7163, 5682.353, 414.85513), (0.0, 0.0, -0.0), (2.5083, 2.4977, 1.8164), "DV_BP_DM_Rubble_Masonry_Pile_E_Snow_2_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_DM_Rubble_Masonry_Pile_E_Snow2_5 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (903.62695, 4926.524, 529.8696), (0.0, 0.0, -0.0), (2.5083, 2.4127, 1.6183), "DV_BP_DM_Rubble_Masonry_Pile_E_Snow2_5_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_DM_Rubble_Masonry_Pile_E_Snow3_2 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (2376.418, 4714.986, 556.1515), (0.0, 0.0, -0.0), (2.7451, 2.6672, 2.4059), "DV_BP_DM_Rubble_Masonry_Pile_E_Snow3_2_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_DM_Rubble_Masonry_Pile_F_Snow_2 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (1668.2347, 5708.6904, 540.5842), (0.0, 0.0, -0.0), (4.4301, 4.0437, 1.3764), "DV_BP_DM_Rubble_Masonry_Pile_F_Snow_2_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_DM_Rubble_Masonry_Pile_I_Snow_2 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (5316.7817, 5604.593, 400.8713), (0.0, 0.0, -0.0), (4.2166, 2.5443, 1.1909), "DV_BP_DM_Rubble_Masonry_Pile_I_Snow_2_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_DM_Snow_Wagon_Broken_A_2 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (2189.3284, 5352.8994, 513.8897), (0.0, 0.0, -0.0), (5.0238, 3.7350, 0.6234), "DV_BP_DM_Snow_Wagon_Broken_A_2_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_DM_Snow_Wagon_Broken_A2 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (666.24365, 5230.6973, 513.88947), (0.0, 0.0, -0.0), (4.4769, 5.2080, 0.6234), "DV_BP_DM_Snow_Wagon_Broken_A2_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_DM_Snow_Wagon_Broken_A3 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (2375.5593, 3721.6074, 854.0717), (0.0, 0.0, -0.0), (2.9158, 4.6245, 0.8176), "DV_BP_DM_Snow_Wagon_Broken_A3_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_DM_Snow_Wagon_Broken_A4 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (1585.6879, 5038.374, 514.381), (0.0, 0.0, -0.0), (4.8125, 3.2690, 0.7097), "DV_BP_DM_Snow_Wagon_Broken_A4_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_DM_Warehouse_Crate_B_Broken_Breakable_2 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (1802.9487, 4935.92, 539.67737), (0.0, 0.0, -0.0), (1.3458, 1.3600, 0.5490), "DV_BP_DM_Warehouse_Crate_B_Broken_Breakable_2_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_DM_Workshop_Barrel_Broken_Breakable_2 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (726.2037, 5478.9697, 547.2139), (0.0, 0.0, -0.0), (0.8004, 0.9481, 0.8464), "DV_BP_DM_Workshop_Barrel_Broken_Breakable_2_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_DM_Workshop_Scatter_Rope_A_Breakable_2 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (786.6147, 4896.427, 521.91095), (0.0, 0.0, -0.0), (0.5813, 0.5375, 0.2139), "DV_BP_DM_Workshop_Scatter_Rope_A_Breakable_2_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_DM_Workshop_Scatter_Rope_F_Breakable_2 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (1163.9678, 4941.619, 521.2431), (0.0, 0.0, -0.0), (1.2183, 0.8025, 0.2800), "DV_BP_DM_Workshop_Scatter_Rope_F_Breakable_2_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_Expedition_ReturnStone_2 (EMorSimpleShape::Empty)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (5127.3877, 5509.4907, 419.6729), (-0.0, -165.00003487916413, -0.0), (2.0000, 2.0000, 2.0000), "DV_BP_Expedition_ReturnStone_2", _folder)
if a: placed += 1
else: skipped += 1

# ======================================================================
# SUMMARY
# ======================================================================
unreal.log(f"[{BUBBLE_NAME}] Reconstruction complete: {placed} placed, {skipped} skipped, {errors} errors")
