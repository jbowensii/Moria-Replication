"""Auto-generated level reconstruction script.
Bubble: BD_BB_MiningCamp
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

BUBBLE_NAME = "BD_BB_MiningCamp"
placed = 0
skipped = 0
errors = 0

# ======================================================================
# PHASE 1: InstancedMeshCatalog  (static mesh placement)
# ======================================================================
unreal.log(f"[{BUBBLE_NAME}] Phase 1: Placing static meshes...")

# Batch 0: StaticMesh'Deep_BoneHoard_B' (3 instances)
_mesh_path = "/Game/Art/Assets/Kits/Architecture/Deep/Deep_BoneHoard_B"
_materials = ['/Game/Art/Assets/Kits/Misc/Dirt_Mounds/Materials/MI_Mines_Dirt']
_folder = "Reconstruction/BD_BB_MiningCamp/Meshes"
a = spawn_static_mesh(_mesh_path, _materials, (599.9012, 3941.668, 790.3679), (0.0, -171.54221458275566, 0.0), (1.0, 1.0, 1.0), "Deep_BoneHoard_B_20", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (576.1359, 2805.5024, 789.94446), (0.0, -171.54221458275566, 0.0), (1.0, 1.0, 1.0), "Deep_BoneHoard_B2_23", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5565.3, 1241.4135, 806.1218), (0.958111653609852, -160.82226681183477, -2.752533274325042), (1.0, 1.0, 1.3658043), "Deep_BoneHoard_B3_10", _folder)
if a: placed += 1
else: skipped += 1

# Batch 1: StaticMesh'Dirt_Mound_G' (1 instances)
_mesh_path = "/Game/Art/Assets/Kits/Misc/Dirt_Mounds/Dirt_Mound_G"
_materials = ['/Game/Art/Assets/Kits/Misc/Dirt_Mounds/Materials/MI_Mines_Dirt']
_folder = "Reconstruction/BD_BB_MiningCamp/Meshes"
a = spawn_static_mesh(_mesh_path, _materials, (3070.542, 1642.239, 914.1088), (-2.3527218300561636, -22.15627860895811, -6.504669053682951), (1.0, 1.0, 1.5288645), "Dirt_Mound_G_41", _folder)
if a: placed += 1
else: skipped += 1

# Batch 2: StaticMesh'Dirt_Mound_I' (36 instances)
_mesh_path = "/Game/Art/Assets/Kits/Misc/Dirt_Mounds/Dirt_Mound_I"
_materials = ['/Game/Art/Assets/Kits/Misc/Dirt_Mounds/Materials/MI_Mines_Dirt']
_folder = "Reconstruction/BD_BB_MiningCamp/Meshes"
a = spawn_static_mesh(_mesh_path, _materials, (2625.342, 5586.137, 789.7961), (0.0, -5.829650719103862, 0.0), (1.0, 1.0, 0.45398188), "Dirt_Mound_I_6", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1691.1034, 5109.658, 788.8092), (2.6092119242776874, -179.76319721130318, 0.8140380090949512), (1.0, 1.0, 0.366032), "Dirt_Mound_I16", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1098.8776, 4174.636, 784.5003), (-2.6999818076594324, -26.025693248472948, 0.4240409254978706), (1.0, 1.0, 0.366032), "Dirt_Mound_I17", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1421.1602, 4822.1064, 804.7085), (-2.4625241179300694, -42.817594238015985, 1.1857229908757698), (1.0, 1.0, 0.18614314), "Dirt_Mound_I18_14", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1367.63, 4298.744, 789.40576), (-0.7536620435467583, 3.4820858673200052, -0.6650389801646005), (1.0, 1.0, 0.186143), "Dirt_Mound_I19", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2374.7988, 5277.503, 779.77386), (0.0, -28.04458588271756, 0.0), (1.0, 1.0, 0.453982), "Dirt_Mound_I2", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3644.6685, 5494.5537, 793.67554), (0.0, -169.70374768107746, 0.0), (1.0, 1.0, 0.366032), "Dirt_Mound_I20", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4048.8545, 4666.3286, 793.67554), (0.0, -169.70374768107746, 0.0), (1.0, 1.0, 0.4434416), "Dirt_Mound_I21", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4025.7258, 5165.434, 793.67554), (0.0, -166.49449291475196, 0.0), (1.0, 1.0, 0.31409422), "Dirt_Mound_I22", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3312.8848, 3616.5771, 795.9795), (0.0, -1.713378939388359, 0.0), (1.0, 1.0, 0.5236818), "Dirt_Mound_I23", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3411.7202, 3877.6394, 783.24084), (-2.408972910480304e-10, -13.6818540318763, 0.031325194245907705), (1.0, 1.0, 0.59731954), "Dirt_Mound_I24", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3839.4548, 4235.968, 793.9865), (0.011722867018506366, -35.623168271441635, 0.029049091002915146), (1.0, 1.0, 0.406181), "Dirt_Mound_I25", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2524.7253, 2960.6665, 787.3513), (0.0, -43.76074356781395, 0.0), (1.0, 1.0, 0.3618631), "Dirt_Mound_I26", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1916.1853, 2686.6812, 785.62036), (0.0, -44.7771932136776, 0.0), (1.0, 1.0, 0.361863), "Dirt_Mound_I27", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1208.4425, 2509.8457, 781.7689), (-0.5465393026164227, -90.40267334970969, 0.31683545341925956), (1.0, 1.0, 0.5958682), "Dirt_Mound_I28", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (917.41595, 2610.1113, 785.6918), (-0.5320739651367148, -92.9124868322944, 0.34045430629802304), (1.0, 1.0, 0.47108218), "Dirt_Mound_I29", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1644.2611, 2536.191, 788.06647), (-0.9642638446661282, 16.236728456175143, 1.3446465577845195), (1.0, 1.0, 0.45538557), "Dirt_Mound_I30", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2396.1426, 2828.839, 787.77795), (0.0, -44.7771932136776, 0.0), (1.0, 1.0, 0.6327117), "Dirt_Mound_I31", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2120.1663, 2938.3992, 779.88684), (1.0626955062966044, 107.33307799950113, 1.0713051134675955), (1.0, 1.0, 0.17948073), "Dirt_Mound_I32", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2136.2056, 5176.666, 793.29736), (0.5223113146127373, 124.37673248844965, 0.3572848253148249), (1.0, 1.0, 0.21380396), "Dirt_Mound_I33", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2842.9727, 2936.5093, 797.0009), (0.0, -97.5296634418805, 0.0), (1.0, 1.0, 0.361863), "Dirt_Mound_I34", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3132.2708, 2581.5347, 793.19836), (0.0, 37.86550322256814, -0.0), (1.0, 1.0, 0.361863), "Dirt_Mound_I35", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3273.705, 1840.6658, 791.21356), (-0.2618713365967667, 175.2986913849915, -0.40240475912802104), (1.0, 1.0, 0.43375233), "Dirt_Mound_I36", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3045.0908, 1372.6387, 791.21356), (-0.5823363757299026, 152.686687605816, -0.07260128432209319), (1.0, 1.0, 0.433752), "Dirt_Mound_I37", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2451.166, 900.4624, 788.62976), (-0.2619018111966372, 149.0700301895179, -0.4024047300148161), (1.0, 1.0, 0.433752), "Dirt_Mound_I38", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2864.0178, 1144.5273, 795.75336), (-0.2619018111966372, 149.0700301895179, -0.4024047300148161), (1.0, 1.0, 0.433752), "Dirt_Mound_I39", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2109.6565, 772.6707, 791.3112), (-0.2619018111966372, 149.0700301895179, -0.4024047300148161), (1.0, 1.0, 0.433752), "Dirt_Mound_I40", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1730.5874, 640.8369, 791.3111), (-0.2617187641973644, -54.6060206352736, -0.4024048002674927), (1.0, 1.0, 1.0), "Dirt_Mound_I41", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4725.5347, 2653.8728, 791.90106), (-0.9160764474069042, 175.29508145299704, 0.41340091705879634), (1.0, 1.0, 0.433752), "Dirt_Mound_I42", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5063.6675, 3043.7522, 800.36725), (0.22487711371069874, -150.457131398663, 1.060128194528371), (1.0, 1.0, 0.29385754), "Dirt_Mound_I43", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5411.676, 3379.4807, 790.2526), (0.2190797433471606, -0.34957883141924434, 0.11060320019837468), (1.0, 1.0, 0.293858), "Dirt_Mound_I44", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5720.7095, 3735.8071, 790.25275), (0.21907998122974875, 160.99452126345668, 0.11060300070932554), (1.0, 1.0, 0.293858), "Dirt_Mound_I45", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1372.3037, 418.89612, 791.3111), (-0.26171871992149237, -29.6060186720345, -0.4024047429308183), (1.0, 1.0, 1.0), "Dirt_Mound_I46", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5225.1885, 526.9717, 797.123), (-0.26171870447376133, 16.86840124799911, -0.4024047588689018), (1.0, 1.0, 0.433752), "Dirt_Mound_I47", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5225.1885, 881.8828, 797.123), (-0.2617187468664509, 3.5987632247820334, -0.40240477907247657), (1.0, 1.0, 0.433752), "Dirt_Mound_I48", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3430.079, 2877.2124, 800.4883), (0.0, -97.5296634418805, 0.0), (1.0, 1.0, 0.21156439), "Dirt_Mound_I49", _folder)
if a: placed += 1
else: skipped += 1

# Batch 3: StaticMesh'Suburbs_Dirt_Mound_Flat_D' (2 instances)
_mesh_path = "/Game/Art/Assets/Kits/Misc/Dirt_Mounds/Suburbs_Dirt_Mound_Flat_D"
_materials = ['/Game/Art/Assets/Kits/Misc/Dirt_Mounds/Materials/MI_DirtMound_Mines']
_folder = "Reconstruction/BD_BB_MiningCamp/Meshes"
a = spawn_static_mesh(_mesh_path, _materials, (5741.5107, 3982.698, 793.99347), (0.0, 154.1757430123612, -0.0), (2.421363, 2.421363, 2.277266), "Suburbs_Dirt_Mound_Flat_D2_158", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2037.5073, 726.29016, 847.31366), (0.0, -165.41943361944013, -0.0), (4.0, 4.0, 2.315972), "Suburbs_Dirt_Mound_Flat_D3_163", _folder)
if a: placed += 1
else: skipped += 1

# Batch 4: StaticMesh'SM_Bubble_MiningCamp_Floor' (1 instances)
_mesh_path = "/Game/LevelDesign/GuideMeshes/Generic/MiningCamp/SM_Bubble_MiningCamp_Floor"
_materials = ['/Game/Environments/ProcTexturing/GuideMeshFloor/M_GuideMeshFloor_Mines']
_folder = "Reconstruction/BD_BB_MiningCamp/Meshes"
a = spawn_static_mesh(_mesh_path, _materials, (0.0, 0.0, 0.0), (0.0, 0.0, -0.0), (1.0, 1.0, 1.0), "SM_Bubble_MiningCamp_Floor_2", _folder)
if a: placed += 1
else: skipped += 1

# Batch 5: StaticMesh'SM_Bubble_MiningCamp_Walls' (1 instances)
_mesh_path = "/Game/LevelDesign/GuideMeshes/Generic/MiningCamp/SM_Bubble_MiningCamp_Walls"
_materials = ['/Game/Environments/ProcTexturing/GuideMeshFloor/MI_GuideMeshFloor_Cave']
_folder = "Reconstruction/BD_BB_MiningCamp/Meshes"
a = spawn_static_mesh(_mesh_path, _materials, (0.0, 0.0, 0.0), (0.0, 0.0, -0.0), (1.0, 1.0, 1.0), "SM_Bubble_MiningCamp_Walls_5", _folder)
if a: placed += 1
else: skipped += 1

# Batch 6: StaticMesh'PWM_Quarry_1x1x1_A' (2 instances)
_mesh_path = "/Game/Unshippable/Whitebox/Rocks/Meshes/PWM_Quarry_1x1x1_A"
_materials = ['/Game/Environments/ProcTexturing/ProcMaterial_Quarry_Atlas_1']
_folder = "Reconstruction/BD_BB_MiningCamp/Meshes"
a = spawn_static_mesh(_mesh_path, _materials, (2376.5334, 1212.2313, 1102.4396), (0.0, -134.66762884558273, 0.0), (1.0, 1.0, 2.0664546), "PWM_Quarry_1x1x1_A_683", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3661.7803, 5311.5137, 767.5448), (0.0, 0.0, -0.0), (1.0, 1.0, 1.0), "PWM_Quarry_1x1x1_A2_2", _folder)
if a: placed += 1
else: skipped += 1

# Batch 7: StaticMesh'PWM_Quarry_1X1x1_C' (14 instances)
_mesh_path = "/Game/Unshippable/Whitebox/Rocks/Meshes/PWM_Quarry_1X1x1_C"
_materials = ['/Game/Environments/ProcTexturing/ProcMaterial_Quarry_Atlas_1']
_folder = "Reconstruction/BD_BB_MiningCamp/Meshes"
a = spawn_static_mesh(_mesh_path, _materials, (2220.2737, 2609.7073, 905.766), (2.6648796696857597, -69.39570155897485, -7.88824521589577), (1.6877111, 2.3760877, 1.0), "PWM_Quarry_1X1x1_C_63", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4197.675, 4360.499, 816.94836), (-1.4896545750670787, -42.28402523050596, -9.67092735644508), (1.687711, 3.469925, 1.0), "PWM_Quarry_1X1x1_C10_62", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5694.0586, 4330.8965, 812.8552), (-0.12759395637745022, 147.85088974356617, 13.96112413713712), (1.687711, 3.469925, 1.5039204), "PWM_Quarry_1X1x1_C11", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4059.7563, 5457.3354, 921.3257), (-10.54934649298648, -156.62400139725403, 12.650285475491478), (1.687711, 3.469925, 1.0), "PWM_Quarry_1X1x1_C12_131", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5446.514, 4049.9324, 778.707), (-0.8085018251532723, 151.00861133894676, 16.603490590960337), (1.687711, 3.469925, 0.93193454), "PWM_Quarry_1X1x1_C13", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (240.60382, 3855.6921, 818.21497), (0.0, -27.602752001098494, 0.0), (1.0, 1.0, 1.0), "PWM_Quarry_1X1x1_C14_30", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2528.7598, 2751.8696, 911.9418), (2.6648806323864322, -69.39560592193972, -10.765839786817528), (1.687711, 2.227891, 1.0), "PWM_Quarry_1X1x1_C2", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2337.0908, 2454.3125, 1445.9014), (5.673951094421296, -52.67040105188481, -9.54208174279343), (1.687711, 3.475439, 1.0), "PWM_Quarry_1X1x1_C3", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3510.684, 3609.0994, 840.79803), (6.542556946077938, -51.372647069424985, -9.975586208400523), (1.687711, 2.227891, 1.0), "PWM_Quarry_1X1x1_C4", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3789.5774, 3768.212, 841.7168), (3.16518494649237, -63.93069174327336, -11.97277916726017), (2.124958, 2.6651375, 1.4372485), "PWM_Quarry_1X1x1_C5", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2895.724, 5857.2583, 808.3026), (-14.83168478117345, 95.81009437959004, -80.41731871518456), (1.0, 1.0, 1.0), "PWM_Quarry_1X1x1_C6_26", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3466.0745, 6017.865, 760.16455), (-14.831603700088168, 95.81013688404288, -17.523923202055705), (1.0, 1.0, 1.0), "PWM_Quarry_1X1x1_C7", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3875.7244, 4105.845, 751.8016), (-2.0592955850362338, -45.467035175726565, -10.108794792137363), (1.687711, 3.4699247, 1.0), "PWM_Quarry_1X1x1_C8", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4086.0293, 4578.78, 774.18463), (-2.934356723975287, -45.562589526329745, -10.968293245730862), (1.687711, 3.469925, 1.0), "PWM_Quarry_1X1x1_C9", _folder)
if a: placed += 1
else: skipped += 1

# Batch 8: StaticMesh'PWM_Quarry_2x2x2_A' (84 instances)
_mesh_path = "/Game/Unshippable/Whitebox/Rocks/Meshes/PWM_Quarry_2x2x2_A"
_materials = ['/Game/Environments/ProcTexturing/ProcMaterial_Quarry_Atlas_1']
_folder = "Reconstruction/BD_BB_MiningCamp/Meshes"
a = spawn_static_mesh(_mesh_path, _materials, (3959.9812, 2806.7114, 1452.1566), (11.769740006589174, 24.342491511923665, -12.017486504936462), (1.263285, 1.263285, 1.263285), "PWM_Quarry_2x2x2_A_473", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (779.6362, 2402.2432, 855.024), (-6.034758680988592, -99.30071158944126, -6.25552293278207), (1.058841, 2.727849, 1.058841), "PWM_Quarry_2x2x2_A10", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (460.65448, 2714.96, 710.49304), (-6.575255262851016, -120.82820329840858, -3.829344921371896), (1.058841, 2.727849, 1.058841), "PWM_Quarry_2x2x2_A11", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (631.2886, 2564.4463, 791.8632), (-0.7662045378365637, -118.96758414013101, -9.118377910783494), (1.058841, 2.727849, 1.058841), "PWM_Quarry_2x2x2_A12", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1542.7485, 2465.784, 721.84973), (-1.5369570675535205, -67.07418413230506, -11.83822592051171), (1.058841, 2.727849, 1.058841), "PWM_Quarry_2x2x2_A13", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1107.3105, 2512.18, 681.0729), (-7.274841881273204, -93.60424105160706, -9.086518313401967), (1.058841, 2.727849, 1.058841), "PWM_Quarry_2x2x2_A14", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3718.9236, 3359.0244, 1659.8081), (-7.98730369950786, 127.16805587641372, -168.3605886917963), (1.058841, 2.2772481, 1.058841), "PWM_Quarry_2x2x2_A15", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3416.3315, 3634.962, 722.8283), (0.07926426876195049, -51.15908638788239, -2.8580016063571896), (1.058841, 2.727849, 1.058841), "PWM_Quarry_2x2x2_A16", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3588.7988, 3830.79, 755.37854), (-0.8558045202883943, -53.38482673167213, -2.87667856395613), (1.058841, 2.727849, 1.058841), "PWM_Quarry_2x2x2_A17", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4009.4006, 4113.382, 741.8105), (-0.3857116485303403, -58.06170189628354, -1.688232306017895), (1.058841, 2.727849, 1.058841), "PWM_Quarry_2x2x2_A18", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2684.2458, 2963.683, 712.6771), (-3.0468441002421893, -77.88005732465378, -3.8924253295986206), (1.058841, 2.727849, 1.058841), "PWM_Quarry_2x2x2_A19", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1913.7717, 2526.2927, 817.82135), (-3.4306028013455956, -74.01007034148401, -5.411010434667351), (1.1452216, 2.3636003, 1.058841), "PWM_Quarry_2x2x2_A2_58", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3698.3145, 5471.6284, 705.9155), (4.665169178707253, 171.58555581837868, 9.785228666720586), (1.058841, 2.727849, 1.058841), "PWM_Quarry_2x2x2_A20", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (270.3342, 4002.8276, 634.76654), (-4.815307948846764, 96.04923915038873, 17.91099920033277), (1.058841, 2.727849, 1.058841), "PWM_Quarry_2x2x2_A21", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (569.5309, 4199.648, 767.72375), (10.216255510912502, 86.01622684005703, 12.461767534848931), (1.058841, 2.727849, 1.058841), "PWM_Quarry_2x2x2_A22", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1963.5187, 2357.7073, 2236.4756), (70.17644672063622, 161.4910109536666, -56.605582865825085), (0.75, 0.75, 2.243998), "PWM_Quarry_2x2x2_A224", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2277.5251, 2623.582, 2357.749), (-70.473694363875, -2.3837290242778204, 40.633994801639815), (0.830254, 0.75, 2.563804), "PWM_Quarry_2x2x2_A225_605", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (510.19257, 4232.5186, 842.1881), (8.944493915372119, 88.65796298671826, 10.003770519774623), (1.058841, 2.727849, 1.058841), "PWM_Quarry_2x2x2_A23", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (269.48993, 4099.5454, 724.239), (-1.5385742185725206, 77.80712719327376, -0.9990537667278199), (1.058841, 2.727849, 1.058841), "PWM_Quarry_2x2x2_A24", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (350.4275, 2302.6707, 1062.8159), (-0.7661134492508093, -118.96757921050346, -10.945251953334555), (1.058841, 2.727849, 1.058841), "PWM_Quarry_2x2x2_A25", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3042.035, 2350.5146, 1637.1852), (12.511560408887638, 47.51452448814605, 178.38303577985616), (1.263285, 1.3631464, 1.263285), "PWM_Quarry_2x2x2_A26_477", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4080.7285, 2652.0935, 784.20776), (1.4979696293381992, 49.359663469635585, 6.398423056991765), (1.058841, 2.727849, 1.058841), "PWM_Quarry_2x2x2_A27_352", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (6164.7134, 5038.7905, 2199.4885), (14.630428816857549, 49.27367794865179, -176.1957324172768), (2.0092046, 1.0, 1.0), "PWM_Quarry_2x2x2_A28_649", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1945.5076, 1150.2307, 1408.2097), (-6.09579435207404, -61.54485583999574, -13.065520960157244), (1.0, 2.4520686, 1.0), "PWM_Quarry_2x2x2_A29_547", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2088.3276, 2689.2554, 769.53503), (-3.4305718978031585, -73.81078159168467, -5.411040349528479), (1.058841, 2.727849, 1.058841), "PWM_Quarry_2x2x2_A3", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2758.8164, 1220.3171, 746.83185), (-2.8937072650970728, -53.551151393658955, -5.902130583976472), (1.058841, 2.727849, 1.058841), "PWM_Quarry_2x2x2_A30_392", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2512.6484, 1251.1942, 760.24475), (-0.9118340881749277, -65.88232023015291, 167.1248971773513), (1.058841, 2.727849, 1.058841), "PWM_Quarry_2x2x2_A31_394", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3032.0054, 2351.1257, 1432.8661), (-2.1243291616333644, -44.6032689067388, 167.55925272133388), (1.3305626, 1.263285, 1.263285), "PWM_Quarry_2x2x2_A32_479", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2876.6633, 2009.01, 1349.3645), (13.349949326096803, 36.7291271318477, -3.2519530351833295), (1.5664523, 1.263285, 0.987711), "PWM_Quarry_2x2x2_A33_503", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3798.131, 2640.0212, 795.74445), (-3.0831600795991148, -145.3979508182536, -5.805755082067726), (1.058841, 2.727849, 1.058841), "PWM_Quarry_2x2x2_A34_541", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2068.1982, 1189.3956, 1315.735), (4.314110971560599, 126.99171972848389, 13.079282867615179), (1.0, 2.7283907, 1.0580325), "PWM_Quarry_2x2x2_A35_549", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4335.677, 2868.3562, 1846.4222), (-12.093139612408098, -153.71041717892948, -159.50009153359537), (1.263285, 1.263285, 1.263285), "PWM_Quarry_2x2x2_A36_559", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4436.865, 2995.4778, 1626.3926), (12.655466117040389, 27.843202853426984, 159.83294403851176), (1.263285, 1.263285, 1.263285), "PWM_Quarry_2x2x2_A37_561", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4261.91, 2903.0747, 1581.9681), (9.813293474250841, 6.9589837159772205, 156.61340082194891), (1.263285, 1.263285, 1.263285), "PWM_Quarry_2x2x2_A38_563", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4126.5005, 2838.951, 1754.172), (9.813293474250841, 6.9589837159772205, 156.61340082194891), (1.263285, 1.263285, 1.6683388), "PWM_Quarry_2x2x2_A39", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2423.673, 2797.7246, 765.4384), (7.175993829728548, 105.06376806309679, 7.2815375336145465), (1.058841, 2.727849, 1.058841), "PWM_Quarry_2x2x2_A4", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3686.4863, 2808.4412, 1681.9132), (15.959935638853745, 9.887389256136, 169.95961253104255), (1.263285, 1.4652513, 1.9702584), "PWM_Quarry_2x2x2_A40", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3296.8225, 2569.655, 1818.4146), (12.511560408887638, 47.51452448814605, 178.38303577985616), (2.235873, 1.263285, 1.263285), "PWM_Quarry_2x2x2_A41", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2672.0854, 1987.2158, 2284.664), (13.354279979343818, 47.48931487615286, 178.37758467687993), (2.235873, 1.263285, 1.263285), "PWM_Quarry_2x2x2_A42", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2097.664, 1285.8418, 1447.0898), (14.152565127845792, 32.578246355039276, -1.1233512815764781), (1.566452, 1.263285, 0.987711), "PWM_Quarry_2x2x2_A43", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1857.2338, 1051.2145, 1187.8524), (0.44465075830145934, -60.69927108598851, -11.99786256668745), (1.058841, 2.727849, 1.058841), "PWM_Quarry_2x2x2_A44", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (725.5353, 491.26233, 1801.9541), (12.742145605489771, 93.2969686956938, 167.26308024126305), (1.263285, 1.263285, 1.263285), "PWM_Quarry_2x2x2_A45", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (743.5587, 178.26929, 2251.2493), (10.596982346133876, 72.33043951059769, 171.53744199865872), (1.263285, 1.263285, 1.263285), "PWM_Quarry_2x2x2_A46", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (763.05927, 160.55222, 1567.0383), (7.023481399992739, -19.60604428613066, 168.9998317358802), (1.0446819, 1.263285, 1.263285), "PWM_Quarry_2x2x2_A47", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5647.661, 4375.676, 2222.15), (15.941426650109333, 42.699839867875625, 171.20336067870375), (2.009205, 1.0, 1.0), "PWM_Quarry_2x2x2_A48", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2177.6182, 901.07007, 760.34), (-2.8937072650970728, -53.551151393658955, -5.902130583976472), (1.058841, 2.727849, 1.058841), "PWM_Quarry_2x2x2_A49", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1618.696, 1933.7064, 1011.8382), (2.5191570197439965, -22.754608591325084, -9.318145858920445), (1.058841, 2.727849, 1.058841), "PWM_Quarry_2x2x2_A5", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (968.48126, 2361.0974, 739.0711), (-2.1797487503842197, -110.96271020253268, -8.846557946918141), (1.058841, 2.727849, 0.7760118), "PWM_Quarry_2x2x2_A50_12", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5509.402, 411.07132, 956.62384), (4.7395073656182864, -68.40960308810972, 164.00939900443942), (2.2523644, 1.5923889, 1.5923889), "PWM_Quarry_2x2x2_A51", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3738.566, 3133.903, 1577.9896), (8.710240038638647, -1.9493711060169943, -19.86748946279952), (1.263285, 1.263285, 1.263285), "PWM_Quarry_2x2x2_A52", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3783.1113, 2965.9282, 1484.522), (7.807151129408955, 133.48063211374162, 14.878023113293546), (1.263285, 1.263285, 1.263285), "PWM_Quarry_2x2x2_A53", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5648.3853, 824.0711, 1409.9617), (13.579422987078882, 12.24639762922515, -1.463531428416481), (1.92326, 1.263285, 1.3824997), "PWM_Quarry_2x2x2_A54", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (6179.1274, 790.0878, 1465.9421), (-17.009579877226667, 177.46014938728237, 2.132507132764974), (1.2558407, 1.2558407, 1.78013), "PWM_Quarry_2x2x2_A55", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (6347.367, 885.8611, 1039.958), (-13.48641874250835, 177.59509820352432, 2.096984932568269), (1.0, 1.0, 1.0), "PWM_Quarry_2x2x2_A56", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (6322.178, 846.6816, 1138.0619), (-13.48641874250835, 177.59509820352432, 2.096984932568269), (1.0, 1.0, 1.0), "PWM_Quarry_2x2x2_A57", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (6272.341, 814.0783, 1339.9008), (-5.718384138935728, -107.83972251111557, -9.727722196279103), (1.0, 1.0, 1.0), "PWM_Quarry_2x2x2_A58", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (6255.904, 772.2226, 1708.6608), (-0.7568670819126916, 80.52582427485655, 14.106323035604095), (1.0, 1.0, 1.2308533), "PWM_Quarry_2x2x2_A59", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4112.359, 4469.026, 689.8707), (1.6689487403607033, 122.9273847418428, 5.549460230753343), (1.058841, 2.727849, 1.058841), "PWM_Quarry_2x2x2_A6", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5637.0767, 648.8261, 1601.2943), (-11.98434168194071, -167.7088048148306, -178.54541008315869), (1.92326, 1.263285, 1.3825), "PWM_Quarry_2x2x2_A60", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5613.9805, 667.3445, 1923.4329), (-10.85567993891838, -134.47070053009824, 173.73370242005677), (1.92326, 1.263285, 1.3825), "PWM_Quarry_2x2x2_A61", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5574.378, 221.96555, 1915.0095), (0.9032051335604713, 96.42333645009094, 11.672180314705383), (1.4474564, 1.263285, 1.3825), "PWM_Quarry_2x2x2_A62", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3579.898, 3056.4417, 1771.938), (-4.255554716416777, -36.975861463079475, 159.02502887434713), (1.263285, 1.263285, 1.263285), "PWM_Quarry_2x2x2_A63", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2972.5166, 2476.25, 1211.8253), (0.5244080140212491, -54.72893739549906, 173.30834856195796), (1.263285, 1.263285, 1.263285), "PWM_Quarry_2x2x2_A64", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2917.2659, 2536.667, 1447.1174), (-0.6659545868950398, -44.762567792576796, 173.76565347941056), (1.330563, 1.263285, 1.263285), "PWM_Quarry_2x2x2_A65_205", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1763.9348, 5274.1694, 799.88934), (-2.798157384257817, 116.35024638804731, 10.885929190561388), (1.058841, 2.727849, 1.058841), "PWM_Quarry_2x2x2_A66", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1304.3259, 4960.977, 792.64655), (-3.115539153758913, 118.00900613739347, 10.800895511420471), (1.058841, 2.727849, 1.058841), "PWM_Quarry_2x2x2_A67", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1547.4863, 5281.0845, 830.7791), (-3.3495781986878117, 118.00292498736275, -169.9716253850471), (1.058841, 2.727849, 0.9429688), "PWM_Quarry_2x2x2_A68", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5235.0195, 3332.095, 707.9579), (0.040796678020159384, -27.16564694733862, -6.5716849046652115), (1.058841, 2.727849, 1.058841), "PWM_Quarry_2x2x2_A69", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3952.436, 2763.2815, 1744.642), (-11.677488339816914, -156.8060561659678, -171.87509637064346), (1.4612786, 1.263285, 1.6133577), "PWM_Quarry_2x2x2_A7_475", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4771.195, 4322.702, 1506.014), (0.0, 148.06463506174453, -0.0), (1.6070055, 1.0, 2.3500981), "PWM_Quarry_2x2x2_A70_24", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4781.582, 4194.8535, 1224.2245), (-4.196380667571014, 97.83189989315552, 0.6848702924580433), (1.607005, 1.6503712, 1.5192739), "PWM_Quarry_2x2x2_A71", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4599.1235, 4280.1724, 1214.1716), (-2.120910450647994, 46.98771323420309, 3.6858256107619205), (0.9894631, 1.4033847, 1.2722877), "PWM_Quarry_2x2x2_A72", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1724.1067, 5617.8467, 1868.292), (-1.272033606885203, -14.731140408049646, -16.65765473130257), (1.7433863, 1.2436053, 1.7338028), "PWM_Quarry_2x2x2_A73_59", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1025.1483, 2165.8257, 1703.5583), (0.0, 0.0, 13.229381144281701), (1.2177283, 1.3597867, 1.0), "PWM_Quarry_2x2x2_A74_71", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (857.7045, 1772.0756, 1581.8203), (0.0, -7.7971803106013935, 0.0), (1.0, 2.2212644, 1.0), "PWM_Quarry_2x2x2_A75_79", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (912.7383, 2104.0964, 1562.2844), (2.851554487872608, -16.308439307142883, 177.96106004097632), (1.0, 1.4488772, 1.0), "PWM_Quarry_2x2x2_A76_82", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3656.2566, 2615.719, 1841.6472), (10.09360595427002, 16.97198529441696, 158.63160651841443), (1.5793703, 1.263285, 1.668339), "PWM_Quarry_2x2x2_A77", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1956.3214, 1952.5824, 1990.7543), (8.95088903041395, 128.78032469273103, 1.6338878514774245e-05), (1.0, 1.0, 1.0), "PWM_Quarry_2x2x2_A78_87", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2513.4053, 1666.0842, 1304.9167), (-4.965056860909822, -133.58200725582978, -4.849914433902468), (1.795306, 1.0, 1.0), "PWM_Quarry_2x2x2_A79_97", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3615.6838, 6021.757, 740.94006), (6.017874122082538, 163.396215837281, 9.020638264062798), (1.058841, 2.727849, 1.058841), "PWM_Quarry_2x2x2_A8", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4009.1519, 2430.659, 765.6241), (2.843680727671023, 16.76886308571698, -2.565612580431699), (1.0, 1.0, 1.0), "PWM_Quarry_2x2x2_A80_123", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3138.131, 1630.0212, 795.74445), (-3.0831602851050737, -10.397979940929988, -5.80575518564038), (1.058841, 2.727849, 1.058841), "PWM_Quarry_2x2x2_A81", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (233.1296, 2827.4746, 749.10693), (8.453062645025586, -18.943450815456952, -2.8883059845039543), (1.0, 1.0, 1.0), "PWM_Quarry_2x2x2_A82_33", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (820.02814, 2525.3013, 733.5395), (-6.491638434800542, -107.04518903411802, -2.9672850663445174), (1.058841, 2.727849, 1.058841), "PWM_Quarry_2x2x2_A9", _folder)
if a: placed += 1
else: skipped += 1

# Batch 9: StaticMesh'PWM_Quarry_2x2x5_A' (20 instances)
_mesh_path = "/Game/Unshippable/Whitebox/Rocks/Meshes/PWM_Quarry_2x2x5_A"
_materials = ['/Game/Environments/ProcTexturing/ProcMaterial_Quarry_Atlas_2']
_folder = "Reconstruction/BD_BB_MiningCamp/Meshes"
a = spawn_static_mesh(_mesh_path, _materials, (4593.7617, 4685.4326, 1552.0347), (0.5579239077966998, -0.6633300482884661, -4.710967731059967), (2.1699958, 2.1699958, 2.1699958), "PWM_Quarry_2x2x5_A_41", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2601.489, 2624.7212, 1841.1991), (-11.137693806947205, 157.89676511709604, -171.01584790417851), (1.2604265, 1.2604265, 1.2604265), "PWM_Quarry_2x2x5_A10", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2181.4705, 1293.6583, 1694.7969), (-5.530059470162289, -38.35802733237101, 167.1547286350166), (1.7948973, 1.7948973, 1.7948973), "PWM_Quarry_2x2x5_A11_446", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2901.9448, 2206.5913, 1779.8674), (2.7944152827647906, -33.30526813715052, 165.20010935043106), (2.1187317, 2.1187317, 2.1187317), "PWM_Quarry_2x2x5_A12_481", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4399.6216, 3037.4397, 1749.7393), (0.958855760084273, 131.10655943167066, 18.62143665874934), (2.169996, 2.169996, 2.169996), "PWM_Quarry_2x2x5_A13", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4511.767, 3141.4219, 1532.491), (2.6397176205022657, -8.967437295093719, 164.4547749824009), (2.4198973, 2.4198973, 2.4198973), "PWM_Quarry_2x2x5_A14", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5217.7812, 4262.175, 1894.6234), (6.963814438975187, 135.88752997913, -160.98291548028186), (2.419897, 2.419897, 2.419897), "PWM_Quarry_2x2x5_A15", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (63.081146, 4249.8516, 1524.9247), (16.925404643045457, 92.30643225380558, 3.0991783737705307), (2.0166225, 2.169996, 2.169996), "PWM_Quarry_2x2x5_A16", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5125.7505, 5424.666, 1384.7915), (0.0, 146.4194390928596, -0.0), (2.1280732, 2.1280732, 2.1280732), "PWM_Quarry_2x2x5_A17_9", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4133.8467, 3804.9148, 1232.1177), (49.20464329497775, 35.79385434072139, -30.252928399496664), (1.2906594, 1.2906594, 1.2906594), "PWM_Quarry_2x2x5_A18_21", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2290.2285, 1794.8333, 1417.9617), (77.59678153916984, -142.67061483167365, -74.45998377440635), (1.3353655, 1.3353655, 1.3353655), "PWM_Quarry_2x2x5_A19_94", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2794.6147, 2668.2207, 1172.1605), (1.7727678091936645, 80.22138788989449, 13.976673640613594), (1.496599, 1.496599, 1.496599), "PWM_Quarry_2x2x5_A2_88", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3574.6636, 3199.6614, 1551.4005), (-17.476899344469917, -119.58123882473554, -10.844146942040346), (1.496599, 1.496599, 1.496599), "PWM_Quarry_2x2x5_A3", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4071.4653, 5633.8223, 1544.4955), (0.0, 0.0, -8.022278115243672), (2.169996, 2.169996, 2.169996), "PWM_Quarry_2x2x5_A4", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2329.5823, 5736.8237, 1551.3434), (1.1154517945874534, -0.15719603966085474, -8.024108002791946), (2.169996, 2.169996, 2.169996), "PWM_Quarry_2x2x5_A5", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2424.694, 2605.0593, 2145.357), (-42.286592187824425, -134.47170137169644, 154.27744720494138), (1.0, 1.0, 1.0), "PWM_Quarry_2x2x5_A56", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2048.9797, 5522.5425, 1413.1013), (-8.788970228348765, -115.75511987091667, -1.5322570364297223), (2.169996, 2.169996, 2.169996), "PWM_Quarry_2x2x5_A6", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (811.2707, 4821.8735, 1413.5454), (14.130724692911869, 39.294522355022906, -12.646881457802081), (2.169996, 2.169996, 2.169996), "PWM_Quarry_2x2x5_A7", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (180.27486, 2481.3545, 1493.432), (1.0128010089729762, 48.25893140116762, 14.268032310716041), (2.169996, 2.169996, 2.169996), "PWM_Quarry_2x2x5_A8", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (693.80634, 4333.798, 1696.425), (-18.92831651422244, -49.83874900428616, -15.217101287525999), (2.169996, 2.169996, 2.169996), "PWM_Quarry_2x2x5_A9", _folder)
if a: placed += 1
else: skipped += 1

# Batch 10: StaticMesh'PWM_Quarry_2x2x5_B' (7 instances)
_mesh_path = "/Game/Unshippable/Whitebox/Rocks/Meshes/PWM_Quarry_2x2x5_B"
_materials = ['/Game/Environments/ProcTexturing/ProcMaterial_Quarry_Atlas_2']
_folder = "Reconstruction/BD_BB_MiningCamp/Meshes"
a = spawn_static_mesh(_mesh_path, _materials, (988.17786, 5737.1753, 1335.4296), (-5.7413328341547665, -131.41663870791928, -6.4693600072915105), (1.849651, 1.849651, 1.849651), "PWM_Quarry_2x2x5_B_45", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (968.8295, 1254.0355, 1292.8762), (-1.3616023490111102e-07, 140.09743610357552, -6.394591883620167), (3.038508, 1.8349377, 3.038508), "PWM_Quarry_2x2x5_B2_62", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1890.8132, 2231.3909, 1675.0502), (23.47729226012967, 50.971372995578314, 12.207178993843284), (1.0, 1.0, 1.0), "PWM_Quarry_2x2x5_B20_594", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3952.0947, 3639.9238, 1331.3643), (22.36969101950492, 50.883571640935955, 4.209820567595538), (1.2925979, 1.2925979, 1.2925979), "PWM_Quarry_2x2x5_B21", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4610.285, 4375.567, 1707.5457), (23.47728978050284, 50.97209291728283, 4.244440577152104), (1.292598, 1.292598, 1.292598), "PWM_Quarry_2x2x5_B22", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4567.8813, 4517.8643, 1443.2456), (17.557227199363837, 50.97595067123042, 2.397572827192887), (1.7966028, 1.7966028, 1.7966028), "PWM_Quarry_2x2x5_B23", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1015.94653, 2027.7094, 1108.3748), (3.2635323079857383, 75.62904067017851, 12.826787673229264), (1.7784364, 1.1501232, 1.7784364), "PWM_Quarry_2x2x5_B3", _folder)
if a: placed += 1
else: skipped += 1

# Batch 11: StaticMesh'PWM_Quarry_4x4x4_A' (118 instances)
_mesh_path = "/Game/Unshippable/Whitebox/Rocks/Meshes/PWM_Quarry_4x4x4_A"
_materials = ['/Game/Environments/ProcTexturing/ProcMaterial_Quarry_Atlas_2']
_folder = "Reconstruction/BD_BB_MiningCamp/Meshes"
a = spawn_static_mesh(_mesh_path, _materials, (4567.7812, 4844.349, 700.4505), (-9.375976444968598, -59.875486758490744, -10.516998703575801), (1.2076848, 1.4695374, 1.2076848), "PWM_Quarry_4x4x4_A_38", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3871.103, 5692.8066, 540.3536), (-3.0006410568932935, -41.69122151761668, -5.426544285783298), (1.207685, 1.469537, 1.207685), "PWM_Quarry_4x4x4_A10_123", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4228.255, 3395.9478, 1721.4576), (-11.596892699901755, -123.52007205347724, -0.5200500279291179), (0.513816, 1.129108, 1.4935316), "PWM_Quarry_4x4x4_A100", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (224.52876, 4371.939, 885.3889), (-1.1657104868143369, 163.21306130477188, 12.932831704914664), (1.679111, 1.469537, 1.207685), "PWM_Quarry_4x4x4_A101", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (349.02936, 4272.144, 1135.8835), (-14.913544412094382, -60.35735772628974, -10.419585283917264), (1.002876, 1.264728, 1.002876), "PWM_Quarry_4x4x4_A102", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (206.38635, 4230.9336, 1369.6414), (17.21752050552018, 102.89825486171608, 5.755332967442123), (0.7962019, 1.3045868, 1.4365352), "PWM_Quarry_4x4x4_A103", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (265.7651, 4228.91, 1873.235), (27.887922335526714, 86.8980345987552, 1.5181800735935906), (1.002876, 1.5044489, 1.002876), "PWM_Quarry_4x4x4_A104", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2432.5154, 6263.0444, 995.7419), (1.6188409831258848, 15.85321058400386, -11.289337398240077), (0.8973142, 1.469537, 1.207685), "PWM_Quarry_4x4x4_A105", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2377.2908, 6125.2676, 1228.1897), (1.8131006426307512, 178.77002993823493, 11.261918399571021), (0.897314, 1.469537, 1.207685), "PWM_Quarry_4x4x4_A106", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4543.1836, 5484.925, 2150.0752), (0.0, 0.0, 14.610789745363315), (1.0, 1.0, 1.0), "PWM_Quarry_4x4x4_A107_12", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5007.526, 5462.9404, 2065.7397), (-1.7611388603085154, 98.40373852716995, 0.4044951657719195), (1.0, 1.0, 1.0), "PWM_Quarry_4x4x4_A108", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5056.961, 5101.4014, 1957.1633), (0.048281326547163064, 19.813235049402525, 1.806224895443489), (1.0, 1.0, 1.0), "PWM_Quarry_4x4x4_A109", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3935.8765, 5606.1396, 660.8224), (9.638741896297596, 54.60470513009664, -2.3830872487429535), (1.207685, 1.469537, 1.207685), "PWM_Quarry_4x4x4_A11", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4864.638, 5123.545, 2122.5852), (0.0482809908022671, 19.813235044394492, 1.8062249531402008), (1.0, 1.0, 1.0), "PWM_Quarry_4x4x4_A110", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4243.5225, 3772.9414, 1109.1272), (-4.197205190081822, -64.17969049665004, -14.897248556991357), (0.6577779, 0.8776393, 0.76506484), "PWM_Quarry_4x4x4_A111", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (734.3121, 5265.422, 1087.1841), (-7.439208416740497, 171.44745113031337, 10.635225149623144), (1.0, 1.5580211, 1.5894892), "PWM_Quarry_4x4x4_A112_35", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (911.7158, 1607.0994, 914.86), (-16.166902752630136, 164.8831127973248, 2.740600039022566), (0.58546674, 1.276397, 1.0), "PWM_Quarry_4x4x4_A113_75", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (807.31055, 1680.4636, 1268.4375), (-11.56478915907553, 161.15091208281316, -0.19497684280902214), (0.585467, 1.276397, 1.0), "PWM_Quarry_4x4x4_A114", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1946.1467, 1947.8385, 1646.8644), (-14.606170492073618, -159.97071669820866, 4.238452570489039), (0.5866069, 1.1063939, 1.0), "PWM_Quarry_4x4x4_A116", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2732.154, 2357.0576, 2024.9929), (8.325152099849623, 29.51379685495832, -177.79088451006123), (0.586607, 1.106394, 1.0), "PWM_Quarry_4x4x4_A117", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2747.7769, 2420.0942, 1643.6252), (2.733988237612968, 27.949221448981664, -0.19454950101389687), (0.586607, 1.106394, 1.0), "PWM_Quarry_4x4x4_A118", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2593.5398, 2403.5918, 1389.138), (2.737477839619106, 29.372313765968002, -0.1265868733269771), (0.586607, 1.0028124, 1.0), "PWM_Quarry_4x4x4_A119", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4019.787, 5785.697, 887.7635), (12.611548582916623, 36.565067327678776, -7.210176233402635), (1.207685, 1.469537, 1.207685), "PWM_Quarry_4x4x4_A12", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4093.6472, 5695.0635, 1154.1882), (2.4056607818821174, 166.90358522561226, 14.202101112726043), (0.86725605, 1.129108, 0.8422776), "PWM_Quarry_4x4x4_A13", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4111.612, 5761.163, 1313.3835), (14.398522611112995, 84.9294338407436, -0.34423874344755395), (0.867256, 1.129108, 0.867256), "PWM_Quarry_4x4x4_A14", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4080.527, 5661.01, 1410.2188), (2.6280106186052508, 166.03787690745, 14.168104379941205), (0.66293967, 0.9247916, 0.66293967), "PWM_Quarry_4x4x4_A15", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4065.0242, 5462.555, 2069.1675), (-0.17181378215296667, 165.2760011635493, 21.207324702863513), (0.66294, 0.924792, 0.66294), "PWM_Quarry_4x4x4_A16", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4647.938, 4875.7856, 1907.4303), (-9.734131284157339, 172.74462255774884, 9.386843414073175), (0.66294, 0.924792, 0.66294), "PWM_Quarry_4x4x4_A17", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3822.0085, 6110.325, 1338.4907), (15.222520488250785, 100.28261633146172, 6.539672990434162), (0.867256, 0.098463096, 0.867256), "PWM_Quarry_4x4x4_A18", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2283.7903, 5801.103, 870.8138), (-2.184661681240223, 165.13682693274757, 14.337971852664651), (1.207685, 1.469537, 1.207685), "PWM_Quarry_4x4x4_A19", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4629.12, 4734.8433, 883.57074), (12.956979065608992, 35.02688996856172, -7.073486791512739), (1.207685, 1.469537, 1.207685), "PWM_Quarry_4x4x4_A2", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2330.666, 5814.734, 1165.54), (1.7353871316922538, 166.73340568273318, 13.680338080712799), (0.867256, 1.129108, 0.867256), "PWM_Quarry_4x4x4_A20", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2338.9272, 5770.048, 1418.6542), (2.6280108444521386, 166.037876935313, 14.168104353347767), (0.66294, 0.924792, 0.66294), "PWM_Quarry_4x4x4_A21", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (695.4077, 4631.836, 928.5654), (-5.330718349236817, 177.80359719713238, 13.507062819941936), (1.207685, 1.469537, 1.207685), "PWM_Quarry_4x4x4_A22_191", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2122.1135, 5584.7705, 722.69257), (-10.338317934651267, 163.31052111182245, 9.874205153890557), (1.207685, 1.469537, 1.207685), "PWM_Quarry_4x4x4_A23", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1022.165, 4593.2847, 582.4263), (-2.2837216495652757, 165.09093441243778, 14.492621888492463), (1.207685, 1.469537, 1.207685), "PWM_Quarry_4x4x4_A24", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (812.7692, 4374.873, 588.03455), (0.5225164759877526, 143.64506999205634, 15.198318056940382), (1.207685, 1.469537, 1.207685), "PWM_Quarry_4x4x4_A25", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2346.262, 5743.689, 1830.6969), (-0.014709549051460408, 169.00403420612608, 13.80164012222487), (1.0902367, 0.9313415, 0.6694894), "PWM_Quarry_4x4x4_A26_29", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (695.8572, 4710.827, 1044.1626), (-7.857359996613322, -47.923334650615814, -13.171812179548594), (1.207685, 1.469537, 1.207685), "PWM_Quarry_4x4x4_A27", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (550.6917, 4453.1553, 1011.4735), (-14.671049669433351, -69.09319338934444, -10.208890796702091), (1.207685, 1.469537, 1.207685), "PWM_Quarry_4x4x4_A28", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (573.764, 4714.9053, 1405.2551), (-5.862731126800304, -43.09710235699063, -12.093747574026102), (1.207685, 1.469537, 1.207685), "PWM_Quarry_4x4x4_A29", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2438.189, 2428.3535, 927.7567), (-3.854522749101205, -58.45960246016607, -8.934449426543127), (1.0, 2.280143, 1.0), "PWM_Quarry_4x4x4_A3", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (610.50964, 2208.577, 1104.4858), (-15.016175658615358, 87.11633371605947, 8.232052771518982), (1.207685, 1.469537, 1.207685), "PWM_Quarry_4x4x4_A30", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (761.60846, 2547.4663, 2093.5625), (10.727903138660983, -116.2755103008007, -18.559599059972562), (0.8932329, 1.1550848, 0.8932329), "PWM_Quarry_4x4x4_A31", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (523.8819, 4438.441, 1202.5017), (-17.860686119123088, -59.78850600512197, -10.579771986397066), (1.002876, 1.2647281, 1.002876), "PWM_Quarry_4x4x4_A32", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (227.55325, 4273.6006, 807.63837), (-13.298279074451738, -59.13641452907198, -11.709441636458399), (1.002876, 1.264728, 1.002876), "PWM_Quarry_4x4x4_A33", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (735.0517, 2146.047, 1443.6576), (2.399793594483592, 12.713734848183492, 3.3895593711221417), (1.1285805, 0.95932853, 0.95932853), "PWM_Quarry_4x4x4_A34", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (451.24454, 4351.879, 1485.4409), (-14.913544412094382, -60.35735772628974, -10.419585283917264), (1.002876, 1.264728, 1.002876), "PWM_Quarry_4x4x4_A35", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3135.4126, 2185.1206, 862.45197), (-8.481018352638333, -138.29989562047317, 5.7295878608799935), (1.0, 1.0, 1.0), "PWM_Quarry_4x4x4_A36_388", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2942.223, 2081.7952, 1095.0366), (-7.233062083673372, -138.17257277891358, 5.712531574385342), (1.3549933, 1.0, 1.0), "PWM_Quarry_4x4x4_A37_390", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3925.4534, 2772.5315, 780.01874), (-8.48098731908538, -138.29964495779734, -0.24456779854946645), (1.0, 1.2987841, 1.0), "PWM_Quarry_4x4x4_A38_466", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3978.5918, 2891.7202, 1150.3848), (16.649272239606756, 109.71630252600443, 11.467127195319424), (1.0, 1.0, 1.0), "PWM_Quarry_4x4x4_A39_468", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1976.59, 2255.7727, 809.2751), (2.56754264435396, 132.00353766433386, 8.335844661169611), (1.0, 2.280143, 1.0), "PWM_Quarry_4x4x4_A4", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4481.151, 3084.3274, 2248.9956), (4.5507022941519075, 148.64009115825485, 17.149311355027493), (1.0, 1.6214223, 1.0), "PWM_Quarry_4x4x4_A40_499", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4769.662, 3235.201, 722.86945), (-10.229341793184469, -174.1231900536824, 6.495552976230869), (1.207685, 1.469537, 1.207685), "PWM_Quarry_4x4x4_A41_529", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4604.49, 3087.296, 1004.06775), (-3.7708435800562365, -62.11657530980971, -13.109711056788708), (1.207685, 1.469537, 1.207685), "PWM_Quarry_4x4x4_A42_530", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4471.5273, 3137.9795, 1373.8352), (-5.522369678235009, -61.526362635150875, -11.557922188829963), (0.867256, 1.129108, 0.867256), "PWM_Quarry_4x4x4_A43_531", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4417.2056, 3058.7725, 1294.6263), (-12.046689212636007, -144.10395155616416, 3.0895620278049547), (0.867256, 1.129108, 0.867256), "PWM_Quarry_4x4x4_A44_532", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4215.7314, 3090.0657, 1403.5817), (-5.862731126800304, -43.09710235699063, -12.093747574026102), (1.207685, 1.469537, 1.207685), "PWM_Quarry_4x4x4_A45", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4424.8955, 3064.207, 1616.9362), (-2.548614335674588, -62.88858317322324, -12.210787281588122), (0.66294, 0.924792, 0.66294), "PWM_Quarry_4x4x4_A46_533", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4231.319, 2861.1306, 905.74243), (-3.1284177480205964, 136.37006761474507, 10.533617196644235), (1.207685, 1.469537, 1.207685), "PWM_Quarry_4x4x4_A47_551", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4607.1016, 3076.6357, 816.943), (-3.1284177480205964, 136.37006761474507, 10.533617196644235), (1.207685, 1.469537, 1.207685), "PWM_Quarry_4x4x4_A48", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4296.8105, 2800.5447, 765.78436), (-10.981721739174441, -149.02911197446102, -0.18197622399298402), (1.207685, 1.469537, 1.207685), "PWM_Quarry_4x4x4_A49", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2927.2844, 2462.7683, 903.5897), (-0.105377508462785, -58.99716101782186, -8.702972331283624), (1.1692523, 1.0, 1.0), "PWM_Quarry_4x4x4_A5_69", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4219.4424, 2891.4954, 1238.4285), (-2.8444217697612566, -52.632420138264116, -12.108063863733676), (0.867256, 1.129108, 0.867256), "PWM_Quarry_4x4x4_A50", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4191.328, 2914.4226, 1395.2478), (6.748436931782106, 112.95296118750966, -167.51543624883658), (0.867256, 1.129108, 0.867256), "PWM_Quarry_4x4x4_A51", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4328.1, 2995.5486, 1433.0638), (5.063171337269399, 124.47622264998117, -166.22260649551805), (0.867256, 1.129108, 0.867256), "PWM_Quarry_4x4x4_A52", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4396.824, 2967.2825, 1926.7708), (-16.444853270964447, -80.82384780940386, -8.78539913471226), (0.73070747, 1.129108, 0.867256), "PWM_Quarry_4x4x4_A53", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5123.9336, 4239.7783, 1222.124), (-17.101193940172205, -131.15886909253635, 2.9113665759915874), (1.0638468, 1.129108, 0.867256), "PWM_Quarry_4x4x4_A54_598", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4573.6763, 3469.84, 927.43854), (-13.125518714389623, -131.16443451203088, -0.08047527003194983), (1.8659875, 1.129108, 0.867256), "PWM_Quarry_4x4x4_A55", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4934.66, 3933.6282, 2321.6245), (-14.366577937865255, -130.91706666865986, 4.831681858342943), (1.063847, 1.129108, 0.867256), "PWM_Quarry_4x4x4_A56", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4296.3374, 3264.3652, 2088.843), (-14.366577937865255, -130.91706666865986, 4.831681858342943), (1.063847, 1.129108, 0.867256), "PWM_Quarry_4x4x4_A57", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5883.3125, 5361.3687, 935.1881), (0.7081333292529187, 130.7344624900509, 13.620785505078652), (1.207685, 2.1346319, 1.207685), "PWM_Quarry_4x4x4_A58_617", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5028.462, 4289.052, 1362.4929), (-16.624418883385733, -119.69509901259622, -4.146818888711122), (0.7599691, 1.129108, 0.867256), "PWM_Quarry_4x4x4_A59", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3914.6667, 3511.412, 904.8886), (1.6951847778058309, 122.03667202111039, 8.343965735204522), (0.8947365, 2.2926378, 1.0), "PWM_Quarry_4x4x4_A6", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5092.945, 4277.541, 1516.6517), (13.250948965981587, 67.29808351750695, 6.123489573390024), (0.759969, 1.129108, 0.867256), "PWM_Quarry_4x4x4_A60", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5032.7495, 4345.158, 1665.6788), (16.107353381049847, 66.48625766918705, 5.89368367825489), (0.759969, 1.129108, 0.867256), "PWM_Quarry_4x4x4_A61", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5099.7417, 4156.2363, 2158.075), (-19.286435267532585, -131.42994288864804, 6.764537389343793), (0.759969, 1.129108, 0.867256), "PWM_Quarry_4x4x4_A62", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5682.3115, 5289.05, 1279.3182), (-3.177918598648028, 146.88159867921496, 15.061926891571831), (1.207685, 2.134632, 1.2890624), "PWM_Quarry_4x4x4_A63", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (828.8788, 368.21246, 932.6432), (-1.4663999663900007, 151.91958721043423, 10.542314839889231), (1.207685, 1.2949601, 1.207685), "PWM_Quarry_4x4x4_A64_631", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (769.1381, 433.21274, 1318.9823), (-9.823272393655952, -94.08330530509924, -9.218536298426272), (1.0396669, 1.129108, 0.867256), "PWM_Quarry_4x4x4_A65", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1001.8275, 394.46207, 900.1522), (-6.91665700371109, 173.78270784649683, 10.355715994053307), (0.867256, 1.129108, 0.867256), "PWM_Quarry_4x4x4_A66", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4459.9795, 5196.419, 793.6712), (11.04313677508699, 66.85441710728685, -0.0546262946382147), (1.207685, 1.469537, 0.6847378), "PWM_Quarry_4x4x4_A67", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (700.4756, 277.9615, 2098.5723), (0.6104555670594509, -171.07301905956206, -166.87166984173913), (0.867256, 1.129108, 0.867256), "PWM_Quarry_4x4x4_A68", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (681.5823, 396.9608, 1876.9734), (-7.660645759445454, 175.69016598439254, -170.47053576147954), (0.867256, 1.603044, 0.867256), "PWM_Quarry_4x4x4_A69", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (835.3553, 2097.1108, 1040.3323), (-3.6640929764938006, -121.10983088326738, -5.125549900345971), (1.169252, 1.0, 1.0), "PWM_Quarry_4x4x4_A7", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (750.748, 527.48724, 1565.064), (-7.660614810774331, 175.69016690894878, 13.575928963711979), (0.867256, 1.1022084, 0.867256), "PWM_Quarry_4x4x4_A70", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3440.9365, 2396.8752, 2144.8867), (6.7484796909688605, 112.94863364225499, 8.077451917199582), (0.867256, 1.129108, 0.867256), "PWM_Quarry_4x4x4_A71_641", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2137.506, 1859.1835, 2261.491), (7.322560618279145, 113.02990775442223, 8.087901245743), (0.867256, 1.129108, 0.867256), "PWM_Quarry_4x4x4_A72", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2182.763, 5539.0083, 1036.1864), (4.089923999763494, 115.58973862922521, 9.25874911896282), (0.65900487, 0.9208569, 0.65900487), "PWM_Quarry_4x4x4_A73_31", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5516.9424, 317.3097, 725.30444), (-13.029601661616146, -151.5914310546916, 0.3063170914610329), (1.207685, 1.469537, 1.207685), "PWM_Quarry_4x4x4_A74", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5509.4155, 838.5157, 674.1129), (12.460509411943125, 47.11279198699161, 3.856173787959405), (1.207685, 1.469537, 1.207685), "PWM_Quarry_4x4x4_A75", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5568.269, 609.0187, 697.5312), (-0.22744759700478467, 46.2649242769889, 3.7653451579019497), (1.207685, 1.469537, 1.207685), "PWM_Quarry_4x4x4_A76", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5864.935, 959.31714, 767.0398), (-7.467253721509674, -94.71859131992223, -10.715636900073575), (1.207685, 1.469537, 1.207685), "PWM_Quarry_4x4x4_A77", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (6036.6914, 850.2764, 829.4301), (-7.467224078446105, -94.71850744641694, -7.888579331940864), (1.207685, 1.469537, 1.207685), "PWM_Quarry_4x4x4_A78", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (6017.299, 743.9392, 1173.09), (1.5753490040112914, 102.93881480714798, 12.771755852163686), (1.207685, 1.469537, 1.207685), "PWM_Quarry_4x4x4_A79", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3769.81, 3197.1626, 944.2745), (-19.954220607645066, -132.72037464726165, 6.774589503303489), (1.169252, 1.0, 1.0), "PWM_Quarry_4x4x4_A8", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5651.655, 868.1728, 882.41736), (1.575349538023698, 102.93881482185725, 12.771755418317353), (1.0370706, 1.2989228, 1.0370706), "PWM_Quarry_4x4x4_A80", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5736.3086, 864.9794, 1007.0607), (1.575349538023698, 102.93881482185725, 12.771755418317353), (1.037071, 1.298923, 1.037071), "PWM_Quarry_4x4x4_A81", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5901.5913, 1020.29224, 982.06244), (-4.323272521166342, -92.63500125962423, -14.098236179966115), (0.7626138, 1.0244659, 0.7626138), "PWM_Quarry_4x4x4_A82", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5713.924, 470.27896, 971.82776), (0.5181183810615446, 102.69988990540607, 18.05384488362936), (1.5908048, 1.298923, 1.037071), "PWM_Quarry_4x4x4_A83", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5682.1387, 456.9133, 1305.7441), (0.5181175348585797, 102.70074856164324, 12.077665893949591), (1.590805, 1.298923, 1.037071), "PWM_Quarry_4x4x4_A84", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5609.8213, 395.58972, 1619.4241), (19.335482900113778, 8.06494308611942, -3.038452352937194), (1.0315638, 1.4971353, 1.0364363), "PWM_Quarry_4x4x4_A85", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5746.292, 776.41956, 1234.3352), (-4.280426340075076, -87.46991172767976, -10.779663259378616), (1.1327679, 1.39462, 1.1327679), "PWM_Quarry_4x4x4_A86", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (6106.175, 1107.1776, 672.0077), (-5.093231168743469, -82.88058834602445, -12.018126700868383), (1.207685, 1.469537, 1.207685), "PWM_Quarry_4x4x4_A87", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5871.1724, 771.27655, 1619.5024), (-3.6704090940582526, 101.74963526553162, 12.795245343465345), (0.91627043, 1.5534055, 1.207685), "PWM_Quarry_4x4x4_A88", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5884.893, 655.88367, 2120.3933), (15.015308193847796, -2.7537537067798548, 4.643211442080624), (1.4917319, 1.298923, 2.0854049), "PWM_Quarry_4x4x4_A89", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3852.3762, 3669.266, 732.3899), (4.716967051900821, 136.0124775598189, 7.633687125433782), (1.0, 2.280143, 1.0), "PWM_Quarry_4x4x4_A9", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5607.0244, 473.7443, 2183.157), (-16.542905320522998, -142.39333062832614, -9.360990834582525), (1.207685, 1.4462345, 1.207685), "PWM_Quarry_4x4x4_A90", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5660.526, 186.01416, 943.1969), (-11.48785335887274, -121.63378128285026, -14.106169876112721), (1.207685, 1.469537, 0.62455577), "PWM_Quarry_4x4x4_A91", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (6129.205, 5583.58, 999.9107), (-5.093139812640957, -82.88001263459799, -15.221497499360114), (0.9477704, 1.469537, 1.207685), "PWM_Quarry_4x4x4_A92", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (6146.052, 5004.4297, 879.7771), (-13.464997100121119, 171.61709385190343, 8.787011827572046), (0.94777, 1.469537, 1.207685), "PWM_Quarry_4x4x4_A93", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3805.3162, 3101.5728, 1221.7275), (11.825986985961535, 19.26757733947948, -16.40145689336813), (1.0, 1.0, 1.0), "PWM_Quarry_4x4x4_A94", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2080.4243, 1678.1984, 1479.5555), (-8.101959214689366, -67.31741408616755, -15.115508634967746), (1.169252, 0.7765052, 1.0), "PWM_Quarry_4x4x4_A95", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1987.5908, 1578.8656, 1864.1537), (-9.354125259105514, -175.13721443248184, 12.099782820347373), (0.9370461, 1.351528, 1.0), "PWM_Quarry_4x4x4_A96", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4818.688, 4261.8047, 1982.0214), (13.84960082680239, 67.36437379549528, 6.139105920749779), (0.43758765, 1.4973264, 1.1534156), "PWM_Quarry_4x4x4_A97", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4454.871, 3492.0742, 1159.9026), (-14.57369811650001, -137.1940617194772, -0.14825413644581498), (0.759969, 1.129108, 0.867256), "PWM_Quarry_4x4x4_A98", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4281.9, 3479.6655, 1418.6991), (13.813922810178495, 61.194271264261054, 1.2017580021209378), (0.5138165, 1.129108, 0.867256), "PWM_Quarry_4x4x4_A99", _folder)
if a: placed += 1
else: skipped += 1

# Batch 12: StaticMesh'PWM_Quarry_8x8x8_A' (414 instances)
_mesh_path = "/Game/Unshippable/Whitebox/Rocks/Meshes/PWM_Quarry_8x8x8_A"
_materials = ['/Game/Environments/ProcTexturing/ProcMaterial_Quarry_Atlas_2']
_folder = "Reconstruction/BD_BB_MiningCamp/Meshes"
a = spawn_static_mesh(_mesh_path, _materials, (2340.2102, 1728.6273, 2241.2522), (16.081392991200207, 30.712585032070542, -6.952484814037971), (0.6183413, 0.26665324, 0.26665324), "PWM_Quarry_8x8x8_A_570", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3315.797, 3050.5757, 1991.6124), (8.694399433653805, 47.665990434750924, -177.95826666062453), (0.933322, 0.425522, 0.425522), "PWM_Quarry_8x8x8_A10", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2907.7366, 5560.8047, 2032.7537), (1.4581225859142097, -174.38203105085847, 14.224275602440553), (0.204809, 0.178583, 0.309656), "PWM_Quarry_8x8x8_A100", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2710.1882, 6010.49, 1956.7362), (-0.4509582750659451, -174.86585182270855, 14.220457608523917), (0.204809, 0.178583, 0.309656), "PWM_Quarry_8x8x8_A101", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5248.869, 3889.418, 924.387), (-12.102020411807189, -115.18469082661123, 3.0429844526243817), (0.933322, 0.425522, 0.425522), "PWM_Quarry_8x8x8_A102", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4102.6426, 2708.7437, 2056.283), (-11.445952688966136, -151.7241847301187, 176.67889474997764), (0.933322, 0.425522, 0.425522), "PWM_Quarry_8x8x8_A103_449", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4074.804, 2647.9934, 2399.279), (-10.902619503327724, -149.45709368594035, 2.9703365815827625), (0.933322, 0.425522, 0.425522), "PWM_Quarry_8x8x8_A104_450", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2641.6428, 6062.3936, 1979.9308), (-3.3119504582281225, -174.62741278317083, 15.449965186229864), (0.862786, 0.64814, 0.303582), "PWM_Quarry_8x8x8_A105", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2761.4797, 1318.8854, 2607.6208), (-11.080474058468972, -152.12598622423295, 17.595211245823474), (1.1031709, 0.425522, 0.5638425), "PWM_Quarry_8x8x8_A106_333", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2165.6968, 1259.7767, 2367.2869), (14.85713440460528, 33.44841382966694, 8.229788523316394), (1.02025, 0.425522, 0.563764), "PWM_Quarry_8x8x8_A107_334", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2930.831, 1692.8469, 2475.4832), (9.082681692304934, 22.375505812338904, -18.598480101517026), (0.933322, 0.425522, 0.425522), "PWM_Quarry_8x8x8_A108_335", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3589.5579, 1964.0214, 2589.3628), (10.41146064651869, 26.461411845547122, -17.90646328559514), (0.933322, 0.425522, 0.425522), "PWM_Quarry_8x8x8_A109_398", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1725.5677, 1890.9219, 1364.2712), (15.203278807897409, 50.087784312719975, 8.78938117391084), (0.6598606, 0.46224338, 0.579951), "PWM_Quarry_8x8x8_A11", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2058.7893, 1200.0135, 2181.7769), (-10.578061744760282, -152.12463645801122, 0.14689395560432617), (0.933322, 0.425522, 0.425522), "PWM_Quarry_8x8x8_A110_400", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4631.314, 2743.9631, 2738.982), (-10.01348732097501, -155.6853812940776, 16.102462644160834), (0.688652, 0.425522, 0.425522), "PWM_Quarry_8x8x8_A111_451", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4400.3115, 2380.362, 2732.947), (11.704074402965214, 27.986387128748607, -17.87268074699883), (0.320675, 0.240767, 0.425522), "PWM_Quarry_8x8x8_A112_452", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4182.12, 2317.6584, 2784.1902), (10.988831189498153, 27.817708183826525, -16.856172042533615), (0.320675, 0.240767, 0.425522), "PWM_Quarry_8x8x8_A113_453", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4034.4912, 2464.3142, 2607.076), (-6.939299656021964, -154.75150471028988, 16.058385398075075), (0.968355, 0.456968, 0.456968), "PWM_Quarry_8x8x8_A114_454", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3565.9304, 2501.3948, 2055.127), (-10.091766125996495, -152.69603689586614, 10.627896713524434), (0.933322, 0.425522, 0.563764), "PWM_Quarry_8x8x8_A115_455", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3198.9695, 2357.7483, 2005.7897), (-12.068390431360276, -142.54980632238056, -0.04434218099498727), (0.933322, 0.425522, 0.425522), "PWM_Quarry_8x8x8_A116_456", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3337.688, 2286.7031, 1913.1024), (-10.509947384421428, -145.5356613503034, -2.9595642362406864), (0.204809, 0.124901, 0.309656), "PWM_Quarry_8x8x8_A117_457", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2851.637, 2016.9163, 1369.1019), (1.429797774413268, -46.79201608483018, -15.669554593124863), (0.27929327, 0.6138262, 0.309656), "PWM_Quarry_8x8x8_A118", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3583.2373, 2092.6047, 2669.125), (10.055908339930898, 29.359159925652197, -8.947722560100996), (1.02025, 0.425522, 0.563764), "PWM_Quarry_8x8x8_A119", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2374.6523, 2418.6514, 1242.9934), (11.581987066613976, 36.09964038818504, 3.1144175855845146), (0.933322, 0.425522, 0.425522), "PWM_Quarry_8x8x8_A12", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3513.8945, 2205.335, 2339.5264), (-9.434479578158813, -150.2265813237237, 2.937147133903846), (1.02025, 0.425522, 0.563764), "PWM_Quarry_8x8x8_A120", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3054.6052, 2034.7535, 2312.8008), (9.082681419747285, 22.37465340427239, -8.363647606073032), (0.47905794, 0.38014883, 0.5788257), "PWM_Quarry_8x8x8_A121", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2856.8215, 2011.049, 2427.9336), (-9.471253380139673, -154.87868856571035, 7.921955421606546), (0.479058, 0.380149, 0.578826), "PWM_Quarry_8x8x8_A122", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2504.319, 5708.417, 1577.97), (14.254595057187732, 90.60045775118957, 4.764220575363769), (0.1450009, 0.118774876, 0.24984786), "PWM_Quarry_8x8x8_A123", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3239.4646, 1573.5648, 2735.68), (-10.656920599150379, -152.74801317624127, 17.762801267809206), (0.8585011, 0.425522, 0.5638425), "PWM_Quarry_8x8x8_A124", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4957.5117, 3781.1172, 2466.0356), (-8.880369690064816, -156.57014499153848, 18.80907240962996), (0.933322, 0.425522, 0.563764), "PWM_Quarry_8x8x8_A125", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4810.4775, 3410.4375, 2426.6887), (-10.659303353175453, -146.53993017870414, 2.6645392658459115), (0.933322, 0.425522, 0.425522), "PWM_Quarry_8x8x8_A126", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4770.9253, 3203.1409, 2714.8772), (8.874416987479034, 25.60739048411247, -12.552856649714611), (2.1252968, 0.5878455, 0.75465614), "PWM_Quarry_8x8x8_A127_497", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2540.7727, 1705.951, 1132.974), (2.0098299753966153, -41.65261551502608, -8.319642152815932), (0.61617374, 1.0241599, 0.5282188), "PWM_Quarry_8x8x8_A128_501", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4710.774, 3606.8396, 2338.906), (-5.533782676461513, -149.1345656110163, 11.938147440730027), (0.204809, 0.124901, 0.309656), "PWM_Quarry_8x8x8_A129", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3194.1838, 3060.9658, 2278.636), (11.703198867473532, 49.67965999658063, 11.014865459893146), (0.933322, 0.425522, 0.425522), "PWM_Quarry_8x8x8_A13", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4766.5166, 3663.6155, 2197.9434), (-10.280092372683654, -146.05244566398824, 2.6436298429257636), (0.204809, 0.124901, 0.309656), "PWM_Quarry_8x8x8_A130", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2810.898, 2190.602, 1493.5135), (1.4297988074567372, -46.79184139363987, -16.783202778114532), (0.279293, 0.462493, 0.309656), "PWM_Quarry_8x8x8_A131_505", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1158.3827, 898.9113, 2252.4224), (9.914517752309001, 27.081367928349767, -9.352447806516125), (1.2211704, 0.7968512, 0.9265111), "PWM_Quarry_8x8x8_A132_517", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1894.0779, 1997.717, 1295.0275), (-77.68857808600346, 33.49856555019021, -81.64558560251498), (0.439019, 0.87892234, 0.46252), "PWM_Quarry_8x8x8_A133", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2036.8933, 2178.7048, 1032.1147), (-12.721436353634612, -145.74857110898287, 9.593066912831887), (0.6365808, 0.5089479, 0.32933322), "PWM_Quarry_8x8x8_A134", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2402.2463, 2483.3179, 977.75275), (-10.704497457160748, -156.67841023948137, 11.791589118608124), (0.636581, 0.508948, 0.329333), "PWM_Quarry_8x8x8_A135", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3765.8289, 3602.0728, 906.33496), (-7.982971034938452, -131.8076856334918, 4.499663853614147), (0.636581, 0.508948, 0.329333), "PWM_Quarry_8x8x8_A136", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1683.757, 1952.7972, 1685.6797), (-12.590790199644552, -138.7362135614382, -15.877932035611725), (0.6839454, 0.508948, 0.329333), "PWM_Quarry_8x8x8_A137", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1647.2966, 2057.257, 1913.3829), (14.017423638038037, 35.89688160608195, 14.646435296373822), (0.683945, 0.508948, 0.329333), "PWM_Quarry_8x8x8_A138", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (626.08746, 2332.2314, 1031.7028), (-11.667568145207115, 157.71892084705385, -3.5146166487673423), (0.636581, 0.508948, 0.329333), "PWM_Quarry_8x8x8_A139", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (6068.3164, 5328.3374, 2264.466), (-15.368958066780475, -133.09797930981316, 5.689719087660527), (0.933322, 0.425522, 0.69646597), "PWM_Quarry_8x8x8_A14", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3749.524, 3392.5278, 1093.1328), (-9.26287982702495, -133.2085058217813, -3.684632187758256), (0.636581, 0.508948, 0.329333), "PWM_Quarry_8x8x8_A140", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2308.4224, 1952.1824, 1193.3552), (0.6200194780001367, 149.4247530152378, -170.66235812695848), (0.616174, 1.02416, 0.528219), "PWM_Quarry_8x8x8_A141_238", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4002.5999, 3933.1355, 819.14636), (-11.771483313216663, -123.52202500000188, 4.092006132596518), (0.636581, 0.508948, 0.329333), "PWM_Quarry_8x8x8_A142", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1185.2611, 2132.462, 1927.23), (13.331490793238407, 39.03448577176701, 15.392015020740851), (0.683945, 0.508948, 0.329333), "PWM_Quarry_8x8x8_A143", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (388.83868, 2485.8286, 875.34503), (-11.382599593677318, 149.4827436537262, -3.409636811002427), (0.636581, 0.508948, 0.329333), "PWM_Quarry_8x8x8_A144_105", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4013.5884, 3682.6184, 1099.3425), (11.292233769525163, 55.705874923154994, -4.2539683059520055), (0.500213, 0.374622, 0.238599), "PWM_Quarry_8x8x8_A145", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (977.99866, 2337.8362, 2060.81), (13.33149097824241, 39.03448570185198, 15.392014463936407), (0.683945, 0.508948, 0.329333), "PWM_Quarry_8x8x8_A146", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3872.4048, 3415.9766, 1325.9324), (10.59134676168052, 44.358693602366515, 164.1773564364479), (0.49551332, 0.508948, 0.329333), "PWM_Quarry_8x8x8_A147", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3795.9397, 3316.817, 1564.5333), (11.749689187954969, 42.078396211778944, 169.27682502899515), (0.55323863, 0.508948, 0.329333), "PWM_Quarry_8x8x8_A148", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4593.014, 4498.295, 1981.348), (5.960389971992664, 87.37210830876325, -170.28469941757973), (0.495513, 0.508948, 0.329333), "PWM_Quarry_8x8x8_A149", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3716.5186, 3429.6064, 1794.2222), (12.08541778149149, 40.25492946751184, 3.863479210113012), (0.58856523, 0.2667215, 0.2667215), "PWM_Quarry_8x8x8_A15", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3900.3508, 3673.5603, 1039.4408), (-11.124847211186484, -126.46889458423766, 4.679128436110423), (0.500213, 0.374622, 0.238599), "PWM_Quarry_8x8x8_A150", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3604.973, 3382.0857, 988.25525), (7.158521487747258, 48.77472925717948, 168.93883115329498), (0.500213, 0.374622, 0.238599), "PWM_Quarry_8x8x8_A151", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4040.318, 4158.227, 913.6948), (12.304762042056758, 57.42138150853313, -2.8576653977065387), (0.500213, 0.26178437, 0.238599), "PWM_Quarry_8x8x8_A152", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1090.1074, 2346.1577, 2172.9187), (17.998164751976354, 21.707369534840705, -158.98725928201475), (0.82869977, 0.374189, 0.42733806), "PWM_Quarry_8x8x8_A153", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4504.4326, 4592.2935, 919.1046), (-9.812530943428577, -115.326327863411, 2.8402254512459644), (0.636581, 0.508948, 0.329333), "PWM_Quarry_8x8x8_A154", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4587.035, 4511.2344, 1396.2212), (14.999237141754282, 55.42308864532012, -4.255004469356195), (0.500213, 0.374622, 0.238599), "PWM_Quarry_8x8x8_A155", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4471.088, 4307.9316, 1139.9656), (-11.145721772870044, -126.21603687585691, 4.630239996131188), (0.500213, 0.374622, 0.238599), "PWM_Quarry_8x8x8_A156", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4210.4517, 3810.738, 2087.1406), (-14.405581526469616, -126.49131998300751, -7.310791053603404), (0.97290885, 0.374622, 0.238599), "PWM_Quarry_8x8x8_A157", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3876.4446, 6122.8853, 806.784), (-10.183961218906076, -97.3082632529163, -2.0321964284788474), (0.5722521, 0.508948, 0.329333), "PWM_Quarry_8x8x8_A158_135", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4007.5356, 5557.22, 2116.5093), (-19.81198259415446, -91.93304424927176, -4.622161864101408), (0.636581, 0.508948, 0.329333), "PWM_Quarry_8x8x8_A159", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4513.3916, 4541.4766, 2126.8313), (-9.288206559054991, -102.61278739089965, -12.99389599883092), (0.6592059, 0.425522, 0.425522), "PWM_Quarry_8x8x8_A16", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4073.7207, 5687.7715, 1886.7065), (-19.81198259415446, -91.93304424927176, -4.622161864101408), (0.636581, 0.508948, 0.329333), "PWM_Quarry_8x8x8_A160", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4047.3596, 5753.525, 1633.5112), (17.800108046164382, 94.66824499190035, -175.3200671622067), (0.495513, 0.508948, 0.329333), "PWM_Quarry_8x8x8_A161", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3844.8728, 5826.499, 2061.5852), (10.753406292408085, 1.440063649927962, -21.0225226001458), (0.47294876, 0.97534496, 0.511217), "PWM_Quarry_8x8x8_A162", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3946.7415, 6156.542, 1041.1711), (12.597654857199506, 86.15076294054494, -178.26801000260076), (0.495513, 0.508948, 0.329333), "PWM_Quarry_8x8x8_A163_155", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4005.6453, 6135.6514, 1577.3597), (17.271357449628006, 94.62291427261952, -175.33374491084282), (0.495513, 0.508948, 0.329333), "PWM_Quarry_8x8x8_A164", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4032.0764, 5957.813, 1176.6323), (15.045722771096273, 94.10870244702704, 4.484802284405972), (0.495513, 0.508948, 0.329333), "PWM_Quarry_8x8x8_A165", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2445.948, 6281.792, 937.41986), (13.322782242708081, 86.17261457070022, -178.26275723212387), (0.495513, 0.508948, 0.329333), "PWM_Quarry_8x8x8_A166", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2455.3733, 6038.9346, 880.9833), (13.322782242708081, 86.17261457070022, -178.26275723212387), (0.495513, 0.508948, 0.329333), "PWM_Quarry_8x8x8_A167", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2460.616, 5860.6714, 837.25397), (-11.26040638091088, -73.68238041407942, 174.05755865038014), (0.495513, 0.508948, 0.329333), "PWM_Quarry_8x8x8_A168", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2495.1228, 5617.3677, 1653.3507), (14.254594792172883, 90.60045796808346, 1.6985778399028446), (0.145001, 0.118775, 0.249848), "PWM_Quarry_8x8x8_A169_20", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2685.3777, 2573.8635, 1509.9133), (14.425489641154325, 35.46049683932408, 9.289154492633177), (0.48705322, 0.39906275, 0.2515548), "PWM_Quarry_8x8x8_A17", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2371.2505, 5141.309, 2503.4429), (-7.5418084929963305, -158.29732287715933, 24.127841114768657), (0.933322, 0.425522, 0.4286534), "PWM_Quarry_8x8x8_A170_16", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2649.4824, 5751.5444, 1800.7297), (14.254594792172883, 90.60045796808346, 1.6985778399028446), (0.145001, 0.29851928, 0.249848), "PWM_Quarry_8x8x8_A171_22", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2398.539, 5883.402, 1097.6289), (4.561203264196057, -2.281982269525272, 167.41296760872547), (0.495513, 0.508948, 0.329333), "PWM_Quarry_8x8x8_A172", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1914.048, 4994.3667, 2454.6985), (6.553525088037602, 19.495024191547294, -24.395295203364768), (0.933322, 0.425522, 0.428653), "PWM_Quarry_8x8x8_A173", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2423.1584, 5720.4766, 2179.5928), (3.2985646253007865, 14.868348001460776, -30.18923983647642), (1.0456077, 0.975345, 0.511217), "PWM_Quarry_8x8x8_A174_220", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1119.8665, 2363.0864, 1935.1162), (8.551567522546337, 40.52325424383626, 19.16038207563015), (0.2254331, 0.508948, 0.329333), "PWM_Quarry_8x8x8_A175_225", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (958.8065, 2353.868, 1668.5114), (-18.420743883989687, 124.32339179785178, 8.502899886794268), (0.225433, 0.38300318, 0.329333), "PWM_Quarry_8x8x8_A176_227", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (447.99634, 2323.3867, 1141.8417), (-11.667568145207115, 157.71892084705385, -3.5146166487673423), (0.636581, 0.508948, 0.329333), "PWM_Quarry_8x8x8_A177_262", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (487.56882, 2397.296, 1873.1816), (-13.233519556629334, 165.00828857709445, -11.789733383764606), (0.76220775, 0.6345748, 0.5894506), "PWM_Quarry_8x8x8_A178", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (479.25998, 2322.9338, 1364.0365), (-14.636383686423493, 168.63525832809626, -9.216215725133162), (0.636581, 0.508948, 0.329333), "PWM_Quarry_8x8x8_A179", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3483.925, 3134.256, 1707.6897), (12.649974836851364, 38.023972370038855, -3.7375472920912123), (0.487053, 0.399063, 0.251555), "PWM_Quarry_8x8x8_A18", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (671.9936, 2297.2695, 1449.162), (15.448921559668863, -16.997407502086308, 7.7562713253996645), (0.636581, 0.508948, 0.65684277), "PWM_Quarry_8x8x8_A180", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (887.52325, 2399.4695, 1676.0651), (17.898660760611904, -59.12640091335644, -9.578980387173798), (0.225433, 0.383003, 0.329333), "PWM_Quarry_8x8x8_A181_268", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (808.6276, 2514.6296, 1831.5265), (-18.420743883989687, 124.32339179785178, 8.502899886794268), (0.225433, 0.383003, 0.329333), "PWM_Quarry_8x8x8_A182", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (962.99445, 2449.8906, 1825.3834), (19.87968028512665, -41.433378504397034, -3.8068854107654477), (0.225433, 0.383003, 0.329333), "PWM_Quarry_8x8x8_A183", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (731.5943, 2522.3103, 1781.2976), (19.87968484060953, -41.43337880574823, -3.806671096656104), (0.225433, 0.383003, 0.329333), "PWM_Quarry_8x8x8_A184", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (547.6278, 2528.623, 1831.5936), (18.365519627135726, -41.41473047103694, 2.496036727775937), (0.225433, 0.383003, 0.329333), "PWM_Quarry_8x8x8_A185", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (815.19354, 2366.976, 1677.563), (-17.765319594443458, 147.7918159177011, -5.356078056872905), (0.225433, 0.383003, 0.329333), "PWM_Quarry_8x8x8_A186", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (883.8545, 2295.3137, 1431.1008), (18.271333445508763, -59.170811193576114, -3.126771143296525), (0.225433, 0.383003, 0.329333), "PWM_Quarry_8x8x8_A187", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2766.0935, 1752.6974, 964.6292), (10.673475813728968, 49.65485098910347, 1.4528182130304983), (0.8562924, 0.508948, 0.3927226), "PWM_Quarry_8x8x8_A188_355", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2870.3162, 1657.3636, 832.1129), (-8.282408405910235, -125.33959403991564, -2.374572613589384), (0.856292, 0.508948, 0.392723), "PWM_Quarry_8x8x8_A189_396", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3234.2637, 2853.9194, 1815.8405), (13.248087973935906, 38.13129939515974, 9.80025869281993), (0.487053, 0.399063, 0.251555), "PWM_Quarry_8x8x8_A19", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3140.4116, 2386.6353, 1802.583), (9.79720891705812, 33.779480186069215, 0.7112088898960883), (0.8019129, 0.374622, 0.238599), "PWM_Quarry_8x8x8_A190_458", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4547.0347, 3408.5312, 2207.8276), (10.864379491233812, 29.970195231426143, -4.065276661348681), (0.972909, 0.374622, 0.238599), "PWM_Quarry_8x8x8_A191", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1839.2462, 766.11664, 2328.482), (-11.128175186981615, -151.23659309724394, 8.245340572466976), (1.078918, 0.425522, 0.563842), "PWM_Quarry_8x8x8_A192_519", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4241.8066, 2910.55, 2030.0573), (7.055482299919118, 39.100306573662166, -4.111603123635168), (0.636581, 0.508948, 0.329333), "PWM_Quarry_8x8x8_A193_535", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2193.517, 1260.676, 729.3924), (-0.4157716843727893, 125.76796000762705, 9.639569788424025), (0.616174, 1.02416, 0.528219), "PWM_Quarry_8x8x8_A194_538", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1912.4258, 1101.9984, 897.9886), (-11.08807345591325, -137.6878624276123, 2.3654345219149175), (1.22117, 0.56363595, 0.71131766), "PWM_Quarry_8x8x8_A195", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1865.3683, 1182.509, 1699.3972), (-10.992278743135161, -156.47755518911677, 6.544376058673513), (0.933322, 0.425522, 0.61182857), "PWM_Quarry_8x8x8_A196", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2213.4045, 1488.5574, 2013.5509), (-6.97930882411996, -59.271328127351595, -11.354826305277907), (0.31815663, 0.21924767, 0.4179246), "PWM_Quarry_8x8x8_A197_572", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5460.6943, 4254.249, 928.09436), (13.188029699946847, 60.88153676219265, 4.780146291237327), (0.636581, 0.508948, 0.329333), "PWM_Quarry_8x8x8_A198_593", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5463.504, 3992.6248, 889.3385), (-14.401579516760085, -120.18713512031901, -1.0216979810373872), (0.500213, 0.261784, 0.238599), "PWM_Quarry_8x8x8_A199", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4965.7993, 3903.9583, 876.6071), (13.380667361324099, 58.16577948588414, 6.151343216675299), (0.94676006, 0.56194794, 0.61944425), "PWM_Quarry_8x8x8_A2_576", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2887.825, 2644.8962, 1659.4791), (17.214754666559745, 38.84744809636198, 9.989205939301547), (0.487053, 0.399063, 0.251555), "PWM_Quarry_8x8x8_A20", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5022.082, 3517.2104, 740.08276), (14.590977586797534, 60.84776924132434, 4.577450078813732), (0.636581, 0.508948, 0.329333), "PWM_Quarry_8x8x8_A200", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5628.7183, 4723.8784, 902.5734), (-12.182068260386012, -113.54999736605984, 2.6992665371023996), (0.933322, 0.425522, 0.425522), "PWM_Quarry_8x8x8_A201_608", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (6065.041, 4760.833, 2401.9136), (-13.686003138086479, -137.9737079911191, 19.322169349081925), (0.968355, 0.456968, 0.456968), "PWM_Quarry_8x8x8_A202", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5481.251, 4590.6455, 1282.5099), (-13.629578069227662, -123.62304796471822, -0.12643473206719086), (0.933322, 0.425522, 0.563764), "PWM_Quarry_8x8x8_A203", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5904.703, 4272.121, 2459.9602), (9.848737036145687, 33.12622150256169, -12.917906982528176), (1.02025, 0.5175295, 0.47264707), "PWM_Quarry_8x8x8_A204", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5489.6587, 4384.874, 2173.9893), (-15.675903325277389, -132.54345528263718, 7.390320352247563), (1.02025, 0.425522, 0.563764), "PWM_Quarry_8x8x8_A205", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5729.9854, 3720.6218, 2461.393), (6.867046580154989, 25.82531316471392, -6.69085683440546), (1.560089, 0.587846, 0.39661673), "PWM_Quarry_8x8x8_A206", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5448.9224, 4568.8013, 1684.023), (13.691518558581492, 51.39706152649606, -5.422485842421283), (0.933322, 0.425522, 0.6007819), "PWM_Quarry_8x8x8_A207", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (6007.7646, 5312.8174, 1532.5618), (15.58043967323211, 45.869561888134534, -3.991698427340132), (0.933322, 0.425522, 1.0863503), "PWM_Quarry_8x8x8_A208", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (6114.85, 5113.067, 2250.7546), (14.222657129069175, 38.15369041394927, -9.524811984831839), (1.02025, 0.425522, 0.563764), "PWM_Quarry_8x8x8_A209_645", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4431.56, 4585.902, 2320.125), (9.576988950174393, 65.14107072755662, 8.633967062085285), (0.933322, 0.425522, 0.425522), "PWM_Quarry_8x8x8_A21", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5687.008, 4902.082, 2055.5352), (-16.34954505777432, -132.24755564611363, 178.18518434722262), (1.02025, 0.425522, 0.563764), "PWM_Quarry_8x8x8_A210", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1096.8843, 819.2543, 1626.9966), (9.599091946523687, 31.95208018067151, -2.589934959265564), (1.22117, 0.6751788, 0.926511), "PWM_Quarry_8x8x8_A211", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1231.6707, 687.1367, 989.227), (-10.299834797499962, -150.49829099179706, -0.9565733527069558), (1.22117, 0.44399196, 0.926511), "PWM_Quarry_8x8x8_A212", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1387.1003, 733.45935, 776.653), (-11.088073160828362, -137.68786231819576, 2.365433760924314), (1.22117, 0.563636, 0.711318), "PWM_Quarry_8x8x8_A213", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5417.5024, 3974.31, 2323.036), (-10.280092236349915, -146.0524456084386, 2.643629397968991), (0.204809, 0.124901, 0.309656), "PWM_Quarry_8x8x8_A214", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5282.7114, 3913.6536, 2297.7834), (-10.558716750995336, -137.30307365133552, 1.0583630212721757), (0.204809, 0.124901, 0.309656), "PWM_Quarry_8x8x8_A215", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5412.3057, 3907.9143, 2396.572), (10.159936617517035, 31.503133268583483, -3.0773928746161494), (0.3576658, 0.124901, 0.309656), "PWM_Quarry_8x8x8_A216", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5810.691, 4405.8486, 2246.0935), (-11.757384166405796, -142.93605339710967, 11.938368282226318), (0.204809, 0.124901, 0.309656), "PWM_Quarry_8x8x8_A217", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5679.61, 4337.471, 2221.0234), (-13.401792143866706, -134.27572199443208, 10.048019229529523), (0.204809, 0.124901, 0.309656), "PWM_Quarry_8x8x8_A218", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5816.4956, 4329.569, 2309.2656), (11.250244007543222, 34.66387598285541, -12.418824238472983), (0.357666, 0.124901, 0.309656), "PWM_Quarry_8x8x8_A219", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2523.2175, 2845.9282, 2351.2048), (12.815571825657502, 43.304100361005176, 13.598908199397119), (0.68865204, 0.425522, 0.425522), "PWM_Quarry_8x8x8_A22", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (6112.7046, 4543.493, 2347.3018), (11.250244007543222, 34.66387598285541, -12.418824238472983), (0.357666, 0.124901, 0.309656), "PWM_Quarry_8x8x8_A220", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (6305.082, 4683.783, 2377.1528), (-11.757384166405796, -142.93605339710967, 11.938368282226318), (0.204809, 0.124901, 0.309656), "PWM_Quarry_8x8x8_A221", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (475.21277, 2674.7996, 1938.9432), (19.87968484060953, -41.43337880574823, -3.806671096656104), (0.225433, 0.383003, 0.329333), "PWM_Quarry_8x8x8_A222_9", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5654.001, 4520.671, 2001.4358), (-11.388091172114118, -49.36616758797526, -15.518218318693277), (0.204809, 0.2415341, 0.309656), "PWM_Quarry_8x8x8_A223", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5550.786, 4343.5283, 1937.9478), (73.14358602614473, -98.65106680673553, -142.18695999409204), (0.204809, 0.124901, 0.309656), "PWM_Quarry_8x8x8_A224", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5939.572, 4740.025, 2139.947), (12.8428243035934, 36.82717687524724, 168.00835928170932), (0.40628856, 0.124901, 0.309656), "PWM_Quarry_8x8x8_A225", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (376.99503, 2672.7805, 1915.8806), (-20.057555767280398, 141.91920386491233, 2.6615171833681077), (0.31280425, 0.2727036, 0.329333), "PWM_Quarry_8x8x8_A226", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (6122.967, 5079.205, 2019.9729), (12.8428243035934, 36.82717687524724, 168.00835928170932), (0.406289, 0.124901, 0.309656), "PWM_Quarry_8x8x8_A227", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5873.2974, 4762.0796, 1982.6252), (12.8428243035934, 36.82717687524724, 168.00835928170932), (0.34408307, 0.124901, 0.309656), "PWM_Quarry_8x8x8_A228", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5086.897, 3603.928, 2260.6282), (12.179175649796072, 31.226049468257855, 172.4787886736712), (0.203946, 0.124901, 0.309656), "PWM_Quarry_8x8x8_A229", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2694.5217, 3182.3586, 2658.1824), (15.914816135105768, 45.440413638318724, 14.835875599211676), (0.933322, 0.425522, 0.425522), "PWM_Quarry_8x8x8_A23", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5263.4497, 3701.5908, 2293.3591), (12.179175649796072, 31.226049468257855, 172.4787886736712), (0.33427718, 0.124901, 0.309656), "PWM_Quarry_8x8x8_A230", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5490.712, 3880.7864, 2360.1357), (12.179175649796072, 31.226049468257855, 172.4787886736712), (0.17457145, 0.124901, 0.309656), "PWM_Quarry_8x8x8_A231", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4492.2744, 2817.1318, 2481.574), (-11.721646631575906, -153.28604759365777, 3.6882802709953943), (0.933322, 0.425522, 0.425522), "PWM_Quarry_8x8x8_A232", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5716.0854, 3656.8013, 2573.3687), (12.179175331443247, 31.226264926103102, 173.914972619064), (0.334277, 0.19619147, 0.309656), "PWM_Quarry_8x8x8_A233", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4869.5244, 3137.0635, 2412.4102), (12.179175331443247, 31.226264926103102, 173.914972619064), (0.5847745, 0.196191, 0.309656), "PWM_Quarry_8x8x8_A234", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4727.524, 2909.1416, 2386.8125), (12.179175649796072, 31.226049468257855, 172.4787886736712), (0.203946, 0.124901, 0.309656), "PWM_Quarry_8x8x8_A235", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5499.891, 3551.1418, 2559.5388), (12.179175649796072, 31.226049468257855, 172.4787886736712), (0.203946, 0.124901, 0.309656), "PWM_Quarry_8x8x8_A236", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5352.775, 3535.4785, 2514.4883), (-10.134217099800926, -162.14444809279252, -169.87841163162133), (0.203946, 0.124901, 0.309656), "PWM_Quarry_8x8x8_A237", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3889.8645, 2449.5513, 2073.303), (12.179175331443247, 31.226264926103102, 173.914972619064), (0.334277, 0.196191, 0.309656), "PWM_Quarry_8x8x8_A238", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3706.4675, 2344.588, 2057.3684), (12.179175649796072, 31.226049468257855, 172.4787886736712), (0.203946, 0.124901, 0.309656), "PWM_Quarry_8x8x8_A239", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2208.8855, 2805.1814, 2487.0676), (12.633499831772982, 44.54642702939412, 14.616546604015571), (0.933322, 0.425522, 0.425522), "PWM_Quarry_8x8x8_A24", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3589.1492, 2314.4556, 2011.3496), (-9.775967798607056, -152.5561446744712, -172.80140779698664), (0.203946, 0.124901, 0.309656), "PWM_Quarry_8x8x8_A240", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3994.172, 2568.428, 1852.3053), (-9.83813298086095, -163.8042338900649, -169.59081814867514), (0.203946, 0.124901, 0.309656), "PWM_Quarry_8x8x8_A241", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4198.0996, 2627.8528, 1909.5891), (10.453741583591912, 19.70479339998102, 170.2079866918952), (0.379561, 0.124901, 0.309656), "PWM_Quarry_8x8x8_A242", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1733.1232, 1005.9423, 1243.6008), (10.524004446757552, 30.44342042402757, -179.67973237279386), (0.933322, 0.425522, 0.425522), "PWM_Quarry_8x8x8_A243", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3891.9736, 3966.2515, 2331.5232), (-16.091155811214055, -130.11045706640346, -22.957734185130033), (0.43591896, 0.24936146, 0.309656), "PWM_Quarry_8x8x8_A244", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3677.053, 3714.0977, 2352.2246), (-16.091155811214055, -130.11045706640346, -22.957734185130033), (0.435919, 0.249361, 0.309656), "PWM_Quarry_8x8x8_A245", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3705.665, 3750.2627, 2299.0486), (-17.447021767437498, -129.50761805969347, -23.13119459236195), (0.15468024, 0.249361, 0.309656), "PWM_Quarry_8x8x8_A246", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5332.264, 778.45807, 2399.7476), (12.179175601596961, 31.22632073538828, -175.2590971890918), (0.40634713, 0.2550468, 0.309656), "PWM_Quarry_8x8x8_A247_75", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5604.8013, 902.0355, 2322.426), (-4.717956322867511, 120.61297840946276, -167.8108685177692), (0.25769192, 0.255047, 0.309656), "PWM_Quarry_8x8x8_A248_77", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5283.072, 275.2401, 2320.9346), (-3.1011329981078166, 113.27527125061269, -167.30991061305087), (0.406347, 0.5039752, 0.309656), "PWM_Quarry_8x8x8_A249", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2889.8154, 3068.1924, 2508.1135), (-11.237607581073844, -132.95850064410408, -29.627593087598996), (0.688652, 0.425522, 0.425522), "PWM_Quarry_8x8x8_A25", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3964.4883, 2244.6829, 2555.9392), (-7.546752968676663, -158.13643231886445, 7.463467559871219), (0.7927397, 0.425522, 0.563842), "PWM_Quarry_8x8x8_A250", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5335.473, 3167.9082, 2451.4695), (12.179175649796072, 31.226049468257855, 172.4787886736712), (0.334277, 0.31378874, 0.309656), "PWM_Quarry_8x8x8_A251", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5302.849, 575.7582, 2296.1182), (4.265711742118844, -61.476257274913536, 167.64597147552013), (0.258432, 0.301697, 0.309656), "PWM_Quarry_8x8x8_A252_82", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1023.90326, 347.66653, 2342.3118), (-10.257720812207854, -156.96868671518004, 15.668419992704852), (0.72090685, 0.425522, 0.563842), "PWM_Quarry_8x8x8_A253", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1002.46967, 139.94565, 2128.823), (10.792182279157945, 26.45883062306418, -8.68453906246024), (0.5044943, 0.5044943, 0.5044943), "PWM_Quarry_8x8x8_A254", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5352.5757, 217.91968, 2263.6804), (-1.1716315089417344, 104.82446870512454, -166.99003139905193), (0.21332651, 0.24808231, 0.309656), "PWM_Quarry_8x8x8_A255_84", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (190.81676, 2723.6453, 1943.4668), (-20.057555573717938, 141.9192037558486, 2.661517749184964), (0.312804, 0.272704, 0.329333), "PWM_Quarry_8x8x8_A256", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5399.032, 472.73285, 1799.6558), (3.1488954577692234, -66.51445720775125, -12.348020884027354), (0.31947178, 0.18772161, 0.32292995), "PWM_Quarry_8x8x8_A257_88", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5462.921, 263.31262, 1103.8619), (3.1488954577692234, -66.51445720775125, -12.348020884027354), (0.319472, 0.187722, 0.32293), "PWM_Quarry_8x8x8_A258_90", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5431.0254, 422.85416, 1102.6399), (-0.5672312831776236, 101.90929626638741, 12.726714793109338), (0.319472, 0.187722, 0.48116156), "PWM_Quarry_8x8x8_A259_92", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2685.8247, 3166.033, 2469.921), (-11.23745731556228, -132.95850767330833, -16.84338064454814), (0.32067543, 0.2407674, 0.425522), "PWM_Quarry_8x8x8_A26", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2905.5273, 1108.9694, 2726.187), (11.667095663662064, 26.32091960623368, -11.535704943626838), (0.909785, 0.504494, 0.504494), "PWM_Quarry_8x8x8_A260", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2749.1375, 4625.907, 2858.7947), (-13.806213661373507, -85.26391931265898, 2.985016346792695), (0.198738, 0.509634, 0.309656), "PWM_Quarry_8x8x8_A261_125", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2258.9124, 5256.2944, 2291.217), (-1.9178472640113637, -168.2947509656005, -155.0653999884847), (0.933322, 0.425522, 0.428653), "PWM_Quarry_8x8x8_A262_20", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (738.61456, 4176.2915, 2110.9402), (-9.013610261539396, -155.18514815483366, 22.45906074237099), (0.688652, 0.425522, 0.425522), "PWM_Quarry_8x8x8_A263", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (646.7, 4293.3555, 1926.3799), (-13.176118713108348, -144.40257989647205, 20.373153474999118), (0.688652, 0.425522, 0.425522), "PWM_Quarry_8x8x8_A264", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5339.8813, 483.80533, 1084.5632), (3.1488954577692234, -66.51445720775125, -12.348020884027354), (0.319472, 0.187722, 0.32293), "PWM_Quarry_8x8x8_A265_94", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1277.2877, 4795.9, 2398.796), (5.10976019236973, 16.32004966781947, -30.34338441272711), (0.933322, 0.425522, 0.428653), "PWM_Quarry_8x8x8_A266", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1946.1317, 4963.874, 2493.3215), (-67.80189078794005, 97.86042079059943, 12.370102206228188), (0.25437236, 0.9882355, 0.428653), "PWM_Quarry_8x8x8_A267", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5447.855, 861.1518, 1046.131), (-7.324095648721178, -156.37871755854988, -177.35545701051), (0.319472, 0.27305833, 0.32293), "PWM_Quarry_8x8x8_A268_96", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (934.2989, 4342.113, 2351.5537), (-13.109464679401064, -153.1754282530775, 7.511714629908901), (0.590509, 0.887789, 0.469193), "PWM_Quarry_8x8x8_A269", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2836.5422, 3276.4973, 2608.637), (-11.968018028242675, -133.03693458614296, -23.824126975099965), (0.320675, 0.240767, 0.425522), "PWM_Quarry_8x8x8_A27", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5364.4697, 751.6443, 924.5883), (-7.324095648721178, -156.37871755854988, -177.35545701051), (0.319472, 0.273058, 0.32293), "PWM_Quarry_8x8x8_A270_98", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2427.0557, 4812.4165, 2841.3398), (12.076892611671076, 110.3235578244124, 5.801881834354782), (0.48503196, 0.971034, 0.469193), "PWM_Quarry_8x8x8_A271_39", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3716.1672, 5122.4487, 2488.1968), (-8.15093973918341, -171.46911125095, 8.531219619953568), (0.3471311, 0.377543, 0.309656), "PWM_Quarry_8x8x8_A272", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3887.758, 4494.744, 2410.118), (8.302565492053239, 100.73229963845885, 8.384277562541591), (0.347131, 0.377543, 0.309656), "PWM_Quarry_8x8x8_A273", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3935.6665, 4751.969, 2437.3652), (8.377677163427082, 10.07775792825487, -8.309539328250537), (0.347131, 0.377543, 0.36794025), "PWM_Quarry_8x8x8_A274", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3894.4192, 5131.763, 2296.1633), (11.729570253489644, 91.27322129341698, 6.609495704905243), (0.25305295, 0.17428117, 0.22398545), "PWM_Quarry_8x8x8_A275", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3988.3987, 4955.9346, 2287.9207), (-3.2853388536543413, 165.48680653595343, 13.042080681194186), (0.253053, 0.174281, 0.223985), "PWM_Quarry_8x8x8_A276", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4242.749, 4917.617, 2187.412), (-2.8495482327204136, 163.61035859994666, 13.142853618074305), (0.253053, 0.43380532, 0.223985), "PWM_Quarry_8x8x8_A277", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4599.0244, 5199.323, 2142.273), (13.302536124700108, 86.42802617813602, -162.14026397648308), (0.832896, 0.412389, 0.25518933), "PWM_Quarry_8x8x8_A278", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4544.5894, 5090.788, 2054.451), (14.743527677968016, 83.04079798575265, 2.8689568004774197), (0.204809, 0.124901, 0.309656), "PWM_Quarry_8x8x8_A279", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2312.0054, 2651.237, 2288.5442), (-14.159821197397996, -138.34958401341214, -28.440948439699735), (0.2648947, 0.18498674, 0.3697417), "PWM_Quarry_8x8x8_A28", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2808.2952, 4841.0312, 2590.3396), (-10.183380143561717, -159.6881707424333, 8.822876016955986), (0.253053, 0.433805, 0.223985), "PWM_Quarry_8x8x8_A280", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2719.235, 4928.9297, 2610.6711), (-7.287627490403379, -60.75219802623814, -11.327971794993282), (0.253053, 0.433805, 0.223985), "PWM_Quarry_8x8x8_A281", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5629.625, 67.593376, 1037.4937), (3.1488954577692234, -66.51445720775125, -12.348020884027354), (0.23000632, 0.4248134, 0.32293), "PWM_Quarry_8x8x8_A282_100", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3591.6506, 3351.3179, 908.3644), (10.59134676168052, 44.358693602366515, 164.1773564364479), (0.21995762, 0.508948, 0.329333), "PWM_Quarry_8x8x8_A283", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3453.6655, 3250.9072, 800.7389), (10.59134676168052, 44.358693602366515, 164.1773564364479), (0.16066085, 0.44965088, 0.27003586), "PWM_Quarry_8x8x8_A284", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2862.7385, 2822.3003, 791.0906), (13.532706529396028, 22.194454579363853, 162.14461433598348), (0.160661, 0.449651, 0.270036), "PWM_Quarry_8x8x8_A285", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2867.1404, 2895.0532, 789.9988), (-14.71139473813992, -53.67888996983119, 156.2372318448213), (0.160661, 0.23789385, 0.24643816), "PWM_Quarry_8x8x8_A286", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2780.7551, 2832.382, 864.26294), (-10.69332743922663, -44.76239055700609, 154.27221755461164), (0.160661, 0.237894, 0.246438), "PWM_Quarry_8x8x8_A287", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5691.7715, 115.5216, 1163.4706), (12.210781685514053, 26.188631295750962, 3.6515199108987573), (0.2975868, 0.424813, 0.37388536), "PWM_Quarry_8x8x8_A288_102", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5726.4487, 104.701614, 1368.0112), (12.604613027871709, 17.811860656271143, 1.8483583069395584), (0.17964745, 0.26720193, 0.22689897), "PWM_Quarry_8x8x8_A289", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2199.3193, 2475.1082, 2325.159), (-14.159821197397996, -138.34958401341214, -28.440948439699735), (0.264895, 0.184987, 0.369742), "PWM_Quarry_8x8x8_A29", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1038.6915, 495.9338, 1802.2123), (-9.475737403601808, -148.58483459486953, 1.3264771859366935), (1.1176922, 0.425522, 0.83536994), "PWM_Quarry_8x8x8_A290", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1621.1532, 810.7991, 1969.984), (12.726266235409527, 31.510662106048805, -3.199401128654297), (1.1177807, 0.31072965, 0.6327374), "PWM_Quarry_8x8x8_A291_118", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (390.26758, 2815.7373, 2018.038), (0.11010984803306433, 59.344891935738445, 20.226307639081103), (0.12573847, 0.1974299, 0.3360716), "PWM_Quarry_8x8x8_A292", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2134.3452, 1046.6448, 2130.053), (12.179175649796072, 31.226049468257855, 172.4787886736712), (0.203946, 0.124901, 0.309656), "PWM_Quarry_8x8x8_A293_120", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1778.7472, 916.1895, 1676.3965), (12.179175649796072, 31.226049468257855, 172.4787886736712), (0.203946, 0.124901, 0.309656), "PWM_Quarry_8x8x8_A294_122", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2560.5237, 5635.221, 1674.6355), (-74.45161448442865, 72.54946796251339, 17.47785977883512), (0.145001, 0.118775, 0.16098064), "PWM_Quarry_8x8x8_A295", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1867.1749, 1020.5454, 1778.6316), (-8.969178732089363, -65.04356012164602, 168.83580181209186), (0.203946, 0.21861003, 0.309656), "PWM_Quarry_8x8x8_A296_124", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2907.9697, 5476.901, 2158.306), (14.247298357653023, 94.57398130475599, 87.62539951794979), (0.204809, 0.178583, 0.309656), "PWM_Quarry_8x8x8_A297", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (873.5602, 2389.6548, 2251.599), (-15.169247658287933, 140.36832048736707, 179.99925541134277), (1.055581, 0.9123608, 0.4787857), "PWM_Quarry_8x8x8_A298_127", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (583.6578, 3948.8413, 2350.989), (16.408251340986617, 37.81775313949752, 178.30566841458221), (1.2033169, 1.0600969, 0.5561439), "PWM_Quarry_8x8x8_A299", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4712.024, 5783.9395, 1405.6763), (0.0, 1.3377792966555622, -0.0), (1.0, 0.6573281, 1.0), "PWM_Quarry_8x8x8_A3_5", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1842.7335, 2258.304, 2147.4507), (-14.159821197397996, -138.34958401341214, -28.440948439699735), (0.1842959, 0.184987, 0.369742), "PWM_Quarry_8x8x8_A30", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3412.565, 4119.869, 2904.2708), (-6.85162401511845, -79.56024466273385, 162.82881084302525), (1.392374, 1.249154, 0.68064207), "PWM_Quarry_8x8x8_A300", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2608.097, 3239.2917, 2904.5378), (-17.719268316620838, -131.7187866461976, 174.77109021273475), (1.392374, 1.249154, 1.0), "PWM_Quarry_8x8x8_A301", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (363.28174, 3065.829, 2198.8018), (6.662918133109067, 85.68426161890908, -169.32375818058225), (1.055581, 0.912361, 0.478786), "PWM_Quarry_8x8x8_A302", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2269.3508, 5294.9556, 2109.8699), (-0.014465398069114453, 11.296111721797406, -14.297608385489138), (0.204809, 0.178583, 0.309656), "PWM_Quarry_8x8x8_A303", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2645.418, 4568.6113, 3165.8533), (-2.159301383700341, -50.70549964643862, 168.25650066583748), (1.1588576, 1.0156376, 0.7664834), "PWM_Quarry_8x8x8_A304", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1775.2479, 4807.419, 3003.1123), (0.10492570114301263, -16.50286855166824, 166.9891211733714), (1.158858, 1.015638, 0.766483), "PWM_Quarry_8x8x8_A305", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1171.2002, 4444.912, 2798.6904), (8.172387212733371, 27.613601039162663, 166.8570225193144), (1.158858, 1.015638, 0.5895538), "PWM_Quarry_8x8x8_A306", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2877.1296, 3370.9949, 2987.8872), (-11.797667049255342, -121.52122862595091, 173.62103036092154), (1.158858, 1.015638, 0.766483), "PWM_Quarry_8x8x8_A307", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1462.0568, 2436.9272, 2459.469), (-16.13757004912868, 178.5387435155401, 179.49655173086575), (1.2225996, 1.0793797, 0.38566604), "PWM_Quarry_8x8x8_A308", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1938.4078, 2631.126, 2622.9656), (-18.116790235960615, -149.16682760613227, 174.71706847552196), (1.2226, 0.70302224, 0.699805), "PWM_Quarry_8x8x8_A309", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1951.5758, 2327.4844, 2251.0083), (-14.159821197397996, -138.34958401341214, -28.440948439699735), (0.31309557, 0.184987, 0.369742), "PWM_Quarry_8x8x8_A31", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2367.4185, 3086.2026, 2868.155), (-15.131683242935894, -131.5707971826316, 169.74186694019824), (1.2226, 0.703022, 0.699805), "PWM_Quarry_8x8x8_A310", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1157.7064, 3898.1604, 2696.1523), (6.219054954747395, 83.21622293528031, -167.68535913854572), (1.2226, 1.07938, 0.7436943), "PWM_Quarry_8x8x8_A311", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3319.282, 3802.1726, 2905.9805), (-10.130064533357992, -98.11534294355604, 173.6505554548814), (1.158858, 1.015638, 0.766483), "PWM_Quarry_8x8x8_A312", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3675.8582, 3961.6267, 2720.993), (-10.904753049073006, -111.93982670700021, 166.1605596240816), (1.158858, 1.015638, 0.34768015), "PWM_Quarry_8x8x8_A313_116", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3463.6243, 4791.511, 2862.3955), (-2.159301383700341, -50.70549964643862, 168.25650066583748), (1.5059973, 1.015638, 0.766483), "PWM_Quarry_8x8x8_A314", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3739.3462, 4608.213, 2779.4824), (-7.430786290430431, -78.5191049619456, 166.7491281874703), (1.1737622, 0.9536727, 0.70451766), "PWM_Quarry_8x8x8_A315", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3725.4448, 5018.088, 2732.9463), (-3.4572136305865113, -62.62817008346535, 165.23042529944584), (1.0067843, 0.72763336, 0.65955126), "PWM_Quarry_8x8x8_A316", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (530.11523, 3272.032, 2415.9604), (-9.912350869161584, -92.88133362172023, 167.70404489195306), (1.1262459, 0.9830258, 0.7338718), "PWM_Quarry_8x8x8_A317_129", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (561.32324, 4299.2173, 2271.9067), (-14.801086931415593, -144.63379561317373, 179.17851259071588), (1.126246, 0.983026, 0.733872), "PWM_Quarry_8x8x8_A318", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (504.63528, 4036.0757, 2159.917), (-8.931487567623831, -151.27817780438482, 178.8799739920637), (1.126246, 0.983026, 0.45816457), "PWM_Quarry_8x8x8_A319", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1809.0697, 2471.6772, 2287.529), (-16.43331578081179, -144.382504570511, -17.820187280727538), (0.933322, 0.425522, 0.425522), "PWM_Quarry_8x8x8_A32", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4886.1, 2809.325, 3039.4683), (0.2655918016141301, 11.39913315935536, 173.81244949106562), (1.392374, 1.249154, 1.0), "PWM_Quarry_8x8x8_A320_20", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1425.3496, 2807.3574, 2498.1238), (-10.01309276020957, 155.68425543792594, -170.49204410530314), (1.2226, 1.07938, 0.385666), "PWM_Quarry_8x8x8_A321_334", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1584.2651, 806.72473, 1623.8013), (-8.725797486294136, -63.80666890024519, 168.64540344064073), (0.203946, 0.34599817, 0.309656), "PWM_Quarry_8x8x8_A322_126", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3043.674, 1905.8062, 2324.6584), (-8.969178732089363, -65.04356012164602, 168.83580181209186), (0.203946, 0.21861, 0.309656), "PWM_Quarry_8x8x8_A323_128", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2990.0269, 1533.4015, 2464.838), (7.227991301013846, 123.38830307617188, -167.6446518804255), (0.203946, 0.37480026, 0.309656), "PWM_Quarry_8x8x8_A324_130", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1957.7388, 937.226, 2448.5198), (11.015065609041736, 31.281090263668762, 179.1499612173672), (1.392374, 1.249154, 0.63773423), "PWM_Quarry_8x8x8_A325_61", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1284.4176, 527.46936, 2364.567), (9.093621727255137, 0.7898224950681801, 173.50023339433676), (1.392374, 1.249154, 0.5079264), "PWM_Quarry_8x8x8_A326_63", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (6120.9004, 961.00836, 2538.7324), (13.942572209740922, 31.37718403133584, -175.22497809772653), (0.8419805, 0.6906803, 0.74528927), "PWM_Quarry_8x8x8_A327", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5829.9033, 3603.6665, 2563.6968), (-6.957305133087768, -44.93682020150604, 173.34233218253095), (1.392374, 1.249154, 0.4345457), "PWM_Quarry_8x8x8_A328", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2785.4485, 1402.5638, 2438.5608), (7.227991301013846, 123.38830307617188, -167.6446518804255), (0.203946, 0.21027984, 0.309656), "PWM_Quarry_8x8x8_A329_132", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1504.2667, 5940.9146, 1288.4412), (-1.739959528858015, -16.942167752743877, -11.007536850122317), (0.971097, 0.62401, 1.0), "PWM_Quarry_8x8x8_A33", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1457.9269, 2984.434, 2742.948), (10.800827339192724, -19.295253279487284, 171.3993828032249), (1.2226, 1.07938, 0.73722327), "PWM_Quarry_8x8x8_A330", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5661.511, 2127.111, 2769.763), (-2.952453219929251, -53.490811141466004, -178.3926462267891), (1.3348511, 1.1916311, 0.413199), "PWM_Quarry_8x8x8_A331", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1054.4626, 375.81113, 1339.0636), (12.179174366938877, 31.226485778498585, -177.4268703747374), (0.26250148, 0.18345648, 0.3682115), "PWM_Quarry_8x8x8_A332_136", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1833.8079, 4539.803, 2898.4695), (13.242751391851959, 3.336634175404289, 176.17337226557822), (1.2226, 1.07938, 0.385666), "PWM_Quarry_8x8x8_A333_337", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5812.687, 4614.917, 796.6462), (13.95843462513724, 45.916173305605405, 1.248940675926584), (0.8783975, 0.7403474, 0.329333), "PWM_Quarry_8x8x8_A334_171", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2162.7769, 4328.3125, 2846.834), (3.143101896449129, -34.191163826250424, 168.8767475900797), (0.98287493, 0.83965504, 0.4197524), "PWM_Quarry_8x8x8_A335", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (829.89777, 3383.8772, 2436.0925), (5.5416941351362485, 86.29345987641398, -167.36952513211867), (1.2226, 1.07938, 0.385666), "PWM_Quarry_8x8x8_A336", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (6329.3105, 5386.924, 2041.5394), (15.200961473754187, 36.31284833433672, 167.99597792200578), (0.27765328, 0.20662344, 0.39137846), "PWM_Quarry_8x8x8_A337_174", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3923.923, 1941.0262, 2797.0046), (5.327813856823529, -13.243501818743225, 174.2694334491408), (1.4163573, 1.249154, 0.480295), "PWM_Quarry_8x8x8_A338_110", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3555.6157, 2214.269, 2661.996), (6.7907108697628455, 4.117126844047758, 176.11577496026362), (1.416357, 1.249154, 0.480295), "PWM_Quarry_8x8x8_A339_112", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1393.5271, 1468.3069, 1138.391), (-9.725281125323603, -126.28936850785202, -8.456481809677994), (0.8650205, 0.42005134, 0.8650205), "PWM_Quarry_8x8x8_A34_65", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1102.8949, 811.33386, 2154.0642), (10.798608733451873, 9.54910101146859, 177.12748770379935), (1.416357, 1.249154, 0.480295), "PWM_Quarry_8x8x8_A340_114", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5239.8057, 3139.0696, 2624.4658), (-3.0035093431829067, -16.211453825147508, 179.73567145800956), (1.3050994, 0.798221, 0.39252058), "PWM_Quarry_8x8x8_A341", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2673.0596, 1559.6558, 2610.2034), (11.157339462457308, 21.72149290743722, 179.45341880457397), (1.416357, 1.249154, 0.480295), "PWM_Quarry_8x8x8_A342", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1313.5746, 284.65677, 2160.6616), (12.374675481991064, 25.345636271183945, -178.67837029993345), (0.35085714, 0.37133738, 0.368212), "PWM_Quarry_8x8x8_A343", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (873.45514, 175.23926, 1891.4845), (-12.192989569880162, -149.04515852106513, 177.48452509644426), (0.350857, 0.371337, 0.368212), "PWM_Quarry_8x8x8_A344", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1048.1692, 309.60886, 1960.2736), (-10.578858576205244, -149.1166014553903, 177.49873001814063), (0.27204308, 0.371337, 0.368212), "PWM_Quarry_8x8x8_A345", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (798.9696, 171.53952, 1614.4366), (-2.598389058648142, 128.08737612391843, -169.48886534916957), (0.29762283, 0.31682482, 0.368212), "PWM_Quarry_8x8x8_A346", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (957.2366, 74.925354, 1985.027), (-12.192989569880162, -149.04515852106513, 177.48452509644426), (0.272043, 0.19167006, 0.368212), "PWM_Quarry_8x8x8_A347", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (890.225, 184.12868, 1793.1222), (-12.192989569880162, -149.04515852106513, 177.48452509644426), (0.272043, 0.19167, 0.368212), "PWM_Quarry_8x8x8_A348", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1978.6359, 112.49694, 2397.2107), (-12.290127384516426, -151.58194340968083, 178.02239019720875), (0.43651414, 0.371337, 0.368212), "PWM_Quarry_8x8x8_A349", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1301.8818, 2309.4001, 2126.18), (13.958516603708928, 42.03335668972228, 28.533754392023496), (0.2048089, 0.12490089, 0.30965587), "PWM_Quarry_8x8x8_A35", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1664.3048, 9.728259, 2391.1377), (12.434654429034394, 16.721834113533795, 179.4650237526011), (0.58273584, 0.32916752, 0.368212), "PWM_Quarry_8x8x8_A350", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2489.9019, 148.2417, 2404.9294), (2.574653347218352, 0.300965915850765, -12.304411678525549), (0.77640545, 0.371337, 0.368212), "PWM_Quarry_8x8x8_A351", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (710.7073, 67.90406, 1548.7618), (-14.376219219085199, -132.49359020263117, 174.12542396847806), (0.179472, 0.183456, 0.368212), "PWM_Quarry_8x8x8_A352", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (787.0852, -64.94851, 2178.457), (-14.64880066895771, -163.3984274363634, -174.1104745224594), (0.179472, 0.183456, 0.368212), "PWM_Quarry_8x8x8_A353", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1311.8348, 532.50653, 780.4196), (-12.192989569880162, -149.04515852106513, 177.48452509644426), (0.272043, 0.371337, 0.368212), "PWM_Quarry_8x8x8_A354", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1222.373, 332.62027, 825.3845), (-12.192989569880162, -149.04515852106513, 177.48452509644426), (0.159264, 0.258558, 0.25543305), "PWM_Quarry_8x8x8_A355", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (944.1605, 185.13968, 1144.6105), (-12.192989569880162, -149.04515852106513, 177.48452509644426), (0.159264, 0.258558, 0.255433), "PWM_Quarry_8x8x8_A356", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1611.6469, 661.0289, 798.15546), (-12.192989569880162, -149.04515852106513, 177.48452509644426), (0.272043, 0.371337, 0.22312903), "PWM_Quarry_8x8x8_A357", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1781.8961, 747.8715, 839.9457), (-12.192989569880162, -149.04515852106513, 177.48452509644426), (0.2233987, 0.371337, 0.3111683), "PWM_Quarry_8x8x8_A358", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2102.174, 1119.591, 1897.8025), (-12.328216277947035, -147.60430982113718, -172.72668916091757), (0.203946, 0.21861, 0.309656), "PWM_Quarry_8x8x8_A359", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2529.45, 2775.9355, 2172.6345), (13.958515607181505, 42.03350631566875, 21.182160922514804), (0.204809, 0.124901, 0.309656), "PWM_Quarry_8x8x8_A36", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2194.776, 1208.8127, 2000.4723), (-12.328218871763017, -147.60375523546026, -175.1648079396526), (0.22428453, 0.21861, 0.309656), "PWM_Quarry_8x8x8_A360", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2746.004, 1835.1956, 2326.8132), (-12.328218871763017, -147.60375523546026, -175.1648079396526), (0.224285, 0.21861, 0.309656), "PWM_Quarry_8x8x8_A361", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2405.7878, 1612.731, 2305.305), (-12.328218871763017, -147.60375523546026, -175.1648079396526), (0.40746015, 0.21861, 0.309656), "PWM_Quarry_8x8x8_A362", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5654.0444, 169.91188, 1582.9185), (12.705262984758486, 5.267547676548141, -8.751433918186233), (0.230006, 0.424813, 0.32293), "PWM_Quarry_8x8x8_A363", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5605.219, 154.09079, 1851.2831), (-7.092528825204392, -90.37975849715696, -16.54882859231268), (0.230006, 0.424813, 0.4780973), "PWM_Quarry_8x8x8_A364", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5482.8384, 162.26552, 2342.2188), (12.705262984758486, 5.267547676548141, -8.751433918186233), (0.3609068, 0.424813, 0.32293), "PWM_Quarry_8x8x8_A365", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5451.776, 257.04703, 2125.1494), (-2.2528691945619888, -89.9979851176272, 167.1324701457199), (0.19460696, 0.248082, 0.44238356), "PWM_Quarry_8x8x8_A366", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5566.6196, 729.1797, 1938.5913), (-21.684935236006886, -161.86993526788788, 171.80799046324498), (0.319472, 0.273058, 0.32293), "PWM_Quarry_8x8x8_A367", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5594.056, 837.5484, 2169.435), (18.428809591325678, 27.258292747788236, -168.5312905021255), (0.319472, 0.273058, 0.32293), "PWM_Quarry_8x8x8_A368", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (6285.9585, 4535.2905, 2407.1348), (15.200962301947927, 36.31285345206973, 170.9580008773114), (0.277653, 0.34467062, 0.21969329), "PWM_Quarry_8x8x8_A369_178", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2621.544, 2871.734, 2250.932), (18.64441434016283, 28.098356898476855, 17.24975591731338), (0.204809, 0.124901, 0.309656), "PWM_Quarry_8x8x8_A37", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4103.7725, 445.28345, 2578.7625), (-1.6413878906066595, -3.170837371692139, 164.576780919463), (0.88893217, 1.0494605, 0.437242), "PWM_Quarry_8x8x8_A370_168", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (6301.2705, 4206.297, 2473.056), (15.200962301947927, 36.31285345206973, 170.9580008773114), (0.277653, 0.35360909, 0.3108102), "PWM_Quarry_8x8x8_A371", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (6060.3853, 4026.2063, 2473.973), (11.817113933256554, 116.39780237395682, -174.5056634365165), (0.277653, 0.5259893, 0.391378), "PWM_Quarry_8x8x8_A372", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3536.8682, 1976.4008, 2418.6987), (-12.328218871763017, -147.60375523546026, -175.1648079396526), (0.4158074, 0.21861, 0.309656), "PWM_Quarry_8x8x8_A373_183", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3245.26, 2390.315, 816.55865), (-10.68197721481899, -55.218018488650735, 163.04801930014509), (0.160661, 0.237894, 0.246438), "PWM_Quarry_8x8x8_A374", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3176.846, 2497.5825, 740.5291), (-10.68197721481899, -55.218018488650735, 163.04801930014509), (0.160661, 0.237894, 0.246438), "PWM_Quarry_8x8x8_A375", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3145.2053, 2307.0986, 1208.1082), (-7.260316444397467, -55.77078198766149, 170.95506335734726), (0.160661, 0.237894, 0.246438), "PWM_Quarry_8x8x8_A376", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3089.2834, 2417.236, 1211.371), (10.367707132584336, 99.44089011501461, -174.81244055841606), (0.160661, 0.237894, 0.246438), "PWM_Quarry_8x8x8_A377", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3787.587, 5284.4316, 2337.5266), (1.801565460577142, 172.53008485658324, 12.62390054426832), (0.253053, 0.433805, 0.29070756), "PWM_Quarry_8x8x8_A378", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5460.355, 1099.0134, 2849.099), (-6.73712228222844, -93.60065483098056, -177.11252668331161), (1.392374, 1.249154, 0.470722), "PWM_Quarry_8x8x8_A379", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3320.4458, 3476.474, 2591.329), (16.000967176339994, 45.4869574533985, 23.92370573561822), (0.96835494, 0.45696753, 0.45696753), "PWM_Quarry_8x8x8_A38", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5181.06, 339.90747, 2561.7827), (1.389171514923308, -171.19083896610238, -172.80336779633888), (1.392374, 1.249154, 0.470722), "PWM_Quarry_8x8x8_A380_316", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5831.1685, 2991.39, 2630.6343), (-0.813598464275954, -32.91457598894171, -179.3905118427263), (1.392374, 1.249154, 0.470722), "PWM_Quarry_8x8x8_A381_293", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5994.2793, 1302.7415, 2796.5415), (-3.0609437955773156, -101.07613494760062, -170.80443082674137), (1.392374, 1.249154, 0.57233465), "PWM_Quarry_8x8x8_A382", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (6108.2983, 2259.9546, 2724.879), (-7.012757056696223, -87.26727439038171, -177.8713106866681), (1.392374, 1.249154, 0.470722), "PWM_Quarry_8x8x8_A383", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (6312.6436, 1394.8784, 2631.8018), (14.617260905913048, 5.260667145727798, 178.22612879966263), (0.841981, 0.5863607, 0.58399886), "PWM_Quarry_8x8x8_A384", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5881.3667, 1230.5347, 2548.335), (14.09022296424114, 29.461213657548594, -175.68914755311695), (0.61309904, 0.41760612, 0.4152441), "PWM_Quarry_8x8x8_A385", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5672.738, 986.9447, 2521.9336), (13.847730347187701, 32.5260539629596, -174.94862204607725), (0.42731816, 0.417606, 0.415244), "PWM_Quarry_8x8x8_A386", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5512.8506, 957.8473, 2572.4282), (-4.049772795872294, 117.8866656933288, -165.8328799741835), (0.427318, 0.417606, 0.415244), "PWM_Quarry_8x8x8_A387", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (6078.417, 1083.4946, 2361.5203), (-14.69717293723929, -164.25347367878928, 179.11394487143133), (0.427318, 0.417606, 0.415244), "PWM_Quarry_8x8x8_A388", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (6057.306, 885.08185, 2126.288), (14.62782570763127, 18.890297862205177, -178.3179029793711), (0.36520973, 0.33275256, 0.33039054), "PWM_Quarry_8x8x8_A389", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3682.01, 3429.168, 2199.833), (14.166448962319258, 46.96604025791066, 19.60849227837464), (0.933322, 0.425522, 0.56376386), "PWM_Quarry_8x8x8_A39", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (6225.204, 1019.25745, 2116.461), (-0.6719970316724946, -67.45950347075267, 164.15349524618068), (0.259589, 0.332753, 0.330391), "PWM_Quarry_8x8x8_A390", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (6181.262, 935.8795, 1947.1976), (15.687516888691862, 16.235069199583993, 177.63815196763855), (0.1822897, 0.2554538, 0.25309175), "PWM_Quarry_8x8x8_A391", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5265.5093, 884.08606, 2557.017), (-13.048123836025844, -168.00850387728508, 179.49760371632794), (0.258432, 0.301697, 0.309656), "PWM_Quarry_8x8x8_A392_307", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5108.1367, 543.6762, 2480.1982), (-13.048123836025844, -168.00850387728508, 179.49760371632794), (0.258432, 0.301697, 0.309656), "PWM_Quarry_8x8x8_A393", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5118.548, 320.9641, 2384.5623), (-11.817901126279315, -168.01940669588626, 179.49995347385547), (0.4831722, 0.51710373, 0.309656), "PWM_Quarry_8x8x8_A394", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (6227.1274, 1815.7794, 2551.9895), (-4.85790892036051, -96.61258982585043, 166.0840917635922), (0.6848334, 0.586361, 0.45326436), "PWM_Quarry_8x8x8_A395", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5837.031, 1350.5447, 2683.8782), (-14.153438452593651, 175.9181457344204, -175.89978805486834), (0.413355, 0.586361, 0.453264), "PWM_Quarry_8x8x8_A396", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5585.2134, 1122.8533, 2839.8704), (-4.049772795872294, 117.8866656933288, -165.8328799741835), (0.50326025, 1.0844986, 0.49118623), "PWM_Quarry_8x8x8_A397_329", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4528.708, 1925.9912, 2858.097), (0.26340615517168253, -10.805908248731434, 176.62561691664632), (1.392374, 1.249154, 0.470722), "PWM_Quarry_8x8x8_A398", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4264.12, 957.6804, 2833.235), (5.865520851767279, 136.9941652205341, -173.37506363213856), (1.392374, 1.249154, 0.470722), "PWM_Quarry_8x8x8_A399", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5049.583, 4945.0864, 1405.566), (-4.171569357553672, -141.08614505454432, 7.06972450750051), (1.0, 0.657328, 1.0), "PWM_Quarry_8x8x8_A4", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4152.208, 3935.0637, 2345.609), (10.750443333562039, 56.53407374758743, 7.112556008983897), (0.933322, 0.425522, 0.425522), "PWM_Quarry_8x8x8_A40", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3421.8286, 1030.9934, 2706.3523), (2.152465545945969, 13.995518262013125, 167.06983742838656), (1.392374, 1.249154, 0.470722), "PWM_Quarry_8x8x8_A400", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2594.654, 845.6338, 2586.5215), (11.765205072523392, 60.38491882111976, 173.59056196047612), (1.392374, 1.249154, 0.470722), "PWM_Quarry_8x8x8_A401", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4574.4478, 250.0365, 2518.6438), (2.5746526631174724, 0.3009659894709266, -12.304411675430396), (0.776405, 0.6262453, 0.368212), "PWM_Quarry_8x8x8_A402", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3156.6213, 466.61383, 2597.3206), (-1.6413878906066595, -3.170837371692139, 164.576780919463), (2.5094392, 1.06619, 0.437242), "PWM_Quarry_8x8x8_A403", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (6377.024, 2991.3848, 2597.922), (1.0343569897352813, 178.04162813943123, -176.2896099339975), (0.413355, 0.586361, 0.453264), "PWM_Quarry_8x8x8_A404", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (6282.1064, 2245.6113, 2568.0898), (-1.1531689237330238, 106.65199580810497, -165.31877151537037), (0.7888993, 0.586361, 0.453264), "PWM_Quarry_8x8x8_A405", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (6343.2993, 2702.1921, 2566.331), (-2.6314386415166195, -87.80978893416044, 165.50500638204892), (1.1876866, 0.7022964, 0.453264), "PWM_Quarry_8x8x8_A406", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1995.933, 3703.5955, 2888.3062), (-10.704955740316295, 160.05184759859094, -171.27489027678405), (0.982875, 0.839655, 0.145941), "PWM_Quarry_8x8x8_A407_347", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2473.9717, 5325.6353, 2149.0056), (-0.014465398069114453, 11.296111721797406, -14.297608385489138), (0.204809, 0.178583, 0.309656), "PWM_Quarry_8x8x8_A408", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3164.4685, 5099.8657, 2532.44), (-0.014465398069114453, 11.296111721797406, -14.297608385489138), (0.204809, 0.178583, 0.309656), "PWM_Quarry_8x8x8_A409", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4158.968, 4242.666, 2179.6018), (11.500043327060453, 53.62799252622454, 6.609008627196868), (0.204809, 0.124901, 0.309656), "PWM_Quarry_8x8x8_A41", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1175.6584, 1438.0188, 1652.538), (-12.473970723680303, -138.31728258460936, -15.96951380912801), (0.683945, 0.508948, 0.5582676), "PWM_Quarry_8x8x8_A410", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1135.6622, 1721.0271, 1869.5786), (14.017423638038037, 35.89688160608195, 14.646435296373822), (0.683945, 0.508948, 0.329333), "PWM_Quarry_8x8x8_A411", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4410.794, 3635.5142, 2171.732), (-14.405581526469616, -126.49131998300751, -7.310791053603404), (0.972909, 0.7025885, 0.238599), "PWM_Quarry_8x8x8_A412", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2534.2104, 6132.6255, 725.6787), (5.185892714716586, 106.43835134087888, -170.17077545004196), (0.8275282, 0.508948, 0.329333), "PWM_Quarry_8x8x8_A413", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2440.9834, 1233.0037, 2231.123), (7.227991301013846, 123.38830307617188, -167.6446518804255), (0.203946, 0.54701924, 0.309656), "PWM_Quarry_8x8x8_A414", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2504.8406, 1480.5583, 2269.2463), (7.227991301013846, 123.38830307617188, -167.6446518804255), (0.203946, 0.547019, 0.309656), "PWM_Quarry_8x8x8_A415", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2715.2322, 2798.4663, 2191.192), (-16.584593517274875, -145.36705457529615, -16.08645522466823), (0.670966, 0.246871, 0.438762), "PWM_Quarry_8x8x8_A42", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4102.615, 4060.3916, 2150.3489), (11.500043327060453, 53.62799252622454, 6.609008627196868), (0.31500098, 0.124901, 0.309656), "PWM_Quarry_8x8x8_A43", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3868.8245, 3722.4163, 2152.1147), (11.500043327060453, 53.62799252622454, 6.609008627196868), (0.204809, 0.124901, 0.309656), "PWM_Quarry_8x8x8_A44", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4337.769, 4424.218, 2109.071), (11.500043327060453, 53.62799252622454, 6.609008627196868), (0.204809, 0.124901, 0.309656), "PWM_Quarry_8x8x8_A45", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3884.1782, 3669.2034, 2004.0757), (11.090683323999736, 57.05343707310064, 7.280304261017994), (0.204809, 0.124901, 0.309656), "PWM_Quarry_8x8x8_A46", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3919.9429, 3568.652, 1831.8895), (-12.09536721586136, -132.1138909589339, -5.434173274555694), (0.204809, 0.124901, 0.309656), "PWM_Quarry_8x8x8_A47", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3917.2668, 3595.739, 1621.6854), (-10.817106196750947, -132.23778385751828, -5.409637442111881), (0.204809, 0.124901, 0.309656), "PWM_Quarry_8x8x8_A48", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3914.584, 3696.2742, 2060.7295), (11.500043327060453, 53.62799252622454, 6.609008627196868), (0.204809, 0.124901, 0.309656), "PWM_Quarry_8x8x8_A49", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1250.3463, 5597.927, 2165.2844), (5.278048636300003, 9.432989440195527, -8.832611043890823), (1.0, 0.3518529, 1.0), "PWM_Quarry_8x8x8_A5_30", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1868.6008, 2354.1816, 2222.3474), (-14.338102745412545, -138.71524742024883, -22.530210829112853), (0.184296, 0.184987, 0.369742), "PWM_Quarry_8x8x8_A50", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4291.3374, 4198.4307, 1003.36566), (10.368826343402649, 60.037620156226616, 5.081131123175832), (1.1077434, 0.425522, 0.425522), "PWM_Quarry_8x8x8_A51_55", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2289.938, 2132.381, 2404.9314), (1.5219771905805566, -51.09395818814462, -14.258910403318906), (0.6139145, 1.0649235, 0.6139145), "PWM_Quarry_8x8x8_A52_101", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2032.3923, 5350.621, 2029.0001), (12.151841763422574, 32.59420592619683, -23.654603680089217), (0.320675, 0.240767, 0.425522), "PWM_Quarry_8x8x8_A53", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4219.222, 4359.72, 2149.6646), (11.500043327060453, 53.62799252622454, 6.609008627196868), (0.204809, 0.124901, 0.309656), "PWM_Quarry_8x8x8_A54", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2933.6177, 5459.9385, 2375.0444), (9.831209165396887, 28.289163686938974, -23.85189498094719), (0.933322, 0.425522, 0.425522), "PWM_Quarry_8x8x8_A55", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3915.439, 4253.371, 2560.8872), (13.09292178393478, 47.0300030960849, 14.005127254237202), (0.933322, 0.425522, 0.563764), "PWM_Quarry_8x8x8_A56_79", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4120.432, 4439.033, 2418.4734), (7.3314634894050315, 73.29579418256165, 12.31890683918048), (0.659206, 0.425522, 0.425522), "PWM_Quarry_8x8x8_A57", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3322.3057, 3681.1577, 2759.6929), (-12.701019740662229, -131.37890756316068, -16.552578842812505), (1.02025, 0.425522, 0.563764), "PWM_Quarry_8x8x8_A58_81", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4195.5283, 4922.7456, 2381.623), (8.377817151575258, 73.52652213813464, 12.350729195904279), (0.659206, 0.425522, 0.425522), "PWM_Quarry_8x8x8_A59_167", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1546.1056, 5524.1523, 2244.066), (-1.0226744999165152, -166.28375805670873, 8.928136152963821), (1.0, 0.70780647, 0.6748745), "PWM_Quarry_8x8x8_A6", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3554.4004, 3640.157, 2486.065), (12.42521310777507, 49.565669769595, 12.469603816061028), (1.02025, 0.425522, 0.563764), "PWM_Quarry_8x8x8_A60", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3852.2402, 6043.6045, 1774.1552), (16.28545162748108, 97.31733606114952, 2.481932867439525), (0.7603997, 0.2525996, 0.3908417), "PWM_Quarry_8x8x8_A61", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3736.933, 5408.053, 2081.996), (14.254595057187732, 90.60045775118957, 4.764220575363769), (0.204809, 0.17858267, 0.309656), "PWM_Quarry_8x8x8_A62", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3797.3044, 5504.4307, 1856.1648), (14.254595057187732, 90.60045775118957, 4.764220575363769), (0.204809, 0.124901, 0.309656), "PWM_Quarry_8x8x8_A63", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3827.3416, 5637.6177, 1796.2941), (14.254595057187732, 90.60045775118957, 4.764220575363769), (0.204809, 0.124901, 0.309656), "PWM_Quarry_8x8x8_A64", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3813.1326, 5764.3564, 1747.7706), (14.254595057187732, 90.60045775118957, 4.764220575363769), (0.204809, 0.124901, 0.309656), "PWM_Quarry_8x8x8_A65", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3854.552, 5281.117, 2133.7568), (14.254595057187732, 90.60045775118957, 4.764220575363769), (0.204809, 0.124901, 0.309656), "PWM_Quarry_8x8x8_A66", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4366.6196, 5057.6577, 2184.0308), (14.254595057187732, 90.60045775118957, 4.764220575363769), (0.204809, 0.124901, 0.309656), "PWM_Quarry_8x8x8_A67", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4264.1133, 5124.7935, 2192.605), (14.254595057187732, 90.60045775118957, 4.764220575363769), (0.204809, 0.124901, 0.309656), "PWM_Quarry_8x8x8_A68", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4155.1123, 5154.3345, 2191.0554), (-2.900603613980243, 172.7917528010409, 14.741514305121873), (0.5534527, 0.124901, 0.309656), "PWM_Quarry_8x8x8_A69", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (677.4731, 5325.6943, 2144.3074), (-1.0226744999165152, -166.28375805670873, 8.928136152963821), (1.0, 0.707806, 0.674874), "PWM_Quarry_8x8x8_A7", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4102.6343, 5108.7163, 2231.6077), (14.122913044163038, 92.16624747032293, 5.148039518588625), (0.19873795, 0.37754285, 0.309656), "PWM_Quarry_8x8x8_A70", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4362.64, 5338.7046, 2177.0186), (14.537988759387307, 86.68904449052845, 3.791441340806096), (0.204809, 0.5567261, 0.309656), "PWM_Quarry_8x8x8_A71", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3417.2283, 5053.323, 2541.863), (12.607409397441796, 105.39863180133983, 8.220154440965008), (0.198738, 0.377543, 0.309656), "PWM_Quarry_8x8x8_A72", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4345.866, 4709.0933, 2176.4019), (11.729570253489644, 91.27322129341698, 6.609495704905243), (0.36880404, 0.33987373, 0.309656), "PWM_Quarry_8x8x8_A73", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4543.7754, 4857.957, 2099.9944), (11.729572448300235, 91.27319397263703, -161.08985177780477), (0.40364966, 0.41238865, 0.34450164), "PWM_Quarry_8x8x8_A74", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4370.446, 4691.966, 2091.1196), (14.254595057187732, 90.60045775118957, 4.764220575363769), (0.204809, 0.124901, 0.309656), "PWM_Quarry_8x8x8_A75", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4337.969, 4873.029, 2134.2852), (79.47928582138483, -116.35939450337088, 153.83129438696682), (0.204809, 0.20472671, 0.309656), "PWM_Quarry_8x8x8_A76", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3140.3052, 4963.765, 2556.2732), (-13.157622912329913, -78.74305142665514, -7.296506109765288), (0.198738, 0.377543, 0.309656), "PWM_Quarry_8x8x8_A77", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2518.7754, 6114.702, 1541.4889), (-13.872679905300373, -93.28796053869108, 8.030425743077714), (0.7604, 0.2526, 0.390842), "PWM_Quarry_8x8x8_A78", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (698.9236, 5204.928, 1777.4855), (11.64009312039098, 93.80242797422386, 5.003257840131925e-06), (0.971097, 0.62400997, 1.0), "PWM_Quarry_8x8x8_A8_41", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2573.5776, 5955.0356, 1810.8157), (13.904718209109989, 86.93920246608884, -7.978089461231613), (0.7604, 0.2526, 0.390842), "PWM_Quarry_8x8x8_A80", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (649.6942, 4488.782, 1720.6716), (-10.774963453394648, -150.7800319733939, 19.339726825908222), (0.688652, 0.425522, 0.425522), "PWM_Quarry_8x8x8_A81_229", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (944.7552, 4536.9736, 2135.417), (14.481729070184805, 27.203848777414517, -23.359407902452546), (0.83120835, 0.425522, 0.425522), "PWM_Quarry_8x8x8_A82_231", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1075.7728, 4807.268, 2028.1635), (12.817764150464413, 33.443204602836005, -13.375610724252383), (1.02025, 0.425522, 0.563764), "PWM_Quarry_8x8x8_A83", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2476.958, 4802.236, 2680.0872), (-13.157622912329913, -78.74305142665514, -7.296506109765288), (0.198738, 0.25078064, 0.309656), "PWM_Quarry_8x8x8_A84", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3539.1438, 5419.101, 2288.4053), (-1.1127319812879846, -168.98639902732572, 24.41624472530947), (0.78859615, 0.425522, 0.425522), "PWM_Quarry_8x8x8_A85", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1926.3767, 5260.847, 2163.9473), (8.145984022759164, 23.07014745290252, -23.943330380306843), (0.933322, 0.425522, 0.425522), "PWM_Quarry_8x8x8_A86", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1913.2054, 5317.6196, 2019.8569), (12.151841763422574, 32.59420592619683, -23.654603680089217), (0.320675, 0.240767, 0.21316624), "PWM_Quarry_8x8x8_A87", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2939.22, 5644.622, 2172.4395), (-5.939910788505559, -162.20848221736279, 26.92681868215756), (0.784787, 0.425522, 0.425522), "PWM_Quarry_8x8x8_A88", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3909.1514, 5054.7915, 2397.913), (9.52138331372804, 91.58709431979298, 6.964690773966121), (0.43565455, 0.377543, 0.309656), "PWM_Quarry_8x8x8_A89_44", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2948.1152, 2770.8096, 1847.2671), (12.16893721798895, 42.016815876558, 4.212436245273268), (0.933322, 0.425522, 0.425522), "PWM_Quarry_8x8x8_A9", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3429.9358, 5789.183, 1988.3966), (-3.312041770499337, -174.62741253745446, 22.759139029800053), (0.86278605, 0.6481402, 0.30358213), "PWM_Quarry_8x8x8_A90_245", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2823.308, 5804.863, 2029.2721), (-3.312132972986068, -174.62597653786145, 24.442955084799618), (0.862786, 0.64814, 0.303582), "PWM_Quarry_8x8x8_A91", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3500.2622, 5583.1094, 2099.3462), (3.481777574645283, 5.745027205019653, -24.422943138165017), (0.788596, 0.425522, 0.425522), "PWM_Quarry_8x8x8_A92", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3489.1313, 5481.003, 2626.6008), (-1.1127013950485707, -168.98622443610998, 23.86695654387172), (1.187127, 0.82405305, 0.82405305), "PWM_Quarry_8x8x8_A93", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2722.5034, 4642.7046, 2834.0808), (-0.4825135771643265, -167.96820198012855, -165.1608360998988), (0.198738, 0.50963366, 0.309656), "PWM_Quarry_8x8x8_A94_123", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3394.6218, 6125.3804, 2051.8945), (-3.3119504582281225, -174.62741278317083, 15.449965186229864), (0.862786, 0.64814, 0.303582), "PWM_Quarry_8x8x8_A95_14", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2931.5847, 5227.5083, 2468.9932), (-1.4594113950744916, -167.599753116612, 24.964664004090164), (0.933322, 0.425522, 0.425522), "PWM_Quarry_8x8x8_A96", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1900.9465, 4727.125, 2760.0283), (7.014372238767973, 20.519706226461828, -24.278167240226637), (1.6123931, 0.425522, 0.708045), "PWM_Quarry_8x8x8_A97_14", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3054.4993, 5480.099, 2151.7546), (14.055224650702531, 90.60982436756235, -2.6380605252632603), (0.204809, 0.178583, 0.309656), "PWM_Quarry_8x8x8_A98", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2698.3735, 5578.4766, 1888.6218), (14.254595057187732, 90.60045775118957, 4.764220575363769), (0.204809, 0.178583, 0.309656), "PWM_Quarry_8x8x8_A99", _folder)
if a: placed += 1
else: skipped += 1

# Batch 13: StaticMesh'PWM_Quarry_Ceilling_Fissure_8x4_A' (1 instances)
_mesh_path = "/Game/Unshippable/Whitebox/Rocks/Meshes/PWM_Quarry_Ceilling_Fissure_8x4_A"
_materials = ['/Game/Environments/ProcTexturing/ProcMaterial_Quarry_Floor_8x4x1']
_folder = "Reconstruction/BD_BB_MiningCamp/Meshes"
a = spawn_static_mesh(_mesh_path, _materials, (4438.658, 5231.6304, 932.9464), (-3.881775310899598, -60.80701336544374, -3.761413597303486), (1.0, 1.0, 1.0), "PWM_Quarry_Ceilling_Fissure_8x4_A_18", _folder)
if a: placed += 1
else: skipped += 1

# Batch 14: StaticMesh'PWM_Quarry_RockDebris_A' (62 instances)
_mesh_path = "/Game/Unshippable/Whitebox/Rocks/Meshes/PWM_Quarry_RockDebris_A"
_materials = ['/Game/Environments/ProcTexturing/ProcMaterial_Quarry_Atlas_5']
_folder = "Reconstruction/BD_BB_MiningCamp/Meshes"
a = spawn_static_mesh(_mesh_path, _materials, (4009.002, 2221.5605, 793.0274), (0.0, -77.0485192521532, 0.0), (2.3282037, 1.9331769, 2.3282037), "PWM_Quarry_RockDebris_A_186", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4007.7756, 2368.362, 794.57904), (0.0, 172.35973933701632, -0.0), (2.328204, 1.933177, 2.328204), "PWM_Quarry_RockDebris_A10", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3253.0364, 2354.575, 792.74115), (0.0, 140.67235210435447, -0.0), (2.328204, 1.933177, 2.328204), "PWM_Quarry_RockDebris_A12", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2880.973, 2876.1624, 790.919), (0.0, 140.67235210435447, -0.0), (2.328204, 1.933177, 2.328204), "PWM_Quarry_RockDebris_A13", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3635.0332, 4209.115, 786.35236), (0.0, 0.0, -0.0), (1.688963, 1.688963, 2.4539254), "PWM_Quarry_RockDebris_A15", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2221.924, 2941.939, 793.33167), (0.0, 0.0, -0.0), (1.4600265, 1.4600265, 1.4600265), "PWM_Quarry_RockDebris_A16_230", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2625.7883, 2991.2773, 793.33167), (0.0, 12.007512399034638, -0.0), (1.709953, 1.709953, 1.709953), "PWM_Quarry_RockDebris_A17", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1658.2152, 2673.7534, 783.8035), (0.0, 45.45967320452339, -0.0), (2.075774, 2.075774, 2.075774), "PWM_Quarry_RockDebris_A18_234", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3931.123, 5132.7363, 790.829), (0.0, 0.0, -0.0), (1.6597843, 1.6597843, 1.6597843), "PWM_Quarry_RockDebris_A19_260", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3881.081, 2495.2832, 793.02734), (0.0, -61.52221823867594, 0.0), (2.328204, 2.328204, 2.328204), "PWM_Quarry_RockDebris_A2", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3771.7234, 4498.8564, 795.0538), (0.0, 96.48388942292219, -0.0), (1.4523985, 1.4523985, 1.4523985), "PWM_Quarry_RockDebris_A20_263", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3732.0652, 4378.806, 793.58246), (0.0, 0.0, -0.0), (1.452399, 1.452399, 2.0615091), "PWM_Quarry_RockDebris_A21", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3338.4604, 3775.8882, 793.1692), (0.0, 55.77457077285671, -0.0), (1.688963, 1.688963, 1.688963), "PWM_Quarry_RockDebris_A22", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2518.1926, 5280.1133, 785.6973), (0.0, -117.96805124540762, 0.0), (2.184258, 2.184258, 2.184258), "PWM_Quarry_RockDebris_A23_271", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1642.7366, 4841.5347, 791.00757), (-1.309417806008351, -117.98890237346367, 0.9280963134121537), (1.5992297, 1.5992297, 1.5992297), "PWM_Quarry_RockDebris_A24", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2030.3263, 5034.822, 786.17523), (0.0, -117.96805124540762, 0.0), (1.5644224, 1.5644224, 1.7160066), "PWM_Quarry_RockDebris_A25", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1449.5424, 4533.611, 791.0076), (5.961160605090724e-08, -117.96778177250724, 1.5760204551039911), (1.8308487, 1.8308487, 1.8308487), "PWM_Quarry_RockDebris_A26", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5575.3965, 3669.6045, 791.47784), (0.0, -98.59502983044074, 0.0), (2.7349415, 2.3399143, 2.7349415), "PWM_Quarry_RockDebris_A27", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5921.7124, 4254.546, 791.47784), (0.0, -139.0529828430782, 0.0), (2.3588352, 1.9638083, 2.3588352), "PWM_Quarry_RockDebris_A28", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4919.378, 2923.1038, 787.641), (0.0, -70.36923383734899, 0.0), (2.37712, 1.982093, 2.37712), "PWM_Quarry_RockDebris_A29", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2848.6467, 1208.0024, 789.83765), (0.0, 28.47792259326325, -0.0), (2.328204, 2.328204, 2.328204), "PWM_Quarry_RockDebris_A3", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4564.5264, 2506.7913, 791.8294), (0.0, -107.15805434568477, 0.0), (2.734941, 2.339914, 2.734941), "PWM_Quarry_RockDebris_A30", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3421.6172, 1949.8826, 790.0686), (0.0, 92.0958178376211, -0.0), (1.7040203, 1.3089933, 1.7040203), "PWM_Quarry_RockDebris_A31", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5131.2476, 3182.1013, 804.0198), (-2.2218019763844303, 0.175210408539786, -2.0674135368912125), (1.7110969, 1.7110969, 1.7110969), "PWM_Quarry_RockDebris_A32_106", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (281.5936, 2895.9155, 792.48737), (0.0, 0.0, -0.0), (1.5451332, 1.5451332, 1.5451332), "PWM_Quarry_RockDebris_A33_109", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (617.18677, 2839.6438, 792.48737), (0.0, -13.363617072100178, 0.0), (1.545133, 1.545133, 1.545133), "PWM_Quarry_RockDebris_A34", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5475.3965, 2969.6045, 791.47784), (0.0, -47.96997168232177, 0.0), (2.0, 2.0, 2.0), "PWM_Quarry_RockDebris_A35", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1962.1755, 2804.2249, 790.1509), (-0.39578248323642906, 20.084638593964012, 0.3602958839431551), (1.545133, 1.545133, 1.545133), "PWM_Quarry_RockDebris_A36_114", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3561.9756, 5547.1484, 802.2678), (2.6650167556032653, -67.67672620488153, -6.460754990794345), (1.3416588, 1.3416588, 1.3416588), "PWM_Quarry_RockDebris_A37", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (922.1179, 4059.747, 794.83154), (-3.3913267048703055, 1.5254339826945512e-08, -0.44567867520157456), (1.2889766, 1.2889766, 1.2395728), "PWM_Quarry_RockDebris_A38_142", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2663.427, 5626.9907, 791.0186), (-0.348968482381599, -117.96540680942337, -0.6573180916339989), (2.184258, 2.184258, 2.184258), "PWM_Quarry_RockDebris_A39", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2282.5767, 828.8022, 802.2467), (-1.1351319797037442, -130.5537007533226, 3.721565651914521), (2.328204, 2.328204, 2.328204), "PWM_Quarry_RockDebris_A4", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2663.427, 6103.05, 793.981), (0.027810007853820585, -41.559966576248634, -0.2326354995708712), (2.184258, 2.184258, 2.184258), "PWM_Quarry_RockDebris_A40_4", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3418.8625, 5889.788, 800.0029), (2.6650167556032653, -67.67672620488153, -6.460754990794345), (1.341659, 1.341659, 1.341659), "PWM_Quarry_RockDebris_A41", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3418.8625, 5889.788, 799.9658), (2.6650167556032653, -67.67672620488153, -6.460754990794345), (1.341659, 1.341659, 1.341659), "PWM_Quarry_RockDebris_A42", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3481.8364, 6151.666, 800.00287), (2.6650167556032653, -67.67672620488153, -6.460754990794345), (1.341659, 1.341659, 1.341659), "PWM_Quarry_RockDebris_A43", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (6075.3965, 1919.6045, 791.47784), (0.0, 109.53011632568743, -0.0), (2.0, 2.0, 2.0), "PWM_Quarry_RockDebris_A44", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (573.37494, 3940.802, 785.3983), (0.0, -117.96805124540762, 0.0), (1.957891, 1.957891, 1.957891), "PWM_Quarry_RockDebris_A45", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (275.44327, 3967.9988, 793.4788), (0.0, -117.96805124540762, 0.0), (1.957891, 1.957891, 1.957891), "PWM_Quarry_RockDebris_A46", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (351.71964, 3021.679, 792.5715), (0.0, -27.968016453577338, 0.0), (1.957891, 1.957891, 1.957891), "PWM_Quarry_RockDebris_A47", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (323.79742, 3691.2568, 792.5715), (0.0, -80.90221617036691, 0.0), (1.4772253, 1.4772253, 1.4772253), "PWM_Quarry_RockDebris_A48", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2558.0818, 2943.3542, 791.29517), (4.051580521815812e-08, -101.69982486720174, -0.9343566947020536), (1.574976, 1.574976, 2.7145596), "PWM_Quarry_RockDebris_A49", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3691.8599, 5214.956, 794.5612), (-0.3644713356892113, 60.27754482749663, -0.847289850532088), (1.0346129, 1.0346129, 1.0346129), "PWM_Quarry_RockDebris_A50", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3280.7048, 3793.5479, 810.80963), (9.083264568602061, -12.70700112625765, 0.10200152297018712), (1.3020039, 1.3020039, 1.7963198), "PWM_Quarry_RockDebris_A51", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4125.3965, 1719.6045, 791.47784), (0.0, 109.53011632568743, -0.0), (2.0, 2.0, 2.0), "PWM_Quarry_RockDebris_A52", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1196.4966, 4160.6587, 794.7704), (0.35010195257332466, -165.2667466170208, 1.7633064841800943), (1.3836308, 1.3836308, 1.3836308), "PWM_Quarry_RockDebris_A53", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4775.3965, 1119.6045, 791.47784), (0.0, -104.21963217236387, 0.0), (2.0, 2.0, 2.0), "PWM_Quarry_RockDebris_A54", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3157.7756, 1668.362, 794.57904), (0.0, -97.64007161191758, 0.0), (2.328204, 1.933177, 2.328204), "PWM_Quarry_RockDebris_A55", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3464.3518, 1709.5449, 797.31165), (0.12660433466699933, -107.15795762818342, 0.4107106903831058), (1.5722249, 1.1771979, 1.5722249), "PWM_Quarry_RockDebris_A56", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2637.983, 919.0611, 802.77826), (-2.9580078654315756, -130.6194873452146, 2.5219174848711634), (1.8880131, 1.8880131, 1.9568048), "PWM_Quarry_RockDebris_A57", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4775.3965, 469.6045, 791.47784), (0.0, -28.282135238772494, 0.0), (2.0, 2.0, 2.0), "PWM_Quarry_RockDebris_A58", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3325.3965, 969.6045, 791.47784), (0.0, -28.282135238772494, 0.0), (2.0, 2.0, 2.0), "PWM_Quarry_RockDebris_A59", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5202.789, 291.97906, 789.9717), (0.0, -53.210782275798216, 0.0), (2.1392274, 2.1392274, 2.1392274), "PWM_Quarry_RockDebris_A6_193", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1875.3965, 369.6045, 791.47784), (0.0, -149.2196278734909, 0.0), (2.0, 2.0, 2.0), "PWM_Quarry_RockDebris_A60", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3150.3965, 3684.6045, 786.47784), (0.0, -149.2196278734909, 0.0), (2.0, 2.0, 2.0), "PWM_Quarry_RockDebris_A61", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2720.3965, 3224.6045, 791.47784), (1.0559132213276343, -19.831821520160915, 0.15985155677922977), (2.0, 2.0, 2.0), "PWM_Quarry_RockDebris_A62", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1550.3965, 4134.6045, 786.47784), (0.0, -149.2196278734909, 0.0), (2.0, 2.0, 2.0), "PWM_Quarry_RockDebris_A63", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1301.3965, 2893.6045, 786.47784), (0.0, -0.258819577654408, 0.0), (2.0, 2.0, 2.0), "PWM_Quarry_RockDebris_A64", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (773.3965, 3084.6045, 786.47784), (0.0, -7.234008714503458, 0.0), (2.0, 2.0, 2.0), "PWM_Quarry_RockDebris_A65", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5003.6016, 916.88116, 789.9717), (0.0, 142.81780179534545, -0.0), (1.7652476, 1.7652476, 1.6944692), "PWM_Quarry_RockDebris_A7", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (6038.259, 1440.7136, 789.9717), (0.0, 177.25464319357596, -0.0), (2.310153, 2.310153, 2.310153), "PWM_Quarry_RockDebris_A8", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5096.313, 1193.4066, 789.9713), (0.0, 104.13539822166895, -0.0), (1.9985658, 1.9985658, 1.8224599), "PWM_Quarry_RockDebris_A9", _folder)
if a: placed += 1
else: skipped += 1

# Batch 15: StaticMesh'PWM_Quarry_RockDebris_C' (12 instances)
_mesh_path = "/Game/Unshippable/Whitebox/Rocks/Meshes/PWM_Quarry_RockDebris_C"
_materials = ['/Game/Environments/ProcTexturing/ProcMaterial_Quarry_RockDebris_A']
_folder = "Reconstruction/BD_BB_MiningCamp/Meshes"
a = spawn_static_mesh(_mesh_path, _materials, (1421.6508, 5711.389, 985.32556), (-5.517272832616643, 1.9937890480666662, -19.16302661263703), (2.3149977, 2.3149977, 2.3149977), "PWM_Quarry_RockDebris_C10_54", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3271.276, 3326.712, 792.1741), (0.0, -154.75074639668713, 0.0), (1.0, 1.0, 1.0), "PWM_Quarry_RockDebris_C11", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4243.211, 4889.398, 801.3534), (0.0, 0.0, -0.0), (1.469126, 1.469126, 1.469126), "PWM_Quarry_RockDebris_C12", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1805.2078, 5597.2974, 957.34106), (-0.8953856520063992, 0.9278275343130562, -12.388488534093275), (1.8118651, 1.8118651, 1.8118651), "PWM_Quarry_RockDebris_C13", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1086.5288, 5282.625, 942.1391), (-7.9824521752046005, 2.3092168260575874, -8.163941607321394), (2.314998, 2.314998, 2.314998), "PWM_Quarry_RockDebris_C14", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3758.4653, 2757.0203, 822.0984), (-2.479125609793039, 142.71512530383552, 5.904254531669971), (1.716078, 1.716078, 1.716078), "PWM_Quarry_RockDebris_C2", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3369.3247, 3233.4316, 792.174), (0.0, 0.0, -0.0), (1.0, 1.0, 1.0), "PWM_Quarry_RockDebris_C3_220", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4452.2295, 3625.0583, 1158.7258), (0.0, 0.0, -0.0), (2.1999562, 2.1999562, 2.1999562), "PWM_Quarry_RockDebris_C5_245", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4802.716, 4174.349, 1181.2053), (0.0, 0.0, -0.0), (2.199956, 2.199956, 2.199956), "PWM_Quarry_RockDebris_C6", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4349.076, 3928.5142, 1166.8347), (11.156666197491404, 4.1469379594078305e-07, -8.229798072276022), (1.4405342, 1.4405342, 1.4405342), "PWM_Quarry_RockDebris_C7_253", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4538.317, 4193.819, 1262.7515), (12.530651626072604, -0.20355212575264023, -13.144561399451385), (1.440534, 1.440534, 1.440534), "PWM_Quarry_RockDebris_C8", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4128.2324, 4755.789, 786.1687), (0.0, 0.0, -0.0), (1.469126, 1.469126, 1.469126), "PWM_Quarry_RockDebris_C9_257", _folder)
if a: placed += 1
else: skipped += 1

# Batch 16: StaticMesh'PWM_Quarry_RockDebris_C' (1 instances)
_mesh_path = "/Game/Unshippable/Whitebox/Rocks/Meshes/PWM_Quarry_RockDebris_C"
_materials = ['/Game/Environments/ProcTexturing/ProcMaterial_Quarry_RockDebris_C']
_folder = "Reconstruction/BD_BB_MiningCamp/Meshes"
a = spawn_static_mesh(_mesh_path, _materials, (2400.6824, 2937.529, 794.9903), (0.0, 0.0, -0.0), (1.0, 1.0, 1.0), "PWM_Quarry_RockDebris_C4_227", _folder)
if a: placed += 1
else: skipped += 1

# ======================================================================
# PHASE 2: ConstructionCatalog  (construction blocks)
# ======================================================================
unreal.log(f"[{BUBBLE_NAME}] Phase 2: Placing construction blocks...")

# Construction blocks use DecoVolume transforms (matched by Name)
_folder = "Reconstruction/BD_BB_MiningCamp/Construction"

# Construction: AB_Mines_Scaffolding_Beam_Panels_3m_3
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Scaffolding
#   Volume: EMorSimpleShape::Empty, BoxExtent: (100.0, 100.0, 100.0)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (2150.0, 2550.0, 1400.0), (-0.0, -89.99999818714215, -0.0), (2.0000, 2.0000, 2.0000), "AB_Mines_Scaffolding_Beam_Panels_3m_3", _folder)
if a: placed += 1
else: skipped += 1

# Construction: AB_Mines_Scaffolding_Beam_Panels_3m_4
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Scaffolding
#   Volume: EMorSimpleShape::Empty, BoxExtent: (100.0, 100.0, 100.0)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (2450.0, 2550.0, 1400.0), (-0.0, -89.99999818714215, -0.0), (2.0000, 2.0000, 2.0000), "AB_Mines_Scaffolding_Beam_Panels_3m_4", _folder)
if a: placed += 1
else: skipped += 1

# Construction: AB_Mines_Scaffolding_Beam_Panels_3m_5
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Scaffolding
#   Volume: EMorSimpleShape::Empty, BoxExtent: (100.0, 100.0, 100.0)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (2150.0, 2650.0, 1400.0), (-0.0, -89.99999818714215, -0.0), (2.0000, 2.0000, 2.0000), "AB_Mines_Scaffolding_Beam_Panels_3m_5", _folder)
if a: placed += 1
else: skipped += 1

# Construction: AB_Mines_Scaffolding_Beam_Panels_3m_6
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Scaffolding
#   Volume: EMorSimpleShape::Empty, BoxExtent: (100.0, 100.0, 100.0)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (2150.0, 2450.0, 1400.0), (-0.0, -89.99999818714215, -0.0), (2.0000, 2.0000, 2.0000), "AB_Mines_Scaffolding_Beam_Panels_3m_6", _folder)
if a: placed += 1
else: skipped += 1

# Construction: AB_Mines_Scaffolding_Beam_Panels_3m_8
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Scaffolding
#   Volume: EMorSimpleShape::Empty, BoxExtent: (100.0, 100.0, 100.0)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (2450.0, 2650.0, 1400.0), (-0.0, -89.99999818714215, -0.0), (2.0000, 2.0000, 2.0000), "AB_Mines_Scaffolding_Beam_Panels_3m_8", _folder)
if a: placed += 1
else: skipped += 1

# Construction: AB_Mines_Scaffolding_Broken_Segment_A_2
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Scaffolding
#   Volume: EMorSimpleShape::Empty, BoxExtent: (100.0, 100.0, 100.0)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (5858.4106, 3797.2454, 807.72845), (4.06758278985286, -36.806368265983274, 9.987741137005466), (2.0000, 2.0000, 2.0000), "AB_Mines_Scaffolding_Broken_Segment_A_2", _folder)
if a: placed += 1
else: skipped += 1

# Construction: AB_Mines_Scaffolding_Foundation_1x1m_3
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Scaffolding
#   Volume: EMorSimpleShape::Empty, BoxExtent: (100.0, 100.0, 100.0)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (4650.0, 2650.0, 800.0), (0.0, 0.0, -0.0), (2.0000, 2.0000, 2.0000), "AB_Mines_Scaffolding_Foundation_1x1m_3", _folder)
if a: placed += 1
else: skipped += 1

# Construction: AB_Mines_Scaffolding_Foundation_1x1m2_5
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Scaffolding
#   Volume: EMorSimpleShape::Empty, BoxExtent: (100.0, 100.0, 100.0)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (3800.0, 5650.0, 1550.0), (0.0, 0.0, -0.0), (2.0000, 2.0000, 2.0000), "AB_Mines_Scaffolding_Foundation_1x1m2_5", _folder)
if a: placed += 1
else: skipped += 1

# Construction: AB_Mines_Scaffolding_Foundation_3x1m_8
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Scaffolding
#   Volume: EMorSimpleShape::Empty, BoxExtent: (100.0, 100.0, 100.0)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (2650.0, 1100.0, 850.0), (0.0, 0.0, -0.0), (2.0000, 2.0000, 2.0000), "AB_Mines_Scaffolding_Foundation_3x1m_8", _folder)
if a: placed += 1
else: skipped += 1

# Construction: AB_Mines_Scaffolding_Foundation_3x1m_Broken_A_5
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Scaffolding
#   Volume: EMorSimpleShape::Empty, BoxExtent: (100.0, 100.0, 100.0)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (4950.0, 3050.0, 1400.0), (0.0, 0.0, -0.0), (2.0000, 2.0000, 2.0000), "AB_Mines_Scaffolding_Foundation_3x1m_Broken_A_5", _folder)
if a: placed += 1
else: skipped += 1

# Construction: AB_Mines_Scaffolding_Foundation_3x1m_Broken_B_8
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Scaffolding
#   Volume: EMorSimpleShape::Empty, BoxExtent: (100.0, 100.0, 100.0)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (4750.0, 2800.0, 1400.0), (0.0, 179.99991120752276, -0.0), (2.0000, 2.0000, 2.0000), "AB_Mines_Scaffolding_Foundation_3x1m_Broken_B_8", _folder)
if a: placed += 1
else: skipped += 1

# Construction: AB_Mines_Scaffolding_Foundation_3x2m2
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Scaffolding
#   Volume: EMorSimpleShape::Empty, BoxExtent: (100.0, 100.0, 100.0)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (2850.0, 1250.0, 850.0), (0.0, 90.00001925454477, -0.0), (2.0000, 2.0000, 2.0000), "AB_Mines_Scaffolding_Foundation_3x2m2", _folder)
if a: placed += 1
else: skipped += 1

# Construction: AB_Mines_Scaffolding_Foundation_3x2m3
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Scaffolding
#   Volume: EMorSimpleShape::Empty, BoxExtent: (100.0, 100.0, 100.0)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (2850.0, 1450.0, 850.0), (0.0, 90.00001925454477, -0.0), (2.0000, 2.0000, 2.0000), "AB_Mines_Scaffolding_Foundation_3x2m3", _folder)
if a: placed += 1
else: skipped += 1

# Construction: AB_Mines_Scaffolding_Foundation_3x2m5
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Scaffolding
#   Volume: EMorSimpleShape::Empty, BoxExtent: (100.0, 100.0, 100.0)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (3850.0, 5600.0, 1250.0), (0.0, 0.0, -0.0), (2.0000, 2.0000, 2.0000), "AB_Mines_Scaffolding_Foundation_3x2m5", _folder)
if a: placed += 1
else: skipped += 1

# Construction: AB_Mines_Scaffolding_Foundation_3x2m6
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Scaffolding
#   Volume: EMorSimpleShape::Empty, BoxExtent: (100.0, 100.0, 100.0)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (1900.0, 2450.0, 1200.0), (0.0, 7.999999990858693e-06, -0.0), (2.0000, 2.0000, 2.0000), "AB_Mines_Scaffolding_Foundation_3x2m6", _folder)
if a: placed += 1
else: skipped += 1

# Construction: AB_Mines_Scaffolding_Foundation_3x3m10
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Scaffolding
#   Volume: EMorSimpleShape::Empty, BoxExtent: (100.0, 100.0, 100.0)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (1950.0, 2300.0, 900.0), (0.0, 0.0, -0.0), (2.0000, 2.0000, 2.0000), "AB_Mines_Scaffolding_Foundation_3x3m10", _folder)
if a: placed += 1
else: skipped += 1

# Construction: AB_Mines_Scaffolding_Foundation_3x3m3
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Scaffolding
#   Volume: EMorSimpleShape::Empty, BoxExtent: (100.0, 100.0, 100.0)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (2550.0, 1300.0, 1150.0), (0.0, 0.0, -0.0), (2.0000, 2.0000, 2.0000), "AB_Mines_Scaffolding_Foundation_3x3m3", _folder)
if a: placed += 1
else: skipped += 1

# Construction: AB_Mines_Scaffolding_Foundation_3x3m6_9
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Scaffolding
#   Volume: EMorSimpleShape::Empty, BoxExtent: (100.0, 100.0, 100.0)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (3900.0, 5600.0, 950.0), (0.0, 0.0, -0.0), (2.0000, 2.0000, 2.0000), "AB_Mines_Scaffolding_Foundation_3x3m6_9", _folder)
if a: placed += 1
else: skipped += 1

# Construction: AB_Mines_Scaffolding_Foundation_3x3m7_16
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Scaffolding
#   Volume: EMorSimpleShape::Empty, BoxExtent: (100.0, 100.0, 100.0)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (1950.0, 2600.0, 900.0), (0.0, 0.0, -0.0), (2.0000, 2.0000, 2.0000), "AB_Mines_Scaffolding_Foundation_3x3m7_16", _folder)
if a: placed += 1
else: skipped += 1

# Construction: AB_Mines_Scaffolding_Foundation_3x3m9
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Scaffolding
#   Volume: EMorSimpleShape::Empty, BoxExtent: (100.0, 100.0, 100.0)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (2250.0, 2600.0, 900.0), (0.0, 0.0, -0.0), (2.0000, 2.0000, 2.0000), "AB_Mines_Scaffolding_Foundation_3x3m9", _folder)
if a: placed += 1
else: skipped += 1

# Construction: AB_Mines_Scaffolding_Foundation_3x3m_Broken_A_2
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Scaffolding
#   Volume: EMorSimpleShape::OrientedBox, BoxExtent: (118.6, 154.8, 149.3)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (5355.901, 4002.1475, 1249.1433), (0.0, 0.0, -0.0), (2.3719, 3.0969, 2.9860), "AB_Mines_Scaffolding_Foundation_3x3m_Broken_A_2", _folder)
if a: placed += 1
else: skipped += 1

# Construction: AB_Mines_Scaffolding_Platform_1x1x2m3_17
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Scaffolding
#   Volume: EMorSimpleShape::Empty, BoxExtent: (100.0, 100.0, 100.0)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (1150.0, 4400.0, 900.0), (0.0, 0.0, -0.0), (2.0000, 2.0000, 2.0000), "AB_Mines_Scaffolding_Platform_1x1x2m3_17", _folder)
if a: placed += 1
else: skipped += 1

# Construction: AB_Mines_Scaffolding_Platform_1x1x2m4_19
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Scaffolding
#   Volume: EMorSimpleShape::Empty, BoxExtent: (100.0, 100.0, 100.0)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (1250.0, 4400.0, 900.0), (0.0, 0.0, -0.0), (2.0000, 2.0000, 2.0000), "AB_Mines_Scaffolding_Platform_1x1x2m4_19", _folder)
if a: placed += 1
else: skipped += 1

# Construction: AB_Mines_Scaffolding_Platform_1x1x3m_13
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Scaffolding
#   Volume: EMorSimpleShape::Empty, BoxExtent: (100.0, 100.0, 100.0)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (2500.0, 2650.0, 1600.0), (0.0, 0.0, -0.0), (2.0000, 2.0000, 2.0000), "AB_Mines_Scaffolding_Platform_1x1x3m_13", _folder)
if a: placed += 1
else: skipped += 1

# Construction: AB_Mines_Scaffolding_Platform_1x1x3m5
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Scaffolding
#   Volume: EMorSimpleShape::Empty, BoxExtent: (100.0, 100.0, 100.0)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (2500.0, 2650.0, 1900.0), (0.0, 0.0, -0.0), (2.0000, 2.0000, 2.0000), "AB_Mines_Scaffolding_Platform_1x1x3m5", _folder)
if a: placed += 1
else: skipped += 1

# Construction: AB_Mines_Scaffolding_Platform_1x3x2m_2
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Scaffolding
#   Volume: EMorSimpleShape::Empty, BoxExtent: (100.0, 100.0, 100.0)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (3650.0, 4050.0, 900.0), (-0.0, -89.99999818714215, -0.0), (2.0000, 2.0000, 2.0000), "AB_Mines_Scaffolding_Platform_1x3x2m_2", _folder)
if a: placed += 1
else: skipped += 1

# Construction: AB_Mines_Scaffolding_Platform_1x3x2m2
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Scaffolding
#   Volume: EMorSimpleShape::Empty, BoxExtent: (100.0, 100.0, 100.0)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (3750.0, 4250.0, 900.0), (0.0, -179.99998633961752, -0.0), (2.0000, 2.0000, 2.0000), "AB_Mines_Scaffolding_Platform_1x3x2m2", _folder)
if a: placed += 1
else: skipped += 1

# Construction: AB_Mines_Scaffolding_Platform_1x3x2m4_18
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Scaffolding
#   Volume: EMorSimpleShape::Empty, BoxExtent: (100.0, 100.0, 100.0)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (950.0, 4300.0, 900.0), (0.0, 0.0, -0.0), (2.0000, 2.0000, 2.0000), "AB_Mines_Scaffolding_Platform_1x3x2m4_18", _folder)
if a: placed += 1
else: skipped += 1

# Construction: AB_Mines_Scaffolding_Platform_1x3x2m5
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Scaffolding
#   Volume: EMorSimpleShape::Empty, BoxExtent: (100.0, 100.0, 100.0)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (1050.0, 4283.492, 900.0), (0.0, 0.0, -0.0), (2.0000, 2.0000, 2.0000), "AB_Mines_Scaffolding_Platform_1x3x2m5", _folder)
if a: placed += 1
else: skipped += 1

# Construction: AB_Mines_Scaffolding_Platform_3x2_2
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Scaffolding
#   Volume: EMorSimpleShape::Empty, BoxExtent: (100.0, 100.0, 100.0)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (4600.0, 2750.0, 1100.0), (0.0, 0.0, -0.0), (2.0000, 2.0000, 2.0000), "AB_Mines_Scaffolding_Platform_3x2_2", _folder)
if a: placed += 1
else: skipped += 1

# Construction: AB_Mines_Scaffolding_Platform_3x3
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Scaffolding
#   Volume: EMorSimpleShape::Empty, BoxExtent: (100.0, 100.0, 100.0)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (4400.0, 2750.0, 1100.0), (0.0, 0.0, -0.0), (2.0000, 2.0000, 2.0000), "AB_Mines_Scaffolding_Platform_3x3", _folder)
if a: placed += 1
else: skipped += 1

# Construction: AB_Mines_Scaffolding_Platform_3x3x2m_2
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Scaffolding
#   Volume: EMorSimpleShape::Empty, BoxExtent: (100.0, 100.0, 100.0)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (2450.0, 1100.0, 900.0), (0.0, 0.0, -0.0), (2.0000, 2.0000, 2.0000), "AB_Mines_Scaffolding_Platform_3x3x2m_2", _folder)
if a: placed += 1
else: skipped += 1

# Construction: AB_Mines_Scaffolding_Platform_3x3x2m10_9
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Scaffolding
#   Volume: EMorSimpleShape::Empty, BoxExtent: (100.0, 100.0, 100.0)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (1200.0, 4600.0, 900.0), (0.0, 0.0, -0.0), (2.0000, 2.0000, 2.0000), "AB_Mines_Scaffolding_Platform_3x3x2m10_9", _folder)
if a: placed += 1
else: skipped += 1

# Construction: AB_Mines_Scaffolding_Platform_3x3x2m2_8
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Scaffolding
#   Volume: EMorSimpleShape::Empty, BoxExtent: (100.0, 100.0, 100.0)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (5100.0, 3500.0, 850.0), (0.0, 0.0, -0.0), (2.0000, 2.0000, 2.0000), "AB_Mines_Scaffolding_Platform_3x3x2m2_8", _folder)
if a: placed += 1
else: skipped += 1

# Construction: AB_Mines_Scaffolding_Platform_3x3x2m3_10
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Scaffolding
#   Volume: EMorSimpleShape::Empty, BoxExtent: (100.0, 100.0, 100.0)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (5100.0, 3500.0, 1050.0), (0.0, 0.0, -0.0), (2.0000, 2.0000, 2.0000), "AB_Mines_Scaffolding_Platform_3x3x2m3_10", _folder)
if a: placed += 1
else: skipped += 1

# Construction: AB_Mines_Scaffolding_Platform_3x3x2m6_19
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Scaffolding
#   Volume: EMorSimpleShape::Empty, BoxExtent: (100.0, 100.0, 100.0)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (5100.0, 3800.0, 1050.0), (0.0, 0.0, -0.0), (2.0000, 2.0000, 2.0000), "AB_Mines_Scaffolding_Platform_3x3x2m6_19", _folder)
if a: placed += 1
else: skipped += 1

# Construction: AB_Mines_Scaffolding_Platform_3x3x2m7_22
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Scaffolding
#   Volume: EMorSimpleShape::Empty, BoxExtent: (100.0, 100.0, 100.0)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (3650.0, 3850.0, 900.0), (0.0, 0.0, -0.0), (2.0000, 2.0000, 2.0000), "AB_Mines_Scaffolding_Platform_3x3x2m7_22", _folder)
if a: placed += 1
else: skipped += 1

# Construction: AB_Mines_Scaffolding_Platform_3x3x2m8_4
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Scaffolding
#   Volume: EMorSimpleShape::Empty, BoxExtent: (100.0, 100.0, 100.0)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (3850.0, 3850.0, 1100.0), (0.0, 0.0, -0.0), (2.0000, 2.0000, 2.0000), "AB_Mines_Scaffolding_Platform_3x3x2m8_4", _folder)
if a: placed += 1
else: skipped += 1

# Construction: AB_Mines_Scaffolding_Platform_3x3x2m9_6
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Scaffolding
#   Volume: EMorSimpleShape::Empty, BoxExtent: (100.0, 100.0, 100.0)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (3950.0, 4250.0, 900.0), (0.0, 0.0, -0.0), (2.0000, 2.0000, 2.0000), "AB_Mines_Scaffolding_Platform_3x3x2m9_6", _folder)
if a: placed += 1
else: skipped += 1

# Construction: AB_Mines_Scaffolding_Platform_3x3x2m_Top_2
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Scaffolding
#   Volume: EMorSimpleShape::Empty, BoxExtent: (100.0, 100.0, 100.0)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (2490.2761, 1377.0751, 2090.4937), (14.94157939897308, 29.82511762566636, 3.662240089317846), (2.0000, 2.0000, 2.0000), "AB_Mines_Scaffolding_Platform_3x3x2m_Top_2", _folder)
if a: placed += 1
else: skipped += 1

# Construction: AB_Mines_Scaffolding_Platform_3x4_6
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Scaffolding
#   Volume: EMorSimpleShape::Empty, BoxExtent: (100.0, 100.0, 100.0)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (4600.0, 2900.0, 1400.0), (0.0, 0.0, -0.0), (2.0000, 2.0000, 2.0000), "AB_Mines_Scaffolding_Platform_3x4_6", _folder)
if a: placed += 1
else: skipped += 1

# Construction: AB_Mines_Scaffolding_Platform_3x5_9
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Scaffolding
#   Volume: EMorSimpleShape::Empty, BoxExtent: (100.0, 100.0, 100.0)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (5100.0, 3950.0, 1250.0), (0.0, 90.0000030488508, -0.0), (2.0000, 2.0000, 2.0000), "AB_Mines_Scaffolding_Platform_3x5_9", _folder)
if a: placed += 1
else: skipped += 1

# Construction: AB_Mines_Scaffolding_Platform_3x6
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Scaffolding
#   Volume: EMorSimpleShape::Empty, BoxExtent: (100.0, 100.0, 100.0)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (4800.0, 3050.0, 1400.0), (0.0, 0.0, -0.0), (2.0000, 2.0000, 2.0000), "AB_Mines_Scaffolding_Platform_3x6", _folder)
if a: placed += 1
else: skipped += 1

# Construction: AB_Mines_Scaffolding_Platform_Pillar_3M_Top_B_2
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Scaffolding
#   Volume: EMorSimpleShape::Empty, BoxExtent: (100.0, 100.0, 100.0)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (2050.0, 2570.0, 1200.0), (0.0, 0.0, -0.0), (2.0000, 2.0000, 2.0000), "AB_Mines_Scaffolding_Platform_Pillar_3M_Top_B_2", _folder)
if a: placed += 1
else: skipped += 1

# Construction: AB_Mines_Scaffolding_Stairs_2M_5
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Scaffolding
#   Volume: EMorSimpleShape::Empty, BoxExtent: (100.0, 100.0, 100.0)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (2850.0, 1050.0, 900.0), (0.0, 90.00001925454477, -0.0), (2.0000, 2.0000, 2.0000), "AB_Mines_Scaffolding_Stairs_2M_5", _folder)
if a: placed += 1
else: skipped += 1

# Construction: AB_Mines_Scaffolding_Stairs_2M2_2
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Scaffolding
#   Volume: EMorSimpleShape::Empty, BoxExtent: (100.0, 100.0, 100.0)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (3600.0, 4250.0, 900.0), (0.0, -179.99998633961752, -0.0), (2.0000, 2.0000, 2.0000), "AB_Mines_Scaffolding_Stairs_2M2_2", _folder)
if a: placed += 1
else: skipped += 1

# Construction: AB_Mines_Scaffolding_Stairs_2M3_5
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Scaffolding
#   Volume: EMorSimpleShape::Empty, BoxExtent: (100.0, 100.0, 100.0)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (1250.0, 4250.0, 900.0), (0.0, 90.0000030488508, -0.0), (2.0000, 2.0000, 2.0000), "AB_Mines_Scaffolding_Stairs_2M3_5", _folder)
if a: placed += 1
else: skipped += 1

# Construction: BP_Mines_Scaffolding_Platform_3X1M_B_2
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Scaffolding
#   Volume: EMorSimpleShape::Empty, BoxExtent: (100.0, 100.0, 100.0)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (5788.8135, 3728.5354, 808.6231), (1.012677882840319, -36.28125411848467, 7.95620009029522), (2.0000, 2.0000, 2.0000), "BP_Mines_Scaffolding_Platform_3X1M_B_2", _folder)
if a: placed += 1
else: skipped += 1

# Construction: BP_Mines_Scaffolding_Post_2M_B_2
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Scaffolding
#   Volume: EMorSimpleShape::OrientedBox, BoxExtent: (36.8, 35.0, 101.3)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (4318.1, 2341.6804, 899.7053), (0.0, 0.0, -0.0), (0.7358, 0.7006, 2.0251), "BP_Mines_Scaffolding_Post_2M_B_2", _folder)
if a: placed += 1
else: skipped += 1

# ======================================================================
# PHASE 3: Breakables + DecoVolumes
# ======================================================================
unreal.log(f"[{BUBBLE_NAME}] Phase 3: Placing breakables and deco volumes...")

_folder = "Reconstruction/BD_BB_MiningCamp/Breakables"

# Breakable Batch 0: BP_DM_Deep_WoodenPlank_A_Breakable (1 instances)
#   BP Class: /Game/LevelDesign/Deco/Deep/BP_DM_Deep_WoodenPlank_A_Breakable
_brk_mesh = "/Game/Art/Assets/Kits/Architecture/Deep/Deep_WoodenPlank_A"
_brk_mats = ['/Game/Art/Assets/Kits/Architecture/Deep/Materials/Deep_WoodTrim/MI_Deep_WoodTrim']
a = spawn_static_mesh(_brk_mesh, _brk_mats, (3332.2583, 1565.4492, 805.7868), (4.752937389671055, 77.54827263552755, 20.569797772304046), (1.0, 1.0, 1.0), "Deep_WoodenPlank_A_50", _folder)
if a: placed += 1
else: skipped += 1

# Breakable Batch 1: BP_DM_Deep_WoodenPlank_B_Breakable (19 instances)
#   BP Class: /Game/LevelDesign/Deco/Deep/BP_DM_Deep_WoodenPlank_B_Breakable
_brk_mesh = "/Game/Art/Assets/Kits/Architecture/Deep/Deep_WoodenPlank_B"
_brk_mats = ['/Game/Art/Assets/Kits/Architecture/Deep/Materials/Deep_WoodTrim/MI_Deep_WoodTrim']
a = spawn_static_mesh(_brk_mesh, _brk_mats, (1320.2443, 4890.911, 1782.448), (9.961430034022582, 24.923277081544793, -0.8804014448193853), (1.0, 1.0, 1.0), "BP_DM_Deep_WoodenPlank_B_Breakable_5", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_brk_mesh, _brk_mats, (3899.4358, 3769.5217, 2005.451), (0.8162031668548712, -120.29684035658997, -1.1104737408306486), (1.0, 1.0, 1.0), "BP_DM_Deep_WoodenPlank_B_Breakable10", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_brk_mesh, _brk_mats, (4279.805, 4242.145, 1998.6481), (0.8162031668548712, -120.29684035658997, -1.1104737408306486), (1.0, 1.0, 1.0), "BP_DM_Deep_WoodenPlank_B_Breakable11", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_brk_mesh, _brk_mats, (3977.141, 3724.1477, 2007.1957), (0.8162303206738207, -120.29629785880348, 178.8892915923959), (1.0, 1.0, 1.0), "BP_DM_Deep_WoodenPlank_B_Breakable12", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_brk_mesh, _brk_mats, (1856.1647, 5139.942, 1886.2402), (9.961430034022582, 24.923277081544793, -0.8804014448193853), (1.0, 1.0, 1.0), "BP_DM_Deep_WoodenPlank_B_Breakable2", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_brk_mesh, _brk_mats, (1282.1053, 4972.4194, 1783.8102), (9.961430034022582, 24.923277081544793, -0.8804014448193853), (1.0, 1.0, 1.0), "BP_DM_Deep_WoodenPlank_B_Breakable3", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_brk_mesh, _brk_mats, (1818.0262, 5221.45, 1887.6027), (9.961485779155176, 24.923609565340488, 179.11967514752146), (1.0, 1.0, 1.0), "BP_DM_Deep_WoodenPlank_B_Breakable4", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_brk_mesh, _brk_mats, (1242.4128, 5057.2495, 1785.2251), (9.961430034022582, 24.923277081544793, -0.8804014448193853), (1.0, 1.0, 1.0), "BP_DM_Deep_WoodenPlank_B_Breakable5_17", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_brk_mesh, _brk_mats, (1778.3333, 5306.2803, 1889.0173), (9.961430034022582, 24.923277081544793, -0.8804014448193853), (1.0, 1.0, 1.0), "BP_DM_Deep_WoodenPlank_B_Breakable6_18", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_brk_mesh, _brk_mats, (1204.2739, 5138.758, 1786.5873), (9.961430034022582, 24.923277081544793, -0.8804014448193853), (1.0, 1.0, 1.0), "BP_DM_Deep_WoodenPlank_B_Breakable7_19", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_brk_mesh, _brk_mats, (1740.1948, 5387.7886, 1890.3798), (9.961485779155176, 24.923609565340488, 179.11967514752146), (1.0, 1.0, 1.0), "BP_DM_Deep_WoodenPlank_B_Breakable8_20", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_brk_mesh, _brk_mats, (4202.099, 4287.5195, 1996.9034), (0.8162031668548712, -120.29684035658997, -1.1104737408306486), (1.0, 1.0, 1.0), "BP_DM_Deep_WoodenPlank_B_Breakable9", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_brk_mesh, _brk_mats, (2073.6387, 4992.046, 800.0024), (0.0, 13.65432959015654, -0.0), (1.0, 1.0, 1.0), "Deep_WoodenPlank_B_26", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_brk_mesh, _brk_mats, (3449.7388, 3603.2947, 1056.941), (57.97396502680879, -4.592469122514239, -173.56585496531972), (1.0, 1.0, 1.0), "Deep_WoodenPlank_B10", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_brk_mesh, _brk_mats, (2192.592, 909.5174, 1062.9434), (-70.56003590519146, -39.83109191250613, 8.826533974534243), (1.0, 1.0, 1.0), "Deep_WoodenPlank_B11", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_brk_mesh, _brk_mats, (2277.2644, 912.4833, 1034.5958), (61.543771756252234, 158.1450709339727, -169.8674162492067), (1.0, 1.0, 1.0), "Deep_WoodenPlank_B12", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_brk_mesh, _brk_mats, (5203.3125, 699.56104, 1062.9434), (-70.55942682417104, -174.17068503661565, 8.827118417012278), (1.0, 1.0, 1.0), "Deep_WoodenPlank_B13", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_brk_mesh, _brk_mats, (5146.256, 636.9287, 1034.5958), (61.54344082727339, 23.806014127697377, -169.8666463691981), (1.0, 1.0, 1.0), "Deep_WoodenPlank_B14", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_brk_mesh, _brk_mats, (3529.639, 3634.7224, 1081.6406), (-66.59938817098788, 158.79762520596913, 10.787741690988266), (1.0, 1.0, 1.0), "Deep_WoodenPlank_B9_165", _folder)
if a: placed += 1
else: skipped += 1

# Breakable Batch 2: BP_DM_Mines_Machine_Whim_Side_Bracket_Breakable (8 instances)
#   BP Class: /Game/LevelDesign/Deco/Mines/BP_DM_Mines_Machine_Whim_Side_Bracket_Breakable
_brk_mesh = "/Game/Art/Assets/Kits/Deco/Mines/Machine/Mines_Machine_Whim_Pieces/Mines_Machine_Whim_Side_Bracket"
_brk_mats = ['/Game/Art/Assets/Kits/Deco/Mines/Materials/Mines_Machine_Whim/MI_Mines_Machine_Whim_Trim', '/Game/Art/Assets/Kits/Deco/Mines/Materials/Mines_Machine_Whim/MI_Mines_Machine_Whim_Uniq']
a = spawn_static_mesh(_brk_mesh, _brk_mats, (4229.5273, 4308.9756, 1131.0502), (0.0, -32.72744535799946, 0.0), (1.0, 1.0, 1.0), "DM_Mines_Machine_Whim_Side_Bracket_Destructible_15", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_brk_mesh, _brk_mats, (1153.7554, 4806.158, 1536.5448), (-3.3907777189861217, -70.129367580675, -8.601898594334797), (1.0, 1.0, 1.0), "DM_Mines_Machine_Whim_Side_Bracket_Destructible12_2", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_brk_mesh, _brk_mats, (3795.9175, 3634.1921, 1146.5365), (0.0, -32.72744535799946, 0.0), (1.0, 1.0, 1.0), "DM_Mines_Machine_Whim_Side_Bracket_Destructible2_21", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_brk_mesh, _brk_mats, (4273.9907, 4378.122, 1869.8026), (4.223782791712792e-05, -32.729979433471115, -91.95895674379835), (1.0, 1.0, 1.0), "DM_Mines_Machine_Whim_Side_Bracket_Destructible3", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_brk_mesh, _brk_mats, (4424.328, 4281.4805, 1869.8018), (4.223782791712792e-05, -32.729979433471115, -91.95895674379835), (1.0, 1.0, 1.0), "DM_Mines_Machine_Whim_Side_Bracket_Destructible4", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_brk_mesh, _brk_mats, (1985.357, 5235.2314, 1694.4478), (3.391065670382001, 109.87043494771729, 8.60165336754087), (1.0, 1.0, 1.0), "DM_Mines_Machine_Whim_Side_Bracket_Destructible5_23", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_brk_mesh, _brk_mats, (2461.7336, 1247.8033, 1932.9382), (7.91892533062798e-14, -75.65639427276446, 7.629393862340904e-06), (1.0, 1.0, 1.0), "DM_Mines_Machine_Whim_Side_Bracket_Destructible6", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_brk_mesh, _brk_mats, (2392.4307, 1439.396, 1932.9382), (8.958620236609602e-14, -75.65639427276449, 7.99999810789864e-06), (1.0, 1.0, 1.0), "DM_Mines_Machine_Whim_Side_Bracket_Destructible7", _folder)
if a: placed += 1
else: skipped += 1

# Breakable Batch 3: BP_DM_Mine_tailings_Debris_2x2_C (7 instances)
#   BP Class: /Game/LevelDesign/Deco/MinesDressing/BP_DM_Mine_tailings_Debris_2x2_C
_brk_mesh = "/Game/Art/Assets/Kits/Deco/Mines/Mine_tailings_Debris_2x2_C"
_brk_mats = ['/Game/Art/Assets/Kits/Misc/Dirt_Mounds/Materials/MI_DirtMound_Mines', '/Game/Art/Assets/Kits/Deco/Rubble/Materials/Rubble_Masonry_Pile/MI_Rubble_Masonry_Pile_Base_Inst', '/Game/Art/Assets/Kits/Deco/Rubble/Materials/Rubble_Masonry_Pile/MI_Rubble_Masonry_Pile_06_Inst']
a = spawn_static_mesh(_brk_mesh, _brk_mats, (2350.0, 5146.1904, 792.28125), (0.0, 0.0, -0.0), (1.0, 1.0, 1.0), "BP_DM_Mine_tailings_Debris_2x2_C_2", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_brk_mesh, _brk_mats, (3862.9517, 4440.761, 795.3717), (0.0, 0.0, -0.0), (1.0, 1.0, 1.0), "BP_DM_Mine_tailings_Debris_2x2_C2_8", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_brk_mesh, _brk_mats, (1600.9384, 2634.4387, 789.6024), (0.0, 0.0, -0.0), (1.0, 1.0, 1.0), "BP_DM_Mine_tailings_Debris_2x2_C3_11", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_brk_mesh, _brk_mats, (4926.751, 2750.7483, 794.32117), (0.0, 0.0, -0.0), (1.0, 1.0, 1.0), "BP_DM_Mine_tailings_Debris_2x2_C4_14", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_brk_mesh, _brk_mats, (3970.5703, 2052.6458, 790.5194), (0.0, -90.0001164887758, 0.0), (1.0, 1.0, 1.0), "BP_DM_Mine_tailings_Debris_2x2_C5_17", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_brk_mesh, _brk_mats, (3854.5547, 2613.272, 926.2001), (-6.53562631878507e-08, -89.99997001713079, -10.109923253043508), (1.0, 1.0, 1.0), "BP_DM_Mine_tailings_Debris_2x2_C6_20", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_brk_mesh, _brk_mats, (2160.5427, 2353.091, 1458.0774), (2.2607036921087778, 46.574351623673984, 1.0664502056777708e-06), (1.0, 1.0, 1.0), "BP_DM_Mine_tailings_Debris_2x2_C7_23", _folder)
if a: placed += 1
else: skipped += 1

# Breakable Batch 4: BP_DM_Mine_tailings_Debris_3x3_A (2 instances)
#   BP Class: /Game/LevelDesign/Deco/MinesDressing/BP_DM_Mine_tailings_Debris_3x3_A
_brk_mesh = "/Game/Art/Assets/Kits/Deco/Mines/Mine_tailings_Debris_3x3_A"
_brk_mats = ['/Game/Art/Assets/Kits/Misc/Dirt_Mounds/Materials/MI_DirtMound_Mines', '/Game/Art/Assets/Kits/Deco/Rubble/Materials/Rubble_Masonry_Pile/MI_Rubble_Masonry_Pile_06_Inst']
a = spawn_static_mesh(_brk_mesh, _brk_mats, (5128.485, 3346.7498, 789.8697), (0.0, 0.0, -0.0), (1.0, 1.0, 1.0), "BP_DM_Mine_tailings_Debris_3x3_A_5", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_brk_mesh, _brk_mats, (5646.7544, 3795.8735, 784.41956), (0.0, 49.37941491615263, -0.0), (1.0, 1.0, 1.0), "BP_DM_Mine_tailings_Debris_3x3_A2_8", _folder)
if a: placed += 1
else: skipped += 1

# Breakable Batch 5: BP_DM_Mine_tailings_Debris_3x3_B (5 instances)
#   BP Class: /Game/LevelDesign/Deco/MinesDressing/BP_DM_Mine_tailings_Debris_3x3_B
_brk_mesh = "/Game/Art/Assets/Kits/Deco/Mines/Mine_tailings_Debris_3x3_B"
_brk_mats = ['/Game/Art/Assets/Kits/Misc/Dirt_Mounds/Materials/MI_DirtMound_Mines', '/Game/Art/Assets/Kits/Deco/Rubble/Materials/Rubble_Masonry_Pile/MI_Rubble_Masonry_Pile_06_Inst']
a = spawn_static_mesh(_brk_mesh, _brk_mats, (1435.473, 4746.787, 789.1171), (0.0, 0.0, -0.0), (1.0, 1.0, 1.0), "BP_DM_Mine_tailings_Debris_3x3_B_2", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_brk_mesh, _brk_mats, (1024.1072, 2614.6663, 792.67804), (0.0, 0.0, -0.0), (1.0, 1.0, 1.0), "BP_DM_Mine_tailings_Debris_3x3_B2_5", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_brk_mesh, _brk_mats, (3464.693, 2037.4421, 793.1954), (0.0, 0.0, -0.0), (1.0, 1.0, 1.0), "BP_DM_Mine_tailings_Debris_3x3_B3_8", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_brk_mesh, _brk_mats, (2280.7227, 800.3227, 796.45953), (1.5431307943711805, 33.534637408612504, -2.3269044040690066), (1.0, 1.0, 1.0), "BP_DM_Mine_tailings_Debris_3x3_B4_11", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_brk_mesh, _brk_mats, (1185.3776, 4124.184, 778.72687), (0.0, 0.0, -0.0), (1.0, 1.0, 1.0), "BP_DM_Mine_tailings_Debris_3x3_B5", _folder)
if a: placed += 1
else: skipped += 1

# Breakable Batch 6: BP_Mines_Machine_Whim_Wheel_Middle_Bracket (2 instances)
#   BP Class: /Game/LevelDesign/Deco/MinesDressing/BP_Mines_Machine_Whim_Wheel_Middle_Bracket
_brk_mesh = "/Game/Art/Assets/Kits/Deco/Mines/Machine/Mines_Machine_Whim_Pieces/Mines_Machine_Whim_Wheel_Middle_Bracket"
_brk_mats = ['/Game/Art/Assets/Kits/Deco/Mines/Materials/Mines_Machine_Whim/MI_Mines_Machine_Whim_Trim', '/Game/Art/Assets/Kits/Deco/Mines/Materials/Mines_Machine_Whim/MI_Mines_Machine_Whim_Uniq']
a = spawn_static_mesh(_brk_mesh, _brk_mats, (4260.2417, 2266.971, 783.4581), (0.0, 0.0, 30.000038820411323), (1.0, 1.0, 1.0), "BP_Mines_Machine_Whim_Wheel_Middle_Bracket_2", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_brk_mesh, _brk_mats, (5064.6416, 335.41003, 813.6012), (-1.5329290663178599, 22.00074698670879, 91.50710924802969), (1.0, 1.0, 1.0), "BP_Mines_Machine_Whim_Wheel_Middle_Bracket2", _folder)
if a: placed += 1
else: skipped += 1

# Breakable Batch 7: BP_DM_Warehouse_Crate_A_Lid_Breakable (1 instances)
#   BP Class: /Game/LevelDesign/Deco/Urban/Warehouse/BP_DM_Warehouse_Crate_A_Lid_Breakable
_brk_mesh = "/Game/Art/Assets/Kits/Deco/Urban/Warehouse/Warehouse_Crate_A_Lid"
_brk_mats = ['/Game/Art/Assets/Kits/Deco/Urban/Warehouse/Materials/Warehouse_Crate/MI_Warehouse_Crate']
a = spawn_static_mesh(_brk_mesh, _brk_mats, (984.3752, 2729.1294, 807.83203), (8.40241525100088, 0.0, -0.0), (1.0, 1.0, 1.0), "BP_DM_Warehouse_Crate_A_Lid_Breakable_2", _folder)
if a: placed += 1
else: skipped += 1

# Breakable Batch 8: BP_DM_Mines_Plank_3M_A (6 instances)
#   BP Class: /Game/LevelDesign/Deco_Architecture/Mines/BP_DM_Mines_Plank_3M_A
_brk_mesh = "/Game/Art/Assets/Kits/Deco_Architecture/Mines/Mines_Plank_3M_A"
_brk_mats = ['/Game/Art/Assets/Kits/Deco_Architecture/Mines/Materials/Mines_Scaffolding/MI_Mines_Scaffolding_E_Deco']
a = spawn_static_mesh(_brk_mesh, _brk_mats, (1429.5245, 4258.9805, 800.0021), (0.0, 58.00603406544603, -0.0), (1.0, 1.0, 1.0), "Mines_Plank_3M_A_23", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_brk_mesh, _brk_mats, (3953.6, 4611.8403, 822.041), (3.2342039751821567, 89.24060641232275, 5.636756128542437), (1.0, 1.0, 1.0), "Mines_Plank_3M_A2", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_brk_mesh, _brk_mats, (4719.151, 2567.9944, 837.5006), (-1.170654456133447, 52.32733174953358, -2.23175065531851), (1.0, 1.0, 1.0), "Mines_Plank_3M_A3_61", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_brk_mesh, _brk_mats, (5037.6963, 893.561, 821.5504), (-1.170654456133447, 52.32733174953358, -2.23175065531851), (1.0, 1.0, 1.0), "Mines_Plank_3M_A4", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_brk_mesh, _brk_mats, (5572.562, 1317.7838, 853.0775), (-14.663148083410002, 21.761572445210824, -7.552734925448404), (1.0, 1.0, 1.0), "Mines_Plank_3M_A5", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_brk_mesh, _brk_mats, (5596.136, 1349.1943, 844.98975), (-17.655699494756774, 47.14588044354146, -10.85629212633769), (1.0, 1.0, 1.0), "Mines_Plank_3M_A6", _folder)
if a: placed += 1
else: skipped += 1

# Breakable Batch 9: BP_DM_Mines_Plank_3M_B (7 instances)
#   BP Class: /Game/LevelDesign/Deco_Architecture/Mines/BP_DM_Mines_Plank_3M_B
_brk_mesh = "/Game/Art/Assets/Kits/Deco_Architecture/Mines/Mines_Plank_3M_B"
_brk_mats = ['/Game/Art/Assets/Kits/Deco_Architecture/Mines/Materials/Mines_Scaffolding/MI_Mines_Scaffolding_E_Deco']
a = spawn_static_mesh(_brk_mesh, _brk_mats, (1515.5933, 4555.0073, 802.96643), (0.0, 0.0, -0.0), (1.0, 1.0, 1.0), "Mines_Plank_3M_B_32", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_brk_mesh, _brk_mats, (3878.089, 5168.7397, 803.7752), (-3.607543891040497, 122.7202427010087, -2.004821392781331), (1.0, 1.0, 1.0), "Mines_Plank_3M_B2", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_brk_mesh, _brk_mats, (3645.157, 5197.1216, 809.88855), (-3.607543891040497, 122.7202427010087, -2.004821392781331), (1.0, 1.0, 1.0), "Mines_Plank_3M_B3", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_brk_mesh, _brk_mats, (1807.9443, 2855.2822, 811.70306), (-6.45721468050707, 0.0, -0.0), (1.0, 1.0, 1.0), "Mines_Plank_3M_B5", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_brk_mesh, _brk_mats, (1562.7169, 2757.9595, 813.1179), (2.8680311628190838, -86.72864039774723, 19.345848690070234), (1.0, 1.0, 1.0), "Mines_Plank_3M_B6", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_brk_mesh, _brk_mats, (3085.3438, 1188.0159, 818.83386), (-0.9063719285296962, 77.95292261125101, -4.239288322037619), (1.0, 1.0, 1.0), "Mines_Plank_3M_B7", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_brk_mesh, _brk_mats, (4660.9893, 2412.7795, 815.9493), (7.210677614771146, 49.785503081338184, -6.05786190408349), (1.0, 1.0, 1.0), "Mines_Plank_3M_B8_58", _folder)
if a: placed += 1
else: skipped += 1

# Breakable Batch 10: BP_DM_Mines_Scaffolding_Arch_A (9 instances)
#   BP Class: /Game/LevelDesign/Deco_Architecture/Mines/BP_DM_Mines_Scaffolding_Arch_A
_brk_mesh = "/Game/Art/Assets/Kits/Deco_Architecture/Mines/Mines_Scaffolding_Arch_A"
_brk_mats = ['/Game/Art/Assets/Kits/Deco_Architecture/Mines/Materials/Mines_Scaffolding/MI_Mines_Scaffolding_B_Deco']
a = spawn_static_mesh(_brk_mesh, _brk_mats, (3934.094, 5459.2266, 1257.8727), (1.3660374624255731e-05, -89.99967893535272, -179.99998633961707), (1.0, 1.0, 1.0), "BP_DM_Mines_Scaffolding_Arch_A_9", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_brk_mesh, _brk_mats, (3762.2136, 5605.576, 1393.9945), (0.0, 0.0, -179.99998633961752), (1.0, 1.0, 1.0), "BP_DM_Mines_Scaffolding_Arch_A14_42", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_brk_mesh, _brk_mats, (3843.1682, 5605.576, 1393.9945), (0.0, 0.0, -179.99998633961752), (1.0, 1.0, 1.0), "BP_DM_Mines_Scaffolding_Arch_A15", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_brk_mesh, _brk_mats, (3945.0085, 5452.6855, 1248.748), (-3.0517571207114427e-05, 0.0005722044666686938, -179.99998633961633), (1.0, 1.0, 1.0), "BP_DM_Mines_Scaffolding_Arch_A2_11", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_brk_mesh, _brk_mats, (4690.814, 2752.2544, 1247.988), (0.0, 0.0, -179.99998633961752), (1.0, 1.0, 1.0), "BP_DM_Mines_Scaffolding_Arch_A4_14", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_brk_mesh, _brk_mats, (4681.6704, 2761.741, 1246.1344), (1.3660375352672014e-05, -89.99987340335971, -179.99998633961974), (1.0, 1.0, 1.0), "BP_DM_Mines_Scaffolding_Arch_A5", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_brk_mesh, _brk_mats, (4690.822, 2767.946, 1247.988), (1.3660371493226978e-05, -179.99950822607263, -179.99998633961343), (1.0, 1.0, 1.0), "BP_DM_Mines_Scaffolding_Arch_A6", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_brk_mesh, _brk_mats, (4839.9897, 3196.46, 1308.9625), (-3.3546715532173515e-19, 179.99995901884827, -179.99998633961457), (1.0, 1.0, 1.0), "BP_DM_Mines_Scaffolding_Arch_A7_21", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_brk_mesh, _brk_mats, (5250.805, 3209.6755, 806.1667), (-3.0517569056748195e-05, 89.99998684315408, -179.9999590188494), (1.0, 1.0, 1.0), "BP_DM_Mines_Scaffolding_Arch_A8_27", _folder)
if a: placed += 1
else: skipped += 1

# Breakable Batch 11: BP_DM_Mines_Scaffolding_Arch_B (39 instances)
#   BP Class: /Game/LevelDesign/Deco_Architecture/Mines/BP_DM_Mines_Scaffolding_Arch_B
_brk_mesh = "/Game/Art/Assets/Kits/Deco_Architecture/Mines/Mines_Scaffolding_Arch_B"
_brk_mats = ['/Game/Art/Assets/Kits/Deco_Architecture/Mines/Materials/Mines_Scaffolding/MI_Mines_Scaffolding_A_Deco']
a = spawn_static_mesh(_brk_mesh, _brk_mats, (3773.3467, 5461.9766, 859.7991), (1.3999997600890331e-05, 90.00001925455273, -179.99998633961786), (1.0, 1.0, 1.0), "BP_DM_Mines_Scaffolding_Arch_B10_17", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_brk_mesh, _brk_mats, (3760.7717, 5461.9614, 859.7991), (1.3999997727673227e-05, -89.99964652405329, -179.9999863396165), (1.0, 1.0, 1.0), "BP_DM_Mines_Scaffolding_Arch_B11", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_brk_mesh, _brk_mats, (3766.2866, 5461.9614, 865.2653), (-3.0517570497912294e-05, 0.0005950926959020493, -179.99998633961786), (1.0, 1.0, 1.0), "BP_DM_Mines_Scaffolding_Arch_B12", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_brk_mesh, _brk_mats, (3760.743, 5742.7046, 1085.6143), (1.3999997727673227e-05, -89.99964652405329, -179.9999863396165), (1.0, 1.0, 1.0), "BP_DM_Mines_Scaffolding_Arch_B15_24", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_brk_mesh, _brk_mats, (3767.9346, 5734.8315, 1085.6143), (-3.051757069822911e-05, 0.0006256102584856392, -179.99998633961798), (1.0, 1.0, 1.0), "BP_DM_Mines_Scaffolding_Arch_B16", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_brk_mesh, _brk_mats, (3769.7214, 5749.359, 1088.2023), (1.3999993290704009e-05, -179.9995082260726, -179.99998633961357), (1.0, 1.0, 1.0), "BP_DM_Mines_Scaffolding_Arch_B17", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_brk_mesh, _brk_mats, (3500.9517, 3709.5076, 856.3277), (3.378323601747252e-13, -89.99993012323692, -179.99998633961786), (1.0, 1.0, 1.0), "BP_DM_Mines_Scaffolding_Arch_B2_5", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_brk_mesh, _brk_mats, (2037.6161, 2736.544, 853.73505), (1.3999998650018772e-05, -89.99962059504497, -179.99995901885234), (1.0, 1.0, 1.0), "BP_DM_Mines_Scaffolding_Arch_B23", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_brk_mesh, _brk_mats, (2073.182, 2737.6816, 853.73505), (-3.051756947067204e-05, 90.00048111792312, 179.9999590188561), (1.0, 1.0, 1.0), "BP_DM_Mines_Scaffolding_Arch_B24", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_brk_mesh, _brk_mats, (2010.7639, 2549.3867, 1046.3192), (4.0981117512184905e-05, -179.99950822614062, 179.99997950942353), (1.0, 1.0, 1.0), "BP_DM_Mines_Scaffolding_Arch_B26", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_brk_mesh, _brk_mats, (2091.2043, 2549.3953, 1046.3192), (4.099998042494363e-05, -179.99950822614062, 179.9999795094236), (1.0, 1.0, 1.0), "BP_DM_Mines_Scaffolding_Arch_B27", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_brk_mesh, _brk_mats, (2100.8696, 2541.285, 1043.7556), (-3.051756947067204e-05, 90.00048111792312, 179.9999590188561), (1.0, 1.0, 1.0), "BP_DM_Mines_Scaffolding_Arch_B28", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_brk_mesh, _brk_mats, (1818.6675, 2290.2021, 1019.10095), (4.099998042494363e-05, -179.99950822614062, 179.9999795094236), (1.0, 1.0, 1.0), "BP_DM_Mines_Scaffolding_Arch_B29", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_brk_mesh, _brk_mats, (3498.9856, 4091.2385, 786.7569), (3.378323601747252e-13, -89.99993012323692, -179.99998633961786), (1.0, 1.0, 1.0), "BP_DM_Mines_Scaffolding_Arch_B3", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_brk_mesh, _brk_mats, (1811.935, 2308.5264, 1063.3198), (1.3660377547185972e-05, -89.9993224116623, -179.999959018859), (1.0, 1.0, 1.0), "BP_DM_Mines_Scaffolding_Arch_B30", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_brk_mesh, _brk_mats, (2456.609, 2686.0466, 1447.4982), (1.3660374090055324e-05, -89.99919276689562, -179.999959018855), (1.0, 1.0, 1.0), "BP_DM_Mines_Scaffolding_Arch_B31", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_brk_mesh, _brk_mats, (2467.892, 2595.3442, 1583.1855), (-6.1035143666515866e-05, 0.0009613034671813126, -179.9999590188584), (1.0, 1.0, 1.0), "BP_DM_Mines_Scaffolding_Arch_B32", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_brk_mesh, _brk_mats, (2456.6177, 2607.781, 1506.1753), (1.3999995167602512e-05, -89.99919276689553, -179.9999590188559), (1.0, 1.0, 1.0), "BP_DM_Mines_Scaffolding_Arch_B33", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_brk_mesh, _brk_mats, (4839.982, 2611.2764, 771.8905), (-6.103515393983795e-05, 89.9999544317762, -179.99995901886004), (1.0, 1.0, 1.0), "BP_DM_Mines_Scaffolding_Arch_B34", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_brk_mesh, _brk_mats, (4489.9795, 2604.1924, 996.3722), (4.0999993939914163e-05, -3.0517574349968098e-05, -179.99995901885922), (1.0, 1.0, 1.0), "BP_DM_Mines_Scaffolding_Arch_B35", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_brk_mesh, _brk_mats, (4514.2246, 2604.1921, 996.3722), (4.0999993939914163e-05, -3.0517574349968098e-05, -179.99995901885922), (1.0, 1.0, 1.0), "BP_DM_Mines_Scaffolding_Arch_B36", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_brk_mesh, _brk_mats, (4317.643, 2604.7456, 1113.36), (4.0999993939914163e-05, -3.0517574349968098e-05, -179.99995901885922), (1.0, 1.0, 1.0), "BP_DM_Mines_Scaffolding_Arch_B37", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_brk_mesh, _brk_mats, (4310.859, 2609.275, 1107.9878), (4.0999992540682515e-05, -89.99993012326543, 179.99995901884793), (1.0, 1.0, 1.0), "BP_DM_Mines_Scaffolding_Arch_B38", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_brk_mesh, _brk_mats, (4680.9653, 2610.6821, 947.5006), (4.099999571387074e-05, -89.99980858068227, 179.9999590188523), (1.0, 1.0, 1.0), "BP_DM_Mines_Scaffolding_Arch_B39_60", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_brk_mesh, _brk_mats, (4839.982, 2603.3809, 762.9397), (4.0981127586767255e-05, -3.0517572064884185e-05, -179.99995901885922), (1.0, 1.0, 1.0), "BP_DM_Mines_Scaffolding_Arch_B4_52", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_brk_mesh, _brk_mats, (4715.7686, 2910.869, 1240.4406), (4.099999698002953e-05, -3.0517578014468943e-05, 177.3092044163067), (1.0, 1.0, 1.0), "BP_DM_Mines_Scaffolding_Arch_B40_63", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_brk_mesh, _brk_mats, (4955.1323, 3864.344, 1203.8662), (4.781131673851734e-05, -179.99994535848194, -89.99993822608712), (1.0, 1.0, 1.0), "BP_DM_Mines_Scaffolding_Arch_B45_73", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_brk_mesh, _brk_mats, (2439.114, 1268.9178, 1284.299), (3.4883690963397204e-13, 89.99997874030844, -179.99998633961786), (1.0, 1.0, 1.0), "BP_DM_Mines_Scaffolding_Arch_B46_76", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_brk_mesh, _brk_mats, (2994.6133, 1167.089, 770.8146), (-3.051756866065943e-05, 90.00072258416714, 179.999979509425), (1.0, 1.0, 1.0), "BP_DM_Mines_Scaffolding_Arch_B47_79", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_brk_mesh, _brk_mats, (2985.9343, 1161.6904, 770.8146), (-1.086289465273017e-18, 0.0007171629785620385, -179.99995901885745), (1.0, 1.0, 1.0), "BP_DM_Mines_Scaffolding_Arch_B48", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_brk_mesh, _brk_mats, (2684.621, 953.0916, 791.6702), (-3.8347538141862365e-18, 0.000716999891865005, -179.99995901885745), (1.0, 1.0, 1.0), "BP_DM_Mines_Scaffolding_Arch_B49", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_brk_mesh, _brk_mats, (3714.047, 4401.906, 786.75665), (1.3660373949438956e-05, -179.9999453584753, -179.99998633961786), (1.0, 1.0, 1.0), "BP_DM_Mines_Scaffolding_Arch_B5", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_brk_mesh, _brk_mats, (2309.7698, 954.30206, 867.34106), (-3.8347538141862365e-18, 0.000716999891865005, -179.99995901885745), (1.0, 1.0, 1.0), "BP_DM_Mines_Scaffolding_Arch_B50", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_brk_mesh, _brk_mats, (3991.7551, 3996.121, 1075.6968), (1.3999996940372052e-05, -179.9999453584787, -179.99998633961772), (1.0, 1.0, 1.0), "BP_DM_Mines_Scaffolding_Arch_B6", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_brk_mesh, _brk_mats, (1346.5751, 4460.64, 796.48395), (-3.0517567635154053e-05, 89.99997874030888, -179.999986339619), (1.0, 1.0, 1.0), "BP_DM_Mines_Scaffolding_Arch_B60", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_brk_mesh, _brk_mats, (1346.5752, 4739.6714, 796.48395), (-3.0517567635154053e-05, 89.99997874030888, -179.999986339619), (1.0, 1.0, 1.0), "BP_DM_Mines_Scaffolding_Arch_B61", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_brk_mesh, _brk_mats, (1086.553, 4132.355, 800.00195), (-2.0490564364548423e-05, -4.098112622012886e-05, -179.9999694824156), (1.0, 1.0, 1.0), "BP_DM_Mines_Scaffolding_Arch_B62", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_brk_mesh, _brk_mats, (909.4992, 4151.417, 800.00195), (-3.0517571223278056e-05, -3.0517574716500314e-05, -179.99995901885734), (1.0, 1.0, 1.0), "BP_DM_Mines_Scaffolding_Arch_B63", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_brk_mesh, _brk_mats, (3701.4873, 3713.9749, 1072.7029), (3.378323601747252e-13, -89.99993012323692, -179.99998633961786), (1.0, 1.0, 1.0), "BP_DM_Mines_Scaffolding_Arch_B9", _folder)
if a: placed += 1
else: skipped += 1

# Breakable Batch 12: BP_DM_Mines_Scaffolding_Beam_2M_B (1 instances)
#   BP Class: /Game/LevelDesign/Deco_Architecture/Mines/BP_DM_Mines_Scaffolding_Beam_2M_B
_brk_mesh = "/Game/Art/Assets/Kits/Deco_Architecture/Mines/Mines_Scaffolding_Beam_2M_C"
_brk_mats = ['/Game/Art/Assets/Kits/Deco_Architecture/Mines/Materials/Mines_Scaffolding/MI_Mines_Scaffolding_B_Deco']
a = spawn_static_mesh(_brk_mesh, _brk_mats, (2352.2927, 744.30884, 814.45), (-78.27417569539419, 33.17821434068591, 9.311811520536318e-05), (1.0, 1.0, 1.0), "BP_DM_Mines_Scaffolding_Beam_2M_B_2", _folder)
if a: placed += 1
else: skipped += 1

# Breakable Batch 13: BP_DM_Mines_Scaffolding_Beam_3M_C (1 instances)
#   BP Class: /Game/LevelDesign/Deco_Architecture/Mines/BP_DM_Mines_Scaffolding_Beam_3M_C
_brk_mesh = "/Game/Art/Assets/Kits/Deco_Architecture/Mines/Mines_Scaffolding_Beam_3M_C"
_brk_mats = ['/Game/Art/Assets/Kits/Deco_Architecture/Mines/Materials/Mines_Scaffolding/MI_Mines_Scaffolding_B_Deco']
a = spawn_static_mesh(_brk_mesh, _brk_mats, (2488.694, 684.75195, 801.33276), (-53.97301998181315, 17.116586287461224, 70.30068331154798), (1.0, 1.0, 1.0), "BP_DM_Mines_Scaffolding_Beam_3M_C_2", _folder)
if a: placed += 1
else: skipped += 1

# Breakable Batch 14: BP_DM_Mines_Scaffolding_Platform_1X1M_A (1 instances)
#   BP Class: /Game/LevelDesign/Deco_Architecture/Mines/BP_DM_Mines_Scaffolding_Platform_1X1M_A
_brk_mesh = "/Game/Art/Assets/Kits/Deco_Architecture/Mines/Mines_Scaffolding_Platform_1X1M_A"
_brk_mats = ['/Game/Art/Assets/Kits/Deco_Architecture/Mines/Materials/Mines_Scaffolding/MI_Mines_Scaffolding_D_Deco', '/Game/Art/Assets/Kits/Deco_Architecture/Mines/Materials/Mines_Scaffolding/MI_Mines_Scaffolding_E_Deco']
a = spawn_static_mesh(_brk_mesh, _brk_mats, (2376.5986, 1036.8417, 1019.29034), (0.0, 30.000038820411323, -0.0), (1.0, 1.0, 1.0), "BP_DM_Mines_Scaffolding_Platform_1X1M_A_2", _folder)
if a: placed += 1
else: skipped += 1

# Breakable Batch 15: BP_DM_Mines_Scaffolding_Platform_3X1M_A (1 instances)
#   BP Class: /Game/LevelDesign/Deco_Architecture/Mines/BP_DM_Mines_Scaffolding_Platform_3X1M_A
_brk_mesh = "/Game/Art/Assets/Kits/Deco_Architecture/Mines/Mines_Scaffolding_Platform_3X1M_A"
_brk_mats = ['/Game/Art/Assets/Kits/Deco_Architecture/Mines/Materials/Mines_Scaffolding/MI_Mines_Scaffolding_D_Deco', '/Game/Art/Assets/Kits/Deco_Architecture/Mines/Materials/Mines_Scaffolding/MI_Mines_Scaffolding_E_Deco']
a = spawn_static_mesh(_brk_mesh, _brk_mats, (3499.5056, 5486.9297, 816.4779), (4.508791964722729, -169.01187810837055, -0.5392762290345212), (1.0, 1.0, 1.0), "DM_Mines_Scaffolding_Platform_3X1M_A_Destructible5", _folder)
if a: placed += 1
else: skipped += 1

# Breakable Batch 16: BP_DM_Mines_Scaffolding_Platform_3X3M_B (6 instances)
#   BP Class: /Game/LevelDesign/Deco_Architecture/Mines/BP_DM_Mines_Scaffolding_Platform_3X3M_B
_brk_mesh = "/Game/Art/Assets/Kits/Deco_Architecture/Mines/Mines_Scaffolding_Platform_3X3M_B"
_brk_mats = ['/Game/Art/Assets/Kits/Deco_Architecture/Mines/Materials/Mines_Scaffolding/MI_Mines_Scaffolding_D_Deco', '/Game/Art/Assets/Kits/Deco_Architecture/Mines/Materials/Mines_Scaffolding/MI_Mines_Scaffolding_E_Deco']
a = spawn_static_mesh(_brk_mesh, _brk_mats, (3426.2986, 3915.9539, 850.1607), (2.856108881004281, 47.26186844165642, 11.925794509726336), (1.0, 1.0, 1.0), "BP_DM_Mines_Scaffolding_Platform_3X3M_B2", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_brk_mesh, _brk_mats, (1095.7781, 2666.6438, 819.8876), (3.1280081856375603, -48.142524509176404, 3.736071453737839), (1.0, 1.0, 1.0), "BP_DM_Mines_Scaffolding_Platform_3X3M_B3", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_brk_mesh, _brk_mats, (2602.3232, 5410.4062, 811.3593), (-8.697753598742167, -80.87081415694199, -3.4153133605711647), (1.0, 1.0, 1.0), "BP_DM_Mines_Scaffolding_Platform_3X3M_B4", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_brk_mesh, _brk_mats, (3335.5388, 1725.3531, 804.54846), (-1.97845487677035, -82.60999489113902, -6.38134815249655), (1.0, 1.0, 1.0), "BP_DM_Mines_Scaffolding_Platform_3X3M_B5", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_brk_mesh, _brk_mats, (4651.553, 2621.2551, 827.7913), (-0.9674069951217371, -109.24276147665871, -2.468414234455546), (1.0, 1.0, 1.0), "BP_DM_Mines_Scaffolding_Platform_3X3M_B6", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_brk_mesh, _brk_mats, (4983.0312, 936.484, 814.0382), (-0.9674069951217371, -109.24276147665871, -2.468414234455546), (1.0, 1.0, 1.0), "BP_DM_Mines_Scaffolding_Platform_3X3M_B7", _folder)
if a: placed += 1
else: skipped += 1

# Breakable Batch 17: BP_DM_Mines_Scaffolding_Post_2M_A (3 instances)
#   BP Class: /Game/LevelDesign/Deco_Architecture/Mines/BP_DM_Mines_Scaffolding_Post_2M_A
_brk_mesh = "/Game/Art/Assets/Kits/Deco_Architecture/Mines/Mines_Scaffolding_Post_2M_A"
_brk_mats = ['/Game/Art/Assets/Kits/Deco_Architecture/Mines/Materials/Mines_Scaffolding/MI_Mines_Scaffolding_B_Deco']
a = spawn_static_mesh(_brk_mesh, _brk_mats, (4702.565, 2603.2283, 1085.121), (5.729560773297156e-07, 89.99998281126685, 89.99997593577295), (1.0, 1.0, 1.0), "BP_DM_Mines_Scaffolding_Post_2M_A_2", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_brk_mesh, _brk_mats, (4502.568, 2615.1602, 1085.121), (3.437615679233712e-06, -89.9998808249097, -89.9998808249097), (1.0, 1.0, 1.0), "BP_DM_Mines_Scaffolding_Post_2M_A2", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_brk_mesh, _brk_mats, (4702.565, 2763.252, 1328.5533), (-5.73019666159462e-07, -89.99990832680892, -89.99990832680892), (1.0, 1.0, 1.0), "BP_DM_Mines_Scaffolding_Post_2M_A3_6", _folder)
if a: placed += 1
else: skipped += 1

# Breakable Batch 18: BP_DM_Mines_Scaffolding_Post_2M_B (11 instances)
#   BP Class: /Game/LevelDesign/Deco_Architecture/Mines/BP_DM_Mines_Scaffolding_Post_2M_B
_brk_mesh = "/Game/Art/Assets/Kits/Deco_Architecture/Mines/Mines_Scaffolding_Post_2M_B"
_brk_mats = ['/Game/Art/Assets/Kits/Deco_Architecture/Mines/Materials/Mines_Scaffolding/MI_Mines_Scaffolding_C_Deco']
a = spawn_static_mesh(_brk_mesh, _brk_mats, (3871.4863, 5467.0356, 1208.5983), (0.0, -89.99999818714215, 0.0), (1.0, 1.0, 1.0), "BP_DM_Mines_Scaffolding_Post_2M_B_2", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_brk_mesh, _brk_mats, (2893.0273, 1346.4604, 1006.5096), (84.99966503963887, -89.99954956053463, -74.99964082546558), (1.0, 1.0, 1.0), "BP_DM_Mines_Scaffolding_Post_2M_B10", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_brk_mesh, _brk_mats, (1453.6652, 308.17038, 840.29565), (-75.9205542218181, 109.25056207461569, -70.66474521013912), (1.0, 1.0, 1.0), "BP_DM_Mines_Scaffolding_Post_2M_B11", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_brk_mesh, _brk_mats, (2893.0273, 1407.2444, 1000.35114), (90.0, -39.09661105361462, -119.09685419501092), (1.0, 1.0, 1.0), "BP_DM_Mines_Scaffolding_Post_2M_B2_8", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_brk_mesh, _brk_mats, (1554.2922, 4761.7627, 813.5777), (-84.32860392513355, -119.5919014695095, -106.06582301930011), (1.0, 1.0, 1.0), "BP_DM_Mines_Scaffolding_Post_2M_B3", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_brk_mesh, _brk_mats, (3306.8452, 4035.4485, 807.9565), (-74.71635626106102, -73.47504140161631, -122.19377584444774), (1.0, 1.0, 1.0), "BP_DM_Mines_Scaffolding_Post_2M_B4", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_brk_mesh, _brk_mats, (3509.4636, 5387.772, 823.73444), (-85.26764731983003, -149.4305506965232, -3.8902884789185315), (1.0, 1.0, 1.0), "BP_DM_Mines_Scaffolding_Post_2M_B5", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_brk_mesh, _brk_mats, (1101.034, 2730.188, 818.18555), (-85.96250476794675, -133.86167057750689, -60.50895167107438), (1.0, 1.0, 1.0), "BP_DM_Mines_Scaffolding_Post_2M_B6", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_brk_mesh, _brk_mats, (3550.66, 1615.5226, 800.0013), (-84.32860392513355, -119.5919014695095, -106.06582301930011), (1.0, 1.0, 1.0), "BP_DM_Mines_Scaffolding_Post_2M_B7", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_brk_mesh, _brk_mats, (3251.9863, 1257.6464, 811.07056), (-84.32866049290467, -100.75194406526423, -106.06621526781963), (1.0, 1.0, 1.0), "BP_DM_Mines_Scaffolding_Post_2M_B8", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_brk_mesh, _brk_mats, (3508.3726, 1742.7002, 817.0757), (-76.54813044751468, 75.84601174638269, -39.45275941688434), (1.0, 1.0, 1.0), "BP_DM_Mines_Scaffolding_Post_2M_B9", _folder)
if a: placed += 1
else: skipped += 1

# Breakable Batch 19: BP_DM_Mines_Scaffolding_Post_3M_A (16 instances)
#   BP Class: /Game/LevelDesign/Deco_Architecture/Mines/BP_DM_Mines_Scaffolding_Post_3M_A
_brk_mesh = "/Game/Art/Assets/Kits/Deco_Architecture/Mines/Mines_Scaffolding_Post_3M_A"
_brk_mats = ['/Game/Art/Assets/Kits/Deco_Architecture/Mines/Materials/Mines_Scaffolding/MI_Mines_Scaffolding_B_Deco']
a = spawn_static_mesh(_brk_mesh, _brk_mats, (4684.327, 2749.2686, 1347.4926), (0.0, 0.0, 90.0000030488508), (1.0, 1.0, 1.0), "BP_DM_Mines_Scaffolding_Post_3M_A_2", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_brk_mesh, _brk_mats, (3170.1091, 3900.5593, 808.6945), (84.12890451460395, 141.55035188472348, -41.52426748999179), (1.0, 1.0, 1.0), "BP_DM_Mines_Scaffolding_Post_3M_A10", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_brk_mesh, _brk_mats, (3788.6636, 5222.193, 785.52325), (81.07530195217775, 8.964431644470372, 18.18415518622074), (1.0, 1.0, 1.0), "BP_DM_Mines_Scaffolding_Post_3M_A11", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_brk_mesh, _brk_mats, (3284.3281, 3586.301, 853.78687), (30.39935417334911, 152.12796302524546, -17.570433569036357), (1.0, 1.0, 1.0), "BP_DM_Mines_Scaffolding_Post_3M_A12", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_brk_mesh, _brk_mats, (3293.4353, 3636.9263, 850.3927), (34.85155277268976, 178.92007588493985, 5.742044187596764), (1.0, 1.0, 1.0), "BP_DM_Mines_Scaffolding_Post_3M_A13", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_brk_mesh, _brk_mats, (1046.3702, 2641.9417, 826.6417), (87.29067935122401, -28.561803985497278, 148.63731460015748), (1.0, 1.0, 1.0), "BP_DM_Mines_Scaffolding_Post_3M_A14", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_brk_mesh, _brk_mats, (1992.1898, 2735.9812, 896.95325), (65.64334571788474, 100.43421495210389, 159.46746982562027), (1.0, 1.0, 1.0), "BP_DM_Mines_Scaffolding_Post_3M_A15", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_brk_mesh, _brk_mats, (3060.5684, 1130.5408, 787.80774), (83.31498281124229, -100.72317356420918, 61.36121391252011), (1.0, 1.0, 1.0), "BP_DM_Mines_Scaffolding_Post_3M_A16_6", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_brk_mesh, _brk_mats, (3451.6318, 1873.554, 822.18646), (84.9790350790361, -111.77080971765868, -165.25017785179108), (1.0, 1.0, 1.0), "BP_DM_Mines_Scaffolding_Post_3M_A17", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_brk_mesh, _brk_mats, (2429.0005, 881.9277, 822.5486), (26.377794901842602, -48.431213969420824, -17.781067855374452), (1.0, 1.0, 1.0), "BP_DM_Mines_Scaffolding_Post_3M_A18", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_brk_mesh, _brk_mats, (2402.5938, 837.89874, 817.9071), (31.32446871581217, -22.80365095723545, 3.4252736131975965), (1.0, 1.0, 1.0), "BP_DM_Mines_Scaffolding_Post_3M_A19", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_brk_mesh, _brk_mats, (1504.6136, 444.73535, 866.7823), (81.85560846540793, -166.85012356557894, 145.70752956651916), (1.0, 1.0, 1.0), "BP_DM_Mines_Scaffolding_Post_3M_A20", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_brk_mesh, _brk_mats, (5018.3545, 549.76105, 822.5486), (26.377809111349503, 177.22939209182033, -17.78109942754231), (1.0, 1.0, 1.0), "BP_DM_Mines_Scaffolding_Post_3M_A21", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_brk_mesh, _brk_mats, (5005.3184, 599.41833, 817.9071), (31.324414013268818, -157.1427456166382, 3.4253007591580564), (1.0, 1.0, 1.0), "BP_DM_Mines_Scaffolding_Post_3M_A22", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_brk_mesh, _brk_mats, (3762.677, 5454.149, 1210.0022), (0.0, 0.0, 90.0000030488508), (1.0, 1.0, 1.0), "BP_DM_Mines_Scaffolding_Post_3M_A6", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_brk_mesh, _brk_mats, (1381.983, 4502.1523, 795.64636), (82.39350248780299, -44.33342388928025, 41.69318435220294), (1.0, 1.0, 1.0), "BP_DM_Mines_Scaffolding_Post_3M_A9", _folder)
if a: placed += 1
else: skipped += 1

# Breakable Batch 20: BP_DM_Mines_Scaffolding_Support_1M (3 instances)
#   BP Class: /Game/LevelDesign/Deco_Architecture/Mines/BP_DM_Mines_Scaffolding_Support_1M
_brk_mesh = "/Game/Art/Assets/Kits/Deco_Architecture/Mines/Mines_Scaffolding_Support_1M"
_brk_mats = ['/Game/Art/Assets/Kits/Deco_Architecture/Mines/Materials/Mines_Scaffolding/MI_Mines_Scaffolding_D_Deco']
a = spawn_static_mesh(_brk_mesh, _brk_mats, (3406.0754, 3700.2202, 828.594), (27.43583335366395, 124.2023738133593, -114.29032914241026), (1.0, 1.0, 1.0), "BP_DM_Mines_Scaffolding_Support_1M_5", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_brk_mesh, _brk_mats, (2274.073, 819.03595, 800.71356), (23.78217773259371, -75.44315516559249, -112.41122501448105), (1.0, 1.0, 1.0), "BP_DM_Mines_Scaffolding_Support_1M2", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_brk_mesh, _brk_mats, (5081.65, 704.5216, 800.71356), (23.78215305672512, 150.2175110378789, -112.40981762978835), (1.0, 1.0, 1.0), "BP_DM_Mines_Scaffolding_Support_1M3", _folder)
if a: placed += 1
else: skipped += 1

# Breakable Batch 21: BP_DM_Mines_Scaffolding_Support_2M (9 instances)
#   BP Class: /Game/LevelDesign/Deco_Architecture/Mines/BP_DM_Mines_Scaffolding_Support_2M
_brk_mesh = "/Game/Art/Assets/Kits/Deco_Architecture/Mines/Mines_Scaffolding_Support_2M"
_brk_mats = ['/Game/Art/Assets/Kits/Deco_Architecture/Mines/Materials/Mines_Scaffolding/MI_Mines_Scaffolding_D_Deco']
a = spawn_static_mesh(_brk_mesh, _brk_mats, (1605.9072, 4979.6353, 1828.815), (9.961430034022582, 24.923277081544793, -0.8804014448193853), (1.0, 1.0, 1.0), "BP_DM_Mines_Scaffolding_Support_2M_2", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_brk_mesh, _brk_mats, (2128.4297, 5222.4395, 1930.0126), (9.961430034022582, 24.923277081544793, -0.8804014448193853), (1.0, 1.0, 1.0), "BP_DM_Mines_Scaffolding_Support_2M2", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_brk_mesh, _brk_mats, (1083.3842, 4736.83, 1727.6174), (9.961430034022582, 24.923277081544793, -0.8804014448193853), (1.0, 1.0, 1.0), "BP_DM_Mines_Scaffolding_Support_2M3", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_brk_mesh, _brk_mats, (1528.0758, 5145.9736, 1831.592), (9.961430034022582, 24.923277081544793, -0.8804014448193853), (1.0, 1.0, 1.0), "BP_DM_Mines_Scaffolding_Support_2M4_9", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_brk_mesh, _brk_mats, (2050.5977, 5388.778, 1932.7897), (9.961430034022582, 24.923277081544793, -0.8804014448193853), (1.0, 1.0, 1.0), "BP_DM_Mines_Scaffolding_Support_2M5", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_brk_mesh, _brk_mats, (1005.55273, 4903.1685, 1730.3945), (9.961430034022582, 24.923277081544793, -0.8804014448193853), (1.0, 1.0, 1.0), "BP_DM_Mines_Scaffolding_Support_2M6", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_brk_mesh, _brk_mats, (4016.2795, 4048.5764, 1995.4037), (0.8162031668548712, -120.29684035658997, -1.1104737408306486), (1.0, 1.0, 1.0), "BP_DM_Mines_Scaffolding_Support_2M7", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_brk_mesh, _brk_mats, (3721.183, 3543.529, 2003.7377), (0.8162031668548712, -120.29684035658997, -1.1104737408306486), (1.0, 1.0, 1.0), "BP_DM_Mines_Scaffolding_Support_2M8", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_brk_mesh, _brk_mats, (4311.3765, 4553.6255, 1987.0703), (0.8162031668548712, -120.29684035658997, -1.1104737408306486), (1.0, 1.0, 1.0), "BP_DM_Mines_Scaffolding_Support_2M9", _folder)
if a: placed += 1
else: skipped += 1

# Breakable Batch 22: BP_DM_Mines_Scaffolding_Support_3M (8 instances)
#   BP Class: /Game/LevelDesign/Deco_Architecture/Mines/BP_DM_Mines_Scaffolding_Support_3M
_brk_mesh = "/Game/Art/Assets/Kits/Deco_Architecture/Mines/Mines_Scaffolding_Support_3M"
_brk_mats = ['/Game/Art/Assets/Kits/Deco_Architecture/Mines/Materials/Mines_Scaffolding/MI_Mines_Scaffolding_D_Deco']
a = spawn_static_mesh(_brk_mesh, _brk_mats, (2100.0713, 5263.994, 1925.8412), (0.8671947145555529, 115.07564966055054, 9.963169794867028), (1.0, 1.0, 1.0), "BP_DM_Mines_Scaffolding_Support_3M_2", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_brk_mesh, _brk_mats, (1832.1116, 5139.478, 1873.945), (0.8671947145555529, 115.07564966055054, 9.963169794867028), (1.0, 1.0, 1.0), "BP_DM_Mines_Scaffolding_Support_3M2", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_brk_mesh, _brk_mats, (1564.1522, 5014.9604, 1822.0487), (0.8671947145555529, 115.07564966055054, 9.963169794867028), (1.0, 1.0, 1.0), "BP_DM_Mines_Scaffolding_Support_3M3", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_brk_mesh, _brk_mats, (1296.1923, 4890.444, 1770.1501), (0.8671950997107598, 115.075649675571, 9.963169546812685), (1.0, 1.0, 1.0), "BP_DM_Mines_Scaffolding_Support_3M4", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_brk_mesh, _brk_mats, (3737.9446, 3543.8787, 2000.4365), (1.110488399646106, -30.281825657295958, 0.8169713181092316), (1.0, 1.0, 1.0), "BP_DM_Mines_Scaffolding_Support_3M5", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_brk_mesh, _brk_mats, (3889.2754, 3802.8782, 1996.1622), (1.110488399646106, -30.281825657295958, 0.8169713181092316), (1.0, 1.0, 1.0), "BP_DM_Mines_Scaffolding_Support_3M6", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_brk_mesh, _brk_mats, (4040.6033, 4061.8804, 1991.8885), (1.110488399646106, -30.281825657295958, 0.8169713181092316), (1.0, 1.0, 1.0), "BP_DM_Mines_Scaffolding_Support_3M7", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_brk_mesh, _brk_mats, (4191.9346, 4320.8765, 1987.6127), (1.110488399646106, -30.281825657295958, 0.8169713181092316), (1.0, 1.0, 1.0), "BP_DM_Mines_Scaffolding_Support_3M8", _folder)
if a: placed += 1
else: skipped += 1

# Breakable Batch 23: BP_Mines_Brace_C (1 instances)
#   BP Class: /Game/LevelDesign/Deco_Architecture/Mines/BP_Mines_Brace_C
_brk_mesh = "/Game/Art/Assets/Kits/Deco/Mines/Machine/Mines_Machine_Whim_Pieces/Mines_Machine_Whim_Side_Support_Beam"
_brk_mats = ['/Game/Art/Assets/Kits/Deco/Mines/Materials/Mines_Machine_Whim/MI_Mines_Machine_Whim_Trim', '/Game/Art/Assets/Kits/Deco/Mines/Materials/Mines_Machine_Whim/MI_Mines_Machine_Whim_Uniq']
a = spawn_static_mesh(_brk_mesh, _brk_mats, (2589.226, 5468.8784, 750.0), (0.0, 25.00001037024192, -0.0), (1.0, 1.0, 1.0), "BP_Mines_Brace_C_2", _folder)
if a: placed += 1
else: skipped += 1

# Breakable Batch 24: BP_Mines_Support_Beam (1 instances)
#   BP Class: /Game/LevelDesign/Deco_Architecture/Mines/BP_Mines_Support_Beam
_brk_mesh = "/Game/Art/Assets/Kits/Deco/Mines/Machine/Mines_Machine_Whim_Pieces/Mines_Machine_Whim_Wheel_Middle_Bracket"
_brk_mats = ['/Game/Art/Assets/Kits/Deco/Mines/Materials/Mines_Machine_Whim/MI_Mines_Machine_Whim_Trim', '/Game/Art/Assets/Kits/Deco/Mines/Materials/Mines_Machine_Whim/MI_Mines_Machine_Whim_Uniq']
a = spawn_static_mesh(_brk_mesh, _brk_mats, (2402.072, 5387.3584, 700.0), (0.0, 110.00001199018955, -0.0), (1.0, 1.0, 1.0), "BP_Mines_Support_Beam_2", _folder)
if a: placed += 1
else: skipped += 1

# Breakable Batch 25: BP_Mines_Support_Beam_B (3 instances)
#   BP Class: /Game/LevelDesign/Deco_Architecture/Mines/BP_Mines_Support_Beam_B
_brk_mesh = "/Game/Art/Assets/Kits/Deco/Mines/Machine/Mines_Machine_Whim_Pieces/Mines_Machine_Whim_Wheel_Middle_Bracket_B"
_brk_mats = ['/Game/Art/Assets/Kits/Deco/Mines/Materials/Mines_Machine_Whim/MI_Mines_Machine_Whim_Trim']
a = spawn_static_mesh(_brk_mesh, _brk_mats, (2426.496, 5386.43, 1110.0), (0.0, 19.99997602993199, -0.0), (1.0, 1.0, 1.0), "BP_Mines_Support_Beam_B_2", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_brk_mesh, _brk_mats, (2398.3052, 5376.1694, 1100.0), (0.0, -70.00006109847311, 0.0), (1.0, 1.0, 1.0), "BP_Mines_Support_Beam_B2", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_brk_mesh, _brk_mats, (2860.4946, 5772.6045, 802.2292), (-6.818206451075236, 76.27371700322662, -3.8760981842452287), (1.0, 1.0, 1.0), "BP_Mines_Support_Beam_B3_2", _folder)
if a: placed += 1
else: skipped += 1

# --- Extra DecoVolumes (not construction blocks) ---
_folder = "Reconstruction/BD_BB_MiningCamp/DecoVolumes"

# DecoVolume: BP_DM_Deep_WoodenPlank_B_Breakable_5 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (1320.2443, 4890.911, 1782.448), (0.0, 0.0, -0.0), (5.7492, 3.2841, 1.2173), "DV_BP_DM_Deep_WoodenPlank_B_Breakable_5_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_DM_Deep_WoodenPlank_B_Breakable10 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (3899.4358, 3769.5217, 2005.451), (0.0, 0.0, -0.0), (3.7709, 5.6174, 0.2710), "DV_BP_DM_Deep_WoodenPlank_B_Breakable10_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_DM_Deep_WoodenPlank_B_Breakable11 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (4279.805, 4242.145, 1998.6481), (0.0, 0.0, -0.0), (3.7709, 5.6174, 0.2710), "DV_BP_DM_Deep_WoodenPlank_B_Breakable11_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_DM_Deep_WoodenPlank_B_Breakable12 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (3977.141, 3724.1477, 2007.1957), (0.0, 0.0, -0.0), (3.7709, 5.6175, 0.2710), "DV_BP_DM_Deep_WoodenPlank_B_Breakable12_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_DM_Deep_WoodenPlank_B_Breakable2 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (1856.1647, 5139.942, 1886.2402), (0.0, 0.0, -0.0), (5.7492, 3.2841, 1.2173), "DV_BP_DM_Deep_WoodenPlank_B_Breakable2_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_DM_Deep_WoodenPlank_B_Breakable3 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (1282.1053, 4972.4194, 1783.8102), (0.0, 0.0, -0.0), (5.7492, 3.2841, 1.2173), "DV_BP_DM_Deep_WoodenPlank_B_Breakable3_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_DM_Deep_WoodenPlank_B_Breakable4 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (1818.0262, 5221.45, 1887.6027), (0.0, 0.0, -0.0), (5.7491, 3.2841, 1.2173), "DV_BP_DM_Deep_WoodenPlank_B_Breakable4_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_DM_Deep_WoodenPlank_B_Breakable5_17 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (1242.4128, 5057.2495, 1785.2251), (0.0, 0.0, -0.0), (5.7492, 3.2841, 1.2173), "DV_BP_DM_Deep_WoodenPlank_B_Breakable5_17_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_DM_Deep_WoodenPlank_B_Breakable6_18 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (1778.3333, 5306.2803, 1889.0173), (0.0, 0.0, -0.0), (5.7492, 3.2841, 1.2173), "DV_BP_DM_Deep_WoodenPlank_B_Breakable6_18_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_DM_Deep_WoodenPlank_B_Breakable7_19 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (1204.2739, 5138.758, 1786.5873), (0.0, 0.0, -0.0), (5.7492, 3.2841, 1.2173), "DV_BP_DM_Deep_WoodenPlank_B_Breakable7_19_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_DM_Deep_WoodenPlank_B_Breakable8_20 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (1740.1948, 5387.7886, 1890.3798), (0.0, 0.0, -0.0), (5.7491, 3.2841, 1.2173), "DV_BP_DM_Deep_WoodenPlank_B_Breakable8_20_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_DM_Deep_WoodenPlank_B_Breakable9 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (4202.099, 4287.5195, 1996.9034), (0.0, 0.0, -0.0), (3.7709, 5.6174, 0.2710), "DV_BP_DM_Deep_WoodenPlank_B_Breakable9_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_DM_Mine_tailings_Debris_1x1_A_2 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (3508.3923, 1899.1942, 816.99896), (0.0, 0.0, -0.0), (1.0107, 1.0107, 0.4337), "DV_BP_DM_Mine_tailings_Debris_1x1_A_2_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_DM_Mine_tailings_Debris_1x1_C_2 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (2257.2307, 2973.8599, 817.3531), (0.0, 0.0, -0.0), (1.3650, 1.0700, 0.5570), "DV_BP_DM_Mine_tailings_Debris_1x1_C_2_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_DM_Mine_tailings_Debris_1x1_D_2 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (2932.5085, 1517.5955, 1019.44653), (0.0, 0.0, -0.0), (1.0971, 1.0995, 0.4947), "DV_BP_DM_Mine_tailings_Debris_1x1_D_2_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_DM_Mine_tailings_Debris_2x2_A_2 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (1904.5736, 5330.0376, 962.4025), (0.0, 0.0, -0.0), (2.1769, 2.1244, 1.0735), "DV_BP_DM_Mine_tailings_Debris_2x2_A_2_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_DM_Mine_tailings_Debris_2x2_A2_5 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (3772.3208, 5262.9614, 809.6498), (0.0, 0.0, -0.0), (2.0658, 2.0672, 0.5085), "DV_BP_DM_Mine_tailings_Debris_2x2_A2_5_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_DM_Mine_tailings_Debris_2x2_A3_8 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (923.2167, 2701.9768, 810.1565), (0.0, 0.0, -0.0), (2.0658, 2.0672, 0.5085), "DV_BP_DM_Mine_tailings_Debris_2x2_A3_8_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_DM_Mine_tailings_Debris_2x2_A4_11 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (2231.1636, 2902.651, 822.09595), (0.0, 0.0, -0.0), (2.0658, 2.1219, 0.8327), "DV_BP_DM_Mine_tailings_Debris_2x2_A4_11_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_DM_Mine_tailings_Debris_2x2_A5_14 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (4976.3047, 2797.867, 807.6926), (0.0, 0.0, -0.0), (2.0658, 2.0672, 0.5085), "DV_BP_DM_Mine_tailings_Debris_2x2_A5_14_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_DM_Mine_tailings_Debris_2x2_A6_20 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (2470.9941, 1663.758, 1442.0878), (0.0, 0.0, -0.0), (2.0658, 2.0672, 0.5085), "DV_BP_DM_Mine_tailings_Debris_2x2_A6_20_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_DM_Mine_tailings_Debris_2x2_B_2 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (3894.0757, 5264.574, 830.33563), (0.0, 0.0, -0.0), (2.1479, 2.1529, 0.9793), "DV_BP_DM_Mine_tailings_Debris_2x2_B_2_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_DM_Mine_tailings_Debris_2x2_B2_5 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (5553.467, 3700.4636, 838.2288), (0.0, 0.0, -0.0), (2.1479, 2.1529, 0.9793), "DV_BP_DM_Mine_tailings_Debris_2x2_B2_5_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_DM_Mine_tailings_Debris_2x2_B3_8 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (4448.1646, 2399.333, 838.2282), (0.0, 0.0, -0.0), (2.1479, 2.1529, 0.9793), "DV_BP_DM_Mine_tailings_Debris_2x2_B3_8_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_DM_Mine_tailings_Debris_2x2_C_2 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (2348.5938, 5145.2295, 819.0409), (0.0, 0.0, -0.0), (2.1324, 2.0854, 0.7345), "DV_BP_DM_Mine_tailings_Debris_2x2_C_2_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_DM_Mine_tailings_Debris_2x2_C2_8 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (3861.5454, 4439.8003, 822.13135), (0.0, 0.0, -0.0), (2.1324, 2.0854, 0.7345), "DV_BP_DM_Mine_tailings_Debris_2x2_C2_8_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_DM_Mine_tailings_Debris_2x2_C3_11 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (1599.5321, 2633.4778, 816.36206), (0.0, 0.0, -0.0), (2.1324, 2.0854, 0.7345), "DV_BP_DM_Mine_tailings_Debris_2x2_C3_11_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_DM_Mine_tailings_Debris_2x2_C4_14 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (4925.3447, 2749.7874, 821.0808), (0.0, 0.0, -0.0), (2.1324, 2.0854, 0.7345), "DV_BP_DM_Mine_tailings_Debris_2x2_C4_14_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_DM_Mine_tailings_Debris_2x2_C5_17 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (3969.6094, 2054.052, 817.27905), (0.0, 0.0, -0.0), (2.0854, 2.1324, 0.7345), "DV_BP_DM_Mine_tailings_Debris_2x2_C5_17_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_DM_Mine_tailings_Debris_2x2_C6_20 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (3848.9114, 2614.6782, 952.37555), (0.0, 0.0, -0.0), (2.1819, 2.1324, 1.0892), "DV_BP_DM_Mine_tailings_Debris_2x2_C6_20_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_DM_Mine_tailings_Debris_2x2_C7_23 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (2159.549, 2350.6433, 1484.7607), (0.0, 0.0, -0.0), (2.9991, 3.0020, 0.8180), "DV_BP_DM_Mine_tailings_Debris_2x2_C7_23_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_DM_Mine_tailings_Debris_3x3_A_5 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (5129.4507, 3346.4731, 819.29724), (0.0, 0.0, -0.0), (3.0000, 3.0055, 1.0281), "DV_BP_DM_Mine_tailings_Debris_3x3_A_5_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_DM_Mine_tailings_Debris_3x3_A2_8 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (5647.5933, 3796.4268, 813.8471), (0.0, 0.0, -0.0), (4.2345, 4.2339, 1.0281), "DV_BP_DM_Mine_tailings_Debris_3x3_A2_8_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_DM_Mine_tailings_Debris_3x3_B_2 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (1438.408, 4752.446, 807.1371), (0.0, 0.0, -0.0), (2.8479, 3.0836, 0.6855), "DV_BP_DM_Mine_tailings_Debris_3x3_B_2_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_DM_Mine_tailings_Debris_3x3_B2_5 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (1027.042, 2620.325, 810.698), (0.0, 0.0, -0.0), (2.8479, 3.0836, 0.6855), "DV_BP_DM_Mine_tailings_Debris_3x3_B2_5_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_DM_Mine_tailings_Debris_3x3_B3_8 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (3467.628, 2043.1008, 811.21533), (0.0, 0.0, -0.0), (2.8479, 3.0836, 0.6855), "DV_BP_DM_Mine_tailings_Debris_3x3_B3_8_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_DM_Mine_tailings_Debris_3x3_B4_11 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (2280.0396, 805.77527, 814.76685), (0.0, 0.0, -0.0), (4.0779, 4.1724, 0.8865), "DV_BP_DM_Mine_tailings_Debris_3x3_B4_11_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_DM_Mine_tailings_Debris_3x3_B5 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (1188.3125, 4129.843, 796.7468), (0.0, 0.0, -0.0), (2.8479, 3.0836, 0.6855), "DV_BP_DM_Mine_tailings_Debris_3x3_B5_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_DM_Mines_Lift_Barrel_A_Breakable2_5 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (2078.3079, 670.9431, 886.5914), (0.0, 0.0, -0.0), (1.2079, 1.2506, 0.8699), "DV_BP_DM_Mines_Lift_Barrel_A_Breakable2_5_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_DM_Mines_Scaffolding_Arch_A_9 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (3909.4045, 5459.4604, 1281.5521), (0.0, 0.0, -0.0), (0.5038, 0.1769, 0.4808), "DV_BP_DM_Mines_Scaffolding_Arch_A_9_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_DM_Mines_Scaffolding_Arch_A14_42 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (3761.9797, 5580.8867, 1417.674), (0.0, 0.0, -0.0), (0.1769, 0.5038, 0.4808), "DV_BP_DM_Mines_Scaffolding_Arch_A14_42_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_DM_Mines_Scaffolding_Arch_A15 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (3842.9343, 5580.8867, 1417.674), (0.0, 0.0, -0.0), (0.1769, 0.5038, 0.4808), "DV_BP_DM_Mines_Scaffolding_Arch_A15_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_DM_Mines_Scaffolding_Arch_A2_11 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (3944.775, 5427.996, 1272.4275), (0.0, 0.0, -0.0), (0.1769, 0.5038, 0.4808), "DV_BP_DM_Mines_Scaffolding_Arch_A2_11_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_DM_Mines_Scaffolding_Arch_A4_14 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (4690.58, 2727.565, 1271.6675), (0.0, 0.0, -0.0), (0.1769, 0.5038, 0.4808), "DV_BP_DM_Mines_Scaffolding_Arch_A4_14_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_DM_Mines_Scaffolding_Arch_A5 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (4656.981, 2761.9749, 1269.8138), (0.0, 0.0, -0.0), (0.5038, 0.1769, 0.4808), "DV_BP_DM_Mines_Scaffolding_Arch_A5_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_DM_Mines_Scaffolding_Arch_A6 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (4691.055, 2792.6355, 1271.6675), (0.0, 0.0, -0.0), (0.1770, 0.5038, 0.4808), "DV_BP_DM_Mines_Scaffolding_Arch_A6_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_DM_Mines_Scaffolding_Arch_A7_21 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (4840.2236, 3221.1494, 1332.642), (0.0, 0.0, -0.0), (0.1769, 0.5038, 0.4808), "DV_BP_DM_Mines_Scaffolding_Arch_A7_21_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_DM_Mines_Scaffolding_Arch_A8_27 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (5275.4946, 3209.4417, 829.8461), (0.0, 0.0, -0.0), (0.5038, 0.1769, 0.4808), "DV_BP_DM_Mines_Scaffolding_Arch_A8_27_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_DM_Mines_Scaffolding_Arch_B10_17 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (3828.1611, 5462.111, 907.97766), (0.0, 0.0, -0.0), (1.1013, 0.1833, 0.9750), "DV_BP_DM_Mines_Scaffolding_Arch_B10_17_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_DM_Mines_Scaffolding_Arch_B11 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (3705.9573, 5461.827, 907.97766), (0.0, 0.0, -0.0), (1.1013, 0.1833, 0.9750), "DV_BP_DM_Mines_Scaffolding_Arch_B11_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_DM_Mines_Scaffolding_Arch_B12 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (3766.4211, 5407.147, 913.44385), (0.0, 0.0, -0.0), (0.1833, 1.1013, 0.9750), "DV_BP_DM_Mines_Scaffolding_Arch_B12_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_DM_Mines_Scaffolding_Arch_B15_24 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (3705.9285, 5742.5703, 1133.7928), (0.0, 0.0, -0.0), (1.1013, 0.1833, 0.9750), "DV_BP_DM_Mines_Scaffolding_Arch_B15_24_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_DM_Mines_Scaffolding_Arch_B16 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (3768.0693, 5680.017, 1133.7928), (0.0, 0.0, -0.0), (0.1833, 1.1013, 0.9750), "DV_BP_DM_Mines_Scaffolding_Arch_B16_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_DM_Mines_Scaffolding_Arch_B17 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (3769.587, 5804.1733, 1136.3809), (0.0, 0.0, -0.0), (0.1833, 1.1013, 0.9750), "DV_BP_DM_Mines_Scaffolding_Arch_B17_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_DM_Mines_Scaffolding_Arch_B2_5 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (3446.1372, 3709.3735, 904.5062), (0.0, 0.0, -0.0), (1.1013, 0.1833, 0.9750), "DV_BP_DM_Mines_Scaffolding_Arch_B2_5_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_DM_Mines_Scaffolding_Arch_B23 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (1982.8015, 2736.4097, 901.91364), (0.0, 0.0, -0.0), (1.1013, 0.1833, 0.9750), "DV_BP_DM_Mines_Scaffolding_Arch_B23_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_DM_Mines_Scaffolding_Arch_B24 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (2127.9966, 2737.8162, 901.9136), (0.0, 0.0, -0.0), (1.1013, 0.1833, 0.9750), "DV_BP_DM_Mines_Scaffolding_Arch_B24_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_DM_Mines_Scaffolding_Arch_B26 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (2010.6294, 2604.2014, 1094.4977), (0.0, 0.0, -0.0), (0.1833, 1.1013, 0.9750), "DV_BP_DM_Mines_Scaffolding_Arch_B26_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_DM_Mines_Scaffolding_Arch_B27 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (2091.0698, 2604.21, 1094.4977), (0.0, 0.0, -0.0), (0.1833, 1.1013, 0.9750), "DV_BP_DM_Mines_Scaffolding_Arch_B27_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_DM_Mines_Scaffolding_Arch_B28 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (2155.6843, 2541.4194, 1091.9341), (0.0, 0.0, -0.0), (1.1013, 0.1833, 0.9750), "DV_BP_DM_Mines_Scaffolding_Arch_B28_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_DM_Mines_Scaffolding_Arch_B29 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (1818.533, 2345.0168, 1067.2794), (0.0, 0.0, -0.0), (0.1833, 1.1013, 0.9750), "DV_BP_DM_Mines_Scaffolding_Arch_B29_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_DM_Mines_Scaffolding_Arch_B3 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (3444.1711, 4091.1045, 834.9354), (0.0, 0.0, -0.0), (1.1013, 0.1833, 0.9750), "DV_BP_DM_Mines_Scaffolding_Arch_B3_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_DM_Mines_Scaffolding_Arch_B30 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (1757.1205, 2308.3916, 1111.4984), (0.0, 0.0, -0.0), (1.1013, 0.1833, 0.9750), "DV_BP_DM_Mines_Scaffolding_Arch_B30_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_DM_Mines_Scaffolding_Arch_B31 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (2401.7944, 2685.9119, 1495.6768), (0.0, 0.0, -0.0), (1.1013, 0.1833, 0.9750), "DV_BP_DM_Mines_Scaffolding_Arch_B31_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_DM_Mines_Scaffolding_Arch_B32 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (2468.027, 2540.5298, 1631.3641), (0.0, 0.0, -0.0), (0.1833, 1.1013, 0.9750), "DV_BP_DM_Mines_Scaffolding_Arch_B32_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_DM_Mines_Scaffolding_Arch_B33 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (2401.8032, 2607.6462, 1554.3539), (0.0, 0.0, -0.0), (1.1013, 0.1833, 0.9750), "DV_BP_DM_Mines_Scaffolding_Arch_B33_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_DM_Mines_Scaffolding_Arch_B34 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (4894.7964, 2611.4104, 820.0691), (0.0, 0.0, -0.0), (1.1013, 0.1833, 0.9750), "DV_BP_DM_Mines_Scaffolding_Arch_B34_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_DM_Mines_Scaffolding_Arch_B35 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (4490.1133, 2549.378, 1044.5508), (0.0, 0.0, -0.0), (0.1833, 1.1013, 0.9750), "DV_BP_DM_Mines_Scaffolding_Arch_B35_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_DM_Mines_Scaffolding_Arch_B36 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (4514.3584, 2549.3777, 1044.5508), (0.0, 0.0, -0.0), (0.1833, 1.1013, 0.9750), "DV_BP_DM_Mines_Scaffolding_Arch_B36_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_DM_Mines_Scaffolding_Arch_B37 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (4317.777, 2549.9312, 1161.5386), (0.0, 0.0, -0.0), (0.1833, 1.1013, 0.9750), "DV_BP_DM_Mines_Scaffolding_Arch_B37_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_DM_Mines_Scaffolding_Arch_B38 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (4256.0444, 2609.1409, 1156.1663), (0.0, 0.0, -0.0), (1.1013, 0.1833, 0.9750), "DV_BP_DM_Mines_Scaffolding_Arch_B38_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_DM_Mines_Scaffolding_Arch_B39_60 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (4626.151, 2610.5479, 995.67914), (0.0, 0.0, -0.0), (1.1013, 0.1833, 0.9750), "DV_BP_DM_Mines_Scaffolding_Arch_B39_60_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_DM_Mines_Scaffolding_Arch_B4_52 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (4840.1157, 2548.5664, 811.1183), (0.0, 0.0, -0.0), (0.1833, 1.1013, 0.9750), "DV_BP_DM_Mines_Scaffolding_Arch_B4_52_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_DM_Mines_Scaffolding_Arch_B40_63 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (4715.9023, 2853.853, 1285.9927), (0.0, 0.0, -0.0), (0.1833, 1.1458, 1.0257), "DV_BP_DM_Mines_Scaffolding_Arch_B40_63_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_DM_Mines_Scaffolding_Arch_B45_73 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (4954.9985, 3816.1653, 1258.6808), (0.0, 0.0, -0.0), (0.1833, 0.9750, 1.1013), "DV_BP_DM_Mines_Scaffolding_Arch_B45_73_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_DM_Mines_Scaffolding_Arch_B46_76 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (2493.9285, 1269.0519, 1332.4775), (0.0, 0.0, -0.0), (1.1013, 0.1833, 0.9750), "DV_BP_DM_Mines_Scaffolding_Arch_B46_76_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_DM_Mines_Scaffolding_Arch_B47_79 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (3049.428, 1167.2238, 818.9931), (0.0, 0.0, -0.0), (1.1013, 0.1833, 0.9750), "DV_BP_DM_Mines_Scaffolding_Arch_B47_79_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_DM_Mines_Scaffolding_Arch_B48 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (2986.069, 1106.8759, 818.99316), (0.0, 0.0, -0.0), (0.1833, 1.1013, 0.9750), "DV_BP_DM_Mines_Scaffolding_Arch_B48_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_DM_Mines_Scaffolding_Arch_B49 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (2684.7559, 898.27704, 839.8488), (0.0, 0.0, -0.0), (0.1833, 1.1013, 0.9750), "DV_BP_DM_Mines_Scaffolding_Arch_B49_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_DM_Mines_Scaffolding_Arch_B5 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (3713.913, 4456.72, 834.9352), (0.0, 0.0, -0.0), (0.1833, 1.1013, 0.9750), "DV_BP_DM_Mines_Scaffolding_Arch_B5_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_DM_Mines_Scaffolding_Arch_B50 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (2309.9045, 899.4875, 915.51965), (0.0, 0.0, -0.0), (0.1833, 1.1013, 0.9750), "DV_BP_DM_Mines_Scaffolding_Arch_B50_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_DM_Mines_Scaffolding_Arch_B6 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (3991.621, 4050.9358, 1123.8754), (0.0, 0.0, -0.0), (0.1833, 1.1013, 0.9750), "DV_BP_DM_Mines_Scaffolding_Arch_B6_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_DM_Mines_Scaffolding_Arch_B60 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (1401.3896, 4460.7744, 844.6625), (0.0, 0.0, -0.0), (1.1013, 0.1833, 0.9750), "DV_BP_DM_Mines_Scaffolding_Arch_B60_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_DM_Mines_Scaffolding_Arch_B61 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (1401.3898, 4739.8057, 844.6625), (0.0, 0.0, -0.0), (1.1013, 0.1833, 0.9750), "DV_BP_DM_Mines_Scaffolding_Arch_B61_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_DM_Mines_Scaffolding_Arch_B62 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (1086.687, 4077.5405, 848.18054), (0.0, 0.0, -0.0), (0.1833, 1.1013, 0.9750), "DV_BP_DM_Mines_Scaffolding_Arch_B62_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_DM_Mines_Scaffolding_Arch_B63 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (909.63324, 4096.6025, 848.18054), (0.0, 0.0, -0.0), (0.1833, 1.1013, 0.9750), "DV_BP_DM_Mines_Scaffolding_Arch_B63_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_DM_Mines_Scaffolding_Arch_B9 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (3646.6729, 3713.8408, 1120.8815), (0.0, 0.0, -0.0), (1.1013, 0.1833, 0.9750), "DV_BP_DM_Mines_Scaffolding_Arch_B9_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_DM_Mines_Scaffolding_Beam_2M_B_2 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (2418.663, 799.3196, 832.21185), (0.0, 0.0, -0.0), (1.6176, 1.1788, 0.6034), "DV_BP_DM_Mines_Scaffolding_Beam_2M_B_2_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_DM_Mines_Scaffolding_Beam_3M_C_2 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (2478.3784, 820.7727, 823.22534), (0.0, 0.0, -0.0), (0.3977, 2.7728, 0.8923), "DV_BP_DM_Mines_Scaffolding_Beam_3M_C_2_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_DM_Mines_Scaffolding_Platform_1X1M_A_2 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (2351.8792, 1079.7357, 1007.44653), (0.0, 0.0, -0.0), (1.4423, 1.4459, 0.2743), "DV_BP_DM_Mines_Scaffolding_Platform_1X1M_A_2_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_DM_Mines_Scaffolding_Platform_3X3M_B2 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (3348.7576, 3990.046, 817.6372), (0.0, 0.0, -0.0), (3.7175, 3.7755, 0.8745), "DV_BP_DM_Mines_Scaffolding_Platform_3X3M_B2_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_DM_Mines_Scaffolding_Platform_3X3M_B3 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (1179.0199, 2739.7476, 802.9574), (0.0, 0.0, -0.0), (3.7136, 3.7822, 0.5750), "DV_BP_DM_Mines_Scaffolding_Platform_3X3M_B3_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_DM_Mines_Scaffolding_Platform_3X3M_B4 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (2712.8882, 5428.4673, 808.3266), (0.0, 0.0, -0.0), (2.7141, 3.3492, 0.8527), "DV_BP_DM_Mines_Scaffolding_Platform_3X3M_B4_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_DM_Mines_Scaffolding_Platform_3X3M_B5 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (3446.6797, 1739.4988, 807.3001), (0.0, 0.0, -0.0), (2.6445, 3.3088, 0.6171), "DV_BP_DM_Mines_Scaffolding_Platform_3X3M_B5_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_DM_Mines_Scaffolding_Platform_3X3M_B6 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (4757.233, 2584.2705, 822.8964), (0.0, 0.0, -0.0), (3.1433, 3.6180, 0.4114), "DV_BP_DM_Mines_Scaffolding_Platform_3X3M_B6_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_DM_Mines_Scaffolding_Platform_3X3M_B7 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (5088.711, 899.4994, 809.1433), (0.0, 0.0, -0.0), (3.1433, 3.6180, 0.4114), "DV_BP_DM_Mines_Scaffolding_Platform_3X3M_B7_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_DM_Mines_Scaffolding_Post_2M_A_2 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (4603.1406, 2608.7173, 1085.3137), (0.0, 0.0, -0.0), (1.9885, 0.1153, 0.2052), "DV_BP_DM_Mines_Scaffolding_Post_2M_A_2_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_DM_Mines_Scaffolding_Post_2M_A2 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (4403.1436, 2609.671, 1084.9285), (0.0, 0.0, -0.0), (1.9885, 0.1154, 0.2052), "DV_BP_DM_Mines_Scaffolding_Post_2M_A2_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_DM_Mines_Scaffolding_Post_2M_A3_6 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (4603.1406, 2757.7627, 1328.3608), (0.0, 0.0, -0.0), (1.9885, 0.1153, 0.2052), "DV_BP_DM_Mines_Scaffolding_Post_2M_A3_6_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_DM_Mines_Scaffolding_Post_2M_B_2 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (3867.6304, 5463.164, 1208.0703), (0.0, 0.0, -0.0), (2.1147, 0.0774, 0.2005), "DV_BP_DM_Mines_Scaffolding_Post_2M_B_2_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_DM_Mines_Scaffolding_Post_2M_B10 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (2892.5393, 1342.2764, 1010.02985), (0.0, 0.0, -0.0), (0.7410, 2.0933, 0.2597), "DV_BP_DM_Mines_Scaffolding_Post_2M_B10_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_DM_Mines_Scaffolding_Post_2M_B11 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (1455.3091, 305.82422, 835.61273), (0.0, 0.0, -0.0), (1.4627, 1.7374, 0.5767), "DV_BP_DM_Mines_Scaffolding_Post_2M_B11_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_DM_Mines_Scaffolding_Post_2M_B2_8 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (2896.9165, 1407.0947, 1004.22266), (0.0, 0.0, -0.0), (2.1174, 0.5647, 0.0774), "DV_BP_DM_Mines_Scaffolding_Post_2M_B2_8_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_DM_Mines_Scaffolding_Post_2M_B3 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (1557.2214, 4763.7324, 809.37335), (0.0, 0.0, -0.0), (1.6515, 1.6192, 0.2834), "DV_BP_DM_Mines_Scaffolding_Post_2M_B3_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_DM_Mines_Scaffolding_Post_2M_B4 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (3308.7153, 4037.9392, 803.43585), (0.0, 0.0, -0.0), (0.7869, 2.0455, 0.5746), "DV_BP_DM_Mines_Scaffolding_Post_2M_B4_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_DM_Mines_Scaffolding_Post_2M_B5 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (3507.9268, 5391.2905, 819.81104), (0.0, 0.0, -0.0), (1.1340, 1.9822, 0.1055), "DV_BP_DM_Mines_Scaffolding_Post_2M_B5_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_DM_Mines_Scaffolding_Post_2M_B6 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (1102.3075, 2733.5894, 814.069), (0.0, 0.0, -0.0), (0.7195, 2.0991, 0.2138), "DV_BP_DM_Mines_Scaffolding_Post_2M_B6_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_DM_Mines_Scaffolding_Post_2M_B7 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (3553.589, 1617.4923, 795.79694), (0.0, 0.0, -0.0), (1.6515, 1.6192, 0.2834), "DV_BP_DM_Mines_Scaffolding_Post_2M_B7_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_DM_Mines_Scaffolding_Post_2M_B8 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (3254.1226, 1260.4564, 806.8662), (0.0, 0.0, -0.0), (1.1326, 1.9752, 0.2834), "DV_BP_DM_Mines_Scaffolding_Post_2M_B8_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_DM_Mines_Scaffolding_Post_2M_B9 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (3510.4749, 1740.2323, 812.6455), (0.0, 0.0, -0.0), (1.4285, 1.7988, 0.4239), "DV_BP_DM_Mines_Scaffolding_Post_2M_B9_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_DM_Mines_Scaffolding_Post_3M_A_2 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (4689.582, 2898.6511, 1347.5139), (0.0, 0.0, -0.0), (0.1098, 2.9877, 0.2013), "DV_BP_DM_Mines_Scaffolding_Post_3M_A_2_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_DM_Mines_Scaffolding_Post_3M_A10 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (3318.3953, 3909.2922, 825.36035), (0.0, 0.0, -0.0), (2.9932, 0.3751, 0.3517), "DV_BP_DM_Mines_Scaffolding_Post_3M_A10_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_DM_Mines_Scaffolding_Post_3M_A11 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (3643.71, 5246.501, 812.733), (0.0, 0.0, -0.0), (2.9634, 0.6853, 0.5586), "DV_BP_DM_Mines_Scaffolding_Post_3M_A11_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_DM_Mines_Scaffolding_Post_3M_A12 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (3365.1147, 3594.6133, 979.2748), (0.0, 0.0, -0.0), (1.8420, 0.3518, 2.5647), "DV_BP_DM_Mines_Scaffolding_Post_3M_A12_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_DM_Mines_Scaffolding_Post_3M_A13 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (3373.7654, 3620.4849, 975.371), (0.0, 0.0, -0.0), (1.7982, 0.5326, 2.5188), "DV_BP_DM_Mines_Scaffolding_Post_3M_A13_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_DM_Mines_Scaffolding_Post_3M_A14 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (1195.6664, 2649.212, 825.8619), (0.0, 0.0, -0.0), (2.9959, 0.3508, 0.2352), "DV_BP_DM_Mines_Scaffolding_Post_3M_A14_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_DM_Mines_Scaffolding_Post_3M_A15 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (1917.1704, 2853.9478, 844.0496), (0.0, 0.0, -0.0), (1.6741, 2.4589, 1.2831), "DV_BP_DM_Mines_Scaffolding_Post_3M_A15_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_DM_Mines_Scaffolding_Post_3M_A16_6 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (3202.4966, 1175.4341, 801.3638), (0.0, 0.0, -0.0), (2.9055, 1.1124, 0.2963), "DV_BP_DM_Mines_Scaffolding_Post_3M_A16_6_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_DM_Mines_Scaffolding_Post_3M_A17 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (3362.7847, 1753.5786, 814.7776), (0.0, 0.0, -0.0), (1.9393, 2.5193, 0.3668), "DV_BP_DM_Mines_Scaffolding_Post_3M_A17_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_DM_Mines_Scaffolding_Post_3M_A18 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (2356.0476, 895.4036, 952.31396), (0.0, 0.0, -0.0), (1.7118, 0.5615, 2.6526), "DV_BP_DM_Mines_Scaffolding_Post_3M_A18_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_DM_Mines_Scaffolding_Post_3M_A19 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (2338.7185, 874.41296, 948.0204), (0.0, 0.0, -0.0), (1.5302, 0.9847, 2.6150), "DV_BP_DM_Mines_Scaffolding_Post_3M_A19_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_DM_Mines_Scaffolding_Post_3M_A20 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (1404.0841, 334.7999, 854.5019), (0.0, 0.0, -0.0), (2.1587, 2.3350, 0.4745), "DV_BP_DM_Mines_Scaffolding_Post_3M_A20_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_DM_Mines_Scaffolding_Post_3M_A21 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (5078.98, 592.5196, 952.31396), (0.0, 0.0, -0.0), (1.4229, 1.0478, 2.6526), "DV_BP_DM_Mines_Scaffolding_Post_3M_A21_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_DM_Mines_Scaffolding_Post_3M_A22 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (5076.0767, 619.58295, 948.0204), (0.0, 0.0, -0.0), (1.6568, 0.6618, 2.6150), "DV_BP_DM_Mines_Scaffolding_Post_3M_A22_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_DM_Mines_Scaffolding_Post_3M_A6 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (3767.932, 5603.5317, 1210.0236), (0.0, 0.0, -0.0), (0.1098, 2.9877, 0.2013), "DV_BP_DM_Mines_Scaffolding_Post_3M_A6_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_DM_Mines_Scaffolding_Post_3M_A9 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (1372.8104, 4650.0024, 815.6221), (0.0, 0.0, -0.0), (0.4034, 2.9917, 0.4219), "DV_BP_DM_Mines_Scaffolding_Post_3M_A9_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_DM_Mines_Scaffolding_Support_1M_5 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (3427.2322, 3688.1458, 873.13153), (0.0, 0.0, -0.0), (0.8471, 0.4544, 1.0094), "DV_BP_DM_Mines_Scaffolding_Support_1M_5_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_DM_Mines_Scaffolding_Support_1M2 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (2260.479, 835.26746, 846.8518), (0.0, 0.0, -0.0), (0.7062, 0.5825, 1.0276), "DV_BP_DM_Mines_Scaffolding_Support_1M2_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_DM_Mines_Scaffolding_Support_1M3 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (5102.7593, 702.89886, 846.852), (0.0, 0.0, -0.0), (0.7941, 0.4540, 1.0276), "DV_BP_DM_Mines_Scaffolding_Support_1M3_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_DM_Mines_Scaffolding_Support_2M_2 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (1566.0177, 5071.515, 1820.0149), (0.0, 0.0, -0.0), (1.1187, 1.9457, 0.2858), "DV_BP_DM_Mines_Scaffolding_Support_2M_2_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_DM_Mines_Scaffolding_Support_2M2 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (2088.54, 5314.3193, 1921.2125), (0.0, 0.0, -0.0), (1.1187, 1.9457, 0.2858), "DV_BP_DM_Mines_Scaffolding_Support_2M2_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_DM_Mines_Scaffolding_Support_2M3 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (1043.4946, 4828.71, 1718.8174), (0.0, 0.0, -0.0), (1.1187, 1.9457, 0.2858), "DV_BP_DM_Mines_Scaffolding_Support_2M3_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_DM_Mines_Scaffolding_Support_2M4_9 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (1488.1863, 5237.8535, 1822.792), (0.0, 0.0, -0.0), (1.1187, 1.9457, 0.2858), "DV_BP_DM_Mines_Scaffolding_Support_2M4_9_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_DM_Mines_Scaffolding_Support_2M5 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (2010.7081, 5480.6577, 1923.9896), (0.0, 0.0, -0.0), (1.1187, 1.9457, 0.2858), "DV_BP_DM_Mines_Scaffolding_Support_2M5_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_DM_Mines_Scaffolding_Support_2M6 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (965.6632, 4995.0483, 1721.5945), (0.0, 0.0, -0.0), (1.1187, 1.9457, 0.2858), "DV_BP_DM_Mines_Scaffolding_Support_2M6_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_DM_Mines_Scaffolding_Support_2M7 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (4102.209, 3997.0874, 1986.7133), (0.0, 0.0, -0.0), (1.8681, 1.2448, 0.2555), "DV_BP_DM_Mines_Scaffolding_Support_2M7_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_DM_Mines_Scaffolding_Support_2M8 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (3807.1125, 3492.04, 1995.0472), (0.0, 0.0, -0.0), (1.8681, 1.2448, 0.2555), "DV_BP_DM_Mines_Scaffolding_Support_2M8_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_DM_Mines_Scaffolding_Support_2M9 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (4397.3057, 4502.1367, 1978.3799), (0.0, 0.0, -0.0), (1.8681, 1.2448, 0.2555), "DV_BP_DM_Mines_Scaffolding_Support_2M9_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_DM_Mines_Scaffolding_Support_3M_2 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (1967.3634, 5203.4243, 1889.3397), (0.0, 0.0, -0.0), (2.8347, 1.5155, 0.7374), "DV_BP_DM_Mines_Scaffolding_Support_3M_2_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_DM_Mines_Scaffolding_Support_3M2 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (1699.4037, 5078.908, 1837.4435), (0.0, 0.0, -0.0), (2.8347, 1.5155, 0.7374), "DV_BP_DM_Mines_Scaffolding_Support_3M2_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_DM_Mines_Scaffolding_Support_3M3 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (1431.4443, 4954.3906, 1785.5472), (0.0, 0.0, -0.0), (2.8347, 1.5155, 0.7374), "DV_BP_DM_Mines_Scaffolding_Support_3M3_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_DM_Mines_Scaffolding_Support_3M4 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (1163.4844, 4829.874, 1733.6487), (0.0, 0.0, -0.0), (2.8347, 1.5155, 0.7374), "DV_BP_DM_Mines_Scaffolding_Support_3M4_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_DM_Mines_Scaffolding_Support_3M5 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (3814.424, 3672.713, 1987.5879), (0.0, 0.0, -0.0), (1.7560, 2.7392, 0.2645), "DV_BP_DM_Mines_Scaffolding_Support_3M5_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_DM_Mines_Scaffolding_Support_3M6 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (3965.755, 3931.7124, 1983.3136), (0.0, 0.0, -0.0), (1.7560, 2.7392, 0.2645), "DV_BP_DM_Mines_Scaffolding_Support_3M6_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_DM_Mines_Scaffolding_Support_3M7 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (4117.0825, 4190.7144, 1979.0399), (0.0, 0.0, -0.0), (1.7560, 2.7392, 0.2645), "DV_BP_DM_Mines_Scaffolding_Support_3M7_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_DM_Mines_Scaffolding_Support_3M8 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (4268.414, 4449.7104, 1974.764), (0.0, 0.0, -0.0), (1.7560, 2.7392, 0.2645), "DV_BP_DM_Mines_Scaffolding_Support_3M8_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_DM_Warehouse_Crate_A_Lid_Breakable_2 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (983.97644, 2728.8115, 810.1689), (0.0, 0.0, -0.0), (0.7520, 0.7564, 0.1705), "DV_BP_DM_Warehouse_Crate_A_Lid_Breakable_2_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_DM_Warehouse_Crate_A_open_Breakable_10 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (4089.874, 2365.0432, 912.9661), (0.0, 0.0, -0.0), (0.8939, 0.8407, 0.7575), "DV_BP_DM_Warehouse_Crate_A_open_Breakable_10_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_DM_Warehouse_Crate_B_Breakable2_3 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (5710.2427, 3961.428, 827.7556), (0.0, 0.0, -0.0), (1.3243, 1.0389, 0.5490), "DV_BP_DM_Warehouse_Crate_B_Breakable2_3_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_DM_Warehouse_Crate_B_Breakable3_10 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (2050.0337, 775.79694, 884.0897), (0.0, 0.0, -0.0), (1.2508, 1.0816, 0.9966), "DV_BP_DM_Warehouse_Crate_B_Breakable3_10_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_DM_Warren_Lighting_Torch_Breakable_23 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (3252.3442, 3188.4805, 861.6902), (0.0, 0.0, -0.0), (1.0112, 1.0765, 1.9128), "DV_BP_DM_Warren_Lighting_Torch_Breakable_23_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_DM_Warren_Lighting_Torch_Breakable2_29 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (5339.35, 3819.879, 1177.3278), (0.0, 0.0, -0.0), (1.0112, 1.0765, 1.9128), "DV_BP_DM_Warren_Lighting_Torch_Breakable2_29_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_DM_Warren_Lighting_Torch_Breakable3_32 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (4195.0625, 2257.4578, 864.82574), (0.0, 0.0, -0.0), (1.0112, 1.0765, 1.9128), "DV_BP_DM_Warren_Lighting_Torch_Breakable3_32_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_DM_Warren_Lighting_Torch_Breakable4_35 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (2500.6262, 1622.9646, 1497.0239), (0.0, 0.0, -0.0), (1.0112, 1.0765, 1.9128), "DV_BP_DM_Warren_Lighting_Torch_Breakable4_35_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_DM_Warren_Lighting_Torch_Breakable5_38 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (2334.0818, 2526.8474, 1561.4254), (0.0, 0.0, -0.0), (1.0112, 1.0765, 1.9128), "DV_BP_DM_Warren_Lighting_Torch_Breakable5_38_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_DM_Warren_Lighting_Torch_Breakable6_41 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (1193.4575, 2502.0342, 910.1032), (0.0, 0.0, -0.0), (1.0112, 1.0765, 1.9128), "DV_BP_DM_Warren_Lighting_Torch_Breakable6_41_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_DM_Workshop_Barrel_Breakable3_21 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (3295.5383, 3480.9453, 877.3144), (0.0, 0.0, -0.0), (1.0531, 1.0721, 0.8538), "DV_BP_DM_Workshop_Barrel_Breakable3_21_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_DM_Workshop_Barrel_Breakable4_26 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (3988.6848, 5296.881, 909.52496), (0.0, 0.0, -0.0), (0.8004, 0.7330, 0.8538), "DV_BP_DM_Workshop_Barrel_Breakable4_26_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_DM_Workshop_Scatter_Bucket_Metal_Breakable_2 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (5803.775, 3999.387, 836.7001), (0.0, 0.0, -0.0), (0.6754, 0.6754, 0.7337), "DV_BP_DM_Workshop_Scatter_Bucket_Metal_Breakable_2_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_DM_Workshop_Scatter_Bucket_Metal_Breakable3_8 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (5020.193, 3874.839, 1241.2942), (0.0, 0.0, -0.0), (0.6754, 0.6754, 0.7337), "DV_BP_DM_Workshop_Scatter_Bucket_Metal_Breakable3_8_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_DM_Workshop_Scatter_Bucket_Metal_Breakable4_11 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (4532.9917, 2433.8643, 828.9832), (0.0, 0.0, -0.0), (0.7212, 0.7220, 0.8158), "DV_BP_DM_Workshop_Scatter_Bucket_Metal_Breakable4_11_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_DM_Workshop_Scatter_Bucket_Metal_Breakable6_18 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (2373.7998, 2576.5408, 1546.1107), (0.0, 0.0, -0.0), (0.6754, 0.6754, 0.7337), "DV_BP_DM_Workshop_Scatter_Bucket_Metal_Breakable6_18_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_DM_Workshop_Scatter_Bucket_Metal_Breakable7_2 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (2437.8547, 5335.9614, 843.55566), (0.0, 0.0, -0.0), (0.6754, 0.7210, 0.7754), "DV_BP_DM_Workshop_Scatter_Bucket_Metal_Breakable7_2_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_DM_Workshop_Scatter_Sandbags_D_Breakable2_5 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (4103.4585, 2371.34, 922.5113), (0.0, 0.0, -0.0), (0.4539, 0.5183, 0.8358), "DV_BP_DM_Workshop_Scatter_Sandbags_D_Breakable2_5_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_Mines_Brace_C_2 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (2488.284, 5422.2954, 905.6493), (0.0, 0.0, -0.0), (2.1108, 1.1906, 3.1177), "DV_BP_Mines_Brace_C_2_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_Mines_Ceiling_Brace_A_2 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (3970.6292, 3709.9531, 1590.4661), (0.0, 0.0, -0.0), (3.7809, 3.7809, 7.9093), "DV_BP_Mines_Ceiling_Brace_A_2_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_Mines_Ceiling_Brace_A2 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (4373.712, 4406.6055, 1583.3011), (0.0, 0.0, -0.0), (3.7977, 3.7977, 7.9093), "DV_BP_Mines_Ceiling_Brace_A2_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_Mines_Ceiling_Brace_A3_12 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (2352.0674, 1355.497, 1690.4661), (0.0, 0.0, -0.0), (3.4960, 3.5576, 7.9093), "DV_BP_Mines_Ceiling_Brace_A3_12_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_Mines_Ceiling_Brace_A4_2 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (2022.8356, 5345.786, 1190.4661), (0.0, 0.0, -0.0), (3.6790, 3.7454, 7.9093), "DV_BP_Mines_Ceiling_Brace_A4_2_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_Mines_Ceiling_Brace_A5 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (2022.8356, 5345.786, 1940.4661), (0.0, 0.0, -0.0), (3.6790, 3.7454, 7.9093), "DV_BP_Mines_Ceiling_Brace_A5_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_Mines_Ceiling_Brace_A6 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (1013.2181, 4908.0957, 1190.4661), (0.0, 0.0, -0.0), (3.6790, 3.7454, 7.9093), "DV_BP_Mines_Ceiling_Brace_A6_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_Mines_Ceiling_Brace_A7 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (1013.2181, 4908.0957, 1940.4661), (0.0, 0.0, -0.0), (3.6790, 3.7454, 7.9093), "DV_BP_Mines_Ceiling_Brace_A7_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_Mines_Machine_Whim_Wheel_Middle_Bracket_2 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (4260.2417, 2363.813, 951.1931), (0.0, 0.0, -0.0), (0.6753, 2.5217, 3.6924), "DV_BP_Mines_Machine_Whim_Wheel_Middle_Bracket_2_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_Mines_Machine_Whim_Wheel_Middle_Bracket2 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (4991.983, 514.87634, 808.50885), (0.0, 0.0, -0.0), (2.0892, 3.8655, 0.7948), "DV_BP_Mines_Machine_Whim_Wheel_Middle_Bracket2_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_Mines_Support_Beam_2 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (2405.4922, 5377.9614, 893.68384), (0.0, 0.0, -0.0), (0.8656, 0.8656, 3.8737), "DV_BP_Mines_Support_Beam_2_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_Mines_Support_Beam_B_2 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (2283.4705, 5334.386, 1079.663), (0.0, 0.0, -0.0), (2.9680, 1.3464, 0.2910), "DV_BP_Mines_Support_Beam_B_2_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_Mines_Support_Beam_B2 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (2346.2612, 5519.195, 1069.663), (0.0, 0.0, -0.0), (1.3464, 2.9680, 0.2910), "DV_BP_Mines_Support_Beam_B2_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_Mines_Support_Beam_B3_2 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (2821.7788, 5622.7954, 790.2455), (0.0, 0.0, -0.0), (1.0593, 3.0406, 0.6710), "DV_BP_Mines_Support_Beam_B3_2_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: DecorationBlockingVolume_1 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (3335.2117, 2655.3298, 1204.592), (0.0, 34.38768838527877, -0.0), (7.2192, 22.4364, 9.9259), "DV_DecorationBlockingVolume_1", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: DecorationBlockingVolume_2 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (3200.0, 400.0, 1050.0), (0.0, 0.0, -0.0), (5.0000, 12.0000, 5.0000), "DV_DecorationBlockingVolume_2", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: DecorationBlockingVolume_4 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (6000.0, 3200.0, 1050.0), (0.0, 0.0, -0.0), (12.0000, 5.0000, 5.0000), "DV_DecorationBlockingVolume_4", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: DecorationBlockingVolume_6 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (3200.0, 6000.0, 1050.0), (0.0, 0.0, -0.0), (5.0000, 12.0000, 5.0000), "DV_DecorationBlockingVolume_6", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: DecorationBlockingVolume_8 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (400.0, 3200.0, 1050.0), (0.0, 0.0, -0.0), (12.0000, 5.0000, 5.0000), "DV_DecorationBlockingVolume_8", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: Deep_WoodenPlank_A_50 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (3332.2583, 1565.4492, 805.7868), (0.0, 0.0, -0.0), (1.8130, 5.9537, 0.8549), "DV_Deep_WoodenPlank_A_50_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: Deep_WoodenPlank_B_26 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (2073.6387, 4992.046, 800.0024), (0.0, 0.0, -0.0), (6.0335, 2.2523, 0.1689), "DV_Deep_WoodenPlank_B_26_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: Deep_WoodenPlank_B10 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (3449.7388, 3603.2947, 1056.941), (0.0, 0.0, -0.0), (3.4618, 1.1306, 5.2270), "DV_Deep_WoodenPlank_B10_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: Deep_WoodenPlank_B11 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (2192.592, 909.5174, 1062.9434), (0.0, 0.0, -0.0), (2.1199, 2.0925, 5.7574), "DV_Deep_WoodenPlank_B11_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: Deep_WoodenPlank_B12 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (2277.2644, 912.4833, 1034.5958), (0.0, 0.0, -0.0), (3.2168, 1.8827, 5.4264), "DV_Deep_WoodenPlank_B12_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: Deep_WoodenPlank_B13 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (5203.3125, 699.56104, 1062.9434), (0.0, 0.0, -0.0), (2.3508, 1.0776, 5.7574), "DV_Deep_WoodenPlank_B13_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: Deep_WoodenPlank_B14 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (5146.256, 636.9287, 1034.5958), (0.0, 0.0, -0.0), (2.9815, 2.0143, 5.4264), "DV_Deep_WoodenPlank_B14_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: Deep_WoodenPlank_B9_165 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (3529.639, 3634.7224, 1081.6406), (0.0, 0.0, -0.0), (2.5429, 1.7287, 5.6363), "DV_Deep_WoodenPlank_B9_165_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: DM_Mines_Machine_Whim_Side_Bracket_Destructible_15 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (4267.776, 4416.634, 1244.5807), (0.0, 0.0, -0.0), (1.7071, 2.1742, 2.2422), "DV_DM_Mines_Machine_Whim_Side_Bracket_Destructible_15_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: DM_Mines_Machine_Whim_Side_Bracket_Destructible12_2 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (1234.9918, 4855.0396, 1666.751), (0.0, 0.0, -0.0), (2.5185, 1.5413, 2.5759), "DV_DM_Mines_Machine_Whim_Side_Bracket_Destructible12_2_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: DM_Mines_Machine_Whim_Side_Bracket_Destructible2_21 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (3834.166, 3741.8503, 1260.067), (0.0, 0.0, -0.0), (1.7071, 2.1742, 2.2422), "DV_DM_Mines_Machine_Whim_Side_Bracket_Destructible2_21_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: DM_Mines_Machine_Whim_Side_Bracket_Destructible3 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (4188.691, 4293.547, 1977.1031), (0.0, 0.0, -0.0), (1.7798, 2.2871, 2.2566), "DV_DM_Mines_Machine_Whim_Side_Bracket_Destructible3_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: DM_Mines_Machine_Whim_Side_Bracket_Destructible4 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (4339.0283, 4196.9053, 1977.1023), (0.0, 0.0, -0.0), (1.7798, 2.2871, 2.2566), "DV_DM_Mines_Machine_Whim_Side_Bracket_Destructible4_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: DM_Mines_Machine_Whim_Side_Bracket_Destructible5_23 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (1876.6952, 5162.319, 1788.3558), (0.0, 0.0, -0.0), (2.5185, 1.5413, 2.5759), "DV_DM_Mines_Machine_Whim_Side_Bracket_Destructible5_23_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: DM_Mines_Machine_Whim_Side_Bracket_Destructible6 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (2563.0642, 1300.58, 2046.4688), (0.0, 0.0, -0.0), (2.2686, 1.1482, 2.2422), "DV_DM_Mines_Machine_Whim_Side_Bracket_Destructible6_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: DM_Mines_Machine_Whim_Side_Bracket_Destructible7 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (2493.7612, 1492.1726, 2046.4688), (0.0, 0.0, -0.0), (2.2686, 1.1482, 2.2422), "DV_DM_Mines_Machine_Whim_Side_Bracket_Destructible7_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: DM_Mines_Scaffolding_Platform_3X1M_A_Destructible5 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (3528.3127, 5339.255, 806.509), (0.0, 0.0, -0.0), (1.6415, 3.2072, 0.3978), "DV_DM_Mines_Scaffolding_Platform_3X1M_A_Destructible5_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: Mines_Plank_3M_A_23 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (1429.5245, 4258.9805, 800.0021), (0.0, 0.0, -0.0), (1.8307, 2.7052, 0.0527), "DV_Mines_Plank_3M_A_23_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: Mines_Plank_3M_A2 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (3953.6, 4611.8403, 822.041), (0.0, 0.0, -0.0), (0.3158, 3.0227, 0.2494), "DV_Mines_Plank_3M_A2_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: Mines_Plank_3M_A3_61 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (4719.151, 2567.9944, 837.5006), (0.0, 0.0, -0.0), (2.0624, 2.5564, 0.1250), "DV_Mines_Plank_3M_A3_61_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: Mines_Plank_3M_A4 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (5037.6963, 893.561, 821.5504), (0.0, 0.0, -0.0), (2.0624, 2.5564, 0.1250), "DV_Mines_Plank_3M_A4_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: Mines_Plank_3M_A5 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (5572.562, 1317.7838, 853.0775), (0.0, 0.0, -0.0), (2.8197, 1.3384, 0.8496), "DV_Mines_Plank_3M_A5_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: Mines_Plank_3M_A6 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (5596.136, 1349.1943, 844.98975), (0.0, 0.0, -0.0), (2.1603, 2.3073, 1.0140), "DV_Mines_Plank_3M_A6_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: Mines_Plank_3M_B_32 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (1514.9846, 4555.554, 802.88165), (0.0, 0.0, -0.0), (1.2079, 0.2713, 0.0745), "DV_Mines_Plank_3M_B_32_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: Mines_Plank_3M_B2 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (3877.9575, 5167.928, 803.74805), (0.0, 0.0, -0.0), (0.8804, 1.1657, 0.1598), "DV_Mines_Plank_3M_B2_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: Mines_Plank_3M_B3 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (3645.0254, 5196.31, 809.8614), (0.0, 0.0, -0.0), (0.8804, 1.1657, 0.1598), "DV_Mines_Plank_3M_B3_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: Mines_Plank_3M_B5 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (1807.33, 2855.829, 811.68726), (0.0, 0.0, -0.0), (1.2087, 0.2713, 0.2099), "DV_Mines_Plank_3M_B5_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: Mines_Plank_3M_B6 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (1563.17, 2758.581, 812.82666), (0.0, 0.0, -0.0), (0.3491, 1.2195, 0.2204), "DV_Mines_Plank_3M_B6_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: Mines_Plank_3M_B7 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (3084.6772, 1187.5352, 818.7994), (0.0, 0.0, -0.0), (0.5223, 1.2380, 0.1135), "DV_Mines_Plank_3M_B7_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: Mines_Plank_3M_B8_58 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (4660.1797, 2412.6777, 815.8465), (0.0, 0.0, -0.0), (0.9821, 1.0988, 0.2535), "DV_Mines_Plank_3M_B8_58_BRK", _folder)
if a: placed += 1
else: skipped += 1

# ======================================================================
# SUMMARY
# ======================================================================
unreal.log(f"[{BUBBLE_NAME}] Reconstruction complete: {placed} placed, {skipped} skipped, {errors} errors")
