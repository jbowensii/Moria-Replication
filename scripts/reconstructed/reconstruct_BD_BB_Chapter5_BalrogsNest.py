"""Auto-generated level reconstruction script.
Bubble: BD_BB_Chapter5_BalrogsNest
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

BUBBLE_NAME = "BD_BB_Chapter5_BalrogsNest"
placed = 0
skipped = 0
errors = 0

# ======================================================================
# PHASE 1: InstancedMeshCatalog  (static mesh placement)
# ======================================================================
unreal.log(f"[{BUBBLE_NAME}] Phase 1: Placing static meshes...")

# Batch 0: StaticMesh'Architectural_sunstone_window_large' (1 instances)
_mesh_path = "/Game/Art/Assets/Kits/Architecture/City/Architectural_sunstone_window_large"
_materials = ['/Game/Art/Assets/Kits/Architecture/Suburbs/Materials/Suburbs_Trim_Sheet_A/MI_Suburbs_Trim_Sheet_A', '/Game/Environments/Materials/MI_CrystalRoofBright']
_folder = "Reconstruction/BD_BB_Chapter5_BalrogsNest/Meshes"
a = spawn_static_mesh(_mesh_path, _materials, (9060.0, 6375.0, 4210.0), (0.0, 90.00004680423052, -0.0), (0.69953835, 1.0, 1.0), "Architectural_sunstone_window_large_33", _folder)
if a: placed += 1
else: skipped += 1

# Batch 1: StaticMesh'Architectural_sunstone_window_small' (2 instances)
_mesh_path = "/Game/Art/Assets/Kits/Architecture/City/Architectural_sunstone_window_small"
_materials = ['/Game/Art/Assets/Kits/Architecture/Suburbs/Materials/Suburbs_Trim_Sheet_A/MI_Suburbs_Trim_Sheet_A', '/Game/Environments/Materials/MI_CrystalRoofBright']
_folder = "Reconstruction/BD_BB_Chapter5_BalrogsNest/Meshes"
a = spawn_static_mesh(_mesh_path, _materials, (9625.0, 6330.0, 4200.0), (0.0, 0.0, -0.0), (1.0, 1.0, 1.0), "Architectural_sunstone_window_small_36", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (8490.0, 6330.0, 4200.0), (0.0, 0.0, -0.0), (1.0, 1.0, 1.0), "Architectural_sunstone_window_small2", _folder)
if a: placed += 1
else: skipped += 1

# Batch 2: StaticMesh'Deep_ArchPiece_A' (1 instances)
_mesh_path = "/Game/Art/Assets/Kits/Architecture/Deep/Deep_ArchPiece_A"
_materials = ['/Game/Art/Assets/Kits/Architecture/Deep/Materials/Deep_TrimSheet/MI_Deep_TrimSheet', '/Game/Environments/Materials/MI_Suburbs_Non_Destructible']
_folder = "Reconstruction/BD_BB_Chapter5_BalrogsNest/Meshes"
a = spawn_static_mesh(_mesh_path, _materials, (5133.938, 5145.497, 2350.125), (0.0, 0.0, -0.0), (1.0, 1.0, 1.0), "Deep_ArchPiece_A8", _folder)
if a: placed += 1
else: skipped += 1

# Batch 3: StaticMesh'Deep_BarlogsNest_Crevice' (8 instances)
_mesh_path = "/Game/Art/Assets/Kits/Architecture/Deep/Deep_BarlogsNest_Crevice"
_materials = ['/Game/Art/Assets/Kits/Architecture/Deep/Materials/Deep_BarlogsNest_Crevice/MI_Deep_BarlogsNest_Crevice']
_folder = "Reconstruction/BD_BB_Chapter5_BalrogsNest/Meshes"
a = spawn_static_mesh(_mesh_path, _materials, (10398.865, 6696.4824, 801.7998), (0.0, 95.14385120869156, -0.0), (1.0425, 1.245, 1.0), "Deep_BarlogsNest_Crevice_2", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (11074.536, 6803.0396, 793.1637), (0.11777299860946983, 93.74117543932863, -1.8004760909741624), (0.9375, 1.9575, 0.93), "Deep_BarlogsNest_Crevice2", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (11211.041, 6776.7812, 818.2057), (0.0, 93.74306470931181, -0.0), (0.91999996, 1.7249999, 0.80740386), "Deep_BarlogsNest_Crevice3", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (11890.032, 6799.5283, 843.3068), (-2.0957334454277556, 96.79028489512551, -4.072631531494471), (0.695, 2.11, 0.6690719), "Deep_BarlogsNest_Crevice5", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (12560.405, 6850.9355, 729.3567), (-4.60848987082023, 96.79816075040003, -5.44033735162237), (0.695, 2.11, 0.669072), "Deep_BarlogsNest_Crevice6", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (13238.915, 6892.217, 705.0538), (6.729525448766012, 96.81201813726057, -5.093109081644402), (0.56, 1.7001438, 0.5391084), "Deep_BarlogsNest_Crevice7", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (13742.037, 6969.0757, 594.72003), (6.663785336322267, 96.75886736362799, -8.466278215781644), (0.49249998, 1.4952153, 0.4741269), "Deep_BarlogsNest_Crevice8", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (14191.425, 6981.684, 493.85553), (-5.23910543454251, 96.41206540851032, -20.799410720631304), (0.41, 1.244747, 0.3947041), "Deep_BarlogsNest_Crevice9", _folder)
if a: placed += 1
else: skipped += 1

# Batch 4: StaticMesh'Deep_BarlogsNest_MeltedStone_A' (20 instances)
_mesh_path = "/Game/Art/Assets/Kits/Architecture/Deep/Deep_BarlogsNest_MeltedStone_A"
_materials = ['/Game/Art/Assets/Kits/Architecture/Deep/Materials/Deep_BarlogsNest_MeltedStone/MI_Deep_BarlogsNest_MeltedStone']
_folder = "Reconstruction/BD_BB_Chapter5_BalrogsNest/Meshes"
a = spawn_static_mesh(_mesh_path, _materials, (9730.493, 5481.5396, 789.3463), (0.0, -140.8153791215668, 0.0), (1.0, 1.0, 1.0), "Deep_BarlogsNest_MeltedStone_A_2", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (7805.7505, 6709.3247, 736.02637), (0.820148539513507, -17.81698429906518, -3.7539667830466334), (1.0, 1.0, 1.0), "Deep_BarlogsNest_MeltedStone_A11", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (8089.993, 5552.924, 761.8391), (0.5903468243290005, -1.3653258153659678, 1.4082773598484832), (1.0, 1.0, 1.0), "Deep_BarlogsNest_MeltedStone_A12", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (10690.903, 5851.6553, 994.4424), (-0.419738674042293, 124.13805282957664, 2.122638385732781), (1.0, 1.0, 1.0), "Deep_BarlogsNest_MeltedStone_A13", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (9867.281, 4875.3135, 871.313), (0.0, 5.264130469566673, -0.0), (1.0, 1.0, 1.0), "Deep_BarlogsNest_MeltedStone_A14", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (9394.638, 4418.9326, 812.6803), (3.2971371536210223, 23.36814360778461, 2.3347016944689027), (1.0, 1.0, 1.0), "Deep_BarlogsNest_MeltedStone_A15", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (9862.994, 7855.0605, 796.084), (0.958657940434136, -146.35808319802115, -0.8083193224079482), (1.0, 1.0, 0.796876), "Deep_BarlogsNest_MeltedStone_A16", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (9368.609, 8688.096, 777.8799), (0.9586578982499274, -138.16673079473367, -0.8083191740797407), (1.0, 1.0, 0.796876), "Deep_BarlogsNest_MeltedStone_A17", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (8371.648, 8279.153, 775.5967), (0.9586579522179861, -89.35412976807542, -0.8083191629861723), (1.0, 1.0, 0.796876), "Deep_BarlogsNest_MeltedStone_A18", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (8035.664, 7150.8984, 784.43964), (-1.2320860165907246, 50.72341636073133, -3.0046383733862636), (0.777737, 0.7777368, 0.6998663), "Deep_BarlogsNest_MeltedStone_A19", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (6467.187, 5490.3584, 794.6382), (-0.03775024174701467, -10.104552681656875, 0.818795343132679), (1.0, 1.0, 1.1670207), "Deep_BarlogsNest_MeltedStone_A2", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (10124.255, 6034.0923, 789.34625), (0.0, 31.484801323591004, -0.0), (1.0, 1.0, 1.0), "Deep_BarlogsNest_MeltedStone_A20", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (8930.863, 4328.85, 781.961), (1.7104913071616248, -76.94491661943322, -3.6596682584621383), (1.0, 1.0, 1.5581355), "Deep_BarlogsNest_MeltedStone_A21", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (7635.72, 6637.7, 759.21277), (0.0, -172.4170187008518, 0.0), (1.0, 1.0, 1.0), "Deep_BarlogsNest_MeltedStone_A22_144", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (7681.964, 5583.2715, 780.3872), (1.2199706269626523e-08, 8.98284888464685, 6.254453015342735), (1.0, 1.0, 1.0), "Deep_BarlogsNest_MeltedStone_A3", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (7946.0195, 6928.1987, 773.0801), (-1.377288836923889, 29.537658387226955, 3.525735771018323), (1.0, 1.0, 1.0), "Deep_BarlogsNest_MeltedStone_A4", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (6821.1777, 6737.717, 790.7186), (2.929970390706522, 160.66894279323168, 3.6640501008884176), (0.924834, 0.924834, 0.8342956), "Deep_BarlogsNest_MeltedStone_A5_271", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (6214.5312, 6576.485, 752.75977), (0.8640940938153453, -20.996796215669146, 2.303764999945677), (0.924834, 0.924834, 0.924834), "Deep_BarlogsNest_MeltedStone_A6", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (6397.6777, 6397.0654, 734.33887), (4.793645797859124, -53.316340504260815, 4.022130911842407), (1.0, 1.0, 1.0), "Deep_BarlogsNest_MeltedStone_A7", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (9825.304, 7371.039, 774.96893), (0.7354610550621821, 111.41108657183747, -1.0155943889493364), (1.0, 1.0, 0.7968757), "Deep_BarlogsNest_MeltedStone_A9", _folder)
if a: placed += 1
else: skipped += 1

# Batch 5: StaticMesh'Deep_BoneHoard_F' (2 instances)
_mesh_path = "/Game/Art/Assets/Kits/Architecture/Deep/Deep_BoneHoard_F"
_materials = ['/Game/Art/Assets/Kits/Misc/Dirt_Mounds/Materials/MI_DirtMound_Mines']
_folder = "Reconstruction/BD_BB_Chapter5_BalrogsNest/Meshes"
a = spawn_static_mesh(_mesh_path, _materials, (9293.037, 6502.303, 795.03174), (1.2585715497893184, -155.46730599675587, 1.0091076910981105), (1.0, 1.0, 0.84526783), "Deep_BoneHoard_F_59", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (8984.067, 6502.3037, 795.0303), (1.2585718158767778, -167.63522012401097, 1.0091083088700596), (1.0, 1.0, 0.845268), "Deep_BoneHoard_F2", _folder)
if a: placed += 1
else: skipped += 1

# Batch 6: StaticMesh'Deep_CircleFloor_B' (1 instances)
_mesh_path = "/Game/Art/Assets/Kits/Architecture/Deep/Deep_CircleFloor_B"
_materials = ['/Game/Art/Assets/Kits/Architecture/Deep/Materials/Deep_TrimSheet/MI_Deep_TrimSheet', '/Game/Art/Assets/Kits/Architecture/Deep/Materials/Deep_TrimSheet/MI_Deep_TrimSheet']
_folder = "Reconstruction/BD_BB_Chapter5_BalrogsNest/Meshes"
a = spawn_static_mesh(_mesh_path, _materials, (9050.799, 6430.6997, 801.1929), (0.0, -90.0001164887758, 0.0), (1.0, 1.0, 1.0), "Deep_CircleFloor_B_282", _folder)
if a: placed += 1
else: skipped += 1

# Batch 7: StaticMesh'Deep_WoodenBeam_A' (15 instances)
_mesh_path = "/Game/Art/Assets/Kits/Architecture/Deep/Deep_WoodenBeam_A"
_materials = ['/Game/Art/Assets/Kits/Architecture/Deep/Materials/Deep_WoodTrim/MI_Deep_WoodTrim']
_folder = "Reconstruction/BD_BB_Chapter5_BalrogsNest/Meshes"
a = spawn_static_mesh(_mesh_path, _materials, (2111.4863, 5939.296, 800.50977), (0.0, 113.93135532033475, -0.0), (1.0, 1.0, 1.0), "Deep_WoodenBeam_A10_282", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1180.5732, 4192.084, 782.208), (-0.4409484648665387, -55.90500123232583, 2.617952235213245e-07), (1.0, 1.0, 1.0), "Deep_WoodenBeam_A11", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1335.3525, 3638.8809, 781.2798), (0.0, 40.059551609911296, -0.0), (1.0, 1.0, 1.0), "Deep_WoodenBeam_A12", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1410.2783, 3046.2393, 776.66406), (0.0, 31.285531674165593, -0.0), (1.0, 1.0, 1.0), "Deep_WoodenBeam_A13", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1217.3774, 2385.745, 782.208), (-0.4409484824678575, -75.90496691603114, 3.7310264709937197e-08), (1.0, 1.0, 1.0), "Deep_WoodenBeam_A14", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1173.6157, 1812.9666, 781.2798), (0.0, 20.059550890205497, -0.0), (1.0, 1.0, 1.0), "Deep_WoodenBeam_A15", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1041.3274, 1230.4397, 776.66406), (0.0, 11.285519632639156, -0.0), (1.0, 1.0, 1.0), "Deep_WoodenBeam_A16", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1487.4355, 4651.2285, 851.14307), (0.0, 133.59292150698903, -0.0), (1.0, 1.0, 1.0), "Deep_WoodenBeam_A2", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2090.5469, 4749.839, 851.14307), (0.0, 124.82387941000783, -0.0), (1.0, 1.0, 1.0), "Deep_WoodenBeam_A3_151", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2708.121, 4733.913, 853.65186), (0.0, 112.52941027670616, -0.0), (1.0, 1.0, 1.0), "Deep_WoodenBeam_A4_174", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3298.122, 4863.913, 853.65186), (0.0, 127.52944301708553, -0.0), (1.0, 1.0, 1.0), "Deep_WoodenBeam_A5_212", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (945.667, 5858.147, 806.0542), (-0.44094847682394117, 26.740362080765433, 2.2321748601484277e-07), (1.0, 1.0, 1.0), "Deep_WoodenBeam_A6", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1514.1289, 5940.8457, 805.126), (0.0, 122.70474669130627, -0.0), (1.0, 1.0, 1.0), "Deep_WoodenBeam_A7_258", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3008.541, 5913.92, 804.0337), (16.73892719979173, -120.27752166966438, -30.408869476393203), (1.0, 1.0, 1.0), "Deep_WoodenBeam_A8", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3197.255, 5943.699, 791.645), (22.685118593398307, -90.81610142171091, -31.54546626902026), (1.0, 1.0, 1.0), "Deep_WoodenBeam_A9", _folder)
if a: placed += 1
else: skipped += 1

# Batch 8: StaticMesh'Deep_WoodenBeam_C' (37 instances)
_mesh_path = "/Game/Art/Assets/Kits/Architecture/Deep/Deep_WoodenBeam_C"
_materials = ['/Game/Art/Assets/Kits/Architecture/Deep/Materials/Deep_WoodTrim/MI_Deep_WoodTrim']
_folder = "Reconstruction/BD_BB_Chapter5_BalrogsNest/Meshes"
a = spawn_static_mesh(_mesh_path, _materials, (2119.4062, 4758.3164, 1035.9863), (1.597162905750573e-05, -91.80875027932537, 89.99996412344439), (1.0, 1.0, 1.0), "Deep_WoodenBeam_B10", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2120.8516, 4757.994, 1627.3706), (1.597162905750573e-05, -91.80875027932537, 89.99996412344439), (1.0, 1.0, 1.0), "Deep_WoodenBeam_B11", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2705.1025, 4728.8857, 1046.1553), (6.041930200026822, -0.6878968971128324, 126.78830729094805), (1.0, 1.0, 1.0), "Deep_WoodenBeam_B12", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2078.4502, 4738.407, 1192.3369), (-0.09085057576755277, -90.72338988077892, 94.78739266009711), (1.0, 1.0, 1.0604596), "Deep_WoodenBeam_B13_183", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2723.1494, 4735.1123, 1035.9863), (1.279208308259823e-05, -76.80862143621262, 89.99996785043238), (1.0, 1.0, 1.0), "Deep_WoodenBeam_B14", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2724.6309, 4735.176, 1627.3706), (1.279208308259823e-05, -76.80862143621262, 89.99996785043238), (1.0, 1.0, 1.0), "Deep_WoodenBeam_B15", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3300.6133, 4858.8193, 1035.9863), (4.872402470763833e-05, -126.47355789370947, 89.99994923080331), (1.0, 1.0, 1.0), "Deep_WoodenBeam_B16", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3302.0488, 4858.4463, 1627.3706), (5.271726884364592e-05, -129.2278734157659, 89.99994989225452), (1.0, 1.0, 1.0), "Deep_WoodenBeam_B17", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3302.0488, 4858.4463, 1627.3706), (-5.054746748464531, 167.22423860842673, 150.41404211628372), (1.0, 1.0, 1.0), "Deep_WoodenBeam_B18", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3302.125, 4876.2783, 1044.852), (8.465998664519693, 15.365172595861091, 127.6811959979979), (1.0, 1.0, 1.0), "Deep_WoodenBeam_B19", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (925.5498, 5855.3687, 1283.1328), (1.5054765152537252e-05, -81.63961139309787, 90.00001939315011), (1.0, 1.0, 1.059662), "Deep_WoodenBeam_B20", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (930.35547, 5860.868, 987.45996), (4.248771154162069e-05, -81.6338885930944, -124.81958266944332), (1.0, 1.0, 1.0), "Deep_WoodenBeam_B21", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1522.3428, 5949.2935, 982.84375), (2.6192880798977356e-05, -90.40752212044387, 89.99994991734913), (1.0, 1.0, 1.0), "Deep_WoodenBeam_B22", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1523.7988, 5949.0073, 1574.2275), (2.6192880798977356e-05, -90.40752212044387, 89.99994991734913), (1.0, 1.0, 1.0), "Deep_WoodenBeam_B23", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2115.9707, 5943.415, 982.84375), (4.1074779932538624e-05, 4.892730812841177, 89.99997007572566), (1.0, 1.0, 1.0), "Deep_WoodenBeam_B24", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2115.9707, 5943.415, 1579.8398), (4.1074779932538624e-05, 4.892730812841177, 89.99997007572566), (1.0, 1.0, 1.0), "Deep_WoodenBeam_B25", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2132.0234, 5949.293, 982.84375), (0.23525694671911862, -101.7018565262108, 125.26847074677157), (1.0, 1.0, 1.0), "Deep_WoodenBeam_B26", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1175.2422, 4211.677, 1259.2866), (6.1639216437319e-05, -164.28562071596073, 90.00001142366435), (1.0, 1.0, 1.059662), "Deep_WoodenBeam_B27", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1181.3105, 4207.616, 963.61426), (8.222519701446432e-05, -164.2789633815447, -124.81957795496538), (1.0, 1.0, 1.0), "Deep_WoodenBeam_B28", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1344.7891, 3631.816, 958.99805), (4.7461083552078306e-05, -173.0531090617696, 89.99994346539921), (1.0, 1.0, 1.0), "Deep_WoodenBeam_B29", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (930.35547, 5860.868, 987.45996), (1.2319161423082224e-05, -81.63400735956574, 89.99996365333057), (1.0, 1.0, 1.0), "Deep_WoodenBeam_B3_257", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1344.6875, 3630.333, 1550.3813), (4.7461083552078306e-05, -173.0531090617696, 89.99994346539921), (1.0, 1.0, 1.0), "Deep_WoodenBeam_B30", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1414.9404, 3042.3193, 958.99805), (4.075749285777824e-05, -77.75222820991517, 89.999833982784), (1.0, 1.0, 1.0), "Deep_WoodenBeam_B31", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1414.9404, 3042.3193, 1555.9941), (4.075749285777824e-05, -77.75222820991517, 89.999833982784), (1.0, 1.0, 1.0), "Deep_WoodenBeam_B32", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1223.3826, 2400.0889, 963.61426), (5.472927034903603e-05, 175.7208285756492, 89.99991473423735), (1.0, 1.0, 1.0), "Deep_WoodenBeam_B33", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1223.0015, 2398.6562, 1554.998), (5.472927034903603e-05, 175.7208285756492, 89.99991473423735), (1.0, 1.0, 1.0), "Deep_WoodenBeam_B34", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1219.069, 2405.98, 1259.2866), (6.155678109324846e-05, 175.71438799718888, 90.00000927257842), (1.0, 1.0, 1.059662), "Deep_WoodenBeam_B35", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1223.3826, 2400.0889, 963.61426), (8.215063634331119e-05, 175.72104509367264, -124.81956651574362), (1.0, 1.0, 1.0), "Deep_WoodenBeam_B36", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1180.0667, 1803.1006, 958.99805), (4.8598801183326996e-05, 166.94685726521806, 89.99997335739582), (1.0, 1.0, 1.0), "Deep_WoodenBeam_B37", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1179.4641, 1801.742, 1550.3813), (4.8598801183326996e-05, 166.94685726521806, 89.99997335739582), (1.0, 1.0, 1.0), "Deep_WoodenBeam_B38", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1044.3676, 1225.1614, 1555.9941), (4.196976694554737e-05, -97.7522146476598, 89.99982367262949), (1.0, 1.0, 1.0), "Deep_WoodenBeam_B39", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (931.8369, 5860.8066, 1578.8438), (1.2319161423082224e-05, -81.63400735956574, 89.99996365333057), (1.0, 1.0, 1.0), "Deep_WoodenBeam_B4_264", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1510.1309, 4648.325, 1033.4775), (1.4358860815552175e-05, -79.51498268227658, 89.99994659776618), (1.0, 1.0, 1.0), "Deep_WoodenBeam_B5", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1511.6133, 4648.3193, 1624.8613), (1.4358860815552175e-05, -79.51498268227658, 89.99994659776618), (1.0, 1.0, 1.0), "Deep_WoodenBeam_B6", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1181.3105, 4207.616, 963.61426), (5.547404218921473e-05, -164.27919870479624, 89.99995513342282), (1.0, 1.0, 1.0), "Deep_WoodenBeam_B7_98", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1458.127, 4644.949, 1033.4775), (4.0563706772187994e-05, -70.74610888175069, -124.81955540316925), (1.0, 1.0, 1.0), "Deep_WoodenBeam_B8", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1181.4424, 4206.1396, 1554.998), (5.547404218921473e-05, -164.27919870479624, 89.99995513342282), (1.0, 1.0, 1.0), "Deep_WoodenBeam_B9_99", _folder)
if a: placed += 1
else: skipped += 1

# Batch 9: StaticMesh'Deep_WoodenPlank_A' (4 instances)
_mesh_path = "/Game/Art/Assets/Kits/Architecture/Deep/Deep_WoodenPlank_A"
_materials = ['/Game/Art/Assets/Kits/Architecture/Deep/Materials/Deep_WoodTrim/MI_Deep_WoodTrim']
_folder = "Reconstruction/BD_BB_Chapter5_BalrogsNest/Meshes"
a = spawn_static_mesh(_mesh_path, _materials, (1388.3955, 5268.7812, 792.05176), (-0.6972043558948795, -90.04931491349011, 4.028853264296638), (1.0, 1.0, 1.0), "Deep_WoodenPlank_A_5", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1768.7412, 5379.3564, 796.02344), (-0.6959534572106796, -90.06420728232656, 5.26032918756984), (1.0, 1.0, 1.0), "Deep_WoodenPlank_A2", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2188.947, 5165.185, 799.61), (0.5412309062776556, -168.87897056479156, -170.2287852813027), (1.0, 1.0, 1.0), "Deep_WoodenPlank_A3_17", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2122.8945, 5650.5107, 804.0718), (-0.617736704589138, -176.66336236301007, 175.29840323436576), (1.0, 1.0, 1.0), "Deep_WoodenPlank_A5", _folder)
if a: placed += 1
else: skipped += 1

# Batch 10: StaticMesh'Deep_WoodenPlank_B' (6 instances)
_mesh_path = "/Game/Art/Assets/Kits/Architecture/Deep/Deep_WoodenPlank_B"
_materials = ['/Game/Art/Assets/Kits/Architecture/Deep/Materials/Deep_WoodTrim/MI_Deep_WoodTrim']
_folder = "Reconstruction/BD_BB_Chapter5_BalrogsNest/Meshes"
a = spawn_static_mesh(_mesh_path, _materials, (1573.0156, 5336.9053, 794.1167), (-0.39614862725480826, -66.24703838039548, 6.950866953145615), (1.0, 1.0, 1.0), "Deep_WoodenPlank_B_2", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1987.0844, 5384.118, 792.0707), (0.2079929986853099, -93.08435539124429, 3.855908052633579), (1.0, 1.0, 1.0), "Deep_WoodenPlank_B3", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2084.8027, 5384.119, 793.5752), (-0.3034057482216407, -86.85046162063975, -174.8113466358991), (1.0, 1.0, 1.0), "Deep_WoodenPlank_B4", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2212.7383, 5384.118, 793.5752), (0.1897084410103761, -87.59913105534312, 3.1255199322949747), (1.0, 1.0, 1.0), "Deep_WoodenPlank_B5", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2348.4434, 5416.7627, 798.8037), (1.2908988673288497, 86.38061734569678, -179.56917123818323), (1.0, 1.0, 1.0), "Deep_WoodenPlank_B6", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1033.1367, 5262.8105, 793.86816), (-0.468536340391257, -71.02751271098793, -176.3265313792366), (1.0, 1.0, 1.0), "Deep_WoodenPlank_B7", _folder)
if a: placed += 1
else: skipped += 1

# Batch 11: StaticMesh'NonD_Stairs_Trim_A_L' (1 instances)
_mesh_path = "/Game/Art/Assets/Kits/Architecture/Non_D/NonD_Stairs_Trim_A_L"
_materials = ['/Game/Art/Assets/Kits/Architecture/Suburbs/Materials/Suburbs_Trim_Sheet_A/MI_Suburbs_Trim_Sheet_A', '/Game/Environments/Materials/MI_Suburbs_Non_Destructible']
_folder = "Reconstruction/BD_BB_Chapter5_BalrogsNest/Meshes"
a = spawn_static_mesh(_mesh_path, _materials, (7300.309, 6685.984, 801.07764), (0.0, -130.00002191720526, 0.0), (1.0, 1.0, 1.0), "NonD_Stairs_Trim_A_L_140", _folder)
if a: placed += 1
else: skipped += 1

# Batch 12: StaticMesh'City_Column_Large_A_Base' (3 instances)
_mesh_path = "/Game/Art/Assets/Kits/Architecture/Suburbs/City_Column_Large_A_Base"
_materials = ['/Game/Art/Assets/Kits/Architecture/Suburbs/Materials/SM_AR_City_Column_C/MI_SM_AR_City_Column_C_Base']
_folder = "Reconstruction/BD_BB_Chapter5_BalrogsNest/Meshes"
a = spawn_static_mesh(_mesh_path, _materials, (4510.9395, 5047.309, 990.26807), (0.0, 56.18847560360793, -0.0), (1.25, 1.25, 1.25), "SM_AR_City_Column_C_Base4", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (6235.8823, 5101.642, 990.26807), (0.0, 56.18847560360793, -0.0), (1.25, 1.25, 1.25), "SM_AR_City_Column_C_Base5", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4490.591, 6525.1016, 982.8545), (0.0, -89.77532864090233, 0.0), (1.25, 1.25, 1.25), "SM_AR_City_Column_C_Base6", _folder)
if a: placed += 1
else: skipped += 1

# Batch 13: StaticMesh'City_Column_Large_A_Capital' (3 instances)
_mesh_path = "/Game/Art/Assets/Kits/Architecture/Suburbs/City_Column_Large_A_Capital"
_materials = ['/Game/Art/Assets/Kits/Architecture/Suburbs/Materials/SM_AR_City_Column_C/MI_SM_AR_City_Column_C_Capital']
_folder = "Reconstruction/BD_BB_Chapter5_BalrogsNest/Meshes"
a = spawn_static_mesh(_mesh_path, _materials, (4503.3203, 5053.13, 1987.1396), (0.0, 56.18847560360793, -0.0), (1.25, 1.25, 1.25), "SM_AR_City_Column_C_Capital4", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (6228.263, 5107.466, 1997.0234), (0.0, 56.18847560360793, -0.0), (1.25, 1.25, 1.25), "SM_AR_City_Column_C_Capital5", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4500.165, 6524.5405, 1989.6099), (0.0, -89.77532864090233, 0.0), (1.25, 1.25, 1.25), "SM_AR_City_Column_C_Capital6", _folder)
if a: placed += 1
else: skipped += 1

# Batch 14: StaticMesh'City_Column_Large_A_Shaft' (9 instances)
_mesh_path = "/Game/Art/Assets/Kits/Architecture/Suburbs/City_Column_Large_A_Shaft"
_materials = ['/Game/Art/Assets/Kits/Architecture/Suburbs/Materials/SM_AR_City_Column_C/MI_SM_AR_City_Column_C_Shaft']
_folder = "Reconstruction/BD_BB_Chapter5_BalrogsNest/Meshes"
a = spawn_static_mesh(_mesh_path, _materials, (4511.0645, 5049.0537, 1240.5703), (0.0, 56.18847560360793, -0.0), (1.25, 1.25, 1.25), "SM_AR_City_Column_C_Shaft11", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4511.0645, 5049.056, 1490.6919), (0.0, 56.18847560360793, -0.0), (1.25, 1.25, 1.25), "SM_AR_City_Column_C_Shaft12", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4511.0645, 5049.0513, 1740.0615), (0.0, 56.18847560360793, -0.0), (1.25, 1.25, 1.25), "SM_AR_City_Column_C_Shaft13", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (6236.0083, 5103.3877, 1245.4062), (0.0, 56.18847560360793, -0.0), (1.25, 1.25, 1.25), "SM_AR_City_Column_C_Shaft14", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (6236.0083, 5103.3877, 1496.7632), (0.0, 56.18847560360793, -0.0), (1.25, 1.25, 1.25), "SM_AR_City_Column_C_Shaft15", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (6236.008, 5103.3877, 1749.9458), (0.0, 56.18847560360793, -0.0), (1.25, 1.25, 1.25), "SM_AR_City_Column_C_Shaft16", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4491.464, 6523.5864, 1232.7637), (0.0, -89.77532864090233, 0.0), (1.25, 1.25, 1.25), "SM_AR_City_Column_C_Shaft17", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4491.464, 6523.585, 1482.1509), (0.0, -89.77532864090233, 0.0), (1.25, 1.25, 1.25), "SM_AR_City_Column_C_Shaft18", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4491.464, 6523.586, 1729.3218), (0.0, -89.77532864090233, 0.0), (1.25, 1.25, 1.25), "SM_AR_City_Column_C_Shaft19", _folder)
if a: placed += 1
else: skipped += 1

# Batch 15: StaticMesh'Suburbs_Column_X_Large_A_Shaft' (16 instances)
_mesh_path = "/Game/Art/Assets/Kits/Architecture/Suburbs/Suburbs_Column_X_Large_A_Shaft"
_materials = ['/Game/Art/Assets/Kits/Architecture/Suburbs/Materials/Suburbs_Column_X_Large_A/MI_Suburbs_Column_X_Large_A_Shaft']
_folder = "Reconstruction/BD_BB_Chapter5_BalrogsNest/Meshes"
a = spawn_static_mesh(_mesh_path, _materials, (6579.4634, 4900.006, 2886.9976), (90.0, -4.869354268407488, -184.86907173245342), (1.0, 1.0, 1.0), "Suburbs_Column_X_Large_A_Shaft11", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4394.0254, 4900.006, 2426.8442), (90.0, -2.4391213347211425, -182.43886898428104), (1.0, 1.0, 1.0), "Suburbs_Column_X_Large_A_Shaft16", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (6179.464, 4900.0063, 2990.4814), (90.0, -5.2434727931303, -185.24325787264593), (1.0, 1.0, 1.0), "Suburbs_Column_X_Large_A_Shaft18", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (6579.4634, 4900.006, 2990.4814), (90.0, -5.2434727931303, -185.24325787264593), (1.0, 1.0, 1.0), "Suburbs_Column_X_Large_A_Shaft19", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (6877.447, 4899.992, 2886.9976), (90.0, -2.4391213347211425, -182.43886898428104), (1.0, 1.0, 1.0), "Suburbs_Column_X_Large_A_Shaft24", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (9296.914, 4899.995, 2886.9976), (90.0, -5.2434727931303, -185.24325787264593), (1.0, 1.0, 1.0), "Suburbs_Column_X_Large_A_Shaft26", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (8077.448, 4899.9907, 2990.4814), (90.0, -5.2434727931303, -185.24325787264593), (1.0, 1.0, 1.0), "Suburbs_Column_X_Large_A_Shaft30", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (6877.4463, 4899.992, 2990.4814), (90.0, -2.4391213347211425, -182.43886898428104), (1.0, 1.0, 1.0), "Suburbs_Column_X_Large_A_Shaft31", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (8896.914, 4899.996, 2990.4814), (90.0, -2.4391213347211425, -182.43886898428104), (1.0, 1.0, 1.0), "Suburbs_Column_X_Large_A_Shaft32", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (9296.914, 4899.995, 2990.4814), (90.0, -4.869354268407488, -184.86907173245342), (1.0, 1.0, 1.0), "Suburbs_Column_X_Large_A_Shaft33", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (9696.914, 4899.995, 2990.4814), (90.0, -4.869354268407488, -184.86907173245342), (1.0, 1.0, 1.0), "Suburbs_Column_X_Large_A_Shaft34", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (8496.913, 4899.9966, 2990.4814), (90.0, -2.4391213347211425, -182.43886898428104), (1.0, 1.0, 1.0), "Suburbs_Column_X_Large_A_Shaft35", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4159.998, 4550.0024, 2810.0), (90.0, -2.4391213347211425, -182.43886898428104), (1.0, 1.0, 1.0), "Suburbs_Column_X_Large_A_Shaft4", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4559.997, 4550.0015, 2810.0), (90.0, -4.869354268407488, -184.86907173245342), (1.0, 1.0, 1.0), "Suburbs_Column_X_Large_A_Shaft5", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4959.9976, 4550.0015, 2810.0), (90.0, -4.869354268407488, -184.86907173245342), (1.0, 1.0, 1.0), "Suburbs_Column_X_Large_A_Shaft6", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3759.997, 4550.003, 2810.0), (90.0, -2.4391213347211425, -182.43886898428104), (1.0, 1.0, 1.0), "Suburbs_Column_X_Large_A_Shaft8", _folder)
if a: placed += 1
else: skipped += 1

# Batch 16: StaticMesh'Suburbs_Stairs_Medium_C_NonDest' (8 instances)
_mesh_path = "/Game/Art/Assets/Kits/Architecture/Suburbs/Suburbs_Stairs_Medium_C_NonDest"
_materials = ['/Game/Art/Assets/Kits/Architecture/Suburbs/Materials/Stairs_Medium_C_NonDest/MI_Stairs_Medium_C_NonDes', '/Game/Art/Assets/Kits/Architecture/Suburbs/Destructable/Materials/MI_Suburbs_Wall_Non_Dest']
_folder = "Reconstruction/BD_BB_Chapter5_BalrogsNest/Meshes"
a = spawn_static_mesh(_mesh_path, _materials, (7559.971, 5117.141, 876.30225), (0.0, 60.938025620897484, -0.0), (1.0707517, 1.0, 1.0), "Suburbs_Stairs_Medium_C_NonDest_119", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (10349.601, 8172.741, 798.26807), (0.0, 69.47646843762841, -0.0), (1.0, 1.0, 1.0), "Suburbs_Stairs_Medium_C_NonDest2_140", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (7710.32, 7213.377, 810.78955), (0.0, -45.167657618708034, 0.0), (1.0767881, 1.0, 1.0), "Suburbs_Stairs_Medium_C_NonDest3_144", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (7169.707, 6781.3564, 803.60693), (0.0, 140.51968079507657, -0.0), (1.0, 1.0, 1.0), "Suburbs_Stairs_Medium_C_NonDest4_153", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5008.213, 5249.7666, 710.6953), (0.0, 4.9368136160979486, -0.0), (1.0, 1.0, 1.0), "Suburbs_Stairs_Medium_C_NonDest5", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5307.4346, 5275.6147, 710.6953), (0.0, 4.9368136160979486, -0.0), (1.0, 1.0, 1.0), "Suburbs_Stairs_Medium_C_NonDest6", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5076.9033, 4908.785, 865.78467), (0.0, 4.9368136160979486, -0.0), (1.0, 1.0, 1.0), "Suburbs_Stairs_Medium_C_NonDest7", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5374.3647, 4934.4663, 865.78467), (0.0, 4.9368136160979486, -0.0), (1.0, 1.0, 1.0), "Suburbs_Stairs_Medium_C_NonDest8", _folder)
if a: placed += 1
else: skipped += 1

# Batch 17: StaticMesh'Suburbs_Stairs_Small_A_NonDest' (1 instances)
_mesh_path = "/Game/Art/Assets/Kits/Architecture/Suburbs/Suburbs_Stairs_Small_A_NonDest"
_materials = ['/Game/Art/Assets/Kits/Architecture/Suburbs/Destructable/Materials/MI_Suburbs_Wall_Non_Dest', '/Game/Art/Assets/Kits/Architecture/Suburbs/Materials/Stairs_Medium_C_NonDest/MI_Stairs_Medium_C_NonDes']
_folder = "Reconstruction/BD_BB_Chapter5_BalrogsNest/Meshes"
a = spawn_static_mesh(_mesh_path, _materials, (7184.165, 5434.6577, 804.47363), (0.0, 43.590115866674196, -0.0), (1.2215263, 1.0, 1.0), "Suburbs_Stairs_Small_A_NonDest4", _folder)
if a: placed += 1
else: skipped += 1

# Batch 18: StaticMesh'Suburbs_Stairs_Small_C_NonDest' (1 instances)
_mesh_path = "/Game/Art/Assets/Kits/Architecture/Suburbs/Suburbs_Stairs_Small_C_NonDest"
_materials = ['/Game/Art/Assets/Kits/Architecture/Suburbs/Destructable/Materials/MI_Suburbs_Wall_Non_Dest', '/Game/Art/Assets/Kits/Architecture/Suburbs/Materials/Stairs_Medium_C_NonDest/MI_Stairs_Medium_C_NonDes']
_folder = "Reconstruction/BD_BB_Chapter5_BalrogsNest/Meshes"
a = spawn_static_mesh(_mesh_path, _materials, (10022.77, 5405.05, 903.0752), (0.0, 122.29258791515088, -0.0), (1.0, 1.0, 1.0), "Suburbs_Stairs_Small_C_NonDest_80", _folder)
if a: placed += 1
else: skipped += 1

# Batch 19: StaticMesh'Dirt_Mound_D' (2 instances)
_mesh_path = "/Game/Art/Assets/Kits/Misc/Dirt_Mounds/Dirt_Mound_D"
_materials = ['/Game/Art/Assets/Kits/Misc/Dirt_Mounds/Materials/MI_DirtMound_Mines']
_folder = "Reconstruction/BD_BB_Chapter5_BalrogsNest/Meshes"
a = spawn_static_mesh(_mesh_path, _materials, (3644.6045, 5862.7275, 771.4375), (0.0, -81.5935660117578, 0.0), (1.0, 1.0, 0.62687725), "Dirt_Mound_D_121", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (8822.072, 9090.863, 897.9922), (-1.3297152945192225e-07, -90.00018017168242, -3.4188840988357785), (1.0, 1.0, 0.41744766), "Dirt_Mound_D2_360", _folder)
if a: placed += 1
else: skipped += 1

# Batch 20: StaticMesh'Dirt_Mound_E' (8 instances)
_mesh_path = "/Game/Art/Assets/Kits/Misc/Dirt_Mounds/Dirt_Mound_E"
_materials = ['/Game/Art/Assets/Kits/Misc/Dirt_Mounds/Materials/MI_DirtMound_Mines']
_folder = "Reconstruction/BD_BB_Chapter5_BalrogsNest/Meshes"
a = spawn_static_mesh(_mesh_path, _materials, (2105.5127, 5680.821, 796.8511), (-0.032745398007764596, -81.56535703169763, 0.6312837534652033), (1.0, 1.0, 0.20834938), "Dirt_Mound_E_33", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2115.8613, 5161.2344, 795.56396), (0.6937765250044977, 113.56953014287349, 0.05875492800251179), (1.0, 1.0, 0.24112609), "Dirt_Mound_E2", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5410.7095, 5367.944, 796.33984), (0.0, -90.0001164887758, 0.0), (1.0, 1.0, 0.68475467), "Dirt_Mound_E3_225", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (6108.589, 5509.1987, 792.8872), (0.0, -75.09839156518107, 0.0), (1.0, 1.0, 0.684755), "Dirt_Mound_E4", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (10257.647, 9443.211, 794.7378), (-0.1479491981339714, -46.17327541721521, 0.37514154078543743), (1.0, 1.0, 0.208349), "Dirt_Mound_E5", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (10439.781, 8980.595, 793.0669), (0.6368758282888881, 132.55313276102598, 0.28124720847478124), (1.0, 1.0, 0.241126), "Dirt_Mound_E6", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2133.633, 5305.919, 797.16046), (0.693776503927501, 113.56890405824177, 0.36994478185733276), (1.4880061, 1.0, 0.12343563), "Dirt_Mound_E7", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1993.2648, 5627.6763, 801.4113), (0.6937760702152188, 113.5689040560067, 0.36994495623751283), (1.488006, 1.0, 0.123436), "Dirt_Mound_E8", _folder)
if a: placed += 1
else: skipped += 1

# Batch 21: StaticMesh'Dirt_Mound_F' (3 instances)
_mesh_path = "/Game/Art/Assets/Kits/Misc/Dirt_Mounds/Dirt_Mound_F"
_materials = ['/Game/Art/Assets/Kits/Misc/Dirt_Mounds/Materials/MI_DirtMound_Mines']
_folder = "Reconstruction/BD_BB_Chapter5_BalrogsNest/Meshes"
a = spawn_static_mesh(_mesh_path, _materials, (2052.0186, 5068.991, 779.8496), (0.0, -84.13034160184014, 0.0), (1.0, 1.0, 0.7201578), "Dirt_Mound_F_29", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5473.8833, 5571.266, 800.0), (0.0, 20.000006467296362, -0.0), (0.6000847, 0.6000847, 0.6000847), "Dirt_Mound_F3_6", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (6024.0703, 6209.8486, 800.0), (0.0, -35.00006033507422, 0.0), (0.5972083, 0.5972083, 0.5972083), "Dirt_Mound_F4_18", _folder)
if a: placed += 1
else: skipped += 1

# Batch 22: StaticMesh'Dirt_Mound_G' (1 instances)
_mesh_path = "/Game/Art/Assets/Kits/Misc/Dirt_Mounds/Dirt_Mound_G"
_materials = ['/Game/Art/Assets/Kits/Misc/Dirt_Mounds/Materials/MI_DirtMound_Mines']
_folder = "Reconstruction/BD_BB_Chapter5_BalrogsNest/Meshes"
a = spawn_static_mesh(_mesh_path, _materials, (9514.787, 9330.465, 903.417), (4.985026374537929, -18.743466803768243, 1.667140696575311), (1.0, 1.0, 1.3272343), "Dirt_Mound_G_400", _folder)
if a: placed += 1
else: skipped += 1

# Batch 23: StaticMesh'Dirt_Mound_H' (20 instances)
_mesh_path = "/Game/Art/Assets/Kits/Misc/Dirt_Mounds/Dirt_Mound_H"
_materials = ['/Game/Art/Assets/Kits/Misc/Dirt_Mounds/Materials/MI_DirtMound_Mines']
_folder = "Reconstruction/BD_BB_Chapter5_BalrogsNest/Meshes"
a = spawn_static_mesh(_mesh_path, _materials, (2925.878, 5839.3184, 800.0), (0.0, 145.10583179114903, -0.0), (1.0, 1.0, 1.0), "Dirt_Mound_H_118", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2611.796, 5271.005, 798.2324), (0.0, -90.0001164887758, 0.0), (1.0, 1.0, 0.17566401), "Dirt_Mound_H10_217", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (10378.027, 7458.625, 983.1836), (2.0877532407974086e-09, -2.5934444321963235, 1.4748808107574125), (1.0, 1.0, 1.0), "Dirt_Mound_H11_420", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (797.2282, 1885.9763, 762.2031), (3.4969798537219297, -155.25657170781366, -5.576078815328671), (1.726425, 1.726425, 2.012741), "Dirt_Mound_H12_89", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (7293.632, 5065.4727, 910.4746), (26.10039581981561, -34.14679248455286, 10.88323708337441), (1.0, 1.0, 1.340464), "Dirt_Mound_H13", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (7118.3994, 4966.2085, 938.0718), (0.8096436381119088, 10.408355135093421, 3.154420742077166), (1.0, 1.0, 1.0), "Dirt_Mound_H14", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (7337.806, 4822.1157, 1084.033), (-8.377747683751975, -32.710542230099264, 0.6080034098981274), (1.0, 1.0, 1.0), "Dirt_Mound_H15", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (10625.547, 8026.3135, 986.5923), (-2.8095706797982962, -110.43529211568662, 1.8396946205219382e-06), (1.3579024, 1.3579024, 1.3579024), "Dirt_Mound_H16_426", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5530.0, 5695.0, 800.0), (0.0, 0.0, -0.0), (0.38072824, 0.38072824, 0.38072824), "Dirt_Mound_H17_9", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (6093.579, 6372.4434, 800.0), (0.0, 85.00009211210833, -0.0), (0.96441406, 0.96441406, 0.96441406), "Dirt_Mound_H18_15", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (985.2628, 1841.8226, 794.7206), (0.07151890490632688, -164.83826378653274, -4.497650050445912), (2.872078, 2.872078, 2.4327586), "Dirt_Mound_H19", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2783.2578, 5057.159, 783.9702), (0.0, -47.852111107867586, 0.0), (1.0, 1.0, 1.0), "Dirt_Mound_H2", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1148.0868, 2690.2502, 764.87714), (2.3606770478638475, -50.57741594873837, 2.195744863610349), (2.872078, 2.872078, 2.432759), "Dirt_Mound_H20", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3743.2393, 4717.1387, 889.5366), (0.0, 0.374145531116847, -0.0), (0.9327898, 1.0, 1.4412622), "Dirt_Mound_H3_145", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3613.5986, 4820.5776, 894.20557), (0.0, -111.42115608133072, 0.0), (1.0, 1.1608844, 1.7430044), "Dirt_Mound_H4_150", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3456.1406, 4644.5728, 905.41943), (0.22506835885485507, 4.710083088868757, 7.186694811094896), (1.9885299, 1.9885299, 1.9270207), "Dirt_Mound_H5_159", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5667.837, 5589.1606, 800.0), (0.0, 75.00003453112258, -0.0), (1.0, 1.0, 1.0), "Dirt_Mound_H6_3", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2718.4346, 4924.8867, 783.1411), (1.338289789654067e-07, -47.852022235048636, 6.378921703114087), (1.8858033, 1.8858033, 2.2222888), "Dirt_Mound_H7", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2596.0803, 5049.891, 776.9075), (3.223951713355666, 147.16697572984137, -5.737854272147812), (1.7264249, 1.7264249, 2.0127406), "Dirt_Mound_H8", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2619.211, 5775.0127, 800.0), (0.0, 174.04625862056827, -0.0), (1.0, 1.0, 0.26721302), "Dirt_Mound_H9_201", _folder)
if a: placed += 1
else: skipped += 1

# Batch 24: StaticMesh'Dirt_Mound_I' (74 instances)
_mesh_path = "/Game/Art/Assets/Kits/Misc/Dirt_Mounds/Dirt_Mound_I"
_materials = ['/Game/Art/Assets/Kits/Misc/Dirt_Mounds/Materials/MI_DirtMound_Mines']
_folder = "Reconstruction/BD_BB_Chapter5_BalrogsNest/Meshes"
a = spawn_static_mesh(_mesh_path, _materials, (3013.9922, 6048.6147, 781.0571), (0.0, 107.50984485509255, -0.0), (1.0, 1.0, 0.93578804), "Dirt_Mound_I_115", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4738.9824, 5334.6416, 791.47705), (2.2359029184733177, -93.0596306188508, 1.572371866263799), (1.0, 1.0, 0.665734), "Dirt_Mound_I11", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5808.165, 4744.7314, 1044.707), (-0.2163696378450903, -12.556855122997963, 0.4162486631552885), (1.0, 1.0, 0.665734), "Dirt_Mound_I12", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5122.7026, 4482.3125, 1056.1348), (-0.17044064673549167, -30.523680581518967, 2.2437844662943904), (1.0, 1.0, 0.7305935), "Dirt_Mound_I13", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4409.6133, 5607.339, 786.3047), (-1.1753235358901242, 137.4536283165982, -2.4678040312100578), (1.0, 1.0, 0.23954597), "Dirt_Mound_I14_206", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (6702.5483, 5047.6987, 911.5713), (2.6092121774656967, -89.76319953589115, 0.814037691308617), (1.0, 1.0, 0.36603165), "Dirt_Mound_I15", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (6333.037, 4962.316, 921.80664), (0.0, -108.17766659355618, 0.0), (1.0, 1.0, 1.2692991), "Dirt_Mound_I16_221", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (6683.071, 5419.1777, 808.96606), (2.437231328750534, -86.50326679703882, 1.2373596431086626), (1.0, 1.0, 0.5617247), "Dirt_Mound_I17_253", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (7303.8994, 5689.2754, 788.81104), (0.45512273230413614, -172.18811502740763, -1.141418202925636), (1.0, 1.0, 0.2570982), "Dirt_Mound_I18", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (7875.4463, 5680.5537, 799.08356), (0.43242602697923466, -34.52603186201123, 2.4853270208825697), (1.0, 1.0, 0.257098), "Dirt_Mound_I19", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3391.2812, 4683.824, 907.8467), (-2.0828152596935457e-07, 111.25357820691083, -3.8191223347835566), (1.0, 1.0, 0.62393045), "Dirt_Mound_I2_142", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (6997.6924, 6713.382, 770.42725), (-3.405181979518551, 126.67450372614051, -3.24136391419368), (1.0, 1.0, 0.45850188), "Dirt_Mound_I20", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (7529.4365, 6611.6943, 774.89014), (3.5015033169132606, -81.21000624279891, 0.09065478140282338), (1.0, 1.0, 0.4300947), "Dirt_Mound_I22_276", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5947.3315, 6571.942, 776.4912), (-2.303405867708249, -126.95286346314153, -2.4205626405737584), (1.0, 1.0, 0.34011436), "Dirt_Mound_I23_300", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (7931.4453, 6736.105, 778.2085), (2.5138441695572715, -34.563598095209805, 1.0522564811344826), (1.0, 1.0, 0.40276313), "Dirt_Mound_I24", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (7475.411, 6524.0786, 791.0241), (-0.25946044945318564, -118.91015857260203, -3.0521084405064414e-05), (1.0, 1.0, 0.20985563), "Dirt_Mound_I26", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (7615.3213, 4540.6074, 1104.1663), (5.304517382272575, -109.49176748919363, 0.9382799069824238), (1.0, 1.0, 0.7507394), "Dirt_Mound_I27_323", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (7956.1846, 4697.519, 1091.5488), (-7.964050043670712, 118.56283861024932, -11.140503782082114), (0.74502957, 0.74502957, 0.538788), "Dirt_Mound_I28", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (8132.291, 5436.506, 777.67487), (0.4324259712468081, -153.7846329214796, 2.485336404590518), (1.0, 1.0, 0.52075297), "Dirt_Mound_I29", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3693.3594, 5074.597, 796.0044), (-2.016784452192865, 111.38823639415737, -3.8215328524909533), (1.0, 1.0, 0.73626506), "Dirt_Mound_I3", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (8532.999, 4620.868, 786.822), (0.432425978542114, -111.76593883610856, 2.485343711512254), (1.0, 1.0, 0.769917), "Dirt_Mound_I30", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (9437.035, 4373.1895, 822.68604), (3.4277024813700856, 11.882688897196685, 2.2787055313491926), (1.0, 1.0, 0.769917), "Dirt_Mound_I32", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (10118.8545, 5913.817, 807.796), (2.615784623336397, -32.86902016887002, -0.9159545226571322), (1.0, 1.0, 0.48372474), "Dirt_Mound_I35", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (10972.738, 5643.217, 1007.25586), (0.08995451311308816, 21.98489438513699, 1.9541568381476146), (1.0, 1.0, 0.70493203), "Dirt_Mound_I36", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (10615.438, 5026.2153, 976.27344), (0.08995396039360684, -31.00549413976224, 1.9541594285697352), (1.0, 1.0, 0.704932), "Dirt_Mound_I37", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (10775.292, 5872.923, 1020.8823), (-0.6501159673854734, -101.85607280041958, -1.568206832054501), (1.0, 1.0, 0.704932), "Dirt_Mound_I38", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (9910.892, 5112.004, 893.0879), (-1.5140687184372623, -150.29852512108278, -0.7680054241058749), (1.0, 1.0, 0.23533644), "Dirt_Mound_I39", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3906.1953, 5174.382, 796.1299), (0.7202230720741202, 157.17986563794327, -9.519134676809937), (1.0, 1.0, 0.4089006), "Dirt_Mound_I4", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (9721.152, 4763.2686, 886.9043), (-1.514068293995469, 167.93506498081874, -0.7680051896064917), (0.7893448, 0.7893448, 0.39749897), "Dirt_Mound_I40", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (9890.527, 7150.3057, 788.7871), (1.6985791047488203, -90.94792170258336, 1.317634867660815), (1.0, 1.0, 0.28792757), "Dirt_Mound_I42", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (9782.878, 7700.3545, 798.1296), (1.6985794336130606, 3.880843984349829, 1.3176365243602475), (1.0, 1.0, 0.287928), "Dirt_Mound_I43", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (8128.1865, 7837.639, 794.01074), (0.5285499155830937, 151.22960287474757, 0.7575977927432491), (1.0, 1.0, 0.257098), "Dirt_Mound_I44", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (8209.591, 8858.823, 757.1751), (-6.9104914494129925, 151.09813708700963, -2.7187193541800636), (1.3718734, 1.3718734, 1.5009933), "Dirt_Mound_I45", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (10147.531, 8399.709, 784.3794), (1.698579414305075, 3.880843993043879, 1.3176370972819855), (1.0, 1.0, 0.287928), "Dirt_Mound_I46_377", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (8901.696, 8905.364, 792.2527), (2.72213232463589, 98.43615331775455, 1.8056431518568123), (1.3677189, 1.3677189, 0.92578167), "Dirt_Mound_I47", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (7858.81, 7396.09, 803.70184), (-0.8009643593521956, -113.74688546178322, 0.4602318503287605), (1.0, 1.0, 0.257098), "Dirt_Mound_I48", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (9741.804, 9632.619, 795.8618), (0.0, 162.94272024950794, -0.0), (1.1488628, 1.1488628, 0.7747557), "Dirt_Mound_I49", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3581.2852, 5872.7124, 788.93164), (-0.2460021953016939, -49.66433324945964, 5.909246136441184e-07), (1.0, 1.0, 0.64795333), "Dirt_Mound_I5_162", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (8005.3594, 7102.0093, 804.10693), (0.5285499489252106, -162.34971149947825, 0.757597293334504), (1.0, 1.0, 0.257098), "Dirt_Mound_I50_403", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (10719.635, 7702.1953, 939.43506), (-4.452728434828245, -3.708954199613129, 2.0612407900602437e-06), (1.0, 1.0, 1.0), "Dirt_Mound_I51_417", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5945.0, 6205.0, 800.0), (0.0, 0.0, -0.0), (0.39803958, 0.39803958, 0.39803958), "Dirt_Mound_I52_12", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (8835.195, 5925.222, 799.0664), (0.0, -90.0001164887758, 0.0), (1.0, 1.0, 0.20847848), "Dirt_Mound_I53_436", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5526.7393, 6934.024, 792.9072), (0.9469579099963775, -64.88781394449532, -0.2409057948600368), (1.0, 1.0, 1.0), "Dirt_Mound_I54", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5193.435, 7223.741, 934.63916), (0.967400491699718, -42.549194463439804, -0.5271911565126889), (1.0, 1.0, 1.0), "Dirt_Mound_I56", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4881.707, 6559.6255, 786.11865), (0.5601904493458193, 4.4057314514878705, 0.8005477441871207), (1.0, 1.0, 0.8909434), "Dirt_Mound_I57", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (7185.141, 7087.765, 978.91046), (-1.2516783028560199, -63.07240533546146, -2.2608641519738764), (0.95623326, 0.95623326, 1.3950202), "Dirt_Mound_I58_104", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (8698.267, 8730.157, 773.26245), (-2.1840211231980806, 117.69800395857595, 2.6093295319352423), (1.02869, 1.02869, 0.705801), "Dirt_Mound_I59", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4267.826, 5258.23, 801.6162), (-1.1753235358901242, 137.4536283165982, -2.4678040312100578), (1.0, 1.0, 0.665734), "Dirt_Mound_I6", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (12308.672, 10375.807, 788.6847), (0.0, 96.92344907580575, -0.0), (1.148863, 1.148863, 0.774756), "Dirt_Mound_I60", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (9388.051, 8967.171, 750.8732), (-2.901550208805225, 136.28883674785465, 1.7772417577489192), (1.5675359, 1.5675359, 0.96672803), "Dirt_Mound_I61", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1373.2207, 4360.9805, 776.85156), (-0.3597106777312006, 24.920155117767422, -0.07733154258285799), (1.4116327, 1.4116327, 1.3612015), "Dirt_Mound_I63", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (867.50586, 5801.6763, 792.00684), (-0.3212280226698573, -71.692115409049, -0.1794738803734222), (1.2433699, 1.2433699, 1.0726037), "Dirt_Mound_I64", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1680.2461, 5997.6465, 788.58887), (-0.32122798200466274, 131.53939987338256, -0.1794738685023282), (1.0, 1.0, 1.0), "Dirt_Mound_I65", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3414.288, 6367.2783, 877.8862), (4.288866516517142, 139.9466194001933, -3.5975338489822444), (1.0, 1.0, 0.935788), "Dirt_Mound_I66", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (9481.762, 6025.297, 797.41016), (0.0, -22.093535799187553, 0.0), (1.0, 1.0, 0.158878), "Dirt_Mound_I67", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (9178.518, 6159.7886, 809.1709), (0.0, -22.093535799187553, 0.0), (1.0, 1.0, 0.099089354), "Dirt_Mound_I68", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (8656.747, 6103.863, 799.0669), (0.31179125052510104, -129.63470002689735, -0.2582397237717426), (1.0, 1.0, 0.208478), "Dirt_Mound_I69", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4195.9893, 6310.879, 764.8833), (-4.083251667724582, 157.00871011165685, -0.5415344699861134), (1.0, 1.0, 0.665734), "Dirt_Mound_I7", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (8546.498, 6552.5737, 799.0669), (0.0, -178.0397761615566, 0.0), (1.0, 1.0, 0.208478), "Dirt_Mound_I70", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (7220.988, 5815.778, 800.0), (0.0, 24.999996910958014, -0.0), (0.483831, 0.483831, 0.483831), "Dirt_Mound_I71_21", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (7266.881, 5119.804, 920.60004), (10.689422514636878, -71.57397279671315, 3.9766995173784214), (0.5796695, 0.5796695, 0.1413945), "Dirt_Mound_I72", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1413.2207, 4535.9805, 776.85156), (-0.27990725400972116, -94.02539075758777, -0.2388000761270143), (1.5226912, 1.5226912, 1.1468586), "Dirt_Mound_I73_102", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (382.50586, 5851.6763, 792.00684), (-0.32122799924913265, -62.63577368260481, -0.1794738902607909), (1.0, 1.0, 1.0), "Dirt_Mound_I74", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (6857.6934, 4630.7485, 921.80664), (0.0, 90.75378365876368, -0.0), (1.0, 1.0, 1.269299), "Dirt_Mound_I75", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (10300.502, 6195.384, 813.1475), (2.615784859544934, -32.86902017395369, -0.9159545326805419), (1.0, 1.0, 0.483725), "Dirt_Mound_I76", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (10460.413, 6242.897, 804.8525), (0.826480197647328, -86.2249841902142, -2.645324869069746), (1.0, 1.0, 0.483725), "Dirt_Mound_I77", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (10417.206, 6897.76, 795.38513), (1.743344076471616, -64.60338805861814, -2.1546322036565346), (1.0, 1.0, 0.483725), "Dirt_Mound_I78", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3649.5088, 6234.172, 782.9331), (-4.083221363342211, 157.0087770047379, 0.5389048802040463), (1.0, 1.0, 0.665734), "Dirt_Mound_I8", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (11965.6045, 8713.285, 794.00464), (0.0, -97.22155382712722, 0.0), (1.0, 1.0, 0.625893), "Dirt_Mound_I80", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (11442.497, 8934.428, 794.00464), (0.0, -54.93482139112397, 0.0), (1.0, 1.0, 0.625893), "Dirt_Mound_I81", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (11968.252, 8829.433, 783.2462), (-1.6460266474949057, -85.88509747839193, -0.11840809227478637), (1.0, 1.0, 0.81269217), "Dirt_Mound_I82", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (11552.775, 10352.244, 788.68616), (0.0, 96.92344907580575, -0.0), (1.148863, 1.148863, 0.774756), "Dirt_Mound_I83", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (12308.672, 8726.593, 788.6847), (0.0, -103.0197168270904, 0.0), (1.148863, 1.148863, 0.774756), "Dirt_Mound_I84", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2348.755, 6050.584, 793.084), (0.788121742586143, 104.49102034430828, 0.9766249867948905), (1.0, 1.0, 1.0363033), "Dirt_Mound_I9", _folder)
if a: placed += 1
else: skipped += 1

# Batch 25: StaticMesh'Suburbs_Dirt_Mound_B' (9 instances)
_mesh_path = "/Game/Art/Assets/Kits/Misc/Dirt_Mounds/Suburbs_Dirt_Mound_B"
_materials = ['/Game/Art/Assets/Kits/Misc/Dirt_Mounds/Materials/MI_DirtMound_Mines']
_folder = "Reconstruction/BD_BB_Chapter5_BalrogsNest/Meshes"
a = spawn_static_mesh(_mesh_path, _materials, (8735.599, 8446.402, 757.70734), (-9.316717823659036e-09, 13.819304752072524, 3.936691151654534), (8.374236, 8.374236, 8.374236), "Suburbs_Dirt_Mound_B_26", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (8936.264, 8552.31, 753.93005), (4.790140777997558, -62.031153885202095, 4.7602455196002476), (8.374236, 8.374236, 8.374236), "Suburbs_Dirt_Mound_B2", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (9448.28, 8769.494, 762.49365), (3.051837781975118, 14.833908137967686, 3.9428645419212796), (8.374236, 8.374236, 8.374236), "Suburbs_Dirt_Mound_B3", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (8304.687, 7755.459, 761.93317), (3.0518378995371958, 14.833908110607995, 3.9428636306022335), (8.374236, 8.374236, 6.3852744), "Suburbs_Dirt_Mound_B4", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (10106.22, 6850.836, 758.0347), (3.131163610606743, -40.380067398338, 3.4602178480326633), (8.374236, 8.374236, 8.374236), "Suburbs_Dirt_Mound_B5", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (8478.307, 5215.874, 760.80676), (-2.3506164396496514, 76.25330581452151, 1.8274045790460771), (8.374236, 8.374236, 8.374236), "Suburbs_Dirt_Mound_B6", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (6694.3345, 6523.381, 785.28955), (2.342859578471894, 14.70657335092313, -0.37512212051656124), (8.374236, 8.374236, 4.942413), "Suburbs_Dirt_Mound_B7", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5879.953, 6441.906, 776.4995), (-1.8896790137005028, -78.6581342015524, -0.6182861018499407), (8.374236, 8.374236, 4.942413), "Suburbs_Dirt_Mound_B8", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5148.756, 6295.513, 768.4559), (1.1551001706057888, -78.56445155500198, 1.7335400546216606), (8.374236, 8.374236, 4.942413), "Suburbs_Dirt_Mound_B9", _folder)
if a: placed += 1
else: skipped += 1

# Batch 26: StaticMesh'BalrogsNest_GuideMesh_Paintable_01' (1 instances)
_mesh_path = "/Game/LevelDesign/GuideMeshes/Chapter5/BalrogsNest/BalrogsNest_GuideMesh_Paintable_01"
_materials = ['/Game/Environments/ProcTexturing/GuideMeshFloor/M_GuideMeshFloor_Mines']
_folder = "Reconstruction/BD_BB_Chapter5_BalrogsNest/Meshes"
a = spawn_static_mesh(_mesh_path, _materials, (0.0, 0.0, 0.0), (0.0, 0.0, -0.0), (1.0, 1.0, 1.0), "BalrogsNest_GuideMesh_Paintable_01_12", _folder)
if a: placed += 1
else: skipped += 1

# Batch 27: StaticMesh'DetailRope1' (90 instances)
_mesh_path = "/Game/Unshippable/ThirdParty/WoodenConstructor/Meshes/Elements/DetailRope1"
_materials = ['/Game/Unshippable/ThirdParty/WoodenConstructor/Materials/RopeDetails_M']
_folder = "Reconstruction/BD_BB_Chapter5_BalrogsNest/Meshes"
a = spawn_static_mesh(_mesh_path, _materials, (9040.0, 5710.0, 2390.0), (87.18268770654745, -0.00277710000239164, 179.9999453581606), (1.0, 1.0, 1.0), "DetailRope100", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (9040.0, 5710.0, 2390.0), (0.00013698367294133528, -2.816039876103373, -89.99755925138), (1.0, 1.0, 1.0), "DetailRope101", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (9040.0, 5625.0, 2385.0), (87.18683266985332, -179.99995901883543, -179.99995901883543), (1.199539, 1.199539, 1.199539), "DetailRope102", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (9035.0, 5625.0, 2385.0), (0.0001279568431774831, 177.1841963293474, -89.99767641770126), (1.1839614, 1.1839614, 1.1839614), "DetailRope103", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (9040.0, 7245.0, 2390.0), (87.18268770654745, -0.00277710000239164, 179.9999453581606), (1.0, 1.0, 1.0), "DetailRope106", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (9040.0, 7245.0, 2390.0), (0.00013698367294133528, -2.816039876103373, -89.99755925138), (1.0, 1.0, 1.0), "DetailRope107", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (9050.0, 7375.0, 2385.0), (87.18683266985332, -179.99995901883543, -179.99995901883543), (1.199539, 1.199539, 1.199539), "DetailRope108", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (9045.0, 7375.0, 2385.0), (0.0001279568431774831, 177.1841963293474, -89.99767641770126), (1.183961, 1.183961, 1.183961), "DetailRope109", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (9340.003, 7245.001, 2390.0), (87.17740339089431, 179.99967898028535, -179.99976777233226), (1.0, 1.0, 1.0), "DetailRope116", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (9340.003, 7245.001, 2390.0), (0.00013692734532905833, 177.18395644159364, -89.99736480172403), (1.0, 1.0, 1.0), "DetailRope117", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (9340.002, 7375.002, 2385.0), (87.18448162474878, -0.00036621158042472827, -179.99963117042915), (1.199539, 1.199539, 1.199539), "DetailRope118", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (9345.005, 7375.0, 2385.0), (0.00013629171208166292, -2.815948573804682, -89.99760561885864), (1.183961, 1.183961, 1.183961), "DetailRope119", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (9340.0, 5714.999, 2390.0), (87.17740339089431, 179.99967898028535, -179.99976777233226), (1.0, 1.0, 1.0), "DetailRope122", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (9340.0, 5714.999, 2390.0), (0.00013692734532905833, 177.18395644159364, -89.99736480172403), (1.0, 1.0, 1.0), "DetailRope123", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (9339.998, 5624.9995, 2385.0), (87.18448162474878, -0.00036621158042472827, -179.99963117042915), (1.199539, 1.199539, 1.199539), "DetailRope124", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (9345.0, 5625.0, 2385.0), (0.00013629171208166292, -2.815948573804682, -89.99760561885864), (1.183961, 1.183961, 1.183961), "DetailRope125", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (9640.0, 5710.0, 2390.0), (87.18268770654745, -0.00277710000239164, 179.9999453581606), (1.0, 1.0, 1.0), "DetailRope132", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (9640.0, 5710.0, 2390.0), (0.00013698367294133528, -2.816039876103373, -89.99755925138), (1.0, 1.0, 1.0), "DetailRope133", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (9640.0, 5625.0, 2385.0), (87.18683266985332, -179.99995901883543, -179.99995901883543), (1.199539, 1.199539, 1.199539), "DetailRope134", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (9635.0, 5625.0, 2385.0), (0.0001279568431774831, 177.1841963293474, -89.99767641770126), (1.183961, 1.183961, 1.183961), "DetailRope135", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (9640.0, 7245.0, 2390.0), (87.18268770654745, -0.00277710000239164, 179.9999453581606), (1.0, 1.0, 1.0), "DetailRope138", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (9640.0, 7245.0, 2390.0), (0.00013698367294133528, -2.816039876103373, -89.99755925138), (1.0, 1.0, 1.0), "DetailRope139", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (8745.003, 7245.001, 2390.0), (87.17723319052766, 179.9996448299616, -179.99976777334683), (1.0, 1.0, 1.0), "DetailRope148", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (8745.003, 7245.001, 2390.0), (0.00013692734532905833, 177.18395644159364, -89.99736480172403), (1.0, 1.0, 1.0), "DetailRope149", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (8745.002, 7375.002, 2385.0), (87.18448162474878, -0.00036621158042472827, -179.99963117042915), (1.199539, 1.199539, 1.199539), "DetailRope150", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (8750.005, 7375.0, 2385.0), (0.00013693974412413613, -2.8159485737911742, -89.9976056347869), (1.183961, 1.183961, 1.183961), "DetailRope151", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (8745.0, 5714.999, 2390.0), (87.17723319052766, 179.9996448299616, -179.99976777334683), (1.0, 1.0, 1.0), "DetailRope154", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (8745.0, 5714.999, 2390.0), (0.00013692734532905833, 177.18395644159364, -89.99736480172403), (1.0, 1.0, 1.0), "DetailRope155", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (8744.998, 5624.9995, 2385.0), (87.18448162474878, -0.00036621158042472827, -179.99963117042915), (1.199539, 1.199539, 1.199539), "DetailRope156", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (8750.0, 5625.0, 2385.0), (0.00013693974412413613, -2.8159485737911742, -89.9976056347869), (1.183961, 1.183961, 1.183961), "DetailRope157", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (8455.0, 5710.0, 2390.0), (87.18268770654745, -0.00277710000239164, 179.9999453581606), (1.0, 1.0, 1.0), "DetailRope164", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (8455.0, 5710.0, 2390.0), (0.00013698367294133528, -2.816039876103373, -89.99755925138), (1.0, 1.0, 1.0), "DetailRope165", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (8470.0, 5625.0, 2385.0), (87.18683266985332, -179.99995901883543, -179.99995901883543), (1.199539, 1.199539, 1.199539), "DetailRope166", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (8450.0, 5625.0, 2385.0), (0.0001279568431774831, 177.1841963293474, -89.99767641770126), (1.183961, 1.183961, 1.183961), "DetailRope167", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (8455.0, 7245.0, 2390.0), (87.18268770654745, -0.00277710000239164, 179.9999453581606), (1.0, 1.0, 1.0), "DetailRope170", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (8455.0, 7245.0, 2390.0), (0.00013698367294133528, -2.816039876103373, -89.99755925138), (1.0, 1.0, 1.0), "DetailRope171", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (8470.0, 7375.0, 2385.0), (87.18683266985332, -179.99995901883543, -179.99995901883543), (1.199539, 1.199539, 1.199539), "DetailRope172", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (8450.0, 7375.0, 2385.0), (0.0001279568431774831, 177.1841963293474, -89.99767641770126), (1.183961, 1.183961, 1.183961), "DetailRope173", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (9910.003, 6634.998, 2390.0), (87.18448162474878, -0.00036621158042472827, -179.99963117042915), (1.0, 1.0, 1.0), "DetailRope174", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (9910.003, 6634.998, 2390.0), (0.00013693974412413613, -2.8159485737911742, -89.9976056347869), (1.0, 1.0, 1.0), "DetailRope175", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (9910.001, 6324.9995, 2390.0), (87.17723319052766, 179.9996448299616, -179.99976777334683), (1.0, 1.0, 1.0), "DetailRope176", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (9910.001, 6324.9995, 2390.0), (0.00013692734532905833, 177.18395644159364, -89.99736480172403), (1.0, 1.0, 1.0), "DetailRope177", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (9910.001, 6944.999, 2390.0), (87.17829179243734, 89.9962399771734, -179.99993024188225), (1.0, 1.0, 1.0), "DetailRope178", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (9910.001, 6944.999, 2390.0), (0.0001878022854517341, 87.18371744157079, -89.99716329681058), (1.0, 1.0, 1.0), "DetailRope179", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (9910.003, 7245.001, 2390.0), (87.17723319052766, 179.9996448299616, -179.99976777334683), (1.0, 1.0, 1.0), "DetailRope180", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (9905.001, 6055.0005, 2385.0), (87.17829179243734, 89.9962399771734, -179.99993024188225), (1.0, 1.0, 1.0), "DetailRope184", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (9905.001, 6055.0005, 2385.0), (0.0001878022854517341, 87.18371744157079, -89.99716329681058), (1.0, 1.0, 1.0), "DetailRope185", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (9050.0, 7635.0, 2185.0), (87.18683266985332, -179.99995901883543, -179.99995901883543), (1.199539, 1.199539, 1.199539), "DetailRope186", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (9340.0, 7635.0, 2185.0), (87.18419715344848, -0.0005798329374113742, -179.9997677730491), (1.199539, 1.199539, 1.199539), "DetailRope187_180", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (8750.0, 7635.0, 2185.0), (0.0003203814661720178, 87.18713269777382, -89.99870898390277), (1.199539, 1.199539, 1.199539), "DetailRope189", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (8155.0, 6320.0, 2390.0), (87.18683266985332, -179.99995901883543, -179.99995901883543), (1.0, 1.0, 1.0), "DetailRope190", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (8155.0, 6320.0, 2390.0), (0.0001279568431774831, 177.1841963293474, -89.99767641770126), (1.0, 1.0, 1.0), "DetailRope191", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (8155.0, 6635.0, 2390.0), (87.18268770654745, -0.00277710000239164, 179.9999453581606), (1.0, 1.0, 1.0), "DetailRope192", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (8155.0, 6635.0, 2390.0), (0.00013698367294133528, -2.816039876103373, -89.99755925138), (1.0, 1.0, 1.0), "DetailRope193", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (8155.0, 6030.0, 2390.0), (87.18140657535513, -90.00141665957233, -179.99983110751492), (1.0, 1.0, 1.0), "DetailRope194", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (8155.0, 6030.0, 2390.0), (0.0001415022123046386, -92.81604092328084, -89.99743929042255), (1.0, 1.0, 1.0), "DetailRope195", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (8169.85, 5720.0, 2378.7847), (75.93256858554672, -0.0005493161359411695, -179.99780067756564), (1.0, 1.0, 1.0), "DetailRope196", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (8150.497, 5720.234, 2384.9995), (0.00013698367294133528, -2.816039876103373, -89.99755925138), (1.0, 1.0, 1.0), "DetailRope197", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (8465.0, 7635.0, 2185.0), (87.18397489692745, -0.0005798332475791276, -179.99976777300674), (1.199539, 1.199539, 1.199539), "DetailRope200", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (9025.006, 5365.0, 2184.7546), (87.18683266985332, -179.99995901883543, -179.99995901883543), (1.199539, 1.199539, 1.199539), "DetailRope201", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (8730.0, 5365.0, 2185.0), (0.0003203814661720178, 87.18713269777382, -89.99870898390277), (1.199539, 1.199539, 1.199539), "DetailRope204", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (6900.0, 5365.0, 2185.0), (0.0003203814661720178, 87.18713269777382, -89.99870898390277), (1.199539, 1.199539, 1.479472), "DetailRope206", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (6600.0, 5365.0, 2185.0), (87.18397489692745, -0.0005798332475791276, -179.99976777300674), (1.199539, 1.199539, 1.4601406), "DetailRope207", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (7200.0, 5365.0, 2185.0), (0.0003203814661720178, 87.18713269777382, -89.99870898390277), (1.199539, 1.199539, 1.3464478), "DetailRope208", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (7520.0, 5365.0, 2185.0), (0.0003203814661720178, 87.18713269777382, -89.99870898390277), (1.199539, 1.199539, 1.479472), "DetailRope209", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (7804.9824, 5364.263, 2185.0), (0.0003203814661720178, 87.18713269777382, -89.99870898390277), (1.199539, 1.199539, 1.346448), "DetailRope210", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5650.0, 5365.0, 2185.0), (0.0003203814661720178, 87.18713269777382, -89.99870898390277), (1.199539, 1.199539, 1.479472), "DetailRope211", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5350.0, 5365.0, 2185.0), (87.18397489692745, -0.0005798332475791276, -179.99976777300674), (1.199539, 1.199539, 1.460141), "DetailRope212", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5950.0, 5365.0, 2185.0), (0.0003203814661720178, 87.18713269777382, -89.99870898390277), (1.199539, 1.199539, 1.346448), "DetailRope213", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (6270.0, 5365.0, 2185.0), (0.0003203814661720178, 87.18713269777382, -89.99870898390277), (1.199539, 1.199539, 1.479472), "DetailRope214", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4400.0, 5365.0, 2185.0), (0.0003203814661720178, 87.18713269777382, -89.99870898390277), (1.199539, 1.199539, 1.479472), "DetailRope215", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4100.0, 5365.0, 2185.0), (87.18397489692745, -0.0005798332475791276, -179.99976777300674), (1.199539, 1.199539, 1.460141), "DetailRope216", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4700.0, 5365.0, 2185.0), (0.0003203814661720178, 87.18713269777382, -89.99870898390277), (1.199539, 1.199539, 1.346448), "DetailRope217", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5020.0, 5365.0, 2185.0), (0.0003203814661720178, 87.18713269777382, -89.99870898390277), (1.199539, 1.199539, 1.479472), "DetailRope218", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (8455.0, 6040.0, 2390.0), (0.00013698367294133528, -2.816039876103373, -89.99755925138), (1.0, 1.0, 1.0), "DetailRope219", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (8455.0, 6340.0, 2390.0), (0.00013698367294133528, -2.816039876103373, -89.99755925138), (1.0, 1.0, 1.0), "DetailRope220", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (8455.0, 6630.0, 2390.0), (0.00013698367294133528, -2.816039876103373, -89.99755925138), (1.0, 1.0, 1.0), "DetailRope221", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (9039.987, 6945.0, 2390.0), (87.18268770654745, -0.00277710000239164, 179.9999453581606), (1.0, 1.0, 1.0), "DetailRope223", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (9339.99, 6945.001, 2390.0), (87.17723319052766, 179.9996448299616, -179.99976777334683), (1.0, 1.0, 1.0), "DetailRope224", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (9639.987, 6945.0, 2390.0), (87.18268770654745, -0.00277710000239164, 179.9999453581606), (1.0, 1.0, 1.0), "DetailRope225", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (8744.99, 6945.001, 2390.0), (87.17723319052766, 179.9996448299616, -179.99976777334683), (1.0, 1.0, 1.0), "DetailRope226", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (8454.987, 6945.0, 2390.0), (87.18268770654745, -0.00277710000239164, 179.9999453581606), (1.0, 1.0, 1.0), "DetailRope227", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (8745.0, 6009.999, 2390.0), (0.00013692734532905833, 177.18395644159364, -89.99736480172403), (1.0, 1.0, 1.0), "DetailRope228", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (9045.0, 6009.999, 2390.0), (0.00013692734532905833, 177.18395644159364, -89.99736480172403), (1.0, 1.0, 1.0), "DetailRope229", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (9345.0, 6009.999, 2390.0), (0.00013708104891199967, 2.808837705136898, -89.99718121266675), (1.0, 1.0, 1.0), "DetailRope230", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (9640.0, 6009.999, 2390.0), (0.00013692734532905833, 177.18395644159364, -89.99736480172403), (1.0, 1.0, 1.0), "DetailRope231", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (8471.435, 6330.0, 2368.6616), (30.937273429905712, 0.0, -0.0), (1.0, 1.0, 1.0), "DetailRope232", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (8471.435, 6635.0005, 2368.6616), (39.374788490974474, 1.0654111177085103e-05, -11.250762817595481), (1.0, 1.0, 1.0), "DetailRope233", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (9691.436, 6635.002, 2388.6616), (59.06222705035386, -179.99989754717188, 8.097205452918712e-05), (1.0, 1.0, 1.0), "DetailRope234", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (9695.064, 6320.0137, 2398.6409), (42.18716454779159, 177.18773412306788, -11.251156945501265), (1.0, 1.0, 1.0), "DetailRope235", _folder)
if a: placed += 1
else: skipped += 1

# Batch 28: StaticMesh'DetailRope2' (56 instances)
_mesh_path = "/Game/Unshippable/ThirdParty/WoodenConstructor/Meshes/Elements/DetailRope2"
_materials = ['/Game/Unshippable/ThirdParty/WoodenConstructor/Materials/RopeDetails_M']
_folder = "Reconstruction/BD_BB_Chapter5_BalrogsNest/Meshes"
a = spawn_static_mesh(_mesh_path, _materials, (972.6113, 5859.3125, 990.4873), (-0.2826530704239907, -83.23709078927584, -84.95068572175992), (1.0, 1.0, 1.0), "DetailRope12_256", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1488.8594, 5931.726, 990.5664), (-0.2826530704239907, -83.23709078927584, -84.95068572175992), (1.0, 1.0, 1.0), "DetailRope13_259", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2065.3633, 4737.125, 1626.313), (-0.28265445283155854, -81.1179193167835, -84.95079925629707), (1.0, 1.0, 1.0), "DetailRope17", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1518.3076, 4644.0557, 1633.1123), (0.2880997441112777, -80.6214909453507, -88.40543447476955), (1.0, 1.0, 1.0), "DetailRope18", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2681.6396, 4729.3994, 1039.0928), (-0.28265401872984175, -93.41205914212516, -84.95066517153934), (1.0, 1.0, 1.0), "DetailRope21", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2680.8086, 4726.8525, 1628.8228), (-0.28265401872984175, -93.41205914212516, -84.95066517153934), (1.0, 1.0, 1.0), "DetailRope23", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2114.9258, 4747.5146, 1032.1758), (0.9790172374834494, -95.44869438347166, -85.03832136232325), (1.0, 1.0, 1.0), "DetailRope24", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2119.754, 4745.5977, 1631.1289), (-0.28265445283155854, -81.1179193167835, -84.95079925629707), (1.0, 1.0, 1.0), "DetailRope25", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2732.58, 4734.6123, 1035.2759), (-6.210631310343262, -68.50775273243089, -76.39590453102329), (1.0, 1.0, 1.0), "DetailRope26", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3273.711, 4852.699, 1039.0928), (-0.2826540279706232, -78.41198904664557, -84.9506593984638), (1.0, 1.0, 1.0), "DetailRope28", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1464.3447, 4637.499, 1036.584), (-0.2826534026249311, -72.34927923417402, -84.95093979388798), (1.0, 1.0, 1.0), "DetailRope3", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3273.5664, 4850.0234, 1628.8228), (-0.2826540279706232, -78.41198904664557, -84.9506593984638), (1.0, 1.0, 1.0), "DetailRope30", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3308.8691, 4845.8086, 1631.0254), (-2.7023004621844207, -141.1500439701826, -87.4477481741675), (1.0, 1.0, 1.0), "DetailRope31_224", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3322.084, 4839.549, 1033.2266), (-0.28262458032004345, -126.03528265216143, -84.95031293804192), (1.0, 1.0, 1.0), "DetailRope32_226", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2705.836, 4753.6797, 1017.0918), (-7.75784219181966, 171.7223020043601, -116.28357401993512), (1.0, 1.0, 1.0), "DetailRope33_228", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2740.0977, 4726.8525, 1628.8228), (-0.282654877047107, -78.33581199058482, -84.95046098284507), (1.0, 1.0, 1.0), "DetailRope34_230", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3303.334, 4835.4688, 1600.3911), (15.048640747080025, -149.06450173301596, -42.48046609683359), (1.0, 1.0, 1.0), "DetailRope35", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3295.621, 4895.124, 1022.3462), (-1.8918453925461836, -176.65580601249255, -117.26517322514047), (1.0, 1.0, 1.0), "DetailRope36", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (972.2422, 5856.659, 1580.2163), (-0.2826530704239907, -83.23709078927584, -84.95068572175992), (1.0, 1.0, 1.0), "DetailRope38", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1488.4883, 5929.0723, 1580.2959), (-0.2826530704239907, -83.23709078927584, -84.95068572175992), (1.0, 1.0, 1.0), "DetailRope39", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2065.6328, 4739.79, 1036.584), (-0.28265445283155854, -81.1179193167835, -84.95079925629707), (1.0, 1.0, 1.0), "DetailRope4", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (924.55176, 5853.6685, 979.8364), (-0.28265181419003443, -83.23676372405022, -116.1842244859184), (1.0, 1.0, 1.0), "DetailRope41", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2085.123, 5934.1377, 985.9512), (-0.2826509740010258, -92.01064648999173, -84.95062286766229), (1.0, 1.0, 1.0), "DetailRope43", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2084.3516, 5931.5713, 1575.6797), (-0.2826509740010258, -92.01064648999173, -84.95062286766229), (1.0, 1.0, 1.0), "DetailRope45", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1536.9023, 5945.694, 1575.6797), (-0.2826509740010258, -92.01064648999173, -84.95062286766229), (1.0, 1.0, 1.0), "DetailRope46", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1536.9023, 5941.0444, 986.08105), (-0.2826509740010258, -92.01064648999173, -84.95062286766229), (1.0, 1.0, 1.0), "DetailRope47", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2130.5605, 5934.1367, 977.5176), (0.4386253607372555, -91.98257655767245, -64.48055274316205), (1.0, 1.0, 1.0), "DetailRope48", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1185.1787, 4165.506, 966.6411), (-0.2825017730894197, -165.88309620455374, -84.94981492521323), (1.0, 1.0, 1.0), "DetailRope49", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1323.0723, 3662.7769, 966.7207), (-0.2825017730894197, -165.88309620455374, -84.94981492521323), (1.0, 1.0, 1.0), "DetailRope50", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1182.5, 4165.535, 1556.3706), (-0.2825017730894197, -165.88309620455374, -84.94981492521323), (1.0, 1.0, 1.0), "DetailRope53", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1320.3984, 3662.8037, 1556.4502), (-0.2825017730894197, -165.88309620455374, -84.94981492521323), (1.0, 1.0, 1.0), "DetailRope54", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1173.4268, 4212.451, 955.9907), (-0.28250115693434885, -165.88258743166676, -116.18049890581361), (1.0, 1.0, 1.0), "DetailRope56", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1401.791, 3071.7246, 962.105), (-0.282470796360794, -174.65631493108134, -84.95000557026829), (1.0, 1.0, 1.0), "DetailRope58", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1409.1533, 3072.1611, 1551.8335), (-0.282470796360794, -174.65631493108134, -84.95000557026829), (1.0, 1.0, 1.0), "DetailRope60", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1343.0801, 3616.918, 1551.8335), (-0.282470796360794, -174.65631493108134, -84.95000557026829), (1.0, 1.0, 1.0), "DetailRope61", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1338.4697, 3616.3198, 962.23535), (-0.282470796360794, -174.65631493108134, -84.95000557026829), (1.0, 1.0, 1.0), "DetailRope62", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2114.9258, 4742.5146, 1192.1758), (0.9790172374834494, -95.44869438347166, -85.03832136232325), (1.0, 1.0, 1.0), "DetailRope65", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2681.6396, 4729.3994, 1144.0928), (-0.28265401872984175, -93.41205914212516, -84.95066517153934), (1.0, 1.0, 1.0), "DetailRope67", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1185.1787, 4165.506, 1261.6411), (-0.2825017730894197, -165.88309620455374, -84.94981492521323), (1.0, 1.0, 1.0), "DetailRope69", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1323.0723, 3662.7769, 1256.7207), (-0.2825017730894197, -165.88309620455374, -84.94981492521323), (1.0, 1.0, 1.0), "DetailRope71", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1444.1533, 3057.1611, 1556.8335), (-0.2824435632616572, 100.34368882954291, -84.94992338383909), (1.0, 1.0, 1.0), "DetailRope72", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1488.8594, 5936.726, 1280.5664), (-0.2826561062175312, -78.23706187905543, -84.95069019666414), (1.0, 1.0, 1.0), "DetailRope74", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1528.8594, 5944.9155, 1280.5664), (-0.28265335986325246, -83.23705487755664, -84.95068773092513), (1.0, 1.0, 1.0), "DetailRope75", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (972.6113, 5859.3125, 1287.7195), (-0.2826530704239907, -83.23709078927584, -84.95068572175992), (1.0, 1.0, 1.0), "DetailRope76", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1212.615, 2359.195, 966.6411), (-0.282501499668894, 174.11684822499845, -84.9497660846365), (1.0, 1.0, 1.0), "DetailRope79", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1170.2488, 1839.6218, 966.7207), (-0.282501499668894, 174.11684822499845, -84.9497660846365), (1.0, 1.0, 1.0), "DetailRope80", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1210.1078, 2360.1387, 1556.3706), (-0.282501499668894, 174.11684822499845, -84.9497660846365), (1.0, 1.0, 1.0), "DetailRope83", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1167.7454, 1840.5615, 1556.4502), (-0.282501499668894, 174.11684822499845, -84.9497660846365), (1.0, 1.0, 1.0), "DetailRope84", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1217.6278, 2407.3286, 955.9907), (-0.28250133933922456, 174.1174373830505, -116.18039613108186), (1.0, 1.0, 1.0), "DetailRope86", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1042.0684, 1257.291, 962.105), (-0.2824697826930186, 165.34364825962314, -84.9499416824933), (1.0, 1.0, 1.0), "DetailRope88", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1049.136, 1255.1831, 1551.8335), (-0.2824697826930186, 165.34364825962314, -84.9499416824933), (1.0, 1.0, 1.0), "DetailRope90", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1173.3654, 1789.6855, 1551.8335), (-0.2824697826930186, 165.34364825962314, -84.9499416824933), (1.0, 1.0, 1.0), "DetailRope91", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1168.8285, 1790.7002, 962.23535), (-0.2824697826930186, 165.34364825962314, -84.9499416824933), (1.0, 1.0, 1.0), "DetailRope92", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1212.615, 2359.195, 1261.6411), (-0.282501499668894, 174.11684822499845, -84.9497660846365), (1.0, 1.0, 1.0), "DetailRope94", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1170.2488, 1839.6218, 1256.7207), (-0.282501499668894, 174.11684822499845, -84.9497660846365), (1.0, 1.0, 1.0), "DetailRope96", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1076.8949, 1229.117, 1556.8335), (-0.28244264454675005, 80.34365240077136, -84.9499140495994), (1.0, 1.0, 1.0), "DetailRope97", _folder)
if a: placed += 1
else: skipped += 1

# Batch 29: StaticMesh'DetailRope4' (35 instances)
_mesh_path = "/Game/Unshippable/ThirdParty/WoodenConstructor/Meshes/Elements/DetailRope4"
_materials = ['/Game/Unshippable/ThirdParty/WoodenConstructor/Materials/RopeDetails_M']
_folder = "Reconstruction/BD_BB_Chapter5_BalrogsNest/Meshes"
a = spawn_static_mesh(_mesh_path, _materials, (1512.002, 5941.2974, 989.7803), (0.0, -100.88882456173256, 0.0), (1.0, 1.0, 1.0), "DetailRope11_255", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (946.8711, 5846.737, 989.8862), (0.0, -100.88891444324449, 0.0), (1.0, 1.0, 1.0), "DetailRope14_260", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2088.4053, 4750.211, 1035.7974), (0.0, -98.76922405024767, 0.0), (1.0, 1.0, 1.0), "DetailRope15", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2088.1348, 4747.547, 1625.5264), (0.0, -98.76922405024767, 0.0), (1.0, 1.0, 1.0), "DetailRope16_152", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1335.5322, 3641.0493, 965.9341), (0.0, 176.4649462002816, -0.0), (1.0, 1.0, 1.0), "DetailRope19", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2706.1084, 4734.7324, 1038.3066), (0.0, -111.063078679005, 0.0), (1.0, 1.0, 1.0), "DetailRope20", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2705.2773, 4732.1875, 1628.0361), (0.0, -111.063078679005, 0.0), (1.0, 1.0, 1.0), "DetailRope22", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3295.9648, 4864.1836, 1038.3066), (0.0, -96.06323218456711, 0.0), (1.0, 1.0, 1.0), "DetailRope27", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3295.8213, 4861.509, 1628.0361), (0.0, -96.06323218456711, 0.0), (1.0, 1.0, 1.0), "DetailRope29", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1511.6328, 5938.6445, 1579.5093), (0.0, -100.88882456173256, 0.0), (1.0, 1.0, 1.0), "DetailRope37", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (949.8203, 5861.35, 1579.6152), (0.0, -100.88891444324449, 0.0), (1.0, 1.0, 1.0), "DetailRope40", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2109.4531, 5940.0664, 985.16406), (0.0, -109.66163186332591, 0.0), (1.0, 1.0, 1.0), "DetailRope42", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2108.6865, 5937.501, 1574.8926), (0.0, -109.66163186332591, 0.0), (1.0, 1.0, 1.0), "DetailRope44", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1485.2637, 4651.2695, 1035.7974), (0.0, -90.0001164887758, 0.0), (1.0, 1.0, 1.0), "DetailRope5_29", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1169.415, 4189.425, 966.04004), (0.0, 176.46489746952793, -0.0), (1.0, 1.0, 1.0), "DetailRope51", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1332.8477, 3641.0757, 1555.6636), (0.0, 176.4649462002816, -0.0), (1.0, 1.0, 1.0), "DetailRope52", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1184.2842, 4188.371, 1555.7695), (0.0, 176.46489746952793, -0.0), (1.0, 1.0, 1.0), "DetailRope55", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1410.7881, 3048.3535, 961.31836), (0.0, 167.6916627360131, -0.0), (1.0, 1.0, 1.0), "DetailRope57", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1408.1455, 3048.787, 1551.0469), (0.0, 167.6916627360131, -0.0), (1.0, 1.0, 1.0), "DetailRope59", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1477.0137, 4651.7764, 1035.9033), (0.0, -90.0001164887758, 0.0), (1.0, 1.0, 1.0), "DetailRope6", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2088.4053, 4750.211, 1190.7974), (0.0, -98.76922405024767, 0.0), (1.0, 1.0, 1.0), "DetailRope64", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2706.1084, 4734.7324, 1143.3066), (0.0, -111.063078679005, 0.0), (1.0, 1.0, 1.0), "DetailRope66", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1184.415, 4189.425, 1261.04), (0.0, 176.46489746952793, -0.0), (1.0, 1.0, 1.0), "DetailRope68", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1485.4014, 4648.5938, 1625.5264), (0.0, -90.0001164887758, 0.0), (1.0, 1.0, 1.0), "DetailRope7_76", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1335.5322, 3641.0493, 1255.9341), (0.0, 176.4649462002816, -0.0), (1.0, 1.0, 1.0), "DetailRope70", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1512.002, 5941.2974, 1279.7803), (0.0, -100.88882456173256, 0.0), (1.0, 1.0, 1.0), "DetailRope73", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (950.41516, 5859.601, 1287.1184), (0.0, -100.88891444324449, 0.0), (1.0, 1.0, 1.0), "DetailRope77", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1174.5261, 1814.9429, 965.9341), (0.0, 156.46490429378701, -0.0), (1.0, 1.0, 1.0), "DetailRope78", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1205.9827, 2387.0627, 966.04004), (0.0, 156.46490429378701, -0.0), (1.0, 1.0, 1.0), "DetailRope81", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1172.0126, 1815.886, 1555.6636), (0.0, 156.46490429378701, -0.0), (1.0, 1.0, 1.0), "DetailRope82", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1219.5945, 2380.9873, 1555.7695), (0.0, 156.46490429378701, -0.0), (1.0, 1.0, 1.0), "DetailRope85", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1042.5294, 1232.2522, 961.31836), (0.0, 147.691572467388, -0.0), (1.0, 1.0, 1.0), "DetailRope87", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1040.1946, 1233.5632, 1551.0469), (0.0, 147.691572467388, -0.0), (1.0, 1.0, 1.0), "DetailRope89", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1220.0779, 2381.9324, 1261.04), (0.0, 156.46490429378701, -0.0), (1.0, 1.0, 1.0), "DetailRope93", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1174.5261, 1814.9429, 1255.9341), (0.0, 156.46490429378701, -0.0), (1.0, 1.0, 1.0), "DetailRope95", _folder)
if a: placed += 1
else: skipped += 1

# Batch 30: StaticMesh'PWM_Nordic_8x8x8_A' (111 instances)
_mesh_path = "/Game/Unshippable/Whitebox/Rocks/Meshes/PWM_Nordic_8x8x8_A"
_materials = ['/Game/Environments/ProcTexturing/ProcMaterial_Quarry_2mx5m_B2']
_folder = "Reconstruction/BD_BB_Chapter5_BalrogsNest/Meshes"
a = spawn_static_mesh(_mesh_path, _materials, (4791.421, 7269.0474, 1046.0093), (0.0, -63.50222712192131, 0.0), (1.0, 1.0, 1.0), "PWM_Nordic_8x8x8_A10_54", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (796.19824, 4870.8286, 2834.7988), (8.145018820231737, 4.612213118881138, -0.38238528634433266), (1.333276, 1.46272, 1.276657), "PWM_Nordic_8x8x8_A100", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1302.8964, 3679.7097, 2425.9343), (-3.8731690678766744, 126.32053915719416, -179.94029714476721), (1.333276, 1.061544, 1.276657), "PWM_Nordic_8x8x8_A101", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1607.6227, 3740.007, 2049.908), (-0.8025512427468734, -173.41236289313125, 176.21019956983824), (1.2118814, 1.0, 1.1552625), "PWM_Nordic_8x8x8_A102", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (656.9243, 2170.567, 2555.2124), (-8.262418893794727, 142.84817648985626, 105.5400193311034), (0.958344, 0.625068, 0.901725), "PWM_Nordic_8x8x8_A103", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2100.2324, 5207.3203, 2489.8433), (-86.52649248690301, 71.12067223618128, 36.11022503475188), (1.0, 1.0, 1.4896259), "PWM_Nordic_8x8x8_A104", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (11424.084, 10850.982, 1209.2582), (-2.8114624849832905, 24.115723193034093, 0.2127685105430473), (1.194442, 0.8289655, 1.471542), "PWM_Nordic_8x8x8_A105", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (11748.92, 10330.68, 2037.8922), (-74.51215320385937, -59.01904713740679, -24.443358899751313), (1.194442, 1.0917555, 1.471542), "PWM_Nordic_8x8x8_A106", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (11831.966, 9017.552, 2109.3718), (-78.51844655940965, -25.945951009083497, 100.68478349766494), (1.3018291, 1.091756, 1.471542), "PWM_Nordic_8x8x8_A107", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (12506.007, 8373.012, 1267.4473), (5.240540121020955, 97.73602575686546, -3.008057313796099), (1.194442, 1.2354937, 2.1131427), "PWM_Nordic_8x8x8_A108", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (12299.818, 10865.719, 1267.4473), (5.240539868175147, 81.13581232511712, -3.008057017244148), (1.194442, 1.132857, 2.010506), "PWM_Nordic_8x8x8_A109", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (8077.5986, 8540.084, 2411.2324), (-35.59356810912458, -20.048520777414957, -7.185179299396618), (0.86101824, 1.2108585, 1.477917), "PWM_Nordic_8x8x8_A11", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (419.09207, 1597.4283, 2512.1072), (-0.21920776088113533, -172.14783441565697, 102.8133876699393), (0.958344, 0.625068, 0.901725), "PWM_Nordic_8x8x8_A110", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (367.92676, 2087.0127, 2542.4788), (-9.148528868353296, 157.62823526467275, 110.6240520814485), (0.958344, 0.625068, 0.901725), "PWM_Nordic_8x8x8_A111", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (713.37146, 3259.732, 2775.544), (8.07171502490109, -0.8863220305235744, -1.1583861497130938), (1.333276, 1.46272, 1.276657), "PWM_Nordic_8x8x8_A112", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (704.2573, 4667.2876, 2798.437), (7.0980225832118355, -2.640777723266859, -3.429443407524839), (1.333276, 1.46272, 1.276657), "PWM_Nordic_8x8x8_A113", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (11737.956, 6714.347, 2355.4004), (2.176658274984507, 160.07349797177227, -2.338104187030196), (1.390303, 1.0, 1.399991), "PWM_Nordic_8x8x8_A114", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (9156.893, 8993.623, 3025.3384), (55.046118792076186, 103.1768907878556, -29.941897409778907), (1.0, 1.2598256, 1.4015827), "PWM_Nordic_8x8x8_A12", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (10356.471, 7276.801, 2832.0244), (-57.85926400410577, -174.6052263541519, -174.42395731714674), (0.69746935, 1.0238339, 1.0238339), "PWM_Nordic_8x8x8_A13_133", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (8571.779, 9482.378, 2388.7393), (3.433045237504592, -148.0500495959851, -157.89575528935717), (1.5034516, 1.0, 1.477917), "PWM_Nordic_8x8x8_A14", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (6729.783, 5244.441, 2762.9395), (-77.17301806664588, 109.8468716009405, -17.912979014039287), (1.136463, 1.2011669, 1.6081239), "PWM_Nordic_8x8x8_A15_143", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2235.6846, 4844.135, 2468.3066), (62.074786747045565, -90.00010365574681, -5.44299226874481), (1.0, 1.0, 1.0), "PWM_Nordic_8x8x8_A16_146", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2173.5908, 5570.882, 2548.4863), (-77.0791933316858, 155.612067507595, 122.16880742787038), (1.0, 1.0, 1.1373614), "PWM_Nordic_8x8x8_A17", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2897.3555, 4993.3486, 2393.4902), (-73.2259821124135, 133.5611557396843, -42.90189935583461), (0.8675224, 0.8830348, 1.0), "PWM_Nordic_8x8x8_A18", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3385.2402, 5514.321, 2442.8916), (82.60631981433083, -130.35101429757262, 126.85390110603754), (0.867522, 0.883035, 1.0), "PWM_Nordic_8x8x8_A19", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (11245.4795, 5406.0137, 1203.0371), (18.571078519476266, 170.3065198346119, -1.893890653356852), (1.0, 1.0, 1.3999914), "PWM_Nordic_8x8x8_A2", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (7348.4604, 5340.2886, 2782.608), (14.656860938660973, -17.78503282351324, 168.11010264869685), (0.83354276, 0.82854486, 0.874433), "PWM_Nordic_8x8x8_A20", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (10625.123, 6112.282, 2666.245), (46.60047180076418, -34.87188543019734, -49.97897472021115), (0.447755, 1.129984, 1.569231), "PWM_Nordic_8x8x8_A21", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (8979.037, 4641.1133, 2509.8237), (-6.202453423321618, 96.75757299749749, -164.96047238614273), (1.0, 1.0, 1.0), "PWM_Nordic_8x8x8_A22_229", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (8461.231, 7811.119, 2893.1182), (-62.691256356216066, 11.426096800623611, -51.902842846205544), (1.0, 1.0, 1.1384177), "PWM_Nordic_8x8x8_A23", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (10552.943, 8134.4824, 2762.1519), (-33.106657615558575, 141.48999790196586, -159.40795848913405), (1.194442, 1.132857, 1.4715416), "PWM_Nordic_8x8x8_A24", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (10561.888, 4719.698, 1259.4985), (1.1421375494835617, 113.92931229251434, 2.09436045416098), (1.0, 1.0, 1.4245237), "PWM_Nordic_8x8x8_A25", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (10984.266, 5751.0884, 1173.6611), (5.507171444850394, -147.5173347043916, 5.720153515592152), (1.0, 1.0, 1.399991), "PWM_Nordic_8x8x8_A27", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (9329.305, 3964.963, 1139.5186), (13.976582817581146, 119.60365781648181, 7.868204790427928), (0.705975, 1.0, 1.424524), "PWM_Nordic_8x8x8_A28", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (9658.41, 10003.927, 2709.3613), (24.805510273574487, 123.31758605893813, -174.54327339418575), (1.0942638, 1.0229486, 1.401583), "PWM_Nordic_8x8x8_A29", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (8547.762, 4574.418, 3000.858), (62.67212312009843, -74.454652701516, 11.450284046648889), (1.0, 1.0, 1.0), "PWM_Nordic_8x8x8_A3", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (6559.752, 7451.298, 1160.2632), (-2.8802491542634012, 50.16586188332101, -3.344604764827983), (1.0, 1.0, 1.0), "PWM_Nordic_8x8x8_A30_241", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (11052.016, 7719.291, 2048.046), (-22.002593214803035, 170.49947221345263, -20.13329938841361), (1.390303, 1.0, 1.399991), "PWM_Nordic_8x8x8_A31_125", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (8750.089, 4013.0942, 1139.5186), (14.975167504853827, 71.29606722424825, 5.701647113118248), (0.705975, 1.0, 1.424524), "PWM_Nordic_8x8x8_A32_38", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3626.204, 4943.1533, 2342.8257), (-74.4345212277943, 16.69438770443202, 74.16740076493778), (0.867522, 0.883035, 1.3269985), "PWM_Nordic_8x8x8_A33_223", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (11264.728, 8376.596, 1267.4473), (5.240539788314469, 124.87821303409794, -3.0080565850513095), (1.194442, 1.182429, 1.471542), "PWM_Nordic_8x8x8_A34", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (6560.04, 6345.1494, 2934.749), (58.108685504048545, 86.00718679578172, 173.8217251670472), (1.0228484, 1.2473766, 1.258672), "PWM_Nordic_8x8x8_A35", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3565.836, 6736.34, 1029.3335), (-2.8259587528047336, 13.340668750743806, 3.157844217263623), (0.7175321, 0.7175321, 0.7175321), "PWM_Nordic_8x8x8_A36_83", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5212.006, 3962.111, 1220.3105), (0.0, -80.23560445462932, 0.0), (1.0, 1.0, 1.0), "PWM_Nordic_8x8x8_A37_147", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5313.2554, 3985.5505, 1848.5571), (19.780129838950845, -85.45485474004542, -1.175141429814018), (1.0, 1.0, 1.0), "PWM_Nordic_8x8x8_A38", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (6636.165, 4381.1475, 1024.8296), (14.905760241204872, 71.89001800438129, 1.2362045019712499e-05), (1.0, 1.0, 1.0), "PWM_Nordic_8x8x8_A39_162", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (8167.2495, 4170.666, 2515.83), (-6.853455029626683, 89.9952441469274, 178.54651745833024), (1.0, 1.0, 1.0), "PWM_Nordic_8x8x8_A4", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (6359.9756, 4322.96, 1723.8633), (2.8902965619255663, -132.40322021833356, 179.5894570271548), (1.0, 1.0, 1.2886931), "PWM_Nordic_8x8x8_A40", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5964.1865, 4686.5264, 1145.1909), (0.0, 150.10964786210928, -0.0), (0.52427226, 0.8200201, 0.52427226), "PWM_Nordic_8x8x8_A41_176", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5687.2324, 5663.235, 2829.2725), (82.23866365518556, -126.48908405844013, -128.81911845370894), (0.78989595, 1.201167, 1.477917), "PWM_Nordic_8x8x8_A42", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4813.767, 5615.029, 2820.8643), (82.66585618858687, -121.12651333298436, 61.427024119768284), (0.789896, 1.201167, 1.477917), "PWM_Nordic_8x8x8_A43", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4094.8877, 5398.728, 2664.9932), (62.37704520923328, -160.97010048913592, 106.29255791767939), (0.789896, 1.201167, 1.477917), "PWM_Nordic_8x8x8_A44", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (7197.9873, 4156.507, 1824.0562), (3.5645725802418804, -71.67864764420675, 177.5564919747068), (1.0, 1.0, 1.288693), "PWM_Nordic_8x8x8_A45", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (8780.227, 9420.754, 1168.206), (4.7390061577799205, -86.74017704702062, -2.336700464426147), (0.959061, 0.959061, 1.3835849), "PWM_Nordic_8x8x8_A46", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (10502.551, 10646.564, 1217.2256), (11.444366841330648, -75.09003155839514, 0.951538450531782), (1.194442, 1.132857, 1.471542), "PWM_Nordic_8x8x8_A47", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (10685.533, 10204.336, 2778.3735), (-35.334717666813596, -82.29101504042637, -169.73680987791937), (1.3080693, 1.0, 1.3487959), "PWM_Nordic_8x8x8_A48", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (11377.539, 8634.325, 2384.8154), (-22.820619045973675, 142.3962337598142, -170.5134340605971), (1.194442, 1.132857, 1.471542), "PWM_Nordic_8x8x8_A49", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (7017.4937, 6792.2812, 2624.3535), (-50.607759726915056, -88.37469955508905, 93.56894546721594), (1.247461, 1.247461, 0.96612835), "PWM_Nordic_8x8x8_A5", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (11104.285, 10110.521, 2385.4224), (-19.828519244485403, -125.36944322804096, -169.2620817752164), (1.194442, 1.132857, 1.471542), "PWM_Nordic_8x8x8_A50", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (10905.938, 8895.041, 2935.974), (-44.36517289978845, 134.83901030314416, -170.05358302792172), (1.194442, 1.132857, 1.471542), "PWM_Nordic_8x8x8_A51", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (10316.619, 9529.311, 3116.3152), (-47.09368347818889, -93.58495321470015, -170.12841776623202), (1.194442, 1.132857, 1.471542), "PWM_Nordic_8x8x8_A52", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (9908.135, 8786.549, 3279.2432), (-46.6080234021922, -63.26750665141164, 179.0108618118268), (1.194442, 1.132857, 1.471542), "PWM_Nordic_8x8x8_A53", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1345.2324, 5456.301, 2719.8433), (-68.22890672841469, -83.81434067241452, 11.216486364246082), (1.0, 1.0, 1.137361), "PWM_Nordic_8x8x8_A54", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1366.9814, 1472.669, 2546.1514), (-57.95895658877972, 110.82701822068223, -12.55749053582841), (1.3332757, 1.0, 1.2766567), "PWM_Nordic_8x8x8_A55", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (797.7676, 5168.636, 2550.5098), (-12.083342238759217, -174.8888053545996, 103.10846367865032), (0.9583439, 0.6250681, 0.9017249), "PWM_Nordic_8x8x8_A56", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (483.4453, 6146.062, 2334.7988), (32.160003417584704, 114.53266277375833, 1.4549574699770293), (1.333276, 1.2694488, 1.276657), "PWM_Nordic_8x8x8_A57", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (9576.415, 4093.7698, 1139.5186), (14.748603962336851, 136.60369405471562, 3.6307373773090585), (0.705975, 1.0, 1.424524), "PWM_Nordic_8x8x8_A58", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (9215.186, 4121.7686, 1956.6968), (-39.534329887231486, 98.98437208798151, -1.481051693608954), (0.705975, 1.0, 1.424524), "PWM_Nordic_8x8x8_A59", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (10577.128, 6933.42, 2549.0645), (-26.99120637425109, -178.4094299347071, -168.98302820771397), (1.0, 1.0, 1.2706152), "PWM_Nordic_8x8x8_A6", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (11072.19, 5071.773, 2096.1746), (-29.4695154358079, 144.86742794292113, 2.547271837129256), (1.2308923, 1.2007322, 1.399991), "PWM_Nordic_8x8x8_A60", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (8490.432, 4610.0312, 2349.4727), (-28.243772785426533, 94.49494113401704, -164.28680529714939), (1.0, 1.0, 1.0), "PWM_Nordic_8x8x8_A61", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (9962.411, 8716.644, 3051.9355), (-85.3567398664604, -175.7122270360696, -27.95807764707723), (1.194442, 1.132857, 1.471542), "PWM_Nordic_8x8x8_A62", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (7494.2686, 8180.4204, 1158.9584), (-2.538665559475792, 55.78654571584427, -3.6105341082839444), (1.0, 1.0, 1.0), "PWM_Nordic_8x8x8_A63", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (9980.899, 5917.443, 2923.775), (-26.53747424436797, 117.21410740377021, 93.83502005976173), (0.71396, 1.0180155, 1.2038949), "PWM_Nordic_8x8x8_A64", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (10114.253, 7027.162, 2862.06), (-70.75558041179323, -156.80701406756003, -11.987005176403564), (0.71396, 1.0962518, 1.0), "PWM_Nordic_8x8x8_A65", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (9256.217, 4895.198, 2695.9531), (58.50447925785062, -103.97740724147364, -18.05746316118361), (0.71396, 1.0, 1.0), "PWM_Nordic_8x8x8_A66_12", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (7806.1714, 6109.9126, 2935.9756), (-51.953696351093555, 12.517134194309513, -8.195983377148476), (0.71396, 1.291952, 1.203895), "PWM_Nordic_8x8x8_A67", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (8379.469, 7433.8633, 2711.712), (-70.8397813839852, -3.077234124177968, -45.9273070630645), (0.44225726, 1.0202492, 0.93219215), "PWM_Nordic_8x8x8_A68", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (8342.152, 7035.6606, 2896.3457), (-73.04862776793824, -39.95408934909834, 14.612733101369741), (0.442257, 0.9414799, 0.74440515), "PWM_Nordic_8x8x8_A69_66", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (11101.395, 7697.7305, 1273.4214), (5.699710659979348, 174.05310652646762, -12.215087200676727), (1.390303, 1.0, 1.399991), "PWM_Nordic_8x8x8_A7_72", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (9355.876, 4964.8633, 2703.913), (-77.0683543938308, 121.53884916012592, -8.02222336477221), (0.71396, 1.096252, 1.0), "PWM_Nordic_8x8x8_A70", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (8516.352, 5010.512, 2616.434), (-72.81909020062452, 76.34692495048942, 7.357521981362353), (0.71396, 1.4917036, 1.0), "PWM_Nordic_8x8x8_A71", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (9284.988, 7511.5693, 2800.7368), (-69.39714595774846, -79.62248612716091, -3.540039508914865), (0.71396, 1.491704, 1.0), "PWM_Nordic_8x8x8_A72", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (8155.1523, 6234.4136, 2984.0723), (-57.7022440874464, 5.625320582667563, -2.015320058585241), (0.442257, 0.94148, 0.744405), "PWM_Nordic_8x8x8_A73", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (8887.831, 5398.6914, 3050.8232), (-57.701943126325496, 92.98486485248608, -2.015321545846049), (0.442257, 0.94148, 0.744405), "PWM_Nordic_8x8x8_A74", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (797.7676, 4441.421, 2550.5098), (-12.083342238759217, -174.8888053545996, 103.10846367865032), (0.958344, 0.625068, 0.901725), "PWM_Nordic_8x8x8_A75", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (597.7676, 1613.4102, 2550.5093), (-12.083342238759217, -174.8888053545996, 103.10846367865032), (0.958344, 0.625068, 0.901725), "PWM_Nordic_8x8x8_A76", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1747.8226, 3167.4004, 2362.469), (-11.107908622750386, 17.263850460433645, 179.10501056152637), (1.333276, 1.0, 1.276657), "PWM_Nordic_8x8x8_A77", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2019.4321, 2533.6018, 1429.2133), (7.547636980753456, 118.07745009876254, 177.33468713793854), (1.2537961, 1.2537961, 1.391157), "PWM_Nordic_8x8x8_A78", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1345.2324, 4792.3203, 2584.8433), (-68.2251314340076, 96.28822062804552, 11.22320337259512), (1.0, 1.0, 1.137361), "PWM_Nordic_8x8x8_A79", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (11865.693, 8166.715, 1267.4473), (5.240539788314469, 124.87821303409794, -3.0080565850513095), (1.194442, 1.132857, 1.471542), "PWM_Nordic_8x8x8_A80", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (12050.9375, 8634.325, 2384.8154), (-22.820619045973675, 142.3962337598142, -170.5134340605971), (1.194442, 1.132857, 1.471542), "PWM_Nordic_8x8x8_A81", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (11905.766, 9765.076, 2788.2415), (-57.004910758751045, 179.33849950338134, -92.01097840680667), (1.194442, 1.132857, 1.471542), "PWM_Nordic_8x8x8_A82", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (8064.703, 6258.374, 3731.2942), (-14.241731538525533, 9.208634951366266, 10.143183432645436), (1.0, 1.0, 1.1252373), "PWM_Nordic_8x8x8_A83", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (9490.005, 7175.539, 3489.4954), (-23.70855853207644, -101.04321032381249, 25.322708607373517), (1.0998967, 1.0, 1.203895), "PWM_Nordic_8x8x8_A84", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (8643.952, 5408.6025, 3766.9294), (19.90151002812555, -113.80376906234444, 6.0445318104761965), (1.0, 1.0, 1.0), "PWM_Nordic_8x8x8_A85", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (9180.152, 5409.4136, 3284.0723), (-57.70208660957759, -84.37470005905277, -2.0153140578379514), (0.7230945, 0.94148, 0.744405), "PWM_Nordic_8x8x8_A86", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (9659.189, 5764.5693, 3737.1118), (-10.493897910093127, 123.56168392310909, -14.619507217571776), (1.0, 1.0, 1.0), "PWM_Nordic_8x8x8_A87", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (8472.445, 7461.32, 3124.4238), (-73.04859959557422, -39.95395501709606, -30.38714896590755), (1.3257821, 1.825005, 1.6279302), "PWM_Nordic_8x8x8_A88", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (8577.152, 5569.9966, 4082.3188), (-4.816161635778161, 62.613934498567716, -172.23034735571522), (1.0, 1.0, 1.0), "PWM_Nordic_8x8x8_A89", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (7262.1396, 7733.726, 2030.1973), (9.197326923660865, -106.0423592039412, -175.9764444333567), (1.488552, 0.8989793, 1.477917), "PWM_Nordic_8x8x8_A9", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (8388.887, 6910.502, 4369.97), (-24.38397275985656, -43.248652648822, 21.9466209976523), (1.0, 1.0, 1.0), "PWM_Nordic_8x8x8_A90", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (10002.471, 6059.816, 3434.8154), (-18.678252150451126, 133.66760490340783, 99.16954523604689), (1.0, 1.0, 1.0), "PWM_Nordic_8x8x8_A91", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (9742.152, 5679.9966, 4202.319), (-4.816161838030577, -41.44836763710215, -172.2301984448096), (1.0, 1.0, 1.0), "PWM_Nordic_8x8x8_A92", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (9753.887, 6580.502, 4369.97), (-24.383913089455486, -163.2485353571539, 21.946412183383597), (1.0, 1.0, 1.0), "PWM_Nordic_8x8x8_A93", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (9933.887, 7010.502, 4809.97), (-24.383848218534492, 21.751707163489638, 21.94631854360263), (1.0, 1.0, 1.0), "PWM_Nordic_8x8x8_A94", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (10018.887, 6195.502, 4954.97), (-19.319639530939487, 167.4530801757211, 6.720619920505247), (1.0, 1.0, 1.0), "PWM_Nordic_8x8x8_A95", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1764.837, 1609.1223, 1419.5573), (5.321166319156019, 176.4714103139585, -172.83687364897037), (1.2796283, 1.0, 1.137361), "PWM_Nordic_8x8x8_A96", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1440.8964, 2120.8286, 2284.7988), (-8.844754647986484, -177.96002144706677, -171.43018407843138), (1.333276, 1.0, 1.3369067), "PWM_Nordic_8x8x8_A97", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (796.19824, 3370.8286, 2834.7988), (8.145018820231737, 4.612213118881138, -0.38238528634433266), (1.333276, 1.4627198, 1.276657), "PWM_Nordic_8x8x8_A98", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1846.1982, 2620.8286, 2334.7988), (33.0523968819164, -134.55053449106447, 1.9412523560914934), (1.333276, 1.0, 1.276657), "PWM_Nordic_8x8x8_A99", _folder)
if a: placed += 1
else: skipped += 1

# Batch 31: StaticMesh'PWM_Quarry_1x1x1_A' (6 instances)
_mesh_path = "/Game/Unshippable/Whitebox/Rocks/Meshes/PWM_Quarry_1x1x1_A"
_materials = ['/Game/Environments/ProcTexturing/ProcMaterial_Quarry_Atlas_1']
_folder = "Reconstruction/BD_BB_Chapter5_BalrogsNest/Meshes"
a = spawn_static_mesh(_mesh_path, _materials, (9221.259, 5012.9805, 2702.4414), (-8.093904141733178, 125.71586122781643, -94.60815450450077), (4.3961635, 3.0956419, 4.4993563), "PWM_Quarry_1x1x1_A_13", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (8174.423, 8049.433, 2670.4658), (9.704046401501163, 52.88458796661005, -83.92547889272831), (4.396163, 3.9290967, 4.499356), "PWM_Quarry_1x1x1_A12", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (7299.089, 5851.6147, 3060.8457), (-24.863859240014374, -1.5089399294490864, 91.27485891284036), (4.396163, 2.132621, 4.499356), "PWM_Quarry_1x1x1_A13", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (9415.0, 5985.0, 4225.0), (0.0, -15.000058335092751, 0.0), (1.295086, 1.3975165, 1.0), "PWM_Quarry_1x1x1_A2_40", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (8740.0, 6665.0, 4280.0), (0.0, -60.000067159027765, 0.0), (1.6013838, 1.0, 1.0), "PWM_Quarry_1x1x1_A3_49", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (7993.0317, 5880.613, 3469.4138), (-4.411650551031731, -52.33834790950203, -121.89000420264018), (4.34716, 4.34716, 5.239051), "PWM_Quarry_1x1x1_A4", _folder)
if a: placed += 1
else: skipped += 1

# Batch 32: StaticMesh'PWM_Quarry_1X1x1_C' (111 instances)
_mesh_path = "/Game/Unshippable/Whitebox/Rocks/Meshes/PWM_Quarry_1X1x1_C"
_materials = ['/Game/Environments/ProcTexturing/ProcMaterial_Quarry_Atlas_1']
_folder = "Reconstruction/BD_BB_Chapter5_BalrogsNest/Meshes"
a = spawn_static_mesh(_mesh_path, _materials, (2644.043, 4649.5713, 822.8301), (5.065883079024897e-07, -90.000117038242, -86.86443520808702), (1.2410945, 1.2410945, 1.2410945), "PWM_Quarry_1X1x1_C_58", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1761.7275, 5935.1787, 853.4946), (-2.643969894443662e-06, 57.29950020113616, -82.45705987334512), (1.0, 1.0, 1.0), "PWM_Quarry_1X1x1_C10_82", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (10181.04, 9807.278, 1016.19226), (-2.6851798435524263, -34.67608676633314, 73.06484377442172), (3.253128, 3.253128, 3.758874), "PWM_Quarry_1X1x1_C100", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (10265.518, 9913.887, 1411.5774), (26.020168578640266, -130.24463414079668, 55.8827616039245), (1.628959, 1.628959, 2.134706), "PWM_Quarry_1X1x1_C101", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (10401.297, 9765.34, 1065.1345), (42.06225076705109, 53.604637746163945, 153.73011001857802), (1.399249, 1.399249, 1.904996), "PWM_Quarry_1X1x1_C102", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (10538.68, 9207.789, 1080.0403), (42.88974189178693, -153.95518858114565, -97.81949461449446), (2.231884, 2.114631, 2.73763), "PWM_Quarry_1X1x1_C103", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (10162.349, 10261.4, 1141.8132), (-40.761906320268636, 175.20789648698275, 36.667535687605564), (2.170884, 2.697615, 2.67663), "PWM_Quarry_1X1x1_C104", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (10242.399, 10124.834, 930.5863), (-40.751624252722934, -134.0295227239556, 36.24932842191211), (2.170884, 2.697615, 2.67663), "PWM_Quarry_1X1x1_C105", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (10699.662, 9156.269, 1660.9656), (-24.16882124416856, 3.147338462391568, 24.577882788701736), (3.253128, 4.079616, 3.758874), "PWM_Quarry_1X1x1_C106", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (10987.737, 8893.338, 1726.5168), (16.613397098909427, -81.54743145682407, -12.719727822659431), (1.935547, 1.935547, 2.441292), "PWM_Quarry_1X1x1_C107", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (10977.125, 8783.389, 839.9828), (-2.6851798435524263, -34.67608676633314, 73.06484377442172), (3.253128, 3.253128, 3.758874), "PWM_Quarry_1X1x1_C108", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (11025.757, 8855.431, 1294.0593), (18.86298860646328, -17.315551645201925, 8.950176623070723), (1.935547, 1.935547, 2.441292), "PWM_Quarry_1X1x1_C109", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3419.8965, 5730.1133, 793.6289), (-6.81616719217188e-07, -61.579432913677095, -42.77547930193938), (1.0, 1.0, 1.0), "PWM_Quarry_1X1x1_C11_176", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (11188.022, 8603.642, 1660.9656), (-24.16882124416856, 3.147338462391568, 24.577882788701736), (3.253128, 3.253128, 3.758874), "PWM_Quarry_1X1x1_C110", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (10339.271, 9909.221, 2021.0166), (40.56419902408286, -90.76651467885809, 25.621988645998876), (2.278283, 2.278283, 2.784029), "PWM_Quarry_1X1x1_C111", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (10748.947, 9163.551, 2002.5459), (16.613397098909427, -81.54743145682407, -12.719727822659431), (1.935547, 1.935547, 2.441292), "PWM_Quarry_1X1x1_C112", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (10994.953, 8885.178, 2002.5459), (16.613397098909427, -81.54743145682407, -12.719727822659431), (1.935547, 1.935547, 2.441292), "PWM_Quarry_1X1x1_C113", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (11272.699, 8325.414, 1255.1311), (40.19071709340615, -110.07144361415773, 7.906153644652432), (3.026615, 3.026615, 3.53236), "PWM_Quarry_1X1x1_C114", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (11299.38, 8541.756, 710.3617), (-2.6851798435524263, -34.67608676633314, 73.06484377442172), (3.253128, 3.253128, 3.758874), "PWM_Quarry_1X1x1_C115", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1622.9448, 2301.7393, 1169.4023), (4.376076620397147, 76.30874686270707, -98.6503577841889), (1.431943, 1.431943, 1.431943), "PWM_Quarry_1X1x1_C116", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (10707.247, 9889.33, 2021.0166), (40.56419902408286, -90.76651467885809, 25.621988645998876), (2.278283, 2.278283, 2.784029), "PWM_Quarry_1X1x1_C117", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (11031.071, 9641.95, 2021.0166), (40.56419902408286, -90.76651467885809, 25.621988645998876), (2.278283, 2.278283, 2.784029), "PWM_Quarry_1X1x1_C118", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (10975.606, 9330.727, 2021.0166), (40.56419902408286, -90.76651467885809, 25.621988645998876), (2.278283, 2.278283, 2.784029), "PWM_Quarry_1X1x1_C119", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2089.4795, 5769.241, 828.0508), (-4.4284994216029725, -110.25131366893231, -86.74200890349158), (1.0, 1.0, 1.0), "PWM_Quarry_1X1x1_C12", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (11249.683, 9108.78, 2021.0166), (40.56419902408286, -90.76651467885809, 25.621988645998876), (2.278283, 2.278283, 2.784029), "PWM_Quarry_1X1x1_C120", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4595.9272, 6158.913, 790.4314), (-4.548949086166298, 2.375135074902558, -159.84181774852635), (0.46320692, 0.46320692, 0.46320692), "PWM_Quarry_1X1x1_C121", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (7648.1846, 5166.416, 997.8698), (-6.1509878600746e-05, 51.70903902383175, 81.87391248312561), (1.2697437, 1.0, 1.0), "PWM_Quarry_1X1x1_C122", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (7957.2383, 5324.269, 2370.4307), (0.0, 0.0, 179.99988388675877), (1.0, 1.0, 1.0), "PWM_Quarry_1X1x1_C123", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (8072.2383, 5324.269, 2370.4307), (-36.562493629959334, 7.445865032766448e-12, 179.99988388675126), (1.0, 1.0, 1.0), "PWM_Quarry_1X1x1_C124", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (8667.461, 7076.219, 2491.8516), (21.53807797384793, 82.72872203343944, 103.36502588845624), (1.27746, 1.27746, 1.27746), "PWM_Quarry_1X1x1_C125", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (8692.461, 7196.219, 2486.8516), (21.538110330736217, -29.77114386520978, 103.36505718411323), (1.27746, 1.27746, 1.27746), "PWM_Quarry_1X1x1_C126", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (8621.012, 5945.464, 2579.8306), (6.484922939091876, -73.38419256617752, -0.7717588703710914), (1.8935435, 1.8935435, 1.8935435), "PWM_Quarry_1X1x1_C127_216", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (7581.8433, 5052.32, 995.21063), (-0.8410989923224844, 45.80749237089245, 81.91744911880448), (1.0, 1.0, 1.0), "PWM_Quarry_1X1x1_C129", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5098.982, 7186.6016, 1122.4438), (-2.137495027384996e-06, 92.49074060117339, -80.03234229678013), (1.431943, 1.855875, 2.1332772), "PWM_Quarry_1X1x1_C13", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2889.5127, 5604.92, 779.37994), (-6.682799507285378, 37.48631212371571, -148.38932739243833), (0.71612, 0.71612, 0.71612), "PWM_Quarry_1X1x1_C14_234", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4694.59, 6155.166, 784.791), (-6.682799507285378, 37.48631212371571, -148.38932739243833), (0.71612, 0.71612, 0.71612), "PWM_Quarry_1X1x1_C15", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4637.5723, 6048.3267, 774.15405), (-16.71935846062832, 131.66391003085505, -94.11047398205858), (1.0816582, 0.58966535, 1.0321525), "PWM_Quarry_1X1x1_C16", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (10296.65, 9534.613, 800.0), (0.11710345612974574, -144.26537020625707, -90.62636986176277), (1.0, 0.92726254, 1.0), "PWM_Quarry_1X1x1_C17_409", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4515.2617, 5050.713, 1006.6211), (-7.728826440781988, -60.423732732560296, -101.35431908510786), (2.148626, 2.035947, 2.148626), "PWM_Quarry_1X1x1_C18_338", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (7789.7383, 6785.433, 862.0244), (0.0, -90.0001164887758, 0.0), (1.0, 1.0, 1.0), "PWM_Quarry_1X1x1_C19_269", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2116.1992, 4852.717, 778.1958), (-24.821509541066682, -91.45198098118388, -86.54481885369887), (1.241094, 1.241094, 1.241094), "PWM_Quarry_1X1x1_C2", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (6412.167, 6961.63, 891.5371), (-3.7116992542514216, -179.21680331406012, 82.09564439146315), (2.057999, 2.057999, 2.057999), "PWM_Quarry_1X1x1_C20_285", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (8900.532, 7515.575, 3042.708), (7.895622840862, -160.3272022462693, 135.23955148165476), (3.3056583, 3.034287, 3.3056583), "PWM_Quarry_1X1x1_C21", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5948.4976, 7168.034, 1023.1494), (2.0218605099613574, 45.548037854099704, 94.27564632855837), (2.057999, 2.188492, 2.057999), "PWM_Quarry_1X1x1_C22", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (10001.886, 9351.196, 786.3965), (0.11712673603171037, -144.2654002068881, -90.6263619485573), (1.0, 0.927263, 1.0), "PWM_Quarry_1X1x1_C23", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (8198.857, 7339.012, 2724.9526), (15.575068724755784, -152.20563102229522, 121.57858267717252), (4.1948338, 3.9234626, 4.1948338), "PWM_Quarry_1X1x1_C24", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (7829.6396, 6806.2896, 2808.1104), (-5.034578189723927, 44.12109701344052, 55.468683959780485), (4.194834, 3.923463, 4.194834), "PWM_Quarry_1X1x1_C25", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (7423.791, 5746.1885, 2671.1406), (17.872061305254057, 128.12847050893612, 158.07622521086935), (6.4790363, 3.034287, 3.305658), "PWM_Quarry_1X1x1_C26", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (6144.6035, 7254.1367, 1165.6406), (6.925091466744917, -73.84820954264327, 72.1023891434005), (2.0579987, 2.601405, 2.0579987), "PWM_Quarry_1X1x1_C27_72", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (6240.205, 5055.008, 982.9912), (-7.728826440781988, -60.423732732560296, -101.35431908510786), (2.697563, 2.425606, 2.697563), "PWM_Quarry_1X1x1_C28_347", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4462.4863, 6549.207, 925.4629), (-7.728757823177622, 153.6129596119353, -101.35447948054032), (2.697563, 2.425606, 2.697563), "PWM_Quarry_1X1x1_C29", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3298.8652, 5193.7646, 803.39404), (-6.6156292923621605, -19.66002906549534, -114.20814993645098), (1.241094, 1.241094, 1.241094), "PWM_Quarry_1X1x1_C3", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (6501.2983, 6540.0864, 800.0), (-6.682615232108829, 37.48609778015826, -62.97619239934419), (0.71612, 0.71612, 0.71612), "PWM_Quarry_1X1x1_C30", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3401.9043, 5848.777, 805.89746), (19.892982158772426, -67.85994830132356, -107.92156293761414), (1.0, 1.0, 1.0), "PWM_Quarry_1X1x1_C31", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (6040.288, 5126.124, 880.22754), (-2.8580635041820024, 165.1996930390777, -76.58828999972873), (2.697563, 2.425606, 2.697563), "PWM_Quarry_1X1x1_C32", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (6064.8955, 5063.8037, 1091.4668), (1.2916744722963252e-05, -90.00002586260021, -99.44682930632291), (1.0, 1.0, 1.0), "PWM_Quarry_1X1x1_C33_157", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (6001.9004, 5514.2427, 799.46094), (-6.682554818160123, 152.766019586513, -62.97633611256351), (0.71612, 0.71612, 0.71612), "PWM_Quarry_1X1x1_C34_206", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (6087.2983, 4950.3916, 1043.7744), (-3.405273084244796, 12.660491715929112, -90.7644089713935), (1.631318, 1.184456, 1.631318), "PWM_Quarry_1X1x1_C35", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (6393.3726, 4859.1675, 925.71875), (-7.930574397736016, -158.22736162642158, -93.15419038455374), (2.1403773, 2.1403773, 2.1403773), "PWM_Quarry_1X1x1_C36_165", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1322.8855, 4900.2124, 799.98804), (-14.150388432935662, 17.342748830087505, -94.12563738919701), (0.71612, 0.56970125, 0.71612), "PWM_Quarry_1X1x1_C37", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (7127.087, 6133.51, 2812.5557), (-3.2095938087046165, 86.85827566616351, 99.773006547882), (5.316176, 3.034287, 3.305658), "PWM_Quarry_1X1x1_C38", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (6395.759, 5977.2407, 2838.6914), (-10.281675248473, 158.93164429970096, 89.98562135468718), (5.316176, 3.034287, 3.305658), "PWM_Quarry_1X1x1_C39", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3180.21, 5241.496, 782.86914), (-6.682799324873365, 83.39156527163098, -148.38987221215274), (0.71611965, 0.71611965, 0.71611965), "PWM_Quarry_1X1x1_C4", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (10726.439, 9705.144, 2766.5864), (6.03319468957689, 95.69580513034578, -179.9388628773608), (2.5399132, 2.5399132, 2.5399132), "PWM_Quarry_1X1x1_C40_341", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (8045.508, 7106.4673, 2639.5322), (7.381583500188862, 114.05179333383306, 88.97573319289496), (4.194834, 3.5875309, 4.194834), "PWM_Quarry_1X1x1_C41", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5617.9536, 6160.6123, 779.51465), (-7.992834006573643e-07, -29.796746753373892, -63.777027464393036), (1.0, 0.6918229, 1.0), "PWM_Quarry_1X1x1_C42_302", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3803.963, 5809.176, 786.3364), (20.25767170750001, -23.70227190577624, -75.97765777457262), (1.0, 0.691823, 1.0), "PWM_Quarry_1X1x1_C43", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3558.6992, 5770.033, 818.06836), (2.352483856543421, 80.87131023406603, -69.38181339481406), (1.0, 0.691823, 1.0), "PWM_Quarry_1X1x1_C44", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (8846.773, 7750.087, 2634.476), (-4.816284390119072, 8.619324193445648, 110.13690170181911), (5.316176, 3.034287, 3.305658), "PWM_Quarry_1X1x1_C45", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (7430.908, 6187.9824, 2817.0098), (0.14943808897130867, -128.82469870995337, 124.85146428955724), (4.194834, 3.923463, 4.194834), "PWM_Quarry_1X1x1_C46", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (9060.388, 8671.786, 796.7544), (0.0, -90.0001164887758, 0.0), (1.0, 1.0, 1.0), "PWM_Quarry_1X1x1_C47_50", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (8046.391, 5662.883, 3217.8782), (-13.225678669157803, -69.29128907321805, 31.182214541598473), (3.4648108, 3.4648108, 3.970557), "PWM_Quarry_1X1x1_C48_2", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (676.5935, 1821.2307, 774.90546), (0.24759324808469285, -118.98039952085888, -64.9566247611045), (1.0, 1.0, 1.0), "PWM_Quarry_1X1x1_C49", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2508.6748, 5079.457, 787.7549), (0.24759467387605333, -173.79675033637935, -64.95642048184467), (1.0, 1.0, 1.0), "PWM_Quarry_1X1x1_C5", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (10714.734, 9005.429, 700.42566), (20.225050599783295, -57.44677451215553, 43.12143569422251), (3.464811, 3.464811, 3.970557), "PWM_Quarry_1X1x1_C50", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (9656.401, 5803.1245, 3245.4268), (-13.225556438070006, -69.29131607706742, 128.56208433979103), (3.464811, 3.464811, 3.970557), "PWM_Quarry_1X1x1_C51", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (8044.836, 6320.395, 3487.1445), (-15.462067722679695, -30.19476726421853, 24.602373210438767), (3.464811, 3.464811, 3.970557), "PWM_Quarry_1X1x1_C52", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (890.42676, 1829.0592, 803.9166), (-6.615630185910009, 60.483224775116774, -114.20777977248511), (1.241094, 1.241094, 1.241094), "PWM_Quarry_1X1x1_C53", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (9888.376, 6530.5044, 3130.0427), (-20.02557673776151, -40.888188415785805, 168.421679230238), (7.4411116, 3.464811, 5.9221454), "PWM_Quarry_1X1x1_C54", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (7386.583, 6675.068, 863.3253), (0.0, -108.68481265458037, 0.0), (1.545608, 1.545608, 1.545608), "PWM_Quarry_1X1x1_C55", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (6294.555, 6949.053, 804.7494), (-4.7700189096028165, 172.85302932556897, 82.6828477693786), (2.057999, 2.057999, 2.057999), "PWM_Quarry_1X1x1_C56", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (7920.1523, 7875.124, 934.1533), (56.588842420683704, -11.448056746544202, 56.00151602262345), (3.464811, 3.464811, 3.970557), "PWM_Quarry_1X1x1_C57", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (7536.583, 6675.068, 963.3253), (0.0, -108.68481265458037, 0.0), (1.545608, 1.545608, 1.545608), "PWM_Quarry_1X1x1_C58", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (7686.583, 6675.068, 963.3253), (0.0, 156.31542089882274, -0.0), (1.545608, 1.545608, 1.545608), "PWM_Quarry_1X1x1_C59", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1940.6172, 4240.2334, 1168.8579), (1.920905178950702e-06, -90.00015867061897, -80.03464481795169), (1.431943, 1.431943, 1.431943), "PWM_Quarry_1X1x1_C6_116", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1622.9443, 4118.574, 1169.4023), (4.376076620397147, 76.30874686270707, -98.6503577841889), (1.431943, 1.431943, 1.431943), "PWM_Quarry_1X1x1_C7", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (9691.321, 6821.2783, 2931.9277), (34.94291104067493, -59.07924224261054, 108.08911651842206), (1.3574674, 1.3574674, 1.8632131), "PWM_Quarry_1X1x1_C74", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (9590.391, 5793.037, 2786.3022), (1.1166746776215777, -69.38213205475637, 104.74822599022097), (1.357467, 1.357467, 1.863213), "PWM_Quarry_1X1x1_C75", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (9268.312, 7208.758, 2995.3462), (-28.403960002800567, -179.61948906684955, 54.133842024955754), (1.935547, 1.935547, 2.441292), "PWM_Quarry_1X1x1_C78_55", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (8653.743, 7125.6387, 2876.121), (-28.40386965989892, 69.92844052759442, 54.13381788409868), (1.935547, 1.935547, 2.441292), "PWM_Quarry_1X1x1_C79_57", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1843.377, 6288.2954, 1168.8579), (-1.1449585162270691e-06, 78.2918665544649, -80.0333517141794), (1.431943, 1.431943, 1.431943), "PWM_Quarry_1X1x1_C8", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (8476.207, 6981.185, 2918.6538), (-14.979762899849739, 139.94035994578567, 29.2737601103981), (1.9700799, 2.496809, 2.4758244), "PWM_Quarry_1X1x1_C80", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (9341.779, 7125.5234, 3228.3948), (-30.024862151021978, -177.78622429213064, -176.4238003306982), (3.253128, 3.253128, 3.758874), "PWM_Quarry_1X1x1_C81", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (8686.719, 7073.9307, 3068.8513), (44.99872554479532, 80.92333524890854, 170.20102268092825), (2.170884, 2.697615, 2.67663), "PWM_Quarry_1X1x1_C82", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (9012.084, 7284.8306, 3080.7974), (-25.0224669002641, 51.02014090813622, 65.44597820360079), (2.170884, 2.697615, 2.67663), "PWM_Quarry_1X1x1_C84", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (9069.064, 5619.744, 2994.1597), (49.42889496559914, 112.89234658114438, 161.69640476910413), (2.303954, 2.830686, 2.809701), "PWM_Quarry_1X1x1_C85", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (10447.499, 9441.612, 1660.9656), (-24.16882124416856, 3.147338462391568, 24.577882788701736), (3.253128, 3.253128, 3.758874), "PWM_Quarry_1X1x1_C86", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (10544.765, 9339.77, 773.474), (-14.947478260342349, 160.25207080888276, -122.20702370187149), (2.303954, 2.830686, 2.809701), "PWM_Quarry_1X1x1_C87", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (10295.057, 10295.177, 1810.9185), (-40.761906320268636, 175.20789648698275, 36.667535687605564), (3.464811, 3.991542, 3.970557), "PWM_Quarry_1X1x1_C88", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (9841.701, 10259.747, 1474.7893), (-87.39992817686759, 159.85671936721872, 157.66573163667314), (3.464811, 3.991542, 3.970557), "PWM_Quarry_1X1x1_C89", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2179.129, 6342.96, 1169.4023), (4.376073560640142, -115.3993710714303, -98.65051718050387), (1.431943, 1.431943, 1.431943), "PWM_Quarry_1X1x1_C9", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (10572.044, 9118.277, 1438.9465), (40.19071709340615, -110.07144361415773, 7.906153644652432), (3.026615, 3.026615, 3.53236), "PWM_Quarry_1X1x1_C90", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (10763.71, 9154.276, 1085.5911), (-14.947266110212533, 160.25318119286945, 114.01351088690197), (2.303954, 2.830686, 2.809701), "PWM_Quarry_1X1x1_C91", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (11037.209, 9128.549, 1496.7322), (9.033825603710609, -108.54378422303817, -18.823150323116387), (1.686001, 1.686001, 2.191747), "PWM_Quarry_1X1x1_C92", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (10157.124, 9624.395, 1508.967), (20.225159662792823, -57.44655822669801, 61.905805178290684), (2.231884, 1.538829, 2.73763), "PWM_Quarry_1X1x1_C93", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (10331.722, 9494.873, 951.2665), (57.609198277500866, 6.823854035981472, 12.006788488262835), (3.253128, 3.253128, 3.758874), "PWM_Quarry_1X1x1_C94", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (10634.736, 9574.877, 2021.0166), (40.56419902408286, -90.76651467885809, 25.621988645998876), (2.278283, 2.278283, 2.784029), "PWM_Quarry_1X1x1_C95", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (10425.58, 9534.598, 1294.0593), (18.86298860646328, -17.315551645201925, 8.950176623070723), (1.935547, 1.935547, 2.441292), "PWM_Quarry_1X1x1_C96", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (10243.386, 9735.649, 1726.5168), (16.613397098909427, -81.54743145682407, -12.719727822659431), (1.935547, 1.935547, 2.441292), "PWM_Quarry_1X1x1_C97", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (10204.1045, 9972.577, 1647.4436), (-19.713195962840793, 22.456058127282894, -108.50123538502552), (1.935547, 1.935547, 2.441292), "PWM_Quarry_1X1x1_C98", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (10277.7, 10161.319, 1437.9373), (5.4451422742920625, -42.91708822563576, -33.34338448055825), (1.935547, 1.935547, 2.441292), "PWM_Quarry_1X1x1_C99", _folder)
if a: placed += 1
else: skipped += 1

# Batch 33: StaticMesh'PWM_Quarry_2x2x2_A' (98 instances)
_mesh_path = "/Game/Unshippable/Whitebox/Rocks/Meshes/PWM_Quarry_2x2x2_A"
_materials = ['/Game/Environments/ProcTexturing/ProcMaterial_Quarry_Atlas_1']
_folder = "Reconstruction/BD_BB_Chapter5_BalrogsNest/Meshes"
a = spawn_static_mesh(_mesh_path, _materials, (1778.4004, 3997.5273, 1183.5718), (-2.0503539224590037, -9.261382033954098, -3.0309448362108276), (1.5625062, 1.5625062, 1.5625062), "PWM_Quarry_2x2x2_A_108", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2759.2842, 6069.773, 851.7617), (-3.503784767317535, 171.83789796734507, -9.955934089470862), (1.0, 1.267181, 1.0), "PWM_Quarry_2x2x2_A10", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (8101.1426, 7296.4243, 2569.1426), (-0.8114622531227665, -177.95554030798183, -2.072936580409981), (1.5, 1.5, 1.0), "PWM_Quarry_2x2x2_A102", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (8701.143, 7296.4243, 2569.1426), (-0.8114622531227665, -177.95554030798183, -2.072936580409981), (1.5, 1.5, 1.0), "PWM_Quarry_2x2x2_A103", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (9844.757, 6555.6953, 3808.5059), (-1.2659303014724186, -100.55016501133578, 178.2477969586106), (2.20565, 2.20565, 2.605348), "PWM_Quarry_2x2x2_A104", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (9754.078, 7120.398, 2875.8877), (2.160982765195657, 24.109232918008438, 179.95554913421097), (2.20565, 2.20565, 3.0986392), "PWM_Quarry_2x2x2_A105", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3547.1094, 6646.0674, 1148.0376), (-5.989623795358364, 102.7482872121782, -4.782196125045043), (1.562506, 1.562506, 1.562506), "PWM_Quarry_2x2x2_A11", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (11587.6875, 7241.704, 1504.2825), (-5.930939642833122, 17.510317187022707, -4.132996149583533), (3.4375, 1.562506, 1.562506), "PWM_Quarry_2x2x2_A111", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (12333.166, 6436.1914, 1311.0309), (-18.079346681664127, 10.91928103770328, 7.5847305816254025), (3.4375, 1.562506, 1.562506), "PWM_Quarry_2x2x2_A112", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (12333.166, 7098.6772, 841.83075), (-18.079346681664127, 10.91928103770328, 7.5847305816254025), (3.4375, 1.562506, 1.562506), "PWM_Quarry_2x2x2_A113", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (12333.166, 6952.5073, 1563.177), (-5.062805221542778, 2.763488783167214, -104.49020492918994), (3.4375, 1.562506, 1.562506), "PWM_Quarry_2x2x2_A114", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (13263.755, 7339.9873, 1254.4238), (-5.930939642833122, 17.510317187022707, -4.132996149583533), (3.4375, 1.562506, 1.562506), "PWM_Quarry_2x2x2_A115", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5250.503, 7436.121, 1184.4673), (-2.0503542362756555, 173.22999495520912, -3.030944659636078), (1.562506, 1.562506, 1.562506), "PWM_Quarry_2x2x2_A12", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5242.7363, 7465.341, 1618.0835), (2.2029960641650903, 152.51756662950316, -179.55807895190426), (2.071208, 2.071208, 2.071208), "PWM_Quarry_2x2x2_A13", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4067.3828, 6999.5674, 1410.5186), (2.1105588109303746, 110.89773904216787, 175.16220070787645), (2.071208, 2.7378907, 2.071208), "PWM_Quarry_2x2x2_A14", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4196.7246, 6730.496, 1835.3159), (0.6052501739839913, 54.75215628480289, 179.30457294986542), (2.071208, 2.071208, 2.281443), "PWM_Quarry_2x2x2_A15", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5491.1875, 7302.092, 1071.5972), (0.9604746296277655, 152.17420687637346, -3.21377482759804), (1.562506, 1.562506, 1.562506), "PWM_Quarry_2x2x2_A16", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5517.79, 7453.4316, 1422.935), (1.32348735376526, 65.61722699459877, 177.01414630295338), (2.071208, 2.071208, 2.071208), "PWM_Quarry_2x2x2_A17", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3269.2598, 4943.7617, 796.646), (-3.1205440459315104, -130.10694935288856, 11.575758742321279), (1.2142222, 1.3536845, 1.0), "PWM_Quarry_2x2x2_A18_232", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5943.1616, 7383.2393, 1148.0376), (-5.9895319274948955, 92.809619897663, -4.782196253686274), (1.562506, 1.562506, 1.562506), "PWM_Quarry_2x2x2_A19", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1778.4004, 3936.662, 1513.2949), (2.2029955810923, -29.973331201146266, -179.55807888363563), (1.562506, 1.562506, 1.562506), "PWM_Quarry_2x2x2_A2", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (6769.5, 7317.141, 2349.4849), (0.8915381007320852, 81.81390195210739, 179.76522568991135), (2.071208, 2.071208, 2.071208), "PWM_Quarry_2x2x2_A20_49", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (7166.396, 4321.11, 1304.6206), (0.0, -37.76818683591426, 0.0), (1.90572, 1.90572, 1.90572), "PWM_Quarry_2x2x2_A21_284", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5532.2407, 7035.95, 830.63184), (0.0, 163.31342888233846, -0.0), (1.0, 1.0, 1.0), "PWM_Quarry_2x2x2_A22_77", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (6792.7954, 6979.149, 800.53076), (0.0, 24.96972901041612, -0.0), (1.0, 1.0, 1.0), "PWM_Quarry_2x2x2_A23_67", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (6051.408, 4225.3623, 1498.106), (3.663528456495996, -83.6692031082886, 175.63633897186855), (2.071208, 2.737891, 2.071208), "PWM_Quarry_2x2x2_A24", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5962.3364, 4407.6445, 1851.0913), (2.5089060376307466, -105.63744633604139, 179.62406571802956), (2.071208, 2.071208, 2.071208), "PWM_Quarry_2x2x2_A25", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4596.123, 4284.324, 1192.1909), (1.8149722727026967, -42.3861098062513, -1.8327942728075952), (1.562506, 1.562506, 1.562506), "PWM_Quarry_2x2x2_A26", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4553.573, 4139.3, 1576.5142), (2.7524701225687322, -129.00355989797197, 176.2428041098589), (2.071208, 2.071208, 2.071208), "PWM_Quarry_2x2x2_A27", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4784.504, 4235.4717, 2022.6343), (1.7348064536953374, 6.135924628719878, -178.0024781893358), (2.071208, 2.071208, 2.071208), "PWM_Quarry_2x2x2_A28", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4138.125, 4319.4717, 1242.9175), (-4.366088376580822, -101.78179143368551, -4.814513911339077), (1.562506, 1.562506, 1.562506), "PWM_Quarry_2x2x2_A29", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2598.167, 5932.67, 805.58984), (16.558413838303807, -89.06503736457307, 0.5295570929721339), (1.0, 1.2671806, 1.0), "PWM_Quarry_2x2x2_A3_66", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4256.843, 4882.823, 901.5591), (0.5720420054212353, -31.271028381406744, 1.5195298126144767), (1.0, 1.0, 1.1730368), "PWM_Quarry_2x2x2_A30", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4669.5254, 6785.7734, 817.7988), (-6.319732078339528, 114.63527153775877, 1.596747243747084), (1.6645108, 1.4961472, 1.0), "PWM_Quarry_2x2x2_A31", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5570.352, 5228.816, 828.7969), (0.41149159241900524, -43.3227250001107, -0.3880310130772674), (1.0, 1.0, 0.71779764), "PWM_Quarry_2x2x2_A32_250", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4676.5376, 4964.2773, 913.8148), (-0.8400572961644702, -17.228513605195538, -1.0556334935843281), (1.6485482, 1.6485482, 1.8215853), "PWM_Quarry_2x2x2_A33", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (7321.1924, 4917.1143, 931.73486), (-5.056091813963628, -23.352052865193087, -0.059356624041995494), (1.3848755, 1.373705, 1.3388336), "PWM_Quarry_2x2x2_A34_148", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (8623.405, 4454.6675, 879.39307), (0.0, -86.0203302272978, 0.0), (1.5061644, 1.5061644, 1.5061644), "PWM_Quarry_2x2x2_A35_19", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (11326.385, 6375.625, 1033.5548), (-5.930939642833122, 17.510317187022707, -4.132996149583533), (1.562506, 1.562506, 1.562506), "PWM_Quarry_2x2x2_A36", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (7609.7373, 5346.091, 892.87256), (-6.445587070671882, -21.782894984623702, 1.3863979445093417), (1.0, 1.0, 1.0), "PWM_Quarry_2x2x2_A37", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (8179.0044, 4284.919, 1855.8418), (3.5042216916636995, -112.1656353284392, -179.93675930019387), (2.071208, 2.071208, 2.365489), "PWM_Quarry_2x2x2_A38", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5987.4385, 6941.6226, 776.8799), (8.218005887877549, 117.27727574411834, 1.347846942413334), (1.664511, 1.496147, 1.0), "PWM_Quarry_2x2x2_A39", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2051.4688, 6493.034, 1183.5718), (-2.0503538669408665, 159.03123695678724, -3.030944491291132), (1.562506, 1.562506, 1.562506), "PWM_Quarry_2x2x2_A4", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (6671.966, 5313.509, 814.7539), (-0.5112609732804445, -9.156921411829872, -0.4673156242410683), (1.384876, 1.373705, 0.829874), "PWM_Quarry_2x2x2_A40", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4345.9043, 5025.686, 914.8154), (0.5720420291771112, 0.1717147747650794, 1.5195295109819074), (1.0, 1.0, 1.173037), "PWM_Quarry_2x2x2_A41_208", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1073.3027, 5861.1978, 832.42285), (0.0, -90.0001164887758, 0.0), (1.0, 1.0, 1.0), "PWM_Quarry_2x2x2_A42_397", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (7171.2515, 5303.26, 783.45996), (-3.8005979937969183, 27.75961244050076, -3.0124510931632384), (1.0, 1.0, 1.0), "PWM_Quarry_2x2x2_A43", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (7528.2563, 5398.062, 779.5674), (3.6967722907262717, 132.5060197305316, -0.8783264232146829), (1.0, 1.0, 1.2125452), "PWM_Quarry_2x2x2_A44", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (7121.117, 5462.255, 697.6006), (-1.772735436358617, -132.64166635426702, -0.4978332360881875), (1.0, 1.0, 1.0), "PWM_Quarry_2x2x2_A45", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (7889.143, 8805.855, 883.0205), (-12.705108013532525, 136.69839716396226, -5.698394961098839), (1.562506, 1.562506, 1.562506), "PWM_Quarry_2x2x2_A46", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (7896.1895, 8836.878, 1645.1445), (0.3003857528505701, -119.18856565911008, 179.65030736531256), (2.071208, 1.3627095, 2.291073), "PWM_Quarry_2x2x2_A47", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (7201.964, 7556.7764, 2480.5781), (0.8915381007320852, 81.81390195210739, 179.76522568991135), (2.071208, 2.071208, 2.071208), "PWM_Quarry_2x2x2_A48_539", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (6998.9487, 7507.8784, 1977.2856), (-0.7636413323181755, -49.37200612528408, 179.48350614296595), (2.071208, 2.071208, 2.5713587), "PWM_Quarry_2x2x2_A49", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2063.8213, 6573.5176, 1599.5898), (2.20299640174581, 138.3182701052116, -179.55807901090407), (2.0712075, 2.0712075, 2.0712075), "PWM_Quarry_2x2x2_A5", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (6926.3633, 5307.308, 812.4429), (-5.039123154036979, -52.701747888311814, 4.255930147379661), (1.0, 1.0, 1.0), "PWM_Quarry_2x2x2_A50", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (10281.56, 10466.106, 1882.2549), (2.508905654320032, 68.96514955209389, 179.6240654860728), (2.071208, 2.071208, 2.071208), "PWM_Quarry_2x2x2_A51", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (7155.297, 4710.4087, 981.6167), (2.3426998501091614, 48.29284176477213, -1.8272398944957458), (2.1154644, 1.7045718, 1.6374981), "PWM_Quarry_2x2x2_A52_163", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4707.835, 4712.9517, 913.52783), (-2.9610593639775944, -164.52445220019055, 5.760109097153992), (1.648548, 1.648548, 1.821585), "PWM_Quarry_2x2x2_A53", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4469.8174, 4648.1777, 1205.9346), (-2.9610593726539665, -164.52445236833688, 5.76011339606801), (1.0, 1.0, 1.0), "PWM_Quarry_2x2x2_A54", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4459.865, 4494.3486, 1300.4233), (-2.9610590159345156, -99.87093447670063, 5.760216662864643), (1.1333579, 1.1938589, 1.0), "PWM_Quarry_2x2x2_A55", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (7258.8184, 5518.837, 786.5862), (-5.390563497093022, -44.880647775961705, 3.8004543018505097), (1.0, 1.0, 1.0), "PWM_Quarry_2x2x2_A56", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (10343.8125, 8436.559, 848.1714), (-8.41094899164334, -17.433836003685958, 0.5742117219945998), (1.0, 1.0, 1.0), "PWM_Quarry_2x2x2_A57", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (7672.746, 6894.9697, 859.2717), (-3.063079535858427, 8.956664994237693, -0.9409484732302319), (1.0, 1.0, 1.0), "PWM_Quarry_2x2x2_A58", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (7628.259, 7016.5317, 958.41504), (-1.6424864410481546, -54.874778241632306, 1.5468452126728394), (1.0, 1.0, 1.0), "PWM_Quarry_2x2x2_A59", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (915.29297, 6289.6865, 1431.4277), (2.202996388140208, 74.89807817621207, -179.55807886512332), (2.071208, 2.071208, 2.071208), "PWM_Quarry_2x2x2_A6", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (7528.5527, 6809.1226, 725.3291), (-2.4424133717371097, 13.105592442777343, -2.911498725660231), (1.0, 1.0, 1.212545), "PWM_Quarry_2x2x2_A60_156", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (7553.298, 6792.6157, 713.7636), (-2.2231450904337606, -160.21322392900137, 0.11003480162053891), (1.0, 1.0, 1.212545), "PWM_Quarry_2x2x2_A61_158", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (7650.8677, 5327.217, 976.3034), (-1.551300179728104, -35.53726022451292, 12.02198872853997), (0.78226304, 0.9337353, 0.78226304), "PWM_Quarry_2x2x2_A62", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (7381.4995, 4557.834, 1119.0459), (-2.2986454620526966, -133.06580430739345, 1.882208358408134), (1.886847, 1.704572, 1.9844761), "PWM_Quarry_2x2x2_A63", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (6669.452, 4936.391, 859.0532), (-0.5111694160115181, -57.46682012688166, -0.46731563221228134), (1.7967818, 1.6068491, 0.829874), "PWM_Quarry_2x2x2_A64", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5202.595, 5215.442, 786.5054), (-0.8510132455910283, 178.2021249481834, -174.85565249836594), (1.0, 0.48542964, 1.0), "PWM_Quarry_2x2x2_A65_25", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1778.4009, 2180.6934, 1183.5718), (-2.0503539224590037, -9.261382033954098, -3.0309448362108276), (1.562506, 1.562506, 1.562506), "PWM_Quarry_2x2x2_A66", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1778.4009, 2119.8281, 1513.2949), (2.2029960537583424, -29.973331203999425, -179.55807889151177), (1.562506, 1.562506, 1.562506), "PWM_Quarry_2x2x2_A67", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2138.046, 4053.9697, 1431.4277), (2.202996388140208, 74.89807817621207, -179.55807886512332), (2.071208, 2.071208, 3.4918997), "PWM_Quarry_2x2x2_A68", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1778.4004, 2799.752, 1085.2852), (2.2029962982667213, -65.00457431851387, -179.55807886698886), (1.562506, 1.562506, 1.562506), "PWM_Quarry_2x2x2_A69", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3116.2275, 6486.3994, 1095.0728), (0.9604747553879995, 162.10977584192614, -3.2137753934636466), (1.562506, 1.562506, 1.562506), "PWM_Quarry_2x2x2_A7", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (9105.0, 5670.0, 4245.0), (0.0, 0.0, -0.0), (1.5198791, 1.0, 1.0), "PWM_Quarry_2x2x2_A70_43", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (8550.0, 6800.0, 4235.0), (0.0, 0.0, -0.0), (1.5104642, 1.3067155, 1.0), "PWM_Quarry_2x2x2_A71_46", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (9420.0, 6750.0, 4295.0), (0.0, 65.00006093247498, -0.0), (1.1799679, 0.61740613, 1.0), "PWM_Quarry_2x2x2_A72_52", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1526.182, 1130.6934, 1183.5718), (-2.0503539224590037, -9.261382033954098, -3.0309448362108276), (1.562506, 1.562506, 1.562506), "PWM_Quarry_2x2x2_A73", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (8260.53, 6423.5503, 3388.0688), (-0.382141073132899, -74.89443567750699, 5.002257978990793), (1.0, 1.0, 1.3996984), "PWM_Quarry_2x2x2_A77_173", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (8303.0205, 6863.5737, 2550.8784), (-0.8116455278749566, -76.7048087405473, -2.072875906755058), (1.0, 1.0, 1.0), "PWM_Quarry_2x2x2_A78", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3092.0977, 6646.6147, 1478.6592), (1.3234866547403434, 75.55355723070069, 177.0141457132518), (2.071208, 2.071208, 2.071208), "PWM_Quarry_2x2x2_A8", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (223.90613, 5826.715, 768.712), (9.142509329863378, -160.88474123252948, 1.2315315721594923e-05), (1.0, 1.0, 1.0), "PWM_Quarry_2x2x2_A82", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (7361.6743, 5416.8765, 777.9311), (-6.59204017164847, -9.048307908415564, -0.06527709437230217), (1.0, 1.0, 1.0), "PWM_Quarry_2x2x2_A85", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (9051.143, 5847.4243, 2559.1426), (0.8113648484714492, 26.079464325596057, 177.92684917923162), (1.0, 1.0, 1.0), "PWM_Quarry_2x2x2_A86", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (8721.143, 5746.4243, 2559.1426), (0.811365028159852, 107.64233022484173, 177.92684904227323), (1.0, 1.0, 1.0), "PWM_Quarry_2x2x2_A87", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (7602.4, 7150.2607, 873.1678), (-1.6424863311808373, -54.874778225292346, 1.5468446775976268), (1.3521212, 1.3521212, 1.3521212), "PWM_Quarry_2x2x2_A88", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2918.9004, 6475.5566, 1928.4873), (2.2029957756002, -149.39005808233864, -179.5580787876589), (2.071208, 2.071208, 2.071208), "PWM_Quarry_2x2x2_A9", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (7483.28, 7117.815, 964.1014), (-1.6424863311808373, -54.874778225292346, 1.5468446775976268), (1.0, 1.0, 1.0), "PWM_Quarry_2x2x2_A91", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (8351.143, 7106.4243, 2569.1426), (0.8113649654160494, -41.41973535527789, 177.92684939935242), (1.5, 1.5, 1.0), "PWM_Quarry_2x2x2_A92", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (8455.364, 6037.2544, 3915.1426), (-2.0072633718528787, -176.4950062169598, -179.19808136199313), (1.0, 1.0, 1.399698), "PWM_Quarry_2x2x2_A93", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (8111.1426, 7699.4243, 2569.1426), (-0.8114317764683512, -82.33031234097443, -2.0729366157235996), (1.5, 1.5, 1.0), "PWM_Quarry_2x2x2_A94", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (8121.1426, 7874.4243, 2569.1426), (-0.8114318113231755, 169.85712623598397, -2.0729369265658524), (1.5, 1.5, 1.0), "PWM_Quarry_2x2x2_A95", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (8674.336, 5790.9653, 3904.8335), (-0.5543823984663705, 130.14697359905563, -177.91058425340856), (1.0, 1.0, 1.399698), "PWM_Quarry_2x2x2_A96", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (8931.143, 5706.4243, 2559.1426), (-0.8114318383217447, -12.017789723879355, -2.0729368308007636), (1.5, 1.5, 1.0), "PWM_Quarry_2x2x2_A97", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (9692.562, 6849.9365, 3850.5225), (0.06728418246844041, -62.928745925427805, 177.83936740794752), (2.20565, 2.20565, 2.605348), "PWM_Quarry_2x2x2_A98", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (9901.143, 5726.4243, 2559.1426), (0.8111668463267966, -77.98153504569184, 177.9269107890192), (1.5, 1.5, 1.0), "PWM_Quarry_2x2x2_A99", _folder)
if a: placed += 1
else: skipped += 1

# Batch 34: StaticMesh'PWM_Quarry_2x2x5_A' (42 instances)
_mesh_path = "/Game/Unshippable/Whitebox/Rocks/Meshes/PWM_Quarry_2x2x5_A"
_materials = ['/Game/Environments/ProcTexturing/ProcMaterial_Quarry_Atlas_2']
_folder = "Reconstruction/BD_BB_Chapter5_BalrogsNest/Meshes"
a = spawn_static_mesh(_mesh_path, _materials, (1586.8545, 6101.715, 2109.5967), (-58.98447648314081, -81.81885366657373, -87.81366254617825), (1.3698099, 1.3698099, 1.3698099), "PWM_Quarry_2x2x5_A_90", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2054.2383, 4077.9844, 1553.2578), (6.879010225638788, 39.01727661634308, -7.39120350368765), (2.271447, 1.718349, 1.718349), "PWM_Quarry_2x2x5_A10", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (9720.005, 9988.058, 1639.5459), (0.0, -74.60754934169329, 0.0), (1.6390913, 1.6390913, 1.6390913), "PWM_Quarry_2x2x5_A11_618", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1812.4531, 6111.6133, 858.2163), (58.383472106636155, -97.23799022501473, 96.23252461428677), (1.283724, 1.283724, 1.283724), "PWM_Quarry_2x2x5_A12", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1765.0449, 6470.225, 1553.2578), (6.879010708804456, -152.69081075207893, -7.391203869485078), (2.271447, 1.718349, 1.718349), "PWM_Quarry_2x2x5_A13", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2050.7637, 5862.5723, 2148.1382), (-41.28884424320008, -89.1170484585089, -87.8893910060281), (1.5559373, 1.5559373, 1.5559373), "PWM_Quarry_2x2x5_A14_127", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2849.9072, 6458.2896, 1440.2354), (6.879010241504248, -135.19691042772845, -7.39120359408362), (2.271447, 1.718349, 1.718349), "PWM_Quarry_2x2x5_A15", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3597.039, 6493.6304, 1576.8677), (-4.039671811757221, -53.774528841958144, 176.7726428988792), (1.572146, 1.572146, 1.572146), "PWM_Quarry_2x2x5_A16", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5224.007, 7318.3203, 1440.2354), (6.879010264668983, -145.132958675355, -7.391202552044173), (2.271447, 1.718349, 1.718349), "PWM_Quarry_2x2x5_A17", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (6811.2837, 5194.9478, 2387.5352), (-63.445641709572, -89.64421698328772, 88.7400221235), (2.5655172, 1.704713, 1.712224), "PWM_Quarry_2x2x5_A18", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4851.885, 4208.9463, 1534.5713), (6.042756392417264, 20.429109573406333, -5.99072283151789), (2.271447, 1.718349, 1.718349), "PWM_Quarry_2x2x5_A19", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2462.125, 6356.374, 1582.6123), (-4.039703370851426, -71.26812924884536, 179.05054492256886), (1.572146, 1.572146, 1.572146), "PWM_Quarry_2x2x5_A2_104", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4174.747, 4411.295, 1674.919), (-5.5408324010467345, 101.74875939958348, 178.4304687221829), (1.572146, 1.572146, 1.572146), "PWM_Quarry_2x2x5_A20", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (8264.997, 4503.295, 1523.1011), (0.0, 44.713660106259006, -0.0), (1.5716234, 1.5716234, 1.5716234), "PWM_Quarry_2x2x5_A21_7", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (8460.622, 9247.849, 1440.2354), (6.8790114831221185, -121.9516478965107, -7.391204450607977), (2.271447, 1.718349, 1.718349), "PWM_Quarry_2x2x5_A22", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (9117.974, 9506.2705, 1582.6123), (-4.039672342241571, -40.529292985281856, 179.05054488647016), (1.572146, 1.572146, 1.572146), "PWM_Quarry_2x2x5_A23", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (7906.369, 8775.09, 1324.7817), (1.768042194157931, -20.042848371878264, -177.45633136477383), (1.572146, 1.572146, 1.572146), "PWM_Quarry_2x2x5_A24", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5847.2344, 6901.488, 2072.496), (-82.474809191478, -129.7736866420657, -26.090536358929597), (1.0, 1.0, 1.0), "PWM_Quarry_2x2x5_A25_75", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5265.591, 6708.628, 2182.3418), (-54.451896973224756, -82.76751201024724, -80.9259768560275), (1.4499506, 1.4499506, 1.4499506), "PWM_Quarry_2x2x5_A26", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4528.1074, 6130.172, 2287.9272), (-54.9383227623782, -74.07587204136605, -88.02344462558007), (1.449951, 1.449951, 1.449951), "PWM_Quarry_2x2x5_A27", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3592.5537, 6213.4897, 1938.8657), (-85.61522040654636, -50.892115054635966, -128.60834891366008), (1.0, 1.0, 1.0), "PWM_Quarry_2x2x5_A28_88", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5736.616, 4765.4014, 2140.4907), (-11.685274505873231, 119.33121356054268, 85.82565463429124), (1.5383396, 1.5383396, 1.8324505), "PWM_Quarry_2x2x5_A29_198", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1285.2461, 1080.0156, 863.7407), (58.38347434608837, 93.9927766379743, 96.23231711510978), (1.2837241, 1.2837241, 1.2837241), "PWM_Quarry_2x2x5_A3_5", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5030.327, 4797.758, 2243.6357), (-87.30468208919935, 3.840986289587169, -11.632364108731819), (1.53834, 1.53834, 1.832451), "PWM_Quarry_2x2x5_A30", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4395.452, 4335.165, 1513.8394), (0.0, -77.26577804583594, 0.0), (1.7581017, 1.7581017, 1.7581017), "PWM_Quarry_2x2x5_A31_271", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (549.01855, 5943.679, 1111.7852), (0.0, -86.86032338753459, 0.0), (1.8861617, 1.8861617, 1.8861617), "PWM_Quarry_2x2x5_A32_403", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1762.9326, 3707.962, 1111.7852), (0.0, -86.86032338753459, 0.0), (1.886162, 1.886162, 1.886162), "PWM_Quarry_2x2x5_A33", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1762.9326, 3240.8076, 1232.5059), (0.0, 164.90075788463992, -0.0), (1.886162, 1.886162, 1.886162), "PWM_Quarry_2x2x5_A34", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (349.01855, 5943.679, 1211.7852), (0.0, -86.86032338753459, 0.0), (1.886162, 1.886162, 1.886162), "PWM_Quarry_2x2x5_A35", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (8379.997, 4718.295, 823.1011), (0.0, 47.526142414711856, -0.0), (1.0, 1.0, 1.0), "PWM_Quarry_2x2x5_A36", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (855.7577, 2246.997, 2301.4404), (-41.28854210043316, 178.18311396162179, -87.88915577812122), (1.555937, 1.555937, 1.555937), "PWM_Quarry_2x2x5_A37", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1419.562, 2687.5457, 1571.1472), (-41.28818276469885, 165.78881476239712, -87.88898848570291), (1.555937, 1.555937, 1.555937), "PWM_Quarry_2x2x5_A38", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1018.9158, 2228.1272, 762.2692), (84.36704288023347, -2.9376403386061347, -89.41773835671856), (1.160333, 1.160333, 1.160333), "PWM_Quarry_2x2x5_A39", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (6784.8994, 4868.0186, 2190.6782), (-64.62117026745494, 68.21848533767651, -70.63252091011788), (1.7122244, 1.704713, 1.7122244), "PWM_Quarry_2x2x5_A4_35", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (300.36804, 968.0857, 1294.5624), (7.409306749239473, 53.42329513341874, -5.465972479024696), (2.6999457, 2.5322235, 2.5322235), "PWM_Quarry_2x2x5_A40", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (150.36804, 1055.9557, 1949.5624), (-11.524353531243893, 164.82036409572194, 155.36571540962768), (2.532223, 2.532223, 2.532223), "PWM_Quarry_2x2x5_A41", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (134.01855, 5943.679, 1211.7852), (0.0, 153.26665525591363, -0.0), (2.0158901, 2.0158901, 2.0158901), "PWM_Quarry_2x2x5_A42", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2324.963, 4362.9277, 1802.0801), (-35.88161912820404, 87.86266402135557, 89.93438331852938), (1.5469279, 1.73915, 1.5469279), "PWM_Quarry_2x2x5_A5", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1183.1079, 517.0156, 1324.1357), (-2.7545470864515975, -92.20269045063829, 3.8401988906494164), (2.2714467, 1.7183487, 1.7183487), "PWM_Quarry_2x2x5_A6_24", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2867.3018, 4603.4697, 866.4004), (58.383095693353205, 112.94267233463445, 96.232279102189), (1.283724, 1.283724, 1.283724), "PWM_Quarry_2x2x5_A7", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3038.4814, 5034.131, 775.11865), (84.36817502494907, -57.75416047616648, -89.41848832062337), (1.1603332, 1.1603332, 1.1603332), "PWM_Quarry_2x2x5_A8_51", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1175.0996, 6201.025, 1657.002), (-4.03967255546337, -54.129023650372645, 179.0505451153943), (1.572146, 1.572146, 1.572146), "PWM_Quarry_2x2x5_A9_108", _folder)
if a: placed += 1
else: skipped += 1

# Batch 35: StaticMesh'PWM_Quarry_3x3x2' (32 instances)
_mesh_path = "/Game/Unshippable/Whitebox/Rocks/Meshes/PWM_Quarry_3x3x2"
_materials = ['/Game/Environments/ProcTexturing/ProcMaterial_Quarry_Atlas_A']
_folder = "Reconstruction/BD_BB_Chapter5_BalrogsNest/Meshes"
a = spawn_static_mesh(_mesh_path, _materials, (1691.1348, 6091.2603, 2060.4102), (3.469442187484334, 71.05347144154018, 172.80284878651167), (1.983766, 2.107586, 2.271762), "PWM_Quarry_3x3x10", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1140.2012, 6045.1626, 1979.6914), (12.577006821775896, -21.42864823598602, 173.96937587190413), (1.983766, 2.3747678, 2.271762), "PWM_Quarry_3x3x11", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1183.8955, 5860.7334, 2207.2656), (3.4694427760226842, 40.08454176892021, 172.80285024098703), (1.983766, 2.107586, 2.271762), "PWM_Quarry_3x3x12", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3665.5625, 5869.6943, 728.6831), (2.028285852630011, 71.2676921996, 10.123773865591184), (1.1005814, 1.1005814, 1.1005814), "PWM_Quarry_3x3x13_168", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3993.6426, 6220.504, 756.09424), (4.815624997525671, -27.869720233416917, 3.0858024240811326), (1.100581, 1.100581, 1.100581), "PWM_Quarry_3x3x14", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5002.3027, 6989.3833, 2063.1997), (3.4694424736556844, 85.25189967171755, 172.80284904139035), (1.983766, 2.107586, 2.271762), "PWM_Quarry_3x3x15", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4698.7007, 5327.353, 773.9702), (4.815624286240627, 148.62752793508778, 3.085826293344115), (1.100581, 1.100581, 1.100581), "PWM_Quarry_3x3x16", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5212.3994, 4510.9375, 2251.6138), (5.074380390974122, -109.36325170470091, 172.55623442463022), (1.983766, 2.107586, 2.271762), "PWM_Quarry_3x3x17", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (9140.237, 4400.623, 2226.7666), (3.1604097061095517, -92.60515849070613, 172.62980339937025), (1.983766, 2.107586, 2.271762), "PWM_Quarry_3x3x18", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5338.923, 7344.7617, 1879.7471), (3.469439330824252, 85.25192727855966, 80.73452563219523), (1.8354902, 2.107586, 2.964206), "PWM_Quarry_3x3x19", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (899.88477, 1066.5518, 853.5244), (-6.564849795395456, 69.19305859511931, -6.8061226044560925), (1.1597443, 1.1597443, 1.1597443), "PWM_Quarry_3x3x2_8", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4850.0674, 7282.2173, 1629.3613), (7.3512154881029295, 112.63805792606944, 83.36742186371923), (1.83549, 2.107586, 3.3714323), "PWM_Quarry_3x3x20_41", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2193.918, 4545.755, 1842.4619), (-5.841490933707608, -102.13075947307775, 174.7987383812695), (1.983766, 2.107586, 2.7250803), "PWM_Quarry_3x3x21", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (10147.668, 6690.692, 2802.3555), (18.181536925768075, 118.10879275903254, 142.98404194609284), (2.465424, 2.589244, 2.75342), "PWM_Quarry_3x3x22", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (733.1299, 996.0635, 2003.6611), (3.4694425532386117, -102.08903820484255, 172.80291514193343), (1.983766, 2.107586, 2.271762), "PWM_Quarry_3x3x23", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (9415.645, 7517.126, 3113.845), (8.839016556901532, 168.64279557427167, 162.7748745569285), (2.676215, 2.676215, 2.676215), "PWM_Quarry_3x3x24", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1101.1312, 2595.4531, 2213.7124), (3.4694422352901797, -21.64630347029754, 172.80284872600504), (1.983766, 2.107586, 2.271762), "PWM_Quarry_3x3x25", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1081.035, 3147.9453, 2132.9937), (12.577000960713875, -114.12799316221476, 173.96935572361932), (1.983766, 2.107586, 2.271762), "PWM_Quarry_3x3x26", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1734.006, 2975.2183, 1483.4192), (3.469442684030014, -34.0393698715052, 172.8028489675192), (1.983766, 2.107586, 2.271762), "PWM_Quarry_3x3x27", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1832.9521, 3519.15, 1402.7004), (12.576999434817774, -126.52043476063457, 173.96935468853817), (1.983766, 2.107586, 2.271762), "PWM_Quarry_3x3x28", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1365.4886, 1530.4792, 1802.389), (8.027049568755153, -50.85815493375739, 168.1132272599879), (1.983766, 2.107586, 2.271762), "PWM_Quarry_3x3x29", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (891.022, 635.93066, 1915.772), (-10.621700689211194, -101.00314761483885, 91.70567045740435), (1.9837662, 2.1075857, 2.2717617), "PWM_Quarry_3x3x3_13", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (908.4228, 3841.251, 2114.1462), (1.4796644599736388, -53.158201504111766, 164.98364705490633), (2.1676068, 2.2914264, 2.7590182), "PWM_Quarry_3x3x30", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1128.8201, 4163.987, 2059.2656), (1.4796644599736388, -53.158201504111766, 164.98364705490633), (2.1676068, 2.2914264, 2.908921), "PWM_Quarry_3x3x31", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (662.3702, 4116.056, 2261.095), (1.4796648312636225, -140.0786153907979, 164.98364425500162), (2.167607, 2.3320534, 3.4308236), "PWM_Quarry_3x3x32", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1233.7815, 1514.1735, 2030.8259), (1.2894923208622706, -79.35549358890277, 165.74524020323517), (2.0928345, 2.248186, 3.093418), "PWM_Quarry_3x3x33", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1355.4844, 4406.588, 1935.2012), (3.4694425532386117, -102.08903820484255, 172.80291514193343), (1.983766, 2.107586, 2.271762), "PWM_Quarry_3x3x4_15", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1254.3003, 4210.203, 1794.0833), (11.199425233832036, 141.90238883824662, 173.83521126422917), (1.983766, 2.107586, 2.3819966), "PWM_Quarry_3x3x5", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1832.1836, 4507.45, 1832.0786), (-5.841490933707608, -102.13075947307775, 174.7987383812695), (1.983766, 2.107586, 2.271762), "PWM_Quarry_3x3x6_19", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1416.1973, 4440.451, 1884.6089), (12.577005900273239, 165.42846678176053, 173.969403191695), (1.983766, 2.107586, 2.271762), "PWM_Quarry_3x3x7", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2568.7188, 4476.825, 1867.6416), (-4.468231262077248, -102.10367069905993, 174.5026224754316), (1.983766, 2.107586, 2.271762), "PWM_Quarry_3x3x8", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2217.914, 4522.508, 2010.7285), (5.4036758688693025, 5.284515093505988, 175.77485740387522), (1.983766, 2.4003794, 2.271762), "PWM_Quarry_3x3x9", _folder)
if a: placed += 1
else: skipped += 1

# Batch 36: StaticMesh'PWM_Quarry_4x3x10_A' (397 instances)
_mesh_path = "/Game/Unshippable/Whitebox/Rocks/Meshes/PWM_Quarry_4x3x10_A"
_materials = ['/Game/Environments/ProcTexturing/ProcMaterial_Quarry_Atlas_A']
_folder = "Reconstruction/BD_BB_Chapter5_BalrogsNest/Meshes"
a = spawn_static_mesh(_mesh_path, _materials, (859.6763, 587.2256, 1924.2788), (1.1550394489936173, -6.760161678092624, 177.9633965649812), (1.0, 1.0, 1.0), "PWM_Quarry_4x3x10_16", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4040.1426, 4522.3564, 1981.7046), (-1.2119142087194106, 34.77832201819064, -177.89946284361454), (1.0, 1.0, 0.72845), "PWM_Quarry_4x3x100", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (6720.496, 7001.4595, 2385.917), (0.66984801185453, 56.76327356204943, 179.90196629489213), (1.0, 1.2059252, 1.0), "PWM_Quarry_4x3x101", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3957.4492, 4392.3564, 1730.8848), (2.035866502023754, -135.30682630361912, 178.82038475891483), (1.0, 1.0, 0.72845), "PWM_Quarry_4x3x102", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (6001.9575, 4641.2656, 1790.3418), (-2.3854367778307832, 33.415033745321686, -177.08716357912814), (1.0, 1.0, 0.72845), "PWM_Quarry_4x3x103_184", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5798.9688, 4490.6025, 1533.6074), (5.035630903189757, -91.58665538541206, 178.0070407097093), (1.0, 1.0, 0.72845), "PWM_Quarry_4x3x104_186", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (11123.763, 6682.9585, 2464.8538), (1.5017536289110698, 104.5509757314229, -174.45468677119948), (1.425311, 1.2149967, 1.2149967), "PWM_Quarry_4x3x105_322", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (6632.409, 7127.2363, 1580.7544), (1.709846091634124, -19.85580664864231, -179.48662083621437), (1.23943, 1.0, 1.0), "PWM_Quarry_4x3x106", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (11887.981, 6391.311, 1338.4518), (-0.7495420921039859, -85.25469373119043, -178.76705191894283), (1.0, 5.4925, 1.0), "PWM_Quarry_4x3x107", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (7206.1597, 7297.67, 2198.1953), (6.393849586397358, 89.83014146772048, -177.69686913364473), (1.0, 1.205925, 1.0), "PWM_Quarry_4x3x108", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (7182.5996, 6999.346, 589.13916), (-2.209533909606087, 47.388062416774936, 1.4371360968903555), (1.0, 1.0, 0.783208), "PWM_Quarry_4x3x109", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (8420.927, 4524.5957, 1080.5039), (0.0, -59.41411716800466, 0.0), (1.0, 1.0, 0.6900759), "PWM_Quarry_4x3x10_A_4", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5585.2705, 5201.628, 840.3262), (0.0, -90.0001164887758, 0.0), (0.533538, 0.533538, 0.25568992), "PWM_Quarry_4x3x10_A2_28", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5476.3643, 5360.798, 749.51855), (0.0, 142.20124721279078, -0.0), (0.533538, 0.533538, 0.25569), "PWM_Quarry_4x3x10_A3", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (878.59955, 777.0821, 1311.1908), (0.5677729540395151, -14.617279316546608, 175.67372038157947), (1.0, 1.0, 1.0), "PWM_Quarry_4x3x11", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (7268.1016, 7117.525, 671.7197), (-2.549469396767828, 65.73584576933521, 0.668845198150093), (1.0, 1.0, 0.783208), "PWM_Quarry_4x3x110", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (7750.8496, 7333.321, 2592.2632), (3.2647276253476534, 56.516238462386596, 174.56229755120643), (1.0, 1.205925, 1.0), "PWM_Quarry_4x3x111", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (7235.534, 7352.9253, 1389.749), (2.1941790880499465, 167.6349315857939, 177.86452687281184), (1.0, 1.205925, 1.2222234), "PWM_Quarry_4x3x112", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (11116.346, 7194.8994, 1305.544), (1.0958216272335393, 109.48863024133345, -174.9406896823693), (1.0, 1.0, 1.0), "PWM_Quarry_4x3x113", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (10984.189, 7136.577, 1974.1079), (4.074472960525307, -57.92974121262339, 169.50371673635993), (1.0, 1.0, 1.0), "PWM_Quarry_4x3x115", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (7566.569, 7420.035, 2698.955), (1.838519611925207, 123.19800448146559, -3.9275517516035348), (1.0, 1.205925, 1.0), "PWM_Quarry_4x3x116", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (7301.9854, 6754.4453, 767.21094), (-3.5671077553121617, -139.74333134150854, -11.838317279945338), (0.8175096, 0.8175096, 0.49816895), "PWM_Quarry_4x3x117_161", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (11004.618, 6254.9214, 2501.397), (-10.72784649416042, 167.3796483366084, -179.49913373398144), (0.84918094, 1.298661, 0.7686459), "PWM_Quarry_4x3x118", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (7539.1763, 7501.2866, 1641.4951), (2.8716032531224247, 101.53576932708812, 176.91054961511222), (1.0, 1.205925, 1.0), "PWM_Quarry_4x3x119_102", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1106.5586, 958.43744, 1636.8517), (2.4783476373319133, -129.60284746068237, -179.40249903111933), (1.1113198, 1.0, 1.2298996), "PWM_Quarry_4x3x12", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (7139.4688, 6981.009, 2276.3516), (1.1577787587675294, 12.418945692448741, -8.811066727656291), (1.0, 1.205925, 1.0), "PWM_Quarry_4x3x120", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (9350.301, 4641.8037, 2481.37), (-0.7945861324405975, -105.30561668064317, -178.96678333821623), (1.0, 1.0, 0.729925), "PWM_Quarry_4x3x121", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4480.45, 5062.108, 2052.0322), (-0.06329342600455673, -89.51780707625922, 179.7501104748332), (0.632561, 1.205925, 0.45027727), "PWM_Quarry_4x3x122", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (6206.125, 4931.62, 1792.8018), (1.1425949737871512, -44.2904062499501, -178.27391175840944), (1.0, 1.205925, 1.0), "PWM_Quarry_4x3x123", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4428.923, 6657.6196, 1784.2646), (1.8643548680839122, 169.76691799747817, -178.27336500228952), (1.0, 1.205925, 1.0), "PWM_Quarry_4x3x124", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (8571.656, 4172.164, 702.55176), (6.709539227182053, 56.01288003216895, 170.82556353460365), (1.0, 1.0, 0.72845), "PWM_Quarry_4x3x125_403", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (7755.0933, 8583.885, 1432.7891), (1.5577408177029433, 104.93339552817355, 176.47856568867306), (1.23943, 1.0, 1.0), "PWM_Quarry_4x3x126_430", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (8346.016, 4020.2563, 1047.5986), (-12.417938436877073, -78.12759669248187, -174.68956865421777), (1.0, 1.0, 0.72845), "PWM_Quarry_4x3x127", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (6974.724, 7170.734, 1685.3921), (1.1577791790521932, 12.418945660683706, -8.811066682362615), (1.0, 1.205925, 1.0), "PWM_Quarry_4x3x128", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (8009.1543, 4493.674, 1240.9297), (-2.022704837524285, -179.06585881093943, 177.4858310183921), (1.23943, 1.0, 1.0), "PWM_Quarry_4x3x129", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1374.39, 4132.9487, 2077.3862), (4.822112859813633, -64.29790759354385, -173.75061864742867), (1.0, 1.0, 1.0), "PWM_Quarry_4x3x13", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (8523.817, 4535.9033, 2066.9692), (13.040685388523379, -71.61888860880944, 178.0325286907393), (1.0, 1.0, 0.72845), "PWM_Quarry_4x3x130", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (8005.681, 4674.9233, 2078.0127), (-23.13497987055537, 36.562987930676094, -151.58787879438236), (1.0, 1.0, 1.0), "PWM_Quarry_4x3x131", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (8456.216, 5432.528, 2883.2354), (-14.84676781329321, -103.26960990102104, 179.67104503368083), (1.0, 1.0, 0.42709517), "PWM_Quarry_4x3x132", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (8633.91, 4189.408, 1973.2842), (10.84560854291254, -38.80535659954291, 7.292485478386629), (1.2316473, 1.2316473, 0.9600974), "PWM_Quarry_4x3x133_45", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (7049.7046, 7229.3267, 1288.3452), (-1.6018674705843987, -130.96580232454312, 176.31284345110797), (1.0, 1.0, 0.8684401), "PWM_Quarry_4x3x134", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (7162.3237, 7563.746, 1328.9507), (1.8148804339257432, 48.777803465562876, -179.59162217980221), (1.23943, 1.0, 1.0), "PWM_Quarry_4x3x135", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (8220.868, 9144.773, 1548.7534), (-5.060608008527674, 144.6539312961484, -0.7763671477494076), (1.0, 1.0, 1.0), "PWM_Quarry_4x3x136", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (8422.668, 9033.315, 830.16797), (-7.632262767116008, 72.32296166502664, -176.02032788665812), (1.0, 1.0, 0.72845), "PWM_Quarry_4x3x137", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (8976.275, 9399.043, 1888.4336), (-15.501857371234923, -55.12183852270006, 177.91492753044577), (1.0, 1.0, 1.0), "PWM_Quarry_4x3x138", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (9476.286, 9478.78, 723.7383), (6.029513139316544, -89.11028500482556, 173.73868336457122), (1.0, 1.0, 0.72845), "PWM_Quarry_4x3x139", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1518.4434, 4313.0684, 1979.7686), (-1.3703007609222522, -91.6266489190756, -176.00933164536363), (1.0, 1.0, 0.7299247), "PWM_Quarry_4x3x14_10", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (9356.461, 9616.668, 1305.2993), (1.7209814746960288, -139.46387460318246, 171.64745430752203), (1.0, 1.0, 0.72845), "PWM_Quarry_4x3x140", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (9288.424, 9508.696, 1969.3872), (-2.2593687923467196, -107.386886750258, 178.77154642967318), (1.0, 1.0, 0.72845), "PWM_Quarry_4x3x141", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (9315.609, 8790.263, 616.12256), (-15.346983205919317, 100.44476797197704, 13.802867870286283), (1.0, 1.0, 0.783208), "PWM_Quarry_4x3x142", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (9388.4795, 9060.94, 751.7534), (21.421510353434535, -81.95935292336952, -11.713471014905041), (1.0, 1.0, 0.609439), "PWM_Quarry_4x3x143", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (9086.049, 8862.828, 609.6582), (-2.448943987423475, -142.7856194798632, -15.972136958619604), (1.0, 1.0, 0.609439), "PWM_Quarry_4x3x144", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (9216.512, 9352.221, 2170.2354), (3.223855279429328, 115.65872247271678, -177.95723428133562), (1.0, 1.0, 0.8644865), "PWM_Quarry_4x3x145", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (8111.6094, 8936.591, 1045.9258), (4.259201844554816, -119.23662342808467, 165.35530155686092), (1.0, 1.0, 0.72845), "PWM_Quarry_4x3x146", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (6873.5513, 7152.736, 1937.8936), (2.93871544241786, -60.346491996103794, 179.56202664809504), (1.0, 1.0, 1.0), "PWM_Quarry_4x3x147_465", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (6253.4214, 4871.873, 2728.518), (0.6698433640945287, -112.22341420945486, 179.9019526639687), (1.0, 1.0, 1.0), "PWM_Quarry_4x3x148", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (7300.3154, 7361.92, 1750.4668), (1.1870595717236174, -14.099974687656522, -178.29777914815193), (0.72371805, 0.92964333, 0.72371805), "PWM_Quarry_4x3x149", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2225.6064, 4722.4707, 669.83984), (5.097479867800201, 67.21206436392379, -12.208649961652766), (1.0, 1.0, 0.69307333), "PWM_Quarry_4x3x15_45", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (6884.618, 4592.6426, 2280.3354), (-1.4377742490979832, -159.30687783798732, 175.41550606844524), (1.0, 1.0, 1.0), "PWM_Quarry_4x3x150_168", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5958.735, 4586.682, 1298.0122), (1.4235889228228384, -85.8340661904008, 0.4341624036020535), (1.0, 1.205925, 1.0), "PWM_Quarry_4x3x151_181", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (7835.063, 8284.531, 2097.3784), (0.7723226385114847, -96.2847674285914, 179.9057707607835), (1.0, 1.0, 1.0), "PWM_Quarry_4x3x152", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (7340.217, 7736.918, 2144.4844), (-0.554779002843229, -127.09075772358426, -179.61204437353322), (1.5202222, 1.0, 1.0), "PWM_Quarry_4x3x153", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (7482.07, 7916.6274, 1783.0762), (0.66984801185453, 56.76327356204943, 179.90196629489213), (1.0, 1.205925, 1.0), "PWM_Quarry_4x3x154", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (7748.131, 8140.8677, 2398.018), (0.7152845279988261, 97.47755523252313, -179.93904738881957), (1.0, 1.0, 1.0), "PWM_Quarry_4x3x155", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (7652.248, 8097.9346, 1785.8657), (0.5120934912416378, 105.93300616512416, -179.55716358690518), (1.0, 1.205925, 1.0), "PWM_Quarry_4x3x156", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (6990.466, 6908.6577, 2988.1538), (-2.7943116876858642, -7.165893668941273, 179.33952399515218), (1.0, 1.0, 1.0), "PWM_Quarry_4x3x157", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (7942.3457, 7534.873, 2727.9048), (-6.327727004756261, -7.1132192744881095, 174.82214843111512), (1.0, 1.5064732, 0.6089958), "PWM_Quarry_4x3x158", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (624.9248, 5723.6704, 2420.8232), (4.986760750503569, 144.75483594398608, -179.26488872243027), (1.1465156, 1.2283856, 1.0), "PWM_Quarry_4x3x159", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2978.4346, 4528.3945, 979.3926), (-8.321900130373294, -61.774425984608385, 1.3912586082423772), (1.0, 1.0, 0.783208), "PWM_Quarry_4x3x16", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (10484.559, 10248.527, 2201.1934), (-0.7583617882422339, -136.26730495957923, -176.3845425824382), (1.0, 1.0, 1.0), "PWM_Quarry_4x3x160", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (10217.033, 10119.899, 2250.1582), (2.136551422967044, 48.55698114014647, 179.20561543205594), (1.0, 1.0, 0.72845), "PWM_Quarry_4x3x161", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (9491.23, 9738.544, 1202.185), (-0.9674681424862456, -134.38970215617036, 176.92193890453615), (1.23943, 1.0, 1.0), "PWM_Quarry_4x3x162", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (9948.335, 10032.343, 2735.8047), (0.6698433532995278, 62.37837377538041, 179.90195260040997), (1.0, 1.0, 1.0), "PWM_Quarry_4x3x163", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (11262.783, 9912.357, 2106.162), (5.776535926052233, 65.56796297156178, 0.06740573526138563), (1.0, 1.0, 1.0), "PWM_Quarry_4x3x164", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (11355.15, 9042.827, 2625.3818), (1.8470949233126213, -43.38177772054988, 174.65546162011492), (1.0, 1.0, 1.0), "PWM_Quarry_4x3x165", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (11551.276, 9099.206, 2020.9077), (0.9837246281615393, -57.129970216104404, -177.78603376830793), (1.0, 1.0, 1.0), "PWM_Quarry_4x3x166", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (11577.111, 8791.875, 1880.3555), (1.1322635813239867, 121.00027714361585, 173.6717271671834), (1.0, 1.0, 0.72845), "PWM_Quarry_4x3x167", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (11392.327, 8696.783, 2532.1865), (-3.548004063402679, 154.36596793634467, -179.84973573855171), (1.0, 1.0, 0.72845), "PWM_Quarry_4x3x168", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (11233.152, 9271.593, 2844.2163), (0.5935198311341685, 116.26982153602015, -172.14833855355522), (1.425311, 1.214997, 1.214997), "PWM_Quarry_4x3x169", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3136.4482, 4920.1123, 587.2715), (-12.702817543306343, -131.95788523933925, 13.276989140426245), (1.0, 1.0, 0.783208), "PWM_Quarry_4x3x17", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (11164.193, 10560.682, 1549.897), (-1.4251097702986155, -71.81097504162895, -179.1019164838131), (1.815031, 1.214997, 1.214997), "PWM_Quarry_4x3x170", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (11385.104, 9761.402, 1994.8408), (1.5601450142043511, 109.78773922389283, -172.86035376945782), (1.0, 1.0, 1.0), "PWM_Quarry_4x3x171", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (11370.439, 9210.446, 2511.166), (-6.867125433806545, -168.02375728868157, 179.5386672068217), (1.0, 1.259218, 1.0), "PWM_Quarry_4x3x172", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (11153.745, 9726.944, 2652.2275), (4.070526261750619, -57.83004384218734, 167.36716103240883), (1.0, 1.0, 1.0), "PWM_Quarry_4x3x173", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (11240.277, 8797.373, 3167.7773), (-12.237854122016001, 167.32495354265316, -177.96513844799122), (0.849181, 1.298661, 0.768646), "PWM_Quarry_4x3x174", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (8498.022, 4381.9634, 2093.7285), (10.615643716521497, -37.01739786711977, 7.625736043568767), (1.231647, 1.231647, 0.960097), "PWM_Quarry_4x3x175_47", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (7830.0957, 7863.7, 619.6421), (-1.0303649552051772, 157.0175821080747, 2.6537168073754143), (1.0, 1.0, 0.9133953), "PWM_Quarry_4x3x176_292", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (10438.156, 6693.419, 2483.1348), (7.436068977968875, -41.42938262084203, 170.63864587175797), (1.0, 1.0, 0.6796589), "PWM_Quarry_4x3x177_22", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (7601.1333, 7852.369, 1125.5879), (-1.962127729000279, 170.56298909276475, 2.920653905962501), (1.0, 1.0, 0.913395), "PWM_Quarry_4x3x178", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (6215.623, 4901.7153, 1013.4629), (3.28116119853076, 83.09307402549473, 176.7339348054602), (1.23943, 1.0, 1.0), "PWM_Quarry_4x3x179", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2719.3125, 4908.492, 562.0703), (33.620907759292514, 116.2120355563182, -1.7130771039202477), (1.0, 1.0, 0.783208), "PWM_Quarry_4x3x18", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4403.922, 6685.6396, 1007.1113), (3.2811608627867574, -62.87121008607717, 176.7339349006791), (1.23943, 1.0, 1.0), "PWM_Quarry_4x3x180", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5817.2188, 6647.994, 2747.625), (0.6698480835986662, 12.772919303944358, 179.90196629577636), (1.0, 1.0, 1.0), "PWM_Quarry_4x3x181", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (6043.221, 6227.8696, 2883.692), (26.971424993412835, -177.3486323386124, 95.74245492237542), (1.4428596, 1.0851302, 1.0851302), "PWM_Quarry_4x3x182", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (7123.0337, 6617.72, 2849.8223), (-2.1152344796750953, 127.38724663031252, -171.0658470320867), (1.0, 1.205925, 1.0), "PWM_Quarry_4x3x183", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5942.5884, 7262.345, 1524.2285), (0.37041827589390114, -176.35208299191675, -176.56332599927697), (1.23943, 1.0, 1.0), "PWM_Quarry_4x3x184_38", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4419.4863, 6883.837, 1315.6865), (-1.3834226252354849, 3.971129647900267, 177.86843427596597), (1.0, 1.205925, 1.0), "PWM_Quarry_4x3x185", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5472.723, 4447.196, 2333.8418), (3.685638034257413, -48.8652253925469, -179.75277411644987), (1.0, 1.0, 1.0), "PWM_Quarry_4x3x186", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (10672.939, 6005.2314, 497.38867), (-4.028320941741087, -45.36023587710609, -0.4420777603873434), (1.0, 1.0, 1.0), "PWM_Quarry_4x3x187", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5752.159, 4489.071, 2107.0386), (-3.628540581243997, 116.50766620239183, -179.3088218722253), (1.0, 1.0, 1.0), "PWM_Quarry_4x3x188", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (6140.5537, 4636.2334, 1837.5537), (0.183861811152777, -40.38585910487303, -175.9364560003147), (1.0, 1.0, 0.72845), "PWM_Quarry_4x3x189", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2227.9268, 4537.507, 863.12695), (6.27416330256666, 128.79638750514727, 6.130342185917821), (0.83988935, 0.9197802, 0.60477686), "PWM_Quarry_4x3x19", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (6069.4907, 4798.4844, 966.91895), (-0.6797486624467515, 140.0268300677745, -1.3239137214696621), (1.0, 1.205925, 1.0), "PWM_Quarry_4x3x190", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (6223.6255, 5030.44, 1551.5933), (-1.1271971531950327, 55.81689785687157, 0.48505246742760644), (0.7804569, 0.6828433, 0.9493665), "PWM_Quarry_4x3x191", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (6343.4155, 4663.5967, 1067.478), (0.3585782157368031, -58.96564051585533, 176.8617785797273), (1.3598889, 1.205925, 1.0), "PWM_Quarry_4x3x192", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4487.623, 4999.0186, 1534.7646), (0.19291178952437907, 167.61701798896058, -1.2219541396388027), (0.67951256, 0.69428986, 1.2607276), "PWM_Quarry_4x3x193", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4771.8516, 5706.8945, 2518.7598), (70.46214706823453, -178.9990400256102, 91.29659805649636), (0.8176306, 1.0, 1.0), "PWM_Quarry_4x3x194_212", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4977.179, 5556.118, 2498.7598), (70.46169808525593, -1.3693761126357258, 91.29635417323755), (0.817631, 1.0, 1.0), "PWM_Quarry_4x3x195", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (7613.993, 7468.1865, 2676.8032), (-9.463256569121524, -6.82543884945015, 172.81418734713844), (1.0, 1.506473, 0.8902824), "PWM_Quarry_4x3x196", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (7796.571, 7297.5264, 2867.3022), (10.986831889146096, 113.24158283246753, 175.49735797119547), (1.0, 1.506473, 0.890282), "PWM_Quarry_4x3x197", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (8648.494, 4614.9434, 2796.625), (-0.46377567721811785, -114.6308303729574, -177.34932898103457), (1.0, 1.0, 1.0), "PWM_Quarry_4x3x198", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (9428.915, 9692.898, 1988.6436), (1.683019904427587, 68.75677916406126, -179.49069158347947), (1.23943, 1.0, 1.0), "PWM_Quarry_4x3x199_140", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1213.931, 904.19586, 863.05457), (-3.610991820184157, -133.36029303375074, 3.296734759647302), (1.0, 1.2918277, 1.0), "PWM_Quarry_4x3x20_84", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4359.8145, 5267.2534, 2495.8936), (69.7883695495968, -14.594852775820515, 77.24156973841191), (0.817631, 1.0, 1.0), "PWM_Quarry_4x3x200", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (6853.8804, 6504.229, 2825.474), (0.6698479987124507, 84.19012030496172, 179.90196628739213), (1.0, 1.6734476, 1.0), "PWM_Quarry_4x3x201", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (7930.339, 7248.565, 3057.113), (-5.319670549671497, -112.44689045521011, 169.62135661367086), (1.0, 1.506473, 0.890282), "PWM_Quarry_4x3x202", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (8007.3745, 7675.8896, 2672.9263), (3.5146412771562514, 150.00208950620961, -171.36237154955566), (1.0, 1.506473, 0.890282), "PWM_Quarry_4x3x203", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (10159.985, 6463.255, 2753.5898), (44.71740140961488, -11.53582875609832, 146.47901123494236), (1.0, 1.506473, 0.7080555), "PWM_Quarry_4x3x204", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (6865.093, 6723.9194, 2616.6494), (0.6698479450677501, 11.258482937637178, 179.90196627157943), (1.0, 1.0, 1.0), "PWM_Quarry_4x3x205", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (6854.8423, 6824.2134, 2479.816), (0.6698480224314283, -111.3691440667897, 179.9019662220507), (1.0, 1.0, 1.0), "PWM_Quarry_4x3x206", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3997.2031, 5000.7534, 2419.6777), (-5.952666814627333, 34.78496723467192, -176.32846500039042), (1.0, 1.0, 0.72845), "PWM_Quarry_4x3x207", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4171.0195, 5060.5645, 2445.481), (-5.952636239411492, -168.97233810486037, -176.3284654920829), (1.3320405, 1.0, 0.72845), "PWM_Quarry_4x3x208", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4045.961, 5341.1567, 2369.4707), (-28.52706982513805, 173.79394653590288, 106.39143944628545), (1.0, 1.0, 1.0), "PWM_Quarry_4x3x209_228", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1239.0884, 586.2207, 1548.7534), (-5.5277394885419255, -94.05626086813169, 2.28131608320413), (1.0, 1.0, 1.0), "PWM_Quarry_4x3x21", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4149.5293, 5188.5, 2427.915), (-5.952666814627333, 34.78496723467192, -176.32846500039042), (1.0, 1.0, 0.72845), "PWM_Quarry_4x3x210", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4111.2354, 5993.6743, 2465.5303), (-1.9314885177064847, -120.63878675894529, 178.7717789633358), (1.0, 1.0, 0.72845), "PWM_Quarry_4x3x211", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3967.4785, 5879.3145, 2496.8184), (-1.9314882975821874, -144.74988311433614, 178.77177876049026), (1.0, 1.0, 0.9500854), "PWM_Quarry_4x3x212", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3749.3096, 5879.3145, 2496.8188), (-1.9314879820987023, 174.45480845753983, 178.77177851938123), (1.0, 1.0, 0.950085), "PWM_Quarry_4x3x213", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4308.795, 6023.282, 2433.918), (-1.9314882487295462, -62.21161104741943, 178.77177875463389), (0.942333, 1.1234162, 0.42496789), "PWM_Quarry_4x3x214", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3148.8916, 5373.4795, 2173.6738), (42.963136078324865, 2.6475823611585483, 85.82696773059473), (1.0, 1.0, 1.0), "PWM_Quarry_4x3x215_237", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3034.8184, 5373.4795, 2230.0132), (42.963136078324865, 2.6475823611585483, 85.82696773059473), (1.0, 1.0, 1.0), "PWM_Quarry_4x3x216", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3265.919, 4391.915, 1660.1665), (0.5493587885788257, 122.06222584904165, -177.73046641711167), (0.61049205, 0.61049205, 0.61049205), "PWM_Quarry_4x3x217", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4337.1377, 4831.871, 2218.2607), (0.24285430183838297, 34.92669221376332, -172.97535564040047), (1.0, 1.0, 0.72845), "PWM_Quarry_4x3x218", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4374.006, 4930.249, 1881.458), (3.106916488630642, -92.04548191530696, 170.33441963609897), (0.5906504, 0.5906504, 0.5089894), "PWM_Quarry_4x3x219", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1637.459, 4096.752, 2065.042), (0.42393183683083535, -136.40407533416084, -176.55296592913675), (1.0, 1.0, 1.0), "PWM_Quarry_4x3x22_93", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4450.2383, 4930.249, 1559.3408), (0.40469251410784385, -140.00287034169799, 173.561017114328), (0.59065, 0.59065, 0.508989), "PWM_Quarry_4x3x220", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4293.342, 4751.2314, 1005.3408), (3.106916488630642, -92.04548191530696, 170.33441963609897), (0.59065, 0.59065, 0.508989), "PWM_Quarry_4x3x221", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4241.961, 4585.9688, 1180.206), (0.017574073767088222, 1.6458130685678602, 1.3899286923819374), (0.9033428, 0.7147331, 0.4518238), "PWM_Quarry_4x3x222", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4432.377, 4840.871, 1144.293), (0.017574073767088222, 1.6458130685678602, 1.3899286923819374), (0.903343, 0.714733, 0.451824), "PWM_Quarry_4x3x223", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4394.9414, 4856.6436, 1152.542), (-3.4905400560933413, -88.71576339455035, 3.5025177078152674), (0.59065, 0.59065, 0.508989), "PWM_Quarry_4x3x224", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4506.0312, 4862.3486, 2110.4014), (-4.434021018417375, 1.6509400689440998, 1.2617240464450379), (0.903343, 0.714733, 0.451824), "PWM_Quarry_4x3x225", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4593.169, 4635.2993, 2088.2383), (-1.5073546557832724, -84.42699239634445, -4.1540529281565775), (0.903343, 0.714733, 0.451824), "PWM_Quarry_4x3x226", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4807.004, 4507.09, 2166.9111), (1.8661032746635868, -31.339230536080972, 175.81100766353333), (0.903343, 0.9597519, 0.451824), "PWM_Quarry_4x3x227", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5078.7725, 4349.737, 2315.1816), (3.6856375627612263, -39.752927083908574, -179.7527743007378), (1.0, 1.0, 1.0), "PWM_Quarry_4x3x228_268", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (7819.798, 7736.5024, 699.4614), (-2.923064985215118, 106.93170195187447, 3.8390193458637434), (1.0, 1.0, 0.63266355), "PWM_Quarry_4x3x229", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1944.9912, 4202.509, 1902.2412), (4.757301521789068, -91.63189899487686, -176.18371852338117), (1.0, 1.0, 0.729925), "PWM_Quarry_4x3x23_22", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (11798.075, 7212.3813, 1239.1388), (-0.7495420921039859, -85.25469373119043, -178.76705191894283), (1.0, 4.0299997, 1.0), "PWM_Quarry_4x3x230", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (7893.796, 8372.529, 701.6582), (1.5675627103078869, 84.48414408872173, -0.3511659073155114), (1.0, 1.0, 0.632664), "PWM_Quarry_4x3x231", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (8242.87, 8720.086, 623.3589), (-4.512023870172314, 102.71060622913787, -0.07260136233982684), (1.0, 1.0, 0.632664), "PWM_Quarry_4x3x232", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (7983.328, 8613.066, 659.9536), (3.352857031983711, 63.63493184019486, 174.1404141201732), (1.0, 1.0, 0.632664), "PWM_Quarry_4x3x233", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (10461.285, 8404.125, 860.8447), (19.61537843491845, 114.11443054725727, 158.953114233417), (1.0, 1.0, 0.72845), "PWM_Quarry_4x3x234", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (8703.926, 9290.891, 1993.185), (-0.01992787835646073, -152.80512122354318, -164.36056557807618), (1.0, 1.0, 1.0), "PWM_Quarry_4x3x235", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (8440.058, 9190.401, 1844.4897), (-0.01992807549167328, -152.805461739613, -177.5398013642309), (1.3370845, 1.0, 1.0), "PWM_Quarry_4x3x236", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (8478.079, 9092.817, 2378.8076), (1.8623443887193305, 75.90527159833658, 178.3917247608405), (1.337085, 1.0, 1.0), "PWM_Quarry_4x3x237", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (9082.064, 9370.111, 1960.2266), (1.862343994654414, 75.90527159761162, 178.39172474413778), (1.337085, 1.0, 1.0), "PWM_Quarry_4x3x238", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (11301.575, 9536.648, 2508.501), (6.765696713342982, -2.5041192412165882, 178.7335542140592), (1.0, 1.259218, 1.0), "PWM_Quarry_4x3x239", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1720.8301, 4544.669, 2013.5273), (-4.264007114745999, -91.6307302561362, -175.92687356039062), (1.0, 1.0, 0.729925), "PWM_Quarry_4x3x24_24", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (11466.232, 9210.419, 2039.5361), (1.7935803902669398, 71.75824135463687, 1.2128530730845657), (1.0, 1.0, 1.0), "PWM_Quarry_4x3x240", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (11435.408, 9541.5, 2037.2539), (-6.872009102392294, -168.66077476178805, 179.61494749719424), (1.0, 1.259218, 1.0), "PWM_Quarry_4x3x241_330", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (11053.284, 8508.066, 2121.7002), (-2.6814883536256615, -113.29192308636613, 173.303766342108), (0.763337, 1.022555, 0.763337), "PWM_Quarry_4x3x242", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (11314.523, 8530.513, 1640.7646), (-1.9352117567372351, -113.36189727447974, 175.03589270754665), (0.763337, 1.022555, 0.763337), "PWM_Quarry_4x3x243", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (11375.49, 8642.084, 1690.5337), (4.187917555053867, -27.131166787332052, 178.0773345996935), (0.763337, 1.022555, 0.763337), "PWM_Quarry_4x3x244", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (10970.506, 8324.707, 1842.1196), (7.154375907925663, -27.231133528500827, 174.07317741913985), (0.763337, 1.022555, 0.763337), "PWM_Quarry_4x3x245", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (11256.092, 10074.959, 2019.4375), (-1.905883983027883, -137.39984122022602, -179.26554470995202), (1.0, 1.4737881, 1.0), "PWM_Quarry_4x3x246", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (10802.797, 9739.997, 2872.416), (-3.681304749959399, -53.33288107396386, 179.69334442302124), (1.0, 1.0, 1.0), "PWM_Quarry_4x3x247", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (10824.539, 9458.408, 3033.3755), (-1.4531859575743151, 8.764464619044878, 176.6033820923456), (1.0, 1.0, 1.0), "PWM_Quarry_4x3x248", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (10626.414, 8660.217, 715.3281), (-28.86047618486851, -67.92649094359412, 13.176857421014336), (0.783559, 0.783559, 0.566767), "PWM_Quarry_4x3x249", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1223.6425, 3986.8184, 2221.8035), (3.010391787438975, -147.44793275432104, 179.76365482909154), (1.0, 1.0, 1.0), "PWM_Quarry_4x3x25", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (10923.98, 8549.953, 944.8926), (-28.86047618486851, -67.92649094359412, 13.176857421014336), (0.783559, 0.783559, 0.566767), "PWM_Quarry_4x3x250", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (10643.582, 8800.178, 649.4165), (19.69426051269803, 83.70644283167488, -25.078618887609874), (0.783559, 0.783559, 0.566767), "PWM_Quarry_4x3x251", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (9748.32, 8918.189, 3038.662), (-1.453186099697412, 8.764738726697544, 171.0112178354058), (1.0, 1.0, 1.0), "PWM_Quarry_4x3x252", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (9455.029, 9121.363, 2713.7275), (-1.453186099697412, 8.764738726697544, 171.0112178354058), (1.0, 1.0, 1.0), "PWM_Quarry_4x3x253", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (9627.107, 9008.969, 2868.5225), (9.646848460111098, 158.92192587094937, -172.91514101159933), (1.0, 1.2727835, 1.0), "PWM_Quarry_4x3x254", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2008.0234, 5179.4355, 2302.4297), (43.843373812335614, 0.5950925908079789, 84.40291838211482), (1.0, 1.0, 1.0), "PWM_Quarry_4x3x255", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (626.3013, 790.87695, 1420.6797), (5.202386876249992e-08, -90.00010457489263, 1.6914095910131002), (1.3664387, 1.3202327, 1.3202327), "PWM_Quarry_4x3x256_417", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (10100.395, 9783.319, 2667.668), (2.136551422967044, 48.55698114014647, 179.20561543205594), (1.0, 1.0, 0.72845), "PWM_Quarry_4x3x257", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (9804.842, 9463.912, 2815.414), (2.136551422967044, 48.55698114014647, 179.20561543205594), (1.0, 1.0, 0.72845), "PWM_Quarry_4x3x258", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (10115.286, 10098.669, 2342.8555), (-1.8091732342681366, -150.85417111477514, 1.698030536085178), (1.0, 1.0, 0.72845), "PWM_Quarry_4x3x259", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1600.0737, 1987.085, 1475.648), (-0.02313233188140054, -150.2641322067538, -178.58461887021326), (1.0, 1.0, 1.0), "PWM_Quarry_4x3x26", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (9566.32, 9800.203, 2189.0972), (1.121459889933697, -9.217286251727442, 178.50146858873367), (1.0, 1.0, 0.72845), "PWM_Quarry_4x3x260", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (9628.871, 4777.7207, 2365.7158), (-27.522341148667497, 90.47999303984922, 18.55703337286673), (1.231647, 1.231647, 0.960097), "PWM_Quarry_4x3x261", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (9899.528, 4598.4727, 2099.669), (-6.300171034721847, 56.939815448302355, 9.341707843948107), (1.231647, 1.231647, 0.960097), "PWM_Quarry_4x3x262", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (9711.582, 4335.787, 1899.313), (-8.854369854352903, 58.35064919147834, 14.539623990658127), (1.463985, 1.231647, 0.960097), "PWM_Quarry_4x3x263", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (8681.908, 4954.438, 2465.0967), (6.426988233016874, -149.06520690647602, 166.78477864191026), (1.5632629, 1.5319853, 0.72845), "PWM_Quarry_4x3x264", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (9557.151, 4922.429, 2438.095), (9.82834619463432, -117.76268369729603, 170.50850682058274), (1.563263, 1.531985, 0.72845), "PWM_Quarry_4x3x265", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (9751.279, 4472.157, 982.93994), (-0.5889892771104545, 42.57152885997572, 4.590636341434137), (1.563263, 1.531985, 0.8284579), "PWM_Quarry_4x3x266", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (9850.056, 4451.3525, 1506.5156), (-0.9696656462730974, 42.56592114518197, 5.0051880662891355), (1.563263, 1.531985, 0.72845), "PWM_Quarry_4x3x267_56", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (9125.637, 3976.5457, 1655.665), (-9.797791092273066, 114.83474401565773, 176.20057043009578), (1.231647, 1.231647, 0.960097), "PWM_Quarry_4x3x268", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (10262.329, 4816.701, 1898.6997), (12.525240290318697, -19.043301461771364, 11.548998579353308), (1.463985, 1.231647, 0.960097), "PWM_Quarry_4x3x269", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2769.6594, 4084.5815, 1463.8887), (-0.02313233188140054, -150.2641322067538, -178.58461887021326), (1.0, 1.0, 1.0), "PWM_Quarry_4x3x27", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (10462.313, 4883.9697, 2153.2412), (4.710712314651763, -143.49755158551017, 167.19074968174056), (1.563263, 1.531985, 0.72845), "PWM_Quarry_4x3x270_64", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3735.5361, 5957.045, 772.62695), (-21.85202228620399, 171.17932515464653, 2.7414501587466136), (0.6303045, 0.6303045, 0.41351256), "PWM_Quarry_4x3x273", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3757.287, 5813.7017, 674.9502), (-21.85202228620399, 171.17932515464653, 2.7414501587466136), (0.630305, 0.630305, 0.413513), "PWM_Quarry_4x3x274", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5782.9062, 7084.0425, 722.65576), (-4.37835715399521, 40.05653116217637, 5.293609552624092), (1.0, 1.0, 1.0), "PWM_Quarry_4x3x275", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (9785.248, 5602.0137, 790.95264), (-0.58895870481907, -7.866576561198157, 4.590637522753443), (0.39241123, 0.39241123, 0.39241123), "PWM_Quarry_4x3x276", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (9961.451, 5840.7144, 768.5117), (-0.58895870481907, -7.866576561198157, 4.590637522753443), (0.392411, 0.392411, 0.392411), "PWM_Quarry_4x3x277", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (9998.188, 5927.5054, 726.02734), (-0.5889586193084452, -106.65875409113055, 4.5906368452217485), (0.392411, 0.392411, 0.392411), "PWM_Quarry_4x3x278", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (9460.598, 4523.343, 755.78125), (-0.58895870481907, -7.866576561198157, 4.590637522753443), (0.392411, 0.392411, 0.392411), "PWM_Quarry_4x3x279", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (687.6367, 6030.4985, 814.92334), (0.0, 62.374384903613965, -0.0), (1.0, 1.0, 0.72987807), "PWM_Quarry_4x3x28_414", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (9922.555, 5547.4517, 884.0176), (3.056543380496111, 117.07129028904744, -4.9251099006321235), (0.392411, 0.392411, 0.25835484), "PWM_Quarry_4x3x280", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (9863.518, 5513.6226, 832.14844), (3.0565438630791033, -175.4271768250523, -4.925109395687251), (0.392411, 0.392411, 0.258355), "PWM_Quarry_4x3x281", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (9754.623, 5557.364, 803.4995), (3.0565438630791033, -175.4271768250523, -4.925109395687251), (0.392411, 0.392411, 0.258355), "PWM_Quarry_4x3x282_341", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (10022.236, 5214.1846, 845.5215), (3.0565437893720433, 3.725799213119767, -4.925109637760068), (0.392411, 0.392411, 0.258355), "PWM_Quarry_4x3x283", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (9896.853, 5526.224, 888.8096), (3.0565435748054526, -171.8013277122076, -4.925109092685318), (0.31669423, 0.31669423, 0.18263817), "PWM_Quarry_4x3x284", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (8559.388, 9001.271, 681.57227), (5.949583602118067, -72.38632820906018, 3.4407098638465192), (0.9719204, 0.9719204, 0.72046065), "PWM_Quarry_4x3x285", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (7860.9644, 8599.438, 889.3623), (-5.723266306442466, -157.78109735153663, 2.083098481421626), (0.97192, 0.97192, 0.720461), "PWM_Quarry_4x3x286", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (10458.966, 8715.286, 645.70703), (17.8211199503946, 83.77612137872687, -24.861358093651493), (0.783559, 0.783559, 0.566767), "PWM_Quarry_4x3x287", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (11013.906, 8831.217, 739.2998), (5.630967424936372, 57.72256207655458, -22.903105031796066), (0.783559, 0.783559, 0.566767), "PWM_Quarry_4x3x288", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (10940.553, 8827.014, 694.7212), (18.60523634869834, 95.21766166179509, -14.700470353328468), (0.783559, 0.783559, 0.566767), "PWM_Quarry_4x3x289", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1045.0454, 635.13477, 1400.2861), (3.419834067421236, -147.8143598750048, 174.79002161717253), (1.0, 1.0, 0.7284503), "PWM_Quarry_4x3x29_26", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (10767.745, 10229.679, 842.2363), (-15.546753035686654, 148.03714116752786, -4.949614544390628), (0.783559, 0.783559, 0.566767), "PWM_Quarry_4x3x290", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (10212.057, 10263.343, 1231.1865), (-9.867493104943925, 160.46300748578395, -4.035705678490562), (0.783559, 0.783559, 0.8989398), "PWM_Quarry_4x3x291", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (10052.312, 10169.482, 991.979), (-10.910064830808679, 79.94055585371652, 7.8404225697328185), (0.783559, 0.783559, 0.63398886), "PWM_Quarry_4x3x292", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (9646.558, 9655.382, 844.3701), (-10.095460303448723, 79.12294808086132, 12.322474108234342), (0.783559, 0.783559, 0.633989), "PWM_Quarry_4x3x293", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (11110.742, 9049.016, 707.1987), (39.96309749159641, 108.74475064686797, -8.58713150016581), (0.783559, 0.783559, 0.3477726), "PWM_Quarry_4x3x294", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (10354.902, 8399.84, 774.14844), (23.503576855577954, 130.88507325518904, -14.18237380195732), (0.783559, 0.783559, 0.566767), "PWM_Quarry_4x3x295", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4732.9727, 4854.1562, 2239.3486), (3.7580238202104517, -31.343744027170032, 179.86556813761058), (0.903343, 0.959752, 0.451824), "PWM_Quarry_4x3x296", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (8577.381, 5498.9272, 3088.1543), (5.777116427502679, 140.37340599719698, -177.33159274855404), (1.231647, 1.231647, 0.960097), "PWM_Quarry_4x3x297", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1472.8463, 4031.3184, 687.6565), (-0.5180663998502194, 142.66612578811782, -3.261840546662578), (1.0, 1.0, 0.625877), "PWM_Quarry_4x3x298", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (8045.419, 5641.3027, 2879.961), (6.209898201775377, 87.9300833375612, 178.61494740102887), (1.6184461, 1.5615301, 0.6332454), "PWM_Quarry_4x3x299", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3034.9678, 4423.798, 1380.0859), (-3.7048935441087805, -148.02050479862785, 175.67629601556524), (1.0, 1.0, 1.0), "PWM_Quarry_4x3x30", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (7873.291, 8024.4873, 972.84424), (1.0244669963710855, 114.73474804931392, 2.6560061492756124), (1.0, 1.0, 0.913395), "PWM_Quarry_4x3x300_82", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (9062.3, 5424.892, 2905.023), (5.7771162472405635, 46.28442343756597, -177.3315930364046), (1.231647, 1.231647, 0.561101), "PWM_Quarry_4x3x301", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (9501.832, 5611.273, 2956.9946), (5.777116603782081, -98.25262667926472, -177.33159260687867), (1.231647, 1.231647, 0.561101), "PWM_Quarry_4x3x302", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (9800.884, 5188.576, 2588.79), (6.257147658857639, -94.21348280294104, 178.8339434682561), (1.563263, 1.531985, 0.72845), "PWM_Quarry_4x3x303", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (8009.1226, 5166.249, 2562.5088), (6.240046363781559, -157.77281921083966, 177.10884230245085), (1.563263, 1.531985, 0.72845), "PWM_Quarry_4x3x304", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (8007.648, 8150.2236, 760.18555), (2.7124928366121424, 28.151397761619695, -0.8632812187896695), (1.0, 1.0, 0.5640453), "PWM_Quarry_4x3x305", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5848.8896, 6958.369, 815.0542), (-5.488555721159454, 127.62608096368145, -4.131011616737537), (0.6384541, 0.6384541, 0.6384541), "PWM_Quarry_4x3x306", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (9981.455, 7817.4287, 696.03516), (0.0, -16.875030431075956, 0.0), (1.0, 1.0, 0.72845), "PWM_Quarry_4x3x307", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (9987.089, 7745.4746, 701.03516), (0.0, -160.00017681518196, 0.0), (0.672003, 0.672003, 0.7101386), "PWM_Quarry_4x3x308", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (9837.879, 7708.253, 753.4077), (0.0, 154.99986264890813, -0.0), (0.7564891, 0.7564891, 0.39565066), "PWM_Quarry_4x3x309", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2762.84, 4347.1016, 1622.7627), (2.5742573518743286, -100.04724296693898, -178.50336065407714), (1.0, 1.0, 1.0), "PWM_Quarry_4x3x31", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (7838.0317, 6952.3545, 843.0532), (0.0, -165.00003487916413, 0.0), (0.756489, 0.756489, 0.395651), "PWM_Quarry_4x3x310", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (7885.498, 7002.1406, 851.48236), (-3.767608699925736, 35.41788685421001, 0.16341497472050706), (0.756489, 0.756489, 0.395651), "PWM_Quarry_4x3x312", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (7597.2134, 7522.089, 1429.9307), (-0.9651793867996802, 114.64238505361236, 2.6560057419454846), (1.0, 1.0, 0.913395), "PWM_Quarry_4x3x313", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (10012.182, 7734.005, 809.5176), (-0.7605284519720145, 95.25175295202932, 1.466570851017732), (0.7565968, 1.0, 0.5291629), "PWM_Quarry_4x3x314", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1038.0518, 1143.2852, 2039.624), (1.7829624399270316, -133.31423759156732, -176.4718068787575), (1.0, 1.0, 0.729925), "PWM_Quarry_4x3x315", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2042.8086, 4755.5723, 681.5908), (-4.953766257090974, 23.22473256363309, -12.267639586005592), (1.2420801, 1.0, 0.625877), "PWM_Quarry_4x3x316", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2522.916, 4525.9365, 1833.5122), (-0.7479551005022157, -95.64663961449578, -176.11852886060709), (1.0, 1.0, 0.729925), "PWM_Quarry_4x3x317", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (682.624, 5815.369, 562.4712), (0.0, 62.374384903613965, -0.0), (1.0, 1.0, 0.729878), "PWM_Quarry_4x3x318_266", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2058.463, 4852.699, 2130.041), (6.626663404060836, -174.06601216720873, -178.4056390727079), (1.0, 1.1943152, 0.6202554), "PWM_Quarry_4x3x319", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2557.8762, 4287.1553, 1778.6143), (-0.9581905904246828, -96.25065475768936, -178.55375698776152), (1.0, 1.0, 1.0), "PWM_Quarry_4x3x32", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2252.2168, 4852.699, 2026.7212), (6.626670563585614, -117.31326733077927, -178.40563895084406), (1.0, 1.194315, 0.620255), "PWM_Quarry_4x3x320", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (9615.627, 5159.1313, 2458.0422), (16.339893618309983, -110.02848934221551, 173.39880081274254), (1.563263, 1.531985, 0.72845), "PWM_Quarry_4x3x321", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (9892.172, 5366.3877, 2466.349), (27.81479632355888, -94.69804788979022, 178.68937698949662), (1.563263, 1.531985, 0.72845), "PWM_Quarry_4x3x322_42", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (9872.199, 7830.665, 2677.0415), (2.79661705510205, 25.286435898676153, 175.38271678325376), (1.563263, 1.531985, 0.72845), "PWM_Quarry_4x3x323", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4507.627, 6542.4385, 1251.2979), (-1.713836648427963, -172.23416339936114, 0.653686519924658), (0.5147992, 0.4450214, 0.65421903), "PWM_Quarry_4x3x324", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (7873.2793, 7415.618, 2055.4165), (17.544798568513382, 120.5718616357631, 179.89711604505456), (1.0, 1.0, 1.0), "PWM_Quarry_4x3x325", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (7955.5884, 7757.382, 1048.7832), (-1.1259764057650141, 15.712431432156777, 2.3833949338745017), (1.0, 1.0, 0.783208), "PWM_Quarry_4x3x326", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1901.5508, 3794.7812, 814.92334), (0.0, 62.374384903613965, -0.0), (1.0, 1.0, 0.729878), "PWM_Quarry_4x3x327", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (7942.176, 7710.3433, 1835.3921), (-5.295350513832441, 12.158937148235314, -18.834196969395652), (1.0, 1.205925, 1.0), "PWM_Quarry_4x3x328", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1901.5508, 3456.2812, 949.73193), (0.0, 62.374384903613965, -0.0), (1.0, 1.0, 0.729878), "PWM_Quarry_4x3x329", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1510.6777, 4627.4375, 2018.126), (0.24866679334916966, -110.13847209266915, -176.05523046985857), (1.0, 1.0, 0.729925), "PWM_Quarry_4x3x33", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (11714.418, 10564.067, 1320.0028), (-1.4251097878677599, 2.624816884270237, -179.10191641895454), (1.815031, 1.214997, 1.214997), "PWM_Quarry_4x3x330", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (12168.897, 10560.682, 1321.8407), (-1.4251097878677599, 2.624816884270237, -179.10191641895454), (1.815031, 1.214997, 1.214997), "PWM_Quarry_4x3x331", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (9915.835, 6894.941, 3557.9868), (49.627112138204446, 121.78753248049003, 17.8965455002002), (3.403134, 1.531985, 0.72845), "PWM_Quarry_4x3x332", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (326.30127, 790.87695, 1420.6797), (-7.679424390553279e-08, -90.00011143952378, -8.308593280981137), (1.320233, 1.320233, 1.320233), "PWM_Quarry_4x3x333", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (326.30127, 790.87695, 2220.6797), (-7.679424390553279e-08, -90.00011143952378, -8.308593280981137), (1.320233, 1.320233, 1.320233), "PWM_Quarry_4x3x334", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1382.198, 1024.22, 1477.0709), (-0.02313233188140054, -150.2641322067538, -178.58461887021326), (1.0, 1.0, 1.0), "PWM_Quarry_4x3x335", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1616.5881, 3972.735, 905.5625), (0.49020658096162395, -155.66382310445258, 5.4774666296069645), (0.839889, 0.91978, 0.604777), "PWM_Quarry_4x3x336", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1393.9253, 3863.2175, 626.54346), (-2.673675571612515, 97.63007583221706, -1.9389036709479963), (1.0, 1.0, 0.625877), "PWM_Quarry_4x3x337", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1073.4282, 1410.0208, 578.1242), (-0.517913875613525, 64.613820659416, -3.2618409169023366), (1.0, 1.0, 0.625877), "PWM_Quarry_4x3x338", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1045.8699, 1257.265, 796.0302), (0.4902069861156737, 126.28338253228294, 5.477652242730936), (0.839889, 0.91978, 0.604777), "PWM_Quarry_4x3x339", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2525.7363, 4731.6846, 2084.3643), (-0.2959289661360315, -150.5306351824867, -179.0397393688694), (1.0, 1.0, 0.729925), "PWM_Quarry_4x3x34", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (892.6311, 1452.4335, 565.37067), (-2.673553743162996, 19.57757655585244, -1.9389036720693196), (1.0, 1.0, 0.625877), "PWM_Quarry_4x3x340", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1311.0543, 2106.1543, 578.1242), (-0.5179139598483641, 110.5863537613327, -3.2618406337887618), (1.0, 1.0, 0.625877), "PWM_Quarry_4x3x341", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1401.732, 1980.1729, 796.0302), (0.4902025769282275, 172.25514329108955, 5.477826723210542), (0.839889, 0.91978, 0.604777), "PWM_Quarry_4x3x342", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1154.9033, 2005.6387, 565.37067), (-2.6735539017399175, 65.54968524555956, -1.9388734020703922), (1.0, 1.0, 0.625877), "PWM_Quarry_4x3x343", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (829.4833, 2891.432, 2464.9019), (-0.2959595206218581, -40.24514680800267, -179.03973943475515), (1.0, 1.0, 0.729925), "PWM_Quarry_4x3x344", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (919.09094, 2996.8682, 2375.7554), (0.24866667708210702, -29.6947631574745, -176.0551830026524), (1.0, 1.0, 0.729925), "PWM_Quarry_4x3x345", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1013.7418, 2169.5422, 2502.1372), (1.744095411019498, -83.2652493057055, 175.97580154882652), (1.0, 1.0, 1.0), "PWM_Quarry_4x3x346", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1063.1022, 2001.938, 2416.7954), (-5.703186294482321, -123.54134510938805, 175.85524722983598), (1.0, 1.0, 1.0), "PWM_Quarry_4x3x347", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1532.209, 3322.6033, 1964.271), (-0.2959595007202444, -52.638372616157596, -179.03973950404082), (1.0, 1.0, 0.729925), "PWM_Quarry_4x3x348", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1764.6573, 3406.3525, 1645.4622), (3.0796700928488545, -42.16241385648535, -178.61577399374548), (1.7372384, 1.7372384, 1.4671636), "PWM_Quarry_4x3x349", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2863.213, 4630.2666, 2044.0337), (1.6523122385483127, -79.82384517471557, -176.58098942363395), (1.0, 1.0, 0.8599663), "PWM_Quarry_4x3x35", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1557.2423, 2577.991, 1771.844), (1.744095798588978, -95.65795061236587, 175.9758013913701), (1.0, 1.0, 1.0), "PWM_Quarry_4x3x350", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1569.4819, 2403.6987, 1686.5022), (-5.703185704237944, -135.9341223779905, 175.85524747036413), (1.0, 1.0, 1.0), "PWM_Quarry_4x3x351", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1242.0363, 1922.9973, 2037.3003), (2.5533019034067177, -69.10217435988845, 175.09225967363508), (1.0, 1.0, 0.729925), "PWM_Quarry_4x3x352", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1181.3209, 4582.173, 2346.8345), (-2.80062922824423, -101.60828023555135, 168.98034678835342), (1.1838411, 1.1838411, 0.91376615), "PWM_Quarry_4x3x353", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (707.5528, 4262.335, 2304.3213), (-0.5359493867276454, -125.9987555374006, 171.6561962896621), (1.1838411, 1.3781557, 0.8040962), "PWM_Quarry_4x3x354", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (882.2947, 4434.0728, 2207.9468), (10.904976758771953, -70.4910315676211, 169.99438248273435), (1.1838411, 1.3781557, 0.8040962), "PWM_Quarry_4x3x355", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (937.694, 1894.8765, 549.2209), (27.331671391504763, 171.59307641880537, -0.5984497679443179), (1.0, 1.0, 0.783208), "PWM_Quarry_4x3x356", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (146.30127, 790.87695, 1165.6797), (3.6638360685732247, 90.41830411801541, 178.21021229646698), (1.320233, 1.5534505, 1.320233), "PWM_Quarry_4x3x357", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (113.55884, 845.87695, 2020.6797), (-9.372009217699906, 90.42303777746903, 178.11452963492664), (1.320233, 1.55345, 1.320233), "PWM_Quarry_4x3x358", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2342.916, 4310.9365, 1833.5122), (-0.7479551005022157, -95.64663961449578, -176.11852886060709), (1.0, 1.0, 0.729925), "PWM_Quarry_4x3x359", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2721.1963, 4674.3086, 2084.9297), (2.7917161983571956, 65.75315300910027, 176.99292233828874), (1.0, 1.0, 0.859966), "PWM_Quarry_4x3x36", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (9747.021, 4322.566, 1406.1421), (-0.5889892771104545, 42.57152885997572, 4.590636341434137), (1.563263, 1.531985, 1.344814), "PWM_Quarry_4x3x360", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (7767.297, 7634.4043, 1347.4297), (-3.9172057508460587, 49.25894193194056, -0.7340697754427584), (1.0, 1.0, 0.913395), "PWM_Quarry_4x3x361", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (12123.8545, 10538.595, 2430.9263), (6.730002418163916, 55.50655607911756, -0.6708679067033698), (1.3640896, 1.3640896, 1.3640896), "PWM_Quarry_4x3x362", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (12319.089, 9380.664, 2290.0847), (-0.14865109280135308, -67.11385636447008, -178.19262248585943), (1.3640896, 1.3640896, 1.3640896), "PWM_Quarry_4x3x363", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (12252.349, 10310.111, 2274.0952), (2.755155373339042, 99.81214824541074, -172.72019715072642), (1.3640896, 1.3640896, 1.3640896), "PWM_Quarry_4x3x364", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (12231.136, 9549.609, 2319.1624), (2.820888611177142, 61.75225551603227, 0.586023920256529), (1.3640896, 1.3640896, 1.3640896), "PWM_Quarry_4x3x365", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (12268.0, 10001.647, 2325.4866), (-6.833189601574518, -178.78612944250185, -179.17380626361378), (1.3640896, 1.6233076, 1.3640896), "PWM_Quarry_4x3x366", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (11964.007, 9683.916, 2483.6665), (2.8208890242121996, 61.75225552651188, 0.5860239001098595), (1.36409, 1.36409, 1.36409), "PWM_Quarry_4x3x367", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (11572.64, 9653.557, 2389.1472), (0.5016910667327338, 129.99153724270002, 2.837102409804256), (1.36409, 1.36409, 1.36409), "PWM_Quarry_4x3x368", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (11708.443, 9650.352, 2197.1992), (-4.530608095646875, 160.21584177162586, -174.26067137541415), (1.0, 1.0, 1.0), "PWM_Quarry_4x3x369", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2485.7812, 6325.5806, 861.63135), (-3.610900405487545, 34.9318214210707, 3.2967798599361275), (1.0, 1.291828, 1.0), "PWM_Quarry_4x3x37", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (11935.532, 10514.522, 1613.0948), (-1.6632995741578993, 25.804226051645387, 170.67163986510806), (1.815031, 1.214997, 0.6673857), "PWM_Quarry_4x3x370", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (11541.42, 8813.981, 860.8447), (19.61537856594495, 83.35939681244199, 158.95311477792438), (1.0, 1.0, 0.72845), "PWM_Quarry_4x3x371", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (11814.281, 8949.619, 715.3281), (-28.860354339964577, -98.68149051258612, 13.177559584410425), (0.783559, 0.783559, 0.566767), "PWM_Quarry_4x3x372", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (11834.96, 8702.697, 944.8926), (-34.94796147402546, -64.56139064175397, -3.1240836182257135), (1.0598105, 1.0598105, 0.8430185), "PWM_Quarry_4x3x373", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (11900.606, 9061.119, 649.4165), (19.694258321431388, 52.95184487173048, -25.077821115916784), (0.783559, 0.783559, 0.566767), "PWM_Quarry_4x3x374", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (11698.543, 9082.569, 645.70703), (17.821121677552487, 53.021447254933655, -24.860532876546944), (0.783559, 0.783559, 0.566767), "PWM_Quarry_4x3x375", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (11380.841, 10400.933, 1861.5251), (0.879318369740755, -120.35246118162607, 177.70790156875228), (1.0, 1.473788, 1.0), "PWM_Quarry_4x3x376", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (12476.435, 9380.664, 2290.0854), (-0.14865109280135308, -67.11385636447008, -178.19262248585943), (1.36409, 1.36409, 1.36409), "PWM_Quarry_4x3x377", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (12409.694, 10310.111, 2274.096), (2.7551564616383106, 99.81214839072058, -172.72019657632103), (1.36409, 1.36409, 1.36409), "PWM_Quarry_4x3x378", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (12388.481, 9549.609, 2319.163), (2.8208890242121996, 61.75225552651188, 0.5860239001098595), (1.36409, 1.36409, 1.36409), "PWM_Quarry_4x3x379", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2592.912, 6412.8765, 1548.7534), (-5.060607378704686, 131.40831581976187, -0.7763673978836145), (1.0, 1.0, 1.0), "PWM_Quarry_4x3x38", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (12425.346, 10001.647, 2325.4873), (-6.833189601574518, -178.78612944250185, -179.17380626361378), (1.36409, 1.623308, 1.36409), "PWM_Quarry_4x3x380", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (12292.448, 9006.099, 2389.122), (2.8208890242121996, 61.75225552651188, 0.5860239001098595), (1.5856746, 1.5856746, 1.5856746), "PWM_Quarry_4x3x381", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (10692.014, 6997.8657, 934.5796), (15.779189158110231, -151.6069344995987, 157.01146383878728), (0.87266827, 1.0712218, 0.81200373), "PWM_Quarry_4x3x382", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (10692.014, 7135.6157, 1450.0006), (15.779189158110231, -151.6069344995987, 157.01146383878728), (0.872668, 1.071222, 0.812004), "PWM_Quarry_4x3x383", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (10709.656, 7082.4736, 1737.4935), (5.264462622011934, 127.51117869318333, 175.29059077541018), (0.872668, 1.071222, 0.4307278), "PWM_Quarry_4x3x384", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (10842.105, 6943.3896, 1892.7537), (5.264463204107242, 89.24065247026323, 175.29058999389045), (0.872668, 1.071222, 0.430728), "PWM_Quarry_4x3x385", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (10842.105, 6455.83, 1958.4669), (5.264462417192385, 89.24065246738184, 175.29059018377615), (0.872668, 1.071222, 0.430728), "PWM_Quarry_4x3x386", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (10842.105, 6273.157, 1863.5771), (5.264463526162345, 169.2883038101921, 175.29059077639207), (0.872668, 1.071222, 0.430728), "PWM_Quarry_4x3x387", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (10872.578, 6299.1763, 1738.1016), (5.264462890404105, -156.35995516432038, 175.2905911685708), (1.238164, 1.436718, 0.79622394), "PWM_Quarry_4x3x388", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (11063.692, 6603.085, 2294.024), (5.264462380850463, 134.39710887030375, 175.29059102119982), (1.238164, 1.436718, 0.796224), "PWM_Quarry_4x3x389", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2212.0312, 6374.4478, 2108.6748), (0.42393199122067987, 31.88795706047323, -176.5529661124317), (1.0, 1.0, 1.0), "PWM_Quarry_4x3x39", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (9747.021, 3956.143, 1406.1421), (-0.5889892771104545, 42.57152885997572, 4.590636341434137), (1.563263, 1.531985, 1.344814), "PWM_Quarry_4x3x390", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (9641.462, 4219.487, 1409.6677), (-0.9696656462730974, 42.56592114518197, 5.0051880662891355), (1.563263, 1.531985, 1.2781732), "PWM_Quarry_4x3x391", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (9533.024, 4411.0566, 2296.859), (-4.743132701173192, -155.2240019007937, -16.514219400710136), (1.563263, 1.531985, 0.8368947), "PWM_Quarry_4x3x392", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2351.8462, 4599.749, 802.58136), (-2.6396485444610907, -168.30386961893737, 8.359593795773293), (0.839889, 0.91978, 0.604777), "PWM_Quarry_4x3x393", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4193.098, 4735.479, 922.6663), (-2.3690174165782607, -123.06236686665729, 170.1290183262229), (0.59065, 0.59065, 0.508989), "PWM_Quarry_4x3x394", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4393.839, 4700.1763, 1140.2784), (3.405524970536033, -124.06738015296226, 170.11970954573715), (0.59065, 0.59065, 0.508989), "PWM_Quarry_4x3x395", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (8852.561, 5471.346, 2885.1506), (7.67835703618981, 88.3156392864034, -179.9124036905444), (1.231647, 1.231647, 0.561101), "PWM_Quarry_4x3x396", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (9201.045, 5570.2886, 2900.398), (1.1690013615726145, 6.364653610861739, 172.4095170977619), (1.231647, 1.231647, 0.561101), "PWM_Quarry_4x3x397", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (8414.026, 5634.207, 3109.6138), (5.777115670484115, 140.37340597300718, -177.3315924751034), (1.7116781, 1.231647, 0.960097), "PWM_Quarry_4x3x398", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (191.77153, 1174.3242, 3021.0688), (-85.57431570822341, 114.95308877952608, 148.09920607164204), (1.320233, 1.55345, 1.320233), "PWM_Quarry_4x3x399", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2229.1172, 6471.467, 1475.648), (-0.02313231778434078, 18.027899188698896, -178.5846189814643), (1.0, 1.0, 1.0), "PWM_Quarry_4x3x40", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (169.54108, 2057.8623, 3067.2434), (-86.84673415395046, 136.78196405735105, 134.3833344356824), (1.320233, 1.55345, 1.320233), "PWM_Quarry_4x3x400", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (169.54108, 3049.208, 3067.2434), (-86.84673415395046, 136.78196405735105, 134.3833344356824), (1.320233, 1.55345, 1.320233), "PWM_Quarry_4x3x401", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (169.54108, 4035.9473, 3067.2434), (-86.84673415395046, 136.78196405735105, 134.3833344356824), (1.320233, 1.55345, 1.320233), "PWM_Quarry_4x3x402", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (169.54108, 5015.708, 3067.2434), (-86.84673415395046, 136.78196405735105, 134.3833344356824), (1.320233, 1.55345, 1.320233), "PWM_Quarry_4x3x403", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (169.54108, 5743.3223, 3067.2434), (-86.84673415395046, 136.78196405735105, 134.3833344356824), (1.320233, 1.55345, 1.320233), "PWM_Quarry_4x3x404", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (81.90967, 904.6517, 2584.5117), (-9.371825355813598, 89.57404701183515, -176.67599029752745), (1.320233, 1.55345, 1.320233), "PWM_Quarry_4x3x405", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (7973.302, 7125.5835, 741.70026), (-3.7676086255070156, 35.41788684827221, 0.16341511896259286), (0.756489, 0.756489, 0.395651), "PWM_Quarry_4x3x406", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (11655.084, 6395.6313, 1738.1016), (5.264462665647032, -156.35995515386875, 175.29059112125125), (1.238164, 1.436718, 0.796224), "PWM_Quarry_4x3x407", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2763.8135, 6258.1562, 830.16797), (-7.632292775943792, 59.07826705456775, -176.02032785708852), (1.0, 1.0, 0.72845), "PWM_Quarry_4x3x41", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1408.2793, 5805.9727, 2311.5996), (-0.295928906456607, 52.454658125985254, -179.03973967306158), (1.0, 1.0, 0.729925), "PWM_Quarry_4x3x42", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1298.7383, 5890.5146, 2222.4531), (0.24866673870251849, 63.00507057442425, -176.05523068979656), (1.1315138, 1.1603336, 0.729925), "PWM_Quarry_4x3x43", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2120.6914, 6024.0293, 2348.835), (1.7441013872703546, 9.434357477729144, 175.97580201028842), (1.0, 1.0, 1.0), "PWM_Quarry_4x3x44", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2285.7852, 6081.2285, 2263.4932), (-5.703185549984828, -30.841426911929446, 175.85524692301703), (1.0, 1.0, 1.0), "PWM_Quarry_4x3x45_101", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2014.915, 6249.9077, 2187.9443), (0.6443670764749853, -161.24677337176118, -177.201939993158), (1.0, 1.0, 1.0), "PWM_Quarry_4x3x46", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1816.0127, 6351.13, 2038.4331), (0.6443669880390188, 0.7728576220529849, -177.2019395536686), (1.0, 1.0, 1.0), "PWM_Quarry_4x3x47", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1018.97656, 6065.353, 2035.4062), (0.644366885384474, -130.4744364469408, -177.20193952357747), (1.0, 1.0, 1.0), "PWM_Quarry_4x3x48", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (825.9844, 5681.851, 2425.3672), (-0.29592897416723946, 21.486209057204743, -179.03973946472854), (1.0, 1.0, 0.729925), "PWM_Quarry_4x3x49_118", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3328.5889, 6481.071, 2083.1445), (0.10976114656009171, 57.73494920368497, -177.83040406585138), (1.0, 1.0, 1.0), "PWM_Quarry_4x3x50_136", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3292.1416, 6598.974, 1475.648), (-0.02313237613044769, 35.521760222588966, -178.58461903651235), (1.0, 1.0, 1.0), "PWM_Quarry_4x3x51", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3958.0674, 6446.698, 729.8823), (8.452596798742597, -42.744750663668306, -178.00000509599144), (1.0, 1.0, 0.72845), "PWM_Quarry_4x3x52_142", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4251.7188, 6611.471, 1095.3721), (6.3827575647993635, -99.0216017493038, 174.09869017370306), (1.0, 1.0, 0.72845), "PWM_Quarry_4x3x53", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3806.4092, 6612.0845, 1305.2993), (1.72100279590097, -152.70897031827542, 171.64745249077203), (1.0, 1.0, 0.72845), "PWM_Quarry_4x3x54", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3803.4512, 6508.279, 1916.6309), (-1.9314885177064847, -120.63878675894529, 178.7717789633358), (1.0, 1.0, 0.72845), "PWM_Quarry_4x3x55", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5689.6646, 7203.426, 2034.1709), (1.6210633482998782, -147.43944446287048, -175.0365470002248), (1.0, 1.0, 1.0), "PWM_Quarry_4x3x56_152", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3597.6572, 5903.3833, 616.12256), (-7.8861696612431835, 89.04275799842479, 13.429591009967169), (1.0, 1.0, 0.783208), "PWM_Quarry_4x3x57", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4994.634, 6748.6577, 544.5669), (27.255633421688863, -56.57061174328507, 3.4739042052028717), (1.0, 1.0, 0.783208), "PWM_Quarry_4x3x58", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4904.6426, 6931.551, 751.7534), (8.450239670848124, -92.8422156491575, -9.696776261740842), (1.0, 1.0, 0.60943896), "PWM_Quarry_4x3x59_172", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3370.498, 5940.2305, 609.6582), (-2.449004498334173, -156.03084932633377, -15.971373744749595), (1.0, 1.0, 0.609439), "PWM_Quarry_4x3x60", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3979.1035, 6490.0874, 2086.788), (4.912148030519254, 130.3282090985398, 178.822816294705), (1.0, 1.0, 0.72845), "PWM_Quarry_4x3x61", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3500.4795, 6416.427, 2098.4346), (4.424089937140899, 68.4573937418976, 178.35789120681866), (1.0, 1.0, 0.72845), "PWM_Quarry_4x3x62", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3058.6553, 6172.2017, 2374.3428), (0.6698480089053744, -87.46117617961967, 179.90196631104956), (1.0, 1.0, 1.0), "PWM_Quarry_4x3x63", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3335.9863, 6223.6523, 2348.9336), (0.6698479655781521, 86.67159775932541, 179.9019663257105), (1.0, 1.0, 1.0), "PWM_Quarry_4x3x64", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2513.0645, 5732.1914, 2488.7373), (0.6698479655781521, 86.67159775932541, 179.9019663257105), (1.1104032, 1.1904488, 1.0), "PWM_Quarry_4x3x65", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2685.9229, 6270.704, 2179.0874), (0.669847993049699, 46.22210432887843, 179.90196628095254), (1.0, 1.0, 1.0), "PWM_Quarry_4x3x66", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4795.469, 6612.2964, 2312.495), (-0.2959289640311834, 66.65390181822751, -179.03973950526728), (1.0, 1.0, 0.729925), "PWM_Quarry_4x3x67", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3661.7207, 4444.8525, 1927.6001), (2.5742571166900006, -100.04724296382672, -178.50336055197107), (1.0, 1.0, 1.0), "PWM_Quarry_4x3x68_242", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4112.6904, 6660.3584, 1498.7485), (0.0, -98.42166792402612, 0.0), (1.0, 1.0, 1.0), "PWM_Quarry_4x3x69_80", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5057.043, 7240.8047, 2039.3281), (0.6443668169034752, 14.97198349963115, -177.2019258138525), (1.0, 1.0, 1.0), "PWM_Quarry_4x3x70", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4463.4297, 6729.267, 2115.0137), (0.6443668834661359, -116.27597263611327, -177.2019396078601), (1.0, 1.0, 1.0), "PWM_Quarry_4x3x71", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4661.3037, 6857.569, 2226.462), (0.941705287447129, 97.6999739099119, -179.64900953214064), (1.0, 1.0, 1.0), "PWM_Quarry_4x3x72", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4255.8945, 6518.4014, 2169.5566), (0.6698479980291474, 68.56494305940694, 179.90196625350694), (1.0, 1.0, 0.72845), "PWM_Quarry_4x3x73", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4091.5898, 6326.4453, 2348.9336), (3.1825873538875786, 86.64244120076843, 177.8622037769378), (1.0, 1.0, 1.0), "PWM_Quarry_4x3x74", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4551.286, 5329.3936, 595.3506), (-16.475401822967658, -140.10368218932422, 12.490695191404077), (1.0, 1.0, 0.783208), "PWM_Quarry_4x3x75", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4328.5312, 5150.505, 541.9453), (21.606401386548896, 112.86202814405227, 6.64087566349649), (1.0, 1.0, 0.783208), "PWM_Quarry_4x3x76", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (11019.734, 7376.1177, 1419.7852), (3.5822704095602877, 50.48672172247563, -2.080871434404496), (1.0, 1.0, 1.0), "PWM_Quarry_4x3x77", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4760.387, 5227.9824, 637.36523), (-2.4488827796433252, 12.696760898008502, -15.972441579065265), (1.0, 1.0, 0.609439), "PWM_Quarry_4x3x78", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4520.747, 6814.3516, 652.18066), (0.8409054808889813, -12.36959650742447, 1.279419193891943), (1.0, 1.0, 1.0), "PWM_Quarry_4x3x79_57", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3740.9922, 6402.517, 2282.6519), (4.0778406151021676, -169.49639466292626, -179.324053193814), (1.0, 1.0, 1.0), "PWM_Quarry_4x3x80_85", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3366.3887, 6587.0796, 1173.9731), (0.10976114656009171, 57.73494920368497, -177.83040406585138), (1.0, 1.0, 1.0), "PWM_Quarry_4x3x81_98", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5679.7095, 7282.4355, 2081.9883), (0.4239292741049097, 39.443900775101795, -176.55296569515642), (1.0, 1.0, 1.0), "PWM_Quarry_4x3x82", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (10871.291, 7273.5664, 701.2002), (-7.63226152726839, -21.766568664616813, -176.02032764149078), (1.0, 1.0, 0.72845), "PWM_Quarry_4x3x83", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (6146.521, 7334.1157, 1349.166), (2.6483712732681837, -142.76683355534323, 176.14734070435836), (1.0, 1.0, 0.72845), "PWM_Quarry_4x3x84", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (7743.1016, 8348.525, 830.4868), (0.1207647455639587, -74.77130031952743, 176.57711504381928), (1.0, 1.0, 1.084475), "PWM_Quarry_4x3x85_429", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5802.098, 7376.676, 1392.728), (-2.7483519402525145, 15.745449693977617, 1.9690355865617593), (1.0, 1.0, 0.783208), "PWM_Quarry_4x3x86", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (6505.9644, 6982.1426, 2644.4023), (4.912148273776368, 123.1803072959835, 178.82281629689805), (1.0, 1.0, 0.72845), "PWM_Quarry_4x3x87", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (7016.287, 7159.198, 2672.6284), (0.644367015434637, -123.42421351235082, -177.20193958718846), (1.0, 1.0, 1.0), "PWM_Quarry_4x3x88", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (6973.4854, 7110.6025, 2598.1924), (0.6698433421280536, -125.3804338237663, 179.9019526250215), (1.0, 1.0, 0.72845), "PWM_Quarry_4x3x89", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (6855.8276, 6976.009, 2055.4165), (0.6698480037058749, 120.60144590537602, 179.90196632018652), (1.0, 1.0, 1.0), "PWM_Quarry_4x3x90", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (6125.6816, 4582.9146, 1150.4365), (-6.724091167413549, -40.95691075068314, 177.0944338645436), (1.0, 1.0, 0.72845), "PWM_Quarry_4x3x91_111", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (6598.6357, 7135.957, 2188.8887), (4.6323571037103655, -53.887138408468616, -178.9747676624149), (1.0, 1.0, 0.72845), "PWM_Quarry_4x3x92", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5778.7734, 4572.6465, 2197.1528), (-0.7583617923050687, 49.129605816175484, -176.38454249730134), (1.0, 1.0, 1.0), "PWM_Quarry_4x3x93", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (6357.979, 7234.5415, 1561.9775), (1.571838291882459, 36.81329642045631, 176.92114787043104), (1.2394303, 1.0, 1.0), "PWM_Quarry_4x3x94", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (6938.1367, 7067.7725, 1048.7832), (-1.1259764057650141, 15.712431432156777, 2.3833949338745017), (1.0, 1.0, 0.783208), "PWM_Quarry_4x3x95", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5994.15, 4759.439, 2242.872), (2.1365513406738543, -126.04653929066535, 179.20561531142897), (1.0, 1.0, 0.72845), "PWM_Quarry_4x3x96", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (7685.6685, 4529.85, 1474.9409), (-0.9674681516277132, -157.7024583574999, 176.92193930061538), (1.23943, 1.0, 1.0), "PWM_Quarry_4x3x97", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4435.579, 4897.987, 621.5342), (25.937068281797497, 114.81251418515293, 2.414793611462114), (1.0, 1.0, 0.783208), "PWM_Quarry_4x3x98", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4423.3594, 4376.613, 2174.1597), (1.3665154447792183, -155.16843415105006, -177.8749445162668), (1.0, 1.0, 1.0), "PWM_Quarry_4x3x99", _folder)
if a: placed += 1
else: skipped += 1

# Batch 37: StaticMesh'PWM_Quarry_4x3x10_B' (33 instances)
_mesh_path = "/Game/Unshippable/Whitebox/Rocks/Meshes/PWM_Quarry_4x3x10_B"
_materials = ['/Game/Environments/ProcTexturing/ProcMaterial_Quarry_Atlas_A']
_folder = "Reconstruction/BD_BB_Chapter5_BalrogsNest/Meshes"
a = spawn_static_mesh(_mesh_path, _materials, (10447.13, 6349.947, 2474.2095), (25.890395396950908, 101.78401024433816, 51.286907499085046), (1.0, 0.8427937, 1.3399757), "PWM_Quarry_4x3x10_B14", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (10195.25, 6084.1826, 2523.1953), (14.392005440021418, -31.621912000748114, 138.32101365149862), (1.0, 1.0, 1.1488035), "PWM_Quarry_4x3x10_B15", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (10251.211, 7458.8057, 2388.1455), (15.394675415287267, -84.16907055087871, 151.19499038597317), (1.0, 1.0, 1.148803), "PWM_Quarry_4x3x10_B16_82", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (9720.578, 7386.6904, 2693.294), (52.98435969213188, -54.81614694802965, 140.9187297386956), (1.0, 1.0, 1.148803), "PWM_Quarry_4x3x10_B18", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (10610.038, 6140.7217, 2029.8218), (0.15189180315121462, -20.500489448243325, 165.9007808285295), (1.0, 1.0, 1.148803), "PWM_Quarry_4x3x10_B19_106", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (10077.771, 8139.913, 2647.498), (52.50672390893382, -33.68078622366356, -7.026673268265085), (1.0, 1.0, 1.0), "PWM_Quarry_4x3x10_B22", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (10733.065, 8499.055, 1978.251), (17.39430414235029, 14.621429196845323, 18.1817095925242), (1.4223312, 1.0987908, 1.2074736), "PWM_Quarry_4x3x10_B24", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (10474.357, 6146.302, 2313.9912), (-2.8541559001165266, -54.74718870780138, 138.28284902480647), (1.0, 1.0, 1.141495), "PWM_Quarry_4x3x10_B26", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (10195.525, 7252.9766, 2602.517), (42.69537855219408, 23.085710281183115, 27.789207825372333), (1.0, 0.842794, 1.2625486), "PWM_Quarry_4x3x10_B29_115", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (10184.693, 7023.1055, 2607.3867), (15.61334675377167, -91.54077754592375, 127.6249136449505), (1.0, 1.0, 1.1984724), "PWM_Quarry_4x3x10_B30", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (10044.453, 5661.6143, 2724.254), (4.273042081502856, 112.48167631377271, 75.72889176658474), (1.0, 1.0, 1.0), "PWM_Quarry_4x3x10_B33", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (10034.234, 5104.5654, 2061.208), (6.5801143292020905, -141.9209980229961, 141.81434917399454), (1.4820371, 1.0, 1.3218304), "PWM_Quarry_4x3x10_B4_201", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (9326.613, 9305.102, 1313.6963), (3.085398507004246, -149.0483253861611, -20.334898131390677), (1.0, 1.0, 1.229587), "PWM_Quarry_4x3x10_B42", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (6204.106, 6933.2754, 850.46387), (-56.05205135800411, 95.28601207750386, -139.20721680297677), (1.0, 1.0, 1.036157), "PWM_Quarry_4x3x10_B43_276", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (9714.94, 4631.5674, 1940.877), (12.971867366770283, -73.3055885208749, 138.86546173176143), (1.0, 1.0, 1.0), "PWM_Quarry_4x3x10_B45_41", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (9696.841, 8549.658, 2829.5508), (79.41217068437828, -46.857261011413904, -16.40654257825129), (1.6726056, 1.6726056, 1.6726056), "PWM_Quarry_4x3x10_B47", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (9339.557, 7950.341, 2907.7031), (27.614236232529798, -105.58348880462451, 101.92499753968326), (1.672606, 1.262155, 1.672606), "PWM_Quarry_4x3x10_B48", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (9116.172, 8367.778, 2764.733), (7.27695913876769, -125.32119030518108, 85.14887723806132), (1.283143, 1.283143, 1.283143), "PWM_Quarry_4x3x10_B49_305", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (10716.008, 5829.2627, 1895.1846), (1.626145893344755, -28.283964393995277, 146.01335126093082), (1.691135, 1.0, 0.9754826), "PWM_Quarry_4x3x10_B5", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (9282.176, 8513.988, 2737.6777), (51.460606593413644, 77.49564136869078, 114.48083882678517), (1.283143, 1.283143, 1.283143), "PWM_Quarry_4x3x10_B50", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (8517.713, 8778.717, 2330.417), (18.88409170284869, 93.81023910832826, 161.66404838526907), (0.9941802, 0.9941802, 0.86519647), "PWM_Quarry_4x3x10_B51", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (9577.767, 7735.5566, 2711.3862), (49.92018519170186, -91.92883455775547, 114.09014854510473), (1.4978204, 1.283143, 1.5143785), "PWM_Quarry_4x3x10_B52", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (10955.043, 5376.0146, 2068.087), (44.196868235552756, 10.316276548010958, 145.2601193004264), (1.49782, 1.6326785, 1.4173181), "PWM_Quarry_4x3x10_B53", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (10184.82, 7644.417, 2386.462), (-4.955780703204952, 37.00701975848047, 45.17787741329739), (1.0, 0.842794, 1.262549), "PWM_Quarry_4x3x10_B54", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (506.44043, 1391.6162, 2291.3633), (19.03182952634727, -177.38689998454922, 107.02459340703147), (1.6723431, 1.0, 1.0), "PWM_Quarry_4x3x10_B55_423", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (9854.817, 7552.711, 2646.7876), (40.555060316669845, -65.17221086031944, 137.81804712819513), (1.49782, 1.283143, 1.6309502), "PWM_Quarry_4x3x10_B56", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (10429.714, 5741.37, 2342.498), (51.46133554793745, 41.42107266996199, 159.77021292652893), (1.1511799, 1.2860389, 1.0706779), "PWM_Quarry_4x3x10_B57", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (10426.298, 5571.2285, 2342.106), (59.99217068874328, 35.04191518947207, 154.48279431066175), (0.9594464, 1.0943055, 1.1963296), "PWM_Quarry_4x3x10_B58", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (10460.224, 8296.701, 2328.5884), (28.89250788366283, -84.37943662781106, 134.67319836858547), (1.2410549, 1.3759139, 1.3440152), "PWM_Quarry_4x3x10_B59", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (10493.202, 5409.2085, 2207.1772), (50.47936201649534, -7.888365685443194, 116.3049431515002), (0.87063533, 1.664637, 0.975483), "PWM_Quarry_4x3x10_B6", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (456.44043, 2191.6162, 2441.3633), (19.03182986172391, 2.6135563600203664, 107.02484334327126), (1.672343, 1.0, 1.0), "PWM_Quarry_4x3x10_B60", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (10780.804, 5179.962, 2072.9102), (54.23151350091878, -33.704716276812526, 92.87374926554874), (0.870635, 1.664637, 0.975483), "PWM_Quarry_4x3x10_B7", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (7818.3535, 5357.6436, 786.9512), (-66.70189983255379, 178.38685447762631, 3.8724218278630342), (0.7776946, 0.6315566, 0.6114816), "PWM_Quarry_4x3x10_B9", _folder)
if a: placed += 1
else: skipped += 1

# Batch 38: StaticMesh'PWM_Quarry_4x3x10_C' (3 instances)
_mesh_path = "/Game/Unshippable/Whitebox/Rocks/Meshes/PWM_Quarry_4x3x10_C"
_materials = ['/Game/Environments/ProcTexturing/ProcMaterial_Quarry_Atlas_A']
_folder = "Reconstruction/BD_BB_Chapter5_BalrogsNest/Meshes"
a = spawn_static_mesh(_mesh_path, _materials, (10282.338, 7023.8438, 2653.1768), (-11.630523642803784, 111.16722479225395, 16.202695805425606), (1.0, 1.0, 1.0), "PWM_Quarry_4x3x10_C3_89", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (8426.53, 4913.989, 2398.1064), (14.66907147748255, 90.00004055080092, -179.99998704536353), (1.0, 1.2828637, 0.6169447), "PWM_Quarry_4x3x10_C8_37", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (7962.395, 4902.283, 2338.8408), (14.66907147748255, 90.00004055080092, -179.99998704536353), (1.0, 1.348711, 0.616945), "PWM_Quarry_4x3x10_C9", _folder)
if a: placed += 1
else: skipped += 1

# Batch 39: StaticMesh'PWM_Quarry_4x4x4_A' (33 instances)
_mesh_path = "/Game/Unshippable/Whitebox/Rocks/Meshes/PWM_Quarry_4x4x4_A"
_materials = ['/Game/Environments/ProcTexturing/ProcMaterial_Quarry_Atlas_2']
_folder = "Reconstruction/BD_BB_Chapter5_BalrogsNest/Meshes"
a = spawn_static_mesh(_mesh_path, _materials, (9664.058, 10144.089, 1012.1924), (0.0, 132.5333785252852, -0.0), (1.3703244, 1.3703244, 1.3703244), "PWM_Quarry_4x4x4_A_610", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1692.1267, 1729.3295, 867.6355), (-5.747009167758839, -72.42023634655347, 1.9143615223522685), (1.5561498, 1.5632219, 1.5561498), "PWM_Quarry_4x4x4_A13_15", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3136.9102, 4518.798, 909.60645), (-4.832824060585612, -83.80836959808138, -0.19229131777985134), (1.0, 1.184065, 1.0), "PWM_Quarry_4x4x4_A14", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1973.209, 4308.175, 890.89014), (2.440528723508291, -75.71792925832065, 0.5644983027137935), (1.0, 1.184065, 1.0), "PWM_Quarry_4x4x4_A15", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1575.4297, 6405.8184, 904.0825), (-5.367523272046548, 80.93201453391802, 2.15934834416843), (1.0, 1.184065, 1.0), "PWM_Quarry_4x4x4_A16", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2317.4465, 4182.378, 1159.626), (-5.304870953198405, -63.147135432073824, -0.16476460182340166), (1.0, 1.2613256, 1.0), "PWM_Quarry_4x4x4_A17_89", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1143.1504, 6273.209, 885.3657), (2.4405219532405336, 93.05229946519388, 0.5644998499402669), (1.0, 1.184065, 1.0), "PWM_Quarry_4x4x4_A18", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1657.1611, 6253.671, 787.6177), (-6.773009247141464, 80.70904774962833, -1.117461722813593), (1.0, 1.0, 1.0), "PWM_Quarry_4x4x4_A19", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3915.3193, 4543.7207, 910.5498), (0.0, -90.0001164887758, 0.0), (1.1329466, 1.1329466, 1.1329466), "PWM_Quarry_4x4x4_A2_224", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1486.1191, 6402.52, 1159.626), (-5.304870470536346, 105.14546020151334, -0.16476464349249995), (1.0, 1.261326, 1.0), "PWM_Quarry_4x4x4_A20", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3079.6846, 6380.0283, 847.1709), (-2.9617311459877733, 119.88211002570246, -2.0423586964199405), (1.0, 1.184065, 1.0), "PWM_Quarry_4x4x4_A21", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2317.4465, 2365.543, 1159.626), (-5.304870953198405, -63.147135432073824, -0.16476460182340166), (1.0, 1.261326, 1.0), "PWM_Quarry_4x4x4_A22", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1429.4142, 1111.666, 866.6697), (-5.4718632476265245, -46.90414630778775, -1.878448606652065), (1.3872588, 1.4989274, 1.3148625), "PWM_Quarry_4x4x4_A23", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1575.0308, 1498.3994, 909.6074), (-5.367553466487079, -87.83773031042699, 2.1593307041912944), (1.0, 1.2820278, 1.0), "PWM_Quarry_4x4x4_A24", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1767.287, 3665.5886, 940.1566), (12.27858382139497, -1.1189576232732212, -3.294311622704095), (1.1255405, 1.3548399, 1.0), "PWM_Quarry_4x4x4_A25", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (6451.385, 7206.254, 838.5298), (-2.9615472641142087, 65.54138602998636, -2.0423277567981706), (1.0, 1.184065, 1.0), "PWM_Quarry_4x4x4_A26", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5112.0166, 4294.5547, 964.80273), (-1.522278175803642, -93.00202326998387, 0.7695567415680982), (1.0, 1.624285, 1.0), "PWM_Quarry_4x4x4_A27_112", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (776.5731, 1046.2482, 830.6243), (12.278582669538286, -79.17156444960695, -3.294311282634148), (1.0, 1.2710919, 1.0878826), "PWM_Quarry_4x4x4_A28", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4337.4287, 4536.4233, 1004.3213), (0.21715901212816754, -69.76180924629625, 0.03586878428375162), (1.0, 1.184065, 1.0), "PWM_Quarry_4x4x4_A29", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1541.2207, 4381.5195, 745.64355), (-6.773009221254842, -53.125366382281086, -1.1174922186512435), (1.0, 1.0, 1.0), "PWM_Quarry_4x4x4_A3_4", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3888.842, 4246.8496, 1302.4272), (-5.535827837390246, -84.22034444984689, 2.085957666295641), (1.0, 1.261326, 1.0), "PWM_Quarry_4x4x4_A30", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3448.0862, 4246.8496, 1302.4272), (-4.507659563730469, -93.15735269494327, -1.0790706327510082), (0.6856661, 1.261326, 1.0), "PWM_Quarry_4x4x4_A31", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1326.0745, 1467.4954, 807.9371), (12.278583021732794, -33.19921509198661, -3.294310915190716), (1.0, 1.184065, 1.0), "PWM_Quarry_4x4x4_A32", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (11259.726, 7192.6816, 692.8589), (-2.961547295410075, 39.03607202201211, -2.042328015115046), (1.0, 1.184065, 1.0), "PWM_Quarry_4x4x4_A33_318", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (296.57312, 1046.2482, 705.6243), (12.278582528863046, -63.90127897122037, -3.2943111321956398), (1.0, 1.184065, 1.0), "PWM_Quarry_4x4x4_A34", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (556.5731, 891.24817, 915.62427), (-4.965331630176987, 74.23776735925614, 2.2328833530502807), (1.0, 1.184065, 1.0), "PWM_Quarry_4x4x4_A35", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (885.6717, 1263.134, 719.8688), (6.479075430620901, -45.72283753714424, 0.3515336358202271), (1.0, 1.184065, 1.0), "PWM_Quarry_4x4x4_A36", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3574.3652, 4459.8564, 910.5498), (0.0, -84.7283927351926, 0.0), (1.132947, 1.132947, 1.132947), "PWM_Quarry_4x4x4_A4", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1541.2207, 2564.6855, 745.64355), (-6.773009221254842, -53.125366382281086, -1.1174922186512435), (1.0, 1.0, 1.0), "PWM_Quarry_4x4x4_A5", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1541.2207, 2935.0938, 697.45386), (-6.773009221254842, -53.125366382281086, -1.1174922186512435), (1.0, 1.0, 1.0), "PWM_Quarry_4x4x4_A6", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1615.1367, 3278.109, 740.65784), (3.7776951059206385, 21.96231543853717, -0.8323058033561376), (1.0, 1.0, 1.0), "PWM_Quarry_4x4x4_A7", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (365.99005, 1114.8889, 631.12555), (3.7776950036907673, -56.08977542199606, -0.8323059194921475), (1.0, 1.0, 1.0), "PWM_Quarry_4x4x4_A8", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1031.5739, 1392.3882, 631.12555), (3.777694872849992, -10.117981313162987, -0.832305856628486), (1.0, 1.0, 1.0), "PWM_Quarry_4x4x4_A9", _folder)
if a: placed += 1
else: skipped += 1

# Batch 40: StaticMesh'PWM_Quarry_4x5x10' (38 instances)
_mesh_path = "/Game/Unshippable/Whitebox/Rocks/Meshes/PWM_Quarry_4x5x10"
_materials = ['/Game/Environments/ProcTexturing/ProcMaterial_Quarry_Atlas_A']
_folder = "Reconstruction/BD_BB_Chapter5_BalrogsNest/Meshes"
a = spawn_static_mesh(_mesh_path, _materials, (1115.6958, 869.7207, 675.1719), (-8.025511835164219, -90.00002669635793, 7.80131349208179e-08), (1.0, 1.0, 1.0), "PWM_Quarry_4x5x10_18", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (709.28955, 825.66797, 801.0464), (-0.053466842638218604, -167.92737520462964, 17.78290448786609), (0.86668974, 0.86668974, 0.66623646), "PWM_Quarry_4x5x11_11", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (944.2329, 940.41797, 809.2197), (-5.2758475801586, -79.39702452262834, -0.5773623005758723), (0.86669, 0.86669, 0.666236), "PWM_Quarry_4x5x12", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2659.4248, 4444.1797, 750.6533), (-13.0924359894042, -90.00011453703662, 1.7597862948149783e-07), (1.0, 1.0, 1.0), "PWM_Quarry_4x5x13", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2396.292, 4516.493, 783.8213), (13.786279708137231, 168.16137433981552, 24.308931686132535), (0.86669, 0.86669, 0.666236), "PWM_Quarry_4x5x14", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2487.9622, 4223.8955, 809.2197), (-5.2758475801586, -79.39702452262834, -0.5773623005758723), (0.86669, 0.86669, 0.666236), "PWM_Quarry_4x5x15", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1744.8818, 4624.118, 623.7344), (-12.65618930383081, -69.3607440565568, -1.244079494801246), (1.0978194, 1.0, 0.76814586), "PWM_Quarry_4x5x16", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2967.0967, 4657.208, 678.66406), (-13.0924359894042, -90.00011453703662, 1.7597862948149783e-07), (1.0, 1.0, 1.0), "PWM_Quarry_4x5x17", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1551.3848, 4336.449, 760.1504), (11.893120430042162, 128.6735864646154, 1.77147123953824), (0.86669, 0.86669, 0.666236), "PWM_Quarry_4x5x18", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1114.5801, 4722.5547, 538.08936), (11.584913934422183, 148.0759295034802, 1.5197284675700462), (0.86669, 0.86669, 0.666236), "PWM_Quarry_4x5x19", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2659.424, 4229.577, 855.30273), (3.619344990261352, 176.5654923099604, 5.6696367748237115), (1.0, 1.0, 1.0), "PWM_Quarry_4x5x20", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2356.5674, 4893.3477, 583.9375), (11.584914584335754, 134.5596804523961, 1.5197328415224487), (0.86669, 0.86669, 0.666236), "PWM_Quarry_4x5x21", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2002.3418, 6197.36, 669.64746), (-8.02551217519407, 78.76929556139731, 7.613979309706686e-06), (1.0, 1.0, 1.0), "PWM_Quarry_4x5x22", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2409.545, 6218.333, 795.522), (3.6146660852190986, 0.8434753648427452, 17.837823565489195), (0.86669, 0.86669, 0.666236), "PWM_Quarry_4x5x23", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2178.916, 6206.256, 803.6948), (-5.275787640157998, 89.37265309738197, -0.577361877516845), (0.86669, 0.86669, 0.666236), "PWM_Quarry_4x5x24", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1316.8555, 5842.3394, 540.49023), (-12.199798650250015, 110.39123014455173, -3.614287566187905), (1.0, 1.0, 0.768146), "PWM_Quarry_4x5x25", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1630.4795, 5989.227, 577.7998), (11.546516059600089, -65.18658152708, 2.999436576222793), (0.86669, 0.86669, 0.666236), "PWM_Quarry_4x5x26", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1551.3848, 2519.6143, 760.1504), (11.893120430042162, 128.6735864646154, 1.77147123953824), (0.86669, 0.86669, 0.666236), "PWM_Quarry_4x5x27", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (8175.0, 6490.0, 4715.0), (3.1238908098138736e-07, -15.000058453284847, -95.00005557842911), (1.6406497, 1.8221204, 1.6248087), "PWM_Quarry_4x5x28_24", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2759.1475, 5821.843, 2463.9663), (0.0, 3.103942707927904, -0.0), (1.0, 1.0, 1.0), "PWM_Quarry_4x5x29_185", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4445.245, 5014.494, 2466.52), (5.789095521187187, -179.5635087250009, -2.2081905485004003), (1.3299637, 1.0, 0.7701208), "PWM_Quarry_4x5x30_256", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (6273.6313, 5081.9717, 2437.9902), (4.992759131607966, -8.402650327009598, 6.069918402068424), (1.329964, 1.0, 0.770121), "PWM_Quarry_4x5x31_356", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5991.225, 4910.6855, 2328.9502), (1.5640240554344373, 68.55320463986874, 7.737915704699468), (1.329964, 1.0, 0.770121), "PWM_Quarry_4x5x32", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (6527.4976, 5044.4717, 2460.4087), (4.992758899159837, -8.402710887839163, 6.069917316860158), (1.329964, 1.0, 0.770121), "PWM_Quarry_4x5x33", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (7359.4893, 4935.4443, 2421.9336), (4.992758899159837, -8.402710887839163, 6.069917316860158), (1.329964, 1.0, 0.770121), "PWM_Quarry_4x5x34", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (9540.0, 5520.0, 4715.0), (-1.132820985229418e-06, -70.00002946737631, -95.00003525032353), (1.64065, 1.82212, 1.624809), "PWM_Quarry_4x5x35", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1404.3466, 2056.3135, 735.03973), (-1.5067140062423365, 8.284668901370043, -4.691162891408852), (1.0, 1.0, 0.768146), "PWM_Quarry_4x5x36", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1492.6918, 2426.9285, 762.0867), (4.945810517377193, 48.83300714643174, 2.7945738667615516), (1.0, 1.0, 0.768146), "PWM_Quarry_4x5x37", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1556.9136, 2604.2783, 783.26074), (-3.459259310506372, -18.47833294693355, -3.510070902602445), (1.0, 1.0, 0.768146), "PWM_Quarry_4x5x38", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1455.2852, 3545.5835, 606.1212), (-2.4359740104586107, 6.0855851568968236, -3.907561986354373), (1.0, 1.0, 0.768146), "PWM_Quarry_4x5x39", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1658.1387, 3275.1611, 762.73157), (1.3558675789270516, -156.30237499097066, 1.157687292930795), (0.86669, 0.86669, 0.666236), "PWM_Quarry_4x5x40", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (594.57983, 1326.6484, 496.58893), (-2.435882623175584, -71.9667677629433, -3.907562312953929), (1.0, 1.0, 0.768146), "PWM_Quarry_4x5x41", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (372.0083, 1072.2087, 653.1993), (1.355868144077914, 125.64536621326774, 1.1576969540028341), (0.86669, 0.86669, 0.666236), "PWM_Quarry_4x5x42", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1038.1936, 1703.9181, 496.58893), (-2.4358827832425893, -25.99450814879882, -3.9075629336404862), (1.0, 1.0, 0.768146), "PWM_Quarry_4x5x43", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1066.4467, 1367.0518, 653.1993), (1.3558675117568768, 171.61707825701666, 1.1576996483282276), (0.86669, 0.86669, 0.666236), "PWM_Quarry_4x5x44", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (741.05615, 1589.6758, 571.0881), (11.584906642963372, -170.62403262360624, 1.5197360950543328), (0.86669, 0.86669, 0.666236), "PWM_Quarry_4x5x45", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (6121.225, 5205.6855, 2473.9502), (-0.703766263679788, 28.34913294727979, 17.913656199140586), (1.329964, 1.0, 0.770121), "PWM_Quarry_4x5x46", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1378.0576, 2231.2, 704.0268), (-1.5067140062423365, 8.284668901370043, -4.691162891408852), (1.0, 1.0, 0.768146), "PWM_Quarry_4x5x47", _folder)
if a: placed += 1
else: skipped += 1

# Batch 41: StaticMesh'PWM_Quarry_5x4x10' (1 instances)
_mesh_path = "/Game/Unshippable/Whitebox/Rocks/Meshes/PWM_Quarry_5x4x10"
_materials = ['/Game/Environments/ProcTexturing/ProcMaterial_Quarry_Atlas_A']
_folder = "Reconstruction/BD_BB_Chapter5_BalrogsNest/Meshes"
a = spawn_static_mesh(_mesh_path, _materials, (8732.087, 7056.0728, 3750.8174), (84.99967596113761, -0.00027177446202163733, -24.999995484029355), (1.4299179, 1.4299179, 1.4299179), "PWM_Quarry_5x4x10_11", _folder)
if a: placed += 1
else: skipped += 1

# Batch 42: StaticMesh'PWM_Quarry_8x8x8_A' (147 instances)
_mesh_path = "/Game/Unshippable/Whitebox/Rocks/Meshes/PWM_Quarry_8x8x8_A"
_materials = ['/Game/Environments/ProcTexturing/ProcMaterial_Quarry_Atlas_2']
_folder = "Reconstruction/BD_BB_Chapter5_BalrogsNest/Meshes"
a = spawn_static_mesh(_mesh_path, _materials, (2333.9329, 3925.099, 1970.4629), (-71.3763394370208, -72.71484556694956, -109.502751055887), (1.0, 1.0, 1.0), "PWM_Quarry_8x8x8_A_132", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2119.042, 5883.162, 2511.4692), (-8.368801832258798, -80.89044574483003, 93.93954984149387), (0.815415, 0.815415, 0.815415), "PWM_Quarry_8x8x8_A10", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4466.5176, 6192.9043, 3329.4353), (16.102591901333792, -85.65879731155927, -89.32966704928754), (1.09731, 0.815415, 1.077027), "PWM_Quarry_8x8x8_A100", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (6395.067, 4423.855, 2196.0166), (-4.677949236929714, 95.97685121904922, 93.31366849088536), (0.815415, 0.815415, 0.815415), "PWM_Quarry_8x8x8_A101", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (6940.105, 4471.3975, 2408.3813), (-0.02331503126216713, -87.38647134750329, 90.26258539824057), (0.815415, 0.815415, 0.815415), "PWM_Quarry_8x8x8_A102", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (6425.448, 4729.7773, 2817.8838), (-6.69393673479886, 86.1221237940216, 91.0336045854009), (0.815415, 0.815415, 0.815415), "PWM_Quarry_8x8x8_A103", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (7563.315, 4923.7466, 2630.9268), (-0.02331503126216713, -87.38647134750329, 90.26258539824057), (0.815415, 0.815415, 0.815415), "PWM_Quarry_8x8x8_A104", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (7169.8584, 4275.285, 2425.6123), (0.0238644669241141, 92.71081774894576, 89.73750945450591), (0.815415, 0.815415, 0.815415), "PWM_Quarry_8x8x8_A105", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (7687.1655, 4760.854, 2462.1382), (-0.02319589220499453, -95.0830539141853, 90.26258599808497), (0.815415, 0.815415, 0.815415), "PWM_Quarry_8x8x8_A106", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (7258.634, 4359.3174, 2223.141), (-0.023190287172375684, -100.00475878181253, 90.26255953973467), (0.815415, 0.815415, 0.815415), "PWM_Quarry_8x8x8_A107", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (8783.155, 4836.8853, 2579.789), (0.10845747794954332, -99.13645980726837, 85.99848321815546), (0.815415, 0.7682969, 1.1459997), "PWM_Quarry_8x8x8_A108", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (8029.798, 4914.129, 2569.7178), (-4.098785129571537, 173.34502097388523, 98.58412884397292), (0.815415, 0.815415, 0.815415), "PWM_Quarry_8x8x8_A109", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3044.3008, 4633.6816, 2354.295), (2.349391570068951, -81.08637160944919, 85.9101620500031), (0.815415, 0.815415, 0.815415), "PWM_Quarry_8x8x8_A11_149", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (7735.702, 8069.2783, 2530.185), (-83.75428978566424, 131.98273213470804, 126.25567126177982), (0.815415, 0.875103, 0.865459), "PWM_Quarry_8x8x8_A110", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (9220.184, 4761.1836, 2845.4043), (-1.928040383836822, -74.60370137965586, -91.38797648206108), (1.09731, 0.815415, 1.077027), "PWM_Quarry_8x8x8_A111", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (7757.5093, 7577.1226, 2586.8496), (-83.75428978566424, 131.98273213470804, 126.25567126177982), (0.815415, 0.875103, 0.865459), "PWM_Quarry_8x8x8_A112", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (7748.5894, 7293.758, 2811.4), (-87.03836074031139, 73.99317514208552, 142.92216373203138), (0.815415, 0.875103, 0.865459), "PWM_Quarry_8x8x8_A113", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (9768.102, 4834.1533, 2636.8354), (14.749845045014183, -64.26699863097751, -83.36297758892819), (1.09731, 0.815415, 1.077027), "PWM_Quarry_8x8x8_A114", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (8136.5576, 4613.562, 2376.3923), (-0.9018857879004399, -168.12927444267757, 96.87230342711115), (0.815415, 0.8597251, 0.815415), "PWM_Quarry_8x8x8_A115", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5231.7, 5369.91, 2608.2778), (-84.23646886580879, -44.98072333911895, 44.77592157741671), (0.374732, 0.815415, 1.205663), "PWM_Quarry_8x8x8_A116", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (9598.064, 10573.02, 535.47363), (88.3883339155019, -115.86633044986968, 158.62838683066167), (1.0, 1.434769, 1.0), "PWM_Quarry_8x8x8_A117", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (9849.453, 10491.698, 2203.3027), (-4.677946529195601, -89.4203480696579, 93.3136871641402), (0.815415, 0.815415, 0.815415), "PWM_Quarry_8x8x8_A118", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (9686.483, 5117.9707, 2838.5566), (6.302596004261052, -81.29712274048475, 90.27595694741103), (0.815415, 0.768297, 1.146), "PWM_Quarry_8x8x8_A119", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3726.8438, 6282.755, 2311.625), (-8.302889925296615, -81.84253793035592, 94.07757908708139), (0.815415, 0.815415, 0.815415), "PWM_Quarry_8x8x8_A12", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (7822.2686, 7520.9673, 2704.4287), (-83.75138174479505, 169.09084912437154, 137.7507562373944), (0.81051457, 0.87020254, 0.8605585), "PWM_Quarry_8x8x8_A120", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (7622.602, 7666.794, 2497.4043), (-83.75216598906808, 131.98629592865913, 129.97186103911977), (1.1579309, 0.870203, 0.67794645), "PWM_Quarry_8x8x8_A121", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (6360.3267, 4928.9277, 2600.2441), (-4.67794976041819, -91.17522955177608, 93.31369101347434), (0.815415, 0.815415, 0.815415), "PWM_Quarry_8x8x8_A122", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (7686.7734, 5378.494, 2933.5322), (7.273711959328864, -169.08959303197042, 96.43788372476376), (0.815415, 0.768297, 1.146), "PWM_Quarry_8x8x8_A123_16", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (7848.481, 6309.114, 3114.1426), (6.104064908273842, 177.70855831617337, 86.34600896195518), (0.815415, 0.768297, 1.146), "PWM_Quarry_8x8x8_A124_48", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (7602.2476, 8090.4287, 2245.2861), (-82.28534955764775, 130.42779289056338, 142.75708481875762), (1.157931, 0.870203, 0.677946), "PWM_Quarry_8x8x8_A125", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (7221.424, 7573.7085, 2354.3564), (-85.32982163836327, 133.08990716090238, 85.6511446331046), (1.157931, 0.870203, 0.677946), "PWM_Quarry_8x8x8_A126", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (10353.854, 5902.8877, 2834.455), (4.2521748314395715, -143.03858997587406, 6.723119078024884), (0.5791631, 0.6601309, 0.57338345), "PWM_Quarry_8x8x8_A127", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (7434.0747, 7640.4956, 705.2466), (-83.74947208004394, 131.98753358550817, 175.78460008798828), (1.157931, 0.870203, 0.677946), "PWM_Quarry_8x8x8_A128", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (7718.399, 4917.6694, 2554.0435), (1.8806655606770009, 5.761543559859059, -1.7060853859502219), (0.703669, 0.703669, 0.703669), "PWM_Quarry_8x8x8_A129", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4326.6074, 6471.9556, 2371.67), (-6.694094143747248, -74.11591051037934, 91.03360586133148), (0.815415, 0.815415, 0.815415), "PWM_Quarry_8x8x8_A13", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5045.0205, 4914.4453, 2272.4365), (-87.89102439390288, -16.861749151323146, 18.78407434869325), (0.37345, 0.815415, 1.242628), "PWM_Quarry_8x8x8_A130", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (7834.2495, 7466.857, 2516.3286), (2.435440352523576, 5.5504763482141435, -7.307647615471201), (0.7705475, 0.703669, 0.703669), "PWM_Quarry_8x8x8_A131", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (10100.846, 5499.9863, 2547.7202), (4.344935523183605, 29.374909739028173, 7.631752652449934), (0.703669, 0.703669, 0.703669), "PWM_Quarry_8x8x8_A132", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (10229.546, 7864.994, 2577.9722), (18.36128238754401, 79.26577416153397, -3.089448937831018), (0.703669, 0.703669, 0.703669), "PWM_Quarry_8x8x8_A133", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (7954.54, 7545.974, 2521.8242), (-2.0059815924136366, -88.12609531204428, 1.0470036343220326), (0.7663961, 0.7737454, 0.703669), "PWM_Quarry_8x8x8_A134", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (9944.786, 7715.7676, 2830.0635), (-87.45541134962276, -36.403074866933714, -141.29377932327054), (0.810515, 0.870203, 0.860559), "PWM_Quarry_8x8x8_A135", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (8572.986, 8036.5234, 2569.3086), (-82.96334402512241, -57.42471542293479, 61.94213144824128), (0.810515, 0.7537856, 0.860559), "PWM_Quarry_8x8x8_A136", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (9310.583, 8056.5254, 2581.1611), (-83.2846928712097, -58.4444689221183, 65.98071460969174), (0.7884085, 0.67950666, 1.3084726), "PWM_Quarry_8x8x8_A137", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (11997.136, 10829.697, 2036.2344), (-72.26423104037426, 93.20869106664962, -86.60052629924456), (1.0, 1.0, 1.0), "PWM_Quarry_8x8x8_A138", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (12002.98, 10183.125, 2507.9624), (-85.46385111564835, 19.83098967429037, -109.80424474131705), (1.0, 1.0, 0.801156), "PWM_Quarry_8x8x8_A139", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3105.7314, 5964.7363, 2422.0938), (-8.393674710097287, 101.79235855212319, 95.21942294739078), (0.815415, 0.815415, 0.815415), "PWM_Quarry_8x8x8_A14", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (8633.314, 5553.7466, 4520.927), (-0.02325515260810054, -47.38647044902742, 90.26258921506816), (1.3133811, 1.0022383, 0.815415), "PWM_Quarry_8x8x8_A140", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (8898.314, 7293.7466, 4740.927), (-0.023224829880048314, 12.613524580358211, 90.26259584995314), (1.313381, 1.002238, 0.815415), "PWM_Quarry_8x8x8_A141", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (847.86237, 1179.7954, 2362.2395), (-6.295226460884399, 95.10338797132232, -176.69941460634436), (0.815415, 0.815415, 0.815415), "PWM_Quarry_8x8x8_A142", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1811.6722, 2773.3853, 1690.6497), (-8.302763675319643, 173.06507807497317, 94.07754306958465), (0.815415, 0.815415, 0.815415), "PWM_Quarry_8x8x8_A143", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1359.5225, 1316.9868, 2012.3855), (-14.485441794817705, 156.29826376738305, 96.19490097455498), (0.815415, 0.815415, 0.815415), "PWM_Quarry_8x8x8_A144", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (452.86237, 919.7954, 2262.2395), (-6.295227678907906, 83.43775629433699, -176.69934057083506), (0.815415, 0.815415, 0.815415), "PWM_Quarry_8x8x8_A145", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (672.86237, 1049.7954, 2372.2395), (-6.295226209422741, 162.1237761083142, -176.69933938107212), (0.815415, 0.815415, 0.815415), "PWM_Quarry_8x8x8_A146", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4648.3784, 6955.5747, 2190.0518), (-5.857325247881634, -61.532320142056015, 94.70261660691365), (0.815415, 0.815415, 0.815415), "PWM_Quarry_8x8x8_A147", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4705.8794, 7349.326, 1930.6265), (-73.79241342049066, 115.03306624657408, -88.52075026317955), (1.0, 1.0, 1.0), "PWM_Quarry_8x8x8_A15", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (973.68066, 5986.819, 472.00488), (0.0, -139.48533137271366, 0.0), (0.88131064, 0.88131064, 0.88131064), "PWM_Quarry_8x8x8_A16_400", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5137.745, 7124.7275, 2253.2627), (-5.857325247881634, -61.532320142056015, 94.70261660691365), (0.815415, 0.815415, 0.815415), "PWM_Quarry_8x8x8_A17", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4752.538, 6617.8135, 2499.4229), (-4.371490750001257, 120.62456576722641, 93.86607157716789), (0.815415, 0.815415, 0.815415), "PWM_Quarry_8x8x8_A18", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (6995.3325, 6832.9624, 2721.1328), (-6.7545771679762066, -76.71566695262915, 90.50075775188473), (0.815415, 1.0354128, 0.815415), "PWM_Quarry_8x8x8_A19", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1098.4341, 392.2129, 1926.2866), (-78.07270220995721, -93.47070236678745, -91.39486307095189), (1.0, 0.8269519, 0.91638464), "PWM_Quarry_8x8x8_A2", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (6367.3267, 7215.5737, 2374.0469), (-4.677920737904874, -72.27648310221463, 93.31380931884145), (0.815415, 0.815415, 0.815415), "PWM_Quarry_8x8x8_A20", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5689.5996, 7259.8916, 2222.4932), (-5.032198316289653, -71.58215704525718, 93.65190647271648), (0.815415, 0.815415, 1.0479094), "PWM_Quarry_8x8x8_A21_117", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5846.2134, 7049.455, 2453.9424), (-3.906312997473884, 104.34197238827704, 90.26316475419993), (0.815415, 0.815415, 0.815415), "PWM_Quarry_8x8x8_A22", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1721.7294, 4010.2112, 838.6908), (0.0, 15.22170472783441, -0.0), (0.827019, 0.90665704, 0.827019), "PWM_Quarry_8x8x8_A23_58", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (9370.0, 7310.0, 4180.0), (0.0, 0.0, -0.0), (1.0, 1.0, 1.0), "PWM_Quarry_8x8x8_A24_16", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (7015.9067, 4929.5093, 522.5542), (87.90853782285977, -161.72958262909242, -138.92842836221308), (0.815415, 0.815415, 0.815415), "PWM_Quarry_8x8x8_A25", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (6236.263, 5194.1562, 511.3789), (87.90808790382634, -133.46698643037323, -151.24684423612572), (0.815415, 0.815415, 0.815415), "PWM_Quarry_8x8x8_A26", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (10043.203, 10133.522, 590.5449), (87.86801316805693, 41.74457120757113, -151.22895053775824), (0.815415, 0.815415, 0.815415), "PWM_Quarry_8x8x8_A27_588", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2698.6172, 5352.6475, 2538.6685), (-2.3484496767977543, 95.72198528149248, -100.37511370812902), (0.815415, 0.815415, 0.815415), "PWM_Quarry_8x8x8_A28_152", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (6287.5645, 6909.8735, 2642.962), (-6.941343067111362, -82.3481519204278, 92.8621573929883), (0.815415, 0.815415, 0.94356817), "PWM_Quarry_8x8x8_A29", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1224.1567, 804.13184, 2142.4316), (-15.508514655468796, -89.84069512658918, -90.0506542660862), (1.0, 1.0, 1.0), "PWM_Quarry_8x8x8_A3_7", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (6425.093, 4924.9824, 3362.4456), (-2.8049343119146832, 96.13903187463575, 95.48209431290294), (1.3613032, 0.815415, 0.955749), "PWM_Quarry_8x8x8_A30", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (9576.494, 10523.459, 1652.5), (0.0, -90.0001164887758, 0.0), (1.0, 1.0, 1.0), "PWM_Quarry_8x8x8_A31_613", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4179.7197, 4658.4795, 2503.624), (13.492830919296996, -102.72387095293588, 92.94487364835376), (0.815415, 0.815415, 0.815415), "PWM_Quarry_8x8x8_A32", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5938.4814, 4765.3154, 2746.7012), (-4.860964080617604, 84.80147764642344, 90.77377915433533), (0.815415, 0.815415, 0.815415), "PWM_Quarry_8x8x8_A33", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5105.5947, 7138.1646, 523.7119), (87.90922953306224, 50.38702182949431, -151.24674584082166), (0.815415, 0.815415, 0.815415), "PWM_Quarry_8x8x8_A34_119", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1220.3077, 2414.992, 2420.9429), (-8.302764050963004, -174.5421104181491, 94.07754078171125), (0.815415, 0.815415, 0.815415), "PWM_Quarry_8x8x8_A35", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5987.4893, 4077.3882, 1021.48193), (-1.9407344466317016, 3.1580198108511364, 176.47466286847165), (1.0, 1.0, 1.0), "PWM_Quarry_8x8x8_A36", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4406.949, 4906.198, 2532.63), (-2.8104259012394204, 83.67110197522072, 93.05377909169457), (0.815415, 0.815415, 0.815415), "PWM_Quarry_8x8x8_A37", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4178.328, 4376.4272, 2265.7915), (-6.295282145050042, 84.28990684217037, 93.17332281487609), (0.815415, 0.815415, 0.815415), "PWM_Quarry_8x8x8_A38", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5241.4062, 4708.758, 664.9907), (-89.23449158680137, 133.91386973054333, -128.71468301615576), (0.815415, 0.815415, 0.815415), "PWM_Quarry_8x8x8_A39", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2350.0286, 3774.588, 1614.2773), (0.0, 15.22170472783441, -0.0), (0.8270186, 0.8270186, 0.8270186), "PWM_Quarry_8x8x8_A4_137", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4140.9395, 7036.2314, 1262.3208), (-1.0087890280968796, 17.90271007878507, 178.69569948418834), (0.815415, 0.815415, 1.047909), "PWM_Quarry_8x8x8_A40", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4508.671, 6642.4116, 548.2905), (87.90309842834417, 12.106541560324215, -151.24318249589746), (0.815415, 0.815415, 0.815415), "PWM_Quarry_8x8x8_A41_392", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5755.537, 4848.1875, 665.22705), (88.4541993951835, -177.6563194001199, 158.64221307798363), (0.815415, 0.815415, 0.815415), "PWM_Quarry_8x8x8_A42", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4768.329, 4551.987, 2605.7915), (-6.295288325965835, 100.74770757264086, 93.17340682019376), (0.815415, 0.815415, 0.815415), "PWM_Quarry_8x8x8_A43", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4298.252, 4615.1523, 2761.5928), (-6.295284551915695, 80.208115987284, 93.17327284573706), (0.815415, 0.815415, 0.815415), "PWM_Quarry_8x8x8_A44", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3542.915, 4808.573, 648.5039), (88.45125947137602, 178.14056804178745, 158.6404601804109), (0.4931201, 0.815415, 0.815415), "PWM_Quarry_8x8x8_A45", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3339.4258, 6219.3247, 657.3701), (86.98278396334928, 107.27276875491505, -60.580697342734965), (0.49312, 0.815415, 0.815415), "PWM_Quarry_8x8x8_A46", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3025.1328, 4493.8154, 2273.8076), (-6.2952873786086885, 95.10335268408303, 93.17327521633294), (0.815415, 0.815415, 0.815415), "PWM_Quarry_8x8x8_A47", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3680.4902, 4398.874, 2305.6865), (-2.217926131117515, -95.24236181845329, 90.08692290750504), (0.815415, 0.815415, 0.815415), "PWM_Quarry_8x8x8_A48_240", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3371.5188, 4245.339, 2114.5283), (-2.4719582822929564, -95.12776595884506, 87.28491982699123), (0.815415, 0.97648346, 1.3768448), "PWM_Quarry_8x8x8_A49", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1522.1855, 6621.49, 1929.7314), (-73.7931675813359, 100.83480697486615, -88.52093988722861), (1.0, 1.0, 1.0), "PWM_Quarry_8x8x8_A5", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3353.9583, 4166.9434, 1845.667), (-1.5781263854173093, -89.49487166853973, 85.97800104713014), (0.6634966, 0.815415, 0.815415), "PWM_Quarry_8x8x8_A50", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5105.552, 5060.37, 708.5054), (86.86124500331661, -87.0459361611028, -91.48316017551937), (0.37473187, 0.55667096, 0.815415), "PWM_Quarry_8x8x8_A51", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (7402.13, 5326.268, 600.48047), (84.79492550387533, -156.0391490115177, -168.75358609033574), (0.500976, 0.815415, 0.815415), "PWM_Quarry_8x8x8_A52", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (7856.704, 4747.721, 565.24817), (88.44862129123022, 159.49195177612353, 167.15678419089735), (1.0, 1.0, 1.0), "PWM_Quarry_8x8x8_A53", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (6652.9897, 4366.5435, 528.1885), (88.4307155900873, 69.52317916181869, 158.63618603404527), (1.0, 1.4347694, 1.0), "PWM_Quarry_8x8x8_A54", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (7661.787, 3869.2449, 2344.0078), (-86.98206197199704, -65.07924485415342, -130.13223961894155), (1.0, 1.0, 1.0), "PWM_Quarry_8x8x8_A55_410", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5325.257, 6743.3184, 2571.8438), (-6.694094143747248, -74.11591051037934, 91.03360586133148), (0.815415, 0.815415, 0.815415), "PWM_Quarry_8x8x8_A56", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (7913.095, 5135.4146, 584.46436), (87.90324573552282, -143.15451985155894, -151.24488692229906), (0.815415, 0.815415, 0.815415), "PWM_Quarry_8x8x8_A57_246", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (7890.984, 5087.298, 756.2855), (85.8626058306501, -42.486456624032975, -133.26677003229742), (0.5730455, 0.7429089, 0.7429089), "PWM_Quarry_8x8x8_A58_159", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (9851.864, 5177.4355, 614.1406), (87.90339067771895, -143.1540784133447, 143.55988041956067), (0.5869534, 0.815415, 0.815415), "PWM_Quarry_8x8x8_A59", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (857.89355, 6495.048, 928.7373), (-1.5530699876532277, -176.39989787723724, 174.8975425245545), (1.0, 1.0, 1.0), "PWM_Quarry_8x8x8_A6", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4803.778, 6207.9478, 2686.6455), (-7.877223595772337, -85.38018759319766, 92.32794342032065), (0.815415, 0.815415, 0.815415), "PWM_Quarry_8x8x8_A60", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5523.2266, 6527.1113, 2751.2202), (-3.1810928950358144, 96.70502101241892, 83.90729003647449), (0.815415, 0.815415, 0.815415), "PWM_Quarry_8x8x8_A61_408", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5393.1494, 5121.6074, 714.37695), (-87.78235478689626, 69.51629264555895, -64.74574856350195), (0.374732, 0.556671, 0.55785084), "PWM_Quarry_8x8x8_A62", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (10262.892, 5491.7617, 597.70215), (87.69732723819617, -31.595146409579407, -156.38635867376908), (0.815415, 0.815415, 0.990604), "PWM_Quarry_8x8x8_A63", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (10348.27, 4936.5234, 637.0571), (89.22817199021988, -41.076712819713606, -72.20389788233983), (0.6892396, 1.0, 1.0), "PWM_Quarry_8x8x8_A64", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (9361.065, 4902.451, 3087.7485), (0.15311684666921482, 104.75464681646226, 91.2783298438167), (0.815415, 0.815415, 0.815415), "PWM_Quarry_8x8x8_A65_377", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (8932.316, 5002.662, 3183.7366), (3.064095937184736, 116.46097640406136, 90.96403955878023), (0.815415, 0.815415, 0.815415), "PWM_Quarry_8x8x8_A66_379", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (10227.786, 7645.9697, 661.1245), (87.88453575501282, -11.38645271906701, -165.52369332422182), (0.68994695, 0.815415, 0.990604), "PWM_Quarry_8x8x8_A67", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (10777.752, 8083.705, 655.66895), (85.52480453110098, -111.3486283547432, -3.389014449185268), (0.68924, 1.0, 1.0), "PWM_Quarry_8x8x8_A68", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (9733.438, 4782.6045, 602.0117), (87.90285041836052, -143.15542706244582, 143.55899309315797), (0.586953, 0.815415, 0.815415), "PWM_Quarry_8x8x8_A69", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (7270.131, 3864.4192, 1079.0513), (-2.9795839437869684, 179.61154597283672, 88.86560322630875), (1.0, 1.0, 1.0), "PWM_Quarry_8x8x8_A7_289", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (9007.939, 4228.0674, 2417.3906), (-4.279568131780116, 106.3017411940565, 96.26600633415978), (0.815415, 0.815415, 0.815415), "PWM_Quarry_8x8x8_A70", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (9393.382, 4640.7153, 2668.3413), (-4.274561417536554, -58.12468785464519, 94.03969408745145), (0.815415, 0.815415, 0.815415), "PWM_Quarry_8x8x8_A71", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (10720.786, 5548.04, 609.55615), (87.68439502199604, -31.603515525558322, -145.1559187730162), (0.815415, 0.815415, 1.1791108), "PWM_Quarry_8x8x8_A72", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5807.1377, 7280.177, 622.0542), (87.88838295789684, 12.09866442389818, 166.9956359880506), (0.815415, 0.815415, 0.815415), "PWM_Quarry_8x8x8_A73_62", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5947.131, 4406.6226, 750.0405), (88.43623367748674, -177.61856263024075, 145.11594916256306), (0.815415, 0.815415, 0.815415), "PWM_Quarry_8x8x8_A74", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (8145.365, 4117.2896, 1238.8721), (1.142744984878026, 176.5975390336378, -179.25257363694507), (0.815415, 0.815415, 1.047909), "PWM_Quarry_8x8x8_A75_406", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (9991.183, 4411.76, 784.9961), (-89.49146189708195, -118.79500183309594, 147.99137295739322), (0.815415, 0.815415, 0.815415), "PWM_Quarry_8x8x8_A76", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (7191.3193, 7061.128, 618.6317), (86.98435868516177, -24.651409013982306, 150.1824303955626), (0.815415, 0.767767, 0.815415), "PWM_Quarry_8x8x8_A77_94", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (8855.559, 4345.703, 471.3508), (-88.98674215405593, 114.86533072096567, -109.08840281935136), (0.7000002, 0.815415, 0.815415), "PWM_Quarry_8x8x8_A78_86", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (9264.542, 4365.5015, 479.81335), (88.26680984924623, -165.43889801591615, 170.30341570690163), (0.7000002, 0.815415, 0.815415), "PWM_Quarry_8x8x8_A79", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1865.7812, 6218.8047, 2267.6406), (-8.302889925296615, -81.84253793035592, 94.07757908708139), (0.81541526, 0.81541526, 0.81541526), "PWM_Quarry_8x8x8_A8", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5945.0205, 4934.4453, 2242.4365), (-87.88868678901235, 160.08339265858885, 18.78271965500495), (0.37345, 0.815415, 1.2426285), "PWM_Quarry_8x8x8_A80", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (7370.8926, 8045.0547, 1424.9897), (-81.65067167926723, -0.4830352641866184, 75.70920584264944), (1.3779814, 0.815415, 1.047909), "PWM_Quarry_8x8x8_A81", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (10953.611, 10829.697, 2036.2344), (-72.26423104037426, 93.20869106664962, -86.60052629924456), (1.0, 1.0, 1.0), "PWM_Quarry_8x8x8_A82", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (9536.76, 9308.096, 523.7119), (87.8961171970781, 63.629040576667215, -151.23867285824534), (0.815415, 0.815415, 0.815415), "PWM_Quarry_8x8x8_A83", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (8991.868, 9127.38, 657.3701), (86.98100146758681, 120.51689252680434, -60.580193147990826), (0.49312, 0.815415, 0.815415), "PWM_Quarry_8x8x8_A84", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (7349.6074, 7101.1685, 599.7368), (86.78559354844116, 81.49962247864013, -161.7297162193129), (0.815415, 0.815415, 0.815415), "PWM_Quarry_8x8x8_A85", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (11549.859, 10183.125, 2507.9624), (-85.46385111564835, 19.83098967429037, -109.80424474131705), (1.0, 1.0, 0.801156), "PWM_Quarry_8x8x8_A86_631", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4428.46, 4834.9326, 2270.3398), (-86.56007729395334, -29.92931981440395, -159.28912725608168), (0.37345, 0.815415, 0.98120856), "PWM_Quarry_8x8x8_A87", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5996.7295, 5008.926, 2535.67), (-85.15882273597543, 128.99108756257536, -117.76597466105471), (0.374732, 0.815415, 1.2056627), "PWM_Quarry_8x8x8_A88", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4616.8877, 5233.944, 2595.2832), (-83.79961947665568, -41.06996435828308, 40.8887216046154), (0.374732, 0.815415, 1.205663), "PWM_Quarry_8x8x8_A89", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2675.7764, 6282.7563, 2311.625), (-8.302889925296615, -81.84253793035592, 94.07757908708139), (0.815415, 0.815415, 0.815415), "PWM_Quarry_8x8x8_A9", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5322.5513, 6207.9473, 2823.3262), (1.6303671122650407, -80.83355285788431, 93.09290020094056), (0.815415, 0.815415, 0.815415), "PWM_Quarry_8x8x8_A90_216", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5707.521, 6207.947, 2823.3257), (1.2312437914727665, 9.097717247117565, 10.035308030748448), (0.815415, 0.815415, 0.815415), "PWM_Quarry_8x8x8_A91", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (7574.5996, 7920.919, 2627.8691), (-83.76116532226752, 131.9732316608271, 115.26022339872064), (0.815415, 0.875103, 0.865459), "PWM_Quarry_8x8x8_A92", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (8023.0244, 8589.885, 2570.727), (-83.75955065013301, 131.97484348889728, 130.03210549015958), (0.815415, 0.875103, 0.865459), "PWM_Quarry_8x8x8_A93", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (8209.35, 4685.651, 469.9106), (87.905623970459, -143.1543582389609, -93.85462497144307), (0.815415, 0.815415, 0.815415), "PWM_Quarry_8x8x8_A94", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (8376.814, 8644.259, 2814.981), (-83.75725601128363, 131.97771862133655, 109.49406542092493), (0.815415, 0.875103, 0.865459), "PWM_Quarry_8x8x8_A95", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (6971.586, 8053.9404, 2544.3633), (29.680284026403434, -68.08452442511557, -93.13979368315444), (1.09731, 0.815415, 1.077027), "PWM_Quarry_8x8x8_A96", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (7485.2803, 6970.0327, 613.7097), (87.89902796971893, -157.20001634317862, -147.86936302775214), (0.815415, 0.68869495, 0.815415), "PWM_Quarry_8x8x8_A97", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5297.191, 6251.2773, 3356.5605), (6.938599881593571, -85.50054809127101, -89.34051510971845), (1.09731, 0.815415, 1.077027), "PWM_Quarry_8x8x8_A98", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4463.4854, 5263.557, 3438.5425), (-5.215697225363925, -85.55404452239608, -86.90637034410823), (1.09731, 0.815415, 1.077027), "PWM_Quarry_8x8x8_A99", _folder)
if a: placed += 1
else: skipped += 1

# Batch 43: StaticMesh'PWM_Quarry_Ceilling_Fissure_8x4_B' (33 instances)
_mesh_path = "/Game/Unshippable/Whitebox/Rocks/Meshes/PWM_Quarry_Ceilling_Fissure_8x4_B"
_materials = ['/Game/Environments/ProcTexturing/ProcMaterial_Quarry_Ceilling_Fissure_8x8']
_folder = "Reconstruction/BD_BB_Chapter5_BalrogsNest/Meshes"
a = spawn_static_mesh(_mesh_path, _materials, (2720.5234, 5005.875, 774.14307), (-0.006774865619837904, 20.832644703021156, 1.5128514419616528), (0.6372718, 0.6372718, 0.6372718), "PWM_Quarry_Ceilling_Fissure_8x4_B_64", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (13538.066, 6968.697, 668.8629), (-8.437285919774455, 9.108261198411993, -0.7658690110766091), (1.785, 0.73499995, 0.48), "PWM_Quarry_Ceilling_Fissure_8x4_B10", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2079.5078, 4972.909, 768.15674), (0.4608808334180505, 16.047363297714785, 8.805503096842168), (1.0, 1.0, 1.0), "PWM_Quarry_Ceilling_Fissure_8x4_B11", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2731.4736, 5748.623, 766.04346), (1.6999889389729483, -174.51032806222554, 2.2967977375903175), (0.8736907, 0.8736907, 0.7120907), "PWM_Quarry_Ceilling_Fissure_8x4_B12", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4341.463, 5342.839, 767.2749), (-0.2230529313858745, 26.646419200436902, 1.5699751099437245), (0.873691, 0.873691, 0.873691), "PWM_Quarry_Ceilling_Fissure_8x4_B13", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3498.0938, 6057.104, 770.16113), (0.6076410370718304, -172.4629933736939, 5.63811178817223), (0.83982784, 0.83982784, 0.83982784), "PWM_Quarry_Ceilling_Fissure_8x4_B14", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1182.1174, 3784.957, 800.00415), (0.46088098402063205, 93.23273140552551, 8.805919100621152), (1.0, 1.0, 1.0), "PWM_Quarry_Ceilling_Fissure_8x4_B15", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (7266.0596, 7296.601, 800.0), (-2.5314023436764175, -142.55135408065271, 6.777376360801357), (1.245955, 1.245955, 1.245955), "PWM_Quarry_Ceilling_Fissure_8x4_B16", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (7125.002, 4923.0117, 800.1372), (0.23484931028141381, -24.648468357045445, 9.514228083477898), (1.0, 1.0, 1.0), "PWM_Quarry_Ceilling_Fissure_8x4_B17", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1182.117, 2627.5725, 800.00415), (0.4608807346629436, 83.87506409464713, 8.80603019590045), (1.0, 1.0, 1.0), "PWM_Quarry_Ceilling_Fissure_8x4_B18", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (756.9988, 1471.3198, 800.003), (0.4608815422874653, 40.58355296955002, 8.806375672382869), (1.0, 1.0, 1.0), "PWM_Quarry_Ceilling_Fissure_8x4_B19", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1132.6318, 1079.0879, 824.0288), (0.7232418706024047, 22.051301997341096, 14.288232247665713), (1.0, 1.0, 1.0), "PWM_Quarry_Ceilling_Fissure_8x4_B2", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (7043.08, 6783.966, 765.33856), (-1.0044252456675786, -167.72573367826712, 12.599718432896987), (0.87751174, 0.87751174, 0.87751174), "PWM_Quarry_Ceilling_Fissure_8x4_B20", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5501.7305, 5390.596, 772.6157), (1.3774939004539621, 6.007507833272719, 7.301310863761833), (0.873691, 0.873691, 0.873691), "PWM_Quarry_Ceilling_Fissure_8x4_B21", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (14606.679, 7092.018, 629.149), (78.45854365591207, 65.11283875228668, 70.69168357193578), (0.5625, 1.0, 1.0), "PWM_Quarry_Ceilling_Fissure_8x4_B22", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (11584.488, 6964.8486, 1021.59894), (-5.063567353296927, -174.5362158142549, 73.47627204910722), (1.0, 1.0, 1.44), "PWM_Quarry_Ceilling_Fissure_8x4_B23", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (12008.752, 6631.973, 1107.0486), (4.113022678546233, -173.6204757194553, -68.7414701640621), (1.0, 1.0, 0.85249996), "PWM_Quarry_Ceilling_Fissure_8x4_B24", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (8110.628, 8097.8057, 804.9043), (1.6132762787510146, -113.28236283754374, 12.325083037534108), (1.0, 1.0, 1.0), "PWM_Quarry_Ceilling_Fissure_8x4_B26", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (8449.851, 8776.625, 777.6743), (0.6076407721147337, -151.01313185766165, 5.638139338472924), (1.245955, 1.245955, 1.245955), "PWM_Quarry_Ceilling_Fissure_8x4_B27", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (7817.4336, 7092.95, 744.562), (1.193793860868883, -113.97028751751289, -4.501220368494872), (1.0, 1.0, 1.0), "PWM_Quarry_Ceilling_Fissure_8x4_B28", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (10775.086, 6384.621, 810.0994), (-1.0615544327210906, 101.69851180387855, 5.830097350114576), (1.0, 1.0, 1.0), "PWM_Quarry_Ceilling_Fissure_8x4_B3_300", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (10917.729, 8784.836, 776.7593), (-0.22463984490706085, 24.194838900319088, 6.577177449059264), (1.2503393, 1.0, 1.0), "PWM_Quarry_Ceilling_Fissure_8x4_B38", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (10452.901, 9945.439, 790.03906), (-4.315033089366524, -156.49453523874217, 15.011115433461272), (1.250339, 1.0, 1.0), "PWM_Quarry_Ceilling_Fissure_8x4_B39", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2218.4883, 4745.5264, 849.0459), (0.46088075186696265, 9.023344383916626, 8.80524883254732), (1.0, 1.0, 1.0), "PWM_Quarry_Ceilling_Fissure_8x4_B4_1", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (9811.861, 9309.527, 766.291), (-2.585388691639311, -119.72157697116505, 8.249776198355407), (1.0348659, 1.0, 1.0), "PWM_Quarry_Ceilling_Fissure_8x4_B40", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (9578.494, 8933.516, 789.28467), (-0.9900816148033911, -132.0919651968365, 10.666587134372078), (0.89886427, 0.64852524, 0.64852524), "PWM_Quarry_Ceilling_Fissure_8x4_B41", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (11532.483, 10268.324, 804.1203), (-0.8296202423224328, -169.19535234198526, 15.584118108671786), (1.250339, 1.0, 1.0), "PWM_Quarry_Ceilling_Fissure_8x4_B42", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (11786.025, 8948.916, 746.00354), (-1.5357968529391375, -15.60510034222394, 0.26422716007977776), (1.1014615, 1.0, 1.0), "PWM_Quarry_Ceilling_Fissure_8x4_B43", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3544.3516, 4929.358, 787.01904), (-0.1416929769294843, 13.567108710045249, 8.491161372989934), (1.2459553, 1.2459553, 1.2459553), "PWM_Quarry_Ceilling_Fissure_8x4_B5", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2731.4746, 6002.063, 755.8999), (0.12911784274978227, -164.258080369233, 5.50327058250503), (1.245955, 1.245955, 1.245955), "PWM_Quarry_Ceilling_Fissure_8x4_B6", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1227.6309, 5938.9336, 787.0166), (2.8873122724722267, 176.9939627156262, 10.514941456828177), (1.245955, 1.245955, 1.245955), "PWM_Quarry_Ceilling_Fissure_8x4_B7", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (858.7998, 1951.9788, 761.29364), (-0.0067747932573247625, 75.64849897218747, 1.5128526298690272), (0.637272, 0.637272, 0.637272), "PWM_Quarry_Ceilling_Fissure_8x4_B8", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (11600.699, 6641.6157, 862.38354), (4.7486601210831525, 173.64891195139023, 1.698351742821306), (1.0, 1.0, 1.4399999), "PWM_Quarry_Ceilling_Fissure_8x4_B9", _folder)
if a: placed += 1
else: skipped += 1

# Batch 44: StaticMesh'PWM_Quarry_RockDebris_A' (93 instances)
_mesh_path = "/Game/Unshippable/Whitebox/Rocks/Meshes/PWM_Quarry_RockDebris_A"
_materials = ['/Game/Environments/ProcTexturing/ProcMaterial_Quarry_Atlas_5']
_folder = "Reconstruction/BD_BB_Chapter5_BalrogsNest/Meshes"
a = spawn_static_mesh(_mesh_path, _materials, (1815.7764, 5831.55, 794.27686), (0.0, 165.47167257801166, -0.0), (1.7585145, 1.7585145, 1.7585145), "PWM_Quarry_RockDebris_A_86", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (7822.081, 6664.739, 794.3408), (0.0, -135.7460217148819, 0.0), (1.875403, 1.875403, 1.875403), "PWM_Quarry_RockDebris_A10", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (6337.4614, 6734.4277, 794.6074), (0.0, 176.55662869042186, -0.0), (1.875403, 1.875403, 1.875403), "PWM_Quarry_RockDebris_A11", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5484.965, 6894.6055, 794.6074), (0.0, 179.6420564491926, -0.0), (1.875403, 1.875403, 1.875403), "PWM_Quarry_RockDebris_A12", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5094.054, 6733.0454, 793.98193), (0.0, -130.75879532709138, 0.0), (1.875403, 1.875403, 2.3265927), "PWM_Quarry_RockDebris_A13", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4707.0996, 6491.386, 794.1094), (1.6057842233908188, 122.01571630050236, -0.4994506031756514), (1.875403, 1.875403, 2.326593), "PWM_Quarry_RockDebris_A14", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4172.881, 6290.306, 798.7539), (-0.620239254758028, -130.7573934109616, -0.12136842405321996), (1.875403, 1.875403, 2.326593), "PWM_Quarry_RockDebris_A15", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3788.9688, 5939.5327, 791.20557), (-0.620239254758028, -130.7573934109616, -0.12136842405321996), (1.875403, 1.875403, 2.326593), "PWM_Quarry_RockDebris_A16_92", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3472.9033, 5809.675, 791.8594), (0.0, 167.97190300942043, -0.0), (1.758515, 1.758515, 1.758515), "PWM_Quarry_RockDebris_A17", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (6099.059, 5624.48, 791.4912), (0.0, 3.6625897948900494, -0.0), (1.5931602, 1.5931602, 1.5931602), "PWM_Quarry_RockDebris_A18", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4579.9297, 6271.934, 793.57764), (-0.6201477075898163, -127.5749773083975, -0.12136840855233796), (1.875403, 1.875403, 2.326593), "PWM_Quarry_RockDebris_A19", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1265.584, 4918.8735, 793.6924), (0.0, 11.493187076526668, -0.0), (1.758515, 1.758515, 1.758515), "PWM_Quarry_RockDebris_A2", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2647.2402, 5762.3555, 793.83545), (0.0, 165.170003856927, -0.0), (1.758515, 1.758515, 1.758515), "PWM_Quarry_RockDebris_A20", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2073.3105, 5711.8955, 793.83545), (0.0, 176.6395371590058, -0.0), (1.758515, 1.758515, 1.758515), "PWM_Quarry_RockDebris_A21", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1666.7461, 5711.8965, 793.83545), (0.0, -150.92645217396407, 0.0), (1.758515, 1.758515, 1.758515), "PWM_Quarry_RockDebris_A22", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1320.5391, 5776.1426, 795.74854), (0.0, 172.67910787185107, -0.0), (1.758515, 1.758515, 1.758515), "PWM_Quarry_RockDebris_A23", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3456.2676, 5237.8213, 794.4697), (0.0, -17.50759891544476, 0.0), (1.1902727, 1.1902727, 1.1902727), "PWM_Quarry_RockDebris_A24", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3666.708, 5260.421, 796.4824), (0.0, -17.50759891544476, 0.0), (1.190273, 1.190273, 1.190273), "PWM_Quarry_RockDebris_A25", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3924.08, 5260.4214, 796.4824), (0.0, 44.97076566141281, -0.0), (1.190273, 1.190273, 1.190273), "PWM_Quarry_RockDebris_A26", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3536.4062, 5445.548, 788.9668), (0.0, 44.97076566141281, -0.0), (1.190273, 1.190273, 1.190273), "PWM_Quarry_RockDebris_A27", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4051.0498, 5390.1626, 794.667), (0.23838768031068322, 69.08975568974637, -0.09103391836249111), (1.190273, 1.190273, 1.190273), "PWM_Quarry_RockDebris_A28", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4363.784, 5474.2656, 796.91064), (0.0, 2.1075516039909226, -0.0), (1.4757867, 1.190273, 1.190273), "PWM_Quarry_RockDebris_A29", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3196.7852, 5788.8076, 783.4356), (0.0, 129.70233735322626, -0.0), (1.758515, 1.758515, 1.758515), "PWM_Quarry_RockDebris_A3", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4722.6084, 5592.5527, 796.395), (0.0, 2.1075516039909226, -0.0), (1.475787, 1.190273, 1.190273), "PWM_Quarry_RockDebris_A30", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (7465.579, 5575.3545, 792.6758), (0.0, -135.7460217148819, 0.0), (1.875403, 1.875403, 1.875403), "PWM_Quarry_RockDebris_A31", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (6492.142, 5583.431, 789.14307), (0.0, 17.961639373376244, -0.0), (1.875403, 1.875403, 1.875403), "PWM_Quarry_RockDebris_A32", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (9716.667, 7845.3574, 794.1411), (0.0, 40.30214614626575, -0.0), (1.875403, 1.875403, 1.875403), "PWM_Quarry_RockDebris_A33", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (8483.369, 8055.734, 786.605), (0.0, -160.93884780298643, 0.0), (1.875403, 1.875403, 1.875403), "PWM_Quarry_RockDebris_A34", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (8157.462, 7145.549, 796.2666), (0.0, -88.55786348223386, 0.0), (1.875403, 1.875403, 1.875403), "PWM_Quarry_RockDebris_A35", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (8207.465, 6855.059, 789.9614), (0.0, -45.55606477380115, 0.0), (1.875403, 1.875403, 1.875403), "PWM_Quarry_RockDebris_A36", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (9245.823, 8590.2705, 792.16016), (0.0, 104.08741192033736, -0.0), (1.875403, 1.875403, 1.875403), "PWM_Quarry_RockDebris_A37", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (8889.461, 8509.331, 792.16016), (0.0, -145.83663510337914, 0.0), (1.875403, 1.875403, 1.875403), "PWM_Quarry_RockDebris_A38", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (8444.168, 8207.121, 792.16016), (0.0, -81.22121828413907, 0.0), (1.875403, 1.875403, 1.875403), "PWM_Quarry_RockDebris_A39", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3174.58, 5119.0327, 793.5259), (0.0, -74.52963123443382, 0.0), (1.758515, 1.758515, 1.758515), "PWM_Quarry_RockDebris_A4", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (9986.195, 9192.3125, 790.6382), (0.0, -141.22723216509814, 0.0), (1.875403, 1.875403, 1.875403), "PWM_Quarry_RockDebris_A40", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (10469.365, 9688.523, 790.6382), (0.0, -141.22723216509814, 0.0), (1.875403, 1.875403, 1.875403), "PWM_Quarry_RockDebris_A41", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (10940.074, 9874.157, 790.02295), (0.0, -141.22723216509814, 0.0), (1.875403, 1.875403, 1.875403), "PWM_Quarry_RockDebris_A42", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (9933.675, 8108.286, 795.2881), (0.0, 70.67790534220066, -0.0), (1.3199856, 1.3199856, 1.3199856), "PWM_Quarry_RockDebris_A43", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (9723.028, 7774.824, 796.29785), (-0.78842172452116, 65.25867830884668, 0.36336494345323844), (1.875403, 1.875403, 1.875403), "PWM_Quarry_RockDebris_A44", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (10905.869, 8904.133, 790.8667), (0.0, 15.60284426220995, -0.0), (1.875403, 1.875403, 1.875403), "PWM_Quarry_RockDebris_A45", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (10522.445, 8881.597, 788.96484), (0.0, -13.484801731169007, 0.0), (1.875403, 1.875403, 1.875403), "PWM_Quarry_RockDebris_A46", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (8120.217, 5733.211, 785.4868), (0.0, -45.55606477380115, 0.0), (1.875403, 1.875403, 1.875403), "PWM_Quarry_RockDebris_A47", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (8336.329, 5297.7524, 789.5342), (0.0, -2.3632812717854175, 0.0), (1.2659245, 1.875403, 1.875403), "PWM_Quarry_RockDebris_A48", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (6781.7617, 5381.406, 792.0303), (0.0, -135.7460217148819, 0.0), (1.8754026, 1.8754026, 1.8754026), "PWM_Quarry_RockDebris_A5_277", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (9621.29, 5412.0303, 789.5342), (0.0, -29.290585254639517, 0.0), (1.875403, 1.875403, 1.875403), "PWM_Quarry_RockDebris_A50", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (9563.809, 5574.7812, 785.28906), (0.0, -29.290585254639517, 0.0), (1.875403, 1.875403, 1.875403), "PWM_Quarry_RockDebris_A51", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (9803.2705, 5665.6616, 796.4131), (3.702648192792091e-09, 13.022125796071442, 0.4189567605045658), (1.875403, 1.875403, 1.875403), "PWM_Quarry_RockDebris_A52", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (8220.765, 7754.26, 794.20215), (0.0, -117.56260491301171, 0.0), (1.641006, 1.641006, 1.641006), "PWM_Quarry_RockDebris_A53", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (9707.512, 7309.63, 788.9751), (0.0, 161.51735518452313, -0.0), (1.875403, 1.875403, 1.875403), "PWM_Quarry_RockDebris_A54", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (7410.9985, 5728.373, 792.6362), (0.0, -158.91410384561578, 0.0), (1.3106828, 1.3106828, 1.3106828), "PWM_Quarry_RockDebris_A55_38", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (7960.8364, 5815.0864, 795.37695), (0.0, 32.13564508398388, -0.0), (1.310683, 1.310683, 1.310683), "PWM_Quarry_RockDebris_A56", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1696.4459, 4967.7964, 794.18854), (-0.24548341309785762, -60.665595783172535, -0.13796996987174148), (1.355255, 1.355255, 1.355255), "PWM_Quarry_RockDebris_A58", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2133.0994, 5665.092, 791.5502), (-0.24548341309785762, -60.665595783172535, -0.13796996987174148), (1.0794513, 1.0794513, 1.0794513), "PWM_Quarry_RockDebris_A59", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (6158.761, 6502.4116, 792.0298), (0.0, -27.886260503148236, 0.0), (1.875403, 1.875403, 1.875403), "PWM_Quarry_RockDebris_A6", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1900.2023, 5093.7734, 797.1349), (0.047835705655395896, -79.76635162262087, -0.28543089216960893), (1.079451, 1.079451, 1.079451), "PWM_Quarry_RockDebris_A60", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1768.887, 5661.4624, 793.5045), (0.13862603731967416, -60.664863158209364, -0.2540588612583971), (1.079451, 1.079451, 1.079451), "PWM_Quarry_RockDebris_A61", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2189.0215, 5036.5645, 799.0571), (0.13862600509860037, -168.0887656875438, -0.2540588251740101), (1.079451, 1.079451, 1.3608888), "PWM_Quarry_RockDebris_A62", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (823.2256, 5486.1724, 792.37646), (-0.16857907639085615, -143.23252344811334, 0.2255733973522008), (1.355255, 1.355255, 1.5707551), "PWM_Quarry_RockDebris_A63", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (948.2129, 4836.336, 793.79346), (0.2613169222432061, 68.13681850441918, -0.10485840536168492), (1.355255, 1.355255, 1.570755), "PWM_Quarry_RockDebris_A64", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4645.9844, 6205.291, 794.79974), (0.0, -90.0001164887758, 0.0), (1.5487497, 1.5487497, 1.5487497), "PWM_Quarry_RockDebris_A65", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3985.2305, 5960.755, 795.0093), (-0.40957627506016653, -137.52691518586363, -0.3749999653454543), (1.54875, 1.54875, 1.54875), "PWM_Quarry_RockDebris_A66", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5129.2246, 6533.7593, 791.64355), (-0.389831514960756, -133.44078080652932, 0.07472538542007275), (1.3848727, 1.3848727, 1.3848727), "PWM_Quarry_RockDebris_A67", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (6770.8325, 5704.379, 798.9922), (-1.298370452991633, 48.17244923460243, 0.626575951569595), (1.1849732, 1.1849732, 1.1849732), "PWM_Quarry_RockDebris_A68", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (6521.743, 5747.992, 794.6929), (-0.44540401801445134, 56.99458479033408, -1.0115965439472694), (1.184973, 1.184973, 1.184973), "PWM_Quarry_RockDebris_A69", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (6392.12, 6353.0156, 792.0303), (0.0, 140.11709781469102, -0.0), (1.875403, 1.875403, 1.875403), "PWM_Quarry_RockDebris_A7", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (7566.671, 5871.3633, 790.4619), (0.5751293318672095, -147.85252877656748, 0.46947725842425736), (1.184973, 1.184973, 1.184973), "PWM_Quarry_RockDebris_A70", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (7678.8086, 6384.5737, 795.7627), (-0.1572570484394485, -147.85387243432095, 0.009181278832212385), (1.184973, 1.184973, 1.184973), "PWM_Quarry_RockDebris_A71", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (6652.1484, 6485.1494, 793.53564), (-0.15725707110295387, -123.32390882520397, 0.009181058361212094), (1.184973, 1.184973, 1.184973), "PWM_Quarry_RockDebris_A72", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (8048.761, 6553.35, 789.7981), (-0.16796874164346187, -146.41924152420287, 0.0020193502591071364), (1.184973, 1.184973, 1.3251961), "PWM_Quarry_RockDebris_A73", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (8375.118, 7186.734, 795.8364), (0.0, -88.14070935838029, 0.0), (1.641006, 1.641006, 1.641006), "PWM_Quarry_RockDebris_A74", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (11025.881, 9036.555, 791.8252), (0.0, 45.89725860899911, -0.0), (1.875403, 1.875403, 1.875403), "PWM_Quarry_RockDebris_A75", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (10297.707, 9472.059, 792.5376), (0.0, -141.22723216509814, 0.0), (1.875403, 1.875403, 1.875403), "PWM_Quarry_RockDebris_A76", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (9341.438, 8389.711, 792.93066), (0.0, -114.68076605921281, 0.0), (1.6051401, 1.6051401, 1.6051401), "PWM_Quarry_RockDebris_A77", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5695.8726, 6227.546, 794.4546), (0.0, 2.1075516039909226, -0.0), (1.0, 1.0, 1.0), "PWM_Quarry_RockDebris_A78", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5289.5103, 6212.5913, 796.8452), (0.0, 55.678957798506005, -0.0), (1.0, 1.0, 1.0), "PWM_Quarry_RockDebris_A79", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5870.143, 6834.6147, 794.6074), (0.0, 179.6420564491926, -0.0), (1.875403, 1.875403, 1.875403), "PWM_Quarry_RockDebris_A8_66", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4969.2896, 6256.416, 798.5752), (0.6297377633299432, 55.66335009032396, -1.3999023077240136), (1.0, 1.0, 1.0), "PWM_Quarry_RockDebris_A80", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (8714.899, 5882.0303, 795.60205), (-0.16345208735564454, -147.84814080390117, 1.6445921708466016), (1.184973, 1.184973, 1.184973), "PWM_Quarry_RockDebris_A82", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (9702.984, 6173.7695, 799.416), (3.2018561598528708, 153.13321713297105, -0.05886836926632691), (1.184973, 1.184973, 1.3729969), "PWM_Quarry_RockDebris_A84", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (9548.453, 6988.732, 794.37305), (-0.07818602484003428, 112.94979198013048, -1.4493407694147435), (1.184973, 1.184973, 1.372997), "PWM_Quarry_RockDebris_A85", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1052.23, 4352.1416, 789.8617), (-0.24548341309785762, -60.665595783172535, -0.13796996987174148), (1.355255, 1.355255, 1.355255), "PWM_Quarry_RockDebris_A86", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (527.4638, 1535.262, 786.2077), (0.13862556099823306, -113.27223850267244, -0.2540283466680004), (1.079451, 1.079451, 1.360889), "PWM_Quarry_RockDebris_A87", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (968.62195, 4009.393, 791.53394), (-0.24548341309785762, -60.665595783172535, -0.13796996987174148), (1.355255, 1.355255, 1.355255), "PWM_Quarry_RockDebris_A88", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (968.62195, 3740.9434, 791.53394), (-0.24548341309785762, -60.665595783172535, -0.13796996987174148), (1.355255, 1.355255, 1.355255), "PWM_Quarry_RockDebris_A89", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4889.1455, 5489.608, 794.34814), (0.0, -37.25183068328172, 0.0), (1.3608222, 1.3608222, 1.3608222), "PWM_Quarry_RockDebris_A9", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (968.622, 3446.4658, 791.53394), (-0.2454834262887459, -24.303653255755385, -0.13796998305691588), (1.355255, 1.355255, 1.355255), "PWM_Quarry_RockDebris_A90", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1074.6296, 3210.433, 794.83453), (-0.2454834262887459, -24.303653255755385, -0.13796998305691588), (1.355255, 1.355255, 1.355255), "PWM_Quarry_RockDebris_A91", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (910.183, 2504.882, 794.8346), (-0.2454834262887459, -24.303653255755385, -0.13796998305691588), (1.355255, 1.355255, 1.355255), "PWM_Quarry_RockDebris_A92", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (910.183, 2253.3389, 794.8346), (-0.24548341284314681, 117.93499811498958, -0.1379700039070505), (1.355255, 1.355255, 1.355255), "PWM_Quarry_RockDebris_A93", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (330.82346, 1488.8049, 794.8346), (-0.24548341284314681, 117.93499811498958, -0.1379700039070505), (1.355255, 1.355255, 1.355255), "PWM_Quarry_RockDebris_A94", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5695.8726, 5777.546, 794.4546), (0.0, 77.23864099486886, -0.0), (1.0, 1.0, 1.0), "PWM_Quarry_RockDebris_A95", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (12113.777, 10174.271, 790.2694), (0.0, -141.22723216509814, 0.0), (1.875403, 1.875403, 1.875403), "PWM_Quarry_RockDebris_A96", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (11571.297, 10046.773, 790.2697), (0.0, -141.22723216509814, 0.0), (1.875403, 1.875403, 1.875403), "PWM_Quarry_RockDebris_A97", _folder)
if a: placed += 1
else: skipped += 1

# Batch 45: StaticMesh'PWM_Quarry_RockDebris_A' (1 instances)
_mesh_path = "/Game/Unshippable/Whitebox/Rocks/Meshes/PWM_Quarry_RockDebris_A"
_materials = ['/Game/Environments/ProcTexturing/ProcMaterial_Quarry_RockDebris_A']
_folder = "Reconstruction/BD_BB_Chapter5_BalrogsNest/Meshes"
a = spawn_static_mesh(_mesh_path, _materials, (1253.8289, 5688.512, 792.7712), (-0.24548341309785762, -60.665595783172535, -0.13796996987174148), (1.3552547, 1.3552547, 1.3552547), "PWM_Quarry_RockDebris_A57_9", _folder)
if a: placed += 1
else: skipped += 1

# ======================================================================
# PHASE 2: ConstructionCatalog  (construction blocks)
# ======================================================================
unreal.log(f"[{BUBBLE_NAME}] Phase 2: Placing construction blocks...")

# Construction blocks use DecoVolume transforms (matched by Name)
_folder = "Reconstruction/BD_BB_Chapter5_BalrogsNest/Construction"

# Construction: AB_Mines_Scaffolding_Beam_Panels_3m_Broken_A_2
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Scaffolding
#   Volume: EMorSimpleShape::Empty, BoxExtent: (100.0, 100.0, 100.0)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (5995.0, 6240.096, 865.0), (0.0, 149.99999400439492, -0.0), (2.0000, 2.0000, 2.0000), "AB_Mines_Scaffolding_Beam_Panels_3m_Broken_A_2", _folder)
if a: placed += 1
else: skipped += 1

# Construction: AB_Mines_Scaffolding_Broken_Segment_A2_2
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Scaffolding
#   Volume: EMorSimpleShape::Empty, BoxExtent: (100.0, 100.0, 100.0)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (6514.9336, 5281.8813, 922.7609), (6.21835410897633, 34.279267258304664, 0.009377045717303339), (2.0000, 2.0000, 2.0000), "AB_Mines_Scaffolding_Broken_Segment_A2_2", _folder)
if a: placed += 1
else: skipped += 1

# Construction: AB_Mines_Scaffolding_Broken_Segment_A3_2
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Scaffolding
#   Volume: EMorSimpleShape::Empty, BoxExtent: (100.0, 100.0, 100.0)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (4362.1196, 5404.755, 826.8561), (-5.477080904374959, 123.51642124021564, -8.853515278875811), (2.0000, 2.0000, 2.0000), "AB_Mines_Scaffolding_Broken_Segment_A3_2", _folder)
if a: placed += 1
else: skipped += 1

# Construction: AB_Mines_Scaffolding_Broken_Segment_A4_5
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Scaffolding
#   Volume: EMorSimpleShape::Empty, BoxExtent: (100.0, 100.0, 100.0)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (4457.607, 5585.7925, 797.1295), (-8.081176115048654, -57.18432644053649, 4.531159510392134), (2.0000, 2.0000, 2.0000), "AB_Mines_Scaffolding_Broken_Segment_A4_5", _folder)
if a: placed += 1
else: skipped += 1

# Construction: AB_Mines_Scaffolding_Broken_Segment_A5_2
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Scaffolding
#   Volume: EMorSimpleShape::Empty, BoxExtent: (100.0, 100.0, 100.0)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (7285.2544, 5842.3677, 875.9541), (33.81246999698878, 176.2919758189284, 160.73926697922687), (2.0000, 2.0000, 2.0000), "AB_Mines_Scaffolding_Broken_Segment_A5_2", _folder)
if a: placed += 1
else: skipped += 1

# Construction: AB_Mines_Scaffolding_Broken_Segment_A6
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Scaffolding
#   Volume: EMorSimpleShape::Empty, BoxExtent: (100.0, 100.0, 100.0)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (8319.999, 5136.99, 1059.4622), (-11.249999511592979, 89.999971915607, 5.632117010986698e-06), (2.0000, 2.0000, 2.0000), "AB_Mines_Scaffolding_Broken_Segment_A6", _folder)
if a: placed += 1
else: skipped += 1

# Construction: AB_Mines_Scaffolding_Broken_Segment_A7
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Scaffolding
#   Volume: EMorSimpleShape::Empty, BoxExtent: (100.0, 100.0, 100.0)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (8038.352, 5656.4087, 822.7956), (3.2454744123850574, 88.09330619638567, -6.0980533655519364), (2.0000, 2.0000, 2.0000), "AB_Mines_Scaffolding_Broken_Segment_A7", _folder)
if a: placed += 1
else: skipped += 1

# Construction: AB_Mines_Scaffolding_Broken_Segment_B_2
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Scaffolding
#   Volume: EMorSimpleShape::Empty, BoxExtent: (100.0, 100.0, 100.0)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (8059.999, 4940.596, 1073.7128), (2.1052556365599835, 89.99997539468026, 4.2340892824358707e-07), (2.0000, 2.0000, 2.0000), "AB_Mines_Scaffolding_Broken_Segment_B_2", _folder)
if a: placed += 1
else: skipped += 1

# Construction: AB_Mines_Scaffolding_Broken_Segment_B2_2
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Scaffolding
#   Volume: EMorSimpleShape::Empty, BoxExtent: (100.0, 100.0, 100.0)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (6134.307, 6405.0, 878.04626), (3.927185155819242e-05, 90.00007201795444, -40.00006199096379), (2.0000, 2.0000, 2.0000), "AB_Mines_Scaffolding_Broken_Segment_B2_2", _folder)
if a: placed += 1
else: skipped += 1

# Construction: AB_Mines_Scaffolding_Broken_Segment_B3_5
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Scaffolding
#   Volume: EMorSimpleShape::Empty, BoxExtent: (100.0, 100.0, 100.0)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (5595.4414, 5693.8394, 868.6368), (16.902189290881182, -57.346194098248475, -116.23395091769862), (2.0000, 2.0000, 2.0000), "AB_Mines_Scaffolding_Broken_Segment_B3_5", _folder)
if a: placed += 1
else: skipped += 1

# Construction: AB_Mines_Scaffolding_Broken_Segment_B4_2
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Scaffolding
#   Volume: EMorSimpleShape::Empty, BoxExtent: (100.0, 100.0, 100.0)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (8155.0, 5235.0, 1075.0), (-0.0, -89.99993822608693, -0.0), (2.0000, 2.0000, 2.0000), "AB_Mines_Scaffolding_Broken_Segment_B4_2", _folder)
if a: placed += 1
else: skipped += 1

# Construction: AB_Mines_Scaffolding_Broken_Segment_B5
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Scaffolding
#   Volume: EMorSimpleShape::Empty, BoxExtent: (100.0, 100.0, 100.0)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (7935.0, 5245.0005, 1075.0), (0.0, 89.99984099200987, -0.0), (2.0000, 2.0000, 2.0000), "AB_Mines_Scaffolding_Broken_Segment_B5", _folder)
if a: placed += 1
else: skipped += 1

# Construction: AB_Mines_Scaffolding_Foundation_3x2m_2
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Scaffolding
#   Volume: EMorSimpleShape::Empty, BoxExtent: (100.0, 100.0, 100.0)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (4229.998, 5230.0024, 830.0), (-0.0, -90.0001164887758, -0.0), (2.0000, 2.0000, 2.0000), "AB_Mines_Scaffolding_Foundation_3x2m_2", _folder)
if a: placed += 1
else: skipped += 1

# Construction: AB_Mines_Scaffolding_Foundation_3x2m2
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Scaffolding
#   Volume: EMorSimpleShape::Empty, BoxExtent: (100.0, 100.0, 100.0)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (4229.998, 5030.0024, 830.0), (-0.0, -90.0001164887758, -0.0), (2.0000, 2.0000, 2.0000), "AB_Mines_Scaffolding_Foundation_3x2m2", _folder)
if a: placed += 1
else: skipped += 1

# Construction: AB_Mines_Scaffolding_Foundation_3x2m3
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Scaffolding
#   Volume: EMorSimpleShape::Empty, BoxExtent: (100.0, 100.0, 100.0)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (4809.5806, 6719.0903, 810.0), (-0.0, -79.9999683893994, -0.0), (2.0000, 2.0000, 2.0000), "AB_Mines_Scaffolding_Foundation_3x2m3", _folder)
if a: placed += 1
else: skipped += 1

# Construction: AB_Mines_Scaffolding_Foundation_3x2m4
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Scaffolding
#   Volume: EMorSimpleShape::Empty, BoxExtent: (100.0, 100.0, 100.0)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (4844.3105, 6522.1284, 810.0), (-0.0, -79.9999683893994, -0.0), (2.0000, 2.0000, 2.0000), "AB_Mines_Scaffolding_Foundation_3x2m4", _folder)
if a: placed += 1
else: skipped += 1

# Construction: AB_Mines_Scaffolding_Foundation_3x2m5
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Scaffolding
#   Volume: EMorSimpleShape::Empty, BoxExtent: (100.0, 100.0, 100.0)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (4619.998, 4790.002, 1270.0), (0.0, -179.99998633961752, -0.0), (2.0000, 2.0000, 2.0000), "AB_Mines_Scaffolding_Foundation_3x2m5", _folder)
if a: placed += 1
else: skipped += 1

# Construction: AB_Mines_Scaffolding_Foundation_3x3m_2
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Scaffolding
#   Volume: EMorSimpleShape::Empty, BoxExtent: (100.0, 100.0, 100.0)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (8319.999, 4934.9976, 925.0), (-0.0, -90.0001164887758, -0.0), (2.0000, 2.0000, 2.0000), "AB_Mines_Scaffolding_Foundation_3x3m_2", _folder)
if a: placed += 1
else: skipped += 1

# Construction: AB_Mines_Scaffolding_Foundation_3x3x1m_B_2
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Scaffolding
#   Volume: EMorSimpleShape::Empty, BoxExtent: (100.0, 100.0, 100.0)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (4329.998, 4970.002, 1118.0), (-0.0, -90.0001164887758, -0.0), (2.0000, 2.0000, 2.0000), "AB_Mines_Scaffolding_Foundation_3x3x1m_B_2", _folder)
if a: placed += 1
else: skipped += 1

# Construction: AB_Mines_Scaffolding_Stairs_3M_2
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Scaffolding
#   Volume: EMorSimpleShape::Empty, BoxExtent: (100.0, 100.0, 100.0)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (8679.998, 4864.997, 930.0), (0.0, 89.99997063746636, -0.0), (2.0000, 2.0000, 2.0000), "AB_Mines_Scaffolding_Stairs_3M_2", _folder)
if a: placed += 1
else: skipped += 1

# Construction: BP_BalrogsNest_Column_A_2
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Stone
#   Volume: EMorSimpleShape::OrientedBox, BoxExtent: (401.4, 617.3, 902.9)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (7512.6494, 6880.711, 1787.3816), (0.0, 0.0, -0.0), (8.0279, 12.3469, 18.0571), "BP_BalrogsNest_Column_A_2", _folder)
if a: placed += 1
else: skipped += 1

# Construction: BP_BalrogsNest_Column_B_2
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Stone
#   Volume: EMorSimpleShape::OrientedBox, BoxExtent: (497.3, 460.6, 877.4)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (8300.493, 5575.8086, 1927.3904), (0.0, 0.0, -0.0), (9.9455, 9.2115, 17.5478), "BP_BalrogsNest_Column_B_2", _folder)
if a: placed += 1
else: skipped += 1

# Construction: BP_BalrogsNest_Column_B_A_2
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Wood
#   Volume: EMorSimpleShape::OrientedBox, BoxExtent: (170.8, 286.6, 501.5)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (7995.0654, 4842.22, 1551.4817), (0.0, 0.0, -0.0), (3.4170, 5.7316, 10.0296), "BP_BalrogsNest_Column_B_A_2", _folder)
if a: placed += 1
else: skipped += 1

# Construction: BP_BalrogsNest_Column_C_2
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Stone
#   Volume: EMorSimpleShape::OrientedBox, BoxExtent: (403.9, 608.0, 862.8)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (10464.904, 4969.3906, 1822.8325), (0.0, 0.0, -0.0), (8.0773, 12.1602, 17.2567), "BP_BalrogsNest_Column_C_2", _folder)
if a: placed += 1
else: skipped += 1

# Construction: BP_BalrogsNest_Column_C_A_2
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Wood
#   Volume: EMorSimpleShape::OrientedBox, BoxExtent: (170.8, 425.3, 501.5)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (10537.107, 4837.4214, 1351.4817), (0.0, 0.0, -0.0), (3.4170, 8.5063, 10.0296), "BP_BalrogsNest_Column_C_A_2", _folder)
if a: placed += 1
else: skipped += 1

# Construction: BP_BalrogsNest_Column_D_2
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Stone
#   Volume: EMorSimpleShape::OrientedBox, BoxExtent: (859.5, 554.1, 852.8)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (9424.117, 7329.711, 1862.8325), (0.0, 0.0, -0.0), (17.1900, 11.0811, 17.0567), "BP_BalrogsNest_Column_D_2", _folder)
if a: placed += 1
else: skipped += 1

# Construction: BP_Mines_Scaffolding_Platform_3X1M_B_2
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Scaffolding
#   Volume: EMorSimpleShape::Empty, BoxExtent: (100.0, 100.0, 100.0)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (4629.998, 5170.0015, 1130.0), (-0.0, -90.0001164887758, -0.0), (2.0000, 2.0000, 2.0000), "BP_Mines_Scaffolding_Platform_3X1M_B_2", _folder)
if a: placed += 1
else: skipped += 1

# Construction: BP_Mines_Scaffolding_Platform_3X1M_B2
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Scaffolding
#   Volume: EMorSimpleShape::Empty, BoxExtent: (100.0, 100.0, 100.0)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (4329.998, 5170.002, 1130.0), (-0.0, -90.0001164887758, -0.0), (2.0000, 2.0000, 2.0000), "BP_Mines_Scaffolding_Platform_3X1M_B2", _folder)
if a: placed += 1
else: skipped += 1

# Construction: BP_Mines_Scaffolding_Post_2M_A_2
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Scaffolding
#   Volume: EMorSimpleShape::OrientedBox, BoxExtent: (11.1, 99.4, 7.5)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (7181.1426, 5975.5757, 805.3722), (0.0, 0.0, -0.0), (0.2222, 1.9885, 0.1492), "BP_Mines_Scaffolding_Post_2M_A_2", _folder)
if a: placed += 1
else: skipped += 1

# Construction: DM_Mines_Scaffolding_Platform_3X3M_A_Destructible_8
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Scaffolding
#   Volume: EMorSimpleShape::Empty, BoxExtent: (100.0, 100.0, 100.0)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (5162.424, 4758.679, 1078.7974), (-0.0, -66.24047028176018, -0.0), (2.0000, 2.0000, 2.0000), "DM_Mines_Scaffolding_Platform_3X3M_A_Destructible_8", _folder)
if a: placed += 1
else: skipped += 1

# ======================================================================
# PHASE 3: Breakables + DecoVolumes
# ======================================================================
unreal.log(f"[{BUBBLE_NAME}] Phase 3: Placing breakables and deco volumes...")

_folder = "Reconstruction/BD_BB_Chapter5_BalrogsNest/Breakables"

# Breakable Batch 0: BP_DM_Deep_WoodenPlank_A_Breakable (29 instances)
#   BP Class: /Game/LevelDesign/Deco/Deep/BP_DM_Deep_WoodenPlank_A_Breakable
_brk_mesh = "/Game/Art/Assets/Kits/Architecture/Deep/Deep_WoodenPlank_A"
_brk_mats = ['/Game/Art/Assets/Kits/Architecture/Deep/Materials/Deep_WoodTrim/MI_Deep_WoodTrim']
a = spawn_static_mesh(_brk_mesh, _brk_mats, (1238.1455, 5922.1953, 1059.1201), (0.44261038651349555, -172.19492911339702, -92.47193319034926), (1.107152, 1.0, 1.0), "Deep_WoodenPlank_A10_261", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_brk_mesh, _brk_mats, (1225.9902, 5913.4526, 1161.4214), (-2.0703120572628615, -172.47215801382697, 91.28995072377342), (1.047202, 1.0, 1.0), "Deep_WoodenPlank_A11_262", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_brk_mesh, _brk_mats, (1234.7695, 5912.8774, 1433.4165), (3.9512846742742704, -172.2285426109011, -89.88000156018332), (1.0471828, 1.0, 1.0), "Deep_WoodenPlank_A12_263", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_brk_mesh, _brk_mats, (4452.091, 6188.9155, 803.1997), (-1.8840330480698975, 5.920386873536572, 22.41345735947582), (1.0, 1.0, 1.0), "Deep_WoodenPlank_A13_169", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_brk_mesh, _brk_mats, (5643.1973, 4991.01, 1088.1665), (0.5552737309840307, 0.40724178605643524, -5.900665294497348), (1.0, 1.0, 1.0), "Deep_WoodenPlank_A14_240", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_brk_mesh, _brk_mats, (5799.1196, 5286.773, 964.9209), (37.538847510600625, -34.366606451121335, 31.67658621484906), (1.0, 1.0, 1.0), "Deep_WoodenPlank_A15_244", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_brk_mesh, _brk_mats, (5905.655, 5604.3804, 796.0801), (0.5965280721637232, -162.6399970602281, -170.7082777913385), (1.0, 1.0, 1.0), "Deep_WoodenPlank_A16", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_brk_mesh, _brk_mats, (5443.708, 6256.7896, 795.68066), (2.3612779830321964, -173.6420305803413, 155.12518452258035), (1.0, 1.0, 1.0), "Deep_WoodenPlank_A17", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_brk_mesh, _brk_mats, (1744.0635, 4716.635, 1069.4883), (17.19716329760708, -162.97646368033898, 88.2695441697919), (1.107152, 1.0, 1.0), "Deep_WoodenPlank_A20", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_brk_mesh, _brk_mats, (1791.4131, 4677.759, 1398.2686), (-4.77917429175075, -170.2109134482022, 92.02706800073807), (1.047202, 1.0, 1.0), "Deep_WoodenPlank_A21", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_brk_mesh, _brk_mats, (1790.4854, 4694.2285, 1285.9521), (-2.063567934074098, -171.26602697713713, -97.69915236522183), (1.047202, 1.0, 1.0), "Deep_WoodenPlank_A22", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_brk_mesh, _brk_mats, (2384.0469, 4717.7793, 1544.9961), (-2.680602633591622, 179.7896162500078, -87.97939190897858), (1.047202, 1.0, 1.0), "Deep_WoodenPlank_A23", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_brk_mesh, _brk_mats, (2391.0547, 4723.0215, 1395.7344), (1.0105401762616921, 179.91988865826917, -87.98126630610592), (1.047202, 1.0, 1.0), "Deep_WoodenPlank_A24", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_brk_mesh, _brk_mats, (2388.8691, 4727.407, 1271.4321), (1.0105468563418716, 179.9199774695107, 100.19774156975494), (1.047202, 1.0, 1.0), "Deep_WoodenPlank_A25", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_brk_mesh, _brk_mats, (2959.2441, 4720.9365, 1174.6641), (6.8595511554806965, -179.05191743739627, 81.4963775302405), (1.047202, 1.0, 1.0), "Deep_WoodenPlank_A26", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_brk_mesh, _brk_mats, (3017.1377, 4777.214, 1384.6606), (-1.0075989505340062, -165.9063587600708, 90.34092850094652), (1.047202, 1.0, 1.0), "Deep_WoodenPlank_A27", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_brk_mesh, _brk_mats, (1820.4609, 5954.399, 1135.0098), (-2.0644835238347485, 178.81584959155919, 88.94727094653051), (1.047202, 1.0, 1.0), "Deep_WoodenPlank_A28", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_brk_mesh, _brk_mats, (1820.4609, 5956.3535, 1336.6045), (-2.064178398982561, -0.0140990969615081, 88.94711944656133), (1.047202, 1.0, 1.0), "Deep_WoodenPlank_A29", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_brk_mesh, _brk_mats, (1820.4629, 5949.652, 1479.4219), (-0.9118652540188821, -178.85624527754888, -91.05319065303667), (1.047202, 1.0, 1.0), "Deep_WoodenPlank_A30", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_brk_mesh, _brk_mats, (1276.8435, 3912.0288, 1073.8728), (-4.441372852983402, 105.37164985381051, -92.47909115369524), (1.107152, 1.0, 1.0), "Deep_WoodenPlank_A31", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_brk_mesh, _brk_mats, (1271.8564, 3912.3643, 1409.5703), (3.9512682407993633, 105.12657761897663, -89.87958635205138), (1.047183, 1.0, 1.0), "Deep_WoodenPlank_A33", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_brk_mesh, _brk_mats, (1377.9099, 3349.3184, 1250.0312), (16.215969923326426, 98.06798814547724, 89.52974495852813), (1.047202, 1.0, 1.0), "Deep_WoodenPlank_A34", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_brk_mesh, _brk_mats, (1383.3018, 3336.1948, 1455.5762), (-0.9117756440267069, 98.49841869027344, -91.05254669567029), (1.047202, 1.0, 1.0), "Deep_WoodenPlank_A36", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_brk_mesh, _brk_mats, (1215.8405, 2086.3384, 1035.2744), (0.4426204654712936, 85.16030508306022, -92.47184535483477), (1.107152, 1.0, 1.0), "Deep_WoodenPlank_A37", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_brk_mesh, _brk_mats, (1209.9702, 2100.1135, 1137.5752), (-2.069980704045157, 84.88282700335247, 91.28988411041297), (1.047202, 1.0, 1.0), "Deep_WoodenPlank_A38", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_brk_mesh, _brk_mats, (1207.4858, 2091.6743, 1409.5703), (3.951270570935662, 85.12654287519509, -89.8795745959799), (1.047183, 1.0, 1.0), "Deep_WoodenPlank_A39", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_brk_mesh, _brk_mats, (1115.1483, 1512.1354, 1455.5762), (-0.9117725089779138, 78.49834742877941, -91.05248358763023), (1.047202, 1.0, 1.0), "Deep_WoodenPlank_A40", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_brk_mesh, _brk_mats, (1121.6901, 1510.6667, 1312.7588), (-2.0640550564315374, -102.65884277185768, 88.94692690775014), (1.047202, 1.0, 1.0), "Deep_WoodenPlank_A41", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_brk_mesh, _brk_mats, (1119.779, 1511.0984, 1111.1641), (-2.064177571744337, 76.17078381274649, 88.9472726863165), (1.047202, 1.0, 1.0), "Deep_WoodenPlank_A42", _folder)
if a: placed += 1
else: skipped += 1

# Breakable Batch 1: BP_DM_Deep_WoodenPlank_B_Breakable (10 instances)
#   BP Class: /Game/LevelDesign/Deco/Deep/BP_DM_Deep_WoodenPlank_B_Breakable
_brk_mesh = "/Game/Art/Assets/Kits/Architecture/Deep/Deep_WoodenPlank_B"
_brk_mats = ['/Game/Art/Assets/Kits/Architecture/Deep/Materials/Deep_WoodTrim/MI_Deep_WoodTrim']
a = spawn_static_mesh(_brk_mesh, _brk_mats, (6742.6016, 6584.167, 805.0), (0.0, 1.35183535057999, -0.0), (1.0, 1.0, 1.0), "BP_DM_Deep_WoodenPlank_B_Breakable_2", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_brk_mesh, _brk_mats, (4197.3115, 6342.8545, 1029.5674), (67.8500601944191, 125.47140529824274, 179.88376282541572), (1.0, 1.0, 1.0), "Deep_WoodenPlank_B10", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_brk_mesh, _brk_mats, (5621.1704, 4929.22, 1077.2354), (0.0, -137.21648221795334, 0.0), (1.0, 1.0, 1.0), "Deep_WoodenPlank_B11_232", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_brk_mesh, _brk_mats, (5715.492, 4861.2314, 1077.2354), (0.0, 42.14503271953646, -0.0), (1.0, 1.0, 1.0), "Deep_WoodenPlank_B12", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_brk_mesh, _brk_mats, (5164.8164, 6232.7944, 800.10986), (-1.5462340715522063, 163.73623693855126, 173.71998784407043), (1.0, 1.0, 1.0), "Deep_WoodenPlank_B13", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_brk_mesh, _brk_mats, (5233.3086, 6372.2764, 800.2803), (-3.643248771816383, 1.1145627166582326, 8.647803715116803), (1.0, 1.0, 1.0), "Deep_WoodenPlank_B14", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_brk_mesh, _brk_mats, (6847.452, 6648.9985, 849.2365), (11.58902687623322, 37.584726199176565, -13.248077938284641), (1.0, 1.0, 1.0), "Deep_WoodenPlank_B15_106", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_brk_mesh, _brk_mats, (8661.178, 8340.052, 800.0), (-5.037994465602715, 10.698986178632211, 7.920878231105861), (1.0, 1.0, 1.0), "Deep_WoodenPlank_B16", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_brk_mesh, _brk_mats, (3166.9316, 5765.7744, 820.8843), (6.086476761852559, 176.88403915299165, -151.86696439588314), (1.0, 1.0, 1.0), "Deep_WoodenPlank_B8", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_brk_mesh, _brk_mats, (4122.793, 6372.593, 1068.8887), (-74.61089486724691, -84.23036516306159, 30.802418036054867), (1.0, 1.0, 1.0), "Deep_WoodenPlank_B9_165", _folder)
if a: placed += 1
else: skipped += 1

# Breakable Batch 2: BP_DM_Mine_tailings_Debris_2x2_C (5 instances)
#   BP Class: /Game/LevelDesign/Deco/MinesDressing/BP_DM_Mine_tailings_Debris_2x2_C
_brk_mesh = "/Game/Art/Assets/Kits/Deco/Mines/Mine_tailings_Debris_2x2_C"
_brk_mats = ['/Game/Art/Assets/Kits/Misc/Dirt_Mounds/Materials/MI_DirtMound_Mines', '/Game/Art/Assets/Kits/Deco/Rubble/Materials/Rubble_Masonry_Pile/MI_Rubble_Masonry_Pile_Base_Inst', '/Game/Art/Assets/Kits/Deco/Rubble/Materials/Rubble_Masonry_Pile/MI_Rubble_Masonry_Pile_06_Inst']
a = spawn_static_mesh(_brk_mesh, _brk_mats, (6107.8994, 6666.458, 787.9741), (0.0, -90.0001164887758, 0.0), (1.0, 1.0, 1.0), "BP_DM_Mine_tailings_Debris_2x2_C_2", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_brk_mesh, _brk_mats, (8573.915, 8526.232, 795.20654), (0.0, -90.0001164887758, 0.0), (1.0, 1.0, 1.0), "BP_DM_Mine_tailings_Debris_2x2_C2_2", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_brk_mesh, _brk_mats, (9858.947, 5856.809, 797.93994), (0.0, -90.0001164887758, 0.0), (1.0, 1.0, 1.0), "BP_DM_Mine_tailings_Debris_2x2_C3_5", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_brk_mesh, _brk_mats, (10471.955, 5235.9736, 989.874), (0.0, -90.0001164887758, 0.0), (1.0, 1.0, 1.0), "BP_DM_Mine_tailings_Debris_2x2_C4", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_brk_mesh, _brk_mats, (9697.351, 7529.3594, 818.8174), (0.0, -90.0001164887758, 0.0), (1.0, 1.0, 1.0), "BP_DM_Mine_tailings_Debris_2x2_C5", _folder)
if a: placed += 1
else: skipped += 1

# Breakable Batch 3: BP_DM_Mine_tailings_Debris_3x3_A (3 instances)
#   BP Class: /Game/LevelDesign/Deco/MinesDressing/BP_DM_Mine_tailings_Debris_3x3_A
_brk_mesh = "/Game/Art/Assets/Kits/Deco/Mines/Mine_tailings_Debris_3x3_A"
_brk_mats = ['/Game/Art/Assets/Kits/Misc/Dirt_Mounds/Materials/MI_DirtMound_Mines', '/Game/Art/Assets/Kits/Deco/Rubble/Materials/Rubble_Masonry_Pile/MI_Rubble_Masonry_Pile_06_Inst']
a = spawn_static_mesh(_brk_mesh, _brk_mats, (8272.315, 7957.171, 776.6328), (0.0, -59.20992764139425, 0.0), (1.0, 1.0, 1.0), "BP_DM_Mine_tailings_Debris_3x3_A_2", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_brk_mesh, _brk_mats, (8622.708, 8784.711, 821.08105), (0.0, -59.20992764139425, 0.0), (1.0, 1.0, 1.0), "BP_DM_Mine_tailings_Debris_3x3_A2", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_brk_mesh, _brk_mats, (8126.9517, 7932.3945, 802.7744), (0.0, -90.0001164887758, 0.0), (1.0, 1.0, 1.0), "BP_DM_Mine_tailings_Debris_3x3_A3_6", _folder)
if a: placed += 1
else: skipped += 1

# Breakable Batch 4: BP_DM_Mines_Lift_Prop_horizontal_broken_Breakable (1 instances)
#   BP Class: /Game/LevelDesign/Deco/MinesDressing/BP_DM_Mines_Lift_Prop_horizontal_broken_Breakable
_brk_mesh = "/Game/Art/Assets/Kits/Deco/Mines/Machine/Mines_Machine_Lift_Pieces/Mines_Lift_Prop_horizontal_broken"
_brk_mats = ['/Game/Art/Assets/Kits/Deco/Mines/Machine/Mines_Machine_Lift_Pieces/Materials/Mi_Mines_Machine_Lift_L']
a = spawn_static_mesh(_brk_mesh, _brk_mats, (7155.249, 5895.0, 806.49817), (3.5528741559884983e-06, -90.00009657155428, -55.000035606231116), (1.0, 1.0, 1.0), "BP_DM_Mines_Lift_Prop_horizontal_broken_Breakable_2", _folder)
if a: placed += 1
else: skipped += 1

# Breakable Batch 5: BP_DM_Mines_Lift_Rails_broken_Breakable (1 instances)
#   BP Class: /Game/LevelDesign/Deco/MinesDressing/BP_DM_Mines_Lift_Rails_broken_Breakable
_brk_mesh = "/Game/Art/Assets/Kits/Deco/Mines/Machine/Mines_Machine_Lift_Pieces/Mines_Lift_Rails_broken"
_brk_mats = ['/Game/Art/Assets/Kits/Deco/Mines/Machine/Mines_Machine_Lift_Pieces/Materials/Mi_Mines_Machine_Lift_K']
a = spawn_static_mesh(_brk_mesh, _brk_mats, (7370.6357, 5927.4805, 773.9186), (-74.9996168041548, 163.71196846797108, -3.425009385912757e-05), (1.0, 1.0, 1.0), "BP_DM_Mines_Lift_Rails_broken_Breakable_2", _folder)
if a: placed += 1
else: skipped += 1

# Breakable Batch 6: BP_DM_Mines_Machine_Whim_Boar_PullBar_Broken (2 instances)
#   BP Class: /Game/LevelDesign/Deco/MinesDressing/BP_DM_Mines_Machine_Whim_Boar_PullBar_Broken
_brk_mesh = "/Game/Art/Assets/Kits/Deco/Mines/Machine/Mines_Machine_Whim_Pieces/Mines_Machine_Whim_Boar_PullBar_Broken"
_brk_mats = ['/Game/Art/Assets/Kits/Deco/Mines/Materials/Mines_Machine_Whim/MI_Mines_Machine_Whim_Uniq', '/Game/Art/Assets/Kits/Deco/Mines/Materials/Mines_Machine_Whim/MI_Mines_Machine_Whim_Trim']
a = spawn_static_mesh(_brk_mesh, _brk_mats, (7340.543, 5825.752, 819.3362), (-23.92734006922242, 128.6589311576764, -19.322418415335502), (1.0, 1.0, 1.0), "BP_DM_Mines_Machine_Whim_Boar_PullBar_Broken_2", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_brk_mesh, _brk_mats, (4630.0, 6100.935, 809.91144), (0.0, 0.0, -130.0000580807365), (1.0, 1.0, 1.0), "BP_DM_Mines_Machine_Whim_Boar_PullBar_Broken2_5", _folder)
if a: placed += 1
else: skipped += 1

# Breakable Batch 7: BP_DM_Mines_Machine_Whim_Heavy_Beam_Broken (3 instances)
#   BP Class: /Game/LevelDesign/Deco/MinesDressing/BP_DM_Mines_Machine_Whim_Heavy_Beam_Broken
_brk_mesh = "/Game/Art/Assets/Kits/Deco/Mines/Machine/Mines_Machine_Whim_Pieces/Mines_Machine_Whim_Heavy_Beam_Broken"
_brk_mats = ['/Game/Art/Assets/Kits/Deco/Mines/Materials/Mines_Machine_Whim/MI_Mines_Machine_Whim_Trim', '/Game/Art/Assets/Kits/Deco/Mines/Materials/Mines_Machine_Whim/MI_Mines_Machine_Whim_Uniq']
a = spawn_static_mesh(_brk_mesh, _brk_mats, (7178.9805, 5797.2334, 831.8257), (-68.28829825617237, 66.94081290467594, 2.7465938146838105), (1.0, 1.0, 1.0), "BP_DM_Mines_Machine_Whim_Heavy_Beam_Broken_2", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_brk_mesh, _brk_mats, (4610.0, 6175.0, 850.0), (0.0, 0.0, -0.0), (1.0, 1.0, 1.0), "BP_DM_Mines_Machine_Whim_Heavy_Beam_Broken2_5", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_brk_mesh, _brk_mats, (7178.219, 5816.6455, 890.0), (0.0, -120.00001257424489, 0.0), (1.0, 1.0, 1.0), "BP_DM_Mines_Machine_Whim_Heavy_Beam_Broken3_8", _folder)
if a: placed += 1
else: skipped += 1

# Breakable Batch 8: BP_DM_Mines_Machine_Whim_Pole_Support_A_Broken (1 instances)
#   BP Class: /Game/LevelDesign/Deco/MinesDressing/BP_DM_Mines_Machine_Whim_Pole_Support_A_Broken
_brk_mesh = "/Game/Art/Assets/Kits/Deco/Mines/Machine/Mines_Machine_Whim_Pieces/Mines_Machine_Whim_Pole_Support_A_Broken"
_brk_mats = ['/Game/Art/Assets/Kits/Deco/Mines/Materials/Mines_Machine_Whim/MI_Mines_Machine_Whim_Trim']
a = spawn_static_mesh(_brk_mesh, _brk_mats, (7266.828, 5924.61, 793.8875), (84.99931396005685, 179.99987473296355, -124.99994701789416), (1.0, 1.0, 1.0), "BP_DM_Mines_Machine_Whim_Pole_Support_A_Broken_2", _folder)
if a: placed += 1
else: skipped += 1

# Breakable Batch 9: BP_DM_Mines_Machine_Whim_Rope_Bracket_Broken (2 instances)
#   BP Class: /Game/LevelDesign/Deco/MinesDressing/BP_DM_Mines_Machine_Whim_Rope_Bracket_Broken
_brk_mesh = "/Game/Art/Assets/Kits/Deco/Mines/Machine/Mines_Machine_Whim_Pieces/Mines_Machine_Whim_Rope_Bracket_Broken_A"
_brk_mats = ['/Game/Art/Assets/Kits/Deco/Mines/Materials/Mines_Machine_Whim/MI_Mines_Machine_Whim_Trim', '/Game/Art/Assets/Kits/Deco/Mines/Materials/Mines_Machine_Whim/MI_Mines_Machine_Whim_Uniq']
a = spawn_static_mesh(_brk_mesh, _brk_mats, (7220.0, 5650.0, 795.0), (0.0, 0.0, -0.0), (1.0, 1.0, 1.0), "BP_DM_Mines_Machine_Whim_Rope_Bracket_Broken_2", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_brk_mesh, _brk_mats, (4595.0, 6095.0, 805.0), (0.0, 0.0, -0.0), (1.0, 1.0, 1.0), "BP_DM_Mines_Machine_Whim_Rope_Bracket_Broken2_5", _folder)
if a: placed += 1
else: skipped += 1

# Breakable Batch 10: BP_DM_Mines_Machine_Whim_Rope_Support_Broken_B (2 instances)
#   BP Class: /Game/LevelDesign/Deco/MinesDressing/BP_DM_Mines_Machine_Whim_Rope_Support_Broken_B
_brk_mesh = "/Game/Art/Assets/Kits/Deco/Mines/Machine/Mines_Machine_Whim_Pieces/Mines_Machine_Whim_Rope_Support_Broken_B"
_brk_mats = ['/Game/Art/Assets/Kits/Deco/Mines/Materials/Mines_Machine_Whim/MI_Mines_Machine_Whim_Trim', '/Game/Art/Assets/Kits/Deco/Mines/Materials/Mines_Machine_Whim/MI_Mines_Machine_Whim_Uniq']
a = spawn_static_mesh(_brk_mesh, _brk_mats, (7181.8003, 5821.944, 802.74066), (-24.485354060295737, 162.14508373560614, -92.18021117934914), (1.0, 1.0, 1.0), "BP_DM_Mines_Machine_Whim_Rope_Support_Broken_B_2", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_brk_mesh, _brk_mats, (7195.7363, 5861.387, 858.13477), (-29.780672286927924, 68.39620816380481, -54.80249045493788), (1.0, 1.0, 1.0), "BP_DM_Mines_Machine_Whim_Rope_Support_Broken_B2_5", _folder)
if a: placed += 1
else: skipped += 1

# Breakable Batch 11: BP_DM_Mines_Machine_Whim_Side_Support_Beam_Broken_B (11 instances)
#   BP Class: /Game/LevelDesign/Deco/MinesDressing/BP_DM_Mines_Machine_Whim_Side_Support_Beam_Broken_B
_brk_mesh = "/Game/Art/Assets/Kits/Deco/Mines/Machine/Mines_Machine_Whim_Pieces/Mines_Machine_Whim_Side_Support_Beam_Broken_B"
_brk_mats = ['/Game/Art/Assets/Kits/Deco/Mines/Materials/Mines_Machine_Whim/MI_Mines_Machine_Whim_Trim']
a = spawn_static_mesh(_brk_mesh, _brk_mats, (8438.657, 5709.236, 2419.2021), (-26.78823769398552, 61.48486422105882, -142.7867634455659), (1.0, 1.0, 1.0), "Mines_Machine_Whim_Side_Support_Beam_Broken_B10", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_brk_mesh, _brk_mats, (8465.156, 5703.7954, 2404.252), (-56.45972413476661, -127.37138719227265, -138.60842593451702), (1.0, 1.0, 1.0), "Mines_Machine_Whim_Side_Support_Beam_Broken_B11", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_brk_mesh, _brk_mats, (8747.719, 6975.3843, 2399.3098), (0.0, 0.0, -30.937408058740974), (1.0, 1.0, 1.0), "Mines_Machine_Whim_Side_Support_Beam_Broken_B14", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_brk_mesh, _brk_mats, (9337.719, 6959.96, 2425.0413), (0.00012977356614740683, 179.9997063018381, -140.6238542769675), (1.0, 1.0, 1.0), "Mines_Machine_Whim_Side_Support_Beam_Broken_B15", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_brk_mesh, _brk_mats, (9637.718, 5997.092, 2389.3098), (-4.481782930291047e-13, 179.9998975471699, -30.93740805876452), (1.0, 1.0, 1.0), "Mines_Machine_Whim_Side_Support_Beam_Broken_B16", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_brk_mesh, _brk_mats, (9047.72, 6012.518, 2415.0413), (0.00012977356689247667, -0.0003662108996080463, -140.6238542771821), (1.0, 1.0, 1.0), "Mines_Machine_Whim_Side_Support_Beam_Broken_B17", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_brk_mesh, _brk_mats, (8460.649, 6320.4126, 2386.4727), (-34.34684923911824, 168.97752477841274, -91.964093276658), (1.0, 1.0, 1.0), "Mines_Machine_Whim_Side_Support_Beam_Broken_B18", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_brk_mesh, _brk_mats, (8472.376, 6628.3003, 2389.8618), (-15.341096575015529, -88.74735526600288, -143.9293574161871), (1.0, 1.0, 1.0), "Mines_Machine_Whim_Side_Support_Beam_Broken_B19", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_brk_mesh, _brk_mats, (9722.218, 6649.587, 2406.4727), (-61.33535946902782, -13.81911703229596, -80.2342592882096), (1.0, 1.0, 1.0), "Mines_Machine_Whim_Side_Support_Beam_Broken_B20", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_brk_mesh, _brk_mats, (9695.493, 6326.7017, 2419.8618), (-15.260617122926863, 89.20929580705531, -146.8439716195194), (1.0, 1.0, 1.0), "Mines_Machine_Whim_Side_Support_Beam_Broken_B21", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_brk_mesh, _brk_mats, (8161.8564, 6317.2563, 2397.7568), (-9.40606478096929, -118.50370049211182, -123.23854957048188), (1.0, 1.0, 1.0), "Mines_Machine_Whim_Side_Support_Beam_Broken_B3", _folder)
if a: placed += 1
else: skipped += 1

# Breakable Batch 12: BP_DM_Mines_Machine_Whim_Side_Support_Beam_Broken_C (8 instances)
#   BP Class: /Game/LevelDesign/Deco/MinesDressing/BP_DM_Mines_Machine_Whim_Side_Support_Beam_Broken_C
_brk_mesh = "/Game/Art/Assets/Kits/Deco/Mines/Machine/Mines_Machine_Whim_Pieces/Mines_Machine_Whim_Side_Support_Beam_Broken_C"
_brk_mats = ['/Game/Art/Assets/Kits/Deco/Mines/Materials/Mines_Machine_Whim/MI_Mines_Machine_Whim_Trim']
a = spawn_static_mesh(_brk_mesh, _brk_mats, (9642.719, 6953.739, 2421.7158), (6.830188929804403e-06, 179.9998975471539, -151.8747073980173), (1.0, 1.0, 1.0), "Mines_Machine_Whim_Side_Support_Beam_Broken_C10", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_brk_mesh, _brk_mats, (9342.721, 5997.0938, 2389.3098), (1.5491701419756559e-13, 179.9999248679243, -25.31173682251754), (1.0, 1.0, 1.0), "Mines_Machine_Whim_Side_Support_Beam_Broken_C11", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_brk_mesh, _brk_mats, (8742.719, 6018.739, 2411.7158), (6.8301875683749316e-06, -3.0517574981462398e-05, -151.87466506253597), (1.0, 1.0, 1.0), "Mines_Machine_Whim_Side_Support_Beam_Broken_C12", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_brk_mesh, _brk_mats, (8440.133, 6323.287, 2406.197), (47.386143818598654, 124.5379615687968, -133.78655576441483), (1.0, 1.0, 1.0), "Mines_Machine_Whim_Side_Support_Beam_Broken_C3", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_brk_mesh, _brk_mats, (8747.719, 7250.3843, 2394.3098), (22.97480287469568, -8.602050467462284, -35.25213677964749), (1.0, 1.0, 1.0), "Mines_Machine_Whim_Side_Support_Beam_Broken_C6", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_brk_mesh, _brk_mats, (8170.214, 5714.025, 2408.8713), (47.3861311580985, -30.14950682119821, -133.78656278059145), (1.0, 1.0, 1.0), "Mines_Machine_Whim_Side_Support_Beam_Broken_C7", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_brk_mesh, _brk_mats, (8754.498, 5709.607, 2376.2896), (3.869361275128662e-05, -89.99991075607626, -30.937374689806244), (1.0, 1.0, 1.0), "Mines_Machine_Whim_Side_Support_Beam_Broken_C8", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_brk_mesh, _brk_mats, (9042.719, 6975.3843, 2399.3098), (0.0, 0.0, -25.312346803534467), (1.0, 1.0, 1.0), "Mines_Machine_Whim_Side_Support_Beam_Broken_C9", _folder)
if a: placed += 1
else: skipped += 1

# Breakable Batch 13: BP_DM_Mines_Wagon_Broken_B (2 instances)
#   BP Class: /Game/LevelDesign/Deco/MinesDressing/BP_DM_Mines_Wagon_Broken_B
_brk_mesh = "/Game/Art/Assets/Kits/Deco/Mines/Mines_Wagon_Broken_B"
_brk_mats = ['/Game/Art/Assets/Kits/Deco/Mines/Materials/Mines_WagonCart/MI_Mines_WagonCart_Trim', '/Game/Art/Assets/Kits/Deco/Mines/Materials/Mines_WagonCart/MI_Mines_WagonCart']
a = spawn_static_mesh(_brk_mesh, _brk_mats, (8919.995, 8462.893, 800.0), (1.3300632237228196, 173.0958656058571, 4.4445757558612184), (1.0, 1.0, 1.0), "BP_DM_Mines_Wagon_Broken_B_2", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_brk_mesh, _brk_mats, (5714.635, 4904.091, 1085.6797), (5.181941549125814, 42.113690985501144, -0.7280275704874686), (1.0, 1.0, 1.0), "BP_DM_Mines_Wagon_Broken_B2", _folder)
if a: placed += 1
else: skipped += 1

# Breakable Batch 14: BP_Mines_Machine_Whim_Main_Beam (1 instances)
#   BP Class: /Game/LevelDesign/Deco/MinesDressing/BP_Mines_Machine_Whim_Main_Beam
_brk_mesh = "/Game/Art/Assets/Kits/Deco/Mines/Machine/Mines_Machine_Whim_Pieces/Mines_Machine_Whim_Main_Beam"
_brk_mats = ['/Game/Art/Assets/Kits/Deco/Mines/Materials/Mines_Machine_Whim/MI_Mines_Machine_Whim_Trim']
a = spawn_static_mesh(_brk_mesh, _brk_mats, (8843.99, 8307.581, 800.0), (6.258535679311165e-08, -106.05370847155164, 5.093967238272037), (1.0, 1.0, 1.0), "BP_Mines_Machine_Whim_Main_Beam_2", _folder)
if a: placed += 1
else: skipped += 1

# Breakable Batch 15: BP_DM_Rubble_Masonry_Pile_A_Breakable (1 instances)
#   BP Class: /Game/LevelDesign/Deco/Rubble/BP_DM_Rubble_Masonry_Pile_A_Breakable
_brk_mesh = "/Game/Art/Assets/Kits/Deco/Rubble/Rubble_Masonry_Pile_A"
_brk_mats = ['/Game/Art/Assets/Kits/Deco/Rubble/Materials/Rubble_Masonry_Pile/MI_Rubble_Masonry_Pile_Atlas_Inst_A', '/Game/Art/Assets/Kits/Deco/Rubble/Materials/Rubble_Masonry_Pile/MI_Rubble_Masonry_Pile_Atlas_Inst_A']
a = spawn_static_mesh(_brk_mesh, _brk_mats, (4611.405, 6251.34, 805.0), (0.0, 65.00009540133658, -0.0), (1.0, 1.0, 1.0), "BP_DM_Rubble_Masonry_Pile_A_Breakable_5", _folder)
if a: placed += 1
else: skipped += 1

# Breakable Batch 16: BP_DM_Rubble_Masonry_Pile_C_Breakable (1 instances)
#   BP Class: /Game/LevelDesign/Deco/Rubble/BP_DM_Rubble_Masonry_Pile_C_Breakable
_brk_mesh = "/Game/Art/Assets/Kits/Deco/Rubble/Rubble_Masonry_Pile_C"
_brk_mats = ['/Game/Art/Assets/Kits/Deco/Rubble/Materials/Rubble_Masonry_Pile/MI_Rubble_Masonry_Pile_Atlas_Inst_B', '/Game/Art/Assets/Kits/Deco/Rubble/Materials/Rubble_Masonry_Pile/MI_Rubble_Masonry_Pile_Atlas_Inst_A']
a = spawn_static_mesh(_brk_mesh, _brk_mats, (5758.3975, 5584.983, 800.0), (0.0, 100.00007542931677, -0.0), (1.0, 1.0, 1.0), "BP_DM_Rubble_Masonry_Pile_C_Breakable_2", _folder)
if a: placed += 1
else: skipped += 1

# Breakable Batch 17: BP_DM_Rubble_Masonry_Pile_E_Breakable (3 instances)
#   BP Class: /Game/LevelDesign/Deco/Rubble/BP_DM_Rubble_Masonry_Pile_E_Breakable
_brk_mesh = "/Game/Art/Assets/Kits/Deco/Rubble/Rubble_Masonry_Pile_E_Optimized"
_brk_mats = ['/Game/Art/Assets/Kits/Deco/Rubble/Materials/Rubble_Masonry_Pile/MI_Rubble_Masonry_Pile_Atlas_Inst_A', '/Game/Art/Assets/Kits/Deco/Rubble/Materials/Rubble_Masonry_Pile/MI_Rubble_Masonry_Pile_Atlas_Inst_B']
a = spawn_static_mesh(_brk_mesh, _brk_mats, (5703.615, 5701.005, 795.0), (0.0, -64.99993826502799, 0.0), (1.0, 1.0, 1.0), "BP_DM_Rubble_Masonry_Pile_E_Breakable_2", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_brk_mesh, _brk_mats, (4221.8164, 5483.3623, 795.0), (0.0, -145.04939935541825, 0.0), (1.0, 1.0, 1.0), "BP_DM_Rubble_Masonry_Pile_E_Breakable2_5", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_brk_mesh, _brk_mats, (4590.4194, 6134.0874, 795.0), (0.0, -100.00012643325417, 0.0), (1.0, 1.0, 1.0), "BP_DM_Rubble_Masonry_Pile_E_Breakable3_8", _folder)
if a: placed += 1
else: skipped += 1

# Breakable Batch 18: BP_DM_Rubble_Masonry_Pile_F_Breakable (2 instances)
#   BP Class: /Game/LevelDesign/Deco/Rubble/BP_DM_Rubble_Masonry_Pile_F_Breakable
_brk_mesh = "/Game/Art/Assets/Kits/Deco/Rubble/Rubble_Masonry_Pile_F_Optimized"
_brk_mats = ['/Game/Art/Assets/Kits/Deco/Rubble/Materials/Rubble_Masonry_Pile/MI_Rubble_Masonry_Pile_Atlas_Inst_B', '/Game/Art/Assets/Kits/Deco/Rubble/Materials/Rubble_Masonry_Pile/MI_Rubble_Masonry_Pile_Atlas_Inst_A']
a = spawn_static_mesh(_brk_mesh, _brk_mats, (7290.0, 5680.0, 790.0), (0.0, 0.0, -0.0), (1.0, 1.0, 1.0), "BP_DM_Rubble_Masonry_Pile_F_Breakable_2", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_brk_mesh, _brk_mats, (5820.0, 5430.0, 785.0), (0.0, 0.0, -0.0), (1.0, 1.0, 1.0), "BP_DM_Rubble_Masonry_Pile_F_Breakable2_8", _folder)
if a: placed += 1
else: skipped += 1

# Breakable Batch 19: BP_DM_Rubble_Masonry_Pile_H_Breakable (1 instances)
#   BP Class: /Game/LevelDesign/Deco/Rubble/BP_DM_Rubble_Masonry_Pile_H_Breakable
_brk_mesh = "/Game/Art/Assets/Kits/Deco/Rubble/Rubble_Masonry_Pile_H_Optimized"
_brk_mats = ['/Game/Art/Assets/Kits/Deco/Rubble/Materials/Rubble_Masonry_Pile/MI_Rubble_Masonry_Pile_Atlas_Inst_B', '/Game/Art/Assets/Kits/Deco/Rubble/Materials/Rubble_Masonry_Pile/MI_Rubble_Masonry_Pile_Atlas_Inst_A']
a = spawn_static_mesh(_brk_mesh, _brk_mats, (7181.5337, 5838.353, 800.0), (0.0, -75.00003453112258, 0.0), (1.0, 1.0, 1.0), "BP_DM_Rubble_Masonry_Pile_H_Breakable_5", _folder)
if a: placed += 1
else: skipped += 1

# Breakable Batch 20: BP_DM_Rubble_Masonry_Pile_I_Breakable (1 instances)
#   BP Class: /Game/LevelDesign/Deco/Rubble/BP_DM_Rubble_Masonry_Pile_I_Breakable
_brk_mesh = "/Game/Art/Assets/Kits/Deco/Rubble/Rubble_Masonry_Pile_I"
_brk_mats = ['/Game/Art/Assets/Kits/Deco/Rubble/Materials/Rubble_Masonry_Pile/MI_Rubble_Masonry_Pile_Atlas_Inst_B', '/Game/Art/Assets/Kits/Deco/Rubble/Materials/Rubble_Masonry_Pile/MI_Rubble_Masonry_Pile_Atlas_Inst_A']
a = spawn_static_mesh(_brk_mesh, _brk_mats, (5712.705, 5417.8486, 795.0), (0.0, -65.00002542279803, 0.0), (1.0, 1.0, 1.0), "BP_DM_Rubble_Masonry_Pile_I_Breakable_2", _folder)
if a: placed += 1
else: skipped += 1

# Breakable Batch 21: BP_Orc_Remains_C (1 instances)
#   BP Class: /Game/LevelDesign/Deco/Warren-Tomb/Orc_Remains/BP_Orc_Remains_C
_brk_mesh = "/Game/Art/Assets/Kits/Deco/Warrens_Tomb/Orc_Remains/Orc_Remains_C"
_brk_mats = ['/Game/CharacterArt/Uruks/RedEye/MI_UrukRedEye_Rusted_Inst', '/Game/CharacterArt/Uruks/RedEye/MI_UrukRedEye_Bolghak_Head_Rusted', '/Game/CharacterArt/Goblins/Native/MI_Goblin_Native_Rusted_Inst', '/Game/CharacterArt/Orcs/Native/MI_OrcNative_Rusted_Inst', '/Game/CharacterArt/Orcs/Gundabad/MI_Orc_Gundabad_Rusted_Inst']
a = spawn_static_mesh(_brk_mesh, _brk_mats, (2830.0, 5035.0, 805.0), (0.0, 0.0, -0.0), (1.0, 1.0, 1.0), "BP_Orc_Remains_C_2", _folder)
if a: placed += 1
else: skipped += 1

# Breakable Batch 22: BP_DM_Mines_Plank_3M_A (1 instances)
#   BP Class: /Game/LevelDesign/Deco_Architecture/Mines/BP_DM_Mines_Plank_3M_A
_brk_mesh = "/Game/Art/Assets/Kits/Deco_Architecture/Mines/Mines_Plank_3M_A"
_brk_mats = ['/Game/Art/Assets/Kits/Deco_Architecture/Mines/Materials/Mines_Scaffolding/MI_Mines_Scaffolding_E_Deco']
a = spawn_static_mesh(_brk_mesh, _brk_mats, (871.2626, 1612.93, 898.41595), (0.3238192628836463, 36.88887702293333, 8.920185580520589e-06), (1.0, 1.0, 1.0), "BP_DM_Mines_Plank_3M_A_2", _folder)
if a: placed += 1
else: skipped += 1

# Breakable Batch 23: BP_DM_Mines_Plank_3M_B (1 instances)
#   BP Class: /Game/LevelDesign/Deco_Architecture/Mines/BP_DM_Mines_Plank_3M_B
_brk_mesh = "/Game/Art/Assets/Kits/Deco_Architecture/Mines/Mines_Plank_3M_B"
_brk_mats = ['/Game/Art/Assets/Kits/Deco_Architecture/Mines/Materials/Mines_Scaffolding/MI_Mines_Scaffolding_E_Deco']
a = spawn_static_mesh(_brk_mesh, _brk_mats, (772.099, 1936.333, 807.79114), (15.304998472479086, -95.26998458892048, 5.309063413629924e-06), (1.0, 1.0, 1.0), "BP_DM_Mines_Plank_3M_B_2", _folder)
if a: placed += 1
else: skipped += 1

# Breakable Batch 24: BP_DM_Mines_Scaffolding_Beam_2M_B (4 instances)
#   BP Class: /Game/LevelDesign/Deco_Architecture/Mines/BP_DM_Mines_Scaffolding_Beam_2M_B
_brk_mesh = "/Game/Art/Assets/Kits/Deco_Architecture/Mines/Mines_Scaffolding_Beam_2M_C"
_brk_mats = ['/Game/Art/Assets/Kits/Deco_Architecture/Mines/Materials/Mines_Scaffolding/MI_Mines_Scaffolding_B_Deco']
a = spawn_static_mesh(_brk_mesh, _brk_mats, (4169.998, 5220.003, 980.0), (0.0, -90.0001164887758, 0.0), (1.0, 1.0, 1.0), "BP_DM_Mines_Scaffolding_Beam_2M_B_2", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_brk_mesh, _brk_mats, (4169.998, 4840.0024, 980.0), (0.0, -90.0001164887758, 0.0), (1.0, 1.0, 1.0), "BP_DM_Mines_Scaffolding_Beam_2M_B2", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_brk_mesh, _brk_mats, (4114.593, 5291.198, 842.21533), (82.5882156253733, 103.60138033954624, -111.29634638157758), (1.0, 1.0, 1.0), "BP_DM_Mines_Scaffolding_Beam_2M_B3_2", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_brk_mesh, _brk_mats, (5334.464, 6968.779, 930.11035), (4.8329849014753035e-06, -90.00016068306192, -86.39270651313171), (1.0, 1.0, 1.0), "BP_DM_Mines_Scaffolding_Beam_2M_B4_2", _folder)
if a: placed += 1
else: skipped += 1

# Breakable Batch 25: BP_DM_Mines_Scaffolding_Beam_3M_C (8 instances)
#   BP Class: /Game/LevelDesign/Deco_Architecture/Mines/BP_DM_Mines_Scaffolding_Beam_3M_C
_brk_mesh = "/Game/Art/Assets/Kits/Deco_Architecture/Mines/Mines_Scaffolding_Beam_3M_C"
_brk_mats = ['/Game/Art/Assets/Kits/Deco_Architecture/Mines/Materials/Mines_Scaffolding/MI_Mines_Scaffolding_B_Deco']
a = spawn_static_mesh(_brk_mesh, _brk_mats, (4759.9985, 5220.002, 880.0), (0.0, -90.0001164887758, 0.0), (1.0, 1.0, 1.0), "BP_DM_Mines_Scaffolding_Beam_3M_C_2", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_brk_mesh, _brk_mats, (4499.998, 5220.002, 880.0), (0.0, -90.0001164887758, 0.0), (1.0, 1.0, 1.0), "BP_DM_Mines_Scaffolding_Beam_3M_C2", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_brk_mesh, _brk_mats, (6523.0005, 5139.782, 912.70654), (-8.721142305375541e-07, -71.85214724606723, -30.665558529618135), (1.0, 1.0, 1.0), "BP_DM_Mines_Scaffolding_Beam_3M_C3_2", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_brk_mesh, _brk_mats, (6477.1235, 5220.1514, 916.55566), (-5.853676353770576e-07, -38.77429173365839, -30.665559220406045), (1.0, 1.0, 1.0), "BP_DM_Mines_Scaffolding_Beam_3M_C4", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_brk_mesh, _brk_mats, (4744.79, 6279.8765, 680.0), (0.0, -79.9999683893994, 0.0), (1.0, 1.0, 1.0), "BP_DM_Mines_Scaffolding_Beam_3M_C5", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_brk_mesh, _brk_mats, (4459.1963, 6229.5186, 680.0), (0.0, -79.9999683893994, 0.0), (1.0, 1.0, 1.0), "BP_DM_Mines_Scaffolding_Beam_3M_C6", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_brk_mesh, _brk_mats, (5244.9233, 6737.649, 789.6172), (44.293614660311775, -90.00015785967547, 4.3831402144541545e-06), (1.0, 1.0, 1.0), "BP_DM_Mines_Scaffolding_Beam_3M_C7_6", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_brk_mesh, _brk_mats, (4719.997, 4430.002, 1130.0), (6.830188509805735e-06, -80.00002816909404, 5.749075019860523e-13), (1.0, 1.0, 1.0), "BP_DM_Mines_Scaffolding_Beam_3M_C8", _folder)
if a: placed += 1
else: skipped += 1

# Breakable Batch 26: BP_DM_Mines_Scaffolding_Platform_1X1M_A (1 instances)
#   BP Class: /Game/LevelDesign/Deco_Architecture/Mines/BP_DM_Mines_Scaffolding_Platform_1X1M_A
_brk_mesh = "/Game/Art/Assets/Kits/Deco_Architecture/Mines/Mines_Scaffolding_Platform_1X1M_A"
_brk_mats = ['/Game/Art/Assets/Kits/Deco_Architecture/Mines/Materials/Mines_Scaffolding/MI_Mines_Scaffolding_D_Deco', '/Game/Art/Assets/Kits/Deco_Architecture/Mines/Materials/Mines_Scaffolding/MI_Mines_Scaffolding_E_Deco']
a = spawn_static_mesh(_brk_mesh, _brk_mats, (5005.8086, 4825.1064, 1108.7661), (0.0, -95.6928966723108, 0.0), (1.0, 1.0, 1.0), "DM_Mines_Scaffolding_Platform_1X1M_A_Destructible_5", _folder)
if a: placed += 1
else: skipped += 1

# Breakable Batch 27: BP_DM_Mines_Scaffolding_Platform_3X1M_A (6 instances)
#   BP Class: /Game/LevelDesign/Deco_Architecture/Mines/BP_DM_Mines_Scaffolding_Platform_3X1M_A
_brk_mesh = "/Game/Art/Assets/Kits/Deco_Architecture/Mines/Mines_Scaffolding_Platform_3X1M_A"
_brk_mats = ['/Game/Art/Assets/Kits/Deco_Architecture/Mines/Materials/Mines_Scaffolding/MI_Mines_Scaffolding_D_Deco', '/Game/Art/Assets/Kits/Deco_Architecture/Mines/Materials/Mines_Scaffolding/MI_Mines_Scaffolding_E_Deco']
a = spawn_static_mesh(_brk_mesh, _brk_mats, (3746.4531, 6160.547, 843.14746), (-6.092345568704642, -114.108129420771, 5.999187066265087), (1.0, 1.0, 1.0), "BP_DM_Mines_Scaffolding_Platform_3X1M_A5_2", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_brk_mesh, _brk_mats, (5088.405, 4590.7876, 1105.7612), (0.0, -34.400423177195535, 0.0), (1.0, 1.0, 1.0), "DM_Mines_Scaffolding_Platform_3X1M_A_Destructible_11", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_brk_mesh, _brk_mats, (4974.919, 5321.581, 881.1084), (5.216365185325611, 10.184843901681715, 17.493231180229532), (1.0, 1.0, 1.0), "DM_Mines_Scaffolding_Platform_3X1M_A_Destructible2", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_brk_mesh, _brk_mats, (5444.008, 4758.511, 1108.415), (0.0, -101.57244763201739, 0.0), (1.0, 1.0, 1.0), "DM_Mines_Scaffolding_Platform_3X1M_A_Destructible3_4", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_brk_mesh, _brk_mats, (6835.856, 5059.6616, 948.5161), (-10.711058497040987, -78.86877522013548, -0.5472101896095086), (1.0, 1.0, 1.0), "DM_Mines_Scaffolding_Platform_3X1M_A_Destructible4", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_brk_mesh, _brk_mats, (4848.503, 6762.591, 988.66016), (-1.5487365931455257, 164.31806466613077, 1.3629670741000148), (1.0, 1.0, 1.0), "DM_Mines_Scaffolding_Platform_3X1M_A_Destructible5", _folder)
if a: placed += 1
else: skipped += 1

# Breakable Batch 28: BP_DM_Mines_Scaffolding_Platform_3X1M_B (1 instances)
#   BP Class: /Game/LevelDesign/Deco_Architecture/Mines/BP_DM_Mines_Scaffolding_Platform_3X1M_B
_brk_mesh = "/Game/Art/Assets/Kits/Deco_Architecture/Mines/Mines_Scaffolding_Platform_3X1M_B"
_brk_mats = ['/Game/Art/Assets/Kits/Deco_Architecture/Mines/Materials/Mines_Scaffolding/MI_Mines_Scaffolding_E_Deco', '/Game/Art/Assets/Kits/Deco_Architecture/Mines/Materials/Mines_Scaffolding/MI_Mines_Scaffolding_D_Deco']
a = spawn_static_mesh(_brk_mesh, _brk_mats, (2970.25, 5657.588, 803.3203), (6.988129269803588, -57.34133593167631, 3.132516358275406e-06), (1.0, 1.0, 1.0), "BP_DM_Mines_Scaffolding_Platform_3X1M_B_2", _folder)
if a: placed += 1
else: skipped += 1

# Breakable Batch 29: BP_DM_Mines_Scaffolding_Platform_3X1M_C (1 instances)
#   BP Class: /Game/LevelDesign/Deco_Architecture/Mines/BP_DM_Mines_Scaffolding_Platform_3X1M_C
_brk_mesh = "/Game/Art/Assets/Kits/Deco_Architecture/Mines/Mines_Scaffolding_Platform_3X1M_C"
_brk_mats = ['/Game/Art/Assets/Kits/Deco_Architecture/Mines/Materials/Mines_Scaffolding/MI_Mines_Scaffolding_E_Deco', '/Game/Art/Assets/Kits/Deco_Architecture/Mines/Materials/Mines_Scaffolding/MI_Mines_Scaffolding_D_Deco']
a = spawn_static_mesh(_brk_mesh, _brk_mats, (7754.8745, 4883.9814, 1087.0508), (15.494169719173847, -117.54390963488741, -4.302428962197754), (1.0, 1.0, 1.0), "BP_DM_Mines_Scaffolding_Platform_3X1M_C_2", _folder)
if a: placed += 1
else: skipped += 1

# Breakable Batch 30: BP_DM_Mines_Scaffolding_Platform_3X3M_B (1 instances)
#   BP Class: /Game/LevelDesign/Deco_Architecture/Mines/BP_DM_Mines_Scaffolding_Platform_3X3M_B
_brk_mesh = "/Game/Art/Assets/Kits/Deco_Architecture/Mines/Mines_Scaffolding_Platform_3X3M_B"
_brk_mats = ['/Game/Art/Assets/Kits/Deco_Architecture/Mines/Materials/Mines_Scaffolding/MI_Mines_Scaffolding_D_Deco', '/Game/Art/Assets/Kits/Deco_Architecture/Mines/Materials/Mines_Scaffolding/MI_Mines_Scaffolding_E_Deco']
a = spawn_static_mesh(_brk_mesh, _brk_mats, (6887.199, 4925.1387, 963.5918), (-4.019866954100649, 9.045593705084777, -2.6626890418438807), (1.0, 1.0, 1.0), "BP_DM_Mines_Scaffolding_Platform_3X3M_B_2", _folder)
if a: placed += 1
else: skipped += 1

# Breakable Batch 31: BP_DM_Mines_Scaffolding_Post_2M_B (2 instances)
#   BP Class: /Game/LevelDesign/Deco_Architecture/Mines/BP_DM_Mines_Scaffolding_Post_2M_B
_brk_mesh = "/Game/Art/Assets/Kits/Deco_Architecture/Mines/Mines_Scaffolding_Post_2M_B"
_brk_mats = ['/Game/Art/Assets/Kits/Deco_Architecture/Mines/Materials/Mines_Scaffolding/MI_Mines_Scaffolding_C_Deco']
a = spawn_static_mesh(_brk_mesh, _brk_mats, (5336.922, 6810.861, 826.65674), (74.58425206492183, -172.6370017986377, -93.4589313608397), (1.0, 1.0, 1.0), "BP_DM_Mines_Scaffolding_Post_2M_B_2", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_brk_mesh, _brk_mats, (6686.971, 5187.3574, 936.0869), (-84.32860485952034, -29.591447000006, -60.529099406894915), (1.0, 1.0, 1.0), "BP_DM_Mines_Scaffolding_Post_2M_B2_5", _folder)
if a: placed += 1
else: skipped += 1

# Breakable Batch 32: BP_DM_Mines_Scaffolding_Post_3M_A (6 instances)
#   BP Class: /Game/LevelDesign/Deco_Architecture/Mines/BP_DM_Mines_Scaffolding_Post_3M_A
_brk_mesh = "/Game/Art/Assets/Kits/Deco_Architecture/Mines/Mines_Scaffolding_Post_3M_A"
_brk_mats = ['/Game/Art/Assets/Kits/Deco_Architecture/Mines/Materials/Mines_Scaffolding/MI_Mines_Scaffolding_B_Deco']
a = spawn_static_mesh(_brk_mesh, _brk_mats, (2978.127, 5622.1724, 807.81006), (81.18716560717722, 1.2627020659726764, 132.70890234882114), (1.0, 1.0, 1.0), "BP_DM_Mines_Scaffolding_Post_3M_A_2", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_brk_mesh, _brk_mats, (4295.908, 6262.235, 800.0), (22.02382595269974, -68.98415701263158, -10.870849136339562), (1.0, 1.0, 1.0), "BP_DM_Mines_Scaffolding_Post_3M_A2_5", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_brk_mesh, _brk_mats, (4253.875, 6232.4043, 799.7383), (24.70143622985178, -44.144461612593005, 7.778218209167722), (1.0, 1.0, 1.0), "BP_DM_Mines_Scaffolding_Post_3M_A3", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_brk_mesh, _brk_mats, (6789.9307, 5078.8223, 933.13086), (84.84658569721763, 105.74858829622876, -179.99984080265992), (1.0, 1.0, 1.0), "BP_DM_Mines_Scaffolding_Post_3M_A4_9", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_brk_mesh, _brk_mats, (4991.7046, 6457.6455, 956.0703), (79.85014932994532, -147.61871471179472, -73.7081735265812), (1.0, 1.0, 1.0), "BP_DM_Mines_Scaffolding_Post_3M_A5", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_brk_mesh, _brk_mats, (4672.196, 6054.829, 786.26294), (49.21868448305652, -72.2374142404684, 1.687286918807116), (1.0, 1.0, 1.0), "BP_DM_Mines_Scaffolding_Post_3M_A6", _folder)
if a: placed += 1
else: skipped += 1

# Breakable Batch 33: BP_DM_Mines_Scaffolding_Support_1M (2 instances)
#   BP Class: /Game/LevelDesign/Deco_Architecture/Mines/BP_DM_Mines_Scaffolding_Support_1M
_brk_mesh = "/Game/Art/Assets/Kits/Deco_Architecture/Mines/Mines_Scaffolding_Support_1M"
_brk_mats = ['/Game/Art/Assets/Kits/Deco_Architecture/Mines/Materials/Mines_Scaffolding/MI_Mines_Scaffolding_D_Deco']
a = spawn_static_mesh(_brk_mesh, _brk_mats, (4127.334, 6266.4, 800.0), (22.74025789901901, -95.57012519260735, -104.15996483097837), (1.0, 1.0, 1.0), "BP_DM_Mines_Scaffolding_Support_1M_5", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_brk_mesh, _brk_mats, (4741.4844, 6065.221, 774.9325), (26.27940613602702, -99.45299728661934, -155.77183731754823), (1.0, 1.0, 1.0), "BP_DM_Mines_Scaffolding_Support_1M2", _folder)
if a: placed += 1
else: skipped += 1

# Breakable Batch 34: BP_DM_Mines_Scaffolding_Support_2M (20 instances)
#   BP Class: /Game/LevelDesign/Deco_Architecture/Mines/BP_DM_Mines_Scaffolding_Support_2M
_brk_mesh = "/Game/Art/Assets/Kits/Deco_Architecture/Mines/Mines_Scaffolding_Support_2M"
_brk_mats = ['/Game/Art/Assets/Kits/Deco_Architecture/Mines/Materials/Mines_Scaffolding/MI_Mines_Scaffolding_D_Deco']
a = spawn_static_mesh(_brk_mesh, _brk_mats, (4717.693, 6470.675, 960.0), (0.0, -170.00011840810922, 0.0), (1.0, 1.0, 1.0), "BP_DM_Mines_Scaffolding_Support_2M10_5", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_brk_mesh, _brk_mats, (4778.369, 6586.719, 1000.4209), (69.73552460026814, -82.95795226435492, 15.07800219642101), (1.0, 1.0, 1.0), "BP_DM_Mines_Scaffolding_Support_2M11", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_brk_mesh, _brk_mats, (5053.832, 6938.744, 953.96875), (85.56359433290464, -34.20886586013868, 28.748454121182785), (1.0, 1.0, 1.0), "BP_DM_Mines_Scaffolding_Support_2M12", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_brk_mesh, _brk_mats, (7849.9995, 5369.998, 1080.0), (0.0, 179.99992486791828, -0.0), (1.0, 1.0, 1.0), "BP_DM_Mines_Scaffolding_Support_2M3", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_brk_mesh, _brk_mats, (7851.4746, 6953.669, 2384.1228), (0.00023300003914400414, -179.99980192454709, -89.99976644599158), (1.0, 1.0, 1.0), "BP_DM_Mines_Scaffolding_Support_2M34_57", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_brk_mesh, _brk_mats, (10201.47, 6043.6685, 2384.1226), (0.00023300003914400414, -179.99980192454709, -89.99976644599158), (1.0, 1.0, 1.0), "BP_DM_Mines_Scaffolding_Support_2M38_63", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_brk_mesh, _brk_mats, (7851.4756, 5453.666, 2384.1301), (0.00023300003914400414, -179.99980192454709, -89.99976644599158), (1.0, 1.0, 1.0), "BP_DM_Mines_Scaffolding_Support_2M39", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_brk_mesh, _brk_mats, (8149.9995, 5379.998, 1090.0), (0.0, 179.99992486791828, -0.0), (1.0, 1.0, 1.0), "BP_DM_Mines_Scaffolding_Support_2M4", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_brk_mesh, _brk_mats, (10201.47, 6943.6685, 2384.1248), (0.00023300003914400414, -179.99980192454709, -89.99976644599158), (1.0, 1.0, 1.0), "BP_DM_Mines_Scaffolding_Support_2M42_69", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_brk_mesh, _brk_mats, (7851.473, 7553.665, 2384.1355), (0.00023300003914400414, -179.99980192454709, -89.99976644599158), (1.0, 1.0, 1.0), "BP_DM_Mines_Scaffolding_Support_2M43", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_brk_mesh, _brk_mats, (7851.475, 6943.665, 2384.132), (0.00023300003914400414, -179.99980192454709, -89.99976644599158), (1.0, 1.0, 1.0), "BP_DM_Mines_Scaffolding_Support_2M44", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_brk_mesh, _brk_mats, (7876.4624, 7543.65, 2384.1301), (0.0002309020794245359, 89.99996218634284, -89.99962757829786), (1.0, 1.0, 1.0), "BP_DM_Mines_Scaffolding_Support_2M45", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_brk_mesh, _brk_mats, (8466.456, 7543.6504, 2384.13), (0.0002309020794245359, 89.99996218634284, -89.99962757829786), (1.0, 1.0, 1.0), "BP_DM_Mines_Scaffolding_Support_2M46", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_brk_mesh, _brk_mats, (10226.456, 7543.6484, 2384.1355), (0.0002309020794245359, 89.99996218634284, -89.99962757829786), (1.0, 1.0, 1.0), "BP_DM_Mines_Scaffolding_Support_2M47", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_brk_mesh, _brk_mats, (9366.456, 7543.6494, 2384.132), (0.0002309020794245359, 89.99996218634284, -89.99962757829786), (1.0, 1.0, 1.0), "BP_DM_Mines_Scaffolding_Support_2M48", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_brk_mesh, _brk_mats, (7876.4614, 5433.65, 2384.1301), (0.0002309020794245359, 89.99996218634284, -89.99962757829786), (1.0, 1.0, 1.0), "BP_DM_Mines_Scaffolding_Support_2M49", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_brk_mesh, _brk_mats, (8466.455, 5433.6504, 2384.13), (0.0002309020794245359, 89.99996218634284, -89.99962757829786), (1.0, 1.0, 1.0), "BP_DM_Mines_Scaffolding_Support_2M50", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_brk_mesh, _brk_mats, (9366.456, 5433.6494, 2384.132), (0.0002309020794245359, 89.99996218634284, -89.99962757829786), (1.0, 1.0, 1.0), "BP_DM_Mines_Scaffolding_Support_2M52", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_brk_mesh, _brk_mats, (4161.925, 6062.3535, 813.8032), (70.23827492166053, -90.00009970037718, 8.459516297703873), (1.0, 1.0, 1.0), "BP_DM_Mines_Scaffolding_Support_2M7_2", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_brk_mesh, _brk_mats, (4374.5625, 5541.009, 833.5908), (-69.69995045064034, -104.63150103582879, 24.786757295007053), (1.0, 1.0, 1.0), "BP_DM_Mines_Scaffolding_Support_2M9", _folder)
if a: placed += 1
else: skipped += 1

# Breakable Batch 35: BP_DM_Mines_Scaffolding_Support_3M (3 instances)
#   BP Class: /Game/LevelDesign/Deco_Architecture/Mines/BP_DM_Mines_Scaffolding_Support_3M
_brk_mesh = "/Game/Art/Assets/Kits/Deco_Architecture/Mines/Mines_Scaffolding_Support_3M"
_brk_mats = ['/Game/Art/Assets/Kits/Deco_Architecture/Mines/Materials/Mines_Scaffolding/MI_Mines_Scaffolding_D_Deco']
a = spawn_static_mesh(_brk_mesh, _brk_mats, (4460.6074, 6233.056, 960.0), (0.0, -79.9999683893994, 0.0), (1.0, 1.0, 1.0), "BP_DM_Mines_Scaffolding_Support_3M_2", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_brk_mesh, _brk_mats, (4472.1914, 6224.945, 960.0), (0.0, 10.00012155996466, -0.0), (1.0, 1.0, 1.0), "BP_DM_Mines_Scaffolding_Support_3M2", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_brk_mesh, _brk_mats, (4697.2744, 4638.056, 1420.0), (0.0, -169.99994970803522, 0.0), (1.0, 1.0, 1.0), "BP_DM_Mines_Scaffolding_Support_3M3", _folder)
if a: placed += 1
else: skipped += 1

# Breakable Batch 36: BP_Mines_Ceiling_Brace_A_Bracket (16 instances)
#   BP Class: /Game/LevelDesign/Deco_Architecture/Mines/BP_Mines_Ceiling_Brace_A_Bracket
_brk_mesh = "/Game/Art/Assets/Kits/Deco/Mines/Machine/Mines_Machine_Whim_Pieces/Mines_Machine_Whim_Side_Bracket"
_brk_mats = ['/Game/Art/Assets/Kits/Deco/Mines/Materials/Mines_Machine_Whim/MI_Mines_Machine_Whim_Trim', '/Game/Art/Assets/Kits/Deco/Mines/Materials/Mines_Machine_Whim/MI_Mines_Machine_Whim_Uniq']
a = spawn_static_mesh(_brk_mesh, _brk_mats, (10201.461, 6853.6675, 2384.1228), (90.0, 0.0, 269.99798777214323), (1.0, 1.0, 1.0), "BP_Mines_Ceiling_Brace_A_Bracket36_69", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_brk_mesh, _brk_mats, (10201.442, 7023.668, 2384.1228), (90.0, 35.047323430941496, 125.04501326474221), (1.0, 1.0, 1.0), "BP_Mines_Ceiling_Brace_A_Bracket39_74", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_brk_mesh, _brk_mats, (7851.475, 6403.6646, 2384.1301), (90.0, 35.047323430941496, 125.04501326474221), (1.0, 1.0, 1.0), "BP_Mines_Ceiling_Brace_A_Bracket41", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_brk_mesh, _brk_mats, (7851.448, 7023.6646, 2384.1301), (90.0, 26.70567390853551, 116.70347375033847), (1.0, 1.0, 1.0), "BP_Mines_Ceiling_Brace_A_Bracket43", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_brk_mesh, _brk_mats, (7851.4478, 7473.6636, 2384.1301), (90.0, -9.469762107327728, 260.52840442772805), (1.0, 1.0, 1.0), "BP_Mines_Ceiling_Brace_A_Bracket44", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_brk_mesh, _brk_mats, (7851.4937, 5493.664, 2384.1301), (90.0, 26.70567390853551, 116.70347375033847), (1.0, 1.0, 1.0), "BP_Mines_Ceiling_Brace_A_Bracket45", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_brk_mesh, _brk_mats, (7851.4937, 5943.665, 2384.1301), (90.0, -9.469762107327728, 260.52840442772805), (1.0, 1.0, 1.0), "BP_Mines_Ceiling_Brace_A_Bracket46", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_brk_mesh, _brk_mats, (8526.454, 7543.6504, 2384.1301), (90.0, -1.9755582678690489, -181.97807392435323), (1.0, 1.0, 1.0), "BP_Mines_Ceiling_Brace_A_Bracket47", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_brk_mesh, _brk_mats, (9276.454, 7543.6577, 2384.1301), (90.0, 5.25049682493441, 5.248423687362247), (1.0, 1.0, 1.0), "BP_Mines_Ceiling_Brace_A_Bracket48", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_brk_mesh, _brk_mats, (9446.453, 7543.6753, 2384.1301), (90.0, -9.568270469089011, -189.57049815601954), (1.0, 1.0, 1.0), "BP_Mines_Ceiling_Brace_A_Bracket49", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_brk_mesh, _brk_mats, (7916.457, 7543.631, 2384.1301), (90.0, -9.568270469089011, -189.57049815601954), (1.0, 1.0, 1.0), "BP_Mines_Ceiling_Brace_A_Bracket51", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_brk_mesh, _brk_mats, (8526.454, 5433.65, 2384.1301), (90.0, -0.6586594290131387, -180.6610813595264), (1.0, 1.0, 1.0), "BP_Mines_Ceiling_Brace_A_Bracket53", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_brk_mesh, _brk_mats, (9276.453, 5433.6577, 2384.1301), (90.0, 5.25049682493441, 5.248423687362247), (1.0, 1.0, 1.0), "BP_Mines_Ceiling_Brace_A_Bracket54", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_brk_mesh, _brk_mats, (9446.453, 5433.675, 2384.1301), (90.0, -20.189620344412848, -200.1919192690691), (1.0, 1.0, 1.0), "BP_Mines_Ceiling_Brace_A_Bracket55", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_brk_mesh, _brk_mats, (7916.458, 5433.632, 2384.1301), (90.0, -20.189620344412848, -200.1919192690691), (1.0, 1.0, 1.0), "BP_Mines_Ceiling_Brace_A_Bracket57", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_brk_mesh, _brk_mats, (8366.455, 5433.6313, 2384.1301), (90.0, 5.25049682493441, 5.248423687362247), (1.0, 1.0, 1.0), "BP_Mines_Ceiling_Brace_A_Bracket58", _folder)
if a: placed += 1
else: skipped += 1

# Breakable Batch 37: BP_Mines_Support_Beam (38 instances)
#   BP Class: /Game/LevelDesign/Deco_Architecture/Mines/BP_Mines_Support_Beam
_brk_mesh = "/Game/Art/Assets/Kits/Deco/Mines/Machine/Mines_Machine_Whim_Pieces/Mines_Machine_Whim_Wheel_Middle_Bracket"
_brk_mats = ['/Game/Art/Assets/Kits/Deco/Mines/Materials/Mines_Machine_Whim/MI_Mines_Machine_Whim_Trim', '/Game/Art/Assets/Kits/Deco/Mines/Materials/Mines_Machine_Whim/MI_Mines_Machine_Whim_Uniq']
a = spawn_static_mesh(_brk_mesh, _brk_mats, (10639.979, 5540.2383, 690.0), (0.0, -79.99993888328352, 0.0), (1.0, 1.0, 1.0), "BP_Mines_Support_Beam10", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_brk_mesh, _brk_mats, (7851.4736, 5353.667, 2404.1226), (90.0, -12.104453513704819, 77.89339445642955), (1.0, 1.0, 1.0), "BP_Mines_Support_Beam22", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_brk_mesh, _brk_mats, (8151.468, 5353.666, 2394.121), (90.0, -12.104453513704819, 77.89339445642955), (1.0, 1.0, 1.0), "BP_Mines_Support_Beam24", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_brk_mesh, _brk_mats, (8456.103, 5353.668, 2378.0903), (-90.0, -90.16437786057757, 180.162881294727), (1.0, 1.0, 1.0), "BP_Mines_Support_Beam30", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_brk_mesh, _brk_mats, (8746.103, 5353.668, 2378.0903), (-90.0, 9.49301088786758, 80.50541462389107), (1.0, 1.0, 1.0), "BP_Mines_Support_Beam32", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_brk_mesh, _brk_mats, (9046.103, 5353.668, 2378.0903), (-90.0, -90.16437786057757, 180.162881294727), (1.0, 1.0, 1.0), "BP_Mines_Support_Beam34", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_brk_mesh, _brk_mats, (9346.103, 5353.668, 2378.0903), (-90.0, -16.7131321255899, 106.71161493316643), (1.0, 1.0, 1.0), "BP_Mines_Support_Beam36", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_brk_mesh, _brk_mats, (9646.103, 5353.668, 2378.0903), (-90.0, 138.06313150638695, -48.06467161700178), (1.0, 1.0, 1.0), "BP_Mines_Support_Beam38", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_brk_mesh, _brk_mats, (10201.468, 6633.668, 2754.121), (-0.00021362309926876356, 89.99988152481276, 179.99814901877687), (1.0, 1.0, 1.0), "BP_Mines_Support_Beam44", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_brk_mesh, _brk_mats, (10201.444, 7623.667, 2584.123), (90.0, 91.00392313340085, 1.001780271033013), (1.0, 1.0, 1.0), "BP_Mines_Support_Beam47", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_brk_mesh, _brk_mats, (10201.452, 7253.668, 2754.121), (-0.00021362309926876356, 89.99988152481276, 179.99814901877687), (1.0, 1.0, 1.0), "BP_Mines_Support_Beam48_82", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_brk_mesh, _brk_mats, (7851.4736, 7323.6685, 2584.123), (90.0, 91.00392313340085, 1.001780271033013), (1.0, 1.0, 1.0), "BP_Mines_Support_Beam49", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_brk_mesh, _brk_mats, (10201.468, 6333.668, 2754.1226), (-0.00021362309926876356, 89.99988152481276, 179.99814901877687), (1.0, 1.0, 1.0), "BP_Mines_Support_Beam50_84", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_brk_mesh, _brk_mats, (7851.473, 5353.664, 2584.1304), (90.0, 35.047323430941496, 125.04501326474221), (1.0, 1.0, 1.0), "BP_Mines_Support_Beam51", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_brk_mesh, _brk_mats, (7851.473, 6633.664, 2754.1284), (-0.00021362309926876356, 89.99988152481276, 179.99814901877687), (1.0, 1.0, 1.0), "BP_Mines_Support_Beam52", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_brk_mesh, _brk_mats, (7851.4727, 5733.664, 2754.13), (-0.00021362309926876356, 89.99988152481276, 179.99814901877687), (1.0, 1.0, 1.0), "BP_Mines_Support_Beam53", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_brk_mesh, _brk_mats, (7851.449, 7623.6646, 2584.1304), (90.0, 91.00392313340085, 1.001780271033013), (1.0, 1.0, 1.0), "BP_Mines_Support_Beam54", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_brk_mesh, _brk_mats, (7851.457, 7253.6646, 2754.1284), (-0.00021362309926876356, 89.99988152481276, 179.99814901877687), (1.0, 1.0, 1.0), "BP_Mines_Support_Beam55", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_brk_mesh, _brk_mats, (7851.473, 6333.6646, 2754.13), (-0.00021362309926876356, 89.99988152481276, 179.99814901877687), (1.0, 1.0, 1.0), "BP_Mines_Support_Beam56", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_brk_mesh, _brk_mats, (7851.478, 7623.6675, 2404.1223), (90.0, 91.00392313340085, 1.001780271033013), (1.0, 1.0, 1.0), "BP_Mines_Support_Beam57", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_brk_mesh, _brk_mats, (8151.476, 7623.666, 2394.1208), (90.0, -90.55359853239582, -180.5558559863341), (1.0, 1.0, 1.0), "BP_Mines_Support_Beam58", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_brk_mesh, _brk_mats, (8456.117, 7623.668, 2378.09), (-90.0, 153.68578310973209, -243.68874644762565), (1.0, 1.0, 1.0), "BP_Mines_Support_Beam59", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_brk_mesh, _brk_mats, (10342.8, 5497.9917, 690.0), (0.0, -79.99993888328352, 0.0), (1.0, 1.0, 1.0), "BP_Mines_Support_Beam6_5", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_brk_mesh, _brk_mats, (8746.113, 7623.668, 2378.09), (-90.0, 4.091326692387468, 265.9058176856196), (1.0, 1.0, 1.0), "BP_Mines_Support_Beam60", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_brk_mesh, _brk_mats, (9046.113, 7623.6675, 2378.09), (-90.0, 153.68578310973209, -243.68874644762565), (1.0, 1.0, 1.0), "BP_Mines_Support_Beam61", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_brk_mesh, _brk_mats, (9346.113, 7623.668, 2378.09), (-90.0, 4.091326692387468, 265.9058176856196), (1.0, 1.0, 1.0), "BP_Mines_Support_Beam62", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_brk_mesh, _brk_mats, (7776.459, 7543.653, 2584.1304), (90.0, -1.9755582678690489, -181.97807392435323), (1.0, 1.0, 1.0), "BP_Mines_Support_Beam65", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_brk_mesh, _brk_mats, (9056.454, 7543.6514, 2754.1284), (-0.00021362305217697368, -0.00015258788408756624, 179.998149018875), (1.0, 1.0, 1.0), "BP_Mines_Support_Beam66", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_brk_mesh, _brk_mats, (8156.4595, 7543.651, 2754.13), (-0.00021362305217697368, -0.00015258788408756624, 179.998149018875), (1.0, 1.0, 1.0), "BP_Mines_Support_Beam67", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_brk_mesh, _brk_mats, (7851.473, 6043.6646, 2754.13), (-0.00021362309926876356, 89.99988152481276, 179.99814901877687), (1.0, 1.0, 1.0), "BP_Mines_Support_Beam68", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_brk_mesh, _brk_mats, (9676.453, 7543.667, 2754.1284), (-0.00021362305217697368, -0.00015258788408756624, 179.998149018875), (1.0, 1.0, 1.0), "BP_Mines_Support_Beam69", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_brk_mesh, _brk_mats, (8756.452, 7543.6514, 2754.13), (-0.00021362305217697368, -0.00015258788408756624, 179.998149018875), (1.0, 1.0, 1.0), "BP_Mines_Support_Beam70", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_brk_mesh, _brk_mats, (7776.4595, 5433.6523, 2584.1304), (90.0, -0.6586594290131387, -180.6610813595264), (1.0, 1.0, 1.0), "BP_Mines_Support_Beam71", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_brk_mesh, _brk_mats, (9056.454, 5433.652, 2754.1284), (-0.00021362305217697368, -0.00015258788408756624, 179.998149018875), (1.0, 1.0, 1.0), "BP_Mines_Support_Beam72", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_brk_mesh, _brk_mats, (8156.457, 5433.651, 2754.13), (-0.00021362305217697368, -0.00015258788408756624, 179.998149018875), (1.0, 1.0, 1.0), "BP_Mines_Support_Beam73", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_brk_mesh, _brk_mats, (9676.455, 5433.667, 2754.1284), (-0.00021362305217697368, -0.00015258788408756624, 179.998149018875), (1.0, 1.0, 1.0), "BP_Mines_Support_Beam75", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_brk_mesh, _brk_mats, (8756.452, 5433.651, 2754.13), (-0.00021362305217697368, -0.00015258788408756624, 179.998149018875), (1.0, 1.0, 1.0), "BP_Mines_Support_Beam76", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_brk_mesh, _brk_mats, (10393.158, 5212.398, 690.0), (0.0, -79.99993888328352, 0.0), (1.0, 1.0, 1.0), "BP_Mines_Support_Beam8_7", _folder)
if a: placed += 1
else: skipped += 1

# Breakable Batch 38: BP_Mines_Support_Beam_B (110 instances)
#   BP Class: /Game/LevelDesign/Deco_Architecture/Mines/BP_Mines_Support_Beam_B
_brk_mesh = "/Game/Art/Assets/Kits/Deco/Mines/Machine/Mines_Machine_Whim_Pieces/Mines_Machine_Whim_Wheel_Middle_Bracket_B"
_brk_mats = ['/Game/Art/Assets/Kits/Deco/Mines/Materials/Mines_Machine_Whim/MI_Mines_Machine_Whim_Trim']
a = spawn_static_mesh(_brk_mesh, _brk_mats, (9943.789, 5745.5156, 2391.1062), (0.0002049056702727294, 0.00010013581169472522, 90.00026882293402), (1.0, 1.0, 1.0), "BP_Mines_Support_Beam_B103", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_brk_mesh, _brk_mats, (7853.7856, 5465.5146, 2391.1072), (0.00023300003914400414, -179.99980192454709, -89.99976644599158), (1.0, 1.0, 1.0), "BP_Mines_Support_Beam_B104", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_brk_mesh, _brk_mats, (8453.788, 5465.516, 2391.1074), (0.0002049056702727294, 0.00010013581169472522, 90.00026882293402), (1.0, 1.0, 1.0), "BP_Mines_Support_Beam_B109", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_brk_mesh, _brk_mats, (8743.788, 5465.5166, 2391.1074), (0.0002049056702727294, 0.00010013581169472522, 90.00026882293402), (1.0, 1.0, 1.0), "BP_Mines_Support_Beam_B110", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_brk_mesh, _brk_mats, (10342.818, 5511.212, 1071.8486), (0.0, 100.00013657266632, -0.0), (1.0, 1.0, 1.0), "BP_Mines_Support_Beam_B130", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_brk_mesh, _brk_mats, (9043.788, 5465.5166, 2391.1074), (0.0002049056702727294, 0.00010013581169472522, 90.00026882293402), (1.0, 1.0, 1.0), "BP_Mines_Support_Beam_B131_308", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_brk_mesh, _brk_mats, (9343.788, 5465.516, 2391.1074), (0.0002049056702727294, 0.00010013581169472522, 90.00026882293402), (1.0, 1.0, 1.0), "BP_Mines_Support_Beam_B132_309", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_brk_mesh, _brk_mats, (7852.3115, 4703.0146, 1181.8486), (0.0, 179.99992486791828, -0.0), (1.0, 1.0, 1.0), "BP_Mines_Support_Beam_B134_63", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_brk_mesh, _brk_mats, (8142.3115, 4703.014, 1181.8486), (0.0, 179.99992486791828, -0.0), (1.0, 1.0, 1.0), "BP_Mines_Support_Beam_B135_65", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_brk_mesh, _brk_mats, (8422.3125, 4713.0127, 871.84863), (-90.0, -53.120723585533185, 233.1202188846368), (1.0, 1.0, 1.0), "BP_Mines_Support_Beam_B136", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_brk_mesh, _brk_mats, (8452.312, 4717.156, 1181.8486), (0.0, 134.99996049089222, -0.0), (1.0, 1.0, 1.0), "BP_Mines_Support_Beam_B137", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_brk_mesh, _brk_mats, (8632.312, 4503.0127, 871.84863), (-90.0, -53.120723585533185, 233.1202188846368), (1.0, 1.0, 1.0), "BP_Mines_Support_Beam_B138", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_brk_mesh, _brk_mats, (8662.312, 4513.0137, 1181.8486), (0.0, 89.99997063746636, -0.0), (1.0, 1.0, 1.0), "BP_Mines_Support_Beam_B140", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_brk_mesh, _brk_mats, (7875.039, 4812.386, 1021.84863), (-16.81896980932386, 3.051757469043822e-05, 179.99971996227157), (1.0, 1.0, 1.0), "BP_Mines_Support_Beam_B141", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_brk_mesh, _brk_mats, (7706.593, 4795.4106, 1043.2383), (-65.06205180968676, 115.5800487646397, 74.08488076113161), (1.0, 1.0, 1.0), "BP_Mines_Support_Beam_B142", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_brk_mesh, _brk_mats, (9643.788, 5465.516, 2391.1074), (0.0002049056702727294, 0.00010013581169472522, 90.00026882293402), (1.0, 1.0, 1.0), "BP_Mines_Support_Beam_B143_310", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_brk_mesh, _brk_mats, (7853.7866, 5735.5146, 2361.1077), (2.0490563900662142e-05, -89.99964652502241, -179.99950822620508), (1.0, 1.0, 1.0), "BP_Mines_Support_Beam_B194", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_brk_mesh, _brk_mats, (8153.786, 5735.5127, 2361.1057), (0.0002322263490475381, -89.99974375861743, -179.99938528274294), (1.0, 1.0, 1.0), "BP_Mines_Support_Beam_B195", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_brk_mesh, _brk_mats, (7853.786, 6035.5166, 2361.1077), (0.0002322263490475381, -89.99974375861743, -179.99938528274294), (1.0, 1.0, 1.0), "BP_Mines_Support_Beam_B196", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_brk_mesh, _brk_mats, (8153.7876, 6035.5166, 2361.1062), (-6.103513303232726e-05, -89.99997063827263, -179.99963116978532), (1.0, 1.0, 1.0), "BP_Mines_Support_Beam_B197", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_brk_mesh, _brk_mats, (7853.789, 6065.5137, 2391.1064), (0.00023300003914400414, -179.99980192454709, -89.99976644599158), (1.0, 1.0, 1.0), "BP_Mines_Support_Beam_B198", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_brk_mesh, _brk_mats, (7853.785, 6335.5166, 2361.1077), (0.0002322263490475381, -89.99974375861743, -179.99938528274294), (1.0, 1.0, 1.0), "BP_Mines_Support_Beam_B199_178", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_brk_mesh, _brk_mats, (7853.787, 6355.5176, 2391.107), (0.00023300003914400414, -179.99980192454709, -89.99976644599158), (1.0, 1.0, 1.0), "BP_Mines_Support_Beam_B200", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_brk_mesh, _brk_mats, (8153.788, 6335.515, 2361.1062), (-6.103513303232726e-05, -89.99997063827263, -179.99963116978532), (1.0, 1.0, 1.0), "BP_Mines_Support_Beam_B201_179", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_brk_mesh, _brk_mats, (7853.789, 6665.5146, 2391.1064), (0.00023300003914400414, -179.99980192454709, -89.99976644599158), (1.0, 1.0, 1.0), "BP_Mines_Support_Beam_B202_182", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_brk_mesh, _brk_mats, (8453.786, 5735.5156, 2421.1057), (7.513209643057401e-05, -89.99991067679684, 0.000366210942303134), (1.0, 1.0, 1.0), "BP_Mines_Support_Beam_B203_196", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_brk_mesh, _brk_mats, (7853.789, 6975.514, 2391.1064), (0.00023300003914400414, -179.99980192454709, -89.99976644599158), (1.0, 1.0, 1.0), "BP_Mines_Support_Beam_B204_186", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_brk_mesh, _brk_mats, (8453.786, 6035.5156, 2421.1057), (7.500002813286983e-05, -89.99991067679719, 0.00036621093410036293), (1.0, 1.0, 1.0), "BP_Mines_Support_Beam_B206_2", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_brk_mesh, _brk_mats, (8453.786, 6335.5156, 2421.1057), (7.500002813286983e-05, -89.99991067679719, 0.00036621093410036293), (1.0, 1.0, 1.0), "BP_Mines_Support_Beam_B207", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_brk_mesh, _brk_mats, (8453.786, 6635.5156, 2421.1057), (7.500002813286983e-05, -89.99991067679719, 0.00036621093410036293), (1.0, 1.0, 1.0), "BP_Mines_Support_Beam_B208", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_brk_mesh, _brk_mats, (8453.784, 6065.515, 2391.1064), (0.00019124527254428682, 0.00010871885429563705, 90.0002396526224), (1.0, 1.0, 1.0), "BP_Mines_Support_Beam_B210_198", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_brk_mesh, _brk_mats, (8453.784, 6665.515, 2391.1064), (0.00019124527254428682, 0.00010871885429563705, 90.0002396526224), (1.0, 1.0, 1.0), "BP_Mines_Support_Beam_B214_203", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_brk_mesh, _brk_mats, (8453.784, 6975.515, 2391.1064), (0.00019124527254428682, 0.00010871885429563705, 90.0002396526224), (1.0, 1.0, 1.0), "BP_Mines_Support_Beam_B215_204", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_brk_mesh, _brk_mats, (8743.786, 5735.5156, 2421.1057), (7.513209643057401e-05, -89.99991067679684, 0.000366210942303134), (1.0, 1.0, 1.0), "BP_Mines_Support_Beam_B216_214", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_brk_mesh, _brk_mats, (8753.784, 6975.515, 2391.108), (0.00019099999311025312, 0.00010899999582792963, 90.00023965262248), (1.0, 1.0, 1.0), "BP_Mines_Support_Beam_B217", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_brk_mesh, _brk_mats, (9053.784, 6975.515, 2391.1094), (0.00019099999311025312, 0.00010899999582792963, 90.00023965262248), (1.0, 1.0, 1.0), "BP_Mines_Support_Beam_B219", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_brk_mesh, _brk_mats, (9353.784, 6975.515, 2391.1108), (0.00019099999311025312, 0.00010899999582792963, 90.00023965262248), (1.0, 1.0, 1.0), "BP_Mines_Support_Beam_B220", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_brk_mesh, _brk_mats, (9653.784, 6975.515, 2391.1123), (0.00019099999311025312, 0.00010899999582792963, 90.00023965262248), (1.0, 1.0, 1.0), "BP_Mines_Support_Beam_B222", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_brk_mesh, _brk_mats, (9043.785, 5735.5156, 2421.1057), (7.513209643057401e-05, -89.99991067679684, 0.000366210942303134), (1.0, 1.0, 1.0), "BP_Mines_Support_Beam_B224_231", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_brk_mesh, _brk_mats, (9343.786, 5735.5156, 2421.1057), (7.513209643057401e-05, -89.99991067679684, 0.000366210942303134), (1.0, 1.0, 1.0), "BP_Mines_Support_Beam_B232", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_brk_mesh, _brk_mats, (9643.786, 5735.5156, 2421.1057), (7.513209643057401e-05, -89.99991067679684, 0.000366210942303134), (1.0, 1.0, 1.0), "BP_Mines_Support_Beam_B240", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_brk_mesh, _brk_mats, (9908.787, 5735.515, 2421.1057), (7.513209643057401e-05, -89.99991067679684, 0.000366210942303134), (1.0, 1.0, 1.0), "BP_Mines_Support_Beam_B248", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_brk_mesh, _brk_mats, (9908.788, 6035.517, 2421.1047), (-0.00015258790673440797, -90.00002735856917, 0.00036621093650409693), (1.0, 1.0, 1.0), "BP_Mines_Support_Beam_B249", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_brk_mesh, _brk_mats, (9943.785, 6065.515, 2391.1064), (0.00019124527254428682, 0.00010871885429563705, 90.0002396526224), (1.0, 1.0, 1.0), "BP_Mines_Support_Beam_B250", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_brk_mesh, _brk_mats, (9983.785, 6355.518, 2391.1064), (0.0002049056702727294, 0.00010013581169472522, 90.00026882293402), (1.0, 1.0, 1.0), "BP_Mines_Support_Beam_B251", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_brk_mesh, _brk_mats, (9908.787, 6635.515, 2421.1057), (7.500002813286983e-05, -89.99991067679719, 0.00036621093410036293), (1.0, 1.0, 1.0), "BP_Mines_Support_Beam_B252", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_brk_mesh, _brk_mats, (9908.788, 6335.517, 2421.1047), (-0.00015258790673440797, -90.00002735856917, 0.00036621093650409693), (1.0, 1.0, 1.0), "BP_Mines_Support_Beam_B253", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_brk_mesh, _brk_mats, (9983.783, 6665.515, 2391.1067), (0.00019124527254428682, 0.00010871885429563705, 90.0002396526224), (1.0, 1.0, 1.0), "BP_Mines_Support_Beam_B254", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_brk_mesh, _brk_mats, (9943.784, 6975.515, 2391.1064), (0.00019124527254428682, 0.00010871885429563705, 90.0002396526224), (1.0, 1.0, 1.0), "BP_Mines_Support_Beam_B255", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_brk_mesh, _brk_mats, (10203.78, 5735.515, 2361.1077), (2.0490563900662142e-05, -89.99964652502241, -179.99950822620508), (1.0, 1.0, 1.0), "BP_Mines_Support_Beam_B256_269", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_brk_mesh, _brk_mats, (10203.78, 6035.517, 2361.1077), (0.0002322263490475381, -89.99974375861743, -179.99938528274294), (1.0, 1.0, 1.0), "BP_Mines_Support_Beam_B257_270", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_brk_mesh, _brk_mats, (10193.783, 5735.5176, 2541.1074), (-3.051758477152455e-05, -90.00010028326501, -179.99980192456547), (1.0, 1.0, 1.0), "BP_Mines_Support_Beam_B258", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_brk_mesh, _brk_mats, (10193.782, 6035.5166, 2541.1074), (-3.051758477152455e-05, -90.00010028326501, -179.99980192456547), (1.0, 1.0, 1.0), "BP_Mines_Support_Beam_B259", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_brk_mesh, _brk_mats, (10203.78, 6335.517, 2361.1077), (0.0002322263490475381, -89.99974375861743, -179.99938528274294), (1.0, 1.0, 1.0), "BP_Mines_Support_Beam_B260", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_brk_mesh, _brk_mats, (10193.782, 6335.516, 2541.1074), (-3.051758477152455e-05, -90.00010028326501, -179.99980192456547), (1.0, 1.0, 1.0), "BP_Mines_Support_Beam_B261", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_brk_mesh, _brk_mats, (7853.7856, 6635.5166, 2361.1077), (0.0002322263490475381, -89.99974375861743, -179.99938528274294), (1.0, 1.0, 1.0), "BP_Mines_Support_Beam_B262", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_brk_mesh, _brk_mats, (8153.788, 6635.5156, 2361.1062), (-6.103513303232726e-05, -89.99997063827263, -179.99963116978532), (1.0, 1.0, 1.0), "BP_Mines_Support_Beam_B263", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_brk_mesh, _brk_mats, (10193.787, 6635.517, 2421.1047), (-0.00015258790673440797, -90.00002735856917, 0.00036621093650409693), (1.0, 1.0, 1.0), "BP_Mines_Support_Beam_B269", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_brk_mesh, _brk_mats, (7853.786, 6935.517, 2361.1077), (0.0002322263490475381, -89.99974375861743, -179.99938528274294), (1.0, 1.0, 1.0), "BP_Mines_Support_Beam_B270", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_brk_mesh, _brk_mats, (8153.7886, 6935.5156, 2361.1062), (-6.103513303232726e-05, -89.99997063827263, -179.99963116978532), (1.0, 1.0, 1.0), "BP_Mines_Support_Beam_B271", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_brk_mesh, _brk_mats, (8453.789, 6935.5166, 2421.1047), (-0.00015258790673440797, -90.00002735856917, 0.00036621093650409693), (1.0, 1.0, 1.0), "BP_Mines_Support_Beam_B272", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_brk_mesh, _brk_mats, (9043.789, 6935.517, 2421.1047), (-0.00015258790673440797, -90.00002735856917, 0.00036621093650409693), (1.0, 1.0, 1.0), "BP_Mines_Support_Beam_B274", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_brk_mesh, _brk_mats, (9343.789, 6935.5166, 2421.1047), (-0.00015258790673440797, -90.00002735856917, 0.00036621093650409693), (1.0, 1.0, 1.0), "BP_Mines_Support_Beam_B275", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_brk_mesh, _brk_mats, (9643.789, 6935.517, 2421.1047), (-0.00015258790673440797, -90.00002735856917, 0.00036621093650409693), (1.0, 1.0, 1.0), "BP_Mines_Support_Beam_B276", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_brk_mesh, _brk_mats, (10193.788, 6935.517, 2421.1047), (-0.00015258790673440797, -90.00002735856917, 0.00036621093650409693), (1.0, 1.0, 1.0), "BP_Mines_Support_Beam_B277", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_brk_mesh, _brk_mats, (7853.789, 7275.513, 2391.105), (0.00023300003914400414, -179.99980192454709, -89.99976644599158), (1.0, 1.0, 1.0), "BP_Mines_Support_Beam_B278", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_brk_mesh, _brk_mats, (8453.785, 7275.515, 2391.105), (0.00019124527254428682, 0.00010871885429563705, 90.0002396526224), (1.0, 1.0, 1.0), "BP_Mines_Support_Beam_B279", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_brk_mesh, _brk_mats, (8743.784, 7275.515, 2391.105), (0.00019124527254428682, 0.00010871885429563705, 90.0002396526224), (1.0, 1.0, 1.0), "BP_Mines_Support_Beam_B280", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_brk_mesh, _brk_mats, (9043.784, 7275.515, 2391.105), (0.00019124527254428682, 0.00010871885429563705, 90.0002396526224), (1.0, 1.0, 1.0), "BP_Mines_Support_Beam_B281", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_brk_mesh, _brk_mats, (9343.784, 7275.515, 2391.105), (0.00019124527254428682, 0.00010871885429563705, 90.0002396526224), (1.0, 1.0, 1.0), "BP_Mines_Support_Beam_B282", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_brk_mesh, _brk_mats, (9643.784, 7275.5146, 2391.105), (0.00019124527254428682, 0.00010871885429563705, 90.0002396526224), (1.0, 1.0, 1.0), "BP_Mines_Support_Beam_B283", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_brk_mesh, _brk_mats, (9943.784, 7275.515, 2391.105), (0.00019124527254428682, 0.00010871885429563705, 90.0002396526224), (1.0, 1.0, 1.0), "BP_Mines_Support_Beam_B284", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_brk_mesh, _brk_mats, (7853.789, 7575.514, 2391.1033), (0.00023300003914400414, -179.99980192454709, -89.99976644599158), (1.0, 1.0, 1.0), "BP_Mines_Support_Beam_B285", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_brk_mesh, _brk_mats, (8453.788, 7575.5156, 2391.1033), (0.00019124527254428682, 0.00010871885429563705, 90.0002396526224), (1.0, 1.0, 1.0), "BP_Mines_Support_Beam_B286", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_brk_mesh, _brk_mats, (8743.784, 7575.5156, 2391.1033), (0.00019124527254428682, 0.00010871885429563705, 90.0002396526224), (1.0, 1.0, 1.0), "BP_Mines_Support_Beam_B287", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_brk_mesh, _brk_mats, (9043.784, 7575.515, 2391.1033), (0.00019124527254428682, 0.00010871885429563705, 90.0002396526224), (1.0, 1.0, 1.0), "BP_Mines_Support_Beam_B288", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_brk_mesh, _brk_mats, (9343.784, 7575.515, 2391.1033), (0.00019124527254428682, 0.00010871885429563705, 90.0002396526224), (1.0, 1.0, 1.0), "BP_Mines_Support_Beam_B289", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_brk_mesh, _brk_mats, (9643.784, 7575.5156, 2391.1033), (0.00019124527254428682, 0.00010871885429563705, 90.0002396526224), (1.0, 1.0, 1.0), "BP_Mines_Support_Beam_B290", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_brk_mesh, _brk_mats, (9943.784, 7575.515, 2391.1033), (0.00019099999311025312, 0.00010899999582792963, 90.00023965262248), (1.0, 1.0, 1.0), "BP_Mines_Support_Beam_B291_500", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_brk_mesh, _brk_mats, (10193.78, 6635.517, 2541.1072), (-3.051758477152455e-05, -90.00010028326501, -179.99980192456547), (1.0, 1.0, 1.0), "BP_Mines_Support_Beam_B292", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_brk_mesh, _brk_mats, (10193.781, 6935.516, 2541.1072), (-3.051758477152455e-05, -90.00010028326501, -179.99980192456547), (1.0, 1.0, 1.0), "BP_Mines_Support_Beam_B293", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_brk_mesh, _brk_mats, (7843.787, 5735.513, 2541.1147), (-3.051758477152455e-05, -90.00010028326501, -179.99980192456547), (1.0, 1.0, 1.0), "BP_Mines_Support_Beam_B294_320", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_brk_mesh, _brk_mats, (7843.787, 6035.5127, 2541.1147), (-3.051758477152455e-05, -90.00010028326501, -179.99980192456547), (1.0, 1.0, 1.0), "BP_Mines_Support_Beam_B295", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_brk_mesh, _brk_mats, (7843.787, 6335.5127, 2541.1147), (-3.051758477152455e-05, -90.00010028326501, -179.99980192456547), (1.0, 1.0, 1.0), "BP_Mines_Support_Beam_B296", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_brk_mesh, _brk_mats, (7843.786, 6635.5137, 2541.1145), (-3.051758477152455e-05, -90.00010028326501, -179.99980192456547), (1.0, 1.0, 1.0), "BP_Mines_Support_Beam_B297", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_brk_mesh, _brk_mats, (7843.7866, 6935.512, 2541.1145), (-3.051758477152455e-05, -90.00010028326501, -179.99980192456547), (1.0, 1.0, 1.0), "BP_Mines_Support_Beam_B298", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_brk_mesh, _brk_mats, (8158.3076, 7551.338, 2541.1147), (-3.051757142667194e-05, 179.9998838867657, -179.99976777354388), (1.0, 1.0, 1.0), "BP_Mines_Support_Beam_B299", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_brk_mesh, _brk_mats, (8458.305, 7551.338, 2541.1147), (-3.051757142667194e-05, 179.9998838867657, -179.99976777354388), (1.0, 1.0, 1.0), "BP_Mines_Support_Beam_B300", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_brk_mesh, _brk_mats, (8758.303, 7551.338, 2541.1147), (-3.051757142667194e-05, 179.9998838867657, -179.99976777354388), (1.0, 1.0, 1.0), "BP_Mines_Support_Beam_B301", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_brk_mesh, _brk_mats, (9058.305, 7551.3354, 2541.1145), (-3.051757142667194e-05, 179.9998838867657, -179.99976777354388), (1.0, 1.0, 1.0), "BP_Mines_Support_Beam_B302", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_brk_mesh, _brk_mats, (9358.304, 7551.339, 2541.1145), (-3.051757142667194e-05, 179.9998838867657, -179.99976777354388), (1.0, 1.0, 1.0), "BP_Mines_Support_Beam_B303", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_brk_mesh, _brk_mats, (8158.3047, 5441.338, 2541.1147), (-3.051757142667194e-05, 179.9998838867657, -179.99976777354388), (1.0, 1.0, 1.0), "BP_Mines_Support_Beam_B304", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_brk_mesh, _brk_mats, (8458.302, 5441.338, 2541.1147), (-3.051757142667194e-05, 179.9998838867657, -179.99976777354388), (1.0, 1.0, 1.0), "BP_Mines_Support_Beam_B305", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_brk_mesh, _brk_mats, (8758.303, 5441.338, 2541.1147), (-3.051757142667194e-05, 179.9998838867657, -179.99976777354388), (1.0, 1.0, 1.0), "BP_Mines_Support_Beam_B306", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_brk_mesh, _brk_mats, (9058.304, 5441.336, 2541.1145), (-3.051757142667194e-05, 179.9998838867657, -179.99976777354388), (1.0, 1.0, 1.0), "BP_Mines_Support_Beam_B307", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_brk_mesh, _brk_mats, (9358.303, 5441.339, 2541.1145), (-3.051757142667194e-05, 179.9998838867657, -179.99976777354388), (1.0, 1.0, 1.0), "BP_Mines_Support_Beam_B308", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_brk_mesh, _brk_mats, (10243.784, 7575.5156, 2391.1033), (0.00019099999311025312, 0.00010899999582792963, 90.00023965262248), (1.0, 1.0, 1.0), "BP_Mines_Support_Beam_B310_501", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_brk_mesh, _brk_mats, (9658.305, 7551.3354, 2541.1145), (-3.051757142667194e-05, 179.9998838867657, -179.99976777354388), (1.0, 1.0, 1.0), "BP_Mines_Support_Beam_B311", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_brk_mesh, _brk_mats, (9958.304, 7551.339, 2541.1145), (-3.051757142667194e-05, 179.9998838867657, -179.99976777354388), (1.0, 1.0, 1.0), "BP_Mines_Support_Beam_B312", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_brk_mesh, _brk_mats, (10243.785, 6065.515, 2391.1064), (0.00019099999311025312, 0.00010899999582792963, 90.00023965262248), (1.0, 1.0, 1.0), "BP_Mines_Support_Beam_B315", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_brk_mesh, _brk_mats, (10283.785, 6355.518, 2391.1064), (0.00020500001608744634, 0.00010000001224822235, 90.00026882293392), (1.0, 1.0, 1.0), "BP_Mines_Support_Beam_B316", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_brk_mesh, _brk_mats, (10283.783, 6665.515, 2391.1067), (0.00019099999311025312, 0.00010899999582792963, 90.00023965262248), (1.0, 1.0, 1.0), "BP_Mines_Support_Beam_B317", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_brk_mesh, _brk_mats, (10243.784, 6975.515, 2391.1064), (0.00019099999311025312, 0.00010899999582792963, 90.00023965262248), (1.0, 1.0, 1.0), "BP_Mines_Support_Beam_B318", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_brk_mesh, _brk_mats, (10243.784, 7275.515, 2391.105), (0.00019099999311025312, 0.00010899999582792963, 90.00023965262248), (1.0, 1.0, 1.0), "BP_Mines_Support_Beam_B319", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_brk_mesh, _brk_mats, (9043.788, 5745.5166, 2391.1062), (0.0002049056702727294, 0.00010013581169472522, 90.00026882293402), (1.0, 1.0, 1.0), "BP_Mines_Support_Beam_B93", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_brk_mesh, _brk_mats, (9343.789, 5745.516, 2391.1062), (0.0002049056702727294, 0.00010013581169472522, 90.00026882293402), (1.0, 1.0, 1.0), "BP_Mines_Support_Beam_B94", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_brk_mesh, _brk_mats, (9643.788, 5745.5156, 2391.1062), (0.0002049056702727294, 0.00010013581169472522, 90.00026882293402), (1.0, 1.0, 1.0), "BP_Mines_Support_Beam_B95", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_brk_mesh, _brk_mats, (7852.3125, 5363.0146, 1111.8486), (0.0, 179.99992486791828, -0.0), (1.0, 1.0, 1.0), "BP_Mines_Support_Beam_B96_22", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_brk_mesh, _brk_mats, (10344.554, 5501.3643, 1071.8486), (0.0, -169.99981234956857, 0.0), (1.0, 1.0, 1.0), "BP_Mines_Support_Beam_B97", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_brk_mesh, _brk_mats, (4646.981, 4852.3154, 2161.8486), (0.0, -90.00005166594045, 0.0), (1.0, 1.0, 1.0), "BP_Mines_Support_Beam_B98", _folder)
if a: placed += 1
else: skipped += 1

# --- Extra DecoVolumes (not construction blocks) ---
_folder = "Reconstruction/BD_BB_Chapter5_BalrogsNest/DecoVolumes"

# DecoVolume: BP_DM_Deep_WoodenPlank_B_Breakable_2 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (6742.6016, 6584.167, 805.0), (0.0, 0.0, -0.0), (6.0186, 1.0016, 0.1689), "DV_BP_DM_Deep_WoodenPlank_B_Breakable_2_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_DM_Mine_tailings_Debris_1x1_A_2 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (5869.3203, 6564.1167, 811.1879), (0.0, 0.0, -0.0), (1.0107, 1.0107, 0.4337), "DV_BP_DM_Mine_tailings_Debris_1x1_A_2_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_DM_Mine_tailings_Debris_1x1_A2_5 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (5090.9526, 6519.426, 818.33685), (0.0, 0.0, -0.0), (1.0107, 1.0107, 0.4337), "DV_BP_DM_Mine_tailings_Debris_1x1_A2_5_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_DM_Mine_tailings_Debris_1x1_A3_8 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (9168.046, 8411.852, 816.9975), (0.0, 0.0, -0.0), (1.0107, 1.0107, 0.4337), "DV_BP_DM_Mine_tailings_Debris_1x1_A3_8_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_DM_Mine_tailings_Debris_1x1_A4_11 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (8455.113, 7922.3174, 818.0693), (0.0, 0.0, -0.0), (1.0107, 1.0107, 0.4337), "DV_BP_DM_Mine_tailings_Debris_1x1_A4_11_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_DM_Mine_tailings_Debris_1x1_A5 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (8898.157, 8665.851, 843.94867), (0.0, 0.0, -0.0), (1.0107, 1.0107, 0.4337), "DV_BP_DM_Mine_tailings_Debris_1x1_A5_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_DM_Mine_tailings_Debris_1x1_A6_15 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (9776.931, 5828.706, 811.99457), (0.0, 0.0, -0.0), (1.0107, 1.0107, 0.4337), "DV_BP_DM_Mine_tailings_Debris_1x1_A6_15_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_DM_Mine_tailings_Debris_1x1_B_2 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (2825.8657, 5069.449, 823.2815), (0.0, 0.0, -0.0), (1.3780, 1.4247, 0.4664), "DV_BP_DM_Mine_tailings_Debris_1x1_B_2_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_DM_Mine_tailings_Debris_1x1_B2_2 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (4774.3457, 6181.055, 809.254), (0.0, 0.0, -0.0), (1.1132, 1.1521, 0.3734), "DV_BP_DM_Mine_tailings_Debris_1x1_B2_2_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_DM_Mine_tailings_Debris_1x1_C_2 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (2775.5513, 5190.758, 809.6964), (0.0, 0.0, -0.0), (1.0309, 1.3650, 0.4613), "DV_BP_DM_Mine_tailings_Debris_1x1_C_2_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_DM_Mine_tailings_Debris_1x1_C2_5 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (2755.5835, 5668.1924, 819.23645), (0.0, 0.0, -0.0), (1.0309, 1.3650, 0.4613), "DV_BP_DM_Mine_tailings_Debris_1x1_C2_5_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_DM_Mine_tailings_Debris_1x1_D_5 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (2947.3164, 5118.663, 810.0444), (0.0, 0.0, -0.0), (1.0136, 1.0161, 0.4947), "DV_BP_DM_Mine_tailings_Debris_1x1_D_5_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_DM_Mine_tailings_Debris_1x1_E_5 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (2835.9763, 5198.4487, 803.8119), (0.0, 0.0, -0.0), (1.3144, 1.3068, 0.2145), "DV_BP_DM_Mine_tailings_Debris_1x1_E_5_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_DM_Mine_tailings_Debris_2x2_A_2 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (9613.614, 7475.2075, 824.9276), (0.0, 0.0, -0.0), (2.2529, 2.2541, 0.5085), "DV_BP_DM_Mine_tailings_Debris_2x2_A_2_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_DM_Mine_tailings_Debris_2x2_A2_5 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (8454.427, 5429.3076, 814.32135), (0.0, 0.0, -0.0), (2.0672, 2.0658, 0.5085), "DV_BP_DM_Mine_tailings_Debris_2x2_A2_5_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_DM_Mine_tailings_Debris_2x2_A3 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (8413.852, 5522.555, 807.9747), (0.0, 0.0, -0.0), (2.9036, 2.9038, 0.5085), "DV_BP_DM_Mine_tailings_Debris_2x2_A3_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_DM_Mine_tailings_Debris_2x2_A4_9 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (10219.647, 9428.732, 812.7274), (0.0, 0.0, -0.0), (2.0672, 2.0658, 0.5085), "DV_BP_DM_Mine_tailings_Debris_2x2_A4_9_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_DM_Mine_tailings_Debris_2x2_A5 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (10219.646, 9670.089, 812.7274), (0.0, 0.0, -0.0), (2.0672, 2.0658, 0.5085), "DV_BP_DM_Mine_tailings_Debris_2x2_A5_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_DM_Mine_tailings_Debris_2x2_B_2 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (5999.9004, 6657.235, 838.8144), (0.0, 0.0, -0.0), (2.1529, 2.1480, 0.9793), "DV_BP_DM_Mine_tailings_Debris_2x2_B_2_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_DM_Mine_tailings_Debris_2x2_B2_5 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (8330.965, 5340.0874, 837.61273), (0.0, 0.0, -0.0), (2.1529, 2.1480, 0.9793), "DV_BP_DM_Mine_tailings_Debris_2x2_B2_5_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_DM_Mine_tailings_Debris_2x2_B3_8 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (10047.684, 6054.488, 851.8505), (0.0, 0.0, -0.0), (2.1529, 2.1480, 0.9793), "DV_BP_DM_Mine_tailings_Debris_2x2_B3_8_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_DM_Mine_tailings_Debris_2x2_C_2 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (6106.9385, 6667.8643, 814.73376), (0.0, 0.0, -0.0), (2.0854, 2.1324, 0.7345), "DV_BP_DM_Mine_tailings_Debris_2x2_C_2_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_DM_Mine_tailings_Debris_2x2_C2_2 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (8572.954, 8527.639, 821.9662), (0.0, 0.0, -0.0), (2.0854, 2.1324, 0.7345), "DV_BP_DM_Mine_tailings_Debris_2x2_C2_2_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_DM_Mine_tailings_Debris_2x2_C3_5 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (9857.986, 5858.2153, 824.6996), (0.0, 0.0, -0.0), (2.0854, 2.1324, 0.7345), "DV_BP_DM_Mine_tailings_Debris_2x2_C3_5_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_DM_Mine_tailings_Debris_2x2_C4 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (10470.994, 5237.38, 1016.63367), (0.0, 0.0, -0.0), (2.0854, 2.1324, 0.7345), "DV_BP_DM_Mine_tailings_Debris_2x2_C4_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_DM_Mine_tailings_Debris_2x2_C5 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (9696.39, 7530.7656, 845.577), (0.0, 0.0, -0.0), (2.0854, 2.1324, 0.7345), "DV_BP_DM_Mine_tailings_Debris_2x2_C5_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_DM_Mine_tailings_Debris_3x3_A_2 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (8272.572, 7956.1997, 806.06036), (0.0, 0.0, -0.0), (4.1176, 4.1157, 1.0281), "DV_BP_DM_Mine_tailings_Debris_3x3_A_2_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_DM_Mine_tailings_Debris_3x3_A2 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (8622.965, 8783.739, 850.5086), (0.0, 0.0, -0.0), (4.1176, 4.1157, 1.0281), "DV_BP_DM_Mine_tailings_Debris_3x3_A2_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_DM_Mine_tailings_Debris_3x3_A3_6 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (8126.6753, 7931.4287, 832.20197), (0.0, 0.0, -0.0), (3.0055, 3.0000, 1.0281), "DV_BP_DM_Mine_tailings_Debris_3x3_A3_6_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_DM_Mines_Fence_A_2 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (9040.0, 6218.612, 2419.4927), (0.0, 0.0, -0.0), (5.9695, 4.7391, 0.3650), "DV_BP_DM_Mines_Fence_A_2_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_DM_Mines_Fence_A2_6 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (8760.0, 6751.388, 2419.4932), (0.0, 0.0, -0.0), (5.9695, 4.7391, 0.3650), "DV_BP_DM_Mines_Fence_A2_6_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_DM_Mines_Fence_A3_8 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (9360.0, 6738.612, 2419.4932), (0.0, 0.0, -0.0), (5.9695, 4.7391, 0.3650), "DV_BP_DM_Mines_Fence_A3_8_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_DM_Mines_Fence_A6 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (8765.0, 5781.388, 2419.4934), (0.0, 0.0, -0.0), (5.9695, 4.7391, 0.3650), "DV_BP_DM_Mines_Fence_A6_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_DM_Mines_Fence_A9 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (8310.0, 6164.3057, 2424.7466), (0.0, 0.0, -0.0), (2.9847, 2.3696, 0.1825), "DV_BP_DM_Mines_Fence_A9_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_DM_Mines_Fence_B_2 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (7997.532, 6164.221, 2424.7463), (0.0, 0.0, -0.0), (3.1031, 1.4535, 0.1825), "DV_BP_DM_Mines_Fence_B_2_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_DM_Mines_Fence_B2 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (8008.052, 6363.594, 2424.7463), (0.0, 0.0, -0.0), (3.1371, 2.2042, 0.1825), "DV_BP_DM_Mines_Fence_B2_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_DM_Mines_Fence_Roof12 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (8766.884, 6277.3525, 2399.2197), (0.0, 0.0, -0.0), (6.6273, 4.8199, 0.4776), "DV_BP_DM_Mines_Fence_Roof12_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_DM_Mines_Fence_Roof13 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (9092.649, 6656.884, 2429.2197), (0.0, 0.0, -0.0), (4.8198, 6.6273, 0.4776), "DV_BP_DM_Mines_Fence_Roof13_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_DM_Mines_Fence_Roof14 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (9967.35, 6613.116, 2429.2205), (0.0, 0.0, -0.0), (4.8199, 6.6273, 0.4776), "DV_BP_DM_Mines_Fence_Roof14_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_DM_Mines_Fence_Roof4 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (9042.649, 5706.884, 2429.2197), (0.0, 0.0, -0.0), (4.8198, 6.6273, 0.4776), "DV_BP_DM_Mines_Fence_Roof4_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_DM_Mines_Fence_Roof7_18 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (8102.6494, 7256.884, 2429.2197), (0.0, 0.0, -0.0), (4.8198, 6.6273, 0.4776), "DV_BP_DM_Mines_Fence_Roof7_18_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_DM_Mines_Fence_Roof8_19 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (8587.35, 7263.116, 2429.2205), (0.0, 0.0, -0.0), (4.8199, 6.6273, 0.4776), "DV_BP_DM_Mines_Fence_Roof8_19_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_DM_Mines_Fence_Roof9_20 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (9042.649, 7256.884, 2429.2197), (0.0, 0.0, -0.0), (4.8198, 6.6273, 0.4776), "DV_BP_DM_Mines_Fence_Roof9_20_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_DM_Mines_Lift_Prop_horizontal_broken_Breakable_2 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (7164.9756, 5970.6978, 842.8227), (0.0, 0.0, -0.0), (1.5859, 1.8361, 2.0727), "DV_BP_DM_Mines_Lift_Prop_horizontal_broken_Breakable_2_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_DM_Mines_Lift_Rails_broken_Breakable_2 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (7344.323, 5912.4185, 857.70026), (0.0, 0.0, -0.0), (1.4701, 1.2343, 1.8858), "DV_BP_DM_Mines_Lift_Rails_broken_Breakable_2_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_DM_Mines_Machine_Whim_Boar_PullBar_Broken_2 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (7335.0703, 5818.0513, 821.252), (0.0, 0.0, -0.0), (0.7489, 0.5388, 0.3760), "DV_BP_DM_Mines_Machine_Whim_Boar_PullBar_Broken_2_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_DM_Mines_Machine_Whim_Boar_PullBar_Broken2_5 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (4626.8516, 6097.0737, 818.1637), (0.0, 0.0, -0.0), (0.1466, 0.5837, 0.6731), "DV_BP_DM_Mines_Machine_Whim_Boar_PullBar_Broken2_5_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_DM_Mines_Machine_Whim_Heavy_Beam_Broken_2 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (7125.9907, 5771.229, 813.9574), (0.0, 0.0, -0.0), (1.3149, 1.3475, 0.5953), "DV_BP_DM_Mines_Machine_Whim_Heavy_Beam_Broken_2_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_DM_Mines_Machine_Whim_Heavy_Beam_Broken2_5 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (4610.0713, 6215.832, 803.7816), (0.0, 0.0, -0.0), (0.1998, 1.0116, 1.0602), "DV_BP_DM_Mines_Machine_Whim_Heavy_Beam_Broken2_5_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_DM_Mines_Machine_Whim_Heavy_Beam_Broken3_8 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (7213.5454, 5796.1675, 843.7816), (0.0, 0.0, -0.0), (0.9759, 0.6788, 1.0602), "DV_BP_DM_Mines_Machine_Whim_Heavy_Beam_Broken3_8_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_DM_Mines_Machine_Whim_Pole_Support_A_Broken_2 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (7296.0034, 5921.7046, 803.0084), (0.0, 0.0, -0.0), (0.7406, 0.7277, 0.1966), "DV_BP_DM_Mines_Machine_Whim_Pole_Support_A_Broken_2_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_DM_Mines_Machine_Whim_Rope_Bracket_Broken_2 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (7138.247, 5651.275, 803.2634), (0.0, 0.0, -0.0), (1.6629, 0.3107, 0.1650), "DV_BP_DM_Mines_Machine_Whim_Rope_Bracket_Broken_2_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_DM_Mines_Machine_Whim_Rope_Bracket_Broken2_5 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (4513.247, 6096.275, 813.2634), (0.0, 0.0, -0.0), (1.6629, 0.3107, 0.1650), "DV_BP_DM_Mines_Machine_Whim_Rope_Bracket_Broken2_5_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_DM_Mines_Machine_Whim_Rope_Support_Broken_B_2 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (7120.6914, 5878.39, 807.7689), (0.0, 0.0, -0.0), (1.9645, 1.4980, 1.3593), "DV_BP_DM_Mines_Machine_Whim_Rope_Support_Broken_B_2_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_DM_Mines_Machine_Whim_Rope_Support_Broken_B2_5 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (7231.729, 5935.876, 868.22235), (0.0, 0.0, -0.0), (1.6465, 1.7402, 1.8022), "DV_BP_DM_Mines_Machine_Whim_Rope_Support_Broken_B2_5_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_DM_Mines_Plank_3M_A_2 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (871.2626, 1612.93, 898.41595), (0.0, 0.0, -0.0), (2.5787, 2.0304, 0.0698), "DV_BP_DM_Mines_Plank_3M_A_2_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_DM_Mines_Plank_3M_B_2 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (772.6954, 1936.8451, 807.5487), (0.0, 0.0, -0.0), (0.3790, 1.2047, 0.3907), "DV_BP_DM_Mines_Plank_3M_B_2_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_DM_Mines_Scaffolding_Beam_2M_B_2 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (4179.7197, 5219.987, 1067.4768), (0.0, 0.0, -0.0), (0.2528, 0.2525, 1.7527), "DV_BP_DM_Mines_Scaffolding_Beam_2M_B_2_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_DM_Mines_Scaffolding_Beam_2M_B2 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (4179.7197, 4839.9863, 1067.4768), (0.0, 0.0, -0.0), (0.2528, 0.2525, 1.7527), "DV_BP_DM_Mines_Scaffolding_Beam_2M_B2_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_DM_Mines_Scaffolding_Beam_2M_B3_2 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (4191.945, 5333.089, 839.3015), (0.0, 0.0, -0.0), (1.5906, 1.2346, 0.3629), "DV_BP_DM_Mines_Scaffolding_Beam_2M_B3_2_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_DM_Mines_Scaffolding_Beam_2M_B4_2 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (5247.772, 6968.7627, 945.3164), (0.0, 0.0, -0.0), (1.7651, 0.2525, 0.3625), "DV_BP_DM_Mines_Scaffolding_Beam_2M_B4_2_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_DM_Mines_Scaffolding_Beam_3M_C_2 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (4769.7437, 5219.9595, 1017.8128), (0.0, 0.0, -0.0), (0.2535, 0.2533, 2.7593), "DV_BP_DM_Mines_Scaffolding_Beam_3M_C_2_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_DM_Mines_Scaffolding_Beam_3M_C2 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (4509.743, 5219.9595, 1017.8128), (0.0, 0.0, -0.0), (0.2535, 0.2533, 2.7593), "DV_BP_DM_Mines_Scaffolding_Beam_3M_C2_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_DM_Mines_Scaffolding_Beam_3M_C3_2 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (6464.1875, 5120.4604, 1036.2177), (0.0, 0.0, -0.0), (1.6234, 0.7470, 2.5027), "DV_BP_DM_Mines_Scaffolding_Beam_3M_C3_2_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_DM_Mines_Scaffolding_Beam_3M_C4 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (6438.3877, 5171.862, 1040.0668), (0.0, 0.0, -0.0), (1.2154, 1.4258, 2.5027), "DV_BP_DM_Mines_Scaffolding_Beam_3M_C4_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_DM_Mines_Scaffolding_Beam_3M_C5 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (4754.3945, 6281.527, 817.8128), (0.0, 0.0, -0.0), (0.2936, 0.2935, 2.7593), "DV_BP_DM_Mines_Scaffolding_Beam_3M_C5_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_DM_Mines_Scaffolding_Beam_3M_C6 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (4468.801, 6231.169, 817.8128), (0.0, 0.0, -0.0), (0.2936, 0.2935, 2.7593), "DV_BP_DM_Mines_Scaffolding_Beam_3M_C6_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_DM_Mines_Scaffolding_Beam_3M_C7_6 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (5254.6685, 6833.8584, 888.28906), (0.0, 0.0, -0.0), (0.2535, 2.1082, 2.1519), "DV_BP_DM_Mines_Scaffolding_Beam_3M_C7_6_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_DM_Mines_Scaffolding_Beam_3M_C8 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (4729.6016, 4431.6523, 1267.8127), (0.0, 0.0, -0.0), (0.2936, 0.2935, 2.7593), "DV_BP_DM_Mines_Scaffolding_Beam_3M_C8_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_DM_Mines_Scaffolding_Platform_3X1M_A5_2 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (3883.4043, 6103.398, 816.4011), (0.0, 0.0, -0.0), (3.2325, 2.2104, 0.7136), "DV_BP_DM_Mines_Scaffolding_Platform_3X1M_A5_2_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_DM_Mines_Scaffolding_Platform_3X1M_B_2 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (3064.9404, 5716.8604, 791.7662), (0.0, 0.0, -0.0), (2.4772, 2.1204, 0.4096), "DV_BP_DM_Mines_Scaffolding_Platform_3X1M_B_2_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_DM_Mines_Scaffolding_Platform_3X1M_C_2 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (7890.831, 4813.5386, 1087.343), (0.0, 0.0, -0.0), (3.1948, 2.2972, 0.7676), "DV_BP_DM_Mines_Scaffolding_Platform_3X1M_C_2_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_DM_Mines_Scaffolding_Platform_3X3M_B_2 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (6869.4507, 5035.7036, 959.0778), (0.0, 0.0, -0.0), (3.3653, 2.7141, 0.5801), "DV_BP_DM_Mines_Scaffolding_Platform_3X3M_B_2_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_DM_Mines_Scaffolding_Post_2M_B_2 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (5332.349, 6809.504, 829.3743), (0.0, 0.0, -0.0), (2.0594, 0.5869, 0.6390), "DV_BP_DM_Mines_Scaffolding_Post_2M_B_2_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_DM_Mines_Scaffolding_Post_2M_B2_5 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (6683.4644, 5187.696, 931.8769), (0.0, 0.0, -0.0), (2.1143, 0.2040, 0.2687), "DV_BP_DM_Mines_Scaffolding_Post_2M_B2_5_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_DM_Mines_Scaffolding_Post_3M_A_2 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (3076.599, 5734.152, 797.4821), (0.0, 0.0, -0.0), (2.1196, 2.3726, 0.4417), "DV_BP_DM_Mines_Scaffolding_Post_3M_A_2_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_DM_Mines_Scaffolding_Post_3M_A2_5 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (4251.6084, 6298.9277, 937.9636), (0.0, 0.0, -0.0), (1.1365, 1.0042, 2.7963), "DV_BP_DM_Mines_Scaffolding_Post_3M_A2_5_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_DM_Mines_Scaffolding_Post_3M_A3 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (4226.9824, 6286.65, 936.402), (0.0, 0.0, -0.0), (0.8247, 1.3564, 2.7600), "DV_BP_DM_Mines_Scaffolding_Post_3M_A3_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_DM_Mines_Scaffolding_Post_3M_A4_9 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (6749.4014, 5222.465, 924.9466), (0.0, 0.0, -0.0), (1.0040, 2.9280, 0.3777), "DV_BP_DM_Mines_Scaffolding_Post_3M_A4_9_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_DM_Mines_Scaffolding_Post_3M_A5 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (4948.9487, 6600.324, 968.6242), (0.0, 0.0, -0.0), (1.0463, 2.9281, 0.2899), "DV_BP_DM_Mines_Scaffolding_Post_3M_A5_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_DM_Mines_Scaffolding_Post_3M_A6 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (4642.918, 6160.571, 887.77295), (0.0, 0.0, -0.0), (0.8210, 2.3058, 2.0376), "DV_BP_DM_Mines_Scaffolding_Post_3M_A6_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_DM_Mines_Scaffolding_Support_1M_5 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (4127.329, 6285.0776, 847.20325), (0.0, 0.0, -0.0), (0.4383, 0.6416, 1.0451), "DV_BP_DM_Mines_Scaffolding_Support_1M_5_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_DM_Mines_Scaffolding_Support_1M2 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (4703.1797, 6084.0938, 802.38403), (0.0, 0.0, -0.0), (1.0090, 0.6354, 0.6601), "DV_BP_DM_Mines_Scaffolding_Support_1M2_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_DM_Mines_Scaffolding_Support_2M10_5 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (4734.086, 6372.042, 949.35504), (0.0, 0.0, -0.0), (0.6090, 2.0223, 0.2129), "DV_BP_DM_Mines_Scaffolding_Support_2M10_5_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_DM_Mines_Scaffolding_Support_2M11 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (4875.6465, 6564.0933, 988.7751), (0.0, 0.0, -0.0), (2.0257, 0.5376, 0.5001), "DV_BP_DM_Mines_Scaffolding_Support_2M11_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_DM_Mines_Scaffolding_Support_2M12 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (5147.6426, 6974.774, 950.5074), (0.0, 0.0, -0.0), (1.8983, 1.1148, 0.3528), "DV_BP_DM_Mines_Scaffolding_Support_2M12_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_DM_Mines_Scaffolding_Support_2M3 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (7849.016, 5270.017, 1069.3551), (0.0, 0.0, -0.0), (0.2645, 2.0068, 0.2129), "DV_BP_DM_Mines_Scaffolding_Support_2M3_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_DM_Mines_Scaffolding_Support_2M34_57 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (7850.4917, 6943.0234, 2484.1038), (0.0, 0.0, -0.0), (0.2645, 0.2129, 2.0068), "DV_BP_DM_Mines_Scaffolding_Support_2M34_57_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_DM_Mines_Scaffolding_Support_2M38_63 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (10200.487, 6033.023, 2484.1035), (0.0, 0.0, -0.0), (0.2645, 0.2129, 2.0068), "DV_BP_DM_Mines_Scaffolding_Support_2M38_63_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_DM_Mines_Scaffolding_Support_2M39 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (7850.4927, 5443.0205, 2484.111), (0.0, 0.0, -0.0), (0.2645, 0.2129, 2.0068), "DV_BP_DM_Mines_Scaffolding_Support_2M39_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_DM_Mines_Scaffolding_Support_2M4 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (8149.016, 5280.017, 1079.3551), (0.0, 0.0, -0.0), (0.2645, 2.0068, 0.2129), "DV_BP_DM_Mines_Scaffolding_Support_2M4_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_DM_Mines_Scaffolding_Support_2M42_69 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (10200.487, 6933.023, 2484.1057), (0.0, 0.0, -0.0), (0.2645, 0.2129, 2.0068), "DV_BP_DM_Mines_Scaffolding_Support_2M42_69_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_DM_Mines_Scaffolding_Support_2M43 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (7850.49, 7543.0195, 2484.1165), (0.0, 0.0, -0.0), (0.2645, 0.2129, 2.0068), "DV_BP_DM_Mines_Scaffolding_Support_2M43_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_DM_Mines_Scaffolding_Support_2M44 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (7850.492, 6933.0195, 2484.113), (0.0, 0.0, -0.0), (0.2645, 0.2129, 2.0068), "DV_BP_DM_Mines_Scaffolding_Support_2M44_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_DM_Mines_Scaffolding_Support_2M45 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (7865.817, 7544.633, 2484.111), (0.0, 0.0, -0.0), (0.2129, 0.2645, 2.0068), "DV_BP_DM_Mines_Scaffolding_Support_2M45_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_DM_Mines_Scaffolding_Support_2M46 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (8455.811, 7544.6333, 2484.1108), (0.0, 0.0, -0.0), (0.2129, 0.2645, 2.0068), "DV_BP_DM_Mines_Scaffolding_Support_2M46_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_DM_Mines_Scaffolding_Support_2M47 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (10215.811, 7544.6313, 2484.1165), (0.0, 0.0, -0.0), (0.2129, 0.2645, 2.0068), "DV_BP_DM_Mines_Scaffolding_Support_2M47_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_DM_Mines_Scaffolding_Support_2M48 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (9355.811, 7544.6323, 2484.113), (0.0, 0.0, -0.0), (0.2129, 0.2645, 2.0068), "DV_BP_DM_Mines_Scaffolding_Support_2M48_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_DM_Mines_Scaffolding_Support_2M49 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (7865.816, 5434.633, 2484.111), (0.0, 0.0, -0.0), (0.2129, 0.2645, 2.0068), "DV_BP_DM_Mines_Scaffolding_Support_2M49_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_DM_Mines_Scaffolding_Support_2M50 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (8455.81, 5434.6333, 2484.1108), (0.0, 0.0, -0.0), (0.2129, 0.2645, 2.0068), "DV_BP_DM_Mines_Scaffolding_Support_2M50_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_DM_Mines_Scaffolding_Support_2M52 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (9355.811, 5434.6323, 2484.113), (0.0, 0.0, -0.0), (0.2129, 0.2645, 2.0068), "DV_BP_DM_Mines_Scaffolding_Support_2M52_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_DM_Mines_Scaffolding_Support_2M7_2 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (4259.252, 6038.27, 806.19543), (0.0, 0.0, -0.0), (2.0163, 0.5654, 0.4199), "DV_BP_DM_Mines_Scaffolding_Support_2M7_2_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_DM_Mines_Scaffolding_Support_2M9 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (4470.205, 5565.6855, 814.77356), (0.0, 0.0, -0.0), (2.0259, 0.5900, 0.6070), "DV_BP_DM_Mines_Scaffolding_Support_2M9_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_DM_Mines_Scaffolding_Support_3M_2 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (4608.4614, 6258.284, 949.2703), (0.0, 0.0, -0.0), (3.0089, 0.7926, 0.2164), "DV_BP_DM_Mines_Scaffolding_Support_3M_2_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_DM_Mines_Scaffolding_Support_3M2 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (4446.963, 6372.799, 949.2703), (0.0, 0.0, -0.0), (0.7926, 3.0089, 0.2164), "DV_BP_DM_Mines_Scaffolding_Support_3M2_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_DM_Mines_Scaffolding_Support_3M3 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (4722.5024, 4490.202, 1409.2703), (0.0, 0.0, -0.0), (0.7926, 3.0089, 0.2164), "DV_BP_DM_Mines_Scaffolding_Support_3M3_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_DM_Mines_Scaffolding_Support_Brace10 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (7851.4736, 5502.799, 2804.123), (0.0, 0.0, -0.0), (0.6754, 3.9674, 1.4754), "DV_BP_DM_Mines_Scaffolding_Support_Brace10_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_DM_Mines_Scaffolding_Support_Brace11 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (7851.4736, 5902.799, 2804.123), (0.0, 0.0, -0.0), (0.6754, 3.9674, 1.4754), "DV_BP_DM_Mines_Scaffolding_Support_Brace11_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_DM_Mines_Scaffolding_Support_Brace12 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (7851.4727, 6302.7983, 2804.123), (0.0, 0.0, -0.0), (0.6754, 3.9674, 1.4754), "DV_BP_DM_Mines_Scaffolding_Support_Brace12_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_DM_Mines_Scaffolding_Support_Brace13 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (7851.4736, 6702.7983, 2804.123), (0.0, 0.0, -0.0), (0.6754, 3.9674, 1.4754), "DV_BP_DM_Mines_Scaffolding_Support_Brace13_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_DM_Mines_Scaffolding_Support_Brace14 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (7851.4736, 7102.7983, 2804.123), (0.0, 0.0, -0.0), (0.6754, 3.9674, 1.4754), "DV_BP_DM_Mines_Scaffolding_Support_Brace14_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_DM_Mines_Scaffolding_Support_Brace15 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (7851.4736, 7502.7993, 2804.123), (0.0, 0.0, -0.0), (0.6754, 3.9674, 1.4754), "DV_BP_DM_Mines_Scaffolding_Support_Brace15_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_DM_Mines_Scaffolding_Support_Brace16 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (7950.6045, 5433.67, 2804.123), (0.0, 0.0, -0.0), (3.9674, 0.6754, 1.4754), "DV_BP_DM_Mines_Scaffolding_Support_Brace16_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_DM_Mines_Scaffolding_Support_Brace17 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (8350.598, 5433.6694, 2804.123), (0.0, 0.0, -0.0), (3.9674, 0.6754, 1.4754), "DV_BP_DM_Mines_Scaffolding_Support_Brace17_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_DM_Mines_Scaffolding_Support_Brace18 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (8750.599, 5433.67, 2804.123), (0.0, 0.0, -0.0), (3.9674, 0.6754, 1.4754), "DV_BP_DM_Mines_Scaffolding_Support_Brace18_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_DM_Mines_Scaffolding_Support_Brace19 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (9150.6, 5433.6694, 2804.123), (0.0, 0.0, -0.0), (3.9674, 0.6754, 1.4754), "DV_BP_DM_Mines_Scaffolding_Support_Brace19_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_DM_Mines_Scaffolding_Support_Brace20 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (9550.598, 5433.6685, 2804.123), (0.0, 0.0, -0.0), (3.9674, 0.6754, 1.4754), "DV_BP_DM_Mines_Scaffolding_Support_Brace20_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_DM_Mines_Scaffolding_Support_Brace22 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (7950.6035, 7543.67, 2804.123), (0.0, 0.0, -0.0), (3.9674, 0.6754, 1.4754), "DV_BP_DM_Mines_Scaffolding_Support_Brace22_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_DM_Mines_Scaffolding_Support_Brace23 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (8350.601, 7543.669, 2804.123), (0.0, 0.0, -0.0), (3.9674, 0.6754, 1.4754), "DV_BP_DM_Mines_Scaffolding_Support_Brace23_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_DM_Mines_Scaffolding_Support_Brace24 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (8750.599, 7543.669, 2804.123), (0.0, 0.0, -0.0), (3.9674, 0.6754, 1.4754), "DV_BP_DM_Mines_Scaffolding_Support_Brace24_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_DM_Mines_Scaffolding_Support_Brace25 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (9150.6, 7543.6694, 2804.123), (0.0, 0.0, -0.0), (3.9674, 0.6754, 1.4754), "DV_BP_DM_Mines_Scaffolding_Support_Brace25_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_DM_Mines_Scaffolding_Support_Brace26 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (9550.599, 7543.668, 2804.123), (0.0, 0.0, -0.0), (3.9674, 0.6754, 1.4754), "DV_BP_DM_Mines_Scaffolding_Support_Brace26_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_DM_Mines_Scaffolding_Support_Brace27 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (9950.599, 7543.668, 2804.123), (0.0, 0.0, -0.0), (3.9674, 0.6754, 1.4754), "DV_BP_DM_Mines_Scaffolding_Support_Brace27_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_DM_Mines_Scaffolding_Support_Brace9 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (9951.468, 7502.8, 2804.123), (0.0, 0.0, -0.0), (0.6754, 3.9674, 1.4754), "DV_BP_DM_Mines_Scaffolding_Support_Brace9_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_DM_Mines_Wagon_B_Breakable_2 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (5639.049, 6724.008, 874.7478), (0.0, 0.0, -0.0), (5.4784, 3.1008, 1.4542), "DV_BP_DM_Mines_Wagon_B_Breakable_2_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_DM_Mines_Wagon_Broken_A_2 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (4333.135, 5545.841, 870.0442), (0.0, 0.0, -0.0), (4.8649, 4.8888, 1.4394), "DV_BP_DM_Mines_Wagon_Broken_A_2_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_DM_Mines_Wagon_Broken_B_2 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (8885.372, 8462.59, 828.3023), (0.0, 0.0, -0.0), (4.7830, 3.2135, 0.9310), "DV_BP_DM_Mines_Wagon_Broken_B_2_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_DM_Mines_Wagon_Broken_B2 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (5737.3, 4927.2295, 1116.5138), (0.0, 0.0, -0.0), (5.1312, 5.0048, 1.0595), "DV_BP_DM_Mines_Wagon_Broken_B2_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_DM_Rubble_Masonry_Pile_A_Breakable_5 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (4613.0796, 6266.3423, 874.4277), (0.0, 0.0, -0.0), (1.5969, 1.6484, 1.4244), "DV_BP_DM_Rubble_Masonry_Pile_A_Breakable_5_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_DM_Rubble_Masonry_Pile_C_Breakable_2 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (5756.332, 5569.4478, 843.89075), (0.0, 0.0, -0.0), (2.1676, 2.2318, 0.9351), "DV_BP_DM_Rubble_Masonry_Pile_C_Breakable_2_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_DM_Rubble_Masonry_Pile_E_Breakable_2 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (5708.4604, 5719.1323, 818.3407), (0.0, 0.0, -0.0), (3.0953, 3.2224, 1.3025), "DV_BP_DM_Rubble_Masonry_Pile_E_Breakable_2_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_DM_Rubble_Masonry_Pile_E_Breakable2_5 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (4240.5083, 5481.722, 818.3407), (0.0, 0.0, -0.0), (3.3424, 3.2776, 1.3025), "DV_BP_DM_Rubble_Masonry_Pile_E_Breakable2_5_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_DM_Rubble_Masonry_Pile_E_Breakable3_8 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (4604.786, 6146.157, 818.3407), (0.0, 0.0, -0.0), (2.6471, 2.8602, 1.3025), "DV_BP_DM_Rubble_Masonry_Pile_E_Breakable3_8_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_DM_Rubble_Masonry_Pile_F_Breakable_2 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (7290.571, 5703.853, 842.851), (0.0, 0.0, -0.0), (4.4301, 4.0437, 1.3764), "DV_BP_DM_Rubble_Masonry_Pile_F_Breakable_2_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_DM_Rubble_Masonry_Pile_F_Breakable2_8 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (5820.571, 5453.853, 837.851), (0.0, 0.0, -0.0), (4.4301, 4.0437, 1.3764), "DV_BP_DM_Rubble_Masonry_Pile_F_Breakable2_8_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_DM_Rubble_Masonry_Pile_H_Breakable_5 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (7207.734, 5857.257, 841.5479), (0.0, 0.0, -0.0), (3.3009, 3.6663, 1.3071), "DV_BP_DM_Rubble_Masonry_Pile_H_Breakable_5_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_DM_Rubble_Masonry_Pile_I_Breakable_2 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (5716.1016, 5435.792, 846.5136), (0.0, 0.0, -0.0), (3.3345, 4.3509, 1.1909), "DV_BP_DM_Rubble_Masonry_Pile_I_Breakable_2_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_DM_Sluice_Angled_B_Breakable_2 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (6066.461, 6580.7207, 877.3058), (0.0, 0.0, -0.0), (3.8280, 3.5700, 1.7609), "DV_BP_DM_Sluice_Angled_B_Breakable_2_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_DM_Warehouse_Cage_Breakable_2 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (5541.49, 5581.8345, 841.1302), (0.0, 0.0, -0.0), (2.3078, 2.9143, 1.3026), "DV_BP_DM_Warehouse_Cage_Breakable_2_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_DM_Warehouse_Crate_A_Broken_Breakable_2 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (4021.0312, 5980.259, 825.2152), (0.0, 0.0, -0.0), (1.0603, 1.0603, 0.5570), "DV_BP_DM_Warehouse_Crate_A_Broken_Breakable_2_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_DM_Warehouse_Crate_A_Broken_Breakable2_2 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (5450.0, 5740.0, 823.1498), (0.0, 0.0, -0.0), (0.7500, 0.7500, 0.5570), "DV_BP_DM_Warehouse_Crate_A_Broken_Breakable2_2_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_DM_Warehouse_Crate_B_Breakable_11 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (8867.92, 8761.814, 874.14374), (0.0, 0.0, -0.0), (1.4475, 1.5064, 1.0181), "DV_BP_DM_Warehouse_Crate_B_Breakable_11_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_DM_Warehouse_Crate_B_Broken_Breakable_2 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (8493.6, 8748.034, 857.4918), (0.0, 0.0, -0.0), (0.8876, 1.1638, 0.7627), "DV_BP_DM_Warehouse_Crate_B_Broken_Breakable_2_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_DM_Warehouse_Crate_B_Broken_Breakable2_2 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (4507.7305, 5656.282, 833.5375), (0.0, 0.0, -0.0), (1.1716, 1.3718, 0.5490), "DV_BP_DM_Warehouse_Crate_B_Broken_Breakable2_2_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_DM_Warehouse_Crate_B_Broken_Breakable3_8 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (4517.912, 6196.6426, 836.5739), (0.0, 0.0, -0.0), (1.2669, 1.0168, 0.7904), "DV_BP_DM_Warehouse_Crate_B_Broken_Breakable3_8_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_DM_Warren_Lighting_Torch_Breakable_2 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (2297.2087, 5046.3413, 867.78284), (0.0, 0.0, -0.0), (1.0112, 1.0765, 1.9128), "DV_BP_DM_Warren_Lighting_Torch_Breakable_2_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_DM_Workshop_Barrel_Breakable_2 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (5060.9585, 6617.722, 818.19586), (0.0, 0.0, -0.0), (1.0736, 1.0927, 0.8610), "DV_BP_DM_Workshop_Barrel_Breakable_2_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_DM_Workshop_Barrel_Breakable2_5 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (5036.9995, 6718.137, 849.6437), (0.0, 0.0, -0.0), (0.7330, 0.8004, 0.8538), "DV_BP_DM_Workshop_Barrel_Breakable2_5_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_DM_Workshop_Barrel_Breakable3_2 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (2821.9666, 5771.9, 833.5859), (0.0, 0.0, -0.0), (0.9477, 1.1504, 1.0462), "DV_BP_DM_Workshop_Barrel_Breakable3_2_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_DM_Workshop_Barrel_Breakable4 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (4778.294, 5422.965, 836.6505), (0.0, 0.0, -0.0), (0.9962, 0.9910, 0.8273), "DV_BP_DM_Workshop_Barrel_Breakable4_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_DM_Workshop_Barrel_Broken_Breakable_2 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (5845.0, 6170.4517, 842.65753), (0.0, 0.0, -0.0), (0.8004, 0.7330, 0.8528), "DV_BP_DM_Workshop_Barrel_Broken_Breakable_2_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_DM_Workshop_Barrel_Broken_Breakable2_2 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (2875.8872, 5693.9316, 814.7011), (0.0, 0.0, -0.0), (1.1622, 1.2065, 0.8226), "DV_BP_DM_Workshop_Barrel_Broken_Breakable2_2_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_DM_Workshop_Barrel_Broken_Breakable3_5 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (7099.948, 5818.495, 810.7325), (0.0, 0.0, -0.0), (1.2911, 1.1581, 1.1672), "DV_BP_DM_Workshop_Barrel_Broken_Breakable3_5_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_DM_Workshop_Barrel_Broken_Breakable4 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (6089.008, 6238.3066, 842.65753), (0.0, 0.0, -0.0), (0.9367, 0.9813, 0.8528), "DV_BP_DM_Workshop_Barrel_Broken_Breakable4_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_DM_Workshop_Scatter_Bucket_Metal_Breakable10_14 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (8486.218, 5185.7515, 806.71674), (0.0, 0.0, -0.0), (0.9950, 0.9971, 0.6759), "DV_BP_DM_Workshop_Scatter_Bucket_Metal_Breakable10_14_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_DM_Workshop_Scatter_Bucket_Metal_Breakable2_2 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (2000.6758, 5825.3086, 843.2694), (0.0, 0.0, -0.0), (0.6754, 0.6754, 0.7337), "DV_BP_DM_Workshop_Scatter_Bucket_Metal_Breakable2_2_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_DM_Workshop_Scatter_Bucket_Metal_Breakable3 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (2235.377, 5749.9717, 818.3581), (0.0, 0.0, -0.0), (1.0230, 1.0811, 0.8450), "DV_BP_DM_Workshop_Scatter_Bucket_Metal_Breakable3_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_DM_Workshop_Scatter_Bucket_Metal_Breakable4_8 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (2864.872, 5164.7603, 797.1231), (0.0, 0.0, -0.0), (0.9640, 1.1910, 1.1264), "DV_BP_DM_Workshop_Scatter_Bucket_Metal_Breakable4_8_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_DM_Workshop_Scatter_Bucket_Metal_Breakable5_11 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (6693.5225, 5247.597, 921.5826), (0.0, 0.0, -0.0), (0.9829, 1.1552, 0.9903), "DV_BP_DM_Workshop_Scatter_Bucket_Metal_Breakable5_11_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_DM_Workshop_Scatter_Bucket_Metal_Breakable6_2 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (8790.225, 8753.023, 848.1649), (0.0, 0.0, -0.0), (0.9948, 0.6754, 0.9856), "DV_BP_DM_Workshop_Scatter_Bucket_Metal_Breakable6_2_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_DM_Workshop_Scatter_Bucket_Metal_Breakable7_5 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (8674.356, 8569.665, 807.854), (0.0, 0.0, -0.0), (0.6754, 0.9939, 0.9839), "DV_BP_DM_Workshop_Scatter_Bucket_Metal_Breakable7_5_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_DM_Workshop_Scatter_Bucket_Metal_Breakable8_8 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (8444.476, 5167.4995, 827.5475), (0.0, 0.0, -0.0), (0.8053, 0.7668, 0.9216), "DV_BP_DM_Workshop_Scatter_Bucket_Metal_Breakable8_8_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_DM_Workshop_Scatter_Bucket_Metal_Breakable9_11 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (8467.538, 5248.751, 823.9292), (0.0, 0.0, -0.0), (1.0063, 0.9457, 0.8939), "DV_BP_DM_Workshop_Scatter_Bucket_Metal_Breakable9_11_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_DM_Workshop_Scatter_Bucket_Wood_Breakable_5 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (6482.048, 5166.5215, 960.85876), (0.0, 0.0, -0.0), (0.8217, 0.6363, 0.6244), "DV_BP_DM_Workshop_Scatter_Bucket_Wood_Breakable_5_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_DM_Workshop_Scatter_Bucket_Wood_Breakable2 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (6422.073, 5250.271, 945.785), (0.0, 0.0, -0.0), (0.8196, 0.5947, 0.6755), "DV_BP_DM_Workshop_Scatter_Bucket_Wood_Breakable2_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_DM_Workshop_Scatter_Bucket_Wood_Breakable3_2 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (8935.918, 8617.941, 822.3979), (0.0, 0.0, -0.0), (0.5543, 0.8271, 0.8197), "DV_BP_DM_Workshop_Scatter_Bucket_Wood_Breakable3_2_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_DM_Workshop_Scatter_Sandbags_B_Breakable_2 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (6050.0, 6440.839, 840.2028), (0.0, 0.0, -0.0), (0.9191, 0.9960, 0.4049), "DV_BP_DM_Workshop_Scatter_Sandbags_B_Breakable_2_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_DM_Workshop_Scatter_Sandbags_B_Breakable2_5 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (7095.0, 5905.839, 810.2028), (0.0, 0.0, -0.0), (0.9191, 0.9960, 0.4049), "DV_BP_DM_Workshop_Scatter_Sandbags_B_Breakable2_5_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_Mines_Ceiling_Brace_A_Bracket36_69 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (10201.4375, 6740.137, 2493.3694), (0.0, 0.0, -0.0), (0.6275, 2.2423, 2.1812), "DV_BP_Mines_Ceiling_Brace_A_Bracket36_69_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_Mines_Ceiling_Brace_A_Bracket39_74 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (10201.466, 7137.1987, 2493.3694), (0.0, 0.0, -0.0), (0.6275, 2.2423, 2.1812), "DV_BP_Mines_Ceiling_Brace_A_Bracket39_74_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_Mines_Ceiling_Brace_A_Bracket41 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (7851.498, 6517.1953, 2493.3767), (0.0, 0.0, -0.0), (0.6275, 2.2423, 2.1812), "DV_BP_Mines_Ceiling_Brace_A_Bracket41_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_Mines_Ceiling_Brace_A_Bracket43 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (7851.4717, 7137.1953, 2493.3767), (0.0, 0.0, -0.0), (0.6275, 2.2423, 2.1812), "DV_BP_Mines_Ceiling_Brace_A_Bracket43_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_Mines_Ceiling_Brace_A_Bracket44 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (7851.424, 7360.1333, 2493.3767), (0.0, 0.0, -0.0), (0.6275, 2.2423, 2.1812), "DV_BP_Mines_Ceiling_Brace_A_Bracket44_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_Mines_Ceiling_Brace_A_Bracket45 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (7851.517, 5607.195, 2493.3767), (0.0, 0.0, -0.0), (0.6275, 2.2423, 2.1812), "DV_BP_Mines_Ceiling_Brace_A_Bracket45_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_Mines_Ceiling_Brace_A_Bracket46 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (7851.4697, 5830.135, 2493.3767), (0.0, 0.0, -0.0), (0.6275, 2.2423, 2.1812), "DV_BP_Mines_Ceiling_Brace_A_Bracket46_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_Mines_Ceiling_Brace_A_Bracket47 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (8639.984, 7543.628, 2493.3767), (0.0, 0.0, -0.0), (2.2423, 0.6275, 2.1812), "DV_BP_Mines_Ceiling_Brace_A_Bracket47_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_Mines_Ceiling_Brace_A_Bracket48 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (9162.924, 7543.681, 2493.3767), (0.0, 0.0, -0.0), (2.2423, 0.6275, 2.1812), "DV_BP_Mines_Ceiling_Brace_A_Bracket48_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_Mines_Ceiling_Brace_A_Bracket49 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (9559.983, 7543.652, 2493.3767), (0.0, 0.0, -0.0), (2.2423, 0.6275, 2.1812), "DV_BP_Mines_Ceiling_Brace_A_Bracket49_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_Mines_Ceiling_Brace_A_Bracket51 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (8029.988, 7543.6074, 2493.3767), (0.0, 0.0, -0.0), (2.2423, 0.6275, 2.1812), "DV_BP_Mines_Ceiling_Brace_A_Bracket51_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_Mines_Ceiling_Brace_A_Bracket53 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (8639.984, 5433.627, 2493.3767), (0.0, 0.0, -0.0), (2.2423, 0.6275, 2.1812), "DV_BP_Mines_Ceiling_Brace_A_Bracket53_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_Mines_Ceiling_Brace_A_Bracket54 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (9162.923, 5433.681, 2493.3767), (0.0, 0.0, -0.0), (2.2423, 0.6275, 2.1812), "DV_BP_Mines_Ceiling_Brace_A_Bracket54_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_Mines_Ceiling_Brace_A_Bracket55 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (9559.983, 5433.652, 2493.3767), (0.0, 0.0, -0.0), (2.2423, 0.6275, 2.1812), "DV_BP_Mines_Ceiling_Brace_A_Bracket55_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_Mines_Ceiling_Brace_A_Bracket57 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (8029.989, 5433.609, 2493.3767), (0.0, 0.0, -0.0), (2.2423, 0.6275, 2.1812), "DV_BP_Mines_Ceiling_Brace_A_Bracket57_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_Mines_Ceiling_Brace_A_Bracket58 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (8252.925, 5433.655, 2493.3767), (0.0, 0.0, -0.0), (2.2423, 0.6275, 2.1812), "DV_BP_Mines_Ceiling_Brace_A_Bracket58_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_Mines_Machine_Whim_Main_Beam_2 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (8578.63, 8384.862, 820.1937), (0.0, 0.0, -0.0), (5.1379, 1.7237, 0.7759), "DV_BP_Mines_Machine_Whim_Main_Beam_2_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_Mines_Scaffolding_Support_Structure_8 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (6229.273, 5214.4463, 1214.2859), (0.0, 0.0, -0.0), (3.4593, 4.4974, 6.2307), "DV_BP_Mines_Scaffolding_Support_Structure_8_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_Mines_Scaffolding_Support_Structure_B13 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (8584.879, 5489.6143, 2360.607), (0.0, 0.0, -0.0), (3.4170, 3.1867, 3.8738), "DV_BP_Mines_Scaffolding_Support_Structure_B13_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_Mines_Scaffolding_Support_Structure_B14 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (8884.879, 5489.61, 2360.607), (0.0, 0.0, -0.0), (3.4170, 3.1867, 3.8738), "DV_BP_Mines_Scaffolding_Support_Structure_B14_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_Mines_Scaffolding_Support_Structure_B18 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (6744.879, 5489.6143, 2360.607), (0.0, 0.0, -0.0), (3.4170, 3.1867, 3.8738), "DV_BP_Mines_Scaffolding_Support_Structure_B18_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_Mines_Scaffolding_Support_Structure_B19 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (7054.879, 5489.6143, 2360.607), (0.0, 0.0, -0.0), (3.4170, 3.1867, 3.8738), "DV_BP_Mines_Scaffolding_Support_Structure_B19_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_Mines_Scaffolding_Support_Structure_B20 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (7364.879, 5489.6143, 2360.607), (0.0, 0.0, -0.0), (3.4170, 3.1867, 3.8738), "DV_BP_Mines_Scaffolding_Support_Structure_B20_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_Mines_Scaffolding_Support_Structure_B21 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (7674.879, 5489.6143, 2360.607), (0.0, 0.0, -0.0), (3.4170, 3.1867, 3.8738), "DV_BP_Mines_Scaffolding_Support_Structure_B21_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_Mines_Scaffolding_Support_Structure_B22 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (5494.879, 5489.6143, 2360.607), (0.0, 0.0, -0.0), (3.4170, 3.1867, 3.8738), "DV_BP_Mines_Scaffolding_Support_Structure_B22_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_Mines_Scaffolding_Support_Structure_B23 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (5804.879, 5489.6143, 2360.607), (0.0, 0.0, -0.0), (3.4170, 3.1867, 3.8738), "DV_BP_Mines_Scaffolding_Support_Structure_B23_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_Mines_Scaffolding_Support_Structure_B24 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (6114.879, 5489.6143, 2360.607), (0.0, 0.0, -0.0), (3.4170, 3.1867, 3.8738), "DV_BP_Mines_Scaffolding_Support_Structure_B24_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_Mines_Scaffolding_Support_Structure_B25 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (6424.879, 5489.6143, 2360.607), (0.0, 0.0, -0.0), (3.4170, 3.1867, 3.8738), "DV_BP_Mines_Scaffolding_Support_Structure_B25_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_Mines_Scaffolding_Support_Structure_B26 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (4244.879, 5489.6143, 2360.607), (0.0, 0.0, -0.0), (3.4170, 3.1867, 3.8738), "DV_BP_Mines_Scaffolding_Support_Structure_B26_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_Mines_Scaffolding_Support_Structure_B27 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (4554.879, 5489.6143, 2360.607), (0.0, 0.0, -0.0), (3.4170, 3.1867, 3.8738), "DV_BP_Mines_Scaffolding_Support_Structure_B27_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_Mines_Scaffolding_Support_Structure_B28 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (4864.879, 5489.6143, 2360.607), (0.0, 0.0, -0.0), (3.4170, 3.1867, 3.8738), "DV_BP_Mines_Scaffolding_Support_Structure_B28_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_Mines_Scaffolding_Support_Structure_B29 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (5174.879, 5489.6143, 2360.607), (0.0, 0.0, -0.0), (3.4170, 3.1867, 3.8738), "DV_BP_Mines_Scaffolding_Support_Structure_B29_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_Mines_Scaffolding_Support_Structure_B4 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (8905.0625, 7509.9043, 2360.607), (0.0, 0.0, -0.0), (3.4170, 3.1867, 3.8738), "DV_BP_Mines_Scaffolding_Support_Structure_B4_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_Mines_Scaffolding_Support_Structure_B5_9 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (8605.0625, 7509.907, 2360.6064), (0.0, 0.0, -0.0), (3.4170, 3.1867, 3.8738), "DV_BP_Mines_Scaffolding_Support_Structure_B5_9_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_Mines_Scaffolding_Support_Structure_B6_11 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (8305.0625, 7509.91, 2360.6064), (0.0, 0.0, -0.0), (3.4170, 3.1867, 3.8738), "DV_BP_Mines_Scaffolding_Support_Structure_B6_11_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_Mines_Scaffolding_Support_Structure_B7 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (9205.0625, 7509.9004, 2360.6064), (0.0, 0.0, -0.0), (3.4170, 3.1867, 3.8738), "DV_BP_Mines_Scaffolding_Support_Structure_B7_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_Mines_Support_Beam10 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (10638.242, 5550.0864, 883.68384), (0.0, 0.0, -0.0), (0.7824, 0.7824, 3.8737), "DV_BP_Mines_Support_Beam10_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_Mines_Support_Beam22 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (7851.4663, 5547.3506, 2394.1226), (0.0, 0.0, -0.0), (0.6755, 3.8737, 0.6753), "DV_BP_Mines_Support_Beam22_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_Mines_Support_Beam24 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (8151.4604, 5547.3496, 2384.121), (0.0, 0.0, -0.0), (0.6755, 3.8737, 0.6753), "DV_BP_Mines_Support_Beam24_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_Mines_Support_Beam30 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (8456.107, 5547.3516, 2388.0903), (0.0, 0.0, -0.0), (0.6754, 3.8737, 0.6753), "DV_BP_Mines_Support_Beam30_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_Mines_Support_Beam32 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (8746.107, 5547.3516, 2388.0906), (0.0, 0.0, -0.0), (0.6754, 3.8737, 0.6753), "DV_BP_Mines_Support_Beam32_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_Mines_Support_Beam34 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (9046.107, 5547.3516, 2388.0903), (0.0, 0.0, -0.0), (0.6754, 3.8737, 0.6753), "DV_BP_Mines_Support_Beam34_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_Mines_Support_Beam36 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (9346.107, 5547.3516, 2388.0906), (0.0, 0.0, -0.0), (0.6754, 3.8737, 0.6753), "DV_BP_Mines_Support_Beam36_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_Mines_Support_Beam38 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (9646.107, 5547.3516, 2388.0906), (0.0, 0.0, -0.0), (0.6754, 3.8737, 0.6753), "DV_BP_Mines_Support_Beam38_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_Mines_Support_Beam44 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (10201.462, 6623.667, 2560.4373), (0.0, 0.0, -0.0), (0.6755, 0.6754, 3.8737), "DV_BP_Mines_Support_Beam44_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_Mines_Support_Beam47 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (10201.451, 7429.9834, 2574.123), (0.0, 0.0, -0.0), (0.6755, 3.8737, 0.6753), "DV_BP_Mines_Support_Beam47_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_Mines_Support_Beam48_82 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (10201.446, 7243.667, 2560.4373), (0.0, 0.0, -0.0), (0.6755, 0.6754, 3.8737), "DV_BP_Mines_Support_Beam48_82_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_Mines_Support_Beam49 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (7851.481, 7129.985, 2574.123), (0.0, 0.0, -0.0), (0.6755, 3.8737, 0.6753), "DV_BP_Mines_Support_Beam49_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_Mines_Support_Beam50_84 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (10201.462, 6323.667, 2560.4387), (0.0, 0.0, -0.0), (0.6755, 0.6754, 3.8737), "DV_BP_Mines_Support_Beam50_84_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_Mines_Support_Beam51 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (7851.4653, 5547.3477, 2574.1304), (0.0, 0.0, -0.0), (0.6755, 3.8737, 0.6753), "DV_BP_Mines_Support_Beam51_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_Mines_Support_Beam52 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (7851.467, 6623.663, 2560.4446), (0.0, 0.0, -0.0), (0.6755, 0.6754, 3.8737), "DV_BP_Mines_Support_Beam52_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_Mines_Support_Beam53 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (7851.4663, 5723.663, 2560.446), (0.0, 0.0, -0.0), (0.6755, 0.6754, 3.8737), "DV_BP_Mines_Support_Beam53_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_Mines_Support_Beam54 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (7851.4565, 7429.981, 2574.1304), (0.0, 0.0, -0.0), (0.6755, 3.8737, 0.6753), "DV_BP_Mines_Support_Beam54_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_Mines_Support_Beam55 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (7851.4507, 7243.6636, 2560.4446), (0.0, 0.0, -0.0), (0.6755, 0.6754, 3.8737), "DV_BP_Mines_Support_Beam55_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_Mines_Support_Beam56 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (7851.467, 6323.6636, 2560.446), (0.0, 0.0, -0.0), (0.6755, 0.6754, 3.8737), "DV_BP_Mines_Support_Beam56_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_Mines_Support_Beam57 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (7851.4854, 7429.984, 2394.1223), (0.0, 0.0, -0.0), (0.6755, 3.8737, 0.6753), "DV_BP_Mines_Support_Beam57_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_Mines_Support_Beam58 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (8151.4834, 7429.9824, 2384.1208), (0.0, 0.0, -0.0), (0.6755, 3.8737, 0.6753), "DV_BP_Mines_Support_Beam58_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_Mines_Support_Beam59 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (8456.107, 7429.9844, 2388.0903), (0.0, 0.0, -0.0), (0.6755, 3.8737, 0.6753), "DV_BP_Mines_Support_Beam59_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_Mines_Support_Beam6_5 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (10341.063, 5507.84, 883.68384), (0.0, 0.0, -0.0), (0.7824, 0.7824, 3.8737), "DV_BP_Mines_Support_Beam6_5_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_Mines_Support_Beam60 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (8746.104, 7429.9844, 2388.0903), (0.0, 0.0, -0.0), (0.6755, 3.8737, 0.6753), "DV_BP_Mines_Support_Beam60_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_Mines_Support_Beam61 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (9046.104, 7429.984, 2388.0903), (0.0, 0.0, -0.0), (0.6755, 3.8737, 0.6753), "DV_BP_Mines_Support_Beam61_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_Mines_Support_Beam62 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (9346.104, 7429.9844, 2388.0903), (0.0, 0.0, -0.0), (0.6755, 3.8737, 0.6753), "DV_BP_Mines_Support_Beam62_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_Mines_Support_Beam65 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (7970.1426, 7543.661, 2574.1304), (0.0, 0.0, -0.0), (3.8737, 0.6755, 0.6753), "DV_BP_Mines_Support_Beam65_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_Mines_Support_Beam66 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (9046.453, 7543.6577, 2560.4446), (0.0, 0.0, -0.0), (0.6754, 0.6755, 3.8737), "DV_BP_Mines_Support_Beam66_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_Mines_Support_Beam67 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (8146.4585, 7543.657, 2560.446), (0.0, 0.0, -0.0), (0.6754, 0.6755, 3.8737), "DV_BP_Mines_Support_Beam67_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_Mines_Support_Beam68 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (7851.467, 6033.6636, 2560.446), (0.0, 0.0, -0.0), (0.6755, 0.6754, 3.8737), "DV_BP_Mines_Support_Beam68_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_Mines_Support_Beam69 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (9666.452, 7543.6733, 2560.4446), (0.0, 0.0, -0.0), (0.6754, 0.6755, 3.8737), "DV_BP_Mines_Support_Beam69_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_Mines_Support_Beam70 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (8746.451, 7543.6577, 2560.446), (0.0, 0.0, -0.0), (0.6754, 0.6755, 3.8737), "DV_BP_Mines_Support_Beam70_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_Mines_Support_Beam71 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (7970.143, 5433.6606, 2574.1304), (0.0, 0.0, -0.0), (3.8737, 0.6755, 0.6753), "DV_BP_Mines_Support_Beam71_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_Mines_Support_Beam72 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (9046.453, 5433.658, 2560.4446), (0.0, 0.0, -0.0), (0.6754, 0.6755, 3.8737), "DV_BP_Mines_Support_Beam72_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_Mines_Support_Beam73 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (8146.456, 5433.657, 2560.446), (0.0, 0.0, -0.0), (0.6754, 0.6755, 3.8737), "DV_BP_Mines_Support_Beam73_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_Mines_Support_Beam75 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (9666.454, 5433.6733, 2560.4446), (0.0, 0.0, -0.0), (0.6754, 0.6755, 3.8737), "DV_BP_Mines_Support_Beam75_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_Mines_Support_Beam76 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (8746.451, 5433.657, 2560.446), (0.0, 0.0, -0.0), (0.6754, 0.6755, 3.8737), "DV_BP_Mines_Support_Beam76_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_Mines_Support_Beam8_7 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (10391.422, 5222.246, 883.68384), (0.0, 0.0, -0.0), (0.7824, 0.7824, 3.8737), "DV_BP_Mines_Support_Beam8_7_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_Mines_Support_Beam_B103 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (9791.589, 5715.178, 2391.0938), (0.0, 0.0, -0.0), (3.0396, 0.2910, 0.3265), "DV_BP_Mines_Support_Beam_B103_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_Mines_Support_Beam_B104 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (8005.986, 5435.178, 2391.1184), (0.0, 0.0, -0.0), (3.0396, 0.2910, 0.3265), "DV_BP_Mines_Support_Beam_B104_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_Mines_Support_Beam_B109 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (8301.588, 5435.1787, 2391.095), (0.0, 0.0, -0.0), (3.0396, 0.2910, 0.3265), "DV_BP_Mines_Support_Beam_B109_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_Mines_Support_Beam_B110 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (8591.588, 5435.179, 2391.095), (0.0, 0.0, -0.0), (3.0396, 0.2910, 0.3265), "DV_BP_Mines_Support_Beam_B110_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_Mines_Support_Beam_B130 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (10369.236, 5361.322, 1041.5116), (0.0, 0.0, -0.0), (0.8494, 3.0502, 0.2910), "DV_BP_Mines_Support_Beam_B130_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_Mines_Support_Beam_B131_308 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (8891.588, 5435.179, 2391.095), (0.0, 0.0, -0.0), (3.0396, 0.2910, 0.3265), "DV_BP_Mines_Support_Beam_B131_308_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_Mines_Support_Beam_B132_309 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (9191.588, 5435.1787, 2391.095), (0.0, 0.0, -0.0), (3.0396, 0.2910, 0.3265), "DV_BP_Mines_Support_Beam_B132_309_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_Mines_Support_Beam_B134_63 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (8004.5117, 4703.0024, 1151.5116), (0.0, 0.0, -0.0), (3.0396, 0.3265, 0.2910), "DV_BP_Mines_Support_Beam_B134_63_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_Mines_Support_Beam_B135_65 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (8294.512, 4703.002, 1151.5116), (0.0, 0.0, -0.0), (3.0396, 0.3265, 0.2910), "DV_BP_Mines_Support_Beam_B135_65_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_Mines_Support_Beam_B136 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (8452.649, 4713.0, 1024.0488), (0.0, 0.0, -0.0), (0.2910, 0.3265, 3.0396), "DV_BP_Mines_Support_Beam_B136_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_Mines_Support_Beam_B137 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (8559.925, 4609.5254, 1151.5116), (0.0, 0.0, -0.0), (2.3802, 2.3802, 0.2910), "DV_BP_Mines_Support_Beam_B137_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_Mines_Support_Beam_B138 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (8662.648, 4503.0, 1024.0488), (0.0, 0.0, -0.0), (0.2910, 0.3265, 3.0396), "DV_BP_Mines_Support_Beam_B138_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_Mines_Support_Beam_B140 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (8662.3, 4360.8135, 1151.5116), (0.0, 0.0, -0.0), (0.3265, 3.0396, 0.2910), "DV_BP_Mines_Support_Beam_B140_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_Mines_Support_Beam_B141 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (7738.1274, 4812.374, 1094.9269), (0.0, 0.0, -0.0), (2.9938, 0.3265, 1.1580), "DV_BP_Mines_Support_Beam_B141_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_Mines_Support_Beam_B142 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (7763.874, 4743.3096, 1177.7357), (0.0, 0.0, -0.0), (0.8792, 1.5070, 2.9223), "DV_BP_Mines_Support_Beam_B142_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_Mines_Support_Beam_B143_310 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (9491.588, 5435.1787, 2391.095), (0.0, 0.0, -0.0), (3.0396, 0.2910, 0.3265), "DV_BP_Mines_Support_Beam_B143_310_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_Mines_Support_Beam_B194 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (7853.774, 5887.715, 2391.4446), (0.0, 0.0, -0.0), (0.3265, 3.0396, 0.2910), "DV_BP_Mines_Support_Beam_B194_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_Mines_Support_Beam_B195 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (8153.774, 5887.713, 2391.4421), (0.0, 0.0, -0.0), (0.3265, 3.0396, 0.2910), "DV_BP_Mines_Support_Beam_B195_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_Mines_Support_Beam_B196 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (7853.774, 6187.717, 2391.444), (0.0, 0.0, -0.0), (0.3265, 3.0396, 0.2910), "DV_BP_Mines_Support_Beam_B196_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_Mines_Support_Beam_B197 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (8153.7754, 6187.717, 2391.4434), (0.0, 0.0, -0.0), (0.3265, 3.0396, 0.2910), "DV_BP_Mines_Support_Beam_B197_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_Mines_Support_Beam_B198 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (8005.9893, 6035.1772, 2391.1177), (0.0, 0.0, -0.0), (3.0396, 0.2910, 0.3265), "DV_BP_Mines_Support_Beam_B198_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_Mines_Support_Beam_B199_178 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (7853.773, 6487.717, 2391.444), (0.0, 0.0, -0.0), (0.3265, 3.0396, 0.2910), "DV_BP_Mines_Support_Beam_B199_178_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_Mines_Support_Beam_B200 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (8005.9873, 6325.181, 2391.1182), (0.0, 0.0, -0.0), (3.0396, 0.2910, 0.3265), "DV_BP_Mines_Support_Beam_B200_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_Mines_Support_Beam_B201_179 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (8153.776, 6487.7153, 2391.4434), (0.0, 0.0, -0.0), (0.3265, 3.0396, 0.2910), "DV_BP_Mines_Support_Beam_B201_179_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_Mines_Support_Beam_B202_182 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (8005.9893, 6635.178, 2391.1177), (0.0, 0.0, -0.0), (3.0396, 0.2910, 0.3265), "DV_BP_Mines_Support_Beam_B202_182_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_Mines_Support_Beam_B203_196 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (8453.798, 5887.716, 2390.7686), (0.0, 0.0, -0.0), (0.3265, 3.0396, 0.2910), "DV_BP_Mines_Support_Beam_B203_196_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_Mines_Support_Beam_B204_186 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (8005.9893, 6945.1777, 2391.1177), (0.0, 0.0, -0.0), (3.0396, 0.2910, 0.3265), "DV_BP_Mines_Support_Beam_B204_186_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_Mines_Support_Beam_B206_2 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (8453.798, 6187.716, 2390.7686), (0.0, 0.0, -0.0), (0.3265, 3.0396, 0.2910), "DV_BP_Mines_Support_Beam_B206_2_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_Mines_Support_Beam_B207 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (8453.798, 6487.716, 2390.7686), (0.0, 0.0, -0.0), (0.3265, 3.0396, 0.2910), "DV_BP_Mines_Support_Beam_B207_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_Mines_Support_Beam_B208 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (8453.798, 6787.716, 2390.7686), (0.0, 0.0, -0.0), (0.3265, 3.0396, 0.2910), "DV_BP_Mines_Support_Beam_B208_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_Mines_Support_Beam_B209_197 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (8453.8, 6187.7173, 2390.768), (0.0, 0.0, -0.0), (0.3265, 3.0396, 0.2910), "DV_BP_Mines_Support_Beam_B209_197_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_Mines_Support_Beam_B210_198 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (8301.584, 6035.1777, 2391.0942), (0.0, 0.0, -0.0), (3.0396, 0.2910, 0.3265), "DV_BP_Mines_Support_Beam_B210_198_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_Mines_Support_Beam_B213_202 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (8453.8, 6487.718, 2390.768), (0.0, 0.0, -0.0), (0.3265, 3.0396, 0.2910), "DV_BP_Mines_Support_Beam_B213_202_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_Mines_Support_Beam_B214_203 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (8301.584, 6635.1777, 2391.0942), (0.0, 0.0, -0.0), (3.0396, 0.2910, 0.3265), "DV_BP_Mines_Support_Beam_B214_203_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_Mines_Support_Beam_B215_204 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (8301.584, 6945.1777, 2391.0942), (0.0, 0.0, -0.0), (3.0396, 0.2910, 0.3265), "DV_BP_Mines_Support_Beam_B215_204_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_Mines_Support_Beam_B216_214 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (8743.798, 5887.716, 2390.7686), (0.0, 0.0, -0.0), (0.3265, 3.0396, 0.2910), "DV_BP_Mines_Support_Beam_B216_214_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_Mines_Support_Beam_B217 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (8601.584, 6945.1777, 2391.0957), (0.0, 0.0, -0.0), (3.0396, 0.2910, 0.3265), "DV_BP_Mines_Support_Beam_B217_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_Mines_Support_Beam_B218_216 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (8591.584, 6035.1777, 2391.0942), (0.0, 0.0, -0.0), (3.0396, 0.2910, 0.3265), "DV_BP_Mines_Support_Beam_B218_216_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_Mines_Support_Beam_B219 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (8901.584, 6945.1777, 2391.0972), (0.0, 0.0, -0.0), (3.0396, 0.2910, 0.3265), "DV_BP_Mines_Support_Beam_B219_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_Mines_Support_Beam_B220 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (9201.584, 6945.1777, 2391.0986), (0.0, 0.0, -0.0), (3.0396, 0.2910, 0.3265), "DV_BP_Mines_Support_Beam_B220_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_Mines_Support_Beam_B221_219 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (8743.8, 6487.7173, 2390.768), (0.0, 0.0, -0.0), (0.3265, 3.0396, 0.2910), "DV_BP_Mines_Support_Beam_B221_219_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_Mines_Support_Beam_B222 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (9501.584, 6945.1777, 2391.1), (0.0, 0.0, -0.0), (3.0396, 0.2910, 0.3265), "DV_BP_Mines_Support_Beam_B222_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_Mines_Support_Beam_B223_221 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (8591.584, 6945.178, 2391.0942), (0.0, 0.0, -0.0), (3.0396, 0.2910, 0.3265), "DV_BP_Mines_Support_Beam_B223_221_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_Mines_Support_Beam_B224_231 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (9043.797, 5887.716, 2390.7686), (0.0, 0.0, -0.0), (0.3265, 3.0396, 0.2910), "DV_BP_Mines_Support_Beam_B224_231_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_Mines_Support_Beam_B225_232 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (9043.8, 6187.717, 2390.768), (0.0, 0.0, -0.0), (0.3265, 3.0396, 0.2910), "DV_BP_Mines_Support_Beam_B225_232_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_Mines_Support_Beam_B226_233 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (8891.584, 6035.1772, 2391.0942), (0.0, 0.0, -0.0), (3.0396, 0.2910, 0.3265), "DV_BP_Mines_Support_Beam_B226_233_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_Mines_Support_Beam_B227 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (8891.586, 6325.18, 2391.0938), (0.0, 0.0, -0.0), (3.0396, 0.2910, 0.3265), "DV_BP_Mines_Support_Beam_B227_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_Mines_Support_Beam_B231 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (8891.584, 6945.1777, 2391.0942), (0.0, 0.0, -0.0), (3.0396, 0.2910, 0.3265), "DV_BP_Mines_Support_Beam_B231_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_Mines_Support_Beam_B232 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (9343.798, 5887.716, 2390.7686), (0.0, 0.0, -0.0), (0.3265, 3.0396, 0.2910), "DV_BP_Mines_Support_Beam_B232_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_Mines_Support_Beam_B233 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (9343.8, 6187.7173, 2390.768), (0.0, 0.0, -0.0), (0.3265, 3.0396, 0.2910), "DV_BP_Mines_Support_Beam_B233_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_Mines_Support_Beam_B234 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (9191.584, 6035.1777, 2391.0942), (0.0, 0.0, -0.0), (3.0396, 0.2910, 0.3265), "DV_BP_Mines_Support_Beam_B234_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_Mines_Support_Beam_B235 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (9191.586, 6325.18, 2391.0938), (0.0, 0.0, -0.0), (3.0396, 0.2910, 0.3265), "DV_BP_Mines_Support_Beam_B235_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_Mines_Support_Beam_B237 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (9343.8, 6487.718, 2390.768), (0.0, 0.0, -0.0), (0.3265, 3.0396, 0.2910), "DV_BP_Mines_Support_Beam_B237_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_Mines_Support_Beam_B239 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (9191.584, 6945.1772, 2391.0942), (0.0, 0.0, -0.0), (3.0396, 0.2910, 0.3265), "DV_BP_Mines_Support_Beam_B239_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_Mines_Support_Beam_B240 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (9643.798, 5887.716, 2390.7686), (0.0, 0.0, -0.0), (0.3265, 3.0396, 0.2910), "DV_BP_Mines_Support_Beam_B240_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_Mines_Support_Beam_B241 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (9643.8, 6187.7173, 2390.768), (0.0, 0.0, -0.0), (0.3265, 3.0396, 0.2910), "DV_BP_Mines_Support_Beam_B241_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_Mines_Support_Beam_B242 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (9491.583, 6035.1777, 2391.0942), (0.0, 0.0, -0.0), (3.0396, 0.2910, 0.3265), "DV_BP_Mines_Support_Beam_B242_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_Mines_Support_Beam_B245 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (9643.8, 6487.7173, 2390.768), (0.0, 0.0, -0.0), (0.3265, 3.0396, 0.2910), "DV_BP_Mines_Support_Beam_B245_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_Mines_Support_Beam_B246 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (9491.584, 6635.1772, 2391.0942), (0.0, 0.0, -0.0), (3.0396, 0.2910, 0.3265), "DV_BP_Mines_Support_Beam_B246_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_Mines_Support_Beam_B247 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (9491.584, 6945.178, 2391.0942), (0.0, 0.0, -0.0), (3.0396, 0.2910, 0.3265), "DV_BP_Mines_Support_Beam_B247_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_Mines_Support_Beam_B248 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (9908.799, 5887.7153, 2390.7686), (0.0, 0.0, -0.0), (0.3265, 3.0396, 0.2910), "DV_BP_Mines_Support_Beam_B248_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_Mines_Support_Beam_B249 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (9908.8, 6187.7173, 2390.768), (0.0, 0.0, -0.0), (0.3265, 3.0396, 0.2910), "DV_BP_Mines_Support_Beam_B249_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_Mines_Support_Beam_B250 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (9791.585, 6035.1777, 2391.0942), (0.0, 0.0, -0.0), (3.0396, 0.2910, 0.3265), "DV_BP_Mines_Support_Beam_B250_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_Mines_Support_Beam_B251 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (9831.585, 6325.1807, 2391.094), (0.0, 0.0, -0.0), (3.0396, 0.2910, 0.3265), "DV_BP_Mines_Support_Beam_B251_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_Mines_Support_Beam_B252 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (9908.799, 6787.7153, 2390.7686), (0.0, 0.0, -0.0), (0.3265, 3.0396, 0.2910), "DV_BP_Mines_Support_Beam_B252_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_Mines_Support_Beam_B253 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (9908.8, 6487.7173, 2390.768), (0.0, 0.0, -0.0), (0.3265, 3.0396, 0.2910), "DV_BP_Mines_Support_Beam_B253_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_Mines_Support_Beam_B254 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (9831.583, 6635.1777, 2391.0945), (0.0, 0.0, -0.0), (3.0396, 0.2910, 0.3265), "DV_BP_Mines_Support_Beam_B254_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_Mines_Support_Beam_B255 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (9791.584, 6945.1777, 2391.0942), (0.0, 0.0, -0.0), (3.0396, 0.2910, 0.3265), "DV_BP_Mines_Support_Beam_B255_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_Mines_Support_Beam_B256_269 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (10203.768, 5887.7153, 2391.4446), (0.0, 0.0, -0.0), (0.3265, 3.0396, 0.2910), "DV_BP_Mines_Support_Beam_B256_269_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_Mines_Support_Beam_B257_270 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (10203.768, 6187.7173, 2391.444), (0.0, 0.0, -0.0), (0.3265, 3.0396, 0.2910), "DV_BP_Mines_Support_Beam_B257_270_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_Mines_Support_Beam_B258 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (10193.771, 5887.718, 2571.4446), (0.0, 0.0, -0.0), (0.3265, 3.0396, 0.2910), "DV_BP_Mines_Support_Beam_B258_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_Mines_Support_Beam_B259 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (10193.7705, 6187.717, 2571.4446), (0.0, 0.0, -0.0), (0.3265, 3.0396, 0.2910), "DV_BP_Mines_Support_Beam_B259_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_Mines_Support_Beam_B260 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (10203.768, 6487.7173, 2391.444), (0.0, 0.0, -0.0), (0.3265, 3.0396, 0.2910), "DV_BP_Mines_Support_Beam_B260_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_Mines_Support_Beam_B261 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (10193.7705, 6487.7163, 2571.4446), (0.0, 0.0, -0.0), (0.3265, 3.0396, 0.2910), "DV_BP_Mines_Support_Beam_B261_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_Mines_Support_Beam_B262 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (7853.7734, 6787.717, 2391.444), (0.0, 0.0, -0.0), (0.3265, 3.0396, 0.2910), "DV_BP_Mines_Support_Beam_B262_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_Mines_Support_Beam_B263 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (8153.776, 6787.716, 2391.4434), (0.0, 0.0, -0.0), (0.3265, 3.0396, 0.2910), "DV_BP_Mines_Support_Beam_B263_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_Mines_Support_Beam_B264 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (8453.8, 6787.7173, 2390.768), (0.0, 0.0, -0.0), (0.3265, 3.0396, 0.2910), "DV_BP_Mines_Support_Beam_B264_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_Mines_Support_Beam_B265 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (8743.8, 6787.718, 2390.768), (0.0, 0.0, -0.0), (0.3265, 3.0396, 0.2910), "DV_BP_Mines_Support_Beam_B265_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_Mines_Support_Beam_B267 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (9343.8, 6787.717, 2390.768), (0.0, 0.0, -0.0), (0.3265, 3.0396, 0.2910), "DV_BP_Mines_Support_Beam_B267_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_Mines_Support_Beam_B268 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (9643.8, 6787.7173, 2390.768), (0.0, 0.0, -0.0), (0.3265, 3.0396, 0.2910), "DV_BP_Mines_Support_Beam_B268_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_Mines_Support_Beam_B269 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (10193.799, 6787.7173, 2390.768), (0.0, 0.0, -0.0), (0.3265, 3.0396, 0.2910), "DV_BP_Mines_Support_Beam_B269_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_Mines_Support_Beam_B270 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (7853.774, 7087.7173, 2391.444), (0.0, 0.0, -0.0), (0.3265, 3.0396, 0.2910), "DV_BP_Mines_Support_Beam_B270_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_Mines_Support_Beam_B271 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (8153.7764, 7087.716, 2391.4434), (0.0, 0.0, -0.0), (0.3265, 3.0396, 0.2910), "DV_BP_Mines_Support_Beam_B271_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_Mines_Support_Beam_B272 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (8453.801, 7087.717, 2390.768), (0.0, 0.0, -0.0), (0.3265, 3.0396, 0.2910), "DV_BP_Mines_Support_Beam_B272_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_Mines_Support_Beam_B274 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (9043.801, 7087.7173, 2390.768), (0.0, 0.0, -0.0), (0.3265, 3.0396, 0.2910), "DV_BP_Mines_Support_Beam_B274_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_Mines_Support_Beam_B275 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (9343.801, 7087.717, 2390.768), (0.0, 0.0, -0.0), (0.3265, 3.0396, 0.2910), "DV_BP_Mines_Support_Beam_B275_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_Mines_Support_Beam_B276 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (9643.801, 7087.7173, 2390.768), (0.0, 0.0, -0.0), (0.3265, 3.0396, 0.2910), "DV_BP_Mines_Support_Beam_B276_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_Mines_Support_Beam_B277 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (10193.8, 7087.7173, 2390.768), (0.0, 0.0, -0.0), (0.3265, 3.0396, 0.2910), "DV_BP_Mines_Support_Beam_B277_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_Mines_Support_Beam_B278 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (8005.9893, 7245.177, 2391.1162), (0.0, 0.0, -0.0), (3.0396, 0.2910, 0.3265), "DV_BP_Mines_Support_Beam_B278_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_Mines_Support_Beam_B279 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (8301.585, 7245.1777, 2391.0928), (0.0, 0.0, -0.0), (3.0396, 0.2910, 0.3265), "DV_BP_Mines_Support_Beam_B279_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_Mines_Support_Beam_B280 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (8591.584, 7245.1777, 2391.0928), (0.0, 0.0, -0.0), (3.0396, 0.2910, 0.3265), "DV_BP_Mines_Support_Beam_B280_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_Mines_Support_Beam_B281 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (8891.584, 7245.1777, 2391.0928), (0.0, 0.0, -0.0), (3.0396, 0.2910, 0.3265), "DV_BP_Mines_Support_Beam_B281_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_Mines_Support_Beam_B282 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (9191.584, 7245.1777, 2391.0928), (0.0, 0.0, -0.0), (3.0396, 0.2910, 0.3265), "DV_BP_Mines_Support_Beam_B282_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_Mines_Support_Beam_B283 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (9491.584, 7245.1772, 2391.0928), (0.0, 0.0, -0.0), (3.0396, 0.2910, 0.3265), "DV_BP_Mines_Support_Beam_B283_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_Mines_Support_Beam_B284 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (9791.584, 7245.1777, 2391.0928), (0.0, 0.0, -0.0), (3.0396, 0.2910, 0.3265), "DV_BP_Mines_Support_Beam_B284_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_Mines_Support_Beam_B285 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (8005.9893, 7545.1777, 2391.1145), (0.0, 0.0, -0.0), (3.0396, 0.2910, 0.3265), "DV_BP_Mines_Support_Beam_B285_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_Mines_Support_Beam_B286 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (8301.588, 7545.178, 2391.091), (0.0, 0.0, -0.0), (3.0396, 0.2910, 0.3265), "DV_BP_Mines_Support_Beam_B286_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_Mines_Support_Beam_B287 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (8591.584, 7545.178, 2391.091), (0.0, 0.0, -0.0), (3.0396, 0.2910, 0.3265), "DV_BP_Mines_Support_Beam_B287_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_Mines_Support_Beam_B288 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (8891.584, 7545.1777, 2391.091), (0.0, 0.0, -0.0), (3.0396, 0.2910, 0.3265), "DV_BP_Mines_Support_Beam_B288_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_Mines_Support_Beam_B289 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (9191.584, 7545.1777, 2391.091), (0.0, 0.0, -0.0), (3.0396, 0.2910, 0.3265), "DV_BP_Mines_Support_Beam_B289_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_Mines_Support_Beam_B290 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (9491.584, 7545.178, 2391.091), (0.0, 0.0, -0.0), (3.0396, 0.2910, 0.3265), "DV_BP_Mines_Support_Beam_B290_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_Mines_Support_Beam_B291_500 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (9791.584, 7545.1777, 2391.091), (0.0, 0.0, -0.0), (3.0396, 0.2910, 0.3265), "DV_BP_Mines_Support_Beam_B291_500_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_Mines_Support_Beam_B292 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (10193.769, 6787.7173, 2571.4443), (0.0, 0.0, -0.0), (0.3265, 3.0396, 0.2910), "DV_BP_Mines_Support_Beam_B292_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_Mines_Support_Beam_B293 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (10193.77, 7087.7163, 2571.4443), (0.0, 0.0, -0.0), (0.3265, 3.0396, 0.2910), "DV_BP_Mines_Support_Beam_B293_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_Mines_Support_Beam_B294_320 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (7843.7754, 5887.7134, 2571.452), (0.0, 0.0, -0.0), (0.3265, 3.0396, 0.2910), "DV_BP_Mines_Support_Beam_B294_320_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_Mines_Support_Beam_B295 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (7843.7754, 6187.713, 2571.452), (0.0, 0.0, -0.0), (0.3265, 3.0396, 0.2910), "DV_BP_Mines_Support_Beam_B295_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_Mines_Support_Beam_B296 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (7843.7754, 6487.713, 2571.452), (0.0, 0.0, -0.0), (0.3265, 3.0396, 0.2910), "DV_BP_Mines_Support_Beam_B296_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_Mines_Support_Beam_B297 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (7843.7744, 6787.714, 2571.4517), (0.0, 0.0, -0.0), (0.3265, 3.0396, 0.2910), "DV_BP_Mines_Support_Beam_B297_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_Mines_Support_Beam_B298 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (7843.775, 7087.7124, 2571.4517), (0.0, 0.0, -0.0), (0.3265, 3.0396, 0.2910), "DV_BP_Mines_Support_Beam_B298_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_Mines_Support_Beam_B299 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (8310.508, 7551.3496, 2571.452), (0.0, 0.0, -0.0), (3.0396, 0.3265, 0.2910), "DV_BP_Mines_Support_Beam_B299_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_Mines_Support_Beam_B300 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (8610.505, 7551.3496, 2571.452), (0.0, 0.0, -0.0), (3.0396, 0.3265, 0.2910), "DV_BP_Mines_Support_Beam_B300_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_Mines_Support_Beam_B301 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (8910.503, 7551.3496, 2571.452), (0.0, 0.0, -0.0), (3.0396, 0.3265, 0.2910), "DV_BP_Mines_Support_Beam_B301_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_Mines_Support_Beam_B302 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (9210.505, 7551.347, 2571.4517), (0.0, 0.0, -0.0), (3.0396, 0.3265, 0.2910), "DV_BP_Mines_Support_Beam_B302_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_Mines_Support_Beam_B303 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (9510.504, 7551.3506, 2571.4517), (0.0, 0.0, -0.0), (3.0396, 0.3265, 0.2910), "DV_BP_Mines_Support_Beam_B303_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_Mines_Support_Beam_B304 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (8310.505, 5441.3496, 2571.452), (0.0, 0.0, -0.0), (3.0396, 0.3265, 0.2910), "DV_BP_Mines_Support_Beam_B304_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_Mines_Support_Beam_B305 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (8610.502, 5441.3496, 2571.452), (0.0, 0.0, -0.0), (3.0396, 0.3265, 0.2910), "DV_BP_Mines_Support_Beam_B305_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_Mines_Support_Beam_B306 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (8910.503, 5441.3496, 2571.452), (0.0, 0.0, -0.0), (3.0396, 0.3265, 0.2910), "DV_BP_Mines_Support_Beam_B306_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_Mines_Support_Beam_B307 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (9210.504, 5441.3477, 2571.4517), (0.0, 0.0, -0.0), (3.0396, 0.3265, 0.2910), "DV_BP_Mines_Support_Beam_B307_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_Mines_Support_Beam_B308 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (9510.503, 5441.3506, 2571.4517), (0.0, 0.0, -0.0), (3.0396, 0.3265, 0.2910), "DV_BP_Mines_Support_Beam_B308_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_Mines_Support_Beam_B310_501 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (10091.584, 7545.178, 2391.091), (0.0, 0.0, -0.0), (3.0396, 0.2910, 0.3265), "DV_BP_Mines_Support_Beam_B310_501_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_Mines_Support_Beam_B311 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (9810.505, 7551.347, 2571.4517), (0.0, 0.0, -0.0), (3.0396, 0.3265, 0.2910), "DV_BP_Mines_Support_Beam_B311_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_Mines_Support_Beam_B312 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (10110.504, 7551.3506, 2571.4517), (0.0, 0.0, -0.0), (3.0396, 0.3265, 0.2910), "DV_BP_Mines_Support_Beam_B312_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_Mines_Support_Beam_B315 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (10091.585, 6035.1777, 2391.0942), (0.0, 0.0, -0.0), (3.0396, 0.2910, 0.3265), "DV_BP_Mines_Support_Beam_B315_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_Mines_Support_Beam_B316 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (10131.585, 6325.1807, 2391.094), (0.0, 0.0, -0.0), (3.0396, 0.2910, 0.3265), "DV_BP_Mines_Support_Beam_B316_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_Mines_Support_Beam_B317 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (10131.583, 6635.1777, 2391.0945), (0.0, 0.0, -0.0), (3.0396, 0.2910, 0.3265), "DV_BP_Mines_Support_Beam_B317_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_Mines_Support_Beam_B318 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (10091.584, 6945.1777, 2391.0942), (0.0, 0.0, -0.0), (3.0396, 0.2910, 0.3265), "DV_BP_Mines_Support_Beam_B318_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_Mines_Support_Beam_B319 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (10091.584, 7245.1777, 2391.0928), (0.0, 0.0, -0.0), (3.0396, 0.2910, 0.3265), "DV_BP_Mines_Support_Beam_B319_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_Mines_Support_Beam_B93 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (8891.588, 5715.179, 2391.0938), (0.0, 0.0, -0.0), (3.0396, 0.2910, 0.3265), "DV_BP_Mines_Support_Beam_B93_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_Mines_Support_Beam_B94 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (9191.589, 5715.1787, 2391.0938), (0.0, 0.0, -0.0), (3.0396, 0.2910, 0.3265), "DV_BP_Mines_Support_Beam_B94_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_Mines_Support_Beam_B95 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (9491.588, 5715.178, 2391.0938), (0.0, 0.0, -0.0), (3.0396, 0.2910, 0.3265), "DV_BP_Mines_Support_Beam_B95_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_Mines_Support_Beam_B96_22 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (8004.5127, 5363.0024, 1081.5116), (0.0, 0.0, -0.0), (3.0396, 0.3265, 0.2910), "DV_BP_Mines_Support_Beam_B96_22_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_Mines_Support_Beam_B97 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (10494.443, 5527.782, 1041.5116), (0.0, 0.0, -0.0), (3.0502, 0.8494, 0.2910), "DV_BP_Mines_Support_Beam_B97_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_Mines_Support_Beam_B98 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (4646.993, 5004.5156, 2131.5115), (0.0, 0.0, -0.0), (0.3265, 3.0396, 0.2910), "DV_BP_Mines_Support_Beam_B98_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_Orc_Remains_C_2 (EMorSimpleShape::Empty)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (2830.0, 5085.0, 805.0), (0.0, 0.0, -0.0), (2.0000, 2.0000, 2.0000), "DV_BP_Orc_Remains_C_2", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_Orc_Remains_E_2 (EMorSimpleShape::Empty)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (2694.1843, 5741.4463, 840.0), (0.0, 115.0000893628421, -0.0), (2.0000, 2.0000, 2.0000), "DV_BP_Orc_Remains_E_2", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: CBP_MapStone_World_2 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (931.9253, 2821.7183, 900.0038), (0.0, 90.00005166594045, -0.0), (2.0000, 2.0000, 2.3053), "DV_CBP_MapStone_World_2", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: Deep_WoodenPlank_A10_261 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (1238.1455, 5922.1953, 1059.1201), (0.0, 0.0, -0.0), (6.6087, 1.1180, 0.5585), "DV_Deep_WoodenPlank_A10_261_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: Deep_WoodenPlank_A11_262 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (1225.9902, 5913.4526, 1161.4214), (0.0, 0.0, -0.0), (6.2672, 1.0304, 0.7301), "DV_Deep_WoodenPlank_A11_262_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: Deep_WoodenPlank_A12_263 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (1234.7695, 5912.8774, 1433.4165), (0.0, 0.0, -0.0), (6.2713, 1.0454, 0.9314), "DV_Deep_WoodenPlank_A12_263_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: Deep_WoodenPlank_A13_169 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (4452.091, 6188.9155, 803.1997), (0.0, 0.0, -0.0), (6.0204, 1.1519, 0.5686), "DV_Deep_WoodenPlank_A13_169_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: Deep_WoodenPlank_A14_240 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (5643.1973, 4991.01, 1088.1665), (0.0, 0.0, -0.0), (6.0053, 0.5594, 0.3045), "DV_Deep_WoodenPlank_A14_240_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: Deep_WoodenPlank_A15_244 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (5799.1196, 5286.773, 964.9209), (0.0, 0.0, -0.0), (4.3246, 3.0885, 3.9959), "DV_Deep_WoodenPlank_A15_244_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: Deep_WoodenPlank_A16 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (5905.655, 5604.3804, 796.0801), (0.0, 0.0, -0.0), (5.8839, 2.2902, 0.3365), "DV_Deep_WoodenPlank_A16_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: Deep_WoodenPlank_A17 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (5443.708, 6256.7896, 795.68066), (0.0, 0.0, -0.0), (6.0186, 1.1958, 0.6347), "DV_Deep_WoodenPlank_A17_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: Deep_WoodenPlank_A20 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (1744.0635, 4716.635, 1069.4883), (0.0, 0.0, -0.0), (6.2636, 2.1023, 2.4464), "DV_Deep_WoodenPlank_A20_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: Deep_WoodenPlank_A21 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (1791.4131, 4677.759, 1398.2686), (0.0, 0.0, -0.0), (6.2420, 1.2820, 1.0276), "DV_Deep_WoodenPlank_A21_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: Deep_WoodenPlank_A22 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (1790.4854, 4694.2285, 1285.9521), (0.0, 0.0, -0.0), (6.2626, 1.2090, 0.7469), "DV_Deep_WoodenPlank_A22_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: Deep_WoodenPlank_A23 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (2384.0469, 4717.7793, 1544.9961), (0.0, 0.0, -0.0), (6.3001, 0.2365, 0.7991), "DV_Deep_WoodenPlank_A23_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: Deep_WoodenPlank_A24 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (2391.0547, 4723.0215, 1395.7344), (0.0, 0.0, -0.0), (6.2914, 0.2223, 0.6165), "DV_Deep_WoodenPlank_A24_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: Deep_WoodenPlank_A25 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (2388.8691, 4727.407, 1271.4321), (0.0, 0.0, -0.0), (6.2917, 0.2901, 0.6368), "DV_Deep_WoodenPlank_A25_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: Deep_WoodenPlank_A26 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (2959.2441, 4720.9365, 1174.6641), (0.0, 0.0, -0.0), (6.3018, 0.3718, 1.2694), "DV_Deep_WoodenPlank_A26_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: Deep_WoodenPlank_A27 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (3017.1377, 4777.214, 1384.6606), (0.0, 0.0, -0.0), (6.1487, 1.7249, 0.6108), "DV_Deep_WoodenPlank_A27_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: Deep_WoodenPlank_A28 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (1820.4609, 5954.399, 1135.0098), (0.0, 0.0, -0.0), (6.2998, 0.3353, 0.7287), "DV_Deep_WoodenPlank_A28_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: Deep_WoodenPlank_A29 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (1820.4609, 5956.3535, 1336.6045), (0.0, 0.0, -0.0), (6.2973, 0.2067, 0.7287), "DV_Deep_WoodenPlank_A29_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: Deep_WoodenPlank_A30 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (1820.4629, 5949.652, 1479.4219), (0.0, 0.0, -0.0), (6.2931, 0.3304, 0.6027), "DV_Deep_WoodenPlank_A30_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: Deep_WoodenPlank_A31 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (1276.8435, 3912.0288, 1073.8728), (0.0, 0.0, -0.0), (1.9552, 6.4803, 1.0201), "DV_Deep_WoodenPlank_A31_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: Deep_WoodenPlank_A33 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (1271.8564, 3912.3643, 1409.5703), (0.0, 0.0, -0.0), (1.8329, 6.1356, 0.9314), "DV_Deep_WoodenPlank_A33_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: Deep_WoodenPlank_A34 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (1377.9099, 3349.3184, 1250.0312), (0.0, 0.0, -0.0), (1.0644, 6.1389, 2.2355), "DV_Deep_WoodenPlank_A34_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: Deep_WoodenPlank_A36 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (1383.3018, 3336.1948, 1455.5762), (0.0, 0.0, -0.0), (1.1302, 6.2516, 0.6026), "DV_Deep_WoodenPlank_A36_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: Deep_WoodenPlank_A37 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (1215.8405, 2086.3384, 1035.2744), (0.0, 0.0, -0.0), (0.7767, 6.6411, 0.5585), "DV_Deep_WoodenPlank_A37_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: Deep_WoodenPlank_A38 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (1209.9702, 2100.1135, 1137.5752), (0.0, 0.0, -0.0), (0.7649, 6.2904, 0.7301), "DV_Deep_WoodenPlank_A38_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: Deep_WoodenPlank_A39 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (1207.4858, 2091.6743, 1409.5703), (0.0, 0.0, -0.0), (0.7318, 6.2964, 0.9314), "DV_Deep_WoodenPlank_A39_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: Deep_WoodenPlank_A40 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (1115.1483, 1512.1354, 1455.5762), (0.0, 0.0, -0.0), (1.4553, 6.2013, 0.6026), "DV_Deep_WoodenPlank_A40_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: Deep_WoodenPlank_A41 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (1121.6901, 1510.6667, 1312.7588), (0.0, 0.0, -0.0), (1.5801, 6.1851, 0.7287), "DV_Deep_WoodenPlank_A41_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: Deep_WoodenPlank_A42 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (1119.779, 1511.0984, 1111.1641), (0.0, 0.0, -0.0), (1.7044, 6.1594, 0.7287), "DV_Deep_WoodenPlank_A42_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: Deep_WoodenPlank_B10 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (4197.3115, 6342.8545, 1029.5674), (0.0, 0.0, -0.0), (2.1035, 2.4701, 5.6215), "DV_Deep_WoodenPlank_B10_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: Deep_WoodenPlank_B11_232 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (5621.1704, 4929.22, 1077.2354), (0.0, 0.0, -0.0), (4.9879, 4.7068, 0.1689), "DV_Deep_WoodenPlank_B11_232_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: Deep_WoodenPlank_B12 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (5715.492, 4861.2314, 1077.2354), (0.0, 0.0, -0.0), (5.0259, 4.6639, 0.1689), "DV_Deep_WoodenPlank_B12_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: Deep_WoodenPlank_B13 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (5164.8164, 6232.7944, 800.10986), (0.0, 0.0, -0.0), (6.0005, 2.5189, 0.4238), "DV_Deep_WoodenPlank_B13_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: Deep_WoodenPlank_B14 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (5233.3086, 6372.2764, 800.2803), (0.0, 0.0, -0.0), (6.0216, 0.9922, 0.6770), "DV_Deep_WoodenPlank_B14_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: Deep_WoodenPlank_B15_106 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (6847.452, 6648.9985, 849.2365), (0.0, 0.0, -0.0), (5.2025, 4.2752, 1.5595), "DV_Deep_WoodenPlank_B15_106_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: Deep_WoodenPlank_B16 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (8661.178, 8340.052, 800.0), (0.0, 0.0, -0.0), (6.0514, 1.9705, 0.8116), "DV_Deep_WoodenPlank_B16_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: Deep_WoodenPlank_B8 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (3166.9316, 5765.7744, 820.8843), (0.0, 0.0, -0.0), (6.0530, 1.1599, 1.1876), "DV_Deep_WoodenPlank_B8_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: Deep_WoodenPlank_B9_165 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (4122.793, 6372.593, 1068.8887), (0.0, 0.0, -0.0), (0.9527, 2.2115, 5.9403), "DV_Deep_WoodenPlank_B9_165_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: DM_Mines_Scaffolding_Platform_1X1M_A_Destructible_5 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (5055.068, 4820.1562, 1096.9222), (0.0, 0.0, -0.0), (1.1611, 1.1525, 0.2743), "DV_DM_Mines_Scaffolding_Platform_1X1M_A_Destructible_5_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: DM_Mines_Scaffolding_Platform_3X1M_A_Destructible_11 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (5172.598, 4715.366, 1094.4178), (0.0, 0.0, -0.0), (2.5993, 3.1190, 0.2869), "DV_DM_Mines_Scaffolding_Platform_3X1M_A_Destructible_11_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: DM_Mines_Scaffolding_Platform_3X1M_A_Destructible2 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (4954.2803, 5460.109, 825.2418), (0.0, 0.0, -0.0), (1.5097, 3.1501, 1.2834), "DV_DM_Mines_Scaffolding_Platform_3X1M_A_Destructible2_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: DM_Mines_Scaffolding_Platform_3X1M_A_Destructible3_4 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (5591.4927, 4729.2446, 1097.0717), (0.0, 0.0, -0.0), (3.2059, 1.6493, 0.2869), "DV_DM_Mines_Scaffolding_Platform_3X1M_A_Destructible3_4_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: DM_Mines_Scaffolding_Platform_3X1M_A_Destructible4 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (6982.956, 5091.3975, 938.9518), (0.0, 0.0, -0.0), (3.2075, 1.6573, 0.5072), "DV_DM_Mines_Scaffolding_Platform_3X1M_A_Destructible4_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: DM_Mines_Scaffolding_Platform_3X1M_A_Destructible5 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (4809.2144, 6617.7744, 973.7737), (0.0, 0.0, -0.0), (1.8512, 3.2321, 0.3880), "DV_DM_Mines_Scaffolding_Platform_3X1M_A_Destructible5_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: Mines_Machine_Whim_Side_Support_Beam_Broken_B10 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (8371.571, 5712.481, 2361.4167), (0.0, 0.0, -0.0), (1.6938, 0.6783, 1.2975), "DV_Mines_Machine_Whim_Side_Support_Beam_Broken_B10_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: Mines_Machine_Whim_Side_Support_Beam_Broken_B11 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (8544.251, 5715.7197, 2366.1453), (0.0, 0.0, -0.0), (1.7778, 0.4357, 1.0315), "DV_Mines_Machine_Whim_Side_Support_Beam_Broken_B11_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: Mines_Machine_Whim_Side_Support_Beam_Broken_B14 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (8747.719, 6892.7866, 2367.2498), (0.0, 0.0, -0.0), (0.3271, 1.6479, 1.1478), "DV_Mines_Machine_Whim_Side_Support_Beam_Broken_B14_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: Mines_Machine_Whim_Side_Support_Beam_Broken_B15 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (9337.719, 6901.949, 2358.0715), (0.0, 0.0, -0.0), (0.3271, 1.5349, 1.3333), "DV_Mines_Machine_Whim_Side_Support_Beam_Broken_B15_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: Mines_Machine_Whim_Side_Support_Beam_Broken_B16 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (9637.718, 6079.6895, 2357.2498), (0.0, 0.0, -0.0), (0.3271, 1.6479, 1.1478), "DV_Mines_Machine_Whim_Side_Support_Beam_Broken_B16_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: Mines_Machine_Whim_Side_Support_Beam_Broken_B17 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (9047.721, 6070.529, 2348.0715), (0.0, 0.0, -0.0), (0.3271, 1.5349, 1.3333), "DV_Mines_Machine_Whim_Side_Support_Beam_Broken_B17_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: Mines_Machine_Whim_Side_Support_Beam_Broken_B18 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (8511.555, 6322.6846, 2313.9897), (0.0, 0.0, -0.0), (1.2815, 0.5834, 1.6340), "DV_Mines_Machine_Whim_Side_Support_Beam_Broken_B18_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: Mines_Machine_Whim_Side_Support_Beam_Broken_B19 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (8533.77, 6646.45, 2328.6113), (0.0, 0.0, -0.0), (1.5852, 0.6767, 1.3054), "DV_Mines_Machine_Whim_Side_Support_Beam_Broken_B19_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: Mines_Machine_Whim_Side_Support_Beam_Broken_B20 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (9643.99, 6638.387, 2366.4072), (0.0, 0.0, -0.0), (1.7162, 0.3997, 1.1364), "DV_Mines_Machine_Whim_Side_Support_Beam_Broken_B20_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: Mines_Machine_Whim_Side_Support_Beam_Broken_B21 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (9630.3545, 6311.73, 2361.6975), (0.0, 0.0, -0.0), (1.6283, 0.6131, 1.2430), "DV_Mines_Machine_Whim_Side_Support_Beam_Broken_B21_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: Mines_Machine_Whim_Side_Support_Beam_Broken_B3 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (8199.259, 6312.0547, 2317.6052), (0.0, 0.0, -0.0), (1.3109, 0.6699, 1.6522), "DV_Mines_Machine_Whim_Side_Support_Beam_Broken_B3_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: Mines_Machine_Whim_Side_Support_Beam_Broken_C10 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (9642.719, 6893.0923, 2372.259), (0.0, 0.0, -0.0), (0.3335, 1.4926, 0.9821), "DV_Mines_Machine_Whim_Side_Support_Beam_Broken_C10_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: Mines_Machine_Whim_Side_Support_Beam_Broken_C11 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (9342.721, 6072.945, 2370.0603), (0.0, 0.0, -0.0), (0.3335, 1.5136, 0.9212), "DV_Mines_Machine_Whim_Side_Support_Beam_Broken_C11_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: Mines_Machine_Whim_Side_Support_Beam_Broken_C12 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (8742.719, 6079.3853, 2362.259), (0.0, 0.0, -0.0), (0.3335, 1.4926, 0.9821), "DV_Mines_Machine_Whim_Side_Support_Beam_Broken_C12_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: Mines_Machine_Whim_Side_Support_Beam_Broken_C3 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (8377.821, 6339.2236, 2361.6184), (0.0, 0.0, -0.0), (1.5557, 0.4982, 1.1333), "DV_Mines_Machine_Whim_Side_Support_Beam_Broken_C3_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: Mines_Machine_Whim_Side_Support_Beam_Broken_C6 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (8749.412, 7177.9263, 2364.798), (0.0, 0.0, -0.0), (0.5756, 1.4909, 1.1664), "DV_Mines_Machine_Whim_Side_Support_Beam_Broken_C6_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: Mines_Machine_Whim_Side_Support_Beam_Broken_C7 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (8233.356, 5726.26, 2364.2927), (0.0, 0.0, -0.0), (1.4575, 0.8801, 1.1333), "DV_Mines_Machine_Whim_Side_Support_Beam_Broken_C7_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: Mines_Machine_Whim_Side_Support_Beam_Broken_C8 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (8680.899, 5709.607, 2349.6973), (0.0, 0.0, -0.0), (1.4679, 0.3335, 1.0406), "DV_Mines_Machine_Whim_Side_Support_Beam_Broken_C8_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: Mines_Machine_Whim_Side_Support_Beam_Broken_C9 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (9042.719, 6899.533, 2380.0596), (0.0, 0.0, -0.0), (0.3335, 1.5136, 0.9212), "DV_Mines_Machine_Whim_Side_Support_Beam_Broken_C9_BRK", _folder)
if a: placed += 1
else: skipped += 1

# ======================================================================
# SUMMARY
# ======================================================================
unreal.log(f"[{BUBBLE_NAME}] Reconstruction complete: {placed} placed, {skipped} skipped, {errors} errors")
