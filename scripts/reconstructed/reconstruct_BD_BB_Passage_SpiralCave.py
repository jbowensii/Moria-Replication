"""Auto-generated level reconstruction script.
Bubble: BD_BB_Passage_SpiralCave
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

BUBBLE_NAME = "BD_BB_Passage_SpiralCave"
placed = 0
skipped = 0
errors = 0

# ======================================================================
# PHASE 1: InstancedMeshCatalog  (static mesh placement)
# ======================================================================
unreal.log(f"[{BUBBLE_NAME}] Phase 1: Placing static meshes...")

# Batch 0: StaticMesh'SM_Grass_Dungeon_03' (3 instances)
_mesh_path = "/Game/Art/Assets/Kits/Deco/Flora/SM_Grass_Dungeon_03"
_materials = ['/Game/Unshippable/ThirdParty/Lordenfel/Environment/Materials/MI_Grass_Dry_No_Wind_01']
_folder = "Reconstruction/BD_BB_Passage_SpiralCave/Meshes"
a = spawn_static_mesh(_mesh_path, _materials, (4841.362, 3215.1206, 605.8089), (25.456597428235604, 0.0, -0.0), (1.0, 1.0, 1.0), "SM_Grass_Dungeon_503", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4121.036, 4002.809, 682.2825), (0.0, 0.0, -33.54543863783732), (1.0, 1.0, 1.0), "SM_Grass_Dungeon_506", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3935.9338, 2748.8965, 637.40155), (0.0, 0.0, -0.0), (1.0, 1.0, 1.0), "SM_Grass_Dungeon_03_500", _folder)
if a: placed += 1
else: skipped += 1

# Batch 1: StaticMesh'SM_Grass_Dungeon_04' (17 instances)
_mesh_path = "/Game/Art/Assets/Kits/Deco/Flora/SM_Grass_Dungeon_04"
_materials = ['/Game/Unshippable/ThirdParty/Lordenfel/Environment/Materials/MI_Grass_Dry_No_Wind_01']
_folder = "Reconstruction/BD_BB_Passage_SpiralCave/Meshes"
a = spawn_static_mesh(_mesh_path, _materials, (4089.943, 2790.0664, 611.1489), (7.0360511877083995, -36.30511577539654, 17.673063207377826), (1.0, 1.0, 1.0), "SM_Grass_Dungeon_5", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3820.7788, 2914.4788, 608.28235), (7.0360506105323175, -59.77743284016979, 17.674059418049808), (1.0, 1.0, 1.0), "SM_Grass_Dungeon_6", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3508.777, 3210.171, 619.0812), (7.0360506105323175, -59.77743284016979, 17.674059418049808), (1.0, 1.0, 1.0), "SM_Grass_Dungeon_7", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3409.192, 3349.6572, 602.1969), (7.0360506105323175, -59.77743284016979, 17.674059418049808), (1.0, 1.0, 1.0), "SM_Grass_Dungeon_8", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3832.2932, 2692.1636, 657.85785), (10.056661478021677, -54.859714640330175, 14.926068406654503), (1.0, 1.0, 1.0), "SM_Grass_Dungeon_9", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4371.1616, 2491.268, 657.85785), (10.056661478021677, -54.859714640330175, 14.926068406654503), (1.0, 1.0, 1.0), "SM_Grass_Dungeon_11", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4761.109, 2454.6245, 657.85785), (11.314288782504578, -58.51641857531665, -0.25134295950889524), (1.0, 1.0, 1.0), "SM_Grass_Dungeon_12", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5021.9697, 3083.6345, 657.85785), (14.381016375737717, -59.271080725281166, -3.225433427852841), (1.0, 1.0, 1.0), "SM_Grass_Dungeon_13", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5065.663, 2727.4338, 726.23737), (29.304008291778946, -64.61556345677675, -8.057126821491982), (1.0, 1.0, 1.0), "SM_Grass_Dungeon_14", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4944.5493, 2521.9749, 726.23737), (19.385792450882008, -72.53570526597419, -33.902464035727135), (1.0, 1.0, 1.0), "SM_Grass_Dungeon_15", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4944.5493, 2331.7356, 726.23737), (19.38578856104871, -25.177305915850567, -33.9025556155406), (1.0, 1.0, 1.0), "SM_Grass_Dungeon_16", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4826.01, 2050.0142, 712.70624), (7.525098509793367, -14.16992167989642, -0.4498291282464821), (1.0, 1.0, 1.0), "SM_Grass_Dungeon_17", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5017.651, 2049.8381, 712.70624), (4.0984683828720545, -14.084196944287834, 0.4170579697690444), (1.0, 1.0, 1.0), "SM_Grass_Dungeon_18", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4826.01, 1878.7992, 735.4021), (1.1405895668525383, -14.010284560366923, 7.898331325589964), (1.0, 1.0, 1.0), "SM_Grass_Dungeon_19", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5017.651, 1878.6232, 767.3404), (4.0984683828720545, -14.084196944287834, 0.4170579697690444), (1.0, 1.0, 1.0), "SM_Grass_Dungeon_20", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4956.452, 1407.6022, 787.56854), (0.056335407535223064, -14.056611813122935, 3.5623164298465473), (1.0, 1.0, 1.0), "SM_Grass_Dungeon_21", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4255.1914, 4101.996, 721.7819), (0.0, 0.0, -16.511932549118363), (1.0, 1.0, 1.0), "SM_Grass_Dungeon_515", _folder)
if a: placed += 1
else: skipped += 1

# Batch 2: StaticMesh'SM_Grass_Dungeon_05' (1 instances)
_mesh_path = "/Game/Art/Assets/Kits/Deco/Flora/SM_Grass_Dungeon_05"
_materials = ['/Game/Unshippable/ThirdParty/Lordenfel/Environment/Materials/MI_Grass_Dry_No_Wind_01']
_folder = "Reconstruction/BD_BB_Passage_SpiralCave/Meshes"
a = spawn_static_mesh(_mesh_path, _materials, (4222.631, 3995.8152, 658.07306), (0.0, 0.0, -13.890655669742427), (1.0, 1.0, 1.0), "SM_Grass_Dungeon_05_512", _folder)
if a: placed += 1
else: skipped += 1

# Batch 3: StaticMesh'SM_Grass_Dungeon_06' (6 instances)
_mesh_path = "/Game/Art/Assets/Kits/Deco/Flora/SM_Grass_Dungeon_06"
_materials = ['/Game/Unshippable/ThirdParty/Lordenfel/Environment/Materials/MI_Grass_Dry_No_Wind_01']
_folder = "Reconstruction/BD_BB_Passage_SpiralCave/Meshes"
a = spawn_static_mesh(_mesh_path, _materials, (4833.311, 3171.2634, 615.89905), (1.015443800373423, 85.79143763483512, 13.541966172974996), (1.0, 1.0, 1.0), "SM_Grass_Dungeon_22", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4841.9023, 3223.5251, 603.16943), (9.513235857990056, -11.835022263017162, 11.769983587921743), (1.0, 1.0, 1.0), "SM_Grass_Dungeon_23", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4485.8926, 2743.9492, 601.0507), (0.0, 0.0, -0.0), (1.0, 1.0, 1.0), "SM_Grass_Dungeon_494", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4471.084, 2628.9858, 627.2253), (0.0, 0.0, -0.0), (1.0, 1.0, 1.0), "SM_Grass_Dungeon_497", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4307.977, 3994.3687, 662.31757), (0.0, 0.0, -0.0), (1.0, 1.0, 1.0), "SM_Grass_Dungeon_509", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4747.504, 2905.1929, 633.2002), (1.015443800373423, 85.79143763483512, 13.541966172974996), (1.0, 1.0, 1.0), "SM_Grass_Dungeon_06_489", _folder)
if a: placed += 1
else: skipped += 1

# Batch 4: StaticMesh'SM_Grass_Dungeon_Low_02' (1 instances)
_mesh_path = "/Game/Art/Assets/Kits/Deco/Flora/SM_Grass_Dungeon_Low_02"
_materials = ['/Game/Unshippable/ThirdParty/Lordenfel/Environment/Materials/MI_Grass_Dry_No_Wind_01']
_folder = "Reconstruction/BD_BB_Passage_SpiralCave/Meshes"
a = spawn_static_mesh(_mesh_path, _materials, (4399.182, 2403.9846, 677.02106), (-8.519500827469495, 1.2938222302052064e-06, 12.56506354702459), (1.0, 1.0, 1.0), "SM_Grass_Dungeon_Low_02_518", _folder)
if a: placed += 1
else: skipped += 1

# Batch 5: StaticMesh'Dirt_Mound_A' (2 instances)
_mesh_path = "/Game/Art/Assets/Kits/Misc/Dirt_Mounds/Dirt_Mound_A"
_materials = ['/Game/Art/Assets/Kits/Misc/Dirt_Mounds/Materials/MI_Mines_Dirt']
_folder = "Reconstruction/BD_BB_Passage_SpiralCave/Meshes"
a = spawn_static_mesh(_mesh_path, _materials, (2495.1548, 4946.9165, 1359.85), (-17.805874140360828, 175.11029268649185, 1.4985757386071228), (1.0, 1.0, 1.0), "Dirt_Mound_A_71", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1899.5892, 5229.083, 1251.455), (-6.592743324745413, -162.67180703196885, -2.051483069094304), (1.0, 0.69148886, 1.4849439), "Dirt_Mound_A2_2", _folder)
if a: placed += 1
else: skipped += 1

# Batch 6: StaticMesh'Dirt_Mound_B' (1 instances)
_mesh_path = "/Game/Art/Assets/Kits/Misc/Dirt_Mounds/Dirt_Mound_B"
_materials = ['/Game/Art/Assets/Kits/Misc/Dirt_Mounds/Materials/MI_Mines_Dirt']
_folder = "Reconstruction/BD_BB_Passage_SpiralCave/Meshes"
a = spawn_static_mesh(_mesh_path, _materials, (3524.2214, 2895.2834, 645.31757), (0.0, -75.15569647667591, 0.0), (1.0, 1.0, 1.2762411), "Dirt_Mound_B_165", _folder)
if a: placed += 1
else: skipped += 1

# Batch 7: StaticMesh'Dirt_Mound_D' (3 instances)
_mesh_path = "/Game/Art/Assets/Kits/Misc/Dirt_Mounds/Dirt_Mound_D"
_materials = ['/Game/Art/Assets/Kits/Misc/Dirt_Mounds/Materials/MI_Mines_Dirt']
_folder = "Reconstruction/BD_BB_Passage_SpiralCave/Meshes"
a = spawn_static_mesh(_mesh_path, _materials, (860.89667, 5561.8765, 3989.0), (0.0, -14.409454560693252, 0.0), (1.0, 1.0, 1.0), "Dirt_Mound_D_18", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5341.1895, 3298.5635, 1996.4921), (0.0, 0.0, -0.0), (1.0, 1.0, 1.1024756), "Dirt_Mound_D4_12", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1588.1527, 1872.695, 4276.149), (0.0, 23.60497552981703, -0.0), (0.30170697, 0.3751362, 0.84935766), "Dirt_Mound_D6_320", _folder)
if a: placed += 1
else: skipped += 1

# Batch 8: StaticMesh'Dirt_Mound_E' (1 instances)
_mesh_path = "/Game/Art/Assets/Kits/Misc/Dirt_Mounds/Dirt_Mound_E"
_materials = ['/Game/Art/Assets/Kits/Misc/Dirt_Mounds/Materials/MI_Mines_Dirt']
_folder = "Reconstruction/BD_BB_Passage_SpiralCave/Meshes"
a = spawn_static_mesh(_mesh_path, _materials, (1643.0, 2847.0, 3994.0), (0.0, 126.38606618852175, -0.0), (1.0, 1.0, 0.2856179), "Dirt_Mound_E_15", _folder)
if a: placed += 1
else: skipped += 1

# Batch 9: StaticMesh'Dirt_Mound_F' (1 instances)
_mesh_path = "/Game/Art/Assets/Kits/Misc/Dirt_Mounds/Dirt_Mound_F"
_materials = ['/Game/Art/Assets/Kits/Misc/Dirt_Mounds/Materials/MI_Mines_Dirt']
_folder = "Reconstruction/BD_BB_Passage_SpiralCave/Meshes"
a = spawn_static_mesh(_mesh_path, _materials, (1497.2852, 4590.4624, 694.426), (-7.599425752126997, -164.8401023097055, 16.935840309983565), (1.0, 1.0, 1.5338347), "Dirt_Mound_F_89", _folder)
if a: placed += 1
else: skipped += 1

# Batch 10: StaticMesh'Dirt_Mound_G' (5 instances)
_mesh_path = "/Game/Art/Assets/Kits/Misc/Dirt_Mounds/Dirt_Mound_G"
_materials = ['/Game/Art/Assets/Kits/Misc/Dirt_Mounds/Materials/MI_Mines_Dirt']
_folder = "Reconstruction/BD_BB_Passage_SpiralCave/Meshes"
a = spawn_static_mesh(_mesh_path, _materials, (3119.0552, 798.0203, 4007.4739), (1.8627072623494891, 110.02607954182761, 0.252485318818553), (0.6925865, 0.8706111, 0.29982626), "Dirt_Mound_D5_36", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3453.9512, 850.43024, 4006.813), (1.8060656870329412, 86.21204069827033, -0.5209960258381796), (0.692586, 0.870611, 0.299826), "Dirt_Mound_D7", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3070.6785, 3295.0046, 671.2315), (-11.125000361495704, 82.9524102112428, -4.712524854885478), (0.5729874, 0.7764377, 1.177536), "Dirt_Mound_G3_25", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1430.0, 3655.0, 3995.0), (0.0, 76.80348332498494, -0.0), (1.0, 1.0, 0.94425213), "Dirt_Mound_G4_38", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2511.6406, 3788.9055, 4010.0), (5.5255723107382426e-08, 146.30663807038374, 2.389204108525533), (1.2846287, 1.3406281, 2.3998091), "Dirt_Mound_G5", _folder)
if a: placed += 1
else: skipped += 1

# Batch 11: StaticMesh'Dirt_Mound_H' (7 instances)
_mesh_path = "/Game/Art/Assets/Kits/Misc/Dirt_Mounds/Dirt_Mound_H"
_materials = ['/Game/Art/Assets/Kits/Misc/Dirt_Mounds/Materials/MI_Mines_Dirt']
_folder = "Reconstruction/BD_BB_Passage_SpiralCave/Meshes"
a = spawn_static_mesh(_mesh_path, _materials, (2108.475, 3200.619, 3993.0), (0.0, -125.60458895475799, 0.0), (0.8584279, 0.98421425, 1.0), "Dirt_Mound_H_12", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3108.4585, 2291.0886, 3328.7117), (0.0, -178.80761160410782, 0.0), (2.0725996, 1.5363336, 1.300268), "Dirt_Mound_H2_51", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3667.0945, 2418.9072, 3328.7117), (0.0, -178.80761160410782, 0.0), (2.0726, 1.536334, 1.300268), "Dirt_Mound_H3", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4245.822, 4751.7905, 1702.595), (0.0, 0.0, -0.0), (1.0, 1.0, 1.0), "Dirt_Mound_H4_59", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4484.472, 4751.7905, 1752.9138), (15.659229812649663, -0.930938746856416, -3.445281735313527), (1.0, 1.0, 1.4274718), "Dirt_Mound_H5", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1727.0533, 1700.1564, 4279.2437), (-4.403595540513583, 95.43933199071327, -11.455750300874497), (1.0, 1.0, 1.0), "Dirt_Mound_H6_317", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3241.0583, 4939.44, 1552.3065), (8.096539507138612, 3.108316026709346e-07, 1.4880135096475673), (1.0, 1.0, 1.0), "Dirt_Mound_H7_80", _folder)
if a: placed += 1
else: skipped += 1

# Batch 12: StaticMesh'Dirt_Mound_I' (37 instances)
_mesh_path = "/Game/Art/Assets/Kits/Misc/Dirt_Mounds/Dirt_Mound_I"
_materials = ['/Game/Art/Assets/Kits/Misc/Dirt_Mounds/Materials/MI_Mines_Dirt']
_folder = "Reconstruction/BD_BB_Passage_SpiralCave/Meshes"
a = spawn_static_mesh(_mesh_path, _materials, (1116.0, 2473.0, 3993.0), (0.0, 0.0, -0.0), (1.0671524, 1.0, 1.075022), "Dirt_Mound_I_2", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5910.0, 5319.0, 3985.0), (0.0, 102.34343022388539, -0.0), (1.1313131, 1.0, 1.0), "Dirt_Mound_I10_36", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5640.0, 4888.0, 3985.0), (0.0, -150.3806202714315, 0.0), (1.131313, 1.0, 1.0), "Dirt_Mound_I11", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5601.7017, 777.724, 3983.482), (0.0, -61.415564306353545, 0.0), (1.334348, 1.334348, 1.4340326), "Dirt_Mound_I12_54", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4948.4805, 903.09656, 4065.769), (21.428380314210425, -16.6838660792782, 45.184531129125496), (1.0, 1.0, 0.809513), "Dirt_Mound_I14", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (6087.1743, 4027.8052, 2492.8833), (6.4828802101920235, -1.385131805133784, -12.66390960995444), (1.287167, 1.1493059, 1.0234267), "Dirt_Mound_I15_6", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (6150.552, 3122.7976, 2347.3264), (9.392641745908994, -0.9270934851065525, -7.606903545356965), (1.0576404, 1.2221235, 1.0), "Dirt_Mound_I16_9", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4256.392, 555.7348, 800.44525), (-0.326843257125709, 3.6628113444230546, 0.23695914673542814), (0.93614364, 0.62098527, 0.20920785), "Dirt_Mound_I17_28", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (442.75104, 5298.4023, 784.29016), (0.0, -88.53441594988443, 0.0), (1.0, 1.0, 1.0), "Dirt_Mound_I18_83", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (870.7642, 5264.1, 784.29016), (0.0, 94.17830390788767, -0.0), (1.0, 1.0, 1.0), "Dirt_Mound_I19", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (854.0, 2645.0, 3993.0), (0.0, -60.000092633621556, 0.0), (1.067152, 1.0, 1.075022), "Dirt_Mound_I2", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1214.1289, 5250.6367, 784.29315), (0.0, 94.17830390788767, -0.0), (1.0, 1.0, 1.0), "Dirt_Mound_I20", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1451.418, 5069.488, 769.6654), (1.7149238779272333, 24.45122114244496, -3.763671641304735), (1.0, 1.0, 1.1463674), "Dirt_Mound_I21", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1867.426, 4415.253, 536.49963), (3.7908844684915923, 101.25402959029748, 0.7538807411237152), (1.2488374, 1.2488374, 2.1820467), "Dirt_Mound_I22_92", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2498.5537, 4207.83, 490.92578), (3.7908845254412316, 101.25402960241549, 0.7538809914470628), (1.248837, 1.248837, 2.182047), "Dirt_Mound_I23", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2978.1248, 4159.2886, 562.06323), (3.7908845254412316, 101.25402960241549, 0.7538809914470628), (1.248837, 1.248837, 2.182047), "Dirt_Mound_I24", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3350.9595, 4079.0098, 579.1071), (3.7908845254412316, 101.25402960241549, 0.7538809914470628), (1.248837, 1.248837, 2.182047), "Dirt_Mound_I25", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4151.4414, 4190.1494, 555.1317), (4.085594636580694, 101.15196380241788, -0.7373351692412481), (1.248837, 1.248837, 2.182047), "Dirt_Mound_I26", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5137.0806, 2424.7827, 665.3833), (4.085594388452971, 17.23697454561893, -0.7373046604506289), (1.248837, 1.248837, 1.2176566), "Dirt_Mound_I27", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5222.0806, 1958.5898, 665.3833), (-0.2928464766641003, 132.72710449529072, -4.790497153563069), (1.248837, 1.248837, 1.217657), "Dirt_Mound_I28", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5230.6885, 1421.5494, 734.381), (4.0855946785082695, -141.32484495880212, -0.7373047381783604), (2.141161, 0.98483, 0.95364994), "Dirt_Mound_I29", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (647.0, 3740.0, 3993.0), (0.0, -60.000092633621556, 0.0), (1.067152, 1.0, 1.075022), "Dirt_Mound_I3", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5204.547, 1069.6802, 751.73785), (1.4211708856769938, -161.77944468382933, -0.048889147876362296), (1.8587377, 1.386633, 0.7805829), "Dirt_Mound_I30", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5270.0674, 402.22748, 751.73785), (1.4211698171060982, -141.26033512042153, -0.04888916791526598), (1.177596, 0.98483, 0.95365), "Dirt_Mound_I31", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3400.403, 1966.841, 751.73785), (1.4211698171060982, -141.26033512042153, -0.04888916791526598), (1.177596, 0.98483, 0.95365), "Dirt_Mound_I32", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3601.7012, 2106.722, 751.73785), (2.9073413175150375, -141.3306917975888, -1.9048157931399505), (0.80262417, 0.70129484, 0.95365), "Dirt_Mound_I33", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (667.1549, 1058.2667, 789.39417), (0.0, 0.0, -0.0), (1.0, 1.0, 1.2492208), "Dirt_Mound_I34_106", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (964.91296, 968.41016, 745.97156), (0.0, 0.0, -0.0), (1.0, 1.0, 1.249221), "Dirt_Mound_I35", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1060.0564, 666.6847, 786.4465), (0.0, 0.0, -0.0), (1.0, 1.0, 1.249221), "Dirt_Mound_I36", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1360.046, 1224.5779, 4406.468), (-9.100279970737832, -8.731351869919946, 6.281488541961219), (1.0, 1.0, 1.0), "Dirt_Mound_I38_350", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (902.0, 3832.1045, 3993.0), (0.0, -60.000092633621556, 0.0), (1.067152, 1.0, 1.075022), "Dirt_Mound_I4", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3199.595, 3829.0796, 4115.0), (0.0, 29.7652375850374, -0.0), (0.9439235, 0.70380205, 0.70380205), "Dirt_Mound_I40_42", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2443.0, 3376.0, 3993.0), (0.0, -60.000092633621556, 0.0), (1.067152, 1.0, 1.075022), "Dirt_Mound_I5", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2702.2034, 5538.0103, 3989.0), (0.0, -89.30583980369892, 0.0), (0.51917046, 0.79117763, 0.25977027), "Dirt_Mound_I6_22", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2413.3875, 5499.2715, 3997.0), (0.0, -44.84206678010493, 0.0), (0.48744565, 0.5887523, 0.14491662), "Dirt_Mound_I7", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4923.0, 5860.0, 3985.0), (0.0, 8.591226872438787, -0.0), (1.0, 1.2549402, 0.692102), "Dirt_Mound_I8_26", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4905.0, 5627.0, 3985.0), (0.0, 8.591226872438787, -0.0), (1.0, 1.25494, 0.692102), "Dirt_Mound_I9", _folder)
if a: placed += 1
else: skipped += 1

# Batch 13: StaticMesh'Mining_Dirt_Mound_B' (3 instances)
_mesh_path = "/Game/Art/Assets/Kits/Misc/Dirt_Mounds/Mining_Dirt_Mound_B"
_materials = ['/Game/Art/Assets/Kits/Misc/Dirt_Mounds/Materials/MI_Mines_Dirt']
_folder = "Reconstruction/BD_BB_Passage_SpiralCave/Meshes"
a = spawn_static_mesh(_mesh_path, _materials, (1481.2151, 2154.4512, 4196.376), (-21.35604860778411, 123.88771723110987, -5.158631357813481), (1.0, 1.0, 2.101874), "Mining_Dirt_Mound_B_323", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1419.1649, 2247.4827, 4150.4624), (-21.35604860778411, 123.88771723110987, -5.158631357813481), (1.0, 1.0, 2.101874), "Mining_Dirt_Mound_B2", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1339.7217, 2347.7036, 4136.0493), (-9.35681198422123, 126.31610705719002, -11.818755990728693), (1.0, 1.0, 2.101874), "Mining_Dirt_Mound_B3", _folder)
if a: placed += 1
else: skipped += 1

# Batch 14: StaticMesh'Suburbs_Dirt_Mound_A' (3 instances)
_mesh_path = "/Game/Art/Assets/Kits/Misc/Dirt_Mounds/Suburbs_Dirt_Mound_A"
_materials = ['/Game/Art/Assets/Kits/Misc/Dirt_Mounds/Materials/MI_Mines_Dirt']
_folder = "Reconstruction/BD_BB_Passage_SpiralCave/Meshes"
a = spawn_static_mesh(_mesh_path, _materials, (4553.653, 1165.5153, 3320.2463), (-4.036925968248178, 0.2459803735937543, -2.753478639467741), (3.3493984, 3.3493984, 2.8114798), "Suburbs_Dirt_Mound_A4_30", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5302.651, 1486.2794, 3494.9294), (3.9147530213589845, 40.58319246800749, 12.784031424724402), (2.225297, 2.225297, 2.8880255), "Suburbs_Dirt_Mound_A5", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5061.343, 1250.7308, 3465.044), (6.410345232362747, 41.022612735020665, 20.357520436025347), (2.225297, 2.225297, 1.2606634), "Suburbs_Dirt_Mound_A6", _folder)
if a: placed += 1
else: skipped += 1

# Batch 15: StaticMesh'Suburbs_Dirt_Mound_A' (3 instances)
_mesh_path = "/Game/Art/Assets/Kits/Misc/Dirt_Mounds/Suburbs_Dirt_Mound_A"
_materials = ['/Game/Art/Assets/Kits/Misc/Dirt_Mounds/Materials/MI_Mines_Dirt']
_folder = "Reconstruction/BD_BB_Passage_SpiralCave/Meshes"
a = spawn_static_mesh(_mesh_path, _materials, (4009.5254, 5047.5376, 3295.1223), (0.0, 0.0, -0.0), (1.9694219, 2.3993597, 1.0109173), "Suburbs_Dirt_Mound_A_25", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4326.74, 4870.559, 3295.1223), (0.0, 0.0, -0.0), (2.7481134, 2.39936, 1.0109178), "Suburbs_Dirt_Mound_A2", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4337.6807, 5099.87, 3354.0518), (0.0, 0.0, -0.0), (1.969422, 2.39936, 2.1215627), "Suburbs_Dirt_Mound_A3", _folder)
if a: placed += 1
else: skipped += 1

# Batch 16: StaticMesh'Suburbs_Dirt_Mound_B' (6 instances)
_mesh_path = "/Game/Art/Assets/Kits/Misc/Dirt_Mounds/Suburbs_Dirt_Mound_B"
_materials = ['/Game/Art/Assets/Kits/Misc/Dirt_Mounds/Materials/MI_Mines_Dirt']
_folder = "Reconstruction/BD_BB_Passage_SpiralCave/Meshes"
a = spawn_static_mesh(_mesh_path, _materials, (3015.3164, 4899.0063, 1517.6322), (16.060929384212642, 0.0, -0.0), (1.9240068, 1.0, 1.4283445), "Suburbs_Dirt_Mound_B_111", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1003.24976, 6283.0195, 3996.0164), (-0.05297849059818585, 100.838097920604, -0.5002440536094859), (4.502958, 1.961616, 1.0), "Suburbs_Dirt_Mound_B13", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3704.537, 5052.1865, 1689.8798), (14.472333654285876, 0.0, -0.0), (1.924007, 1.0, 1.2748181), "Suburbs_Dirt_Mound_B2", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3912.445, 4813.372, 1700.2007), (0.0, 0.0, -0.0), (1.7078068, 1.0, 1.7078068), "Suburbs_Dirt_Mound_B3_119", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3048.3528, 1280.8735, 796.5722), (0.0, 0.0, -0.0), (2.5810373, 2.5810373, 1.0), "Suburbs_Dirt_Mound_B4_139", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2839.2559, 1338.1421, 796.5722), (0.0, -65.14898724845315, 0.0), (2.581037, 2.581037, 1.0), "Suburbs_Dirt_Mound_B5", _folder)
if a: placed += 1
else: skipped += 1

# Batch 17: StaticMesh'Suburbs_Dirt_Mound_C' (9 instances)
_mesh_path = "/Game/Art/Assets/Kits/Misc/Dirt_Mounds/Suburbs_Dirt_Mound_C"
_materials = ['/Game/Art/Assets/Kits/Misc/Dirt_Mounds/Materials/MI_Mines_Dirt']
_folder = "Reconstruction/BD_BB_Passage_SpiralCave/Meshes"
a = spawn_static_mesh(_mesh_path, _materials, (4194.418, 4588.2305, 1695.2086), (0.0, -134.7726884678193, 0.0), (1.77262, 1.0, 1.0), "Suburbs_Dirt_Mound_C13", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3845.743, 4219.2207, 1694.3589), (0.0, 26.214419626689505, -0.0), (1.77262, 1.0, 1.5297368), "Suburbs_Dirt_Mound_C14", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3554.603, 4299.914, 1671.7651), (2.438828215664389, -72.86755773012345, -7.859832317552113), (1.77262, 1.0, 2.2390056), "Suburbs_Dirt_Mound_C15", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3386.6348, 4306.072, 1631.7699), (-17.47332679969623, 160.895019912602, 0.9876152288223496), (1.77262, 1.0, 2.239006), "Suburbs_Dirt_Mound_C16", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3754.1519, 4958.4136, 1689.8866), (15.701511295720294, 0.0, -0.0), (1.3030497, 1.6334859, 1.3705361), "Suburbs_Dirt_Mound_C17_115", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3754.1519, 5023.464, 1699.595), (17.501137824515528, 0.0, -0.0), (1.30305, 1.633486, 1.2657971), "Suburbs_Dirt_Mound_C18", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1815.3629, 4876.126, 1230.3503), (5.107376077437353, 11.679491842386886, -1.192474430553664), (2.940886, 4.0410604, 1.4801056), "Suburbs_Dirt_Mound_C19_122", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1744.542, 5068.9844, 1234.1162), (4.754494370119828, -0.18377685419442139, -2.215820072280236), (2.15517, 2.15517, 1.079537), "Suburbs_Dirt_Mound_C20", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2025.8497, 4568.6504, 1236.0278), (3.684101779262051, 70.29231187905165, 3.7349034597834834), (2.940886, 5.0862074, 1.480106), "Suburbs_Dirt_Mound_C21", _folder)
if a: placed += 1
else: skipped += 1

# Batch 18: StaticMesh'Suburbs_Dirt_Mound_C' (2 instances)
_mesh_path = "/Game/Art/Assets/Kits/Misc/Dirt_Mounds/Suburbs_Dirt_Mound_C"
_materials = ['/Game/Art/Assets/Kits/Misc/Dirt_Mounds/Materials/MI_Mines_Dirt']
_folder = "Reconstruction/BD_BB_Passage_SpiralCave/Meshes"
a = spawn_static_mesh(_mesh_path, _materials, (4007.3477, 4473.7896, 1695.2086), (0.0, 26.214419626689505, -0.0), (1.7726203, 1.0, 1.0), "Suburbs_Dirt_Mound_C11_63", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4063.941, 4362.5493, 1695.2086), (0.0, 62.21966946665327, -0.0), (1.77262, 1.0, 1.0), "Suburbs_Dirt_Mound_C12", _folder)
if a: placed += 1
else: skipped += 1

# Batch 19: StaticMesh'SM_Grass_Low_01' (1 instances)
_mesh_path = "/Game/Unshippable/ThirdParty/Lordenfel/Environment/Vegetation/Meshes/SM_Grass_Low_01"
_materials = ['/Game/Art/Assets/Kits/Misc/Vegetation/Materials/MI_Grass_03']
_folder = "Reconstruction/BD_BB_Passage_SpiralCave/Meshes"
a = spawn_static_mesh(_mesh_path, _materials, (3958.617, 2682.6118, 661.9791), (-10.114044645432584, 0.0, -0.0), (1.0, 1.0, 1.0), "SM_Grass_Low_01_521", _folder)
if a: placed += 1
else: skipped += 1

# Batch 20: StaticMesh'SM_Grass_Low_Dry_03' (3 instances)
_mesh_path = "/Game/Unshippable/ThirdParty/Lordenfel/Environment/Vegetation/Meshes/SM_Grass_Low_Dry_03"
_materials = ['/Game/Art/Assets/Kits/Deco/Flora/Materials/MI_Grass_Mushroom']
_folder = "Reconstruction/BD_BB_Passage_SpiralCave/Meshes"
a = spawn_static_mesh(_mesh_path, _materials, (1898.5094, 4248.2397, 679.4859), (-30.218140390623578, -66.90308032878664, -11.902984925431841), (1.0, 1.0, 1.0), "SM_Grass_Low_Dry_5", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1898.5094, 4248.2397, 681.29376), (0.0, 0.0, -34.972624281026036), (1.0, 1.0, 1.0), "SM_Grass_Low_Dry_646", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4867.7017, 3191.683, 619.40765), (18.33909002290836, 5.590439717059958, 17.280906308128557), (1.0, 1.0, 1.0), "SM_Grass_Low_Dry_03_618", _folder)
if a: placed += 1
else: skipped += 1

# Batch 21: StaticMesh'SM_Grass_Patch_01' (4 instances)
_mesh_path = "/Game/Unshippable/ThirdParty/Lordenfel/Environment/Vegetation/Meshes/SM_Grass_Patch_01"
_materials = ['/Game/Unshippable/ThirdParty/Lordenfel/Environment/Materials/MI_Grass_Dry_01']
_folder = "Reconstruction/BD_BB_Passage_SpiralCave/Meshes"
a = spawn_static_mesh(_mesh_path, _materials, (4240.7095, 3968.6838, 660.52673), (-25.574248329206213, -34.30773773598346, -16.13979806702147), (1.0, 1.0, 1.0), "SM_Grass_Patch_2", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4296.6064, 4032.7185, 698.0352), (-25.574248329206213, -34.30773773598346, -16.13979806702147), (1.0, 1.0, 1.0), "SM_Grass_Patch_3", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4132.935, 4032.7185, 706.8284), (-25.574248329206213, -34.30773773598346, -16.13979806702147), (1.0, 1.0, 1.0), "SM_Grass_Patch_4", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4144.7676, 3968.6838, 659.20447), (0.0, 0.0, -23.10357615278704), (1.0, 1.0, 1.0), "SM_Grass_Patch_01_536", _folder)
if a: placed += 1
else: skipped += 1

# Batch 22: StaticMesh'SM_Grass_Patch_07' (8 instances)
_mesh_path = "/Game/Unshippable/ThirdParty/Lordenfel/Environment/Vegetation/Meshes/SM_Grass_Patch_07"
_materials = ['/Game/Unshippable/ThirdParty/Lordenfel/Environment/Materials/MI_Grass_Dry_01']
_folder = "Reconstruction/BD_BB_Passage_SpiralCave/Meshes"
a = spawn_static_mesh(_mesh_path, _materials, (3246.993, 3751.9443, 572.2228), (0.0, -30.257201405774158, 0.0), (1.0, 1.0, 1.0), "SM_Grass_Patch_15", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3107.1072, 3839.003, 572.2228), (0.0, -30.257201405774158, 0.0), (1.0, 1.0, 1.0), "SM_Grass_Patch_16", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2835.8604, 3876.8652, 572.2228), (0.0, -21.362180549534173, 0.0), (1.0, 1.0, 1.0), "SM_Grass_Patch_17", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2431.7927, 4002.161, 572.2228), (0.0, -21.362180549534173, 0.0), (1.0, 1.0, 1.0), "SM_Grass_Patch_18", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2627.9614, 3962.0952, 578.3033), (0.0, -21.362180549534173, 0.0), (1.0, 1.0, 1.0), "SM_Grass_Patch_19", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1124.2517, 3127.379, 585.07007), (0.5302143810101521, -93.66970717894185, 8.211303299578036), (1.0, 1.0, 1.0), "SM_Grass_Patch_26", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1108.4635, 3310.438, 585.07007), (0.5302143810101521, -93.66970717894185, 8.211303299578036), (1.0, 1.0, 1.0), "SM_Grass_Patch_27", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3431.5776, 3742.487, 572.2228), (0.0, 0.0, -0.0), (1.0, 1.0, 1.0), "SM_Grass_Patch_549", _folder)
if a: placed += 1
else: skipped += 1

# Batch 23: StaticMesh'SM_Grass_Patch_08' (26 instances)
_mesh_path = "/Game/Unshippable/ThirdParty/Lordenfel/Environment/Vegetation/Meshes/SM_Grass_Patch_08"
_materials = ['/Game/Unshippable/ThirdParty/Lordenfel/Environment/Materials/MI_Grass_Dry_01']
_folder = "Reconstruction/BD_BB_Passage_SpiralCave/Meshes"
a = spawn_static_mesh(_mesh_path, _materials, (3850.9, 2873.1433, 609.45624), (0.0, 0.0, 17.349586263471096), (1.0, 1.0, 1.0), "SM_Grass_Patch_9", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4736.1123, 2918.591, 609.45624), (9.35084189957073, -0.36703494831618066, 15.092677511205023), (1.0, 1.0, 1.0), "SM_Grass_Patch_10", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4930.5054, 3195.3113, 609.45624), (17.132287350951334, 1.8699515867714138, 22.645082513768067), (1.0, 1.0, 1.0), "SM_Grass_Patch_11", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4774.6797, 3070.247, 600.245), (23.68901459107016, -62.309532189128376, -10.489834080617857), (1.0, 1.0, 1.0), "SM_Grass_Patch_12", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4491.1274, 2746.3992, 591.07495), (12.007049021424482, -77.61895975464459, -0.6997675468099095), (1.0, 1.0, 1.0), "SM_Grass_Patch_13", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4644.043, 2882.4932, 591.07495), (12.551024993435659, -87.71844682685239, -10.315063109977508), (1.0, 1.0, 1.0), "SM_Grass_Patch_14", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1261.768, 3980.534, 597.562), (-19.75582951854982, 8.605954437631274, -19.40402379503272), (1.0, 1.0, 1.0), "SM_Grass_Patch_20", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1365.0466, 4155.08, 609.4563), (9.795449675737627, 91.8469247240961, -18.436095214291775), (1.0, 1.0, 1.0), "SM_Grass_Patch_21", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1609.7858, 4238.6055, 603.24176), (41.268077165669666, 63.73558939710497, -5.94394235699984), (1.0, 1.0, 1.0), "SM_Grass_Patch_22", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1972.3513, 4194.7817, 614.079), (38.54338479383849, 59.518098434609364, -12.512695733775278), (1.0, 1.0, 1.0), "SM_Grass_Patch_23", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1801.8259, 4167.011, 594.76483), (38.54338479383849, 59.518098434609364, -12.512695733775278), (1.0, 1.0, 1.0), "SM_Grass_Patch_24", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1151.0663, 3858.681, 596.5871), (-12.794310697073952, -105.26661438191401, 26.710537746297685), (1.0, 1.0, 1.0), "SM_Grass_Patch_25", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1229.7253, 2520.392, 593.94696), (-15.945068695816031, -0.7492981175633419, 5.488964140297017), (1.0, 1.0, 1.0), "SM_Grass_Patch_28", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1407.231, 2498.4282, 593.94696), (24.2035618720229, -0.7898557846940596, 4.959362283028525), (1.0, 1.0, 1.0), "SM_Grass_Patch_29", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1301.4674, 2378.4612, 595.70245), (0.0, 0.0, 8.459485057708035), (1.0, 1.0, 1.0), "SM_Grass_Patch_30", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1856.2062, 4272.4062, 661.8201), (38.54338479383849, 59.518098434609364, -12.512695733775278), (1.0, 1.0, 1.0), "SM_Grass_Patch_31", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1938.144, 4258.5474, 644.21466), (-10.917418847581308, -26.564514473741895, -28.61871205275901), (1.0, 1.0, 1.0), "SM_Grass_Patch_32", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1180.9077, 2179.0278, 618.02924), (7.598038584204756e-07, -64.1045034944383, 8.46034701177696), (1.0, 1.0, 1.0), "SM_Grass_Patch_35", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1600.0118, 2323.4883, 645.6861), (9.018144779463825, -0.3373413173927665, 6.308411233195753), (1.0, 1.0, 1.0), "SM_Grass_Patch_36", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1752.7206, 2740.2212, 661.8946), (17.87846979319795, -64.0369507511356, -10.70925867989175), (1.0, 1.0, 1.0), "SM_Grass_Patch_37", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1721.4009, 2610.6135, 670.6419), (18.67485020382188, -2.343841390930596, 0.7999766514648908), (1.0, 1.0, 1.0), "SM_Grass_Patch_38", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1659.2125, 2450.8845, 659.4462), (1.804584266283467, 76.30331962027009, 16.07562413396103), (1.0, 1.0, 1.0), "SM_Grass_Patch_39", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1957.9856, 3173.6062, 652.42957), (26.68676624438493, -62.204311926032794, -5.892059186102972), (1.0, 1.0, 1.0), "SM_Grass_Patch_40", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1926.6658, 3047.4153, 659.2899), (18.78979393563076, 1.011466994426557, 11.222322065541809), (1.0, 1.0, 1.0), "SM_Grass_Patch_41", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2048.933, 3259.4492, 652.42957), (1.7897491193439696, -139.445133914789, -26.627293365768), (1.0, 1.0, 1.0), "SM_Grass_Patch_42", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4099.217, 2819.6672, 599.59766), (0.0, 0.0, 17.349586263471096), (1.0, 1.0, 1.0), "SM_Grass_Patch_08_524", _folder)
if a: placed += 1
else: skipped += 1

# Batch 24: StaticMesh'SM_Grass_Patch_08' (2 instances)
_mesh_path = "/Game/Unshippable/ThirdParty/Lordenfel/Environment/Vegetation/Meshes/SM_Grass_Patch_08"
_materials = ['/Game/Art/Assets/Kits/Deco/Flora/Materials/MI_Grass_Mushroom']
_folder = "Reconstruction/BD_BB_Passage_SpiralCave/Meshes"
a = spawn_static_mesh(_mesh_path, _materials, (1112.3734, 3852.3735, 582.7078), (7.950926520414835, 179.92016884071117, 22.594294929559197), (1.0, 1.0, 1.0), "SM_Grass_Patch_33", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1213.1469, 3936.9297, 556.4223), (16.993357592990108, 105.5141857316748, -4.530486883842789), (1.0, 1.0, 1.0), "SM_Grass_Patch_34", _folder)
if a: placed += 1
else: skipped += 1

# Batch 25: StaticMesh'SM_Grass_Patch_Dry_01' (16 instances)
_mesh_path = "/Game/Unshippable/ThirdParty/Lordenfel/Environment/Vegetation/Meshes/SM_Grass_Patch_Dry_01"
_materials = ['/Game/Unshippable/ThirdParty/Lordenfel/Environment/Materials/MI_Grass_Dry_01']
_folder = "Reconstruction/BD_BB_Passage_SpiralCave/Meshes"
a = spawn_static_mesh(_mesh_path, _materials, (3666.4934, 3921.1643, 647.57355), (0.0, 75.3083602938673, -0.0), (1.0, 1.0, 1.0), "SM_Grass_Patch_Dry_2", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3569.4878, 3883.5894, 647.57355), (0.0, 30.763081679763996, -0.0), (1.0, 1.0, 1.0), "SM_Grass_Patch_Dry_3", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3474.377, 3883.5894, 656.01605), (7.331880461067264, 29.960375000828133, -12.484070950389425), (1.0, 1.0, 1.0), "SM_Grass_Patch_Dry_4", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3536.5872, 3901.6309, 662.82605), (7.331881155467041, 29.960373345730854, -12.484070503411129), (1.0, 1.0, 1.0), "SM_Grass_Patch_Dry_5", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1263.8588, 2142.4644, 629.72034), (0.0, 54.42527246206318, -0.0), (1.0, 1.0, 1.0), "SM_Grass_Patch_Dry_9", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3610.7483, 2830.7886, 659.80237), (0.0, -67.860259407175, 0.0), (1.0, 1.0, 1.0), "SM_Grass_Patch_Dry_16", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3603.8677, 2772.1443, 659.80237), (0.0, -67.860259407175, 0.0), (1.0, 1.0, 1.0), "SM_Grass_Patch_Dry_17", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3606.3892, 2756.5022, 659.80237), (0.0, -127.81312820962374, 0.0), (1.0, 1.0, 1.0), "SM_Grass_Patch_Dry_18", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4684.524, 2034.8315, 697.0168), (0.0, 0.0, -0.0), (1.0, 1.0, 1.0), "SM_Grass_Patch_Dry_20", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2293.8787, 3290.338, 732.89484), (11.164040080888553, -36.366946713194004, 14.732217414380889), (1.0, 1.0, 1.0), "SM_Grass_Patch_Dry_48", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2226.7527, 3390.4983, 639.5217), (11.494503420269911, -36.27651762500795, 15.190853796634668), (1.0, 1.0, 1.0), "SM_Grass_Patch_Dry_49", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1263.8588, 2223.4976, 629.72034), (0.0, 0.0, -0.0), (1.0, 1.0, 1.0), "SM_Grass_Patch_Dry_572", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3592.7556, 2855.7195, 659.80237), (0.0, 0.0, -0.0), (1.0, 1.0, 1.0), "SM_Grass_Patch_Dry_593", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4954.4775, 2184.4492, 697.0168), (0.0, 0.0, -0.0), (1.0, 1.0, 1.0), "SM_Grass_Patch_Dry_599", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2335.582, 3269.8564, 744.35565), (0.0, -37.81518617548419, 0.0), (1.0, 1.0, 1.0), "SM_Grass_Patch_Dry_704", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3628.4048, 3905.3318, 647.57355), (0.0, 0.0, -0.0), (1.0, 1.0, 1.0), "SM_Grass_Patch_Dry_01_542", _folder)
if a: placed += 1
else: skipped += 1

# Batch 26: StaticMesh'SM_Grass_Patch_Dry_01' (21 instances)
_mesh_path = "/Game/Unshippable/ThirdParty/Lordenfel/Environment/Vegetation/Meshes/SM_Grass_Patch_Dry_01"
_materials = ['/Game/Art/Assets/Kits/Deco/Flora/Materials/MI_Grass_Mushroom']
_folder = "Reconstruction/BD_BB_Passage_SpiralCave/Meshes"
a = spawn_static_mesh(_mesh_path, _materials, (3983.9634, 2866.371, 594.20215), (-2.275360310219331, 62.91063205330257, 8.09849971397958), (1.0, 1.0, 1.0), "SM_Grass_Patch_Dry_22", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3796.268, 2987.351, 591.3944), (-16.933009564736256, 61.59903882469872, 15.885829217896951), (1.0, 1.0, 1.0), "SM_Grass_Patch_Dry_23", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3937.4983, 2764.773, 627.72064), (-6.5748289358927785, 6.1145066806493285, 9.89658566904133), (1.0, 1.0, 1.0), "SM_Grass_Patch_Dry_24", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1939.5746, 4144.4214, 598.5641), (26.939628126655023, 107.80811176201374, -0.3581231213078671), (1.0, 1.0, 1.0), "SM_Grass_Patch_Dry_29", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2011.0814, 4175.306, 598.5641), (23.529142659577314, 113.26292990120118, 12.62496703281587), (1.0, 1.0, 1.0), "SM_Grass_Patch_Dry_30", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1972.7186, 4133.1865, 576.07605), (10.910537471966652, 41.06861738160726, 5.322392217422704), (1.0, 1.0, 1.0), "SM_Grass_Patch_Dry_31", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1452.9216, 4197.4893, 576.07605), (10.910537471966652, 41.06861738160726, 5.322392217422704), (1.0, 1.0, 1.0), "SM_Grass_Patch_Dry_32", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1411.1465, 4173.0938, 576.07605), (10.91053708576297, -45.98931774967336, 5.322567185127133), (1.0, 1.0, 1.0), "SM_Grass_Patch_Dry_33", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1547.5544, 4251.4688, 576.07605), (-1.9341737869706217, -46.950442228846825, -6.8458249906270465), (1.0, 1.0, 1.0), "SM_Grass_Patch_Dry_34", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1547.5544, 4251.4688, 576.07605), (-1.9340511169858956, -108.60877560015044, -6.845823842493245), (1.0, 1.0, 1.0), "SM_Grass_Patch_Dry_35", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1648.9786, 4251.4688, 598.12665), (-20.520354877440216, -109.90915926386769, -0.2614123383389594), (1.0, 1.0, 1.0), "SM_Grass_Patch_Dry_36", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1625.9401, 4237.2285, 584.49335), (-20.52007929152934, -163.0153123319927, -0.26138310801863984), (1.0, 1.0, 1.0), "SM_Grass_Patch_Dry_37", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1892.4941, 4198.0356, 622.91296), (-25.349304843683186, -55.37606826093558, -7.297424935870559), (1.0, 1.0, 1.0), "SM_Grass_Patch_Dry_38", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1101.4827, 3143.6885, 596.35144), (14.025668056167934, -75.72277610126643, 20.797071895864775), (1.0, 1.0, 1.0), "SM_Grass_Patch_Dry_40", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1526.1022, 2764.7659, 612.99023), (12.876921199854968, 51.431311318629874, 7.8576536575393225), (1.0, 1.0, 1.0), "SM_Grass_Patch_Dry_44", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1588.5237, 2764.7659, 634.60785), (4.1486905572343, 174.80982928378194, 11.82839869249854), (1.0, 1.0, 1.0), "SM_Grass_Patch_Dry_45", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1511.4036, 2838.854, 607.7742), (4.148690947466598, 174.80982886524384, 11.828398666400545), (1.0, 1.0, 1.0), "SM_Grass_Patch_Dry_46", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4192.133, 2802.6558, 594.20215), (0.0, 0.0, 13.502641128596323), (1.0, 1.0, 1.0), "SM_Grass_Patch_Dry_603", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1892.4941, 4144.4214, 598.2522), (0.0, 0.0, -26.294157826000816), (1.0, 1.0, 1.0), "SM_Grass_Patch_Dry_634", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1132.6946, 3109.8887, 591.6557), (-16.434388307134217, 0.7764450527763846, -0.2629089413151584), (1.0, 1.0, 1.0), "SM_Grass_Patch_Dry_656", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1439.7588, 2873.2002, 584.54675), (12.876921199854968, 51.431311318629874, 7.8576536575393225), (1.0, 1.0, 1.0), "SM_Grass_Patch_Dry_687", _folder)
if a: placed += 1
else: skipped += 1

# Batch 27: StaticMesh'SM_Grass_Patch_Dry_02' (3 instances)
_mesh_path = "/Game/Unshippable/ThirdParty/Lordenfel/Environment/Vegetation/Meshes/SM_Grass_Patch_Dry_02"
_materials = ['/Game/Unshippable/ThirdParty/Lordenfel/Environment/Materials/MI_Grass_Dry_01']
_folder = "Reconstruction/BD_BB_Passage_SpiralCave/Meshes"
a = spawn_static_mesh(_mesh_path, _materials, (3198.6526, 3382.5054, 603.0552), (0.0, 0.0, -0.0), (1.0, 1.0, 1.0), "SM_Grass_Patch_Dry_14", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2023.0404, 3157.14, 681.7789), (33.46189650922701, 5.6330251081734515, 22.758590150648885), (1.0, 1.0, 1.0), "SM_Grass_Patch_Dry_701", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3237.8706, 3387.311, 595.01), (0.0, 0.0, -0.0), (1.0, 1.0, 1.0), "SM_Grass_Patch_Dry_02_589", _folder)
if a: placed += 1
else: skipped += 1

# Batch 28: StaticMesh'SM_Grass_Patch_Dry_02' (1 instances)
_mesh_path = "/Game/Unshippable/ThirdParty/Lordenfel/Environment/Vegetation/Meshes/SM_Grass_Patch_Dry_02"
_materials = ['/Game/Art/Assets/Kits/Deco/Flora/Materials/MI_Grass_Mushroom']
_folder = "Reconstruction/BD_BB_Passage_SpiralCave/Meshes"
a = spawn_static_mesh(_mesh_path, _materials, (4471.9707, 2772.79, 580.1296), (0.0, 0.0, -0.0), (1.0, 1.0, 1.0), "SM_Grass_Patch_Dry_609", _folder)
if a: placed += 1
else: skipped += 1

# Batch 29: StaticMesh'SM_Grass_Patch_Dry_03' (2 instances)
_mesh_path = "/Game/Unshippable/ThirdParty/Lordenfel/Environment/Vegetation/Meshes/SM_Grass_Patch_Dry_03"
_materials = ['/Game/Art/Assets/Kits/Deco/Flora/Materials/MI_Grass_Mushroom']
_folder = "Reconstruction/BD_BB_Passage_SpiralCave/Meshes"
a = spawn_static_mesh(_mesh_path, _materials, (1463.4434, 2751.0422, 590.11847), (-19.979765395927096, 138.80091365954058, 2.790882548954847), (1.0, 1.0, 1.0), "SM_Grass_Patch_Dry_42", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1474.6903, 2809.6848, 592.38556), (22.918882487273525, -4.273864939071373, -0.38034058699668655), (1.0, 1.0, 1.0), "SM_Grass_Patch_Dry_03_679", _folder)
if a: placed += 1
else: skipped += 1

# Batch 30: StaticMesh'SM_Grass_Patch_Dry_05' (3 instances)
_mesh_path = "/Game/Unshippable/ThirdParty/Lordenfel/Environment/Vegetation/Meshes/SM_Grass_Patch_Dry_05"
_materials = ['/Game/Art/Assets/Kits/Deco/Flora/Materials/MI_Grass_Mushroom']
_folder = "Reconstruction/BD_BB_Passage_SpiralCave/Meshes"
a = spawn_static_mesh(_mesh_path, _materials, (1222.3447, 2184.9546, 607.4943), (0.0, 0.0, 15.97496355456387), (1.0, 1.0, 1.0), "SM_Grass_Patch_Dry_43", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1297.0444, 2481.9656, 594.49023), (0.0, 0.0, 15.97496355456387), (1.0, 1.0, 1.0), "SM_Grass_Patch_Dry_666", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4708.599, 2943.8093, 599.90765), (7.864956130572569, 38.070637311446944, 12.7204378944409), (1.0, 1.0, 1.0), "SM_Grass_Patch_Dry_05_612", _folder)
if a: placed += 1
else: skipped += 1

# Batch 31: StaticMesh'SM_Grass_Patch_Dry_06' (5 instances)
_mesh_path = "/Game/Unshippable/ThirdParty/Lordenfel/Environment/Vegetation/Meshes/SM_Grass_Patch_Dry_06"
_materials = ['/Game/Unshippable/ThirdParty/Lordenfel/Environment/Materials/MI_Grass_Dry_01']
_folder = "Reconstruction/BD_BB_Passage_SpiralCave/Meshes"
a = spawn_static_mesh(_mesh_path, _materials, (2252.5654, 3448.4043, 577.65546), (0.0, 27.595308885877536, -0.0), (1.0, 1.0, 1.0), "SM_Grass_Patch_Dry_10", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2625.714, 3531.9558, 577.65546), (0.0, 57.11603335239412, -0.0), (1.0, 1.0, 1.0), "SM_Grass_Patch_Dry_11", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2559.994, 3514.0618, 577.65546), (0.0, 9.974308011606801, -0.0), (1.0, 1.0, 1.0), "SM_Grass_Patch_Dry_12", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2974.4656, 3462.5488, 577.65546), (0.0, -1.6818848435339684, 0.0), (1.0, 1.0, 1.0), "SM_Grass_Patch_Dry_13", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2145.6316, 3437.9614, 577.65546), (0.0, 0.0, -0.0), (1.0, 1.0, 1.0), "SM_Grass_Patch_Dry_06_579", _folder)
if a: placed += 1
else: skipped += 1

# Batch 32: StaticMesh'SM_Grass_Patch_Dry_06' (2 instances)
_mesh_path = "/Game/Unshippable/ThirdParty/Lordenfel/Environment/Vegetation/Meshes/SM_Grass_Patch_Dry_06"
_materials = ['/Game/Art/Assets/Kits/Deco/Flora/Materials/MI_Grass_Mushroom']
_folder = "Reconstruction/BD_BB_Passage_SpiralCave/Meshes"
a = spawn_static_mesh(_mesh_path, _materials, (4039.5647, 2838.993, 588.6629), (-19.00055030173873, 131.68787708786792, -13.539885209473091), (1.0, 1.0, 1.0), "SM_Grass_Patch_Dry_27", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3964.1555, 2821.8948, 606.17645), (-9.802644036671785, 65.83311064693174, 10.68047924580128), (1.0, 1.0, 1.0), "SM_Grass_Patch_Dry_630", _folder)
if a: placed += 1
else: skipped += 1

# Batch 33: StaticMesh'SM_Grass_Patch_Dry_07' (1 instances)
_mesh_path = "/Game/Unshippable/ThirdParty/Lordenfel/Environment/Vegetation/Meshes/SM_Grass_Patch_Dry_07"
_materials = ['/Game/Unshippable/ThirdParty/Lordenfel/Environment/Materials/MI_Grass_Dry_01']
_folder = "Reconstruction/BD_BB_Passage_SpiralCave/Meshes"
a = spawn_static_mesh(_mesh_path, _materials, (3141.2397, 3431.9902, 569.9345), (0.0, -15.612121459902964, 0.0), (1.0, 1.0, 1.0), "SM_Grass_Patch_Dry_07_586", _folder)
if a: placed += 1
else: skipped += 1

# Batch 34: StaticMesh'PWM_Quarry_1x1x1_A' (155 instances)
_mesh_path = "/Game/Unshippable/Whitebox/Rocks/Meshes/PWM_Quarry_1x1x1_A"
_materials = ['/Game/Environments/ProcTexturing/ProcMaterial_Quarry_Atlas_1']
_folder = "Reconstruction/BD_BB_Passage_SpiralCave/Meshes"
a = spawn_static_mesh(_mesh_path, _materials, (4420.0, 3420.0, 1930.0), (10.908652855668302, 165.6730685599306, -2.7670596784718926), (1.0, 1.0, 1.0), "PWM_Quarry_1x1x1_A_13", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1087.6396, 61.01706, 2437.8723), (0.0, 0.0, -0.0), (1.0, 1.0, 1.0), "PWM_Quarry_1x1x1_A10", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1016.9424, 1052.291, 2200.1458), (-6.131194329742747, 88.5529006884196, 174.5294063164929), (1.3196216, 1.2701243, 1.6393057), "PWM_Quarry_1x1x1_A11_138", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4915.4424, 4215.117, 1388.0103), (0.0, -30.059969628677297, 0.0), (1.2419213, 1.2419213, 1.2419213), "PWM_Quarry_1x1x1_A12_167", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4905.5654, 4246.2466, 1692.1558), (0.0, 22.248541127080973, -0.0), (1.5458745, 1.5458745, 1.5458745), "PWM_Quarry_1x1x1_A13_170", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5004.8364, 3836.8647, 1870.9117), (0.0, 32.58789520282929, -0.0), (1.5144856, 1.0, 1.0), "PWM_Quarry_1x1x1_A14_179", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5103.325, 4181.151, 3924.9001), (-4.273099580250258, -131.44322689192188, 173.00220936571782), (1.662738, 1.662738, 1.91218), "PWM_Quarry_1x1x1_A149_212", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2828.4517, 2493.116, 626.29016), (18.444438064155683, -128.59116388827317, -171.65917058963228), (1.662738, 1.662738, 1.91218), "PWM_Quarry_1x1x1_A149_642", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4955.7583, 3836.8647, 1787.261), (0.0, 32.58789520282929, -0.0), (1.514486, 1.0, 1.0), "PWM_Quarry_1x1x1_A15", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (315.4567, 3579.882, 642.00494), (22.58501250483064, -148.70976648565633, -175.57249814170854), (1.481873, 1.481873, 2.056834), "PWM_Quarry_1x1x1_A150_11", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3285.6648, 522.37427, 617.9349), (43.94795441947072, -123.53968754833774, -153.146184540869), (1.481873, 1.481873, 2.056834), "PWM_Quarry_1x1x1_A150_75", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5158.162, 4335.584, 3938.157), (1.195147981890154, -150.07850013436038, -179.62618183901435), (1.481873, 1.481873, 2.056834), "PWM_Quarry_1x1x1_A150_213", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2876.6404, 2647.1782, 595.06537), (27.52787863942155, -147.26422601620607, -172.16333543952675), (1.481873, 1.481873, 2.056834), "PWM_Quarry_1x1x1_A150_643", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4919.7007, 1727.6052, 3120.9111), (4.862563123135765, -16.994721118380262, 178.87101315565295), (1.316265, 1.186616, 1.186616), "PWM_Quarry_1x1x1_A153", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2762.9165, 2492.7173, 3120.9111), (4.862572073842636, 103.94293805082374, 178.87101333444406), (1.316265, 1.186616, 1.186616), "PWM_Quarry_1x1x1_A154", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2583.0757, 1338.8352, 3011.424), (-2.3782348664964803, -117.92228871745787, -2.4504396615470125), (1.316265, 1.186616, 1.186616), "PWM_Quarry_1x1x1_A155", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3835.5532, 2510.6692, 2994.5347), (-3.232086207255987, 126.3822807875771, 3.805774964299055), (1.316265, 1.186616, 1.186616), "PWM_Quarry_1x1x1_A156", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (590.72125, 3156.512, 718.4976), (21.110869583615823, -54.22735676437536, -177.697921031821), (1.662738, 1.662738, 1.91218), "PWM_Quarry_1x1x1_A156_40", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3646.1245, 168.84946, 540.77905), (1.936306761080849, -37.32944561630175, -156.4287781503837), (1.662738, 1.662738, 1.91218), "PWM_Quarry_1x1x1_A156_104", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5396.8716, 3798.308, 4037.6055), (25.263713614999784, -64.01738798984948, 159.04329154767257), (1.662738, 1.662738, 1.91218), "PWM_Quarry_1x1x1_A156_242", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3158.249, 2123.808, 643.21423), (17.634442425715395, -52.580812828269224, -172.73907737337228), (1.662738, 1.662738, 1.91218), "PWM_Quarry_1x1x1_A156_672", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2266.4583, 4380.3867, 1229.9656), (0.0, 0.0, -0.0), (1.0, 1.0, 1.0), "PWM_Quarry_1x1x1_A16_202", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3036.602, 4320.9736, 1404.2811), (0.0, -24.51144435218819, 0.0), (1.0, 1.0, 1.8297437), "PWM_Quarry_1x1x1_A17_205", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3517.7861, 4189.777, 1582.3641), (0.0, 65.75431837039713, -0.0), (1.0, 1.0, 1.7910225), "PWM_Quarry_1x1x1_A18_208", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (557.2593, 5450.031, 1637.7937), (0.0, 0.0, -0.0), (1.0, 1.0, 1.0), "PWM_Quarry_1x1x1_A19_226", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4725.0, 3050.0, 1935.0), (-1.1557313477866218, 19.71820632885647, 3.8053012772544856), (1.0, 1.0, 1.0), "PWM_Quarry_1x1x1_A2", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1165.3442, 6256.7397, 1861.6633), (0.0, 0.0, -0.0), (1.0, 1.0, 1.0), "PWM_Quarry_1x1x1_A20_249", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1441.766, 5871.9453, 1390.8468), (11.163591859499432, -5.210296321661574, -21.00976530983196), (1.0, 1.0, 1.0), "PWM_Quarry_1x1x1_A21_272", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1444.0253, 6007.02, 1441.602), (-17.583801509159077, -78.25747435249083, -16.106539939659545), (1.0, 1.0, 1.0), "PWM_Quarry_1x1x1_A22", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1490.7374, 6073.1274, 1477.0227), (-17.583801509159077, -78.25747435249083, -16.106539939659545), (1.0, 1.4059255, 1.0), "PWM_Quarry_1x1x1_A23", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2779.192, 5389.1216, 3486.8171), (0.0, 0.0, -0.0), (1.0, 1.0, 2.063962), "PWM_Quarry_1x1x1_A24_289", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3453.1277, 5377.2837, 3942.1096), (0.0, 0.0, -0.0), (2.1890938, 1.0, 1.0), "PWM_Quarry_1x1x1_A25_301", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1463.6562, 5103.9634, 3938.2837), (0.0, 59.68860290837603, -0.0), (1.0, 1.0, 1.0), "PWM_Quarry_1x1x1_A26_314", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1206.8033, 5042.7744, 3938.2837), (0.0, -137.90811623636495, 0.0), (1.0, 1.0, 1.0), "PWM_Quarry_1x1x1_A27", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (910.1523, 2676.1943, 3368.1067), (0.0, 0.0, -0.0), (1.0, 1.0, 1.0), "PWM_Quarry_1x1x1_A28_330", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (632.98346, 5210.8237, 827.34247), (-42.81255423548836, 58.61547397495286, 5.2325229006586885e-05), (0.47804424, 0.47804424, 0.47804424), "PWM_Quarry_1x1x1_A29_63", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3495.0288, 3154.7407, 2547.6714), (2.8338064066694125e-05, -37.398530028096104, 101.58069089989583), (1.6700006, 2.08857, 1.6700006), "PWM_Quarry_1x1x1_A3_47", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (645.891, 3804.768, 786.6966), (-89.82436591725428, 68.12766304052425, 108.54353259522621), (0.5983628, 0.74881417, 0.69659024), "PWM_Quarry_1x1x1_A30_75", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (922.5032, 3791.1504, 694.4996), (24.251329656583202, 76.7510861020612, 60.17810431567435), (0.33919072, 0.33919072, 0.33919072), "PWM_Quarry_1x1x1_A31_82", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3482.704, 4187.7354, 3893.4883), (2.65127820964984, -137.2147924198812, 3.4456236380373225e-06), (1.5813775, 1.0, 1.0), "PWM_Quarry_1x1x1_A32_10", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3752.477, 4985.275, 3812.0), (0.0, 74.26118371400773, -0.0), (0.9919737, 0.7452559, 0.52516276), "PWM_Quarry_1x1x1_A33_16", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (783.6332, 3741.0835, 712.8864), (-0.7246399678999623, -147.49269760848253, -0.7877808335482733), (1.6431557, 0.748814, 0.69659), "PWM_Quarry_1x1x1_A34", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2814.3733, 2204.586, 1298.7385), (0.0, -101.95627890909405, 0.0), (1.0, 1.0, 1.0), "PWM_Quarry_1x1x1_A4_86", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2767.811, 2214.446, 1165.1864), (0.0, -101.95627890909405, 0.0), (1.0, 1.0, 1.0), "PWM_Quarry_1x1x1_A5", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1087.6396, 115.86478, 2437.8723), (0.0, 0.0, -0.0), (1.0, 1.0, 1.0), "PWM_Quarry_1x1x1_A6_130", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (291.7099, 3303.5046, 2119.1606), (-4.919790368920162, 147.5012377182801, 3.1271436455285904), (1.573959, 1.573959, 1.573959), "PWM_Quarry_1x1x1_A7_36", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4014.3303, 348.84723, 1920.959), (19.843922339759224, 158.19913047881448, -10.666319847075174), (1.573959, 1.573959, 1.573959), "PWM_Quarry_1x1x1_A7_100", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4624.746, 3877.0776, 5266.3804), (-17.63188832705263, 143.40514016742, 21.16709578299209), (1.573959, 1.573959, 1.573959), "PWM_Quarry_1x1x1_A7_238", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3002.9966, 2370.8008, 2066.9983), (0.0, 147.63559326737246, -0.0), (1.573959, 1.573959, 1.573959), "PWM_Quarry_1x1x1_A7_668", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (330.86902, 3252.7305, 2266.0593), (4.327674688288209, 42.142142109774205, 3.9063534425042925), (1.573959, 1.573959, 1.573959), "PWM_Quarry_1x1x1_A8_37", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4127.3057, 317.12823, 2030.1437), (-15.021028832274363, 56.66628240460361, -16.849207461487755), (1.573959, 1.573959, 1.573959), "PWM_Quarry_1x1x1_A8_101", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4610.94, 3807.0732, 5409.9053), (24.396465366160534, 43.82145736171495, 12.615389863445046), (1.573959, 1.573959, 1.573959), "PWM_Quarry_1x1x1_A8_239", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3056.8684, 2320.0266, 2209.162), (0.0, 41.99450183455401, -0.0), (1.573959, 1.573959, 1.573959), "PWM_Quarry_1x1x1_A8_669", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4723.1113, 1583.3141, 3169.6467), (4.370255775586989, 25.033127544515615, -179.2389200925348), (2.632682, 2.632682, 2.54852), "PWM_Quarry_1x1x1_A82_273", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2987.747, 2398.2769, 3139.6467), (4.370235951945532, 145.97062652855166, -179.23896778669675), (2.632682, 2.632682, 2.54852), "PWM_Quarry_1x1x1_A83", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2904.1155, 1313.3799, 2960.932), (-3.4054563158398423, -159.85313050842268, -1.8870848770605495), (2.632682, 2.632682, 2.54852), "PWM_Quarry_1x1x1_A84", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3769.2056, 2281.279, 2925.1106), (0.1305932932826167, 84.60814804302194, 3.33761722933947), (2.632682, 2.632682, 2.54852), "PWM_Quarry_1x1x1_A85", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (447.3913, 3578.6628, 1259.8168), (0.5177159978354825, 84.92057317471678, 5.804498981225972), (1.533111, 1.533111, 1.533111), "PWM_Quarry_1x1x1_A9_39", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3688.4028, 589.9497, 1099.9467), (0.04073762937103551, 97.32082054720611, -22.426635855571018), (1.533111, 1.533111, 1.533111), "PWM_Quarry_1x1x1_A9_103", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5066.388, 4252.741, 4557.6846), (9.623830340915672, 86.17998743004785, 25.65610363443049), (1.533111, 1.533111, 1.533111), "PWM_Quarry_1x1x1_A9_241", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3070.6216, 2645.9587, 1196.2887), (0.0, 84.89433408524472, -0.0), (1.533111, 1.533111, 1.533111), "PWM_Quarry_1x1x1_A9_671", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4076.376, 2441.4358, 3262.992), (-9.825161445635864, 53.016953752345955, -179.7316482967275), (1.132031, 1.828332, 1.132031), "PWM_Quarry_1x1x1_A94", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2584.2007, 1402.3901, 3262.992), (-9.825045204216917, 173.95459100768764, -179.7316827028676), (1.132031, 1.828332, 1.132031), "PWM_Quarry_1x1x1_A95", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2754.6438, 2371.6128, 2815.4844), (9.421282714826118, 171.5109851368446, -2.5547789026106353), (1.132031, 1.828332, 1.132031), "PWM_Quarry_1x1x1_A96", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4799.3975, 1968.1266, 2861.9346), (15.007167060318745, 56.755680790167276, 0.4414463908165982), (1.132031, 1.828332, 1.132031), "PWM_Quarry_1x1x1_A97", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3201.8198, 5674.8174, 741.3818), (-2.1425777240419523, 175.92227432613652, 3.9334367136425743), (0.9862249, 0.9862249, 0.9862249), "StaticMeshActor_18723", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3397.7458, 5680.7046, 759.41345), (0.5701637828944034, -94.8682221857868, 9.748274123359632), (0.80991876, 0.80991876, 0.80991876), "StaticMeshActor_18724", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3320.9246, 5653.4683, 726.68146), (-2.978637413460988, -7.664793664379669, 0.9607904350719302), (0.87574327, 0.87574327, 0.87574327), "StaticMeshActor_18725", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2848.9136, 451.77856, 4062.3013), (-1.343627832572293, -59.57181018401452, 9.05460026695501), (1.6875, 1.25, 1.5625), "StaticMeshActor_18726", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3851.9272, 5565.8604, 934.835), (-3.212952371383734, -93.13800269451787, 5.312384812804584), (0.8937389, 0.8937389, 0.8937389), "StaticMeshActor_18727", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3248.7107, 5257.312, 983.3985), (5.04324066628454, -98.7466231284411, -4.076783149546965), (0.9765641, 0.9765641, 0.9765641), "StaticMeshActor_18728", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3158.2678, 5256.393, 987.0904), (-2.304931242447483, 92.64163499531378, 8.71746687466708), (0.8643128, 0.8643128, 0.8643128), "StaticMeshActor_18729", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2888.0393, 5219.0234, 1035.8878), (4.355345400993442, -134.2023327300605, -3.7337948404834136), (2.9207041, 2.9207041, 2.9207041), "StaticMeshActor_18730", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2173.7373, 4432.718, 1175.7059), (-9.303985947174661, -3.3588256936473573, -3.038268821982393), (0.95254415, 0.95254415, 0.95254415), "StaticMeshActor_18731", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2687.281, 4403.13, 1360.8851), (-4.410950779873816, 71.21851592462916, 15.841725228665851), (1.0846701, 1.0846701, 1.0846701), "StaticMeshActor_18732", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1129.783, 5121.068, 3920.3367), (0.05746840673611265, 97.27415593270462, -9.995301654779883), (1.0599754, 1.0599754, 1.0599754), "StaticMeshActor_18733", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1807.9518, 5297.47, 3926.8728), (0.9846402913798631, 87.94002829373758, 5.25539552754611), (0.94337183, 0.94337183, 0.94337183), "StaticMeshActor_18734", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1603.8674, 5241.2314, 3896.4678), (-3.465911994240821, -7.081482731415367, -1.319671939422156), (1.0570722, 1.0570722, 1.0570722), "StaticMeshActor_18735", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3261.1462, 5562.454, 3922.876), (5.372475877776638, 178.8668120322815, -1.8374935991869383), (1.0325875, 1.0325875, 1.0325875), "StaticMeshActor_18736", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3549.8677, 5047.447, 1609.6907), (9.912094008846426, 88.41371002332141, 0.7894262462867925), (0.96294516, 0.96294516, 0.96294516), "StaticMeshActor_18738", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3315.1094, 4210.4253, 1591.6631), (27.893824577999002, -75.2885311887003, 173.44861749710194), (0.982739, 0.982739, 0.982739), "StaticMeshActor_18739", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4697.12, 1791.3887, 3210.7031), (-8.914214177434637, -171.39763135254742, 3.88635053809344), (0.8781563, 0.8781563, 0.8781563), "StaticMeshActor_18740", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2048.8062, 3672.6438, 3938.743), (-1.0449223822961786, -99.38305372593099, 9.308226007877867), (1.0810953, 1.0810953, 1.0810953), "StaticMeshActor_18743", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2324.3513, 3555.3606, 3980.5596), (-1.8634943191831046, 169.42845809309682, 1.740696256457877), (0.9207299, 0.9207299, 0.9207299), "StaticMeshActor_18744", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2132.0632, 3030.5896, 3985.2866), (-1.960754748996346, 1.3283597037745403, -5.090210270673406), (0.8664816, 0.8664816, 0.8664816), "StaticMeshActor_18745", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3453.4392, 5093.421, 1599.7831), (-8.982237676562908, -86.49812868538022, -1.9129945845825551), (1.0940999, 1.0940999, 1.0940999), "StaticMeshActor_18746", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3438.3604, 5069.446, 1409.2784), (-3.7051695357637042, 3.8303557983006433, 1.2052851034326688), (0.99043596, 0.99043596, 0.99043596), "StaticMeshActor_18747", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3882.6768, 5663.616, 1073.3519), (-4.123015803341211, -9.172911475894512, 3.3899260972103153), (1.0357562, 1.0357562, 1.0357562), "StaticMeshActor_18748", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1815.3973, 4519.227, 1175.6814), (-0.17227172441198504, -94.31671601314541, 0.9438465377961015), (0.8639295, 0.8639295, 0.8639295), "StaticMeshActor_18749", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (6059.9565, 4066.43, 2719.4731), (-12.865203375424894, 31.825014687793647, 3.151928381022494), (1.0958123, 1.0958123, 1.0958123), "StaticMeshActor_18750", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (300.23358, 3539.7742, 4067.4878), (-3.7875057052327454, -132.2173182047194, -0.9217834311667226), (0.9341362, 0.9341362, 0.9341362), "StaticMeshActor_18752", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3544.0344, 442.86145, 4075.7104), (8.009146741136657, 92.74065411779749, -1.6074832574368867), (1.3125, 1.125, 1.125), "StaticMeshActor_18753", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (6248.624, 3249.3276, 2706.0295), (0.9688349775939485, 0.05794141591094029, -8.596679153434701), (1.053011, 1.053011, 1.053011), "StaticMeshActor_18754", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2745.3152, 688.7847, 4375.8755), (-5.6716909915486875, 116.57496091496924, 12.013184384116489), (1.0069869, 1.0069869, 1.0069869), "StaticMeshActor_18755", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2789.746, 619.71576, 4384.955), (-2.3529665379870046, -47.736267849913446, -13.340484671427078), (1.0854363, 1.0854363, 1.0854363), "StaticMeshActor_18756", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2803.6133, 820.9951, 4345.278), (34.93178205955247, -150.44203083360063, 15.929708562591802), (1.0, 1.0, 1.0), "StaticMeshActor_18757", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5367.278, 764.5556, 4256.6016), (-7.1405036524263785, 177.97695004810933, 1.8346472272979102), (1.0075321, 1.0075321, 1.0075321), "StaticMeshActor_18758", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5341.0537, 790.5332, 4168.9473), (-8.325743472352874, 175.2568741720355, -4.980803343752702), (0.8237331, 0.8237331, 0.8237331), "StaticMeshActor_18759", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2662.6904, 1948.0397, 893.2573), (0.784153244562524, 99.59606686416066, 3.8826472899569215), (0.89331937, 0.89331937, 0.89331937), "StaticMeshActor_18761", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2793.222, 2011.5278, 1151.7303), (-4.760620048347957, -93.34838517783588, 4.353671327011407), (0.9247053, 0.9247053, 0.9247053), "StaticMeshActor_18762", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2711.215, 2043.1475, 982.0689), (-6.063903329179393, -6.309081738807037, 0.28949737728987796), (1.0456527, 1.0456527, 1.0456527), "StaticMeshActor_18763", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2026.9354, 5367.2954, 3862.926), (6.909698630884083, 6.570830842498069, -2.524993669410612), (0.889362, 0.889362, 0.889362), "StaticMeshActor_18764", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1931.5587, 5331.681, 3876.074), (2.0458252444530687, -176.1764455498814, -9.087339501941427), (0.8926197, 0.8926197, 0.8926197), "StaticMeshActor_18765", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1934.0455, 5340.5176, 3789.7197), (-7.968078818583634, 88.64967583502957, 1.932825542373698), (0.8293655, 0.8293655, 0.8293655), "StaticMeshActor_18766", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1518.7809, 5146.6606, 3746.8936), (-2.512603871690629, -6.10522418086667, -5.084320353878487), (1.0517583, 1.0517583, 1.0517583), "StaticMeshActor_18767", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (736.7886, 2827.9963, 4709.631), (24.103282270834054, -125.52264487313961, -9.6476442121428), (0.97314453, 0.97314453, 0.97314453), "StaticMeshActor_18768", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5335.8994, 5759.5386, 4309.789), (-4.153319745976051, 99.95334091904395, 7.803777822827864), (1.0733778, 1.0733778, 1.0733778), "StaticMeshActor_18781", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5244.0464, 5661.112, 4318.4126), (9.666635773546108, -6.446991118930065, -1.2668761194709013), (1.0809668, 1.0809668, 1.0809668), "StaticMeshActor_18782", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5337.8184, 5757.289, 4206.9746), (-8.435698844695446, -4.8901054391024354, 6.911015031669877), (1.0359218, 1.0359218, 1.0359218), "StaticMeshActor_18783", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5346.628, 5661.0933, 4209.645), (-9.68997243379163, -1.0142518630161244, -7.31484912691119), (1.0631548, 1.0631548, 1.0631548), "StaticMeshActor_18784", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5251.947, 5658.601, 4205.354), (3.5440483805259264, -0.637939369134584, 3.354432890719718), (1.0041441, 1.0041441, 1.0041441), "StaticMeshActor_18785", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2941.8313, 3298.6255, 1931.4373), (-8.783234934645757, 102.54325198154244, 0.6922653797638219), (1.0310457, 1.0310457, 1.0310457), "StaticMeshActor_18786", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3584.3645, 3204.614, 2729.3103), (-1.6729125908046, 127.64186395243787, -15.979460046911319), (0.90016526, 0.90016526, 0.90016526), "StaticMeshActor_18787", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4266.4453, 2088.7073, 3129.9978), (-17.289093386319273, 31.316117010243588, -9.328949303698897), (0.8664463, 0.8664463, 0.8664463), "StaticMeshActor_18789", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5863.86, 2913.6272, 1373.8896), (-6.442840698205916, -2.842895553688083, -28.122891993980158), (1.099857, 1.099857, 1.099857), "StaticMeshActor_18792", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5964.5825, 2913.9893, 1356.502), (5.342552416465733, -179.47252314970123, 24.140603449347207), (0.9456504, 0.9456504, 0.9456504), "StaticMeshActor_18793", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (6445.4375, 3507.4546, 1291.6012), (33.0869265600234, -96.64280323071408, 4.644521409984503), (1.0205173, 1.0205173, 1.0205173), "StaticMeshActor_18794", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (6448.7534, 2813.762, 1260.484), (21.691765775763656, 92.54758881367434, -4.404113171022165), (0.8564093, 0.8564093, 0.8564093), "StaticMeshActor_18795", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5402.0273, 1768.1051, 1079.7137), (-3.0806266508468854, -178.7832264843366, 2.6772079001617373), (1.0985153, 1.0985153, 1.0985153), "StaticMeshActor_18796", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5480.61, 1720.8887, 3781.9492), (-8.592648411314007, 174.96736582287159, -4.031248659144066), (0.81115514, 0.81115514, 0.81115514), "StaticMeshActor_18797", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5396.687, 4059.6604, 3424.8906), (-1.8416444348600063, 18.389649867145838, 3.6514860494487302), (1.0664436, 1.0664436, 1.0664436), "StaticMeshActor_18801", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5333.4043, 4143.9424, 3506.7725), (-1.4029540661080024, -179.586957029903, 2.10072911050742), (1.0234437, 1.0234437, 1.0234437), "StaticMeshActor_18802", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5328.828, 4200.815, 3488.0303), (0.6552607135712014, -94.66702798959324, 6.146808937348426), (0.9788691, 0.9788691, 0.9788691), "StaticMeshActor_18803", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5278.6626, 4173.3135, 3399.7747), (14.552550250586217, -154.90984091195762, 7.09990918376211), (1.0481333, 1.0481333, 1.0481333), "StaticMeshActor_18804", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5334.79, 4094.9011, 3394.2063), (-3.0232238330443275, -61.294501939645244, 12.486872080271233), (1.0642836, 1.0642836, 1.0642836), "StaticMeshActor_18805", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2856.0505, 4416.0684, 1364.5713), (-8.635009377998376, -85.0418689049342, -8.909576207457109), (0.8162888, 0.8162888, 0.8162888), "StaticMeshActor_18806", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3108.9678, 4306.5967, 1429.2095), (6.382339711707037, 13.322968060274476, 9.170792023978374), (0.96393645, 0.96393645, 0.96393645), "StaticMeshActor_18807", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3422.9805, 4185.054, 1533.4694), (-17.080169684949297, -11.791899826150663, 87.93420349742122), (0.9080427, 0.9080427, 0.9080427), "StaticMeshActor_18808", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3152.0361, 4285.6235, 1381.1324), (13.822318547083876, -7.774992042888366, -0.46096787829469155), (0.8441119, 0.8441119, 0.8441119), "StaticMeshActor_18809", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2783.1372, 4342.3213, 1371.337), (19.467047850696105, 65.78721790914989, -13.883145767132826), (0.83461076, 0.83461076, 0.83461076), "StaticMeshActor_18810", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3644.5662, 4150.377, 1107.025), (0.8952192599308226, -80.00104059064161, 1.833855589976037), (0.8209326, 0.8209326, 0.8209326), "StaticMeshActor_18811", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3737.5083, 4137.506, 1012.44275), (-8.692412759181243, 89.91520839130209, -4.019409508628219), (0.9288666, 0.9288666, 0.9288666), "StaticMeshActor_18812", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (444.25916, 945.7626, 1014.6137), (-5.19250467327174, 87.99522793329139, 5.836482377975952), (0.8689934, 0.8689934, 0.8689934), "StaticMeshActor_18813", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2259.056, 3609.0945, 3803.9192), (-1.0861204594390288, 91.25457632461189, -0.8860472353277272), (0.81733733, 0.81733733, 0.81733733), "StaticMeshActor_18814", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2154.795, 3597.3667, 3807.9236), (7.06708696485048, -83.47704583092593, -5.729766930210806), (1.019, 1.019, 1.019), "StaticMeshActor_18815", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2016.7787, 3616.56, 3868.406), (-1.111267048075672, 3.209562948726312, -1.1687622184384543), (1.0172869, 1.0172869, 1.0172869), "StaticMeshActor_18816", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2612.724, 5927.599, 870.7929), (6.780007300765445, 1.605771226289357, -8.438721645639681), (0.80887586, 0.80887586, 0.80887586), "StaticMeshActor_18817", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3444.5305, 758.07104, 4710.272), (-4.253479108807188, 6.5502778612283725, 38.70188476547784), (0.8809871, 0.8809871, 0.8809871), "StaticMeshActor_18818", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3148.5474, 761.1321, 4698.404), (-29.29879479204884, -90.74431890631988, -24.66714517488033), (1.0891701, 1.0891701, 1.0891701), "StaticMeshActor_18819", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1308.8602, 3307.5156, 3581.137), (17.481811102684972, -1.8952634726299025, -18.21722225070991), (0.82794917, 0.82794917, 0.82794917), "StaticMeshActor_18820", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1249.3586, 3250.2524, 3525.8267), (23.326647384971807, 84.57487925834013, 22.414124775599095), (0.84084874, 0.84084874, 0.84084874), "StaticMeshActor_18821", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1327.332, 3245.0476, 3555.4385), (-9.706693694717886, -172.811522988564, 6.8418981515187465), (0.8155561, 0.8155561, 0.8155561), "StaticMeshActor_18822", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2185.1902, 3248.5398, 3458.6292), (12.567932255839315, 85.42605282904591, -37.02752479364995), (1.0806804, 1.0806804, 1.0806804), "StaticMeshActor_18823", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2142.786, 3244.933, 3499.3906), (44.099551424812546, -177.27580814010338, 5.08439904258838), (1.0426265, 1.0426265, 1.0426265), "StaticMeshActor_18824", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2151.8745, 3351.5774, 5810.758), (-5.532378878557781, -1.1781615935670218, 8.985931652894568), (0.87497467, 0.87497467, 0.87497467), "StaticMeshActor_18825", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2055.5476, 3352.0598, 5830.3286), (6.651100983230873, -89.09093382600774, 10.996518752916385), (1.0471208, 1.0471208, 1.0471208), "StaticMeshActor_18826", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3743.5452, 4155.482, 5808.56), (-13.753053491428595, -178.72197021800778, -1.659790193200743), (0.91991365, 0.91991365, 0.91991365), "StaticMeshActor_18827", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4535.8223, 4053.0276, 5938.7153), (-10.085785190411391, -92.5888655015114, -3.1787722487704135), (0.998652, 0.998652, 0.998652), "StaticMeshActor_18828", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4529.9478, 4051.3315, 5945.718), (-6.6340024605540995, 86.55131985778064, 0.6942106469510168), (0.8179377, 0.8179377, 0.8179377), "StaticMeshActor_18829", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2940.456, 2570.3987, 5974.192), (-15.212645505508833, 88.62320658211084, 1.3732670267100922), (0.8796842, 0.8796842, 0.8796842), "StaticMeshActor_18830", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2943.5645, 2489.1655, 5988.036), (13.702344048853073, -0.39715557078379476, 25.131861501987636), (1.0384417, 1.0384417, 1.0384417), "StaticMeshActor_18831", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2844.333, 2557.9475, 5903.5767), (-0.4709777595380916, 0.5969590826772634, 10.062424436430328), (1.0320683, 1.0320683, 1.0320683), "StaticMeshActor_18832", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2850.7783, 2598.399, 5909.4917), (10.700002900862396, -2.1072994685335673, 9.615939448551417), (0.80375487, 0.80375487, 0.80375487), "StaticMeshActor_18833", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2824.844, 5168.6074, 1198.0267), (4.355344754316808, -134.20233266989058, -3.7337944873139053), (2.0287104, 2.0287104, 2.0287104), "StaticMeshActor18867", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3366.5962, 5156.1523, 1000.0762), (5.0432410144940985, -98.74662313233148, -4.0767828512928155), (1.6176786, 1.6176786, 1.6176786), "StaticMeshActor18868", _folder)
if a: placed += 1
else: skipped += 1

# Batch 35: StaticMesh'PWM_Quarry_1x1x1_B' (51 instances)
_mesh_path = "/Game/Unshippable/Whitebox/Rocks/Meshes/PWM_Quarry_1x1x1_B"
_materials = ['/Game/Environments/ProcTexturing/ProcMaterial_Quarry_Atlas_1']
_folder = "Reconstruction/BD_BB_Passage_SpiralCave/Meshes"
a = spawn_static_mesh(_mesh_path, _materials, (2657.4497, 5948.1997, 806.1878), (3.4273819229537286, -4.823547457974476, 3.596820499056445), (1.0229678, 1.0229678, 1.0229678), "StaticMeshActor_18498", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2649.6577, 5752.437, 811.98584), (-0.41015636018421886, -81.06945952857755, 9.193509727570076), (0.8411505, 0.8411505, 0.8411505), "StaticMeshActor_18499", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3314.6816, 5225.841, 978.1169), (-2.924011186979144, -178.98241827064362, 6.318709303494344), (0.9579707, 0.9579707, 0.9579707), "StaticMeshActor_18500", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1243.1295, 5160.517, 3890.6113), (2.6664303233332896, -96.05719311724961, 9.44788342043734), (0.8992914, 0.8992914, 0.8992914), "StaticMeshActor_18503", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5509.8374, 2124.5327, 3908.1191), (4.642500274155686, 82.91777688215348, -1.1859134017797353), (1.084533, 1.084533, 1.084533), "StaticMeshActor_18507", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (490.5767, 3646.7761, 4001.6282), (-6.1359868361895264, 99.64173623713744, -2.1684874164433636), (0.8820459, 0.8820459, 0.8820459), "StaticMeshActor_18513", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (505.99463, 2763.6187, 4031.503), (7.554781970610303, 158.88893724343052, 6.539840284687145), (1.0955522, 1.0955522, 1.0955522), "StaticMeshActor_18514", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2162.8074, 3082.0918, 3815.5757), (-4.284393141077541, -103.0106693810237, -0.12323006206135508), (1.099814, 1.099814, 1.099814), "StaticMeshActor_18517", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5250.8203, 104.86669, 5127.6875), (1.3234997394785082, 18.219261140609433, 19.959829678860906), (1.0138137, 1.0138137, 1.0138137), "StaticMeshActor_18519", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5361.4497, 144.52069, 5136.1836), (-16.70138632627582, 23.08506537466557, 34.62149877124835), (0.8026387, 0.8026387, 0.8026387), "StaticMeshActor_18520", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (287.9325, 3647.133, 4360.378), (-4.330993213717525, -156.72665473987794, -5.883300081057197), (0.99883157, 0.99883157, 0.99883157), "StaticMeshActor_18521", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (225.97777, 3588.0789, 4285.0547), (-2.3802787569678494, -97.7130824112889, 8.728687780866592), (0.89083064, 0.89083064, 0.89083064), "StaticMeshActor_18523", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (6256.1714, 3348.3247, 2592.4146), (-6.10705574563289, -98.5540330008563, 2.5422301143345933), (0.90394264, 0.90394264, 0.90394264), "StaticMeshActor_18526", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (6072.5645, 705.463, 5175.6743), (17.98592275991805, -74.99762743024938, 9.408171580956681), (0.8470934, 0.8470934, 0.8470934), "StaticMeshActor_18529", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2942.8784, 3252.982, 1813.4341), (4.762574418516016, 24.873825787702764, 29.650733108641365), (0.8303991, 0.8303991, 0.8303991), "StaticMeshActor_18535", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2122.674, 5399.1665, 3843.7578), (7.28406905896387, -170.01664460285315, -7.603881174698886), (0.9040295, 0.9040295, 0.9040295), "StaticMeshActor_18536", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2020.3605, 5367.5044, 3779.715), (-7.131591446303828, -8.290099174612537, -7.724883279638187), (1.0030326, 1.0030326, 1.0030326), "StaticMeshActor_18538", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1835.733, 5276.1426, 3887.6934), (5.268425748617451, 2.721241910862749, 7.1572683499552445), (0.84081787, 0.84081787, 0.84081787), "StaticMeshActor_18539", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1515.4025, 5189.5283, 3820.3838), (-9.684844258067434, 98.27599935054181, 7.045160450235773), (0.8916812, 0.8916812, 0.8916812), "StaticMeshActor_18540", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1416.9847, 5158.1694, 3839.2068), (-6.6785293222906805, -85.93020610246468, 9.995605203672454), (0.99233836, 0.99233836, 0.99233836), "StaticMeshActor_18541", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5349.0903, 2508.356, 984.15125), (-4.98120127260865, -77.7087972715883, 4.215270651467018), (1.065776, 1.065776, 1.065776), "StaticMeshActor_18542", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (594.9387, 2768.2925, 4588.7935), (0.8143764625098693, 152.95416189112947, -25.110318417374543), (0.9492815, 0.9492815, 0.9492815), "StaticMeshActor_18543", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (579.3928, 2756.039, 4485.3496), (-4.03298918624329, 140.0733908635133, -4.378112850147675), (0.95509565, 0.95509565, 0.95509565), "StaticMeshActor_18544", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (581.0862, 2753.5176, 4392.1426), (3.983297705202356, -111.4560258565464, 7.400746631105687), (0.9997862, 0.9997862, 0.9997862), "StaticMeshActor_18545", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (599.76917, 2766.2822, 4290.0557), (1.307953947065585, -34.67248715771758, -13.478851563475528), (0.8484105, 0.8484105, 0.8484105), "StaticMeshActor_18546", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1333.2065, 3349.5063, 5851.4927), (1.3547547309598478, -88.29553528905942, -18.108155815704663), (1.0572402, 1.0572402, 1.0572402), "StaticMeshActor_18548", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1250.7559, 3344.2349, 5797.4595), (-1.0213922863777378, -82.796909225054, -32.97195541941224), (0.93671316, 0.93671316, 0.93671316), "StaticMeshActor_18549", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1339.1276, 3249.4792, 5847.876), (25.46071446216899, -1.8886103471053526, -11.10604686011486), (0.90804136, 0.90804136, 0.90804136), "StaticMeshActor_18550", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5351.386, 5653.983, 4303.4023), (8.877517271230612, -86.87963992061076, -0.4385072645876947), (1.0656948, 1.0656948, 1.0656948), "StaticMeshActor_18564", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3755.432, 4050.102, 5797.747), (-15.693024319936466, 178.18504022781497, 21.485359231331184), (0.8156189, 0.8156189, 0.8156189), "StaticMeshActor_18566", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5855.6396, 2835.2192, 1337.3528), (-2.098602238510243, 1.6517284438018782, -33.776973957308996), (0.98023474, 0.98023474, 0.98023474), "StaticMeshActor_18568", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5525.006, 1816.5251, 3771.284), (-8.511199315733455, -95.01140966877595, -7.648467344514536), (0.9422237, 0.9422237, 0.9422237), "StaticMeshActor_18574", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5396.283, 4084.3164, 3487.869), (-9.819487864536558, 8.42938787395872, -2.636901493302218), (1.0138407, 1.0138407, 1.0138407), "StaticMeshActor_18578", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5357.995, 4121.294, 3455.7056), (1.6262134078266888, 83.39955920743839, 2.0734707901940963), (0.9801419, 0.9801419, 0.9801419), "StaticMeshActor_18579", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3460.7144, 4242.4434, 1545.7683), (-4.829315030933758, -80.26843498643306, 3.9154459421660848), (0.9953669, 0.9953669, 0.9953669), "StaticMeshActor_18580", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2875.735, 4450.233, 1329.1779), (-5.9759512415581515, 92.0256580464102, -8.468321491623586), (0.99014926, 0.99014926, 0.99014926), "StaticMeshActor_18581", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3555.8513, 4261.596, 1554.3055), (-5.325499323768298, 179.24290873238607, 1.5082737060675078), (1.0917408, 1.0917408, 1.0917408), "StaticMeshActor_18582", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3256.3474, 4286.222, 1392.476), (8.17819523160817, -4.633574869216074, -8.08087072444871), (1.0660527, 1.0660527, 1.0660527), "StaticMeshActor_18583", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3944.4062, 4245.141, 1615.4221), (-7.835814228266095, 97.20959461810438, -0.40710473359701593), (0.9400469, 0.9400469, 0.9400469), "StaticMeshActor_18586", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (464.1463, 913.4021, 1091.2068), (0.1383318437392506, 81.08213587484316, -2.090332268169297), (0.8888765, 0.8888765, 0.8888765), "StaticMeshActor_18587", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1552.5142, 2650.0947, 3908.3755), (3.3731433739000325, 76.00361323907096, 5.043604354952544), (0.87265015, 0.87265015, 0.87265015), "StaticMeshActor_18589", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4555.8477, 160.60785, 5104.327), (-16.49197121729245, 167.45284158915217, -35.92241725726554), (0.9650425, 0.9650425, 0.9650425), "StaticMeshActor_18591", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2339.8203, 3645.4092, 3808.5813), (24.62773295868366, -67.29369517212055, 3.9034528452327786), (0.9658467, 0.9658467, 0.9658467), "StaticMeshActor_18592", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2049.0833, 3604.4875, 3824.9358), (-0.3943175219809481, 8.11705141944599, -3.491149571650575), (0.8558809, 0.8558809, 0.8558809), "StaticMeshActor_18593", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2034.504, 3608.293, 3902.5505), (2.040566875924595, 97.71623828536569, -0.15496820228250072), (0.89036524, 0.89036524, 0.89036524), "StaticMeshActor_18594", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2642.8687, 5853.0005, 909.4261), (-4.41940250520106, 95.53215030383258, -7.228148902122584), (0.8062208, 0.8062208, 0.8062208), "StaticMeshActor_18595", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2141.1636, 3338.4485, 3513.5857), (-19.36703635979501, 7.55797814366954, -24.61032201276944), (0.9153985, 0.9153985, 0.9153985), "StaticMeshActor_18597", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2064.1523, 4043.8633, 5844.985), (2.753147314451023, 97.24267480829803, -19.936004280896903), (1.0543718, 1.0543718, 1.0543718), "StaticMeshActor_18598", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3726.1357, 4948.7534, 5862.807), (4.311330518624986, -6.95056163698539, -1.4553221418539766), (0.9096567, 0.9096567, 0.9096567), "StaticMeshActor_18599", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3644.9526, 4958.201, 5855.821), (-1.6617432532674274, 174.74953195816425, 6.3622912686171516), (0.93933505, 0.93933505, 0.93933505), "StaticMeshActor_18600", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4543.7104, 4147.9966, 5955.578), (-0.7164916495072879, 85.5965164663315, 6.746776434862142), (0.82235885, 0.82235885, 0.82235885), "StaticMeshActor_18603", _folder)
if a: placed += 1
else: skipped += 1

# Batch 36: StaticMesh'PWM_Quarry_1x1x1_B' (20 instances)
_mesh_path = "/Game/Unshippable/Whitebox/Rocks/Meshes/PWM_Quarry_1x1x1_B"
_materials = ['/Game/Environments/ProcTexturing/ProcMaterial_Quarry_Atlas_A']
_folder = "Reconstruction/BD_BB_Passage_SpiralCave/Meshes"
a = spawn_static_mesh(_mesh_path, _materials, (2640.0737, 1952.1969, 816.02997), (1.6968374292934993, 8.268995202152238, 9.087984321800997), (0.82189864, 0.82189864, 0.82189864), "StaticMeshActor_18497", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1834.5474, 5320.5254, 3953.3572), (1.7991675244378516, 2.806633564943395, -1.1648559285714293), (1.0738028, 1.0738028, 1.0738028), "StaticMeshActor_18504", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5284.5205, 3453.1157, 3666.3953), (8.097414292291331, -171.41597573661423, -2.185943799188585), (1.003792, 1.003792, 1.003792), "StaticMeshActor_18506", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3048.3928, 1943.1097, 803.45776), (9.224435365043615, -97.178680905069, -0.6423037928533746), (0.952862, 0.952862, 0.952862), "StaticMeshActor_18508", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3577.9368, 526.52814, 4437.8306), (24.513437983965648, -26.71548255444984, -2.7439874826317014), (1.0688035, 1.0688035, 1.0688035), "StaticMeshActor_18524", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (6041.7007, 4048.8003, 2618.8862), (5.152598064275244, -84.24783045212004, 2.422549765527128), (0.9920599, 0.9920599, 0.9920599), "StaticMeshActor_18525", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3770.635, 856.9775, 4345.3774), (5.328216777975336, 20.687226632602496, -1.0124513465675473), (0.9869896, 0.9869896, 0.9869896), "StaticMeshActor_18530", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2736.09, 2110.3691, 1202.1271), (8.006477957476443, -85.24500279619943, -7.19809047425351), (1.0970856, 1.0970856, 1.0970856), "StaticMeshActor_18533", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2723.8457, 1964.7572, 948.5299), (8.239831482455815, -9.87234742626381, 2.3934008582490254), (0.8683286, 0.8683286, 0.8683286), "StaticMeshActor_18534", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5370.5205, 122.19341, 5029.1064), (7.57543655842466, -63.55173068913516, 0.22503904140799097), (0.99642295, 0.99642295, 0.99642295), "StaticMeshActor_18547", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3055.2817, 1944.3448, 913.0072), (-5.292052637587163, -171.94536171095592, -4.142455553009682), (0.82246864, 0.82246864, 0.82246864), "StaticMeshActor_18565", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5352.8945, 1662.0054, 980.6472), (-4.263091282335641, -97.24016885145575, 1.2216190524480093), (0.9305381, 0.9305381, 0.9305381), "StaticMeshActor_18573", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3741.1482, 4147.446, 1103.0073), (-8.710021767198574, 5.679293007938829, 6.32580530359919), (0.94047487, 0.94047487, 0.94047487), "StaticMeshActor_18584", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3531.0127, 4137.754, 1037.2716), (-9.856932280350623, -171.0324887280721, -1.6535947701908986), (0.86459804, 0.86459804, 0.86459804), "StaticMeshActor_18585", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4449.785, 150.64488, 5009.597), (31.383178973974584, -119.94314152096653, -13.580593679291495), (1.0462732, 1.0462732, 1.0462732), "StaticMeshActor_18590", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2154.22, 3255.9087, 5811.86), (-13.12445068469956, 89.06659661761739, -11.689085832860437), (0.9567387, 0.9567387, 0.9567387), "StaticMeshActor_18602", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4436.056, 3353.584, 5952.8726), (-8.597443133693988, 171.33115640681922, -12.397919896562513), (0.96564883, 0.96564883, 0.96564883), "StaticMeshActor_18607", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4561.6733, 3253.1267, 5991.0654), (-11.00067034945906, 99.32280779027715, -9.88961875428689), (0.90761244, 0.90761244, 0.90761244), "StaticMeshActor_18608", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4447.08, 3268.963, 5965.695), (16.145705615207913, -97.22322885131226, -0.016662320975708928), (0.92461395, 0.92461395, 0.92461395), "StaticMeshActor_18609", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2843.486, 2502.0298, 5935.5186), (3.485554777250446, -171.7332888283462, -9.859252778331443), (0.908348, 0.908348, 0.908348), "StaticMeshActor_18610", _folder)
if a: placed += 1
else: skipped += 1

# Batch 37: StaticMesh'PWM_Quarry_1x1x1_B' (3 instances)
_mesh_path = "/Game/Unshippable/Whitebox/Rocks/Meshes/PWM_Quarry_1x1x1_B"
_materials = ['/Game/Environments/ProcTexturing/ProcMaterial_Quarry_Floor_6x2x1']
_folder = "Reconstruction/BD_BB_Passage_SpiralCave/Meshes"
a = spawn_static_mesh(_mesh_path, _materials, (2038.6885, 4429.252, 1204.5394), (-1.0945434546991437, 2.683550355433992, 8.049326910307434), (0.9224283, 0.9224283, 0.9224283), "StaticMeshActor_18502", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2564.3926, 4422.274, 1374.9851), (-4.568725247690692, 172.83219139754047, -9.90789611304845), (0.80177844, 0.80177844, 0.80177844), "StaticMeshActor_18509", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2498.5898, 4372.955, 1320.1208), (15.810275257476215, -3.6125791945230468, 179.36504882185997), (0.9604466, 0.9604466, 0.9604466), "StaticMeshActor_18510", _folder)
if a: placed += 1
else: skipped += 1

# Batch 38: StaticMesh'PWM_Quarry_1X1x1_C' (290 instances)
_mesh_path = "/Game/Unshippable/Whitebox/Rocks/Meshes/PWM_Quarry_1X1x1_C"
_materials = ['/Game/Environments/ProcTexturing/ProcMaterial_Quarry_Atlas_1']
_folder = "Reconstruction/BD_BB_Passage_SpiralCave/Meshes"
a = spawn_static_mesh(_mesh_path, _materials, (2802.5994, 3160.7524, 1231.3677), (0.0, 0.0, -0.0), (1.0, 1.0, 1.0), "PWM_Quarry_1X1x1_C_8", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3879.3772, 2404.8152, 2995.004), (3.52123925158129, -59.4208980137001, 89.89113884870491), (2.25, 1.5, 1.5), "PWM_Quarry_1X1x1_C10", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2279.8481, 4108.1436, 587.7413), (-42.3601685549964, -134.84070492137235, -33.12173743586466), (1.268508, 1.268508, 1.268508), "PWM_Quarry_1X1x1_C100", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3296.4539, 3808.0596, 560.94995), (-41.67370352568865, -60.53240594879629, -50.77129869601433), (1.1310055, 1.1310055, 1.1310055), "PWM_Quarry_1X1x1_C101", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4829.7993, 5768.124, 4012.561), (0.0, 90.38153756332304, -0.0), (0.81187266, 0.81187266, 0.81187266), "PWM_Quarry_1X1x1_C102_198", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4857.618, 5551.1265, 4012.561), (0.0, -166.56947427610996, 0.0), (0.9518284, 0.982618, 0.811873), "PWM_Quarry_1X1x1_C103", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4870.034, 5849.775, 4023.394), (5.338351819130128e-06, 90.38155330671557, 55.41361538829238), (1.1016881, 1.1016881, 1.1016881), "PWM_Quarry_1X1x1_C104", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4925.098, 6049.0776, 4014.1587), (-7.253754043250587, 39.45026090000424, -95.85234884536544), (1.101688, 1.101688, 1.101688), "PWM_Quarry_1X1x1_C105", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (861.99786, 5357.769, 3999.981), (-70.50657909522141, -179.9999453584493, -179.99998633960558), (0.6926916, 0.63348955, 0.77530336), "PWM_Quarry_1X1x1_C106_248", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (865.9075, 5505.623, 3999.981), (-70.50475295588139, 97.05596939335688, -179.9999178983721), (0.692692, 0.63349, 0.775303), "PWM_Quarry_1X1x1_C107", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (870.18243, 5082.8906, 3999.981), (-70.50458818730317, 71.45545499316344, -179.99989609727643), (0.692692, 0.63349, 0.775303), "PWM_Quarry_1X1x1_C108", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (910.655, 5202.945, 4010.1028), (-70.50458818730317, 71.45545499316344, -179.99989609727643), (0.692692, 0.63349, 0.775303), "PWM_Quarry_1X1x1_C109", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2716.8896, 1252.2463, 2995.004), (3.5212612933667984, 61.51671102755513, 89.89105637749942), (2.25, 1.5, 1.5), "PWM_Quarry_1X1x1_C11", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5174.6455, 3911.0874, 3962.1519), (4.079291362975764, -58.52452012098811, -103.53310903447772), (2.25, 1.5, 1.5), "PWM_Quarry_1X1x1_C11_211", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2920.7493, 2229.0955, 660.68713), (-3.6480416729897285, -57.51324480784304, -77.34319754997546), (2.25, 1.5, 1.5), "PWM_Quarry_1X1x1_C11_641", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (973.19275, 5397.159, 3959.2188), (0.0, -107.00172232675244, 0.0), (0.7656679, 0.7656679, 1.0), "PWM_Quarry_1X1x1_C110_254", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1093.854, 3809.3594, 4063.997), (0.0, -149.69670027020373, 0.0), (0.54861593, 0.54861593, 0.54861593), "PWM_Quarry_1X1x1_C111_277", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (999.2281, 3796.194, 4068.161), (0.0, -149.69670027020373, 0.0), (0.71047795, 0.71047795, 0.71047795), "PWM_Quarry_1X1x1_C112", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (906.25055, 3583.934, 3983.6262), (0.0, -149.69670027020373, 0.0), (0.710478, 0.710478, 0.710478), "PWM_Quarry_1X1x1_C113", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1037.6737, 3581.9324, 3992.1938), (0.0, -20.497803522097524, 0.0), (0.43841285, 0.43841285, 0.43841285), "PWM_Quarry_1X1x1_C114", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1144.963, 3841.6875, 4028.0708), (-1.3429565294841241, 128.9429082105425, 177.70048293308326), (0.7620953, 0.7620953, 0.7620953), "PWM_Quarry_1X1x1_C115", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2130.7085, 3202.4282, 3987.9092), (0.0, -2.564605572464438, 0.0), (0.58469397, 0.58469397, 0.58469397), "PWM_Quarry_1X1x1_C116_300", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2265.5002, 3335.2144, 4019.3777), (-0.060212232858496306, 75.95278615155344, -22.656465564380927), (0.8856621, 0.8856621, 0.8856621), "PWM_Quarry_1X1x1_C117", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2265.5002, 3591.3892, 3985.2588), (-0.060212232858496306, 75.95278615155344, -22.656465564380927), (0.885662, 0.885662, 0.885662), "PWM_Quarry_1X1x1_C118", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1773.3385, 2709.3374, 4071.8381), (-0.060180564645722995, 20.925170966719342, -75.98785657559073), (0.7384298, 0.7384298, 0.7384298), "PWM_Quarry_1X1x1_C119", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2795.901, 2445.9795, 2857.7983), (0.16622073282189095, 78.96357769115339, -94.28656390835859), (2.25, 1.5, 1.5), "PWM_Quarry_1X1x1_C12", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1106.4924, 2666.988, 4039.7441), (-14.195831577366326, 15.534752618206774, 18.6060759678674), (0.885662, 0.885662, 0.885662), "PWM_Quarry_1X1x1_C120", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (922.7023, 2732.7292, 4050.2527), (-14.195831577366326, 15.534752618206774, 18.6060759678674), (0.885662, 0.885662, 0.885662), "PWM_Quarry_1X1x1_C121", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1322.6292, 2582.0107, 3985.2588), (-0.06021005714909259, -93.71369023184921, -22.655459248801858), (0.885662, 0.885662, 0.885662), "PWM_Quarry_1X1x1_C122", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1659.3743, 2684.6575, 4040.35), (0.0, -44.293640124225796, 0.0), (0.6912076, 0.6912076, 0.6912076), "PWM_Quarry_1X1x1_C123_309", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1794.5647, 2829.026, 4023.9893), (12.142308161472242, -88.79333347943601, -86.44709169579718), (0.4388178, 0.4388178, 0.60635513), "PWM_Quarry_1X1x1_C124", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1353.1613, 2253.9895, 4172.672), (-8.312897801692031, -64.8541920461767, 17.118844632438215), (0.30997467, 0.30997467, 0.30997467), "PWM_Quarry_1X1x1_C125_328", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1377.6316, 2283.1953, 4153.1084), (26.35108316706319, -23.17623698681082, -86.29162949460482), (0.309975, 0.309975, 0.309975), "PWM_Quarry_1X1x1_C126", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1624.7583, 1488.6436, 4333.609), (0.0, -55.30758404753468, 0.0), (1.0, 1.3847419, 1.0), "PWM_Quarry_1X1x1_C127_345", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1570.9677, 1571.4033, 4333.609), (0.0, 125.37451804858378, -0.0), (1.0, 1.384742, 1.0), "PWM_Quarry_1X1x1_C128", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3280.1777, 1148.4481, 3365.8296), (0.0, -10.78387389852282, 0.0), (0.7169824, 0.7169824, 0.7169824), "PWM_Quarry_1X1x1_C129_390", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2793.7715, 2537.8245, 2876.5518), (-1.598081588912939, 78.96809321706537, -94.31846138969686), (2.25, 1.5, 1.5), "PWM_Quarry_1X1x1_C13", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3403.204, 1096.5492, 3365.8296), (0.0, -84.96605845925629, 0.0), (0.716982, 1.2980996, 0.716982), "PWM_Quarry_1X1x1_C130", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3129.694, 1126.7267, 3365.8296), (0.0, -97.41540441937335, 0.0), (0.716982, 1.2981, 0.716982), "PWM_Quarry_1X1x1_C131", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3729.8303, 1106.4071, 3365.8296), (0.0, -68.1147752784118, 0.0), (0.716982, 1.2981, 0.716982), "PWM_Quarry_1X1x1_C132", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3881.8457, 1141.3251, 3365.8296), (0.0, 54.02969670958602, -0.0), (0.716982, 1.2981, 0.716982), "PWM_Quarry_1X1x1_C133", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4449.847, 1098.6171, 3391.4666), (0.0, 0.0, -0.0), (1.0, 1.0, 1.0), "PWM_Quarry_1X1x1_C134_397", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3017.7292, 2253.6414, 3365.8296), (0.0, -97.41540441937335, 0.0), (0.716982, 1.2981, 0.716982), "PWM_Quarry_1X1x1_C135", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3176.087, 2325.9001, 3365.8296), (0.0, 134.2617655231918, -0.0), (0.716982, 1.2981, 0.716982), "PWM_Quarry_1X1x1_C136", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2965.7393, 2139.6108, 3324.9082), (5.179234371787862e-05, 134.26136893349903, -100.69191902001063), (0.716982, 0.62360233, 0.716982), "PWM_Quarry_1X1x1_C137", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3184.4612, 2144.2202, 3312.7192), (-8.00286826535471, 2.389495485392064, -82.88580347667762), (1.027374, 0.623602, 0.716982), "PWM_Quarry_1X1x1_C138", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3215.512, 2253.1921, 3328.6328), (-10.295714793980583, 28.43490722930107, -87.09884965968976), (1.027374, 0.623602, 0.716982), "PWM_Quarry_1X1x1_C139", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2919.8381, 2498.0298, 3077.5847), (-0.7970923405609106, -75.60531164397484, -89.40850029659052), (2.25, 1.5, 1.5), "PWM_Quarry_1X1x1_C14", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3029.652, 2164.3813, 3328.5142), (5.179234371787862e-05, 134.26136893349903, -100.69191902001063), (0.716982, 0.623602, 0.716982), "PWM_Quarry_1X1x1_C140", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5723.802, 4846.4517, 4012.4907), (-9.69699044589586, 54.064438650105146, 60.02048235361901), (1.0, 1.0, 1.0), "PWM_Quarry_1X1x1_C141_413", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5885.9473, 5235.924, 4043.5266), (6.7120883585717, 54.37453988593982, -64.9783678651908), (1.4466897, 1.0, 1.0), "PWM_Quarry_1X1x1_C142", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (6104.5864, 5235.924, 4021.9238), (6.712088328722508, -18.39245834722704, -64.97934577058592), (1.44669, 1.0, 1.0), "PWM_Quarry_1X1x1_C143", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5590.645, 1087.9136, 3997.583), (0.0, 81.75132658531469, -0.0), (0.68979836, 0.68979836, 1.0), "PWM_Quarry_1X1x1_C144_449", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5435.764, 985.85144, 4051.8474), (32.28884724739754, 91.72607923650715, 0.9224624802326357), (1.0, 1.0, 1.0), "PWM_Quarry_1X1x1_C145", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5146.242, 886.05286, 3953.5464), (-10.358276714511213, 34.41750523965229, 109.84342645605722), (1.9314969, 1.9314969, 1.9314969), "PWM_Quarry_1X1x1_C146", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5875.915, 927.9962, 3997.583), (0.0, 22.243323476721248, -0.0), (0.689798, 0.689798, 1.0), "PWM_Quarry_1X1x1_C147", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5674.1104, 917.4166, 4041.4114), (0.0, 22.243323476721248, -0.0), (1.4165977, 0.689798, 1.0), "PWM_Quarry_1X1x1_C148", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4780.7744, 962.5557, 4017.2424), (12.953876989167036, -7.734496937220054, -1.7437744724408615), (1.8552154, 0.689798, 1.0), "PWM_Quarry_1X1x1_C149", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4844.7695, 1896.7012, 2905.1035), (2.807887056998222, -36.57251554337699, -100.01620384028757), (2.25, 1.5, 1.5), "PWM_Quarry_1X1x1_C15", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4926.553, 1858.0928, 2929.8425), (1.0528515782970858, -36.39148201213924, -100.04198665221082), (2.25, 1.5, 1.5), "PWM_Quarry_1X1x1_C16", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4817.8584, 1751.0052, 3115.8745), (-5.638977680904761, 168.77736231329698, -85.3582527639406), (2.25, 1.5, 1.5), "PWM_Quarry_1X1x1_C17", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3528.7751, 2662.6272, 2213.7173), (-17.497466828584372, -47.65997268442237, 8.189593394679553), (1.586906, 1.586906, 1.586906), "PWM_Quarry_1X1x1_C18_29", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3528.7751, 2662.6272, 2334.8188), (-17.497466828584372, -47.65997268442237, 8.189593394679553), (1.586906, 1.586906, 1.586906), "PWM_Quarry_1X1x1_C19", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3001.4036, 3185.9656, 1285.551), (0.0, 178.2214087560601, -0.0), (1.0, 1.0, 1.6700628), "PWM_Quarry_1X1x1_C2_11", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (866.88965, 1082.2461, 1095.0039), (3.5212614753152494, 154.3292267297933, 89.89105582236921), (2.25, 1.5, 1.5), "PWM_Quarry_1X1x1_C20", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (546.88965, 1032.2461, 1095.0039), (3.5212611534500895, -157.85808893698356, 89.89104892704945), (2.25, 1.5, 1.5), "PWM_Quarry_1X1x1_C21", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (996.88965, 832.2461, 1095.0039), (3.5212628454954564, -53.79590754815485, 89.89106575781902), (2.25, 1.5, 1.5), "PWM_Quarry_1X1x1_C22", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (916.88965, 532.2461, 1215.0039), (2.095003099944974, -112.14517063528184, -89.79797432442784), (2.25, 1.5, 1.5), "PWM_Quarry_1X1x1_C23", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (801.2258, 3222.5713, 773.11237), (4.906520155944081, 35.12984238918639, -71.34139529447455), (2.25, 1.5, 1.5), "PWM_Quarry_1X1x1_C24_41", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3838.6821, 279.2481, 491.86615), (-16.81214043827866, 49.6144221281741, -89.59542840938714), (2.25, 1.5, 1.5), "PWM_Quarry_1X1x1_C24_105", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5574.16, 3850.3047, 4169.983), (25.870031866218227, 36.24617875788649, -65.28875415292487), (2.25, 1.5, 1.5), "PWM_Quarry_1X1x1_C24_243", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3373.211, 2189.8674, 676.1736), (0.13485422615956777, 34.982373118245846, -74.69086415954759), (2.25, 1.5, 1.5), "PWM_Quarry_1X1x1_C24_673", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (556.7615, 1016.3928, 1470.5576), (13.658764534879673, 29.115539993579027, -78.2493720322455), (2.46875, 1.71875, 1.71875), "PWM_Quarry_1X1x1_C25", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (926.88965, 662.2461, 1755.0039), (28.324374549249388, -107.07735043732445, 63.963561470336664), (2.25, 1.5, 1.5), "PWM_Quarry_1X1x1_C26", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (856.88965, 422.2461, 1645.0039), (-72.0735290321164, 121.81513484348325, -163.5585287442648), (2.25, 1.5, 1.5), "PWM_Quarry_1X1x1_C27", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3524.6719, 2774.257, 1827.6992), (-17.497282367697334, -31.97112778998415, 8.189919970675467), (1.586906, 1.586906, 1.8076719), "PWM_Quarry_1X1x1_C28", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3333.448, 3160.064, 1806.5642), (0.0, 0.0, -0.0), (1.0, 1.0, 1.0), "PWM_Quarry_1X1x1_C29_37", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3409.3135, 2725.295, 1021.8048), (-21.34649611905979, 0.0, -0.0), (1.3951049, 1.3951049, 1.7923759), "PWM_Quarry_1X1x1_C3_22", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3524.6719, 2774.257, 1980.6923), (-17.497282367697334, -31.97112778998415, 8.189919970675467), (1.586906, 1.586906, 1.807672), "PWM_Quarry_1X1x1_C30", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (378.45282, 3416.8796, 1699.1738), (2.590939219449784, -91.42899410850823, 82.58903193058497), (1.729816, 1.729816, 1.729816), "PWM_Quarry_1X1x1_C31_19", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3868.5916, 448.18555, 1513.9465), (0.9722283706959175, -77.9933146309488, 110.79220116071744), (1.729816, 1.729816, 1.729816), "PWM_Quarry_1X1x1_C31_83", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4850.876, 4039.4126, 4921.0103), (-5.452881431686665, -91.43565648145648, 62.35826150977319), (1.729816, 1.729816, 1.729816), "PWM_Quarry_1X1x1_C31_221", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3046.6487, 2484.1758, 1640.3748), (2.7226173544431678, -91.15841964252523, 88.42128344289031), (1.729816, 1.729816, 1.729816), "PWM_Quarry_1X1x1_C31_651", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (348.68353, 3425.0198, 1846.1848), (0.8469651260082443, -80.29418894392882, 83.21875002855508), (1.729816, 1.729816, 1.729816), "PWM_Quarry_1X1x1_C32_20", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3910.1438, 460.2772, 1657.7933), (-5.777759514764181, -68.96115869129059, 110.70670629152217), (1.729816, 1.729816, 1.729816), "PWM_Quarry_1X1x1_C32_84", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4771.6006, 4029.9946, 5048.256), (-3.1159576876142183, -80.38381593899301, 61.824530930800606), (1.729816, 1.729816, 1.729816), "PWM_Quarry_1X1x1_C32_222", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3031.9597, 2492.316, 1789.6486), (-0.1380930074904719, -80.25859974129592, 88.9625421383031), (1.729816, 1.729816, 1.729816), "PWM_Quarry_1X1x1_C32_652", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3694.5261, 2624.668, 2844.03), (0.0, 0.0, -0.0), (1.4313675, 1.4313675, 1.4313675), "PWM_Quarry_1X1x1_C33_44", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (327.1589, 3424.4846, 1729.156), (11.578421932467677, 50.33779856933859, -78.32777606042367), (1.729816, 1.729816, 1.729816), "PWM_Quarry_1X1x1_C34_21", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3836.9922, 447.42114, 1564.826), (-5.281309119697313, 61.59750387492495, -101.09426039810164), (1.729816, 1.729816, 1.729816), "PWM_Quarry_1X1x1_C34_85", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4792.2446, 4044.8179, 4932.009), (30.04388326694641, 54.28894943546322, -65.95257186194917), (1.729816, 1.729816, 1.729816), "PWM_Quarry_1X1x1_C34_223", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2998.664, 2491.7808, 1675.4093), (7.8272012262082615, 49.57433624620814, -82.85297398420553), (1.729816, 1.729816, 1.729816), "PWM_Quarry_1X1x1_C34_653", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (375.67496, 3300.8613, 1880.1814), (7.4832610801365265, -38.24281264711417, 87.62677117096135), (1.729816, 1.729816, 1.729816), "PWM_Quarry_1X1x1_C35_22", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3975.1235, 346.6528, 1670.7068), (-15.89851877532521, -26.907524503438108, 103.61039816474018), (1.729816, 1.729816, 1.729816), "PWM_Quarry_1X1x1_C35_86", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4786.7993, 3901.7617, 5073.2603), (18.223488812647517, -43.14420541359069, 68.18997475631687), (1.729816, 1.729816, 1.729816), "PWM_Quarry_1X1x1_C35_224", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3062.264, 2368.1575, 1820.7334), (2.8946210973879203, -37.916109654494, 91.23470251666507), (1.729816, 1.729816, 1.729816), "PWM_Quarry_1X1x1_C35_654", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3229.6953, 3445.3577, 2612.6943), (10.329327599694777, 149.03742871531048, -1.7793578122157647), (1.6287861, 1.4741442, 1.559206), "PWM_Quarry_1X1x1_C36_50", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3477.7244, 3453.417, 2934.6338), (-4.101348418646019, 13.79547640084347, 9.546344075773492), (1.1886692, 1.1886692, 1.1886692), "PWM_Quarry_1X1x1_C37_53", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3318.8042, 3544.455, 3003.9216), (-13.48202392547131, 154.19093930782523, -8.728392218859039), (1.188669, 1.188669, 1.188669), "PWM_Quarry_1X1x1_C38", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3247.3188, 3570.822, 3023.344), (-13.48202392547131, 154.19093930782523, -8.728392218859039), (1.188669, 1.188669, 1.188669), "PWM_Quarry_1X1x1_C39", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3390.907, 2716.8745, 1141.9585), (21.421568941865377, -179.99998474121062, -179.99998474121062), (1.395105, 1.395105, 1.792376), "PWM_Quarry_1X1x1_C4", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2521.339, 2488.8816, 2314.958), (3.849072438414928e-05, -54.198124157845555, -34.656221031402325), (1.1784867, 1.0, 1.3216687), "PWM_Quarry_1X1x1_C40_76", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2438.242, 2604.0906, 2314.958), (3.849072438414928e-05, -54.198124157845555, -34.656221031402325), (1.178487, 1.0, 1.321669), "PWM_Quarry_1X1x1_C41", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2794.3992, 2138.786, 1668.0624), (0.0, 159.72975497637526, -0.0), (1.0, 1.0, 1.0), "PWM_Quarry_1X1x1_C42_83", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2965.619, 2043.4827, 1180.5841), (0.0, 0.0, -0.0), (1.0, 1.0, 1.0), "PWM_Quarry_1X1x1_C43_101", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3178.6345, 2189.247, 1672.7112), (-2.6323807546841883e-08, 33.408482391796575, 18.528646314625327), (1.0, 1.0, 1.5367211), "PWM_Quarry_1X1x1_C44_104", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (869.2754, 1060.8639, 1245.5087), (-3.5100402840746865, -19.04800275132449, 85.7639086030664), (2.25, 1.5, 1.5), "PWM_Quarry_1X1x1_C45", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (946.15356, 811.7002, 1208.5474), (5.375521505467047, 98.31700216038728, 88.83823006070247), (2.25, 1.5, 1.5), "PWM_Quarry_1X1x1_C46", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (940.18823, 897.0403, 1140.8737), (5.375521505467047, 98.31700216038728, 88.83823006070247), (2.25, 1.5, 1.5), "PWM_Quarry_1X1x1_C47", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (834.72174, 457.97824, 1515.0192), (-72.0735290321164, 121.81513484348325, -163.5585287442648), (2.25, 1.5, 1.5), "PWM_Quarry_1X1x1_C48", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (886.0986, 590.478, 1614.9998), (-72.0735290321164, 121.81513484348325, -163.5585287442648), (2.25, 1.5, 1.5), "PWM_Quarry_1X1x1_C49", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (886.5525, 928.9607, 1499.4316), (3.455650462824871, 105.29969774949433, -89.99036027107269), (2.129103, 2.129103, 2.129103), "PWM_Quarry_1X1x1_C5", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (907.5096, 555.9656, 1740.5496), (-72.0735290321164, 121.81513484348325, -163.5585287442648), (2.25, 1.5, 1.5), "PWM_Quarry_1X1x1_C50", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (717.76965, 1058.166, 1095.0039), (3.5212611534500895, -157.85808893698356, 89.89104892704945), (2.25, 1.5, 1.5), "PWM_Quarry_1X1x1_C51", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (556.7615, 1016.3927, 1308.5005), (-3.2528688496933786, 28.266542327029192, -87.4891029005469), (2.46875, 1.71875, 1.71875), "PWM_Quarry_1X1x1_C52", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (975.26074, 597.35034, 2188.1614), (-51.42956203826452, -20.199737594974525, -12.520232052271032), (1.6468114, 1.6468114, 2.227584), "PWM_Quarry_1X1x1_C53_134", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1025.1772, 597.35034, 2300.4814), (-51.42977498991284, -7.134491176414312, -12.519498652493995), (1.646811, 1.646811, 2.227584), "PWM_Quarry_1X1x1_C54", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3633.8154, 4146.266, 979.0731), (0.0, 0.0, -0.0), (1.0, 1.0, 1.0), "PWM_Quarry_1X1x1_C55_148", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3529.6787, 3992.5498, 635.3011), (0.0, 0.0, -0.0), (1.0, 1.0, 1.0), "PWM_Quarry_1X1x1_C56_154", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1939.1233, 4428.922, 976.0324), (0.0, -7.819274087339147, 0.0), (1.0, 1.0, 1.0), "PWM_Quarry_1X1x1_C57_189", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3763.6206, 4175.205, 1623.3518), (0.0, 0.0, 9.167492200584661), (1.0, 1.0, 1.0), "PWM_Quarry_1X1x1_C58_211", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3686.0144, 4175.2314, 1447.4453), (0.0, 0.0, -0.0), (1.0, 1.0, 1.0), "PWM_Quarry_1X1x1_C59_214", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3996.1477, 2463.3179, 3217.08), (-2.9267887522295224, 146.0507792379953, 85.17470121755969), (2.25, 1.5, 1.5), "PWM_Quarry_1X1x1_C6_162", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1256.46, 5324.626, 812.44775), (0.0, 0.0, -0.0), (1.0, 1.0, 1.0), "PWM_Quarry_1X1x1_C60_219", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1540.0656, 6237.0464, 1751.7059), (0.0, -16.870452854155563, 0.0), (1.1417123, 0.8868936, 1.5740997), "PWM_Quarry_1X1x1_C61_241", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1304.9802, 6256.498, 1751.7059), (0.0, 7.910722392067711, -0.0), (1.4009198, 0.886894, 1.8471295), "PWM_Quarry_1X1x1_C62", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1304.9802, 6256.498, 1573.4369), (0.0, 7.910721699628708, -0.0), (1.40092, 0.886894, 1.847129), "PWM_Quarry_1X1x1_C63", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1713.7611, 5849.882, 2126.291), (0.0, 30.034329261962846, -0.0), (1.0, 1.9075553, 1.0), "PWM_Quarry_1X1x1_C64_258", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1583.4436, 5395.513, 1236.1615), (0.05496774200978738, -8.577149157940461, 64.08612323462795), (1.2719425, 1.1475489, 1.3754835), "PWM_Quarry_1X1x1_C65_265", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1564.4886, 6181.7246, 1563.8698), (0.0, 0.0, -0.0), (1.0, 1.0, 1.0), "PWM_Quarry_1X1x1_C66_277", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2879.5942, 5440.7573, 3627.872), (0.0, 0.0, -0.0), (1.0, 1.0, 1.0), "PWM_Quarry_1X1x1_C67_292", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1400.49, 5071.0933, 3851.352), (0.0, 15.972960870067636, -0.0), (1.0, 1.0, 1.0), "PWM_Quarry_1X1x1_C68_308", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1147.2826, 1632.2842, 3076.151), (69.51794864917997, 43.12452137811527, 4.344195819593716), (1.1577623, 1.9036294, 1.1577623), "PWM_Quarry_1X1x1_C69_345", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3823.4387, 2649.0366, 3193.8425), (-1.1625999807808978, 146.0298861623942, 85.14355703911463), (2.25, 1.5, 1.5), "PWM_Quarry_1X1x1_C7", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (768.6959, 1848.9832, 2535.8936), (0.0, 0.0, -0.0), (1.0, 1.0, 1.0), "PWM_Quarry_1X1x1_C70_351", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (664.4911, 5303.7114, 852.87067), (0.0, -52.39306959059476, 0.0), (0.66709495, 0.66709495, 0.66709495), "PWM_Quarry_1X1x1_C71_66", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (901.04364, 5211.798, 852.87067), (0.0, 8.061170705826386, -0.0), (0.667095, 0.667095, 0.667095), "PWM_Quarry_1X1x1_C72", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (937.8641, 5327.974, 869.3697), (0.0, -170.58985672094866, 0.0), (0.667095, 0.667095, 0.667095), "PWM_Quarry_1X1x1_C73", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1233.933, 5210.4424, 849.5486), (0.0, 117.65140001251297, -0.0), (0.667095, 0.667095, 0.667095), "PWM_Quarry_1X1x1_C74", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (485.24792, 3795.4587, 810.1116), (0.0, 0.0, -113.00280135693524), (0.5162375, 0.5162375, 0.5162375), "PWM_Quarry_1X1x1_C75_72", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (846.2468, 3797.239, 738.35187), (0.0, 12.28276750688213, -0.0), (0.5010301, 0.5010301, 0.5010301), "PWM_Quarry_1X1x1_C76_78", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (987.2273, 3780.4858, 660.8471), (0.0, 174.0981846730962, -0.0), (0.50103, 0.50103, 0.50103), "PWM_Quarry_1X1x1_C77", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (338.79367, 5302.162, 833.6584), (0.0, 166.92668366611417, -0.0), (0.9564326, 0.9564326, 0.9564326), "PWM_Quarry_1X1x1_C78_86", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (503.65857, 5304.3926, 844.98694), (0.0, -104.21511460423532, 0.0), (0.83039486, 0.83039486, 0.83039486), "PWM_Quarry_1X1x1_C79_89", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2606.6777, 1322.3284, 3217.08), (-2.9267565816943804, -93.0117228506607, 85.17471018382857), (2.25, 1.5, 1.5), "PWM_Quarry_1X1x1_C8", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (409.04407, 3714.1052, 702.2313), (-16.37786466410324, 1.0674779490901276, -85.57513523962888), (1.00361, 1.00361, 1.00361), "PWM_Quarry_1X1x1_C8_7", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3366.2358, 676.40735, 631.49146), (-44.45846028020253, 15.42968365311415, -89.06459859380524), (1.00361, 1.00361, 1.00361), "PWM_Quarry_1X1x1_C8_71", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5222.96, 4458.168, 4043.8735), (4.231667715489468, 1.3057462336577514, -92.60364399984466), (1.00361, 1.00361, 1.00361), "PWM_Quarry_1X1x1_C8_209", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2975.8591, 2781.4011, 645.4783), (-22.20428084345287, 1.1061994896244256, -85.69219504330238), (1.00361, 1.00361, 1.00361), "PWM_Quarry_1X1x1_C8_639", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (575.0283, 5275.4, 837.5376), (0.0, -53.55974980281217, 0.0), (0.830395, 0.830395, 0.830395), "PWM_Quarry_1X1x1_C80", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (438.18677, 5191.0444, 806.2737), (-2.4538274984653103, -72.54559852538081, -23.22577025460721), (0.9253018, 0.68379647, 0.68379647), "PWM_Quarry_1X1x1_C81", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2604.2947, 2656.2925, 823.91534), (0.0, 76.37966032604538, -0.0), (1.0, 1.0, 1.0), "PWM_Quarry_1X1x1_C82_94", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2504.308, 2571.2732, 810.00854), (0.0, 145.0732334537344, -0.0), (0.61805046, 0.61805046, 0.61805046), "PWM_Quarry_1X1x1_C83", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (792.16974, 1296.049, 839.63214), (0.0, 0.0, -0.0), (0.60707974, 0.60707974, 0.60707974), "PWM_Quarry_1X1x1_C84_106", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5210.199, 996.2742, 832.0642), (0.0, 92.75637986402168, -0.0), (0.6831923, 0.6831923, 0.6831923), "PWM_Quarry_1X1x1_C85_153", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5210.199, 839.5168, 804.9044), (0.0, -179.2054239272949, 0.0), (0.683192, 0.683192, 0.683192), "PWM_Quarry_1X1x1_C86", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5243.7603, 554.4031, 818.2733), (0.0, 76.71326933316936, -0.0), (0.683192, 0.683192, 0.683192), "PWM_Quarry_1X1x1_C87", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5275.815, 367.18234, 814.7686), (0.0, -179.97551376908288, 0.0), (0.94871086, 0.94871086, 0.94871086), "PWM_Quarry_1X1x1_C88", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5139.886, 1051.5468, 809.7035), (0.0, 176.1987603165326, -0.0), (0.683192, 0.683192, 0.683192), "PWM_Quarry_1X1x1_C89", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2582.5466, 1234.7542, 3193.8425), (-1.1625718249058854, -93.03272043092139, 85.1434921542857), (2.25, 1.5, 1.5), "PWM_Quarry_1X1x1_C9", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5057.4976, 1890.6754, 769.4259), (0.0, 95.89317972395733, -0.0), (0.76471335, 0.76471335, 0.76471335), "PWM_Quarry_1X1x1_C90", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4959.416, 1837.7983, 743.4398), (0.0, -139.22995625154343, 0.0), (0.764713, 0.764713, 0.764713), "PWM_Quarry_1X1x1_C91", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5170.2905, 1621.8143, 769.4259), (0.0, 95.89317972395733, -0.0), (0.764713, 0.764713, 0.764713), "PWM_Quarry_1X1x1_C92", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4924.0176, 2402.8848, 686.9082), (0.0, 95.89317972395733, -0.0), (0.764713, 0.764713, 0.764713), "PWM_Quarry_1X1x1_C93", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4924.0176, 2531.7778, 661.92487), (-32.974541657940435, 175.62977823863656, -177.61834000805783), (0.764713, 0.764713, 0.764713), "PWM_Quarry_1X1x1_C94", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3387.057, 3861.5215, 630.8723), (-85.00824761811808, 134.28844169944702, 55.66839327634288), (0.7567172, 0.7567172, 1.1685942), "PWM_Quarry_1X1x1_C95_169", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3366.7937, 3958.6733, 699.24695), (-48.76682200313633, 118.03387297702503, -22.801910162603736), (0.756717, 0.756717, 0.756717), "PWM_Quarry_1X1x1_C96", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3168.4363, 3879.3271, 624.67114), (-48.76674561011038, -109.04860288949173, -22.801382862959294), (0.756717, 0.756717, 0.756717), "PWM_Quarry_1X1x1_C97", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2852.657, 4067.7554, 649.45056), (-48.76674561011038, -109.04860288949173, -22.801382862959294), (1.2685084, 1.2685084, 1.2685084), "PWM_Quarry_1X1x1_C98", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2580.3865, 4135.449, 638.1683), (-42.3601685549964, -134.84070492137235, -33.12173743586466), (1.268508, 1.268508, 1.268508), "PWM_Quarry_1X1x1_C99", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (6051.102, 2831.1255, 1261.113), (-13.845489595156984, -98.89533014441142, 10.289691342971043), (0.82483745, 0.82483745, 0.82483745), "StaticMeshActor_18569", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (6142.9453, 2845.0083, 1243.7953), (-7.305053285596502, -83.24686581461472, 3.6497211765295523), (1.0144684, 1.0144684, 1.0144684), "StaticMeshActor_18570", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (6354.6064, 3154.0022, 1350.8853), (-3.07861283879748, -86.23816472009624, 12.721185700055896), (0.86247724, 0.86247724, 0.86247724), "StaticMeshActor_18571", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (6446.4067, 3572.128, 1252.8479), (-1.9788818788311582, -4.714263420907384, 34.76510065189085), (1.0948505, 1.0948505, 1.0948505), "StaticMeshActor_18572", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3760.0784, 4851.2417, 5866.628), (-4.537291796249224, -178.6798725610657, 4.083955030207634), (0.9331757, 0.9331757, 0.9331757), "StaticMeshActor_18601", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4445.2783, 4152.928, 5930.175), (-7.269713440251377, -87.65677239377177, -3.1545405432538587), (0.8351246, 0.8351246, 0.8351246), "StaticMeshActor_18604", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4434.935, 4044.831, 5937.7), (8.907098290376165, 97.24717859503596, -2.1828914114652114), (0.92549, 0.92549, 0.92549), "StaticMeshActor_18605", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4423.264, 4044.1313, 5931.3296), (-8.347624691921133, 175.32263742447594, 2.331221045590453), (1.0108835, 1.0108835, 1.0108835), "StaticMeshActor_18606", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2650.7297, 5842.6113, 817.8762), (-5.417601857520382, 171.81726864058558, -7.091276859383647), (1.0999123, 1.0999123, 1.0999123), "StaticMeshActor_18611", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2851.6975, 332.99356, 4033.0408), (-2.0682375990457906, -85.49066302804081, -15.128419397096904), (0.87530345, 0.87530345, 0.87530345), "StaticMeshActor_18612", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3873.2722, 5668.499, 927.0535), (0.8361381229247025, -83.81377443467215, -7.997039287330125), (0.8197956, 0.8197956, 0.8197956), "StaticMeshActor_18613", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1873.2644, 4513.8877, 1174.0835), (6.0154429816640365, 83.04432892997836, 2.3285773298523207), (0.80983293, 0.80983293, 0.80983293), "StaticMeshActor_18614", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2072.6567, 4422.716, 1168.6501), (4.522540626349414, -176.45997709056292, 2.273088260067179), (0.8106406, 0.8106406, 0.8106406), "StaticMeshActor_18615", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1623.2094, 4777.547, 1172.2379), (-3.9763485334986743, -0.9657897620355407, -9.8628221221309), (0.913362, 0.913362, 0.913362), "StaticMeshActor_18616", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1935.3557, 5340.0103, 3944.5452), (-7.059752523581002, -99.61429491644085, 5.949618273386957), (0.8291666, 0.8291666, 0.8291666), "StaticMeshActor_18617", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1710.8278, 5292.6016, 3930.3645), (8.703067237175928, 5.8536471191846635, 4.095033030923264), (0.80784696, 0.80784696, 0.80784696), "StaticMeshActor_18618", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1405.0609, 5169.7036, 3863.7231), (-2.866333008923126, -80.98058145169752, -1.4604800246820744), (1.0284798, 1.0284798, 1.0284798), "StaticMeshActor_18619", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5488.0703, 3552.9507, 3933.5962), (0.34820984760859497, 83.25624781481571, -7.201812429876635), (1.0174518, 1.0174518, 1.0174518), "StaticMeshActor_18620", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5445.0337, 3256.8035, 3936.6697), (1.2498288665479131, -93.35567729616545, 5.9798499380935946), (0.94557464, 0.94557464, 0.94557464), "StaticMeshActor_18622", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5513.2354, 2028.0753, 3915.3904), (7.648656464447428, 9.383853230293102, 4.566962656858034), (1.0890917, 1.0890917, 1.0890917), "StaticMeshActor_18623", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3158.7537, 1943.023, 817.19415), (-9.611907085103695, -172.59680669082303, 9.849435618001054), (0.90964323, 0.90964323, 0.90964323), "StaticMeshActor_18624", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3108.851, 4239.8804, 1163.8978), (-25.753418211244252, -151.19590779165347, 7.129895432445607), (1.0, 1.0, 1.0), "StaticMeshActor_18625", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3455.2148, 5046.839, 1616.1664), (3.9891107627335223, 96.34924221884602, 7.289114717053286), (0.8116941, 0.8116941, 0.8116941), "StaticMeshActor_18626", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3406.518, 4199.258, 1628.1542), (-20.90664585803454, 90.11064541418284, 2.828744097871938), (1.0216297, 1.0216297, 1.0216297), "StaticMeshActor_18627", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3438.7686, 4216.2314, 1645.9078), (8.179493932996975, -170.32620085861774, -9.160705727902611), (0.83525544, 0.83525544, 0.83525544), "StaticMeshActor_18628", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1944.9042, 3696.01, 3926.1047), (-2.8863829463905692, -1.0640563917795411, 88.96201817590612), (1.0040848, 1.0040848, 1.0040848), "StaticMeshActor_18629", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1241.3135, 2415.3513, 4008.8938), (-6.07552949541679, -176.06561025052923, 9.267560159066155), (0.84671545, 0.84671545, 0.84671545), "StaticMeshActor_18630", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1491.2013, 2730.264, 3942.5232), (65.97375776190204, -11.877437390581921, -16.56210027546865), (1.0478635, 1.0478635, 1.0478635), "StaticMeshActor_18631", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1576.7216, 2641.3145, 3964.501), (-12.37359420972182, 165.25566762122884, -15.782989413499994), (0.9411829, 0.9411829, 0.9411829), "StaticMeshActor_18632", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (391.12418, 3645.7014, 4016.4268), (-13.050386025215914, 124.32157130800968, -7.168091423499744), (0.85706, 0.85706, 0.85706), "StaticMeshActor_18633", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3541.4658, 5076.0117, 1605.1276), (-3.800018148168702, -87.31678968733087, 9.52509639424732), (0.95115244, 0.95115244, 0.95115244), "StaticMeshActor_18634", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3534.9375, 5071.9404, 1517.0443), (6.894891012142722, -179.88564212837412, 8.320338413466217), (0.8253666, 0.8253666, 0.8253666), "StaticMeshActor_18635", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3433.0916, 5073.893, 1512.3711), (3.873775557305371, 8.722584028808495, 8.57375763492086), (0.90802264, 0.90802264, 0.90802264), "StaticMeshActor_18636", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3544.3137, 5060.921, 1401.2894), (-3.011963240416732, -86.18901816515046, 6.024651263130585), (0.91137856, 0.91137856, 0.91137856), "StaticMeshActor_18637", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2796.734, 902.78516, 4515.366), (1.9299036542520074, 146.8299384720088, 0.5520503482169345), (0.8891457, 0.8891457, 0.8891457), "StaticMeshActor_18638", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2552.84, 1120.9954, 4232.982), (-21.388675135322384, 97.38045750117455, 83.47449209865486), (2.0, 2.0, 2.0), "StaticMeshActor_18639", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3757.0342, 819.4445, 4308.377), (10.05921520345161, 103.10639345361145, 8.832441642797704), (1.0268673, 1.0268673, 1.0268673), "StaticMeshActor_18640", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3701.4807, 781.9012, 4231.6714), (-5.55401656911171, -151.7191309704865, 5.005792977155613), (0.86596715, 0.86596715, 0.86596715), "StaticMeshActor_18641", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3787.9985, 835.91125, 4203.662), (-5.366332820087359, 15.219449298750389, 7.845789580847496), (1.095021, 1.095021, 1.095021), "StaticMeshActor_18642", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3755.6687, 834.1297, 4204.443), (2.3331037969233264, 11.944221571919389, 4.99464698689065), (0.8378096, 0.8378096, 0.8378096), "StaticMeshActor_18643", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3700.758, 779.4401, 4122.6226), (0.5362858231161471, -154.59530843818368, 0.3929465019535255), (1.0849652, 1.0849652, 1.0849652), "StaticMeshActor_18644", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2960.783, 5244.926, 1102.8344), (-4.291259391846027, -3.780517337326785, 8.485195261700632), (1.0259349, 1.0259349, 1.0259349), "StaticMeshActor_18645", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3823.601, 5641.9116, 1021.7329), (4.013275264178658, -98.37716689898637, 5.326347254741326), (1.0466188, 1.0466188, 1.0466188), "StaticMeshActor_18646", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4548.694, 1872.9215, 3057.1382), (-5.787140862518374, -171.79445550333, -3.852478602125154), (0.83080965, 0.83080965, 0.83080965), "StaticMeshActor_18647", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4396.803, 1927.1122, 3038.1848), (-3.6742247851136387, 69.88848632016989, -7.419617242240312), (1.0795381, 1.0795381, 1.0795381), "StaticMeshActor_18648", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1689.4937, 2915.2932, 3785.6475), (-12.289308182449773, 119.3051369713061, -7.867798579872583), (0.93727857, 0.93727857, 0.93727857), "StaticMeshActor_18649", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2138.5684, 3040.4976, 3906.1926), (6.001447534365066, -3.172271732232866, 7.773568682264446), (1.0960128, 1.0960128, 1.0960128), "StaticMeshActor_18650", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1727.6224, 4597.0527, 1166.0967), (2.9095718035793965, 0.5299958791865764, -8.688171553829834), (1.0, 1.0, 1.0), "StaticMeshActor_18651", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (212.62798, 3618.8853, 4371.949), (1.9232099663244546, 119.33754704877988, -8.5061647827535), (0.88292634, 0.88292634, 0.88292634), "StaticMeshActor_18652", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (316.3459, 3621.6116, 4274.2065), (10.788082851873693, -150.15003435540027, 3.48787271641073), (0.8927263, 0.8927263, 0.8927263), "StaticMeshActor_18653", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (372.7289, 3583.8325, 4491.163), (4.108029489192931, -58.613096121379655, 161.55608930845665), (1.1875, 1.1875, 1.1875), "StaticMeshActor_18655", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (6255.6255, 3254.162, 2597.9524), (-16.273680298368326, 6.821878065021753, 6.061563389609518), (1.0334971, 1.0334971, 1.0334971), "StaticMeshActor_18656", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2861.5042, 753.53015, 4505.7837), (-19.732545424175846, 55.47944461242142, 12.197115342953191), (0.95348114, 0.95348114, 0.95348114), "StaticMeshActor_18657", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2766.215, 698.2411, 4271.891), (-0.8222962460698214, -64.7879295186943, 1.1776627620404814), (0.9964017, 0.9964017, 0.9964017), "StaticMeshActor_18658", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2831.5193, 830.2716, 4470.964), (9.282219555002701, -25.1780412267126, 19.523935173769065), (0.9407198, 0.9407198, 0.9407198), "StaticMeshActor_18659", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2821.1401, 632.9652, 4297.6235), (-1.1683956460559917, -89.43571548368433, -7.241301230510244), (1.0198898, 1.0198898, 1.0198898), "StaticMeshActor_18660", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5250.8525, 779.39294, 4259.0674), (-0.04663083775271687, -98.3482584961543, -0.4976502104389952), (1.0112569, 1.0112569, 1.0112569), "StaticMeshActor_18661", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5290.666, 806.25073, 4180.7983), (-4.180907821031281, 178.81842455435822, -6.059661266857935), (1.0270889, 1.0270889, 1.0270889), "StaticMeshActor_18662", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2901.7568, 3241.1743, 1838.001), (-14.609616641662775, 141.740653800486, 13.787395940106599), (0.85771006, 0.85771006, 0.85771006), "StaticMeshActor_18665", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2883.5747, 3328.093, 1940.8724), (2.110194746510747, 51.52541534897728, 29.16302333754621), (0.95250046, 0.95250046, 0.95250046), "StaticMeshActor_18666", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2901.9534, 3235.507, 1937.726), (-6.168579238177404, 73.8989596296343, 15.94142582323888), (0.84174156, 0.84174156, 0.84174156), "StaticMeshActor_18667", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2890.444, 3282.884, 1841.5992), (13.123817214011428, -140.7909079789463, -11.163330165839165), (1.0350194, 1.0350194, 1.0350194), "StaticMeshActor_18668", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2129.6133, 5386.631, 3764.3252), (9.246407889862303, -177.3230318304059, 4.6283837545197795), (0.93206984, 0.93206984, 0.93206984), "StaticMeshActor_18669", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1838.1846, 5313.6006, 3781.2297), (7.030129583880394, -93.08099905515488, 3.0468586296668696), (0.9215311, 0.9215311, 0.9215311), "StaticMeshActor_18670", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1429.8453, 5114.208, 3766.9443), (4.711382408441977, 4.6320562193309875, -3.220855806113398), (0.9770503, 0.9770503, 0.9770503), "StaticMeshActor_18671", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2654.705, 5760.5303, 903.0476), (7.934425948808304, 1.2950871440797946, 1.8930249224268618), (0.8101023, 0.8101023, 0.8101023), "StaticMeshActor_18672", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5273.562, 76.94614, 5025.051), (-7.275542919720829, -167.7383137442984, -21.239867296950766), (0.83657146, 0.83657146, 0.83657146), "StaticMeshActor_18673", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1252.8636, 3249.7764, 5807.1606), (5.767861870851281, 90.27073096414776, 30.166791149295793), (0.81348443, 0.81348443, 0.81348443), "StaticMeshActor_18674", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2950.3726, 3279.0176, 1832.8942), (20.889251247800278, -84.70092527544489, 3.907266788895883), (0.8634276, 0.8634276, 0.8634276), "StaticMeshActor_18681", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4224.749, 2138.6816, 3015.756), (-8.082062366019702, 19.935600530905877, 6.55836206367749), (0.80763537, 0.80763537, 0.80763537), "StaticMeshActor_18683", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2993.0374, 2099.039, 1864.5884), (16.223549342292838, 101.20208340911536, -4.264771234768115), (1.0851539, 1.0851539, 1.0851539), "StaticMeshActor_18684", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3154.6187, 1954.5242, 903.9536), (-6.99099733262037, -82.76513821149413, -8.37356578065174), (0.99333847, 0.99333847, 0.99333847), "StaticMeshActor_18685", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5948.3164, 2855.3872, 1303.9679), (32.50351034381826, 81.9491753530566, -13.37436141778587), (0.83865064, 0.83865064, 0.83865064), "StaticMeshActor_18686", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5956.666, 2798.9863, 1297.7626), (24.716119256770263, 81.45049830391274, -4.003751933633634), (0.8617852, 0.8617852, 0.8617852), "StaticMeshActor_18687", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5864.3936, 2788.1755, 1299.4883), (-4.186645887659157, -175.907068686506, 32.018578344413605), (0.9596099, 0.9596099, 0.9596099), "StaticMeshActor_18688", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (6263.1367, 2806.2737, 1275.0161), (0.7552959614928014, -2.778259467779191, -18.783997371744498), (1.0221182, 1.0221182, 1.0221182), "StaticMeshActor_18689", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (6360.0415, 2812.6218, 1271.2122), (-16.826930935215138, -98.20182700540768, 7.622902110037675), (0.8081015, 0.8081015, 0.8081015), "StaticMeshActor_18690", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5348.4473, 1772.7458, 1075.3018), (0.6713939705684682, 7.406544583677032, -0.31219480430584934), (0.8188034, 0.8188034, 0.8188034), "StaticMeshActor_18691", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5367.016, 1759.0833, 991.5376), (-2.4180603021086338, -85.8236059534191, -9.460723438379327), (0.9036969, 0.9036969, 0.9036969), "StaticMeshActor_18692", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5430.152, 1659.887, 1062.9983), (-6.683074211788089, -8.633818967752518, 2.9065726051930283), (0.83834624, 0.83834624, 0.83834624), "StaticMeshActor_18693", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5497.032, 1631.1262, 3886.2434), (8.44711910051335, 5.206641588131204, 9.84574720618115), (1.0786355, 1.0786355, 1.0786355), "StaticMeshActor_18694", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5434.9214, 1656.3375, 3804.8262), (8.307059210557105, -94.18267229375465, -1.7181088292581446), (1.015312, 1.015312, 1.015312), "StaticMeshActor_18695", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5409.4785, 2140.7383, 3789.835), (-2.812037363188, -81.56058913776074, 75.93794427060013), (1.0, 1.057215, 1.0572155), "StaticMeshActor_18696", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3368.9036, 4273.8276, 1547.4432), (-7.763885116618181, 96.9907331469237, -3.818725300471173), (0.9856858, 0.9856858, 0.9856858), "StaticMeshActor_18697", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2970.701, 4439.674, 1355.611), (4.290499592646447, -92.91155401678648, -7.740173609409378), (0.97375315, 0.97375315, 0.97375315), "StaticMeshActor_18698", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (717.86285, 2932.161, 4734.6904), (-24.149502384494678, -72.35173565226285, -44.62451504664773), (0.80235463, 0.80235463, 0.80235463), "StaticMeshActor_18699", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (646.2027, 2844.2732, 4706.711), (38.30609888377611, 100.34738543259137, 39.71865826674294), (0.80320776, 0.80320776, 0.80320776), "StaticMeshActor_18700", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1548.3278, 2685.078, 3908.385), (-6.230804859350979, -19.972871390868512, -9.731263223152498), (1.0071186, 1.0071186, 1.0071186), "StaticMeshActor_18701", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1609.7335, 2819.2065, 3808.9885), (5.638866213588317, 155.8657427009537, 3.557155441316684), (0.8290564, 0.8290564, 0.8290564), "StaticMeshActor_18702", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1564.7255, 2699.7664, 3809.5042), (1.9307510779009005, 149.7493063288131, -3.5243839220169657), (1.0985973, 1.0985973, 1.0985973), "StaticMeshActor_18703", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1561.6189, 2652.2446, 3808.5947), (3.710554351430147, 62.06228281446099, 2.0555842743582096), (1.0078609, 1.0078609, 1.0078609), "StaticMeshActor_18704", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4542.8193, 156.53197, 4996.555), (10.990826567425648, -13.469299696571564, 17.921458767865154), (1.0532668, 1.0532668, 1.0532668), "StaticMeshActor_18705", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2334.7703, 3561.6428, 3898.1978), (-10.50131132735678, 98.04790410529974, 4.058184103992853), (1.072202, 1.072202, 1.072202), "StaticMeshActor_18706", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2231.2488, 3582.5283, 3885.5955), (-10.613311446068543, 95.95263285951894, 6.735138096610767), (1.043202, 1.043202, 1.043202), "StaticMeshActor_18707", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3555.4744, 725.02106, 4638.0454), (-8.56423910550057, 15.133830069347086, 33.912477480133965), (0.9368864, 0.9368864, 0.9368864), "StaticMeshActor_18708", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3555.8914, 652.67236, 4608.57), (10.885037378240503, -171.22356781767226, -26.56615796152317), (0.8542503, 0.8542503, 0.8542503), "StaticMeshActor_18709", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1233.6129, 3340.9976, 3556.8435), (27.386492644015252, -13.986022725334154, -20.598539519701685), (1.0276679, 1.0276679, 1.0276679), "StaticMeshActor_18710", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2203.7524, 3349.2993, 3461.2114), (-21.688291512787316, 6.060173876412221, -27.66552533554954), (0.905165, 0.905165, 0.905165), "StaticMeshActor_18711", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2154.2524, 4159.935, 5808.797), (-10.382965853272664, -83.92629040022207, 23.635082862975764), (0.95733964, 0.95733964, 0.95733964), "StaticMeshActor_18712", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2046.5634, 4153.9966, 5805.1997), (-1.4899596196866771, 99.76337254619523, -16.991884434175443), (0.8652366, 0.8652366, 0.8652366), "StaticMeshActor_18713", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2142.2097, 4050.4917, 5796.3105), (-16.195218578983145, -6.8547352772823915, -6.020598780802853), (1.055636, 1.055636, 1.055636), "StaticMeshActor_18714", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3634.9885, 4842.595, 5837.0605), (2.5689363248473542, 1.1777663234983005, 1.8841670735795573), (0.9212515, 0.9212515, 0.9212515), "StaticMeshActor_18715", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2046.3853, 3250.7336, 5812.588), (-20.786620957509008, -9.67095887185523, 1.2579259356551797), (0.8500089, 0.8500089, 0.8500089), "StaticMeshActor_18716", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4556.826, 4956.956, 6009.5063), (16.505040835326167, -92.66588834911373, -5.287200703439056), (1.0252106, 1.0252106, 1.0252106), "StaticMeshActor_18717", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4450.626, 4966.1855, 6020.0854), (6.515835966797807, 2.340375682002189, 12.116145971539279), (1.0093911, 1.0093911, 1.0093911), "StaticMeshActor_18718", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4567.8384, 4871.6, 5999.802), (1.116721981506377, 173.7444957995798, -15.14904552462166), (1.015976, 1.015976, 1.015976), "StaticMeshActor_18719", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5240.0957, 4838.407, 5800.131), (12.403725789648254, -175.32307500794732, -29.299743025147087), (0.8896275, 0.8896275, 0.8896275), "StaticMeshActor_18720", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4548.0127, 3347.7617, 5980.5894), (-7.676391775998155, 81.9554109880309, -9.28155548062053), (0.8999941, 0.8999941, 0.8999941), "StaticMeshActor_18721", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2848.2932, 2459.8862, 5952.5757), (28.555959270189657, -90.44909394248526, -1.037508391446243), (0.9979257, 0.9979257, 0.9979257), "StaticMeshActor_18722", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1660.8406, 4698.6094, 1166.0967), (2.909571931002512, 0.5299960421078987, -8.688171549706848), (1.0, 1.0, 1.0), "StaticMeshActor18654", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2754.9043, 4156.01, 3956.1047), (-2.8863829463905692, -1.0640563917795411, 88.96201817590612), (1.2, 1.2, 1.2), "StaticMeshActor18663", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4982.743, 1144.7152, 3933.7302), (-8.852996809107644, 71.15544278822674, -0.9644168215915306), (1.011257, 1.011257, 1.011257), "StaticMeshActor18664", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1407.657, 2327.2852, 4081.9043), (-19.08459467530123, 108.79467332183593, -15.864714892361096), (1.125, 1.46875, 0.941183), "StaticMeshActor18675", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (197.72891, 3458.8325, 4456.163), (4.108030591471492, -131.49979494698914, 161.55606047466716), (1.1875, 1.1875, 1.1875), "StaticMeshActor18676", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (237.72891, 3023.8325, 4446.163), (-4.869079003348691, 120.25022269133652, 156.33328746703057), (1.4375, 1.3125, 1.4375), "StaticMeshActor18677", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2859.9302, 3264.1316, 1941.5992), (-15.231625552264767, -106.299179338756, 60.038367678738624), (1.035019, 1.035019, 1.035019), "StaticMeshActor18678", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2918.8252, 3231.5247, 1764.7152), (18.00764261169754, -103.14445493819841, 154.9108557970432), (1.035019, 1.035019, 1.035019), "StaticMeshActor18679", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2844.398, 2990.6536, 1764.7152), (18.00764261169754, -103.14445493819841, 154.9108557970432), (1.035019, 1.035019, 1.035019), "StaticMeshActor18680", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5146.185, 785.4852, 4136.5566), (-4.18078566512262, 170.5697828430003, -6.0596608677592805), (1.3847313, 1.3847313, 1.3847313), "StaticMeshActor18682", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3105.6416, 4257.3555, 1018.2439), (-7.048950113326826, 0.5165710166260306, 100.59573048820477), (1.4237988, 1.2737432, 1.0), "StaticMeshActor18737", _folder)
if a: placed += 1
else: skipped += 1

# Batch 39: StaticMesh'PWM_Quarry_2x2x2_A' (428 instances)
_mesh_path = "/Game/Unshippable/Whitebox/Rocks/Meshes/PWM_Quarry_2x2x2_A"
_materials = ['/Game/Environments/ProcTexturing/ProcMaterial_Quarry_Atlas_1']
_folder = "Reconstruction/BD_BB_Passage_SpiralCave/Meshes"
a = spawn_static_mesh(_mesh_path, _materials, (814.7869, 905.89136, 2024.8188), (1.7320533299397693, 176.0467746571581, -179.1748168955118), (1.0, 1.0, 1.0), "PWM_Quarry_2x2x2_A_8", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (603.1772, 3277.247, 2892.5857), (-13.498646599139208, 0.0, -0.0), (1.387666, 1.387666, 1.387666), "PWM_Quarry_2x2x2_A_61", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4649.3, 438.51987, 2454.4949), (-41.63854752118662, 13.80906538280776, -2.658080176938969), (1.387666, 1.387666, 1.387666), "PWM_Quarry_2x2x2_A_125", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4647.311, 3744.2163, 6089.622), (6.958128485586174, -0.08660130641341952, -7.439562861232166), (1.387666, 1.387666, 1.387666), "PWM_Quarry_2x2x2_A_263", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3391.3826, 2344.5432, 2804.8022), (-19.32611088049878, 0.0, -0.0), (1.387666, 1.387666, 1.387666), "PWM_Quarry_2x2x2_A_694", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (825.97217, 1031.9636, 923.1206), (2.687003012062983, 23.593808906705767, -4.177856253721919), (1.474444, 1.474444, 1.474444), "PWM_Quarry_2x2x2_A10", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (516.8702, 952.07983, 926.0317), (2.6870027025039867, -178.90627871011566, -4.177856256863414), (1.474444, 1.474444, 1.474444), "PWM_Quarry_2x2x2_A11", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (755.97217, 421.96362, 933.1206), (-2.686798151556146, 77.65662339173628, 175.82197719956895), (1.474444, 1.474444, 1.474444), "PWM_Quarry_2x2x2_A12", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (885.97217, 791.9636, 933.1206), (-2.6867980028635743, -60.15594145665558, 175.8219768651807), (1.474444, 1.474444, 1.474444), "PWM_Quarry_2x2x2_A13", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4870.929, 1679.9373, 3147.5894), (-1.720031279576721, 168.92895481543349, -179.0297393386148), (0.820277, 0.820277, 0.820277), "PWM_Quarry_2x2x2_A131_54", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3903.3784, 2366.4482, 3131.1152), (-11.595124328790245, -129.01361888795344, 81.05957633254444), (0.75, 0.75, 2.637758), "PWM_Quarry_2x2x2_A132", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4284.108, 2230.059, 3246.4226), (-7.204407915255711, -127.41842636243196, 83.71933720100593), (0.75, 0.75, 2.5), "PWM_Quarry_2x2x2_A133_249", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4024.7014, 2217.1602, 3044.5317), (-16.617092891716222, 48.59750174238386, 100.39677701428164), (0.75, 0.75, 2.637758), "PWM_Quarry_2x2x2_A134", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2737.459, 1292.5579, 3131.1152), (-11.594970921590333, -8.076326347947791, 81.05881270151953), (0.75, 0.75, 2.637758), "PWM_Quarry_2x2x2_A135", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4473.884, 1966.3484, 3111.5896), (-25.81765461776758, 53.52454689499887, 97.95723580118005), (0.75, 0.75, 2.637758), "PWM_Quarry_2x2x2_A136", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2658.0435, 1689.9703, 3240.5476), (-7.204285161621585, -6.481079222378158, 83.71927280170611), (0.7969528, 0.85992795, 2.637758), "PWM_Quarry_2x2x2_A137", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2803.1335, 1473.3704, 3044.5317), (-16.616729581368883, 169.53500379584082, 100.39677848396884), (0.75, 0.75, 2.637758), "PWM_Quarry_2x2x2_A138", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2717.3364, 1987.5894, 3101.5896), (-25.81741334840917, 174.4621127215013, 97.95730265111062), (0.75, 0.75, 2.637758), "PWM_Quarry_2x2x2_A139", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (573.0562, 949.88153, 1775.2471), (-6.707061063458766, 74.99365266020772, 15.12725999720786), (1.474444, 1.474444, 1.474444), "PWM_Quarry_2x2x2_A14", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4825.4473, 1832.3542, 3245.9058), (-15.013918024769938, -104.73642158385711, 85.13509804733987), (0.75, 0.75, 2.637758), "PWM_Quarry_2x2x2_A140_94", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4537.7153, 2052.8608, 3262.2773), (1.4788855539417658, 155.454585347524, -8.492126692982257), (0.8, 0.8, 0.8), "PWM_Quarry_2x2x2_A141", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4748.2744, 1780.5913, 3121.9993), (3.84038331598504, -13.681334623268555, -175.35108165713334), (0.820277, 0.820277, 0.820277), "PWM_Quarry_2x2x2_A142", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2828.877, 2475.3901, 3147.5894), (-1.7200621173294919, -70.13298938565039, -179.02975300842874), (0.820277, 0.820277, 0.820277), "PWM_Quarry_2x2x2_A143", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2752.674, 1977.0999, 3242.8271), (-2.68420390079956, 172.63281498728807, -179.75459792950352), (0.820277, 0.820277, 0.820277), "PWM_Quarry_2x2x2_A144", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2752.0503, 2208.537, 3234.104), (3.840403664312178, 53.81860802960281, -158.47558520759068), (0.820277, 0.820277, 0.820277), "PWM_Quarry_2x2x2_A145", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2759.8914, 2224.368, 3245.0635), (-12.272094657016444, -4.590058312545898, 85.73597222513251), (0.75, 0.75, 2.637758), "PWM_Quarry_2x2x2_A146", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2929.9963, 2447.3027, 2943.8018), (11.874197366902221, -5.404510698570746, -96.08259787994457), (0.75, 0.75, 2.637758), "PWM_Quarry_2x2x2_A147", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2677.2202, 1976.4268, 2926.5757), (7.566651534021246, -7.219696329336787, -93.46813949276849), (0.75, 0.75, 2.637758), "PWM_Quarry_2x2x2_A148", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2949.7688, 2260.4302, 3039.671), (16.41982354524753, 175.57056508262517, -82.52969564167473), (0.75, 0.75, 2.637758), "PWM_Quarry_2x2x2_A149", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (795.97217, 641.9636, 1483.1206), (-14.543762892643741, -37.646304090520616, -11.168486914933286), (1.474444, 1.474444, 1.474444), "PWM_Quarry_2x2x2_A15", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2809.4995, 1762.7654, 2996.9814), (25.36798528281018, 170.14519017169818, -85.1212323796336), (0.75, 0.75, 2.637758), "PWM_Quarry_2x2x2_A150", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2731.2695, 1278.3057, 2984.7388), (-0.6140135496086916, 56.085537204737115, 2.5399260983780896), (0.820277, 0.820277, 0.820277), "PWM_Quarry_2x2x2_A151", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2778.4248, 1774.4102, 2855.0017), (2.35321181057366, 173.18192715084317, -2.550506567384348), (0.820277, 0.820277, 0.820277), "PWM_Quarry_2x2x2_A152", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2686.8267, 1487.2747, 3022.5503), (-1.4365844817282445, -121.25124662943017, 3.1871335428439234), (0.820277, 0.820277, 0.820277), "PWM_Quarry_2x2x2_A153", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (633.65497, 3292.9895, 2241.275), (0.9631442117910664, -1.4503097493020705e-09, -3.473510530260393), (1.0, 1.0, 1.0), "PWM_Quarry_2x2x2_A153_50", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4367.3223, 415.31073, 1866.845), (-27.189692272368163, 13.06303418282318, -5.706577790163775), (1.0, 1.0, 1.0), "PWM_Quarry_2x2x2_A153_114", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4902.7603, 3840.521, 5497.293), (21.29154608467979, -2.0754085663185884, -11.402308763742356), (1.0, 1.0, 1.0), "PWM_Quarry_2x2x2_A153_252", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3355.5732, 2360.2856, 2153.763), (-4.864319211496896, 1.2143052283550155e-08, -3.4735108723703623), (1.0, 1.0, 1.0), "PWM_Quarry_2x2x2_A153_682", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2678.0818, 1469.9948, 2881.892), (8.471085945600741, -18.945432875186746, -106.06891018361695), (0.75, 0.75, 2.637758), "PWM_Quarry_2x2x2_A154", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4780.7593, 1770.76, 2978.7322), (6.421853813558445, -121.30288788862245, -99.29330156685107), (0.75, 0.75, 2.637758), "PWM_Quarry_2x2x2_A155", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4529.553, 2091.227, 2873.6162), (2.023432142475496, -122.8602221235128, -96.48669513622517), (0.75, 0.75, 2.637758), "PWM_Quarry_2x2x2_A156", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4594.8906, 1828.3165, 3060.2368), (21.769886096106102, 61.340777436567876, -78.99121430499098), (0.75, 0.75, 2.637758), "PWM_Quarry_2x2x2_A157", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (432.13495, 3589.5828, 868.72766), (-5.1713717616761, -5.212685711158051, 0.8676221705594671), (1.0, 1.0, 1.0), "PWM_Quarry_2x2x2_A157_3", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3489.9626, 570.73865, 762.96716), (-33.40107970353001, 7.132788244920874, 1.4407162728251532), (1.0, 1.0, 1.0), "PWM_Quarry_2x2x2_A157_67", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5188.3086, 4313.086, 4190.5376), (14.43941609963449, -6.510507762734725, -8.616611560112945), (1.0, 1.0, 1.0), "PWM_Quarry_2x2x2_A157_205", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3015.7356, 2656.879, 808.7697), (-10.974425787218257, -5.288390730120237, 1.4060065368943115), (1.0, 1.0, 1.0), "PWM_Quarry_2x2x2_A157_635", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4210.4844, 2171.185, 2998.2776), (31.00094360930745, 56.27890605153096, -81.89942098038652), (0.75, 0.75, 2.637758), "PWM_Quarry_2x2x2_A158", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (415.32626, 3655.488, 538.65765), (-9.40287784076045, -34.123886497393514, 3.6087491359557062), (1.397144, 1.397144, 1.397144), "PWM_Quarry_2x2x2_A158_4", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3307.2866, 609.14703, 482.3847), (-33.26078397242887, -27.714074524893505, 20.00155057778592), (1.397144, 1.397144, 1.397144), "PWM_Quarry_2x2x2_A158_68", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5286.7173, 4420.352, 3886.594), (3.4953727538766564, -33.723824833306665, -13.96480988985419), (1.397144, 1.397144, 1.397144), "PWM_Quarry_2x2x2_A158_206", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2965.5007, 2722.784, 482.11206), (-14.208649424115174, -34.81381069850564, 6.977160115461924), (1.397144, 1.397144, 1.397144), "PWM_Quarry_2x2x2_A158_636", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3808.7002, 2450.8613, 2961.907), (-0.396575949821337, -59.24536339100368, -3.763031234288341), (0.820277, 0.820277, 0.820277), "PWM_Quarry_2x2x2_A159", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5259.5, 3972.9893, 4735.7837), (-27.24223812592306, -168.16809748731526, 1.6214996910640984), (1.428856, 1.428856, 1.428856), "PWM_Quarry_2x2x2_A159_232", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3334.5605, 2388.7063, 1303.1998), (0.0, -166.8644465997139, 0.0), (1.428856, 1.428856, 1.428856), "PWM_Quarry_2x2x2_A159_662", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (695.97217, 171.96362, 933.1206), (-2.686798603137282, -77.03095835329574, 175.82197735145132), (1.474444, 1.474444, 1.474444), "PWM_Quarry_2x2x2_A16", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4247.83, 2201.6765, 2860.6719), (7.8610983983745575, 58.0679605885714, 0.5346569148878836), (0.820277, 0.820277, 0.820277), "PWM_Quarry_2x2x2_A160", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3943.5044, 2367.4717, 2988.452), (-1.9322201348514991, 123.17465552404786, 9.477659614779045), (0.820277, 0.820277, 0.820277), "PWM_Quarry_2x2x2_A161", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4005.2717, 2403.6865, 2874.9697), (7.926509527978333, -137.66118065256154, -94.4241324377017), (0.75, 0.75, 2.637758), "PWM_Quarry_2x2x2_A162", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (888.0729, 3663.4978, 633.8672), (5.605836796489694, -15.90444855020189, -1.594376240414776), (1.0, 1.0, 1.0), "PWM_Quarry_2x2x2_A162_44", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3756.1458, 718.021, 343.49518), (-22.022672147247423, -4.238096486210274, 4.347150512527702), (1.0, 1.0, 1.0), "PWM_Quarry_2x2x2_A162_108", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5696.4277, 4401.4, 4140.358), (22.85035329201995, -19.853492182882242, -15.332481930068043), (1.0, 1.0, 1.0), "PWM_Quarry_2x2x2_A162_246", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3445.4712, 2730.7937, 528.83014), (0.0, -15.826352198080055, 0.0), (1.0, 1.0, 1.0), "PWM_Quarry_2x2x2_A162_676", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5789.6675, 4401.4, 4029.9434), (2.186003311305751, -155.78856682417413, -25.263724945986656), (1.0, 1.0, 1.0), "PWM_Quarry_2x2x2_A163", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (631.01636, 3577.4822, 1060.5061), (-1.962182043380647, 113.3724839120569, 0.4198377517764123), (1.0, 1.0, 1.0), "PWM_Quarry_2x2x2_A164_12", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3753.04, 611.83093, 837.67285), (10.876489905499808, 123.90375522099977, -24.858800363542784), (1.0, 1.0, 1.0), "PWM_Quarry_2x2x2_A164_76", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5307.985, 4270.7495, 4436.2295), (-2.96269490483092, 111.90825417072774, 22.167204261017535), (1.0, 1.0, 1.0), "PWM_Quarry_2x2x2_A164_214", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3233.061, 2644.7783, 979.364), (0.35480085000760714, 113.4475265149703, -4.928100361390964), (1.0, 1.0, 1.0), "PWM_Quarry_2x2x2_A164_644", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5324.9326, 4183.5776, 4743.1406), (18.957443544596156, -22.073762086637526, 161.33571575977365), (1.0, 1.0, 1.0), "PWM_Quarry_2x2x2_A165_247", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3387.1736, 2597.5435, 1255.2235), (-3.182769448214837, -18.881529057010322, 177.5458413248669), (1.0, 1.0, 1.0), "PWM_Quarry_2x2x2_A165_677", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (398.8969, 3550.819, 2142.3032), (5.827462797271557, 0.0, -0.0), (1.0, 1.0, 1.0), "PWM_Quarry_2x2x2_A166_47", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4065.6416, 613.59094, 1899.3473), (-22.32891942188259, 12.858378149979728, -2.1472779882329056), (1.0, 1.0, 1.0), "PWM_Quarry_2x2x2_A166_111", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4713.6157, 4116.0225, 5356.914), (26.107660896843033, -2.8217772568609325, -8.229033677159004), (1.0, 1.0, 1.0), "PWM_Quarry_2x2x2_A166_249", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3111.9795, 2618.115, 2079.1382), (0.0, 0.0, -0.0), (1.0, 1.0, 1.0), "PWM_Quarry_2x2x2_A166_679", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3781.0322, 2658.0288, 3365.8948), (0.044492646674529526, 15.166957912564365, -1.8591306447089395), (0.820277, 0.820277, 0.820277), "PWM_Quarry_2x2x2_A167_166", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2387.354, 2695.5657, 2955.9592), (-8.918396683038537, 100.51773088190525, -164.59605729989045), (0.820277, 0.820277, 0.820277), "PWM_Quarry_2x2x2_A168", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3751.8337, 2693.1917, 3317.203), (-1.8586426282898636, -77.64251563766831, 0.046691794446175265), (0.820277, 0.820277, 0.820277), "PWM_Quarry_2x2x2_A169", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (790.3478, 305.21127, 1373.1206), (3.4485145847540313, 9.675930216998212, -1.4669799003958461), (1.0, 1.0, 1.0), "PWM_Quarry_2x2x2_A17", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3913.925, 2552.949, 3301.169), (0.04449311207079098, -59.38952264507767, -1.8591306685270592), (0.4234261, 0.4234261, 0.4234261), "PWM_Quarry_2x2x2_A170", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3617.1921, 1468.0773, 2872.0544), (-73.18472719730288, -35.93122624981412, 103.79187800697525), (1.5, 1.5, 1.5), "PWM_Quarry_2x2x2_A18", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3717.1921, 1258.0773, 2752.0544), (0.910400562297732, -168.312625808089, 98.74757626898504), (1.0, 1.0, 1.0), "PWM_Quarry_2x2x2_A19", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (824.1116, 1032.8859, 1971.43), (3.76979292363945, -145.16573681008904, 165.66491331963806), (1.144373, 1.144373, 1.144373), "PWM_Quarry_2x2x2_A2_20", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (518.22235, 2780.0667, 4048.5466), (-3.176178161975244, -26.059114938408793, -2.512726226079548), (1.0, 1.0, 1.125), "PWM_Quarry_2x2x2_A20_10", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (555.98315, 3052.8623, 2810.8186), (8.526797684799293, 27.789256011070222, -31.925770900210523), (1.355404, 1.355404, 1.355404), "PWM_Quarry_2x2x2_A206_57", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4617.285, 204.15921, 2396.9465), (-15.436785142894962, 41.263733231046665, -46.996482243519104), (1.355404, 1.355404, 1.355404), "PWM_Quarry_2x2x2_A206_121", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4634.7793, 3533.46, 5968.4326), (30.06910546977459, 28.348045251776632, -28.72427818757547), (1.355404, 1.355404, 1.355404), "PWM_Quarry_2x2x2_A206_259", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3336.1304, 2120.1584, 2728.2495), (3.363786636902314, 27.507379569603433, -34.64367743573913), (1.355404, 1.355404, 1.355404), "PWM_Quarry_2x2x2_A206_689", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3398.067, 2996.5425, 1934.0485), (-8.446042028843907, 95.67891970650692, -23.012421849141152), (1.0, 1.0, 1.44703), "PWM_Quarry_2x2x2_A21_34", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (805.8488, 564.3167, 1382.4071), (3.448514241777447, 9.675930218842511, -1.4669799290392211), (1.0, 1.0, 1.0), "PWM_Quarry_2x2x2_A22", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (706.64636, 112.86421, 1471.8995), (3.448514241777447, 9.675930218842511, -1.4669799290392211), (1.0, 1.0, 1.0), "PWM_Quarry_2x2x2_A23", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (729.20715, 311.24255, 1435.1879), (3.448514241777447, 9.675930218842511, -1.4669799290392211), (1.0, 1.0, 1.0), "PWM_Quarry_2x2x2_A24", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (679.15533, 105.01912, 1555.8931), (3.448514241777447, 9.675930218842511, -1.4669799290392211), (1.0, 1.0, 1.0), "PWM_Quarry_2x2x2_A25", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5044.709, 4017.195, 1943.0527), (0.0, -66.49691227283084, 0.0), (1.1603953, 0.6134653, 1.768437), "PWM_Quarry_2x2x2_A26_173", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4648.6978, 3691.8206, 1759.4313), (0.0, 0.0, -0.0), (0.9936746, 0.549414, 1.0), "PWM_Quarry_2x2x2_A27_176", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2081.713, 4465.1685, 1099.4146), (-2.438903812230122, -14.739836894090644, -9.188291907531156), (1.0, 1.0, 1.0), "PWM_Quarry_2x2x2_A28_192", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1770.7307, 5856.0913, 1898.485), (3.204076019498376, -67.26440293406986, -11.126037431752414), (1.056919, 0.5810134, 1.7760148), "PWM_Quarry_2x2x2_A29_237", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4540.0, 1530.4921, 2827.5298), (0.0, 0.0, 39.37449711711939), (1.5, 1.5, 1.5), "PWM_Quarry_2x2x2_A3_145", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1689.3048, 6075.4316, 1898.485), (3.204076019498376, -67.26440293406986, -11.126037431752414), (1.056919, 0.581013, 1.776015), "PWM_Quarry_2x2x2_A30", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1221.0448, 6245.161, 1521.6132), (1.2326148743904902e-07, 18.04252159148057, 14.410066585431256), (1.0, 1.0, 1.0), "PWM_Quarry_2x2x2_A31_269", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3320.01, 5414.19, 2558.9404), (0.0, 0.0, 77.49717707175907), (1.0, 1.0, 1.0), "PWM_Quarry_2x2x2_A32_280", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3021.501, 5443.971, 2565.5452), (0.0, 0.0, 77.49717707175907), (1.0, 1.0, 1.0), "PWM_Quarry_2x2x2_A33", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2799.422, 5381.36, 2627.5166), (4.322451035879934, 19.929987497420445, 78.25423793802263), (1.0, 1.0, 1.0), "PWM_Quarry_2x2x2_A34", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2778.3242, 5387.272, 2863.257), (4.322451035879934, 19.929987497420445, 78.25423793802263), (1.0, 1.0, 1.0), "PWM_Quarry_2x2x2_A35", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2424.459, 5433.5825, 3700.3394), (0.9989972670345433, 9.900771556407753, -95.70467014241603), (1.2692041, 1.2692041, 1.2692041), "PWM_Quarry_2x2x2_A36_295", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2424.4595, 5459.2817, 3446.8435), (0.9989967587696549, 9.900771088709483, -95.7046701463907), (1.269204, 1.269204, 1.269204), "PWM_Quarry_2x2x2_A37", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2424.4597, 5421.474, 3819.6277), (0.9989967587696549, 9.900771088709483, -95.7046701463907), (1.269204, 1.269204, 1.269204), "PWM_Quarry_2x2x2_A38", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2728.887, 5474.607, 3825.0166), (0.9989967587696549, 9.900771088709483, -95.7046701463907), (1.269204, 1.269204, 1.269204), "PWM_Quarry_2x2x2_A39", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3493.7505, 1820.4922, 2824.2278), (-64.68432642610283, -179.99994535844863, -179.9999863396134), (1.5, 1.5, 1.5), "PWM_Quarry_2x2x2_A4", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (829.49805, 4130.018, 3232.1658), (-87.05391733157104, -179.99998217542716, -168.84517658661636), (1.4075527, 1.2786974, 0.57278186), "PWM_Quarry_2x2x2_A40_304", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (767.3415, 4445.6006, 3235.364), (-87.05358101714168, -179.9999313523078, -168.84513640707425), (1.407553, 1.278697, 0.572782), "PWM_Quarry_2x2x2_A41", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (994.97125, 3861.8462, 3626.4514), (-4.492996274176144e-07, -20.98944161378485, -89.45166917125553), (1.0, 1.0, 1.0), "PWM_Quarry_2x2x2_A42_318", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1063.2446, 2760.2969, 3579.6348), (0.0, 0.0, -0.0), (1.0, 1.0, 1.0), "PWM_Quarry_2x2x2_A43_327", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (821.5588, 2293.9314, 2887.995), (73.23683551901931, 19.543647852977223, 8.559238328048822e-05), (1.0, 1.0, 1.0), "PWM_Quarry_2x2x2_A44_333", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (872.15546, 2293.9314, 3125.4497), (73.23683551901931, 19.543647852977223, 8.559238328048822e-05), (1.0, 1.0, 1.0), "PWM_Quarry_2x2x2_A45", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1311.2109, 1363.0801, 2979.9985), (71.26852592824201, 55.78343752319333, 5.1485626638768e-05), (1.6994708, 1.8760612, 1.0), "PWM_Quarry_2x2x2_A46_342", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (707.00226, 1567.9612, 2503.0115), (17.959215254004132, 4.703343500118134, -18.837400851991294), (1.4232334, 1.4507915, 1.0), "PWM_Quarry_2x2x2_A47_348", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3525.4272, 4160.304, 3938.0), (0.0, 43.577716577423246, -0.0), (1.2596728, 0.60698324, 0.60698324), "PWM_Quarry_2x2x2_A48_4", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (740.7656, 939.9227, 1480.3785), (-1.845367347760947, 29.45333207074144, -1.041900708030849), (1.157649, 1.157649, 1.567572), "PWM_Quarry_2x2x2_A5_5", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4697.991, 1670.3917, 3173.1206), (2.6869963596029036, -97.34338244049388, -4.177856429245085), (1.474444, 1.474444, 1.474444), "PWM_Quarry_2x2x2_A6_264", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2925.9722, 2411.9636, 3163.1206), (2.6870034607395965, 23.59380889537973, -4.177856160898622), (1.474444, 1.474444, 1.474444), "PWM_Quarry_2x2x2_A7", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2860.305, 1392.45, 2953.5698), (-0.9671020823285501, -37.7268690987642, 178.04878692494094), (1.474444, 1.474444, 1.474444), "PWM_Quarry_2x2x2_A8", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3859.6982, 2287.107, 2926.7793), (-7.269560235785001, -153.12931726662333, 178.2564514954955), (1.474444, 1.474444, 1.474444), "PWM_Quarry_2x2x2_A9", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2813.4304, 5267.6606, 1233.695), (-1.8925172134881623, 98.63637699810107, 0.5399762180978717), (0.9041171, 0.9041171, 0.9041171), "StaticMeshActor_18168", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2783.045, 5011.7593, 1168.4067), (-5.166717523684466, -176.76311194400154, 6.3028552069994985), (0.88906896, 0.88906896, 0.88906896), "StaticMeshActor_18169", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2623.6196, 987.78375, 4024.373), (-13.65795838918592, 148.00555046620707, -175.5272414766546), (1.0, 1.0, 1.0), "StaticMeshActor_18170", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3644.053, 617.9519, 4031.0647), (4.652416316429834, -125.25578680321036, 5.131024738563845), (0.96008843, 0.96008843, 0.96008843), "StaticMeshActor_18171", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3618.7156, 5712.775, 880.82947), (-7.801268464727725, -159.30122597579808, 1.100888437534528), (1.2654977, 1.2654977, 1.2654977), "StaticMeshActor_18172", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3382.2397, 5182.2085, 891.5728), (-8.076386557710231, 170.5878895521903, -6.193023294922101), (0.82094175, 0.82094175, 0.82094175), "StaticMeshActor_18174", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3097.003, 5043.001, 1062.4542), (6.70865863930918, -12.123595026149003, -0.2093201003754794), (0.9751379, 0.9751379, 0.9751379), "StaticMeshActor_18175", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2894.125, 5104.4463, 1055.9397), (-3.546142974901197, 98.64394174134563, -2.7183228601741996), (0.87370473, 0.87370473, 0.87370473), "StaticMeshActor_18176", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2299.0105, 5111.382, 1261.8792), (0.5853948851618374, -176.69703635238474, 4.091298855031001), (0.9146389, 0.9146389, 0.9146389), "StaticMeshActor_18177", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3499.468, 5571.6514, 3877.4883), (0.16933399945455907, 85.78834376414133, -1.987640129918306), (0.9075073, 0.9075073, 0.9075073), "StaticMeshActor_18178", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3311.83, 5576.7295, 3875.7163), (-1.9097595118371178, -98.3245964351286, 7.300725741879959), (1.0254962, 1.0254962, 1.0254962), "StaticMeshActor_18179", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5596.5, 2237.7297, 3887.738), (-9.136443400619006, 170.43942559075847, 3.2815425563924014), (0.8520578, 0.8520578, 0.8520578), "StaticMeshActor_18180", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2418.987, 4428.8228, 1175.1472), (5.0786629249717095, 1.1326748655651033, -14.673554949885675), (1.0095183, 1.0095183, 1.0095183), "StaticMeshActor_18181", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2638.5208, 5005.8877, 1344.5422), (-3.393402051567093, 90.58261643967516, 0.7643195018075131), (1.0221349, 1.0221349, 1.0221349), "StaticMeshActor_18182", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2463.3557, 5044.763, 1315.4235), (6.491123879712279, -0.1160278182637307, -5.7038870991556525), (0.9380834, 0.9380834, 0.9380834), "StaticMeshActor_18183", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2859.3354, 5005.9, 1374.6709), (-2.809692848591692, -85.43875781170041, -7.56954974087674), (1.0377169, 1.0377169, 1.0377169), "StaticMeshActor_18184", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3349.2769, 5012.2334, 1577.0686), (-8.85717804479009, 81.48197451782036, 1.9824711105062094), (0.8264942, 0.8264942, 0.8264942), "StaticMeshActor_18185", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3099.5652, 5037.3315, 1466.2374), (4.109143204027754, 178.24158723702487, -3.0449516343006366), (0.9582621, 0.9582621, 0.9582621), "StaticMeshActor_18186", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3898.4182, 4179.7065, 1586.0323), (13.296238543214637, -39.4904143717352, 7.328007766566393), (1.0320617, 1.0320617, 1.0320617), "StaticMeshActor_18187", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3687.2832, 4221.217, 1587.9567), (2.6905817207350626, 177.05145144630117, -2.0397343396267), (0.9272789, 0.9272789, 0.9272789), "StaticMeshActor_18188", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5322.4863, 3498.0488, 2072.8372), (6.3370566905183985, 62.67448439819638, 10.842293613674176), (0.8543037, 0.8543037, 0.8543037), "StaticMeshActor_18190", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4303.42, 907.8704, 3252.3071), (-8.583771647136007, -97.29455629840204, 4.451001649125973), (0.8707901, 0.8707901, 0.8707901), "StaticMeshActor_18192", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4096.4795, 913.8109, 3263.9773), (9.576585371137794, 177.4791621931397, 6.804496632269959), (1.0085759, 1.0085759, 1.0085759), "StaticMeshActor_18193", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3304.641, 1024.7025, 3230.2275), (4.233119119718669, 85.61345772320588, -1.7216189311876668), (0.8382552, 0.8382552, 0.8382552), "StaticMeshActor_18194", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3500.8623, 902.91425, 3251.9302), (-0.9075622023657309, 98.8958193534536, 1.6208849954071933), (0.903407, 0.903407, 0.903407), "StaticMeshActor_18195", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3288.6582, 894.93365, 3260.5527), (-4.555236804209615, -0.5724181352529012, -7.46160894640342), (0.8993781, 0.8993781, 0.8993781), "StaticMeshActor_18196", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1700.6912, 3657.3538, 3885.2747), (4.685974722459327, 60.71030417324649, 3.5680507807558333), (1.0355388, 1.0355388, 1.0355388), "StaticMeshActor_18200", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2289.6694, 3091.7, 4065.1558), (-5.641814944441428, -83.13104530089352, 3.9112640696055285), (0.8792789, 0.8792789, 0.8792789), "StaticMeshActor_18201", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2061.3296, 2967.6694, 3885.733), (-11.308135283690476, 10.766216631060713, -1.8836973645157928), (0.95273435, 0.95273435, 0.95273435), "StaticMeshActor_18202", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1741.2847, 2713.3079, 3898.016), (-0.6285704382209893, 23.42424835660372, 12.304080690892196), (1.0, 1.0, 1.0), "StaticMeshActor_18203", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1484.4757, 3767.1475, 3914.0952), (-0.9476623335188668, -14.264800765846699, 1.5713596261627654), (1.0427295, 1.0427295, 1.0427295), "StaticMeshActor_18204", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1202.9857, 3899.123, 3927.3481), (8.640694505608069, 118.39960484368686, 1.6275764015378622), (1.0887188, 1.0887188, 1.0887188), "StaticMeshActor_18205", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1502.1843, 2517.8071, 3934.3757), (13.603290392804285, -114.38702879149443, -1.5982361828932987), (1.0026639, 1.0026639, 1.0026639), "StaticMeshActor_18206", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3094.353, 5052.7446, 1257.0856), (1.2958096875435399, -95.34185798341998, -6.375213854504507), (0.84042776, 0.84042776, 0.84042776), "StaticMeshActor_18207", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3302.0586, 5024.933, 1453.0587), (6.21194113133614, -92.27375629779179, 2.711875858619216), (0.9923909, 0.9923909, 0.9923909), "StaticMeshActor_18208", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3768.7944, 762.30176, 4504.98), (6.993008260858151, -153.93842393576787, -1.0492859416568183), (0.9967223, 0.9967223, 0.9967223), "StaticMeshActor_18209", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4012.0984, 5624.081, 1002.3059), (-6.69491532262315, 83.87211336348993, 1.2586193124484906), (0.87710404, 0.87710404, 0.87710404), "StaticMeshActor_18210", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3618.1643, 5178.425, 1607.3695), (6.72768104478204, 104.10337376285747, -1.1017453628895986), (0.97831744, 0.97831744, 0.97831744), "StaticMeshActor_18211", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3619.0178, 5256.217, 958.75354), (0.0, 0.0, -0.0), (1.0, 1.0, 1.0), "StaticMeshActor_18212", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3918.111, 5569.155, 1186.7798), (-6.957182883049162, -96.49233338999423, 6.375130727284529), (0.84407496, 0.84407496, 0.84407496), "StaticMeshActor_18213", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3519.3591, 5331.493, 926.4437), (-6.929565302833576, -0.23696897716259363, 5.237027087480181), (1.0, 1.0, 1.0), "StaticMeshActor_18214", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3894.6216, 5904.0176, 1256.5137), (-1.316497715537795, -173.27391298282714, 7.310198716559728), (0.857414, 0.857414, 0.857414), "StaticMeshActor_18215", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3827.3254, 6182.098, 1282.9928), (4.137571283776883, -102.22925367338591, -11.250794394760925), (1.25, 1.0, 1.5625), "StaticMeshActor_18216", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (6260.737, 3278.3528, 2982.927), (-42.95751950400671, 179.24110567141926, 1.1078077572064298), (1.0211546, 1.0211546, 1.0211546), "StaticMeshActor_18217", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (6355.029, 3290.2964, 2894.98), (-4.2227181761769215, 96.1256283711646, 12.321175270626627), (0.8262823, 0.8262823, 0.8262823), "StaticMeshActor_18219", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (6118.6987, 4127.7437, 2890.1704), (4.836039516451644, 36.2712149557164, 7.429653852499657), (1.0048316, 1.0048316, 1.0048316), "StaticMeshActor_18220", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3938.2817, 5154.81, 2855.188), (-2.8640439008436878, 48.6516028789458, -0.13943475912948838), (0.88693094, 0.88693094, 0.88693094), "StaticMeshActor_18221", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3524.2114, 5258.061, 2947.5203), (-29.919431814870148, -116.87815083169848, -15.157011099658952), (0.90839404, 0.90839404, 0.90839404), "StaticMeshActor_18222", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3878.3408, 5087.054, 2866.7896), (-9.429504545289973, 126.9812403450513, -0.142791648753496), (0.8023924, 0.8023924, 0.8023924), "StaticMeshActor_18223", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3960.0464, 5182.295, 2665.061), (-0.809112436595129, -117.59083893100812, -1.43637066742008), (0.9675235, 0.9675235, 0.9675235), "StaticMeshActor_18224", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3836.5923, 5258.2397, 2689.1604), (10.159720926527466, 149.52739583584588, 15.194692792929372), (1.0953283, 1.0953283, 1.0953283), "StaticMeshActor_18225", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4017.8826, 5041.133, 2903.5066), (-2.97882217889672, 142.8639338392155, 23.82121714413025), (0.8285099, 0.8285099, 0.8285099), "StaticMeshActor_18226", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4724.1587, 1803.0748, 2941.5522), (-0.2334289997201617, 177.11447945452284, -37.88967789877516), (0.98687726, 0.98687726, 0.98687726), "StaticMeshActor_18228", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1996.603, 3028.3176, 3702.0886), (-3.6797487857421176, -94.29517020118507, -3.067932210309073), (0.822236, 0.822236, 0.822236), "StaticMeshActor_18230", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1886.4906, 2915.476, 3912.035), (-6.787048131337078, 9.275169501591739, 0.9941406938946699), (0.8207286, 0.8207286, 0.8207286), "StaticMeshActor_18231", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2199.8562, 3103.7988, 3540.094), (-7.150360513306172, -16.310457976634538, -36.3507376003302), (0.999521, 0.999521, 0.999521), "StaticMeshActor_18232", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1893.0001, 2944.883, 3693.526), (37.40533679595201, 115.62365453572656, 10.225360452191453), (0.8179838, 0.8179838, 0.8179838), "StaticMeshActor_18233", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2295.5261, 3094.843, 3855.7256), (-5.132872610916996, 161.50819674216763, -6.690307135037351), (1.0259631, 1.0259631, 1.0259631), "StaticMeshActor_18234", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2206.9263, 3031.2227, 3939.4072), (-6.941955404697354, 44.86275853341927, 0.18087275220420934), (1.0932311, 1.0932311, 1.0932311), "StaticMeshActor_18235", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1973.6248, 3041.0522, 3500.0842), (-6.903839371724599, -155.65680036892894, 13.384774967451529), (0.8812296, 0.8812296, 0.8812296), "StaticMeshActor_18236", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5533.537, 679.2882, 5386.846), (23.324126500262263, -78.95935408896254, -3.0182174869607), (1.084389, 1.084389, 1.084389), "StaticMeshActor_18237", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5319.748, 251.17702, 5318.504), (-27.578671144029276, -97.45532004014163, 20.170119834057374), (0.9917162, 0.9917162, 0.9917162), "StaticMeshActor_18238", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5305.348, 108.060875, 5260.3003), (-36.74814055233353, -94.28990495067204, 7.368094546114904), (0.94604576, 0.94604576, 0.94604576), "StaticMeshActor_18239", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5497.316, 305.70984, 5258.2144), (22.458894926265025, -175.89686508414664, 39.23755240347519), (0.99995536, 0.99995536, 0.99995536), "StaticMeshActor_18240", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5391.949, 153.33778, 5160.0815), (-19.410336103303994, 123.6225329692137, -15.401212692973772), (1.0235476, 1.0235476, 1.0235476), "StaticMeshActor_18241", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4717.69, 5134.7275, 6004.685), (4.076542920069805, 178.58881975362803, -19.511350169651482), (0.8014099, 0.8014099, 0.8014099), "StaticMeshActor_18242", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (443.59122, 3667.8655, 4107.526), (4.998612409651631, -2.485504262835258, -1.2091064998152028), (1.0227956, 1.0227956, 1.0227956), "StaticMeshActor_18243", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (38.80858, 3641.9316, 4383.497), (-7.265076830780886, -149.75368154934264, 18.217575173656662), (0.9094153, 0.9094153, 0.9094153), "StaticMeshActor_18244", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3597.8062, 594.23486, 4494.6294), (-2.746185393199914, 40.09619946905515, 20.656203064141913), (0.82846034, 0.82846034, 0.82846034), "StaticMeshActor_18245", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3662.8892, 581.4929, 4235.8794), (7.946849609892098, 64.3122086299261, -8.511993357999017), (1.0990478, 1.0990478, 1.0990478), "StaticMeshActor_18246", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3575.0962, 298.0574, 4103.039), (-5.967009622036318, -19.559203147059165, -6.971160019426581), (0.94866353, 1.0625, 0.94866353), "StaticMeshActor_18247", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3629.4912, 245.39236, 4393.8257), (-28.938843372743246, 139.7753409034256, 4.366329928214505), (1.0450941, 1.0450941, 1.0450941), "StaticMeshActor_18248", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (6277.35, 3523.3938, 2597.3813), (0.6952652720749222, -84.78552969559115, -3.1497497771052037), (0.8712046, 0.8712046, 0.8712046), "StaticMeshActor_18250", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (6286.903, 3299.1162, 2664.3948), (-0.07916258652216845, -172.46874805053798, -4.629150174834383), (1.0137628, 1.0137628, 1.0137628), "StaticMeshActor_18251", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2728.402, 807.23376, 4068.316), (-5.31372051759581, -47.415189430950065, 4.738069113824287), (0.87030274, 0.87030274, 0.87030274), "StaticMeshActor_18252", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2773.5425, 266.3199, 4400.705), (-8.485169247316943, -81.71792305765474, 25.403773723274444), (1.0584974, 1.0584974, 1.0584974), "StaticMeshActor_18253", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2777.848, 73.478355, 4419.2124), (17.753091860187336, -174.93496166120968, -8.318451483348664), (0.93212736, 0.93212736, 0.93212736), "StaticMeshActor_18254", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5551.876, 692.7291, 4327.372), (6.357198118855964, 3.1809114446931535, 3.8786461824611864), (0.92073274, 0.92073274, 0.92073274), "StaticMeshActor_18255", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5537.0767, 759.46857, 4174.077), (6.862468402873972, -171.65724082076255, 1.442680994636017), (0.8987838, 0.8987838, 0.8987838), "StaticMeshActor_18256", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (6317.4106, 718.78296, 5262.2363), (-7.9403375748396785, -164.23172220184395, -5.0173950009968635), (0.8471683, 0.8471683, 0.8471683), "StaticMeshActor_18257", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (6129.5566, 699.6096, 5330.165), (-1.7427671985933821, 7.445584456849633, 18.79853056796861), (1.0849159, 1.0849159, 1.0849159), "StaticMeshActor_18258", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5265.907, 761.9499, 5403.1807), (-11.298367866151763, 179.26587222189437, 46.22461834306261), (0.88299197, 0.88299197, 0.88299197), "StaticMeshActor_18259", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4694.3887, 851.3795, 5329.485), (7.8044814284589785, -13.152893298026557, -34.31436379017035), (1.0164922, 1.0164922, 1.0164922), "StaticMeshActor_18260", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4473.801, 846.67706, 5335.707), (14.456081647724647, -2.727783528554705, -40.059910269685595), (0.9622868, 0.9622868, 0.9622868), "StaticMeshActor_18261", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3902.0547, 839.8664, 4458.48), (-7.624785619933686, 87.0078321809449, 8.528181756346127), (0.8216471, 0.8216471, 0.8216471), "StaticMeshActor_18262", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3897.7085, 827.7514, 4250.0596), (-3.3926693474759864, -75.33544825837147, -8.60504073403154), (1.0452489, 1.0452489, 1.0452489), "StaticMeshActor_18263", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3065.829, 912.8296, 5323.4443), (10.244647758644216, -7.740264661161444, 18.56597990560526), (1.0746696, 1.0746696, 1.0746696), "StaticMeshActor_18264", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3089.3467, 853.1754, 5284.4307), (-21.53387815506176, 83.69466467321057, -1.8098445348245105), (0.93024766, 0.93024766, 0.93024766), "StaticMeshActor_18265", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3084.285, 773.6866, 5116.871), (19.349710422238985, -102.34384277370889, -5.518005279203566), (1.0547701, 1.0547701, 1.0547701), "StaticMeshActor_18266", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2867.889, 1008.14795, 5286.1655), (-4.883025383752866, -23.373319590200875, 13.01642973064511), (1.0255959, 1.0255959, 1.0255959), "StaticMeshActor_18267", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3047.4146, 902.9832, 5116.8467), (-12.625577620536195, 78.318594464209, -7.085143746126268), (0.9148955, 0.9148955, 0.9148955), "StaticMeshActor_18268", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2850.6345, 946.6195, 5104.635), (11.958787943601513, -95.41040972077633, 6.183535287960394), (0.81770843, 0.81770843, 0.81770843), "StaticMeshActor_18269", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2497.926, 2598.1895, 2949.0322), (-5.343841386213887, 5.038452248504839, 4.2350550524717505), (0.9224403, 0.9224403, 0.9224403), "StaticMeshActor_18271", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2810.691, 2118.525, 1038.8276), (-2.4447628121298264, -84.09976425200894, -4.758239934198522), (1.0241448, 1.0241448, 1.0241448), "StaticMeshActor_18274", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2897.6348, 3310.9172, 2064.4897), (-8.782959405208123, 26.65413508358627, 16.278671934170493), (1.0029091, 1.0029091, 1.0029091), "StaticMeshActor_18275", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2490.2754, 3557.458, 5443.7104), (-2.2149338253997573, -84.50948665806706, -42.184443589441834), (0.9577168, 0.9577168, 0.9577168), "StaticMeshActor_18276", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2293.7727, 3508.9355, 5861.2334), (3.3731426889247125, 84.69421060885526, -39.51457914226452), (0.81685746, 0.81685746, 0.81685746), "StaticMeshActor_18277", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2178.1562, 3507.6655, 5912.8477), (34.004365049945896, 170.83333976705643, -11.786988684249726), (0.8892318, 0.8892318, 0.8892318), "StaticMeshActor_18278", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2288.4343, 3294.1184, 5854.1963), (-9.358705548865464, 94.76206289097335, -16.490263946329335), (0.9041326, 0.9041326, 0.9041326), "StaticMeshActor_18279", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2298.738, 4102.345, 5855.093), (-0.5581342677834885, 101.57912824918121, -22.003537451727748), (0.9716734, 0.9716734, 0.9716734), "StaticMeshActor_18280", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3269.113, 5476.2964, 3891.6055), (0.0, -59.06234105096117, 0.0), (0.9409269, 0.9409269, 0.9409269), "StaticMeshActor_18281", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3503.6992, 5487.2964, 3729.5837), (5.450510263912568, -93.16649244612982, 5.036940449204957), (0.96481156, 0.96481156, 0.96481156), "StaticMeshActor_18282", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3311.2947, 5475.0083, 3740.9734), (6.419421075797658, 8.034268658274422, 2.9275737515050118), (0.84571666, 0.84571666, 0.84571666), "StaticMeshActor_18283", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2091.5522, 5329.464, 3784.5151), (6.806740636653303, -77.67742988934324, -175.65570367412536), (0.87394315, 1.6380628, 1.2804004), "StaticMeshActor_18284", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1853.9614, 5250.825, 3758.773), (-4.127166826804273, 1.234240604242602, 0.619722471161183), (0.93911356, 0.93911356, 0.93911356), "StaticMeshActor_18285", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1717.0118, 5176.5493, 3819.8801), (3.3003474467166667, -8.858643001397372, -4.791473239408024), (1.0, 1.0, 1.0), "StaticMeshActor_18286", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1443.1907, 5148.946, 3717.2986), (-5.174164039591177, 174.5019247230934, -2.4866942371839245), (0.9723027, 0.9723027, 0.9723027), "StaticMeshActor_18287", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1194.6069, 5125.072, 3745.5613), (-5.539734262126321, -93.65879005119939, 8.2507519628108), (1.0931227, 1.0931227, 1.0931227), "StaticMeshActor_18288", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5334.032, 2640.616, 1276.0863), (-3.9697874051740154, 29.55163182039665, 10.291640721447086), (0.8025662, 0.8025662, 0.8025662), "StaticMeshActor_18289", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5372.5913, 2573.4377, 1076.3567), (-6.361480121694931, 123.28957744888191, 0.029784912538730838), (0.8346334, 0.8346334, 0.8346334), "StaticMeshActor_18290", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5519.3955, 2597.2722, 1299.646), (41.8602078063217, -69.82607787977868, 7.857837159380454), (0.89719546, 0.89719546, 0.89719546), "StaticMeshActor_18291", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5519.77, 2528.1702, 1070.0842), (-3.613768966870925, -174.99402261938795, -18.082670457395107), (0.87953067, 0.87953067, 0.87953067), "StaticMeshActor_18292", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5490.638, 2511.008, 1054.2045), (6.485743340427624, -89.35943980526635, 6.57417352797764), (1.0540019, 1.0540019, 1.0540019), "StaticMeshActor_18293", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5541.5435, 236.94681, 5080.5493), (-22.506803620846338, 136.86952234758093, -3.258117802530351), (0.93586355, 0.93586355, 0.93586355), "StaticMeshActor_18294", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5491.9746, 112.55443, 5058.7646), (-24.45794770093764, 131.81380417884176, 16.557462507202032), (0.80525404, 0.80525404, 0.80525404), "StaticMeshActor_18295", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1284.1515, 3494.1445, 5923.133), (-1.2900394242889872, 83.15690966479676, 10.325863973839594), (0.8001102, 0.8001102, 0.8001102), "StaticMeshActor_18296", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1303.2638, 2691.4214, 5855.2974), (15.429791476230987, -6.464538228368849, -19.04434181905284), (0.9334414, 0.9334414, 0.9334414), "StaticMeshActor_18297", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4714.328, 1649.678, 2932.3174), (-8.2408142604267, -6.416991447028796, -31.755002671520774), (1.0652908, 1.0652908, 1.0652908), "StaticMeshActor_18298", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4056.1462, 2081.4749, 2920.2788), (-17.32644581438525, -82.03667631417251, -22.99123832576544), (1.0140147, 1.0140147, 1.0140147), "StaticMeshActor_18305", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3811.8865, 2653.762, 2922.2822), (-19.71109034903786, 27.529389365037424, -13.555727327891915), (1.0999343, 1.0999343, 1.0999343), "StaticMeshActor_18306", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3627.144, 2721.323, 2880.4402), (-1.1656790260509349, 89.81659502663693, -25.500912927273493), (0.97081876, 0.97081876, 0.97081876), "StaticMeshActor_18307", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3864.6208, 2494.497, 2908.551), (10.980846041616314, -159.04445787894645, -0.9903866163797572), (0.9689536, 0.9689536, 0.9689536), "StaticMeshActor_18308", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3659.1772, 2509.9285, 2947.5654), (16.889432862723208, -6.588989811167528, 5.5419906569823025), (0.8049143, 0.8049143, 0.8049143), "StaticMeshActor_18309", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3107.5247, 2494.43, 2847.6497), (33.4921624982347, -102.5181303375451, -33.72464057104153), (0.96837544, 0.96837544, 0.96837544), "StaticMeshActor_18322", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2902.7495, 2502.3547, 2863.8489), (-3.415892746479664, -35.63171096217113, -31.14028368865949), (1.0696974, 1.0696974, 1.0696974), "StaticMeshActor_18329", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5490.7407, 5899.063, 4451.179), (-3.7749938139301906, -7.359465952422742, -3.734496693290854), (0.89477766, 0.89477766, 0.89477766), "StaticMeshActor_18330", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5425.473, 5838.8555, 4417.7446), (7.549168950032786, -83.95641953404302, 5.950665327285152), (1.0708497, 1.0708497, 1.0708497), "StaticMeshActor_18331", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5501.1997, 5892.6577, 4266.1816), (0.9000071245028977, 3.970180932231915, -3.2953798256998126), (0.96189034, 0.96189034, 0.96189034), "StaticMeshActor_18332", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5381.062, 5865.708, 4228.5664), (-2.0729979683917317, 5.389035063020449, -3.415923808541553), (0.9689975, 0.9689975, 0.9689975), "StaticMeshActor_18333", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5351.657, 5676.757, 4426.437), (-6.515319948143617, 85.23164547665132, 3.673616900014262), (1.019115, 1.019115, 1.019115), "StaticMeshActor_18334", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3060.6877, 3296.0356, 2109.0408), (10.216090682283353, 177.1543670783422, -6.273041646984852), (0.84254676, 0.84254676, 0.84254676), "StaticMeshActor_18335", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2889.2236, 3331.1128, 2108.6602), (2.9042854755423697, 167.11843766309383, -24.621338828575944), (0.92706645, 0.92706645, 0.92706645), "StaticMeshActor_18336", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3088.5625, 3304.3909, 2053.0986), (2.563595742391092, 159.3922789788163, -22.873322134192698), (0.8145716, 0.8145716, 0.8145716), "StaticMeshActor_18337", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3080.002, 3214.3027, 1872.786), (-9.201720853030576, 172.7792769312139, -21.679532321237943), (1.0538385, 1.0538385, 1.0538385), "StaticMeshActor_18338", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3100.5845, 3504.5833, 2862.2725), (-5.3334959042078625, -5.803283391793886, 20.285635098027633), (0.9058502, 0.9058502, 0.9058502), "StaticMeshActor_18339", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3079.1755, 3462.2288, 2664.5674), (-24.691740898045335, 91.4957733236412, -9.353911652196038), (1.0785205, 1.0785205, 1.0785205), "StaticMeshActor_18340", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2890.5674, 3512.8364, 2659.563), (-3.7793277702908252, -179.1410275715346, -20.164521458323122), (1.0190502, 1.0190502, 1.0190502), "StaticMeshActor_18341", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2896.5808, 3504.49, 2866.0435), (9.321084454661428, -82.6575024216427, 0.7922075343064788), (0.9414793, 0.9414793, 0.9414793), "StaticMeshActor_18342", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1648.8329, 4697.105, 899.8928), (-6.42455972743168, -157.39150725829765, 1.4169411515112875), (0.88891673, 0.88891673, 0.88891673), "StaticMeshActor_18343", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1768.35, 4562.956, 1026.2269), (-2.520385698360686, 92.48004081672191, 4.302006557322044), (1.0108411, 1.0108411, 1.0108411), "StaticMeshActor_18344", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3107.0647, 2499.648, 2666.4375), (-12.583251381210209, -59.46399114429731, -7.482178023491381), (0.8111618, 0.8111618, 0.8111618), "StaticMeshActor_18345", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3602.4963, 2742.973, 2686.5562), (10.859679277685359, -103.50103898521732, 18.76731002048862), (0.9214334, 0.9214334, 0.9214334), "StaticMeshActor_18346", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3502.433, 3556.2432, 5378.9604), (3.4053952926038664, 74.42841503661563, -25.387082504921935), (0.808139, 0.808139, 0.808139), "StaticMeshActor_18347", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3553.7944, 3220.7156, 2876.9163), (3.671895500345574, -54.70486381398913, 11.8356501687071), (0.9286898, 0.9286898, 0.9286898), "StaticMeshActor_18348", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5567.5117, 3577.8186, 1437.695), (11.138342850886302, 174.095680637656, -10.688689326921407), (0.90375334, 0.90375334, 0.90375334), "StaticMeshActor_18351", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5569.4395, 3308.378, 1477.8032), (2.697709481047462, 97.39617335320669, -22.330533674023247), (1.0562737, 1.0562737, 1.0562737), "StaticMeshActor_18352", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5930.175, 3100.6775, 1438.8903), (-4.5587762131274205, 3.343932909425957, -0.3042602065151641), (0.8654511, 0.8654511, 0.8654511), "StaticMeshActor_18353", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5719.7153, 3020.613, 1437.1387), (15.300401411101268, 94.49481993831093, -3.7545475555641854), (1.0498043, 1.0498043, 1.0498043), "StaticMeshActor_18354", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5717.3315, 2843.8103, 1377.6744), (-14.086607785520522, -2.9070732554760927, -14.692868075453825), (0.8885861, 0.8885861, 0.8885861), "StaticMeshActor_18355", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (6110.449, 3552.5078, 1354.9767), (-14.937102643603808, 4.845378495630645, 8.683088023863657), (0.93575287, 0.93575287, 0.93575287), "StaticMeshActor_18356", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (6313.238, 3545.9097, 1334.981), (-10.51574665632313, -10.800749194399257, 13.213673738919852), (0.86661875, 0.86661875, 0.86661875), "StaticMeshActor_18357", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (6499.967, 3397.4426, 1410.6455), (-33.99316426807667, 90.33208043743286, -5.911282975172623), (0.8545694, 0.8545694, 0.8545694), "StaticMeshActor_18358", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4792.603, 4518.26, 1216.3916), (9.052328494993302, -29.040770879715616, 8.531397132951216), (0.9934378, 0.9934378, 0.9934378), "StaticMeshActor_18359", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4784.9985, 4504.0366, 1019.0564), (-0.6471252372441895, 58.32269889528788, 2.658112968978368), (1.06622, 1.06622, 1.06622), "StaticMeshActor_18360", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5325.4443, 1897.3265, 1238.3442), (0.8525640168795042, 85.22624837804578, -15.26059148802518), (1.093127, 1.093127, 1.093127), "StaticMeshActor_18361", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5372.4854, 1735.577, 1286.0408), (5.793406438487408, -151.18796054878422, -26.701959723043263), (0.84212875, 0.84212875, 0.84212875), "StaticMeshActor_18362", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5348.6445, 1853.5349, 1059.4119), (4.881133842068124, 2.519542614748174, 1.2748066752699088), (0.9554752, 0.9554752, 0.9554752), "StaticMeshActor_18363", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5447.9233, 1699.8966, 1143.565), (-15.32687324860058, -174.7949916701222, 6.915853581515978), (1.0461646, 1.0461646, 2.1726723), "StaticMeshActor_18364", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5643.6104, 1126.9729, 1196.6083), (8.176337290892251, -82.90899866159472, 4.596191742596345), (1.0436747, 1.0436747, 1.0436747), "StaticMeshActor_18365", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5579.0186, 1122.6713, 1030.1422), (-9.869475271160415, 98.8989647719288, -9.521238266761026), (0.97353274, 0.97353274, 0.97353274), "StaticMeshActor_18366", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5623.121, 930.5923, 1225.6791), (-6.130310860394139, -83.40809442614518, 5.286077687847429), (0.95942724, 0.95942724, 0.95942724), "StaticMeshActor_18367", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5588.967, 911.69763, 1044.2645), (-7.33346578098227, 111.16559940514914, -5.3623350543092405), (0.93593615, 0.93593615, 0.93593615), "StaticMeshActor_18368", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5667.728, 316.18802, 2160.2178), (37.20550532875654, 8.117876789877794, 3.8093606061734473), (1.0505378, 1.0505378, 1.0505378), "StaticMeshActor_18369", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5493.3403, 1708.3136, 3663.409), (-4.380432172260935, -97.32511007247366, -2.3630674854951197), (1.0604999, 1.0604999, 1.0604999), "StaticMeshActor_18372", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5554.368, 2279.3333, 3823.5322), (-3.9024966779987524, -89.99115192736124, 9.164164633485019), (0.8160321, 0.8160321, 0.8160321), "StaticMeshActor_18376", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5499.847, 2251.7932, 3734.779), (1.816947446245654, -81.12239147679713, -9.500030338761661), (0.88460207, 0.88460207, 0.88460207), "StaticMeshActor_18377", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5472.4614, 2105.8728, 3900.1594), (-2.812316465309485, -81.5616917782166, 8.437966220410026), (0.82816714, 0.82816714, 0.82816714), "StaticMeshActor_18378", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5566.791, 3508.0742, 3837.6267), (9.361810968048413, 80.68960815283303, -7.2220143579516956), (0.8410639, 0.8410639, 0.8410639), "StaticMeshActor_18380", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5356.7466, 3184.1123, 3841.7332), (30.937382980305635, -6.027574042914442e-14, 1.3589858298032395e-05), (0.8325767, 0.8325767, 0.8325767), "StaticMeshActor_18381", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5502.627, 3297.6765, 3850.3716), (-9.54717984474996, -5.735381291877048, -7.9916070283717895), (0.93517303, 0.93517303, 0.93517303), "StaticMeshActor_18382", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5346.6685, 3295.509, 3753.053), (0.1447449854994014, 105.12590647616783, 8.095253009397014), (0.9380137, 0.9380137, 0.9380137), "StaticMeshActor_18383", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5361.773, 4328.17, 3623.6694), (-9.704681213300203, -3.636077928032055, 8.734773488402771), (1.0198519, 1.0198519, 1.0198519), "StaticMeshActor_18384", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5446.1016, 4183.8765, 3607.9333), (3.305709216398273, -97.12091455383322, 5.848776547350977), (1.0309284, 1.0309284, 1.0309284), "StaticMeshActor_18385", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5291.9834, 4307.666, 3467.1533), (6.042217064201587, 2.434996164619152, -0.5683898123687332), (0.8611954, 0.8611954, 0.8611954), "StaticMeshActor_18386", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1914.8519, 4484.0195, 1135.8872), (0.39531086614393807, 88.0794049691392, 5.146077047216062), (0.9559681, 0.9559681, 0.9559681), "StaticMeshActor_18387", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2323.8037, 4420.5225, 943.078), (-2.5549616103259427, 99.69114107355878, 1.5322241163239085), (1.0875438, 1.0875438, 1.0875438), "StaticMeshActor_18388", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2317.3022, 4421.7905, 998.68677), (8.944303514974994, 95.63791162152344, -7.731505919091263), (0.85030603, 0.85030603, 0.85030603), "StaticMeshActor_18389", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3506.6472, 4187.7285, 1371.8281), (1.6399487311882448, -93.7594588759891, -2.053405633924979), (0.5974883, 1.3017898, 1.3017898), "StaticMeshActor_18390", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3338.8787, 4306.337, 1359.9856), (-9.47479280615341, 97.79636791534185, 0.1953561205873626), (0.8222128, 0.8222128, 0.8222128), "StaticMeshActor_18391", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3692.476, 4281.663, 1379.0469), (6.044218800084645, -93.11872455965835, -9.021852103812988), (1.042217, 1.042217, 1.042217), "StaticMeshActor_18392", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3688.663, 4201.697, 1219.946), (0.3839932551028198, -1.9533997419931297, -6.184509335405987), (0.876466, 0.876466, 0.876466), "StaticMeshActor_18393", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3847.1394, 4247.066, 1400.5371), (9.783460603798071, -178.9563260128476, 6.447366869930029), (1.0794344, 1.0794344, 1.0794344), "StaticMeshActor_18394", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3862.2202, 4203.384, 1227.6993), (4.57457430927367, 81.42276508362808, -5.780884361269814), (1.0819846, 1.0819846, 1.0819846), "StaticMeshActor_18395", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3844.224, 4202.9106, 1021.5943), (-3.1143185569034304, 5.612411904364566, -6.759581660581479), (0.9441688, 0.9441688, 0.9441688), "StaticMeshActor_18396", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (690.49854, 3096.1294, 4853.433), (22.40348808107315, -6.8373406771562015, -17.522276713260702), (0.92818433, 0.92818433, 0.92818433), "StaticMeshActor_18397", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (608.3404, 3040.7205, 4766.8564), (12.830293689029716, 102.04134508937179, 46.418143557788305), (0.98151857, 0.98151857, 0.98151857), "StaticMeshActor_18398", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (546.08, 809.63293, 1192.9019), (-1.8498225843755811, -83.7366104747076, 4.349773408514489), (0.8836891, 0.8836891, 0.8836891), "StaticMeshActor_18403", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (-57.225395, 745.0512, 2100.2249), (-20.374816918620656, 103.91963606422287, -1.9857800408595638), (1.0140271, 1.0140271, 1.835742), "StaticMeshActor_18404", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (-27.565723, 666.9738, 1758.8912), (8.308221724927686, -67.92794801941477, 1.8221696381452182), (0.998506, 0.998506, 1.820221), "StaticMeshActor_18405", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (-13.610705, 630.21716, 1104.764), (1.3550552435629033, 87.97348827144371, 8.520998669995555), (0.9762199, 0.9762199, 0.9762199), "StaticMeshActor_18406", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (-52.965324, 720.79, 960.3063), (8.39947842763772, -0.46121211837953735, 2.2849500291650897), (0.99466234, 0.99466234, 0.99466234), "StaticMeshActor_18407", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1109.4951, 1548.431, 2975.9165), (7.107247464154617, 124.85183601413082, -28.78353115236713), (0.91994256, 0.91994256, 0.91994256), "StaticMeshActor_18408", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (608.7279, 2460.0793, 2713.7473), (-9.225586529261731, -77.64294511847332, 16.59747282909147), (0.96825373, 0.96825373, 0.96825373), "StaticMeshActor_18409", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (703.92163, 2694.101, 2861.4792), (-22.088776567243126, 23.020317325219494, -13.63296577683993), (1.0492591, 1.0492591, 1.0492591), "StaticMeshActor_18410", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (631.30145, 2686.8142, 2692.5942), (20.51999948838014, -176.32813157459393, -8.32757604886049), (0.88731503, 0.88731503, 0.88731503), "StaticMeshActor_18411", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (694.7677, 3299.0112, 2849.757), (40.434915213351445, -166.87949889536299, 8.712634751790057), (0.9146608, 0.9146608, 0.9146608), "StaticMeshActor_18412", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (696.94904, 3503.4639, 2661.9534), (-9.748685548118196, 88.90384699850576, -38.543972754729474), (1.032047, 1.032047, 1.032047), "StaticMeshActor_18413", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (706.7338, 3290.7942, 2651.4958), (-31.431087632281272, -3.834686138859199, 10.189694067010072), (1.0373156, 1.0373156, 1.0373156), "StaticMeshActor_18414", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1413.7775, 2521.6223, 3880.6328), (8.895515627790047, -93.30572710888774, 7.0362220767789445), (0.9051082, 0.9051082, 0.9051082), "StaticMeshActor_18415", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1536.5763, 2730.0715, 3595.8926), (-4.873107959365168, -43.50873127132292, 11.838614313936406), (1.0265383, 1.0265383, 1.0265383), "StaticMeshActor_18416", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1427.0339, 2742.9236, 3611.1), (-3.687530033576302, 87.15203912055205, -17.75827021146758), (0.9043506, 0.9043506, 0.9043506), "StaticMeshActor_18417", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (623.59766, 5700.4727, 4440.0903), (-2.712066857262276, -89.94765948854065, 4.822336535395892), (1.0537128, 1.0537128, 1.0537128), "StaticMeshActor_18418", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (696.6253, 5896.1104, 4249.806), (8.195037026070647, -94.60597899978482, 4.0265324026790665), (0.91267455, 0.91267455, 0.91267455), "StaticMeshActor_18419", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (699.04645, 5702.2, 4253.509), (-9.844451635311867, 6.759257094437102, 0.19880394999166703), (0.9908681, 0.9908681, 0.9908681), "StaticMeshActor_18420", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1388.7518, 1841.4418, 4517.774), (5.415895920176559, -166.32696515061795, 9.103165492187555), (0.9376068, 0.9376068, 0.9376068), "StaticMeshActor_18421", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1300.4866, 1906.0834, 4451.471), (4.219568029934357, -62.46945446039069, 1.0574577452380591), (1.0062783, 1.0062783, 1.0062783), "StaticMeshActor_18422", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1497.3429, 1693.2802, 4459.496), (6.9863683509280925, 28.299854487268554, -8.672606972195087), (0.8833253, 0.8833253, 0.8833253), "StaticMeshActor_18423", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1455.3408, 1866.2125, 4345.8467), (5.069154219357972, -148.51031662428397, 6.420471178308804), (0.89462054, 0.89462054, 0.89462054), "StaticMeshActor_18424", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1297.8816, 1903.9752, 4249.171), (-4.535461023549985, -68.02568583415042, -0.3876648401114407), (0.8585006, 0.8585006, 0.8585006), "StaticMeshActor_18425", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1551.303, 1745.264, 4298.8877), (1.0494379541791166, -121.31070299184205, -7.7880244563237), (0.8851424, 0.8851424, 0.8851424), "StaticMeshActor_18426", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3098.9395, 2772.69, 3586.6648), (-0.5645751064638176, -174.65116668869808, 3.9458059570235915), (0.9584968, 0.9584968, 0.9584968), "StaticMeshActor_18427", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3091.0928, 2694.7114, 3455.1108), (4.430005535238667, 4.7192220623329035, 4.136863406093612), (0.96716416, 0.96716416, 0.96716416), "StaticMeshActor_18428", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3168.5457, 2576.2297, 3469.1504), (3.026190103118666, -80.40475822364839, 6.135523215520833), (1.0427973, 1.0427973, 1.0427973), "StaticMeshActor_18429", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2911.43, 2743.8386, 3422.6956), (-3.4138182781227613, 97.50247446873051, -7.988800104991278), (0.8089419, 0.8089419, 0.8089419), "StaticMeshActor_18430", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2895.791, 3292.2063, 5264.2095), (-1.960754370795333, -9.887968922611227, -1.107177818313837), (0.9360939, 0.9360939, 0.9360939), "StaticMeshActor_18431", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4424.5415, 217.58151, 5117.3545), (-25.19439798344334, 55.57315515751118, 15.141913717612358), (0.8671105, 0.8671105, 0.8671105), "StaticMeshActor_18432", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4694.268, 80.6364, 5105.3306), (6.5405202826232225, -0.6086730678117682, 46.55126913859297), (0.82488954, 0.82488954, 0.82488954), "StaticMeshActor_18433", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4690.7334, 201.12312, 5151.7466), (8.447980934564765, -6.5181267273125, -39.890620743341714), (1.0277545, 1.0277545, 1.0277545), "StaticMeshActor_18434", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1943.5533, 3384.0847, 3704.6707), (10.099580053524688, -166.60006044445387, -18.179840357038454), (1.031079, 1.031079, 1.031079), "StaticMeshActor_18435", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1958.8502, 3376.7292, 3558.7124), (-30.180908541537736, 101.75515022712703, -0.42605611140091143), (0.8623466, 0.8623466, 0.8623466), "StaticMeshActor_18436", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2295.3333, 3506.5784, 3659.2478), (2.732759279399429, 18.285685478091697, 27.46711157207798), (1.072512, 1.072512, 1.072512), "StaticMeshActor_18437", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2122.0835, 3460.456, 3682.9558), (-19.91302461246784, 106.81626704080713, -1.7538142430996533), (0.91567886, 0.91567886, 0.91567886), "StaticMeshActor_18438", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2315.0574, 3449.9407, 3470.8281), (3.3488485619466632, 17.123349973448814, 24.483407179771365), (0.89667016, 0.89667016, 0.89667016), "StaticMeshActor_18439", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2121.8398, 3417.64, 3525.9988), (13.286719098322788, -161.06404676986793, -28.816286050647754), (0.90408945, 0.90408945, 0.90408945), "StaticMeshActor_18440", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1880.4368, 3613.714, 3829.7778), (-1.4879759541715423, -81.03774425266087, -5.489501915512067), (1.0118036, 1.0118036, 1.0118036), "StaticMeshActor_18441", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1631.1865, 3603.451, 3852.6274), (4.883981134331653, -26.578034030248606, 0.9429937626060454), (1.0465181, 1.0465181, 1.0465181), "StaticMeshActor_18442", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1352.6188, 3726.463, 3836.665), (-6.088287282739694, 52.78193285835173, -3.281830111844197), (0.9097422, 0.9097422, 0.9097422), "StaticMeshActor_18443", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2251.663, 3742.9114, 3933.7263), (5.036797413322887, -17.365019330064637, 1.5451355333530161), (0.90603834, 0.90603834, 0.90603834), "StaticMeshActor_18444", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1455.3784, 3653.8481, 3850.8801), (3.09830988529435, -28.470246054680292, 6.897294864162614), (0.8239018, 0.8239018, 0.8239018), "StaticMeshActor_18445", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1249.5841, 3668.0713, 3878.3088), (0.8332282433815414, 121.58193201675014, -0.22756952822406507), (0.93499315, 0.93499315, 0.93499315), "StaticMeshActor_18446", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3090.6482, 3402.4087, 4237.4453), (5.538887350863244, 9.86551550488746, -6.986176398497366), (0.9659295, 0.9659295, 0.9659295), "StaticMeshActor_18447", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3092.6055, 3387.0342, 4444.0586), (-9.0274043466595, -5.820220225199156, 5.662881007702073), (0.87361175, 0.87361175, 0.87361175), "StaticMeshActor_18448", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2909.594, 3349.8489, 4434.827), (-10.273681660635168, -94.82434837084082, 3.4917021530353685), (0.8842314, 0.8842314, 0.8842314), "StaticMeshActor_18449", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2911.6785, 3356.4402, 4188.368), (-8.178680828815427, 98.10556077876733, 9.063816449877754), (1.0661966, 1.0661966, 1.0661966), "StaticMeshActor_18450", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3308.1272, 653.1347, 4724.9053), (-35.24551504423095, -87.74251805236267, 1.0530016760347287), (0.87565035, 0.87565035, 0.87565035), "StaticMeshActor_18451", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1570.3245, 3419.1099, 3816.6123), (15.349770918928492, -1.7684625542831214, -32.28594391902256), (0.8422104, 0.8422104, 0.8422104), "StaticMeshActor_18452", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1427.193, 3448.4512, 3758.3452), (12.184483488215731, 95.74207728191232, 24.622227694559985), (0.98412347, 0.98412347, 0.98412347), "StaticMeshActor_18453", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1239.6925, 3461.063, 3710.76), (23.825442299146207, 93.6188402324171, 29.508877789795164), (0.8906169, 0.8906169, 0.8906169), "StaticMeshActor_18454", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1209.7175, 3429.8125, 3620.0325), (25.620408155393772, -4.995026481569522, -19.631196816809283), (0.8602266, 0.8602266, 0.8602266), "StaticMeshActor_18455", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1750.2299, 2808.2415, 3825.4216), (3.987715874854137, 45.19314849336897, -44.03387132401946), (1.0507159, 1.0507159, 1.0507159), "StaticMeshActor_18456", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1232.6237, 2920.6206, 3545.1943), (-5.6292431580698565, 93.11115159595263, 28.13020956737107), (0.8780712, 0.8780712, 0.8780712), "StaticMeshActor_18457", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1682.5586, 2897.755, 3572.8923), (20.597098144568985, 149.81485777324048, -4.597503812376678), (1.0794497, 1.0794497, 1.0794497), "StaticMeshActor_18458", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1450.2739, 3102.0935, 3582.6968), (2.3573842924319695, 82.58910604351021, 22.765864578687033), (1.0580857, 1.0580857, 1.0580857), "StaticMeshActor_18459", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1276.684, 3090.2427, 3538.4263), (-10.06204044800262, -172.8262177183195, 11.419687400131904), (1.0804465, 1.0804465, 1.0804465), "StaticMeshActor_18460", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1695.2881, 3399.8098, 3682.199), (1.4433691183372432, 3.467537964438668, -29.063691745339334), (1.0106748, 1.0106748, 1.0106748), "StaticMeshActor_18461", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1769.9849, 3241.5374, 3649.3484), (-7.970458187976387, -0.9671021732646299, -7.855652563776995), (0.992075, 0.992075, 0.992075), "StaticMeshActor_18462", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1430.2822, 3421.158, 3681.0212), (19.084730567267282, 103.13799891442916, 13.935218265567618), (1.0757977, 1.0757977, 1.0757977), "StaticMeshActor_18463", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1446.1942, 3247.5437, 3626.8313), (-10.388092251802052, -99.22783877634386, -6.797516757919087), (0.8393606, 0.8393606, 0.8393606), "StaticMeshActor_18464", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2062.1108, 3274.4973, 3642.5422), (-15.272643978497552, -89.47162540814121, 32.37517693086876), (0.8436508, 0.8436508, 0.8436508), "StaticMeshActor_18465", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2291.8342, 3297.3545, 3444.471), (-29.48549711736704, 9.028051430820947, -7.272368743511136), (0.9459034, 0.9459034, 0.9459034), "StaticMeshActor_18466", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1988.9685, 3099.0347, 3578.0056), (-17.864500471212654, 94.89342448881457, -18.87100315848114), (0.83008087, 0.83008087, 0.83008087), "StaticMeshActor_18467", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3098.4595, 5107.4565, 5848.914), (-4.5839527367220665, 174.4133536688773, 2.966392880789237), (0.85105443, 0.85105443, 0.85105443), "StaticMeshActor_18468", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3875.4216, 5111.564, 5962.1104), (-15.47280630916158, 178.0736317478468, -1.286712486009669), (1.0642899, 1.0642899, 1.0642899), "StaticMeshActor_18469", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3688.5737, 5094.1665, 5906.0474), (0.3197212824374881, 83.97162730959204, 18.74337954940676), (0.9942797, 0.9942797, 0.9942797), "StaticMeshActor_18470", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3871.4805, 4892.348, 5933.745), (-3.458526547047463, -90.07123193776408, -1.7560420565271793), (0.998394, 0.998394, 0.998394), "StaticMeshActor_18471", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1493.4489, 3498.058, 5960.3525), (-0.025481954367321195, -80.82263850544643, 6.953777306340831), (0.9116461, 0.9116461, 0.9116461), "StaticMeshActor_18472", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1497.7714, 3290.6829, 5928.6064), (12.51568459248621, 82.9684209028558, 8.289486596990109), (1.055424, 1.055424, 1.055424), "StaticMeshActor_18473", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1496.0337, 2692.0032, 5843.9375), (-7.483947099248176, -84.74938344422766, -21.917417855533905), (0.81840396, 0.81840396, 0.81840396), "StaticMeshActor_18474", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4488.8535, 5104.404, 6048.5044), (16.114074904632382, -93.85200776854887, -8.353028733978396), (0.9802305, 0.9802305, 0.9802305), "StaticMeshActor_18475", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4496.6377, 4904.0825, 6049.4834), (3.125768467391182, -90.15735490939586, 14.560503902783127), (0.8546118, 0.8546118, 0.8546118), "StaticMeshActor_18476", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4518.423, 5121.4517, 6039.748), (-7.65914954633427, 98.24729508730132, 3.372019891779658), (1.005692, 1.005692, 1.005692), "StaticMeshActor_18477", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3907.3892, 4307.2686, 5858.0815), (-4.682739519823041, -99.79266316425559, -8.394745919491996), (0.9703548, 0.9703548, 0.9703548), "StaticMeshActor_18478", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3703.161, 4309.5195, 5852.6616), (-10.218717724646067, -89.88280824827038, -14.00570487230155), (1.0833886, 1.0833886, 1.0833886), "StaticMeshActor_18479", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3894.1846, 4091.0103, 5913.016), (-11.427857029232959, -84.82426404690582, -19.46194474132253), (1.0217036, 1.0217036, 1.0217036), "StaticMeshActor_18480", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4697.193, 4896.305, 6056.4043), (-1.1788022785393542, 90.22913652859576, -4.082366586737536), (0.90887237, 0.90887237, 0.90887237), "StaticMeshActor_18481", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4732.0454, 4923.688, 6016.204), (14.957935278861653, -82.02776450098266, 18.93774426000987), (1.0545849, 1.0545849, 1.0545849), "StaticMeshActor_18482", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4690.553, 4293.1963, 6011.9595), (-6.143707424787039, -87.08766099082591, 9.24082048715682), (0.8573398, 0.8573398, 0.8573398), "StaticMeshActor_18483", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4511.7007, 4304.8784, 6022.2466), (-0.07919258244701755, -83.36001305124043, -8.03976420430311), (1.084422, 1.084422, 1.084422), "StaticMeshActor_18484", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4702.1895, 4102.4355, 6009.173), (5.661604575568507, 96.63423573367774, -7.695677801122888), (0.9431318, 0.9431318, 0.9431318), "StaticMeshActor_18485", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4492.638, 3303.184, 6054.931), (2.0856188445174344, -177.76090757333594, 0.8269015299742266), (1.0709434, 1.0709434, 1.0709434), "StaticMeshActor_18486", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4706.2217, 3519.2407, 5994.0547), (2.5092880892646674, 87.87794917857396, -8.06826708476037), (0.87041533, 0.87041533, 0.87041533), "StaticMeshActor_18487", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4494.3657, 3510.033, 5981.313), (12.583078675011993, -87.88233481958073, -1.4687807296611777), (0.9302356, 0.9302356, 0.9302356), "StaticMeshActor_18488", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4708.7603, 3317.846, 6020.272), (-10.374877396672792, 96.40715128300292, -8.292146327354358), (0.89867383, 0.89867383, 0.89867383), "StaticMeshActor_18489", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3895.8018, 2699.4204, 6134.385), (9.166713380475366, -89.31042530148837, -7.233519776764712), (0.8212837, 0.8212837, 0.8212837), "StaticMeshActor_18490", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3886.4346, 2509.7017, 6144.62), (0.4565227417346748, -85.42835029892244, -6.343108816277433), (1.0721791, 1.0721791, 1.0721791), "StaticMeshActor_18491", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3694.4026, 2704.9363, 6112.491), (13.841609043952795, -3.4622192313084468, 18.95355733330987), (0.98268557, 0.98268557, 0.98268557), "StaticMeshActor_18492", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3693.9426, 2505.1821, 6121.8706), (-13.745452283309396, -179.4725845192855, -4.718445046368895), (0.92414725, 0.92414725, 0.92414725), "StaticMeshActor_18493", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3076.7397, 2739.3237, 5970.9346), (7.753323305219744, -1.5979613016613288, 7.003426194994411), (1.0810136, 1.0810136, 1.0810136), "StaticMeshActor_18494", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3072.2524, 2545.6072, 6024.452), (15.065470854768611, -86.16251064633018, -2.8404232862827774), (0.8187234, 0.8187234, 0.8187234), "StaticMeshActor_18495", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2893.1743, 2721.557, 5927.406), (2.196028078560729, -172.7791924108648, -21.530632741301883), (1.0336155, 1.0336155, 1.0336155), "StaticMeshActor_18496", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2145.3374, 1451.2773, 4197.089), (-13.65795838918592, 148.00555046620707, -175.5272414766546), (1.0, 1.0, 1.0), "StaticMeshActor18197", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2717.8994, 3021.693, 4593.6733), (-6.154144373382811, -74.66323034606839, 3.0397085787141758), (0.879279, 0.879279, 0.879279), "StaticMeshActor18227", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2285.3105, 1330.1185, 4326.6963), (13.789154891193737, -11.590392711085855, 8.451036457146476), (1.045249, 1.045249, 1.045249), "StaticMeshActor18270", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2318.725, 1205.616, 4217.2563), (-28.944030926618197, 43.11630631768331, -158.37710798190486), (1.045249, 1.045249, 1.045249), "StaticMeshActor18272", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2490.379, 1255.5629, 4426.587), (7.159780320111768, -3.0004581780098167, -178.71020788089268), (1.045249, 1.045249, 1.045249), "StaticMeshActor18273", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2848.1465, 622.13043, 4069.5525), (-5.313568325381417, -137.6417234434447, 4.7381693585923985), (0.870303, 0.870303, 0.870303), "StaticMeshActor18299", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2902.952, 306.44547, 3983.0608), (-0.7295532257618026, 12.157685108028048, -17.406314532789384), (0.8125, 0.8125, 0.8125), "StaticMeshActor18300", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3761.9387, 3063.99, 3773.0435), (-5.6843262706405255, 12.597066353123926, -11.908723409163878), (1.099934, 1.099934, 1.099934), "StaticMeshActor18310", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5310.3784, 3625.865, 3658.7603), (2.0282705978741545e-13, 99.99997875766985, -179.99998633961494), (0.935173, 0.935173, 0.935173), "StaticMeshActor18399", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5021.575, 4777.6836, 3868.6206), (5.307438477802266, 99.71141708257473, 9.379255751928703), (1.625, 1.625, 1.625), "StaticMeshActor18400", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2656.1091, 946.6195, 5104.635), (11.958787943601513, -95.41040972077633, 6.183535287960394), (1.5088466, 1.5088466, 1.5088466), "StaticMeshActor18501", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2245.1987, 3072.836, 3700.4695), (15.204071168090657, -178.49659079002606, 22.08979300103442), (1.050716, 1.050716, 1.050716), "StaticMeshActor18511", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5271.026, 692.7291, 4338.7583), (0.5016705711463816, 163.02952871676223, -2.9675601528167603), (1.5296112, 1.1076674, 0.920733), "StaticMeshActor18512", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2705.7239, 4281.187, 3355.853), (-6.208922702168695, -17.668273996394294, 15.612506602037005), (0.906038, 0.906038, 0.906038), "StaticMeshActor18515", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3726.2524, 3733.4363, 3267.6997), (-3.133391836940855, 66.58697033837946, -3.8841243173187516), (0.906038, 0.906038, 0.906038), "StaticMeshActor18516", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3669.6912, 3876.92, 3249.0515), (0.20702969342821656, -76.94625602215999, 4.984837264375532), (0.906038, 0.906038, 0.906038), "StaticMeshActor18518", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (6355.029, 3425.914, 2782.7617), (-4.2227181761769215, 96.1256283711646, 12.321175270626627), (1.2617702, 1.4809228, 1.4809228), "StaticMeshActor18567", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1697.5132, 3677.0608, 3884.0344), (4.685974334079536, 9.452310503426474, 3.568080924645314), (1.035539, 0.7595414, 1.035539), "StaticMeshActor18741", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4816.1284, 4377.0, 1968.5125), (-3.8040775615831213, 63.691550456952996, 2.6412954236533754), (1.013763, 1.013763, 1.013763), "StaticMeshActor18837", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4724.1587, 3823.0747, 1521.5522), (-16.54134741043296, 101.74258507134748, 7.86404389631091), (0.986877, 0.986877, 0.986877), "StaticMeshActor18839_8", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4564.1587, 3703.0747, 1581.5522), (-24.061310366378486, -172.02143511482973, -32.25249942071654), (0.986877, 0.986877, 0.986877), "StaticMeshActor18840", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5153.6787, 3853.876, 2036.156), (10.600051584730501, -49.35284192545575, 9.559976644215896), (0.854304, 0.854304, 0.854304), "StaticMeshActor18842", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4074.738, 4389.6836, 1577.7194), (-1.3478089405413336, 54.78389858321905, 8.111745510821713), (1.032062, 1.032062, 1.032062), "StaticMeshActor18843", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3939.738, 4209.6836, 1392.7194), (-1.3478090274201688, -55.21631373581151, 8.111905425825983), (1.032062, 1.032062, 1.032062), "StaticMeshActor18845", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1515.0457, 2888.4443, 3522.9219), (-4.873107791801068, -43.508731297167834, 11.838614745345454), (1.026538, 1.026538, 0.42076397), "StaticMeshActor18864", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2291.1023, 3260.0505, 4058.6614), (2.448821019013532, -126.09499541502608, 6.720845428571518), (1.1285431, 1.1285431, 1.1285431), "StaticMeshActor18870", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (109.769844, 813.49725, 2170.9426), (-20.374816918620656, 103.91963606422287, -1.9857800408595638), (1.014027, 1.014027, 1.835742), "StaticMeshActor18871", _folder)
if a: placed += 1
else: skipped += 1

# Batch 40: StaticMesh'PWM_Quarry_2x2x5_A' (116 instances)
_mesh_path = "/Game/Unshippable/Whitebox/Rocks/Meshes/PWM_Quarry_2x2x5_A"
_materials = ['/Game/Environments/ProcTexturing/ProcMaterial_Quarry_Atlas_2']
_folder = "Reconstruction/BD_BB_Passage_SpiralCave/Meshes"
a = spawn_static_mesh(_mesh_path, _materials, (682.18115, 990.0044, 1910.0), (-6.583984162528643, -166.97775930137985, -8.43963525048581), (1.0, 1.0, 1.0), "PWM_Quarry_2x2x5_A_39", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (443.39746, 3796.6023, 2805.9324), (-7.890723529044189, 28.120453835446266, 18.410985358871912), (1.111634, 1.111634, 1.111634), "PWM_Quarry_2x2x5_A_59", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4363.241, 908.25195, 2471.5386), (-31.127824735101616, 46.56007792780379, 1.2239313407028265), (1.111634, 1.111634, 1.111634), "PWM_Quarry_2x2x5_A_123", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4520.4243, 4275.1313, 6020.3564), (13.657425967485782, 27.754434791186526, 21.38726297888752), (1.111634, 1.111634, 1.111634), "PWM_Quarry_2x2x5_A_261", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3223.6304, 2863.8987, 2734.8198), (-13.01904190528199, 28.63194432517393, 15.595625253018646), (1.111634, 1.111634, 1.111634), "PWM_Quarry_2x2x5_A_692", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5420.215, 2285.2417, 3745.0), (0.0, 8.4371342660219, -0.0), (1.0, 1.0, 1.0), "PWM_Quarry_2x2x5_A10", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5234.07, 1863.8, 3155.0), (0.0, 50.62432626772123, -0.0), (1.0, 1.0, 1.0), "PWM_Quarry_2x2x5_A11", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2876.7373, 3177.9028, 1377.7969), (0.0, -50.39406791274623, 0.0), (1.0, 1.0, 1.0), "PWM_Quarry_2x2x5_A12_5", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3326.7388, 3016.2344, 1098.8765), (-4.254241116507934, 15.309953865321958, -1.163482519570779), (1.0, 1.0, 1.0595429), "PWM_Quarry_2x2x5_A13_14", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3531.4106, 2941.3435, 1910.3724), (-12.553497213273564, 0.0, -0.0), (1.0, 1.0, 1.0), "PWM_Quarry_2x2x5_A14_41", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2501.3237, 2830.96, 2250.0693), (0.0, 0.0, 90.42442308146688), (1.5420438, 1.0, 1.0), "PWM_Quarry_2x2x5_A15_62", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (671.4586, 3236.464, 1968.1063), (4.611707583486244, 37.78160428901277, 3.566364730297924), (1.0, 1.0, 1.0), "PWM_Quarry_2x2x5_A154_48", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4283.706, 348.877, 1606.3833), (-16.241727801603943, 52.32348341134979, -15.678464862820377), (1.0, 1.0, 1.0), "PWM_Quarry_2x2x5_A154_112", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5034.2427, 3817.5232, 5249.4443), (25.275031979170585, 39.119264688312555, 10.639415051614113), (1.0, 1.0, 1.0), "PWM_Quarry_2x2x5_A154_250", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3365.4458, 2303.7603, 1878.1676), (0.0, 37.637934125761056, -0.0), (1.0, 1.0, 1.0), "PWM_Quarry_2x2x5_A154_680", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (588.0693, 3195.1924, 1893.9034), (5.718705737854137, -11.124149715741087, -1.1224591673453783), (1.0, 1.0, 1.0), "PWM_Quarry_2x2x5_A155_49", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4185.9688, 286.7751, 1578.9232), (-22.303341212734097, 0.891093300284701, 2.411085275553624), (1.0, 1.0, 1.0), "PWM_Quarry_2x2x5_A155_113", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4982.556, 3788.5393, 5146.238), (24.029076974714826, -14.828507006188733, -13.332471011756203), (1.0, 1.0, 1.0), "PWM_Quarry_2x2x5_A155_251", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3274.9534, 2262.4885, 1812.8151), (0.0, -11.06811552805539, 0.0), (1.0, 1.0, 1.0), "PWM_Quarry_2x2x5_A155_681", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (621.34216, 3118.305, 2367.8594), (-9.219764241899073, -84.6749281231449, -0.9894531434830368), (1.0, 1.0, 1.0), "PWM_Quarry_2x2x5_A156_51", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4452.424, 250.79669, 1978.1229), (-12.61761463239703, -77.6573512138692, 27.572409484316143), (1.0, 1.0, 1.0), "PWM_Quarry_2x2x5_A156_115", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4849.5605, 3651.822, 5588.135), (-14.081168639498275, -80.76510841742495, -22.647614638777814), (1.0, 1.0, 1.0), "PWM_Quarry_2x2x5_A156_253", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3356.1765, 2185.601, 2280.9434), (-9.711945288659093, -85.64392292332037, 4.897436796104826), (1.0, 1.0, 1.0), "PWM_Quarry_2x2x5_A156_683", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (440.13193, 2961.3486, 2714.5918), (-27.813635015133436, -116.14533726329404, 8.408700903457333), (1.301329, 1.301329, 1.301329), "PWM_Quarry_2x2x5_A157_52", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4491.839, 84.949524, 2363.6575), (-14.756566213764858, -113.62568426726651, 35.39495715299244), (1.301329, 1.301329, 1.301329), "PWM_Quarry_2x2x5_A157_116", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4561.0645, 3458.4448, 5827.0312), (-42.13510383368334, -104.9472157129593, -11.733061746494245), (1.301329, 1.301329, 1.301329), "PWM_Quarry_2x2x5_A157_254", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3211.1077, 2028.6448, 2644.2827), (-25.126248354545254, -118.72306722621846, 14.186474258211247), (1.301329, 1.301329, 1.301329), "PWM_Quarry_2x2x5_A157_684", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (240.6128, 3024.9946, 2691.3599), (-36.38373987216091, -161.25021137083723, 21.716977672691385), (1.301329, 1.301329, 1.301329), "PWM_Quarry_2x2x5_A158_53", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4296.3604, 105.6752, 2439.5317), (-9.898184505293129, -153.0779306812993, 32.510197132723974), (1.301329, 1.301329, 1.301329), "PWM_Quarry_2x2x5_A158_117", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4381.288, 3530.7822, 5744.29), (-58.12176115463223, -162.5792435881004, 22.800943060209786), (1.301329, 1.301329, 1.301329), "PWM_Quarry_2x2x5_A158_255", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3010.2607, 2092.2908, 2641.4287), (-30.845332712386003, -162.45774625614408, 23.895472125560723), (1.301329, 1.301329, 1.301329), "PWM_Quarry_2x2x5_A158_685", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (125.206726, 3173.7905, 2607.9595), (-31.57845742992188, -160.91892967889092, -1.715611882005433), (1.301329, 1.301329, 1.301329), "PWM_Quarry_2x2x5_A159_54", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4127.1934, 222.31468, 2425.6616), (-5.229522639574254, -151.8969790166639, 9.107334745193336), (1.301329, 1.301329, 1.301329), "PWM_Quarry_2x2x5_A159_118", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4300.1084, 3692.437, 5645.842), (-53.32148562394793, -161.95481585674887, -0.9627211765997045), (1.301329, 1.301329, 1.301329), "PWM_Quarry_2x2x5_A159_256", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2886.9832, 2241.0867, 2570.1768), (-26.053707809304413, -161.94075059512969, 0.40172679498899205), (1.301329, 1.301329, 1.301329), "PWM_Quarry_2x2x5_A159_686", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2807.9412, 2223.0725, 2185.821), (11.391950045439527, -60.62240696491585, -179.59323402702992), (1.0, 1.0, 1.0), "PWM_Quarry_2x2x5_A16_65", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2692.0195, 2299.2102, 2316.8381), (-18.678984112100213, 145.8474717992174, -173.06680083414275), (1.0, 1.0, 1.325545), "PWM_Quarry_2x2x5_A17", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2799.6973, 2103.0203, 1371.3439), (0.0, 0.0, 13.465744803780966), (1.0, 1.0, 1.0), "PWM_Quarry_2x2x5_A18_80", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2718.643, 1983.1102, 896.9843), (0.0, 0.0, 13.465744803780966), (1.0, 1.0, 1.0), "PWM_Quarry_2x2x5_A19", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (877.0957, 1059.7828, 1701.5873), (-0.07608029009098018, 110.03853405696024, 179.132817180148), (1.367137, 1.367137, 1.367137), "PWM_Quarry_2x2x5_A2_4", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (326.72412, 3758.411, 2756.426), (-12.72286318278785, 76.11159083517225, 20.728908403630548), (1.259888, 1.259888, 1.259888), "PWM_Quarry_2x2x5_A2_60", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4247.8403, 844.20105, 2481.647), (-15.764335203203562, 95.9324432664407, -8.255090371667864), (1.259888, 1.259888, 1.259888), "PWM_Quarry_2x2x5_A2_124", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4428.8916, 4247.1587, 5928.916), (-0.0846023337331078, 73.57383492871392, 38.579697662911066), (1.259888, 1.259888, 1.259888), "PWM_Quarry_2x2x5_A2_262", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3102.5334, 2825.707, 2697.4155), (-14.056000098682315, 77.46321586413553, 14.897207868053988), (1.259888, 1.259888, 1.259888), "PWM_Quarry_2x2x5_A2_693", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3088.5872, 2101.2812, 1386.9058), (-6.392852916423671, 117.60377924655454, -0.4701232045031294), (1.0, 1.0, 1.0), "PWM_Quarry_2x2x5_A20_107", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2576.5674, 3332.2234, 2319.1763), (24.985780714012808, 2.425547822828498e-06, 7.480981999006604), (1.0, 1.0, 1.0), "PWM_Quarry_2x2x5_A21_145", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3651.5586, 4061.1086, 771.3602), (-13.70806675546729, 91.16926824017703, -0.27719092610888135), (1.0, 1.0, 1.0), "PWM_Quarry_2x2x5_A22_151", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (737.234, 5424.08, 1532.8037), (0.0, 0.0, -0.0), (1.6140432, 1.0, 1.0), "PWM_Quarry_2x2x5_A23_223", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1163.7819, 5423.7964, 2408.1907), (0.0, 0.0, -37.362766073689016), (1.0, 1.0, 1.0), "PWM_Quarry_2x2x5_A24_234", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2815.4578, 5383.198, 3107.579), (0.0, 28.619101559629446, -0.0), (1.0, 1.0, 1.0), "PWM_Quarry_2x2x5_A25_286", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1068.6239, 3094.433, 3548.9849), (0.0, 0.0, -106.0260577321517), (1.0, 1.0, 1.0), "PWM_Quarry_2x2x5_A26_321", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1106.4332, 3426.7727, 3574.8884), (0.0, 0.0, -81.8170791444122), (1.0, 1.0, 1.0), "PWM_Quarry_2x2x5_A27_324", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (414.5035, 938.005, 1436.9368), (0.0, 0.0, -0.0), (1.2146126, 1.2146126, 1.2146126), "PWM_Quarry_2x2x5_A28_339", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5383.513, 3959.3635, 3750.0), (0.0, 0.0, -0.0), (1.0, 1.0, 1.0), "PWM_Quarry_2x2x5_A29", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (733.5814, 3281.0706, 2777.0303), (-8.394081100509425, -46.52621765822831, 5.395068588417279), (1.463677, 1.463677, 1.463677), "PWM_Quarry_2x2x5_A3_62", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4706.3955, 460.39893, 2291.2947), (-28.33557617014572, -40.84336846710296, 26.612401857225453), (1.463677, 1.463677, 1.463677), "PWM_Quarry_2x2x5_A3_126", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4809.758, 3758.37, 6028.1006), (0.49855044687842, -45.65540690107241, -14.521776092124266), (1.463677, 1.463677, 1.463677), "PWM_Quarry_2x2x5_A3_264", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3509.3796, 2348.3667, 2676.5981), (-12.376526970232305, -47.30689112101591, 9.721275627718741), (1.463677, 1.463677, 1.463677), "PWM_Quarry_2x2x5_A3_695", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (628.41254, 3588.8523, 1200.9983), (4.1481868170994485, -15.351727561671352, 177.18067130782913), (1.392514, 1.392514, 1.392514), "PWM_Quarry_2x2x5_A33_28", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3814.1953, 632.0633, 963.0714), (-23.528747231165468, -3.8046245812250628, -177.09261985636516), (1.392514, 1.392514, 1.392514), "PWM_Quarry_2x2x5_A33_92", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5256.3936, 4264.492, 4567.277), (21.562787527967995, -18.905551596376856, 163.7538483418173), (1.392514, 1.392514, 1.392514), "PWM_Quarry_2x2x5_A33_230", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3244.7354, 2656.1484, 1119.3948), (-1.4721678799072302, -15.315735126663224, 178.7214919720952), (1.392514, 1.392514, 1.392514), "PWM_Quarry_2x2x5_A33_660", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (428.0241, 3483.9055, 1302.7249), (-2.1792051004649293, 111.89111346847191, 5.4059681023500366), (1.380038, 1.380038, 1.380038), "PWM_Quarry_2x2x5_A35_38", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3711.6138, 496.40552, 1143.6028), (10.044982262444227, 122.63880649022558, -20.155876279976972), (1.380038, 1.380038, 1.380038), "PWM_Quarry_2x2x5_A35_102", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4987.7646, 4155.595, 4561.2505), (-2.615487365023126, 110.45111116115248, 27.170713384959), (1.380038, 1.380038, 1.380038), "PWM_Quarry_2x2x5_A35_240", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3005.9695, 2551.2017, 1246.0182), (0.0, 111.99397423512013, -0.0), (1.380038, 1.380038, 1.380038), "PWM_Quarry_2x2x5_A35_670", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (582.63574, 3535.9978, 1400.3635), (5.72914268122352, -78.76462785829507, -4.5565405361961675), (1.346451, 1.346451, 1.346451), "PWM_Quarry_2x2x5_A38_13", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3879.225, 584.9305, 1158.4817), (-2.1402351410986067, -65.35547427950183, 22.594443685694884), (1.346451, 1.346451, 1.346451), "PWM_Quarry_2x2x5_A38_77", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5144.7266, 4188.534, 4729.7466), (1.986488477132108, -80.74603885244987, -26.035004419751996), (1.346451, 1.346451, 1.346451), "PWM_Quarry_2x2x5_A38_215", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3219.4373, 2603.294, 1322.3773), (4.567073762733159, -78.24966321388504, 1.1771290902410325), (1.346451, 1.346451, 1.346451), "PWM_Quarry_2x2x5_A38_645", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5081.423, 4011.8184, 4275.811), (18.447692274681625, -10.054356577417046, 169.99286462788177), (1.266365, 1.266365, 1.266365), "PWM_Quarry_2x2x5_A39_220", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2970.7148, 2370.6165, 968.41095), (-6.404113456904026, -7.912444693127799, -178.5836352558688), (1.266365, 1.266365, 1.266365), "PWM_Quarry_2x2x5_A39_650", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (697.3317, 3445.8027, 2782.3057), (-9.929785914804985, -14.860701442305844, 14.025922960313281), (1.463677, 1.463677, 1.463677), "PWM_Quarry_2x2x5_A4_63", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4643.3877, 614.52405, 2318.755), (-37.58087156563832, -4.95221030911113, 20.365402974894963), (1.463677, 1.463677, 1.463677), "PWM_Quarry_2x2x5_A4_127", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4771.61, 3922.2046, 6041.577), (7.947116478474128, -15.160412745375355, 1.585001637960185), (1.463677, 1.463677, 1.463677), "PWM_Quarry_2x2x5_A4_265", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3473.8533, 2513.0989, 2685.5308), (-15.5582004944589, -15.202850090106484, 15.574868745130336), (1.463677, 1.463677, 1.463677), "PWM_Quarry_2x2x5_A4_696", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (629.06134, 3523.073, 1943.6583), (2.183691981406428, -122.40967939673, -6.833250986809322), (1.346451, 1.346451, 1.346451), "PWM_Quarry_2x2x5_A40_14", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4176.0938, 618.8568, 1614.7815), (14.893596866392809, -105.98802784913244, 18.722657999055148), (1.346451, 1.346451, 1.346451), "PWM_Quarry_2x2x5_A40_78", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4998.9697, 4106.1323, 5248.839), (-15.021300905407395, -121.4012868114969, -20.275942283964913), (1.346451, 1.346451, 1.346451), "PWM_Quarry_2x2x5_A40_216", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3320.7854, 2590.3691, 1858.1509), (5.2951107587482165, -122.0873079689133, -1.8948057610717985), (1.346451, 1.346451, 1.346451), "PWM_Quarry_2x2x5_A40_646", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (702.9979, 3437.826, 2035.2206), (0.6981490430615033, -156.56136230429252, -0.15291232443545177), (1.346451, 1.346451, 1.346451), "PWM_Quarry_2x2x5_A41_15", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4300.2197, 556.59973, 1657.6105), (25.45489857090603, -140.74655917150227, 13.914700780527443), (1.346451, 1.346451, 1.346451), "PWM_Quarry_2x2x5_A41_79", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5037.54, 4007.7817, 5348.623), (-21.01740511450563, -156.85576312566798, -1.4003842751910283), (1.346451, 1.346451, 1.346451), "PWM_Quarry_2x2x5_A41_217", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3403.6365, 2505.122, 1941.7328), (6.042730185206585, -156.42438653374583, 2.1746322711805885), (1.346451, 1.346451, 1.346451), "PWM_Quarry_2x2x5_A41_647", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (597.10114, 3570.2908, 2441.5752), (11.620274844214268, -109.8157582994263, -1.733969102893559), (1.346451, 1.346451, 1.346451), "PWM_Quarry_2x2x5_A42_16", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4371.87, 692.78235, 2070.1704), (17.58889487439303, -89.92287670931027, 26.81902235172152), (1.346451, 1.346451, 1.346451), "PWM_Quarry_2x2x5_A42_80", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4794.726, 4091.538, 5706.2705), (-2.6799089195023265, -111.63780537074258, -18.215814002623024), (1.346451, 1.346451, 1.346451), "PWM_Quarry_2x2x5_A42_218", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3339.5454, 2637.587, 2356.7397), (13.538431305490386, -108.58661273167564, 3.9045084025057477), (1.346451, 1.346451, 1.346451), "PWM_Quarry_2x2x5_A42_648", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (821.0189, 3565.1858, 951.18176), (9.13006005798836, 11.117291921427658, -5.96781610554315), (1.346451, 1.346451, 1.346451), "PWM_Quarry_2x2x5_A43_17", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3867.5925, 630.2969, 651.2843), (-18.101425615759474, 24.266840764313876, -13.523541907008202), (1.346451, 1.346451, 1.346451), "PWM_Quarry_2x2x5_A43_81", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5524.337, 4266.2515, 4399.1426), (30.567705630810366, 9.23826123043252, -9.903707258353894), (1.346451, 1.346451, 1.346451), "PWM_Quarry_2x2x5_A43_219", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3410.9817, 2632.482, 851.3131), (3.4105661100590665, 10.994411405874883, -7.091582361923688), (1.346451, 1.346451, 1.346451), "PWM_Quarry_2x2x5_A43_649", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (604.8685, 3119.5159, 2758.7578), (-25.49439036728401, -80.8073371754093, 0.2836382541338296), (1.463677, 1.463677, 1.463677), "PWM_Quarry_2x2x5_A5_66", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4620.998, 275.50803, 2330.3252), (-28.56315233055908, -82.92731122286273, 31.88403619345554), (1.463677, 1.463677, 1.463677), "PWM_Quarry_2x2x5_A5_130", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4697.8, 3604.535, 5945.6333), (-27.65759435342551, -70.34916743738765, -23.95431460209021), (1.463677, 1.463677, 1.463677), "PWM_Quarry_2x2x5_A5_268", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3379.4768, 2186.812, 2671.4912), (-26.285186414341887, -83.61230283025778, 6.7020290512934215), (1.463677, 1.463677, 1.463677), "PWM_Quarry_2x2x5_A5_699", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (512.41174, 3831.6316, 559.79565), (14.131884294841816, 54.58417327663169, -9.038025110308366), (1.0, 1.0, 1.0), "PWM_Quarry_2x2x5_A6_6", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3363.8242, 802.1708, 461.30634), (-1.2978004864411072, 64.39325605216116, -32.910474936959396), (1.0, 1.0, 1.0), "PWM_Quarry_2x2x5_A6_70", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5367.8286, 4589.2954, 3962.6082), (31.57814807659029, 59.663635700554245, 5.146480224524491), (1.0, 1.0, 1.0), "PWM_Quarry_2x2x5_A6_208", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3064.2307, 2898.9277, 493.28345), (10.709784172973595, 53.54407860476063, -13.868837053922574), (1.0, 1.0, 1.0), "PWM_Quarry_2x2x5_A6_638", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1634.0859, 5150.5947, 3910.9592), (-83.71045542132943, 26.618262154668336, -20.858049514228163), (1.0, 1.0, 1.0), "PWM_Quarry_2x2x5_A7_9", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5360.0, 3815.0, 3750.0), (0.0, 0.0, -0.0), (1.0, 1.0, 1.0), "PWM_Quarry_2x2x5_A8_9", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (527.8515, 3144.9114, 2211.7388), (-6.896110753614999, -46.54613782987172, 171.20978131304312), (1.116563, 1.116563, 1.116563), "PWM_Quarry_2x2x5_A80_34", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4293.5156, 247.39923, 1885.6108), (-26.930729276070718, -40.256075372321895, -167.84796522642336), (1.116563, 1.116563, 1.116563), "PWM_Quarry_2x2x5_A80_98", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4816.0093, 3700.737, 5414.0547), (1.9001279825289012, -46.184495670282764, 151.27923747661495), (1.116563, 1.116563, 1.116563), "PWM_Quarry_2x2x5_A80_236", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3247.3176, 2212.2075, 2135.1218), (-10.881318238093636, -47.21194723872929, 175.51417983940266), (1.116563, 1.116563, 1.116563), "PWM_Quarry_2x2x5_A80_666", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (396.09924, 3167.5823, 2314.707), (-6.824264831558483, 154.5105817928526, -158.92968643175143), (1.116563, 1.116563, 1.116563), "PWM_Quarry_2x2x5_A81_35", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4223.846, 250.28271, 2039.2759), (19.450696024788876, 165.86285530277917, -169.4248704307074), (1.116563, 1.116563, 1.116563), "PWM_Quarry_2x2x5_A81_99", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4656.3135, 3714.4763, 5466.817), (-21.527335056487797, 149.86881982300503, -142.34103162728428), (1.116563, 1.116563, 1.116563), "PWM_Quarry_2x2x5_A81_237", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3126.701, 2234.8784, 2250.9355), (-1.5591733195466624, 154.6939038979723, -161.43490574947586), (1.116563, 1.116563, 1.116563), "PWM_Quarry_2x2x5_A81_667", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5400.215, 2745.2417, 3755.0), (0.0, 143.43733678220661, -0.0), (1.0, 1.0, 1.0), "PWM_Quarry_2x2x5_A9", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (877.1565, 3363.6846, 928.08844), (-16.310093767607253, -179.9999580130996, -179.99996335427065), (1.395149, 1.395149, 1.395149), "PWM_Quarry_2x2x5_A91_43", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3947.0046, 442.98685, 597.4684), (11.853197395288051, -167.54067424718863, -177.97044735387263), (1.395149, 1.395149, 1.395149), "PWM_Quarry_2x2x5_A91_107", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5587.8564, 4067.5615, 4371.306), (-36.47032590833284, 175.32257800034486, -170.80313458865763), (1.395149, 1.395149, 1.395149), "PWM_Quarry_2x2x5_A91_245", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3464.4844, 2430.9807, 822.6392), (-10.482632835790369, -179.99995901885796, -179.99995901885544), (1.395149, 1.395149, 1.395149), "PWM_Quarry_2x2x5_A91_675", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5647.5024, 4067.5615, 4184.5786), (-36.47032590833284, 175.32257800034486, -170.80313458865763), (1.395149, 1.395149, 1.395149), "PWM_Quarry_2x2x5_A92", _folder)
if a: placed += 1
else: skipped += 1

# Batch 41: StaticMesh'PWM_Quarry_2x2x5_B' (55 instances)
_mesh_path = "/Game/Unshippable/Whitebox/Rocks/Meshes/PWM_Quarry_2x2x5_B"
_materials = ['/Game/Environments/ProcTexturing/ProcMaterial_Quarry_Atlas_2']
_folder = "Reconstruction/BD_BB_Passage_SpiralCave/Meshes"
a = spawn_static_mesh(_mesh_path, _materials, (862.2393, 882.9939, 1623.7001), (0.0, 53.13953301718898, -0.0), (1.30235, 1.30235, 1.30235), "PWM_Quarry_2x2x5_B_1", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (650.23584, 3635.243, 2842.1787), (-16.357737643519968, -8.83777399394564, -157.78785110931207), (1.204144, 1.204144, 1.204144), "PWM_Quarry_2x2x5_B_64", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4591.471, 794.37683, 2400.2905), (-44.47309279896009, 2.0993542552049758, -154.715893186835), (1.204144, 1.204144, 1.204144), "PWM_Quarry_2x2x5_B_128", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4703.9087, 4104.0366, 6105.17), (2.8080975406877102, -8.107986154919681, -168.19336965583904), (1.204144, 1.204144, 1.204144), "PWM_Quarry_2x2x5_B_266", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3433.08, 2702.5388, 2749.878), (-22.1136486164254, -9.156036280220572, -156.82306671405547), (1.204144, 1.204144, 1.204144), "PWM_Quarry_2x2x5_B_697", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3067.8193, 2033.079, 1082.0508), (-4.519226267099939, 58.69484443441979, 6.597002250856711), (1.0, 1.0, 1.0), "PWM_Quarry_2x2x5_B10_98", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (694.8296, 3219.8167, 1172.0996), (7.484402910794782, -1.5704076667115603, -177.33194077137796), (1.101083, 1.101083, 1.101083), "PWM_Quarry_2x2x5_B11_26", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3934.6494, 282.66083, 893.4845), (-20.72003968654911, 11.128337868782186, -178.6623134052254), (1.101083, 1.101083, 1.101083), "PWM_Quarry_2x2x5_B11_90", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5335.366, 3800.9163, 4503.2354), (27.5130766384973, -4.8271810685236405, 173.7164070427842), (1.101083, 1.101083, 1.101083), "PWM_Quarry_2x2x5_B11_228", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3307.875, 2187.1128, 1083.9019), (1.6591073064853015, -1.5576782239194467, -177.17244513659412), (1.101083, 1.101083, 1.101083), "PWM_Quarry_2x2x5_B11_658", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (690.38336, 3728.1355, 750.1838), (-2.690487601460761, -156.05675320821192, 7.062647773197742), (1.396515, 1.396515, 1.396515), "PWM_Quarry_2x2x5_B13_5", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3627.3516, 749.65674, 541.485), (22.044848216124713, -141.10717389822554, 20.99374204812471), (1.396515, 1.396515, 1.396515), "PWM_Quarry_2x2x5_B13_69", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5469.691, 4457.168, 4187.995), (-24.39307017813283, -156.22149559719256, 5.579026341484271), (1.396515, 1.396515, 1.396515), "PWM_Quarry_2x2x5_B13_207", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3260.6133, 2795.432, 664.6177), (2.636295591921522, -156.05790063317696, 9.426726502966014), (1.396515, 1.396515, 1.396515), "PWM_Quarry_2x2x5_B13_637", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (471.38586, 3651.9363, 2585.888), (1.6796464740445107, -25.64293869052367, 18.01115807975577), (1.396515, 1.396515, 1.396515), "PWM_Quarry_2x2x5_B17_8", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4314.4404, 757.3518, 2259.456), (-24.47715459556839, -15.331282427910596, 28.96481894823871), (1.396515, 1.396515, 1.396515), "PWM_Quarry_2x2x5_B17_72", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4625.4355, 4158.382, 5807.1104), (16.547597877927625, -28.754293259083813, 1.8834630925628544), (1.396515, 1.396515, 1.396515), "PWM_Quarry_2x2x5_B17_210", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3229.1323, 2719.2322, 2513.0708), (-3.573792089640135, -25.684667570718595, 20.53443851079952), (1.396515, 1.396515, 1.396515), "PWM_Quarry_2x2x5_B17_640", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (741.35046, 931.5122, 1842.6549), (-1.5695496419809745, 98.80883270017351, -177.06317534476594), (1.5, 1.5, 1.5), "PWM_Quarry_2x2x5_B2_2", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (589.5451, 3746.0623, 2883.3462), (-6.4207683769747215, -2.945429604744705, 38.875558259198954), (1.204144, 1.204144, 1.204144), "PWM_Quarry_2x2x5_B2_65", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4535.5176, 893.38354, 2469.0352), (-34.64764841754619, 9.856433906794198, 38.15338383314491), (1.204144, 1.204144, 1.204144), "PWM_Quarry_2x2x5_B2_129", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4631.1064, 4210.685, 6136.5566), (13.56114692084629, -4.0119020966836985, 30.224933954257875), (1.204144, 1.204144, 1.204144), "PWM_Quarry_2x2x5_B2_267", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3376.8828, 2813.3584, 2796.9946), (-12.240417358221656, -2.9950866307546145, 39.1814351975998), (1.204144, 1.204144, 1.204144), "PWM_Quarry_2x2x5_B2_698", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (881.9044, 988.6731, 1776.8796), (-5.658568856948039, -44.621793004134865, -177.18928632665938), (1.75, 1.75, 1.75), "PWM_Quarry_2x2x5_B3_3", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1261.3402, 5047.228, 3916.844), (47.89634019150988, -88.40092797852996, 87.75783977761895), (1.0, 1.0, 1.0), "PWM_Quarry_2x2x5_B4_12", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (229.01538, 3562.1814, 2696.6394), (23.22763681319661, 8.364691492520526, -155.0108475411481), (1.999362, 1.999362, 1.999362), "PWM_Quarry_2x2x5_B40_32", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4176.8643, 628.7687, 2468.273), (-4.408406996429234, 19.90686885006852, -160.9361648414851), (1.999362, 1.999362, 1.999362), "PWM_Quarry_2x2x5_B40_96", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4360.957, 4063.1636, 5814.206), (44.38472912801233, 4.361321686597882, -161.16385355920144), (1.999362, 1.999362, 1.999362), "PWM_Quarry_2x2x5_B40_234", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2999.2593, 2629.4773, 2647.8584), (17.45978295981387, 8.0558722608597, -155.89806275255535), (1.999362, 1.999362, 1.999362), "PWM_Quarry_2x2x5_B40_664", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (149.76855, 3443.4888, 2722.6216), (9.822289847773442, -89.26314237677619, 137.94190684839808), (1.999362, 1.999362, 1.999362), "PWM_Quarry_2x2x5_B42_33", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4145.7227, 498.69733, 2524.4397), (6.325031428526329, -72.66362184573305, 166.25019957397373), (1.999362, 1.999362, 1.999362), "PWM_Quarry_2x2x5_B42_97", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4279.3174, 3944.7173, 5795.54), (2.0757294755925644, -91.92863898420526, 117.49103942895533), (1.999362, 1.999362, 1.999362), "PWM_Quarry_2x2x5_B42_235", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2923.06, 2510.785, 2681.7524), (9.696237716580624, -88.26019451943499, 143.85363348559417), (1.999362, 1.999362, 1.999362), "PWM_Quarry_2x2x5_B42_665", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (853.3765, 3319.9365, 922.3013), (-0.768518051831634, -98.41639412457127, -15.169646930422658), (1.396515, 1.396515, 1.396515), "PWM_Quarry_2x2x5_B44_42", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3932.997, 395.07602, 602.07324), (1.3151645786917445, -85.7386275586681, 12.989986903776705), (1.396515, 1.396515, 1.396515), "PWM_Quarry_2x2x5_B44_106", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5569.629, 3926.4976, 4339.1904), (-10.9792786749486, -96.92960027176846, -34.502495878728524), (1.396515, 1.396515, 1.396515), "PWM_Quarry_2x2x5_B44_244", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3440.2397, 2287.2327, 819.29645), (0.08687350726408583, -98.45071272215264, -9.405150737186512), (1.396515, 1.396515, 1.396515), "PWM_Quarry_2x2x5_B44_674", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (104.31067, 3384.6528, 2602.1853), (-17.747101852754476, -106.43017009289518, 153.65103605167909), (1.88036, 1.88036, 1.88036), "PWM_Quarry_2x2x5_B46_23", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4062.5803, 423.8391, 2437.7417), (-9.968665674362072, -100.73972466968246, -178.3511594120225), (1.88036, 1.88036, 1.88036), "PWM_Quarry_2x2x5_B46_87", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4279.548, 3902.9136, 5660.318), (-29.613958317069017, -98.81324627446647, 133.6748172710555), (1.88036, 1.88036, 1.88036), "PWM_Quarry_2x2x5_B46_225", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2865.609, 2451.949, 2566.5542), (-16.015015189327666, -108.12033323718676, 159.4661865485882), (1.88036, 1.88036, 1.88036), "PWM_Quarry_2x2x5_B46_655", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (314.70685, 3488.39, 2107.2656), (8.328257718532338, 57.425737384977865, 16.736668710024567), (1.503211, 1.503211, 1.503211), "PWM_Quarry_2x2x5_B47_29", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3989.961, 533.3367, 1906.0369), (-5.441711044970508, 69.32942119131904, -7.980498273545711), (1.503211, 1.503211, 1.503211), "PWM_Quarry_2x2x5_B47_93", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4647.8223, 4061.1743, 5287.087), (25.267470187588536, 61.111507169399964, 31.057182902432015), (1.503211, 1.503211, 1.503211), "PWM_Quarry_2x2x5_B47_231", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3024.667, 2555.686, 2052.83), (5.164038670513916, 56.846193326939016, 11.808322192748617), (1.503211, 1.503211, 1.503211), "PWM_Quarry_2x2x5_B47_661", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3196.9563, 3116.4353, 995.41693), (0.0, -22.55721975084145, 0.0), (1.0, 1.0, 1.0), "PWM_Quarry_2x2x5_B5_17", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (931.48315, 3502.9578, 821.49695), (0.23218742787128946, 87.72438617010611, 5.82285166982568), (1.242487, 1.242487, 1.242487), "PWM_Quarry_2x2x5_B52_46", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3914.7236, 582.66077, 482.7545), (1.1154874087665339, 99.92626436206753, -22.400342290914406), (1.242487, 1.242487, 1.242487), "PWM_Quarry_2x2x5_B52_110", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5673.96, 4217.31, 4309.0845), (8.394483904219658, 88.74772900525281, 26.058253484444165), (1.242487, 1.242487, 1.242487), "PWM_Quarry_2x2x5_B52_248", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3507.7078, 2570.254, 711.0827), (0.0, 87.71260715409015, -0.0), (1.242487, 1.242487, 1.242487), "PWM_Quarry_2x2x5_B52_678", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5741.8613, 4217.31, 4180.6265), (8.394483904219658, 88.74772900525281, 26.058253484444165), (1.242487, 1.242487, 1.242487), "PWM_Quarry_2x2x5_B53", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3215.427, 3098.412, 1239.979), (6.319439551628865, 173.53535516484774, -7.7122191563486915), (1.0, 1.0, 1.0), "PWM_Quarry_2x2x5_B6", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3159.0798, 3155.2688, 1239.979), (6.319440828077295, -175.31343616666584, -7.712219201967477), (1.0, 1.0, 1.0), "PWM_Quarry_2x2x5_B7", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2672.7354, 2343.075, 2292.5686), (12.53918795571204, 0.7957782558231389, -179.173253201329), (1.0, 1.0, 1.0), "PWM_Quarry_2x2x5_B8_72", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2589.7502, 2415.6465, 2273.2478), (-2.5609418267428365, -104.5791792812441, 159.68060278542572), (1.0, 1.0, 1.0), "PWM_Quarry_2x2x5_B9", _folder)
if a: placed += 1
else: skipped += 1

# Batch 42: StaticMesh'PWM_Quarry_3x3x2' (5 instances)
_mesh_path = "/Game/Unshippable/Whitebox/Rocks/Meshes/PWM_Quarry_3x3x2"
_materials = ['/Game/Environments/ProcTexturing/ProcMaterial_Quarry_Atlas_A']
_folder = "Reconstruction/BD_BB_Passage_SpiralCave/Meshes"
a = spawn_static_mesh(_mesh_path, _materials, (750.35187, 2818.462, 652.553), (14.702691473859163, 93.15271285291081, 175.91293879608972), (1.4299823, 1.4299823, 1.4299823), "PWM_Quarry_1X1x1_C150", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (836.9619, 2609.1714, 604.077), (12.149856080777468, 93.29757279997119, 176.86112265793827), (1.8132645, 1.8132645, 1.8132645), "PWM_Quarry_1X1x1_C151", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1045.0864, 2429.5671, 524.5148), (13.21580581490651, -51.20632247477672, 161.51784571592583), (1.813264, 1.813264, 1.813264), "PWM_Quarry_1X1x1_C152", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (866.30365, 4024.1091, 638.50757), (8.402955470888068, -131.79151633995295, 168.42292939257823), (1.813264, 1.813264, 1.813264), "PWM_Quarry_1X1x1_C153", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (857.31696, 2276.4736, 588.7033), (15.591402370181578, 41.43923540312821, 171.15568960017308), (1.813264, 1.813264, 1.813264), "PWM_Quarry_1X1x1_C158", _folder)
if a: placed += 1
else: skipped += 1

# Batch 43: StaticMesh'PWM_Quarry_4x4x4_A' (681 instances)
_mesh_path = "/Game/Unshippable/Whitebox/Rocks/Meshes/PWM_Quarry_4x4x4_A"
_materials = ['/Game/Environments/ProcTexturing/ProcMaterial_Quarry_Atlas_2']
_folder = "Reconstruction/BD_BB_Passage_SpiralCave/Meshes"
a = spawn_static_mesh(_mesh_path, _materials, (3142.148, 2149.4888, 1049.1477), (-6.823455733808002, 33.8818902745037, 10.035277386861209), (0.727887, 0.544342, 1.0), "PWM_Quarry_4x4x4_A10", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3025.908, 2136.166, 1379.9381), (-2.425231884421603, -6.544647922889158, 12.063831580926058), (0.727887, 0.544342, 1.0), "PWM_Quarry_4x4x4_A11", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3040.7415, 2182.525, 1603.1279), (-2.425231884421603, -6.544647922889158, 12.063831580926058), (0.727887, 0.544342, 1.0), "PWM_Quarry_4x4x4_A12", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (13.941162, 3138.866, 2868.5962), (-33.66491662353411, -81.09965368578321, -42.68520823884557), (0.754483, 0.754483, 0.754483), "PWM_Quarry_4x4x4_A152_55", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4160.9277, 183.81802, 2706.5737), (-35.28421812871363, -88.41676071333181, -8.320123642805374), (0.754483, 0.754483, 0.754483), "PWM_Quarry_4x4x4_A152_119", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4105.451, 3628.6484, 5844.7617), (-35.15582544466587, -66.52891553419886, -69.06347923589549), (0.754483, 0.754483, 0.754483), "PWM_Quarry_4x4x4_A152_257", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2802.7559, 2206.162, 2840.7603), (-34.37066631156631, -85.00824162342413, -35.70483455700304), (0.754483, 0.754483, 0.754483), "PWM_Quarry_4x4x4_A152_687", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (535.0846, 3325.8792, 2535.7876), (-10.46004499652058, 0.0, -0.0), (1.0, 1.0, 1.0), "PWM_Quarry_4x4x4_A163_56", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4413.676, 447.95862, 2173.9624), (-38.60307530217348, 13.62882967746638, -2.541894770524758), (1.0, 1.0, 1.0), "PWM_Quarry_4x4x4_A163_120", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4707.224, 3839.3286, 5740.8086), (9.970964549772871, -0.48589062756237117, -7.498347488954597), (1.0, 1.0, 1.0), "PWM_Quarry_4x4x4_A163_258", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3287.415, 2393.1753, 2456.7617), (-16.28750807700011, 0.0, -0.0), (1.0, 1.0, 1.0), "PWM_Quarry_4x4x4_A163_688", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (681.1385, 3477.8403, 968.96643), (2.1113320706235896, 63.62528887303658, 7.597462133997832), (1.0, 1.0, 1.0), "PWM_Quarry_4x4x4_A175_24", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3774.0095, 518.17993, 729.9231), (-8.39335685158045, 77.63810508148644, -18.687867965668914), (1.0, 1.0, 1.0), "PWM_Quarry_4x4x4_A175_88", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5247.7197, 4186.5815, 4303.6875), (17.67270958407725, 65.80652136562675, 23.075606763997545), (1.0, 1.0, 1.0), "PWM_Quarry_4x4x4_A175_226", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3124.405, 2545.1365, 898.43835), (-0.48263547975852417, 63.551059550981485, 2.3781887947730347), (1.0, 1.0, 1.0), "PWM_Quarry_4x4x4_A175_656", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (592.16486, 3403.0237, 1507.0769), (-0.3000623945532624, 118.65057626051602, 7.318443122631597), (0.923847, 0.923847, 0.923847), "PWM_Quarry_4x4x4_A176_25", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3965.085, 464.1878, 1243.3933), (14.596880015977908, 128.10266375882796, -16.92929780261112), (0.923847, 0.923847, 0.923847), "PWM_Quarry_4x4x4_A176_89", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5072.8945, 3945.417, 4784.8545), (-3.365900150236644, 117.43441968482725, 28.86481481670066), (0.923847, 0.923847, 0.923847), "PWM_Quarry_4x4x4_A176_227", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3190.0105, 2370.3198, 1432.6483), (2.491496122891099, 118.55263714129532, 2.201676508768161), (0.923847, 0.923847, 0.923847), "PWM_Quarry_4x4x4_A176_657", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (522.5375, 3406.8362, 1872.4646), (-5.475282764018138, 176.2377969280028, 2.280120931114534), (1.0, 1.0, 1.0), "PWM_Quarry_4x4x4_A177_27", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4075.5308, 479.06488, 1598.2893), (22.758591079960265, -171.18664434125623, 2.505404240597753), (1.0, 1.0, 1.0), "PWM_Quarry_4x4x4_A177_91", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4925.618, 4003.168, 5130.751), (-25.179011170319917, 173.13590387156077, 11.88858074856816), (1.0, 1.0, 1.0), "PWM_Quarry_4x4x4_A177_229", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3207.5835, 2474.1323, 1798.1406), (0.33969936851718807, 176.25492125204883, 1.898397465805138), (1.0, 1.0, 1.0), "PWM_Quarry_4x4x4_A177_659", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (765.87354, 3379.5715, 1155.4634), (6.103137438320601, -19.921150027267366, -0.25649682880794294), (0.789448, 0.789448, 1.169861), "PWM_Quarry_4x4x4_A188_58", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3954.56, 451.8681, 850.845), (-21.04746721997944, -8.438191545039876, 7.637297562148973), (0.789448, 0.789448, 1.169861), "PWM_Quarry_4x4x4_A188_122", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5252.923, 3978.0332, 4370.616), (22.34033164723238, -24.179864708268948, -15.24770887736375), (1.0, 1.0, 1.169861), "PWM_Quarry_4x4x4_A188_260", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3167.743, 2346.8677, 980.9616), (0.6218067941832234, -19.804718062206515, 1.7261664824384781), (1.0, 1.0, 1.169861), "PWM_Quarry_4x4x4_A188_690", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (126.58332, 3660.768, 4218.487), (-4.044891637096014, -157.31777454946283, -1.6885682351309943), (1.0495036, 1.0, 1.25), "PWM_Quarry_4x4x4_A4_5", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (209.42873, 2759.444, 4235.392), (3.0451712867853584, -13.928313929952896, 3.2970338990983046), (1.0, 1.0, 1.25), "PWM_Quarry_4x4x4_A5", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2778.2402, 190.18533, 4218.487), (-4.219207332111607, 91.43524538800689, -3.4752193969259157), (1.0, 1.0, 1.25), "PWM_Quarry_4x4x4_A6", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3644.4287, 134.44409, 4260.392), (1.2765759869481927, -13.024049233385636, -2.3777773704068466), (1.0, 1.0, 1.25), "PWM_Quarry_4x4x4_A7", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2905.2583, 2044.3408, 952.1209), (0.0, 0.0, 12.114154242257165), (0.7278874, 0.54434246, 1.0), "PWM_Quarry_4x4x4_A8_94", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (667.56, 3405.8699, 1593.8975), (0.5892646663631282, 84.21630046158504, 5.797696369720628), (0.860851, 0.860851, 0.860851), "PWM_Quarry_4x4x4_A9_31", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4069.875, 487.99994, 1284.4099), (-0.2293075450925777, 96.6664879476133, -22.42556067638633), (0.860851, 0.860851, 0.860851), "PWM_Quarry_4x4x4_A9_95", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5158.6724, 4032.5474, 4922.2935), (9.929694454774971, 85.5322036280599, 25.546102435137385), (0.860851, 0.860851, 0.860851), "PWM_Quarry_4x4x4_A9_233", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3323.5728, 2473.166, 1506.2885), (0.0, 84.18648411066266, -0.0), (0.860851, 0.860851, 0.860851), "PWM_Quarry_4x4x4_A9_663", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5302.1245, 2509.5232, 678.4873), (-3.94070377608259, -86.96124656009708, 4.289409051163819), (0.9579219, 0.9579219, 0.9579219), "StaticMeshActor_17608", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2540.0583, 5266.9673, 1216.5077), (-2.162200734613095, -85.35003110660921, -4.997191580936103), (0.88970166, 0.88970166, 0.88970166), "StaticMeshActor_17609", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4341.724, 4729.4976, 1481.0538), (6.204638848947701, 14.006060602090983, 6.590936458968605), (1.061514, 1.061514, 1.061514), "StaticMeshActor_17610", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4193.191, 4996.3228, 1556.1536), (3.8110477039358477, -88.28677758290159, 9.271213066208897), (0.91335344, 0.91335344, 0.91335344), "StaticMeshActor_17611", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3962.949, 5068.6294, 1562.7521), (-6.358763973871389, -3.9831540934789715, -4.582092574172992), (0.8902553, 0.8902553, 0.8902553), "StaticMeshActor_17612", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2742.3176, 3165.4055, 692.0259), (-2.0468449690919845, -70.62058257725211, 6.6637358830400215), (0.836589, 0.836589, 0.836589), "StaticMeshActor_17613", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1670.7106, 5267.566, 989.3684), (-4.123870631936111, 104.4921785120739, 0.47759242345879616), (1.003293, 1.003293, 1.003293), "StaticMeshActor_17614", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2523.6228, 4934.1035, 1096.7363), (-0.01803650364076149, -86.09298668858101, -7.407286535244831), (0.98021615, 0.98021615, 0.98021615), "StaticMeshActor_17615", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2631.3762, 5647.4424, 1033.1244), (4.332914537217543, -86.23553495319601, -178.73789888578122), (0.9014699, 0.9014699, 0.9014699), "StaticMeshActor_17616", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4256.35, 4832.913, 3079.8884), (-4.535553139735275, -5.793700919245872, 3.2531118750582793), (0.81306845, 0.81306845, 0.81306845), "StaticMeshActor_17617", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4185.99, 5394.844, 3156.2039), (-2.046813827878294, -6.71682760212242, 4.990853845058319), (1.086247, 1.086247, 1.086247), "StaticMeshActor_17618", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3826.04, 5514.437, 3145.7478), (8.471974564570745, 174.3190530074548, -8.73370104635413), (1.0084922, 1.0084922, 1.0084922), "StaticMeshActor_17619", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4247.4087, 5114.2324, 3158.606), (0.0, 0.0, -0.0), (0.9222643, 0.9222643, 0.9222643), "StaticMeshActor_17620", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3816.968, 5103.738, 3097.0254), (-4.352020185925478, 14.93272326944722, -6.652679819067126), (0.84870195, 0.84870195, 0.84870195), "StaticMeshActor_17621", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2716.3079, 2235.0928, 674.1779), (15.448931222718725, 0.8579003638555929, 7.703893131500309), (1.0669678, 1.0669678, 1.0669678), "StaticMeshActor_17623", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2465.9573, 6122.832, 658.48615), (6.916788359704109, -84.83441343539693, -9.193327805335114), (0.84831256, 0.84831256, 0.84831256), "StaticMeshActor_17624", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3798.5498, 602.73926, 3949.1704), (5.57085738182887, -144.69189665169915, 14.620046235658323), (0.8467878, 0.8467878, 0.8467878), "StaticMeshActor_17625", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3663.4675, 765.73004, 3858.9792), (5.28912038714664, -13.948883429189797, 4.1097334465525455), (0.851993, 0.851993, 0.851993), "StaticMeshActor_17626", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3648.8792, 4956.584, 1131.7903), (-5.020842413337075, -99.35725310832207, -1.569518785983217), (1.0125502, 1.0125502, 1.0125502), "StaticMeshActor_17627", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3294.4954, 4896.8027, 1151.5605), (2.8430799349498366, -88.04144085272439, -1.3191833326763973), (1.0585716, 1.0585716, 1.0585716), "StaticMeshActor_17628", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3283.4695, 2900.8333, 695.6789), (-9.24206487495282, 92.19152146846818, -4.464140554131859), (1.0098472, 1.0098472, 1.0098472), "StaticMeshActor_17629", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2998.0803, 3000.1, 754.21594), (-1.0024415235467339, -88.60684860772744, -9.722687299412705), (0.8268419, 0.8268419, 0.8268419), "StaticMeshActor_17630", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1736.0691, 4881.9062, 985.2753), (-0.4112853944410496, -10.167601247912588, 1.8983787322415497), (1.0194595, 1.0194595, 1.0194595), "StaticMeshActor_17631", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2556.0618, 5468.136, 3815.8982), (3.778788487161966, 172.14823070004087, 3.2933819261333133), (0.9816466, 0.54711676, 0.9816466), "StaticMeshActor_17632", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2996.0652, 5590.3833, 3796.8691), (7.721441644115214, 179.160009093875, -5.846772350824862), (0.8613028, 0.8613028, 0.8613028), "StaticMeshActor_17633", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5396.6597, 5409.099, 3963.0142), (-0.6875610321620337, -174.28369834544606, 0.788599002845174), (0.9027358, 0.9027358, 0.9027358), "StaticMeshActor_17634", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5298.334, 4781.8633, 3761.3882), (-7.328643407771569, 90.93502050530418, 3.879337192934088), (0.90289885, 0.90289885, 0.90289885), "StaticMeshActor_17635", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5395.226, 4606.749, 3962.2534), (-0.1054992882866428, -179.8771180869024, 3.1769200091104772), (1.0275903, 1.0275903, 1.0275903), "StaticMeshActor_17636", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5550.8296, 5241.1753, 4001.2637), (-3.1208193012265535, 96.48072300536619, 8.59571641183877), (0.9560288, 0.9560288, 0.9560288), "StaticMeshActor_17637", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5711.9453, 5493.271, 4112.078), (-7.744627650709658, -160.38915314146612, -7.1954646272679215), (0.8901915, 0.8901915, 0.8901915), "StaticMeshActor_17638", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5498.486, 3582.735, 3821.54), (-13.86529400994611, -0.17492674749242404, -0.02151488975081874), (0.80794996, 0.80794996, 0.80794996), "StaticMeshActor_17639", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5441.682, 4261.8223, 3760.231), (-3.5673520907086, -0.33123781339115616, 0.3877951157362938), (1.0870092, 1.0870092, 1.0870092), "StaticMeshActor_17640", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5547.2246, 5650.3706, 4077.4607), (0.6183302242885894, -149.33411412964668, 6.632497671797715), (0.8997293, 0.8997293, 0.8997293), "StaticMeshActor_17641", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (6060.572, 5633.243, 3990.2102), (-0.5185242811358816, 20.133062110051167, 10.756973729032042), (1.0692445, 1.0692445, 1.0692445), "StaticMeshActor_17642", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (6342.117, 5856.328, 4025.2544), (-10.378995941501916, -62.94988379298511, -0.0958866761583111), (0.8073136, 0.8073136, 0.8073136), "StaticMeshActor_17643", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5789.6074, 604.8228, 3962.3503), (0.14288751935721733, 179.90383089963655, -8.769284747706198), (0.92968214, 0.92968214, 0.92968214), "StaticMeshActor_17644", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5392.8784, 595.7417, 3953.9812), (4.712133700003333, -86.63303542312268, 3.945972724301214), (0.90724206, 0.90724206, 0.90724206), "StaticMeshActor_17645", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3393.3518, 2192.4592, 762.5434), (-2.386413114623827, -94.73315637751236, 6.942844124184249), (1.0650581, 1.0650581, 1.0650581), "StaticMeshActor_17646", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2996.2388, 2199.6433, 770.653), (-8.526581236244793, -87.41020225589068, 9.588267422165726), (0.9369675, 0.9369675, 0.9369675), "StaticMeshActor_17647", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5683.962, 194.98297, 851.4216), (1.3253295391080975, 97.55066264789367, 3.4736855915419844), (0.89330953, 0.89330953, 0.89330953), "StaticMeshActor_17648", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5697.889, 703.06683, 853.011), (0.18127262635794453, 96.20664247617543, 9.018800068788753), (0.9864049, 0.9864049, 0.9864049), "StaticMeshActor_17649", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3396.8528, 2594.0508, 755.857), (8.63187663431048, 94.25479123896902, 6.175577502332205), (0.8817226, 0.8817226, 0.8817226), "StaticMeshActor_17650", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (263.09265, 854.4732, 680.64386), (-3.3688041390996206, 89.39841189902394, -9.255035940828597), (0.8635316, 0.8635316, 0.8635316), "StaticMeshActor_17651", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (45.335373, 766.0871, 622.755), (-0.799560464756542, -174.92263287488035, -6.427947368035501), (1.0891464, 1.0891464, 1.0891464), "StaticMeshActor_17652", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (293.45667, 5678.689, 599.65546), (1.1468707675797978, -93.9983619645905, -1.659942707525207), (0.84283745, 0.84283745, 0.84283745), "StaticMeshActor_17653", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (195.74852, 5796.2607, 757.4762), (1.9181630533611227, -80.60510239514116, -1.0908508086291429), (0.87463003, 0.87463003, 0.87463003), "StaticMeshActor_17654", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2712.6743, 4525.4, 1040.7491), (4.631583877796143, 176.46409875706377, -0.027740480917626525), (1.04659, 1.04659, 1.04659), "StaticMeshActor_17655", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4076.282, 4502.5483, 1378.8898), (-1.2105712710304235, -165.27432185213954, 1.341662974361962), (1.0354648, 1.0354648, 1.0354648), "StaticMeshActor_17656", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5251.434, 3090.4968, 1806.3435), (1.1823339485213273, -16.786896611003986, 0.24068883621435153), (0.89220756, 0.89220756, 0.89220756), "StaticMeshActor_17657", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4559.4585, 3454.8906, 1795.9119), (0.0, -109.6871613988991, 0.0), (0.816868, 0.816868, 0.816868), "StaticMeshActor_17658", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5390.6094, 3793.1057, 1951.168), (-9.935760606844719, -99.75744436975083, -8.632691604818035), (0.8069727, 0.8069727, 0.8069727), "StaticMeshActor_17659", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5111.9814, 1628.792, 3067.8242), (0.5924100747862094, -65.941841618772, 7.019568225692142), (0.88002586, 0.88002586, 0.88002586), "StaticMeshActor_17660", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4845.8467, 1481.0422, 2981.7068), (5.308250950418007, 105.5445354367898, 6.440071818510801), (1.0306427, 1.0306427, 1.0306427), "StaticMeshActor_17661", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3553.4304, 2974.1658, 3104.6592), (-3.4825744064025366, 171.35034959992277, -4.2438968211935135), (1.0833223, 1.0833223, 1.0833223), "StaticMeshActor_17662", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3557.5544, 2549.8315, 3176.6892), (-2.6358032825066595, -165.74741821380834, -4.7864074847599305), (1.0295877, 1.0295877, 1.0295877), "StaticMeshActor_17664", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3768.7434, 837.70764, 3128.2502), (-4.693480404220422, -174.33496450851666, -0.956451344925663), (0.93015206, 0.93015206, 0.93015206), "StaticMeshActor_17665", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3395.3752, 2993.398, 3159.274), (-6.657287227854057, 172.94354165683245, -5.188415710552959), (1.0141362, 1.0141362, 1.0141362), "StaticMeshActor_17666", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3404.7559, 2597.185, 3159.472), (-8.04318336641506, 86.34613985753927, 0.18302802025021464), (1.0211583, 1.0211583, 1.0211583), "StaticMeshActor_17667", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2991.7737, 1007.29016, 3153.6848), (-1.5432738147037275, 87.08297053924008, 0.4920033512553613), (0.8091937, 0.8091937, 0.8091937), "StaticMeshActor_17668", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2990.2903, 2593.8433, 3152.8228), (6.670416693116171, 84.10680857205631, -0.4327699108616875), (0.80684954, 0.80684954, 0.80684954), "StaticMeshActor_17669", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5916.3623, 3934.173, 2212.196), (4.496880114148372, 89.39190507260557, -5.409881130392624), (0.8051055, 0.8051055, 0.8051055), "StaticMeshActor_17670", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (6364.839, 3408.756, 2342.8528), (-1.1062010990406999, -154.41249211828656, 1.1154310023642084), (1.0733075, 1.0733075, 1.0733075), "StaticMeshActor_17671", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5411.256, 3738.0884, 2152.3406), (21.738849659498847, 141.49327974292945, -8.688690166626683), (0.8259294, 0.8259294, 0.8259294), "StaticMeshActor_17672", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5230.9165, 4059.691, 2320.727), (-12.11010506133679, 114.52495603749522, 10.612344828676996), (0.98686796, 0.98686796, 0.98686796), "StaticMeshActor_17674", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5522.124, 3523.2334, 2146.9392), (-0.026916530187868593, 84.40221485972808, -0.5504150544801011), (0.91897947, 0.91897947, 0.91897947), "StaticMeshActor_17675", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2243.0332, 4370.31, 677.8813), (-14.504182824094363, -83.23929803204699, 5.469432157596642), (0.94738257, 0.94738257, 0.94738257), "StaticMeshActor_17676", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2627.929, 4333.0, 766.50775), (-7.273834675376026, -24.281191927791625, -21.997773143664062), (0.9482718, 0.9482718, 0.9482718), "StaticMeshActor_17677", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4278.712, 4302.0615, 657.1559), (2.955033022788373, 73.42762138857537, -3.304595354759296), (0.8929751, 0.8929751, 0.8929751), "StaticMeshActor_17678", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3835.5325, 4202.8813, 694.6687), (-3.6277164196026344, 150.30545691736248, -7.481996307073638), (0.9589801, 0.9589801, 0.9589801), "StaticMeshActor_17679", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3341.328, 3489.7424, 3961.2754), (-6.881072634965507, -99.18387193674155, -5.8656614867711045), (0.99320203, 0.89713293, 1.0368719), "StaticMeshActor_17681", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2999.0679, 3402.0486, 3958.0747), (3.675952206590371, -179.4004431457034, 1.5804669526575532), (1.0054054, 1.0054054, 1.0054054), "StaticMeshActor_17682", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3005.5764, 3805.6692, 3960.8958), (-14.193053569344858, -85.47540060780328, 2.2359285912911604), (1.0472652, 1.0472652, 1.0472652), "StaticMeshActor_17683", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2617.7761, 3552.5923, 3938.4287), (6.684978454681603, -71.57880278411984, -2.6550902434317623), (0.94034606, 0.94034606, 0.94034606), "StaticMeshActor_17684", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2587.164, 3402.9827, 3966.1384), (5.329262282389637, -174.36381327020518, -7.803222939322411), (0.9896549, 0.9896549, 0.9896549), "StaticMeshActor_17685", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2719.7678, 3762.5303, 3868.1812), (2.6979310764106286, 83.04092649032887, -5.669615612846969), (0.81126845, 0.81126845, 0.81126845), "StaticMeshActor_17686", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2680.1091, 3099.531, 3920.472), (-1.154022068086485, -16.405333468280933, 6.975186040530916), (1.0887806, 1.0887806, 1.0887806), "StaticMeshActor_17687", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (891.66644, 3865.2986, 3834.862), (-13.719604216584235, -59.55696951818801, -4.687347048865119), (1.0572144, 1.0572144, 1.0572144), "StaticMeshActor_17688", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (891.42303, 4144.89, 3891.995), (1.0040170216342454, -89.13619954023918, 4.203932809397246), (0.9922033, 0.9922033, 0.9922033), "StaticMeshActor_17689", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (596.9486, 3795.6663, 3968.9524), (6.297133675743878, 59.63011158558706, 4.3643171747203136), (0.90443194, 0.90443194, 0.90443194), "StaticMeshActor_17690", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (901.93463, 2471.8586, 3964.5107), (6.757529544059018, 118.9296078262216, 15.163624670797638), (0.8439355, 0.8439355, 0.8439355), "StaticMeshActor_17691", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (603.7023, 2606.951, 3962.1963), (-0.35247809049569245, -175.3144894212905, 7.209723157983093), (0.98799497, 0.98799497, 0.98799497), "StaticMeshActor_17692", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (6541.8633, 2466.2502, 715.88214), (-1.6893614631963363, -98.62342579902112, -3.7047731802614314), (0.91637886, 0.91637886, 0.91637886), "StaticMeshActor_17693", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (6220.328, 2411.2297, 770.24725), (-0.09298744862060514, 97.76848587018044, -6.024749014156104), (0.8810149, 0.8810149, 0.8810149), "StaticMeshActor_17694", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5191.4277, 3016.3706, 1674.5247), (1.9416888420958438, -76.51205447512586, -33.20217837659898), (0.81421834, 0.81421834, 0.81421834), "StaticMeshActor_17695", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5530.8203, 2803.6187, 1621.3838), (27.548156385165953, 175.84168059433887, 10.896954279222987), (1.0867326, 1.0867326, 1.0867326), "StaticMeshActor_17696", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5162.605, 4727.581, 3457.0012), (2.829283258814159, 91.24186542627871, 9.153815306419808), (0.87717736, 0.87717736, 0.87717736), "StaticMeshActor_17697", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2708.8044, 2606.4653, 2448.31), (27.30118982301038, 16.13697614181697, 5.705273533872889), (0.9558135, 0.9558135, 0.9558135), "StaticMeshActor_17698", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2471.7002, 2687.1155, 2487.0354), (36.842788307788375, 20.973652527501688, -1.5075373245862882), (0.8514581, 0.8514581, 0.8514581), "StaticMeshActor_17699", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1778.6962, 541.802, 2560.492), (-11.190640889482866, 179.76268470898953, 16.233354393250508), (1.0709411, 1.0709411, 1.0709411), "StaticMeshActor_17700", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1330.6019, 560.1997, 2567.2532), (12.810908594969858, 93.88040600518804, 22.14317128834712), (0.8969778, 0.8969778, 0.8969778), "StaticMeshActor_17701", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2595.6218, 542.22345, 2590.6294), (-10.70361281839069, -86.56393019654678, 3.6731922492528013), (0.8727459, 0.8727459, 0.8727459), "StaticMeshActor_17702", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2191.6687, 565.2616, 2586.6023), (0.7053944586926033, 175.54598431875618, 9.561043762888652), (0.8225203, 0.8225203, 0.8225203), "StaticMeshActor_17703", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4190.913, 4594.5986, 769.10425), (-3.1203910659115732, -94.13171301402711, 8.971876294280225), (0.8257332, 0.8257332, 0.8257332), "StaticMeshActor_17704", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2933.6047, 792.5641, 4872.3193), (22.62609254005515, -124.16816286928035, -3.8211981967954443), (0.9476904, 0.9476904, 1.3078244), "StaticMeshActor_17705", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3833.805, 762.7569, 4785.7393), (-4.594330117044007, 96.85429575265289, -6.1850578166443055), (0.90807116, 0.90807116, 0.90807116), "StaticMeshActor_17706", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (838.13574, 2503.9854, 4783.4214), (11.802634402258231, -160.39454675926632, -8.242004303599515), (1.093849, 1.093849, 1.093849), "StaticMeshActor_17707", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (870.7407, 2455.0417, 4317.594), (-10.320343385178159, 129.94736512626443, 1.4851619661857642), (0.89199173, 0.89199173, 0.89199173), "StaticMeshActor_17708", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (774.5398, 2909.6326, 4920.867), (6.728609167457301, 97.10245621310328, -33.247777012010864), (1.096414, 1.0045764, 1.0045764), "StaticMeshActor_17709", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2979.4917, 5574.525, 2469.3435), (18.630841579915153, 94.22594233544402, 6.036738260683799), (0.97575724, 0.97575724, 0.97575724), "StaticMeshActor_17710", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2599.7725, 5803.9683, 2361.2534), (-19.41854793321743, -153.5601676930467, 38.976689903630515), (1.0567393, 1.0567393, 1.0567393), "StaticMeshActor_17711", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2484.4172, 5875.2793, 2095.425), (24.779413379074224, 143.15844167134077, -6.029571683542421), (0.8877302, 0.8877302, 0.8877302), "StaticMeshActor_17712", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5078.7637, 3907.4265, 1638.2466), (1.8033872268553068, -87.55136024091122, -33.92764636841522), (0.95731425, 0.95731425, 0.95731425), "StaticMeshActor_17713", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4916.715, 3189.81, 1726.3265), (8.73495635876182, -135.7389379040696, -3.234222002289737), (1.0288789, 1.0288789, 1.0288789), "StaticMeshActor_17714", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (6197.7227, 3839.7253, 2649.0393), (-1.4284058040695773, -140.45230023360637, -10.176788474730007), (1.25, 1.25, 1.25), "StaticMeshActor_17715", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3998.726, 5372.082, 1575.9463), (5.290684363222026, 163.98891646843475, -4.095519762365192), (0.98667353, 0.98667353, 0.98667353), "StaticMeshActor_17716", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3924.4543, 6106.118, 1607.7751), (-6.494689389777033, -101.41214102627539, -7.634704544509249), (1.0, 1.0, 1.0), "StaticMeshActor_17717", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4058.856, 6210.2646, 1578.7504), (4.711785444283131, -8.986907247480726, 8.085057592058178), (0.82746613, 0.82746613, 0.82746613), "StaticMeshActor_17718", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3918.047, 6209.814, 954.24646), (-10.954681469999352, 117.41947021658872, 2.060832782784011), (0.8190751, 0.8190751, 0.8190751), "StaticMeshActor_17719", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3303.69, 3714.2932, 5280.6553), (0.6362922709704766, 110.40698222350882, -28.912135949373383), (1.0238879, 1.0238879, 1.0238879), "StaticMeshActor_17720", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4193.902, 4601.445, 1157.747), (-8.696960319889882, 3.0902422374003207, -1.0588379967242882), (0.9463351, 0.9463351, 0.9463351), "StaticMeshActor_17721", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4056.809, 4431.357, 1067.4792), (9.656307161429401, -173.31170756757754, 4.136223342320987), (1.0106162, 1.0106162, 1.0106162), "StaticMeshActor_17722", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4375.9614, 4519.332, 1395.8557), (7.417383370917295, 159.4082784170926, 19.526262742888115), (0.98222005, 0.98222005, 0.98222005), "StaticMeshActor_17723", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4606.9663, 4752.4307, 1109.9253), (9.001689046330654, -92.1494773850693, 1.7693385139889841), (1.0168709, 1.0168709, 1.0168709), "StaticMeshActor_17724", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (733.3115, 3373.9126, 5011.134), (8.091863458080338, 89.38074941296101, -46.52521060000642), (1.0776726, 1.0776726, 1.0776726), "StaticMeshActor_17725", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (741.76434, 3855.2812, 4814.761), (6.045959441405416, 160.7877095495932, -12.999967819000176), (1.0459605, 1.0459605, 1.0459605), "StaticMeshActor_17726", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (424.03815, 4009.3933, 4620.474), (-3.6338800324086646, 53.70960913396308, -19.578125920883924), (1.0546976, 1.0546976, 1.0546976), "StaticMeshActor_17727", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (502.78464, 3420.7222, 4871.957), (-0.5866077920182907, -95.16739262344841, -26.344360988880485), (1.0667443, 1.0667443, 1.0667443), "StaticMeshActor_17728", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5924.6934, 3841.2405, 3352.2883), (-4.702973144306758, 87.06127426357081, -30.481990697132588), (0.8372908, 0.8372908, 0.8372908), "StaticMeshActor_17729", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (6028.928, 3386.8467, 3229.2676), (-18.332394012642027, 8.492937893391385, -0.8523251740215599), (1.0332857, 1.0332857, 1.0332857), "StaticMeshActor_17730", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (6389.4985, 3802.5347, 3166.0493), (-23.24496030582604, -176.32344949931746, 6.519751702281826), (1.0950308, 1.0950308, 1.0950308), "StaticMeshActor_17731", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (6387.4746, 3390.2705, 3173.3237), (1.2078490471351657, 86.46828315896853, 33.47549109242545), (1.020674, 1.020674, 1.020674), "StaticMeshActor_17732", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (6124.1846, 3869.4656, 3112.1008), (-24.139862117129926, 139.8388242649984, 34.27513771055843), (1.0022799, 1.0022799, 1.0022799), "StaticMeshActor_17733", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (6198.3027, 4198.3853, 3156.1572), (-4.178008507988733, 123.13623058386614, 15.7323540885471), (0.9353733, 0.9353733, 0.9353733), "StaticMeshActor_17734", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2744.0264, 2993.8074, 2443.633), (1.9164383699921304, 80.45463443811576, 43.174861618252926), (0.87095803, 0.87095803, 0.87095803), "StaticMeshActor_17735", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2422.0195, 2957.5588, 2485.6162), (-22.49865862602086, 176.5733162473244, 3.1058416172771666), (0.8946198, 0.8946198, 0.8946198), "StaticMeshActor_17736", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2723.297, 3306.8916, 2419.7573), (31.18983809225776, -30.219294710755296, 2.243938390574888), (0.85096204, 0.85096204, 1.3267729), "StaticMeshActor_17737", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5990.232, 5681.261, 4765.545), (-6.564085909477187, 130.18479753442466, -5.176574282872367), (1.0090996, 1.0090996, 1.0090996), "StaticMeshActor_17738", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5988.157, 5677.05, 4394.3354), (0.10814244314062249, 24.95134732601715, 6.3019210576038045), (1.0623429, 1.0623429, 1.0623429), "StaticMeshActor_17739", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (6344.2563, 5855.354, 4897.914), (-22.01251057082611, -70.82506301313894, -5.2985533795737725), (1.034712, 1.034712, 1.034712), "StaticMeshActor_17740", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (6290.444, 5955.1436, 4537.7476), (7.725100903823684, 110.03138628326123, 4.373890982062675), (1.0166591, 1.0166591, 1.0166591), "StaticMeshActor_17741", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (6448.741, 5800.9795, 5550.981), (23.863594068612837, 117.42632010771258, 13.105716316522118), (0.9797226, 0.9797226, 0.9797226), "StaticMeshActor_17742", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (6405.1523, 5876.993, 5185.138), (-17.24108964263942, -57.11886809524642, -12.623537195361111), (0.920377, 0.920377, 0.920377), "StaticMeshActor_17743", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4059.5386, 4877.6753, 2804.395), (1.4614420547342852, 146.84522936467212, 8.508703985355393), (0.9988935, 0.9988935, 1.0671779), "StaticMeshActor_17744", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3631.618, 5511.0454, 2717.5693), (5.754270268798527, 152.25974186547177, -4.599335217688367), (1.0851166, 1.0851166, 1.0851166), "StaticMeshActor_17745", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4275.4907, 4850.948, 2785.913), (7.873561163060631, -120.5893586372575, -8.127348686943563), (0.9346119, 0.9346119, 0.9346119), "StaticMeshActor_17746", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4306.826, 5156.5234, 2762.9265), (6.739709788983146, 55.852813925271384, -2.5785826557640457), (0.802964, 0.802964, 0.802964), "StaticMeshActor_17747", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4195.3613, 5391.3086, 2753.801), (-9.700347778941318, -128.61287990167207, -5.933135569282936), (0.85785, 0.85785, 0.85785), "StaticMeshActor_17748", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5038.2505, 3290.8872, 1514.0021), (14.130406733807499, 19.89486957857239, -0.7294615471857842), (0.99898714, 0.99898714, 0.99898714), "StaticMeshActor_17749", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5078.8335, 1673.0106, 2912.9495), (-7.1334832688705365, -160.94498036629366, -13.52749530559875), (0.87033004, 0.87033004, 0.87033004), "StaticMeshActor_17750", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2731.5286, 3119.269, 3536.0396), (-5.3993831664142515, -46.35305066019704, 9.77018916200586), (0.8464119, 0.8464119, 0.8464119), "StaticMeshActor_17751", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2347.3025, 3211.5295, 3633.2576), (-6.911072164233523, -19.617859738197968, -36.120118758775234), (0.8335353, 0.8335353, 0.8335353), "StaticMeshActor_17752", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2593.6904, 3409.2803, 3560.445), (-3.631072550781506, 87.33760780269172, 23.315179988432888), (0.8652652, 0.8652652, 0.8652652), "StaticMeshActor_17753", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5942.726, 582.3556, 4826.446), (3.6734934141639592, 14.851524360078958, -1.2115170771253096), (0.8089201, 0.8089201, 0.8089201), "StaticMeshActor_17754", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5785.347, 595.5808, 5152.4463), (-8.417817033661766, 113.68235869667284, 1.761609175062224), (0.8840482, 0.8840482, 0.8840482), "StaticMeshActor_17755", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5468.0713, 466.99136, 5362.585), (-13.504119312871957, 10.248530817219567, -40.239254981691126), (0.892232, 0.892232, 0.892232), "StaticMeshActor_17756", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5861.972, 600.0487, 5324.9487), (2.504603037172296, 15.297054459618135, 19.070414092093007), (0.98077005, 0.98077005, 0.98077005), "StaticMeshActor_17757", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4445.6245, 4980.218, 1884.5562), (-6.436156179612372, 63.32690613097923, 2.9024959739646983), (0.8222792, 0.8222792, 1.2031782), "StaticMeshActor_17758", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5326.827, 5210.109, 5568.1543), (-9.088654160554437, 122.38517437718637, 6.359830800184483), (0.97046936, 0.97046936, 0.97046936), "StaticMeshActor_17759", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5441.2085, 5225.1514, 4955.669), (-6.2060861044845295, -82.58787051932669, 6.820809034964663), (1.0545658, 1.0545658, 1.0545658), "StaticMeshActor_17760", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3267.815, 3573.493, 4848.809), (-5.729643400350311, 141.403037335996, -9.694181048687394), (0.989911, 0.989911, 0.989911), "StaticMeshActor_17761", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3305.2217, 3490.327, 4762.7974), (4.086188584750056, 99.81465095262286, -14.383145914036687), (0.85422117, 0.85422117, 0.85422117), "StaticMeshActor_17762", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3315.6492, 3319.1514, 4372.9536), (9.068421534280207, -74.97564943824142, -0.274658363169321), (1.0054209, 1.0054209, 1.0054209), "StaticMeshActor_17763", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1409.6721, 1596.7043, 4611.2397), (-7.932739518390969, -8.488678114007877, 6.856126567609781), (1.0001535, 1.0001535, 1.0001535), "StaticMeshActor_17764", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1268.8677, 1815.1467, 4755.1846), (8.764614971616165, 5.544884725102214, 6.81355939882344), (0.815894, 0.815894, 0.815894), "StaticMeshActor_17765", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1347.7738, 876.3151, 4247.3057), (6.9874741175475545, -159.5374159274343, 0.40317010220716515), (1.0181218, 1.0181218, 1.0181218), "StaticMeshActor_17766", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1528.65, 1132.2207, 4192.585), (5.506634953434256, -123.5781249363406, -81.06870271255956), (0.9421792, 0.9421792, 0.9421792), "StaticMeshActor_17767", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1895.7195, 438.389, 4805.313), (21.644833289906877, 65.86138839547338, -4.215270451901359), (1.0, 1.0, 1.224433), "StaticMeshActor_17768", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2190.116, 610.2355, 4749.8413), (0.8925892198319566, -43.916867709751756, 8.974236413114312), (0.8975981, 0.8975981, 0.8975981), "StaticMeshActor_17769", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5397.2188, 601.71594, 5562.102), (-15.991793953622139, -1.4080202796706198, -32.336334451045985), (1.0615816, 1.0615816, 1.0615816), "StaticMeshActor_17770", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5398.752, 840.65454, 5710.0376), (46.82399455207712, 97.20293151396356, 8.36433137754791), (0.8192149, 0.8192149, 0.8192149), "StaticMeshActor_17771", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4978.8545, 71.53706, 5241.8813), (-33.38110997309908, 85.20235931907902, 10.88151463210244), (1.0436499, 1.0436499, 1.0436499), "StaticMeshActor_17772", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5242.055, 4048.222, 1275.497), (-19.90832194414068, -144.4805840269905, -11.621856394145528), (0.9133669, 0.9133669, 0.9133669), "StaticMeshActor_17773", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5092.635, 4361.897, 1152.7158), (-10.016021069092814, -122.4676380055816, -4.599609031398819), (0.8483401, 0.8483401, 0.8483401), "StaticMeshActor_17774", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5151.3296, 5430.1562, 5752.388), (-4.493835953780918, 97.27261566828675, -46.11986965487225), (0.98100466, 0.98100466, 0.98100466), "StaticMeshActor_17775", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4987.107, 5392.4146, 5950.758), (18.541360234984257, 176.83825912166205, -22.178618595499024), (0.98612523, 0.98612523, 0.98612523), "StaticMeshActor_17776", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4655.2383, 5419.335, 6075.0405), (-4.349852002284997, 99.02309944094894, -10.191771606574592), (0.99780846, 0.99780846, 0.99780846), "StaticMeshActor_17777", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5007.354, 5008.2236, 6067.9004), (16.51517945331398, -91.82464333030153, 13.839439828967492), (1.0063401, 1.0063401, 1.0063401), "StaticMeshActor_17778", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5042.633, 4648.2534, 6091.5522), (17.73998403270449, 170.46631587749692, -9.053101603999378), (1.008877, 1.008877, 1.008877), "StaticMeshActor_17779", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (724.2773, 3883.0547, 4361.9106), (-6.361266653011418, -23.149595906045217, 9.318322418941861), (0.8569754, 0.8569754, 0.8569754), "StaticMeshActor_17780", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (519.8868, 3896.188, 4302.108), (-15.011992305763021, 136.78940293424256, 7.794266786565352), (0.81521255, 0.81521255, 0.81521255), "StaticMeshActor_17781", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1387.1572, 5561.8237, 2510.9343), (-29.822264532182594, -87.10446252399545, 0.7056974945306808), (0.9729162, 0.9729162, 0.9729162), "StaticMeshActor_17782", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1156.6927, 5338.234, 2712.4624), (-26.441529466376778, 81.81878548967723, 20.255102842907686), (0.8159545, 0.8159545, 0.8159545), "StaticMeshActor_17783", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (193.68596, 5073.394, 2616.4028), (-6.098144247200645, 87.07091240081486, 12.127769636994644), (0.8855373, 0.8855373, 0.8855373), "StaticMeshActor_17784", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (219.81816, 5551.723, 2487.9783), (-4.732330439779099, -14.402617693273179, -34.62042328096216), (1.0339149, 1.0339149, 1.0339149), "StaticMeshActor_17785", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (180.50449, 4599.3, 2559.268), (-1.2013244721759564, 3.1163816511946467, -8.33148113415003), (1.072578, 1.072578, 1.072578), "StaticMeshActor_17786", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (722.5491, 4626.116, 2675.6277), (2.9140103511212687, 84.49136739601487, 35.44598361080643), (0.93015134, 0.93015134, 0.93015134), "StaticMeshActor_17787", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (462.48813, 4620.7573, 2513.0312), (-27.50643524588922, 172.00797087932813, -1.3731688913492675), (0.8208452, 0.8208452, 0.8208452), "StaticMeshActor_17788", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (693.4677, 4198.954, 2680.2175), (-9.41366542733719, 178.91557528466464, -5.074738223930944), (0.8639068, 1.1239431, 0.8639068), "StaticMeshActor_17789", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (498.7908, 4209.0293, 2594.4363), (2.6709172225900892, -80.19886178985615, -19.66696155850935), (0.8342791, 0.8342791, 0.8342791), "StaticMeshActor_17790", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (177.6801, 4191.285, 2565.7778), (7.75056947587749, 80.65853266388721, 7.670966634859577), (1.0288422, 1.0288422, 1.0288422), "StaticMeshActor_17791", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (487.59552, 3796.8008, 2569.5408), (32.90716311237811, -8.520660486393592, -9.484984932840108), (0.9707071, 0.9707071, 0.9707071), "StaticMeshActor_17792", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (530.35547, 2991.3882, 2556.9963), (3.483041639026469, 175.90362409562226, -7.8926406119738), (0.89108634, 1.3487468, 0.89108634), "StaticMeshActor_17793", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (657.49567, 3784.4233, 2654.1355), (-28.64901534948797, 6.348206315087063, -4.917419352627322), (0.9577392, 0.9577392, 0.9577392), "StaticMeshActor_17794", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (492.35165, 3396.0356, 2559.5132), (-5.402008336744629, -97.48917888200837, -12.033326337927306), (1.0762275, 1.0762275, 1.0762275), "StaticMeshActor_17795", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (600.55927, 2570.2158, 2545.079), (-1.125609936971606, 87.63237176325717, -8.43518001131881), (1.0905426, 0.8586911, 0.8586911), "StaticMeshActor_17796", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (507.01614, 2183.415, 2551.743), (4.326024265055574, 100.37431347622024, 105.73386208632225), (0.8779861, 0.8779861, 0.8779861), "StaticMeshActor_17797", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (524.2288, 1699.3362, 2494.7842), (-11.74975565205351, -84.79420899971144, -14.849337382201936), (0.8695915, 0.8695915, 0.65583664), "StaticMeshActor_17798", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (240.81407, 1410.4956, 2476.4133), (-6.862487610004967, -98.77087237614838, 4.889780447992718), (1.3165021, 1.2571487, 0.8418323), "StaticMeshActor_17799", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (-72.94585, 1169.2963, 2726.182), (0.4137933215882705, 6.351975575000635, -19.29257118121922), (1.0456766, 1.0456766, 1.0456766), "StaticMeshActor_17800", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (249.79906, 886.50745, 2456.316), (35.22317130966969, -64.11390109670651, 16.346494540039306), (0.8397055, 0.8397055, 0.8397055), "StaticMeshActor_17801", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (-121.8718, 768.9423, 2499.2468), (-0.5579222184529063, -173.03966224427808, -23.200799524327728), (0.9219246, 0.9219246, 0.9219246), "StaticMeshActor_17802", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (956.0107, 1335.6176, 2818.335), (24.968065256595885, 85.56511413929252, 33.87530242519163), (0.9123758, 0.9123758, 0.9123758), "StaticMeshActor_17803", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (904.14417, 600.90405, 2444.4233), (-0.13772810552689133, -86.1415191427427, 42.9565320599383), (0.81579244, 0.81579244, 0.81579244), "StaticMeshActor_17804", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (852.24115, 222.00806, 2472.2036), (0.923425521548781, -103.30803745845753, 30.417967110370725), (1.0113173, 1.0113173, 1.0113173), "StaticMeshActor_17805", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1327.5233, 201.88388, 2608.9065), (-0.22076403226641003, 98.92418554540433, 4.114169027150978), (1.0137476, 1.0137476, 1.0137476), "StaticMeshActor_17806", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1787.5867, 186.89786, 2583.6465), (-2.8535155427381875, 8.178024462182329, 8.017853349555612), (0.8376508, 0.8376508, 0.8376508), "StaticMeshActor_17807", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2197.4727, 194.5473, 2585.7556), (3.2749049995940513, 81.775636077945, 2.534797285471996), (1.028069, 1.028069, 1.028069), "StaticMeshActor_17808", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2606.7551, 200.40295, 2591.287), (-5.838896972721716, -81.8768243762572, 3.10351774375542), (1.0313277, 1.0313277, 1.0313277), "StaticMeshActor_17809", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4200.9526, 543.42914, 2563.6536), (8.388523638449572, 176.9369372012811, 15.665816291589717), (0.91828924, 0.91828924, 0.91828924), "StaticMeshActor_17810", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3808.3699, 553.2956, 2586.331), (12.134807021669472, 99.7258143353996, -9.603850149768562), (0.9986574, 0.9986574, 0.9986574), "StaticMeshActor_17811", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4624.253, 556.8103, 2567.786), (-10.720275513552531, -3.7143246556728373, -13.676392111532847), (0.92919886, 0.92919886, 0.92919886), "StaticMeshActor_17812", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4207.0713, 192.23965, 2581.9485), (0.5106999801275958, -96.55382751025022, 4.408317588527315), (0.9292913, 0.9292913, 0.9292913), "StaticMeshActor_17813", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3791.1875, 179.05296, 2583.9065), (-11.128693366304846, -80.39166574207904, 8.509504474878991), (0.9239334, 0.9239334, 0.9239334), "StaticMeshActor_17814", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4684.5684, 200.2005, 2647.5369), (-6.274108022713629, -81.19346821455656, 9.124752278969927), (0.8988819, 0.8988819, 0.8988819), "StaticMeshActor_17815", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5106.0757, 597.50464, 2575.8037), (8.104461764338252, 78.95887766770777, -24.82626447863852), (0.98551595, 0.98551595, 0.98551595), "StaticMeshActor_17816", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5109.29, 201.87885, 2563.3513), (-2.7667542845695916, 81.02364915692884, -18.276274562648627), (1.0903225, 1.0903225, 1.0903225), "StaticMeshActor_17817", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5511.6445, 603.5624, 2467.8481), (-9.717191660299804, 87.68748079191656, -22.74520731930503), (0.9616958, 0.9616958, 0.9616958), "StaticMeshActor_17818", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5786.7876, 195.49303, 2365.0737), (-1.2302264060495995, -80.10587138726981, -23.679261774422418), (0.88437986, 0.88437986, 0.88437986), "StaticMeshActor_17819", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5539.8003, 211.06308, 2476.9883), (-39.88979129071195, 178.68607478463568, 7.258231950358585), (0.8736222, 0.8736222, 0.8736222), "StaticMeshActor_17820", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (784.63763, 1724.6521, 2718.9443), (-5.580231135434938, -97.5757797012773, -34.39733771741268), (0.82541114, 0.82541114, 0.82541114), "StaticMeshActor_17821", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (695.4973, 2099.9675, 2676.3943), (-17.176301374876743, -90.68859385410093, -42.95129232262033), (0.9141901, 0.9141901, 0.9141901), "StaticMeshActor_17822", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3792.6958, 599.42957, 4351.865), (8.501085117926191, 30.765751423666906, 11.631828786035163), (0.8517579, 0.8517579, 0.8517579), "StaticMeshActor_17823", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (915.6008, 699.4851, 5481.6655), (-12.249755972604307, 134.41671773795173, -39.81869512939973), (0.964648, 0.964648, 0.964648), "StaticMeshActor_17824", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (871.739, 584.9239, 5098.482), (-14.459503974440313, 55.529407458822035, -20.03860676988249), (0.85803473, 0.85803473, 0.85803473), "StaticMeshActor_17825", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4212.762, 933.5932, 2875.6675), (4.946620416439359, 173.7523551673729, 15.687420398661603), (1.0970447, 1.0970447, 1.0970447), "StaticMeshActor_17826", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3801.2131, 935.93475, 2901.7747), (-18.58374487413556, -80.75036840592654, 10.206713593663762), (0.84378135, 0.84378135, 0.84378135), "StaticMeshActor_17827", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3393.041, 608.4976, 2750.7937), (-30.5521273887226, -90.15448453501914, 7.49875562511137), (0.9838531, 0.9838531, 0.9838531), "StaticMeshActor_17828", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3405.5237, 923.1259, 2903.263), (15.598355143841, -179.97724111506534, 29.478657485471526), (1.0964271, 1.0964271, 1.0964271), "StaticMeshActor_17829", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2991.226, 608.348, 2758.402), (-37.27954263734061, -83.14126819544335, 6.280087210408003), (0.82009625, 0.82009625, 0.82009625), "StaticMeshActor_17830", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3014.422, 912.2192, 2884.7607), (15.404622772947683, -170.44801747606942, 29.379419688348612), (0.8181007, 0.8181007, 0.8181007), "StaticMeshActor_17831", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1640.0397, 1190.519, 3606.1387), (9.533563985892984, -21.79632596905725, 13.55763195188892), (1.0059396, 1.0059396, 1.0059396), "StaticMeshActor_17832", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1916.6782, 1091.1116, 3636.3767), (15.329744224721589, -96.88438710021376, -8.733762604978857), (0.8402241, 0.8402241, 0.8402241), "StaticMeshActor_17833", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1812.9154, 1237.7009, 3973.265), (-2.3262328456853627, -124.58957925172129, 0.14665416401146603), (1.0758407, 1.0758407, 1.0758407), "StaticMeshActor_17834", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3779.7842, 819.6363, 3524.7234), (-7.657957640524525, 174.14098902077112, 3.324554651205316), (0.9496032, 0.842873, 0.842873), "StaticMeshActor_17835", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4196.8564, 763.7286, 3868.499), (0.39160229434786414, 2.281067049668065, 10.432476670486341), (0.8173038, 0.8173038, 0.9067624), "StaticMeshActor_17836", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4208.851, 822.64594, 3462.036), (8.594603948869597, -93.1409249536858, -2.6258237512479), (0.93021876, 0.93021876, 0.93021876), "StaticMeshActor_17837", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4095.0132, 783.0561, 4277.103), (1.471454543690445, -89.96455378606491, 3.4065419105181904), (0.93303907, 0.93303907, 0.93303907), "StaticMeshActor_17838", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5877.8604, 697.8589, 4197.812), (2.1659755450030906, 5.838468216452838, 4.8426478499026855), (0.8731891, 0.8731891, 0.8731891), "StaticMeshActor_17839", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (6205.532, 506.68243, 4291.833), (-4.5206902695738735, 4.072917116153186, 0.13514800485668782), (0.8634018, 0.8634018, 0.8634018), "StaticMeshActor_17840", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (6193.751, 474.12677, 4764.247), (-3.1278689304707425, 36.50824514687686, 3.790347506607894), (1.5146377, 1.5146377, 1.5146377), "StaticMeshActor_17841", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (6506.7485, 614.5501, 4750.0283), (-5.775663767111375, -173.80800730942272, 4.362946265566299), (0.86608034, 0.86608034, 0.86608034), "StaticMeshActor_17842", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (6511.668, 607.61316, 4359.3096), (-8.3917237681807, 101.55700568736583, 9.55255149935769), (0.91337526, 0.91337526, 0.91337526), "StaticMeshActor_17843", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (6534.811, 595.45435, 5555.7285), (1.5777393021468924, -84.01684185603389, 8.988733649986123), (0.9266864, 0.9266864, 0.9266864), "StaticMeshActor_17844", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (6192.3516, 606.89215, 5551.365), (-6.443268157444358, 105.55620419574473, -1.0004578103249286), (0.9589764, 0.9589764, 0.9589764), "StaticMeshActor_17845", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (6550.164, 603.8782, 5158.027), (-0.457397484654834, -91.75311737127552, 1.7275288567807965), (1.0468557, 1.0468557, 1.0468557), "StaticMeshActor_17846", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (6192.9336, 611.5587, 5155.8545), (1.891914404808063, -88.23500241935388, -4.744475702662535), (1.0358303, 1.0358303, 1.0358303), "StaticMeshActor_17847", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (6560.552, 845.7833, 5657.807), (30.168458128245895, -78.4085132658175, 10.39908687405393), (0.824664, 0.824664, 0.824664), "StaticMeshActor_17848", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (6203.9565, 838.5045, 5695.08), (-36.32016624072185, -89.04621267419971, -5.386536178558769), (1.0138348, 1.0138348, 1.0138348), "StaticMeshActor_17849", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5819.981, 833.457, 5701.118), (4.0397089604184755, -177.76275301593049, 37.21286740768101), (0.9282324, 0.9282324, 0.9282324), "StaticMeshActor_17850", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4988.071, 877.3511, 5688.698), (28.35895208495567, 99.42613658944181, 10.55433806267019), (0.8037498, 0.8037498, 0.8037498), "StaticMeshActor_17851", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4960.6763, 770.47296, 5504.646), (-7.147400059635622, 169.0177039598855, 44.7671382464049), (1.0189359, 1.0189359, 1.0189359), "StaticMeshActor_17852", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4600.868, 864.1242, 5691.2593), (49.70005617150044, 97.1742563420039, 5.738270438664621), (1.0575047, 1.0575047, 1.0575047), "StaticMeshActor_17853", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4016.2764, 770.3048, 4756.3438), (1.5347161251109191, -127.46346093305742, 2.7001562024868537), (1.0016196, 1.0016196, 1.0016196), "StaticMeshActor_17854", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3369.4858, 734.53613, 4909.078), (-6.304138075025861, 176.08656477504334, -31.335570966806483), (1.0225949, 1.0225949, 1.0225949), "StaticMeshActor_17855", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3378.4316, 859.68634, 5673.257), (11.343085698558045, -4.8406675052754595, 27.184527859464783), (0.83325934, 0.83325934, 0.83325934), "StaticMeshActor_17856", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3393.486, 803.5368, 5237.6797), (-1.524017337488006, -6.748077956296856, 20.44734047366011), (1.0519631, 1.0519631, 1.0519631), "StaticMeshActor_17857", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2938.4058, 845.1777, 5680.446), (-19.85491970730832, 66.42341009433183, 2.5126256530856668), (0.95181406, 0.95181406, 0.95181406), "StaticMeshActor_17858", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2788.01, 2382.537, 2764.156), (4.792333049374475, 126.62382449716418, -5.652556458138573), (1.1095016, 1.0469507, 1.2452923), "StaticMeshActor_17860", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2489.156, 2947.7642, 3597.3228), (19.406013869737688, 134.79814531147514, -2.0790113921442455), (1.0748079, 1.0748079, 1.0748079), "StaticMeshActor_17861", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2523.1384, 3091.082, 2429.5818), (-11.63799872509575, -123.30073610804597, -20.491573852827052), (0.80430293, 0.80430293, 0.80430293), "StaticMeshActor_17862", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3430.5947, 2858.409, 2324.1426), (-17.051881900643853, 59.544602447228634, -9.711762959855957), (1.0784676, 1.0784676, 1.0784676), "StaticMeshActor_17863", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2974.604, 2282.3267, 1373.9304), (3.451471703148876, -93.21037958196678, -5.183501620859273), (0.8924974, 0.8924974, 0.8924974), "StaticMeshActor_17864", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3011.8188, 2270.38, 1062.7065), (6.856675706674367, 2.3902621912714017, -3.8999939664345464), (1.0107535, 1.0107535, 1.0107535), "StaticMeshActor_17865", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2932.9204, 2646.6548, 2063.7231), (6.310370453732355, 9.175952116480444, 6.298506092778007), (0.82387125, 0.82387125, 0.82387125), "StaticMeshActor_17866", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2945.8772, 2992.6914, 2121.937), (29.6525562634915, -3.700805125259482, 0.3045902851603169), (0.9860585, 0.9860585, 0.9860585), "StaticMeshActor_17867", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2944.9724, 3061.1345, 1071.398), (1.7813364379522316, 0.5470581133861309, 5.860818560609568), (0.827463, 0.827463, 0.827463), "StaticMeshActor_17868", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3119.933, 3011.5264, 1609.8408), (-8.663025701756691, 109.29356392730969, -7.008026567135553), (1.083677, 1.083677, 1.083677), "StaticMeshActor_17869", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2754.715, 3553.7312, 4394.7593), (6.145714704265366, -45.478240370336465, 6.458224573512572), (0.85595304, 0.85595304, 0.85595304), "StaticMeshActor_17870", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2694.4832, 3336.8386, 4322.9487), (8.164110672091658, 79.605699651941, -18.37573078475614), (1.09441, 1.09441, 1.09441), "StaticMeshActor_17871", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2721.295, 3469.5288, 4765.7866), (-0.9624325532848516, -89.29503317973337, -2.988739042040578), (1.0825375, 1.0825375, 1.0825375), "StaticMeshActor_17872", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2692.4817, 3489.3284, 5240.8374), (-0.6029359042150378, -67.10363345862443, -26.15084922738534), (0.9068716, 0.9068716, 0.9068716), "StaticMeshActor_17873", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2705.9268, 3586.0205, 4863.0215), (28.36360968629997, -47.01855571850473, -2.7606207679400576), (0.80568767, 0.80568767, 0.80568767), "StaticMeshActor_17874", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2655.1611, 3408.4834, 5780.0596), (19.130984323895188, -87.3277986852664, 38.096614145546305), (0.95146906, 0.95146906, 0.95146906), "StaticMeshActor_17875", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2692.3188, 3746.0688, 5283.006), (34.91628883558348, -33.02578837241961, -17.213989152648296), (0.9702655, 0.9702655, 0.9702655), "StaticMeshActor_17876", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2396.1375, 3420.5754, 5780.3096), (6.465143349475715, -98.52786342657409, 34.16493882069243), (0.92887723, 0.92887723, 0.92887723), "StaticMeshActor_17877", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2589.9329, 3796.2073, 5556.231), (25.297851066610104, 5.248253499937779, 1.9302841696830464), (1.1202178, 0.9534874, 0.9534874), "StaticMeshActor_17878", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2405.3247, 3791.8076, 5726.3516), (-39.46550343655007, -173.09081725632547, 5.779562798617671), (0.9591645, 0.9591645, 0.9591645), "StaticMeshActor_17879", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2203.8662, 3792.1782, 5949.802), (-22.157776592848283, 7.104926356664298, 1.200348232676539), (0.94356036, 0.94356036, 0.94356036), "StaticMeshActor_17880", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (6448.649, 3939.2593, 1175.3574), (8.716598767054881, 82.36494042732468, -10.032593718408583), (0.86468124, 0.86468124, 0.86468124), "StaticMeshActor_17881", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (6204.394, 3913.7893, 1213.7382), (-1.3170167844098641, -0.9917298262044558, -31.95059285596156), (0.9916632, 0.9916632, 0.9916632), "StaticMeshActor_17882", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5859.896, 3912.1338, 1266.1647), (39.26355312950026, 71.27177761132513, 4.615247912139304), (1.0779984, 1.0779984, 1.0779984), "StaticMeshActor_17883", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5528.258, 3954.8928, 1365.791), (-24.301418899694855, -7.3716418744754995, 36.10961618040023), (1.0062556, 1.0062556, 1.0062556), "StaticMeshActor_17884", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5396.38, 3792.259, 1550.9843), (18.70825111087947, -82.6003224662895, 18.27151488979735), (0.8963623, 0.8963623, 0.8963623), "StaticMeshActor_17885", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3507.7285, 5551.703, 2433.001), (28.4490506135846, 65.18325146757653, 4.304848255521343), (0.8446179, 0.8446179, 0.8446179), "StaticMeshActor_17886", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3289.3533, 5559.9907, 3458.0762), (-1.7507323837158209, 142.3025473607133, 6.996199208934688), (0.93952286, 0.93952286, 0.97976446), "StaticMeshActor_17887", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2996.6155, 5581.5054, 3457.335), (-5.480803699620779, -6.108612455654271, -1.4591674663127598), (0.91858673, 0.91858673, 0.91858673), "StaticMeshActor_17888", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2566.925, 5560.3384, 3510.4014), (1.0414467856937515, -82.18341596569931, -3.6760252617354094), (0.9040322, 0.8548282, 1.0599761), "StaticMeshActor_17889", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2189.1284, 5498.6772, 3537.0093), (4.272700821395534, 113.59968426062706, -2.096283049098182), (1.0791239, 1.0791239, 1.0791239), "StaticMeshActor_17890", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1793.3793, 5394.5884, 3561.7969), (3.412956143543347, -4.550231613009716, -3.656982386582044), (1.0192187, 1.0192187, 1.0192187), "StaticMeshActor_17891", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1731.8761, 5264.126, 3458.1538), (5.843622226087543, 7.838734297196337, 5.147278275509896), (1.0676337, 1.0676337, 1.0676337), "StaticMeshActor_17892", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1482.1921, 5254.0957, 3787.149), (5.461084498266931, -172.08325202882966, 0.8044274077543787), (0.94948024, 0.94948024, 0.94948024), "StaticMeshActor_17893", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2154.7153, 5508.195, 1557.5446), (5.0116916151645725, 102.54931809108119, 0.8065603172671344), (0.9996333, 0.9996333, 0.9996333), "StaticMeshActor_17894", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1850.2554, 5500.751, 2341.4365), (-25.22723153609762, -115.60229097255126, 1.9912363818476988), (0.81753695, 0.94139373, 0.88144624), "StaticMeshActor_17895", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1953.7158, 5553.864, 1966.9702), (-12.508422077638318, -126.03520894416769, 0.7031375039215264), (1.0515356, 1.0515356, 1.0515356), "StaticMeshActor_17896", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (273.08212, 5847.1616, 1658.3112), (-4.1479799623871205, -5.530761679537723, -14.577150193269057), (0.8893877, 0.8893877, 0.8893877), "StaticMeshActor_17897", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (226.55571, 6025.29, 1585.0039), (6.269614978344145, -12.824797701626018, -8.49481240095993), (0.94921106, 0.94921106, 0.94921106), "StaticMeshActor_17898", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (315.7416, 5779.9663, 1013.0128), (0.20187972346302513, -94.66284663504445, -8.224578885082613), (1.0902368, 1.0902368, 1.0902368), "StaticMeshActor_17899", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (189.66283, 5787.3296, 1160.5682), (-9.686920497547467, 95.81621828507463, -8.639251589500189), (1.0796304, 0.9549313, 0.9549313), "StaticMeshActor_17900", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (259.71036, 5761.602, 2136.639), (7.171396656892898, -176.33760272968678, 17.559536541018844), (0.878784, 0.878784, 0.878784), "StaticMeshActor_17901", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5372.485, 2580.3372, 1565.864), (8.26707525441195, -5.329345201089647, -6.3130486084738155), (1.0905589, 1.0905589, 1.0905589), "StaticMeshActor_17902", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5365.1787, 2509.6208, 1131.2216), (-3.2027284493486903, 168.16348131569316, -2.131073354577775), (0.97805846, 0.97805846, 0.97805846), "StaticMeshActor_17903", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5390.954, 2611.9597, 1548.744), (21.29320060786473, -62.84344609451529, 13.511904117733563), (0.8260599, 0.8260599, 0.8260599), "StaticMeshActor_17904", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5818.373, 2435.6553, 1241.3312), (-1.2709045027361017, 12.971166224636235, 22.905607682862726), (0.95563406, 0.95563406, 0.95563406), "StaticMeshActor_17905", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (6221.187, 2482.0403, 1228.4193), (3.4827050169525267, -168.0992155415467, -36.10436048787548), (0.89840776, 0.89840776, 0.89840776), "StaticMeshActor_17906", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (6455.572, 2463.1702, 1181.92), (-5.477020658871392, 177.38738355495357, -15.961672926558691), (1.0848516, 1.0848516, 1.0848516), "StaticMeshActor_17907", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (598.79736, 2610.3599, 4354.0215), (-9.951476309237046, -114.50951103490854, -1.4491272446080334), (0.9804741, 0.9804741, 0.9804741), "StaticMeshActor_17908", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (604.9578, 2601.7979, 4750.822), (-23.750180153937933, 53.67455250413191, 7.958910248228412), (1.0659041, 1.0659041, 1.0659041), "StaticMeshActor_17909", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (998.07324, 313.32825, 4864.921), (20.233688054022647, -141.42954887988068, 21.114580338852203), (1.0075868, 1.0075868, 1.0075868), "StaticMeshActor_17910", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5789.213, 208.34859, 5161.726), (-14.189116616548583, -127.27203345683843, -19.738034893803967), (1.0861449, 1.0861449, 1.0861449), "StaticMeshActor_17911", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1797.8755, 604.49585, 4364.3936), (-4.674499123521883, 86.65150203614276, 2.8160970315676037), (0.9603039, 0.9603039, 0.9603039), "StaticMeshActor_17912", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1532.2734, 229.98288, 4738.4746), (-6.152435511215709, 26.72755541467416, -17.57748428566866), (1.0338826, 1.0338826, 1.0338826), "StaticMeshActor_17913", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1790.9238, 207.03163, 4751.217), (1.1127741834302025, 113.89876715932921, 4.814692683396155), (1.0440137, 1.0440137, 1.0440137), "StaticMeshActor_17914", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1404.0569, 68.85989, 4848.2754), (-6.707306207005719, -177.2963742036462, 5.284045997688607), (1.0659941, 1.0659941, 1.0659941), "StaticMeshActor_17915", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2711.5, 3570.48, 3604.017), (-8.70471272053052, 30.01881325020652, 12.098383197936343), (1.0288177, 1.0288177, 1.0288177), "StaticMeshActor_17916", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3011.5947, 3674.6743, 3591.912), (7.310379382976086, -177.82397643269414, -15.414125909151284), (1.014838, 1.014838, 1.014838), "StaticMeshActor_17917", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2999.7192, 3593.2744, 3229.34), (-1.5976563153275103, 9.031079158730433, 15.747863015956561), (0.9671339, 0.9671339, 0.9671339), "StaticMeshActor_17918", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4073.7896, 495.65442, 4297.595), (-6.477019260401848, 85.92926423183978, 2.4896569871149916), (0.8900898, 0.8900898, 0.8900898), "StaticMeshActor_17919", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4208.5454, 200.36595, 4363.083), (8.437876459669678, -170.9067693800343, 6.807956238727819), (0.9167255, 0.9167255, 0.9167255), "StaticMeshActor_17920", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4860.7334, 4900.136, 3333.488), (-6.563903503934661, -88.46978235774006, 0.5256164878042625), (1.0288963, 1.0288963, 1.0288963), "StaticMeshActor_17921", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5136.8267, 4246.897, 3367.676), (1.6901186893346488e-07, 117.9108499557681, 15.00117355927751), (1.0868411, 1.0656532, 1.0868411), "StaticMeshActor_17922", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (864.9904, 4595.175, 5708.0835), (-47.896021997370006, -177.69054305871958, 1.8742400620027595), (1.0022128, 1.0022128, 1.0022128), "StaticMeshActor_17924", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (878.79254, 4193.6094, 5681.945), (6.182890421300447, -82.5362473720646, 29.102426910493417), (0.95842737, 0.95842737, 0.95842737), "StaticMeshActor_17925", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (881.88727, 3784.454, 5693.111), (-48.78173737512987, 8.859850742942504, -9.939452848972822), (1.0056484, 1.1379231, 1.1379231), "StaticMeshActor_17926", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (881.55286, 3399.8184, 5685.368), (-9.494202349609, 87.57336213634032, -35.26516638892603), (1.0711251, 1.0711251, 1.0711251), "StaticMeshActor_17927", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1367.2129, 3799.1494, 6103.411), (-6.8847351040103115, -174.99271847705214, -7.687316980817407), (1.0627546, 1.0627546, 1.0627546), "StaticMeshActor_17928", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1284.9286, 2963.7761, 6075.9805), (19.33162098776069, 88.75152144629674, 10.576626725486179), (0.81105405, 0.81105405, 0.81105405), "StaticMeshActor_17929", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (992.25323, 5807.542, 2352.6116), (-24.12613064009834, 89.84454728676312, 23.489544688766166), (0.9206345, 0.9206345, 0.9206345), "StaticMeshActor_17930", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (844.43945, 5918.302, 2067.557), (19.503126229383135, 146.40263216271194, -13.340667516404734), (0.881996, 0.881996, 0.881996), "StaticMeshActor_17931", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (960.361, 6295.164, 1959.844), (12.326039186075118, 43.60043459800098, -19.55041402355774), (1.0791471, 1.0791471, 1.0791471), "StaticMeshActor_17932", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2983.9438, 3694.7078, 5281.12), (29.24947246471315, 101.30058810527422, 17.75807899541474), (1.040083, 1.040083, 1.040083), "StaticMeshActor_17933", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3334.8782, 2649.4607, 2856.461), (-11.403931826251881, 71.36421921600974, -40.75912609719484), (1.0725007, 1.0725007, 1.0725007), "StaticMeshActor_17938", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3001.8687, 2324.5938, 2820.2698), (-28.76046675200291, -88.77144780746934, -8.02758851202774), (0.80038023, 0.80038023, 0.80038023), "StaticMeshActor_17939", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5784.8857, 6206.3555, 4754.7144), (-4.197907325920784, 68.67309941330043, 11.420972339926072), (1.08325, 1.08325, 1.08325), "StaticMeshActor_17940", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5744.0454, 6037.618, 4768.086), (3.683315714300604, -14.638180392344273, 4.850313364701434), (0.8589376, 0.8589376, 0.8589376), "StaticMeshActor_17941", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5927.728, 6140.911, 4397.992), (-10.304932472739443, -111.49750442989476, -13.57260094592031), (1.0693941, 1.0693941, 1.0693941), "StaticMeshActor_17942", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5751.557, 6049.597, 4389.502), (-3.9153145818692496, -26.207672972504696, 2.913948463185834), (1.0280259, 1.0280259, 1.0280259), "StaticMeshActor_17943", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5571.6177, 5733.9497, 4720.352), (15.219364810248722, 153.35864108111258, -4.306456292685547), (0.9889373, 0.9889373, 0.9889373), "StaticMeshActor_17944", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5357.428, 5444.438, 5108.612), (-1.0195006796085164, -170.28873920084428, 3.073605979306302), (1.016957, 1.016957, 1.016957), "StaticMeshActor_17945", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2983.5217, 3280.7798, 2390.29), (7.915101959575632, -92.36388846151458, -0.8569640159375239), (1.089047, 1.089047, 1.089047), "StaticMeshActor_17946", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3200.2378, 3168.2256, 2090.2334), (-10.416289014168012, 143.07536830462257, -23.822136938498105), (1.0844795, 1.0844795, 1.0844795), "StaticMeshActor_17947", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3274.8486, 3221.351, 2409.6057), (-12.69158935267458, 56.75304613548144, 0.6607539639869746), (0.8821548, 0.8821548, 0.8821548), "StaticMeshActor_17948", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3019.8816, 3444.6082, 2869.5352), (3.0119383300940687, 179.1036650679682, -0.7090452705885488), (0.9344805, 0.9344805, 0.9344805), "StaticMeshActor_17949", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3329.2695, 3312.548, 2775.9993), (-20.504178550846447, 126.96082272782783, -21.843534391333275), (0.8374661, 0.8374661, 0.8374661), "StaticMeshActor_17950", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3253.1565, 3529.3176, 3244.306), (-1.1699219322257552, -31.201992867990096, 7.974518962105517), (0.9748939, 0.9748939, 0.9748939), "StaticMeshActor_17951", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3219.9607, 3443.8933, 2875.2583), (-22.694150700958904, 70.91503980261682, 5.723631188880111), (0.80227685, 0.80227685, 0.80227685), "StaticMeshActor_17952", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3267.0244, 3639.353, 3571.8376), (3.565508952898196, 51.83180595707718, 0.3519176275831617), (1.0953872, 1.0953872, 1.0953872), "StaticMeshActor_17953", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2226.0967, 4504.0635, 996.27216), (-6.004516756905881, 37.337989629236105, 6.89717390786287), (0.89517665, 0.89517665, 0.89517665), "StaticMeshActor_17954", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2979.0093, 2396.2158, 2359.1863), (6.722776450067052, 94.71500620975706, 6.680658627989205), (0.95122796, 0.95122796, 0.95122796), "StaticMeshActor_17955", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3396.7515, 2451.832, 2736.2632), (-9.080505827646022, 55.333770195635715, -2.6302492514495595), (1.0436015, 1.0436015, 1.0436015), "StaticMeshActor_17956", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3640.3943, 3776.6406, 5714.535), (45.98823074788268, 6.041356186468027, 6.829806837125858), (1.0353878, 1.0353878, 1.0353878), "StaticMeshActor_17957", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3633.291, 4129.155, 5838.542), (8.742552900556696, 88.29671324245535, 19.837818574793253), (0.9870695, 0.9870695, 0.9870695), "StaticMeshActor_17958", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3400.6619, 3797.0977, 5557.6567), (31.030214536107742, 3.6054132650345987, -18.01916773983478), (0.9018642, 0.9018642, 0.9018642), "StaticMeshActor_17959", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3408.4084, 3755.341, 5445.1196), (9.090843465244948, -84.80310455793352, 21.166863306876355), (0.97049713, 0.97049713, 0.97049713), "StaticMeshActor_17960", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3576.9167, 3469.8787, 5738.617), (5.452601316287801, -90.47085896811048, 26.589083338415882), (0.93164736, 0.93164736, 0.93164736), "StaticMeshActor_17961", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3269.022, 3495.3472, 5224.9805), (-25.597594197924625, -19.956326805460296, 3.979517330736422), (0.9142231, 0.9142231, 0.9142231), "StaticMeshActor_17962", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3406.6995, 3404.4673, 5564.6978), (-36.214659824904906, -43.21624657833885, 3.6824636888966946), (0.86569434, 0.86569434, 0.86569434), "StaticMeshActor_17963", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3356.1262, 3065.2515, 6067.445), (22.823268907991164, -84.00245201014465, -8.282775138724187), (1.018543, 1.018543, 1.018543), "StaticMeshActor_17964", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3303.4253, 3310.549, 4709.7827), (-15.531004074384988, 110.06856184341831, 4.483445304151833), (1.0919753, 1.0919753, 1.0919753), "StaticMeshActor_17965", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3304.639, 3209.0645, 4303.2236), (-3.0096129023271025, 173.62818591473422, -7.638823138112324), (1.0822457, 1.0822457, 1.0822457), "StaticMeshActor_17966", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3254.7158, 3112.091, 3863.9246), (5.002860607400277, 171.6512327239988, 9.87008833285503), (0.9889755, 0.9889755, 0.9889755), "StaticMeshActor_17967", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3247.6106, 2967.871, 3724.7708), (1.6411097520565654, 5.77274642821282, -2.648681623642787), (0.9273645, 0.9273645, 0.9273645), "StaticMeshActor_17968", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3394.997, 2998.507, 3570.018), (1.3550071736566915, 5.5596882164825745, 2.3081506558339497), (1.0723659, 1.0723659, 1.0723659), "StaticMeshActor_17969", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3447.003, 2670.283, 3396.1555), (-5.967742900605718, -10.479064930539868, -5.451294238380218), (1.0369321, 1.0369321, 1.0369321), "StaticMeshActor_17970", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3398.2788, 3395.1653, 3562.6174), (4.345011042699956, 42.30566667119946, -1.6328430084235859), (0.9876889, 0.9876889, 0.9876889), "StaticMeshActor_17971", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3402.88, 3410.9006, 3165.4832), (7.809890592405635, -142.98945135789197, 11.61134498486304), (0.8269301, 0.8269301, 0.8269301), "StaticMeshActor_17972", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3486.685, 3232.9495, 3187.92), (8.365135855888187, 110.29227216530418, -7.073424607619582), (0.94723845, 0.94723845, 0.94723845), "StaticMeshActor_17973", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3550.0537, 2906.012, 2694.497), (-16.892183631330887, 64.71114764185295, -13.144961138871267), (1.0, 1.0, 1.2584962), "StaticMeshActor_17974", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3392.9036, 3007.8325, 2756.169), (10.613205244283467, 124.59684316277526, -19.35388356904549), (0.9217482, 0.9217482, 0.9217482), "StaticMeshActor_17975", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3249.895, 2503.7808, 1914.786), (-2.4873965214512017, 125.11794575347747, -6.92056349081962), (1.027553, 1.027553, 1.027553), "StaticMeshActor_17976", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2503.8171, 6207.267, 2042.0492), (26.36653319146053, 178.08628304839374, 6.269869282790939), (0.958881, 0.958881, 0.958881), "StaticMeshActor_17977", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4656.432, 3246.5676, 1749.9918), (2.7820319116941077, 145.83664748009656, -8.447540358847686), (0.9706795, 0.9706795, 0.9706795), "StaticMeshActor_17978", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4970.7485, 3552.2456, 1686.6287), (-19.359740635599017, -11.061280064591688, 4.227969062913955), (1.0231287, 1.0231287, 1.0231287), "StaticMeshActor_17979", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5435.7114, 3321.8323, 1760.2902), (20.74738691421276, -169.91970672546415, -2.3103939095447283), (1.0386667, 1.0386667, 1.0386667), "StaticMeshActor_17980", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5872.4243, 3489.8042, 1485.6606), (18.269794982712195, -179.42941728584213, -10.833677105218971), (0.89006823, 0.89006823, 0.89006823), "StaticMeshActor_17981", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5480.398, 2874.3237, 1533.6171), (13.52558295827547, 178.38574759754948, 14.169717526629789), (0.8558986, 0.8558986, 0.8558986), "StaticMeshActor_17982", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5131.039, 4291.943, 1568.4183), (-10.586395528425681, -56.09359131307433, 8.879412231467786), (1.0184811, 1.0184811, 1.0184811), "StaticMeshActor_17983", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4852.0645, 4511.953, 1453.1833), (-51.210663074493965, 55.37130251463526, 8.98106701681043), (1.0574186, 1.0574186, 1.0574186), "StaticMeshActor_17984", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5329.6025, 2753.508, 1939.1595), (-1.1839599897889712, -149.0848851146195, -4.273070550302695), (0.9679047, 0.9679047, 0.9679047), "StaticMeshActor_17985", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5398.625, 2215.8772, 1706.1415), (-8.159820726856786, 98.21916653467073, -1.362609969736153), (1.0775387, 1.0775387, 1.0775387), "StaticMeshActor_17986", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5444.115, 1833.1489, 1524.1779), (1.9062274605692688, -79.54036832319214, -2.6218259425241888), (0.88132226, 0.88132226, 0.88132226), "StaticMeshActor_17987", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5593.071, 1806.8499, 1548.3793), (-7.16799826610293, -173.10772645904208, -7.225280263625594), (0.97194326, 0.97194326, 0.97194326), "StaticMeshActor_17988", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5379.7393, 2344.67, 1867.3964), (-0.3135985424744916, 145.6904343812382, 2.9049513859260525), (0.9525399, 0.9525399, 0.9525399), "StaticMeshActor_17989", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5398.922, 1789.0433, 1934.7509), (-5.778564248906075, -88.742398129083, 1.8156723354241975), (1.0950761, 1.0950761, 1.2452514), "StaticMeshActor_17990", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5357.505, 2225.236, 1306.3645), (6.804586231434059, 94.99866695238076, 1.74732518881425), (0.92518336, 0.92518336, 0.92518336), "StaticMeshActor_17991", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5500.618, 2203.6145, 1534.2026), (-6.786651570146688, 100.66663002088139, -4.719543203660318), (0.9404119, 0.9404119, 0.9404119), "StaticMeshActor_17992", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5402.233, 2193.334, 1158.0522), (14.422429084309293, -173.50124568737792, -6.686584337582336), (1.0326943, 1.0326943, 1.0326943), "StaticMeshActor_17993", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5543.281, 1454.4072, 1518.0214), (-6.460236078237473, 137.3228852594263, -6.369507241223922), (0.831579, 0.831579, 0.831579), "StaticMeshActor_17994", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5603.766, 1444.738, 1063.213), (-5.795227630723453, -2.5560305974207633, -5.2438053711027885), (0.80192727, 0.80192727, 0.80192727), "StaticMeshActor_17995", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5709.995, 1069.0825, 1747.4369), (-24.05068632685177, -174.00757417683346, 5.9381713728995305), (1.087141, 1.087141, 1.087141), "StaticMeshActor_17996", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5734.448, 648.9699, 2107.501), (13.475996141107675, 10.789763435507004, 10.115598322816501), (1.0036565, 1.0036565, 1.0036565), "StaticMeshActor_17997", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5982.947, 1011.4597, 1461.973), (7.886812039618015, -179.90285420242014, -2.187713317685336), (0.8538428, 0.8538428, 0.8538428), "StaticMeshActor_17998", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5784.974, 990.0625, 1169.4297), (7.468189638216481, -176.4055701155234, 9.734091141278443), (1.0796098, 1.0796098, 1.0796098), "StaticMeshActor_17999", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5790.6587, 601.77075, 1964.2687), (-30.28213782057368, -175.28381039692061, -4.70999139357459), (1.069269, 1.069269, 1.069269), "StaticMeshActor_18000", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5895.4414, 199.54727, 2021.1532), (0.76832836951197, -88.16173869573497, -29.74615421857223), (0.9319929, 0.9319929, 0.9319929), "StaticMeshActor_18001", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5544.506, 2072.3462, 3224.483), (-4.59518420028367, 113.36435818252461, 4.1650142726400246), (1.0525664, 1.0525664, 1.0525664), "StaticMeshActor_18002", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5488.566, 3392.9978, 3561.1284), (24.95173644802912, 19.626392570814016, 23.685182901233986), (1.0, 1.0, 1.0), "StaticMeshActor_18003", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5680.128, 3347.8198, 3347.0728), (-44.02017383908151, -164.0122450591528, -8.833189992482845), (1.0, 1.0, 1.0), "StaticMeshActor_18004", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5489.74, 3844.1406, 3464.9836), (0.8461794789975037, 97.79082010738051, 29.85649059386581), (1.0540944, 1.0540944, 1.0540944), "StaticMeshActor_18005", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5683.077, 3827.1963, 3264.1138), (-10.768858701431395, 107.82294125453234, 57.31404278751343), (0.88753563, 0.88753563, 0.88753563), "StaticMeshActor_18006", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5392.3076, 4597.728, 3568.6184), (5.97754199824563, -170.9345826244304, 9.894119746119147), (1.0169364, 1.0169364, 1.0169364), "StaticMeshActor_18007", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3016.527, 4494.521, 1271.4393), (8.23936444522667, -171.76650638324188, 3.855664736461932), (0.8720466, 0.8720466, 0.8720466), "StaticMeshActor_18008", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3428.3347, 4332.939, 1090.2804), (3.549587678877175, 87.73530987306486, 1.2023516758291637), (0.9298569, 0.9298569, 0.9298569), "StaticMeshActor_18009", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (306.19315, 706.95184, 2089.9646), (-22.3134137854466, 103.87656138159599, -1.9667971553638761), (0.8671668, 0.8671668, 0.8671668), "StaticMeshActor_18013", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (353.41696, 608.38995, 1509.021), (3.442203365259645, 13.78246735037972, -1.8977053810292608), (1.0807614, 1.0807614, 1.0807614), "StaticMeshActor_18014", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (313.9106, 739.74335, 1026.1583), (5.116247936415045, 177.67493952820925, 1.4492701975169309), (1.0445518, 1.0445518, 1.0445518), "StaticMeshActor_18015", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (-38.936016, 495.55676, 1451.1855), (0.7357752415648067, -168.80810779291863, 0.3499553052773934), (0.8039055, 0.8039055, 1.5513346), "StaticMeshActor_18016", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (763.40204, 622.11084, 2055.431), (26.042250619741452, 167.19526387302346, 2.765394278976924), (0.9231569, 0.9231569, 0.9231569), "StaticMeshActor_18017", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (675.98975, 277.50787, 2103.5598), (-8.332702426889117, 80.13297264698953, -22.898465963432667), (1.0318401, 1.0318401, 1.0318401), "StaticMeshActor_18018", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1135.7521, 1659.5415, 3297.7378), (-22.66061618274066, 36.143233711964236, -3.7965696152006054), (0.83589506, 0.83589506, 0.83589506), "StaticMeshActor_18019", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (665.5552, 2364.9568, 2682.1228), (-9.407621565046542, -78.20696700818918, 30.838415351057115), (0.92972636, 0.75294894, 0.92972636), "StaticMeshActor_18020", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (741.4528, 2482.1987, 2941.0708), (19.981006284163367, -163.8652741940918, -6.381287510831152), (0.82749194, 0.82749194, 0.96747965), "StaticMeshActor_18021", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1410.0917, 1406.8485, 3565.1523), (21.524070238175266, -143.22477245704323, -2.2774950569508854), (0.9605463, 0.9605463, 0.9605463), "StaticMeshActor_18022", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (704.8431, 2956.9724, 3290.2168), (-17.549713390932766, 8.007602862432687, -3.9767457078779356), (1.084848, 1.084848, 1.084848), "StaticMeshActor_18023", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (600.3207, 2996.0127, 3163.71), (-30.656068271503013, 7.946259991764377, -6.652587913909125), (0.98119617, 0.98119617, 0.98119617), "StaticMeshActor_18024", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (752.0355, 2552.923, 3269.321), (13.652229844558358, -175.24541768986248, 0.25130728666049745), (0.94779474, 0.94779474, 0.94779474), "StaticMeshActor_18025", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (595.8454, 2599.815, 3149.253), (-29.786959932494064, 12.921019963113325, -6.561706469723901), (0.83586496, 0.83586496, 0.83586496), "StaticMeshActor_18026", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (476.9909, 2976.1907, 2809.5168), (1.4770891012820238, 98.96651649620554, -22.465389053486074), (1.0592401, 1.0592401, 1.0592401), "StaticMeshActor_18027", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (558.0764, 3380.5386, 2681.2837), (10.089788177100123, 90.71586490458645, -32.42287869534627), (0.8335969, 0.8335969, 0.8335969), "StaticMeshActor_18028", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (712.18665, 2981.741, 2900.2798), (21.982099428598286, -174.02186252444142, -5.36605708799602), (1.0364969, 1.0364969, 1.0364969), "StaticMeshActor_18029", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (688.8728, 3781.2622, 2920.139), (-17.772676226193724, 12.552603067333278, -8.524140278930476), (1.0884588, 1.0884588, 1.0884588), "StaticMeshActor_18030", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (707.7083, 3393.7507, 2912.5686), (-10.123259058148069, -85.03112762951723, 29.367001864515597), (0.9680115, 0.9680115, 0.9680115), "StaticMeshActor_18031", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (838.96844, 2987.6528, 3617.288), (-0.35299566231348645, 91.86024381442229, -33.41412074263705), (0.92624086, 0.92624086, 0.92624086), "StaticMeshActor_18032", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (887.77124, 2579.5227, 3616.3508), (-3.025879477119216, 82.45950708545037, -24.822935109595733), (0.88939595, 0.88939595, 0.88939595), "StaticMeshActor_18033", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1208.8627, 2616.5015, 3694.726), (-7.334320003100307, 91.0617582308236, -29.88342183583868), (1.0076768, 1.0076768, 1.0076768), "StaticMeshActor_18034", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (686.3856, 3766.7085, 3295.5305), (-25.173306687897064, 6.7106328483024456, 5.5468869955164015), (1.0687022, 1.0687022, 1.1940322), "StaticMeshActor_18035", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (705.2575, 3370.9285, 3277.8818), (12.933048539299447, -179.02424771384483, -5.31985408234144), (0.98718506, 0.98718506, 0.98718506), "StaticMeshActor_18036", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (619.2001, 4231.533, 3249.1626), (6.319720504150859, -81.57436801912407, 20.581239075042244), (0.821761, 0.821761, 0.821761), "StaticMeshActor_18037", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (867.0063, 3365.6135, 3646.8071), (2.370205105678297, 98.804352225039, -40.602843304174925), (0.97680056, 0.97680056, 0.97680056), "StaticMeshActor_18038", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (649.25073, 4268.4683, 2932.272), (4.435510898348622, 86.23518451867534, -14.340938942155958), (1.1060966, 0.91477334, 0.91477334), "StaticMeshActor_18039", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (720.29694, 4679.6924, 2906.7217), (-33.94397000262259, -15.196989961155818, 13.121536747143125), (0.96628195, 0.96628195, 0.96628195), "StaticMeshActor_18040", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (524.26917, 4628.1997, 2803.9238), (26.22244645527821, 161.68490739326117, 0.09105627071689518), (1.0652982, 1.0652982, 1.0652982), "StaticMeshActor_18041", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (675.90424, 4698.1445, 3205.5422), (-11.573700390373133, -18.420441311246318, 3.754457301619025), (0.8484412, 0.8484412, 0.8484412), "StaticMeshActor_18042", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (595.88586, 4602.8594, 3159.8477), (-13.373443265507223, -7.020904176131719, 0.7918632812626917), (0.808411, 0.808411, 0.808411), "StaticMeshActor_18043", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (812.7315, 3737.3862, 3670.6582), (-7.1024786929903225, -75.53433166649468, 28.652979874375564), (0.96968764, 0.96968764, 0.96968764), "StaticMeshActor_18044", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (677.547, 4152.5303, 3628.6616), (9.157792222062175, -87.60093924388109, 16.25029515723711), (1.0363865, 1.0363865, 1.0363865), "StaticMeshActor_18045", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (611.39484, 4591.502, 3954.2693), (2.5733288273329196, -100.5230021544462, -12.033079657292657), (0.9060195, 0.9060195, 0.9060195), "StaticMeshActor_18046", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (615.14734, 4616.6997, 3545.443), (4.679287335739709, -174.77169786826886, -4.517028499639479), (1.0057943, 1.0057943, 1.0057943), "StaticMeshActor_18047", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (596.30994, 4598.0293, 3555.1687), (-3.602355855303983, 82.01356958889856, 2.1170917522846318), (0.87672204, 0.87672204, 0.87672204), "StaticMeshActor_18048", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (756.15533, 4581.39, 3891.1853), (-7.36856006451426, 91.15445268364432, 1.384576608815857), (0.8548943, 0.8548943, 0.8548943), "StaticMeshActor_18049", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (823.1499, 3394.9646, 5238.5605), (22.54642414686047, 171.73397797542216, 3.770773689121578), (1.1436605, 1.1913534, 1.099441), "StaticMeshActor_18050", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (810.075, 3809.1924, 5222.421), (-15.98095587490054, 6.428566398889156, -4.87365697337354), (0.95643044, 0.95643044, 0.95643044), "StaticMeshActor_18051", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (781.20056, 4200.3125, 5262.4214), (-10.809812123207426, -83.33333747750487, 11.40982073040056), (0.9788517, 0.9788517, 0.9788517), "StaticMeshActor_18052", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (731.4559, 4575.308, 5255.301), (18.048238919764533, 175.92161813292046, -3.990111966360263), (0.93825376, 0.93825376, 0.93825376), "StaticMeshActor_18053", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (842.2233, 4989.0474, 5700.9253), (-2.9023130152040313, 97.55708726454118, -30.737852893937863), (0.9835139, 0.9835139, 0.9835139), "StaticMeshActor_18054", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (668.9463, 4981.7095, 5289.9644), (-22.69757226996292, 7.3100135561656305, -0.23901376954239584), (1.0600224, 0.9246094, 1.0498542), "StaticMeshActor_18055", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (863.6279, 5405.6313, 5730.641), (-39.233509261163384, 179.99117489258646, -10.163875728438462), (0.8928378, 0.8928378, 0.8928378), "StaticMeshActor_18056", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (662.5196, 5373.138, 5306.0312), (6.061019519737393, 101.05439176718181, -25.795895202659967), (0.98644876, 0.98644876, 0.98644876), "StaticMeshActor_18057", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (594.3835, 6198.4595, 4244.6875), (4.37573974597939, 161.47926000418326, -2.7165831177510307), (1.3602128, 1.3602128, 1.3602128), "StaticMeshActor_18058", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (611.3561, 6196.9556, 4362.8374), (3.7205880583460367, -90.34023717854187, -1.2871089931070037), (0.9868208, 0.9868208, 0.9868208), "StaticMeshActor_18059", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (620.0541, 5803.3306, 4208.783), (4.422833795766857, -4.433837766701944, 3.824894843322756), (1.0855279, 1.2253006, 1.4523009), "StaticMeshActor_18060", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (551.0413, 6190.8984, 4781.1084), (1.7917426268441516, -91.42074412349973, -0.46762082877173966), (1.0489264, 1.0489264, 1.2054582), "StaticMeshActor_18061", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (558.40936, 5779.7397, 4769.992), (-5.415557885236621, 87.86884018619698, 0.33758410222362656), (0.84829366, 0.84829366, 0.84829366), "StaticMeshActor_18062", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (996.349, 2210.413, 4367.0903), (16.048784974551975, 28.93565363245541, -3.95043842970095), (0.9992622, 0.9992622, 0.9992622), "StaticMeshActor_18063", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1098.1409, 2057.4985, 4772.386), (3.002175811394581, 21.92618654070204, 3.583971852169653), (0.9130786, 0.9130786, 0.9130786), "StaticMeshActor_18064", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1146.4572, 2082.8406, 4324.3936), (-11.46380614637596, 120.49058401645041, 4.398757188571741), (1.1596715, 1.1086494, 1.0495374), "StaticMeshActor_18065", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1681.0477, 1361.392, 4099.8403), (52.04603905142213, 48.921628744147306, 88.31211447123118), (0.93687403, 0.93687403, 1.15625), "StaticMeshActor_18066", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3049.1924, 2919.9253, 3731.7812), (2.18342028410712, 176.18671246106643, 3.814288064480875), (0.95251155, 0.95251155, 0.95251155), "StaticMeshActor_18067", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3052.2573, 3134.1316, 3858.841), (7.243981924060401, -171.5088771556435, -6.56161427883155), (0.8540154, 0.8540154, 0.8540154), "StaticMeshActor_18068", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3023.2288, 3132.9731, 4313.6416), (7.564400108803076, 94.34041245694522, 2.6854842417720355), (1.0007992, 1.0007992, 1.0007992), "StaticMeshActor_18069", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2841.4788, 3007.5837, 3782.5305), (5.450457204049725, -91.72840714164874, -3.679322068828748), (0.84569776, 0.84569776, 0.84569776), "StaticMeshActor_18070", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3018.2986, 3251.9844, 4720.4487), (-2.6317746925718315, -13.59869247534369, 9.260787226658337), (0.9912998, 0.9912998, 0.9912998), "StaticMeshActor_18071", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2995.3665, 3169.4653, 6007.792), (-42.17687984176757, -95.66858024975292, 3.9388725173197425), (0.93353546, 0.93353546, 0.93353546), "StaticMeshActor_18072", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2606.139, 2994.1394, 5961.2866), (-0.72082528148422, 1.1151144135193622, 24.78629067870035), (1.014704, 1.014704, 1.014704), "StaticMeshActor_18073", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1946.4181, 5893.876, 1531.5841), (-10.392273820856444, 29.095118171106105, -9.279235465766968), (0.8840096, 0.8840096, 0.8840096), "StaticMeshActor_18074", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1789.8065, 6189.285, 1553.8611), (-6.964323806009858, 82.25683563316367, 7.685917000729308), (0.8119021, 0.8119021, 0.8119021), "StaticMeshActor_18075", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4133.0854, 550.84784, 5239.523), (-0.2158782718022519, 113.98997830604408, -37.97869984752138), (0.9340126, 0.9340126, 0.9340126), "StaticMeshActor_18076", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4510.557, 464.28635, 5385.4854), (29.393571634907186, 83.68433949667806, 14.45602688847923), (1.0719283, 1.0719283, 1.0719283), "StaticMeshActor_18077", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4197.022, 194.79915, 5164.679), (-15.035247423473137, -54.077268925025095, 36.471648102538346), (0.89917696, 0.89917696, 0.89917696), "StaticMeshActor_18078", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4968.5938, 485.17502, 5413.7236), (15.420713998035051, -3.211578760791964, -12.049590610884833), (1.031876, 1.031876, 1.031876), "StaticMeshActor_18079", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4205.0146, 204.06941, 4767.3916), (9.121435874828265, -123.11503646386835, -2.169555032832413), (0.8769734, 0.8769734, 0.8769734), "StaticMeshActor_18080", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1664.1947, 3508.6523, 3742.1853), (11.849783986719137, -16.812896386906203, 5.958960086552178), (0.9924625, 0.9924625, 0.9924625), "StaticMeshActor_18081", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2223.1123, 3479.8123, 3573.9636), (0.5641941058663011, 5.290222950268593, -7.800170997405499), (0.8587987, 0.8587987, 0.8587987), "StaticMeshActor_18082", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1165.1653, 3621.782, 3677.921), (-19.2364797796789, 25.94264826117701, 6.867990453656502), (1.1450303, 1.0062909, 0.9842808), "StaticMeshActor_18083", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2493.7158, 6168.783, 1104.588), (-2.59738173826983, -81.4523622949236, -5.523955995224988), (0.9905628, 0.9905628, 0.9905628), "StaticMeshActor_18084", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2467.0933, 6171.5513, 1603.757), (-1.140991393321064, -100.3832882600352, 12.213968301344918), (0.905072, 0.905072, 0.905072), "StaticMeshActor_18085", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2423.848, 5854.0522, 1736.1853), (-1.87707476573824, -84.04006674258129, -7.900207988603412), (0.8400818, 0.8400818, 0.8400818), "StaticMeshActor_18086", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2391.569, 5570.1245, 1719.1388), (-3.6238401048795397, -52.636650068322936, 2.7199156565657128), (0.8914653, 0.8914653, 0.8914653), "StaticMeshActor_18087", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1604.3608, 5994.6313, 1281.2875), (-6.08724968624987, -174.0352549349393, -0.05548094448253396), (0.81752264, 0.81752264, 0.81752264), "StaticMeshActor_18088", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (808.14685, 5918.864, 1531.6166), (2.7341118340540196, 62.81106906690956, 11.252613748238318), (0.92273694, 0.92273694, 0.92273694), "StaticMeshActor_18089", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1414.7174, 6408.592, 1547.9259), (-2.5812680457278554, 169.18945065236198, -15.406126702372216), (0.9714287, 0.9714287, 0.9714287), "StaticMeshActor_18090", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (969.28845, 6295.509, 1526.707), (-5.51644899891021, 25.43921876186905, 20.698848201100777), (1.0549176, 1.0549176, 1.0549176), "StaticMeshActor_18091", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2985.3015, 3496.9907, 4874.527), (24.30311347768555, -84.97058874055813, -2.792144406743408), (0.8499612, 0.8499612, 0.8499612), "StaticMeshActor_18092", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3005.0903, 3408.998, 4763.651), (-6.159851273809944, -175.74373871500154, -22.55834992087498), (1.0121601, 1.0121601, 1.0121601), "StaticMeshActor_18093", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3789.9624, 596.9965, 4751.818), (25.511588327772227, -73.06624508697452, -0.47286947690825687), (1.0036529, 1.0036529, 1.0036529), "StaticMeshActor_18094", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5064.541, 6186.0615, 5819.6885), (-2.805146000513438, 85.90939182205933, -18.940245751983486), (0.9273489, 0.9273489, 0.9273489), "StaticMeshActor_18095", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5054.9395, 5823.5576, 5785.7866), (-10.936280649937256, 93.5597566384367, -20.354372901253303), (1.0624231, 1.0624231, 1.0624231), "StaticMeshActor_18096", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4608.3965, 6214.6245, 5778.6406), (6.7838245110540685, -173.3221756088138, 5.753588415415262), (1.019982, 1.019982, 1.019982), "StaticMeshActor_18097", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4608.7363, 5851.1274, 5795.8735), (-17.36166365886739, 86.16596967318915, 2.1151720991830496), (1.0275481, 1.0275481, 1.0275481), "StaticMeshActor_18098", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4219.7446, 5541.5776, 5965.9707), (-9.137358868155896, 86.75426157536648, -7.461334559993989), (0.87308276, 0.87308276, 0.87308276), "StaticMeshActor_18099", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4643.191, 5510.108, 5920.2534), (0.5253574609260001, 7.688178410625306, 15.425044831097837), (1.0342298, 1.0342298, 1.0342298), "StaticMeshActor_18100", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4190.029, 5420.657, 6090.1826), (2.1184303465687333, 175.21586419761968, -15.952479424636374), (0.9036641, 0.9036641, 0.9036641), "StaticMeshActor_18101", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4192.0366, 5027.8057, 6136.854), (-6.745208134794074, 92.53234490669469, 5.041404040785133), (1.0331088, 1.0331088, 1.0331088), "StaticMeshActor_18102", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3787.1345, 5537.702, 5936.4653), (-9.419006425566922, -177.38152174764446, -27.72424347087691), (0.87211233, 0.87211233, 0.87211233), "StaticMeshActor_18103", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3405.3093, 5406.9653, 5946.4595), (2.4362463252337747, -173.23501730331702, -3.7837224745674574), (0.86523855, 0.86523855, 0.86523855), "StaticMeshActor_18104", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3804.4717, 5394.2783, 5945.176), (13.384739310917098, -98.25693742535624, -0.6378783786876265), (0.92601454, 0.92601454, 0.92601454), "StaticMeshActor_18105", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1868.7654, 5470.2173, 5882.561), (-7.254485468319441, 99.67984911436497, 5.9059364679298385), (1.2707963, 1.25292, 0.99314), "StaticMeshActor_18106", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1306.4939, 5433.8228, 5872.946), (20.820545065931164, 1.1519683636634923, -3.7522884200160016), (1.0666327, 1.0666327, 1.0666327), "StaticMeshActor_18107", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1229.4067, 5025.2666, 5925.1665), (2.876843954505024, -82.61706752888358, -25.950043650046613), (0.8175165, 0.8175165, 0.8175165), "StaticMeshActor_18108", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1815.357, 5011.488, 5966.3438), (9.926626678358739, 178.24229772087526, 2.2832816049815254), (0.8145114, 0.8145114, 0.8145114), "StaticMeshActor_18109", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1827.1985, 3810.0754, 6075.7715), (10.818152662578074, -176.26822058190487, -2.8689275999129906), (1.0806769, 1.0806769, 1.0806769), "StaticMeshActor_18110", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3000.0598, 5398.9824, 5952.8486), (-5.366821380515268, -86.51706184172063, -11.190915951782571), (1.0637963, 1.0637963, 1.0637963), "StaticMeshActor_18111", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3690.9377, 4576.9756, 5975.3022), (8.650762651357752, -9.053681078390014, 2.3963807501953402), (0.8357483, 0.8357483, 0.8357483), "StaticMeshActor_18112", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3705.0403, 4997.445, 6008.3203), (4.16236405694014, -84.17408348152583, -3.6702258500128093), (1.0324042, 1.0324042, 1.0324042), "StaticMeshActor_18113", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3406.9805, 4991.162, 5963.017), (-0.9885868897555358, -80.49917205449063, -9.771270854673782), (1.0545645, 1.0545645, 1.0545645), "StaticMeshActor_18114", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1788.2023, 2973.203, 6090.643), (0.5985567335352501, 85.33606832292409, 0.10244070604058113), (0.91282076, 0.91282076, 0.91282076), "StaticMeshActor_18115", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1784.23, 3399.6309, 6059.297), (-10.321226765750467, 5.444502303431387, 5.6120666125344965), (1.0253032, 1.0253032, 1.0253032), "StaticMeshActor_18116", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2202.925, 3001.4333, 5953.067), (10.837070942415773, -97.09600639611847, 12.677239869847714), (0.84032255, 0.84032255, 0.84032255), "StaticMeshActor_18117", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1793.6543, 2593.594, 5945.92), (-11.74826145729196, -178.73979138056976, 20.612679503307774), (1.062706, 1.062706, 1.062706), "StaticMeshActor_18118", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4197.871, 4611.309, 6152.5356), (-7.224456997876666, -91.16968123608633, -11.008910751793756), (0.97416806, 0.97416806, 0.97416806), "StaticMeshActor_18119", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3805.0466, 4596.146, 5957.317), (3.030111256012868, -88.37352881151733, -23.031916402644242), (0.9340856, 0.9340856, 0.9340856), "StaticMeshActor_18120", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4168.3433, 4197.4463, 6070.1396), (-12.604031373386409, -97.35243510745626, -9.798032622686287), (0.92686087, 0.92686087, 0.92686087), "StaticMeshActor_18121", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4601.5864, 4616.172, 6148.7964), (2.4954095650703634, -3.0303651338155797, 4.430857507443998), (0.9451282, 0.9451282, 0.9451282), "StaticMeshActor_18122", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4972.2266, 3811.8643, 6128.1875), (-7.054810522118575, 91.85576917439094, 2.563895875778742), (0.99163413, 0.99163413, 0.99163413), "StaticMeshActor_18123", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4594.202, 3798.7097, 6108.5376), (-5.333861611024639, -174.43332419354255, -3.7189636855095918), (0.88098574, 0.88098574, 0.88098574), "StaticMeshActor_18124", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5009.039, 4207.801, 6070.8403), (3.6828853961203527, 176.71435799592382, -2.716247467673835), (1.218029, 1.098608, 1.1909748), "StaticMeshActor_18125", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4205.9517, 3037.5576, 6200.1465), (8.1009804348976, 177.7568909744933, -3.415008720311438), (1.0663514, 1.0663514, 1.0663514), "StaticMeshActor_18126", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3767.6885, 3038.788, 6131.858), (-14.222414099415444, -178.81132139209836, -18.96130257111643), (0.851203, 0.851203, 0.851203), "StaticMeshActor_18127", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5794.533, 4641.0786, 5821.84), (-1.0525511599382893, -179.73569872111102, -11.739378060659275), (0.92747205, 0.92747205, 0.92747205), "StaticMeshActor_18128", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5480.3154, 4668.0234, 5893.4976), (-17.959469353833097, -3.9066163325905463, 4.190535451227279), (0.86055344, 0.86055344, 0.86055344), "StaticMeshActor_18129", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5097.1772, 3799.4, 5993.2227), (-11.341278263384776, -2.876922735806947, 3.9384437536345653), (1.0234613, 1.0234613, 1.0234613), "StaticMeshActor_18130", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5450.223, 3793.5242, 5877.052), (10.839433628452275, 177.031287259065, 2.315860525495771), (0.8545364, 0.8545364, 0.8545364), "StaticMeshActor_18131", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5095.0674, 4203.293, 5979.3135), (-3.0437314615005024, -99.0943942957546, 3.718774925590374), (0.87706566, 0.87706566, 0.87706566), "StaticMeshActor_18132", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5452.3096, 4204.578, 5875.025), (-6.841308291430894, 1.449231632822896, 4.109858555169793), (1.0279742, 1.0279742, 1.0279742), "StaticMeshActor_18133", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5814.2153, 4194.695, 5806.253), (-1.4344176355912734, 176.56544368103462, 4.925606564382131), (0.88273793, 0.88273793, 0.88273793), "StaticMeshActor_18134", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5813.1577, 3804.003, 5795.098), (5.772301074924663, 175.74075139485115, 9.027946090406473), (0.80204546, 0.80204546, 0.80204546), "StaticMeshActor_18135", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5098.0327, 3389.0369, 5962.7324), (3.6468503163405366, -172.03528638067294, -3.1348579102002967), (0.94091326, 0.94091326, 0.94091326), "StaticMeshActor_18136", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5464.2856, 3394.7932, 5869.3916), (-5.694976146261043, 95.97675476229041, -14.644012128102776), (0.8381329, 0.8381329, 0.8381329), "StaticMeshActor_18137", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5014.3022, 3404.8713, 6054.3896), (0.02013535293104615, -83.49744155579769, 4.209762306666456), (1.0075474, 1.0075474, 1.0075474), "StaticMeshActor_18138", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5811.7515, 3399.0215, 5793.8335), (-3.023468170609805, -95.67426839400986, 12.294439172563514), (0.86780185, 0.86780185, 0.86780185), "StaticMeshActor_18139", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5106.7485, 2995.4026, 5980.112), (-0.14709483363800663, 89.67054008165098, -22.308562394244394), (0.83244765, 0.83244765, 0.83244765), "StaticMeshActor_18140", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (6538.7744, 1384.4591, 5806.458), (-2.8319085627081932, -176.79760978100478, 9.036493152865562), (0.8466176, 0.8466176, 0.8466176), "StaticMeshActor_18141", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (6195.676, 1346.5458, 5810.8955), (-4.202514059556826, 173.8706229138263, 14.901729024338765), (1.0596427, 1.0596427, 1.0596427), "StaticMeshActor_18142", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (6495.728, 2209.4746, 5787.144), (2.2528219262698284, -88.61173728899342, -7.960602249926693), (0.91021395, 0.91021395, 0.91021395), "StaticMeshActor_18143", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (6206.643, 2195.5679, 5793.5723), (8.719793459248647, 81.7249057471696, -8.598021155435513), (1.0752456, 1.0752456, 1.0752456), "StaticMeshActor_18144", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (6474.164, 1808.8357, 5791.95), (-3.293212836870909, -171.61227297541856, 8.321319932235074), (0.95127314, 0.95127314, 0.95127314), "StaticMeshActor_18145", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (6199.1387, 1795.1035, 5798.318), (-6.534117939976975, 7.0325540168466505, -6.81829778185262), (0.8739051, 0.8739051, 0.8739051), "StaticMeshActor_18146", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5800.769, 1350.1293, 5804.768), (-16.58035041377592, -84.81744719875825, -7.817534919043165), (0.9772304, 0.9772304, 0.9772304), "StaticMeshActor_18147", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5403.814, 1278.3, 5814.968), (20.52988822292233, 99.93761816342646, -7.988710047312836), (1.2270559, 1.2159135, 0.8882557), "StaticMeshActor_18148", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5020.948, 1257.1262, 5851.535), (-22.92706070640012, -101.23766120810454, 0.055189327344951834), (1.0177349, 1.0177349, 1.0177349), "StaticMeshActor_18149", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5080.22, 2179.4958, 5950.4565), (-1.6347046564077852, -3.8260802492596087, -9.032256685167814), (0.8435017, 0.8435017, 0.8435017), "StaticMeshActor_18150", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5065.2236, 1709.9164, 5919.9814), (-13.264374672294618, 1.4193542084196578, -20.45984071512386), (0.8360653, 0.8360653, 0.8360653), "StaticMeshActor_18151", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5095.4624, 2566.5159, 5977.589), (8.783860673551422, -175.4018151269746, 3.0267835885638714), (1.0246671, 1.0246671, 1.0246671), "StaticMeshActor_18152", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4638.869, 1253.5615, 5881.456), (15.258024491330259, 97.98104188951747, -2.813445933108266), (0.99358106, 0.99358106, 0.99358106), "StaticMeshActor_18153", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4221.892, 2610.8142, 6239.731), (4.910235914518855, -91.78226490588541, 9.096221233624071), (0.9429706, 0.9429706, 0.9429706), "StaticMeshActor_18154", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3352.3267, 1088.8363, 5936.1133), (2.327250450784491, -4.379089550013536, -25.774841765890752), (0.82796335, 0.82796335, 0.82796335), "StaticMeshActor_18155", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3387.5496, 1285.6206, 6099.7124), (2.382185241973734, 0.5090916879192922, -29.159026003438665), (1.0756993, 1.0756993, 1.0756993), "StaticMeshActor_18156", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3400.7102, 994.1739, 5947.873), (4.383942812881202, 172.22030581696947, -38.275178429576364), (0.8636778, 0.8636778, 0.8636778), "StaticMeshActor_18157", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2877.783, 1145.6819, 5917.2607), (-26.039519138334782, -80.23288258539674, -21.482695387922107), (0.97170526, 0.97170526, 0.97170526), "StaticMeshActor_18158", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2923.0715, 1278.3313, 6110.581), (12.295697271518032, 80.98669658632393, 13.406711306589644), (0.944187, 0.944187, 0.944187), "StaticMeshActor_18159", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2595.3428, 1411.8965, 5959.4453), (-21.20202553119794, 169.97446644968025, 34.00394141848316), (0.80945325, 0.80945325, 0.80945325), "StaticMeshActor_18160", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3348.8523, 2665.462, 6150.3037), (-9.669311787396962, 86.42985258930138, 7.329703583679769), (1.0956247, 1.0956247, 1.0956247), "StaticMeshActor_18161", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2456.3594, 1689.747, 5941.601), (26.82040602000619, 1.4580073633876125, -11.930478956846228), (0.89881635, 0.89881635, 0.89881635), "StaticMeshActor_18162", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2105.652, 1723.0499, 5815.9995), (-8.535156288919762, 170.91358418372107, 7.891147729252417), (0.89857465, 0.89857465, 0.89857465), "StaticMeshActor_18163", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2590.0933, 2628.2522, 6053.2495), (13.55907047477354, -84.52117273801562, 10.216435021954887), (0.9069385, 0.9069385, 0.9069385), "StaticMeshActor_18164", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2532.7195, 2162.5947, 5954.0435), (-11.055878498985395, -175.05890350806627, 3.720102311502182), (0.8202315, 0.8202315, 0.8202315), "StaticMeshActor_18165", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2111.171, 2139.7893, 5866.989), (1.3961869011755415, 81.0197979004852, 17.713628763047037), (0.9058708, 0.9058708, 0.9058708), "StaticMeshActor_18166", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3992.7805, 459.62274, 4760.441), (-0.0629882782579407, -155.8145359100263, 6.48262336754224), (1.0227985, 1.0227985, 1.0227985), "StaticMeshActor_18167", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2909.2207, 5596.522, 996.46265), (-2.1621402520532507, -127.53757678792581, -4.997192983096391), (1.0, 1.0, 1.0), "StaticMeshActor17622", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3813.4307, 1784.1658, 2904.6592), (-3.4825743515268224, 95.41295777798412, -4.243896543507784), (1.083322, 1.083322, 1.083322), "StaticMeshActor17663", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4737.4087, 4529.2324, 3348.606), (0.0, -130.00015094089886, 0.0), (0.922264, 1.5693417, 0.922264), "StaticMeshActor17673", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1686.0996, 5033.8687, 985.2753), (-0.4112855980818701, 102.89872668705186, 1.8983884325698552), (1.019459, 1.019459, 1.019459), "StaticMeshActor17680", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4103.4307, 1334.1658, 2904.6592), (-3.4825744187022645, -98.6496344367685, -4.2438975237379335), (1.083322, 1.083322, 1.083322), "StaticMeshActor17859", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2759.542, 5679.1724, 968.4899), (-3.8211672357884727, -148.69506334470702, -3.880035229508875), (1.0, 1.7213194, 1.0), "StaticMeshActor17923", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4176.716, 1905.1514, 2979.1626), (-2.6712642702803926, 138.33680619776254, -173.04460483989916), (1.083322, 1.083322, 1.083322), "StaticMeshActor17934", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3185.545, 1620.4333, 2909.9578), (3.642191203277016, 115.37036770908192, -176.38640203869465), (1.083322, 1.083322, 1.083322), "StaticMeshActor17935", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3661.328, 2969.7424, 3516.2754), (-5.126006523028875, -87.6178384968106, -178.7631993933308), (1.0, 1.0, 1.1402385), "StaticMeshActor17936", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1209.062, 430.37158, 4459.269), (55.75081970331071, -116.60100379167733, 7.97721433944848), (1.018122, 1.018122, 1.018122), "StaticMeshActor17937", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1137.7738, 1336.3152, 4637.3057), (-5.4442138014612365, 125.0556590165986, -1.4026183879008254), (1.018122, 1.0681517, 1.018122), "StaticMeshActor18010", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (957.7738, 966.3152, 4647.3057), (67.02514918224749, -136.2537490315007, 71.32824125270182), (1.018122, 1.018122, 1.018122), "StaticMeshActor18011", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3340.3062, 5581.799, 772.30975), (3.1481299669168905, 3.3847064109187124, 172.99686391518296), (1.0, 1.0, 1.0), "StaticMeshActor18012", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3654.23, 374.07062, 4325.1265), (13.752465528520073, 94.10991747283906, 19.251661851928183), (0.851758, 0.851758, 1.0), "StaticMeshActor18173", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5500.0835, 3075.0334, 2067.7754), (-6.963531808665738, -79.04749172012696, -172.62236453381996), (1.0, 1.0, 1.0), "StaticMeshActor18189", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (396.97775, 1007.9011, 2099.0947), (31.357093505269205, -48.15734552531184, -1.9088737289320146), (0.803905, 0.803905, 0.803905), "StaticMeshActor18191", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2760.4932, 432.72348, 4381.5303), (-18.476379750487332, -83.12677717648492, 19.093395024784638), (1.0, 1.0, 1.9890856), "StaticMeshActor18198", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3653.4329, 62.756916, 4741.807), (-0.49649045090820926, -15.565032126466196, -12.674316964497036), (1.4375, 1.0625, 1.022799), "StaticMeshActor18199", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3065.2986, 148.3554, 4788.5957), (5.347128633124302, 168.38744562090318, 6.565157952003416), (1.4375, 1.0625, 1.022799), "StaticMeshActor18218", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (196.29597, 3317.23, 4802.155), (9.1560251946939, 67.02532860329926, 24.813157020626296), (1.066744, 1.066744, 1.066744), "StaticMeshActor18229", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (262.7011, 2917.0857, 4734.9014), (25.925451141794234, 7.0689390076440155, 4.881396986469113), (1.066744, 1.066744, 1.066744), "StaticMeshActor18249", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (188.03815, 3665.3933, 4620.474), (0.0, -157.50015073990477, 0.0), (1.054698, 1.054698, 1.054698), "StaticMeshActor18301", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3269.916, 2804.5618, 1600.9493), (-17.051881900643853, 59.544602447228634, -9.711762959855957), (1.078468, 1.078468, 1.078468), "StaticMeshActor18302", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3294.1096, 2649.5225, 1600.9493), (-17.051728278689836, 23.90778184648693, -9.711762317178248), (1.078468, 1.078468, 1.078468), "StaticMeshActor18303", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3294.1096, 2593.6494, 1939.7976), (-5.1316221344512165, 157.57768036500764, 172.9816294522718), (1.078468, 1.078468, 1.078468), "StaticMeshActor18304", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2805.3623, 3058.451, 885.75415), (1.7813357277520465, 19.105161520301966, 5.861256287688282), (0.57333624, 0.57333624, 0.57333624), "StaticMeshActor18311", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (833.4832, 767.723, 1921.3365), (4.858056154411245, -166.02850884522067, -175.4205661198328), (0.671369, 0.923157, 0.923157), "StaticMeshActor18312", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (833.4834, 767.723, 1528.0219), (4.858056154411245, -166.02850884522067, -175.4205661198328), (0.671369, 0.923157, 0.923157), "StaticMeshActor18313", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (826.22296, 919.2521, 1528.0219), (4.858056154411245, -166.02850884522067, -175.4205661198328), (0.671369, 0.923157, 0.923157), "StaticMeshActor18314", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (780.7267, 919.252, 1765.1842), (1.0936972664963354, -166.0755873812459, -176.35637338949834), (0.671369, 0.923157, 0.923157), "StaticMeshActor18315", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (650.6765, 1007.9011, 2099.0947), (20.005752177552615, -42.611179352970375, 10.78406123142643), (0.803905, 0.803905, 0.803905), "StaticMeshActor18316", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1167.1337, 422.40875, 2567.2532), (12.810908594969858, 93.88040600518804, 22.14317128834712), (0.896978, 0.896978, 0.896978), "StaticMeshActor18317", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3227.6392, 4304.8735, 1271.4393), (8.23936410176106, 165.44876024916564, 3.8557131340532895), (0.872047, 0.3945192, 0.872047), "StaticMeshActor18318", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1592.6344, 5392.2593, 985.27527), (-0.4112855350659471, 102.89872668540438, 1.8983882357353912), (1.019459, 1.019459, 1.019459), "StaticMeshActor18319", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (189.66283, 5787.3296, 1440.5657), (-9.686920497547467, 95.81621828507463, -8.639251589500189), (0.954931, 0.954931, 0.954931), "StaticMeshActor18321", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (189.66283, 5787.3296, 1642.0505), (-9.686920497547467, 95.81621828507463, -8.639251589500189), (0.954931, 0.954931, 0.954931), "StaticMeshActor18323", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (153.6612, 5787.3296, 1884.332), (-11.031218036182187, -84.65648479919477, 3.4377018320343713), (0.954931, 0.954931, 0.954931), "StaticMeshActor18324", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (153.6612, 5787.3296, 2187.1587), (-11.031218036182187, -84.65648479919477, 3.4377018320343713), (0.954931, 0.954931, 0.954931), "StaticMeshActor18325", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1686.1918, 5500.751, 2487.7922), (-25.22723153609762, -115.60229097255126, 1.9912363818476988), (0.817537, 0.98800766, 0.817537), "StaticMeshActor18326", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (524.229, 2030.765, 2501.5151), (0.8703243733335693, -84.81042330698335, -8.856568016862573), (0.869591, 0.869591, 0.655837), "StaticMeshActor18327", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (172.35434, 2093.5972, 2501.5151), (-0.4277035637665011, -84.75463930025376, 5.28940417730573), (1.2669717, 1.2477252, 0.655837), "StaticMeshActor18328", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (558.4108, 5832.993, 4604.949), (-5.415557885236621, 87.86884018619698, 0.33758410222362656), (0.848294, 0.848294, 0.848294), "StaticMeshActor18350", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (645.448, 5762.422, 5246.716), (-1.57519639303109, 71.15676056173974, -23.18206800150241), (1.2880448, 0.986449, 1.5337209), "StaticMeshActor18370", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (863.632, 5594.795, 5660.9297), (-39.233509261163384, 179.99117489258646, -10.163875728438462), (0.892838, 0.892838, 0.892838), "StaticMeshActor18371", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1229.4067, 4794.129, 5925.1665), (2.876843954505024, -82.61706752888358, -25.950043650046613), (0.817517, 0.817517, 0.817517), "StaticMeshActor18374", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1523.1055, 430.37158, 4459.269), (55.750802991217206, -66.60091622368778, 7.977269648764025), (1.018122, 1.018122, 1.018122), "StaticMeshActor18379", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (905.46484, 484.4224, 4715.6997), (20.233688054022647, -141.42954887988068, 21.114580338852203), (1.007587, 1.007587, 1.007587), "StaticMeshActor18401", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (998.07324, 313.32825, 5263.579), (20.233688054022647, -141.42954887988068, 21.114580338852203), (1.007587, 1.007587, 1.007587), "StaticMeshActor18402", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3872.153, 665.2955, 5237.6797), (-1.524017337488006, -6.748077956296856, 20.44734047366011), (1.051963, 1.3804617, 1.051963), "StaticMeshActor18505", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5856.518, 582.3578, 4477.545), (3.673493718404439, 174.11541146768417, -1.2114867400362643), (0.93539923, 0.80892, 0.9879294), "StaticMeshActor18552", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2036.7694, 2973.203, 6090.643), (0.5985570044930513, 85.33606832629464, 0.10244098696676403), (0.912821, 0.912821, 0.912821), "StaticMeshActor18559", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (6110.9336, 4032.545, 2453.1494), (-19.809905590302904, -29.54785222306242, -52.68744045413999), (0.832551, 0.832551, 0.832551), "StaticMeshActor18563", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4205.9517, 3456.5596, 6200.1465), (8.1009804348976, 177.7568909744933, -3.415008720311438), (1.066351, 1.066351, 1.066351), "StaticMeshActor18575", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3789.808, 3382.7847, 6047.4946), (-17.24520612707156, 173.89800876481857, -29.748931233075194), (1.2912083, 1.2912083, 1.2912083), "StaticMeshActor18576", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3076.3208, 3746.0688, 5058.2686), (34.91628748122702, 41.39751224838624, -17.214110076394864), (0.970266, 0.970266, 0.970266), "StaticMeshActor18588", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2866.627, 693.8892, 4922.013), (22.62609254005515, -124.16816286928035, -3.8211981967954443), (0.94769, 0.94769, 0.94769), "StaticMeshActor18596", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2812.3315, 3746.0688, 5058.2686), (2.316152140358136, -78.3964069320528, -175.84831621777712), (0.970266, 0.970266, 1.8154496), "StaticMeshActor18621", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5564.025, 1454.4072, 1312.0892), (-6.460236078237473, 137.3228852594263, -6.369507241223922), (0.831579, 0.831579, 0.831579), "StaticMeshActor18742", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5791.9854, 1128.0494, 1496.3157), (-24.0505985814568, -148.55650549538464, 5.9382659246435034), (1.087141, 1.087141, 1.087141), "StaticMeshActor18751", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5326.733, 4259.1377, 2520.1428), (-13.70614699377858, -164.03770296191811, 5.552360719329288), (0.9865631, 0.9865631, 0.9865631), "StaticMeshActor18760", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (6201.401, 372.9638, 4535.349), (6.234187032483747, 94.49605323534627, 0.7857142181323978), (0.930768, 0.930768, 0.930768), "StaticMeshActor18771", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5302.1245, 2509.5232, 809.3801), (-3.94070377608259, -86.96124656009708, 4.289409051163819), (0.957922, 0.957922, 0.957922), "StaticMeshActor18772", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (996.3459, 2210.413, 4187.4067), (16.048784974551975, 28.93565363245541, -3.95043842970095), (0.999262, 0.999262, 0.999262), "StaticMeshActor18773", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5704.9307, 1473.1656, 1842.1589), (-24.0505985814568, -148.55650549538464, 5.9382659246435034), (1.087141, 1.087141, 1.087141), "StaticMeshActor18774", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2220.652, 1378.0499, 6065.9995), (-8.53515625475996, 170.91358415651564, 7.89114819271301), (0.898575, 0.898575, 0.898575), "StaticMeshActor18775", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4344.202, 3873.7097, 6218.5376), (-5.333861611024639, -174.43332419354255, -3.7189636855095918), (0.880986, 0.880986, 0.880986), "StaticMeshActor18776", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1472.8619, 5059.1484, 5971.172), (2.876843954505024, -82.61706752888358, -25.950043650046613), (0.817517, 0.817517, 0.817517), "StaticMeshActor18777", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (741.33624, 2774.128, 2918.5293), (21.982099428598286, -174.02186252444142, -5.36605708799602), (1.036497, 1.036497, 1.036497), "StaticMeshActor18778", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3501.6895, 3358.7393, 4961.723), (-15.531003739546248, 110.06856176535055, 4.483445782722141), (0.34073818, 0.34073818, 0.34073818), "StaticMeshActor18780", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2934.3015, 467.25204, 4857.1455), (22.62609254005515, -124.16816286928035, -3.8211981967954443), (0.94769, 0.94769, 1.28782), "StaticMeshActor18790", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3208.9543, 409.43875, 4831.587), (7.43917577852677, 173.66070370661285, -21.750154403741824), (0.94769, 0.94769, 0.94769), "StaticMeshActor18791", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3424.97, 388.8293, 4760.916), (15.432921685217003, -163.5786512273569, -17.16821564476484), (0.94769, 0.94769, 1.1467752), "StaticMeshActor18798", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2636.4604, 702.2778, 4818.4316), (20.068597065309202, -144.59577181844298, -11.328367353733892), (0.94769, 0.94769, 0.94769), "StaticMeshActor18799", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1330.678, 284.4586, 4738.4746), (-12.883911748030428, 24.363256609783736, -3.3782960992013864), (1.033883, 1.033883, 1.033883), "StaticMeshActor18800", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3004.7012, 2353.6345, 1733.5997), (-6.546417509589136, 63.68214596644054, 3.527432160828901), (1.04659, 1.04659, 1.04659), "StaticMeshActor18834", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3022.5688, 2793.6155, 1671.8535), (0.041691485578183744, 153.34093809867298, -1.2072144820001154), (0.973282, 0.973282, 0.973282), "StaticMeshActor18835", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3010.093, 2982.826, 1388.4154), (-0.6056519118014088, 1.4617596448433792, 1.0451622613754719), (0.973282, 0.973282, 0.973282), "StaticMeshActor18836", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3447.7324, 4262.8296, 793.1199), (-1.6564023942353225, 124.18628186006187, 1.2390110591273638), (1.04659, 1.04659, 1.04659), "StaticMeshActor18838_25", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4888.2505, 3570.8872, 1544.0021), (19.255277550505028, 39.96425762759119, 157.90726164244342), (0.998987, 0.998987, 0.998987), "StaticMeshActor18841", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1209.7203, 5638.047, 991.2543), (0.0, 0.0, 4.99997770581576), (1.2, 1.2, 1.2), "StaticMeshActor18844", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (644.7012, 253.63452, 1733.5997), (-6.546416958699172, -96.6304375083031, 3.527464525471232), (1.0, 1.0, 1.0), "StaticMeshActor18846", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (644.7008, 253.63452, 1202.7899), (-6.546416931317888, -96.63043754862194, 3.5274650137602976), (1.0, 1.0, 1.0), "StaticMeshActor18847", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (645.44824, 6179.7393, 5279.07), (1.674119593915554, -106.53168026105517, 13.509142310802307), (1.288045, 0.986449, 2.0946925), "StaticMeshActor18848", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (6182.601, 5148.522, 5573.7695), (16.893793851087825, 74.59702706012207, -11.076933090714085), (1.062343, 1.062343, 1.062343), "StaticMeshActor18850_109", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (6143.176, 5626.1387, 4504.7886), (4.353350558983239, 143.72955336157528, 1.9493729743215031), (1.062343, 1.3115863, 1.062343), "StaticMeshActor18851", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (6043.7417, 5626.1387, 4990.1235), (8.586496304635897, 144.39206959434796, 7.82015308995772), (1.062343, 1.311586, 1.7021402), "StaticMeshActor18852", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (6247.8145, 5751.876, 4990.1235), (10.566006988566892, 120.20494338838498, 4.4128345761354275), (1.062343, 1.311586, 1.70214), "StaticMeshActor18853", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5847.834, 5350.857, 4291.3843), (8.327176677841619, 119.98908888895727, 3.0974655576340306), (1.062343, 1.311586, 1.4093255), "StaticMeshActor18854", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (6213.9077, 649.53174, 4174.801), (5.27548137150492, -88.8277069793064, 3.659034349709728), (1.1267604, 1.4259254, 1.5508994), "StaticMeshActor18855", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (6213.9077, 649.53174, 5506.5635), (5.322577232988492, -89.06545536848398, 1.0849136018015482), (1.12676, 1.425925, 1.550899), "StaticMeshActor18856", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5782.4062, 5363.9062, 4553.54), (8.586496081159627, 144.39206966070054, 7.820153893562094), (1.062343, 1.311586, 1.70214), "StaticMeshActor18857", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (6408.7744, 1139.2996, 5657.218), (-4.612272972848617, -176.79098213675195, 8.937313339195867), (1.1001263, 1.1001263, 0.26888272), "StaticMeshActor18859", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (6272.601, 1139.2996, 5657.218), (-4.612272972848617, -176.79098213675195, 8.937313339195867), (1.100126, 1.100126, 0.268883), "StaticMeshActor18860", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5436.7324, 5693.7393, 5033.0854), (-6.425231511097031, 69.21113655857489, 5.616682604755815), (1.3489131, 1.08325, 1.476947), "StaticMeshActor18861", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5333.9424, 6118.3374, 5695.6587), (-6.425231619996433, 88.15471946505191, 5.61690905024177), (1.348913, 1.08325, 1.476947), "StaticMeshActor18862", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5523.003, 6084.446, 5033.0854), (-1.8913877879689303, 6.456762140948354, 3.3265012984248914), (0.88625973, 1.8068315, 1.8782278), "StaticMeshActor18863", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3698.941, 4922.881, 1231.022), (-5.020812978478489, -86.48001169838226, -1.569519236810081), (1.01255, 1.01255, 1.01255), "StaticMeshActor18865", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2548.9065, 6189.4814, 834.20776), (5.94735919635856, 20.668668187708732, -1.3688047603562228), (0.990563, 0.990563, 0.990563), "StaticMeshActor18869", _folder)
if a: placed += 1
else: skipped += 1

# Batch 44: StaticMesh'PWM_Quarry_4x8x3' (1 instances)
_mesh_path = "/Game/Unshippable/Whitebox/Rocks/Meshes/PWM_Quarry_4x8x3"
_materials = ['/Game/Environments/ProcTexturing/ProcMaterial_Quarry_Atlas_A']
_folder = "Reconstruction/BD_BB_Passage_SpiralCave/Meshes"
a = spawn_static_mesh(_mesh_path, _materials, (3738.8928, 4986.449, 3851.917), (1.017090559561163, -9.863341719092977, -84.17050185755853), (0.5138561, 0.27657443, 0.36422732), "PWM_Quarry_4x8x3_13", _folder)
if a: placed += 1
else: skipped += 1

# Batch 45: StaticMesh'PWM_Quarry_5x4x10' (1 instances)
_mesh_path = "/Game/Unshippable/Whitebox/Rocks/Meshes/PWM_Quarry_5x4x10"
_materials = ['/Game/Environments/ProcTexturing/ProcMaterial_Quarry_Atlas_A']
_folder = "Reconstruction/BD_BB_Passage_SpiralCave/Meshes"
a = spawn_static_mesh(_mesh_path, _materials, (3407.971, 4209.5176, 3927.5005), (1.7878175800886098, -47.88339838650971, -88.38392513589534), (0.27527344, 0.16331235, 0.44473523), "PWM_Quarry_5x4x10_7", _folder)
if a: placed += 1
else: skipped += 1

# Batch 46: StaticMesh'PWM_Quarry_8x8x8_A' (170 instances)
_mesh_path = "/Game/Unshippable/Whitebox/Rocks/Meshes/PWM_Quarry_8x8x8_A"
_materials = ['/Game/Environments/ProcTexturing/ProcMaterial_Quarry_Atlas_2']
_folder = "Reconstruction/BD_BB_Passage_SpiralCave/Meshes"
a = spawn_static_mesh(_mesh_path, _materials, (5446.3394, 2030.4708, 344.20493), (-0.3895263073388176, -0.980865436406312, 5.518305738401344), (0.98533267, 0.98533267, 0.98533267), "StaticMeshActor_17464", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5595.9326, 1995.9963, 568.97095), (-1.551940818532009, -83.57879575137915, 0.7561701075039688), (0.9102844, 0.9102844, 0.9102844), "StaticMeshActor_17465", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2952.8784, 2872.5024, 306.9446), (-1.403503418812314, -178.59476947642742, 6.226727618514759), (1.0781057, 1.0781057, 1.0781057), "StaticMeshActor_17466", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4846.085, 5158.478, 2952.492), (6.869175799764773, -92.29523978529848, -2.589081025659678), (1.0992014, 1.0992014, 1.0992014), "StaticMeshActor_17467", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2238.949, 5890.583, 1154.0651), (0.0, 89.99999818714215, -0.0), (1.0, 1.0, 1.0), "StaticMeshActor_17468", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3139.156, 642.7726, 3501.682), (6.017672602521038e-10, 177.18749666023214, 0.7093136970182925), (1.1000928, 1.028247, 1.0), "StaticMeshActor_17469", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2394.6116, 403.76215, 3752.2388), (2.792557381203729, -176.98387831879742, -5.987305547506102), (0.8404758, 0.8404758, 0.8404758), "StaticMeshActor_17470", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2253.123, 824.5558, 3721.0117), (-1.5800474460856275, 70.12327747388105, -7.005888837943329), (0.8388933, 0.8388933, 0.8388933), "StaticMeshActor_17471", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5703.074, 2605.1455, 1943.8004), (-2.212157917120057, -179.92796199205907, -3.638061674340558), (0.943989, 0.943989, 0.943989), "StaticMeshActor_17472", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (6048.0845, 2524.3726, 2345.9644), (3.452921023015877, 140.8235941245532, -5.086792343504705), (1.0283846, 1.0283846, 1.0283846), "StaticMeshActor_17473", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5703.883, 2089.9858, 2298.3904), (3.564811519885161, 127.3045505454479, -12.672636664996602), (0.9243618, 0.9243618, 0.9243618), "StaticMeshActor_17474", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2042.5826, 5733.641, 1238.2334), (0.0, 15.000066558863706, -0.0), (1.0740237, 1.0740237, 1.0740237), "StaticMeshActor_17476", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (461.4911, 5195.4365, 3741.3545), (0.9711912272864489, 86.65579522722385, 7.91432060014328), (0.903299, 0.903299, 0.903299), "StaticMeshActor_17477", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (581.87646, 6010.8374, 3700.77), (0.08985118991509347, -85.50201909108002, 8.802259728825486), (0.82992285, 0.82992285, 0.82992285), "StaticMeshActor_17478", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3837.921, 5523.8022, 3471.6663), (-2.0835264442411825, 42.22198551097362, -1.8895874054593216), (0.99138933, 0.99138933, 0.99138933), "StaticMeshActor_17479", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5247.8735, 5251.693, 3723.355), (8.253115430710103, 175.1126998285751, 4.648309681541628), (0.95367926, 0.95367926, 0.95367926), "StaticMeshActor_17480", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (6009.459, 5769.802, 3932.1543), (-11.856840610164793, -27.83636286615278, 1.0824771709236203), (1.0753673, 1.0753673, 1.0753673), "StaticMeshActor_17481", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4155.349, 5685.139, 1232.4497), (0.0, 0.0, -0.0), (1.0, 1.0, 1.0), "StaticMeshActor_17482", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5788.88, 2747.0286, 3566.5664), (0.0, 8.437515534227996, -0.0), (1.0, 0.820406, 0.8204058), "StaticMeshActor_17483", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5439.31, 1049.7474, 3530.3643), (0.0, 134.9998858963921, -0.0), (1.0052017, 0.9735687, 0.9735687), "StaticMeshActor_17484", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (6250.0444, 401.65167, 3751.9138), (1.709739822416094, -95.97330910651756, -4.001587280010549), (0.8113065, 0.8113065, 0.8113065), "StaticMeshActor_17485", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4803.2017, 740.526, 3511.0183), (-3.227539286598258, 2.322267616475816, -7.306945879596155), (1.0389143, 0.9751898, 0.94513345), "StaticMeshActor_17486", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5790.73, 1297.1274, 557.5144), (-3.4846494829044388, -163.85958715603155, 2.71060984418887), (0.9457732, 0.9457732, 0.9457732), "StaticMeshActor_17487", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3925.2312, 4096.0693, 190.13452), (-6.034759213956742, -26.22107044291803, -8.811462595830369), (1.0225444, 1.0225444, 1.0225444), "StaticMeshActor_17488", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1973.218, 4707.5747, 375.66232), (-6.503021662263472, 2.1616591108243104, 7.527487506737165), (1.0350173, 1.0350173, 1.0350173), "StaticMeshActor_17489", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (891.16376, 5604.5986, 424.91287), (1.853413578599872, -85.94792879558155, -6.631896723476644), (0.9535238, 0.9535238, 0.9535238), "StaticMeshActor_17490", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1683.0117, 5435.738, 485.5836), (-1.77456650281394, 97.0249788909967, -5.408141831158905), (0.86584044, 0.86584044, 0.86584044), "StaticMeshActor_17491", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5551.4546, 4035.3562, 1003.2488), (0.0, -42.47771918144765, 0.0), (1.0424348, 1.0424348, 1.0424348), "StaticMeshActor_17492", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5196.226, 1377.6368, 3015.1638), (14.06203851689535, 0.42577333580658416, 2.9058075829475043), (0.918746, 0.918746, 0.918746), "StaticMeshActor_17494", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5596.5044, 1196.0812, 2960.0576), (-0.4557189656718322, 157.92170178739704, -6.439757087741299), (1.0471411, 1.0471411, 1.0471411), "StaticMeshActor_17495", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5674.988, 1776.043, 2684.6194), (-6.037598252991164, 150.5526304335546, 3.3505480725275434), (1.116634, 1.1295596, 1.1770332), "StaticMeshActor_17496", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2419.9082, 879.65314, 3091.7673), (17.80476981447055, -88.90790404336, -8.548554799825146), (0.81909865, 0.81909865, 0.81909865), "StaticMeshActor_17497", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2816.1921, 2978.6719, 3030.3225), (-5.259491110422406, 38.85917227792024, -4.106903473939656), (1.0685095, 1.0685095, 1.0685095), "StaticMeshActor_17498", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4994.0967, 4747.6836, 2206.112), (-9.251433677497358, 129.82055983678663, 7.566404342994573), (1.0907767, 1.0907767, 1.0907767), "StaticMeshActor_17499", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3195.5579, 4447.885, 619.1464), (-28.987337070857677, -115.12403973351968, 2.992047049082273), (0.9100589, 0.9100589, 0.9100589), "StaticMeshActor_17500", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4836.7505, 4563.2285, 862.68634), (4.507617734158656, 170.30049645081334, -7.3371894744826704), (1.0470052, 1.0089833, 0.9579253), "StaticMeshActor_17501", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3159.3933, 3817.95, 3590.1418), (-3.6054992167520665, 5.332786549528355, -6.695190283805583), (0.99446106, 0.99446106, 1.1699615), "StaticMeshActor_17502", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1335.7633, 1692.5143, 3826.844), (-0.9392384200451477, 119.42960439609375, -13.230283465839067), (1.0441451, 1.0441451, 1.0441451), "StaticMeshActor_17503", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1053.1461, 2103.223, 3752.6675), (-7.555449444524212, 109.72974126624213, -18.514159617009856), (0.99363685, 0.99363685, 0.99363685), "StaticMeshActor_17504", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (6097.443, 4139.128, 608.6256), (4.6808858254086205, 91.15888627405853, -3.619049554978823), (1.0945117, 1.0945117, 1.0945117), "StaticMeshActor_17505", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5798.8193, 4171.9844, 551.13074), (10.280520303083234, -11.93063391334035, -1.5595397058567453), (0.8558376, 0.8558376, 0.8558376), "StaticMeshActor_17506", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5721.941, 2266.4673, 641.6588), (-9.266966370046003, -166.20327594427138, -0.7957762721524072), (0.90280896, 0.90280896, 0.90280896), "StaticMeshActor_17507", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5685.1987, 4548.5493, 666.13794), (-2.1548767112330127, 146.33964974716005, 4.299629603190702), (0.8642075, 0.8642075, 0.8642075), "StaticMeshActor_17508", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2985.6729, 2574.499, 2257.1733), (-5.994170947950581, 133.44062040887638, -1.3217769703811397), (0.8557979, 0.8557979, 0.8557979), "StaticMeshActor_17509", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1305.2236, 890.2282, 2885.6335), (10.57781896956805, -1.1520994714728918, -25.31045433738655), (1.063973, 1.063973, 1.063973), "StaticMeshActor_17510", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2396.0637, 727.468, 2900.62), (6.997876279557492, 5.296597406739451, -31.2856125113158), (1.0144131, 1.0144131, 1.0144131), "StaticMeshActor_17511", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1602.8854, 942.56506, 3167.3787), (30.968451070955243, -101.74554270973192, -4.004240032153899), (0.88902074, 0.8497609, 0.8497609), "StaticMeshActor_17512", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5030.719, 989.36865, 2910.9673), (1.0707619838682103, -7.059479200527901, -1.2545471911824366), (1.0, 1.0, 1.0), "StaticMeshActor_17513", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5804.932, 1181.8965, 2444.6487), (0.4327748367159681, 98.17967953045213, 15.13232519803632), (1.0416464, 1.0833056, 1.0416464), "StaticMeshActor_17514", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1463.7993, 1375.937, 5816.9536), (-17.229401870570456, 136.34159358555456, -13.315489510341148), (1.0354698, 1.1544834, 1.1123775), "StaticMeshActor_17515", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1078.3804, 1811.3574, 5309.4937), (1.8302248533318741, -143.37081158648294, 15.166456467071235), (0.96261615, 0.96261615, 0.96261615), "StaticMeshActor_17516", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5088.345, 4730.014, 3023.0427), (-0.781555021276822, 134.6815748990671, -5.728942516925938), (0.9122292, 0.9122292, 0.9122292), "StaticMeshActor_17517", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2339.9158, 865.94147, 4609.7856), (8.196998273316215, -105.86277615311415, -9.113431797227173), (0.8723793, 0.82861495, 0.92777777), "StaticMeshActor_17518", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4133.633, 5380.8164, 2132.622), (-5.8076170095693005, 150.20232012486642, -2.918121161360222), (0.9981184, 0.96963304, 0.9473691), "StaticMeshActor_17519", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (585.2135, 2784.0378, 5583.242), (21.269143243000727, -171.0500778315959, -5.330627411325329), (0.97618556, 0.97618556, 0.97618556), "StaticMeshActor_17520", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2299.8772, 5650.3877, 2285.148), (9.665550654930103, 99.60667253063872, 3.3694502805070714), (1.0435554, 1.0435554, 1.0435554), "StaticMeshActor_17521", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3107.1162, 4279.747, 5733.0547), (18.362095439261424, 2.1035418154509355, -19.355745025706305), (0.8265251, 0.8265251, 0.8265251), "StaticMeshActor_17522", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5938.823, 2524.57, 3155.4673), (13.132758030230525, -122.65702349280839, -22.762421713769033), (0.9337318, 0.9337318, 0.9337318), "StaticMeshActor_17523", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5759.566, 2850.4192, 2938.8523), (-23.152437726312122, 157.79783589779186, 2.2097155860991173), (0.3, 0.95111907, 1.2641685), "StaticMeshActor_17524", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5761.703, 4569.929, 2938.25), (11.57381681012731, 72.8390495978444, -5.184021848227298), (1.0899615, 1.0899615, 1.0899615), "StaticMeshActor_17525", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (6046.803, 5615.7954, 5636.055), (-36.471559131400355, -52.47070331850608, -7.518127377182215), (1.0321715, 1.0321715, 1.0321715), "StaticMeshActor_17526", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (6174.0576, 6164.36, 4615.864), (-14.768826147331882, -63.47130984873835, -0.3702085479889532), (0.8610445, 0.8610445, 0.8610445), "StaticMeshActor_17527", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2588.369, 3224.722, 3123.6306), (8.264508949631486, 9.495842326428175, 22.332663260384262), (1.0564469, 1.0818622, 1.0), "StaticMeshActor_17528", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2211.142, 823.7155, 5492.968), (-5.772430693413358, 78.85201801709269, 29.819574888805512), (1.098831, 1.098831, 1.158527), "StaticMeshActor_17529", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5794.742, 59.984997, 4549.8374), (1.546709680047004, 23.54097574752505, 1.7266741506922507), (0.8092317, 0.8092317, 0.8092317), "StaticMeshActor_17530", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (663.01746, 5764.732, 1256.1874), (0.0, -85.00002983040224, 0.0), (0.85, 0.85, 0.85), "StaticMeshActor_17531", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5410.3867, 5248.912, 4442.467), (5.692571795862383, 179.14474959614594, -1.228515339301548), (1.0414121, 0.9604338, 0.94485927), "StaticMeshActor_17532", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5433.189, 5432.157, 4598.193), (-5.9940798406966325, -6.725616236729026, 15.26936153745102), (0.82420385, 0.82420385, 0.82420385), "StaticMeshActor_17533", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5602.8843, 5392.5034, 5575.981), (-7.832154022574204, -4.858672760833756, -48.71802027069181), (1.0787822, 1.0787822, 1.0787822), "StaticMeshActor_17534", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2187.87, 833.4259, 4259.1616), (-39.37482160074656, -42.18850214190397, 9.251834695855328e-05), (0.94949603, 0.94949603, 0.94949603), "StaticMeshActor_17535", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (421.83087, 1274.644, 4668.202), (-4.069824557662607, -81.72479704369792, 0.02571096681764096), (1.0555508, 1.0555508, 1.0555508), "StaticMeshActor_17536", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1506.5444, 374.7295, 5485.758), (-44.38635581028359, -107.61627351393237, 26.207475356495717), (0.866151, 0.866151, 1.0068444), "StaticMeshActor_17537", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2391.4575, 409.9157, 5358.9585), (14.76113450482921, -26.24780376635184, -3.5629585523279887), (1.0589901, 1.0589901, 1.0589901), "StaticMeshActor_17538", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2518.374, 4311.454, 5948.061), (20.400533768173982, 85.4720164794416, -8.996611997636853), (1.228449, 0.73006713, 0.80802023), "StaticMeshActor_17540", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1609.3773, 5532.3765, 3055.5986), (7.672925748209295, 94.67385936903551, 1.2049246083629803), (1.0015571, 1.0909008, 1.0314441), "StaticMeshActor_17541", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2367.558, 5605.58, 2932.1714), (3.4025825230683635, -78.82830285559274, 5.764346844168571), (0.90228796, 0.90228796, 0.90228796), "StaticMeshActor_17542", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (623.1759, 5538.321, 2467.1602), (0.21251533471509973, 22.860509423983245, -41.77685697638219), (0.83443743, 0.83443743, 0.83443743), "StaticMeshActor_17543", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (91.24772, 3607.2805, 2714.6882), (13.938890955028155, -5.02786157964465, 4.172158410724584), (0.83779234, 0.83779234, 0.83779234), "StaticMeshActor_17544", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (222.86987, 2802.7651, 2734.424), (-0.5911257172472038, -99.1461740252047, -8.754149953226618), (0.9543207, 1.0371363, 0.9543207), "StaticMeshActor_17545", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (120.34065, 1811.1814, 2855.222), (-0.5277414671988445, -86.53485195601237, 6.3273677467598555), (0.94158864, 0.94158864, 0.94158864), "StaticMeshActor_17546", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (660.5043, 972.9412, 2517.092), (-24.46661559683262, -77.03364481415545, -17.474918232983324), (0.8790876, 0.8790876, 0.8790876), "StaticMeshActor_17547", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (655.8856, 1840.5654, 3109.8674), (-3.84396334696655, -75.1109002055451, 18.475795976677436), (0.92190707, 0.92190707, 0.92190707), "StaticMeshActor_17548", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3216.2222, 262.0988, 2688.8882), (-2.507567882748926, -176.17972035880007, 22.845455651596147), (0.9707501, 0.9707501, 0.9707501), "StaticMeshActor_17549", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3264.8699, 686.7168, 2918.5127), (-25.82381731072251, -80.57289591847865, -10.329314895782568), (1.0358164, 1.0358164, 1.0358164), "StaticMeshActor_17550", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (515.1868, 1197.9924, 5159.951), (-3.1693117265088673, 83.73848620212165, -18.88900663242413), (1.080054, 1.0341572, 1.0341572), "StaticMeshActor_17551", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3994.6963, 6005.3657, 2076.0261), (6.604189660095026e-06, -89.99951842359357, -25.310122504447513), (0.81808645, 0.81808645, 0.81808645), "StaticMeshActor_17552", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4090.6975, 733.4279, 2923.6313), (1.369759920527437, 174.4417745318796, 19.405068677814928), (0.94891953, 0.94891953, 0.94891953), "StaticMeshActor_17553", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4005.204, 401.48877, 2961.4387), (1.1522868909302117, -178.85342422692256, 24.017365713266663), (1.0826036, 1.0826036, 1.0826036), "StaticMeshActor_17554", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4733.7783, 485.57547, 4046.4785), (4.909251845082752, -91.16559858727923, -6.021972549131105), (0.92910826, 0.92910826, 0.92910826), "StaticMeshActor_17555", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3901.3188, 807.85846, 5615.486), (1.4952646091572377, -13.609404973907397, 21.02176490608305), (0.8038471, 0.8038471, 0.8038471), "StaticMeshActor_17556", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2800.3037, 3467.0056, 4389.6855), (9.193243227392395, -118.0196936000268, 5.751047759998763), (0.95187813, 0.95187813, 0.95187813), "StaticMeshActor_17557", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3042.9714, 2986.784, 2238.9014), (-32.229802560023074, -3.1926884390711665, -7.375304838153862), (0.8548734, 0.8548734, 0.8548734), "StaticMeshActor_17561", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2555.415, 3053.9595, 5887.475), (13.159128228743656, -175.5638571773735, -23.23381974536546), (0.8158689, 0.8158689, 0.8158689), "StaticMeshActor_17563", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5594.2183, 4405.374, 1359.8003), (3.2888113353630493, 70.44109072745901, 1.3123078557926793), (0.88973445, 0.88973445, 0.88973445), "StaticMeshActor_17564", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4789.81, 5204.952, 2166.3206), (-10.11120534401318, 155.27301223091737, -3.60540820304425), (0.9222899, 0.9222899, 0.9222899), "StaticMeshActor_17565", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3202.84, 5699.0557, 2960.5444), (-11.118743061816865, 88.48782566016068, -4.51199402485768), (0.8362137, 0.8362137, 0.8362137), "StaticMeshActor_17566", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (576.2115, 5273.3564, 2948.7644), (-4.119292774391327, 54.65548095237276, -4.072296219958279), (0.95231736, 0.95231736, 0.95231736), "StaticMeshActor_17567", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1393.3336, 4380.575, 6132.9873), (-1.7164303755087391, -170.15566551837938, 7.661431411540371), (0.85240483, 0.85240483, 0.85240483), "StaticMeshActor_17568", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1382.2185, 4383.944, 6109.388), (-6.762510813349866, 170.91723336955, 10.281958061864733), (0.8596766, 0.8596766, 0.8596766), "StaticMeshActor_17569", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1361.7675, 5194.9707, 6287.172), (1.3632915981951315, -89.50054582064439, -13.826811283903773), (0.90864825, 0.90864825, 0.90864825), "StaticMeshActor_17570", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1060.2277, 3544.5981, 5903.465), (-26.22381279644819, 178.97000034171126, 7.519413906823787), (1.0721682, 1.1374569, 1.0721682), "StaticMeshActor_17571", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1312.4601, 2638.5742, 5997.721), (28.688675572938905, -6.0061942238536155, -21.127165319937145), (1.0038258, 0.93734, 0.93734), "StaticMeshActor_17572", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1601.1396, 6091.0527, 2552.1157), (-2.8648686769243596, -8.719178192033317, -60.976571076698264), (0.9200834, 0.9200834, 0.9200834), "StaticMeshActor_17573", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5877.474, 5897.6987, 5518.5337), (14.624563709876755, 70.02269440715631, 32.22874893960404), (1.0695953, 1.0695953, 1.0695953), "StaticMeshActor_17574", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3736.214, 3663.5457, 6173.8037), (-32.76684552516496, 176.61623533119675, -10.775299079531296), (0.8068062, 0.8068062, 0.8068062), "StaticMeshActor_17575", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3077.19, 3379.3367, 5487.4556), (-18.556396107581676, -75.14441057743716, -10.56979256439515), (1.08024, 1.08024, 1.08024), "StaticMeshActor_17576", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3193.025, 3602.9321, 6022.572), (29.083413232419296, -86.36070127565985, -18.858974389505327), (1.0052253, 1.0052253, 1.0052253), "StaticMeshActor_17577", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3185.891, 3056.7847, 3489.5776), (-2.263854526216823, 169.31324418423432, 8.612039943217644), (0.92152196, 0.92152196, 0.92152196), "StaticMeshActor_17578", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3392.3381, 3424.71, 3569.1755), (-2.031494293098921, 113.65119584420471, -2.456665242920046), (0.93339384, 0.93339384, 0.93339384), "StaticMeshActor_17579", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3212.8604, 5986.332, 2475.4077), (0.0, 0.0, 16.875068265369556), (0.87829757, 0.87829757, 0.87829757), "StaticMeshActor_17581", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (6003.031, 462.37866, 1416.7616), (2.458450953427336, 176.6024322995769, 2.5299566028692295), (1.0252486, 1.0252486, 1.1452311), "StaticMeshActor_17582", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (391.17978, 457.96924, 1426.9747), (-1.4028930651186613, -13.072416664306717, 3.159724143463024), (0.93466586, 0.93466586, 0.93466586), "StaticMeshActor_17583", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (515.5883, 4382.3066, 4515.595), (1.4864382886788394, 97.13067331046544, -6.760742151020942), (0.9954735, 0.9954735, 0.9954735), "StaticMeshActor_17584", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (337.04965, 5181.0244, 4599.661), (6.516887244479997, 5.418135622660067, 5.773739002081606), (0.9668009, 0.9668009, 1.212584), "StaticMeshActor_17585", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (710.3414, 2358.4246, 4763.615), (-13.419495451398149, 15.07950615093271, 1.8840223841776067), (1.0495334, 1.0495334, 1.0495334), "StaticMeshActor_17586", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (607.58624, 6010.6885, 5748.023), (-33.71502394399462, -178.27258626802535, 6.114733332746353), (0.8412614, 0.8412614, 0.8412614), "StaticMeshActor_17587", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4005.0493, 6135.2183, 5971.324), (3.414629298072647, 173.15656916397663, -5.39785666280427), (1.1184219, 0.9954027, 0.9456402), "StaticMeshActor_17588", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3177.1636, 6111.1196, 5983.1426), (-4.455627755376665, 93.29430158616722, -8.314575695558545), (0.96744645, 0.98904014, 0.85007167), "StaticMeshActor_17589", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2380.5662, 5769.448, 5989.7), (-10.986542177705253, 86.69818041548785, -5.105469183137961), (0.93886626, 1.4450785, 0.93886626), "StaticMeshActor_17590", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3132.735, 5245.3604, 6131.307), (12.930128680462413, 3.6204149764804536, -2.859497315423406), (0.90709573, 0.90709573, 0.90709573), "StaticMeshActor_17591", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1435.2545, 6059.5176, 6025.7056), (-10.399018086747496, 170.4737043835855, -9.014527625122808), (0.954191, 0.954191, 0.954191), "StaticMeshActor_17592", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2423.5955, 5205.3975, 6120.4395), (0.45612000256509927, 3.227657847638925, 8.402460867544889), (0.8670635, 0.8670635, 0.8670635), "StaticMeshActor_17593", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2390.395, 5203.2856, 6151.0874), (-2.3095704271266873, -97.81810745075016, 4.2398282376607535), (1.0860188, 1.0860188, 1.0860188), "StaticMeshActor_17594", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4789.2104, 2810.5583, 6179.811), (4.20124181146837, 91.81044021727138, -8.347136884427085), (0.8921951, 0.8921951, 0.8921951), "StaticMeshActor_17595", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5599.1655, 4401.795, 6056.2974), (15.795975950275286, -93.90511622819268, 16.172473364856966), (1.0633876, 1.0633876, 1.0633876), "StaticMeshActor_17596", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5667.3877, 2794.3408, 6007.606), (-4.227721889174125, 86.85484989968256, 0.4905834794869886), (0.9391254, 0.87184054, 0.87184054), "StaticMeshActor_17597", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (6168.298, 4551.246, 6070.8896), (-7.722900914085503, 173.64656298722872, -12.667787837636764), (0.9142964, 0.9142964, 0.9142964), "StaticMeshActor_17598", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (6206.3105, 3601.9426, 5999.4766), (-6.5562433738785595, -2.5881956025389594, -3.910034251089459), (0.99482024, 0.99482024, 0.99482024), "StaticMeshActor_17599", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (6219.8823, 2795.208, 5996.0977), (7.119030928338916, 4.806339341556001, -7.805726324380063), (0.8630072, 0.8630072, 0.8630072), "StaticMeshActor_17600", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5642.7505, 1857.0126, 6064.85), (12.870479799756131, 90.76094995294376, -9.722717184386202), (0.9571983, 0.9571983, 0.9571983), "StaticMeshActor_17601", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4825.6475, 1942.912, 5975.097), (-6.2594297172363165, -83.70459566048876, 8.99370200815681), (1.0638876, 1.0638876, 1.1061157), "StaticMeshActor_17602", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4792.457, 1207.6698, 6161.543), (-27.40462981542756, -90.51619496122767, 13.869965290790754), (0.8844176, 0.8844176, 0.8844176), "StaticMeshActor_17603", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3975.1804, 1042.9812, 6098.885), (-8.5752560873744, -1.5413209575338904, -30.341461993585845), (0.8178592, 0.8178592, 0.8178592), "StaticMeshActor_17604", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3997.2275, 1960.3942, 6243.779), (0.1125411642812939, 80.03824260646488, -4.382782171318047), (0.8151838, 0.8151838, 0.8151838), "StaticMeshActor_17605", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3140.3457, 2013.8195, 6195.097), (-3.82281527175274, -91.65271576659477, 1.7142037284340188), (0.87239736, 0.87239736, 0.87239736), "StaticMeshActor_17606", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2401.551, 2117.07, 6026.7017), (1.8876660012741047, 2.4629222961721653, -6.944855042498615), (1.0755398, 1.0755398, 1.0755398), "StaticMeshActor_17607", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5715.4106, 1968.4005, 3553.446), (-5.571014081189992, 84.37541770172201, 1.1008818884100784), (1.0, 0.820406, 0.820406), "StaticMeshActor17493", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (6030.44, 3452.878, 2944.9897), (-18.95114127231045, 168.8339870685924, -2.147277909035938), (0.45, 0.951119, 1.264169), "StaticMeshActor17539", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3038.0386, 2643.2944, 1125.8685), (-10.257474314741568, -4.249358698076044, -175.230070512334), (0.89530027, 0.855798, 0.855798), "StaticMeshActor17558", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2628.379, 3778.194, 3643.8894), (0.0, 73.1250088920844, -0.0), (0.93135685, 0.91818863, 0.886616), "StaticMeshActor17559_152", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1116.8583, 5424.255, 3520.8477), (2.8124945172626328, -78.74941171762848, 1.828696015935745e-06), (1.0, 1.0, 1.0), "StaticMeshActor17560", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5411.3755, 5876.295, 4358.4155), (-5.692107949760977, -0.8538513124562179, 1.2284145613571358), (1.0, 1.0, 1.0), "StaticMeshActor17562", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4952.6753, 4101.5933, 190.13416), (-6.034759213956742, -26.22107044291803, -8.811462595830369), (1.022544, 1.022544, 1.022544), "StaticMeshActor17580", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (663.01746, 5764.732, 1941.228), (0.7009826995629359, -94.950201065271, -171.9584768058603), (0.85, 0.85, 0.85), "StaticMeshActor18320", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3132.735, 4795.3604, 6131.307), (12.930128680462413, 3.6204149764804536, -2.859497315423406), (0.907096, 0.907096, 0.907096), "StaticMeshActor18349", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (490.3473, 4382.3066, 4884.9043), (1.4864380617162662, 97.13067333270396, -6.760742409637597), (0.995474, 1.039896, 0.995474), "StaticMeshActor18373", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (831.24585, 2175.7986, 5309.4937), (1.8302248533318741, -143.37081158648294, 15.166456467071235), (0.962616, 0.962616, 0.962616), "StaticMeshActor18375", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5362.418, -97.85185, 4549.8374), (1.5467095998837719, -158.25953822566035, 1.7266869310612762), (0.809232, 0.809232, 0.809232), "StaticMeshActor18522", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5362.418, 230.097, 4549.8374), (1.5467099749276114, 95.33608070486801, 1.7266987559925706), (0.809232, 0.809232, 0.809232), "StaticMeshActor18527", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5362.418, 230.097, 5097.884), (1.546709816519377, 95.33608070446479, 1.7266989002901785), (0.809232, 0.809232, 0.809232), "StaticMeshActor18528", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4794.946, 328.3297, 4549.8374), (1.5467099812090592, 69.67320946421793, 1.7267033355867032), (0.809232, 0.809232, 0.809232), "StaticMeshActor18531", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4794.946, 328.3297, 5097.884), (1.5467099812090592, 69.67320946421793, 1.7267033355867032), (0.809232, 0.809232, 0.809232), "StaticMeshActor18532", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4241.6855, 494.48907, 4549.8374), (1.5467099550164547, 65.64781949828846, 1.7267042449577006), (0.809232, 0.809232, 0.809232), "StaticMeshActor18537", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4241.6855, 494.48907, 5097.884), (1.5467099550164547, 65.64781949828846, 1.7267042449577006), (0.809232, 0.809232, 0.809232), "StaticMeshActor18551", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2035.658, 4380.575, 6095.2896), (-1.7164304497396854, -170.15566551126696, 7.661430941985463), (1.0204514, 1.0204514, 1.0204514), "StaticMeshActor18553", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3605.2039, 2151.8645, 6243.779), (0.1125411642812939, 80.03824260646488, -4.382782171318047), (0.815184, 0.815184, 0.815184), "StaticMeshActor18554", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3605.2039, 1603.4178, 6243.779), (0.1125411642812939, 80.03824260646488, -4.382782171318047), (0.815184, 0.815184, 0.815184), "StaticMeshActor18555", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4318.127, 1603.4178, 6243.779), (0.1125411642812939, 80.03824260646488, -4.382782171318047), (0.815184, 0.815184, 0.815184), "StaticMeshActor18556", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2842.6548, 1596.491, 6185.097), (-3.8228153472502218, -91.65271578989727, 1.714204135631582), (0.872397, 0.872397, 0.872397), "StaticMeshActor18557", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1312.46, 2021.1748, 5888.1685), (28.688675572938905, -6.0061942238536155, -21.127165319937145), (0.93734, 0.93734, 0.93734), "StaticMeshActor18558", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2408.4104, 2578.222, 6148.899), (13.159128228743656, -175.5638571773735, -23.23381974536546), (0.815869, 0.93742967, 0.815869), "StaticMeshActor18560", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (6106.326, 3388.5476, 2131.282), (-7.231566448131101, 179.18526075834967, 4.727153493790129), (0.943989, 0.943989, 0.50392455), "StaticMeshActor18561", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5821.8896, 4022.6055, 2131.282), (-7.231566448131101, 179.18526075834967, 4.727153493790129), (0.943989, 0.943989, 0.503925), "StaticMeshActor18562", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3191.4016, 807.85895, 5615.486), (73.09957903311438, 77.75652910555533, 87.44389409287709), (0.8936204, 0.803847, 1.1950976), "StaticMeshActor18577", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (6231.0576, 3512.8074, 1563.2826), (-6.922761898822365, -177.75145367192545, -19.7618766080169), (0.943989, 0.943989, 0.503925), "StaticMeshActor18769", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (6251.0576, 2791.0713, 1538.7335), (-7.077086830740904, 178.30144714863232, 11.81080351039936), (0.943989, 0.943989, 0.503925), "StaticMeshActor18770", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3502.292, 4190.0093, 3710.2485), (-3.934020598752658, 2.4865098224243187, -6.508239158156558), (0.10748148, 0.15784591, 0.25572693), "StaticMeshActor18779", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5862.206, 3179.1785, 3573.2046), (0.0, 8.437515534227996, -0.0), (1.0, 0.820406, 0.820406), "StaticMeshActor18788", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5705.1484, 5982.1216, 5062.9023), (-5.692108109322651, -21.017884487782073, 1.2284185151396623), (0.7036788, 0.7036788, 0.9317472), "StaticMeshActor18849", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (6158.298, 5121.815, 6047.5923), (-4.487029963109343, 171.06664963452738, 11.22605443539247), (0.914296, 0.914296, 0.914296), "StaticMeshActor18858", _folder)
if a: placed += 1
else: skipped += 1

# Batch 47: StaticMesh'PWM_Quarry_Ceilling_Fissure_8x4_A' (5 instances)
_mesh_path = "/Game/Unshippable/Whitebox/Rocks/Meshes/PWM_Quarry_Ceilling_Fissure_8x4_A"
_materials = ['/Game/Environments/ProcTexturing/ProcMaterial_Quarry_Floor_8x4x1']
_folder = "Reconstruction/BD_BB_Passage_SpiralCave/Meshes"
a = spawn_static_mesh(_mesh_path, _materials, (1104.0754, 5859.7114, 2145.0337), (-11.807644598416166, -176.30812119600108, 156.21013884642008), (1.0, 1.336895, 1.0), "PWM_Quarry_Ceilling_Fissure_8x4_A_252", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1098.2482, 5631.515, 2243.1406), (-11.807644598416166, -176.30812119600108, 156.21013884642008), (1.0, 1.336895, 1.0), "PWM_Quarry_Ceilling_Fissure_8x4_A2", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1412.224, 5651.764, 2308.9182), (14.613135187219784, 172.10203834777772, 164.98473515718968), (1.0, 1.336895, 1.0), "PWM_Quarry_Ceilling_Fissure_8x4_A3", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1426.0393, 5848.019, 2257.972), (14.613135187219784, 172.10203834777772, 164.98473515718968), (1.0, 1.336895, 1.0), "PWM_Quarry_Ceilling_Fissure_8x4_A4", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3310.432, 5428.732, 919.7807), (2.997121736481727, 3.6905786022835056, -178.95991191959223), (2.2111223, 1.9734257, 1.7435861), "StaticMeshActor18866_33", _folder)
if a: placed += 1
else: skipped += 1

# Batch 48: StaticMesh'PWM_Quarry_Floor_2x2x2_A' (12 instances)
_mesh_path = "/Game/Unshippable/Whitebox/Rocks/Meshes/PWM_Quarry_Floor_2x2x2_A"
_materials = ['/Game/Environments/ProcTexturing/ProcMaterial_Quarry_Atlas_3']
_folder = "Reconstruction/BD_BB_Passage_SpiralCave/Meshes"
a = spawn_static_mesh(_mesh_path, _materials, (3210.0, 164.54645, 4496.7363), (0.0, 0.0, -1.6967774327634226), (1.6875, 1.98096, 1.0), "PWM_Quarry_Floor_2x2x2_A_12", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2450.3872, 4370.8237, 1183.8495), (6.193555542477742, 0.5049079978498955, 4.669678885364435), (1.370378, 0.810025, 1.25702), "PWM_Quarry_Floor_2x2x2_A10", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (987.1326, 6068.964, 1787.7526), (-14.576202709723972, -23.698885385246008, 1.0002463164696912e-05), (1.0, 1.6807872, 2.6372201), "PWM_Quarry_Floor_2x2x2_A11_246", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1391.583, 6283.2456, 1861.7485), (-6.725188807251653, -86.73101618541772, 2.070495985989274), (1.0, 1.9536908, 2.63722), "PWM_Quarry_Floor_2x2x2_A12", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (105.0, 3190.0, 4485.0), (-3.288264841619148e-08, -90.1815208113296, -1.6967773752516035), (1.9375, 1.25, 0.9375), "PWM_Quarry_Floor_2x2x2_A2", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2850.5212, 2094.4856, 1367.0309), (0.0, 0.0, 12.438039941357964), (1.0, 1.0, 1.9349017), "PWM_Quarry_Floor_2x2x2_A3_112", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2946.2847, 4328.37, 1049.3617), (0.7024098041266587, -10.46203554105937, 5.000459308962505), (1.2043657, 1.0, 2.1829073), "PWM_Quarry_Floor_2x2x2_A4_184", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3250.9583, 4281.1284, 1415.4465), (-0.10031127137898226, -14.532653650081574, 0.6594592411343848), (1.5427089, 1.0, 1.2399421), "PWM_Quarry_Floor_2x2x2_A5", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2434.1882, 4373.75, 1011.4546), (6.193555562055955, 0.5049075148479443, 4.669678859233732), (1.3703775, 1.0, 1.2570198), "PWM_Quarry_Floor_2x2x2_A6_195", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2675.8896, 4350.372, 1011.4546), (6.193555542477742, 0.5049079978498955, 4.669678885364435), (1.370378, 1.0, 1.25702), "PWM_Quarry_Floor_2x2x2_A7", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2776.9563, 4370.8237, 1289.3834), (6.193555542477742, 0.5049079978498955, 4.669678885364435), (1.370378, 1.0, 1.25702), "PWM_Quarry_Floor_2x2x2_A8", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2577.9883, 4370.8237, 1237.0479), (6.193555542477742, 0.5049079978498955, 4.669678885364435), (1.370378, 0.8100246, 1.25702), "PWM_Quarry_Floor_2x2x2_A9", _folder)
if a: placed += 1
else: skipped += 1

# Batch 49: StaticMesh'PWM_Quarry_Floor_4x4x4_A' (3 instances)
_mesh_path = "/Game/Unshippable/Whitebox/Rocks/Meshes/PWM_Quarry_Floor_4x4x4_A"
_materials = ['/Game/Environments/ProcTexturing/ProcMaterial_Quarry_Atlas_4']
_folder = "Reconstruction/BD_BB_Passage_SpiralCave/Meshes"
a = spawn_static_mesh(_mesh_path, _materials, (1205.1198, 5651.453, 1183.3054), (-4.767516988543952, 1.9156778239163663, -16.689147023634305), (1.0, 1.0, 1.0), "PWM_Quarry_Floor_4x4x4_A_261", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1490.5687, 5652.2383, 1188.8524), (7.403517449612928, -1.7362060210369497, -16.77404935842089), (1.0, 1.0, 1.0), "PWM_Quarry_Floor_4x4x4_A2", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1194.0665, 6037.32, 1305.874), (-10.242432142428088, 3.4414996506345625, -25.423920025471787), (1.0, 1.0, 1.0), "PWM_Quarry_Floor_4x4x4_A3", _folder)
if a: placed += 1
else: skipped += 1

# Batch 50: StaticMesh'PWM_Quarry_Floor_6x2x1_A' (63 instances)
_mesh_path = "/Game/Unshippable/Whitebox/Rocks/Meshes/PWM_Quarry_Floor_6x2x1_A"
_materials = ['/Game/Environments/ProcTexturing/ProcMaterial_Quarry_Atlas_4']
_folder = "Reconstruction/BD_BB_Passage_SpiralCave/Meshes"
a = spawn_static_mesh(_mesh_path, _materials, (4462.4487, 3429.843, 1945.0), (5.467473839165347e-13, 81.56248286295717, 2.6255846002620076e-05), (1.0, 1.0, 1.0), "PWM_Quarry_Floor_6x2x1_A_16", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4913.2256, 3758.5571, 1953.4982), (-2.6072387969721937, -157.1686664088961, -155.8903556290092), (1.0, 1.0, 1.0), "PWM_Quarry_Floor_6x2x1_A10", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4641.525, 3638.1658, 1944.3018), (-2.818176546767233, 16.889944889779855, 171.5623477487783), (1.0, 1.0, 1.0), "PWM_Quarry_Floor_6x2x1_A11", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2178.5369, 2787.4856, 3842.8093), (14.679655043884578, 173.36439628637683, 2.3033156172255946), (1.5, 1.5, 1.5), "PWM_Quarry_Floor_6x2x1_A12_157", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2587.0298, 2763.027, 3694.2349), (-24.80581719980273, -35.652344184286584, -12.292695645522825), (1.5, 1.5, 1.5), "PWM_Quarry_Floor_6x2x1_A13", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2997.164, 2314.14, 3355.0), (-2.9530471377832682e-05, 25.30778747239689, -42.18664599020652), (1.0, 1.0, 1.0), "PWM_Quarry_Floor_6x2x1_A14_161", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2826.0718, 2570.8198, 3557.6755), (16.874953897535093, 143.4367358295064, -179.9999866157178), (1.5, 1.5, 1.5), "PWM_Quarry_Floor_6x2x1_A15", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3410.0, 4235.0, 3965.0), (-2.3381959612759577, 33.782352312381896, -1.5633853641756448), (1.0, 1.0, 1.0), "PWM_Quarry_Floor_6x2x1_A16_169", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3590.0, 4125.0, 3925.0), (3.743052908945173, 64.80050099938579, 1.3438996045964675), (1.0, 1.0, 1.0), "PWM_Quarry_Floor_6x2x1_A17", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3931.2969, 4682.37, 3217.4207), (-1.1812134416756193, -44.804933024284175, 6.7829689862566385), (1.0, 1.0, 1.6694565), "PWM_Quarry_Floor_6x2x1_A18_173", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3815.4697, 4995.658, 3247.3145), (-9.43649354854377, 77.1643741846449, -7.041229601908958), (1.0, 1.0, 1.0), "PWM_Quarry_Floor_6x2x1_A19", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4496.7188, 3187.0981, 1977.7822), (-1.9748535541543775, -50.85711698386775, -174.43251007472418), (0.84375, 0.84375, 0.84375), "PWM_Quarry_Floor_6x2x1_A2", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4265.0015, 4730.419, 3249.9824), (3.8741843371536775, -126.56461253759728, 177.15023236742755), (1.0, 1.0, 1.0), "PWM_Quarry_Floor_6x2x1_A20", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4915.6216, 4489.9062, 3446.702), (-1.7434383273176641, 121.75983282464338, -11.627654209697088), (1.0, 1.0, 1.0), "PWM_Quarry_Floor_6x2x1_A21", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5129.547, 4195.4116, 3513.993), (12.757988684772984, -55.92896253880425, 11.923832263925075), (1.0, 1.0, 1.0), "PWM_Quarry_Floor_6x2x1_A22", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5296.492, 3901.8608, 3580.5688), (-7.814117709932795, 99.64104878850937, 6.7471070564456435), (1.0, 1.0, 1.0), "PWM_Quarry_Floor_6x2x1_A23", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4976.696, 4130.563, 2548.041), (5.624981191300521, 149.0623485682908, 3.0249951894197743e-05), (1.0, 1.0, 1.0), "PWM_Quarry_Floor_6x2x1_A24", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5344.602, 2595.0032, 2256.8765), (-10.300873563391116, 77.79755450318561, 8.41206530830879), (1.4403256, 1.5981405, 1.9005461), "PWM_Quarry_Floor_6x2x1_A26", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2042.4473, 1502.3938, 4220.0), (-3.7741705080359362, 132.0498897140429, 4.17389844575209), (1.0, 1.0, 1.0), "PWM_Quarry_Floor_6x2x1_A27", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3751.5847, 2878.7402, 3749.8252), (-27.2277850836395, -113.68700863048484, 14.678872861691378), (1.2, 1.2, 1.2), "PWM_Quarry_Floor_6x2x1_A28", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3663.744, 3140.393, 3906.3816), (-6.26437371069738, -3.0654294260049695, -8.868560200661227), (1.0, 1.0, 1.0), "PWM_Quarry_Floor_6x2x1_A29", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4958.4214, 3009.535, 1950.5878), (-2.1571653523523597, -11.227415823299312, -167.7077731114886), (1.0, 1.0, 1.0), "PWM_Quarry_Floor_6x2x1_A3", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3591.0293, 2827.315, 3761.639), (-33.279905989692985, -96.97156445310321, -162.5548502266988), (1.2, 1.2, 1.2), "PWM_Quarry_Floor_6x2x1_A30", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2689.1797, 2662.544, 3514.725), (-19.618255725410656, -55.107480087245904, -19.082608115740133), (2.0, 2.0, 2.0), "PWM_Quarry_Floor_6x2x1_A31", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1976.3462, 1693.6749, 4213.4937), (3.564990264144005, -50.76123826492959, -4.35382119404356), (1.0, 1.0, 1.0), "PWM_Quarry_Floor_6x2x1_A32", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2728.7463, 5466.058, 3920.6858), (-5.195251784538324, -179.61214014339694, -8.137938801800553), (1.5, 1.5, 1.5), "PWM_Quarry_Floor_6x2x1_A33", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2071.2002, 5278.8604, 3926.4978), (-1.5824279856224137, 11.529599765565527, 5.172520581989392), (1.5, 1.5, 1.5), "PWM_Quarry_Floor_6x2x1_A34", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1100.717, 5109.822, 3904.1475), (-2.8008426091949783, 177.20471378426922, -7.846862903870388), (1.5, 1.5, 1.5), "PWM_Quarry_Floor_6x2x1_A35", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3697.085, 5374.4673, 3922.2563), (4.8620035564273645e-08, -19.27459875568813, 5.920442264605296), (1.5, 1.5, 1.5), "PWM_Quarry_Floor_6x2x1_A36", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3183.9055, 5483.543, 3922.3462), (-2.0227656365428612, -13.941772736034096, 5.356196750871096), (1.5, 1.5, 1.5), "PWM_Quarry_Floor_6x2x1_A37", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3625.0437, 2642.9478, 3618.795), (30.659637573645252, 95.05080910773039, -0.537567080945363), (1.2, 1.2, 1.2), "PWM_Quarry_Floor_6x2x1_A38_35", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3764.7908, 5120.972, 3917.5337), (0.2751296211360429, -95.61733162938457, -177.2006138616806), (1.1643283, 1.0, 1.0), "PWM_Quarry_Floor_6x2x1_A39", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (285.0, 5505.0, 820.0), (0.0, 144.99998898772822, -0.0), (1.25, 1.25, 1.25), "PWM_Quarry_Floor_6x2x1_A4_28", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5405.532, 2549.9343, 3913.0505), (-1.7242734632995758, -95.09690650307319, 8.906354703244897), (1.0, 1.141264, 1.2094558), "PWM_Quarry_Floor_6x2x1_A40_2", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5441.318, 1858.2786, 3950.7642), (-1.7242734632995758, -95.09690650307319, 8.906354703244897), (1.0, 1.0, 1.0), "PWM_Quarry_Floor_6x2x1_A41", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4755.8164, 1072.0293, 3955.8677), (-4.502654231168254, 174.46645442451342, 8.931800069156429), (1.0, 1.0, 1.0), "PWM_Quarry_Floor_6x2x1_A42", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5426.318, 3068.2786, 3960.7642), (-4.978027140813139, 82.53591078329949, 0.6978824009412398), (1.0, 1.0, 1.0), "PWM_Quarry_Floor_6x2x1_A43", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5406.148, 3964.1846, 3948.7017), (-6.36062558549499, 100.10248036248112, -8.627899315404557), (1.0, 1.0, 1.0), "PWM_Quarry_Floor_6x2x1_A44", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5311.318, 1373.2786, 3955.7642), (-5.657227397042755, 45.78995401189643, -0.7487794499698324), (1.0, 1.0, 1.0), "PWM_Quarry_Floor_6x2x1_A45", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2836.889, 1020.2805, 3954.958), (-3.487426797238447, -16.89126641539048, 5.905258227469279), (1.0, 1.0, 1.0), "PWM_Quarry_Floor_6x2x1_A46_22", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4278.2393, 5177.4087, 3956.3574), (-4.340301470191048, 142.59407019692807, 9.295340361754691), (1.25, 1.25, 1.25), "PWM_Quarry_Floor_6x2x1_A47", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4398.519, 4604.486, 2968.1914), (0.13794931203977148, -5.621917873540231, 2.809105994885661), (1.0, 1.0, 1.0), "PWM_Quarry_Floor_6x2x1_A48", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5351.014, 2573.9006, 2150.8474), (-10.300873563391116, 77.79755450318561, 8.41206530830879), (1.440326, 1.59814, 1.900546), "PWM_Quarry_Floor_6x2x1_A49", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1454.9701, 5412.4263, 1259.1235), (-2.2583922435651917, 174.05876149625587, 14.781537381770129), (1.0, 1.0, 1.0), "PWM_Quarry_Floor_6x2x1_A5", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1588.6241, 5018.075, 1156.0634), (-5.610930860299799, 95.64532779759655, -0.2768250422271092), (1.25, 1.25, 1.25), "PWM_Quarry_Floor_6x2x1_A50", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2142.2378, 4431.9346, 1211.8021), (14.277285456537358, -19.476500037984252, 5.65537858282138), (1.0, 1.0, 1.0), "PWM_Quarry_Floor_6x2x1_A51", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5457.077, 2251.067, 3895.254), (-2.6329654422885227, 82.5693423295992, -2.3203735636254224), (1.9902047, 1.9902047, 1.9902047), "PWM_Quarry_Floor_6x2x1_A53", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2850.729, 1147.4697, 3349.3652), (-2.44116191433476, -25.670438567984995, 16.704511522533988), (1.0, 1.0, 1.0), "PWM_Quarry_Floor_6x2x1_A54_20", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3215.3687, 1108.9642, 3323.022), (-7.019378378528509, 171.83966908048407, -16.92474458030883), (1.0, 1.0, 1.0), "PWM_Quarry_Floor_6x2x1_A55", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3669.091, 1076.0347, 3375.3472), (0.7771456198191047, -172.90539670849637, 159.007186202695), (1.0, 1.0, 1.0), "PWM_Quarry_Floor_6x2x1_A56", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4077.2788, 1047.9661, 3373.659), (7.665234782381897, -7.808105692389237, -160.6007456226019), (1.0, 0.7652123, 1.0), "PWM_Quarry_Floor_6x2x1_A57", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4285.1187, 1142.9846, 3319.512), (-6.413085815820923, 13.975768226801435, 20.906162378615587), (1.0, 1.0, 1.0), "PWM_Quarry_Floor_6x2x1_A58", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4688.866, 4747.2563, 3552.3145), (0.0, 30.00015437767157, -0.0), (1.5, 1.5, 1.5), "PWM_Quarry_Floor_6x2x1_A59", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1102.0145, 5420.398, 1275.2942), (-7.409331559687627, -3.38119535583628, -14.901579560381395), (1.0, 1.0, 1.0), "PWM_Quarry_Floor_6x2x1_A6", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5030.0156, 4403.4893, 3562.3145), (0.0, -124.9998251408764, 0.0), (1.5, 1.582994, 1.5), "PWM_Quarry_Floor_6x2x1_A60", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4908.4263, 4644.8223, 3697.124), (-0.0003662109118218153, 130.00155842250842, 0.00013765248134974778), (1.5, 2.09375, 2.0), "PWM_Quarry_Floor_6x2x1_A61_8", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3160.0, 149.14578, 3938.2588), (-2.2605896943469217, -11.372161846544707, 2.760570393847243), (1.0, 1.0, 1.0), "PWM_Quarry_Floor_6x2x1_A64", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4086.394, 5310.813, 3970.08), (6.884119715111494e-08, -19.274598762509477, 5.920442727937126), (0.65732336, 0.65732336, 0.65732336), "PWM_Quarry_Floor_6x2x1_A65", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4633.3677, 4996.527, 3997.9326), (-4.340301833884358, 142.59407016308248, 9.295339266727265), (1.25, 1.25, 1.25), "PWM_Quarry_Floor_6x2x1_A66", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4893.6104, 4597.143, 3581.124), (-0.0003051757478102588, 120.03854459359576, 0.00019545047428708715), (0.6953778, 2.09375, 2.0), "PWM_Quarry_Floor_6x2x1_A67", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2937.4866, 4372.753, 1474.5957), (15.000004886260893, 5.445984592879747e-05, -159.99956968563257), (1.0, 1.0, 1.0), "PWM_Quarry_Floor_6x2x1_A7", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3168.4604, 4314.3794, 1536.5306), (-24.41430322816603, 166.5058194778265, 163.92526974072854), (1.0, 1.0, 1.0), "PWM_Quarry_Floor_6x2x1_A8", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4669.815, 3743.4531, 1900.6127), (-8.161957308115712, 22.619719231931782, -92.68121573459523), (1.0, 1.0, 1.0), "PWM_Quarry_Floor_6x2x1_A9", _folder)
if a: placed += 1
else: skipped += 1

# Batch 51: StaticMesh'PWM_Quarry_Floor_8x4x1_A' (10 instances)
_mesh_path = "/Game/Unshippable/Whitebox/Rocks/Meshes/PWM_Quarry_Floor_8x4x1_A"
_materials = ['/Game/Environments/ProcTexturing/ProcMaterial_Quarry_Atlas_6']
_folder = "Reconstruction/BD_BB_Passage_SpiralCave/Meshes"
a = spawn_static_mesh(_mesh_path, _materials, (5555.1987, 3580.8508, 740.0), (0.0, -1.3760070183516615, 0.0), (1.0, 1.0, 1.0), "PWM_Quarry_Floor_8x4x1_A_20", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (345.7844, 2852.2605, 3984.477), (5.8523246183805275, -21.17959719478938, 9.805011908820914), (1.0, 1.0, 1.0), "PWM_Quarry_Floor_8x4x1_A17_6", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (348.18808, 3557.3086, 3975.3706), (2.2065610121542893, 15.774802548747582, -9.513732604110466), (1.0, 1.0, 1.0), "PWM_Quarry_Floor_8x4x1_A18", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3548.2344, 344.8556, 3984.477), (5.852325980376607, 68.81943147663947, 9.812115424302133), (1.0, 1.0, 1.0), "PWM_Quarry_Floor_8x4x1_A19", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3155.4631, 3262.4688, 631.143), (-1.630310201453465, -11.49289025577328, 16.79999717244049), (1.0, 1.0, 1.0), "PWM_Quarry_Floor_8x4x1_A2", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2862.1353, 352.79474, 3972.0674), (2.2065604121430997, 105.77866916193462, -9.513732517913304), (1.0, 1.0, 1.0), "PWM_Quarry_Floor_8x4x1_A20", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5273.902, 3580.8508, 641.4901), (0.0, -1.3760070183516615, 0.0), (1.0, 1.0, 1.0), "PWM_Quarry_Floor_8x4x1_A23", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5399.1787, 973.4479, 872.88635), (1.0584884166994415e-06, -78.74953573635786, -30.93752931173503), (1.0, 1.0, 1.0), "PWM_Quarry_Floor_8x4x1_A4_42", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5450.7466, 341.20166, 865.82324), (1.6405360523170216, 92.9729080712051, -157.61716543752138), (1.0, 1.0, 1.0), "PWM_Quarry_Floor_8x4x1_A5", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (995.684, 364.92737, 823.627), (2.50803179526376, -104.63486871721307, -161.36410990742803), (1.0, 1.0, 1.0), "PWM_Quarry_Floor_8x4x1_A7", _folder)
if a: placed += 1
else: skipped += 1

# Batch 52: StaticMesh'PWM_Quarry_Floor_8x8x8_Flat_Top_A' (1 instances)
_mesh_path = "/Game/Unshippable/Whitebox/Rocks/Meshes/PWM_Quarry_Floor_8x8x8_Flat_Top_A"
_materials = ['/Game/Environments/ProcTexturing/ProcMaterial_Quarry_8m_Floor']
_folder = "Reconstruction/BD_BB_Passage_SpiralCave/Meshes"
a = spawn_static_mesh(_mesh_path, _materials, (4686.2485, 5447.049, 3493.9272), (-0.7037965236286918, -119.99847591070849, -1.868347339951182), (1.2220703, 1.099201, 1.2980913), "StaticMeshActor17475", _folder)
if a: placed += 1
else: skipped += 1

# Batch 53: StaticMesh'PWM_Quarry_RockDebris_A' (28 instances)
_mesh_path = "/Game/Unshippable/Whitebox/Rocks/Meshes/PWM_Quarry_RockDebris_A"
_materials = ['/Game/Environments/ProcTexturing/ProcMaterial_Quarry_Atlas_5']
_folder = "Reconstruction/BD_BB_Passage_SpiralCave/Meshes"
a = spawn_static_mesh(_mesh_path, _materials, (5234.2417, 720.7595, 795.0), (0.0, 101.25006264455241, -0.0), (2.0, 2.0, 2.0), "PWM_Quarry_RockDebris_A_46", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5605.6064, 2892.0178, 3996.1628), (0.0, -108.4576775205012, 0.0), (1.5, 1.5, 1.5), "PWM_Quarry_RockDebris_A10", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (955.5937, 2605.8105, 4068.0776), (-9.492614486225788, 12.377350091993122, 7.379890354494141), (1.5, 1.5, 1.5), "PWM_Quarry_RockDebris_A12_2", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5607.1035, 2525.4707, 3994.8955), (0.0, -57.11474652716508, 0.0), (1.5, 1.5, 1.5), "PWM_Quarry_RockDebris_A13", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5596.4097, 2097.8367, 3994.8955), (0.0, -79.89395167269738, 0.0), (1.5, 1.5, 1.5), "PWM_Quarry_RockDebris_A14", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5630.0, 1480.0, 4000.0), (0.0, 0.0, -0.0), (1.5, 1.5, 1.5), "PWM_Quarry_RockDebris_A3_33", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5036.3594, 1578.3208, 780.61865), (2.6650166509951725, -135.1766833837251, -6.460754580724254), (1.341659, 1.341659, 1.341659), "PWM_Quarry_RockDebris_A37", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5070.0, 920.0, 4010.0), (4.95901821479196, -61.759946752241426, 2.658250963032302), (1.5, 1.5, 1.5), "PWM_Quarry_RockDebris_A4", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4615.714, 2455.898, 653.1448), (3.1276664140215233, -29.575500001028054, 9.62334400727653), (1.341659, 1.341659, 1.341659), "PWM_Quarry_RockDebris_A44", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3526.4573, 3232.3047, 618.11597), (3.499348341665303, -49.885013221300596, 19.209748993166397), (1.341659, 1.341659, 1.341659), "PWM_Quarry_RockDebris_A45", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3712.5637, 3002.2947, 611.86017), (13.711460067377367, -137.85390886534918, -2.6459056645087093), (1.341659, 1.341659, 1.341659), "PWM_Quarry_RockDebris_A46", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3259.5627, 3324.6887, 629.3797), (-18.24444520757216, 71.59273160259497, 1.3927523835208726), (1.341659, 1.341659, 1.341659), "PWM_Quarry_RockDebris_A47", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2657.559, 3411.4287, 643.2626), (13.333881780035556, -32.00945265508255, 15.57190271393896), (1.341659, 1.341659, 1.341659), "PWM_Quarry_RockDebris_A48", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2376.4473, 3456.7996, 613.9537), (-1.2391968952338446, 10.939512869830963, 31.60647011348114), (1.341659, 1.341659, 1.341659), "PWM_Quarry_RockDebris_A49", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4659.1577, 2226.1997, 662.91205), (-0.3644714378946312, -7.222625085660235, -0.847289969951814), (1.034613, 1.034613, 1.034613), "PWM_Quarry_RockDebris_A50", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2285.9707, 3443.7437, 607.371), (30.617684837167698, -68.07007743530093, 3.717363879096848), (1.341659, 1.341659, 1.341659), "PWM_Quarry_RockDebris_A51", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2177.1155, 4139.908, 619.86005), (-27.599947072876724, -113.79458083650687, 2.5192074186917246), (1.341659, 1.341659, 1.341659), "PWM_Quarry_RockDebris_A52", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2613.3115, 3951.7617, 598.2792), (27.645742562189458, 75.72934659290999, 1.9054934836687323), (1.341659, 1.341659, 1.341659), "PWM_Quarry_RockDebris_A53", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3218.994, 3881.6785, 620.15063), (20.59918980854527, 97.86061792931716, 4.091449029368486), (1.341659, 1.341659, 1.341659), "PWM_Quarry_RockDebris_A54", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1799.1089, 4213.9004, 610.2884), (-9.896057297000157, -31.379574718256187, -26.967956439053548), (1.341659, 1.341659, 1.341659), "PWM_Quarry_RockDebris_A55", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5613.8037, 3686.0, 3993.334), (0.0, 0.0, -0.0), (1.5, 1.5, 1.5), "PWM_Quarry_RockDebris_A6", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5648.9175, 3902.7732, 3993.0596), (0.0, -109.68755816276153, 0.0), (1.5, 1.5, 1.5), "PWM_Quarry_RockDebris_A7", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4149.021, 5579.149, 3971.4275), (0.0, 0.0, -0.0), (1.5, 1.5, 2.0213473), "PWM_Quarry_RockDebris_A8", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3490.9993, 1170.945, 3328.8362), (0.0, 0.0, -0.0), (1.5, 1.5, 2.1631124), "PWM_Quarry_RockDebris_C59_27", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2821.674, 1225.7032, 3324.246), (0.0, 92.81251954052102, -0.0), (1.5, 1.5, 2.2722118), "PWM_Quarry_RockDebris_C60", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3033.3833, 1186.0555, 3329.246), (0.0, -8.43749936170975, 0.0), (1.0, 1.0, 1.0), "PWM_Quarry_RockDebris_C61", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3873.3833, 1086.0555, 3334.246), (0.0, 0.0, -0.0), (1.5, 1.5, 1.0), "PWM_Quarry_RockDebris_C62", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4194.0654, 1126.3387, 3324.246), (0.0, -95.6250299849751, 0.0), (1.5, 1.5, 1.0), "PWM_Quarry_RockDebris_C63", _folder)
if a: placed += 1
else: skipped += 1

# Batch 54: StaticMesh'PWM_Quarry_RockDebris_A_Optimized' (8 instances)
_mesh_path = "/Game/Unshippable/Whitebox/Rocks/Meshes/PWM_Quarry_RockDebris_A_Optimized"
_materials = ['/Game/Environments/ProcTexturing/ProcMaterial_Quarry_RockDebris_A']
_folder = "Reconstruction/BD_BB_Passage_SpiralCave/Meshes"
a = spawn_static_mesh(_mesh_path, _materials, (832.8301, 4130.423, 774.0387), (0.0, 0.0, -2.3526610915421102), (1.3091867, 1.3091867, 1.3091867), "PWM_Quarry_1X1x1_C154", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (683.4756, 3917.0095, 762.3054), (0.0, 0.0, -2.3526610915421102), (1.309187, 1.309187, 1.309187), "PWM_Quarry_1X1x1_C155", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (791.35767, 2513.6394, 737.52783), (0.0, 0.0, -2.3526610915421102), (1.309187, 1.309187, 1.309187), "PWM_Quarry_1X1x1_C156", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (715.6915, 2745.4897, 749.3064), (0.0, 0.0, -3.2233887754912884), (0.8557313, 0.8557313, 0.8557313), "PWM_Quarry_1X1x1_C157", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (676.5763, 2849.0408, 755.8415), (0.0, 0.0, -2.3526610915421102), (0.855731, 0.855731, 0.855731), "PWM_Quarry_1X1x1_C159", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4886.438, 3782.8274, 676.2923), (2.6479687290614886, -40.322930303033736, -28.146540844619977), (2.0, 2.0, 2.0), "PWM_Quarry_RockDebris_A2_9", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4550.0, 4022.6797, 644.5148), (5.010141078184086, -1.5238036902675105, -16.941895982216142), (2.0, 2.0, 2.0), "PWM_Quarry_RockDebris_C_15", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4104.3936, 3914.1016, 624.92914), (16.79153423407995, 84.12362893652856, -7.328246198330698), (2.0, 2.0, 2.0), "PWM_Quarry_RockDebris_C2", _folder)
if a: placed += 1
else: skipped += 1

# Batch 55: StaticMesh'PWM_Quarry_RockDebris_B' (2 instances)
_mesh_path = "/Game/Unshippable/Whitebox/Rocks/Meshes/PWM_Quarry_RockDebris_B"
_materials = ['/Game/Unshippable/Cinematics/Cine002/Environments/Materials/ProcMaterial_Quarry_RockDebris_A']
_folder = "Reconstruction/BD_BB_Passage_SpiralCave/Meshes"
a = spawn_static_mesh(_mesh_path, _materials, (3819.175, 2122.5918, 798.5767), (0.0, 90.0004130536642, -0.0), (1.0, 1.0, 1.0), "PWM_Quarry_RockDebris_A11_0", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4691.1587, 2701.655, 648.5767), (0.0, -35.000302956118816, 0.0), (1.0, 1.0, 1.0), "PWM_Quarry_RockDebris_A11_18", _folder)
if a: placed += 1
else: skipped += 1

# Batch 56: StaticMesh'PWM_Quarry_RockDebris_C' (37 instances)
_mesh_path = "/Game/Unshippable/Whitebox/Rocks/Meshes/PWM_Quarry_RockDebris_C"
_materials = ['/Game/Environments/ProcTexturing/ProcMaterial_Quarry_RockDebris_A']
_folder = "Reconstruction/BD_BB_Passage_SpiralCave/Meshes"
a = spawn_static_mesh(_mesh_path, _materials, (2904.109, 3966.5186, 607.09534), (10.455851378061725, 5.737054215109963, -15.730619276288452), (1.25, 1.25, 1.25), "PWM_Quarry_RockDebris_C10", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2574.109, 4126.5815, 626.57166), (-14.062621540026493, -89.99980998186841, -6.146032747897804e-05), (1.25, 1.25, 1.25), "PWM_Quarry_RockDebris_C11", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1998.8347, 3260.1697, 586.30963), (-2.691162900296265, 44.181010875502345, 14.083686418117441), (2.0, 2.0, 2.0), "PWM_Quarry_RockDebris_C12", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1688.8674, 3002.4536, 596.32513), (-14.31939687840831, 126.1555837463555, 2.1752755279788536), (2.0, 2.0, 2.0), "PWM_Quarry_RockDebris_C13", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1576.3298, 2668.2651, 606.03937), (4.158049653509947, -118.76486439495183, -19.50793558343426), (1.5, 1.5, 1.5), "PWM_Quarry_RockDebris_C14", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1433.3458, 2387.0051, 618.2696), (14.062497999092647, 0.0, -0.0), (1.0, 1.0, 1.0), "PWM_Quarry_RockDebris_C15", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1255.8596, 2384.9788, 608.5874), (-5.47686729440314, -12.942138316216914, 8.229586145091822), (1.0, 1.0, 1.0), "PWM_Quarry_RockDebris_C16", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1274.687, 2201.6184, 605.40967), (-14.31897000868397, 126.15532927336145, 4.9880042473905375), (2.0, 2.0, 1.0), "PWM_Quarry_RockDebris_C17", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2240.1997, 2504.0508, 744.2497), (-8.418610352847777, 149.15428328734743, -0.7275387226657857), (1.5, 1.5, 1.5), "PWM_Quarry_RockDebris_C18", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5305.0, 275.0, 780.0), (0.0, 0.0, -0.0), (1.5, 1.5, 1.5), "PWM_Quarry_RockDebris_C19_49", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5159.547, 1031.8716, 775.0), (0.0, -157.50001379721112, 0.0), (1.5, 1.5, 1.5), "PWM_Quarry_RockDebris_C20", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2973.4631, 1436.0619, 770.0), (0.0, -157.50001379721112, 0.0), (2.0, 2.0, 1.0), "PWM_Quarry_RockDebris_C21", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3391.9712, 1457.8789, 765.0), (0.0, -16.87472505613022, 0.0), (2.0, 2.0, 1.0), "PWM_Quarry_RockDebris_C22", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2241.7598, 1932.2362, 775.0), (1.3916564040696962, -16.819428040388093, 4.594545015354427), (1.5, 1.5, 1.0), "PWM_Quarry_RockDebris_C23", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2364.8464, 1623.7013, 775.0), (0.0, -22.499785264391715, 0.0), (2.0, 2.0, 1.0), "PWM_Quarry_RockDebris_C24", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2322.381, 2258.686, 777.6004), (5.624995489063799, -2.812347374229503, -1.1042720587856327e-09), (2.0, 2.0, 1.0), "PWM_Quarry_RockDebris_C25", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2437.9236, 2728.6514, 778.42334), (5.625015915603374, -2.8123171030234615, 2.812508948109924), (2.0, 2.0, 1.0), "PWM_Quarry_RockDebris_C26", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1220.5912, 4108.0625, 636.67676), (3.925350774437919, 63.600185019403504, -23.918093996003186), (2.0, 2.0, 1.0), "PWM_Quarry_RockDebris_C27", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (972.3805, 4227.704, 741.1729), (2.651322505544496, 63.75150387070738, -11.713502113273455), (1.25, 1.25, 1.5), "PWM_Quarry_RockDebris_C28", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (893.84735, 2347.3374, 688.39075), (-4.752013636700382, -68.69345214623509, 14.113240991610455), (2.0, 2.0, 1.0), "PWM_Quarry_RockDebris_C31", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (786.2062, 1248.9983, 771.60815), (-5.6249998239637025, 50.62532590704031, -1.2860263830858656e-08), (2.0, 2.0, 2.0), "PWM_Quarry_RockDebris_C32", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (378.68106, 1180.2299, 806.8521), (-7.505127078031875, 121.27034862381495, 0.3136891520975054), (2.0, 2.0, 2.0), "PWM_Quarry_RockDebris_C33", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1107.2849, 880.8567, 799.6719), (3.774157715837655, -81.42458981979902, 4.173931700202588), (2.0, 2.0, 2.0), "PWM_Quarry_RockDebris_C34", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1255.0486, 2183.6836, 620.3387), (2.329538747971659, -24.832732675626072, 6.196854891502284), (2.0, 2.0, 1.0), "PWM_Quarry_RockDebris_C35", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4987.695, 2736.9238, 660.22626), (8.437501667396425, 0.0, -0.0), (1.5, 1.5, 1.5), "PWM_Quarry_RockDebris_C4", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1286.4922, 388.12183, 795.0), (0.0, 126.56215405997217, -0.0), (2.0, 2.0, 1.25), "PWM_Quarry_RockDebris_C41", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1586.4922, 353.12183, 790.0), (0.0, 33.74957361711183, -0.0), (1.5, 1.5, 1.0), "PWM_Quarry_RockDebris_C42", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1147.3805, 5132.704, 791.1729), (0.0, 0.0, -0.0), (2.0, 2.0, 1.0), "PWM_Quarry_RockDebris_C46", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (647.3805, 5312.704, 791.1729), (0.0, -73.12499866925161, 0.0), (2.0, 2.0, 1.0), "PWM_Quarry_RockDebris_C47", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1367.3805, 4792.704, 776.1729), (-4.556396414537472, -72.8141216404587, -4.336395306884371), (1.25, 1.25, 1.0), "PWM_Quarry_RockDebris_C48", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1087.3805, 4732.704, 781.1729), (0.0, 0.0, -0.0), (1.0, 1.0, 1.0), "PWM_Quarry_RockDebris_C49", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4955.365, 2399.4001, 649.59436), (-4.6882011598378615, 38.62642549237703, 5.35951596279269), (1.5, 1.5, 1.5), "PWM_Quarry_RockDebris_C5", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5051.3237, 2562.0178, 649.59436), (-4.688201134192426, 38.62642548571279, 5.359516582726521), (1.5, 1.5, 1.5), "PWM_Quarry_RockDebris_C50", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4834.043, 3028.373, 616.6237), (7.468580126110756, -97.07513729574167, -14.115631714269904), (1.25, 1.25, 1.25), "PWM_Quarry_RockDebris_C6", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4724.7676, 2028.8674, 677.36676), (-4.688201134192426, 38.62642548571279, 5.359516582726521), (1.5, 1.5, 1.5), "PWM_Quarry_RockDebris_C65", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4895.488, 1953.5217, 677.36676), (-4.688201503184267, 128.62642122230196, 5.35953876096409), (1.5, 1.5, 1.5), "PWM_Quarry_RockDebris_C66", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3795.8677, 2833.2822, 588.5038), (-6.014922940160885, 129.6481362657756, -5.846923351032589), (1.5, 1.5, 1.5), "PWM_Quarry_RockDebris_C9", _folder)
if a: placed += 1
else: skipped += 1

# Batch 57: StaticMesh'SM_Debris_Floor_01' (31 instances)
_mesh_path = "/Game/Unshippable/Whitebox/Rocks/Meshes/SM_Debris_Floor_01"
_materials = ['/Game/Environments/ProcTexturing/ProcMaterial_Quarry_RockDebris_A']
_folder = "Reconstruction/BD_BB_Passage_SpiralCave/Meshes"
a = spawn_static_mesh(_mesh_path, _materials, (5890.0, 3330.0, 3995.0), (0.0, 0.0, -0.0), (2.0, 2.0, 1.0), "PWM_Quarry_RockDebris_C56_45", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2995.751, 4465.5166, 1524.7036), (-14.744814233825256, 164.7594639132816, 3.5945010317783828), (1.0, 1.0, 1.0), "SM_Debris_Floor_2", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2522.912, 4835.6587, 1377.5931), (17.898951247192734, 0.0, -0.0), (1.0, 1.0, 1.0), "SM_Debris_Floor_3", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2921.799, 4844.9214, 1495.1887), (-14.744814180965195, 164.75946386377782, 3.5945014393829435), (1.0, 1.0, 1.0), "SM_Debris_Floor_4", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2696.2957, 4835.6577, 1433.9722), (-16.946256190504393, 160.63890457696345, 5.848832036960233), (1.0, 1.0, 1.0), "SM_Debris_Floor_5", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3150.8643, 4889.3594, 1555.5696), (11.78946315560561, -41.02502915304926, -9.610719131918803), (1.0, 1.0, 1.0), "SM_Debris_Floor_6", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3370.5974, 4899.6045, 1609.6726), (11.379639084574956, -40.928187654887054, -8.479460846934467), (1.0, 1.0, 1.0), "SM_Debris_Floor_7", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2232.3867, 4507.328, 1283.9664), (8.156146927465567, -63.65603519242122, -15.987638434365293), (1.0, 1.0, 1.0), "SM_Debris_Floor_8", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2060.9243, 4573.447, 1251.719), (2.1522469929699963, -61.88477038025335, -9.267150961654439), (1.0, 1.0, 1.0), "SM_Debris_Floor_9", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2295.1743, 4941.6514, 1304.0404), (17.898951247192734, 0.0, -0.0), (1.0, 1.0, 1.0), "SM_Debris_Floor_14", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3761.1482, 4847.371, 1694.0804), (2.6948304511142727, -19.73489379659918, 1.1300751606779487), (1.0, 1.0, 1.0), "SM_Debris_Floor_16", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3712.1414, 5013.3438, 1690.3682), (17.170424874048773, -19.4546502287916, -1.198486362572462), (1.0, 1.0, 1.0), "SM_Debris_Floor_17", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3254.5671, 4394.79, 1598.8673), (15.781490532292032, -25.20412935016082, -4.399719029718795), (1.0, 1.0, 1.0), "SM_Debris_Floor_19", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3124.5828, 4398.4624, 1561.0286), (15.781490532292032, -25.20412935016082, -4.399719029718795), (1.0, 1.0, 1.0), "SM_Debris_Floor_20", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3983.2559, 4767.652, 1694.0804), (0.0, -19.744111824484158, 0.0), (1.0, 1.0, 1.0), "SM_Debris_Floor_36", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (416.28268, 1518.8973, 799.39886), (0.0, 60.46758483632502, -0.0), (1.0, 1.0, 1.0), "SM_Debris_Floor_37", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (752.67676, 5154.861, 845.7273), (9.457716037142518, -2.9329225119644033, -21.63925517775896), (1.0, 1.0, 1.0), "SM_Debris_Floor_49", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1132.3143, 3554.5603, 3997.3), (0.0, 0.0, -0.0), (1.0, 1.0, 1.0), "SM_Debris_Floor_108", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (768.0886, 2509.6694, 741.9958), (-5.38674891873011, 0.0, -0.0), (1.0, 1.0, 1.0), "SM_Debris_Floor_112", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1741.2119, 3512.8242, 3994.0447), (0.0, -24.656798063217686, 0.0), (1.0, 1.0, 1.0), "SM_Debris_Floor_113", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1924.3973, 3584.23, 3994.0447), (0.0, 139.70932166611848, -0.0), (1.0, 1.0, 1.0), "SM_Debris_Floor_115", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (584.5831, 1456.3165, 800.21686), (0.0, 0.0, -0.0), (1.0, 1.0, 1.0), "SM_Debris_Floor_116", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3072.5266, 1223.2158, 3334.7808), (0.0, -48.02154519274893, 0.0), (1.0, 1.0, 1.0), "SM_Debris_Floor_126", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2860.7534, 1295.8081, 3334.7808), (0.0, -48.02154519274893, 0.0), (1.0, 1.0, 1.0), "SM_Debris_Floor_127", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2335.8801, 5621.016, 3993.946), (0.0, 0.0, -0.0), (1.0, 1.0, 1.0), "SM_Debris_Floor_234", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1266.5278, 3667.335, 3997.3), (0.0, 0.0, -0.0), (1.0, 1.0, 1.0), "SM_Debris_Floor_271", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1132.8738, 3661.5852, 4022.8252), (-21.015106658221423, -72.13903993746986, 8.577340865233664), (1.0, 1.0, 1.0), "SM_Debris_Floor_274", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1570.2985, 3523.5515, 3994.0447), (0.0, 0.0, -0.0), (1.0, 1.0, 1.0), "SM_Debris_Floor_287", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1719.896, 1643.1018, 4305.223), (-16.247801174166653, -47.102019202283635, 8.271544161342577), (1.0, 1.0, 1.0), "SM_Debris_Floor_339", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3268.4468, 1341.6884, 3334.7808), (0.0, -48.02154519274893, 0.0), (1.0, 1.0, 1.0), "SM_Debris_Floor_357", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2725.2004, 4465.5293, 1443.1313), (17.898951247192734, 0.0, -0.0), (1.0, 1.0, 1.0), "SM_Debris_Floor_01_8", _folder)
if a: placed += 1
else: skipped += 1

# Batch 58: StaticMesh'SM_Debris_Floor_02' (149 instances)
_mesh_path = "/Game/Unshippable/Whitebox/Rocks/Meshes/SM_Debris_Floor_02"
_materials = ['/Game/Environments/ProcTexturing/ProcMaterial_Quarry_RockDebris_A']
_folder = "Reconstruction/BD_BB_Passage_SpiralCave/Meshes"
a = spawn_static_mesh(_mesh_path, _materials, (6046.7007, 929.9144, 3995.0), (0.0, -73.12494166846878, 0.0), (2.0, 2.0, 1.0), "PWM_Quarry_RockDebris_C58", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (6266.6147, 929.9144, 3995.0), (0.0, 105.75776524834181, -0.0), (2.0, 2.0, 1.0), "PWM_Quarry_RockDebris_C68", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2079.5461, 5148.954, 1272.3433), (5.969580226540414, 0.0077010270624358135, -1.3229980032415443), (1.0, 1.0, 1.0), "SM_Debris_Floor_10", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2135.4062, 5035.0645, 1275.538), (5.969580571391911, 0.007700996618882125, -1.3229980052210453), (1.0, 1.0, 1.0), "SM_Debris_Floor_11", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1821.58, 5090.95, 1245.0208), (5.969580571391911, 0.007700996618882125, -1.3229980052210453), (1.0, 1.0, 1.0), "SM_Debris_Floor_12", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1002.9373, 4568.3706, 789.32245), (0.0, -1.8516236255715628, 0.0), (1.0, 1.0, 1.0), "SM_Debris_Floor_23", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1252.115, 4704.204, 785.79083), (0.0, 51.0275830252271, -0.0), (1.0, 1.0, 1.0), "SM_Debris_Floor_24", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (594.4424, 3952.9944, 794.7384), (0.0, -1.8516236255715628, 0.0), (1.0, 1.0, 1.0), "SM_Debris_Floor_25", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (411.48004, 3981.614, 793.59485), (0.0, -1.8516236255715628, 0.0), (1.0, 1.0, 1.0), "SM_Debris_Floor_26", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (966.65094, 4365.5254, 791.82385), (-1.7812498404515376, -1.9295044866703903, 1.7318720366431166), (1.0, 1.0, 1.0), "SM_Debris_Floor_27", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (858.3017, 3857.7854, 723.435), (-29.639861716546253, -13.283234940698112, -8.692654613169454), (1.0, 1.0, 1.0), "SM_Debris_Floor_28", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2482.3528, 2616.5166, 817.62244), (0.3723067168528809, -112.08366102890388, -0.26119998896453184), (1.0, 1.0, 1.0), "SM_Debris_Floor_30", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2434.2864, 2394.8088, 810.44275), (3.6515552333346237, -112.2840188097417, -6.234892799423575), (1.0, 1.0, 1.0), "SM_Debris_Floor_31", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2519.6025, 4476.1914, 1371.9197), (13.729226315675652, -0.046356215488659036, -4.38430764740637), (1.0, 1.0, 1.0), "SM_Debris_Floor_32", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2581.2595, 3033.2312, 797.7685), (16.052997659616306, -0.39068603507769706, -4.912750072409392), (1.0, 1.0, 1.0), "SM_Debris_Floor_33", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1314.7451, 1084.8314, 796.8926), (0.0, -18.81863360635114, 0.0), (1.0, 1.0, 1.0), "SM_Debris_Floor_39", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1463.9589, 682.4716, 796.8926), (0.0, -118.44676099334234, 0.0), (1.0, 1.0, 1.0), "SM_Debris_Floor_40", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3886.092, 4267.936, 1694.3428), (0.0, -27.55200234105065, 0.0), (1.0, 1.0, 1.0), "SM_Debris_Floor_41", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2606.5745, 1434.0312, 796.8926), (0.0, 122.15831668200678, -0.0), (1.0, 1.0, 1.0), "SM_Debris_Floor_42", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2735.7498, 1446.4498, 796.8926), (0.0, -138.2134137870248, 0.0), (1.0, 1.0, 1.0), "SM_Debris_Floor_43", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3163.435, 1622.292, 796.8926), (0.0, 54.996638374195896, -0.0), (1.0, 1.0, 1.0), "SM_Debris_Floor_44", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3225.0193, 1508.0656, 796.8926), (0.0, 154.6258652350677, -0.0), (1.0, 1.0, 1.0), "SM_Debris_Floor_45", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (860.4895, 4893.7134, 795.99854), (0.0, 0.0, -0.0), (1.0, 1.0, 1.0), "SM_Debris_Floor_46", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2880.7688, 1376.918, 796.8926), (0.0, 154.6258652350677, -0.0), (1.0, 1.0, 1.0), "SM_Debris_Floor_47", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3088.3906, 1372.0128, 796.8926), (0.0, -127.348109249835, 0.0), (1.0, 1.0, 1.0), "SM_Debris_Floor_48", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4985.535, 928.27734, 796.8926), (0.0, -127.348109249835, 0.0), (1.0, 1.0, 1.0), "SM_Debris_Floor_50", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5009.1626, 741.1133, 796.8926), (0.0, 154.6258652350677, -0.0), (1.0, 1.0, 1.0), "SM_Debris_Floor_51", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5043.119, 591.7871, 796.8926), (0.0, -127.348109249835, 0.0), (1.0, 1.0, 1.0), "SM_Debris_Floor_52", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4803.1284, 1853.5685, 747.15753), (-1.4531554240249613, 154.95906433355293, -11.474698541315622), (1.0, 1.0, 1.0), "SM_Debris_Floor_53", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4838.391, 1706.8915, 773.4954), (10.909378669745783, -127.52800937509637, -3.857696665330961), (1.0, 1.0, 1.0), "SM_Debris_Floor_54", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4785.0605, 1497.9943, 794.3356), (-0.21463013457308686, -126.23726125591959, 0.6030266643665436), (1.0, 1.0, 1.0), "SM_Debris_Floor_55", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4938.108, 1503.2024, 793.4203), (-0.6368102983713687, -48.20687490585714, -0.08468627930710265), (1.0, 1.0, 1.0), "SM_Debris_Floor_56", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4802.9004, 1300.1842, 794.3356), (-0.2146301372248465, -126.23726125773698, 0.6030269585274557), (1.0, 1.0, 1.0), "SM_Debris_Floor_57", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3288.29, 3865.1821, 673.78973), (0.0, 0.0, -34.525448154970725), (1.0, 1.0, 1.0), "SM_Debris_Floor_59", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3478.9248, 3861.1506, 679.04706), (37.82392521120026, 101.82911342729581, 1.4678303778672361), (1.0, 1.0, 1.0), "SM_Debris_Floor_60", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3397.2776, 3745.3887, 613.43896), (29.69467301797198, 101.59123812070422, 2.7732108698364164), (1.0, 1.0, 1.0), "SM_Debris_Floor_61", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3190.702, 3778.828, 600.6781), (26.34099109003511, 99.85003562225683, 23.490461513568036), (1.0, 1.0, 1.0), "SM_Debris_Floor_62", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1371.989, 5688.2017, 3993.9878), (0.0, 0.0, -0.0), (1.0, 1.0, 1.0), "SM_Debris_Floor_64", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1530.5032, 5688.2017, 3993.9878), (0.0, -57.13036882281804, 0.0), (1.0, 1.0, 1.0), "SM_Debris_Floor_65", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1788.9349, 5288.2627, 3993.9878), (0.0, -57.13036882281804, 0.0), (1.0, 1.0, 1.0), "SM_Debris_Floor_66", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1591.8682, 5256.3804, 3993.9878), (0.0, -38.276188138255115, 0.0), (1.0, 1.0, 1.0), "SM_Debris_Floor_67", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1699.1732, 5199.67, 3993.9878), (0.0, -81.8766781152771, 0.0), (1.0, 1.0, 1.0), "SM_Debris_Floor_68", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1858.4287, 5752.0884, 3993.9878), (0.0, -81.8766781152771, 0.0), (1.0, 1.0, 1.0), "SM_Debris_Floor_70", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1966.2327, 5792.2183, 3993.9878), (0.0, -36.88156124976248, 0.0), (1.0, 1.0, 1.0), "SM_Debris_Floor_71", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1262.5042, 5793.764, 3993.9878), (0.0, 0.0, -0.0), (1.0, 1.0, 1.0), "SM_Debris_Floor_73", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4821.001, 5952.6772, 4034.4575), (15.69162836092176, 0.019679445026325675, 1.9489778708968322), (1.0, 1.0, 1.0), "SM_Debris_Floor_75", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4806.892, 5844.144, 4034.3196), (15.691630728372512, 0.019678987260911374, 1.9489780507421983), (1.0, 1.0, 1.0), "SM_Debris_Floor_76", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4805.3545, 5670.6274, 4040.0076), (15.691630728372512, 0.019678987260911374, 1.9489780507421983), (1.0, 1.0, 1.0), "SM_Debris_Floor_77", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4805.9707, 5484.8833, 4038.0005), (5.769536413924384, -64.20040471489962, -16.953308088151324), (1.0, 1.0, 1.0), "SM_Debris_Floor_78", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4166.289, 5434.1426, 3996.35), (0.0, 27.41997848258316, -0.0), (1.0, 1.0, 1.0), "SM_Debris_Floor_82", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3846.611, 5434.8076, 3996.35), (0.0, 2.1023384218783447, -0.0), (1.0, 1.0, 1.0), "SM_Debris_Floor_83", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3559.922, 5449.86, 3996.35), (0.0, -19.24487248942978, 0.0), (1.0, 1.0, 1.0), "SM_Debris_Floor_84", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3383.1406, 5534.0474, 3996.35), (0.0, -29.92633130465397, 0.0), (1.0, 1.0, 1.0), "SM_Debris_Floor_85", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3231.161, 5576.988, 3996.35), (0.0, 14.87640031908017, -0.0), (1.0, 1.0, 1.0), "SM_Debris_Floor_86", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3656.0923, 5725.3286, 3996.35), (0.0, -19.24487248942978, 0.0), (1.0, 1.0, 1.0), "SM_Debris_Floor_87", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3865.4053, 5817.046, 3996.35), (0.0, 44.31715185569489, -0.0), (1.0, 1.0, 1.0), "SM_Debris_Floor_88", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3120.047, 5607.187, 3996.35), (0.0, -29.92633130465397, 0.0), (1.0, 1.0, 1.0), "SM_Debris_Floor_89", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2835.126, 5643.012, 3996.35), (0.0, -29.92633130465397, 0.0), (1.0, 1.0, 1.0), "SM_Debris_Floor_90", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2147.9941, 5450.0703, 3994.303), (-4.586852863367779, 0.0, -0.0), (1.0, 1.0, 1.0), "SM_Debris_Floor_95", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1972.5364, 5401.1885, 3992.156), (-2.0064085774745832, -0.13745116909906296, -5.466490865280602), (1.0, 1.0, 1.0), "SM_Debris_Floor_96", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (998.1646, 5457.713, 3993.9878), (0.0, -67.66872698839501, 0.0), (1.0, 1.0, 1.0), "SM_Debris_Floor_97", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2581.2595, 2772.7004, 817.62244), (4.459496833851331, 0.37026110513902266, 4.750232880998959), (1.0, 1.0, 1.0), "SM_Debris_Floor_98", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (957.7236, 5678.761, 4019.3066), (6.366804825132632e-06, -115.10192437801527, 28.74724552640394), (1.0, 1.0, 1.0), "SM_Debris_Floor_99", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1000.2859, 5834.5713, 4015.376), (1.6158664348083922, -89.9201707021907, 23.537532070730162), (1.0, 1.0, 1.0), "SM_Debris_Floor_100", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (879.97705, 5512.8057, 4019.3064), (-9.120177981957504, -89.70986370925844, 8.629644062223447), (1.0, 1.0, 1.0), "SM_Debris_Floor_101", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2398.4482, 2202.789, 815.3482), (-0.9881285210251055, -112.2687062327885, -2.9107361523822446), (1.0, 1.0, 1.0), "SM_Debris_Floor_102", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1984.8372, 3138.314, 3997.6792), (0.0, -132.20034306994955, 0.0), (1.0, 1.0, 1.0), "SM_Debris_Floor_103", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1798.8011, 3039.6135, 3997.6792), (-1.681823542605806, -132.17340190620953, -1.855560023320483), (1.0, 1.0, 1.0), "SM_Debris_Floor_104", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1305.7288, 2846.855, 3997.6792), (-1.681823542605806, -132.17340190620953, -1.855560023320483), (1.0, 1.0, 1.0), "SM_Debris_Floor_105", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1089.2344, 2889.8267, 3997.6792), (-1.681762464717733, -14.616331176925481, -1.8555603668016802), (1.0, 1.0, 1.0), "SM_Debris_Floor_106", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (805.6682, 2585.3152, 725.06525), (-20.957213903576843, 0.0, -0.0), (1.0, 1.0, 1.0), "SM_Debris_Floor_109", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2048.9229, 3585.8948, 3994.562), (0.0, 139.70932166611848, -0.0), (1.0, 1.0, 1.0), "SM_Debris_Floor_114", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2167.4932, 3328.0386, 4026.7847), (9.324774033411371, 0.0, -0.0), (1.0, 1.0, 1.0), "SM_Debris_Floor_117", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2167.4932, 3481.6292, 4019.7737), (9.057164214684253, 2.227228105972422, 13.877743923063026), (1.0, 1.0, 1.0), "SM_Debris_Floor_118", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2062.9624, 3409.3323, 4004.7253), (10.293696395802097, 0.0, -0.0), (1.0, 1.0, 1.0), "SM_Debris_Floor_119", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1388.9681, 978.38196, 796.8926), (0.0, -118.44676099334234, 0.0), (1.0, 1.0, 1.0), "SM_Debris_Floor_120", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1389.7358, 788.92114, 796.8926), (0.0, -18.81863360635114, 0.0), (1.0, 1.0, 1.0), "SM_Debris_Floor_124", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4068.72, 1217.0835, 3333.8604), (0.0, 0.0, -0.0), (1.0, 1.0, 1.0), "SM_Debris_Floor_128", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4288.4453, 1283.3904, 3333.8604), (0.0, 73.59374727372338, -0.0), (1.0, 1.0, 1.0), "SM_Debris_Floor_129", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (429.37738, 5070.853, 795.99854), (0.0, 0.0, -0.0), (1.0, 1.0, 1.0), "SM_Debris_Floor_130", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4547.3936, 1613.273, 3333.8604), (0.0, -14.1269215029677, 0.0), (1.0, 1.0, 1.0), "SM_Debris_Floor_131", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4473.5356, 1538.1128, 3333.8604), (0.0, -14.1269215029677, 0.0), (1.0, 1.0, 1.0), "SM_Debris_Floor_132", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4594.2617, 1787.4409, 3333.8604), (0.0, -14.1269215029677, 0.0), (1.0, 1.0, 1.0), "SM_Debris_Floor_133", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4490.3467, 1938.8417, 3333.8604), (0.0, -14.1269215029677, 0.0), (1.0, 1.0, 1.0), "SM_Debris_Floor_134", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4338.364, 2009.3473, 3333.8604), (0.0, 161.10791654914584, -0.0), (1.0, 1.0, 1.0), "SM_Debris_Floor_135", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4180.4194, 2220.2612, 3333.8604), (0.0, 161.10791654914584, -0.0), (1.0, 1.0, 1.0), "SM_Debris_Floor_136", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4242.745, 2102.8003, 3333.8604), (0.0, -55.669860174690676, 0.0), (1.0, 1.0, 1.0), "SM_Debris_Floor_137", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4011.731, 2313.964, 3333.8604), (0.0, -162.18195986517838, 0.0), (1.0, 1.0, 1.0), "SM_Debris_Floor_138", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3863.2292, 2364.4949, 3333.8604), (0.0, -162.18195986517838, 0.0), (1.0, 1.0, 1.0), "SM_Debris_Floor_139", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3721.83, 2169.9868, 3333.8604), (0.0, -162.18195986517838, 0.0), (1.0, 1.0, 1.0), "SM_Debris_Floor_140", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3559.6118, 2121.788, 3333.8604), (0.0, -75.95998951033009, 0.0), (1.0, 1.0, 1.0), "SM_Debris_Floor_141", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3406.3577, 2112.1375, 3333.8604), (0.0, -156.33932543054343, 0.0), (1.0, 1.0, 1.0), "SM_Debris_Floor_142", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4951.5786, 1077.6035, 796.8926), (0.0, 154.6258652350677, -0.0), (1.0, 1.0, 1.0), "SM_Debris_Floor_143", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2882.2688, 2051.2817, 3333.8604), (0.0, -156.33932543054343, 0.0), (1.0, 1.0, 1.0), "SM_Debris_Floor_144", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3076.1616, 2044.3346, 3333.8604), (0.0, 5.220283127340279, -0.0), (1.0, 1.0, 1.0), "SM_Debris_Floor_145", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3199.9272, 1938.0281, 3333.8604), (0.0, 5.220284276815022, -0.0), (1.0, 1.0, 1.0), "SM_Debris_Floor_146", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2855.5713, 1817.0702, 3333.8604), (0.0, 57.01332463336461, -0.0), (1.0, 1.0, 1.0), "SM_Debris_Floor_147", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2757.7007, 1664.3352, 3333.8604), (0.0, 57.01332463336461, -0.0), (1.0, 1.0, 1.0), "SM_Debris_Floor_148", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2735.2947, 1488.1814, 3333.8604), (0.0, 104.41223447979505, -0.0), (1.0, 1.0, 1.0), "SM_Debris_Floor_149", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2896.2244, 1709.2479, 3333.8604), (0.0, 129.93594453176874, -0.0), (1.0, 1.0, 1.0), "SM_Debris_Floor_150", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3824.4385, 1279.4968, 3353.6963), (0.0, 0.0, 19.616275792815664), (1.0, 1.0, 1.0), "SM_Debris_Floor_151", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3442.4768, 1180.7615, 3372.0906), (-6.122650760707669, -2.271728734325501, 21.044968329158635), (1.0, 1.0, 1.0), "SM_Debris_Floor_152", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3184.0708, 1260.467, 3359.756), (-0.7411500964802288, 22.506459445770385, 19.417598430506597), (1.0, 1.0, 1.0), "SM_Debris_Floor_153", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5022.7314, 3012.9277, 1994.7078), (0.0, -112.05615249313587, 0.0), (1.0, 1.0, 1.0), "SM_Debris_Floor_155", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5159.383, 3076.2253, 2003.0178), (-18.58831494375098, -104.36752304823116, -22.950528399374022), (1.0, 1.0, 1.0), "SM_Debris_Floor_156", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5198.253, 3451.7131, 2018.208), (1.4801355682977932, -93.21484968927876, -22.813139810978484), (1.0, 1.0, 1.0), "SM_Debris_Floor_157", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5106.128, 3659.373, 2028.8767), (-11.704832650669633, -86.44136814851309, -27.479488503641274), (1.0, 1.0, 1.0), "SM_Debris_Floor_158", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (6057.5254, 5013.064, 3997.772), (0.0, 55.1700191142001, -0.0), (1.0, 1.0, 1.0), "SM_Debris_Floor_160", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5952.5596, 4877.278, 3997.772), (0.0, -115.53176495666156, 0.0), (1.0, 1.0, 1.0), "SM_Debris_Floor_161", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5814.966, 4635.718, 3997.772), (0.0, -115.53176495666156, 0.0), (1.0, 1.0, 1.0), "SM_Debris_Floor_162", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5759.265, 4457.261, 3997.772), (0.0, 53.46709291227848, -0.0), (1.0, 1.0, 1.0), "SM_Debris_Floor_163", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (6077.7896, 4878.8125, 3995.956), (0.0, -164.20012140888852, 0.0), (1.0, 1.0, 1.0), "SM_Debris_Floor_164", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5966.2324, 4730.878, 3995.956), (0.0, 98.09335411751562, -0.0), (1.0, 1.0, 1.0), "SM_Debris_Floor_165", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5962.1465, 4497.5938, 3995.956), (0.0, 98.09335411751562, -0.0), (1.0, 1.0, 1.0), "SM_Debris_Floor_166", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5995.475, 4279.372, 3995.956), (0.0, 98.09335411751562, -0.0), (1.0, 1.0, 1.0), "SM_Debris_Floor_167", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5911.551, 3681.2915, 3995.956), (0.0, -100.20867426629945, 0.0), (1.0, 1.0, 1.0), "SM_Debris_Floor_170", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5785.6753, 3449.2673, 3995.956), (0.0, -100.20867426629945, 0.0), (1.0, 1.0, 1.0), "SM_Debris_Floor_171", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5744.1963, 3065.5981, 3995.956), (0.0, 123.45563046081783, -0.0), (1.0, 1.0, 1.0), "SM_Debris_Floor_172", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5725.717, 2855.7473, 3995.956), (0.0, -79.66182995755754, 0.0), (1.0, 1.0, 1.0), "SM_Debris_Floor_173", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5835.669, 2671.512, 3995.956), (0.0, -161.7030621784748, 0.0), (1.0, 1.0, 1.0), "SM_Debris_Floor_174", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5832.008, 2469.9595, 4000.0015), (0.0, 163.70007747368456, -0.0), (1.0, 1.0, 1.0), "SM_Debris_Floor_175", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5755.3833, 1702.0093, 3995.956), (0.0, 145.7051986143967, -0.0), (1.0, 1.0, 1.0), "SM_Debris_Floor_176", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5878.888, 1607.181, 3995.956), (0.0, 111.10815130257214, -0.0), (1.0, 1.0, 1.0), "SM_Debris_Floor_177", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2986.7737, 3905.284, 641.1369), (0.0, 0.0, -34.525448154970725), (1.0, 1.0, 1.0), "SM_Debris_Floor_178", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5794.053, 1852.286, 3995.956), (0.0, -87.66900183381145, 0.0), (1.0, 1.0, 1.0), "SM_Debris_Floor_179", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5645.2896, 1822.0261, 3995.956), (0.0, -87.66900183381145, 0.0), (1.0, 1.0, 1.0), "SM_Debris_Floor_180", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5854.1104, 1287.4554, 3995.956), (0.0, 111.10815130257214, -0.0), (1.0, 1.0, 1.0), "SM_Debris_Floor_181", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5921.7104, 1160.373, 3995.956), (0.0, -34.05688332581924, 0.0), (1.0, 1.0, 1.0), "SM_Debris_Floor_182", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5931.101, 1415.791, 3995.956), (0.0, -34.05688332581924, 0.0), (1.0, 1.0, 1.0), "SM_Debris_Floor_183", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (6086.966, 1111.0127, 3995.956), (0.0, -34.05688332581924, 0.0), (1.0, 1.0, 1.0), "SM_Debris_Floor_184", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1020.5545, 5601.961, 3993.9878), (0.0, 0.0, -0.0), (1.0, 1.0, 1.0), "SM_Debris_Floor_185", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4683.8354, 5952.5894, 3997.1716), (0.0, 0.0, -0.0), (1.0, 1.0, 1.0), "SM_Debris_Floor_204", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2274.299, 5542.518, 3994.9138), (-2.1459958789466103, 5.837089327279225e-07, -0.8995972530962906), (1.0, 1.0, 1.0), "SM_Debris_Floor_237", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1041.6732, 5772.157, 3993.9878), (0.0, -67.66872698839501, 0.0), (1.0, 1.0, 1.0), "SM_Debris_Floor_242", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1999.2305, 3275.2073, 3994.167), (0.0, 0.0, -0.0), (1.0, 1.0, 1.0), "SM_Debris_Floor_264", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1476.3889, 3428.3105, 3994.562), (0.0, 0.0, -0.0), (1.0, 1.0, 1.0), "SM_Debris_Floor_284", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1669.8661, 3582.5037, 3994.562), (0.0, -24.656798063217686, 0.0), (1.0, 1.0, 1.0), "SM_Debris_Floor_290", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1607.9271, 3014.0493, 3995.4824), (-1.681823542605806, -132.17340190620953, -1.855560023320483), (1.0, 1.0, 1.0), "SM_Debris_Floor_294", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1458.4564, 2144.9624, 4221.5903), (2.8161053368311944e-07, -25.65197998934954, 30.52680936184577), (1.0, 1.0, 1.0), "SM_Debris_Floor_333", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1702.3889, 1821.5708, 4273.332), (-6.999389621899679, -0.2554626395536829, 2.0954447258475173), (1.0, 1.0, 1.0), "SM_Debris_Floor_336", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1606.4543, 1921.2417, 4283.616), (-2.188384184198998, -56.80673397509849, 13.333450084110709), (1.0, 1.0, 1.0), "SM_Debris_Floor_342", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3488.2217, 1336.5553, 3333.8604), (0.0, 0.0, -0.0), (1.0, 1.0, 1.0), "SM_Debris_Floor_354", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4495.781, 1428.5481, 3333.8604), (0.0, 73.59374727372338, -0.0), (1.0, 1.0, 1.0), "SM_Debris_Floor_363", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3246.48, 2089.3499, 3333.8604), (0.0, -156.33932543054343, 0.0), (1.0, 1.0, 1.0), "SM_Debris_Floor_377", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5022.7314, 3137.8164, 1994.7078), (0.0, 0.0, -0.0), (1.0, 1.0, 1.0), "SM_Debris_Floor_406", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (6251.7715, 5117.9976, 3997.772), (0.0, 0.0, -0.0), (1.0, 1.0, 1.0), "SM_Debris_Floor_418", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5920.4604, 1774.1476, 3995.956), (0.0, 111.10815130257214, -0.0), (1.0, 1.0, 1.0), "SM_Debris_Floor_441", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (6261.901, 1069.6891, 3995.956), (0.0, -115.5979325827809, 0.0), (1.0, 1.0, 1.0), "SM_Debris_Floor_460", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1912.5413, 4694.3076, 1245.3525), (2.8083965662007695, 0.0, -0.0), (1.0, 1.0, 1.0), "SM_Debris_Floor_02_23", _folder)
if a: placed += 1
else: skipped += 1

# ======================================================================
# PHASE 2: ConstructionCatalog  (construction blocks)
# ======================================================================
unreal.log(f"[{BUBBLE_NAME}] Phase 2: Placing construction blocks...")

# Construction blocks use DecoVolume transforms (matched by Name)
_folder = "Reconstruction/BD_BB_Passage_SpiralCave/Construction"

# Construction: AB_Mines_Scaffolding_Balcony_B_2
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Scaffolding
#   Volume: EMorSimpleShape::Empty, BoxExtent: (100.0, 100.0, 100.0)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (3195.0, 1810.0, 1650.0), (0.0, 0.0, -0.0), (2.0000, 2.0000, 2.0000), "AB_Mines_Scaffolding_Balcony_B_2", _folder)
if a: placed += 1
else: skipped += 1

# Construction: AB_Mines_Scaffolding_Balcony_B2
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Scaffolding
#   Volume: EMorSimpleShape::Empty, BoxExtent: (100.0, 100.0, 100.0)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (2944.9998, 2060.0, 1650.0), (0.0, 90.00007597449323, -0.0), (2.0000, 2.0000, 2.0000), "AB_Mines_Scaffolding_Balcony_B2", _folder)
if a: placed += 1
else: skipped += 1

# Construction: AB_Mines_Scaffolding_Balcony_B3
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Scaffolding
#   Volume: EMorSimpleShape::Empty, BoxExtent: (100.0, 100.0, 100.0)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (2944.9998, 2060.0, 1950.0), (0.0, 90.00007597449323, -0.0), (2.0000, 2.0000, 2.0000), "AB_Mines_Scaffolding_Balcony_B3", _folder)
if a: placed += 1
else: skipped += 1

# Construction: AB_Mines_Scaffolding_Balcony_B4
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Scaffolding
#   Volume: EMorSimpleShape::Empty, BoxExtent: (100.0, 100.0, 100.0)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (5100.0005, 2150.0, 1350.0), (0.0, 89.99975996369572, -0.0), (2.0000, 2.0000, 2.0000), "AB_Mines_Scaffolding_Balcony_B4", _folder)
if a: placed += 1
else: skipped += 1

# Construction: AB_Mines_Scaffolding_Balcony_B5
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Scaffolding
#   Volume: EMorSimpleShape::Empty, BoxExtent: (100.0, 100.0, 100.0)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (5100.0005, 2670.0, 1650.0), (0.0, 89.99975996369572, -0.0), (2.0000, 2.0000, 2.0000), "AB_Mines_Scaffolding_Balcony_B5", _folder)
if a: placed += 1
else: skipped += 1

# Construction: AB_Mines_Scaffolding_Balcony_B6_4
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Scaffolding
#   Volume: EMorSimpleShape::Empty, BoxExtent: (100.0, 100.0, 100.0)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (5100.0, 2370.0, 1350.0), (-0.0, -90.0001164887758, -0.0), (2.0000, 2.0000, 2.0000), "AB_Mines_Scaffolding_Balcony_B6_4", _folder)
if a: placed += 1
else: skipped += 1

# Construction: AB_Mines_Scaffolding_Balcony_B7
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Scaffolding
#   Volume: EMorSimpleShape::Empty, BoxExtent: (100.0, 100.0, 100.0)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (5040.0005, 1530.0, 1350.0), (0.0, 89.99975996369572, -0.0), (2.0000, 2.0000, 2.0000), "AB_Mines_Scaffolding_Balcony_B7", _folder)
if a: placed += 1
else: skipped += 1

# Construction: AB_Mines_Scaffolding_Balcony_B8
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Scaffolding
#   Volume: EMorSimpleShape::Empty, BoxExtent: (100.0, 100.0, 100.0)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (5100.0005, 2880.0, 1860.0), (0.0, 89.99975996369572, -0.0), (2.0000, 2.0000, 2.0000), "AB_Mines_Scaffolding_Balcony_B8", _folder)
if a: placed += 1
else: skipped += 1

# Construction: AB_Mines_Scaffolding_Balcony_B9
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Scaffolding
#   Volume: EMorSimpleShape::Empty, BoxExtent: (100.0, 100.0, 100.0)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (5040.0, 1850.0, 1350.0), (-0.0, -90.0001164887758, -0.0), (2.0000, 2.0000, 2.0000), "AB_Mines_Scaffolding_Balcony_B9", _folder)
if a: placed += 1
else: skipped += 1

# Construction: AB_Mines_Scaffolding_Balcony_Single_A_Broken_AB_2
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Scaffolding
#   Volume: EMorSimpleShape::Empty, BoxExtent: (100.0, 100.0, 100.0)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (3630.0, 2640.0, 1885.0), (0.0, 0.0, -0.0), (2.0000, 2.0000, 2.0000), "AB_Mines_Scaffolding_Balcony_Single_A_Broken_AB_2", _folder)
if a: placed += 1
else: skipped += 1

# Construction: AB_Mines_Scaffolding_Balcony_Single_A_Broken_AB2
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Scaffolding
#   Volume: EMorSimpleShape::Empty, BoxExtent: (100.0, 100.0, 100.0)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (3596.8545, 2967.0537, 1793.6204), (-5.624938892169706, 20.00001024023197, -6.514484117797955e-08), (2.0000, 2.0000, 2.0000), "AB_Mines_Scaffolding_Balcony_Single_A_Broken_AB2", _folder)
if a: placed += 1
else: skipped += 1

# Construction: AB_Mines_Scaffolding_Beam_3m_8
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Scaffolding
#   Volume: EMorSimpleShape::Empty, BoxExtent: (100.0, 100.0, 100.0)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (3726.299, 2629.0457, 4595.0), (0.0, 92.81253626073598, -0.0), (2.0000, 2.0000, 2.0000), "AB_Mines_Scaffolding_Beam_3m_8", _folder)
if a: placed += 1
else: skipped += 1

# Construction: AB_Mines_Scaffolding_Beam_3m10
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Scaffolding
#   Volume: EMorSimpleShape::Empty, BoxExtent: (100.0, 100.0, 100.0)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (2681.8716, 4143.35, 3139.5796), (-12.106751165051294, 7.438215232145094, -3.815460172739335), (2.0000, 2.0000, 2.0000), "AB_Mines_Scaffolding_Beam_3m10", _folder)
if a: placed += 1
else: skipped += 1

# Construction: AB_Mines_Scaffolding_Beam_3m11
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Scaffolding
#   Volume: EMorSimpleShape::Empty, BoxExtent: (100.0, 100.0, 100.0)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (2716.463, 3845.9907, 3120.0723), (-12.106751165051294, 7.438215232145094, -3.815460172739335), (2.0000, 2.0000, 2.0000), "AB_Mines_Scaffolding_Beam_3m11", _folder)
if a: placed += 1
else: skipped += 1

# Construction: AB_Mines_Scaffolding_Beam_3m12
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Scaffolding
#   Volume: EMorSimpleShape::Empty, BoxExtent: (100.0, 100.0, 100.0)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (2121.791, 3968.6785, 3172.7722), (-3.049773996365646, 2.029236027849864, 37.009250934715716), (2.0000, 2.0000, 2.0000), "AB_Mines_Scaffolding_Beam_3m12", _folder)
if a: placed += 1
else: skipped += 1

# Construction: AB_Mines_Scaffolding_Beam_3m13
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Scaffolding
#   Volume: EMorSimpleShape::Empty, BoxExtent: (100.0, 100.0, 100.0)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (2231.2273, 3530.5452, 4595.0), (-0.0, -30.93728850858391, -0.0), (2.0000, 2.0000, 2.0000), "AB_Mines_Scaffolding_Beam_3m13", _folder)
if a: placed += 1
else: skipped += 1

# Construction: AB_Mines_Scaffolding_Beam_3m14
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Scaffolding
#   Volume: EMorSimpleShape::Empty, BoxExtent: (100.0, 100.0, 100.0)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (2385.4578, 3787.8628, 4595.0), (-0.0, -30.93728850858391, -0.0), (2.0000, 2.0000, 2.0000), "AB_Mines_Scaffolding_Beam_3m14", _folder)
if a: placed += 1
else: skipped += 1

# Construction: AB_Mines_Scaffolding_Beam_3m15
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Scaffolding
#   Volume: EMorSimpleShape::Empty, BoxExtent: (100.0, 100.0, 100.0)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (2539.69, 4045.181, 4595.0), (-0.0, -30.93728850858391, -0.0), (2.0000, 2.0000, 2.0000), "AB_Mines_Scaffolding_Beam_3m15", _folder)
if a: placed += 1
else: skipped += 1

# Construction: AB_Mines_Scaffolding_Beam_3m16
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Scaffolding
#   Volume: EMorSimpleShape::Empty, BoxExtent: (100.0, 100.0, 100.0)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (2693.922, 4302.498, 4595.0), (-0.0, -30.93728850858391, -0.0), (2.0000, 2.0000, 2.0000), "AB_Mines_Scaffolding_Beam_3m16", _folder)
if a: placed += 1
else: skipped += 1

# Construction: AB_Mines_Scaffolding_Beam_3m17
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Scaffolding
#   Volume: EMorSimpleShape::Empty, BoxExtent: (100.0, 100.0, 100.0)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (2917.8613, 4283.1743, 4595.0), (-0.0, -120.93728899933107, -0.0), (2.0000, 2.0000, 2.0000), "AB_Mines_Scaffolding_Beam_3m17", _folder)
if a: placed += 1
else: skipped += 1

# Construction: AB_Mines_Scaffolding_Beam_3m18
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Scaffolding
#   Volume: EMorSimpleShape::Empty, BoxExtent: (100.0, 100.0, 100.0)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (3175.1787, 4128.944, 4595.0), (-0.0, -120.93728899933107, -0.0), (2.0000, 2.0000, 2.0000), "AB_Mines_Scaffolding_Beam_3m18", _folder)
if a: placed += 1
else: skipped += 1

# Construction: AB_Mines_Scaffolding_Beam_3m19
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Scaffolding
#   Volume: EMorSimpleShape::Empty, BoxExtent: (100.0, 100.0, 100.0)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (3432.4958, 3974.7097, 4595.0), (-0.0, -120.93728899933107, -0.0), (2.0000, 2.0000, 2.0000), "AB_Mines_Scaffolding_Beam_3m19", _folder)
if a: placed += 1
else: skipped += 1

# Construction: AB_Mines_Scaffolding_Beam_3m2
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Scaffolding
#   Volume: EMorSimpleShape::Empty, BoxExtent: (100.0, 100.0, 100.0)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (3426.6602, 2614.3254, 4595.0), (0.0, 92.81253626073598, -0.0), (2.0000, 2.0000, 2.0000), "AB_Mines_Scaffolding_Beam_3m2", _folder)
if a: placed += 1
else: skipped += 1

# Construction: AB_Mines_Scaffolding_Beam_3m20
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Scaffolding
#   Volume: EMorSimpleShape::Empty, BoxExtent: (100.0, 100.0, 100.0)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (3689.813, 3820.4773, 4595.0), (-0.0, -120.93728899933107, -0.0), (2.0000, 2.0000, 2.0000), "AB_Mines_Scaffolding_Beam_3m20", _folder)
if a: placed += 1
else: skipped += 1

# Construction: AB_Mines_Scaffolding_Beam_3m21
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Scaffolding
#   Volume: EMorSimpleShape::Empty, BoxExtent: (100.0, 100.0, 100.0)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (3797.5115, 3633.938, 4595.0), (-0.0, -177.1874614149522, -0.0), (2.0000, 2.0000, 2.0000), "AB_Mines_Scaffolding_Beam_3m21", _folder)
if a: placed += 1
else: skipped += 1

# Construction: AB_Mines_Scaffolding_Beam_3m22
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Scaffolding
#   Volume: EMorSimpleShape::Empty, BoxExtent: (100.0, 100.0, 100.0)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (3812.232, 3334.2993, 4595.0), (-0.0, -177.1874614149522, -0.0), (2.0000, 2.0000, 2.0000), "AB_Mines_Scaffolding_Beam_3m22", _folder)
if a: placed += 1
else: skipped += 1

# Construction: AB_Mines_Scaffolding_Beam_3m23
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Scaffolding
#   Volume: EMorSimpleShape::Empty, BoxExtent: (100.0, 100.0, 100.0)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (3826.9485, 3034.6616, 4595.0), (-0.0, -177.1874614149522, -0.0), (2.0000, 2.0000, 2.0000), "AB_Mines_Scaffolding_Beam_3m23", _folder)
if a: placed += 1
else: skipped += 1

# Construction: AB_Mines_Scaffolding_Beam_3m24
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Scaffolding
#   Volume: EMorSimpleShape::Empty, BoxExtent: (100.0, 100.0, 100.0)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (3841.6667, 2735.022, 4595.0), (-0.0, -177.1874614149522, -0.0), (2.0000, 2.0000, 2.0000), "AB_Mines_Scaffolding_Beam_3m24", _folder)
if a: placed += 1
else: skipped += 1

# Construction: AB_Mines_Scaffolding_Beam_3m25
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Scaffolding
#   Volume: EMorSimpleShape::Empty, BoxExtent: (100.0, 100.0, 100.0)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (2138.5261, 3716.6814, 3319.657), (-3.049835014106256, 2.0292125768555653, 22.9464624667297), (2.0000, 2.0000, 2.0000), "AB_Mines_Scaffolding_Beam_3m25", _folder)
if a: placed += 1
else: skipped += 1

# Construction: AB_Mines_Scaffolding_Beam_3m26
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Scaffolding
#   Volume: EMorSimpleShape::Empty, BoxExtent: (100.0, 100.0, 100.0)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (3361.2893, 3839.5247, 3010.4895), (-13.910185150945027, 4.78048357405326, -11.531676181865663), (2.0000, 2.0000, 2.0000), "AB_Mines_Scaffolding_Beam_3m26", _folder)
if a: placed += 1
else: skipped += 1

# Construction: AB_Mines_Scaffolding_Beam_3m27
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Scaffolding
#   Volume: EMorSimpleShape::Empty, BoxExtent: (100.0, 100.0, 100.0)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (3358.842, 4113.2344, 3092.7456), (-13.91015664546468, 4.780512830862613, -22.781737343763403), (2.0000, 2.0000, 2.0000), "AB_Mines_Scaffolding_Beam_3m27", _folder)
if a: placed += 1
else: skipped += 1

# Construction: AB_Mines_Scaffolding_Beam_3m28
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Scaffolding
#   Volume: EMorSimpleShape::Empty, BoxExtent: (100.0, 100.0, 100.0)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (2408.3203, 3064.9006, 4595.0), (-0.0, -177.1874614149522, -0.0), (2.0000, 2.0000, 2.0000), "AB_Mines_Scaffolding_Beam_3m28", _folder)
if a: placed += 1
else: skipped += 1

# Construction: AB_Mines_Scaffolding_Beam_3m29
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Scaffolding
#   Volume: EMorSimpleShape::Empty, BoxExtent: (100.0, 100.0, 100.0)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (2423.04, 2765.262, 4595.0), (-0.0, -177.1874614149522, -0.0), (2.0000, 2.0000, 2.0000), "AB_Mines_Scaffolding_Beam_3m29", _folder)
if a: placed += 1
else: skipped += 1

# Construction: AB_Mines_Scaffolding_Beam_3m3
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Scaffolding
#   Volume: EMorSimpleShape::Empty, BoxExtent: (100.0, 100.0, 100.0)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (3127.0222, 2599.6062, 4595.0), (0.0, 92.81253626073598, -0.0), (2.0000, 2.0000, 2.0000), "AB_Mines_Scaffolding_Beam_3m3", _folder)
if a: placed += 1
else: skipped += 1

# Construction: AB_Mines_Scaffolding_Beam_3m4
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Scaffolding
#   Volume: EMorSimpleShape::Empty, BoxExtent: (100.0, 100.0, 100.0)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (2827.3828, 2584.8865, 4595.0), (0.0, 92.81253626073598, -0.0), (2.0000, 2.0000, 2.0000), "AB_Mines_Scaffolding_Beam_3m4", _folder)
if a: placed += 1
else: skipped += 1

# Construction: AB_Mines_Scaffolding_Beam_3m5
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Scaffolding
#   Volume: EMorSimpleShape::Empty, BoxExtent: (100.0, 100.0, 100.0)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (5100.0, 2000.0, 1450.0), (0.0, 90.00010028305118, -0.0), (2.0000, 2.0000, 2.0000), "AB_Mines_Scaffolding_Beam_3m5", _folder)
if a: placed += 1
else: skipped += 1

# Construction: AB_Mines_Scaffolding_Beam_3m6
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Scaffolding
#   Volume: EMorSimpleShape::Empty, BoxExtent: (100.0, 100.0, 100.0)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (2527.744, 2570.1665, 4595.0), (0.0, 92.81253626073598, -0.0), (2.0000, 2.0000, 2.0000), "AB_Mines_Scaffolding_Beam_3m6", _folder)
if a: placed += 1
else: skipped += 1

# Construction: AB_Mines_Scaffolding_Beam_3m9
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Scaffolding
#   Volume: EMorSimpleShape::Empty, BoxExtent: (100.0, 100.0, 100.0)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (3371.4202, 3545.402, 2952.2764), (-13.910185150945027, 4.78048357405326, -11.531676181865663), (2.0000, 2.0000, 2.0000), "AB_Mines_Scaffolding_Beam_3m9", _folder)
if a: placed += 1
else: skipped += 1

# Construction: AB_Mines_Scaffolding_Beam_Panels_3m_3
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Scaffolding
#   Volume: EMorSimpleShape::Empty, BoxExtent: (100.0, 100.0, 100.0)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (3300.0, 2010.0, 1450.0), (0.0, 89.99981506294705, -0.0), (2.0000, 2.0000, 2.0000), "AB_Mines_Scaffolding_Beam_Panels_3m_3", _folder)
if a: placed += 1
else: skipped += 1

# Construction: AB_Mines_Scaffolding_Beam_Panels_3m_4
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Scaffolding
#   Volume: EMorSimpleShape::Empty, BoxExtent: (100.0, 100.0, 100.0)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (4200.0, 2000.0, 1450.0), (0.0, 90.00005166594045, -0.0), (2.0000, 2.0000, 2.0000), "AB_Mines_Scaffolding_Beam_Panels_3m_4", _folder)
if a: placed += 1
else: skipped += 1

# Construction: AB_Mines_Scaffolding_Beam_Panels_3m_5
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Scaffolding
#   Volume: EMorSimpleShape::Empty, BoxExtent: (100.0, 100.0, 100.0)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (3600.0, 2000.0, 1450.0), (0.0, 90.00005166594045, -0.0), (2.0000, 2.0000, 2.0000), "AB_Mines_Scaffolding_Beam_Panels_3m_5", _folder)
if a: placed += 1
else: skipped += 1

# Construction: AB_Mines_Scaffolding_Beam_Panels_3m_6
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Scaffolding
#   Volume: EMorSimpleShape::Empty, BoxExtent: (100.0, 100.0, 100.0)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (3550.0, 2510.0, 1450.0), (-0.0, -0.0003356933594815241, -0.0), (2.0000, 2.0000, 2.0000), "AB_Mines_Scaffolding_Beam_Panels_3m_6", _folder)
if a: placed += 1
else: skipped += 1

# Construction: AB_Mines_Scaffolding_Beam_Panels_3m_7
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Scaffolding
#   Volume: EMorSimpleShape::Empty, BoxExtent: (100.0, 100.0, 100.0)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (4500.0, 2000.0, 1450.0), (0.0, 90.00005166594045, -0.0), (2.0000, 2.0000, 2.0000), "AB_Mines_Scaffolding_Beam_Panels_3m_7", _folder)
if a: placed += 1
else: skipped += 1

# Construction: AB_Mines_Scaffolding_Beam_Panels_3m_8
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Scaffolding
#   Volume: EMorSimpleShape::Empty, BoxExtent: (100.0, 100.0, 100.0)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (5040.0, 1700.0, 1450.0), (0.0, 90.00005166594045, -0.0), (2.0000, 2.0000, 2.0000), "AB_Mines_Scaffolding_Beam_Panels_3m_8", _folder)
if a: placed += 1
else: skipped += 1

# Construction: AB_Mines_Scaffolding_Beam_Panels_3m_13
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Scaffolding
#   Volume: EMorSimpleShape::Empty, BoxExtent: (100.0, 100.0, 100.0)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (3550.0, 2810.0, 1450.0), (-0.0, -0.0003356933594815241, -0.0), (2.0000, 2.0000, 2.0000), "AB_Mines_Scaffolding_Beam_Panels_3m_13", _folder)
if a: placed += 1
else: skipped += 1

# Construction: AB_Mines_Scaffolding_Beam_Panels_3m_Broken_A_2
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Scaffolding
#   Volume: EMorSimpleShape::Empty, BoxExtent: (100.0, 100.0, 100.0)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (4800.0, 1999.9996, 1450.0), (0.0, 90.0001326944829, -0.0), (2.0000, 2.0000, 2.0000), "AB_Mines_Scaffolding_Beam_Panels_3m_Broken_A_2", _folder)
if a: placed += 1
else: skipped += 1

# Construction: AB_Mines_Scaffolding_Beam_Panels_3m_Broken_A10
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Scaffolding
#   Volume: EMorSimpleShape::Empty, BoxExtent: (100.0, 100.0, 100.0)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (5099.9995, 2730.0007, 1850.0), (-0.0, -89.9998815062137, -0.0), (2.0000, 2.0000, 2.0000), "AB_Mines_Scaffolding_Beam_Panels_3m_Broken_A10", _folder)
if a: placed += 1
else: skipped += 1

# Construction: AB_Mines_Scaffolding_Beam_Panels_3m_Broken_A11
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Scaffolding
#   Volume: EMorSimpleShape::Empty, BoxExtent: (100.0, 100.0, 100.0)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (5099.9995, 2420.0007, 1550.0), (-0.0, -89.9998815062137, -0.0), (2.0000, 2.0000, 2.0000), "AB_Mines_Scaffolding_Beam_Panels_3m_Broken_A11", _folder)
if a: placed += 1
else: skipped += 1

# Construction: AB_Mines_Scaffolding_Beam_Panels_3m_Broken_A2
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Scaffolding
#   Volume: EMorSimpleShape::Empty, BoxExtent: (100.0, 100.0, 100.0)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (3900.0, 1999.9996, 1450.0), (0.0, 90.0001326944829, -0.0), (2.0000, 2.0000, 2.0000), "AB_Mines_Scaffolding_Beam_Panels_3m_Broken_A2", _folder)
if a: placed += 1
else: skipped += 1

# Construction: AB_Mines_Scaffolding_Beam_Panels_3m_Broken_A3
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Scaffolding
#   Volume: EMorSimpleShape::Empty, BoxExtent: (100.0, 100.0, 100.0)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (3650.0, 2200.0, 1450.0), (0.0, 0.0, -0.0), (2.0000, 2.0000, 2.0000), "AB_Mines_Scaffolding_Beam_Panels_3m_Broken_A3", _folder)
if a: placed += 1
else: skipped += 1

# Construction: AB_Mines_Scaffolding_Beam_Panels_3m_Broken_A4
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Scaffolding
#   Volume: EMorSimpleShape::Empty, BoxExtent: (100.0, 100.0, 100.0)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (3650.0, 2500.0, 1450.0), (-0.0, -179.99995901885745, -0.0), (2.0000, 2.0000, 2.0000), "AB_Mines_Scaffolding_Beam_Panels_3m_Broken_A4", _folder)
if a: placed += 1
else: skipped += 1

# Construction: AB_Mines_Scaffolding_Beam_Panels_3m_Broken_A5
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Scaffolding
#   Volume: EMorSimpleShape::Empty, BoxExtent: (100.0, 100.0, 100.0)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (3650.0, 2800.0, 1450.0), (0.0, 0.0, -0.0), (2.0000, 2.0000, 2.0000), "AB_Mines_Scaffolding_Beam_Panels_3m_Broken_A5", _folder)
if a: placed += 1
else: skipped += 1

# Construction: AB_Mines_Scaffolding_Beam_Panels_3m_Broken_A6
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Scaffolding
#   Volume: EMorSimpleShape::Empty, BoxExtent: (100.0, 100.0, 100.0)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (3650.0024, 4020.0005, 1450.0), (-0.0, -0.0004272461022210228, -0.0), (2.0000, 2.0000, 2.0000), "AB_Mines_Scaffolding_Beam_Panels_3m_Broken_A6", _folder)
if a: placed += 1
else: skipped += 1

# Construction: AB_Mines_Scaffolding_Beam_Panels_3m_Broken_A7_6
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Scaffolding
#   Volume: EMorSimpleShape::Empty, BoxExtent: (100.0, 100.0, 100.0)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (3046.9006, 4180.7617, 1300.0), (-0.0, -98.43764271662266, -0.0), (2.0000, 2.0000, 2.0000), "AB_Mines_Scaffolding_Beam_Panels_3m_Broken_A7_6", _folder)
if a: placed += 1
else: skipped += 1

# Construction: AB_Mines_Scaffolding_Beam_Panels_3m_Broken_A8
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Scaffolding
#   Volume: EMorSimpleShape::Empty, BoxExtent: (100.0, 100.0, 100.0)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (3750.0027, 4020.0005, 1450.0), (0.0, 179.99950822623498, -0.0), (2.0000, 2.0000, 2.0000), "AB_Mines_Scaffolding_Beam_Panels_3m_Broken_A8", _folder)
if a: placed += 1
else: skipped += 1

# Construction: AB_Mines_Scaffolding_Beam_Panels_3m_Broken_A9
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Scaffolding
#   Volume: EMorSimpleShape::Empty, BoxExtent: (100.0, 100.0, 100.0)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (5100.0, 2519.9998, 1455.0), (0.0, 90.0001326944829, -0.0), (2.0000, 2.0000, 2.0000), "AB_Mines_Scaffolding_Beam_Panels_3m_Broken_A9", _folder)
if a: placed += 1
else: skipped += 1

# Construction: AB_Mines_Scaffolding_Broken_Segment_A_2
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Scaffolding
#   Volume: EMorSimpleShape::Empty, BoxExtent: (100.0, 100.0, 100.0)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (1781.759, 5041.4604, 2614.7266), (-1.0846564097753268, -87.01946425660255, -19.656097002001214), (2.0000, 2.0000, 2.0000), "AB_Mines_Scaffolding_Broken_Segment_A_2", _folder)
if a: placed += 1
else: skipped += 1

# Construction: AB_Mines_Scaffolding_Broken_Segment_A2
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Scaffolding
#   Volume: EMorSimpleShape::Empty, BoxExtent: (100.0, 100.0, 100.0)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (2078.8457, 5063.211, 2712.979), (61.41057536343932, 75.28399556092616, -6.642484789820299), (2.0000, 2.0000, 2.0000), "AB_Mines_Scaffolding_Broken_Segment_A2", _folder)
if a: placed += 1
else: skipped += 1

# Construction: AB_Mines_Scaffolding_Broken_Segment_B_6
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Scaffolding
#   Volume: EMorSimpleShape::Empty, BoxExtent: (100.0, 100.0, 100.0)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (987.9929, 3756.66, 2703.2593), (1.1120102415701156, -106.71538851273236, 44.934035409388876), (2.0000, 2.0000, 2.0000), "AB_Mines_Scaffolding_Broken_Segment_B_6", _folder)
if a: placed += 1
else: skipped += 1

# Construction: AB_Mines_Scaffolding_Broken_Segment_B2
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Scaffolding
#   Volume: EMorSimpleShape::Empty, BoxExtent: (100.0, 100.0, 100.0)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (2381.236, 5020.4536, 2675.0), (-0.0, -171.5626139939116, -0.0), (2.0000, 2.0000, 2.0000), "AB_Mines_Scaffolding_Broken_Segment_B2", _folder)
if a: placed += 1
else: skipped += 1

# Construction: AB_Mines_Scaffolding_Broken_Segment_C_2
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Scaffolding
#   Volume: EMorSimpleShape::Empty, BoxExtent: (100.0, 100.0, 100.0)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (2631.2043, 5143.7285, 2670.0), (-0.0, -78.74987491531705, -0.0), (2.0000, 2.0000, 2.0000), "AB_Mines_Scaffolding_Broken_Segment_C_2", _folder)
if a: placed += 1
else: skipped += 1

# Construction: AB_Mines_Scaffolding_Foundation_1x1m_2
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Scaffolding
#   Volume: EMorSimpleShape::Empty, BoxExtent: (100.0, 100.0, 100.0)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (3237.961, 4135.139, 1350.0), (-0.0, -97.81243959683121, -0.0), (2.0000, 2.0000, 2.0000), "AB_Mines_Scaffolding_Foundation_1x1m_2", _folder)
if a: placed += 1
else: skipped += 1

# Construction: AB_Mines_Scaffolding_Foundation_1x1m2_2
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Scaffolding
#   Volume: EMorSimpleShape::Empty, BoxExtent: (100.0, 100.0, 100.0)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (3492.0952, 4263.226, 3302.3015), (-14.31655755564856, 9.026538226945936, 12.411218511736378), (2.0000, 2.0000, 2.0000), "AB_Mines_Scaffolding_Foundation_1x1m2_2", _folder)
if a: placed += 1
else: skipped += 1

# Construction: AB_Mines_Scaffolding_Foundation_3x1m_Broken_A_11
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Scaffolding
#   Volume: EMorSimpleShape::Empty, BoxExtent: (100.0, 100.0, 100.0)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (3610.0, 2640.0, 1650.0), (0.0, 0.0, -0.0), (2.0000, 2.0000, 2.0000), "AB_Mines_Scaffolding_Foundation_3x1m_Broken_A_11", _folder)
if a: placed += 1
else: skipped += 1

# Construction: AB_Mines_Scaffolding_Foundation_3x1m_Broken_A2
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Scaffolding
#   Volume: EMorSimpleShape::Empty, BoxExtent: (100.0, 100.0, 100.0)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (3564.8533, 2953.4958, 1650.0), (0.0, 22.49990184208405, -0.0), (2.0000, 2.0000, 2.0000), "AB_Mines_Scaffolding_Foundation_3x1m_Broken_A2", _folder)
if a: placed += 1
else: skipped += 1

# Construction: AB_Mines_Scaffolding_Foundation_3x1m_Broken_A3_2
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Scaffolding
#   Volume: EMorSimpleShape::Empty, BoxExtent: (100.0, 100.0, 100.0)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (2666.4417, 5088.5864, 2515.3594), (-19.59900161140719, -84.70932376782295, 1.5916383310437296), (2.0000, 2.0000, 2.0000), "AB_Mines_Scaffolding_Foundation_3x1m_Broken_A3_2", _folder)
if a: placed += 1
else: skipped += 1

# Construction: AB_Mines_Scaffolding_Foundation_3x1m_Broken_B_2
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Scaffolding
#   Volume: EMorSimpleShape::Empty, BoxExtent: (100.0, 100.0, 100.0)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (3638.6165, 4123.405, 3353.6938), (-14.024016534897179, 5.767689213595113, -0.9874877500009319), (2.0000, 2.0000, 2.0000), "AB_Mines_Scaffolding_Foundation_3x1m_Broken_B_2", _folder)
if a: placed += 1
else: skipped += 1

# Construction: AB_Mines_Scaffolding_Foundation_3x1m_Broken_B2
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Scaffolding
#   Volume: EMorSimpleShape::Empty, BoxExtent: (100.0, 100.0, 100.0)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (2954.3318, 4364.6626, 3370.3857), (5.876374576196486, -76.98087074887869, 13.936722687807961), (2.0000, 2.0000, 2.0000), "AB_Mines_Scaffolding_Foundation_3x1m_Broken_B2", _folder)
if a: placed += 1
else: skipped += 1

# Construction: AB_Mines_Scaffolding_Foundation_3x1m_Broken_B3
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Scaffolding
#   Volume: EMorSimpleShape::Empty, BoxExtent: (100.0, 100.0, 100.0)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (3430.8928, 2667.1538, 4794.1475), (0.0, 2.8126640184491642, -0.0), (2.0000, 2.0000, 2.0000), "AB_Mines_Scaffolding_Foundation_3x1m_Broken_B3", _folder)
if a: placed += 1
else: skipped += 1

# Construction: AB_Mines_Scaffolding_Foundation_3x1m_Broken_B4
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Scaffolding
#   Volume: EMorSimpleShape::Empty, BoxExtent: (100.0, 100.0, 100.0)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (3771.7598, 3065.9631, 4794.1475), (0.0, 92.81231995694225, -0.0), (2.0000, 2.0000, 2.0000), "AB_Mines_Scaffolding_Foundation_3x1m_Broken_B4", _folder)
if a: placed += 1
else: skipped += 1

# Construction: AB_Mines_Scaffolding_Foundation_3x1m_Broken_B5
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Scaffolding
#   Volume: EMorSimpleShape::Empty, BoxExtent: (100.0, 100.0, 100.0)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (3642.3489, 997.8293, 3864.8457), (0.0, 85.0582034367311, -0.0), (2.0000, 2.0000, 2.0000), "AB_Mines_Scaffolding_Foundation_3x1m_Broken_B5", _folder)
if a: placed += 1
else: skipped += 1

# Construction: AB_Mines_Scaffolding_Foundation_3x1m_Broken_B6
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Scaffolding
#   Volume: EMorSimpleShape::Empty, BoxExtent: (100.0, 100.0, 100.0)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (2845.3237, 1066.7291, 3864.8457), (-0.0, -94.94159393125199, -0.0), (2.0000, 2.0000, 2.0000), "AB_Mines_Scaffolding_Foundation_3x1m_Broken_B6", _folder)
if a: placed += 1
else: skipped += 1

# Construction: AB_Mines_Scaffolding_Foundation_3x2m_2
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Scaffolding
#   Volume: EMorSimpleShape::Empty, BoxExtent: (100.0, 100.0, 100.0)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (3354.91, 3187.1924, 750.0), (-0.0, -140.00000132049152, -0.0), (2.0000, 2.0000, 2.0000), "AB_Mines_Scaffolding_Foundation_3x2m_2", _folder)
if a: placed += 1
else: skipped += 1

# Construction: AB_Mines_Scaffolding_Foundation_3x2m2
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Scaffolding
#   Volume: EMorSimpleShape::Empty, BoxExtent: (100.0, 100.0, 100.0)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (3076.1824, 3331.4658, 750.0), (-0.0, -95.00002760264337, -0.0), (2.0000, 2.0000, 2.0000), "AB_Mines_Scaffolding_Foundation_3x2m2", _folder)
if a: placed += 1
else: skipped += 1

# Construction: AB_Mines_Scaffolding_Foundation_3x2m3
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Scaffolding
#   Volume: EMorSimpleShape::Empty, BoxExtent: (100.0, 100.0, 100.0)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (1083.4032, 1130.3052, 900.0), (-0.0, -143.43745615400172, -0.0), (2.0000, 2.0000, 2.0000), "AB_Mines_Scaffolding_Foundation_3x2m3", _folder)
if a: placed += 1
else: skipped += 1

# Construction: AB_Mines_Scaffolding_Foundation_3x2m4_1
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Scaffolding
#   Volume: EMorSimpleShape::Empty, BoxExtent: (100.0, 100.0, 100.0)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (1191.1305, 892.72394, 900.0), (0.0, 126.56244394310686, -0.0), (2.0000, 2.0000, 2.0000), "AB_Mines_Scaffolding_Foundation_3x2m4_1", _folder)
if a: placed += 1
else: skipped += 1

# Construction: AB_Mines_Scaffolding_Foundation_3x2m5
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Scaffolding
#   Volume: EMorSimpleShape::Empty, BoxExtent: (100.0, 100.0, 100.0)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (4432.3447, 4678.393, 1750.0), (-0.0, -146.24977593492343, -0.0), (2.0000, 2.0000, 2.0000), "AB_Mines_Scaffolding_Foundation_3x2m5", _folder)
if a: placed += 1
else: skipped += 1

# Construction: AB_Mines_Scaffolding_Foundation_3x2m6_2
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Scaffolding
#   Volume: EMorSimpleShape::Empty, BoxExtent: (100.0, 100.0, 100.0)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (1029.119, 2958.2004, 4150.0), (0.0, 5.625096251751507, -0.0), (2.0000, 2.0000, 2.0000), "AB_Mines_Scaffolding_Foundation_3x2m6_2", _folder)
if a: placed += 1
else: skipped += 1

# Construction: AB_Mines_Scaffolding_Foundation_3x2m7
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Scaffolding
#   Volume: EMorSimpleShape::Empty, BoxExtent: (100.0, 100.0, 100.0)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (970.3077, 3555.3118, 4150.0), (0.0, 5.625095791732844, -0.0), (2.0000, 2.0000, 2.0000), "AB_Mines_Scaffolding_Foundation_3x2m7", _folder)
if a: placed += 1
else: skipped += 1

# Construction: AB_Mines_Scaffolding_Foundation_3x3m_2
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Scaffolding
#   Volume: EMorSimpleShape::Empty, BoxExtent: (100.0, 100.0, 100.0)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (5321.214, 1678.7869, 3550.0), (0.0, 44.999996422339045, -0.0), (2.0000, 2.0000, 2.0000), "AB_Mines_Scaffolding_Foundation_3x3m_2", _folder)
if a: placed += 1
else: skipped += 1

# Construction: AB_Mines_Scaffolding_Foundation_3x3m_Broken_A_2
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Scaffolding
#   Volume: EMorSimpleShape::OrientedBox, BoxExtent: (187.4, 191.7, 149.3)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (3395.9348, 3227.9077, 1344.1433), (0.0, 0.0, -0.0), (3.7471, 3.8342, 2.9860), "AB_Mines_Scaffolding_Foundation_3x3m_Broken_A_2", _folder)
if a: placed += 1
else: skipped += 1

# Construction: AB_Mines_Scaffolding_Foundation_3x3m_Broken_A10
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Scaffolding
#   Volume: EMorSimpleShape::OrientedBox, BoxExtent: (192.1, 184.7, 149.3)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (4389.841, 4634.9023, 1749.1433), (0.0, 0.0, -0.0), (3.8422, 3.6938, 2.9860), "AB_Mines_Scaffolding_Foundation_3x3m_Broken_A10", _folder)
if a: placed += 1
else: skipped += 1

# Construction: AB_Mines_Scaffolding_Foundation_3x3m_Broken_A11
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Scaffolding
#   Volume: EMorSimpleShape::OrientedBox, BoxExtent: (186.6, 167.0, 149.3)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (4860.7256, 3939.0107, 1749.1433), (0.0, 0.0, -0.0), (3.7315, 3.3404, 2.9860), "AB_Mines_Scaffolding_Foundation_3x3m_Broken_A11", _folder)
if a: placed += 1
else: skipped += 1

# Construction: AB_Mines_Scaffolding_Foundation_3x3m_Broken_A12
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Scaffolding
#   Volume: EMorSimpleShape::OrientedBox, BoxExtent: (202.3, 198.4, 152.6)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (3522.1143, 3534.4502, 2586.1787), (0.0, 0.0, -0.0), (4.0457, 3.9679, 3.0523), "AB_Mines_Scaffolding_Foundation_3x3m_Broken_A12", _folder)
if a: placed += 1
else: skipped += 1

# Construction: AB_Mines_Scaffolding_Foundation_3x3m_Broken_A13
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Scaffolding
#   Volume: EMorSimpleShape::OrientedBox, BoxExtent: (156.1, 120.2, 149.3)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (3648.5835, 4216.05, 1559.1433), (0.0, 0.0, -0.0), (3.1215, 2.4045, 2.9860), "AB_Mines_Scaffolding_Foundation_3x3m_Broken_A13", _folder)
if a: placed += 1
else: skipped += 1

# Construction: AB_Mines_Scaffolding_Foundation_3x3m_Broken_A14_3
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Scaffolding
#   Volume: EMorSimpleShape::OrientedBox, BoxExtent: (161.4, 126.8, 149.3)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (3081.1045, 3442.0146, 1644.1433), (0.0, 0.0, -0.0), (3.2284, 2.5355, 2.9860), "AB_Mines_Scaffolding_Foundation_3x3m_Broken_A14_3", _folder)
if a: placed += 1
else: skipped += 1

# Construction: AB_Mines_Scaffolding_Foundation_3x3m_Broken_A15
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Scaffolding
#   Volume: EMorSimpleShape::OrientedBox, BoxExtent: (187.4, 191.7, 149.3)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (3427.9163, 3255.6494, 1639.1433), (0.0, 0.0, -0.0), (3.7471, 3.8342, 2.9860), "AB_Mines_Scaffolding_Foundation_3x3m_Broken_A15", _folder)
if a: placed += 1
else: skipped += 1

# Construction: AB_Mines_Scaffolding_Foundation_3x3m_Broken_A16
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Scaffolding
#   Volume: EMorSimpleShape::OrientedBox, BoxExtent: (208.5, 232.4, 151.1)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (628.3527, 1181.3857, 874.401), (0.0, 0.0, -0.0), (4.1692, 4.6488, 3.0227), "AB_Mines_Scaffolding_Foundation_3x3m_Broken_A16", _folder)
if a: placed += 1
else: skipped += 1

# Construction: AB_Mines_Scaffolding_Foundation_3x3m_Broken_A17
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Scaffolding
#   Volume: EMorSimpleShape::OrientedBox, BoxExtent: (185.2, 192.1, 149.3)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (1082.4294, 1135.5107, 1194.1433), (0.0, 0.0, -0.0), (3.7045, 3.8418, 2.9860), "AB_Mines_Scaffolding_Foundation_3x3m_Broken_A17", _folder)
if a: placed += 1
else: skipped += 1

# Construction: AB_Mines_Scaffolding_Foundation_3x3m_Broken_A18
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Scaffolding
#   Volume: EMorSimpleShape::OrientedBox, BoxExtent: (177.8, 151.5, 149.3)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (908.79407, 1317.3068, 899.1433), (0.0, 0.0, -0.0), (3.5567, 3.0304, 2.9860), "AB_Mines_Scaffolding_Foundation_3x3m_Broken_A18", _folder)
if a: placed += 1
else: skipped += 1

# Construction: AB_Mines_Scaffolding_Foundation_3x3m_Broken_A19_2
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Scaffolding
#   Volume: EMorSimpleShape::OrientedBox, BoxExtent: (154.8, 118.6, 149.3)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (3717.1477, 3019.0996, 5094.1436), (0.0, 0.0, -0.0), (3.0969, 2.3719, 2.9860), "AB_Mines_Scaffolding_Foundation_3x3m_Broken_A19_2", _folder)
if a: placed += 1
else: skipped += 1

# Construction: AB_Mines_Scaffolding_Foundation_3x3m_Broken_A2
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Scaffolding
#   Volume: EMorSimpleShape::OrientedBox, BoxExtent: (161.4, 126.8, 149.3)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (3076.7473, 3392.2056, 1049.1433), (0.0, 0.0, -0.0), (3.2284, 2.5355, 2.9860), "AB_Mines_Scaffolding_Foundation_3x3m_Broken_A2", _folder)
if a: placed += 1
else: skipped += 1

# Construction: AB_Mines_Scaffolding_Foundation_3x3m_Broken_A20
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Scaffolding
#   Volume: EMorSimpleShape::OrientedBox, BoxExtent: (186.2, 177.0, 153.9)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (3273.8562, 2863.5933, 5086.603), (0.0, 0.0, -0.0), (3.7246, 3.5401, 3.0783), "AB_Mines_Scaffolding_Foundation_3x3m_Broken_A20", _folder)
if a: placed += 1
else: skipped += 1

# Construction: AB_Mines_Scaffolding_Foundation_3x3m_Broken_A21_6
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Scaffolding
#   Volume: EMorSimpleShape::OrientedBox, BoxExtent: (193.1, 198.7, 153.4)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (2951.8513, 2881.6055, 4808.4185), (0.0, 0.0, -0.0), (3.8618, 3.9742, 3.0689), "AB_Mines_Scaffolding_Foundation_3x3m_Broken_A21_6", _folder)
if a: placed += 1
else: skipped += 1

# Construction: AB_Mines_Scaffolding_Foundation_3x3m_Broken_A22_2
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Scaffolding
#   Volume: EMorSimpleShape::OrientedBox, BoxExtent: (189.9, 190.0, 149.3)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (5125.0, 1847.758, 3549.1433), (0.0, 0.0, -0.0), (3.7980, 3.8004, 2.9860), "AB_Mines_Scaffolding_Foundation_3x3m_Broken_A22_2", _folder)
if a: placed += 1
else: skipped += 1

# Construction: AB_Mines_Scaffolding_Foundation_3x3m_Broken_A23_2
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Scaffolding
#   Volume: EMorSimpleShape::OrientedBox, BoxExtent: (168.0, 173.1, 155.8)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (2060.464, 4966.07, 2521.4673), (0.0, 0.0, -0.0), (3.3594, 3.4618, 3.1166), "AB_Mines_Scaffolding_Foundation_3x3m_Broken_A23_2", _folder)
if a: placed += 1
else: skipped += 1

# Construction: AB_Mines_Scaffolding_Foundation_3x3m_Broken_A24
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Scaffolding
#   Volume: EMorSimpleShape::OrientedBox, BoxExtent: (156.4, 168.2, 164.8)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (1002.39667, 4229.883, 2874.3555), (0.0, 0.0, -0.0), (3.1276, 3.3645, 3.2962), "AB_Mines_Scaffolding_Foundation_3x3m_Broken_A24", _folder)
if a: placed += 1
else: skipped += 1

# Construction: AB_Mines_Scaffolding_Foundation_3x3m_Broken_A3_6
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Scaffolding
#   Volume: EMorSimpleShape::OrientedBox, BoxExtent: (179.0, 153.4, 149.3)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (1398.9712, 4651.2812, 847.1433), (0.0, 0.0, -0.0), (3.5800, 3.0682, 2.9860), "AB_Mines_Scaffolding_Foundation_3x3m_Broken_A3_6", _folder)
if a: placed += 1
else: skipped += 1

# Construction: AB_Mines_Scaffolding_Foundation_3x3m_Broken_A4
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Scaffolding
#   Volume: EMorSimpleShape::OrientedBox, BoxExtent: (166.1, 133.7, 149.3)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (2226.0552, 4211.3477, 1099.1433), (0.0, 0.0, -0.0), (3.3218, 2.6741, 2.9860), "AB_Mines_Scaffolding_Foundation_3x3m_Broken_A4", _folder)
if a: placed += 1
else: skipped += 1

# Construction: AB_Mines_Scaffolding_Foundation_3x3m_Broken_A5_20
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Scaffolding
#   Volume: EMorSimpleShape::OrientedBox, BoxExtent: (161.4, 126.8, 149.3)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (2774.5066, 3368.4578, 749.1915), (0.0, 0.0, -0.0), (3.2284, 2.5355, 2.9860), "AB_Mines_Scaffolding_Foundation_3x3m_Broken_A5_20", _folder)
if a: placed += 1
else: skipped += 1

# Construction: AB_Mines_Scaffolding_Foundation_3x3m_Broken_A6
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Scaffolding
#   Volume: EMorSimpleShape::OrientedBox, BoxExtent: (166.1, 133.7, 149.3)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (3423.9734, 4044.4482, 1354.1433), (0.0, 0.0, -0.0), (3.3218, 2.6741, 2.9860), "AB_Mines_Scaffolding_Foundation_3x3m_Broken_A6", _folder)
if a: placed += 1
else: skipped += 1

# Construction: AB_Mines_Scaffolding_Foundation_3x3m_Broken_A9
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Scaffolding
#   Volume: EMorSimpleShape::OrientedBox, BoxExtent: (186.6, 167.0, 149.3)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (4818.632, 4040.6372, 1749.1433), (0.0, 0.0, -0.0), (3.7315, 3.3404, 2.9860), "AB_Mines_Scaffolding_Foundation_3x3m_Broken_A9", _folder)
if a: placed += 1
else: skipped += 1

# Construction: AB_Mines_Scaffolding_Foundation_3x3m_Broken_B_2
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Scaffolding
#   Volume: EMorSimpleShape::OrientedBox, BoxExtent: (140.6, 151.2, 151.7)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (3349.21, 3187.374, 1046.5563), (0.0, 0.0, -0.0), (2.8126, 3.0235, 3.0343), "AB_Mines_Scaffolding_Foundation_3x3m_Broken_B_2", _folder)
if a: placed += 1
else: skipped += 1

# Construction: AB_Mines_Scaffolding_Foundation_3x3m_Broken_B10_33
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Scaffolding
#   Volume: EMorSimpleShape::OrientedBox, BoxExtent: (147.0, 145.4, 151.7)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (1656.8065, 4462.998, 1086.5563), (0.0, 0.0, -0.0), (2.9407, 2.9084, 3.0343), "AB_Mines_Scaffolding_Foundation_3x3m_Broken_B10_33", _folder)
if a: placed += 1
else: skipped += 1

# Construction: AB_Mines_Scaffolding_Foundation_3x3m_Broken_B11_35
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Scaffolding
#   Volume: EMorSimpleShape::OrientedBox, BoxExtent: (156.5, 64.9, 151.7)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (2462.9849, 3333.5264, 748.07996), (0.0, 0.0, -0.0), (3.1291, 1.2975, 3.0343), "AB_Mines_Scaffolding_Foundation_3x3m_Broken_B11_35", _folder)
if a: placed += 1
else: skipped += 1

# Construction: AB_Mines_Scaffolding_Foundation_3x3m_Broken_B12
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Scaffolding
#   Volume: EMorSimpleShape::OrientedBox, BoxExtent: (135.6, 154.5, 151.7)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (4525.495, 4379.166, 1751.5563), (0.0, 0.0, -0.0), (2.7120, 3.0893, 3.0343), "AB_Mines_Scaffolding_Foundation_3x3m_Broken_B12", _folder)
if a: placed += 1
else: skipped += 1

# Construction: AB_Mines_Scaffolding_Foundation_3x3m_Broken_B13
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Scaffolding
#   Volume: EMorSimpleShape::OrientedBox, BoxExtent: (165.5, 167.0, 157.1)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (4782.6973, 4195.0864, 1739.2437), (0.0, 0.0, -0.0), (3.3100, 3.3408, 3.1411), "AB_Mines_Scaffolding_Foundation_3x3m_Broken_B13", _folder)
if a: placed += 1
else: skipped += 1

# Construction: AB_Mines_Scaffolding_Foundation_3x3m_Broken_B14
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Scaffolding
#   Volume: EMorSimpleShape::OrientedBox, BoxExtent: (131.1, 156.7, 151.7)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (4342.2793, 4599.235, 1751.5563), (0.0, 0.0, -0.0), (2.6224, 3.1350, 3.0343), "AB_Mines_Scaffolding_Foundation_3x3m_Broken_B14", _folder)
if a: placed += 1
else: skipped += 1

# Construction: AB_Mines_Scaffolding_Foundation_3x3m_Broken_B15_37
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Scaffolding
#   Volume: EMorSimpleShape::OrientedBox, BoxExtent: (156.5, 64.9, 151.7)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (2459.7063, 3236.2266, 748.07996), (0.0, 0.0, -0.0), (3.1291, 1.2975, 3.0343), "AB_Mines_Scaffolding_Foundation_3x3m_Broken_B15_37", _folder)
if a: placed += 1
else: skipped += 1

# Construction: AB_Mines_Scaffolding_Foundation_3x3m_Broken_B16
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Scaffolding
#   Volume: EMorSimpleShape::OrientedBox, BoxExtent: (167.2, 148.5, 155.0)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (3460.5283, 3454.5415, 2291.4907), (0.0, 0.0, -0.0), (3.3438, 2.9701, 3.0999), "AB_Mines_Scaffolding_Foundation_3x3m_Broken_B16", _folder)
if a: placed += 1
else: skipped += 1

# Construction: AB_Mines_Scaffolding_Foundation_3x3m_Broken_B17_3
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Scaffolding
#   Volume: EMorSimpleShape::OrientedBox, BoxExtent: (140.6, 151.2, 151.7)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (3491.4956, 3313.29, 1939.2539), (0.0, 0.0, -0.0), (2.8126, 3.0235, 3.0343), "AB_Mines_Scaffolding_Foundation_3x3m_Broken_B17_3", _folder)
if a: placed += 1
else: skipped += 1

# Construction: AB_Mines_Scaffolding_Foundation_3x3m_Broken_B18_6
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Scaffolding
#   Volume: EMorSimpleShape::OrientedBox, BoxExtent: (156.5, 64.9, 151.7)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (3073.465, 3330.306, 1346.5563), (0.0, 0.0, -0.0), (3.1291, 1.2975, 3.0343), "AB_Mines_Scaffolding_Foundation_3x3m_Broken_B18_6", _folder)
if a: placed += 1
else: skipped += 1

# Construction: AB_Mines_Scaffolding_Foundation_3x3m_Broken_B19
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Scaffolding
#   Volume: EMorSimpleShape::OrientedBox, BoxExtent: (153.9, 136.6, 151.7)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (1282.0885, 778.6695, 901.5563), (0.0, 0.0, -0.0), (3.0782, 2.7310, 3.0343), "AB_Mines_Scaffolding_Foundation_3x3m_Broken_B19", _folder)
if a: placed += 1
else: skipped += 1

# Construction: AB_Mines_Scaffolding_Foundation_3x3m_Broken_B2_4
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Scaffolding
#   Volume: EMorSimpleShape::OrientedBox, BoxExtent: (63.9, 156.4, 151.7)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (3423.3901, 2723.08, 5091.5566), (0.0, 0.0, -0.0), (1.2779, 3.1271, 3.0343), "AB_Mines_Scaffolding_Foundation_3x3m_Broken_B2_4", _folder)
if a: placed += 1
else: skipped += 1

# Construction: AB_Mines_Scaffolding_Foundation_3x3m_Broken_B20
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Scaffolding
#   Volume: EMorSimpleShape::OrientedBox, BoxExtent: (135.6, 154.5, 151.7)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (4594.1006, 4439.3203, 1751.5563), (0.0, 0.0, -0.0), (2.7120, 3.0893, 3.0343), "AB_Mines_Scaffolding_Foundation_3x3m_Broken_B20", _folder)
if a: placed += 1
else: skipped += 1

# Construction: AB_Mines_Scaffolding_Foundation_3x3m_Broken_B21
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Scaffolding
#   Volume: EMorSimpleShape::OrientedBox, BoxExtent: (191.1, 110.9, 179.6)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (597.2094, 1231.072, 1056.332), (0.0, 0.0, -0.0), (3.8230, 2.2178, 3.5918), "AB_Mines_Scaffolding_Foundation_3x3m_Broken_B21", _folder)
if a: placed += 1
else: skipped += 1

# Construction: AB_Mines_Scaffolding_Foundation_3x3m_Broken_B22
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Scaffolding
#   Volume: EMorSimpleShape::OrientedBox, BoxExtent: (172.7, 119.5, 180.3)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (2926.6052, 4326.231, 3098.789), (0.0, 0.0, -0.0), (3.4538, 2.3908, 3.6067), "AB_Mines_Scaffolding_Foundation_3x3m_Broken_B22", _folder)
if a: placed += 1
else: skipped += 1

# Construction: AB_Mines_Scaffolding_Foundation_3x3m_Broken_B23_6
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Scaffolding
#   Volume: EMorSimpleShape::OrientedBox, BoxExtent: (167.7, 119.0, 156.3)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (2967.148, 2838.7651, 5092.4873), (0.0, 0.0, -0.0), (3.3533, 2.3797, 3.1256), "AB_Mines_Scaffolding_Foundation_3x3m_Broken_B23_6", _folder)
if a: placed += 1
else: skipped += 1

# Construction: AB_Mines_Scaffolding_Foundation_3x3m_Broken_B24
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Scaffolding
#   Volume: EMorSimpleShape::OrientedBox, BoxExtent: (167.2, 112.7, 155.2)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (3227.7344, 2994.2039, 4797.117), (0.0, 0.0, -0.0), (3.3444, 2.2530, 3.1036), "AB_Mines_Scaffolding_Foundation_3x3m_Broken_B24", _folder)
if a: placed += 1
else: skipped += 1

# Construction: AB_Mines_Scaffolding_Foundation_3x3m_Broken_B25
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Scaffolding
#   Volume: EMorSimpleShape::OrientedBox, BoxExtent: (175.4, 144.0, 155.7)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (3281.9172, 2827.4985, 5365.797), (0.0, 0.0, -0.0), (3.5086, 2.8797, 3.1136), "AB_Mines_Scaffolding_Foundation_3x3m_Broken_B25", _folder)
if a: placed += 1
else: skipped += 1

# Construction: AB_Mines_Scaffolding_Foundation_3x3m_Broken_B26_2
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Scaffolding
#   Volume: EMorSimpleShape::OrientedBox, BoxExtent: (182.5, 169.8, 204.0)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (967.3084, 4527.913, 2820.082), (0.0, 0.0, -0.0), (3.6494, 3.3965, 4.0797), "AB_Mines_Scaffolding_Foundation_3x3m_Broken_B26_2", _folder)
if a: placed += 1
else: skipped += 1

# Construction: AB_Mines_Scaffolding_Foundation_3x3m_Broken_B27
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Scaffolding
#   Volume: EMorSimpleShape::OrientedBox, BoxExtent: (138.9, 166.6, 158.7)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (1029.0836, 3762.7478, 2869.6533), (0.0, 0.0, -0.0), (2.7786, 3.3314, 3.1745), "AB_Mines_Scaffolding_Foundation_3x3m_Broken_B27", _folder)
if a: placed += 1
else: skipped += 1

# Construction: AB_Mines_Scaffolding_Foundation_3x3m_Broken_B3
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Scaffolding
#   Volume: EMorSimpleShape::OrientedBox, BoxExtent: (158.1, 72.1, 151.7)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (1934.5221, 4316.353, 1101.5563), (0.0, 0.0, -0.0), (3.1615, 1.4421, 3.0343), "AB_Mines_Scaffolding_Foundation_3x3m_Broken_B3", _folder)
if a: placed += 1
else: skipped += 1

# Construction: AB_Mines_Scaffolding_Foundation_3x3m_Broken_B4
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Scaffolding
#   Volume: EMorSimpleShape::OrientedBox, BoxExtent: (93.1, 162.1, 151.7)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (1419.6096, 5026.259, 1086.5563), (0.0, 0.0, -0.0), (1.8615, 3.2414, 3.0343), "AB_Mines_Scaffolding_Foundation_3x3m_Broken_B4", _folder)
if a: placed += 1
else: skipped += 1

# Construction: AB_Mines_Scaffolding_Foundation_3x3m_Broken_B5
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Scaffolding
#   Volume: EMorSimpleShape::OrientedBox, BoxExtent: (93.1, 162.1, 151.7)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (1495.6736, 4736.0625, 1086.5563), (0.0, 0.0, -0.0), (1.8615, 3.2414, 3.0343), "AB_Mines_Scaffolding_Foundation_3x3m_Broken_B5", _folder)
if a: placed += 1
else: skipped += 1

# Construction: AB_Mines_Scaffolding_Foundation_3x3m_Broken_B6
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Scaffolding
#   Volume: EMorSimpleShape::OrientedBox, BoxExtent: (93.1, 162.1, 151.7)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (1343.5454, 5316.457, 1086.5563), (0.0, 0.0, -0.0), (1.8615, 3.2414, 3.0343), "AB_Mines_Scaffolding_Foundation_3x3m_Broken_B6", _folder)
if a: placed += 1
else: skipped += 1

# Construction: AB_Mines_Scaffolding_Foundation_3x3m_Broken_B7
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Scaffolding
#   Volume: EMorSimpleShape::OrientedBox, BoxExtent: (158.1, 72.1, 151.7)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (2538.8604, 4233.4355, 1101.5563), (0.0, 0.0, -0.0), (3.1615, 1.4421, 3.0343), "AB_Mines_Scaffolding_Foundation_3x3m_Broken_B7", _folder)
if a: placed += 1
else: skipped += 1

# Construction: AB_Mines_Scaffolding_Foundation_3x3m_Broken_B8
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Scaffolding
#   Volume: EMorSimpleShape::OrientedBox, BoxExtent: (158.1, 72.1, 151.7)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (2836.0752, 4192.655, 1101.5563), (0.0, 0.0, -0.0), (3.1615, 1.4421, 3.0343), "AB_Mines_Scaffolding_Foundation_3x3m_Broken_B8", _folder)
if a: placed += 1
else: skipped += 1

# Construction: AB_Mines_Scaffolding_Foundation_3x3m_Broken_B9
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Scaffolding
#   Volume: EMorSimpleShape::OrientedBox, BoxExtent: (158.1, 72.1, 151.7)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (3143.1968, 4150.5146, 1101.5563), (0.0, 0.0, -0.0), (3.1615, 1.4421, 3.0343), "AB_Mines_Scaffolding_Foundation_3x3m_Broken_B9", _folder)
if a: placed += 1
else: skipped += 1

# Construction: AB_Mines_Scaffolding_Platform_1x1x2m_5
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Scaffolding
#   Volume: EMorSimpleShape::Empty, BoxExtent: (100.0, 100.0, 100.0)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (4940.0, 2000.0, 810.0), (0.0, 0.0, -0.0), (2.0000, 2.0000, 2.0000), "AB_Mines_Scaffolding_Platform_1x1x2m_5", _folder)
if a: placed += 1
else: skipped += 1

# Construction: AB_Mines_Scaffolding_Platform_1x1x2m10_5
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Scaffolding
#   Volume: EMorSimpleShape::Empty, BoxExtent: (100.0, 100.0, 100.0)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (3650.0, 4000.0, 710.0), (0.0, 179.99991120752276, -0.0), (2.0000, 2.0000, 2.0000), "AB_Mines_Scaffolding_Platform_1x1x2m10_5", _folder)
if a: placed += 1
else: skipped += 1

# Construction: AB_Mines_Scaffolding_Platform_1x1x2m11
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Scaffolding
#   Volume: EMorSimpleShape::Empty, BoxExtent: (100.0, 100.0, 100.0)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (3650.0, 2400.0, 1010.0), (0.0, 0.0, -0.0), (2.0000, 2.0000, 2.0000), "AB_Mines_Scaffolding_Platform_1x1x2m11", _folder)
if a: placed += 1
else: skipped += 1

# Construction: AB_Mines_Scaffolding_Platform_1x1x2m12
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Scaffolding
#   Volume: EMorSimpleShape::Empty, BoxExtent: (100.0, 100.0, 100.0)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (5000.0, 2520.0, 800.0), (0.0, 0.0, -0.0), (2.0000, 2.0000, 2.0000), "AB_Mines_Scaffolding_Platform_1x1x2m12", _folder)
if a: placed += 1
else: skipped += 1

# Construction: AB_Mines_Scaffolding_Platform_1x1x2m13
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Scaffolding
#   Volume: EMorSimpleShape::Empty, BoxExtent: (100.0, 100.0, 100.0)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (5000.0, 2520.0, 1000.0), (0.0, 0.0, -0.0), (2.0000, 2.0000, 2.0000), "AB_Mines_Scaffolding_Platform_1x1x2m13", _folder)
if a: placed += 1
else: skipped += 1

# Construction: AB_Mines_Scaffolding_Platform_1x1x2m14
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Scaffolding
#   Volume: EMorSimpleShape::Empty, BoxExtent: (100.0, 100.0, 100.0)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (5100.0, 2520.0, 800.0), (0.0, 0.0, -0.0), (2.0000, 2.0000, 2.0000), "AB_Mines_Scaffolding_Platform_1x1x2m14", _folder)
if a: placed += 1
else: skipped += 1

# Construction: AB_Mines_Scaffolding_Platform_1x1x2m15
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Scaffolding
#   Volume: EMorSimpleShape::Empty, BoxExtent: (100.0, 100.0, 100.0)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (5100.0, 2520.0, 1000.0), (0.0, 0.0, -0.0), (2.0000, 2.0000, 2.0000), "AB_Mines_Scaffolding_Platform_1x1x2m15", _folder)
if a: placed += 1
else: skipped += 1

# Construction: AB_Mines_Scaffolding_Platform_1x1x2m16_5
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Scaffolding
#   Volume: EMorSimpleShape::Empty, BoxExtent: (100.0, 100.0, 100.0)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (3846.1533, 2634.9336, 3545.0), (-0.0, -177.18744864242285, -0.0), (2.0000, 2.0000, 2.0000), "AB_Mines_Scaffolding_Platform_1x1x2m16_5", _folder)
if a: placed += 1
else: skipped += 1

# Construction: AB_Mines_Scaffolding_Platform_1x1x2m2
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Scaffolding
#   Volume: EMorSimpleShape::Empty, BoxExtent: (100.0, 100.0, 100.0)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (4940.0, 2000.0, 1010.0), (0.0, 0.0, -0.0), (2.0000, 2.0000, 2.0000), "AB_Mines_Scaffolding_Platform_1x1x2m2", _folder)
if a: placed += 1
else: skipped += 1

# Construction: AB_Mines_Scaffolding_Platform_1x1x2m3
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Scaffolding
#   Volume: EMorSimpleShape::Empty, BoxExtent: (100.0, 100.0, 100.0)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (5040.0, 2000.0, 810.0), (0.0, 0.0, -0.0), (2.0000, 2.0000, 2.0000), "AB_Mines_Scaffolding_Platform_1x1x2m3", _folder)
if a: placed += 1
else: skipped += 1

# Construction: AB_Mines_Scaffolding_Platform_1x1x2m4
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Scaffolding
#   Volume: EMorSimpleShape::Empty, BoxExtent: (100.0, 100.0, 100.0)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (5040.0, 2000.0, 1010.0), (0.0, 0.0, -0.0), (2.0000, 2.0000, 2.0000), "AB_Mines_Scaffolding_Platform_1x1x2m4", _folder)
if a: placed += 1
else: skipped += 1

# Construction: AB_Mines_Scaffolding_Platform_1x1x2m5
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Scaffolding
#   Volume: EMorSimpleShape::Empty, BoxExtent: (100.0, 100.0, 100.0)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (3390.0, 2000.0, 810.0), (0.0, 0.0, -0.0), (2.0000, 2.0000, 2.0000), "AB_Mines_Scaffolding_Platform_1x1x2m5", _folder)
if a: placed += 1
else: skipped += 1

# Construction: AB_Mines_Scaffolding_Platform_1x1x2m6
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Scaffolding
#   Volume: EMorSimpleShape::Empty, BoxExtent: (100.0, 100.0, 100.0)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (3390.0, 2000.0, 1010.0), (0.0, 0.0, -0.0), (2.0000, 2.0000, 2.0000), "AB_Mines_Scaffolding_Platform_1x1x2m6", _folder)
if a: placed += 1
else: skipped += 1

# Construction: AB_Mines_Scaffolding_Platform_1x1x2m7_16
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Scaffolding
#   Volume: EMorSimpleShape::Empty, BoxExtent: (100.0, 100.0, 100.0)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (3150.0, 2000.0, 1600.0), (0.0, 90.00011648875932, -0.0), (2.0000, 2.0000, 2.0000), "AB_Mines_Scaffolding_Platform_1x1x2m7_16", _folder)
if a: placed += 1
else: skipped += 1

# Construction: AB_Mines_Scaffolding_Platform_1x1x2m8
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Scaffolding
#   Volume: EMorSimpleShape::Empty, BoxExtent: (100.0, 100.0, 100.0)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (3650.0, 2800.0, 710.0), (0.0, 0.0, -0.0), (2.0000, 2.0000, 2.0000), "AB_Mines_Scaffolding_Platform_1x1x2m8", _folder)
if a: placed += 1
else: skipped += 1

# Construction: AB_Mines_Scaffolding_Platform_1x1x2m9
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Scaffolding
#   Volume: EMorSimpleShape::Empty, BoxExtent: (100.0, 100.0, 100.0)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (3650.0, 2400.0, 810.0), (0.0, 0.0, -0.0), (2.0000, 2.0000, 2.0000), "AB_Mines_Scaffolding_Platform_1x1x2m9", _folder)
if a: placed += 1
else: skipped += 1

# Construction: AB_Mines_Scaffolding_Platform_1x3x2m2
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Scaffolding
#   Volume: EMorSimpleShape::Empty, BoxExtent: (100.0, 100.0, 100.0)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (2640.0, 1800.0, 900.0), (0.0, 0.0, -0.0), (2.0000, 2.0000, 2.0000), "AB_Mines_Scaffolding_Platform_1x3x2m2", _folder)
if a: placed += 1
else: skipped += 1

# Construction: AB_Mines_Scaffolding_Platform_1x3x3m2
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Scaffolding
#   Volume: EMorSimpleShape::Empty, BoxExtent: (100.0, 100.0, 100.0)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (2740.0, 1800.0, 950.0), (0.0, 0.0, -0.0), (2.0000, 2.0000, 2.0000), "AB_Mines_Scaffolding_Platform_1x3x3m2", _folder)
if a: placed += 1
else: skipped += 1

# Construction: AB_Mines_Scaffolding_Platform_3x10
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Scaffolding
#   Volume: EMorSimpleShape::Empty, BoxExtent: (100.0, 100.0, 100.0)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (970.91345, 3552.5073, 4440.0), (0.0, 5.625041329299785, -0.0), (2.0000, 2.0000, 2.0000), "AB_Mines_Scaffolding_Platform_3x10", _folder)
if a: placed += 1
else: skipped += 1

# Construction: AB_Mines_Scaffolding_Platform_3x11
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Scaffolding
#   Volume: EMorSimpleShape::Empty, BoxExtent: (100.0, 100.0, 100.0)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (1000.31946, 3253.9514, 4440.0), (0.0, 5.625041329299785, -0.0), (2.0000, 2.0000, 2.0000), "AB_Mines_Scaffolding_Platform_3x11", _folder)
if a: placed += 1
else: skipped += 1

# Construction: AB_Mines_Scaffolding_Platform_3x2_5
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Scaffolding
#   Volume: EMorSimpleShape::Empty, BoxExtent: (100.0, 100.0, 100.0)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (3255.0005, 1840.0001, 950.0), (0.0, 90.00004680423052, -0.0), (2.0000, 2.0000, 2.0000), "AB_Mines_Scaffolding_Platform_3x2_5", _folder)
if a: placed += 1
else: skipped += 1

# Construction: AB_Mines_Scaffolding_Platform_3x3_2
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Scaffolding
#   Volume: EMorSimpleShape::Empty, BoxExtent: (100.0, 100.0, 100.0)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (1239.4657, 5262.7573, 950.0), (-0.0, -74.99990873202879, -0.0), (2.0000, 2.0000, 2.0000), "AB_Mines_Scaffolding_Platform_3x3_2", _folder)
if a: placed += 1
else: skipped += 1

# Construction: AB_Mines_Scaffolding_Platform_3x3x2m_2
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Scaffolding
#   Volume: EMorSimpleShape::Empty, BoxExtent: (100.0, 100.0, 100.0)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (1250.7195, 5191.378, 893.0), (0.0, 15.000073607810464, -0.0), (2.0000, 2.0000, 2.0000), "AB_Mines_Scaffolding_Platform_3x3x2m_2", _folder)
if a: placed += 1
else: skipped += 1

# Construction: AB_Mines_Scaffolding_Platform_3x3x2m2
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Scaffolding
#   Volume: EMorSimpleShape::Empty, BoxExtent: (100.0, 100.0, 100.0)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (1329.4005, 4897.737, 893.0), (0.0, 15.000073607810464, -0.0), (2.0000, 2.0000, 2.0000), "AB_Mines_Scaffolding_Platform_3x3x2m2", _folder)
if a: placed += 1
else: skipped += 1

# Construction: AB_Mines_Scaffolding_Platform_3x3x2m_Open_2
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Scaffolding
#   Volume: EMorSimpleShape::Empty, BoxExtent: (100.0, 100.0, 100.0)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (2250.0, 3280.0, 4090.0), (0.0, 0.0, -0.0), (2.0000, 2.0000, 2.0000), "AB_Mines_Scaffolding_Platform_3x3x2m_Open_2", _folder)
if a: placed += 1
else: skipped += 1

# Construction: AB_Mines_Scaffolding_Platform_3x3x2m_Open2
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Scaffolding
#   Volume: EMorSimpleShape::Empty, BoxExtent: (100.0, 100.0, 100.0)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (2250.0, 3280.0, 4285.0), (0.0, 0.0, -0.0), (2.0000, 2.0000, 2.0000), "AB_Mines_Scaffolding_Platform_3x3x2m_Open2", _folder)
if a: placed += 1
else: skipped += 1

# Construction: AB_Mines_Scaffolding_Platform_3x3x2m_Open3
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Scaffolding
#   Volume: EMorSimpleShape::Empty, BoxExtent: (100.0, 100.0, 100.0)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (2250.0, 3280.0, 4480.0), (0.0, 0.0, -0.0), (2.0000, 2.0000, 2.0000), "AB_Mines_Scaffolding_Platform_3x3x2m_Open3", _folder)
if a: placed += 1
else: skipped += 1

# Construction: AB_Mines_Scaffolding_Platform_3x3x2m_Open4
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Scaffolding
#   Volume: EMorSimpleShape::Empty, BoxExtent: (100.0, 100.0, 100.0)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (2250.0, 3280.0, 4675.0), (0.0, 0.0, -0.0), (2.0000, 2.0000, 2.0000), "AB_Mines_Scaffolding_Platform_3x3x2m_Open4", _folder)
if a: placed += 1
else: skipped += 1

# Construction: AB_Mines_Scaffolding_Platform_3x3x2m_Open5
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Scaffolding
#   Volume: EMorSimpleShape::Empty, BoxExtent: (100.0, 100.0, 100.0)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (2250.0, 3280.0, 4870.0), (0.0, 0.0, -0.0), (2.0000, 2.0000, 2.0000), "AB_Mines_Scaffolding_Platform_3x3x2m_Open5", _folder)
if a: placed += 1
else: skipped += 1

# Construction: AB_Mines_Scaffolding_Platform_3x3x3__2
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Scaffolding
#   Volume: EMorSimpleShape::Empty, BoxExtent: (100.0, 100.0, 100.0)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (959.9059, 3252.8364, 4150.0), (0.0, 5.625095791732844, -0.0), (2.0000, 2.0000, 2.0000), "AB_Mines_Scaffolding_Platform_3x3x3__2", _folder)
if a: placed += 1
else: skipped += 1

# Construction: AB_Mines_Scaffolding_Platform_3x3x3_Open_5
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Scaffolding
#   Volume: EMorSimpleShape::Empty, BoxExtent: (100.0, 100.0, 100.0)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (3335.0, 1809.9995, 1680.0), (-0.0, -0.0002441406282020384, -0.0), (2.0000, 2.0000, 2.0000), "AB_Mines_Scaffolding_Platform_3x3x3_Open_5", _folder)
if a: placed += 1
else: skipped += 1

# Construction: AB_Mines_Scaffolding_Platform_3x3x3_Open2
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Scaffolding
#   Volume: EMorSimpleShape::Empty, BoxExtent: (100.0, 100.0, 100.0)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (2570.0, 1810.0001, 1700.0), (0.0, 179.99991120752276, -0.0), (2.0000, 2.0000, 2.0000), "AB_Mines_Scaffolding_Platform_3x3x3_Open2", _folder)
if a: placed += 1
else: skipped += 1

# Construction: AB_Mines_Scaffolding_Platform_3x3x3_Open3
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Scaffolding
#   Volume: EMorSimpleShape::Empty, BoxExtent: (100.0, 100.0, 100.0)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (2949.9998, 1645.0, 2300.0), (-0.0, -90.00009542133918, -0.0), (2.0000, 2.0000, 2.0000), "AB_Mines_Scaffolding_Platform_3x3x3_Open3", _folder)
if a: placed += 1
else: skipped += 1

# Construction: AB_Mines_Scaffolding_Platform_3x3x3_Open_Broken_A_2
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Scaffolding
#   Volume: EMorSimpleShape::Empty, BoxExtent: (100.0, 100.0, 100.0)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (2745.0, 1809.9996, 1650.0), (-0.0, -90.00023965222978, -0.0), (2.0000, 2.0000, 2.0000), "AB_Mines_Scaffolding_Platform_3x3x3_Open_Broken_A_2", _folder)
if a: placed += 1
else: skipped += 1

# Construction: AB_Mines_Scaffolding_Platform_3x3x3_Open_Broken_A2_8
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Scaffolding
#   Volume: EMorSimpleShape::Empty, BoxExtent: (100.0, 100.0, 100.0)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (3160.0, 1810.0005, 1650.0), (0.0, 89.999630318475, -0.0), (2.0000, 2.0000, 2.0000), "AB_Mines_Scaffolding_Platform_3x3x3_Open_Broken_A2_8", _folder)
if a: placed += 1
else: skipped += 1

# Construction: AB_Mines_Scaffolding_Platform_3x3x3_Open_Broken_A3
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Scaffolding
#   Volume: EMorSimpleShape::Empty, BoxExtent: (100.0, 100.0, 100.0)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (2945.0002, 2025.0, 1370.0), (-0.0, -0.00012207030837116422, -0.0), (2.0000, 2.0000, 2.0000), "AB_Mines_Scaffolding_Platform_3x3x3_Open_Broken_A3", _folder)
if a: placed += 1
else: skipped += 1

# Construction: AB_Mines_Scaffolding_Platform_3x3x3_Open_Broken_A8
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Scaffolding
#   Volume: EMorSimpleShape::Empty, BoxExtent: (100.0, 100.0, 100.0)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (3527.2808, 3544.057, 2872.9873), (2.2411100707216183e-08, -36.17675752963696, 7.638301727855655), (2.0000, 2.0000, 2.0000), "AB_Mines_Scaffolding_Platform_3x3x3_Open_Broken_A8", _folder)
if a: placed += 1
else: skipped += 1

# Construction: AB_Mines_Scaffolding_Platform_3x4_6
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Scaffolding
#   Volume: EMorSimpleShape::Empty, BoxExtent: (100.0, 100.0, 100.0)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (949.6881, 5185.112, 950.0), (-0.0, -74.99990873202879, -0.0), (2.0000, 2.0000, 2.0000), "AB_Mines_Scaffolding_Platform_3x4_6", _folder)
if a: placed += 1
else: skipped += 1

# Construction: AB_Mines_Scaffolding_Platform_3x5_10
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Scaffolding
#   Volume: EMorSimpleShape::Empty, BoxExtent: (100.0, 100.0, 100.0)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (897.9241, 5378.296, 950.0), (-0.0, -74.99990873202879, -0.0), (2.0000, 2.0000, 2.0000), "AB_Mines_Scaffolding_Platform_3x5_10", _folder)
if a: placed += 1
else: skipped += 1

# Construction: AB_Mines_Scaffolding_Platform_3x6
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Scaffolding
#   Volume: EMorSimpleShape::Empty, BoxExtent: (100.0, 100.0, 100.0)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (659.91046, 5107.4653, 950.0), (-0.0, -74.99990873202879, -0.0), (2.0000, 2.0000, 2.0000), "AB_Mines_Scaffolding_Platform_3x6", _folder)
if a: placed += 1
else: skipped += 1

# Construction: AB_Mines_Scaffolding_Platform_3x7
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Scaffolding
#   Volume: EMorSimpleShape::Empty, BoxExtent: (100.0, 100.0, 100.0)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (608.1464, 5300.6494, 950.0), (-0.0, -74.99990873202879, -0.0), (2.0000, 2.0000, 2.0000), "AB_Mines_Scaffolding_Platform_3x7", _folder)
if a: placed += 1
else: skipped += 1

# Construction: AB_Mines_Scaffolding_Platform_3x8
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Scaffolding
#   Volume: EMorSimpleShape::Empty, BoxExtent: (100.0, 100.0, 100.0)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (556.38245, 5493.8335, 950.0), (-0.0, -74.99990873202879, -0.0), (2.0000, 2.0000, 2.0000), "AB_Mines_Scaffolding_Platform_3x8", _folder)
if a: placed += 1
else: skipped += 1

# Construction: AB_Mines_Scaffolding_Platform_3x9
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Scaffolding
#   Volume: EMorSimpleShape::Empty, BoxExtent: (100.0, 100.0, 100.0)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (1029.2347, 2960.374, 4440.0), (0.0, 5.625041674313767, -0.0), (2.0000, 2.0000, 2.0000), "AB_Mines_Scaffolding_Platform_3x9", _folder)
if a: placed += 1
else: skipped += 1

# Construction: AB_Mines_Scaffolding_Platform_Pillar_3M_8
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Scaffolding
#   Volume: EMorSimpleShape::Empty, BoxExtent: (100.0, 100.0, 100.0)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (3290.0, 2000.0, 950.0), (0.0, 0.0, -0.0), (2.0000, 2.0000, 2.0000), "AB_Mines_Scaffolding_Platform_Pillar_3M_8", _folder)
if a: placed += 1
else: skipped += 1

# Construction: AB_Mines_Scaffolding_Platform_Pillar_3M11
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Scaffolding
#   Volume: EMorSimpleShape::Empty, BoxExtent: (100.0, 100.0, 100.0)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (3650.0, 4000.0, 950.0), (0.0, 179.99991120752276, -0.0), (2.0000, 2.0000, 2.0000), "AB_Mines_Scaffolding_Platform_Pillar_3M11", _folder)
if a: placed += 1
else: skipped += 1

# Construction: AB_Mines_Scaffolding_Platform_Pillar_3M12_1
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Scaffolding
#   Volume: EMorSimpleShape::Empty, BoxExtent: (100.0, 100.0, 100.0)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (3846.1533, 2634.9336, 4095.0), (-0.0, -177.18744864242285, -0.0), (2.0000, 2.0000, 2.0000), "AB_Mines_Scaffolding_Platform_Pillar_3M12_1", _folder)
if a: placed += 1
else: skipped += 1

# Construction: AB_Mines_Scaffolding_Platform_Pillar_3M13
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Scaffolding
#   Volume: EMorSimpleShape::Empty, BoxExtent: (100.0, 100.0, 100.0)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (3846.1533, 2634.9336, 3795.0), (-0.0, -177.18744864242285, -0.0), (2.0000, 2.0000, 2.0000), "AB_Mines_Scaffolding_Platform_Pillar_3M13", _folder)
if a: placed += 1
else: skipped += 1

# Construction: AB_Mines_Scaffolding_Platform_Pillar_3M15_3
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Scaffolding
#   Volume: EMorSimpleShape::Empty, BoxExtent: (100.0, 100.0, 100.0)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (2427.8635, 2565.2593, 4095.0), (0.0, 2.812633507231197, -0.0), (2.0000, 2.0000, 2.0000), "AB_Mines_Scaffolding_Platform_Pillar_3M15_3", _folder)
if a: placed += 1
else: skipped += 1

# Construction: AB_Mines_Scaffolding_Platform_Pillar_3M16_4
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Scaffolding
#   Volume: EMorSimpleShape::Empty, BoxExtent: (100.0, 100.0, 100.0)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (2427.8635, 2565.2593, 3795.0), (0.0, 2.812633507231197, -0.0), (2.0000, 2.0000, 2.0000), "AB_Mines_Scaffolding_Platform_Pillar_3M16_4", _folder)
if a: placed += 1
else: skipped += 1

# Construction: AB_Mines_Scaffolding_Platform_Pillar_3M17
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Scaffolding
#   Volume: EMorSimpleShape::Empty, BoxExtent: (100.0, 100.0, 100.0)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (2427.8635, 2565.2593, 3495.0), (0.0, 2.812633507231197, -0.0), (2.0000, 2.0000, 2.0000), "AB_Mines_Scaffolding_Platform_Pillar_3M17", _folder)
if a: placed += 1
else: skipped += 1

# Construction: AB_Mines_Scaffolding_Platform_Pillar_3M18_17
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Scaffolding
#   Volume: EMorSimpleShape::Empty, BoxExtent: (100.0, 100.0, 100.0)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (2427.8635, 2565.2593, 3195.0), (0.0, 2.8126339660113815, -0.0), (2.0000, 2.0000, 2.0000), "AB_Mines_Scaffolding_Platform_Pillar_3M18_17", _folder)
if a: placed += 1
else: skipped += 1

# Construction: AB_Mines_Scaffolding_Platform_Pillar_3M2
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Scaffolding
#   Volume: EMorSimpleShape::Empty, BoxExtent: (100.0, 100.0, 100.0)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (3290.0, 2000.0, 1250.0), (0.0, 0.0, -0.0), (2.0000, 2.0000, 2.0000), "AB_Mines_Scaffolding_Platform_Pillar_3M2", _folder)
if a: placed += 1
else: skipped += 1

# Construction: AB_Mines_Scaffolding_Platform_Pillar_3M24
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Scaffolding
#   Volume: EMorSimpleShape::Empty, BoxExtent: (100.0, 100.0, 100.0)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (2693.922, 4302.498, 4095.0), (-0.0, -120.93718160526006, -0.0), (2.0000, 2.0000, 2.0000), "AB_Mines_Scaffolding_Platform_Pillar_3M24", _folder)
if a: placed += 1
else: skipped += 1

# Construction: AB_Mines_Scaffolding_Platform_Pillar_3M25
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Scaffolding
#   Volume: EMorSimpleShape::Empty, BoxExtent: (100.0, 100.0, 100.0)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (2693.922, 4302.498, 3795.0), (-0.0, -120.93718160526006, -0.0), (2.0000, 2.0000, 2.0000), "AB_Mines_Scaffolding_Platform_Pillar_3M25", _folder)
if a: placed += 1
else: skipped += 1

# Construction: AB_Mines_Scaffolding_Platform_Pillar_3M26
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Scaffolding
#   Volume: EMorSimpleShape::Empty, BoxExtent: (100.0, 100.0, 100.0)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (2693.922, 4302.498, 3495.0), (-0.0, -120.93718160526006, -0.0), (2.0000, 2.0000, 2.0000), "AB_Mines_Scaffolding_Platform_Pillar_3M26", _folder)
if a: placed += 1
else: skipped += 1

# Construction: AB_Mines_Scaffolding_Platform_Pillar_3M27
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Scaffolding
#   Volume: EMorSimpleShape::Empty, BoxExtent: (100.0, 100.0, 100.0)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (3775.587, 3769.0662, 4095.0), (0.0, 149.0628734871105, -0.0), (2.0000, 2.0000, 2.0000), "AB_Mines_Scaffolding_Platform_Pillar_3M27", _folder)
if a: placed += 1
else: skipped += 1

# Construction: AB_Mines_Scaffolding_Platform_Pillar_3M28
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Scaffolding
#   Volume: EMorSimpleShape::Empty, BoxExtent: (100.0, 100.0, 100.0)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (3775.587, 3769.0662, 3795.0), (0.0, 149.0628734871105, -0.0), (2.0000, 2.0000, 2.0000), "AB_Mines_Scaffolding_Platform_Pillar_3M28", _folder)
if a: placed += 1
else: skipped += 1

# Construction: AB_Mines_Scaffolding_Platform_Pillar_3M29
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Scaffolding
#   Volume: EMorSimpleShape::Empty, BoxExtent: (100.0, 100.0, 100.0)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (3775.587, 3769.0662, 3495.0), (0.0, 149.0628734871105, -0.0), (2.0000, 2.0000, 2.0000), "AB_Mines_Scaffolding_Platform_Pillar_3M29", _folder)
if a: placed += 1
else: skipped += 1

# Construction: AB_Mines_Scaffolding_Platform_Pillar_3M3
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Scaffolding
#   Volume: EMorSimpleShape::Empty, BoxExtent: (100.0, 100.0, 100.0)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (3190.0, 2000.0, 950.0), (0.0, 0.0, -0.0), (2.0000, 2.0000, 2.0000), "AB_Mines_Scaffolding_Platform_Pillar_3M3", _folder)
if a: placed += 1
else: skipped += 1

# Construction: AB_Mines_Scaffolding_Platform_Pillar_3M4
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Scaffolding
#   Volume: EMorSimpleShape::Empty, BoxExtent: (100.0, 100.0, 100.0)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (3190.0, 2000.0, 1250.0), (0.0, 0.0, -0.0), (2.0000, 2.0000, 2.0000), "AB_Mines_Scaffolding_Platform_Pillar_3M4", _folder)
if a: placed += 1
else: skipped += 1

# Construction: AB_Mines_Scaffolding_Platform_Pillar_3M5_2
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Scaffolding
#   Volume: EMorSimpleShape::Empty, BoxExtent: (100.0, 100.0, 100.0)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (5000.0, 2520.0, 1250.0), (0.0, 0.0, -0.0), (2.0000, 2.0000, 2.0000), "AB_Mines_Scaffolding_Platform_Pillar_3M5_2", _folder)
if a: placed += 1
else: skipped += 1

# Construction: AB_Mines_Scaffolding_Platform_Pillar_3M6
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Scaffolding
#   Volume: EMorSimpleShape::Empty, BoxExtent: (100.0, 100.0, 100.0)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (5100.0, 2520.0, 1250.0), (0.0, 0.0, -0.0), (2.0000, 2.0000, 2.0000), "AB_Mines_Scaffolding_Platform_Pillar_3M6", _folder)
if a: placed += 1
else: skipped += 1

# Construction: AB_Mines_Scaffolding_Platform_Pillar_3M7
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Scaffolding
#   Volume: EMorSimpleShape::Empty, BoxExtent: (100.0, 100.0, 100.0)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (5000.0, 2520.0, 1650.0), (0.0, 0.0, -0.0), (2.0000, 2.0000, 2.0000), "AB_Mines_Scaffolding_Platform_Pillar_3M7", _folder)
if a: placed += 1
else: skipped += 1

# Construction: AB_Mines_Scaffolding_Platform_Pillar_3M8
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Scaffolding
#   Volume: EMorSimpleShape::Empty, BoxExtent: (100.0, 100.0, 100.0)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (5100.0, 2520.0, 1650.0), (0.0, 0.0, -0.0), (2.0000, 2.0000, 2.0000), "AB_Mines_Scaffolding_Platform_Pillar_3M8", _folder)
if a: placed += 1
else: skipped += 1

# Construction: AB_Mines_Scaffolding_Platform_Pillar_3M9
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Scaffolding
#   Volume: EMorSimpleShape::Empty, BoxExtent: (100.0, 100.0, 100.0)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (3650.0, 2800.0, 950.0), (0.0, 0.0, -0.0), (2.0000, 2.0000, 2.0000), "AB_Mines_Scaffolding_Platform_Pillar_3M9", _folder)
if a: placed += 1
else: skipped += 1

# Construction: AB_Mines_Scaffolding_Platform_Pillar_3M_Top_B15
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Scaffolding
#   Volume: EMorSimpleShape::Empty, BoxExtent: (100.0, 100.0, 100.0)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (2713.172, 4214.0166, 4395.0), (-0.0, -30.93752887049159, -0.0), (2.0000, 2.0000, 2.0000), "AB_Mines_Scaffolding_Platform_Pillar_3M_Top_B15", _folder)
if a: placed += 1
else: skipped += 1

# Construction: AB_Mines_Scaffolding_Platform_Pillar_3M_Top_B16
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Scaffolding
#   Volume: EMorSimpleShape::Empty, BoxExtent: (100.0, 100.0, 100.0)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (3687.4473, 3748.446, 4395.0), (-0.0, -120.93761953541703, -0.0), (2.0000, 2.0000, 2.0000), "AB_Mines_Scaffolding_Platform_Pillar_3M_Top_B16", _folder)
if a: placed += 1
else: skipped += 1

# Construction: AB_Mines_Scaffolding_Platform_Pillar_3M_Top_B2
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Scaffolding
#   Volume: EMorSimpleShape::Empty, BoxExtent: (100.0, 100.0, 100.0)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (4870.0, 2000.0, 1250.0), (0.0, 89.99997063746636, -0.0), (2.0000, 2.0000, 2.0000), "AB_Mines_Scaffolding_Platform_Pillar_3M_Top_B2", _folder)
if a: placed += 1
else: skipped += 1

# Construction: AB_Mines_Scaffolding_Platform_Pillar_3M_Top_B3
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Scaffolding
#   Volume: EMorSimpleShape::Empty, BoxExtent: (100.0, 100.0, 100.0)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (5110.0, 2000.0002, 1250.0), (-0.0, -89.99981506294705, -0.0), (2.0000, 2.0000, 2.0000), "AB_Mines_Scaffolding_Platform_Pillar_3M_Top_B3", _folder)
if a: placed += 1
else: skipped += 1

# Construction: AB_Mines_Scaffolding_Platform_Pillar_3M_Top_B4
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Scaffolding
#   Volume: EMorSimpleShape::Empty, BoxExtent: (100.0, 100.0, 100.0)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (3460.0, 2000.0002, 1250.0), (-0.0, -89.99981506294705, -0.0), (2.0000, 2.0000, 2.0000), "AB_Mines_Scaffolding_Platform_Pillar_3M_Top_B4", _folder)
if a: placed += 1
else: skipped += 1

# Construction: AB_Mines_Scaffolding_Platform_Pillar_3M_Top_B5
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Scaffolding
#   Volume: EMorSimpleShape::Empty, BoxExtent: (100.0, 100.0, 100.0)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (3650.0002, 2330.0, 1250.0), (-0.0, -179.9998224150775, -0.0), (2.0000, 2.0000, 2.0000), "AB_Mines_Scaffolding_Platform_Pillar_3M_Top_B5", _folder)
if a: placed += 1
else: skipped += 1

# Construction: AB_Mines_Scaffolding_Platform_Pillar_3M_Top_B6
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Scaffolding
#   Volume: EMorSimpleShape::Empty, BoxExtent: (100.0, 100.0, 100.0)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (3649.9995, 2870.0, 1250.0), (0.0, 0.00045776367931470125, -0.0), (2.0000, 2.0000, 2.0000), "AB_Mines_Scaffolding_Platform_Pillar_3M_Top_B6", _folder)
if a: placed += 1
else: skipped += 1

# Construction: AB_Mines_Scaffolding_Platform_Pillar_3M_Top_B7
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Scaffolding
#   Volume: EMorSimpleShape::Empty, BoxExtent: (100.0, 100.0, 100.0)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (3650.0005, 3930.0, 1250.0), (-0.0, -179.99966532066975, -0.0), (2.0000, 2.0000, 2.0000), "AB_Mines_Scaffolding_Platform_Pillar_3M_Top_B7", _folder)
if a: placed += 1
else: skipped += 1

# Construction: AB_Mines_Scaffolding_Platform_Pillar_3M_Top_B8
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Scaffolding
#   Volume: EMorSimpleShape::Empty, BoxExtent: (100.0, 100.0, 100.0)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (3780.8423, 2700.809, 4395.0), (-0.0, -177.18738697646918, -0.0), (2.0000, 2.0000, 2.0000), "AB_Mines_Scaffolding_Platform_Pillar_3M_Top_B8", _folder)
if a: placed += 1
else: skipped += 1

# Construction: AB_Mines_Scaffolding_Platform_Pillar_3M_Top_C_2
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Scaffolding
#   Volume: EMorSimpleShape::Empty, BoxExtent: (100.0, 100.0, 100.0)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (2488.5977, 2633.3213, 4395.0), (0.0, 92.81261103342001, -0.0), (2.0000, 2.0000, 2.0000), "AB_Mines_Scaffolding_Platform_Pillar_3M_Top_C_2", _folder)
if a: placed += 1
else: skipped += 1

# Construction: AB_Mines_Scaffolding_Platform_Pillar_3M_Top_D_2
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Scaffolding
#   Volume: EMorSimpleShape::Empty, BoxExtent: (100.0, 100.0, 100.0)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (3650.0017, 3780.0002, 1410.0), (-90.0, -90.11734056073848, 180.11807623856214), (2.0000, 2.0000, 2.0000), "AB_Mines_Scaffolding_Platform_Pillar_3M_Top_D_2", _folder)
if a: placed += 1
else: skipped += 1

# Construction: AB_Mines_Scaffolding_Platform_Pillar_3M_Top_D2
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Scaffolding
#   Volume: EMorSimpleShape::Empty, BoxExtent: (100.0, 100.0, 100.0)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (2730.0, 1710.0001, 1410.0), (0.0, 179.99991120752276, -0.0), (2.0000, 2.0000, 2.0000), "AB_Mines_Scaffolding_Platform_Pillar_3M_Top_D2", _folder)
if a: placed += 1
else: skipped += 1

# Construction: AB_Mines_Scaffolding_Platform_Pillar_3M_Top_D3
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Scaffolding
#   Volume: EMorSimpleShape::Empty, BoxExtent: (100.0, 100.0, 100.0)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (2730.0002, 1900.0, 1410.0), (0.0, 179.99991120752276, -0.0), (2.0000, 2.0000, 2.0000), "AB_Mines_Scaffolding_Platform_Pillar_3M_Top_D3", _folder)
if a: placed += 1
else: skipped += 1

# Construction: AB_Mines_Scaffolding_Platform_Pillar_3M_Top_D4
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Scaffolding
#   Volume: EMorSimpleShape::Empty, BoxExtent: (100.0, 100.0, 100.0)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (3170.0, 1709.9996, 1410.0), (-0.0, -0.00030517577092912265, -0.0), (2.0000, 2.0000, 2.0000), "AB_Mines_Scaffolding_Platform_Pillar_3M_Top_D4", _folder)
if a: placed += 1
else: skipped += 1

# Construction: AB_Mines_Scaffolding_Platform_Pillar_3M_Top_D5
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Scaffolding
#   Volume: EMorSimpleShape::Empty, BoxExtent: (100.0, 100.0, 100.0)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (3170.0, 1899.9996, 1410.0), (-0.0, -0.00030517577092912265, -0.0), (2.0000, 2.0000, 2.0000), "AB_Mines_Scaffolding_Platform_Pillar_3M_Top_D5", _folder)
if a: placed += 1
else: skipped += 1

# Construction: AB_Mines_Scaffolding_Platform_Pillar_3M_Top_D6
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Scaffolding
#   Volume: EMorSimpleShape::Empty, BoxExtent: (100.0, 100.0, 100.0)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (3650.0144, 3030.0002, 1410.0), (-90.0, 0.0, -89.9990225339331), (2.0000, 2.0000, 2.0000), "AB_Mines_Scaffolding_Platform_Pillar_3M_Top_D6", _folder)
if a: placed += 1
else: skipped += 1

# Construction: AB_Mines_Scaffolding_Platform_Pillar_3M_Top_D7_5
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Scaffolding
#   Volume: EMorSimpleShape::Empty, BoxExtent: (100.0, 100.0, 100.0)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (2417.0, 3058.0, 4456.0), (-0.0, -90.00005166594045, -0.0), (2.0000, 2.0000, 2.0000), "AB_Mines_Scaffolding_Platform_Pillar_3M_Top_D7_5", _folder)
if a: placed += 1
else: skipped += 1

# Construction: AB_Mines_Scaffolding_Rail_3M2
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Stone
#   Volume: EMorSimpleShape::OrientedBox, BoxExtent: (111.9, 123.4, 57.3)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (2073.857, 1690.6168, 4320.514), (0.0, 0.0, -0.0), (2.2370, 2.4687, 1.1465), "AB_Mines_Scaffolding_Rail_3M2", _folder)
if a: placed += 1
else: skipped += 1

# Construction: AB_Mines_Scaffolding_Rail_3M3
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Stone
#   Volume: EMorSimpleShape::OrientedBox, BoxExtent: (84.3, 141.1, 78.6)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (1632.5055, 2240.5996, 4212.7407), (0.0, 0.0, -0.0), (1.6857, 2.8221, 1.5712), "AB_Mines_Scaffolding_Rail_3M3", _folder)
if a: placed += 1
else: skipped += 1

# Construction: AB_Mines_Scaffolding_Rail_3M4_2
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Scaffolding
#   Volume: EMorSimpleShape::Empty, BoxExtent: (100.0, 100.0, 100.0)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (1123.7771, 2969.6868, 4635.0), (0.0, 5.625041674313767, -0.0), (2.0000, 2.0000, 2.0000), "AB_Mines_Scaffolding_Rail_3M4_2", _folder)
if a: placed += 1
else: skipped += 1

# Construction: AB_Mines_Scaffolding_Rail_3M5
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Scaffolding
#   Volume: EMorSimpleShape::Empty, BoxExtent: (100.0, 100.0, 100.0)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (1065.4565, 3561.8203, 4635.0), (0.0, 5.625041329299785, -0.0), (2.0000, 2.0000, 2.0000), "AB_Mines_Scaffolding_Rail_3M5", _folder)
if a: placed += 1
else: skipped += 1

# Construction: AB_Mines_Scaffolding_Rail_3M6
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Scaffolding
#   Volume: EMorSimpleShape::Empty, BoxExtent: (100.0, 100.0, 100.0)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (1094.3718, 3268.2424, 4635.0), (0.0, 5.625041329299785, -0.0), (2.0000, 2.0000, 2.0000), "AB_Mines_Scaffolding_Rail_3M6", _folder)
if a: placed += 1
else: skipped += 1

# Construction: AB_Mines_Scaffolding_Stairs_1M_8
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Wood
#   Volume: EMorSimpleShape::Empty, BoxExtent: (100.0, 100.0, 100.0)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (1306.377, 5103.472, 1030.0), (0.0, 15.000088880529146, -0.0), (2.0000, 2.0000, 2.0000), "AB_Mines_Scaffolding_Stairs_1M_8", _folder)
if a: placed += 1
else: skipped += 1

# Construction: AB_Mines_Scaffolding_Stairs_1M4
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Scaffolding
#   Volume: EMorSimpleShape::Empty, BoxExtent: (100.0, 100.0, 100.0)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (4865.552, 3912.3848, 1940.0), (-0.0, -157.50006421323405, -0.0), (2.0000, 2.0000, 2.0000), "AB_Mines_Scaffolding_Stairs_1M4", _folder)
if a: placed += 1
else: skipped += 1

# Construction: AB_Mines_Scaffolding_Stairs_2M_2
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Scaffolding
#   Volume: EMorSimpleShape::Empty, BoxExtent: (100.0, 100.0, 100.0)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (1042.9246, 4758.005, 900.0), (-0.0, -74.99969295801759, -0.0), (2.0000, 2.0000, 2.0000), "AB_Mines_Scaffolding_Stairs_2M_2", _folder)
if a: placed += 1
else: skipped += 1

# Construction: AB_Mines_Scaffolding_Stairs_2M3
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Scaffolding
#   Volume: EMorSimpleShape::Empty, BoxExtent: (100.0, 100.0, 100.0)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (4135.5913, 4468.776, 1800.0), (-0.0, -53.43743982178759, -0.0), (2.0000, 2.0000, 2.0000), "AB_Mines_Scaffolding_Stairs_2M3", _folder)
if a: placed += 1
else: skipped += 1

# Construction: AB_Mines_Scaffolding_Stairs_2M4_12
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Scaffolding
#   Volume: EMorSimpleShape::Empty, BoxExtent: (100.0, 100.0, 100.0)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (4850.0, 3480.0, 2100.0), (0.0, 90.00001925454477, -0.0), (2.0000, 2.0000, 2.0000), "AB_Mines_Scaffolding_Stairs_2M4_12", _folder)
if a: placed += 1
else: skipped += 1

# Construction: AB_Mines_Scaffolding_Stairs_2M5
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Scaffolding
#   Volume: EMorSimpleShape::Empty, BoxExtent: (100.0, 100.0, 100.0)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (4850.0, 3320.0, 2100.0), (0.0, 90.00001925454477, -0.0), (2.0000, 2.0000, 2.0000), "AB_Mines_Scaffolding_Stairs_2M5", _folder)
if a: placed += 1
else: skipped += 1

# Construction: AB_Mines_Scaffolding_Stairs_3M_2
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Scaffolding
#   Volume: EMorSimpleShape::Empty, BoxExtent: (100.0, 100.0, 100.0)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (3613.9695, 1866.9935, 950.0), (0.0, 90.00005166594045, -0.0), (2.0000, 2.0000, 2.0000), "AB_Mines_Scaffolding_Stairs_3M_2", _folder)
if a: placed += 1
else: skipped += 1

# Construction: AB_Mines_Scaffolding_Stairs_3M2_2
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Scaffolding
#   Volume: EMorSimpleShape::Empty, BoxExtent: (100.0, 100.0, 100.0)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (5028.4424, 1472.8875, 3550.0), (-0.0, -44.99999866815529, -0.0), (2.0000, 2.0000, 2.0000), "AB_Mines_Scaffolding_Stairs_3M2_2", _folder)
if a: placed += 1
else: skipped += 1

# Construction: BP_DM_Mines_Machine_Whim_Lift_A_Breakable_2
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Stone
#   Volume: EMorSimpleShape::Empty, BoxExtent: (100.0, 100.0, 100.0)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (4486.0, 3405.0, 2395.0), (0.0, 0.0, -0.0), (2.0000, 2.0000, 2.0000), "BP_DM_Mines_Machine_Whim_Lift_A_Breakable_2", _folder)
if a: placed += 1
else: skipped += 1

# Construction: BP_DM_Mines_Scaffolding_Platform_3X3M_A_2
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Stone
#   Volume: EMorSimpleShape::OrientedBox, BoxExtent: (152.7, 153.9, 13.6)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (4543.955, 3397.561, 2184.1194), (0.0, 0.0, -0.0), (3.0539, 3.0774, 0.2714), "BP_DM_Mines_Scaffolding_Platform_3X3M_A_2", _folder)
if a: placed += 1
else: skipped += 1

# Construction: BP_DM_Mines_Scaffolding_Platform_3X3M_A10
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Stone
#   Volume: EMorSimpleShape::OrientedBox, BoxExtent: (160.1, 161.2, 13.6)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (3414.456, 2399.5898, 3489.1194), (0.0, 0.0, -0.0), (3.2012, 3.2236, 0.2714), "BP_DM_Mines_Scaffolding_Platform_3X3M_A10", _folder)
if a: placed += 1
else: skipped += 1

# Construction: BP_DM_Mines_Scaffolding_Platform_3X3M_A11
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Stone
#   Volume: EMorSimpleShape::OrientedBox, BoxExtent: (160.1, 161.2, 13.6)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (3114.8171, 2384.8677, 3489.1194), (0.0, 0.0, -0.0), (3.2012, 3.2236, 0.2714), "BP_DM_Mines_Scaffolding_Platform_3X3M_A11", _folder)
if a: placed += 1
else: skipped += 1

# Construction: BP_DM_Mines_Scaffolding_Platform_3X3M_A12
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Stone
#   Volume: EMorSimpleShape::OrientedBox, BoxExtent: (160.1, 161.2, 13.6)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (2815.179, 2370.1453, 3489.1194), (0.0, 0.0, -0.0), (3.2012, 3.2236, 0.2714), "BP_DM_Mines_Scaffolding_Platform_3X3M_A12", _folder)
if a: placed += 1
else: skipped += 1

# Construction: BP_DM_Mines_Scaffolding_Platform_3X3M_A13_8
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Stone
#   Volume: EMorSimpleShape::OrientedBox, BoxExtent: (160.1, 161.2, 13.6)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (2515.54, 2355.4236, 3489.1194), (0.0, 0.0, -0.0), (3.2012, 3.2236, 0.2714), "BP_DM_Mines_Scaffolding_Platform_3X3M_A13_8", _folder)
if a: placed += 1
else: skipped += 1

# Construction: BP_DM_Mines_Scaffolding_Platform_3X3M_A15
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Stone
#   Volume: EMorSimpleShape::OrientedBox, BoxExtent: (154.8, 153.0, 32.1)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (5468.2393, 3150.767, 4012.915), (0.0, 0.0, -0.0), (3.0960, 3.0593, 0.6414), "BP_DM_Mines_Scaffolding_Platform_3X3M_A15", _folder)
if a: placed += 1
else: skipped += 1

# Construction: BP_DM_Mines_Scaffolding_Platform_3X3M_A16
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Stone
#   Volume: EMorSimpleShape::OrientedBox, BoxExtent: (175.1, 173.6, 30.6)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (5536.803, 2497.7314, 3995.2432), (0.0, 0.0, -0.0), (3.5020, 3.4724, 0.6123), "BP_DM_Mines_Scaffolding_Platform_3X3M_A16", _folder)
if a: placed += 1
else: skipped += 1

# Construction: BP_DM_Mines_Scaffolding_Platform_3X3M_A17
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Stone
#   Volume: EMorSimpleShape::OrientedBox, BoxExtent: (154.5, 152.7, 28.6)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (5576.6484, 1821.045, 3991.3196), (0.0, 0.0, -0.0), (3.0892, 3.0539, 0.5717), "BP_DM_Mines_Scaffolding_Platform_3X3M_A17", _folder)
if a: placed += 1
else: skipped += 1

# Construction: BP_DM_Mines_Scaffolding_Platform_3X3M_A19_11
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Stone
#   Volume: EMorSimpleShape::OrientedBox, BoxExtent: (216.8, 216.8, 13.6)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (4891.47, 1205.0802, 3389.1194), (0.0, 0.0, -0.0), (4.3355, 4.3355, 0.2714), "BP_DM_Mines_Scaffolding_Platform_3X3M_A19_11", _folder)
if a: placed += 1
else: skipped += 1

# Construction: BP_DM_Mines_Scaffolding_Platform_3X3M_A2_5
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Stone
#   Volume: EMorSimpleShape::OrientedBox, BoxExtent: (188.1, 187.3, 13.6)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (1695.67, 4763.319, 1224.1195), (0.0, 0.0, -0.0), (3.7630, 3.7463, 0.2714), "BP_DM_Mines_Scaffolding_Platform_3X3M_A2_5", _folder)
if a: placed += 1
else: skipped += 1

# Construction: BP_DM_Mines_Scaffolding_Platform_3X3M_A3
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Stone
#   Volume: EMorSimpleShape::OrientedBox, BoxExtent: (188.1, 187.3, 13.6)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (1618.0238, 5053.097, 1224.1195), (0.0, 0.0, -0.0), (3.7630, 3.7463, 0.2714), "BP_DM_Mines_Scaffolding_Platform_3X3M_A3", _folder)
if a: placed += 1
else: skipped += 1

# Construction: BP_DM_Mines_Scaffolding_Platform_3X3M_A4
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Stone
#   Volume: EMorSimpleShape::OrientedBox, BoxExtent: (188.1, 187.3, 13.6)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (1540.3776, 5342.8755, 1224.1195), (0.0, 0.0, -0.0), (3.7630, 3.7463, 0.2714), "BP_DM_Mines_Scaffolding_Platform_3X3M_A4", _folder)
if a: placed += 1
else: skipped += 1

# Construction: BP_DM_Mines_Scaffolding_Platform_3X3M_A5
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Stone
#   Volume: EMorSimpleShape::OrientedBox, BoxExtent: (173.7, 172.3, 21.1)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (1954.616, 4483.6304, 1239.2522), (0.0, 0.0, -0.0), (3.4735, 3.4452, 0.4220), "BP_DM_Mines_Scaffolding_Platform_3X3M_A5", _folder)
if a: placed += 1
else: skipped += 1

# Construction: BP_DM_Mines_Scaffolding_Platform_3X3M_A6
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Stone
#   Volume: EMorSimpleShape::OrientedBox, BoxExtent: (173.2, 172.2, 13.6)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (2259.1133, 4468.637, 1239.1195), (0.0, 0.0, -0.0), (3.4640, 3.4439, 0.2714), "BP_DM_Mines_Scaffolding_Platform_3X3M_A6", _folder)
if a: placed += 1
else: skipped += 1

# Construction: BP_DM_Mines_Scaffolding_Platform_3X3M_A7
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Stone
#   Volume: EMorSimpleShape::OrientedBox, BoxExtent: (173.2, 172.2, 13.6)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (2556.3286, 4427.856, 1239.1195), (0.0, 0.0, -0.0), (3.4640, 3.4439, 0.2714), "BP_DM_Mines_Scaffolding_Platform_3X3M_A7", _folder)
if a: placed += 1
else: skipped += 1

# Construction: BP_DM_Mines_Scaffolding_Platform_3X3M_A8
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Stone
#   Volume: EMorSimpleShape::OrientedBox, BoxExtent: (173.2, 172.2, 13.6)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (2853.544, 4387.0747, 1239.1195), (0.0, 0.0, -0.0), (3.4640, 3.4439, 0.2714), "BP_DM_Mines_Scaffolding_Platform_3X3M_A8", _folder)
if a: placed += 1
else: skipped += 1

# Construction: BP_DM_Mines_Scaffolding_Platform_3X3M_A9_2
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Stone
#   Volume: EMorSimpleShape::OrientedBox, BoxExtent: (160.1, 161.2, 13.6)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (3714.0942, 2414.3123, 3489.1194), (0.0, 0.0, -0.0), (3.2012, 3.2236, 0.2714), "BP_DM_Mines_Scaffolding_Platform_3X3M_A9_2", _folder)
if a: placed += 1
else: skipped += 1

# Construction: BP_DM_Mines_Scaffolding_Rail_3M_2
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Stone
#   Volume: EMorSimpleShape::OrientedBox, BoxExtent: (146.5, 45.3, 42.7)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (788.27563, 5044.9033, 1142.5139), (0.0, 0.0, -0.0), (2.9302, 0.9060, 0.8534), "BP_DM_Mines_Scaffolding_Rail_3M_2", _folder)
if a: placed += 1
else: skipped += 1

# Construction: BP_DM_Mines_Scaffolding_Rail_3M10
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Stone
#   Volume: EMorSimpleShape::OrientedBox, BoxExtent: (150.0, 14.1, 42.7)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (3127.5203, 2143.5515, 3540.514), (0.0, 0.0, -0.0), (3.0004, 0.2817, 0.8533), "BP_DM_Mines_Scaffolding_Rail_3M10", _folder)
if a: placed += 1
else: skipped += 1

# Construction: BP_DM_Mines_Scaffolding_Rail_3M11
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Stone
#   Volume: EMorSimpleShape::OrientedBox, BoxExtent: (150.0, 14.1, 42.7)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (2832.8823, 2128.831, 3540.514), (0.0, 0.0, -0.0), (3.0004, 0.2817, 0.8533), "BP_DM_Mines_Scaffolding_Rail_3M11", _folder)
if a: placed += 1
else: skipped += 1

# Construction: BP_DM_Mines_Scaffolding_Rail_3M12
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Stone
#   Volume: EMorSimpleShape::OrientedBox, BoxExtent: (14.1, 150.0, 42.7)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (2382.473, 2326.8103, 3540.514), (0.0, 0.0, -0.0), (0.2817, 3.0004, 0.8533), "BP_DM_Mines_Scaffolding_Rail_3M12", _folder)
if a: placed += 1
else: skipped += 1

# Construction: BP_DM_Mines_Scaffolding_Rail_3M13
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Stone
#   Volume: EMorSimpleShape::OrientedBox, BoxExtent: (14.1, 150.0, 42.7)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (3864.1265, 2329.519, 3540.514), (0.0, 0.0, -0.0), (0.2817, 3.0004, 0.8533), "BP_DM_Mines_Scaffolding_Rail_3M13", _folder)
if a: placed += 1
else: skipped += 1

# Construction: BP_DM_Mines_Scaffolding_Rail_3M14
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Stone
#   Volume: EMorSimpleShape::OrientedBox, BoxExtent: (150.0, 14.1, 42.7)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (2533.2434, 2114.1094, 3540.514), (0.0, 0.0, -0.0), (3.0004, 0.2817, 0.8533), "BP_DM_Mines_Scaffolding_Rail_3M14", _folder)
if a: placed += 1
else: skipped += 1

# Construction: BP_DM_Mines_Scaffolding_Rail_3M2
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Stone
#   Volume: EMorSimpleShape::OrientedBox, BoxExtent: (119.7, 106.2, 57.2)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (4046.8335, 2515.7217, 3380.2803), (0.0, 0.0, -0.0), (2.3945, 2.1233, 1.1430), "BP_DM_Mines_Scaffolding_Rail_3M2", _folder)
if a: placed += 1
else: skipped += 1

# Construction: BP_DM_Mines_Scaffolding_Rail_3M3_1
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Stone
#   Volume: EMorSimpleShape::OrientedBox, BoxExtent: (150.0, 14.1, 42.7)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (3721.8093, 2172.501, 3540.514), (0.0, 0.0, -0.0), (3.0004, 0.2817, 0.8533), "BP_DM_Mines_Scaffolding_Rail_3M3_1", _folder)
if a: placed += 1
else: skipped += 1

# Construction: BP_DM_Mines_Scaffolding_Rail_3M4
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Stone
#   Volume: EMorSimpleShape::OrientedBox, BoxExtent: (107.4, 114.0, 42.7)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (4550.8374, 2054.1826, 3402.2004), (0.0, 0.0, -0.0), (2.1474, 2.2799, 0.8534), "BP_DM_Mines_Scaffolding_Rail_3M4", _folder)
if a: placed += 1
else: skipped += 1

# Construction: BP_DM_Mines_Scaffolding_Rail_3M7
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Stone
#   Volume: EMorSimpleShape::OrientedBox, BoxExtent: (155.9, 22.8, 84.7)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (2957.1611, 4310.2344, 1573.9733), (0.0, 0.0, -0.0), (3.1184, 0.4562, 1.6938), "BP_DM_Mines_Scaffolding_Rail_3M7", _folder)
if a: placed += 1
else: skipped += 1

# Construction: BP_DM_Mines_Scaffolding_Tower_A_13
#   Snap: ESnapPointPlacement::Even, Grid: Default, Stability: Stone
#   Volume: EMorSimpleShape::Empty, BoxExtent: (100.0, 100.0, 100.0)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (2950.0, 1799.9998, 1000.0), (-0.0, -90.00005166594045, -0.0), (2.0000, 2.0000, 2.0000), "BP_DM_Mines_Scaffolding_Tower_A_13", _folder)
if a: placed += 1
else: skipped += 1

# Construction: BP_DM_Mines_Scaffolding_Tower_A2
#   Snap: ESnapPointPlacement::Even, Grid: Default, Stability: Stone
#   Volume: EMorSimpleShape::Empty, BoxExtent: (100.0, 100.0, 100.0)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (5040.0, 1275.0, 1000.0), (-0.0, -179.99994535848643, -0.0), (2.0000, 2.0000, 2.0000), "BP_DM_Mines_Scaffolding_Tower_A2", _folder)
if a: placed += 1
else: skipped += 1

# Construction: BP_DM_Mines_Scaffolding_Tower_B_4
#   Snap: ESnapPointPlacement::Even, Grid: Default, Stability: Stone
#   Volume: EMorSimpleShape::Empty, BoxExtent: (100.0, 100.0, 100.0)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (5040.0, 1275.0, 1350.0), (-0.0, -179.99994535848643, -0.0), (2.0000, 2.0000, 2.0000), "BP_DM_Mines_Scaffolding_Tower_B_4", _folder)
if a: placed += 1
else: skipped += 1

# Construction: BP_DM_Mines_Scaffolding_Tower_B2
#   Snap: ESnapPointPlacement::Even, Grid: Default, Stability: Stone
#   Volume: EMorSimpleShape::Empty, BoxExtent: (100.0, 100.0, 100.0)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (5040.0, 1275.0, 1650.0), (-0.0, -179.99994535848643, -0.0), (2.0000, 2.0000, 2.0000), "BP_DM_Mines_Scaffolding_Tower_B2", _folder)
if a: placed += 1
else: skipped += 1

# Construction: BP_DM_Mines_Scaffolding_Tower_B3
#   Snap: ESnapPointPlacement::Even, Grid: Default, Stability: Stone
#   Volume: EMorSimpleShape::Empty, BoxExtent: (100.0, 100.0, 100.0)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (2950.0, 1799.9998, 1350.0), (-0.0, -90.00005166594045, -0.0), (2.0000, 2.0000, 2.0000), "BP_DM_Mines_Scaffolding_Tower_B3", _folder)
if a: placed += 1
else: skipped += 1

# Construction: BP_DM_Mines_Scaffolding_Tower_B4
#   Snap: ESnapPointPlacement::Even, Grid: Default, Stability: Stone
#   Volume: EMorSimpleShape::Empty, BoxExtent: (100.0, 100.0, 100.0)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (2950.0, 1799.9998, 1650.0), (-0.0, -90.00005166594045, -0.0), (2.0000, 2.0000, 2.0000), "BP_DM_Mines_Scaffolding_Tower_B4", _folder)
if a: placed += 1
else: skipped += 1

# Construction: BP_DM_Mines_Scaffolding_Tower_B5
#   Snap: ESnapPointPlacement::Even, Grid: Default, Stability: Stone
#   Volume: EMorSimpleShape::Empty, BoxExtent: (100.0, 100.0, 100.0)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (5040.0, 1275.0, 1950.0), (-0.0, -179.99994535848643, -0.0), (2.0000, 2.0000, 2.0000), "BP_DM_Mines_Scaffolding_Tower_B5", _folder)
if a: placed += 1
else: skipped += 1

# Construction: BP_DM_Mines_Scaffolding_Tower_C_2
#   Snap: ESnapPointPlacement::Even, Grid: Default, Stability: Stone
#   Volume: EMorSimpleShape::Empty, BoxExtent: (100.0, 100.0, 100.0)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (2950.0, 1799.9998, 1950.0), (0.0, 179.99995901885745, -0.0), (2.0000, 2.0000, 2.0000), "BP_DM_Mines_Scaffolding_Tower_C_2", _folder)
if a: placed += 1
else: skipped += 1

# Construction: BP_DM_Mines_Scaffolding_Tower_D_2
#   Snap: ESnapPointPlacement::Even, Grid: Default, Stability: Stone
#   Volume: EMorSimpleShape::Empty, BoxExtent: (100.0, 100.0, 100.0)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (2950.0, 1799.9998, 2250.0), (-0.0, -90.00005166594045, -0.0), (2.0000, 2.0000, 2.0000), "BP_DM_Mines_Scaffolding_Tower_D_2", _folder)
if a: placed += 1
else: skipped += 1

# Construction: BP_DM_Mines_Scaffolding_Tower_D2
#   Snap: ESnapPointPlacement::Even, Grid: Default, Stability: Stone
#   Volume: EMorSimpleShape::Empty, BoxExtent: (100.0, 100.0, 100.0)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (5040.0, 1275.0, 2250.0), (-0.0, -179.99994535848643, -0.0), (2.0000, 2.0000, 2.0000), "BP_DM_Mines_Scaffolding_Tower_D2", _folder)
if a: placed += 1
else: skipped += 1

# Construction: BP_DM_Mines_Scaffolding_Tower_D3_2
#   Snap: ESnapPointPlacement::Even, Grid: Default, Stability: Stone
#   Volume: EMorSimpleShape::Empty, BoxExtent: (100.0, 100.0, 100.0)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (2260.0, 3280.0, 5130.0), (0.0, -179.99998633961752, -0.0), (2.0000, 2.0000, 2.0000), "BP_DM_Mines_Scaffolding_Tower_D3_2", _folder)
if a: placed += 1
else: skipped += 1

# ======================================================================
# PHASE 3: Breakables + DecoVolumes
# ======================================================================
unreal.log(f"[{BUBBLE_NAME}] Phase 3: Placing breakables and deco volumes...")

_folder = "Reconstruction/BD_BB_Passage_SpiralCave/Breakables"

# Breakable Batch 0: BP_DM_Mines_Machine_Whim_Side_Support_Beam_Breakable (6 instances)
#   BP Class: /Game/LevelDesign/Deco/Mines/BP_DM_Mines_Machine_Whim_Side_Support_Beam_Breakable
_brk_mesh = "/Game/Art/Assets/Kits/Deco/Mines/Machine/Mines_Machine_Whim_Pieces/Mines_Machine_Whim_Side_Support_Beam"
_brk_mats = ['/Game/Art/Assets/Kits/Deco/Mines/Materials/Mines_Machine_Whim/MI_Mines_Machine_Whim_Trim', '/Game/Art/Assets/Kits/Deco/Mines/Materials/Mines_Machine_Whim/MI_Mines_Machine_Whim_Uniq']
a = spawn_static_mesh(_brk_mesh, _brk_mats, (2732.6414, 1944.6887, 3165.0), (0.0, -87.18720188195033, 0.0), (1.0, 1.0, 1.0), "Mines_Machine_Whim_Side_Support_Beam_Breakable2", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_brk_mesh, _brk_mats, (2703.833, 2123.4902, 3265.0), (-90.0, 1.1792833974993155, -178.36651013747343), (1.0, 1.0, 1.0), "Mines_Machine_Whim_Side_Support_Beam_Breakable3_1", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_brk_mesh, _brk_mats, (2688.13, 2443.1057, 3265.0), (-90.0, -0.7742117978551346, 183.58697112518212), (1.0, 1.0, 1.0), "Mines_Machine_Whim_Side_Support_Beam_Breakable4_3", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_brk_mesh, _brk_mats, (3881.2566, 2001.1177, 3165.0), (0.0, -87.18720188195033, 0.0), (1.0, 1.0, 1.0), "Mines_Machine_Whim_Side_Support_Beam_Breakable5", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_brk_mesh, _brk_mats, (3631.5571, 1988.8496, 3165.0), (0.0, -87.18720188195033, 0.0), (1.0, 1.0, 1.0), "Mines_Machine_Whim_Side_Support_Beam_Breakable6", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_brk_mesh, _brk_mats, (3142.145, 1964.8042, 3165.0), (0.0, -87.18720188195033, 0.0), (1.0, 1.0, 1.0), "Mines_Machine_Whim_Side_Support_Beam_Breakable7", _folder)
if a: placed += 1
else: skipped += 1

# Breakable Batch 1: BP_DM_Mine_tailings_Debris_3x3_A (4 instances)
#   BP Class: /Game/LevelDesign/Deco/MinesDressing/BP_DM_Mine_tailings_Debris_3x3_A
_brk_mesh = "/Game/Art/Assets/Kits/Deco/Mines/Mine_tailings_Debris_3x3_A"
_brk_mats = ['/Game/Art/Assets/Kits/Misc/Dirt_Mounds/Materials/MI_DirtMound_Mines', '/Game/Art/Assets/Kits/Deco/Rubble/Materials/Rubble_Masonry_Pile/MI_Rubble_Masonry_Pile_06_Inst']
a = spawn_static_mesh(_brk_mesh, _brk_mats, (3510.0, 1655.0, 780.0), (0.0, 0.0, -0.0), (1.0, 1.0, 1.0), "BP_DM_Mine_tailings_Debris_3x3_A_2", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_brk_mesh, _brk_mats, (2505.0, 1600.0, 780.0), (0.0, 179.99995901885745, -0.0), (1.0, 1.0, 1.0), "BP_DM_Mine_tailings_Debris_3x3_A2", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_brk_mesh, _brk_mats, (3315.0, 2145.0, 3320.0), (0.0, 48.07012047559909, -0.0), (1.0, 1.0, 1.0), "BP_DM_Mine_tailings_Debris_3x3_A3_5", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_brk_mesh, _brk_mats, (850.0, 2855.0, 3980.0), (0.0, 0.0, -0.0), (1.0, 1.0, 1.0), "BP_DM_Mine_tailings_Debris_3x3_A4_8", _folder)
if a: placed += 1
else: skipped += 1

# Breakable Batch 2: BP_DM_Mine_tailings_Debris_3x3_B (4 instances)
#   BP Class: /Game/LevelDesign/Deco/MinesDressing/BP_DM_Mine_tailings_Debris_3x3_B
_brk_mesh = "/Game/Art/Assets/Kits/Deco/Mines/Mine_tailings_Debris_3x3_B"
_brk_mats = ['/Game/Art/Assets/Kits/Misc/Dirt_Mounds/Materials/MI_DirtMound_Mines', '/Game/Art/Assets/Kits/Deco/Rubble/Materials/Rubble_Masonry_Pile/MI_Rubble_Masonry_Pile_06_Inst']
a = spawn_static_mesh(_brk_mesh, _brk_mats, (3733.529, 1749.148, 795.0), (0.0, -74.99998993184444, 0.0), (1.0, 1.0, 1.0), "BP_DM_Mine_tailings_Debris_3x3_B_2", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_brk_mesh, _brk_mats, (3885.0, 2260.0, 3330.0), (0.0, 0.0, -0.0), (1.0, 1.0, 1.0), "BP_DM_Mine_tailings_Debris_3x3_B2_2", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_brk_mesh, _brk_mats, (3705.0, 2145.0, 3335.0), (0.0, 51.15178395382798, -0.0), (1.0, 1.0, 1.0), "BP_DM_Mine_tailings_Debris_3x3_B3_5", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_brk_mesh, _brk_mats, (705.0, 3545.0, 3995.0), (0.0, 33.91883718222697, -0.0), (1.0, 1.0, 1.0), "BP_DM_Mine_tailings_Debris_3x3_B4_8", _folder)
if a: placed += 1
else: skipped += 1

# Breakable Batch 3: BP_DM_Mines_Wagon_Broken_B (2 instances)
#   BP Class: /Game/LevelDesign/Deco/MinesDressing/BP_DM_Mines_Wagon_Broken_B
_brk_mesh = "/Game/Art/Assets/Kits/Deco/Mines/Mines_Wagon_Broken_B"
_brk_mats = ['/Game/Art/Assets/Kits/Deco/Mines/Materials/Mines_WagonCart/MI_Mines_WagonCart_Trim', '/Game/Art/Assets/Kits/Deco/Mines/Materials/Mines_WagonCart/MI_Mines_WagonCart']
a = spawn_static_mesh(_brk_mesh, _brk_mats, (3821.1953, 2122.592, 820.0), (0.0, 90.0004130536642, -0.0), (1.0, 1.0, 1.0), "BP_DM_Mines_Wagon_Broken_B_0", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_brk_mesh, _brk_mats, (4690.0, 2700.0, 670.0), (0.0, -35.000302956118816, 0.0), (1.0, 1.0, 1.0), "BP_DM_Mines_Wagon_Broken_B_2", _folder)
if a: placed += 1
else: skipped += 1

# Breakable Batch 4: BP_DM_Mines_Scaffolding_Beam_2M_A (4 instances)
#   BP Class: /Game/LevelDesign/Deco_Architecture/Mines/BP_DM_Mines_Scaffolding_Beam_2M_A
_brk_mesh = "/Game/Art/Assets/Kits/Deco_Architecture/Mines/Mines_Scaffolding_Beam_2M_A"
_brk_mats = ['/Game/Art/Assets/Kits/Deco_Architecture/Mines/Materials/Mines_Scaffolding/MI_Mines_Scaffolding_B_Deco']
a = spawn_static_mesh(_brk_mesh, _brk_mats, (4405.0, 3550.0, 2000.0), (0.0, 179.99995901885745, -0.0), (1.0, 1.0, 1.0), "BP_DM_Mines_Scaffolding_Beam_2M_A_2", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_brk_mesh, _brk_mats, (4395.0, 3260.0, 2000.0), (0.0, -89.99984099200987, 0.0), (1.0, 1.0, 1.0), "BP_DM_Mines_Scaffolding_Beam_2M_A6", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_brk_mesh, _brk_mats, (4685.0, 3240.0002, 2000.0), (0.0, 0.0003638267445977182, -0.0), (1.0, 1.0, 1.0), "BP_DM_Mines_Scaffolding_Beam_2M_A7", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_brk_mesh, _brk_mats, (4693.5146, 3550.455, 2000.0), (0.0, 92.81291830150126, -0.0), (1.0, 1.0, 1.0), "BP_DM_Mines_Scaffolding_Beam_2M_A8", _folder)
if a: placed += 1
else: skipped += 1

# Breakable Batch 5: BP_DM_Mines_Scaffolding_Beam_2M_B (11 instances)
#   BP Class: /Game/LevelDesign/Deco_Architecture/Mines/BP_DM_Mines_Scaffolding_Beam_2M_B
_brk_mesh = "/Game/Art/Assets/Kits/Deco_Architecture/Mines/Mines_Scaffolding_Beam_2M_C"
_brk_mats = ['/Game/Art/Assets/Kits/Deco_Architecture/Mines/Materials/Mines_Scaffolding/MI_Mines_Scaffolding_B_Deco']
a = spawn_static_mesh(_brk_mesh, _brk_mats, (3127.26, 2186.3428, 3300.0), (0.0, 2.812835487553315, -0.0), (1.0, 1.0, 1.0), "BP_DM_Mines_Scaffolding_Beam_2M_B13_33", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_brk_mesh, _brk_mats, (3107.2832, 2185.361, 3300.0), (0.0, 2.812835487553315, -0.0), (1.0, 1.0, 1.0), "BP_DM_Mines_Scaffolding_Beam_2M_B14_36", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_brk_mesh, _brk_mats, (2722.7466, 2166.4705, 3300.0), (0.0, 2.812835487553315, -0.0), (1.0, 1.0, 1.0), "BP_DM_Mines_Scaffolding_Beam_2M_B15_37", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_brk_mesh, _brk_mats, (2702.772, 2165.489, 3300.0), (0.0, 2.812835487553315, -0.0), (1.0, 1.0, 1.0), "BP_DM_Mines_Scaffolding_Beam_2M_B16_39", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_brk_mesh, _brk_mats, (3621.6633, 2210.6313, 3300.0), (0.0, 2.812835487553315, -0.0), (1.0, 1.0, 1.0), "BP_DM_Mines_Scaffolding_Beam_2M_B18", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_brk_mesh, _brk_mats, (2887.5479, 2174.5662, 3300.0), (0.0, 2.812835487553315, -0.0), (1.0, 1.0, 1.0), "BP_DM_Mines_Scaffolding_Beam_2M_B19", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_brk_mesh, _brk_mats, (3247.1152, 2192.2302, 3300.0), (0.0, 2.812835487553315, -0.0), (1.0, 1.0, 1.0), "BP_DM_Mines_Scaffolding_Beam_2M_B20", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_brk_mesh, _brk_mats, (3591.6992, 2209.1592, 3300.0), (0.0, 2.812835487553315, -0.0), (1.0, 1.0, 1.0), "BP_DM_Mines_Scaffolding_Beam_2M_B21", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_brk_mesh, _brk_mats, (3851.3867, 2221.9167, 3300.0), (0.0, 2.812835487553315, -0.0), (1.0, 1.0, 1.0), "BP_DM_Mines_Scaffolding_Beam_2M_B3", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_brk_mesh, _brk_mats, (3871.3628, 2222.8982, 3300.0), (0.0, 2.812835487553315, -0.0), (1.0, 1.0, 1.0), "BP_DM_Mines_Scaffolding_Beam_2M_B4_1", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_brk_mesh, _brk_mats, (3302.0493, 2194.929, 3300.0), (0.0, 2.812835487553315, -0.0), (1.0, 1.0, 1.0), "BP_DM_Mines_Scaffolding_Beam_2M_B5_20", _folder)
if a: placed += 1
else: skipped += 1

# Breakable Batch 6: BP_DM_Mines_Scaffolding_Beam_2M_C (7 instances)
#   BP Class: /Game/LevelDesign/Deco_Architecture/Mines/BP_DM_Mines_Scaffolding_Beam_2M_C
_brk_mesh = "/Game/Art/Assets/Kits/Deco_Architecture/Mines/Mines_Scaffolding_Beam_2M_B"
_brk_mats = ['/Game/Art/Assets/Kits/Deco_Architecture/Mines/Materials/Mines_Scaffolding/MI_Mines_Scaffolding_B_Deco']
a = spawn_static_mesh(_brk_mesh, _brk_mats, (1324.2864, 4316.2954, 661.08124), (-57.87087896898623, 148.05482946546937, 2.970857174291301), (1.0, 1.0, 1.0), "BP_DM_Mines_Scaffolding_Beam_2M_C_2", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_brk_mesh, _brk_mats, (1413.0157, 4291.927, 653.76245), (54.102720748572374, -51.96822404670679, 39.8345955842403), (1.0, 1.0, 1.0), "BP_DM_Mines_Scaffolding_Beam_2M_C2", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_brk_mesh, _brk_mats, (3146.2727, 4382.728, 1579.8278), (-72.27939769973015, 103.06617512073099, 103.39600595203444), (1.0, 1.0, 1.0), "BP_DM_Mines_Scaffolding_Beam_2M_C3", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_brk_mesh, _brk_mats, (1000.29584, 1361.8679, 794.8925), (-67.49804886919601, -118.12265041314029, -179.9999651020921), (1.0, 1.0, 1.0), "BP_DM_Mines_Scaffolding_Beam_2M_C4", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_brk_mesh, _brk_mats, (1198.1649, 1415.9843, 754.2057), (74.8748711857612, -175.5041479921112, 22.06689744903872), (1.0, 1.0, 1.0), "BP_DM_Mines_Scaffolding_Beam_2M_C5", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_brk_mesh, _brk_mats, (1486.0586, 721.99304, 811.52686), (-68.94504985002986, -164.7734787196761, 78.05139246843193), (1.0, 1.0, 1.0), "BP_DM_Mines_Scaffolding_Beam_2M_C6", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_brk_mesh, _brk_mats, (1363.779, 505.53445, 863.8619), (-85.98837063678057, 28.518657923982353, 156.59900263197153), (1.0, 1.0, 1.0), "BP_DM_Mines_Scaffolding_Beam_2M_C7", _folder)
if a: placed += 1
else: skipped += 1

# Breakable Batch 7: BP_DM_Mines_Scaffolding_Platform_3X1M_A (5 instances)
#   BP Class: /Game/LevelDesign/Deco_Architecture/Mines/BP_DM_Mines_Scaffolding_Platform_3X1M_A
_brk_mesh = "/Game/Art/Assets/Kits/Deco_Architecture/Mines/Mines_Scaffolding_Platform_3X1M_A"
_brk_mats = ['/Game/Art/Assets/Kits/Deco_Architecture/Mines/Materials/Mines_Scaffolding/MI_Mines_Scaffolding_D_Deco', '/Game/Art/Assets/Kits/Deco_Architecture/Mines/Materials/Mines_Scaffolding/MI_Mines_Scaffolding_E_Deco']
a = spawn_static_mesh(_brk_mesh, _brk_mats, (3282.1716, 2191.9502, 3498.0), (0.0, 92.81281021026828, -0.0), (1.0, 1.0, 1.0), "BP_DM_Mines_Scaffolding_Platform_3X1M_A10", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_brk_mesh, _brk_mats, (2982.5332, 2177.2297, 3498.0), (0.0, 92.81281021026828, -0.0), (1.0, 1.0, 1.0), "BP_DM_Mines_Scaffolding_Platform_3X1M_A11", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_brk_mesh, _brk_mats, (2682.8943, 2162.508, 3498.0), (0.0, 92.81281021026828, -0.0), (1.0, 1.0, 1.0), "BP_DM_Mines_Scaffolding_Platform_3X1M_A12_2", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_brk_mesh, _brk_mats, (3881.4475, 2221.3904, 3498.0), (0.0, 92.81281021026828, -0.0), (1.0, 1.0, 1.0), "BP_DM_Mines_Scaffolding_Platform_3X1M_A4_2", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_brk_mesh, _brk_mats, (3581.8098, 2206.6702, 3498.0), (0.0, 92.81281021026828, -0.0), (1.0, 1.0, 1.0), "BP_DM_Mines_Scaffolding_Platform_3X1M_A5", _folder)
if a: placed += 1
else: skipped += 1

# Breakable Batch 8: BP_DM_Mines_Scaffolding_Platform_3X1M_B (5 instances)
#   BP Class: /Game/LevelDesign/Deco_Architecture/Mines/BP_DM_Mines_Scaffolding_Platform_3X1M_B
_brk_mesh = "/Game/Art/Assets/Kits/Deco_Architecture/Mines/Mines_Scaffolding_Platform_3X1M_B"
_brk_mats = ['/Game/Art/Assets/Kits/Deco_Architecture/Mines/Materials/Mines_Scaffolding/MI_Mines_Scaffolding_E_Deco', '/Game/Art/Assets/Kits/Deco_Architecture/Mines/Materials/Mines_Scaffolding/MI_Mines_Scaffolding_D_Deco']
a = spawn_static_mesh(_brk_mesh, _brk_mats, (3685.2393, 2461.5159, 751.95734), (5.212266815023936, -17.13189539391162, 13.606045049221425), (1.0, 1.0, 1.0), "BP_DM_Mines_Scaffolding_Platform_3X1M_B_9", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_brk_mesh, _brk_mats, (3650.0, 2950.0, 1500.0), (0.0, -0.00030517577092912265, 0.0), (1.0, 1.0, 1.0), "BP_DM_Mines_Scaffolding_Platform_3X1M_B2", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_brk_mesh, _brk_mats, (3650.7036, 3189.3804, 640.9885), (-8.929718494244153, -6.735901528963223, 15.965829727781246), (1.0, 1.0, 1.0), "BP_DM_Mines_Scaffolding_Platform_3X1M_B3", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_brk_mesh, _brk_mats, (3767.1577, 2406.8547, 769.286), (34.93085091742175, -120.07187237462401, -2.9034403786899494), (1.0, 1.0, 1.0), "BP_DM_Mines_Scaffolding_Platform_3X1M_B4", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_brk_mesh, _brk_mats, (5321.395, 3620.0, 4027.393), (16.541291304950608, 93.38682726626364, 11.742972564880747), (1.0, 1.0, 1.0), "BP_DM_Mines_Scaffolding_Platform_3X1M_B5_2", _folder)
if a: placed += 1
else: skipped += 1

# Breakable Batch 9: BP_DM_Mines_Scaffolding_Platform_3X1M_C (47 instances)
#   BP Class: /Game/LevelDesign/Deco_Architecture/Mines/BP_DM_Mines_Scaffolding_Platform_3X1M_C
_brk_mesh = "/Game/Art/Assets/Kits/Deco_Architecture/Mines/Mines_Scaffolding_Platform_3X1M_C"
_brk_mats = ['/Game/Art/Assets/Kits/Deco_Architecture/Mines/Materials/Mines_Scaffolding/MI_Mines_Scaffolding_E_Deco', '/Game/Art/Assets/Kits/Deco_Architecture/Mines/Materials/Mines_Scaffolding/MI_Mines_Scaffolding_D_Deco']
a = spawn_static_mesh(_brk_mesh, _brk_mats, (3650.0, 3870.0, 1500.0), (0.0, 179.99994535848643, -0.0), (1.0, 1.0, 1.0), "BP_DM_Mines_Scaffolding_Platform_3X1M_C_2", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_brk_mesh, _brk_mats, (3727.3213, 2768.2712, 717.61127), (61.729909478701174, 134.98357192966023, -21.210541366470984), (1.0, 1.0, 1.0), "BP_DM_Mines_Scaffolding_Platform_3X1M_C10", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_brk_mesh, _brk_mats, (3812.2048, 2484.8708, 742.662), (-4.291718017343346, -28.94848752255315, 15.335670851119877), (1.0, 1.0, 1.0), "BP_DM_Mines_Scaffolding_Platform_3X1M_C11", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_brk_mesh, _brk_mats, (1773.9501, 5244.8096, 1259.8917), (8.437501465895345, 15.000983728747043, 2.2725553460940186e-06), (1.0, 1.0, 1.0), "BP_DM_Mines_Scaffolding_Platform_3X1M_C12_19", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_brk_mesh, _brk_mats, (1838.7231, 4313.376, 995.173), (45.97186146559034, 49.52571262869651, -8.473082968624857), (1.0, 1.0, 1.0), "BP_DM_Mines_Scaffolding_Platform_3X1M_C13", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_brk_mesh, _brk_mats, (1830.633, 4708.417, 1240.4446), (8.148014282562235, 15.158596977179858, -0.6138612083252216), (1.0, 1.0, 1.0), "BP_DM_Mines_Scaffolding_Platform_3X1M_C14", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_brk_mesh, _brk_mats, (2724.6184, 3947.682, 634.89886), (39.69478507282782, 67.70289720906062, -5.241977054624904), (1.0, 1.0, 1.0), "BP_DM_Mines_Scaffolding_Platform_3X1M_C15", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_brk_mesh, _brk_mats, (1626.0095, 4104.889, 567.43896), (-20.799040105159378, -52.4747220596505, -24.936676542585985), (1.0, 1.0, 1.0), "BP_DM_Mines_Scaffolding_Platform_3X1M_C16", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_brk_mesh, _brk_mats, (2290.0996, 3389.1394, 678.55347), (21.198974518414335, -51.87575929247112, 12.340191068337418), (1.0, 1.0, 1.0), "BP_DM_Mines_Scaffolding_Platform_3X1M_C17_26", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_brk_mesh, _brk_mats, (2541.7866, 3168.8357, 795.75934), (-12.292692319287188, 100.09679606839941, 5.646844089030318), (1.0, 1.0, 1.0), "BP_DM_Mines_Scaffolding_Platform_3X1M_C18", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_brk_mesh, _brk_mats, (3053.5715, 4242.135, 1488.0891), (0.0, -112.18754144605977, 0.0), (1.0, 1.0, 1.0), "BP_DM_Mines_Scaffolding_Platform_3X1M_C19", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_brk_mesh, _brk_mats, (3649.2673, 3826.0615, 701.29175), (-2.754485874423745, 179.33913451258866, 21.872567272735413), (1.0, 1.0, 1.0), "BP_DM_Mines_Scaffolding_Platform_3X1M_C2_5", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_brk_mesh, _brk_mats, (2569.7976, 4325.983, 1428.6306), (6.9160778358952815, -104.3865278294197, -19.27889957378407), (1.0, 1.0, 1.0), "BP_DM_Mines_Scaffolding_Platform_3X1M_C20", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_brk_mesh, _brk_mats, (1429.1992, 799.30145, 815.09875), (8.738390191017357e-08, 144.06279993067577, -11.250852455286331), (1.0, 1.0, 1.0), "BP_DM_Mines_Scaffolding_Platform_3X1M_C21", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_brk_mesh, _brk_mats, (651.5595, 1417.0336, 829.71136), (12.276268246256315, -56.59653028128915, 9.812364735426764), (1.0, 1.0, 1.0), "BP_DM_Mines_Scaffolding_Platform_3X1M_C22", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_brk_mesh, _brk_mats, (3048.4548, 4307.814, 2929.159), (-54.05835161434199, 99.80763722957757, 47.83603386956667), (1.0, 1.0, 1.0), "BP_DM_Mines_Scaffolding_Platform_3X1M_C23_2", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_brk_mesh, _brk_mats, (3660.2783, 3993.8193, 3207.0513), (-19.564117487881354, 7.572947528419957, 17.147972196827297), (1.0, 1.0, 1.0), "BP_DM_Mines_Scaffolding_Platform_3X1M_C24_5", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_brk_mesh, _brk_mats, (3385.4314, 4318.986, 3172.3982), (-31.00326411973474, 73.92363099933958, -4.8243701107150985), (1.0, 1.0, 1.0), "BP_DM_Mines_Scaffolding_Platform_3X1M_C25_10", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_brk_mesh, _brk_mats, (3911.89, 3707.6167, 3201.77), (-14.950805249741077, 18.282200560838, 0.13933728139489876), (1.0, 1.0, 1.0), "BP_DM_Mines_Scaffolding_Platform_3X1M_C26", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_brk_mesh, _brk_mats, (3811.89, 3402.6167, 3201.77), (-14.950775013483609, -15.467804250863978, 0.13933914115228777), (1.0, 1.0, 1.0), "BP_DM_Mines_Scaffolding_Platform_3X1M_C27", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_brk_mesh, _brk_mats, (3977.862, 3119.4111, 3235.3218), (-17.831117070227922, 21.567502949581716, 8.408057416426605), (1.0, 1.0, 1.0), "BP_DM_Mines_Scaffolding_Platform_3X1M_C28", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_brk_mesh, _brk_mats, (3379.5945, 3044.4966, 4944.159), (0.0, -87.18738219756044, 0.0), (1.0, 1.0, 1.0), "BP_DM_Mines_Scaffolding_Platform_3X1M_C29", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_brk_mesh, _brk_mats, (1318.2852, 4401.673, 704.62604), (-8.379089616655557, -143.34918548176216, 21.665010687269636), (1.0, 1.0, 1.0), "BP_DM_Mines_Scaffolding_Platform_3X1M_C3_8", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_brk_mesh, _brk_mats, (3422.8806, 2784.0872, 4944.159), (0.0, 2.811767777488404, -0.0), (1.0, 1.0, 1.0), "BP_DM_Mines_Scaffolding_Platform_3X1M_C30", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_brk_mesh, _brk_mats, (2691.4094, 3006.3906, 4984.6636), (-17.163301934712887, -164.20342860567195, 22.120256711395758), (1.0, 1.0, 1.0), "BP_DM_Mines_Scaffolding_Platform_3X1M_C31", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_brk_mesh, _brk_mats, (3323.5806, 2869.3174, 5239.159), (0.0, -177.18831597561723, 0.0), (1.0, 1.0, 1.0), "BP_DM_Mines_Scaffolding_Platform_3X1M_C32", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_brk_mesh, _brk_mats, (3323.5806, 2869.3174, 4939.159), (0.0, -177.18831597561723, 0.0), (1.0, 1.0, 1.0), "BP_DM_Mines_Scaffolding_Platform_3X1M_C33", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_brk_mesh, _brk_mats, (3869.4167, 3171.4546, 4944.159), (0.0, 92.81152244048877, -0.0), (1.0, 1.0, 1.0), "BP_DM_Mines_Scaffolding_Platform_3X1M_C34", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_brk_mesh, _brk_mats, (3540.002, 2110.0, 1500.0), (0.0, 90.0001164887758, -0.0), (1.0, 1.0, 1.0), "BP_DM_Mines_Scaffolding_Platform_3X1M_C35", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_brk_mesh, _brk_mats, (5276.6997, 3177.8164, 4011.9329), (-8.43743696975177, 179.99995901885816, 3.506697494169835e-12), (1.0, 1.0, 1.0), "BP_DM_Mines_Scaffolding_Platform_3X1M_C36", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_brk_mesh, _brk_mats, (5279.1733, 3477.8164, 3995.886), (-36.562402746209834, 179.99995901885967, 1.7754164454777587e-11), (1.0, 1.0, 1.0), "BP_DM_Mines_Scaffolding_Platform_3X1M_C37", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_brk_mesh, _brk_mats, (5308.03, 2636.7153, 4018.5933), (-8.543213648589624, -168.96708553342933, 1.1080216372298037), (1.0, 1.0, 1.0), "BP_DM_Mines_Scaffolding_Platform_3X1M_C38", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_brk_mesh, _brk_mats, (5386.646, 2027.8164, 4001.282), (-14.062343933496356, 179.9999590188539, 7.02365601892284e-12), (1.0, 1.0, 1.0), "BP_DM_Mines_Scaffolding_Platform_3X1M_C39", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_brk_mesh, _brk_mats, (3750.0, 3570.0, 1500.0), (0.0, 0.0001435279788693279, -0.0), (1.0, 1.0, 1.0), "BP_DM_Mines_Scaffolding_Platform_3X1M_C4", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_brk_mesh, _brk_mats, (5375.26, 2337.8164, 4011.864), (-5.6249685928151445, 179.99995901885777, 7.889283635422614e-12), (1.0, 1.0, 1.0), "BP_DM_Mines_Scaffolding_Platform_3X1M_C40", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_brk_mesh, _brk_mats, (5145.1406, 3533.8372, 3948.4932), (-33.18969236706385, -83.71349510519332, -13.352875400696952), (1.0, 1.0, 1.0), "BP_DM_Mines_Scaffolding_Platform_3X1M_C41", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_brk_mesh, _brk_mats, (5371.639, 1743.2797, 3998.3145), (-30.56307545392046, 139.98667690879768, 24.25890650296186), (1.0, 1.0, 1.0), "BP_DM_Mines_Scaffolding_Platform_3X1M_C42", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_brk_mesh, _brk_mats, (3429.7976, 5175.983, 1578.6306), (0.0, 90.00005166594045, -0.0), (1.0, 1.0, 1.0), "BP_DM_Mines_Scaffolding_Platform_3X1M_C43", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_brk_mesh, _brk_mats, (3243.8364, 1032.2783, 4014.8457), (0.0, 85.05819232362843, -0.0), (1.0, 1.0, 1.0), "BP_DM_Mines_Scaffolding_Platform_3X1M_C44", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_brk_mesh, _brk_mats, (3542.721, 1006.43787, 4014.8457), (0.0, 85.05819232362843, -0.0), (1.0, 1.0, 1.0), "BP_DM_Mines_Scaffolding_Platform_3X1M_C45", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_brk_mesh, _brk_mats, (3119.7976, 5175.983, 1578.6306), (6.299031455681963e-08, 100.0000622792769, 15.00008814925588), (1.0, 1.0, 1.0), "BP_DM_Mines_Scaffolding_Platform_3X1M_C46", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_brk_mesh, _brk_mats, (2822.4922, 5127.8667, 1508.2507), (0.22922094436512272, 79.40876578574334, 14.08095763814072), (1.0, 1.0, 1.0), "BP_DM_Mines_Scaffolding_Platform_3X1M_C47", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_brk_mesh, _brk_mats, (3750.002, 2650.0, 1500.0), (0.0, 0.00014400000441926997, -0.0), (1.0, 1.0, 1.0), "BP_DM_Mines_Scaffolding_Platform_3X1M_C5", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_brk_mesh, _brk_mats, (3750.002, 2350.0, 1500.0), (0.0, 0.00014400000441926997, -0.0), (1.0, 1.0, 1.0), "BP_DM_Mines_Scaffolding_Platform_3X1M_C6", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_brk_mesh, _brk_mats, (3750.002, 2050.0, 1500.0), (0.0, 0.00014400000441926997, -0.0), (1.0, 1.0, 1.0), "BP_DM_Mines_Scaffolding_Platform_3X1M_C7", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_brk_mesh, _brk_mats, (3550.002, 2350.0, 1500.0), (0.0, 179.99994535848643, -0.0), (1.0, 1.0, 1.0), "BP_DM_Mines_Scaffolding_Platform_3X1M_C8", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_brk_mesh, _brk_mats, (3894.9363, 3581.6948, 607.7887), (2.2341093148267586, 21.800322220786175, -19.235262133300914), (1.0, 1.0, 1.0), "BP_DM_Mines_Scaffolding_Platform_3X1M_C9", _folder)
if a: placed += 1
else: skipped += 1

# Breakable Batch 10: BP_DM_Mines_Scaffolding_Platform_3X3M_B (17 instances)
#   BP Class: /Game/LevelDesign/Deco_Architecture/Mines/BP_DM_Mines_Scaffolding_Platform_3X3M_B
_brk_mesh = "/Game/Art/Assets/Kits/Deco_Architecture/Mines/Mines_Scaffolding_Platform_3X3M_B"
_brk_mats = ['/Game/Art/Assets/Kits/Deco_Architecture/Mines/Materials/Mines_Scaffolding/MI_Mines_Scaffolding_D_Deco', '/Game/Art/Assets/Kits/Deco_Architecture/Mines/Materials/Mines_Scaffolding/MI_Mines_Scaffolding_E_Deco']
a = spawn_static_mesh(_brk_mesh, _brk_mats, (3586.5835, 2985.7043, 674.663), (-0.000244636604512483, -74.99672997069352, 14.99700397601919), (1.0, 1.0, 1.0), "BP_DM_Mines_Scaffolding_Platform_3X3M_B_2", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_brk_mesh, _brk_mats, (5471.939, 3011.4893, 4026.331), (5.624988101139923, 179.99997951201698, -1.314819114451845), (1.0, 1.0, 1.0), "BP_DM_Mines_Scaffolding_Platform_3X3M_B11", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_brk_mesh, _brk_mats, (5470.5645, 3301.4893, 4012.333), (-5.62500015727469, -0.0002441406269512079, 2.4031239200017487e-05), (1.0, 1.0, 1.0), "BP_DM_Mines_Scaffolding_Platform_3X3M_B12", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_brk_mesh, _brk_mats, (5571.0796, 2361.4893, 4002.4326), (5.624987684027957, 179.9999795094294, 5.955450977555262e-14), (1.0, 1.0, 1.0), "BP_DM_Mines_Scaffolding_Platform_3X3M_B13", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_brk_mesh, _brk_mats, (5501.284, 2639.751, 4009.3074), (-5.5639346842210555, 8.477640115502712, -0.8279417844294701), (1.0, 1.0, 1.0), "BP_DM_Mines_Scaffolding_Platform_3X3M_B14", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_brk_mesh, _brk_mats, (5567.2705, 1654.3695, 4002.808), (5.083428476723289, 154.58045101661634, -2.4113154770475607), (1.0, 1.0, 1.0), "BP_DM_Mines_Scaffolding_Platform_3X3M_B15", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_brk_mesh, _brk_mats, (5580.035, 1971.4893, 4001.5513), (-5.62500015727469, -0.0002441406269512079, 2.4031239200017487e-05), (1.0, 1.0, 1.0), "BP_DM_Mines_Scaffolding_Platform_3X3M_B16", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_brk_mesh, _brk_mats, (4716.676, 1238.8907, 3400.0), (1.3363204010092027e-05, 45.00004299455286, 14.064403802338274), (1.0, 1.0, 1.0), "BP_DM_Mines_Scaffolding_Platform_3X3M_B17_10", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_brk_mesh, _brk_mats, (4931.4805, 1455.0739, 3404.898), (2.7583993620979017, 45.54942189809409, 11.264833939229392), (1.0, 1.0, 1.0), "BP_DM_Mines_Scaffolding_Platform_3X3M_B18", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_brk_mesh, _brk_mats, (1389.7604, 4416.205, 717.75635), (-1.127258212286848, 24.399079205330978, -25.324981999475675), (1.0, 1.0, 1.0), "BP_DM_Mines_Scaffolding_Platform_3X3M_B2", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_brk_mesh, _brk_mats, (1691.7192, 4491.7188, 1238.0), (0.0, -45.00002828938376, 0.0), (1.0, 1.0, 1.0), "BP_DM_Mines_Scaffolding_Platform_3X3M_B3_7", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_brk_mesh, _brk_mats, (2215.2249, 4347.6387, 1301.752), (15.700209392009976, -14.993499688483734, -4.987976432401496), (1.0, 1.0, 1.0), "BP_DM_Mines_Scaffolding_Platform_3X3M_B4", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_brk_mesh, _brk_mats, (2811.1052, 3573.1863, 591.6419), (-3.854765877388685, 173.5252991607217, -30.902061176115392), (1.0, 1.0, 1.0), "BP_DM_Mines_Scaffolding_Platform_3X3M_B5_14", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_brk_mesh, _brk_mats, (1262.0902, 1131.1301, 830.51514), (-12.468476035403945, 44.24529548567303, 3.8754076482445217), (1.0, 1.0, 1.0), "BP_DM_Mines_Scaffolding_Platform_3X3M_B6", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_brk_mesh, _brk_mats, (3464.923, 4255.38, 3156.683), (-19.47003239048151, 4.849002858385415, 48.82917498338236), (1.0, 1.0, 1.0), "BP_DM_Mines_Scaffolding_Platform_3X3M_B7_2", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_brk_mesh, _brk_mats, (2949.5317, 4266.456, 3172.1042), (-10.559539706257093, 10.013283060337397, 71.17676732051771), (1.0, 1.0, 1.0), "BP_DM_Mines_Scaffolding_Platform_3X3M_B8", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_brk_mesh, _brk_mats, (5470.5654, 3691.4893, 4012.3328), (5.624987684027957, 179.9999795094294, 5.955450977555262e-14), (1.0, 1.0, 1.0), "BP_DM_Mines_Scaffolding_Platform_3X3M_B9", _folder)
if a: placed += 1
else: skipped += 1

# Breakable Batch 11: BP_DM_Mines_Scaffolding_Post_1M_A (9 instances)
#   BP Class: /Game/LevelDesign/Deco_Architecture/Mines/BP_DM_Mines_Scaffolding_Post_1M_A
_brk_mesh = "/Game/Art/Assets/Kits/Deco_Architecture/Mines/Mines_Scaffolding_Post_1M_A"
_brk_mats = ['/Game/Art/Assets/Kits/Deco_Architecture/Mines/Materials/Mines_Scaffolding/MI_Mines_Scaffolding_B_Deco']
a = spawn_static_mesh(_brk_mesh, _brk_mats, (3775.1963, 1951.2368, 880.3795), (-90.0, -16.70132371121037, 106.70175686729482), (1.0, 1.0, 1.0), "BP_DM_Mines_Scaffolding_Post_1M_A_8", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_brk_mesh, _brk_mats, (3775.1963, 1951.2368, 980.3795), (-90.0, -6.582357469879243, 96.58281125252559), (1.0, 1.0, 1.0), "BP_DM_Mines_Scaffolding_Post_1M_A2", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_brk_mesh, _brk_mats, (3236.489, 2204.7249, 3380.0), (3.948271188226773e-06, -87.18707378929619, -89.99988217130695), (1.0, 1.0, 1.0), "BP_DM_Mines_Scaffolding_Post_1M_A3_2", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_brk_mesh, _brk_mats, (3775.1963, 1951.2368, 1080.3795), (-90.0, 7.907562297350323, 82.09290409035555), (1.0, 1.0, 1.0), "BP_DM_Mines_Scaffolding_Post_1M_A4", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_brk_mesh, _brk_mats, (3775.1963, 1951.2368, 1180.3795), (-90.0, 14.037251745751762, -284.03678650399416), (1.0, 1.0, 1.0), "BP_DM_Mines_Scaffolding_Post_1M_A5", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_brk_mesh, _brk_mats, (4720.3105, 2051.2368, 880.3795), (-90.0, -90.02933559833009, 0.029704583194444467), (1.0, 1.0, 1.0), "BP_DM_Mines_Scaffolding_Post_1M_A6", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_brk_mesh, _brk_mats, (4720.3105, 2051.2368, 980.3795), (-90.0, 33.69675229413775, -123.69630194925224), (1.0, 1.0, 1.0), "BP_DM_Mines_Scaffolding_Post_1M_A7", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_brk_mesh, _brk_mats, (4720.3105, 2051.2368, 1080.3795), (-90.0, 5.355966065766065, -95.35565323076926), (1.0, 1.0, 1.0), "BP_DM_Mines_Scaffolding_Post_1M_A8", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_brk_mesh, _brk_mats, (4720.3105, 2051.2368, 1180.3795), (-90.0, -4.7642294627406905, -85.23537290449781), (1.0, 1.0, 1.0), "BP_DM_Mines_Scaffolding_Post_1M_A9", _folder)
if a: placed += 1
else: skipped += 1

# Breakable Batch 12: BP_DM_Mines_Scaffolding_Post_2M_A (1 instances)
#   BP Class: /Game/LevelDesign/Deco_Architecture/Mines/BP_DM_Mines_Scaffolding_Post_2M_A
_brk_mesh = "/Game/Art/Assets/Kits/Deco_Architecture/Mines/Mines_Scaffolding_Post_2M_A"
_brk_mats = ['/Game/Art/Assets/Kits/Deco_Architecture/Mines/Materials/Mines_Scaffolding/MI_Mines_Scaffolding_B_Deco']
a = spawn_static_mesh(_brk_mesh, _brk_mats, (2876.267, 2180.02, 3378.0), (-0.0003109764674261201, 92.81248763950224, 89.99996252304001), (1.0, 1.0, 1.0), "BP_DM_Mines_Scaffolding_Post_2M_A2_2", _folder)
if a: placed += 1
else: skipped += 1

# Breakable Batch 13: BP_DM_Mines_Scaffolding_Post_2M_B (2 instances)
#   BP Class: /Game/LevelDesign/Deco_Architecture/Mines/BP_DM_Mines_Scaffolding_Post_2M_B
_brk_mesh = "/Game/Art/Assets/Kits/Deco_Architecture/Mines/Mines_Scaffolding_Post_2M_B"
_brk_mats = ['/Game/Art/Assets/Kits/Deco_Architecture/Mines/Materials/Mines_Scaffolding/MI_Mines_Scaffolding_C_Deco']
a = spawn_static_mesh(_brk_mesh, _brk_mats, (3732.2356, 2222.07, 3378.0), (0.0, 92.81273572254389, -0.0), (1.0, 1.0, 1.0), "BP_DM_Mines_Scaffolding_Post_2M_B2_2", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_brk_mesh, _brk_mats, (2996.1235, 2185.908, 3378.0), (-0.0003662109170978466, 92.81253626145872, 179.99995901884938), (1.0, 1.0, 1.0), "BP_DM_Mines_Scaffolding_Post_2M_B3_7", _folder)
if a: placed += 1
else: skipped += 1

# Breakable Batch 14: BP_DM_Mines_Scaffolding_Post_3M_A (1 instances)
#   BP Class: /Game/LevelDesign/Deco_Architecture/Mines/BP_DM_Mines_Scaffolding_Post_3M_A
_brk_mesh = "/Game/Art/Assets/Kits/Deco_Architecture/Mines/Mines_Scaffolding_Post_3M_A"
_brk_mats = ['/Game/Art/Assets/Kits/Deco_Architecture/Mines/Materials/Mines_Scaffolding/MI_Mines_Scaffolding_B_Deco']
a = spawn_static_mesh(_brk_mesh, _brk_mats, (3582.4155, 2214.71, 3378.0), (0.00023295197692210887, 92.81255688500585, 89.99993970827525), (1.0, 1.0, 1.0), "BP_DM_Mines_Scaffolding_Post_3M_A2_2", _folder)
if a: placed += 1
else: skipped += 1

# Breakable Batch 15: BP_DM_Mines_Scaffolding_Rail_1M (12 instances)
#   BP Class: /Game/LevelDesign/Deco_Architecture/Mines/BP_DM_Mines_Scaffolding_Rail_1M
_brk_mesh = "/Game/Art/Assets/Kits/Deco_Architecture/Mines/Mines_Scaffolding_Rail_1M"
_brk_mats = ['/Game/Art/Assets/Kits/Deco_Architecture/Mines/Materials/Mines_Scaffolding/MI_Mines_Scaffolding_A_Deco']
a = spawn_static_mesh(_brk_mesh, _brk_mats, (928.4838, 5082.475, 1100.0), (0.0, -75.00003453112258, 0.0), (1.0, 1.0, 1.0), "BP_DM_Mines_Scaffolding_Rail_1M_2", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_brk_mesh, _brk_mats, (3127.1777, 4295.939, 1580.7775), (2.92851238725491, -93.15250199830632, -19.668364682121418), (1.0, 1.0, 1.0), "BP_DM_Mines_Scaffolding_Rail_1M10", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_brk_mesh, _brk_mats, (1591.3035, 2541.8271, 4048.7593), (-2.72723318118766, 167.77925367453278, -10.039517170607201), (1.0, 1.0, 1.0), "BP_DM_Mines_Scaffolding_Rail_1M11", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_brk_mesh, _brk_mats, (3593.184, 5032.1294, 1647.7336), (-0.46151740351016296, -102.56382900866251, -19.871395257343906), (1.0, 1.0, 1.0), "BP_DM_Mines_Scaffolding_Rail_1M12", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_brk_mesh, _brk_mats, (404.171, 5545.659, 1100.0), (0.0, -165.0001029412836, 0.0), (1.0, 1.0, 1.0), "BP_DM_Mines_Scaffolding_Rail_1M2", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_brk_mesh, _brk_mats, (524.86615, 5075.8945, 1100.0), (0.0, 14.999694478017897, -0.0), (1.0, 1.0, 1.0), "BP_DM_Mines_Scaffolding_Rail_1M3", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_brk_mesh, _brk_mats, (4696.931, 1912.8715, 3360.0), (0.0, -108.7499056571947, 0.0), (1.0, 1.0, 1.0), "BP_DM_Mines_Scaffolding_Rail_1M4", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_brk_mesh, _brk_mats, (4440.5186, 2174.7349, 3362.9443), (6.82987730561518e-05, 48.75000396747245, 5.625237650431002), (1.0, 1.0, 1.0), "BP_DM_Mines_Scaffolding_Rail_1M5", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_brk_mesh, _brk_mats, (1961.0864, 1793.7089, 4254.2173), (-15.828277721962571, 50.90314628783892, 8.31659375155802), (1.0, 1.0, 1.0), "BP_DM_Mines_Scaffolding_Rail_1M6_2", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_brk_mesh, _brk_mats, (1694.3743, 2098.4358, 4217.146), (18.03218330994645, -146.85650081273963, -6.574431474277386), (1.0, 1.0, 1.0), "BP_DM_Mines_Scaffolding_Rail_1M7", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_brk_mesh, _brk_mats, (2437.6633, 4391.478, 1361.5084), (-8.928011769136994, -92.13764375797118, -20.26162722929869), (1.0, 1.0, 1.0), "BP_DM_Mines_Scaffolding_Rail_1M8_2", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_brk_mesh, _brk_mats, (2809.8037, 4344.3076, 1484.9335), (1.8172320297267908, 82.72201387274595, 16.761352476562806), (1.0, 1.0, 1.0), "BP_DM_Mines_Scaffolding_Rail_1M9", _folder)
if a: placed += 1
else: skipped += 1

# Breakable Batch 16: BP_DM_Mines_Scaffolding_Rail_Corner (2 instances)
#   BP Class: /Game/LevelDesign/Deco_Architecture/Mines/BP_DM_Mines_Scaffolding_Rail_Corner
_brk_mesh = "/Game/Art/Assets/Kits/Deco_Architecture/Mines/Mines_Scaffolding_Rail_Corner"
_brk_mats = ['/Game/Art/Assets/Kits/Deco_Architecture/Mines/Materials/Mines_Scaffolding/MI_Mines_Scaffolding_A_Deco']
a = spawn_static_mesh(_brk_mesh, _brk_mats, (2172.1714, 1559.3998, 4321.734), (-10.698973975418772, 135.00286844264502, 6.644020972151292), (1.0, 1.0, 1.0), "AB_Mines_Scaffolding_Rail_Corner_2", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_brk_mesh, _brk_mats, (638.7059, 5004.8296, 1100.0), (0.0, 15.000073607810464, -0.0), (1.0, 1.0, 1.0), "BP_DM_Mines_Scaffolding_Rail_Corner_2", _folder)
if a: placed += 1
else: skipped += 1

# Breakable Batch 17: BP_DM_Mines_Scaffolding_Stairs_2M (2 instances)
#   BP Class: /Game/LevelDesign/Deco_Architecture/Mines/BP_DM_Mines_Scaffolding_Stairs_2M
_brk_mesh = "/Game/Art/Assets/Kits/Deco_Architecture/Mines/Mines_Scaffolding_Stairs_2M"
_brk_mats = ['/Game/Art/Assets/Kits/Deco_Architecture/Mines/Materials/Mines_Scaffolding/MI_Mines_Scaffolding_A_Deco']
a = spawn_static_mesh(_brk_mesh, _brk_mats, (3510.0, 2140.0, 3500.0), (0.0, 0.0, -0.0), (1.0, 1.0, 1.0), "BP_DM_Mines_Scaffolding_Stairs_2M2_2", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_brk_mesh, _brk_mats, (3360.0, 2140.0, 3500.0), (0.0, 0.0, -0.0), (1.0, 1.0, 1.0), "BP_DM_Mines_Scaffolding_Stairs_2M3", _folder)
if a: placed += 1
else: skipped += 1

# Breakable Batch 18: BP_Mines_Ceiling_Brace_A_Bracket (8 instances)
#   BP Class: /Game/LevelDesign/Deco_Architecture/Mines/BP_Mines_Ceiling_Brace_A_Bracket
_brk_mesh = "/Game/Art/Assets/Kits/Deco/Mines/Machine/Mines_Machine_Whim_Pieces/Mines_Machine_Whim_Side_Bracket"
_brk_mats = ['/Game/Art/Assets/Kits/Deco/Mines/Materials/Mines_Machine_Whim/MI_Mines_Machine_Whim_Trim', '/Game/Art/Assets/Kits/Deco/Mines/Materials/Mines_Machine_Whim/MI_Mines_Machine_Whim_Uniq']
a = spawn_static_mesh(_brk_mesh, _brk_mats, (3754.8855, 2040.8628, 1249.9998), (0.0, 0.0, -0.0), (1.0, 1.0, 1.0), "BP_Mines_Ceiling_Brace_A_Bracket_2", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_brk_mesh, _brk_mats, (3754.8855, 1961.5913, 1249.9998), (0.0, 0.0, -0.0), (1.0, 1.0, 1.0), "BP_Mines_Ceiling_Brace_A_Bracket2", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_brk_mesh, _brk_mats, (4740.621, 1961.6115, 1249.9998), (0.0, 179.99988388675877, -0.0), (1.0, 1.0, 1.0), "BP_Mines_Ceiling_Brace_A_Bracket3", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_brk_mesh, _brk_mats, (4740.6216, 2040.8818, 1249.9998), (0.0, 179.99988388675877, -0.0), (1.0, 1.0, 1.0), "BP_Mines_Ceiling_Brace_A_Bracket4", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_brk_mesh, _brk_mats, (4913.3223, 1961.6115, 699.99976), (0.0, 179.99988388675877, -0.0), (1.0, 1.0, 1.0), "BP_Mines_Ceiling_Brace_A_Bracket5_9", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_brk_mesh, _brk_mats, (4913.3228, 2040.8818, 699.99976), (0.0, 179.99988388675877, -0.0), (1.0, 1.0, 1.0), "BP_Mines_Ceiling_Brace_A_Bracket6", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_brk_mesh, _brk_mats, (3593.7893, 2040.8628, 768.8018), (0.0, 0.0, -0.0), (1.0, 1.0, 1.0), "BP_Mines_Ceiling_Brace_A_Bracket7", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_brk_mesh, _brk_mats, (3593.7893, 1961.5913, 768.8018), (0.0, 0.0, -0.0), (1.0, 1.0, 1.0), "BP_Mines_Ceiling_Brace_A_Bracket8", _folder)
if a: placed += 1
else: skipped += 1

# Breakable Batch 19: BP_Mines_Support_Beam_B (10 instances)
#   BP Class: /Game/LevelDesign/Deco_Architecture/Mines/BP_Mines_Support_Beam_B
_brk_mesh = "/Game/Art/Assets/Kits/Deco/Mines/Machine/Mines_Machine_Whim_Pieces/Mines_Machine_Whim_Wheel_Middle_Bracket_B"
_brk_mats = ['/Game/Art/Assets/Kits/Deco/Mines/Materials/Mines_Machine_Whim/MI_Mines_Machine_Whim_Trim']
a = spawn_static_mesh(_brk_mesh, _brk_mats, (3804.8855, 2040.8628, 1099.9998), (-90.0, 1.8848502594162701e-06, -359.99997456409073), (1.0, 1.0, 1.0), "BP_Mines_Support_Beam_B_2", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_brk_mesh, _brk_mats, (4690.6206, 2040.8824, 499.99933), (-90.0, 14.024293125752541, -194.02444224192539), (1.0, 1.0, 1.0), "BP_Mines_Support_Beam_B10", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_brk_mesh, _brk_mats, (3804.8855, 2040.8628, 799.99945), (-90.0, 1.1029615739881892e-06, 3.093243794535529e-05), (1.0, 1.0, 1.0), "BP_Mines_Support_Beam_B2", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_brk_mesh, _brk_mats, (3804.8855, 1961.5913, 1099.9998), (-90.0, 1.1029615739881892e-06, 3.093243794535529e-05), (1.0, 1.0, 1.0), "BP_Mines_Support_Beam_B3", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_brk_mesh, _brk_mats, (3804.8855, 1961.5913, 799.9993), (-90.0, -2.445095509883975e-05, 5.645095651739012e-05), (1.0, 1.0, 1.0), "BP_Mines_Support_Beam_B4", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_brk_mesh, _brk_mats, (4690.6206, 1961.6107, 1099.9998), (-90.0, 9.454165594553745, -189.45431078661466), (1.0, 1.0, 1.0), "BP_Mines_Support_Beam_B5", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_brk_mesh, _brk_mats, (4690.6206, 1961.6107, 799.99945), (-90.0, 9.454165594553745, -189.45431078661466), (1.0, 1.0, 1.0), "BP_Mines_Support_Beam_B6", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_brk_mesh, _brk_mats, (4690.6206, 2040.8824, 1099.9998), (-90.0, 9.454165594553745, -189.45431078661466), (1.0, 1.0, 1.0), "BP_Mines_Support_Beam_B7", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_brk_mesh, _brk_mats, (4690.6206, 2040.8824, 799.9993), (-90.0, 9.454165594553745, -189.45431078661466), (1.0, 1.0, 1.0), "BP_Mines_Support_Beam_B8", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_brk_mesh, _brk_mats, (4690.6206, 1961.6107, 499.99945), (-90.0, 14.024293125752541, -194.02444224192539), (1.0, 1.0, 1.0), "BP_Mines_Support_Beam_B9", _folder)
if a: placed += 1
else: skipped += 1

# --- Extra DecoVolumes (not construction blocks) ---
_folder = "Reconstruction/BD_BB_Passage_SpiralCave/DecoVolumes"

# DecoVolume: AB_Mines_Scaffolding_Rail_Corner_2 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (2167.9058, 1495.1685, 4367.5615), (0.0, 0.0, -0.0), (1.5767, 1.4679, 1.1347), "DV_AB_Mines_Scaffolding_Rail_Corner_2_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_DM_Mine_tailings_Debris_2x2_A_2 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (2843.77, 2092.0583, 3349.6267), (0.0, 0.0, -0.0), (2.0658, 2.0672, 0.5085), "DV_BP_DM_Mine_tailings_Debris_2x2_A_2_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_DM_Mine_tailings_Debris_2x2_A2_5 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (4946.43, 1864.0013, 762.77136), (0.0, 0.0, -0.0), (2.7969, 2.8406, 0.9133), "DV_BP_DM_Mine_tailings_Debris_2x2_A2_5_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_DM_Mine_tailings_Debris_2x2_B_2 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (3082.383, 1573.3641, 828.68646), (0.0, 0.0, -0.0), (2.8110, 2.8083, 0.9793), "DV_BP_DM_Mine_tailings_Debris_2x2_B_2_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_DM_Mine_tailings_Debris_3x3_A_2 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (3510.9658, 1654.7234, 809.42755), (0.0, 0.0, -0.0), (3.0000, 3.0055, 1.0281), "DV_BP_DM_Mine_tailings_Debris_3x3_A_2_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_DM_Mine_tailings_Debris_3x3_A2 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (2504.0342, 1600.2766, 809.42755), (0.0, 0.0, -0.0), (3.0000, 3.0055, 1.0281), "DV_BP_DM_Mine_tailings_Debris_3x3_A2_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_DM_Mine_tailings_Debris_3x3_A3_5 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (3315.8513, 2145.5337, 3349.4275), (0.0, 0.0, -0.0), (4.2407, 4.2402, 1.0281), "DV_BP_DM_Mine_tailings_Debris_3x3_A3_5_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_DM_Mine_tailings_Debris_3x3_A4_8 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (850.96594, 2854.7234, 4009.4275), (0.0, 0.0, -0.0), (3.0000, 3.0055, 1.0281), "DV_BP_DM_Mine_tailings_Debris_3x3_A4_8_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_DM_Mine_tailings_Debris_3x3_B_2 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (3739.7546, 1747.7777, 813.01996), (0.0, 0.0, -0.0), (3.7156, 3.5489, 0.6855), "DV_BP_DM_Mine_tailings_Debris_3x3_B_2_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_DM_Mine_tailings_Debris_3x3_B2_2 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (3887.9348, 2265.6587, 3348.02), (0.0, 0.0, -0.0), (2.8479, 3.0836, 0.6855), "DV_BP_DM_Mine_tailings_Debris_3x3_B2_2_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_DM_Mine_tailings_Debris_3x3_B3_5 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (3702.4338, 2150.8352, 3353.02), (0.0, 0.0, -0.0), (4.1879, 4.1522, 0.6855), "DV_BP_DM_Mine_tailings_Debris_3x3_B3_5_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_DM_Mine_tailings_Debris_3x3_B4_8 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (704.2778, 3551.3335, 4013.02), (0.0, 0.0, -0.0), (4.0839, 4.1480, 0.6855), "DV_BP_DM_Mine_tailings_Debris_3x3_B4_8_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_DM_Mines_Debris_2x2_B_2 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (2802.4375, 1607.5977, 802.1371), (0.0, 0.0, -0.0), (3.6588, 3.4833, 0.6345), "DV_BP_DM_Mines_Debris_2x2_B_2_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_DM_Mines_Debris_2x2_B2_14 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (2397.5977, 1982.5625, 810.1371), (0.0, 0.0, -0.0), (3.4833, 3.6588, 0.6345), "DV_BP_DM_Mines_Debris_2x2_B2_14_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_DM_Mines_Debris_2x2_C_2 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (2645.0, 1585.0, 806.1499), (0.0, 0.0, -0.0), (2.2675, 2.2675, 0.3612), "DV_BP_DM_Mines_Debris_2x2_C_2_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_DM_Mines_Debris_2x2_C2 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (2535.0, 1520.0, 806.1499), (0.0, 0.0, -0.0), (2.2675, 2.2675, 0.3612), "DV_BP_DM_Mines_Debris_2x2_C2_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_DM_Mines_Debris_2x2_C3 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (3090.0, 1595.0, 806.1499), (0.0, 0.0, -0.0), (2.2675, 2.2675, 0.3612), "DV_BP_DM_Mines_Debris_2x2_C3_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_DM_Mines_Debris_2x2_C4_12 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (2485.0, 1955.0, 808.1499), (0.0, 0.0, -0.0), (2.2675, 2.2675, 0.3612), "DV_BP_DM_Mines_Debris_2x2_C4_12_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_DM_Mines_Scaffolding_Beam_2M_A_2 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (4427.852, 3517.1611, 2087.4768), (0.0, 0.0, -0.0), (0.7099, 0.7151, 1.7527), "DV_BP_DM_Mines_Scaffolding_Beam_2M_A_2_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_DM_Mines_Scaffolding_Beam_2M_A6 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (4427.839, 3282.852, 2087.4768), (0.0, 0.0, -0.0), (0.7151, 0.7099, 1.7527), "DV_BP_DM_Mines_Scaffolding_Beam_2M_A6_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_DM_Mines_Scaffolding_Beam_2M_A7 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (4662.148, 3272.839, 2087.4768), (0.0, 0.0, -0.0), (0.7099, 0.7151, 1.7527), "DV_BP_DM_Mines_Scaffolding_Beam_2M_A7_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_DM_Mines_Scaffolding_Beam_2M_A8 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (4661.837, 3526.019, 2087.4768), (0.0, 0.0, -0.0), (0.7491, 0.7441, 1.7527), "DV_BP_DM_Mines_Scaffolding_Beam_2M_A8_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_DM_Mines_Scaffolding_Beam_2M_B13_33 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (3126.7993, 2196.0532, 3387.4768), (0.0, 0.0, -0.0), (0.2646, 0.2649, 1.7527), "DV_BP_DM_Mines_Scaffolding_Beam_2M_B13_33_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_DM_Mines_Scaffolding_Beam_2M_B14_36 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (3106.8225, 2195.0715, 3387.4768), (0.0, 0.0, -0.0), (0.2646, 0.2649, 1.7527), "DV_BP_DM_Mines_Scaffolding_Beam_2M_B14_36_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_DM_Mines_Scaffolding_Beam_2M_B15_37 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (2722.286, 2176.181, 3387.4768), (0.0, 0.0, -0.0), (0.2646, 0.2649, 1.7527), "DV_BP_DM_Mines_Scaffolding_Beam_2M_B15_37_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_DM_Mines_Scaffolding_Beam_2M_B16_39 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (2702.3113, 2175.1995, 3387.4768), (0.0, 0.0, -0.0), (0.2646, 0.2649, 1.7527), "DV_BP_DM_Mines_Scaffolding_Beam_2M_B16_39_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_DM_Mines_Scaffolding_Beam_2M_B18 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (3621.2026, 2220.3418, 3387.4768), (0.0, 0.0, -0.0), (0.2646, 0.2649, 1.7527), "DV_BP_DM_Mines_Scaffolding_Beam_2M_B18_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_DM_Mines_Scaffolding_Beam_2M_B19 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (2887.0872, 2184.2766, 3387.4768), (0.0, 0.0, -0.0), (0.2646, 0.2649, 1.7527), "DV_BP_DM_Mines_Scaffolding_Beam_2M_B19_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_DM_Mines_Scaffolding_Beam_2M_B20 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (3246.6545, 2201.9407, 3387.4768), (0.0, 0.0, -0.0), (0.2646, 0.2649, 1.7527), "DV_BP_DM_Mines_Scaffolding_Beam_2M_B20_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_DM_Mines_Scaffolding_Beam_2M_B21 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (3591.2385, 2218.8696, 3387.4768), (0.0, 0.0, -0.0), (0.2646, 0.2649, 1.7527), "DV_BP_DM_Mines_Scaffolding_Beam_2M_B21_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_DM_Mines_Scaffolding_Beam_2M_B3 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (3850.926, 2231.6272, 3387.4768), (0.0, 0.0, -0.0), (0.2646, 0.2649, 1.7527), "DV_BP_DM_Mines_Scaffolding_Beam_2M_B3_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_DM_Mines_Scaffolding_Beam_2M_B4_1 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (3870.902, 2232.6086, 3387.4768), (0.0, 0.0, -0.0), (0.2646, 0.2649, 1.7527), "DV_BP_DM_Mines_Scaffolding_Beam_2M_B4_1_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_DM_Mines_Scaffolding_Beam_2M_B5_20 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (3301.5886, 2204.6394, 3387.4768), (0.0, 0.0, -0.0), (0.2646, 0.2649, 1.7527), "DV_BP_DM_Mines_Scaffolding_Beam_2M_B5_20_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_DM_Mines_Scaffolding_Beam_2M_C_2 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (1242.9749, 4323.0054, 706.6224), (0.0, 0.0, -0.0), (1.7710, 1.4008, 1.1644), "DV_BP_DM_Mines_Scaffolding_Beam_2M_C_2_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_DM_Mines_Scaffolding_Beam_2M_C2 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (1453.9951, 4371.4175, 680.8276), (0.0, 0.0, -0.0), (0.9650, 1.7131, 1.2623), "DV_BP_DM_Mines_Scaffolding_Beam_2M_C2_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_DM_Mines_Scaffolding_Beam_2M_C3 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (3082.033, 4316.7676, 1563.92), (0.0, 0.0, -0.0), (1.9020, 1.4451, 0.5758), "DV_BP_DM_Mines_Scaffolding_Beam_2M_C3_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_DM_Mines_Scaffolding_Beam_2M_C4 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (1009.42474, 1448.6171, 761.3988), (0.0, 0.0, -0.0), (1.4395, 1.8504, 0.9040), "DV_BP_DM_Mines_Scaffolding_Beam_2M_C4_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_DM_Mines_Scaffolding_Beam_2M_C5 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (1269.2687, 1358.0823, 772.15546), (0.0, 0.0, -0.0), (1.8871, 1.2197, 0.7377), "DV_BP_DM_Mines_Scaffolding_Beam_2M_C5_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_DM_Mines_Scaffolding_Beam_2M_C6 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (1522.9371, 636.28986, 806.4759), (0.0, 0.0, -0.0), (0.8800, 1.7959, 0.6173), "DV_BP_DM_Mines_Scaffolding_Beam_2M_C6_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_DM_Mines_Scaffolding_Beam_2M_C7 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (1279.7821, 465.13318, 857.3166), (0.0, 0.0, -0.0), (1.8221, 0.8748, 0.3843), "DV_BP_DM_Mines_Scaffolding_Beam_2M_C7_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_DM_Mines_Scaffolding_Girder_4M_A (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (3861.7866, 2249.879, 3798.9502), (0.0, 0.0, -0.0), (0.8380, 2.3721, 5.9785), "DV_BP_DM_Mines_Scaffolding_Girder_4M_A_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_DM_Mines_Scaffolding_Girder_4M_A2 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (3856.9297, 2465.527, 3798.9502), (0.0, 0.0, -0.0), (0.8380, 2.3721, 5.9785), "DV_BP_DM_Mines_Scaffolding_Girder_4M_A2_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_DM_Mines_Scaffolding_Girder_4M_A6 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (2438.149, 2405.8362, 3798.9502), (0.0, 0.0, -0.0), (0.8380, 2.3721, 5.9785), "DV_BP_DM_Mines_Scaffolding_Girder_4M_A6_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_DM_Mines_Scaffolding_Girder_4M_A9 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (2443.0059, 2190.187, 3798.9502), (0.0, 0.0, -0.0), (0.8380, 2.3721, 5.9785), "DV_BP_DM_Mines_Scaffolding_Girder_4M_A9_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_DM_Mines_Scaffolding_Platform_2X2M_A_3 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (2477.0427, 1813.9705, 926.677), (0.0, 0.0, -0.0), (2.1539, 2.0924, 2.5864), "DV_BP_DM_Mines_Scaffolding_Platform_2X2M_A_3_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_DM_Mines_Scaffolding_Platform_3X1M_A10 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (3132.0398, 2183.658, 3486.6565), (0.0, 0.0, -0.0), (3.1041, 1.2065, 0.2869), "DV_BP_DM_Mines_Scaffolding_Platform_3X1M_A10_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_DM_Mines_Scaffolding_Platform_3X1M_A11 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (2832.4014, 2168.9375, 3486.6565), (0.0, 0.0, -0.0), (3.1041, 1.2065, 0.2869), "DV_BP_DM_Mines_Scaffolding_Platform_3X1M_A11_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_DM_Mines_Scaffolding_Platform_3X1M_A12_2 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (2532.7625, 2154.2158, 3486.6565), (0.0, 0.0, -0.0), (3.1041, 1.2065, 0.2869), "DV_BP_DM_Mines_Scaffolding_Platform_3X1M_A12_2_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_DM_Mines_Scaffolding_Platform_3X1M_A4_2 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (3731.3157, 2213.0981, 3486.6565), (0.0, 0.0, -0.0), (3.1041, 1.2065, 0.2869), "DV_BP_DM_Mines_Scaffolding_Platform_3X1M_A4_2_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_DM_Mines_Scaffolding_Platform_3X1M_A5 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (3431.678, 2198.378, 3486.6565), (0.0, 0.0, -0.0), (3.1041, 1.2065, 0.2869), "DV_BP_DM_Mines_Scaffolding_Platform_3X1M_A5_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_DM_Mines_Scaffolding_Platform_3X1M_B_9 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (3719.4702, 2561.7166, 714.52686), (0.0, 0.0, -0.0), (1.6919, 2.4580, 0.8984), "DV_BP_DM_Mines_Scaffolding_Platform_3X1M_B_9_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_DM_Mines_Scaffolding_Platform_3X1M_B2 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (3649.7827, 3061.705, 1488.3861), (0.0, 0.0, -0.0), (1.0468, 2.2543, 0.2844), "DV_BP_DM_Mines_Scaffolding_Platform_3X1M_B2_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_DM_Mines_Scaffolding_Platform_3X1M_B3 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (3656.2544, 3293.6506, 599.6381), (0.0, 0.0, -0.0), (1.2369, 2.3576, 1.0451), "DV_BP_DM_Mines_Scaffolding_Platform_3X1M_B3_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_DM_Mines_Scaffolding_Platform_3X1M_B4 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (3862.5972, 2347.8687, 764.2907), (0.0, 0.0, -0.0), (2.4801, 1.9622, 0.9258), "DV_BP_DM_Mines_Scaffolding_Platform_3X1M_B4_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_DM_Mines_Scaffolding_Platform_3X1M_B5_2 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (5214.017, 3623.163, 3994.6372), (0.0, 0.0, -0.0), (2.3233, 1.0843, 1.0047), "DV_BP_DM_Mines_Scaffolding_Platform_3X1M_B5_2_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_DM_Mines_Scaffolding_Platform_3X1M_C_2 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (3650.3184, 3717.2805, 1488.9031), (0.0, 0.0, -0.0), (1.0138, 3.0520, 0.2873), "DV_BP_DM_Mines_Scaffolding_Platform_3X1M_C_2_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_DM_Mines_Scaffolding_Platform_3X1M_C10 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (3651.8452, 2636.7065, 738.6005), (0.0, 0.0, -0.0), (1.9047, 3.1322, 1.5427), "DV_BP_DM_Mines_Scaffolding_Platform_3X1M_C10_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_DM_Mines_Scaffolding_Platform_3X1M_C11 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (3878.4482, 2613.1868, 691.73706), (0.0, 0.0, -0.0), (2.3113, 3.1506, 1.1571), "DV_BP_DM_Mines_Scaffolding_Platform_3X1M_C11_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_DM_Mines_Scaffolding_Platform_3X1M_C12_19 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (1735.6892, 5392.6646, 1248.8682), (0.0, 0.0, -0.0), (1.7993, 3.2185, 0.4330), "DV_BP_DM_Mines_Scaffolding_Platform_3X1M_C12_19_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_DM_Mines_Scaffolding_Platform_3X1M_C13 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (1717.0508, 4406.0137, 1002.9551), (0.0, 0.0, -0.0), (3.0640, 2.4324, 1.2390), "DV_BP_DM_Mines_Scaffolding_Platform_3X1M_C13_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_DM_Mines_Scaffolding_Platform_3X1M_C14 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (1791.6592, 4856.1973, 1231.0349), (0.0, 0.0, -0.0), (1.8096, 3.2205, 0.4605), "DV_BP_DM_Mines_Scaffolding_Platform_3X1M_C14_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_DM_Mines_Scaffolding_Platform_3X1M_C15 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (2582.1746, 4003.8257, 636.92865), (0.0, 0.0, -0.0), (3.2206, 1.8891, 1.0822), "DV_BP_DM_Mines_Scaffolding_Platform_3X1M_C15_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_DM_Mines_Scaffolding_Platform_3X1M_C16 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (1751.1171, 4177.027, 618.3384), (0.0, 0.0, -0.0), (3.0901, 2.2221, 1.8065), "DV_BP_DM_Mines_Scaffolding_Platform_3X1M_C16_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_DM_Mines_Scaffolding_Platform_3X1M_C17_26 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (2415.1218, 3467.6465, 637.9014), (0.0, 0.0, -0.0), (3.0890, 2.5164, 1.2364), "DV_BP_DM_Mines_Scaffolding_Platform_3X1M_C17_26_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_DM_Mines_Scaffolding_Platform_3X1M_C18 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (2394.2646, 3136.6125, 770.35474), (0.0, 0.0, -0.0), (3.1911, 1.6256, 0.7886), "DV_BP_DM_Mines_Scaffolding_Platform_3X1M_C18_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_DM_Mines_Scaffolding_Platform_3X1M_C19 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (3195.1028, 4184.757, 1476.9922), (0.0, 0.0, -0.0), (3.2088, 2.0913, 0.2873), "DV_BP_DM_Mines_Scaffolding_Platform_3X1M_C19_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_DM_Mines_Scaffolding_Platform_3X1M_C2_5 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (3651.2273, 3688.438, 634.19196), (0.0, 0.0, -0.0), (1.0486, 2.9513, 1.4507), "DV_BP_DM_Mines_Scaffolding_Platform_3X1M_C2_5_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_DM_Mines_Scaffolding_Platform_3X1M_C20 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (2714.2554, 4294.221, 1468.2499), (0.0, 0.0, -0.0), (3.1545, 1.6283, 1.3917), "DV_BP_DM_Mines_Scaffolding_Platform_3X1M_C20_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_DM_Mines_Scaffolding_Platform_3X1M_C21 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (1340.2781, 676.08685, 834.0115), (0.0, 0.0, -0.0), (2.6105, 3.0640, 0.8773), "DV_BP_DM_Mines_Scaffolding_Platform_3X1M_C21_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_DM_Mines_Scaffolding_Platform_3X1M_C22 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (779.7634, 1492.5385, 793.52747), (0.0, 0.0, -0.0), (3.1246, 2.4675, 1.0004), "DV_BP_DM_Mines_Scaffolding_Platform_3X1M_C22_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_DM_Mines_Scaffolding_Platform_3X1M_C23_2 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (2972.215, 4195.3174, 2858.6008), (0.0, 0.0, -0.0), (2.0446, 2.8577, 2.2618), "DV_BP_DM_Mines_Scaffolding_Platform_3X1M_C23_2_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_DM_Mines_Scaffolding_Platform_3X1M_C24_5 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (3622.7136, 4132.7393, 3154.7383), (0.0, 0.0, -0.0), (1.7099, 3.0732, 1.4461), "DV_BP_DM_Mines_Scaffolding_Platform_3X1M_C24_5_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_DM_Mines_Scaffolding_Platform_3X1M_C25_10 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (3238.4866, 4362.0073, 3174.0935), (0.0, 0.0, -0.0), (3.1903, 1.9392, 0.9876), "DV_BP_DM_Mines_Scaffolding_Platform_3X1M_C25_10_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_DM_Mines_Scaffolding_Platform_3X1M_C26 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (3860.8892, 3851.5767, 3190.7722), (0.0, 0.0, -0.0), (1.9594, 3.2285, 0.5463), "DV_BP_DM_Mines_Scaffolding_Platform_3X1M_C26_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_DM_Mines_Scaffolding_Platform_3X1M_C27 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (3849.4644, 3550.6494, 3190.7722), (0.0, 0.0, -0.0), (1.8277, 3.2223, 0.5463), "DV_BP_DM_Mines_Scaffolding_Platform_3X1M_C27_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_DM_Mines_Scaffolding_Platform_3X1M_C28 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (3913.1553, 3254.5417, 3203.7107), (0.0, 0.0, -0.0), (2.2000, 3.1834, 1.0059), "DV_BP_DM_Mines_Scaffolding_Platform_3X1M_C28_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_DM_Mines_Scaffolding_Platform_3X1M_C29 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (3532.1145, 3052.3086, 4933.0625), (0.0, 0.0, -0.0), (3.0981, 1.1623, 0.2873), "DV_BP_DM_Mines_Scaffolding_Platform_3X1M_C29_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_DM_Mines_Scaffolding_Platform_3X1M_C3_8 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (1408.6136, 4297.0796, 638.6905), (0.0, 0.0, -0.0), (2.6616, 2.8846, 1.5266), "DV_BP_DM_Mines_Scaffolding_Platform_3X1M_C3_8_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_DM_Mines_Scaffolding_Platform_3X1M_C30 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (3415.0708, 2936.6072, 4933.0625), (0.0, 0.0, -0.0), (1.1623, 3.0980, 0.2873), "DV_BP_DM_Mines_Scaffolding_Platform_3X1M_C30_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_DM_Mines_Scaffolding_Platform_3X1M_C31 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (2748.3267, 2879.804, 4919.9893), (0.0, 0.0, -0.0), (2.0742, 3.0174, 1.6516), "DV_BP_DM_Mines_Scaffolding_Platform_3X1M_C31_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_DM_Mines_Scaffolding_Platform_3X1M_C32 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (3331.3901, 2716.7974, 5228.0625), (0.0, 0.0, -0.0), (1.1623, 3.0980, 0.2873), "DV_BP_DM_Mines_Scaffolding_Platform_3X1M_C32_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_DM_Mines_Scaffolding_Platform_3X1M_C33 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (3331.3901, 2716.7974, 4928.0625), (0.0, 0.0, -0.0), (1.1623, 3.0980, 0.2873), "DV_BP_DM_Mines_Scaffolding_Platform_3X1M_C33_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_DM_Mines_Scaffolding_Platform_3X1M_C34 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (3716.8967, 3163.6455, 4933.0625), (0.0, 0.0, -0.0), (3.0980, 1.1623, 0.2873), "DV_BP_DM_Mines_Scaffolding_Platform_3X1M_C34_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_DM_Mines_Scaffolding_Platform_3X1M_C35 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (3387.2825, 2109.6812, 1488.9031), (0.0, 0.0, -0.0), (3.0520, 1.0138, 0.2873), "DV_BP_DM_Mines_Scaffolding_Platform_3X1M_C35_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_DM_Mines_Scaffolding_Platform_3X1M_C36 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (5278.643, 3025.097, 4001.003), (0.0, 0.0, -0.0), (1.0450, 3.0520, 0.4330), "DV_BP_DM_Mines_Scaffolding_Platform_3X1M_C36_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_DM_Mines_Scaffolding_Platform_3X1M_C37 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (5286.0396, 3325.097, 3987.1626), (0.0, 0.0, -0.0), (0.9854, 3.0520, 0.8347), "DV_BP_DM_Mines_Scaffolding_Platform_3X1M_C37_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_DM_Mines_Scaffolding_Platform_3X1M_C38 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (5339.567, 2487.5166, 4004.7485), (0.0, 0.0, -0.0), (1.6174, 3.1988, 0.4931), "DV_BP_DM_Mines_Scaffolding_Platform_3X1M_C38_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_DM_Mines_Scaffolding_Platform_3X1M_C39 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (5389.6514, 1875.0969, 3990.595), (0.0, 0.0, -0.0), (1.0532, 3.0520, 0.5250), "DV_BP_DM_Mines_Scaffolding_Platform_3X1M_C39_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_DM_Mines_Scaffolding_Platform_3X1M_C4 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (3749.6812, 3722.7195, 1488.9031), (0.0, 0.0, -0.0), (1.0138, 3.0520, 0.2873), "DV_BP_DM_Mines_Scaffolding_Platform_3X1M_C4_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_DM_Mines_Scaffolding_Platform_3X1M_C40 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (5376.6646, 2185.097, 4000.8518), (0.0, 0.0, -0.0), (1.0371, 3.0520, 0.3853), "DV_BP_DM_Mines_Scaffolding_Platform_3X1M_C40_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_DM_Mines_Scaffolding_Platform_3X1M_C41 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (5296.823, 3537.337, 3969.1484), (0.0, 0.0, -0.0), (3.1360, 1.0610, 1.3788), "DV_BP_DM_Mines_Scaffolding_Platform_3X1M_C41_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_DM_Mines_Scaffolding_Platform_3X1M_C42 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (5313.6343, 1616.1346, 3935.7358), (0.0, 0.0, -0.0), (2.1472, 3.1071, 1.8208), "DV_BP_DM_Mines_Scaffolding_Platform_3X1M_C42_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_DM_Mines_Scaffolding_Platform_3X1M_C43 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (3277.0781, 5175.664, 1567.5337), (0.0, 0.0, -0.0), (3.0520, 1.0138, 0.2873), "DV_BP_DM_Mines_Scaffolding_Platform_3X1M_C43_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_DM_Mines_Scaffolding_Platform_3X1M_C44 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (3091.6572, 1045.1168, 4003.7488), (0.0, 0.0, -0.0), (3.1280, 1.2729, 0.2873), "DV_BP_DM_Mines_Scaffolding_Platform_3X1M_C44_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_DM_Mines_Scaffolding_Platform_3X1M_C45 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (3390.5417, 1019.27637, 4003.7488), (0.0, 0.0, -0.0), (3.1280, 1.2729, 0.2873), "DV_BP_DM_Mines_Scaffolding_Platform_3X1M_C45_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_DM_Mines_Scaffolding_Platform_3X1M_C46 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (2977.4067, 5150.552, 1528.3849), (0.0, 0.0, -0.0), (3.1525, 1.5232, 1.0675), "DV_BP_DM_Mines_Scaffolding_Platform_3X1M_C46_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_DM_Mines_Scaffolding_Platform_3X1M_C47 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (2679.5156, 5154.472, 1460.3308), (0.0, 0.0, -0.0), (3.1646, 1.5553, 1.0253), "DV_BP_DM_Mines_Scaffolding_Platform_3X1M_C47_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_DM_Mines_Scaffolding_Platform_3X1M_C5 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (3749.683, 2802.7195, 1488.9031), (0.0, 0.0, -0.0), (1.0138, 3.0520, 0.2873), "DV_BP_DM_Mines_Scaffolding_Platform_3X1M_C5_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_DM_Mines_Scaffolding_Platform_3X1M_C6 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (3749.683, 2502.7195, 1488.9031), (0.0, 0.0, -0.0), (1.0138, 3.0520, 0.2873), "DV_BP_DM_Mines_Scaffolding_Platform_3X1M_C6_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_DM_Mines_Scaffolding_Platform_3X1M_C7 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (3749.683, 2202.7195, 1488.9031), (0.0, 0.0, -0.0), (1.0138, 3.0520, 0.2873), "DV_BP_DM_Mines_Scaffolding_Platform_3X1M_C7_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_DM_Mines_Scaffolding_Platform_3X1M_C8 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (3550.3203, 2197.2805, 1488.9031), (0.0, 0.0, -0.0), (1.0138, 3.0520, 0.2873), "DV_BP_DM_Mines_Scaffolding_Platform_3X1M_C8_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_DM_Mines_Scaffolding_Platform_3X1M_C9 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (3838.2915, 3718.276, 647.5817), (0.0, 0.0, -0.0), (2.0725, 3.1290, 1.3153), "DV_BP_DM_Mines_Scaffolding_Platform_3X1M_C9_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_DM_Mines_Scaffolding_Platform_3X3M_B_2 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (3688.3713, 3012.8066, 636.392), (0.0, 0.0, -0.0), (2.9593, 3.5215, 0.8382), "DV_BP_DM_Mines_Scaffolding_Platform_3X3M_B_2_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_DM_Mines_Scaffolding_Platform_3X3M_B11 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (5471.0674, 2899.6462, 4019.2366), (0.0, 0.0, -0.0), (3.0595, 2.2624, 0.6116), "DV_BP_DM_Mines_Scaffolding_Platform_3X3M_B11_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_DM_Mines_Scaffolding_Platform_3X3M_B12 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (5469.784, 3413.139, 4002.6526), (0.0, 0.0, -0.0), (3.0544, 2.2569, 0.5601), "DV_BP_DM_Mines_Scaffolding_Platform_3X3M_B12_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_DM_Mines_Scaffolding_Platform_3X3M_B13 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (5569.9565, 2249.8396, 3992.786), (0.0, 0.0, -0.0), (3.0544, 2.2569, 0.5601), "DV_BP_DM_Mines_Scaffolding_Platform_3X3M_B13_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_DM_Mines_Scaffolding_Platform_3X3M_B14 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (5484.198, 2750.2175, 4001.233), (0.0, 0.0, -0.0), (3.3512, 2.6790, 0.5893), "DV_BP_DM_Mines_Scaffolding_Platform_3X3M_B14_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_DM_Mines_Scaffolding_Platform_3X3M_B15 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (5518.6577, 1553.513, 3997.8389), (0.0, 0.0, -0.0), (3.7239, 3.3414, 0.6260), "DV_BP_DM_Mines_Scaffolding_Platform_3X3M_B15_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_DM_Mines_Scaffolding_Platform_3X3M_B16 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (5579.255, 2083.139, 3991.8708), (0.0, 0.0, -0.0), (3.0544, 2.2569, 0.5601), "DV_BP_DM_Mines_Scaffolding_Platform_3X3M_B16_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_DM_Mines_Scaffolding_Platform_3X3M_B17_10 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (4641.8843, 1313.9254, 3363.4485), (0.0, 0.0, -0.0), (3.7452, 3.7452, 0.8037), "DV_BP_DM_Mines_Scaffolding_Platform_3X3M_B17_10_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_DM_Mines_Scaffolding_Platform_3X3M_B18 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (4855.8447, 1531.6259, 3373.6091), (0.0, 0.0, -0.0), (3.7393, 3.7623, 0.8445), "DV_BP_DM_Mines_Scaffolding_Platform_3X3M_B18_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_DM_Mines_Scaffolding_Platform_3X3M_B2 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (1347.2106, 4512.282, 756.72675), (0.0, 0.0, -0.0), (3.6471, 3.2231, 1.2628), "DV_BP_DM_Mines_Scaffolding_Platform_3X3M_B2_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_DM_Mines_Scaffolding_Platform_3X3M_B3_7 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (1770.7892, 4570.5454, 1228.2897), (0.0, 0.0, -0.0), (3.7478, 3.7478, 0.2631), "DV_BP_DM_Mines_Scaffolding_Platform_3X3M_B3_7_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_DM_Mines_Scaffolding_Platform_3X3M_B4 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (2244.3696, 4455.854, 1301.8313), (0.0, 0.0, -0.0), (3.4348, 2.9473, 1.2647), "DV_BP_DM_Mines_Scaffolding_Platform_3X3M_B4_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_DM_Mines_Scaffolding_Platform_3X3M_B5_14 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (2796.296, 3473.4324, 640.5278), (0.0, 0.0, -0.0), (3.3130, 2.3938, 1.5863), "DV_BP_DM_Mines_Scaffolding_Platform_3X3M_B5_14_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_DM_Mines_Scaffolding_Platform_3X3M_B6 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (1182.2795, 1207.9794, 813.6503), (0.0, 0.0, -0.0), (3.7516, 3.7157, 1.0623), "DV_BP_DM_Mines_Scaffolding_Platform_3X3M_B6_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_DM_Mines_Scaffolding_Platform_3X3M_B7_2 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (3429.4536, 4318.799, 3071.3606), (0.0, 0.0, -0.0), (3.5896, 1.8773, 2.7794), "DV_BP_DM_Mines_Scaffolding_Platform_3X3M_B7_2_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_DM_Mines_Scaffolding_Platform_3X3M_B8 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (2925.3958, 4289.4424, 3065.104), (0.0, 0.0, -0.0), (3.4863, 1.4171, 2.7412), "DV_BP_DM_Mines_Scaffolding_Platform_3X3M_B8_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_DM_Mines_Scaffolding_Platform_3X3M_B9 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (5469.4424, 3579.8396, 4002.686), (0.0, 0.0, -0.0), (3.0544, 2.2569, 0.5601), "DV_BP_DM_Mines_Scaffolding_Platform_3X3M_B9_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_DM_Mines_Scaffolding_Platform_3X3M_C_3 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (3254.9995, 1630.4739, 950.4507), (0.0, 0.0, -0.0), (3.1718, 2.4818, 3.0510), "DV_BP_DM_Mines_Scaffolding_Platform_3X3M_C_3_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_DM_Mines_Scaffolding_Post_1M_A_8 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (3775.1943, 2001.1707, 875.16296), (0.0, 0.0, -0.0), (0.2013, 0.9987, 0.1098), "DV_BP_DM_Mines_Scaffolding_Post_1M_A_8_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_DM_Mines_Scaffolding_Post_1M_A2 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (3775.194, 2001.1707, 975.163), (0.0, 0.0, -0.0), (0.2013, 0.9987, 0.1098), "DV_BP_DM_Mines_Scaffolding_Post_1M_A2_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_DM_Mines_Scaffolding_Post_1M_A3_2 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (3186.871, 2197.0642, 3380.0017), (0.0, 0.0, -0.0), (1.0029, 0.1587, 0.2013), "DV_BP_DM_Mines_Scaffolding_Post_1M_A3_2_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_DM_Mines_Scaffolding_Post_1M_A4 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (3775.194, 2001.1707, 1075.163), (0.0, 0.0, -0.0), (0.2013, 0.9987, 0.1098), "DV_BP_DM_Mines_Scaffolding_Post_1M_A4_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_DM_Mines_Scaffolding_Post_1M_A5 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (3775.194, 2001.1707, 1175.163), (0.0, 0.0, -0.0), (0.2013, 0.9987, 0.1098), "DV_BP_DM_Mines_Scaffolding_Post_1M_A5_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_DM_Mines_Scaffolding_Post_1M_A6 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (4720.3125, 2001.3027, 875.163), (0.0, 0.0, -0.0), (0.2013, 0.9987, 0.1098), "DV_BP_DM_Mines_Scaffolding_Post_1M_A6_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_DM_Mines_Scaffolding_Post_1M_A7 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (4720.3125, 2001.3027, 975.163), (0.0, 0.0, -0.0), (0.2013, 0.9987, 0.1098), "DV_BP_DM_Mines_Scaffolding_Post_1M_A7_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_DM_Mines_Scaffolding_Post_1M_A8 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (4720.3125, 2001.3027, 1075.163), (0.0, 0.0, -0.0), (0.2013, 0.9987, 0.1098), "DV_BP_DM_Mines_Scaffolding_Post_1M_A8_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_DM_Mines_Scaffolding_Post_1M_A9 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (4720.3125, 2001.3027, 1175.163), (0.0, 0.0, -0.0), (0.2013, 0.9987, 0.1098), "DV_BP_DM_Mines_Scaffolding_Post_1M_A9_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_DM_Mines_Scaffolding_Post_2M_A2_2 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (2776.6934, 2180.624, 3378.1926), (0.0, 0.0, -0.0), (1.9917, 0.2128, 0.2052), "DV_BP_DM_Mines_Scaffolding_Post_2M_A2_2_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_DM_Mines_Scaffolding_Post_2M_B2_2 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (3735.897, 2226.1262, 3377.472), (0.0, 0.0, -0.0), (2.1159, 0.1811, 0.2005), "DV_BP_DM_Mines_Scaffolding_Post_2M_B2_2_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_DM_Mines_Scaffolding_Post_2M_B3_7 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (2992.0823, 2189.5857, 3378.528), (0.0, 0.0, -0.0), (2.1159, 0.1811, 0.2005), "DV_BP_DM_Mines_Scaffolding_Post_2M_B3_7_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_DM_Mines_Scaffolding_Post_3M_A2_2 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (3432.9548, 2212.6284, 3378.0215), (0.0, 0.0, -0.0), (2.9894, 0.2563, 0.2013), "DV_BP_DM_Mines_Scaffolding_Post_3M_A2_2_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_DM_Mines_Scaffolding_Rail_1M_2 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (1007.0331, 5103.551, 1142.5139), (0.0, 0.0, -0.0), (1.6065, 0.5513, 0.8534), "DV_BP_DM_Mines_Scaffolding_Rail_1M_2_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_DM_Mines_Scaffolding_Rail_1M10 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (3189.5479, 4295.98, 1648.0944), (0.0, 0.0, -0.0), (1.8233, 0.2475, 1.3563), "DV_BP_DM_Mines_Scaffolding_Rail_1M10_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_DM_Mines_Scaffolding_Rail_1M11 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (1573.3412, 2471.3618, 4104.738), (0.0, 0.0, -0.0), (0.4915, 1.7453, 1.1291), "DV_BP_DM_Mines_Scaffolding_Rail_1M11_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_DM_Mines_Scaffolding_Rail_1M12 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (3653.62, 5018.1304, 1715.3582), (0.0, 0.0, -0.0), (1.8064, 0.5256, 1.3566), "DV_BP_DM_Mines_Scaffolding_Rail_1M12_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_DM_Mines_Scaffolding_Rail_1M2 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (425.24634, 5467.11, 1142.5139), (0.0, 0.0, -0.0), (0.5513, 1.6065, 0.8534), "DV_BP_DM_Mines_Scaffolding_Rail_1M2_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_DM_Mines_Scaffolding_Rail_1M3 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (503.79108, 5154.444, 1142.5139), (0.0, 0.0, -0.0), (0.5513, 1.6065, 0.8534), "DV_BP_DM_Mines_Scaffolding_Rail_1M3_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_DM_Mines_Scaffolding_Rail_1M4 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (4773.951, 1886.7556, 3402.514), (0.0, 0.0, -0.0), (1.5840, 0.6506, 0.8533), "DV_BP_DM_Mines_Scaffolding_Rail_1M4_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_DM_Mines_Scaffolding_Rail_1M5 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (4376.5166, 2230.8267, 3397.2817), (0.0, 0.0, -0.0), (1.3692, 1.2241, 1.0087), "DV_BP_DM_Mines_Scaffolding_Rail_1M5_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_DM_Mines_Scaffolding_Rail_1M6_2 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (1899.0569, 1854.7295, 4283.379), (0.0, 0.0, -0.0), (1.4212, 1.3227, 1.0755), "DV_BP_DM_Mines_Scaffolding_Rail_1M6_2_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_DM_Mines_Scaffolding_Rail_1M7 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (1749.2672, 2043.6016, 4266.1514), (0.0, 0.0, -0.0), (1.2056, 1.6172, 1.0250), "DV_BP_DM_Mines_Scaffolding_Rail_1M7_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_DM_Mines_Scaffolding_Rail_1M8_2 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (2498.7998, 4378.6553, 1428.7357), (0.0, 0.0, -0.0), (1.8270, 0.3905, 1.3684), "DV_BP_DM_Mines_Scaffolding_Rail_1M8_2_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_DM_Mines_Scaffolding_Rail_1M9 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (2720.3245, 4355.1562, 1502.1779), (0.0, 0.0, -0.0), (1.8079, 0.3513, 1.2899), "DV_BP_DM_Mines_Scaffolding_Rail_1M9_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_DM_Mines_Scaffolding_Rail_Corner_2 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (578.9055, 5034.1636, 1142.5139), (0.0, 0.0, -0.0), (1.2324, 1.2413, 0.8534), "DV_BP_DM_Mines_Scaffolding_Rail_Corner_2_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_DM_Mines_Scaffolding_Stairs_2M2_2 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (3511.067, 1991.1719, 3387.8826), (0.0, 0.0, -0.0), (1.5118, 3.0048, 2.2422), "DV_BP_DM_Mines_Scaffolding_Stairs_2M2_2_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_DM_Mines_Scaffolding_Stairs_2M3 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (3361.067, 1991.1719, 3387.8826), (0.0, 0.0, -0.0), (1.5118, 3.0048, 2.2422), "DV_BP_DM_Mines_Scaffolding_Stairs_2M3_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_DM_Mines_Wagon_Broken_B_0 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (3818.8767, 2157.575, 847.76086), (0.0, 0.0, -0.0), (2.6525, 4.4856, 0.6234), "DV_BP_DM_Mines_Wagon_Broken_B_0_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_DM_Mines_Wagon_Broken_B_2 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (4719.986, 2681.8335, 697.76086), (0.0, 0.0, -0.0), (5.1957, 4.7456, 0.6234), "DV_BP_DM_Mines_Wagon_Broken_B_2_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_DM_Warehouse_Crate_B_Breakable_17 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (4322.1987, 573.316, 841.0007), (0.0, 0.0, -0.0), (1.3578, 1.3787, 0.7721), "DV_BP_DM_Warehouse_Crate_B_Breakable_17_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_DM_Warren_Lighting_Torch_Breakable_2 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (5365.7812, 2863.91, 783.8237), (0.0, 0.0, -0.0), (1.2399, 1.1873, 1.9128), "DV_BP_DM_Warren_Lighting_Torch_Breakable_2_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_DM_Warren_Lighting_Torch_Breakable2 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (5137.7812, 1479.9099, 1564.8237), (0.0, 0.0, -0.0), (1.2399, 1.1873, 1.9128), "DV_BP_DM_Warren_Lighting_Torch_Breakable2_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_DM_Warren_Lighting_Torch_Breakable3 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (1910.1047, 4468.736, 1315.8237), (0.0, 0.0, -0.0), (1.2313, 1.2799, 1.9128), "DV_BP_DM_Warren_Lighting_Torch_Breakable3_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_DM_Workshop_Barrel_Breakable4_26 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (5118.4355, 1518.3198, 832.8758), (0.0, 0.0, -0.0), (0.9835, 1.0200, 0.8538), "DV_BP_DM_Workshop_Barrel_Breakable4_26_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_DM_Workshop_Barrel_Breakable5 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (4213.8257, 572.7463, 841.7294), (0.0, 0.0, -0.0), (0.8815, 0.9869, 0.9619), "DV_BP_DM_Workshop_Barrel_Breakable5_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_DM_Workshop_Barrel_Breakable6 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (2769.9421, 1454.3516, 815.83417), (0.0, 0.0, -0.0), (0.9582, 1.0106, 0.9493), "DV_BP_DM_Workshop_Barrel_Breakable6_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_Mines_Ceiling_Brace_A_2 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (951.99927, 3766.5562, 4390.466), (0.0, 0.0, -0.0), (3.1262, 3.1792, 7.9093), "DV_BP_Mines_Ceiling_Brace_A_2_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_Mines_Ceiling_Brace_A2 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (1129.7427, 2684.1768, 4393.301), (0.0, 0.0, -0.0), (3.4077, 3.4672, 7.9093), "DV_BP_Mines_Ceiling_Brace_A2_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_Mines_Ceiling_Brace_A_Bracket_2 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (3864.132, 2040.8904, 1363.5303), (0.0, 0.0, -0.0), (2.1812, 0.6275, 2.2422), "DV_BP_Mines_Ceiling_Brace_A_Bracket_2_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_Mines_Ceiling_Brace_A_Bracket2 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (3864.132, 1961.6189, 1363.5303), (0.0, 0.0, -0.0), (2.1812, 0.6275, 2.2422), "DV_BP_Mines_Ceiling_Brace_A_Bracket2_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_Mines_Ceiling_Brace_A_Bracket3 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (4631.3745, 1961.584, 1363.5303), (0.0, 0.0, -0.0), (2.1812, 0.6275, 2.2422), "DV_BP_Mines_Ceiling_Brace_A_Bracket3_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_Mines_Ceiling_Brace_A_Bracket4 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (4631.375, 2040.8544, 1363.5303), (0.0, 0.0, -0.0), (2.1812, 0.6275, 2.2422), "DV_BP_Mines_Ceiling_Brace_A_Bracket4_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_Mines_Ceiling_Brace_A_Bracket5_9 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (4804.0757, 1961.584, 813.5303), (0.0, 0.0, -0.0), (2.1812, 0.6275, 2.2422), "DV_BP_Mines_Ceiling_Brace_A_Bracket5_9_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_Mines_Ceiling_Brace_A_Bracket6 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (4804.076, 2040.8544, 813.5303), (0.0, 0.0, -0.0), (2.1812, 0.6275, 2.2422), "DV_BP_Mines_Ceiling_Brace_A_Bracket6_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_Mines_Ceiling_Brace_A_Bracket7 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (3703.036, 2040.8904, 882.33234), (0.0, 0.0, -0.0), (2.1812, 0.6275, 2.2422), "DV_BP_Mines_Ceiling_Brace_A_Bracket7_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_Mines_Ceiling_Brace_A_Bracket8 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (3703.036, 1961.6189, 882.33234), (0.0, 0.0, -0.0), (2.1812, 0.6275, 2.2422), "DV_BP_Mines_Ceiling_Brace_A_Bracket8_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_Mines_Scaffoldfing_Support_Bracket_2 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (3588.6152, 4046.4438, 1608.5941), (0.0, 0.0, -0.0), (1.4525, 1.7656, 2.2134), "DV_BP_Mines_Scaffoldfing_Support_Bracket_2_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_Mines_Scaffoldfing_Support_Bracket2 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (2638.6152, 1566.4438, 903.59406), (0.0, 0.0, -0.0), (1.4525, 1.7656, 2.2134), "DV_BP_Mines_Scaffoldfing_Support_Bracket2_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_Mines_Scaffoldfing_Support_Bracket3 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (3728.6152, 4046.4434, 1608.5941), (0.0, 0.0, -0.0), (1.4525, 1.7656, 2.2134), "DV_BP_Mines_Scaffoldfing_Support_Bracket3_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_Mines_Support_Beam_B_2 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (3774.5483, 2040.8749, 1252.1998), (0.0, 0.0, -0.0), (0.2910, 0.3265, 3.0396), "DV_BP_Mines_Support_Beam_B_2_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_Mines_Support_Beam_B10 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (4720.9575, 2040.8702, 652.19946), (0.0, 0.0, -0.0), (0.2910, 0.3265, 3.0396), "DV_BP_Mines_Support_Beam_B10_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_Mines_Support_Beam_B2 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (3774.5483, 2040.8749, 952.1996), (0.0, 0.0, -0.0), (0.2910, 0.3265, 3.0396), "DV_BP_Mines_Support_Beam_B2_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_Mines_Support_Beam_B3 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (3774.5483, 1961.6034, 1252.2), (0.0, 0.0, -0.0), (0.2910, 0.3265, 3.0396), "DV_BP_Mines_Support_Beam_B3_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_Mines_Support_Beam_B4 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (3774.5483, 1961.6034, 952.19946), (0.0, 0.0, -0.0), (0.2910, 0.3265, 3.0396), "DV_BP_Mines_Support_Beam_B4_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_Mines_Support_Beam_B5 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (4720.9575, 1961.5985, 1252.2), (0.0, 0.0, -0.0), (0.2910, 0.3265, 3.0396), "DV_BP_Mines_Support_Beam_B5_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_Mines_Support_Beam_B6 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (4720.9575, 1961.5985, 952.1996), (0.0, 0.0, -0.0), (0.2910, 0.3265, 3.0396), "DV_BP_Mines_Support_Beam_B6_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_Mines_Support_Beam_B7 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (4720.9575, 2040.8702, 1252.2), (0.0, 0.0, -0.0), (0.2910, 0.3265, 3.0396), "DV_BP_Mines_Support_Beam_B7_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_Mines_Support_Beam_B8 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (4720.9575, 2040.8702, 952.19946), (0.0, 0.0, -0.0), (0.2910, 0.3265, 3.0396), "DV_BP_Mines_Support_Beam_B8_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_Mines_Support_Beam_B9 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (4720.9575, 1961.5985, 652.1996), (0.0, 0.0, -0.0), (0.2910, 0.3265, 3.0396), "DV_BP_Mines_Support_Beam_B9_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_Suburbs_Ladder_C_2 (EMorSimpleShape::Empty)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (3310.0002, 1950.0, 1305.0), (0.0, 0.0, -0.0), (2.0000, 2.0000, 2.0000), "DV_BP_Suburbs_Ladder_C_2", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: DecorationBlockingVolume_1 (EMorSimpleShape::Empty)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (4756.074, 3435.7495, 2140.0), (0.0, 14.062650307639597, -0.0), (2.0000, 2.0000, 2.0000), "DV_DecorationBlockingVolume_1", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: DecorationBlockingVolume_2 (EMorSimpleShape::Sphere)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (4112.7964, 1676.745, 3454.011), (-0.0, -45.90542230093919, -0.0), (8.0000, 8.0000, 8.0000), "DV_DecorationBlockingVolume_2", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: DecorationBlockingVolume_3 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (1000.0, 3250.0, 4400.0), (0.0, 5.625095791732844, -0.0), (2.0000, 8.0000, 8.0000), "DV_DecorationBlockingVolume_3", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: DecorationBlockingVolume_4 (EMorSimpleShape::Empty)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (1581.8634, 3624.9219, 3945.0), (0.0, 15.000054069223001, -0.0), (2.0000, 2.0000, 2.0000), "DV_DecorationBlockingVolume_4", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: DecorationBlockingVolume_6 (EMorSimpleShape::Sphere)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (1488.4753, 2978.0935, 4088.3848), (0.0, 0.0, -0.0), (2.0000, 2.0000, 2.0000), "DV_DecorationBlockingVolume_6", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: DecorationBlockingVolume_9 (EMorSimpleShape::Sphere)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (1392.3156, 5406.705, 4084.0664), (0.0, 0.0, -0.0), (2.0000, 2.0000, 2.0000), "DV_DecorationBlockingVolume_9", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: DecorationBlockingVolume_10 (EMorSimpleShape::Empty)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (5380.4653, 2280.0, 4010.0), (0.0, 0.0, -0.0), (2.0000, 2.0000, 2.0000), "DV_DecorationBlockingVolume_10", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: DecorationBlockingVolume_11 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (3200.0, 400.0, 1050.0), (0.0, 0.0, -0.0), (5.0000, 12.0000, 5.0000), "DV_DecorationBlockingVolume_11", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: DecorationBlockingVolume_14 (EMorSimpleShape::Sphere)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (5664.454, 1814.6907, 4120.3813), (0.0, 0.0, -0.0), (2.0000, 2.0000, 2.0000), "DV_DecorationBlockingVolume_14", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: DecorationBlockingVolume_15 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (400.0, 3200.0, 1050.0), (0.0, 0.0, -0.0), (12.0000, 5.0000, 5.0000), "DV_DecorationBlockingVolume_15", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: DecorationBlockingVolume_16 (EMorSimpleShape::Empty)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (2524.595, 4907.3003, 1508.9907), (8.396583976857327, -5.68615717550888, -0.8330076915167512), (2.0000, 2.0000, 2.0000), "DV_DecorationBlockingVolume_16", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: DecorationBlockingVolume_17 (EMorSimpleShape::Sphere)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (3935.3997, 1165.8033, 980.21277), (0.0, 0.0, -0.0), (2.0000, 2.0000, 2.0000), "DV_DecorationBlockingVolume_17", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: DecorationBlockingVolume_18 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (5700.0, 3100.0, 1000.0), (0.0, 0.0, -0.0), (16.0000, 5.0000, 6.0000), "DV_DecorationBlockingVolume_18", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: DecorationBlockingVolume_20 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (6000.0, 3200.0, 4250.0), (0.0, 0.0, -0.0), (12.0000, 5.0000, 5.0000), "DV_DecorationBlockingVolume_20", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: DecorationBlockingVolume10 (EMorSimpleShape::Sphere)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (2087.311, 5582.5967, 4084.0664), (0.0, 0.0, -0.0), (2.0000, 2.0000, 2.0000), "DV_DecorationBlockingVolume10", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: DecorationBlockingVolume12 (EMorSimpleShape::Sphere)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (4606.9336, 5487.7896, 4084.0664), (0.0, 0.0, -0.0), (2.0000, 2.0000, 2.0000), "DV_DecorationBlockingVolume12", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: DecorationBlockingVolume19 (EMorSimpleShape::Sphere)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (1869.8738, 1065.7072, 980.21277), (0.0, 0.0, -0.0), (2.0000, 2.0000, 2.0000), "DV_DecorationBlockingVolume19", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: DecorationBlockingVolume21 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (3200.0, 6000.0, 4250.0), (0.0, 0.0, -0.0), (5.0000, 12.0000, 5.0000), "DV_DecorationBlockingVolume21", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: DecorationBlockingVolume22 (EMorSimpleShape::Sphere)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (2629.491, 1081.0116, 888.7357), (0.0, 0.0, -0.0), (2.0000, 2.0000, 2.0000), "DV_DecorationBlockingVolume22", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: DecorationBlockingVolume23 (EMorSimpleShape::Sphere)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (4547.5127, 1161.9451, 888.7361), (0.0, 0.0, -0.0), (2.0000, 2.0000, 2.0000), "DV_DecorationBlockingVolume23", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: DecorationBlockingVolume24 (EMorSimpleShape::Empty)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (3042.3684, 4931.9834, 1508.9906), (8.396583976857327, -5.68615717550888, -0.8330076915167512), (2.0000, 2.0000, 2.0000), "DV_DecorationBlockingVolume24", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: DecorationBlockingVolume25 (EMorSimpleShape::Empty)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (3530.6506, 4979.2173, 1540.4417), (8.396584312845913, 24.31387558111873, -0.8330078802241054), (2.0000, 2.0000, 2.0000), "DV_DecorationBlockingVolume25", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: DecorationBlockingVolume3 (EMorSimpleShape::Sphere)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (3057.5474, 1849.6509, 3391.7305), (-0.0, -45.90542230093919, -0.0), (8.0000, 8.0000, 8.0000), "DV_DecorationBlockingVolume3", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: DecorationBlockingVolume4 (EMorSimpleShape::Sphere)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (3302.1392, 1454.1677, 3391.7305), (-0.0, -45.90542230093919, -0.0), (8.0000, 8.0000, 8.0000), "DV_DecorationBlockingVolume4", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: DecorationBlockingVolume5 (EMorSimpleShape::Empty)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (5042.1484, 2431.499, 1820.0), (0.0, 2.8127011796441868, -0.0), (2.0000, 2.0000, 2.0000), "DV_DecorationBlockingVolume5", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: DecorationBlockingVolume7 (EMorSimpleShape::Sphere)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (1895.801, 3384.4927, 4102.698), (0.0, 0.0, -0.0), (2.0000, 2.0000, 2.0000), "DV_DecorationBlockingVolume7", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: DecorationBlockingVolume8 (EMorSimpleShape::Empty)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (1889.0005, 2721.0251, 4040.0), (0.0, 15.000017649669042, -0.0), (2.0000, 2.0000, 2.0000), "DV_DecorationBlockingVolume8", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: Mines_Machine_Whim_Side_Support_Beam_Breakable2 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (2712.6445, 2055.0117, 3320.6492), (0.0, 0.0, -0.0), (0.3982, 2.2049, 3.1177), "DV_Mines_Machine_Whim_Side_Support_Beam_Breakable2_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: Mines_Machine_Whim_Side_Support_Beam_Breakable3_1 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (2547.6567, 2130.3933, 3376.1714), (0.0, 0.0, -0.0), (3.1282, 0.4436, 2.1933), "DV_Mines_Machine_Whim_Side_Support_Beam_Breakable3_1_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: Mines_Machine_Whim_Side_Support_Beam_Breakable4_3 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (2531.9536, 2450.009, 3376.1714), (0.0, 0.0, -0.0), (3.1282, 0.4436, 2.1933), "DV_Mines_Machine_Whim_Side_Support_Beam_Breakable4_3_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: Mines_Machine_Whim_Side_Support_Beam_Breakable5 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (3861.2598, 2111.4407, 3320.6492), (0.0, 0.0, -0.0), (0.3982, 2.2049, 3.1177), "DV_Mines_Machine_Whim_Side_Support_Beam_Breakable5_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: Mines_Machine_Whim_Side_Support_Beam_Breakable6 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (3611.5603, 2099.1726, 3320.6492), (0.0, 0.0, -0.0), (0.3982, 2.2049, 3.1177), "DV_Mines_Machine_Whim_Side_Support_Beam_Breakable6_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: Mines_Machine_Whim_Side_Support_Beam_Breakable7 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (3122.1482, 2075.1272, 3320.6492), (0.0, 0.0, -0.0), (0.3982, 2.2049, 3.1177), "DV_Mines_Machine_Whim_Side_Support_Beam_Breakable7_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: RockBlockingVolume10 (EMorSimpleShape::Empty)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (3199.973, 617.0285, 4299.5034), (-0.0, 0.0, 7.79999990514594e-05), (2.0000, 2.0000, 2.0000), "DV_RockBlockingVolume10", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: RockBlockingVolume11 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (400.0, 3200.0, 4300.0), (0.00010245283119049863, -89.99954442867534, 2.926654708076287e-13), (5.0000, 14.0000, 5.0000), "DV_RockBlockingVolume11", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: RockBlockingVolume12 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (3200.0, 6200.0, 1050.0), (-0.0, 0.0, 7.79999990514594e-05), (5.0000, 8.0000, 5.0000), "DV_RockBlockingVolume12", _folder)
if a: placed += 1
else: skipped += 1

# ======================================================================
# SUMMARY
# ======================================================================
unreal.log(f"[{BUBBLE_NAME}] Reconstruction complete: {placed} placed, {skipped} skipped, {errors} errors")
