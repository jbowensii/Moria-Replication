"""Auto-generated level reconstruction script.
Bubble: BD_BB_Outdoor_TradingPost
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

BUBBLE_NAME = "BD_BB_Outdoor_TradingPost"
placed = 0
skipped = 0
errors = 0

# ======================================================================
# PHASE 1: InstancedMeshCatalog  (static mesh placement)
# ======================================================================
unreal.log(f"[{BUBBLE_NAME}] Phase 1: Placing static meshes...")

# Batch 0: StaticMesh'CBP_Figurines_01' (1 instances)
_mesh_path = "/Game/Art/Assets/GPI/CBP/CBP_Figurines_01"
_materials = ['/Game/Art/Assets/GPI/CBP/Materials/CBP_Figurines/MI_CBP_Figurines_Atlas']
_folder = "Reconstruction/BD_BB_Outdoor_TradingPost/Meshes"
a = spawn_static_mesh(_mesh_path, _materials, (9788.969, 13956.086, 773.37317), (0.0, -165.54925083548574, 0.0), (1.0, 1.0, 1.0), "CBP_Figurines_01_158", _folder)
if a: placed += 1
else: skipped += 1

# Batch 1: StaticMesh'CBP_Figurines_02' (1 instances)
_mesh_path = "/Game/Art/Assets/GPI/CBP/CBP_Figurines_02"
_materials = ['/Game/Art/Assets/GPI/CBP/Materials/CBP_Figurines/MI_CBP_Figurines_Atlas']
_folder = "Reconstruction/BD_BB_Outdoor_TradingPost/Meshes"
a = spawn_static_mesh(_mesh_path, _materials, (9743.379, 13918.167, 773.37317), (0.0, -165.54939149377557, 0.0), (1.0, 1.0, 1.0), "CBP_Figurines_02_155", _folder)
if a: placed += 1
else: skipped += 1

# Batch 2: StaticMesh'CBP_Figurines_04' (1 instances)
_mesh_path = "/Game/Art/Assets/GPI/CBP/CBP_Figurines_04"
_materials = ['/Game/Art/Assets/GPI/CBP/Materials/CBP_Figurines/MI_CBP_Figurines_Atlas']
_folder = "Reconstruction/BD_BB_Outdoor_TradingPost/Meshes"
a = spawn_static_mesh(_mesh_path, _materials, (9819.42, 13964.68, 766.05566), (0.0, -165.54939149377557, 0.0), (1.0, 1.0, 1.0), "CBP_Figurines_152", _folder)
if a: placed += 1
else: skipped += 1

# Batch 3: StaticMesh'CBP_Figurines_06' (1 instances)
_mesh_path = "/Game/Art/Assets/GPI/CBP/CBP_Figurines_06"
_materials = ['/Game/Art/Assets/GPI/CBP/Materials/CBP_Figurines/MI_CBP_Figurines_Atlas']
_folder = "Reconstruction/BD_BB_Outdoor_TradingPost/Meshes"
a = spawn_static_mesh(_mesh_path, _materials, (9146.579, 17772.12, 416.0556), (0.0, 165.0000041053679, -0.0), (1.0, 1.0, 1.0), "CBP_Figurines_149", _folder)
if a: placed += 1
else: skipped += 1

# Batch 4: StaticMesh'CBP_Figurines_07' (1 instances)
_mesh_path = "/Game/Art/Assets/GPI/CBP/CBP_Figurines_07"
_materials = ['/Game/Art/Assets/GPI/CBP/Materials/CBP_Figurines/MI_CBP_Figurines_Atlas']
_folder = "Reconstruction/BD_BB_Outdoor_TradingPost/Meshes"
a = spawn_static_mesh(_mesh_path, _materials, (9700.373, 13936.049, 766.05566), (0.0, -170.54942839404805, 0.0), (1.0, 1.0, 1.0), "CBP_Figurines_07_161", _folder)
if a: placed += 1
else: skipped += 1

# Batch 5: StaticMesh'GPI_Dwarf_Memorial_D' (1 instances)
_mesh_path = "/Game/Art/Assets/GPI/CBP/GPI_Dwarf_Memorial_D"
_materials = ['/Game/Art/Assets/GPI/CBP/Materials/GPI_Dwarf_Memorial/MI_GPI_Dwarf_Memorial_D']
_folder = "Reconstruction/BD_BB_Outdoor_TradingPost/Meshes"
a = spawn_static_mesh(_mesh_path, _materials, (9755.4795, 13951.357, 766.05566), (0.0, -147.1534094111654, 0.0), (1.0, 1.0, 1.0), "GPI_Dwarf_Memorial_B_143", _folder)
if a: placed += 1
else: skipped += 1

# Batch 6: StaticMesh'chest2' (2 instances)
_mesh_path = "/Game/Art/Assets/GPI/chest2"
_materials = ['/Game/Art/Assets/GPI/Material/Chest2/chest']
_folder = "Reconstruction/BD_BB_Outdoor_TradingPost/Meshes"
a = spawn_static_mesh(_mesh_path, _materials, (11441.58, 9341.518, 600.76416), (0.0, 169.99994341244798, -0.0), (1.0, 1.0, 1.0), "chest2_40", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (10874.388, 10833.788, 654.9523), (-0.9746399610765744, -22.796539505479338, -2.3172608220231723), (1.0, 1.0, 1.0), "chest3", _folder)
if a: placed += 1
else: skipped += 1

# Batch 7: StaticMesh'chestCap2' (2 instances)
_mesh_path = "/Game/Art/Assets/GPI/chestCap2"
_materials = ['/Game/Art/Assets/GPI/Material/Chest2/chest']
_folder = "Reconstruction/BD_BB_Outdoor_TradingPost/Meshes"
a = spawn_static_mesh(_mesh_path, _materials, (11436.339, 9311.808, 652.2596), (0.0, 169.99994341244798, -0.0), (1.0, 1.0, 1.0), "chestCap2_37", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (10886.087, 10859.3125, 707.61774), (-0.9746399610765744, -22.796539505479338, -2.3172608220231723), (1.0, 1.0, 1.0), "chestCap3", _folder)
if a: placed += 1
else: skipped += 1

# Batch 8: StaticMesh'Bottles_medicinal_decoction_1_SM' (1 instances)
_mesh_path = "/Game/Art/Assets/GPI/FoodStoreroom/Meshes/Bottles_medicinal_decoction_1_SM"
_materials = ['/Game/Art/Assets/GPI/FoodStoreroom/Materials/Bottle_M']
_folder = "Reconstruction/BD_BB_Outdoor_TradingPost/Meshes"
a = spawn_static_mesh(_mesh_path, _materials, (11587.482, 10085.062, 743.6489), (0.0, 0.0, -0.0), (1.0, 1.0, 1.0), "Bottles_medicinal_decoction_1_SM_506", _folder)
if a: placed += 1
else: skipped += 1

# Batch 9: StaticMesh'Bottles_salve_SM' (1 instances)
_mesh_path = "/Game/Art/Assets/GPI/FoodStoreroom/Meshes/Bottles_salve_SM"
_materials = ['/Game/Art/Assets/GPI/FoodStoreroom/Materials/Salve_M']
_folder = "Reconstruction/BD_BB_Outdoor_TradingPost/Meshes"
a = spawn_static_mesh(_mesh_path, _materials, (11591.705, 9974.188, 692.1964), (0.0, 0.0, -0.0), (1.0, 1.0, 1.0), "Bottles_salve_SM_503", _folder)
if a: placed += 1
else: skipped += 1

# Batch 10: StaticMesh'GPI_Gem_Emerald' (1 instances)
_mesh_path = "/Game/Art/Assets/GPI/Gems_Stone/GPI_Gem_Emerald"
_materials = ['/Game/Art/Assets/GPI/Gems_Stone/Material/GPI_Gems_Mat']
_folder = "Reconstruction/BD_BB_Outdoor_TradingPost/Meshes"
a = spawn_static_mesh(_mesh_path, _materials, (9247.337, 17737.28, 351.6803), (45.00001482325226, -100.00005704527388, 1.4077714061940118e-06), (1.0, 1.0, 1.0), "GPI_Gem_Emerald_173", _folder)
if a: placed += 1
else: skipped += 1

# Batch 11: StaticMesh'SM_Bale2' (3 instances)
_mesh_path = "/Game/Art/Assets/GPI/Props/Meshes/Props/SM_Bale2"
_materials = ['/Game/Art/Assets/GPI/Props/Material_Instances/MI_Bale2']
_folder = "Reconstruction/BD_BB_Outdoor_TradingPost/Meshes"
a = spawn_static_mesh(_mesh_path, _materials, (4765.2236, 5591.883, 349.07892), (0.0, 15.000036446857495, -0.0), (1.0, 1.0, 1.0), "SM_Bale2_721", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5297.709, 5291.74, 334.69946), (0.0, 79.99995877012579, -0.0), (1.0, 1.0, 1.0), "SM_Bale3_724", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4804.594, 5115.3433, 347.38586), (0.0, -34.99999947832233, 0.0), (1.0, 1.0, 1.0), "SM_Bale4_727", _folder)
if a: placed += 1
else: skipped += 1

# Batch 12: StaticMesh'City_Gate_Base' (8 instances)
_mesh_path = "/Game/Art/Assets/Kits/Architecture/City/City_Gate_Base"
_materials = ['/Game/Art/Assets/Kits/Architecture/Outdoors/MI_City_Gate_Base_RedRock']
_folder = "Reconstruction/BD_BB_Outdoor_TradingPost/Meshes"
a = spawn_static_mesh(_mesh_path, _materials, (10100.0, 10040.0, 600.0), (0.0, -179.99994535848643, 0.0), (1.4140433, 1.0, 1.0), "City_Gate_Capitol_Top_1309", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (10100.0, 9140.0, 600.0), (0.0, -179.99994535848643, 0.0), (1.414043, 1.0, 1.0), "City_Gate_Capitol_Top2_1321", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (6503.089, 8558.767, 156.63953), (0.0, 39.99975776193207, -0.0), (1.414043, 1.0, 1.0), "City_Gate_Capitol_Top3", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5924.583, 9248.212, 156.63953), (0.0, 39.99975776193207, -0.0), (1.414043, 1.0, 1.0), "City_Gate_Capitol_Top4", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4028.5996, 5932.5874, 156.64124), (0.0, 14.049041432108973, -0.0), (1.414043, 1.0, 1.0), "City_Gate_Capitol_Top5", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3810.1265, 6805.668, 156.64124), (0.0, 14.049135536307602, -0.0), (1.414043, 1.0, 1.0), "City_Gate_Capitol_Top6", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2921.8826, 5664.081, 386.57452), (0.0, 9.808703714511733, -0.0), (1.414043, 1.0, 1.0), "City_Gate_Capitol_Top7", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2768.5642, 6550.9272, 386.57452), (0.0, 9.808874599270686, -0.0), (1.414043, 1.0, 1.0), "City_Gate_Capitol_Top8", _folder)
if a: placed += 1
else: skipped += 1

# Batch 13: StaticMesh'City_Gate_X_Column_A' (8 instances)
_mesh_path = "/Game/Art/Assets/Kits/Architecture/City/City_Gate_X_Column_A"
_materials = ['/Game/Art/Assets/Kits/Architecture/Outdoors/MI_Outdoors_Trim_Sheet_A', '/Game/Art/Assets/Kits/Architecture/Suburbs/Materials/Suburbs_Trim_Sheet_B/MI_Suburbs_Trim_Sheet_B_Gold']
_folder = "Reconstruction/BD_BB_Outdoor_TradingPost/Meshes"
a = spawn_static_mesh(_mesh_path, _materials, (10000.0, 10040.0, 1650.0), (-2.6337494720381325e-18, -3.0517577092894745e-05, 179.99976777355934), (0.5, 0.5, 0.5), "City_Gate_X_Column_A_50", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (10000.0, 9140.0, 1650.0), (-2.6337494720381325e-18, -3.0517577092894745e-05, 179.99976777355934), (0.5, 0.5, 0.5), "City_Gate_X_Column_A2", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (6579.695, 8623.049, 1206.6394), (4.907047565594288e-15, -140.0001238728725, 179.99976777357358), (0.5, 0.5, 0.5), "City_Gate_X_Column_A3", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (6001.1875, 9312.489, 1206.6394), (4.907047565594288e-15, -140.0001238728725, 179.99976777357358), (0.5, 0.5, 0.5), "City_Gate_X_Column_A4", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4125.6133, 5956.8643, 1206.6411), (1.009794189827775e-12, -165.9507190652455, 179.99976777353103), (0.5, 0.5, 0.5), "City_Gate_X_Column_A5", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3907.1355, 6829.9434, 1206.6411), (7.372894262784089e-13, -165.95043921009585, 179.99976777354934), (0.5, 0.5, 0.5), "City_Gate_X_Column_A6", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3020.426, 5681.118, 1436.575), (1.3307875282917392e-12, -170.19088048682454, 179.9997677735092), (0.5, 0.5, 0.5), "City_Gate_X_Column_A7", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2867.101, 6567.9634, 1436.575), (2.863597909909333e-12, -170.19073693338316, 179.9997677735124), (0.5, 0.5, 0.5), "City_Gate_X_Column_A8", _folder)
if a: placed += 1
else: skipped += 1

# Batch 14: StaticMesh'City_Pillar_Base_B' (16 instances)
_mesh_path = "/Game/Art/Assets/Kits/Architecture/City/City_Pillar_Base_B"
_materials = ['/Game/Art/Assets/Kits/Architecture/Outdoors/MI_City_Gate_Base_RedRock']
_folder = "Reconstruction/BD_BB_Outdoor_TradingPost/Meshes"
a = spawn_static_mesh(_mesh_path, _materials, (10000.0, 10040.0, 600.0), (0.0, -90.0001164887758, 0.0), (1.0, 1.0, 1.0), "City_Pillar_Base_B_58", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4125.6133, 5956.8643, 156.64124), (0.0, -75.95114357251583, 0.0), (1.0, 1.0, 1.0), "City_Pillar_Base_B10", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3907.1355, 6829.9434, 156.64124), (0.0, 104.04913217878754, -0.0), (1.0, 1.0, 1.0), "City_Pillar_Base_B11", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3907.1355, 6829.9434, 156.64124), (0.0, -75.95108272491488, 0.0), (1.0, 1.0, 1.0), "City_Pillar_Base_B12", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3020.426, 5681.118, 386.57452), (0.0, 99.80853042747447, -0.0), (1.0, 1.0, 1.0), "City_Pillar_Base_B13", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3020.426, 5681.118, 386.57452), (0.0, -80.19153163935577, 0.0), (1.0, 1.0, 1.0), "City_Pillar_Base_B14", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2867.101, 6567.9634, 386.57452), (0.0, 99.80887757794147, -0.0), (1.0, 1.0, 1.0), "City_Pillar_Base_B15", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2867.101, 6567.9634, 386.57452), (0.0, -80.19150207699694, 0.0), (1.0, 1.0, 1.0), "City_Pillar_Base_B16", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (10000.0, 10040.0, 600.0), (0.0, 89.999630318475, -0.0), (1.0, 1.0, 1.0), "City_Pillar_Base_B2", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (10000.0, 9140.0, 600.0), (0.0, -90.0001164887758, 0.0), (1.0, 1.0, 1.0), "City_Pillar_Base_B3", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (10000.0, 9140.0, 600.0), (0.0, 89.999630318475, -0.0), (1.0, 1.0, 1.0), "City_Pillar_Base_B4", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (6579.695, 8623.049, 156.63953), (0.0, 129.99971279054114, -0.0), (1.0, 1.0, 1.0), "City_Pillar_Base_B5", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (6579.695, 8623.049, 156.63953), (0.0, -50.00055027936202, 0.0), (1.0, 1.0, 1.0), "City_Pillar_Base_B6", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (6001.1875, 9312.489, 156.63953), (0.0, 129.99971279054114, -0.0), (1.0, 1.0, 1.0), "City_Pillar_Base_B7", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (6001.1875, 9312.489, 156.63953), (0.0, -50.00055027936202, 0.0), (1.0, 1.0, 1.0), "City_Pillar_Base_B8", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4125.6133, 5956.8643, 156.64124), (0.0, 104.04888703587362, -0.0), (1.0, 1.0, 1.0), "City_Pillar_Base_B9", _folder)
if a: placed += 1
else: skipped += 1

# Batch 15: StaticMesh'City_Pillar_Capitol_Base_B' (16 instances)
_mesh_path = "/Game/Art/Assets/Kits/Architecture/City/City_Pillar_Capitol_Base_B"
_materials = ['/Game/Art/Assets/Kits/Architecture/City/Materials/CityGate/MI_City_Pillar_Capitol_Base_RedRock']
_folder = "Reconstruction/BD_BB_Outdoor_TradingPost/Meshes"
a = spawn_static_mesh(_mesh_path, _materials, (6579.695, 8623.049, 1206.6394), (0.0, -49.99987822834905, 0.0), (0.87987, 0.87987, 0.87987), "City_Pillar_Capitol_Base_B10", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3907.1355, 6829.9434, 1206.6411), (0.0, -75.95068533344725, 0.0), (0.87987, 0.87987, 0.87987), "City_Pillar_Capitol_Base_B11", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3907.1355, 6829.9434, 1206.6411), (0.0, 104.04925448472603, -0.0), (0.87987, 0.87987, 0.87987), "City_Pillar_Capitol_Base_B12", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4125.6133, 5956.8643, 1206.6411), (0.0, 104.04906762060266, -0.0), (0.87987, 0.87987, 0.87987), "City_Pillar_Capitol_Base_B13", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4125.6133, 5956.8643, 1206.6411), (0.0, -75.9504377425492, 0.0), (0.87987, 0.87987, 0.87987), "City_Pillar_Capitol_Base_B14", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2867.101, 6567.9634, 1436.575), (0.0, -80.19091744006792, 0.0), (0.87987, 0.87987, 0.87987), "City_Pillar_Capitol_Base_B15", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2867.101, 6567.9634, 1436.575), (0.0, 99.8089486697179, -0.0), (0.87987, 0.87987, 0.87987), "City_Pillar_Capitol_Base_B16", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3020.426, 5681.118, 1436.575), (0.0, 99.80879597925471, -0.0), (0.87987, 0.87987, 0.87987), "City_Pillar_Capitol_Base_B17", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3020.426, 5681.118, 1436.575), (0.0, -80.19079164438456, 0.0), (0.87987, 0.87987, 0.87987), "City_Pillar_Capitol_Base_B18", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (10000.0, 9140.0, 1650.0), (0.0, 89.99984099200987, -0.0), (0.8798696, 0.8798696, 0.8798696), "City_Pillar_Capitol_Base_B3", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (10000.0, 9140.0, 1650.0), (0.0, -89.99984099200987, 0.0), (0.8798696, 0.8798696, 0.8798696), "City_Pillar_Capitol_Base_B4", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (10000.0, 10040.0, 1650.0), (0.0, -89.99993822608693, 0.0), (0.87987, 0.87987, 0.87987), "City_Pillar_Capitol_Base_B5", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (10000.0, 10040.0, 1650.0), (0.0, 90.0002623402507, -0.0), (0.87987, 0.87987, 0.87987), "City_Pillar_Capitol_Base_B6", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (6001.1875, 9312.489, 1206.6394), (0.0, -50.0003336757968, 0.0), (0.87987, 0.87987, 0.87987), "City_Pillar_Capitol_Base_B7", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (6001.1875, 9312.489, 1206.6394), (0.0, 130.00002191720526, -0.0), (0.87987, 0.87987, 0.87987), "City_Pillar_Capitol_Base_B8", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (6579.695, 8623.049, 1206.6394), (0.0, 129.99986568490058, -0.0), (0.87987, 0.87987, 0.87987), "City_Pillar_Capitol_Base_B9", _folder)
if a: placed += 1
else: skipped += 1

# Batch 16: StaticMesh'City_Pillar_Capitol_Top_Half_L_B' (32 instances)
_mesh_path = "/Game/Art/Assets/Kits/Architecture/City/City_Pillar_Capitol_Top_Half_L_B"
_materials = ['/Game/Art/Assets/Kits/Architecture/Outdoors/MI_City_Gate_Capitol_Top_RedRock']
_folder = "Reconstruction/BD_BB_Outdoor_TradingPost/Meshes"
a = spawn_static_mesh(_mesh_path, _materials, (10000.0, 10040.0, 1500.0), (0.0, 90.00009542133918, -0.0), (0.8, 0.8, 0.8), "City_Pillar_Capitol_Top_B11", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (10000.0, 9140.0, 1500.0), (0.0, 179.99971996224815, -0.0), (0.8, 0.8, 0.8), "City_Pillar_Capitol_Top_B13", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (10000.0, 9140.0, 1500.0), (0.0, -90.0001164887758, 0.0), (0.8, 0.8, 0.8), "City_Pillar_Capitol_Top_B15", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (10000.0, 9140.0, 1500.0), (0.0, -3.051757709276941e-05, 0.0), (0.8, 0.8, 0.8), "City_Pillar_Capitol_Top_B17", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (10000.0, 9140.0, 1500.0), (0.0, 90.00009542133918, -0.0), (0.8, 0.8, 0.8), "City_Pillar_Capitol_Top_B19", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (6579.695, 8623.049, 1056.6394), (0.0, 39.99944938683695, -0.0), (0.8, 0.8, 0.8), "City_Pillar_Capitol_Top_B21", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (6579.695, 8623.049, 1056.6394), (0.0, 129.9996196543403, -0.0), (0.8, 0.8, 0.8), "City_Pillar_Capitol_Top_B23", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (6579.695, 8623.049, 1056.6394), (0.0, -140.0000576472962, 0.0), (0.8, 0.8, 0.8), "City_Pillar_Capitol_Top_B25", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (6579.695, 8623.049, 1056.6394), (0.0, -50.00003087412388, 0.0), (0.8, 0.8, 0.8), "City_Pillar_Capitol_Top_B27", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (6001.1875, 9312.489, 1056.6394), (0.0, 39.99944938683695, -0.0), (0.8, 0.8, 0.8), "City_Pillar_Capitol_Top_B29", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (6001.1875, 9312.489, 1056.6394), (0.0, 129.9996196543403, -0.0), (0.8, 0.8, 0.8), "City_Pillar_Capitol_Top_B31", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (6001.1875, 9312.489, 1056.6394), (0.0, -140.0000576472962, 0.0), (0.8, 0.8, 0.8), "City_Pillar_Capitol_Top_B33", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (6001.1875, 9312.489, 1056.6394), (0.0, -50.00003087412388, 0.0), (0.8, 0.8, 0.8), "City_Pillar_Capitol_Top_B35", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4125.6133, 5956.8643, 1056.6411), (0.0, 14.048666186834641, -0.0), (0.8, 0.8, 0.8), "City_Pillar_Capitol_Top_B37", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4125.6133, 5956.8643, 1056.6411), (0.0, 104.04874114898237, -0.0), (0.8, 0.8, 0.8), "City_Pillar_Capitol_Top_B39", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4125.6133, 5956.8643, 1056.6411), (0.0, -165.95043921003872, 0.0), (0.8, 0.8, 0.8), "City_Pillar_Capitol_Top_B41", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4125.6133, 5956.8643, 1056.6411), (0.0, -75.95050244912373, 0.0), (0.8, 0.8, 0.8), "City_Pillar_Capitol_Top_B43", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3907.1355, 6829.9434, 1056.6411), (0.0, 14.048839167777825, -0.0), (0.8, 0.8, 0.8), "City_Pillar_Capitol_Top_B45", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3907.1355, 6829.9434, 1056.6411), (0.0, 104.04906762060266, -0.0), (0.8, 0.8, 0.8), "City_Pillar_Capitol_Top_B47", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3907.1355, 6829.9434, 1056.6411), (0.0, -165.95043921003872, 0.0), (0.8, 0.8, 0.8), "City_Pillar_Capitol_Top_B49", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (10000.0, 10040.0, 1500.0), (0.0, 179.99971996224815, -0.0), (0.8, 0.8, 0.8), "City_Pillar_Capitol_Top_B5", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3907.1355, 6829.9434, 1056.6411), (0.0, -75.9504377425492, 0.0), (0.8, 0.8, 0.8), "City_Pillar_Capitol_Top_B51", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3020.426, 5681.118, 1286.575), (0.0, 9.808402141924518, -0.0), (0.8, 0.8, 0.8), "City_Pillar_Capitol_Top_B53", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3020.426, 5681.118, 1286.575), (0.0, 99.80835221689583, -0.0), (0.8, 0.8, 0.8), "City_Pillar_Capitol_Top_B55", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3020.426, 5681.118, 1286.575), (0.0, -170.19073693334306, 0.0), (0.8, 0.8, 0.8), "City_Pillar_Capitol_Top_B57", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3020.426, 5681.118, 1286.575), (0.0, -80.19079164438456, 0.0), (0.8, 0.8, 0.8), "City_Pillar_Capitol_Top_B59", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2867.101, 6567.9634, 1286.575), (0.0, 9.808577254797727, -0.0), (0.8, 0.8, 0.8), "City_Pillar_Capitol_Top_B61", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2867.101, 6567.9634, 1286.575), (0.0, 99.80874344450011, -0.0), (0.8, 0.8, 0.8), "City_Pillar_Capitol_Top_B63", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2867.101, 6567.9634, 1286.575), (0.0, -170.19073693334306, 0.0), (0.8, 0.8, 0.8), "City_Pillar_Capitol_Top_B65", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2867.101, 6567.9634, 1286.575), (0.0, -80.19081724441502, 0.0), (0.8, 0.8, 0.8), "City_Pillar_Capitol_Top_B67", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (10000.0, 10040.0, 1500.0), (0.0, -90.0001164887758, 0.0), (0.8, 0.8, 0.8), "City_Pillar_Capitol_Top_B7", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (10000.0, 10040.0, 1500.0), (0.0, -3.051757709276941e-05, 0.0), (0.8, 0.8, 0.8), "City_Pillar_Capitol_Top_B9", _folder)
if a: placed += 1
else: skipped += 1

# Batch 17: StaticMesh'City_Pillar_Capitol_Top_Half_R_B' (32 instances)
_mesh_path = "/Game/Art/Assets/Kits/Architecture/City/City_Pillar_Capitol_Top_Half_R_B"
_materials = ['/Game/Art/Assets/Kits/Architecture/Outdoors/MI_City_Gate_Capitol_Top_RedRock']
_folder = "Reconstruction/BD_BB_Outdoor_TradingPost/Meshes"
a = spawn_static_mesh(_mesh_path, _materials, (10000.0, 10040.0, 1500.0), (0.0, 0.0, -0.0), (0.8, 0.8, 0.8), "City_Pillar_Capitol_Top_B10", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (10000.0, 10040.0, 1500.0), (0.0, 90.00009542133918, -0.0), (0.8, 0.8, 0.8), "City_Pillar_Capitol_Top_B12", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (10000.0, 9140.0, 1500.0), (0.0, 179.99971996224815, -0.0), (0.8, 0.8, 0.8), "City_Pillar_Capitol_Top_B14", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (10000.0, 9140.0, 1500.0), (0.0, -90.00009542133918, 0.0), (0.8, 0.8, 0.8), "City_Pillar_Capitol_Top_B16", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (10000.0, 9140.0, 1500.0), (0.0, 0.0, -0.0), (0.8, 0.8, 0.8), "City_Pillar_Capitol_Top_B18", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (10000.0, 9140.0, 1500.0), (0.0, 90.00009542133918, -0.0), (0.8, 0.8, 0.8), "City_Pillar_Capitol_Top_B20", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (6579.695, 8623.049, 1056.6394), (0.0, 39.99948933190447, -0.0), (0.8, 0.8, 0.8), "City_Pillar_Capitol_Top_B22", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (6579.695, 8623.049, 1056.6394), (0.0, 129.99966349691883, -0.0), (0.8, 0.8, 0.8), "City_Pillar_Capitol_Top_B24", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (6579.695, 8623.049, 1056.6394), (0.0, -140.0000576472962, 0.0), (0.8, 0.8, 0.8), "City_Pillar_Capitol_Top_B26", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (6579.695, 8623.049, 1056.6394), (0.0, -50.000000322548, 0.0), (0.8, 0.8, 0.8), "City_Pillar_Capitol_Top_B28", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (6001.1875, 9312.489, 1056.6394), (0.0, 39.99948933190447, -0.0), (0.8, 0.8, 0.8), "City_Pillar_Capitol_Top_B30", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (6001.1875, 9312.489, 1056.6394), (0.0, 129.99966349691883, -0.0), (0.8, 0.8, 0.8), "City_Pillar_Capitol_Top_B32", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (6001.1875, 9312.489, 1056.6394), (0.0, -140.0000576472962, 0.0), (0.8, 0.8, 0.8), "City_Pillar_Capitol_Top_B34", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (6001.1875, 9312.489, 1056.6394), (0.0, -50.000000322548, 0.0), (0.8, 0.8, 0.8), "City_Pillar_Capitol_Top_B36", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4125.6133, 5956.8643, 1056.6411), (0.0, 14.048787995099504, -0.0), (0.8, 0.8, 0.8), "City_Pillar_Capitol_Top_B38", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4125.6133, 5956.8643, 1056.6411), (0.0, 104.04894215210558, -0.0), (0.8, 0.8, 0.8), "City_Pillar_Capitol_Top_B40", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4125.6133, 5956.8643, 1056.6411), (0.0, -165.95057801920726, 0.0), (0.8, 0.8, 0.8), "City_Pillar_Capitol_Top_B42", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4125.6133, 5956.8643, 1056.6411), (0.0, -75.95056398110246, 0.0), (0.8, 0.8, 0.8), "City_Pillar_Capitol_Top_B44", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3907.1355, 6829.9434, 1056.6411), (0.0, 14.048894712015919, -0.0), (0.8, 0.8, 0.8), "City_Pillar_Capitol_Top_B46", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3907.1355, 6829.9434, 1056.6411), (0.0, 104.04902941456307, -0.0), (0.8, 0.8, 0.8), "City_Pillar_Capitol_Top_B48", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3907.1355, 6829.9434, 1056.6411), (0.0, -165.95043921003872, 0.0), (0.8, 0.8, 0.8), "City_Pillar_Capitol_Top_B50", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3907.1355, 6829.9434, 1056.6411), (0.0, -75.9504377425492, 0.0), (0.8, 0.8, 0.8), "City_Pillar_Capitol_Top_B52", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3020.426, 5681.118, 1286.575), (0.0, 9.80852918080424, -0.0), (0.8, 0.8, 0.8), "City_Pillar_Capitol_Top_B54", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3020.426, 5681.118, 1286.575), (0.0, 99.8086815157684, -0.0), (0.8, 0.8, 0.8), "City_Pillar_Capitol_Top_B56", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3020.426, 5681.118, 1286.575), (0.0, -170.19088048678444, 0.0), (0.8, 0.8, 0.8), "City_Pillar_Capitol_Top_B58", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (10000.0, 10040.0, 1500.0), (0.0, 179.99971996224815, -0.0), (0.8, 0.8, 0.8), "City_Pillar_Capitol_Top_B6", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3020.426, 5681.118, 1286.575), (0.0, -80.19091744006792, 0.0), (0.8, 0.8, 0.8), "City_Pillar_Capitol_Top_B60", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2867.101, 6567.9634, 1286.575), (0.0, 9.808635754478829, -0.0), (0.8, 0.8, 0.8), "City_Pillar_Capitol_Top_B62", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2867.101, 6567.9634, 1286.575), (0.0, 99.80874344450011, -0.0), (0.8, 0.8, 0.8), "City_Pillar_Capitol_Top_B64", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2867.101, 6567.9634, 1286.575), (0.0, -170.19073693334306, 0.0), (0.8, 0.8, 0.8), "City_Pillar_Capitol_Top_B66", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2867.101, 6567.9634, 1286.575), (0.0, -80.19081724441502, 0.0), (0.8, 0.8, 0.8), "City_Pillar_Capitol_Top_B68", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (10000.0, 10040.0, 1500.0), (0.0, -90.00009542133918, 0.0), (0.8, 0.8, 0.8), "City_Pillar_Capitol_Top_B8", _folder)
if a: placed += 1
else: skipped += 1

# Batch 18: StaticMesh'NonD_Arch_Half_3m_C' (8 instances)
_mesh_path = "/Game/Art/Assets/Kits/Architecture/Non_D/NonD_Arch_Half_3m_C"
_materials = ['/Game/Art/Assets/Kits/Architecture/Outdoors/MI_Outdoors_Trim_Sheet_A']
_folder = "Reconstruction/BD_BB_Outdoor_TradingPost/Meshes"
a = spawn_static_mesh(_mesh_path, _materials, (6126.5576, 8473.438, -50.0), (0.0, -138.56250075143797, 0.0), (1.0, 1.0, 1.0), "Suburbs_Wall_Thin_Arch_Half_1m_C_306", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (6126.5576, 8473.438, -350.0), (0.0, -138.56250075143797, 0.0), (1.0, 1.0, 1.0), "Suburbs_Wall_Thin_Arch_Half_1m_C2", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5751.7188, 8142.5376, -50.0), (0.0, 41.43759947977455, -0.0), (1.0, 1.0, 1.0), "Suburbs_Wall_Thin_Arch_Half_1m_C3", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5751.7188, 8142.5376, -350.0), (0.0, 41.43759947977455, -0.0), (1.0, 1.0, 1.0), "Suburbs_Wall_Thin_Arch_Half_1m_C4", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5795.655, 8848.277, -50.0), (0.0, -138.56250075143797, 0.0), (1.0, 1.0, 1.0), "Suburbs_Wall_Thin_Arch_Half_1m_C5", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5795.655, 8848.277, -350.0), (0.0, -138.56250075143797, 0.0), (1.0, 1.0, 1.0), "Suburbs_Wall_Thin_Arch_Half_1m_C6", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5420.816, 8517.377, -50.0), (0.0, 41.43759947977455, -0.0), (1.0, 1.0, 1.0), "Suburbs_Wall_Thin_Arch_Half_1m_C7", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5420.816, 8517.377, -350.0), (0.0, 41.43759947977455, -0.0), (1.0, 1.0, 1.0), "Suburbs_Wall_Thin_Arch_Half_1m_C8", _folder)
if a: placed += 1
else: skipped += 1

# Batch 19: StaticMesh'NonD_Arch_Half_A' (4 instances)
_mesh_path = "/Game/Art/Assets/Kits/Architecture/Non_D/NonD_Arch_Half_A"
_materials = ['/Game/Art/Assets/Kits/Architecture/Outdoors/MI_Outdoors_Trim_Sheet_A']
_folder = "Reconstruction/BD_BB_Outdoor_TradingPost/Meshes"
a = spawn_static_mesh(_mesh_path, _materials, (6126.5576, 8473.438, 250.0), (0.0, -138.56250075143797, 0.0), (1.0, 1.0, 1.0), "NonD_Arch_Half_A_49", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5795.6553, 8848.28, 250.0), (0.0, -138.56250075143797, 0.0), (1.0, 1.0, 1.0), "NonD_Arch_Half_A2_60", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5420.813, 8517.381, 250.0), (0.0, 41.43737563967661, -0.0), (1.0, 1.0, 1.0), "NonD_Arch_Half_A3_63", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5751.7153, 8142.5396, 250.0), (0.0, 41.43737563967661, -0.0), (1.0, 1.0, 1.0), "NonD_Arch_Half_A4_64", _folder)
if a: placed += 1
else: skipped += 1

# Batch 20: StaticMesh'NonD_Stairs_Trim_D' (2 instances)
_mesh_path = "/Game/Art/Assets/Kits/Architecture/Non_D/NonD_Stairs_Trim_D"
_materials = ['/Game/Art/Assets/Kits/Architecture/Outdoors/MI_Outdoors_Trim_Sheet_A']
_folder = "Reconstruction/BD_BB_Outdoor_TradingPost/Meshes"
a = spawn_static_mesh(_mesh_path, _materials, (6193.8213, 8472.792, 500.0), (0.0, 41.43748713135065, -0.0), (1.0, 1.0, 1.0), "NonD_Stairs_Trim_E_121", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5803.358, 8915.104, 500.0), (0.0, 41.43748713135065, -0.0), (1.0, 1.0, 1.0), "NonD_Stairs_Trim_E2", _folder)
if a: placed += 1
else: skipped += 1

# Batch 21: StaticMesh'NonD_Stairs_Trim_E' (2 instances)
_mesh_path = "/Game/Art/Assets/Kits/Architecture/Non_D/NonD_Stairs_Trim_E"
_materials = ['/Game/Art/Assets/Kits/Architecture/Outdoors/MI_Outdoors_Trim_Sheet_A']
_folder = "Reconstruction/BD_BB_Outdoor_TradingPost/Meshes"
a = spawn_static_mesh(_mesh_path, _materials, (12250.0, 9300.0, 550.0), (0.0, 179.99991120752276, -0.0), (1.0, 1.0, 1.0), "NonD_Stairs_Trim_E3_322", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (12250.0, 9900.0, 550.0), (0.0, 179.99991120752276, -0.0), (1.0, 1.0, 1.0), "NonD_Stairs_Trim_E4", _folder)
if a: placed += 1
else: skipped += 1

# Batch 22: StaticMesh'NonDest_Boundry_3m_Ledge_B' (13 instances)
_mesh_path = "/Game/Art/Assets/Kits/Architecture/Non_D/NonDest_Boundry_3m_Ledge_B"
_materials = ['/Game/Art/Assets/Kits/Architecture/Outdoors/MI_Outdoors_Trim_Sheet_A']
_folder = "Reconstruction/BD_BB_Outdoor_TradingPost/Meshes"
a = spawn_static_mesh(_mesh_path, _materials, (6414.919, 9062.402, 355.0), (0.0, -48.56256091827546, 0.0), (1.0, 1.0, 1.0), "NonDest_Boundry_3m_Ledge_B_167", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4096.7554, 5906.447, 400.0), (0.0, -80.12580128149156, 0.0), (1.0, 1.0, 1.0), "NonDest_Boundry_3m_Ledge_B15_1509", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4045.31, 6202.0024, 400.0), (0.0, -80.12580128149156, 0.0), (1.0, 1.0, 1.0), "NonDest_Boundry_3m_Ledge_B16", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3993.8645, 6497.558, 400.0), (0.0, -80.12580128149156, 0.0), (1.0, 1.0, 1.0), "NonDest_Boundry_3m_Ledge_B17", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2732.4578, 5871.98, 400.0), (0.0, -80.12580128149156, 0.0), (1.0, 1.0, 1.0), "NonDest_Boundry_3m_Ledge_B18", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2681.0125, 6167.5356, 400.0), (0.0, -80.12580128149156, 0.0), (1.0, 1.0, 1.0), "NonDest_Boundry_3m_Ledge_B19", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (6613.461, 8837.496, 355.0), (0.0, -48.56256091827546, 0.0), (1.0, 1.0, 1.0), "NonDest_Boundry_3m_Ledge_B2", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2629.567, 6463.0913, 400.0), (0.0, -80.12580128149156, 0.0), (1.0, 1.0, 1.0), "NonDest_Boundry_3m_Ledge_B20", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2783.903, 5576.4243, 400.0), (0.0, -80.12580128149156, 0.0), (1.0, 1.0, 1.0), "NonDest_Boundry_3m_Ledge_B21", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5965.1123, 8665.321, 555.0), (0.0, -48.56256091827546, 0.0), (1.0, 1.0, 1.0), "NonDest_Boundry_3m_Ledge_B3", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (6163.6543, 8440.415, 555.0), (0.0, -48.56256091827546, 0.0), (1.0, 1.0, 1.0), "NonDest_Boundry_3m_Ledge_B4", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5102.9824, 7904.2466, 555.0), (0.0, -48.56256091827546, 0.0), (1.0, 1.0, 1.0), "NonDest_Boundry_3m_Ledge_B5", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5301.5244, 7679.3403, 555.0), (0.0, -48.56256091827546, 0.0), (1.0, 1.0, 1.0), "NonDest_Boundry_3m_Ledge_B6", _folder)
if a: placed += 1
else: skipped += 1

# Batch 23: StaticMesh'NonDest_Boundry_3m_Ledge_B' (8 instances)
_mesh_path = "/Game/Art/Assets/Kits/Architecture/Non_D/NonDest_Boundry_3m_Ledge_B"
_materials = ['/Game/Art/Assets/Kits/Architecture/Suburbs/Materials/Suburbs_Trim_Sheet_A/MI_Suburbs_Trim_Sheet_A_Red']
_folder = "Reconstruction/BD_BB_Outdoor_TradingPost/Meshes"
a = spawn_static_mesh(_mesh_path, _materials, (9544.352, 9303.538, 430.00012), (0.0, -89.99999818714215, 0.0), (1.0, 1.0, 1.0), "NonDest_Boundry_3m_Ledge_B10", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (9854.148, 9603.538, 621.3999), (0.0, -89.99999818714215, 0.0), (1.0, 1.0, 1.0), "NonDest_Boundry_3m_Ledge_B11", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (9854.148, 9303.538, 621.3999), (0.0, -89.99999818714215, 0.0), (1.0, 1.0, 1.0), "NonDest_Boundry_3m_Ledge_B12", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (8897.495, 9603.538, 211.69626), (0.0, -89.99999818714215, 0.0), (1.0, 1.0, 1.0), "NonDest_Boundry_3m_Ledge_B13", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (8898.494, 9303.509, 211.69626), (0.0, -89.99999818714215, 0.0), (1.0, 1.0, 1.0), "NonDest_Boundry_3m_Ledge_B14", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (9254.81, 9603.538, 430.00006), (0.0, -89.99999818714215, 0.0), (1.0, 1.0, 1.0), "NonDest_Boundry_3m_Ledge_B7_5", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (9255.809, 9303.509, 430.00006), (0.0, -89.99999818714215, 0.0), (1.0, 1.0, 1.0), "NonDest_Boundry_3m_Ledge_B8", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (9544.352, 9603.538, 430.00012), (0.0, -89.99999818714215, 0.0), (1.0, 1.0, 1.0), "NonDest_Boundry_3m_Ledge_B9", _folder)
if a: placed += 1
else: skipped += 1

# Batch 24: StaticMesh'NonDest_Boundry_3m_Trim_B' (10 instances)
_mesh_path = "/Game/Art/Assets/Kits/Architecture/Non_D/NonDest_Boundry_3m_Trim_B"
_materials = ['/Game/Art/Assets/Kits/Architecture/Outdoors/MI_Outdoors_Trim_Sheet_A']
_folder = "Reconstruction/BD_BB_Outdoor_TradingPost/Meshes"
a = spawn_static_mesh(_mesh_path, _materials, (5954.9546, 8292.652, 549.19867), (0.0, 41.43737563967661, -0.0), (1.0, 1.0, 1.0), "NonDest_Boundry_3m_Trim_B_103", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (6179.8584, 8491.192, 349.19867), (0.0, 41.43737563967661, -0.0), (1.0, 1.0, 1.0), "NonDest_Boundry_3m_Trim_B10_317", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (6040.7725, 9102.058, 349.19867), (0.0, 41.43737563967661, -0.0), (1.0, 1.0, 1.0), "NonDest_Boundry_3m_Trim_B11", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5730.0513, 8094.112, 549.19867), (0.0, 41.43737563967661, -0.0), (1.0, 1.0, 1.0), "NonDest_Boundry_3m_Trim_B2", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5584.344, 8712.474, 549.19867), (0.0, -138.56254082510407, 0.0), (1.0, 1.0, 1.0), "NonDest_Boundry_3m_Trim_B3", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5809.2476, 8911.016, 549.19867), (0.0, -138.56254082510407, 0.0), (1.0, 1.0, 1.0), "NonDest_Boundry_3m_Trim_B4", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5505.148, 7895.5713, 549.19867), (0.0, 41.43737563967661, -0.0), (1.0, 1.0, 1.0), "NonDest_Boundry_3m_Trim_B5", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5359.441, 8513.932, 549.19867), (0.0, -138.56254082510407, 0.0), (1.0, 1.0, 1.0), "NonDest_Boundry_3m_Trim_B6", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5280.2446, 7697.0303, 549.19867), (0.0, 41.43737563967661, -0.0), (1.0, 1.0, 1.0), "NonDest_Boundry_3m_Trim_B7", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5134.5376, 8315.391, 549.19867), (0.0, -138.56254082510407, 0.0), (1.0, 1.0, 1.0), "NonDest_Boundry_3m_Trim_B8", _folder)
if a: placed += 1
else: skipped += 1

# Batch 25: StaticMesh'NonDest_Boundry_3m_Trim_B' (2 instances)
_mesh_path = "/Game/Art/Assets/Kits/Architecture/Non_D/NonDest_Boundry_3m_Trim_B"
_materials = ['/Game/Art/Assets/Kits/Architecture/Suburbs/Materials/Suburbs_Trim_Sheet_A/MI_Suburbs_Trim_Sheet_A']
_folder = "Reconstruction/BD_BB_Outdoor_TradingPost/Meshes"
a = spawn_static_mesh(_mesh_path, _materials, (5815.869, 8903.519, 349.19867), (0.0, 41.43737563967661, -0.0), (1.0, 1.0, 1.0), "NonDest_Boundry_3m_Trim_B12", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (6404.7617, 8689.731, 349.19867), (0.0, 41.43737563967661, -0.0), (1.0, 1.0, 1.0), "NonDest_Boundry_3m_Trim_B9", _folder)
if a: placed += 1
else: skipped += 1

# Batch 26: StaticMesh'NonDest_Floor_Trim_3M' (2 instances)
_mesh_path = "/Game/Art/Assets/Kits/Architecture/Non_D/NonDest_Floor_Trim_3M"
_materials = ['/Game/Art/Assets/Kits/Architecture/Outdoors/MI_Outdoors_Trim_Sheet_A']
_folder = "Reconstruction/BD_BB_Outdoor_TradingPost/Meshes"
a = spawn_static_mesh(_mesh_path, _materials, (12299.0, 9600.0, 802.0), (0.0, -90.00002735739477, 0.0), (1.0, 1.0, 1.0), "NonDest_Floor_Trim_3M_314", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (12299.0, 9900.0, 802.0), (0.0, -90.00002735739477, 0.0), (1.0, 1.0, 1.0), "NonDest_Floor_Trim_3M2", _folder)
if a: placed += 1
else: skipped += 1

# Batch 27: StaticMesh'NonDest_FloorBlock3m_3x3' (7 instances)
_mesh_path = "/Game/Art/Assets/Kits/Architecture/Non_D/NonDest_FloorBlock3m_3x3"
_materials = ['/Game/Environments/Materials/MI_ArchitectureBase_NonDestructible']
_folder = "Reconstruction/BD_BB_Outdoor_TradingPost/Meshes"
a = spawn_static_mesh(_mesh_path, _materials, (9600.0, 9750.0, 350.0), (0.0, 0.0, -0.0), (1.0, 1.0, 1.0), "NonDest_FloorBlock3m_3x13", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5310.6978, 7886.6055, 250.0), (0.0, -48.56256091827546, 0.0), (1.0, 1.0, 1.0), "NonDest_FloorBlock3m_3x19", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3057.2244, 6683.5317, 400.0), (0.0, 10.000023180215065, -0.0), (1.0, 1.0, 1.0), "NonDest_FloorBlock3m_3x35", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3804.3926, 5901.395, 400.0), (0.0, 10.000023180215065, -0.0), (1.0, 1.0, 1.0), "NonDest_FloorBlock3m_3x40", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4050.5947, 5944.8076, 400.0), (0.0, 10.000023180215065, -0.0), (0.700842, 1.0, 1.0), "NonDest_FloorBlock3m_3x41", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3893.284, 6830.952, 400.0), (0.0, 10.000023180215065, -0.0), (0.65844786, 1.0, 1.0), "NonDest_FloorBlock3m_3x42", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3508.9502, 5849.301, 400.0), (0.0, 10.000023180215065, -0.0), (1.0, 1.0, 1.0), "NonDest_FloorBlock3m_3x43", _folder)
if a: placed += 1
else: skipped += 1

# Batch 28: StaticMesh'NonDest_FloorBlock3m_3x3' (21 instances)
_mesh_path = "/Game/Art/Assets/Kits/Architecture/Non_D/NonDest_FloorBlock3m_3x3"
_materials = ['/Game/Environments/Materials/MI_ArchitectureBase_NonDestructible_RedRock']
_folder = "Reconstruction/BD_BB_Outdoor_TradingPost/Meshes"
a = spawn_static_mesh(_mesh_path, _materials, (9700.0, 9465.0, 430.0), (0.0, 0.0, -0.0), (1.0, 1.0, 1.0), "NonDest_FloorBlock3m_3x10", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (9250.0, 9450.0, 335.0), (0.0, 0.0, -0.0), (1.0, 1.0, 1.0), "NonDest_FloorBlock3m_3x14", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (6210.3125, 8680.768, 50.0), (0.0, -48.56256091827546, 0.0), (1.0, 1.0, 1.0), "NonDest_FloorBlock3m_3x21", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (6011.7705, 8905.674, 50.0), (0.0, -48.56256091827546, 0.0), (1.0, 1.0, 1.0), "NonDest_FloorBlock3m_3x22", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5535.601, 8085.146, -50.0), (0.0, -48.56256091827546, 0.0), (1.0, 1.0, 1.0), "NonDest_FloorBlock3m_3x23", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3213.5078, 5797.2046, 400.0), (0.0, 10.000023180215065, -0.0), (1.0, 1.0, 1.0), "NonDest_FloorBlock3m_3x29_2008", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3161.4133, 6092.647, 400.0), (0.0, 10.000023180215065, -0.0), (1.0, 1.0, 1.0), "NonDest_FloorBlock3m_3x31_2012", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3456.856, 6144.742, 400.0), (0.0, 10.000023180215065, -0.0), (1.0, 1.0, 1.0), "NonDest_FloorBlock3m_3x32", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3109.3188, 6388.0894, 400.0), (0.0, 10.000023180215065, -0.0), (1.0, 1.0, 1.0), "NonDest_FloorBlock3m_3x33", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3404.7615, 6440.1846, 400.0), (0.0, 10.000023180215065, -0.0), (1.0, 1.0, 1.0), "NonDest_FloorBlock3m_3x34", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3752.2983, 6196.837, 400.0), (0.0, 10.000023180215065, -0.0), (1.0, 1.0, 1.0), "NonDest_FloorBlock3m_3x36", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3700.2039, 6492.2793, 400.0), (0.0, 10.000023180215065, -0.0), (1.0, 1.0, 1.0), "NonDest_FloorBlock3m_3x37", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3997.4727, 6240.068, 400.0), (0.0, 10.000023180215065, -0.0), (0.6584476, 1.0, 1.0), "NonDest_FloorBlock3m_3x38", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3945.3782, 6535.5103, 400.0), (0.0, 10.000023180215065, -0.0), (0.6584476, 1.0, 1.0), "NonDest_FloorBlock3m_3x39", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (6210.3125, 8680.768, 350.0), (0.0, -48.56256091827546, 0.0), (1.0, 1.0, 1.0), "NonDest_FloorBlock3m_3x5", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2918.0654, 5745.11, 400.0), (0.0, 10.000023180215065, -0.0), (1.0, 1.0, 1.0), "NonDest_FloorBlock3m_3x54", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2865.971, 6040.5522, 400.0), (0.0, 10.000023180215065, -0.0), (1.0, 1.0, 1.0), "NonDest_FloorBlock3m_3x55", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2813.8765, 6335.995, 400.0), (0.0, 10.000023180215065, -0.0), (1.0, 1.0, 1.0), "NonDest_FloorBlock3m_3x56", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2761.782, 6631.4375, 400.0), (0.0, 10.000023180215065, -0.0), (1.0, 1.0, 1.0), "NonDest_FloorBlock3m_3x57", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (6011.7705, 8905.674, 350.0), (0.0, -48.56256091827546, 0.0), (1.0, 1.0, 1.0), "NonDest_FloorBlock3m_3x6", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (9700.0, 9765.0, 430.0), (0.0, 0.0, -0.0), (1.0, 1.0, 1.0), "NonDest_FloorBlock3m_3x9_29", _folder)
if a: placed += 1
else: skipped += 1

# Batch 29: StaticMesh'NonDest_FloorBlock3m_3x3' (20 instances)
_mesh_path = "/Game/Art/Assets/Kits/Architecture/Non_D/NonDest_FloorBlock3m_3x3"
_materials = ['/Game/Art/Assets/Kits/Architecture/Suburbs/Destructable/Materials/MI_Redrock_Wall_Non_Dest']
_folder = "Reconstruction/BD_BB_Outdoor_TradingPost/Meshes"
a = spawn_static_mesh(_mesh_path, _materials, (5310.6978, 7886.6055, 550.0), (0.0, -48.56256091827546, 0.0), (1.0, 1.0, 1.0), "NonDest_FloorBlock3m_3x15", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5112.156, 8111.5103, 550.0), (0.0, -48.56256091827546, 0.0), (1.0, 1.0, 1.0), "NonDest_FloorBlock3m_3x16", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5535.601, 8085.146, 250.0), (0.0, -48.56256091827546, 0.0), (1.0, 1.0, 1.0), "NonDest_FloorBlock3m_3x17", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5337.059, 8310.051, 250.0), (0.0, -48.56256091827546, 0.0), (1.0, 1.0, 1.0), "NonDest_FloorBlock3m_3x18", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5112.156, 8111.5103, 250.0), (0.0, -48.56256091827546, 0.0), (1.0, 1.0, 1.0), "NonDest_FloorBlock3m_3x20", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5337.059, 8310.051, -50.0), (0.0, -48.56256091827546, 0.0), (1.0, 1.0, 1.0), "NonDest_FloorBlock3m_3x24", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (12200.0, 10700.0, 1880.0), (0.0, 0.0, -0.0), (1.0, 1.0, 1.0), "NonDest_FloorBlock3m_3x25_2291", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (12200.0, 11000.0, 1880.0), (0.0, 0.0, -0.0), (1.0, 1.0, 1.0), "NonDest_FloorBlock3m_3x26", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (12200.0, 11300.0, 1880.0), (0.0, 0.0, -0.0), (1.0, 1.0, 1.0), "NonDest_FloorBlock3m_3x27", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (12500.0, 10700.0, 1880.0), (0.0, 0.0, -0.0), (1.0, 1.0, 1.0), "NonDest_FloorBlock3m_3x64", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (12500.0, 11000.0, 1880.0), (0.0, 0.0, -0.0), (1.0, 1.0, 1.0), "NonDest_FloorBlock3m_3x65", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (12500.0, 11300.0, 1880.0), (0.0, 0.0, -0.0), (1.0, 1.0, 1.0), "NonDest_FloorBlock3m_3x66", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (12200.0, 7900.0, 1880.0), (0.0, 0.0, -0.0), (1.0, 1.0, 1.0), "NonDest_FloorBlock3m_3x67", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (12200.0, 8200.0, 1880.0), (0.0, 0.0, -0.0), (1.0, 1.0, 1.0), "NonDest_FloorBlock3m_3x68", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (12200.0, 8500.0, 1880.0), (0.0, 0.0, -0.0), (1.0, 1.0, 1.0), "NonDest_FloorBlock3m_3x69", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5535.601, 8085.146, 550.0), (0.0, -48.56256091827546, 0.0), (1.0, 1.0, 1.0), "NonDest_FloorBlock3m_3x7", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (12500.0, 7900.0, 1880.0), (0.0, 0.0, -0.0), (1.0, 1.0, 1.0), "NonDest_FloorBlock3m_3x70", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (12500.0, 8200.0, 1880.0), (0.0, 0.0, -0.0), (1.0, 1.0, 1.0), "NonDest_FloorBlock3m_3x71", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (12500.0, 8500.0, 1880.0), (0.0, 0.0, -0.0), (1.0, 1.0, 1.0), "NonDest_FloorBlock3m_3x72", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5337.059, 8310.051, 550.0), (0.0, -48.56256091827546, 0.0), (1.0, 1.0, 1.0), "NonDest_FloorBlock3m_3x8", _folder)
if a: placed += 1
else: skipped += 1

# Batch 30: StaticMesh'NonDest_Pillar_2M_A' (2 instances)
_mesh_path = "/Game/Art/Assets/Kits/Architecture/Non_D/NonDest_Pillar_2M_A"
_materials = ['/Game/Art/Assets/Kits/Architecture/Outdoors/MI_Outdoors_Trim_Sheet_A']
_folder = "Reconstruction/BD_BB_Outdoor_TradingPost/Meshes"
a = spawn_static_mesh(_mesh_path, _materials, (12250.0, 9900.0, 650.0), (0.0, -89.9998815062137, 0.0), (1.0, 1.0, 1.0), "NonDest_Pillar_2M_A_318", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (12250.001, 9300.0, 650.0), (0.0, -89.9998815062137, 0.0), (1.0, 1.0, 1.0), "NonDest_Pillar_2M_A2", _folder)
if a: placed += 1
else: skipped += 1

# Batch 31: StaticMesh'NonDest_Pillar_3M_A' (4 instances)
_mesh_path = "/Game/Art/Assets/Kits/Architecture/Non_D/NonDest_Pillar_3M_A"
_materials = ['/Game/Art/Assets/Kits/Architecture/Outdoors/MI_Outdoors_Trim_Sheet_A']
_folder = "Reconstruction/BD_BB_Outdoor_TradingPost/Meshes"
a = spawn_static_mesh(_mesh_path, _materials, (4900.4375, 8124.6846, 200.0), (0.0, 41.43763664370613, -0.0), (1.0, 1.0, 1.0), "NonDest_Pillar_3M_A10", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (6249.8555, 9315.931, 0.0), (0.0, 41.43763664370613, -0.0), (1.0, 1.0, 1.0), "NonDest_Pillar_3M_A7", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (6646.938, 8866.125, 0.0), (0.0, 41.43763664370613, -0.0), (1.0, 1.0, 1.0), "NonDest_Pillar_3M_A8", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5297.5205, 7674.878, 200.0), (0.0, 41.43763664370613, -0.0), (1.0, 1.0, 1.0), "NonDest_Pillar_3M_A9", _folder)
if a: placed += 1
else: skipped += 1

# Batch 32: StaticMesh'NonDest_Pillar_4M_A' (2 instances)
_mesh_path = "/Game/Art/Assets/Kits/Architecture/Non_D/NonDest_Pillar_4M_A"
_materials = ['/Game/Art/Assets/Kits/Architecture/Outdoors/MI_Outdoors_Trim_Sheet_A']
_folder = "Reconstruction/BD_BB_Outdoor_TradingPost/Meshes"
a = spawn_static_mesh(_mesh_path, _materials, (6422.035, 8667.585, 0.0), (0.0, 41.43763664370613, -0.0), (1.0, 1.0, 1.0), "NonDest_Pillar_3M_A5", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (6024.952, 9117.392, 0.0), (0.0, 41.43763664370613, -0.0), (1.0, 1.0, 1.0), "NonDest_Pillar_3M_A6", _folder)
if a: placed += 1
else: skipped += 1

# Batch 33: StaticMesh'NonDest_Pillar_6M_A' (3 instances)
_mesh_path = "/Game/Art/Assets/Kits/Architecture/Non_D/NonDest_Pillar_6M_A"
_materials = ['/Game/Art/Assets/Kits/Architecture/Outdoors/MI_Outdoors_Trim_Sheet_A']
_folder = "Reconstruction/BD_BB_Outdoor_TradingPost/Meshes"
a = spawn_static_mesh(_mesh_path, _materials, (6197.132, 8469.044, -100.0), (0.0, 41.43763664370613, -0.0), (1.0, 1.0, 1.0), "NonDest_Pillar_3M_A_82", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5747.3257, 8071.961, -100.0), (0.0, 41.43763664370613, -0.0), (1.0, 1.0, 1.0), "NonDest_Pillar_3M_A2", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5350.242, 8521.765, -100.0), (0.0, 41.43763664370613, -0.0), (1.0, 1.0, 1.0), "NonDest_Pillar_3M_A4", _folder)
if a: placed += 1
else: skipped += 1

# Batch 34: StaticMesh'NonDest_Pillar_6M_A' (1 instances)
_mesh_path = "/Game/Art/Assets/Kits/Architecture/Non_D/NonDest_Pillar_6M_A"
_materials = ['/Game/Art/Assets/Kits/Architecture/Suburbs/Materials/Suburbs_Trim_Sheet_A/MI_Suburbs_Trim_Sheet_A']
_folder = "Reconstruction/BD_BB_Outdoor_TradingPost/Meshes"
a = spawn_static_mesh(_mesh_path, _materials, (5800.0483, 8918.848, -100.0), (0.0, 41.43763664370613, -0.0), (1.0, 1.0, 1.0), "NonDest_Pillar_3M_A3", _folder)
if a: placed += 1
else: skipped += 1

# Batch 35: StaticMesh'NonDest_Wall_Trim_Thick_3M' (2 instances)
_mesh_path = "/Game/Art/Assets/Kits/Architecture/Non_D/NonDest_Wall_Trim_Thick_3M"
_materials = ['/Game/Environments/Materials/MI_ArchitectureBase_NonDestructible_RedRock', '/Game/Art/Assets/Kits/Architecture/Outdoors/MI_Outdoors_Trim_Sheet_A']
_folder = "Reconstruction/BD_BB_Outdoor_TradingPost/Meshes"
a = spawn_static_mesh(_mesh_path, _materials, (6408.3745, 8670.734, -100.0), (0.0, -138.56229968164013, 0.0), (1.0, 1.0, 1.0), "NonDest_Wall_Trim_Thick_3M_298", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5733.666, 8075.1113, -100.0), (0.0, -138.56229968164013, 0.0), (1.0, 1.0, 1.0), "NonDest_Wall_Trim_Thick_3M2", _folder)
if a: placed += 1
else: skipped += 1

# Batch 36: StaticMesh'Scaffolding_Beam_B' (8 instances)
_mesh_path = "/Game/Art/Assets/Kits/Architecture/Suburbs/Destructable/Scaffolding_Beam_B"
_materials = ['/Game/Art/Assets/Kits/Architecture/Suburbs/Destructable/Materials/Scaffolding_Beam_A']
_folder = "Reconstruction/BD_BB_Outdoor_TradingPost/Meshes"
a = spawn_static_mesh(_mesh_path, _materials, (10268.825, 10368.439, 895.2278), (0.0, 42.62847849398373, -0.0), (1.5, 1.5, 1.5), "Scaffolding_Beam_B_659", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (10872.721, 10701.674, 776.32385), (0.0, 39.13122727058266, -0.0), (1.5, 1.5, 1.5), "Scaffolding_Beam_B2", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (12353.419, 10402.526, 895.2278), (0.05791999424790451, -145.87956539261623, 0.17293074110313642), (1.5, 1.5, 1.5), "Scaffolding_Beam_B3", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (11706.773, 10162.234, 776.97406), (0.05723697514601868, -149.37712757166523, -0.012969970357983614), (1.5, 1.5, 1.5), "Scaffolding_Beam_B4", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (12293.769, 8804.414, 895.2278), (0.0, -179.11849397837258, 0.0), (1.5, 1.5, 1.5), "Scaffolding_Beam_B5", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (11620.341, 8957.933, 776.32385), (0.0, 177.3844590769075, -0.0), (1.5, 1.5, 1.5), "Scaffolding_Beam_B6", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (9972.801, 10436.047, 895.2278), (0.0, 124.81174334549871, -0.0), (1.5, 1.5, 1.5), "Scaffolding_Beam_B7", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (9724.802, 11079.654, 776.32385), (0.0, 121.31403658915403, -0.0), (1.5, 1.5, 1.5), "Scaffolding_Beam_B8", _folder)
if a: placed += 1
else: skipped += 1

# Batch 37: StaticMesh'Crude_Board_A' (8 instances)
_mesh_path = "/Game/Art/Assets/Kits/Architecture/Suburbs/Materials/Crude_Ceiling/Crude_Board_A"
_materials = ['/Game/Art/Assets/Kits/Architecture/Suburbs/Materials/Crude_Ceiling/MI_Crude_Ceilng']
_folder = "Reconstruction/BD_BB_Outdoor_TradingPost/Meshes"
a = spawn_static_mesh(_mesh_path, _materials, (12199.416, 8900.122, 799.8749), (0.0, 89.99999818714215, -0.0), (1.0, 1.0, 1.0), "Crude_Board_B10", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (12199.416, 10302.232, 756.1803), (0.0, 89.99997063746636, -0.0), (1.0, 1.0, 1.0), "Crude_Board_B13", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (12199.416, 10302.232, 791.7682), (0.0, -89.99999818714215, 0.0), (1.0, 1.0, 1.0), "Crude_Board_B15", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (12199.416, 9946.791, 764.287), (0.0, -90.00005166594045, 0.0), (1.0, 1.0, 1.0), "Crude_Board_B16", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (12199.416, 9946.791, 799.8749), (0.0, 89.99999818714215, -0.0), (1.0, 1.0, 1.0), "Crude_Board_B18", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (12199.416, 9255.563, 756.1803), (0.0, 89.99997063746636, -0.0), (1.0, 1.0, 1.0), "Crude_Board_B5", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (12199.416, 9255.563, 791.7682), (0.0, -89.99999818714215, 0.0), (1.0, 1.0, 1.0), "Crude_Board_B7", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (12199.416, 8900.122, 764.287), (0.0, -90.00005166594045, 0.0), (1.0, 1.0, 1.0), "Crude_Board_B8", _folder)
if a: placed += 1
else: skipped += 1

# Batch 38: StaticMesh'Crude_Board_B' (9 instances)
_mesh_path = "/Game/Art/Assets/Kits/Architecture/Suburbs/Materials/Crude_Ceiling/Crude_Board_B"
_materials = ['/Game/Art/Assets/Kits/Architecture/Suburbs/Materials/Crude_Ceiling/MI_Crude_Ceilng']
_folder = "Reconstruction/BD_BB_Outdoor_TradingPost/Meshes"
a = spawn_static_mesh(_mesh_path, _materials, (12199.444, 9944.191, 747.256), (0.0, 89.99997063746636, -0.0), (1.0, 1.0, 1.0), "Crude_Board_B11", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (12199.416, 10302.232, 738.2551), (0.0, 89.99997063746636, -0.0), (1.0, 1.0, 1.0), "Crude_Board_B12", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (12199.416, 10302.232, 773.843), (0.0, -89.99999818714215, 0.0), (1.0, 1.0, 1.0), "Crude_Board_B14", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (12199.416, 9946.791, 781.9497), (0.0, 89.99999818714215, -0.0), (1.0, 1.0, 1.0), "Crude_Board_B17", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (12199.417, 10297.341, 747.256), (0.0, 89.99997063746636, -0.0), (1.0, 1.0, 1.0), "Crude_Board_B2", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (12199.444, 8897.522, 747.256), (0.0, 89.99997063746636, -0.0), (1.0, 1.0, 1.0), "Crude_Board_B3", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (12199.416, 9255.563, 738.2551), (0.0, 89.99997063746636, -0.0), (1.0, 1.0, 1.0), "Crude_Board_B4", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (12199.416, 9255.563, 773.843), (0.0, -89.99999818714215, 0.0), (1.0, 1.0, 1.0), "Crude_Board_B6", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (12199.416, 8900.122, 781.9497), (0.0, 89.99999818714215, -0.0), (1.0, 1.0, 1.0), "Crude_Board_B9", _folder)
if a: placed += 1
else: skipped += 1

# Batch 39: StaticMesh'Crude_Ceiling' (6 instances)
_mesh_path = "/Game/Art/Assets/Kits/Architecture/Suburbs/Materials/Crude_Ceiling/Crude_Ceiling"
_materials = ['/Game/Art/Assets/Kits/Architecture/Suburbs/Materials/Crude_Ceiling/MI_Crude_Ceilng']
_folder = "Reconstruction/BD_BB_Outdoor_TradingPost/Meshes"
a = spawn_static_mesh(_mesh_path, _materials, (10241.977, 11235.685, 641.8215), (-1.8768003969554088, 119.84897700574739, -0.03097549512084527), (1.0, 1.0, 1.0), "Crude_Ceiling_712", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4315.253, 4675.2, 345.059), (0.0, -22.465301338149157, 0.0), (1.0, 1.0, 1.0), "Crude_Ceiling14", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (11806.587, 9140.689, 592.2194), (0.0, 0.0, -0.0), (1.0, 1.0, 1.0), "Crude_Ceiling2_566", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (11511.928, 9140.689, 592.2194), (0.0, 0.0, -0.0), (1.0, 1.0, 1.0), "Crude_Ceiling3", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (11652.352, 9987.467, 592.21936), (0.0, 0.0, -0.0), (1.0, 1.0, 1.0), "Crude_Ceiling4", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (11357.692, 9987.467, 592.21936), (0.0, 0.0, -0.0), (1.0, 1.0, 1.0), "Crude_Ceiling5", _folder)
if a: placed += 1
else: skipped += 1

# Batch 40: StaticMesh'Crude_Stairs_2M' (2 instances)
_mesh_path = "/Game/Art/Assets/Kits/Architecture/Suburbs/Materials/Crude_Stairs/Crude_Stairs_2M"
_materials = ['/Game/Art/Assets/Kits/Architecture/Suburbs/Materials/Crude_Ceiling/MI_Crude_Ceilng']
_folder = "Reconstruction/BD_BB_Outdoor_TradingPost/Meshes"
a = spawn_static_mesh(_mesh_path, _materials, (12050.0, 10035.223, 742.10846), (0.0, -90.00009542133918, 0.0), (1.0, 1.0, 1.0), "Crude_Stairs_2M2", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (12050.0, 9164.205, 742.10846), (0.0, -90.00009542133918, 0.0), (1.0, 1.0, 1.0), "Crude_Stairs_2M3", _folder)
if a: placed += 1
else: skipped += 1

# Batch 41: StaticMesh'SM_AR_City_Column_B_Base' (4 instances)
_mesh_path = "/Game/Art/Assets/Kits/Architecture/Suburbs/SM_AR_City_Column_B_Base"
_materials = ['/Game/Art/Assets/Kits/Architecture/Suburbs/Materials/SM_AR_City_Column_B/MI_SM_AR_City_Column_B_Shaft_Red', '/Game/Art/Assets/Kits/Architecture/Suburbs/Materials/SM_AR_City_Column_B/MI_SM_AR_City_Column_B_Base_Red']
_folder = "Reconstruction/BD_BB_Outdoor_TradingPost/Meshes"
a = spawn_static_mesh(_mesh_path, _materials, (12495.445, 9850.573, 2512.3757), (0.0, 90.00001925454477, -0.0), (1.6525966, 1.6525966, 1.6525966), "SM_AR_City_Column_B_Base_182", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (12495.445, 9334.147, 2512.3757), (0.0, 90.00001925454477, -0.0), (1.6525966, 1.6525966, 1.6525966), "SM_AR_City_Column_B_Base2", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (12495.44, 8971.553, 2512.3757), (0.0, 90.00001925454477, -0.0), (1.6525966, 1.6525966, 1.6525966), "SM_AR_City_Column_B_Base3", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (12495.443, 10213.147, 2511.9941), (0.0, 90.00001925454477, -0.0), (1.6525966, 1.6525966, 1.6525966), "SM_AR_City_Column_B_Base4", _folder)
if a: placed += 1
else: skipped += 1

# Batch 42: StaticMesh'SM_AR_City_Column_B_Capital' (4 instances)
_mesh_path = "/Game/Art/Assets/Kits/Architecture/Suburbs/SM_AR_City_Column_B_Capital"
_materials = ['/Game/Art/Assets/Kits/Architecture/Suburbs/Materials/SM_AR_City_Column_B/MI_SM_AR_City_Column_B_Capital_Red', '/Game/Art/Assets/Kits/Architecture/Suburbs/Materials/SM_AR_City_Column_B/MI_SM_AR_City_Column_B_Shaft_Red']
_folder = "Reconstruction/BD_BB_Outdoor_TradingPost/Meshes"
a = spawn_static_mesh(_mesh_path, _materials, (12495.446, 9850.569, 3456.7913), (0.0, 90.00001925454477, -0.0), (1.6525966, 1.6525966, 1.2110707), "SM_AR_City_Column_B_Capital_179", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (12495.447, 9334.147, 3456.7913), (0.0, 90.00001925454477, -0.0), (1.6525966, 1.6525966, 1.2110707), "SM_AR_City_Column_B_Capital2", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (12495.434, 8971.554, 3291.6013), (0.0, 90.00001925454477, -0.0), (1.6525966, 1.6525966, 1.6525966), "SM_AR_City_Column_B_Capital3", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (12495.433, 10213.159, 3291.6013), (0.0, 90.00001925454477, -0.0), (1.6525966, 1.6525966, 1.6525966), "SM_AR_City_Column_B_Capital4", _folder)
if a: placed += 1
else: skipped += 1

# Batch 43: StaticMesh'SM_AR_City_Column_B_Shaft' (8 instances)
_mesh_path = "/Game/Art/Assets/Kits/Architecture/Suburbs/SM_AR_City_Column_B_Shaft"
_materials = ['/Game/Art/Assets/Kits/Architecture/Suburbs/Materials/SM_AR_City_Column_B/MI_SM_AR_City_Column_B_Shaft_Red']
_folder = "Reconstruction/BD_BB_Outdoor_TradingPost/Meshes"
a = spawn_static_mesh(_mesh_path, _materials, (12495.446, 9850.569, 2795.753), (0.0, 90.00001925454477, -0.0), (1.6525966, 1.6525966, 1.6525966), "SM_AR_City_Column_B_Shaft_185", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (12495.441, 8971.553, 3126.256), (0.0, 90.00001925454477, -0.0), (1.6525966, 1.6525966, 1.6525966), "SM_AR_City_Column_B_Shaft11", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (12495.44, 10213.147, 2795.753), (0.0, 90.00001925454477, -0.0), (1.6525966, 1.6525966, 1.6525966), "SM_AR_City_Column_B_Shaft12_206", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (12495.44, 10213.155, 3126.256), (0.0, 90.00001925454477, -0.0), (1.6525966, 1.6525966, 1.6525966), "SM_AR_City_Column_B_Shaft14", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (12495.446, 9850.569, 3126.256), (0.0, 90.00001925454477, -0.0), (1.6525966, 1.6525966, 1.6525966), "SM_AR_City_Column_B_Shaft3", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (12495.447, 9334.147, 2795.753), (0.0, 90.00001925454477, -0.0), (1.6525966, 1.6525966, 1.6525966), "SM_AR_City_Column_B_Shaft5", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (12495.447, 9334.147, 3126.256), (0.0, 90.00001925454477, -0.0), (1.6525966, 1.6525966, 1.6525966), "SM_AR_City_Column_B_Shaft7", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (12495.441, 8971.553, 2795.753), (0.0, 90.00001925454477, -0.0), (1.6525966, 1.6525966, 1.6525966), "SM_AR_City_Column_B_Shaft9", _folder)
if a: placed += 1
else: skipped += 1

# Batch 44: StaticMesh'Suburb_Stairs_Trim_3M_B' (1 instances)
_mesh_path = "/Game/Art/Assets/Kits/Architecture/Suburbs/Suburb_Stairs_Trim_3M_B"
_materials = ['/Game/Art/Assets/Kits/Architecture/Suburbs/Materials/Suburb_Stairs_Trim/MI_Suburb_Stairs_Trim_3M_RedRock']
_folder = "Reconstruction/BD_BB_Outdoor_TradingPost/Meshes"
a = spawn_static_mesh(_mesh_path, _materials, (6412.8477, 8663.752, 350.0), (0.0, 41.43737563967661, -0.0), (1.0, 1.0, 1.0), "Suburb_Stairs_Trim_Ruin_3M2", _folder)
if a: placed += 1
else: skipped += 1

# Batch 45: StaticMesh'Suburb_Stairs_Trim_Angle_A' (8 instances)
_mesh_path = "/Game/Art/Assets/Kits/Architecture/Suburbs/Suburb_Stairs_Trim_Angle_A"
_materials = ['/Game/Art/Assets/Kits/Architecture/Suburbs/Materials/Suburb_Stairs_Trim/MI_Suburbs_Stairs_Trim_Angle_Red_Rock']
_folder = "Reconstruction/BD_BB_Outdoor_TradingPost/Meshes"
a = spawn_static_mesh(_mesh_path, _materials, (10015.706, 9920.0, 1590.0), (90.0, -175.23641837555166, -85.23635764201748), (1.0, 1.0, 1.0), "Suburb_Stairs_Trim_Angle_A_1591", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (9985.706, 9260.0, 1590.0), (90.0, -5.042490875779919, -95.04232357208032), (1.0, 1.0, 1.0), "Suburb_Stairs_Trim_Angle_A2", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (6490.531, 8704.878, 1146.6394), (90.0, 11.188369929060146, -118.81177943979182), (1.0, 1.0, 1.0), "Suburb_Stairs_Trim_Angle_A3", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (6089.2725, 9229.753, 1146.6394), (90.0, 0.0, 50.00008706581173), (1.0, 1.0, 1.0), "Suburb_Stairs_Trim_Angle_A4", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4081.246, 6069.461, 1146.6411), (90.0, -143.32921898932477, -247.37923372237213), (1.0, 1.0, 1.0), "Suburb_Stairs_Trim_Angle_A5", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3950.133, 6717.0015, 1146.6411), (90.0, 0.8743144879262962, 76.82475757488933), (1.0, 1.0, 1.0), "Suburb_Stairs_Trim_Angle_A6", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2984.5056, 5796.6875, 1376.575), (90.0, 147.237319037336, 47.42629750536486), (1.0, 1.0, 1.0), "Suburb_Stairs_Trim_Angle_A7", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2901.6306, 6452.15, 1376.575), (90.0, 26.47881782283771, 106.66818519519937), (1.0, 1.0, 1.0), "Suburb_Stairs_Trim_Angle_A8", _folder)
if a: placed += 1
else: skipped += 1

# Batch 46: StaticMesh'Suburb_Stairs_Trim_Pillar_A' (4 instances)
_mesh_path = "/Game/Art/Assets/Kits/Architecture/Suburbs/Suburb_Stairs_Trim_Pillar_A"
_materials = ['/Game/Art/Assets/Kits/Architecture/Suburbs/Materials/Suburb_Stairs_Trim/MI_Suburb_Stairs_Trim_Pillar_A_RedRock']
_folder = "Reconstruction/BD_BB_Outdoor_TradingPost/Meshes"
a = spawn_static_mesh(_mesh_path, _materials, (6197.775, 8478.07, 550.0), (0.0, 41.43737563967661, -0.0), (1.0, 1.0, 1.0), "Suburb_Stairs_Trim_Pillar_A_118", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5807.313, 8920.383, 550.0), (0.0, 41.43737563967661, -0.0), (1.0, 1.0, 1.0), "Suburb_Stairs_Trim_Pillar_A2", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5298.16, 7683.911, 550.0), (0.0, -138.56250075143797, 0.0), (1.0, 1.0, 1.0), "Suburb_Stairs_Trim_Pillar_A4", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4911.0073, 8122.474, 550.0), (0.0, -138.56268066991834, 0.0), (1.0, 1.0, 1.0), "Suburb_Stairs_Trim_Pillar_A5", _folder)
if a: placed += 1
else: skipped += 1

# Batch 47: StaticMesh'Suburb_Stairs_Trim_Pillar_B' (1 instances)
_mesh_path = "/Game/Art/Assets/Kits/Architecture/Suburbs/Suburb_Stairs_Trim_Pillar_B"
_materials = ['/Game/Art/Assets/Kits/Architecture/Suburbs/Materials/Suburb_Stairs_Trim/MI_Suburb_Stairs_Trim_Pillar_B_RedRock']
_folder = "Reconstruction/BD_BB_Outdoor_TradingPost/Meshes"
a = spawn_static_mesh(_mesh_path, _materials, (6625.1562, 8855.228, 349.99994), (0.0, 41.43737563967661, -0.0), (1.0, 1.0, 1.0), "Suburb_Stairs_Trim_Pillar_A3", _folder)
if a: placed += 1
else: skipped += 1

# Batch 48: StaticMesh'Suburb_Stairs_Trim_Ruin_3M' (1 instances)
_mesh_path = "/Game/Art/Assets/Kits/Architecture/Suburbs/Suburb_Stairs_Trim_Ruin_3M"
_materials = ['/Game/Art/Assets/Kits/Architecture/Suburbs/Materials/Suburb_Stairs_Trim/MI_Suburb_Stairs_Trim_3M_Dest_RedRock', '/Game/Environments/Models/Architecture/Materials/MI_ArchSimple_Stone_Damaged_A_MAT_RedRock']
_folder = "Reconstruction/BD_BB_Outdoor_TradingPost/Meshes"
a = spawn_static_mesh(_mesh_path, _materials, (6002.1567, 9128.979, 350.0), (0.0, 41.43737563967661, -0.0), (1.0, 1.0, 1.0), "Suburb_Stairs_Trim_Ruin_3M_140", _folder)
if a: placed += 1
else: skipped += 1

# Batch 49: StaticMesh'Suburbs_Column_X_Large_A_Shaft' (3 instances)
_mesh_path = "/Game/Art/Assets/Kits/Architecture/Suburbs/Suburbs_Column_X_Large_A_Shaft"
_materials = ['/Game/Art/Assets/Kits/Architecture/Suburbs/Materials/Suburbs_Column_X_Large_A/MI_Suburbs_Column_X_Large_A_Shaft']
_folder = "Reconstruction/BD_BB_Outdoor_TradingPost/Meshes"
a = spawn_static_mesh(_mesh_path, _materials, (12489.998, 9931.386, 2779.0713), (0.0, 90.00001925454477, -0.0), (1.2111866, 1.2111866, 1.2111866), "Suburbs_Column_X_Large_A_Shaft_418", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (12378.764, 7858.485, 1247.0244), (0.0, 90.00001925454477, -0.0), (1.2111866, 1.2111866, 1.2111866), "Suburbs_Column_X_Large_A_Shaft14", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (12489.998, 9931.388, 3262.0015), (0.0, 90.00001925454477, -0.0), (1.2111866, 1.2111866, 1.0111051), "Suburbs_Column_X_Large_A_Shaft2", _folder)
if a: placed += 1
else: skipped += 1

# Batch 50: StaticMesh'Suburbs_Column_X_Large_A_Shaft' (24 instances)
_mesh_path = "/Game/Art/Assets/Kits/Architecture/Suburbs/Suburbs_Column_X_Large_A_Shaft"
_materials = ['/Game/Art/Assets/Kits/Architecture/Suburbs/Materials/Suburbs_Column_X_Large_A/MI_Suburbs_Column_X_Large_A_Shaft_Red']
_folder = "Reconstruction/BD_BB_Outdoor_TradingPost/Meshes"
a = spawn_static_mesh(_mesh_path, _materials, (12446.324, 7948.327, 3406.4326), (-90.0, 145.00802964006084, -55.00799755442175), (1.2111866, 1.2111866, 1.1111866), "Suburbs_Column_X_Large_A_Shaft10", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (12867.82, 7732.464, 3164.6338), (34.520371342028284, -89.99999257042616, 6.701623208889259e-06), (1.2111866, 1.2111866, 1.0861865), "Suburbs_Column_X_Large_A_Shaft11", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (12446.316, 7858.4775, 2212.4268), (0.0, 90.00001925454477, -0.0), (1.2111866, 1.2111866, 1.2111866), "Suburbs_Column_X_Large_A_Shaft12", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (12446.064, 7858.485, 1730.4769), (0.0, 90.00001925454477, -0.0), (1.2111866, 1.2111866, 1.2111866), "Suburbs_Column_X_Large_A_Shaft13", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (12446.324, 8392.727, 3406.4326), (-90.0, 145.00802964006084, -55.00799755442175), (1.2111866, 1.2111866, 1.1111866), "Suburbs_Column_X_Large_A_Shaft15", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (12867.819, 8763.886, 3488.9204), (54.35295178094229, -89.99993598973771, 4.5978712205077566e-07), (1.2111866, 1.2111866, 0.86711705), "Suburbs_Column_X_Large_A_Shaft16", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (12446.312, 11463.527, 2695.2427), (0.0, 90.00004680423052, -0.0), (1.211187, 1.2111866, 1.2111866), "Suburbs_Column_X_Large_A_Shaft17", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (12446.313, 11228.973, 3527.894), (90.0, 179.99988830316968, 90.00011175672094), (1.211187, 1.2111866, 1.1111866), "Suburbs_Column_X_Large_A_Shaft18", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (12867.804, 11366.5625, 3107.846), (-34.52035463824599, -89.99994147337989, 9.399067833370829e-06), (1.211187, 1.2111866, 1.0861865), "Suburbs_Column_X_Large_A_Shaft19", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (12446.312, 11465.897, 2211.4353), (0.0, 90.00004680423052, -0.0), (1.211187, 1.2111866, 1.2111866), "Suburbs_Column_X_Large_A_Shaft20", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (12446.322, 11465.859, 1729.4854), (0.0, 90.00004680423052, -0.0), (1.211187, 1.2111866, 1.2111866), "Suburbs_Column_X_Large_A_Shaft21", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (12490.001, 8989.424, 2179.879), (0.0, 90.00001925454477, -0.0), (1.211187, 1.211187, 1.211187), "Suburbs_Column_X_Large_A_Shaft22", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (12446.322, 10809.135, 3526.9854), (90.0, 179.99988830316968, 90.00011175672094), (1.211187, 1.2111866, 1.1111866), "Suburbs_Column_X_Large_A_Shaft23", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (12868.574, 10381.941, 3402.6792), (-57.132746036935956, -89.99948471057012, 9.294796843247365e-05), (1.211187, 1.2111866, 0.8810154), "Suburbs_Column_X_Large_A_Shaft24", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (12446.32, 9050.44, 3570.544), (-90.0, 145.00802964006084, -55.00799755442175), (1.2111866, 1.2111866, 1.3811864), "Suburbs_Column_X_Large_A_Shaft25", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (12446.32, 9601.359, 3570.5454), (-90.0, 145.00802964006084, -55.00799755442175), (1.2111866, 1.2111866, 1.3711866), "Suburbs_Column_X_Large_A_Shaft26", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (12489.999, 10308.162, 2179.879), (0.0, 90.00001925454477, -0.0), (1.211187, 1.211187, 1.211187), "Suburbs_Column_X_Large_A_Shaft27", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (12489.998, 9376.384, 2779.0713), (0.0, 90.00001925454477, -0.0), (1.2111866, 1.2111866, 1.2111866), "Suburbs_Column_X_Large_A_Shaft3", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (12489.998, 9376.385, 3262.0015), (0.0, 90.00001925454477, -0.0), (1.2111866, 1.2111866, 1.0111051), "Suburbs_Column_X_Large_A_Shaft4", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (12490.001, 8989.424, 2629.879), (0.0, 90.00001925454477, -0.0), (1.2111866, 1.2111866, 1.2111866), "Suburbs_Column_X_Large_A_Shaft5", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (12490.001, 8989.426, 3112.8086), (0.0, 90.00001925454477, -0.0), (1.2111866, 1.2111866, 1.2111866), "Suburbs_Column_X_Large_A_Shaft6", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (12489.999, 10308.162, 2629.879), (0.0, 90.00001925454477, -0.0), (1.2111866, 1.2111866, 1.2111866), "Suburbs_Column_X_Large_A_Shaft7", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (12489.999, 10308.164, 3112.8086), (0.0, 90.00001925454477, -0.0), (1.2111866, 1.2111866, 1.2111866), "Suburbs_Column_X_Large_A_Shaft8", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (12446.316, 7858.4775, 2695.8787), (0.0, 90.00001925454477, -0.0), (1.2111866, 1.2111866, 1.2111866), "Suburbs_Column_X_Large_A_Shaft9_587", _folder)
if a: placed += 1
else: skipped += 1

# Batch 51: StaticMesh'Crude_Wood_Platform_2x2M' (4 instances)
_mesh_path = "/Game/Art/Assets/Kits/Architecture/Suburbs/Suburbs_Floor/Crude_Wood_Platform_2x2M"
_materials = ['/Game/Art/Assets/Kits/Architecture/Suburbs/Materials/Crude_Ceiling/MI_Crude_Ceilng']
_folder = "Reconstruction/BD_BB_Outdoor_TradingPost/Meshes"
a = spawn_static_mesh(_mesh_path, _materials, (12148.858, 9160.534, 539.0621), (0.0, 0.0, -0.0), (1.0, 1.0, 1.0), "Crude_Wood_Platform_2x2M_580", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (12148.858, 8961.911, 539.0621), (0.0, 0.0, -0.0), (1.0, 1.0, 1.0), "Crude_Wood_Platform_2x2M2", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (12148.858, 10237.443, 537.7282), (0.0, 0.0, -0.0), (1.0, 1.0, 1.0), "Crude_Wood_Platform_2x2M3", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (12148.858, 10038.82, 537.7282), (0.0, 0.0, -0.0), (1.0, 1.0, 1.0), "Crude_Wood_Platform_2x2M4", _folder)
if a: placed += 1
else: skipped += 1

# Batch 52: StaticMesh'Suburbs_Floor_3x3m_A' (8 instances)
_mesh_path = "/Game/Art/Assets/Kits/Architecture/Suburbs/Suburbs_Floor_3x3m_A"
_materials = ['/Game/Environments/Materials/MI_ArchitectureBase_NonDestructible_RedRock']
_folder = "Reconstruction/BD_BB_Outdoor_TradingPost/Meshes"
a = spawn_static_mesh(_mesh_path, _materials, (5976.3027, 8490.805, 550.0), (0.0, -48.56256091827546, 0.0), (1.0, 1.0, 1.0), "Suburbs_Floor_3x3m_A106_226", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5751.3994, 8292.264, 550.0), (0.0, -48.56256091827546, 0.0), (1.0, 1.0, 1.0), "Suburbs_Floor_3x3m_A107", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5777.761, 8715.71, 550.0), (0.0, -48.56256091827546, 0.0), (1.0, 1.0, 1.0), "Suburbs_Floor_3x3m_A108", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5552.858, 8517.169, 550.0), (0.0, -48.56256091827546, 0.0), (1.0, 1.0, 1.0), "Suburbs_Floor_3x3m_A109", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5526.496, 8093.722, 550.0), (0.0, -48.56256091827546, 0.0), (1.0, 1.0, 1.0), "Suburbs_Floor_3x3m_A110", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5327.9546, 8318.628, 550.0), (0.0, -48.56256091827546, 0.0), (1.0, 1.0, 1.0), "Suburbs_Floor_3x3m_A111", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5301.593, 7895.1807, 550.0), (0.0, -48.56256091827546, 0.0), (1.0, 1.0, 1.0), "Suburbs_Floor_3x3m_A112", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5103.0513, 8120.0874, 550.0), (0.0, -48.56256091827546, 0.0), (1.0, 1.0, 1.0), "Suburbs_Floor_3x3m_A113", _folder)
if a: placed += 1
else: skipped += 1

# Batch 53: StaticMesh'Suburbs_Floor_3x3m_AA_Broken' (5 instances)
_mesh_path = "/Game/Art/Assets/Kits/Architecture/Suburbs/Suburbs_Floor_3x3m_AA_Broken"
_materials = ['/Game/Art/Assets/Kits/Architecture/Suburbs/Suburbs_Floor/Materials/Subrubs_Floor_Tileable_A/Suburbs_Floor_A_NonDest_RedRock']
_folder = "Reconstruction/BD_BB_Outdoor_TradingPost/Meshes"
a = spawn_static_mesh(_mesh_path, _materials, (6435.216, 8879.308, 350.0), (0.0, -138.56254082510407, 0.0), (1.0, 1.0, 1.0), "Suburbs_Floor_3x3m_B_180", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5321.712, 7949.681, 552.1742), (0.0, 131.43737614586334, -0.0), (1.0, 1.0, 1.0), "Suburbs_Floor_3x3m_B10", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5531.099, 8468.006, 552.1742), (0.0, 41.43760484019437, -0.0), (1.0, 1.0, 1.0), "Suburbs_Floor_3x3m_B5", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5306.196, 8269.465, 552.1742), (0.0, -48.56243920286699, 0.0), (1.0, 1.0, 1.0), "Suburbs_Floor_3x3m_B6", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5921.454, 8479.124, 552.1742), (0.0, -138.56253037946084, 0.0), (1.0, 1.0, 1.0), "Suburbs_Floor_3x3m_B9", _folder)
if a: placed += 1
else: skipped += 1

# Batch 54: StaticMesh'Suburbs_Floor_3x3m_AB_Broken' (6 instances)
_mesh_path = "/Game/Art/Assets/Kits/Architecture/Suburbs/Suburbs_Floor_3x3m_AB_Broken"
_materials = ['/Game/Art/Assets/Kits/Architecture/Suburbs/Suburbs_Floor/Materials/Subrubs_Floor_Tileable_A/Suburbs_Floor_A_NonDest_RedRock']
_folder = "Reconstruction/BD_BB_Outdoor_TradingPost/Meshes"
a = spawn_static_mesh(_mesh_path, _materials, (5156.2593, 8137.104, 551.67285), (0.0, 41.43768952990157, -0.0), (1.0, 1.0, 1.0), "Suburbs_Floor_3x3m_B11", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (6236.675, 9104.212, 350.0), (0.0, 41.43760484019437, -0.0), (1.0, 1.0, 1.0), "Suburbs_Floor_3x3m_B2", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (6322.7095, 9006.754, 350.0), (0.0, 131.43759715723988, -0.0), (1.0, 1.0, 1.0), "Suburbs_Floor_3x3m_B3", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5756.0024, 8666.545, 552.1742), (0.0, 41.43760484019437, -0.0), (1.0, 1.0, 1.0), "Suburbs_Floor_3x3m_B4", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5471.6465, 8082.0454, 551.67285), (0.0, -48.56241002144553, 0.0), (1.0, 1.0, 1.0), "Suburbs_Floor_3x3m_B7", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5696.55, 8280.586, 551.67285), (0.0, 131.4376329472639, -0.0), (1.0, 1.0, 1.0), "Suburbs_Floor_3x3m_B8", _folder)
if a: placed += 1
else: skipped += 1

# Batch 55: StaticMesh'Suburbs_Floor_Stone_IND_A' (3 instances)
_mesh_path = "/Game/Art/Assets/Kits/Architecture/Suburbs/Suburbs_Floor_Stone_IND_A"
_materials = ['/Game/Art/Assets/Kits/Architecture/Suburbs/Materials/Suburbs_Floor_Stone_IND/MI_Suburbs_Floor_Stone_IND_MAT_Inst_Dest_RedRock']
_folder = "Reconstruction/BD_BB_Outdoor_TradingPost/Meshes"
a = spawn_static_mesh(_mesh_path, _materials, (6184.9966, 9159.998, 357.54358), (0.0, -44.99999866815529, 0.0), (1.0, 1.0, 1.0), "Suburbs_Floor_Stone_IND_A_200", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (6290.304, 9111.527, 355.0), (0.0, 10.00001622682798, -0.0), (1.0, 1.0, 1.0), "Suburbs_Floor_Stone_IND_B_203", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (6422.889, 8972.918, 360.0), (0.0, -45.000056798727684, 0.0), (1.0, 1.0, 1.0), "Suburbs_Floor_Stone_IND_C_187", _folder)
if a: placed += 1
else: skipped += 1

# Batch 56: StaticMesh'Suburbs_Floor_Stone_IND_A' (4 instances)
_mesh_path = "/Game/Art/Assets/Kits/Architecture/Suburbs/Suburbs_Floor_Stone_IND_A"
_materials = ['/Game/Art/Assets/Kits/Architecture/Suburbs/Materials/Suburbs_Floor_Stone_IND/MI_Suburbs_Floor_Stone_IND_MAT_Inst_Dest_RedRock']
_folder = "Reconstruction/BD_BB_Outdoor_TradingPost/Meshes"
a = spawn_static_mesh(_mesh_path, _materials, (5741.772, 8739.851, 561.1494), (0.0, -50.00003087412388, 0.0), (1.0, 1.0, 1.0), "Suburbs_Floor_Stone_IND_A2_738", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5646.026, 8248.294, 559.9043), (0.0, -50.000093879931846, 0.0), (1.0, 1.0, 1.0), "Suburbs_Floor_Stone_IND_A3_747", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5198.5806, 8022.1895, 559.9044), (0.0, -50.000093879931846, 0.0), (1.0, 1.0, 1.0), "Suburbs_Floor_Stone_IND_A4", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5422.891, 8093.461, 559.9043), (0.0, 68.08283345620231, -0.0), (1.0, 1.0, 1.0), "Suburbs_Floor_Stone_IND_A5", _folder)
if a: placed += 1
else: skipped += 1

# Batch 57: StaticMesh'Suburbs_Floor_Stone_IND_B' (2 instances)
_mesh_path = "/Game/Art/Assets/Kits/Architecture/Suburbs/Suburbs_Floor_Stone_IND_B"
_materials = ['/Game/Art/Assets/Kits/Architecture/Suburbs/Materials/Suburbs_Floor_Stone_IND/MI_Suburbs_Floor_Stone_IND_MAT_Inst_Dest_RedRock']
_folder = "Reconstruction/BD_BB_Outdoor_TradingPost/Meshes"
a = spawn_static_mesh(_mesh_path, _materials, (5910.7705, 8550.757, 560.5649), (0.0, -50.00003087412388, 0.0), (1.0, 1.0, 1.0), "Suburbs_Floor_Stone_IND_B2_735", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5255.943, 8212.727, 560.56366), (0.0, -52.81887653606694, 0.0), (1.0, 1.0, 1.0), "Suburbs_Floor_Stone_IND_B3", _folder)
if a: placed += 1
else: skipped += 1

# Batch 58: StaticMesh'Suburbs_Floor_Stone_IND_C' (1 instances)
_mesh_path = "/Game/Art/Assets/Kits/Architecture/Suburbs/Suburbs_Floor_Stone_IND_C"
_materials = ['/Game/Art/Assets/Kits/Architecture/Suburbs/Materials/Suburbs_Floor_Stone_IND/MI_Suburbs_Floor_Stone_IND_MAT_Inst_Dest_RedRock', '/Game/Art/Assets/Kits/Architecture/Suburbs/Materials/Suburbs_Floor_Stone_IND/MI_Suburbs_Floor_Stone_IND_MAT_Inst_Dest_RedRock']
_folder = "Reconstruction/BD_BB_Outdoor_TradingPost/Meshes"
a = spawn_static_mesh(_mesh_path, _materials, (5687.3755, 8439.229, 558.47766), (0.0, 0.0, -0.0), (1.0, 1.0, 1.0), "Suburbs_Floor_Stone_IND_C2_756", _folder)
if a: placed += 1
else: skipped += 1

# Batch 59: StaticMesh'Suburbs_Floor_Stone_IND_D' (1 instances)
_mesh_path = "/Game/Art/Assets/Kits/Architecture/Suburbs/Suburbs_Floor_Stone_IND_D"
_materials = ['/Game/Art/Assets/Kits/Architecture/Suburbs/Materials/Suburbs_Floor_Stone_IND/MI_Suburbs_Floor_Stone_IND_MAT_Inst_Dest_RedRock']
_folder = "Reconstruction/BD_BB_Outdoor_TradingPost/Meshes"
a = spawn_static_mesh(_mesh_path, _materials, (6336.715, 8802.424, 357.3205), (0.0, 45.00001509340179, -0.0), (1.0, 1.0, 1.0), "Suburbs_Floor_Stone_IND_D_206", _folder)
if a: placed += 1
else: skipped += 1

# Batch 60: StaticMesh'Suburbs_Floor_Stone_IND_D' (3 instances)
_mesh_path = "/Game/Art/Assets/Kits/Architecture/Suburbs/Suburbs_Floor_Stone_IND_D"
_materials = ['/Game/Art/Assets/Kits/Architecture/Suburbs/Materials/Suburbs_Floor_Stone_IND/MI_Suburbs_Floor_Stone_IND_MAT_Inst_Dest_RedRock']
_folder = "Reconstruction/BD_BB_Outdoor_TradingPost/Meshes"
a = spawn_static_mesh(_mesh_path, _materials, (5582.7593, 8457.258, 558.50854), (0.0, 40.000030478796546, -0.0), (1.0, 1.0, 1.0), "Suburbs_Floor_Stone_IND_D2_744", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5544.5376, 8325.788, 560.4585), (0.0, 42.95459472199787, -0.0), (1.0, 1.0, 1.0), "Suburbs_Floor_Stone_IND_D3_765", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5738.3423, 8174.3926, 558.50854), (0.0, 40.000030478796546, -0.0), (1.0, 1.0, 1.0), "Suburbs_Floor_Stone_IND_D4", _folder)
if a: placed += 1
else: skipped += 1

# Batch 61: StaticMesh'Suburbs_Floor_Stone_IND_E' (2 instances)
_mesh_path = "/Game/Art/Assets/Kits/Architecture/Suburbs/Suburbs_Floor_Stone_IND_E"
_materials = ['/Game/Art/Assets/Kits/Architecture/Suburbs/Materials/Suburbs_Floor_Stone_IND/MI_Suburbs_Floor_Stone_IND_MAT_Inst_Dest_RedRock']
_folder = "Reconstruction/BD_BB_Outdoor_TradingPost/Meshes"
a = spawn_static_mesh(_mesh_path, _materials, (6210.0, 9025.0, 360.0), (0.0, -4.999999999933509, 0.0), (1.0, 1.0, 1.0), "Suburbs_Floor_Stone_IND_E_197", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (6420.889, 8762.031, 359.64413), (0.0, 40.00002696525857, -0.0), (1.0, 1.0, 1.0), "Suburbs_Floor_Stone_IND_E2_209", _folder)
if a: placed += 1
else: skipped += 1

# Batch 62: StaticMesh'Suburbs_Floor_Stone_IND_E' (7 instances)
_mesh_path = "/Game/Art/Assets/Kits/Architecture/Suburbs/Suburbs_Floor_Stone_IND_E"
_materials = ['/Game/Art/Assets/Kits/Architecture/Suburbs/Materials/Suburbs_Floor_Stone_IND/MI_Suburbs_Floor_Stone_IND_MAT_Inst_Dest_RedRock']
_folder = "Reconstruction/BD_BB_Outdoor_TradingPost/Meshes"
a = spawn_static_mesh(_mesh_path, _materials, (5605.0127, 8602.845, 560.98334), (0.0, 40.00002696525857, -0.0), (1.0, 1.0, 1.0), "Suburbs_Floor_Stone_IND_E3_741", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5855.916, 8364.765, 560.57776), (0.0, -50.000000322548, 0.0), (1.0, 1.0, 1.0), "Suburbs_Floor_Stone_IND_E4_750", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5867.9834, 8738.116, 558.2511), (-0.05114745641993245, 0.1311491547746269, 2.114707358934076), (1.0, 1.0, 1.0), "Suburbs_Floor_Stone_IND_E5_759", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5554.8726, 8008.19, 559.88477), (0.0, 40.00002696525857, -0.0), (1.0, 1.0, 1.0), "Suburbs_Floor_Stone_IND_E6", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5423.165, 8208.089, 560.5777), (0.0, -141.03724621016366, 0.0), (1.0, 1.0, 1.0), "Suburbs_Floor_Stone_IND_E7", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5859.353, 8237.714, 559.058), (0.0, 40.00002696525857, -0.0), (1.0, 1.0, 1.0), "Suburbs_Floor_Stone_IND_E8", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5395.341, 7942.8223, 559.9898), (0.0, 40.00002696525857, -0.0), (1.0, 1.0, 1.0), "Suburbs_Floor_Stone_IND_E9", _folder)
if a: placed += 1
else: skipped += 1

# Batch 63: StaticMesh'Suburbs_Floor_Stone_IND_F' (1 instances)
_mesh_path = "/Game/Art/Assets/Kits/Architecture/Suburbs/Suburbs_Floor_Stone_IND_F"
_materials = ['/Game/Art/Assets/Kits/Architecture/Suburbs/Materials/Suburbs_Floor_Stone_IND/MI_Suburbs_Floor_Stone_IND_MAT_Inst_Dest_RedRock']
_folder = "Reconstruction/BD_BB_Outdoor_TradingPost/Meshes"
a = spawn_static_mesh(_mesh_path, _materials, (6341.4644, 8896.465, 360.0), (0.0, 44.9998338579472, -0.0), (1.0, 1.0, 1.0), "Suburbs_Floor_Stone_IND_F_194", _folder)
if a: placed += 1
else: skipped += 1

# Batch 64: StaticMesh'Suburbs_Floor_Stone_IND_F' (3 instances)
_mesh_path = "/Game/Art/Assets/Kits/Architecture/Suburbs/Suburbs_Floor_Stone_IND_F"
_materials = ['/Game/Art/Assets/Kits/Architecture/Suburbs/Materials/Suburbs_Floor_Stone_IND/MI_Suburbs_Floor_Stone_IND_MAT_Inst_Dest_RedRock']
_folder = "Reconstruction/BD_BB_Outdoor_TradingPost/Meshes"
a = spawn_static_mesh(_mesh_path, _materials, (5773.3813, 8253.525, 557.67365), (0.0, 0.0, -0.0), (1.0, 1.0, 1.0), "Suburbs_Floor_Stone_IND_F2_753", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5736.9746, 8610.495, 559.2402), (2.7918398232937873, 7.4097042729179925e-09, -2.882049405026924), (1.0, 1.0, 1.0), "Suburbs_Floor_Stone_IND_F3_762", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5043.771, 8086.6797, 559.14026), (2.6449143615132904, 38.9890336589626, -2.835815273282113), (1.0, 1.0, 1.0), "Suburbs_Floor_Stone_IND_F4", _folder)
if a: placed += 1
else: skipped += 1

# Batch 65: StaticMesh'Suburbs_Stairs_Medium_c2' (6 instances)
_mesh_path = "/Game/Art/Assets/Kits/Architecture/Suburbs/Suburbs_Stairs_Medium_c2"
_materials = ['/Game/Environments/Materials/MI_ArchitectureBase_NonDestructible_RedRock', '/Game/Art/Assets/Kits/Architecture/Suburbs/Materials/Suburbs_Stairs/MI_Suburbs_Stairs_elements_RedRock']
_folder = "Reconstruction/BD_BB_Outdoor_TradingPost/Meshes"
a = spawn_static_mesh(_mesh_path, _materials, (6361.0176, 9187.522, 150.0), (0.0, -48.56256091827546, 0.0), (1.0, 1.0, 1.0), "Ruins_Stairs_Medium_C5_843", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5199.1235, 7783.8584, 350.0), (0.0, 132.62864496523892, -0.0), (1.0, 1.0, 1.0), "Ruins_Stairs_Medium_C8", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (9850.0, 9449.105, 430.0), (0.0, 90.00007597449323, -0.0), (1.0, 1.0, 1.0), "Suburbs_Stairs_Medium_C_NonDest5_1628", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (9250.019, 9758.088, 230.85474), (0.0, 90.00007597449323, -0.0), (1.0, 1.0, 1.0), "Suburbs_Stairs_Medium_C_NonDest6", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (6097.384, 8581.497, 350.0), (0.0, -48.56256091827546, 0.0), (1.0, 1.0, 1.0), "Suburbs_Stairs_Small_C_NonDest4_74", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5899.3174, 8806.399, 350.0), (0.0, -48.56256091827546, 0.0), (1.0, 1.0, 1.0), "Suburbs_Stairs_Small_C_NonDest5", _folder)
if a: placed += 1
else: skipped += 1

# Batch 66: StaticMesh'Suburbs_Stairs_Small_C_CornerExt_NonDest' (2 instances)
_mesh_path = "/Game/Art/Assets/Kits/Architecture/Suburbs/Suburbs_Stairs_Small_C_CornerExt_NonDest"
_materials = ['/Game/Art/Assets/Kits/Architecture/Suburbs/Destructable/Materials/MI_Suburbs_Wall_Non_Dest', '/Game/Art/Assets/Kits/Architecture/Suburbs/Materials/Stairs_Medium_C_NonDest/MI_Stairs_Medium_C_NonDes_RedRock']
_folder = "Reconstruction/BD_BB_Outdoor_TradingPost/Meshes"
a = spawn_static_mesh(_mesh_path, _materials, (3999.257, 6702.8735, 302.21017), (0.0, -80.12580128149156, 0.0), (1.0, 1.0, 1.0), "Suburbs_Stairs_Small_C_CornerExt_NonDest2", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4102.132, 6111.761, 302.21017), (0.0, -170.12594258294118, 0.0), (1.0, 1.0, 1.0), "Suburbs_Stairs_Small_C_CornerExt_NonDest3", _folder)
if a: placed += 1
else: skipped += 1

# Batch 67: StaticMesh'Suburbs_Stairs_Small_C_NonDest' (4 instances)
_mesh_path = "/Game/Art/Assets/Kits/Architecture/Suburbs/Suburbs_Stairs_Small_C_NonDest"
_materials = ['/Game/Art/Assets/Kits/Architecture/Suburbs/Destructable/Materials/MI_Redrock_Wall_Non_Dest', '/Game/Art/Assets/Kits/Architecture/Suburbs/Materials/Stairs_Medium_C_NonDest/MI_Stairs_Medium_C_NonDes_RedRock']
_folder = "Reconstruction/BD_BB_Outdoor_TradingPost/Meshes"
a = spawn_static_mesh(_mesh_path, _materials, (12300.008, 9450.059, 700.0), (0.0, 90.00023965221622, -0.0), (1.0, 1.0, 1.0), "Suburbs_Stairs_Medium_C_NonDest_5", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (12300.007, 9750.059, 700.0), (0.0, 90.00023965221622, -0.0), (1.0, 1.0, 1.0), "Suburbs_Stairs_Medium_C_NonDest2", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (12150.008, 9450.059, 600.0), (0.0, 90.00023965221622, -0.0), (1.0, 1.0, 1.0), "Suburbs_Stairs_Medium_C_NonDest3", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (12150.008, 9750.059, 600.0), (0.0, 90.00023965221622, -0.0), (1.0, 1.0, 1.0), "Suburbs_Stairs_Medium_C_NonDest4", _folder)
if a: placed += 1
else: skipped += 1

# Batch 68: StaticMesh'Suburbs_Stairs_Small_C_NonDest' (2 instances)
_mesh_path = "/Game/Art/Assets/Kits/Architecture/Suburbs/Suburbs_Stairs_Small_C_NonDest"
_materials = ['/Game/Art/Assets/Kits/Architecture/Suburbs/Destructable/Materials/MI_Suburbs_Wall_Non_Dest', '/Game/Art/Assets/Kits/Architecture/Suburbs/Materials/Stairs_Medium_C_NonDest/MI_Stairs_Medium_C_NonDes_RedRock']
_folder = "Reconstruction/BD_BB_Outdoor_TradingPost/Meshes"
a = spawn_static_mesh(_mesh_path, _materials, (4024.9744, 6555.097, 302.21017), (0.0, -80.12580128149156, 0.0), (1.0, 1.0, 1.0), "Suburbs_Stairs_Small_C_NonDest11", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4076.4126, 6259.5386, 302.21017), (0.0, -80.12580128149156, 0.0), (1.0, 1.0, 1.0), "Suburbs_Stairs_Small_C_NonDest12", _folder)
if a: placed += 1
else: skipped += 1

# Batch 69: StaticMesh'Suburbs_Wall_Thick_3x3m_A' (4 instances)
_mesh_path = "/Game/Art/Assets/Kits/Architecture/Suburbs/Suburbs_Wall_Thick_3x3m_A"
_materials = ['/Game/Environments/Materials/MI_ArchitectureBase_NonDestructible_RedRock']
_folder = "Reconstruction/BD_BB_Outdoor_TradingPost/Meshes"
a = spawn_static_mesh(_mesh_path, _materials, (9400.0, 9900.0, 380.0), (0.0, 0.0, -89.99999818714215), (1.0, 1.0, 1.0), "NonDest_FloorBlock3m_3x11", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (9400.0, 9600.0, 380.0), (0.0, 0.0, -89.99999818714215), (1.0, 1.0, 1.0), "NonDest_FloorBlock3m_3x12_3", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (6543.9194, 8975.268, 300.0), (3.3154750514675267e-06, -48.561944720389064, -89.99999892182893), (1.0, 1.0, 1.0), "NonDest_FloorBlock3m_3x3_55", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (6345.377, 9200.168, 300.0), (3.3154750514675267e-06, -48.561944720389064, -89.99999892182893), (1.0, 1.0, 1.0), "NonDest_FloorBlock3m_3x4_1", _folder)
if a: placed += 1
else: skipped += 1

# Batch 70: StaticMesh'Defiled_Statues_B' (1 instances)
_mesh_path = "/Game/Art/Assets/Kits/Deco/Defiled/Defiled_Statues_B"
_materials = ['/Game/Art/Assets/Kits/Deco/Defiled/Materials/Defiled_Statues_A/MI_Defiled_Statues_A_Red']
_folder = "Reconstruction/BD_BB_Outdoor_TradingPost/Meshes"
a = spawn_static_mesh(_mesh_path, _materials, (6706.7217, 11711.925, 1069.949), (0.0, -132.0898504639728, 0.0), (4.8905935, 4.8905935, 4.8905935), "Defiled_Statues_C_A_1722", _folder)
if a: placed += 1
else: skipped += 1

# Batch 71: StaticMesh'Defiled_Statues_H_L' (1 instances)
_mesh_path = "/Game/Art/Assets/Kits/Deco/Defiled/Defiled_Statues_H_L"
_materials = ['/Game/Art/Assets/Kits/Deco/Defiled/Materials/Defiled_Statues_H/MI_Defiled_Statues_H_Outdoors_A']
_folder = "Reconstruction/BD_BB_Outdoor_TradingPost/Meshes"
a = spawn_static_mesh(_mesh_path, _materials, (12293.578, 10983.676, 1868.1145), (0.0, 96.65009064461914, -0.0), (5.45, 5.45, 5.45), "Defiled_Statues_H_L_2260", _folder)
if a: placed += 1
else: skipped += 1

# Batch 72: StaticMesh'Flora_Elven_Tree_A' (1 instances)
_mesh_path = "/Game/Art/Assets/Kits/Deco/Flora/Flora_Elven_Tree_A"
_materials = ['/Game/Art/Assets/Kits/Deco/Flora/Materials/Flora_Elven_Forest/MI_Flora_Elven_Forest_D', '/Game/Art/Assets/Kits/Deco/Flora/Materials/Flora_Elven_Forest/MI_Flora_Elven_Forest_C', '/Game/Art/Assets/Kits/Deco/Flora/Materials/Flora_Elven_Forest/MI_Flora_Elven_Forest_A', '/Game/Art/Assets/Kits/Deco/Flora/Materials/Flora_Elven_Forest/MI_Flora_Elven_Forest_B']
_folder = "Reconstruction/BD_BB_Outdoor_TradingPost/Meshes"
a = spawn_static_mesh(_mesh_path, _materials, (1936.0912, 9942.657, 2064.9229), (0.0, 59.99994310047553, -0.0), (3.0, 3.0, 3.0), "Flora_Elven_Tree_Mature8_2330", _folder)
if a: placed += 1
else: skipped += 1

# Batch 73: StaticMesh'Flora_Elven_Tree_Elder' (12 instances)
_mesh_path = "/Game/Art/Assets/Kits/Deco/Flora/Flora_Elven_Tree_Elder"
_materials = ['/Game/Art/Assets/GPI/Generator/Materials/MI_GPI_Tree_Bark', '/Game/Art/Assets/GPI/Generator/Materials/MI_GPI_TreeBranches_Mat_WPO']
_folder = "Reconstruction/BD_BB_Outdoor_TradingPost/Meshes"
a = spawn_static_mesh(_mesh_path, _materials, (10474.894, 2489.5405, 593.7528), (0.0, 0.0, -0.0), (1.747538, 1.747538, 1.747538), "Flora_Elven_Tree_Elder12_305", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3674.557, 7954.0605, 807.5635), (0.0, 0.0, -0.0), (1.327036, 1.327036, 1.327036), "Flora_Elven_Tree_Elder13_311", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (9150.0, 18650.0, 2200.0), (0.0, 0.0, -0.0), (1.5165085, 1.5165085, 1.5165085), "Flora_Elven_Tree_Elder4_242", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (7704.8164, 15492.541, 381.93237), (0.0, 0.0, -0.0), (1.0, 1.0, 1.0), "Flora_Elven_Tree_Elder5_1213", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (10191.803, 12399.975, 791.32916), (0.0, 0.0, -0.0), (1.0, 1.0, 1.0), "Flora_Elven_Tree_Elder6_260", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (7976.848, 4945.2095, 101.80194), (0.0, 0.0, -0.0), (1.0, 1.0, 1.0), "Flora_Elven_Tree_Mature20_1257", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (9424.927, 5448.6655, 1064.7195), (0.0, 0.0, -0.0), (1.224987, 1.224987, 1.224987), "Flora_Elven_Tree_Mature28_308", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (6697.276, 5362.5005, -0.14450073), (0.0, 0.0, -0.0), (1.0, 1.0, 1.0), "Flora_Elven_Tree_Middle_1254", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4536.4756, 16780.822, 1794.8615), (0.0, 0.0, -0.0), (1.0, 1.0, 1.0), "Flora_Elven_Tree_Middle14_1187", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5804.3955, 14450.978, 510.60217), (0.0, 0.0, -0.0), (1.0, 1.0, 1.0), "Flora_Elven_Tree_Middle18_1205", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4928.71, 13050.183, 2344.2983), (0.0, -85.00006134235026, 0.0), (1.0, 1.0, 1.0), "Flora_Elven_Tree_Middle5_2351", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (8602.895, 5007.3936, 326.32828), (-4.555358981501713, -117.26531707528706, -8.2779222995573), (1.0, 1.0, 1.0), "Flora_Elven_Tree_Young_630", _folder)
if a: placed += 1
else: skipped += 1

# Batch 74: StaticMesh'Flora_Elven_Tree_Mature' (12 instances)
_mesh_path = "/Game/Art/Assets/Kits/Deco/Flora/Flora_Elven_Tree_Mature"
_materials = ['/Game/Art/Assets/GPI/Generator/Materials/MI_GPI_Tree_Bark', '/Game/Art/Assets/GPI/Generator/Materials/MI_GPI_TreeBranches_Mat_WPO']
_folder = "Reconstruction/BD_BB_Outdoor_TradingPost/Meshes"
a = spawn_static_mesh(_mesh_path, _materials, (7477.8433, 7578.3257, 329.10098), (1.8677083401050445, 0.0, -0.0), (1.6542718, 1.6542718, 1.6542718), "Flora_Elven_Tree_Mature_68", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5523.983, 13223.926, 2697.7253), (0.0, 0.0, -0.0), (1.3731608, 1.3731608, 1.3731608), "Flora_Elven_Tree_Mature10_2348", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5343.3926, 18206.838, 2139.036), (0.0, 0.0, -0.0), (1.0, 1.0, 1.0), "Flora_Elven_Tree_Mature13_1202", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (8100.0, 17950.0, 1300.0), (0.0, 0.0, -0.0), (1.0, 1.0, 1.0), "Flora_Elven_Tree_Mature18_245", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (11431.065, 14502.278, 3500.0), (0.0, 34.45043013076725, -0.0), (1.3927222, 1.3927222, 1.3927222), "Flora_Elven_Tree_Mature19_248", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (9606.869, 6926.217, 903.9557), (1.8677078815560726, 0.0, -0.0), (1.313214, 1.313214, 1.313214), "Flora_Elven_Tree_Mature2", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4684.261, 14400.224, 2086.9814), (0.0, 0.0, -0.0), (1.3899804, 1.3899804, 1.3899804), "Flora_Elven_Tree_Mature21_257", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (8426.469, 6770.699, 1065.7845), (1.8677078815560726, 0.0, -0.0), (1.3737426, 1.3737426, 1.3737426), "Flora_Elven_Tree_Mature3", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (8278.892, 11049.803, 230.26935), (0.0, 0.0, -0.0), (1.0, 1.0, 1.0), "Flora_Elven_Tree_Mature4_1790", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5547.856, 3675.3396, 2066.4216), (0.0, 0.0, -0.0), (1.4440397, 1.4440397, 1.4440397), "Flora_Elven_Tree_Mature6_2319", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4239.39, 2797.8286, 2434.5002), (0.0, 0.0, -0.0), (1.0, 1.0, 1.0), "Flora_Elven_Tree_Mature7_2327", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (6344.3213, 11212.698, 1343.6686), (0.0, 0.0, -0.0), (1.0, 1.0, 1.0), "Flora_Elven_Tree_Mature9_2336", _folder)
if a: placed += 1
else: skipped += 1

# Batch 75: StaticMesh'Flora_Elven_Tree_Middle' (12 instances)
_mesh_path = "/Game/Art/Assets/Kits/Deco/Flora/Flora_Elven_Tree_Middle"
_materials = ['/Game/Art/Assets/GPI/Generator/Materials/MI_GPI_Tree_Bark', '/Game/Art/Assets/GPI/Generator/Materials/MI_GPI_TreeBranches_Mat_WPO']
_folder = "Reconstruction/BD_BB_Outdoor_TradingPost/Meshes"
a = spawn_static_mesh(_mesh_path, _materials, (4675.1294, 3873.7566, 1258.093), (0.0, -129.6588013908281, 0.0), (1.0, 1.0, 1.0), "Flora_Elven_Tree_Middle13_1302", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4744.9214, 16154.738, 1628.9042), (0.0, 0.0, -0.0), (1.0, 1.0, 1.0), "Flora_Elven_Tree_Middle15_1190", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5033.849, 18484.613, 3098.9832), (0.0, 0.0, -0.0), (1.0, 1.0, 1.0), "Flora_Elven_Tree_Middle16_1193", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3206.2144, 16524.885, 2901.337), (0.0, 0.0, -0.0), (1.0, 1.0, 1.0), "Flora_Elven_Tree_Middle17_1199", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5927.6606, 17034.055, 447.1991), (0.0, 0.0, -0.0), (1.0, 1.0, 1.0), "Flora_Elven_Tree_Middle19_1209", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5800.0, 11100.0, 1862.0901), (0.0, 0.0, -0.0), (1.0, 1.0, 1.0), "Flora_Elven_Tree_Middle4_2126", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4189.158, 4766.001, 1497.5577), (0.0, 0.0, -0.0), (1.0, 1.0, 1.0), "Flora_Elven_Tree_Middle8_1293", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (11646.138, 13288.1045, 1622.7563), (0.0, 34.45043013076725, -0.0), (1.5997818, 1.5997818, 1.5997818), "Flora_Elven_Tree_Middle9_269", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (6867.7227, 12278.685, 1704.6715), (0.0, 0.0, -0.0), (1.0, 1.0, 1.0), "Flora_Elven_Tree_Sapling4_1787", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (10331.3545, 6061.9277, 1042.2751), (0.0, 0.0, -0.0), (1.0, 1.0, 1.0), "Flora_Elven_Tree_Sapling5_711", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (6578.9766, 11302.016, 1090.4729), (0.0, 0.0, -0.0), (0.96518254, 0.96518254, 0.96518254), "Flora_Elven_Tree_Young4_1815", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5757.6494, 4622.137, 1043.7548), (0.0, 0.0, -0.0), (1.0, 1.0, 1.0), "Flora_Elven_Tree_Young9_1279", _folder)
if a: placed += 1
else: skipped += 1

# Batch 76: StaticMesh'Flora_Elven_Tree_Sapling' (3 instances)
_mesh_path = "/Game/Art/Assets/Kits/Deco/Flora/Flora_Elven_Tree_Sapling"
_materials = ['/Game/Art/Assets/GPI/Generator/Materials/MI_GPI_Tree_Bark', '/Game/Art/Assets/GPI/Generator/Materials/MI_GPI_TreeBranches_Mat_WPO']
_folder = "Reconstruction/BD_BB_Outdoor_TradingPost/Meshes"
a = spawn_static_mesh(_mesh_path, _materials, (7930.0, 7313.3047, 1035.4304), (0.0, 0.0, -0.0), (3.4230285, 3.4230285, 3.4230285), "Flora_Elven_Tree_Sapling_59", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (8112.282, 6809.837, 1318.731), (0.0, 0.0, -0.0), (4.6008477, 4.6008477, 4.6008477), "Flora_Elven_Tree_Sapling2", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (9086.236, 6799.2207, 763.79205), (0.0, 0.0, -0.0), (3.423028, 3.423028, 3.423028), "Flora_Elven_Tree_Sapling3", _folder)
if a: placed += 1
else: skipped += 1

# Batch 77: StaticMesh'Flora_Elven_Tree_Young' (9 instances)
_mesh_path = "/Game/Art/Assets/Kits/Deco/Flora/Flora_Elven_Tree_Young"
_materials = ['/Game/Art/Assets/GPI/Generator/Materials/MI_GPI_Tree_Bark', '/Game/Art/Assets/GPI/Generator/Materials/MI_GPI_TreeBranches_Mat_WPO']
_folder = "Reconstruction/BD_BB_Outdoor_TradingPost/Meshes"
a = spawn_static_mesh(_mesh_path, _materials, (5443.867, 4684.361, 781.0863), (0.0, 0.0, -0.0), (1.0, 1.0, 1.0), "Flora_Elven_Tree_Middle2_1276", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (7086.624, 12004.47, 726.5678), (0.0, 0.0, -0.0), (1.0, 1.0, 1.0), "Flora_Elven_Tree_Middle3_1809", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3904.1194, 5445.281, 1485.5724), (0.0, 0.0, -0.0), (1.0, 1.0, 1.0), "Flora_Elven_Tree_Young10_1296", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3667.4766, 17274.287, 3699.3713), (0.0, 0.0, -0.0), (1.0, 1.0, 1.0), "Flora_Elven_Tree_Young11_1196", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (7533.728, 7183.3984, 540.7771), (0.0, 0.0, -0.0), (2.8278313, 2.8278313, 2.8278313), "Flora_Elven_Tree_Young2_62", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (6256.952, 11035.02, 1356.177), (0.0, 0.0, -0.0), (1.0, 1.0, 1.0), "Flora_Elven_Tree_Young3_1784", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3792.6448, 3781.037, 2114.6782), (0.0, -29.99999868431647, 0.0), (1.6124773, 1.6124773, 1.6124773), "Flora_Elven_Tree_Young6_2323", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5024.4976, 11248.771, 2176.8057), (0.0, 0.0, -0.0), (1.4753518, 1.4753518, 1.4753518), "Flora_Elven_Tree_Young7_2333", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (6938.46, 12781.872, 1480.8542), (0.0, 0.0, -0.0), (1.0, 1.0, 1.0), "Flora_Elven_Tree_Young8_2339", _folder)
if a: placed += 1
else: skipped += 1

# Batch 78: StaticMesh'Ground_Roots_A' (7 instances)
_mesh_path = "/Game/Art/Assets/Kits/Deco/Flora/Ground_Roots_A"
_materials = ['/Game/Unshippable/ThirdParty/MWConiferForest/Materials/Trees/MTL_Holly_Tree', '/Game/Unshippable/ThirdParty/MWConiferForest/Materials/Trees/MTL_Holly_Tree']
_folder = "Reconstruction/BD_BB_Outdoor_TradingPost/Meshes"
a = spawn_static_mesh(_mesh_path, _materials, (7099.3066, 10619.732, 261.9086), (-8.753508990266688, 50.93225783774721, -14.900206939359538), (1.0, 1.0, 1.0), "Ground_Roots_A_1044", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (8710.369, 7355.678, 273.12564), (13.49915084114665, -29.399293891664136, 22.50345003177548), (0.5182799, 0.5182799, 0.5182799), "Ground_Roots_A2_1101", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5030.802, 5989.1973, 344.94275), (-1.610150050686932e-07, 129.9999732290445, 20.000239999655825), (0.46220553, 0.46220553, 0.46220553), "Ground_Roots_A4_1636", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5995.5522, 5139.085, 375.4207), (-8.60544334724181e-07, 79.99996018270188, 20.000011356999725), (0.5435654, 0.5435654, 0.5435654), "Ground_Roots_A5_1645", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4024.13, 10710.706, 619.0143), (1.3660376334682623e-05, 20.000029202029296, 7.867813216586633e-05), (0.53279394, 0.53279394, 0.53279394), "Ground_Roots_A6_712", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5117.9146, 10653.178, 634.9433), (1.400000139621566e-05, -79.99996838941739, 7.90000089099751e-05), (0.532794, 0.532794, 0.532794), "Ground_Roots_A7", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (9060.193, 12274.732, 718.49976), (-12.68307724512096, -24.184967691535807, 20.123622150841936), (1.0, 1.0, 1.0), "Ground_Roots_B4", _folder)
if a: placed += 1
else: skipped += 1

# Batch 79: StaticMesh'Ground_Roots_A' (1 instances)
_mesh_path = "/Game/Art/Assets/Kits/Deco/Flora/Ground_Roots_A"
_materials = ['/Game/Art/Assets/Kits/Deco/Flora/Materials/Roots_Tileable_Inst', '/Game/Unshippable/ThirdParty/MWConiferForest/Materials/Trees/MTL_Holly_Tree']
_folder = "Reconstruction/BD_BB_Outdoor_TradingPost/Meshes"
a = spawn_static_mesh(_mesh_path, _materials, (7007.4995, 8617.091, 169.86778), (-1.4454651750152585, -52.92837383080116, 15.640322191504659), (0.63585097, 0.63585097, 0.63585097), "Ground_Roots_A3_1489", _folder)
if a: placed += 1
else: skipped += 1

# Batch 80: StaticMesh'Ground_Roots_B' (10 instances)
_mesh_path = "/Game/Art/Assets/Kits/Deco/Flora/Ground_Roots_B"
_materials = ['/Game/Unshippable/ThirdParty/MWConiferForest/Materials/Trees/MTL_Holly_Tree']
_folder = "Reconstruction/BD_BB_Outdoor_TradingPost/Meshes"
a = spawn_static_mesh(_mesh_path, _materials, (11084.373, 10789.658, 676.12317), (8.771941315297457, 138.8568555317741, 14.4272516770767), (0.89071715, 0.89071715, 0.89071715), "Ground_Roots_B_41", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3967.51, 10820.812, 662.56494), (6.223402254522221e-07, -25.000031276536756, 44.99997316989288), (0.78383225, 0.78383225, 0.78383225), "Ground_Roots_B10_715", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5236.179, 10689.817, 678.49396), (-6.981937638558664e-07, -125.00007994889792, 44.99996949009538), (0.783832, 0.783832, 0.783832), "Ground_Roots_B11", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (11139.39, 10788.355, 681.39307), (-7.164305093925863e-08, -145.65615680539034, 15.75722930442866), (1.0, 1.0, 1.0), "Ground_Roots_B2_44", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (9037.634, 12210.168, 751.8526), (17.889602882134906, -85.60815751060326, 24.486500066102522), (1.0, 1.0, 1.0), "Ground_Roots_B3_720", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (6928.053, 10752.725, 388.9329), (-24.630309603635407, -42.41546250981146, 29.843685415271196), (1.0, 1.0, 1.0), "Ground_Roots_B5_1047", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (8649.177, 7329.538, 291.75793), (23.515510119547166, 49.86831728337167, 27.649693540870313), (0.79262686, 0.79262686, 0.79262686), "Ground_Roots_B6_1098", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (6948.426, 8626.9, 189.00772), (0.0, 0.0, 25.432461505730803), (0.9672091, 0.9672091, 0.9672091), "Ground_Roots_B7_1492", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5042.4326, 6023.8794, 367.29547), (-1.9645829062664682e-07, 45.00003129748377, 24.999919819543436), (0.6186628, 0.6186628, 0.6186628), "Ground_Roots_B8_1639", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (6027.462, 5156.91, 399.40103), (8.2860168632318, 18.39533240128893, 26.360452067837343), (0.6258282, 0.6258282, 0.6258282), "Ground_Roots_B9_1642", _folder)
if a: placed += 1
else: skipped += 1

# Batch 81: StaticMesh'Holly_Tree_A' (7 instances)
_mesh_path = "/Game/Art/Assets/Kits/Deco/Flora/Holly_Tree_A"
_materials = ['/Game/Unshippable/Cinematics/Cine001/Environment/Materials/MI_Tree_15', '/Game/Unshippable/ThirdParty/MWConiferForest/Materials/Trees/MTL_Holly_Tree', '/Game/Art/Assets/Kits/Misc/Vegetation/Materials/MI_Holly_Tree_Canopy', '/Game/Art/Assets/Kits/Misc/Vegetation/Materials/MI_Holly_Tree_Canopy', '/Game/Unshippable/Cinematics/Cine001/Environment/Materials/MI_Tree_15']
_folder = "Reconstruction/BD_BB_Outdoor_TradingPost/Meshes"
a = spawn_static_mesh(_mesh_path, _materials, (9033.295, 12214.252, 720.7063), (0.0, -35.514346773176165, 0.0), (1.8187861, 1.8187861, 1.8187861), "Holly_Tree_A2_14", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (8092.649, 7646.9844, 281.66122), (0.0, -18.966979348712943, 0.0), (1.0, 1.0, 1.0), "Holly_Tree_A3_661", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5045.57, 6024.1016, 337.236), (0.0, -6.487610074276147, 0.0), (1.0, 1.0, 1.0), "Holly_Tree_A4_1365", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (6204.0435, 6732.107, 89.95201), (0.0, 0.0, -0.0), (1.0, 1.0, 1.0), "Holly_Tree_A5_693", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (6955.56, 8599.727, 176.16345), (0.0, -10.00012155996466, 0.0), (1.5146723, 1.5146723, 1.5146723), "Holly_Tree_B3_1857", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (6031.963, 5127.115, 296.17615), (0.0, 116.97387363705322, -0.0), (1.7320226, 1.7320226, 1.7320226), "Holly_Tree_C_5", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5220.671, 10682.79, 606.32385), (0.0, -80.00009250264795, 0.0), (1.0, 1.0, 1.0), "Holly_Tree_C3_705", _folder)
if a: placed += 1
else: skipped += 1

# Batch 82: StaticMesh'Holly_Tree_B' (4 instances)
_mesh_path = "/Game/Art/Assets/Kits/Deco/Flora/Holly_Tree_B"
_materials = ['/Game/Unshippable/ThirdParty/MWConiferForest/Materials/Trees/MTL_Holly_Tree', '/Game/Art/Assets/Kits/Misc/Vegetation/Materials/MI_Holly_Tree_Canopy', '/Game/Unshippable/ThirdParty/MWConiferForest/Materials/Trees/MTL_Holly_Tree', '/Game/Art/Assets/Kits/Misc/Vegetation/Materials/MI_Holly_Tree_Canopy']
_folder = "Reconstruction/BD_BB_Outdoor_TradingPost/Meshes"
a = spawn_static_mesh(_mesh_path, _materials, (11080.101, 10810.586, 621.30554), (0.0, 61.19508661134642, -0.0), (1.224994, 1.224994, 1.224994), "Holly_Tree_B_1538", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (8683.287, 7336.2363, 266.29724), (0.0, -55.30731066663754, 0.0), (1.0, 1.0, 1.0), "Holly_Tree_B2_658", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (7820.459, 5808.2197, 135.15625), (0.0, 0.0, -0.0), (1.0, 1.0, 1.0), "Holly_Tree_B4_696", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (6031.653, 14993.912, 515.0914), (0.0, 0.0, -0.0), (1.0, 1.0, 1.0), "Holly_Tree_B5_1071", _folder)
if a: placed += 1
else: skipped += 1

# Batch 83: StaticMesh'Holly_Tree_C' (4 instances)
_mesh_path = "/Game/Art/Assets/Kits/Deco/Flora/Holly_Tree_C"
_materials = ['/Game/Unshippable/ThirdParty/MWConiferForest/Materials/Trees/MTL_Holly_Tree', '/Game/Art/Assets/Kits/Misc/Vegetation/Materials/MI_Holly_Tree_Canopy', '/Game/Unshippable/ThirdParty/MWConiferForest/Materials/Trees/MTL_Holly_Tree', '/Game/Art/Assets/Kits/Misc/Vegetation/Materials/MI_Holly_Tree_Canopy']
_folder = "Reconstruction/BD_BB_Outdoor_TradingPost/Meshes"
a = spawn_static_mesh(_mesh_path, _materials, (6933.2773, 10723.902, 306.5545), (0.0, 166.5801765115927, -0.0), (1.2357382, 1.2357382, 1.2357382), "Holly_Tree_A_2", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3957.8345, 10798.569, 619.36993), (0.0, -84.999936913957, 0.0), (1.0, 1.0, 1.0), "Holly_Tree_A6_702", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (7162.1104, 7032.457, -86.27692), (0.0, 10.000096064206778, -0.0), (0.82427764, 0.82427764, 0.82427764), "Holly_Tree_C2_699", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (7353.6504, 17145.213, 547.45966), (0.0, 0.0, -0.0), (1.0, 1.0, 1.0), "Holly_Tree_C4_1074", _folder)
if a: placed += 1
else: skipped += 1

# Batch 84: StaticMesh'Roots_A' (1 instances)
_mesh_path = "/Game/Art/Assets/Kits/Deco/Flora/Roots_A"
_materials = ['/Game/Unshippable/ThirdParty/MWConiferForest/Materials/Trees/MTL_Holly_Tree']
_folder = "Reconstruction/BD_BB_Outdoor_TradingPost/Meshes"
a = spawn_static_mesh(_mesh_path, _materials, (11082.83, 10852.731, 688.53253), (67.94236926176927, -169.8764547639463, 169.52349109664988), (0.8998785, 0.8998785, 0.8998785), "Roots_E_37", _folder)
if a: placed += 1
else: skipped += 1

# Batch 85: StaticMesh'Garden_Hydroponic_Shelf' (1 instances)
_mesh_path = "/Game/Art/Assets/Kits/Deco/Garden/Garden_Hydroponic_Shelf"
_materials = ['/Game/Art/Assets/Kits/Deco/Garden/Materials/Garden_Hydroponic_Shelf/MI_Garden_Hydroponic_Shelf']
_folder = "Reconstruction/BD_BB_Outdoor_TradingPost/Meshes"
a = spawn_static_mesh(_mesh_path, _materials, (11212.666, 9299.541, 670.32996), (0.0, 0.0, -0.0), (1.0, 1.0, 1.0), "Garden_Hydroponic_Shelf_515", _folder)
if a: placed += 1
else: skipped += 1

# Batch 86: StaticMesh'Mines_Lift_Barrel_A' (24 instances)
_mesh_path = "/Game/Art/Assets/Kits/Deco/Mines/Machine/Mines_Machine_Lift_Pieces/Mines_Lift_Barrel_A"
_materials = ['/Game/Art/Assets/Kits/Deco/Mines/Machine/Mines_Machine_Lift_Pieces/Materials/Mi_Mines_Machine_Lift_G']
_folder = "Reconstruction/BD_BB_Outdoor_TradingPost/Meshes"
a = spawn_static_mesh(_mesh_path, _materials, (11594.238, 9955.138, 644.7179), (-2.812859517167667e-07, 11.986650695091368, -89.99993790654702), (1.0, 1.0, 1.0), "Mines_Lift_Barrel_A_1437", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (12149.216, 9181.632, 831.7462), (-90.0, 23.43604092199967, -113.43724184163429), (1.0, 1.0, 1.0), "Mines_Lift_Barrel_A10", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (12149.215, 9079.755, 804.69006), (-90.0, 23.43604092199967, -113.43724184163429), (1.0, 1.0, 1.0), "Mines_Lift_Barrel_A11", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (12149.233, 9039.128, 863.0949), (-90.0, 23.43604092199967, -113.43724184163429), (1.0, 1.0, 1.0), "Mines_Lift_Barrel_A12", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (12149.233, 9117.595, 864.147), (-90.0, 23.43604092199967, -113.43724184163429), (1.0, 1.0, 1.0), "Mines_Lift_Barrel_A13", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (12149.213, 9075.042, 922.8194), (-90.0, 23.43604092199967, -113.43724184163429), (1.0, 1.0, 1.0), "Mines_Lift_Barrel_A14", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (12149.242, 9986.286, 773.91254), (-90.0, 7.128399463311968, 82.87060359002484), (1.0, 1.0, 1.0), "Mines_Lift_Barrel_A15", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (12149.232, 10061.95, 773.91254), (-90.0, 7.128399463311968, 82.87060359002484), (1.0, 1.0, 1.0), "Mines_Lift_Barrel_A16", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (12149.242, 10186.981, 773.91254), (-90.0, 7.128399463311968, 82.87060359002484), (1.0, 1.0, 1.0), "Mines_Lift_Barrel_A17", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (12149.245, 10264.633, 773.91254), (-90.0, 7.128399463311968, 82.87060359002484), (1.0, 1.0, 1.0), "Mines_Lift_Barrel_A18", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (12149.234, 10228.539, 831.74615), (-90.0, 7.128399463311968, 82.87060359002484), (1.0, 1.0, 1.0), "Mines_Lift_Barrel_A19", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (11266.835, 10056.285, 644.7185), (-2.812859517167667e-07, 11.986650695091368, -89.99993790654702), (1.0, 1.0, 1.0), "Mines_Lift_Barrel_A2", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (12149.218, 10124.001, 804.69), (-90.0, 7.128399463311968, 82.87060359002484), (1.0, 1.0, 1.0), "Mines_Lift_Barrel_A20", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (12149.199, 10164.627, 863.09485), (-90.0, 7.128399463311968, 82.87060359002484), (1.0, 1.0, 1.0), "Mines_Lift_Barrel_A21", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (12149.2, 10086.161, 864.1469), (-90.0, 7.128399463311968, 82.87060359002484), (1.0, 1.0, 1.0), "Mines_Lift_Barrel_A22", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (12149.222, 10128.713, 922.81934), (-90.0, 45.034679263957294, 44.96434097812487), (1.0, 1.0, 1.0), "Mines_Lift_Barrel_A23", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (12149.245, 10027.561, 831.74615), (-90.0, 26.582407263498972, 63.416595789837835), (1.0, 1.0, 1.0), "Mines_Lift_Barrel_A24", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (11823.969, 8942.126, 653.53107), (0.0, 0.0, -90.00002735739477), (1.0, 1.0, 1.0), "Mines_Lift_Barrel_A3_26", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (11499.32, 9257.802, 652.117), (0.0, 0.0, -90.00002735739477), (1.0, 1.0, 1.0), "Mines_Lift_Barrel_A4", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (12149.192, 9217.469, 773.9126), (-90.0, 26.58540449350996, -116.58658707854097), (1.0, 1.0, 1.0), "Mines_Lift_Barrel_A5_586", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (12149.202, 9141.806, 773.9126), (-90.0, 23.43604092199967, -113.43724184163429), (1.0, 1.0, 1.0), "Mines_Lift_Barrel_A6", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (12149.192, 9016.773, 773.9126), (-90.0, 23.43604092199967, -113.43724184163429), (1.0, 1.0, 1.0), "Mines_Lift_Barrel_A7", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (12149.189, 8939.12, 773.9126), (-90.0, 23.43604092199967, -113.43724184163429), (1.0, 1.0, 1.0), "Mines_Lift_Barrel_A8", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (12149.2, 8975.216, 831.7462), (-90.0, 23.43604092199967, -113.43724184163429), (1.0, 1.0, 1.0), "Mines_Lift_Barrel_A9", _folder)
if a: placed += 1
else: skipped += 1

# Batch 87: StaticMesh'Mines_Wagon' (7 instances)
_mesh_path = "/Game/Art/Assets/Kits/Deco/Mines/Mines_Wagon"
_materials = ['/Game/Art/Assets/Kits/Deco/Mines/Materials/Mines_WagonCart/MI_Mines_WagonCart_Trim', '/Game/Art/Assets/Kits/Deco/Mines/Materials/Mines_WagonCart/MI_Mines_WagonCart']
_folder = "Reconstruction/BD_BB_Outdoor_TradingPost/Meshes"
a = spawn_static_mesh(_mesh_path, _materials, (11209.168, 10320.164, 598.6532), (0.9510087882393131, 72.71019742551766, -1.7054749214541975), (1.0, 1.0, 1.0), "Mines_Wagon_1442", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (9422.38, 12981.925, 699.4635), (0.0, 103.0457069669283, -0.0), (1.0, 1.0, 1.0), "Mines_Wagon2_755", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (10959.321, 6306.7744, 598.9216), (-0.42501841021787556, -59.866117014547925, -1.9148863570873067), (1.0, 1.0, 1.0), "Mines_Wagon3_1087", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4507.246, 5312.6157, 352.28888), (2.2544402275368745, -153.22374627040935, 4.169152142324198), (1.0, 1.0, 1.0), "Mines_Wagon4_1240", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4556.312, 5035.2075, 348.21326), (0.5389906222968074, -141.26358998447694, 2.261074962866761), (1.0, 1.0, 1.0), "Mines_Wagon5", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5054.341, 4813.3096, 348.36438), (1.2991372232335563, -89.87878284312545, -2.4836119415128612), (1.0, 1.0, 1.0), "Mines_Wagon6", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4827.847, 4876.2075, 342.3051), (0.0, -112.89672354489592, 0.0), (1.0, 1.0, 1.0), "Mines_Wagon7", _folder)
if a: placed += 1
else: skipped += 1

# Batch 88: StaticMesh'Orc_Shanty_Junkhoards_A' (3 instances)
_mesh_path = "/Game/Art/Assets/Kits/Deco/Orc/Shanty/Orc_Shanty_Junkhoards_A"
_materials = ['/Game/Art/Assets/Kits/Deco/Orc/Shanty/Material/Orc_Shanty_Junkhoards/Orc_Shanty_Junkhoards_A']
_folder = "Reconstruction/BD_BB_Outdoor_TradingPost/Meshes"
a = spawn_static_mesh(_mesh_path, _materials, (11485.604, 9251.597, 699.5955), (0.0, 0.0, -0.0), (1.0, 1.0, 1.0), "Orc_Shanty_Junkhoards_A_518", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (11477.32, 9256.231, 699.5955), (0.0, 0.0, -0.0), (1.0, 1.0, 1.0), "Orc_Shanty_Junkhoards_A2_521", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (11483.53, 9256.261, 699.5955), (0.0, 0.0, -0.0), (1.0, 1.0, 1.0), "Orc_Shanty_Junkhoards_A3_524", _folder)
if a: placed += 1
else: skipped += 1

# Batch 89: StaticMesh'Orc_Shanty_Junkhoards_B' (1 instances)
_mesh_path = "/Game/Art/Assets/Kits/Deco/Orc/Shanty/Orc_Shanty_Junkhoards_B"
_materials = ['/Game/Art/Assets/Kits/Deco/Orc/Shanty/Material/Orc_Shanty_Junkhoards/Orc_Shanty_Junkhoards_B']
_folder = "Reconstruction/BD_BB_Outdoor_TradingPost/Meshes"
a = spawn_static_mesh(_mesh_path, _materials, (11491.851, 9275.475, 699.5956), (0.0, 0.0, -0.0), (1.0, 1.0, 1.0), "Orc_Shanty_Junkhoards_B_527", _folder)
if a: placed += 1
else: skipped += 1

# Batch 90: StaticMesh'Orc_Shanty_Junkhoards_C' (1 instances)
_mesh_path = "/Game/Art/Assets/Kits/Deco/Orc/Shanty/Orc_Shanty_Junkhoards_C"
_materials = ['/Game/Art/Assets/Kits/Deco/Orc/Shanty/Material/Orc_Shanty_Junkhoards/Orc_Shanty_Junkhoards_C']
_folder = "Reconstruction/BD_BB_Outdoor_TradingPost/Meshes"
a = spawn_static_mesh(_mesh_path, _materials, (11509.136, 9265.821, 699.5955), (0.0, 0.0, -0.0), (1.0, 1.0, 1.0), "Orc_Shanty_Junkhoards_C_530", _folder)
if a: placed += 1
else: skipped += 1

# Batch 91: StaticMesh'Orc_Shanty_Junkhoards_D' (2 instances)
_mesh_path = "/Game/Art/Assets/Kits/Deco/Orc/Shanty/Orc_Shanty_Junkhoards_D"
_materials = ['/Game/Art/Assets/Kits/Deco/Orc/Shanty/Material/Orc_Shanty_Junkhoards/Orc_Shanty_Junkhoards_D']
_folder = "Reconstruction/BD_BB_Outdoor_TradingPost/Meshes"
a = spawn_static_mesh(_mesh_path, _materials, (11495.188, 9239.05, 699.5955), (0.0, 0.0, -0.0), (1.0, 1.0, 1.0), "Orc_Shanty_Junkhoards_D_533", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (11502.479, 9238.305, 699.5955), (0.0, 0.0, -0.0), (1.0, 1.0, 1.0), "Orc_Shanty_Junkhoards_D2_536", _folder)
if a: placed += 1
else: skipped += 1

# Batch 92: StaticMesh'Rubble_Masonry_Mound_Pile_B' (8 instances)
_mesh_path = "/Game/Art/Assets/Kits/Deco/Rubble/Rubble_Masonry_Mound_Pile_B"
_materials = ['/Game/Art/Assets/Kits/Deco/Rubble/Materials/Rubble_Masonry_Pile/MI_Rubble_Masonry_Pile_Atlas_Inst_B_RedRock']
_folder = "Reconstruction/BD_BB_Outdoor_TradingPost/Meshes"
a = spawn_static_mesh(_mesh_path, _materials, (9261.12, 13431.36, 691.4118), (0.0, 72.30966606739119, -0.0), (4.2026434, 4.2026434, 4.2026434), "Rubble_Masonry_Mound_Pile_B_46", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (10250.872, 13675.765, 700.00256), (0.0, 137.45453861823628, -0.0), (4.202643, 4.202643, 4.202643), "Rubble_Masonry_Mound_Pile_B2", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (10980.539, 5655.831, 608.4535), (0.0, 15.562626638327384, -0.0), (4.919739, 4.919739, 4.919739), "Rubble_Masonry_Mound_Pile_B3_6", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (11512.512, 5700.2363, 770.79944), (16.83012685179935, -17.51898238937422, 4.8326324472543), (4.919739, 4.919739, 4.919739), "Rubble_Masonry_Mound_Pile_B4", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (11214.605, 5198.9175, 894.17377), (-3.382085678508563e-08, 15.562917191785443, 29.695508443459737), (4.919739, 4.919739, 4.919739), "Rubble_Masonry_Mound_Pile_B5", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (10796.4795, 4840.64, 981.97), (16.83012397219352, -17.51901401888026, 9.77871208832572), (4.919739, 4.919739, 4.919739), "Rubble_Masonry_Mound_Pile_B6", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (10157.595, 5149.0894, 870.1423), (-3.382085678508563e-08, 15.562917191785443, 29.695508443459737), (4.919739, 4.919739, 4.919739), "Rubble_Masonry_Mound_Pile_B7", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (10394.179, 13522.019, 700.0008), (5.128979789476196, 115.57437101287348, 4.809639994264736), (4.202643, 4.202643, 4.202643), "Rubble_Masonry_Mound_Pile_B8", _folder)
if a: placed += 1
else: skipped += 1

# Batch 93: StaticMesh'Rubble_Masonry_Mound_Pile_D' (1 instances)
_mesh_path = "/Game/Art/Assets/Kits/Deco/Rubble/Rubble_Masonry_Mound_Pile_D"
_materials = ['/Game/Art/Assets/Kits/Deco/Rubble/Materials/Rubble_Masonry_Pile/MI_Rubble_Masonry_Pile_Atlas_Inst_B']
_folder = "Reconstruction/BD_BB_Outdoor_TradingPost/Meshes"
a = spawn_static_mesh(_mesh_path, _materials, (10450.774, 13817.835, 693.1964), (0.0, 34.45043013076725, -0.0), (3.3429568, 3.3429568, 3.3429568), "Rubble_Masonry_Mound_Pile_D2_33", _folder)
if a: placed += 1
else: skipped += 1

# Batch 94: StaticMesh'Rubble_Masonry_Pile_D' (1 instances)
_mesh_path = "/Game/Art/Assets/Kits/Deco/Rubble/Rubble_Masonry_Pile_D"
_materials = ['/Game/Art/Assets/Kits/Deco/Rubble/Materials/Rubble_Masonry_Pile/MI_Rubble_Masonry_Pile_Atlas_Inst_A_RedRock', '/Game/Art/Assets/Kits/Deco/Rubble/Materials/Rubble_Masonry_Pile/MI_Rubble_Masonry_Pile_Atlas_Inst_B_RedRock']
_folder = "Reconstruction/BD_BB_Outdoor_TradingPost/Meshes"
a = spawn_static_mesh(_mesh_path, _materials, (11260.901, 6208.817, 601.8477), (0.0, 46.13140729014023, -0.0), (1.0996963, 1.0996963, 1.0996963), "Rubble_Masonry_Pile_D_518", _folder)
if a: placed += 1
else: skipped += 1

# Batch 95: StaticMesh'Rubble_Masonry_Pile_E' (13 instances)
_mesh_path = "/Game/Art/Assets/Kits/Deco/Rubble/Rubble_Masonry_Pile_E"
_materials = ['/Game/Art/Assets/Kits/Deco/Rubble/Materials/Rubble_Masonry_Pile/MI_Rubble_Masonry_Pile_Atlas_Inst_A_RedRock', '/Game/Art/Assets/Kits/Deco/Rubble/Materials/Rubble_Masonry_Pile/MI_Rubble_Masonry_Pile_Atlas_Inst_B_RedRock']
_folder = "Reconstruction/BD_BB_Outdoor_TradingPost/Meshes"
a = spawn_static_mesh(_mesh_path, _materials, (11101.176, 5873.1543, 595.2843), (0.0, -28.279755657322482, 0.0), (2.6846035, 2.6846035, 2.6846035), "Rubble_Masonry_Pile_E_521", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (10323.075, 5195.6953, 819.0005), (11.029996138102414, -102.6777961526949, 5.936525384463756), (2.684603, 2.684603, 2.684603), "Rubble_Masonry_Pile_E10", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (11967.067, 5583.5625, 1014.8733), (22.81090812547471, -27.32085737165074, 2.285110458472124), (2.684603, 2.684603, 2.684603), "Rubble_Masonry_Pile_E11", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (11967.309, 5797.911, 999.2115), (26.875190648158796, -22.90106377480131, 11.764583516839968), (2.684603, 2.684603, 2.684603), "Rubble_Masonry_Pile_E12", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (11091.832, 5289.8745, 746.9476), (14.028211616269198, -27.680998350025774, 4.585364625932523), (2.684603, 2.684603, 2.684603), "Rubble_Masonry_Pile_E13", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (11445.334, 5335.87, 826.7856), (29.810073472621067, -30.11010526011594, -11.724150388018394), (2.684603, 2.684603, 2.684603), "Rubble_Masonry_Pile_E2", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (10818.44, 5481.3057, 616.7556), (2.374555721957545, -28.188045039571595, 4.420686390911947), (2.684603, 2.684603, 2.684603), "Rubble_Masonry_Pile_E3", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (10684.653, 5268.128, 706.6717), (-3.9172977224745025, -28.351898420309393, 2.1112356385178024), (2.684603, 2.684603, 2.684603), "Rubble_Masonry_Pile_E4", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (11714.711, 5870.869, 779.3426), (20.055057610171055, -134.83738878573843, -18.828826626108366), (2.684603, 2.684603, 2.684603), "Rubble_Masonry_Pile_E5", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (10916.834, 5121.255, 827.48987), (9.566715964182285, -26.49331451877904, 10.627907110756329), (2.684603, 2.684603, 2.684603), "Rubble_Masonry_Pile_E6", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (10482.169, 4826.933, 958.84576), (8.056573085093595, -0.3199770141220564, 27.46184109858569), (2.684603, 2.684603, 2.684603), "Rubble_Masonry_Pile_E7", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (10448.154, 4984.5073, 870.4078), (19.266538645694688, -119.26276813023085, -10.804564040871814), (2.684603, 2.684603, 2.684603), "Rubble_Masonry_Pile_E8", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (10429.448, 5528.6797, 745.7521), (-22.990659401852064, 55.502437128100006, -9.175139098715652), (2.684603, 2.684603, 2.684603), "Rubble_Masonry_Pile_E9", _folder)
if a: placed += 1
else: skipped += 1

# Batch 96: StaticMesh'Rubble_Masonry_Pile_E_Optimized' (3 instances)
_mesh_path = "/Game/Art/Assets/Kits/Deco/Rubble/Rubble_Masonry_Pile_E_Optimized"
_materials = ['/Game/Art/Assets/Kits/Deco/Rubble/Materials/Rubble_Masonry_Pile/MI_Rubble_Masonry_Pile_Atlas_Inst_A_RedRock', '/Game/Art/Assets/Kits/Deco/Rubble/Materials/Rubble_Masonry_Pile/MI_Rubble_Masonry_Pile_Atlas_Inst_B_RedRock']
_folder = "Reconstruction/BD_BB_Outdoor_TradingPost/Meshes"
a = spawn_static_mesh(_mesh_path, _materials, (10479.456, 13311.052, 682.8469), (0.0, 34.45043013076725, -0.0), (2.5448828, 2.5448828, 2.5448828), "Rubble_Masonry_Pile_E_Optimized_42", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (10683.883, 5998.8, 591.2661), (0.0, -44.3618478680232, 0.0), (1.956512, 1.956512, 1.956512), "Rubble_Masonry_Pile_E_Optimized2_524", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (10624.925, 5160.2686, 877.82043), (25.727317829644335, -96.29165728371102, 17.798424156007197), (1.956512, 1.956512, 1.956512), "Rubble_Masonry_Pile_E_Optimized3", _folder)
if a: placed += 1
else: skipped += 1

# Batch 97: StaticMesh'Rubble_Masonry_Pile_F' (1 instances)
_mesh_path = "/Game/Art/Assets/Kits/Deco/Rubble/Rubble_Masonry_Pile_F"
_materials = ['/Game/Art/Assets/Kits/Deco/Rubble/Materials/Rubble_Masonry_Pile/MI_Rubble_Masonry_Pile_Atlas_Inst_B', '/Game/Art/Assets/Kits/Deco/Rubble/Materials/Rubble_Masonry_Pile/MI_Rubble_Masonry_Pile_Atlas_Inst_A']
_folder = "Reconstruction/BD_BB_Outdoor_TradingPost/Meshes"
a = spawn_static_mesh(_mesh_path, _materials, (11375.389, 5952.6274, 595.5381), (0.0, 0.0, -0.0), (1.0, 1.0, 1.0), "Rubble_Masonry_Pile_F_515", _folder)
if a: placed += 1
else: skipped += 1

# Batch 98: StaticMesh'Rubble_Masonry_Pile_F_Optimized' (17 instances)
_mesh_path = "/Game/Art/Assets/Kits/Deco/Rubble/Rubble_Masonry_Pile_F_Optimized"
_materials = ['/Game/Art/Assets/Kits/Deco/Rubble/Materials/Rubble_Masonry_Pile/MI_Rubble_Masonry_Pile_Atlas_Inst_B_RedRock', '/Game/Art/Assets/Kits/Deco/Rubble/Materials/Rubble_Masonry_Pile/MI_Rubble_Masonry_Pile_Atlas_Inst_A_RedRock']
_folder = "Reconstruction/BD_BB_Outdoor_TradingPost/Meshes"
a = spawn_static_mesh(_mesh_path, _materials, (10502.546, 13468.633, 686.6741), (0.0, 34.45043013076725, -0.0), (1.0, 1.0, 1.0), "Rubble_Masonry_Pile_F_Optimized_39", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (11446.167, 5922.223, 630.0505), (10.946805559869674, -9.896058205677111, 2.0654331293152683), (1.802961, 1.802961, 1.802961), "Rubble_Masonry_Pile_F_Optimized10", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (11351.642, 5481.8945, 666.28326), (17.60182866671777, -10.196411519328981, 0.849612748577626), (1.802961, 1.802961, 1.802961), "Rubble_Masonry_Pile_F_Optimized11", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (11683.561, 5483.522, 900.2457), (22.27032073745399, -9.457732603845082, 2.1913710613169908), (1.802961, 1.802961, 1.802961), "Rubble_Masonry_Pile_F_Optimized12", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (10880.656, 4933.507, 916.5876), (10.946805280473699, -9.896057260299106, 15.115522066519352), (1.802961, 1.802961, 1.802961), "Rubble_Masonry_Pile_F_Optimized13", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (11156.372, 4862.164, 978.8089), (14.146392970123184, -27.820617813379073, 13.555320053797047), (1.802961, 1.802961, 1.802961), "Rubble_Masonry_Pile_F_Optimized14", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (11873.733, 5463.664, 1019.5211), (17.6018276317156, -10.196410552032257, 6.264969963944886), (1.802961, 1.802961, 1.802961), "Rubble_Masonry_Pile_F_Optimized15", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (10167.5, 13488.2705, 691.9571), (0.0, 34.45043013076725, -0.0), (0.7958156, 0.7958156, 0.7958156), "Rubble_Masonry_Pile_F_Optimized16", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (10272.852, 12968.938, 657.6555), (-1.7501219426471548, 78.09743316697754, -3.303955068384415), (0.8649736, 0.8649736, 0.8649736), "Rubble_Masonry_Pile_F_Optimized17", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (9231.677, 13227.426, 700.63184), (0.0, 34.45043013076725, -0.0), (1.0, 1.0, 1.0), "Rubble_Masonry_Pile_F_Optimized2_73", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (10330.763, 14435.448, 860.28125), (28.61636171687809, 73.07157141526314, 5.705710728689046), (1.5218759, 1.5218759, 1.5218759), "Rubble_Masonry_Pile_F_Optimized3_80", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (10260.761, 13983.777, 699.1161), (-2.025330520426179, -32.34988386050809, -29.067966949537936), (1.521876, 1.521876, 1.521876), "Rubble_Masonry_Pile_F_Optimized4", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (9922.526, 14193.541, 665.0852), (-28.607938478018397, -106.83481907285157, -5.750364648897167), (1.521876, 1.521876, 1.521876), "Rubble_Masonry_Pile_F_Optimized5", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (10067.35, 14125.86, 700.63184), (0.0, 34.45043013076725, -0.0), (1.0, 1.0, 1.0), "Rubble_Masonry_Pile_F_Optimized6", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (10473.271, 13644.624, 700.63184), (0.0, -82.0769026061324, 0.0), (1.0, 1.0, 1.0), "Rubble_Masonry_Pile_F_Optimized7", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (10585.998, 5615.25, 598.9895), (0.0, -27.820829865672398, 0.0), (1.8029611, 1.8029611, 1.8029611), "Rubble_Masonry_Pile_F_Optimized8_495", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (10346.457, 13803.429, 665.0848), (-28.607875203125875, -119.51811707834203, -5.750365344480597), (1.521876, 1.521876, 1.521876), "Rubble_Masonry_Pile_F_Optimized9", _folder)
if a: placed += 1
else: skipped += 1

# Batch 99: StaticMesh'Rubble_Masonry_Pile_H' (1 instances)
_mesh_path = "/Game/Art/Assets/Kits/Deco/Rubble/Rubble_Masonry_Pile_H"
_materials = ['/Game/Art/Assets/Kits/Deco/Rubble/Materials/Rubble_Masonry_Pile/MI_Rubble_Masonry_Pile_Atlas_Inst_B', '/Game/Art/Assets/Kits/Deco/Rubble/Materials/Rubble_Masonry_Pile/MI_Rubble_Masonry_Pile_Atlas_Inst_A']
_folder = "Reconstruction/BD_BB_Outdoor_TradingPost/Meshes"
a = spawn_static_mesh(_mesh_path, _materials, (11090.195, 5853.9927, 613.3655), (0.0, 0.0, -0.0), (1.0, 1.0, 1.0), "Rubble_Masonry_Pile_H_504", _folder)
if a: placed += 1
else: skipped += 1

# Batch 100: StaticMesh'Armory_Scatter_Helmet' (1 instances)
_mesh_path = "/Game/Art/Assets/Kits/Deco/Urban/Armory/Armory_Scatter_Helmet"
_materials = ['/Game/Art/Assets/Kits/Deco/Urban/Armory/Materials/Armory_Scatter_Helmet/MI_Armory_Scatter_Helmet']
_folder = "Reconstruction/BD_BB_Outdoor_TradingPost/Meshes"
a = spawn_static_mesh(_mesh_path, _materials, (9161.986, 17732.863, 351.4271), (1.7494931091977023e-07, 130.00013557979227, -15.0000583092108), (1.0, 1.0, 1.0), "Armory_Scatter_Helmet_170", _folder)
if a: placed += 1
else: skipped += 1

# Batch 101: StaticMesh'Urban_Buntin_SML_A' (4 instances)
_mesh_path = "/Game/Art/Assets/Kits/Deco/Urban/Buntin/Urban_Buntin_SML_A"
_materials = ['/Game/Art/Assets/Kits/Deco_Architecture/TradingPost/Materials/MI_OTP_Rope', '/Game/Art/Assets/Kits/Deco_Architecture/TradingPost/Materials/MI_OTP_Fabric_Pattern_D']
_folder = "Reconstruction/BD_BB_Outdoor_TradingPost/Meshes"
a = spawn_static_mesh(_mesh_path, _materials, (10871.365, 10699.955, 987.1531), (6.930449402503264, -151.13286677210314, -1.2524719759211078), (1.3950262, 1.3950262, 1.3950262), "Urban_Buntin_SML_A_663", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (11708.69, 10163.642, 988.3231), (6.832988984287548, 20.339354718208476, -1.4078059995459133), (1.395026, 1.395026, 1.395026), "Urban_Buntin_SML_A2", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (11623.4795, 8958.27, 987.1531), (6.9304496264185635, -12.880402113141201, -1.2524415668980835), (1.395026, 1.395026, 1.395026), "Urban_Buntin_SML_A3", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (9726.321, 11078.079, 987.1531), (6.930449418582887, -68.94979981901527, -1.2524414019151586), (1.395026, 1.395026, 1.395026), "Urban_Buntin_SML_A4", _folder)
if a: placed += 1
else: skipped += 1

# Batch 102: StaticMesh'Dwelling_Basin_A' (1 instances)
_mesh_path = "/Game/Art/Assets/Kits/Deco/Urban/Dwelling/Dwelling_Basin_A"
_materials = ['/Game/Art/Assets/Kits/Deco/Urban/Dwelling/Materials/Dwelling_Basin_A/MI_Dwelling_Basin_A']
_folder = "Reconstruction/BD_BB_Outdoor_TradingPost/Meshes"
a = spawn_static_mesh(_mesh_path, _materials, (11683.061, 9981.45, 676.0966), (0.0, 0.0, -0.0), (1.0, 1.0, 1.0), "Dwelling_Basin_A_509", _folder)
if a: placed += 1
else: skipped += 1

# Batch 103: StaticMesh'Dwelling_Bench' (1 instances)
_mesh_path = "/Game/Art/Assets/Kits/Deco/Urban/Dwelling/Dwelling_Bench"
_materials = ['/Game/Art/Assets/Kits/Deco/Urban/Dwelling/Materials/Dwelling_Bench/MI_Dwelling_Bench']
_folder = "Reconstruction/BD_BB_Outdoor_TradingPost/Meshes"
a = spawn_static_mesh(_mesh_path, _materials, (5146.247, 5115.1714, 345.0), (0.0, 46.90905433157744, -0.0), (1.0, 1.0, 1.0), "Dwelling_Bench_1401", _folder)
if a: placed += 1
else: skipped += 1

# Batch 104: StaticMesh'Dwelling_Ornate_Box' (1 instances)
_mesh_path = "/Game/Art/Assets/Kits/Deco/Urban/Dwelling/Dwelling_Ornate_Box"
_materials = ['/Game/Art/Assets/Kits/Deco/Urban/Dwelling/Materials/Dwelling_Ornate_Box/MI_Dwelling_Ornate_Box']
_folder = "Reconstruction/BD_BB_Outdoor_TradingPost/Meshes"
a = spawn_static_mesh(_mesh_path, _materials, (9200.835, 17724.014, 350.88187), (0.0, 0.0, -0.0), (1.0, 1.0, 1.0), "Dwelling_Ornate_Box_164", _folder)
if a: placed += 1
else: skipped += 1

# Batch 105: StaticMesh'SM_Hourglass' (1 instances)
_mesh_path = "/Game/Art/Assets/Kits/Deco/Urban/ExpeditionTable/SM_Hourglass"
_materials = ['/Game/Art/Assets/Kits/Deco/Urban/ExpeditionTable/Materials/MI_Hourglass', '/Game/Art/Assets/Kits/Deco/Urban/ExpeditionTable/Materials/M_ExpeditionTable_PropsGlass']
_folder = "Reconstruction/BD_BB_Outdoor_TradingPost/Meshes"
a = spawn_static_mesh(_mesh_path, _materials, (11729.081, 10011.017, 676.0966), (0.0, 0.0, -0.0), (1.0, 1.0, 1.0), "SM_Hourglass_554", _folder)
if a: placed += 1
else: skipped += 1

# Batch 106: StaticMesh'SM_MagnifyingGlass' (1 instances)
_mesh_path = "/Game/Art/Assets/Kits/Deco/Urban/ExpeditionTable/SM_MagnifyingGlass"
_materials = ['/Game/Art/Assets/Kits/Deco/Urban/ExpeditionTable/Materials/MI_MagnifyingGlass', '/Game/Art/Assets/Kits/Deco/Urban/ExpeditionTable/Materials/M_ExpeditionTable_PropsGlass']
_folder = "Reconstruction/BD_BB_Outdoor_TradingPost/Meshes"
a = spawn_static_mesh(_mesh_path, _materials, (11710.289, 9158.364, 670.197), (0.0, 26.195504375663777, -0.0), (1.0, 1.0, 1.0), "SM_MagnifyingGlass_557", _folder)
if a: placed += 1
else: skipped += 1

# Batch 107: StaticMesh'Kitchen_Stone_Countertop_B' (1 instances)
_mesh_path = "/Game/Art/Assets/Kits/Deco/Urban/Kitchen/Kitchen_Stone_Countertop_B"
_materials = ['/Game/Art/Assets/GPI/Material/GPI_Hearth/MI_GPI_Hearth', '/Game/Art/Assets/Kits/Architecture/Suburbs/Materials/Suburbs_Trim_Sheet_A/MI_Suburbs_Trim_Sheet_A']
_folder = "Reconstruction/BD_BB_Outdoor_TradingPost/Meshes"
a = spawn_static_mesh(_mesh_path, _materials, (9767.375, 13934.961, 697.8469), (0.0, 32.846538425494025, -0.0), (1.0, 1.0, 1.0), "Kitchen_Stone_Countertop_B_140", _folder)
if a: placed += 1
else: skipped += 1

# Batch 108: StaticMesh'Shop_Pottery_Large_C' (1 instances)
_mesh_path = "/Game/Art/Assets/Kits/Deco/Urban/Shop/Shop_Pottery_Large_C"
_materials = ['/Game/Art/Assets/Kits/Deco/Urban/Shop/Materials/Shop_Pottery/MI_Shop_Pottery']
_folder = "Reconstruction/BD_BB_Outdoor_TradingPost/Meshes"
a = spawn_static_mesh(_mesh_path, _materials, (11768.509, 10051.491, 598.7671), (0.0, 0.0, -0.0), (1.0, 1.0, 1.0), "Shop_Pottery_Large_C_542", _folder)
if a: placed += 1
else: skipped += 1

# Batch 109: StaticMesh'Shop_Pottery_Large_D_A' (1 instances)
_mesh_path = "/Game/Art/Assets/Kits/Deco/Urban/Shop/Shop_Pottery_Large_D_A"
_materials = ['/Game/Art/Assets/Kits/Deco/Urban/Shop/Materials/Shop_Pottery/MI_Shop_Pottery_B']
_folder = "Reconstruction/BD_BB_Outdoor_TradingPost/Meshes"
a = spawn_static_mesh(_mesh_path, _materials, (11605.104, 9167.511, 596.3966), (0.0, 0.0, -0.0), (1.0, 1.0, 1.0), "Shop_Pottery_Large_D_A_539", _folder)
if a: placed += 1
else: skipped += 1

# Batch 110: StaticMesh'Shop_Pottery_Small_A_A' (1 instances)
_mesh_path = "/Game/Art/Assets/Kits/Deco/Urban/Shop/Shop_Pottery_Small_A_A"
_materials = ['/Game/Art/Assets/Kits/Deco/Urban/Shop/Materials/Shop_Pottery/MI_Shop_Pottery_B']
_folder = "Reconstruction/BD_BB_Outdoor_TradingPost/Meshes"
a = spawn_static_mesh(_mesh_path, _materials, (11056.912, 9389.097, 673.9762), (0.0, 0.0, -0.0), (1.0, 1.0, 1.0), "Shop_Pottery_Small_A_A_545", _folder)
if a: placed += 1
else: skipped += 1

# Batch 111: StaticMesh'Shop_Pottery_Small_C' (1 instances)
_mesh_path = "/Game/Art/Assets/Kits/Deco/Urban/Shop/Shop_Pottery_Small_C"
_materials = ['/Game/Art/Assets/Kits/Deco/Urban/Shop/Materials/Shop_Pottery/MI_Shop_Pottery']
_folder = "Reconstruction/BD_BB_Outdoor_TradingPost/Meshes"
a = spawn_static_mesh(_mesh_path, _materials, (11757.047, 10105.831, 673.64795), (0.0, 0.0, -0.0), (1.0, 1.0, 1.0), "Shop_Pottery_Small_C_551", _folder)
if a: placed += 1
else: skipped += 1

# Batch 112: StaticMesh'Shop_Pottery_Small_D_A' (1 instances)
_mesh_path = "/Game/Art/Assets/Kits/Deco/Urban/Shop/Shop_Pottery_Small_D_A"
_materials = ['/Game/Art/Assets/Kits/Deco/Urban/Shop/Materials/Shop_Pottery/MI_Shop_Pottery_B']
_folder = "Reconstruction/BD_BB_Outdoor_TradingPost/Meshes"
a = spawn_static_mesh(_mesh_path, _materials, (11445.129, 9207.532, 745.47266), (0.0, 0.0, -0.0), (1.0, 1.0, 1.0), "Shop_Pottery_Small_D_A_548", _folder)
if a: placed += 1
else: skipped += 1

# Batch 113: StaticMesh'GPI_Heavy_Carry_Crate' (6 instances)
_mesh_path = "/Game/Art/Assets/Kits/Deco/Urban/Warehouse/GPI_Heavy_Carry_Crate"
_materials = ['/Game/Art/Assets/Kits/Deco/Urban/Warehouse/Materials/GPI_Heavy_Carry_Crate/MI_GPI_Heavy_Carry_Crate']
_folder = "Reconstruction/BD_BB_Outdoor_TradingPost/Meshes"
a = spawn_static_mesh(_mesh_path, _materials, (11364.195, 10003.417, 600.0), (0.0, -33.01415980721768, 0.0), (1.0, 1.0, 1.0), "GPI_Heavy_Carry_Crate_1420", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (11601.714, 10065.25, 600.0), (0.0, -98.01419399683692, 0.0), (1.0, 1.0, 1.0), "GPI_Heavy_Carry_Crate2", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (11531.237, 9106.119, 600.0), (0.0, -10.000030597161448, 0.0), (1.0, 1.0, 1.0), "GPI_Heavy_Carry_Crate3", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (11201.284, 9299.017, 600.0), (0.0, 114.99990933671516, -0.0), (1.0, 1.0, 1.0), "GPI_Heavy_Carry_Crate4", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (11718.297, 9125.306, 600.0), (0.0, -17.58062578219328, 0.0), (1.0, 1.0, 1.0), "GPI_Heavy_Carry_Crate5", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (11697.661, 9053.338, 746.2488), (0.0, 81.85556708085456, -0.0), (1.0, 1.0, 1.0), "GPI_Heavy_Carry_Crate6", _folder)
if a: placed += 1
else: skipped += 1

# Batch 114: StaticMesh'Warehouse_Cage' (1 instances)
_mesh_path = "/Game/Art/Assets/Kits/Deco/Urban/Warehouse/Warehouse_Cage"
_materials = ['/Game/Art/Assets/Kits/Deco/Urban/Warehouse/Materials/Warehouse_Cage/MI_Warehouse_Cage']
_folder = "Reconstruction/BD_BB_Outdoor_TradingPost/Meshes"
a = spawn_static_mesh(_mesh_path, _materials, (10882.892, 10937.876, 657.59576), (2.8309223996956496, -20.531588119714527, 8.626459398681904e-08), (1.0, 1.0, 1.0), "Warehouse_Cage_683", _folder)
if a: placed += 1
else: skipped += 1

# Batch 115: StaticMesh'Warehouse_Metal_Crate_A' (13 instances)
_mesh_path = "/Game/Art/Assets/Kits/Deco/Urban/Warehouse/Warehouse_Metal_Crate_A"
_materials = ['/Game/Art/Assets/Kits/Deco/Urban/Warehouse/Materials/Warehouse_Crate/MI_Warehouse_Metal_Crate']
_folder = "Reconstruction/BD_BB_Outdoor_TradingPost/Meshes"
a = spawn_static_mesh(_mesh_path, _materials, (11480.239, 10058.721, 600.0), (0.0, 11.98665155539809, -0.0), (1.0, 1.0, 1.0), "Warehouse_Metal_Crate_A_1417", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (11511.484, 9133.498, 746.65894), (0.0, -39.99999627657838, 0.0), (1.0, 1.0, 1.0), "Warehouse_Metal_Crate_A10", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (11761.919, 9012.265, 597.9573), (0.0, -61.651253561245476, 0.0), (1.0, 1.0, 1.0), "Warehouse_Metal_Crate_A11", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (11742.542, 9039.177, 671.45776), (0.0, 35.558998257709256, -0.0), (1.0, 1.0, 1.0), "Warehouse_Metal_Crate_A12", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (11698.525, 9050.936, 814.6707), (0.0, -29.99999868431647, 0.0), (1.0, 1.0, 1.0), "Warehouse_Metal_Crate_A13", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (11506.305, 9955.899, 600.0), (0.0, 71.98607822880959, -0.0), (1.0, 1.0, 1.0), "Warehouse_Metal_Crate_A2", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (11497.017, 10072.862, 743.47266), (0.0, 86.98615011084009, -0.0), (1.0, 1.0, 1.0), "Warehouse_Metal_Crate_A3", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (11739.805, 10110.744, 599.999), (0.0, 106.98661193691945, -0.0), (1.0, 1.0, 1.0), "Warehouse_Metal_Crate_A4", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (11683.874, 10075.2705, 670.0281), (0.0, 71.98607822880959, -0.0), (1.0, 1.0, 1.0), "Warehouse_Metal_Crate_A5", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (11224.468, 10380.173, 664.67194), (0.0, 92.70793092452706, -0.0), (1.0, 1.0, 1.0), "Warehouse_Metal_Crate_A6", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (11271.455, 9932.369, 600.7337), (0.0, 59.524379823134915, -0.0), (1.0, 1.0, 1.0), "Warehouse_Metal_Crate_A7", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (11329.75, 9297.871, 595.7032), (0.0, 60.00002593912136, -0.0), (1.0, 1.0, 1.0), "Warehouse_Metal_Crate_A8", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (11540.664, 9100.467, 671.4286), (0.0, -29.99999868431647, 0.0), (1.0, 1.0, 1.0), "Warehouse_Metal_Crate_A9_23", _folder)
if a: placed += 1
else: skipped += 1

# Batch 116: StaticMesh'Warehouse_Metal_Crate_B' (9 instances)
_mesh_path = "/Game/Art/Assets/Kits/Deco/Urban/Warehouse/Warehouse_Metal_Crate_B"
_materials = ['/Game/Art/Assets/Kits/Deco/Urban/Warehouse/Materials/Warehouse_Crate/MI_Warehouse_Metal_Crate']
_folder = "Reconstruction/BD_BB_Outdoor_TradingPost/Meshes"
a = spawn_static_mesh(_mesh_path, _materials, (11085.565, 10487.299, 625.6655), (-3.7846982894817316, -44.78014697247111, -2.404418528440157), (1.0, 1.0, 1.0), "Warehouse_Metal_Crate_B_677", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (11419.66, 10041.738, 670.0), (0.0, 16.986671992684048, -0.0), (1.0, 1.0, 1.0), "Warehouse_Metal_Crate_B2_1425", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (11554.396, 10071.848, 670.0), (0.0, -8.014129870468459, 0.0), (1.0, 1.0, 1.0), "Warehouse_Metal_Crate_B3", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (11701.914, 9996.318, 602.44775), (0.0, 46.98575118860594, -0.0), (1.0, 1.0, 1.0), "Warehouse_Metal_Crate_B4", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (11643.913, 9034.925, 600.3273), (0.0, -30.000063894566395, 0.0), (1.0, 1.0, 1.0), "Warehouse_Metal_Crate_B_open_20", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (11431.993, 9211.953, 600.3273), (0.0, -35.00006033507422, 0.0), (1.0, 1.0, 1.0), "Warehouse_Metal_Crate_B_open3", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (11469.355, 9185.776, 671.8237), (0.0, -45.000056798727684, 0.0), (1.0, 1.0, 1.0), "Warehouse_Metal_Crate_B_open4", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (11661.586, 9073.265, 671.8237), (0.0, -126.35855883370132, 0.0), (1.0, 1.0, 1.0), "Warehouse_Metal_Crate_B_open5", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (11052.649, 9410.997, 600.3273), (0.0, -35.00006033507422, 0.0), (1.0, 1.0, 1.0), "Warehouse_Metal_Crate_B_open6", _folder)
if a: placed += 1
else: skipped += 1

# Batch 117: StaticMesh'Workshop_Scatter_Rope_E' (1 instances)
_mesh_path = "/Game/Art/Assets/Kits/Deco/Urban/Workshop/Scatter/Workshop_Scatter_Rope_E"
_materials = ['/Game/Art/Assets/Kits/Deco_Architecture/Mines/Materials/Mines_Scaffolding/MI_Mines_Scaffolding_Rope_A']
_folder = "Reconstruction/BD_BB_Outdoor_TradingPost/Meshes"
a = spawn_static_mesh(_mesh_path, _materials, (11558.29, 9093.4795, 745.4726), (0.0, -30.000063894566395, 0.0), (1.0, 1.0, 1.0), "Workshop_Scatter_Rope_E_61", _folder)
if a: placed += 1
else: skipped += 1

# Batch 118: StaticMesh'Workshop_Scatter_Rope_H' (1 instances)
_mesh_path = "/Game/Art/Assets/Kits/Deco/Urban/Workshop/Scatter/Workshop_Scatter_Rope_H"
_materials = ['/Game/Art/Assets/Kits/Deco_Architecture/Mines/Materials/Mines_Scaffolding/MI_Mines_Scaffolding_Rope_A']
_folder = "Reconstruction/BD_BB_Outdoor_TradingPost/Meshes"
a = spawn_static_mesh(_mesh_path, _materials, (11801.345, 9079.585, 600.95056), (0.0, -90.7315115554993, 0.0), (1.0, 1.0, 1.0), "Workshop_Scatter_Rope_H_574", _folder)
if a: placed += 1
else: skipped += 1

# Batch 119: StaticMesh'Workshop_Scatter_Sandbags_A' (2 instances)
_mesh_path = "/Game/Art/Assets/Kits/Deco/Urban/Workshop/Scatter/Workshop_Scatter_Sandbags_A"
_materials = ['/Game/Art/Assets/Kits/Deco/Urban/Workshop/Materials/Workshop_Scatter_Sandbags/MI_Workshop_Scatter_Sandbags']
_folder = "Reconstruction/BD_BB_Outdoor_TradingPost/Meshes"
a = spawn_static_mesh(_mesh_path, _materials, (11426.979, 9909.102, 599.9644), (0.0, -58.013368730808686, 0.0), (1.0, 1.0, 1.0), "Workshop_Scatter_Sandbags_A_9", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (11323.008, 9304.503, 669.3521), (0.0, 0.0, -0.0), (1.0, 1.0, 1.0), "Workshop_Scatter_Sandbags_A2_47", _folder)
if a: placed += 1
else: skipped += 1

# Batch 120: StaticMesh'Workshop_Scatter_Sandbags_B' (4 instances)
_mesh_path = "/Game/Art/Assets/Kits/Deco/Urban/Workshop/Scatter/Workshop_Scatter_Sandbags_B"
_materials = ['/Game/Art/Assets/Kits/Deco/Urban/Workshop/Materials/Workshop_Scatter_Sandbags/MI_Workshop_Scatter_Sandbags']
_folder = "Reconstruction/BD_BB_Outdoor_TradingPost/Meshes"
a = spawn_static_mesh(_mesh_path, _materials, (11647.872, 9884.291, 599.538), (0.0, -33.01415980721768, 0.0), (1.0, 1.0, 1.0), "Workshop_Scatter_Sandbags_B_12", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (11191.289, 10263.27, 671.92535), (0.0, -12.48999063688557, 0.0), (1.0, 1.0, 1.0), "Workshop_Scatter_Sandbags_B2_689", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (11265.519, 9371.427, 599.98376), (0.0, 0.0, -0.0), (1.0, 1.0, 1.0), "Workshop_Scatter_Sandbags_B3_50", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (11867.223, 9040.385, 600.5609), (0.0, 0.0, -0.0), (1.0, 1.0, 1.0), "Workshop_Scatter_Sandbags_B4_577", _folder)
if a: placed += 1
else: skipped += 1

# Batch 121: StaticMesh'Workshop_Scatter_Sandbags_D' (1 instances)
_mesh_path = "/Game/Art/Assets/Kits/Deco/Urban/Workshop/Scatter/Workshop_Scatter_Sandbags_D"
_materials = ['/Game/Art/Assets/Kits/Deco/Urban/Workshop/Materials/Workshop_Scatter_Sandbags/MI_Workshop_Scatter_Sandbags']
_folder = "Reconstruction/BD_BB_Outdoor_TradingPost/Meshes"
a = spawn_static_mesh(_mesh_path, _materials, (11552.155, 9187.361, 595.0826), (0.3600878040097765, -14.210969107767612, -19.29138296850841), (1.0, 1.0, 1.0), "Workshop_Scatter_Sandbags_C_55", _folder)
if a: placed += 1
else: skipped += 1

# Batch 122: StaticMesh'Ruins_Column_Single_A_A' (1 instances)
_mesh_path = "/Game/Art/Assets/Kits/Deco_Architecture/Ruins/Ruins_Column_Single_A_A"
_materials = ['/Game/Art/Assets/Kits/Deco_Architecture/Ruins/Materials/Ruins_Column_Single_A/MI_Ruins_Column_Single_A_A_Inst_RedRock']
_folder = "Reconstruction/BD_BB_Outdoor_TradingPost/Meshes"
a = spawn_static_mesh(_mesh_path, _materials, (5716.0835, 8099.031, 550.0), (0.0, 40.00004908107326, -0.0), (1.0, 1.0, 1.0), "Ruins_Column_Single_A_A_269", _folder)
if a: placed += 1
else: skipped += 1

# Batch 123: StaticMesh'Ruins_Column_Single_A_B' (1 instances)
_mesh_path = "/Game/Art/Assets/Kits/Deco_Architecture/Ruins/Ruins_Column_Single_A_B"
_materials = ['/Game/Art/Assets/Kits/Deco_Architecture/Ruins/Materials/Ruins_Column_Single_A/MI_Ruins_Column_Single_A_B_RedRock']
_folder = "Reconstruction/BD_BB_Outdoor_TradingPost/Meshes"
a = spawn_static_mesh(_mesh_path, _materials, (5377.7334, 8502.258, 550.0), (0.0, 40.00004908107326, -0.0), (1.0, 1.0, 1.0), "Ruins_Column_Single_A_A2", _folder)
if a: placed += 1
else: skipped += 1

# Batch 124: StaticMesh'Ruins_Stairs_Medium_C' (4 instances)
_mesh_path = "/Game/Art/Assets/Kits/Deco_Architecture/Ruins/Ruins_Stairs_Medium_C"
_materials = ['/Game/Art/Assets/Kits/Architecture/Suburbs/Materials/Suburbs_Stairs/MI_Suburbs_Stairs_02_RedRock', '/Game/Art/Assets/Kits/Architecture/Suburbs/Materials/Suburbs_Stairs/MI_Suburbs_Stairs_01_RedRock', '/Game/Art/Assets/Kits/Deco/Rubble/Materials/Rubble_Masonry_Pile/MI_Rubble_Masonry_Pile_Base_Inst_RedRock']
_folder = "Reconstruction/BD_BB_Outdoor_TradingPost/Meshes"
a = spawn_static_mesh(_mesh_path, _materials, (9850.0, 9749.003, 430.0), (0.0, 90.00001925454477, -0.0), (1.0, 1.0, 1.0), "Ruins_Stairs_Medium_C6", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (6560.262, 8961.82, 150.0), (0.0, -48.56256091827546, 0.0), (1.0, 1.0, 1.0), "Ruins_Stairs_Medium_C7", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4995.9463, 8004.5806, 350.0), (0.0, 132.62864496523892, -0.0), (1.0, 1.0, 1.0), "Ruins_Stairs_Medium_C9", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (9100.023, 9458.296, 130.0), (0.0, 90.00001925454477, -0.0), (1.0, 1.0, 1.0), "Ruins_Stairs_Small_C8", _folder)
if a: placed += 1
else: skipped += 1

# Batch 125: StaticMesh'Ruins_Stairs_Small_A' (1 instances)
_mesh_path = "/Game/Art/Assets/Kits/Deco_Architecture/Ruins/Ruins_Stairs_Small_A"
_materials = ['/Game/Art/Assets/Kits/Architecture/Suburbs/Materials/Suburbs_Stairs/MI_Suburbs_Stairs_02_RedRock', '/Game/Art/Assets/Kits/Architecture/Suburbs/Materials/Suburbs_Stairs/MI_Suburbs_Stairs_01_RedRock', '/Game/Art/Assets/Kits/Deco/Rubble/Materials/Rubble_Masonry_Pile/MI_Rubble_Masonry_Pile_Base_Inst_RedRock']
_folder = "Reconstruction/BD_BB_Outdoor_TradingPost/Meshes"
a = spawn_static_mesh(_mesh_path, _materials, (6697.275, 8990.0, 143.20293), (-15.000031681461925, -48.562256386913255, 3.2587397123376945e-06), (1.0, 1.0, 1.0), "Ruins_Stairs_Medium_C10", _folder)
if a: placed += 1
else: skipped += 1

# Batch 126: StaticMesh'Ruins_Stairs_Small_B' (2 instances)
_mesh_path = "/Game/Art/Assets/Kits/Deco_Architecture/Ruins/Ruins_Stairs_Small_B"
_materials = ['/Game/Art/Assets/Kits/Architecture/Suburbs/Materials/Suburbs_Stairs/MI_Suburbs_Stairs_01_RedRock', '/Game/Art/Assets/Kits/Architecture/Suburbs/Materials/Suburbs_Stairs/MI_Suburbs_Stairs_02_RedRock', '/Game/Art/Assets/Kits/Deco/Rubble/Materials/Rubble_Masonry_Pile/MI_Rubble_Masonry_Pile_Base_Inst_RedRock']
_folder = "Reconstruction/BD_BB_Outdoor_TradingPost/Meshes"
a = spawn_static_mesh(_mesh_path, _materials, (9694.229, 9883.675, 426.2917), (0.0, 90.00001925454477, -0.0), (1.0, 1.0, 1.0), "Ruins_Stairs_Small_C10", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (9079.131, 9608.296, 205.07518), (0.0, 90.00001925454477, -0.0), (1.0, 1.0, 1.0), "Ruins_Stairs_Small_C7_653", _folder)
if a: placed += 1
else: skipped += 1

# Batch 127: StaticMesh'Ruins_Stairs_Small_C' (1 instances)
_mesh_path = "/Game/Art/Assets/Kits/Deco_Architecture/Ruins/Ruins_Stairs_Small_C"
_materials = ['/Game/Art/Assets/Kits/Architecture/Suburbs/Materials/Suburbs_Stairs/MI_Suburbs_Stairs_01_RedRock', '/Game/Art/Assets/Kits/Architecture/Suburbs/Materials/Suburbs_Stairs/MI_Suburbs_Stairs_02_RedRock', '/Game/Art/Assets/Kits/Deco/Rubble/Materials/Rubble_Masonry_Pile/MI_Rubble_Masonry_Pile_Base_Inst_RedRock']
_folder = "Reconstruction/BD_BB_Outdoor_TradingPost/Meshes"
a = spawn_static_mesh(_mesh_path, _materials, (9250.023, 9458.296, 330.0), (0.0, 90.00001925454477, -0.0), (1.0, 1.0, 1.0), "Ruins_Stairs_Small_C6", _folder)
if a: placed += 1
else: skipped += 1

# Batch 128: StaticMesh'Ruins_Stairs_Small_D' (1 instances)
_mesh_path = "/Game/Art/Assets/Kits/Deco_Architecture/Ruins/Ruins_Stairs_Small_D"
_materials = ['/Game/Art/Assets/Kits/Architecture/Suburbs/Materials/Suburbs_Stairs/MI_Suburbs_Stairs_01_RedRock', '/Game/Art/Assets/Kits/Architecture/Suburbs/Materials/Suburbs_Stairs/MI_Suburbs_Stairs_02_RedRock', '/Game/Art/Assets/Kits/Deco/Rubble/Materials/Rubble_Masonry_Pile/MI_Rubble_Masonry_Pile_Base_Inst_RedRock']
_folder = "Reconstruction/BD_BB_Outdoor_TradingPost/Meshes"
a = spawn_static_mesh(_mesh_path, _materials, (8950.0, 9750.0, 180.0), (0.0, 90.00001925454477, -0.0), (1.0, 1.0, 1.0), "Ruins_Stairs_Small_C9", _folder)
if a: placed += 1
else: skipped += 1

# Batch 129: StaticMesh'Balustrade_0-5m' (2 instances)
_mesh_path = "/Game/Art/Assets/Kits/Deco_Architecture/Suburbs/Balustrade_0-5m"
_materials = ['/Game/Art/Assets/Kits/Deco_Architecture/Suburbs/Materials/MI_Balustrade_RedRock']
_folder = "Reconstruction/BD_BB_Outdoor_TradingPost/Meshes"
a = spawn_static_mesh(_mesh_path, _materials, (5281.637, 7680.875, 552.1742), (0.0, 131.43724274232625, -0.0), (1.0, 1.0, 1.0), "Balustrade_broken13", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5803.3613, 8915.103, 552.1742), (0.0, -48.562744727917014, 0.0), (1.0, 1.0, 1.0), "Balustrade_broken20", _folder)
if a: placed += 1
else: skipped += 1

# Batch 130: StaticMesh'Balustrade_1m' (6 instances)
_mesh_path = "/Game/Art/Assets/Kits/Deco_Architecture/Suburbs/Balustrade_1m"
_materials = ['/Game/Art/Assets/Kits/Deco_Architecture/Suburbs/Materials/MI_Balustrade_RedRock']
_folder = "Reconstruction/BD_BB_Outdoor_TradingPost/Meshes"
a = spawn_static_mesh(_mesh_path, _materials, (5325.0767, 7719.2217, 552.1742), (0.0, 131.43724274232625, -0.0), (1.0, 1.0, 1.0), "Balustrade_broken12", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5278.5864, 8451.845, 552.1742), (0.0, 131.43737614586334, -0.0), (1.0, 1.0, 1.0), "Balustrade_broken15", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5353.555, 8518.023, 552.1742), (0.0, 131.43737614586334, -0.0), (1.0, 1.0, 1.0), "Balustrade_broken16", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5765.877, 8882.014, 552.1742), (0.0, -48.562744727917014, 0.0), (1.0, 1.0, 1.0), "Balustrade_broken19", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5812.367, 8149.3906, 552.1742), (0.0, -48.56264924781549, 0.0), (1.0, 1.0, 1.0), "Balustrade_broken6", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5737.3994, 8083.2104, 552.1742), (0.0, -48.56264924781549, 0.0), (1.0, 1.0, 1.0), "Balustrade_broken7", _folder)
if a: placed += 1
else: skipped += 1

# Batch 131: StaticMesh'Balustrade_broken' (12 instances)
_mesh_path = "/Game/Art/Assets/Kits/Deco_Architecture/Suburbs/Balustrade_broken"
_materials = ['/Game/Art/Assets/Kits/Deco_Architecture/Suburbs/Materials/MI_Balustrade_RedRock']
_folder = "Reconstruction/BD_BB_Outdoor_TradingPost/Meshes"
a = spawn_static_mesh(_mesh_path, _materials, (6112.2383, 8414.109, 552.1742), (0.0, 131.43740904242725, -0.0), (1.0, 1.0, 1.0), "Balustrade_broken_328", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5587.464, 7950.851, 552.1742), (0.0, 131.43724274232625, -0.0), (1.0, 1.0, 1.0), "Balustrade_broken10", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5475.012, 7851.581, 552.1742), (0.0, -48.56264924781549, 0.0), (1.0, 1.0, 1.0), "Balustrade_broken11", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5203.6196, 8385.662, 552.1742), (0.0, 131.43737614586334, -0.0), (1.0, 1.0, 1.0), "Balustrade_broken14", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5503.4907, 8650.384, 552.1742), (0.0, -48.562744727917014, 0.0), (1.0, 1.0, 1.0), "Balustrade_broken17", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5615.9424, 8749.653, 552.1742), (0.0, 131.43737614586334, -0.0), (1.0, 1.0, 1.0), "Balustrade_broken18", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (6112.2383, 8414.109, 552.1742), (0.0, -48.56264924781549, 0.0), (1.0, 1.0, 1.0), "Balustrade_broken2", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4978.7153, 8187.1274, 552.1742), (0.0, -48.56256091827546, 0.0), (1.0, 1.0, 1.0), "Balustrade_broken3_351", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5962.3027, 8281.75, 552.1742), (0.0, 131.4373183915756, -0.0), (1.0, 1.0, 1.0), "Balustrade_broken4", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5887.335, 8215.57, 552.1742), (0.0, -48.56264924781549, 0.0), (1.0, 1.0, 1.0), "Balustrade_broken5", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4978.7153, 8187.1274, 552.1742), (0.0, 131.43737614586334, -0.0), (1.0, 1.0, 1.0), "Balustrade_broken8_352", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5128.652, 8319.482, 552.1742), (0.0, -48.56261944264467, 0.0), (1.0, 1.0, 1.0), "Balustrade_broken9_353", _folder)
if a: placed += 1
else: skipped += 1

# Batch 132: StaticMesh'Dirt_Mound_D' (9 instances)
_mesh_path = "/Game/Art/Assets/Kits/Misc/Dirt_Mounds/Dirt_Mound_D"
_materials = ['/Game/Art/Assets/Kits/Misc/Dirt_Mounds/Materials/Trading_Post_Dirt_Inst']
_folder = "Reconstruction/BD_BB_Outdoor_TradingPost/Meshes"
a = spawn_static_mesh(_mesh_path, _materials, (10958.807, 11415.459, 638.74457), (0.0, -3.265716358055947, 0.0), (1.0, 1.0718112, 1.0), "Dirt_Mound_D20_647", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (9417.976, 5955.658, 424.78925), (-0.3697509570572199, -67.28272286649066, -17.845704934126324), (0.5615147, 0.5615147, 0.38242716), "Dirt_Mound_D21_734", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (8978.083, 11235.26, 637.3125), (0.0, 2.160387015111284, -0.0), (0.75989836, 0.75989836, 0.36887175), "Dirt_Mound_D22_10", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (12043.668, 9596.403, 584.55676), (0.0, 179.50838197209083, -0.0), (0.83195454, 0.7638125, 0.4819201), "Dirt_Mound_D23_31", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (11481.791, 11556.065, 702.65845), (0.0, 15.620212031163364, -0.0), (1.4031701, 1.071811, 1.4101409), "Dirt_Mound_D24", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (7160.8003, 11432.996, 165.65991), (0.0, 0.0, -0.0), (1.1415477, 1.0, 1.0), "Dirt_Mound_D25_1037", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4332.2334, 4889.44, 344.85608), (0.0, 12.395938644425204, -0.0), (1.0, 1.0, 1.0), "Dirt_Mound_D26_1152", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5745.7983, 4857.428, 344.85608), (0.0, 91.07494437268859, -0.0), (1.0, 1.0, 1.0), "Dirt_Mound_D27", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3885.1074, 10386.904, 620.0), (0.0, -139.55626677733247, 0.0), (1.0, 1.0, 1.0), "Dirt_Mound_D33_1582", _folder)
if a: placed += 1
else: skipped += 1

# Batch 133: StaticMesh'Dirt_Mound_E' (3 instances)
_mesh_path = "/Game/Art/Assets/Kits/Misc/Dirt_Mounds/Dirt_Mound_E"
_materials = ['/Game/Art/Assets/Kits/Misc/Dirt_Mounds/Materials/Trading_Post_Dirt_Inst']
_folder = "Reconstruction/BD_BB_Outdoor_TradingPost/Meshes"
a = spawn_static_mesh(_mesh_path, _materials, (8609.278, 5687.4736, 249.42896), (0.0, 111.0049904305536, -0.0), (0.75636035, 0.75636035, 0.75636035), "Dirt_Mound_E4_722", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4486.039, 11050.04, 640.7175), (-5.1665036053885665, -94.71697487741986, -1.8493651872410377), (1.2098633, 1.2098633, 1.4487027), "Dirt_Mound_E5_1585", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (10805.6, 8248.714, 606.793), (3.5087701542877454, -0.6930541931922746, -0.15533447137788053), (1.0, 1.0, 0.81483287), "Dirt_Mound_F17_15", _folder)
if a: placed += 1
else: skipped += 1

# Batch 134: StaticMesh'Dirt_Mound_F' (15 instances)
_mesh_path = "/Game/Art/Assets/Kits/Misc/Dirt_Mounds/Dirt_Mound_F"
_materials = ['/Game/Art/Assets/Kits/Misc/Dirt_Mounds/Materials/Trading_Post_Dirt_Inst']
_folder = "Reconstruction/BD_BB_Outdoor_TradingPost/Meshes"
a = spawn_static_mesh(_mesh_path, _materials, (9158.675, 12242.79, 671.1378), (1.2924833788006853, 12.172914383338762, -2.0674134529787778), (0.9073786, 0.94794184, 0.62284774), "Dirt_Mound_D_528", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (9033.399, 11698.155, 650.597), (2.7871845442426872, 159.5817059960319, 2.429598115166583), (0.907379, 1.0465188, 0.622848), "Dirt_Mound_D19", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (9372.826, 13856.366, 700.0027), (0.0, -14.398926359202783, 0.0), (2.2459702, 2.2459702, 2.2459702), "Dirt_Mound_F_49", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (10546.28, 13087.296, 690.99945), (-0.8489381141385591, 140.56165897121664, 4.132315975700639), (2.24597, 2.24597, 2.24597), "Dirt_Mound_F10", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (8826.979, 5315.2603, 247.94867), (0.0, -50.23943658656122, 0.0), (1.0, 1.0, 1.0), "Dirt_Mound_F11_719", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (8529.419, 5098.5073, 248.92279), (0.0, -38.312712280664186, 0.0), (0.76867753, 0.76867753, 0.76867753), "Dirt_Mound_F12_728", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (9004.433, 5956.104, 325.72064), (4.648304537020082, -33.81268201042983, -11.47405824197246), (0.847292, 0.847292, 0.38282844), "Dirt_Mound_F13_731", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (10251.861, 9017.666, 616.13214), (-5.628693225154628, 49.046216292287056, -2.7093814938189666), (1.0, 1.0, 1.0), "Dirt_Mound_F15_11", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4192.823, 5441.148, 362.06165), (-3.4951434195513235e-09, 19.06505553288985, -1.255798366584011), (1.0, 1.0, 1.0), "Dirt_Mound_F18_1155", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (9024.816, 13191.901, 685.39197), (0.0, -37.82779368338115, 0.0), (2.24597, 2.24597, 2.24597), "Dirt_Mound_F3", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (10306.245, 14262.565, 700.00256), (0.0, 64.83960412801787, -0.0), (3.3178353, 2.24597, 2.24597), "Dirt_Mound_F4", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (11506.88, 4828.234, 889.48157), (-16.426177832632323, 119.3527078779839, -3.111847386392695), (8.902462, 5.050822, 5.007741), "Dirt_Mound_F6", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (10658.7, 13548.445, 648.9101), (0.0, -1.4900207355386497, 0.0), (2.24597, 2.24597, 2.24597), "Dirt_Mound_F7", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (10671.945, 13448.971, 657.6629), (0.7540862450706767, -5.837127244603005, -4.995696041506313), (2.24597, 2.24597, 2.9353626), "Dirt_Mound_F8", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (9140.877, 13074.38, 690.1978), (0.0, 4.300288991904606, -0.0), (1.2728424, 1.2728424, 1.2728424), "Dirt_Mound_F9", _folder)
if a: placed += 1
else: skipped += 1

# Batch 135: StaticMesh'Dirt_Mound_G' (48 instances)
_mesh_path = "/Game/Art/Assets/Kits/Misc/Dirt_Mounds/Dirt_Mound_G"
_materials = ['/Game/Art/Assets/Kits/Misc/Dirt_Mounds/Materials/Trading_Post_Dirt_Inst']
_folder = "Reconstruction/BD_BB_Outdoor_TradingPost/Meshes"
a = spawn_static_mesh(_mesh_path, _materials, (7499.807, 5096.905, -71.68227), (-11.747955405517605, -115.2745340444917, -11.27929556687033), (2.5784736, 1.7954764, 1.7954764), "Dirt_Mound_F14", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (10840.652, 8689.584, 619.17084), (11.21414147222817, -9.965576716362907, 1.6393860869546073), (1.0, 1.0, 1.0), "Dirt_Mound_G_5", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (8182.3076, 11467.057, 173.21907), (-0.5955198667171124, 178.20182379522583, -0.39422598838255485), (1.517462, 1.0, 0.7500111), "Dirt_Mound_G10", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (8217.969, 11825.304, 188.63213), (-0.595428360906113, 178.2018235120814, 2.1865159807387946), (1.5992843, 1.2329, 0.750011), "Dirt_Mound_G11", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (6974.78, 10633.034, 278.74612), (-18.387726508142926, 12.043930037360203, -6.428924685437391), (1.9139475, 1.0, 1.5207992), "Dirt_Mound_G12", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (7334.6406, 10710.751, 130.70888), (1.3652846043880278e-09, 11.242858383725748, -2.3469848866761795), (1.517462, 1.0, 1.0), "Dirt_Mound_G13", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (6504.096, 10920.79, 458.38422), (-1.1806334178861895, -11.909057733513658, -5.579895027796344), (1.4398305, 1.4398305, 1.4398305), "Dirt_Mound_G14_1052", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (8205.441, 7556.6606, 243.66977), (0.0, 40.47712637367033, -0.0), (1.0, 0.43460134, 0.9493823), "Dirt_Mound_G15_1077", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (9510.357, 8543.787, 328.29822), (7.172060360946925, -120.66708257324377, -17.518219652570927), (1.0, 1.0, 1.0), "Dirt_Mound_G16_1080", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (9285.275, 8637.776, 255.72717), (11.763515312607135, -104.75224695851577, -14.882198547591617), (1.0, 1.0, 1.0), "Dirt_Mound_G17", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (9764.577, 8411.299, 448.99805), (5.959414453486353, -121.93515636190565, -25.200348502016105), (1.0, 1.0, 1.0), "Dirt_Mound_G18", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (9545.038, 8028.4644, 460.4342), (5.959414453486353, -121.93515636190565, -25.200348502016105), (0.66979206, 1.0, 0.69090587), "Dirt_Mound_G19", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (12184.862, 14057.366, 649.8717), (0.0, 0.6783767254091316, -0.0), (1.995766, 1.995766, 1.995766), "Dirt_Mound_G2", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (9370.823, 8177.6465, 364.96133), (5.959413599059768, -121.93513756518607, -21.706632274792224), (0.669792, 1.0, 0.5287159), "Dirt_Mound_G20", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (10264.818, 6756.613, 572.7701), (6.133153963808985, -51.60467073593066, 3.724797717560788), (1.0, 1.0, 1.0), "Dirt_Mound_G21_1126", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (9785.218, 6674.6187, 540.76416), (6.659215914881101, -42.305662561302576, -2.731842102109365), (1.3944955, 1.0, 1.728867), "Dirt_Mound_G22", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4890.863, 4390.7812, 347.917), (0.0, 97.852528059072, -0.0), (1.4530708, 1.4530708, 1.4530708), "Dirt_Mound_G23_1149", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (6114.6436, 5265.1274, 355.73123), (0.0, 19.458154317810312, -0.0), (1.1974156, 1.1974156, 1.1974156), "Dirt_Mound_G24_1162", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5538.251, 7178.5435, 354.30432), (0.0, 34.513091048036856, -0.0), (1.3415705, 1.1209974, 0.5705797), "Dirt_Mound_G25_1224", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (7170.7915, 9902.551, 143.58289), (0.0, 99.4468315997432, -0.0), (1.0, 1.1757382, 1.0), "Dirt_Mound_G26_1233", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4071.0227, 7241.759, 353.72504), (-0.35137938315829015, -18.849914500030867, 0.4260747290396842), (1.167185, 1.167185, 1.167185), "Dirt_Mound_G27_1430", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4232.5283, 7681.5938, 350.17563), (-0.2926025258864982, -26.36462317985886, 0.468370499083286), (1.3077959, 1.167185, 1.167185), "Dirt_Mound_G28", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4410.776, 5804.126, 344.42682), (-0.5520019542376466, 33.50507984200147, -0.017974861021444792), (1.167185, 1.167185, 1.167185), "Dirt_Mound_G29", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (12167.496, 13405.054, 649.87195), (0.0, -40.416687410456724, 0.0), (1.995766, 1.995766, 1.995766), "Dirt_Mound_G3", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5024.6924, 6210.56, 337.3335), (-0.5520019542376466, 33.50507984200147, -0.017974861021444792), (1.167185, 1.167185, 0.6887662), "Dirt_Mound_G30", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5763.9795, 6775.9907, 337.57697), (0.0, 11.602674373665378, -0.0), (1.0, 1.0, 1.1256863), "Dirt_Mound_G31_1452", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3830.3215, 6077.8696, 397.90295), (0.0, -78.99896606338368, 0.0), (1.0, 1.0, 1.0), "Dirt_Mound_G32_1498", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3140.8105, 6569.859, 399.99994), (0.0, -94.45837640880677, 0.0), (1.8228362, 1.4460989, 1.4460989), "Dirt_Mound_G34_1506", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (6294.1436, 10182.654, 291.52313), (5.284162365107959, 62.027315228611606, -24.900387794358853), (1.32169, 1.3398781, 1.0), "Dirt_Mound_G35_1529", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (6077.3945, 9766.861, 257.54828), (3.010789948731639, 61.81850916253982, -25.945979325102964), (1.8237817, 1.339878, 1.7294875), "Dirt_Mound_G36", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5756.9033, 9858.282, 426.56757), (14.415534416890662, 85.22348134552426, -26.488429152660284), (1.823782, 1.339878, 1.315652), "Dirt_Mound_G37", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5967.162, 10422.535, 482.2847), (-0.2002868773527065, -115.5509608898752, 27.799898934719668), (1.601839, 0.95023334, 1.315652), "Dirt_Mound_G38", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5198.613, 10792.574, 645.0), (3.3363216972535814, 80.89348077255849, 2.1014712132912825), (1.6871475, 1.6871475, 1.6871475), "Dirt_Mound_G39_1579", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (11637.104, 12836.418, 649.8727), (0.0, -35.06167828527715, 0.0), (1.995766, 1.995766, 1.0014602), "Dirt_Mound_G4", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5121.746, 9803.107, 635.0), (0.0, -45.13308492786603, 0.0), (1.0, 1.0, 1.0), "Dirt_Mound_G40_1593", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (6670.9805, 10004.137, 170.05023), (-3.714419563078089e-07, 55.76888122101737, -8.12783785136549), (1.2057168, 1.4402388, 1.2057168), "Dirt_Mound_G41_1617", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (6394.756, 9599.416, 165.10046), (-1.4163509854493876, 45.79911624645352, -8.004332349716865), (0.89010376, 0.80349827, 0.89010376), "Dirt_Mound_G42", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (6602.707, 9229.829, 115.0), (0.0, 36.243691286376084, -0.0), (1.4832596, 1.3065012, 1.0294365), "Dirt_Mound_G43_1621", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4850.0, 7750.0, 350.0), (0.0, 41.67342797386722, -0.0), (1.0, 1.0, 1.0), "Dirt_Mound_G44_777", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (10518.575, 7595.2817, 622.64343), (-3.815459759298964, -4.518920595349944, -0.11651612238441847), (1.0, 1.0, 0.55796695), "Dirt_Mound_G5_18", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (10767.073, 7609.017, 610.56415), (-1.6054686806298732, -1.498107744911386, -0.20132442615439777), (1.0, 1.0, 0.91468614), "Dirt_Mound_G6", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (11876.662, 10112.622, 595.6194), (1.2379860122546518e-07, 101.42003141047627, 4.240324017190707), (1.4571626, 1.0, 1.0), "Dirt_Mound_G7_34", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (7334.6406, 10710.751, 130.70888), (1.3652846043880278e-09, 11.242858383725748, -2.3469848866761795), (1.5174615, 1.0, 1.0), "Dirt_Mound_G8_1027", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (8118.0503, 11104.669, 163.15538), (-0.9523009691244025, -12.68682892605004, -2.145141723139063), (1.517462, 1.0, 1.1541041), "Dirt_Mound_G9", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (7402.16, 6513.758, -71.98493), (17.74754232529744, -21.272643271896985, -12.816649684627954), (1.7878557, 1.4526986, 1.6516352), "Dirt_Mound_H19", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (9781.102, 7617.6987, 623.4766), (10.668079040477313, -15.588071567415549, 2.313770848263711), (0.94921815, 1.1059055, 1.7320833), "Suburbs_Dirt_Mound_A2", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (10840.937, 7151.368, 628.13525), (10.634037277738269, 19.714254690664486, 0.9154767850787547), (0.949218, 1.1753479, 0.75142866), "Suburbs_Dirt_Mound_A4", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (11131.279, 6538.7124, 619.68726), (11.763840012956427, 29.304336772789586, -1.1199035855482051), (1.4661759, 1.692306, 2.0646558), "Suburbs_Dirt_Mound_A5", _folder)
if a: placed += 1
else: skipped += 1

# Batch 136: StaticMesh'Dirt_Mound_H' (11 instances)
_mesh_path = "/Game/Art/Assets/Kits/Misc/Dirt_Mounds/Dirt_Mound_H"
_materials = ['/Game/Art/Assets/Kits/Misc/Dirt_Mounds/Materials/Suburbs_Dirt_Inst']
_folder = "Reconstruction/BD_BB_Outdoor_TradingPost/Meshes"
a = spawn_static_mesh(_mesh_path, _materials, (5771.728, 8738.988, 554.2217), (0.0, -42.10891789156527, 0.0), (0.5812734, 0.5812734, 0.22809741), "Dirt_Mound_H37_1043", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5771.728, 8263.912, 556.2726), (0.0, -14.583557146255663, 0.0), (0.581273, 0.581273, 0.228097), "Dirt_Mound_H38", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5127.5073, 8042.695, 555.84204), (0.0, -14.583557146255663, 0.0), (0.581273, 0.581273, 0.228097), "Dirt_Mound_H39", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5172.7925, 8197.996, 555.84204), (0.0, 41.35793947861862, -0.0), (0.581273, 0.581273, 0.228097), "Dirt_Mound_H40", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5383.166, 8197.996, 556.53564), (0.0, 41.35793947861862, -0.0), (0.581273, 0.581273, 0.228097), "Dirt_Mound_H41", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5383.166, 7980.8955, 556.5356), (0.0, -42.41836206246792, 0.0), (0.581273, 0.581273, 0.228097), "Dirt_Mound_H42", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5536.308, 8378.38, 556.53546), (0.0, -96.93011949346659, 0.0), (0.581273, 0.581273, 0.228097), "Dirt_Mound_H43", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5699.649, 8723.244, 556.5354), (0.0, -173.04443323099414, 0.0), (0.581273, 0.581273, 0.228097), "Dirt_Mound_H44", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5903.1704, 8674.0625, 556.5354), (0.0, 95.31402936216514, -0.0), (0.581273, 0.581273, 0.228097), "Dirt_Mound_H45", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5903.1704, 8478.744, 556.5354), (0.0, 95.31402936216514, -0.0), (0.581273, 0.581273, 0.228097), "Dirt_Mound_H46", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5720.57, 8478.744, 556.5354), (0.0, 95.31402936216514, -0.0), (0.581273, 0.581273, 0.228097), "Dirt_Mound_H47", _folder)
if a: placed += 1
else: skipped += 1

# Batch 137: StaticMesh'Dirt_Mound_H' (1 instances)
_mesh_path = "/Game/Art/Assets/Kits/Misc/Dirt_Mounds/Dirt_Mound_H"
_materials = ['/Game/Art/Assets/Kits/Misc/Dirt_Mounds/Materials/Sururbs_Dirt_darker_Inst']
_folder = "Reconstruction/BD_BB_Outdoor_TradingPost/Meshes"
a = spawn_static_mesh(_mesh_path, _materials, (10273.421, 12989.265, 671.03107), (0.0, 0.0, -0.0), (1.1412828, 1.1412828, 1.0512003), "Dirt_Mound_H2_522", _folder)
if a: placed += 1
else: skipped += 1

# Batch 138: StaticMesh'Dirt_Mound_H' (44 instances)
_mesh_path = "/Game/Art/Assets/Kits/Misc/Dirt_Mounds/Dirt_Mound_H"
_materials = ['/Game/Art/Assets/Kits/Misc/Dirt_Mounds/Materials/Trading_Post_Dirt_Inst']
_folder = "Reconstruction/BD_BB_Outdoor_TradingPost/Meshes"
a = spawn_static_mesh(_mesh_path, _materials, (5314.201, 4822.0166, 344.85608), (0.0, 64.51625777981454, -0.0), (1.2242391, 1.2242391, 1.2242391), "Dirt_Mound_D28", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5379.106, 4972.751, 344.85596), (0.0, 5.156188211912002, -0.0), (1.224239, 1.224239, 1.224239), "Dirt_Mound_D29", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (9608.293, 11843.084, 661.6218), (2.328711866595454, 52.94549637385954, -0.7218932829481702), (1.1776615, 1.4060146, 0.89313066), "Dirt_Mound_D3", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4300.61, 5452.3066, 344.85596), (0.0, 63.2786952491744, -0.0), (1.224239, 1.224239, 1.224239), "Dirt_Mound_D30", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5364.106, 5042.751, 344.85596), (0.0, 39.48964422392039, -0.0), (1.224239, 1.224239, 1.224239), "Dirt_Mound_D31", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5799.106, 5422.751, 344.85596), (0.0, 39.48964422392039, -0.0), (1.224239, 1.224239, 1.224239), "Dirt_Mound_D32_1421", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (9162.115, 12514.382, 659.18304), (-0.8603513815860064, -14.755857071404138, -3.262847283867215), (1.733387, 1.8748076, 1.5390217), "Dirt_Mound_E3_525", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (10135.075, 9182.965, 610.45575), (1.7151709271077686, 113.21233280416149, -2.2094727477712026), (1.2945174, 1.0, 1.445256), "Dirt_Mound_F16", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (7384.6675, 10280.041, 121.67413), (0.0, 59.93532763905827, -0.0), (1.8730001, 1.8730001, 1.8730001), "Dirt_Mound_H10_1030", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (8137.664, 10827.658, 136.16194), (1.10002226611105, 102.7904042224985, 1.0204505705826052), (1.873, 1.873, 1.4630436), "Dirt_Mound_H11", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (8364.018, 8993.522, 148.36037), (3.8497605352510242, -71.75479034241002, 0.8700688496857089), (1.7429672, 1.7429672, 2.536452), "Dirt_Mound_H12", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5226.278, 4481.2783, 329.2633), (0.0, 43.619015194358454, -0.0), (1.7538538, 1.7538538, 2.0918055), "Dirt_Mound_H13_1146", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5929.0957, 5464.3047, 336.88074), (0.0, -18.247863004734633, 0.0), (1.5204966, 1.6201193, 3.2947571), "Dirt_Mound_H14_1159", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5221.493, 7279.7964, 351.46423), (1.1957337829400014, -21.710938612150606, 7.601822837609506e-08), (1.7687373, 1.7950114, 0.58287215), "Dirt_Mound_H15_1227", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (6950.503, 8811.932, 125.58807), (1.3416677159598684, -16.199156443433242, 3.168770758194806), (1.7539246, 1.8005434, 1.7139269), "Dirt_Mound_H16_1236", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (7530.117, 8643.051, 130.56786), (1.341668033544801, -16.19915643586638, 3.1687707132353857), (1.753925, 1.800543, 1.713927), "Dirt_Mound_H17", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (7419.1167, 7152.809, 42.5578), (12.707004869181066, 77.64745642722804, 19.19719282820881), (1.2102989, 1.0, 1.0), "Dirt_Mound_H18_1258", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (7330.363, 7472.4653, 53.332474), (12.707004869181066, 77.64745642722804, 19.19719282820881), (1.210299, 1.0, 1.0), "Dirt_Mound_H20", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (7269.879, 7638.319, 70.514694), (7.797193801316535, -28.436034237855, -21.253875069334843), (1.210299, 1.0, 1.0), "Dirt_Mound_H21", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (6645.004, 8086.3506, -41.286057), (2.240963960581212, -42.264256500793934, -22.470732543719247), (1.210299, 1.0, 0.77038604), "Dirt_Mound_H22", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (6456.388, 8260.509, -55.33112), (-9.336088956389446, -70.95663492941868, -25.87216440395992), (1.210299, 1.0, 0.770386), "Dirt_Mound_H23", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (6919.873, 8229.144, 107.25625), (17.52591398766249, 81.81402037156897, 15.92455765568516), (1.3131293, 1.3878984, 1.6204877), "Dirt_Mound_H24", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5470.9053, 5940.141, 348.66907), (1.7529689744056464e-09, 14.512032354548381, -1.5417786414508046), (1.3537745, 1.1825725, 1.0), "Dirt_Mound_H25_1377", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4518.8335, 7952.1323, 353.5769), (-0.21450802901886273, -169.92565117173342, 1.4776026828661206), (1.6083918, 1.2950909, 1.6400188), "Dirt_Mound_H26_1434", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5158.297, 5915.6157, 335.00476), (0.0, -64.29333682848598, 0.0), (1.284421, 1.284421, 1.284421), "Dirt_Mound_H27_1439", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (10880.612, 11140.723, 659.29694), (6.430664101151154, 0.0, -0.0), (1.2366098, 1.2366098, 1.2366098), "Dirt_Mound_H3_650", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (7079.4873, 8541.839, 177.45439), (1.692524796454082, -84.09006082403998, -2.8655394918919264), (1.0, 1.0, 1.0), "Dirt_Mound_H32_1495", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3397.5789, 5678.78, 382.60004), (0.0, 28.143576849804045, -0.0), (2.5364099, 1.9727858, 1.9727858), "Dirt_Mound_H33_1503", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3981.6199, 10350.588, 633.39813), (-2.303435970524331, 105.45504059515899, 1.7071771373517983), (1.7160277, 1.7160277, 1.7160277), "Dirt_Mound_H34_1588", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4141.107, 10187.429, 634.7155), (-0.3386534932712595, 106.76476070427188, 1.6551382578072884), (1.716028, 1.716028, 2.3297493), "Dirt_Mound_H35", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5367.7217, 9799.602, 568.33685), (-10.393706572015226, 0.0, -0.0), (1.716028, 1.716028, 2.7967772), "Dirt_Mound_H36", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (10225.405, 12403.246, 657.60065), (-0.449432190651296, 46.17087771579305, -3.501312166147892), (1.9664457, 1.5914626, 1.4690114), "Dirt_Mound_H4_708", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4214.8945, 6975.7305, 347.47885), (-2.4288027117444444, 27.21770812922038, 1.5609033616632568e-07), (1.3220829, 1.3220829, 1.3220829), "Dirt_Mound_H48_1056", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4327.085, 5998.195, 351.59113), (-2.428802673971474, 27.217708132161732, 6.107599563312642e-11), (1.5442975, 1.5442975, 1.2239814), "Dirt_Mound_H49", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (9703.722, 13931.455, 705.58795), (0.0, -10.275939910383293, 0.0), (1.0, 1.0, 0.22791046), "Dirt_Mound_H5_716", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (10090.738, 10358.478, 603.446), (-1.0969542470472429, -11.382902544232286, -7.930480932441609), (1.5263823, 1.3750049, 1.9771997), "Dirt_Mound_H6_4", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (10398.073, 8827.127, 600.00024), (0.0, -119.02290746189648, 0.0), (1.0, 1.0, 1.0), "Dirt_Mound_H7_8", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (8782.8, 8933.01, 219.42743), (3.581559956511315, -59.62488491420579, 1.6591011098536375), (1.5942429, 1.5942429, 2.3877282), "Dirt_Mound_H8_1039", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (11229.464, 10591.815, 625.4295), (3.4558227667828114, 43.64918560798124, -3.615753082748815), (1.7252514, 2.2993758, 1.1382713), "Dirt_Mound_I_644", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (10914.47, 9163.211, 587.18866), (0.0, -153.82082899211605, 0.0), (1.4580312, 1.4580312, 1.3068194), "Dirt_Mound_I4_22", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (10892.413, 5944.965, 600.5542), (0.0, 0.0, -0.0), (1.8589648, 1.8589648, 1.8589648), "Dirt_Mound_I6_1064", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (10277.976, 8362.53, 597.72974), (-0.28826901065547866, -0.44046018663470643, 5.043263782960218), (1.3194624, 1.3194624, 1.9824694), "Suburbs_Dirt_Mound_A_649", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (10736.546, 6191.4277, 557.8919), (6.193800645438771, 54.5798347126594, -0.11337283433036503), (1.4378924, 1.6640224, 2.036372), "Suburbs_Dirt_Mound_A6", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (10587.666, 6571.0137, 557.8927), (6.36901534646906, 70.55946320026737, 4.684760827737021), (1.724431, 1.950561, 2.322911), "Suburbs_Dirt_Mound_A7", _folder)
if a: placed += 1
else: skipped += 1

# Batch 139: StaticMesh'Dirt_Mound_I' (2 instances)
_mesh_path = "/Game/Art/Assets/Kits/Misc/Dirt_Mounds/Dirt_Mound_I"
_materials = ['/Game/Art/Assets/Kits/Misc/Dirt_Mounds/Materials/Suburbs_Dirt_Inst']
_folder = "Reconstruction/BD_BB_Outdoor_TradingPost/Meshes"
a = spawn_static_mesh(_mesh_path, _materials, (11872.281, 5732.7354, 574.08813), (0.0, 0.0, -0.0), (1.9757965, 1.9757965, 1.9757965), "Dirt_Mound_H_510", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (9738.906, 11193.884, 652.9547), (0.0, 111.76428672580447, -0.0), (0.43127754, 0.43127754, 0.43127754), "Dirt_Mound_I3_7", _folder)
if a: placed += 1
else: skipped += 1

# Batch 140: StaticMesh'Dirt_Mound_I' (13 instances)
_mesh_path = "/Game/Art/Assets/Kits/Misc/Dirt_Mounds/Dirt_Mound_I"
_materials = ['/Game/Art/Assets/Kits/Misc/Dirt_Mounds/Materials/Trading_Post_Dirt_Inst']
_folder = "Reconstruction/BD_BB_Outdoor_TradingPost/Meshes"
a = spawn_static_mesh(_mesh_path, _materials, (10172.643, 14138.5205, 674.5967), (0.0, -113.63118496858884, 0.0), (1.5471356, 1.3573607, 1.3573607), "Dirt_Mound_E_516", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (10356.475, 13629.173, 674.5967), (-4.227211904277299e-08, -138.98489533089904, 1.8990327014353452), (1.547136, 1.357361, 1.093748), "Dirt_Mound_E2", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (12280.114, 5444.662, 716.16876), (9.186358853599595, -27.605773744597503, 2.2769392405077604), (4.5360465, 2.448645, 4.5360465), "Dirt_Mound_F2_507", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (10304.236, 5019.274, 559.1124), (-12.513519226802439, 40.03258654770406, 3.3067147167788167), (4.536047, 2.448645, 3.2675314), "Dirt_Mound_F5", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3610.5344, 6644.0713, 399.99994), (0.0, -38.4731437732582, 0.0), (1.0, 1.0, 0.45146725), "Dirt_Mound_G33", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (6035.8228, 6559.2734, 233.25859), (-22.441315947609432, -0.07308944833823074, 10.227069951299205), (0.51807547, 0.51807547, 0.5190205), "Dirt_Mound_H28_1455", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (6194.6665, 6878.6104, 43.903263), (-25.074064016923977, 56.9982146713695, -12.667631996757446), (0.518075, 0.518075, 0.51902), "Dirt_Mound_H29", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (6075.7305, 7144.2085, 30.156954), (-29.198704059289508, 58.060087591824065, -13.152711001937995), (0.518075, 0.518075, 0.51902), "Dirt_Mound_H30", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5999.9897, 7448.248, -40.007206), (-20.425782427487835, 55.8843731592111, -11.34500143828445), (0.518075, 0.7969194, 0.35589656), "Dirt_Mound_H31", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (7708.991, 8585.435, 189.85414), (3.8277469815948892, -3.981719398170641, 8.153440467815456), (0.83389026, 0.64183426, 0.30207315), "Dirt_Mound_H9_717", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (11431.379, 10455.167, 629.36615), (9.6003631865271, 68.61163218025656, 1.7296021367821375), (1.075709, 1.2303562, 0.46928948), "Dirt_Mound_I2", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (12039.34, 8730.502, 592.9662), (0.0, -66.5654337886444, 0.0), (1.0, 1.2057333, 1.0), "Dirt_Mound_I5_28", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (9800.808, 7294.15, 625.563), (6.303163800215831, 67.7636428724633, 2.287600913581198), (0.56128657, 0.71797466, 0.8041286), "Suburbs_Dirt_Mound_A3", _folder)
if a: placed += 1
else: skipped += 1

# Batch 141: StaticMesh'Tree_Mound_A' (3 instances)
_mesh_path = "/Game/Art/Assets/Kits/Misc/Dirt_Mounds/Tree_Mound_A"
_materials = ['/Game/Art/Assets/Kits/Misc/Dirt_Mounds/Materials/Trading_Post_Dirt_Inst']
_folder = "Reconstruction/BD_BB_Outdoor_TradingPost/Meshes"
a = spawn_static_mesh(_mesh_path, _materials, (11080.101, 10810.586, 666.98004), (0.0, 0.0, -0.0), (1.6144714, 1.6144714, 0.73191476), "Tree_Mound_A_47", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (6930.67, 10717.493, 344.6474), (-31.719540134896587, 0.0, -0.0), (1.2644897, 1.2644897, 1.2644897), "Tree_Mound_A2_1041", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (6031.963, 5127.115, 376.69647), (0.0, 0.0, -0.0), (1.0, 1.0, 0.5105768), "Tree_Mound_A3_1165", _folder)
if a: placed += 1
else: skipped += 1

# Batch 142: StaticMesh'Tree_Mound_B' (5 instances)
_mesh_path = "/Game/Art/Assets/Kits/Misc/Dirt_Mounds/Tree_Mound_B"
_materials = ['/Game/Art/Assets/Kits/Misc/Dirt_Mounds/Materials/Trading_Post_Dirt_Inst']
_folder = "Reconstruction/BD_BB_Outdoor_TradingPost/Meshes"
a = spawn_static_mesh(_mesh_path, _materials, (8690.163, 7325.8584, 285.48816), (0.0, 0.0, -0.0), (0.6218858, 0.6218858, 0.47197837), "Tree_Mound_B_728", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (8098.7236, 7627.5737, 267.74033), (0.0, 0.0, -0.0), (0.621886, 0.621886, 0.35153), "Tree_Mound_B2", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5045.57, 6024.1016, 337.236), (0.0, 0.0, -0.0), (1.0, 1.0, 1.0), "Tree_Mound_B3_1368", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3957.8345, 10798.569, 625.37213), (0.0, 0.0, -0.0), (1.0, 1.0, 1.0), "Tree_Mound_B4_709", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5215.956, 10703.209, 641.30115), (0.0, -100.00008183358206, 0.0), (1.0, 1.0, 1.0), "Tree_Mound_B5", _folder)
if a: placed += 1
else: skipped += 1

# Batch 143: StaticMesh'SM_Cube' (1 instances)
_mesh_path = "/Game/FX/ShadowFog/Meshes/SM_Cube"
_materials = ['/Game/Environments/ProcTexturing/GuideMeshFloor/MI_GuideMeshFloor_TradingPost']
_folder = "Reconstruction/BD_BB_Outdoor_TradingPost/Meshes"
a = spawn_static_mesh(_mesh_path, _materials, (6400.0, 6400.0, 5.0), (0.0, 0.0, -0.0), (64.0, 96.0, 0.05), "Plane_StreamFix", _folder)
if a: placed += 1
else: skipped += 1

# Batch 144: StaticMesh'Rock_04' (3 instances)
_mesh_path = "/Game/Unshippable/Cinematics/Cine001/Environment/Rock_04"
_materials = ['/Game/Unshippable/Cinematics/Cine001/Environment/Materials/MI_Rock_04']
_folder = "Reconstruction/BD_BB_Outdoor_TradingPost/Meshes"
a = spawn_static_mesh(_mesh_path, _materials, (3910.755, 9478.811, -107.48535), (0.0, 173.39817405934764, -0.0), (0.262851, 0.262851, 0.262851), "Rock_25", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5686.6865, 9335.273, -88.26843), (0.0, 153.67063552188597, -0.0), (0.15106952, 0.15106952, 0.15106952), "Rock_26", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (10333.144, 15321.143, 208.96753), (0.0, 102.03395418807513, -0.0), (0.22736447, 0.267693, 0.247219), "Rock_90", _folder)
if a: placed += 1
else: skipped += 1

# Batch 145: StaticMesh'Rock_04' (36 instances)
_mesh_path = "/Game/Unshippable/Cinematics/Cine001/Environment/Rock_04"
_materials = ['/Game/Unshippable/Cinematics/Cine001/Environment/Materials/MI_Rock_04_Red']
_folder = "Reconstruction/BD_BB_Outdoor_TradingPost/Meshes"
a = spawn_static_mesh(_mesh_path, _materials, (10217.848, 15015.353, 208.96753), (0.0, 87.76510075945778, -0.0), (0.37209204, 0.267693, 0.28812858), "Rock_6", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (6549.029, 8400.506, -167.15332), (-1.271820115832733, 132.39943413304582, 0.2785641813333242), (0.3963072, 0.3486525, 0.2770392), "Rock_7", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (7863.9497, 6135.1714, -113.0293), (-1.0477600802739016, 108.33344166677456, 0.7730264829142477), (0.396307, 0.348653, 0.277039), "Rock_8", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (8081.16, 3099.766, -172.38745), (-0.41934205496957117, 77.83705371186907, 0.7187354420760343), (0.396307, 0.348653, 0.31777826), "Rock_9", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (8295.419, 4860.7983, 65.02111), (17.26189505539972, 13.524426346763374, 5.476687587372603), (0.17397556, 0.23917255, 0.23917255), "Rock_22", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4472.4434, 8797.499, -296.34375), (-1.143219049018669, 173.34636168382625, -0.6230467979823789), (0.23081803, 0.18316403, 0.172026), "Rock_29", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (8751.042, 5071.4565, 213.30031), (-0.6488952790520887, 25.65406344681717, 1.1121704854028982e-05), (0.12096375, 0.1861614, 0.1861614), "Rock_33", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (7091.1377, 1934.5527, -203.4975), (0.4585993276210586, -104.62728083157245, -1.2185974857107447), (0.396307, 0.41937232, 0.41799346), "Rock_63", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (7969.243, 2310.9116, -282.47046), (-0.7908631056747617, 92.15591251968375, 1.0341577805472624), (0.396307, 0.419372, 0.417993), "Rock_64", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (8745.603, 2968.5952, 183.31348), (0.0, 95.68157653032927, -0.0), (0.34966603, 0.2327739, 0.2327739), "Rock_74", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2907.335, 8683.786, -280.09143), (1.0844567401716556, -1.6531067592084863, 0.7202714828458404), (0.33177474, 0.183164, 0.24155498), "Rock_77", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5982.4346, 8620.623, -180.5531), (3.7877286684123272, 123.37691242324424, 0.47641421967000963), (0.19837533, 0.15072136, 0.108301185), "Rock_82", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (7332.647, 5187.9336, -210.22266), (-5.3034053837436455, 108.27587715058301, 0.7762081824229146), (0.198375, 0.150721, 0.12732273), "Rock_86", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4759.265, 9262.601, -14.96595), (-1.2342223285245626, 163.3335633861848, -0.41485585707981154), (0.396307, 0.348653, 0.277039), "Rock_89", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (9052.486, 5533.611, 253.55809), (5.445599326478952, 43.877573789015905, -0.8684996917657858), (0.1523809, 0.09642532, 0.13497917), "Rock_136", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3458.655, 9090.446, -47.661453), (-0.026733427307390437, 165.18327466013034, -7.094146757470552), (0.396307, 0.48372558, 0.4037255), "Rock_191", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3128.0898, 8954.328, -323.3531), (-1.143219049018669, 173.34636168382625, -0.6230467979823789), (0.3189457, 0.27129173, 0.26015365), "Rock_192", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (8837.618, 5797.7476, 250.91162), (-5.312804887575352, -142.6244937789327, 1.4787071988996556), (0.095857754, 0.096425, 0.14148723), "Rock_199", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (8353.733, 5707.7456, 232.16176), (-0.21548460764446575, 156.03126482066315, -3.8180237681421207), (0.078525886, 0.14095959, 0.10713789), "Rock_206", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (8056.7007, 5850.44, 156.64864), (-9.451570276765167, 126.32840403876786, 2.474401756747372), (0.078526, 0.14096, 0.13523681), "Rock_207", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (7734.0776, 6098.78, -62.789913), (-10.777557124489709, 121.2743729471699, 14.610505792259607), (0.173976, 0.239173, 0.239173), "Rock_208", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (7844.0283, 4713.732, -36.57584), (17.03585078623725, -33.680601184269655, -22.164883157975897), (0.34557095, 0.41076797, 0.38213718), "Rock_210", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (8702.209, 7203.606, 236.68567), (0.0, -10.987976695991945, 0.0), (0.096789576, 0.16198657, 0.091445774), "Rock_222", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (8262.486, 7349.6846, 236.68567), (0.0, -38.590697388942324, 0.0), (0.13170272, 0.161987, 0.091446), "Rock_223", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (8985.631, 7185.615, 236.68561), (0.0, 24.943016836221375, -0.0), (0.131703, 0.161987, 0.091446), "Rock_224", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (9411.448, 7488.335, 236.68561), (0.0, 57.51394496992457, -0.0), (0.131703, 0.161987, 0.091446), "Rock_225", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (9481.405, 7665.5664, 236.68561), (0.0, 87.44029633020268, -0.0), (0.131703, 0.161987, 0.091446), "Rock_226", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (9435.367, 7951.1987, 236.68561), (-3.3836362193462715, 132.93113162417723, -3.5906984624048532), (0.131703, 0.161987, 0.091446), "Rock_227", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4612.2915, 4510.3574, 336.8122), (0.0, -38.590697388942324, 0.0), (0.131703, 0.161987, 0.091446), "Rock_228", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4983.7393, 4443.6514, 336.8122), (0.0, 0.29390858847123214, -0.0), (0.131703, 0.161987, 0.091446), "Rock_229", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4372.5015, 4834.707, 336.8122), (0.0, -73.57976538728344, 0.0), (0.131703, 0.161987, 0.091446), "Rock_230", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4250.364, 5249.1787, 349.59326), (-1.6966247575232953, -73.57964850981101, 6.462955265329984e-07), (0.131703, 0.161987, 0.091446), "Rock_231", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4179.7593, 5499.9414, 357.3094), (-1.4224548150965148, -106.61386374668328, 0.9247993203324074), (0.11948568, 0.161987, 0.091446), "Rock_232", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4070.0183, 7250.796, 346.5215), (-0.27597040839418785, -112.54992478415386, -0.5863035968315894), (0.131703, 0.161987, 0.091446), "Rock_233", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4235.6006, 7734.1807, 350.94638), (-0.27597040839418785, -112.54992478415386, -0.5863035968315894), (0.091766894, 0.1096026, 0.08012582), "Rock_234", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4285.958, 8370.483, -131.41649), (-0.8446959686386044, -3.887358865599761, -13.327239053475127), (0.396307, 0.483726, 0.46550888), "Rock_245", _folder)
if a: placed += 1
else: skipped += 1

# Batch 146: StaticMesh'Rock_09' (7 instances)
_mesh_path = "/Game/Unshippable/Cinematics/Cine001/Environment/Rock_09"
_materials = ['/Game/Unshippable/Cinematics/Cine001/Environment/Materials/MI_Rock_09']
_folder = "Reconstruction/BD_BB_Outdoor_TradingPost/Meshes"
a = spawn_static_mesh(_mesh_path, _materials, (8064.836, 4915.7324, -88.0802), (0.0, -169.305485906945, 0.0), (0.669368, 1.056938, 0.25156155), "Rock_13", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (6753.769, 1377.146, -132.80298), (0.0, -7.215301680931229, 0.0), (0.775265, 0.70189136, 0.656097), "Rock_65", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4532.147, 9564.526, -84.9848), (0.0, 86.73108851036818, -0.0), (0.45474687, 0.95359284, 0.67071295), "Rock_73", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (6263.352, 9217.443, -102.2478), (0.0, 51.51321750643573, -0.0), (0.6273257, 1.0148956, 0.6273257), "Rock_83", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4638.6187, 9446.997, -132.80383), (0.0, 91.61228428900516, -0.0), (0.670676, 1.058246, 0.551508), "Rock_84", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1925.5615, 9554.348, -132.8045), (0.0, 91.61228428900516, -0.0), (0.670676, 1.058246, 0.551508), "Rock_85", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3043.9517, 9621.462, -132.80676), (0.0, 91.61228428900516, -0.0), (0.670676, 1.058246, 0.551508), "Rock_87", _folder)
if a: placed += 1
else: skipped += 1

# Batch 147: StaticMesh'Rock_09' (42 instances)
_mesh_path = "/Game/Unshippable/Cinematics/Cine001/Environment/Rock_09"
_materials = ['/Game/Unshippable/Cinematics/Cine001/Environment/Materials/MI_Rock_09_Red']
_folder = "Reconstruction/BD_BB_Outdoor_TradingPost/Meshes"
a = spawn_static_mesh(_mesh_path, _materials, (6854.3228, 4899.2827, -216.35529), (0.7629115665758566, -164.20709279983345, 0.08150239430427604), (0.639363, 0.639363, 0.947318), "Rock_11", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (7643.372, 4513.1533, -267.93225), (-0.7447509408554848, 13.89496499727055, -0.18423462715015315), (0.639363, 1.1022402, 0.947318), "Rock_12", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (7158.805, 3147.8506, -261.44043), (-0.7672118773793892, 0.4598406989154056, -0.006134032773122637), (0.639363, 1.313959, 0.947318), "Rock_14", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (7783.43, 1867.835, -269.80566), (-0.7484131541763783, -12.708343134340813, 0.1688032082167838), (0.639363, 0.86799264, 0.947318), "Rock_18", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (7766.922, 4513.129, -168.37848), (0.7629119782140193, -121.53125352332034, 0.08150220894237374), (0.639363, 0.639363, 0.947318), "Rock_20", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (7569.202, 6333.1084, -202.71051), (0.9273720077046339, -164.21515830278662, -0.5004883007881966), (0.48476407, 0.639363, 0.947318), "Rock_21", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (7367.7134, 5914.7227, -277.56152), (13.119863600397005, -166.28239698276025, -3.0589293150823416), (0.40979066, 1.0225981, 0.84114915), "Rock_39", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (7422.1426, 6517.222, -22.072021), (-0.7257690672592967, 24.097396804286383, -0.24829101567514125), (0.639363, 1.313959, 0.67887473), "Rock_44", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (6850.317, 7755.447, -86.29276), (-4.72259455039378, -140.96956880226455, 0.47140451688831403), (0.94838345, 1.313959, 0.72170836), "Rock_45", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (6527.883, 6101.0874, -58.82485), (0.4850867514835978, 26.037307251384846, 0.7688037194990736), (0.639363, 1.10224, 0.6894317), "Rock_49", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (7971.21, 3464.4238, -272.3246), (-0.7665100440209243, 2.4395763722863455, -0.03265380758895088), (0.639363, 1.10224, 0.947318), "Rock_60", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (6728.403, 5632.5186, -255.67603), (0.7629116173326876, -173.9018066562386, 0.08150201289311829), (0.639363, 0.639363, 0.947318), "Rock_61", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5600.9307, 7908.245, -240.57556), (0.5320102957910887, -133.89948305027306, 0.552833366352363), (0.639363, 0.9162091, 0.947318), "Rock_62", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5204.03, 8263.289, -42.9844), (0.3535852208654638, -117.44961360012911, 0.6808769751425937), (0.8028395, 0.810405, 0.6237292), "Rock_66", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4807.2637, 8496.961, -229.94775), (0.2761240431685792, 111.09635448688809, -0.7157593094793262), (0.427061, 0.512611, 0.623729), "Rock_67", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (8577.811, 11672.95, 160.2237), (3.294794604837193, 1.628830760340512, 0.33443877660937693), (0.67635, 1.0570629, 1.4061736), "Rock_68", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (7665.9844, 12654.704, 96.47897), (-0.7258605221979275, -76.11360523980458, -0.24829098798425567), (1.0284228, 1.313959, 1.028643), "Rock_69", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (9254.892, 3911.0815, 200.3667), (0.0, -10.55462660080259, 0.0), (0.670676, 1.058246, 0.551508), "Rock_70", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (9046.809, 2725.4531, 153.0293), (0.0, -0.5634460145751311, 0.0), (0.610231, 1.0641335, 0.954282), "Rock_71", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5679.7515, 8833.62, -241.63086), (-0.37075802675476727, 61.10041716969996, -0.6716002816134545), (0.427061, 0.512611, 0.623729), "Rock_72", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3521.7227, 9021.13, -212.73022), (-0.05227659873382257, 86.09804042565037, -0.7654419135793916), (0.427061, 0.512611, 0.623729), "Rock_76", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2198.712, 9334.407, -195.02026), (-0.03427125800225711, 87.43965128148255, -0.7663879133466309), (0.639363, 1.10224, 1.082628), "Rock_78", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2075.25, 8404.099, -193.36737), (-0.10092161813573786, 82.44011308411588, -0.7604980359195527), (0.639363, 1.10224, 1.082628), "Rock_80", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5276.747, 9029.236, -297.8192), (-0.014923071884443959, 88.88473733289455, -0.7669678313188062), (0.639363, 1.313959, 0.947318), "Rock_81", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (6154.876, 6993.6895, -110.75351), (4.4027189948362455, 38.85192777356239, -1.6700440763427467), (0.70948166, 1.10224, 0.83606), "Rock_88", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (10006.967, 15681.471, 132.9544), (-0.6589661328528023, 23.19497500348409, -0.045288094787713305), (0.6342995, 0.5724776, 0.8760025), "Rock_91", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (8971.965, 10699.663, 108.264404), (-0.6265869172377372, 39.0276875884513, 0.20913707331489795), (0.954282, 0.9186039, 1.195985), "Rock_93", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4554.4253, 8292.12, -226.57666), (-0.03424068930173676, 87.43971478252021, -0.7663879616219674), (0.639363, 1.10224, 1.0826275), "Rock_188", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (6321.675, 6985.361, -232.42676), (0.7050665737791715, -146.35156579565958, -4.17922897637133), (0.639363, 0.6943196, 0.45547047), "Rock_200", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (8393.449, 10647.443, 113.03266), (-4.461181166657342, 1.5835734789032871, 0.3348812297455035), (0.31305414, 0.37439042, 0.69024366), "Rock_209", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (7791.404, 15404.502, 186.19821), (-0.7257690093507614, -143.52444030934595, -0.24829103950952194), (1.028423, 1.313959, 1.028643), "Rock_235", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5946.373, 14831.967, 284.23288), (-0.7257690093507614, -143.52444030934595, -0.24829103950952194), (1.028423, 1.313959, 1.028643), "Rock_236", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5564.5474, 16266.906, 284.23325), (-0.7257690607047417, 18.101164143842716, -0.2482910234566086), (1.028423, 1.313959, 1.028643), "Rock_237", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5650.8945, 17261.914, 284.23325), (-0.7257691172912799, 12.941404204073912, -0.24829104755659687), (1.028423, 1.313959, 1.028643), "Rock_238", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (7292.15, 17261.914, 284.23325), (2.358893137752156, -161.211924091668, 0.8006314496426816), (1.028423, 1.313959, 0.7590652), "Rock_239", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (7736.601, 16421.822, 284.2335), (2.3588929862956176, -161.21192410070614, 0.8006309596028491), (1.028423, 1.313959, 0.759065), "Rock_240", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (8139.865, 14569.952, 201.01779), (2.3588946064436627, -176.39732225371336, 0.8006309863271495), (1.028423, 1.313959, 1.1323704), "Rock_241", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5954.2886, 14513.69, 291.80356), (2.3588950648656763, -176.39732225081295, 0.8006310009435291), (1.028423, 1.313959, 1.13237), "Rock_242", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (6645.8174, 13747.69, 330.0344), (5.143576401046128, -176.5020790707997, -0.33145141869570977), (1.028423, 1.313959, 1.13237), "Rock_243", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (7595.8564, 5509.2407, -31.312653), (-0.7257690773666227, -0.5734253944278976, -0.24829105601197393), (1.0071216, 1.313959, 0.68851703), "Rock_244", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5890.095, 8916.795, -115.167854), (1.4561878722572734, -127.58217284952948, -5.468688565975772), (0.71085703, 1.10224, 0.6047519), "Rock_246", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (6059.7065, 5969.9326, 55.172222), (0.4850870967887304, 7.382195718374868, 0.7688030575351058), (0.639363, 1.10224, 0.638444), "Rock_247", _folder)
if a: placed += 1
else: skipped += 1

# Batch 148: StaticMesh'Tree_01' (12 instances)
_mesh_path = "/Game/Unshippable/Cinematics/Cine001/Environment/Tree_01"
_materials = ['/Game/Unshippable/Cinematics/Cine001/Environment/Materials/MI_Tree_01']
_folder = "Reconstruction/BD_BB_Outdoor_TradingPost/Meshes"
a = spawn_static_mesh(_mesh_path, _materials, (9666.277, 10416.88, 651.3716), (0.0, -10.881439698580072, 0.0), (0.49502236, 0.49502236, 0.49502236), "Tree_698", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (8158.731, 7703.249, 245.06343), (-0.6645201919654433, 83.39966254647078, 0.3056155157863056), (0.4732885, 0.4732885, 0.4732885), "Tree_742", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (10524.538, 6607.9146, 646.5827), (1.426034243702363, 143.20498567563394, 2.0538889341723117e-06), (0.5332841, 0.5332841, 0.5332841), "Tree_747", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (11217.886, 8383.331, 751.1466), (-0.8469236107207301, -176.83006583404253, 2.783451415809562e-08), (0.7390887, 0.7390887, 0.7390887), "Tree_760", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (6711.2344, 10791.499, 464.83777), (-5.6696775625880536, -72.08941147044794, 1.1349453848093665e-06), (0.7668988, 0.7668988, 0.7668988), "Tree_1072", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (8759.47, 7399.243, 252.06473), (0.0, 150.28974213515988, -0.0), (0.4776356, 0.4776356, 0.4776356), "Tree_1094", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (7427.9526, 6134.7593, -25.87153), (-16.03405891788954, 141.828937928897, -3.7793580011319703), (0.51280373, 0.6151918, 0.6151918), "Tree_1255", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5669.966, 5020.6963, 347.97723), (0.0, -25.6263424419515, 0.0), (0.6372829, 0.6372829, 0.6372829), "Tree_1311", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4960.0, 4565.0, 365.0), (7.112742048638088, 19.13641704676724, 2.4602719791975236), (0.8084309, 0.8084309, 0.8084309), "Tree_1406", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (8047.995, 11048.928, 173.3331), (-2.4202573419262206, 108.99026256061055, -0.19747933413050595), (0.43809918, 0.43809918, 0.43809918), "Tree_1486", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (6151.415, 9881.73, 278.80957), (30.517603783575222, 160.0581443903886, 1.7314139595826876e-05), (0.56577986, 0.56577986, 0.56577986), "Tree_1611", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (8589.284, 10020.691, 210.2663), (3.7200145823252906, 160.14861052206322, 2.0133819854028377e-06), (1.0, 1.0, 1.0), "Tree_01_676", _folder)
if a: placed += 1
else: skipped += 1

# Batch 149: StaticMesh'Tree_02' (12 instances)
_mesh_path = "/Game/Unshippable/Cinematics/Cine001/Environment/Tree_02"
_materials = ['/Game/Unshippable/Cinematics/Cine001/Environment/Materials/MI_Tree_02']
_folder = "Reconstruction/BD_BB_Outdoor_TradingPost/Meshes"
a = spawn_static_mesh(_mesh_path, _materials, (10147.215, 8841.216, 854.7126), (-2.1248475556655517, 83.66321352152808, -7.16793844319085), (2.3412783, 2.3412783, 2.3412783), "Tree_2", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (11425.564, 8544.064, 735.5212), (-0.44662478052377325, 63.243592044946865, 2.5339129025125176), (4.016149, 5.2108884, 4.016149), "Tree_4", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (11639.695, 10326.713, 651.20416), (-1.2500610410201698, -155.04351310521864, 4.3780522164886495), (4.0161486, 4.0161486, 4.0161486), "Tree_153", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4560.063, 7913.2764, 350.0), (0.0, 0.0, -0.0), (4.057959, 4.057959, 4.057959), "Tree_167", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4339.8145, 5760.047, 349.9994), (0.0, -56.58981251565752, 0.0), (5.091344, 5.091344, 5.091344), "Tree_437", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (9823.287, 10424.835, 647.5781), (0.0, 25.94146496883489, -0.0), (1.9072499, 1.9072499, 1.9072499), "Tree_692", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (9441.339, 11772.042, 645.79224), (-6.427032669557033, -135.84800493708505, 1.182573699844155e-06), (2.7596543, 2.7596543, 2.7596543), "Tree_741", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (10328.607, 6576.3613, 627.9669), (0.0, 24.76528055372301, -0.0), (3.0864754, 3.0864754, 3.0864754), "Tree_744", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (10037.577, 7181.69, 654.04803), (4.757595501135144, -133.2696430767344, 1.5438289404352929e-06), (1.812281, 1.812281, 1.812281), "Tree_756", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5339.602, 5163.546, 329.21747), (0.0, -161.26572703791075, 0.0), (2.594971, 2.594971, 2.594971), "Tree_1305", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4215.566, 10330.779, 630.0), (0.0, -38.809415974087145, 0.0), (2.9583893, 2.9583893, 2.9583893), "Tree_1596", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (6523.649, 10543.156, 445.6827), (-5.000000015502797, -63.15179316933244, 2.795581789322846e-07), (4.2663426, 4.2663426, 4.2663426), "Tree_02_161", _folder)
if a: placed += 1
else: skipped += 1

# Batch 150: StaticMesh'Tree_07' (6 instances)
_mesh_path = "/Game/Unshippable/Cinematics/Cine001/Environment/Tree_07"
_materials = ['/Game/Unshippable/Cinematics/Cine001/Environment/Materials/MI_Tree_07']
_folder = "Reconstruction/BD_BB_Outdoor_TradingPost/Meshes"
a = spawn_static_mesh(_mesh_path, _materials, (8356.163, 10249.509, 194.22496), (6.813783212029325, 34.166353234294455, 3.012506464848017), (4.016149, 5.210888, 4.016149), "Tree_8", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3731.9404, 6512.8657, 345.3479), (0.0, 0.0, -0.0), (3.761889, 3.761889, 3.761889), "Tree_10", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5826.89, 5729.3423, 336.76404), (0.0, 0.0, -0.0), (3.2722661, 3.2722661, 3.2722661), "Tree_1171", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4745.0, 4580.0, 325.0), (0.0, 0.0, -0.0), (3.2750292, 3.2750292, 3.2750292), "Tree_1409", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5146.001, 7278.152, 345.3479), (0.0, 0.0, -0.0), (3.7618895, 3.7618895, 3.7618895), "Tree_1793", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (8909.249, 9170.089, 206.56993), (2.574083365495382, 42.79073527728809, 3.1566425817711594), (4.016149, 5.210888, 4.016149), "Tree_07_144", _folder)
if a: placed += 1
else: skipped += 1

# Batch 151: StaticMesh'Tree_10' (11 instances)
_mesh_path = "/Game/Unshippable/Cinematics/Cine001/Environment/Tree_10"
_materials = ['/Game/Unshippable/Cinematics/Cine001/Environment/Materials/MI_Tree_10']
_folder = "Reconstruction/BD_BB_Outdoor_TradingPost/Meshes"
a = spawn_static_mesh(_mesh_path, _materials, (8685.285, 8767.579, 226.0867), (4.288994959358451, 149.7058183876046, 0.17426402565198842), (2.5209382, 2.5209382, 2.5209382), "Tree_673", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (10271.03, 10552.774, 637.0898), (1.9185518995629776, 28.32122711479159, -0.400726388704534), (1.6002741, 1.6002741, 1.6002741), "Tree_685", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (9782.076, 11749.762, 642.91364), (3.841475094984665, -36.68506112618699, 5.544197877320709e-07), (2.8704014, 2.8704014, 2.8704014), "Tree_732", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (10140.46, 7023.035, 609.40607), (-1.9925843866256432, -147.66530379481998, 10.387613361238756), (2.0704315, 2.0704315, 2.0704315), "Tree_753", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (10930.872, 9206.011, 612.0945), (-7.315704882955891, 133.83144078052788, 1.915560905316444e-06), (2.242428, 2.242428, 2.242428), "Tree_872", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5434.716, 7197.6694, 357.8592), (0.0, 170.92378456949348, -0.0), (2.8369668, 2.8369668, 2.8369668), "Tree_1246", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4525.0, 5520.0, 350.0), (0.8969404167057533, 34.89098528629714, -8.463257613924938), (2.2881505, 2.2881505, 2.2881505), "Tree_1418", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5683.2515, 5651.9517, 339.79526), (6.964265041527628, 43.81063219313847, 1.3938205752980117e-06), (1.0, 1.0, 1.0), "Tree_1471", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5935.914, 5278.7095, 329.0769), (8.09066008707359, -97.52989589556712, 2.891464897242974e-06), (1.4861597, 1.4861597, 1.4861597), "Tree_1474", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (7433.441, 10567.85, 136.18274), (5.615539087769792, -73.31682736750345, 12.762705401264755), (1.0, 1.0, 1.0), "Tree_1483", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4314.8335, 9941.89, 635.0075), (3.134831921914267, -114.8679739914763, 1.109840519394073e-06), (1.6748053, 1.6748053, 1.6748053), "Tree_1599", _folder)
if a: placed += 1
else: skipped += 1

# Batch 152: StaticMesh'Tree_12' (20 instances)
_mesh_path = "/Game/Unshippable/Cinematics/Cine001/Environment/Tree_12"
_materials = ['/Game/Unshippable/Cinematics/Cine001/Environment/Materials/MI_Tree_12']
_folder = "Reconstruction/BD_BB_Outdoor_TradingPost/Meshes"
a = spawn_static_mesh(_mesh_path, _materials, (8688.408, 9263.461, 221.9172), (8.272226751164329, -39.925504618533544, 0.8927149808804032), (1.0, 1.0, 1.0), "Tree_670", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (10953.069, 10618.733, 641.0044), (0.0, 168.26503551009588, -0.0), (1.0, 1.0, 1.0), "Tree_682", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (10363.913, 10424.03, 612.567), (-9.248901633569217, -83.65723084558519, 0.3282786446167566), (1.0, 1.0, 1.0), "Tree_688", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (9121.32, 12567.888, 706.7692), (20.961522551582526, 53.652816697117835, -3.3942871808052324), (1.8484339, 1.8484339, 1.8484339), "Tree_735", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (8884.471, 8202.193, 236.07603), (0.0, -11.613709130439082, 0.0), (1.0, 1.0, 1.0), "Tree_745", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (10301.721, 12227.373, 649.66846), (0.0, 26.59491548985887, -0.0), (1.0, 1.0, 1.0), "Tree_749", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (10020.622, 6479.742, 631.656), (30.491204561730175, 2.2505046153513804, 34.56021673703977), (1.0, 1.0, 1.0), "Tree_750", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (10026.887, 7035.261, 656.21826), (19.570021513118643, 144.95432349346288, 5.802857803932731), (0.44283792, 0.44283792, 0.44283792), "Tree_762", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (11029.654, 8979.376, 643.7037), (-4.445648484419686, 30.784650536518676, -0.20233163338034388), (1.3735312, 1.3735312, 1.3735312), "Tree_869", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (7234.787, 10827.417, 206.8413), (0.0, -97.06970546769941, 0.0), (1.0, 1.0, 1.0), "Tree_1066", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (8243.0, 7653.3286, 243.15454), (1.7504037831547854, -51.000866429338096, 2.0453632342970827), (0.5465732, 0.5465732, 0.5465732), "Tree_1091", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (7208.1343, 6900.339, -66.525085), (0.0, -65.78131471937107, 0.0), (1.0, 1.0, 1.0), "Tree_1249", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5609.7925, 5577.0303, 338.4319), (1.8590686194567922, 69.49253870134338, -0.26724230935922805), (1.0, 1.0, 1.0), "Tree_1308", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4580.0, 4750.0, 335.0), (0.0, -53.56478948647027, 0.0), (1.0, 1.0, 1.0), "Tree_1412", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5575.0, 7075.0, 355.0), (0.0, -38.60406504364859, 0.0), (1.0, 1.0, 1.0), "Tree_1424", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4942.4136, 6133.512, 336.52896), (0.0, -96.65963939593325, 0.0), (1.0, 1.0, 1.0), "Tree_1462", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5241.489, 5769.859, 330.69708), (0.0, 0.0, -0.0), (1.0, 1.0, 1.0), "Tree_1468", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (7615.5146, 10073.422, 122.97049), (0.0, 86.5694017116757, -0.0), (1.0, 1.0, 1.0), "Tree_1477", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4445.0, 10895.0, 650.0), (0.0, -17.85662763459451, 0.0), (1.6185766, 1.6185766, 1.6185766), "Tree_1602", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (6808.152, 9850.903, 142.50641), (-5.724334375189386, -21.449522690777407, 2.393780663157376e-06), (1.0, 1.0, 1.0), "Tree_1614", _folder)
if a: placed += 1
else: skipped += 1

# Batch 153: StaticMesh'Tree_13' (15 instances)
_mesh_path = "/Game/Unshippable/Cinematics/Cine001/Environment/Tree_13"
_materials = ['/Game/Unshippable/Cinematics/Cine001/Environment/Materials/MI_Tree_13']
_folder = "Reconstruction/BD_BB_Outdoor_TradingPost/Meshes"
a = spawn_static_mesh(_mesh_path, _materials, (10489.194, 10063.076, 584.7532), (-2.530120707464305, -116.15291822988951, 1.2418344115837299), (1.0, 1.0, 1.0), "Tree_679", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (10060.646, 10520.889, 687.20184), (-16.05422750787868, 16.11795438917557, 8.904081338194404), (1.357207, 1.357207, 1.357207), "Tree_727", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (9390.483, 11605.842, 830.37354), (51.90394697353749, -83.90994503970946, 5.329699006760131e-05), (1.951379, 2.5121467, 2.5121467), "Tree_738", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (8415.256, 7410.8237, 250.34361), (-2.3282166326092133, -27.01043681620162, 1.272654809861491e-06), (1.0, 1.0, 1.0), "Tree_739", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (10053.659, 12736.014, 673.3122), (3.6679341638980367, 50.7344291834899, 6.108229673876208e-08), (1.0, 1.0, 1.0), "Tree_752", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (9985.015, 6978.4146, 641.86786), (1.1635450055590548, 45.26961134749299, -7.623170217507064), (0.6082691, 0.6082691, 0.6082691), "Tree_759", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (10482.587, 7567.649, 639.40857), (0.0, -101.06640221471169, 0.0), (1.0, 1.0, 1.0), "Tree_763", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (11299.824, 8591.802, 787.9443), (15.549478235866513, 0.0, -0.0), (1.0, 1.0, 1.0), "Tree_866", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (7107.5796, 10595.955, 269.2424), (-20.88775788378473, 0.0, -0.0), (1.2592714, 1.2592714, 1.2592714), "Tree_1069", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (6505.2417, 6892.461, -109.5721), (-16.465451110865885, -32.77227836848519, 5.275124561729023), (1.0, 1.0, 1.0), "Tree_1252", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4328.796, 5335.8555, 372.23422), (-7.366759869916236, -69.28326844113421, 2.7784479909706377e-06), (1.0, 1.0, 1.0), "Tree_1314", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4345.0, 7635.0, 345.0), (0.0, -105.22558468614952, 0.0), (1.3204663, 1.3204663, 1.3204663), "Tree_1427", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4463.9185, 5922.7876, 341.60995), (-1.3807066486076944, 101.33118473522373, 1.1367654697597918), (1.0, 1.0, 1.0), "Tree_1465", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (7239.1514, 9820.719, 134.07591), (-1.7342529312526063, 14.426354491643004, 1.6461815062510985e-06), (1.0, 1.0, 1.0), "Tree_1480", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5174.3794, 9914.849, 633.3933), (4.227148869691576, 42.51065471951192, 2.456856335092397e-07), (1.0, 1.0, 1.0), "Tree_1608", _folder)
if a: placed += 1
else: skipped += 1

# Batch 154: StaticMesh'Rock_19' (12 instances)
_mesh_path = "/Game/Unshippable/Cinematics/Cine003/Environment/Rock_19"
_materials = ['/Game/Unshippable/Cinematics/Cine003/Environment/Material/MI_Rock_27']
_folder = "Reconstruction/BD_BB_Outdoor_TradingPost/Meshes"
a = spawn_static_mesh(_mesh_path, _materials, (7791.896, 6616.8877, -73.414894), (1.6487168252439282, 92.29932135937182, 8.836523321983622), (0.98399276, 1.0765231, 1.0765231), "Rock_30", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (7677.603, 6814.576, -243.17694), (1.3087592654566622, 100.44362657792173, 8.205066122528462), (1.0, 1.0, 1.0), "Rock_194", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (8118.418, 6935.8203, 259.05542), (12.145108663785386, -59.78192498498807, 12.792727034798), (1.0599128, 1.0272791, 1.0), "Rock_196", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (6651.5596, 11699.5205, 170.49316), (-0.4726257551780237, -125.33586482334357, 3.2238363453832033), (1.6283065, 1.1071885, 1.5683933), "Rock_198", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (12320.289, 14103.313, 1407.323), (-3.831298361073996, -163.47547229962808, 8.513592672167054), (1.7306995, 1.2095805, 1.6707855), "Rock_201", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (12176.863, 14572.543, 2410.8064), (10.023323688817339, 40.82727631408928, 18.944623723473583), (1.7307, 1.209581, 1.5035312), "Rock_202", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2717.4392, 7265.899, -412.64746), (-12.805969462719219, 150.91422890328414, 3.188951699154487), (2.171203, 2.171203, 2.0811152), "Rock_203", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3675.8267, 4153.3457, 44.544952), (-3.9551693201461746, 92.18249087900647, -2.696838091453466), (2.4184556, 2.171203, 2.081115), "Rock_205", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5958.785, 2430.7463, 44.544952), (-3.9551694988760824, -124.04171555300984, -2.69683859906173), (2.566139, 2.3188858, 2.228798), "Rock_211", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5286.1406, 863.7433, 44.544952), (-3.955169728519912, -129.49980366472832, -2.6968383923679884), (2.566139, 2.318886, 2.228798), "Rock_212", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2630.0234, 7975.7803, -119.8191), (2.3638050837914664, 171.31715500424394, -1.4873352352187406), (1.9513763, 1.9513763, 1.8612887), "Rock_221", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (9050.362, 6561.4775, 217.96376), (-0.6871037691634112, 30.129533467162577, 11.489905150106829), (1.142892, 0.7347005, 1.142892), "Rock_1526", _folder)
if a: placed += 1
else: skipped += 1

# Batch 155: StaticMesh'SM_Wooden_Floor_Ruined_01' (11 instances)
_mesh_path = "/Game/Unshippable/ThirdParty/Lordenfel/Environment/Architecture/WoodenObjects/SM_Wooden_Floor_Ruined_01"
_materials = ['/Game/Unshippable/ThirdParty/Lordenfel/Environment/Materials/MI_Wood_01']
_folder = "Reconstruction/BD_BB_Outdoor_TradingPost/Meshes"
a = spawn_static_mesh(_mesh_path, _materials, (7431.531, 9458.764, 109.44542), (5.444391919318, 92.55414390509142, 1.244357720859509e-06), (0.6618806, 0.7364937, 1.0), "SM_Wooden_Floor_Ruined_10", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (8315.89, 9508.018, 164.72006), (1.365259595174226, -85.08154388815525, -6.777343216342141), (0.7072585, 1.0, 1.0), "SM_Wooden_Floor_Ruined_11", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (10661.681, 10559.632, 639.7734), (3.8011291413699153, 29.776712881842354, -8.270202260315601), (0.5137247, 0.5137247, 0.37172636), "SM_Wooden_Floor_Ruined_13", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (10563.595, 10833.865, 652.3794), (0.0, 1.1668370041730787, -0.0), (0.513725, 0.513725, 0.371726), "SM_Wooden_Floor_Ruined_14", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (10692.412, 11263.477, 654.77216), (2.9395765880930655, -5.003539949429017, 8.258739912471044e-08), (0.513725, 0.513725, 0.371726), "SM_Wooden_Floor_Ruined_15", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (10729.705, 11557.953, 660.8547), (5.169129937889893, 20.085913903336017, 1.2472206700454322), (0.513725, 0.513725, 0.371726), "SM_Wooden_Floor_Ruined_16", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (8718.211, 9542.086, 201.6648), (1.2767596693417844e-07, -88.45079747031284, -3.28591854337151), (0.74164003, 1.0, 1.0), "SM_Wooden_Floor_Ruined_18", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (9856.213, 12149.04, 667.13885), (0.5623978551765277, 44.69491264516626, -2.0958863668076995), (0.513725, 0.513725, 0.371726), "SM_Wooden_Floor_Ruined_23", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (10121.657, 10802.848, 652.289), (0.7624142588953359, 90.26071491141558, -1.282379025826575), (0.42289504, 0.42289504, 0.28089607), "SM_Wooden_Floor_Ruined_25", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (9803.177, 13012.487, 695.4323), (-2.2100219091870623, -4.606720161284731, -1.7340392974013255), (0.513725, 0.513725, 0.371726), "SM_Wooden_Floor_Ruined_26", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (6961.4746, 9390.197, 111.737686), (-4.481506012979815, -75.5571283080634, 5.052973170346614), (1.0, 1.0, 1.0), "SM_Wooden_Floor_Ruined_313", _folder)
if a: placed += 1
else: skipped += 1

# Batch 156: StaticMesh'SM_Wooden_Floor_Ruined_01' (3 instances)
_mesh_path = "/Game/Unshippable/ThirdParty/Lordenfel/Environment/Architecture/WoodenObjects/SM_Wooden_Floor_Ruined_01"
_materials = ['/Game/Unshippable/ThirdParty/Lordenfel/Environment/Materials/MI_Wood_2']
_folder = "Reconstruction/BD_BB_Outdoor_TradingPost/Meshes"
a = spawn_static_mesh(_mesh_path, _materials, (11148.651, 9724.151, 600.0656), (-0.09036254265350947, -106.62777288817021, 0.07272722399663817), (0.513725, 0.513725, 0.371726), "SM_Wooden_Floor_Ruined_2", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (10645.148, 8872.616, 600.25885), (0.0, 177.29191248571468, -0.0), (0.6543712, 0.5100988, 0.33004603), "SM_Wooden_Floor_Ruined_9", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (10281.978, 9599.271, 607.1721), (-0.10549955796478563, -78.8325855819142, 3.780879843891757), (0.513725, 0.513725, 0.371726), "SM_Wooden_Floor_Ruined_01_2", _folder)
if a: placed += 1
else: skipped += 1

# Batch 157: StaticMesh'SM_Wooden_Floor_Ruined_02' (7 instances)
_mesh_path = "/Game/Unshippable/ThirdParty/Lordenfel/Environment/Architecture/WoodenObjects/SM_Wooden_Floor_Ruined_02"
_materials = ['/Game/Unshippable/ThirdParty/Lordenfel/Environment/Materials/MI_Wood_01']
_folder = "Reconstruction/BD_BB_Outdoor_TradingPost/Meshes"
a = spawn_static_mesh(_mesh_path, _materials, (10736.964, 10346.869, 610.3977), (1.3803811191499262, 15.896065524848296, -3.4799199367101994), (0.513725, 0.513725, 0.371726), "SM_Wooden_Floor_Ruined_12", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (10553.284, 11845.835, 652.673), (1.541320785504254, 40.87250426866906, 0.901493688944534), (0.513725, 0.513725, 0.371726), "SM_Wooden_Floor_Ruined_17", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (10369.583, 11994.991, 652.4493), (0.7368475914985314, 76.18014311065595, -0.005798363752174501), (0.513725, 0.513725, 0.371726), "SM_Wooden_Floor_Ruined_19", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (10014.013, 12051.657, 658.77673), (0.7368478693487767, 76.17924575864976, -2.00628654625322), (0.513725, 0.513725, 0.371726), "SM_Wooden_Floor_Ruined_20", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (9737.748, 12353.695, 677.50195), (-1.1886595017223494, 22.24108157813236, -2.545135551258192), (0.513725, 0.513725, 0.371726), "SM_Wooden_Floor_Ruined_21", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (9667.475, 12683.192, 691.0066), (-2.352386610390072, -9.594697184795717, -1.5354003208584999), (0.513725, 0.513725, 0.371726), "SM_Wooden_Floor_Ruined_22", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (10287.868, 10834.301, 652.70984), (0.0, 103.65019588140753, -0.0), (0.513725, 0.513725, 0.371726), "SM_Wooden_Floor_Ruined_24", _folder)
if a: placed += 1
else: skipped += 1

# Batch 158: StaticMesh'SM_Wooden_Floor_Ruined_02' (6 instances)
_mesh_path = "/Game/Unshippable/ThirdParty/Lordenfel/Environment/Architecture/WoodenObjects/SM_Wooden_Floor_Ruined_02"
_materials = ['/Game/Unshippable/ThirdParty/Lordenfel/Environment/Materials/MI_Wood_2']
_folder = "Reconstruction/BD_BB_Outdoor_TradingPost/Meshes"
a = spawn_static_mesh(_mesh_path, _materials, (10671.306, 8670.899, 601.40326), (1.122778045821887, -2.0699770859305064, 0.45466783328015004), (0.69224983, 0.43423903, 0.69224983), "SM_Wooden_Floor_Ruined_4", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (10952.574, 9774.956, 600.3274), (0.3496876689426277, 93.85604317877811, -0.7330627806686408), (0.513725, 0.513725, 0.371726), "SM_Wooden_Floor_Ruined_5", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (11777.268, 9589.577, 599.729), (0.21366196487208589, 91.85339054313545, 0.4091619624016872), (0.513725, 0.513725, 0.371726), "SM_Wooden_Floor_Ruined_6", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (10095.344, 8101.476, 635.3426), (4.281188924248174, -102.2433671239256, -0.14031962932225486), (0.513725, 0.513725, 0.371726), "SM_Wooden_Floor_Ruined_8", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (10277.699, 7876.089, 648.2036), (0.054532230720763394, 167.42023065650437, -3.3872065785842653), (0.513725, 0.513725, 0.371726), "SM_Wooden_Floor_Ruined_27", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (11380.091, 9641.046, 600.4885), (0.36658306974536015, 66.85362401313525, 0.28052596171446953), (0.513725, 0.513725, 0.371726), "SM_Wooden_Floor_Ruined_02_6", _folder)
if a: placed += 1
else: skipped += 1

# Batch 159: StaticMesh'SM_Cliff_01' (2 instances)
_mesh_path = "/Game/Unshippable/ThirdParty/Lordenfel/Environment/Rocks/SM_Cliff_01"
_materials = ['/Game/Unshippable/ThirdParty/Lordenfel/Environment/Materials/MI_Cliff_01']
_folder = "Reconstruction/BD_BB_Outdoor_TradingPost/Meshes"
a = spawn_static_mesh(_mesh_path, _materials, (3792.205, 4915.462, 371.05353), (-4.816069917532432, -170.625590968249, 86.65062268432794), (0.63832515, 0.8584614, 0.63832515), "SM_Cliff_849", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (8995.41, 6141.613, 322.531), (0.5537550759436343, -42.83770898757605, -78.01743436955492), (0.540737, 0.540737, 0.540737), "SM_Cliff_1381", _folder)
if a: placed += 1
else: skipped += 1

# Batch 160: StaticMesh'SM_Cliff_01' (1 instances)
_mesh_path = "/Game/Unshippable/ThirdParty/Lordenfel/Environment/Rocks/SM_Cliff_01"
_materials = ['/Game/Unshippable/ThirdParty/Lordenfel/Environment/Materials/MI_Lordenfel_RedRock_01']
_folder = "Reconstruction/BD_BB_Outdoor_TradingPost/Meshes"
a = spawn_static_mesh(_mesh_path, _materials, (1870.4865, 9765.647, 467.8688), (-11.235624494595568, 84.21904629106396, -85.80593264929534), (1.494153, 1.494153, 1.494153), "SM_Cliff_148", _folder)
if a: placed += 1
else: skipped += 1

# Batch 161: StaticMesh'SM_Cliff_01' (1 instances)
_mesh_path = "/Game/Unshippable/ThirdParty/Lordenfel/Environment/Rocks/SM_Cliff_01"
_materials = ['/Game/Unshippable/ThirdParty/Lordenfel/Environment/Materials/MI_Lordenfel_RedRock_8x8x8_B']
_folder = "Reconstruction/BD_BB_Outdoor_TradingPost/Meshes"
a = spawn_static_mesh(_mesh_path, _materials, (7707.357, 15906.199, 299.0775), (1.3575494236812132e-05, 27.5150758635444, 91.6772274846949), (1.75059, 1.0, 1.0), "SM_Cliff_1625", _folder)
if a: placed += 1
else: skipped += 1

# Batch 162: StaticMesh'SM_Cliff_01' (188 instances)
_mesh_path = "/Game/Unshippable/ThirdParty/Lordenfel/Environment/Rocks/SM_Cliff_01"
_materials = ['/Game/Unshippable/ThirdParty/Lordenfel/Environment/Materials/MI_Lordenfel_RedRock_Cliff_01']
_folder = "Reconstruction/BD_BB_Outdoor_TradingPost/Meshes"
a = spawn_static_mesh(_mesh_path, _materials, (10595.815, 13187.045, 598.90106), (36.849906838780825, 5.835294241809357, -86.39379831904863), (0.6418779, 0.44883716, 0.44883716), "SM_Cliff_15", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (12131.676, 8501.252, 305.0679), (13.580277537304289, -88.82694675001693, -8.225768016875637), (2.20693, 2.743559, 1.5), "SM_Cliff_24", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (10181.299, 3784.1123, 682.1918), (-33.93081525033984, 1.5743288078808206, -12.023681715920679), (2.6790528, 2.6790528, 2.2561166), "SM_Cliff_37", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (10257.81, 3583.5437, 1073.9873), (2.691011626764329, -85.16120551883691, 30.122031634857517), (3.725432, 4.972422, 2.7173378), "SM_Cliff_44", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (7875.2114, 7318.383, 188.76965), (-3.0533745708377293, -176.9095376363796, -4.5232537203383805), (1.2030092, 1.8233747, 1.1391335), "SM_Cliff_45", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3966.3186, 5013.8037, 455.1347), (0.0, 0.0, -45.000056798727684), (0.87036824, 1.0413469, 0.87036824), "SM_Cliff_49", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (9918.463, 14504.082, 625.61707), (2.9140233504348196, 54.55905959446859, 177.45651639450782), (1.0, 1.0, 1.0), "SM_Cliff_52", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (8088.7866, 6291.124, 629.1008), (2.4393544186140406, -5.395569546281707, 6.734601482775673), (1.6947458, 1.4844683, 1.5947689), "SM_Cliff_54", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (10106.536, 10032.05, 415.86252), (59.81806055913689, -3.698550793429901, 19.79256376819825), (1.1942868, 1.1942868, 0.835628), "SM_Cliff_58", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (8877.505, 14085.231, 1596.4491), (-24.87603909239809, 23.16260230894773, 21.465536423235392), (2.36072, 2.7184112, 2.598776), "SM_Cliff_61", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (8999.865, 11947.39, 638.3808), (-6.903838172477159, 117.21103921733521, 21.659671012397013), (0.65610194, 0.65610194, 0.65610194), "SM_Cliff_69", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (7894.7695, 6679.4976, 503.1983), (2.7560840657347794, -136.75565352841997, 3.2459643715646522), (1.3816007, 2.1105483, 1.2835107), "SM_Cliff_70", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (8319.183, 16290.568, 291.90445), (10.933727404431037, -85.9098816714523, 24.824003378096954), (3.9064724, 3.7322106, 2.3307664), "SM_Cliff_75", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (9180.104, 10346.589, 390.4523), (30.078430616101926, -123.21273277174254, 103.58354598135367), (1.442395, 1.9731605, 1.083736), "SM_Cliff_87", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (9654.068, 15921.296, 3056.195), (-16.314786160189687, -22.49969525768342, 15.013124811529662), (2.298904, 2.298904, 2.0287774), "SM_Cliff_88", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (11891.076, 11431.939, 615.737), (4.99171331435249, -66.85797237861539, -7.600066879310081), (2.20693, 1.7831831, 1.9904233), "SM_Cliff_96", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (8640.796, 10753.258, 321.04126), (-32.05838118175473, 14.337920450597098, 177.64934834311828), (1.0715646, 1.2555608, 1.2555608), "SM_Cliff_109", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (9577.792, 17356.098, 2760.1775), (-23.02270816024731, 28.76898253443363, -6.579987691732162), (3.1059408, 3.1059408, 2.5062778), "SM_Cliff_126", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (11862.195, 10894.251, 671.473), (-3.031646480504852, -40.33303909527446, -177.4287708960865), (1.5254639, 1.7921503, 1.7921503), "SM_Cliff_138", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3375.4272, 9625.095, 522.058), (-5.940887146046382, 82.58175181097604, -81.1163555956586), (1.494153, 1.494153, 1.494153), "SM_Cliff_142", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2327.0908, 9813.335, 261.52856), (-63.82986161263079, -97.12699182369236, 96.12948388787781), (2.325349, 1.621344, 1.621344), "SM_Cliff_154", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (9184.347, 7113.8184, 279.24197), (-9.846528271813744, -131.7537921837501, 10.151592984231167), (1.0, 1.0, 1.0), "SM_Cliff_161", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (9543.168, 7335.426, 216.09134), (-4.980926688153731, -120.0188173570954, 0.4368820528532499), (1.0, 1.0, 1.0), "SM_Cliff_174", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (9306.288, 14877.466, 1791.4302), (-19.85052671854888, 12.066749848456707, 7.961247365227362), (2.7171662, 3.6630518, 2.9463067), "SM_Cliff_179", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (8709.861, 11844.175, 362.7382), (28.87436249068931, 178.72087728297362, 159.8755498396267), (1.442395, 1.442395, 1.083736), "SM_Cliff_183", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5688.3013, 11134.854, 842.58044), (-8.260315326310788, -13.0361336475647, 2.650881276032204), (2.5571234, 2.5571234, 1.7163838), "SM_Cliff_190", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (9669.712, 7146.5527, 413.2781), (7.3365389233914104, -17.179016966387113, 90.8621248381565), (1.3450558, 1.8028558, 0.84764606), "SM_Cliff_191", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (9755.661, 7193.286, 301.60904), (-6.52581982431756, -46.0108008222466, 92.38437254195503), (0.9104089, 1.611792, 0.94947904), "SM_Cliff_197", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (10780.513, 14617.111, 2489.8672), (-15.470365527240569, 34.00203666215729, 2.5591748710223277), (2.8156307, 3.345958, 2.3706088), "SM_Cliff_214", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (10655.158, 13809.055, 1046.3135), (2.5092781570471177, 19.02209128753592, 15.298945052345465), (1.0503693, 1.0503693, 1.0503693), "SM_Cliff_215", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (6834.3203, 2308.0474, 132.87634), (1.7954671687973296, 143.85360055524282, 85.81606897519548), (1.0, 1.0, 1.0), "SM_Cliff_219", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (9594.285, 7614.6685, 287.1299), (-17.363524112961557, -107.19096846010358, 24.276103247347645), (1.0, 1.0, 1.0), "SM_Cliff_226", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (10901.591, 8705.792, 610.46814), (-0.7489926621326365, -11.061554437907114, -86.53068028163926), (0.473833, 0.473833, 0.473833), "SM_Cliff_228", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (8770.763, 12401.97, 653.4104), (0.8723381016874447, 170.61742100054013, 147.57972349882291), (1.0, 1.0, 1.0), "SM_Cliff_230", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (11145.97, 14041.779, 2402.3818), (-8.606659167710792, 38.19489272340987, 5.968386170644669), (2.460872, 2.5158987, 2.030676), "SM_Cliff_258", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (6236.6445, 11828.158, 1708.7495), (-3.1903380702076563, 118.04261091038234, -177.98650034649984), (2.243385, 2.332398, 1.5979201), "SM_Cliff_279", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (10458.688, 7513.305, 555.7132), (4.532554867759587, 1.2188573831804619, -80.35383440774285), (0.6782724, 0.6782724, 0.4954035), "SM_Cliff_284", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (12007.892, 4316.3467, 1763.818), (-9.635344842850138, -60.87811881686204, 5.287341762835557), (3.5862281, 3.2448037, 2.8047013), "SM_Cliff_289", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3556.1265, 12033.535, 1129.719), (6.630993279362435e-06, -39.99948169956435, 10.000206535404622), (2.0995939, 2.0995939, 2.0995939), "SM_Cliff_321", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3477.5752, 9566.705, 197.93457), (-66.49841730564573, -84.99893444721828, -89.99972626062598), (2.3253493, 1.6213443, 1.6213443), "SM_Cliff_325", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (11632.693, 18696.984, 2395.5208), (7.103514547198541e-06, -80.56364418648093, 9.619270847943243), (2.2403307, 2.2403307, 1.9284341), "SM_Cliff_330", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3653.9897, 1518.6592, 452.33777), (-0.867188360663639, -160.03715702055842, -85.07532859137783), (1.6254791, 1.6254791, 1.6254791), "SM_Cliff_338", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (8857.059, 15473.179, 1497.3851), (-0.7711793268149053, -37.78582285238753, 23.937686452951457), (2.037772, 2.4085495, 1.5285673), "SM_Cliff_341", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4222.221, 3450.2397, 440.15152), (28.60230317987389, 74.24935160174174, 77.81180711586829), (2.3491373, 3.6284118, 1.2120901), "SM_Cliff_349", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3651.4856, 12277.912, 1755.3358), (9.066156409446353e-09, -20.000063038622503, 5.000038924810105), (1.3972139, 1.3972139, 1.3972139), "SM_Cliff_350", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3385.604, 12594.843, 1744.2722), (-8.050535204544264, 19.015156772440662, -172.23244179199793), (0.79131466, 1.64492, 1.1473608), "SM_Cliff_354", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2127.0059, 8056.9883, 224.0965), (84.99956560732817, 1.3660339289418561e-05, 1.3660339289418561e-05), (1.6153045, 1.6153045, 1.6153045), "SM_Cliff_363", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (11836.974, 7654.763, 1503.7583), (-2.6155092036477496, -1.3748474303525062, 7.033752761328262), (1.0, 1.6622043, 1.46187), "SM_Cliff_369", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3604.2107, 3435.4, 504.44934), (-10.994781778545876, 7.875453032749457, -25.750671038645446), (2.0964072, 3.2721784, 2.0055687), "SM_Cliff_370", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (8984.613, 11734.309, 501.67334), (85.46949188318249, -135.11840525908693, 3.407299694617941e-05), (1.0, 1.0, 0.56375957), "SM_Cliff_374", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3987.4067, 2938.1865, 1251.7408), (-15.202056763732458, -2.6694335848151223, -13.965544557633992), (2.065617, 3.2238445, 2.065617), "SM_Cliff_383", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (9886.775, 7089.7666, 613.1596), (-12.800506940288397, -24.27014270134208, -95.30757313304326), (0.4114215, 0.4114215, 0.4114215), "SM_Cliff_392", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (9792.981, 7229.1343, 649.5717), (-2.7539033077026227, 45.97755078885956, 86.52875203070481), (0.40420565, 0.40420565, 0.40420565), "SM_Cliff_409", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (8969.824, 4803.0776, 282.8833), (6.351993137081663, -60.914484450055824, -95.4181769026745), (1.5483599, 1.638158, 1.5483599), "SM_Cliff_410", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (9915.825, 6983.208, 568.1356), (3.9181516032392745, -25.324404383726318, -86.52149123546286), (0.6499511, 0.50968385, 0.3599031), "SM_Cliff_446", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (9365.636, 8125.3467, 258.48376), (-54.58403723115831, -64.44823400721965, 18.41009053889777), (0.7893887, 0.7893887, 0.7893887), "SM_Cliff_480", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (9799.674, 7079.2393, 490.87622), (0.0, 92.09819543120342, -0.0), (1.0, 1.0, 1.0), "SM_Cliff_488", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (9582.592, 5668.9062, 548.2932), (5.748812599035698, -72.29043809244159, 36.071372954079735), (1.0, 1.0, 1.0), "SM_Cliff_492", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (11904.248, 6159.48, 663.2304), (0.5407251592492804, 8.106895825884369, -83.80703276251886), (2.9584835, 1.459914, 1.6062449), "SM_Cliff_494", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (10014.093, 6250.3657, 474.3491), (17.276725566964227, -128.27279311888603, 21.486561824615894), (1.2327368, 0.7510199, 0.7510199), "SM_Cliff_496", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (10195.094, 6235.9136, 425.6071), (-2.3138125044788964, -80.41981608387447, -161.29747326828402), (1.0, 1.0, 1.0), "SM_Cliff_499", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (9269.824, 3203.0776, 432.8833), (0.0, 0.0, -85.00002983040224), (1.853743, 1.9435409, 1.853743), "SM_Cliff_506", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (10264.651, 6702.9136, 561.94147), (-83.8696445678406, 33.08145356662152, 7.038204389059538), (0.47906303, 0.47906303, 0.37679842), "SM_Cliff_520", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5574.2275, 7410.1616, -0.8867729), (0.0004115103531295681, -179.999945358476, -179.99998633961727), (1.0, 1.0, 1.0), "SM_Cliff_526", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (9882.887, 5370.827, 315.61847), (-16.154872907752807, 137.20513753493955, 174.94032598570942), (1.880515, 2.0218644, 1.880515), "SM_Cliff_553", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3915.2122, 18858.465, 1108.5587), (-29.491817391112523, -3.4378959962166697, 7.33029755758826), (2.5132709, 2.8274522, 2.163343), "SM_Cliff_564", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (9995.315, 6336.5337, 532.51215), (74.34733821718552, -179.99976575734644, -35.977220419715636), (0.60165197, 0.60165197, 0.4074257), "SM_Cliff_575", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5190.7896, 14335.671, 1147.541), (0.043364624352590225, -7.3542781570686815, -14.021516729454016), (2.005202, 2.7225032, 2.005202), "SM_Cliff_577", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (10918.61, 9198.255, 454.9527), (87.60905966666338, 90.00005193422363, 137.62161807610056), (0.84452784, 1.0, 0.4718905), "SM_Cliff_591", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (6417.1147, 11046.934, 752.9165), (0.0, 49.999751905649106, -0.0), (1.0, 1.0, 1.0), "SM_Cliff_592", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (7904.053, 6156.627, 414.1172), (-5.566466799526689, -6.342436876621648, 6.760602520851703), (1.1029261, 0.8926481, 1.0029491), "SM_Cliff_601", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (9833.443, 8870.664, 321.6173), (14.460987936581008, -164.37292254611953, -7.162962776154096), (1.653337, 1.9326534, 1.3873875), "SM_Cliff_605", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (9147.865, 6152.283, 386.9969), (-6.989199698499817, 106.8237192019186, -71.52605685876074), (0.5852669, 0.49404064, 0.49404064), "SM_Cliff_610", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (9283.378, 5701.416, 364.54962), (86.46999002392609, -179.9973836132539, -62.89715257156998), (0.5400021, 0.76573247, 0.5400021), "SM_Cliff_624", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (9239.096, 10076.307, 238.80333), (4.980970502273475, -29.62149404614247, 3.6825242413871937), (1.0, 1.376544, 1.0), "SM_Cliff_625", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (8772.199, 5221.262, 255.66475), (79.8463600390942, -105.80876915008785, 40.781672089215256), (0.35822856, 0.5063268, 0.5134663), "SM_Cliff_627", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (8596.197, 5797.9795, 257.30887), (7.8803304018566935, 18.88942253716319, 15.10062689028697), (1.0, 1.0, 1.0), "SM_Cliff_637", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (10897.051, 11167.447, 643.5446), (0.0, 19.999918333244267, -0.0), (0.5596936, 0.5596936, 0.5596936), "SM_Cliff_640", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3838.1194, 5488.16, 627.65015), (0.0, 0.0, 146.3577809909614), (1.7169422, 1.7169422, 1.7169422), "SM_Cliff_663", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (7287.872, 10792.317, 139.16881), (-0.9277035717650576, -172.65041281163357, -89.65195634716562), (0.7072287, 0.534536, 0.4198772), "SM_Cliff_685", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (9117.497, 9249.267, 11.23584), (0.0, -179.99967898105174, 0.0), (1.0, 1.0, 0.72248214), "SM_Cliff_702", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (11742.05, 7656.4487, 780.6526), (-0.10742114376417342, -99.05459457115295, -165.33396288345077), (1.79215, 2.072171, 1.79215), "SM_Cliff_703", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5104.7407, 1549.957, 1896.2571), (22.535604841402964, -83.77102929038182, 1.7070447675755227), (1.7932769, 2.7627704, 1.7932769), "SM_Cliff_732", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (6122.6875, 10794.173, 588.55566), (-1.9303592300916268, 58.41619158874344, 2.835024314702179), (1.3361375, 1.3361375, 1.3361375), "SM_Cliff_735", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5482.876, 9222.083, -16.276047), (-26.469726048856305, 58.83127471798574, -88.59910721560318), (1.6630111, 1.9250605, 1.0438303), "SM_Cliff_744", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5694.949, 10670.014, 680.5408), (-10.307738814821073, 81.54151921179607, -9.078461246805347), (1.2035309, 1.2035309, 1.2035309), "SM_Cliff_745", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5804.24, 9696.603, 445.9554), (-1.0218152917503104e-08, -141.70554850648458, 17.8310616601942), (1.0, 1.0, 1.0), "SM_Cliff_765", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (7322.8687, 10469.367, 199.435), (-9.88253746154314, 173.4216194547502, 18.874068933974737), (0.5570311, 0.5570311, 0.58304965), "SM_Cliff_787", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5518.3794, 9491.756, 530.9389), (-11.051451977766613, -1.6581419902873757, 173.9849027359711), (0.88546914, 0.88546914, 0.88546914), "SM_Cliff_790", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (6306.9355, 5109.1865, 188.22209), (-0.5818478811508948, 4.378041674319682, 97.55622707321912), (1.0, 1.0, 1.0), "SM_Cliff_816", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (6801.5127, 10394.0625, 135.7703), (-3.1861855243684887, -140.01914521569395, 88.65871887200854), (1.2097975, 1.2097975, 1.2097975), "SM_Cliff_817", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (9790.606, 11195.188, 652.9176), (0.0, -33.97104140415871, 0.0), (0.4876273, 0.4876273, 0.4876273), "SM_Cliff_822", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (9373.714, 11287.645, 653.53125), (-19.669128611565984, -0.07159422221992326, -1.3610535890288495), (0.67226213, 0.67226213, 0.67226213), "SM_Cliff_835", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (9847.143, 10188.626, 649.15375), (7.813936316258804, -135.63396964986384, 2.0434067611274283), (1.0, 1.0, 1.0), "SM_Cliff_862", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (10213.189, 10239.33, 634.6824), (-15.001004125209604, 166.05635055651572, 5.095157546203712), (0.68930155, 0.68930155, 0.68930155), "SM_Cliff_867", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (11456.895, 10622.819, 432.64725), (-5.104797600470678, 5.532868060136368, 1.484796845878244), (1.0, 1.0, 1.0), "SM_Cliff_1003", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (8082.431, 6688.372, 733.9845), (0.6317100071164424, -160.07677766588338, 9.97726527304796), (1.5415238, 2.959861, 1.801633), "SM_Cliff_1016", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (7627.0938, 7194.9746, 211.15729), (-1.3247376003742657, -20.04144486435925, 177.99286000655718), (1.283511, 2.0011985, 1.283511), "SM_Cliff_1018", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2708.8108, 10387.743, 1235.3295), (-9.478699241747131, 138.30973700554173, 22.03477218376512), (1.3194054, 1.3194054, 1.3194054), "SM_Cliff_1026", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5757.654, 9046.442, 210.97787), (-1.3050226865717072, 39.282854040836774, -171.0352150851143), (1.0, 1.0, 1.0), "SM_Cliff_1034", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (8662.011, 8961.249, 117.892334), (0.012180622950806474, 9.671476665082048, 171.44428235118053), (0.59233004, 0.59233004, 0.59233004), "SM_Cliff_1035", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5205.6567, 7499.8, 413.35425), (0.0, 0.0, -0.0), (0.54171425, 0.54171425, 0.54171425), "SM_Cliff_1040", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5437.5205, 9654.894, 581.7734), (-3.4667058875119756, -157.89575344264094, 15.883422574616809), (1.0, 1.0, 1.0), "SM_Cliff_1041", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5600.346, 775.2967, 752.1725), (-12.046446506000656, 88.9473449899305, 0.21971720951277784), (3.2048724, 3.2048724, 3.2048724), "SM_Cliff_1043", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5351.473, 19075.367, 634.6326), (-11.09805322919822, -2.8156809559721106e-08, 2.123009785319668), (1.6175241, 1.0786304, 1.3458568), "SM_Cliff_1057", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3038.518, 8266.55, 198.50049), (86.56729616198464, -28.347161447525377, 156.04571100120728), (1.5182275, 1.5182275, 1.5182275), "SM_Cliff_1061", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (7603.35, 8729.58, -163.92578), (0.0, -77.7457281793838, 0.0), (1.0, 1.0, 1.0), "SM_Cliff_1063", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (11656.745, 10752.1455, 968.40405), (0.0, 43.920209022314154, -0.0), (1.0, 1.0, 1.0), "SM_Cliff_1080", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5177.436, 9361.069, 456.9547), (0.8349087589252178, -20.150945363085714, 2.274007573653681), (1.4182992, 1.169841, 1.169841), "SM_Cliff_1086", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (10182.318, 12500.599, 559.4465), (0.0, 0.0, -0.0), (1.0, 1.2892349, 0.52148175), "SM_Cliff_1093", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5421.9463, 9115.347, 21.588501), (8.176816555168278, -98.14270073081917, -4.288757556871286), (1.1748321, 1.1748321, 1.2908479), "SM_Cliff_1094", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (10349.0, 12697.192, 658.6813), (6.317465478303368e-06, -31.5094599185719, 47.8382422420823), (1.1430472, 1.1430472, 1.1430472), "SM_Cliff_1100", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (11296.543, 12288.351, 857.85876), (0.0, -8.142516198397091, 0.0), (1.0, 1.0, 1.0), "SM_Cliff_1119", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3920.3955, 12076.772, 1195.791), (8.448368725330191, 169.11874508216823, -4.79089267138951), (2.557123, 2.557123, 2.557123), "SM_Cliff_1124", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4414.9805, 2758.6467, 1486.3403), (28.60230317987389, 74.24935160174174, 77.81180711586829), (2.349137, 3.628412, 1.21209), "SM_Cliff_1126", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3766.6738, 9353.299, -217.62817), (0.0, 69.76799162993267, -0.0), (1.4966887, 1.4966887, 1.4966887), "SM_Cliff_1130", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3555.151, 3909.7231, 709.2744), (-19.279206431539677, 1.9059002389087417e-06, -13.07171821716053), (2.089896, 2.089896, 2.089896), "SM_Cliff_1140", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5770.351, 7196.2554, 81.239105), (1.1535439639995362e-05, 31.144146847155582, 92.20758316619538), (1.1441278, 1.0, 1.2339456), "SM_Cliff_1158", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (6328.978, 5508.219, 301.4737), (0.0, -162.29729174970376, 0.0), (1.2007605, 1.1824634, 1.0), "SM_Cliff_1167", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5798.5635, 13536.102, 726.33954), (-0.41244505097052087, -8.515043235354753, -2.752685343275166), (2.2804701, 2.6616592, 1.5097203), "SM_Cliff_1169", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (9597.723, 5477.0205, 477.8553), (7.582760308498744, 146.65209488223493, -12.224000663105821), (1.330268, 1.767105, 0.88098294), "SM_Cliff_1180", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4399.1343, 14703.181, 1295.6783), (0.043365010561890835, -7.354278536859304, -25.748751221048934), (2.005202, 2.722503, 2.005202), "SM_Cliff_1183", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (8296.288, 13057.466, 141.43018), (-22.264895937893453, 6.3305760496766545, 23.83339110358249), (2.717166, 3.663052, 2.946307), "SM_Cliff_1186", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (6368.374, 5461.6226, 306.62067), (0.0, 122.64516997357897, -0.0), (0.6684614, 0.6684614, 0.6684614), "SM_Cliff_1192", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (8195.612, 12797.719, 162.76938), (18.060554711206912, 104.87682628621924, 86.42667392015363), (1.4248968, 1.4248968, 0.2865799), "SM_Cliff_1196", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3518.6738, 3858.8467, 1251.7395), (-19.279206431539677, 1.9059002389087417e-06, -13.07171821716053), (1.363241, 1.363241, 1.363241), "SM_Cliff_1204", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (8674.217, 12705.675, 362.7382), (28.87433166046121, -154.40109871495542, 159.87555047541218), (1.442395, 1.442395, 1.083736), "SM_Cliff_1206", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3673.243, 17308.592, 2180.5132), (13.33489683062449, -62.5649351354402, -166.1606359099126), (2.4356234, 2.4356234, 1.9795982), "SM_Cliff_1214", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (6496.6953, 5703.772, -1.5479376), (7.988580984756364e-08, 138.42079268315047, 16.70296120572668), (1.0, 1.0, 1.0), "SM_Cliff_1219", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (12023.958, 13575.35, 1808.8834), (-16.40954596896451, 72.14593445081407, 3.25843873876819e-05), (2.460872, 2.515899, 2.030676), "SM_Cliff_1223", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (6111.4814, 5519.23, 356.48715), (5.372257162056729, -78.75121003933312, -164.45808634875672), (0.6715124, 0.6715124, 0.6715124), "SM_Cliff_1238", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (6098.5596, 5686.8354, 151.00418), (-19.047425648102177, -55.974766902298896, -178.62445592706194), (1.0, 1.0, 1.0), "SM_Cliff_1245", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (6278.771, 5819.6855, -22.53021), (-3.4364175088242805e-09, -177.99178024652824, 12.62415867678186), (1.0, 1.0, 1.0), "SM_Cliff_1248", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (12091.873, 13151.796, 1071.3058), (-14.403137646161301, 23.821692650888853, -177.7537069113613), (2.815631, 3.345958, 2.370609), "SM_Cliff_1263", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2696.5525, 11195.114, -15.195412), (-9.846526311221227, -41.75329484312994, -9.848815261413767), (2.099594, 2.099594, 2.099594), "SM_Cliff_1289", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3377.6648, 13770.98, 1269.0714), (8.33705885024958, -96.20893461063736, 11.574475441517245), (2.099594, 2.099594, 2.099594), "SM_Cliff_1303", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3668.025, 17098.268, 909.46356), (-1.2233583111097521, -35.826287644161596, 39.39638077483285), (2.1086595, 3.4819887, 1.7431533), "SM_Cliff_1346", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5447.388, 5945.719, 376.86176), (15.307938350896716, 13.280030520775702, 3.1685947424640872), (0.56147146, 0.56147146, 0.56147146), "SM_Cliff_1371", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (10125.0, 8705.0, 543.8392), (3.53327711772433, 134.89069334006825, -178.54006228270444), (1.0, 1.0, 0.7328829), "SM_Cliff_1382", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (6318.98, 9483.481, 31.1353), (-7.066406911881687, -129.44069501695412, 174.45129566426382), (0.761797, 0.761797, 0.761797), "SM_Cliff_1388", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2334.8594, 9890.88, 1295.5555), (-9.872162658607401, 137.32673324111846, 15.231864940163629), (2.052495, 1.720738, 1.720738), "SM_Cliff_1419", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5720.5522, 8963.09, -47.290676), (-10.870850623271272, 37.752911343722744, -170.87195243141775), (1.0, 1.0, 1.0), "SM_Cliff_1426", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (12286.453, 12179.671, 1171.9196), (-16.40954596896451, 72.14593445081407, 3.25843873876819e-05), (2.460872, 2.515899, 2.030676), "SM_Cliff_1436", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (12211.89, 11624.196, 1168.5553), (-14.403137646161301, 23.821692650888853, -177.7537069113613), (1.9924757, 2.522803, 1.5474544), "SM_Cliff_1437", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (11818.507, 11917.279, 813.2827), (-23.536837164222145, 29.368303278958944, 16.3450734309062), (2.815631, 3.345958, 2.370609), "SM_Cliff_1439", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (9526.902, 10277.851, 503.5066), (5.416174952729356, 4.545317640538925, 179.99663952157428), (1.0, 1.0, 0.6676134), "SM_Cliff_1445", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5854.261, 6781.376, 274.57422), (-5.4378353614084824, -88.09344280300414, 6.316916538698517e-07), (0.5841909, 0.5841909, 0.5841909), "SM_Cliff_1446", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (9405.449, 11599.974, 594.13226), (2.070239189204655e-05, 127.16290131750986, 91.20522262124028), (0.9313698, 0.65987486, 0.55654025), "SM_Cliff_1462", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (11032.821, 14226.357, 2167.1592), (-10.42669611129141, -6.001648405529599, 11.343927597838194), (2.943864, 2.7696025, 2.13919), "SM_Cliff_1465", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (10496.157, 15037.625, 2461.97), (22.940562736855433, -132.14457781315133, -3.4572154844485956), (2.717166, 4.113816, 2.2754655), "SM_Cliff_1469", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (11025.021, 8589.505, 572.7531), (0.0, 0.0, 90.00007597449323), (1.0, 1.0, 0.9294917), "SM_Cliff_1470", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (7263.635, 10449.167, 134.21017), (-1.9793696017930442, -13.112548491417689, 83.16760707023575), (0.534536, 0.534536, 0.534536), "SM_Cliff_1476", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (9315.344, 5329.935, 402.42853), (3.6115032312819464, -115.9452185777466, -166.53825339098915), (1.6582905, 1.6582905, 1.6582905), "SM_Cliff_1481", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (8654.685, 6153.763, 280.15994), (-3.105071204009642, 98.86728709479273, 14.866955061539372), (1.4398271, 1.354936, 1.354936), "SM_Cliff_1488", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (9344.2705, 4833.986, 558.6768), (3.367070785507932, 29.195431205751852, 11.59953092279643), (2.0266895, 2.0266895, 2.0266895), "SM_Cliff_1492", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (9177.608, 6297.966, 229.08488), (5.078443917158504, 90.86750239663844, 24.369919957660272), (1.0, 1.0, 1.0), "SM_Cliff_1494", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (9462.304, 5038.4956, 632.95703), (19.2094413222554, 38.71019991391445, 12.944277012928588), (1.9307377, 2.4758613, 1.4111271), "SM_Cliff_1499", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5496.368, 1705.9742, 1659.2744), (-1.9659731565745104, -6.4447022220333325, 5.979043074587808), (2.089896, 2.089896, 2.089896), "SM_Cliff_1501", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (9474.496, 5558.113, 497.4935), (7.582667565387522, 146.652360945281, -178.51222659384408), (1.330268, 1.7671049, 1.330268), "SM_Cliff_1503", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (9499.819, 6842.325, 669.8457), (-16.407440120387314, -153.1619005673934, 7.405744196570681), (1.0, 1.3225428, 1.136796), "SM_Cliff_1516", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (8646.895, 6448.2637, 1164.1849), (19.561037680916204, 3.770709756962824e-08, -4.04913294160559), (1.3736699, 1.3736699, 1.3736699), "SM_Cliff_1523", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (10366.838, 6032.3657, 525.4289), (-2.44894403427346, -144.75296139250503, -177.5613975281403), (1.0, 1.0, 1.0), "SM_Cliff_1524", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4949.7974, 9530.341, 615.5963), (-15.326600884313658, -53.64358941450993, 15.637683438829416), (1.0, 1.0, 1.0), "SM_Cliff_1536", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3537.6147, 10498.477, 417.71835), (3.9551773985440567e-07, 140.00001045176242, 15.000416230833562), (2.052495, 1.7207384, 1.7207384), "SM_Cliff_1552", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5136.554, 19009.227, 1592.112), (-14.936462735567092, 0.0, -0.0), (2.0321858, 1.8282646, 2.0321858), "SM_Cliff_1558", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5541.711, 9158.668, 761.9957), (-1.746368382025825, 46.11565628866391, 1.678844427729804), (1.3317127, 1.3198609, 1.083255), "SM_Cliff_1571", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (11572.997, 6644.757, 886.087), (-10.656890819532338, -40.09225125446173, 8.36357919397393), (1.4126245, 1.4126245, 1.4126245), "SM_Cliff_1575", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4415.6357, 2744.12, 859.89966), (1.1359987871408046e-07, -7.7372746719178025, -26.306152801997335), (2.6773086, 2.6773086, 2.6773086), "SM_Cliff_1577", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (6271.886, 4396.374, 565.16406), (-2.169464041278025, -4.388702189097339, -8.944761645943215), (2.069316, 2.069316, 2.069316), "SM_Cliff_1581", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (7547.9355, 8446.631, -163.9242), (0.0, 36.984693830194594, -0.0), (1.0, 1.0, 1.0), "SM_Cliff_1591", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5045.1646, 6285.7676, 323.48825), (-7.499847867921711, 29.632940520249026, -85.15286147819165), (0.626574, 0.291694, 0.6844), "SM_Cliff_1599", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5732.842, 14256.297, 444.03943), (3.1352809772530306e-06, 51.06380699012066, 91.67724550566484), (1.75059, 1.0, 1.0), "SM_Cliff_1622", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5542.2773, 17821.549, 474.24628), (0.0, -31.932251837195984, 0.0), (1.0, 1.0, 0.3793004), "SM_Cliff_1629", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (7724.96, 8518.129, 271.44043), (0.0, 139.99985897116102, -0.0), (0.40309933, 0.40309933, 0.40309933), "SM_Cliff_1633", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (9777.109, 8740.139, 442.32178), (-17.307891184192105, 0.6816030922331069, 18.4019993514115), (1.2721654, 1.2721654, 1.2721654), "SM_Cliff_1680", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (7944.8247, 17700.42, 632.9176), (-26.81661979596821, 20.317911461246457, 3.355364531271729), (1.4200648, 2.0133908, 1.4200648), "SM_Cliff_1712", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (7528.0537, 17789.965, 752.8562), (-23.02270816024731, 28.76898253443363, -6.579987691732162), (2.1357033, 2.1357033, 1.5360403), "SM_Cliff_1719", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5105.173, 3388.9739, 704.19104), (-16.50024686342839, 2.552475340606012, -11.90060355277316), (2.9492152, 2.9492152, 2.307245), "SM_Cliff_1751", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5305.151, 3159.7231, 1659.2744), (-19.279206431539677, 1.9059002389087417e-06, -13.07171821716053), (2.0898957, 2.0898957, 2.0898957), "SM_Cliff_1776", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (8597.095, 11347.723, 318.1421), (-14.999969756065502, 0.0, -0.0), (1.1887892, 1.6385142, 0.9968231), "SM_Cliff_1851", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3400.0, 7386.6025, 400.0), (-12.758545380289943, 39.33035172271874, 26.776097675228623), (1.7875694, 1.7875694, 1.6181575), "SM_Cliff_2093", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2200.0, 8100.0, 400.0), (0.0, 0.0, 15.000045845452274), (1.803395, 2.3732789, 1.6269239), "SM_Cliff_2119", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5169.5938, 15035.824, 1121.3169), (1.3487849358182034, -27.37881675804498, -12.845826792306465), (1.4189022, 2.096081, 1.6656882), "SM_Cliff_2134", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4561.5728, 16801.48, 789.2952), (5.405767460130692, -40.42779788984006, 27.130517669392376), (1.9222981, 1.9222981, 1.6846838), "SM_Cliff_2155", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4778.172, 16479.875, 494.26117), (-9.527831866123247, -22.512512320571638, -145.59477471841896), (1.6519899, 1.6519899, 1.195965), "SM_Cliff_2161", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5278.239, 17393.52, 688.3346), (-7.695799268749736, -4.850952103373514, 32.364215850304795), (1.9404362, 1.9404362, 1.4657719), "SM_Cliff_2170", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (7230.302, 4030.5535, 325.16266), (79.18005812342322, 0.0, -0.0), (2.0249512, 2.0249512, 0.886634), "SM_Cliff_2206", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (11271.803, 8861.434, 378.88507), (-5.078613295400726, -9.370178892894968, 165.86727003370135), (1.0, 1.0, 1.0), "SM_Rock_Large_1401", _folder)
if a: placed += 1
else: skipped += 1

# Batch 163: StaticMesh'SM_Cliff_02' (2 instances)
_mesh_path = "/Game/Unshippable/ThirdParty/Lordenfel/Environment/Rocks/SM_Cliff_02"
_materials = ['/Game/Unshippable/ThirdParty/Lordenfel/Environment/Materials/MI_Cliff_02']
_folder = "Reconstruction/BD_BB_Outdoor_TradingPost/Meshes"
a = spawn_static_mesh(_mesh_path, _materials, (3818.2686, 4718.884, 332.10535), (14.766889364924179, -5.345398472151351, 87.33606217254535), (0.67074263, 0.67074263, 0.67074263), "SM_Cliff_853", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5758.9077, 18216.602, 455.70587), (73.70609943370192, -179.9999847412094, -179.9999847412094), (1.0, 1.0, 0.60804015), "SM_Cliff_1609", _folder)
if a: placed += 1
else: skipped += 1

# Batch 164: StaticMesh'SM_Cliff_02' (280 instances)
_mesh_path = "/Game/Unshippable/ThirdParty/Lordenfel/Environment/Rocks/SM_Cliff_02"
_materials = ['/Game/Unshippable/ThirdParty/Lordenfel/Environment/Materials/MI_Lordenfel_RedRock_Cliff_02']
_folder = "Reconstruction/BD_BB_Outdoor_TradingPost/Meshes"
a = spawn_static_mesh(_mesh_path, _materials, (8784.998, 11742.748, 711.65), (-0.38443048134187935, 31.711492271026827, 20.763455991334112), (1.0, 1.0, 1.0), "SM_Cliff_6", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (8546.872, 10659.669, 233.24599), (13.428314614931255, 176.8025653449859, 166.47415638440665), (1.0, 1.0, 1.0), "SM_Cliff_12", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (9209.466, 3607.5913, 421.98047), (12.165194950220053, -2.8228761127672826, -86.31418219571445), (1.918888, 1.663259, 2.445658), "SM_Cliff_22", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (11873.889, 8156.492, 469.92767), (4.394092754989992, 56.55702608628987, -3.230774071962965), (2.131054, 2.131054, 1.7657337), "SM_Cliff_25", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3931.1594, 4523.963, 370.413), (0.43525380296219696, -4.981078365326221, -50.01888593312313), (1.0130882, 1.480727, 1.1839995), "SM_Cliff_35", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (8736.615, 15657.673, 1120.5012), (-25.072877302687573, 47.98724023306197, -12.41677799777058), (2.368199, 2.368199, 2.368199), "SM_Cliff_66", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (10851.986, 9007.461, 574.5714), (-86.20712791452792, 24.271422141323498, 89.73434865335282), (0.46138754, 0.46138754, 0.28603917), "SM_Cliff_68", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (9475.663, 10181.073, 160.36151), (41.55334534419057, -97.05327285517903, -71.32985385063624), (1.9934905, 1.5040253, 1.0), "SM_Cliff_71", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (11024.86, 13888.375, 957.7097), (-10.476928814720743, 62.52264174859048, -4.621247385421279), (1.8279433, 1.8279433, 1.8279433), "SM_Cliff_73", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (9139.088, 16058.119, 2047.2737), (-18.188658336525677, 0.0, -0.0), (2.095458, 2.095458, 2.095458), "SM_Cliff_80", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (8961.004, 10215.203, 235.3009), (-69.23006958277959, 158.1282552943431, -15.728907187616272), (1.5478477, 1.3399609, 1.2423304), "SM_Cliff_83", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (11857.6875, 11100.196, 650.0), (1.1522777163019504e-08, 2.937602047762877, -5.452057181687772), (2.131054, 2.131054, 2.131054), "SM_Cliff_93", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (8788.886, 10626.812, 434.5458), (-32.13997894284612, 20.96551363175637, -6.790984108198094), (1.1214007, 0.9674447, 0.9504367), "SM_Cliff_99", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (10852.438, 13989.953, 1151.13), (0.8433850897463653, 77.76049878111232, -10.25045807132749), (1.017311, 1.017311, 1.017311), "SM_Cliff_100", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (10049.5625, 15631.662, 3162.3628), (1.158809889114827e-06, 102.28504659688575, -19.96246074990896), (2.022005, 2.022005, 2.022005), "SM_Cliff_110", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (11667.819, 4023.5752, 1645.9385), (11.01505160150112, 84.05934637837906, -23.804288778812396), (2.3527038, 2.3527038, 2.3527038), "SM_Cliff_112", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (11527.649, 11892.008, 580.42096), (-5.620758965964642, 64.29322560754152, -11.499941324615968), (1.8287618, 1.979058, 1.979058), "SM_Cliff_113", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (12261.551, 13823.19, 1347.8073), (-17.79184053361504, 127.09214297312954, -7.684083533400445), (2.4458826, 2.4458826, 1.9527913), "SM_Cliff_121", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5117.784, 9550.288, 403.82806), (-84.99959282161586, -22.136724510090076, 1.3804572127868282e-05), (1.4122449, 1.4122449, 1.4122449), "SM_Cliff_127", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4259.093, 9482.886, 412.58987), (-79.97257626052352, 173.53885558151856, 0.06977919018220394), (1.5252016, 0.93662333, 1.5252016), "SM_Cliff_133", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2777.227, 9732.61, 405.4315), (-84.96323588213603, -170.07881828907648, -4.960116629370495), (1.525202, 1.525202, 1.525202), "SM_Cliff_139", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (9656.731, 7842.034, 419.72), (-19.683289845766446, -4.373138514577366, -3.6164247757262125), (0.70169854, 0.70169854, 0.70169854), "SM_Cliff_141", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (8793.507, 18867.5, 1441.5454), (8.552658120089605, 90.55989652899098, -24.714810878769022), (1.9793597, 1.9793597, 1.9793597), "SM_Cliff_153", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (9462.667, 8018.9854, 274.82468), (-19.825136064496586, 1.3740301654681286, -15.411925274731797), (0.66732365, 0.66732365, 0.66732365), "SM_Cliff_156", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (11432.767, 13869.265, 1535.4459), (-14.912351195537548, 99.3741176365633, -9.505919914138902), (2.491771, 3.5063655, 2.285646), "SM_Cliff_160", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (11387.095, 13864.891, 1819.1636), (-17.3198562582245, 106.74311782497584, -8.042848012279153), (2.7215064, 2.588834, 2.006758), "SM_Cliff_165", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (9528.384, 7163.6816, 389.36975), (0.0, -25.00003249417806, 0.0), (1.0, 1.3015379, 1.0), "SM_Cliff_168", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (9772.401, 15161.981, 1881.3188), (-19.552187756238567, 34.450427330074206, 3.0225895756748634e-06), (2.728202, 2.38693, 2.728202), "SM_Cliff_171", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (10857.567, 13056.504, 788.6481), (-17.07745432498717, 99.75370022411761, -9.610687275152063), (1.4991672, 1.5786661, 1.2930423), "SM_Cliff_172", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (7850.0, 13031.282, 594.66736), (-7.263578664128255, 163.2939935336461, -22.844233631215115), (1.0, 1.0, 0.505468), "SM_Cliff_176", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5357.208, 15101.343, 446.33954), (1.0187473353188725, -31.140346837209652, 82.57215106771963), (2.3487914, 1.9841589, 1.0521189), "SM_Cliff_181", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (6357.091, 12044.611, 1232.0781), (11.045884173374821, 178.0434584421197, -6.424987158396452), (3.095622, 3.095622, 2.525433), "SM_Cliff_187", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (8306.629, 18771.38, 1242.1537), (-24.34182912726509, -0.003051798606381404, -2.54403696492726), (2.6694927, 2.1272118, 2.6694927), "SM_Cliff_193", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (9645.842, 7423.6484, 238.12418), (9.04875060053792, -19.120178689104673, -97.4161315554273), (1.1096919, 1.4024729, 1.1390034), "SM_Cliff_194", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (11885.636, 13023.368, 1035.3572), (-10.04452442605374, 116.97017535070657, -15.956696709178729), (2.4901319, 2.4901319, 1.5638704), "SM_Cliff_208", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (11096.597, 13474.156, 1473.3846), (22.845775013613064, -145.5494205519879, 155.36584819255017), (1.7341197, 1.4825537, 1.4825537), "SM_Cliff_211", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (9563.182, 7431.5986, 395.51895), (-12.658812060337038, 0.4521830503472375, -13.391113680390536), (0.79877824, 0.79877824, 0.79877824), "SM_Cliff_222", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (8595.437, 11835.605, 651.0669), (-14.086882657600626, 61.078444325562, -5.211304725623364), (1.0, 1.0, 1.0), "SM_Cliff_223", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (10310.917, 5994.8228, 823.43335), (4.999998922753864, -29.99999957519694, 2.2550645333433548e-06), (1.0, 1.0, 1.0), "SM_Cliff_232", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (10821.732, 8159.9263, 612.34534), (-84.45443056800406, 33.05446063991902, 89.27411572872155), (0.5395829, 0.7619866, 0.5395829), "SM_Cliff_233", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (8791.177, 12174.716, 561.50867), (-18.871491973816166, 86.54076694508531, 4.6021103836782515), (1.0, 1.0, 1.0), "SM_Cliff_254", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (10303.089, 6120.753, 881.85834), (-1.0763550896282483, -52.7985567649948, -13.08969141881623), (0.8804312, 0.8804312, 0.8804312), "SM_Cliff_269", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (8782.031, 12967.399, 756.72284), (-18.747222220382266, 143.99462067459623, -23.85867295389019), (1.341793, 1.341793, 1.341793), "SM_Cliff_273", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5965.2505, 11402.522, 1215.603), (1.0287564883911775, 164.65879320288002, -5.347321282900711), (2.082762, 2.610634, 2.5233214), "SM_Cliff_274", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (6398.268, 5077.689, 29.512875), (-2.482360519113165, -179.15127967663412, -89.06935852852321), (1.6512986, 1.567473, 1.722463), "SM_Cliff_290", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (7720.0, 13300.0, 850.0), (-80.00001853146082, 0.0, -0.0), (1.0, 1.0, 0.505468), "SM_Cliff_291", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5364.784, 11378.229, 1626.5946), (-11.505188559395737, 65.17338956233505, -5.6426087880886815), (1.942703, 1.942703, 1.942703), "SM_Cliff_294", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2635.3347, 10517.724, 536.62756), (-2.681884619159219, 1.38684061234324, -2.2280576018898017), (1.6414758, 1.6414758, 1.4958222), "SM_Cliff_298", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (12299.363, 13905.911, 575.24457), (4.213688938144505e-12, 179.99989754716697, 85.0000144793138), (1.0, 1.0, 1.0), "SM_Cliff_299", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3740.7522, 10262.466, 726.44574), (-17.06142714027246, -96.31889935971378, -31.963344211532473), (1.36053, 1.289913, 1.181234), "SM_Cliff_305", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (9158.549, 3760.13, 205.32501), (12.165194950220053, -2.8228761127672826, -86.31418219571445), (1.918888, 1.663259, 1.3811598), "SM_Cliff_310", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (9439.081, 10181.079, 437.90247), (0.0, 0.0, 15.000058335092751), (1.0, 1.3765436, 1.0), "SM_Cliff_311", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (12021.604, 7337.9263, 1075.8579), (2.820103151653785, 85.58207603618759, -5.726074653517631), (2.509363, 2.2900474, 3.053088), "SM_Cliff_315", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3423.6816, 9900.6455, 278.45325), (80.50297316585238, 89.99942715879753, -89.99991656482807), (1.6432961, 1.3706641, 2.1298842), "SM_Cliff_322", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (10962.855, 18699.172, 1684.565), (7.18864999919699, 88.83173683770752, -10.943633850055166), (2.3124714, 2.3124714, 2.3124714), "SM_Cliff_324", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3784.2324, 998.28906, 370.85538), (0.8671407561593895, 9.962746994619845, 85.07558779161542), (1.4032415, 1.4032415, 1.4032415), "SM_Cliff_343", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (10543.262, 6296.3813, 608.34344), (-10.720673014780278, -85.51492680509789, -9.947722045650844), (1.0, 1.0, 1.0), "SM_Cliff_347", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3289.6846, 8064.584, 279.63928), (-0.07525635346711812, 0.8672416142457179, -170.03839308283912), (1.5704153, 1.4778845, 1.4047348), "SM_Cliff_360", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (11909.241, 12487.003, 764.08984), (-2.3706971850374323, 14.430860459284592, 9.132125757683813), (2.0130782, 2.0130782, 2.0130782), "SM_Cliff_366", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4560.066, 2881.3125, 384.0631), (-16.920255387476622, -88.79891278740251, -10.485715754596209), (3.1906755, 1.8702064, 1.5029166), "SM_Cliff_367", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (12186.415, 4523.4976, 652.4378), (5.340887262869797, 169.13830723977327, -94.91403913557868), (2.4064918, 1.0, 1.8552004), "SM_Cliff_379", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4351.3047, 1657.5869, 906.4339), (-12.262756212610917, 25.792402709869204, 2.6641150536845677), (4.0302954, 3.0803463, 2.700016), "SM_Cliff_380", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3389.366, 12377.402, 1242.52), (-4.999969498649654, 3.3327726089100677e-06, 10.000130023817297), (1.5856302, 1.5856302, 1.5856302), "SM_Cliff_382", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (9826.619, 6880.062, 611.8962), (-76.56116544983219, -11.453560694363937, -80.50982969108523), (0.54946107, 0.54946107, 0.54946107), "SM_Cliff_388", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4877.254, 15310.445, 759.343), (-9.819761869961702, -97.7974239130639, 3.209506640676878), (2.449796, 2.293257, 1.5391369), "SM_Cliff_391", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (8907.991, 11368.977, 578.54065), (7.904869517067821e-07, -13.431060888033299, 85.808358439275), (0.7168813, 0.5130461, 0.6330516), "SM_Cliff_394", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3580.9185, 15181.939, 578.0469), (-17.791196729702285, -0.16348259994285713, -6.495666346942939), (1.276082, 2.6792498, 1.315941), "SM_Cliff_398", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3138.156, 13483.381, 1434.74), (-8.168914741738943, 10.000353228609256, 3.668422392566706), (1.2316225, 1.2316225, 1.6102141), "SM_Cliff_399", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3929.398, 16067.278, 613.9242), (34.71344843459077, 156.74028690612622, -89.39989807369233), (1.8348597, 1.3748227, 1.8348597), "SM_Cliff_403", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (9889.159, 3421.852, 987.30414), (-18.784089943117444, 1.9699659154106828, -10.92614937867426), (5.2513704, 3.2642055, 2.8551393), "SM_Cliff_406", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (10270.416, 7181.6055, 616.0045), (-81.38297499650537, -138.15959086367158, -33.55387963004302), (0.22999878, 0.63265675, 0.4708657), "SM_Cliff_413", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (12090.212, 6856.986, 948.2744), (-7.622894705554209, 63.91273789574832, 2.6975706444303937), (2.6760533, 3.2875845, 2.788308), "SM_Cliff_421", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4897.7495, 11509.431, 1298.9515), (-15.36407354642773, 45.041512490357576, 173.73773207962998), (2.082762, 2.610634, 2.523321), "SM_Cliff_425", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (8599.26, 6475.5264, 786.10315), (9.670251437807568, -64.34526571432356, -23.219602449101295), (1.4180906, 1.5196626, 1.9214282), "SM_Cliff_428", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (10029.098, 7089.6953, 623.39667), (-85.95221455069816, -130.66453999362966, -17.316513124323098), (0.284383, 0.52994275, 0.38626283), "SM_Cliff_438", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (9890.014, 7197.203, 657.8242), (0.0, -133.94082131324552, 0.0), (0.61875117, 0.61875117, 0.61875117), "SM_Cliff_468", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (9530.993, 5621.1367, 427.44196), (-75.53794033277731, 100.84181443787308, -54.1009331694857), (1.8974768, 1.2627598, 1.4401668), "SM_Cliff_471", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (10509.023, 6006.7754, 557.99854), (-1.3180541934491996, 113.49917786790765, -0.541015708516356), (1.0, 1.0, 1.0), "SM_Cliff_482", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (9768.553, 5773.1655, 534.6126), (-20.52752873787614, 43.613171081400054, -10.34323063639822), (1.0, 1.0, 1.0), "SM_Cliff_485", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (12019.869, 4945.9824, 625.00244), (1.5156059437358724e-07, -6.980071571568953, -90.00001937249527), (2.6169412, 1.0, 1.718021), "SM_Cliff_490", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (9085.666, 3313.3125, 349.32834), (-1.0166623238499464, 2.939488001833426, -85.10404072491019), (2.0767484, 1.6476074, 1.7224635), "SM_Cliff_502", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (9669.928, 7158.3516, 685.25024), (0.0, 0.0, -0.0), (0.58196497, 0.58196497, 0.58196497), "SM_Cliff_504", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (9636.335, 11710.773, 597.26575), (83.74686954307744, 89.46622818404668, 125.37128808526306), (0.47622335, 0.47622335, 0.46900022), "SM_Cliff_510", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5454.756, 7625.7285, 127.01309), (0.0, -109.99994456342102, 0.0), (1.0, 1.0, 1.0), "SM_Cliff_513", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (10472.51, 6453.462, 409.55588), (-0.4351190861249695, -65.74834900684893, 7.707127983868085), (1.0, 1.0, 1.0), "SM_Cliff_516", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (9789.774, 5231.2944, 641.68884), (-2.6122745852018783, -126.38717981121128, -18.755097641005868), (1.2548057, 1.2548057, 1.2548057), "SM_Cliff_546", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5252.1064, 15317.184, 764.00104), (-5.472778605810333, -96.67767933182353, 5.06444367363446), (1.7643247, 1.8668426, 1.6615565), "SM_Cliff_554", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (11069.936, 9084.321, 542.00494), (87.1805759178652, 11.267347852016929, -179.99962659207347), (0.5419744, 0.76216066, 0.5419744), "SM_Cliff_556", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (9802.353, 4237.135, 890.2103), (-25.641236610367447, 0.0, -0.0), (2.299108, 2.299108, 2.299108), "SM_Cliff_560", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4243.997, 18850.43, 989.3127), (19.029827703123686, 148.08664370321912, -14.437043190467897), (2.040311, 2.040311, 2.040311), "SM_Cliff_561", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4248.7446, 14196.779, 1694.4749), (1.6720916659819836, 6.226472601410289, -16.99252353257759), (1.393551, 1.7794887, 1.7794887), "SM_Cliff_567", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (12065.603, 10269.13, 592.1437), (84.56650482965505, -146.51705097137767, -166.40508392715913), (0.620963, 0.620963, 0.620963), "SM_Cliff_569", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4530.153, 11548.811, 1235.8267), (-12.69616824944436, 62.42599493396278, -10.358003323011896), (1.8118637, 2.610634, 2.523321), "SM_Cliff_574", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3196.9153, 14321.932, 1099.294), (24.17510053198737, 178.6943192396591, -2.2869257263352103), (1.764325, 1.866843, 1.661556), "SM_Cliff_586", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (9515.36, 6484.7905, 515.50464), (-62.07149508198903, 7.906221177355578, -163.0687560838442), (0.4567601, 0.4567601, 0.4567601), "SM_Cliff_595", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (9410.296, 6329.9478, 469.26294), (-77.59907019659863, -10.054392453872802, -112.95551870339136), (0.2959127, 0.44407046, 0.44407046), "SM_Cliff_598", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (9402.672, 9060.724, 49.07493), (81.8122893042054, -136.78677385121458, -54.565316334980075), (1.720636, 2.6932776, 0.5981996), "SM_Cliff_609", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (8942.387, 6030.8955, 268.93774), (0.9428799322417765, 144.2139149492832, -101.95784335343406), (0.5407373, 0.5407373, 0.5407373), "SM_Cliff_614", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (8508.826, 5021.9414, 259.2483), (-84.57146506191194, 39.997373138992266, 1.2742727581271516), (0.45424426, 0.45424426, 0.45424426), "SM_Cliff_615", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (9024.672, 6049.06, 328.71625), (-0.7986462341998397, 127.23722880936899, -93.14206412606394), (0.4364678, 0.4364678, 0.4364678), "SM_Cliff_629", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3393.249, 15849.373, 1517.9285), (-8.168884048314018, 10.001065308913772, 32.20035510791549), (1.231622, 1.231622, 1.610214), "SM_Cliff_630", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (10961.268, 11046.544, 673.06464), (0.0, 99.99999964828497, -0.0), (0.49475163, 0.49475163, 0.49475163), "SM_Cliff_634", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3989.2773, 16362.004, 1349.5988), (11.963631504653469, -178.6499952694436, -22.634426793186833), (2.4412181, 2.4412181, 2.0566392), "SM_Cliff_638", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5117.784, 15700.164, 594.46277), (-12.728576219593128, -133.28977333580755, -2.512938901996459), (2.194077, 2.194077, 1.541373), "SM_Cliff_645", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5547.8706, 4562.282, 660.7748), (-7.58712923874549, -1.5891723047802289, -12.41021891808806), (1.5791498, 1.4121885, 1.4121885), "SM_Cliff_654", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4775.8184, 4141.208, 587.99896), (-8.538422380030468, -50.74743556730473, -10.741180745390078), (1.43343, 1.43343, 1.43343), "SM_Cliff_657", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (7110.2915, 10350.178, 118.56937), (2.2047232163349766, 17.84495437477104, 83.18531641497204), (0.5345355, 0.5345355, 0.5345355), "SM_Cliff_670", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (11460.42, 10488.913, 563.188), (-2.881987794965615, 105.91628005608155, -16.26910503261719), (1.0105572, 0.7678333, 0.7678333), "SM_Cliff_673", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3547.3057, 6968.8643, 747.47516), (4.601025308792752e-08, -147.2746678690352, -16.8973671263786), (1.0, 1.0, 1.0), "SM_Cliff_687", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (9991.132, 8490.018, 444.33505), (56.38971525598734, 0.8949975180327667, 81.42096055599139), (1.1295677, 0.9266571, 0.34890333), "SM_Cliff_691", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3079.6323, 6787.8833, 698.35376), (-15.609133599803384, 68.80517568193656, 8.169437270665165e-06), (1.0, 1.0, 1.0), "SM_Cliff_695", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (7069.661, 11051.249, 105.31456), (0.8392542506190913, -164.69518890754105, -92.30546214583131), (0.743853, 0.743853, 0.629194), "SM_Cliff_706", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (7329.165, 4728.274, 382.40765), (-2.513885283345868, -177.1166998163957, -100.5037177011937), (1.0296242, 0.64112043, 0.5828742), "SM_Cliff_715", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (6166.249, 9330.891, 19.663044), (3.8008567094912764, -52.86528798324312, 171.86274408584492), (0.7617975, 0.7617975, 0.7617975), "SM_Cliff_717", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (6002.352, 9810.838, 249.46922), (-10.95040781694397, -84.59350221137441, -1.0300903423445573), (1.0, 1.0, 1.0), "SM_Cliff_731", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (6106.3203, 10487.669, 456.19806), (-66.16988363815017, 178.04159366302258, -0.4500116636495916), (0.83479744, 0.9914052, 0.83479744), "SM_Cliff_741", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (6778.432, 10060.92, 173.04181), (76.50551537909074, -6.216797314199872, 20.897827546208262), (0.5692387, 0.5692387, 0.5692387), "SM_Cliff_742", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2858.968, 8032.0054, 361.60022), (-4.684539352932535, 89.58915336141922, 3.706099765431489), (1.985934, 2.0491753, 1.5204117), "SM_Cliff_751", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5647.923, 9292.524, 538.30646), (1.917732440053385, 115.80587395732638, -4.207885409961212), (1.0, 1.0, 1.0), "SM_Cliff_762", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5634.434, 9634.61, 592.5573), (-16.58084021738153, -19.818146813920116, 4.25592337614911e-06), (0.70866495, 0.70866495, 0.70866495), "SM_Cliff_794", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (6390.1396, 4983.7827, 255.31084), (-0.11599714300024495, -170.68686922397862, -96.17165725952809), (1.0, 1.0, 1.0), "SM_Cliff_811", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (6819.137, 10719.608, 243.29887), (-88.13369626151524, -32.754023260828184, -37.828828417461125), (1.2908721, 1.2908721, 1.2908721), "SM_Cliff_813", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (9441.193, 11304.097, 657.1621), (2.721529149237258, 51.10305507280026, -17.23730392268322), (0.6795926, 0.6795926, 0.6795926), "SM_Cliff_825", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3913.1992, 5282.1187, 372.8247), (-5.375244171316797, -178.2468607502216, 84.55184140490991), (0.5383378, 0.775116, 0.6157587), "SM_Cliff_844", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (9431.829, 11501.59, 656.0244), (-18.591582786270752, -2.1411136229307, -20.64990146070639), (0.56509465, 0.56509465, 0.56509465), "SM_Cliff_851", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (11267.639, 6581.459, 816.02057), (-3.654346566184799e-08, 57.66684036898602, -12.063873777178037), (1.0, 1.0, 1.0), "SM_Cliff_859", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3947.231, 3946.2354, 373.91904), (-5.375244171316797, -178.2468607502216, 84.55184140490991), (0.538338, 0.775116, 0.615759), "SM_Cliff_892", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (9490.792, 11338.028, 691.56323), (8.133131436605654, 76.27593198012306, -19.454833626893212), (1.0, 1.0, 1.0), "SM_Cliff_922", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (9387.148, 11655.372, 369.38397), (-11.127314791412472, -114.14180475934056, -158.0458498690801), (1.0, 1.0, 1.0), "SM_Cliff_985", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (10191.984, 10447.2705, 415.67456), (6.083697175063662, -49.84488067931647, -11.630860053794288), (1.0, 0.836807, 1.0), "SM_Cliff_988", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (11390.665, 10516.499, 602.8773), (-2.9969751644155325e-07, 101.71783209723098, -16.324188610328484), (0.75709647, 0.7258596, 0.4808721), "SM_Cliff_1006", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3876.6191, 7977.2554, 252.46008), (21.63554815964051, -104.43796698131794, -8.485627026054502), (1.5363876, 1.5953854, 1.1919075), "SM_Cliff_1007", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (7938.7114, 6758.3477, -52.099), (-1.9112853624810635, 12.448537089194186, -91.04753958764526), (2.076748, 1.567473, 1.722463), "SM_Cliff_1008", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2551.6096, 9715.526, 1294.6698), (-20.153593396223386, -169.72698605156214, 5.309108423913673e-06), (1.3394523, 1.3394523, 1.3394523), "SM_Cliff_1013", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4463.083, 4165.9307, 703.9285), (-5.576660584342754, -103.70666199030406, 11.757097421486902), (1.7211441, 1.7211441, 1.4322814), "SM_Cliff_1022", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2500.452, 10241.609, 1333.2538), (-18.351136778640043, -109.12908819922932, -16.080566968220527), (1.7749567, 1.7749567, 1.7749567), "SM_Cliff_1023", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5785.368, 4274.1406, 1359.1986), (18.66390912180262, 144.92747837614914, 7.444843634124079), (1.169563, 1.169563, 1.169563), "SM_Cliff_1027", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5682.212, 9144.728, 355.3819), (-11.630280711721936, 105.1008211389102, -9.41217240639546), (1.0, 1.0, 1.0), "SM_Cliff_1030", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5302.2964, 7552.176, 349.9989), (4.106365487753855, 139.13904741005976, -4.16882317299966), (0.63678527, 0.63678527, 0.63678527), "SM_Cliff_1036", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4404.2075, 19655.02, 1057.8892), (-15.110259852132781, 0.0, -0.0), (2.8984609, 1.9154365, 2.955845), "SM_Cliff_1046", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3867.3787, 8143.2227, 214.52002), (88.11873378592067, -179.99998474121543, -179.99998474121543), (1.0, 1.0, 1.0), "SM_Cliff_1054", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (7644.028, 8626.732, 240.57736), (3.561861660878057, -7.557982903193671, -1.7824705874998157), (0.74133974, 0.74133974, 0.74133974), "SM_Cliff_1055", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (7108.544, 8846.4, 163.74327), (3.209986186725734e-07, 17.59232823518111, -165.12264031735285), (0.20399125, 0.1619068, 0.03375959), "SM_Cliff_1062", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (11048.101, 7013.5566, 661.70056), (0.0, 0.0, -89.90110023215689), (1.0, 0.7293543, 1.0), "SM_Cliff_1068", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (11495.779, 2972.5867, 625.0024), (-0.00012167343208161751, -22.419464286101775, -89.9999343616608), (2.616941, 1.0, 1.718021), "SM_Cliff_1069", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (11640.006, 7123.3535, 625.0033), (4.646758647682477e-07, -165.46506446108887, -89.99977947684715), (2.616941, 1.0, 1.718021), "SM_Cliff_1070", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (10950.876, 2130.3716, 625.0022), (8.79569167641538e-07, -27.48238831350905, -89.99993627148754), (2.616941, 1.0, 1.718021), "SM_Cliff_1072", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (11782.582, 12835.613, 597.8347), (2.167450064929327, 55.539036702855256, -95.60119376081785), (1.0, 1.0, 1.0), "SM_Cliff_1074", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (11015.693, 11611.202, 672.4949), (-5.324585019576759e-08, -2.327941678999294, -86.93614824056182), (0.76000965, 0.39183143, 0.5665491), "SM_Cliff_1076", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5436.377, 9271.67, 611.1168), (1.2720609929436038, 115.54332345092767, -2.6596062908157942), (1.2216125, 1.2216125, 1.2216125), "SM_Cliff_1077", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1914.7904, 2768.6829, 1069.8292), (10.153739051664516, 104.61794453020285, -20.544464417391335), (3.4490972, 3.4490972, 2.7015696), "SM_Cliff_1084", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4757.9756, 13794.288, 1492.7046), (-5.163055411231668, -21.474612752840244, -11.782166367012609), (3.7806284, 1.6789026, 2.490875), "SM_Cliff_1085", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5216.1714, 9170.865, 250.28333), (0.0, 108.47095224510807, -0.0), (1.0, 1.0, 1.0), "SM_Cliff_1089", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (10560.531, 13023.267, 837.212), (-28.71282510182866, 70.83864491629394, -6.8049290040322346), (1.0058478, 0.9481242, 1.1715417), "SM_Cliff_1097", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5652.5503, 8959.217, 238.87085), (1.2163131217957344, 135.60692037084266, -1.3522643592526986), (0.93378675, 0.9710122, 0.9710122), "SM_Cliff_1102", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (10211.482, 12559.096, 709.5216), (-25.983335618689427, 77.08405161331972, -15.483274002716202), (0.50534374, 0.50534374, 0.50534374), "SM_Cliff_1104", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3551.9387, 11852.519, 965.9919), (-14.195983960762996, 0.0, -0.0), (1.4318298, 1.4318298, 1.4318298), "SM_Cliff_1106", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (7606.663, 12070.326, 148.69278), (-79.99984125517771, -151.2811074983531, 3.43752829161945e-05), (0.68389297, 0.5712795, 0.31863448), "SM_Cliff_1110", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (7575.9277, 7443.1064, 180.79858), (-10.319883904418, -178.603642348601, 176.7385947047214), (1.0, 1.0, 1.0), "SM_Cliff_1113", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3600.451, 9422.119, 23.3667), (0.0, -162.24717866343187, 0.0), (1.7195494, 1.7195494, 1.7195494), "SM_Cliff_1114", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (10959.708, 11835.654, 664.72363), (-26.15319563774587, 51.61798151665221, -1.9574293942341912), (0.60108125, 0.551351, 0.40556908), "SM_Cliff_1116", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (12044.107, 4802.0293, 1211.0944), (30.716685587909822, 87.94634849123872, -4.273926285675257), (2.352704, 2.352704, 2.352704), "SM_Cliff_1117", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (10487.965, 11465.506, 541.6801), (6.06269841299151, 31.586006938261164, 84.60566583166751), (0.7136888, 0.5259937, 0.5617641), "SM_Cliff_1127", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4417.3735, 11579.841, 1678.5771), (-11.581908104470632, 1.6890920271415182, -165.4846281537273), (2.3681622, 1.8457355, 1.8457355), "SM_Cliff_1129", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5909.4585, 13359.308, 1473.641), (0.0, -34.35515859849995, 0.0), (3.1088922, 1.4139104, 2.0202181), "SM_Cliff_1137", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1333.64, 2726.3145, 677.95605), (-3.032470653788965, -22.17443914105171, 3.781220087730669e-07), (2.27545, 2.27545, 2.2023902), "SM_Cliff_1142", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5873.691, 5611.369, 213.80739), (-14.894106457963451, -8.646545855892356, 2.2383263273578624), (1.0, 1.0, 1.0), "SM_Cliff_1143", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (7667.892, 16534.646, 236.75049), (1.3557817188192773e-05, 7.017944421217072, 91.67725057159308), (1.75059, 1.0, 1.0), "SM_Cliff_1152", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5575.108, 7692.272, 96.08911), (2.212208904295585, -171.60052721292644, -92.24307144422036), (1.0864384, 0.87866706, 0.87866706), "SM_Cliff_1153", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (9318.995, 8867.458, 220.08298), (0.2343502492231984, -100.40198540860989, -111.42956329099015), (0.94262165, 0.5791967, 0.7926055), "SM_Cliff_1155", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5736.309, 7082.4595, 153.63647), (2.2122102925815943, -161.51562712379393, -92.24311103470527), (1.5650277, 0.8341561, 1.1187562), "SM_Cliff_1160", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2006.141, 8050.0, 370.1877), (1.7080683136084156, 109.93013974092682, -4.69982921230726), (1.897241, 1.897241, 1.668699), "SM_Cliff_1161", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5716.3, 7411.6978, -69.03033), (81.83749811387797, 81.12507170438438, 143.61637375995426), (1.0, 1.1799295, 1.2849933), "SM_Cliff_1164", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4278.693, 18858.807, 743.7874), (-10.803009377577354, 2.656612767056034, 21.073370786112932), (2.0864565, 2.0864565, 1.6853944), "SM_Cliff_1165", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (6285.77, 5353.799, 285.50375), (-5.873512737815594e-09, 169.0791333878995, -8.297973387035938), (0.81526124, 0.81526124, 0.81526124), "SM_Cliff_1174", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5302.3037, 13501.769, 1452.2509), (-4.403747691027058, -27.44940232941719, 2.2840570260376025), (3.45909, 2.104889, 2.104889), "SM_Cliff_1177", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1914.7904, 3450.8987, -434.74597), (10.153739493301378, 77.23512516574957, -20.54434507367433), (3.449097, 3.449097, 2.70157), "SM_Cliff_1179", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5085.978, 3930.309, 794.21246), (-1.4834290472859275, 0.5400639076223938, -16.68792738282314), (1.8556844, 1.8254122, 1.5805643), "SM_Cliff_1188", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (6504.342, 4420.512, 1009.85724), (9.38384042441474, -93.87954440882865, 2.6645468854410352), (1.8961823, 2.0956633, 2.1562455), "SM_Cliff_1190", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (11288.751, 13101.098, 717.0654), (14.846784688350299, -141.82940230653057, 166.81970837495533), (1.73412, 1.482554, 1.482554), "SM_Cliff_1191", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (7075.161, 3919.5427, 1203.4331), (-15.123719361081768, 106.8449640059139, -66.83081441629605), (1.642779, 1.550342, 1.129532), "SM_Cliff_1193", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (6434.795, 4395.4087, 708.73236), (-12.008605497092798, -5.831298979979248, 9.828176299644335), (2.6413436, 1.7594552, 2.324008), "SM_Cliff_1194", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (7584.405, 13180.101, 284.52124), (-73.548858193432, 113.4326690666123, -130.45774069232777), (1.042725, 0.95028806, 0.529478), "SM_Cliff_1197", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2398.9736, 9967.979, 765.75867), (-2.851165975604503, -178.59325965341466, -6.20095788069395), (1.878557, 1.878557, 1.878557), "SM_Cliff_1200", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3517.563, 17038.408, 3057.3352), (3.0618625433790245, 158.07647957796226, -13.886871745076398), (2.194077, 2.194077, 1.541373), "SM_Cliff_1201", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (8383.73, 12889.211, 341.49844), (-9.999940019189406, 26.87797697062641, 15.000351901153117), (1.0, 1.0, 1.0), "SM_Cliff_1213", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (6354.623, 12867.393, 2037.4558), (-4.783721076916945e-07, -79.35482274130082, 20.000163528314356), (3.108892, 1.41391, 1.0080594), "SM_Cliff_1216", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (7850.0, 12750.0, 300.0), (0.0, 0.0, -0.0), (1.0, 1.0, 0.505468), "SM_Cliff_1225", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3504.0627, 9451.818, 339.07635), (-11.523527805358132, 166.96593583000146, 2.441389929639216), (1.264182, 1.4573429, 1.45463), "SM_Cliff_1260", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (9690.417, 7750.9414, 537.56177), (-10.166838934640735, -1.3132625555551165, -14.71438609541125), (0.667324, 0.667324, 0.53821033), "SM_Cliff_1271", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2537.769, 10374.356, 552.81226), (-7.571502504219505, 53.446863452197526, -1.837829152566278), (1.942703, 1.942703, 1.78299), "SM_Cliff_1280", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3189.6719, 12502.351, 1087.7747), (-16.566012387689987, 1.2789419343804298, -175.38460582535984), (1.4060745, 1.845736, 1.845736), "SM_Cliff_1286", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3192.3953, 12971.064, 1374.4116), (11.581814990464286, -178.3109011216116, 165.48438071355378), (1.3143426, 1.845736, 1.845736), "SM_Cliff_1287", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3223.4272, 14654.0, 1231.6075), (-14.195983960762996, 0.0, -0.0), (1.43183, 1.43183, 1.43183), "SM_Cliff_1304", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3150.446, 11101.871, 623.62274), (19.145983203430724, 170.8110372060716, -11.636047879055448), (2.5344586, 1.6983564, 1.1517324), "SM_Cliff_1308", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4390.5225, 15400.28, 1334.966), (1.6720919897027466, 6.226507968574787, -24.904936215383216), (1.393551, 1.779489, 1.779489), "SM_Cliff_1312", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (9903.652, 8747.783, 397.71573), (1.8630036294037329, -0.31536863400600434, -94.77831646979155), (1.8714001, 1.4469687, 0.88658774), "SM_Cliff_1313", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2706.2046, 12709.573, 452.90054), (-21.598877533310016, 22.978760896768822, -5.86389129842173), (1.6858608, 1.942703, 1.78299), "SM_Cliff_1316", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3088.0647, 15965.056, 1457.2902), (-9.100739075400684, 3.2812203050080333, 20.55663678736924), (1.9874368, 1.779489, 1.779489), "SM_Cliff_1323", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2820.7063, 18698.629, 1105.4817), (-4.865023005987766, 82.4461050138807, -32.60107429077064), (2.313857, 2.313857, 2.32221), "SM_Cliff_1328", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4045.7751, 7652.5435, 231.76483), (-1.969268962812386, -16.963472198060007, 78.65311990035465), (1.0, 1.0, 1.0), "SM_Cliff_1338", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3410.4214, 16229.199, 902.00494), (25.096237437386936, 157.81974151697125, -21.937317521173505), (2.5819302, 2.4140356, 1.6330409), "SM_Cliff_1342", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (6470.0, 12900.0, 2400.0), (0.8671812051112119, -170.0372051957051, -4.924407982672863), (1.0, 1.0, 1.0), "SM_Cliff_1343", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5206.2764, 6067.4697, 315.7865), (-3.034115350787941, 37.26828920467168, -86.02063523717491), (0.6265735, 0.29169413, 0.47145623), "SM_Cliff_1354", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3218.9736, 9902.979, 680.75867), (-15.434845171477393, -133.15611908095502, -15.952208884399802), (1.878557, 1.878557, 1.878557), "SM_Cliff_1369", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1370.9464, 10039.982, 634.9228), (0.29474288057125486, 0.0, -0.0), (1.3942016, 1.3942016, 1.3942016), "SM_Cliff_1370", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (11470.0, 8885.0, 680.0), (-16.130950807203405, -30.18261856082441, -8.01309218489779), (0.6775757, 0.6775757, 0.6775757), "SM_Cliff_1398", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4912.9595, 18280.012, 2314.3389), (-13.769379279585374, 5.902170365038708, 21.620355879165672), (2.0547905, 2.0547905, 1.6702114), "SM_Cliff_1403", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4519.3145, 18150.04, 2992.3442), (12.720879546107819, 154.09340218610913, -27.9082626288231), (2.194077, 2.194077, 1.541373), "SM_Cliff_1410", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5895.1133, 6831.2065, 186.14165), (0.0, 0.0, -10.604126342619312), (0.65061194, 0.87425303, 0.90010494), "SM_Cliff_1449", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (11030.809, 8562.081, 523.5582), (2.3515682142192612e-07, -19.999995194986923, -89.99999317202912), (1.0, 1.0, 1.0), "SM_Cliff_1458", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (9897.079, 14787.331, 2178.3062), (22.84577948982846, -145.5494994347871, 170.50316868773555), (1.73412, 1.482554, 1.482554), "SM_Cliff_1467", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (10220.99, 15146.581, 3084.2454), (-11.825285388346183, 96.6292213897422, -16.688750903168486), (1.8023142, 1.8752741, 1.3469203), "SM_Cliff_1472", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4858.3457, 18731.33, 974.0919), (-19.859161289204078, 103.91531027560836, -26.07757703663163), (1.97936, 1.97936, 1.97936), "SM_Cliff_1474", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (9640.624, 6823.941, 680.2713), (-18.398985514740566, -162.97908855905908, 12.862644497077625), (0.90626365, 0.90626365, 0.90626365), "SM_Cliff_1475", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (9194.577, 5187.479, 718.98126), (-0.2933958653573719, -34.13400437113814, -11.34808170830454), (1.4504395, 1.4504395, 1.4504395), "SM_Cliff_1477", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (8125.513, 10464.218, 82.36863), (0.5746102860623661, 25.754848288935282, 87.01269896991239), (0.97906876, 0.47452, 0.32812005), "SM_Cliff_1482", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (9216.668, 6439.6694, 519.91595), (-2.308836795032085, 123.60141387150965, 12.963783943023328), (1.1065089, 1.1065089, 1.3561373), "SM_Cliff_1483", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (9115.561, 4833.3643, 333.51974), (3.757928422711517, 76.92645424012346, -7.034697594382531), (1.5675161, 1.5675161, 1.5675161), "SM_Cliff_1489", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (9615.514, 4589.2236, 555.4561), (-13.763580751862708, 143.9536837863573, -4.697022276999064), (1.5730516, 1.796044, 1.5730516), "SM_Cliff_1495", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (8265.9, 6010.8857, 411.82288), (-6.279816797873788, 114.24756761854755, 8.650125993753608), (1.296738, 1.296738, 1.296738), "SM_Cliff_1502", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (9685.938, 5738.4663, 506.33276), (6.889851790632999, 128.96174066424416, -27.57968166217166), (1.1557608, 1.0996251, 1.0996251), "SM_Cliff_1506", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (10054.054, 6048.2334, 854.4146), (-6.563214330821283e-08, -34.99994113657086, -4.999999957158739), (1.0, 1.0, 0.7400123), "SM_Cliff_1511", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (9315.44, 6815.682, 637.8321), (-1.91093227621927e-07, -35.358487799790666, -19.039579965471585), (1.1413639, 1.1413639, 1.1413639), "SM_Cliff_1513", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (9071.096, 6603.909, 849.08234), (4.857363613203822, -57.52719074107945, -18.69390688705002), (1.0, 1.0, 1.0), "SM_Cliff_1520", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (10248.047, 5885.5884, 674.1492), (0.0, -135.0000537473682, 0.0), (1.0, 1.0, 1.0), "SM_Cliff_1521", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (9239.276, 10299.784, 212.34564), (-3.051756853768794e-05, -179.99997950942887, -179.99997950942887), (1.0, 1.0, 1.0), "SM_Cliff_1526", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (10316.784, 8516.114, 634.3247), (-2.1108702818955463, -165.0833589936779, 4.533675136405277), (1.1233438, 1.0, 0.34622544), "SM_Cliff_1532", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5151.5405, 9518.181, 749.3554), (-11.773224905333006, 14.664136791875578, -7.690673279721159), (1.0, 1.0, 1.0), "SM_Cliff_1533", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4165.435, 9925.225, 364.19046), (-20.153593363943994, -169.72698598672383, 4.950009219292985e-06), (1.339452, 1.339452, 1.339452), "SM_Cliff_1539", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3779.0798, 9762.816, 573.86993), (-14.999970253878695, -140.0000612096972, -10.00000025346842), (1.0, 1.0, 1.0), "SM_Cliff_1544", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4183.434, 17806.059, 975.70154), (-21.342651271841152, -9.368011949977086, 24.384044816380474), (2.0966177, 2.0966177, 2.0966177), "SM_Cliff_1546", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4739.3066, 18511.4, 978.26416), (-14.67965761471092, 112.34074824314148, -15.296785040009494), (1.969636, 1.969636, 1.969636), "SM_Cliff_1554", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3565.0479, 10109.108, 487.5677), (17.732249957117336, -13.81023994432061, 162.8354535301629), (1.2999862, 1.2999862, 1.2999862), "SM_Cliff_1557", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2551.2568, 7998.8315, 757.069), (8.828380232102273, -119.06866941080263, -18.225952501121906), (1.3879904, 1.878557, 1.878557), "SM_Cliff_1560", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (9253.615, 4433.1865, 725.75903), (-22.01632400600751, 71.75585252332388, 7.044387058922878), (1.4894449, 1.4894449, 1.4894449), "SM_Cliff_1565", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4987.536, 2137.308, 791.4695), (-3.004973852451704, -86.08489656226651, 5.730184848920567), (2.3952775, 2.3952775, 2.3952775), "SM_Cliff_1573", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5320.9062, 9797.034, 575.5669), (-15.665711505513377, -46.66104169130879, -6.581878250226734), (1.0, 1.0, 1.0), "SM_Cliff_1574", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (7999.158, 7153.087, 697.3289), (-2.1106872271930825, 9.916015136114945, -175.4664809002255), (1.0, 1.0, 1.0), "SM_Cliff_1580", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (8392.666, 7022.549, 307.3973), (-1.0446778501994964, -50.32296325003236, -3.9024045624236914), (1.141364, 1.141364, 1.141364), "SM_Cliff_1588", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (7171.5874, 11604.288, 148.69284), (-69.8087196810502, -102.3869606559831, -13.253021681656655), (0.683893, 0.57128, 0.318634), "SM_Cliff_1590", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (7990.0947, 8502.175, 193.4524), (2.81583739859396, 106.88247301100259, 90.75135623144415), (0.628386, 0.176497, 0.370115), "SM_Cliff_1610", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3583.7568, 11163.821, 450.13672), (19.145983203430724, 170.8110372060716, -11.636047879055448), (2.534459, 1.698356, 1.151732), "SM_Cliff_1615", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (6528.2915, 14085.505, 444.03955), (4.090186075058522e-06, 69.15529842737, 91.67724975076155), (1.75059, 1.0, 1.0), "SM_Cliff_1621", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (7899.895, 15405.962, 236.7511), (7.18233948462238e-06, 12.383178079328811, 91.67724966299885), (1.75059, 1.0, 1.0), "SM_Cliff_1627", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (7899.895, 14765.149, 236.75098), (7.18233948462238e-06, 12.383178079328811, 91.67724966299885), (1.75059, 1.0, 1.0), "SM_Cliff_1628", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (7448.9976, 17024.262, 330.82306), (7.602110593522847, -164.2031508246157, 87.67658111433968), (1.75059, 1.0, 1.0), "SM_Cliff_1630", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (7230.949, 17663.172, 236.7478), (7.18233948462238e-06, 12.383178079328811, 91.67724966299885), (1.75059, 1.0, 1.0), "SM_Cliff_1631", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (6497.8853, 8199.252, -26.277527), (-2.513730704945063, 51.50732480561924, -100.50384526887872), (1.029624, 0.2950593, 0.582874), "SM_Cliff_1637", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (7909.8354, 8448.24, 192.55278), (-1.3484202358580382, -99.52528969688035, 85.42121795692418), (0.62838566, 0.17649712, 0.3701148), "SM_Cliff_1652", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4198.9736, 11417.979, 1380.7587), (4.1425048573745176e-08, 106.64591363365994, -15.789825241129948), (1.8785568, 1.8785568, 1.8785568), "SM_Cliff_1658", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (10181.305, 8735.373, 550.18665), (-3.026702924449394, -151.73577852115372, -33.236109936089285), (1.5604655, 0.8414698, 1.0), "SM_Cliff_1676", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (7772.078, 17654.598, 627.7465), (-27.043669138633238, -4.763854770474499, 12.365445678601624), (1.5432818, 1.5432818, 1.5432818), "SM_Cliff_1709", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (7773.8887, 18295.135, 743.37885), (-36.58569479400629, 0.0, -0.0), (1.7424464, 1.7424464, 1.7424464), "SM_Cliff_1715", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (9387.254, 15420.026, 2541.9915), (-14.383115976660122, -4.303100309709112, 16.852306308349185), (2.100438, 2.4520836, 2.217537), "SM_Cliff_1727", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5675.967, 3609.062, 556.89014), (-2.3846435541621087, 51.670581799771384, 1.9280230535689813), (2.0551476, 2.0551476, 1.9468912), "SM_Cliff_1733", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4102.0576, 4154.0703, 359.64307), (-11.063079382988594, 7.5069799796112555, -34.477993906504665), (1.7322879, 1.7322879, 1.7322879), "SM_Cliff_1748", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5997.4673, 4184.7773, 1356.0609), (-11.578673840106319, 4.677388107637013e-06, 18.64749662863333), (2.095833, 2.095833, 2.095833), "SM_Cliff_1758", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5273.103, 1691.0984, 2068.9), (-17.941772648027616, 6.275227344053174, 14.280876018951414), (2.238815, 2.238815, 2.238815), "SM_Cliff_1765", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5463.0356, 2247.3376, 2200.417), (-20.72296111745759, 0.0, -0.0), (1.8842926, 1.8842926, 1.8842926), "SM_Cliff_1773", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5453.611, 2541.9163, 2471.4358), (-26.752653594032, -21.427704207867208, 8.485961727586211), (1.8752531, 1.8752531, 1.8717846), "SM_Cliff_1780", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2100.0, 2500.0, 1550.0), (-25.00000055343977, 0.0, -0.0), (2.453841, 2.453841, 2.453841), "SM_Cliff_1799", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3650.0, 4250.0, 550.0), (-25.00000055343977, 0.0, -0.0), (1.3784311, 1.3784311, 1.3784311), "SM_Cliff_1831", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (8693.264, 12369.695, 532.07574), (-6.658112018472659, 137.8741099096196, -28.151763223699795), (1.0, 1.0, 1.0), "SM_Cliff_1841", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (8533.73, 12139.211, 341.49844), (-9.999939049431385, 1.8275460166689743e-06, 15.000193398851648), (1.0, 1.0, 1.0), "SM_Cliff_1848", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3599.8098, 7651.842, 553.9495), (-22.521120558995115, -168.85167252093115, -27.22561586270703), (1.5329232, 1.5329232, 1.5329232), "SM_Cliff_2058", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3200.0, 7850.0, 800.0), (-9.999999490266388, 2.70219808615438e-07, 30.000049280018235), (1.0, 1.0, 1.0), "SM_Cliff_2080", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3299.9995, 7021.131, 595.31537), (23.398931672171766, -111.87974931224215, 170.93806134341767), (1.0, 1.0, 1.3119451), "SM_Cliff_2090", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3693.463, 7226.798, 363.04816), (26.184192017376734, -49.286686256790844, 170.49008384633157), (1.0, 1.0, 1.0), "SM_Cliff_2104", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3904.1997, 7681.175, 379.88348), (6.0715835704608934e-06, -145.00011727516042, -30.000068168098924), (1.0, 1.0, 1.0), "SM_Cliff_2111", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2757.533, 8073.1587, 286.08765), (-15.788814387641407, 70.6064968572383, -179.62562998558468), (1.8972412, 1.8972412, 1.382294), "SM_Cliff_2115", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3921.8118, 17381.564, 1180.7404), (-38.831690663117115, 53.342658686967134, -6.9864183661764), (2.875349, 4.1752687, 2.875349), "SM_Cliff_2142", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4511.5713, 16941.854, 898.8805), (8.3676364663061, 133.68413988324355, -18.54708906827256), (2.1350992, 2.1350992, 1.7574123), "SM_Cliff_2150", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4992.7563, 16826.436, 861.6295), (8.29297680355023, 156.45605009169776, -27.477084852479482), (2.1940775, 2.1940775, 1.5413729), "SM_Cliff_2158", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5204.4824, 16443.893, 356.6187), (-16.27526580036077, 1.9965763083264013e-05, -166.3219125387184), (1.6889298, 1.5657926, 0.3512771), "SM_Cliff_2164", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5207.9595, 16940.012, 569.3388), (-13.769379925902395, -4.09783971555565, 21.620356047749976), (1.6190094, 1.6190094, 1.2344298), "SM_Cliff_2173", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (9051.277, 4193.584, 1250.1678), (-60.489723336489774, 12.884522430511788, -58.78571841631482), (1.6427791, 1.5503422, 1.1295317), "SM_Cliff_2216", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5016.963, 11242.781, 1200.0558), (7.818461678377564, 107.63440901999093, -12.598602469132107), (2.1266196, 2.0947902, 2.4862182), "SM_Cliff_02_1120", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (9957.028, 10232.534, 587.401), (2.5029979940844216, -90.67721935755152, 0.006081604068163594), (0.6841099, 0.759454, 0.402914), "SM_Rock_Large_33", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (10196.636, 8822.996, 655.04846), (0.6581365839278643, -150.7203167586912, -7.474243847113972), (1.0235178, 0.8828209, 0.52628076), "SM_Rock_Large_1375", _folder)
if a: placed += 1
else: skipped += 1

# Batch 165: StaticMesh'SM_Cliff_02' (10 instances)
_mesh_path = "/Game/Unshippable/ThirdParty/Lordenfel/Environment/Rocks/SM_Cliff_02"
_materials = ['/Game/Unshippable/ThirdParty/Lordenfel/Environment/Materials/MI_Lordenfel_RedRock_Cliff_03']
_folder = "Reconstruction/BD_BB_Outdoor_TradingPost/Meshes"
a = spawn_static_mesh(_mesh_path, _materials, (9152.656, 9107.178, 240.65536), (-20.28662092342118, -8.219360859887907, -0.983062636378656), (1.0, 1.0, 1.0), "SM_Cliff_30", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (9699.698, 9125.478, 327.87894), (-6.422119755359123, -0.09051517989647447, 16.376329343288766), (1.0, 1.0, 1.0), "SM_Cliff_50", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (10601.371, 14254.046, 636.1416), (-11.302641165970103, 66.72628337259395, 167.24095417148214), (1.0, 1.0, 1.0), "SM_Cliff_147", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (9481.785, 8795.821, 257.44983), (-30.28509669482106, -8.021666863275046, 18.93210542795378), (1.0, 1.0, 1.0), "SM_Cliff_196", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3669.7231, 1880.3037, 892.8968), (-21.867095737362305, 5.395287654917893, -2.0146178816110227), (2.2496839, 2.5706728, 2.2496839), "SM_Cliff_714", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4354.6846, 2237.3716, 2113.2422), (-21.867095737362305, 5.395287654917893, -2.0146178816110227), (1.4599226, 1.7809122, 1.4599226), "SM_Cliff_729", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3555.3137, 6841.1655, 418.7036), (-29.646181714423527, 131.085643321762, -179.8141492696214), (0.8916208, 0.8129452, 0.93561745), "SM_Cliff_1004", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (6274.5415, 5654.885, 253.78366), (13.046261020018989, -32.98502124771967, -8.335328293155792), (0.7096954, 0.7096954, 0.7096954), "SM_Cliff_1231", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (9730.0, 10185.0, 775.0), (2.561703916431294, 74.69771602483436, -5.270660791395155), (0.83765006, 0.8567898, 0.621486), "SM_Cliff_1332", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (9480.67, 9135.775, 342.6424), (-34.99996476621819, -9.999877720826715, 4.874921374674311e-06), (1.0, 1.0, 1.0), "SM_Cliff_2306", _folder)
if a: placed += 1
else: skipped += 1

# Batch 166: StaticMesh'SM_Cliff_03' (3 instances)
_mesh_path = "/Game/Unshippable/ThirdParty/Lordenfel/Environment/Rocks/SM_Cliff_03"
_materials = ['/Game/Unshippable/ThirdParty/Lordenfel/Environment/Materials/MI_Cliff_03']
_folder = "Reconstruction/BD_BB_Outdoor_TradingPost/Meshes"
a = spawn_static_mesh(_mesh_path, _materials, (3999.966, 4878.547, 382.8564), (0.0, 0.0, -50.000000322548), (0.65847623, 0.7883288, 0.7883288), "SM_Cliff_43", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (10644.051, 14220.75, 820.39124), (-5.943847132633669, -43.07113359829504, 0.6303540955949911), (1.0398426, 1.0398426, 1.0398426), "SM_Cliff_124", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4380.923, 3278.7764, 967.74084), (-7.157195979206003, 0.812341156120545, -29.7440766415339), (1.5783528, 1.5783528, 1.5783528), "SM_Cliff_1741", _folder)
if a: placed += 1
else: skipped += 1

# Batch 167: StaticMesh'SM_Cliff_03' (1 instances)
_mesh_path = "/Game/Unshippable/ThirdParty/Lordenfel/Environment/Rocks/SM_Cliff_03"
_materials = ['/Game/Unshippable/ThirdParty/Lordenfel/Environment/Materials/MI_Lordenfel_RedRock_01']
_folder = "Reconstruction/BD_BB_Outdoor_TradingPost/Meshes"
a = spawn_static_mesh(_mesh_path, _materials, (1271.8256, 8185.0825, 313.59918), (85.94027896886246, -0.00012164705614018463, -2.3077402628902317), (1.50055, 1.50055, 1.50055), "SM_Cliff_755", _folder)
if a: placed += 1
else: skipped += 1

# Batch 168: StaticMesh'SM_Cliff_03' (297 instances)
_mesh_path = "/Game/Unshippable/ThirdParty/Lordenfel/Environment/Rocks/SM_Cliff_03"
_materials = ['/Game/Unshippable/ThirdParty/Lordenfel/Environment/Materials/MI_Lordenfel_RedRock_Cliff_03']
_folder = "Reconstruction/BD_BB_Outdoor_TradingPost/Meshes"
a = spawn_static_mesh(_mesh_path, _materials, (11340.0, 6460.0, 660.0), (-14.081146748105612, -35.61688439988379, 2.954290246848657), (1.0, 1.0, 1.0), "SM_Cliff_2", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (10571.652, 12991.713, 618.64215), (-13.614104810505467, -27.93371278285516, 82.1983866316839), (0.44529, 0.44529, 0.44529), "SM_Cliff_10", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (9842.524, 8563.729, 269.86063), (-15.253997755327639, 7.564685272290639, 14.750228975325678), (1.218154, 1.316636, 1.157231), "SM_Cliff_11", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (9235.519, 14053.156, 939.1592), (-21.15807818904851, 104.18180041177934, -16.272429675673393), (1.5535786, 1.5535786, 1.5535786), "SM_Cliff_14", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (12001.938, 10703.633, 522.0615), (-85.69660737866252, -179.99978097798513, 161.95815804546248), (1.4137589, 2.8181899, 1.4137589), "SM_Cliff_18", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (11962.286, 7970.2314, 474.08533), (-2.0611882052816877, -108.73157031614673, -6.054290987749931), (2.239886, 2.239886, 1.9132907), "SM_Cliff_26", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (8011.15, 6372.3135, 555.7666), (-1.513213704039161, 107.52650973190124, -7.276550055046165), (1.0696315, 1.6135474, 1.6135474), "SM_Cliff_28", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (9263.998, 12047.506, 157.99237), (84.7605010912501, -63.46934394800562, 111.87840137110506), (1.5568974, 3.59498, 1.782058), "SM_Cliff_29", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (11082.218, 3702.9648, 779.136), (-19.404601806246884, -7.119537213049393, 1.1771722980878367e-06), (3.0669675, 3.0669675, 2.4692326), "SM_Cliff_31", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (11833.616, 7423.4575, 447.90024), (89.83848711584751, 2.0098324466105515, -98.13911967892301), (1.69769, 3.297614, 3.051486), "SM_Cliff_32", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (8889.115, 11880.386, 696.2094), (-24.128480578051636, 147.4448136714379, 2.5086743952139456e-05), (0.73786914, 0.73786914, 0.73786914), "SM_Cliff_40", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3975.5713, 5571.7085, 387.90826), (4.098113201440978e-05, -7.837205513714311e-13, 84.99995206266284), (0.9145577, 1.1880615, 0.9145577), "SM_Cliff_60", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (8723.765, 14548.37, 597.9557), (-11.083070201923471, -37.56683497427257, 27.754832820525714), (3.3019001, 2.5410998, 3.2239602), "SM_Cliff_63", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (7850.0806, 18303.957, 900.4533), (-25.093994155229563, 0.0, -0.0), (2.0649648, 2.0649648, 2.0649648), "SM_Cliff_64", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (10948.207, 9003.712, 547.33325), (-0.9720763559597433, -12.652250809519106, -82.48689757627693), (0.4434116, 0.4434116, 0.4434116), "SM_Cliff_65", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (11993.091, 11912.611, 943.0112), (-4.739989950002688, -34.25555003607864, -0.7399289659675038), (2.054751, 2.054751, 2.054751), "SM_Cliff_67", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (11681.18, 15149.609, 3681.7197), (-13.359068451077855, 4.808651532925309, 4.945452693869418), (2.5719328, 3.3264735, 2.8024857), "SM_Cliff_72", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (10848.633, 13098.958, 757.4971), (0.28378076789522816, -15.089446947330371, 16.852732495174294), (1.401342, 1.401342, 0.8440288), "SM_Cliff_76", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (9435.315, 7109.168, 237.62949), (-4.999969509830419, -35.00006010537411, -10.00018417097882), (1.1545465, 1.1545465, 1.1545465), "SM_Cliff_77", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (9735.525, 10144.601, 422.89474), (-20.104826965080797, 65.8207728207686, 60.57342488146955), (0.8514747, 1.4695543, 0.8514747), "SM_Cliff_79", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (12271.097, 10800.0, 699.60114), (-6.021758635525603, 0.0, -0.0), (2.2398863, 2.2398863, 2.2398863), "SM_Cliff_89", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (9685.812, 7901.475, 332.53793), (-19.999938265742262, -19.999999026564407, 3.4302512958489494e-06), (0.794311, 0.794311, 0.794311), "SM_Cliff_92", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (9352.504, 4228.2236, 477.4968), (87.46693643762015, -40.223520573174525, 55.8822196850512), (1.3161397, 1.6661046, 1.5139816), "SM_Cliff_108", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (12026.759, 14092.675, 2001.1216), (-21.181642876211455, 44.541312578550446, 13.818742901246496), (2.6735733, 2.369379, 2.2010036), "SM_Cliff_117", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (8836.645, 12609.196, 707.50073), (-34.96167204040621, 67.76524704264929, 19.186093411421815), (1.0, 1.0, 1.0), "SM_Cliff_119", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5500.9473, 9360.322, 227.66907), (-64.99972208255379, -116.39539383625812, 84.99970188599978), (1.3272396, 1.3272396, 1.3272396), "SM_Cliff_120", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (11910.017, 10794.436, 323.15347), (84.75992045865159, -63.46962168813954, 0.020613427385519852), (2.1969361, 3.59498, 1.1758778), "SM_Cliff_123", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (11829.563, 11649.615, 600.0), (4.006561258377464, -104.0089974804608, 2.4069416218183082e-06), (2.2198281, 1.7718691, 2.2198281), "SM_Cliff_132", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (11776.88, 11851.834, 448.85934), (89.84881891180055, 0.655471335570582, 94.10806125136308), (1.6976901, 3.2976143, 3.0514855), "SM_Cliff_135", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (12110.191, 13503.34, 1134.8665), (-12.079070376220356, 35.80458825405798, 14.554391391204982), (2.677596, 2.677596, 2.0193927), "SM_Cliff_137", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (8810.087, 14235.45, 1265.0156), (-22.62356411615263, 16.412708546372937, 12.49149919034273), (3.2595773, 2.3155437, 2.3155437), "SM_Cliff_143", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (10548.201, 14214.681, 1394.2366), (-35.72768802646463, -134.09765046980615, 3.2347555094293443), (1.0, 1.4224857, 1.0), "SM_Cliff_155", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (10281.97, 15015.366, 910.5342), (-21.017823461893208, -8.65979062138923, 10.392924566064119), (1.5319561, 2.081164, 1.7073566), "SM_Cliff_164", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (10771.039, 13369.385, 866.5198), (-5.715515045036164, 150.12548617132674, 59.5852386610479), (1.0, 1.985699, 0.471765), "SM_Cliff_178", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (9117.66, 18599.133, 1214.4784), (-24.45221336797474, 14.46951502258141, -6.096924198577061), (1.8203331, 1.8203331, 1.8203331), "SM_Cliff_180", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (11750.416, 6992.489, 284.90393), (-2.99966435122646, -35.21615345677423, -3.915740753938332), (1.7400867, 1.7400867, 1.5896794), "SM_Cliff_182", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (6314.261, 12215.327, 1113.3384), (-5.776337101159224, 44.766107264290355, 5.256952156555437), (3.089073, 3.089073, 2.5106142), "SM_Cliff_184", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (10858.187, 8413.611, 595.9795), (-0.2466102799079008, -30.84237180570461, -90.41292232594783), (0.473833, 0.473833, 0.473833), "SM_Cliff_185", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (9906.467, 8830.959, 448.6374), (-2.6909077793634595e-07, 14.776702596732148, -86.59136827950005), (1.0, 1.3797295, 1.0), "SM_Cliff_188", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (13133.552, 14031.967, 1105.9999), (-17.294401640789808, 28.40339007310338, 19.612174187708195), (2.005594, 2.005594, 2.005594), "SM_Cliff_200", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (6949.397, 3106.831, -63.00032), (-68.58136675717152, 22.72477196861543, 81.40446624561055), (1.1296945, 1.1296945, 1.1296945), "SM_Cliff_202", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5985.7866, 10647.377, 396.2689), (-8.82793987163179, 68.47613380956042, 5.635671835257229), (1.2717447, 1.0414026, 1.4782771), "SM_Cliff_204", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3769.21, 10009.41, 672.09924), (-9.001527032195273, 117.24029846384815, 33.30487237620082), (1.3474329, 1.0, 1.0), "SM_Cliff_210", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (9048.283, 12267.65, 592.4203), (-77.25122393888742, 0.4654602444699453, 90.54600576358311), (0.5988663, 1.0, 1.0), "SM_Cliff_246", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (10177.642, 5961.4595, 992.77325), (34.78535085394593, 16.9029842648057, 173.75352020873117), (1.0, 1.0, 1.0), "SM_Cliff_252", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (10290.244, 8489.091, 527.22046), (-11.78381360525597, 129.32307351907366, -3.171478190436585), (0.7956083, 0.7956083, 0.7956083), "SM_Cliff_253", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (11822.21, 2712.6348, 625.0041), (8.007859837444188e-07, -26.322140727809064, 90.0000179736538), (3.6306005, 1.755884, 3.3449922), "SM_Cliff_264", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (10479.296, 7740.953, 555.0382), (0.80685671815224, -40.226011959351, -89.0459586135679), (0.4322104, 0.4322104, 0.4322104), "SM_Cliff_270", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4766.3325, 14563.405, 1201.517), (-6.117307974957485, -63.9858558435566, 168.87661607092897), (1.44859, 1.1723583, 1.9551023), "SM_Cliff_288", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (12282.591, 13200.478, 549.07477), (0.0, 0.0, 79.99995877012579), (1.0, 1.0, 1.0), "SM_Cliff_295", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (11318.249, 13937.107, 2321.2446), (-17.551970522362417, 25.178281351457514, 14.739663472949752), (1.6414819, 2.0763617, 2.0763617), "SM_Cliff_301", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (11508.214, 14465.049, 2831.8872), (-13.332428038632525, 34.45040638849456, 5.416978568763066), (1.9276446, 1.9276446, 1.7494379), "SM_Cliff_304", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (10252.985, 6347.9805, 668.68243), (-9.756562360038755, -135.87208698119042, 17.425355976818945), (1.0, 1.0, 1.0), "SM_Cliff_308", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (12284.557, 16363.544, 549.0745), (7.339226719707409e-07, -10.000030595618355, 79.99996092468632), (1.0, 1.0, 1.0), "SM_Cliff_312", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2000.6934, 9777.593, 236.97107), (50.12956307099451, 83.06919417142419, 81.56003464756917), (2.2169654, 1.3648347, 1.4465035), "SM_Cliff_318", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1534.9922, 8020.0527, 248.51807), (60.56263463570607, -61.65289580328913, -58.22205092785891), (2.4284935, 1.55798, 1.855167), "SM_Cliff_320", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (9373.756, 16545.393, 1794.5366), (-18.60290547017305, -38.05551364709189, 15.707715929210787), (3.1312969, 3.9831848, 3.1891613), "SM_Cliff_327", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2141.9473, 8286.686, 113.59387), (78.3582732908685, -95.81714148626764, 80.01507323722234), (1.36515, 1.36515, 1.729219), "SM_Cliff_329", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (6197.7773, 11455.461, 674.5183), (-4.702087460226613, 5.613986300534052, 0.9775643167425742), (2.4466767, 1.7772671, 1.483986), "SM_Cliff_331", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3856.3926, 4881.039, 356.9815), (7.019384845227301, 6.090732389702036, -86.11778952518938), (0.699273, 0.9103037, 0.8213817), "SM_Cliff_332", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (6409.283, 10569.496, 103.04098), (-1.7941894107402405, 57.726846629902155, -7.950285626594646), (1.7471071, 3.2124405, 0.9186648), "SM_Cliff_339", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3351.7744, 2904.4932, 537.8609), (-0.17074564947225304, 3.0486604851923453, 85.00275805485425), (1.3011807, 0.9780555, 1.3011807), "SM_Cliff_346", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (10197.108, 6518.5503, 585.8454), (83.76551732610588, -0.00015021648976972006, -52.3282984260735), (0.31242567, 0.6429724, 0.40983167), "SM_Cliff_351", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (7730.061, 18495.818, 993.6085), (-30.69461167349849, 0.0, -0.0), (1.7178268, 1.7178268, 2.3588157), "SM_Cliff_352", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3670.577, 7040.452, 403.43054), (24.60645053166648, -33.85619472835794, -5.878051079850817), (0.66162574, 1.0713147, 0.953675), "SM_Cliff_357", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (6558.6245, 9777.906, 112.57454), (-9.960112803993406, -53.7162856750106, -86.88152589042339), (1.5039088, 0.26066026, 1.4142615), "SM_Cliff_368", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3901.557, 2278.8752, 850.3214), (-13.726104841584817, -77.1478247316245, 13.357208154610273), (2.733048, 2.441988, 2.733048), "SM_Cliff_376", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2980.1858, 7859.3936, 350.1206), (12.095772336770146, -27.32607796144538, 19.285814967094154), (1.56579, 1.56579, 1.929859), "SM_Cliff_377", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5899.0366, 3686.9907, 777.20416), (-0.5893554008568388, -177.45995128048062, -14.723508728862893), (3.5154028, 3.5154028, 2.4360945), "SM_Cliff_387", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (12091.595, 5151.504, 533.7243), (-1.2515678872025851e-08, 2.306857561934986, 89.99997663391481), (2.8039505, 1.2193974, 2.5183423), "SM_Cliff_395", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (10857.131, 3358.539, 1011.4986), (-17.049863299090685, -2.8741451724320326, 0.9281451626096394), (4.364089, 4.9832306, 2.894986), "SM_Cliff_400", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (8298.021, 6224.7856, 453.01007), (-6.788758038718485, 85.5125162125018, 8.724140239402603), (0.8081586, 1.8324542, 1.8324542), "SM_Cliff_416", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (12018.022, 14027.934, 1653.3496), (-1.4655458398065733, 7.415320466044074, -3.247680583889064), (2.219828, 2.219828, 2.5311217), "SM_Cliff_417", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3411.881, 7950.2803, 255.09328), (-9.656096666916874, -2.6130370279298116, 15.220789855992479), (1.0, 1.5579797, 1.5060679), "SM_Cliff_420", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (8457.642, 10738.677, 232.99054), (0.0, -20.000060948281234, 0.0), (0.74287915, 0.74287915, 0.70129335), "SM_Cliff_424", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3907.9043, 1049.2236, 1128.7156), (-5.762115657276422, -17.96810670195166, 13.854813136129886), (2.3787012, 2.885464, 2.9790125), "SM_Cliff_430", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5847.9287, 11578.992, 1235.9347), (-9.324311533379813, 45.235484602090025, -9.86334177149811), (2.4978187, 2.4978187, 2.4978187), "SM_Cliff_433", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (9073.724, 6633.517, 564.82446), (-24.70177882227215, -135.54678249834208, -17.85394074147073), (1.0, 1.0, 1.0), "SM_Cliff_442", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (6254.387, 12054.634, 1288.4839), (-9.32434122623277, 45.235704620673104, -3.254608239751036), (2.497819, 2.497819, 2.497819), "SM_Cliff_459", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (9915.856, 5875.994, 338.55725), (-84.34662117013661, 114.19794722129541, -66.31869191051358), (1.532898, 1.7929263, 1.8348464), "SM_Cliff_464", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (9889.803, 5875.1875, 299.25), (15.318701904628291, -69.7612350961538, 12.443494798879625), (1.3025904, 1.3025904, 1.3025904), "SM_Cliff_478", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5366.78, 7451.9272, 419.94104), (0.0, 134.9999263430944, -0.0), (0.82447064, 0.82447064, 0.82447064), "SM_Cliff_483", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (11976.131, 3974.6594, 629.2357), (6.397368305311186e-06, -6.980071799927175, 90.00000273318808), (2.2427297, 1.4876469, 1.7853514), "SM_Cliff_487", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (9761.826, 7001.1987, 616.9629), (0.0, 114.73876022823882, -0.0), (0.6900773, 0.6900773, 0.6900773), "SM_Cliff_497", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (9280.974, 4815.365, 419.02722), (-2.3300477217684943, -15.602384989819798, -85.57434986375128), (1.5172464, 1.4784067, 1.9250768), "SM_Cliff_498", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (9940.817, 8822.734, 739.4023), (-2.067169047713061, 30.345918488353337, 5.6208958396391475), (1.0, 1.0, 1.0), "SM_Cliff_500", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (10884.4375, 7794.1235, 572.6205), (1.6346673508367437, -23.326600032218728, -93.13534830242902), (0.51428133, 0.51428133, 0.51428133), "SM_Cliff_509", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (10475.223, 6773.3716, 583.86755), (-77.55118554529922, 40.36092900088472, 109.78394525424164), (0.28542608, 0.28542608, 0.28542608), "SM_Cliff_524", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (10201.103, 5507.15, 602.1679), (-9.633910447094875, 98.12428783958758, 8.704327290659894), (1.0, 1.0, 1.0), "SM_Cliff_533", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (10408.803, 6507.619, 585.82434), (-1.646890399044672e-07, -141.6465172321934, 10.060070329139007), (0.6213149, 0.6213149, 0.6213149), "SM_Cliff_542", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (11291.977, 9005.316, 617.34033), (-15.448914197840379, 118.38753086286464, -13.975769038401697), (0.41664767, 0.41664767, 0.41664767), "SM_Cliff_547", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (10572.95, 6541.8477, 578.2276), (83.76499980311476, 1.9643399035243346e-05, 76.48563863251952), (0.312426, 0.642972, 0.409832), "SM_Cliff_551", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (6160.7363, 10807.261, 721.8034), (-20.497556854631874, 65.22656710816416, -0.7611392801781898), (1.248111, 1.4285748, 1.1536558), "SM_Cliff_557", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (10722.106, 4285.6123, 1172.477), (-24.788697397775863, 1.3937932615487631e-06, -3.072113237395072), (2.1381936, 2.1381936, 2.1381936), "SM_Cliff_570", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (9570.325, 6602.002, 545.12854), (80.21780792153493, -179.9999889709133, 169.11759727118962), (0.5301448, 0.5301448, 0.5301448), "SM_Cliff_571", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4195.9707, 11756.775, 1194.4152), (-7.259674029708681, 65.56211779019442, -0.04486068218429972), (1.7652414, 2.1871393, 2.5291245), "SM_Cliff_573", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (11534.3955, 8169.9634, 531.0006), (-80.1906829820592, 135.57090926136792, -54.77688052497413), (1.0543317, 2.852944, 1.5862685), "SM_Cliff_583", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (9743.679, 6226.5317, 523.8947), (-60.867669228315826, 32.028980540935486, -8.514924279494176), (0.285426, 0.285426, 0.285426), "SM_Cliff_584", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (6690.6704, 12713.45, 850.59674), (-7.645536900626284, 134.435961263857, 2.5303863557943247), (2.1485746, 2.1485746, 1.7818375), "SM_Cliff_587", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (9704.985, 10073.102, 607.16174), (-9.846557214427746, -1.7537839857363273, 10.151219931389816), (1.0, 1.0, 1.0), "SM_Cliff_593", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5572.8613, 9768.436, 422.2421), (4.677538910304982, -175.0322466826041, 11.47491955935986), (1.1183044, 1.0, 1.0), "SM_Cliff_599", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (9441.205, 5901.3657, 379.17538), (72.70083499659513, -155.68638261087222, -13.682207844239768), (0.49234393, 0.49234393, 0.49234393), "SM_Cliff_602", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4190.7373, 15620.501, 1069.6748), (-8.281584203631551, -6.627349668152498, -8.153198156115204), (1.10585, 1.98503, 1.709701), "SM_Cliff_604", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (9688.696, 8969.335, 435.12146), (-5.517761136248216, -14.086242174490277, -74.8673154011189), (1.0364413, 1.8395907, 0.4549233), "SM_Cliff_606", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (8604.357, 5082.0713, 242.34161), (-79.90484676317165, 109.96466864362914, 124.99017097798978), (0.40699744, 0.55180496, 0.55180496), "SM_Cliff_607", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (11054.55, 11143.58, 763.1696), (0.0, -45.000056798727684, 0.0), (0.6930795, 0.6930795, 0.56259394), "SM_Cliff_616", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (8732.95, 5971.799, 317.22733), (-0.8899531579971174, 86.2744276182738, 16.14440728361628), (1.0, 1.0, 1.0), "SM_Cliff_632", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3748.95, 15858.772, 1267.6228), (-25.490996449314586, 127.88062037470391, -14.470883710282441), (2.241335, 2.028851, 2.377477), "SM_Cliff_633", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4526.295, 16293.102, 795.7005), (-20.44940356234826, 74.34999709310011, 9.245444578552904), (2.475886, 2.755375, 2.367485), "SM_Cliff_641", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (8387.824, 5817.4697, 270.03406), (-2.206522333699373e-09, 3.5117126817301485, 11.185642998134739), (1.0, 1.0, 1.0), "SM_Cliff_642", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (9312.265, 8774.168, 127.337166), (-10.591555709406341, 53.57566787455387, -100.82927605329735), (1.0, 1.0, 1.0), "SM_Cliff_643", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (6056.085, 9604.856, 234.38751), (6.929916740633022e-08, 119.94270549657443, 6.52737891092464), (1.0, 1.0, 1.0), "SM_Cliff_649", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3988.4817, 5041.5684, 524.30475), (13.457928795411554, -178.29875531430315, 22.631667625607598), (1.5695941, 1.5695941, 1.5695941), "SM_Cliff_659", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (9583.813, 8949.161, 515.3593), (-9.999938844678507, 2.882592463118688e-06, 2.3841855439550722e-05), (1.0, 1.0, 1.0), "SM_Cliff_660", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (7118.1143, 10134.629, 65.78421), (-17.184112274359304, -140.37051007335816, -86.07906981905903), (0.7327586, 0.7327586, 0.7327586), "SM_Cliff_664", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3780.3503, 4961.118, 475.34747), (4.889656086412491, 178.21090212318973, 26.440430250690167), (2.12291, 2.12291, 2.472886), "SM_Cliff_667", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3109.877, 5175.521, 67.21246), (-19.290925137069507, -24.6182244024321, -8.950988764952243), (2.1161697, 3.194019, 2.734157), "SM_Cliff_672", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3648.9568, 6783.7925, 560.23724), (-11.578643080362983, 112.39136942255307, 9.314827265356854), (1.0, 1.0, 1.3730289), "SM_Cliff_681", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (9269.587, 9148.492, 257.61206), (-11.252195856641803, -10.696075914628656, 87.86293588949538), (1.036441, 1.839591, 0.454923), "SM_Cliff_689", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3384.6887, 6738.5815, 573.1269), (-5.8030081835118565, 71.24809729904896, 11.964857080813598), (1.0, 1.0, 1.2727652), "SM_Cliff_698", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (8180.0146, 10673.963, 129.58751), (-1.3829047242473078, -12.140990124384523, 87.29029155979795), (0.84349793, 0.4745197, 0.71837795), "SM_Cliff_712", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4614.3647, 1828.1206, 1935.154), (-21.403137843859906, 6.898566902841613e-07, 8.033786649941783), (1.9389532, 1.9389532, 2.4844062), "SM_Cliff_725", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (6207.8066, 9693.752, 147.05724), (87.50570200820407, -0.00191104924925023, -149.8527088625496), (0.6395232, 0.6395232, 0.5382713), "SM_Cliff_726", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (7281.76, 10127.55, 61.147575), (0.4966707404954544, 27.94677383150355, 80.64939167370775), (0.91381645, 0.6735024, 0.6735024), "SM_Cliff_727", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4950.1904, 9639.9795, -95.903), (67.62495204233544, 119.8727906000713, -56.8983161303617), (1.3204707, 1.3204707, 1.3204707), "SM_Cliff_730", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4282.796, 1709.6348, 1929.628), (-10.457822937527645, -64.62612405685917, 17.713437926693924), (1.9108105, 1.9108105, 1.9108105), "SM_Cliff_736", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4843.769, 8024.9077, 80.95947), (70.47687124253888, -91.15922442467361, -79.78151574828267), (1.5005498, 1.5005498, 1.5005498), "SM_Cliff_737", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4220.6606, 3668.2373, 799.8882), (17.523668147204102, 159.6037987845193, 12.936955628769692), (2.753142, 2.753142, 2.753142), "SM_Cliff_739", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3711.876, 7784.4233, 202.19067), (-4.48538158485623, -3.4259640182078472, 12.36978254294561), (1.4174905, 1.4174905, 1.3527279), "SM_Cliff_748", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5839.1597, 9545.877, 449.04288), (-7.995144854480234e-08, -147.23157008851285, 5.366368536101721), (1.0, 1.0, 1.0), "SM_Cliff_753", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (6277.028, 4746.9326, 223.12213), (-1.9734311000587324e-08, 174.6862859814593, 16.640993397785692), (1.4403143, 1.4403143, 1.4403143), "SM_Cliff_754", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (7279.751, 10341.791, 171.28032), (-1.9274292930944354, 89.25026380488536, 3.9231489316007835), (0.62308955, 0.62308955, 0.62308955), "SM_Cliff_758", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5793.021, 9804.66, 387.5456), (61.06773657780722, 26.980291472053317, 9.794028402044328), (0.652904, 0.652904, 0.652904), "SM_Cliff_774", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2697.9617, 7534.709, 502.20877), (-2.79629558158176, 70.1470511520065, -6.012573092764534), (1.5528439, 3.443551, 1.938679), "SM_Cliff_781", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (8976.744, 12868.509, 667.0758), (-25.303312380039166, 106.89938684149986, -4.7996233982611525), (1.2074422, 1.2074422, 1.2074422), "SM_Cliff_797", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (6633.903, 11302.505, 250.25703), (-11.179321950864148, 158.08493301085045, -74.85186148416172), (1.4086254, 1.2506216, 1.2402697), "SM_Cliff_809", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (9614.655, 4306.6665, 1482.1852), (4.583049968274118, -27.65728707272521, -75.64850516484854), (1.0, 1.0, 1.0), "SM_Cliff_810", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (9664.989, 11287.761, 648.23114), (0.0, 125.59145809348023, -0.0), (0.8397034, 0.7381926, 0.8397034), "SM_Cliff_819", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (8345.311, 10692.019, 84.568146), (-7.96139524792512, 0.0, -0.0), (1.0, 1.0, 1.0), "SM_Cliff_821", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3978.8442, 4667.534, 337.9475), (17.523666995618225, 149.16850512569928, 9.261743817874935), (2.3034012, 2.3034012, 2.3034012), "SM_Cliff_828", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (9563.162, 11465.348, 637.2855), (-10.015775916998395, -105.16222125228798, 18.25047414347181), (0.64293545, 0.64293545, 0.64293545), "SM_Cliff_845", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (9697.787, 7360.872, 639.7638), (-1.9746090748388796, -119.69745213792008, 7.829053232855202), (0.6317613, 0.6317613, 0.6317613), "SM_Cliff_846", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (10004.248, 10296.885, 691.53357), (-5.28991345506019e-10, 175.06632814723037, 7.139573432663633), (0.75084025, 0.75084025, 0.75084025), "SM_Cliff_855", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3836.1084, 4391.824, 404.76767), (-0.1382448963198776, -4.980468198143276, 80.35726303680413), (0.7947829, 0.7947829, 0.7947829), "SM_Cliff_856", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (10188.709, 10181.851, 617.3315), (-1.387725648727293, 109.29736373942397, 9.602352119783896), (0.4352917, 0.5258751, 0.66521865), "SM_Cliff_894", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2931.9656, 7682.655, 448.30493), (-19.064455367904674, 95.28964826645255, -20.478579746206698), (2.2997322, 2.5864267, 1.8309774), "SM_Cliff_959", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (11448.663, 10752.72, 669.66327), (-14.328062579679825, 0.0, -0.0), (1.0, 1.0, 1.0), "SM_Cliff_1000", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (7592.401, 4749.7007, 104.69205), (-0.6661381928342294, -35.680634347660266, -65.04410271160476), (0.9025603, 1.0249369, 0.58111274), "SM_Cliff_1009", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (8932.426, 8931.179, 255.66217), (-22.756865965669853, -25.074555200463926, 6.699962967777259), (0.7891512, 0.7891512, 0.7891512), "SM_Cliff_1010", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3396.948, 7995.313, 476.71738), (18.148507099402902, -28.357484044016427, -170.69523807415706), (1.0, 1.0, 1.0), "SM_Cliff_1011", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2033.1165, 9746.792, 1214.0963), (-13.146604977341248, -179.10987377591402, 171.1380740038558), (1.7461469, 1.7461469, 2.307819), "SM_Cliff_1020", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (7137.5586, 11172.49, 96.56313), (-2.779724868260322, 165.28124942448355, 9.627039508342722), (1.0, 1.0, 1.0), "SM_Cliff_1024", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5370.5034, 9432.393, 436.49817), (-14.294310597897026, -54.4627929592711, 16.818978959887907), (1.0, 1.0, 1.0), "SM_Cliff_1038", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5423.8755, 9512.668, 616.71606), (3.532407099002689, 164.48901566343196, 1.848755057507825e-06), (1.0, 1.0, 1.0), "SM_Cliff_1044", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (6409.826, 8677.132, -30.156313), (-2.295989774126299, 34.186383821288636, -86.62426965168294), (1.0, 1.0, 1.0), "SM_Cliff_1047", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (10321.381, 14407.0, 1366.8765), (-34.996185586440916, -128.09377235825937, 3.506863896068002e-05), (1.0, 1.985699, 0.4717655), "SM_Cliff_1048", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5566.52, 2384.7007, 1530.8474), (16.06445346493921, -126.98195194857155, 171.11463502276274), (3.194019, 3.194019, 2.734157), "SM_Cliff_1051", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (9124.496, 15030.636, 1639.6028), (-3.952179822726344, -37.5528221738379, 28.645412367568976), (2.673573, 2.369379, 1.7441058), "SM_Cliff_1064", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5669.457, 9127.628, 430.43567), (-2.8644107126294207, 23.181246952216128, 6.656415997771498), (1.0, 1.0, 1.0), "SM_Cliff_1066", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (11082.054, 11404.047, 601.23157), (1.3924265747778621, -17.846095974559805, 85.234999673051), (1.0, 0.79621565, 1.0), "SM_Cliff_1073", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2989.033, 4320.819, 989.6289), (19.359214512347585, 163.04044963011484, -163.17161910364408), (1.5267211, 2.1688445, 2.1994245), "SM_Cliff_1075", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5748.4966, 15313.901, 383.1991), (-21.656768719195565, 100.88703718539864, -12.184845914912255), (1.0, 1.0, 0.84583694), "SM_Cliff_1078", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4290.386, 13695.63, 1841.8304), (-8.281584203631551, -6.627349668152498, -8.153198156115204), (1.1058503, 1.9850299, 1.7097011), "SM_Cliff_1081", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (6838.1265, 13329.223, 444.03943), (5.842193342759715e-07, 38.05613577005612, 91.677237052242), (1.0, 1.0, 1.0), "SM_Cliff_1082", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (10183.452, 12370.813, 523.423), (0.0, -140.52679724753347, 0.0), (0.6731237, 0.6731237, 0.6731237), "SM_Cliff_1090", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (8380.92, 18729.256, 1309.3086), (-30.694582345703196, 7.604612914169102, 7.530927453592152e-08), (1.717827, 1.717827, 1.717827), "SM_Cliff_1096", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2751.9434, 9518.14, 393.04895), (0.0, 113.87951574374257, -0.0), (2.0783029, 1.965961, 2.276399), "SM_Cliff_1105", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3134.1626, 10153.247, 646.14984), (-2.184753524065886, 105.28035397247662, 16.410188872411723), (1.942703, 1.942703, 1.78299), "SM_Cliff_1108", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5715.366, 14892.295, 444.0393), (-8.722211226192888e-07, 160.91184085913912, 91.67723587965713), (1.0, 1.0, 1.0), "SM_Cliff_1109", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (11072.606, 11987.705, 701.5423), (-21.426822218503478, 43.129950373894104, 3.1695594840925714), (0.6100443, 0.6100443, 0.6100443), "SM_Cliff_1112", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5369.4243, 11280.112, 861.90906), (-1.1807250057744694, 64.15895133748285, -5.530120698468208), (1.942703, 1.942703, 1.7829902), "SM_Cliff_1122", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (11090.298, 11052.49, 669.695), (0.570883496771841, 62.87518364701111, 89.70740723128532), (0.59572685, 0.59572685, 0.59572685), "SM_Cliff_1123", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (8360.087, 13785.45, 315.01562), (-22.62356411615263, 16.412708546372937, 12.49149919034273), (3.259577, 2.315544, 2.315544), "SM_Cliff_1125", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (6897.5977, 11764.942, 599.3028), (-7.645536976282135, 134.43596127503085, 2.5303861751825143), (1.1242099, 1.1242099, 1.3536981), "SM_Cliff_1128", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (7951.0967, 14234.44, 296.6715), (-7.316444164006792e-08, -3.4116819486302483, 91.67723259489502), (1.0, 1.0, 1.0), "SM_Cliff_1132", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (6433.8115, 12943.924, 1717.7701), (4.1448182873884925, 24.26647887847971, 169.1544190240875), (1.6642985, 1.9868464, 1.6642985), "SM_Cliff_1133", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2564.412, 10526.25, 1044.4274), (-18.483609498639492, 173.54394157767078, 17.982403026719485), (1.8769134, 1.8769134, 1.8769134), "SM_Cliff_1135", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (6292.3677, 13012.259, 669.25916), (0.0, 0.0, -8.287720345953835), (2.3464484, 2.3464484, 1.7655097), "SM_Cliff_1141", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2240.156, 10295.082, 1292.2205), (-4.22158680575529, -68.9622684776243, 162.75957623927607), (1.5734714, 1.5734714, 1.5734714), "SM_Cliff_1145", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5652.61, 7190.278, 189.05699), (4.163146238178382, 31.281100706065253, 83.1862836124324), (1.2931852, 1.0, 0.79104275), "SM_Cliff_1150", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (9744.688, 8610.787, -3.3970692), (86.22693850679097, 136.16674683923424, 178.85834039119115), (1.7206359, 2.1308346, 2.3869996), "SM_Cliff_1151", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1630.1858, 7859.3936, 350.1206), (12.095772336770146, -27.32607796144538, 19.285814967094154), (1.56579, 1.56579, 1.929859), "SM_Cliff_1162", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5863.0933, 11161.443, 888.8781), (-0.38388062962276237, 146.60001389738505, -4.463714529892559), (2.0038476, 2.0038476, 2.0038476), "SM_Cliff_1163", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5423.4473, 16169.8, 361.7068), (6.39913938247548e-07, -139.67331801404003, 91.67722988017093), (1.3697598, 1.3697598, 1.3697598), "SM_Cliff_1166", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (6445.0967, 5480.7173, 117.71602), (-8.026672739812271, 136.07248786502012, 3.0423216777367585), (0.72558147, 0.72558147, 0.72558147), "SM_Cliff_1170", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5429.4565, 13558.68, 792.964), (-4.814085903315552, -0.23318480421423005, -5.049772902341665), (2.253696, 2.253696, 1.820905), "SM_Cliff_1173", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (7035.2017, 18060.727, 335.4679), (6.487899054384295e-08, -177.71204909909594, 91.67724308297626), (1.307303, 1.307303, 1.307303), "SM_Cliff_1175", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (8620.785, 12438.998, 417.81213), (-24.63735899048232, 26.400709445533682, 20.40362581413727), (1.0, 1.0, 1.29826), "SM_Cliff_1176", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (8470.167, 13160.136, 330.50177), (-15.563656847399324, 3.534657527014393, 18.770369261042024), (1.0, 1.324281, 1.0), "SM_Cliff_1178", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (9632.217, 7314.687, 315.46194), (-1.2595215269913311, -30.420990114974845, -2.3704527307859116), (1.036441, 2.519398, 0.454923), "SM_Cliff_1181", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4583.714, 14870.779, 1055.6385), (22.473063501492074, 75.76538833140846, -1.45044042136693), (2.9791777, 1.909603, 2.4972854), "SM_Cliff_1182", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (6507.5977, 13494.942, 1589.3027), (-0.46597262905984516, 163.9404972288522, 9.513796185093003), (1.12421, 1.12421, 1.353698), "SM_Cliff_1187", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (6416.2056, 5630.703, 48.475113), (-5.3875424297618935, 163.9386270664128, 9.470095500643406), (0.79877925, 0.79877925, 0.79877925), "SM_Cliff_1189", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3233.4883, 4807.9214, 488.91772), (-63.84374956031561, 97.83612422814674, -21.29349011303961), (4.910758, 2.586427, 1.1711624), "SM_Cliff_1195", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2536.2495, 3934.3665, -55.300293), (13.546591060083193, 158.16415838851037, 179.7509910062494), (1.526721, 2.168844, 2.199425), "SM_Cliff_1198", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3779.1794, 16917.104, 1561.0898), (-7.275207691945959, 76.49145282848062, -1.3512271701792817), (2.475886, 2.198722, 2.367485), "SM_Cliff_1202", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3178.0708, 4156.285, 799.8882), (28.19000937700035, 157.8483192120129, 8.438935698030155), (1.1044419, 1.1044419, 1.1044419), "SM_Cliff_1203", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3199.7456, 4303.345, 525.562), (-28.718381863379264, -21.161283298052815, -15.905941481345238), (1.1493785, 1.1493785, 1.4491633), "SM_Cliff_1205", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5369.832, 4752.184, 396.90778), (-11.532836049954755, -67.4745171840544, 11.808476959459215), (1.0, 1.0, 1.0), "SM_Cliff_1220", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (12047.408, 14236.004, 2848.09), (-15.000182957712585, 36.810660858996386, 16.036569915197713), (1.641482, 2.9509237, 2.736877), "SM_Cliff_1224", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4402.042, 18172.348, 2982.6204), (2.7220489085355912, 76.25649547822357, -1.3418579992117483), (2.475886, 2.198722, 2.367485), "SM_Cliff_1237", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5996.061, 4641.6367, 268.63904), (-11.525849279801934, -126.92997027296624, 7.491269620704022e-06), (1.6794263, 1.6794263, 1.6794263), "SM_Cliff_1242", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (9654.72, 7245.8896, 312.1341), (5.464149194022809e-05, -99.99993835266136, 0.00018310547469403303), (0.99102664, 0.99102664, 0.99102664), "SM_Cliff_1267", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (9606.162, 7575.4575, 311.2267), (-4.528380760167906, -105.395321796741, 9.560058012683967), (1.396071, 0.9896414, 0.9896414), "SM_Cliff_1270", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3611.5361, 12356.936, 1893.1907), (-5.869507294124548, 35.36934082687704, 178.62412120673372), (0.67466396, 1.3901148, 1.0865204), "SM_Cliff_1283", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5408.51, 4986.3643, 334.87344), (8.49182423641864, -157.7293693733354, 14.372457245809539), (0.714431, 0.714431, 0.714431), "SM_Cliff_1288", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5166.7065, 14063.456, 670.40784), (-4.182922252687213, -96.31718012787927, 6.760188630709275), (1.6876336, 2.346448, 1.597595), "SM_Cliff_1296", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5246.5967, 3169.9258, 1127.3838), (-0.589294257885086, -177.45987599352463, -3.0035698634748638), (3.515403, 3.515403, 2.436095), "SM_Cliff_1299", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4613.8306, 14175.5625, 1256.3402), (-18.973541876926063, -89.19457869627436, 3.1695914693926293), (2.0293252, 2.0293252, 2.3587732), "SM_Cliff_1300", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3580.797, 18730.812, 1219.1625), (-31.069977224151906, -15.642575854470524, 18.71218177624845), (2.0764678, 2.0764678, 2.0764678), "SM_Cliff_1325", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (9875.0, 10145.0, 630.0), (1.708175769381039, 160.07015975778955, 4.699863614570453), (0.6214861, 0.6214861, 0.6214861), "SM_Cliff_1326", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4473.909, 15728.747, 978.7231), (-27.984675342018672, 95.46296508718272, 7.335780768549262), (2.475886, 2.755375, 2.367485), "SM_Cliff_1329", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3865.3481, 7273.743, 287.88333), (15.170813013751223, -21.428710605440344, 70.4715858169326), (1.0, 1.0, 1.0), "SM_Cliff_1333", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3857.424, 5675.8667, 528.2408), (-13.77075117464483, -109.63152064620373, 16.884637721947456), (1.2933247, 1.2933247, 1.2933247), "SM_Cliff_1334", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3652.6477, 5599.3003, 552.68), (-12.833526394701872, -105.96364985179981, 12.795734127681397), (1.569594, 1.7073287, 1.569594), "SM_Cliff_1337", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3951.0098, 16782.094, 850.5168), (-23.681638764491257, -33.55566361474443, 27.785583159023474), (1.926364, 1.940792, 1.9889154), "SM_Cliff_1339", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5874.4565, 13158.68, 2192.9639), (-4.814085999949388, -10.233214701285439, -5.049773201085251), (1.8239268, 1.427906, 1.1985663), "SM_Cliff_1347", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5505.6704, 12993.45, 2350.5967), (-16.635252281846686, -26.5109222342015, 7.0158892653008085), (1.6328797, 1.6328797, 1.2661418), "SM_Cliff_1350", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (6310.7446, 13688.341, 917.26105), (-2.9850463947416954, -179.82100113362824, 13.158204993502384), (2.475886, 2.198722, 2.367485), "SM_Cliff_1357", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5344.6133, 5913.3433, 342.53845), (0.0, 0.0, -0.0), (0.570172, 0.570172, 0.570172), "SM_Cliff_1359", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3938.2815, 17695.371, 1699.1051), (-0.44171071026655667, -42.52154246251237, -147.95674509964348), (2.5058095, 2.5202377, 2.5683606), "SM_Cliff_1362", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (10420.608, 6623.0464, 590.3186), (83.92705549745739, 103.79607430385522, 51.14616576452538), (0.312426, 0.642972, 0.409832), "SM_Cliff_1368", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (10066.275, 8834.336, 561.20233), (-15.70785511665605, 107.27978572487808, -9.902802672304842), (0.8587371, 0.8587371, 0.8587371), "SM_Cliff_1372", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (9821.954, 6169.0635, 565.9693), (78.1985953370968, -164.6451100306679, -174.01115132466165), (0.312426, 0.443928, 0.27350745), "SM_Cliff_1373", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (9647.847, 6061.6143, 420.47696), (69.27921292565881, -137.6856838576874, -24.791855967078728), (0.6622289, 0.642972, 0.409832), "SM_Cliff_1376", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (11305.756, 7026.777, 624.09247), (-82.03546909514365, -123.6827518891564, 150.9014554500387), (0.80250657, 2.2665336, 0.9207165), "SM_Cliff_1386", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (11550.0, 8760.0, 730.0), (4.208536628253091, -114.66570466271467, 9.079486124782353), (0.6761989, 0.6761989, 0.6761989), "SM_Cliff_1395", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (8872.821, 5268.789, 232.39447), (72.47387688422901, -177.62353271178316, -51.86403910981996), (0.5224526, 0.5224526, 0.5224526), "SM_Cliff_1402", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3966.621, 17900.809, 3516.7773), (-9.188812460086643, 81.22877946605006, -14.60757251432577), (2.6270046, 2.6270046, 2.6270046), "SM_Cliff_1406", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4132.163, 17812.654, 2394.661), (-7.275207467143773, 76.4913572760275, -16.35131868693488), (2.475886, 2.755375, 2.367485), "SM_Cliff_1408", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (6597.9985, 8805.453, -32.209362), (-2.295989774126299, 34.186383821288636, -86.62426965168294), (1.0, 1.0, 1.0), "SM_Cliff_1431", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (11639.039, 12701.554, 646.0891), (-19.800568500654762, 35.3443864326455, 11.47562340458392), (1.641482, 2.076362, 2.076362), "SM_Cliff_1438", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5917.6924, 6606.2803, 315.45706), (0.0, -154.9845023429332, 0.0), (0.71957314, 0.9022, 0.9022), "SM_Cliff_1442", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (11030.711, 8323.052, 553.69366), (-4.114013305981694, -5.357544442245131, -85.02453402217157), (1.0, 1.0, 1.0), "SM_Cliff_1451", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (8913.521, 11136.527, 578.5407), (-3.2122718386757075e-08, 1.4129559267533183, 85.80835137116885), (0.716881, 0.513046, 0.633052), "SM_Cliff_1460", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (9292.59, 11401.26, 584.4319), (5.068197640229079e-07, 10.563166980064489, 85.80837100724662), (0.6361891, 0.513046, 0.633052), "SM_Cliff_1461", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (11073.208, 7633.106, 608.5116), (-3.2099308112144196, -15.972657193569603, -86.45718609592545), (1.0, 1.0, 1.0), "SM_Cliff_1466", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (7218.8286, 10954.795, 104.46109), (-0.9893806035631947, -148.93677901052553, -90.05444474726063), (0.534536, 0.534536, 0.419877), "SM_Cliff_1478", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (7048.526, 10628.948, 123.4222), (-0.6602472876696331, 159.71169584366302, -92.36303581923046), (0.74385285, 0.74385285, 0.6291939), "SM_Cliff_1479", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (9372.473, 6607.3853, 717.2924), (9.846550419660877, 86.75381312023903, 10.15134330778126), (0.8078942, 1.0, 1.0), "SM_Cliff_1480", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (7724.35, 7670.1216, 258.61066), (0.2620593402326404, 153.84433809607967, -177.7232177084893), (0.65253574, 0.49879375, 0.19010441), "SM_Cliff_1485", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (8931.742, 6236.6924, 341.4774), (4.697769950856941, 81.71393864655734, 20.07044465927266), (1.0, 1.0, 1.0), "SM_Cliff_1491", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (8527.685, 5947.1406, 271.15085), (10.000004337514806, 0.0, -0.0), (1.0, 1.0, 1.0), "SM_Cliff_1498", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5875.9106, 3310.729, 857.54846), (15.983651622213008, -169.3568875492749, -9.333372560790675), (3.194019, 3.194019, 2.734157), "SM_Cliff_1504", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (8673.052, 6737.1636, 404.87244), (-10.000001357214755, -164.999782374004, 2.0143351502217515e-07), (1.3305509, 1.7382525, 1.3305509), "SM_Cliff_1505", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (11856.859, 6345.489, 666.8479), (-5.000000000253746, 0.0, -0.0), (1.910551, 1.910551, 1.910551), "SM_Cliff_1508", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (9699.282, 7084.1025, 545.25653), (-23.940463731656987, -129.89293975597823, 1.1951058247564326), (1.0, 0.90852517, 1.0), "SM_Cliff_1510", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (9895.357, 5890.99, 1003.22675), (-9.846619544872697, -169.84891253623175, -1.7537232315340783), (1.0, 1.0, 1.2416837), "SM_Cliff_1517", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (10259.568, 8825.615, 554.95355), (-2.5758961134446574, 14.78258832310221, -90.3341010686824), (0.6715434, 0.7967517, 0.5075563), "SM_Cliff_1528", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (8303.709, 6587.0024, 1237.2518), (3.3001535505125843, -58.2328116363665, 163.79393876081176), (1.0, 0.83121437, 1.0), "SM_Cliff_1531", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3470.7876, 9750.011, 506.26483), (-9.999970740365814, 134.99999901745755, 10.000111798038743), (1.3237023, 1.3237023, 1.3237023), "SM_Cliff_1541", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5002.4873, 18245.031, 757.4267), (22.635672347595435, 118.97811015883521, -34.79721403575852), (2.500383, 2.0479896, 1.9482459), "SM_Cliff_1542", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3188.2317, 9439.235, 273.28918), (-0.6526189852456329, 92.14511536498613, 11.758072188032225), (1.2641817, 1.9772115, 1.4546299), "SM_Cliff_1548", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4575.073, 18307.365, 1145.8193), (-19.181335646919557, 5.8165538547678635, 3.958196959011862), (3.0183904, 3.0183904, 3.7240245), "SM_Cliff_1550", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (8097.5947, 6367.8115, 1434.016), (0.0, 0.0, -0.0), (1.0, 1.0, 0.78703636), "SM_Cliff_1562", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4817.843, 3366.8027, 501.61417), (-1.66384917871629, -151.7483995228825, 15.688325956908262), (2.4289157, 2.4289157, 2.0459785), "SM_Cliff_1569", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (11631.819, 10269.823, 581.20575), (84.99996523582185, -9.050956503155258e-05, -15.000120566463998), (0.6209633, 0.6209633, 0.6209633), "SM_Cliff_1572", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (9530.622, 9103.365, 232.72061), (-5.517761136248216, -14.086242174490277, -74.8673154011189), (1.036441, 1.839591, 0.454923), "SM_Cliff_1583", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (6798.919, 18835.068, 454.94135), (-80.82714050877297, 23.228513304706652, 8.808991374060894e-05), (1.0, 1.0, 0.5596089), "SM_Cliff_1605", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5635.947, 18755.658, 911.0647), (0.0, 0.0, -0.0), (1.0, 1.0, 0.6888485), "SM_Cliff_1616", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (6838.1265, 13775.95, 444.03943), (-1.2652025499159592e-09, -179.88760241227746, 91.67723628515967), (1.0, 1.0, 1.0), "SM_Cliff_1620", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5879.982, 15294.097, 444.04285), (-1.2652025499159592e-09, -179.88760241227746, 91.67723628515967), (1.0, 1.0, 1.0), "SM_Cliff_1624", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (7487.262, 12654.557, 540.98145), (-1.1976930988558971, 65.79949853470184, 91.66016853809134), (1.0, 1.0, 0.60869014), "SM_Cliff_1626", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5625.689, 15693.621, 444.03943), (1.0936970170788366e-06, -153.71619636749793, 91.67723342249008), (1.520797, 1.0, 1.0), "SM_Cliff_1632", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5558.778, 16901.71, 368.43152), (-2.716726830496937e-07, 166.89593830438926, 91.67724655410215), (1.3340411, 1.3340411, 1.3340411), "SM_Cliff_1634", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5715.366, 17447.664, 335.4701), (-8.722211226192888e-07, 160.91184085913912, 91.67723587965713), (1.3073028, 1.3073028, 1.3073028), "SM_Cliff_1635", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5783.643, 18152.766, 757.2889), (-19.016022010986482, 37.25024952230663, -13.91610597250048), (1.6313746, 1.6313746, 0.75172365), "SM_Cliff_1636", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (7723.2803, 6096.8164, 104.69205), (-9.037016210353531, -31.088252690269048, -76.37255362872611), (0.90256, 0.7607647, 0.581113), "SM_Cliff_1638", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (6382.345, 18955.86, 476.13873), (-8.872125478395665e-08, -38.5116249667233, 75.41697319842417), (1.0, 1.0, 0.67331266), "SM_Cliff_1646", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2903.1082, 10140.592, 396.83606), (-5.53399564016658, 116.7078085975907, 10.410356795941196), (2.1072433, 2.1072433, 2.1072433), "SM_Cliff_1668", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (7420.201, 7541.4463, 78.97449), (0.0, -29.41375300829116, 0.0), (1.0, 1.0, 1.0), "SM_Cliff_1683", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1889.5898, 9975.97, 800.59296), (-7.187348395615191, 92.98091530750307, 6.376534483576837), (1.9001894, 1.9001894, 1.9001894), "SM_Cliff_1696", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (9435.342, 8915.339, 116.71728), (-19.261413787312616, -3.852081159646667, 14.875214317679266), (1.2181541, 1.3166361, 1.1572315), "SM_Cliff_1701", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (8963.538, 13478.894, 876.8657), (-25.304076306661397, 83.9207740576772, -12.576630543493307), (1.5148706, 1.5148706, 1.827056), "SM_Cliff_1706", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (6384.591, 11490.747, 613.95325), (11.167174801507874, 53.93585529529895, -162.54607221057393), (1.664299, 1.986846, 1.7770622), "SM_Cliff_1744", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5184.4287, 2711.5398, 1862.2815), (-27.16067222693279, 1.6432941546050062, -7.685760644946562), (1.6455443, 1.6455443, 2.2824519), "SM_Cliff_1754", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4605.1333, 2231.9817, 1641.106), (-15.649412576443813, 0.0, -0.0), (2.7542524, 2.7542524, 2.7542524), "SM_Cliff_1762", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5587.1772, 3408.9487, 1287.7135), (4.8896541592614495, 178.21090207521618, 5.307866421431314), (2.12291, 2.12291, 2.4728856), "SM_Cliff_1769", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4650.0, 3650.0, 600.0), (-9.846526860952288, -1.7537841440932482, -19.848967889641415), (2.104823, 2.104823, 2.249353), "SM_Cliff_1803", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3525.6802, 3387.6062, 1162.7112), (-19.841646768952465, -6.837037380486742, -19.52523911696344), (2.104823, 2.104823, 2.404608), "SM_Cliff_1818", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3499.106, 3879.4634, 857.55164), (-19.290984085901954, -24.618498204332184, -15.915465108319495), (3.1940186, 3.1940186, 2.734157), "SM_Cliff_1822", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (8541.638, 11630.464, 417.81213), (-24.637385767774948, -0.4772640479110582, 20.40362457559818), (1.0, 1.0, 1.2982599), "SM_Cliff_1837", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (8670.167, 11510.136, 480.50177), (-15.563656847399324, 3.534657527014393, 18.770369261042024), (1.0, 1.3242809, 1.0), "SM_Cliff_1844", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (8665.07, 11090.055, 323.4862), (29.999816345856953, -179.99998474121105, -179.99998474121105), (1.0, 1.3156921, 1.2451229), "SM_Cliff_1854", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3250.0, 7500.0, 650.0), (-15.00000061289354, 4.775578392180702e-08, 30.00006686196887), (1.0, 1.0, 1.0), "SM_Cliff_2076", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3350.0, 7350.0, 650.0), (0.0, 0.0, -149.99992628954172), (1.0, 1.0, 1.0), "SM_Cliff_2087", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3150.0, 6850.0, 563.39746), (0.0, 0.0, 30.000030034276726), (1.0, 1.0, 1.0), "SM_Cliff_2097", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3689.943, 7485.05, 429.16238), (-19.999937277239372, 85.00008859228389, 10.000059628506579), (1.0, 1.0, 1.0), "SM_Cliff_2108", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4858.4883, 14797.145, 1117.2803), (12.719184289110306, 76.01793049744659, -1.3740537417889171), (2.4758863, 2.1987221, 2.3674846), "SM_Cliff_2131", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4804.883, 17912.23, 1247.3923), (-36.72781920554232, 29.5931185669806, 2.8967511430722914), (2.6209404, 2.6209404, 2.6209404), "SM_Cliff_2139", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4464.98, 17216.705, 1158.2257), (-17.217833326428558, -9.976836088306346, 30.721832641297596), (2.2286863, 2.2286863, 2.0004637), "SM_Cliff_2146", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5090.0874, 17547.396, 1292.0947), (-16.31338605163792, 88.09754082430968, -27.013702942893925), (1.5780044, 1.5780044, 1.5780044), "SM_Cliff_2176", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (9516.042, 4961.171, 793.6998), (-81.98010233685524, 0.0, -0.0), (0.8286704, 1.0, 0.41265026), "SM_Cliff_2229", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (11297.096, 11699.998, 549.9998), (3.920533033143412e-12, 0.00013861941283537947, -88.70459466492999), (1.530782, 1.0, 1.4993201), "SM_Cliff_2288", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2643.5537, 17780.424, 996.33813), (12.389554947851238, 124.24886812241616, -18.601684304751416), (4.750005, 4.750005, 4.5576324), "SM_Cliff_2319", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (8955.699, 6770.139, 250.16264), (-4.8022663886305384e-12, -99.99993835273585, 0.0001831054864364465), (1.2909334, 1.2909334, 1.2909334), "SM_Cliff_01_1584", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3747.676, 11618.273, 751.43665), (-14.8703305288355, 1.0488333567712087, 1.2097741739590047), (1.4423587, 1.4423587, 1.8888597), "SM_Cliff_03_1116", _folder)
if a: placed += 1
else: skipped += 1

# Batch 169: StaticMesh'SM_Cliff_03' (2 instances)
_mesh_path = "/Game/Unshippable/ThirdParty/Lordenfel/Environment/Rocks/SM_Cliff_03"
_materials = ['/Game/Unshippable/ThirdParty/Lordenfel/Environment/Materials/MI_Lordenfel_Rock_Cliff_03']
_folder = "Reconstruction/BD_BB_Outdoor_TradingPost/Meshes"
a = spawn_static_mesh(_mesh_path, _materials, (3290.8271, 2251.329, 382.76697), (0.8671669975550289, 20.03724128359705, -85.07561856430986), (1.2607139, 1.2607139, 1.2607139), "SM_Cliff_335", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3763.6995, 18709.562, 826.84766), (-18.459015064077743, 46.0508444135557, -18.765320969853963), (1.9259135, 2.37169, 1.9806243), "SM_Cliff_558", _folder)
if a: placed += 1
else: skipped += 1

# Batch 170: StaticMesh'SM_Rock_01' (1 instances)
_mesh_path = "/Game/Unshippable/ThirdParty/Lordenfel/Environment/Rocks/SM_Rock_01"
_materials = ['/Game/Unshippable/ThirdParty/Lordenfel/Environment/Materials/MI_Lordenfel_Red_Rock_Lrg_01']
_folder = "Reconstruction/BD_BB_Outdoor_TradingPost/Meshes"
a = spawn_static_mesh(_mesh_path, _materials, (8511.426, 5241.6973, 249.0699), (71.0065676596446, -59.187588905244475, -57.758181433515524), (0.22032426, 0.26828852, 0.10695752), "SM_Rock_636", _folder)
if a: placed += 1
else: skipped += 1

# Batch 171: StaticMesh'SM_Rock_01' (33 instances)
_mesh_path = "/Game/Unshippable/ThirdParty/Lordenfel/Environment/Rocks/SM_Rock_01"
_materials = ['/Game/Unshippable/ThirdParty/Lordenfel/Environment/Materials/MI_Lordenfel_RedRock_01']
_folder = "Reconstruction/BD_BB_Outdoor_TradingPost/Meshes"
a = spawn_static_mesh(_mesh_path, _materials, (7474.0146, 10150.402, 144.4035), (80.42325280655774, 65.46064981102916, 65.15544297653166), (0.11689197, 0.13449055, 0.10050171), "SM_Cliff_798", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (9990.817, 12290.012, 668.62), (0.0, 0.0, -92.81366591071546), (0.29595146, 0.30645558, 0.103524484), "SM_Rock_2", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (7375.0996, 12750.657, 307.51196), (60.044452305731504, 46.84744845879816, 123.72559334729348), (2.1498163, 1.7470828, 0.550857), "SM_Rock_11", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (7407.439, 3653.4827, 842.2439), (45.69898100842572, 140.70147033870455, -30.35944075440239), (1.804531, 1.804531, 1.185584), "SM_Rock_17", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (7636.9194, 4061.5457, 963.381), (-27.63397265556758, -27.946959902877417, -156.51849677002767), (1.804531, 1.804531, 1.185584), "SM_Rock_18", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (8020.383, 13183.763, 281.7107), (14.3337175833068, -9.85742220779255, -96.61785655202807), (1.204477, 1.204477, 0.58553), "SM_Rock_20", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (7306.332, 13053.217, 580.16406), (60.04438471139113, 79.18300945654703, 123.72563716901108), (2.149816, 1.747083, 0.550857), "SM_Rock_21", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (10187.717, 4896.763, 887.392), (42.940602199766005, 145.485836187334, -176.18435951350543), (1.0, 1.0, 0.69363165), "SM_Rock_23", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (7853.1377, 8742.6875, 184.81131), (15.390368665787914, -139.96725197824372, -14.767575126878075), (0.3656676, 0.3656676, 0.045398585), "SM_Rock_31", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (8963.362, 8325.942, 249.14722), (0.0, -135.0000537473682, 0.0), (0.29021737, 0.3043285, 0.038973086), "SM_Rock_32", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (7395.24, 10854.728, 172.39703), (0.0, -109.82453334221778, 0.0), (0.486502, 0.486502, 0.166233), "SM_Rock_33", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (8339.323, 8028.466, 255.7836), (0.0, 2.2389202913891335, -0.0), (0.3799942, 0.31985882, 0.087560326), "SM_Rock_34", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5243.484, 5176.822, 355.91684), (1.7466161048701483, 49.47530378721328, -4.220734167436884), (0.3432307, 0.28847027, 0.079263225), "SM_Rock_36", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (7614.3823, 3175.1611, 607.226), (-8.150330227429176, 77.59673234116536, 92.4957496429005), (2.3743753, 2.3743753, 2.3743753), "SM_Rock_212", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (9056.016, 8257.237, 246.25497), (5.670178955463922e-06, -58.767968748583236, -100.16806143733953), (0.5587125, 0.31008518, 0.19967397), "SM_Rock_240", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (6713.067, 3778.1995, 327.40714), (20.000007386667473, 4.9170313861568576e-05, 60.00006404078669), (3.210199, 3.210199, 1.2903335), "SM_Rock_390", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1520.0693, 8516.158, 133.0456), (-8.31085149612184, -23.66207738054541, -93.25619452736048), (1.6682187, 1.6682187, 1.2353559), "SM_Rock_405", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1682.4287, 8282.186, 525.548), (69.12664014772238, -61.17343788279191, -51.50199224805646), (1.4719871, 1.4719871, 1.1185629), "SM_Rock_411", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (10331.678, 10115.327, 621.60834), (0.0, -87.67107330363362, 0.0), (0.5606448, 0.6040531, 0.23718277), "SM_Rock_595", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (11369.531, 10368.923, 644.5405), (0.0, 0.0, -14.810060109655879), (0.37726793, 0.48590505, 0.1339711), "SM_Rock_654", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (8609.986, 9138.192, 197.2146), (0.0, -135.0000537473682, 0.0), (0.4865018, 0.4865018, 0.16623282), "SM_Rock_667", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1050.0006, 8650.0, 276.20734), (0.0, 0.0, -0.0), (1.0, 1.0, 0.7587881), "SM_Rock_1017", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (6756.637, 8753.761, 173.04526), (3.0713854375626277, -19.401580669076463, -1.0810241063000008), (1.0, 1.0, 0.83483297), "SM_Rock_1056", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (10919.078, 10721.36, 657.3364), (0.0, 0.0, -4.429351730541251), (0.29841074, 0.32274443, 0.07633295), "SM_Rock_1068", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2007.5732, 8672.815, 351.5343), (0.0, 0.0, -0.0), (2.1203518, 2.1203518, 1.3620727), "SM_Rock_1184", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5588.484, 6096.822, 355.91684), (7.0196278587769026e-06, 36.030141842678944, -21.566190507507915), (0.53657854, 0.4771148, 0.17921394), "SM_Rock_1374", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (6778.146, 18259.486, 351.9818), (84.59099770507353, -32.87856459530091, -2.0574239175155494e-05), (1.0, 1.0, 1.0), "SM_Rock_1602", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (8110.0, 12410.0, 310.0), (-85.00009741059004, 0.0, -0.0), (1.0, 1.0, 0.4593602), "SM_Rock_1621", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (6609.0234, 17967.379, 409.4234), (1.643747331564485, -34.241698688881385, 9.156467273598208e-05), (1.6678779, 1.0, 0.54531276), "SM_Rock_1622", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (6444.921, 17885.238, 649.8368), (-3.647074625474968e-07, -34.271176900603315, -106.82565457448689), (1.0, 1.0, 1.0), "SM_Rock_1639", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (7057.462, 8542.114, 194.8229), (20.259220808676393, -2.211517726597574, -96.3636660473044), (0.72529227, 0.35355818, 0.19148487), "SM_Rock_1693", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (9011.748, 4493.4707, 758.36847), (-52.939788792966034, 0.0, -0.0), (1.8045311, 1.8045311, 1.1855843), "SM_Rock_2203", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (7430.2114, 2670.2913, 215.45166), (-79.79296072356532, 149.18581524176207, -179.9999314149314), (2.2923462, 2.2923462, 2.2923462), "SM_Rock_01_240", _folder)
if a: placed += 1
else: skipped += 1

# Batch 172: StaticMesh'SM_Rock_01' (2 instances)
_mesh_path = "/Game/Unshippable/ThirdParty/Lordenfel/Environment/Rocks/SM_Rock_01"
_materials = ['/Game/Unshippable/ThirdParty/Lordenfel/Environment/Materials/MI_Lordenfel_RedRock_Cliff_01']
_folder = "Reconstruction/BD_BB_Outdoor_TradingPost/Meshes"
a = spawn_static_mesh(_mesh_path, _materials, (4069.0303, 5050.6724, 517.8944), (0.0, 0.0, 79.99996004918876), (1.0, 1.0, 1.0), "SM_Rock_52", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (7172.841, 10298.144, 166.93494), (4.082966203607293e-05, 156.0750747021582, 170.17034848108506), (1.0, 1.0, 1.0), "SM_Rock_748", _folder)
if a: placed += 1
else: skipped += 1

# Batch 173: StaticMesh'SM_Rock_Large_01' (69 instances)
_mesh_path = "/Game/Unshippable/ThirdParty/Lordenfel/Environment/Rocks/SM_Rock_Large_01"
_materials = ['/Game/Unshippable/ThirdParty/Lordenfel/Environment/Materials/MI_Lordenfel_Red_Rock_Lrg_01']
_folder = "Reconstruction/BD_BB_Outdoor_TradingPost/Meshes"
a = spawn_static_mesh(_mesh_path, _materials, (6503.861, 18262.174, 1034.9578), (13.685412348400005, -35.609379878632545, -103.72401328894179), (1.948769, 1.948769, 1.948769), "SM_Rock_Large_18", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (6471.4, 7169.7383, 16.031212), (-10.036070295587146, 176.35627140602438, 13.421009690709814), (0.6351578, 0.6351578, 0.54595464), "SM_Rock_Large_21", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (7077.2236, 4575.797, 129.10307), (-0.6394362822315767, 83.45808605180562, -21.527344350699618), (2.8994849, 1.8680073, 2.5247345), "SM_Rock_Large_25", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (6693.121, 3207.6365, 759.75977), (18.499144337492446, 0.0, -0.0), (4.186241, 2.55997, 3.216697), "SM_Rock_Large_28", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (6925.9517, 2504.8813, 326.51498), (15.43150437136483, -36.410647381782944, -54.39993476186135), (3.8691802, 3.8332603, 4.274927), "SM_Rock_Large_29", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (6908.0146, 5366.754, -23.820553), (-1.5975035384774725, 29.28739177845439, -18.047823383109105), (0.89120585, 0.89120585, 0.89120585), "SM_Rock_Large_30", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (7625.4316, 4475.4307, 379.152), (26.68219607305012, 50.69617376992879, -57.54964176154344), (0.9752555, 1.2914169, 1.3714433), "SM_Rock_Large_37", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (7016.946, 6516.3604, -121.11103), (-6.2738041186242075, -31.666263919624928, -8.292024027695003), (0.44116223, 0.44116223, 0.44116223), "SM_Rock_Large_38", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (7561.0366, 5097.137, 24.961823), (19.72424891062383, 4.6516139861229195, -3.579559219953942), (0.85933065, 0.85933065, 0.85933065), "SM_Rock_Large_40", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (7159.2026, 5204.6143, 46.537468), (45.350515342142536, -17.24612161138213, -161.54210603722908), (1.4416304, 1.4416304, 1.4416304), "SM_Rock_Large_41", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (6942.583, 5122.4917, 13.167281), (4.224137413426761, 154.95210726778072, 0.40455631537744813), (1.2023863, 1.5185484, 1.5985743), "SM_Rock_Large_43", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (9981.126, 12516.61, 672.16394), (-40.31933889560888, -89.48248546008708, 22.95668441316377), (0.539374, 0.539374, 0.539374), "SM_Rock_Large_49", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (10847.624, 10733.878, 658.0111), (0.0, 54.78744349211375, -0.0), (0.2787661, 0.2787661, 0.2787661), "SM_Rock_Large_51", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (10877.267, 10664.732, 653.1456), (-14.452634037254247, -63.108813953179485, 165.42063791648192), (0.232052, 0.232052, 0.232052), "SM_Rock_Large_55", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (10322.927, 10523.421, 653.1456), (-14.452634037254247, -63.108813953179485, 165.42063791648192), (0.232052, 0.232052, 0.232052), "SM_Rock_Large_58", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (7648.197, 8974.954, 137.6152), (-7.756531048438827, 140.9472753692892, -7.072325904411349), (0.35854712, 0.35854712, 0.35854712), "SM_Rock_Large_62", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (8223.517, 7579.0107, 252.49872), (12.219259535168364, 93.14288162864112, -172.05700059891723), (0.5728521, 0.49011132, 0.5047472), "SM_Rock_Large_63", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5669.321, 6781.9155, 361.22552), (1.968200750640293e-05, 128.88149995525927, -20.287475299922555), (0.5437239, 0.5437239, 0.5437239), "SM_Rock_Large_67", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (6426.2485, 7373.7666, 7.840019), (-10.036102301930654, -2.2779848408667744, 13.420104527832255), (0.9729235, 0.9729235, 0.53600055), "SM_Rock_Large_70", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (10495.647, 8799.857, 635.9147), (0.0, -33.6592080305926, 0.0), (0.54548115, 0.54548115, 0.54548115), "SM_Rock_Large_71", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (6587.385, 7859.306, 18.889442), (-10.036102301930654, -2.2779848408667744, 13.420104527832255), (1.3606474, 1.2594544, 0.83666646), "SM_Rock_Large_72", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (6483.634, 7702.839, -6.7973404), (-10.035949652797282, 173.74669933140547, 13.42227462018829), (0.88836116, 0.4515769, 0.31407785), "SM_Rock_Large_73", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5895.75, 7753.2437, 14.101219), (-5.669371443566476, 139.36876746153158, 0.1563425565537267), (1.360647, 1.259454, 1.143707), "SM_Rock_Large_74", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5890.8486, 8069.752, -75.465675), (8.43469596140026, -39.10703057967026, -11.19009393934093), (1.360647, 1.259454, 1.7109652), "SM_Rock_Large_75", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (6692.6875, 6329.089, 9.918594), (-5.052215593843279, 126.47976488626706, -3.725616681702102), (1.558044, 1.558044, 1.1632583), "SM_Rock_Large_76", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (6945.1465, 6914.4976, -7.4177246), (-8.765685312079425, -20.074309127778495, 1.862864588165196), (1.2718667, 1.2718667, 1.010924), "SM_Rock_Large_77", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (6851.8994, 8109.6455, 53.268097), (-9.525298598977335, 82.2173445902381, -6.046783441848501), (1.124188, 1.124188, 1.124188), "SM_Rock_Large_78", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (7228.2905, 7747.7197, 69.50888), (-16.439117603727773, -42.168975571919404, -13.634430732445825), (1.124188, 1.124188, 1.124188), "SM_Rock_Large_79", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5785.814, 7695.435, 110.925674), (-5.66934222939057, -29.935729658142318, 0.1563454235543873), (0.8173252, 0.7161322, 0.600385), "SM_Rock_Large_80", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (6570.447, 2935.89, 238.82556), (-68.7569647704247, 0.0, -0.0), (3.134383, 3.134383, 3.134383), "SM_Rock_Large_209", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (6466.604, 3853.622, 351.03888), (0.0, 0.0, -0.0), (1.0, 1.0, 1.0), "SM_Rock_Large_222", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (7506.5425, 4199.365, 5.972168), (-10.000000164519466, 0.0, -0.0), (1.767742, 1.767742, 1.767742), "SM_Rock_Large_228", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (9270.127, 12612.841, 710.5083), (-14.674316141479768, -97.273644887441, -21.775725986322676), (0.89926136, 0.89926136, 0.89926136), "SM_Rock_Large_233", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (7554.2354, 3571.8975, 33.279907), (0.0, 70.00002222525863, -0.0), (2.569838, 2.569838, 2.569838), "SM_Rock_Large_393", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (8426.999, 9001.441, 212.81055), (0.0, -179.99994535848643, 0.0), (1.0, 1.0, 1.0), "SM_Rock_Large_664", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3782.123, 10783.1045, 686.96814), (-9.999970078698405, -59.99975260908119, -9.80538943217424e-08), (1.0, 1.0, 1.0), "SM_Rock_Large_687", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (7305.112, 5000.5405, -4.0469403), (18.97188564959882, 5.6705697995469695, 3.7431374970184197), (1.24347, 1.24347, 1.24347), "SM_Rock_Large_701", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (9979.945, 10552.048, 651.81586), (-12.092803063004451, -106.56472707315542, -175.0694387301652), (0.48571214, 0.5599822, 0.5599822), "SM_Rock_Large_704", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (7091.201, 4468.6553, 394.50983), (-4.964477194487383, 6.154113599377287, -3.3819881578624402), (1.7008836, 1.7008836, 1.7008836), "SM_Rock_Large_710", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (6842.3584, 4901.795, 222.04276), (0.0, 0.0, -0.0), (1.558044, 1.558044, 1.558044), "SM_Rock_Large_719", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (7121.5405, 5898.83, -97.86397), (17.720067908002875, -1.3227540275667615, -19.193816868579013), (0.7102085, 0.7102085, 0.7102085), "SM_Rock_Large_724", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (7474.2227, 10282.394, 149.93973), (16.93627533733869, 90.80479958249278, 5.692712606552719), (0.60727006, 0.60727006, 0.60727006), "SM_Rock_Large_745", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (9673.491, 9004.192, 626.12915), (0.158098389753761, 172.57195553712063, 0.0910430032571191), (0.49054664, 0.49054664, 0.49054664), "SM_Rock_Large_765", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (10244.583, 8232.767, 635.3278), (0.0, 171.24182713309705, -0.0), (0.5549292, 0.5549292, 0.5549292), "SM_Rock_Large_770", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5833.4385, 5362.974, 366.17697), (19.30059515158401, -170.17330451121884, 11.239078724383287), (0.5885349, 0.5885349, 0.5885349), "SM_Rock_Large_819", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (7984.916, 10892.743, 188.46597), (-1.4227905684103224, 118.12745399613944, 4.712726987472768), (0.44153336, 0.44153336, 0.44153336), "SM_Rock_Large_824", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (6983.77, 8896.203, 169.13934), (0.0, 17.59235451776744, -0.0), (0.5540438, 0.5540438, 0.5540438), "SM_Rock_Large_1059", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (11124.963, 10645.937, 664.8558), (0.26917093432064365, 171.52386445869197, 20.090535980494273), (0.81902546, 0.81902546, 0.81902546), "SM_Rock_Large_1065", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (9581.062, 11935.842, 708.21), (9.238522604328988, 97.63993314175173, -1.0253905246751052), (0.7349834, 0.7349834, 0.7349834), "SM_Rock_Large_1107", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5659.2944, 5448.531, 351.4258), (0.0, -76.11449237720613, 0.0), (0.64688504, 0.64688504, 0.64688504), "SM_Rock_Large_1168", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (6299.853, 7039.2593, 22.341484), (-16.161012496242247, -2.3354188833676868, 13.673184089247124), (1.2343998, 1.2343998, 1.2343998), "SM_Rock_Large_1230", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5138.278, 5896.2925, 340.40106), (0.0, -31.57760748340851, 0.0), (0.631473, 0.631473, 0.631473), "SM_Rock_Large_1362", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2411.2458, 8774.378, 35.384064), (-16.17111159338324, 1.691621000887493e-06, 7.854200446823495), (2.6946578, 2.6946578, 2.6946578), "SM_Rock_Large_1367", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (11331.644, 9113.859, 601.472), (-19.999996755753948, 0.0, -0.0), (1.0, 1.0, 1.0), "SM_Rock_Large_1461", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5700.0, 18900.0, 450.0), (-6.6971748382527805, 1.3407067638380012, -11.347595366271843), (3.0470293, 3.0470293, 3.0470293), "SM_Rock_Large_1599", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (6272.4966, 18300.746, 538.5779), (-4.946652354053919, -92.26558896821166, -93.38039253794487), (2.8312721, 2.8312721, 2.8312721), "SM_Rock_Large_1612", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (7580.0, 12360.0, 290.0), (0.0, -119.99990742845164, 0.0), (1.3093987, 1.3093987, 1.3093987), "SM_Rock_Large_1618", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (6716.5967, 18424.803, 602.20056), (43.17998784570638, 0.0, -0.0), (2.404237, 2.404237, 2.404237), "SM_Rock_Large_1619", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (6425.605, 17703.977, 395.40784), (0.0, -122.35932035556642, 0.0), (1.6268829, 1.6268829, 1.6268829), "SM_Rock_Large_1625", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5906.725, 17691.3, 550.5015), (64.79495463155247, 140.25870729984612, -179.99998303129948), (2.140712, 2.140712, 2.140712), "SM_Rock_Large_1632", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (6162.9517, 17941.832, 920.162), (13.6854092123936, -164.25210320385725, -103.72384928742113), (1.9487693, 1.9487693, 1.9487693), "SM_Rock_Large_1642", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4232.583, 7032.989, 384.6839), (4.999998670948895, -45.00006099337647, 5.000012895566539), (0.6839029, 0.6839029, 0.6839029), "SM_Rock_Large_1648", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (6472.4634, 18808.086, 871.82324), (0.0, 0.0, -123.08667852483502), (2.3766513, 2.3766513, 2.3766513), "SM_Rock_Large_1649", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (6825.8433, 18536.354, 940.2273), (37.604964900297006, 163.55608980868706, 154.1881597241401), (2.2278929, 1.5624675, 2.2278929), "SM_Rock_Large_1652", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (7417.7866, 7917.4272, 225.13025), (0.0, 75.91841090141891, -0.0), (0.6747562, 0.6747562, 0.6747562), "SM_Rock_Large_1686", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (6885.4507, 8259.745, 182.56815), (4.493916581098285, -36.634646564347776, -23.68594471555457), (1.1241882, 1.1241882, 1.1241882), "SM_Rock_Large_1690", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (8363.761, 3857.7124, 833.73975), (25.370103513554483, 0.0, -0.0), (4.274927, 4.274927, 4.274927), "SM_Rock_Large_2200", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (10111.071, 4780.1514, 712.16956), (-41.773075558144676, -36.44833421253804, 89.04381596009262), (1.0, 1.0, 2.4256773), "SM_Rock_Large_2226", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (8304.591, 4402.9414, 299.552), (0.0, 76.49462182574965, -0.0), (3.911142, 3.911142, 3.911142), "SM_Rock_Large_01_237", _folder)
if a: placed += 1
else: skipped += 1

# Batch 174: StaticMesh'SM_Rock_Large_01' (7 instances)
_mesh_path = "/Game/Unshippable/ThirdParty/Lordenfel/Environment/Rocks/SM_Rock_Large_01"
_materials = ['/Game/Unshippable/ThirdParty/Lordenfel/Environment/Materials/MI_Lordenfel_RedRock_01']
_folder = "Reconstruction/BD_BB_Outdoor_TradingPost/Meshes"
a = spawn_static_mesh(_mesh_path, _materials, (1500.0, 9300.0, 0.0), (-11.238433665017512, -140.96698721230504, 13.516905280690446), (1.5471491, 1.5471491, 1.5471491), "SM_Rock_Large_7", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2332.099, 9260.441, 119.34277), (0.0, 19.556175531602708, -0.0), (3.24697, 3.24697, 3.24697), "SM_Rock_Large_81", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (943.22845, 9184.589, 206.47888), (-14.99996880678797, 148.76751009227115, 4.5257942398137826e-06), (2.458399, 2.458399, 2.458399), "SM_Rock_Large_402", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1480.1406, 8835.285, 94.83826), (18.889471440632622, 137.20510842308286, -16.685391558207815), (2.2421114, 2.2421114, 2.2421114), "SM_Rock_Large_414", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (8417.857, 5193.8433, 272.7457), (-0.9862367926894697, 76.98564093265982, -4.259155410806604), (0.48575878, 0.48575878, 0.48575878), "SM_Rock_Large_633", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (10835.679, 11844.64, 666.5106), (0.0, -66.98099043652748, 0.0), (0.5477514, 0.5477514, 0.5477514), "SM_Rock_Large_1130", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1608.4199, 9181.173, 362.0077), (0.0, 70.7114203734725, -0.0), (3.2469702, 3.2469702, 3.2469702), "SM_Rock_Large_1181", _folder)
if a: placed += 1
else: skipped += 1

# Batch 175: StaticMesh'SM_Rock_Large_01' (1 instances)
_mesh_path = "/Game/Unshippable/ThirdParty/Lordenfel/Environment/Rocks/SM_Rock_Large_01"
_materials = ['/Game/Unshippable/ThirdParty/Lordenfel/Environment/Materials/MI_Lordenfel_RedRock_Cliff_01']
_folder = "Reconstruction/BD_BB_Outdoor_TradingPost/Meshes"
a = spawn_static_mesh(_mesh_path, _materials, (8496.062, 3860.7317, 1402.5743), (28.05568234893359, 6.818080147769543, -11.356475906863823), (4.186241, 2.5599701, 3.2166972), "SM_Rock_Large_24", _folder)
if a: placed += 1
else: skipped += 1

# Batch 176: StaticMesh'SM_Rock_Large_01' (1 instances)
_mesh_path = "/Game/Unshippable/ThirdParty/Lordenfel/Environment/Rocks/SM_Rock_Large_01"
_materials = ['/Game/Unshippable/ThirdParty/Lordenfel/Environment/Materials/MI_Rock_Large_01']
_folder = "Reconstruction/BD_BB_Outdoor_TradingPost/Meshes"
a = spawn_static_mesh(_mesh_path, _materials, (1950.0, 9300.0, -100.0), (0.0, 0.0, -0.0), (1.0, 1.0, 1.0), "SM_Rock_Large_1014", _folder)
if a: placed += 1
else: skipped += 1

# Batch 177: StaticMesh'SM_Rock_Medium_01' (2 instances)
_mesh_path = "/Game/Unshippable/ThirdParty/Lordenfel/Environment/Rocks/SM_Rock_Medium_01"
_materials = ['/Game/Unshippable/ThirdParty/Lordenfel/Environment/Materials/MI_Lordenfel_RedRock_01']
_folder = "Reconstruction/BD_BB_Outdoor_TradingPost/Meshes"
a = spawn_static_mesh(_mesh_path, _materials, (11579.482, 6008.0034, 811.6341), (-50.06638321668003, 46.137553818932695, 1.3254536831570552e-05), (1.0, 1.0, 1.0), "SM_Rock_Medium_20", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (7308.053, 5307.2686, -69.803406), (21.561888929091605, 21.14702178471314, 11.377044095232131), (1.0, 1.0, 1.0), "SM_Rock_Medium_01_704", _folder)
if a: placed += 1
else: skipped += 1

# Batch 178: StaticMesh'SM_Rock_Medium_01' (1 instances)
_mesh_path = "/Game/Unshippable/ThirdParty/Lordenfel/Environment/Rocks/SM_Rock_Medium_01"
_materials = ['/Game/Unshippable/ThirdParty/Lordenfel/Environment/Materials/MI_Lordenfel_RedRock_Small_01']
_folder = "Reconstruction/BD_BB_Outdoor_TradingPost/Meshes"
a = spawn_static_mesh(_mesh_path, _materials, (7728.285, 8857.885, 158.56223), (5.020530305741456, -69.55162881105748, 2.027743597378749e-07), (0.81677485, 0.81677485, 0.81677485), "SM_Rock_Medium_724", _folder)
if a: placed += 1
else: skipped += 1

# Batch 179: StaticMesh'PWM_Quarry_Floor_8x8x8_A' (1 instances)
_mesh_path = "/Game/Unshippable/Whitebox/Rocks/Meshes/PWM_Quarry_Floor_8x8x8_A"
_materials = ['/Game/Unshippable/ThirdParty/Lordenfel/Environment/Materials/MI_Lordenfel_Rock_8x8x8_Floor_A']
_folder = "Reconstruction/BD_BB_Outdoor_TradingPost/Meshes"
a = spawn_static_mesh(_mesh_path, _materials, (13318.682, 1700.4077, 1962.9485), (0.0, 0.0, -0.0), (2.4999995, 1.8401265, 2.7589643), "PWM_Quarry_Floor_8x8x8_A10", _folder)
if a: placed += 1
else: skipped += 1

# Batch 180: StaticMesh'PWM_Quarry_Floor_8x8x8_A' (13 instances)
_mesh_path = "/Game/Unshippable/Whitebox/Rocks/Meshes/PWM_Quarry_Floor_8x8x8_A"
_materials = ['/Game/Unshippable/ThirdParty/Lordenfel/Environment/Materials/MI_Lordenfel_Rock_8x8x8_RedFloor_A']
_folder = "Reconstruction/BD_BB_Outdoor_TradingPost/Meshes"
a = spawn_static_mesh(_mesh_path, _materials, (12646.907, 11349.999, 2330.0), (0.0, 0.0, -0.0), (0.2458017, 1.5, 2.8987713), "PWM_Quarry_Floor_8x8x8_A_10", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (12625.714, 9610.022, 2631.2903), (0.0, 0.0, -0.0), (0.401973, 0.5311799, 0.401973), "PWM_Quarry_Floor_8x8x8_A11", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (12625.714, 9161.705, 2631.2903), (0.0, 0.0, -0.0), (0.401973, 0.53118, 0.401973), "PWM_Quarry_Floor_8x8x8_A12", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (12703.956, 10465.242, 2979.977), (0.0, -90.19035777675012, 0.0), (2.4999995, 0.27638945, 1.4999467), "PWM_Quarry_Floor_8x8x8_A14", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (12703.569, 8949.887, 3229.9883), (0.0, -89.99975996369572, 0.0), (2.4999995, 0.27638945, 0.9887638), "PWM_Quarry_Floor_8x8x8_A15", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (12625.714, 10045.896, 2631.2903), (0.0, 0.0, -0.0), (0.40197274, 0.40197274, 0.40197274), "PWM_Quarry_Floor_8x8x8_A2_2", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (12655.663, 9650.0, 1746.4456), (0.0, 0.0, -0.0), (0.16104977, 2.4999995, 3.2310226), "PWM_Quarry_Floor_8x8x8_A3", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (12646.907, 7950.0195, 2380.0), (0.0, 0.0, -0.0), (0.2458017, 1.5, 2.8203428), "PWM_Quarry_Floor_8x8x8_A4", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (13268.7, 6250.37, 1877.4851), (0.0, 1.9722598314207571, -0.0), (2.4999995, 3.0668774, 3.8151047), "PWM_Quarry_Floor_8x8x8_A5", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (12640.493, 12638.922, 1831.2522), (0.0, -89.99975996369572, 0.0), (2.9914532, 0.36543736, 3.9337418), "PWM_Quarry_Floor_8x8x8_A6", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (12637.981, 14699.652, 1868.428), (0.0, -89.999630318475, 0.0), (2.4999995, 0.36543736, 3.9337418), "PWM_Quarry_Floor_8x8x8_A7", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (12635.573, 17049.77, 1899.3145), (0.0, -179.9998224150775, 0.0), (0.37549067, 3.066877, 3.0907483), "PWM_Quarry_Floor_8x8x8_A8", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (13517.842, 3652.8818, 1877.4851), (0.0, 90.40819555631799, -0.0), (3.514276, 3.066877, 3.8151047), "PWM_Quarry_Floor_8x8x8_A9", _folder)
if a: placed += 1
else: skipped += 1

# Batch 181: StaticMesh'PWM_Quarry_Floor_8x8x8_A' (1 instances)
_mesh_path = "/Game/Unshippable/Whitebox/Rocks/Meshes/PWM_Quarry_Floor_8x8x8_A"
_materials = ['/Game/Environments/ProcTexturing/ProcMaterial_Quarry_Atlas_6']
_folder = "Reconstruction/BD_BB_Outdoor_TradingPost/Meshes"
a = spawn_static_mesh(_mesh_path, _materials, (3950.0, 4250.0, 100.0), (0.0, 0.0, -0.0), (0.29080206, 1.1166373, 1.0), "PWM_Quarry_Floor_8x8x8_A19", _folder)
if a: placed += 1
else: skipped += 1

# ======================================================================
# PHASE 2: ConstructionCatalog  (construction blocks)
# ======================================================================
unreal.log(f"[{BUBBLE_NAME}] Phase 2: Placing construction blocks...")

# Construction blocks use DecoVolume transforms (matched by Name)
_folder = "Reconstruction/BD_BB_Outdoor_TradingPost/Construction"

# Construction: AB_Mines_Scaffolding_Beam_3m_2
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Scaffolding
#   Volume: EMorSimpleShape::Empty, BoxExtent: (100.0, 100.0, 100.0)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (11250.0, 11350.0, 1600.0), (0.0, 0.0, -0.0), (2.0000, 2.0000, 2.0000), "AB_Mines_Scaffolding_Beam_3m_2", _folder)
if a: placed += 1
else: skipped += 1

# Construction: AB_Mines_Scaffolding_Beam_3m2
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Scaffolding
#   Volume: EMorSimpleShape::Empty, BoxExtent: (100.0, 100.0, 100.0)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (11250.0, 11650.0, 1600.0), (0.0, 0.0, -0.0), (2.0000, 2.0000, 2.0000), "AB_Mines_Scaffolding_Beam_3m2", _folder)
if a: placed += 1
else: skipped += 1

# Construction: AB_Mines_Scaffolding_Foundation_3x1m5
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Scaffolding
#   Volume: EMorSimpleShape::Empty, BoxExtent: (100.0, 100.0, 100.0)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (11350.0, 12000.0, 800.0), (0.0, 0.0, -0.0), (2.0000, 2.0000, 2.0000), "AB_Mines_Scaffolding_Foundation_3x1m5", _folder)
if a: placed += 1
else: skipped += 1

# Construction: AB_Mines_Scaffolding_Foundation_3x1m6_12
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Scaffolding
#   Volume: EMorSimpleShape::Empty, BoxExtent: (100.0, 100.0, 100.0)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (11350.0, 11150.0, 1100.0), (-0.0, -89.99999818714215, -0.0), (2.0000, 2.0000, 2.0000), "AB_Mines_Scaffolding_Foundation_3x1m6_12", _folder)
if a: placed += 1
else: skipped += 1

# Construction: AB_Mines_Scaffolding_Foundation_3x1m7
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Scaffolding
#   Volume: EMorSimpleShape::Empty, BoxExtent: (100.0, 100.0, 100.0)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (11350.0, 11050.0, 1100.0), (-0.0, -89.99999818714215, -0.0), (2.0000, 2.0000, 2.0000), "AB_Mines_Scaffolding_Foundation_3x1m7", _folder)
if a: placed += 1
else: skipped += 1

# Construction: AB_Mines_Scaffolding_Foundation_3x2m_2
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Scaffolding
#   Volume: EMorSimpleShape::Empty, BoxExtent: (100.0, 100.0, 100.0)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (11200.0, 7500.0, 950.0), (0.0, 0.0, -0.0), (2.0000, 2.0000, 2.0000), "AB_Mines_Scaffolding_Foundation_3x2m_2", _folder)
if a: placed += 1
else: skipped += 1

# Construction: AB_Mines_Scaffolding_Foundation_3x2m2
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Scaffolding
#   Volume: EMorSimpleShape::Empty, BoxExtent: (100.0, 100.0, 100.0)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (11200.0, 7250.0, 950.0), (0.0, 0.0, -0.0), (2.0000, 2.0000, 2.0000), "AB_Mines_Scaffolding_Foundation_3x2m2", _folder)
if a: placed += 1
else: skipped += 1

# Construction: AB_Mines_Scaffolding_Foundation_3x2m3
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Scaffolding
#   Volume: EMorSimpleShape::Empty, BoxExtent: (100.0, 100.0, 100.0)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (11200.0, 6950.0, 950.0), (0.0, 0.0, -0.0), (2.0000, 2.0000, 2.0000), "AB_Mines_Scaffolding_Foundation_3x2m3", _folder)
if a: placed += 1
else: skipped += 1

# Construction: AB_Mines_Scaffolding_Foundation_3x2m7_10
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Scaffolding
#   Volume: EMorSimpleShape::Empty, BoxExtent: (100.0, 100.0, 100.0)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (11800.0, 8400.0, 1550.0), (0.0, 0.0, -0.0), (2.0000, 2.0000, 2.0000), "AB_Mines_Scaffolding_Foundation_3x2m7_10", _folder)
if a: placed += 1
else: skipped += 1

# Construction: AB_Mines_Scaffolding_Foundation_3x2m8
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Scaffolding
#   Volume: EMorSimpleShape::Empty, BoxExtent: (100.0, 100.0, 100.0)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (11800.0, 8400.0, 1250.0), (0.0, 0.0, -0.0), (2.0000, 2.0000, 2.0000), "AB_Mines_Scaffolding_Foundation_3x2m8", _folder)
if a: placed += 1
else: skipped += 1

# Construction: AB_Mines_Scaffolding_Foundation_3x2m9
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Scaffolding
#   Volume: EMorSimpleShape::Empty, BoxExtent: (100.0, 100.0, 100.0)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (11800.0, 8400.0, 950.0), (0.0, 0.0, -0.0), (2.0000, 2.0000, 2.0000), "AB_Mines_Scaffolding_Foundation_3x2m9", _folder)
if a: placed += 1
else: skipped += 1

# Construction: AB_Mines_Scaffolding_Foundation_3x3m_5
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Scaffolding
#   Volume: EMorSimpleShape::Empty, BoxExtent: (100.0, 100.0, 100.0)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (11450.0, 11650.0, 1100.0), (0.0, 0.0, -0.0), (2.0000, 2.0000, 2.0000), "AB_Mines_Scaffolding_Foundation_3x3m_5", _folder)
if a: placed += 1
else: skipped += 1

# Construction: AB_Mines_Scaffolding_Foundation_3x3m10
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Scaffolding
#   Volume: EMorSimpleShape::Empty, BoxExtent: (100.0, 100.0, 100.0)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (11450.0, 7200.0, 1250.0), (0.0, 0.0, -0.0), (2.0000, 2.0000, 2.0000), "AB_Mines_Scaffolding_Foundation_3x3m10", _folder)
if a: placed += 1
else: skipped += 1

# Construction: AB_Mines_Scaffolding_Foundation_3x3m11
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Scaffolding
#   Volume: EMorSimpleShape::Empty, BoxExtent: (100.0, 100.0, 100.0)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (11650.0, 7500.0, 1550.0), (0.0, 0.0, -0.0), (2.0000, 2.0000, 2.0000), "AB_Mines_Scaffolding_Foundation_3x3m11", _folder)
if a: placed += 1
else: skipped += 1

# Construction: AB_Mines_Scaffolding_Foundation_3x3m12
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Scaffolding
#   Volume: EMorSimpleShape::Empty, BoxExtent: (100.0, 100.0, 100.0)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (11650.0, 11050.0, 1100.0), (0.0, 0.0, -0.0), (2.0000, 2.0000, 2.0000), "AB_Mines_Scaffolding_Foundation_3x3m12", _folder)
if a: placed += 1
else: skipped += 1

# Construction: AB_Mines_Scaffolding_Foundation_3x3m13
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Scaffolding
#   Volume: EMorSimpleShape::Empty, BoxExtent: (100.0, 100.0, 100.0)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (11950.0, 7200.0, 1550.0), (0.0, 0.0, -0.0), (2.0000, 2.0000, 2.0000), "AB_Mines_Scaffolding_Foundation_3x3m13", _folder)
if a: placed += 1
else: skipped += 1

# Construction: AB_Mines_Scaffolding_Foundation_3x3m2
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Scaffolding
#   Volume: EMorSimpleShape::Empty, BoxExtent: (100.0, 100.0, 100.0)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (11650.0, 11650.0, 1400.0), (0.0, 0.0, -0.0), (2.0000, 2.0000, 2.0000), "AB_Mines_Scaffolding_Foundation_3x3m2", _folder)
if a: placed += 1
else: skipped += 1

# Construction: AB_Mines_Scaffolding_Foundation_3x3m3
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Scaffolding
#   Volume: EMorSimpleShape::Empty, BoxExtent: (100.0, 100.0, 100.0)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (11650.0, 11350.0, 1400.0), (0.0, 0.0, -0.0), (2.0000, 2.0000, 2.0000), "AB_Mines_Scaffolding_Foundation_3x3m3", _folder)
if a: placed += 1
else: skipped += 1

# Construction: AB_Mines_Scaffolding_Foundation_3x3m4
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Scaffolding
#   Volume: EMorSimpleShape::Empty, BoxExtent: (100.0, 100.0, 100.0)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (11650.0, 11050.0, 1400.0), (0.0, 0.0, -0.0), (2.0000, 2.0000, 2.0000), "AB_Mines_Scaffolding_Foundation_3x3m4", _folder)
if a: placed += 1
else: skipped += 1

# Construction: AB_Mines_Scaffolding_Foundation_3x3m5_28
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Scaffolding
#   Volume: EMorSimpleShape::Empty, BoxExtent: (100.0, 100.0, 100.0)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (11450.0, 11350.0, 1100.0), (0.0, 0.0, -0.0), (2.0000, 2.0000, 2.0000), "AB_Mines_Scaffolding_Foundation_3x3m5_28", _folder)
if a: placed += 1
else: skipped += 1

# Construction: AB_Mines_Scaffolding_Foundation_3x3m6_33
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Scaffolding
#   Volume: EMorSimpleShape::Empty, BoxExtent: (100.0, 100.0, 100.0)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (11450.0, 7500.0, 950.0), (0.0, 0.0, -0.0), (2.0000, 2.0000, 2.0000), "AB_Mines_Scaffolding_Foundation_3x3m6_33", _folder)
if a: placed += 1
else: skipped += 1

# Construction: AB_Mines_Scaffolding_Foundation_3x3m7
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Scaffolding
#   Volume: EMorSimpleShape::Empty, BoxExtent: (100.0, 100.0, 100.0)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (11450.0, 7200.0, 950.0), (0.0, 0.0, -0.0), (2.0000, 2.0000, 2.0000), "AB_Mines_Scaffolding_Foundation_3x3m7", _folder)
if a: placed += 1
else: skipped += 1

# Construction: AB_Mines_Scaffolding_Foundation_3x3m8
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Scaffolding
#   Volume: EMorSimpleShape::Empty, BoxExtent: (100.0, 100.0, 100.0)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (11450.0, 6950.0, 950.0), (0.0, 0.0, -0.0), (2.0000, 2.0000, 2.0000), "AB_Mines_Scaffolding_Foundation_3x3m8", _folder)
if a: placed += 1
else: skipped += 1

# Construction: AB_Mines_Scaffolding_Foundation_3x3m9
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Scaffolding
#   Volume: EMorSimpleShape::Empty, BoxExtent: (100.0, 100.0, 100.0)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (11450.0, 7500.0, 1250.0), (0.0, 0.0, -0.0), (2.0000, 2.0000, 2.0000), "AB_Mines_Scaffolding_Foundation_3x3m9", _folder)
if a: placed += 1
else: skipped += 1

# Construction: AB_Mines_Scaffolding_Foundation_3x3x1m_2
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Scaffolding
#   Volume: EMorSimpleShape::Empty, BoxExtent: (100.0, 100.0, 100.0)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (11350.0, 11100.0, 800.0), (0.0, 0.0, -0.0), (2.0000, 2.0000, 2.0000), "AB_Mines_Scaffolding_Foundation_3x3x1m_2", _folder)
if a: placed += 1
else: skipped += 1

# Construction: AB_Mines_Scaffolding_Foundation_3x3x1m10
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Scaffolding
#   Volume: EMorSimpleShape::Empty, BoxExtent: (100.0, 100.0, 100.0)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (11950.0, 11050.0, 1600.0), (0.0, 0.0, -0.0), (2.0000, 2.0000, 2.0000), "AB_Mines_Scaffolding_Foundation_3x3x1m10", _folder)
if a: placed += 1
else: skipped += 1

# Construction: AB_Mines_Scaffolding_Foundation_3x3x1m2
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Scaffolding
#   Volume: EMorSimpleShape::Empty, BoxExtent: (100.0, 100.0, 100.0)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (11350.0, 11400.0, 800.0), (0.0, 0.0, -0.0), (2.0000, 2.0000, 2.0000), "AB_Mines_Scaffolding_Foundation_3x3x1m2", _folder)
if a: placed += 1
else: skipped += 1

# Construction: AB_Mines_Scaffolding_Foundation_3x3x1m3
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Scaffolding
#   Volume: EMorSimpleShape::Empty, BoxExtent: (100.0, 100.0, 100.0)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (11350.0, 11700.0, 800.0), (0.0, 0.0, -0.0), (2.0000, 2.0000, 2.0000), "AB_Mines_Scaffolding_Foundation_3x3x1m3", _folder)
if a: placed += 1
else: skipped += 1

# Construction: AB_Mines_Scaffolding_Foundation_3x3x1m4
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Scaffolding
#   Volume: EMorSimpleShape::Empty, BoxExtent: (100.0, 100.0, 100.0)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (11350.0, 12000.0, 800.0), (0.0, 0.0, -0.0), (2.0000, 2.0000, 2.0000), "AB_Mines_Scaffolding_Foundation_3x3x1m4", _folder)
if a: placed += 1
else: skipped += 1

# Construction: AB_Mines_Scaffolding_Foundation_3x3x1m5_12
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Scaffolding
#   Volume: EMorSimpleShape::Empty, BoxExtent: (100.0, 100.0, 100.0)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (11650.0, 11650.0, 1600.0), (0.0, 0.0, -0.0), (2.0000, 2.0000, 2.0000), "AB_Mines_Scaffolding_Foundation_3x3x1m5_12", _folder)
if a: placed += 1
else: skipped += 1

# Construction: AB_Mines_Scaffolding_Foundation_3x3x1m6
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Scaffolding
#   Volume: EMorSimpleShape::Empty, BoxExtent: (100.0, 100.0, 100.0)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (11650.0, 11350.0, 1600.0), (0.0, 0.0, -0.0), (2.0000, 2.0000, 2.0000), "AB_Mines_Scaffolding_Foundation_3x3x1m6", _folder)
if a: placed += 1
else: skipped += 1

# Construction: AB_Mines_Scaffolding_Foundation_3x3x1m7
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Scaffolding
#   Volume: EMorSimpleShape::Empty, BoxExtent: (100.0, 100.0, 100.0)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (11650.0, 11050.0, 1600.0), (0.0, 0.0, -0.0), (2.0000, 2.0000, 2.0000), "AB_Mines_Scaffolding_Foundation_3x3x1m7", _folder)
if a: placed += 1
else: skipped += 1

# Construction: AB_Mines_Scaffolding_Foundation_3x3x1m9
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Scaffolding
#   Volume: EMorSimpleShape::Empty, BoxExtent: (100.0, 100.0, 100.0)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (11950.0, 11350.0, 1600.0), (0.0, 0.0, -0.0), (2.0000, 2.0000, 2.0000), "AB_Mines_Scaffolding_Foundation_3x3x1m9", _folder)
if a: placed += 1
else: skipped += 1

# Construction: AB_Mines_Scaffolding_Foundation_3x3x1m_B_2
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Scaffolding
#   Volume: EMorSimpleShape::OrientedBox, BoxExtent: (153.9, 152.9, 23.8)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (11347.561, 11651.266, 1628.9011), (0.0, 0.0, -0.0), (3.0774, 3.0583, 0.4757), "AB_Mines_Scaffolding_Foundation_3x3x1m_B_2", _folder)
if a: placed += 1
else: skipped += 1

# Construction: AB_Mines_Scaffolding_Foundation_3x3x1m_B10
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Scaffolding
#   Volume: EMorSimpleShape::OrientedBox, BoxExtent: (153.9, 152.9, 23.8)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (11647.561, 6901.2656, 1678.9011), (0.0, 0.0, -0.0), (3.0774, 3.0583, 0.4757), "AB_Mines_Scaffolding_Foundation_3x3x1m_B10", _folder)
if a: placed += 1
else: skipped += 1

# Construction: AB_Mines_Scaffolding_Foundation_3x3x1m_B11
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Scaffolding
#   Volume: EMorSimpleShape::OrientedBox, BoxExtent: (153.9, 152.9, 23.8)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (11947.561, 6901.2656, 1678.9011), (0.0, 0.0, -0.0), (3.0774, 3.0583, 0.4757), "AB_Mines_Scaffolding_Foundation_3x3x1m_B11", _folder)
if a: placed += 1
else: skipped += 1

# Construction: AB_Mines_Scaffolding_Foundation_3x3x1m_B12
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Scaffolding
#   Volume: EMorSimpleShape::OrientedBox, BoxExtent: (153.9, 152.9, 23.8)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (11847.561, 8101.2656, 1678.9011), (0.0, 0.0, -0.0), (3.0774, 3.0583, 0.4757), "AB_Mines_Scaffolding_Foundation_3x3x1m_B12", _folder)
if a: placed += 1
else: skipped += 1

# Construction: AB_Mines_Scaffolding_Foundation_3x3x1m_B13
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Scaffolding
#   Volume: EMorSimpleShape::OrientedBox, BoxExtent: (153.9, 152.9, 23.8)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (11847.561, 7801.2656, 1678.9011), (0.0, 0.0, -0.0), (3.0774, 3.0583, 0.4757), "AB_Mines_Scaffolding_Foundation_3x3x1m_B13", _folder)
if a: placed += 1
else: skipped += 1

# Construction: AB_Mines_Scaffolding_Foundation_3x3x1m_B14
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Scaffolding
#   Volume: EMorSimpleShape::OrientedBox, BoxExtent: (153.9, 152.9, 23.8)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (11847.561, 8101.2656, 1378.9011), (0.0, 0.0, -0.0), (3.0774, 3.0583, 0.4757), "AB_Mines_Scaffolding_Foundation_3x3x1m_B14", _folder)
if a: placed += 1
else: skipped += 1

# Construction: AB_Mines_Scaffolding_Foundation_3x3x1m_B2
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Scaffolding
#   Volume: EMorSimpleShape::OrientedBox, BoxExtent: (153.9, 152.9, 23.8)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (11347.561, 11351.266, 1628.9011), (0.0, 0.0, -0.0), (3.0774, 3.0583, 0.4757), "AB_Mines_Scaffolding_Foundation_3x3x1m_B2", _folder)
if a: placed += 1
else: skipped += 1

# Construction: AB_Mines_Scaffolding_Foundation_3x3x1m_B3_16
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Scaffolding
#   Volume: EMorSimpleShape::OrientedBox, BoxExtent: (153.9, 152.9, 23.8)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (11847.561, 8701.266, 1678.9011), (0.0, 0.0, -0.0), (3.0774, 3.0583, 0.4757), "AB_Mines_Scaffolding_Foundation_3x3x1m_B3_16", _folder)
if a: placed += 1
else: skipped += 1

# Construction: AB_Mines_Scaffolding_Foundation_3x3x1m_B4_9
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Scaffolding
#   Volume: EMorSimpleShape::OrientedBox, BoxExtent: (153.9, 152.9, 23.8)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (11547.561, 7801.2656, 1378.9011), (0.0, 0.0, -0.0), (3.0774, 3.0583, 0.4757), "AB_Mines_Scaffolding_Foundation_3x3x1m_B4_9", _folder)
if a: placed += 1
else: skipped += 1

# Construction: AB_Mines_Scaffolding_Foundation_3x3x1m_B5
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Scaffolding
#   Volume: EMorSimpleShape::OrientedBox, BoxExtent: (153.9, 152.9, 23.8)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (11547.561, 8101.2656, 1378.9011), (0.0, 0.0, -0.0), (3.0774, 3.0583, 0.4757), "AB_Mines_Scaffolding_Foundation_3x3x1m_B5", _folder)
if a: placed += 1
else: skipped += 1

# Construction: AB_Mines_Scaffolding_Foundation_3x3x1m_B6
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Scaffolding
#   Volume: EMorSimpleShape::OrientedBox, BoxExtent: (153.9, 152.9, 23.8)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (11847.561, 7801.2656, 1378.9011), (0.0, 0.0, -0.0), (3.0774, 3.0583, 0.4757), "AB_Mines_Scaffolding_Foundation_3x3x1m_B6", _folder)
if a: placed += 1
else: skipped += 1

# Construction: AB_Mines_Scaffolding_Foundation_3x3x1m_B7
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Scaffolding
#   Volume: EMorSimpleShape::OrientedBox, BoxExtent: (153.9, 152.9, 23.8)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (11747.561, 8401.266, 1378.9011), (0.0, 0.0, -0.0), (3.0774, 3.0583, 0.4757), "AB_Mines_Scaffolding_Foundation_3x3x1m_B7", _folder)
if a: placed += 1
else: skipped += 1

# Construction: AB_Mines_Scaffolding_Foundation_3x3x1m_B8_18
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Scaffolding
#   Volume: EMorSimpleShape::OrientedBox, BoxExtent: (153.9, 152.9, 23.8)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (12147.561, 8701.266, 1678.9011), (0.0, 0.0, -0.0), (3.0774, 3.0583, 0.4757), "AB_Mines_Scaffolding_Foundation_3x3x1m_B8_18", _folder)
if a: placed += 1
else: skipped += 1

# Construction: AB_Mines_Scaffolding_Foundation_3x3x1m_B9_21
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Scaffolding
#   Volume: EMorSimpleShape::OrientedBox, BoxExtent: (153.9, 152.9, 23.8)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (11647.561, 7201.2656, 1678.9011), (0.0, 0.0, -0.0), (3.0774, 3.0583, 0.4757), "AB_Mines_Scaffolding_Foundation_3x3x1m_B9_21", _folder)
if a: placed += 1
else: skipped += 1

# Construction: AB_Mines_Scaffolding_Platform_1x1x3m_4
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Scaffolding
#   Volume: EMorSimpleShape::OrientedBox, BoxExtent: (55.8, 54.7, 151.0)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (11249.603, 11250.0, 1100.8577), (0.0, 0.0, -0.0), (1.1169, 1.0939, 3.0203), "AB_Mines_Scaffolding_Platform_1x1x3m_4", _folder)
if a: placed += 1
else: skipped += 1

# Construction: AB_Mines_Scaffolding_Platform_1x1x3m10
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Scaffolding
#   Volume: EMorSimpleShape::OrientedBox, BoxExtent: (55.8, 54.7, 151.0)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (11749.603, 8800.0, 950.8576), (0.0, 0.0, -0.0), (1.1169, 1.0939, 3.0203), "AB_Mines_Scaffolding_Platform_1x1x3m10", _folder)
if a: placed += 1
else: skipped += 1

# Construction: AB_Mines_Scaffolding_Platform_1x1x3m11
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Scaffolding
#   Volume: EMorSimpleShape::OrientedBox, BoxExtent: (55.8, 54.7, 151.0)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (11749.603, 8800.0, 1250.8577), (0.0, 0.0, -0.0), (1.1169, 1.0939, 3.0203), "AB_Mines_Scaffolding_Platform_1x1x3m11", _folder)
if a: placed += 1
else: skipped += 1

# Construction: AB_Mines_Scaffolding_Platform_1x1x3m12
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Scaffolding
#   Volume: EMorSimpleShape::OrientedBox, BoxExtent: (55.8, 54.7, 151.0)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (11749.603, 8800.0, 1550.8577), (0.0, 0.0, -0.0), (1.1169, 1.0939, 3.0203), "AB_Mines_Scaffolding_Platform_1x1x3m12", _folder)
if a: placed += 1
else: skipped += 1

# Construction: AB_Mines_Scaffolding_Platform_1x1x3m13_24
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Scaffolding
#   Volume: EMorSimpleShape::OrientedBox, BoxExtent: (55.8, 54.7, 151.0)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (11749.603, 8300.0, 950.8576), (0.0, 0.0, -0.0), (1.1169, 1.0939, 3.0203), "AB_Mines_Scaffolding_Platform_1x1x3m13_24", _folder)
if a: placed += 1
else: skipped += 1

# Construction: AB_Mines_Scaffolding_Platform_1x1x3m14
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Scaffolding
#   Volume: EMorSimpleShape::OrientedBox, BoxExtent: (55.8, 54.7, 151.0)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (11749.603, 8800.0, 650.8576), (0.0, 0.0, -0.0), (1.1169, 1.0939, 3.0203), "AB_Mines_Scaffolding_Platform_1x1x3m14", _folder)
if a: placed += 1
else: skipped += 1

# Construction: AB_Mines_Scaffolding_Platform_1x1x3m15
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Scaffolding
#   Volume: EMorSimpleShape::OrientedBox, BoxExtent: (55.8, 54.7, 151.0)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (11749.603, 8300.0, 1250.8577), (0.0, 0.0, -0.0), (1.1169, 1.0939, 3.0203), "AB_Mines_Scaffolding_Platform_1x1x3m15", _folder)
if a: placed += 1
else: skipped += 1

# Construction: AB_Mines_Scaffolding_Platform_1x1x3m16
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Scaffolding
#   Volume: EMorSimpleShape::OrientedBox, BoxExtent: (55.8, 54.7, 151.0)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (11749.603, 8300.0, 1550.8577), (0.0, 0.0, -0.0), (1.1169, 1.0939, 3.0203), "AB_Mines_Scaffolding_Platform_1x1x3m16", _folder)
if a: placed += 1
else: skipped += 1

# Construction: AB_Mines_Scaffolding_Platform_1x1x3m17_29
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Scaffolding
#   Volume: EMorSimpleShape::OrientedBox, BoxExtent: (55.8, 54.7, 151.0)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (11549.603, 6800.0, 950.8576), (0.0, 0.0, -0.0), (1.1169, 1.0939, 3.0203), "AB_Mines_Scaffolding_Platform_1x1x3m17_29", _folder)
if a: placed += 1
else: skipped += 1

# Construction: AB_Mines_Scaffolding_Platform_1x1x3m18
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Scaffolding
#   Volume: EMorSimpleShape::OrientedBox, BoxExtent: (55.8, 54.7, 151.0)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (11549.603, 6800.0, 1250.8577), (0.0, 0.0, -0.0), (1.1169, 1.0939, 3.0203), "AB_Mines_Scaffolding_Platform_1x1x3m18", _folder)
if a: placed += 1
else: skipped += 1

# Construction: AB_Mines_Scaffolding_Platform_1x1x3m19
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Scaffolding
#   Volume: EMorSimpleShape::OrientedBox, BoxExtent: (55.8, 54.7, 151.0)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (11549.603, 6800.0, 1550.8577), (0.0, 0.0, -0.0), (1.1169, 1.0939, 3.0203), "AB_Mines_Scaffolding_Platform_1x1x3m19", _folder)
if a: placed += 1
else: skipped += 1

# Construction: AB_Mines_Scaffolding_Platform_1x1x3m2
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Scaffolding
#   Volume: EMorSimpleShape::OrientedBox, BoxExtent: (55.8, 54.7, 151.0)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (11249.603, 11250.0, 1400.8577), (0.0, 0.0, -0.0), (1.1169, 1.0939, 3.0203), "AB_Mines_Scaffolding_Platform_1x1x3m2", _folder)
if a: placed += 1
else: skipped += 1

# Construction: AB_Mines_Scaffolding_Platform_1x1x3m20
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Scaffolding
#   Volume: EMorSimpleShape::OrientedBox, BoxExtent: (55.8, 54.7, 151.0)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (11549.603, 6800.0, 650.8576), (0.0, 0.0, -0.0), (1.1169, 1.0939, 3.0203), "AB_Mines_Scaffolding_Platform_1x1x3m20", _folder)
if a: placed += 1
else: skipped += 1

# Construction: AB_Mines_Scaffolding_Platform_1x1x3m21
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Scaffolding
#   Volume: EMorSimpleShape::OrientedBox, BoxExtent: (55.8, 54.7, 151.0)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (11449.603, 8200.0, 950.8576), (0.0, 0.0, -0.0), (1.1169, 1.0939, 3.0203), "AB_Mines_Scaffolding_Platform_1x1x3m21", _folder)
if a: placed += 1
else: skipped += 1

# Construction: AB_Mines_Scaffolding_Platform_1x1x3m22
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Scaffolding
#   Volume: EMorSimpleShape::OrientedBox, BoxExtent: (55.8, 54.7, 151.0)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (11449.603, 8200.0, 1250.8577), (0.0, 0.0, -0.0), (1.1169, 1.0939, 3.0203), "AB_Mines_Scaffolding_Platform_1x1x3m22", _folder)
if a: placed += 1
else: skipped += 1

# Construction: AB_Mines_Scaffolding_Platform_1x1x3m23
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Scaffolding
#   Volume: EMorSimpleShape::OrientedBox, BoxExtent: (55.8, 54.7, 151.0)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (11449.603, 8200.0, 650.8576), (0.0, 0.0, -0.0), (1.1169, 1.0939, 3.0203), "AB_Mines_Scaffolding_Platform_1x1x3m23", _folder)
if a: placed += 1
else: skipped += 1

# Construction: AB_Mines_Scaffolding_Platform_1x1x3m3
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Scaffolding
#   Volume: EMorSimpleShape::OrientedBox, BoxExtent: (55.8, 54.7, 151.0)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (11249.603, 11750.0, 1100.8577), (0.0, 0.0, -0.0), (1.1169, 1.0939, 3.0203), "AB_Mines_Scaffolding_Platform_1x1x3m3", _folder)
if a: placed += 1
else: skipped += 1

# Construction: AB_Mines_Scaffolding_Platform_1x1x3m4
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Scaffolding
#   Volume: EMorSimpleShape::OrientedBox, BoxExtent: (55.8, 54.7, 151.0)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (11249.603, 11750.0, 1400.8577), (0.0, 0.0, -0.0), (1.1169, 1.0939, 3.0203), "AB_Mines_Scaffolding_Platform_1x1x3m4", _folder)
if a: placed += 1
else: skipped += 1

# Construction: AB_Mines_Scaffolding_Platform_1x1x3m5_10
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Scaffolding
#   Volume: EMorSimpleShape::OrientedBox, BoxExtent: (55.8, 54.7, 151.0)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (12199.603, 8850.0, 950.8576), (0.0, 0.0, -0.0), (1.1169, 1.0939, 3.0203), "AB_Mines_Scaffolding_Platform_1x1x3m5_10", _folder)
if a: placed += 1
else: skipped += 1

# Construction: AB_Mines_Scaffolding_Platform_1x1x3m6
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Scaffolding
#   Volume: EMorSimpleShape::OrientedBox, BoxExtent: (55.8, 54.7, 151.0)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (12199.603, 8850.0, 1250.8577), (0.0, 0.0, -0.0), (1.1169, 1.0939, 3.0203), "AB_Mines_Scaffolding_Platform_1x1x3m6", _folder)
if a: placed += 1
else: skipped += 1

# Construction: AB_Mines_Scaffolding_Platform_1x1x3m7
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Scaffolding
#   Volume: EMorSimpleShape::OrientedBox, BoxExtent: (55.8, 54.7, 151.0)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (12199.603, 8850.0, 1550.8577), (0.0, 0.0, -0.0), (1.1169, 1.0939, 3.0203), "AB_Mines_Scaffolding_Platform_1x1x3m7", _folder)
if a: placed += 1
else: skipped += 1

# Construction: AB_Mines_Scaffolding_Platform_1x1x3m8
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Scaffolding
#   Volume: EMorSimpleShape::OrientedBox, BoxExtent: (55.8, 54.7, 151.0)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (12199.603, 8850.0, 1850.8577), (0.0, 0.0, -0.0), (1.1169, 1.0939, 3.0203), "AB_Mines_Scaffolding_Platform_1x1x3m8", _folder)
if a: placed += 1
else: skipped += 1

# Construction: AB_Mines_Scaffolding_Platform_1x1x3m9
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Scaffolding
#   Volume: EMorSimpleShape::OrientedBox, BoxExtent: (55.8, 54.7, 151.0)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (12199.603, 8850.0, 650.8576), (0.0, 0.0, -0.0), (1.1169, 1.0939, 3.0203), "AB_Mines_Scaffolding_Platform_1x1x3m9", _folder)
if a: placed += 1
else: skipped += 1

# Construction: AB_Mines_Scaffolding_Platform_3x3x2m_5
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Scaffolding
#   Volume: EMorSimpleShape::OrientedBox, BoxExtent: (155.4, 153.7, 101.4)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (11599.126, 11650.822, 1751.2651), (0.0, 0.0, -0.0), (3.1087, 3.0748, 2.0284), "AB_Mines_Scaffolding_Platform_3x3x2m_5", _folder)
if a: placed += 1
else: skipped += 1

# Construction: AB_Mines_Scaffolding_Stairs_2M2_8
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Scaffolding
#   Volume: EMorSimpleShape::Empty, BoxExtent: (100.0, 100.0, 100.0)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (11700.0, 11350.0, 1750.0), (0.0, 0.0, -0.0), (2.0000, 2.0000, 2.0000), "AB_Mines_Scaffolding_Stairs_2M2_8", _folder)
if a: placed += 1
else: skipped += 1

# Construction: AB_Mines_Scaffolding_Stairs_3M2
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Scaffolding
#   Volume: EMorSimpleShape::Empty, BoxExtent: (100.0, 100.0, 100.0)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (11200.0, 7850.0, 950.0), (-0.0, -179.99994535848643, -0.0), (2.0000, 2.0000, 2.0000), "AB_Mines_Scaffolding_Stairs_3M2", _folder)
if a: placed += 1
else: skipped += 1

# Construction: BP_DM_Mines_Scaffolding_Rail_3M_2
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Stone
#   Volume: EMorSimpleShape::OrientedBox, BoxExtent: (6.7, 149.9, 42.7)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (11400.003, 7799.845, 1442.5139), (0.0, 0.0, -0.0), (0.1348, 2.9974, 0.8534), "BP_DM_Mines_Scaffolding_Rail_3M_2", _folder)
if a: placed += 1
else: skipped += 1

# Construction: BP_DM_Mines_Scaffolding_Rail_3M2
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Stone
#   Volume: EMorSimpleShape::OrientedBox, BoxExtent: (6.7, 149.9, 42.7)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (11400.003, 8099.845, 1442.5139), (0.0, 0.0, -0.0), (0.1348, 2.9974, 0.8534), "BP_DM_Mines_Scaffolding_Rail_3M2", _folder)
if a: placed += 1
else: skipped += 1

# Construction: BP_DM_Mines_Scaffolding_Rail_3M3_6
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Stone
#   Volume: EMorSimpleShape::OrientedBox, BoxExtent: (149.9, 6.7, 42.7)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (11450.155, 7060.003, 1442.5139), (0.0, 0.0, -0.0), (2.9974, 0.1348, 0.8534), "BP_DM_Mines_Scaffolding_Rail_3M3_6", _folder)
if a: placed += 1
else: skipped += 1

# Construction: BP_Suburbs_Platform_Medium_3x3m_Corner_B_Non_Destructible_no_floor_2
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Stone
#   Volume: EMorSimpleShape::OrientedBox, BoxExtent: (170.2, 173.5, 183.3)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (12379.887, 8828.275, 679.57007), (0.0, 0.0, -0.0), (3.4037, 3.4705, 3.6668), "BP_Suburbs_Platform_Medium_3x3m_Corner_B_Non_Destructible_no_floor_2", _folder)
if a: placed += 1
else: skipped += 1

# Construction: BP_Suburbs_Platform_Medium_3x3m_Corner_B_Non_Destructible_no_floor2_5
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Stone
#   Volume: EMorSimpleShape::OrientedBox, BoxExtent: (173.5, 170.2, 183.3)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (12378.224, 9170.184, 679.57007), (0.0, 0.0, -0.0), (3.4705, 3.4037, 3.6668), "BP_Suburbs_Platform_Medium_3x3m_Corner_B_Non_Destructible_no_floor2_5", _folder)
if a: placed += 1
else: skipped += 1

# Construction: BP_Suburbs_Platform_Medium_3x3m_Corner_B_Non_Destructible_no_floor3_8
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Stone
#   Volume: EMorSimpleShape::OrientedBox, BoxExtent: (170.2, 173.5, 183.3)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (12379.877, 10028.275, 679.57007), (0.0, 0.0, -0.0), (3.4037, 3.4705, 3.6668), "BP_Suburbs_Platform_Medium_3x3m_Corner_B_Non_Destructible_no_floor3_8", _folder)
if a: placed += 1
else: skipped += 1

# Construction: BP_Suburbs_Platform_Medium_3x3m_Corner_B_Non_Destructible_no_floor4_9
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Stone
#   Volume: EMorSimpleShape::OrientedBox, BoxExtent: (173.5, 170.2, 183.3)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (12378.215, 10370.184, 679.57007), (0.0, 0.0, -0.0), (3.4705, 3.4037, 3.6668), "BP_Suburbs_Platform_Medium_3x3m_Corner_B_Non_Destructible_no_floor4_9", _folder)
if a: placed += 1
else: skipped += 1

# Construction: BP_Suburbs_Platform_Small_3x3m_A_Non_Destructible_5
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Stone
#   Volume: EMorSimpleShape::OrientedBox, BoxExtent: (150.0, 150.0, 78.2)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (12450.007, 9750.06, 728.16724), (0.0, 0.0, -0.0), (3.0000, 3.0000, 1.5633), "BP_Suburbs_Platform_Small_3x3m_A_Non_Destructible_5", _folder)
if a: placed += 1
else: skipped += 1

# Construction: BP_Suburbs_Platform_Small_3x3m_A_Non_Destructible2
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Stone
#   Volume: EMorSimpleShape::OrientedBox, BoxExtent: (150.0, 150.0, 78.2)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (12450.008, 9450.06, 728.16724), (0.0, 0.0, -0.0), (3.0000, 3.0000, 1.5633), "BP_Suburbs_Platform_Small_3x3m_A_Non_Destructible2", _folder)
if a: placed += 1
else: skipped += 1

# ======================================================================
# PHASE 3: Breakables + DecoVolumes
# ======================================================================
unreal.log(f"[{BUBBLE_NAME}] Phase 3: Placing breakables and deco volumes...")

_folder = "Reconstruction/BD_BB_Outdoor_TradingPost/Breakables"

# Breakable Batch 0: BP_DM_Mines_Scaffolding_Rail_1M (1 instances)
#   BP Class: /Game/LevelDesign/Deco_Architecture/Mines/BP_DM_Mines_Scaffolding_Rail_1M
_brk_mesh = "/Game/Art/Assets/Kits/Deco_Architecture/Mines/Mines_Scaffolding_Rail_1M"
_brk_mats = ['/Game/Art/Assets/Kits/Deco_Architecture/Mines/Materials/Mines_Scaffolding/MI_Mines_Scaffolding_A_Deco']
a = spawn_static_mesh(_brk_mesh, _brk_mats, (11600.0, 8250.0, 1400.0), (0.0, 0.0, -0.0), (1.0, 1.0, 1.0), "BP_DM_Mines_Scaffolding_Rail_1M_2", _folder)
if a: placed += 1
else: skipped += 1

# Breakable Batch 1: BP_DM_Mines_Scaffolding_Rail_Corner (2 instances)
#   BP Class: /Game/LevelDesign/Deco_Architecture/Mines/BP_DM_Mines_Scaffolding_Rail_Corner
_brk_mesh = "/Game/Art/Assets/Kits/Deco_Architecture/Mines/Mines_Scaffolding_Rail_Corner"
_brk_mats = ['/Game/Art/Assets/Kits/Deco_Architecture/Mines/Materials/Mines_Scaffolding/MI_Mines_Scaffolding_A_Deco']
a = spawn_static_mesh(_brk_mesh, _brk_mats, (11600.0, 8450.0, 1400.0), (0.0, -89.99999818714215, 0.0), (1.0, 1.0, 1.0), "BP_DM_Mines_Scaffolding_Rail_Corner_2", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_brk_mesh, _brk_mats, (11300.0, 7550.0, 1400.0), (0.0, -89.99999818714215, 0.0), (1.0, 1.0, 1.0), "BP_DM_Mines_Scaffolding_Rail_Corner2", _folder)
if a: placed += 1
else: skipped += 1

# Breakable Batch 2: BP_DM_Mines_Scaffolding_Beam_3M_B (10 instances)
#   BP Class: /Game/Unshippable/Cinematics/Cine002/Environments/Scaffoldings/BP_DM_Mines_Scaffolding_Beam_3M_B
_brk_mesh = "/Game/Art/Assets/Kits/Deco_Architecture/Mines/Mines_Scaffolding_Beam_3M_B"
_brk_mats = ['/Game/Unshippable/Cinematics/Cine002/Environments/Materials/MI_Mines_Scaffolding_B_Mat']
a = spawn_static_mesh(_brk_mesh, _brk_mats, (10871.121, 14845.337, 618.9275), (0.0, 55.28176954079739, -0.0), (1.506474, 1.506474, 1.506474), "BP_DM_Mines_Scaffolding_Beam_3M_B10", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_brk_mesh, _brk_mats, (10249.215, 14698.412, 618.92737), (0.0, -124.71747216645969, 0.0), (1.506474, 1.506474, 1.506474), "BP_DM_Mines_Scaffolding_Beam_3M_B11", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_brk_mesh, _brk_mats, (10563.482, 14468.041, 618.92737), (0.0, 55.28176954079739, -0.0), (1.506474, 1.506474, 1.506474), "BP_DM_Mines_Scaffolding_Beam_3M_B12", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_brk_mesh, _brk_mats, (10117.06, 14456.633, 637.40796), (2.7586432771543845e-07, -114.7163171374262, 5.319478732329194), (1.506474, 1.506474, 1.506474), "BP_DM_Mines_Scaffolding_Beam_3M_B3", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_brk_mesh, _brk_mats, (10467.072, 14307.9795, 686.062), (-19.46548376432708, 102.78390012049424, 43.139746713211245), (1.506474, 1.506474, 1.506474), "BP_DM_Mines_Scaffolding_Beam_3M_B4", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_brk_mesh, _brk_mats, (10296.529, 14948.751, 618.92737), (0.0, -124.71747216645969, 0.0), (1.506474, 1.506474, 1.506474), "BP_DM_Mines_Scaffolding_Beam_3M_B5", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_brk_mesh, _brk_mats, (10731.383, 14644.535, 618.92737), (0.0, 55.28176954079739, -0.0), (1.506474, 1.506474, 1.506474), "BP_DM_Mines_Scaffolding_Beam_3M_B6", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_brk_mesh, _brk_mats, (10602.007, 15349.0625, 618.92737), (0.0, -124.71747216645969, 0.0), (1.506474, 1.506474, 1.506474), "BP_DM_Mines_Scaffolding_Beam_3M_B7", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_brk_mesh, _brk_mats, (10882.948, 17968.568, 268.92737), (0.0, 20.831512786620415, -0.0), (1.506474, 1.506474, 1.506474), "BP_DM_Mines_Scaffolding_Beam_3M_B8", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_brk_mesh, _brk_mats, (10463.998, 15128.945, 618.9275), (0.0, -124.71747216645969, 0.0), (1.506474, 1.506474, 1.506474), "BP_DM_Mines_Scaffolding_Beam_3M_B9", _folder)
if a: placed += 1
else: skipped += 1

# Breakable Batch 3: BP_DM_Mines_Scaffolding_Beam_3M_C (20 instances)
#   BP Class: /Game/Unshippable/Cinematics/Cine002/Environments/Scaffoldings/BP_DM_Mines_Scaffolding_Beam_3M_C
_brk_mesh = "/Game/Art/Assets/Kits/Deco_Architecture/Mines/Mines_Scaffolding_Beam_3M_C"
_brk_mats = ['/Game/Unshippable/Cinematics/Cine002/Environments/Materials/MI_Mines_Scaffolding_B_Mat']
a = spawn_static_mesh(_brk_mesh, _brk_mats, (10147.534, 14400.404, 1032.3269), (-3.113698537706078e-05, 155.2826405108165, -89.99954771060655), (1.5, 1.5, 1.145884), "BP_DM_Mines_Scaffolding_Beam_3M_C10", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_brk_mesh, _brk_mats, (10533.584, 14489.229, 1032.3258), (5.824722543172227e-06, 141.74448671813636, -89.9995193206842), (1.5, 1.5, 0.934026), "BP_DM_Mines_Scaffolding_Beam_3M_C11", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_brk_mesh, _brk_mats, (10373.582, 14547.05, 1032.3279), (5.887902588947737e-06, 145.28201663621496, -89.99954662818003), (1.5, 1.5, 1.052892), "BP_DM_Mines_Scaffolding_Beam_3M_C12", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_brk_mesh, _brk_mats, (10260.335, 14624.461, 1032.327), (2.7883994232233256e-05, 158.78070029024437, -89.99948872607021), (1.5, 1.5, 1.145884), "BP_DM_Mines_Scaffolding_Beam_3M_C13", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_brk_mesh, _brk_mats, (10700.006, 14687.8125, 1032.3273), (5.887902588947737e-06, 145.28201663621496, -89.99954662818003), (1.5, 1.5, 0.934026), "BP_DM_Mines_Scaffolding_Beam_3M_C14", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_brk_mesh, _brk_mats, (10521.703, 14760.821, 1032.328), (5.887902588947737e-06, 145.28201663621496, -89.99954662818003), (1.5, 1.5, 1.052892), "BP_DM_Mines_Scaffolding_Beam_3M_C15", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_brk_mesh, _brk_mats, (10301.5625, 14896.323, 1032.3264), (8.260239182764929e-06, 145.28188867555127, -89.99951135343088), (1.5, 1.5, 1.145884), "BP_DM_Mines_Scaffolding_Beam_3M_C16", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_brk_mesh, _brk_mats, (10484.563, 15104.096, 1023.70593), (8.260239182764929e-06, 145.28188867555127, -89.99951135343088), (1.5, 1.5, 1.145884), "BP_DM_Mines_Scaffolding_Beam_3M_C17", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_brk_mesh, _brk_mats, (10671.032, 14976.349, 1032.3292), (5.887902588947737e-06, 145.28201663621496, -89.99954662818003), (1.5, 1.5, 1.052892), "BP_DM_Mines_Scaffolding_Beam_3M_C18", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_brk_mesh, _brk_mats, (10647.038, 17957.967, 682.327), (3.4813605480588047e-06, 110.83184159619836, -89.99958202746275), (1.5, 1.5, 0.934026), "BP_DM_Mines_Scaffolding_Beam_3M_C19", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_brk_mesh, _brk_mats, (10712.795, 18417.672, 673.7064), (4.393691647356309e-06, 110.8316875775592, -89.99952330642378), (1.5, 1.5, 1.145884), "BP_DM_Mines_Scaffolding_Beam_3M_C21", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_brk_mesh, _brk_mats, (10801.927, 18219.986, 682.3296), (3.4813605480588047e-06, 110.83184159619836, -89.99958202746275), (1.5, 1.5, 1.052892), "BP_DM_Mines_Scaffolding_Beam_3M_C22", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_brk_mesh, _brk_mats, (10876.027, 18047.684, 673.7073), (3.4813605480588047e-06, 110.83184159619836, -89.99958202746275), (1.5, 1.5, 1.19272), "BP_DM_Mines_Scaffolding_Beam_3M_C23", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_brk_mesh, _brk_mats, (10436.624, 14316.684, 997.60767), (-7.27987409324838, -100.17056716141094, -113.08861219018306), (1.5, 1.5, 1.5), "BP_DM_Mines_Scaffolding_Beam_3M_C3", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_brk_mesh, _brk_mats, (10739.428, 14643.867, 1023.70654), (-6.928684625554969e-07, -124.71734933710168, -89.99969566988221), (1.5, 1.5, 2.091508), "BP_DM_Mines_Scaffolding_Beam_3M_C4", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_brk_mesh, _brk_mats, (10889.209, 17963.467, 682.3275), (-7.385758290356927e-07, -159.16776185943712, -89.9998315388572), (1.5, 1.5, 2.091508), "BP_DM_Mines_Scaffolding_Beam_3M_C5", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_brk_mesh, _brk_mats, (10879.174, 14844.667, 1032.3275), (-6.928684625554969e-07, -124.71734933710168, -89.99969566988221), (1.5, 1.5, 1.878793), "BP_DM_Mines_Scaffolding_Beam_3M_C6", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_brk_mesh, _brk_mats, (10587.616, 14455.385, 1022.056), (-6.928684625554969e-07, -124.71734933710168, -89.99969566988221), (1.5, 1.5, 1.70346), "BP_DM_Mines_Scaffolding_Beam_3M_C7", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_brk_mesh, _brk_mats, (10392.809, 14286.255, 1032.3271), (5.887902588947737e-06, 145.28201663621496, -89.99954662818003), (1.5, 1.5, 0.934026), "BP_DM_Mines_Scaffolding_Beam_3M_C8", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_brk_mesh, _brk_mats, (10239.848, 14354.274, 1008.42444), (8.208781367059537e-06, 145.2819468700032, -79.41676975890648), (1.5, 1.5, 1.052892), "BP_DM_Mines_Scaffolding_Beam_3M_C9", _folder)
if a: placed += 1
else: skipped += 1

# --- Extra DecoVolumes (not construction blocks) ---
_folder = "Reconstruction/BD_BB_Outdoor_TradingPost/DecoVolumes"

# DecoVolume: BP_DM_Mines_Fence_A_2 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (10386.514, 15018.171, 897.4328), (0.0, 0.0, -0.0), (2.0701, 2.3940, 2.3695), "DV_BP_DM_Mines_Fence_A_2_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_DM_Mines_Fence_Brace_D2 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (10239.154, 14271.54, 1432.4281), (0.0, 0.0, -0.0), (10.6634, 9.8842, 7.2629), "DV_BP_DM_Mines_Fence_Brace_D2_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_DM_Mines_Fence_Brace_D3 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (10676.348, 14638.811, 930.10516), (0.0, 0.0, -0.0), (7.2279, 7.5289, 4.1621), "DV_BP_DM_Mines_Fence_Brace_D3_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_DM_Mines_Fence_Brace_D4 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (10607.621, 13979.219, 930.10516), (0.0, 0.0, -0.0), (7.3329, 7.5182, 4.1621), "DV_BP_DM_Mines_Fence_Brace_D4_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_DM_Mines_Fence_Brace_D5 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (9855.811, 14524.244, 930.10516), (0.0, 0.0, -0.0), (7.1358, 6.2773, 4.1621), "DV_BP_DM_Mines_Fence_Brace_D5_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_DM_Mines_Scaffolding_Beam_3M_B10 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (10830.481, 14873.548, 826.52844), (0.0, 0.0, -0.0), (1.1031, 0.9275, 4.1567), "DV_BP_DM_Mines_Scaffolding_Beam_3M_B10_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_DM_Mines_Scaffolding_Beam_3M_B11 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (10289.8545, 14670.201, 826.5283), (0.0, 0.0, -0.0), (1.1032, 0.9275, 4.1567), "DV_BP_DM_Mines_Scaffolding_Beam_3M_B11_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_DM_Mines_Scaffolding_Beam_3M_B12 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (10522.843, 14496.252, 826.5283), (0.0, 0.0, -0.0), (1.1031, 0.9275, 4.1567), "DV_BP_DM_Mines_Scaffolding_Beam_3M_B12_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_DM_Mines_Scaffolding_Beam_3M_B3 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (10179.2705, 14427.95, 839.5284), (0.0, 0.0, -0.0), (1.4844, 0.9565, 4.2388), "DV_BP_DM_Mines_Scaffolding_Beam_3M_B3_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_DM_Mines_Scaffolding_Beam_3M_B4 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (10284.749, 14306.856, 796.9792), (0.0, 0.0, -0.0), (3.7876, 1.1212, 3.6817), "DV_BP_DM_Mines_Scaffolding_Beam_3M_B4_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_DM_Mines_Scaffolding_Beam_3M_B5 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (10337.169, 14920.54, 826.5283), (0.0, 0.0, -0.0), (1.1032, 0.9275, 4.1567), "DV_BP_DM_Mines_Scaffolding_Beam_3M_B5_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_DM_Mines_Scaffolding_Beam_3M_B6 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (10690.743, 14672.746, 826.5283), (0.0, 0.0, -0.0), (1.1031, 0.9275, 4.1567), "DV_BP_DM_Mines_Scaffolding_Beam_3M_B6_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_DM_Mines_Scaffolding_Beam_3M_B7 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (10642.646, 15320.852, 826.5283), (0.0, 0.0, -0.0), (1.1032, 0.9275, 4.1567), "DV_BP_DM_Mines_Scaffolding_Beam_3M_B7_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_DM_Mines_Scaffolding_Beam_3M_B8 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (10865.395, 18014.82, 476.52832), (0.0, 0.0, -0.0), (0.7399, 1.1429, 4.1567), "DV_BP_DM_Mines_Scaffolding_Beam_3M_B8_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_DM_Mines_Scaffolding_Beam_3M_B9 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (10504.638, 15100.734, 826.52844), (0.0, 0.0, -0.0), (1.1032, 0.9275, 4.1567), "DV_BP_DM_Mines_Scaffolding_Beam_3M_B9_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_DM_Mines_Scaffolding_Beam_3M_C10 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (10213.509, 14543.88, 1046.9457), (0.0, 0.0, -0.0), (1.6673, 3.0310, 0.3802), "DV_BP_DM_Mines_Scaffolding_Beam_3M_C10_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_DM_Mines_Scaffolding_Beam_3M_C11 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (10613.234, 14590.347, 1046.9445), (0.0, 0.0, -0.0), (1.8941, 2.2591, 0.3802), "DV_BP_DM_Mines_Scaffolding_Beam_3M_C11_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_DM_Mines_Scaffolding_Beam_3M_C12 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (10456.171, 14666.3545, 1046.9465), (0.0, 0.0, -0.0), (1.9670, 2.6044, 0.3802), "DV_BP_DM_Mines_Scaffolding_Beam_3M_C12_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_DM_Mines_Scaffolding_Beam_3M_C13 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (10317.433, 14771.694, 1046.9459), (0.0, 0.0, -0.0), (1.4986, 3.0850, 0.3802), "DV_BP_DM_Mines_Scaffolding_Beam_3M_C13_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_DM_Mines_Scaffolding_Beam_3M_C14 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (10773.265, 14793.652, 1046.9458), (0.0, 0.0, -0.0), (1.7802, 2.3348, 0.3802), "DV_BP_DM_Mines_Scaffolding_Beam_3M_C14_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_DM_Mines_Scaffolding_Beam_3M_C15 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (10604.292, 14880.126, 1046.9467), (0.0, 0.0, -0.0), (1.9670, 2.6044, 0.3802), "DV_BP_DM_Mines_Scaffolding_Beam_3M_C15_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_DM_Mines_Scaffolding_Beam_3M_C16 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (10391.45, 15026.162, 1046.9453), (0.0, 0.0, -0.0), (2.1131, 2.8153, 0.3802), "DV_BP_DM_Mines_Scaffolding_Beam_3M_C16_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_DM_Mines_Scaffolding_Beam_3M_C17 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (10574.451, 15233.935, 1038.3248), (0.0, 0.0, -0.0), (2.1131, 2.8153, 0.3802), "DV_BP_DM_Mines_Scaffolding_Beam_3M_C17_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_DM_Mines_Scaffolding_Beam_3M_C18 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (10753.621, 15095.653, 1046.9479), (0.0, 0.0, -0.0), (1.9670, 2.6044, 0.3802), "DV_BP_DM_Mines_Scaffolding_Beam_3M_C18_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_DM_Mines_Scaffolding_Beam_3M_C19 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (10767.321, 18003.803, 696.9455), (0.0, 0.0, -0.0), (2.5439, 1.2717, 0.3802), "DV_BP_DM_Mines_Scaffolding_Beam_3M_C19_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_DM_Mines_Scaffolding_Beam_3M_C21 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (10860.366, 18473.89, 688.32526), (0.0, 0.0, -0.0), (3.0902, 1.4796, 0.3802), "DV_BP_DM_Mines_Scaffolding_Beam_3M_C21_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_DM_Mines_Scaffolding_Beam_3M_C22 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (10937.5205, 18271.648, 696.9482), (0.0, 0.0, -0.0), (2.8504, 1.3883, 0.3802), "DV_BP_DM_Mines_Scaffolding_Beam_3M_C22_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_DM_Mines_Scaffolding_Beam_3M_C23 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (11029.632, 18106.197, 688.326), (0.0, 0.0, -0.0), (3.2110, 1.5255, 0.3802), "DV_BP_DM_Mines_Scaffolding_Beam_3M_C23_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_DM_Mines_Scaffolding_Beam_3M_C3 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (10245.311, 14359.646, 930.5256), (0.0, 0.0, -0.0), (3.9323, 1.2630, 2.0051), "DV_BP_DM_Mines_Scaffolding_Beam_3M_C3_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_DM_Mines_Scaffolding_Beam_3M_C4 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (10502.47, 14807.974, 1038.3257), (0.0, 0.0, -0.0), (4.9600, 3.5991, 0.3802), "DV_BP_DM_Mines_Scaffolding_Beam_3M_C4_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_DM_Mines_Scaffolding_Beam_3M_C5 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (10786.644, 18232.838, 696.94586), (0.0, 0.0, -0.0), (2.4075, 5.5289, 0.3802), "DV_BP_DM_Mines_Scaffolding_Beam_3M_C5_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_DM_Mines_Scaffolding_Beam_3M_C6 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (10666.312, 14992.078, 1046.9464), (0.0, 0.0, -0.0), (4.4776, 3.2648, 0.3802), "DV_BP_DM_Mines_Scaffolding_Beam_3M_C6_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_DM_Mines_Scaffolding_Beam_3M_C7 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (10394.615, 14589.034, 1036.6748), (0.0, 0.0, -0.0), (4.0799, 2.9893, 0.3802), "DV_BP_DM_Mines_Scaffolding_Beam_3M_C7_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_DM_Mines_Scaffolding_Beam_3M_C8 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (10466.067, 14392.095, 1046.9457), (0.0, 0.0, -0.0), (1.7802, 2.3348, 0.3802), "DV_BP_DM_Mines_Scaffolding_Beam_3M_C8_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_DM_Mines_Scaffolding_Beam_3M_C9 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (10319.502, 14469.344, 1049.4432), (0.0, 0.0, -0.0), (1.9786, 2.6212, 0.9073), "DV_BP_DM_Mines_Scaffolding_Beam_3M_C9_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_DM_Mines_Scaffolding_Rail_1M_2 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (11599.973, 8331.327, 1442.5139), (0.0, 0.0, -0.0), (0.1348, 1.6271, 0.8534), "DV_BP_DM_Mines_Scaffolding_Rail_1M_2_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_DM_Mines_Scaffolding_Rail_Corner_2 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (11643.8125, 8500.171, 1442.5139), (0.0, 0.0, -0.0), (1.0161, 1.0036, 0.8534), "DV_BP_DM_Mines_Scaffolding_Rail_Corner_2_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_DM_Mines_Scaffolding_Rail_Corner2 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (11343.8125, 7600.1704, 1442.5139), (0.0, 0.0, -0.0), (1.0161, 1.0036, 0.8534), "DV_BP_DM_Mines_Scaffolding_Rail_Corner2_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_Mines_Ceiling_Brace_A_2 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (9720.371, 14210.684, 1090.4661), (0.0, 0.0, -0.0), (3.8222, 3.8222, 7.9093), "DV_BP_Mines_Ceiling_Brace_A_2_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_Mines_Ceiling_Brace_A2 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (9533.035, 14034.796, 1090.4661), (0.0, 0.0, -0.0), (3.7603, 3.6934, 7.9093), "DV_BP_Mines_Ceiling_Brace_A2_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_Mines_Ceiling_Brace_A3 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (9381.814, 13770.232, 1090.4661), (0.0, 0.0, -0.0), (3.6296, 3.6296, 7.9093), "DV_BP_Mines_Ceiling_Brace_A3_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: CBP_MapStone_World_2 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (10334.94, 9184.514, 700.0), (-0.0, -45.000056798727684, -0.0), (2.0000, 2.0000, 2.3053), "DV_CBP_MapStone_World_2", _folder)
if a: placed += 1
else: skipped += 1

# ======================================================================
# SUMMARY
# ======================================================================
unreal.log(f"[{BUBBLE_NAME}] Reconstruction complete: {placed} placed, {skipped} skipped, {errors} errors")
