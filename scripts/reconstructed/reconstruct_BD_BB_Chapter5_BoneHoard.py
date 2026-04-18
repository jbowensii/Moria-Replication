"""Auto-generated level reconstruction script.
Bubble: BD_BB_Chapter5_BoneHoard
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

BUBBLE_NAME = "BD_BB_Chapter5_BoneHoard"
placed = 0
skipped = 0
errors = 0

# ======================================================================
# PHASE 1: InstancedMeshCatalog  (static mesh placement)
# ======================================================================
unreal.log(f"[{BUBBLE_NAME}] Phase 1: Placing static meshes...")

# Batch 0: StaticMesh'Cube' (2 instances)
_mesh_path = "/Engine/BasicShapes/Cube"
_materials = ['/Engine/BasicShapes/BasicShapeMaterial']
_folder = "Reconstruction/BD_BB_Chapter5_BoneHoard/Meshes"
a = spawn_static_mesh(_mesh_path, _materials, (6450.0, 8550.0, 1250.0), (0.0, -15.000058335092751, 0.0), (1.0, 1.0, 1.0), "ColumnDummy", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (6400.0, 6400.0, 6800.0), (0.0, 0.0, -0.0), (1.0, 1.0, 1.0), "MASTERCONTROLUNIT", _folder)
if a: placed += 1
else: skipped += 1

# Batch 1: StaticMesh'Cube' (8 instances)
_mesh_path = "/Engine/BasicShapes/Cube"
_materials = ['/Game/Unshippable/WhiteboxMaterials/MI_WB_Grid_DarkGrey']
_folder = "Reconstruction/BD_BB_Chapter5_BoneHoard/Meshes"
a = spawn_static_mesh(_mesh_path, _materials, (3200.0, 12800.0, 3200.0), (90.0, -90.00000904691218, -180.0000056091651), (64.0, 64.0, 2.021348), "staticMeshFloor10_18", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (9600.0, 2.7827148, 3200.0), (90.0, -90.00000904691218, -180.0000056091651), (64.0, 64.0, 2.021348), "staticMeshFloor11", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (9600.0, 12800.0, 3200.0), (90.0, -90.00000904691218, -180.0000056091651), (64.0, 64.0, 2.021348), "staticMeshFloor12_19", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (0.0, 3200.0, 3200.0), (90.0, -2.6272043122370463, -182.62721276416505), (64.0, 64.0, 2.021348), "staticMeshFloor13", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (12700.0, 3200.0005, 3200.0), (90.0, -2.6272079662521186, -182.6272221534191), (64.0, 64.0, 2.021348), "staticMeshFloor14", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (12800.0, 9600.0, 4800.0), (90.0, -33.66481611721513, -213.66481008012312), (32.366535, 64.0, 2.021348), "staticMeshFloor15", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (0.0, 9600.0, 4800.0), (90.0, -168.79966663229533, -348.7996304097463), (32.366535, 64.0, 2.021348), "staticMeshFloor16", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3200.0005, 2.8554688, 3200.0), (90.0, -90.00000904691218, -180.0000056091651), (64.0, 64.0, 2.021348), "staticMeshFloor9", _folder)
if a: placed += 1
else: skipped += 1

# Batch 2: StaticMesh'Cube' (4 instances)
_mesh_path = "/Engine/BasicShapes/Cube"
_materials = ['/Game/Environments/ProcTexturing/ProcMaterial_Quarry_Ceilling_Fissure_8x8']
_folder = "Reconstruction/BD_BB_Chapter5_BoneHoard/Meshes"
a = spawn_static_mesh(_mesh_path, _materials, (3200.0, 9600.002, 6400.0), (0.0, 90.0000030488508, -0.0), (64.0, 64.0, 2.021348), "staticMeshFloor2", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3200.0022, 3174.3193, 6400.0), (0.0, 90.0000030488508, -0.0), (64.0, 64.0, 2.021348), "staticMeshFloor4", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (9600.0, 9599.93, 6400.0), (0.0, 90.0000030488508, -0.0), (64.0, 64.0, 2.021348), "staticMeshFloor6", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (9600.0, 3174.2478, 6400.0), (0.0, 90.0000030488508, -0.0), (64.0, 64.0, 2.021348), "staticMeshFloor8", _folder)
if a: placed += 1
else: skipped += 1

# Batch 3: StaticMesh'Plane' (1 instances)
_mesh_path = "/Engine/BasicShapes/Plane"
_materials = ['/Game/Unshippable/ThirdParty/FantasyDungeon/Materials/BaseMaterials/black']
_folder = "Reconstruction/BD_BB_Chapter5_BoneHoard/Meshes"
a = spawn_static_mesh(_mesh_path, _materials, (6400.0, 8550.0, 5600.0), (0.00019807550387994285, -179.99998474121372, -179.99998474121372), (32.0, 32.0, 32.0), "Plane_19", _folder)
if a: placed += 1
else: skipped += 1

# Batch 4: StaticMesh'Deep_BoneHoard_A' (1 instances)
_mesh_path = "/Game/Art/Assets/Kits/Architecture/Deep/Deep_BoneHoard_A"
_materials = ['/Game/Art/Assets/Kits/Misc/Dirt_Mounds/Materials/BoneHoard_Bone_Mount_Inst1']
_folder = "Reconstruction/BD_BB_Chapter5_BoneHoard/Meshes"
a = spawn_static_mesh(_mesh_path, _materials, (6569.8105, 8660.557, 1223.9365), (0.0, 0.0, -0.0), (1.0, 1.0, 1.0), "Deep_BoneHoard_3", _folder)
if a: placed += 1
else: skipped += 1

# Batch 5: StaticMesh'Deep_BoneHoard_B' (18 instances)
_mesh_path = "/Game/Art/Assets/Kits/Architecture/Deep/Deep_BoneHoard_B"
_materials = ['/Game/Art/Assets/Kits/Misc/Dirt_Mounds/Materials/BoneHoard_Bone_Mount_Inst1']
_folder = "Reconstruction/BD_BB_Chapter5_BoneHoard/Meshes"
a = spawn_static_mesh(_mesh_path, _materials, (8078.7783, 6871.391, 1268.7002), (-6.750668669929375e-09, 39.60531857685314, 5.472520096878396), (1.0, 1.0, 1.0), "Deep_BoneHoard_B_257", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5964.2715, 7339.856, 1250.6797), (-2.320648133614236, 57.794698248327755, -0.8481445532779399), (1.0, 1.0, 0.896281), "Deep_BoneHoard_B10", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4806.1533, 9523.536, 1251.6973), (-2.6358032154647026, 31.77854235151896, -1.7762756640671777), (1.0, 1.0, 0.7182006), "Deep_BoneHoard_B11", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5630.773, 9652.584, 1255.5635), (-1.0780028645484379, 27.104388445695534, -4.062500743557642), (1.0, 1.0, 1.4858747), "Deep_BoneHoard_B12", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (7417.448, 9760.229, 1240.061), (-3.1887818030483754, 105.40153203503871, 3.073166350617495), (1.0, 1.0, 1.1555982), "Deep_BoneHoard_B13", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5401.703, 9208.456, 1235.8569), (-3.1781614810460743, 78.16380065496648, 7.955542293487194e-06), (1.0, 1.0, 1.8482162), "Deep_BoneHoard_B14", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1475.7914, 8441.789, 800.0), (0.0, 179.999754113147, -0.0), (1.0, 1.0, 0.5), "Deep_BoneHoard_B16", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (7589.1284, 8630.855, 1265.9023), (0.03315367137246311, -74.91875727695113, 2.0315456268242995), (1.0, 1.0, 1.3935125), "Deep_BoneHoard_B18", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5773.4805, 6784.5967, 1266.2551), (0.0, -104.28776159297458, 0.0), (1.8160368, 1.8160368, 1.8160368), "Deep_BoneHoard_B19_7", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (6538.379, 10830.297, 1257.7402), (0.0, -9.57958944576006, 0.0), (1.0, 1.0, 1.53125), "Deep_BoneHoard_B2_260", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5938.064, 10562.401, 1238.6271), (-3.3103938930468417, 117.03217542508342, 2.0612996444004366), (1.0, 1.0, 1.3158219), "Deep_BoneHoard_B20", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5306.081, 6990.1685, 1245.5562), (-3.1014705995001313, -149.30403847356493, -1.1122436651522467), (1.0, 1.0, 0.8296603), "Deep_BoneHoard_B3", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4895.076, 9552.934, 1256.081), (-0.013000488526162209, 2.3846742342494553, 0.022494637881970432), (1.0, 1.0, 0.82966), "Deep_BoneHoard_B4_192", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4477.001, 9650.064, 1274.2954), (1.8044263055720833, -171.0618517009912, 0.8350961989618643), (1.0, 1.0, 1.0), "Deep_BoneHoard_B5_2", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (8159.786, 7531.0938, 1247.4434), (-1.8231506161851005, -88.13079461493066, -3.8214723103444226), (1.0, 1.0, 1.0), "Deep_BoneHoard_B6_159", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (7584.413, 10340.457, 1238.6495), (-4.379700038532013, 90.00001911157379, 9.95931397054875e-07), (1.0, 1.0, 1.4504697), "Deep_BoneHoard_B7_70", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1918.2599, 9214.232, 800.0), (0.0, -33.75002946191932, 0.0), (1.0, 1.0, 1.0), "Deep_BoneHoard_B8_9", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4999.451, 8135.154, 1241.7573), (-3.1781610990263833, -6.839843705097865, 4.918057478921887e-06), (1.0, 1.0, 1.0), "Deep_BoneHoard_B9", _folder)
if a: placed += 1
else: skipped += 1

# Batch 6: StaticMesh'Deep_BoneHoard_C' (2 instances)
_mesh_path = "/Game/Art/Assets/Kits/Architecture/Deep/Deep_BoneHoard_C"
_materials = ['/Game/Art/Assets/Kits/Misc/Dirt_Mounds/Materials/BoneHoard_Bone_Mount_Inst1']
_folder = "Reconstruction/BD_BB_Chapter5_BoneHoard/Meshes"
a = spawn_static_mesh(_mesh_path, _materials, (9288.762, 6459.649, 1345.6509), (0.0, 164.93726603121453, -0.0), (1.0, 1.0, 1.0), "Deep_BoneHoard_C_50", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3043.553, 9227.74, 1345.6509), (0.0, -29.125610859908786, 0.0), (1.0, 1.0, 1.0), "Deep_BoneHoard_C2", _folder)
if a: placed += 1
else: skipped += 1

# Batch 7: StaticMesh'Deep_BoneHoard_E' (65 instances)
_mesh_path = "/Game/Art/Assets/Kits/Architecture/Deep/Deep_BoneHoard_E"
_materials = ['/Game/Art/Assets/Kits/Misc/Dirt_Mounds/Materials/BoneHoard_Bone_Mount_Inst1']
_folder = "Reconstruction/BD_BB_Chapter5_BoneHoard/Meshes"
a = spawn_static_mesh(_mesh_path, _materials, (4922.842, 7365.079, 1268.0161), (1.6794268924639506, 111.84715294621445, 2.3169327484443825), (1.0, 1.1499317, 1.0), "Deep_BoneHoard_E_98", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (8066.4434, 8408.894, 1268.3823), (0.9937308653704723, -158.76297532997248, 0.2482039295697592), (1.0, 1.0, 1.0), "Deep_BoneHoard_E10", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1963.1251, 8943.349, 858.654), (-30.93700876033754, -160.31251431019484, 1.891721041953468e-05), (1.0, 1.0, 1.0), "Deep_BoneHoard_E11", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (6733.0244, 10796.375, 1260.1279), (0.9062771634114788, -80.82953394340794, -0.7094726815540251), (1.0, 1.0, 1.0), "Deep_BoneHoard_E12", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (7433.133, 10582.221, 1261.5112), (0.3576901562479551, -114.66284050224961, -0.22335817019998316), (1.0, 1.0, 1.0), "Deep_BoneHoard_E13", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (7171.8354, 10298.762, 1257.532), (-0.40951531847941836, 55.474453257804974, -0.6860961663727645), (1.0, 1.0, 1.5788596), "Deep_BoneHoard_E14", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (7834.5923, 7440.4897, 1265.2549), (2.3340327324168078, -158.751234260966, 0.4834208920962068), (1.0, 1.0, 1.0), "Deep_BoneHoard_E15", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (7553.897, 6443.5312, 1270.7998), (-2.9538874955103505, 115.90552596054289, 0.3972209779027719), (1.0, 1.0, 1.0), "Deep_BoneHoard_E16", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4857.0234, 9401.607, 1263.7339), (-4.384926178598597e-09, 89.99999226078143, 0.8115631839466105), (1.0, 1.0, 1.0), "Deep_BoneHoard_E17_195", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5181.7793, 9788.829, 1263.855), (-0.7981872903941345, -169.62086510340632, -0.146240244636964), (1.0, 1.0, 1.0), "Deep_BoneHoard_E18", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5222.2627, 9183.53, 1263.1748), (-0.7981872903941345, -169.62086510340632, -0.146240244636964), (1.0, 1.0, 1.0), "Deep_BoneHoard_E19", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5083.134, 8237.615, 1265.3452), (-2.999145415064171, 163.17690135418653, 0.3429339535655786), (1.0, 1.0, 1.0), "Deep_BoneHoard_E2", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5414.63, 10531.34, 1255.6572), (-0.2637023884542581, -108.96932277808578, -0.7673951033780629), (1.0, 1.0, 1.0), "Deep_BoneHoard_E20", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3746.3162, 6837.366, 1341.2173), (0.04633508298063656, 78.65897338970315, -0.6675720493110149), (1.0, 1.149932, 1.0), "Deep_BoneHoard_E21", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4235.2036, 6797.896, 1342.7858), (-0.14721680527909226, 87.09525642336257, 0.706434440621793), (1.0, 1.149932, 1.0), "Deep_BoneHoard_E22", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4344.717, 8084.8647, 1257.5137), (-1.9447024260418861, 58.36942787297336, -0.22747799095392734), (1.0, 1.0, 1.0), "Deep_BoneHoard_E23", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4885.892, 8099.0283, 1265.4336), (0.307501944077303, 67.72842595849481, 0.7508681024512625), (1.0, 1.0, 1.0), "Deep_BoneHoard_E24", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (7704.2705, 9524.515, 1262.1675), (-0.9704895099796161, 10.898345779181156, 0.5175470092854956), (1.0, 1.0, 1.0), "Deep_BoneHoard_E25", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (8392.196, 9715.154, 1262.7842), (-0.48007196209748104, -123.85796537219309, -0.25506589917335276), (1.0, 1.0, 1.0), "Deep_BoneHoard_E26", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1804.158, 8491.043, 858.63574), (-25.31145938593516, 132.18760790636367, -5.625090960337044), (1.0, 1.0, 1.0), "Deep_BoneHoard_E27", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2027.815, 8238.949, 1167.9716), (-24.60302438560346, 141.48582944254207, -12.315213936129823), (1.0, 1.0, 2.0), "Deep_BoneHoard_E28", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4735.8237, 9036.826, 1265.1611), (-3.122192271317359, 147.17623451976124, 0.9960327648922214), (1.0, 1.0, 3.1434295), "Deep_BoneHoard_E29_37", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3935.0303, 9818.955, 1341.3237), (-0.591644190762841, -136.85971152066386, 0.019941391481655996), (1.0, 1.0, 1.0), "Deep_BoneHoard_E30", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3652.4307, 10145.359, 1344.7588), (-0.47912599244255694, -41.144044884449734, -0.5338135072894987), (1.0, 1.0, 1.0), "Deep_BoneHoard_E31", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3778.9473, 10003.862, 1337.9902), (-0.9862671353599711, -135.77877179395233, 3.0389140228699616), (1.0, 1.0, 1.0), "Deep_BoneHoard_E32", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3827.4697, 9217.922, 1344.3359), (0.5690571243181458, 163.31568210645298, 0.4580309499071913), (1.0, 1.0, 1.0), "Deep_BoneHoard_E33", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (8190.5264, 8774.308, 1257.8285), (0.4086433533281652, -77.12975418311385, 0.6281933679519225), (1.0, 1.0, 1.0), "Deep_BoneHoard_E34", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (8058.428, 9352.938, 1262.3506), (0.4356362923880283, -48.04998976429967, 0.9610475935856619), (1.0, 1.0, 1.0), "Deep_BoneHoard_E35", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (7858.3574, 8510.954, 1273.3809), (-0.768249543032355, 23.050874277290916, 0.4436643434355907), (1.0, 1.0, 1.5860498), "Deep_BoneHoard_E36", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (7551.4424, 8826.794, 1275.6406), (-0.9704895099796161, 10.898345779181156, 0.5175470092854956), (1.0, 1.0, 1.0), "Deep_BoneHoard_E37", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (7356.4365, 10393.283, 1261.6157), (-1.245391909789734, 158.87395895601003, -0.56674201169828), (1.0, 1.0, 1.0), "Deep_BoneHoard_E38", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5806.4956, 7162.4404, 1265.7432), (0.45334687734538964, 115.92691138909618, 0.39674329226530447), (1.0, 1.0, 1.0), "Deep_BoneHoard_E39", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (7592.7783, 7256.2, 1266.4268), (-3.578185686685689, -41.100858924411106, 1.5675777171012237), (1.0, 1.149932, 1.0), "Deep_BoneHoard_E4", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (6280.0195, 7491.7744, 1270.5117), (0.421463700601793, 120.32319002681815, 0.4303121066622902), (1.0, 1.0, 1.0), "Deep_BoneHoard_E40", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5449.5645, 6883.402, 1269.3745), (-0.40469358286000834, -57.492733571300526, -0.4460754367092318), (1.0, 1.0, 1.0), "Deep_BoneHoard_E41", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (8198.242, 8103.9976, 1263.5437), (-0.46603386729523594, 16.533902581916045, -0.5663145942458411), (1.0, 1.0, 1.4978406), "Deep_BoneHoard_E42", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (6715.907, 7643.3984, 1279.1377), (4.352223551444538, 53.6883726494084, -0.21667471026546137), (1.0, 1.0, 1.0), "Deep_BoneHoard_E43", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (7041.824, 7054.8022, 1268.3877), (4.35222339397182, 53.688611536483926, 1.0195007427765057), (1.0, 1.0, 1.0), "Deep_BoneHoard_E44", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5293.5493, 6559.143, 1258.7886), (0.355489943357995, 78.8334264986404, 1.641551782206919), (1.0, 1.0, 1.0), "Deep_BoneHoard_E45", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (6071.9, 6433.6665, 1258.6411), (0.13713672945145178, 90.93819698116995, 0.07320611944495219), (1.0, 1.0, 1.0), "Deep_BoneHoard_E46", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (6558.05, 6387.3467, 1254.0903), (-0.8110350557699986, 119.92579811372602, 1.470963192324033), (1.0, 1.0, 1.0), "Deep_BoneHoard_E47", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4519.716, 8881.2, 1261.8179), (2.0834474723746723, 40.27441018745761, 1.8141714218361558), (1.0, 1.0, 1.0), "Deep_BoneHoard_E48", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (8928.695, 7641.164, 1346.912), (0.5162189143930038, 158.68219671452826, 0.06011386237238237), (1.0, 1.0, 1.9345188), "Deep_BoneHoard_E49", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (9417.802, 6850.4277, 1349.6582), (0.5162189923458974, 119.52715371864107, 0.06011417151338499), (1.0, 1.0, 3.4332929), "Deep_BoneHoard_E50", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (8803.674, 7193.2354, 1344.1294), (-0.5171202716939349, -33.47750887591258, 0.04985056116361394), (1.0, 1.0, 1.0), "Deep_BoneHoard_E51", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (8545.465, 6867.3623, 1345.1611), (0.14633676690679578, -33.47698839792201, 0.04985116147465076), (1.0, 1.0, 1.0), "Deep_BoneHoard_E52", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (8273.742, 6553.262, 1346.6418), (0.15451253437709916, -50.9074667242557, 0.0036528533746641436), (1.0, 1.0, 2.2330828), "Deep_BoneHoard_E53", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (9039.525, 6363.5967, 1347.3353), (-0.18936155759633386, 176.95654701470224, -0.21499631870204422), (1.0, 1.0, 1.9103973), "Deep_BoneHoard_E54_124", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4335.7285, 10231.39, 1343.2358), (0.767351200178216, 141.07286663549658, 0.23045027232272963), (1.0, 1.0, 1.4867663), "Deep_BoneHoard_E55", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (7023.5947, 10674.777, 1260.5234), (2.4793831464007883, 118.81337043219126, 0.9043895273795239), (1.0, 1.0, 0.684852), "Deep_BoneHoard_E56", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (9152.645, 6744.394, 1348.6401), (-0.24801637240335797, 158.39989943957053, -0.143554675377999), (1.0, 1.0, 1.0), "Deep_BoneHoard_E57", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (8938.853, 7032.9565, 1342.7217), (1.8269933396999192, -151.56371178542875, -0.23928831694062594), (1.0, 1.0, 1.0), "Deep_BoneHoard_E58", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (7199.85, 6047.0767, 1342.9121), (0.15451301930103173, 150.94098355961648, 0.003653209893679065), (1.0, 1.0, 4.128629), "Deep_BoneHoard_E59", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (8215.427, 9805.453, 1259.7583), (0.4212518766531434, -77.13132057944767, 0.6281947103395386), (1.0, 1.0, 1.0), "Deep_BoneHoard_E6_178", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3199.1794, 8039.5244, 1346.4586), (0.5690571246764227, 40.52715707508306, 0.4580310487054959), (1.0, 1.0, 3.0623305), "Deep_BoneHoard_E60", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4351.1797, 7333.5244, 1283.4586), (0.5690571168336255, 23.652098010072834, 0.45803112940789414), (1.0, 1.0, 4.03125), "Deep_BoneHoard_E61", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3997.4697, 7948.922, 1345.3359), (0.5690572104965826, 112.69067532706342, 0.45803114976796866), (1.0, 1.0, 1.0), "Deep_BoneHoard_E62", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2390.815, 8960.949, 1162.9716), (5.618189252081172, -0.2768860001625703, -2.8260801255576267), (0.5, 0.5, 1.0), "Deep_BoneHoard_E63", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1751.815, 8308.949, 1032.9716), (-18.564511001070553, 163.00046289126402, -7.12292389619451), (0.5, 0.375, 2.0), "Deep_BoneHoard_E67", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2695.0986, 8887.172, 1367.1189), (2.8124942971054225, -174.37500573490817, 1.5962899518693097e-07), (0.5, 0.5, 1.90625), "Deep_BoneHoard_E69_21", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (7688.5767, 8607.207, 1274.2959), (0.4212520236907528, -77.12918168595239, 2.2973545286769443), (1.0, 1.0, 1.0), "Deep_BoneHoard_E7_180", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2719.255, 8327.145, 1408.2723), (-2.8086545548517594, 8.442735985919589, 16.739020970013446), (0.5, 0.375, 1.0), "Deep_BoneHoard_E70", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2734.3218, 8313.785, 1419.8258), (8.311854669317635, -109.5417840846435, -11.192079155901798), (0.5, 0.375, 1.0), "Deep_BoneHoard_E71", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (8595.819, 7827.6963, 1256.9004), (0.4212519159637121, -77.12918169141551, 2.2973547612696996), (1.0, 1.0, 1.0), "Deep_BoneHoard_E8_182", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (8625.065, 8103.9976, 1263.5436), (-0.4662475195600121, 154.27541977451574, -0.5663146506614531), (1.0, 1.0, 1.0), "Deep_BoneHoard_E9", _folder)
if a: placed += 1
else: skipped += 1

# Batch 8: StaticMesh'Deep_BoneHoard_F' (5 instances)
_mesh_path = "/Game/Art/Assets/Kits/Architecture/Deep/Deep_BoneHoard_F"
_materials = ['/Game/Art/Assets/Kits/Misc/Dirt_Mounds/Materials/BoneHoard_Bone_Mount_Inst1']
_folder = "Reconstruction/BD_BB_Chapter5_BoneHoard/Meshes"
a = spawn_static_mesh(_mesh_path, _materials, (5687.576, 9850.759, 1263.2837), (-0.4614868116652688, 141.06527104487338, 0.03519422764521461), (1.0, 1.0, 1.0), "Deep_BoneHoard_F_109", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4514.755, 9322.037, 1245.083), (-3.429199059112824, -55.95749000908522, 0.47653680766348516), (1.0, 1.0, 1.0), "Deep_BoneHoard_F2", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (7252.327, 6963.249, 1298.535), (1.5765715929531234, 0.27472702726117615, -1.6907654381601658), (1.0, 1.0, 1.9889828), "Deep_BoneHoard_F3_172", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4118.0137, 7480.4126, 1268.523), (-0.5878295692191965, 35.817178179576764, 0.697659366446789), (1.0, 1.0, 2.1489637), "Deep_BoneHoard_F5", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (7627.8066, 10065.379, 1260.2495), (0.15307818635825846, 42.938719433649645, 0.2895812470576034), (1.0, 1.0, 0.8000107), "Deep_BoneHoard_F6", _folder)
if a: placed += 1
else: skipped += 1

# Batch 9: StaticMesh'Deep_Column_Shaft_3m_A_B' (1 instances)
_mesh_path = "/Game/Art/Assets/Kits/Architecture/Deep/Deep_Column_Shaft_3m_A_B"
_materials = ['/Game/Art/Assets/Kits/Architecture/Deep/Materials/Deep_Column/MI_Deep_Column_B']
_folder = "Reconstruction/BD_BB_Chapter5_BoneHoard/Meshes"
a = spawn_static_mesh(_mesh_path, _materials, (8099.5503, 8310.498, 1212.0448), (40.65777610441864, -98.92731854211048, -45.39219865335252), (1.0, 1.0, 1.0), "Deep_Column_Shaft_3m_A_B_136", _folder)
if a: placed += 1
else: skipped += 1

# Batch 10: StaticMesh'Deep_Column_Shaft_3m_B_B' (1 instances)
_mesh_path = "/Game/Art/Assets/Kits/Architecture/Deep/Deep_Column_Shaft_3m_B_B"
_materials = ['/Game/Art/Assets/Kits/Architecture/Deep/Materials/Deep_Column/MI_Deep_Column_B']
_folder = "Reconstruction/BD_BB_Chapter5_BoneHoard/Meshes"
a = spawn_static_mesh(_mesh_path, _materials, (5659.3086, 9477.503, 1669.1343), (46.03361902800874, 12.306394861741042, -77.23977783307238), (1.0, 1.0, 1.0), "Deep_Column_Shaft_3m_B_B2_244", _folder)
if a: placed += 1
else: skipped += 1

# Batch 11: StaticMesh'Deep_Column_Tapered_A' (9 instances)
_mesh_path = "/Game/Art/Assets/Kits/Architecture/Deep/Deep_Column_Tapered_A"
_materials = ['/Game/Art/Assets/Kits/Architecture/Deep/Materials/Deep_Column/MI_Deep_Column_A_BoneHoard_Outer', '/Game/Art/Assets/Kits/Architecture/Deep/Materials/Deep_Column/MI_Deep_Column_C_BoneHoard_Outer']
_folder = "Reconstruction/BD_BB_Chapter5_BoneHoard/Meshes"
a = spawn_static_mesh(_mesh_path, _materials, (7169.539, 11960.699, 1340.0), (0.0, 170.00009497009785, -0.0), (1.0, 1.0, 1.0), "Deep_Column_Tapered_A_2", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4591.968, 11525.18, 1340.0), (0.0, -147.18728406628017, 0.0), (1.0, 1.0, 1.0), "Deep_Column_Tapered_A2", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2993.395, 9255.178, 1340.0), (0.0, -99.37469763982008, 0.0), (1.0, 1.0, 1.0), "Deep_Column_Tapered_A3", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3503.0972, 6561.6616, 1340.0), (0.0, -54.374665354645416, 0.0), (1.0, 1.0, 1.0), "Deep_Column_Tapered_A4", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5789.7607, 5063.095, 1340.0), (0.0, -9.374755650852324, 0.0), (1.0, 1.0, 1.0), "Deep_Column_Tapered_A5", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (8409.443, 5615.2896, 1340.0), (0.0, 35.62530550463571, -0.0), (1.0, 1.0, 1.0), "Deep_Column_Tapered_A6", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (9310.129, 10477.248, 1340.0), (0.0, 122.18748329253543, -0.0), (1.0, 1.0, 1.0), "Deep_Column_Tapered_A7", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (9874.977, 7874.308, 1340.0), (0.0, 77.18740574299976, -0.0), (1.0, 1.0, 1.0), "Deep_Column_Tapered_A8", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (10087.117, 7940.549, 1339.8411), (0.0, 172.81237845055045, -0.0), (1.0, 1.0, 1.0), "Deep_Column_Tapered_A9", _folder)
if a: placed += 1
else: skipped += 1

# Batch 12: StaticMesh'Deep_Column_Tapered_B' (9 instances)
_mesh_path = "/Game/Art/Assets/Kits/Architecture/Deep/Deep_Column_Tapered_B"
_materials = ['/Game/Art/Assets/Kits/Architecture/Deep/Materials/Deep_Column/MI_Deep_Column_A_BoneHoard_Outer', '/Game/Art/Assets/Kits/Architecture/Deep/Materials/Deep_Column/MI_Deep_Column_C_BoneHoard_Outer']
_folder = "Reconstruction/BD_BB_Chapter5_BoneHoard/Meshes"
a = spawn_static_mesh(_mesh_path, _materials, (8373.792, 11447.36, 1335.0), (0.0, 144.99998898772822, -0.0), (1.0, 1.0, 1.0), "Deep_Column_Tapered_B_5", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5854.536, 11989.333, 1335.0), (0.0, -175.00001978379615, 0.0), (1.0, 1.0, 1.0), "Deep_Column_Tapered_B2", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3557.9246, 10555.799, 1330.0), (0.0, -124.37497509292474, 0.0), (1.0, 1.0, 1.0), "Deep_Column_Tapered_B3", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2965.0632, 7824.5273, 1335.0), (0.0, -79.37490349586139, 0.0), (1.0, 1.0, 1.0), "Deep_Column_Tapered_B4", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4495.0625, 5564.4463, 1335.0), (0.0, -34.37481528645169, 0.0), (1.0, 1.0, 1.0), "Deep_Column_Tapered_B5", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (7158.9014, 5087.7007, 1335.0), (0.0, 16.250549999487706, -0.0), (1.0, 1.0, 1.0), "Deep_Column_Tapered_B6", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (9373.606, 6600.7593, 1337.0), (0.0, 55.62548579991942, -0.0), (1.0, 1.0, 1.0), "Deep_Column_Tapered_B7", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (10050.305, 9140.077, 1337.8589), (0.0, 10.625580148249611, -0.0), (1.0, 1.0, 1.0), "Deep_Column_Tapered_B8", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (9855.052, 9214.435, 1337.0), (0.0, 100.62555572185636, -0.0), (1.0, 1.0, 1.0), "Deep_Column_Tapered_B9", _folder)
if a: placed += 1
else: skipped += 1

# Batch 13: StaticMesh'Deep_Column_Top_3m_A_A' (13 instances)
_mesh_path = "/Game/Art/Assets/Kits/Architecture/Deep/Deep_Column_Top_3m_A_A"
_materials = ['/Game/Art/Assets/Kits/Architecture/Deep/Materials/Deep_Column/MI_Deep_Column_C']
_folder = "Reconstruction/BD_BB_Chapter5_BoneHoard/Meshes"
a = spawn_static_mesh(_mesh_path, _materials, (7754.234, 7982.3335, 1413.4761), (48.67553776172126, -86.13836408670736, -51.09017623114946), (1.0, 1.0, 1.0), "Deep_Column_Top_3m_A_A_151", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (7095.9624, 10971.187, 2853.0), (0.0, 164.000004493943, -0.0), (1.0, 1.0, 1.0), "Deep_Column_Top_3m_A_A10_28", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (8816.347, 9189.55, 2854.0), (0.0, 105.99999900725344, -0.0), (1.0, 1.0, 1.0), "Deep_Column_Top_3m_A_A11_31", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (8222.281, 6782.211, 2856.0), (0.0, 44.99999866815529, -0.0), (1.0, 1.0, 1.0), "Deep_Column_Top_3m_A_A12_34", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3978.3596, 7884.4814, 2854.0), (0.0, -74.99998993184444, 0.0), (1.0, 1.0, 1.0), "Deep_Column_Top_3m_A_A13_37", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4645.961, 6742.789, 2856.0), (0.0, -44.99999866815529, 0.0), (1.0, 1.0, 1.0), "Deep_Column_Top_3m_A_A14_40", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4679.596, 10322.274, 2857.0), (0.0, -135.00000119449854, 0.0), (1.0, 1.0, 1.0), "Deep_Column_Top_3m_A_A15_43", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4027.8115, 9194.69, 2853.0), (0.0, -104.99999433376263, 0.0), (1.0, 1.0, 1.0), "Deep_Column_Top_3m_A_A16_46", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5798.814, 6125.7085, 2851.0), (0.0, -16.999999276983736, 0.0), (1.0, 1.0, 1.0), "Deep_Column_Top_3m_A_A19_55", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (7102.9067, 6134.4434, 2852.0), (0.0, 13.999999443458856, -0.0), (1.0, 1.0, 1.0), "Deep_Column_Top_3m_A_A21_61", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (8866.262, 7904.139, 2853.0), (0.0, 72.00000634712251, -0.0), (1.0, 1.0, 1.0), "Deep_Column_Top_3m_A_A23_69", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (8182.3213, 10288.481, 2852.0), (0.0, 135.9999872904529, -0.0), (1.0, 1.0, 1.0), "Deep_Column_Top_3m_A_A26_82", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5811.071, 10921.571, 2852.0), (0.0, -164.99999752096636, 0.0), (1.0, 1.0, 1.0), "Deep_Column_Top_3m_A_A28_88", _folder)
if a: placed += 1
else: skipped += 1

# Batch 14: StaticMesh'Deep_Stairs' (2 instances)
_mesh_path = "/Game/Art/Assets/Kits/Architecture/Deep/Deep_Stairs"
_materials = ['/Game/Art/Assets/Kits/Architecture/Deep/Materials/Deep_TrimSheet/MI_Deep_TrimSheet', '/Game/Art/Assets/Kits/Architecture/Deep/Materials/MI_Deep_Non_Destructible_Dark']
_folder = "Reconstruction/BD_BB_Chapter5_BoneHoard/Meshes"
a = spawn_static_mesh(_mesh_path, _materials, (6441.5337, 10070.309, 1262.8501), (0.0, 90.0000030488508, -0.0), (1.0, 1.0, 1.0), "Deep_Stairs_21", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (7945.0215, 8516.903, 1261.0474), (0.0, 3.051757709276941e-05, -0.0), (1.0, 1.0, 1.0), "Deep_Stairs4", _folder)
if a: placed += 1
else: skipped += 1

# Batch 15: StaticMesh'Deep_Stairs' (2 instances)
_mesh_path = "/Game/Art/Assets/Kits/Architecture/Deep/Deep_Stairs"
_materials = ['/Game/Art/Assets/Kits/Architecture/Deep/Materials/Deep_TrimSheet/MI_Deep_TrimSheet', '/Game/Art/Assets/Kits/Architecture/Suburbs/Destructable/Materials/MI_Suburbs_Wall_Non_Dest']
_folder = "Reconstruction/BD_BB_Chapter5_BoneHoard/Meshes"
a = spawn_static_mesh(_mesh_path, _materials, (4866.872, 8520.141, 1262.8643), (0.0, -179.99998633961752, -0.0), (1.0, 1.0, 1.0), "Deep_Stairs2", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (6498.689, 6982.7705, 1261.0483), (0.0, -89.99997063746636, 0.0), (1.0, 1.0, 1.0), "Deep_Stairs3", _folder)
if a: placed += 1
else: skipped += 1

# Batch 16: StaticMesh'Deep_Wall_A' (14 instances)
_mesh_path = "/Game/Art/Assets/Kits/Architecture/Deep/Deep_Wall_A"
_materials = ['/Game/Art/Assets/Kits/Architecture/Deep/Materials/Deep_Assets_A/MI_Deep_Assets_A_BoneHoard', '/Game/Art/Assets/Kits/Architecture/Deep/Materials/Deep_JigsawStoneWallTileable/MI_Deep_JigsawStoneWallTileable_BoneHoard', '/Game/Unshippable/ThirdParty/FantasyDungeon/Materials/BaseMaterials/black', '/Game/Art/Assets/Kits/Architecture/Deep/Materials/Deep_TrimSheet/MI_Deep_TrimSheet_BoneHoard']
_folder = "Reconstruction/BD_BB_Chapter5_BoneHoard/Meshes"
a = spawn_static_mesh(_mesh_path, _materials, (9754.158, 7165.581, 1341.1719), (0.0, 67.20247053033125, -0.0), (1.0, 1.0, 1.0), "BalrogsNestWall17_6", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (7818.0376, 5200.2666, 1341.1719), (0.0, 22.821472770645233, -0.0), (1.0, 1.0, 1.0), "BalrogsNestWall18", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (6463.4395, 4917.69, 1341.1719), (0.0, 1.1964874130225105, -0.0), (1.0, 1.0, 1.0), "BalrogsNestWall19", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5057.4106, 5173.494, 1341.1719), (0.0, -23.471220934073823, 0.0), (1.0, 1.0, 1.0), "BalrogsNestWall20", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3868.5156, 5973.459, 1341.1719), (0.0, -45.71667730979276, 0.0), (1.0, 1.0, 1.0), "BalrogsNestWall21", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3092.3936, 7136.0884, 1341.1719), (0.0, -65.4461026051125, 0.0), (1.0, 1.0, 1.0), "BalrogsNestWall22", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (9745.179, 9919.1455, 1341.1719), (0.0, 112.61284204905317, -0.0), (1.0, 1.0, 1.0), "BalrogsNestWall23", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (8960.002, 11073.807, 1341.1719), (0.0, 134.5606024872773, -0.0), (1.0, 1.0, 1.0), "BalrogsNestWall24", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (7808.972, 11845.285, 1341.1719), (0.0, 157.92370160285006, -0.0), (1.0, 1.0, 1.0), "BalrogsNestWall25", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (6489.1333, 12119.318, 1341.1719), (0.0, 179.56889798941498, -0.0), (1.0, 1.0, 1.0), "BalrogsNestWall26", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5155.0503, 11898.721, 1341.1719), (0.0, -158.4105101764962, 0.0), (1.0, 1.0, 1.0), "BalrogsNestWall27", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3982.7031, 11164.662, 1341.1719), (0.0, -136.73091248006247, 0.0), (1.0, 1.0, 1.0), "BalrogsNestWall28", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3127.9062, 10005.681, 1341.1719), (0.0, -113.68453046203538, 0.0), (1.0, 1.0, 1.0), "BalrogsNestWall29", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (8990.002, 6013.124, 1341.1719), (0.0, 45.29007422517252, -0.0), (1.0, 1.0, 1.0), "BalrogsNestWall9", _folder)
if a: placed += 1
else: skipped += 1

# Batch 17: StaticMesh'Deep_Wall_B' (2 instances)
_mesh_path = "/Game/Art/Assets/Kits/Architecture/Deep/Deep_Wall_B"
_materials = ['/Game/Art/Assets/Kits/Architecture/Deep/Materials/Deep_Assets_A/MI_Deep_Assets_A_BoneHoard', '/Game/Art/Assets/Kits/Architecture/Deep/Materials/Deep_JigsawStoneWallTileable/MI_Deep_JigsawStoneWallTileable_BoneHoard', '/Game/Unshippable/ThirdParty/FantasyDungeon/Materials/BaseMaterials/black', '/Game/Art/Assets/Kits/Architecture/Deep/Materials/Deep_TrimSheet/MI_Deep_TrimSheet_BoneHoard']
_folder = "Reconstruction/BD_BB_Chapter5_BoneHoard/Meshes"
a = spawn_static_mesh(_mesh_path, _materials, (10175.532, 8553.575, 1891.1719), (0.0, 90.0000030488508, -0.0), (1.0, 1.0, 1.0), "Deep_Wall_B_2", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2843.2676, 8552.685, 1341.1719), (0.0, -89.99997063746636, 0.0), (1.0, 1.0, 1.0), "Deep_Wall_B2_5", _folder)
if a: placed += 1
else: skipped += 1

# Batch 18: StaticMesh'Deep_WallTrim' (16 instances)
_mesh_path = "/Game/Art/Assets/Kits/Architecture/Deep/Deep_WallTrim"
_materials = ['/Game/Art/Assets/Kits/Architecture/Deep/Materials/Deep_TrimSheet/MI_Deep_TrimSheet_BoneHoard']
_folder = "Reconstruction/BD_BB_Chapter5_BoneHoard/Meshes"
a = spawn_static_mesh(_mesh_path, _materials, (8953.586, 11030.535, 3254.575), (0.0, 134.5871028478161, -0.0), (1.0, 1.0, 1.0), "Deep_WallTrim10", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (7826.9233, 11800.016, 3251.1714), (0.0, 157.85411056939586, -0.0), (1.0, 1.0, 1.0), "Deep_WallTrim11", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (6522.5283, 12092.066, 3251.1714), (0.0, 179.49811608169276, -0.0), (1.0, 1.0, 1.0), "Deep_WallTrim12", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5201.8955, 11880.143, 3251.1714), (0.0, -158.32987055572332, 0.0), (1.0, 1.0, 1.0), "Deep_WallTrim13", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3990.7441, 11104.888, 3251.1714), (0.0, -136.66011661896897, 0.0), (1.0, 1.0, 1.0), "Deep_WallTrim14", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3170.5957, 9987.225, 3251.1714), (0.0, -112.79863781408963, 0.0), (1.0, 1.0, 1.0), "Deep_WallTrim15", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (9954.99, 8593.234, 3251.1714), (0.0, 90.49415586896892, -0.0), (1.0, 1.0, 1.0), "Deep_WallTrim16", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2888.667, 8557.73, 3251.1714), (0.0, -89.72860329686459, 0.0), (1.0, 1.0, 1.0), "Deep_WallTrim17", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (8941.883, 6020.134, 3251.1714), (0.0, 45.74945769926597, -0.0), (1.0, 1.0, 1.0), "Deep_WallTrim2", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (9703.065, 7142.009, 3251.1714), (0.0, 67.21708483748397, -0.0), (1.0, 1.0, 1.0), "Deep_WallTrim3_7", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (7777.569, 5231.6343, 3251.1714), (0.0, 22.845695264702417, -0.0), (1.0, 1.0, 1.0), "Deep_WallTrim4", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (6459.2153, 4966.525, 3251.1714), (0.0, 1.182426464672209, -0.0), (1.0, 1.0, 1.0), "Deep_WallTrim5", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5101.198, 5210.047, 3251.1714), (0.0, -23.49389443670893, 0.0), (1.0, 1.0, 1.0), "Deep_WallTrim6", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3883.3975, 6033.7393, 3251.1714), (0.0, -45.2799969772123, 0.0), (1.0, 1.0, 1.0), "Deep_WallTrim7", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3128.6367, 7171.0605, 3251.1714), (0.0, -65.25759762008803, 0.0), (1.0, 1.0, 1.0), "Deep_WallTrim8", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (9722.777, 9874.736, 3251.1714), (0.0, 112.6979533790507, -0.0), (1.0, 1.0, 1.0), "Deep_WallTrim9", _folder)
if a: placed += 1
else: skipped += 1

# Batch 19: StaticMesh'Suburbs_Foor_2x3m_A' (2 instances)
_mesh_path = "/Game/Art/Assets/Kits/Architecture/Suburbs/Suburbs_Foor_2x3m_A"
_materials = ['/Game/Art/Assets/Kits/Architecture/Suburbs/Materials/Suburbs_Floor_A/Suburbs_Floor_A_1_Inst_Dest', '/Game/Art/Assets/Kits/Architecture/Suburbs/Materials/Suburbs_Floor_A/MI_Suburbs_Floor_A_2_Inst']
_folder = "Reconstruction/BD_BB_Chapter5_BoneHoard/Meshes"
a = spawn_static_mesh(_mesh_path, _materials, (99.99994, 9760.0, 799.0), (0.0, 90.00005166594045, -0.0), (1.0, 1.0, 1.0), "Suburbs_Foor_2x3m_A_31", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (100.000244, 9460.0, 799.0), (0.0, 90.00005166594045, -0.0), (1.0, 1.0, 1.0), "Suburbs_Foor_2x3m_A2", _folder)
if a: placed += 1
else: skipped += 1

# Batch 20: StaticMesh'Suburbs_Stairs_Medium_C_NonDest' (3 instances)
_mesh_path = "/Game/Art/Assets/Kits/Architecture/Suburbs/Suburbs_Stairs_Medium_C_NonDest"
_materials = ['/Game/Art/Assets/Kits/Architecture/Suburbs/Materials/Stairs_Medium_C_NonDest/MI_Stairs_Medium_C_NonDes', '/Game/Art/Assets/Kits/Architecture/Suburbs/Destructable/Materials/MI_Suburbs_Wall_Non_Dest']
_folder = "Reconstruction/BD_BB_Chapter5_BoneHoard/Meshes"
a = spawn_static_mesh(_mesh_path, _materials, (10045.07, 8578.807, 1145.7422), (0.0, -89.99997063746636, 0.0), (1.0, 1.0, 1.0), "Suburbs_Stairs_Medium_C_NonDest_19", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (10478.712, 8609.537, 902.86426), (0.0, -61.07663275640571, 0.0), (1.0, 1.0, 1.0), "Suburbs_Stairs_Medium_C_NonDest2", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (10739.119, 8754.219, 709.2676), (0.0, -59.92327561792876, 0.0), (1.0, 1.0, 1.0), "Suburbs_Stairs_Medium_C_NonDest3", _folder)
if a: placed += 1
else: skipped += 1

# Batch 21: StaticMesh'Suburbs_Stairs_Medium_C_NonDest' (3 instances)
_mesh_path = "/Game/Art/Assets/Kits/Architecture/Suburbs/Suburbs_Stairs_Medium_C_NonDest"
_materials = ['/Game/Art/Assets/Kits/Architecture/Suburbs/Materials/Stairs_Medium_C_NonDest/MI_Stairs_Medium_C_NonDes_Suburbs', '/Game/Art/Assets/Kits/Architecture/Suburbs/Destructable/Materials/MI_Suburbs_Wall_Non_Dest']
_folder = "Reconstruction/BD_BB_Chapter5_BoneHoard/Meshes"
a = spawn_static_mesh(_mesh_path, _materials, (2769.808, 8577.562, 1135.7368), (0.0, 88.29630846768478, -0.0), (1.0, 1.0, 1.0), "Suburbs_Stairs_Medium_C_NonDest4", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2339.5742, 8610.678, 939.0908), (0.0, 67.6691509406137, -0.0), (1.0, 1.0, 1.0), "Suburbs_Stairs_Medium_C_NonDest5", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2070.7637, 8721.082, 740.438), (0.0, 67.6691509406137, -0.0), (1.0, 1.0, 1.0), "Suburbs_Stairs_Medium_C_NonDest6_247", _folder)
if a: placed += 1
else: skipped += 1

# Batch 22: StaticMesh'Suburbs_Stairs_Small_C_CornerExt_NonDest' (4 instances)
_mesh_path = "/Game/Art/Assets/Kits/Architecture/Suburbs/Suburbs_Stairs_Small_C_CornerExt_NonDest"
_materials = ['/Game/Art/Assets/Kits/Architecture/Suburbs/Destructable/Materials/MI_Suburbs_Wall_Non_Dest', '/Game/Art/Assets/Kits/Architecture/Suburbs/Materials/Stairs_Medium_C_NonDest/MI_Stairs_Medium_C_NonDes']
_folder = "Reconstruction/BD_BB_Chapter5_BoneHoard/Meshes"
a = spawn_static_mesh(_mesh_path, _materials, (8861.369, 8376.369, 1245.6304), (0.0, 90.73108421355057, -0.0), (1.0, 1.0, 1.0), "Suburbs_Stairs_Small_C_CornerExt_NonDest_43", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (8857.557, 8674.482, 1245.6304), (0.0, 0.7312850651275503, -0.0), (1.0, 1.0, 1.0), "Suburbs_Stairs_Small_C_CornerExt_NonDest2", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3978.372, 8659.346, 1244.8242), (0.0, -91.03576921575555, 0.0), (1.0, 1.0, 1.0), "Suburbs_Stairs_Small_C_CornerExt_NonDest3", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3972.4902, 8360.838, 1245.1353), (0.0, 179.14160126878306, -0.0), (1.0, 1.0, 1.0), "Suburbs_Stairs_Small_C_CornerExt_NonDest4", _folder)
if a: placed += 1
else: skipped += 1

# Batch 23: StaticMesh'Suburbs_Stairs_Small_C_NonDest' (2 instances)
_mesh_path = "/Game/Art/Assets/Kits/Architecture/Suburbs/Suburbs_Stairs_Small_C_NonDest"
_materials = ['/Game/Art/Assets/Kits/Architecture/Suburbs/Destructable/Materials/MI_Suburbs_Wall_Non_Dest', '/Game/Art/Assets/Kits/Architecture/Suburbs/Materials/Stairs_Medium_C_NonDest/MI_Stairs_Medium_C_NonDes']
_folder = "Reconstruction/BD_BB_Chapter5_BoneHoard/Meshes"
a = spawn_static_mesh(_mesh_path, _materials, (8860.208, 8524.973, 1245.6299), (0.0, 90.73137136230834, -0.0), (1.0, 1.0, 1.0), "Suburbs_Stairs_Small_C_NonDest_49", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3975.5225, 8510.838, 1245.1353), (0.0, -91.03368409515046, 0.0), (1.0, 1.0, 1.0), "Suburbs_Stairs_Small_C_NonDest2", _folder)
if a: placed += 1
else: skipped += 1

# Batch 24: StaticMesh'SM_Bone_Hoard_Pile_Skeletal_A' (4 instances)
_mesh_path = "/Game/Art/Assets/Kits/Deco/Remains/SM_Bone_Hoard_Pile_Skeletal_A"
_materials = ['/Game/Art/Assets/Kits/Misc/Dirt_Mounds/Materials/BoneHoard_Bone_Mount_Inst1']
_folder = "Reconstruction/BD_BB_Chapter5_BoneHoard/Meshes"
a = spawn_static_mesh(_mesh_path, _materials, (1659.0, 9622.0, 953.0), (0.0, 164.9647876849271, -0.0), (1.28125, 1.28125, 1.28125), "SM_Bone_Hoard_Pile_Skeletal_A_29", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2029.0, 8439.0, 1072.0), (0.0, -44.999970287262066, 0.0), (1.0, 1.0, 1.0), "SM_Bone_Hoard_Pile_Skeletal_A2_5", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1804.0, 8216.0, 1116.0), (-1.8883056294269138, -39.340692928130025, -2.0846861821221414), (1.0, 1.0, 1.0), "SM_Bone_Hoard_Pile_Skeletal_A3_17", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1872.0, 8250.0, 1128.0), (-2.6521604455358, -123.32989270599107, -8.33001680847118), (1.0, 1.0, 1.0), "SM_Bone_Hoard_Pile_Skeletal_A4", _folder)
if a: placed += 1
else: skipped += 1

# Batch 25: StaticMesh'SM_Bone_Hoard_Pile_Skeletal_B' (1 instances)
_mesh_path = "/Game/Art/Assets/Kits/Deco/Remains/SM_Bone_Hoard_Pile_Skeletal_B"
_materials = ['/Game/Art/Assets/Kits/Misc/Dirt_Mounds/Materials/BoneHoard_Bone_Mount_Inst1']
_folder = "Reconstruction/BD_BB_Chapter5_BoneHoard/Meshes"
a = spawn_static_mesh(_mesh_path, _materials, (1878.0, 9555.0, 998.0), (0.0, -22.50003057388069, 0.0), (1.375, 1.375, 1.375), "SM_Bone_Hoard_Pile_Skeletal_B_2", _folder)
if a: placed += 1
else: skipped += 1

# Batch 26: StaticMesh'SM_Bone_Hoard_Pile_Skeletal_E' (4 instances)
_mesh_path = "/Game/Art/Assets/Kits/Deco/Remains/SM_Bone_Hoard_Pile_Skeletal_E"
_materials = ['/Game/Art/Assets/Kits/Misc/Dirt_Mounds/Materials/BoneHoard_Bone_Mount_Inst1']
_folder = "Reconstruction/BD_BB_Chapter5_BoneHoard/Meshes"
a = spawn_static_mesh(_mesh_path, _materials, (1877.0, 8294.0, 1130.0), (-9.68252585812927, 163.7932080918864, -2.989349193037507), (1.0, 1.0, 2.0), "SM_Bone_Hoard_Pile_Skeletal_E_14", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2675.0, 8896.0, 1359.0), (-1.075927461535827, 157.5242818547548, -2.5987237018718448), (1.34375, 1.34375, 2.625), "SM_Bone_Hoard_Pile_Skeletal_E2_34", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2855.0, 8840.0, 1351.0), (3.6063195095615166, 81.53826919525127, -5.153168242173692), (1.65625, 2.0, 3.0), "SM_Bone_Hoard_Pile_Skeletal_E3", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2687.0, 8345.0, 1393.0), (3.606318993244462, -120.9617327475328, -5.15316752347165), (1.5, 1.625, 2.53125), "SM_Bone_Hoard_Pile_Skeletal_E4", _folder)
if a: placed += 1
else: skipped += 1

# Batch 27: StaticMesh'SM_Bone_Hoard_Pile_Skeletal_F' (5 instances)
_mesh_path = "/Game/Art/Assets/Kits/Deco/Remains/SM_Bone_Hoard_Pile_Skeletal_F"
_materials = ['/Game/Art/Assets/Kits/Misc/Dirt_Mounds/Materials/BoneHoard_Bone_Mount_Inst1']
_folder = "Reconstruction/BD_BB_Chapter5_BoneHoard/Meshes"
a = spawn_static_mesh(_mesh_path, _materials, (2432.902, 8743.951, 1152.994), (5.6249948482973045, 6.127280497871116e-07, -2.812499789671241), (1.0, 1.0, 1.0), "SM_Bone_Hoard_Pile_Skeletal_F_2", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2409.655, 8505.101, 1149.3617), (-0.2589111315351475, -92.52007903350322, 0.13660275133762742), (1.0, 1.0, 1.0), "SM_Bone_Hoard_Pile_Skeletal_F2", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2273.5364, 8877.137, 1150.2369), (3.165642649535156, 8.570767009540562, -1.9468690867393064), (1.0, 1.0, 1.0), "SM_Bone_Hoard_Pile_Skeletal_F3", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2181.2244, 9055.318, 1105.8318), (0.571399921815135, 64.7092348036385, -1.265777352010515), (1.0, 1.0, 1.0), "SM_Bone_Hoard_Pile_Skeletal_F4", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2515.1567, 8946.975, 1266.6552), (-4.543303661766956, 90.52305680109433, -6.543394295762846), (1.0, 1.0, 1.0), "SM_Bone_Hoard_Pile_Skeletal_F5", _folder)
if a: placed += 1
else: skipped += 1

# Batch 28: StaticMesh'Rubble_Masonry_Mound_Pile_D' (1 instances)
_mesh_path = "/Game/Art/Assets/Kits/Deco/Rubble/Rubble_Masonry_Mound_Pile_D"
_materials = ['/Game/Art/Assets/Kits/Deco/Rubble/Materials/Rubble_Masonry_Pile/MI_Rubble_Masonry_Pile_Atlas_Inst_B']
_folder = "Reconstruction/BD_BB_Chapter5_BoneHoard/Meshes"
a = spawn_static_mesh(_mesh_path, _materials, (6303.39, 6644.5366, 1254.3809), (2.916203905517163, 90.15034659162698, 2.952138241783975), (1.0, 1.0, 1.0), "Rubble_Masonry_Mound_Pile_D", _folder)
if a: placed += 1
else: skipped += 1

# Batch 29: StaticMesh'Remains_Bones_Assemblage_A' (13 instances)
_mesh_path = "/Game/Art/Assets/Kits/Deco/Warrens_Tomb/Remains_Bones_Assemblage_A"
_materials = ['/Game/Art/Assets/Kits/Deco/Orc/Shanty/Material/Orc_Shanty_Midden/MI_Orc_Shanty_Midden_Mat_Inst2']
_folder = "Reconstruction/BD_BB_Chapter5_BoneHoard/Meshes"
a = spawn_static_mesh(_mesh_path, _materials, (2642.9775, 8856.213, 1363.0), (0.0, 149.06260831355954, -0.0), (1.5, 1.5, 1.5), "Remains_Bones_Assemblage_A_4", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2600.062, 8903.967, 1362.3353), (-4.00671454546262, -136.19513277632842, -6.904173664534581), (1.5, 1.5, 1.5), "Remains_Bones_Assemblage_A10", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2781.062, 8730.967, 1368.3353), (25.376558543385908, 41.272640951427455, -27.97534366620223), (1.5, 1.5, 1.5), "Remains_Bones_Assemblage_A11", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2689.8213, 8436.711, 1379.538), (-4.219422230812552, 31.31815077653037, 31.521774298583676), (1.5, 1.5, 1.5), "Remains_Bones_Assemblage_A12", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2779.062, 8400.967, 1420.3353), (5.924758744337118, -31.328797044912108, 29.11380996218466), (1.5, 1.5, 1.5), "Remains_Bones_Assemblage_A13", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2528.062, 8321.967, 1311.3353), (8.362591332947527, 40.481961380180046, 5.701614505907339), (1.5, 1.5, 1.5), "Remains_Bones_Assemblage_A2", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (948.6214, 9984.729, 828.1386), (-5.450863357355109e-08, 115.3121875336577, 2.812601369410731), (1.5, 1.5, 1.5), "Remains_Bones_Assemblage_A3", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1547.2799, 8384.856, 849.90857), (10.370152366852146, 15.603417179141378, 25.732258059740783), (1.5, 1.5, 1.5), "Remains_Bones_Assemblage_A4", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (978.77936, 9771.505, 810.95416), (0.6835782109192521, 163.59403466760003, 7.509146816041773), (1.5, 1.5, 1.5), "Remains_Bones_Assemblage_A5", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1687.399, 8349.953, 1008.15204), (10.370150659470688, 15.603932543405836, 31.35749504265313), (1.5, 1.5, 1.5), "Remains_Bones_Assemblage_A6", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2347.0708, 8981.098, 1166.2451), (-2.812377870572861, 149.06260901052048, 2.8125012227159853), (1.5, 1.5, 1.5), "Remains_Bones_Assemblage_A7", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2754.9104, 8743.67, 1351.6547), (-2.798889177843892, -154.96331793116093, 11.259020128680826), (1.5, 1.5, 1.5), "Remains_Bones_Assemblage_A8", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1930.2799, 8287.856, 1142.9086), (-8.107665994362899, 69.52480082288139, 6.038151061305269), (1.5, 1.5, 1.5), "Remains_Bones_Assemblage_A9", _folder)
if a: placed += 1
else: skipped += 1

# Batch 30: StaticMesh'Remains_Bones_Assemblage_C' (9 instances)
_mesh_path = "/Game/Art/Assets/Kits/Deco/Warrens_Tomb/Remains_Bones_Assemblage_C"
_materials = ['/Game/Art/Assets/Kits/Deco/Orc/Shanty/Material/Orc_Shanty_Midden/MI_Orc_Shanty_Midden_Mat_Inst2']
_folder = "Reconstruction/BD_BB_Chapter5_BoneHoard/Meshes"
a = spawn_static_mesh(_mesh_path, _materials, (2173.2244, 8272.229, 1195.5704), (10.641182695003996, 3.706025248972728, 25.639080760029536), (1.75, 1.75, 1.75), "Remains_Bones_Assemblage_C_13", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2113.1367, 8480.689, 1078.2426), (0.7573583784927626, 19.59065468723021, 6.2413453949227495), (1.75, 1.75, 1.75), "Remains_Bones_Assemblage_C10", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1946.46, 8030.151, 1253.7749), (1.2951836931545937, -144.29968142664086, -29.182066708575174), (1.75, 1.75, 1.75), "Remains_Bones_Assemblage_C2", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1814.5641, 8991.749, 820.13074), (17.423837069470576, 86.980742542805, 5.200439721877079), (1.75, 1.75, 1.75), "Remains_Bones_Assemblage_C4", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1922.9796, 8557.065, 1003.89014), (-4.331268228796886, -27.915709778736954, -2.559295579540039), (1.75, 1.75, 1.75), "Remains_Bones_Assemblage_C5", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2336.1367, 8927.689, 1166.2426), (10.263554004276797, 102.60604326521984, 18.823581678741995), (1.75, 1.75, 1.75), "Remains_Bones_Assemblage_C6", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2671.1367, 8790.689, 1381.2426), (6.963988476948391, 121.34368602737644, 13.410281137006788), (1.75, 1.75, 1.75), "Remains_Bones_Assemblage_C7", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2643.3972, 8361.204, 1405.5388), (2.986649202515393, -1.7382812236576377, 5.8796398147747935), (1.5, 1.5, 1.5), "Remains_Bones_Assemblage_C8", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2238.648, 8891.99, 1144.6815), (-1.3457642156513365, 36.13818586103829, 0.41953864040898453), (1.75, 1.75, 1.75), "Remains_Bones_Assemblage_C9", _folder)
if a: placed += 1
else: skipped += 1

# Batch 31: StaticMesh'Dirt_Mound_A' (7 instances)
_mesh_path = "/Game/Art/Assets/Kits/Misc/Dirt_Mounds/Dirt_Mound_A"
_materials = ['/Game/Art/Assets/Kits/Misc/Dirt_Mounds/Materials/Suburbs_Dirt_Inst']
_folder = "Reconstruction/BD_BB_Chapter5_BoneHoard/Meshes"
a = spawn_static_mesh(_mesh_path, _materials, (8754.807, 9250.359, 1251.959), (0.0, 100.57746785417176, -0.0), (1.0, 1.0, 1.0), "Dirt_Mound_A_211", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (8846.714, 8857.231, 1251.959), (0.0, 100.57746785417176, -0.0), (1.0, 1.0, 1.0), "Dirt_Mound_A2", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (7080.6836, 10862.766, 1250.0752), (0.0, 169.73082619712375, -0.0), (1.0, 1.0, 1.0), "Dirt_Mound_A4_267", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (6082.3306, 10937.962, 1242.0933), (0.0, -155.35454698489613, 0.0), (1.0, 1.0, 1.0), "Dirt_Mound_A5", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5792.577, 10904.003, 1251.251), (0.0, -174.8200308965506, 0.0), (1.0, 1.0, 1.0), "Dirt_Mound_A6", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4056.1475, 9161.571, 1249.3691), (0.0, -88.08397956134156, 0.0), (1.0, 1.0, 1.0), "Dirt_Mound_A7_287", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4168.71, 9479.944, 1245.8555), (0.0, -116.12934629761709, 0.0), (1.0, 1.0, 1.0), "Dirt_Mound_A8", _folder)
if a: placed += 1
else: skipped += 1

# Batch 32: StaticMesh'Dirt_Mound_B' (12 instances)
_mesh_path = "/Game/Art/Assets/Kits/Misc/Dirt_Mounds/Dirt_Mound_B"
_materials = ['/Game/Art/Assets/Kits/Misc/Dirt_Mounds/Materials/MI_Mines_Dirt']
_folder = "Reconstruction/BD_BB_Chapter5_BoneHoard/Meshes"
a = spawn_static_mesh(_mesh_path, _materials, (8527.883, 9724.127, 1237.5791), (-1.4934389454835757, 125.65384538473344, -9.609954331697962), (1.0, 1.0, 1.0), "Dirt_Mound_B_214", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (8267.683, 11563.227, 1321.9663), (-0.4142762739784686, 137.6510475530722, -6.110716774811023), (1.238423, 1.238423, 1.238423), "Dirt_Mound_B10", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (7499.57, 11917.315, 1323.6519), (-0.4140930576409444, 168.6674409418135, -6.110718738591848), (1.4640651, 1.4640651, 1.4640651), "Dirt_Mound_B11", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (6189.526, 12074.848, 1321.7432), (-0.41406241765468627, -172.21536099120422, -6.110715931595992), (1.464065, 1.464065, 1.464065), "Dirt_Mound_B12", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (8730.037, 7765.4834, 1237.4648), (-3.655762136370447, 75.33070504646432, -7.38287304599124), (1.0, 1.0, 1.0), "Dirt_Mound_B2_238", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (8556.684, 7365.4253, 1234.0059), (-6.323730707191157, 51.55253484534569, -5.2841492846164035), (1.0, 1.0, 1.0), "Dirt_Mound_B3", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (6063.2285, 4964.4785, 1326.106), (0.0, -11.722656453049458, 0.0), (1.5048666, 1.5048666, 1.5048666), "Dirt_Mound_B4_38", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (6819.1987, 4954.4575, 1341.7397), (0.0, 14.38307985474693, -0.0), (1.504867, 1.504867, 1.504867), "Dirt_Mound_B5", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (7368.992, 5071.45, 1339.04), (0.0, 8.888382079292882, -0.0), (1.504867, 1.504867, 1.504867), "Dirt_Mound_B6", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (9950.933, 8954.897, 1337.6943), (0.0, 101.42475693976533, -0.0), (1.3846273, 1.3846273, 1.3846273), "Dirt_Mound_B7_61", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (9544.6, 10282.189, 1336.8857), (0.0, 124.65839477773767, -0.0), (1.384627, 1.384627, 1.384627), "Dirt_Mound_B8", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (8622.528, 11348.184, 1333.4463), (0.0, 147.80550722557768, -0.0), (1.2384226, 1.2384226, 1.2384226), "Dirt_Mound_B9_86", _folder)
if a: placed += 1
else: skipped += 1

# Batch 33: StaticMesh'Dirt_Mound_C' (3 instances)
_mesh_path = "/Game/Art/Assets/Kits/Misc/Dirt_Mounds/Dirt_Mound_C"
_materials = ['/Game/Art/Assets/Kits/Misc/Dirt_Mounds/Materials/MI_Mines_Dirt']
_folder = "Reconstruction/BD_BB_Chapter5_BoneHoard/Meshes"
a = spawn_static_mesh(_mesh_path, _materials, (8204.371, 5425.1133, 1317.6387), (-1.3896789859232026, 30.052142534659822, -2.799254786764557), (1.4557832, 1.4557832, 1.4557832), "Dirt_Mound_C_43", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4271.9004, 5645.644, 1319.0059), (-2.136077661064215, -36.833619244363156, -2.61584449809345), (1.7123836, 1.7123836, 1.7123836), "Dirt_Mound_C2_145", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3628.289, 6281.1763, 1296.5029), (-2.135986218724411, -57.15084071770664, -2.615844590414678), (1.712384, 1.712384, 1.712384), "Dirt_Mound_C3", _folder)
if a: placed += 1
else: skipped += 1

# Batch 34: StaticMesh'Dirt_Mound_D' (7 instances)
_mesh_path = "/Game/Art/Assets/Kits/Misc/Dirt_Mounds/Dirt_Mound_D"
_materials = ['/Game/Art/Assets/Kits/Misc/Dirt_Mounds/Materials/MI_Mines_Dirt']
_folder = "Reconstruction/BD_BB_Chapter5_BoneHoard/Meshes"
a = spawn_static_mesh(_mesh_path, _materials, (4108.1367, 7852.3877, 1243.7734), (0.0, 11.268073918113227, -0.0), (1.0, 1.0, 0.35396197), "Dirt_Mound_D_291", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4412.326, 7737.1123, 1257.5879), (3.98713624549621, -153.6617579733748, 0.8121769233912001), (1.0, 1.0, 0.021517826), "Dirt_Mound_D2", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (7112.8555, 10138.619, 1260.2134), (-1.5325012251326215, 63.06183979767157, 5.916354096703513e-07), (1.0, 1.0, 0.1110184), "Dirt_Mound_D3_50", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5954.838, 6816.979, 1258.7676), (0.7044998702343989, 77.30000922597496, 0.01480943291539376), (1.0, 1.0, 0.11403421), "Dirt_Mound_D4_77", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4695.337, 7926.0996, 1257.1543), (0.3598289806968008, 12.734290454737913, -0.19705200396388295), (1.0, 1.0, 0.026447747), "Dirt_Mound_D5", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (7650.7026, 5108.1313, 1329.042), (0.0, 100.39469781654975, -0.0), (1.0, 1.0, 1.0), "Dirt_Mound_D6_46", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (9164.422, 6151.326, 1332.562), (-1.854431151560482, 140.37009407766706, 1.5357853516101074), (1.0, 1.0, 1.0), "Dirt_Mound_D7", _folder)
if a: placed += 1
else: skipped += 1

# Batch 35: StaticMesh'Dirt_Mound_E' (54 instances)
_mesh_path = "/Game/Art/Assets/Kits/Misc/Dirt_Mounds/Dirt_Mound_E"
_materials = ['/Game/Art/Assets/Kits/Misc/Dirt_Mounds/Materials/MI_Mines_Dirt']
_folder = "Reconstruction/BD_BB_Chapter5_BoneHoard/Meshes"
a = spawn_static_mesh(_mesh_path, _materials, (5070.7188, 10639.572, 1256.75), (0.0, -58.53262220244847, 0.0), (1.0, 1.0, 0.47962186), "Dirt_Mound_E_275", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5449.823, 6370.33, 1253.6699), (0.0, 70.20503853598872, -0.0), (1.0, 1.0, 0.11497823), "Dirt_Mound_E11_315", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (6954.088, 6879.5864, 1251.2178), (0.7933946843130236, 121.46262733793532, -0.2465820453743372), (1.0, 1.0, 0.31147966), "Dirt_Mound_E13", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (8219.8125, 8094.9854, 1256.6714), (0.9495258706846165, 178.93582733421852, 0.3566039240861223), (1.0, 1.0, 0.16167592), "Dirt_Mound_E14", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (7666.712, 6422.3154, 1256.9004), (-0.008209227758313724, 127.75337119524016, 0.12325998450045779), (1.0, 1.0, 0.17285632), "Dirt_Mound_E15", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (7625.1113, 7185.6455, 1247.252), (0.7933949234935386, 136.58535077685917, -0.2465820433032724), (1.0, 1.0, 0.31148), "Dirt_Mound_E16", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4738.824, 9105.987, 1259.3462), (0.5696514595390293, -8.202820248663068, 0.8482248513241687), (1.0, 1.0, 0.15438329), "Dirt_Mound_E17_210", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3943.371, 9566.208, 1339.2578), (0.302611524516442, 167.70213315476437, -0.3501281537677501), (1.0, 1.0, 0.08412131), "Dirt_Mound_E18", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (9033.958, 8596.494, 1336.7529), (0.09997346896884048, -171.08264735845216, 0.5158407188390991), (1.0, 1.0, 0.161676), "Dirt_Mound_E19", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (6277.437, 10056.779, 1239.5522), (0.0, 13.321281048949256, -0.0), (1.0, 1.0, 0.479622), "Dirt_Mound_E2", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (8878.846, 7462.994, 1337.4307), (0.2538986055946731, 170.98524875244505, -0.013946533872968682), (1.0, 1.0, 0.161676), "Dirt_Mound_E20", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (8392.244, 6773.461, 1338.8892), (0.22787557066739716, 147.78958110027529, -0.11291502769384054), (1.0, 1.0, 0.161676), "Dirt_Mound_E21", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (8745.321, 5978.4595, 1340.2397), (0.2089764661782171, 139.39019910379565, -0.14498900428598144), (1.0, 1.0, 0.09338313), "Dirt_Mound_E22", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (9077.616, 6482.9097, 1339.6924), (0.25139822067539325, 165.33068434693635, -0.03909301873163623), (1.0, 1.0, 0.093383), "Dirt_Mound_E23", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (8069.1226, 5625.6035, 1339.4219), (0.16519491955873475, 124.6065128084562, -0.19357298272444654), (1.0, 1.0, 0.093383), "Dirt_Mound_E24", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (7558.545, 6095.406, 1339.6812), (-0.241027846466075, 124.60864250012963, 0.20556852489928915), (1.0, 1.0, 0.093383), "Dirt_Mound_E25", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (7297.7754, 5236.369, 1340.9131), (0.11173507374219287, 110.1824424996763, -0.2286682130702472), (1.0, 1.0, 0.093383), "Dirt_Mound_E26", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (6363.71, 5154.2466, 1341.332), (-0.013092042871148735, 90.28337508242382, 0.18100785305845038), (1.0, 1.0, 0.093383), "Dirt_Mound_E27", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (6469.9146, 5864.587, 1340.3037), (-0.035156249020869695, 97.31350948898832, 0.17807539053841118), (1.0, 1.0, 0.093383), "Dirt_Mound_E28", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (6609.5864, 10056.779, 1239.5522), (0.0, 13.321281048949256, -0.0), (1.0, 1.0, 0.479622), "Dirt_Mound_E3", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4746.68, 5609.073, 1340.4731), (0.09911287613036096, 53.00553624585158, 0.15202619934537015), (1.0, 1.0, 0.093383), "Dirt_Mound_E30", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5588.2876, 5262.9985, 1339.5679), (-0.00744626798875465, 88.45861169800699, 0.1812508782695124), (1.0, 1.0, 0.093383), "Dirt_Mound_E31", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4640.554, 6557.1543, 1341.8115), (0.08666143650770328, 57.628614668257114, 0.15957616605473302), (1.0, 1.0, 0.093383), "Dirt_Mound_E32", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3978.4824, 6698.255, 1339.5596), (0.00247935679599355, 85.33211472059527, 0.18158006353450715), (1.0, 1.0, 0.093383), "Dirt_Mound_E33", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3948.4648, 6279.881, 1343.9829), (-2.017852586236577, 43.48601929806331, -0.8608702951866363), (1.0, 1.0, 0.0035926066), "Dirt_Mound_E34", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4348.131, 5944.7173, 1342.4121), (0.6301941228359857, -115.83877471883366, -0.013153087578196075), (1.0, 1.0, 0.093383), "Dirt_Mound_E35", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4700.7617, 7996.4326, 1244.1841), (-2.6506657149277424, 22.07720308364999, 0.5953905603932619), (1.0, 1.0, 0.32519808), "Dirt_Mound_E36", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3251.8545, 7404.5566, 1340.935), (0.4499113792683284, 26.518083377481748, -0.044708245588976646), (1.0, 1.0, 0.090364575), "Dirt_Mound_E37", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4008.8545, 7459.942, 1339.8403), (-0.7596129480151675, 33.68674659739797, -0.14059443529373777), (1.0, 1.0, 0.090365), "Dirt_Mound_E38", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3768.9258, 8519.857, 1341.1577), (-0.5720214269550487, 9.092233376721277, -0.24179081616507586), (1.0, 1.0, 0.090365), "Dirt_Mound_E39", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4618.3516, 10173.919, 1256.7583), (0.0, -35.16925368217502, 0.0), (1.0, 1.0, 0.07509273), "Dirt_Mound_E4", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3073.9756, 8756.37, 1340.0791), (-0.03726196405067243, 9.090346992224719, -0.2417602624011152), (1.0, 1.0, 0.090365), "Dirt_Mound_E40", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3156.1934, 7938.4033, 1341.877), (-1.0645448400735615, 23.690786921444612, -0.21682739333779885), (1.0, 1.0, 0.090365), "Dirt_Mound_E41", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4311.823, 10149.619, 1340.0107), (0.2195154172532486, 147.67625179334624, 0.2822177173533149), (1.0, 1.0, 0.084121), "Dirt_Mound_E42", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4705.1543, 10579.968, 1342.396), (0.055905479535188055, -50.947753899096355, -0.04470825266509219), (1.0, 1.0, 0.084121), "Dirt_Mound_E43", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4285.576, 11148.59, 1342.02), (-0.2895202781174958, -43.43420044682426, -0.08331300060862833), (1.0, 1.0, 0.084121), "Dirt_Mound_E44", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5356.962, 10973.574, 1340.9883), (0.04602864920047045, -62.27148165727154, -0.05480957026020578), (1.0, 1.0, 0.084121), "Dirt_Mound_E45", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (6269.787, 11168.599, 1341.7617), (0.02658309292158405, -80.46911155283289, -0.06637572819478729), (1.0, 1.0, 0.084121), "Dirt_Mound_E46", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (7482.1953, 10950.3955, 1341.8423), (-0.05496216181655533, -106.84920920801083, -0.12127685163714626), (0.8477545, 1.0, 0.08401714), "Dirt_Mound_E48", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (9702.126, 9372.154, 1341.7393), (0.08620379985583071, -156.1257566357691, -0.1619262568508261), (1.0, 1.0, 0.095806), "Dirt_Mound_E51", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (9445.509, 9976.744, 1341.2163), (-0.08041382030185118, 21.881531769680656, -0.008056642096312707), (1.0, 1.0, 0.095806), "Dirt_Mound_E52", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (8919.981, 10777.401, 1340.5557), (0.03880535571174325, -135.19188843306532, 0.12324890819790998), (1.0, 1.0, 0.095806), "Dirt_Mound_E53", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (7973.5107, 11460.474, 1339.5283), (0.031801341637724766, -111.5569706446656, 0.18485903061714665), (1.0, 1.0, 0.095806), "Dirt_Mound_E54", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (8467.988, 6536.8315, 1338.8145), (0.39719665629358847, 139.39144522894435, 0.07449622935231201), (1.0, 1.0, 0.093383), "Dirt_Mound_E55_27", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (6871.2456, 10637.836, 1250.0), (0.0, -104.2501485099317, 0.0), (1.0, 1.0, 0.39300704), "Dirt_Mound_E56_112", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4990.368, 11519.466, 1339.9575), (-0.2895202781174958, -43.43420044682426, -0.08331300060862833), (1.0, 1.0, 0.084121), "Dirt_Mound_E58_21", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5422.986, 11781.633, 1341.7402), (-0.2894592407966458, -70.38129191392709, -0.08331299789031489), (1.0, 1.0, 0.084121), "Dirt_Mound_E59", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4896.4014, 8732.216, 1239.5527), (0.0, 100.38889782553792, -0.0), (1.0, 1.0, 0.479622), "Dirt_Mound_E6", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (6225.9443, 11921.854, 1340.8965), (-0.2894592407966458, -70.38129191392709, -0.08331299789031489), (1.0, 1.0, 0.084121), "Dirt_Mound_E60", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (7472.428, 11669.408, 1339.6323), (-0.3625488183989377, 74.0686313688316, -0.3395995453357612), (1.0, 1.0, 0.084121), "Dirt_Mound_E61", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (8506.634, 10886.317, 1340.3164), (-0.3919067097612813, 7.392334178466383, -0.11108397653215822), (1.0, 1.0, 0.05381894), "Dirt_Mound_E62", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4090.6914, 8732.216, 1235.8232), (0.0, -167.0329602739005, 0.0), (1.0, 1.0, 0.479622), "Dirt_Mound_E7", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (6351.181, 7044.951, 1255.9795), (-0.008209227530313083, -176.21151134949972, 0.12326028832530532), (1.0, 1.0, 0.2575376), "Dirt_Mound_E8", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (6626.6772, 7100.5444, 1249.8027), (-0.008209227785213732, -157.0179120717867, 0.12325999319682268), (1.0, 1.0, 0.257538), "Dirt_Mound_E9", _folder)
if a: placed += 1
else: skipped += 1

# Batch 36: StaticMesh'Dirt_Mound_F' (2 instances)
_mesh_path = "/Game/Art/Assets/Kits/Misc/Dirt_Mounds/Dirt_Mound_F"
_materials = ['/Game/Art/Assets/Kits/Misc/Dirt_Mounds/Materials/MI_Mines_Dirt']
_folder = "Reconstruction/BD_BB_Chapter5_BoneHoard/Meshes"
a = spawn_static_mesh(_mesh_path, _materials, (9880.111, 8442.387, 1340.0), (0.0, 5.000006090594674, -0.0), (2.3125, 2.3125, 1.5625), "Dirt_Mound_F7_50", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (10159.896, 8954.125, 1848.0216), (0.0, 10.000229210918928, -0.0), (1.375, 1.1875, 1.7825954), "Dirt_Mound_F9_65", _folder)
if a: placed += 1
else: skipped += 1

# Batch 37: StaticMesh'Dirt_Mound_F' (5 instances)
_mesh_path = "/Game/Art/Assets/Kits/Misc/Dirt_Mounds/Dirt_Mound_F"
_materials = ['/Game/Art/Assets/Kits/Misc/Dirt_Mounds/Materials/Suburbs_Dirt_Inst']
_folder = "Reconstruction/BD_BB_Chapter5_BoneHoard/Meshes"
a = spawn_static_mesh(_mesh_path, _materials, (4361.717, 9768.47, 1257.1777), (0.0, 126.14938293236338, -0.0), (1.0, 1.0, 0.52488196), "Dirt_Mound_F_281", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (8160.193, 9149.632, 1258.1621), (0.0, 23.1940908403463, -0.0), (1.0, 1.0, 0.08144999), "Dirt_Mound_F2_61", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (8044.3374, 8935.828, 1260.5522), (1.0742734294133625, 23.19379232784658, 7.572028493196565e-06), (1.0, 1.0, 0.113135606), "Dirt_Mound_F3", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (9859.746, 7485.1963, 1328.6553), (-3.8108829125469024, -13.293486554476848, 0.1164337904391211), (1.0, 1.0, 1.0), "Dirt_Mound_F4_101", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (9986.155, 8167.5635, 1329.9932), (-3.8108828780140347, -13.293486564108449, 0.11643408686338452), (1.0, 1.0, 1.0), "Dirt_Mound_F5", _folder)
if a: placed += 1
else: skipped += 1

# Batch 38: StaticMesh'Dirt_Mound_F' (1 instances)
_mesh_path = "/Game/Art/Assets/Kits/Misc/Dirt_Mounds/Dirt_Mound_F"
_materials = ['/Game/Art/Assets/Kits/Misc/Dirt_Mounds/Materials/Sururbs_Dirt_DarkELQ_Inst']
_folder = "Reconstruction/BD_BB_Chapter5_BoneHoard/Meshes"
a = spawn_static_mesh(_mesh_path, _materials, (3996.5107, 8395.865, 1244.955), (0.0, 15.568710929563055, -0.0), (1.625, 1.625, 1.625), "Dirt_Mound_F6_97", _folder)
if a: placed += 1
else: skipped += 1

# Batch 39: StaticMesh'Dirt_Mound_G' (17 instances)
_mesh_path = "/Game/Art/Assets/Kits/Misc/Dirt_Mounds/Dirt_Mound_G"
_materials = ['/Game/Art/Assets/Kits/Misc/Dirt_Mounds/Materials/MI_Mines_Dirt']
_folder = "Reconstruction/BD_BB_Chapter5_BoneHoard/Meshes"
a = spawn_static_mesh(_mesh_path, _materials, (7331.8394, 10775.102, 1246.9004), (0.0, 57.55707363444929, -0.0), (1.0, 1.0, 1.0), "Dirt_Mound_G_230", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (8548.052, 11100.809, 1339.8516), (-1.3318479458549595, 48.45784338692875, 0.4289141106329878), (1.0, 1.0, 0.247116), "Dirt_Mound_G10_171", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (9754.99, 9654.219, 1341.7393), (0.014746376537800974, -0.8546752914396968, 0.9885811088727214), (1.0, 1.0, 1.0), "Dirt_Mound_G11_72", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (9150.811, 10834.508, 1340.8745), (0.01474641723922071, 41.00687793561776, 0.9885812367898742), (1.0, 1.0, 1.0), "Dirt_Mound_G12", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (8688.705, 11236.181, 1334.6719), (0.014746382978600812, 63.183551188632286, 0.9885816844092512), (1.0, 1.0, 1.0), "Dirt_Mound_G13", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (8011.4224, 11701.189, 1335.6436), (-1.1853028481489158, 63.20507304597177, 0.006840049393230252), (1.0, 1.0, 1.0), "Dirt_Mound_G14", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2936.1719, 8924.537, 1328.5078), (-6.645171045730877, 163.16264811964894, 2.005721811964267), (1.0, 1.0, 1.0), "Dirt_Mound_G15_138", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3033.5532, 7497.1626, 1321.9689), (-6.883025533469028, -160.2758490324364, 0.8890313019954172), (1.0, 1.0, 1.0), "Dirt_Mound_G16", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3305.879, 6884.9775, 1341.7402), (0.1427167896382502, -153.97781800438966, -0.13174438807490282), (1.2302421, 1.2302421, 1.2302421), "Dirt_Mound_G17", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (9687.783, 9081.823, 1335.0), (0.0, 15.000088880529146, -0.0), (1.875, 1.875, 1.875), "Dirt_Mound_G18_59", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (9667.711, 7604.1514, 1338.2607), (1.2958368231892297, 162.16712459146802, 0.19664473968711213), (1.0, 1.0, 0.24711597), "Dirt_Mound_G2_110", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (6723.6304, 10911.437, 1253.7393), (0.0, 77.90943616033098, -0.0), (1.0, 1.0, 1.0), "Dirt_Mound_G3", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (9548.055, 7228.7856, 1336.2773), (2.420038686334715, 161.04192785679402, 0.11837352318899064), (1.0, 1.0, 0.247116), "Dirt_Mound_G4", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (9777.666, 8153.0215, 1335.5972), (2.378571642251744, 169.21398113167425, 0.46121590426156067), (1.0, 1.0, 0.247116), "Dirt_Mound_G5", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (9094.104, 7946.217, 1335.6074), (2.378571642251744, 169.21398113167425, 0.46121590426156067), (1.0, 1.0, 0.247116), "Dirt_Mound_G6", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (9530.728, 9551.636, 1336.7578), (0.21575880287852087, 24.770285110596244, 0.09382858906261611), (1.0, 1.0, 0.247116), "Dirt_Mound_G8_166", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (8897.018, 9405.807, 1338.9902), (0.21575896222222862, 24.77028511173465, 0.09382898540761961), (1.0, 1.0, 0.247116), "Dirt_Mound_G9", _folder)
if a: placed += 1
else: skipped += 1

# Batch 40: StaticMesh'Dirt_Mound_H' (12 instances)
_mesh_path = "/Game/Art/Assets/Kits/Misc/Dirt_Mounds/Dirt_Mound_H"
_materials = ['/Game/Art/Assets/Kits/Misc/Dirt_Mounds/Materials/MI_Mines_Dirt']
_folder = "Reconstruction/BD_BB_Chapter5_BoneHoard/Meshes"
a = spawn_static_mesh(_mesh_path, _materials, (9366.193, 6807.7793, 1338.4238), (0.0, -171.51076557303452, 0.0), (1.0, 1.0, 1.0), "Dirt_Mound_H_107", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5660.8955, 11985.806, 1344.166), (0.0, 158.9666685056418, -0.0), (1.0, 1.0, 1.0), "Dirt_Mound_H10", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5722.2227, 6346.76, 1240.8256), (0.0, 150.5682127733013, -0.0), (2.875, 2.875, 2.712462), "Dirt_Mound_H13", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (10303.18, 8152.3374, 1853.686), (0.0, 85.00002013391547, -0.0), (2.0, 1.6875, 3.0625), "Dirt_Mound_H16_62", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4663.1123, 6956.8438, 1251.4678), (-0.34771711629940083, -103.77190862064957, 8.221373111686583), (1.478502, 1.478502, 0.459139), "Dirt_Mound_H2", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (6064.908, 7039.024, 1250.0), (0.0, 132.52812469477237, -0.0), (2.875, 2.875, 2.9236977), "Dirt_Mound_H20", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (6428.3584, 10465.188, 1257.6763), (0.0, 164.58589214312858, -0.0), (1.0, 1.0, 0.18432899), "Dirt_Mound_H4_276", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (6326.4624, 10927.674, 1257.6011), (-1.978111127244772e-08, 164.58476371067076, 5.15614648970361), (1.3071401, 1.3071401, 0.49146923), "Dirt_Mound_H5", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (6536.4634, 6653.408, 1250.4697), (2.0223258119034213e-08, 172.30226367988314, 4.619864904771467), (1.2577546, 1.0, 0.3607644), "Dirt_Mound_H6_318", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (7025.654, 11913.137, 1337.6064), (0.0, -61.547730174805125, 0.0), (1.2374623, 1.2374623, 1.2374623), "Dirt_Mound_H7_19", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (9853.06, 9391.521, 1343.2285), (0.0, 90.0000030488508, -0.0), (1.0, 1.0, 1.0), "Dirt_Mound_H8_68", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (6865.978, 12003.976, 1344.0498), (0.0, 90.0000030488508, -0.0), (1.0, 1.0, 1.0), "Dirt_Mound_H9_115", _folder)
if a: placed += 1
else: skipped += 1

# Batch 41: StaticMesh'Dirt_Mound_I' (21 instances)
_mesh_path = "/Game/Art/Assets/Kits/Misc/Dirt_Mounds/Dirt_Mound_I"
_materials = ['/Game/Art/Assets/Kits/Misc/Dirt_Mounds/Materials/BoneHoard_Bone_Mount_Inst1']
_folder = "Reconstruction/BD_BB_Chapter5_BoneHoard/Meshes"
a = spawn_static_mesh(_mesh_path, _materials, (9925.835, 8362.179, 1313.0789), (-2.5548400289331665, 10.35214743196458, -0.6059874760155498), (1.2938068, 1.2938068, 2.1635206), "Dirt_Mound_I15_3", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (9892.39, 9037.769, 1313.0789), (-2.0196226663704744, 10.34864285922459, -0.5081787251383169), (1.293807, 1.293807, 2.0016518), "Dirt_Mound_I16", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (8944.921, 8935.056, 1245.5001), (0.2573959661526976, 1.4673748658256651, -0.4496764817207596), (1.293807, 1.293807, 0.7878208), "Dirt_Mound_I17", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (7855.6465, 6857.547, 1289.8757), (-1.1416932113302298, 103.28785346401226, -0.2718811264046531), (1.293807, 1.293807, 1.293807), "Dirt_Mound_I18", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5841.6904, 5001.4395, 1319.5537), (-0.9359739474838122, -88.89427799595758, -1.1421812527805117), (1.293807, 1.293807, 1.3257998), "Dirt_Mound_I19", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5736.5547, 6147.4775, 1283.0791), (-0.9359740585473602, 38.859106803084856, -1.1421508225719323), (1.293807, 1.293807, 1.3258), "Dirt_Mound_I20", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3373.7188, 6647.189, 1332.406), (-0.9359741693376484, 94.42179198271218, -1.1421508985107451), (2.1219707, 1.293807, 0.9658688), "Dirt_Mound_I21", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4566.827, 6878.899, 1249.469), (2.806634643931864, -84.90814154608569, 9.06720117415091), (1.4589677, 1.0159043, 0.9656184), "Dirt_Mound_I22", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3540.8162, 10686.894, 1320.4734), (-0.4547423962480523, -131.09727189752985, -0.5903320168085736), (2.121971, 1.293807, 0.965869), "Dirt_Mound_I23", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5466.6797, 10686.894, 1276.7583), (0.38660920579124053, -131.09790144507085, 0.3742001665777399), (2.121971, 1.293807, 1.1221005), "Dirt_Mound_I24", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (8163.8193, 11765.6, 1332.9773), (-0.018127485027146138, 115.65896368392215, 1.216767551727954), (2.121971, 1.293807, 1.1221), "Dirt_Mound_I25", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (7393.6562, 10870.359, 1292.9615), (-0.2948607525578294, 177.80554428651632, 1.1208721740389163), (2.121971, 1.293807, 0.8346318), "Dirt_Mound_I26", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (8580.155, 9579.04, 1274.2268), (-2.8677981563210966, -113.23086409789661, -4.845763921966905), (2.121971, 1.293807, 1.2446928), "Dirt_Mound_I27", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (9778.888, 9539.575, 1313.0789), (-2.0196226663704744, 10.34864285922459, -0.5081787251383169), (1.293807, 1.293807, 1.3232697), "Dirt_Mound_I28", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (8835.206, 9049.514, 1223.0809), (-6.4339895108596, 149.87255898266702, -2.776763460238094), (1.3777766, 1.0030661, 1.244693), "Dirt_Mound_I29", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4124.36, 8852.987, 1259.9254), (-0.9359740193714802, -72.4815871955465, -0.2939148050687737), (2.121971, 1.293807, 1.1148243), "Dirt_Mound_I30", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5699.499, 12122.497, 1329.8396), (0.38660914512156025, -6.193420723701166, 0.3742018579311867), (2.121971, 1.293807, 1.5301716), "Dirt_Mound_I31", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4586.127, 11811.251, 1331.128), (0.3866091760959528, 6.609925230355787, 0.3742028551518553), (2.121971, 1.293807, 1.522289), "Dirt_Mound_I32", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (6454.8877, 6079.575, 1239.0789), (-2.0196226636275245, -62.77615264309626, -0.5081482315010344), (1.0, 1.0, 0.78125), "Dirt_Mound_I33", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4961.827, 6590.899, 1218.469), (2.806633764047031, 100.71659617844357, 9.068077057651857), (1.458968, 1.015904, 0.965618), "Dirt_Mound_I34", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4085.3599, 7930.9873, 1276.9254), (-0.9359741448763821, -4.981537742277491, -0.29391483329152907), (2.121971, 1.293807, 1.0), "Dirt_Mound_I35", _folder)
if a: placed += 1
else: skipped += 1

# Batch 42: StaticMesh'Dirt_Mound_I' (2 instances)
_mesh_path = "/Game/Art/Assets/Kits/Misc/Dirt_Mounds/Dirt_Mound_I"
_materials = ['/Game/Art/Assets/Kits/Misc/Dirt_Mounds/Materials/MI_Mines_Dirt']
_folder = "Reconstruction/BD_BB_Chapter5_BoneHoard/Meshes"
a = spawn_static_mesh(_mesh_path, _materials, (9941.439, 7807.3887, 1330.0), (0.0, 25.000012817384555, -0.0), (1.5, 1.5, 1.5), "Dirt_Mound_I7_53", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (9690.907, 9531.923, 1340.0), (0.0, 20.000025612318534, -0.0), (1.0, 1.0, 1.0), "Dirt_Mound_I8_56", _folder)
if a: placed += 1
else: skipped += 1

# Batch 43: StaticMesh'Dirt_Mound_I' (2 instances)
_mesh_path = "/Game/Art/Assets/Kits/Misc/Dirt_Mounds/Dirt_Mound_I"
_materials = ['/Game/Art/Assets/Kits/Misc/Dirt_Mounds/Materials/Sururbs_Dirt_DarkELQ_Inst']
_folder = "Reconstruction/BD_BB_Chapter5_BoneHoard/Meshes"
a = spawn_static_mesh(_mesh_path, _materials, (8147.8345, 8395.37, 1245.0), (0.0, -179.54491009631187, 0.0), (1.4375, 1.5625, 0.52055216), "Dirt_Mound_I11", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5161.9673, 10600.792, 1259.9398), (0.0, 142.01633291499428, -0.0), (1.0, 1.0, 0.32129616), "Dirt_Mound_I6", _folder)
if a: placed += 1
else: skipped += 1

# Batch 44: StaticMesh'Orc_Fort_9X9_Mound' (9 instances)
_mesh_path = "/Game/Art/Assets/Kits/Misc/Dirt_Mounds/Orc_Fort_9X9_Mound"
_materials = ['/Game/Art/Assets/Kits/Misc/Dirt_Mounds/Materials/MI_Mines_Dirt']
_folder = "Reconstruction/BD_BB_Chapter5_BoneHoard/Meshes"
a = spawn_static_mesh(_mesh_path, _materials, (8085.999, 10284.461, 1262.0396), (0.0, 43.31821241327202, -0.0), (1.0, 1.0, 1.0), "Orc_Fort_9X9_Mound_223", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (7916.728, 8687.584, 1259.1553), (0.0, -89.29503963989751, 0.0), (1.0, 1.0, 1.0), "Orc_Fort_9X9_Mound2_255", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (7988.799, 8352.861, 1259.1553), (-0.014862059383982034, 88.85924970460802, 0.402815137872163), (1.0, 1.0, 1.0), "Orc_Fort_9X9_Mound3", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (8729.966, 8509.844, 1251.8848), (-3.105804680468994, 0.6937713674339163, -0.037475589872946316), (1.0, 1.0, 1.0), "Orc_Fort_9X9_Mound4", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4855.657, 5277.97, 1341.7402), (0.0, -124.12970451825122, 0.0), (1.1293448, 1.1293448, 2.1290843), "Orc_Fort_9X9_Mound5_31", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5443.371, 5059.128, 1341.7402), (0.0, -93.53796560115445, 0.0), (1.129345, 1.129345, 2.129084), "Orc_Fort_9X9_Mound6", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4930.953, 11791.543, 1341.7402), (0.0, 116.56583624767127, -0.0), (1.6353943, 1.6353943, 1.6353943), "Orc_Fort_9X9_Mound7_119", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3998.1924, 11179.199, 1342.627), (0.0, 131.58440190776412, -0.0), (1.635394, 1.635394, 1.635394), "Orc_Fort_9X9_Mound8", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3004.169, 9670.326, 1341.7402), (0.0, 157.40109484782784, -0.0), (1.2357193, 1.2357193, 1.2357193), "Orc_Fort_9X9_Mound9_123", _folder)
if a: placed += 1
else: skipped += 1

# Batch 45: StaticMesh'Deep_Spike_A' (12 instances)
_mesh_path = "/Game/Unshippable/Whitebox/Rocks/Meshes/Deep_Spike_A"
_materials = ['/Game/Environments/ProcTexturing/ProcMaterial_Quarry_Ceilling_Fissure_8x8']
_folder = "Reconstruction/BD_BB_Chapter5_BoneHoard/Meshes"
a = spawn_static_mesh(_mesh_path, _materials, (5658.004, 10133.069, 1426.8882), (4.954151086786616, 24.78939465008118, 64.35077922206946), (2.2194629, 2.2194629, 2.2194629), "Deep_Spike_A10", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (6788.8066, 10241.8545, 1344.7361), (2.780310114874599, 179.41152863687668, -3.1919851916755992), (2.9948182, 2.9948182, 2.9948182), "Deep_Spike_A11", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (7200.0, 9850.0, 1305.0), (-0.298370306520388, 163.56012450509408, 15.480298183492433), (2.0449965, 2.0449965, 2.0449965), "Deep_Spike_A12", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (7565.0, 9705.0, 1305.0), (9.701332166883804, -174.0294354549943, 10.898087625732112), (2.7903159, 2.7903159, 2.7903159), "Deep_Spike_A13", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (6825.573, 10115.987, 1512.9999), (0.7123817556896186, 148.06998586710992, -4.171905191147693), (2.994818, 2.994818, 2.994818), "Deep_Spike_A14", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (7107.809, 7189.806, 1405.2743), (-3.0486448570479734, 19.296357200947497, -0.24670409213890038), (3.243067, 3.243067, 3.243067), "Deep_Spike_A15", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (7942.116, 8579.206, 1348.7823), (6.335825280110228, 111.97424257572958, 13.490934899553134), (2.5797691, 2.5797691, 2.5797691), "Deep_Spike_A16", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (8095.0, 7670.0, 1295.0), (-2.7944336828370644, 63.29123734564257, 4.579479433857557), (2.4648607, 2.4648607, 2.4648607), "Deep_Spike_A17", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (7680.0, 9145.0, 1360.0), (8.794346850982976, 132.2871023030144, 13.92831000586659), (2.554359, 2.554359, 2.554359), "Deep_Spike_A18", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (7787.8086, 8513.476, 1377.8187), (9.037177562962597, 99.90670483692759, 11.871602364347678), (2.579769, 2.579769, 2.579769), "Deep_Spike_A19", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5618.987, 7234.647, 1295.0), (17.978370079064806, 119.72934628880184, 60.851311442247365), (2.3440738, 2.3440738, 2.3440738), "Deep_Spike_A4", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4960.9336, 9205.445, 1348.4733), (8.022978367485736, 49.467596859803415, 56.27099485856598), (2.3834517, 2.3834517, 2.3834517), "Deep_Spike_A8", _folder)
if a: placed += 1
else: skipped += 1

# Batch 46: StaticMesh'PWM_Deep_Medium_Cluster_A' (35 instances)
_mesh_path = "/Game/Unshippable/Whitebox/Rocks/Meshes/PWM_Deep_Medium_Cluster_A"
_materials = ['/Game/Environments/ProcTexturing/ProcMaterial_Quarry_Ceilling_Fissure_8x8']
_folder = "Reconstruction/BD_BB_Chapter5_BoneHoard/Meshes"
a = spawn_static_mesh(_mesh_path, _materials, (4982.7188, 8882.137, 1279.7003), (-6.575500088440386, 150.4324275667802, -1.1428223237260873), (1.5, 1.5, 1.5), "PWM_Deep_Medium_Cluster_A_2", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (6575.0, 7148.064, 1030.0), (43.06129474125615, 91.49819494165249, -4.296022418559352), (1.154208, 1.5917087, 1.5917087), "PWM_Deep_Medium_Cluster_A10", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5125.508, 9467.126, 1293.2263), (-5.708586208264416, 138.19517409229255, 7.2149472278635916), (1.2542797, 1.2542797, 1.6917797), "PWM_Deep_Medium_Cluster_A11_53", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5476.7886, 9960.775, 1378.4557), (44.80023667047135, -78.2720215632153, -15.262913265821972), (1.1636326, 1.1636326, 1.1636326), "PWM_Deep_Medium_Cluster_A12", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (6262.064, 10228.561, 1299.6631), (-7.012788120200231, 91.7835700905911, -6.3389591548974), (1.5439676, 1.5439676, 1.5439676), "PWM_Deep_Medium_Cluster_A13", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (7169.9985, 10048.065, 1378.7491), (-12.519653350942402, 52.85649622519426, -6.229156411244483), (1.0447816, 1.0447816, 1.4822813), "PWM_Deep_Medium_Cluster_A14", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (7748.407, 9397.665, 1263.148), (0.0, 36.88853250305744, -0.0), (1.270024, 1.270024, 1.4580435), "PWM_Deep_Medium_Cluster_A15_72", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (7273.734, 7011.637, 1273.9703), (-4.01364150057597, -72.40185990501693, -8.435484924865024), (1.3048347, 1.3048347, 1.3048347), "PWM_Deep_Medium_Cluster_A16", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (7605.421, 7014.5215, 1314.0522), (-10.324307642348009, -66.27880951890437, -13.593381611415884), (0.99376994, 1.4312701, 1.4312701), "PWM_Deep_Medium_Cluster_A17", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (7948.0723, 7917.712, 1339.9142), (5.363951554584032, -27.573484995393652, -2.794738471147264), (1.1433892, 1.1433892, 1.1433892), "PWM_Deep_Medium_Cluster_A18", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (7944.433, 7634.6377, 1306.9696), (44.813930978929875, 166.74822513140776, -4.231323558299144), (0.6875, 1.125, 1.125), "PWM_Deep_Medium_Cluster_A19", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (7885.423, 8794.043, 1194.495), (0.0, -15.029633105812076, 0.0), (1.4362683, 1.4362683, 1.4362683), "PWM_Deep_Medium_Cluster_A20", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5204.501, 9405.039, 1125.0), (0.0, 108.0208159190857, -0.0), (0.75, 0.75, 1.1875), "PWM_Deep_Medium_Cluster_A21", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (7393.6055, 6704.244, 1193.2968), (-13.557069564030604, -81.20581716000267, -7.803224104654934), (0.77910924, 0.77910924, 0.77910924), "PWM_Deep_Medium_Cluster_A22", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (7841.376, 6860.3564, 1279.7344), (-15.47750814404022, -36.98235689765314, -15.307249786763451), (0.779109, 0.779109, 0.779109), "PWM_Deep_Medium_Cluster_A23", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5923.6045, 10274.413, 1276.2382), (2.090034471893236, 123.79427363769214, -20.025851269066866), (1.543968, 1.543968, 1.543968), "PWM_Deep_Medium_Cluster_A24", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (6257.3203, 10014.036, 1331.0085), (-7.012695133062929, 56.80265527820625, -6.338989853681838), (1.543968, 1.543968, 1.543968), "PWM_Deep_Medium_Cluster_A25", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5241.386, 9888.315, 1304.07), (0.2842383322083552, 174.9390497791783, -7.663513197351592), (1.25428, 1.25428, 1.69178), "PWM_Deep_Medium_Cluster_A26", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (6976.9756, 6930.9023, 1329.2186), (-20.075621278528363, -116.36098231038665, -10.792999007380308), (1.304835, 1.304835, 1.304835), "PWM_Deep_Medium_Cluster_A27_6", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (7020.0073, 10447.694, 1294.2999), (-23.326688993422774, 50.93560269796792, -5.910736627555616), (0.4581812, 0.46303675, 0.90053505), "PWM_Deep_Medium_Cluster_A28", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (7549.5845, 9986.464, 1326.8312), (-18.737182207800785, 76.7263636119739, -12.506165248464379), (0.458181, 0.463037, 0.900535), "PWM_Deep_Medium_Cluster_A29", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4900.488, 8072.4688, 1387.8336), (0.0, 170.00008159196898, -0.0), (1.0073074, 1.0073074, 1.0073074), "PWM_Deep_Medium_Cluster_A3", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (8218.84, 8835.827, 1250.7117), (5.363951554584032, -27.573484995393652, -2.794738471147264), (0.8036143, 0.8036143, 0.8036143), "PWM_Deep_Medium_Cluster_A30", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (8265.273, 8517.919, 1113.8795), (5.6252373693832265, -21.586823434711263, -2.2209474083329335), (0.803614, 0.803614, 0.803614), "PWM_Deep_Medium_Cluster_A31", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (8130.4126, 8186.3877, 1148.1404), (4.674828802074542, -39.46634076220898, -3.8390201623726545), (0.803614, 0.803614, 0.803614), "PWM_Deep_Medium_Cluster_A32", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (6563.5225, 10280.313, 1413.8654), (-7.0127269366114104, 91.78355884491886, -14.949767972521576), (0.67948306, 0.67948306, 0.67948306), "PWM_Deep_Medium_Cluster_A33", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (6884.588, 10350.848, 1361.8258), (-18.699370341120716, 80.10516322344779, -20.744995946663114), (0.679483, 0.679483, 0.679483), "PWM_Deep_Medium_Cluster_A34", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (7990.237, 9064.439, 1285.6152), (-2.4551390345166366, 74.05587591503097, -19.62237496635809), (0.679483, 0.679483, 0.679483), "PWM_Deep_Medium_Cluster_A35", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4863.785, 7817.869, 1283.3354), (-8.219085626134422, 174.40384347057264, 0.8027569609617021), (1.066048, 1.066048, 1.066048), "PWM_Deep_Medium_Cluster_A36", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5045.0, 7755.0, 1125.0), (39.44342962727599, -0.5481566419543153, -12.169159135652947), (1.0746486, 1.0746486, 1.0746486), "PWM_Deep_Medium_Cluster_A4", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4821.4146, 8481.043, 1345.2667), (-8.1704681269983, 175.91002489892304, -3.7451464364040326), (1.4000003, 1.4, 1.4), "PWM_Deep_Medium_Cluster_A5", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5048.9526, 7580.625, 1228.6025), (-7.974915471774212, -164.8491563437088, -2.1513062866273245), (1.2776341, 1.2776341, 1.2776341), "PWM_Deep_Medium_Cluster_A6", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5893.827, 7028.8315, 1177.8402), (-4.972381263468047, -118.12412100635964, 4.166095523039653), (1.3912513, 1.3912513, 1.5787513), "PWM_Deep_Medium_Cluster_A7", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5122.1943, 7250.479, 1235.8741), (-7.974915471774212, -164.8491563437088, -2.1513062866273245), (1.0660477, 1.0660477, 1.0660477), "PWM_Deep_Medium_Cluster_A8", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (6285.0, 7033.064, 1170.0), (1.3595742469932715, -135.01597266217348, -1.359924255920245), (1.1455479, 1.1455479, 1.1455479), "PWM_Deep_Medium_Cluster_A9", _folder)
if a: placed += 1
else: skipped += 1

# Batch 47: StaticMesh'PWM_Deep_Small_Cluster_A' (14 instances)
_mesh_path = "/Game/Unshippable/Whitebox/Rocks/Meshes/PWM_Deep_Small_Cluster_A"
_materials = ['/Game/Environments/ProcTexturing/ProcMaterial_Quarry_Ceilling_Fissure_8x8']
_folder = "Reconstruction/BD_BB_Chapter5_BoneHoard/Meshes"
a = spawn_static_mesh(_mesh_path, _materials, (6664.554, 10173.701, 1415.0605), (-34.61908225317417, 75.07001680173659, 6.184674665063613), (2.4369001, 2.4369001, 2.4369001), "PWM_Deep_Small_Cluster_A13", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5984.2603, 9755.148, 1266.1852), (-28.52108521351541, 119.2701716942132, 1.0879441448564726), (2.375, 2.375, 2.375), "PWM_Deep_Small_Cluster_A14", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (7380.8335, 9855.646, 1422.745), (-27.38323809832236, 39.44945947959384, -0.8464057499482371), (2.8705003, 2.8705003, 3.3080013), "PWM_Deep_Small_Cluster_A15", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (7709.2603, 9655.148, 1276.1852), (18.71576565093521, -135.28539212183506, -2.200377249836284), (2.375, 2.375, 2.375), "PWM_Deep_Small_Cluster_A16", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (6638.7305, 6894.05, 1350.8291), (24.947034694536086, 65.38846431024265, -7.491639314121318), (3.529848, 2.5093405, 3.529848), "PWM_Deep_Small_Cluster_A17", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (7405.6934, 7423.986, 1443.4384), (-41.076085026992345, -44.081358649329204, -5.9622514132234805), (3.25, 3.25, 3.25), "PWM_Deep_Small_Cluster_A18", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (7881.4487, 8272.72, 1432.5924), (-29.639157110939745, 25.236386302056715, -13.131254789974232), (3.25, 3.25, 3.25), "PWM_Deep_Small_Cluster_A19", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (7803.6924, 7271.7056, 1406.137), (22.807560363765308, -179.15759752002458, 2.2386906348733566), (3.7267115, 3.148842, 3.148842), "PWM_Deep_Small_Cluster_A20", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (6824.2603, 9860.148, 1266.1852), (-28.52108794066194, 79.2701854784441, 1.0879409627979573), (2.375, 2.375, 2.375), "PWM_Deep_Small_Cluster_A22", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (6840.063, 10265.648, 1311.653), (-31.477936764978903, 56.467504890946856, 16.396413576270525), (2.4369, 2.4369, 2.4369), "PWM_Deep_Small_Cluster_A23", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5352.4785, 7108.059, 1341.9052), (-22.570464051903254, -120.00192462478488, -1.9133287340898262), (3.3922315, 3.3922315, 3.3922315), "PWM_Deep_Small_Cluster_A4", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5634.8374, 7027.02, 1375.1925), (20.861463896173838, 71.9412598441107, 4.504393309333751), (2.1875, 2.1875, 2.1875), "PWM_Deep_Small_Cluster_A5", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5527.5684, 7086.8047, 1386.4519), (15.025705435995993, 55.35022708373907, 8.937985686526938), (2.4958184, 2.4958184, 2.4958184), "PWM_Deep_Small_Cluster_A6", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5270.4414, 9127.904, 1459.94), (-45.5757584913096, 160.14617914438713, 9.722266998747429), (3.4627976, 3.4627976, 3.4627976), "PWM_Deep_Small_Cluster_A9", _folder)
if a: placed += 1
else: skipped += 1

# Batch 48: StaticMesh'PWM_Nordic_4x4x4_A' (8 instances)
_mesh_path = "/Game/Unshippable/Whitebox/Rocks/Meshes/PWM_Nordic_4x4x4_A"
_materials = ['/Game/Environments/ProcTexturing/ProcMaterial_Quarry_2mx5m_B2']
_folder = "Reconstruction/BD_BB_Chapter5_BoneHoard/Meshes"
a = spawn_static_mesh(_mesh_path, _materials, (5000.0, 8800.0, 6300.0), (5.945242964578117e-07, 50.62501109776001, -89.99990518529708), (2.0, 2.0, 2.0), "PWM_Nordic_4x4x4_A_2", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (6200.0, 10300.0, 6200.0), (7.554763678594361e-05, -53.43713332711498, -89.99939036546101), (2.1875, 2.28125, 2.5625), "PWM_Nordic_4x4x4_A2", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (8100.0, 9400.0, 5800.0), (-22.471617350818697, 91.16415464947242, -3.0429987208255445), (2.1875, 2.28125, 2.5625), "PWM_Nordic_4x4x4_A3", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (6250.0, 10250.0, 5600.0), (-29.233949024095086, 7.7199095359865515, -8.684021038636947), (2.1875, 2.28125, 2.5625), "PWM_Nordic_4x4x4_A4", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5900.0, 7200.0, 6000.0), (-37.87774859153459, 63.38971023141091, 8.091480511365772), (2.1875, 2.28125, 2.5625), "PWM_Nordic_4x4x4_A5", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4900.0, 8300.0, 6200.0), (-35.88088463056582, 28.18444294227555, -107.43447112413466), (2.1875, 2.28125, 2.5625), "PWM_Nordic_4x4x4_A6", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (7000.0, 7200.0, 6000.0), (-22.499998564613673, 39.3744055540989, 0.0008696998949977682), (2.1875, 2.28125, 2.5625), "PWM_Nordic_4x4x4_A7", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (7000.0, 10000.0, 6100.0), (-22.49999822550006, -109.68740153414889, 0.000865271816372362), (2.1875, 3.4375, 2.5625), "PWM_Nordic_4x4x4_A8", _folder)
if a: placed += 1
else: skipped += 1

# Batch 49: StaticMesh'PWM_Nordic_8x8x8_A' (97 instances)
_mesh_path = "/Game/Unshippable/Whitebox/Rocks/Meshes/PWM_Nordic_8x8x8_A"
_materials = ['/Game/Environments/ProcTexturing/ProcMaterial_Quarry_2mx5m_B2']
_folder = "Reconstruction/BD_BB_Chapter5_BoneHoard/Meshes"
a = spawn_static_mesh(_mesh_path, _materials, (4394.8066, 7197.113, 4031.4822), (-17.05859238103414, 9.63575691746503, -176.12525992768283), (1.294024, 1.294024, 0.97999), "PWM_Nordic_8x8x8_A_56", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5411.854, 6587.038, 4697.4365), (-8.688965275127703, -38.89252096886511, -128.2260808914977), (1.858997, 1.294024, 1.461542), "PWM_Nordic_8x8x8_A10", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4708.3633, 7311.436, 4417.7646), (6.1889966479980485, -68.85588930773326, -129.22889841470862), (1.949672, 0.512405, 1.461542), "PWM_Nordic_8x8x8_A11", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (6671.832, 10352.532, 4544.09), (-46.7988079238762, -120.09054190639189, -161.0099081713117), (1.294024, 1.294024, 1.381574), "PWM_Nordic_8x8x8_A12_115", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5520.2266, 10331.66, 4915.2925), (-36.26988682519353, -84.85319088996144, -170.79850207982298), (1.294024, 1.294024, 1.75), "PWM_Nordic_8x8x8_A13", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (8480.704, 9303.69, 4209.9995), (-32.789791258887895, -167.96423359266637, -173.87244959204293), (1.4495628, 1.4336438, 1.381574), "PWM_Nordic_8x8x8_A14", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (7645.218, 9975.193, 4511.192), (-75.34530542477847, -78.70331497593439, -43.50119331861527), (1.294024, 1.294024, 1.381574), "PWM_Nordic_8x8x8_A15", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (8596.582, 8221.076, 4106.6006), (-27.94467631375253, 176.7313662561478, -164.43423908286582), (1.330092, 1.294024, 1.0160581), "PWM_Nordic_8x8x8_A16", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (8389.763, 8125.8125, 4624.933), (-88.62793775121928, -14.77480566674627, -158.78490340197806), (1.294024, 1.294024, 1.381574), "PWM_Nordic_8x8x8_A17", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (7317.943, 6512.5986, 4110.264), (-28.344842354619544, 98.78778688969429, -173.20678405624835), (1.406777, 1.550281, 1.3763312), "PWM_Nordic_8x8x8_A18", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (7111.2812, 6898.8477, 4609.784), (-73.91554721753619, 148.00015230292297, -29.729312648554345), (1.3609582, 1.294024, 1.381574), "PWM_Nordic_8x8x8_A19", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5405.4043, 10452.5, 4083.3418), (-11.258178514032565, -60.997104364700974, -178.1643294866143), (1.294024, 1.294024, 0.97999), "PWM_Nordic_8x8x8_A2", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (8072.54, 7381.2285, 4421.1357), (-26.397152999950894, 133.15676924421842, -169.18255731258859), (1.294024, 1.294024, 1.4927741), "PWM_Nordic_8x8x8_A20", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (7984.386, 9021.858, 4790.531), (-10.807555346475143, -169.50474726256024, -174.39013958993584), (1.3742102, 1.294024, 1.381574), "PWM_Nordic_8x8x8_A21", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (6968.346, 10322.713, 5016.2046), (65.38736376999508, -108.49216864877891, -6.748408551422603), (1.5150871, 1.294024, 1.381574), "PWM_Nordic_8x8x8_A22", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4671.6865, 9325.807, 4617.5205), (-31.952597647991457, -46.160118895790674, -169.6332995595577), (1.07626, 1.536556, 1.6106), "PWM_Nordic_8x8x8_A23", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (7939.9097, 7588.835, 4600.351), (-60.809411661384054, 178.88508516363325, -61.66113029771667), (1.4029897, 1.750626, 1.676892), "PWM_Nordic_8x8x8_A24", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4427.7007, 9328.751, 4785.2065), (-6.595215492165065, -39.70465382836252, -177.46808942409208), (1.94103, 1.536556, 1.535113), "PWM_Nordic_8x8x8_A25", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (7005.062, 6895.5474, 4782.001), (10.750396639812548, -87.08514720068773, -168.47937734554176), (1.125, 1.680625, 1.094289), "PWM_Nordic_8x8x8_A26", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5032.568, 10025.886, 5963.713), (3.659128800899636, -51.96412623809875, 177.86883666669235), (1.94103, 1.680625, 1.568891), "PWM_Nordic_8x8x8_A27", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (8021.117, 7871.8584, 5640.5312), (-13.537900350810006, 139.66768701025796, -178.30060629827406), (1.5, 1.625, 2.125), "PWM_Nordic_8x8x8_A28_9", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (10773.168, 10138.585, 1110.436), (-5.632415551042205, 58.49551082250459, -0.04556272754157729), (1.0, 1.1077414, 1.0), "PWM_Nordic_8x8x8_A29_9", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (6010.8535, 10821.486, 3814.157), (-11.819639120046869, -79.17952276354993, 178.7843459470251), (1.294024, 1.294024, 1.0095296), "PWM_Nordic_8x8x8_A3", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (11838.966, 11048.159, 1125.7012), (5.984218727030714e-10, -0.604461582591024, -4.397583062490395), (1.350321, 1.0, 1.0), "PWM_Nordic_8x8x8_A30", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (12041.333, 8013.8413, 1104.2959), (0.0, 115.46991697251089, -0.0), (1.0, 1.0, 1.0), "PWM_Nordic_8x8x8_A31", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (10784.816, 8300.301, 2579.63), (-38.02810077947742, 76.75108261473157, -177.66358842776864), (0.562317, 0.944081, 0.944081), "PWM_Nordic_8x8x8_A32_31", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (11130.015, 10626.662, 1060.4229), (0.8632679817517291, -134.09183273440786, -1.995971676137119), (1.0, 1.0713012, 1.0), "PWM_Nordic_8x8x8_A33_84", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (10713.432, 7942.8926, 2239.7163), (-1.0380554819283203, 79.2054823101169, -0.230895950026669), (0.618236, 1.0, 1.0), "PWM_Nordic_8x8x8_A34", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (11231.345, 8259.756, 2764.329), (-57.44787058315622, 140.97933384325572, -51.069784457220656), (0.618236, 1.0, 1.0), "PWM_Nordic_8x8x8_A35", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (11845.975, 8794.56, 2405.374), (-60.21868391984599, 96.93985635049319, -176.74727252441994), (0.75865304, 1.0894248, 1.0273733), "PWM_Nordic_8x8x8_A36", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (12003.149, 8259.756, 2442.6006), (-64.97153258401134, 126.79711506568735, -34.94710259998101), (0.618236, 1.0, 1.0), "PWM_Nordic_8x8x8_A37", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (11384.602, 8142.3584, 2031.8921), (-25.634124827560502, 84.32895949748152, -173.11985374922293), (0.562317, 0.944081, 0.944081), "PWM_Nordic_8x8x8_A38_25", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (11726.209, 8060.899, 1771.8584), (-16.5090628276585, 95.91368009650611, 1.6292737895184224), (0.618236, 1.0, 1.243512), "PWM_Nordic_8x8x8_A39", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5183.6387, 10540.003, 4053.1628), (-38.691957975090425, -43.41891596070225, -7.375063428385329), (1.294024, 1.294024, 0.97999), "PWM_Nordic_8x8x8_A4", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (12039.353, 9718.903, 2499.0745), (-65.72729882835948, -108.39930548966306, -163.28040578402104), (0.618236, 1.0, 1.0), "PWM_Nordic_8x8x8_A40", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4628.8022, 10479.9, 4176.8486), (-5.029815015607306, -122.90661751381693, -164.24212485789047), (1.294024, 1.294024, 0.97999), "PWM_Nordic_8x8x8_A41", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (10513.781, 9499.766, 1656.1821), (-10.122649259103513, -45.72008514890273, -0.4762260706295495), (0.77834404, 1.0, 1.329404), "PWM_Nordic_8x8x8_A42", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (11095.536, 10163.258, 1977.0449), (-13.494810224938563, -44.40477840183633, 179.44961407831556), (1.2808046, 1.049791, 1.180318), "PWM_Nordic_8x8x8_A43", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3566.7036, 8363.823, 5501.348), (-23.172515085643465, -10.669676730254597, 165.93322001768814), (1.294024, 1.294024, 0.97999), "PWM_Nordic_8x8x8_A44", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3804.8645, 9315.235, 5449.333), (-64.7532921159697, 167.24669958301908, 165.304571665697), (1.94103, 1.680625, 1.568891), "PWM_Nordic_8x8x8_A45", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2276.1074, 9331.085, 2239.7163), (-1.0380554700113542, -115.6628733224515, -0.2308959716479577), (0.618236, 1.0, 1.0), "PWM_Nordic_8x8x8_A46", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1845.1504, 8847.737, 2159.1343), (-82.58000421361666, -159.25103665569648, 65.8980478357898), (0.74350476, 1.0, 1.051029), "PWM_Nordic_8x8x8_A47", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1810.0391, 7983.745, 1775.5732), (-19.22244172704288, 75.46070758599777, -175.05757675539706), (0.618236, 1.0893614, 1.0), "PWM_Nordic_8x8x8_A48", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2411.1758, 7628.824, 1573.9131), (-4.408630230779703, -170.643523960931, -9.333527429290756), (1.0, 1.0, 1.0), "PWM_Nordic_8x8x8_A49", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (6191.217, 10940.416, 4096.789), (-41.672967068147535, -78.64287320527275, -1.5595678805005952), (1.294024, 1.294024, 0.97999), "PWM_Nordic_8x8x8_A5", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1687.6074, 7689.326, 1105.8193), (-5.805237003356744, 79.4496520163718, 1.667551489952673), (1.0, 1.0, 1.0), "PWM_Nordic_8x8x8_A50", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (811.0781, 8131.9316, 1180.5845), (-5.159118479185347, 88.34479412211427, -3.143676301648901), (1.0, 1.0, 1.0), "PWM_Nordic_8x8x8_A51", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (881.98047, 8576.348, 2259.769), (-38.63832647709613, 58.77915677281911, -165.94880783474125), (1.0, 1.0, 1.204187), "PWM_Nordic_8x8x8_A52", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1705.8711, 7662.249, 2059.455), (-29.51587072786053, 76.96780884024551, 4.82454151254614), (0.618236, 1.0, 1.736267), "PWM_Nordic_8x8x8_A53", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1708.3789, 9981.744, 2266.191), (-1.0380554346804234, -149.29702081426825, -0.23089597251614238), (0.618236, 1.0, 1.0), "PWM_Nordic_8x8x8_A54", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2145.545, 9924.619, 1179.3003), (-1.0380554346804234, -149.29702081426825, -0.23089597251614238), (1.0, 1.0, 1.0), "PWM_Nordic_8x8x8_A55", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1050.1128, 10868.173, 1169.0604), (1.0683694046599794, -13.788330668078931, -1.8879088987748562), (1.450336, 1.0, 1.374314), "PWM_Nordic_8x8x8_A56_287", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1067.1602, 10509.834, 2092.0771), (-30.268651883005155, -104.52251864270714, -1.3035294869913994), (1.0, 1.0, 1.109511), "PWM_Nordic_8x8x8_A57", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (840.51074, 9768.832, 2222.527), (-76.74316417803722, -124.32116473111486, 18.893273330338246), (0.344797, 1.5284599, 1.446212), "PWM_Nordic_8x8x8_A58", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1112.4125, 8967.551, 2389.1987), (-78.77442645662514, 109.39777005243069, 160.56303847601797), (0.800583, 1.9479038, 1.901998), "PWM_Nordic_8x8x8_A59", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (6842.8765, 10893.943, 3841.8489), (-17.708984867427965, -116.24446573845327, -170.68675442197443), (1.294024, 1.294024, 0.97999), "PWM_Nordic_8x8x8_A6", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (11110.415, 8751.299, 2606.0742), (-63.59195395880424, 63.08097121056101, -154.46204522555934), (0.88782394, 1.1834306, 1.0), "PWM_Nordic_8x8x8_A61", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2480.4229, 9327.677, 1034.8091), (5.337326999545529, -104.98208751913344, -0.06720021726898948), (1.0, 1.0, 1.0), "PWM_Nordic_8x8x8_A62", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (11822.965, 10770.447, 1870.2568), (-19.038631083480738, -79.08745676277813, -175.56143092416076), (1.2036107, 1.049791, 1.180318), "PWM_Nordic_8x8x8_A63", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2326.838, 9586.31, 1802.5122), (-5.160064434651529, 161.77288114827027, -177.22031809029252), (1.1082358, 1.0412503, 1.0), "PWM_Nordic_8x8x8_A64", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (829.5658, 8096.8794, 1759.9115), (15.053031851424418, -102.26378957363838, -179.47216106065568), (1.0, 1.163767, 1.7650331), "PWM_Nordic_8x8x8_A65", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2440.5771, 8717.976, 2091.336), (-5.623778734700468, 173.78079265727104, -178.35288419351), (0.830669, 0.830669, 0.337568), "PWM_Nordic_8x8x8_A66_399", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4423.4565, 10211.147, 5146.2236), (-3.9297491791907193, -116.11589686545146, -147.96265206658938), (1.07626, 1.536556, 1.6106), "PWM_Nordic_8x8x8_A67", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3624.6885, 10540.256, 4381.3833), (-13.119565822573241, -88.3776526303063, -159.86730665085906), (1.294024, 1.294024, 0.97999), "PWM_Nordic_8x8x8_A68", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4811.854, 7637.038, 6097.4365), (22.912715689192094, -163.78638362851189, -65.77166696703075), (1.858997, 1.294024, 1.461542), "PWM_Nordic_8x8x8_A69", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (7896.8506, 10357.559, 3888.9316), (-17.353547563876457, -127.40857993306182, -176.4106201537581), (1.294024, 1.294024, 0.97999), "PWM_Nordic_8x8x8_A7", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (10333.168, 8913.585, 1110.436), (-5.632385546018659, 123.49575657315671, 0.7159862362587126), (1.25, 1.072232, 1.0511677), "PWM_Nordic_8x8x8_A70", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (10061.481, 8449.476, 3254.4421), (-2.335937449021467, -171.4017635181129, -5.126678170064344), (0.625, 0.9375, 1.0), "PWM_Nordic_8x8x8_A71_10", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (10144.514, 8183.795, 3054.7825), (-3.9471441163044743, 168.63222719794038, -4.021210458252725), (0.5, 0.625, 0.6875), "PWM_Nordic_8x8x8_A72", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1689.343, 10430.592, 1267.6538), (-0.8743896425376022, -127.1544183933582, -0.6050414709762622), (1.0315012, 1.0, 1.0), "PWM_Nordic_8x8x8_A73", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4605.9087, 9838.598, 3851.4177), (-17.204652262598607, -31.194641725130047, -174.92713941808404), (1.294024, 1.294024, 1.0996253), "PWM_Nordic_8x8x8_A74", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4168.0513, 9070.667, 3926.3545), (-12.711334672685872, -58.79193624170309, -178.88701022295137), (1.294024, 1.294024, 1.099625), "PWM_Nordic_8x8x8_A75", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3924.9568, 8316.934, 3683.933), (-10.938750600946342, -7.510191820022381, -179.91356398061527), (1.294024, 1.294024, 1.099625), "PWM_Nordic_8x8x8_A76", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4442.047, 8543.458, 4285.6416), (-19.353180821723274, -20.64596379346545, -169.6172914544339), (1.5635427, 1.294024, 1.099625), "PWM_Nordic_8x8x8_A77", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4162.8936, 8856.073, 3794.534), (-10.328153255527953, -26.510983348036472, -176.3756111934845), (1.294024, 1.294024, 1.099625), "PWM_Nordic_8x8x8_A78", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (6057.3003, 10520.898, 4270.9014), (-11.693022406163372, -83.06947474328217, -177.70207481279675), (1.294024, 1.294024, 0.888679), "PWM_Nordic_8x8x8_A79", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4182.8096, 7762.3877, 4501.6123), (-7.950835021959862, 86.30903308791201, 164.3816878727488), (1.294024, 1.294024, 0.97999), "PWM_Nordic_8x8x8_A8", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4828.206, 9797.781, 4417.697), (-11.8992910344778, -69.0205023788498, 179.4121165549124), (1.294024, 1.294024, 0.888679), "PWM_Nordic_8x8x8_A80", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4516.572, 7735.367, 5221.049), (-6.226958406270582, 5.057194213474157, -160.6564981695937), (1.94103, 1.536556, 1.837469), "PWM_Nordic_8x8x8_A81", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5301.1836, 6696.985, 5058.995), (-21.78604315676202, 63.78613782966892, 174.23162052778852), (1.94103, 1.536556, 1.535113), "PWM_Nordic_8x8x8_A82", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (6226.051, 6507.4683, 4401.9995), (-20.021480790412543, 48.791987709325106, -169.77993228334427), (1.4723192, 1.294024, 1.24021), "PWM_Nordic_8x8x8_A83", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (7289.7793, 7004.4746, 4959.308), (-50.84521463673608, 140.6543766669592, -27.91409612958907), (1.294024, 1.750626, 1.676892), "PWM_Nordic_8x8x8_A84", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1647.7527, 8863.899, 2257.6929), (-81.49601163155101, 139.0378106904681, 127.11992155659134), (0.743505, 1.0, 1.051029), "PWM_Nordic_8x8x8_A85", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (12359.873, 10887.503, 1113.7704), (-4.183197313867579, -108.59951797182133, 1.357312787289792), (1.350321, 1.0, 1.0), "PWM_Nordic_8x8x8_A86", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (12347.743, 10795.974, 1855.2155), (-20.209380507846017, -106.26765199494545, 0.4994485363478213), (1.350321, 1.0, 1.1099279), "PWM_Nordic_8x8x8_A87", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (12483.374, 8124.505, 1114.5321), (3.672918305323451, 23.122676930446424, 0.3090331949923369), (1.0, 1.0, 1.0), "PWM_Nordic_8x8x8_A88", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (12346.62, 8224.798, 1761.295), (-15.606229768120818, 121.95302984795289, -5.6900023707388945), (0.618236, 1.0, 1.243512), "PWM_Nordic_8x8x8_A89", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (6052.29, 5969.8286, 4076.6392), (-7.751952912578867, -10.510893668709862, -143.6712934106994), (1.858997, 1.3687612, 1.24021), "PWM_Nordic_8x8x8_A9", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (10390.6455, 8541.788, 1107.0155), (-5.289306416923229, 152.11582094257196, -2.06524658639503), (1.25, 1.072232, 1.051168), "PWM_Nordic_8x8x8_A90", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (434.63873, 8183.45, 1212.5795), (0.7058420391835231, -39.757323097877475, 13.001170437701635), (1.0, 1.0, 1.0), "PWM_Nordic_8x8x8_A91", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (420.6758, 8478.204, 1783.5044), (0.7058443694482406, -39.75604456982145, 33.49356724471091), (1.0, 0.6157982, 1.0), "PWM_Nordic_8x8x8_A92", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (574.14795, 9025.551, 2476.2356), (42.59382963185432, -140.48732995291277, -131.1017867248807), (0.743505, 1.1990135, 1.3428748), "PWM_Nordic_8x8x8_A93_146", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (437.89343, 10808.656, 1151.5215), (-1.6101375014750645, -175.36393124518793, 1.4534750554933564), (1.450336, 1.0, 1.374314), "PWM_Nordic_8x8x8_A94", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (423.52628, 10724.637, 1902.5541), (-1.6100767793200856, -175.36391251547394, 28.792550040443906), (1.450336, 1.0, 1.374314), "PWM_Nordic_8x8x8_A95", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5966.3516, 10439.971, 4931.9556), (80.23462543163197, -169.0241005794582, 106.73869624458155), (1.515087, 1.294024, 1.381574), "PWM_Nordic_8x8x8_A96", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3720.1958, 7811.458, 3711.2078), (-10.938750600946342, -7.510191820022381, -179.91356398061527), (1.294024, 1.294024, 1.099625), "PWM_Nordic_8x8x8_A97", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (7508.96, 6449.3804, 4034.4292), (-28.344842354619544, 98.78778688969429, -173.20678405624835), (1.406777, 1.550281, 1.376331), "PWM_Nordic_8x8x8_A98", _folder)
if a: placed += 1
else: skipped += 1

# Batch 50: StaticMesh'PWM_Quarry_1x1x1_A' (29 instances)
_mesh_path = "/Game/Unshippable/Whitebox/Rocks/Meshes/PWM_Quarry_1x1x1_A"
_materials = ['/Game/Environments/ProcTexturing/ProcMaterial_Quarry_Atlas_1']
_folder = "Reconstruction/BD_BB_Chapter5_BoneHoard/Meshes"
a = spawn_static_mesh(_mesh_path, _materials, (5783.8867, 7586.1846, 1428.8616), (2.890502500076189, 132.30044705841436, -67.72013973808185), (1.0, 1.0, 1.0), "PWM_Quarry_1x1x1_A_230", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (8487.076, 7017.7383, 1736.0464), (-0.434997473663049, 175.0189703687184, -19.98107774989249), (2.375, 1.3125, 1.3125), "PWM_Quarry_1x1x1_A10_73", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (8296.131, 7217.985, 1978.7994), (-11.258512837245444, 60.77923623953978, 3.154749128711248), (2.5064867, 1.5, 1.9500918), "PWM_Quarry_1x1x1_A11_77", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (8071.8306, 9881.321, 2451.7886), (-6.066038595560926, 148.3523567625637, -171.5398267920716), (2.25, 3.0625, 2.25), "PWM_Quarry_1x1x1_A12", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (8240.047, 9646.692, 1620.9253), (-13.23529245954125, 128.40580282150395, 166.84163773140685), (3.0, 3.8125, 1.75), "PWM_Quarry_1x1x1_A13", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (8354.846, 6984.1436, 1351.8776), (0.0, -116.08086021977164, 0.0), (3.510781, 3.510781, 3.510781), "PWM_Quarry_1x1x1_A14", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (8381.271, 7129.912, 1558.0316), (0.0, 148.32605954242695, -0.0), (3.5483587, 3.015837, 3.510781), "PWM_Quarry_1x1x1_A15", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (8279.069, 7129.912, 1464.6483), (-5.584289353746231, 170.93467083338612, -1.5254820026141998), (3.548359, 3.015837, 3.510781), "PWM_Quarry_1x1x1_A16", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (8354.846, 7345.805, 1347.6337), (-15.241089437368435, 68.07067894697904, 6.041505320025548), (3.510781, 3.510781, 3.510781), "PWM_Quarry_1x1x1_A17", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (8107.034, 7543.2393, 2658.6697), (-8.478729770019823, 68.63506170764191, 3.3013042854063563), (2.9165082, 1.7251043, 2.759976), "PWM_Quarry_1x1x1_A18", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (8032.4155, 7345.9756, 2664.961), (-1.4773252019793655, 116.11406004213123, -9.849272769297636), (1.983468, 2.8810706, 2.759976), "PWM_Quarry_1x1x1_A19", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4526.352, 9764.354, 3476.7112), (2.3611082134965997, 89.56050187072049, -16.90472285718486), (2.5, 4.144016, 1.6875), "PWM_Quarry_1x1x1_A2_107", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (6930.0, 10850.0, 1275.0), (0.0, 0.0, -0.0), (1.0, 1.0, 1.0), "PWM_Quarry_1x1x1_A20_3", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (7966.0083, 10297.399, 1255.0), (0.0, 177.1875850299506, -0.0), (1.21875, 1.21875, 1.0), "PWM_Quarry_1x1x1_A21", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (8848.194, 8151.4785, 1265.0), (-3.051757728814559e-05, -95.62414282947682, 9.194250338435008e-06), (1.625, 1.8125, 1.0), "PWM_Quarry_1x1x1_A22", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (6839.8184, 6171.06, 1264.9999), (0.0003958900629587082, -75.93524692874138, -8.437194575401868), (1.625, 1.8125, 1.0), "PWM_Quarry_1x1x1_A24", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4626.3916, 10112.907, 1270.024), (5.624988698878223, 47.81176666136263, 9.541495747935182e-07), (1.0, 1.0, 1.0), "PWM_Quarry_1x1x1_A25", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4921.3916, 10337.907, 1280.024), (5.624989215071746, -25.313202216935895, 1.812213984771716e-06), (1.0, 1.0, 1.0), "PWM_Quarry_1x1x1_A26", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1836.4624, 9115.856, 791.80475), (5.037216264222732, -0.26272583987581, -2.8121032306502682), (1.0, 1.0, 1.0), "PWM_Quarry_1x1x1_A27_2", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (893.4624, 9900.856, 754.80475), (1.4319972336397198, 159.885549243899, -4.493102104203093), (1.0, 1.0, 1.0), "PWM_Quarry_1x1x1_A28", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (818.4624, 8937.856, 742.80475), (5.286437847816107, 159.96074257477525, -1.9247133210691103), (1.0, 1.0, 1.0), "PWM_Quarry_1x1x1_A29", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (6280.7383, 6263.0493, 3761.9727), (4.652294902450091, -170.35247286817037, -15.937957781633743), (6.060384, 4.144016, 4.144016), "PWM_Quarry_1x1x1_A3", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1690.4624, 8587.856, 741.80475), (5.612025083574496, -0.26367186697945016, -2.838287518954852), (1.0, 1.0, 1.0), "PWM_Quarry_1x1x1_A30", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5323.2754, 6952.7856, 4602.7314), (-26.204074064588077, -43.40969658602689, 49.876894347317176), (5.758197, 5.758197, 5.758197), "PWM_Quarry_1x1x1_A4_130", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (8422.582, 7425.095, 2451.7886), (-19.68313077186654, 86.38356273047333, -174.37043756453383), (2.25, 3.0625, 2.25), "PWM_Quarry_1x1x1_A5_9", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (8502.469, 7076.495, 1351.8776), (0.0, -59.353512621286136, 0.0), (3.5107806, 3.5107806, 3.5107806), "PWM_Quarry_1x1x1_A6_191", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (8533.597, 7287.3423, 2251.5742), (13.557774565952542, -132.44874923141663, 166.42549865113668), (1.4375, 2.5625, 1.4375), "PWM_Quarry_1x1x1_A7_43", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (9785.0, 9605.0, 1375.0), (0.0, 0.0, -0.0), (2.25, 2.25, 2.25), "PWM_Quarry_1x1x1_A8_44", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (9829.871, 7540.9287, 1385.0), (0.0, -20.000060948281234, 0.0), (2.5, 2.5, 2.5), "PWM_Quarry_1x1x1_A9_47", _folder)
if a: placed += 1
else: skipped += 1

# Batch 51: StaticMesh'PWM_Quarry_1x1x1_A' (1 instances)
_mesh_path = "/Game/Unshippable/Whitebox/Rocks/Meshes/PWM_Quarry_1x1x1_A"
_materials = ['/Game/Environments/ProcTexturing/ProcMaterial_Quarry_Ceilling_Fissure_8x8']
_folder = "Reconstruction/BD_BB_Chapter5_BoneHoard/Meshes"
a = spawn_static_mesh(_mesh_path, _materials, (7338.842, 6318.145, 1264.9998), (-3.0517578340614825e-05, 22.500763081735034, 9.000000586048922e-06), (1.625, 1.8125, 1.0), "PWM_Quarry_1x1x1_A23", _folder)
if a: placed += 1
else: skipped += 1

# Batch 52: StaticMesh'PWM_Quarry_1X1x1_C' (57 instances)
_mesh_path = "/Game/Unshippable/Whitebox/Rocks/Meshes/PWM_Quarry_1X1x1_C"
_materials = ['/Game/Environments/ProcTexturing/ProcMaterial_Quarry_Atlas_1']
_folder = "Reconstruction/BD_BB_Chapter5_BoneHoard/Meshes"
a = spawn_static_mesh(_mesh_path, _materials, (11483.429, 8591.111, 864.63525), (0.9875219216401856, -179.97638118289169, -94.15922062723543), (1.0, 1.0, 1.0), "PWM_Quarry_1X1x1_C_81", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2163.0771, 8470.305, 967.8428), (-2.3039855367140736, 166.7657187321539, 179.43337875356892), (1.189462, 1.189462, 1.189462), "PWM_Quarry_1X1x1_C10_321", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1090.1797, 9738.862, 843.73486), (-5.519592316129343, 125.98636533996672, -82.45458755577644), (1.0, 0.782369, 1.0), "PWM_Quarry_1X1x1_C11_381", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (936.2627, 9025.257, 828.4302), (2.518920626130215, 74.48593939293377, -82.50579647535697), (1.0, 0.782369, 1.168178), "PWM_Quarry_1X1x1_C12", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (837.5176, 9117.111, 834.50146), (0.7824387613271712, -85.23647941734312, -99.30737205098256), (0.56005, 0.342419, 0.728228), "PWM_Quarry_1X1x1_C13", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1684.41, 8369.662, 854.4053), (-5.265073431095378, 134.54644574352585, -84.09631151212385), (1.0, 0.782369, 1.168178), "PWM_Quarry_1X1x1_C14", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (8257.397, 7742.638, 1239.394), (-57.05772639840456, -177.85211507903358, -92.55861410678571), (1.0, 1.0, 1.0), "PWM_Quarry_1X1x1_C15_165", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5350.6777, 6958.9478, 1239.8203), (3.385985754172841e-08, 90.0000033225318, -33.85714263731502), (1.0, 1.0, 1.0), "PWM_Quarry_1X1x1_C16_233", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5461.4834, 7274.299, 1414.3966), (-2.986753820126443, 81.91336207478481, -110.13984877831898), (0.6147882, 0.6147882, 0.6147882), "PWM_Quarry_1X1x1_C17", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (6759.1997, 9909.615, 1262.9541), (-1.7849635137551476e-07, 90.00000547997544, -43.29784911209977), (1.0, 1.0, 1.0), "PWM_Quarry_1X1x1_C18_300", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (6230.795, 9781.662, 1678.136), (-19.33327731028512, 101.82222812620428, -122.30288366380591), (1.0, 0.59220624, 1.0), "PWM_Quarry_1X1x1_C19", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (11461.574, 8686.698, 821.1465), (-1.5215772123837803, -80.18630630802537, -89.26058741760116), (1.042713, 0.632627, 1.042713), "PWM_Quarry_1X1x1_C2", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (6217.123, 10152.471, 1244.5205), (-34.40096901630161, 146.12811393961005, -141.22920530775252), (1.0, 1.0, 1.0), "PWM_Quarry_1X1x1_C20", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5887.9966, 10079.197, 1475.2367), (-1.128554077110399e-06, 90.00000913298408, -123.10979690731988), (1.604745, 1.604745, 1.604745), "PWM_Quarry_1X1x1_C21", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5968.4814, 9344.047, 1431.2949), (-4.994931907247703, 84.23564409998774, -88.59804498824596), (0.8757959, 0.4680019, 0.8757959), "PWM_Quarry_1X1x1_C22", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (6030.4634, 7755.4155, 1558.478), (-9.298675345652656, 96.95700285563436, -124.52795034353673), (1.604745, 1.604745, 1.604745), "PWM_Quarry_1X1x1_C23", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5450.928, 8747.503, 1233.4048), (-15.576816907720787, 101.90049953486849, -128.12351526429822), (0.96490645, 0.96490645, 0.96490645), "PWM_Quarry_1X1x1_C24", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5484.4907, 10265.829, 1323.1915), (-1.128554077110399e-06, 90.00000913298408, -123.10979690731988), (1.604745, 1.604745, 1.604745), "PWM_Quarry_1X1x1_C25", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5760.8257, 7847.2646, 1589.2012), (-20.668427508114455, 149.41387626696132, -112.47973806622925), (1.604745, 1.604745, 1.604745), "PWM_Quarry_1X1x1_C26", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (7244.007, 7825.8877, 1634.9994), (-31.76565455632646, 116.33425520135002, -134.74308949366008), (1.604745, 1.604745, 1.604745), "PWM_Quarry_1X1x1_C27", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (7286.0117, 9141.273, 1728.5475), (-23.520848187848376, 107.75612458065174, -130.74788689365653), (1.604745, 1.604745, 1.604745), "PWM_Quarry_1X1x1_C28", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (11146.574, 9091.698, 826.1465), (-1.5215772123837803, -80.18630630802537, -89.26058741760116), (1.042713, 0.632627, 1.042713), "PWM_Quarry_1X1x1_C29", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (11895.017, 8888.028, 803.1314), (0.0, 15.057892522232875, -0.0), (1.0, 1.0, 1.0), "PWM_Quarry_1X1x1_C3_104", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (6743.102, 10438.505, 1292.5175), (7.450328654798352, -20.395599831017883, 22.428937859464657), (2.3634481, 3.1234815, 1.5959151), "PWM_Quarry_1X1x1_C30_29", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1880.6051, 8605.773, 786.84515), (0.0, 0.0, -127.67623454571498), (1.210576, 1.210576, 1.210576), "PWM_Quarry_1X1x1_C31_2", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2100.5776, 8529.686, 934.32007), (-1.9759825115362974, -2.5606690495265805, -127.63192030585449), (1.210576, 1.210576, 1.210576), "PWM_Quarry_1X1x1_C32", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2272.9639, 8458.298, 1017.09155), (-27.25551986062037, 38.4586156462057, -128.07989908469884), (1.5293826, 1.5293826, 1.5293826), "PWM_Quarry_1X1x1_C33", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2001.9548, 8579.365, 860.2324), (-19.599794190047106, 15.96119150428278, -130.45003700533218), (1.210576, 1.210576, 1.210576), "PWM_Quarry_1X1x1_C34_25", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2236.8281, 8875.384, 916.04724), (-21.659025373670435, 36.98840167245031, -122.71745515495117), (1.529383, 1.529383, 1.529383), "PWM_Quarry_1X1x1_C35", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2119.7424, 8901.535, 836.4525), (-21.659025373670435, 36.98840167245031, -122.71745515495117), (1.529383, 1.529383, 1.529383), "PWM_Quarry_1X1x1_C36", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2379.433, 8806.764, 1009.86426), (-21.659025373670435, 36.98840167245031, -122.71745515495117), (1.529383, 1.529383, 1.529383), "PWM_Quarry_1X1x1_C37", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2598.2156, 8781.283, 1140.8254), (-22.85601691719989, -6.143646074432191, -83.12107163175719), (1.529383, 1.3916633, 1.529383), "PWM_Quarry_1X1x1_C38", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2573.3633, 8380.394, 1196.5377), (-22.85601691719989, -6.143646074432191, -83.12107163175719), (1.529383, 1.391663, 1.529383), "PWM_Quarry_1X1x1_C39", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (12101.05, 9127.304, 841.7515), (-1.6000971100783057, 35.52416926964575, -91.14215999568951), (0.532516, 0.228532, 0.532516), "PWM_Quarry_1X1x1_C4_114", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2567.9739, 8281.213, 1196.4574), (-11.731478783175588, -50.82180642746256, -69.1269238454268), (1.529383, 1.391663, 1.529383), "PWM_Quarry_1X1x1_C40", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2697.0261, 8365.622, 1258.8606), (6.744501372758777, -15.594114294034194, -84.99614370486111), (1.529383, 1.391663, 1.529383), "PWM_Quarry_1X1x1_C41", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (8235.44, 7029.6367, 1470.4877), (-1.4891411105451111, -89.11660979064408, -89.92805968637357), (2.082901, 2.082901, 2.082901), "PWM_Quarry_1X1x1_C42_165", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (8350.648, 7174.0566, 1470.4177), (-0.3811966359421421, 52.86644801680139, -99.4242219917181), (3.2928066, 3.2928066, 3.2928066), "PWM_Quarry_1X1x1_C43", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (8319.678, 7242.0947, 1733.4604), (10.13836363638905, 5.0360108639674995e-06, -83.3957830228635), (2.5863395, 3.1618807, 2.5863395), "PWM_Quarry_1X1x1_C44_201", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (8319.678, 7107.471, 1733.4604), (8.889856876928551, 121.84699793634361, -96.17245684547339), (2.586339, 3.161881, 2.586339), "PWM_Quarry_1X1x1_C45", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (8136.204, 7129.7627, 2761.7979), (-3.379881650174554, 159.3053330254333, -87.92639220137069), (2.586339, 2.9695156, 2.586339), "PWM_Quarry_1X1x1_C46", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (8084.934, 10017.139, 1453.2537), (-6.097992832525426, 32.80532181458022, -92.97409682184814), (2.9111886, 3.4867306, 2.9111886), "PWM_Quarry_1X1x1_C47", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (7928.5796, 9924.696, 1473.0105), (5.116736889957137, -132.1009364217265, -85.54229709221003), (2.911189, 3.486731, 2.911189), "PWM_Quarry_1X1x1_C48", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (8432.263, 9407.4795, 1360.1838), (2.0103768762104997, -47.2257357838711, -81.00606478277408), (2.911189, 3.486731, 2.911189), "PWM_Quarry_1X1x1_C49", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (11483.466, 9351.402, 805.6689), (1.952689563661565, -173.42538755263118, -89.77479375698636), (0.532516, 0.381841, 0.532516), "PWM_Quarry_1X1x1_C5", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (8132.2056, 9414.761, 1386.9429), (-13.31097159682739, 29.490393415004327, -76.98440481536586), (2.911189, 3.486731, 2.911189), "PWM_Quarry_1X1x1_C50", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (8527.512, 9676.966, 1421.4711), (9.19754667825669, -128.192366912032, -99.09124726639803), (2.911189, 3.486731, 2.911189), "PWM_Quarry_1X1x1_C51", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (8444.394, 9843.111, 1463.5076), (0.5097954161630303, -79.59677162217598, -92.41136769589984), (2.911189, 3.405446, 2.911189), "PWM_Quarry_1X1x1_C52", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (8330.414, 9779.191, 1829.8214), (4.181710998451341, -79.75152020952457, -92.41765568914477), (2.911189, 3.405446, 2.911189), "PWM_Quarry_1X1x1_C53", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (8347.79, 9683.106, 1836.9604), (4.181710998451341, -79.75152020952457, -92.41765568914477), (2.911189, 3.405446, 2.911189), "PWM_Quarry_1X1x1_C54", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (7904.3843, 9841.45, 2670.2622), (-1.184115654223225, -68.23891805830615, 78.02049985253176), (2.038816, 2.5750852, 2.361493), "PWM_Quarry_1X1x1_C55", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (8034.3354, 9954.594, 2717.0024), (-6.123781288199865, -96.72581614797171, 69.90758922209335), (2.416654, 2.952923, 2.7393312), "PWM_Quarry_1X1x1_C56", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (6008.5933, 10785.893, 1226.3094), (-2.7522889884754265, -25.60436923396231, -0.16976921075237458), (2.363448, 3.123482, 1.595915), "PWM_Quarry_1X1x1_C57", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (10364.058, 8782.4, 1081.2158), (0.0, 17.27661883331131, -0.0), (0.744546, 0.744546, 0.744546), "PWM_Quarry_1X1x1_C6_187", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (10820.413, 8590.598, 860.76074), (0.0, 98.17908818966283, -0.0), (1.0, 1.156843, 1.111873), "PWM_Quarry_1X1x1_C7_190", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (10604.52, 8492.793, 1060.6274), (0.0, 90.76024383833823, -0.0), (0.530082, 0.530082, 0.530082), "PWM_Quarry_1X1x1_C8_202", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2041.998, 9093.191, 934.14404), (1.866585878543864, 127.37420764804398, -93.15368759578509), (1.0, 1.0, 1.0), "PWM_Quarry_1X1x1_C9_314", _folder)
if a: placed += 1
else: skipped += 1

# Batch 53: StaticMesh'PWM_Quarry_2x2x2_A' (68 instances)
_mesh_path = "/Game/Unshippable/Whitebox/Rocks/Meshes/PWM_Quarry_2x2x2_A"
_materials = ['/Game/Environments/ProcTexturing/ProcMaterial_Quarry_Atlas_1']
_folder = "Reconstruction/BD_BB_Chapter5_BoneHoard/Meshes"
a = spawn_static_mesh(_mesh_path, _materials, (10013.118, 8880.253, 1155.0356), (0.0, -149.87886911689915, 0.0), (1.536306, 1.536306, 1.536306), "PWM_Quarry_2x2x2_A_15", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (6672.2256, 11052.373, 3478.773), (-0.2493896834355616, 165.18309521002857, -175.87560010855674), (3.0495596, 3.1131215, 1.8191383), "PWM_Quarry_2x2x2_A10_8", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (10956.943, 8249.48, 767.9541), (0.0, 62.043469685837835, -0.0), (1.536306, 1.536306, 1.536306), "PWM_Quarry_2x2x2_A11_22", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (10495.589, 8310.895, 1106.2852), (0.0, 14.023025613794918, -0.0), (1.0, 1.0, 1.0), "PWM_Quarry_2x2x2_A12", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (10954.672, 8269.794, 980.1123), (0.0, -60.37680573685858, 0.0), (1.188202, 1.188202, 1.188202), "PWM_Quarry_2x2x2_A13_32", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (12315.82, 8559.093, 809.48145), (0.0, 18.85566263324974, -0.0), (1.188202, 1.188202, 1.188202), "PWM_Quarry_2x2x2_A14", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (11655.922, 8244.175, 925.50977), (0.0, -15.895170675705339, 0.0), (1.188202, 1.188202, 1.188202), "PWM_Quarry_2x2x2_A15", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (11065.531, 9320.0625, 856.7456), (0.0, -128.21840195967786, 0.0), (1.0, 1.0, 1.0), "PWM_Quarry_2x2x2_A16_94", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (11543.07, 8438.8545, 839.32324), (0.0, -96.87750453133805, 0.0), (1.188202, 1.188202, 1.188202), "PWM_Quarry_2x2x2_A17", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (10442.728, 8859.0, 983.1797), (5.24557163597553, -158.31350676743497, 2.89862339034382), (0.84605, 0.84605, 0.84605), "PWM_Quarry_2x2x2_A18", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2719.9023, 8845.928, 1208.771), (0.0, 87.33194535129401, -0.0), (1.274838, 1.274838, 1.274838), "PWM_Quarry_2x2x2_A19_252", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (10010.883, 8313.21, 1158.3418), (0.0, -97.66924549773968, 0.0), (1.536306, 1.536306, 1.536306), "PWM_Quarry_2x2x2_A2", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2160.4336, 8942.929, 895.50244), (0.0, 90.0000030488508, -0.0), (1.0, 1.0, 1.0), "PWM_Quarry_2x2x2_A20_302", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2355.2363, 8933.197, 1005.417), (0.0, -16.863493670532186, 0.0), (1.283643, 1.283643, 1.283643), "PWM_Quarry_2x2x2_A21_304", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2553.8584, 8982.054, 1164.2715), (-6.510101461001713, 79.89849646607495, -4.341003450634942), (1.130213, 1.130213, 0.765671), "PWM_Quarry_2x2x2_A22_306", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2243.0938, 9053.913, 999.07715), (-7.819214558869597, 45.712106569498275, 0.052270930914722055), (1.130213, 1.130213, 0.765671), "PWM_Quarry_2x2x2_A23_308", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1957.0205, 8474.903, 850.0), (0.0, -23.92837542052254, 0.0), (1.283643, 1.283643, 1.283643), "PWM_Quarry_2x2x2_A24_316", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1386.9961, 8176.007, 899.0703), (0.0, -96.96749497488624, 0.0), (1.283643, 1.450233, 1.283643), "PWM_Quarry_2x2x2_A25_336", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1777.1787, 9974.42, 880.9448), (1.995744023951526, -110.92180598733351, 0.9068801619833101), (1.598132, 1.743435, 1.283643), "PWM_Quarry_2x2x2_A26", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2144.9648, 8247.165, 1042.2881), (0.0, 90.0000030488508, -0.0), (1.0, 1.0, 1.0), "PWM_Quarry_2x2x2_A27_421", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2703.2334, 8298.063, 1281.9893), (0.0, 90.0000030488508, -0.0), (1.0, 1.0, 1.0), "PWM_Quarry_2x2x2_A28_429", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (10127.995, 8786.989, 1220.395), (0.0, -159.1476187670184, 0.0), (0.724991, 0.724991, 0.724991), "PWM_Quarry_2x2x2_A29_432", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (10191.816, 8249.48, 1081.1592), (0.0, -178.38717510790175, 0.0), (1.536306, 1.536306, 1.536306), "PWM_Quarry_2x2x2_A3", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (8228.896, 9776.782, 1829.4254), (-19.054964742221102, 111.1292254788205, -5.373565191985426), (2.0, 1.625, 1.625), "PWM_Quarry_2x2x2_A30_39", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (8323.441, 7455.102, 2617.534), (15.188938275923286, 6.763374089247169, 13.168419855113445), (2.25, 1.5, 1.0), "PWM_Quarry_2x2x2_A31_2", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (8397.194, 7185.881, 2551.0496), (3.378805293203006, -106.20946314475556, 166.7858331506227), (1.5, 2.4375, 1.5), "PWM_Quarry_2x2x2_A32_12", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (9722.319, 9077.292, 1310.0), (0.0, -79.99993888328352, 0.0), (2.25, 1.4375, 0.4375), "PWM_Quarry_2x2x2_A33_15", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (8452.88, 7159.197, 2155.2705), (13.347498197222833, -111.65730439488757, -8.519957809773652), (1.5199337, 2.0150352, 1.3395951), "PWM_Quarry_2x2x2_A34_34", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5785.0, 6255.0, 3405.0), (0.0, -30.000063894566395, 0.0), (1.8125, 1.0, 1.0), "PWM_Quarry_2x2x2_A35_40", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (8158.6045, 7326.0415, 1205.0), (-2.968017381449435, 69.61518813450377, 6.416011903846221), (3.25, 1.5625, 1.0625), "PWM_Quarry_2x2x2_A36_49", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (8624.662, 6887.987, 1250.0), (0.0, 74.99999173733916, -0.0), (1.0, 1.0, 1.0), "PWM_Quarry_2x2x2_A37_58", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (8779.597, 7197.8457, 1249.8491), (4.147080095533637e-13, 71.75170288226566, 179.99995901886442), (1.8125, 1.0, 1.0), "PWM_Quarry_2x2x2_A38_64", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (8599.093, 7132.219, 1858.943), (-4.0939941755907, 54.89732545850742, 2.8727824228348524), (1.0, 1.0, 1.3125), "PWM_Quarry_2x2x2_A39_70", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (10140.3545, 8886.512, 1070.523), (0.0, 118.26585806786329, -0.0), (1.536306, 1.536306, 1.536306), "PWM_Quarry_2x2x2_A4", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (8560.838, 7323.823, 1380.0), (-14.693113511833172, -177.68257727609677, -10.302307988013624), (2.0, 1.75, 1.8125), "PWM_Quarry_2x2x2_A40_83", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (8064.6934, 9744.499, 1357.978), (-11.186767127746068, 120.59252520850204, -6.3376457996001045), (2.0, 1.75, 1.8125), "PWM_Quarry_2x2x2_A41", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (10290.0, 8240.0, 1995.0), (90.0, 2.246916062620548e-06, 2.246917214104561e-06), (2.125, 1.0, 1.0), "PWM_Quarry_2x2x2_A42_57", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (10560.0, 8230.0, 1995.0), (90.0, -18.423059226779316, -198.4233967001805), (2.125, 1.0, 1.847789), "PWM_Quarry_2x2x2_A43", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (10316.346, 8256.911, 2096.275), (-87.91033689187556, -17.119177637145945, 36.64333979980753), (2.125, 1.0, 0.9195845), "PWM_Quarry_2x2x2_A44", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (9699.234, 8010.7114, 1300.0), (-3.0517572900205292e-05, -111.99633656974856, 179.9999795094279), (2.25, 1.4375, 0.4375), "PWM_Quarry_2x2x2_A45", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (9651.397, 9469.5205, 1300.001), (-3.0517574588764266e-05, -84.9999268801011, 179.99997950942796), (2.25, 1.4375, 0.4375), "PWM_Quarry_2x2x2_A46", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (7666.5317, 9627.289, 1220.0), (0.0, -34.999966730845806, 0.0), (2.0625, 1.625, 0.625), "PWM_Quarry_2x2x2_A47_139", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (8335.0, 9440.0, 1185.0), (0.0, -34.999966730845806, 0.0), (1.5625, 1.375, 1.0), "PWM_Quarry_2x2x2_A48_145", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (10040.0, 8275.0, 2985.0), (0.0, 0.0, 90.00001925454748), (0.75, 2.4375, 1.375), "PWM_Quarry_2x2x2_A49_26", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (10637.818, 8387.462, 869.55176), (0.0, -1.6561890276981446, 0.0), (1.536306, 1.536306, 1.536306), "PWM_Quarry_2x2x2_A5", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (10128.746, 8172.8438, 2530.6812), (0.5072716142579069, -0.00015260312748544198, 90.00002317454091), (0.375, 2.4375, 1.375), "PWM_Quarry_2x2x2_A51", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5999.228, 11006.435, 3460.3774), (6.832066324170938, -178.68585607339682, -176.067053493807), (3.04956, 3.113122, 1.819138), "PWM_Quarry_2x2x2_A52_157", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (10222.892, 8920.643, 1872.1547), (-0.018920889631041635, 0.43506924783848316, -85.01946588433113), (0.625, 2.4375, 1.375), "PWM_Quarry_2x2x2_A53", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (10165.566, 8956.006, 2909.4648), (-0.018829357717275695, 0.43507036024185797, 84.98055937141258), (1.0625, 2.6875, 1.125), "PWM_Quarry_2x2x2_A54", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (10217.0625, 8763.108, 3004.4565), (-0.01882931781018211, 0.43507113273662135, -90.01785466937808), (1.0625, 2.6875, 1.125), "PWM_Quarry_2x2x2_A55", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (10065.0, 7985.0, 2765.0), (0.0, 0.0, 90.00001925454748), (0.75, 2.4375, 1.375), "PWM_Quarry_2x2x2_A56", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (9885.186, 7849.571, 1445.0), (-1.0713319759718095e-08, -79.99005329284536, -2.9130554128365422), (1.8125, 1.8125, 1.972959), "PWM_Quarry_2x2x2_A57_35", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (9862.701, 9457.098, 1410.0), (0.0, 105.00001874691905, -0.0), (1.875, 1.875, 1.8125), "PWM_Quarry_2x2x2_A58_41", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (6314.961, 6679.434, 6028.364), (0.0, 14.06290580379622, -0.0), (8.256498, 3.6897144, 4.889753), "PWM_Quarry_2x2x2_A59_17", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (10486.108, 9003.814, 833.3291), (0.0, -55.127502393326616, 0.0), (1.536306, 1.536306, 1.536306), "PWM_Quarry_2x2x2_A6", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (7602.207, 10417.297, 5920.946), (0.0, 123.41984127811858, -0.0), (8.259366, 5.4752655, 4.915552), "PWM_Quarry_2x2x2_A60_20", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4724.011, 6226.416, 3698.863), (0.0, 0.0, -0.0), (1.092222, 1.092222, 1.4970008), "PWM_Quarry_2x2x2_A61_2", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4567.2334, 6556.573, 3584.1038), (0.0, -27.746368001964367, 0.0), (2.3604069, 1.0, 1.5668986), "PWM_Quarry_2x2x2_A62_5", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5487.284, 5960.7695, 3538.6316), (0.0, 0.0, -0.0), (1.0, 1.0, 1.0), "PWM_Quarry_2x2x2_A63_8", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1837.9683, 8353.954, 850.0004), (0.0, -23.92837542052254, 0.0), (1.283643, 1.283643, 1.283643), "PWM_Quarry_2x2x2_A64", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1464.0143, 8046.2188, 960.45776), (0.0, -96.96749497488624, 0.0), (1.283643, 1.450233, 1.283643), "PWM_Quarry_2x2x2_A65_31", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2294.6626, 8350.4, 1042.079), (4.416126636605138, 16.061305396849257, 5.2675923444667845), (1.0, 1.0, 1.0), "PWM_Quarry_2x2x2_A66", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (12062.473, 8428.621, 809.48145), (0.0, -9.201110871142815, 0.0), (1.188202, 1.4961385, 1.188202), "PWM_Quarry_2x2x2_A67", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (10295.269, 8429.998, 2457.5522), (85.3498277557493, 0.0, -0.0), (1.556057, 1.0, 1.0), "PWM_Quarry_2x2x2_A68", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (6630.4087, 10899.664, 3794.5864), (-0.24935906836086566, 165.18309357647632, 176.73572374003743), (3.04956, 3.113122, 1.819138), "PWM_Quarry_2x2x2_A69", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2633.208, 8302.777, 1070.523), (0.0, -63.100465556491514, 0.0), (1.536306, 1.536306, 1.536306), "PWM_Quarry_2x2x2_A7", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (8424.694, 7142.5425, 1414.6698), (3.378806755743242, -70.836549146632, 166.7858345603916), (1.830478, 2.767978, 2.0296707), "PWM_Quarry_2x2x2_A70", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2298.8242, 8166.37, 833.3291), (0.0, 123.17043434910288, -0.0), (1.536306, 1.536306, 1.536306), "PWM_Quarry_2x2x2_A9", _folder)
if a: placed += 1
else: skipped += 1

# Batch 54: StaticMesh'PWM_Quarry_2x2x5_A' (44 instances)
_mesh_path = "/Game/Unshippable/Whitebox/Rocks/Meshes/PWM_Quarry_2x2x5_A"
_materials = ['/Game/Environments/ProcTexturing/ProcMaterial_Quarry_Atlas_2']
_folder = "Reconstruction/BD_BB_Chapter5_BoneHoard/Meshes"
a = spawn_static_mesh(_mesh_path, _materials, (8885.064, 6108.709, 3552.1921), (-55.327783165664385, 127.30816893696014, -83.47432357333528), (2.278323, 2.278323, 2.278323), "PWM_Quarry_2x2x5_A_11", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4138.4004, 7688.6133, 3540.4773), (-61.1944757125771, -153.68172761851014, 84.21689384400482), (3.516942, 3.516942, 4.09755), "PWM_Quarry_2x2x5_A10", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5112.704, 6404.6523, 3679.5818), (-56.8487571769733, -125.54541466642046, 87.31056696540934), (3.7468538, 3.7468538, 4.09755), "PWM_Quarry_2x2x5_A11", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (6984.632, 6032.1094, 3529.582), (-62.36405941468457, -89.55535100748172, 96.24782898061332), (3.516942, 3.516942, 4.09755), "PWM_Quarry_2x2x5_A12", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (6562.4365, 11887.914, 3596.833), (-62.67702672765034, -103.6846147207357, -79.88244180827192), (3.516942, 3.516942, 4.09755), "PWM_Quarry_2x2x5_A13", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (6562.437, 11442.82, 3596.833), (-77.58039633867925, 120.33388227181543, 58.164193346031524), (3.516942, 3.516942, 4.09755), "PWM_Quarry_2x2x5_A14", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4762.665, 11702.604, 3441.3425), (-54.20183767336641, -68.17452712361931, -91.66203848064934), (3.516942, 3.516942, 4.09755), "PWM_Quarry_2x2x5_A15", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4948.5986, 11304.586, 3512.9128), (-87.94749131243171, 160.10990757769815, 43.760901349993674), (3.516942, 3.516942, 4.09755), "PWM_Quarry_2x2x5_A16", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3659.7275, 10487.979, 3577.7014), (-48.29257180722964, -40.38702548907744, -78.33648149860973), (3.516942, 3.516942, 4.09755), "PWM_Quarry_2x2x5_A17", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4052.3455, 10300.412, 3633.4531), (-83.56145809572988, -86.51153161557538, -31.448423089840958), (3.516942, 3.516942, 4.09755), "PWM_Quarry_2x2x5_A18", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3120.9473, 8561.636, 3643.5002), (-78.98259971414126, -85.68581988688591, -17.828942346779094), (6.138029, 6.138029, 6.718637), "PWM_Quarry_2x2x5_A19", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (9475.591, 6933.2754, 3552.9233), (-64.0793572644038, 147.63429931788895, -75.85003682850952), (2.278323, 2.278323, 2.9751675), "PWM_Quarry_2x2x5_A2", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3945.4775, 6487.1475, 3766.1968), (-82.78509768801463, -8.424706423901213, -59.32489440309619), (6.138029, 6.138029, 6.718637), "PWM_Quarry_2x2x5_A20", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5429.752, 5204.663, 3721.5623), (-75.16162029333243, -103.46143710060697, 75.50689356558055), (6.267865, 6.138029, 6.718637), "PWM_Quarry_2x2x5_A21", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (7927.3457, 5343.4863, 3663.246), (-82.78266277148242, 80.27111169098569, -59.32174983576054), (6.138029, 8.295904, 7.2564363), "PWM_Quarry_2x2x5_A22", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (9824.482, 8651.478, 3706.5945), (-86.2850831868698, 129.5432693037513, -28.412654180358402), (5.9591265, 5.040674, 5.621282), "PWM_Quarry_2x2x5_A23", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (8801.881, 10974.078, 3800.278), (-78.4344667277672, 159.76653486431886, -32.6256922721175), (5.8133187, 5.1925273, 5.773135), "PWM_Quarry_2x2x5_A24", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (7729.255, 11508.587, 3698.813), (-82.77975340535804, -147.85452824236538, -59.31865972971909), (6.906163, 6.138029, 6.718637), "PWM_Quarry_2x2x5_A25", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (10103.58, 8925.415, 1517.3682), (1.598858411628291, 107.81887150292168, 175.84770805267516), (1.416337, 1.416337, 1.416337), "PWM_Quarry_2x2x5_A26_4", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2738.041, 8913.03, 1679.7571), (-6.62936365774895, -101.28801844930967, -179.55919869578437), (1.416337, 1.416337, 1.416337), "PWM_Quarry_2x2x5_A27", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2721.5098, 8226.478, 1612.7388), (0.15663669119325935, -71.88505060735147, 179.29869910938004), (1.416337, 1.416337, 1.416337), "PWM_Quarry_2x2x5_A28_241", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2602.749, 8603.604, 1947.334), (88.31792817704326, -154.18764140966843, 119.99356210310124), (1.416337, 1.416337, 1.416337), "PWM_Quarry_2x2x5_A29_405", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (8435.646, 7071.1274, 3609.0754), (-61.19786830212795, -33.413816436423346, 84.2187675510829), (3.9094596, 3.7015188, 4.09755), "PWM_Quarry_2x2x5_A3", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1848.3984, 7973.064, 1125.7717), (0.21145975837842984, 87.16100933545053, -85.7452897458067), (1.4708575, 1.4708575, 1.4708575), "PWM_Quarry_2x2x5_A30_424", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2589.537, 9084.304, 1475.0679), (0.8162490131408229, 84.38963248507434, -179.7188759092686), (1.416337, 1.416337, 1.416337), "PWM_Quarry_2x2x5_A31", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (8404.727, 6371.602, 3732.2463), (-67.48168317798516, -54.20512364143397, 94.61799724494378), (4.4201736, 4.4201736, 5.199094), "PWM_Quarry_2x2x5_A32", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (9343.016, 8192.775, 3795.4375), (-67.48132409590137, -12.625667865969502, 94.61805576154333), (5.975397, 4.420174, 5.000781), "PWM_Quarry_2x2x5_A33", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (8638.963, 10419.818, 3684.957), (-55.121991377611536, 34.275979648610765, 100.83397177642856), (4.420174, 5.3336477, 5.000781), "PWM_Quarry_2x2x5_A34", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5504.6045, 6370.3955, 3900.0), (0.0, 45.00007048643773, -0.0), (2.375, 2.375, 2.375), "PWM_Quarry_2x2x5_A35_37", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3985.2207, 8075.546, 5204.5034), (-47.344778135585386, 177.75711100762376, 74.42470220469313), (6.138029, 6.138029, 3.6875), "PWM_Quarry_2x2x5_A36", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3731.8962, 10488.157, 3725.584), (-78.9840328074386, -100.27755848923891, -17.828722600645587), (3.516942, 3.516942, 4.09755), "PWM_Quarry_2x2x5_A37", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (6535.8774, 4811.622, 3607.9355), (-82.78201090806662, 80.27013331043938, -75.9932001504132), (6.138029, 8.295904, 7.256436), "PWM_Quarry_2x2x5_A38", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4585.12, 10601.863, 3701.1506), (-62.36677517496246, 131.3296410875247, 96.24775889415388), (3.516942, 3.516942, 4.09755), "PWM_Quarry_2x2x5_A39", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (8871.889, 8881.422, 3585.8274), (-62.368933007408216, 6.106669402204128, 96.24701131695778), (3.516942, 3.516942, 4.09755), "PWM_Quarry_2x2x5_A4", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (8620.401, 6111.236, 3650.8718), (-67.48168317798516, -54.20512364143397, 94.61799724494378), (4.420174, 4.420174, 5.199094), "PWM_Quarry_2x2x5_A40", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5240.818, 6580.915, 3944.2188), (-72.74408745354282, 47.46076115344726, -85.0359223134022), (3.746854, 3.746854, 4.09755), "PWM_Quarry_2x2x5_A41", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (8135.9297, 7287.016, 3969.6396), (-61.15487885367328, 136.45388459577887, -87.25970130138676), (3.90946, 3.701519, 4.09755), "PWM_Quarry_2x2x5_A42", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (8462.16, 7079.149, 2044.107), (0.07792230759344289, 95.46615010001521, -178.61984506346468), (2.1604366, 2.1604366, 2.1604366), "PWM_Quarry_2x2x5_A43_182", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (8535.055, 7206.203, 1936.1748), (0.07792202675320246, 135.44277817169896, -178.61984486599422), (2.5726275, 2.160437, 2.351489), "PWM_Quarry_2x2x5_A44_184", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (7936.4893, 10545.121, 3585.8276), (-62.36780694497912, 41.05022027985911, 96.24703192666962), (3.516942, 3.516942, 4.09755), "PWM_Quarry_2x2x5_A5", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (10345.98, 8196.155, 2220.6963), (-0.2989194412933195, 76.49765961188362, 176.31017907821519), (1.416337, 1.75, 1.416337), "PWM_Quarry_2x2x5_A6_24", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (6562.4365, 11070.202, 3552.8296), (-61.19564017176056, 91.80853173362551, 84.21749692523584), (3.516942, 3.516942, 4.09755), "PWM_Quarry_2x2x5_A7", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4831.9727, 10382.499, 3529.5815), (-62.36677517496246, 131.3296410875247, 96.24775889415388), (3.516942, 3.516942, 4.09755), "PWM_Quarry_2x2x5_A8", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4014.6462, 8544.321, 3288.4517), (-62.365150934072595, 166.27082788075325, 96.24802344800105), (3.516942, 3.516942, 4.09755), "PWM_Quarry_2x2x5_A9", _folder)
if a: placed += 1
else: skipped += 1

# Batch 55: StaticMesh'PWM_Quarry_3x3x2' (7 instances)
_mesh_path = "/Game/Unshippable/Whitebox/Rocks/Meshes/PWM_Quarry_3x3x2"
_materials = ['/Game/Environments/ProcTexturing/ProcMaterial_Quarry_Atlas_A']
_folder = "Reconstruction/BD_BB_Chapter5_BoneHoard/Meshes"
a = spawn_static_mesh(_mesh_path, _materials, (8329.53, 7418.525, 2709.954), (-1.7970580713268625, 64.99951241082415, -179.20678333413568), (3.220301, 3.220301, 3.220301), "PWM_Quarry_3x3x2_11", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (10274.116, 8602.1875, 1027.7139), (7.131032484150429, 86.88304786966883, 164.98181638167364), (1.644608, 1.644608, 1.644608), "PWM_Quarry_3x3x3_18", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (8414.998, 7294.83, 1397.2446), (-19.312561152239113, 43.13035401845171, 8.148505861345528), (2.1875, 2.125, 1.6875), "PWM_Quarry_3x3x4_25", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4883.6143, 9598.966, 5429.2227), (7.106087456580519, 47.09174929196194, -165.6191791587503), (4.364444, 4.364444, 4.364444), "PWM_Quarry_3x3x5", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (8229.62, 9722.639, 2829.8838), (5.95136824832715, -76.24706797730452, 152.91528483296523), (3.220301, 3.220301, 3.220301), "PWM_Quarry_3x3x6", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (8340.27, 9730.619, 1585.928), (-19.312561152239113, 43.13035401845171, 8.148505861345528), (2.1875, 2.125, 1.6875), "PWM_Quarry_3x3x7", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (8255.36, 9775.46, 1644.6617), (20.845389364243932, -74.52563272273186, -176.72063720638516), (2.25, 2.4375, 2.375), "PWM_Quarry_3x3x8", _folder)
if a: placed += 1
else: skipped += 1

# Batch 56: StaticMesh'PWM_Quarry_4x3x10_A' (3 instances)
_mesh_path = "/Game/Unshippable/Whitebox/Rocks/Meshes/PWM_Quarry_4x3x10_A"
_materials = ['/Game/Environments/ProcTexturing/ProcMaterial_Quarry_Atlas_A']
_folder = "Reconstruction/BD_BB_Chapter5_BoneHoard/Meshes"
a = spawn_static_mesh(_mesh_path, _materials, (10482.686, 9080.052, 2084.669), (-14.366639802065807, 36.46950113215593, -14.948088967040688), (1.9934751, 1.6034127, 0.9884635), "PWM_Quarry_4x3x10_C19", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (10645.986, 9022.187, 2271.848), (-1.4131774231816674, -123.69821299496294, -0.03918456360422679), (0.79995847, 1.1203285, 0.5198286), "PWM_Quarry_4x3x10_C22", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (10559.935, 8888.931, 2451.7505), (1.168856965380795, 88.9410911069582, -8.031524327863323), (0.799958, 1.120329, 0.519829), "PWM_Quarry_4x3x10_C23", _folder)
if a: placed += 1
else: skipped += 1

# Batch 57: StaticMesh'PWM_Quarry_4x3x10_B' (1 instances)
_mesh_path = "/Game/Unshippable/Whitebox/Rocks/Meshes/PWM_Quarry_4x3x10_B"
_materials = ['/Game/Environments/ProcTexturing/ProcMaterial_Quarry_Atlas_A']
_folder = "Reconstruction/BD_BB_Chapter5_BoneHoard/Meshes"
a = spawn_static_mesh(_mesh_path, _materials, (10349.086, 8324.935, 2647.0566), (23.920891996547944, -23.75109922707218, 47.413805853538136), (0.547323, 1.0, 1.0), "PWM_Quarry_4x3x10_B_7", _folder)
if a: placed += 1
else: skipped += 1

# Batch 58: StaticMesh'PWM_Quarry_4x3x10_C' (20 instances)
_mesh_path = "/Game/Unshippable/Whitebox/Rocks/Meshes/PWM_Quarry_4x3x10_C"
_materials = ['/Game/Environments/ProcTexturing/ProcMaterial_Quarry_Atlas_A']
_folder = "Reconstruction/BD_BB_Chapter5_BoneHoard/Meshes"
a = spawn_static_mesh(_mesh_path, _materials, (11065.523, 8141.9453, 1294.4868), (-1.9401548436213916, -46.79003423274906, 2.064440820137277), (1.0, 1.0, 1.0), "PWM_Quarry_4x3x10_C_35", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (10783.8125, 9589.398, 1024.0259), (1.7658778701073248, 53.01302568383417, -10.39425476990608), (0.752853, 0.752853, 0.752853), "PWM_Quarry_4x3x10_C10", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (10776.873, 9285.095, 927.3086), (-9.319213084435543, -84.12182158391828, -0.39590491236826536), (0.752853, 0.7939231, 0.611361), "PWM_Quarry_4x3x10_C11", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (10768.502, 9373.721, 942.05615), (-2.6867067316488353, -13.166015202840708, -8.935516852497258), (0.752853, 0.752853, 0.611361), "PWM_Quarry_4x3x10_C12", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5568.0195, 7744.5566, 1471.8586), (-52.08100741341931, 145.98342198875915, -7.261898001613712), (0.7463646, 0.7463646, 0.2980433), "PWM_Quarry_4x3x10_C13_243", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (8449.662, 7282.511, 1607.8934), (0.8672564333853267, -175.07568667269032, -9.96289083155224), (1.3125, 1.0, 0.25), "PWM_Quarry_4x3x10_C14_28", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (8249.662, 9732.512, 2207.8936), (-6.1993409963440405, 135.14298578311258, -9.967071965883658), (1.5625, 1.25, 0.5), "PWM_Quarry_4x3x10_C15", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (10793.579, 8110.9316, 2216.0825), (-5.552459100687671, 126.75558793551254, 172.88706350123772), (1.11083, 1.11083, 0.786485), "PWM_Quarry_4x3x10_C16", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (9965.523, 8941.945, 1494.4868), (-1.9401546945228472, 8.209960019471561, 2.0644410930786603), (1.0, 1.875, 0.9375), "PWM_Quarry_4x3x10_C17", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (10776.873, 9035.095, 1117.3086), (0.629169012220214, -84.19928133811567, 0.6231609065236108), (0.875, 0.92998356, 0.611361), "PWM_Quarry_4x3x10_C18", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (11305.709, 8071.426, 1992.125), (1.8960398877025946, 179.32013258859863, 174.64715368118942), (1.0, 1.0, 1.0), "PWM_Quarry_4x3x10_C2", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (10655.713, 9419.319, 1017.4611), (1.7658778701073248, 53.01302568383417, -10.39425476990608), (1.0589765, 0.752853, 0.752853), "PWM_Quarry_4x3x10_C20", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (10701.735, 9231.175, 986.1614), (1.335916382282901, 123.79457794372495, -1.785797095598908), (1.058977, 0.752853, 0.752853), "PWM_Quarry_4x3x10_C21", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (10407.755, 9004.263, 2417.4766), (4.636665820132005, 110.92569445213292, 178.15989459625172), (0.752853, 0.752853, 0.752853), "PWM_Quarry_4x3x10_C3_10", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (10884.743, 8086.537, 1610.1885), (-6.30786063274536, 24.768362388200167, 2.580564738646237), (1.875, 1.7146211, 0.786485), "PWM_Quarry_4x3x10_C4", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (10993.579, 8210.932, 2216.0825), (-5.552459100687671, 126.75558793551254, 172.88706350123772), (1.11083, 1.11083, 0.786485), "PWM_Quarry_4x3x10_C5", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (10349.45, 8144.964, 1467.3364), (0.8606930194446686, -6.934814970591125, 2.4390863081485303), (0.878285, 0.878285, 0.794637), "PWM_Quarry_4x3x10_C6", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (10706.144, 8228.146, 867.4551), (0.5861739334451015, -154.42066037588495, -2.51895114307859), (0.878285, 0.878285, 0.653523), "PWM_Quarry_4x3x10_C7", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (11382.846, 8429.842, 2372.54), (-19.184504274590765, 130.15756975525915, 168.24023824572532), (1.11083, 1.11083, 0.786485), "PWM_Quarry_4x3x10_C8_55", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (11719.721, 8447.408, 2328.919), (12.42530114242096, -137.2582627878779, 170.84246113017403), (1.11083, 1.11083, 0.786485), "PWM_Quarry_4x3x10_C9_68", _folder)
if a: placed += 1
else: skipped += 1

# Batch 59: StaticMesh'PWM_Quarry_4x4x4_A' (4 instances)
_mesh_path = "/Game/Unshippable/Whitebox/Rocks/Meshes/PWM_Quarry_4x4x4_A"
_materials = ['/Game/Environments/ProcTexturing/ProcMaterial_Quarry_Atlas_2']
_folder = "Reconstruction/BD_BB_Chapter5_BoneHoard/Meshes"
a = spawn_static_mesh(_mesh_path, _materials, (10312.56, 8530.119, 2436.8438), (-0.006988533706395544, -84.48457829401428, 3.408571664753265), (0.5415359, 0.5415359, 0.5415359), "PWM_Quarry_4x4x4_A_55", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (10423.415, 8348.845, 2351.6528), (-3.9048768571542807, -84.71722410650028, 1.0982324702714886e-06), (0.541536, 0.541536, 0.541536), "PWM_Quarry_4x4x4_A2", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (10591.382, 8364.376, 2351.6536), (-3.9048768421915647, -84.7172240949359, 7.738979732387218e-07), (0.541536, 0.8403254, 0.541536), "PWM_Quarry_4x4x4_A3", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (10418.691, 8498.804, 2401.2378), (-3.9048464661394013, -84.71715939411578, 3.416514361864785), (0.9868368, 0.8671128, 0.541536), "PWM_Quarry_4x4x4_A4", _folder)
if a: placed += 1
else: skipped += 1

# Batch 60: StaticMesh'PWM_Quarry_4x5x10' (8 instances)
_mesh_path = "/Game/Unshippable/Whitebox/Rocks/Meshes/PWM_Quarry_4x5x10"
_materials = ['/Game/Environments/ProcTexturing/ProcMaterial_Quarry_Atlas_A']
_folder = "Reconstruction/BD_BB_Chapter5_BoneHoard/Meshes"
a = spawn_static_mesh(_mesh_path, _materials, (8378.418, 7161.0503, 2372.0105), (78.07778698723314, 145.8758754720261, 90.4453547360927), (1.0, 1.0, 0.5625), "PWM_Quarry_4x5x10_15", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (8549.029, 7280.6562, 2026.9672), (76.98688902526425, 80.3238415306806, -58.45302070069413), (0.5625, 0.5, 0.375), "PWM_Quarry_4x5x11_46", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (8448.811, 7244.067, 1744.1537), (-79.99616464069504, -90.0005734609608, 54.99795159345775), (0.8445814, 1.1875, 0.375), "PWM_Quarry_4x5x12_67", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (8278.418, 9711.051, 2372.0105), (78.07775833302325, -154.1241494484107, 90.4453284611657), (1.0, 1.0, 0.5625), "PWM_Quarry_4x5x13", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (8225.963, 9702.376, 1378.5985), (-76.79392775948891, -57.98241328573412, 93.3719501937701), (0.8125, 1.625, 0.8125), "PWM_Quarry_4x5x15", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (8138.674, 9448.088, 1241.5818), (78.07704743228794, 145.8750229767199, 105.44503378900879), (0.6875, 1.5, 0.5625), "PWM_Quarry_4x5x16", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (9790.0, 8340.0, 1200.0), (0.0, 0.0, -89.99945205658098), (1.0, 0.75, 1.0), "PWM_Quarry_4x5x17_18", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (8232.878, 9688.962, 2611.7253), (78.07775833302325, -154.1241494484107, 90.4453284611657), (1.0, 1.0, 0.5625), "PWM_Quarry_4x5x18", _folder)
if a: placed += 1
else: skipped += 1

# Batch 61: StaticMesh'PWM_Quarry_5x4x10' (3 instances)
_mesh_path = "/Game/Unshippable/Whitebox/Rocks/Meshes/PWM_Quarry_5x4x10"
_materials = ['/Game/Environments/ProcTexturing/ProcMaterial_Quarry_Atlas_A']
_folder = "Reconstruction/BD_BB_Chapter5_BoneHoard/Meshes"
a = spawn_static_mesh(_mesh_path, _materials, (9880.0, 9205.0, 1485.0), (0.0, 0.0, -90.00009542133918), (1.0, 1.0, 0.625), "PWM_Quarry_5x4x10_38", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (10414.46, 8914.367, 2009.3319), (4.980935415311644, 5.0189951605941605, -9.563200030999981), (1.1476138, 1.0, 1.0), "PWM_Quarry_5x4x12_60", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (7764.072, 9924.512, 1240.0), (0.0, -34.999966730845806, 0.0), (1.375, 1.3125, 0.125), "PWM_Quarry_5x4x13_136", _folder)
if a: placed += 1
else: skipped += 1

# Batch 62: StaticMesh'PWM_Quarry_8x8x8_A' (45 instances)
_mesh_path = "/Game/Unshippable/Whitebox/Rocks/Meshes/PWM_Quarry_8x8x8_A"
_materials = ['/Game/Environments/ProcTexturing/ProcMaterial_Quarry_Atlas_2']
_folder = "Reconstruction/BD_BB_Chapter5_BoneHoard/Meshes"
a = spawn_static_mesh(_mesh_path, _materials, (10528.979, 7768.217, 1425.541), (0.0, 167.86022817436265, -0.0), (1.0, 1.0, 1.0), "PWM_Quarry_8x8x8_A_28", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (10615.121, 9464.875, 673.2197), (-85.04712176812176, -21.984410815185406, -145.02824365331904), (0.846199, 0.846199, 0.846199), "PWM_Quarry_8x8x8_A10", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (10617.555, 9506.129, 2405.588), (-88.01001386399152, 104.59994334293623, 94.58289882861949), (1.1247767, 1.0, 1.0), "PWM_Quarry_8x8x8_A11", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (10756.337, 9568.344, 2488.4062), (-75.07859341717437, 138.52747972259974, 48.428872017909136), (1.1492082, 1.220488, 1.158921), "PWM_Quarry_8x8x8_A12", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (11974.433, 10215.126, 2287.3145), (-89.73647242814404, -41.77432721676479, -138.9524214155831), (0.48661315, 0.673937, 0.673937), "PWM_Quarry_8x8x8_A13_212", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (9973.4795, 8045.0312, 1587.1927), (-85.81004782626644, 156.83537401117465, 113.53995342333444), (0.625123, 0.292381, 0.5), "PWM_Quarry_8x8x8_A14", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (10424.834, 8817.454, 2609.4548), (-85.80999267111419, 156.83609571066836, 102.4705448895005), (0.625123, 0.4211877, 0.755362), "PWM_Quarry_8x8x8_A15", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (10534.707, 8802.623, 2765.1543), (-85.8081283202734, -150.53119028702034, -116.20831117723746), (0.625123, 0.639094, 0.755362), "PWM_Quarry_8x8x8_A16", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (11879.127, 9491.463, 2787.0469), (-1.6401368599651676, 1.9090650340831326, -89.67474292574013), (1.0378829, 1.0746634, 1.0843035), "PWM_Quarry_8x8x8_A17", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (11967.159, 8751.475, 2396.213), (-89.67707002604692, -41.38523657879376, 68.86461478645501), (0.436648, 0.673937, 0.673937), "PWM_Quarry_8x8x8_A18", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2000.458, 9958.378, 1893.2803), (1.0559739121028504, -157.93075654286167, 93.41956141041632), (1.0, 0.73422545, 1.0388294), "PWM_Quarry_8x8x8_A19_267", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (11037.272, 7798.6514, 852.01953), (0.0, 179.06036011557003, -0.0), (1.0, 1.0, 1.0), "PWM_Quarry_8x8x8_A2", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2348.663, 9176.574, 2067.9644), (-82.73122259144452, -120.71496248289296, -75.49272056619327), (0.628471, 0.575755, 0.880359), "PWM_Quarry_8x8x8_A20_275", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2039.5479, 9598.589, 479.9956), (8.877230632845968, -133.09805199417235, -1.1750490836343583), (1.0, 1.0, 1.0), "PWM_Quarry_8x8x8_A21_279", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1258.7988, 10079.543, 2363.814), (83.62295186815938, 57.84776525496985, -70.89686791140632), (1.0887352, 0.76515836, 1.0), "PWM_Quarry_8x8x8_A22_291", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1892.9277, 8038.783, 725.4326), (0.0, 118.18797770127452, -0.0), (0.832839, 0.832839, 0.832839), "PWM_Quarry_8x8x8_A23_353", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1613.1289, 8060.6797, 2160.8335), (86.06264857505441, -4.474673638099741, 3.6677681871823515), (0.681959, 0.832839, 0.91217417), "PWM_Quarry_8x8x8_A24", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1635.8213, 8221.514, 2293.495), (86.06150628418949, -4.473987860780244, -4.404590435423443), (0.681959, 0.832839, 0.772209), "PWM_Quarry_8x8x8_A25", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2464.0234, 8060.62, 2209.8574), (86.05868174050354, -4.472722703542212, -26.09863498463325), (0.681959, 0.714527, 0.772209), "PWM_Quarry_8x8x8_A26", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2696.7607, 8575.447, 2160.8032), (-89.2257154956353, 80.68732958747471, -175.84070679688992), (0.625123, 0.292381, 0.625123), "PWM_Quarry_8x8x8_A27", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2405.9307, 8578.523, 2087.8208), (-83.15933087033116, 1.3020644176138028, 93.15790382261567), (0.305588, 0.584875, 0.625123), "PWM_Quarry_8x8x8_A28_401", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2176.404, 9732.051, 1875.3557), (-3.399598440214002, -158.19725372843578, 93.42498631758163), (1.0, 0.734225, 1.038829), "PWM_Quarry_8x8x8_A29", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (11903.603, 8405.434, 2506.9766), (-80.35713862828204, -80.3733200269172, 86.72551416094214), (1.0, 1.0, 1.0), "PWM_Quarry_8x8x8_A3_59", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (10130.017, 8500.0, 1565.846), (0.0, 9.233108859296879, -0.0), (0.6190536, 0.75, 0.625), "PWM_Quarry_8x8x8_A30_45", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (10820.0, 8290.0, 1195.0), (0.0, -0.777648911942651, 0.0), (1.3472618, 0.75, 1.3125), "PWM_Quarry_8x8x8_A31", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (10274.619, 8814.341, 1280.0), (0.0, -169.9999147551563, 0.0), (0.875, 0.9375, 1.0625), "PWM_Quarry_8x8x8_A32", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (10286.337, 8533.344, 1348.4062), (-88.87503337148891, 179.578635962871, 6.402210661761743), (1.0493015, 1.375, 1.1022824), "PWM_Quarry_8x8x8_A33", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (11365.788, 8007.412, 2271.021), (-79.5108350108886, 69.50736491119318, 118.74054167021924), (1.2665867, 1.0, 1.0869199), "PWM_Quarry_8x8x8_A34", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (10755.121, 8739.875, 628.2197), (-85.0457750327483, 153.0152823455989, -145.02745142819663), (0.846199, 0.846199, 0.9343383), "PWM_Quarry_8x8x8_A35", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (9892.368, 7629.9536, 1235.0), (0.0, 10.000068840793773, -0.0), (0.5625, 0.75, 0.3125), "PWM_Quarry_8x8x8_A36", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2098.1865, 7991.523, 2199.4417), (86.06264782006328, -4.474679112009318, 3.667761878632484), (0.681959, 0.832839, 0.912174), "PWM_Quarry_8x8x8_A37", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2424.3167, 7937.833, 2176.7751), (86.06296090790065, -4.474812632995993, -6.423267183644489), (0.681959, 0.832839, 0.912174), "PWM_Quarry_8x8x8_A38", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (12363.199, 10210.299, 2315.9167), (-89.73435251804966, -41.772609977207594, -138.95106891082253), (0.486613, 0.673937, 0.673937), "PWM_Quarry_8x8x8_A39", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (11532.257, 10455.177, 2391.3672), (-89.75612538281796, -41.81732438764755, -123.2601795306986), (1.0, 1.080504, 1.0), "PWM_Quarry_8x8x8_A4_130", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (12242.113, 10212.096, 2404.161), (-89.73409937340057, -41.772349890198974, -138.95114859787833), (0.486613, 0.673937, 0.673937), "PWM_Quarry_8x8x8_A40", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (12377.928, 9895.831, 2470.4573), (-82.3118857247272, -179.42630407075387, -1.3073421593690226), (0.486613, 0.673937, 0.673937), "PWM_Quarry_8x8x8_A41", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (12377.29, 9448.607, 2508.7495), (-82.3118857247272, -179.42630407075387, -1.3073421593690226), (0.486613, 1.2146324, 0.673937), "PWM_Quarry_8x8x8_A42", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (12604.506, 8484.023, 2513.7268), (-80.35713862828204, -80.3733200269172, 86.72551416094214), (1.0, 1.0, 1.0), "PWM_Quarry_8x8x8_A43", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (11126.903, 7891.4756, 1787.5331), (3.8176586455731094, 10.550916495864639, 80.85225073074538), (1.266587, 1.0, 1.08692), "PWM_Quarry_8x8x8_A44", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (12088.063, 8189.3247, 2177.0088), (80.99797319246163, -72.13651358081567, -72.0134579407876), (0.8930311, 0.70301795, 1.08692), "PWM_Quarry_8x8x8_A45", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (11087.948, 9997.988, 2512.7222), (-89.68694365282728, -41.89023068021357, -76.01994704440291), (1.1398462, 1.078017, 1.0), "PWM_Quarry_8x8x8_A5_132", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2592.5723, 7904.1475, 747.2471), (0.0, -15.438507318885927, 0.0), (1.0, 1.0, 1.0), "PWM_Quarry_8x8x8_A6", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1641.9893, 9680.0, 2245.5469), (-7.306153117781813, -99.92450427192385, 96.19538992756), (1.0, 0.7578163, 1.0), "PWM_Quarry_8x8x8_A7_265", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (10303.511, 9264.365, 850.0), (-87.46339052737507, -62.93110894151892, -84.46165419727781), (0.846199, 0.846199, 0.846199), "PWM_Quarry_8x8x8_A8", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2210.7344, 9131.029, 553.70605), (2.3240877025642694, -112.64225747183293, -173.49019618097512), (0.696178, 0.696178, 0.696178), "PWM_Quarry_8x8x8_A9_298", _folder)
if a: placed += 1
else: skipped += 1

# Batch 63: StaticMesh'PWM_Quarry_Ceilling_Fissure_8x4_B' (10 instances)
_mesh_path = "/Game/Unshippable/Whitebox/Rocks/Meshes/PWM_Quarry_Ceilling_Fissure_8x4_B"
_materials = ['/Game/Environments/ProcTexturing/ProcMaterial_Quarry_Ceilling_Fissure_8x8']
_folder = "Reconstruction/BD_BB_Chapter5_BoneHoard/Meshes"
a = spawn_static_mesh(_mesh_path, _materials, (11408.762, 8444.365, 840.8291), (-0.24087524639766186, -8.71301375952307, 9.98412242461237), (1.0, 1.0, 0.749248), "PWM_Quarry_Ceilling_Fissure_8x4_B_48", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (374.73624, 10034.208, 779.1073), (0.0, 75.93742851124716, -0.0), (0.712558, 0.862571, 0.5), "PWM_Quarry_Ceilling_Fissure_8x4_B10", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (11933.789, 8579.13, 789.70703), (0.21278094343436224, 20.726247431126012, 8.605484942402784), (0.736647, 0.736647, 0.690629), "PWM_Quarry_Ceilling_Fissure_8x4_B2", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (11032.568, 9361.767, 833.9634), (2.493797705984601, -132.88043860733075, 10.093895520869056), (1.0, 1.0, 0.749248), "PWM_Quarry_Ceilling_Fissure_8x4_B3", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (11733.315, 10189.859, 870.53937), (-2.4981688863272726, -132.4907381735139, 16.2874423510329), (1.0, 1.1552453, 0.749248), "PWM_Quarry_Ceilling_Fissure_8x4_B4", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1141.2021, 10099.922, 850.0), (1.5182966519548022, 154.76536625090887, 10.218800403746426), (1.0, 1.0, 1.0), "PWM_Quarry_Ceilling_Fissure_8x4_B5_339", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1659.3724, 9395.872, 815.6655), (-0.1759947707743247, 131.31802980066587, 13.778686457589616), (0.862571, 0.862571, 0.862571), "PWM_Quarry_Ceilling_Fissure_8x4_B6", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (890.235, 8543.38, 812.32874), (-2.0624696515152667, 3.6566847896264982, 12.55429670063503), (0.712558, 0.862571, 0.862571), "PWM_Quarry_Ceilling_Fissure_8x4_B7", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1459.5817, 8421.331, 799.8767), (-1.021636823876987, -37.47792760992621, 6.416131135345737), (0.612731, 0.612731, 0.612731), "PWM_Quarry_Ceilling_Fissure_8x4_B8_364", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (253.23956, 8873.159, 780.1073), (0.0, -73.12484241255481, 0.0), (0.712558, 0.862571, 0.5), "PWM_Quarry_Ceilling_Fissure_8x4_B9", _folder)
if a: placed += 1
else: skipped += 1

# Batch 64: StaticMesh'PWM_Quarry_Floor_2x2x2_A' (2 instances)
_mesh_path = "/Game/Unshippable/Whitebox/Rocks/Meshes/PWM_Quarry_Floor_2x2x2_A"
_materials = ['/Game/Environments/ProcTexturing/ProcMaterial_Quarry_Atlas_3']
_folder = "Reconstruction/BD_BB_Chapter5_BoneHoard/Meshes"
a = spawn_static_mesh(_mesh_path, _materials, (2426.0625, 8570.046, 1035.2751), (-1.6117553500097572, -23.094269545141522, 1.2062088285408062e-06), (1.0, 1.6404344, 1.0), "PWM_Quarry_Floor_2x2x2_A_23", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2119.8005, 8428.686, 971.839), (-1.6054827402530399e-09, 2.7067451690009685, 4.436017564695103), (1.085175, 1.0, 1.0), "PWM_Quarry_Floor_2x2x2_A2_34", _folder)
if a: placed += 1
else: skipped += 1

# Batch 65: StaticMesh'PWM_Quarry_RockDebris_A' (103 instances)
_mesh_path = "/Game/Unshippable/Whitebox/Rocks/Meshes/PWM_Quarry_RockDebris_A"
_materials = ['/Game/Environments/ProcTexturing/ProcMaterial_Quarry_Atlas_5']
_folder = "Reconstruction/BD_BB_Chapter5_BoneHoard/Meshes"
a = spawn_static_mesh(_mesh_path, _materials, (11515.958, 8611.131, 846.16016), (0.0, 58.349391129641155, -0.0), (1.0, 1.0, 1.0), "PWM_Quarry_RockDebris_A_72", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (11373.229, 9319.697, 794.2345), (0.0, -142.3865474755917, 0.0), (1.520606, 1.520606, 1.520606), "PWM_Quarry_RockDebris_A10", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (7792.3457, 8175.051, 1273.3301), (16.32540848421372, 161.96304185157265, -6.657471193836761), (1.277792, 1.277792, 3.2176309), "PWM_Quarry_RockDebris_A100", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (7601.129, 8007.0303, 1368.2964), (-26.58178551034621, -26.257260938994122, 1.7136093176808571), (1.277792, 1.277792, 3.9818952), "PWM_Quarry_RockDebris_A101", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (7090.1567, 7013.568, 1256.5879), (1.6668664527633628, 34.33117643464807, -0.41235350092041945), (1.406845, 1.333108, 1.582016), "PWM_Quarry_RockDebris_A102_315", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (6922.875, 7406.4077, 1261.3223), (2.3852246448076535, 130.10759099495843, 2.8726774831512207), (1.406845, 1.333108, 1.582016), "PWM_Quarry_RockDebris_A103", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (6143.573, 7325.4805, 1257.958), (-8.407470610121347, -76.80168994082568, 2.237704309219747), (1.406845, 1.333108, 1.582016), "PWM_Quarry_RockDebris_A104", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5891.494, 9797.749, 1267.5078), (-0.3288573335615886, 19.751678159786337, 8.259824106921192), (1.433339, 1.214637, 2.511202), "PWM_Quarry_RockDebris_A107", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (7560.1797, 8330.366, 1359.5806), (-23.61434845259493, -29.855805187245497, 30.72461504312225), (1.279855, 0.953407, 1.982041), "PWM_Quarry_RockDebris_A109", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (11460.713, 9539.977, 794.2344), (0.0, -120.95864257681083, 0.0), (1.090704, 1.090704, 1.090704), "PWM_Quarry_RockDebris_A11", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (7455.878, 9460.487, 1257.3081), (-1.2945862061617925, -58.75836181657897, 1.9506914657868473), (1.279855, 1.1367606, 1.982041), "PWM_Quarry_RockDebris_A110", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (7987.4487, 8904.995, 1242.9404), (-1.4515990862433548, -102.56255697953638, 0.35651901983479717), (1.279855, 1.136761, 1.982041), "PWM_Quarry_RockDebris_A111", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5802.544, 7798.429, 1509.376), (13.173782889409654, 51.417302637509074, -5.325927263313282), (1.231679, 0.843268, 2.68607), "PWM_Quarry_RockDebris_A114", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (6281.617, 8225.64, 1621.294), (12.872371636831703, 16.409331339957266, -21.575621874349178), (1.231679, 1.0795211, 2.68607), "PWM_Quarry_RockDebris_A115", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5227.774, 8230.367, 1265.3257), (14.825756342000608, 25.226073493420444, 14.576793062555538), (1.086923, 0.839221, 2.041694), "PWM_Quarry_RockDebris_A118", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5530.51, 9449.559, 1294.6313), (13.277688315805207, -26.030941222533208, 1.700133612535689), (1.3381197, 1.3381197, 1.5820986), "PWM_Quarry_RockDebris_A119", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (11174.51, 9189.132, 796.1963), (0.0, -151.56915487373422, 0.0), (1.090704, 1.090704, 1.090704), "PWM_Quarry_RockDebris_A12", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (6469.527, 7544.526, 1267.4272), (0.556526693247979, -168.96814430854755, 6.990374493575909), (1.406845, 1.333108, 1.582016), "PWM_Quarry_RockDebris_A121", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (6873.681, 7359.183, 1262.3291), (-0.7869262389274642, -169.03504182023997, 0.5979490146253722), (1.098572, 1.024835, 0.83241224), "PWM_Quarry_RockDebris_A122", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (11905.051, 9948.148, 794.7251), (0.0, -151.56915487373422, 0.0), (1.090704, 1.090704, 1.090704), "PWM_Quarry_RockDebris_A13", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (12165.98, 10258.598, 795.99805), (0.0, -142.3865474755917, 0.0), (1.520606, 1.520606, 1.520606), "PWM_Quarry_RockDebris_A14", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (11780.555, 9843.949, 795.99805), (0.0, -179.1776790196837, 0.0), (1.520606, 1.520606, 1.520606), "PWM_Quarry_RockDebris_A15", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (10854.607, 9014.881, 841.1343), (0.0, -138.1195329792319, 0.0), (1.520606, 1.520606, 1.520606), "PWM_Quarry_RockDebris_A16", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (11137.706, 8620.238, 846.3823), (0.0, -0.8127746084555306, 0.0), (1.0, 1.0, 1.0), "PWM_Quarry_RockDebris_A17", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (10381.947, 8448.448, 1144.4268), (-11.04586701775079, -1.0573424325978196, 5.0813105609507865), (0.925027, 0.925027, 0.925027), "PWM_Quarry_RockDebris_A18", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (10302.559, 8680.684, 1147.0781), (-18.404475836992894, -0.7999267333097287, -3.392547155833438), (0.738415, 0.925027, 1.323394), "PWM_Quarry_RockDebris_A19", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (10928.212, 8674.937, 846.3823), (0.0, -0.8127746084555306, 0.0), (1.0, 1.0, 1.0), "PWM_Quarry_RockDebris_A2", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1655.4648, 8552.511, 795.6221), (-0.9222106598849289, 67.34435699878074, 0.3848940028590784), (1.582294, 1.582294, 1.582294), "PWM_Quarry_RockDebris_A20_368", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1356.418, 8647.499, 796.82227), (0.7966530808602331, -52.8662431749025, 0.6031941056788782), (1.582294, 1.582294, 1.582294), "PWM_Quarry_RockDebris_A21", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1127.6846, 8750.765, 798.4346), (0.7966530808602331, -52.8662431749025, 0.6031941056788782), (1.582294, 1.582294, 1.582294), "PWM_Quarry_RockDebris_A22", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (727.77344, 8648.318, 799.90344), (-0.40234378559952033, 23.758997511936236, 0.8920321934142956), (1.582294, 1.582294, 1.582294), "PWM_Quarry_RockDebris_A23", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1483.6016, 9475.54, 793.0503), (-0.5127257551004595, 120.84939564670222, -0.5122985346114272), (1.582294, 1.582294, 1.582294), "PWM_Quarry_RockDebris_A24", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1614.1562, 9223.396, 793.87695), (0.4773003416887798, 120.84064941800247, -0.5122679949606473), (1.582294, 1.582294, 1.582294), "PWM_Quarry_RockDebris_A25", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1864.8682, 9005.319, 794.1504), (0.6137680338171891, 139.1119666284655, -0.33682251704911176), (1.582294, 1.582294, 1.582294), "PWM_Quarry_RockDebris_A26", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1167.1943, 9780.521, 794.5426), (0.18625927928997402, 70.73474224142869, 0.22926899265374212), (1.582294, 1.582294, 1.582294), "PWM_Quarry_RockDebris_A27", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (890.5117, 10054.582, 795.3839), (-0.281738247035542, -177.6538091316053, 0.08864798242251251), (1.582294, 1.582294, 1.582294), "PWM_Quarry_RockDebris_A28", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (606.1553, 10108.709, 794.1007), (-0.281738247035542, -177.6538091316053, 0.08864798242251251), (1.582294, 1.582294, 1.582294), "PWM_Quarry_RockDebris_A29", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (11314.098, 8680.96, 846.3823), (0.0, 3.01924866170697, -0.0), (1.0, 1.0, 1.0), "PWM_Quarry_RockDebris_A3", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (893.0781, 9081.238, 789.7334), (-0.24581909073701838, 166.15191703134965, 0.16360798919305516), (1.238404, 1.582294, 1.582294), "PWM_Quarry_RockDebris_A30", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1856.0309, 8089.399, 1131.368), (-3.875183577138043, 67.04740260161327, 7.577631322937278), (1.066694, 1.066694, 1.368673), "PWM_Quarry_RockDebris_A31", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (11228.229, 8779.697, 794.2344), (0.0, -142.3865474755917, 0.0), (1.520606, 1.520606, 1.520606), "PWM_Quarry_RockDebris_A32", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (8612.38, 9250.811, 1253.7822), (0.0, 87.87762899908874, -0.0), (1.0, 1.0, 1.0), "PWM_Quarry_RockDebris_A33", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (8611.2, 9488.267, 1256.3281), (-0.8559872412207611, 139.39251657625928, 4.492844856702698), (1.7389312, 1.7389312, 1.7389312), "PWM_Quarry_RockDebris_A34", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (7553.09, 10507.908, 1249.3667), (0.0, 116.83005731242248, -0.0), (1.1394415, 1.1394415, 1.1394415), "PWM_Quarry_RockDebris_A35_293", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (8227.331, 9971.286, 1245.8135), (0.40213409719640336, 139.396833832505, 3.414610481807458), (1.738931, 1.738931, 1.738931), "PWM_Quarry_RockDebris_A36", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (7086.367, 10777.135, 1249.9502), (0.0, -141.20101981651794, 0.0), (1.139441, 1.139441, 1.139441), "PWM_Quarry_RockDebris_A37", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (6174.479, 10893.24, 1253.0034), (0.0, -141.20101981651794, 0.0), (1.139441, 1.139441, 1.139441), "PWM_Quarry_RockDebris_A38", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5651.826, 10805.2705, 1253.0034), (0.0, -171.11371227347104, 0.0), (1.139441, 1.139441, 1.139441), "PWM_Quarry_RockDebris_A39", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (11396.842, 9359.717, 794.9287), (0.0, 12.201476988873981, -0.0), (1.0, 1.0, 1.0), "PWM_Quarry_RockDebris_A4", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (6002.9824, 10794.85, 1249.2793), (0.0, -171.11371227347104, 0.0), (1.139441, 1.139441, 1.139441), "PWM_Quarry_RockDebris_A40", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (6173.6714, 10053.136, 1247.4165), (0.0, -99.8666401693958, 0.0), (1.139441, 1.139441, 1.139441), "PWM_Quarry_RockDebris_A41", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5356.415, 10541.829, 1250.0117), (0.0, -141.20101981651794, 0.0), (1.139441, 1.139441, 1.139441), "PWM_Quarry_RockDebris_A42", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4746.9873, 10137.449, 1245.627), (0.0, -125.27161242634241, 0.0), (1.9563465, 1.9563465, 1.9563465), "PWM_Quarry_RockDebris_A43", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4398.006, 9202.506, 1260.5508), (1.4983930304450284, -165.99208022232907, 2.4538560680407184), (1.3331083, 1.3331083, 1.3331083), "PWM_Quarry_RockDebris_A44", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4175.788, 9181.572, 1253.1831), (0.0, -72.67523724834145, 0.0), (1.4068452, 1.333108, 1.4068452), "PWM_Quarry_RockDebris_A45", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4246.4116, 8775.706, 1255.6157), (-4.169661856543073e-07, -81.81552164772609, 7.547347972020615), (1.406845, 1.333108, 1.406845), "PWM_Quarry_RockDebris_A46", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4091.6445, 8190.9995, 1252.6777), (0.0, -43.927243078463, 0.0), (1.406845, 1.333108, 1.406845), "PWM_Quarry_RockDebris_A47", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5061.01, 7052.8325, 1250.5986), (0.0, -50.00299195911964, 0.0), (1.406845, 1.333108, 1.406845), "PWM_Quarry_RockDebris_A48", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4262.2793, 7493.109, 1254.3145), (-1.2080080348135336, -43.93939743017052, 1.163897195448285), (1.406845, 1.333108, 1.406845), "PWM_Quarry_RockDebris_A49", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (11816.232, 8928.178, 795.7744), (0.0, 58.349391129641155, -0.0), (1.0, 1.0, 1.0), "PWM_Quarry_RockDebris_A5", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4638.082, 7080.33, 1251.7568), (0.0, -81.81564481219948, 0.0), (1.406845, 1.333108, 1.406845), "PWM_Quarry_RockDebris_A50", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (225.69196, 10039.078, 792.1339), (-0.281738247035542, -177.6538091316053, 0.08864798242251251), (1.582294, 1.582294, 1.582294), "PWM_Quarry_RockDebris_A51", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5614.761, 6311.705, 1251.1523), (0.0, -0.5671387256803192, 0.0), (1.406845, 1.333108, 1.406845), "PWM_Quarry_RockDebris_A52", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (234.84338, 8877.697, 790.1487), (0.06875949448631054, -56.71590948584194, -0.2872313896709553), (1.582294, 1.582294, 1.582294), "PWM_Quarry_RockDebris_A53", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (296.59744, 9284.18, 791.1586), (0.12903342406908125, 83.90947583308996, 0.26566648371424445), (1.582294, 1.582294, 1.582294), "PWM_Quarry_RockDebris_A54", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (7114.919, 6324.168, 1252.6294), (-1.7040100879891347, 31.167295964353166, 5.935488199955815), (1.7644666, 1.6907296, 1.7644666), "PWM_Quarry_RockDebris_A55", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (7895.758, 6738.579, 1251.206), (0.0, 31.342225872816712, -0.0), (1.406845, 1.333108, 1.406845), "PWM_Quarry_RockDebris_A56", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4122.5654, 8128.917, 1251.8076), (0.0, -81.81564481219948, 0.0), (1.406845, 1.333108, 1.406845), "PWM_Quarry_RockDebris_A57", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4949.1533, 9895.224, 1249.4912), (0.0, -125.27161242634241, 0.0), (1.678802, 1.678802, 1.678802), "PWM_Quarry_RockDebris_A58", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (8158.0264, 7697.6006, 1250.5137), (-3.0363092710187795e-08, 31.34344060800931, -1.4519653070599223), (2.425343, 2.3516064, 2.425343), "PWM_Quarry_RockDebris_A59", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (11880.124, 8920.054, 785.9532), (0.0, -118.98136777466517, 0.0), (1.520606, 1.520606, 1.520606), "PWM_Quarry_RockDebris_A6", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (7757.8037, 7884.1895, 1250.9658), (-3.0363092710187795e-08, 31.34344060800931, -1.4519653070599223), (2.425343, 2.351606, 2.425343), "PWM_Quarry_RockDebris_A60", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (7911.5444, 7181.8447, 1243.563), (-1.879211426963545, 103.61712005210215, 0.31502382232630666), (2.425343, 2.351606, 3.115638), "PWM_Quarry_RockDebris_A61", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (7618.926, 6583.3115, 1249.4062), (0.0, 140.37197325605243, -0.0), (1.764467, 1.69073, 1.764467), "PWM_Quarry_RockDebris_A62", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (385.12463, 9804.886, 791.49786), (0.16132905806679546, -37.02834519705679, -0.24728390588891855), (1.582294, 1.582294, 1.582294), "PWM_Quarry_RockDebris_A63", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5313.6597, 8984.1, 1256.727), (-3.470245464780798, -166.02419150365048, -1.4496460553581294), (1.333108, 1.333108, 1.333108), "PWM_Quarry_RockDebris_A65", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5273.0254, 9561.723, 1263.3867), (-5.680611835479956e-09, -125.2716076793236, 0.13989345048188107), (1.678802, 1.678802, 1.678802), "PWM_Quarry_RockDebris_A66", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5174.126, 9264.957, 1253.2759), (0.07477008204051931, 86.99990638222353, -0.11834715749929572), (1.678802, 1.678802, 1.678802), "PWM_Quarry_RockDebris_A67", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (8631.822, 7518.9805, 1265.04), (-0.7708740840961043, 31.313507624516777, 2.256077146411271), (2.425343, 2.351606, 2.425343), "PWM_Quarry_RockDebris_A68", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (8681.532, 8876.477, 1251.6089), (-2.086028946067988, 139.37232294854903, 0.9419700166565901), (1.4022268, 1.4022268, 1.4022268), "PWM_Quarry_RockDebris_A69", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (11666.7, 8733.916, 796.1455), (0.0, 58.349391129641155, -0.0), (1.0, 1.0, 1.0), "PWM_Quarry_RockDebris_A7", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5547.5625, 6816.5615, 1253.6455), (-2.161987284971703, -81.81552396428263, -2.0430296698007933), (1.406845, 1.333108, 1.406845), "PWM_Quarry_RockDebris_A70", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5963.2295, 7151.328, 1253.9761), (-1.1058348633924446, -81.8529129335503, -1.3138123484424327), (1.406845, 1.333108, 1.5820158), "PWM_Quarry_RockDebris_A71", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5420.8525, 6570.7666, 1251.2954), (-0.8739012687919063, 109.17350401051108, 0.5185032577735766), (1.406845, 1.333108, 1.8881733), "PWM_Quarry_RockDebris_A72", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5213.8896, 6677.6963, 1249.2119), (-0.8492735781357432, 173.16281735353925, -0.5579223717412407), (1.406845, 1.333108, 1.888173), "PWM_Quarry_RockDebris_A73", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4770.93, 7249.5103, 1248.7783), (0.13434980281072073, -164.67631083264527, -0.5476378674485874), (1.406845, 1.333108, 1.888173), "PWM_Quarry_RockDebris_A74", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4803.9727, 6817.298, 1247.8579), (0.0, 4.936096067232363, -0.0), (1.406845, 1.333108, 1.406845), "PWM_Quarry_RockDebris_A75", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4908.9404, 8121.716, 1253.4502), (0.07477007852232609, 86.99990298507977, 0.19246313016959074), (1.678802, 1.678802, 1.9504638), "PWM_Quarry_RockDebris_A78", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4821.1494, 9551.191, 1253.874), (0.07477008204051931, 86.99990638222353, -0.11834715749929572), (1.678802, 1.678802, 1.678802), "PWM_Quarry_RockDebris_A79", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (12036.95, 8918.423, 785.9527), (0.0, -108.31493738075638, 0.0), (1.520606, 1.520606, 1.520606), "PWM_Quarry_RockDebris_A8", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5336.576, 8706.885, 1264.1963), (4.672027413634194, -16.37378112948167, -0.6003419109169204), (1.678802, 1.678802, 1.6023374), "PWM_Quarry_RockDebris_A81_268", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5333.7476, 10583.131, 1268.4219), (-1.4739233374221463e-08, -163.7743932436821, 5.9172384627868295), (1.678802, 1.678802, 1.678802), "PWM_Quarry_RockDebris_A82", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (6204.6943, 9990.297, 1258.8037), (0.0, 162.27713828870046, -0.0), (1.678802, 1.678802, 1.678802), "PWM_Quarry_RockDebris_A83", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (6831.0635, 9940.939, 1262.0723), (2.367746675509396, -136.5059153261581, -2.803131240616246), (1.678802, 1.678802, 1.678802), "PWM_Quarry_RockDebris_A84", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (6728.926, 10386.756, 1253.1035), (0.0, 27.19453356865914, -0.0), (1.2760019, 1.2760019, 1.0094934), "PWM_Quarry_RockDebris_A85", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5786.255, 10495.484, 1251.8877), (0.0, -26.783934512491392, 0.0), (1.276002, 1.276002, 1.009493), "PWM_Quarry_RockDebris_A86", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (7258.243, 10036.916, 1257.5693), (-2.668182174621225, 77.80422344094075, -0.6270445129865164), (1.678802, 1.678802, 1.9820409), "PWM_Quarry_RockDebris_A87", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (11578.295, 9757.969, 794.2344), (0.0, -142.3865474755917, 0.0), (1.520606, 1.520606, 1.520606), "PWM_Quarry_RockDebris_A9", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (6544.084, 10764.166, 1250.5742), (0.0, 156.42880346513485, -0.0), (1.678802, 1.678802, 1.678802), "PWM_Quarry_RockDebris_A93", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (7156.9043, 10552.213, 1251.2793), (0.0, -166.1905831831436, 0.0), (1.1893601, 1.1893601, 1.0993711), "PWM_Quarry_RockDebris_A94", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (6152.441, 9834.323, 1277.5913), (-8.335814546157089, 75.76527395015785, 2.4017097435682215), (1.433339, 1.214637, 2.511202), "PWM_Quarry_RockDebris_A95", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (8191.9062, 9589.162, 1249.4873), (-0.7684936554951532, -121.52272497563361, 0.9327550215964112), (1.2777922, 1.2777922, 1.5810311), "PWM_Quarry_RockDebris_A97", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (7752.4766, 8781.148, 1252.9175), (2.8734670417406485, -121.46394333005206, 0.9338448234837448), (1.277792, 1.277792, 1.581031), "PWM_Quarry_RockDebris_A98", _folder)
if a: placed += 1
else: skipped += 1

# Batch 66: StaticMesh'PWM_Quarry_RockDebris_A_Optimized' (1 instances)
_mesh_path = "/Game/Unshippable/Whitebox/Rocks/Meshes/PWM_Quarry_RockDebris_A_Optimized"
_materials = ['/Game/Environments/ProcTexturing/ProcMaterial_Quarry_RockDebris_A']
_folder = "Reconstruction/BD_BB_Chapter5_BoneHoard/Meshes"
a = spawn_static_mesh(_mesh_path, _materials, (2476.773, 8520.951, 1141.173), (2.41084483388062, 0.0, -0.0), (1.0, 1.0, 1.0), "PWM_Quarry_RockDebris_A_Optimized_60", _folder)
if a: placed += 1
else: skipped += 1

# ======================================================================
# PHASE 2: ConstructionCatalog  (construction blocks)
# ======================================================================
unreal.log(f"[{BUBBLE_NAME}] Phase 2: Placing construction blocks...")

# Construction blocks use DecoVolume transforms (matched by Name)
_folder = "Reconstruction/BD_BB_Chapter5_BoneHoard/Construction"

# Construction: AB_Orc_Scaffolding_Balcony_C_2
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Wood
#   Volume: EMorSimpleShape::OrientedBox, BoxExtent: (114.1, 180.4, 168.8)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (3837.0107, 9249.16, 1797.1106), (0.0, 0.0, -0.0), (2.2821, 3.6077, 3.3760), "AB_Orc_Scaffolding_Balcony_C_2", _folder)
if a: placed += 1
else: skipped += 1

# Construction: AB_Orc_Scaffolding_Balcony_C10
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Wood
#   Volume: EMorSimpleShape::OrientedBox, BoxExtent: (116.1, 182.4, 168.8)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (3790.636, 7847.1606, 1797.1106), (0.0, 0.0, -0.0), (2.3228, 3.6481, 3.3760), "AB_Orc_Scaffolding_Balcony_C10", _folder)
if a: placed += 1
else: skipped += 1

# Construction: AB_Orc_Scaffolding_Balcony_C11
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Wood
#   Volume: EMorSimpleShape::OrientedBox, BoxExtent: (182.4, 116.1, 168.8)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (3935.8674, 8077.3486, 1797.1106), (0.0, 0.0, -0.0), (3.6481, 2.3228, 3.3760), "AB_Orc_Scaffolding_Balcony_C11", _folder)
if a: placed += 1
else: skipped += 1

# Construction: AB_Orc_Scaffolding_Balcony_C12
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Wood
#   Volume: EMorSimpleShape::OrientedBox, BoxExtent: (182.4, 116.1, 168.8)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (4020.824, 7701.9346, 1797.1106), (0.0, 0.0, -0.0), (3.6481, 2.3228, 3.3760), "AB_Orc_Scaffolding_Balcony_C12", _folder)
if a: placed += 1
else: skipped += 1

# Construction: AB_Orc_Scaffolding_Balcony_C13
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Wood
#   Volume: EMorSimpleShape::OrientedBox, BoxExtent: (116.1, 182.4, 168.8)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (4166.0557, 7932.124, 2397.1106), (0.0, 0.0, -0.0), (2.3228, 3.6481, 3.3760), "AB_Orc_Scaffolding_Balcony_C13", _folder)
if a: placed += 1
else: skipped += 1

# Construction: AB_Orc_Scaffolding_Balcony_C14
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Wood
#   Volume: EMorSimpleShape::OrientedBox, BoxExtent: (116.1, 182.4, 168.8)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (3790.636, 7847.1606, 2397.1106), (0.0, 0.0, -0.0), (2.3228, 3.6481, 3.3760), "AB_Orc_Scaffolding_Balcony_C14", _folder)
if a: placed += 1
else: skipped += 1

# Construction: AB_Orc_Scaffolding_Balcony_C15
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Wood
#   Volume: EMorSimpleShape::OrientedBox, BoxExtent: (161.9, 164.8, 168.8)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (4809.331, 10454.482, 1797.1106), (0.0, 0.0, -0.0), (3.2374, 3.2959, 3.3760), "AB_Orc_Scaffolding_Balcony_C15", _folder)
if a: placed += 1
else: skipped += 1

# Construction: AB_Orc_Scaffolding_Balcony_C16
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Wood
#   Volume: EMorSimpleShape::OrientedBox, BoxExtent: (182.4, 116.1, 168.8)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (4016.7063, 7716.356, 2397.1106), (0.0, 0.0, -0.0), (3.6481, 2.3228, 3.3760), "AB_Orc_Scaffolding_Balcony_C16", _folder)
if a: placed += 1
else: skipped += 1

# Construction: AB_Orc_Scaffolding_Balcony_C17
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Wood
#   Volume: EMorSimpleShape::OrientedBox, BoxExtent: (164.8, 161.9, 168.8)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (4801.891, 10182.628, 1797.1106), (0.0, 0.0, -0.0), (3.2959, 3.2374, 3.3760), "AB_Orc_Scaffolding_Balcony_C17", _folder)
if a: placed += 1
else: skipped += 1

# Construction: AB_Orc_Scaffolding_Balcony_C18
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Wood
#   Volume: EMorSimpleShape::OrientedBox, BoxExtent: (109.9, 182.4, 168.8)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (7277.655, 6158.248, 1787.1106), (0.0, 0.0, -0.0), (2.1988, 3.6477, 3.3760), "AB_Orc_Scaffolding_Balcony_C18", _folder)
if a: placed += 1
else: skipped += 1

# Construction: AB_Orc_Scaffolding_Balcony_C19
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Wood
#   Volume: EMorSimpleShape::OrientedBox, BoxExtent: (161.9, 164.8, 168.8)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (4530.038, 10190.064, 2397.1106), (0.0, 0.0, -0.0), (3.2374, 3.2959, 3.3760), "AB_Orc_Scaffolding_Balcony_C19", _folder)
if a: placed += 1
else: skipped += 1

# Construction: AB_Orc_Scaffolding_Balcony_C2
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Wood
#   Volume: EMorSimpleShape::OrientedBox, BoxExtent: (114.1, 180.4, 168.8)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (4212.857, 9152.767, 1797.1106), (0.0, 0.0, -0.0), (2.2821, 3.6077, 3.3760), "AB_Orc_Scaffolding_Balcony_C2", _folder)
if a: placed += 1
else: skipped += 1

# Construction: AB_Orc_Scaffolding_Balcony_C20
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Wood
#   Volume: EMorSimpleShape::OrientedBox, BoxExtent: (164.8, 161.9, 168.8)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (4801.891, 10182.628, 2397.1106), (0.0, 0.0, -0.0), (3.2959, 3.2374, 3.3760), "AB_Orc_Scaffolding_Balcony_C20", _folder)
if a: placed += 1
else: skipped += 1

# Construction: AB_Orc_Scaffolding_Balcony_C21
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Wood
#   Volume: EMorSimpleShape::OrientedBox, BoxExtent: (164.8, 161.9, 168.8)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (4537.4795, 10461.923, 2397.1106), (0.0, 0.0, -0.0), (3.2959, 3.2374, 3.3760), "AB_Orc_Scaffolding_Balcony_C21", _folder)
if a: placed += 1
else: skipped += 1

# Construction: AB_Orc_Scaffolding_Balcony_C22_19
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Wood
#   Volume: EMorSimpleShape::OrientedBox, BoxExtent: (182.4, 116.1, 168.8)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (5857.9873, 10735.529, 1797.1106), (0.0, 0.0, -0.0), (3.6481, 2.3228, 3.3760), "AB_Orc_Scaffolding_Balcony_C22_19", _folder)
if a: placed += 1
else: skipped += 1

# Construction: AB_Orc_Scaffolding_Balcony_C23
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Wood
#   Volume: EMorSimpleShape::OrientedBox, BoxExtent: (182.4, 116.1, 168.8)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (5857.9873, 10735.529, 2397.1106), (0.0, 0.0, -0.0), (3.6481, 2.3228, 3.3760), "AB_Orc_Scaffolding_Balcony_C23", _folder)
if a: placed += 1
else: skipped += 1

# Construction: AB_Orc_Scaffolding_Balcony_C24
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Wood
#   Volume: EMorSimpleShape::OrientedBox, BoxExtent: (109.9, 182.4, 168.8)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (6897.552, 6091.8984, 1787.1106), (0.0, 0.0, -0.0), (2.1988, 3.6477, 3.3760), "AB_Orc_Scaffolding_Balcony_C24", _folder)
if a: placed += 1
else: skipped += 1

# Construction: AB_Orc_Scaffolding_Balcony_C25
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Wood
#   Volume: EMorSimpleShape::OrientedBox, BoxExtent: (182.4, 109.9, 168.8)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (7120.7793, 5935.019, 2387.1106), (0.0, 0.0, -0.0), (3.6477, 2.1988, 3.3760), "AB_Orc_Scaffolding_Balcony_C25", _folder)
if a: placed += 1
else: skipped += 1

# Construction: AB_Orc_Scaffolding_Balcony_C26
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Wood
#   Volume: EMorSimpleShape::OrientedBox, BoxExtent: (109.9, 182.4, 168.8)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (7277.655, 6158.248, 2387.1106), (0.0, 0.0, -0.0), (2.1988, 3.6477, 3.3760), "AB_Orc_Scaffolding_Balcony_C26", _folder)
if a: placed += 1
else: skipped += 1

# Construction: AB_Orc_Scaffolding_Balcony_C27
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Wood
#   Volume: EMorSimpleShape::OrientedBox, BoxExtent: (109.9, 182.4, 168.8)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (6897.552, 6091.8984, 2387.1106), (0.0, 0.0, -0.0), (2.1988, 3.6477, 3.3760), "AB_Orc_Scaffolding_Balcony_C27", _folder)
if a: placed += 1
else: skipped += 1

# Construction: AB_Orc_Scaffolding_Balcony_C28
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Wood
#   Volume: EMorSimpleShape::OrientedBox, BoxExtent: (182.4, 109.9, 168.8)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (7120.7793, 5935.019, 1787.1106), (0.0, 0.0, -0.0), (3.6477, 2.1988, 3.3760), "AB_Orc_Scaffolding_Balcony_C28", _folder)
if a: placed += 1
else: skipped += 1

# Construction: AB_Orc_Scaffolding_Balcony_C29
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Wood
#   Volume: EMorSimpleShape::OrientedBox, BoxExtent: (114.1, 180.4, 168.8)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (5619.8677, 6173.8804, 1937.1107), (0.0, 0.0, -0.0), (2.2821, 3.6077, 3.3760), "AB_Orc_Scaffolding_Balcony_C29", _folder)
if a: placed += 1
else: skipped += 1

# Construction: AB_Orc_Scaffolding_Balcony_C3
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Wood
#   Volume: EMorSimpleShape::OrientedBox, BoxExtent: (180.4, 114.1, 168.8)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (3976.7373, 9013.044, 1797.1106), (0.0, 0.0, -0.0), (3.6077, 2.2821, 3.3760), "AB_Orc_Scaffolding_Balcony_C3", _folder)
if a: placed += 1
else: skipped += 1

# Construction: AB_Orc_Scaffolding_Balcony_C30
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Wood
#   Volume: EMorSimpleShape::OrientedBox, BoxExtent: (180.4, 114.1, 168.8)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (5849.4204, 6311.838, 2297.1106), (0.0, 0.0, -0.0), (3.6077, 2.2821, 3.3760), "AB_Orc_Scaffolding_Balcony_C30", _folder)
if a: placed += 1
else: skipped += 1

# Construction: AB_Orc_Scaffolding_Balcony_C31
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Wood
#   Volume: EMorSimpleShape::OrientedBox, BoxExtent: (114.1, 180.4, 168.8)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (5976.3906, 6082.663, 1937.1107), (0.0, 0.0, -0.0), (2.2821, 3.6077, 3.3760), "AB_Orc_Scaffolding_Balcony_C31", _folder)
if a: placed += 1
else: skipped += 1

# Construction: AB_Orc_Scaffolding_Balcony_C32
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Wood
#   Volume: EMorSimpleShape::OrientedBox, BoxExtent: (114.1, 180.4, 168.8)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (4212.856, 9152.768, 2397.1106), (0.0, 0.0, -0.0), (2.2821, 3.6077, 3.3760), "AB_Orc_Scaffolding_Balcony_C32", _folder)
if a: placed += 1
else: skipped += 1

# Construction: AB_Orc_Scaffolding_Balcony_C33
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Wood
#   Volume: EMorSimpleShape::OrientedBox, BoxExtent: (180.4, 114.1, 168.8)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (7064.009, 10786.641, 2302.1106), (0.0, 0.0, -0.0), (3.6077, 2.2821, 3.3760), "AB_Orc_Scaffolding_Balcony_C33", _folder)
if a: placed += 1
else: skipped += 1

# Construction: AB_Orc_Scaffolding_Balcony_C34
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Wood
#   Volume: EMorSimpleShape::OrientedBox, BoxExtent: (180.4, 114.1, 168.8)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (7064.009, 10786.641, 1752.1106), (0.0, 0.0, -0.0), (3.6077, 2.2821, 3.3760), "AB_Orc_Scaffolding_Balcony_C34", _folder)
if a: placed += 1
else: skipped += 1

# Construction: AB_Orc_Scaffolding_Balcony_C35
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Wood
#   Volume: EMorSimpleShape::OrientedBox, BoxExtent: (182.4, 116.1, 168.8)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (3926.2483, 8074.601, 2397.1106), (0.0, 0.0, -0.0), (3.6481, 2.3228, 3.3760), "AB_Orc_Scaffolding_Balcony_C35", _folder)
if a: placed += 1
else: skipped += 1

# Construction: AB_Orc_Scaffolding_Balcony_C36
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Wood
#   Volume: EMorSimpleShape::OrientedBox, BoxExtent: (114.1, 180.4, 168.8)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (8680.738, 7945.165, 2297.1106), (0.0, 0.0, -0.0), (2.2821, 3.6077, 3.3760), "AB_Orc_Scaffolding_Balcony_C36", _folder)
if a: placed += 1
else: skipped += 1

# Construction: AB_Orc_Scaffolding_Balcony_C37
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Wood
#   Volume: EMorSimpleShape::OrientedBox, BoxExtent: (114.1, 180.4, 168.8)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (8680.738, 7945.165, 1757.1106), (0.0, 0.0, -0.0), (2.2821, 3.6077, 3.3760), "AB_Orc_Scaffolding_Balcony_C37", _folder)
if a: placed += 1
else: skipped += 1

# Construction: AB_Orc_Scaffolding_Balcony_C38
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Wood
#   Volume: EMorSimpleShape::OrientedBox, BoxExtent: (109.9, 182.4, 168.8)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (8633.64, 9146.484, 1757.1106), (0.0, 0.0, -0.0), (2.1988, 3.6477, 3.3760), "AB_Orc_Scaffolding_Balcony_C38", _folder)
if a: placed += 1
else: skipped += 1

# Construction: AB_Orc_Scaffolding_Balcony_C39
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Wood
#   Volume: EMorSimpleShape::OrientedBox, BoxExtent: (109.9, 182.4, 168.8)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (8633.64, 9146.484, 2317.1106), (0.0, 0.0, -0.0), (2.1988, 3.6477, 3.3760), "AB_Orc_Scaffolding_Balcony_C39", _folder)
if a: placed += 1
else: skipped += 1

# Construction: AB_Orc_Scaffolding_Balcony_C4
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Wood
#   Volume: EMorSimpleShape::OrientedBox, BoxExtent: (180.4, 114.1, 168.8)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (4073.132, 9388.884, 1797.1106), (0.0, 0.0, -0.0), (3.6077, 2.2821, 3.3760), "AB_Orc_Scaffolding_Balcony_C4", _folder)
if a: placed += 1
else: skipped += 1

# Construction: AB_Orc_Scaffolding_Balcony_C40
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Wood
#   Volume: EMorSimpleShape::OrientedBox, BoxExtent: (182.4, 109.9, 168.8)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (7064.167, 6317.3955, 2387.1106), (0.0, 0.0, -0.0), (3.6477, 2.1988, 3.3760), "AB_Orc_Scaffolding_Balcony_C40", _folder)
if a: placed += 1
else: skipped += 1

# Construction: AB_Orc_Scaffolding_Balcony_C5
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Wood
#   Volume: EMorSimpleShape::OrientedBox, BoxExtent: (114.1, 180.4, 168.8)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (3837.0107, 9249.16, 2397.1106), (0.0, 0.0, -0.0), (2.2821, 3.6077, 3.3760), "AB_Orc_Scaffolding_Balcony_C5", _folder)
if a: placed += 1
else: skipped += 1

# Construction: AB_Orc_Scaffolding_Balcony_C6
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Wood
#   Volume: EMorSimpleShape::OrientedBox, BoxExtent: (182.4, 109.9, 168.8)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (7054.4287, 6315.126, 1787.1106), (0.0, 0.0, -0.0), (3.6477, 2.1988, 3.3760), "AB_Orc_Scaffolding_Balcony_C6", _folder)
if a: placed += 1
else: skipped += 1

# Construction: AB_Orc_Scaffolding_Balcony_C7
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Wood
#   Volume: EMorSimpleShape::OrientedBox, BoxExtent: (180.4, 114.1, 168.8)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (3976.7373, 9013.044, 2397.1106), (0.0, 0.0, -0.0), (3.6077, 2.2821, 3.3760), "AB_Orc_Scaffolding_Balcony_C7", _folder)
if a: placed += 1
else: skipped += 1

# Construction: AB_Orc_Scaffolding_Balcony_C8
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Wood
#   Volume: EMorSimpleShape::OrientedBox, BoxExtent: (180.4, 114.1, 168.8)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (4073.132, 9388.884, 2397.1106), (0.0, 0.0, -0.0), (3.6077, 2.2821, 3.3760), "AB_Orc_Scaffolding_Balcony_C8", _folder)
if a: placed += 1
else: skipped += 1

# Construction: AB_Orc_Scaffolding_Balcony_C9
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Wood
#   Volume: EMorSimpleShape::OrientedBox, BoxExtent: (116.1, 182.4, 168.8)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (4166.0557, 7932.124, 1797.1106), (0.0, 0.0, -0.0), (2.3228, 3.6481, 3.3760), "AB_Orc_Scaffolding_Balcony_C9", _folder)
if a: placed += 1
else: skipped += 1

# Construction: AB_Orc_Scaffolding_Foundation_1x1m_2
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Stone
#   Volume: EMorSimpleShape::OrientedBox, BoxExtent: (96.9, 100.7, 172.5)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (4729.963, 10117.886, 2089.6206), (0.0, 0.0, -0.0), (1.9385, 2.0145, 3.4493), "AB_Orc_Scaffolding_Foundation_1x1m_2", _folder)
if a: placed += 1
else: skipped += 1

# Construction: AB_Orc_Scaffolding_Foundation_1x1m10
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Stone
#   Volume: EMorSimpleShape::OrientedBox, BoxExtent: (96.9, 100.7, 172.5)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (8162.9795, 6579.075, 1789.6206), (0.0, 0.0, -0.0), (1.9385, 2.0145, 3.4493), "AB_Orc_Scaffolding_Foundation_1x1m10", _folder)
if a: placed += 1
else: skipped += 1

# Construction: AB_Orc_Scaffolding_Foundation_1x1m11
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Stone
#   Volume: EMorSimpleShape::OrientedBox, BoxExtent: (100.7, 96.9, 172.5)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (8026.042, 6724.8696, 1789.6206), (0.0, 0.0, -0.0), (2.0145, 1.9385, 3.4493), "AB_Orc_Scaffolding_Foundation_1x1m11", _folder)
if a: placed += 1
else: skipped += 1

# Construction: AB_Orc_Scaffolding_Foundation_1x1m12
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Stone
#   Volume: EMorSimpleShape::OrientedBox, BoxExtent: (96.9, 100.7, 172.5)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (8020.4883, 6730.6143, 2364.6206), (0.0, 0.0, -0.0), (1.9385, 2.0145, 3.4493), "AB_Orc_Scaffolding_Foundation_1x1m12", _folder)
if a: placed += 1
else: skipped += 1

# Construction: AB_Orc_Scaffolding_Foundation_1x1m13
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Stone
#   Volume: EMorSimpleShape::OrientedBox, BoxExtent: (100.7, 96.9, 172.5)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (8157.426, 6584.8193, 2364.6206), (0.0, 0.0, -0.0), (2.0145, 1.9385, 3.4493), "AB_Orc_Scaffolding_Foundation_1x1m13", _folder)
if a: placed += 1
else: skipped += 1

# Construction: AB_Orc_Scaffolding_Foundation_1x1m14
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Stone
#   Volume: EMorSimpleShape::OrientedBox, BoxExtent: (101.3, 96.4, 172.5)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (4436.241, 6802.0254, 1784.6206), (0.0, 0.0, -0.0), (2.0251, 1.9286, 3.4493), "AB_Orc_Scaffolding_Foundation_1x1m14", _folder)
if a: placed += 1
else: skipped += 1

# Construction: AB_Orc_Scaffolding_Foundation_1x1m15
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Stone
#   Volume: EMorSimpleShape::OrientedBox, BoxExtent: (96.4, 101.3, 172.5)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (4575.23, 6945.7725, 1784.6206), (0.0, 0.0, -0.0), (1.9286, 2.0251, 3.4493), "AB_Orc_Scaffolding_Foundation_1x1m15", _folder)
if a: placed += 1
else: skipped += 1

# Construction: AB_Orc_Scaffolding_Foundation_1x1m16
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Stone
#   Volume: EMorSimpleShape::OrientedBox, BoxExtent: (101.3, 96.4, 172.5)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (4580.875, 6951.6895, 2359.6206), (0.0, 0.0, -0.0), (2.0251, 1.9286, 3.4493), "AB_Orc_Scaffolding_Foundation_1x1m16", _folder)
if a: placed += 1
else: skipped += 1

# Construction: AB_Orc_Scaffolding_Foundation_1x1m17
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Stone
#   Volume: EMorSimpleShape::OrientedBox, BoxExtent: (96.4, 101.3, 172.5)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (4441.885, 6807.9434, 2359.6206), (0.0, 0.0, -0.0), (1.9286, 2.0251, 3.4493), "AB_Orc_Scaffolding_Foundation_1x1m17", _folder)
if a: placed += 1
else: skipped += 1

# Construction: AB_Orc_Scaffolding_Foundation_1x1m2
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Stone
#   Volume: EMorSimpleShape::OrientedBox, BoxExtent: (85.4, 90.9, 172.5)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (6026.766, 10812.627, 1794.6206), (0.0, 0.0, -0.0), (1.7072, 1.8180, 3.4493), "AB_Orc_Scaffolding_Foundation_1x1m2", _folder)
if a: placed += 1
else: skipped += 1

# Construction: AB_Orc_Scaffolding_Foundation_1x1m3
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Stone
#   Volume: EMorSimpleShape::OrientedBox, BoxExtent: (90.9, 85.4, 172.5)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (6028.032, 10812.814, 2089.6206), (0.0, 0.0, -0.0), (1.8180, 1.7072, 3.4493), "AB_Orc_Scaffolding_Foundation_1x1m3", _folder)
if a: placed += 1
else: skipped += 1

# Construction: AB_Orc_Scaffolding_Foundation_1x1m4
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Stone
#   Volume: EMorSimpleShape::OrientedBox, BoxExtent: (85.4, 90.9, 172.5)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (6028.2197, 10811.547, 2389.6206), (0.0, 0.0, -0.0), (1.7072, 1.8180, 3.4493), "AB_Orc_Scaffolding_Foundation_1x1m4", _folder)
if a: placed += 1
else: skipped += 1

# Construction: AB_Orc_Scaffolding_Foundation_1x1m5
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Stone
#   Volume: EMorSimpleShape::OrientedBox, BoxExtent: (90.9, 85.4, 172.5)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (5734.4844, 10713.174, 1794.6206), (0.0, 0.0, -0.0), (1.8180, 1.7072, 3.4493), "AB_Orc_Scaffolding_Foundation_1x1m5", _folder)
if a: placed += 1
else: skipped += 1

# Construction: AB_Orc_Scaffolding_Foundation_1x1m6
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Stone
#   Volume: EMorSimpleShape::OrientedBox, BoxExtent: (85.4, 90.9, 172.5)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (5734.672, 10711.908, 2089.6206), (0.0, 0.0, -0.0), (1.7072, 1.8180, 3.4493), "AB_Orc_Scaffolding_Foundation_1x1m6", _folder)
if a: placed += 1
else: skipped += 1

# Construction: AB_Orc_Scaffolding_Foundation_1x1m7
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Stone
#   Volume: EMorSimpleShape::OrientedBox, BoxExtent: (90.9, 85.4, 172.5)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (5733.4053, 10711.721, 2389.6206), (0.0, 0.0, -0.0), (1.8180, 1.7072, 3.4493), "AB_Orc_Scaffolding_Foundation_1x1m7", _folder)
if a: placed += 1
else: skipped += 1

# Construction: AB_Orc_Scaffolding_Foundation_1x1m8
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Stone
#   Volume: EMorSimpleShape::OrientedBox, BoxExtent: (100.7, 96.9, 172.5)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (8125.871, 10446.652, 1769.6206), (0.0, 0.0, -0.0), (2.0145, 1.9385, 3.4493), "AB_Orc_Scaffolding_Foundation_1x1m8", _folder)
if a: placed += 1
else: skipped += 1

# Construction: AB_Orc_Scaffolding_Foundation_1x1m9
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Stone
#   Volume: EMorSimpleShape::OrientedBox, BoxExtent: (96.9, 100.7, 172.5)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (7983.6704, 10313.191, 1769.6206), (0.0, 0.0, -0.0), (1.9385, 2.0144, 3.4493), "AB_Orc_Scaffolding_Foundation_1x1m9", _folder)
if a: placed += 1
else: skipped += 1

# Construction: AB_Orc_Scaffolding_Foundation_3x3m_B_2
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Stone
#   Volume: EMorSimpleShape::OrientedBox, BoxExtent: (202.6, 187.1, 167.7)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (4032.831, 9201.1, 1499.8337), (0.0, 0.0, -0.0), (4.0520, 3.7428, 3.3536), "AB_Orc_Scaffolding_Foundation_3x3m_B_2", _folder)
if a: placed += 1
else: skipped += 1

# Construction: AB_Orc_Scaffolding_Foundation_3x3m_B10
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Stone
#   Volume: EMorSimpleShape::OrientedBox, BoxExtent: (202.6, 187.1, 167.7)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (7111.425, 10971.191, 2334.8337), (0.0, 0.0, -0.0), (4.0520, 3.7428, 3.3536), "AB_Orc_Scaffolding_Foundation_3x3m_B10", _folder)
if a: placed += 1
else: skipped += 1

# Construction: AB_Orc_Scaffolding_Foundation_3x3m_B11
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Stone
#   Volume: EMorSimpleShape::OrientedBox, BoxExtent: (187.1, 202.6, 167.7)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (7108.495, 10961.863, 2054.8337), (0.0, 0.0, -0.0), (3.7428, 4.0520, 3.3536), "AB_Orc_Scaffolding_Foundation_3x3m_B11", _folder)
if a: placed += 1
else: skipped += 1

# Construction: AB_Orc_Scaffolding_Foundation_3x3m_B12
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Stone
#   Volume: EMorSimpleShape::OrientedBox, BoxExtent: (202.6, 187.1, 167.7)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (7106.5947, 10972.484, 1784.8337), (0.0, 0.0, -0.0), (4.0520, 3.7428, 3.3536), "AB_Orc_Scaffolding_Foundation_3x3m_B12", _folder)
if a: placed += 1
else: skipped += 1

# Construction: AB_Orc_Scaffolding_Foundation_3x3m_B13
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Stone
#   Volume: EMorSimpleShape::OrientedBox, BoxExtent: (189.5, 189.2, 167.7)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (8825.59, 9193.918, 1489.8337), (0.0, 0.0, -0.0), (3.7890, 3.7835, 3.3536), "AB_Orc_Scaffolding_Foundation_3x3m_B13", _folder)
if a: placed += 1
else: skipped += 1

# Construction: AB_Orc_Scaffolding_Foundation_3x3m_B14
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Stone
#   Volume: EMorSimpleShape::OrientedBox, BoxExtent: (189.2, 189.5, 167.7)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (8819.898, 9175.443, 2329.8337), (0.0, 0.0, -0.0), (3.7835, 3.7891, 3.3536), "AB_Orc_Scaffolding_Foundation_3x3m_B14", _folder)
if a: placed += 1
else: skipped += 1

# Construction: AB_Orc_Scaffolding_Foundation_3x3m_B15
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Stone
#   Volume: EMorSimpleShape::OrientedBox, BoxExtent: (189.5, 189.2, 167.7)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (8807.428, 9177.401, 2049.8337), (0.0, 0.0, -0.0), (3.7891, 3.7835, 3.3536), "AB_Orc_Scaffolding_Foundation_3x3m_B15", _folder)
if a: placed += 1
else: skipped += 1

# Construction: AB_Orc_Scaffolding_Foundation_3x3m_B16
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Stone
#   Volume: EMorSimpleShape::OrientedBox, BoxExtent: (189.2, 189.5, 167.7)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (8818.762, 9180.314, 1779.8337), (0.0, 0.0, -0.0), (3.7835, 3.7891, 3.3536), "AB_Orc_Scaffolding_Foundation_3x3m_B16", _folder)
if a: placed += 1
else: skipped += 1

# Construction: AB_Orc_Scaffolding_Foundation_3x3m_B17
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Stone
#   Volume: EMorSimpleShape::OrientedBox, BoxExtent: (187.1, 202.6, 167.7)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (8865.289, 7897.749, 2329.8337), (0.0, 0.0, -0.0), (3.7428, 4.0520, 3.3536), "AB_Orc_Scaffolding_Foundation_3x3m_B17", _folder)
if a: placed += 1
else: skipped += 1

# Construction: AB_Orc_Scaffolding_Foundation_3x3m_B18
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Stone
#   Volume: EMorSimpleShape::OrientedBox, BoxExtent: (202.6, 187.1, 167.7)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (8855.96, 7900.6777, 2049.8337), (0.0, 0.0, -0.0), (4.0520, 3.7428, 3.3536), "AB_Orc_Scaffolding_Foundation_3x3m_B18", _folder)
if a: placed += 1
else: skipped += 1

# Construction: AB_Orc_Scaffolding_Foundation_3x3m_B19
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Stone
#   Volume: EMorSimpleShape::OrientedBox, BoxExtent: (187.1, 202.6, 167.7)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (8866.584, 7902.578, 1779.8337), (0.0, 0.0, -0.0), (3.7428, 4.0520, 3.3536), "AB_Orc_Scaffolding_Foundation_3x3m_B19", _folder)
if a: placed += 1
else: skipped += 1

# Construction: AB_Orc_Scaffolding_Foundation_3x3m_B2
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Stone
#   Volume: EMorSimpleShape::OrientedBox, BoxExtent: (187.1, 202.6, 167.7)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (4025.0718, 9193.066, 2399.8337), (0.0, 0.0, -0.0), (3.7428, 4.0520, 3.3536), "AB_Orc_Scaffolding_Foundation_3x3m_B2", _folder)
if a: placed += 1
else: skipped += 1

# Construction: AB_Orc_Scaffolding_Foundation_3x3m_B20
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Stone
#   Volume: EMorSimpleShape::OrientedBox, BoxExtent: (202.6, 187.1, 167.7)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (8874.343, 7910.612, 1489.8337), (0.0, 0.0, -0.0), (4.0520, 3.7428, 3.3536), "AB_Orc_Scaffolding_Foundation_3x3m_B20", _folder)
if a: placed += 1
else: skipped += 1

# Construction: AB_Orc_Scaffolding_Foundation_3x3m_B21
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Stone
#   Volume: EMorSimpleShape::OrientedBox, BoxExtent: (223.9, 217.5, 167.7)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (8239.494, 6790.417, 1489.8337), (0.0, 0.0, -0.0), (4.4779, 4.3499, 3.3536), "AB_Orc_Scaffolding_Foundation_3x3m_B21", _folder)
if a: placed += 1
else: skipped += 1

# Construction: AB_Orc_Scaffolding_Foundation_3x3m_B22
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Stone
#   Volume: EMorSimpleShape::OrientedBox, BoxExtent: (217.5, 223.9, 167.7)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (8226.559, 6787.2373, 1784.8337), (0.0, 0.0, -0.0), (4.3499, 4.4779, 3.3536), "AB_Orc_Scaffolding_Foundation_3x3m_B22", _folder)
if a: placed += 1
else: skipped += 1

# Construction: AB_Orc_Scaffolding_Foundation_3x3m_B23
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Stone
#   Volume: EMorSimpleShape::OrientedBox, BoxExtent: (217.5, 223.9, 167.7)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (8226.559, 6787.2373, 2074.8337), (0.0, 0.0, -0.0), (4.3499, 4.4779, 3.3536), "AB_Orc_Scaffolding_Foundation_3x3m_B23", _folder)
if a: placed += 1
else: skipped += 1

# Construction: AB_Orc_Scaffolding_Foundation_3x3m_B24
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Stone
#   Volume: EMorSimpleShape::OrientedBox, BoxExtent: (223.9, 217.5, 167.7)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (8223.379, 6800.1733, 2369.8337), (0.0, 0.0, -0.0), (4.4779, 4.3499, 3.3536), "AB_Orc_Scaffolding_Foundation_3x3m_B24", _folder)
if a: placed += 1
else: skipped += 1

# Construction: AB_Orc_Scaffolding_Foundation_3x3m_B25
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Stone
#   Volume: EMorSimpleShape::OrientedBox, BoxExtent: (189.5, 189.2, 167.7)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (7097.8203, 6128.4604, 2389.8337), (0.0, 0.0, -0.0), (3.7891, 3.7835, 3.3536), "AB_Orc_Scaffolding_Foundation_3x3m_B25", _folder)
if a: placed += 1
else: skipped += 1

# Construction: AB_Orc_Scaffolding_Foundation_3x3m_B26
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Stone
#   Volume: EMorSimpleShape::OrientedBox, BoxExtent: (189.2, 189.5, 167.7)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (7084.2153, 6135.2896, 1489.8337), (0.0, 0.0, -0.0), (3.7835, 3.7891, 3.3536), "AB_Orc_Scaffolding_Foundation_3x3m_B26", _folder)
if a: placed += 1
else: skipped += 1

# Construction: AB_Orc_Scaffolding_Foundation_3x3m_B27
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Stone
#   Volume: EMorSimpleShape::OrientedBox, BoxExtent: (202.6, 187.1, 167.7)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (5789.252, 6134.231, 2329.8337), (0.0, 0.0, -0.0), (4.0520, 3.7428, 3.3536), "AB_Orc_Scaffolding_Foundation_3x3m_B27", _folder)
if a: placed += 1
else: skipped += 1

# Construction: AB_Orc_Scaffolding_Foundation_3x3m_B28
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Stone
#   Volume: EMorSimpleShape::OrientedBox, BoxExtent: (187.1, 202.6, 167.7)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (5792.1807, 6143.5605, 2049.8337), (0.0, 0.0, -0.0), (3.7428, 4.0520, 3.3536), "AB_Orc_Scaffolding_Foundation_3x3m_B28", _folder)
if a: placed += 1
else: skipped += 1

# Construction: AB_Orc_Scaffolding_Foundation_3x3m_B29
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Stone
#   Volume: EMorSimpleShape::OrientedBox, BoxExtent: (202.6, 187.1, 167.7)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (5794.08, 6132.937, 1779.8337), (0.0, 0.0, -0.0), (4.0520, 3.7428, 3.3536), "AB_Orc_Scaffolding_Foundation_3x3m_B29", _folder)
if a: placed += 1
else: skipped += 1

# Construction: AB_Orc_Scaffolding_Foundation_3x3m_B3
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Stone
#   Volume: EMorSimpleShape::OrientedBox, BoxExtent: (194.5, 194.4, 167.7)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (3968.513, 7885.9805, 1499.8337), (0.0, 0.0, -0.0), (3.8895, 3.8876, 3.3536), "AB_Orc_Scaffolding_Foundation_3x3m_B3", _folder)
if a: placed += 1
else: skipped += 1

# Construction: AB_Orc_Scaffolding_Foundation_3x3m_B30
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Stone
#   Volume: EMorSimpleShape::OrientedBox, BoxExtent: (187.1, 202.6, 167.7)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (5802.1143, 6125.1777, 1489.8337), (0.0, 0.0, -0.0), (3.7428, 4.0520, 3.3536), "AB_Orc_Scaffolding_Foundation_3x3m_B30", _folder)
if a: placed += 1
else: skipped += 1

# Construction: AB_Orc_Scaffolding_Foundation_3x3m_B31
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Stone
#   Volume: EMorSimpleShape::OrientedBox, BoxExtent: (217.0, 224.6, 167.7)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (4651.397, 6736.073, 1484.8337), (0.0, 0.0, -0.0), (4.3391, 4.4927, 3.3536), "AB_Orc_Scaffolding_Foundation_3x3m_B31", _folder)
if a: placed += 1
else: skipped += 1

# Construction: AB_Orc_Scaffolding_Foundation_3x3m_B32
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Stone
#   Volume: EMorSimpleShape::OrientedBox, BoxExtent: (224.6, 217.0, 167.7)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (4647.552, 6748.5117, 1779.8337), (0.0, 0.0, -0.0), (4.4927, 4.3391, 3.3536), "AB_Orc_Scaffolding_Foundation_3x3m_B32", _folder)
if a: placed += 1
else: skipped += 1

# Construction: AB_Orc_Scaffolding_Foundation_3x3m_B33
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Stone
#   Volume: EMorSimpleShape::OrientedBox, BoxExtent: (224.6, 217.0, 167.7)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (4647.552, 6748.5117, 2069.8337), (0.0, 0.0, -0.0), (4.4927, 4.3391, 3.3536), "AB_Orc_Scaffolding_Foundation_3x3m_B33", _folder)
if a: placed += 1
else: skipped += 1

# Construction: AB_Orc_Scaffolding_Foundation_3x3m_B34
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Stone
#   Volume: EMorSimpleShape::OrientedBox, BoxExtent: (217.0, 224.6, 167.7)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (4659.99, 6752.3574, 2364.8337), (0.0, 0.0, -0.0), (4.3391, 4.4927, 3.3536), "AB_Orc_Scaffolding_Foundation_3x3m_B34", _folder)
if a: placed += 1
else: skipped += 1

# Construction: AB_Orc_Scaffolding_Foundation_3x3m_B4
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Stone
#   Volume: EMorSimpleShape::OrientedBox, BoxExtent: (194.4, 194.5, 167.7)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (3974.6846, 7899.476, 2399.8337), (0.0, 0.0, -0.0), (3.8876, 3.8895, 3.3536), "AB_Orc_Scaffolding_Foundation_3x3m_B4", _folder)
if a: placed += 1
else: skipped += 1

# Construction: AB_Orc_Scaffolding_Foundation_3x3m_B5
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Stone
#   Volume: EMorSimpleShape::OrientedBox, BoxExtent: (217.5, 223.9, 167.7)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (4674.563, 10330.334, 1499.8337), (0.0, 0.0, -0.0), (4.3499, 4.4779, 3.3536), "AB_Orc_Scaffolding_Foundation_3x3m_B5", _folder)
if a: placed += 1
else: skipped += 1

# Construction: AB_Orc_Scaffolding_Foundation_3x3m_B6
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Stone
#   Volume: EMorSimpleShape::OrientedBox, BoxExtent: (223.9, 217.5, 167.7)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (4677.742, 10317.398, 2399.8337), (0.0, 0.0, -0.0), (4.4779, 4.3499, 3.3536), "AB_Orc_Scaffolding_Foundation_3x3m_B6", _folder)
if a: placed += 1
else: skipped += 1

# Construction: AB_Orc_Scaffolding_Foundation_3x3m_B7
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Stone
#   Volume: EMorSimpleShape::OrientedBox, BoxExtent: (217.5, 223.9, 167.7)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (4664.806, 10314.219, 2099.8337), (0.0, 0.0, -0.0), (4.3499, 4.4779, 3.3536), "AB_Orc_Scaffolding_Foundation_3x3m_B7", _folder)
if a: placed += 1
else: skipped += 1

# Construction: AB_Orc_Scaffolding_Foundation_3x3m_B8
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Stone
#   Volume: EMorSimpleShape::OrientedBox, BoxExtent: (223.9, 217.5, 167.7)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (4677.742, 10317.398, 1799.8337), (0.0, 0.0, -0.0), (4.4779, 4.3499, 3.3536), "AB_Orc_Scaffolding_Foundation_3x3m_B8", _folder)
if a: placed += 1
else: skipped += 1

# Construction: AB_Orc_Scaffolding_Foundation_3x3m_B9
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Stone
#   Volume: EMorSimpleShape::OrientedBox, BoxExtent: (187.1, 202.6, 167.7)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (7098.561, 10980.244, 1494.8337), (0.0, 0.0, -0.0), (3.7428, 4.0520, 3.3536), "AB_Orc_Scaffolding_Foundation_3x3m_B9", _folder)
if a: placed += 1
else: skipped += 1

# Construction: AB_Orc_Scaffolding_Foundation_3x3m_C_2
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Stone
#   Volume: EMorSimpleShape::OrientedBox, BoxExtent: (242.3, 201.7, 167.7)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (4049.6711, 9192.402, 1799.8337), (0.0, 0.0, -0.0), (4.8460, 4.0340, 3.3536), "AB_Orc_Scaffolding_Foundation_3x3m_C_2", _folder)
if a: placed += 1
else: skipped += 1

# Construction: AB_Orc_Scaffolding_Foundation_3x3m_C2
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Stone
#   Volume: EMorSimpleShape::OrientedBox, BoxExtent: (201.7, 242.3, 167.7)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (4016.374, 9176.227, 2099.8337), (0.0, 0.0, -0.0), (4.0340, 4.8460, 3.3536), "AB_Orc_Scaffolding_Foundation_3x3m_C2", _folder)
if a: placed += 1
else: skipped += 1

# Construction: AB_Orc_Scaffolding_Foundation_3x3m_C3
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Stone
#   Volume: EMorSimpleShape::OrientedBox, BoxExtent: (243.8, 204.3, 167.7)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (3952.7285, 7884.2676, 1799.8337), (0.0, 0.0, -0.0), (4.8757, 4.0869, 3.3536), "AB_Orc_Scaffolding_Foundation_3x3m_C3", _folder)
if a: placed += 1
else: skipped += 1

# Construction: AB_Orc_Scaffolding_Foundation_3x3m_C4
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Stone
#   Volume: EMorSimpleShape::OrientedBox, BoxExtent: (204.3, 243.8, 167.7)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (3972.972, 7915.2603, 2099.8337), (0.0, 0.0, -0.0), (4.0869, 4.8757, 3.3536), "AB_Orc_Scaffolding_Foundation_3x3m_C4", _folder)
if a: placed += 1
else: skipped += 1

# Construction: AB_Orc_Scaffolding_Foundation_3x3m_C5
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Stone
#   Volume: EMorSimpleShape::OrientedBox, BoxExtent: (196.2, 239.1, 167.7)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (7083.492, 6150.924, 1789.8337), (0.0, 0.0, -0.0), (3.9250, 4.7825, 3.3536), "AB_Orc_Scaffolding_Foundation_3x3m_C5", _folder)
if a: placed += 1
else: skipped += 1

# Construction: AB_Orc_Scaffolding_Foundation_3x3m_C6
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Stone
#   Volume: EMorSimpleShape::OrientedBox, BoxExtent: (239.1, 196.2, 167.7)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (7113.4546, 6129.184, 2089.8337), (0.0, 0.0, -0.0), (4.7825, 3.9250, 3.3536), "AB_Orc_Scaffolding_Foundation_3x3m_C6", _folder)
if a: placed += 1
else: skipped += 1

# Construction: AB_Orc_Scaffolding_Platform_1x1x2m_2
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Stone
#   Volume: EMorSimpleShape::OrientedBox, BoxExtent: (96.5, 89.7, 123.6)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (4873.4287, 10239.244, 2045.1443), (0.0, 0.0, -0.0), (1.9306, 1.7936, 2.4715), "AB_Orc_Scaffolding_Platform_1x1x2m_2", _folder)
if a: placed += 1
else: skipped += 1

# Construction: AB_Orc_Scaffolding_Platform_1x3x2m_5
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Stone
#   Volume: EMorSimpleShape::OrientedBox, BoxExtent: (116.1, 176.6, 123.6)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (4173.8447, 7954.71, 1349.8368), (0.0, 0.0, -0.0), (2.3228, 3.5330, 2.4715), "AB_Orc_Scaffolding_Platform_1x3x2m_5", _folder)
if a: placed += 1
else: skipped += 1

# Construction: AB_Orc_Scaffolding_Platform_3x1_No_Legs_2
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Scaffolding
#   Volume: EMorSimpleShape::OrientedBox, BoxExtent: (115.6, 166.0, 63.4)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (4191.633, 7964.312, 1318.0592), (0.0, 0.0, -0.0), (2.3121, 3.3196, 1.2673), "AB_Orc_Scaffolding_Platform_3x1_No_Legs_2", _folder)
if a: placed += 1
else: skipped += 1

# Construction: AB_Orc_Scaffolding_Platform_3x1_No_Legs10
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Scaffolding
#   Volume: EMorSimpleShape::OrientedBox, BoxExtent: (147.0, 168.8, 21.2)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (6268.8374, 5111.8213, 1346.4171), (0.0, 0.0, -0.0), (2.9400, 3.3753, 0.4244), "AB_Orc_Scaffolding_Platform_3x1_No_Legs10", _folder)
if a: placed += 1
else: skipped += 1

# Construction: AB_Orc_Scaffolding_Platform_3x1_No_Legs4
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Scaffolding
#   Volume: EMorSimpleShape::OrientedBox, BoxExtent: (167.1, 120.0, 50.1)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (4049.9478, 7743.506, 1358.1619), (0.0, 0.0, -0.0), (3.3413, 2.4001, 1.0019), "AB_Orc_Scaffolding_Platform_3x1_No_Legs4", _folder)
if a: placed += 1
else: skipped += 1

# Construction: AB_Orc_Scaffolding_Platform_3x1_No_Legs5
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Scaffolding
#   Volume: EMorSimpleShape::OrientedBox, BoxExtent: (151.3, 57.2, 77.8)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (3992.1033, 9079.038, 1411.3354), (0.0, 0.0, -0.0), (3.0261, 1.1438, 1.5552), "AB_Orc_Scaffolding_Platform_3x1_No_Legs5", _folder)
if a: placed += 1
else: skipped += 1

# Construction: AB_Orc_Scaffolding_Platform_3x1_No_Legs6
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Scaffolding
#   Volume: EMorSimpleShape::OrientedBox, BoxExtent: (57.2, 151.3, 77.8)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (6974.471, 10995.958, 1401.3345), (0.0, 0.0, -0.0), (1.1438, 3.0261, 1.5552), "AB_Orc_Scaffolding_Platform_3x1_No_Legs6", _folder)
if a: placed += 1
else: skipped += 1

# Construction: AB_Orc_Scaffolding_Platform_3x1_No_Legs7
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Scaffolding
#   Volume: EMorSimpleShape::OrientedBox, BoxExtent: (151.3, 57.2, 77.8)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (7138.1323, 11104.43, 1401.3345), (0.0, 0.0, -0.0), (3.0261, 1.1438, 1.5552), "AB_Orc_Scaffolding_Platform_3x1_No_Legs7", _folder)
if a: placed += 1
else: skipped += 1

# Construction: AB_Orc_Scaffolding_Platform_3x1_No_Legs8
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Scaffolding
#   Volume: EMorSimpleShape::OrientedBox, BoxExtent: (57.2, 151.3, 77.8)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (7215.7656, 10930.365, 1401.3345), (0.0, 0.0, -0.0), (1.1438, 3.0261, 1.5552), "AB_Orc_Scaffolding_Platform_3x1_No_Legs8", _folder)
if a: placed += 1
else: skipped += 1

# Construction: AB_Orc_Scaffolding_Platform_3x1_No_Legs9
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Scaffolding
#   Volume: EMorSimpleShape::OrientedBox, BoxExtent: (159.7, 163.1, 21.2)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (5432.683, 5257.783, 1343.4171), (0.0, 0.0, -0.0), (3.1949, 3.2624, 0.4244), "AB_Orc_Scaffolding_Platform_3x1_No_Legs9", _folder)
if a: placed += 1
else: skipped += 1

# Construction: AB_Orc_Scaffolding_Platform_3x1x3m_2
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Stone
#   Volume: EMorSimpleShape::OrientedBox, BoxExtent: (119.9, 177.1, 167.7)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (3859.5996, 9231.195, 1495.1664), (0.0, 0.0, -0.0), (2.3973, 3.5410, 3.3536), "AB_Orc_Scaffolding_Platform_3x1x3m_2", _folder)
if a: placed += 1
else: skipped += 1

# Construction: AB_Orc_Scaffolding_Platform_3x1x3m10
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Stone
#   Volume: EMorSimpleShape::OrientedBox, BoxExtent: (166.5, 161.7, 167.7)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (8060.3115, 10375.48, 2075.1663), (0.0, 0.0, -0.0), (3.3302, 3.2333, 3.3536), "AB_Orc_Scaffolding_Platform_3x1x3m10", _folder)
if a: placed += 1
else: skipped += 1

# Construction: AB_Orc_Scaffolding_Platform_3x1x3m11
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Stone
#   Volume: EMorSimpleShape::OrientedBox, BoxExtent: (109.9, 175.6, 167.7)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (8635.448, 9118.003, 2065.1663), (0.0, 0.0, -0.0), (2.1988, 3.5110, 3.3536), "AB_Orc_Scaffolding_Platform_3x1x3m11", _folder)
if a: placed += 1
else: skipped += 1

# Construction: AB_Orc_Scaffolding_Platform_3x1x3m12
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Stone
#   Volume: EMorSimpleShape::OrientedBox, BoxExtent: (119.9, 177.1, 167.7)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (8676.152, 7936.865, 1420.1664), (0.0, 0.0, -0.0), (2.3973, 3.5410, 3.3536), "AB_Orc_Scaffolding_Platform_3x1x3m12", _folder)
if a: placed += 1
else: skipped += 1

# Construction: AB_Orc_Scaffolding_Platform_3x1x3m13
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Stone
#   Volume: EMorSimpleShape::OrientedBox, BoxExtent: (161.7, 166.5, 167.7)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (8095.132, 6661.456, 1505.1664), (0.0, 0.0, -0.0), (3.2333, 3.3302, 3.3536), "AB_Orc_Scaffolding_Platform_3x1x3m13", _folder)
if a: placed += 1
else: skipped += 1

# Construction: AB_Orc_Scaffolding_Platform_3x1x3m14
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Stone
#   Volume: EMorSimpleShape::OrientedBox, BoxExtent: (161.7, 166.5, 167.7)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (8091.8076, 6644.634, 2095.1665), (0.0, 0.0, -0.0), (3.2333, 3.3302, 3.3536), "AB_Orc_Scaffolding_Platform_3x1x3m14", _folder)
if a: placed += 1
else: skipped += 1

# Construction: AB_Orc_Scaffolding_Platform_3x1x3m15_6
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Stone
#   Volume: EMorSimpleShape::OrientedBox, BoxExtent: (177.1, 119.9, 167.7)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (5828.368, 6323.37, 1420.1664), (0.0, 0.0, -0.0), (3.5410, 2.3973, 3.3536), "AB_Orc_Scaffolding_Platform_3x1x3m15_6", _folder)
if a: placed += 1
else: skipped += 1

# Construction: AB_Orc_Scaffolding_Platform_3x1x3m16
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Stone
#   Volume: EMorSimpleShape::OrientedBox, BoxExtent: (175.6, 109.9, 167.7)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (7053.2295, 6295.675, 1485.1664), (0.0, 0.0, -0.0), (3.5110, 2.1988, 3.3536), "AB_Orc_Scaffolding_Platform_3x1x3m16", _folder)
if a: placed += 1
else: skipped += 1

# Construction: AB_Orc_Scaffolding_Platform_3x1x3m17
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Stone
#   Volume: EMorSimpleShape::OrientedBox, BoxExtent: (163.9, 164.9, 167.7)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (4515.327, 6873.73, 1500.1664), (0.0, 0.0, -0.0), (3.2771, 3.2979, 3.3536), "AB_Orc_Scaffolding_Platform_3x1x3m17", _folder)
if a: placed += 1
else: skipped += 1

# Construction: AB_Orc_Scaffolding_Platform_3x1x3m18
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Stone
#   Volume: EMorSimpleShape::OrientedBox, BoxExtent: (163.9, 164.9, 167.7)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (4498.3647, 6876.343, 2090.1663), (0.0, 0.0, -0.0), (3.2771, 3.2979, 3.3536), "AB_Orc_Scaffolding_Platform_3x1x3m18", _folder)
if a: placed += 1
else: skipped += 1

# Construction: AB_Orc_Scaffolding_Platform_3x1x3m2
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Stone
#   Volume: EMorSimpleShape::OrientedBox, BoxExtent: (119.9, 177.1, 167.7)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (4189.0234, 9145.32, 1495.1664), (0.0, 0.0, -0.0), (2.3973, 3.5410, 3.3536), "AB_Orc_Scaffolding_Platform_3x1x3m2", _folder)
if a: placed += 1
else: skipped += 1

# Construction: AB_Orc_Scaffolding_Platform_3x1x3m3
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Stone
#   Volume: EMorSimpleShape::OrientedBox, BoxExtent: (116.1, 176.6, 167.7)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (4164.209, 7962.8564, 1495.1664), (0.0, 0.0, -0.0), (2.3228, 3.5327, 3.3536), "AB_Orc_Scaffolding_Platform_3x1x3m3", _folder)
if a: placed += 1
else: skipped += 1

# Construction: AB_Orc_Scaffolding_Platform_3x1x3m4
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Stone
#   Volume: EMorSimpleShape::OrientedBox, BoxExtent: (161.7, 166.5, 167.7)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (4560.0356, 10192.051, 1495.1664), (0.0, 0.0, -0.0), (3.2333, 3.3301, 3.3536), "AB_Orc_Scaffolding_Platform_3x1x3m4", _folder)
if a: placed += 1
else: skipped += 1

# Construction: AB_Orc_Scaffolding_Platform_3x1x3m5
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Stone
#   Volume: EMorSimpleShape::OrientedBox, BoxExtent: (161.7, 166.5, 167.7)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (4800.491, 10438.367, 1495.1664), (0.0, 0.0, -0.0), (3.2333, 3.3302, 3.3536), "AB_Orc_Scaffolding_Platform_3x1x3m5", _folder)
if a: placed += 1
else: skipped += 1

# Construction: AB_Orc_Scaffolding_Platform_3x1x3m6
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Stone
#   Volume: EMorSimpleShape::OrientedBox, BoxExtent: (116.1, 176.6, 167.7)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (5681.8335, 10776.529, 1495.1664), (0.0, 0.0, -0.0), (2.3228, 3.5327, 3.3536), "AB_Orc_Scaffolding_Platform_3x1x3m6", _folder)
if a: placed += 1
else: skipped += 1

# Construction: AB_Orc_Scaffolding_Platform_3x1x3m7
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Stone
#   Volume: EMorSimpleShape::OrientedBox, BoxExtent: (116.1, 176.6, 167.7)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (6003.742, 10898.472, 1495.1664), (0.0, 0.0, -0.0), (2.3228, 3.5327, 3.3536), "AB_Orc_Scaffolding_Platform_3x1x3m7", _folder)
if a: placed += 1
else: skipped += 1

# Construction: AB_Orc_Scaffolding_Platform_3x1x3m8
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Stone
#   Volume: EMorSimpleShape::OrientedBox, BoxExtent: (177.1, 119.9, 167.7)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (7072.3076, 10782.053, 2070.1663), (0.0, 0.0, -0.0), (3.5410, 2.3973, 3.3536), "AB_Orc_Scaffolding_Platform_3x1x3m8", _folder)
if a: placed += 1
else: skipped += 1

# Construction: AB_Orc_Scaffolding_Platform_3x1x3m9
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Stone
#   Volume: EMorSimpleShape::OrientedBox, BoxExtent: (166.5, 161.7, 167.7)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (8043.4893, 10378.805, 1485.1664), (0.0, 0.0, -0.0), (3.3302, 3.2333, 3.3536), "AB_Orc_Scaffolding_Platform_3x1x3m9", _folder)
if a: placed += 1
else: skipped += 1

# Construction: BP_BoneHoardColumn_Large10_32
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Stone
#   Volume: EMorSimpleShape::Empty, BoxExtent: (100.0, 100.0, 100.0)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (7097.8657, 10964.869, 2049.0), (0.0, 165.0001259867028, -0.0), (2.0000, 2.0000, 2.0000), "BP_BoneHoardColumn_Large10_32", _folder)
if a: placed += 1
else: skipped += 1

# Construction: BP_BoneHoardColumn_Large11_35
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Stone
#   Volume: EMorSimpleShape::Empty, BoxExtent: (100.0, 100.0, 100.0)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (8816.04, 9188.555, 2052.0), (0.0, 105.99999900725344, -0.0), (2.0000, 2.0000, 2.0000), "BP_BoneHoardColumn_Large11_35", _folder)
if a: placed += 1
else: skipped += 1

# Construction: BP_BoneHoardColumn_Large12_38
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Stone
#   Volume: EMorSimpleShape::Empty, BoxExtent: (100.0, 100.0, 100.0)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (8219.0, 6781.0, 2051.0), (0.0, 44.99999866815529, -0.0), (2.0000, 2.0000, 2.0000), "BP_BoneHoardColumn_Large12_38", _folder)
if a: placed += 1
else: skipped += 1

# Construction: BP_BoneHoardColumn_Large13_41
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Stone
#   Volume: EMorSimpleShape::Empty, BoxExtent: (100.0, 100.0, 100.0)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (4645.0, 6746.0, 2051.0), (-0.0, -44.99999680766002, -0.0), (2.0000, 2.0000, 2.0000), "BP_BoneHoardColumn_Large13_41", _folder)
if a: placed += 1
else: skipped += 1

# Construction: BP_BoneHoardColumn_Large14_44
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Stone
#   Volume: EMorSimpleShape::Empty, BoxExtent: (100.0, 100.0, 100.0)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (3985.2046, 7890.21, 2049.0), (-0.0, -75.00015435969866, -0.0), (2.0000, 2.0000, 2.0000), "BP_BoneHoardColumn_Large14_44", _folder)
if a: placed += 1
else: skipped += 1

# Construction: BP_BoneHoardColumn_Large9_29
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Stone
#   Volume: EMorSimpleShape::Empty, BoxExtent: (100.0, 100.0, 100.0)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (4682.0, 10319.0, 2051.0), (0.0, -135.0000303901233, -0.0), (2.0000, 2.0000, 2.0000), "BP_BoneHoardColumn_Large9_29", _folder)
if a: placed += 1
else: skipped += 1

# Construction: BP_BoneHoardColumnA_Large_2
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Stone
#   Volume: EMorSimpleShape::Empty, BoxExtent: (100.0, 100.0, 100.0)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (4031.66, 9198.768, 2050.0), (-0.0, -105.00012581147602, -0.0), (2.0000, 2.0000, 2.0000), "BP_BoneHoardColumnA_Large_2", _folder)
if a: placed += 1
else: skipped += 1

# Construction: BP_BoneHoardColumnA_Large12_35
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Stone
#   Volume: EMorSimpleShape::Empty, BoxExtent: (100.0, 100.0, 100.0)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (8181.0, 10280.0, 2050.0), (0.0, 135.00006074169625, -0.0), (2.0000, 2.0000, 2.0000), "BP_BoneHoardColumnA_Large12_35", _folder)
if a: placed += 1
else: skipped += 1

# Construction: BP_BoneHoardColumnA_Large13
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Stone
#   Volume: EMorSimpleShape::Empty, BoxExtent: (100.0, 100.0, 100.0)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (5821.2983, 10919.313, 2050.0), (0.0, -163.1249530290677, -0.0), (2.0000, 2.0000, 2.0000), "BP_BoneHoardColumnA_Large13", _folder)
if a: placed += 1
else: skipped += 1

# Construction: BP_BoneHoardColumnA_Large4_11
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Stone
#   Volume: EMorSimpleShape::Empty, BoxExtent: (100.0, 100.0, 100.0)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (5799.6304, 6132.682, 2049.0), (-0.0, -15.000109016036971, -0.0), (2.0000, 2.0000, 2.0000), "BP_BoneHoardColumnA_Large4_11", _folder)
if a: placed += 1
else: skipped += 1

# Construction: BP_BoneHoardColumnA_Large6_17
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Stone
#   Volume: EMorSimpleShape::Empty, BoxExtent: (100.0, 100.0, 100.0)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (7097.222, 6135.224, 2050.0), (0.0, 14.999921131575023, -0.0), (2.0000, 2.0000, 2.0000), "BP_BoneHoardColumnA_Large6_17", _folder)
if a: placed += 1
else: skipped += 1

# Construction: BP_BoneHoardColumnA_Large8_23
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Stone
#   Volume: EMorSimpleShape::Empty, BoxExtent: (100.0, 100.0, 100.0)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (8863.893, 7903.4253, 2051.0), (0.0, 75.00003380892639, -0.0), (2.0000, 2.0000, 2.0000), "BP_BoneHoardColumnA_Large8_23", _folder)
if a: placed += 1
else: skipped += 1

# Construction: Orc_Scaffolding_Beam_3m_5
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Scaffolding
#   Volume: EMorSimpleShape::OrientedBox, BoxExtent: (114.0, 174.7, 41.7)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (3801.9724, 7856.573, 1360.0214), (0.0, 0.0, -0.0), (2.2809, 3.4933, 0.8337), "Orc_Scaffolding_Beam_3m_5", _folder)
if a: placed += 1
else: skipped += 1

# Construction: Orc_Scaffolding_Beam_3m2
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Scaffolding
#   Volume: EMorSimpleShape::OrientedBox, BoxExtent: (177.4, 133.1, 50.0)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (3907.5564, 8051.7593, 1365.6622), (0.0, 0.0, -0.0), (3.5488, 2.6611, 1.0004), "Orc_Scaffolding_Beam_3m2", _folder)
if a: placed += 1
else: skipped += 1

# Construction: Orc_Scaffolding_Beam_3m3
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Scaffolding
#   Volume: EMorSimpleShape::OrientedBox, BoxExtent: (109.0, 174.0, 23.8)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (3840.7744, 9238.517, 1353.971), (0.0, 0.0, -0.0), (2.1803, 3.4806, 0.4769), "Orc_Scaffolding_Beam_3m3", _folder)
if a: placed += 1
else: skipped += 1

# Construction: Orc_Scaffolding_Beam_3m4
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Scaffolding
#   Volume: EMorSimpleShape::OrientedBox, BoxExtent: (173.8, 148.9, 59.4)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (4221.817, 9303.408, 1327.8967), (0.0, 0.0, -0.0), (3.4765, 2.9786, 1.1885), "Orc_Scaffolding_Beam_3m4", _folder)
if a: placed += 1
else: skipped += 1

# Construction: Orc_Scaffolding_Beam_3m5
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Scaffolding
#   Volume: EMorSimpleShape::OrientedBox, BoxExtent: (131.1, 131.1, 69.6)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (4592.863, 10238.496, 1690.717), (0.0, 0.0, -0.0), (2.6215, 2.6215, 1.3918), "Orc_Scaffolding_Beam_3m5", _folder)
if a: placed += 1
else: skipped += 1

# ======================================================================
# PHASE 3: Breakables + DecoVolumes
# ======================================================================
unreal.log(f"[{BUBBLE_NAME}] Phase 3: Placing breakables and deco volumes...")

_folder = "Reconstruction/BD_BB_Chapter5_BoneHoard/Breakables"

# Breakable Batch 0: BP_Orc_Scaffolding_Post_1m_A (20 instances)
#   BP Class: /Game/LevelDesign/Architecture/Orc/BP_Orc_Scaffolding_Post_1m_A
_brk_mesh = "/Game/Art/Assets/Kits/Deco_Architecture/Orc_Camp/Orc_Scaffolding_Post_1m_A"
_brk_mats = ['/Game/Art/Assets/Kits/Deco_Architecture/Orc_Camp/Materials/MI_Orc_Scaffolding_Poles']
a = spawn_static_mesh(_brk_mesh, _brk_mats, (3988.0, 8715.0, 1347.0), (1.2020951638745592, -64.71432996658102, -92.5429462114577), (1.0, 1.0, 1.0), "BP_Orc_Scaffolding_Post_1m_A_2", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_brk_mesh, _brk_mats, (8957.001, 8493.631, 1346.9904), (-2.622040013722569, -5.182861118824365, -89.48406750901876), (1.0, 1.0, 1.0), "BP_Orc_Scaffolding_Post_1m_A10", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_brk_mesh, _brk_mats, (9066.336, 7805.333, 1356.9703), (-2.622040521607226, 163.56717704184578, -95.10895074397364), (1.0, 1.0, 1.0), "BP_Orc_Scaffolding_Post_1m_A11", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_brk_mesh, _brk_mats, (8779.354, 6831.735, 1341.9904), (-2.6220400839758757, 20.12952805517522, -89.4838115104488), (1.0, 1.0, 1.0), "BP_Orc_Scaffolding_Post_1m_A12", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_brk_mesh, _brk_mats, (5036.791, 6305.419, 1346.9904), (-2.62201112635914, -126.12029451300829, -89.48387262784344), (1.0, 1.0, 1.0), "BP_Orc_Scaffolding_Post_1m_A13", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_brk_mesh, _brk_mats, (3972.519, 7513.229, 1350.7363), (0.5611515185739718, -112.19839042021087, -92.918307663877), (1.0, 1.0, 1.0), "BP_Orc_Scaffolding_Post_1m_A14", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_brk_mesh, _brk_mats, (7668.414, 6375.903, 1344.9904), (-2.6220385156603596, 101.69208434043108, -89.4839753807203), (1.0, 1.0, 1.0), "BP_Orc_Scaffolding_Post_1m_A15", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_brk_mesh, _brk_mats, (7817.336, 6205.333, 1351.9703), (-3.3424692058672067, -97.97588672446102, -94.67013889777141), (1.0, 1.0, 1.0), "BP_Orc_Scaffolding_Post_1m_A16", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_brk_mesh, _brk_mats, (7872.336, 6514.333, 1346.9703), (1.6693637821634453, 138.19384377459033, -87.84225764252925), (1.0, 1.0, 1.0), "BP_Orc_Scaffolding_Post_1m_A17", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_brk_mesh, _brk_mats, (7263.532, 6289.825, 1340.411), (-2.622039462630908, 155.1299324516782, -92.29625632491022), (1.0, 1.0, 1.0), "BP_Orc_Scaffolding_Post_1m_A18", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_brk_mesh, _brk_mats, (6614.972, 6045.4775, 1347.9904), (-2.621980078437998, -47.37026630684789, -89.48349319935393), (1.0, 1.0, 1.0), "BP_Orc_Scaffolding_Post_1m_A19", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_brk_mesh, _brk_mats, (4352.3203, 9595.084, 1339.9728), (-2.622039699559235, -5.182860764002408, -100.7344901259686), (1.0, 1.0, 1.0), "BP_Orc_Scaffolding_Post_1m_A2", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_brk_mesh, _brk_mats, (6567.1978, 6507.3135, 1260.9838), (-2.621980078437998, -47.37026630684789, -89.48349319935393), (1.0, 1.0, 1.0), "BP_Orc_Scaffolding_Post_1m_A20", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_brk_mesh, _brk_mats, (5440.0, 10974.0, 1381.0), (0.0, 0.0, -81.56243747610303), (1.0, 1.0, 1.0), "BP_Orc_Scaffolding_Post_1m_A3_8", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_brk_mesh, _brk_mats, (6990.512, 11218.39, 1349.0974), (-6.076199218852102, 117.99189052330651, -88.49206573540654), (1.0, 1.0, 1.0), "BP_Orc_Scaffolding_Post_1m_A4", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_brk_mesh, _brk_mats, (7394.0, 11034.0, 1370.0), (0.0, 0.0, -78.75000319333631), (1.0, 1.0, 1.0), "BP_Orc_Scaffolding_Post_1m_A5_12", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_brk_mesh, _brk_mats, (7889.0, 10802.0, 1344.0), (6.128360610381982e-05, -19.687256647610287, -89.99988542096538), (1.0, 1.0, 1.0), "BP_Orc_Scaffolding_Post_1m_A6_15", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_brk_mesh, _brk_mats, (7565.0, 10888.0, 1388.0), (-6.577147800031774, -62.59364253259392, 99.64480895588997), (1.0, 1.0, 1.0), "BP_Orc_Scaffolding_Post_1m_A7_18", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_brk_mesh, _brk_mats, (8607.018, 10172.869, 1345.9998), (0.00026795359882248544, 81.56240916575676, -84.37427404172021), (1.0, 1.0, 1.0), "BP_Orc_Scaffolding_Post_1m_A8", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_brk_mesh, _brk_mats, (9041.324, 9475.258, 1347.0), (-0.0006411896387952273, -135.00049603546248, 89.99994155151732), (1.0, 1.0, 1.0), "BP_Orc_Scaffolding_Post_1m_A9", _folder)
if a: placed += 1
else: skipped += 1

# Breakable Batch 1: BP_Orc_Scaffolding_Post_1m_C (14 instances)
#   BP Class: /Game/LevelDesign/Architecture/Orc/BP_Orc_Scaffolding_Post_1m_C
_brk_mesh = "/Game/Art/Assets/Kits/Deco_Architecture/Orc_Camp/Orc_Scaffolding_Post_1m_C"
_brk_mats = ['/Game/Art/Assets/Kits/Deco_Architecture/Orc_Camp/Materials/MI_Orc_Scaffolding_Poles']
a = spawn_static_mesh(_brk_mesh, _brk_mats, (3959.0, 8236.0, 1348.0), (-6.723632126473294e-12, 179.99967898101693, -89.99993012368576), (1.0, 1.0, 1.0), "BP_Orc_Scaffolding_Post_1m_C_2", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_brk_mesh, _brk_mats, (4481.0996, 7393.6797, 1272.764), (1.4740277783299182e-05, -154.68762595269394, -95.62442486628693), (1.0, 1.0, 1.0), "BP_Orc_Scaffolding_Post_1m_C10", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_brk_mesh, _brk_mats, (7643.2056, 6112.7754, 1345.5287), (-1.2864372108151723, -157.46207556791538, -90.46026846950461), (1.0, 1.0, 1.0), "BP_Orc_Scaffolding_Post_1m_C11", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_brk_mesh, _brk_mats, (7975.6006, 6588.2725, 1350.0547), (-3.370514758113776, 47.773396863393, -88.5700400317306), (1.0, 1.0, 1.0), "BP_Orc_Scaffolding_Post_1m_C12", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_brk_mesh, _brk_mats, (6419.869, 5908.6035, 1343.0547), (-1.2864382258638347, -157.46226664162086, -90.46027856358563), (1.0, 1.0, 1.0), "BP_Orc_Scaffolding_Post_1m_C13", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_brk_mesh, _brk_mats, (6438.767, 6396.5015, 1265.0531), (-1.286437828517767, -115.27475450066537, -90.46023471615321), (1.0, 1.0, 1.0), "BP_Orc_Scaffolding_Post_1m_C14", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_brk_mesh, _brk_mats, (4332.9097, 9889.249, 1346.0005), (1.786724205215712e-07, -36.562744098796294, -89.99987932818873), (1.0, 1.0, 1.0), "BP_Orc_Scaffolding_Post_1m_C2", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_brk_mesh, _brk_mats, (5140.0, 10893.0, 1347.0), (2.945696337605395e-07, 14.062547976555356, -89.99993918921096), (1.0, 1.0, 1.0), "BP_Orc_Scaffolding_Post_1m_C3_8", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_brk_mesh, _brk_mats, (6734.273, 10737.06, 1311.194), (-16.206147649239778, -158.06309026892419, -93.83698118728661), (1.0, 1.0, 1.0), "BP_Orc_Scaffolding_Post_1m_C4", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_brk_mesh, _brk_mats, (7512.0, 11120.0, 1364.0), (0.0, 0.0, -73.12499866925161), (1.0, 1.0, 1.0), "BP_Orc_Scaffolding_Post_1m_C5_12", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_brk_mesh, _brk_mats, (9026.219, 8634.415, 1350.0547), (-1.2864389116905923, 95.66286712205851, -90.46029745909642), (1.0, 1.0, 1.0), "BP_Orc_Scaffolding_Post_1m_C6", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_brk_mesh, _brk_mats, (9054.598, 7493.5537, 1347.7943), (-1.3251937834164826, -129.34461598105239, -78.41678363600047), (1.0, 1.0, 1.0), "BP_Orc_Scaffolding_Post_1m_C7", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_brk_mesh, _brk_mats, (8800.763, 6879.996, 1345.4697), (-1.3253176706505017, 140.6538545697687, -89.66786519887748), (1.0, 1.0, 1.0), "BP_Orc_Scaffolding_Post_1m_C8", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_brk_mesh, _brk_mats, (5121.96, 6173.672, 1350.0547), (-1.2864371476559537, -25.27478372675023, -90.46027243781829), (1.0, 1.0, 1.0), "BP_Orc_Scaffolding_Post_1m_C9", _folder)
if a: placed += 1
else: skipped += 1

# Breakable Batch 2: BP_Orc_Scaffolding_Post_1m_D (3 instances)
#   BP Class: /Game/LevelDesign/Architecture/Orc/BP_Orc_Scaffolding_Post_1m_D
_brk_mesh = "/Game/Art/Assets/Kits/Deco_Architecture/Orc_Camp/Orc_Scaffolding_Post_1m_D"
_brk_mats = ['/Game/Art/Assets/Kits/Deco_Architecture/Orc_Camp/Materials/MI_Orc_Scaffolding_Poles']
a = spawn_static_mesh(_brk_mesh, _brk_mats, (5470.0, 10659.0, 1399.0), (2.922107445296518e-06, -118.12469920372548, -89.99968156719315), (1.0, 1.0, 1.0), "BP_Orc_Scaffolding_Post_1m_D_4", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_brk_mesh, _brk_mats, (6044.5, 11155.875, 1341.5278), (14.150420086205415, 71.5498641333716, -80.79388440165627), (1.0, 1.0, 1.0), "BP_Orc_Scaffolding_Post_1m_D2", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_brk_mesh, _brk_mats, (7564.0, 10956.0, 1386.0), (87.18719744960046, 14.062491619402376, 1.3849599085279202e-05), (1.0, 1.0, 1.0), "BP_Orc_Scaffolding_Post_1m_D3_8", _folder)
if a: placed += 1
else: skipped += 1

# Breakable Batch 3: BP_Orc_Scaffolding_Post_2m_A (2 instances)
#   BP Class: /Game/LevelDesign/Architecture/Orc/BP_Orc_Scaffolding_Post_2m_A
_brk_mesh = "/Game/Art/Assets/Kits/Deco_Architecture/Orc_Camp/Orc_Scaffolding_Post_2m_A"
_brk_mats = ['/Game/Art/Assets/Kits/Deco_Architecture/Orc_Camp/Materials/MI_Orc_Scaffolding_Poles']
a = spawn_static_mesh(_brk_mesh, _brk_mats, (5273.958, 10748.363, 1363.5137), (5.277136021579232, 98.89726449261902, -77.2363869376435), (1.0, 1.0, 1.0), "BP_Orc_Scaffolding_Post_2m_A_4", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_brk_mesh, _brk_mats, (6271.449, 11252.5625, 1351.2377), (-0.7633977731213764, -73.1966646797092, -92.96295892837482), (1.0, 1.0, 1.0), "BP_Orc_Scaffolding_Post_2m_A2", _folder)
if a: placed += 1
else: skipped += 1

# Breakable Batch 4: BP_Orc_Scaffolding_Post_2m_B (3 instances)
#   BP Class: /Game/LevelDesign/Architecture/Orc/BP_Orc_Scaffolding_Post_2m_B
_brk_mesh = "/Game/Art/Assets/Kits/Deco_Architecture/Orc_Camp/Orc_Scaffolding_Post_2m_B"
_brk_mats = ['/Game/Art/Assets/Kits/Deco_Architecture/Orc_Camp/Materials/MI_Orc_Scaffolding_Poles']
a = spawn_static_mesh(_brk_mesh, _brk_mats, (5598.0, 10981.0, 1353.0), (2.922107445296518e-06, -118.12469920372548, -89.99968156719315), (1.0, 1.0, 1.0), "BP_Orc_Scaffolding_Post_2m_B_4", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_brk_mesh, _brk_mats, (6727.389, 11042.004, 1343.2567), (14.150422064865001, 71.54980914296449, -89.23113863968473), (1.0, 1.0, 1.0), "BP_Orc_Scaffolding_Post_2m_B2", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_brk_mesh, _brk_mats, (8134.0, 10610.0, 1347.0), (-90.0, -6.69463600963901, -10.180667551961342), (1.0, 1.0, 1.0), "BP_Orc_Scaffolding_Post_2m_B3_8", _folder)
if a: placed += 1
else: skipped += 1

# Breakable Batch 5: BP_Orc_Scaffolding_Post_2m_C (11 instances)
#   BP Class: /Game/LevelDesign/Architecture/Orc/BP_Orc_Scaffolding_Post_2m_C
_brk_mesh = "/Game/Art/Assets/Kits/Deco_Architecture/Orc_Camp/Orc_Scaffolding_Post_2m_C"
_brk_mats = ['/Game/Art/Assets/Kits/Deco_Architecture/Orc_Camp/Materials/MI_Orc_Scaffolding_Poles']
a = spawn_static_mesh(_brk_mesh, _brk_mats, (4342.0, 8329.0, 1300.0), (39.28999594437108, 166.3679835867086, 66.73286096658073), (1.0, 1.0, 1.0), "BP_Orc_Scaffolding_Post_2m_C_2", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_brk_mesh, _brk_mats, (8166.285, 6340.2573, 1341.0), (40.77211548986732, -9.798552426791424, 81.33715810172617), (1.0, 1.0, 1.0), "BP_Orc_Scaffolding_Post_2m_C10", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_brk_mesh, _brk_mats, (6032.2036, 5831.776, 1340.0), (41.192422310481305, 17.9302658439438, 85.02123182840462), (1.0, 1.0, 1.0), "BP_Orc_Scaffolding_Post_2m_C11", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_brk_mesh, _brk_mats, (4312.963, 10078.903, 1346.0), (41.19240002023541, -63.632015512019564, 85.02126670116124), (1.0, 1.0, 1.0), "BP_Orc_Scaffolding_Post_2m_C2", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_brk_mesh, _brk_mats, (5980.0, 11154.0, 1346.0), (2.922107445296518e-06, -118.12469920372548, -89.99968156719315), (1.0, 1.0, 1.0), "BP_Orc_Scaffolding_Post_2m_C3_8", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_brk_mesh, _brk_mats, (6272.803, 10670.274, 1312.8693), (-81.72044332488025, -51.26650844044717, 33.610703682413984), (1.0, 1.0, 1.0), "BP_Orc_Scaffolding_Post_2m_C4", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_brk_mesh, _brk_mats, (7631.0, 11110.0, 1364.0), (38.915912062929856, -155.3107812145068, 88.26157443982306), (1.0, 1.0, 1.0), "BP_Orc_Scaffolding_Post_2m_C5_12", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_brk_mesh, _brk_mats, (8748.559, 9900.222, 1367.206), (38.670648501162766, -6.671201843415705, 95.0573188270054), (1.0, 1.0, 1.0), "BP_Orc_Scaffolding_Post_2m_C6", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_brk_mesh, _brk_mats, (8917.963, 8976.903, 1343.0), (41.19240002023541, -63.632015512019564, 85.02126670116124), (1.0, 1.0, 1.0), "BP_Orc_Scaffolding_Post_2m_C7", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_brk_mesh, _brk_mats, (5471.377, 6090.451, 1343.0), (41.19241636354341, 175.4305243370896, 85.02123613000211), (1.0, 1.0, 1.0), "BP_Orc_Scaffolding_Post_2m_C8", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_brk_mesh, _brk_mats, (4556.7637, 7753.868, 1277.7635), (40.90803346427985, -174.39509607363956, 96.21094696611145), (1.0, 1.0, 1.0), "BP_Orc_Scaffolding_Post_2m_C9", _folder)
if a: placed += 1
else: skipped += 1

# Breakable Batch 6: BP_Orc_Scaffolding_Post_2m_D (20 instances)
#   BP Class: /Game/LevelDesign/Architecture/Orc/BP_Orc_Scaffolding_Post_2m_D
_brk_mesh = "/Game/Art/Assets/Kits/Deco_Architecture/Orc_Camp/Orc_Scaffolding_Post_2m_D"
_brk_mats = ['/Game/Art/Assets/Kits/Deco_Architecture/Orc_Camp/Materials/MI_Orc_Scaffolding_Poles']
a = spawn_static_mesh(_brk_mesh, _brk_mats, (4263.0, 8450.0, 1282.0), (0.3091885305183053, -15.652069570607251, 75.26061729649028), (1.0, 1.0, 1.0), "BP_Orc_Scaffolding_Post_2m_D_2", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_brk_mesh, _brk_mats, (9121.255, 7789.79, 1354.7742), (5.8329682450570415, -35.41030657979832, -84.03350260203507), (1.0, 1.0, 1.0), "BP_Orc_Scaffolding_Post_2m_D10", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_brk_mesh, _brk_mats, (5296.828, 5991.2563, 1347.0804), (0.309204427719625, -18.464570771529186, 86.51026961968093), (1.0, 1.0, 1.0), "BP_Orc_Scaffolding_Post_2m_D11", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_brk_mesh, _brk_mats, (5069.532, 6351.955, 1348.7742), (5.832939210622313, 34.90203808295997, -86.84622284019324), (1.0, 1.0, 1.0), "BP_Orc_Scaffolding_Post_2m_D12", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_brk_mesh, _brk_mats, (4542.3374, 7183.132, 1299.4271), (1.8231565002368801, -15.55114849687242, 94.74132314553981), (1.0, 1.0, 1.0), "BP_Orc_Scaffolding_Post_2m_D13", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_brk_mesh, _brk_mats, (4072.0483, 7466.0635, 1351.1963), (29.7088473553997, -44.84682445694164, -90.58497850107966), (1.0, 1.0, 1.0), "BP_Orc_Scaffolding_Post_2m_D14", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_brk_mesh, _brk_mats, (7487.0215, 6225.5605, 1342.9178), (-0.7165215081361186, -167.49570349086127, 86.57051606061081), (1.0, 1.0, 1.0), "BP_Orc_Scaffolding_Post_2m_D15", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_brk_mesh, _brk_mats, (7680.908, 6320.3916, 1346.7742), (5.832941787000862, -97.28520270366661, -86.84625034686492), (1.0, 1.0, 1.0), "BP_Orc_Scaffolding_Post_2m_D16", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_brk_mesh, _brk_mats, (7770.782, 6581.1846, 1341.0804), (21.536557079731214, 4.661066608132787, 64.84295206684794), (1.0, 1.0, 1.0), "BP_Orc_Scaffolding_Post_2m_D17", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_brk_mesh, _brk_mats, (6140.2754, 5971.538, 1342.0804), (0.3092036120170239, -150.6521180154395, 86.51024081243523), (1.0, 1.0, 1.0), "BP_Orc_Scaffolding_Post_2m_D18", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_brk_mesh, _brk_mats, (6624.532, 5945.955, 1351.7742), (3.510358019908428, -24.579468817813275, -91.98664429928893), (1.0, 1.0, 1.0), "BP_Orc_Scaffolding_Post_2m_D19", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_brk_mesh, _brk_mats, (3980.1162, 9005.223, 1391.4785), (58.28441041490856, -12.348908445234619, -104.71199229987121), (1.0, 1.0, 1.0), "BP_Orc_Scaffolding_Post_2m_D2_5", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_brk_mesh, _brk_mats, (6021.964, 6076.967, 1358.9088), (-12.451203724920186, -28.205720878657527, 110.58624061875163), (1.0, 1.0, 1.0), "BP_Orc_Scaffolding_Post_2m_D20", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_brk_mesh, _brk_mats, (4331.308, 9983.49, 1345.0769), (0.309201964842283, 102.47313732180247, 89.32275571574513), (1.0, 1.0, 1.0), "BP_Orc_Scaffolding_Post_2m_D3", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_brk_mesh, _brk_mats, (3875.111, 9455.133, 1355.4327), (58.89189426367742, 111.04654133800648, -100.21341949846014), (1.0, 1.0, 1.0), "BP_Orc_Scaffolding_Post_2m_D4", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_brk_mesh, _brk_mats, (5498.558, 11141.966, 1348.2341), (4.045062397583973, -30.460145600282882, -79.33154012339419), (1.0, 1.0, 1.0), "BP_Orc_Scaffolding_Post_2m_D5_12", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_brk_mesh, _brk_mats, (6806.3345, 10830.992, 1314.9218), (-4.424071894400006, 158.02091727080887, -64.77513538123067), (1.0, 1.0, 1.0), "BP_Orc_Scaffolding_Post_2m_D6", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_brk_mesh, _brk_mats, (7695.0, 10154.0, 1298.0), (-42.124754611451706, 2.54640791067639, 83.39415030594837), (1.0, 1.0, 1.0), "BP_Orc_Scaffolding_Post_2m_D7_16", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_brk_mesh, _brk_mats, (9092.782, 8878.185, 1347.0804), (0.30920432909698053, 102.47317754159886, 86.51026388418742), (1.0, 1.0, 1.0), "BP_Orc_Scaffolding_Post_2m_D8", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_brk_mesh, _brk_mats, (8900.255, 8497.79, 1348.7742), (5.832940219380389, 155.83964591067152, -86.84628235187725), (1.0, 1.0, 1.0), "BP_Orc_Scaffolding_Post_2m_D9", _folder)
if a: placed += 1
else: skipped += 1

# Breakable Batch 7: BP_Orc_Scaffolding_Post_3m_B (11 instances)
#   BP Class: /Game/LevelDesign/Architecture/Orc/BP_Orc_Scaffolding_Post_3m_B
_brk_mesh = "/Game/Art/Assets/Kits/Deco_Architecture/Orc_Camp/Orc_Scaffolding_Post_3m_B"
_brk_mats = ['/Game/Art/Assets/Kits/Deco_Architecture/Orc_Camp/Materials/MI_Orc_Scaffolding_Poles']
a = spawn_static_mesh(_brk_mesh, _brk_mats, (3974.7168, 8133.409, 1341.9082), (88.95733795828814, -29.683885208759147, -20.019570599858376), (1.0, 1.0, 1.0), "BP_Orc_Scaffolding_Post_3m_B_2", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_brk_mesh, _brk_mats, (7666.0615, 6637.1772, 1336.293), (3.3795164800933573, 172.77315159703778, 86.89629500892663), (1.0, 1.0, 1.0), "BP_Orc_Scaffolding_Post_3m_B10", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_brk_mesh, _brk_mats, (6640.9805, 6296.669, 1270.293), (5.446373559378946, 144.7760587788293, 73.29827053986854), (1.0, 1.0, 1.0), "BP_Orc_Scaffolding_Post_3m_B11", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_brk_mesh, _brk_mats, (4746.396, 9842.65, 1314.0919), (88.95619811221286, 74.38035826621947, -20.01778573907927), (1.0, 1.0, 1.0), "BP_Orc_Scaffolding_Post_3m_B2", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_brk_mesh, _brk_mats, (5537.1504, 10974.107, 1359.0), (4.678153416318342e-06, 126.5625617654533, -92.81235979234836), (1.0, 1.0, 1.0), "BP_Orc_Scaffolding_Post_3m_B3_8", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_brk_mesh, _brk_mats, (6680.003, 10713.193, 1339.5256), (15.81521146732115, -42.963806623059924, -83.98663567134022), (1.0, 1.0, 1.0), "BP_Orc_Scaffolding_Post_3m_B4", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_brk_mesh, _brk_mats, (8064.8594, 10518.081, 1348.6511), (-1.4128735788344198, -161.52959275479697, -90.27296239003854), (1.0, 1.0, 1.0), "BP_Orc_Scaffolding_Post_3m_B5_12", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_brk_mesh, _brk_mats, (8809.054, 9726.778, 1384.6511), (3.1107350593319003, -3.8763733407453342, -79.96842284630708), (1.0, 1.0, 1.0), "BP_Orc_Scaffolding_Post_3m_B6", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_brk_mesh, _brk_mats, (9173.379, 8344.762, 1346.293), (3.7291845233695367, 46.38397127866544, 89.69241886626067), (1.0, 1.0, 1.0), "BP_Orc_Scaffolding_Post_3m_B7", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_brk_mesh, _brk_mats, (4797.8613, 6196.3604, 1346.293), (3.7291851813303096, -74.55368391192751, 89.69241817770329), (1.0, 1.0, 1.0), "BP_Orc_Scaffolding_Post_3m_B8", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_brk_mesh, _brk_mats, (4314.8115, 6787.85, 1365.2811), (85.33317589530424, -63.719194694211936, -177.78931879317685), (1.0, 1.0, 1.0), "BP_Orc_Scaffolding_Post_3m_B9", _folder)
if a: placed += 1
else: skipped += 1

# Breakable Batch 8: BP_Orc_Scaffolding_Post_3m_C (11 instances)
#   BP Class: /Game/LevelDesign/Architecture/Orc/BP_Orc_Scaffolding_Post_3m_C
_brk_mesh = "/Game/Art/Assets/Kits/Deco_Architecture/Orc_Camp/Orc_Scaffolding_Post_3m_C"
_brk_mats = ['/Game/Art/Assets/Kits/Deco_Architecture/Orc_Camp/Materials/MI_Orc_Scaffolding_Poles']
a = spawn_static_mesh(_brk_mesh, _brk_mats, (3939.2305, 8169.8823, 1345.9591), (1.379644030338881, 33.131384317737584, 88.84280812948943), (1.0, 1.0, 1.0), "BP_Orc_Scaffolding_Post_3m_C_2", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_brk_mesh, _brk_mats, (8095.758, 6314.804, 1346.3397), (14.024829612778282, 63.349823677225636, 89.13622203090544), (1.0, 1.0, 1.0), "BP_Orc_Scaffolding_Post_3m_C10", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_brk_mesh, _brk_mats, (6921.8975, 5842.5337, 1345.3397), (14.024832113659096, 60.53693018934838, 89.13623377318378), (1.0, 1.0, 1.0), "BP_Orc_Scaffolding_Post_3m_C11", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_brk_mesh, _brk_mats, (4632.833, 9861.876, 1283.6202), (5.726676010425036, 179.10490141636757, 87.79206369763106), (1.0, 1.0, 1.0), "BP_Orc_Scaffolding_Post_3m_C2", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_brk_mesh, _brk_mats, (5348.155, 10439.559, 1350.3539), (-1.674591410507916, 126.52944165481077, -73.67689919716648), (1.0, 1.0, 1.0), "BP_Orc_Scaffolding_Post_3m_C3_8", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_brk_mesh, _brk_mats, (6343.3237, 11195.99, 1344.9426), (0.43215810034551966, -44.757814207844156, -90.37518164953885), (1.0, 1.0, 1.0), "BP_Orc_Scaffolding_Post_3m_C4", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_brk_mesh, _brk_mats, (7986.0947, 10495.828, 1344.9646), (-3.344026486459291, -119.31594546130468, -89.82616933842566), (1.0, 1.0, 1.0), "BP_Orc_Scaffolding_Post_3m_C5_12", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_brk_mesh, _brk_mats, (8792.502, 8137.715, 1347.3397), (14.024829546045728, -43.525264324426445, 89.13620949876906), (1.0, 1.0, 1.0), "BP_Orc_Scaffolding_Post_3m_C6", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_brk_mesh, _brk_mats, (8995.47, 7359.365, 1346.538), (20.624656238223384, -6.796660839955769, -89.7666944131143), (1.0, 1.0, 1.0), "BP_Orc_Scaffolding_Post_3m_C7", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_brk_mesh, _brk_mats, (4816.082, 6629.492, 1347.3397), (14.024829790141622, -164.46277919079031, 89.13623888380248), (1.0, 1.0, 1.0), "BP_Orc_Scaffolding_Post_3m_C8", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_brk_mesh, _brk_mats, (4325.575, 7084.074, 1350.3838), (5.901594306000373, 86.57804437223164, 90.61359970238296), (1.0, 1.0, 1.0), "BP_Orc_Scaffolding_Post_3m_C9", _folder)
if a: placed += 1
else: skipped += 1

# Breakable Batch 9: BP_Orc_Scaffolding_Post_3m_d (17 instances)
#   BP Class: /Game/LevelDesign/Architecture/Orc/BP_Orc_Scaffolding_Post_3m_d
_brk_mesh = "/Game/Art/Assets/Kits/Deco_Architecture/Orc_Camp/Orc_Scaffolding_Post_3m_D"
_brk_mats = ['/Game/Art/Assets/Kits/Deco_Architecture/Orc_Camp/Materials/MI_Orc_Scaffolding_Poles']
a = spawn_static_mesh(_brk_mesh, _brk_mats, (3984.198, 8182.878, 1365.4512), (1.8377087419803696e-05, -59.06036193448426, 98.43783024758379), (1.0, 1.0, 1.0), "BP_Orc_Scaffolding_Post_3m_D_2", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_brk_mesh, _brk_mats, (8576.24, 8126.3765, 1278.7798), (-28.253361482820253, 142.74253779634017, 90.60834970148639), (1.0, 1.0, 1.0), "BP_Orc_Scaffolding_Post_3m_D10", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_brk_mesh, _brk_mats, (8885.264, 9064.608, 1390.6525), (7.939726730756352, 140.89368047983652, 96.00867994780843), (1.0, 1.0, 1.0), "BP_Orc_Scaffolding_Post_3m_D11", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_brk_mesh, _brk_mats, (4764.5376, 7284.8154, 1280.7798), (-27.177213222378946, 23.17020298612445, 87.67290206753499), (1.0, 1.0, 1.0), "BP_Orc_Scaffolding_Post_3m_D12", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_brk_mesh, _brk_mats, (5563.4146, 6073.4087, 1390.6525), (7.939727222237405, 19.955996065721894, 96.00870048264082), (1.0, 1.0, 1.0), "BP_Orc_Scaffolding_Post_3m_D13", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_brk_mesh, _brk_mats, (4335.4336, 6862.4844, 1366.1519), (-63.65584605410833, -45.89738305072129, 94.85856252341853), (1.0, 1.0, 1.0), "BP_Orc_Scaffolding_Post_3m_D14", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_brk_mesh, _brk_mats, (4658.4033, 8004.829, 1332.2985), (-5.580165672919886, 101.1171425560893, 92.28736297801319), (1.0, 1.0, 1.0), "BP_Orc_Scaffolding_Post_3m_D15", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_brk_mesh, _brk_mats, (7219.849, 6118.5063, 1382.6525), (7.939728712856654, -112.2311699535945, 96.00872879068098), (1.0, 1.0, 1.0), "BP_Orc_Scaffolding_Post_3m_D16", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_brk_mesh, _brk_mats, (6218.91, 6446.932, 1268.8888), (7.939729906850437, -137.5431336390393, 84.75879324709543), (1.0, 1.0, 1.0), "BP_Orc_Scaffolding_Post_3m_D17", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_brk_mesh, _brk_mats, (4275.0, 8809.0, 1393.0), (10.43110676344291, 122.16225423874286, 102.78257722675319), (1.0, 1.0, 1.0), "BP_Orc_Scaffolding_Post_3m_D2_5", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_brk_mesh, _brk_mats, (4736.8535, 9958.027, 1286.1925), (-64.51320176317714, 111.7127407262955, 60.134984162422356), (1.0, 1.0, 1.0), "BP_Orc_Scaffolding_Post_3m_D3", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_brk_mesh, _brk_mats, (4115.496, 9911.718, 1354.5349), (11.170789448960786, -164.94744473456223, 91.6526265823295), (1.0, 1.0, 1.0), "BP_Orc_Scaffolding_Post_3m_D4", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_brk_mesh, _brk_mats, (4785.0, 10652.0, 1347.0), (3.202694153656843e-06, 64.68751162918684, -89.99987369294519), (1.0, 1.0, 1.0), "BP_Orc_Scaffolding_Post_3m_D5_12", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_brk_mesh, _brk_mats, (6956.048, 11207.911, 1353.7904), (57.337998647860296, -40.35334976783702, -89.80760099118005), (1.0, 1.0, 1.0), "BP_Orc_Scaffolding_Post_3m_D6", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_brk_mesh, _brk_mats, (7603.9614, 10147.922, 1301.785), (5.464457998893714, -163.56084155030942, -83.68883757711667), (1.0, 1.0, 1.0), "BP_Orc_Scaffolding_Post_3m_D7_16", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_brk_mesh, _brk_mats, (7389.387, 10394.18, 1316.0615), (5.381997001502685, -73.04691116171298, -77.11139290532998), (1.0, 1.0, 1.0), "BP_Orc_Scaffolding_Post_3m_D8_19", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_brk_mesh, _brk_mats, (8894.985, 9921.593, 1359.7245), (-14.98822224810171, 13.165128187154036, -90.85553606012172), (1.0, 1.0, 1.0), "BP_Orc_Scaffolding_Post_3m_D9_22", _folder)
if a: placed += 1
else: skipped += 1

# Breakable Batch 10: BP_Orc_Scaffolding_Post_4m_A (3 instances)
#   BP Class: /Game/LevelDesign/Architecture/Orc/BP_Orc_Scaffolding_Post_4m_A
_brk_mesh = "/Game/Art/Assets/Kits/Deco_Architecture/Orc_Camp/Orc_Scaffolding_Post_4m_A"
_brk_mats = ['/Game/Art/Assets/Kits/Deco_Architecture/Orc_Camp/Materials/MI_Orc_Scaffolding_Poles']
a = spawn_static_mesh(_brk_mesh, _brk_mats, (5045.155, 10265.832, 1316.5284), (-1.0953969832092112, 149.0093977572196, -87.29365190437095), (1.0, 1.0, 1.0), "BP_Orc_Scaffolding_Post_4m_A_4", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_brk_mesh, _brk_mats, (6598.794, 11017.928, 1359.9739), (7.144404618020541, -23.24108942966762, -96.3769785300781), (1.0, 1.0, 1.0), "BP_Orc_Scaffolding_Post_4m_A2", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_brk_mesh, _brk_mats, (7448.5347, 10250.829, 1333.1078), (-1.1612545128620662, -133.22006675000867, -92.08932588738453), (1.0, 1.0, 1.0), "BP_Orc_Scaffolding_Post_4m_A3_8", _folder)
if a: placed += 1
else: skipped += 1

# Breakable Batch 11: BP_Orc_Scaffolding_Post_4m_B (9 instances)
#   BP Class: /Game/LevelDesign/Architecture/Orc/BP_Orc_Scaffolding_Post_4m_B
_brk_mesh = "/Game/Art/Assets/Kits/Deco_Architecture/Orc_Camp/Orc_Scaffolding_Post_4m_B"
_brk_mats = ['/Game/Art/Assets/Kits/Deco_Architecture/Orc_Camp/Materials/MI_Orc_Scaffolding_Poles']
a = spawn_static_mesh(_brk_mesh, _brk_mats, (4198.0, 8503.0, 1291.0), (0.0, 0.0, 72.52374422406277), (1.0, 1.0, 1.0), "BP_Orc_Scaffolding_Post_4m_B_2", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_brk_mesh, _brk_mats, (4159.2085, 9607.985, 1347.8885), (-7.864900782078457, 94.58946141298713, 90.31359998283988), (1.0, 1.0, 1.0), "BP_Orc_Scaffolding_Post_4m_B2", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_brk_mesh, _brk_mats, (5203.0, 10727.0, 1345.0), (6.768110251351307e-06, 154.68756120810926, -89.99989023028225), (1.0, 1.0, 1.0), "BP_Orc_Scaffolding_Post_4m_B3_8", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_brk_mesh, _brk_mats, (6337.1147, 11012.016, 1355.576), (5.154936883047095, -27.76806654995835, -96.81695732717459), (1.0, 1.0, 1.0), "BP_Orc_Scaffolding_Post_4m_B4", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_brk_mesh, _brk_mats, (7332.9683, 10780.941, 1395.4723), (4.420226349794502, 88.9889264779116, -97.08037631163963), (1.0, 1.0, 1.0), "BP_Orc_Scaffolding_Post_4m_B5_12", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_brk_mesh, _brk_mats, (8944.629, 9496.035, 1361.5724), (32.67404797253373, -72.23167736034638, -33.765294459684455), (1.0, 1.0, 1.0), "BP_Orc_Scaffolding_Post_4m_B6", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_brk_mesh, _brk_mats, (8622.707, 8497.025, 1254.9395), (-4.925844014489201, 148.31328086936446, 86.66540178528221), (1.0, 1.0, 1.0), "BP_Orc_Scaffolding_Post_4m_B7", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_brk_mesh, _brk_mats, (5525.415, 6771.9463, 1367.6056), (1.3476567319159174, 75.07382928607534, 95.14908290463458), (1.0, 1.0, 1.0), "BP_Orc_Scaffolding_Post_4m_B8", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_brk_mesh, _brk_mats, (4253.93, 7479.458, 1310.6521), (-5.589782343849428, -24.14312638023856, 95.49399834790434), (1.0, 1.0, 1.0), "BP_Orc_Scaffolding_Post_4m_B9", _folder)
if a: placed += 1
else: skipped += 1

# Breakable Batch 12: BP_Orc_Scaffolding_Post_5m_D (13 instances)
#   BP Class: /Game/LevelDesign/Architecture/Orc/BP_Orc_Scaffolding_Post_5m_D
_brk_mesh = "/Game/Art/Assets/Kits/Deco_Architecture/Orc_Camp/Orc_Scaffolding_Post_5m_D"
_brk_mats = ['/Game/Art/Assets/Kits/Deco_Architecture/Orc_Camp/Materials/MI_Orc_Scaffolding_Poles']
a = spawn_static_mesh(_brk_mesh, _brk_mats, (3700.3616, 9162.593, 1348.0002), (-0.08477925673636216, -151.81467948496532, 89.99681793681634), (1.0, 1.0, 1.0), "BP_Orc_Scaffolding_Post_5m_D_2", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_brk_mesh, _brk_mats, (5658.844, 6547.668, 1390.9324), (5.7168527838147245, 82.47067562914603, 99.19767002098524), (1.0, 1.0, 1.0), "BP_Orc_Scaffolding_Post_5m_D10", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_brk_mesh, _brk_mats, (4187.087, 7776.335, 1351.726), (-0.08468627585421806, -179.9394503641992, 89.9967482895578), (1.0, 1.0, 1.0), "BP_Orc_Scaffolding_Post_5m_D11", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_brk_mesh, _brk_mats, (4201.3296, 7211.2954, 1349.275), (-19.70968177800859, 28.225615976574574, 95.22734952640509), (1.0, 1.0, 1.0), "BP_Orc_Scaffolding_Post_5m_D12", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_brk_mesh, _brk_mats, (6977.1416, 5736.0, 1351.4618), (8.615244104508097, 18.332989934598068, 90.29305692254941), (1.0, 1.0, 1.0), "BP_Orc_Scaffolding_Post_5m_D13", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_brk_mesh, _brk_mats, (4064.8665, 9377.448, 1351.9624), (-0.0847172306861011, -33.68954241836931, 89.99682330402776), (1.0, 1.0, 1.0), "BP_Orc_Scaffolding_Post_5m_D2", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_brk_mesh, _brk_mats, (4907.571, 9676.221, 1359.5115), (-19.709809487068682, 146.35083914720565, 95.22733219267201), (1.0, 1.0, 1.0), "BP_Orc_Scaffolding_Post_5m_D3", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_brk_mesh, _brk_mats, (5044.2393, 10757.066, 1339.035), (8.437482110952676, 33.75180916739483, -89.9994173696809), (1.0, 1.0, 1.0), "BP_Orc_Scaffolding_Post_5m_D4_9", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_brk_mesh, _brk_mats, (6960.9683, 10576.357, 1301.0348), (-6.355989772869249, -151.75603506045388, -83.81623140296448), (1.0, 1.0, 1.0), "BP_Orc_Scaffolding_Post_5m_D5", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_brk_mesh, _brk_mats, (7318.2563, 10676.719, 1379.2267), (18.54952998773839, 64.80067790830046, -96.61718075647248), (1.0, 1.0, 1.0), "BP_Orc_Scaffolding_Post_5m_D6_13", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_brk_mesh, _brk_mats, (8512.613, 8121.2705, 1276.4012), (8.615231172868208, -51.97930403371953, 79.04404830485039), (1.0, 1.0, 1.0), "BP_Orc_Scaffolding_Post_5m_D7", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_brk_mesh, _brk_mats, (8373.371, 9063.198, 1275.4692), (9.35587670415753, -161.76352078359622, 89.94262132606227), (1.0, 1.0, 1.0), "BP_Orc_Scaffolding_Post_5m_D8", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_brk_mesh, _brk_mats, (4945.8687, 6878.015, 1283.4012), (8.615244422092251, -172.91668918860495, 79.04358556319026), (1.0, 1.0, 1.0), "BP_Orc_Scaffolding_Post_5m_D9", _folder)
if a: placed += 1
else: skipped += 1

# Breakable Batch 13: BP_DM_Rubble_Masonry_Pile_C_Breakable (4 instances)
#   BP Class: /Game/LevelDesign/Deco/Rubble/BP_DM_Rubble_Masonry_Pile_C_Breakable
_brk_mesh = "/Game/Art/Assets/Kits/Deco/Rubble/Rubble_Masonry_Pile_C"
_brk_mats = ['/Game/Art/Assets/Kits/Deco/Rubble/Materials/Rubble_Masonry_Pile/MI_Rubble_Masonry_Pile_Atlas_Inst_B', '/Game/Art/Assets/Kits/Deco/Rubble/Materials/Rubble_Masonry_Pile/MI_Rubble_Masonry_Pile_Atlas_Inst_A']
a = spawn_static_mesh(_brk_mesh, _brk_mats, (5456.234, 6686.3667, 1229.4756), (0.0, 108.08652676833654, -0.0), (1.0, 1.0, 1.0), "Rubble_Masonry_Pile_C_220", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_brk_mesh, _brk_mats, (5206.339, 9752.784, 1241.9639), (0.0, 19.839216371772356, -0.0), (1.0, 1.0, 1.0), "Rubble_Masonry_Pile_C2_260", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_brk_mesh, _brk_mats, (6850.006, 9727.024, 1629.0399), (-13.707825692877432, 21.804859451472836, -4.4041132831132925), (1.0, 1.0, 1.0), "Rubble_Masonry_Pile_C3_286", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_brk_mesh, _brk_mats, (6304.4463, 9702.208, 1685.0125), (-17.792418640021758, 18.680865302240075, 7.062795068293397), (1.0, 1.0, 1.0), "Rubble_Masonry_Pile_C4", _folder)
if a: placed += 1
else: skipped += 1

# Breakable Batch 14: BP_DM_Rubble_Masonry_Pile_E_Breakable (2 instances)
#   BP Class: /Game/LevelDesign/Deco/Rubble/BP_DM_Rubble_Masonry_Pile_E_Breakable
_brk_mesh = "/Game/Art/Assets/Kits/Deco/Rubble/Rubble_Masonry_Pile_E_Optimized"
_brk_mats = ['/Game/Art/Assets/Kits/Deco/Rubble/Materials/Rubble_Masonry_Pile/MI_Rubble_Masonry_Pile_Atlas_Inst_A', '/Game/Art/Assets/Kits/Deco/Rubble/Materials/Rubble_Masonry_Pile/MI_Rubble_Masonry_Pile_Atlas_Inst_B']
a = spawn_static_mesh(_brk_mesh, _brk_mats, (8040.451, 7566.118, 1251.081), (0.0, 90.0000030488508, -0.0), (1.0, 1.0, 1.0), "Rubble_Masonry_Pile_E_186", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_brk_mesh, _brk_mats, (5703.4126, 9492.592, 1752.4856), (-12.032927510200006, -172.94035783785054, -1.4786068758427755), (1.0, 1.0, 1.0), "Rubble_Masonry_Pile_E2_257", _folder)
if a: placed += 1
else: skipped += 1

# Breakable Batch 15: BP_DM_Rubble_Masonry_Pile_F_Breakable (11 instances)
#   BP Class: /Game/LevelDesign/Deco/Rubble/BP_DM_Rubble_Masonry_Pile_F_Breakable
_brk_mesh = "/Game/Art/Assets/Kits/Deco/Rubble/Rubble_Masonry_Pile_F_Optimized"
_brk_mats = ['/Game/Art/Assets/Kits/Deco/Rubble/Materials/Rubble_Masonry_Pile/MI_Rubble_Masonry_Pile_Atlas_Inst_B', '/Game/Art/Assets/Kits/Deco/Rubble/Materials/Rubble_Masonry_Pile/MI_Rubble_Masonry_Pile_Atlas_Inst_A']
a = spawn_static_mesh(_brk_mesh, _brk_mats, (7537.6465, 7725.3154, 1291.4634), (14.543026990328114, 163.0230353776538, 8.482247066922227), (1.0, 1.0, 1.0), "Rubble_Masonry_Pile_F_198", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_brk_mesh, _brk_mats, (6176.233, 10010.586, 1534.8519), (16.74597066654195, -126.82018560921644, -17.89303703040548), (1.0, 1.0, 0.69746155), "Rubble_Masonry_Pile_F10", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_brk_mesh, _brk_mats, (7245.232, 8083.9688, 1687.3704), (12.975644572767155, 127.86129941611632, -7.691223860411084), (1.0, 1.0, 0.5869284), "Rubble_Masonry_Pile_F11", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_brk_mesh, _brk_mats, (7583.4653, 8428.757, 1594.9106), (-23.446015511479466, -56.0266729085452, 14.075402038941206), (1.0, 1.0, 0.586928), "Rubble_Masonry_Pile_F12", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_brk_mesh, _brk_mats, (5491.028, 6949.9473, 1236.1152), (0.0, 90.0000030488508, -0.0), (1.0, 1.0, 1.0), "Rubble_Masonry_Pile_F2_201", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_brk_mesh, _brk_mats, (5839.5034, 7279.8315, 1266.7188), (15.10987297219885, 90.00000543666047, 2.7147057496500907e-07), (1.0, 1.0, 0.41245738), "Rubble_Masonry_Pile_F3", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_brk_mesh, _brk_mats, (5299.503, 7055.3135, 1259.4727), (-3.6820980454998637, -171.52682714084477, 6.9704906498963854), (1.0, 1.0, 0.412457), "Rubble_Masonry_Pile_F4", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_brk_mesh, _brk_mats, (4549.213, 8155.085, 1229.1401), (0.0, -8.814087171883562, 0.0), (1.0, 1.0, 1.0), "Rubble_Masonry_Pile_F6", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_brk_mesh, _brk_mats, (5405.727, 9244.426, 1239.8677), (8.81142260383537, -23.813446941363758, 1.7253013628507079e-06), (1.0, 1.0, 0.8101899), "Rubble_Masonry_Pile_F7", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_brk_mesh, _brk_mats, (5118.5146, 9474.459, 1250.2286), (-2.523864690844061, -23.81179703183978, 1.1502142148576416e-05), (1.0, 1.0, 0.81019), "Rubble_Masonry_Pile_F8", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_brk_mesh, _brk_mats, (7069.19, 9904.262, 1248.2065), (-1.8910522492405895, -23.81237978575736, 5.883679942323445), (1.0, 1.0, 0.81019), "Rubble_Masonry_Pile_F9", _folder)
if a: placed += 1
else: skipped += 1

# Breakable Batch 16: BP_DM_Rubble_Masonry_Pile_H_Breakable (4 instances)
#   BP Class: /Game/LevelDesign/Deco/Rubble/BP_DM_Rubble_Masonry_Pile_H_Breakable
_brk_mesh = "/Game/Art/Assets/Kits/Deco/Rubble/Rubble_Masonry_Pile_H_Optimized"
_brk_mats = ['/Game/Art/Assets/Kits/Deco/Rubble/Materials/Rubble_Masonry_Pile/MI_Rubble_Masonry_Pile_Atlas_Inst_B', '/Game/Art/Assets/Kits/Deco/Rubble/Materials/Rubble_Masonry_Pile/MI_Rubble_Masonry_Pile_Atlas_Inst_A']
a = spawn_static_mesh(_brk_mesh, _brk_mats, (7927.324, 8100.067, 1245.0654), (0.0, 90.0000030488508, -0.0), (1.0, 1.0, 1.0), "Rubble_Masonry_Pile_H_177", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_brk_mesh, _brk_mats, (7611.9033, 7886.199, 1316.6309), (17.131369160968138, 160.62461259250327, 1.0960077140195876), (1.0, 1.0, 1.0), "Rubble_Masonry_Pile_H2_180", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_brk_mesh, _brk_mats, (7353.577, 9280.97, 1610.4062), (-21.711880374794685, -1.0860897244039482, 9.12677167042536), (1.0, 1.0, 1.0), "Rubble_Masonry_Pile_H3", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_brk_mesh, _brk_mats, (7472.6006, 9231.013, 1234.9326), (-1.3669127315706915, -53.3155488240777, 0.9117170233317085), (1.0, 1.0, 1.0), "Rubble_Masonry_Pile_H4", _folder)
if a: placed += 1
else: skipped += 1

# Breakable Batch 17: BP_DM_Rubble_Masonry_Pile_I_Breakable (3 instances)
#   BP Class: /Game/LevelDesign/Deco/Rubble/BP_DM_Rubble_Masonry_Pile_I_Breakable
_brk_mesh = "/Game/Art/Assets/Kits/Deco/Rubble/Rubble_Masonry_Pile_I"
_brk_mats = ['/Game/Art/Assets/Kits/Deco/Rubble/Materials/Rubble_Masonry_Pile/MI_Rubble_Masonry_Pile_Atlas_Inst_B', '/Game/Art/Assets/Kits/Deco/Rubble/Materials/Rubble_Masonry_Pile/MI_Rubble_Masonry_Pile_Atlas_Inst_A']
a = spawn_static_mesh(_brk_mesh, _brk_mats, (7629.031, 8329.403, 1266.8267), (15.698749362075775, 174.26586275608364, -58.545044656498746), (1.0, 1.0, 1.0), "Rubble_Masonry_Pile_I_192", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_brk_mesh, _brk_mats, (7055.2603, 9158.684, 1714.6849), (5.0706430766701525, -70.718955025591, -2.065093636324987), (1.0, 1.0, 1.0), "Rubble_Masonry_Pile_I2", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_brk_mesh, _brk_mats, (7462.912, 9126.756, 1612.1727), (17.165675524293945, -100.06218666928662, -20.164822885027075), (1.0, 1.0, 1.0), "Rubble_Masonry_Pile_I3", _folder)
if a: placed += 1
else: skipped += 1

# Breakable Batch 18: BP_DM_Warehouse_Crate_A_Lid_Breakable (1 instances)
#   BP Class: /Game/LevelDesign/Deco/Urban/Warehouse/BP_DM_Warehouse_Crate_A_Lid_Breakable
_brk_mesh = "/Game/Art/Assets/Kits/Deco/Urban/Warehouse/Warehouse_Crate_A_Lid"
_brk_mats = ['/Game/Art/Assets/Kits/Deco/Urban/Warehouse/Materials/Warehouse_Crate/MI_Warehouse_Crate']
a = spawn_static_mesh(_brk_mesh, _brk_mats, (7549.3623, 9498.205, 1263.1299), (-4.760162522549576, 91.13763620672334, -13.457703365605413), (1.0, 1.0, 1.0), "Warehouse_Crate_A_Lid_446", _folder)
if a: placed += 1
else: skipped += 1

# Breakable Batch 19: BP_DM_Warehouse_Crate_B_Lid_Breakable (3 instances)
#   BP Class: /Game/LevelDesign/Deco/Urban/Warehouse/BP_DM_Warehouse_Crate_B_Lid_Breakable
_brk_mesh = "/Game/Art/Assets/Kits/Deco/Urban/Warehouse/Warehouse_Crate_B_Lid"
_brk_mats = ['/Game/Art/Assets/Kits/Deco/Urban/Warehouse/Materials/Warehouse_Crate/MI_Warehouse_Crate']
a = spawn_static_mesh(_brk_mesh, _brk_mats, (7090.411, 9821.351, 1306.9624), (-4.172027492288479, -1.0400390300391618, -128.04056117019002), (1.0, 1.0, 1.0), "Warehouse_Crate_B_Lid_434", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_brk_mesh, _brk_mats, (7015.8394, 7331.495, 1275.2578), (-20.86795156308792, 128.92739908869643, 51.91626118901398), (1.0, 1.0, 1.0), "Warehouse_Crate_B_Lid2_455", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_brk_mesh, _brk_mats, (6747.484, 9686.26, 1719.8374), (-26.55364905554665, 138.57059385627983, -36.316957570592166), (1.0, 1.0, 1.0), "Warehouse_Crate_B_Lid3", _folder)
if a: placed += 1
else: skipped += 1

# Breakable Batch 20: BP_DM_Mines_Scaffolding_Arch_B (2 instances)
#   BP Class: /Game/LevelDesign/Deco_Architecture/Mines/BP_DM_Mines_Scaffolding_Arch_B
_brk_mesh = "/Game/Art/Assets/Kits/Deco_Architecture/Mines/Mines_Scaffolding_Arch_B"
_brk_mats = ['/Game/Art/Assets/Kits/Deco_Architecture/Mines/Materials/Mines_Scaffolding/MI_Mines_Scaffolding_A_Deco']
a = spawn_static_mesh(_brk_mesh, _brk_mats, (9849.121, 8598.215, 1820.0), (0.0, 95.00004479164929, -0.0), (1.0, 1.0, 1.0), "BP_DM_Mines_Scaffolding_Arch_B_2", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_brk_mesh, _brk_mats, (9880.0, 8360.0, 1820.0), (0.0, 95.00004479164929, -0.0), (1.0, 1.0, 1.0), "BP_DM_Mines_Scaffolding_Arch_B2", _folder)
if a: placed += 1
else: skipped += 1

# Breakable Batch 21: BP_DM_Mines_Scaffolding_Platform_3X1M_A (1 instances)
#   BP Class: /Game/LevelDesign/Deco_Architecture/Mines/BP_DM_Mines_Scaffolding_Platform_3X1M_A
_brk_mesh = "/Game/Art/Assets/Kits/Deco_Architecture/Mines/Mines_Scaffolding_Platform_3X1M_A"
_brk_mats = ['/Game/Art/Assets/Kits/Deco_Architecture/Mines/Materials/Mines_Scaffolding/MI_Mines_Scaffolding_D_Deco', '/Game/Art/Assets/Kits/Deco_Architecture/Mines/Materials/Mines_Scaffolding/MI_Mines_Scaffolding_E_Deco']
a = spawn_static_mesh(_brk_mesh, _brk_mats, (9900.0, 8340.0, 1840.0), (0.0, 5.000023098478975, -0.0), (1.0, 1.0, 1.0), "BP_DM_Mines_Scaffolding_Platform_3X1M_A_5", _folder)
if a: placed += 1
else: skipped += 1

# Breakable Batch 22: BP_DM_Mines_Scaffolding_Platform_3X1M_C (2 instances)
#   BP Class: /Game/LevelDesign/Deco_Architecture/Mines/BP_DM_Mines_Scaffolding_Platform_3X1M_C
_brk_mesh = "/Game/Art/Assets/Kits/Deco_Architecture/Mines/Mines_Scaffolding_Platform_3X1M_C"
_brk_mats = ['/Game/Art/Assets/Kits/Deco_Architecture/Mines/Materials/Mines_Scaffolding/MI_Mines_Scaffolding_E_Deco', '/Game/Art/Assets/Kits/Deco_Architecture/Mines/Materials/Mines_Scaffolding/MI_Mines_Scaffolding_D_Deco']
a = spawn_static_mesh(_brk_mesh, _brk_mats, (9775.9, 8631.962, 1840.0), (0.0, -174.99988372592426, 0.0), (1.0, 1.0, 1.0), "BP_DM_Mines_Scaffolding_Platform_3X1M_C_2", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_brk_mesh, _brk_mats, (9550.0, 8200.0, 1390.0), (24.594776624355454, 11.010221800645779, 4.629415008048114), (1.0, 1.0, 1.0), "BP_DM_Mines_Scaffolding_Platform_3X1M_C2_5", _folder)
if a: placed += 1
else: skipped += 1

# --- Extra DecoVolumes (not construction blocks) ---
_folder = "Reconstruction/BD_BB_Chapter5_BoneHoard/DecoVolumes"

# DecoVolume: BP_DM_Mines_Fence_Brace_F_BoneHoard (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (10164.104, 8541.912, 2067.9453), (0.0, 0.0, -0.0), (3.2637, 3.6426, 4.1697), "DV_BP_DM_Mines_Fence_Brace_F_BoneHoard_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_DM_Mines_Scaffolding_Arch_B_2 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (9794.503, 8593.571, 1771.8214), (0.0, 0.0, -0.0), (1.1130, 0.2786, 0.9750), "DV_BP_DM_Mines_Scaffolding_Arch_B_2_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_DM_Mines_Scaffolding_Arch_B2 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (9825.382, 8355.356, 1771.8214), (0.0, 0.0, -0.0), (1.1130, 0.2786, 0.9750), "DV_BP_DM_Mines_Scaffolding_Arch_B2_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_DM_Mines_Scaffolding_Platform_3X1M_A_5 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (9885.984, 8489.706, 1828.6566), (0.0, 0.0, -0.0), (1.3201, 3.1364, 0.2869), "DV_BP_DM_Mines_Scaffolding_Platform_3X1M_A_5_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_DM_Mines_Scaffolding_Platform_3X1M_C_2 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (9789.528, 8479.852, 1828.9031), (0.0, 0.0, -0.0), (1.2759, 3.1287, 0.2873), "DV_BP_DM_Mines_Scaffolding_Platform_3X1M_C_2_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_DM_Mines_Scaffolding_Platform_3X1M_C2_5 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (9530.369, 8350.344, 1368.6024), (0.0, 0.0, -0.0), (1.5066, 3.1817, 0.9063), "DV_BP_DM_Mines_Scaffolding_Platform_3X1M_C2_5_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_DM_Warren_lighting_Fireplace_A_large_Breakable_2 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (11604.396, 8810.22, 930.1564), (0.0, 0.0, -0.0), (2.6152, 2.4132, 3.1461), "DV_BP_DM_Warren_lighting_Fireplace_A_large_Breakable_2_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_DM_Warren_Lighting_Torch_B_Breakable_2 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (10001.548, 8147.9517, 1939.8129), (0.0, 0.0, -0.0), (1.3059, 1.3062, 0.9678), "DV_BP_DM_Warren_Lighting_Torch_B_Breakable_2_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_DM_Warren_Lighting_Torch_B_Breakable2 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (9901.548, 8947.952, 1939.8129), (0.0, 0.0, -0.0), (1.3059, 1.3062, 0.9678), "DV_BP_DM_Warren_Lighting_Torch_B_Breakable2_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_DM_Warren_Lighting_Torch_B_Breakable3_6 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (2328.5278, 8408.606, 1196.7043), (0.0, 0.0, -0.0), (1.3059, 1.3062, 0.9678), "DV_BP_DM_Warren_Lighting_Torch_B_Breakable3_6_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_DM_Warren_Lighting_Torch_B_Breakable4_9 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (1808.6831, 9125.531, 899.0327), (0.0, 0.0, -0.0), (1.6472, 1.6783, 0.9678), "DV_BP_DM_Warren_Lighting_Torch_B_Breakable4_9_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_DM_Warren_Lighting_Torch_B_Breakable5_12 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (823.1141, 8939.319, 850.813), (0.0, 0.0, -0.0), (1.3059, 1.3062, 0.9678), "DV_BP_DM_Warren_Lighting_Torch_B_Breakable5_12_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_DM_Warren_Lighting_Torch_B_Breakable6 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (1673.8374, 8599.489, 849.0926), (0.0, 0.0, -0.0), (1.4537, 1.4052, 0.9678), "DV_BP_DM_Warren_Lighting_Torch_B_Breakable6_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_DM_Warren_Lighting_Torch_B_Breakable7 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (2440.508, 8815.354, 1192.9072), (0.0, 0.0, -0.0), (1.6624, 1.6536, 0.9938), "DV_BP_DM_Warren_Lighting_Torch_B_Breakable7_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_DM_Warren_Lighting_Torch_B_Breakable8 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (908.72864, 9891.797, 865.813), (0.0, 0.0, -0.0), (1.8035, 1.8074, 0.9678), "DV_BP_DM_Warren_Lighting_Torch_B_Breakable8_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_DM_Warren_Lighting_Torch_Breakable_7 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (10704.88, 8845.011, 1864.8237), (0.0, 0.0, -0.0), (1.0112, 1.0765, 1.9128), "DV_BP_DM_Warren_Lighting_Torch_Breakable_7_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_DM_Warren_Lighting_Torch_Breakable2_11 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (4100.9478, 7610.063, 1405.8555), (0.0, 0.0, -0.0), (1.0112, 1.0765, 1.9128), "DV_BP_DM_Warren_Lighting_Torch_Breakable2_11_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_DM_Warren_Lighting_Torch_Breakable3_13 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (4006.34, 9412.748, 1406.42), (0.0, 0.0, -0.0), (1.0112, 1.0765, 1.9128), "DV_BP_DM_Warren_Lighting_Torch_Breakable3_13_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_DM_Warren_Lighting_Torch_Breakable4 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (7054.8804, 10745.011, 1314.8237), (0.0, 0.0, -0.0), (1.0112, 1.0765, 1.9128), "DV_BP_DM_Warren_Lighting_Torch_Breakable4_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_DM_Warren_Lighting_Torch_Breakable5 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (7405.028, 6223.05, 1406.183), (0.0, 0.0, -0.0), (1.0112, 1.0765, 1.9128), "DV_BP_DM_Warren_Lighting_Torch_Breakable5_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_Orc_Scaffolding_Post_1m_A_2 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (3938.028, 8687.986, 1344.4888), (0.0, 0.0, -0.0), (1.1242, 0.6902, 0.2404), "DV_BP_Orc_Scaffolding_Post_1m_A_2_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_Orc_Scaffolding_Post_1m_A10 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (8954.904, 8436.809, 1347.3066), (0.0, 0.0, -0.0), (0.3397, 1.1429, 0.2063), "DV_BP_Orc_Scaffolding_Post_1m_A10_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_Orc_Scaffolding_Post_1m_A11 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (9079.657, 7860.363, 1351.725), (0.0, 0.0, -0.0), (0.5464, 1.1577, 0.2956), "DV_BP_Orc_Scaffolding_Post_1m_A11_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_Orc_Scaffolding_Post_1m_A12 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (8801.753, 6779.4717, 1342.3069), (0.0, 0.0, -0.0), (0.6119, 1.1407, 0.2063), "DV_BP_Orc_Scaffolding_Post_1m_A12_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_Orc_Scaffolding_Post_1m_A13 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (4989.131, 6336.429, 1347.3068), (0.0, 0.0, -0.0), (1.0493, 0.8575, 0.2063), "DV_BP_Orc_Scaffolding_Post_1m_A13_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_Orc_Scaffolding_Post_1m_A14 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (3918.8628, 7531.823, 1347.8193), (0.0, 0.0, -0.0), (1.1365, 0.6434, 0.2451), "DV_BP_Orc_Scaffolding_Post_1m_A14_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_Orc_Scaffolding_Post_1m_A15 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (7723.398, 6390.391, 1345.3068), (0.0, 0.0, -0.0), (1.1524, 0.4626, 0.2063), "DV_BP_Orc_Scaffolding_Post_1m_A15_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_Orc_Scaffolding_Post_1m_A16 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (7760.914, 6210.462, 1347.1229), (0.0, 0.0, -0.0), (1.1589, 0.3980, 0.2899), "DV_BP_Orc_Scaffolding_Post_1m_A16_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_Orc_Scaffolding_Post_1m_A17 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (7907.9507, 6558.6064, 1349.1395), (0.0, 0.0, -0.0), (0.9236, 1.0005, 0.2347), "DV_BP_Orc_Scaffolding_Post_1m_A17_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_Orc_Scaffolding_Post_1m_A18 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (7284.745, 6342.524, 1337.944), (0.0, 0.0, -0.0), (0.6889, 1.1270, 0.2411), "DV_BP_Orc_Scaffolding_Post_1m_A18_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_Orc_Scaffolding_Post_1m_A19 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (6575.26, 6004.7827, 1348.3073), (0.0, 0.0, -0.0), (0.9912, 0.9376, 0.2063), "DV_BP_Orc_Scaffolding_Post_1m_A19_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_Orc_Scaffolding_Post_1m_A2 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (4349.8096, 9539.306, 1329.2145), (0.0, 0.0, -0.0), (0.3445, 1.1567, 0.4024), "DV_BP_Orc_Scaffolding_Post_1m_A2_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_Orc_Scaffolding_Post_1m_A20 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (6527.4854, 6466.6187, 1261.3007), (0.0, 0.0, -0.0), (0.9912, 0.9376, 0.2063), "DV_BP_Orc_Scaffolding_Post_1m_A20_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_Orc_Scaffolding_Post_1m_A3_8 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (5443.0273, 10917.825, 1389.2761), (0.0, 0.0, -0.0), (0.2310, 1.1408, 0.3490), "DV_BP_Orc_Scaffolding_Post_1m_A3_8_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_Orc_Scaffolding_Post_1m_A4 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (7039.15, 11247.824, 1350.207), (0.0, 0.0, -0.0), (1.1136, 0.7489, 0.2386), "DV_BP_Orc_Scaffolding_Post_1m_A4_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_Orc_Scaffolding_Post_1m_A5_12 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (7397.0273, 10978.299, 1381.0225), (0.0, 0.0, -0.0), (0.2310, 1.1404, 0.4019), "DV_BP_Orc_Scaffolding_Post_1m_A5_12_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_Orc_Scaffolding_Post_1m_A6_15 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (7872.7217, 10747.519, 1343.9441), (0.0, 0.0, -0.0), (0.5968, 1.1378, 0.1858), "DV_BP_Orc_Scaffolding_Post_1m_A6_15_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_Orc_Scaffolding_Post_1m_A7_18 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (7615.59, 10912.0625, 1378.2577), (0.0, 0.0, -0.0), (1.1183, 0.7381, 0.3958), "DV_BP_Orc_Scaffolding_Post_1m_A7_18_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_Orc_Scaffolding_Post_1m_A8 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (8663.363, 10167.571, 1351.5103), (0.0, 0.0, -0.0), (1.1601, 0.3956, 0.2953), "DV_BP_Orc_Scaffolding_Post_1m_A8_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_Orc_Scaffolding_Post_1m_A9 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (9079.333, 9432.967, 1347.056), (0.0, 0.0, -0.0), (0.9594, 0.9594, 0.1858), "DV_BP_Orc_Scaffolding_Post_1m_A9_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_Orc_Scaffolding_Post_1m_C_2 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (3958.9937, 8289.361, 1347.9274), (0.0, 0.0, -0.0), (0.3426, 1.5481, 0.1558), "DV_BP_Orc_Scaffolding_Post_1m_C_2_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_Orc_Scaffolding_Post_1m_C10 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (4458.392, 7441.6763, 1267.4619), (0.0, 0.0, -0.0), (0.9750, 1.5530, 0.3067), "DV_BP_Orc_Scaffolding_Post_1m_C10_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_Orc_Scaffolding_Post_1m_C11 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (7622.758, 6162.0605, 1345.0273), (0.0, 0.0, -0.0), (0.9132, 1.5614, 0.1758), "DV_BP_Orc_Scaffolding_Post_1m_C11_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_Orc_Scaffolding_Post_1m_C12 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (8015.157, 6552.48, 1351.311), (0.0, 0.0, -0.0), (1.3807, 1.3011, 0.2141), "DV_BP_Orc_Scaffolding_Post_1m_C12_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_Orc_Scaffolding_Post_1m_C13 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (6399.4214, 5957.889, 1342.5533), (0.0, 0.0, -0.0), (0.9132, 1.5614, 0.1758), "DV_BP_Orc_Scaffolding_Post_1m_C13_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_Orc_Scaffolding_Post_1m_C14 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (6390.5186, 6419.2876, 1264.5518), (0.0, 0.0, -0.0), (1.5486, 0.9736, 0.1758), "DV_BP_Orc_Scaffolding_Post_1m_C14_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_Orc_Scaffolding_Post_1m_C2 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (4301.1274, 9846.385, 1345.9279), (0.0, 0.0, -0.0), (1.1974, 1.4476, 0.1558), "DV_BP_Orc_Scaffolding_Post_1m_C2_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_Orc_Scaffolding_Post_1m_C3_8 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (5152.972, 10841.239, 1346.9274), (0.0, 0.0, -0.0), (0.7085, 1.5850, 0.1558), "DV_BP_Orc_Scaffolding_Post_1m_C3_8_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_Orc_Scaffolding_Post_1m_C4 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (6715.322, 10786.819, 1307.6936), (0.0, 0.0, -0.0), (0.8996, 1.5730, 0.3443), "DV_BP_Orc_Scaffolding_Post_1m_C4_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_Orc_Scaffolding_Post_1m_C5_12 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (7512.0063, 11068.916, 1379.4203), (0.0, 0.0, -0.0), (0.3426, 1.5267, 0.5984), "DV_BP_Orc_Scaffolding_Post_1m_C5_12_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_Orc_Scaffolding_Post_1m_C6 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (9079.317, 8639.676, 1349.5533), (0.0, 0.0, -0.0), (1.5752, 0.4970, 0.1758), "DV_BP_Orc_Scaffolding_Post_1m_C6_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_Orc_Scaffolding_Post_1m_C7 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (9014.0, 7526.509, 1358.4346), (0.0, 0.0, -0.0), (1.4165, 1.2434, 0.4712), "DV_BP_Orc_Scaffolding_Post_1m_C7_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_Orc_Scaffolding_Post_1m_C8 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (8834.584, 6921.269, 1345.7062), (0.0, 0.0, -0.0), (1.2496, 1.4161, 0.1726), "DV_BP_Orc_Scaffolding_Post_1m_C8_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_Orc_Scaffolding_Post_1m_C9 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (5099.174, 6125.4233, 1349.5533), (0.0, 0.0, -0.0), (0.9736, 1.5486, 0.1758), "DV_BP_Orc_Scaffolding_Post_1m_C9_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_Orc_Scaffolding_Post_1m_D_4 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (5422.1772, 10684.131, 1399.493), (0.0, 0.0, -0.0), (1.0073, 0.6070, 0.1848), "DV_BP_Orc_Scaffolding_Post_1m_D_4_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_Orc_Scaffolding_Post_1m_D2 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (6094.4214, 11137.255, 1350.4729), (0.0, 0.0, -0.0), (1.0771, 0.5120, 0.3717), "DV_BP_Orc_Scaffolding_Post_1m_D2_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_Orc_Scaffolding_Post_1m_D3_8 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (7511.5576, 10943.372, 1389.0299), (0.0, 0.0, -0.0), (1.1002, 0.4437, 0.1620), "DV_BP_Orc_Scaffolding_Post_1m_D3_8_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_Orc_Scaffolding_Post_2m_A_4 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (5378.5615, 10762.799, 1387.5878), (0.0, 0.0, -0.0), (2.1406, 0.4083, 0.6013), "DV_BP_Orc_Scaffolding_Post_2m_A_4_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_Orc_Scaffolding_Post_2m_A2 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (6167.965, 11221.067, 1345.862), (0.0, 0.0, -0.0), (2.1145, 0.7359, 0.2302), "DV_BP_Orc_Scaffolding_Post_2m_A2_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_Orc_Scaffolding_Post_2m_B_4 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (5518.3203, 11023.157, 1353.0228), (0.0, 0.0, -0.0), (2.2486, 1.2939, 0.1382), "DV_BP_Orc_Scaffolding_Post_2m_B_4_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_Orc_Scaffolding_Post_2m_B2 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (6812.9136, 11013.542, 1344.5443), (0.0, 0.0, -0.0), (2.3990, 0.9557, 0.2018), "DV_BP_Orc_Scaffolding_Post_2m_B2_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_Orc_Scaffolding_Post_2m_B3_8 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (8220.269, 10583.854, 1346.6193), (0.0, 0.0, -0.0), (2.4052, 0.8497, 0.1461), "DV_BP_Orc_Scaffolding_Post_2m_B3_8_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_Orc_Scaffolding_Post_2m_C_2 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (4352.721, 8224.074, 1324.0532), (0.0, 0.0, -0.0), (0.5268, 2.2022, 1.1002), "DV_BP_Orc_Scaffolding_Post_2m_C_2_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_Orc_Scaffolding_Post_2m_C10 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (8166.164, 6448.392, 1344.1471), (0.0, 0.0, -0.0), (0.6224, 2.2106, 0.7022), "DV_BP_Orc_Scaffolding_Post_2m_C10_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_Orc_Scaffolding_Post_2m_C11 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (5985.851, 5929.4985, 1337.8374), (0.0, 0.0, -0.0), (1.2222, 2.1849, 0.5988), "DV_BP_Orc_Scaffolding_Post_2m_C11_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_Orc_Scaffolding_Post_2m_C2 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (4402.8267, 10139.094, 1343.8373), (0.0, 0.0, -0.0), (2.1106, 1.4807, 0.5988), "DV_BP_Orc_Scaffolding_Post_2m_C2_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_Orc_Scaffolding_Post_2m_C3_8 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (5890.835, 11215.233, 1347.733), (0.0, 0.0, -0.0), (2.0972, 1.3662, 0.2676), "DV_BP_Orc_Scaffolding_Post_2m_C3_8_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_Orc_Scaffolding_Post_2m_C4 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (6374.111, 10641.385, 1337.4706), (0.0, 0.0, -0.0), (2.1731, 0.9410, 0.6669), "DV_BP_Orc_Scaffolding_Post_2m_C4_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_Orc_Scaffolding_Post_2m_C5_12 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (7685.2407, 11016.614, 1357.6697), (0.0, 0.0, -0.0), (1.3680, 2.1574, 0.5040), "DV_BP_Orc_Scaffolding_Post_2m_C5_12_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_Orc_Scaffolding_Post_2m_C6 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (8758.649, 10006.701, 1350.9794), (0.0, 0.0, -0.0), (0.8345, 2.2110, 0.6008), "DV_BP_Orc_Scaffolding_Post_2m_C6_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_Orc_Scaffolding_Post_2m_C7 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (9007.826, 9037.094, 1340.8373), (0.0, 0.0, -0.0), (2.1106, 1.4807, 0.5988), "DV_BP_Orc_Scaffolding_Post_2m_C7_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_Orc_Scaffolding_Post_2m_C8 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (5476.8047, 5982.4287, 1340.8374), (0.0, 0.0, -0.0), (0.5175, 2.1972, 0.5988), "DV_BP_Orc_Scaffolding_Post_2m_C8_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_Orc_Scaffolding_Post_2m_C9 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (4567.4854, 7647.724, 1259.8323), (0.0, 0.0, -0.0), (0.5268, 2.2024, 0.6335), "DV_BP_Orc_Scaffolding_Post_2m_C9_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_Orc_Scaffolding_Post_2m_D_2 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (4293.8394, 8549.284, 1311.1664), (0.0, 0.0, -0.0), (0.9680, 2.1685, 0.8276), "DV_BP_Orc_Scaffolding_Post_2m_D_2_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_Orc_Scaffolding_Post_2m_D10 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (9060.658, 7700.9517, 1364.5134), (0.0, 0.0, -0.0), (1.5849, 1.9931, 0.5512), "DV_BP_Orc_Scaffolding_Post_2m_D10_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_Orc_Scaffolding_Post_2m_D11 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (5333.7773, 6092.372, 1355.4133), (0.0, 0.0, -0.0), (1.0677, 2.1654, 0.4238), "DV_BP_Orc_Scaffolding_Post_2m_D11_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_Orc_Scaffolding_Post_2m_D12 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (5133.3955, 6265.004, 1353.2534), (0.0, 0.0, -0.0), (1.5752, 1.9896, 0.4485), "DV_BP_Orc_Scaffolding_Post_2m_D12_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_Orc_Scaffolding_Post_2m_D13 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (4574.3833, 7286.0015, 1292.3527), (0.0, 0.0, -0.0), (0.9705, 2.1816, 0.4803), "DV_BP_Orc_Scaffolding_Post_2m_D13_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_Orc_Scaffolding_Post_2m_D14 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (3998.8494, 7386.6904, 1350.2386), (0.0, 0.0, -0.0), (1.8526, 1.8698, 0.4749), "DV_BP_Orc_Scaffolding_Post_2m_D14_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_Orc_Scaffolding_Post_2m_D15 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (7507.229, 6119.8057, 1351.0822), (0.0, 0.0, -0.0), (0.8650, 2.1838, 0.4244), "DV_BP_Orc_Scaffolding_Post_2m_D15_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_Orc_Scaffolding_Post_2m_D16 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (7573.5938, 6331.4644, 1351.2533), (0.0, 0.0, -0.0), (2.1825, 0.7117, 0.4485), "DV_BP_Orc_Scaffolding_Post_2m_D16_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_Orc_Scaffolding_Post_2m_D17 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (7748.383, 6676.6187, 1386.3539), (0.0, 0.0, -0.0), (0.9535, 2.0600, 1.2393), "DV_BP_Orc_Scaffolding_Post_2m_D17_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_Orc_Scaffolding_Post_2m_D18 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (6190.384, 5876.2554, 1350.4135), (0.0, 0.0, -0.0), (1.4070, 2.0718, 0.4238), "DV_BP_Orc_Scaffolding_Post_2m_D18_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_Orc_Scaffolding_Post_2m_D19 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (6582.784, 5846.5156, 1346.4814), (0.0, 0.0, -0.0), (1.2733, 2.1117, 0.3903), "DV_BP_Orc_Scaffolding_Post_2m_D19_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_Orc_Scaffolding_Post_2m_D2_5 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (3983.645, 8898.052, 1378.789), (0.0, 0.0, -0.0), (0.4692, 2.1811, 0.7803), "DV_BP_Orc_Scaffolding_Post_2m_D2_5_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_Orc_Scaffolding_Post_2m_D20 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (6065.745, 6168.8257, 1322.7942), (0.0, 0.0, -0.0), (1.2529, 2.0872, 1.0875), "DV_BP_Orc_Scaffolding_Post_2m_D20_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_Orc_Scaffolding_Post_2m_D3 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (4225.3047, 9963.166, 1348.1196), (0.0, 0.0, -0.0), (2.1745, 0.8598, 0.3197), "DV_BP_Orc_Scaffolding_Post_2m_D3_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_Orc_Scaffolding_Post_2m_D4 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (3966.963, 9511.311, 1347.2816), (0.0, 0.0, -0.0), (2.0556, 1.4641, 0.6932), "DV_BP_Orc_Scaffolding_Post_2m_D4_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_Orc_Scaffolding_Post_2m_D5_12 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (5446.157, 11049.372, 1366.6632), (0.0, 0.0, -0.0), (1.4474, 2.0560, 0.7092), "DV_BP_Orc_Scaffolding_Post_2m_D5_12_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_Orc_Scaffolding_Post_2m_D6 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (6837.141, 10924.644, 1358.9614), (0.0, 0.0, -0.0), (1.0998, 2.0759, 1.2015), "DV_BP_Orc_Scaffolding_Post_2m_D6_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_Orc_Scaffolding_Post_2m_D7_16 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (7702.003, 10261.419, 1306.4409), (0.0, 0.0, -0.0), (0.5685, 2.1627, 0.6709), "DV_BP_Orc_Scaffolding_Post_2m_D7_16_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_Orc_Scaffolding_Post_2m_D8 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (8987.057, 8857.893, 1355.4133), (0.0, 0.0, -0.0), (2.1847, 0.8611, 0.4238), "DV_BP_Orc_Scaffolding_Post_2m_D8_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_Orc_Scaffolding_Post_2m_D9 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (8942.003, 8597.27, 1353.2533), (0.0, 0.0, -0.0), (1.2733, 2.1314, 0.4485), "DV_BP_Orc_Scaffolding_Post_2m_D9_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_Orc_Scaffolding_Post_3m_B_2 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (3841.7234, 8155.281, 1346.3307), (0.0, 0.0, -0.0), (3.3358, 0.7207, 0.2954), "DV_BP_Orc_Scaffolding_Post_3m_B_2_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_Orc_Scaffolding_Post_3m_B10 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (7647.498, 6503.858, 1344.448), (0.0, 0.0, -0.0), (0.6558, 3.3605, 0.3528), "DV_BP_Orc_Scaffolding_Post_3m_B10_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_Orc_Scaffolding_Post_3m_B11 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (6567.9497, 6190.4023, 1309.7793), (0.0, 0.0, -0.0), (2.0087, 2.8417, 1.1327), "DV_BP_Orc_Scaffolding_Post_3m_B11_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_Orc_Scaffolding_Post_3m_B2 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (4757.495, 9708.328, 1318.5168), (0.0, 0.0, -0.0), (0.4161, 3.3595, 0.2955), "DV_BP_Orc_Scaffolding_Post_3m_B2_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_Orc_Scaffolding_Post_3m_B3_8 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (5644.0254, 11056.015, 1351.6406), (0.0, 0.0, -0.0), (2.8379, 2.1904, 0.3224), "DV_BP_Orc_Scaffolding_Post_3m_B3_8_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_Orc_Scaffolding_Post_3m_B4 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (6587.386, 10616.1045, 1352.982), (0.0, 0.0, -0.0), (2.5301, 2.5721, 0.5539), "DV_BP_Orc_Scaffolding_Post_3m_B4_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_Orc_Scaffolding_Post_3m_B5_12 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (8020.1636, 10645.303, 1347.2122), (0.0, 0.0, -0.0), (1.2908, 3.2565, 0.1798), "DV_BP_Orc_Scaffolding_Post_3m_B5_12_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_Orc_Scaffolding_Post_3m_B6 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (8800.951, 9594.12, 1407.4863), (0.0, 0.0, -0.0), (0.4977, 3.3367, 0.7516), "DV_BP_Orc_Scaffolding_Post_3m_B6_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_Orc_Scaffolding_Post_3m_B7 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (9077.161, 8439.233, 1347.8964), (0.0, 0.0, -0.0), (2.5984, 2.4918, 0.1911), "DV_BP_Orc_Scaffolding_Post_3m_B7_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_Orc_Scaffolding_Post_3m_B8 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (4928.358, 6230.3203, 1347.8964), (0.0, 0.0, -0.0), (3.2987, 1.1321, 0.1911), "DV_BP_Orc_Scaffolding_Post_3m_B8_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_Orc_Scaffolding_Post_3m_B9 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (4370.363, 6665.29, 1356.4319), (0.0, 0.0, -0.0), (1.5157, 3.1338, 0.5095), "DV_BP_Orc_Scaffolding_Post_3m_B9_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_Orc_Scaffolding_Post_3m_C_2 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (3857.7842, 8300.918, 1348.3192), (0.0, 0.0, -0.0), (1.9857, 2.8117, 0.2829), "DV_BP_Orc_Scaffolding_Post_3m_C_2_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_Orc_Scaffolding_Post_3m_C10 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (7959.238, 6386.681, 1348.6237), (0.0, 0.0, -0.0), (2.9741, 1.7207, 0.3277), "DV_BP_Orc_Scaffolding_Post_3m_C10_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_Orc_Scaffolding_Post_3m_C11 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (6789.0693, 5921.024, 1347.6235), (0.0, 0.0, -0.0), (2.9175, 1.8492, 0.3277), "DV_BP_Orc_Scaffolding_Post_3m_C11_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_Orc_Scaffolding_Post_3m_C2 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (4627.482, 9707.762, 1289.0464), (0.0, 0.0, -0.0), (0.3709, 3.1568, 0.3627), "DV_BP_Orc_Scaffolding_Post_3m_C2_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_Orc_Scaffolding_Post_3m_C3_8 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (5464.0933, 10531.363, 1394.3938), (0.0, 0.0, -0.0), (2.6495, 2.1013, 1.0965), "DV_BP_Orc_Scaffolding_Post_3m_C3_8_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_Orc_Scaffolding_Post_3m_C4 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (6237.17, 11084.006, 1344.797), (0.0, 0.0, -0.0), (2.4407, 2.4558, 0.2349), "DV_BP_Orc_Scaffolding_Post_3m_C4_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_Orc_Scaffolding_Post_3m_C5_12 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (7849.859, 10568.27, 1346.0663), (0.0, 0.0, -0.0), (2.9030, 1.8248, 0.2394), "DV_BP_Orc_Scaffolding_Post_3m_C5_12_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_Orc_Scaffolding_Post_3m_C6 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (8900.914, 8247.491, 1349.6237), (0.0, 0.0, -0.0), (2.4189, 2.5322, 0.3277), "DV_BP_Orc_Scaffolding_Post_3m_C6_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_Orc_Scaffolding_Post_3m_C7 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (8979.926, 7205.8696, 1349.1327), (0.0, 0.0, -0.0), (0.7429, 3.1685, 0.3210), "DV_BP_Orc_Scaffolding_Post_3m_C7_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_Orc_Scaffolding_Post_3m_C8 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (4854.506, 6480.0674, 1349.6235), (0.0, 0.0, -0.0), (1.1962, 3.1267, 0.3277), "DV_BP_Orc_Scaffolding_Post_3m_C8_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_Orc_Scaffolding_Post_3m_C9 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (4171.828, 7096.982, 1348.2635), (0.0, 0.0, -0.0), (3.1629, 0.5249, 0.2766), "DV_BP_Orc_Scaffolding_Post_3m_C9_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_Orc_Scaffolding_Post_3m_D_2 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (4100.226, 8256.28, 1342.7332), (0.0, 0.0, -0.0), (3.0596, 2.1543, 0.8333), "DV_BP_Orc_Scaffolding_Post_3m_D_2_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_Orc_Scaffolding_Post_3m_D10 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (8495.798, 8012.8325, 1276.9891), (0.0, 0.0, -0.0), (2.4730, 2.9685, 0.6299), "DV_BP_Orc_Scaffolding_Post_3m_D10_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_Orc_Scaffolding_Post_3m_D11 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (8798.888, 8956.855, 1373.4778), (0.0, 0.0, -0.0), (2.5051, 2.8650, 0.7745), "DV_BP_Orc_Scaffolding_Post_3m_D11_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_Orc_Scaffolding_Post_3m_D12 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (4708.5044, 7412.1216, 1285.2411), (0.0, 0.0, -0.0), (1.8398, 3.2178, 0.7088), "DV_BP_Orc_Scaffolding_Post_3m_D12_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_Orc_Scaffolding_Post_3m_D13 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (5515.3984, 6202.892, 1373.4778), (0.0, 0.0, -0.0), (1.6454, 3.2217, 0.7746), "DV_BP_Orc_Scaffolding_Post_3m_D13_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_Orc_Scaffolding_Post_3m_D14 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (4425.0063, 6968.938, 1362.8534), (0.0, 0.0, -0.0), (2.5507, 2.7923, 0.8052), "DV_BP_Orc_Scaffolding_Post_3m_D14_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_Orc_Scaffolding_Post_3m_D15 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (4522.8906, 7974.0684, 1324.7755), (0.0, 0.0, -0.0), (3.2667, 1.2298, 0.5497), "DV_BP_Orc_Scaffolding_Post_3m_D15_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_Orc_Scaffolding_Post_3m_D16 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (7348.036, 6067.129, 1365.4777), (0.0, 0.0, -0.0), (3.2001, 1.8128, 0.7746), "DV_BP_Orc_Scaffolding_Post_3m_D16_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_Orc_Scaffolding_Post_3m_D17 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (6316.0347, 6347.752, 1278.7181), (0.0, 0.0, -0.0), (2.6204, 2.7713, 0.7328), "DV_BP_Orc_Scaffolding_Post_3m_D17_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_Orc_Scaffolding_Post_3m_D2_5 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (4159.141, 8739.377, 1359.8971), (0.0, 0.0, -0.0), (3.0482, 2.1355, 1.1544), "DV_BP_Orc_Scaffolding_Post_3m_D2_5_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_Orc_Scaffolding_Post_3m_D3 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (4601.771, 9968.045, 1318.1113), (0.0, 0.0, -0.0), (3.2653, 0.8779, 1.3487), "DV_BP_Orc_Scaffolding_Post_3m_D3_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_Orc_Scaffolding_Post_3m_D4 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (4153.533, 9778.029, 1347.6727), (0.0, 0.0, -0.0), (1.4367, 3.2489, 0.5642), "DV_BP_Orc_Scaffolding_Post_3m_D4_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_Orc_Scaffolding_Post_3m_D5_12 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (4909.3364, 10589.538, 1349.3318), (0.0, 0.0, -0.0), (3.1406, 1.8944, 0.3680), "DV_BP_Orc_Scaffolding_Post_3m_D5_12_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_Orc_Scaffolding_Post_3m_D6 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (6862.8286, 11104.591, 1352.5193), (0.0, 0.0, -0.0), (2.5529, 2.8368, 0.6950), "DV_BP_Orc_Scaffolding_Post_3m_D6_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_Orc_Scaffolding_Post_3m_D7_16 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (7569.669, 10281.691, 1318.9993), (0.0, 0.0, -0.0), (1.4688, 3.2518, 0.7696), "DV_BP_Orc_Scaffolding_Post_3m_D7_16_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_Orc_Scaffolding_Post_3m_D8_19 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (7258.307, 10360.926, 1348.9058), (0.0, 0.0, -0.0), (3.2398, 1.4563, 1.1221), "DV_BP_Orc_Scaffolding_Post_3m_D8_19_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_Orc_Scaffolding_Post_3m_D9_22 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (8923.629, 9785.413, 1360.8246), (0.0, 0.0, -0.0), (1.3584, 3.2615, 0.5523), "DV_BP_Orc_Scaffolding_Post_3m_D9_22_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_Orc_Scaffolding_Post_4m_A_4 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (5143.9507, 10433.145, 1327.0125), (0.0, 0.0, -0.0), (2.3937, 3.8409, 0.3570), "DV_BP_Orc_Scaffolding_Post_4m_A_4_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_Orc_Scaffolding_Post_4m_A2 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (6525.8936, 10838.623, 1339.9916), (0.0, 0.0, -0.0), (1.8322, 4.0954, 0.6480), "DV_BP_Orc_Scaffolding_Post_4m_A2_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_Orc_Scaffolding_Post_4m_A3_8 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (7306.02, 10383.192, 1327.3129), (0.0, 0.0, -0.0), (3.3043, 3.1192, 0.3101), "DV_BP_Orc_Scaffolding_Post_4m_A3_8_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_Orc_Scaffolding_Post_4m_B_2 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (4203.593, 8686.3, 1347.1227), (0.0, 0.0, -0.0), (0.2977, 4.3271, 1.5406), "DV_BP_Orc_Scaffolding_Post_4m_B_2_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_Orc_Scaffolding_Post_4m_B2 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (3967.7256, 9597.82, 1344.5833), (0.0, 0.0, -0.0), (4.4836, 0.6832, 0.2704), "DV_BP_Orc_Scaffolding_Post_4m_B2_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_Orc_Scaffolding_Post_4m_B3_8 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (5279.904, 10902.681, 1346.5153), (0.0, 0.0, -0.0), (2.1808, 4.1692, 0.2074), "DV_BP_Orc_Scaffolding_Post_4m_B3_8_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_Orc_Scaffolding_Post_4m_B4 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (6254.9717, 10839.953, 1334.915), (0.0, 0.0, -0.0), (2.3164, 4.1019, 0.7604), "DV_BP_Orc_Scaffolding_Post_4m_B4_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_Orc_Scaffolding_Post_4m_B5_12 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (7523.4854, 10784.861, 1373.844), (0.0, 0.0, -0.0), (4.4677, 0.3489, 0.7776), "DV_BP_Orc_Scaffolding_Post_4m_B5_12_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_Orc_Scaffolding_Post_4m_B6 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (8819.412, 9541.783, 1499.4417), (0.0, 0.0, -0.0), (3.2006, 1.5031, 3.3866), "DV_BP_Orc_Scaffolding_Post_4m_B6_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_Orc_Scaffolding_Post_4m_B7 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (8516.693, 8337.47, 1264.0615), (0.0, 0.0, -0.0), (2.6248, 3.9620, 0.4909), "DV_BP_Orc_Scaffolding_Post_4m_B7_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_Orc_Scaffolding_Post_4m_B8 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (5342.622, 6826.915, 1349.0295), (0.0, 0.0, -0.0), (4.3964, 1.4438, 0.6147), "DV_BP_Orc_Scaffolding_Post_4m_B8_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_Orc_Scaffolding_Post_4m_B9 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (4335.2305, 7651.9624, 1290.3408), (0.0, 0.0, -0.0), (2.0792, 4.2095, 0.6605), "DV_BP_Orc_Scaffolding_Post_4m_B9_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_Orc_Scaffolding_Post_5m_D_2 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (3801.692, 8919.829, 1338.8657), (0.0, 0.0, -0.0), (3.8079, 5.4200, 0.4833), "DV_BP_Orc_Scaffolding_Post_5m_D_2_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_Orc_Scaffolding_Post_5m_D10 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (5408.015, 6611.3853, 1342.8647), (0.0, 0.0, -0.0), (5.5223, 2.2352, 1.4709), "DV_BP_Orc_Scaffolding_Post_5m_D10_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_Orc_Scaffolding_Post_5m_D11 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (4162.015, 7514.469, 1342.5918), (0.0, 0.0, -0.0), (1.4436, 5.3802, 0.4833), "DV_BP_Orc_Scaffolding_Post_5m_D11_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_Orc_Scaffolding_Post_5m_D12 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (4089.6543, 7446.348, 1309.7217), (0.0, 0.0, -0.0), (3.9925, 5.3961, 1.3968), "DV_BP_Orc_Scaffolding_Post_5m_D12_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_Orc_Scaffolding_Post_5m_D13 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (6920.088, 5992.881, 1344.9282), (0.0, 0.0, -0.0), (3.1059, 5.5742, 0.7179), "DV_BP_Orc_Scaffolding_Post_5m_D13_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_Orc_Scaffolding_Post_5m_D2 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (4231.1978, 9581.252, 1342.828), (0.0, 0.0, -0.0), (4.1799, 5.2730, 0.4833), "DV_BP_Orc_Scaffolding_Post_5m_D2_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_Orc_Scaffolding_Post_5m_D3 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (4752.917, 9466.928, 1319.9581), (0.0, 0.0, -0.0), (4.1154, 5.3531, 1.3968), "DV_BP_Orc_Scaffolding_Post_5m_D3_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_Orc_Scaffolding_Post_5m_D4_9 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (5209.463, 10552.556, 1351.772), (0.0, 0.0, -0.0), (4.2291, 5.3012, 0.6866), "DV_BP_Orc_Scaffolding_Post_5m_D4_9_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_Orc_Scaffolding_Post_5m_D5 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (6812.406, 10790.935, 1335.2611), (0.0, 0.0, -0.0), (3.8674, 5.4270, 1.2100), "DV_BP_Orc_Scaffolding_Post_5m_D5_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_Orc_Scaffolding_Post_5m_D6_13 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (7567.646, 10593.368, 1367.2701), (0.0, 0.0, -0.0), (5.5130, 3.4904, 1.4977), "DV_BP_Orc_Scaffolding_Post_5m_D6_13_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_Orc_Scaffolding_Post_5m_D7 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (8728.17, 8265.738, 1320.558), (0.0, 0.0, -0.0), (5.0565, 4.4932, 1.6928), "DV_BP_Orc_Scaffolding_Post_5m_D7_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_Orc_Scaffolding_Post_5m_D8 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (8430.18, 8806.222, 1270.8607), (0.0, 0.0, -0.0), (3.1050, 5.5769, 0.7134), "DV_BP_Orc_Scaffolding_Post_5m_D8_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_Orc_Scaffolding_Post_5m_D9 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (4958.9653, 6618.855, 1327.5599), (0.0, 0.0, -0.0), (2.2722, 5.4961, 1.6928), "DV_BP_Orc_Scaffolding_Post_5m_D9_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: CBP_MapStone_World_2 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (1194.4701, 9530.486, 900.00354), (0.0, 140.00012387272128, -0.0), (2.0000, 2.0000, 2.3053), "DV_CBP_MapStone_World_2", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: DecorationBlockingVolume_1 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (10310.832, 8560.8, 1949.5819), (0.0, 0.0, -0.0), (2.0000, 2.0000, 2.0000), "DV_DecorationBlockingVolume_1", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: Rubble_Masonry_Pile_C_220 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (5456.374, 6670.6953, 1273.3663), (0.0, 0.0, -0.0), (2.3692, 2.4198, 0.9351), "DV_Rubble_Masonry_Pile_C_220_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: Rubble_Masonry_Pile_C2_260 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (5190.679, 9752.165, 1285.8546), (0.0, 0.0, -0.0), (2.4543, 2.4068, 0.9351), "DV_Rubble_Masonry_Pile_C2_260_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: Rubble_Masonry_Pile_C3_286 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (6845.7373, 9726.768, 1675.4481), (0.0, 0.0, -0.0), (2.6374, 2.4486, 1.5038), "DV_Rubble_Masonry_Pile_C3_286_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: Rubble_Masonry_Pile_C4 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (6300.1777, 9711.419, 1730.4982), (0.0, 0.0, -0.0), (2.6374, 2.5165, 1.6936), "DV_Rubble_Masonry_Pile_C4_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: Rubble_Masonry_Pile_E_186 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (8028.399, 7551.737, 1274.4218), (0.0, 0.0, -0.0), (2.2457, 2.5083, 1.3025), "DV_Rubble_Masonry_Pile_E_186_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: Rubble_Masonry_Pile_E2_257 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (5713.886, 9482.355, 1778.6082), (0.0, 0.0, -0.0), (2.9720, 2.5309, 1.8530), "DV_Rubble_Masonry_Pile_E2_257_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: Rubble_Masonry_Pile_F_198 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (7539.662, 7691.8823, 1338.7991), (0.0, 0.0, -0.0), (5.6800, 5.3275, 3.0075), "DV_Rubble_Masonry_Pile_F_198_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: Rubble_Masonry_Pile_F10 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (6192.333, 10013.113, 1575.6252), (0.0, 0.0, -0.0), (5.9158, 5.8031, 3.3409), "DV_Rubble_Masonry_Pile_F10_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: Rubble_Masonry_Pile_F11 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (7234.182, 8066.4326, 1720.5651), (0.0, 0.0, -0.0), (5.9344, 6.0393, 2.3022), "DV_Rubble_Masonry_Pile_F11_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: Rubble_Masonry_Pile_F12 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (7614.6016, 8437.453, 1616.9657), (0.0, 0.0, -0.0), (5.6424, 6.0356, 3.3838), "DV_Rubble_Masonry_Pile_F12_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: Rubble_Masonry_Pile_F2_201 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (5467.175, 6950.518, 1288.9662), (0.0, 0.0, -0.0), (4.0437, 4.4301, 1.3764), "DV_Rubble_Masonry_Pile_F2_201_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: Rubble_Masonry_Pile_F3 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (5815.6504, 7274.7, 1287.9127), (0.0, 0.0, -0.0), (4.0437, 4.4250, 1.7029), "DV_Rubble_Masonry_Pile_F3_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: Rubble_Masonry_Pile_F4 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (5301.6274, 7029.0176, 1278.1403), (0.0, 0.0, -0.0), (5.0210, 4.6902, 1.3366), "DV_Rubble_Masonry_Pile_F4_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: Rubble_Masonry_Pile_F6 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (4553.432, 8178.5684, 1281.9911), (0.0, 0.0, -0.0), (4.9974, 4.6747, 1.3764), "DV_Rubble_Masonry_Pile_F6_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: Rubble_Masonry_Pile_F7 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (5409.873, 9268.669, 1282.269), (0.0, 0.0, -0.0), (5.7941, 5.5360, 1.7806), "DV_Rubble_Masonry_Pile_F7_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: Rubble_Masonry_Pile_F8 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (5130.3916, 9495.29, 1292.9813), (0.0, 0.0, -0.0), (5.7266, 5.5062, 1.3091), "DV_Rubble_Masonry_Pile_F8_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: Rubble_Masonry_Pile_F9 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (7082.276, 9929.22, 1288.3145), (0.0, 0.0, -0.0), (5.7419, 5.5629, 1.6691), "DV_Rubble_Masonry_Pile_F9_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: Rubble_Masonry_Pile_H_177 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (7897.124, 8088.5884, 1286.6133), (0.0, 0.0, -0.0), (2.5859, 3.1028, 1.3071), "DV_Rubble_Masonry_Pile_H_177_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: Rubble_Masonry_Pile_H2_180 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (7623.3535, 7849.3228, 1352.3949), (0.0, 0.0, -0.0), (4.0235, 3.5692, 2.2101), "DV_Rubble_Masonry_Pile_H2_180_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: Rubble_Masonry_Pile_H3 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (7357.006, 9317.319, 1648.3138), (0.0, 0.0, -0.0), (3.4667, 2.8085, 2.7279), "DV_Rubble_Masonry_Pile_H3_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: Rubble_Masonry_Pile_H4 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (7491.0757, 9257.864, 1276.2568), (0.0, 0.0, -0.0), (3.9613, 4.0455, 1.4217), "DV_Rubble_Masonry_Pile_H4_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: Rubble_Masonry_Pile_I_192 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (7656.753, 8365.192, 1297.449), (0.0, 0.0, -0.0), (4.3718, 2.3715, 3.1768), "DV_Rubble_Masonry_Pile_I_192_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: Rubble_Masonry_Pile_I2 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (7057.175, 9179.855, 1765.0359), (0.0, 0.0, -0.0), (3.1064, 4.4047, 1.6000), "DV_Rubble_Masonry_Pile_I2_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: Rubble_Masonry_Pile_I3 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (7460.4395, 9157.178, 1657.5105), (0.0, 0.0, -0.0), (2.7389, 4.2228, 2.8380), "DV_Rubble_Masonry_Pile_I3_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: Warehouse_Barrel_425 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (5508.625, 9133.463, 1304.791), (0.0, 0.0, -0.0), (1.0832, 0.8004, 1.1168), "DV_Warehouse_Barrel_425_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: Warehouse_Barrel2_428 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (6260.1714, 9287.575, 1817.551), (0.0, 0.0, -0.0), (1.0380, 0.8004, 1.0918), "DV_Warehouse_Barrel2_428_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: Warehouse_Barrel3_431 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (6292.867, 9842.285, 1677.115), (0.0, 0.0, -0.0), (1.0607, 1.0095, 1.2396), "DV_Warehouse_Barrel3_431_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: Warehouse_Barrel4_443 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (7451.7046, 9578.34, 1276.6838), (0.0, 0.0, -0.0), (0.7330, 1.1609, 1.1489), "DV_Warehouse_Barrel4_443_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: Warehouse_Barrel5_461 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (5917.455, 7179.224, 1280.3674), (0.0, 0.0, -0.0), (1.3230, 1.1588, 1.3487), "DV_Warehouse_Barrel5_461_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: Warehouse_Barrel6 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (5987.6753, 7319.8164, 1282.5822), (0.0, 0.0, -0.0), (1.3060, 1.0802, 1.1923), "DV_Warehouse_Barrel6_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: Warehouse_Crate_A_380 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (5543.453, 7496.4277, 1400.6631), (0.0, 0.0, -0.0), (1.0273, 1.1404, 0.9168), "DV_Warehouse_Crate_A_380_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: Warehouse_Crate_A_Lid_446 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (7550.22, 9498.3545, 1265.3575), (0.0, 0.0, -0.0), (0.7648, 0.7536, 0.2972), "DV_Warehouse_Crate_A_Lid_446_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: Warehouse_Crate_A_Open_383 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (5440.4287, 8441.093, 1702.2396), (0.0, 0.0, -0.0), (0.9325, 1.0997, 0.9459), "DV_Warehouse_Crate_A_Open_383_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: Warehouse_Crate_A_Open2_458 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (6977.902, 7597.871, 1646.908), (0.0, 0.0, -0.0), (0.9973, 1.2308, 1.1888), "DV_Warehouse_Crate_A_Open2_458_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: Warehouse_Crate_B_377 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (7131.4146, 7482.5244, 1596.6315), (0.0, 0.0, -0.0), (1.4870, 1.2477, 0.9686), "DV_Warehouse_Crate_B_377_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: Warehouse_Crate_B_Broken_50 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (6857.8354, 7574.6094, 1674.052), (0.0, 0.0, -0.0), (1.2553, 1.2908, 1.3905), "DV_Warehouse_Crate_B_Broken_50_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: Warehouse_Crate_B_Broken2_437 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (6948.6797, 9858.56, 1285.7893), (0.0, 0.0, -0.0), (1.4165, 1.4673, 1.0257), "DV_Warehouse_Crate_B_Broken2_437_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: Warehouse_Crate_B_Broken3_449 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (7932.9053, 8266.084, 1276.7158), (0.0, 0.0, -0.0), (1.4335, 1.3879, 1.0248), "DV_Warehouse_Crate_B_Broken3_449_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: Warehouse_Crate_B_Lid_434 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (7090.3975, 9819.076, 1305.2372), (0.0, 0.0, -0.0), (1.1987, 0.5306, 0.7099), "DV_Warehouse_Crate_B_Lid_434_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: Warehouse_Crate_B_Lid2_455 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (7013.5967, 7330.6553, 1276.8108), (0.0, 0.0, -0.0), (0.9558, 1.3191, 1.0001), "DV_Warehouse_Crate_B_Lid2_455_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: Warehouse_Crate_B_Lid3 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (6747.6934, 9688.274, 1721.8484), (0.0, 0.0, -0.0), (1.3359, 1.0512, 0.9604), "DV_Warehouse_Crate_B_Lid3_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: Warehouse_Crate_B_open_368 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (6993.613, 9631.253, 1692.6605), (0.0, 0.0, -0.0), (1.3376, 1.3801, 1.1183), "DV_Warehouse_Crate_B_open_368_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: Warehouse_Crate_B_open2_374 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (7173.2188, 8988.122, 1774.2869), (0.0, 0.0, -0.0), (1.4440, 1.4012, 1.1713), "DV_Warehouse_Crate_B_open2_374_BRK", _folder)
if a: placed += 1
else: skipped += 1

# ======================================================================
# SUMMARY
# ======================================================================
unreal.log(f"[{BUBBLE_NAME}] Reconstruction complete: {placed} placed, {skipped} skipped, {errors} errors")
