"""Auto-generated level reconstruction script.
Bubble: BD_BB_Chapter3_HeadwaterNexus
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

BUBBLE_NAME = "BD_BB_Chapter3_HeadwaterNexus"
placed = 0
skipped = 0
errors = 0

# ======================================================================
# PHASE 1: InstancedMeshCatalog  (static mesh placement)
# ======================================================================
unreal.log(f"[{BUBBLE_NAME}] Phase 1: Placing static meshes...")

# Batch 0: StaticMesh'Deep_ArchPiece_A' (6 instances)
_mesh_path = "/Game/Art/Assets/Kits/Architecture/Deep/Deep_ArchPiece_A"
_materials = ['/Game/Art/Assets/Kits/Architecture/Deep/Materials/Deep_TrimSheet/MI_Deep_TrimSheet_Lighter', '/Game/Art/Assets/Kits/Architecture/Deep/Materials/Deep_Non_Destructible/MI_Deep_Non_Destuctible_Lighter']
_folder = "Reconstruction/BD_BB_Chapter3_HeadwaterNexus/Meshes"
a = spawn_static_mesh(_mesh_path, _materials, (6569.3857, 5833.744, 1038.6576), (-0.2886048381480268, -90.21069777351825, 175.95097259536863), (0.5, 0.5, 0.5), "Deep_ArchPiece_A10", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (6779.406, 736.629, 1365.923), (0.0004169999669706248, 131.89815570845852, 179.99976777352686), (0.5, 0.5, 0.5), "Deep_ArchPiece_A13", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (6113.264, 1479.049, 1365.9302), (0.00041664150400602906, 131.89815570845826, 179.99976777352617), (0.5, 0.5, 0.5), "Deep_ArchPiece_A5_376", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (6412.985, 6704.3706, 1031.7429), (-0.2886048381480268, -90.21069777351825, 175.95097259536863), (0.5, 0.5, 0.5), "Deep_ArchPiece_A7", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (6409.786, 5834.3867, 1027.3602), (-0.2886048381480268, -90.21069777351825, 175.95097259536863), (0.5, 0.5, 0.5), "Deep_ArchPiece_A8", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (6572.5845, 6703.728, 1043.0403), (-0.2886048381480268, -90.21069777351825, 175.95097259536863), (0.5, 0.5, 0.5), "Deep_ArchPiece_A9", _folder)
if a: placed += 1
else: skipped += 1

# Batch 1: StaticMesh'Deep_ArchPiece_B_Damaged' (1 instances)
_mesh_path = "/Game/Art/Assets/Kits/Architecture/Deep/Deep_ArchPiece_B_Damaged"
_materials = ['/Game/Art/Assets/Kits/Architecture/Deep/Materials/Deep_TrimSheet/MI_Deep_TrimSheet_Damaged_Lighter', '/Game/Art/Assets/Kits/Architecture/Deep/Materials/Deep_Non_Destructible/MI_Deep_Non_Destructible_Light', '/Game/Unshippable/Whitebox/Rocks/Materials/PWM_Nordic_Blend_Tileable']
_folder = "Reconstruction/BD_BB_Chapter3_HeadwaterNexus/Meshes"
a = spawn_static_mesh(_mesh_path, _materials, (11500.147, 6156.7812, 1475.807), (0.11508890950944504, 93.72606483389056, 2.592351166629791), (1.0, 1.0, 1.0), "Deep_ArchPiece_B_8", _folder)
if a: placed += 1
else: skipped += 1

# Batch 2: StaticMesh'Deep_ArchPiece_B_Damaged' (1 instances)
_mesh_path = "/Game/Art/Assets/Kits/Architecture/Deep/Deep_ArchPiece_B_Damaged"
_materials = ['/Game/Art/Assets/Kits/Architecture/Deep/Materials/Deep_TrimSheet/MI_Deep_TrimSheet_Lighter', '/Game/Art/Assets/Kits/Architecture/Deep/Materials/Deep_Non_Destructible/MI_Deep_Non_Destructible_Light', '/Game/Unshippable/Whitebox/Rocks/Materials/PWM_Nordic_Blend_Tileable']
_folder = "Reconstruction/BD_BB_Chapter3_HeadwaterNexus/Meshes"
a = spawn_static_mesh(_mesh_path, _materials, (8960.197, 10923.873, 1379.9114), (-9.151919635709291e-05, 14.161002824555016, -89.99968887271955), (1.0, 1.0, 1.0), "Deep_ArchPiece_A2_127", _folder)
if a: placed += 1
else: skipped += 1

# Batch 3: StaticMesh'Deep_ArchPiece_B_Damaged' (2 instances)
_mesh_path = "/Game/Art/Assets/Kits/Architecture/Deep/Deep_ArchPiece_B_Damaged"
_materials = ['/Game/Art/Assets/Kits/Architecture/Deep/Materials/Deep_TrimSheet/MI_Deep_TrimSheet_Lighter', '/Game/Art/Assets/Kits/Architecture/Deep/Materials/Deep_Non_Destructible/MI_Deep_Non_Destuctible_Lighter', '/Game/Unshippable/Whitebox/Rocks/Materials/PWM_Nordic_Blend_Tileable']
_folder = "Reconstruction/BD_BB_Chapter3_HeadwaterNexus/Meshes"
a = spawn_static_mesh(_mesh_path, _materials, (6251.1816, 6105.023, 1017.42285), (0.2885761897606807, 89.78977425669362, 4.049011254230241), (1.0, 1.0, 1.0), "Deep_ArchPiece_A_33", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5125.2827, 11191.003, 1416.9856), (0.0006966792900038201, 156.42455724293362, -0.00021362307471028204), (1.0, 1.0, 1.0), "Deep_ArchPiece_A11", _folder)
if a: placed += 1
else: skipped += 1

# Batch 4: StaticMesh'Deep_ArchPiece_B_Piece_B' (1 instances)
_mesh_path = "/Game/Art/Assets/Kits/Architecture/Deep/Deep_ArchPiece_B_Piece_B"
_materials = ['/Game/Art/Assets/Kits/Architecture/Deep/Materials/Deep_TrimSheet/MI_Deep_TrimSheet_Damaged_Lighter', '/Game/Art/Assets/Kits/Architecture/Deep/Materials/Deep_Non_Destructible/MI_Deep_Non_Destructible_Light', '/Game/Unshippable/Whitebox/Rocks/Materials/PWM_Nordic_Blend_Tileable']
_folder = "Reconstruction/BD_BB_Chapter3_HeadwaterNexus/Meshes"
a = spawn_static_mesh(_mesh_path, _materials, (2012.9406, 8278.532, 765.6704), (-77.48162115414179, 0.8542907441476901, 35.535831633313016), (1.0, 1.0, 1.0), "Deep_ArchPiece_B_Piece_B_1008", _folder)
if a: placed += 1
else: skipped += 1

# Batch 5: StaticMesh'Deep_ArchPiece_Bended' (1 instances)
_mesh_path = "/Game/Art/Assets/Kits/Architecture/Deep/Deep_ArchPiece_Bended"
_materials = ['/Game/Art/Assets/Kits/Architecture/Deep/Materials/Deep_TrimSheet/MI_Deep_TrimSheet_Damaged_Lighter', '/Game/Art/Assets/Kits/Architecture/Deep/Materials/Deep_Non_Destructible/MI_Deep_Non_Destuctible_Lighter']
_folder = "Reconstruction/BD_BB_Chapter3_HeadwaterNexus/Meshes"
a = spawn_static_mesh(_mesh_path, _materials, (10615.226, 6260.0845, 770.5658), (0.000881094409444868, 69.01192526120404, 0.0009155273819407466), (1.0, 1.0, 1.0), "Deep_ArchPiece_Bended4_17", _folder)
if a: placed += 1
else: skipped += 1

# Batch 6: StaticMesh'Deep_ArchPiece_Bended' (1 instances)
_mesh_path = "/Game/Art/Assets/Kits/Architecture/Deep/Deep_ArchPiece_Bended"
_materials = ['/Game/Art/Assets/Kits/Architecture/Deep/Materials/Deep_TrimSheet/MI_Deep_TrimSheet_Lighter', '/Game/Art/Assets/Kits/Architecture/Deep/Materials/Deep_Non_Destructible/MI_Deep_Non_Destuctible_Lighter']
_folder = "Reconstruction/BD_BB_Chapter3_HeadwaterNexus/Meshes"
a = spawn_static_mesh(_mesh_path, _materials, (8409.895, 6246.0293, 2378.5984), (-0.00012207029388013109, 117.1038491006423, -179.99988388676064), (1.0, 1.0, 1.0), "Deep_ArchPiece_Bended3", _folder)
if a: placed += 1
else: skipped += 1

# Batch 7: StaticMesh'Deep_ArchPiece_Bended_B' (1 instances)
_mesh_path = "/Game/Art/Assets/Kits/Architecture/Deep/Deep_ArchPiece_Bended_B"
_materials = ['/Game/Art/Assets/Kits/Architecture/Deep/Materials/Deep_TrimSheet/MI_Deep_TrimSheet_Lighter', '/Game/Art/Assets/Kits/Architecture/Deep/Materials/Deep_Non_Destructible/MI_Deep_Non_Destuctible_Lighter']
_folder = "Reconstruction/BD_BB_Chapter3_HeadwaterNexus/Meshes"
a = spawn_static_mesh(_mesh_path, _materials, (6474.9233, 1155.1348, 2448.5754), (-1.1705325397180066, -41.267451870489545, 11.203611251251372), (1.0, 1.0, 1.0), "Deep_ArchPiece_Bended_B4_62", _folder)
if a: placed += 1
else: skipped += 1

# Batch 8: StaticMesh'Deep_ArchPiece_Bended_B_Damaged' (1 instances)
_mesh_path = "/Game/Art/Assets/Kits/Architecture/Deep/Deep_ArchPiece_Bended_B_Damaged"
_materials = ['/Game/Art/Assets/Kits/Architecture/Deep/Materials/Deep_TrimSheet/MI_Deep_TrimSheet_Damaged_Lighter', '/Game/Art/Assets/Kits/Architecture/Deep/Materials/Deep_Non_Destructible/MI_Deep_Non_Destructible_Light', '/Game/Unshippable/Whitebox/Rocks/Materials/PWM_Nordic_Blend_Tileable']
_folder = "Reconstruction/BD_BB_Chapter3_HeadwaterNexus/Meshes"
a = spawn_static_mesh(_mesh_path, _materials, (11279.879, 6305.5425, 2363.8306), (0.0, 100.00013657266632, -0.0), (1.0, 1.0, 1.0), "Deep_ArchPiece_Bended_B_Damaged_11", _folder)
if a: placed += 1
else: skipped += 1

# Batch 9: StaticMesh'Deep_ArchPiece_Bended_B_Damaged' (2 instances)
_mesh_path = "/Game/Art/Assets/Kits/Architecture/Deep/Deep_ArchPiece_Bended_B_Damaged"
_materials = ['/Game/Art/Assets/Kits/Architecture/Deep/Materials/Deep_TrimSheet/MI_Deep_TrimSheet_Lighter', '/Game/Art/Assets/Kits/Architecture/Deep/Materials/Deep_Non_Destructible/MI_Deep_Non_Destuctible_Lighter', '/Game/Unshippable/Whitebox/Rocks/Materials/PWM_Nordic_Blend_Tileable']
_folder = "Reconstruction/BD_BB_Chapter3_HeadwaterNexus/Meshes"
a = spawn_static_mesh(_mesh_path, _materials, (8951.17, 10758.0205, 2208.466), (1.843795060195061, -169.83923945905283, -3.052649787486844e-05), (1.0, 1.0, 1.0), "Deep_ArchPiece_Bended_B2_95", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (6328.0176, 6103.066, 2107.8298), (-0.2887878286123536, 89.95373556308384, 0.0002330245773116202), (1.0, 1.0, 1.0), "Deep_ArchPiece_Bended_B3_2", _folder)
if a: placed += 1
else: skipped += 1

# Batch 10: StaticMesh'Deep_ArchPiece_Bended_Damaged' (1 instances)
_mesh_path = "/Game/Art/Assets/Kits/Architecture/Deep/Deep_ArchPiece_Bended_Damaged"
_materials = ['/Game/Art/Assets/Kits/Architecture/Deep/Materials/Deep_TrimSheet/MI_Deep_TrimSheet_Damaged_Lighter', '/Game/Art/Assets/Kits/Architecture/Deep/Materials/Deep_Non_Destructible/MI_Deep_Non_Destructible_Light', '/Game/Unshippable/Whitebox/Rocks/Materials/PWM_Nordic_Blend_Tileable']
_folder = "Reconstruction/BD_BB_Chapter3_HeadwaterNexus/Meshes"
a = spawn_static_mesh(_mesh_path, _materials, (8371.503, 6157.801, 2009.0216), (4.098112374274372e-05, 119.99987949198801, 179.99992486790865), (1.0, 1.0, 1.0), "Deep_ArchPiece_Bended6", _folder)
if a: placed += 1
else: skipped += 1

# Batch 11: StaticMesh'Deep_ArchPiece_Bended_Damaged' (1 instances)
_mesh_path = "/Game/Art/Assets/Kits/Architecture/Deep/Deep_ArchPiece_Bended_Damaged"
_materials = ['/Game/Art/Assets/Kits/Architecture/Deep/Materials/Deep_TrimSheet/MI_Deep_TrimSheet_Damaged_Lighter', '/Game/Art/Assets/Kits/Architecture/Deep/Materials/Deep_Non_Destructible/MI_Deep_Non_Destuctible_Lighter', '/Game/Unshippable/Whitebox/Rocks/Materials/PWM_Nordic_Blend_Tileable']
_folder = "Reconstruction/BD_BB_Chapter3_HeadwaterNexus/Meshes"
a = spawn_static_mesh(_mesh_path, _materials, (8371.503, 6157.801, 959.0216), (0.0, -59.99999989158382, 0.0), (1.0, 1.0, 1.0), "Deep_ArchPiece_Bended5_24", _folder)
if a: placed += 1
else: skipped += 1

# Batch 12: StaticMesh'Deep_CircleFloor_B' (1 instances)
_mesh_path = "/Game/Art/Assets/Kits/Architecture/Deep/Deep_CircleFloor_B"
_materials = ['/Game/Art/Assets/Kits/Architecture/Deep/Materials/MI_Deep_Non_Destructible1', '/Game/Art/Assets/Kits/Architecture/Deep/Materials/Deep_TrimSheet/MI_Deep_TrimSheet_Damaged_Lighter']
_folder = "Reconstruction/BD_BB_Chapter3_HeadwaterNexus/Meshes"
a = spawn_static_mesh(_mesh_path, _materials, (2885.278, 8069.9146, 674.72125), (-0.2018432520447478, 0.002948020341615152, -0.8353881822308753), (1.5498309, 1.5498309, 1.5498309), "Deep_CircleFloor_B_110", _folder)
if a: placed += 1
else: skipped += 1

# Batch 13: StaticMesh'Deep_FloorTile_A' (3 instances)
_mesh_path = "/Game/Art/Assets/Kits/Architecture/Deep/Deep_FloorTile_A"
_materials = ['/Game/Art/Assets/Kits/Architecture/Deep/Materials/Deep_TrimSheet/MI_Deep_TrimSheet_Lighter']
_folder = "Reconstruction/BD_BB_Chapter3_HeadwaterNexus/Meshes"
a = spawn_static_mesh(_mesh_path, _materials, (9761.603, 5247.183, 860.50116), (0.0, 3.631841493386013, -0.0), (1.0, 1.0, 1.0), "Deep_FloorTile_A_5", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (9633.244, 5784.8574, 686.73224), (0.0, 3.6318409195658528, -0.0), (1.0, 1.0, 1.0), "Deep_FloorTile_A2", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (10209.128, 6238.663, 692.59033), (0.0, 52.229486161539846, -0.0), (1.0, 1.0, 1.0), "Deep_FloorTile_A3", _folder)
if a: placed += 1
else: skipped += 1

# Batch 14: StaticMesh'Deep_FloorTile_B' (3 instances)
_mesh_path = "/Game/Art/Assets/Kits/Architecture/Deep/Deep_FloorTile_B"
_materials = ['/Game/Art/Assets/Kits/Architecture/Deep/Materials/Deep_TrimSheet/MI_Deep_TrimSheet_Lighter']
_folder = "Reconstruction/BD_BB_Chapter3_HeadwaterNexus/Meshes"
a = spawn_static_mesh(_mesh_path, _materials, (9903.25, 5381.7227, 863.0891), (0.5411495013774296, 3.21688032765766, -0.01687622545365947), (1.0, 1.0, 1.0), "Deep_FloorTile_B_8", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (9603.883, 5356.2593, 862.1847), (-2.674804656955582, 4.99162335153158, 1.6383481772926355e-06), (1.0, 1.0, 1.0), "Deep_FloorTile_B2", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (9784.151, 5932.3086, 690.6241), (3.6360990068946375, 3.6318519631784834, 9.970888227176316e-07), (1.0, 1.0, 1.0), "Deep_FloorTile_B3", _folder)
if a: placed += 1
else: skipped += 1

# Batch 15: StaticMesh'Deep_FloorTile_C' (1 instances)
_mesh_path = "/Game/Art/Assets/Kits/Architecture/Deep/Deep_FloorTile_C"
_materials = ['/Game/Art/Assets/Kits/Architecture/Deep/Materials/Deep_TrimSheet/MI_Deep_TrimSheet_Lighter']
_folder = "Reconstruction/BD_BB_Chapter3_HeadwaterNexus/Meshes"
a = spawn_static_mesh(_mesh_path, _materials, (9945.644, 5801.8745, 690.0818), (0.0, 3.6318409195658528, -0.0), (1.0, 1.0, 1.0), "Deep_FloorTile_C2", _folder)
if a: placed += 1
else: skipped += 1

# Batch 16: StaticMesh'Deep_FloorTile_D' (7 instances)
_mesh_path = "/Game/Art/Assets/Kits/Architecture/Deep/Deep_FloorTile_D"
_materials = ['/Game/Art/Assets/Kits/Architecture/Deep/Materials/Deep_TrimSheet/MI_Deep_TrimSheet_Lighter']
_folder = "Reconstruction/BD_BB_Chapter3_HeadwaterNexus/Meshes"
a = spawn_static_mesh(_mesh_path, _materials, (9754.192, 5371.0977, 860.1458), (0.0, 3.847858408553052, -0.0), (1.0, 1.0, 1.0), "Deep_FloorTile_D_14", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (9909.761, 5258.005, 863.4249), (0.0, 2.9504003327815598, -0.0), (1.0, 1.0, 1.0), "Deep_FloorTile_D2", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (10054.639, 5393.33, 859.93005), (0.0, 3.834614254825973, -0.0), (1.0, 1.0, 1.0), "Deep_FloorTile_D3", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (9615.803, 5936.213, 696.02484), (0.0, -0.18753052956307995, 0.0), (1.0, 1.0, 1.0), "Deep_FloorTile_D5", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (9788.929, 5793.5947, 688.7092), (0.0, 2.950400791603245, -0.0), (1.0, 1.0, 1.0), "Deep_FloorTile_D6", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (9985.924, 5941.5405, 696.1112), (3.9188135850809274, 11.1067145339612, -1.7535093853987862), (1.0, 1.0, 1.0), "Deep_FloorTile_D7", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (10063.02, 5268.358, 859.93005), (0.0, 3.834614254825973, -0.0), (1.0, 1.0, 1.0), "Deep_FloorTile_D8", _folder)
if a: placed += 1
else: skipped += 1

# Batch 17: StaticMesh'Deep_Pillar_A' (2 instances)
_mesh_path = "/Game/Art/Assets/Kits/Architecture/Deep/Deep_Pillar_A"
_materials = ['/Game/Art/Assets/Kits/Architecture/Deep/Materials/Deep_TrimSheet/MI_Deep_TrimSheet_Damaged_Lighter', '/Game/Art/Assets/Kits/Architecture/Deep/Materials/Deep_Non_Destructible/MI_Deep_Non_Destructible_Light']
_folder = "Reconstruction/BD_BB_Chapter3_HeadwaterNexus/Meshes"
a = spawn_static_mesh(_mesh_path, _materials, (7399.3794, 1142.5575, 798.5372), (0.0, -68.96561174528732, 0.0), (1.359466, 1.359466, 1.359466), "Deep_Pillar_A7", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (6315.1367, 2106.2122, 773.42523), (0.0, -18.624330785244176, 0.0), (1.359466, 1.359466, 1.359466), "Deep_Pillar_A8", _folder)
if a: placed += 1
else: skipped += 1

# Batch 18: StaticMesh'Deep_Pillar_A_Damaged' (1 instances)
_mesh_path = "/Game/Art/Assets/Kits/Architecture/Deep/Deep_Pillar_A_Damaged"
_materials = ['/Game/Art/Assets/Kits/Architecture/Deep/Materials/Deep_TrimSheet/MI_Deep_TrimSheet_Damaged_Lighter', '/Game/Art/Assets/Kits/Architecture/Deep/Materials/Deep_Non_Destructible/MI_Deep_Non_Destructible_Light', '/Game/Unshippable/Whitebox/Rocks/Materials/PWM_Nordic_Blend_Tileable']
_folder = "Reconstruction/BD_BB_Chapter3_HeadwaterNexus/Meshes"
a = spawn_static_mesh(_mesh_path, _materials, (3871.0103, 7849.164, 807.2578), (0.0, 0.0, -0.0), (1.0, 1.0, 1.0), "Deep_Pillar_A5", _folder)
if a: placed += 1
else: skipped += 1

# Batch 19: StaticMesh'Deep_Pillar_A_Damaged' (2 instances)
_mesh_path = "/Game/Art/Assets/Kits/Architecture/Deep/Deep_Pillar_A_Damaged"
_materials = ['/Game/Art/Assets/Kits/Architecture/Deep/Materials/Deep_TrimSheet/MI_Deep_TrimSheet_Damaged_Lighter', '/Game/Art/Assets/Kits/Architecture/Deep/Materials/Deep_Non_Destructible/MI_Deep_Non_Destuctible_Lighter', '/Game/Unshippable/Whitebox/Rocks/Materials/PWM_Nordic_Blend_Tileable']
_folder = "Reconstruction/BD_BB_Chapter3_HeadwaterNexus/Meshes"
a = spawn_static_mesh(_mesh_path, _materials, (8920.0, 5660.0, 900.0), (0.0, -122.57076411806817, 0.0), (1.0, 1.0, 1.0), "Deep_Pillar_A_15", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (9836.603, 10356.781, 1045.9407), (0.0, -165.56874361460422, 0.0), (1.0, 1.0, 0.9400686), "Deep_Pillar_A2_23", _folder)
if a: placed += 1
else: skipped += 1

# Batch 20: StaticMesh'Deep_Pillar_A_Damaged_B' (2 instances)
_mesh_path = "/Game/Art/Assets/Kits/Architecture/Deep/Deep_Pillar_A_Damaged_B"
_materials = ['/Game/Art/Assets/Kits/Architecture/Deep/Materials/Deep_Non_Destructible/MI_Deep_Non_Destructible_Light', '/Game/Art/Assets/Kits/Architecture/Deep/Materials/Deep_TrimSheet/MI_Deep_TrimSheet_Damaged_Lighter', '/Game/Unshippable/Whitebox/Rocks/Materials/PWM_Nordic_Blend_Tileable']
_folder = "Reconstruction/BD_BB_Chapter3_HeadwaterNexus/Meshes"
a = spawn_static_mesh(_mesh_path, _materials, (11111.171, 6718.005, 1285.8105), (0.0, -91.14364411855641, 0.0), (1.0, 1.0, 1.0), "Deep_Pillar_A_B_Damaged_194", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2100.227, 7875.4414, 808.7017), (0.0, 92.37737212257102, -0.0), (1.0, 1.0, 1.0), "Deep_Pillar_A_B_Damaged2_1005", _folder)
if a: placed += 1
else: skipped += 1

# Batch 21: StaticMesh'Suburbs_Stairs_Medium_C_NonDest' (24 instances)
_mesh_path = "/Game/Art/Assets/Kits/Architecture/Suburbs/Suburbs_Stairs_Medium_C_NonDest"
_materials = ['/Game/Art/Assets/Kits/Architecture/Suburbs/Materials/Stairs_Medium_C_NonDest/MI_Stairs_Medium_C_NonDes_Lighter', '/Game/Art/Assets/Kits/Architecture/Suburbs/Materials/Stairs_Medium_C_NonDest/MI_Stairs_Medium_C_NonDes_Lighter']
_folder = "Reconstruction/BD_BB_Chapter3_HeadwaterNexus/Meshes"
a = spawn_static_mesh(_mesh_path, _materials, (5465.5215, 4292.255, 670.86664), (0.0, -164.72711936999707, 0.0), (1.0, 1.0, 1.0), "Suburbs_Stairs_Medium_C_NonDest_25", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (7073.9517, 1588.9712, 790.8919), (-1.272979748256922, 5.000580903214711, 1.116813777631416e-07), (1.0, 1.0, 1.0), "Suburbs_Stairs_Medium_C_NonDest10_359", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (7070.643, 2049.21, 606.0943), (0.0, -20.162751508585394, 0.0), (1.0, 1.0, 1.0), "Suburbs_Stairs_Medium_C_NonDest11_361", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (6663.0464, 1448.8417, 994.8746), (0.07801441290520349, -88.51154188083851, 1.2705697661441107), (1.0, 1.0, 1.0), "Suburbs_Stairs_Medium_C_NonDest12", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4536.539, 10506.932, 926.42737), (0.0, 136.2305708076759, -0.0), (1.0, 1.0, 1.0), "Suburbs_Stairs_Medium_C_NonDest13", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4319.6357, 10714.732, 926.42737), (0.0, 136.2305708076759, -0.0), (1.0, 1.0, 1.0), "Suburbs_Stairs_Medium_C_NonDest14", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4270.9478, 10230.602, 714.908), (0.0, 140.591026118667, -0.0), (1.0, 1.0, 1.0), "Suburbs_Stairs_Medium_C_NonDest15", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4038.8794, 10421.314, 714.908), (0.0, 140.591026118667, -0.0), (1.0, 1.0, 1.0), "Suburbs_Stairs_Medium_C_NonDest16", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4820.6274, 10725.812, 1088.735), (0.0, 147.6518882114765, -0.0), (1.0, 1.0, 1.0), "Suburbs_Stairs_Medium_C_NonDest17", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4575.3154, 10881.188, 1088.735), (0.0, 147.6518882114765, -0.0), (1.0, 1.0, 1.0), "Suburbs_Stairs_Medium_C_NonDest18", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (11065.339, 6306.6875, 1200.2161), (0.0, 140.89981293047768, -0.0), (1.0, 1.0, 1.0), "Suburbs_Stairs_Medium_C_NonDest19", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (6044.351, 4450.2583, 670.86664), (0.0, -164.72860440338326, 0.0), (1.0, 1.0, 1.0), "Suburbs_Stairs_Medium_C_NonDest2", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (10260.865, 3731.5088, 810.0473), (-0.808624205680149, -176.21658902080983, -7.064970223575091), (1.0, 1.0, 1.0), "Suburbs_Stairs_Medium_C_NonDest20", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (9961.552, 3711.711, 805.8063), (-0.8086545977627502, -176.21447721175264, -7.06490935451141), (1.0, 1.0, 1.0), "Suburbs_Stairs_Medium_C_NonDest21", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5790.8784, 7257.656, 665.86664), (0.0, 15.272581895602826, -0.0), (1.0, 1.0, 1.0), "Suburbs_Stairs_Medium_C_NonDest22", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5501.474, 7178.633, 665.86664), (0.0, 15.272581895602826, -0.0), (1.0, 1.0, 1.0), "Suburbs_Stairs_Medium_C_NonDest23", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5212.0674, 7099.609, 665.86664), (0.0, 15.272581895602826, -0.0), (1.0, 1.0, 1.0), "Suburbs_Stairs_Medium_C_NonDest24", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5754.937, 4371.2485, 670.86664), (0.0, -164.72724563259138, 0.0), (1.0, 1.0, 1.0), "Suburbs_Stairs_Medium_C_NonDest3", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (10183.4375, 4937.427, 845.8743), (0.0, 0.0, -0.0), (1.0, 1.0, 1.0), "Suburbs_Stairs_Medium_C_NonDest4_39", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (9883.4375, 4937.427, 845.8743), (0.0, 0.0, -0.0), (1.0, 1.0, 1.0), "Suburbs_Stairs_Medium_C_NonDest5", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (9583.4375, 4937.427, 845.8743), (0.0, 0.0, -0.0), (1.0, 1.0, 1.0), "Suburbs_Stairs_Medium_C_NonDest6", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (10525.51, 4639.383, 999.69904), (0.0, 123.00311683257554, -0.0), (1.0, 1.0, 1.0), "Suburbs_Stairs_Medium_C_NonDest7_14", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (9712.23, 5429.9673, 665.5739), (0.0, 3.967990600849008, -0.0), (1.0, 1.0, 1.0), "Suburbs_Stairs_Medium_C_NonDest8", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (10011.64, 5450.7314, 665.5739), (0.0, 3.967990600849008, -0.0), (1.0, 1.0, 1.0), "Suburbs_Stairs_Medium_C_NonDest9", _folder)
if a: placed += 1
else: skipped += 1

# Batch 22: StaticMesh'Cavern_Stalactites_A' (20 instances)
_mesh_path = "/Game/Art/Assets/Kits/Deco/Caveren/Cavern_Stalactites_A"
_materials = ['/Game/Art/Assets/Kits/Deco/Caveren/Materials/Cavern_Stalactites/Cavern_Stalactites_Mat_C']
_folder = "Reconstruction/BD_BB_Chapter3_HeadwaterNexus/Meshes"
a = spawn_static_mesh(_mesh_path, _materials, (6343.2876, 5820.5015, 1933.9014), (0.0, 0.0, -0.0), (1.0, 1.0, 1.0), "Cavern_Stalactites_A_804", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (10733.874, 6653.769, 2468.0386), (0.0, 0.0, -0.0), (1.0, 1.0, 1.0), "Cavern_Stalactites_A10_1463", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (8773.342, 6023.673, 2173.372), (0.0, 0.0, -0.0), (1.0, 1.0, 1.0), "Cavern_Stalactites_A11_1488", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (8534.516, 5928.846, 1947.1038), (0.0, 0.0, -0.0), (1.0, 1.0, 1.0), "Cavern_Stalactites_A12_1491", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (8217.48, 8364.34, 1923.1313), (0.0, 0.0, -0.0), (1.0, 1.0, 1.0), "Cavern_Stalactites_A13_1515", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (9043.81, 3410.9788, 2170.1292), (0.0, 0.0, -0.0), (1.0, 1.0, 1.0), "Cavern_Stalactites_A14_1542", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (7180.8843, 3108.9224, 1704.6339), (0.0, 0.0, -0.0), (1.0, 1.0, 1.0), "Cavern_Stalactites_A15_1576", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (11057.755, 4339.518, 2022.7603), (0.0, 0.0, -0.0), (1.0, 1.0, 1.0), "Cavern_Stalactites_A16_1602", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (9327.697, 3435.9458, 2033.4839), (0.0, 0.0, -0.0), (1.0, 1.0, 1.0), "Cavern_Stalactites_A17_1611", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (10750.29, 1447.2645, 2117.038), (0.0, 0.0, -0.0), (1.0, 1.0, 1.0), "Cavern_Stalactites_A18_1636", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (10731.649, 871.1665, 2074.9053), (0.0, 0.0, -0.0), (1.0, 1.0, 1.0), "Cavern_Stalactites_A19_1652", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (6101.9297, 5766.8926, 2217.325), (0.0, 0.0, -0.0), (1.0, 1.0, 1.0), "Cavern_Stalactites_A2_823", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5149.491, 6313.7007, 1923.9521), (0.0, 0.0, -0.0), (1.0, 1.0, 1.0), "Cavern_Stalactites_A20_1764", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4456.802, 7728.998, 1679.0659), (0.0, 0.0, -0.0), (1.0, 1.0, 1.0), "Cavern_Stalactites_A21_1807", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (9579.461, 10577.647, 2030.3013), (0.0, 0.0, -0.0), (1.0, 1.0, 1.0), "Cavern_Stalactites_A3_1339", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (10596.175, 8581.714, 1844.489), (0.0, 0.0, -0.0), (1.0, 1.0, 1.0), "Cavern_Stalactites_A5_1421", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (10574.049, 8861.234, 1820.6783), (0.0, 0.0, -0.0), (1.0, 1.0, 1.0), "Cavern_Stalactites_A6_1424", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (10206.119, 9153.98, 1998.9419), (0.0, 0.0, -0.0), (1.0, 1.0, 1.0), "Cavern_Stalactites_A7_1433", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (10009.866, 8603.828, 2016.3235), (0.0, 0.0, -0.0), (1.0, 1.0, 1.0), "Cavern_Stalactites_A8", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (10225.223, 7986.112, 1842.8097), (0.0, 0.0, -0.0), (1.0, 1.0, 1.0), "Cavern_Stalactites_A9_1437", _folder)
if a: placed += 1
else: skipped += 1

# Batch 23: StaticMesh'Cavern_Stalactites_B' (31 instances)
_mesh_path = "/Game/Art/Assets/Kits/Deco/Caveren/Cavern_Stalactites_B"
_materials = ['/Game/Art/Assets/Kits/Deco/Caveren/Materials/Cavern_Stalactites/Cavern_Stalactites_Mat_C']
_folder = "Reconstruction/BD_BB_Chapter3_HeadwaterNexus/Meshes"
a = spawn_static_mesh(_mesh_path, _materials, (9563.303, 4570.3564, 1990.2535), (0.0, 0.0, -0.0), (1.0, 1.0, 1.0), "Cavern_Stalactites_B_365", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (11591.417, 9032.268, 2086.5312), (0.0, 0.0, -0.0), (1.0, 1.0, 1.0), "Cavern_Stalactites_B10_1373", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (10339.542, 7880.53, 1771.6039), (0.0, 0.0, -0.0), (1.0, 1.0, 1.0), "Cavern_Stalactites_B11_1409", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (10539.753, 8526.6, 1823.2466), (0.0, 0.0, -0.0), (1.0, 1.0, 1.0), "Cavern_Stalactites_B12_1427", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (11087.105, 6478.736, 2452.4666), (0.0, 0.0, -0.0), (1.0, 1.0, 1.0), "Cavern_Stalactites_B13_1475", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (9727.724, 5054.039, 1976.8287), (0.0, 0.0, -0.0), (1.0, 1.0, 1.0), "Cavern_Stalactites_B14_1482", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (8183.6167, 7515.081, 1942.1631), (0.0, 0.0, -0.0), (1.0, 1.0, 1.0), "Cavern_Stalactites_B15_1485", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (8416.307, 5913.604, 1846.8271), (0.0, 0.0, -0.0), (1.0, 1.0, 1.0), "Cavern_Stalactites_B16_1494", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (10748.794, 5561.776, 2304.857), (0.0, 0.0, -0.0), (1.0, 1.0, 1.0), "Cavern_Stalactites_B17_1500", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (8611.393, 3234.5854, 2292.3652), (0.0, 0.0, -0.0), (1.0, 1.0, 1.0), "Cavern_Stalactites_B18_1545", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (7372.5796, 2926.8398, 2003.8926), (0.0, 0.0, -0.0), (1.0, 1.0, 1.0), "Cavern_Stalactites_B19_1573", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (7879.419, 3388.169, 1715.281), (0.0, 0.0, -0.0), (1.0, 1.0, 1.0), "Cavern_Stalactites_B2_397", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (11094.016, 4380.912, 2025.9209), (0.0, 0.0, -0.0), (1.0, 1.0, 1.0), "Cavern_Stalactites_B20_1596", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (9583.322, 3765.1436, 1974.6044), (0.0, 0.0, -0.0), (1.0, 1.0, 1.0), "Cavern_Stalactites_B21_1608", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (10927.762, 1929.3203, 2061.9465), (0.0, 0.0, -0.0), (1.0, 1.0, 1.0), "Cavern_Stalactites_B22_1639", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (11104.006, 2351.0586, 2047.758), (0.0, 0.0, -0.0), (1.0, 1.0, 1.0), "Cavern_Stalactites_B23_1642", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4985.583, 3055.832, 1764.3245), (0.0, 0.0, -0.0), (1.0, 1.0, 1.0), "Cavern_Stalactites_B24_1718", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5298.481, 3278.9019, 1887.418), (0.0, 0.0, -0.0), (1.0, 1.0, 1.0), "Cavern_Stalactites_B25_1732", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5461.8394, 3901.9346, 1734.1459), (0.0, 0.0, -0.0), (1.0, 1.0, 1.0), "Cavern_Stalactites_B26_1749", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4960.399, 7675.554, 1892.3204), (0.0, 0.0, -0.0), (1.0, 1.0, 1.0), "Cavern_Stalactites_B27_1779", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5850.0747, 8065.779, 1982.7334), (0.0, 0.0, -0.0), (1.0, 1.0, 1.0), "Cavern_Stalactites_B28_1787", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5945.7017, 8489.397, 2187.4702), (0.0, 0.0, -0.0), (1.0, 1.0, 1.0), "Cavern_Stalactites_B29_1795", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (6149.744, 1575.8413, 2364.62), (0.0, 0.0, -0.0), (1.0, 1.0, 1.0), "Cavern_Stalactites_B3_565", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4665.905, 7725.0674, 1815.1389), (0.0, 0.0, -0.0), (1.0, 1.0, 1.0), "Cavern_Stalactites_B30_1804", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1711.0343, 10841.356, 1890.1609), (0.0, 0.0, -0.0), (1.0, 1.0, 1.0), "Cavern_Stalactites_B31_1914", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (6174.901, 1443.4229, 2322.3335), (0.0, 0.0, -0.0), (1.0, 1.0, 1.0), "Cavern_Stalactites_B4", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (6325.755, 5762.0806, 1979.5183), (0.0, 0.0, -0.0), (1.0, 1.0, 1.0), "Cavern_Stalactites_B5_801", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (6288.771, 6531.786, 1937.2324), (0.0, 0.0, -0.0), (1.0, 1.0, 1.0), "Cavern_Stalactites_B6", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (6020.1543, 6877.79, 1894.0637), (0.0, 0.0, -0.0), (1.0, 1.0, 1.0), "Cavern_Stalactites_B7", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (10101.332, 10145.593, 1897.4951), (0.0, 0.0, -0.0), (1.0, 1.0, 1.0), "Cavern_Stalactites_B8_1327", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (8708.82, 10493.257, 2170.322), (0.0, 0.0, -0.0), (1.0, 1.0, 1.0), "Cavern_Stalactites_B9_1354", _folder)
if a: placed += 1
else: skipped += 1

# Batch 24: StaticMesh'Cavern_Stalactites_C' (27 instances)
_mesh_path = "/Game/Art/Assets/Kits/Deco/Caveren/Cavern_Stalactites_C"
_materials = ['/Game/Art/Assets/Kits/Deco/Caveren/Materials/Cavern_Stalactites/Cavern_Stalactites_Mat_C']
_folder = "Reconstruction/BD_BB_Chapter3_HeadwaterNexus/Meshes"
a = spawn_static_mesh(_mesh_path, _materials, (9549.337, 9579.435, 2293.5405), (0.0, 0.0, -0.0), (1.0, 1.0, 1.0), "Cavern_Stalactites_C_1333", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (10911.981, 5526.0967, 2265.6077), (0.0, 0.0, -0.0), (1.0, 1.0, 1.0), "Cavern_Stalactites_C10_1478", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (10957.02, 3589.2642, 2106.9712), (0.0, 0.0, -0.0), (1.0, 1.0, 1.0), "Cavern_Stalactites_C11_1508", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (8045.0195, 8285.525, 1901.6876), (0.0, 0.0, -0.0), (1.0, 1.0, 1.0), "Cavern_Stalactites_C12_1512", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (8672.793, 7714.107, 2256.9812), (0.0, 0.0, -0.0), (1.0, 1.0, 1.0), "Cavern_Stalactites_C13_1518", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (8085.039, 9100.21, 2165.4177), (0.0, 0.0, -0.0), (1.0, 1.0, 1.0), "Cavern_Stalactites_C14_1523", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (9100.896, 3418.4683, 2183.8135), (0.0, 0.0, -0.0), (1.0, 1.0, 1.0), "Cavern_Stalactites_C15_1539", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (8172.716, 2971.0122, 2128.5193), (0.0, 0.0, -0.0), (1.0, 1.0, 1.0), "Cavern_Stalactites_C16_1548", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (11609.658, 3434.2505, 1982.8173), (0.0, 0.0, -0.0), (1.0, 1.0, 1.0), "Cavern_Stalactites_C17_1615", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (10881.015, 1346.0681, 2026.3658), (0.0, 0.0, -0.0), (1.0, 1.0, 1.0), "Cavern_Stalactites_C18_1633", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (11081.565, 2426.8699, 2058.0728), (0.0, 0.0, -0.0), (1.0, 1.0, 1.0), "Cavern_Stalactites_C19_1645", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (7988.1357, 7891.153, 1825.319), (0.0, 0.0, -0.0), (1.0, 1.0, 1.0), "Cavern_Stalactites_C2_185", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (11029.018, 941.96484, 1862.1228), (0.0, 0.0, -0.0), (1.0, 1.0, 1.0), "Cavern_Stalactites_C20_1649", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5225.148, 6505.2437, 2019.6705), (0.0, 0.0, -0.0), (1.0, 1.0, 1.0), "Cavern_Stalactites_C21_1761", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4850.6006, 7564.61, 1802.4875), (0.0, 0.0, -0.0), (1.0, 1.0, 1.0), "Cavern_Stalactites_C22_1776", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5996.444, 10334.106, 2541.0479), (0.0, 0.0, -0.0), (1.0, 1.0, 1.0), "Cavern_Stalactites_C23_1842", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (6695.133, 10172.302, 2459.112), (0.0, 0.0, -0.0), (1.0, 1.0, 1.0), "Cavern_Stalactites_C24_1848", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (6262.7676, 10491.632, 2294.236), (0.0, 0.0, -0.0), (1.0, 1.0, 1.0), "Cavern_Stalactites_C25_1869", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3658.4731, 10588.628, 2566.9602), (0.0, 0.0, -0.0), (1.0, 1.0, 1.0), "Cavern_Stalactites_C26_1884", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2552.6953, 10515.025, 2204.449), (0.0, 0.0, -0.0), (1.0, 1.0, 1.0), "Cavern_Stalactites_C27_1911", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (8194.775, 9461.24, 1923.5681), (0.0, 0.0, -0.0), (1.0, 1.0, 1.0), "Cavern_Stalactites_C3_217", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (8485.419, 6868.6772, 2352.9214), (0.0, 0.0, -0.0), (1.0, 1.0, 1.0), "Cavern_Stalactites_C4_128", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (8064.4023, 3494.2227, 2062.3413), (0.0, 0.0, -0.0), (1.0, 1.0, 1.0), "Cavern_Stalactites_C5_385", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (7756.0674, 3074.654, 1717.4269), (0.0, 0.0, -0.0), (1.0, 1.0, 1.0), "Cavern_Stalactites_C6_394", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (10087.267, 8766.86, 2024.7064), (0.0, 0.0, -0.0), (1.0, 1.0, 1.0), "Cavern_Stalactites_C7_1430", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (10082.841, 8536.64, 2011.4983), (0.0, 0.0, -0.0), (1.0, 1.0, 1.0), "Cavern_Stalactites_C8_1440", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (10562.969, 7154.156, 2221.5964), (0.0, 0.0, -0.0), (1.0, 1.0, 1.0), "Cavern_Stalactites_C9_1460", _folder)
if a: placed += 1
else: skipped += 1

# Batch 25: StaticMesh'Cavern_Stalactites_D' (3 instances)
_mesh_path = "/Game/Art/Assets/Kits/Deco/Caveren/Cavern_Stalactites_D"
_materials = ['/Game/Art/Assets/Kits/Deco/Caveren/Materials/Cavern_Stalactites/Cavern_Stalactites_Mat_D']
_folder = "Reconstruction/BD_BB_Chapter3_HeadwaterNexus/Meshes"
a = spawn_static_mesh(_mesh_path, _materials, (8232.316, 7291.0615, 1903.2656), (0.0, -16.35494879971197, 0.0), (1.9981527, 1.9981527, 1.9981527), "Cavern_Stalactites_D_188", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (8396.166, 9375.037, 2183.573), (0.0, -62.58463125695573, 0.0), (1.5, 1.5, 1.5), "Cavern_Stalactites_D2_214", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (10912.989, 5122.239, 2157.0256), (0.0, -77.03939585276187, 0.0), (1.0, 1.0, 1.0), "Cavern_Stalactites_D3_1505", _folder)
if a: placed += 1
else: skipped += 1

# Batch 26: StaticMesh'Cavern_Stalactites_E' (8 instances)
_mesh_path = "/Game/Art/Assets/Kits/Deco/Caveren/Cavern_Stalactites_E"
_materials = ['/Game/Art/Assets/Kits/Deco/Caveren/Materials/Cavern_Stalactites/Cavern_Stalactites_Mat_D']
_folder = "Reconstruction/BD_BB_Chapter3_HeadwaterNexus/Meshes"
a = spawn_static_mesh(_mesh_path, _materials, (8562.774, 9922.095, 2188.9192), (0.0, 28.68571095388876, -0.0), (1.4737208, 1.4737208, 1.4737208), "Cavern_Stalactites_E_65", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (6191.0205, 5576.2676, 2183.1392), (0.0, 61.787267448407036, -0.0), (1.5, 1.5, 1.5), "Cavern_Stalactites_E2_793", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (11622.4795, 8866.116, 1770.3446), (0.0, 0.0, -0.0), (1.0, 1.0, 1.0), "Cavern_Stalactites_E3_1370", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (10539.065, 4251.5625, 2092.1738), (0.0, 31.08344812827483, -0.0), (1.0, 1.0, 1.0), "Cavern_Stalactites_E4_1590", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (7903.1177, 744.54834, 2095.9663), (0.0, 0.0, -0.0), (1.0, 1.0, 1.0), "Cavern_Stalactites_E5_1668", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4957.852, 3293.622, 1683.1421), (0.0, 38.27753968279928, -0.0), (1.0, 1.0, 1.0), "Cavern_Stalactites_E6_1729", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4733.524, 8119.6284, 1985.7992), (0.0, 149.61773954220914, -0.0), (1.0, 1.0, 1.0), "Cavern_Stalactites_E7_1801", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (398.79196, 11433.577, 1859.5787), (0.0, 0.0, -0.0), (1.0, 1.0, 1.0), "Cavern_Stalactites_E8_1932", _folder)
if a: placed += 1
else: skipped += 1

# Batch 27: StaticMesh'Cavern_Stalactites_G' (38 instances)
_mesh_path = "/Game/Art/Assets/Kits/Deco/Caveren/Cavern_Stalactites_G"
_materials = ['/Game/Art/Assets/Kits/Deco/Caveren/Materials/Cavern_Stalactites/Cavern_Stalactites_Mat_B']
_folder = "Reconstruction/BD_BB_Chapter3_HeadwaterNexus/Meshes"
a = spawn_static_mesh(_mesh_path, _materials, (6052.7505, 6382.3057, 2316.2534), (0.0, 94.23791028423283, -0.0), (1.0, 1.0, 1.0), "Cavern_Stalactites_G_808", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (6364.557, 6408.046, 1993.1627), (0.0, 103.11088396631216, -0.0), (1.0, 1.0, 1.0), "Cavern_Stalactites_G10_820", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (9379.172, 10503.253, 2171.922), (0.0, -23.01300015483781, 0.0), (1.0, 1.0, 1.0), "Cavern_Stalactites_G11_1336", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (8489.778, 10514.235, 2151.5513), (0.0, 0.0, -0.0), (1.0, 1.0, 1.0), "Cavern_Stalactites_G12_1342", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (11118.2, 9860.65, 1965.637), (0.0, 0.0, -0.0), (1.0, 1.0, 1.0), "Cavern_Stalactites_G13_1358", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (10816.678, 8881.325, 1822.697), (0.0, 38.37151375730669, -0.0), (1.0, 1.0, 1.0), "Cavern_Stalactites_G14_1376", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (10719.666, 8695.624, 1836.4307), (0.0, 23.80472144279595, -0.0), (1.0, 1.0, 1.0), "Cavern_Stalactites_G15_1418", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (10972.526, 6735.959, 2280.7974), (0.0, 143.2332769152168, -0.0), (1.0, 1.0, 1.0), "Cavern_Stalactites_G16_1444", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (10368.54, 6607.9727, 2533.9795), (0.0, -20.078308622748892, 0.0), (1.0, 1.0, 1.0), "Cavern_Stalactites_G17_1466", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (9421.401, 5604.274, 1997.8123), (0.0, -52.60403426397915, 0.0), (1.0, 1.0, 1.0), "Cavern_Stalactites_G18_1529", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (9528.019, 5119.728, 1766.9778), (0.0, 68.38787453985225, -0.0), (1.0, 1.0, 1.0), "Cavern_Stalactites_G19_1536", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (9964.929, 9953.143, 1912.0889), (0.0, -151.18606819530686, 0.0), (1.0, 1.0, 1.0), "Cavern_Stalactites_G2_55", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (7554.8574, 2981.2756, 1912.2036), (0.0, 0.0, -0.0), (1.0, 1.0, 1.0), "Cavern_Stalactites_G20_1558", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (7070.8296, 2991.267, 1967.0547), (0.0, -39.9082638287023, 0.0), (1.0, 1.0, 1.0), "Cavern_Stalactites_G21_1561", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (7443.5435, 3252.8318, 1647.04), (0.0, -173.52167440619502, 0.0), (1.0, 1.0, 1.0), "Cavern_Stalactites_G22_1567", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5872.917, 2036.2275, 2357.6484), (0.0, 148.21493144534412, -0.0), (1.0, 1.0, 1.0), "Cavern_Stalactites_G24_1684", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4467.981, 2272.932, 1962.6406), (0.0, 76.99389444340643, -0.0), (1.0, 1.0, 1.0), "Cavern_Stalactites_G25_1702", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4892.4517, 3188.6604, 1817.4668), (0.0, 34.931855821345366, -0.0), (1.0, 1.0, 1.0), "Cavern_Stalactites_G26_1712", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5347.611, 3675.6191, 1835.4692), (0.0, -173.09511090215088, 0.0), (1.0, 1.0, 1.0), "Cavern_Stalactites_G27_1721", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5186.6323, 5110.794, 1810.3578), (0.0, -61.839019553563666, 0.0), (1.0, 1.0, 1.0), "Cavern_Stalactites_G28_1756", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5728.563, 7764.9526, 1913.2231), (0.0, 0.0, -0.0), (1.0, 1.0, 1.0), "Cavern_Stalactites_G29_1773", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (10708.727, 9829.885, 1958.8303), (0.0, -46.524044558396284, 0.0), (1.0, 1.0, 1.0), "Cavern_Stalactites_G3_1329", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (6853.5923, 8440.459, 1919.9486), (0.0, -128.99797136140583, 0.0), (1.0, 1.0, 1.0), "Cavern_Stalactites_G30_1821", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (7395.8257, 8799.017, 2083.912), (0.0, 42.36914819681149, -0.0), (1.0, 1.0, 1.0), "Cavern_Stalactites_G31_1827", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (6453.4414, 10462.975, 2355.7456), (0.0, 151.85660648556262, -0.0), (1.0, 1.0, 1.0), "Cavern_Stalactites_G32_1836", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (7179.311, 10098.246, 2282.4963), (0.0, 121.8615464218194, -0.0), (1.0, 1.0, 1.0), "Cavern_Stalactites_G33_1845", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5578.6123, 10454.106, 2369.2034), (0.0, 94.49810777589272, -0.0), (1.0, 1.0, 1.0), "Cavern_Stalactites_G34_1860", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (6133.019, 10559.13, 2271.7144), (0.0, 149.19546504757346, -0.0), (1.0, 1.0, 1.0), "Cavern_Stalactites_G35_1866", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2552.3857, 11268.306, 1852.7242), (0.0, 105.70731632657464, -0.0), (1.0, 1.0, 1.0), "Cavern_Stalactites_G36_1901", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2473.173, 10914.027, 2101.5679), (0.0, 101.93549713871465, -0.0), (1.0, 1.0, 1.0), "Cavern_Stalactites_G37_1908", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1165.8718, 8363.38, 1814.6483), (0.0, -88.22949263610316, 0.0), (1.0, 1.0, 1.0), "Cavern_Stalactites_G38_1920", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (568.9024, 11257.082, 1992.7253), (0.0, 0.0, -0.0), (1.0, 1.0, 1.0), "Cavern_Stalactites_G39_1929", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (8462.448, 9569.778, 2241.671), (0.0, 91.00560467889628, -0.0), (1.5, 1.5, 1.5), "Cavern_Stalactites_G4_211", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (8313.541, 6626.767, 2275.647), (0.0, 53.14732173389891, -0.0), (1.2304132, 1.2304132, 1.2304132), "Cavern_Stalactites_G5_113", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (9065.397, 5783.0356, 2180.2878), (0.0, 110.62788366029824, -0.0), (1.230413, 1.230413, 1.230413), "Cavern_Stalactites_G6_199", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (8401.981, 7118.2964, 2179.7131), (0.0, 58.08465978282715, -0.0), (1.230413, 1.230413, 1.230413), "Cavern_Stalactites_G7", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (9048.382, 3996.9185, 1778.5525), (0.0, 0.0, -0.0), (1.0, 1.0, 1.0), "Cavern_Stalactites_G8_353", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (8413.849, 3129.1719, 2272.989), (0.0, -134.20987327403375, 0.0), (1.5, 1.5, 1.5), "Cavern_Stalactites_G9_400", _folder)
if a: placed += 1
else: skipped += 1

# Batch 28: StaticMesh'Cavern_Stalactites_H' (66 instances)
_mesh_path = "/Game/Art/Assets/Kits/Deco/Caveren/Cavern_Stalactites_H"
_materials = ['/Game/Art/Assets/Kits/Deco/Caveren/Materials/Cavern_Stalactites/Cavern_Stalactites_Mat_A']
_folder = "Reconstruction/BD_BB_Chapter3_HeadwaterNexus/Meshes"
a = spawn_static_mesh(_mesh_path, _materials, (8146.047, 8113.4014, 1947.679), (0.0, 75.82256931852704, -0.0), (1.0828357, 1.0828357, 1.0828357), "Cavern_Stalactites_H_44", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (8371.927, 4104.006, 1901.1033), (0.0, -142.3340983583642, 0.0), (1.0, 1.0, 1.0), "Cavern_Stalactites_H10_391", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (6944.6514, 985.86523, 2412.2285), (0.0, 172.4014480971747, -0.0), (1.0, 1.0, 1.0), "Cavern_Stalactites_H11_568", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (6112.1353, 6700.0615, 2107.6055), (0.0, 141.14217144167762, -0.0), (1.0, 1.0, 1.0), "Cavern_Stalactites_H12_796", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (10298.334, 10061.747, 1904.8715), (0.0, 155.55035369181002, -0.0), (1.0, 1.0, 1.0), "Cavern_Stalactites_H13", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (11257.99, 9014.493, 2033.2966), (0.0, -73.88855016552812, 0.0), (1.0, 1.0, 1.0), "Cavern_Stalactites_H14_1366", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (11448.911, 9234.14, 2187.692), (0.0, -139.80777829365337, 0.0), (1.0, 1.0, 1.0), "Cavern_Stalactites_H15", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (10753.427, 8329.386, 1814.7463), (0.0, 45.53030672949991, -0.0), (1.0, 1.0, 1.0), "Cavern_Stalactites_H16_1395", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (11104.107, 8853.042, 1971.26), (0.0, -18.171111916206737, 0.0), (1.0, 1.0, 1.0), "Cavern_Stalactites_H17", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (10456.029, 7300.0103, 2076.2368), (0.0, -18.949523317961102, 0.0), (1.0, 1.0, 1.0), "Cavern_Stalactites_H18_1399", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (10733.334, 6974.3853, 2329.5977), (0.0, 142.48991397113028, -0.0), (1.0, 1.0, 1.0), "Cavern_Stalactites_H19_1447", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (8488.093, 8038.925, 2058.7637), (0.0, -25.663572410986784, 0.0), (1.082836, 1.082836, 1.082836), "Cavern_Stalactites_H2", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (10917.258, 5706.8716, 2424.1355), (0.0, 43.02052701861232, -0.0), (1.0, 1.0, 1.0), "Cavern_Stalactites_H20_1469", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (10410.149, 5472.8335, 2220.2898), (0.0, -172.12462285816426, 0.0), (1.0, 1.0, 1.0), "Cavern_Stalactites_H21_1497", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (7963.021, 8458.635, 1972.3018), (0.0, -30.414212371789233, 0.0), (1.082836, 1.082836, 1.082836), "Cavern_Stalactites_H22", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (9620.572, 5382.1367, 1976.7611), (0.0, 0.0, -0.0), (1.0, 1.0, 1.0), "Cavern_Stalactites_H23_1532", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (10905.171, 4162.0464, 2094.1704), (-3.3469843259096024, 178.36190747154774, 0.09562098133902472), (1.0, 1.0, 1.0), "Cavern_Stalactites_H24_1587", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (7152.001, 3414.373, 1650.5469), (0.0, -56.117211931470976, 0.0), (1.0, 1.0, 1.0), "Cavern_Stalactites_H25_1564", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (11260.92, 3992.9902, 2085.047), (0.0, 105.94944849581798, -0.0), (1.0, 1.0, 1.0), "Cavern_Stalactites_H26_1593", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (9417.183, 3631.3206, 1985.7499), (0.0, -80.57250985065338, 0.0), (1.0, 1.0, 1.0), "Cavern_Stalactites_H27_1605", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (11579.712, 2842.1433, 2084.0093), (0.0, 52.6426844284189, -0.0), (1.0, 1.0, 1.0), "Cavern_Stalactites_H28_1618", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (12055.26, 3303.8823, 1860.7993), (0.0, 108.98805832992679, -0.0), (1.0, 1.0, 1.0), "Cavern_Stalactites_H29_1621", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (11353.141, 9920.541, 1962.2661), (0.0, 0.0, -0.0), (1.0, 1.0, 1.0), "Cavern_Stalactites_H3_1362", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (10905.455, 1681.9827, 2041.6395), (0.0, 65.33219569685176, -0.0), (1.0, 1.0, 1.0), "Cavern_Stalactites_H30_1630", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (8829.24, 1764.6361, 2268.8096), (0.0, -68.31960809873877, 0.0), (1.0, 1.0, 1.0), "Cavern_Stalactites_H31_1655", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (7867.099, 531.5126, 2081.9458), (0.0, 94.2067502540252, -0.0), (1.0, 1.0, 1.0), "Cavern_Stalactites_H32_1665", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (6076.7188, 1928.5222, 2549.8079), (0.0, -59.85180510846735, 0.0), (1.0, 1.0, 1.0), "Cavern_Stalactites_H34_1681", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5415.747, 2232.5845, 2338.0908), (0.0, 0.0, -0.0), (1.0, 1.0, 1.0), "Cavern_Stalactites_H35_1690", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (6015.123, 2482.9988, 2232.111), (0.0, 51.631330981827816, -0.0), (1.0, 1.0, 1.0), "Cavern_Stalactites_H36_1693", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5169.404, 2523.7397, 2009.5214), (0.0, 106.01028886377983, -0.0), (1.0, 1.0, 1.0), "Cavern_Stalactites_H37_1696", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4744.9644, 2846.0967, 1792.2062), (0.0, -84.79733771862946, 0.0), (1.0, 1.0, 1.0), "Cavern_Stalactites_H38_1699", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5153.4634, 3591.7488, 1866.9119), (0.0, -80.82742530407543, 0.0), (1.0, 1.0, 1.0), "Cavern_Stalactites_H39_1726", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (8403.156, 7469.8945, 2216.7686), (0.0, 82.21991046006288, -0.0), (1.2811828, 1.2811828, 1.2811828), "Cavern_Stalactites_H4_196", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (6303.3228, 4539.5645, 2080.3843), (0.0, 0.0, -0.0), (1.0, 1.0, 1.0), "Cavern_Stalactites_H40_1739", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (6745.018, 3758.4438, 2179.9353), (0.0, 106.67248476992583, -0.0), (1.0, 1.0, 1.0), "Cavern_Stalactites_H41", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (6391.579, 4529.8867, 1989.3187), (0.0, 0.0, -0.0), (1.0, 1.0, 1.0), "Cavern_Stalactites_H42", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (6113.732, 4324.861, 2202.0151), (0.0, -153.9212621515369, 0.0), (1.0, 1.0, 1.0), "Cavern_Stalactites_H43", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5599.732, 4150.7754, 2112.3796), (0.0, 15.647110012992366, -0.0), (1.0, 1.0, 1.0), "Cavern_Stalactites_H44_1746", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5255.7427, 5966.7236, 1967.9578), (0.0, 93.93867247040734, -0.0), (1.0, 1.0, 1.0), "Cavern_Stalactites_H45_1753", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5976.6084, 5548.4663, 2295.6958), (0.0, 0.0, -0.0), (1.0, 1.0, 1.0), "Cavern_Stalactites_H46_1767", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5947.3457, 8235.869, 2064.2107), (0.0, 0.0, -0.0), (1.0, 1.0, 1.0), "Cavern_Stalactites_H48_1782", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (6281.254, 8460.867, 2136.6445), (0.0, 0.0, -0.0), (1.0, 1.0, 1.0), "Cavern_Stalactites_H49_1790", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (9350.782, 6030.1753, 2529.7551), (0.0, 116.55249313758546, -0.0), (1.4558831, 1.4558831, 1.4558831), "Cavern_Stalactites_H5_124", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4408.8145, 7994.8677, 1944.1725), (0.0, -19.34014772353591, 0.0), (1.0, 1.0, 1.0), "Cavern_Stalactites_H50_1798", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (6974.0977, 8672.987, 2051.6248), (0.0, 30.251566456816146, -0.0), (1.0, 1.0, 1.0), "Cavern_Stalactites_H51_1814", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (7563.13, 9319.945, 2188.0005), (0.0, -73.34985610720749, 0.0), (1.0, 1.0, 1.0), "Cavern_Stalactites_H52_1824", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (6988.513, 10386.394, 2189.9531), (0.0, 158.27758733712926, -0.0), (1.0, 1.0, 1.0), "Cavern_Stalactites_H53_1833", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4093.2363, 11396.292, 2443.3467), (0.0, -35.23184337708575, 0.0), (1.0, 1.0, 1.0), "Cavern_Stalactites_H54_1851", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4516.24, 11204.793, 2458.9116), (0.0, 27.97754157147704, -0.0), (1.0, 1.0, 1.0), "Cavern_Stalactites_H55_1854", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5413.351, 10732.831, 2414.2542), (0.0, 133.52559514964696, -0.0), (1.0, 1.0, 1.0), "Cavern_Stalactites_H56_1857", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3324.7087, 11883.739, 2137.6167), (0.0, -161.03333755694123, 0.0), (1.0, 1.0, 1.0), "Cavern_Stalactites_H57_1872", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2881.783, 12108.382, 1914.6167), (0.0, 48.00528411294069, -0.0), (1.0, 1.0, 1.0), "Cavern_Stalactites_H58_1875", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3695.027, 10894.253, 2458.5186), (0.0, -111.0781645068049, 0.0), (1.0, 1.0, 1.0), "Cavern_Stalactites_H59_1878", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (9453.696, 4300.955, 1916.3525), (0.0, -75.54183420009313, 0.0), (1.0, 1.0, 1.0), "Cavern_Stalactites_H6_348", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4059.0234, 10760.5625, 2573.0347), (0.0, 0.0, -0.0), (1.0, 1.0, 1.0), "Cavern_Stalactites_H60_1881", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1748.9636, 11029.009, 1844.2214), (0.0, -80.5883498684297, 0.0), (1.0, 1.0, 1.0), "Cavern_Stalactites_H61_1892", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2213.7998, 11104.457, 1877.6533), (0.0, -112.99801445043492, 0.0), (1.0, 1.0, 1.0), "Cavern_Stalactites_H62_1895", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2216.1392, 8874.15, 2293.1116), (0.0, 112.30040609594344, -0.0), (1.0, 1.0, 1.0), "Cavern_Stalactites_H63_1904", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1981.0833, 8440.092, 2112.7544), (0.0, 112.30040609594344, -0.0), (1.0, 1.0, 1.0), "Cavern_Stalactites_H64", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1219.1543, 8692.508, 1985.7756), (0.0, 106.13806641612514, -0.0), (1.0, 1.0, 1.0), "Cavern_Stalactites_H65_1917", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1956.3569, 8130.231, 1803.3928), (0.0, 0.0, -0.0), (1.0, 1.0, 1.0), "Cavern_Stalactites_H66_1923", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1048.2091, 11154.496, 1911.7856), (0.0, 178.953463965676, -0.0), (1.0, 1.0, 1.0), "Cavern_Stalactites_H67_1926", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (11195.933, 5872.2505, 2411.1042), (0.0, 43.02052701861232, -0.0), (1.0, 1.0, 1.0), "Cavern_Stalactites_H68", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (9668.116, 4858.595, 2043.2833), (0.0, -89.84676718202529, 0.0), (1.0, 1.0, 1.0), "Cavern_Stalactites_H7", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (7976.997, 3578.658, 1933.9705), (0.0, -89.84676718202529, 0.0), (1.0, 1.0, 1.0), "Cavern_Stalactites_H8", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (8161.407, 3675.0312, 2119.838), (0.0, 15.93321126591417, -0.0), (1.0, 1.0, 1.0), "Cavern_Stalactites_H9", _folder)
if a: placed += 1
else: skipped += 1

# Batch 29: StaticMesh'Cavern_Stalactites_J' (4 instances)
_mesh_path = "/Game/Art/Assets/Kits/Deco/Caveren/Cavern_Stalactites_J"
_materials = ['/Game/Art/Assets/Kits/Deco/Caveren/Materials/Cavern_Stalactites/Cavern_Stalactites_Mat_B']
_folder = "Reconstruction/BD_BB_Chapter3_HeadwaterNexus/Meshes"
a = spawn_static_mesh(_mesh_path, _materials, (9254.623, 4280.03, 1738.5142), (0.0, 0.0, -0.0), (1.0, 1.0, 1.0), "Cavern_Stalactites_J_356", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (6782.4194, 962.3249, 2212.9814), (0.0, 152.438713753896, -0.0), (1.1315033, 1.1315033, 1.1315033), "Cavern_Stalactites_J2_574", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (10537.097, 7480.095, 1576.1964), (0.0, 101.7474541338121, -0.0), (1.0, 1.0, 1.0), "Cavern_Stalactites_J3_1406", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (9957.637, 8391.227, 2123.5032), (0.0, 87.25936762651929, -0.0), (1.0, 1.0, 1.0), "Cavern_Stalactites_J4_1412", _folder)
if a: placed += 1
else: skipped += 1

# Batch 30: StaticMesh'Cavern_Stalagmites_A' (69 instances)
_mesh_path = "/Game/Art/Assets/Kits/Deco/Caveren/Cavern_Stalagmites_A"
_materials = ['/Game/Art/Assets/Kits/Deco/Caveren/Materials/Cavern_Stalagmites/Cavern_Stalagmites_Mat_A']
_folder = "Reconstruction/BD_BB_Chapter3_HeadwaterNexus/Meshes"
a = spawn_static_mesh(_mesh_path, _materials, (9096.791, 5713.3027, 938.45496), (0.0, 0.0, -0.0), (1.6771588, 1.5503012, 1.5), "Cavern_Stalagmites_A_98", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (11536.124, 10047.268, 781.62646), (0.8279491895110707, -67.19989314846572, -1.9688720891445335), (2.0, 2.0, 2.0), "Cavern_Stalagmites_A10", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (10807.727, 8766.855, 884.1197), (-1.804901262230557, 147.66675670923377, 1.1421095468123388), (2.0, 2.0, 2.0), "Cavern_Stalagmites_A11", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (10959.78, 1233.593, 797.3203), (0.0, -70.74438464130043, 0.0), (2.0, 2.0, 2.0), "Cavern_Stalagmites_A12", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (8193.183, 6712.145, 1026.1565), (-4.838530879465199, 22.55605189116492, -5.343719209201856), (1.5, 1.5, 1.5), "Cavern_Stalagmites_A13", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (9086.884, 4401.5483, 1212.0646), (-3.415479316032587e-08, -47.93578863529636, -4.868347284779017), (2.0, 2.0, 2.0), "Cavern_Stalagmites_A14_345", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (10622.38, 7945.8633, 912.1765), (-1.0088197190116057, -118.17962213696717, -1.8825377458963028), (2.0, 2.0, 2.0), "Cavern_Stalagmites_A15", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1393.3743, 8487.133, 693.4899), (0.0, 16.85229963217127, -0.0), (2.0, 2.0, 2.0), "Cavern_Stalagmites_A16_393", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (8203.182, 3250.5894, 672.955), (2.457338277090426, 21.75537705465396, 0.9803014504940735), (2.0, 2.0, 2.0), "Cavern_Stalagmites_A17_320", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (10320.46, 7674.98, 833.7488), (2.3184903307459637, -123.55986418567724, -2.0614011882313754), (2.0, 2.0, 2.0), "Cavern_Stalagmites_A18", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (10539.001, 6587.5796, 685.56244), (0.0, -136.30971306621126, 0.0), (2.0, 2.0, 2.0), "Cavern_Stalagmites_A19_1385", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (10379.056, 5081.622, 931.91785), (0.0, -38.45309789069384, 0.0), (1.7532105, 1.7532105, 1.7532105), "Cavern_Stalagmites_A2_19", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4380.5586, 7948.333, 844.5606), (-0.19479370323582804, 161.33334991096723, -1.715179514441035), (2.0, 2.0, 2.0), "Cavern_Stalagmites_A20_863", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (6029.2925, 7640.1226, 945.1761), (1.9236728940877086, -90.35079630246392, 0.8914094681431995), (2.0, 2.0, 2.0), "Cavern_Stalagmites_A21", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (9181.987, 5955.0728, 719.15094), (0.0, 0.0, -0.0), (1.5, 1.5, 1.5), "Cavern_Stalagmites_A22_109", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (8381.793, 7114.906, 808.0741), (0.0, -118.27617097743017, 0.0), (1.5, 1.5, 1.5), "Cavern_Stalagmites_A23", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (8062.644, 6400.723, 1094.9796), (0.0, -60.88177467090154, 0.0), (1.5, 1.5, 1.5), "Cavern_Stalagmites_A24", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (8151.248, 6271.244, 1017.99146), (0.0, -60.88177467090154, 0.0), (1.5, 1.5, 1.5), "Cavern_Stalagmites_A25", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (7771.72, 3607.7708, 947.9722), (-7.176382932273253e-09, -39.92034622502046, -1.843078609230983), (2.0, 2.0, 2.0), "Cavern_Stalagmites_A26_323", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (8051.228, 4070.7278, 912.2291), (0.0, -62.25967401759794, 0.0), (2.0, 1.9999999, 1.9999999), "Cavern_Stalagmites_A27_372", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (8517.364, 4268.3003, 910.1219), (0.8471142589899079, 1.0033397658094743, -4.06793249329516), (2.0, 2.0, 2.0), "Cavern_Stalagmites_A28", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (6138.2183, 5588.5073, 903.4925), (1.7183687139493426e-10, -168.26370015781458, -1.843444290596465), (2.0, 2.0, 2.0), "Cavern_Stalagmites_A29_786", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (10464.54, 5188.352, 1068.7681), (0.8150942718659796, -71.42068258647714, -0.7187499553694249), (2.0, 2.0, 2.0), "Cavern_Stalagmites_A3", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (6316.642, 6714.4727, 1158.5018), (2.4283575358372422, -80.57842506774367, -8.729247486369596), (2.0, 2.0, 2.0), "Cavern_Stalagmites_A30", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (6049.598, 6825.586, 887.7142), (-0.3566588268193994, -142.84520219200297, -1.8684997690928784), (2.0, 2.0, 2.0), "Cavern_Stalagmites_A31", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (6628.3853, 6377.3438, 1155.123), (0.0, -34.277924211646905, 0.0), (2.0, 2.0, 2.0), "Cavern_Stalagmites_A32_817", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5944.026, 5314.3223, 881.59393), (0.7461092919616608, -170.82935179000594, -1.841766154453605), (2.0, 2.0, 2.0), "Cavern_Stalagmites_A33", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (7246.1934, 8726.512, 1000.6397), (-0.705535911338933, 11.9326756326158, 1.57540992761738), (2.0, 2.0, 2.0), "Cavern_Stalagmites_A34", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (10870.027, 8565.107, 984.82275), (1.6942758976815198, -37.51839790526897, -1.300567494162895), (2.0, 2.0, 2.0), "Cavern_Stalagmites_A35", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (10831.656, 7017.4165, 1381.5455), (-8.905638224486387, -146.47801740565436, -0.7717896870483018), (2.0, 2.0, 2.0), "Cavern_Stalagmites_A36", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (10908.826, 7243.5674, 1505.6367), (3.8176250913921677, 93.44659007733998, 8.088749433537403), (2.0, 2.0, 2.0), "Cavern_Stalagmites_A37", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (11171.694, 5382.4937, 1265.402), (-8.905609112751938, -146.47777241368638, -8.104676046243798), (2.0, 2.0, 2.0), "Cavern_Stalagmites_A38", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (9472.298, 5226.2637, 879.15356), (0.0, 61.775416291583014, -0.0), (2.0, 2.0, 2.0), "Cavern_Stalagmites_A39", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (8297.125, 9642.273, 885.2736), (0.0, -44.23538053220568, 0.0), (2.0, 1.9999999, 1.9999999), "Cavern_Stalagmites_A4_58", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (10909.346, 4201.7646, 1191.6654), (-8.905609112751938, -146.47777241368638, -8.104676046243798), (2.0, 2.0, 2.0), "Cavern_Stalagmites_A40", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (11592.72, 3609.7285, 881.4073), (-8.905608948274596, -146.47743408690175, 2.579795492301635), (2.0, 2.0, 2.0), "Cavern_Stalagmites_A41", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (11223.324, 2267.3618, 976.9187), (0.0, -77.80309795044751, 0.0), (2.0, 2.0, 2.0), "Cavern_Stalagmites_A42", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (11140.688, 1725.2999, 1095.6066), (0.0, -77.80309795044751, 0.0), (2.0, 2.0, 2.0), "Cavern_Stalagmites_A43", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (11301.96, 1946.5924, 1020.36865), (0.0, 175.77602690620273, -0.0), (2.0, 2.0, 2.0), "Cavern_Stalagmites_A44", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (11291.019, 935.30896, 873.71936), (0.0, -70.74438464130043, 0.0), (2.0, 2.0, 2.0), "Cavern_Stalagmites_A45", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (7544.88, 571.6999, 1007.4061), (0.0, 0.0, -0.0), (2.0, 2.0, 2.0), "Cavern_Stalagmites_A46_1661", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (7469.8477, 1356.3933, 691.9339), (0.0, 0.0, -0.0), (2.0, 2.0, 2.0), "Cavern_Stalagmites_A47", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (6223.5024, 1910.7191, 1068.9226), (0.0, 0.0, -0.0), (2.0, 2.0, 2.0), "Cavern_Stalagmites_A48", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (6253.621, 2328.9268, 703.28796), (0.0, 25.76364734533788, -0.0), (2.0, 2.0, 2.0), "Cavern_Stalagmites_A49", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (9619.667, 10645.404, 1248.2795), (-1.2011413421944825, -66.32166060985907, -2.957275213877125), (2.0, 2.0, 2.0), "Cavern_Stalagmites_A5_1316", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5643.763, 2493.6885, 678.35126), (2.6607098657788833e-09, 0.9664199013893064, -9.291931778043411), (2.0, 2.0, 2.0), "Cavern_Stalagmites_A50", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5807.7915, 2208.9753, 1097.5105), (-5.772766672366358, 42.20544906503602, 0.43213887820116587), (2.0, 2.0, 2.0), "Cavern_Stalagmites_A51", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5228.943, 4175.3867, 916.8751), (0.0, 40.501357464019435, -0.0), (2.0, 2.0, 2.0), "Cavern_Stalagmites_A52_1708", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4643.1997, 3179.8376, 913.7218), (0.0, -18.83749373682062, 0.0), (2.0, 2.0, 2.0), "Cavern_Stalagmites_A53", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (7036.343, 3949.4436, 1073.3527), (-5.926788327152239, 163.85184175156422, 7.964786282022193), (2.0, 2.0, 2.0), "Cavern_Stalagmites_A54", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5260.216, 3864.6448, 685.7272), (0.0, 25.199264437022837, -0.0), (2.0, 2.0, 2.0), "Cavern_Stalagmites_A55", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5210.0503, 5117.3145, 877.6594), (0.0, 55.91229007931644, -0.0), (2.0, 2.0, 2.0), "Cavern_Stalagmites_A56", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4386.604, 7691.6216, 1146.9204), (-1.2325440370539282, 122.2534641754016, -1.208587843606275), (2.0, 2.0, 2.0), "Cavern_Stalagmites_A57", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4747.8193, 7634.5884, 713.6623), (-1.4407346045953853, -22.306791642605877, -2.71209714576974), (2.0, 2.0, 2.0), "Cavern_Stalagmites_A58", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (6907.347, 8286.958, 1195.8958), (-0.7055359232592536, 11.932675632089486, 1.5754100416300303), (2.0, 2.0, 2.0), "Cavern_Stalagmites_A59", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (9868.881, 10100.29, 785.112), (0.0, 0.0, -0.0), (2.0, 2.0, 2.0), "Cavern_Stalagmites_A6_68", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (7342.897, 10034.661, 1020.91016), (-0.04940794231830717, -10.545653046277085, 1.7254292844409276), (2.0, 2.0, 2.0), "Cavern_Stalagmites_A60", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (6388.243, 10593.101, 1213.2006), (-0.04940795411545944, -10.545743685268652, -9.606170032931724), (2.0, 2.0, 2.0), "Cavern_Stalagmites_A61", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (7020.3438, 10601.507, 1309.134), (-0.04940795411545944, -10.545743685268652, -9.606170032931724), (2.0, 2.0, 2.0), "Cavern_Stalagmites_A62", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5338.8936, 10252.347, 1171.2462), (-0.04940795411545944, -10.545743685268652, -9.606170032931724), (2.0, 2.0, 2.0), "Cavern_Stalagmites_A63", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (6168.2046, 10647.939, 1400.4015), (-0.04940795411545944, -10.545743685268652, -9.606170032931724), (2.0, 2.0, 2.0), "Cavern_Stalagmites_A65", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1986.9122, 10907.366, 915.38916), (-0.04940795411545944, -10.545743685268652, -9.606170032931724), (2.0, 2.0, 2.0), "Cavern_Stalagmites_A66", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1567.509, 11366.119, 1136.8105), (-9.492584482675671, -109.16347145398542, 1.480993215104185), (2.0, 2.0, 2.0), "Cavern_Stalagmites_A67", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2295.9495, 11030.124, 766.8897), (-0.04940795411545944, -10.545743685268652, -9.606170032931724), (2.0, 2.0, 2.0), "Cavern_Stalagmites_A68", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3857.9175, 11190.172, 852.49915), (-8.877654650943649, -149.61820387842428, 2.8767516454397533), (2.0, 2.0, 2.0), "Cavern_Stalagmites_A69", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (10028.18, 10116.129, 879.8715), (2.129886602851431, -4.286346021853725, -0.15957638420511056), (2.0, 2.0, 2.0), "Cavern_Stalagmites_A7_1313", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (11043.022, 4326.469, 1285.4761), (-3.242950379262887, 96.34644147909545, 11.580893600363597), (2.0, 2.0, 2.0), "Cavern_Stalagmites_A71", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (8389.838, 10061.387, 1056.0499), (1.8502369769738, 29.98073406214276, 1.0671362622246625), (2.0, 2.0, 2.0), "Cavern_Stalagmites_A8", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (10872.083, 10081.751, 1052.1847), (0.8279488718215955, -67.1998931423681, -1.9688721531234112), (2.0, 2.0, 2.0), "Cavern_Stalagmites_A9", _folder)
if a: placed += 1
else: skipped += 1

# Batch 31: StaticMesh'Cavern_Stalagmites_B' (4 instances)
_mesh_path = "/Game/Art/Assets/Kits/Deco/Caveren/Cavern_Stalagmites_B"
_materials = ['/Game/Art/Assets/Kits/Deco/Caveren/Materials/Cavern_Stalagmites/Cavern_Stalagmites_Mat_B']
_folder = "Reconstruction/BD_BB_Chapter3_HeadwaterNexus/Meshes"
a = spawn_static_mesh(_mesh_path, _materials, (9968.706, 10087.587, 839.1369), (0.0, 81.40739757398605, -0.0), (2.0, 2.0, 2.0), "Cavern_Stalagmites_B_71", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (8115.455, 6567.0493, 1100.1772), (0.0, 0.0, -0.0), (1.5, 1.5, 1.5), "Cavern_Stalagmites_B6_103", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (8365.164, 4267.917, 950.49304), (0.0, 0.0, -0.0), (2.0, 2.0, 2.0), "Cavern_Stalagmites_B7_376", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (6068.837, 6909.2793, 960.0297), (3.100630447291012, 0.0, -0.0), (2.0, 2.0, 2.0), "Cavern_Stalagmites_B8_813", _folder)
if a: placed += 1
else: skipped += 1

# Batch 32: StaticMesh'Cavern_Stalagmites_C' (34 instances)
_mesh_path = "/Game/Art/Assets/Kits/Deco/Caveren/Cavern_Stalagmites_C"
_materials = ['/Game/Art/Assets/Kits/Deco/Caveren/Materials/Cavern_Stalagmites/Cavern_Stalagmites_Mat_C']
_folder = "Reconstruction/BD_BB_Chapter3_HeadwaterNexus/Meshes"
a = spawn_static_mesh(_mesh_path, _materials, (5542.897, 10134.127, 1081.475), (-3.0578000676377415, -10.134580729731008, -7.788786561020853), (2.0, 2.0, 2.0), "Cavern_Stalagmites_A64", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3627.3855, 10903.445, 801.7758), (-0.7700195194165338, -149.21197614641378, 2.8425425280410272), (2.0, 2.0, 2.0), "Cavern_Stalagmites_A70", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (6058.1123, 5660.2114, 888.08984), (-6.687744008641486, -13.795928350089818, 1.6378750236553172), (2.0, 2.0, 2.0), "Cavern_Stalagmites_C_783", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (9730.701, 4034.8923, 1037.8925), (1.1659240099062253e-07, 110.45260062453195, 2.5162968190316763), (2.0, 2.0, 2.0), "Cavern_Stalagmites_C10_339", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (9693.885, 3548.9849, 931.6905), (5.440355419410195, 0.0, -0.0), (2.0, 2.0, 2.0), "Cavern_Stalagmites_C11_368", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (9426.544, 3385.0403, 790.29755), (0.0, -47.53845164344263, 0.0), (2.0, 2.0, 2.0), "Cavern_Stalagmites_C12", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (8352.935, 4170.92, 919.48505), (0.0, 0.0, -0.0), (2.0, 2.0, 2.0), "Cavern_Stalagmites_C13_379", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (10719.187, 9785.932, 919.40924), (3.4305570585695397, 22.0614697001849, 1.3892241756604216), (2.0, 2.0, 2.0), "Cavern_Stalagmites_C14", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (10224.803, 10211.917, 1004.6089), (3.430557078290748, 22.06146969714991, 1.3892240742963198), (2.0, 2.0, 2.0), "Cavern_Stalagmites_C15", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (8321.59, 4228.5913, 982.21155), (0.0, -5.9116514183238476, 0.0), (1.5, 1.5, 1.5), "Cavern_Stalagmites_C16", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (6007.8193, 8253.323, 1008.6444), (0.0, 0.0, -0.0), (2.0, 2.0, 2.0), "Cavern_Stalagmites_C17_857", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (8633.335, 10281.288, 1058.9502), (0.0, 0.0, -0.0), (2.0, 2.0, 2.0), "Cavern_Stalagmites_C18_1319", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (8717.677, 9722.947, 759.94666), (0.0, 0.0, -0.0), (2.0, 2.0, 2.0), "Cavern_Stalagmites_C19", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (6463.8965, 5795.5854, 1166.837), (0.0, -77.58972050173621, 0.0), (2.0, 2.0, 2.0), "Cavern_Stalagmites_C2_790", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (10810.604, 10016.324, 1031.4318), (0.0, 0.0, -0.0), (2.0, 2.0, 2.0), "Cavern_Stalagmites_C20", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (9612.274, 10319.489, 1071.8398), (2.0425608470189482, -14.785184868745343, 3.715440910520775e-08), (2.0, 2.0, 2.0), "Cavern_Stalagmites_C21", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (10111.981, 7701.67, 818.6859), (-1.6493530938097651, -0.1648864973144711, 5.709349421253712), (2.0, 2.0, 2.0), "Cavern_Stalagmites_C22_1382", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (10517.425, 7310.8994, 988.647), (-3.4939878973427083, -24.524870991180215, 1.5519851215933674e-06), (2.0, 2.0, 2.0), "Cavern_Stalagmites_C23_1388", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (10955.402, 4677.4604, 1243.5125), (0.0, 0.0, -0.0), (2.0, 2.0, 2.0), "Cavern_Stalagmites_C24_1579", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (10949.183, 4424.1235, 1245.7222), (0.0, -148.45584188447936, 0.0), (2.0, 2.0, 2.0), "Cavern_Stalagmites_C25", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (11014.592, 1552.6365, 1159.0029), (0.0, 0.0, -0.0), (2.0, 2.0, 2.0), "Cavern_Stalagmites_C26_1627", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (7757.645, 740.6103, 853.56995), (0.0, 0.0, -0.0), (2.0, 2.0, 2.0), "Cavern_Stalagmites_C27_1658", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (7668.8125, 453.0899, 1038.244), (0.0, 0.0, -0.0), (2.0, 2.0, 2.0), "Cavern_Stalagmites_C28", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4821.741, 3217.6528, 821.3811), (0.0, 0.0, -0.0), (2.0, 2.0, 2.0), "Cavern_Stalagmites_C29_1705", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (10262.891, 5246.82, 914.0958), (-1.5160215858262736, -75.31442227148092, 4.320195153495601), (1.9576756, 1.9576756, 1.9576756), "Cavern_Stalagmites_C3_23", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (10191.118, 9928.135, 853.452), (0.0, 0.0, -0.0), (2.0, 2.0, 2.0), "Cavern_Stalagmites_C4_1308", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (8495.656, 9708.954, 867.8273), (-2.2237242926317977, -0.02621459997049259, 0.6770953050520362), (2.0, 2.0, 2.0), "Cavern_Stalagmites_C5_51", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (8220.838, 7461.4, 824.9455), (0.0, 0.0, -0.0), (2.0, 2.0, 2.0), "Cavern_Stalagmites_C6_191", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (8844.009, 5915.0557, 885.7147), (0.0, 23.59316468328338, -0.0), (2.0, 2.0, 2.0), "Cavern_Stalagmites_C7_95", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (7926.093, 3576.8262, 880.004), (0.0, 0.0, -0.0), (2.0, 2.0, 2.0), "Cavern_Stalagmites_C8_314", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (9365.241, 4401.666, 1185.9344), (0.0, 0.0, -0.0), (2.0, 2.0, 2.0), "Cavern_Stalagmites_C9_336", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (6023.045, 8564.277, 888.87775), (-4.024504931179577, -77.3709317942696, 2.345810963681659), (2.0, 2.0, 2.0), "Cavern_Stalagmites_D3_860", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (7017.0396, 8793.375, 996.9066), (-4.024505017093573, -77.37093177281449, 2.3458104884795405), (2.0, 2.0, 2.0), "Cavern_Stalagmites_D4", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (6267.7925, 10230.369, 938.3056), (-2.5679015422776703, -103.69614392587333, 3.8867089982209904), (2.0, 2.0, 2.0), "Cavern_Stalagmites_D6", _folder)
if a: placed += 1
else: skipped += 1

# Batch 33: StaticMesh'Cavern_Stalagmites_D' (8 instances)
_mesh_path = "/Game/Art/Assets/Kits/Deco/Caveren/Cavern_Stalagmites_D"
_materials = ['/Game/Art/Assets/Kits/Deco/Caveren/Materials/Cavern_Stalagmites/Cavern_Stalagmites_Mat_D']
_folder = "Reconstruction/BD_BB_Chapter3_HeadwaterNexus/Meshes"
a = spawn_static_mesh(_mesh_path, _materials, (7757.7837, 3551.196, 852.83), (4.366265915662176, 0.0, -0.0), (2.0, 2.0, 2.0), "Cavern_Stalagmites_D_317", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (7753.676, 8002.943, 1048.2085), (-2.651765330997471e-07, -88.82204737854875, 3.4284842502486192), (2.0, 2.0, 2.0), "Cavern_Stalagmites_D10", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (7773.6504, 7478.6216, 1089.8469), (-2.9372258116617465, -29.90033487945342, 9.906215408970148), (2.0, 2.0, 2.0), "Cavern_Stalagmites_D11", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (9382.022, 4229.4067, 1152.1069), (0.0, -33.987060313516054, 0.0), (2.0, 2.0, 2.0), "Cavern_Stalagmites_D2_333", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (8254.404, 7540.2847, 696.0795), (0.0, -76.1523739948857, 0.0), (2.0, 2.0, 2.0099885), "Cavern_Stalagmites_D5_116", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4984.2524, 7021.0234, 840.5314), (-6.907317592229289, 58.869701834148266, 10.539347360180303), (1.853966, 1.853966, 2.515537), "Cavern_Stalagmites_D7", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (7377.6255, 3436.0244, 827.2112), (1.3031522101246389, 9.478917452389924, 2.1210654212364273), (2.0, 2.0, 2.0), "Cavern_Stalagmites_D8", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (8167.2646, 8468.475, 699.5812), (0.0, -88.82214495580584, 0.0), (2.0, 2.0, 2.0), "Cavern_Stalagmites_D9", _folder)
if a: placed += 1
else: skipped += 1

# Batch 34: StaticMesh'Cavern_Stalagmites_E' (9 instances)
_mesh_path = "/Game/Art/Assets/Kits/Deco/Caveren/Cavern_Stalagmites_E"
_materials = ['/Game/Art/Assets/Kits/Deco/Caveren/Materials/Cavern_Stalagmites/Cavern_Stalagmites_Mat_C']
_folder = "Reconstruction/BD_BB_Chapter3_HeadwaterNexus/Meshes"
a = spawn_static_mesh(_mesh_path, _materials, (8204.48, 8449.21, 822.97626), (0.0, 0.0, -0.0), (2.0, 2.0, 2.0), "Cavern_Stalagmites_E_199", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4841.1675, 2088.1606, 1070.0033), (0.0, 93.28441135885124, -0.0), (3.437362, 3.437362, 3.437362), "Cavern_Stalagmites_E2", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (7752.3164, 7952.65, 1174.5331), (0.0, 0.0, -0.0), (2.0, 2.0, 2.0), "Cavern_Stalagmites_E3", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (8172.521, 7286.319, 1029.7222), (0.0, 0.0, -0.0), (2.0, 2.0, 2.0), "Cavern_Stalagmites_E4", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (6040.174, 8357.811, 1026.5457), (0.0, -151.1701024881421, 0.0), (2.0, 2.0, 2.0), "Cavern_Stalagmites_E5_869", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (8535.616, 10566.595, 1325.9354), (0.0, 0.0, -0.0), (2.0, 2.0, 2.0), "Cavern_Stalagmites_E6_1345", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (7048.387, 8669.2, 1084.6666), (0.0, -151.1701024881421, 0.0), (2.0, 2.0, 2.0), "Cavern_Stalagmites_E7", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (10871.891, 8425.669, 1121.7456), (0.0, -76.27966406972135, 0.0), (2.0, 2.0, 2.0), "Cavern_Stalagmites_E8_1392", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (7292.35, 3177.442, 852.9782), (0.0, 0.0, -0.0), (2.0, 2.0, 2.0), "Cavern_Stalagmites_E9_1552", _folder)
if a: placed += 1
else: skipped += 1

# Batch 35: StaticMesh'Cavern_Stalagmites_G' (1 instances)
_mesh_path = "/Game/Art/Assets/Kits/Deco/Caveren/Cavern_Stalagmites_G"
_materials = ['/Game/Art/Assets/Kits/Deco/Caveren/Materials/Cavern_Stalagmites/Cavern_Stalagmites_Mat_F']
_folder = "Reconstruction/BD_BB_Chapter3_HeadwaterNexus/Meshes"
a = spawn_static_mesh(_mesh_path, _materials, (8141.5767, 8351.416, 768.38367), (0.0, -81.34252988172594, 0.0), (2.0, 2.0, 2.0), "Cavern_Stalagmites_G_202", _folder)
if a: placed += 1
else: skipped += 1

# Batch 36: StaticMesh'Cavern_Trim_A' (11 instances)
_mesh_path = "/Game/Art/Assets/Kits/Deco/Caveren/Cavern_Trim_A"
_materials = ['/Game/Art/Assets/Kits/Deco/Caveren/Materials/Cavern_Trim/Cavern_Trim_A_MAT']
_folder = "Reconstruction/BD_BB_Chapter3_HeadwaterNexus/Meshes"
a = spawn_static_mesh(_mesh_path, _materials, (8889.434, 5798.1245, 673.1468), (0.0, -59.705379691259715, 0.0), (1.0, 1.0, 1.0), "Cavern_Trim_A_26", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (8790.658, 8420.201, 675.0), (0.0, -173.76670086958865, 0.0), (1.0, 1.0, 1.0), "Cavern_Trim_A11_39", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (8826.295, 9004.308, 680.26404), (0.0, 134.05508252688986, -0.0), (1.0, 1.0, 1.0), "Cavern_Trim_A12", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (8924.438, 9034.2295, 685.0), (0.0, 104.44501143746544, -0.0), (0.7565889, 0.7565889, 0.7565889), "Cavern_Trim_A13", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (8927.409, 8546.556, 680.26404), (0.0, 160.0247106393581, -0.0), (1.0, 1.0, 1.0), "Cavern_Trim_A14", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (9624.537, 5178.321, 668.909), (0.0, -41.27929391169678, 0.0), (1.0, 1.0, 1.0), "Cavern_Trim_A2_110", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (10582.917, 6100.0566, 668.909), (0.0, 79.91319025401614, -0.0), (1.0, 1.0, 1.0), "Cavern_Trim_A3", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3372.0132, 11079.731, 669.6115), (0.0, 167.32557085157606, -0.0), (1.0, 1.0, 1.0), "Cavern_Trim_A5_145", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5558.478, 2644.1587, 690.0), (0.0, -5.000091899981231, 0.0), (0.19544257, 0.42294243, 0.71979), "Cavern_Trim_A7_42", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (8173.0283, 1359.0358, 670.0), (0.0, -164.9999525275666, 0.0), (0.2883051, 0.39023465, 1.0893365), "Cavern_Trim_A8_147", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (7925.2847, 1469.6477, 670.0), (0.0, 155.00009338950497, -0.0), (0.288305, 0.390235, 1.089337), "Cavern_Trim_A9", _folder)
if a: placed += 1
else: skipped += 1

# Batch 37: StaticMesh'Cavern_Trim_B' (2 instances)
_mesh_path = "/Game/Art/Assets/Kits/Deco/Caveren/Cavern_Trim_B"
_materials = ['/Game/Art/Assets/Kits/Deco/Caveren/Materials/Cavern_Trim/Cavern_Trim_A_MAT']
_folder = "Reconstruction/BD_BB_Chapter3_HeadwaterNexus/Meshes"
a = spawn_static_mesh(_mesh_path, _materials, (9072.004, 1076.6771, 687.60785), (4.923856653463913, 19.96204377244901, -0.8703917837459048), (1.0712965, 1.0712965, 1.9937167), "Cavern_Trim_B4_74", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2158.057, 2446.556, 695.8144), (0.0, -122.93205854598013, 0.0), (1.0, 1.0, 1.186067), "Cavern_Trim_B5", _folder)
if a: placed += 1
else: skipped += 1

# Batch 38: StaticMesh'Cavern_Trim_C' (11 instances)
_mesh_path = "/Game/Art/Assets/Kits/Deco/Caveren/Cavern_Trim_C"
_materials = ['/Game/Art/Assets/Kits/Deco/Caveren/Materials/Cavern_Trim/Cavern_Trim_A_MAT']
_folder = "Reconstruction/BD_BB_Chapter3_HeadwaterNexus/Meshes"
a = spawn_static_mesh(_mesh_path, _materials, (5524.7197, 8518.183, 755.73956), (-2.110870239959961, -155.08368988338114, 4.533623696600234), (1.3362979, 1.3362979, 2.5185084), "Cavern_Trim_C_94", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (6772.476, 3586.6423, 676.44604), (0.0, -110.7022341007153, 0.0), (1.0, 1.0, 1.0), "Cavern_Trim_C10_99", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (9383.198, 1680.5354, 689.9238), (6.134220002191346e-08, 149.99996844719138, 5.000082009331149), (1.0, 0.7238639, 1.8490525), "Cavern_Trim_C13_71", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5350.569, 7054.2095, 701.00635), (-0.23043820196542827, 33.74459130837138, 0.6437381837096516), (1.0, 1.0, 1.1101315), "Cavern_Trim_C2", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1926.3785, 9136.111, 666.5064), (0.13441113017692563, 89.09289274741604, 2.4369896365239714), (1.0, 1.0, 1.4478363), "Cavern_Trim_C3", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (8840.486, 6535.003, 680.15753), (0.0, 27.03164961757787, -0.0), (1.0, 1.0, 1.0), "Cavern_Trim_C4_57", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (9842.15, 7802.602, 673.5621), (0.0, -144.59995063448042, 0.0), (1.0, 1.0, 1.0), "Cavern_Trim_C5_59", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (10802.051, 6821.395, 656.69885), (0.9290156536921443, 150.18332444480413, 3.165351788545479e-06), (1.0, 1.0, 1.0), "Cavern_Trim_C6_101", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (9232.517, 8250.476, 679.2802), (0.10741452385293462, -133.0602174773696, 0.8865160738139862), (1.0, 1.0, 1.0), "Cavern_Trim_C7", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (8277.551, 7269.8096, 672.5799), (-1.2964172378580172, 0.10817542079731392, -0.002532959117577435), (1.0, 1.0, 1.0), "Cavern_Trim_C8_106", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (6715.4897, 2131.06, 676.24524), (0.0, 65.34749584245941, -0.0), (1.0, 1.0, 1.0), "Cavern_Trim_C9_80", _folder)
if a: placed += 1
else: skipped += 1

# Batch 39: StaticMesh'Cavern_Trim_D' (25 instances)
_mesh_path = "/Game/Art/Assets/Kits/Deco/Caveren/Cavern_Trim_D"
_materials = ['/Game/Art/Assets/Kits/Deco/Caveren/Materials/Cavern_Trim/Cavern_Trim_A_MAT']
_folder = "Reconstruction/BD_BB_Chapter3_HeadwaterNexus/Meshes"
a = spawn_static_mesh(_mesh_path, _materials, (10621.176, 7219.3013, 666.45105), (-2.8481946288803493e-08, 99.4679572809122, 0.9515621780656135), (1.0, 1.0, 0.89814776), "Cavern_Trim_D_86", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4800.9697, 2898.5151, 615.87286), (-3.5751336031145353, -112.38309309914094, 0.14548635344398578), (1.0, 1.0, 1.0), "Cavern_Trim_D10", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5675.5527, 4633.79, 753.685), (1.3495152090893352, 176.73480867631525, 4.141110040686589), (1.0, 1.0, 1.0), "Cavern_Trim_D11", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (6872.874, 3889.8293, 666.56683), (-0.44271841323903666, 131.3228407604124, 1.95202739838383), (1.0, 1.0, 1.0), "Cavern_Trim_D12", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (6496.876, 4404.6157, 663.62256), (-0.442718433179457, 131.32284076470378, 1.952027910704199), (1.0, 1.0, 1.0), "Cavern_Trim_D13", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2662.6953, 3205.4866, 713.7878), (0.0, -176.8985851245724, 0.0), (1.0, 1.0, 1.0), "Cavern_Trim_D14_127", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3104.4653, 2944.0068, 697.4963), (1.1752980467259773, -154.13461897194748, 1.014228842548106e-06), (1.0, 1.0, 1.0), "Cavern_Trim_D16", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2854.1992, 11099.583, 673.99023), (0.32085495223301114, -178.63547336380054, 0.68071689471164), (1.0, 1.0, 1.0), "Cavern_Trim_D17_151", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4395.4946, 8264.51, 697.8856), (0.0, 14.202499863765544, -0.0), (1.0, 1.0, 1.0), "Cavern_Trim_D19_177", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (7273.537, 1943.8346, 675.28546), (0.0, 0.0, -0.0), (1.0, 1.0, 1.0), "Cavern_Trim_D2_87", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (6732.043, 2084.6445, 660.0), (0.0, -9.999969569001227, 0.0), (1.0, 1.0, 1.0), "Cavern_Trim_D22_48", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (8241.19, 2956.9858, 665.0), (0.0, -64.99990383297576, 0.0), (1.0, 1.0, 1.2128966), "Cavern_Trim_D23_54", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (9196.953, 3187.5476, 675.0), (0.0, 124.99999625358713, -0.0), (1.0, 1.0, 1.0949683), "Cavern_Trim_D24_67", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (8378.624, 3074.1514, 665.0), (0.0, -50.000000322548, 0.0), (0.4999145, 0.4999145, 1.3276812), "Cavern_Trim_D25_131", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (8377.344, 1259.273, 675.0), (0.0, -105.00002109988785, 0.0), (0.292209, 0.292209, 0.8074094), "Cavern_Trim_D26_144", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (7031.944, 2184.7798, 685.0), (0.0, -0.0001525878854640202, 0.0), (0.4056069, 0.48497808, 0.6939687), "Cavern_Trim_D27_151", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (799.1166, 9674.482, 675.0), (0.0, -114.28042503107346, 0.0), (1.0, 1.0, 0.7953324), "Cavern_Trim_D28_169", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3343.0327, 10552.682, 668.6444), (-0.06442259737856036, -174.9997751118111, 3.2781278843970587), (1.0, 1.0, 1.0), "Cavern_Trim_D29_5", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (7713.3867, 1368.418, 660.60474), (0.0, -32.69036840150109, 0.0), (1.0, 1.0, 1.0), "Cavern_Trim_D3", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (8419.788, 676.45337, 660.6048), (0.0, -10.624572365039333, 0.0), (1.0, 1.0, 1.0), "Cavern_Trim_D4", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (7646.896, 820.6303, 660.60486), (0.0, -55.31848488652625, 0.0), (1.0, 1.0, 1.0), "Cavern_Trim_D5", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (8823.85, 1162.206, 633.2436), (0.0, -10.624572365039333, 0.0), (1.0, 1.0, 1.0), "Cavern_Trim_D6", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (7623.6177, 2923.292, 642.3199), (0.0, -126.8051092531334, 0.0), (1.0, 1.0, 1.0), "Cavern_Trim_D7", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (6746.4385, 3060.2773, 673.80975), (0.5349562426335908, -155.2280700444893, 3.533595891945249), (0.96997786, 0.96997786, 0.96997786), "Cavern_Trim_D8", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4961.62, 3496.7283, 654.4585), (-3.578247257198105, -110.05140646059212, 2.4842678860898335), (1.0, 1.0, 1.0), "Cavern_Trim_D9_102", _folder)
if a: placed += 1
else: skipped += 1

# Batch 40: StaticMesh'Cavern_Trim_E' (5 instances)
_mesh_path = "/Game/Art/Assets/Kits/Deco/Caveren/Cavern_Trim_E"
_materials = ['/Game/Art/Assets/Kits/Deco/Caveren/Materials/Cavern_Trim/Cavern_Trim_A_MAT']
_folder = "Reconstruction/BD_BB_Chapter3_HeadwaterNexus/Meshes"
a = spawn_static_mesh(_mesh_path, _materials, (4107.17, 2843.4194, 730.0), (0.0, 169.9999215004284, -0.0), (1.0, 1.5840218, 1.0), "Cavern_Trim_E_29", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2801.5938, 2893.9182, 730.0), (0.0, -59.99999989158382, 0.0), (1.0, 1.479352, 0.8604685), "Cavern_Trim_E4", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5867.2363, 4128.9775, 730.0), (0.0, -165.00004804796816, 0.0), (1.0, 1.0, 1.0), "Cavern_Trim_E6_45", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (8587.381, 3516.6333, 720.0), (0.0, 149.99999400439492, -0.0), (1.5505491, 1.5505491, 1.5505491), "Cavern_Trim_E7_63", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (9136.943, 2928.1257, 738.15216), (0.0, 109.99999274422221, -0.0), (1.550549, 2.0405068, 1.6796951), "Cavern_Trim_E8", _folder)
if a: placed += 1
else: skipped += 1

# Batch 41: StaticMesh'SM_Grass_Dungeon_02' (103 instances)
_mesh_path = "/Game/Art/Assets/Kits/Deco/Flora/SM_Grass_Dungeon_02"
_materials = ['/Game/Art/Assets/Kits/Deco/Flora/Materials/MI_Grass_Mushroom']
_folder = "Reconstruction/BD_BB_Chapter3_HeadwaterNexus/Meshes"
a = spawn_static_mesh(_mesh_path, _materials, (4891.5015, 7730.7495, 796.4333), (-3.016631833015876, 3.311938328153099, 4.8218040082578755), (1.855837, 1.855837, 1.855837), "SM_Grass_Dungeon_37", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4781.241, 7936.781, 754.60364), (-3.0166011724187975, -76.68816507539746, 4.821841273780431), (1.855837, 1.855837, 1.855837), "SM_Grass_Dungeon_38", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5805.5454, 7726.5312, 949.75446), (11.958096448039472, 3.380794689436291, 5.697566962285811), (1.6183981, 1.6183981, 1.6183981), "SM_Grass_Dungeon_39", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5817.894, 7776.214, 902.60815), (11.958097145956541, 3.380794730687681, 5.6975669938734965), (1.618398, 1.618398, 1.618398), "SM_Grass_Dungeon_42", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5817.894, 7995.3584, 868.4273), (11.958097145956541, 3.380794730687681, 5.6975669938734965), (1.618398, 1.618398, 1.618398), "SM_Grass_Dungeon_43", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5963.697, 7848.9126, 1098.2942), (17.56362182721032, 70.15096029790529, 10.47046526231557), (1.618398, 1.618398, 1.618398), "SM_Grass_Dungeon_44", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5893.7314, 7503.2207, 957.3544), (11.958097145956541, 3.380794730687681, 5.6975669938734965), (1.618398, 1.618398, 1.618398), "SM_Grass_Dungeon_45", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5437.3584, 8314.731, 798.4599), (17.56362182721032, 70.15096029790529, 10.47046526231557), (1.618398, 1.618398, 1.618398), "SM_Grass_Dungeon_46", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (9886.349, 7777.792, 826.4822), (6.0552081382415395, -67.78234932826095, -3.503784500079611), (1.486159, 1.486159, 1.486159), "SM_Grass_Dungeon_101", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (10545.212, 8750.077, 879.9522), (6.0552081382415395, -67.78234932826095, -3.503784500079611), (1.486159, 1.486159, 1.486159), "SM_Grass_Dungeon_105", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (10814.406, 6489.0845, 1128.4819), (6.0552081382415395, -67.78234932826095, -3.503784500079611), (1.486159, 1.486159, 1.486159), "SM_Grass_Dungeon_112", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (10814.406, 6460.4414, 1128.4819), (6.0552081382415395, -67.78234932826095, -3.503784500079611), (1.486159, 1.486159, 1.486159), "SM_Grass_Dungeon_113", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (7943.1245, 8197.371, 1054.6637), (0.9402485514965323, -67.03075673195404, 8.760034202758352), (1.486159, 1.486159, 1.486159), "SM_Grass_Dungeon_132", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (7993.324, 8252.977, 1028.702), (0.9402481375026398, -67.03075681184251, 8.760035034318589), (1.486159, 1.486159, 1.486159), "SM_Grass_Dungeon_133", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (9482.865, 5870.182, 733.7367), (0.9402481375026398, -67.03075681184251, 8.760035034318589), (1.486159, 1.486159, 1.486159), "SM_Grass_Dungeon_135", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (9544.271, 5800.4126, 721.00574), (0.9402478449585716, 16.00665152595844, 8.760295747741903), (1.486159, 1.486159, 1.486159), "SM_Grass_Dungeon_136", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (10698.495, 6515.325, 1002.66565), (6.0552081382415395, -67.78234932826095, -3.503784500079611), (1.486159, 1.486159, 1.486159), "SM_Grass_Dungeon_148", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (8063.2246, 720.85187, 712.6261), (3.7083419664512594, 111.09576795152303, -8.688476464357066), (1.486159, 1.486159, 1.486159), "SM_Grass_Dungeon_160", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (8189.1084, 1325.8356, 767.82947), (-2.4132080692886198, -172.215365479944, -5.2795106505113605), (1.486159, 1.486159, 1.486159), "SM_Grass_Dungeon_161", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (9791.087, 3483.8372, 890.27734), (15.873558077241643, 73.61267534748714, -11.27450800936786), (1.486159, 1.486159, 1.486159), "SM_Grass_Dungeon_162", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (9458.111, 4760.384, 1036.8164), (3.475614857358051, 146.19605717984513, -6.967833134669489), (1.486159, 1.486159, 1.486159), "SM_Grass_Dungeon_163", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (10497.604, 3895.0864, 1058.5723), (11.478390613728413, -66.13413803642328, -13.298702807532477), (1.486159, 1.486159, 1.486159), "SM_Grass_Dungeon_164", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (10481.871, 4889.211, 1196.7091), (1.3305277763998131, -65.55926201720446, -4.909942633697277), (1.486159, 1.486159, 1.486159), "SM_Grass_Dungeon_165", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (9857.392, 7986.371, 898.90924), (1.3305281038422454, -161.84661066201815, -4.909943191014372), (1.486159, 1.486159, 1.486159), "SM_Grass_Dungeon_166", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (10340.803, 8198.819, 878.2452), (0.975670874953039, -84.50711239329215, -1.1949463303694057), (1.486159, 1.486159, 1.486159), "SM_Grass_Dungeon_167", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (7083.9033, 9845.549, 899.6062), (9.354716684511777, 8.722901543885135, -10.322510840281833), (1.486159, 1.486159, 1.486159), "SM_Grass_Dungeon_168", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (10514.681, 7460.3857, 997.961), (1.330527855073562, -102.9201894560813, -4.909941967711826), (1.486159, 1.486159, 1.486159), "SM_Grass_Dungeon_169", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (9987.247, 7504.423, 679.8057), (9.384904325611654, -11.532256989423987, -5.171265246451958), (1.486159, 1.486159, 1.486159), "SM_Grass_Dungeon_170", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (10074.344, 5338.963, 857.8849), (7.600258764528642, 32.1832710776492, 3.0805124443917267), (1.486159, 1.486159, 1.486159), "SM_Grass_Dungeon_171", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (8881.914, 5995.6636, 876.55066), (3.475615173486842, -162.4294015438526, -6.967835744701034), (1.486159, 1.486159, 1.486159), "SM_Grass_Dungeon_173", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (9024.782, 6428.158, 708.3272), (8.598374950951838, 127.72044220279943, -13.53622458131339), (1.486159, 1.486159, 1.486159), "SM_Grass_Dungeon_174", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (8213.552, 7525.577, 844.2681), (8.598373291389839, 139.49522482891044, -13.537078550524221), (1.486159, 1.486159, 1.486159), "SM_Grass_Dungeon_175", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (8420.995, 8755.081, 744.2491), (-0.06182849308021153, -59.913153032800466, -3.4295047278893778), (1.486159, 1.486159, 1.486159), "SM_Grass_Dungeon_176", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (7656.007, 8408.085, 1270.9005), (21.18665821739076, 128.6910092147134, -17.796230802096833), (1.486159, 1.486159, 1.486159), "SM_Grass_Dungeon_177", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (8611.103, 9899.241, 1036.2323), (5.987138134634555, -139.63719811623517, 2.2816567476214904), (1.486159, 1.486159, 1.486159), "SM_Grass_Dungeon_178", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (9770.703, 10073.883, 850.12146), (6.585580918282769, -8.98294091617533, 0.6011877531540984), (1.486159, 1.486159, 1.486159), "SM_Grass_Dungeon_179", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (9523.253, 10567.703, 1237.5415), (9.384904325611654, -11.532256989423987, -5.171265246451958), (1.486159, 1.486159, 1.486159), "SM_Grass_Dungeon_180", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (10654.234, 8910.537, 797.1364), (4.2691767254, -115.10852268231615, -6.286468089040402), (1.486159, 1.486159, 1.486159), "SM_Grass_Dungeon_182", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (11072.812, 9024.432, 779.7717), (2.3865363956397543, -127.92328424472313, -3.2308042649004767), (1.486159, 1.486159, 1.486159), "SM_Grass_Dungeon_183", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (8725.91, 9647.981, 786.22205), (2.8469448980028282, -162.43419776147232, 19.174117303981927), (1.486159, 1.486159, 1.486159), "SM_Grass_Dungeon_184", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (10087.76, 9638.627, 790.94934), (2.212445562762823, -143.51876235565416, -7.8120109683906485), (1.486159, 1.486159, 1.486159), "SM_Grass_Dungeon_185", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (11585.491, 9754.92, 792.9842), (10.484394198098991, -124.32319385540062, -6.974577676827551), (1.486159, 1.486159, 1.486159), "SM_Grass_Dungeon_186", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (11112.185, 9991.123, 936.24365), (5.126905737914595, 52.827699202293154, -11.288238197805486), (1.486159, 1.486159, 1.486159), "SM_Grass_Dungeon_188", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (12104.326, 9016.227, 790.817), (8.330322789314641, -121.45045347464014, -5.627379669383171), (1.486159, 1.486159, 1.486159), "SM_Grass_Dungeon_192", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (7547.291, 8846.566, 1008.33984), (13.799043254312599, -48.530001307724135, 13.152885949506677), (1.486159, 1.486159, 1.486159), "SM_Grass_Dungeon_199", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (7157.792, 10212.955, 1277.5181), (5.465728403244394, -24.79620120771646, -38.9317295566592), (1.486159, 1.486159, 1.486159), "SM_Grass_Dungeon_206", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5699.141, 10294.997, 1212.9918), (7.417749332196095, 8.679260994190564, -10.622284296109887), (1.486159, 1.486159, 1.486159), "SM_Grass_Dungeon_212", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (10311.975, 5647.4126, 936.86975), (-1.4851691980777804, 74.09067936828801, 22.045859678060772), (1.486159, 1.486159, 1.486159), "SM_Grass_Dungeon_213", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5332.39, 9919.261, 924.80365), (-5.660187051638194, 5.4577929596200585, -20.06909310214586), (1.486159, 1.486159, 1.486159), "SM_Grass_Dungeon_214", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5115.7915, 9752.578, 911.9652), (-0.6387945879239062, -102.71483828520776, -18.141904554644395), (1.486159, 1.486159, 1.486159), "SM_Grass_Dungeon_216", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4777.1577, 9919.261, 904.0666), (5.823916806600119, 5.459402539543743, -18.973542096933482), (1.486159, 1.486159, 1.486159), "SM_Grass_Dungeon_218", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5063.528, 10320.862, 1230.9396), (0.7329670069778039, -130.1081738601309, -7.743804282110497), (1.486159, 1.486159, 1.486159), "SM_Grass_Dungeon_220", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4809.9917, 10500.283, 1130.995), (8.716208317089851, -44.08690622817978, -9.273131184979654), (1.486159, 1.486159, 1.486159), "SM_Grass_Dungeon_228", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3684.9473, 10639.605, 690.09985), (8.71620783258599, -15.760556644011164, -9.273131611356911), (1.486159, 1.486159, 1.486159), "SM_Grass_Dungeon_230", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4355.0234, 11286.579, 1359.6072), (10.561316771160953, -12.057800681702727, -9.67196657700192), (1.486159, 1.486159, 1.486159), "SM_Grass_Dungeon_234", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4190.1597, 10780.946, 1129.0269), (9.885126954143406, -24.631865771773253, -5.46597300648164), (1.486159, 1.486159, 1.486159), "SM_Grass_Dungeon_240", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2141.6257, 11104.6455, 1081.3176), (2.8323429852312274, -17.24996920021145, -4.25271608611865), (1.486159, 1.486159, 1.486159), "SM_Grass_Dungeon_243", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3416.1667, 11321.656, 781.4288), (6.753328064644782, 8.687122548816616, 1.226453504931553), (1.486159, 1.486159, 1.486159), "SM_Grass_Dungeon_245", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3519.8687, 11435.105, 810.0192), (-1.1436157036648555, -98.53084910025807, -6.451630032741259), (1.486159, 1.486159, 1.486159), "SM_Grass_Dungeon_247", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2915.5125, 11609.572, 773.9397), (1.6200322029808643, -114.32555127995313, 6.310834600531406), (1.486159, 1.486159, 1.486159), "SM_Grass_Dungeon_251", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2412.5034, 11200.551, 940.1371), (-4.782653896692364, 91.3560961574425, 1.1938857231981028), (1.486159, 1.486159, 1.486159), "SM_Grass_Dungeon_252", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (6738.1147, 8709.764, 1073.4576), (5.417671864342888, 9.579847243847057, 16.62458728588413), (1.486159, 1.486159, 1.486159), "SM_Grass_Dungeon_260", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (6367.186, 8516.048, 1112.8177), (7.5441544424155875, 8.019558638702785, 2.8664323311565227), (1.486159, 1.486159, 1.486159), "SM_Grass_Dungeon_262", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3876.6243, 8498.861, 854.29083), (-5.278228753723346, -10.659882703389355, 1.0675744441978905), (1.486159, 1.486159, 1.486159), "SM_Grass_Dungeon_264", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4233.1133, 8571.228, 715.0642), (7.095913571449838, -31.26288210261872, -2.6348873686375653), (1.486159, 1.486159, 1.486159), "SM_Grass_Dungeon_266", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5466.7676, 4463.355, 878.3125), (-0.12490858433449305, -67.86880714834373, 13.196829087455194), (1.486159, 1.486159, 1.486159), "SM_Grass_Dungeon_270", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (10641.864, 3634.1777, 1123.0051), (-6.637512101047445, -150.37967555258734, -6.121978866354567), (1.486159, 1.486159, 1.486159), "SM_Grass_Dungeon_272", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (11120.847, 3885.1047, 1303.4927), (0.3519182792411484, -111.95482363666525, -8.95260666870234), (1.486159, 1.486159, 1.486159), "SM_Grass_Dungeon_279", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (9656.642, 3859.5088, 1044.0957), (9.384904129983017, -32.496855694093995, -5.171264989064971), (1.486159, 1.486159, 1.486159), "SM_Grass_Dungeon_285", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (11062.245, 3391.0425, 834.3099), (4.238101752988192, 56.58323662371921, -16.71240120093199), (1.486159, 1.486159, 1.486159), "SM_Grass_Dungeon_292", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (10922.593, 2682.5232, 801.4342), (16.05470634772424, 68.65197048284432, 14.463396505335115), (1.486159, 1.486159, 1.486159), "SM_Grass_Dungeon_300", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (10541.9375, 1693.0007, 871.23785), (13.597300431885897, 79.11476525295402, 6.370442201093169), (1.486159, 1.486159, 1.486159), "SM_Grass_Dungeon_305", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (10863.5625, 914.0917, 802.1627), (0.7713337456003923, -173.3232988114294, 3.4913592166672447), (1.486159, 1.486159, 1.486159), "SM_Grass_Dungeon_308", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (10967.787, 611.6295, 772.10846), (0.7713400697015576, 2.3891086749013253, 3.491381192473632), (1.486159, 1.486159, 1.486159), "SM_Grass_Dungeon_313", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (7921.468, 3320.3455, 848.51013), (1.3897520128594214, 113.2742902671343, 9.425022032519827), (1.486159, 1.486159, 1.486159), "SM_Grass_Dungeon_317", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (10652.997, 9745.372, 921.1097), (3.985203545727093, 56.61081186164598, 7.936263744914825), (1.486159, 1.486159, 1.486159), "SM_Grass_Dungeon_319", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (7581.3535, 3565.6191, 950.65796), (11.788327231792028, 50.13021631008014, -5.687652443951785), (1.486159, 1.486159, 1.486159), "SM_Grass_Dungeon_321", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (9144.92, 3852.4795, 819.78656), (10.25222985308767, -15.124784295006888, -13.222687034994303), (1.486159, 1.486159, 1.486159), "SM_Grass_Dungeon_324", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (6743.213, 2036.8794, 843.8915), (15.539933553345149, 153.95123880914966, -13.385374663870985), (1.486159, 1.486159, 1.486159), "SM_Grass_Dungeon_331", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5062.2603, 3588.5042, 862.2345), (12.281496774021262, 111.63383632914592, -8.87588341639603), (1.486159, 1.486159, 1.486159), "SM_Grass_Dungeon_337", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (6144.3926, 4382.0156, 826.32043), (17.41622901393586, 35.48016353606148, -16.06863520936865), (1.486159, 1.486159, 1.486159), "SM_Grass_Dungeon_342", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5441.4307, 5280.9897, 842.66766), (3.6102737867848913, -108.97485789378918, 6.584883761456599), (1.486159, 1.486159, 1.486159), "SM_Grass_Dungeon_348", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5401.091, 6394.349, 842.66766), (3.6102734292494936, -133.99039093000553, 6.584938597411855), (1.486159, 1.486159, 1.486159), "SM_Grass_Dungeon_351", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5723.667, 5634.1074, 832.20667), (4.3838880569418395, 98.88699699209387, 1.7227159615277925), (1.486159, 1.486159, 1.486159), "SM_Grass_Dungeon_355", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3380.1245, 2989.7195, 901.22833), (15.618107428872253, 51.81363970514856, -21.78018222366546), (1.486159, 1.486159, 1.486159), "SM_Grass_Dungeon_359", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3738.607, 1994.3364, 848.8129), (15.877073740535597, -82.55218488113262, -15.94442694097094), (1.486159, 1.486159, 1.486159), "SM_Grass_Dungeon_363", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2605.9956, 1672.4137, 797.0085), (7.358483334229871, 149.19752281089103, -5.727692600765815), (1.486159, 1.486159, 1.486159), "SM_Grass_Dungeon_366", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3806.279, 2347.4993, 777.9316), (8.209079938856963, 33.940984445237596, 27.204530533197556), (1.486159, 1.486159, 1.486159), "SM_Grass_Dungeon_370", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3020.5913, 3193.831, 891.3016), (-0.5982969209370625, 22.410218778053263, -14.67727421479702), (1.486159, 1.486159, 1.486159), "SM_Grass_Dungeon_373", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2571.756, 2948.003, 777.14557), (7.867823473454465, 22.63347313163568, -11.164154974055945), (1.486159, 1.486159, 1.486159), "SM_Grass_Dungeon_377", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3677.5144, 1538.3514, 885.50104), (11.195091785978102, 24.33971800946841, 8.260254958783314), (1.486159, 1.486159, 1.486159), "SM_Grass_Dungeon_381", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1104.662, 2565.65, 778.7593), (7.358483334229871, 149.19752281089103, -5.727692600765815), (1.486159, 1.486159, 1.486159), "SM_Grass_Dungeon_389", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1302.0399, 2154.1533, 1181.0466), (12.995670949106524, 171.96565223667952, -19.860994485886565), (1.486159, 1.486159, 1.486159), "SM_Grass_Dungeon_396", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2826.4517, 759.6241, 780.77094), (7.358483025394823, 96.31458571352007, -5.727691507080914), (1.486159, 1.486159, 1.486159), "SM_Grass_Dungeon_399", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (11626.948, 9031.268, 790.817), (8.330321903799888, -170.7981179583547, -5.627379360869946), (1.486159, 1.486159, 1.486159), "SM_Grass_Dungeon_408", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1155.5895, 8435.477, 843.31006), (7.2566779962456485, -110.81686016335027, -2.9392392266001104), (1.486159, 1.486159, 1.486159), "SM_Grass_Dungeon_413", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1401.8799, 8164.3, 963.2296), (-1.7317502817391548, -43.43487206371706, -1.0024412191844239), (1.486159, 1.486159, 1.486159), "SM_Grass_Dungeon_416", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (827.3007, 11281.016, 825.48773), (3.3992445045660835, -97.67807490056089, -10.874144738555467), (1.486159, 1.486159, 1.486159), "SM_Grass_Dungeon_421", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2229.323, 10807.436, 841.62494), (18.179835340486072, 69.75804404462137, -2.6731883031458925), (1.486159, 1.486159, 1.486159), "SM_Grass_Dungeon_428", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (6737.248, 10484.664, 1262.962), (10.348671120978167, 5.521111053123116, -18.534393234419948), (1.486159, 1.486159, 1.486159), "SM_Grass_Dungeon_460", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2656.0457, 11419.049, 811.1811), (8.819081172754794, 7.742830771309094, -5.252197157237803), (1.486159, 1.486159, 1.486159), "SM_Grass_Dungeon_599", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1583.6267, 8778.915, 761.4377), (5.995675941666569, 31.541801599783888, -5.309600411413905), (1.486159, 1.486159, 1.486159), "SM_Grass_Dungeon_1021", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (973.4658, 9178.322, 708.95087), (5.320832958229513, 72.86885600962863, -0.7698366500367724), (1.486159, 1.486159, 1.486159), "SM_Grass_Dungeon_1030", _folder)
if a: placed += 1
else: skipped += 1

# Batch 42: StaticMesh'SM_Grass_Dungeon_04' (103 instances)
_mesh_path = "/Game/Art/Assets/Kits/Deco/Flora/SM_Grass_Dungeon_04"
_materials = ['/Game/Art/Assets/Kits/Deco/Flora/Materials/MI_Grass_Mushroom']
_folder = "Reconstruction/BD_BB_Chapter3_HeadwaterNexus/Meshes"
a = spawn_static_mesh(_mesh_path, _materials, (5663.4175, 8041.441, 771.783), (5.358747720202294, 100.06304498812892, 5.853692797391888), (1.5411589, 1.5411589, 1.5411589), "SM_Grass_Dungeon_5", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4831.3076, 7981.482, 762.2357), (0.0, -70.00008551529459, 0.0), (1.5490563, 1.5490563, 1.5490563), "SM_Grass_Dungeon_6", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5682.849, 7662.295, 751.3129), (5.358748120867946, 70.06300741794189, 5.85371529353635), (1.541159, 1.541159, 1.541159), "SM_Grass_Dungeon_7", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5296.89, 7076.956, 918.17706), (0.9065380068073253, -44.69458218636932, 10.280849201799548), (1.5, 1.4, 1.5), "SM_Grass_Dungeon_9", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5559.9497, 8351.866, 796.94116), (5.3587470377831785, -44.93701276686371, 5.853814445867247), (1.5, 1.4, 1.5), "SM_Grass_Dungeon_10", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5559.9497, 8539.704, 834.2077), (5.358747512615681, 170.06301361788363, 5.85395031713333), (1.5, 1.4, 1.5), "SM_Grass_Dungeon_11", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (6154.7134, 8828.583, 842.5233), (0.05448678067596925, 170.08168082380973, 2.975257017463494), (1.5, 1.4, 1.5), "SM_Grass_Dungeon_69", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (6464.623, 8515.888, 1088.3279), (2.9791232061140067, 169.89492915112905, -0.5842589593685084), (1.5, 1.4, 1.5), "SM_Grass_Dungeon_72", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (6474.0576, 9013.426, 842.5233), (0.054487020336434815, 170.08168082995041, 2.975256996648868), (1.5, 1.4, 1.5), "SM_Grass_Dungeon_73", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5199.472, 9580.04, 845.9126), (0.054487020336434815, 170.08168082995041, 2.975256996648868), (1.5, 1.4, 1.5), "SM_Grass_Dungeon_74", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5765.7856, 9731.584, 822.4012), (0.054487082030331764, -20.874449273067547, 2.975269491887316), (1.5, 1.4, 1.5), "SM_Grass_Dungeon_75", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5051.7676, 10120.947, 1135.6108), (0.05448700026723394, -173.70723043439142, 2.9752632936169174), (1.5, 1.4, 1.5), "SM_Grass_Dungeon_76", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4301.2573, 9789.226, 744.924), (0.8060452835524767, 45.35546824391713, 3.9079649075178162), (1.5, 1.4, 1.5), "SM_Grass_Dungeon_77", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4020.7383, 8073.018, 876.6962), (-1.513549672755104, -31.00283769572992, 0.9094584612641132), (1.549056, 1.549056, 1.549056), "SM_Grass_Dungeon_79", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3816.492, 8031.364, 879.8187), (-1.5135496587891166, 29.269356416272203, 0.9094595974486064), (1.549056, 1.549056, 1.549056), "SM_Grass_Dungeon_80", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4452.6064, 8265.808, 710.16296), (-1.5135496847891876, -31.00283768773645, 0.9094579887810192), (1.549056, 1.549056, 1.549056), "SM_Grass_Dungeon_81", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3698.594, 8932.245, 709.4649), (-1.5135498756189327, 44.321356708017134, 0.909459001509573), (1.549056, 1.549056, 1.549056), "SM_Grass_Dungeon_83", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (9794.301, 7836.3164, 787.2681), (-3.3127439501037115, -173.23912850368993, -0.2814941130343189), (1.0, 1.0, 1.0), "SM_Grass_Dungeon_102", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (10454.18, 8585.033, 906.2054), (1.5100045365015828, -173.24804504357746, 0.28976257665905575), (1.0, 1.0, 1.0), "SM_Grass_Dungeon_104", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (9553.852, 8028.586, 754.7141), (-0.307525651261997, 125.66890829249702, 3.3754752192805664), (1.0, 1.0, 1.0), "SM_Grass_Dungeon_106", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (8152.6035, 7714.9146, 881.3578), (8.489951741855911, 124.77590083729956, -9.056121430975013), (1.0, 1.0, 1.0), "SM_Grass_Dungeon_125", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (8152.6035, 7933.701, 866.13544), (8.634363285253364, -138.46960211684888, -6.486144525382563), (1.0, 1.0, 1.0), "SM_Grass_Dungeon_126", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (8063.0986, 7426.3276, 1074.4945), (3.208371258656731, -86.3422324013485, 20.907156070263806), (1.0, 1.0, 1.0), "SM_Grass_Dungeon_127", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (8504.441, 7038.071, 823.8907), (-0.6273193382398712, 33.77335003585334, -6.405701463552607), (1.0, 1.0, 1.0), "SM_Grass_Dungeon_128", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (8309.587, 7273.9375, 1030.6857), (3.6221081970383837, 69.49487560721843, -7.9933773388046605), (1.0, 1.0, 1.0), "SM_Grass_Dungeon_130", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (8784.332, 6244.375, 868.9226), (-0.6273193382398712, 33.77335003585334, -6.405701463552607), (1.0, 1.0, 1.0), "SM_Grass_Dungeon_134", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (8497.294, 6734.619, 838.6079), (-8.394927707520084, 34.187317081853834, -11.650055184595073), (1.0, 1.0, 1.0), "SM_Grass_Dungeon_137", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (9895.032, 8434.645, 802.61646), (1.5100049705801146, -173.24804503764616, 0.28976300418452344), (1.0, 1.0, 1.0), "SM_Grass_Dungeon_138", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (10429.156, 8927.731, 799.8414), (1.959068902428191, 170.60168588365352, -3.7074581836640914), (1.0, 1.0, 1.0), "SM_Grass_Dungeon_150", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (10870.382, 8921.459, 895.32404), (-6.334503517086057, 170.5485858792186, -2.331024367713722), (1.0, 1.0, 1.0), "SM_Grass_Dungeon_152", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (9885.279, 9759.662, 784.13586), (-0.06585692573501878, 142.30377406421965, -2.1419070166096277), (1.0, 1.0, 1.0), "SM_Grass_Dungeon_157", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (11362.402, 9741.429, 780.1092), (0.4538818198789434, 162.66541071267292, -0.47708129178825165), (1.0, 1.0, 1.0), "SM_Grass_Dungeon_159", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (9755.687, 7279.8447, 712.8331), (-0.30752549972587967, 125.66890829224232, 3.375475012386163), (1.0, 1.0, 1.0), "SM_Grass_Dungeon_181", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (9486.379, 8176.327, 762.1382), (-3.464783293855825, -127.98193408822654, 4.062887962904776), (1.0, 1.0, 1.0), "SM_Grass_Dungeon_193", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (8457.074, 9481.589, 885.49097), (8.69127743165612, 133.05334049929525, -2.139312212056615), (1.0, 1.0, 1.0), "SM_Grass_Dungeon_196", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (8470.345, 8952.305, 746.16046), (6.752659166663089, 142.16900511002845, -0.741790618256396), (1.0, 1.0, 1.0), "SM_Grass_Dungeon_197", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (7698.881, 9030.18, 824.34204), (6.0025816905957985, 142.06719738812976, 1.148905731342544), (1.0, 1.0, 1.0), "SM_Grass_Dungeon_200", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (7261.6104, 9142.839, 862.49146), (6.002582346920951, 142.06719742403266, 1.1489058718644225), (1.0, 1.0, 1.0), "SM_Grass_Dungeon_201", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (6971.361, 9088.463, 864.6132), (6.002583044389809, 173.79382313045627, 1.1489072587637865), (1.0, 1.0, 1.0), "SM_Grass_Dungeon_202", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (6808.0776, 9748.176, 873.2822), (6.002583038100938, 173.79382312421023, 1.1489071438400886), (1.0, 1.0, 1.0), "SM_Grass_Dungeon_203", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (7266.942, 9531.374, 871.7427), (-0.6651916655553886, -97.51147152592621, 1.4389888909076338), (1.0, 1.0, 1.0), "SM_Grass_Dungeon_204", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (6086.3247, 10071.305, 957.4609), (10.37403160990172, 173.91705849985686, 2.470060621074029), (1.0, 1.0, 1.0), "SM_Grass_Dungeon_207", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (6329.204, 9836.717, 856.7245), (3.771990519622197, 173.81445131720207, 1.391916355563954), (1.0, 1.0, 1.0), "SM_Grass_Dungeon_210", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (8761.834, 9500.39, 792.60254), (5.163938372920664, 91.96188541133266, -7.318451460224372), (1.0, 1.0, 1.0), "SM_Grass_Dungeon_221", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (8285.968, 9373.621, 826.5538), (17.917568011338442, 142.2459590474883, 2.2912065407551006), (1.0, 1.0, 1.0), "SM_Grass_Dungeon_222", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5443.703, 9719.467, 844.8998), (5.580432023098248, 173.41174139616567, -2.634125005917291), (1.0, 1.0, 1.0), "SM_Grass_Dungeon_235", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4804.209, 9623.497, 844.89984), (5.5804316787348744, 173.4117414030706, -2.6341249849200477), (1.0, 1.0, 1.0), "SM_Grass_Dungeon_236", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (6138.468, 9836.717, 856.7245), (3.771990910195973, -144.6501417053535, 1.3919171005771533), (1.0, 1.0, 1.0), "SM_Grass_Dungeon_237", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3977.5771, 10742.631, 944.8113), (-5.198608925301383, -129.5001654912919, -5.948028060924666), (1.0, 1.0, 1.0), "SM_Grass_Dungeon_241", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (9723.469, 3683.9988, 1055.6033), (0.9209488831942706, -156.5426585793808, 3.5596848904987555), (1.1875, 1.1875, 1.1875), "SM_Grass_Dungeon_287", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (9540.949, 3262.7153, 811.41986), (5.023337136076534, 127.40616588472975, 12.55070923718019), (1.1875, 1.1875, 1.1875), "SM_Grass_Dungeon_288", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (8130.639, 3708.2341, 850.5212), (5.653586041344286, -121.57254444479416, 5.738385298055944), (1.1875, 1.1875, 1.1875), "SM_Grass_Dungeon_289", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (9496.303, 3636.793, 1018.23157), (-14.90182400324195, -157.20066855766382, 5.532677979968087), (1.1875, 1.1875, 1.1875), "SM_Grass_Dungeon_290", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (11298.06, 3346.3132, 823.8097), (8.184136663560238, 163.679204432856, 9.502593823133873), (1.1875, 1.1875, 1.1875), "SM_Grass_Dungeon_293", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (10741.022, 3265.8062, 850.0292), (8.184136663560238, 163.679204432856, 9.502593823133873), (1.5, 1.5, 1.5), "SM_Grass_Dungeon_294", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (10928.739, 1813.6003, 1074.4064), (6.440143438690781, -70.01354634765443, -4.85290472431309), (1.549056, 1.549056, 1.549056), "SM_Grass_Dungeon_295", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (11164.801, 2054.6597, 1046.8824), (13.53771607127031, -69.55264686216482, -2.201050203503152), (1.549056, 1.549056, 1.549056), "SM_Grass_Dungeon_296", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (11339.529, 2755.1501, 814.4948), (-3.1343076036795576, 163.4291957372043, -3.949920198973476), (1.549056, 1.549056, 1.549056), "SM_Grass_Dungeon_297", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (11055.352, 801.53064, 817.63904), (4.080436316503516, -70.09232367338149, -5.7129216398156135), (1.549056, 1.549056, 1.549056), "SM_Grass_Dungeon_309", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (11006.6455, 555.8766, 788.3077), (6.0712720446213275, 102.21301614170186, 1.2962147396561952), (1.549056, 1.549056, 1.549056), "SM_Grass_Dungeon_310", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (10524.135, 2067.6052, 805.7184), (7.272156705116696, -133.20884185878054, 0.16306884990219053), (1.549056, 1.549056, 1.549056), "SM_Grass_Dungeon_314", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (8340.838, 3867.284, 752.6742), (-10.03857266389097, -130.29079331941654, 1.8644890677875), (1.549056, 1.549056, 1.549056), "SM_Grass_Dungeon_318", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (9173.619, 3611.053, 783.6041), (-13.800597340716884, -118.82073161250206, -3.058593160387029), (1.1875, 1.1875, 1.1875), "SM_Grass_Dungeon_325", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (7774.0015, 595.12573, 1005.4626), (12.286790871879587, -81.25277732982791, -0.08630491166219531), (1.1875, 1.1875, 1.1875), "SM_Grass_Dungeon_326", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (7403.664, 1509.9629, 865.0635), (6.810389538214184, -69.13526502312841, 20.044739458061954), (1.1875, 1.1875, 1.1875), "SM_Grass_Dungeon_327", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (7233.839, 1331.9053, 979.6825), (0.0, 0.0, -0.0), (1.1875, 1.1875, 1.1875), "SM_Grass_Dungeon_332", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5864.2007, 2462.681, 787.71387), (5.439419012902039, -29.459135440559564, 9.52701278300943), (1.1875, 1.1875, 1.1875), "SM_Grass_Dungeon_333", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (6700.9175, 2366.6157, 691.9475), (0.25559252901429697, 163.28991740575418, -8.110106603195245), (1.1875, 1.1875, 1.1875), "SM_Grass_Dungeon_334", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5049.216, 3384.1572, 841.3236), (-13.649717167985004, 3.2965083210710797, -13.716520307750017), (1.1875, 1.1875, 1.1875), "SM_Grass_Dungeon_338", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4927.072, 3518.7312, 938.06525), (-16.33218613693845, 4.829742293970146, -19.12253057533037), (1.1875, 1.1875, 1.1875), "SM_Grass_Dungeon_339", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (6914.0923, 3426.8489, 681.511), (-1.1584471336685422, 3.06143218112264, -4.100738565190714), (1.1875, 1.1875, 1.1875), "SM_Grass_Dungeon_343", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5465.253, 2630.628, 823.9828), (-9.324737153946613, 5.86095834430362, 14.601408867337332), (1.1875, 1.1875, 1.1875), "SM_Grass_Dungeon_344", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5405.9497, 4685.131, 911.26886), (-15.467680212111683, 54.33015037129425, -14.317351841318423), (1.1875, 1.1875, 1.1875), "SM_Grass_Dungeon_345", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5402.5547, 6698.143, 887.8901), (0.8143571888270401, -115.60713798474936, 13.708645784348475), (1.5, 1.4, 1.5), "SM_Grass_Dungeon_352", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5603.8223, 4122.905, 734.4681), (-16.332186212582364, 4.829741827923655, -19.122530509048765), (1.1875, 1.1875, 1.1875), "SM_Grass_Dungeon_356", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3172.3403, 2788.004, 746.05334), (7.216177542850577, 10.010069507596075, -16.00762837281893), (1.1875, 1.1875, 1.1875), "SM_Grass_Dungeon_360", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3419.5515, 1447.1953, 816.1627), (2.279821210840979, 70.63638324587673, 2.880748450442595), (1.1875, 1.1875, 1.1875), "SM_Grass_Dungeon_367", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3012.1511, 2907.7026, 746.05347), (7.216177542850577, 10.010069507596075, -16.00762837281893), (1.1875, 1.1875, 1.1875), "SM_Grass_Dungeon_378", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3751.0872, 1793.4194, 893.29297), (-0.35678102243088683, 70.65194273161578, 3.8069961353956545), (1.1875, 1.1875, 1.1875), "SM_Grass_Dungeon_382", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3597.9421, 1828.687, 826.3727), (2.279820770379708, 70.63638321905445, 2.8807482780297122), (1.1875, 1.1875, 1.1875), "SM_Grass_Dungeon_383", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1370.6501, 3212.4468, 1015.75024), (-9.366118082330344, -50.035517152773686, -6.286407389132844), (1.1875, 1.1875, 1.1875), "SM_Grass_Dungeon_384", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2492.2578, 1857.5773, 800.4545), (0.0, 117.08942858159509, -0.0), (1.1875, 1.1875, 1.1875), "SM_Grass_Dungeon_385", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2360.0837, 2136.5557, 775.1727), (0.0, 117.08942858159509, -0.0), (1.1875, 1.1875, 1.1875), "SM_Grass_Dungeon_386", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (990.9242, 2750.8135, 782.2053), (0.0, 117.08942858159509, -0.0), (1.1875, 1.1875, 1.1875), "SM_Grass_Dungeon_390", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (971.45807, 3099.274, 788.5955), (3.356887750709262, 117.13976723883626, 1.7192557202217382), (1.1875, 1.1875, 1.1875), "SM_Grass_Dungeon_391", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1862.2296, 2886.9446, 800.86127), (5.134703548413759, 15.389277302891914, -4.647888178635719), (1.1875, 1.1875, 1.1875), "SM_Grass_Dungeon_392", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2432.4448, 3114.086, 1053.6294), (-5.207305438142188, -70.45458766449873, -21.80069014874136), (1.1875, 1.1875, 1.1875), "SM_Grass_Dungeon_393", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2905.4678, 962.0552, 784.217), (0.0, 64.2064774060571, -0.0), (1.1875, 1.1875, 1.1875), "SM_Grass_Dungeon_400", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2818.6194, 1437.9415, 784.217), (0.0, 64.2064774060571, -0.0), (1.1875, 1.1875, 1.1875), "SM_Grass_Dungeon_401", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3376.819, 973.73206, 784.21783), (0.0, 64.2064774060571, -0.0), (1.1875, 1.1875, 1.1875), "SM_Grass_Dungeon_402", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1046.2297, 11044.972, 824.34534), (0.8237003427775473, -52.0630483366026, -2.0889587296393874), (1.549056, 1.549056, 1.549056), "SM_Grass_Dungeon_409", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1396.4272, 8987.119, 725.4349), (-1.513549646973623, -96.05007650470729, 0.9094608328113745), (1.549056, 1.549056, 1.549056), "SM_Grass_Dungeon_410", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1501.3376, 8261.353, 975.9405), (-7.113678024164002, 0.0, -0.0), (1.549056, 1.549056, 1.549056), "SM_Grass_Dungeon_417", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (988.59106, 8925.22, 723.9657), (0.9675305743869719, 53.00985095810278, 4.202934212593785), (1.549056, 1.549056, 1.549056), "SM_Grass_Dungeon_418", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (616.91974, 11536.306, 874.9898), (-18.537841599966782, -49.58108703568522, -17.881469691727972), (1.549056, 1.549056, 1.549056), "SM_Grass_Dungeon_422", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1562.2751, 10793.559, 839.8658), (-1.6078492652593097, -52.05026672598439, -3.984557940803779), (1.549056, 1.549056, 1.549056), "SM_Grass_Dungeon_423", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1734.489, 11191.132, 1087.2529), (-4.2159427055927265, 15.023655814668368, -10.7167661004642), (1.549056, 1.549056, 1.549056), "SM_Grass_Dungeon_424", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1402.6432, 11309.298, 1112.4395), (17.36805934533399, 13.615157160030193, -12.173615041531292), (1.549056, 1.549056, 1.549056), "SM_Grass_Dungeon_425", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (11685.158, 2834.4421, 814.4948), (-3.1343076036795576, 163.4291957372043, -3.949920198973476), (1.549056, 1.549056, 1.549056), "SM_Grass_Dungeon_750", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (12135.544, 2942.2954, 820.5807), (3.229026698735668, 163.42743380507386, -5.842376955601223), (1.549056, 1.549056, 1.549056), "SM_Grass_Dungeon_752", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (7420.082, 1722.9178, 739.0542), (6.81038997051932, -100.02365884397643, 20.044741285762836), (1.1875, 1.1875, 1.1875), "SM_Grass_Dungeon_817", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2835.2695, 3168.0913, 957.974), (0.0012228486428743721, 9.929652328621446, -17.27722080074679), (1.1875, 1.1875, 1.1875), "SM_Grass_Dungeon_938", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5017.6895, 7663.543, 690.07294), (0.0, -70.00008551529459, 0.0), (2.2661505, 2.2661505, 2.2661505), "SM_Grass_Dungeon_04_2", _folder)
if a: placed += 1
else: skipped += 1

# Batch 43: StaticMesh'SM_Grass_Dungeon_05' (171 instances)
_mesh_path = "/Game/Art/Assets/Kits/Deco/Flora/SM_Grass_Dungeon_05"
_materials = ['/Game/Art/Assets/Kits/Deco/Flora/Materials/MI_Grass_Mushroom']
_folder = "Reconstruction/BD_BB_Chapter3_HeadwaterNexus/Meshes"
a = spawn_static_mesh(_mesh_path, _materials, (8159.0205, 629.8645, 717.43024), (10.808645026363672, -153.10112577371478, 1.5724190172151), (1.0, 1.0, 1.0), "SM_Grass_Dungeon_12", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (9812.893, 3355.4734, 867.3495), (11.806486941948027, 172.3456437845935, 14.20732676740425), (1.0, 1.0, 1.0), "SM_Grass_Dungeon_13", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (9588.651, 4740.6484, 1043.7969), (9.123066475708981, -118.17921537041549, 1.1637279702942511), (1.0, 1.0, 1.0), "SM_Grass_Dungeon_15", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (10397.317, 3979.7585, 1042.695), (14.40191676503774, 32.13339181459462, 10.044374392265027), (1.0, 1.0, 1.0), "SM_Grass_Dungeon_16", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (10381.876, 4974.644, 1210.1674), (7.276767549336532, 29.64568813890715, -1.188049230066147), (1.0, 1.0, 1.0), "SM_Grass_Dungeon_17", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (9953.261, 8076.4077, 912.3675), (7.276767851775653, -66.64203655503458, -1.188049665057523), (1.0, 1.0, 1.0), "SM_Grass_Dungeon_18", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (10275.13, 8312.182, 896.0149), (3.6090847859843738, 10.557555966659221, -1.8767699000500442), (1.0, 1.0, 1.0), "SM_Grass_Dungeon_19", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (8298.499, 1397.091, 788.67773), (7.969784958087461, -77.5112056524047, -4.920318138850609), (1.0, 1.0, 1.0), "SM_Grass_Dungeon_20", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (10487.044, 7588.969, 1011.4192), (7.276767330742616, -7.715941966463174, -1.1880492913012755), (1.0, 1.0, 1.0), "SM_Grass_Dungeon_21", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (9858.7, 7473.746, 676.1839), (6.734822163976694, 84.68503391746471, 6.911451913872768), (1.0, 1.0, 1.0), "SM_Grass_Dungeon_22", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (10000.185, 5229.802, 865.767), (-1.2191163654851274, 127.0573993063358, 4.349926661457371), (1.0, 1.0, 1.0), "SM_Grass_Dungeon_23", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (8978.818, 6085.3286, 883.5311), (9.123066292826781, -66.80466260024303, 1.1637283119614827), (1.0, 1.0, 1.0), "SM_Grass_Dungeon_25", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (9142.826, 6369.4985, 698.1625), (15.031238458320688, -134.71177584084853, 7.127089340534353), (1.0, 1.0, 1.0), "SM_Grass_Dungeon_26", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (8341.082, 7492.2437, 834.1034), (15.031237986370646, -122.93685613528626, 7.127279510812446), (1.0, 1.0, 1.0), "SM_Grass_Dungeon_27", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (8313.645, 8830.168, 762.0293), (5.927309512910819, 35.097604661757536, -2.717834098768541), (1.0, 1.0, 1.0), "SM_Grass_Dungeon_28", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (7771.214, 8356.865, 1231.128), (16.914586942113964, -128.868521851536, 20.764758401856383), (1.0, 1.0, 1.0), "SM_Grass_Dungeon_29", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (8667.997, 10017.06, 1062.4316), (0.04241536268500734, -44.786988862729515, -2.824493339586429), (1.0, 1.0, 1.0), "SM_Grass_Dungeon_30", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (9643.284, 10039.485, 857.84546), (1.322153596712753, 86.19573132659158, 3.5537687328229506), (1.0, 1.0, 1.0), "SM_Grass_Dungeon_31", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (9394.706, 10537.026, 1233.9197), (6.734822945538076, 84.6850340302742, 6.911452090618945), (1.0, 1.0, 1.0), "SM_Grass_Dungeon_32", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (10414.014, 9774.365, 893.23285), (7.85336192326704, 50.49487347604742, 3.2170349014860324), (1.0, 1.0, 1.0), "SM_Grass_Dungeon_33", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (10654.216, 9042.607, 803.13), (8.366796917226823, -19.4174204977968, 1.8964341630145387), (1.0, 1.0, 1.0), "SM_Grass_Dungeon_34", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (11102.694, 9152.571, 792.6553), (5.509059320086855, -32.67416125731088, -0.28372168263544856), (1.0, 1.0, 1.0), "SM_Grass_Dungeon_35", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (8809.105, 9647.889, 798.71387), (10.677620775273278, 139.1281013464893, 0.3398426282196634), (1.0, 1.0, 1.0), "SM_Grass_Dungeon_36", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (10150.07, 9754.893, 799.7347), (10.08284138013116, -48.0493775213711, -0.027190778030275455), (1.0, 1.0, 1.0), "SM_Grass_Dungeon_47", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (11603.467, 9885.27, 805.74274), (9.268729642032344, -27.955782483486512, -1.5917970723353707), (1.0, 1.0, 1.0), "SM_Grass_Dungeon_48", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (11085.681, 9861.604, 935.5207), (13.235047701620644, 149.18938090088338, 3.2951466793303537), (1.0, 1.0, 1.0), "SM_Grass_Dungeon_49", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (12119.163, 9147.583, 788.9636), (7.295147321298817, -25.285035232630243, 5.905620816939073), (1.0, 1.0, 1.0), "SM_Grass_Dungeon_51", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (6614.9355, 10033.7, 980.8211), (11.786378703105534, 105.87059115604016, 7.480065468592715), (1.0, 1.0, 1.0), "SM_Grass_Dungeon_52", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (7429.8247, 8907.133, 1011.74365), (-11.498137654892641, 43.845060879067425, 9.920547055153543), (1.0, 1.0, 1.0), "SM_Grass_Dungeon_53", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (7028.8003, 10211.719, 1248.5714), (40.40111268436968, 76.51595958051861, 8.35478502639144), (1.0, 1.0, 1.0), "SM_Grass_Dungeon_54", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (6626.019, 10415.701, 1244.2241), (19.653968184961787, 104.6781551458695, 9.692293529016844), (1.0, 1.0, 1.0), "SM_Grass_Dungeon_55", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5589.929, 10220.647, 1208.1615), (12.315644634110733, 105.46795741551105, 5.550905151179843), (1.0, 1.0, 1.0), "SM_Grass_Dungeon_56", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5220.324, 9850.298, 937.61017), (22.909628993946956, 98.49839151115835, -7.2204592117279), (1.0, 1.0, 1.0), "SM_Grass_Dungeon_57", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5085.431, 9881.176, 916.33386), (20.631727904032036, -7.6212170312838134, -1.974731661370085), (1.0, 1.0, 1.0), "SM_Grass_Dungeon_58", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4664.795, 9850.298, 894.2028), (20.74392438850578, 103.05401385854901, 4.989817096170539), (1.0, 1.0, 1.0), "SM_Grass_Dungeon_59", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5097.0186, 10448.196, 1242.867), (10.152355533203586, -34.90497082912246, -1.52996893959446), (1.0, 1.0, 1.0), "SM_Grass_Dungeon_60", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4684.8555, 10542.482, 1124.7897), (10.835061167675013, 52.743960469438484, 6.705254982303714), (1.0, 1.0, 1.0), "SM_Grass_Dungeon_61", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3554.773, 10617.371, 683.89453), (10.83506264344407, 81.07009561638843, 6.705318662878017), (1.0, 1.0, 1.0), "SM_Grass_Dungeon_62", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4226.8657, 11255.835, 1349.1772), (10.998741457141797, 85.20325003336764, 8.619595060497682), (1.0, 1.0, 1.0), "SM_Grass_Dungeon_63", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2011.0498, 11087.085, 1092.2836), (6.485477708264124, 78.10182536269407, 0.25689802364849407), (1.0, 1.0, 1.0), "SM_Grass_Dungeon_64", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3305.073, 11250.422, 789.38525), (0.6871851359690703, 103.79592906674101, 3.666540810409948), (1.0, 1.0, 1.0), "SM_Grass_Dungeon_65", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3481.958, 11560.604, 827.10345), (9.029899141793825, -3.65744049531073, -3.540527499581709), (1.0, 1.0, 1.0), "SM_Grass_Dungeon_66", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2917.8408, 11739.676, 797.3175), (-3.9225164710396583, -19.43149234023365, -1.88684107400724), (1.0, 1.0, 1.0), "SM_Grass_Dungeon_67", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2544.817, 11347.628, 808.6665), (6.8736790252493725, 103.90789348161215, 6.355142796156869), (1.0, 1.0, 1.0), "SM_Grass_Dungeon_68", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (6625.812, 8644.313, 1097.6119), (-14.477236312324766, 103.3518135154292, 1.1463131642440996), (1.0, 1.0, 1.0), "SM_Grass_Dungeon_70", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (6254.8833, 8446.723, 1120.6222), (-1.0021054873258903, 102.92287352320254, 4.3120473518275455), (1.0, 1.0, 1.0), "SM_Grass_Dungeon_71", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3752.4143, 8467.6045, 887.0587), (1.8942576130194744, 84.18051667726341, -8.309021489767177), (1.0, 1.0, 1.0), "SM_Grass_Dungeon_78", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4101.8477, 8586.573, 718.6649), (4.472571728811791, 64.34543527568712, 4.3660744770712645), (1.0, 1.0, 1.0), "SM_Grass_Dungeon_82", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5377.6763, 4555.3, 911.2959), (-10.629854406544831, 27.234254285197004, -4.241058822719644), (1.0, 1.0, 1.0), "SM_Grass_Dungeon_85", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (10715.258, 3740.3374, 1151.6766), (9.126957645727499, -56.36557300583905, -9.113373504906052), (1.0, 1.0, 1.0), "SM_Grass_Dungeon_86", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (8177.3936, 771.68866, 712.4619), (3.744425898275328, -72.10478978475756, 6.746613542035573), (1.0, 1.0, 1.0), "SM_Grass_Dungeon_87", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (8165.693, 1448.4221, 774.40717), (9.650599492850096, 4.101669593027017, 2.950709094885165), (1.0, 1.0, 1.0), "SM_Grass_Dungeon_88", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (9912.877, 3456.123, 886.03687), (-8.269286491340315, -109.2709038641382, 9.938389261205872), (1.0, 1.0, 1.0), "SM_Grass_Dungeon_89", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (9522.456, 4867.4653, 1040.3676), (3.8775459105005012, -37.227355448566705, 5.0149342836272215), (1.0, 1.0, 1.0), "SM_Grass_Dungeon_90", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (10387.23, 3837.1785, 1049.4392), (-3.785369441191954, 111.27539800482913, 11.702641209290402), (1.0, 1.0, 1.0), "SM_Grass_Dungeon_91", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (10370.996, 4832.0757, 1204.5092), (5.890669085141196, 110.74570354178111, 2.8217484700287097), (1.0, 1.0, 1.0), "SM_Grass_Dungeon_92", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (9812.741, 8102.838, 906.7093), (5.8906690533148724, 14.458130430169659, 2.8217683241104594), (1.0, 1.0, 1.0), "SM_Grass_Dungeon_93", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (10218.125, 8180.944, 894.0621), (5.990232614799909, 91.33438155399014, -0.9281309070675413), (1.0, 1.0, 1.0), "SM_Grass_Dungeon_94", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (6473.0635, 10097.869, 975.49225), (13.17667053960161, 53.84224790555608, -4.563020427051368), (1.0, 1.0, 1.0), "SM_Grass_Dungeon_95", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (10024.273, 8509.229, 805.5681), (3.6090847859843738, 10.557555966659221, -1.8767699000500442), (1.0, 1.0, 1.0), "SM_Grass_Dungeon_96", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (7109.6436, 9723.289, 896.55444), (-1.8062438964583991, -174.25949064833932, 8.67245783163232), (1.0, 1.0, 1.0), "SM_Grass_Dungeon_103", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (10391.88, 7482.2563, 1005.76105), (5.890669301369958, 73.3844089249807, 2.821782014182299), (1.0, 1.0, 1.0), "SM_Grass_Dungeon_107", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (9967.306, 7381.3066, 687.8252), (-2.130431955859817, 164.8206325802119, 3.5971564446274513), (1.0, 1.0, 1.0), "SM_Grass_Dungeon_111", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (6974.921, 9771.199, 891.0445), (11.786378703105534, 105.87059115604016, 7.480065468592715), (1.0, 1.0, 1.0), "SM_Grass_Dungeon_114", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (10142.003, 5237.0317, 883.4008), (-0.9415892926803364, -152.46045977198654, -4.674773541610784), (1.0, 1.0, 1.0), "SM_Grass_Dungeon_117", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (10417.608, 5625.5825, 999.9785), (6.233394954537355, -112.49835814125916, -24.43081559223414), (1.0, 1.0, 1.0), "SM_Grass_Dungeon_121", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (8838.422, 6112.7744, 880.1018), (3.8775463298658788, 14.147322750492268, 5.01496523299032), (1.0, 1.0, 1.0), "SM_Grass_Dungeon_122", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (9118.287, 6510.473, 698.27673), (-0.8974911965025696, -54.83294231933332, 11.807282236778752), (1.0, 1.0, 1.0), "SM_Grass_Dungeon_123", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (8288.291, 7625.241, 834.21765), (-0.8974917754037842, -43.05776397095497, 11.807796662453825), (1.0, 1.0, 1.0), "SM_Grass_Dungeon_124", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (7743.8516, 8495.398, 1254.2407), (-13.313538030981373, -53.33630197740816, 16.45786297111922), (1.0, 1.0, 1.0), "SM_Grass_Dungeon_131", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (8527.808, 9989.426, 1059.6332), (4.400971109793657, 35.650993466575294, -4.2953797673459295), (1.0, 1.0, 1.0), "SM_Grass_Dungeon_139", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (9755.432, 9951.494, 870.2977), (0.26320808538487894, 166.6620497966419, -2.3011775891856803), (1.0, 1.0, 1.0), "SM_Grass_Dungeon_140", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (9503.312, 10444.587, 1245.5609), (-2.1304319106525647, 164.82063257788235, 3.5971567859911344), (1.0, 1.0, 1.0), "SM_Grass_Dungeon_143", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (10585.185, 9680.137, 902.95154), (-10.729553925687979, 130.20321423195114, 4.1575419965962706), (1.0, 1.0, 1.0), "SM_Grass_Dungeon_144", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (10538.763, 8958.075, 802.2544), (3.044051128792904, 61.384548897922194, 4.383215223661658), (1.0, 1.0, 1.0), "SM_Grass_Dungeon_149", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (10971.166, 9096.225, 791.3281), (4.725704228333302, 48.17621138656435, 1.2101783014101477), (1.0, 1.0, 1.0), "SM_Grass_Dungeon_151", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (8692.315, 9751.149, 853.87665), (-3.351776495878748, 13.273049086988317, -15.64956976065631), (1.0, 1.0, 1.0), "SM_Grass_Dungeon_153", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (10008.519, 9735.259, 792.5308), (5.187699263459635, 33.16150798960899, 5.784791965054009), (1.0, 1.0, 1.0), "SM_Grass_Dungeon_156", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (11477.585, 9817.874, 796.48334), (6.589070130607244, 53.41084625567221, 4.741116170645823), (1.0, 1.0, 1.0), "SM_Grass_Dungeon_158", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (11215.658, 9921.253, 930.5991), (2.4646929915451268, -130.02815687009883, 9.413772978431355), (1.0, 1.0, 1.0), "SM_Grass_Dungeon_187", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (11995.175, 9076.695, 797.76294), (-1.0498349437908336, 54.96288439126181, 3.980549428444816), (1.0, 1.0, 1.0), "SM_Grass_Dungeon_191", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (7457.1304, 8773.31, 1054.4242), (-8.015075873662052, 125.67625946341737, -13.995239324200806), (1.0, 1.0, 1.0), "SM_Grass_Dungeon_198", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (7123.874, 10110.167, 1215.0443), (2.584946218239569, 156.18691687787845, 36.9660721678717), (1.0, 1.0, 1.0), "SM_Grass_Dungeon_205", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (6759.176, 10363.33, 1242.5474), (-2.456207214642889, -176.35507505918244, 16.80349897216288), (1.0, 1.0, 1.0), "SM_Grass_Dungeon_208", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (10320.366, 5522.599, 979.6355), (-19.31073054552429, 169.9060515764921, -6.508941725483111), (1.0, 1.0, 1.0), "SM_Grass_Dungeon_209", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5724.762, 10172.737, 1209.0615), (0.14347491418705158, -174.2623185204993, 8.868505807710124), (1.0, 1.0, 1.0), "SM_Grass_Dungeon_211", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4994.442, 9773.724, 890.83136), (8.512135924584882, 75.33533298896752, 16.046349976313344), (1.0, 1.0, 1.0), "SM_Grass_Dungeon_215", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4797.3984, 9797.927, 881.978), (2.080140276578081, -176.3557657114483, 17.092765748767896), (1.0, 1.0, 1.0), "SM_Grass_Dungeon_217", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4964.0137, 10396.451, 1232.5067), (6.660710537895458, 46.554013702566444, 5.63141557967214), (1.0, 1.0, 1.0), "SM_Grass_Dungeon_219", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4727.842, 10406.102, 1130.1261), (-1.223754512712393, 132.79391946950102, 7.603189591828705), (1.0, 1.0, 1.0), "SM_Grass_Dungeon_227", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3657.3232, 10517.719, 689.23096), (-1.2236936851196871, 161.12023352735983, 7.603266549384281), (1.0, 1.0, 1.0), "SM_Grass_Dungeon_229", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4335.513, 11163.14, 1358.0953), (-3.044953013470534, 164.87188483571563, 8.095959598297355), (1.0, 1.0, 1.0), "SM_Grass_Dungeon_233", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2110.3042, 10984.021, 1090.7), (4.3494777834237315, 158.97940240654253, 2.261989914975855), (1.0, 1.0, 1.0), "SM_Grass_Dungeon_242", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3438.5222, 11200.592, 802.95593), (0.04825529265229846, -175.73961066242444, -2.907715070203572), (1.0, 1.0, 1.0), "SM_Grass_Dungeon_244", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3395.5537, 11447.277, 814.1931), (8.456968733777131, 77.94933362139925, 4.215593113910324), (1.0, 1.0, 1.0), "SM_Grass_Dungeon_246", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2803.285, 11654.358, 805.8577), (4.746001798443715, 60.645070226628, -8.389098916638032), (1.0, 1.0, 1.0), "SM_Grass_Dungeon_250", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2677.9734, 11296.256, 818.97943), (-1.5606995128832828, -175.89144404865883, 3.6409289744314153), (1.0, 1.0, 1.0), "SM_Grass_Dungeon_253", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (8316.834, 8686.413, 762.07196), (7.182188559963967, 116.1925113666967, -4.390013821263829), (1.0, 1.0, 1.0), "SM_Grass_Dungeon_254", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (6758.2163, 8598.479, 1126.6696), (-0.03076178874075959, -176.49146022736048, -18.276061059216048), (1.0, 1.0, 1.0), "SM_Grass_Dungeon_259", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (6387.2876, 8395.269, 1137.8773), (-0.8682251227420729, -176.6001641880613, -4.467407461980343), (1.0, 1.0, 1.0), "SM_Grass_Dungeon_261", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3861.8962, 8376.363, 874.20935), (12.056069205626882, 164.83263823069817, -3.6889032821780465), (1.0, 1.0, 1.0), "SM_Grass_Dungeon_263", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4172.6987, 8462.629, 728.34235), (-0.0125732246839339, 144.77733939543958, 0.9403634855723486), (1.0, 1.0, 1.0), "SM_Grass_Dungeon_265", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5361.7007, 4413.694, 924.2926), (5.8353311468633775, 106.36269552184709, -15.437985867785056), (1.0, 1.0, 1.0), "SM_Grass_Dungeon_269", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (10574.268, 3739.2087, 1127.2616), (13.919577453450552, 25.98993062087167, 3.5316201349257135), (1.0, 1.0, 1.0), "SM_Grass_Dungeon_271", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (11112.719, 4016.5562, 1315.0184), (11.390070211546627, -16.793792465004618, -1.8051147411732684), (1.0, 1.0, 1.0), "SM_Grass_Dungeon_277", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (11002.724, 3925.9067, 1302.3868), (7.110157858631754, 64.86107000837572, 6.823456346682697), (1.0, 1.0, 1.0), "SM_Grass_Dungeon_278", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (9525.628, 3876.855, 1040.4738), (6.734825360410024, 63.72094487247267, 6.911760680695575), (1.0, 1.0, 1.0), "SM_Grass_Dungeon_283", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (9593.973, 3751.6802, 1052.1151), (-2.1304011992449556, 143.85634769516687, 3.597210995185765), (1.0, 1.0, 1.0), "SM_Grass_Dungeon_284", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (11169.539, 3329.3872, 816.83777), (3.5876729385215627, -125.54482158286108, 14.783599231526418), (1.0, 1.0, 1.0), "SM_Grass_Dungeon_291", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (10921.541, 2550.3274, 801.03186), (-12.842926177051666, 160.21113266005838, 12.183159955325593), (1.0, 1.0, 1.0), "SM_Grass_Dungeon_298", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (11027.01, 2633.8125, 849.83466), (-10.388059587040335, -117.31050343436313, -15.038479652790299), (1.0, 1.0, 1.0), "SM_Grass_Dungeon_299", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (10660.185, 1668.885, 903.70245), (-7.189970109081042, -105.94109001758096, -7.3971852247333585), (1.0, 1.0, 1.0), "SM_Grass_Dungeon_304", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (10975.745, 980.2918, 824.74084), (-1.0402527989473693, -78.34647694772508, -2.4888003372943617), (1.0, 1.0, 1.0), "SM_Grass_Dungeon_306", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (10843.438, 1034.6932, 828.0192), (5.831231628469098, 1.9604763239646936, -5.6419367623732315), (1.0, 1.0, 1.0), "SM_Grass_Dungeon_307", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (10850.969, 553.9979, 794.6866), (-1.0402528018699544, 97.36623577188647, -2.4888002583204796), (1.0, 1.0, 1.0), "SM_Grass_Dungeon_311", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (10978.837, 489.8561, 797.96497), (5.831232242532961, 177.67299929487962, -5.641936305360213), (1.0, 1.0, 1.0), "SM_Grass_Dungeon_312", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (8014.55, 3230.3125, 875.12006), (-7.0032038543368005, -151.866387472763, -2.3847654814379706), (1.0, 1.0, 1.0), "SM_Grass_Dungeon_315", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (8028.481, 3372.2366, 886.9121), (4.693440030450115, -72.09312831984175, -11.52133329777205), (1.0, 1.0, 1.0), "SM_Grass_Dungeon_316", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (7680.221, 3489.5085, 957.78516), (-4.496856627500729, -133.45962186086544, 4.255438468016453), (1.0, 1.0, 1.0), "SM_Grass_Dungeon_320", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (9015.704, 3827.906, 806.5129), (14.500441459245168, 82.8111269379959, 8.780587985849694), (1.0, 1.0, 1.0), "SM_Grass_Dungeon_322", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (9120.261, 3730.3071, 810.64166), (-2.5636289139857977, 162.27720871164712, 11.571737461759376), (1.0, 1.0, 1.0), "SM_Grass_Dungeon_323", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (6873.167, 2037.3148, 819.6121), (13.865180875365386, -106.74727730609837, 14.196223755459686), (1.0, 1.0, 1.0), "SM_Grass_Dungeon_329", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (6789.76, 2152.537, 835.18634), (-7.8385310362582965, -28.648098069171922, 11.972277242544735), (1.0, 1.0, 1.0), "SM_Grass_Dungeon_330", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5158.7036, 3499.0503, 849.0096), (10.005352791223041, -150.96378631336006, 10.253422289294383), (1.0, 1.0, 1.0), "SM_Grass_Dungeon_335", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5175.9297, 3640.449, 862.61865), (-4.805451096915243, -71.54496776963757, 7.408065209676884), (1.0, 1.0, 1.0), "SM_Grass_Dungeon_336", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (6084.3594, 4268.286, 795.662), (16.073674707018508, 136.15837723816415, 16.570793309084795), (1.0, 1.0, 1.0), "SM_Grass_Dungeon_340", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (6225.147, 4287.6597, 812.371), (-9.60507015788949, -146.76129445508158, 14.652630506276992), (1.0, 1.0, 1.0), "SM_Grass_Dungeon_341", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5431.9863, 5411.4185, 862.12537), (-4.360595838880206, -14.235839187440924, 0.07777606419839424), (1.0, 1.0, 1.0), "SM_Grass_Dungeon_346", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5326.0327, 5316.1514, 875.32764), (2.740163971969896, 65.97925160952363, -8.486784981709711), (1.0, 1.0, 1.0), "SM_Grass_Dungeon_347", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5447.686, 6516.536, 862.12537), (-4.3605957316287345, -39.25140484174194, 0.07777624853378118), (1.0, 1.0, 1.0), "SM_Grass_Dungeon_349", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5311.3867, 6475.0103, 875.32764), (2.740169442347864, 40.963753705029866, -8.486786455835764), (1.0, 1.0, 1.0), "SM_Grass_Dungeon_350", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5795.0356, 5523.625, 845.60284), (0.40651912112921024, -166.07550048537453, 1.2618115371103746), (1.0, 1.0, 1.0), "SM_Grass_Dungeon_353", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5844.3438, 5657.6533, 854.61646), (2.3725138936538985, -85.6008015947665, -3.5839536967663372), (1.0, 1.0, 1.0), "SM_Grass_Dungeon_354", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3355.0762, 2864.0686, 868.6282), (21.79705650260139, 153.88276408430025, 15.851330192236622), (1.0, 1.0, 1.0), "SM_Grass_Dungeon_357", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3484.1357, 2925.5208, 875.16187), (-7.63207869754877, -129.6246370045082, 20.130065583396394), (1.0, 1.0, 1.0), "SM_Grass_Dungeon_358", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3666.344, 2101.5876, 821.3736), (16.23535144540242, 17.643218989428725, 14.972544450256521), (1.0, 1.0, 1.0), "SM_Grass_Dungeon_361", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3617.2732, 1967.8479, 834.8323), (-8.071104863604988, 95.19524025739102, 14.471687377544798), (1.0, 1.0, 1.0), "SM_Grass_Dungeon_362", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2737.5251, 1659.081, 797.0892), (7.4971075612985185, -114.74865764215727, 4.941790903191128), (1.0, 1.0, 1.0), "SM_Grass_Dungeon_364", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2665.1108, 1782.3235, 803.64655), (-0.07351686825835878, -34.377565570887505, 4.018861555908681), (1.0, 1.0, 1.0), "SM_Grass_Dungeon_365", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3725.109, 2246.42, 803.86084), (-25.105773620973988, 125.62963681413817, 3.566362881340451), (1.0, 1.0, 1.0), "SM_Grass_Dungeon_368", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3859.4946, 2261.0298, 850.80066), (-4.00012306947216, -153.03221403717302, -28.402744290276395), (1.0, 1.0, 1.0), "SM_Grass_Dungeon_369", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2932.797, 3095.2944, 899.081), (17.177479478475604, 117.44993828618874, -2.2554651407314523), (1.0, 1.0, 1.0), "SM_Grass_Dungeon_371", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3073.6013, 3081.4822, 877.6459), (8.340091524176446, -160.01480512144124, 12.547139686045561), (1.0, 1.0, 1.0), "SM_Grass_Dungeon_372", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2483.8433, 2849.4663, 770.8462), (12.793447389152004, 119.60923763203444, 6.076074515771736), (1.0, 1.0, 1.0), "SM_Grass_Dungeon_375", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2626.2637, 2835.654, 772.10474), (-0.2785034870051366, -160.23480177443642, 9.42764682275167), (1.0, 1.0, 1.0), "SM_Grass_Dungeon_376", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3587.1138, 1442.009, 890.3734), (-6.588806859504779, 118.14870224191345, 7.551499900633916), (1.0, 1.0, 1.0), "SM_Grass_Dungeon_379", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3726.0977, 1429.1056, 921.8848), (-4.962738289692888, -160.90364671336124, -9.462555629115045), (1.0, 1.0, 1.0), "SM_Grass_Dungeon_380", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1236.1918, 2552.3174, 778.83997), (7.497107332457132, -114.74865762894552, 4.941791261640863), (1.0, 1.0, 1.0), "SM_Grass_Dungeon_387", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1163.7772, 2675.5596, 785.39734), (-0.07351686825835878, -34.377565570887505, 4.018861555908681), (1.0, 1.0, 1.0), "SM_Grass_Dungeon_388", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1425.0609, 2195.3396, 1155.6033), (20.48319469817563, -87.57492637289064, 12.7055293207288), (1.0, 1.0, 1.0), "SM_Grass_Dungeon_394", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1307.5388, 2276.9285, 1158.3569), (-5.060607454417527, -9.734985370911183, 18.187764823581947), (1.0, 1.0, 1.0), "SM_Grass_Dungeon_395", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2895.1914, 646.6963, 780.8516), (7.497107609147893, -167.63135051207314, 4.94181699256221), (1.0, 1.0, 1.0), "SM_Grass_Dungeon_397", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2949.7668, 778.81006, 787.409), (-0.073516862957804, -87.26047603367003, 4.018882401144851), (1.0, 1.0, 1.0), "SM_Grass_Dungeon_398", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (11736.269, 9105.587, 788.9636), (7.295147918877621, -74.63277774463243, 5.905538289185362), (1.0, 1.0, 1.0), "SM_Grass_Dungeon_403", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1653.579, 8675.61, 768.8462), (1.2610093731630483, -152.08559875663062, 3.5190760518884416), (1.0, 1.0, 1.0), "SM_Grass_Dungeon_404", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (11601.715, 9153.473, 797.76294), (-1.0498352135070863, 5.6152344034205095, 3.98053415777185), (1.0, 1.0, 1.0), "SM_Grass_Dungeon_405", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (990.03, 9047.475, 718.0446), (2.7948092262410658, 168.15191585662515, 2.4194246698191137), (1.0, 1.0, 1.0), "SM_Grass_Dungeon_406", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1093.0852, 9146.424, 726.0945), (1.6261986922077534, -111.31951363636362, -1.035400380115318), (1.0, 1.0, 1.0), "SM_Grass_Dungeon_407", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1146.7863, 8567.356, 846.2832), (4.757096729110085, -15.155760207848887, 4.556416498829007), (1.0, 1.0, 1.0), "SM_Grass_Dungeon_411", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1037.7589, 8475.18, 855.9472), (-0.152374217317659, 65.26100477300464, 1.2526369854582171), (1.0, 1.0, 1.0), "SM_Grass_Dungeon_412", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1278.6531, 8205.993, 986.78674), (3.6532624944869774, 51.4572951789709, -4.597259088262483), (1.0, 1.0, 1.0), "SM_Grass_Dungeon_414", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1321.7183, 8069.7485, 979.15674), (8.67645029840046, 132.35596029127925, -1.3210139616378078), (1.0, 1.0, 1.0), "SM_Grass_Dungeon_415", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (786.66693, 11406.775, 828.771), (13.009357536329516, -1.7535399665339406, 1.4882320498078279), (1.0, 1.0, 1.0), "SM_Grass_Dungeon_419", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (702.82587, 11291.106, 820.5397), (4.169433527366327, 79.40896560599953, 8.914063570199705), (1.0, 1.0, 1.0), "SM_Grass_Dungeon_420", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2239.9038, 10677.127, 822.0243), (3.3486430710843837, 166.1300185115892, 15.419481368140957), (1.0, 1.0, 1.0), "SM_Grass_Dungeon_426", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2346.5728, 10766.443, 855.48615), (-11.06741227527923, -114.26876625638816, 1.7518470076471127), (1.0, 1.0, 1.0), "SM_Grass_Dungeon_427", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5347.8047, 9797.927, 899.1134), (13.592457914660152, -176.25318574636407, 17.841909979272266), (1.0, 1.0, 1.0), "SM_Grass_Dungeon_478", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (11045.071, 3260.0276, 830.006), (18.70685413757188, 153.31305476981763, 3.0195802645336767), (1.0, 1.0, 1.0), "SM_Grass_Dungeon_726", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (10569.447, 1563.7029, 869.35236), (-4.907988705664562, 173.0753623061973, 10.086334420349084), (1.0, 1.0, 1.0), "SM_Grass_Dungeon_761", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (7547.675, 3438.1064, 941.52234), (6.970048396466658, 146.734670963702, 9.375915894822148), (1.0, 1.0, 1.0), "SM_Grass_Dungeon_804", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1510.7113, 8668.683, 764.7727), (7.226207890947487, 127.36920356662405, 3.53202159704266), (1.0, 1.0, 1.0), "SM_Grass_Dungeon_1020", _folder)
if a: placed += 1
else: skipped += 1

# Batch 44: StaticMesh'SM_Grass_Dungeon_Low_02' (83 instances)
_mesh_path = "/Game/Art/Assets/Kits/Deco/Flora/SM_Grass_Dungeon_Low_02"
_materials = ['/Game/Art/Assets/Kits/Deco/Flora/Materials/MI_Grass_Mushroom']
_folder = "Reconstruction/BD_BB_Chapter3_HeadwaterNexus/Meshes"
a = spawn_static_mesh(_mesh_path, _materials, (8222.908, 689.73987, 715.09), (3.023792981238145, -103.08154626209641, 6.036000185683853), (1.0, 1.0, 1.0), "SM_Grass_Dungeon_Low_73", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (8255.157, 1473.2002, 787.6754), (6.144397380300978, -26.934663937148436, -0.25747687752440473), (1.0, 1.0, 1.0), "SM_Grass_Dungeon_Low_74", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (9899.967, 3364.9158, 868.4706), (-5.640808590229376, -140.3258429474985, 14.957235922007142), (1.0, 1.0, 1.0), "SM_Grass_Dungeon_Low_75", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (9606.675, 4826.3633, 1043.7577), (2.2491651169439746, -68.15996174402521, 4.4841548588189415), (1.0, 1.0, 1.0), "SM_Grass_Dungeon_Low_76", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (10337.497, 3915.9182, 1038.443), (-0.8932792360375547, 80.45125641418629, 14.156542519399734), (1.0, 1.0, 1.0), "SM_Grass_Dungeon_Low_77", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (10321.384, 4911.3203, 1211.8237), (2.85290144943703, 79.86905408882362, 1.5730762375761769), (1.0, 1.0, 1.0), "SM_Grass_Dungeon_Low_78", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (9896.944, 8143.472, 914.02386), (2.8529008369770406, -16.418731280455688, 1.5730776888931601), (1.0, 1.0, 1.0), "SM_Grass_Dungeon_Low_79", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (10197.573, 8272.034, 902.73254), (1.0315497558741953, 60.735350447150466, -1.6853027059574017), (1.0, 1.0, 1.0), "SM_Grass_Dungeon_Low_80", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (7020.1367, 9696.193, 889.6685), (-0.7478026437244082, 154.82217556670014, 10.542267792023496), (1.0, 1.0, 1.0), "SM_Grass_Dungeon_Low_81", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (10400.538, 7575.3496, 1013.0757), (2.85290136275543, 42.50754034299608, 1.5730794070591292), (1.0, 1.0, 1.0), "SM_Grass_Dungeon_Low_82", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (9873.934, 7387.6904, 682.0273), (-3.633728064159927, 133.88829860307885, 6.354993422754845), (1.0, 1.0, 1.0), "SM_Grass_Dungeon_Low_83", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (10069.007, 5178.17, 882.1649), (-6.8395986875323445, 177.09102412548458, -1.3920288173292312), (1.0, 1.0, 1.0), "SM_Grass_Dungeon_Low_84", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (8923.104, 6152.913, 883.49194), (2.2491652326957094, -16.785400623344767, 4.484176896781557), (1.0, 1.0, 1.0), "SM_Grass_Dungeon_Low_86", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (9185.709, 6445.6123, 691.8677), (1.6405218603001648, -85.66098110708955, 12.766021718643122), (1.0, 1.0, 1.0), "SM_Grass_Dungeon_Low_87", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (8367.531, 7575.506, 827.8086), (1.6405233734933375, -73.88565773713603, 12.766602203177056), (1.0, 1.0, 1.0), "SM_Grass_Dungeon_Low_88", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (8259.739, 8761.19, 764.9894), (3.1584707757247537, 85.39313881533924, -0.43969723437694763), (1.0, 1.0, 1.0), "SM_Grass_Dungeon_Low_89", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (7810.278, 8435.137, 1226.8483), (-6.679472399139649, -84.04320345447152, 23.088473678031846), (1.0, 1.0, 1.0), "SM_Grass_Dungeon_Low_90", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (8591.53, 10057.832, 1066.8395), (-2.0360107040333464, 5.377984396972477, -3.7723084135462472), (1.0, 1.0, 1.0), "SM_Grass_Dungeon_Low_91", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (9661.724, 9954.761, 870.2306), (-4.595397619994555, 136.08745741993613, 0.047454448287146664), (1.0, 1.0, 1.0), "SM_Grass_Dungeon_Low_92", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (9409.939, 10450.971, 1239.763), (-3.633728064159927, 133.88829860307885, 6.354993422754845), (1.0, 1.0, 1.0), "SM_Grass_Dungeon_Low_93", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (10486.694, 9766.785, 890.2191), (-0.12179555942052894, 100.21797833257848, 4.8224360103358785), (1.0, 1.0, 1.0), "SM_Grass_Dungeon_Low_94", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (10566.777, 9047.542, 804.5092), (1.2090393430918311, 30.485382010345226, 4.372004463401378), (1.0, 1.0, 1.0), "SM_Grass_Dungeon_Low_95", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (11018.671, 9176.863, 797.29175), (1.0303817707001952, 17.42242564074882, 0.7911562620889553), (1.0, 1.0, 1.0), "SM_Grass_Dungeon_Low_96", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (8777.718, 9789.839, 852.27313), (-14.398620820453308, -16.025358970829704, -9.845396576623925), (1.0, 1.0, 1.0), "SM_Grass_Dungeon_Low_97", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (10075.458, 9800.724, 797.7797), (3.7663502131396136, 2.165771201509143, 4.468751182569897), (1.0, 1.0, 1.0), "SM_Grass_Dungeon_Low_98", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (11517.571, 9902.338, 804.30646), (4.432797836859271, 22.406318614552255, 2.852962903717381), (1.0, 1.0, 1.0), "SM_Grass_Dungeon_Low_99", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (12032.961, 9162.42, 793.5758), (-2.51068087664168, 24.051297370777963, 6.129125536615174), (1.0, 1.0, 1.0), "SM_Grass_Dungeon_Low_102", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (7389.023, 8837.042, 1044.8318), (-17.630766646320076, 95.47083401974939, -5.951751463388301), (1.0, 1.0, 1.0), "SM_Grass_Dungeon_Low_104", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (7033.7114, 10134.691, 1207.1544), (17.11409701172652, 128.38430609072122, 33.24202139943153), (1.0, 1.0, 1.0), "SM_Grass_Dungeon_Low_105", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (6668.873, 10340.28, 1232.1158), (2.8470267894881407, 153.16125198246147, 17.860962805048057), (1.0, 1.0, 1.0), "SM_Grass_Dungeon_Low_106", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5635.072, 10145.642, 1205.2405), (1.0255393100584407, 154.82030926222836, 9.708770898833459), (1.0, 1.0, 1.0), "SM_Grass_Dungeon_Low_107", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5258.146, 9774.877, 914.10504), (17.13289279264541, 151.84486834477423, 10.34151346893949), (1.0, 1.0, 1.0), "SM_Grass_Dungeon_Low_108", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5000.9165, 9866.982, 898.24347), (11.881486778759035, 44.07803104909474, 11.537877166184424), (1.0, 1.0, 1.0), "SM_Grass_Dungeon_Low_109", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4706.553, 9774.877, 878.7364), (6.900191875376191, 152.98591132014474, 15.796139602304258), (1.0, 1.0, 1.0), "SM_Grass_Dungeon_Low_110", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5013.8467, 10475.521, 1240.1647), (4.949243108424621, 15.507082656474909, 3.576598695476487), (1.0, 1.0, 1.0), "SM_Grass_Dungeon_Low_111", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4652.1826, 10461.215, 1124.5105), (-0.7975770702910628, 101.86393422647572, 9.326083294890454), (1.0, 1.0, 1.0), "SM_Grass_Dungeon_Low_112", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3564.5723, 10530.333, 683.61536), (-0.7975467770818824, 130.19029736239509, 9.326228667143319), (1.0, 1.0, 1.0), "SM_Grass_Dungeon_Low_113", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4242.3687, 11169.63, 1349.4088), (-2.1066889341662285, 133.9259804896967, 10.685428269168199), (1.0, 1.0, 1.0), "SM_Grass_Dungeon_Low_116", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2018.0142, 10999.84, 1095.7236), (1.2446651457527302, 128.16545092306407, 1.8846638790024597), (1.0, 1.0, 1.0), "SM_Grass_Dungeon_Low_117", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3348.1975, 11175.37, 802.73914), (-5.090208960663047, 153.71940248786441, -0.3659971535320693), (1.0, 1.0, 1.0), "SM_Grass_Dungeon_Low_118", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3396.756, 11540.401, 825.16406), (5.764788385060529, 46.88891514167745, 1.4382863768022438), (1.0, 1.0, 1.0), "SM_Grass_Dungeon_Low_119", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2832.1145, 11743.131, 814.92926), (-3.780760749313662, 30.8855566498808, -7.482056026047859), (1.0, 1.0, 1.0), "SM_Grass_Dungeon_Low_120", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2587.6704, 11271.435, 814.0805), (-3.1236571572458605, 153.1903251678883, 6.100393469023639), (1.0, 1.0, 1.0), "SM_Grass_Dungeon_Low_121", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (6667.532, 8575.023, 1131.2233), (-12.758819766800455, 155.0774661208039, -13.859495557483108), (1.0, 1.0, 1.0), "SM_Grass_Dungeon_Low_122", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (6296.6035, 8371.406, 1136.6904), (-6.671295119046654, 152.9384558183959, -1.2494504536431144), (1.0, 1.0, 1.0), "SM_Grass_Dungeon_Low_123", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3770.274, 8382.09, 893.3708), (4.873449750446776, 134.38739173000874, -7.121398985725502), (1.0, 1.0, 1.0), "SM_Grass_Dungeon_Low_124", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4086.983, 8500.642, 726.789), (-3.1791384826748676, 113.9923178692479, 2.9836717057416453), (1.0, 1.0, 1.0), "SM_Grass_Dungeon_Low_125", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5318.701, 4496.0073, 937.33435), (-6.2513120216362426, 77.8377095559059, -14.1675407375495), (1.0, 1.0, 1.0), "SM_Grass_Dungeon_Low_127", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (10646.9795, 3795.0105, 1147.089), (10.089372784405395, -5.411682171917691, -2.0002747102484673), (1.0, 1.0, 1.0), "SM_Grass_Dungeon_Low_128", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (11025.25, 4016.5862, 1310.3866), (5.94609603219719, 33.74634595170843, 4.361251225690686), (1.0, 1.0, 1.0), "SM_Grass_Dungeon_Low_129", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (9509.065, 3791.0479, 1046.3171), (-3.6336059467255164, 112.92391726409893, 6.355265704183818), (1.0, 1.0, 1.0), "SM_Grass_Dungeon_Low_131", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (11130.205, 3244.2605, 816.71716), (7.01627101667496, -156.42436058407827, 13.022678802850036), (1.0, 1.0, 1.0), "SM_Grass_Dungeon_Low_132", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (11001.296, 2544.5803, 836.78546), (-20.199921569276903, -147.7921968354121, -5.622193450339067), (1.0, 1.0, 1.0), "SM_Grass_Dungeon_Low_133", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (10934.162, 1056.2424, 837.94366), (-1.4742433089541571, -28.137725289807324, -5.649566899912961), (1.0, 1.0, 1.0), "SM_Grass_Dungeon_Low_134", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (10886.759, 475.15164, 807.8894), (-1.4741514701412217, 147.57458163191976, -5.649565821005472), (1.0, 1.0, 1.0), "SM_Grass_Dungeon_Low_135", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (7630.57, 3410.5615, 947.9923), (-5.3241577399051385, -164.49587786166327, 8.144357339731934), (1.0, 1.0, 1.0), "SM_Grass_Dungeon_Low_136", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (9027.564, 3741.2578, 801.6364), (0.08910044885131885, 131.45103830261812, 13.419548748423267), (1.0, 1.0, 1.0), "SM_Grass_Dungeon_Low_137", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (6877.601, 2124.7712, 817.6725), (-4.235412173742762, -59.546454802957705, 16.467574535879418), (1.0, 1.0, 1.0), "SM_Grass_Dungeon_Low_138", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5221.9946, 3559.5518, 851.3365), (-3.9684460945166045, -102.55727172159806, 11.003510912256857), (1.0, 1.0, 1.0), "SM_Grass_Dungeon_Low_139", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (6159.725, 4223.8774, 791.26746), (-4.394286929896408, -177.49579198571027, 19.656519322042307), (1.0, 1.0, 1.0), "SM_Grass_Dungeon_Low_140", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5346.5977, 5407.4575, 881.22046), (-5.5693971046098945, 36.14880218255121, -6.567321841551965), (1.0, 1.0, 1.0), "SM_Grass_Dungeon_Low_141", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5368.632, 6549.0547, 881.22046), (-5.569396710075573, 11.133301535549274, -6.567321312957489), (1.0, 1.0, 1.0), "SM_Grass_Dungeon_Low_142", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5869.7812, 5567.467, 858.34503), (-3.42871046680934, -115.99798381738472, -2.132690082893942), (1.0, 1.0, 1.0), "SM_Grass_Dungeon_Low_143", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3439.632, 2845.3484, 855.52985), (0.04797592904782801, -159.6769327606403, 23.332093493906495), (1.0, 1.0, 1.0), "SM_Grass_Dungeon_Low_144", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3591.6643, 2056.1113, 816.1902), (-3.167847014131881, 64.49763299816586, 18.717523701100767), (1.0, 1.0, 1.0), "SM_Grass_Dungeon_Low_145", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2751.3098, 1745.4915, 801.0115), (-1.6530148848141775, -65.27007693639348, 5.659467651054643), (1.0, 1.0, 1.0), "SM_Grass_Dungeon_Low_146", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3784.879, 2204.242, 852.0413), (-20.958984953996296, -179.6484633155916, -21.321502652373564), (1.0, 1.0, 1.0), "SM_Grass_Dungeon_Low_147", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2993.449, 3033.499, 885.83795), (9.937863001229612, 168.68751394050526, 8.616190377356508), (1.0, 1.0, 1.0), "SM_Grass_Dungeon_Low_148", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2545.8298, 2787.671, 767.4298), (0.9502228895279915, 168.85769946556766, 10.406508974230194), (1.0, 1.0, 1.0), "SM_Grass_Dungeon_Low_149", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3645.3977, 1381.7396, 915.73706), (-12.726257121723249, 168.76122741700917, -3.513367165623511), (1.0, 1.0, 1.0), "SM_Grass_Dungeon_Low_150", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1249.9764, 2638.7275, 782.76227), (-1.6530148848141775, -65.27007693639348, 5.659467651054643), (1.0, 1.0, 1.0), "SM_Grass_Dungeon_Low_151", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1400.096, 2278.4006, 1143.36), (1.298739723178612, -40.03478332450778, 20.370945432686902), (1.0, 1.0, 1.0), "SM_Grass_Dungeon_Low_152", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2972.4136, 687.84814, 784.7739), (-1.6530148410030945, -118.15300254652921, 5.659510085113938), (1.0, 1.0, 1.0), "SM_Grass_Dungeon_Low_153", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1580.8694, 8616.385, 768.51184), (-0.7640686238629593, 177.0475700421558, 4.546282315772451), (1.0, 1.0, 1.0), "SM_Grass_Dungeon_Low_154", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1076.8218, 9054.082, 727.8057), (-2.7788092545667977, -141.94542201785345, 0.4448849706561671), (1.0, 1.0, 1.0), "SM_Grass_Dungeon_Low_155", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1059.5507, 8566.375, 854.0693), (-3.139160037837948, 34.45713780133171, 3.3239811183786867), (1.0, 1.0, 1.0), "SM_Grass_Dungeon_Low_156", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1246.7861, 8124.589, 992.2313), (3.1465182183359706, 101.74769829841709, -3.389831490669961), (1.0, 1.0, 1.0), "SM_Grass_Dungeon_Low_157", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (702.05176, 11384.847, 823.1679), (4.5014232977782624, 48.386507391385265, 7.674648802930431), (1.0, 1.0, 1.0), "SM_Grass_Dungeon_Low_158", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2326.358, 10676.951, 836.0763), (-12.227264878724394, -145.8483892389537, 9.451510233197123), (1.0, 1.0, 1.0), "SM_Grass_Dungeon_Low_159", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (10398.85, 5535.1777, 1016.41626), (-10.030577957835433, -138.91267693808712, -22.366666899070545), (1.0, 1.0, 1.0), "SM_Grass_Dungeon_Low_210", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (11691.368, 9180.65, 793.5758), (-2.510742636603618, -25.296204501752502, 6.129043182541426), (1.0, 1.0, 1.0), "SM_Grass_Dungeon_Low_404", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (10652.794, 1575.9768, 893.3353), (-13.598173059036545, -136.7330355523337, -0.5346067191250092), (1.0, 1.0, 1.0), "SM_Grass_Dungeon_Low_762", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (8073.9844, 3290.8518, 896.8969), (-5.363525532490933, -101.38003230577074, -10.181854668435928), (1.0, 1.0, 1.0), "SM_Grass_Dungeon_Low_794", _folder)
if a: placed += 1
else: skipped += 1

# Batch 45: StaticMesh'SM_HeadWaterNexusGM_Cut_GuideMeshChunk2' (1 instances)
_mesh_path = "/Game/LevelDesign/GuideMeshes/Nexus/CavernNexus2/OcclusionGuide/SM_HeadWaterNexusGM_Cut_GuideMeshChunk2"
_materials = ['/Engine/EngineMaterials/WorldGridMaterial']
_folder = "Reconstruction/BD_BB_Chapter3_HeadwaterNexus/Meshes"
a = spawn_static_mesh(_mesh_path, _materials, (0.0, 0.0, 0.0), (0.0, 0.0, -0.0), (1.0, 1.0, 1.0), "SM_HeadWaterNexusGM_Cut_GuideMeshChunk2_3", _folder)
if a: placed += 1
else: skipped += 1

# Batch 46: StaticMesh'SM_HeadWaterNexusGM_Cut_GuideMeshChunk3' (1 instances)
_mesh_path = "/Game/LevelDesign/GuideMeshes/Nexus/CavernNexus2/OcclusionGuide/SM_HeadWaterNexusGM_Cut_GuideMeshChunk3"
_materials = ['/Game/LevelDesign/GuideMeshes/MI_GuidemeshOcclusion']
_folder = "Reconstruction/BD_BB_Chapter3_HeadwaterNexus/Meshes"
a = spawn_static_mesh(_mesh_path, _materials, (0.0, 0.0, 0.0), (0.0, 0.0, -0.0), (1.0, 1.0, 1.0), "SM_HeadWaterNexusGM_Cut_GuideMeshChunk3_5", _folder)
if a: placed += 1
else: skipped += 1

# Batch 47: StaticMesh'SM_Cobwebs_G_01' (1 instances)
_mesh_path = "/Game/Unshippable/ThirdParty/Cobwebs/Meshes/SM_Cobwebs_G_01"
_materials = ['/Game/Unshippable/ThirdParty/Cobwebs/Materials/MI_Cobwebs_Atlas_G']
_folder = "Reconstruction/BD_BB_Chapter3_HeadwaterNexus/Meshes"
a = spawn_static_mesh(_mesh_path, _materials, (4222.447, 8179.3154, 1054.9592), (0.0, 0.0, -0.0), (1.0, 1.0, 1.0), "SM_Cobwebs_G_01_14", _folder)
if a: placed += 1
else: skipped += 1

# Batch 48: StaticMesh'SM_MushroomNucleus_B_B' (85 instances)
_mesh_path = "/Game/Unshippable/ThirdParty/DeepElderCaves/Meshes/Props/SM_MushroomNucleus_B_B"
_materials = ['/Game/Unshippable/ThirdParty/DeepElderCaves/Materials/MI_MushroomNucleus_Green_SSS_Var2']
_folder = "Reconstruction/BD_BB_Chapter3_HeadwaterNexus/Meshes"
a = spawn_static_mesh(_mesh_path, _materials, (9106.062, 3656.3594, 802.903), (0.0889569237393119, 131.45129445808294, 2.9292910754697608), (1.0, 1.0, 1.0), "SM_MushroomNucleus_B_B100", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (6817.031, 2222.752, 827.79004), (-4.235351473042892, -59.54644679991383, 5.980058102612161), (1.0, 1.0, 1.0), "SM_MushroomNucleus_B_B101", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5244.4185, 3672.606, 860.66736), (-3.968445091788906, -102.55721541805833, 0.5158596654172964), (1.0, 1.0, 1.0), "SM_MushroomNucleus_B_B102", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (6274.6313, 4231.3633, 801.8432), (-4.394255173969056, -177.49564084154298, 9.169169246825318), (1.0, 1.0, 1.0), "SM_MushroomNucleus_B_B103", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5255.482, 5337.216, 892.8966), (-5.569245550150659, 36.14877470794187, -17.05545087631689), (1.0, 1.0, 1.0), "SM_MushroomNucleus_B_B104", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5256.3623, 6523.932, 892.8966), (-5.569213622526401, 11.133240122889562, -17.055449764154), (1.0, 1.0, 1.0), "SM_MushroomNucleus_B_B105", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5917.714, 5672.429, 865.945), (-3.428497048018237, -115.99803049961606, -12.621030190566092), (1.0, 1.0, 1.0), "SM_MushroomNucleus_B_B106", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3547.217, 2887.6965, 857.31165), (0.047928472025542075, -159.67689790564853, 12.845436960965246), (1.0, 1.0, 1.0), "SM_MushroomNucleus_B_B107", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3544.2573, 1950.9502, 824.2593), (-3.1678161480588214, 64.49754899718309, 8.22977191354672), (1.0, 1.0, 1.0), "SM_MushroomNucleus_B_B108", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2700.4363, 1849.2389, 805.4235), (-1.6529539878440023, -65.26986835097766, -4.828399368732217), (1.0, 1.0, 1.0), "SM_MushroomNucleus_B_B109", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3892.9167, 2207.897, 893.0961), (-20.958863016934245, -179.64828609719314, -31.810087391459508), (1.0, 1.0, 1.0), "SM_MushroomNucleus_B_B110", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3105.8428, 3013.82, 867.0915), (9.937903514482517, 168.68775934309377, -1.872924778619819), (1.0, 1.0, 1.0), "SM_MushroomNucleus_B_B111", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2659.7747, 2767.992, 766.819), (0.9502334430973449, 168.85796042030012, -0.08279418255761305), (1.0, 1.0, 1.0), "SM_MushroomNucleus_B_B112", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3756.431, 1362.6804, 941.8026), (-12.72616716917531, 168.7614628926265, -14.003145582180084), (1.0, 1.0, 1.0), "SM_MushroomNucleus_B_B113", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1199.1029, 2742.475, 787.1743), (-1.6529539878440023, -65.26986835097766, -4.828399368732217), (1.0, 1.0, 1.0), "SM_MushroomNucleus_B_B114", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1310.0128, 2350.8943, 1142.495), (1.2986924871937418, -40.034606749649285, 9.883466994550288), (1.0, 1.0, 1.0), "SM_MushroomNucleus_B_B115", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3024.4426, 791.0209, 789.186), (-1.6529542789941967, -118.15274140005104, -4.828398944037713), (1.0, 1.0, 1.0), "SM_MushroomNucleus_B_B116", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1696.4359, 8613.259, 771.076), (-0.7639160209445564, 177.04739249868308, -5.943176579822597), (1.0, 1.0, 1.0), "SM_MushroomNucleus_B_B117", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1165.9222, 9127.512, 734.227), (-2.778686153199469, -141.94561878621892, -10.044737725440926), (1.0, 1.0, 1.0), "SM_MushroomNucleus_B_B118", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (966.03394, 8498.747, 861.3606), (-3.1389159071351513, 34.456974966558526, -7.165648970309977), (1.0, 1.0, 1.0), "SM_MushroomNucleus_B_B119", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1273.1685, 8012.1514, 986.50745), (3.146517793821949, 101.74772600727445, -13.878602392379825), (1.0, 1.0, 1.0), "SM_MushroomNucleus_B_B120", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (627.5322, 11296.774, 815.26825), (4.501456581872621, 48.38648444421161, -2.8153994855525735), (1.0, 1.0, 1.0), "SM_MushroomNucleus_B_B121", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2418.095, 10742.488, 861.7928), (-12.227262193838706, -145.84832846424158, -1.0391844315011027), (1.0, 1.0, 1.0), "SM_MushroomNucleus_B_B122", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (8246.32, 802.86896, 710.0867), (3.023799569877563, -103.081594132253, -4.450591179533028), (1.0, 1.0, 1.0), "SM_MushroomNucleus_B_B36_812", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (8151.3047, 1522.7117, 776.08075), (6.144370055607864, -26.934695225394307, -10.744293747271701), (1.0, 1.0, 1.0), "SM_MushroomNucleus_B_B37", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (9561.065, 4932.5654, 1040.2399), (2.249172125433567, -68.16003357407249, -6.002471320370902), (1.0, 1.0, 1.0), "SM_MushroomNucleus_B_B38", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (9986.736, 3440.2585, 881.3419), (-5.640807852011847, -140.32575707625034, 4.46989449040661), (1.0, 1.0, 1.0), "SM_MushroomNucleus_B_B39_35", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (10320.91, 3801.5261, 1041.725), (-0.8932800901091899, 80.45144919495138, 3.668382041612781), (1.0, 1.0, 1.0), "SM_MushroomNucleus_B_B40", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (10303.904, 4797.1187, 1206.9427), (2.8529900846561436, 79.8690468514644, -8.915861805166323), (1.0, 1.0, 1.0), "SM_MushroomNucleus_B_B41", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (9785.345, 8173.355, 909.1429), (2.8529899576500624, -16.418668291318674, -8.91586265762617), (1.0, 1.0, 1.0), "SM_MushroomNucleus_B_B42", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (10143.62, 8169.768, 901.3596), (1.0316375230572878, 60.7354038298671, -12.17474205193276), (1.0, 1.0, 1.0), "SM_MushroomNucleus_B_B43", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (7125.872, 9649.474, 892.4884), (-0.7477721571105317, 154.8221911670193, 0.05478333102394401), (1.0, 1.0, 1.0), "SM_MushroomNucleus_B_B44", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (10317.34, 7495.187, 1008.19464), (2.852990350497864, 42.507568287210134, -8.9158626395505), (1.0, 1.0, 1.0), "SM_MushroomNucleus_B_B45", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (9955.869, 7306.5366, 690.462), (-3.6337278964595785, 133.88817530159395, -4.132721103723035), (1.0, 1.0, 1.0), "SM_MushroomNucleus_B_B46", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (10183.696, 5175.2656, 896.6498), (-6.839537048774786, 177.09113313038526, -11.88128488471448), (1.0, 1.0, 1.0), "SM_MushroomNucleus_B_B47", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (10482.736, 5612.2812, 1036.1882), (-10.030545795061883, -138.91252086464763, -32.85647208575811), (1.0, 1.0, 1.0), "SM_MushroomNucleus_B_B48_212", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (8811.664, 6183.576, 879.9741), (2.249171785346056, -16.785458655489464, -6.002471474750238), (1.0, 1.0, 1.0), "SM_MushroomNucleus_B_B49", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (9174.32, 6560.671, 689.9738), (1.6405021398552297, -85.66074408977187, 2.279019147100243), (1.0, 1.0, 1.0), "SM_MushroomNucleus_B_B50", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (8332.902, 7685.8184, 825.91473), (1.6405019904360887, -73.88546622561901, 2.279028812223996), (1.0, 1.0, 1.0), "SM_MushroomNucleus_B_B51", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (8253.359, 8645.875, 759.39294), (3.15843634384296, 85.39301468336825, -10.92782605442233), (1.0, 1.0, 1.0), "SM_MushroomNucleus_B_B52", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (7796.0415, 8548.872, 1242.1495), (-6.6796259355926555, -84.04297280782306, 12.598084459595782), (1.0, 1.0, 1.0), "SM_MushroomNucleus_B_B53", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (8476.82, 10044.077, 1071.5494), (-2.0360105692829875, 5.3778190288515555, -14.262420675494008), (1.0, 1.0, 1.0), "SM_MushroomNucleus_B_B54", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (9746.69, 9876.9795, 880.28723), (-4.595366957450105, 136.08731973674722, -10.44338820661902), (1.0, 1.0, 1.0), "SM_MushroomNucleus_B_B55", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (9491.875, 10369.816, 1248.1978), (-3.6337278964595785, 133.88817530159395, -4.132721103723035), (1.0, 1.0, 1.0), "SM_MushroomNucleus_B_B56", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (10509.972, 9653.527, 891.50055), (-0.12182624863978961, 100.21792141995071, -5.665162101137928), (1.0, 1.0, 1.0), "SM_MushroomNucleus_B_B57", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (10468.603, 8986.458, 803.083), (1.2091279596457716, 30.4854149702085, -6.116973812083382), (1.0, 1.0, 1.0), "SM_MushroomNucleus_B_B58", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (10909.245, 9139.491, 796.047), (1.0304706669183221, 17.422546831119398, -9.69796904740527), (1.0, 1.0, 1.0), "SM_MushroomNucleus_B_B59", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (8669.351, 9817.853, 881.297), (-14.398560122098422, -16.02548210240109, -20.33227502211466), (1.0, 1.0, 1.0), "SM_MushroomNucleus_B_B60", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (9960.232, 9793.533, 791.20215), (3.7664591917715087, 2.165771605389063, -6.020324868627569), (1.0, 1.0, 1.0), "SM_MushroomNucleus_B_B61", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (11412.042, 9855.737, 796.307), (4.432899863541663, 22.406340200045417, -7.636230011767856), (1.0, 1.0, 1.0), "SM_MushroomNucleus_B_B62", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (11278.488, 9879.4375, 924.9226), (3.2966794267302015, -160.98553263477174, -1.505584476138801), (1.0, 1.0, 1.0), "SM_MushroomNucleus_B_B63", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (11585.806, 9227.443, 799.73816), (-2.5106200794262854, -25.29611111589115, -4.3600768333776285), (1.0, 1.0, 1.0), "SM_MushroomNucleus_B_B64_407", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (11928.69, 9112.814, 799.73816), (-2.5106198679725114, 24.05138906985095, -4.360076572238432), (1.0, 1.0, 1.0), "SM_MushroomNucleus_B_B65", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (7402.4614, 8727.815, 1080.3093), (-17.630767471233067, 95.47063459840622, -16.440123650349964), (1.0, 1.0, 1.0), "SM_MushroomNucleus_B_B67", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (7104.278, 10048.814, 1175.2909), (17.114079417540427, 128.38429040499506, 22.755453929166556), (1.0, 1.0, 1.0), "SM_MushroomNucleus_B_B68", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (6773.1025, 10290.364, 1228.0187), (2.847122622319083, 153.16125160985914, 7.371850769065835), (1.0, 1.0, 1.0), "SM_MushroomNucleus_B_B69", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5740.8423, 10098.922, 1204.4429), (1.0255731669664603, 154.82030779130136, -0.7788389655385389), (1.0, 1.0, 1.0), "SM_MushroomNucleus_B_B70", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5357.1616, 9724.961, 881.2957), (17.13293942527614, 151.8448228402045, -0.1480096320389213), (1.0, 1.0, 1.0), "SM_MushroomNucleus_B_B71", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4921.319, 9786.166, 875.77234), (11.881545012385184, 44.07797863851459, 1.0475331999589599), (1.0, 1.0, 1.0), "SM_MushroomNucleus_B_B72", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4810.1304, 9724.961, 866.3914), (6.9003079549254105, 152.9858699427549, 5.306413693986603), (1.0, 1.0, 1.0), "SM_MushroomNucleus_B_B73", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4903.553, 10441.963, 1231.1608), (4.949229756464058, 15.507047923163984, -6.913970452542361), (1.0, 1.0, 1.0), "SM_MushroomNucleus_B_B74", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4678.6123, 10348.68, 1127.3728), (-0.7975769187314284, 101.86387325916358, -1.16180425584796), (1.0, 1.0, 1.0), "SM_MushroomNucleus_B_B75", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3641.2349, 10443.814, 686.47766), (-0.7975464892928658, 130.19016110857086, -1.1618043722112952), (1.0, 1.0, 1.0), "SM_MushroomNucleus_B_B76", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4324.416, 11088.338, 1354.9751), (-2.106689101949463, 133.92597815658533, 0.19694785715738894), (1.0, 1.0, 1.0), "SM_MushroomNucleus_B_B77", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2091.6936, 10910.736, 1094.1027), (1.2447064207435334, 128.16559338069862, -8.603820442020755), (1.0, 1.0, 1.0), "SM_MushroomNucleus_B_B78", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3452.664, 11127.024, 813.7686), (-5.090117499507625, 153.7194114366872, -10.855925029340275), (1.0, 1.0, 1.0), "SM_MushroomNucleus_B_B79", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3320.198, 11454.407, 814.4158), (5.764944919520752, 46.88912495844259, -9.051603765539848), (1.0, 1.0, 1.0), "SM_MushroomNucleus_B_B80", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2734.6787, 11681.377, 822.96106), (-3.7806394485951955, 30.88570161112285, -17.972106696895306), (1.0, 1.0, 1.0), "SM_MushroomNucleus_B_B81", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2691.9001, 11221.898, 821.47595), (-3.1235045933740464, 153.19032957352204, -4.3891294434611305), (1.0, 1.0, 1.0), "SM_MushroomNucleus_B_B82", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (6771.03, 8530.245, 1156.8287), (-12.758756961119323, 155.07743577674253, -24.34801934395543), (1.0, 1.0, 1.0), "SM_MushroomNucleus_B_B83", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (6400.101, 8321.804, 1150.8472), (-6.671203882735306, 152.93842804161375, -11.738495756035414), (1.0, 1.0, 1.0), "SM_MushroomNucleus_B_B84", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3852.9958, 8301.832, 883.9785), (4.873544437120183, 134.3872228720395, -17.61056578646399), (1.0, 1.0, 1.0), "SM_MushroomNucleus_B_B85", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4136.504, 8396.403, 734.1436), (-3.178894334503114, 113.99223871211764, -7.505616035108389), (1.0, 1.0, 1.0), "SM_MushroomNucleus_B_B86", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5976.221, 7031.3135, 898.80554), (1.5112748532400009, 135.52071466702907, -6.360535477710787), (1.0, 1.0, 1.0), "SM_MushroomNucleus_B_B87", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5297.431, 4383.048, 949.98346), (-6.25122098190724, 77.83780218649355, -24.65634219561896), (1.0, 1.0, 1.0), "SM_MushroomNucleus_B_B88", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (10533.28, 3802.8435, 1127.5201), (10.08938345995973, -5.41134596540098, -12.489745204540752), (1.0, 1.0, 1.0), "SM_MushroomNucleus_B_B89", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (10931.131, 3950.3037, 1299.4191), (5.946062086903466, 33.74640184031752, -6.128845311645369), (1.0, 1.0, 1.0), "SM_MushroomNucleus_B_B90", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (9556.542, 3685.9526, 1054.7518), (-3.6336054155426414, 112.92363934452831, -4.132720042488095), (1.0, 1.0, 1.0), "SM_MushroomNucleus_B_B92", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (11234.458, 3292.6428, 804.01514), (7.016271578607963, -156.4241495039674, 2.53419244731718), (1.0, 1.0, 1.0), "SM_MushroomNucleus_B_B93", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (11091.361, 2604.8154, 877.17645), (-20.19998407279786, -147.7920593251945, -16.1117866126095), (1.0, 1.0, 1.0), "SM_MushroomNucleus_B_B94", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (10732.487, 1654.9752, 921.2603), (-13.598205136263434, -136.73330658996863, -11.023041475198825), (1.0, 1.0, 1.0), "SM_MushroomNucleus_B_B95_764", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (10830.876, 1108.1221, 841.42334), (-1.4742430079085453, -28.13763458995992, -16.139861396301185), (1.0, 1.0, 1.0), "SM_MushroomNucleus_B_B96", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (10985.875, 415.69623, 811.3691), (-1.4741510682114076, 147.57472518618295, -16.140138120968725), (1.0, 1.0, 1.0), "SM_MushroomNucleus_B_B97", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (8093.755, 3404.2434, 907.97186), (-5.363554748944398, -101.38004789971798, -20.669005865157434), (1.0, 1.0, 1.0), "SM_MushroomNucleus_B_B98", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (7740.6343, 3443.9546, 959.9115), (-5.32424937856342, -164.4956826644763, -2.345672380744587), (1.0, 1.0, 1.0), "SM_MushroomNucleus_B_B99", _folder)
if a: placed += 1
else: skipped += 1

# Batch 49: StaticMesh'SM_MushroomNucleus_B_C' (2 instances)
_mesh_path = "/Game/Unshippable/ThirdParty/DeepElderCaves/Meshes/Props/SM_MushroomNucleus_B_C"
_materials = ['/Game/Unshippable/ThirdParty/DeepElderCaves/Materials/MI_MushroomNucleus_Green_SSS_Var3']
_folder = "Reconstruction/BD_BB_Chapter3_HeadwaterNexus/Meshes"
a = spawn_static_mesh(_mesh_path, _materials, (9814.629, 7737.893, 824.8922), (2.357343754974851, 178.53168069164514, -11.103636495433294), (1.0, 1.0, 1.0), "SM_MushroomNucleus_B_C28", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4066.5269, 10657.976, 1013.1005), (-0.9555970503047814, -138.07679965170908, -13.836792932942043), (1.0, 1.0, 1.0), "SM_MushroomNucleus_B_C41", _folder)
if a: placed += 1
else: skipped += 1

# Batch 50: StaticMesh'SM_Debris_Floor_05' (1 instances)
_mesh_path = "/Game/Unshippable/ThirdParty/Lordenfel/Environment/Architecture/Floors/SM_Debris_Floor_05"
_materials = ['/Game/Unshippable/ThirdParty/Lordenfel/Environment/Materials/MI_Floor_Bricks_01_Cavern']
_folder = "Reconstruction/BD_BB_Chapter3_HeadwaterNexus/Meshes"
a = spawn_static_mesh(_mesh_path, _materials, (5323.1978, 7830.9277, 714.47485), (4.518466879777744, 21.26510556280964, -3.7676094202074735), (1.0, 1.0, 1.0), "SM_Debris_Floor_05_142", _folder)
if a: placed += 1
else: skipped += 1

# Batch 51: StaticMesh'SM_Floor_Ruined_03' (1 instances)
_mesh_path = "/Game/Unshippable/ThirdParty/Lordenfel/Environment/Architecture/Floors/SM_Floor_Ruined_03"
_materials = ['/Game/Unshippable/ThirdParty/Lordenfel/Environment/Materials/MI_Floor_01_Cavern', '/Game/Unshippable/ThirdParty/Lordenfel/Environment/Materials/MI_Floor_Bricks_01_Cavern']
_folder = "Reconstruction/BD_BB_Chapter3_HeadwaterNexus/Meshes"
a = spawn_static_mesh(_mesh_path, _materials, (9777.382, 7353.7285, 696.53345), (0.5839811340210245, -155.63791676935304, -0.046569852522714374), (1.0, 1.0, 1.0), "SM_Floor_Ruined_03_167", _folder)
if a: placed += 1
else: skipped += 1

# Batch 52: StaticMesh'SM_Floor_Ruined_06' (3 instances)
_mesh_path = "/Game/Unshippable/ThirdParty/Lordenfel/Environment/Architecture/Floors/SM_Floor_Ruined_06"
_materials = ['/Game/Unshippable/ThirdParty/Lordenfel/Environment/Materials/MI_Floor_01_Cavern', '/Game/Unshippable/ThirdParty/Lordenfel/Environment/Materials/MI_Floor_Bricks_01_Cavern']
_folder = "Reconstruction/BD_BB_Chapter3_HeadwaterNexus/Meshes"
a = spawn_static_mesh(_mesh_path, _materials, (7644.4917, 2513.3455, 649.74475), (-0.6997373416896181, 167.47424382861595, 179.9999112060034), (1.0, 1.0, 1.0), "SM_Floor_Ruined_43", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (9298.96, 6689.146, 648.24603), (-0.5221556846304961, -154.3450598624692, -179.68053110460238), (1.0, 1.0, 1.0), "SM_Floor_Ruined_170", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (9974.015, 6147.571, 699.86334), (0.0, 0.0, -0.0), (1.0, 1.0, 1.0), "SM_Floor_Ruined_06_147", _folder)
if a: placed += 1
else: skipped += 1

# Batch 53: StaticMesh'SM_Floor_Ruined_07' (2 instances)
_mesh_path = "/Game/Unshippable/ThirdParty/Lordenfel/Environment/Architecture/Floors/SM_Floor_Ruined_07"
_materials = ['/Game/Unshippable/ThirdParty/Lordenfel/Environment/Materials/MI_Floor_01_Cavern', '/Game/Unshippable/ThirdParty/Lordenfel/Environment/Materials/MI_Floor_Bricks_01_Cavern']
_folder = "Reconstruction/BD_BB_Chapter3_HeadwaterNexus/Meshes"
a = spawn_static_mesh(_mesh_path, _materials, (7654.3955, 2183.6162, 697.73584), (0.0, -13.969390693344156, 0.0), (1.0, 1.0, 1.0), "SM_Floor_Ruined_36", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (9482.964, 6104.1255, 693.7115), (0.0, 0.0, -0.0), (1.0, 1.0, 1.0), "SM_Floor_Ruined_07_140", _folder)
if a: placed += 1
else: skipped += 1

# Batch 54: StaticMesh'SM_Floor_Ruined_08' (13 instances)
_mesh_path = "/Game/Unshippable/ThirdParty/Lordenfel/Environment/Architecture/Floors/SM_Floor_Ruined_08"
_materials = ['/Game/Unshippable/ThirdParty/Lordenfel/Environment/Materials/MI_Floor_01_Cavern', '/Game/Unshippable/ThirdParty/Lordenfel/Environment/Materials/MI_Floor_Bricks_01_Cavern']
_folder = "Reconstruction/BD_BB_Chapter3_HeadwaterNexus/Meshes"
a = spawn_static_mesh(_mesh_path, _materials, (8803.351, 7643.917, 697.3774), (1.8396295024647666, 10.892830896663169, -1.4540712409366943), (1.0, 1.0, 1.0), "SM_Floor_Ruined_17", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (9749.828, 6952.3647, 699.9281), (0.25655598973822186, 18.519202063978035, -1.4320677865450102), (1.0, 1.0, 1.0), "SM_Floor_Ruined_20", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (9247.09, 6408.29, 697.0902), (0.0, 17.128530876974793, -0.0), (1.0, 1.0, 1.0), "SM_Floor_Ruined_23", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (6152.708, 4040.1482, 730.54865), (0.9529616937726324, 7.463896528148875, -7.2348633314158), (1.0, 1.0, 1.0), "SM_Floor_Ruined_24", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2327.9976, 9729.377, 693.21674), (0.2115241054671901, -0.2938232128163743, 1.4422010887658585), (1.0, 1.0, 1.0), "SM_Floor_Ruined_30", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (8159.2725, 2345.784, 691.0603), (-2.9349365892661448, -8.189332297632776, 4.4126525583689484e-07), (1.0, 1.0, 1.0), "SM_Floor_Ruined_64", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (9695.0, 6237.547, 699.9278), (0.0, 0.0, -0.0), (1.0, 1.0, 1.0), "SM_Floor_Ruined_143", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (9324.567, 7914.5356, 690.06616), (0.0, 8.364272157041755, -0.0), (1.0, 1.0, 1.0), "SM_Floor_Ruined_157", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (9104.453, 6513.9385, 696.75305), (0.0, 17.128530876974793, -0.0), (1.0, 1.0, 1.0), "SM_Floor_Ruined_179", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3648.639, 9527.13, 721.0764), (4.461814022049251, -41.75418004648132, -3.3587039535001306), (1.0, 1.0, 1.0), "SM_Floor_Ruined_186", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3145.1846, 9290.473, 697.5139), (0.0, -41.19311492118064, 0.0), (1.0, 1.0, 1.0), "SM_Floor_Ruined_197", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2518.139, 9930.807, 691.47906), (0.37995658086815626, 0.5997443866953315, -0.17666625721843163), (1.0, 1.0, 1.0), "SM_Floor_Ruined_204", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3310.7698, 10083.556, 690.60004), (-2.3616029336237014, 7.086119865550745, 1.0132867755747082e-07), (1.0, 1.0, 1.0), "SM_Floor_Ruined_208", _folder)
if a: placed += 1
else: skipped += 1

# Batch 55: StaticMesh'SM_Floor_Ruined_09' (12 instances)
_mesh_path = "/Game/Unshippable/ThirdParty/Lordenfel/Environment/Architecture/Floors/SM_Floor_Ruined_09"
_materials = ['/Game/Unshippable/ThirdParty/Lordenfel/Environment/Materials/MI_Floor_01_Cavern', '/Game/Unshippable/ThirdParty/Lordenfel/Environment/Materials/MI_Floor_Bricks_01_Cavern']
_folder = "Reconstruction/BD_BB_Chapter3_HeadwaterNexus/Meshes"
a = spawn_static_mesh(_mesh_path, _materials, (9170.509, 7372.3794, 696.7522), (0.0, 23.995723572805684, -0.0), (1.0, 1.0, 1.0), "SM_Floor_Ruined_8", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3821.4202, 9994.048, 718.21936), (5.428661449332161, -45.90682920405555, -1.0702819830625845), (1.0, 1.0, 1.0), "SM_Floor_Ruined_11", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (8889.92, 6922.587, 698.29047), (0.16048189276680444, -162.93204803748807, 0.5420543615999504), (1.0, 1.0, 1.0), "SM_Floor_Ruined_18", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5795.2324, 3740.56, 703.0757), (0.3096330167896993, 15.350246398737777, -2.5974736501303513), (1.0, 1.0, 1.0), "SM_Floor_Ruined_21", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5816.37, 2793.975, 698.0368), (0.0, 0.0, -0.0), (1.0, 1.0, 1.0), "SM_Floor_Ruined_27", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1938.7123, 9906.588, 697.5142), (0.5817066546278303, 7.139045363133254, -3.2264709265672553), (1.0, 1.0, 1.0), "SM_Floor_Ruined_28", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (7080.0903, 2289.5378, 699.2906), (-9.770479686326993e-10, -20.298401498093106, -0.062347414810659925), (1.0, 1.0, 1.0), "SM_Floor_Ruined_31", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (9231.15, 10645.75, 1243.5037), (1.2602975032624053, 0.0, -0.0), (1.0, 1.0, 1.0), "SM_Floor_Ruined_122", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3270.5442, 9598.322, 700.2454), (1.3042820514384612, -42.518095165806024, -0.7640686669186074), (1.0, 1.0, 1.0), "SM_Floor_Ruined_151", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (8578.909, 8065.503, 685.5081), (-0.25247191680321557, 7.0579730243221555, 2.0380752668479647), (1.0, 1.0, 1.0), "SM_Floor_Ruined_154", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (10185.468, 6687.48, 695.99384), (0.0, 18.300512070947363, -0.0), (1.0, 1.0, 1.0), "SM_Floor_Ruined_176", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3385.1382, 10471.72, 690.68225), (-3.4644465794919803, -34.87405216277923, 1.3155908565490919e-06), (1.0, 1.0, 1.0), "SM_Floor_Ruined_200", _folder)
if a: placed += 1
else: skipped += 1

# Batch 56: StaticMesh'SM_Floor_Ruined_11' (1 instances)
_mesh_path = "/Game/Unshippable/ThirdParty/Lordenfel/Environment/Architecture/Floors/SM_Floor_Ruined_11"
_materials = ['/Game/Unshippable/ThirdParty/Lordenfel/Environment/Materials/MI_Floor_01_Cavern', '/Game/Unshippable/ThirdParty/Lordenfel/Environment/Materials/MI_Floor_Bricks_01_Cavern']
_folder = "Reconstruction/BD_BB_Chapter3_HeadwaterNexus/Meshes"
a = spawn_static_mesh(_mesh_path, _materials, (8584.6, 2090.6282, 680.3253), (0.0, -2.9069518780689316, 0.0), (1.0, 1.0, 1.0), "SM_Floor_Ruined_55", _folder)
if a: placed += 1
else: skipped += 1

# Batch 57: StaticMesh'PWM_Nordic_1x1x1_A' (16 instances)
_mesh_path = "/Game/Unshippable/Whitebox/Rocks/Meshes/PWM_Nordic_1x1x1_A"
_materials = ['/Game/Unshippable/Whitebox/Rocks/Materials/PWM_Nordic_Atlas_A']
_folder = "Reconstruction/BD_BB_Chapter3_HeadwaterNexus/Meshes"
a = spawn_static_mesh(_mesh_path, _materials, (3333.5596, 1721.3069, 2047.9598), (0.0, 0.0, -0.0), (1.0, 1.0, 1.0), "PWM_Nordic_1x1x1_A_78", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (11735.423, 10163.03, 1231.9517), (0.0, 0.0, -16.87524395578421), (1.3125, 1.3125, 1.3125), "PWM_Nordic_1x1x1_A10", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (11735.423, 9963.03, 2001.9517), (-47.36614500649167, -20.933131259999563, -57.495633383772606), (1.3125, 1.3125, 1.3125), "PWM_Nordic_1x1x1_A11", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (11075.0, 6365.0, 2475.0), (-11.57690420092608, -55.073453094799476, 16.0343337386306), (1.0, 1.0, 1.0), "PWM_Nordic_1x1x1_A12_14", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (6668.723, 8550.739, 2075.0), (0.0, -67.50006435163657, 0.0), (1.0, 1.0, 1.0), "PWM_Nordic_1x1x1_A13_22", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (6772.683, 8317.909, 1866.3304), (-36.1037602071313, -61.28965044897146, -100.46346544340446), (1.0, 1.0, 1.0), "PWM_Nordic_1x1x1_A14", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2322.5276, 6895.0, 1019.34204), (90.0, -8.373743112162964e-05, 5.2866301420007286e-05), (1.78125, 1.375, 1.0), "PWM_Nordic_1x1x1_A15_26", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2274.8916, 6905.0, 1218.5753), (-81.56245087623978, -9.155266520357475e-05, 3.2673419480940046e-12), (1.78125, 1.28125, 1.0), "PWM_Nordic_1x1x1_A16", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3913.0, 2390.0, 767.0), (0.0, 0.0, -0.0), (1.0, 1.0, 1.0), "PWM_Nordic_1x1x1_A2_194", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (7781.0864, 3839.276, 900.0414), (0.0, 0.0, -0.0), (1.0, 1.0, 1.0), "PWM_Nordic_1x1x1_A3", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (6128.1426, 6859.206, 891.27625), (0.0, 166.43590942088454, -0.0), (1.691643, 1.691643, 1.691643), "PWM_Nordic_1x1x1_A4", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (8455.957, 7668.032, 2220.0), (8.437484046686839, -36.56155442037773, 1.4604887954999164e-05), (1.09375, 1.09375, 1.09375), "PWM_Nordic_1x1x1_A5_5", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (7723.4453, 9643.074, 1149.6323), (-13.934356735290589, -19.679780697406613, -12.765286925831393), (1.0, 1.0, 1.0), "PWM_Nordic_1x1x1_A6_8", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (10167.103, 5207.723, 2220.9883), (18.112314325400828, 5.772811423394535e-06, -87.51013093044394), (2.4848351, 2.4848351, 2.4848351), "PWM_Nordic_1x1x1_A7_549", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (10300.623, 5365.263, 2259.0635), (15.81663662292153, 152.96731037311798, -95.69747895650016), (2.484835, 2.484835, 2.484835), "PWM_Nordic_1x1x1_A8", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (10605.423, 10263.03, 1231.9517), (46.22960026252617, 112.9241322382813, -20.865444578105254), (1.0, 1.0, 1.0), "PWM_Nordic_1x1x1_A9", _folder)
if a: placed += 1
else: skipped += 1

# Batch 58: StaticMesh'PWM_Nordic_1X1x1_B' (7 instances)
_mesh_path = "/Game/Unshippable/Whitebox/Rocks/Meshes/PWM_Nordic_1X1x1_B"
_materials = ['/Game/Unshippable/Whitebox/Rocks/Materials/PWM_Nordic_Atlas_A']
_folder = "Reconstruction/BD_BB_Chapter3_HeadwaterNexus/Meshes"
a = spawn_static_mesh(_mesh_path, _materials, (10588.087, 7575.319, 815.5996), (0.0, 136.93838376568686, -0.0), (1.776378, 1.776378, 1.776378), "PWM_Nordic_1X1x1_B_53", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (8274.129, 837.0572, 693.2477), (0.002124786243513139, -179.99992486791044, 174.99994463693412), (1.2763537, 1.0, 0.7653128), "PWM_Nordic_1X1x1_B2_83", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4468.8105, 3491.7825, 962.1714), (22.0873469529033, 107.29393188206608, -0.5482191282363718), (1.4194369, 1.4194369, 1.4194369), "PWM_Nordic_1X1x1_B3", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (9520.0, 2375.0, 785.0), (0.0, -20.000060948281234, 0.0), (0.60622615, 0.60622615, 0.60622615), "PWM_Nordic_1X1x1_B4_118", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (9425.0, 8145.0, 755.0), (0.0, 0.0, -0.0), (1.0, 1.0, 1.0), "PWM_Nordic_1X1x1_B7_47", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (8689.526, 8913.93, 719.9999), (0.0, 155.1691454338542, -0.0), (0.9009008, 1.0, 1.0), "PWM_Nordic_1X1x1_B8_59", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (8840.0, 8365.0, 750.0), (0.0, 0.0, -0.0), (0.33851054, 0.33851054, 0.33851054), "PWM_Nordic_1X1x1_B9_83", _folder)
if a: placed += 1
else: skipped += 1

# Batch 59: StaticMesh'PWM_Nordic_1X1x1_C' (6 instances)
_mesh_path = "/Game/Unshippable/Whitebox/Rocks/Meshes/PWM_Nordic_1X1x1_C"
_materials = ['/Game/Unshippable/Whitebox/Rocks/Materials/PWM_Nordic_Atlas_A']
_folder = "Reconstruction/BD_BB_Chapter3_HeadwaterNexus/Meshes"
a = spawn_static_mesh(_mesh_path, _materials, (8742.424, 8726.262, 719.31885), (15.5766743134917, 12.065697242467756, 3.285057627650682), (1.0, 1.6271341, 0.58975655), "PWM_Nordic_1X1x1_C12_68", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (9366.349, 2519.6255, 719.99963), (2.0490563205243858e-05, 19.99973036123256, -179.99995901885825), (1.0, 2.230774, 0.534987), "PWM_Nordic_1X1x1_C2", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (9234.159, 2788.6814, 745.0), (0.0, 25.00002637632099, -0.0), (1.0, 1.2801781, 1.0), "PWM_Nordic_1X1x1_C3_112", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (8887.612, 3531.854, 760.0), (0.0, 40.00003313626452, -0.0), (1.0, 1.280178, 1.0), "PWM_Nordic_1X1x1_C4", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (11651.086, 5484.963, 2195.7805), (0.7381930766271958, 91.49120842654922, -177.0330297257347), (3.446317, 3.446317, 3.446317), "PWM_Nordic_1X1x1_C5", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (10741.86, 7296.1567, 765.61505), (11.36047566345183, 12.718818765470946, 10.638363135933082), (1.6304195, 1.6304195, 1.6304195), "PWM_Nordic_1X1x1_C7", _folder)
if a: placed += 1
else: skipped += 1

# Batch 60: StaticMesh'PWM_Nordic_1X1x1_D' (7 instances)
_mesh_path = "/Game/Unshippable/Whitebox/Rocks/Meshes/PWM_Nordic_1X1x1_D"
_materials = ['/Game/Unshippable/Whitebox/Rocks/Materials/PWM_Nordic_Atlas_A']
_folder = "Reconstruction/BD_BB_Chapter3_HeadwaterNexus/Meshes"
a = spawn_static_mesh(_mesh_path, _materials, (9290.0, 1520.0, 755.0), (0.0, 0.0, -0.0), (1.0, 1.0, 1.0), "PWM_Nordic_1X1x1_D_96", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (11786.659, 4900.5444, 1943.8265), (8.308890468717447, 86.31853391085366, 16.35741923418368), (5.902312, 5.902312, 10.115876), "PWM_Nordic_1X1x1_D10_316", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2855.0, 2885.0, 765.0), (0.0, 0.0, -0.0), (1.0, 1.0, 1.0), "PWM_Nordic_1X1x1_D2_218", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (6207.839, 7163.324, 1770.3269), (20.386291049605894, 67.1453859874809, 22.303310656577086), (3.3480601, 3.4209182, 4.7296863), "PWM_Nordic_1X1x1_D24_241", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (6250.8584, 10669.9375, 1346.2104), (15.000002841930657, -172.6444032991469, 2.475120005006535e-06), (2.457846, 2.457846, 2.457846), "PWM_Nordic_1X1x1_D3", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5631.934, 10747.749, 1379.1455), (-24.58124229121911, 62.710337463435785, -164.2118819565073), (1.6522793, 1.6522793, 1.6522793), "PWM_Nordic_1X1x1_D4", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (9886.547, 10773.364, 1299.5896), (0.0, 48.8437452867911, -0.0), (2.4906878, 2.4906878, 2.4906878), "PWM_Nordic_1X1x1_D5_577", _folder)
if a: placed += 1
else: skipped += 1

# Batch 61: StaticMesh'PWM_Nordic_2x2x2_A' (78 instances)
_mesh_path = "/Game/Unshippable/Whitebox/Rocks/Meshes/PWM_Nordic_2x2x2_A"
_materials = ['/Game/Unshippable/Whitebox/Rocks/Materials/PWM_Nordic_Atlas_B']
_folder = "Reconstruction/BD_BB_Chapter3_HeadwaterNexus/Meshes"
a = spawn_static_mesh(_mesh_path, _materials, (10049.02, 10241.463, 1794.8839), (-2.888275153507602, -4.828796305486302, -30.81625227549763), (1.0, 1.0, 1.0), "PWM_Nordic_2x2x2_A_2", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1416.1532, 3573.7007, 1027.3131), (-1.6431579074285816, 73.68682575428399, -176.69805530411355), (2.226, 2.226, 2.226), "PWM_Nordic_2x2x2_A10", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1644.657, 3280.284, 739.95496), (5.045352141630034, -102.97502954059071, 179.33642296550528), (2.226, 2.226, 2.226), "PWM_Nordic_2x2x2_A11", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2094.7869, 3214.4646, 586.8765), (-0.5849913891803153, 1.4902851287285384, -176.19401660036377), (3.2746408, 2.226, 2.226), "PWM_Nordic_2x2x2_A12", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (9048.697, 3396.8247, 724.7068), (9.96155592330882, 30.075982196432403, -179.11940886882635), (0.572358, 1.702445, 0.312117), "PWM_Nordic_2x2x2_A13", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1804.2251, 2023.3625, 852.3145), (5.270864081342711, 60.629457913504076, -177.86947297664264), (2.226, 2.226, 2.226), "PWM_Nordic_2x2x2_A14", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1422.8868, 2119.6428, 860.57275), (2.269152809682163, 81.64193826045296, 177.8581263702609), (2.226, 2.226, 2.226), "PWM_Nordic_2x2x2_A15", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (7096.7275, 1445.6432, 775.17), (4.0981123925211455e-05, -179.8444355372657, -179.99995901885643), (1.8786547, 1.4219083, 1.9444665), "PWM_Nordic_2x2x2_A16", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2006.9279, 1746.6293, 851.1012), (2.222693759763678, 105.63266230371745, -174.76698124434947), (3.1147854, 2.226, 2.226), "PWM_Nordic_2x2x2_A17", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (7006.6426, 1029.0588, 1181.8975), (-2.213042958670229, 174.7122059014846, -179.9564711987998), (1.878655, 1.421908, 1.4737687), "PWM_Nordic_2x2x2_A18", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (8760.0, 3550.0, 750.0), (0.0, 0.0, -0.0), (1.0, 1.0, 1.0), "PWM_Nordic_2x2x2_A19_141", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (8506.738, 763.03015, 527.64246), (-0.43399043277280525, -164.97993095434353, -177.19866682621327), (2.7261178, 2.0027645, 1.8240982), "PWM_Nordic_2x2x2_A2_86", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (9511.508, 6874.4873, 2405.8564), (2.0006522852857304e-05, -56.24917532440011, 112.49963623814232), (1.0, 1.0, 1.0), "PWM_Nordic_2x2x2_A20_18", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3839.5415, 7843.2314, 470.35016), (1.0528941756797745, -0.8831175304385614, 179.15343109736904), (3.731608, 3.731608, 3.397462), "PWM_Nordic_2x2x2_A21", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1867.2097, 2290.967, 757.67737), (0.0, -18.465028584697453, 0.0), (2.226, 2.226, 2.226), "PWM_Nordic_2x2x2_A22", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5700.376, 2093.96, 1380.8243), (0.0001092830123380623, 150.15580469391148, 179.99997950942625), (1.878655, 1.4863586, 1.5540414), "PWM_Nordic_2x2x2_A23_50", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (6476.199, 1307.4684, 922.32983), (-0.6036680949576693, 101.84704733267054, -176.2514432628923), (2.226, 2.226, 2.226), "PWM_Nordic_2x2x2_A24_12", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (6523.7183, 1620.156, 1022.0707), (1.1671016815131054, 90.15532002614945, -177.21731214485476), (1.878655, 1.421908, 1.473769), "PWM_Nordic_2x2x2_A25", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (6391.3955, 1782.206, 1019.03015), (-1.538024491225348, -174.87305129506407, -178.96253458070822), (1.878655, 1.421908, 1.473769), "PWM_Nordic_2x2x2_A26", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (6685.513, 1007.6119, 1082.3622), (1.2723274994265472, 77.59659492333137, -178.93854614934853), (2.226, 2.226, 2.226), "PWM_Nordic_2x2x2_A27", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2444.1658, 8992.077, 2234.0417), (-25.384094524448695, -172.7876937872401, 137.2138955532586), (1.78125, 1.78125, 1.78125), "PWM_Nordic_2x2x2_A28_33", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (7480.1885, 4046.545, 1043.0677), (0.00016399998979781339, 90.15535896413967, 179.99992486791697), (1.878655, 1.421908, 1.473769), "PWM_Nordic_2x2x2_A29", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (9134.395, 921.6556, 785.0), (0.0, -140.0000576472962, 0.0), (1.0, 1.0, 1.0), "PWM_Nordic_2x2x2_A3_93", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (9303.333, 4492.647, 985.75995), (-5.726593654709977, -97.3568173563495, 177.88011654536425), (2.2051008, 1.7483535, 1.8002145), "PWM_Nordic_2x2x2_A30", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (10667.546, 5616.248, 1004.85736), (-1.7517089544224669, -83.14279437940847, -175.37430329912735), (1.878655, 1.421908, 1.473769), "PWM_Nordic_2x2x2_A31", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (10685.2, 5305.561, 1015.48315), (3.7129029043361546, -98.92291325335914, 179.39519036645262), (2.5146482, 1.421908, 1.473769), "PWM_Nordic_2x2x2_A32", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (10778.181, 4938.867, 1029.8105), (0.7589011997574544, -17.18804938264526, -179.02089409352715), (2.6226623, 1.753873, 1.473769), "PWM_Nordic_2x2x2_A33", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (10952.568, 4901.079, 1005.45544), (-1.2049254645305185, 90.15527722961345, -179.9998976145762), (2.622662, 2.2290726, 1.6442312), "PWM_Nordic_2x2x2_A34", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (10950.972, 5488.1597, 1003.15045), (-2.7652585430931955, 90.15526759594707, -179.99989751121265), (2.622662, 2.229073, 1.473769), "PWM_Nordic_2x2x2_A35", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (10917.569, 5991.765, 1043.0676), (-0.00018310547718373556, -119.84472740040349, 179.99982241508533), (2.9761257, 2.229073, 1.473769), "PWM_Nordic_2x2x2_A36", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5418.0566, 2180.8193, 1393.064), (-0.00018310547239777962, 10.943341611730842, 179.99992486792402), (1.878655, 1.421908, 1.473769), "PWM_Nordic_2x2x2_A37_52", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (9392.132, 2309.6467, 790.0), (0.0, 140.00013702358888, -0.0), (0.7562672, 0.7562672, 0.7562672), "PWM_Nordic_2x2x2_A4_102", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (8101.525, 6523.953, 668.54407), (-2.3488150771443563, 145.0863003331845, -176.64156491438283), (2.976126, 3.0331807, 1.473769), "PWM_Nordic_2x2x2_A40_28", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (8628.406, 6331.797, 699.2344), (4.097668835262965, 20.155150667025495, -179.99988391586334), (2.976126, 2.229073, 1.473769), "PWM_Nordic_2x2x2_A41", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (8970.847, 5771.3584, 708.5687), (-0.00018318414797591687, 120.15502199293367, -175.36686447572015), (2.976126, 2.229073, 1.473769), "PWM_Nordic_2x2x2_A42", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5348.717, 10691.715, 1192.3077), (6.373207332020213, -56.44722898917398, -177.46629164860084), (1.878655, 1.421908, 1.473769), "PWM_Nordic_2x2x2_A43", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5367.977, 10509.376, 1276.2983), (-1.8011474428021699, 151.1981336917625, 170.19499766583164), (1.878655, 1.421908, 1.473769), "PWM_Nordic_2x2x2_A44", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (9369.558, 10445.434, 786.6107), (0.9090503484238692, 3.757201357074724, -179.9372920165888), (3.979993, 3.7166128, 2.4776359), "PWM_Nordic_2x2x2_A45", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (8659.894, 10239.632, 729.9236), (-0.2603149106974283, 18.841060422115078, -179.89558001101503), (3.979993, 3.23294, 2.9005337), "PWM_Nordic_2x2x2_A46", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4823.488, 11408.224, 895.94586), (7.661776624697179, -81.37352774667913, -176.91960898591213), (3.731608, 3.731608, 3.397462), "PWM_Nordic_2x2x2_A47", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5007.4473, 11054.03, 978.90576), (2.1044011856133933, -27.72808213412097, -171.9934130960238), (3.731608, 3.731608, 3.397462), "PWM_Nordic_2x2x2_A48", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (8436.457, 6710.773, 654.22345), (-0.00021362304297797873, 125.15515892790977, -179.99963116977466), (3.6723495, 2.7023928, 1.473769), "PWM_Nordic_2x2x2_A49", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5365.4194, 5277.992, 2289.3628), (-9.594023692715737, 79.13607421541482, 156.59854017401673), (1.2822747, 1.2822747, 1.2822747), "PWM_Nordic_2x2x2_A5_45", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (9210.641, 10044.246, 538.6239), (0.2626822097243488, 164.87634536033025, -179.9796460339754), (3.979993, 3.23294, 2.900534), "PWM_Nordic_2x2x2_A50", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1080.1866, 3604.4941, 992.8055), (-0.8822020627037896, -6.90716538725283, -173.78674309219235), (2.262883, 2.262883, 2.380894), "PWM_Nordic_2x2x2_A52_69", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1954.4869, 3360.8582, 712.3374), (0.007511628514448843, 10.448842098375016, -174.46590146536815), (2.262883, 2.262883, 2.380894), "PWM_Nordic_2x2x2_A53", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (7273.287, 1672.6935, 629.30194), (-1.2463989363702643, -93.0633513252022, 178.62571913565642), (1.878655, 1.421908, 1.473769), "PWM_Nordic_2x2x2_A54", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (7016.945, 1750.9114, 624.4607), (-1.4369506483405114, 179.892827489107, -178.82635493437996), (1.878655, 1.421908, 1.473769), "PWM_Nordic_2x2x2_A55", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (7097.207, 1267.1787, 775.16974), (4.0999991442317436e-05, -179.8444355372657, -179.99995901885717), (1.878655, 1.421908, 1.878655), "PWM_Nordic_2x2x2_A56", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (7039.93, 1903.8977, 634.3243), (1.0973517195497047, 159.9068525271919, -179.79449996966605), (1.878655, 1.421908, 1.473769), "PWM_Nordic_2x2x2_A57", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (8655.578, 10801.961, 1045.3887), (-0.4397278020267371, -169.4189477370879, -179.99989754570797), (3.979993, 3.23294, 2.477636), "PWM_Nordic_2x2x2_A58", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4931.3564, 10605.17, 694.4266), (1.6033998357600687, -48.38292737644974, -173.1398530183013), (3.731608, 3.731608, 3.397462), "PWM_Nordic_2x2x2_A59", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (9320.0, 2820.0, 760.0), (0.0, 0.0, -0.0), (1.0, 1.0, 1.0), "PWM_Nordic_2x2x2_A6_121", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (10751.503, 4596.7866, 1033.326), (2.7609935541654984, -55.463957360193774, -174.40930840826059), (3.0914164, 1.5619746, 1.473769), "PWM_Nordic_2x2x2_A61", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5009.427, 10717.911, 784.99805), (-6.896788861496606, 65.5739091469697, 178.5647350870779), (3.731608, 3.731608, 3.397462), "PWM_Nordic_2x2x2_A62", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (9393.964, 10644.834, 953.51514), (-0.437591501730964, -175.2231525028278, -179.95490708219415), (3.979993, 3.5748522, 2.477636), "PWM_Nordic_2x2x2_A63", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (9029.255, 10623.12, 947.6172), (-0.4112548636628504, 169.8681641863286, -179.84371154864237), (3.979993, 3.23294, 2.477636), "PWM_Nordic_2x2x2_A64", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4376.2637, 10335.109, 756.93365), (6.401066648301641, -128.3331258876354, -179.9216851645488), (1.3963248, 1.3963248, 1.3963248), "PWM_Nordic_2x2x2_A65", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4190.1357, 10482.643, 759.3851), (6.401061728592913, -128.33361812094594, -178.8009111194509), (1.396325, 1.396325, 1.396325), "PWM_Nordic_2x2x2_A66", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (8680.0, 8875.0, 765.0), (0.0, 0.0, -0.0), (1.0, 1.0, 1.0), "PWM_Nordic_2x2x2_A67_62", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (8798.344, 8511.097, 728.22833), (-6.612822796742906, -172.58897493874505, -178.44483385866064), (0.67981577, 1.008012, 0.2678437), "PWM_Nordic_2x2x2_A68_74", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (9088.878, 11404.235, 1240.5334), (-0.5716855435325319, -164.12693831830595, 179.98323188267196), (3.979993, 3.574852, 2.477636), "PWM_Nordic_2x2x2_A69", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (6998.4346, 1377.371, 768.1256), (-1.366037697190128e-05, -99.84461340369283, 179.99999999999937), (1.8977945, 1.8977945, 1.8977945), "PWM_Nordic_2x2x2_A7_337", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (8756.512, 11252.526, 1234.6943), (-0.4399109191756336, -169.00524356407362, 179.99756162439724), (3.979993, 3.23294, 2.477636), "PWM_Nordic_2x2x2_A70", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (11808.684, 6408.925, 1330.232), (-0.008148189055989775, -81.28067662747587, -179.43514106705254), (3.979993, 3.574852, 2.477636), "PWM_Nordic_2x2x2_A71", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (11824.214, 6049.904, 1330.1633), (0.5573230143410381, -96.19044649349321, -179.56329729671768), (3.979993, 3.23294, 2.477636), "PWM_Nordic_2x2x2_A72", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (12164.655, 6469.306, 1384.8339), (1.2812200606306776, -72.93713242118437, 172.06957914163283), (5.429177, 4.083063, 2.5860536), "PWM_Nordic_2x2x2_A73", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (11537.664, 6138.994, 1192.4247), (1.9159757884387776, -99.71067807300086, -179.66101711082592), (3.979993, 3.23294, 2.477636), "PWM_Nordic_2x2x2_A74", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (11185.213, 6217.646, 932.675), (-0.7064514673675447, -35.340819389860556, 177.91426609914984), (2.9466147, 3.23294, 2.477636), "PWM_Nordic_2x2x2_A75", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5340.611, 11756.616, 1173.4298), (1.654804149178205, 134.95904596494228, 179.47606094565842), (4.692668, 4.692538, 3.397462), "PWM_Nordic_2x2x2_A76_49", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5704.0635, 11557.431, 1201.8455), (-1.049347214593735, -121.26028757865262, 178.02810250682518), (4.692668, 4.692538, 3.397462), "PWM_Nordic_2x2x2_A77_51", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (6032.151, 887.297, 1256.977), (0.9826797481015501, -47.13302208762225, -170.98657048045973), (5.429177, 4.083063, 2.586054), "PWM_Nordic_2x2x2_A78", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1505.3828, 1629.8053, 806.46594), (2.0257790238840774, 42.22728783733112, -176.25034120309593), (4.5076556, 4.083063, 2.7466614), "PWM_Nordic_2x2x2_A79", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (8192.037, 757.15564, 633.8267), (-0.43399043277280525, -164.97993095434353, -177.19866682621327), (1.860549, 1.137196, 0.95853), "PWM_Nordic_2x2x2_A8_108", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1353.876, 3908.6682, 955.2826), (1.8669775404937325, -0.7233887396956351, -178.63284381847177), (3.7907484, 4.083063, 2.746661), "PWM_Nordic_2x2x2_A80", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (11181.386, 6425.88, 1230.5583), (2.1579422287260117, -132.4333608530595, 178.97906436890915), (1.6091479, 1.6091479, 1.6091479), "PWM_Nordic_2x2x2_A81_56", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4057.9214, 10559.79, 764.9873), (-2.0420225425963197, 112.82847771128829, 173.81454082562908), (1.396325, 1.396325, 1.396325), "PWM_Nordic_2x2x2_A82", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (9271.4795, 2930.786, 725.5828), (9.96155592330882, 30.075982196432403, -179.11940886882635), (0.5723577, 1.7024451, 0.31211668), "PWM_Nordic_2x2x2_A9_125", _folder)
if a: placed += 1
else: skipped += 1

# Batch 62: StaticMesh'PWM_Nordic_4x4x4_A' (146 instances)
_mesh_path = "/Game/Unshippable/Whitebox/Rocks/Meshes/PWM_Nordic_4x4x4_A"
_materials = ['/Game/Unshippable/Whitebox/Rocks/Materials/PWM_Nordic_Atlas_B']
_folder = "Reconstruction/BD_BB_Chapter3_HeadwaterNexus/Meshes"
a = spawn_static_mesh(_mesh_path, _materials, (11765.913, 5866.874, 2640.4238), (0.0, 0.0, -0.0), (1.9254597, 1.9254597, 1.9254597), "PWM_Nordic_4x4x4_A_30", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (9188.451, 5678.9883, 755.43), (0.0, 134.10890951770202, -0.0), (1.0, 1.0, 1.0), "PWM_Nordic_4x4x4_A10_554", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5502.718, 2400.2024, 2424.2253), (-11.885990090448775, -74.03716688180187, 99.41538618755665), (1.157702, 1.157702, 1.157702), "PWM_Nordic_4x4x4_A100", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5028.861, 2829.113, 2056.595), (-11.833312226432003, -40.456387246390946, 91.5668893771208), (1.5630666, 1.5630666, 1.5630666), "PWM_Nordic_4x4x4_A101", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (6338.785, 4180.3896, 2187.3596), (-16.880556971402196, -143.79040290366726, 93.32041506322258), (1.0, 1.0, 1.0), "PWM_Nordic_4x4x4_A102", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (6673.541, 3997.2427, 2243.0442), (-13.886933895475787, -172.7959356494969, 100.44341396940361), (1.6820631, 1.6050614, 1.6050614), "PWM_Nordic_4x4x4_A103", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (6266.091, 2822.6772, 2402.7231), (-16.425199308416353, -26.437070842198768, 103.70842349302406), (1.563067, 1.563067, 1.563067), "PWM_Nordic_4x4x4_A104_304", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5934.993, 2899.6843, 2452.639), (-9.352756617845465, 77.57171790373248, 86.99162810903643), (1.563067, 1.563067, 1.563067), "PWM_Nordic_4x4x4_A105", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (6462.8667, 2324.203, 2515.4202), (-11.158875549028341, -139.3299635700587, 85.73707671582683), (1.3029166, 1.3029166, 1.3029166), "PWM_Nordic_4x4x4_A106", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5872.647, 1843.7849, 2396.9392), (-9.34103330760438, 45.8627370385114, -173.33411549156742), (1.463543, 1.463543, 1.463543), "PWM_Nordic_4x4x4_A107_373", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (8690.0, 8815.0, 730.0), (0.0, 0.0, -0.0), (0.6372801, 0.5421172, 0.33766264), "PWM_Nordic_4x4x4_A108_65", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (7813.789, 3956.5352, 1919.3306), (-4.308622577063639, 167.16270089579788, 96.59487623601773), (1.0, 1.0, 1.0), "PWM_Nordic_4x4x4_A109", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (6270.4185, 8174.7505, 1123.0616), (0.0, 112.09453277950362, -0.0), (0.73554575, 0.73554575, 0.73554575), "PWM_Nordic_4x4x4_A11_128", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (7972.243, 3615.4436, 1889.6317), (-16.347960011663677, -63.56317495045653, 83.98636179625679), (1.0, 1.0, 1.0), "PWM_Nordic_4x4x4_A110", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (7853.427, 3927.604, 1648.2515), (-14.49643120912001, -133.787891525478, 92.92349696539382), (1.0, 1.0, 1.2756295), "PWM_Nordic_4x4x4_A111", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (7935.249, 4130.7163, 925.0555), (-10.469361451598976, -86.2287227258967, 91.57373338163279), (1.0, 1.4655962, 1.0), "PWM_Nordic_4x4x4_A112_411", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (7584.607, 3089.0085, 1806.886), (5.1958963495750945, -177.09101042052603, -175.0901589603442), (1.1255431, 0.7774262, 1.0), "PWM_Nordic_4x4x4_A113", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (7737.2217, 3495.5347, 1672.3391), (1.3318523681518726, -108.59149538782236, -174.90060545741596), (1.0, 0.717851, 1.0), "PWM_Nordic_4x4x4_A114", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (7690.072, 3219.8054, 1962.5511), (5.195896889127015, 172.12817547778337, -175.0901585556461), (1.0, 0.717851, 1.0), "PWM_Nordic_4x4x4_A115", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (7483.442, 3371.168, 1699.7738), (-10.469361451598976, -86.2287227258967, 91.57373338163279), (1.0, 1.465596, 1.0), "PWM_Nordic_4x4x4_A116_414", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (7673.219, 2843.8733, 2170.5442), (3.5368559040548138, -96.40962388748363, -175.32042996939927), (1.2912139, 1.0090646, 1.2912139), "PWM_Nordic_4x4x4_A117_424", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (7534.6455, 2058.0493, 2309.051), (3.5368556751262576, -96.40962389231208, -175.3204297135181), (1.6796603, 1.009065, 1.291214), "PWM_Nordic_4x4x4_A118", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (8333.721, 3456.4731, 2308.657), (-6.94689725072604, -166.63623973412527, -171.50727175433627), (1.291214, 1.009065, 1.291214), "PWM_Nordic_4x4x4_A119", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3787.7769, 1662.2764, 1857.4856), (3.301756615908101, 177.68286987684036, -179.99998634162452), (1.1725017, 1.1725017, 1.1725017), "PWM_Nordic_4x4x4_A12_30", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (8713.638, 8603.591, 711.1384), (-12.194581917388224, 179.40744442233262, 1.1290835186164405), (0.37438628, 0.6580647, 0.14213835), "PWM_Nordic_4x4x4_A120_71", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (7837.276, 2752.5908, 2152.3872), (-8.775908272909918, -62.72064505999414, 91.50305871941919), (1.0, 1.0, 1.0), "PWM_Nordic_4x4x4_A121", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (11073.221, 1205.6903, 1994.1844), (-19.90261877599141, 169.26612991724917, 91.92101024670664), (1.0, 1.0, 1.0), "PWM_Nordic_4x4x4_A122", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (9206.135, 5332.7656, 1659.7847), (-6.78021186066194, -29.58160615989701, 93.69994691160872), (0.8030348, 1.0, 1.0), "PWM_Nordic_4x4x4_A123", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (7661.969, 8365.901, 1802.1212), (-79.17551171597705, -169.71095089987028, -145.1256591803462), (1.0, 1.0, 1.0), "PWM_Nordic_4x4x4_A124", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (7320.984, 8323.625, 1710.2075), (-79.17636295283991, -125.2284175616756, -145.1265066515934), (1.0, 1.388152, 1.0), "PWM_Nordic_4x4x4_A125", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (7441.6396, 8365.451, 1342.8226), (79.59512818255303, -68.05299944141561, 21.52598128121505), (1.0, 1.0, 1.0), "PWM_Nordic_4x4x4_A126", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (9427.857, 4726.629, 1905.187), (-15.947632487540737, -64.40264812486403, 90.2982309084367), (0.803035, 1.0, 1.0), "PWM_Nordic_4x4x4_A127", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (9624.562, 5038.496, 1941.9646), (-4.919340716088807, -62.81237863748831, 90.72369723200043), (0.8076517, 1.0, 1.0), "PWM_Nordic_4x4x4_A128", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (8108.705, 9924.78, 2321.5193), (1.3090057547971825, -89.56570714848353, -166.62152518112228), (1.571629, 1.571629, 1.571629), "PWM_Nordic_4x4x4_A129", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1605.1675, 3240.7388, 2151.707), (-3.5677498405718633, -114.35851080771644, -178.8898790370979), (0.9552408, 1.0, 1.0), "PWM_Nordic_4x4x4_A13_3", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (8210.542, 9665.547, 2421.1787), (-0.9206534060642053, 87.5737615522716, -97.84606324969852), (1.571629, 1.571629, 1.571629), "PWM_Nordic_4x4x4_A130", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (10415.67, 9274.509, 2130.9883), (11.662797329152415, 99.08461162629116, -166.656713907076), (0.8954642, 0.8954642, 0.8954642), "PWM_Nordic_4x4x4_A131", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (11458.632, 9162.743, 2118.8027), (11.662819718760508, 99.08514637597338, -171.79522765000218), (0.895464, 0.895464, 0.895464), "PWM_Nordic_4x4x4_A132", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (7192.019, 8420.847, 1678.3964), (-82.3329780160872, -154.8823235518291, -125.36934277079484), (1.4053007, 1.3017188, 1.3017188), "PWM_Nordic_4x4x4_A133", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (10926.217, 1096.1774, 2030.4854), (-5.311004380846251, -176.9436130859723, -178.3295224568708), (1.291214, 1.1594361, 1.291214), "PWM_Nordic_4x4x4_A134", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (10459.617, 2114.6736, 2473.5085), (2.3333356490800448, 159.3672428787037, -177.14741720255444), (1.5198164, 1.6415908, 1.6313461), "PWM_Nordic_4x4x4_A135", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (8815.49, 8663.36, 703.85095), (-5.163176556664864, -31.169063649183258, 60.00388302104416), (0.530224, 0.530224, 0.530224), "PWM_Nordic_4x4x4_A136", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (7868.0806, 1047.8383, 2320.0354), (-33.92629981431427, 44.82262939092567, 152.04341146307118), (1.519816, 1.388038, 1.519816), "PWM_Nordic_4x4x4_A137", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (11969.566, 3020.4749, 2087.8323), (-35.54839775717633, -149.98137106503208, 163.36923592234274), (1.4778976, 1.7318889, 1.6151731), "PWM_Nordic_4x4x4_A138", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (11722.365, 3388.965, 1997.5748), (-6.066161440947949, -131.2111126481786, 168.92849356188663), (1.0, 1.0706758, 1.0), "PWM_Nordic_4x4x4_A139", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4679.228, 1477.3545, 2552.082), (-51.79355332884692, -9.226314028608144, -179.99998701388932), (2.757396, 2.757396, 2.757396), "PWM_Nordic_4x4x4_A14", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (11643.755, 3805.7588, 1999.0111), (-11.34228677640469, 140.91772499744803, -174.46198346583316), (1.0, 1.0, 1.0), "PWM_Nordic_4x4x4_A140", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (9254.705, 4519.494, 1833.4325), (-16.347960011663677, -63.56317495045653, 83.98636179625679), (1.0, 1.0, 1.0), "PWM_Nordic_4x4x4_A141", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (8897.912, 4327.852, 1828.8612), (-11.96731802406606, 119.38269325491109, 92.0357646448748), (1.0, 1.2661946, 1.1652756), "PWM_Nordic_4x4x4_A142", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (8745.538, 4725.5303, 1452.2606), (-9.035308411395574, 119.77648007741358, 89.64407178245371), (1.0, 1.0, 1.0), "PWM_Nordic_4x4x4_A143", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (8966.785, 4728.042, 1576.265), (-9.035306870575678, -125.27618611525702, 89.64413544679287), (1.0, 1.0, 1.0), "PWM_Nordic_4x4x4_A144", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (9158.947, 4016.6362, 1848.0452), (-16.34786827874617, -92.801717180011, 83.98633920927273), (1.0, 1.0, 1.0), "PWM_Nordic_4x4x4_A145", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (10720.972, 8372.435, 1872.8428), (-75.04412765252239, -58.8919723355258, 173.29016936401672), (1.7241722, 1.7241722, 1.7241722), "PWM_Nordic_4x4x4_A146", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1143.1713, 2104.6465, 2083.1113), (1.7656503611291463, -18.404418132246775, -166.50147317163396), (1.771987, 1.0, 1.0), "PWM_Nordic_4x4x4_A147", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (6713.875, 1707.4012, 950.29865), (-42.19635728918947, -4.412295517946682, 98.52864296724769), (0.7975288, 0.699821, 0.632792), "PWM_Nordic_4x4x4_A148", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (6846.195, 3955.9902, 2068.9763), (-16.515256216972578, 152.56992189371505, 110.71304179559831), (1.682063, 1.605061, 1.605061), "PWM_Nordic_4x4x4_A149", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (9599.985, 5578.091, 2312.6133), (6.218464027213639, -9.689942511415335, 175.80834878960616), (1.3342494, 1.3342494, 1.3342494), "PWM_Nordic_4x4x4_A15", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (6524.9185, 4527.2715, 2094.2278), (-14.497315064874043, -134.74199741228108, 81.12038196214911), (1.682063, 1.605061, 1.605061), "PWM_Nordic_4x4x4_A150", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (7533.967, 9612.381, 2040.2706), (-7.308224968942529, -121.69268432570964, 172.26218236693933), (1.405301, 1.301719, 1.301719), "PWM_Nordic_4x4x4_A151", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (10164.444, 7539.5356, 2075.537), (-76.12392803506518, -25.93772993435713, -130.68251244255396), (1.0, 1.0, 1.0), "PWM_Nordic_4x4x4_A16", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5121.859, 3824.6282, 1759.9713), (27.393296774395377, -150.22624310010906, -159.36386648968764), (1.0, 0.71785074, 1.0), "PWM_Nordic_4x4x4_A17_51", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (10607.8, 7782.3364, 1673.9747), (-80.15442609264969, 0.00012791431707521544, -156.1000358603869), (1.0, 1.0, 1.0), "PWM_Nordic_4x4x4_A2_20", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (9257.545, 1421.4227, 750.0), (0.0, 70.00006109847311, -0.0), (0.5860712, 0.5860712, 0.5860712), "PWM_Nordic_4x4x4_A20_89", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4381.2734, 8107.8384, 2156.5398), (16.646725728328033, -85.09674297378862, -168.76859506349433), (1.0, 0.717851, 1.0), "PWM_Nordic_4x4x4_A21", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4569.298, 7933.528, 2223.2717), (2.257738838083864, 96.4144411006089, 165.8549687742288), (1.4014285, 1.4014285, 1.4014285), "PWM_Nordic_4x4x4_A22", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (6863.2124, 8258.359, 1128.5304), (0.0, 122.82001590022168, -0.0), (1.0, 1.0, 1.0), "PWM_Nordic_4x4x4_A24_132", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (895.0152, 11140.111, 2031.8391), (-8.5082080459963, -116.33815500283052, -177.2507007600498), (1.214643, 1.214643, 1.214643), "PWM_Nordic_4x4x4_A25", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1020.8466, 11653.766, 1817.321), (-3.3778686503326645, 160.6621145534524, -179.42845414769482), (1.214643, 1.214643, 1.214643), "PWM_Nordic_4x4x4_A26", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1805.9313, 10194.955, 2248.3193), (-2.7797546662819257, -94.41818668671642, -175.5830323911551), (1.4934652, 1.4934652, 1.3631839), "PWM_Nordic_4x4x4_A27", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (8089.9414, 7476.2285, 1930.9258), (-18.79382011164888, -1.9983825586138664, -178.0101697521041), (1.0, 1.0, 1.0), "PWM_Nordic_4x4x4_A28_42", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (8139.855, 7195.3887, 2068.8425), (-11.041931462781797, 8.885314968485414, -171.92017304892713), (1.3354676, 1.3354676, 1.3354676), "PWM_Nordic_4x4x4_A29", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (6276.9814, 5444.1465, 2172.5403), (1.639112939139183, 96.10934123862445, -171.48073346952415), (0.7889985, 0.7889985, 0.7889985), "PWM_Nordic_4x4x4_A3_12", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (9872.04, 5811.557, 2490.4883), (8.73171280689121, -0.18630981244762806, 175.78409090749327), (1.0, 1.0, 1.0), "PWM_Nordic_4x4x4_A30_90", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (8105.035, 7920.888, 1917.2126), (-18.878084177064505, -0.8383484338526551, 178.39781102737834), (1.0, 1.0, 1.3919839), "PWM_Nordic_4x4x4_A31", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (6030.9663, 5048.139, 2210.38), (-5.960692251654871, 105.87629146234492, 178.3082437090612), (1.0, 1.0, 1.0685434), "PWM_Nordic_4x4x4_A32_40", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (6495.866, 2009.1663, 887.40906), (1.2931118814670548, 93.36298459185822, 1.2829233012462355), (0.9791982, 1.0, 1.0), "PWM_Nordic_4x4x4_A33", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (9185.431, 3167.665, 722.83014), (4.923890947367469, 29.962618602103042, 179.12955206102578), (0.32864907, 0.42785406, 0.2080923), "PWM_Nordic_4x4x4_A34_128", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (8466.116, 3799.326, 710.14526), (4.530609142270013, 65.08383826277932, -177.88255512124482), (0.57945275, 1.5287038, 0.208092), "PWM_Nordic_4x4x4_A35", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (10101.041, 5586.5073, 2517.0222), (-6.2669972460105035, -179.3299270854622, -175.8809241348842), (1.0, 1.0, 1.0), "PWM_Nordic_4x4x4_A36_92", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (8994.754, 3456.679, 726.3041), (-4.5307308681173275, -114.91595657262589, 177.8824315546817), (0.328649, 0.427854, 0.208092), "PWM_Nordic_4x4x4_A37", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (10903.434, 8024.5244, 944.56433), (80.6580284746539, 119.82959076924733, 153.22875049100463), (1.0, 1.0, 1.0), "PWM_Nordic_4x4x4_A38", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (6252.5166, 2093.4373, 934.9786), (3.818901836289517, 28.23183377880268, -5.167389219201673), (1.0, 1.0, 1.253161), "PWM_Nordic_4x4x4_A4_139", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (6370.8115, 5408.555, 1801.1096), (3.5151360370913802, -178.59966023552965, 178.2375299002262), (0.670411, 1.0, 1.6118187), "PWM_Nordic_4x4x4_A40", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (6075.7344, 6925.6797, 2076.4836), (-0.4754332161874905, -164.0674341428531, 175.09404102026645), (1.0, 1.0, 1.0), "PWM_Nordic_4x4x4_A41_59", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4207.235, 7869.317, 1898.5062), (1.7296029480305566, 88.55860167444258, 177.2864129053312), (1.0, 1.0, 1.0), "PWM_Nordic_4x4x4_A42_75", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4241.5137, 8809.853, 2459.385), (-8.733399375015836, 89.38754861682213, 170.54684748167205), (1.7863271, 2.068085, 1.8405606), "PWM_Nordic_4x4x4_A43", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3657.9802, 8328.701, 2431.6777), (1.5732199254214614, 168.12196496819004, -179.42968356881624), (1.1363077, 1.9020525, 1.0), "PWM_Nordic_4x4x4_A44_84", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1441.5985, 10137.855, 750.0), (0.0, 15.000043495803544, -0.0), (0.47979146, 0.47979146, 0.47979146), "PWM_Nordic_4x4x4_A45_178", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3612.8792, 7991.795, 2543.102), (1.3864257584609632, -177.7466367788126, -179.06281246500274), (1.0, 1.0, 1.0), "PWM_Nordic_4x4x4_A46", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4039.4773, 2376.6384, 769.0), (0.0, 35.53176951214076, -0.0), (0.45795077, 0.45795077, 0.45795077), "PWM_Nordic_4x4x4_A47_191", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1071.2026, 2495.5994, 2022.9971), (-1.2268983500326496, -31.77239756303737, -167.98559551876812), (1.0, 1.0, 1.6395211), "PWM_Nordic_4x4x4_A48_44", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4432.9883, 2558.7134, 2090.8547), (4.470658400159831, -89.16100423732641, -168.09974004780833), (1.8893663, 1.8485626, 1.8485626), "PWM_Nordic_4x4x4_A49_539", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (11683.132, 6463.232, 2679.1157), (9.818260548763751, -87.04288704853703, 6.311174929352747e-07), (1.92546, 1.92546, 1.92546), "PWM_Nordic_4x4x4_A5", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4699.688, 3659.0925, 2663.1565), (-3.24597101140669, -81.63342443566786, -171.99102059183735), (2.583518, 2.583518, 2.583518), "PWM_Nordic_4x4x4_A50_621", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4761.1196, 3898.4592, 1634.1046), (3.818812966154728, 166.32798072284058, 94.74506804757638), (1.0, 1.0, 1.1474875), "PWM_Nordic_4x4x4_A51_102", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2093.9976, 1900.5507, 1945.1678), (-5.298919125383268, 53.21416582247986, -167.5347725800469), (1.0, 1.0, 1.0), "PWM_Nordic_4x4x4_A52_52", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5767.5757, 1843.2817, 2179.0322), (-3.0936889969094183, 74.973033569731, 179.4324773774531), (1.0, 1.0, 1.0), "PWM_Nordic_4x4x4_A53", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2401.679, 1817.6289, 1987.9047), (-8.46826025699863, 18.134064450227946, -156.69590454412545), (1.0, 1.0, 1.0), "PWM_Nordic_4x4x4_A54", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5176.518, 2042.3524, 2092.766), (9.52149967225727, 66.86200901264077, 176.55713417567983), (1.0, 1.0, 1.0), "PWM_Nordic_4x4x4_A55", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3838.7527, 2376.0625, 771.27985), (-1.4402767062761945, 170.06677619553503, 170.0994776822369), (1.0, 0.5701309, 0.08280325), "PWM_Nordic_4x4x4_A56_197", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1221.6932, 2361.4822, 2061.848), (1.4013291502586627, -16.888731144848503, -166.46139154690525), (1.0, 1.0, 1.0), "PWM_Nordic_4x4x4_A57", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2409.881, 1530.6027, 1843.9878), (-78.50196453304329, -45.66521518832958, 90.32629046502774), (1.0, 1.0, 1.0), "PWM_Nordic_4x4x4_A58_58", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5553.8325, 2080.3857, 2336.994), (-11.098389622944332, 69.88488307493066, -177.97383588079262), (1.4635434, 1.4635434, 1.4635434), "PWM_Nordic_4x4x4_A59", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5725.436, 2430.724, 2696.2053), (-4.443175445610442, 46.185053514514465, -178.14188124181194), (1.4226104, 1.4226104, 1.4226104), "PWM_Nordic_4x4x4_A6", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2371.1707, 1258.1604, 1792.6165), (-74.11743274281915, -70.71410897110157, 155.287231288054), (1.0, 1.0, 1.0), "PWM_Nordic_4x4x4_A60", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2569.1997, 1129.3928, 1768.1527), (-87.53184555046552, 88.4951247414499, -86.26303387843546), (1.0, 1.0, 1.0), "PWM_Nordic_4x4x4_A61_63", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4217.954, 1094.2701, 2194.9385), (4.8014930053678455, 157.39074013571638, 177.10425114557475), (2.757396, 2.757396, 2.757396), "PWM_Nordic_4x4x4_A62", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4933.9614, 3508.85, 1726.94), (-19.903197588817626, -66.87942205907896, 91.9212555197199), (1.0, 1.0, 1.0), "PWM_Nordic_4x4x4_A63_104", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2722.0186, 373.64963, 1784.1287), (-83.82369315241287, -3.0517590928924675e-05, -6.103517355405355e-05), (1.4196547, 1.4196547, 1.4196547), "PWM_Nordic_4x4x4_A64_72", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (6593.9727, 1740.7007, 859.07056), (-1.0839539164453567, 175.0949798798687, 1.4638926900385798), (1.168935, 0.79715705, 1.0), "PWM_Nordic_4x4x4_A65", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1747.3573, 1886.9187, 2043.9539), (-5.665068746124073, 127.80227003008744, 169.043856298396), (1.0, 1.0, 1.0), "PWM_Nordic_4x4x4_A66", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1724.0437, 1912.5385, 2026.4219), (-6.654968527095089, 122.52322645955033, 169.6105174061852), (1.3282115, 1.3105719, 1.0701493), "PWM_Nordic_4x4x4_A67", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (6150.6084, 4880.681, 2449.394), (0.7078599547882382, 168.20083649177522, 174.7135508546532), (1.9638294, 1.9638294, 1.9638294), "PWM_Nordic_4x4x4_A68_73", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5928.6885, 7469.9473, 2096.4587), (-2.7542112915031796, -177.52960213893547, 172.15304214792735), (2.9412465, 2.3857887, 2.1469905), "PWM_Nordic_4x4x4_A69", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (8048.107, 6787.8486, 1990.2231), (-9.063812387180985, -3.6079714389290105, -179.43065360654654), (1.0, 1.0, 1.0), "PWM_Nordic_4x4x4_A7_112", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (6271.2583, 8141.244, 2003.4464), (-10.112487449855887, 103.99682235218654, -177.7290116307909), (1.3688354, 1.3688354, 1.3688354), "PWM_Nordic_4x4x4_A70", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5334.571, 4532.589, 1887.231), (0.7570581015120955, -8.436584189283524, 176.71789086020883), (1.1947805, 1.2339976, 1.1947805), "PWM_Nordic_4x4x4_A71", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (6000.9214, 7986.1377, 2089.1177), (-10.112424915536094, 103.99681892634702, 176.9962561184479), (1.368835, 1.368835, 1.368835), "PWM_Nordic_4x4x4_A72_114", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5947.1455, 8099.054, 2161.3872), (-10.797791125139886, 137.18756299622598, 176.06239318255115), (1.368835, 1.368835, 1.368835), "PWM_Nordic_4x4x4_A73", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4770.7183, 7330.077, 1695.5536), (-5.396301623184566, 78.43581620563184, 172.60799003482168), (1.2319331, 1.2319331, 1.2319331), "PWM_Nordic_4x4x4_A74", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (6476.2583, 10370.115, 2476.2842), (-19.243620611612027, -112.48291518256768, 179.76607219930452), (1.368835, 1.368835, 1.368835), "PWM_Nordic_4x4x4_A75_477", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (7065.7627, 9960.253, 2479.7449), (-42.96246602246917, -35.726349155729714, 111.09708272950441), (1.368835, 1.368835, 1.368835), "PWM_Nordic_4x4x4_A76", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2780.5112, 10362.776, 2455.8774), (-12.303587691917114, -85.91772333577906, -164.75733101922157), (1.368835, 1.368835, 1.368835), "PWM_Nordic_4x4x4_A77", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5994.193, 7741.844, 1715.8999), (-0.8865052412243716, 173.38382149752894, 179.64508235256224), (1.0503054, 1.0503054, 1.0503054), "PWM_Nordic_4x4x4_A78", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5142.101, 4395.165, 1605.6254), (-1.8698116832052125, -85.79313464023384, -167.805492974707), (0.9880592, 0.9880592, 0.9880592), "PWM_Nordic_4x4x4_A79", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (9952.866, 5479.9844, 2374.1597), (6.218463468905668, 6.044690079439372e-08, 175.8083482600052), (1.0, 1.0, 1.0), "PWM_Nordic_4x4x4_A8_533", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5220.9214, 4674.2866, 2250.4446), (0.5774454032040541, -4.716430245280098, -178.91023362000107), (1.19478, 1.233998, 1.19478), "PWM_Nordic_4x4x4_A80", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5223.0747, 5112.977, 2379.8953), (-71.72582559781587, 170.01128420600227, -168.0215325481841), (1.3351599, 1.8459886, 1.3351599), "PWM_Nordic_4x4x4_A81", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5225.042, 5526.0923, 2108.4766), (-8.402589183633127, -4.888489603845001, -178.89836955823887), (0.9586918, 1.233998, 1.19478), "PWM_Nordic_4x4x4_A82", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (6376.6675, 5372.8125, 2459.762), (-1.5169359307056849, 80.67171506397311, -161.7087613576567), (1.451737, 1.451737, 1.451737), "PWM_Nordic_4x4x4_A83", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5244.937, 7040.872, 2403.0884), (-5.364379733417729, -0.7686766244455621, -166.4141762605684), (1.451737, 1.451737, 1.451737), "PWM_Nordic_4x4x4_A84", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2830.0, 2755.0, 750.0), (0.0, 0.0, -0.0), (0.5000404, 0.5000404, 0.5000404), "PWM_Nordic_4x4x4_A85_215", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (7406.223, 1725.6884, 635.3433), (9.83863563798237, 20.01024945851504, 4.775591789377341), (1.0, 1.0, 1.0), "PWM_Nordic_4x4x4_A86", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5914.507, 8049.944, 695.0), (0.0, 7.587397697498625, -0.0), (1.0, 1.3872797, 0.82782423), "PWM_Nordic_4x4x4_A87_221", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (7310.521, 1984.2303, 650.23145), (-1.8475622583623947, 64.22168912765385, -99.7039188486588), (0.683877, 0.683877, 0.6168482), "PWM_Nordic_4x4x4_A88", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (7426.199, 1933.829, 567.8723), (8.574954708015893, 32.59327994305477, 3.042070350875479), (1.0, 1.0, 1.0), "PWM_Nordic_4x4x4_A89", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1419.4446, 11478.8955, 1695.596), (-0.9592892002562721, -115.97724619748831, 176.71107716334382), (1.2146434, 1.2146434, 1.2146434), "PWM_Nordic_4x4x4_A9_198", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (7290.929, 1666.734, 874.3799), (2.123116525419913, 87.19070928583552, -93.17816267882581), (0.525908, 0.525908, 0.45887908), "PWM_Nordic_4x4x4_A91", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (7416.387, 1448.2598, 736.1993), (2.7378567453656015, 56.982830992289216, -94.66107965092407), (0.7943847, 0.7943847, 0.7273557), "PWM_Nordic_4x4x4_A92", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (6787.6436, 1998.337, 829.83636), (0.7618926205825018, 79.27772261395336, -97.14202399603094), (0.683877, 0.683877, 0.728378), "PWM_Nordic_4x4x4_A93", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (7344.3086, 1495.5829, 894.1879), (2.123116525419913, 87.19070928583552, -93.17816267882581), (0.525908, 0.525908, 0.458879), "PWM_Nordic_4x4x4_A94_122", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (6699.273, 1659.4467, 973.95746), (-33.989928987796766, 4.258659294955635, 108.75063266013088), (0.6604124, 0.6998211, 0.6327921), "PWM_Nordic_4x4x4_A95", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (7896.9956, 9399.748, 2090.919), (1.3090056318022372, -89.56566668097003, -174.44686151189507), (1.8527429, 1.5716288, 1.7204182), "PWM_Nordic_4x4x4_A96_444", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2740.162, 10554.902, 725.0), (0.0, 28.25729395665223, -0.0), (0.50025123, 0.50025123, 0.50025123), "PWM_Nordic_4x4x4_A97_20", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (9275.5, 8178.038, 757.75977), (4.345033940911289, 35.79005487008597, 58.39843851316307), (0.53022367, 0.53022367, 0.53022367), "PWM_Nordic_4x4x4_A98_56", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5415.057, 3375.4272, 2055.949), (-9.078976989728217, -76.1234641527069, 101.69352583683064), (1.2622834, 1.1577024, 1.1577024), "PWM_Nordic_4x4x4_A99", _folder)
if a: placed += 1
else: skipped += 1

# Batch 63: StaticMesh'PWM_Nordic_4x4x4_A' (1 instances)
_mesh_path = "/Game/Unshippable/Whitebox/Rocks/Meshes/PWM_Nordic_4x4x4_A"
_materials = ['/Game/Unshippable/Whitebox/Rocks/Materials/PWM_Nordic_Blend_Tileable']
_folder = "Reconstruction/BD_BB_Chapter3_HeadwaterNexus/Meshes"
a = spawn_static_mesh(_mesh_path, _materials, (7300.193, 1765.14, 744.0893), (-0.44994812047492516, 72.312751093607, -99.86654925472293), (0.683877, 0.683877, 0.616848), "PWM_Nordic_4x4x4_A90", _folder)
if a: placed += 1
else: skipped += 1

# Batch 64: StaticMesh'PWM_Nordic_8x8x8_A' (580 instances)
_mesh_path = "/Game/Unshippable/Whitebox/Rocks/Meshes/PWM_Nordic_8x8x8_A"
_materials = ['/Game/Unshippable/Whitebox/Rocks/Materials/PWM_Nordic_Atlas_B']
_folder = "Reconstruction/BD_BB_Chapter3_HeadwaterNexus/Meshes"
a = spawn_static_mesh(_mesh_path, _materials, (11236.646, 6990.204, 1288.6576), (-3.777770423774943, -108.94333770815426, -2.347655905381296), (1.0, 1.0, 1.0020143), "PWM_Nordic_8x8x8_A_36", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (11271.109, 4910.636, 2271.7551), (-69.11960190798719, -174.48572560507577, -3.6783146623538028), (1.0, 1.0, 1.0), "PWM_Nordic_8x8x8_A10_524", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (7407.461, 4263.45, 1416.02), (5.117287105941515, 32.53830115791725, 176.17746603970176), (1.2054034, 1.012303, 1.29147), "PWM_Nordic_8x8x8_A100_160", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5890.346, 1489.9087, 1423.6604), (0.7459606479116484, -26.01318177570677, -0.7760009571651089), (0.549392, 0.643402, 0.368786), "PWM_Nordic_8x8x8_A1000", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (213.1783, 3758.4563, 1685.3116), (4.815002990185392, -86.24602389117562, 179.50555466802064), (0.961023, 0.634456, 1.052583), "PWM_Nordic_8x8x8_A1001_32", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (319.99768, 2997.4878, 2156.6228), (-2.7519219695366077, 2.67980929910426, 179.0844647011879), (0.883276, 1.318906, 0.70137995), "PWM_Nordic_8x8x8_A1002", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (661.97986, 2885.9236, 2031.1448), (-30.770047051502356, 52.67736328966384, -167.49721146484), (0.4138885, 0.5669729, 0.64524275), "PWM_Nordic_8x8x8_A1003", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (317.8371, 2979.04, 2026.0875), (32.81476132628629, -110.3301233194831, 176.49818105219617), (0.413889, 0.566973, 0.645243), "PWM_Nordic_8x8x8_A1004", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (455.77625, 11601.444, 2186.8486), (-63.65868964119381, -98.16117633459399, 90.12027888742296), (1.4561, 1.210743, 1.261981), "PWM_Nordic_8x8x8_A1005_41", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (439.32855, 7284.4297, 2011.3981), (4.253874534800107, 132.95382027435647, 179.1072303753286), (1.0, 1.0, 1.0), "PWM_Nordic_8x8x8_A1006", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (502.31467, 7199.453, 1242.9707), (8.765745921449204, -54.28795404483854, -0.23260485932835817), (1.0, 1.0, 1.3298497), "PWM_Nordic_8x8x8_A1007", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (319.55673, 7485.582, 2381.669), (-35.675604835510505, 163.0699198287368, -178.22916234672098), (1.0, 1.3065009, 1.0), "PWM_Nordic_8x8x8_A1008", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3889.2144, 6726.586, 1030.8041), (0.27886021773436764, 167.87235457432052, 3.6198049408027737), (0.846977, 1.0, 1.069156), "PWM_Nordic_8x8x8_A1009", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (722.9773, 7824.1455, 1948.3168), (-24.593262172466353, 141.87499470222934, -126.22063594514363), (1.5502877, 1.374626, 1.0621426), "PWM_Nordic_8x8x8_A101", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3887.8086, 6679.3755, 1761.563), (0.8122533414583001, 150.88815872470292, 178.05335059124022), (0.846977, 1.0, 1.2537125), "PWM_Nordic_8x8x8_A1010", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1988.6611, 6933.8604, 2198.4907), (0.6972871027880749, 1.6019287597738943, -171.10054079006838), (1.1729445, 1.1729445, 1.1729445), "PWM_Nordic_8x8x8_A1011", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (11729.015, 3913.8086, 1747.2811), (-16.540800526747283, -152.5165375189055, 92.6724621312295), (0.792394, 1.093091, 0.940449), "PWM_Nordic_8x8x8_A1012_106", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (11541.358, 989.995, 1268.5745), (-0.18847669510254486, -60.920344859799386, -6.889555680358018), (0.8111355, 0.5436543, 0.684103), "PWM_Nordic_8x8x8_A1013", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1662.5754, 6607.1855, 2211.6443), (6.203328840532863, -85.7638102760488, 179.57561877812194), (1.251712, 1.258034, 1.379101), "PWM_Nordic_8x8x8_A1016", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1781.923, 7703.5215, 2357.6802), (-5.764464670843186, 76.06362738470033, 175.0331777770069), (1.251712, 1.258034, 1.379101), "PWM_Nordic_8x8x8_A1017", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1643.7573, 7699.101, 1771.9542), (-20.702730762793337, 66.1868392052537, -175.60920509296102), (0.8973455, 0.787345, 0.8973455), "PWM_Nordic_8x8x8_A1018", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4803.333, 7143.3794, 1314.5151), (-0.3398132808373269, -9.899291345006482, 87.80910887368137), (0.95910305, 1.4445894, 0.9590347), "PWM_Nordic_8x8x8_A102", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2788.649, 6251.4497, 2434.168), (-52.54589604558678, 63.46713877712386, -170.75212383732517), (0.59999996, 1.53209, 1.53209), "PWM_Nordic_8x8x8_A1021", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (7252.3906, 10097.679, 2327.4739), (-51.04672822236232, 14.44546923683752, -87.56563200882137), (1.446266, 0.327371, 1.265721), "PWM_Nordic_8x8x8_A1022", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (6509.496, 3542.8938, 2564.0083), (13.724781167167414, 170.3317881799989, -17.758971884513134), (0.977762, 0.578004, 0.857171), "PWM_Nordic_8x8x8_A103_259", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (7377.619, 4013.0247, 1964.9358), (12.150830415137248, 89.46059708015673, 178.42445813891393), (1.2338659, 0.69689494, 1.29147), "PWM_Nordic_8x8x8_A104", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (7327.3564, 2678.83, 2476.3904), (-2.1285706952549623, 175.68130137382116, 178.96554690764833), (1.1648256, 0.91668564, 1.0442345), "PWM_Nordic_8x8x8_A106_229", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (7462.733, 3504.0247, 2191.6152), (0.6335305496472583, 89.377076969948, -177.24899988485552), (1.282656, 1.012303, 1.29147), "PWM_Nordic_8x8x8_A107_214", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (6939.7104, 1423.9353, 2995.9194), (3.4782196518730633, 45.94433818103586, -179.52743147493874), (1.1496075, 0.87925464, 1.1584216), "PWM_Nordic_8x8x8_A108_231", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (7441.6724, 3958.96, 1502.4121), (-4.290863073741932, -76.74646250805665, -178.70836319666898), (1.0236894, 0.7533364, 1.0325035), "PWM_Nordic_8x8x8_A109", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (7151.8022, 444.06314, 1134.7239), (-2.6537473178906037, 25.7552707121983, 0.26201843209349185), (1.0, 1.0, 1.0), "PWM_Nordic_8x8x8_A11_286", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5089.981, 4389.2534, 666.7336), (4.2968103584155015, -115.03986648760166, 2.4974058798876646), (0.93319654, 0.93319654, 0.6047287), "PWM_Nordic_8x8x8_A110", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5036.2373, 2100.9321, 869.11694), (0.0, 111.71099045190839, -0.0), (1.0, 1.0, 0.609134), "PWM_Nordic_8x8x8_A111", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (6807.939, 3579.483, 2606.6423), (-58.5719417639503, -139.4496904702979, -40.81406343292261), (1.303689, 0.863857, 1.143024), "PWM_Nordic_8x8x8_A112_251", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (6933.6304, 2828.8489, 2776.5505), (71.5954761040268, -11.704310671888514, -4.24142244259924), (1.263615, 0.863857, 1.143024), "PWM_Nordic_8x8x8_A113", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (6890.673, 2260.0112, 2655.8591), (-61.93905594829993, -118.84270991385279, -74.68261419051643), (1.263615, 0.863857, 1.143024), "PWM_Nordic_8x8x8_A114", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (6602.4688, 2759.687, 2633.275), (-74.84801109640013, 116.58335329384076, -128.95913000027585), (1.3418661, 0.863857, 1.143024), "PWM_Nordic_8x8x8_A115_302", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (6717.9775, 1424.1288, 2734.424), (-79.02518435639011, -151.10814809087046, -43.55368592280631), (0.94376, 0.863857, 1.143024), "PWM_Nordic_8x8x8_A116", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (8212.978, 7169.8955, 780.3528), (0.0, -39.74481030412636, 0.0), (0.574597, 0.574597, 0.574597), "PWM_Nordic_8x8x8_A117", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5457.1084, 1725.8975, 2051.1418), (1.6453512783419795, -21.717862983596977, -173.6121375469325), (0.798375, 0.528022, 0.91708165), "PWM_Nordic_8x8x8_A118_367", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5788.113, 2118.5156, 2633.632), (-14.452940184633567, 38.03973209044881, -164.91780108074371), (0.798375, 0.528022, 0.8448004), "PWM_Nordic_8x8x8_A119_375", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (7971.583, 2401.0405, 2495.7302), (-25.13098167564337, 164.275386758999, 177.62996020981475), (1.479404, 1.0, 0.705441), "PWM_Nordic_8x8x8_A12_439", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (8903.626, 6255.0835, 608.19147), (6.353222002119489, 30.89368525022251, 1.0237906331375077), (0.574597, 0.574597, 0.574597), "PWM_Nordic_8x8x8_A120", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (8195.939, 6942.105, 760.63367), (0.0, -13.366240504339112, 0.0), (0.574597, 0.574597, 0.574597), "PWM_Nordic_8x8x8_A121", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (8468.1, 5607.0654, 927.8718), (0.0, 78.70256776106822, -0.0), (0.574597, 0.574597, 0.574597), "PWM_Nordic_8x8x8_A122", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5292.8306, 1733.1956, 1275.7399), (1.6721805461327588, 166.0256761215735, -0.0167236285459272), (0.993406, 0.9934064, 0.6025405), "PWM_Nordic_8x8x8_A123", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (9026.124, 5690.9126, 734.70416), (4.2240891661164043e-08, 78.70247631283503, 2.1562224089561473), (0.574597, 0.574597, 0.574597), "PWM_Nordic_8x8x8_A124", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5800.81, 1605.1771, 2612.1484), (3.7760215158882766, -92.69280104442015, -177.8782784996472), (0.798375, 0.66925216, 0.917082), "PWM_Nordic_8x8x8_A125", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (6330.536, 1796.0913, 2770.833), (-70.26701165496986, 55.727326737986516, -85.77332592956354), (0.94376, 0.863857, 1.143024), "PWM_Nordic_8x8x8_A126_66", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (7289.4746, 720.61725, 2276.5466), (-9.394988295220276, 17.229855840736192, -166.20644261563376), (0.798375, 0.669252, 0.98549145), "PWM_Nordic_8x8x8_A127", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (7306.4517, 1404.3378, 2695.8684), (-19.056940722547896, 64.8580160626842, -178.58434427981192), (0.798375, 0.669252, 0.917082), "PWM_Nordic_8x8x8_A128", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (8185.325, 6653.435, 826.159), (0.0, -13.366240504339112, 0.0), (0.574597, 0.574597, 0.574597), "PWM_Nordic_8x8x8_A129", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (12029.524, 2972.8564, 2616.0332), (1.6522222828932147, -97.07792665038988, -89.94966329964379), (2.0797524, 1.0316846, 2.01819), "PWM_Nordic_8x8x8_A13", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (8737.505, 5673.785, 914.2519), (0.0, 106.63388223781617, -0.0), (0.574597, 0.574597, 0.46469694), "PWM_Nordic_8x8x8_A130", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (8248.886, 3845.5818, 2286.385), (-28.370839899160835, -95.02568251121518, -165.02782059393616), (1.0377471, 0.729622, 0.857171), "PWM_Nordic_8x8x8_A131_399", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (8748.838, 3974.1892, 2255.603), (-24.85629230148042, -73.22021979597113, -179.2078283750771), (0.977762, 0.729622, 0.857171), "PWM_Nordic_8x8x8_A132", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (7466.664, 3949.9407, 949.25745), (0.0, -56.12628199838195, 0.0), (1.0, 1.0, 0.939685), "PWM_Nordic_8x8x8_A133", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (7327.3564, 2091.9448, 2589.2542), (-1.7617188471443084, -2.212829620565034, -170.75717051700514), (1.164826, 0.916686, 1.044235), "PWM_Nordic_8x8x8_A134", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (7843.1553, 1551.8988, 2835.06), (-76.65313278167768, 7.940579731752879, -17.441495146897022), (1.263615, 0.863857, 1.143024), "PWM_Nordic_8x8x8_A135", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (7948.692, 2133.1401, 2819.7024), (-80.88647101122373, 46.74179124747378, -57.762452280886535), (1.263615, 0.863857, 1.143024), "PWM_Nordic_8x8x8_A136", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (8932.078, 3782.2014, 2328.9756), (-22.21457128307521, -99.4646582541892, -169.46100945775686), (0.977762, 0.729622, 0.857171), "PWM_Nordic_8x8x8_A137_431", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (9148.031, 4067.4343, 2168.6426), (0.21821088051262888, 153.7377986643569, 179.53351733260297), (1.1131794, 0.80375475, 0.857171), "PWM_Nordic_8x8x8_A138", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (9216.558, 4726.5347, 2160.961), (12.200809948621869, -144.23369407043467, -172.35046784221873), (0.977762, 0.729622, 0.857171), "PWM_Nordic_8x8x8_A139", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5627.637, 1651.111, 1740.8577), (-5.036255113258806, 78.00759325876169, -4.568023744051472), (0.64026785, 0.64026785, 0.64026785), "PWM_Nordic_8x8x8_A14_381", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (11264.888, 1373.7544, 904.1542), (0.0, -134.20282816981154, 0.0), (1.1320155, 1.0, 0.609134), "PWM_Nordic_8x8x8_A140_462", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (11451.932, 3775.2366, 2498.4016), (10.407295587816705, 105.94350570168366, 85.89129782837787), (1.218515, 0.989001, 1.218515), "PWM_Nordic_8x8x8_A141_478", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (11371.111, 1387.8259, 2419.9136), (14.148030658746848, 81.20615202169341, -169.07346648439085), (1.135899, 0.650977, 0.930144), "PWM_Nordic_8x8x8_A142", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (11260.757, 1968.7526, 2168.8743), (13.580693844545467, 65.12638156150568, -157.9674653277467), (0.977762, 0.578004, 0.857171), "PWM_Nordic_8x8x8_A143", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (7933.6074, 6571.4717, 1082.1658), (0.0, -13.366240504339112, 0.0), (0.574597, 0.6316538, 0.78477085), "PWM_Nordic_8x8x8_A144", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (11682.929, 2439.35, 966.89453), (7.703647605376149, 117.81194767405682, 3.7800085597928716e-06), (1.068589, 1.0, 0.9993682), "PWM_Nordic_8x8x8_A145", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (9583.984, 3978.0073, 851.8074), (6.774242572961074, 30.897703946503622, 0.42881933763904473), (1.0, 1.0, 0.469778), "PWM_Nordic_8x8x8_A146_315", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (11465.645, 1538.0278, 1205.9374), (3.617103833577069, -84.30364845266872, 1.8456856732439837), (1.0520883, 0.68679804, 0.6612223), "PWM_Nordic_8x8x8_A147", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (12372.329, 2310.0686, 1053.2142), (-3.254973481203151, -165.2085888302105, 2.385314527225537), (0.98999995, 0.93896127, 1.0388167), "PWM_Nordic_8x8x8_A148_323", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (9097.867, 5156.8584, 778.12866), (-7.277800091790915, 176.1682048632584, -3.6782829408987787), (1.0, 1.0, 0.579282), "PWM_Nordic_8x8x8_A149", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (8049.128, 4596.957, 1219.3422), (-5.367827847107475, -51.616692911786494, -1.949066312801626), (1.2721779, 1.2721779, 1.2721779), "PWM_Nordic_8x8x8_A15", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (10381.201, 4862.8354, 715.653), (0.0, -56.45568563332748, 0.0), (1.0, 1.0, 0.579282), "PWM_Nordic_8x8x8_A150", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (10381.719, 5002.9004, 807.4854), (-1.5785829228626282, 155.45013462755085, 2.9987129335536156), (0.7215252, 0.7215252, 0.54188347), "PWM_Nordic_8x8x8_A151", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4913.6323, 7422.1367, 647.2449), (-0.33981352842858925, -29.899294574635615, 132.8089310363958), (0.57534736, 0.54479134, 0.48267326), "PWM_Nordic_8x8x8_A152", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (10455.972, 5344.282, 724.7379), (0.0, -169.629994090657, 0.0), (1.0, 1.0, 0.579282), "PWM_Nordic_8x8x8_A153", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (6105.515, 314.82208, 1913.7587), (4.464778444859127, -91.59099796863545, 0.5918508022691091), (0.5, 0.5, 1.0), "PWM_Nordic_8x8x8_A154", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (10580.53, 5367.9233, 813.0214), (7.492785293156952, -22.229492079106983, -0.5592651784183494), (0.721525, 0.721525, 0.641858), "PWM_Nordic_8x8x8_A155_44", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (10543.817, 4820.1807, 938.0585), (7.884346159676856, -91.1520129643629, 5.582568205922463), (0.721525, 0.721525, 0.5430823), "PWM_Nordic_8x8x8_A156", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (10556.31, 5243.307, 973.377), (10.067355181131811, -70.30174280761427, -4.339201289957367), (0.5441278, 0.5441278, 0.36568478), "PWM_Nordic_8x8x8_A157", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (8886.357, 5160.682, 1216.0609), (2.4693520757516563, 88.64103358401502, -0.5849608358089816), (1.0101179, 0.9701063, 0.9701063), "PWM_Nordic_8x8x8_A158_496", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (9215.052, 4354.798, 890.7863), (0.0, 45.07015359980807, -0.0), (0.71658427, 1.1196609, 0.64150923), "PWM_Nordic_8x8x8_A159", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (8588.309, 2594.2927, 2581.3838), (-72.89863026749835, 20.004453871990215, -107.60354413624846), (1.0460839, 1.0766999, 1.0), "PWM_Nordic_8x8x8_A16_441", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (7687.817, 3413.8645, 606.2308), (14.082971722414031, -110.42089874269385, 1.850173944072025e-06), (0.716584, 0.81594473, 0.641509), "PWM_Nordic_8x8x8_A160_286", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (9070.727, 5103.994, 1938.4655), (9.186548657224149, -72.94616221071864, 178.3387026038881), (0.977762, 0.80171764, 0.857171), "PWM_Nordic_8x8x8_A161", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (9436.313, 5047.6113, 2259.1172), (9.18654975168989, -87.06778492964182, 178.33870353789771), (0.977762, 0.729622, 0.857171), "PWM_Nordic_8x8x8_A162", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (11367.705, 5330.8135, 2353.6064), (0.8138382418660554, 15.76568432670691, 178.66110901422948), (0.9144026, 0.66626275, 0.7938118), "PWM_Nordic_8x8x8_A163", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (10600.29, 8035.402, 616.355), (5.3311759594119845, -136.0673865404725, 172.31801813520545), (1.0, 1.0, 0.579282), "PWM_Nordic_8x8x8_A164", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (6236.6836, 1991.9205, 2639.8318), (-1.7617188471443084, -2.212829620565034, -170.75717051700514), (0.9532674, 0.70512736, 0.8326763), "PWM_Nordic_8x8x8_A165", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (8375.849, 4391.017, 687.07306), (-2.091552484790419, 103.82090816939785, 0.38344391901141833), (1.0, 1.0, 0.599168), "PWM_Nordic_8x8x8_A166", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (7863.2065, 7351.248, 856.6426), (0.0, 42.821885498041986, -0.0), (1.0, 1.0, 0.579282), "PWM_Nordic_8x8x8_A167", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (8713.289, 4855.3325, 953.5447), (-3.3111875757840417, -3.323211468215619, 5.905390884942591), (1.0, 1.0, 1.0), "PWM_Nordic_8x8x8_A168", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (10477.256, 5093.778, 966.0803), (2.3893872651139034, 30.712286131859827, 10.693969231824125), (0.544128, 0.544128, 0.365685), "PWM_Nordic_8x8x8_A169", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (8122.11, 4398.048, 1847.938), (-28.441309147684777, -70.6539870857979, -176.78333365013253), (1.272178, 1.272178, 1.272178), "PWM_Nordic_8x8x8_A17", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (7341.1416, 7690.411, 1440.8284), (-9.536650044738268, 0.8026254490107338, 4.359960574789681), (1.272178, 1.2193931, 1.272178), "PWM_Nordic_8x8x8_A170", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (7594.17, 7823.234, 1969.5422), (-32.64898628874589, -8.365539240649293, -170.8013069327694), (1.272178, 1.1387204, 1.272178), "PWM_Nordic_8x8x8_A171", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (7404.5684, 7463.198, 1327.4492), (-4.568573486591709, 118.66544661551626, -12.390717251983027), (0.977762, 0.729622, 0.857171), "PWM_Nordic_8x8x8_A172", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (8845.15, 5283.318, 1242.3452), (-0.6458435629403073, 161.04199784548774, -4.8352974785529605), (0.970106, 0.48007455, 0.970106), "PWM_Nordic_8x8x8_A173_59", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4501.5073, 7479.582, 615.70386), (14.853514966884394, -161.02987620181594, -4.886077996353777), (1.2913862, 1.2238239, 0.609134), "PWM_Nordic_8x8x8_A174", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (10823.762, 6450.9893, 562.6331), (-0.9802245259773111, 175.92304640935586, 5.584902004987591), (0.87419015, 1.0, 0.95228064), "PWM_Nordic_8x8x8_A175_30", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (904.77704, 4008.6663, 1573.0162), (-2.5535890005674458, -55.64135213551316, -4.343017629249005), (0.73901, 0.73901, 0.73901), "PWM_Nordic_8x8x8_A176", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1386.905, 4156.6484, 1550.9813), (-2.553589028390942, -93.36145462008174, -4.34301744789669), (0.73901, 0.73901, 0.73901), "PWM_Nordic_8x8x8_A177", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4563.8467, 7331.3857, 939.83136), (10.136759758944454, 40.429058129800616, 1.0273202785880025), (1.0, 1.0, 0.609134), "PWM_Nordic_8x8x8_A178", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1622.0201, 3997.4521, 2133.9316), (-16.461423387035182, -130.2070821789333, 179.38336089078373), (0.73901, 0.73901, 0.73901), "PWM_Nordic_8x8x8_A179", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5286.3994, 7232.268, 2194.2986), (-53.128959716977604, -70.32740718489168, 145.77610086314758), (1.0991654, 1.0, 0.83902997), "PWM_Nordic_8x8x8_A18_63", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4334.9106, 8106.1777, 2424.5532), (0.624019566492354, -6.499937798331549, -172.42401613780487), (0.977762, 0.729622, 0.857171), "PWM_Nordic_8x8x8_A180", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4374.4526, 7170.22, 1363.6532), (-10.439054320045253, 37.829031054530326, 88.53869004927591), (1.4561, 1.2139026, 1.1821092), "PWM_Nordic_8x8x8_A181", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4864.5063, 4629.3936, 902.73413), (0.0, 166.81619478855237, -0.0), (1.0, 1.0, 0.609134), "PWM_Nordic_8x8x8_A182_174", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (988.5652, 3950.724, 1958.5708), (-16.46120987488845, -56.44252854785975, 179.38336130311063), (0.73901, 0.84812087, 0.73901), "PWM_Nordic_8x8x8_A183", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4749.705, 7376.163, 2414.084), (1.9861506080853852, 28.3986336414323, -174.61103719152626), (1.16297, 1.012303, 1.29147), "PWM_Nordic_8x8x8_A184", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4281.618, 11720.645, 963.2314), (0.706024395928916, 19.779604887387926, -2.050720258457072), (1.0, 1.0, 0.7900682), "PWM_Nordic_8x8x8_A185", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5491.8794, 11091.739, 1075.3824), (0.5383965752350195, 63.01842776129926, -1.9653623719134516), (1.0, 0.616778, 0.41718036), "PWM_Nordic_8x8x8_A186", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4662.9487, 8176.4297, 2371.2556), (6.079030942878304, -85.09352983793887, -176.2394754744811), (0.977762, 0.578004, 0.857171), "PWM_Nordic_8x8x8_A187", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (11113.119, 7747.9214, 1047.3792), (-2.0690304147665555, 174.7415855842583, -3.41787688378442), (1.0, 1.0, 1.1155684), "PWM_Nordic_8x8x8_A188_108", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (8046.455, 7823.3105, 2296.6118), (-42.2684632379246, -21.71441755654439, -156.78388407466673), (1.263615, 1.0312736, 1.143024), "PWM_Nordic_8x8x8_A189", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4958.4824, 4278.4004, 2065.2974), (21.362802086476897, -12.61303719557156, -107.32106275376266), (1.536351, 0.453766, 0.857171), "PWM_Nordic_8x8x8_A19", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (10933.578, 7731.3687, 1914.7764), (-10.395386147556565, 172.8162829819875, -178.91015882757108), (1.0, 1.0, 1.0), "PWM_Nordic_8x8x8_A190_110", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (8501.019, 5811.646, 654.5101), (4.484378670495587, 51.0711466330169, 3.688732104985064), (0.87419, 1.0, 0.952281), "PWM_Nordic_8x8x8_A191", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (8077.2637, 6643.4785, 2537.182), (-28.58615005075763, 8.753845100433777, -166.52261621779144), (1.2380947, 1.2380947, 1.2380947), "PWM_Nordic_8x8x8_A192", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (8678.421, 5863.014, 2715.5273), (28.197204089580282, -124.06477526482216, -174.1864310091503), (1.238095, 1.238095, 1.238095), "PWM_Nordic_8x8x8_A193", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (10801.794, 7893.7246, 2270.1453), (-6.460022681175112, 100.42426151130164, 174.5032044475899), (1.272178, 1.24611, 1.272178), "PWM_Nordic_8x8x8_A194", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (7867.256, 8874.876, 2532.0996), (60.919781517933764, -31.018862101394717, 151.04612911751823), (1.272178, 0.7699511, 0.81065047), "PWM_Nordic_8x8x8_A196", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (9720.5625, 9157.7, 2356.231), (-82.53868246378045, 105.25773360909767, 89.46810920729312), (0.87123483, 1.4689219, 1.7038784), "PWM_Nordic_8x8x8_A197", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (10321.46, 8693.371, 2552.9343), (-8.321504149769005, 161.43278498134845, 175.67633208117954), (1.272178, 1.13872, 1.605341), "PWM_Nordic_8x8x8_A198", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (9985.507, 8243.176, 2303.9333), (-83.94387639095146, 99.44940121822587, 90.21642898867347), (0.9477458, 1.2364838, 1.619566), "PWM_Nordic_8x8x8_A199_58", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (9099.999, 5500.0, 943.3349), (0.0, 103.66235926952481, -0.0), (0.6430888, 0.5745975, 0.5745975), "PWM_Nordic_8x8x8_A2_81", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (10062.563, 4991.6255, 2474.1917), (72.56310656943724, -146.7634538990318, -143.94501766040037), (0.81567246, 1.0, 1.0), "PWM_Nordic_8x8x8_A20_526", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (8585.739, 7972.2603, 2575.158), (-87.12523011491534, -157.55735791521357, 172.17800042717846), (1.272178, 1.13872, 1.605341), "PWM_Nordic_8x8x8_A200", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (9168.988, 8036.502, 2681.6938), (0.17629814517165268, 99.55319069074883, 172.545077058147), (1.272178, 1.13872, 1.272178), "PWM_Nordic_8x8x8_A201", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (10162.181, 7317.7725, 2458.0422), (-34.759522836978014, -77.2486527076242, -85.14358830068498), (0.96999997, 0.84749997, 1.605341), "PWM_Nordic_8x8x8_A202", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (10405.095, 8185.901, 2280.1204), (0.0, 0.0, -177.16576273480482), (1.0, 1.0, 1.0), "PWM_Nordic_8x8x8_A203_22", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (9425.77, 7295.812, 2437.836), (-13.011107955292765, -57.87972057225832, 179.4854860909286), (1.272178, 1.13872, 0.63023806), "PWM_Nordic_8x8x8_A204", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (10811.9, 6402.637, 2831.229), (-83.11916201358531, -96.60210315406599, -67.44680314625747), (1.272178, 1.1959403, 1.7153989), "PWM_Nordic_8x8x8_A205", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (10441.206, 7167.5386, 2705.2969), (12.56514058690944, 104.37303278298471, 176.5558984081062), (1.272178, 1.13872, 0.630238), "PWM_Nordic_8x8x8_A206", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (9778.981, 6816.237, 2706.0417), (-11.379606199249016, -89.67332514691621, -173.62763758679412), (1.272178, 1.13872, 0.630238), "PWM_Nordic_8x8x8_A207", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (10987.639, 5329.633, 2742.2512), (-39.91555027732841, -84.5670056038253, -94.64897856669187), (1.0013018, 1.060561, 1.605341), "PWM_Nordic_8x8x8_A208", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (10816.413, 6129.3784, 822.74255), (4.73330707697316, 169.34925946131742, -2.549316409878839), (1.0, 1.3282202, 0.7037547), "PWM_Nordic_8x8x8_A209_116", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (10695.2, 5038.517, 2510.8464), (80.92794616334699, -68.8168995655042, -155.936746172429), (0.815672, 1.0, 1.0), "PWM_Nordic_8x8x8_A21_528", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (10343.567, 7943.358, 620.89294), (1.9417474809561188, -125.46665836668357, -175.85925874647637), (0.6761025, 1.0, 0.630327), "PWM_Nordic_8x8x8_A210_144", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (11046.601, 6782.107, 928.4798), (0.0, -155.80429193293784, 0.0), (1.0, 1.0, 1.0), "PWM_Nordic_8x8x8_A211", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (11391.923, 5527.208, 1044.6667), (1.3278831449402755e-09, 177.8804504829962, -5.467619953205545), (1.0, 1.0, 1.0), "PWM_Nordic_8x8x8_A212", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (11211.229, 5570.4863, 946.4347), (0.0, -175.87341483437487, 0.0), (1.0, 1.0, 0.80999756), "PWM_Nordic_8x8x8_A213", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (11096.352, 6285.569, 871.0035), (0.0, -173.0013377725824, 0.0), (1.0, 1.0, 0.809998), "PWM_Nordic_8x8x8_A214", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (11065.391, 6966.3027, 927.9274), (0.0, -85.8309975908653, 0.0), (1.0, 1.0, 1.0), "PWM_Nordic_8x8x8_A215", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (11581.225, 5294.518, 2178.0247), (21.122712221085273, 16.0032975025112, 176.9454375188782), (0.9123078, 0.9123078, 0.9123078), "PWM_Nordic_8x8x8_A216", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (10823.839, 7309.131, 713.59515), (-10.497070257229867, 166.23254656809334, -0.06329343789657753), (1.0, 1.0, 0.67800885), "PWM_Nordic_8x8x8_A217", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (10634.97, 7297.8916, 531.3776), (0.0, -109.53374935154368, 0.0), (1.0, 1.0, 1.0), "PWM_Nordic_8x8x8_A218", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (10517.999, 7518.4717, 596.9389), (0.75261165254431, -150.50768411162505, 178.997616014861), (1.020206, 1.020206, 0.599488), "PWM_Nordic_8x8x8_A219", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (7429.607, 8723.629, 781.75696), (4.600890150394874, 80.5001493539517, -0.7689816907470154), (1.0, 1.0, 0.558635), "PWM_Nordic_8x8x8_A220", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (8216.097, 6389.1074, 566.9678), (5.9153364834705595, 21.78047567931024, -3.263549866016942), (0.87419, 1.0, 0.952281), "PWM_Nordic_8x8x8_A221", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (10233.32, 10702.184, 1312.2683), (2.1019899174678653, 179.0421232205004, 96.29483020005226), (1.4561, 1.374626, 1.041244), "PWM_Nordic_8x8x8_A222_62", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (7426.657, 8526.325, 2151.803), (-9.534025322064233, 93.25019805406441, -178.6370581384788), (0.97012997, 0.97012997, 0.97012997), "PWM_Nordic_8x8x8_A223", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (7618.534, 8336.493, 978.31506), (0.12516320279759763, -9.415343223646815, -0.8038329621908493), (0.89315224, 0.91244715, 0.6523951), "PWM_Nordic_8x8x8_A224", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (6420.237, 7587.6577, 1086.647), (-2.2583618708124455, -167.9447181806557, -3.7721859539788793), (1.3230824, 1.219393, 1.272178), "PWM_Nordic_8x8x8_A225_108", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (7373.9966, 8878.602, 2701.9585), (69.40731838123797, -45.327702075174834, 138.0135134879299), (1.272178, 0.9878149, 1.0001032), "PWM_Nordic_8x8x8_A226", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (8544.718, 5970.557, 553.22205), (6.751757853429086, 51.84700830688943, 0.1304511171009539), (0.87419, 1.0, 0.952281), "PWM_Nordic_8x8x8_A227", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (11070.825, 8126.674, 899.662), (0.0, -88.70965713110348, 0.0), (1.1074332, 1.0, 0.579282), "PWM_Nordic_8x8x8_A229", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (9851.1045, 4252.965, 2487.7412), (2.8212627074485366, -90.50107088511878, 86.03319775768513), (1.2185153, 0.98900115, 1.2185153), "PWM_Nordic_8x8x8_A23", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (11487.675, 8413.11, 1229.142), (2.183561276493945, 87.51835700522923, 91.14974299700042), (1.5399597, 1.374626, 1.1999124), "PWM_Nordic_8x8x8_A230_13", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (11318.968, 10272.81, 799.44574), (0.0, -58.11092828572202, 0.0), (1.107433, 1.0, 0.5558788), "PWM_Nordic_8x8x8_A231_51", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (10201.194, 10622.483, 827.3967), (-1.3472594133402211, 58.71994563911516, 0.24278209473927434), (1.107433, 1.0, 0.555879), "PWM_Nordic_8x8x8_A233", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (10524.811, 9870.299, 663.92413), (0.0, -140.88979066964322, 0.0), (1.107433, 1.0, 0.555879), "PWM_Nordic_8x8x8_A234", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (6171.719, 8116.35, 573.2414), (4.439499797195651, -149.76536384040796, 7.764947803386763), (1.0098428, 1.0, 0.93135345), "PWM_Nordic_8x8x8_A235_101", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (7996.466, 10648.944, 1516.0353), (-4.36850040240289, -149.0214082239129, 94.70000193478424), (1.5067062, 1.3608669, 1.0907589), "PWM_Nordic_8x8x8_A236", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (7921.076, 10020.728, 2134.726), (-15.930720870669152, -82.04021740567607, 92.58849859979121), (1.1141559, 1.219545, 1.1297672), "PWM_Nordic_8x8x8_A237_73", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (11563.008, 10252.857, 2262.4487), (-0.0529479978636861, -69.10502824512272, 179.74903118762484), (1.0, 1.0, 1.0), "PWM_Nordic_8x8x8_A238", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (11507.631, 10439.344, 1125.7842), (0.0, -70.14703555209172, 0.0), (1.0, 1.0, 1.0), "PWM_Nordic_8x8x8_A239", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (7899.4775, 1500.7489, 2657.7107), (-80.90472535508741, 66.46040306457265, -68.96482108194921), (1.1810248, 1.0, 1.2829868), "PWM_Nordic_8x8x8_A24", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (11344.638, 10536.681, 1691.1074), (0.1801940073130329, -179.78119472544958, -170.76970209507905), (1.0, 1.0, 1.3270224), "PWM_Nordic_8x8x8_A240", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (10350.428, 10453.492, 1977.3817), (-45.590667579527874, -104.53354350527108, 100.29180182432847), (1.4561, 1.0608231, 1.041244), "PWM_Nordic_8x8x8_A241_64", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (8681.936, 10707.556, 2461.149), (-73.21847785367268, -57.73331291281784, 152.76405908657952), (1.1327966, 1.0756179, 1.1207556), "PWM_Nordic_8x8x8_A242", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (9478.722, 10707.556, 2422.2742), (-56.77119846178139, -128.7720316431764, -136.6200400511357), (1.1372247, 1.075618, 1.075618), "PWM_Nordic_8x8x8_A243_573", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (11332.549, 8653.553, 2055.7456), (19.5333217735813, -79.06273000413205, 179.3559572587413), (1.0265511, 1.0, 1.301078), "PWM_Nordic_8x8x8_A244", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (10892.642, 8753.764, 642.3948), (5.931855218581671, 116.43577344458194, -1.6069949339121794), (1.107433, 1.0, 0.555879), "PWM_Nordic_8x8x8_A245", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (11645.292, 8172.8467, 1483.3533), (15.035493606925057, -84.38099060426873, 179.3767838287137), (1.0, 1.1608044, 1.3869418), "PWM_Nordic_8x8x8_A246", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (11194.446, 9723.143, 2429.7253), (4.775542994365588, -1.917724614561643, 16.04060754934016), (1.4561, 1.1029209, 1.0), "PWM_Nordic_8x8x8_A247_48", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (10608.613, 8327.762, 628.4211), (-2.5190432707570976, -114.25568193949204, 5.606675291023164), (1.107433, 1.0, 0.555879), "PWM_Nordic_8x8x8_A248", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (7901.194, 10061.5205, 1279.0308), (-9.192201861618464, -84.92277020853638, 95.4852334962487), (1.4994996, 1.1556752, 1.0784853), "PWM_Nordic_8x8x8_A249_60", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5713.3105, 4415.207, 2454.8074), (-7.012908436331373, -81.16174083581268, -179.9180374612818), (1.0214674, 1.0, 1.0214674), "PWM_Nordic_8x8x8_A25", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4408.269, 11324.4375, 955.1426), (14.51504510519662, -137.23699155027475, 0.9420267407014621), (1.0, 1.0, 1.0), "PWM_Nordic_8x8x8_A250_70", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3843.296, 11079.396, 572.1276), (3.526474076613525, -125.7996733310564, 176.72801724086534), (1.0, 1.0, 0.579282), "PWM_Nordic_8x8x8_A251", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (6702.655, 8022.233, 2215.4443), (-46.43315795607737, 121.29445857593998, 94.28975888503965), (1.5125726, 1.374626, 1.2619815), "PWM_Nordic_8x8x8_A252", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (6920.933, 9049.92, 2722.0044), (7.741056842712433, 141.70725357923308, -171.1548443755136), (1.629881, 1.548407, 1.173781), "PWM_Nordic_8x8x8_A253", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (7048.79, 9908.682, 2833.5398), (0.49688716060781746, 140.90763274375934, -177.1089248336349), (1.629881, 1.548407, 0.91526496), "PWM_Nordic_8x8x8_A254", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4648.7925, 5968.637, 1313.9431), (-3.3094196795146025, -86.68483993230994, 82.03059922383571), (1.4561, 1.374626, 1.019033), "PWM_Nordic_8x8x8_A255_160", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (6474.545, 9494.595, 2864.075), (-0.5307615992611094, -174.65631428278664, -168.34245133205647), (1.629881, 1.548407, 1.173781), "PWM_Nordic_8x8x8_A256", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (6550.229, 7745.9023, 1557.0239), (-14.545073591980595, 101.24784750343052, 95.07967659448856), (1.097516, 1.0, 1.1454954), "PWM_Nordic_8x8x8_A257", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (6642.7446, 8493.142, 815.3402), (13.067857895053711, 107.80690164190385, -1.8795170257833025), (1.0, 1.0, 0.6473234), "PWM_Nordic_8x8x8_A258_119", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (6040.8774, 8398.915, 2499.6768), (74.83380530118298, -80.68472775645986, -8.44818201905199), (0.91451216, 1.3784636, 1.3116617), "PWM_Nordic_8x8x8_A259", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (6444.9297, 4878.1855, 975.13995), (-7.964844590944962, -89.82367319952722, 0.8157642519608423), (1.0, 1.0, 0.9453193), "PWM_Nordic_8x8x8_A26", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5300.9316, 7808.752, 2364.1387), (-88.88693463238661, 163.03184004091707, -65.41565889453454), (1.4316015, 1.3501275, 1.3318068), "PWM_Nordic_8x8x8_A260", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5991.46, 9446.775, 2777.1367), (10.951660922413035, 27.817322981085454, -7.913207953433645), (1.629881, 1.548407, 1.033484), "PWM_Nordic_8x8x8_A261", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5297.587, 5836.6333, 2510.1853), (-53.016261279673024, -18.682795779746513, 91.16544051377446), (1.20896, 1.409608, 1.20896), "PWM_Nordic_8x8x8_A262", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (8416.348, 9881.304, 650.67163), (0.0, -4.415222210990794, 0.0), (1.107433, 1.0, 0.555879), "PWM_Nordic_8x8x8_A263", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (6657.6943, 5308.7314, 936.999), (-3.996826515999981, 118.33453669401386, 1.181831723802578), (1.272178, 1.219393, 0.9764897), "PWM_Nordic_8x8x8_A264", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (10891.173, 10573.898, 1275.1028), (-5.735105628403536, -102.86962598161352, 93.34229096199051), (1.4561, 1.374626, 1.041244), "PWM_Nordic_8x8x8_A265_180", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (6891.479, 6690.45, 1525.9244), (-8.028626455909972, -143.32174164546458, -4.489868506230492), (1.2950233, 1.2720892, 1.2720892), "PWM_Nordic_8x8x8_A266", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (6985.034, 5893.203, 1647.8129), (-12.961304398857857, 162.70575724431325, -1.4473571387489284), (1.272178, 1.345365, 1.272178), "PWM_Nordic_8x8x8_A267", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (6090.44, 6630.646, 2488.3516), (-63.101005774165024, -147.74252384562743, 155.82000330312843), (1.402394, 1.0936056, 1.2875179), "PWM_Nordic_8x8x8_A268", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5197.512, 5074.124, 2250.0732), (-51.07036289927383, 19.93609364871002, 79.7362265921653), (1.3351623, 1.409608, 1.20896), "PWM_Nordic_8x8x8_A269_65", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (7920.242, 612.18695, 2359.9937), (-69.71027996749692, 32.65158417243887, 65.93565616119771), (1.0, 1.4356292, 1.282987), "PWM_Nordic_8x8x8_A27", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1663.4646, 11867.608, 1196.3058), (-1.4376218570549488, -150.10586162208557, 96.47815767510028), (1.4561, 1.374626, 1.041244), "PWM_Nordic_8x8x8_A270", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2462.7947, 12024.339, 1364.4655), (-6.493741817318792, -84.4664022076378, 91.36505301456172), (1.0785528, 1.1468859, 0.7248278), "PWM_Nordic_8x8x8_A271", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2120.4194, 11381.18, 2144.3289), (-60.253189283194764, -82.34821961073648, 87.78498920127372), (1.5915183, 1.4658039, 1.2929869), "PWM_Nordic_8x8x8_A272", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1696.0452, 8108.073, 2339.7217), (-67.41201598262323, 80.60066842426752, 96.44075762965367), (1.6638184, 1.4272413, 1.3778232), "PWM_Nordic_8x8x8_A273", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1008.78156, 11916.16, 1259.6792), (-1.9326782460945704, -116.18506063869626, 0.983459631731108), (1.0, 1.4326017, 1.2580966), "PWM_Nordic_8x8x8_A274", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (792.7609, 11440.956, 2191.709), (-71.42558276593424, -130.07315898062237, 129.16530846033274), (1.0999519, 1.374626, 1.5164839), "PWM_Nordic_8x8x8_A275", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1376.5239, 11243.368, 2089.9197), (9.954099339365793, 175.76342161042407, 155.45315377383037), (1.4668832, 1.374626, 0.7040262), "PWM_Nordic_8x8x8_A276", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (767.1165, 10301.077, 2311.781), (-9.453095304101339, 3.181518658786949, -0.05627443449228833), (1.8924391, 1.5286368, 0.75474346), "PWM_Nordic_8x8x8_A277", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1447.7618, 11380.484, 859.2245), (0.0, -119.5125812972463, 0.0), (1.0, 1.0, 0.609134), "PWM_Nordic_8x8x8_A278", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1836.2201, 11203.607, 907.43695), (0.0, -114.48048253879108, 0.0), (1.0, 1.0, 0.42878342), "PWM_Nordic_8x8x8_A279", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4958.731, 4364.3164, 1319.1477), (-7.634916303747267, 2.2931490123640303, -7.530456472872465), (0.9468198, 0.9468198, 0.9468198), "PWM_Nordic_8x8x8_A28_40", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (727.05695, 8993.288, 2400.5632), (-1.2889403910558128, -4.544220230033073, -2.5814209427911012), (1.7422615, 1.374626, 0.704026), "PWM_Nordic_8x8x8_A280", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1313.0109, 10415.531, 2277.1177), (2.930541478794623, -179.5877014640467, 173.12559995000476), (1.466883, 1.374626, 0.704026), "PWM_Nordic_8x8x8_A281", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (678.4073, 11833.588, 1998.8309), (-51.06236745042281, -96.17094496475903, 94.03783024540257), (1.4561, 1.2107433, 1.261981), "PWM_Nordic_8x8x8_A282", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (405.6888, 11893.088, 768.04724), (41.97387764587856, -100.33759266385921, 84.14423071822488), (0.91769665, 0.7859816, 0.9500327), "PWM_Nordic_8x8x8_A283_206", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1994.3567, 11673.39, 1081.9921), (22.928038341199173, -80.50707619708115, 92.70230147154554), (0.917697, 0.9665614, 0.950033), "PWM_Nordic_8x8x8_A284", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (10761.788, 8537.142, 2515.8372), (-8.321504149769005, 161.43278498134845, 175.67633208117954), (1.272178, 1.13872, 1.605341), "PWM_Nordic_8x8x8_A285", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1636.8508, 7168.3467, 1120.537), (9.100427213589903, -91.73897953318996, 7.273364618541606), (1.3396723, 1.2580343, 1.3791006), "PWM_Nordic_8x8x8_A286", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4048.1865, 12132.026, 1048.7812), (-1.1417540196953089, -75.67296680188558, 1.8438719170903441), (1.0, 1.0, 1.0), "PWM_Nordic_8x8x8_A287_228", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2365.2153, 8407.838, 2589.2795), (57.36083594160459, -160.2246887143208, 32.16839294861005), (0.965, 1.4341836, 1.419369), "PWM_Nordic_8x8x8_A288_233", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2817.4868, 11597.564, 2321.2258), (-48.8150297317565, 8.468292221041292, -96.61998306664549), (0.96999997, 0.9, 1.261981), "PWM_Nordic_8x8x8_A289_236", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (6062.054, 5276.676, 3021.1694), (0.0, 0.0, -0.0), (1.0, 1.0, 1.0), "PWM_Nordic_8x8x8_A29_68", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3764.61, 12402.711, 1722.4004), (-20.110593077418464, -167.95629578808305, 89.21426460189586), (0.9108949, 1.2542772, 1.0997884), "PWM_Nordic_8x8x8_A290", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4349.8877, 11770.58, 2535.889), (-3.3144828358025884, -84.62602726287463, 179.06249791947897), (0.798375, 0.528022, 0.8448), "PWM_Nordic_8x8x8_A291", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2815.8257, 9568.757, 2569.793), (-85.19074788171018, 49.12430704175805, -39.441357196271376), (0.71, 1.374626, 1.419369), "PWM_Nordic_8x8x8_A292", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3440.9668, 11189.567, 2567.4402), (-72.98751816952571, 19.356774836708265, -108.79549672960657), (0.9236913, 1.374626, 1.261981), "PWM_Nordic_8x8x8_A293_450", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5217.1426, 10717.875, 2738.9863), (-84.71116005367384, -142.5378489707272, 34.774587987236856), (1.5513833, 1.374626, 1.261981), "PWM_Nordic_8x8x8_A294_452", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (9801.308, 8037.3823, 505.06653), (-2.519012615706235, -114.25568042772575, -1.9094543369439272), (1.107433, 1.0, 0.555879), "PWM_Nordic_8x8x8_A295_33", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4460.895, 11195.868, 2698.2297), (-75.489828736442, -109.28343019877903, 81.55381048522206), (1.0703255, 1.374626, 1.3157941), "PWM_Nordic_8x8x8_A296_268", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4871.188, 8973.514, 2432.158), (-65.74837598835195, 77.0774904211125, -72.79918088687243), (0.5578336, 1.7097085, 1.419369), "PWM_Nordic_8x8x8_A297_252", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1366.815, 7999.3354, 756.6629), (0.0, -171.45645401912452, 0.0), (1.0779897, 1.0, 0.5130153), "PWM_Nordic_8x8x8_A298", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1151.3064, 8135.4053, 593.768), (0.0, 176.87263538901107, -0.0), (1.0, 1.1159494, 0.609134), "PWM_Nordic_8x8x8_A299", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4530.869, 3785.6704, 1334.1206), (-5.340545083029735, -30.311978646792895, -0.7562561203444184), (1.0, 1.0, 1.0), "PWM_Nordic_8x8x8_A3_536", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2106.766, 3613.8323, 1239.1503), (-5.086029191189253, -107.53906864897284, 0.06974211458405041), (0.73901016, 0.73901016, 0.73901016), "PWM_Nordic_8x8x8_A30_110", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1367.2473, 8595.755, 522.78394), (2.3760518801169965, -21.645938109405957, 178.8166624204842), (1.0, 1.0, 0.609134), "PWM_Nordic_8x8x8_A300_257", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3203.0503, 12335.111, 2400.7754), (-83.07914659316802, -5.985587257116439, -82.81944840807185), (1.4819738, 1.1980903, 1.2203416), "PWM_Nordic_8x8x8_A301", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3952.1777, 11965.607, 2200.514), (2.189328487284496, 172.58944216045236, -166.8058541480771), (0.9570707, 0.669252, 1.016141), "PWM_Nordic_8x8x8_A302", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (6053.3096, 10854.391, 1118.0026), (0.0, -79.555416495517, 0.0), (1.0, 1.0, 1.0), "PWM_Nordic_8x8x8_A303_270", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (7255.464, 10346.652, 953.7149), (-0.8392641382609947, 68.77019383241692, -3.687652359609634), (1.0, 1.173469, 0.6029164), "PWM_Nordic_8x8x8_A304", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (6464.549, 10691.305, 979.1987), (-1.2982482949135354, 68.05197044249559, 1.3062518489105837), (1.0, 1.173469, 0.575139), "PWM_Nordic_8x8x8_A305", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (9234.676, 491.9607, 2686.1199), (-2.7846982088599574, -88.98775798235549, -5.931090989705226), (1.4978235, 1.510502, 1.0170193), "PWM_Nordic_8x8x8_A306", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (6398.424, 7819.101, 1804.5906), (11.634021472862383, -1.8435542352873264, -179.51879868667754), (0.7994062, 0.7994062, 0.7994062), "PWM_Nordic_8x8x8_A307", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4132.444, 11165.954, 859.8102), (2.904946453655461, -154.44544370784033, 1.3881803218408295), (1.0, 1.0, 0.60190177), "PWM_Nordic_8x8x8_A308_46", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (7445.267, 979.6408, 645.9058), (3.7089283693003536, 55.20678566489678, -4.325957430541336), (1.1710104, 1.0237848, 0.52043766), "PWM_Nordic_8x8x8_A309", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (11598.83, 4986.171, 1169.7983), (-1.374084095487278, -5.446471493461153, 179.78089416921748), (1.045567, 1.0, 0.96115214), "PWM_Nordic_8x8x8_A31_120", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (10405.023, 694.1275, 2640.7297), (0.25014918108379947, -88.18646178222033, -165.2050782546009), (1.447527, 1.510502, 0.953836), "PWM_Nordic_8x8x8_A310", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (10419.949, 270.30637, 2648.3071), (-5.78118917613273, -89.78457128257207, -165.1275687734459), (1.447527, 1.510502, 0.953836), "PWM_Nordic_8x8x8_A311", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (10212.716, 2029.0343, 2750.4727), (79.2381932071453, 7.378028431231824, -84.09987477250097), (0.82231945, 1.510502, 1.499538), "PWM_Nordic_8x8x8_A312", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (10636.459, 3715.997, 2481.2253), (76.67775816450221, -35.66245381258303, -126.28682116570805), (0.944548, 1.510502, 1.499538), "PWM_Nordic_8x8x8_A313_296", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (9559.461, 2662.9111, 2778.802), (8.056057198367984, -87.73434815330167, 179.61839674590692), (1.447527, 1.510502, 0.953836), "PWM_Nordic_8x8x8_A314", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (10634.527, 2683.6882, 2625.217), (8.056055356941801, -87.73420776717852, -169.95287751667996), (1.447527, 1.510502, 0.953836), "PWM_Nordic_8x8x8_A315", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (10589.817, 3838.4617, 768.14886), (-0.3663634781795332, -149.86477876341078, 1.4692595520487692), (1.0, 1.0, 0.5973552), "PWM_Nordic_8x8x8_A316_317", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5722.234, 2181.6675, 899.83997), (0.0, 76.5107177882436, -0.0), (1.0, 0.82970876, 0.609134), "PWM_Nordic_8x8x8_A317", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (6716.023, 1654.9951, 533.61816), (2.195277353800809, 32.59185690482079, -178.461139776132), (1.0, 1.0, 0.609134), "PWM_Nordic_8x8x8_A318", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5310.3613, 10454.401, 890.5248), (5.038889414791673, 165.53234650428374, -4.084227980493877), (1.0896993, 1.0582781, 0.548922), "PWM_Nordic_8x8x8_A319", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (11195.012, 7362.4253, 2130.8403), (-3.5619507666070396, 133.94962990383675, -170.9733376305865), (1.0411859, 1.0300092, 1.0), "PWM_Nordic_8x8x8_A32_140", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5447.2236, 1822.1876, 1280.67), (1.6721810082123516, 166.0256761231507, -0.01672362743710732), (0.993406, 0.993406, 0.60254), "PWM_Nordic_8x8x8_A320", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5851.7007, 1643.3978, 1274.8663), (5.098453142834096, 148.43603595540412, 0.8490192816920102), (0.993406, 1.0239172, 0.60254), "PWM_Nordic_8x8x8_A321", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (12250.249, 3802.4453, 943.6337), (2.4252008142669377, -93.57141206559545, 0.316910539463687), (1.0, 1.0998176, 0.94989526), "PWM_Nordic_8x8x8_A322", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (10520.978, 4303.4556, 594.51044), (4.479954008868199, -152.5908506704728, 178.4266910201359), (1.0, 1.0, 0.609134), "PWM_Nordic_8x8x8_A323", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (11622.804, 4008.6252, 989.1655), (3.216772256244025, 169.34951207610916, 176.58928502447893), (1.0, 0.756927, 0.74083), "PWM_Nordic_8x8x8_A324", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (12050.935, 4092.7563, 1338.4265), (-4.097930823444094, 77.1359175327912, 1.8870546330975186), (0.993406, 0.993406, 0.60254), "PWM_Nordic_8x8x8_A325", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (11636.857, 4372.515, 1451.4187), (-1.7098997786447854, 41.55712805045109, 5.023132374504182), (1.0, 1.0, 0.8711427), "PWM_Nordic_8x8x8_A326", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (12345.94, 3748.0618, 1576.6823), (-12.077636657003474, -84.40272304615097, -97.28375689585847), (0.7923936, 1.0930909, 0.9404489), "PWM_Nordic_8x8x8_A327", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (12417.723, 2601.4397, 1667.6161), (-12.806185738189212, 116.85131769066093, -88.6629450293161), (0.96421945, 1.1246555, 1.1613135), "PWM_Nordic_8x8x8_A328", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (11485.542, 2516.4338, 2259.0544), (-53.33850734147022, 124.35933715764152, 93.19210777141915), (1.0, 1.435629, 1.282987), "PWM_Nordic_8x8x8_A329_325", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (7111.061, 8418.771, 1156.9512), (0.8055318599526321, 151.82916670233448, 1.5038825765943198), (0.51127416, 0.51127416, 0.51127416), "PWM_Nordic_8x8x8_A33_136", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (12066.749, 3819.8542, 1596.2136), (1.6624380745863474, -18.889768365321295, -107.44874291125086), (0.792394, 1.093091, 0.940449), "PWM_Nordic_8x8x8_A330", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (11151.705, 1686.1189, 2159.4268), (7.316298042674233, 77.02748239849309, -149.31403523303527), (0.977762, 0.578004, 0.857171), "PWM_Nordic_8x8x8_A331", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (10853.819, 2106.1157, 2478.3687), (2.3480408135784536, -113.18477272856097, -8.797790005435198), (0.977762, 0.578004, 0.857171), "PWM_Nordic_8x8x8_A332", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (11285.291, 1306.3323, 1678.3575), (-5.681822529140446, 170.32265946225036, -176.4601748885509), (0.68410325, 0.68410325, 0.68410325), "PWM_Nordic_8x8x8_A333", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (11521.214, 1417.078, 1286.1285), (3.8158831066276675, -25.293703833884198, -5.625610514162117), (0.684103, 0.7208946, 0.684103), "PWM_Nordic_8x8x8_A334", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (12113.802, 2321.9026, 1430.8602), (5.352964881102183, 26.977603414137256, -82.72700618911733), (0.8821912, 0.8821912, 0.8821912), "PWM_Nordic_8x8x8_A335", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (11554.848, 2061.5435, 1502.6621), (-6.582032703758209, 168.5777398278154, -89.70005369322833), (0.882191, 0.882191, 0.882191), "PWM_Nordic_8x8x8_A336", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (11086.173, 2025.647, 785.5259), (1.5982642033198886, -44.508304721310516, 3.732764974445808), (0.993406, 0.993406, 0.60254), "PWM_Nordic_8x8x8_A337", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (11491.302, 1768.7295, 1571.8733), (4.606415412916194, 75.71380530884123, -168.6609488870988), (0.977762, 0.578004, 1.2479888), "PWM_Nordic_8x8x8_A338", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (10918.602, 3747.841, 715.83716), (4.205657876847276, -52.074029118123, 0.22227597872987404), (1.0, 1.0, 0.6881465), "PWM_Nordic_8x8x8_A339", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (11396.236, 7344.0615, 1616.6971), (-0.4428406162668943, 122.13331805330111, 175.97132534309645), (1.0, 1.0316274, 0.919856), "PWM_Nordic_8x8x8_A34", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (11126.499, 4146.5786, 1005.953), (3.714892146028719, 166.81423728085, 3.430480824955776), (1.0, 1.0, 0.70685536), "PWM_Nordic_8x8x8_A340", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (6639.64, 1000.11835, 1031.3231), (-7.367035201081332, -122.44189395069894, -1.0559695015659396), (0.993406, 0.99063295, 0.60254), "PWM_Nordic_8x8x8_A341", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (9261.111, 3931.7454, 2048.7322), (-19.722595916198078, -100.69008676118875, -168.73603010320986), (0.7606586, 0.51251864, 0.6400676), "PWM_Nordic_8x8x8_A342", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (6506.091, 10861.441, 2334.455), (-29.129543594580355, -105.52977002543253, -165.26868691727665), (1.2657206, 1.2657206, 1.2657206), "PWM_Nordic_8x8x8_A343_467", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1951.8735, 9996.473, 2394.8318), (-11.99609239028053, -32.078795977400326, -169.57653752851294), (1.7821624, 1.53, 0.7775), "PWM_Nordic_8x8x8_A345", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2662.4165, 10669.254, 2488.8938), (-25.932434832358787, -15.163574975183012, -168.7277907109689), (1.0699999, 1.5375, 0.81), "PWM_Nordic_8x8x8_A346", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2141.2686, 10675.777, 2270.218), (-18.546690922803922, 6.477172769152423, -161.75464823937367), (1.4426305, 1.2933478, 0.91395587), "PWM_Nordic_8x8x8_A347", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (7089.0728, 10054.325, 2489.432), (-37.36425791698154, 16.935611089781165, -76.90809215310753), (1.4462662, 0.32737067, 1.265721), "PWM_Nordic_8x8x8_A348", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (7420.059, 10551.442, 1034.8378), (-6.473906742951065, -131.2288984703339, 9.953770374248547), (1.0, 1.0, 1.0), "PWM_Nordic_8x8x8_A349", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (11563.433, 5372.633, 1788.3414), (2.815757372334265, 87.74290560475502, 179.71913550974983), (0.76092213, 0.76092213, 0.93421435), "PWM_Nordic_8x8x8_A35_553", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (6944.9146, 10902.85, 1971.2023), (-4.910095954576374, -125.64642910744296, -175.96229126004155), (1.0, 1.0830493, 1.0), "PWM_Nordic_8x8x8_A350", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (6133.087, 10898.654, 2226.3271), (2.597254192049985, 163.92277839450975, -166.858017037208), (0.957071, 0.669252, 1.016141), "PWM_Nordic_8x8x8_A351", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (6248.3594, 11003.855, 1554.4166), (-0.7341919829820863, -8.55813655861602, -3.661621155024049), (0.9770585, 0.669252, 1.016141), "PWM_Nordic_8x8x8_A352", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (6705.6685, 10875.007, 2290.42), (-10.325253300549347, -162.50038951046426, -177.02407916130082), (0.957071, 0.669252, 1.016141), "PWM_Nordic_8x8x8_A353", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (6818.7993, 10933.711, 1364.9359), (-0.7341918345275021, -10.351684101809177, -3.6616203982729107), (0.957071, 0.669252, 1.016141), "PWM_Nordic_8x8x8_A354", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (6795.7583, 11044.737, 1838.5945), (-5.379089003120144, 2.1056547236961727, 177.11238168229332), (1.0, 1.0, 1.0), "PWM_Nordic_8x8x8_A355", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4199.026, 12050.469, 1641.9265), (-1.882476724054787, -13.69610618131244, -6.3751219691139305), (0.9423783, 0.669252, 1.1166188), "PWM_Nordic_8x8x8_A356_490", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (7380.5454, 10399.463, 1612.3932), (3.4569482800051783, -161.9526081320316, -179.73158003861454), (0.315033, 0.669252, 1.016141), "PWM_Nordic_8x8x8_A357", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3562.019, 12435.45, 706.6103), (7.182591212456828, -172.51725874322827, 0.04679306265739834), (0.5936542, 0.76369274, 1.0), "PWM_Nordic_8x8x8_A358_508", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2656.2808, 12480.167, 1040.0579), (5.296334028604472, -19.937866309519023, 9.260073180685863), (0.593654, 0.822645, 1.0675322), "PWM_Nordic_8x8x8_A359", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (11227.571, 571.91077, 1996.1891), (-39.32516209114172, 169.28594605270095, -86.40893383917356), (1.0, 1.435629, 1.282987), "PWM_Nordic_8x8x8_A36", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3785.1182, 12213.195, 1945.0765), (8.585931053474233, 64.14729929348904, 176.27779955073018), (0.9754351, 0.45960352, 0.83197606), "PWM_Nordic_8x8x8_A360", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2565.274, 12213.195, 1873.5577), (9.19547648372769, -112.40434825304482, 178.28593414509774), (0.957071, 0.459604, 0.831976), "PWM_Nordic_8x8x8_A361", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2614.9832, 12454.899, 1610.2974), (-2.6024472099755185, -107.3177158638196, -176.13927655830813), (0.9491093, 0.45164233, 0.8240143), "PWM_Nordic_8x8x8_A362", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3872.606, 11502.025, 652.08215), (8.217583052175884, -154.90502768391403, 2.014273131721183), (1.0, 1.0, 0.609134), "PWM_Nordic_8x8x8_A363_96", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3442.7969, 10079.661, 2846.2861), (7.443906819033961, 5.464293795773516, -174.60443698883392), (1.629881, 1.548407, 0.5453685), "PWM_Nordic_8x8x8_A364_517", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4100.114, 10286.496, 2928.756), (7.908234614296027, -5.281616370565795, 7.685340067279431), (1.629881, 1.3740499, 0.7374446), "PWM_Nordic_8x8x8_A365", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3999.7766, 8983.82, 2715.8037), (-66.33868937458541, -174.714852271177, -101.3432948777501), (0.8852246, 1.3977727, 1.3814352), "PWM_Nordic_8x8x8_A366", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3055.8298, 8338.542, 2744.8152), (-6.911071819903584, 88.11996923894365, 0.8163752234176375), (1.6530342, 1.374626, 0.71605617), "PWM_Nordic_8x8x8_A367_81", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5203.582, 10144.317, 2643.4612), (-2.5313109644488683, 7.142607790392777, 172.43143608422784), (1.629881, 1.548407, 0.65192), "PWM_Nordic_8x8x8_A368_525", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5235.355, 8922.573, 2529.865), (69.43219088502846, -8.696162482267903, 163.64346756623593), (1.1798483, 1.585079, 1.3118862), "PWM_Nordic_8x8x8_A369", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (10611.094, 1496.0282, 2511.7007), (-63.77911515735587, -173.80748131150798, 0.5410758290543954), (1.0287892, 1.0495, 1.0838001), "PWM_Nordic_8x8x8_A37", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (6068.9116, 8284.632, 601.37164), (-9.877655395703023, 28.699339445504602, -1.0923766190851631), (1.0, 1.0, 0.609134), "PWM_Nordic_8x8x8_A370", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (7400.265, 315.67807, 1095.1866), (6.794093710579883, -138.74004669479842, 4.936564678629052), (0.66495186, 0.70126766, 0.5656379), "PWM_Nordic_8x8x8_A371", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (9587.283, 3250.4404, 2502.8481), (-55.01825630851447, -89.22229914117788, -173.51387201679793), (1.045717, 1.045717, 1.045717), "PWM_Nordic_8x8x8_A372", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (11705.12, 4842.0186, 2107.3274), (32.21778061560739, 1.5320423407871446, 175.14635657539432), (1.0, 1.0, 0.919856), "PWM_Nordic_8x8x8_A373", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (11824.292, 4440.9844, 1933.5608), (-6.067964003978002, 126.6643879851783, -159.78498843230741), (1.0, 1.0161262, 1.0), "PWM_Nordic_8x8x8_A374", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (11523.339, 5010.0107, 1692.7288), (9.683414550845983, -171.56791540923848, 4.570120213284466), (0.6822611, 0.6621181, 0.6621181), "PWM_Nordic_8x8x8_A375", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4894.2056, 10185.02, 698.1711), (-15.710725269563174, 51.58654969378295, 0.6405257937684363), (0.753726, 0.753726, 0.753726), "PWM_Nordic_8x8x8_A376", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5594.453, 10241.608, 620.55005), (7.340103225986542, -119.75923786997795, -4.272644415636855), (1.0, 1.173469, 0.575139), "PWM_Nordic_8x8x8_A377", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5650.9316, 10478.5625, 1055.2051), (14.092538397041269, -73.4799474950658, 4.915739326645269), (0.8822653, 0.8822653, 0.8822653), "PWM_Nordic_8x8x8_A378_48", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (9933.374, 11059.181, 2012.8856), (22.049329921519195, 117.45210552399004, -178.1241483608431), (1.1458974, 0.869246, 1.326916), "PWM_Nordic_8x8x8_A379", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (10541.831, 4221.0957, 2568.188), (2.391458348141074, -92.41796271079369, -102.10582771336038), (1.218515, 0.989001, 1.218515), "PWM_Nordic_8x8x8_A38", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (7966.2515, 10008.452, 2264.7603), (-10.275999510762993, -131.0503447159041, -160.29974429844813), (1.0509905, 0.7631717, 1.1100605), "PWM_Nordic_8x8x8_A380_129", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (9489.841, 10108.816, 2541.897), (-69.42624934780666, -148.26575097129262, -114.11505344380261), (1.1137966, 1.2415293, 1.075618), "PWM_Nordic_8x8x8_A381", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5965.167, 1444.5859, 1379.2007), (-0.6664733179132744, 148.35043669666095, 0.8457183655299046), (0.549392, 0.6434023, 0.36878565), "PWM_Nordic_8x8x8_A382", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (6452.5347, 5126.782, 2222.187), (-5.151459134505341, 149.5338988686815, -174.7941397482624), (1.222601, 1.012303, 1.29147), "PWM_Nordic_8x8x8_A383", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (6283.889, 5109.264, 1471.4972), (-7.205230007315944, -173.47077471819156, -5.031402279618751), (0.726202, 0.7136415, 0.84970903), "PWM_Nordic_8x8x8_A384_4", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (10705.731, 3989.583, 830.07086), (3.7148923098732194, 174.0552061709646, 3.430480837767889), (1.0, 1.0, 0.706855), "PWM_Nordic_8x8x8_A385", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5097.2207, 4113.947, 1922.6172), (-0.5852971676985678, -97.3630731121927, -157.14276715209346), (0.9357791, 0.7254809, 1.0046481), "PWM_Nordic_8x8x8_A386", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4714.3276, 5765.712, 1401.4495), (-1.2484136888072421, 84.15474940718448, -10.252471862251069), (1.003445, 0.792265, 1.304748), "PWM_Nordic_8x8x8_A387", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4845.5933, 4673.5005, 1589.6179), (-2.2043463577358775, 84.3275984408092, -12.239684009086242), (1.003445, 0.792265, 1.304748), "PWM_Nordic_8x8x8_A388_30", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (9825.897, 10694.5625, 868.99713), (0.0, -141.6391486222084, 0.0), (1.0, 1.0, 1.0), "PWM_Nordic_8x8x8_A389", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4812.6045, 3471.2903, 2106.396), (20.478194126982277, -156.0822873472262, -172.68218954034867), (1.1358987, 0.6509768, 0.9301437), "PWM_Nordic_8x8x8_A39", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5815.6196, 4984.0454, 2520.6658), (-68.07025571327259, -176.42882111183985, -94.71462517830192), (0.96614295, 0.89974284, 0.96614295), "PWM_Nordic_8x8x8_A390", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (7158.9565, 8330.767, 1342.3176), (-8.38738997923236, 151.58633153494856, 1.5200041525863575), (0.511274, 0.511274, 0.511274), "PWM_Nordic_8x8x8_A391", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (10634.939, 4423.8965, 942.4767), (-0.36636356009150217, 151.26115534078, 1.4692611942739782), (0.7570113, 0.7570113, 0.35436633), "PWM_Nordic_8x8x8_A392_94", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4742.8545, 5144.598, 1182.691), (0.0, -168.37713955465657, 0.0), (1.0, 1.0, 1.0), "PWM_Nordic_8x8x8_A393_63", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2185.0537, 5742.048, 1337.5425), (14.80359590862421, -130.97830115807974, -5.214356144723992), (1.5320897, 1.5320897, 1.72224), "PWM_Nordic_8x8x8_A394", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (6934.1294, 5860.722, 2211.701), (57.7252113974218, 172.83325220964733, 0.2736510737938526), (1.0, 1.0, 1.0), "PWM_Nordic_8x8x8_A395", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5334.285, 6592.3823, 2481.4548), (-59.63705501952269, -18.57009487505788, 108.92754908795573), (1.20896, 1.409608, 1.20896), "PWM_Nordic_8x8x8_A396", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (6258.956, 1707.2555, 1073.5901), (-1.0567933294262533, -170.7906840835168, 0.2033188592252386), (0.549392, 0.56356955, 0.43912965), "PWM_Nordic_8x8x8_A397", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4332.919, 7609.8755, 2288.3682), (55.44011033313272, -82.96246751044663, 94.35633303450216), (1.0675, 1.0475, 1.419369), "PWM_Nordic_8x8x8_A398", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2894.22, 8793.244, 2847.3955), (-5.451476644478593, -141.35222620555177, -179.05679485486795), (1.0, 1.0, 1.0), "PWM_Nordic_8x8x8_A399", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (11631.941, 664.0951, 1219.8534), (-5.220642082701845, 172.51016826996675, 6.797284094821348), (1.068318, 1.107534, 1.0), "PWM_Nordic_8x8x8_A4", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (7343.555, 399.01053, 1661.4293), (-17.953400639360673, 18.789493757264275, 87.481247821167), (0.77881485, 1.2144439, 1.0618019), "PWM_Nordic_8x8x8_A40_288", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (6983.8228, 6656.357, 2180.1523), (57.72511695708587, 172.83325225954835, -5.6306448186023115), (1.0, 1.0, 1.0), "PWM_Nordic_8x8x8_A400", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3913.1792, 7248.4487, 1063.8193), (-0.7819517770597363, -175.30597744996166, 3.545392649777957), (0.846977, 1.0, 1.0691558), "PWM_Nordic_8x8x8_A401", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3517.2046, 11204.246, 537.5346), (3.2111448383385217, 175.9132598292376, -0.22921749675423464), (1.0, 1.0, 0.601902), "PWM_Nordic_8x8x8_A402", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (521.05975, 3747.6902, 1338.5616), (5.018713887637518, 82.62695409202578, 0.8279119072565667), (0.634456, 0.725158, 0.634456), "PWM_Nordic_8x8x8_A403_112", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (8211.005, 10247.781, 896.34576), (0.0, -13.029845388041254, 0.0), (1.0, 1.0, 1.0), "PWM_Nordic_8x8x8_A404", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1887.4812, 3751.757, 946.7508), (0.0, 78.71085259838215, -0.0), (1.075194, 0.91578895, 0.5249231), "PWM_Nordic_8x8x8_A405_122", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1098.1134, 3606.078, 837.41986), (10.160916254183643, -90.37591651895838, 1.810984325013843), (1.075194, 0.915789, 0.6652272), "PWM_Nordic_8x8x8_A406", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (341.49658, 12276.058, 1165.6117), (0.21757567390388188, 175.0289256625289, 2.157531843836474), (1.0, 0.9000896, 1.258097), "PWM_Nordic_8x8x8_A407_38", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (476.61456, 3735.1755, 1899.7695), (2.6940721928899833, 176.6382180045794, 178.48758150215397), (0.8970718, 0.528022, 0.917082), "PWM_Nordic_8x8x8_A408", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1996.3934, 3442.7878, 2313.2834), (-25.69888307291846, -100.46008008709917, -176.70312504405462), (0.798375, 0.7181471, 0.917082), "PWM_Nordic_8x8x8_A409", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (8627.598, 2000.1564, 2593.0134), (-79.65009341183735, 129.5888392203059, -36.87378585508895), (1.0, 1.0, 1.0), "PWM_Nordic_8x8x8_A41", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2015.527, 3600.039, 1766.0739), (2.496249712587494, 169.83886624245807, -177.996084362689), (0.798375, 0.528022, 0.917082), "PWM_Nordic_8x8x8_A410", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2091.646, 3046.275, 2478.73), (-58.914860475779406, -92.01147639532013, 82.41012120049567), (0.88327646, 1.3189056, 1.1662636), "PWM_Nordic_8x8x8_A411", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (683.5768, 3253.7908, 2380.0083), (-63.595310524411516, -58.80963461802008, 51.87413588277663), (0.883276, 1.318906, 1.166264), "PWM_Nordic_8x8x8_A412", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2757.1545, 3683.2803, 1759.7305), (-14.774412865003056, -101.61407531248827, 94.36345816038525), (1.4561, 1.374626, 1.1421794), "PWM_Nordic_8x8x8_A413_135", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4085.8325, 3322.5718, 1619.942), (-23.334101079332147, -108.7559331475385, 96.83039758133098), (1.4561, 1.374626, 1.142179), "PWM_Nordic_8x8x8_A414", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3830.257, 2477.9705, 2146.2593), (11.639221782167322, 173.9333522793377, 99.96106082298381), (1.0213671, 0.69313616, 1.202068), "PWM_Nordic_8x8x8_A415", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3210.7861, 3398.354, 932.1661), (14.35365417364703, -104.49391042526241, 2.7120568906407434), (1.0, 1.0, 1.0), "PWM_Nordic_8x8x8_A416", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3302.287, 3456.942, 1630.5856), (-8.560302297948674, -106.90645608396133, -174.0281227549254), (1.009998, 1.0, 1.0), "PWM_Nordic_8x8x8_A417", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2845.53, 3236.7034, 2366.0955), (-50.96289176562945, -124.69968148084052, 112.37817914067965), (1.4561, 1.374626, 1.2906036), "PWM_Nordic_8x8x8_A418", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1683.5067, 4111.919, 1131.5399), (-6.43612615828974, 50.818679097110255, 5.965309633782424), (1.075194, 0.915789, 0.41373903), "PWM_Nordic_8x8x8_A419", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (9286.475, 2215.5847, 2748.2139), (-67.93005263551572, 72.89336686349793, -68.62626749895642), (1.0, 1.0, 1.0), "PWM_Nordic_8x8x8_A42", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1351.1223, 3137.9978, 2536.0564), (-74.41820776300546, -114.29391503651873, 113.75608100503145), (1.1940694, 1.374626, 1.290604), "PWM_Nordic_8x8x8_A420", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (657.497, 3850.7134, 783.32544), (11.958301634752987, -19.753876228312187, 4.539351641677644), (1.075194, 0.915789, 0.665227), "PWM_Nordic_8x8x8_A421", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (526.85425, 3775.0537, 960.07166), (2.8152603567329213, -17.576967015656408, 2.7254762945608215), (0.9610228, 0.634456, 0.634456), "PWM_Nordic_8x8x8_A422", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (906.95715, 2061.9353, 966.5581), (10.177878800960809, -176.67717298301775, 2.6671539318482598), (1.075194, 0.915789, 0.665227), "PWM_Nordic_8x8x8_A423", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1358.4244, 2161.4312, 779.62244), (13.297597984122135, 84.24780896906354, -2.8153990046139863), (1.075194, 0.915789, 0.665227), "PWM_Nordic_8x8x8_A424", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2118.7078, 1509.9545, 755.0789), (13.297598180260817, 34.62349252276303, -2.8153990006383185), (1.075194, 0.915789, 0.665227), "PWM_Nordic_8x8x8_A425", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2298.755, 979.45593, 1178.3373), (6.390746703295027, 4.086153980320612, 95.69812835665547), (1.053614, 1.374626, 1.142179), "PWM_Nordic_8x8x8_A426", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3743.2085, 1069.7676, 2150.7637), (-51.52080835546384, 168.28579783479034, -82.18077816353801), (1.053614, 1.374626, 1.142179), "PWM_Nordic_8x8x8_A427", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4554.1914, 1696.8853, 1022.5436), (0.0, 169.35069938702844, -0.0), (1.0, 1.0, 0.9752824), "PWM_Nordic_8x8x8_A428", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4587.2017, 1808.2509, 1963.4172), (-20.005092675577334, 81.7224341653789, 96.02948574825336), (1.3269978, 1.2912012, 0.97711325), "PWM_Nordic_8x8x8_A429", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1491.0629, 9650.617, 2500.5867), (3.76864589638638, -174.88045039030138, 177.72927092212572), (1.4561005, 1.3746257, 1.0), "PWM_Nordic_8x8x8_A43", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1481.8308, 2548.0076, 2391.5947), (-78.73403396492938, 52.92711183995299, 119.13798264661568), (1.053614, 1.1396488, 1.4728028), "PWM_Nordic_8x8x8_A430", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4204.957, 782.4438, 1387.28), (-10.272918356330653, 150.05310732759398, 91.92328563240653), (1.4561, 1.4448001, 1.142179), "PWM_Nordic_8x8x8_A431", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4232.54, 7868.426, 540.20197), (-10.59204217139203, -103.47528598982717, -4.981201548910513), (1.0, 1.0, 0.609134), "PWM_Nordic_8x8x8_A432_882", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4035.333, 1111.4749, 703.3467), (-9.036529744982689, -134.61414593167865, 2.873171348505891), (1.090593, 0.939932, 0.581691), "PWM_Nordic_8x8x8_A433", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4182.5015, 1977.8562, 2081.9648), (-55.76587003713807, 104.61480517951347, 85.3078683272456), (1.2571068, 1.2458068, 0.9431859), "PWM_Nordic_8x8x8_A434", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4183.696, 1417.5042, 1746.2368), (2.496249713384858, 75.65951315616225, -177.99608417361497), (0.798375, 0.528022, 0.917082), "PWM_Nordic_8x8x8_A435", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4298.3115, 1417.5042, 1449.0186), (2.496249713384858, 75.65951315616225, -177.99608417361497), (0.8922989, 0.6219457, 1.011006), "PWM_Nordic_8x8x8_A436", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4266.7085, 1705.6133, 1216.655), (-1.1640014302345034, -164.79806024259977, 1.3790670927640856), (0.7395968, 0.65902424, 0.8187519), "PWM_Nordic_8x8x8_A437", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3697.1597, 1911.3932, 2422.1912), (7.320831565349567, 167.7699021554704, 128.63831815583669), (1.4561, 1.374626, 1.142179), "PWM_Nordic_8x8x8_A438", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2993.2983, 2465.45, 2378.0337), (8.772216966732547, 175.59107045184817, 1.0590820890191328), (1.4561, 1.374626, 1.142179), "PWM_Nordic_8x8x8_A439", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (994.7837, 7806.6206, 1958.3733), (-35.26428522856676, 68.30805747005803, -77.62933894330496), (1.5920435, 1.5535445, 1.0), "PWM_Nordic_8x8x8_A44", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (683.5759, 2772.0613, 2217.5125), (-58.46430000815561, 33.0548764374322, -40.82501407798494), (0.883276, 1.318906, 1.166264), "PWM_Nordic_8x8x8_A440", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (344.78314, 2539.943, 787.21326), (11.107988481142323, 77.4239378089223, 6.358759691996919), (1.075194, 0.915789, 0.665227), "PWM_Nordic_8x8x8_A441", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (283.58105, 2455.1497, 1404.1559), (5.14715105498863, -117.84264082070392, -91.45165435501166), (1.0257975, 1.318906, 1.0848786), "PWM_Nordic_8x8x8_A442", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1004.54803, 2577.4846, 2280.4233), (9.094149934467243, -64.7455074051186, -169.4863606342385), (0.798375, 0.528022, 0.917082), "PWM_Nordic_8x8x8_A443", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (785.3408, 2389.118, 1032.9044), (-1.9791562363922284, 70.64533315071509, -3.427215428267724), (0.798375, 0.528022, 0.917082), "PWM_Nordic_8x8x8_A444", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (705.2611, 2311.195, 1765.2522), (14.0286837814616, -89.89532128654879, -176.57200985572788), (0.798375, 0.528022, 0.917082), "PWM_Nordic_8x8x8_A445_38", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2169.828, 1418.0819, 1867.6833), (8.455022787651389, -24.338925757552637, -169.07305142160058), (0.8690548, 0.528022, 1.0852094), "PWM_Nordic_8x8x8_A446", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2087.6694, 1673.7712, 2145.2407), (-3.8110962519655502, 59.962925501721216, -173.19445045186612), (0.798375, 0.7393707, 0.917082), "PWM_Nordic_8x8x8_A447", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2360.7925, 2526.521, 2317.5308), (-7.227356103368202, -4.490417027435724, 175.3254471043785), (1.9445684, 1.374626, 0.75053036), "PWM_Nordic_8x8x8_A448_49", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3002.332, 1103.5385, 2239.123), (-83.08180914628628, -23.512521427160966, 107.69826630552303), (1.053614, 1.374626, 1.5744114), "PWM_Nordic_8x8x8_A449", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1426.7299, 8778.6875, 2389.7937), (3.76864568310768, -174.8804487960063, -165.47622469038677), (1.4561, 1.374626, 1.0), "PWM_Nordic_8x8x8_A45", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2275.9373, 454.03064, 1225.4672), (-4.094724576622706, -156.20699814059265, 86.13691684444936), (1.0726849, 1.5680778, 1.142179), "PWM_Nordic_8x8x8_A450", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4135.352, 401.05365, 1329.5317), (7.71847591761912, -13.639952921853213, 90.55261025740626), (1.1424905, 1.374626, 1.142179), "PWM_Nordic_8x8x8_A451", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3531.5684, 503.97043, 2086.8247), (0.3030900900701525, 89.25195449684098, 153.15590940154303), (1.2401285, 1.0, 0.65503186), "PWM_Nordic_8x8x8_A452_68", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2851.2236, 512.7807, 2100.6455), (-11.000365204918454, 87.46806885855665, -159.86418558794523), (1.334894, 1.1535041, 0.655032), "PWM_Nordic_8x8x8_A453", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3308.264, 1651.8821, 2214.1912), (-0.9815366202444001, -103.22075909608537, -175.98172731730017), (0.8585708, 0.9516251, 0.8585708), "PWM_Nordic_8x8x8_A454_81", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2649.9465, 5678.549, 1306.7118), (14.865214278212486, -92.38016844244032, 5.032087786504159), (1.53209, 1.53209, 1.53209), "PWM_Nordic_8x8x8_A455_6", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (8172.657, 10369.885, 881.75256), (3.3649262165286298, -33.090447977283766, 0.6769053544144089), (1.107433, 0.772506, 0.555879), "PWM_Nordic_8x8x8_A456", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5196.9414, 1813.7007, 1686.4688), (1.7371648073333543, 55.1108123894158, 176.48991514404403), (0.7735535, 0.7735535, 0.99737877), "PWM_Nordic_8x8x8_A457", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (9613.899, 11620.127, 2095.7646), (11.935194869326399, 116.4887383735667, 177.87329190450717), (1.145897, 1.1155455, 1.2556647), "PWM_Nordic_8x8x8_A458", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (7620.2153, 6685.352, 1800.2218), (-7.076172835502206, -1.1718446257354809, -173.4510871826462), (1.272178, 1.219393, 1.272178), "PWM_Nordic_8x8x8_A459", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (9587.283, 3665.8708, 2438.943), (-9.18801859559876, -90.10216842935225, 172.27068433575784), (1.045717, 1.045717, 1.045717), "PWM_Nordic_8x8x8_A46", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (8647.889, 5282.544, 1938.3308), (-8.173522220872979, 73.9793192999941, 174.88990616800533), (1.272178, 1.219393, 1.272178), "PWM_Nordic_8x8x8_A460_86", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (7419.343, 6186.739, 1159.6636), (4.5602648845331775, -79.06073967948087, 7.172761012524247), (1.272178, 1.219393, 1.272178), "PWM_Nordic_8x8x8_A461", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3671.3306, 5832.974, 1162.1038), (11.938826794607698, -70.2144574087706, 10.232956324581927), (1.53209, 1.53209, 1.53209), "PWM_Nordic_8x8x8_A462_8", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (7289.7217, 7170.4165, 1442.5886), (8.313346610351367, -148.66915687456085, -1.7441095107454498), (1.272178, 1.219393, 1.272178), "PWM_Nordic_8x8x8_A463", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (7549.956, 6664.2544, 1508.2384), (-3.958098810987543, -19.175201819227702, 2.258849907213235), (0.96099603, 1.219393, 1.272178), "PWM_Nordic_8x8x8_A464", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2055.6587, 1774.0352, 735.0037), (13.297598180260817, 34.62349252276303, -2.8153990006383185), (1.075194, 0.915789, 0.665227), "PWM_Nordic_8x8x8_A465", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2095.4692, 1259.7524, 935.16284), (-10.36099372220125, 148.45676201412323, 6.840587424711409), (0.9229326, 0.7635276, 1.011969), "PWM_Nordic_8x8x8_A466", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1141.3146, 1878.5394, 941.88763), (-0.7609863588100388, -20.095887877073164, 1.0356553535861488), (1.075194, 0.915789, 0.7430383), "PWM_Nordic_8x8x8_A467", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (763.7986, 7209.6294, 1226.3191), (-1.1239931815812283, 30.893076701926155, 25.37340485418969), (1.214577, 1.258034, 1.1450797), "PWM_Nordic_8x8x8_A468", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3841.0745, 976.72656, 680.57996), (19.550319577219376, -162.83326072748227, 6.732218131877281), (1.075194, 0.915789, 0.665227), "PWM_Nordic_8x8x8_A469", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (6615.2446, 497.18057, 1688.4496), (-5.254088882904717, 129.18029187676268, -4.315490532483062), (0.75914806, 0.75, 0.75), "PWM_Nordic_8x8x8_A47", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2205.1199, 1805.2053, 540.5571), (21.10496657106683, 35.981892831290146, 5.711337828797702), (1.075194, 0.915789, 0.665227), "PWM_Nordic_8x8x8_A470", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (884.3186, 1953.0449, 1174.3953), (-0.9074401291894714, -31.887817584470554, 0.9100912328200909), (1.075194, 0.915789, 0.42219403), "PWM_Nordic_8x8x8_A471", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1013.5838, 1601.9164, 926.55414), (-1.1774291111449007, 9.98105485040137, 6.827568006702436), (1.075194, 0.915789, 0.80582917), "PWM_Nordic_8x8x8_A472_25", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (220.75372, 3743.7705, 938.0825), (-4.236694215136962, -76.78467041616138, -1.8663636557803216), (0.961023, 0.634456, 1.0525829), "PWM_Nordic_8x8x8_A473_30", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3761.4119, 6213.403, 2245.042), (-18.606715077037933, 123.74218425767803, -178.63411418115655), (1.6874026, 1.53209, 2.356575), "PWM_Nordic_8x8x8_A474_10", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1377.3857, 1750.1948, 2252.2498), (-77.78236520201197, 75.04388178831397, 97.39171098604366), (1.053614, 1.139649, 1.341007), "PWM_Nordic_8x8x8_A475_87", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3832.4177, 1757.8154, 510.11523), (4.365753294243404, -20.234253769567474, 1.3297721172301296), (0.84370077, 0.84370077, 0.84370077), "PWM_Nordic_8x8x8_A476", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (7872.4697, 5478.058, 1547.0665), (2.351543360405513, -62.738354184482176, 8.16381982667898), (1.272178, 1.2639914, 1.272178), "PWM_Nordic_8x8x8_A477", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (9211.335, 5584.731, 2500.115), (-8.333221605489918, 83.42413320957168, -178.0213801687069), (1.2707634, 1.2179782, 1.2707634), "PWM_Nordic_8x8x8_A478", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (9183.932, 6045.7065, 2599.7898), (-36.73531932653649, 62.368905252128535, 175.71309781616205), (1.270763, 1.217978, 1.5459428), "PWM_Nordic_8x8x8_A479", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1463.0396, 7367.5703, 1844.3889), (-7.434935506613678, 177.22596163540717, -120.06585449735071), (1.4561, 1.374626, 1.0), "PWM_Nordic_8x8x8_A48", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (8203.076, 7088.686, 2535.7695), (-22.723481633810128, 88.38634802443939, 153.80594579346428), (1.270763, 1.217978, 0.8369675), "PWM_Nordic_8x8x8_A480", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (8440.123, 6663.624, 2709.959), (-19.518037709811736, 18.581080814491003, -169.85658624232727), (1.270763, 1.217978, 0.90955746), "PWM_Nordic_8x8x8_A481", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (8953.375, 7058.973, 2659.1343), (-14.978912051834184, 19.420554732010984, -170.10555240618234), (1.270763, 1.217978, 0.909557), "PWM_Nordic_8x8x8_A482", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (9981.473, 6007.366, 2806.0925), (-14.978852295118633, 19.42058627264575, -179.20590925986718), (1.270763, 1.3147788, 0.9137949), "PWM_Nordic_8x8x8_A483", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (8088.113, 7096.6978, 2496.6965), (-2.2844846944857116, -10.067473392618211, -171.78038683462955), (1.270763, 1.217978, 1.270763), "PWM_Nordic_8x8x8_A484", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (8407.517, 5706.859, 2285.6665), (-13.819642679465977, 58.68544816820766, -178.26290024760638), (1.0, 1.0, 1.0), "PWM_Nordic_8x8x8_A485", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (7975.6387, 7234.0767, 1276.9143), (-2.710204497900033, 64.12891076381152, -3.6641235980880102), (0.41076154, 0.66915846, 0.72194356), "PWM_Nordic_8x8x8_A486_116", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (7932.0312, 7192.6206, 1747.8511), (8.765153783150176, -123.07537417094181, -179.88733548914024), (0.620808, 0.669158, 1.0161068), "PWM_Nordic_8x8x8_A487", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (8477.611, 5458.522, 1908.2028), (-2.0980221451516567, -18.26330467113189, -170.51355706618048), (0.8006662, 0.669158, 1.016107), "PWM_Nordic_8x8x8_A488", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (9137.043, 5323.7266, 1634.1443), (0.8399969431104503, 10.451658475002887, 174.9879717458912), (0.620808, 0.669158, 1.016107), "PWM_Nordic_8x8x8_A489", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (985.63074, 7439.4404, 1376.7821), (-17.780458715057573, 73.17881381743399, -92.10464958354571), (1.263284, 1.1818099, 0.80718416), "PWM_Nordic_8x8x8_A49", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2632.8286, 5990.709, 2360.355), (-20.301420295097223, 61.489775296674345, -171.5833712365141), (1.53209, 1.53209, 1.53209), "PWM_Nordic_8x8x8_A490_12", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (9472.41, 11580.586, 1399.3663), (-12.550564054407795, 32.785515411828754, -7.749449230136442), (1.0, 1.0, 1.0), "PWM_Nordic_8x8x8_A491", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5487.122, 10174.59, 702.03125), (5.0388897048136165, -65.13748341524001, -4.084228532222107), (1.089699, 1.058278, 0.548922), "PWM_Nordic_8x8x8_A492", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2113.0713, 6534.2944, 2353.0554), (-19.563662113487588, 36.123697052698276, 179.95921719155754), (1.265, 1.1949999, 0.86249995), "PWM_Nordic_8x8x8_A493", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (10950.122, 4624.729, 938.7569), (2.837943952622573, 156.59428093708354, -0.44281000642664115), (1.0818795, 1.0913274, 0.7265889), "PWM_Nordic_8x8x8_A494_11", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4411.7744, 11545.208, 2585.7017), (2.597254730600827, 161.50690245854372, -166.8568202600578), (0.957071, 0.669252, 1.016141), "PWM_Nordic_8x8x8_A495", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (6429.599, 5181.244, 2411.4219), (-12.200896664496824, -124.48557830068144, 177.8027358959374), (1.083861, 0.95418197, 1.29147), "PWM_Nordic_8x8x8_A496", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (8130.0557, 8680.487, 512.5531), (9.19580566282344, -29.853825962937474, -0.5355838705756445), (1.107433, 1.0, 0.555879), "PWM_Nordic_8x8x8_A497", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (8024.935, 8007.13, 604.496), (3.9682570833652693, 16.2901604113505, 2.798657524444191), (1.107433, 1.0, 0.555879), "PWM_Nordic_8x8x8_A498", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (6345.275, 5073.5786, 1955.6412), (4.953143743995932, 31.557613864340247, -177.6155729156051), (0.6894375, 0.8160178, 1.1595049), "PWM_Nordic_8x8x8_A499", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (7906.6978, 3175.3188, 2498.788), (2.689298257764335, -166.36511288575613, -171.12843836167997), (1.34553, 0.8135419, 1.0457166), "PWM_Nordic_8x8x8_A5", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2457.9631, 7030.523, 2684.6047), (15.603089859237684, 0.762144092865953, 1.72592151901655), (1.4561, 1.374626, 0.47086978), "PWM_Nordic_8x8x8_A50_94", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (6400.5884, 7084.8813, 2016.4651), (4.557825712469967, 102.7991271552301, -174.38661171145392), (0.7355681, 0.816018, 1.336498), "PWM_Nordic_8x8x8_A500", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (6153.6274, 5567.988, 2374.8784), (-54.080724228734645, 132.13525422604238, -138.70062129562342), (1.1517874, 1.256847, 1.287518), "PWM_Nordic_8x8x8_A501", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (10107.0, 10018.638, 590.4443), (14.216490632429469, -121.00150169690211, 1.0961432970491678), (1.0, 1.0, 0.6683587), "PWM_Nordic_8x8x8_A502", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (8364.255, 9886.9, 651.3983), (6.391238555410165, 144.36685280297294, 0.3677790779860796), (0.866382, 0.837422, 0.50546753), "PWM_Nordic_8x8x8_A503", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (11966.579, 8532.621, 1243.1327), (2.183561276493945, 87.51835700522923, 91.14974299700042), (1.4561, 1.374626, 1.199912), "PWM_Nordic_8x8x8_A504", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (10693.127, 10148.857, 796.9361), (0.0, -114.98048322576, 0.0), (1.107433, 1.0, 0.62543666), "PWM_Nordic_8x8x8_A505", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4110.7285, 11839.671, 1222.5364), (10.42733485531134, -141.7086751749858, -0.003265191218857543), (1.0, 1.0, 1.0), "PWM_Nordic_8x8x8_A506", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (8013.756, 7983.712, 546.10425), (9.19580566282344, -29.853825962937474, -0.5355838705756445), (1.107433, 1.0, 0.555879), "PWM_Nordic_8x8x8_A507", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (7713.2944, 7972.743, 839.7115), (-2.7008362641857895, -10.963989968654147, 1.4874211826853698), (1.107433, 1.0, 0.555879), "PWM_Nordic_8x8x8_A508", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (9768.389, 10623.788, 2407.7288), (-54.70388361932413, -159.1772656370886, -104.38896987880831), (1.075618, 1.075618, 1.075618), "PWM_Nordic_8x8x8_A509", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4844.813, 3770.2732, 598.83514), (0.0, 90.8950802974193, -0.0), (1.0, 1.0, 0.6091341), "PWM_Nordic_8x8x8_A51_19", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (6914.34, 5822.0977, 1045.2465), (-8.586913037239528, 165.63141003366565, -0.6157226364096163), (1.272178, 1.219393, 0.97649), "PWM_Nordic_8x8x8_A510", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (6686.8403, 5555.565, 2094.35), (-5.046997406800224, 150.96410895521385, -173.92349638098332), (1.272178, 1.219393, 0.97649), "PWM_Nordic_8x8x8_A511", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (6755.941, 6355.3447, 2143.7173), (-15.7952849614412, -168.3153005446855, -178.65909397477358), (1.272178, 1.219393, 0.97649), "PWM_Nordic_8x8x8_A512", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (6658.697, 5771.3706, 2244.1677), (-10.459289968143723, 171.22753722555734, -176.0347821365706), (1.272178, 1.219393, 0.97649), "PWM_Nordic_8x8x8_A513", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (6469.2515, 7115.8496, 1380.657), (8.646139184328712, -18.384766105810005, -7.534546467210551), (0.677365, 0.677365, 0.849709), "PWM_Nordic_8x8x8_A514", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (6302.6143, 1434.988, 1099.3558), (-0.9991453006814001, -138.12055449269346, 4.51413282098457), (0.549392, 0.56357, 0.43913), "PWM_Nordic_8x8x8_A515", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (6493.0835, 1188.4199, 1123.5118), (-2.616913246023434, -116.15485257594072, 3.8125596833839395), (0.549392, 0.56357, 0.43913), "PWM_Nordic_8x8x8_A516", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4415.6226, 11460.861, 1276.0629), (8.244864489428457, -103.63341410242829, 6.406145893295919), (0.7035206, 0.7035206, 0.7035206), "PWM_Nordic_8x8x8_A517", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1725.3859, 6501.9297, 1154.3898), (6.203321345430237, -85.76410234295398, -1.9192201338151293), (1.251712, 1.258034, 1.379101), "PWM_Nordic_8x8x8_A518_157", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4732.773, 11177.893, 1110.6995), (19.967547556939092, -108.9332979006478, 4.807107014986295), (0.703521, 0.703521, 0.71292186), "PWM_Nordic_8x8x8_A519", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4608.368, 3366.2776, 681.0841), (13.992502164077235, -30.66717244508003, 1.62015069470268), (1.0, 1.0, 0.609134), "PWM_Nordic_8x8x8_A52", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (10898.9795, 6485.7495, 1170.073), (7.054556720586232, -166.14801451585302, 3.7897454577898504), (0.15473704, 0.43478346, 0.42549115), "PWM_Nordic_8x8x8_A520", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (8060.3584, 6982.2505, 2097.2476), (-14.889949470857923, 7.7479439265912475, -173.47010971793205), (0.74366915, 0.6908841, 0.74366915), "PWM_Nordic_8x8x8_A521", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (8721.523, 5326.7583, 1367.7822), (-2.7169796940051274, 177.09521247506217, -2.16870118591364), (0.800666, 0.669158, 1.016107), "PWM_Nordic_8x8x8_A522", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (7843.715, 6849.4263, 1800.8488), (8.05245963294451, -118.57471439786922, -176.9482388205826), (0.800666, 0.68161434, 1.016107), "PWM_Nordic_8x8x8_A523", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (7953.9473, 6084.6245, 1980.5175), (-3.9837657931870214, -49.97748713506171, -163.30299062619133), (0.800666, 0.669158, 1.016107), "PWM_Nordic_8x8x8_A524", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (8103.6875, 5682.5225, 1817.0771), (-4.190093089800009, -38.650202981107455, -163.09166575925198), (1.0321791, 0.669158, 1.016107), "PWM_Nordic_8x8x8_A525", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (8387.268, 6264.4814, 2518.4558), (-10.92657473357262, -36.83123912880659, -154.2121641558909), (0.800666, 0.669158, 1.016107), "PWM_Nordic_8x8x8_A526", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (9052.322, 5480.0215, 1983.2031), (-1.7043756240580104, 15.985468117602416, -177.49914525172278), (0.6324552, 0.50094724, 1.288591), "PWM_Nordic_8x8x8_A527", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (7973.4844, 7134.244, 1840.9629), (-1.4162905205162664, 49.04148459983473, -176.81622440121336), (0.620808, 0.669158, 1.016107), "PWM_Nordic_8x8x8_A528", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (6905.492, 865.31805, 1045.0248), (0.0, 158.1973940516047, -0.0), (0.649982, 0.649982, 0.550583), "PWM_Nordic_8x8x8_A53_541", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (841.59546, 9182.016, 2474.5837), (-88.07612447821735, 110.50433711673512, 62.35221531415591), (1.5310261, 1.4654552, 1.3243693), "PWM_Nordic_8x8x8_A54", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3617.4656, 7393.0405, 2700.9285), (-62.544687420350975, 160.63931942710306, 166.1371966976387), (0.7075, 0.765, 0.8175), "PWM_Nordic_8x8x8_A55", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (10858.564, 6387.104, 1170.0892), (14.26947847737102, 153.21614379138634, 33.863357686964086), (0.154737, 0.44860548, 0.3785135), "PWM_Nordic_8x8x8_A553", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (8188.4023, 8562.916, 2450.9426), (-5.3002914431388986, 158.4051198553983, -162.02252526784682), (1.4561, 1.374626, 1.1079068), "PWM_Nordic_8x8x8_A56_411", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (9941.043, 9502.904, 2422.6924), (-5.738829573830602, 149.59881367761704, 172.3768101724604), (1.6648412, 1.374626, 0.8404179), "PWM_Nordic_8x8x8_A57_412", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (8802.759, 9233.944, 2731.0237), (7.741057489722103, 141.70701088504012, -173.6846414781033), (1.629881, 1.548407, 1.3161232), "PWM_Nordic_8x8x8_A58", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4199.287, 10810.609, 648.835), (0.0, -123.34912940723217, 0.0), (1.0, 1.0, 0.609134), "PWM_Nordic_8x8x8_A59", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (8304.995, 2897.6968, 2833.0742), (75.93793428412684, 124.63316719367916, -21.107113706851436), (1.045717, 1.045717, 1.045717), "PWM_Nordic_8x8x8_A6_427", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (10386.752, 9899.633, 2384.506), (-3.9993288915366003, -14.95703030161388, -163.53666642551332), (1.7239399, 1.6346564, 1.0), "PWM_Nordic_8x8x8_A60", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (8746.049, 9950.503, 2687.9836), (4.702819898507668, 146.14598868052977, -178.2677437150936), (1.4561, 1.374626, 1.0), "PWM_Nordic_8x8x8_A61", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (10809.976, 9236.978, 2402.7231), (-11.20742927450276, 166.5008845534315, -163.9229976815698), (1.4561, 1.374626, 1.0), "PWM_Nordic_8x8x8_A62_425", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (7365.7056, 651.6571, 820.3933), (-1.2297667667217598, 50.32800975411663, 0.24869634145028352), (1.17101, 1.023785, 0.520438), "PWM_Nordic_8x8x8_A623", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (11023.613, 10135.991, 2421.0916), (-14.410032311999204, 179.7323861645015, 123.73675617609052), (1.4561, 1.374626, 1.0), "PWM_Nordic_8x8x8_A63", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (9995.96, 1215.2003, 2638.6292), (65.407536361929, -77.75647934909529, -168.20044568633028), (0.6250191, 1.5105025, 1.499538), "PWM_Nordic_8x8x8_A64_3", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (8750.766, 1367.9426, 2660.2146), (8.056057198367984, -87.73434815330167, 179.61839674590692), (1.6547848, 1.510502, 0.9538363), "PWM_Nordic_8x8x8_A65", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (11230.643, 8839.637, 2540.421), (2.2487374423052646, 29.349735143319656, 169.3442464510131), (1.4561, 1.374626, 1.0), "PWM_Nordic_8x8x8_A66", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (8057.8506, 9677.984, 2469.323), (-76.22896161671164, -112.38501247616841, -173.7250053674195), (1.0911641, 1.374626, 1.4748327), "PWM_Nordic_8x8x8_A67_60", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (7841.7524, 10420.718, 2390.003), (-65.03524625249761, -102.25236143714575, 117.19423164746061), (1.2692373, 1.374626, 1.474833), "PWM_Nordic_8x8x8_A68", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (10688.706, 10264.312, 2248.3394), (-12.423981973936748, 175.96772447205478, 156.7534993504591), (1.4561, 1.374626, 1.0), "PWM_Nordic_8x8x8_A69", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (9490.289, 4991.6255, 2270.937), (-70.2164636378195, 17.233118591531152, -13.513055601485915), (1.0, 1.0, 1.0), "PWM_Nordic_8x8x8_A7_522", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4737.3706, 6760.2515, 1461.3383), (-0.3398132808373269, -9.899291345006482, 87.80910887368137), (1.3567626, 1.2752886, 1.2640887), "PWM_Nordic_8x8x8_A70", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4057.563, 1335.7357, 734.59503), (3.06706164740546, 164.2600631916023, 0.2830950067537139), (1.0, 1.0, 1.0), "PWM_Nordic_8x8x8_A700", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2339.6265, 3474.7673, 819.4996), (5.726682406028649, -120.2332133022636, 1.3103942330489673e-06), (1.1594052, 1.0, 0.609134), "PWM_Nordic_8x8x8_A71", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2163.1948, 7426.324, 2609.8748), (-38.70447078091314, -22.56582842555136, -163.91534319885892), (1.0, 1.0, 1.0), "PWM_Nordic_8x8x8_A72", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4747.662, 3380.8005, 740.0232), (0.0, -54.57150284543587, 0.0), (1.0, 1.0, 0.26233613), "PWM_Nordic_8x8x8_A73", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3038.6616, 7036.1416, 2774.0146), (-0.22436521230355863, 0.29122729856491036, 1.6622619794545386), (1.4561, 1.374626, 0.5510497), "PWM_Nordic_8x8x8_A74", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1987.4165, 4005.0024, 1573.0162), (-2.5535890005674458, -55.64135213551316, -4.343017629249005), (0.73901, 0.7558256, 0.73901), "PWM_Nordic_8x8x8_A75", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (595.41187, 1885.3997, 1475.0262), (-2.1580201650689244, -8.954438917253597, 0.6731703238166036), (0.80245066, 0.73901, 0.73901), "PWM_Nordic_8x8x8_A76", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (722.28705, 1274.6975, 1423.7179), (0.7772345015274486, 45.74748460674093, 2.2590937900245494), (0.73901, 0.73901, 0.73901), "PWM_Nordic_8x8x8_A77", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1670.9977, 1069.173, 1364.2482), (-1.5823059366573393, 106.19016236319729, 1.7899099749401781), (0.7560355, 0.73901, 0.73901), "PWM_Nordic_8x8x8_A78", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (6718.7925, 1086.8546, 1050.4325), (1.3022645488314024, 84.22710727651882, 3.9155209540268956), (0.649982, 0.649982, 0.550583), "PWM_Nordic_8x8x8_A79", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (8912.541, 3417.2747, 2548.0486), (-37.828554968347156, -92.51299190161767, -168.57441464035952), (1.045717, 1.045717, 1.045717), "PWM_Nordic_8x8x8_A8_435", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (7046.1255, 1056.0316, 1077.588), (1.3022639784735959, 84.2271072481992, 3.9155209008975964), (0.519317, 0.519317, 0.5952583), "PWM_Nordic_8x8x8_A80", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1649.5953, 1079.2783, 1931.5835), (73.9814331872859, 112.49387701128471, 6.504114348180924), (0.73901, 0.73901, 0.73901), "PWM_Nordic_8x8x8_A81", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (10848.75, 6434.55, 1091.9846), (7.8134840123507505, 178.097418327665, 1.738763339904038), (0.33405465, 0.4677252, 0.425491), "PWM_Nordic_8x8x8_A818", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1062.1836, 1116.202, 1952.956), (-2.4644465602657344, -17.77615125940848, -162.799850325118), (0.97388035, 0.73901, 0.73901), "PWM_Nordic_8x8x8_A82", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (11291.8955, 6178.1504, 1093.4484), (-23.71640082601987, 1.6598198735467282, 5.549433788697537), (0.67330647, 0.67330647, 0.67330647), "PWM_Nordic_8x8x8_A823", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (7092.605, 449.74527, 1630.8048), (4.464778286649105, -148.51857146844574, -4.75732410926848), (0.640268, 0.71505827, 0.7789029), "PWM_Nordic_8x8x8_A83_570", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (515.4586, 1816.4902, 1891.5139), (12.477943710600252, -98.23229787917367, -174.82294283312487), (0.97388, 0.73901, 0.73901), "PWM_Nordic_8x8x8_A84", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4998.863, 4347.0596, 769.7849), (0.0, 26.982967117699882, -0.0), (1.0, 1.0, 0.609134), "PWM_Nordic_8x8x8_A85", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4715.7974, 3786.6345, 677.64264), (5.141313034510171, -57.222284119370826, 177.42868085289103), (1.0, 0.8304572, 0.8113565), "PWM_Nordic_8x8x8_A86", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1204.4344, 1092.5652, 1346.2306), (-3.2709658407067677, 77.38531118362613, -2.664520126183369), (0.7750424, 0.73901, 0.73901), "PWM_Nordic_8x8x8_A87_89", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3932.621, 3276.5195, 960.6399), (6.808645011938923, -88.2232117683943, 2.180150268542415), (1.0, 1.0, 1.0), "PWM_Nordic_8x8x8_A88", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4423.422, 3104.1814, 1837.7437), (14.609410252351903, -138.1506870490081, -176.4961955293948), (0.977762, 0.578004, 0.857171), "PWM_Nordic_8x8x8_A89_58", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (8859.944, 3255.8157, 2597.1765), (-24.36102198611647, 93.51829133049758, 179.22206398443836), (1.4794041, 1.0, 0.7054411), "PWM_Nordic_8x8x8_A9_437", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4391.6973, 3188.6072, 1343.6151), (-9.017333068963426, -44.45171730568483, -175.19971923207393), (0.7983748, 0.5280218, 1.0473593), "PWM_Nordic_8x8x8_A90", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4933.2373, 3445.3733, 2199.8457), (-18.016752023779187, -20.515653965134415, -175.7555687895835), (0.977762, 0.578004, 0.857171), "PWM_Nordic_8x8x8_A91_67", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5261.0015, 3780.132, 2056.122), (-30.060268154799342, -83.41167635360321, -160.11508302693812), (0.977762, 0.72962195, 0.857171), "PWM_Nordic_8x8x8_A92", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5052.7104, 2676.256, 2271.7056), (1.9670810621007102, -110.38271642243734, -127.88911260399156), (0.977762, 0.578004, 0.857171), "PWM_Nordic_8x8x8_A93", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5295.5117, 3229.5706, 2181.6145), (-5.007203466760839, 79.10005692488288, 127.6511583165962), (0.977762, 0.578004, 0.857171), "PWM_Nordic_8x8x8_A94", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4665.6226, 11510.861, 1276.0629), (8.244865136282023, -103.6334140929364, 6.406146955768143), (0.703521, 0.703521, 0.703521), "PWM_Nordic_8x8x8_A942", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5865.992, 3751.574, 2397.098), (-70.73065587960014, 86.51490695047957, -87.50606792762031), (1.1160467, 0.86790687, 0.9954559), "PWM_Nordic_8x8x8_A95_77", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (12045.04, 10514.2295, 1319.4545), (-2.273374302729499, -97.36727721398141, 89.0403437403441), (1.4561, 1.374626, 1.199912), "PWM_Nordic_8x8x8_A957", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (11966.491, 10045.159, 2361.0693), (-58.96562721845621, -95.8113774611874, 88.13986410311009), (1.4561, 1.374626, 1.199912), "PWM_Nordic_8x8x8_A958_158", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (11959.041, 8892.064, 2460.1555), (-55.36791438490864, 85.8106122536634, 92.02187166562187), (1.5178977, 1.374626, 1.199912), "PWM_Nordic_8x8x8_A959", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5692.23, 3166.1514, 2327.0327), (-5.007110056779337, 79.09914008409838, 113.61693994792816), (0.977762, 0.578004, 0.857171), "PWM_Nordic_8x8x8_A96_300", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5999.609, 11732.0625, 1704.2343), (5.107724190779144, -148.93370238479866, -6.5572505731723965), (1.0, 1.0, 1.0), "PWM_Nordic_8x8x8_A968", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4678.841, 12335.904, 1724.2234), (4.9088358911434975, -42.73296503051399, 6.707434525345373), (1.0, 1.0, 1.0), "PWM_Nordic_8x8x8_A969", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5629.704, 1579.2803, 1746.2054), (-1.998779218376451, -19.97015312140915, 5.359970175202254), (0.640268, 0.640268, 0.640268), "PWM_Nordic_8x8x8_A97", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5447.124, 12305.194, 1630.5403), (7.970058181355614, -113.12768172343009, -2.342255205996657), (1.0, 1.0, 1.0), "PWM_Nordic_8x8x8_A970", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5382.4307, 12218.851, 2182.3406), (-42.31091380566688, -114.73572166251742, 172.59989958407874), (1.0, 1.0, 1.0), "PWM_Nordic_8x8x8_A971", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (6051.19, 11887.574, 2135.6829), (-3.1850580292485215, 124.61132106676871, 179.3223318050437), (1.0508871, 1.0, 1.0), "PWM_Nordic_8x8x8_A972", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (6138.278, 11332.6455, 2166.733), (-10.599578611117167, 156.71387585366492, 177.7098693827135), (1.0, 1.0, 1.0), "PWM_Nordic_8x8x8_A973", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5586.653, 11531.182, 2646.6824), (-66.6586657013632, -160.11980821874425, -141.67768917748566), (1.0, 1.0, 1.2271701), "PWM_Nordic_8x8x8_A974", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5111.818, 11568.722, 2622.843), (-3.049590666452409, -104.20140012795974, -5.9513851213097695), (1.0, 1.0, 0.72683114), "PWM_Nordic_8x8x8_A975", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4856.7573, 11993.978, 2395.763), (-15.118344628102072, 73.86889594808622, -173.84272169209385), (1.0, 1.0, 0.6204371), "PWM_Nordic_8x8x8_A976", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5194.025, 11906.634, 2432.0322), (-15.118344628102072, 73.86889594808622, -173.84272169209385), (1.0, 1.0, 0.620437), "PWM_Nordic_8x8x8_A977", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5097.0063, 11561.729, 2507.7288), (-0.583587667458406, 8.336425534885262, -169.26272993076736), (1.0, 1.0, 0.620437), "PWM_Nordic_8x8x8_A978", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1228.1697, 3816.2754, 2303.9849), (-16.461423387035182, -130.2070821789333, 179.38336089078373), (0.73901, 0.8972965, 0.73901), "PWM_Nordic_8x8x8_A979", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (7297.9746, 3682.9175, 648.83453), (0.0, 7.021205260507, -0.0), (0.5523614, 1.0, 0.609134), "PWM_Nordic_8x8x8_A98", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (6446.6567, 484.47974, 2306.2556), (-22.383326506784183, 112.79513402341763, -174.36839285177908), (1.0, 1.0, 1.0), "PWM_Nordic_8x8x8_A980", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5472.4624, 1063.3357, 1793.0466), (7.355805329624762, -20.140503277037116, 2.516325560870299), (0.680551, 0.75, 0.75), "PWM_Nordic_8x8x8_A981", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5657.7407, 1349.5326, 2228.8713), (-0.6652525805744445, -64.16261779729561, 179.48991285319642), (0.680551, 0.75, 0.75), "PWM_Nordic_8x8x8_A982", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5623.385, 738.65625, 2260.5063), (-14.399263522554849, 28.99166969411122, -177.4469650121342), (0.680551, 0.75, 0.75), "PWM_Nordic_8x8x8_A983", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5672.725, 500.59164, 1720.0631), (-13.859314620509581, 54.4374529367261, -3.6927796487244895), (0.680551, 0.75, 0.82905173), "PWM_Nordic_8x8x8_A984", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5922.7344, 906.2092, 2490.784), (2.9937331671651, -146.7178068206614, -4.145720555159483), (0.680551, 0.75, 0.41157115), "PWM_Nordic_8x8x8_A985", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (6280.7627, 1129.576, 2510.3955), (1.776103683566868, 49.22448574991994, -178.58116943767757), (0.680551, 0.75, 0.411571), "PWM_Nordic_8x8x8_A986", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (9423.956, 2599.862, 765.0), (0.0, 15.000119589458441, -0.0), (0.4244843, 0.4244843, 0.17460118), "PWM_Nordic_8x8x8_A988_115", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1305.0, 10085.0, 735.0), (0.0, 0.0, -0.0), (0.18810496, 0.18810496, 0.18810496), "PWM_Nordic_8x8x8_A989_181", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (6701.6455, 5076.078, 1585.4625), (2.291630354822214, 162.90077148779312, 179.1778224126598), (1.2422143, 1.0492216, 1.2914703), "PWM_Nordic_8x8x8_A99_158", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2570.0, 10715.0, 780.0), (0.0, 52.06579627944375, -0.0), (0.28874514, 0.28874514, 0.28874514), "PWM_Nordic_8x8x8_A990_23", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (12345.474, 8587.502, 1243.1327), (-0.12362875443595733, 92.259854438909, 91.78427517395541), (1.4561, 1.374626, 1.199912), "PWM_Nordic_8x8x8_A991", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (12412.297, 8892.064, 2358.8215), (-54.80480477180028, 108.9678553444665, 79.06756706858582), (1.517898, 1.374626, 1.199912), "PWM_Nordic_8x8x8_A992", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (12306.686, 10480.176, 1323.8687), (-2.323180651017348, -100.55730139031678, 89.16821319040153), (1.4561, 1.374626, 1.199912), "PWM_Nordic_8x8x8_A993", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (12355.419, 9995.954, 2370.9822), (-62.76002582667591, -117.95906482334617, 115.15160789181334), (1.4561, 1.374626, 1.199912), "PWM_Nordic_8x8x8_A994", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (8837.831, 11586.761, 1896.0225), (-14.89938270084707, -88.38274946680971, 0.26269416712768767), (0.28079218, 1.115546, 1.255665), "PWM_Nordic_8x8x8_A995", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (8348.494, 11593.743, 1913.8383), (-10.04040503177213, -28.834379922778503, -6.740570632736388), (0.58965486, 0.8831295, 1.255665), "PWM_Nordic_8x8x8_A996", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (8733.184, 11291.132, 2450.0808), (-77.35178069995541, -128.4332949383794, -147.75831366568116), (1.132797, 1.075618, 1.120756), "PWM_Nordic_8x8x8_A997", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (12444.85, 3680.75, 1601.9537), (-10.12599955788761, -93.06323089672543, -95.93856083254111), (0.792394, 1.093091, 0.981168), "PWM_Nordic_8x8x8_A999", _folder)
if a: placed += 1
else: skipped += 1

# Batch 65: StaticMesh'PWM_Nordic_8x8x8_A' (441 instances)
_mesh_path = "/Game/Unshippable/Whitebox/Rocks/Meshes/PWM_Nordic_8x8x8_A"
_materials = ['/Game/Unshippable/Whitebox/Rocks/Materials/PWM_Nordic_Blend_Tileable']
_folder = "Reconstruction/BD_BB_Chapter3_HeadwaterNexus/Meshes"
a = spawn_static_mesh(_mesh_path, _materials, (5150.789, 7155.1875, 742.2916), (8.349346005215068, 47.42504832127987, -4.452637159603554), (0.53119564, 0.5566106, 0.49895668), "PWM_Nordic_8x8x8_A1014", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (6046.2256, 7366.1577, 790.97943), (5.347331100632001, -109.95315558390135, 0.5394592112528228), (0.465501, 0.490916, 0.433262), "PWM_Nordic_8x8x8_A1015", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4441.4883, 10036.495, 735.5553), (-8.132110745129417, -16.976196796789797, 1.9793090955646018), (0.465501, 0.490916, 0.433262), "PWM_Nordic_8x8x8_A1019", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3801.1123, 10518.34, 638.16235), (3.0373711950677897, -161.94568446074925, -0.4437561757679915), (0.465501, 0.490916, 0.363311), "PWM_Nordic_8x8x8_A1020", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (6069.7017, 7077.577, 763.2485), (0.6392920436806502, 178.15514076452558, -8.72051844177274), (0.465501, 0.490916, 0.433262), "PWM_Nordic_8x8x8_A1023", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (7952.091, 6251.234, 1008.5959), (28.946338255575924, 14.276719397135398, 4.769514495814408), (0.8106206, 0.8106206, 0.6287205), "PWM_Nordic_8x8x8_A105", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (8060.672, 6257.4673, 791.3545), (4.621524046819779, 3.793730100807247, -4.929046186354423), (0.87419, 1.0, 0.6786428), "PWM_Nordic_8x8x8_A195", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (8142.2593, 6992.638, 847.0969), (4.496989706769572, 20.002531707892707, -0.8566895620526157), (0.810621, 0.62352365, 0.6974362), "PWM_Nordic_8x8x8_A228", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (8142.7007, 6474.2666, 2161.472), (-15.364899154636444, 1.9123355230691752, 177.3016207734866), (0.810621, 0.623524, 0.697436), "PWM_Nordic_8x8x8_A232", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (8704.147, 5457.153, 1038.1205), (-6.827331515217228, -178.32379130348016, 9.590086711001247), (0.810621, 0.623524, 0.697436), "PWM_Nordic_8x8x8_A529", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (9195.956, 5780.3115, 676.55884), (14.75747058849715, 47.487309780742656, 4.144540029105606), (0.5347557, 0.810621, 0.628721), "PWM_Nordic_8x8x8_A530", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (8876.882, 6500.98, 644.90625), (13.7709170556366, 27.54809522636642, 0.6224362285774818), (0.33929697, 0.6151618, 0.43326178), "PWM_Nordic_8x8x8_A531", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (8540.194, 7100.052, 637.8149), (15.671484774154619, 24.432341284100286, -5.1156008091635865), (0.339297, 0.615162, 0.41838536), "PWM_Nordic_8x8x8_A532", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (8678.889, 6813.405, 610.3796), (16.28268725844993, 33.98877295022279, -2.47946059592242), (0.339297, 0.615162, 0.418385), "PWM_Nordic_8x8x8_A533", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (8232.08, 5760.082, 1043.9219), (30.769161294299433, 60.83740201400906, -0.2949525059314403), (0.7222289, 0.63797134, 0.45607123), "PWM_Nordic_8x8x8_A534", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (8999.339, 5416.865, 2034.8138), (-0.17086794317982704, 139.0402565470618, 177.15440050627728), (0.71836597, 0.623524, 0.93756187), "PWM_Nordic_8x8x8_A535", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (8050.436, 7020.876, 1146.3235), (-5.640136472479355, 66.54467032741279, -0.8583677305718999), (0.6643597, 0.47726268, 0.55117464), "PWM_Nordic_8x8x8_A536", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (9275.018, 6034.821, 534.2196), (13.662987519599625, 32.69470037263333, 1.8433836339447232), (0.46550107, 0.49091583, 0.433262), "PWM_Nordic_8x8x8_A537", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (7904.5005, 6436.8193, 1911.5216), (-12.552064013713862, -16.805906733388333, -176.62032173935611), (0.810621, 0.623524, 0.697436), "PWM_Nordic_8x8x8_A538", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (8821.983, 6374.156, 522.2445), (-13.831296209448855, -156.49303256699352, -0.6450806789729225), (0.64841884, 0.64841884, 0.64841884), "PWM_Nordic_8x8x8_A539", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (8997.25, 6084.9224, 586.6295), (-13.329832851937935, -175.17335156176262, 3.779082878703401), (0.5005028, 0.5005028, 0.5005028), "PWM_Nordic_8x8x8_A540", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (9493.02, 5525.432, 576.0441), (-13.829527884418114, -162.0125046525613, 0.6760252401712266), (0.500503, 0.500503, 0.500503), "PWM_Nordic_8x8x8_A541", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (9463.156, 5784.008, 539.7721), (25.111689787894004, 13.522795636364506, -1.3747863699670364), (0.465501, 0.490916, 0.433262), "PWM_Nordic_8x8x8_A542", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (10414.854, 5748.6465, 682.5125), (-0.1307068660486304, -55.7895220061008, -3.260681191838352), (0.465501, 0.490916, 0.433262), "PWM_Nordic_8x8x8_A543", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (10706.037, 6215.014, 742.1606), (1.6575231839478808, -13.710206794324357, 4.362519114013862), (0.5086916, 0.53410655, 0.4764526), "PWM_Nordic_8x8x8_A544", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (10407.486, 5904.6914, 552.2395), (2.2384028571661894, -21.5577643052375, 4.095245093994424), (0.508692, 0.534107, 0.476453), "PWM_Nordic_8x8x8_A545", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (10540.453, 6272.084, 522.34564), (3.3984906776403414, -39.628109113665566, 3.199401468700065), (0.508692, 0.534107, 0.476453), "PWM_Nordic_8x8x8_A546", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (10519.898, 5957.961, 672.9823), (9.731249120612965, 145.98502271127745, -3.6056514285550674), (0.508692, 0.534107, 0.476453), "PWM_Nordic_8x8x8_A547", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (10505.313, 6345.9404, 557.61646), (22.702405469828413, 165.68371518615683, 0.8840945889306288), (0.508692, 0.534107, 0.476453), "PWM_Nordic_8x8x8_A548", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (10457.48, 7088.318, 599.1303), (-1.238220496142222, 22.412296248058215, 4.499359617321116), (0.508692, 0.534107, 0.476453), "PWM_Nordic_8x8x8_A549", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (10510.685, 6688.1577, 517.9017), (2.4663530331206416, -141.09161816712805, -3.9623714514232833), (0.508692, 0.534107, 0.476453), "PWM_Nordic_8x8x8_A550", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (10281.719, 7516.613, 641.0713), (-0.5940552701949927, 14.359620306182842, 9.978883994082695), (0.508692, 0.534107, 0.476453), "PWM_Nordic_8x8x8_A551", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (10041.783, 7691.331, 624.4833), (-3.5584411540484147, 59.30997109152751, 2.721649125099867), (0.508692, 0.534107, 0.476453), "PWM_Nordic_8x8x8_A552", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (11142.701, 6674.8027, 1146.7667), (-14.927061179638871, -0.6795349041455112, 8.36373885759409), (0.508692, 0.534107, 0.476453), "PWM_Nordic_8x8x8_A554", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (11367.521, 6761.9316, 1414.3082), (-1.9783936069622277, 168.41747598307018, 1.2490846187167968), (0.508692, 0.534107, 0.476453), "PWM_Nordic_8x8x8_A555", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (11298.2705, 5885.909, 2446.4888), (-3.3681038171639455, 165.46148931305598, -177.90746249225722), (0.508692, 0.534107, 0.476453), "PWM_Nordic_8x8x8_A556", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (11445.997, 6545.216, 1321.8363), (-17.159973211413796, -145.40777937018944, -4.320740162593666), (0.508692, 0.534107, 0.476453), "PWM_Nordic_8x8x8_A557", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (9408.918, 5266.0537, 751.4689), (-32.97235461401268, -20.138670277420818, 14.010530094764803), (0.500503, 0.500503, 0.500503), "PWM_Nordic_8x8x8_A558", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (9476.564, 5349.344, 655.4373), (-13.588225655619238, -170.46081086090626, 2.681823735054579), (0.500503, 0.500503, 0.500503), "PWM_Nordic_8x8x8_A559", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (10274.647, 5426.8467, 719.8746), (-3.025268520052779, 0.04360962917759896, 9.066102252916608), (0.465501, 0.490916, 0.433262), "PWM_Nordic_8x8x8_A560", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (10288.483, 5656.246, 510.07712), (2.088728483274962, -62.954378315496875, 4.797729690167948), (0.5798624, 0.5798624, 0.5798624), "PWM_Nordic_8x8x8_A561", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (9865.296, 7190.372, 419.3663), (17.761783176237483, 35.95324583144064, -5.643494576988266), (0.648419, 0.648419, 0.648419), "PWM_Nordic_8x8x8_A562", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (10254.996, 4884.8105, 868.1887), (-14.187319664110422, -174.17683562905555, -13.154146432054016), (0.465501, 0.490916, 0.433262), "PWM_Nordic_8x8x8_A563", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (9435.926, 4853.416, 836.5946), (-13.486174110505008, -172.519530058821, 3.1633599136406834), (0.500503, 0.500503, 0.500503), "PWM_Nordic_8x8x8_A564", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (9425.415, 4487.386, 965.2706), (-28.90047856359362, -154.1180917850464, -8.55093375883641), (0.465501, 0.490916, 0.433262), "PWM_Nordic_8x8x8_A565", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (9590.946, 4180.92, 966.2522), (15.809363112665563, 2.8900451917609646, -5.344543730493745), (0.465501, 0.490916, 0.433262), "PWM_Nordic_8x8x8_A566", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (9714.816, 3577.5452, 789.2447), (-3.2513430085041564, 146.95547300383382, 8.893463226690729), (0.465501, 0.490916, 0.433262), "PWM_Nordic_8x8x8_A567", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (9557.324, 3903.1223, 904.41815), (12.569587203108743, -20.018221866124495, -12.71957467755515), (0.465501, 0.490916, 0.433262), "PWM_Nordic_8x8x8_A568", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (9801.759, 4207.052, 865.4895), (10.714986134615975, 32.2134597378937, -0.8709108260053952), (0.465501, 0.490916, 0.433262), "PWM_Nordic_8x8x8_A569", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (10401.39, 4969.869, 980.9592), (-11.159270757305968, -9.589720416628596, 2.515747032709974), (0.465501, 0.490916, 0.433262), "PWM_Nordic_8x8x8_A570_276", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (9236.873, 3837.4583, 759.445), (25.370115149976144, -136.12380293472248, 0.909515390754838), (0.465501, 0.490916, 0.433262), "PWM_Nordic_8x8x8_A571", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (9415.484, 3675.8848, 765.93933), (58.64994763542471, 42.46124070352918, 11.29406532199248), (0.465501, 0.490916, 0.433262), "PWM_Nordic_8x8x8_A572", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (8120.5205, 3270.4524, 565.2608), (2.792863768529501, -118.07769309497907, -0.7973329133063336), (0.465501, 0.490916, 0.433262), "PWM_Nordic_8x8x8_A573", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (7977.322, 3293.136, 688.8028), (1.8579272744154487, -152.3875837909088, -2.2326049948543645), (0.465501, 0.490916, 0.433262), "PWM_Nordic_8x8x8_A574", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (8022.7837, 3676.5723, 656.9921), (0.19266594463635997, 174.46752830164363, 4.052275760536836), (0.69523984, 0.6873771, 0.433262), "PWM_Nordic_8x8x8_A575", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (7473.5176, 3445.486, 761.9655), (2.8993541230770714, -98.87186099679592, 0.16485615663915987), (0.465501, 0.490916, 0.433262), "PWM_Nordic_8x8x8_A576", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (7851.1987, 3673.9417, 786.9186), (-3.2373044040314625, -52.71321764600764, -2.122283987650901), (0.465501, 0.490916, 0.433262), "PWM_Nordic_8x8x8_A577", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (7688.2856, 3552.6084, 767.8446), (-10.457825277071754, -52.86331237946437, -10.427703862369887), (0.465501, 0.490916, 0.433262), "PWM_Nordic_8x8x8_A578", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (7930.247, 3507.649, 696.5278), (-3.794311449441647, -74.64777244090924, -5.317870674148279), (0.465501, 0.490916, 0.433262), "PWM_Nordic_8x8x8_A579", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (8056.5693, 4049.127, 796.54175), (-2.336181542844145, -173.1521283486843, 5.969389895929828), (0.465501, 0.490916, 0.433262), "PWM_Nordic_8x8x8_A580", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (8573.557, 4133.489, 730.94214), (2.927589174432834, -74.36757505764055, 0.9688414910362299), (0.465501, 0.490916, 0.433262), "PWM_Nordic_8x8x8_A581", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (9075.2705, 4232.972, 1012.1261), (5.576563366590074, -126.81055855614326, 6.499053483607719), (0.465501, 0.490916, 0.433262), "PWM_Nordic_8x8x8_A582", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (7445.8296, 3666.571, 996.8833), (22.091679012029214, -52.24689232986619, 5.212249171509411), (0.465501, 0.490916, 0.433262), "PWM_Nordic_8x8x8_A583", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (8987.367, 4699.8823, 1288.8516), (3.27383935926637, 112.84959194148087, -0.11517342585719714), (0.465501, 0.490916, 0.433262), "PWM_Nordic_8x8x8_A584_326", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (9064.473, 4623.0796, 1087.5221), (-16.08694565266885, 112.88741037254302, -0.11956786528174862), (0.465501, 0.490916, 0.44927675), "PWM_Nordic_8x8x8_A585", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (8976.287, 4669.2793, 1597.5676), (-4.275969756310988, -67.53721319600882, -179.85621098652672), (0.57130885, 0.59672385, 0.53906983), "PWM_Nordic_8x8x8_A586", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (9385.141, 4317.9844, 1037.3928), (1.8940797384159194, 47.95278263149696, -4.965576136041883), (0.465501, 0.490916, 0.433262), "PWM_Nordic_8x8x8_A587", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (11636.803, 3469.7805, 668.8077), (-2.9473569137935995, -75.67592894090753, -0.3601684824389777), (0.465501, 0.490916, 0.433262), "PWM_Nordic_8x8x8_A588", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (11043.551, 3701.8335, 933.6917), (-2.7122501894194193, -58.61347544976935, -1.2087707466024882), (0.465501, 0.490916, 0.433262), "PWM_Nordic_8x8x8_A589_408", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (11051.647, 3691.3962, 865.32733), (-24.39822516437318, -58.1217723672317, -1.3258974931859961), (0.465501, 0.490916, 0.433262), "PWM_Nordic_8x8x8_A590", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (10925.167, 3787.5159, 995.1399), (-9.439147857570271, -99.10534518850031, 0.8466492606863112), (0.465501, 0.490916, 0.433262), "PWM_Nordic_8x8x8_A591", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (11133.706, 5286.9277, 1068.265), (0.6844191097893297, -21.143736096097676, -4.5976253904682025), (0.508692, 0.534107, 0.476453), "PWM_Nordic_8x8x8_A592", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (11143.917, 5041.201, 1179.9291), (-13.757995570476604, -167.57463286284192, -3.644103961403838), (0.465501, 0.490916, 0.433262), "PWM_Nordic_8x8x8_A593", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (11105.732, 4797.3096, 1177.2762), (2.2823146036690223, 177.47507744319918, 2.043243276297286), (0.465501, 0.490916, 0.433262), "PWM_Nordic_8x8x8_A594", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (11488.213, 4161.788, 1266.858), (-18.83712830925047, -120.4026194565848, -1.6643687813617438), (0.465501, 0.490916, 0.433262), "PWM_Nordic_8x8x8_A595", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (11085.897, 4573.7173, 1171.4944), (-3.336486737243022, 165.9785500100372, 5.538848454766334), (0.465501, 0.490916, 0.433262), "PWM_Nordic_8x8x8_A596", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (11195.009, 4548.383, 1203.2762), (-33.22570300050271, 162.6652839934101, 16.211239885583208), (0.465501, 0.40414745, 0.6341051), "PWM_Nordic_8x8x8_A597", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (10720.93, 3825.7517, 1024.9818), (4.174659680017811, -114.46801193449427, -4.994781223354087), (0.465501, 0.490916, 0.2938082), "PWM_Nordic_8x8x8_A598", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (10675.651, 3430.8733, 754.8611), (-2.9230342427746105, -92.67292927579314, 0.5168760815165759), (0.465501, 0.490916, 0.433262), "PWM_Nordic_8x8x8_A599", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (10750.751, 1801.2488, 771.3154), (-3.028991427102425, -136.00896363508014, -14.058104806161369), (0.465501, 0.490916, 0.433262), "PWM_Nordic_8x8x8_A600", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (10755.119, 2057.9338, 721.8031), (-13.56826629623015, 141.46897689382712, 2.7177419146323714), (0.465501, 0.490916, 0.433262), "PWM_Nordic_8x8x8_A601", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (11112.254, 2338.9712, 768.5801), (11.258840991249409, -63.14897772994914, -8.092589270907427), (0.465501, 0.490916, 0.433262), "PWM_Nordic_8x8x8_A602", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (10836.613, 1389.1401, 742.5559), (-3.0289300362492466, -136.00895969953112, -3.8655393004527303), (0.465501, 0.490916, 0.433262), "PWM_Nordic_8x8x8_A603", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (10758.803, 1674.9619, 747.5702), (-4.811217552432253, -176.47858518082862, -0.9779662251619133), (0.465501, 0.490916, 0.433262), "PWM_Nordic_8x8x8_A604", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (10990.141, 1737.9752, 926.98364), (-19.76794507335139, 124.63205286863582, 6.512176043767429), (0.465501, 0.490916, 0.433262), "PWM_Nordic_8x8x8_A605", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (11366.579, 2185.0076, 988.4795), (-3.818176072685811, 19.1940258804038, -3.6613163221170524), (0.465501, 0.490916, 0.433262), "PWM_Nordic_8x8x8_A606", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (11208.639, 2276.7927, 868.2514), (10.850922579040569, -124.27119729175853, -9.409483673542905), (0.465501, 0.490916, 0.433262), "PWM_Nordic_8x8x8_A607", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (11272.533, 1752.7047, 1064.7445), (11.258841519468449, -63.14897406390034, -6.416105858734884), (0.465501, 0.490916, 0.433262), "PWM_Nordic_8x8x8_A608", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (11241.725, 1609.0643, 1129.8226), (-5.675567869574546, 9.957519388978332, -0.5890197911242376), (0.465501, 0.490916, 0.433262), "PWM_Nordic_8x8x8_A609", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (11489.388, 2151.4758, 1243.7891), (-5.701110589576469, 6.380798492580171, -0.23443601924427077), (0.465501, 0.490916, 0.433262), "PWM_Nordic_8x8x8_A610", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (11157.203, 1022.63654, 757.004), (-3.028839221992543, -136.00898844134883, -2.304382200527187), (0.465501, 0.490916, 0.433262), "PWM_Nordic_8x8x8_A611", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (10919.787, 1171.8589, 675.77966), (-3.028808666131273, -136.00901631303475, 2.550232398555799), (0.465501, 0.490916, 0.433262), "PWM_Nordic_8x8x8_A612", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (11260.637, 353.7059, 747.2016), (-3.013183969500751, 149.01932470293386, 2.3247682254142283), (0.465501, 0.490916, 0.433262), "PWM_Nordic_8x8x8_A613", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (11358.742, 739.9064, 846.5231), (12.028823247519037, -162.72497517086677, -0.7250673092184667), (0.465501, 0.490916, 0.433262), "PWM_Nordic_8x8x8_A614", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (11199.801, 1096.1937, 841.10345), (-2.4641720516479233, -123.62389658797439, -2.9001159698025893), (0.465501, 0.490916, 0.433262), "PWM_Nordic_8x8x8_A615", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (11236.575, 659.7065, 734.7195), (48.620667016573336, -167.12841663910908, 3.0586234331793585), (0.465501, 0.490916, 0.433262), "PWM_Nordic_8x8x8_A616", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (7848.0464, 600.3586, 657.6261), (1.8579271703817832, -152.38755513502045, 5.353576170020121), (0.465501, 0.490916, 0.433262), "PWM_Nordic_8x8x8_A617", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (7632.053, 337.9248, 920.7767), (-0.3256225335869604, -130.0181715371284, 5.656707037895121), (0.465501, 0.490916, 0.433262), "PWM_Nordic_8x8x8_A618", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (7247.151, 683.91693, 1080.207), (6.125354025242782, 143.8894768245257, -6.720580896650209), (0.465501, 0.490916, 0.433262), "PWM_Nordic_8x8x8_A619", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (7444.8247, 532.5123, 949.5038), (-2.529846410842146, -149.20815614655248, 3.0121463216733417), (0.465501, 0.490916, 0.433262), "PWM_Nordic_8x8x8_A620", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (7577.509, 1110.008, 672.65515), (1.8579267822246297, -152.38755515102085, 5.353576310176611), (0.465501, 0.490916, 0.433262), "PWM_Nordic_8x8x8_A621", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (7839.4707, 955.51355, 645.5009), (6.374690670337428, 68.38621103160315, -5.278320029788333), (0.465501, 0.490916, 0.433262), "PWM_Nordic_8x8x8_A622", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (7756.3057, 593.92456, 829.2855), (0.5210136675304036, 63.60855688737457, -2.3957217057793794), (0.465501, 0.490916, 0.433262), "PWM_Nordic_8x8x8_A624", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (7845.4136, 380.31287, 792.9018), (9.21498180948721, -24.49941864274747, 0.6140135489778739), (0.465501, 0.490916, 0.433262), "PWM_Nordic_8x8x8_A625", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (7363.0786, 1426.092, 665.6639), (-6.750701213899601, -153.19715522239918, 5.388243498991646), (0.465501, 0.490916, 0.433262), "PWM_Nordic_8x8x8_A626", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (7266.1216, 1113.0502, 802.08057), (3.1707261790628056, -167.2461002076667, 4.698028553121563), (0.465501, 0.490916, 0.433262), "PWM_Nordic_8x8x8_A627", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (7215.5933, 959.0391, 948.3386), (-6.135985309500214, -168.0104543429176, 4.717956176103029), (0.465501, 0.490916, 0.433262), "PWM_Nordic_8x8x8_A628", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (7328.2246, 3215.5728, 667.2342), (-1.3203427280815447, 140.8408015334028, -2.5868524711238408), (0.465501, 0.490916, 0.433262), "PWM_Nordic_8x8x8_A629", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (7122.766, 3315.8591, 620.3845), (0.4376511216591122, -171.58577426312974, -4.798919122400815), (0.465501, 0.490916, 0.433262), "PWM_Nordic_8x8x8_A630", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (6822.8657, 3941.7605, 697.07446), (-0.9100646426645684, 172.35466531332582, -4.7322388182828865), (0.465501, 0.490916, 0.433262), "PWM_Nordic_8x8x8_A631", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (7179.9746, 3526.055, 765.2427), (26.779655605583233, -156.0766480389186, -11.294554083263922), (0.465501, 0.490916, 0.433262), "PWM_Nordic_8x8x8_A632", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (6868.5034, 3834.0815, 617.0123), (6.122785692282665, 74.97377453014963, 1.5332636622521807), (0.465501, 0.490916, 0.433262), "PWM_Nordic_8x8x8_A633", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (6209.8457, 4543.317, 749.99695), (4.197472258565407, 12.459808788786507, -4.717070819876055), (0.465501, 0.490916, 0.433262), "PWM_Nordic_8x8x8_A634", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (6271.985, 4375.207, 640.9833), (5.392235844922232, 92.29207887662176, 3.283904926677227), (0.465501, 0.490916, 0.433262), "PWM_Nordic_8x8x8_A635", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (6418.2764, 4363.5654, 667.15015), (6.268932978039291, 67.51830701755212, 0.7275387937824104), (0.465501, 0.490916, 0.433262), "PWM_Nordic_8x8x8_A636", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (6247.257, 4652.664, 947.0957), (-1.4304197871972277, -68.74796551910855, 3.5010374682030423), (0.465501, 0.490916, 0.433262), "PWM_Nordic_8x8x8_A637", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (6941.482, 4003.3662, 934.87885), (3.768857125961801, -176.21216188110688, 5.054687732692928), (0.465501, 0.490916, 0.433262), "PWM_Nordic_8x8x8_A638", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (7323.393, 1938.0763, 575.86896), (17.210632365652927, 42.466470940706195, -5.923430926433759), (0.465501, 0.490916, 0.433262), "PWM_Nordic_8x8x8_A639_532", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (6029.2144, 4369.364, 606.9967), (6.224112077318304, 70.44156596436918, 1.0456242315871607), (0.465501, 0.490916, 0.433262), "PWM_Nordic_8x8x8_A640", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5428.788, 4216.467, 646.5244), (3.492143005503437, 10.313722030623806, -9.425629592514698), (0.465501, 0.490916, 0.433262), "PWM_Nordic_8x8x8_A641", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (6663.2036, 4139.888, 658.71747), (-6.177551388295027, -130.94571836605846, 1.2913821881077785), (0.465501, 0.490916, 0.433262), "PWM_Nordic_8x8x8_A642", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (6365.3384, 4559.2764, 759.90704), (3.49766287139447, 117.33471379388821, 5.2565912213216475), (0.465501, 0.490916, 0.433262), "PWM_Nordic_8x8x8_A643", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5243.984, 3990.1682, 777.19507), (1.2776208218250698, -18.451476331890152, -4.925017945568729), (0.465501, 0.490916, 0.433262), "PWM_Nordic_8x8x8_A644", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5160.375, 3428.0386, 638.46075), (6.624444290898593, -161.19189795286616, 3.2010198296931973), (0.465501, 0.490916, 0.433262), "PWM_Nordic_8x8x8_A645", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4916.468, 3764.502, 913.25446), (0.4358503264416979, -53.01953071715579, -1.789856038562019), (0.465501, 0.490916, 0.433262), "PWM_Nordic_8x8x8_A646", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4508.693, 3192.7864, 867.83746), (8.385256656265588, -19.068997103481614, -4.977202225971067), (0.465501, 0.490916, 0.433262), "PWM_Nordic_8x8x8_A647", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4480.112, 3269.3, 996.9104), (6.752695471360591, -177.96063712197486, 3.145233576449785), (0.465501, 0.490916, 0.433262), "PWM_Nordic_8x8x8_A648_506", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4637.389, 3055.6003, 685.4376), (-2.689545117866438, -46.45397875953861, 5.545562802281376), (0.465501, 0.490916, 0.433262), "PWM_Nordic_8x8x8_A649", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4847.5396, 3251.3103, 610.73505), (3.8095248153142105, 114.00256295414286, -6.295439903588509), (0.5353075, 0.5685977, 0.433262), "PWM_Nordic_8x8x8_A650", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4547.862, 3255.8364, 866.29816), (3.6703109807382623, -170.7116714265711, 2.470092786991498), (0.465501, 0.490916, 0.433262), "PWM_Nordic_8x8x8_A651", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4594.571, 3119.5168, 797.79266), (6.482723012658656, 127.38098023884879, -3.671325750515228), (0.465501, 0.490916, 0.433262), "PWM_Nordic_8x8x8_A652_521", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5226.099, 1932.7462, 1555.378), (8.142233934591792, 54.7196678471749, 1.5757751221664402), (0.465501, 0.490916, 0.433262), "PWM_Nordic_8x8x8_A653", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5446.9243, 1857.3856, 1566.0424), (17.360666179743514, 71.7928683272826, 3.691925122680879), (0.465501, 0.490916, 0.433262), "PWM_Nordic_8x8x8_A654", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (6103.8423, 2411.677, 621.0671), (10.811103152965138, 96.56553211619757, 8.414827186732257), (0.465501, 0.490916, 0.433262), "PWM_Nordic_8x8x8_A655", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (6187.4873, 2170.8904, 792.0343), (9.483463482080957, 61.14376328864504, 0.343963800174518), (0.5827307, 0.490916, 0.433262), "PWM_Nordic_8x8x8_A656", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (6649.8813, 2209.9966, 627.44), (13.128767987217076, 101.64964788427136, 8.870573855876012), (0.465501, 0.490916, 0.433262), "PWM_Nordic_8x8x8_A657", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (6355.6094, 2187.1907, 688.83466), (-9.80865537634942, -125.18340821657381, 1.981628098884882), (0.465501, 0.490916, 0.433262), "PWM_Nordic_8x8x8_A658", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (6006.1323, 2141.9387, 868.73627), (-3.9007873473539103, -157.57452702105363, 2.177734208186862), (0.465501, 0.490916, 0.433262), "PWM_Nordic_8x8x8_A659", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5956.3867, 2135.6504, 1068.8208), (4.412553411366773, 81.65230485863496, 0.08361791948416597), (0.465501, 0.490916, 0.433262), "PWM_Nordic_8x8x8_A660", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (6556.6895, 1851.6229, 982.49835), (11.891802751061354, 80.35488471553994, 2.9899595347963577), (0.465501, 0.490916, 0.433262), "PWM_Nordic_8x8x8_A661", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (6868.7407, 2092.8428, 625.51794), (-1.8255308652311983, 10.577812334103426, -3.647796302225003), (0.465501, 0.490916, 0.433262), "PWM_Nordic_8x8x8_A662", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (7210.2705, 1216.2509, 826.77106), (-0.08755495321138591, 114.56382997808558, 2.359039165673032), (0.465501, 0.490916, 0.433262), "PWM_Nordic_8x8x8_A663", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (7102.046, 870.1952, 1236.1177), (3.2027574869526463, 101.21343708011322, 1.490844688850346), (0.465501, 0.490916, 0.433262), "PWM_Nordic_8x8x8_A664", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (6158.908, 1576.7444, 1249.7678), (12.563954361247204, 8.35888594440871, -0.39306651212812194), (0.465501, 0.490916, 0.433262), "PWM_Nordic_8x8x8_A665", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (6242.175, 1382.1766, 1306.7496), (1.6919674977307755, 28.64123205742294, 0.21374505578347408), (0.39937574, 0.490916, 0.433262), "PWM_Nordic_8x8x8_A666", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (6799.1304, 830.1377, 1298.0942), (0.9918536910255087, 75.88329363219563, 5.394165333474121), (0.465501, 0.490916, 0.433262), "PWM_Nordic_8x8x8_A667", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (6580.9307, 996.78973, 1275.7544), (6.061860671839043, 52.174925117649614, 0.6721188373091275), (0.39119595, 0.490916, 0.39287362), "PWM_Nordic_8x8x8_A668", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (6657.079, 887.0901, 1297.2269), (3.926106342683201, -128.25855839488153, -3.562561356894707), (0.465501, 0.490916, 0.392874), "PWM_Nordic_8x8x8_A669", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (8285.106, 1429.6959, 590.032), (-0.15591458640232986, -119.28738140639933, -9.234007090423864), (0.465501, 0.490916, 0.433262), "PWM_Nordic_8x8x8_A670", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (8157.205, 1412.3834, 563.03577), (-6.433349303215749, 105.57892234678813, 6.63947272079432), (0.465501, 0.490916, 0.433262), "PWM_Nordic_8x8x8_A671", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (6073.0435, 1542.9718, 2515.0603), (-4.475891050270271, 25.533874524770393, -179.6986039233559), (0.465501, 0.490916, 0.5634593), "PWM_Nordic_8x8x8_A672", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5803.2964, 1657.7793, 2290.4187), (10.685030014050563, -114.88421121974929, -179.49554139968487), (0.5249806, 0.5503956, 0.6528983), "PWM_Nordic_8x8x8_A673", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (6905.0854, 878.26733, 2367.1614), (-9.109346270987125, 66.3413019499605, 177.84729861528314), (0.465501, 0.490916, 0.563459), "PWM_Nordic_8x8x8_A674", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (6716.441, 1143.071, 2615.7285), (-28.680996488635596, 64.72837326899777, 171.9398234737348), (0.465501, 0.490916, 0.563459), "PWM_Nordic_8x8x8_A675", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (6398.2603, 1423.1702, 2617.267), (-39.19223297452646, 42.462010646482305, -172.421028178327), (0.465501, 0.490916, 0.563459), "PWM_Nordic_8x8x8_A676", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5817.1143, 1809.5964, 1425.5781), (4.287192959062252, 70.95409942501237, 2.2448117925644855), (0.465501, 0.490916, 0.433262), "PWM_Nordic_8x8x8_A677", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5113.12, 2386.3467, 706.29785), (13.726754119611163, 117.82091724523856, 3.7927539916972077), (0.465501, 0.490916, 0.433262), "PWM_Nordic_8x8x8_A678", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5369.4014, 2643.6687, 593.87195), (12.932619758156827, 127.33327775210444, 5.991667703219403), (0.465501, 0.490916, 0.433262), "PWM_Nordic_8x8x8_A679", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4532.5186, 2296.3967, 602.6761), (13.736841446526983, 93.7845863802345, 0.9723513295333491), (0.465501, 0.490916, 0.433262), "PWM_Nordic_8x8x8_A680", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4224.7354, 2244.9177, 584.7406), (-14.106537532929627, -89.05699489017637, -0.31451364710366414), (0.465501, 0.490916, 0.433262), "PWM_Nordic_8x8x8_A681", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4908.8145, 2249.145, 674.52026), (-12.567777570130787, -69.26036323577873, -5.032531946698671), (0.465501, 0.490916, 0.4890565), "PWM_Nordic_8x8x8_A682", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5229.56, 2469.6501, 583.02686), (-11.286042936383945, -57.37173314610131, -7.498229932105564), (0.465501, 0.490916, 0.433262), "PWM_Nordic_8x8x8_A683", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4049.556, 2087.6475, 720.8663), (9.299779242815093, 137.55436680965346, 5.005797754407924), (0.465501, 0.490916, 0.433262), "PWM_Nordic_8x8x8_A684", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3973.8113, 2081.4797, 680.9601), (-10.543425850497304, -68.72978622378417, -0.3980106594568126), (0.465501, 0.490916, 0.433262), "PWM_Nordic_8x8x8_A685", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3605.084, 1455.233, 687.02655), (-4.556579564464473, -8.501067149874514, 0.21258546162530223), (0.465501, 0.490916, 0.433262), "PWM_Nordic_8x8x8_A686", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4114.1045, 1891.0526, 921.8163), (-3.157500905777446, -93.25312196163345, 3.869780985094287), (0.465501, 0.490916, 0.433262), "PWM_Nordic_8x8x8_A687", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4372.5454, 2079.5063, 810.6016), (-17.033538788959316, -91.66835780697167, 3.295836261537257), (0.465501, 0.490916, 0.433262), "PWM_Nordic_8x8x8_A688", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3600.0488, 1128.9148, 752.2777), (11.34769096389451, -156.72515456423224, 4.609374873302604), (0.465501, 0.490916, 0.433262), "PWM_Nordic_8x8x8_A689", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3910.8364, 1492.7859, 803.70667), (15.367358827880484, 142.11743680643687, -7.683532522249635), (0.465501, 0.490916, 0.433262), "PWM_Nordic_8x8x8_A690", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3807.3076, 1383.6647, 816.27264), (14.608391941005571, 131.36675808066528, -5.561705909727484), (0.465501, 0.490916, 0.433262), "PWM_Nordic_8x8x8_A691", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4076.2842, 1750.2314, 946.66473), (14.384786734083972, 175.8433829336123, 6.126586800665126), (0.465501, 0.490916, 0.433262), "PWM_Nordic_8x8x8_A692", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3728.8645, 784.2698, 765.31757), (-4.479553224553823, 5.061676202008436, -2.902008461856364), (0.465501, 0.490916, 0.433262), "PWM_Nordic_8x8x8_A693", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3573.4958, 1103.1149, 667.4215), (-6.131378045455351, 5.086700835877089, -0.8629455799689846), (0.465501, 0.490916, 0.433262), "PWM_Nordic_8x8x8_A694", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3714.6472, 285.28433, 807.8307), (9.297033720439734, 143.6339625746226, -2.054626201030171), (0.465501, 0.490916, 0.433262), "PWM_Nordic_8x8x8_A695", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3613.022, 415.98825, 705.5429), (7.634190156567802, -177.55220826802406, 0.34387200958197706), (0.465501, 0.490916, 0.433262), "PWM_Nordic_8x8x8_A696", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3855.9966, 798.8335, 849.3157), (-4.177795139779491, -22.253538288060533, -0.5262755579129628), (0.465501, 0.490916, 0.433262), "PWM_Nordic_8x8x8_A697", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3807.5647, 1165.1606, 865.67755), (-4.203491370148706, -26.083405002240227, -0.2462463103494004), (0.465501, 0.490916, 0.433262), "PWM_Nordic_8x8x8_A698", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3866.4358, 1092.3898, 890.2681), (3.9550440031065666, 130.4642408503771, -1.4455566787818255), (0.465501, 0.490916, 0.433262), "PWM_Nordic_8x8x8_A699", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3752.2534, 1928.4354, 675.642), (-13.276579864589534, -13.126831327227523, 1.2748411916361817), (0.465501, 0.490916, 0.433262), "PWM_Nordic_8x8x8_A701", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2414.662, 1501.1367, 740.7563), (-4.638640897446659, -166.67346524290514, -4.273223351877395), (0.465501, 0.490916, 0.433262), "PWM_Nordic_8x8x8_A702", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2370.3765, 1780.79, 669.39545), (-3.81890861319463, -156.58606747299325, -5.019043043434475), (0.465501, 0.490916, 0.433262), "PWM_Nordic_8x8x8_A703", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2257.272, 2036.2081, 682.69226), (15.647003058815352, 45.499445901644236, 1.3739316735391527), (0.465501, 0.490916, 0.433262), "PWM_Nordic_8x8x8_A704", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2282.112, 1421.9523, 991.0405), (0.45909210292814323, -91.05273987022898, -5.9096067542105475), (0.465501, 0.490916, 0.433262), "PWM_Nordic_8x8x8_A705", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2516.1033, 1634.6696, 646.4987), (-2.534606639611829, -143.03386489370604, -5.773680961070338), (0.465501, 0.490916, 0.433262), "PWM_Nordic_8x8x8_A706", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2585.02, 1433.7096, 702.95306), (-6.303496799137024, 150.5126988673418, 0.008300721002787018), (0.465501, 0.490916, 0.433262), "PWM_Nordic_8x8x8_A707", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1731.9487, 2434.5051, 654.0858), (10.531187093972763, 89.03076846018041, 11.718475355890282), (0.465501, 0.490916, 0.433262), "PWM_Nordic_8x8x8_A708", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1971.8639, 2274.1953, 681.3199), (-15.031829418627224, -122.33092928359541, -4.60543865323852), (0.465501, 0.490916, 0.433262), "PWM_Nordic_8x8x8_A709", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2762.1418, 3118.201, 756.41364), (5.78515655747491, -52.89950428226931, -2.5081784179493534), (0.465501, 0.490916, 0.433262), "PWM_Nordic_8x8x8_A710", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2958.5525, 3068.7944, 710.673), (5.97155295693541, -91.49647617611821, 7.900574349894317), (0.465501, 0.490916, 0.433262), "PWM_Nordic_8x8x8_A711", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3294.2317, 2971.2937, 668.948), (-9.81777969188351, 42.45421926024265, -1.2154850552666172), (0.465501, 0.490916, 0.433262), "PWM_Nordic_8x8x8_A712", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1192.8595, 3305.695, 728.4646), (2.190073206846329, 161.2662974705848, -15.473508824983544), (0.465501, 0.490916, 0.433262), "PWM_Nordic_8x8x8_A713", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (915.1118, 3342.8972, 712.06366), (-27.40380741316125, 74.3585742128164, 1.27533768806478), (0.465501, 0.490916, 0.433262), "PWM_Nordic_8x8x8_A714", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (595.7609, 3430.214, 747.352), (27.449119976888817, -106.9912181990807, 0.8760970553874937), (0.465501, 0.490916, 0.433262), "PWM_Nordic_8x8x8_A715", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (239.06693, 3428.301, 679.21783), (21.004663221271933, -91.96709869533126, 0.0006724601278770241), (0.465501, 0.490916, 0.433262), "PWM_Nordic_8x8x8_A716", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1366.5223, 3166.1072, 791.8221), (19.07954426288304, -82.55547677011712, 7.928527484465822), (0.465501, 0.490916, 0.433262), "PWM_Nordic_8x8x8_A717", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2309.141, 3221.6755, 873.3032), (10.167446232598339, -127.13593252067233, -0.2583007081808448), (0.465501, 0.490916, 0.433262), "PWM_Nordic_8x8x8_A718_705", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1141.0375, 3442.2908, 935.19165), (-7.878875911733084, 51.18676363129066, -2.4797666265681215), (0.465501, 0.490916, 0.433262), "PWM_Nordic_8x8x8_A719", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1750.8168, 3614.1338, 1148.173), (4.350329484412024, -173.30346983164893, 1.8255305984788437), (0.465501, 0.490916, 0.433262), "PWM_Nordic_8x8x8_A720", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (761.15125, 3648.3342, 1227.4205), (-0.4226988719235982, 68.775400692877, -4.698242588842487), (0.465501, 0.490916, 0.433262), "PWM_Nordic_8x8x8_A721", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3873.311, 3019.9304, 602.6577), (-14.445373774517472, 86.06091152576825, -0.6680301532397795), (0.465501, 0.490916, 0.433262), "PWM_Nordic_8x8x8_A722", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3529.2915, 2971.9258, 652.2482), (-13.536833673372804, 104.38164572129715, -5.133452584908183), (0.465501, 0.490916, 0.433262), "PWM_Nordic_8x8x8_A723", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4212.2085, 2961.0815, 585.78406), (-14.311522594353649, 74.97857613291097, 2.0920404038755582), (0.465501, 0.490916, 0.433262), "PWM_Nordic_8x8x8_A724", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4415.465, 3013.207, 570.55365), (-11.865450000859033, 47.945193585768344, 8.325316564880294), (0.465501, 0.490916, 0.433262), "PWM_Nordic_8x8x8_A725", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5375.1934, 4600.078, 735.4191), (11.020016111943407, 32.95403570256824, 1.1348571351879646), (0.465501, 0.490916, 0.433262), "PWM_Nordic_8x8x8_A726", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (6077.5605, 4635.5137, 762.63007), (4.827072642455077, 20.666930695119458, -4.070160228687517), (0.465501, 0.490916, 0.433262), "PWM_Nordic_8x8x8_A727", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5359.015, 4748.161, 739.0215), (4.827071885947637, 20.66692997036121, -1.7095946926172974), (0.465501, 0.490916, 0.433262), "PWM_Nordic_8x8x8_A728", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5239.1763, 5128.1265, 777.00525), (5.057303082380548, 31.184324159374675, -0.8009947957370831), (0.465501, 0.490916, 0.433262), "PWM_Nordic_8x8x8_A729", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5090.346, 5424.3784, 876.51917), (14.314883023507775, 11.082091889594636, -2.525909445244342), (0.465501, 0.490916, 0.433262), "PWM_Nordic_8x8x8_A730", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5075.1055, 6012.576, 920.9972), (12.843199949870318, -7.210082275052459, -6.855956642658593), (0.465501, 0.490916, 0.433262), "PWM_Nordic_8x8x8_A731", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5119.047, 5816.5776, 793.3531), (5.072104477957384, 7.2641908640695085, -1.494506866775759), (0.465501, 0.490916, 0.433262), "PWM_Nordic_8x8x8_A732", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (6003.371, 4961.411, 822.49695), (0.5157817134256086, 3.5949408126608784, -5.302429273669748), (0.465501, 0.490916, 0.433262), "PWM_Nordic_8x8x8_A733", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (6098.6724, 5458.27, 869.1035), (3.505689935065747, 136.98266161539698, 4.013794241195089), (0.465501, 0.490916, 0.433262), "PWM_Nordic_8x8x8_A734", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5932.2603, 5260.3374, 782.5362), (7.808025636640077, 159.97862787913618, 2.66262863944989), (0.465501, 0.490916, 0.433262), "PWM_Nordic_8x8x8_A735", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (6015.2026, 5224.4404, 885.85016), (7.808025636640077, 159.97862787913618, 2.66262863944989), (0.465501, 0.490916, 0.433262), "PWM_Nordic_8x8x8_A736", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (6215.3267, 5683.828, 909.7884), (0.8834986042804077, 168.5325169803572, 5.2538150749370045), (0.465501, 0.490916, 0.433262), "PWM_Nordic_8x8x8_A737", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (6209.3525, 6889.298, 946.4579), (0.8130603638207552, 169.2974898288568, 5.265136472668372), (0.465501, 0.490916, 0.433262), "PWM_Nordic_8x8x8_A738", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (6254.282, 6578.856, 872.0294), (0.39180039999280636, 2.2563170245531716, -7.312317342171154), (0.465501, 0.490916, 0.433262), "PWM_Nordic_8x8x8_A739", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (6099.0, 5822.3193, 791.2927), (2.7734114496512774, -174.7279035569582, -4.605589929756228), (0.465501, 0.490916, 0.433262), "PWM_Nordic_8x8x8_A740", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (6208.676, 6111.567, 849.7301), (24.101896595858012, 172.99304393321907, 2.6686399268074537), (0.465501, 0.490916, 0.433262), "PWM_Nordic_8x8x8_A741", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (6124.206, 6101.9155, 767.0309), (0.6392918766450771, 161.09007579149278, -8.720518907471218), (0.465501, 0.490916, 0.433262), "PWM_Nordic_8x8x8_A742", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (6145.8916, 6430.804, 795.8907), (6.368044050968934, -169.0543831022392, -1.9231261711735879), (0.465501, 0.490916, 0.433262), "PWM_Nordic_8x8x8_A743", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (6388.998, 5510.472, 1089.6956), (-3.0610655560883906, 119.63768068497097, 5.7484432443910745), (0.465501, 0.490916, 0.433262), "PWM_Nordic_8x8x8_A744", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (6350.6772, 6759.1387, 1121.8053), (6.500411693918831, -108.94151612834716, -6.163298290458175), (0.465501, 0.490916, 0.433262), "PWM_Nordic_8x8x8_A745", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (6652.6133, 5706.9526, 1298.5608), (4.849563549999545, -40.2764272661414, -4.348480269583422), (0.465501, 0.490916, 0.433262), "PWM_Nordic_8x8x8_A746", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (6640.0083, 6556.8604, 1200.7085), (5.243761788879366, -139.4194346101573, -4.148559742181637), (0.465501, 0.490916, 0.433262), "PWM_Nordic_8x8x8_A747", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (6608.52, 6431.9287, 1078.5322), (3.9200977960755217, -155.1907362478779, -5.416472645321932), (0.465501, 0.490916, 0.433262), "PWM_Nordic_8x8x8_A748", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (6286.9907, 6508.9165, 980.4092), (3.9200975174925077, -155.19073748357874, 1.5400390971642721), (0.465501, 0.490916, 0.40003031), "PWM_Nordic_8x8x8_A749", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (6315.758, 5699.9106, 964.16724), (2.806497077563474, 154.07506335099973, -2.0897823492864593), (0.465501, 0.490916, 0.44592172), "PWM_Nordic_8x8x8_A750", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (6302.4385, 5932.191, 2329.9482), (11.989794647048031, -7.925414664522107, -179.30539958031892), (0.465501, 0.490916, 0.433262), "PWM_Nordic_8x8x8_A751", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (6308.0317, 6332.6797, 2314.4658), (11.199514079588079, 10.184265470161483, -171.985856737072), (0.465501, 0.490916, 0.433262), "PWM_Nordic_8x8x8_A752", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (6334.465, 6752.8784, 2072.222), (-11.246456051259184, 162.17723836412986, -179.89038229343774), (0.465501, 0.490916, 0.433262), "PWM_Nordic_8x8x8_A753", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (6074.5005, 6971.8716, 2104.6387), (-11.246456051259184, 162.17723836412986, -179.89038229343774), (0.465501, 0.490916, 0.433262), "PWM_Nordic_8x8x8_A754", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (6338.067, 5500.3604, 1966.1124), (3.6195208011803106, 144.18297581001877, -175.77529424932), (0.465501, 0.490916, 0.433262), "PWM_Nordic_8x8x8_A755_775", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (6309.1064, 5653.4844, 2183.8438), (-10.192108890037808, 159.51599801968553, -167.53523684826902), (0.465501, 0.490916, 0.433262), "PWM_Nordic_8x8x8_A756", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (6307.8184, 6217.3364, 2213.272), (-14.146971827686658, -173.84815331866233, 177.8788523754636), (0.465501, 0.490916, 0.433262), "PWM_Nordic_8x8x8_A757", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (6480.7524, 6379.5923, 2063.0354), (13.168565016387163, 20.94146974919436, -174.36765634738822), (0.465501, 0.490916, 0.433262), "PWM_Nordic_8x8x8_A758", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (6599.04, 6559.206, 1907.0012), (22.725384543088804, 32.84353319707326, -171.63780369622856), (0.465501, 0.490916, 0.433262), "PWM_Nordic_8x8x8_A759", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (6165.843, 6842.3027, 2163.616), (12.338053215293087, -33.373929959114086, 172.70868286574225), (0.465501, 0.490916, 0.433262), "PWM_Nordic_8x8x8_A760", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (6039.8364, 6810.0654, 809.76355), (6.647976885328572, -150.49945007307224, 0.1982727995820073), (0.465501, 0.490916, 0.433262), "PWM_Nordic_8x8x8_A761", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5886.5767, 7574.4624, 779.8421), (3.3925969053346194, -166.66204952563172, -4.17092877078373), (0.465501, 0.490916, 0.433262), "PWM_Nordic_8x8x8_A762", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5961.9697, 7965.592, 744.1537), (-2.8013917072188015, 5.621032286118079, 4.588562191725665), (0.465501, 0.490916, 0.433262), "PWM_Nordic_8x8x8_A763", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5834.6465, 8580.064, 716.77655), (3.8462332926193405, 125.48449551382221, 0.8760375305966591), (0.465501, 0.490916, 0.433262), "PWM_Nordic_8x8x8_A764", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5707.4736, 8199.38, 655.2346), (13.369547663217482, -121.33723883781403, 1.0341798884246036), (0.465501, 0.490916, 0.433262), "PWM_Nordic_8x8x8_A765", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (6044.8022, 8038.23, 920.8167), (-3.3698118544615085, 13.033935082484948, 4.189360590054089), (0.465501, 0.490916, 0.433262), "PWM_Nordic_8x8x8_A766", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5932.583, 8251.47, 828.582), (4.025676668442656, -157.29784762322728, -3.563842087285904), (0.465501, 0.490916, 0.433262), "PWM_Nordic_8x8x8_A767", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (6064.4116, 8466.742, 804.9625), (5.884392549981433, 126.17749078213242, -4.790862960142781), (0.465501, 0.490916, 0.433262), "PWM_Nordic_8x8x8_A768", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (6222.4414, 8373.867, 939.6453), (3.8910624366250888, 161.061411062446, -5.345581887151209), (0.465501, 0.490916, 0.433262), "PWM_Nordic_8x8x8_A769", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (6129.885, 8672.218, 684.90936), (-0.2991335658299188, 87.2642823423193, -6.152008534013678), (0.465501, 0.490916, 0.433262), "PWM_Nordic_8x8x8_A770", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (6933.453, 8866.7705, 817.8024), (13.421880283263931, 118.02343847321656, -0.7525327008655426), (0.465501, 0.490916, 0.433262), "PWM_Nordic_8x8x8_A771", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (6602.2603, 8679.712, 783.76764), (-13.36239635402135, -92.5547149289604, 7.440521975934441), (0.465501, 0.490916, 0.433262), "PWM_Nordic_8x8x8_A772", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (6284.9043, 8636.421, 746.6423), (-12.897064859076076, -75.41217176604192, 3.8265986489462285), (0.465501, 0.490916, 0.433262), "PWM_Nordic_8x8x8_A773", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (7006.9565, 8403.864, 1030.2421), (-3.2325442415240646, -62.05474544356062, 3.100402490883119), (0.465501, 0.490916, 0.433262), "PWM_Nordic_8x8x8_A774", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (6341.7725, 8168.972, 1045.4645), (-3.235015571090384, -62.00573993265472, 3.0976868765193615), (0.465501, 0.490916, 0.433262), "PWM_Nordic_8x8x8_A775", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (6913.719, 8204.703, 1219.6375), (-16.794402311682912, -63.81250227248439, 4.418427771527517), (0.465501, 0.490916, 0.433262), "PWM_Nordic_8x8x8_A776", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (6583.5186, 8178.042, 1183.7806), (3.373539545168793, 83.39758212762115, 2.7483521709621943), (0.465501, 0.490916, 0.433262), "PWM_Nordic_8x8x8_A777", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (6556.3257, 8010.061, 1375.0903), (-2.42874154115601, -93.8928272648538, -2.696136651443358), (0.465501, 0.490916, 0.433262), "PWM_Nordic_8x8x8_A778", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4582.431, 7771.8296, 699.4768), (7.114924598695904, -8.1788021588076, -5.325103357799964), (0.465501, 0.490916, 0.433262), "PWM_Nordic_8x8x8_A779", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4413.2734, 8140.106, 629.2854), (12.625466916458526, 103.22264426378094, 4.382049036711316), (0.77574635, 0.490916, 0.40186754), "PWM_Nordic_8x8x8_A780", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4970.798, 7390.274, 615.03046), (-15.668760272420185, -151.39868420309688, 7.792571801788987), (0.465501, 0.490916, 0.433262), "PWM_Nordic_8x8x8_A781_885", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4453.3364, 7831.7646, 850.50635), (8.454974185174034, 102.42053842389736, 4.246826107150283), (0.465501, 0.490916, 0.433262), "PWM_Nordic_8x8x8_A782", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4883.4097, 7781.315, 603.7882), (9.425775756723203, 71.10455596121285, -0.7417907903717434), (0.465501, 0.490916, 0.433262), "PWM_Nordic_8x8x8_A783", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4519.5254, 8030.168, 676.3807), (-1.153290150752002, 121.96044810700036, -7.907898292484264), (0.465501, 0.490916, 0.433262), "PWM_Nordic_8x8x8_A784_893", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4207.1406, 8004.1113, 696.81573), (-18.44949194902288, -164.82421470128483, 10.259033446919432), (0.465501, 0.490916, 0.38339588), "PWM_Nordic_8x8x8_A785", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3989.394, 8226.648, 666.86035), (10.188686886766204, 69.60945839316113, 4.865569952016321), (0.465501, 0.490916, 0.433262), "PWM_Nordic_8x8x8_A786", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4157.344, 7846.2734, 860.9913), (10.750394565934654, 124.99282850035512, 3.489624473589948), (0.465501, 0.490916, 0.433262), "PWM_Nordic_8x8x8_A787", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4268.907, 7724.627, 968.85236), (-3.558716075096847, -64.10732984823495, -1.0902100324487554), (0.465501, 0.490916, 0.433262), "PWM_Nordic_8x8x8_A788", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4513.1973, 7706.616, 962.6878), (7.39919233765645, 19.723940179261, -4.830627678528733), (0.465501, 0.490916, 0.433262), "PWM_Nordic_8x8x8_A789", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (7015.9575, 10017.308, 882.7128), (16.307997904345346, -97.02818924826121, 4.017335399130508), (0.465501, 0.490916, 0.433262), "PWM_Nordic_8x8x8_A790_913", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (7387.6562, 9929.4795, 867.12726), (-16.17391848422415, 53.02252014397, 4.53903189098828), (0.465501, 0.490916, 0.433262), "PWM_Nordic_8x8x8_A791", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (6806.1934, 10019.456, 778.06415), (-7.879608405131252, 100.42286585569714, -6.645814510540272), (0.465501, 0.490916, 0.433262), "PWM_Nordic_8x8x8_A792", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (6780.351, 10217.174, 912.9247), (-11.742340771990182, 37.122311533836445, 10.833039356812378), (0.465501, 0.490916, 0.433262), "PWM_Nordic_8x8x8_A793", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (6242.7085, 10386.252, 980.7319), (5.043281517676033, -71.98619720573613, -0.28338609047749946), (0.465501, 0.490916, 0.433262), "PWM_Nordic_8x8x8_A794", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (6542.246, 10019.731, 776.5053), (9.78787222978479, -102.14014479603306, -6.395325279200372), (0.465501, 0.490916, 0.433262), "PWM_Nordic_8x8x8_A795", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (6012.0283, 10211.359, 818.3756), (-8.094146068288634, 118.66161631482233, -0.602721769994961), (0.465501, 0.490916, 0.433262), "PWM_Nordic_8x8x8_A796", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (6472.063, 8829.28, 738.9683), (-2.7872924619469015, -85.70297796939022, 3.9580079513315622), (0.465501, 0.490916, 0.433262), "PWM_Nordic_8x8x8_A797", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (7319.207, 10223.665, 1191.325), (-4.525695545251556, -130.18419893349215, -0.2123412780744719), (0.465501, 0.490916, 0.433262), "PWM_Nordic_8x8x8_A798", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (6018.402, 10616.29, 1107.0251), (-0.08795163008577021, 61.28155292085374, -0.5321349692673409), (0.61463356, 0.64004856, 0.58239454), "PWM_Nordic_8x8x8_A799", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5614.3604, 10271.232, 932.52814), (0.011078562575444208, 71.85436964656124, -0.5390930051446896), (0.614634, 0.640049, 0.582395), "PWM_Nordic_8x8x8_A800", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5886.9824, 9893.23, 722.8707), (8.182778689392526, -58.934692875941614, 10.153015670704404), (0.465501, 0.490916, 0.433262), "PWM_Nordic_8x8x8_A801", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (6186.7036, 10027.694, 750.471), (8.331559906042532, -69.33202688545752, 0.07769822866903338), (0.465501, 0.490916, 0.433262), "PWM_Nordic_8x8x8_A802", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4622.2593, 10052.745, 684.2169), (9.129619895975326, -78.10870881887746, 8.389740347767573), (0.627964, 0.65337896, 0.5957247), "PWM_Nordic_8x8x8_A803", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4820.1255, 9936.1455, 746.4478), (20.733139289168324, -109.52886174833684, -2.26687595800054), (0.465501, 0.490916, 0.433262), "PWM_Nordic_8x8x8_A804", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5022.542, 9799.809, 731.8154), (18.773785158356986, -112.77959140125088, -3.3164353265882234), (0.465501, 0.490916, 0.433262), "PWM_Nordic_8x8x8_A805", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5244.3516, 9841.2705, 721.4625), (10.022311786558177, -43.348208490162605, 16.29000803158206), (0.465501, 0.490916, 0.433262), "PWM_Nordic_8x8x8_A806", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4736.064, 10338.128, 920.7824), (22.210989902853424, -144.21326141838242, -1.6991875440141517), (0.465501, 0.490916, 0.433262), "PWM_Nordic_8x8x8_A807", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4274.404, 10743.621, 904.7497), (15.458775106316379, -92.19840989237822, 16.23492201929544), (0.465501, 0.490916, 0.433262), "PWM_Nordic_8x8x8_A808", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4468.8193, 10592.099, 884.8209), (17.153979076241033, -125.72321695084706, 5.278808226148036), (0.465501, 0.490916, 0.433262), "PWM_Nordic_8x8x8_A809", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5085.4785, 10061.879, 943.19226), (14.287676480136206, -66.42224548642449, 6.263916521492873), (0.465501, 0.490916, 0.433262), "PWM_Nordic_8x8x8_A810", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5542.638, 10024.281, 898.5034), (15.229806997280525, -78.03466602803532, 3.295686625703456), (0.465501, 0.490916, 0.433262), "PWM_Nordic_8x8x8_A811", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5249.552, 10419.472, 1110.9515), (2.5576256145773946, -125.36389018364532, 2.7801510228449917), (0.4742452, 0.490916, 0.433262), "PWM_Nordic_8x8x8_A812", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5070.436, 10357.754, 1033.1395), (11.610385613348738, -152.83484932560725, -9.451384071593973), (0.465501, 0.490916, 0.433262), "PWM_Nordic_8x8x8_A813", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4433.6016, 10969.67, 1143.5132), (5.961675375133038, -61.39634709837791, 8.30084235878742), (0.465501, 0.490916, 0.433262), "PWM_Nordic_8x8x8_A814_965", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4662.171, 10716.795, 957.54504), (15.62964731945994, -113.90801216123748, 8.88659650042319), (0.465501, 0.490916, 0.433262), "PWM_Nordic_8x8x8_A815", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4857.9326, 10459.713, 978.21533), (12.55589556650254, -166.27258023792123, -13.990570352950805), (0.465501, 0.490916, 0.433262), "PWM_Nordic_8x8x8_A816", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4281.728, 11237.137, 1149.6948), (-9.30062897164785, 30.581181008106643, -0.09625262378699594), (0.465501, 0.490916, 0.433262), "PWM_Nordic_8x8x8_A817", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5022.503, 10657.75, 1114.8251), (2.9079509123016667, -133.09203286459982, 2.411102012891834), (0.5823689, 0.607784, 0.5501299), "PWM_Nordic_8x8x8_A819", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3843.9756, 10903.752, 743.89636), (9.970979785108893, -172.49981771228875, -5.112914512328783), (0.465501, 0.490916, 0.433262), "PWM_Nordic_8x8x8_A820", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3970.0684, 10676.998, 711.7215), (-11.191589783479952, 35.94738876376918, -0.2171933731045507), (0.465501, 0.490916, 0.433262), "PWM_Nordic_8x8x8_A821", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4143.3457, 10421.669, 695.12775), (9.351663076766885, -111.49462441450412, 6.179532593744817), (0.465501, 0.490916, 0.433262), "PWM_Nordic_8x8x8_A822", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4638.969, 10362.1875, 915.06696), (4.303749998517139, 178.13525577672, -5.516113340938634), (0.465501, 0.490916, 0.433262), "PWM_Nordic_8x8x8_A824", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3791.9714, 10454.268, 552.1377), (3.0676170498898236, -155.82593034701378, -0.11746222896961425), (0.465501, 0.490916, 0.433262), "PWM_Nordic_8x8x8_A825_991", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3876.6519, 10634.357, 745.7956), (3.0393319277517024, -161.70788772382355, -0.4310303330557417), (0.465501, 0.490916, 0.36331114), "PWM_Nordic_8x8x8_A826", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4360.698, 10848.543, 1010.794), (18.531404588665684, -104.65503623972617, 7.047271889088852), (0.465501, 0.490916, 0.433262), "PWM_Nordic_8x8x8_A827", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4961.0444, 10583.293, 1050.1337), (12.626395835921496, -74.43150906947734, 15.354767065669131), (0.465501, 0.490916, 0.433262), "PWM_Nordic_8x8x8_A828", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3547.2915, 11909.181, 771.67334), (1.9618565148339857, -150.02911154904925, 7.221313557067332), (0.465501, 0.490916, 0.433262), "PWM_Nordic_8x8x8_A829", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3261.3882, 10980.164, 591.44006), (7.206271018960494, 164.54144297388484, -8.588196467765272), (0.465501, 0.490916, 0.433262), "PWM_Nordic_8x8x8_A830", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3267.9795, 11336.484, 612.6447), (10.563099409327911, 172.0414963986214, -2.316803043343431), (0.465501, 0.490916, 0.433262), "PWM_Nordic_8x8x8_A831", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3800.0085, 11293.135, 731.20087), (4.397501138266395, -136.26191074882266, 0.0963441315908988), (0.465501, 0.490916, 0.433262), "PWM_Nordic_8x8x8_A832", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3902.4382, 11423.844, 904.54596), (8.472581423455996, -115.35926164517095, 1.6624442271521327), (0.465501, 0.490916, 0.433262), "PWM_Nordic_8x8x8_A833", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3614.7886, 11839.9, 877.1435), (13.957912178740532, -171.06739442917166, -4.757506447890905), (0.465501, 0.490916, 0.433262), "PWM_Nordic_8x8x8_A834", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2268.3125, 11023.662, 722.36414), (1.131065505114371, -0.30175779555856075, -1.6465759892902498), (0.465501, 0.490916, 0.433262), "PWM_Nordic_8x8x8_A835", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2404.7605, 11274.349, 756.6984), (0.25640067829392477, -9.501281907896056, -1.874755952760398), (0.465501, 0.490916, 0.433262), "PWM_Nordic_8x8x8_A836", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2153.2615, 11037.591, 893.50903), (7.03045449424523, -18.282590708602793, -3.264343265958507), (0.465501, 0.490916, 0.433262), "PWM_Nordic_8x8x8_A837", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2267.5024, 10656.426, 641.77344), (2.668663992473378, 0.48132324285554623, -12.775573164088394), (0.465501, 0.490916, 0.433262), "PWM_Nordic_8x8x8_A838", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2775.2305, 11985.346, 726.75397), (3.721887812888501, -1.0951537554926036, -0.3065185475473859), (0.465501, 0.490916, 0.433262), "PWM_Nordic_8x8x8_A839", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2425.9636, 11560.068, 770.8407), (3.637341643525977, 16.726316402263112, 0.8464965095182866), (0.465501, 0.490916, 0.433262), "PWM_Nordic_8x8x8_A840", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2318.5166, 11645.818, 1089.6101), (3.477721826680695, -17.7769165847486, -1.3612975987604388), (0.465501, 0.490916, 0.433262), "PWM_Nordic_8x8x8_A841", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2530.1792, 11925.916, 961.7549), (0.09163396258793242, 63.39868203846472, 5.220367441731847), (0.465501, 0.490916, 0.433262), "PWM_Nordic_8x8x8_A842", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2369.2886, 10854.519, 672.7515), (10.005358528358101, 36.34911791462189, -7.302000747985481), (0.465501, 0.490916, 0.433262), "PWM_Nordic_8x8x8_A843", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2210.9639, 11397.436, 976.1738), (-1.753234673932952, -85.1906674212218, -0.7116698799963788), (0.465501, 0.490916, 0.433262), "PWM_Nordic_8x8x8_A844", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1865.1333, 11495.736, 1171.5602), (8.429907596555333, -85.3178171567845, -0.7190857777578963), (0.465501, 0.490916, 0.433262), "PWM_Nordic_8x8x8_A845", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2611.8848, 12070.134, 900.1153), (-12.031371116764142, 176.7904085655325, -2.0024715931667303), (0.465501, 0.490916, 0.433262), "PWM_Nordic_8x8x8_A846", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4621.521, 11325.465, 1383.4888), (11.949939924236366, -80.64147352470759, 6.1238084824766394), (0.465501, 0.490916, 0.433262), "PWM_Nordic_8x8x8_A847", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5478.013, 10784.982, 1375.8442), (8.819207043276553, -157.42285396507714, -10.138793282446208), (0.465501, 0.490916, 0.433262), "PWM_Nordic_8x8x8_A848_1070", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5423.235, 10671.859, 1318.0955), (10.004588253770569, -156.64019652331152, -10.021605915498288), (0.465501, 0.490916, 0.433262), "PWM_Nordic_8x8x8_A849", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5680.6, 10652.47, 1370.3765), (11.792881842309297, -77.21692659539326, 7.830384627639523), (0.465501, 0.490916, 0.433262), "PWM_Nordic_8x8x8_A850", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (6028.0317, 10629.197, 1329.2921), (11.792881842309297, -77.21692659539326, 7.830384627639523), (0.465501, 0.490916, 0.433262), "PWM_Nordic_8x8x8_A851", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4781.578, 11364.83, 1368.7382), (13.404335306985299, -106.8112076834031, 0.2830508109688614), (0.465501, 0.490916, 0.433262), "PWM_Nordic_8x8x8_A852", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4279.413, 9973.021, 569.2369), (-0.4361571383298992, 117.10108409670647, -5.537383825587683), (0.465501, 0.490916, 0.433262), "PWM_Nordic_8x8x8_A853", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1583.2349, 10963.187, 775.3935), (-12.290772514032746, -121.0419943040445, 4.411224229525558), (0.465501, 0.490916, 0.433262), "PWM_Nordic_8x8x8_A854", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1883.3484, 10842.398, 761.3427), (-12.981413207886048, -95.28038514551224, -1.3165586498546933), (0.465501, 0.490916, 0.433262), "PWM_Nordic_8x8x8_A855", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1095.8685, 11258.912, 764.5943), (-6.969666284043854, -81.99903039557482, -10.96295134196335), (0.465501, 0.490916, 0.433262), "PWM_Nordic_8x8x8_A856", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (579.64514, 11553.191, 710.9092), (-6.969635446564215, -81.99902228596444, -2.7852478841429473), (0.465501, 0.490916, 0.433262), "PWM_Nordic_8x8x8_A857", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1020.64636, 11540.018, 839.1528), (-1.8396298306406917, 23.39404231270306, -0.9227600694630598), (0.465501, 0.490916, 0.433262), "PWM_Nordic_8x8x8_A858", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (723.15344, 11808.321, 873.4013), (-0.5769347333285944, 70.47240706395579, -1.9754943573082073), (0.465501, 0.490916, 0.433262), "PWM_Nordic_8x8x8_A859", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (477.46436, 11737.183, 798.5982), (-1.419830029930285, -49.636108021357245, 1.4897153322676095), (0.465501, 0.490916, 0.433262), "PWM_Nordic_8x8x8_A860", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1089.5592, 11645.301, 1045.6787), (-4.773316097972994, 32.37696198981834, 3.478729545233265), (0.4459379, 0.57500905, 0.433262), "PWM_Nordic_8x8x8_A861", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1339.6393, 11516.779, 1074.9585), (2.598968373806055, -175.43726512390663, -5.303099358480261), (0.465501, 0.490916, 0.433262), "PWM_Nordic_8x8x8_A862", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1920.5732, 8041.897, 672.2589), (4.213154196651611, 77.76770881591298, 10.353303042777403), (0.465501, 0.490916, 0.433262), "PWM_Nordic_8x8x8_A863", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1922.6094, 8303.074, 581.5318), (20.7438738104717, -2.5955805484601546, -2.3943477608128343), (0.465501, 0.490916, 0.433262), "PWM_Nordic_8x8x8_A864", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1793.5725, 8602.139, 579.8069), (19.847582788430756, 22.96728782547612, 6.604919726556861), (0.465501, 0.490916, 0.433262), "PWM_Nordic_8x8x8_A865", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1798.5845, 8996.906, 579.7859), (14.682270228739949, 27.017337360243673, 0.7714539294640786), (0.465501, 0.490916, 0.433262), "PWM_Nordic_8x8x8_A866", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4614.6553, 9776.409, 722.64935), (16.330574325082925, -68.6182862119392, 9.691678759054234), (0.465501, 0.490916, 0.433262), "PWM_Nordic_8x8x8_A867_193", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1030.7457, 8551.868, 691.71326), (0.6259458672618636, 130.584230917012, 1.2207338246803097), (0.465501, 0.490916, 0.352827), "PWM_Nordic_8x8x8_A868", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (991.35187, 8242.021, 738.71094), (-0.3346251810722626, 171.84545895827694, 1.330413396665094), (0.465501, 0.490916, 0.352827), "PWM_Nordic_8x8x8_A869", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1076.1509, 7975.3975, 749.55054), (0.4978935241698065, -0.9885254850826733, 5.227234399316744), (0.465501, 0.490916, 0.352827), "PWM_Nordic_8x8x8_A870", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (624.4306, 7983.927, 714.45026), (0.3439580025774902, 118.99842509017662, 6.308899472101178), (0.465501, 0.490916, 0.352827), "PWM_Nordic_8x8x8_A871", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (292.65, 7573.313, 718.2773), (0.2942786668908293, 128.3955050384873, 0.3285522355708959), (0.465501, 0.490916, 0.352827), "PWM_Nordic_8x8x8_A872", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (884.48505, 7823.1997, 818.1326), (-0.44039920303270874, -102.71483190123256, 0.02288818306960251), (0.465501, 0.490916, 0.352827), "PWM_Nordic_8x8x8_A873", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (935.9151, 8017.9814, 737.5164), (-0.4043273653130594, -76.23632630678698, -0.1758728006882148), (0.465501, 0.490916, 0.352827), "PWM_Nordic_8x8x8_A874", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1755.9972, 7878.2007, 763.9492), (-6.604705609979841, -152.42090329735964, 2.9836423831928975), (0.465501, 0.490916, 0.433262), "PWM_Nordic_8x8x8_A875", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1051.0769, 7665.947, 989.25696), (0.4052009275294295, 57.00561372953373, -0.17410276694463586), (0.465501, 0.490916, 0.352827), "PWM_Nordic_8x8x8_A876", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1751.8967, 7732.9272, 904.6247), (2.717404233390437, 120.03271555182917, 7.481628320400571), (0.465501, 0.490916, 0.433262), "PWM_Nordic_8x8x8_A877", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1434.6917, 9110.527, 616.4995), (1.36200106310725, 74.58349499411428, 0.1637268009120895), (0.465501, 0.490916, 0.352827), "PWM_Nordic_8x8x8_A878", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (971.52545, 8862.049, 599.0812), (-0.11273192533219509, 162.44054270168056, 1.3670653324669912), (0.465501, 0.490916, 0.352827), "PWM_Nordic_8x8x8_A879", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1145.5187, 9088.447, 575.60834), (-1.3624569577379906, -105.67162587513883, -0.1576842625000062), (0.465501, 0.490916, 0.352827), "PWM_Nordic_8x8x8_A880", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1602.13, 8413.237, 710.3339), (4.956339877433012, -91.78318725248144, -4.274505328849692), (0.465501, 0.490916, 0.433262), "PWM_Nordic_8x8x8_A881", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3703.4072, 8194.554, 666.9613), (2.9038202658796197, 151.87482021954818, 10.79003680200646), (0.465501, 0.490916, 0.433262), "PWM_Nordic_8x8x8_A882", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (7927.3164, 9630.467, 798.82074), (-6.679962260107508, -98.6101643290765, 3.88183601712908), (0.465501, 0.490916, 0.433262), "PWM_Nordic_8x8x8_A883", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (7643.4663, 9634.824, 764.4791), (7.07033054158826, 106.41753637914815, -4.238890665131895), (0.465501, 0.490916, 0.433262), "PWM_Nordic_8x8x8_A884", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (9575.539, 10233.449, 827.1736), (6.3856650220441304, -109.93720875462233, 2.5892938158760486), (0.465501, 0.490916, 0.433262), "PWM_Nordic_8x8x8_A885", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (8664.34, 9974.642, 809.32007), (9.34524605062766, -38.31363060489574, 6.975007384180263), (0.465501, 0.490916, 0.433262), "PWM_Nordic_8x8x8_A886", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (8885.321, 10250.227, 821.5466), (-1.9872127953043548, 121.24388767811789, -6.5972898959474495), (0.465501, 0.490916, 0.433262), "PWM_Nordic_8x8x8_A887", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (9314.554, 10270.849, 833.08826), (5.2717371621657145, -91.85716714542936, 4.440612644933985), (0.465501, 0.490916, 0.433262), "PWM_Nordic_8x8x8_A888", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (9646.408, 10060.117, 665.3762), (-6.766204169905274, 37.05541290507916, 1.2969966303922342), (0.465501, 0.490916, 0.433262), "PWM_Nordic_8x8x8_A889", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (8821.789, 9883.66, 683.19745), (-6.447937093296842, 68.63238272173217, -2.42980916650501), (0.465501, 0.490916, 0.433262), "PWM_Nordic_8x8x8_A890", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (9361.443, 10910.719, 1205.8888), (4.847221454781852, -110.0419135924827, -2.139801380335762), (0.465501, 0.490916, 0.433262), "PWM_Nordic_8x8x8_A891", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (8453.94, 10699.8, 1293.5035), (2.4055720632390734, -23.128753060109155, 4.721191416076996), (0.465501, 0.490916, 0.433262), "PWM_Nordic_8x8x8_A892", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (8611.067, 10498.562, 1090.27), (4.971997560255594, -65.94667695331081, 1.8305357226864707), (0.465501, 0.490916, 0.433262), "PWM_Nordic_8x8x8_A893", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (9571.026, 10598.662, 1074.8325), (2.230295666047585, -151.3507054711929, -4.806305042293614), (0.465501, 0.490916, 0.433262), "PWM_Nordic_8x8x8_A894", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (8915.046, 10845.294, 1201.3599), (4.826989343579471, -61.798001614155524, 2.184966536327571), (0.465501, 0.490916, 0.433262), "PWM_Nordic_8x8x8_A895", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (9148.6, 10919.113, 1207.8258), (5.295965625522474, -84.82897372757093, 0.12539659022687544), (0.465501, 0.490916, 0.433262), "PWM_Nordic_8x8x8_A896", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (8601.241, 10703.505, 1244.3802), (4.566570239935925, -55.661801828475404, 2.6878051362158435), (0.465501, 0.490916, 0.433262), "PWM_Nordic_8x8x8_A897", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (9525.65, 10906.651, 1388.7411), (-1.2317505565773483, -151.33251858197164, 1.3915710853036063), (0.465501, 0.490916, 0.433262), "PWM_Nordic_8x8x8_A898", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (8465.957, 10581.547, 2245.6646), (9.133213201345708, -54.95532792552418, -173.3154662111093), (0.465501, 0.490916, 0.433262), "PWM_Nordic_8x8x8_A899", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (8834.882, 10578.464, 1087.0756), (10.30445750216564, -39.0364914802967, 4.527739829657237), (0.465501, 0.490916, 0.433262), "PWM_Nordic_8x8x8_A900", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (8450.672, 9556.586, 691.45123), (5.2900551848218855, -92.13824602992838, 2.296234013688389), (0.465501, 0.490916, 0.433262), "PWM_Nordic_8x8x8_A901", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (8294.951, 9509.322, 702.55817), (5.655206136336693, -104.37472938340989, 1.1248168823508218), (0.465501, 0.490916, 0.433262), "PWM_Nordic_8x8x8_A902", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (8430.925, 9499.617, 667.7777), (-5.752288426681679, 68.25511697930648, -0.3912661060098397), (0.465501, 0.490916, 0.433262), "PWM_Nordic_8x8x8_A903", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (7689.239, 8826.5, 740.72766), (-4.742248305648531, -103.91475944398108, 1.1895751433484063), (0.465501, 0.490916, 0.433262), "PWM_Nordic_8x8x8_A904", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (7293.888, 8928.057, 745.21375), (-4.519103503207416, -112.28956998085934, 1.8670347376256258), (0.465501, 0.490916, 0.433262), "PWM_Nordic_8x8x8_A905", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (10811.961, 9659.114, 742.4192), (8.468861113424046, -55.17827935150155, -2.0343934086303466), (0.465501, 0.490916, 0.433262), "PWM_Nordic_8x8x8_A906", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (10410.043, 9645.734, 682.0552), (-2.0230101349189544, -144.9507392051645, -8.47170825667732), (0.465501, 0.490916, 0.433262), "PWM_Nordic_8x8x8_A907", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (10218.641, 10177.538, 855.2326), (-1.7298582810768988, -103.77886635686693, -1.0949399983248522), (0.465501, 0.490916, 0.433262), "PWM_Nordic_8x8x8_A908", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (10198.321, 10086.371, 771.1537), (13.673785824982446, 105.29455874103111, 6.943176446740296), (0.465501, 0.490916, 0.433262), "PWM_Nordic_8x8x8_A909", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (11512.272, 10058.549, 790.29706), (0.4489927223430953, -54.89425087685535, -2.0122376880893857), (0.465501, 0.490916, 0.433262), "PWM_Nordic_8x8x8_A910", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (11231.902, 10003.435, 780.21545), (0.5842337623051183, 96.072993887366, 1.9771117913836167), (0.465501, 0.490916, 0.433262), "PWM_Nordic_8x8x8_A911", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (11197.536, 10253.447, 1081.3671), (2.1748970133370773, -115.91949119768569, -0.25073219931573704), (0.465501, 0.490916, 0.433262), "PWM_Nordic_8x8x8_A912", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (11042.133, 10204.492, 1113.4597), (-4.001556348779291, -115.8921180628516, -0.2511598218231562), (0.465501, 0.490916, 0.433262), "PWM_Nordic_8x8x8_A913", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (10806.359, 10242.651, 1070.268), (7.4043474049556455, -115.94198382253435, -0.2526550049420942), (0.465501, 0.490916, 0.433262), "PWM_Nordic_8x8x8_A914", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (10195.203, 10301.718, 1033.6332), (5.7238410843336345, -85.90262325064735, -2.769073779839007), (0.465501, 0.490916, 0.433262), "PWM_Nordic_8x8x8_A915", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (9850.691, 10263.29, 888.0982), (-0.006835876072382507, -143.5180405904768, -4.400970406135245), (0.465501, 0.490916, 0.433262), "PWM_Nordic_8x8x8_A916", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (11133.729, 8910.811, 685.15796), (0.44905750306454045, 138.15814541134262, 2.169250542874402), (0.465501, 0.490916, 0.433262), "PWM_Nordic_8x8x8_A917", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (10767.858, 8945.578, 695.48755), (0.44905800038439575, 138.15814542500135, 2.169250720981864), (0.465501, 0.490916, 0.433262), "PWM_Nordic_8x8x8_A918", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (11676.73, 8944.085, 671.9622), (1.4734699996059386, 108.16631203725454, 1.6542663351703115), (0.465501, 0.490916, 0.433262), "PWM_Nordic_8x8x8_A919", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (10362.795, 8584.464, 664.57733), (-12.156372612092325, -45.966577153127965, 4.890686495813118), (0.465501, 0.490916, 0.433262), "PWM_Nordic_8x8x8_A920", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (11178.436, 8652.039, 921.7315), (-3.7335508920381706, -48.207883126273764, -4.940215693552959), (0.465501, 0.490916, 0.433262), "PWM_Nordic_8x8x8_A921", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (10317.027, 7757.7754, 624.85767), (-14.346100273350155, 37.6184720265219, -7.464996468349619), (0.648419, 0.648419, 0.50543696), "PWM_Nordic_8x8x8_A922", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (10002.282, 7975.167, 640.0974), (7.309633321936032, -106.57287246187461, 3.2944023341006567), (0.648419, 0.648419, 0.55637616), "PWM_Nordic_8x8x8_A923", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (10745.812, 7272.6816, 930.6746), (-0.9259948421531894, 164.04773025655183, -0.8687133549799707), (0.648419, 0.648419, 0.648419), "PWM_Nordic_8x8x8_A924", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (10668.741, 7623.5205, 841.1238), (0.43823166148711884, -169.69573948679735, -6.606108361781276), (0.648419, 0.648419, 0.53778845), "PWM_Nordic_8x8x8_A925", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (10614.116, 8113.568, 768.14734), (0.9425593568828503, -165.3248323125624, -6.553497377377347), (0.648419, 0.648419, 0.537788), "PWM_Nordic_8x8x8_A926", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (11040.513, 8070.745, 1050.0537), (-6.017333598181393, -2.339050049717106, 2.3463132697866573), (0.648419, 0.648419, 0.537788), "PWM_Nordic_8x8x8_A927", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (10849.642, 6186.5864, 964.23456), (3.3984906776403414, -39.628109113665566, 3.199401468700065), (0.508692, 0.534107, 0.476453), "PWM_Nordic_8x8x8_A928", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (10723.01, 5954.6216, 975.53314), (12.665434856552404, 148.68052068723426, -2.5241089849252347), (0.508692, 0.534107, 0.476453), "PWM_Nordic_8x8x8_A929", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (9592.937, 8064.7144, 540.3327), (0.33938521446436354, -106.82092073068928, 0.6178588908236089), (0.508692, 0.534107, 0.476453), "PWM_Nordic_8x8x8_A930", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (10927.912, 7144.0186, 1308.5089), (7.93368633897843, -119.29021954102167, 0.4414978027381301), (0.508692, 0.534107, 0.476453), "PWM_Nordic_8x8x8_A931", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (9546.54, 10777.925, 2080.49), (-5.9255669880626085, -161.0240505450563, -164.27760965519929), (0.465501, 0.490916, 0.433262), "PWM_Nordic_8x8x8_A932", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (8825.957, 10611.244, 2338.9783), (-1.022643958239223, -72.86212040122149, 178.16384363884364), (0.465501, 0.490916, 0.433262), "PWM_Nordic_8x8x8_A933", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (9467.105, 11053.405, 1941.057), (-5.925536880382654, -161.02405079771333, -170.2586056987947), (0.465501, 0.490916, 0.433262), "PWM_Nordic_8x8x8_A934", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (8228.486, 10621.958, 2031.2211), (-15.19805848451105, -5.705871261921652, 178.27384347332654), (0.589848, 0.615263, 0.55760896), "PWM_Nordic_8x8x8_A935", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (10282.932, 10047.152, 1950.8906), (-64.68186715035665, -115.6767874644496, 6.02721763273277), (0.465501, 0.6127104, 0.5441241), "PWM_Nordic_8x8x8_A936", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (10684.046, 7646.116, 1719.4324), (-2.403960906467459, 152.00704117169818, 172.88952755855152), (0.508692, 0.534107, 0.476453), "PWM_Nordic_8x8x8_A937", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (11091.492, 6682.082, 2437.9236), (-17.62185716458156, -130.63391633114847, 172.37469695630796), (0.5605047, 0.534107, 0.476453), "PWM_Nordic_8x8x8_A938", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (10600.116, 7237.2944, 2243.0164), (-17.62185716458156, -130.63391633114847, 172.37469695630796), (0.508692, 0.534107, 0.476453), "PWM_Nordic_8x8x8_A939", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (11060.134, 7828.415, 1379.6461), (13.108406444463073, -85.67284388497087, 179.95935370217788), (0.54783374, 0.5732488, 0.5155947), "PWM_Nordic_8x8x8_A940", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5576.3887, 8489.582, 831.74023), (3.8030793296949392, 128.06102079234174, -4.848326785887906), (0.28593305, 0.28593305, 0.116578825), "PWM_Nordic_8x8x8_A941", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2337.6492, 7929.8066, 699.813), (3.5209565149152198, 27.258177934279647, 0.518829382712049), (0.465501, 0.490916, 0.433262), "PWM_Nordic_8x8x8_A943", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2086.2148, 7822.5547, 707.71515), (-1.3093873042966948, 130.43372500677447, 3.309631785280602), (0.465501, 0.490916, 0.433262), "PWM_Nordic_8x8x8_A944", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3496.5967, 7984.706, 674.45746), (-0.1962277954529538, 112.02916149657005, 3.553618779698274), (0.465501, 0.490916, 0.433262), "PWM_Nordic_8x8x8_A945", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3441.271, 8176.3936, 672.2327), (0.19746082984265562, 105.69677952777657, 3.553527684980664), (0.465501, 0.490916, 0.19894333), "PWM_Nordic_8x8x8_A946", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2307.232, 8080.96, 685.10034), (1.793586282229655, 78.64287693169588, 3.0745239596947083), (0.465501, 0.490916, 0.22625554), "PWM_Nordic_8x8x8_A947", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3659.6868, 8696.879, 612.5865), (10.140467275453734, 51.6923011426252, 2.349487696693079), (0.465501, 0.490916, 0.433262), "PWM_Nordic_8x8x8_A948", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3917.523, 8456.602, 676.2016), (9.783222211487889, 18.443359791584555, -3.5642392410710486), (0.465501, 0.490916, 0.433262), "PWM_Nordic_8x8x8_A949", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3737.6477, 8391.884, 683.8356), (4.695788289651619, -172.14863380743307, 5.448363959947882), (0.465501, 0.490916, 0.433262), "PWM_Nordic_8x8x8_A950", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (9781.164, 7896.276, 606.13873), (-2.8425900883858257, 46.09698467876306, 3.4626160070269583), (0.508692, 0.534107, 0.3983422), "PWM_Nordic_8x8x8_A951", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3471.1392, 9027.773, 535.45715), (10.140468725855234, 51.69321808668781, 5.598144856021325), (0.465501, 0.490916, 0.433262), "PWM_Nordic_8x8x8_A952", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3302.2646, 9213.582, 518.148), (10.140468725855234, 51.69321808668781, 5.598144856021325), (0.465501, 0.490916, 0.433262), "PWM_Nordic_8x8x8_A953", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3525.4812, 9024.523, 546.5345), (-8.623992981395167, -115.21843532324914, -7.741455774067809), (0.465501, 0.490916, 0.433262), "PWM_Nordic_8x8x8_A954", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5923.1104, 2501.802, 659.0632), (10.81110376339201, 96.56555567599291, 2.3521426285354425), (0.34088126, 0.36629626, 0.30864227), "PWM_Nordic_8x8x8_A955", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4111.564, 9804.969, 560.3914), (2.556092323739849, 99.99108722145338, 11.287079566144337), (0.465501, 0.490916, 0.433262), "PWM_Nordic_8x8x8_A956", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (11533.928, 6220.7466, 1129.9792), (-14.73178141742303, 2.2776488802532793, 3.89144950655518), (0.77447903, 0.79989403, 0.5451076), "PWM_Nordic_8x8x8_A960", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (11938.804, 5647.774, 1688.5154), (0.7235355566697599, 131.1127370087962, -0.43844606296858324), (1.0, 1.0599684, 1.0), "PWM_Nordic_8x8x8_A961", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (11807.501, 6956.7285, 1743.1993), (0.3934188630582725, -90.39330266274706, 0.23733522713318309), (1.0, 1.0, 1.0), "PWM_Nordic_8x8x8_A962", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (11665.317, 7023.247, 2364.4995), (7.34095857930066, -97.3499355334544, 179.89974915821227), (1.1923411, 1.0800992, 1.0), "PWM_Nordic_8x8x8_A963", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (11970.572, 5614.982, 2321.7625), (4.618643050312649, -54.652045861674935, -179.57611101666603), (1.0, 1.0, 1.0), "PWM_Nordic_8x8x8_A964", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (12073.752, 6533.583, 2413.7505), (-51.25518489585282, -161.3774291129626, 174.81232733760416), (1.190706, 1.0, 1.0), "PWM_Nordic_8x8x8_A965", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (12354.121, 6298.835, 1784.0536), (0.201552060356514, 174.52831246663186, -0.41290285715326563), (1.0412817, 1.0, 1.0), "PWM_Nordic_8x8x8_A966", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (10584.65, 5579.798, 992.41235), (21.954236517185084, -170.58594191366032, 6.399717297165753), (0.43873265, 0.46414766, 0.35479805), "PWM_Nordic_8x8x8_A967", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (9139.241, 1145.7601, 719.0356), (5.782591053748217, 153.9796861952917, 5.921477339911071), (0.465501, 0.490916, 0.433262), "PWM_Nordic_8x8x8_A987", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (9293.815, 10959.1455, 2112.6985), (-6.668638603438139, -156.55546742742737, -170.74830752926923), (0.465501, 0.490916, 0.433262), "PWM_Nordic_8x8x8_A998", _folder)
if a: placed += 1
else: skipped += 1

# Batch 66: StaticMesh'PWM_Nordic_Blend_A' (145 instances)
_mesh_path = "/Game/Unshippable/Whitebox/Rocks/Meshes/PWM_Nordic_Blend_A"
_materials = ['/Game/Art/Assets/Kits/Misc/Dirt_Mounds/Materials/MI_DirtMound_Cavern']
_folder = "Reconstruction/BD_BB_Chapter3_HeadwaterNexus/Meshes"
a = spawn_static_mesh(_mesh_path, _materials, (8789.639, 5817.942, 884.53674), (0.13909676845708993, 179.51198140102255, 0.06179182640204074), (1.4427098, 1.4427098, 1.4427098), "PWM_Nordic_Blend_A_60", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (9564.206, 5193.297, 845.3924), (-1.1422121803822713, 0.16479496184872575, -7.408387023442465), (1.0465356, 1.0465356, 0.60427445), "PWM_Nordic_Blend_A10", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (8935.0, 905.0, 740.0), (0.0, 0.0, -0.0), (0.8169608, 0.8169608, 0.6278204), "PWM_Nordic_Blend_A100_80", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2802.3608, 10551.099, 726.8006), (-4.236225335836652e-07, 41.065012648737486, -10.49841432770546), (0.46383244, 0.46383244, 0.46383244), "PWM_Nordic_Blend_A101_26", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (9250.061, 5751.9507, 692.54614), (0.15174617146965508, 160.2758899193539, 0.012494045693637035), (1.7685283, 1.7685283, 1.7685283), "PWM_Nordic_Blend_A102", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (10677.673, 4843.657, 1168.5852), (2.1632898802491933, -38.88497120775168, 8.763684794063249), (0.907571, 0.907571, 0.50489736), "PWM_Nordic_Blend_A103", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (10658.7295, 6647.049, 671.9369), (0.14291490713356506, 135.37051400474255, -5.822142204795942), (1.768528, 1.768528, 1.768528), "PWM_Nordic_Blend_A104", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (10609.8955, 7800.057, 809.83466), (-0.21572893600353885, 131.8506030737652, -5.820099355881008), (2.3062608, 2.3062608, 2.449651), "PWM_Nordic_Blend_A105", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (9849.814, 5103.8193, 837.56476), (-2.996368252513134, -23.208161536526905, -4.6266785553823135), (1.0, 1.0, 0.509892), "PWM_Nordic_Blend_A106", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (9838.079, 5430.1094, 844.7134), (0.8267807485869424, 5.588073756669279, 16.02063923551497), (1.0, 0.34216434, 0.31689999), "PWM_Nordic_Blend_A107", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (9941.638, 5437.6143, 844.6048), (0.8267809752930759, 5.588073788961506, 16.020639247689815), (1.0, 0.342164, 0.3369425), "PWM_Nordic_Blend_A108", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (10228.077, 5082.07, 917.4034), (26.613388499144282, -85.54398041390398, 5.4056459703059545), (1.0, 1.0, 1.126363), "PWM_Nordic_Blend_A109", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (10162.472, 5234.902, 844.97485), (0.4927426351060431, 8.707824284594437, -5.510070099621709), (1.0, 1.0, 0.50989217), "PWM_Nordic_Blend_A11", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (10237.212, 4973.371, 980.21027), (18.765829208375994, -82.22423052283841, 5.238444823667906), (0.7785561, 1.0, 1.126363), "PWM_Nordic_Blend_A110", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (10550.717, 5299.058, 1049.4552), (-14.0072625956582, 113.22058723720913, 14.50543320558011), (1.542917, 1.542917, 1.258742), "PWM_Nordic_Blend_A111", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (10576.447, 4232.6255, 1025.4486), (-0.030029454133370343, -56.93823203739418, 3.9644270926498817), (1.1819197, 1.1819197, 1.3335297), "PWM_Nordic_Blend_A112", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (10592.606, 3860.6853, 1018.03076), (1.3975434186256246, 143.23901103688675, 3.1784965147675384), (1.18192, 1.18192, 1.5936683), "PWM_Nordic_Blend_A113", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (9258.876, 1120.2057, 729.4946), (0.9109011548341145, 82.59984478897337, 1.4631506487685466), (1.2816005, 1.6418234, 2.1453114), "PWM_Nordic_Blend_A114", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (7881.8193, 638.85614, 734.8243), (0.6616812431551359, 91.91894221966122, 1.5913823913788172), (1.2816, 1.641823, 2.145311), "PWM_Nordic_Blend_A115", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (7468.9824, 988.19293, 849.9475), (-5.699067055338298, 91.74170793691027, -16.203889970222253), (1.2816, 1.641823, 2.0334234), "PWM_Nordic_Blend_A116", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (241.07149, 3473.3372, 775.4875), (-3.4396666863364334, 178.931524372932, -3.854919585286666), (1.0, 1.0, 1.0), "PWM_Nordic_Blend_A117", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5861.4756, 8528.555, 842.58044), (0.0, -164.92240317555087, 0.0), (1.2667103, 1.2667103, 1.2667103), "PWM_Nordic_Blend_A118", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4063.7183, 8237.625, 732.83167), (0.0, 5.461975189975804, -0.0), (1.26671, 1.26671, 1.26671), "PWM_Nordic_Blend_A119", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (9412.952, 4689.615, 1042.5923), (0.17572033376666701, 97.92120140081808, -1.494476246413726), (1.0, 1.0, 1.0), "PWM_Nordic_Blend_A12", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4412.043, 8176.78, 732.83167), (0.0, 5.461975189975804, -0.0), (1.26671, 1.26671, 1.26671), "PWM_Nordic_Blend_A120", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3747.9226, 8667.395, 732.83154), (0.0, -37.194335066141136, 0.0), (1.26671, 1.26671, 0.99123377), "PWM_Nordic_Blend_A121", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2020.3043, 8438.905, 690.4332), (0.0, -37.194335066141136, 0.0), (1.815124, 1.815124, 0.7269521), "PWM_Nordic_Blend_A122", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2373.118, 8067.092, 690.4332), (0.0, -54.338868266430225, 0.0), (1.815124, 1.815124, 0.726952), "PWM_Nordic_Blend_A123", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3780.9656, 10291.666, 671.1704), (-2.0479735451073413, 174.12405664544482, -3.4652407556777156), (1.0, 1.0, 0.6789857), "PWM_Nordic_Blend_A124", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3853.787, 10205.44, 698.2909), (-2.0479735451073413, 174.12405664544482, -3.4652407556777156), (1.0, 1.0, 0.37746507), "PWM_Nordic_Blend_A125", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2138.3416, 7774.2188, 690.4332), (0.0, -109.36691266911318, 0.0), (1.815124, 1.815124, 0.726952), "PWM_Nordic_Blend_A126", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (11543.948, 6476.2427, 1429.8312), (3.8274328227367898, -98.09991446711244, 4.580848432802049), (1.217928, 1.217928, 1.516557), "PWM_Nordic_Blend_A127", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (11274.91, 6518.3994, 1327.0569), (3.004860170328125, 151.8471626525292, -5.15719548907175), (1.217928, 1.217928, 1.7134675), "PWM_Nordic_Blend_A128", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (11889.301, 5798.8994, 1622.8287), (0.0, 10.946852215049997, -0.0), (1.0, 1.0, 1.0), "PWM_Nordic_Blend_A129", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (9496.582, 4514.304, 1014.39453), (0.49203420718451363, 102.93620546600825, 3.4312736475315955), (1.0, 1.0, 1.0), "PWM_Nordic_Blend_A13", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (12053.839, 6047.919, 1622.8287), (0.0, 32.004988355113476, -0.0), (1.0, 1.0, 1.0), "PWM_Nordic_Blend_A130", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (12116.558, 6316.844, 1622.8287), (0.0, 55.25953022478951, -0.0), (1.0, 1.0, 1.0), "PWM_Nordic_Blend_A131", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (12146.576, 6552.5376, 1622.8287), (0.0, 55.25953022478951, -0.0), (1.0, 1.0, 1.0), "PWM_Nordic_Blend_A132", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (12042.149, 6696.7246, 1622.8287), (0.0, -176.69790475225932, 0.0), (1.1742922, 1.1742922, 1.1742922), "PWM_Nordic_Blend_A133", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (11667.595, 6795.002, 1622.8287), (0.0, -162.7345320223533, 0.0), (1.174292, 1.174292, 1.174292), "PWM_Nordic_Blend_A134", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2814.686, 8003.3286, 690.4332), (0.0, -15.581726231331325, 0.0), (1.815124, 1.815124, 0.83756685), "PWM_Nordic_Blend_A135", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3194.6636, 8084.234, 690.4331), (0.0, -15.581726231331325, 0.0), (1.815124, 1.815124, 0.5664837), "PWM_Nordic_Blend_A136", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (6879.6035, 1732.1279, 843.8235), (32.384123063267694, -61.13090722427005, 3.115441420728243), (1.0, 0.7493306, 0.64873564), "PWM_Nordic_Blend_A137_2", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (11077.227, 4921.238, 1216.922), (-4.726653481599737, 110.05474967155412, 1.774581072728543), (1.542917, 1.542917, 1.258742), "PWM_Nordic_Blend_A138", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (10256.692, 4730.9917, 1046.4929), (-0.8770449197384401, -44.6105982517354, 3.866435036963103), (0.5173075, 0.5173075, 0.59517974), "PWM_Nordic_Blend_A14", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (9653.895, 4218.415, 1027.5221), (1.7212074515384441, -58.54193137566604, -1.7764282144317476), (1.0, 1.0, 0.819568), "PWM_Nordic_Blend_A15", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (9593.7295, 4450.943, 1031.4121), (-1.7996523773613966, 141.8710841594684, 3.8135761221136186), (1.0, 1.0, 0.93210834), "PWM_Nordic_Blend_A16", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (9089.392, 4505.9478, 1201.7438), (1.4437174181958288, 37.517695454846134, -1.8078610806471163), (1.0, 1.0, 0.9182091), "PWM_Nordic_Blend_A17", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (10869.208, 3426.6316, 842.9619), (2.9591587169760594, -143.10034504816525, -1.8870849907926923), (1.0, 1.0, 1.1672304), "PWM_Nordic_Blend_A18", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (11148.364, 5261.6606, 1216.922), (-4.640349699281347, 123.62413621833868, 1.3712172520308896), (1.5429165, 1.5429165, 1.2587419), "PWM_Nordic_Blend_A19", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (7658.253, 780.60614, 859.58325), (6.890049017474931, 170.50511443749517, 7.496623324254983), (1.0, 1.0, 1.0), "PWM_Nordic_Blend_A2_474", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (11121.928, 5824.3086, 1234.0538), (-6.262115952528995, -107.2433858498801, -17.997923277791692), (1.460318, 1.460318, 1.460318), "PWM_Nordic_Blend_A20_81", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (10492.24, 3526.0422, 875.0227), (9.135490570941675, 118.69591018629835, -2.7113333502224997), (1.0, 1.0, 1.16723), "PWM_Nordic_Blend_A21", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (10856.636, 2250.9883, 794.1918), (2.893214594021639, 50.61571919778686, -1.2010498020936726), (1.0, 1.0, 1.16723), "PWM_Nordic_Blend_A22", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (10764.794, 2198.177, 784.0859), (-2.9684450383389756, 45.16540846445979, -0.9172364233746729), (1.0, 1.0, 1.16723), "PWM_Nordic_Blend_A23", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (10734.397, 1457.5146, 832.1214), (0.420541660088759, 125.75573444377592, -3.078216295555147), (1.0, 1.0, 1.16723), "PWM_Nordic_Blend_A24", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (10762.699, 1276.0753, 802.4016), (-2.9524227326636385, -28.817013234170346, 8.55354746966411), (1.0, 1.0, 1.0067286), "PWM_Nordic_Blend_A25_453", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (11451.293, 692.31433, 760.2114), (-0.7328796272303847, 56.67589860294426, -2.190826429648422), (2.344437, 1.9342788, 2.4377668), "PWM_Nordic_Blend_A26", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (11271.814, 1061.5494, 771.0258), (0.6637509007208259, 91.8535122513872, -2.2127686523390233), (1.5740561, 1.934279, 2.437767), "PWM_Nordic_Blend_A27_110", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (6774.002, 854.16156, 1404.3646), (6.94934001038185e-08, 171.1740746401577, -17.24285697317738), (1.1853555, 1.1853555, 1.4757184), "PWM_Nordic_Blend_A28_547", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5563.0244, 1850.6212, 1557.3911), (0.0, -27.020690898113905, 0.0), (1.0, 1.0, 1.0), "PWM_Nordic_Blend_A29_582", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (8374.155, 6814.0596, 828.03705), (0.6315405562483645, 111.4471412197965, -0.2260741537071429), (1.0, 1.0, 0.68221897), "PWM_Nordic_Blend_A3", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5389.8525, 1927.1245, 1549.5599), (-3.7825550732677616e-08, -19.57806301849092, -4.242553064289475), (1.0, 1.0, 1.0), "PWM_Nordic_Blend_A30", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3936.9607, 1766.3967, 906.0338), (0.0, -81.54077301119823, 0.0), (1.0, 1.0, 1.0), "PWM_Nordic_Blend_A31_604", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3567.8828, 407.49982, 800.00037), (0.0, -78.28801654134222, 0.0), (1.0, 1.0, 1.0), "PWM_Nordic_Blend_A32_614", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3523.2195, 1194.6392, 810.1185), (0.0, -79.09378071473118, 0.0), (1.0, 1.0, 1.0), "PWM_Nordic_Blend_A33_617", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2690.142, 1197.2036, 801.0281), (0.0, 118.14076963806507, -0.0), (1.0, 1.0, 1.0), "PWM_Nordic_Blend_A34_637", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1433.4524, 2093.8352, 1121.9464), (3.014845704687134, 148.16087792009273, -0.5200195970450852), (1.0, 1.0, 0.8387953), "PWM_Nordic_Blend_A35_649", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1912.3175, 1560.2385, 1093.5016), (-0.5760496788833699, 148.00086035678413, 6.478486056541836), (1.0, 1.0, 1.0034374), "PWM_Nordic_Blend_A36", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (687.47723, 2725.1802, 800.0032), (0.0, 178.86843097288605, -0.0), (1.0, 1.0, 1.0), "PWM_Nordic_Blend_A37_656", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (880.795, 3271.5432, 759.5124), (2.7159561000826202, -157.32141279476542, -5.801117304514423), (1.0, 1.0, 1.0), "PWM_Nordic_Blend_A38_673", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (651.9914, 3358.0479, 772.2539), (0.3089395525126185, -135.96617797263255, -5.1554857354689325), (1.0, 1.0, 1.0), "PWM_Nordic_Blend_A39", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (8309.966, 6927.8047, 868.10376), (-13.317625864433412, -42.33053299785562, 9.016395903848402), (1.0, 1.0, 1.0), "PWM_Nordic_Blend_A4", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (463.52054, 3391.115, 760.6348), (0.8558095396316732, 5.049255239450973, 4.573041203099657), (1.0, 1.0, 1.0), "PWM_Nordic_Blend_A40", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2336.1765, 3010.2168, 785.24396), (0.0, 0.0, -0.0), (1.0, 1.0, 1.0), "PWM_Nordic_Blend_A41_681", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2679.713, 2963.7625, 733.1976), (-2.8302305671841825, 28.672806871052817, 0.25437493094723285), (1.0, 1.0, 1.0), "PWM_Nordic_Blend_A42", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2011.2604, 3043.205, 776.20715), (-2.8779292848665774, 166.62111248921565, 0.3859944857817756), (1.0, 1.0, 1.0), "PWM_Nordic_Blend_A43_688", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1493.7509, 3344.0823, 1004.2088), (3.1020527743365527, 4.923423192543753, 0.267172674268591), (1.0, 1.0, 1.1300261), "PWM_Nordic_Blend_A44_699", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (8180.625, 7409.4497, 767.7429), (-11.736083379633843, -51.48806840777751, 11.007515350486266), (1.6912503, 1.6912503, 1.6912503), "PWM_Nordic_Blend_A45", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (8115.996, 7963.0527, 788.1022), (-11.736083379633843, -51.48806840777751, 11.007515350486266), (1.69125, 1.69125, 1.3599901), "PWM_Nordic_Blend_A46", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (6490.804, 5902.119, 1134.0034), (0.0, 43.431241039340044, -0.0), (1.0, 1.0, 0.69993097), "PWM_Nordic_Blend_A47_746", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5859.293, 5337.2275, 873.0194), (-0.2326354815877941, 109.55064457987908, -0.01898191902211383), (1.0, 1.0, 1.0), "PWM_Nordic_Blend_A48_753", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (11548.996, 5842.6987, 1464.1687), (4.678741246736839, -109.84039767985817, 3.7068906670770914), (1.460318, 1.460318, 1.2041259), "PWM_Nordic_Blend_A49", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (8573.325, 6041.788, 856.96106), (2.2325221265114727, 13.924132543751057, -0.842101880867331), (1.2106534, 1.2106534, 1.2106534), "PWM_Nordic_Blend_A5", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (11596.098, 6282.609, 1435.8248), (3.827432302385898, -98.09991446791817, 4.580847978264594), (1.460318, 1.460318, 1.204126), "PWM_Nordic_Blend_A50", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5375.381, 4609.1226, 869.36237), (-0.18875118394325466, 119.9191453629216, 0.8485787149698939), (1.0, 1.0, 1.0), "PWM_Nordic_Blend_A51_766", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5298.2256, 4843.0083, 869.3034), (-0.1887511981730458, 119.91914536413896, 0.8485789879670067), (1.0, 1.0, 1.0), "PWM_Nordic_Blend_A52", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5220.829, 5107.2637, 869.38184), (-0.08663932997645848, 113.11001008675247, 0.8650306011481529), (1.0, 1.0, 1.0), "PWM_Nordic_Blend_A53", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (6127.93, 6166.766, 879.53467), (0.0, -84.16895201774037, 0.0), (1.0, 1.0, 1.0), "PWM_Nordic_Blend_A54_826", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (6123.4214, 6541.104, 879.53467), (0.0, -54.05254822282282, 0.0), (1.0, 1.0, 1.0), "PWM_Nordic_Blend_A55", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (6401.2915, 8300.269, 1113.7046), (3.7781583024836025, -144.3973452154497, -0.7714845122076317), (1.0, 1.0, 1.0), "PWM_Nordic_Blend_A56_848", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4378.8213, 7947.289, 818.6942), (-5.565703044174623, 158.92399265755554, 7.998011249259407), (1.0, 1.0, 2.0113852), "PWM_Nordic_Blend_A57_891", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4162.313, 7920.9263, 834.2313), (3.5646818759835126, 72.35223645622472, -5.801635295866928), (1.0, 1.0, 2.0616596), "PWM_Nordic_Blend_A58_902", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4369.4697, 7610.253, 1152.7545), (0.674440197420013, -12.181336117706316, -1.6271667790732187), (1.0, 1.0, 2.0315142), "PWM_Nordic_Blend_A59_908", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (11115.04, 5579.6807, 1229.7411), (0.2328887710613387, -88.00794775658359, -19.020633349938876), (1.4603177, 1.4603177, 1.4603177), "PWM_Nordic_Blend_A6", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5963.7637, 8414.566, 901.7485), (0.0, 0.0, -2.8791503984892897), (1.0, 1.0, 1.0), "PWM_Nordic_Blend_A60_911", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (6268.876, 8694.254, 860.9376), (0.0, -158.08782983250663, 0.0), (1.0, 1.0, 1.0), "PWM_Nordic_Blend_A61_922", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (6055.925, 10176.896, 935.8869), (0.0, -116.7127915813192, 0.0), (1.0, 1.0, 1.0), "PWM_Nordic_Blend_A62_933", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (6334.647, 10344.989, 911.44196), (5.8675556135495555, 6.8226128092605665, 3.981325602583597), (1.5989457, 1.5989457, 2.0121756), "PWM_Nordic_Blend_A63_944", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5311.544, 10280.186, 1141.3193), (0.8420361562750346, 171.5160966452124, -4.096007601984194), (1.0, 1.0, 1.0), "PWM_Nordic_Blend_A64_971", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4582.971, 10370.957, 899.8597), (5.048019430045364e-08, -34.54321443052484, 17.36032620260512), (1.0, 1.0, 1.2398732), "PWM_Nordic_Blend_A65_974", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4532.9053, 10364.949, 924.1126), (0.7585822102747733, -34.178282245463336, 12.948663571144603), (1.0, 1.0, 1.0), "PWM_Nordic_Blend_A66_995", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4880.9517, 10455.668, 1115.8304), (3.1735583178861226, -34.454004801705025, 7.529541390811997), (1.0, 1.0, 1.1206619), "PWM_Nordic_Blend_A67_1002", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3419.6921, 11494.732, 773.63196), (0.0, -110.05782768423623, 0.0), (1.0, 1.0, 0.7890579), "PWM_Nordic_Blend_A68_1007", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4190.34, 11131.517, 1123.3469), (2.3733265569771214, -56.596680960444715, -8.356231561001714), (1.0, 1.0, 1.1880003), "PWM_Nordic_Blend_A69_1019", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (8505.298, 6556.01, 771.13434), (-4.91833563729222, 168.0687389070758, 9.380401200170791), (1.0, 1.0, 1.0), "PWM_Nordic_Blend_A7", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3774.4644, 11224.247, 812.55347), (3.8470149423083586, -82.43671479941712, -1.1832581011939824), (1.0, 1.0, 1.0), "PWM_Nordic_Blend_A70_1022", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2354.6663, 10873.864, 784.3081), (9.163374636312822, 101.88763594681225, -2.7332760136113143), (1.0, 1.0, 1.0), "PWM_Nordic_Blend_A71_1039", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2011.5024, 11333.504, 1111.9049), (0.0, 0.0, -2.0794066847487596), (1.0, 1.0, 1.0), "PWM_Nordic_Blend_A72_1049", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2769.1375, 11863.079, 804.7983), (-7.454387166200941e-09, 67.88894296062135, -1.8230896939110002), (1.0, 1.0, 1.0), "PWM_Nordic_Blend_A73_1060", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4197.439, 11770.4, 1660.8699), (6.306819195431404, -10.356994030119184, -14.73022413444085), (1.0, 1.0, 1.524707), "PWM_Nordic_Blend_A74_1068", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5723.3735, 10604.425, 1417.5707), (-3.5716251009675157, 20.563441177073464, -1.3387756288932757), (1.0, 1.0, 1.2793642), "PWM_Nordic_Blend_A75_1081", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (507.55322, 11689.712, 901.472), (10.195954672848218, 35.050670294546634, -4.712280457579251), (1.0, 1.0, 1.3028798), "PWM_Nordic_Blend_A76_1101", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (398.8453, 11509.215, 800.07245), (3.987935827432608, 16.7153371252793, 0.2877791898985174), (1.0, 1.0, 1.0), "PWM_Nordic_Blend_A77_1104", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1131.1377, 7898.5127, 900.9684), (0.0, 11.426662026055185, -0.0), (1.0, 1.0, 1.2316003), "PWM_Nordic_Blend_A78_1143", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1792.0449, 7906.802, 871.2101), (5.214779250246064, -54.68496869297523, 3.0094637894167364e-06), (1.0, 1.0, 1.4212195), "PWM_Nordic_Blend_A79_1146", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (11137.312, 6160.108, 1215.301), (3.796841340503288, -54.659722450685166, -4.122527623627676), (1.0, 1.0, 1.0), "PWM_Nordic_Blend_A8", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1696.1255, 7767.2056, 983.7731), (9.642215877526052, -144.09691514727913, -0.39178488816475515), (1.0, 1.0, 1.421219), "PWM_Nordic_Blend_A80", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1732.4476, 8377.088, 785.9188), (-13.727751368445915, -35.80661110039797, 8.865009210707937), (0.781694, 1.0, 1.280856), "PWM_Nordic_Blend_A81_1154", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4922.6455, 9832.031, 849.3948), (4.931621505222124, -23.960414760247467, -2.1878355544311896), (1.0, 1.0, 1.0), "PWM_Nordic_Blend_A82_1162", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (7752.1636, 7602.301, 1056.3785), (-11.735687153590593, -51.491147439310836, 25.75521151390024), (1.69125, 1.69125, 1.35999), "PWM_Nordic_Blend_A83", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (8043.524, 7361.585, 950.619), (-33.73395029962888, 17.742034985721528, -2.6037905731210707), (1.69125, 1.69125, 1.35999), "PWM_Nordic_Blend_A84", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (7946.6406, 8436.242, 818.1421), (-12.718812090589886, -21.178589644474567, 2.7228833460218587), (1.69125, 1.69125, 1.35999), "PWM_Nordic_Blend_A85", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (8563.926, 10714.118, 1329.4106), (3.89335054840603, 42.901087210774705, 3.61042953461228), (1.0, 1.0, 1.0), "PWM_Nordic_Blend_A86_1203", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (8593.031, 9505.622, 758.1907), (0.0, -80.34347652217852, 0.0), (1.0, 1.0, 1.0268258), "PWM_Nordic_Blend_A87_1214", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (7680.7637, 9529.425, 852.3634), (-1.7026671768496304, 27.159749601798165, -3.701721238404385), (1.0, 1.0, 1.0), "PWM_Nordic_Blend_A88_1217", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (7593.188, 8905.296, 857.5102), (-11.346219914539569, -11.845243592041198, 2.362852128395769), (1.0, 1.0, 1.0), "PWM_Nordic_Blend_A89_1231", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (8184.684, 6329.7617, 850.4413), (0.8505742118764826, -34.535096907238184, -2.229675162669892), (1.7113295, 1.7113295, 1.7113295), "PWM_Nordic_Blend_A9", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (8467.202, 8876.268, 683.8307), (0.0, -127.37189457085425, 0.0), (1.0, 1.0, 1.0), "PWM_Nordic_Blend_A90", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (7888.962, 8803.347, 799.87274), (-13.03567416786364, -0.27459712175329637, -4.124389480832609), (1.0, 1.0, 1.0), "PWM_Nordic_Blend_A91_1237", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (9941.978, 9962.686, 827.1552), (0.0, 0.0, -5.761749312501342), (0.94899654, 0.94899654, 0.94899654), "PWM_Nordic_Blend_A92_1251", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (11263.286, 9049.029, 789.83264), (0.0, 0.0, -0.0), (1.0, 1.0, 1.0), "PWM_Nordic_Blend_A93_1269", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (10572.175, 4906.164, 1157.4768), (-9.592309288805366e-08, -27.13552871381247, 10.508454688987351), (0.9075714, 0.9075714, 0.66515326), "PWM_Nordic_Blend_A94_1293", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4627.433, 9754.747, 829.3451), (3.0698837184520715, 27.979813546859667, 2.5288794596548794), (1.0, 1.0, 1.0), "PWM_Nordic_Blend_A95", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (6515.394, 9946.265, 872.823), (4.617146414651153, 0.0, -0.0), (1.0, 1.0, 1.0), "PWM_Nordic_Blend_A96_166", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (6201.743, 10021.976, 847.49255), (3.725697395327765, 36.2619292109935, 2.7290116232794985), (1.0, 1.0, 1.0), "PWM_Nordic_Blend_A97", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5943.587, 9867.636, 826.6441), (3.7256969612478272, 36.26192920255144, 2.729011842532928), (1.0, 1.0, 1.0), "PWM_Nordic_Blend_A98", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3241.244, 10899.443, 722.21155), (-0.9789122671496089, -32.55441259992741, -1.5331115755991587), (1.0, 1.0, 1.0), "PWM_Nordic_Blend_A99_171", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5309.378, 3952.2231, 763.3665), (3.792455726304192, 71.04402985807455, -16.366548801144006), (1.1631234, 1.1631234, 1.1631234), "PWM_Nordic_Blend_B101", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (8839.542, 10370.952, 1054.9872), (0.5290323472205228, 11.752597866550708, 3.9366191426635964), (1.4425303, 1.4425303, 1.1423085), "PWM_Nordic_Blend_B107", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (9323.46, 10445.32, 1061.274), (0.33909151679177585, 14.506001337763017, 3.957552174632525), (1.44253, 1.44253, 1.142308), "PWM_Nordic_Blend_B108", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (9541.295, 10277.669, 858.7286), (0.3390919371481319, 14.506001353218949, 3.957552228386671), (1.44253, 1.44253, 1.142308), "PWM_Nordic_Blend_B109", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (9154.974, 9933.024, 792.3413), (0.09318418075146791, 18.055323392455996, 3.9710262955545246), (1.44253, 1.44253, 1.142308), "PWM_Nordic_Blend_B110", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (9499.382, 10045.287, 792.9312), (-0.5516663593228202, 27.368519073488596, 3.933708331227297), (1.44253, 1.44253, 1.142308), "PWM_Nordic_Blend_B111", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (8170.2817, 9818.009, 927.6283), (1.3325631631636847, 29.011957118564244, -10.627502587791941), (1.44253, 1.44253, 1.357917), "PWM_Nordic_Blend_B112", _folder)
if a: placed += 1
else: skipped += 1

# Batch 67: StaticMesh'PWM_Nordic_Blend_B' (109 instances)
_mesh_path = "/Game/Unshippable/Whitebox/Rocks/Meshes/PWM_Nordic_Blend_B"
_materials = ['/Game/Art/Assets/Kits/Misc/Dirt_Mounds/Materials/MI_DirtMound_Cavern']
_folder = "Reconstruction/BD_BB_Chapter3_HeadwaterNexus/Meshes"
a = spawn_static_mesh(_mesh_path, _materials, (9796.725, 3446.9153, 774.3771), (5.778213199291061, 83.0933431264487, 3.632073167446123e-05), (1.0, 1.0, 1.0), "PWM_Nordic_Blend_B_266", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (8403.155, 3960.6182, 691.51843), (4.193203210740742, 85.27648343954951, 19.793273217740595), (1.2748247, 1.2748247, 1.2748247), "PWM_Nordic_Blend_B10", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (6159.436, 2232.2756, 851.1694), (7.090179093233687, 176.6981778440234, -20.605651709298407), (1.1690077, 1.1690077, 1.3596326), "PWM_Nordic_Blend_B100_128", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5143.5537, 5513.4087, 844.8781), (-1.8377686029076354, 124.52305139814757, 5.303684198537663), (1.241917, 1.241917, 0.6044472), "PWM_Nordic_Blend_B102", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5305.592, 5000.619, 826.68317), (2.4469085136885758, 134.10383477274976, 1.0594405036061825), (1.241917, 1.241917, 1.104337), "PWM_Nordic_Blend_B103", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5168.1157, 7321.14, 683.1313), (-9.551574859414842, 148.12184484894829, -8.40740936998553), (1.241917, 1.241917, 1.194621), "PWM_Nordic_Blend_B104", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5896.933, 7523.687, 749.4155), (11.436503098000394, -47.43457314824022, 5.556579228736797), (0.893711, 0.893711, 0.8464149), "PWM_Nordic_Blend_B105", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (6152.8057, 7625.9097, 965.64624), (-6.3797910066964425, 128.26209838910694, 1.6688840910057834), (0.893711, 0.893711, 0.5631672), "PWM_Nordic_Blend_B106", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (11362.776, 4140.12, 1373.9548), (7.587970449517578, -26.496551833876254, -26.819337865739982), (1.0, 1.0, 1.0), "PWM_Nordic_Blend_B11", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (8940.924, 11649.295, 1519.8302), (1.6237887128208084, -16.13867353416542, 1.9592852655128905), (1.0, 0.938816, 0.935462), "PWM_Nordic_Blend_B113", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (9212.235, 11414.4375, 1498.9164), (2.176125414482644, -35.279416429310494, 1.3184899426499064), (1.0, 0.938816, 0.935462), "PWM_Nordic_Blend_B114", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (8625.533, 11692.212, 1512.4928), (-0.8366089227033597, 42.68075423944576, 2.403108495623451), (1.0, 0.938816, 0.935462), "PWM_Nordic_Blend_B115", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (8265.936, 11360.604, 1519.6359), (-2.54360964734692, 112.22935135708879, 0.05623832831228562), (1.0, 0.938816, 0.935462), "PWM_Nordic_Blend_B116", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (12016.893, 3549.629, 826.2508), (0.0, 17.094143086101226, -0.0), (1.0, 1.0, 1.0), "PWM_Nordic_Blend_B12_434", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (11274.965, 1960.3512, 1061.7825), (10.777414975384879, -77.77786023605302, -1.13559037121057), (1.4206145, 1.4206145, 1.4206145), "PWM_Nordic_Blend_B13_445", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (8036.274, 988.62, 598.20825), (0.0, -178.65410071545938, 0.0), (1.0, 1.0, 1.0), "PWM_Nordic_Blend_B14_477", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4813.2427, 3533.2131, 875.03033), (4.237253294456837, 70.88417194311207, -2.354462037007118), (1.1032935, 1.1032935, 1.1032935), "PWM_Nordic_Blend_B15_513", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (6791.047, 4541.299, 891.18787), (1.79004898057257, 3.166149689376806, -0.6105041208437373), (1.1106021, 1.8140656, 2.0583959), "PWM_Nordic_Blend_B16", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4670.8213, 3550.0986, 1003.8667), (3.792454067812615, 71.04407699651594, -18.507812737999835), (1.0, 1.0, 1.0), "PWM_Nordic_Blend_B17_519", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (6344.401, 1545.2692, 1210.4904), (0.0, 139.62455810713533, -0.0), (1.0, 1.0, 1.0), "PWM_Nordic_Blend_B18_544", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (6996.456, 1198.3148, 984.8972), (0.0, -171.61531887683014, 0.0), (1.0, 1.0, 1.0), "PWM_Nordic_Blend_B19_550", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (9404.925, 4640.763, 1026.8518), (-1.1434325649454975, 141.83663042624744, 4.425115422171626), (1.0, 1.0, 1.0), "PWM_Nordic_Blend_B2_272", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3878.1292, 1616.4984, 857.4461), (-2.2601617456022933, -79.32559101358393, 7.8912588907258066), (1.0, 1.0, 1.0), "PWM_Nordic_Blend_B20_601", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3578.2334, 742.0571, 783.5445), (-0.7061156660526421, -49.42840411843505, 3.4295148057153644), (1.0, 1.0, 0.79774874), "PWM_Nordic_Blend_B21_611", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2704.8923, 830.7314, 802.1066), (0.0, 119.83248841725765, -0.0), (1.0, 1.0, 1.0), "PWM_Nordic_Blend_B22_634", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2825.7427, 449.54608, 797.971), (-0.8003846132015761, 119.26877437505236, -6.112884701517121), (1.0, 1.0, 1.0), "PWM_Nordic_Blend_B23", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1449.6031, 2441.7239, 765.8003), (0.0, -170.28943576393178, 0.0), (1.0, 1.0, 1.0), "PWM_Nordic_Blend_B24_641", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2217.884, 2104.567, 770.1784), (0.0, 136.97132735616088, -0.0), (1.0, 1.0, 1.0), "PWM_Nordic_Blend_B25_646", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (903.15265, 2580.7002, 799.99744), (0.0, 173.09498111992795, -0.0), (1.0, 1.0, 1.0), "PWM_Nordic_Blend_B26_653", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (393.9037, 2766.079, 805.5282), (0.0, -175.56891756258293, 0.0), (0.89827627, 0.89827627, 0.89827627), "PWM_Nordic_Blend_B27_660", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2998.6816, 2993.6797, 702.39795), (0.0, -2.757934483181363, 0.0), (1.0, 1.0, 1.0), "PWM_Nordic_Blend_B28_678", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1607.9741, 3075.2073, 800.25964), (-0.31076048915852866, 6.266185804310637, -1.9885557910889684), (1.0, 1.0, 1.0), "PWM_Nordic_Blend_B29_685", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (9332.577, 3616.4421, 770.0045), (-1.8764649016931225, -56.25241030028278, -5.932800114956373), (1.0, 1.0, 1.0), "PWM_Nordic_Blend_B3_281", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2072.6707, 3212.3855, 833.2828), (0.0, 24.272605338472616, -0.0), (1.0, 1.0, 0.77923703), "PWM_Nordic_Blend_B30_692", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1837.6235, 3375.659, 993.6084), (0.0, 25.391831377844536, -0.0), (1.0, 0.9226684, 1.0), "PWM_Nordic_Blend_B31_695", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5040.115, 4595.533, 912.39734), (0.77424966059163, -44.21627893226747, -1.706726077009689), (1.1035482, 1.1035482, 1.1035482), "PWM_Nordic_Blend_B32_716", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (6476.2837, 6537.2666, 1163.3441), (0.0, -38.704254649949185, 0.0), (0.8125232, 0.8125232, 0.8700661), "PWM_Nordic_Blend_B33_743", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (6743.9517, 6146.813, 1170.3444), (-4.7562349619013385e-07, -72.59060572199957, -11.673643902073191), (1.3792219, 1.3792219, 1.3792219), "PWM_Nordic_Blend_B34", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (6051.5454, 5593.541, 872.19855), (3.680690047052623e-08, -72.77521222702092, 1.4424345229195101), (1.0, 1.0, 1.0), "PWM_Nordic_Blend_B35_750", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5131.414, 6167.904, 867.15027), (2.666437326180083, 110.68761984284443, 1.5303947339563655e-06), (1.2419171, 1.2419171, 1.1043371), "PWM_Nordic_Blend_B36_757", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (6764.211, 8344.528, 1110.3062), (0.0, -128.44597789681558, 0.0), (1.0, 1.0, 1.0), "PWM_Nordic_Blend_B37_845", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (6741.893, 8879.2, 853.0104), (-2.3924864737050164, -159.59545831571023, 3.918158418259859), (1.0, 1.0, 0.7777119), "PWM_Nordic_Blend_B38_925", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (6948.0337, 8920.348, 838.5846), (-2.717406741960777, -123.06658160813113, 6.12664815450924), (1.0, 1.0, 1.0284147), "PWM_Nordic_Blend_B39", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (8164.108, 4265.7725, 978.5592), (7.199188759142368, 54.539223005556835, -5.700744719205143), (1.0, 0.8856534, 1.0), "PWM_Nordic_Blend_B4", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5966.737, 10237.849, 917.5566), (0.41791780887833957, 55.04373180801248, 3.5163523405082726), (1.0, 1.0, 1.2924328), "PWM_Nordic_Blend_B40_936", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (7153.842, 10350.548, 1218.6604), (-4.375610345458235, -30.96843974882648, -7.949188025200111), (1.0, 1.0, 1.0), "PWM_Nordic_Blend_B41_939", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (6675.623, 10570.226, 1263.6971), (4.265610273362035, 5.091854282459703, -5.010803689136475), (1.0, 1.0, 1.0), "PWM_Nordic_Blend_B42", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (7174.47, 10517.19, 1296.017), (0.8521136929042074, -17.776364529619585, -9.546600374588696), (1.2827119, 1.2827119, 1.2827119), "PWM_Nordic_Blend_B43", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3725.1604, 10699.487, 687.02277), (0.0, -16.93310658069364, 0.0), (1.0, 1.0, 1.0), "PWM_Nordic_Blend_B44_981", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (9846.66, 3441.0835, 772.28314), (5.7782163982301284, 83.09331780427839, 11.216674227854705), (1.0, 1.0, 1.0), "PWM_Nordic_Blend_B45", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4034.8372, 11168.294, 961.1857), (6.898529367785097, -54.27148971726643, -8.166106740424185), (1.0, 1.0, 1.0), "PWM_Nordic_Blend_B46_1016", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3487.5437, 11768.44, 819.20496), (0.0, -74.4831438772085, 0.0), (1.0, 1.0, 1.0), "PWM_Nordic_Blend_B47_1025", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2603.2134, 11777.932, 823.23193), (0.0, 70.75428589299135, -0.0), (1.0, 1.0, 1.0), "PWM_Nordic_Blend_B48_1036", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2377.3167, 11241.73, 831.69904), (4.749009357204499, 101.43772869512036, 3.1787074497362053), (1.0, 1.0, 1.0), "PWM_Nordic_Blend_B49_1042", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (8649.607, 4397.412, 968.4899), (6.494847592729068, 19.7646115197696, -10.342925002859259), (1.0, 0.885653, 1.0), "PWM_Nordic_Blend_B5", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1694.7288, 11378.98, 1136.9463), (2.4248059044837706, 18.410023100628745, -6.923065189067198), (1.0, 1.0, 1.0), "PWM_Nordic_Blend_B50_1053", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (3494.6165, 12264.729, 814.27496), (-2.1066993527997678e-07, -64.5049152372219, -7.977935446026298), (1.0, 1.0, 1.0), "PWM_Nordic_Blend_B51", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (2817.4038, 12326.333, 750.9195), (-4.681426457728919, 115.72598876679943, 8.78895749839964), (1.0, 1.0, 1.0), "PWM_Nordic_Blend_B52", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5342.253, 10913.986, 1407.6879), (4.2791403283834795, -42.26879799982094, 5.341143555929159), (1.0, 1.0, 0.65967286), "PWM_Nordic_Blend_B53_1077", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4884.878, 11238.3545, 1393.3547), (-2.3798215485320773, 10.448980691330112, -3.7338558880420725), (1.0, 1.0, 0.659673), "PWM_Nordic_Blend_B54", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (4369.676, 9975.767, 675.70844), (0.0, 0.0, 14.485767370738909), (1.0, 1.0, 1.0), "PWM_Nordic_Blend_B55_1084", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1333.9526, 11058.4375, 840.2095), (0.0, -11.067657582554208, 0.0), (1.0, 1.0, 1.0), "PWM_Nordic_Blend_B56_1094", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (584.9122, 11821.812, 943.284), (0.0, 0.0, -5.165405300574128), (1.0, 1.0, 1.5736532), "PWM_Nordic_Blend_B57_1110", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1940.9454, 8250.044, 663.57556), (-1.4994508206228374, 148.87537653668286, 6.024783376724567), (1.0, 1.0, 1.0), "PWM_Nordic_Blend_B58_1120", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (400.4002, 7641.9077, 817.46155), (0.0, -106.48156230124681, 0.0), (1.0, 1.0, 1.0), "PWM_Nordic_Blend_B59_1133", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (8853.803, 4172.279, 830.2153), (8.260949361566905, -7.833008508959995, -4.600524909528348), (1.0, 1.0, 1.0), "PWM_Nordic_Blend_B6", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (1384.5167, 7703.0815, 999.21387), (0.0, -166.91817605909088, 0.0), (1.0, 1.0, 1.0), "PWM_Nordic_Blend_B60_1140", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (7088.3276, 9908.058, 834.3977), (-1.742614879152974, 19.361811712913205, 7.9177251454644475), (1.2698874, 1.1749783, 1.1749783), "PWM_Nordic_Blend_B61_1158", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5501.979, 9847.249, 791.54065), (-5.859618828238729, 45.434458487146024, 8.095338644196678), (1.0, 1.0, 1.0), "PWM_Nordic_Blend_B62", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (7392.727, 9702.716, 845.7482), (-0.7312619985886091, -25.57497841216813, 4.145641195270311), (1.0, 1.0, 1.0), "PWM_Nordic_Blend_B63", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (9009.334, 10160.293, 872.17664), (0.0, 51.30982167355293, -0.0), (1.0, 1.0, 1.0), "PWM_Nordic_Blend_B64_1180", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (8459.823, 10209.123, 1069.8496), (0.0, 84.41741416670851, -0.0), (1.0, 1.0, 1.0), "PWM_Nordic_Blend_B65_1183", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (9338.506, 10526.644, 1065.0656), (-0.4156190379606408, 32.89048434217924, 2.5104168457253446), (1.0, 1.0, 0.9354616), "PWM_Nordic_Blend_B66_1198", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (8875.526, 10440.434, 1057.1436), (-1.0216369506161418, 47.151746250468356, 2.330559048802874), (1.0, 1.0, 0.935462), "PWM_Nordic_Blend_B67", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (9360.967, 10857.811, 1244.6163), (0.5455613852265963, 11.120960788775653, 2.485392647873392), (1.0, 0.9388165, 0.935462), "PWM_Nordic_Blend_B68", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (9123.431, 10834.665, 1241.3517), (-0.9607543278817098, 45.66945945350165, 2.3563056637097053), (1.0, 0.938816, 0.935462), "PWM_Nordic_Blend_B69", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (7708.2056, 3726.101, 916.2033), (0.0, 44.36794324383179, -0.0), (1.0851309, 0.97642785, 1.3144052), "PWM_Nordic_Blend_B7_311", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (8686.452, 9807.89, 771.89703), (-0.024475272971812508, 65.450102572012, 3.707493924097969), (1.0, 1.0, 1.0), "PWM_Nordic_Blend_B70_1208", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (7448.9346, 8970.374, 864.3596), (3.68537528768575, 176.9394451006018, 1.6580998141052715e-07), (0.65878266, 0.65878266, 0.6508417), "PWM_Nordic_Blend_B71_1227", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (10649.243, 10166.141, 1037.1311), (4.997730682348208, 1.0200004429566425, -4.940154677698086), (1.0, 1.0, 1.0), "PWM_Nordic_Blend_B72_1254", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (10309.97, 10220.131, 1044.6631), (13.779517549928988, 20.930479507042588, -11.536161596567908), (0.8913556, 0.8913556, 0.8913556), "PWM_Nordic_Blend_B73", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (10971.255, 10119.157, 1027.3029), (4.275404556378226, 6.30276642061352, -14.135772604285552), (0.891356, 0.891356, 1.30163), "PWM_Nordic_Blend_B74", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (11845.928, 10167.672, 788.72626), (0.0, 46.61458214594914, -0.0), (1.0, 1.0, 1.0), "PWM_Nordic_Blend_B75_1259", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (11396.779, 9924.915, 783.2132), (-1.6398316059587073, 41.554888346851534, 0.14519019331130342), (1.0, 1.0, 1.0), "PWM_Nordic_Blend_B76", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (11513.096, 8961.982, 757.08514), (-0.4896545983694043, -158.3890276000357, 7.242969559205162), (1.0, 1.0, 1.0), "PWM_Nordic_Blend_B77_1265", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (10071.715, 8424.343, 759.9629), (-1.7923573015148256e-08, -117.31940964720573, 4.113077988914226), (1.0, 1.0, 0.82780004), "PWM_Nordic_Blend_B78_1272", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (10955.767, 8578.921, 915.5586), (0.0, -135.65139126774926, 0.0), (1.0, 1.0, 1.1402491), "PWM_Nordic_Blend_B79_1277", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (11238.539, 3630.663, 844.86816), (4.135351896137466, 38.69580143845963, -4.039031800194304), (1.0, 1.0, 1.0), "PWM_Nordic_Blend_B8", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (10393.615, 3863.1243, 967.49744), (-11.469328982029113, -77.40560585138877, 4.138254575648991), (0.6979033, 0.6979033, 0.6979033), "PWM_Nordic_Blend_B80", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (10600.303, 8409.126, 872.3816), (-3.262421022924437, -92.0576759711248, 9.888714843206014), (1.0, 1.0, 1.0257183), "PWM_Nordic_Blend_B81", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (10806.364, 7849.484, 1052.7286), (1.5875408220167058, -76.27398701382027, -0.326690633685294), (1.0, 1.0, 1.025718), "PWM_Nordic_Blend_B82", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (9814.158, 8264.405, 778.4011), (-3.7236937323847634, -135.96175933198487, 1.2003755848611974), (1.0, 1.0, 0.7797655), "PWM_Nordic_Blend_B83_1297", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (5220.653, 6715.0645, 901.79816), (2.666436746212366, 110.68761982007936, 1.0948023648824071e-06), (1.0, 1.0, 1.0), "PWM_Nordic_Blend_B84", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (8069.5728, 9515.668, 800.90656), (-2.261291317149596, 12.072340568849325, 5.922506935947306e-07), (1.0, 1.0, 0.67369056), "PWM_Nordic_Blend_B85_162", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (11860.624, 10042.87, 783.21326), (-1.6398316643325725, 41.554888349611936, 0.14519002404501127), (1.0, 1.0, 1.0), "PWM_Nordic_Blend_B86", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (12074.735, 10130.912, 783.2133), (-1.6398314065785358, -125.5879055151211, 0.14519069514096475), (1.0, 1.0, 1.0), "PWM_Nordic_Blend_B87", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (9245.235, 8191.4507, 744.6923), (-8.30840918255588, -129.10175038017562, 3.6056656731606482), (0.6985043, 0.6985043, 0.29488936), "PWM_Nordic_Blend_B88", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (8788.473, 8717.874, 725.30304), (-3.8591911908373624, 135.9260311636313, 9.084235101280969), (0.7801753, 0.7801753, 0.37656042), "PWM_Nordic_Blend_B89", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (10816.591, 4028.4875, 1107.559), (-5.655853317841392, -85.06477697093293, 5.542279234344809), (0.97761935, 0.97761935, 0.97761935), "PWM_Nordic_Blend_B9", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (8718.501, 8787.845, 708.6958), (4.710548286236408, 13.464477467336696, -6.537566929939497), (0.698504, 0.698504, 0.294889), "PWM_Nordic_Blend_B90", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (9075.789, 9780.916, 796.51746), (2.975851761370883, 60.23039103413496, -0.17364515825825796), (0.698504, 0.698504, 0.294889), "PWM_Nordic_Blend_B91", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (9708.269, 9946.308, 816.5345), (1.982079857010563, 15.224312728536468, -2.226806382658437), (0.7886626, 0.7886626, 0.29974633), "PWM_Nordic_Blend_B92", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (9305.691, 8142.244, 737.81134), (-8.308408983170423, -129.10175032227463, 3.6056652540009884), (0.77923375, 0.698504, 0.4347239), "PWM_Nordic_Blend_B93_21", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (10281.826, 9563.539, 799.27185), (-0.887268077647255, -43.73529161904665, -2.845825247128502), (0.698504, 0.698504, 0.252073), "PWM_Nordic_Blend_B94", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (8664.773, 8635.129, 735.982), (-3.300232212679118, -36.761234150264094, -8.434173777509042), (0.779234, 0.698504, 0.33102763), "PWM_Nordic_Blend_B95", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (12386.457, 10151.239, 788.26776), (-1.466400035054925, -147.52183868877756, 0.7472005482881854), (1.1245124, 1.1245124, 1.1245124), "PWM_Nordic_Blend_B96", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (213.09688, 2722.5745, 805.5282), (0.0, -10.99862533633338, 0.0), (0.898276, 0.898276, 0.898276), "PWM_Nordic_Blend_B97", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (6793.247, 1710.4556, 1031.3181), (0.0, 129.87354078240227, -0.0), (0.3996859, 0.3996859, 0.3996859), "PWM_Nordic_Blend_B98", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (6751.5674, 2030.671, 826.69275), (4.690850415534618, 146.73510886072523, -6.625030510939508), (0.6210402, 0.5936457, 0.7018813), "PWM_Nordic_Blend_B99", _folder)
if a: placed += 1
else: skipped += 1

# Batch 68: StaticMesh'PWM_Quarry_1X1x1_C' (9 instances)
_mesh_path = "/Game/Unshippable/Whitebox/Rocks/Meshes/PWM_Quarry_1X1x1_C"
_materials = ['/Game/Unshippable/Whitebox/Rocks/Materials/PWM_Nordic_Blend_Tileable']
_folder = "Reconstruction/BD_BB_Chapter3_HeadwaterNexus/Meshes"
a = spawn_static_mesh(_mesh_path, _materials, (8945.07, 5808.1187, 957.03906), (-8.964140931059495, -178.71214749200317, -83.95586510694618), (1.7764784, 1.7764784, 1.7764784), "PWM_Quarry_1X1x1_C_72", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (9359.122, 4871.893, 1138.9822), (1.7835188758759815, 8.082884977447431, -94.89439686095123), (1.776478, 1.776478, 1.776478), "PWM_Quarry_1X1x1_C10", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (9029.683, 5935.283, 811.7911), (-8.964140931059495, -178.71214749200317, -83.95586510694618), (1.776478, 1.776478, 1.776478), "PWM_Quarry_1X1x1_C2", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (8770.08, 5821.2197, 2166.5073), (-1.1157524788187088, 166.51710234325432, 79.76393206695163), (1.776478, 1.776478, 1.776478), "PWM_Quarry_1X1x1_C3", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (11202.748, 5639.3794, 1442.4534), (1.4441314139319885, 89.3075283006309, -89.95422546694644), (2.0481973, 2.0481973, 2.0481973), "PWM_Quarry_1X1x1_C4", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (11149.548, 5635.112, 1251.31), (-10.1521919066325, -60.18581836201542, -83.14390342337511), (1.776478, 1.776478, 1.776478), "PWM_Quarry_1X1x1_C5", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (9527.599, 5485.0107, 776.7669), (5.857223567618566, 92.95525914450634, -80.91040630867359), (1.776478, 1.776478, 1.776478), "PWM_Quarry_1X1x1_C7", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (9417.3955, 5122.907, 943.31226), (-20.738857321689412, -114.16385065635919, -95.54111796473887), (1.776478, 1.776478, 1.776478), "PWM_Quarry_1X1x1_C8", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (9350.458, 4774.32, 1055.6527), (-20.738857321689412, -114.16385065635919, -95.54111796473887), (1.776478, 1.776478, 1.776478), "PWM_Quarry_1X1x1_C9", _folder)
if a: placed += 1
else: skipped += 1

# Batch 69: StaticMesh'PWM_Quarry_4x3x10_A' (29 instances)
_mesh_path = "/Game/Unshippable/Whitebox/Rocks/Meshes/PWM_Quarry_4x3x10_A"
_materials = ['/Game/Art/Assets/Landmarks/CrystalDescent/Materials/Rock_Materials/ProcMaterial_Quarry_2m_Nordic']
_folder = "Reconstruction/BD_BB_Chapter3_HeadwaterNexus/Meshes"
a = spawn_static_mesh(_mesh_path, _materials, (7476.5215, 1090.4495, 2212.9724), (0.7343138687939066, 116.17464276428483, 175.04049304104032), (0.844192, 0.844192, 0.844192), "PWM_Quarry_4x3x10_A_60", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (7513.1914, 1310.1271, 810.8899), (7.807861556249694, 51.336967377219835, -6.057495511498884), (0.637462, 0.637462, 0.337869), "PWM_Quarry_4x3x10_A10", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (7549.8843, 1250.7478, 783.4841), (-6.687957906615976, -91.18137155011237, 0.02694707802049716), (0.637462, 0.637462, 0.337869), "PWM_Quarry_4x3x10_A11", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (7339.021, 1009.4144, 1054.8793), (-0.8149717297714844, 149.67226371652245, 2.560088820973606), (0.637462, 0.637462, 0.337869), "PWM_Quarry_4x3x10_A12", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (7300.3213, 1022.7101, 1234.7006), (-0.8149717297714844, 149.67226371652245, 2.560088820973606), (0.637462, 0.637462, 0.5446219), "PWM_Quarry_4x3x10_A13", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (6414.9414, 1837.0387, 2623.887), (-1.8731379957986611, 161.7868783694496, -179.7939807676803), (1.146241, 1.685247, 0.484874), "PWM_Quarry_4x3x10_A14", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (6477.768, 2027.7422, 2621.7327), (-1.8731379957986611, 161.7868783694496, -179.7939807676803), (1.146241, 1.685247, 0.484874), "PWM_Quarry_4x3x10_A15", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (6327.954, 2100.4968, 2195.0042), (2.2469784819256757, -176.3420792984572, 176.1368303850011), (0.6151935, 0.6151935, 0.6151935), "PWM_Quarry_4x3x10_A16", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (6351.3223, 1926.0109, 2274.3906), (2.833526535231615, 95.13900166181435, 177.27612356179887), (0.615193, 0.615193, 0.615193), "PWM_Quarry_4x3x10_A17", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (6369.666, 1943.1682, 2360.695), (-0.5722656285158334, 128.30470566960406, 179.26630286326144), (0.615193, 0.8951471, 0.615193), "PWM_Quarry_4x3x10_A18", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (6412.712, 1795.3312, 2513.6472), (5.841856486927607, 121.3320956779941, 178.80458561234127), (0.615193, 0.895147, 0.615193), "PWM_Quarry_4x3x10_A19", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (7247.8394, 1078.4167, 2329.6892), (-5.8300150044018855, 128.05862583508986, 178.67984493852535), (0.844192, 0.844192, 0.99476206), "PWM_Quarry_4x3x10_A2", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (6186.4814, 2138.6084, 2471.053), (2.2469784819256757, -176.3420792984572, 176.1368303850011), (0.615193, 0.6913739, 0.615193), "PWM_Quarry_4x3x10_A20", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (7281.049, 1175.9633, 1112.9586), (-4.81802349943609, -5.5097045986909325, -7.731598379039332), (0.637462, 0.637462, 0.5332893), "PWM_Quarry_4x3x10_A21", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (7156.6733, 1158.1239, 1079.992), (-3.4471436490930287, 4.148698316780737, -8.429504177000767), (0.637462, 0.637462, 0.41423473), "PWM_Quarry_4x3x10_A22", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (6401.316, 2037.9255, 2342.909), (3.4861145224142858, 166.56112478848152, -178.1854845150957), (0.615193, 0.895147, 0.615193), "PWM_Quarry_4x3x10_A23", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (6532.253, 1999.2051, 2529.6948), (3.4861145224142858, 166.56112478848152, -178.1854845150957), (0.615193, 0.895147, 0.615193), "PWM_Quarry_4x3x10_A24", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (6359.6562, 2286.2385, 2509.2742), (0.0538327856199266, -131.74135604208996, -176.0707232114781), (0.615193, 0.895147, 0.615193), "PWM_Quarry_4x3x10_A25", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (6421.929, 2180.4744, 2497.551), (0.0538327856199266, -131.74135604208996, -176.0707232114781), (0.615193, 0.895147, 0.615193), "PWM_Quarry_4x3x10_A26", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (6314.922, 1829.5005, 1141.251), (0.7273863009768351, -166.97794137490322, 3.1450799135428644), (0.637462, 0.637462, 0.533289), "PWM_Quarry_4x3x10_A27", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (6483.0293, 2148.546, 869.65674), (-2.2485962126335646, -18.093534104033296, -2.316497806814615), (0.7322923, 0.69377345, 0.533289), "PWM_Quarry_4x3x10_A29", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (7151.162, 1046.1675, 2397.1104), (-1.7702632388004658, -171.89300590351752, 174.29010319617646), (1.1462408, 1.6852471, 0.48487377), "PWM_Quarry_4x3x10_A3", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (6484.6104, 2218.0078, 735.317), (-2.2485962126335646, -18.093534104033296, -2.316497806814615), (0.637462, 0.637462, 0.44675568), "PWM_Quarry_4x3x10_A30", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (6525.984, 2161.1511, 819.29364), (-3.0650634929162552, -82.26084409231034, 1.0126041285090024), (0.6621242, 0.7135737, 0.446756), "PWM_Quarry_4x3x10_A31", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (7652.1826, 1078.0225, 2400.9546), (-0.8851621939576376, 97.62856740232844, 175.06491066018785), (0.95099956, 1.0558724, 0.6432655), "PWM_Quarry_4x3x10_A4", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (7583.8896, 947.6487, 2227.1462), (0.7343138687939066, 116.17464276428483, 175.04049304104032), (0.844192, 1.1285309, 0.844192), "PWM_Quarry_4x3x10_A5", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (7827.3447, 1229.4135, 2370.816), (2.8182062232453817, 141.90588053604696, 175.85174104580005), (0.90506804, 0.90506804, 0.46801627), "PWM_Quarry_4x3x10_A6", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (7884.113, 1002.1004, 2268.6875), (-3.5826416310259774, 69.87856195549799, 172.87289729240666), (0.905068, 0.905068, 0.468016), "PWM_Quarry_4x3x10_A7", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_mesh_path, _materials, (8041.136, 1184.0593, 2377.8125), (5.671052503433194, -128.72176013198862, -174.3866476046758), (0.905068, 0.905068, 0.468016), "PWM_Quarry_4x3x10_A8", _folder)
if a: placed += 1
else: skipped += 1

# ======================================================================
# PHASE 2: ConstructionCatalog  (construction blocks)
# ======================================================================
unreal.log(f"[{BUBBLE_NAME}] Phase 2: Placing construction blocks...")

# Construction blocks use DecoVolume transforms (matched by Name)
_folder = "Reconstruction/BD_BB_Chapter3_HeadwaterNexus/Construction"

# Construction: BP_Column_1x2m_A_Base30_3
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Stone
#   Volume: EMorSimpleShape::Capsule, BoxExtent: (100.0, 100.0, 100.0)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (3603.295, 7482.3896, 975.0), (-0.0, -89.999565495937, -0.0), (2.0000, 2.0000, 2.0000), "BP_Column_1x2m_A_Base30_3", _folder)
if a: placed += 1
else: skipped += 1

# Construction: BP_Column_1x2m_A_Base33
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Stone
#   Volume: EMorSimpleShape::Capsule, BoxExtent: (100.0, 100.0, 100.0)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (3013.295, 7882.3896, 975.0), (-0.0, -89.999565495937, -0.0), (2.0000, 2.0000, 2.0000), "BP_Column_1x2m_A_Base33", _folder)
if a: placed += 1
else: skipped += 1

# Construction: BP_Column_1x2m_A_Base34
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Stone
#   Volume: EMorSimpleShape::Capsule, BoxExtent: (100.0, 100.0, 100.0)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (3603.295, 6682.3896, 975.0), (-0.0, -89.999565495937, -0.0), (2.0000, 2.0000, 2.0000), "BP_Column_1x2m_A_Base34", _folder)
if a: placed += 1
else: skipped += 1

# Construction: BP_Column_1x2m_A_Base36
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Stone
#   Volume: EMorSimpleShape::Capsule, BoxExtent: (100.0, 100.0, 100.0)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (3003.295, 7492.3896, 975.0), (-0.0, -89.999565495937, -0.0), (2.0000, 2.0000, 2.0000), "BP_Column_1x2m_A_Base36", _folder)
if a: placed += 1
else: skipped += 1

# Construction: BP_Column_1x2m_A_Base37
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Stone
#   Volume: EMorSimpleShape::Capsule, BoxExtent: (100.0, 100.0, 100.0)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (2383.295, 7882.3896, 975.0), (-0.0, -89.999565495937, -0.0), (2.0000, 2.0000, 2.0000), "BP_Column_1x2m_A_Base37", _folder)
if a: placed += 1
else: skipped += 1

# Construction: BP_Column_1x2m_A_Base38_5
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Stone
#   Volume: EMorSimpleShape::Capsule, BoxExtent: (100.0, 100.0, 100.0)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (2423.295, 6687.3896, 975.0), (-0.0, -89.999565495937, -0.0), (2.0000, 2.0000, 2.0000), "BP_Column_1x2m_A_Base38_5", _folder)
if a: placed += 1
else: skipped += 1

# Construction: BP_Column_1x2m_A_Base39
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Stone
#   Volume: EMorSimpleShape::Capsule, BoxExtent: (100.0, 100.0, 100.0)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (3003.295, 6882.3896, 975.0), (-0.0, -89.999565495937, -0.0), (2.0000, 2.0000, 2.0000), "BP_Column_1x2m_A_Base39", _folder)
if a: placed += 1
else: skipped += 1

# Construction: BP_Column_1x2m_A_Shaft55_8
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Stone
#   Volume: EMorSimpleShape::Capsule, BoxExtent: (100.0, 100.0, 100.0)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (3603.295, 7482.3896, 1180.0), (-0.0, -89.99975996369572, -0.0), (2.0000, 2.0000, 2.0000), "BP_Column_1x2m_A_Shaft55_8", _folder)
if a: placed += 1
else: skipped += 1

# Construction: BP_Column_1x2m_A_Shaft56
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Stone
#   Volume: EMorSimpleShape::Capsule, BoxExtent: (100.0, 100.0, 100.0)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (3603.295, 7482.3896, 1380.0), (-0.0, -89.99975996369572, -0.0), (2.0000, 2.0000, 2.0000), "BP_Column_1x2m_A_Shaft56", _folder)
if a: placed += 1
else: skipped += 1

# Construction: BP_Column_1x2m_A_Shaft57
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Stone
#   Volume: EMorSimpleShape::Capsule, BoxExtent: (100.0, 100.0, 100.0)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (3603.295, 7482.3896, 1580.0), (-0.0, -89.99975996369572, -0.0), (2.0000, 2.0000, 2.0000), "BP_Column_1x2m_A_Shaft57", _folder)
if a: placed += 1
else: skipped += 1

# Construction: BP_Column_1x2m_A_Shaft58
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Stone
#   Volume: EMorSimpleShape::Capsule, BoxExtent: (100.0, 100.0, 100.0)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (3013.295, 7882.3896, 1180.0), (-0.0, -89.99975996369572, -0.0), (2.0000, 2.0000, 2.0000), "BP_Column_1x2m_A_Shaft58", _folder)
if a: placed += 1
else: skipped += 1

# Construction: BP_Column_1x2m_A_Shaft59
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Stone
#   Volume: EMorSimpleShape::Capsule, BoxExtent: (100.0, 100.0, 100.0)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (3013.295, 7882.3896, 1380.0), (-0.0, -89.99975996369572, -0.0), (2.0000, 2.0000, 2.0000), "BP_Column_1x2m_A_Shaft59", _folder)
if a: placed += 1
else: skipped += 1

# Construction: BP_Column_1x2m_A_Shaft60
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Stone
#   Volume: EMorSimpleShape::Capsule, BoxExtent: (100.0, 100.0, 100.0)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (3013.295, 7882.3896, 1580.0), (-0.0, -89.99975996369572, -0.0), (2.0000, 2.0000, 2.0000), "BP_Column_1x2m_A_Shaft60", _folder)
if a: placed += 1
else: skipped += 1

# Construction: BP_Column_1x2m_A_Shaft61
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Stone
#   Volume: EMorSimpleShape::Capsule, BoxExtent: (100.0, 100.0, 100.0)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (3003.295, 7492.3896, 1180.0), (-0.0, -89.99975996369572, -0.0), (2.0000, 2.0000, 2.0000), "BP_Column_1x2m_A_Shaft61", _folder)
if a: placed += 1
else: skipped += 1

# Construction: BP_Column_1x2m_A_Shaft62
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Stone
#   Volume: EMorSimpleShape::Capsule, BoxExtent: (100.0, 100.0, 100.0)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (3603.295, 6682.3896, 1180.0), (-0.0, -89.99975996369572, -0.0), (2.0000, 2.0000, 2.0000), "BP_Column_1x2m_A_Shaft62", _folder)
if a: placed += 1
else: skipped += 1

# Construction: BP_Column_1x2m_A_Shaft63
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Stone
#   Volume: EMorSimpleShape::Capsule, BoxExtent: (100.0, 100.0, 100.0)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (3603.295, 6682.3896, 1380.0), (-0.0, -89.99975996369572, -0.0), (2.0000, 2.0000, 2.0000), "BP_Column_1x2m_A_Shaft63", _folder)
if a: placed += 1
else: skipped += 1

# Construction: BP_Column_1x2m_A_Shaft64
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Stone
#   Volume: EMorSimpleShape::Capsule, BoxExtent: (100.0, 100.0, 100.0)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (3603.295, 6682.3896, 1580.0), (-0.0, -89.99975996369572, -0.0), (2.0000, 2.0000, 2.0000), "BP_Column_1x2m_A_Shaft64", _folder)
if a: placed += 1
else: skipped += 1

# Construction: BP_Column_1x2m_A_Shaft65
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Stone
#   Volume: EMorSimpleShape::Capsule, BoxExtent: (100.0, 100.0, 100.0)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (3603.295, 6682.3896, 1760.0), (-0.0, -89.99975996369572, -0.0), (2.0000, 2.0000, 2.0000), "BP_Column_1x2m_A_Shaft65", _folder)
if a: placed += 1
else: skipped += 1

# Construction: BP_Column_1x2m_A_Shaft66
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Stone
#   Volume: EMorSimpleShape::Capsule, BoxExtent: (100.0, 100.0, 100.0)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (3603.295, 6682.3896, 1960.0), (-0.0, -89.99975996369572, -0.0), (2.0000, 2.0000, 2.0000), "BP_Column_1x2m_A_Shaft66", _folder)
if a: placed += 1
else: skipped += 1

# Construction: BP_Column_1x2m_A_Shaft69
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Stone
#   Volume: EMorSimpleShape::Capsule, BoxExtent: (100.0, 100.0, 100.0)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (3003.295, 6882.3896, 1180.0), (-0.0, -89.99975996369572, -0.0), (2.0000, 2.0000, 2.0000), "BP_Column_1x2m_A_Shaft69", _folder)
if a: placed += 1
else: skipped += 1

# Construction: BP_Column_1x2m_A_Shaft70
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Stone
#   Volume: EMorSimpleShape::Capsule, BoxExtent: (100.0, 100.0, 100.0)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (2383.295, 7882.3896, 1180.0), (-0.0, -89.99975996369572, -0.0), (2.0000, 2.0000, 2.0000), "BP_Column_1x2m_A_Shaft70", _folder)
if a: placed += 1
else: skipped += 1

# Construction: BP_Column_1x2m_A_Shaft71
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Stone
#   Volume: EMorSimpleShape::Capsule, BoxExtent: (100.0, 100.0, 100.0)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (2383.295, 7882.3896, 1380.0), (-0.0, -89.99975996369572, -0.0), (2.0000, 2.0000, 2.0000), "BP_Column_1x2m_A_Shaft71", _folder)
if a: placed += 1
else: skipped += 1

# Construction: BP_Column_1x2m_A_Shaft72
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Stone
#   Volume: EMorSimpleShape::Capsule, BoxExtent: (100.0, 100.0, 100.0)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (2383.295, 7882.3896, 1580.0), (-0.0, -89.99975996369572, -0.0), (2.0000, 2.0000, 2.0000), "BP_Column_1x2m_A_Shaft72", _folder)
if a: placed += 1
else: skipped += 1

# Construction: BP_Column_1x2m_A_Shaft73
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Stone
#   Volume: EMorSimpleShape::Capsule, BoxExtent: (100.0, 100.0, 100.0)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (2383.295, 7882.3896, 1780.0), (-0.0, -89.99975996369572, -0.0), (2.0000, 2.0000, 2.0000), "BP_Column_1x2m_A_Shaft73", _folder)
if a: placed += 1
else: skipped += 1

# Construction: BP_Column_1x2m_A_Shaft74_16
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Stone
#   Volume: EMorSimpleShape::Capsule, BoxExtent: (100.0, 100.0, 100.0)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (2423.295, 6687.3896, 1180.0), (-0.0, -89.99975996369572, -0.0), (2.0000, 2.0000, 2.0000), "BP_Column_1x2m_A_Shaft74_16", _folder)
if a: placed += 1
else: skipped += 1

# Construction: BP_Column_1x2m_A_Shaft75
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Stone
#   Volume: EMorSimpleShape::Capsule, BoxExtent: (100.0, 100.0, 100.0)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (2423.295, 6687.3896, 1380.0), (-0.0, -89.99975996369572, -0.0), (2.0000, 2.0000, 2.0000), "BP_Column_1x2m_A_Shaft75", _folder)
if a: placed += 1
else: skipped += 1

# Construction: BP_Column_1x2m_A_Shaft76
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Stone
#   Volume: EMorSimpleShape::Capsule, BoxExtent: (100.0, 100.0, 100.0)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (2423.295, 6687.3896, 1580.0), (-0.0, -89.99975996369572, -0.0), (2.0000, 2.0000, 2.0000), "BP_Column_1x2m_A_Shaft76", _folder)
if a: placed += 1
else: skipped += 1

# Construction: BP_Column_1x2m_A_Shaft77
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Stone
#   Volume: EMorSimpleShape::Capsule, BoxExtent: (100.0, 100.0, 100.0)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (2423.295, 6687.3896, 1780.0), (-0.0, -89.99975996369572, -0.0), (2.0000, 2.0000, 2.0000), "BP_Column_1x2m_A_Shaft77", _folder)
if a: placed += 1
else: skipped += 1

# Construction: BP_Column_1x2m_A_Shaft78
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Stone
#   Volume: EMorSimpleShape::Capsule, BoxExtent: (100.0, 100.0, 100.0)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (2423.295, 6687.3896, 1980.0), (-0.0, -89.99975996369572, -0.0), (2.0000, 2.0000, 2.0000), "BP_Column_1x2m_A_Shaft78", _folder)
if a: placed += 1
else: skipped += 1

# Construction: BP_Column_1x2m_A_Shaft79
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Stone
#   Volume: EMorSimpleShape::Capsule, BoxExtent: (100.0, 100.0, 100.0)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (2423.295, 6687.3896, 2180.0), (-0.0, -89.99975996369572, -0.0), (2.0000, 2.0000, 2.0000), "BP_Column_1x2m_A_Shaft79", _folder)
if a: placed += 1
else: skipped += 1

# Construction: BP_Floor_Stone_100x100x020_A_Breakable_1
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Advanced
#   Volume: EMorSimpleShape::Empty, BoxExtent: (100.0, 100.0, 100.0)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (3453.2988, 6732.3896, 1085.0), (-0.0, -89.99975996369572, -0.0), (2.0000, 2.0000, 2.0000), "BP_Floor_Stone_100x100x020_A_Breakable_1", _folder)
if a: placed += 1
else: skipped += 1

# Construction: BP_Floor_Stone_100x100x020_A_Breakable2
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Advanced
#   Volume: EMorSimpleShape::Empty, BoxExtent: (100.0, 100.0, 100.0)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (3453.2988, 6832.3896, 1085.0), (-0.0, -89.99975996369572, -0.0), (2.0000, 2.0000, 2.0000), "BP_Floor_Stone_100x100x020_A_Breakable2", _folder)
if a: placed += 1
else: skipped += 1

# Construction: BP_Floor_Stone_100x100x020_A_Breakable3
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Advanced
#   Volume: EMorSimpleShape::Empty, BoxExtent: (100.0, 100.0, 100.0)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (3553.2988, 6732.3896, 1085.0), (-0.0, -89.99975996369572, -0.0), (2.0000, 2.0000, 2.0000), "BP_Floor_Stone_100x100x020_A_Breakable3", _folder)
if a: placed += 1
else: skipped += 1

# Construction: BP_Floor_Stone_100x100x020_A_Breakable4
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Advanced
#   Volume: EMorSimpleShape::Empty, BoxExtent: (100.0, 100.0, 100.0)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (3553.2988, 6832.3896, 1085.0), (-0.0, -89.99975996369572, -0.0), (2.0000, 2.0000, 2.0000), "BP_Floor_Stone_100x100x020_A_Breakable4", _folder)
if a: placed += 1
else: skipped += 1

# Construction: BP_Floor_Stone_3x3m_A28_0
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Advanced
#   Volume: EMorSimpleShape::Empty, BoxExtent: (100.0, 100.0, 100.0)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (2853.2961, 7732.3887, 1580.0), (-0.0, -89.99975996369572, -0.0), (2.0000, 2.0000, 2.0000), "BP_Floor_Stone_3x3m_A28_0", _folder)
if a: placed += 1
else: skipped += 1

# Construction: BP_Floor_Stone_3x3m_A29
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Advanced
#   Volume: EMorSimpleShape::Empty, BoxExtent: (100.0, 100.0, 100.0)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (2553.2961, 7732.3887, 1580.0), (-0.0, -89.99975996369572, -0.0), (2.0000, 2.0000, 2.0000), "BP_Floor_Stone_3x3m_A29", _folder)
if a: placed += 1
else: skipped += 1

# Construction: BP_Floor_Stone_3x3m_A34_6
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Advanced
#   Volume: EMorSimpleShape::Empty, BoxExtent: (100.0, 100.0, 100.0)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (2853.2961, 7732.3887, 1280.0), (-0.0, -89.99975996369572, -0.0), (2.0000, 2.0000, 2.0000), "BP_Floor_Stone_3x3m_A34_6", _folder)
if a: placed += 1
else: skipped += 1

# Construction: BP_Floor_Stone_3x3m_A35
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Advanced
#   Volume: EMorSimpleShape::Empty, BoxExtent: (100.0, 100.0, 100.0)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (2553.2961, 7732.3887, 1280.0), (-0.0, -89.99975996369572, -0.0), (2.0000, 2.0000, 2.0000), "BP_Floor_Stone_3x3m_A35", _folder)
if a: placed += 1
else: skipped += 1

# Construction: BP_Floor_Stone_3x3m_A36
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Advanced
#   Volume: EMorSimpleShape::Empty, BoxExtent: (100.0, 100.0, 100.0)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (2853.2961, 7432.3887, 1280.0), (-0.0, -89.99975996369572, -0.0), (2.0000, 2.0000, 2.0000), "BP_Floor_Stone_3x3m_A36", _folder)
if a: placed += 1
else: skipped += 1

# Construction: BP_Floor_Stone_3x3m_A37
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Advanced
#   Volume: EMorSimpleShape::Empty, BoxExtent: (100.0, 100.0, 100.0)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (2553.2961, 7432.3887, 1280.0), (-0.0, -89.99975996369572, -0.0), (2.0000, 2.0000, 2.0000), "BP_Floor_Stone_3x3m_A37", _folder)
if a: placed += 1
else: skipped += 1

# Construction: BP_Floor_Stone_3x3m_A38
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Advanced
#   Volume: EMorSimpleShape::Empty, BoxExtent: (100.0, 100.0, 100.0)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (2853.2961, 7132.3887, 1280.0), (-0.0, -89.99975996369572, -0.0), (2.0000, 2.0000, 2.0000), "BP_Floor_Stone_3x3m_A38", _folder)
if a: placed += 1
else: skipped += 1

# Construction: BP_Floor_Stone_3x3m_A39
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Advanced
#   Volume: EMorSimpleShape::Empty, BoxExtent: (100.0, 100.0, 100.0)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (2553.2961, 7132.3887, 1280.0), (-0.0, -89.99975996369572, -0.0), (2.0000, 2.0000, 2.0000), "BP_Floor_Stone_3x3m_A39", _folder)
if a: placed += 1
else: skipped += 1

# Construction: BP_Floor_Stone_3x3m_A40
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Advanced
#   Volume: EMorSimpleShape::Empty, BoxExtent: (100.0, 100.0, 100.0)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (2853.2961, 6832.3887, 1280.0), (-0.0, -89.99975996369572, -0.0), (2.0000, 2.0000, 2.0000), "BP_Floor_Stone_3x3m_A40", _folder)
if a: placed += 1
else: skipped += 1

# Construction: BP_Floor_Stone_3x3m_A41
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Advanced
#   Volume: EMorSimpleShape::Empty, BoxExtent: (100.0, 100.0, 100.0)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (2553.2961, 6832.3887, 1280.0), (-0.0, -89.99975996369572, -0.0), (2.0000, 2.0000, 2.0000), "BP_Floor_Stone_3x3m_A41", _folder)
if a: placed += 1
else: skipped += 1

# Construction: BP_Floor_Stone_3x3m_A42
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Advanced
#   Volume: EMorSimpleShape::Empty, BoxExtent: (100.0, 100.0, 100.0)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (3453.2961, 7332.3887, 1280.0), (-0.0, -89.99975996369572, -0.0), (2.0000, 2.0000, 2.0000), "BP_Floor_Stone_3x3m_A42", _folder)
if a: placed += 1
else: skipped += 1

# Construction: BP_Floor_Stone_3x3m_A43
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Advanced
#   Volume: EMorSimpleShape::Empty, BoxExtent: (100.0, 100.0, 100.0)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (3153.2961, 7332.3887, 1280.0), (-0.0, -89.99975996369572, -0.0), (2.0000, 2.0000, 2.0000), "BP_Floor_Stone_3x3m_A43", _folder)
if a: placed += 1
else: skipped += 1

# Construction: BP_Floor_Stone_3x3m_A44
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Advanced
#   Volume: EMorSimpleShape::Empty, BoxExtent: (100.0, 100.0, 100.0)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (3453.2961, 7332.3887, 1260.0), (-0.0, -89.99975996369572, -0.0), (2.0000, 2.0000, 2.0000), "BP_Floor_Stone_3x3m_A44", _folder)
if a: placed += 1
else: skipped += 1

# Construction: BP_Floor_Stone_3x3m_A45
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Advanced
#   Volume: EMorSimpleShape::Empty, BoxExtent: (100.0, 100.0, 100.0)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (3153.2961, 7332.3887, 1260.0), (-0.0, -89.99975996369572, -0.0), (2.0000, 2.0000, 2.0000), "BP_Floor_Stone_3x3m_A45", _folder)
if a: placed += 1
else: skipped += 1

# Construction: BP_Foundation_Stone_6x6x6m_A10
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Stone
#   Volume: EMorSimpleShape::OrientedBox, BoxExtent: (301.0, 301.0, 301.0)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (2450.0, 7050.0, 580.0), (0.0, 0.0, -0.0), (6.0200, 6.0200, 6.0200), "BP_Foundation_Stone_6x6x6m_A10", _folder)
if a: placed += 1
else: skipped += 1

# Construction: BP_Foundation_Stone_6x6x6m_A11
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Stone
#   Volume: EMorSimpleShape::OrientedBox, BoxExtent: (301.0, 301.0, 301.0)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (3050.0, 7050.0, 580.0), (0.0, 0.0, -0.0), (6.0200, 6.0200, 6.0200), "BP_Foundation_Stone_6x6x6m_A11", _folder)
if a: placed += 1
else: skipped += 1

# Construction: BP_Foundation_Stone_6x6x6m_A12
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Stone
#   Volume: EMorSimpleShape::OrientedBox, BoxExtent: (301.0, 301.0, 301.0)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (3650.0, 7050.0, 580.0), (0.0, 0.0, -0.0), (6.0200, 6.0200, 6.0200), "BP_Foundation_Stone_6x6x6m_A12", _folder)
if a: placed += 1
else: skipped += 1

# Construction: BP_Foundation_Stone_6x6x6m_A13
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Stone
#   Volume: EMorSimpleShape::OrientedBox, BoxExtent: (301.0, 301.0, 301.0)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (2450.0, 6450.0, 580.0), (0.0, 0.0, -0.0), (6.0200, 6.0200, 6.0200), "BP_Foundation_Stone_6x6x6m_A13", _folder)
if a: placed += 1
else: skipped += 1

# Construction: BP_Foundation_Stone_6x6x6m_A14
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Stone
#   Volume: EMorSimpleShape::OrientedBox, BoxExtent: (301.0, 301.0, 301.0)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (3050.0, 6450.0, 580.0), (0.0, 0.0, -0.0), (6.0200, 6.0200, 6.0200), "BP_Foundation_Stone_6x6x6m_A14", _folder)
if a: placed += 1
else: skipped += 1

# Construction: BP_Foundation_Stone_6x6x6m_A15
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Stone
#   Volume: EMorSimpleShape::OrientedBox, BoxExtent: (301.0, 301.0, 301.0)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (3650.0, 6450.0, 580.0), (0.0, 0.0, -0.0), (6.0200, 6.0200, 6.0200), "BP_Foundation_Stone_6x6x6m_A15", _folder)
if a: placed += 1
else: skipped += 1

# Construction: BP_Foundation_Stone_6x6x6m_A5_6
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Stone
#   Volume: EMorSimpleShape::OrientedBox, BoxExtent: (301.0, 301.0, 301.0)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (2450.0, 7650.0, 580.0), (0.0, 0.0, -0.0), (6.0200, 6.0200, 6.0200), "BP_Foundation_Stone_6x6x6m_A5_6", _folder)
if a: placed += 1
else: skipped += 1

# Construction: BP_Foundation_Stone_6x6x6m_A6
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Stone
#   Volume: EMorSimpleShape::OrientedBox, BoxExtent: (301.0, 301.0, 301.0)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (3050.0, 7650.0, 580.0), (0.0, 0.0, -0.0), (6.0200, 6.0200, 6.0200), "BP_Foundation_Stone_6x6x6m_A6", _folder)
if a: placed += 1
else: skipped += 1

# Construction: BP_Foundation_Stone_6x6x6m_A7
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Stone
#   Volume: EMorSimpleShape::OrientedBox, BoxExtent: (301.0, 301.0, 301.0)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (3650.0, 7650.0, 580.0), (0.0, 0.0, -0.0), (6.0200, 6.0200, 6.0200), "BP_Foundation_Stone_6x6x6m_A7", _folder)
if a: placed += 1
else: skipped += 1

# Construction: BP_Foundation_Stone_6x6x6m_A8_14
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Stone
#   Volume: EMorSimpleShape::OrientedBox, BoxExtent: (348.7, 348.7, 301.0)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (1789.7064, 10298.443, 465.35352), (0.0, 0.0, -0.0), (6.9739, 6.9739, 6.0200), "BP_Foundation_Stone_6x6x6m_A8_14", _folder)
if a: placed += 1
else: skipped += 1

# Construction: BP_Foundation_Stone_6x6x6m_A9_16
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Stone
#   Volume: EMorSimpleShape::OrientedBox, BoxExtent: (348.7, 348.7, 301.0)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (2380.5906, 10402.634, 465.35352), (0.0, 0.0, -0.0), (6.9739, 6.9739, 6.0200), "BP_Foundation_Stone_6x6x6m_A9_16", _folder)
if a: placed += 1
else: skipped += 1

# Construction: BP_Ruin_Wall_Thick_1x1m_B_Breakable_2
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Stone
#   Volume: EMorSimpleShape::OrientedBox, BoxExtent: (65.1, 62.0, 54.4)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (5941.5757, 9908.369, 949.94867), (0.0, 0.0, -0.0), (1.3021, 1.2396, 1.0871), "BP_Ruin_Wall_Thick_1x1m_B_Breakable_2", _folder)
if a: placed += 1
else: skipped += 1

# Construction: BP_Ruin_Wall_Thick_1x1m_B_Breakable4
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Stone
#   Volume: EMorSimpleShape::OrientedBox, BoxExtent: (71.2, 70.5, 52.7)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (9059.631, 5382.1353, 752.4792), (0.0, 0.0, -0.0), (1.4243, 1.4092, 1.0543), "BP_Ruin_Wall_Thick_1x1m_B_Breakable4", _folder)
if a: placed += 1
else: skipped += 1

# Construction: BP_Ruin_Wall_Thick_1x1m_B_Breakable5
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Stone
#   Volume: EMorSimpleShape::OrientedBox, BoxExtent: (71.9, 71.4, 52.7)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (6261.484, 4405.7563, 1213.7052), (0.0, 0.0, -0.0), (1.4376, 1.4277, 1.0542), "BP_Ruin_Wall_Thick_1x1m_B_Breakable5", _folder)
if a: placed += 1
else: skipped += 1

# Construction: BP_Ruin_Wall_Thick_1x2m_B_Breakable_3
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Stone
#   Volume: EMorSimpleShape::OrientedBox, BoxExtent: (105.7, 69.3, 49.3)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (1844.9, 10561.38, 813.0976), (0.0, 0.0, -0.0), (2.1146, 1.3866, 0.9852), "BP_Ruin_Wall_Thick_1x2m_B_Breakable_3", _folder)
if a: placed += 1
else: skipped += 1

# Construction: BP_Ruin_Wall_Thick_1x2m_B_Breakable2_6
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Stone
#   Volume: EMorSimpleShape::OrientedBox, BoxExtent: (69.3, 105.7, 49.3)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (2672.001, 10250.946, 813.0976), (0.0, 0.0, -0.0), (1.3866, 2.1146, 0.9852), "BP_Ruin_Wall_Thick_1x2m_B_Breakable2_6", _folder)
if a: placed += 1
else: skipped += 1

# Construction: BP_Ruin_Wall_Thick_1x2m_B_Breakable3_9
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Stone
#   Volume: EMorSimpleShape::OrientedBox, BoxExtent: (69.3, 105.7, 49.3)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (2216.1348, 10475.192, 813.0976), (0.0, 0.0, -0.0), (1.3866, 2.1146, 0.9852), "BP_Ruin_Wall_Thick_1x2m_B_Breakable3_9", _folder)
if a: placed += 1
else: skipped += 1

# Construction: BP_Ruin_Wall_Thick_1x2m_B_Breakable4
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Stone
#   Volume: EMorSimpleShape::OrientedBox, BoxExtent: (61.5, 102.2, 49.3)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (2701.996, 10063.412, 733.0976), (0.0, 0.0, -0.0), (1.2291, 2.0450, 0.9852), "BP_Ruin_Wall_Thick_1x2m_B_Breakable4", _folder)
if a: placed += 1
else: skipped += 1

# Construction: BP_Ruin_Wall_Thick_1x2m_B_Breakable5_2
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Stone
#   Volume: EMorSimpleShape::OrientedBox, BoxExtent: (62.8, 102.9, 49.3)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (6559.36, 9790.051, 917.7441), (0.0, 0.0, -0.0), (1.2553, 2.0573, 0.9852), "BP_Ruin_Wall_Thick_1x2m_B_Breakable5_2", _folder)
if a: placed += 1
else: skipped += 1

# Construction: BP_Ruin_Wall_Thick_1x2m_B_Breakable6
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Stone
#   Volume: EMorSimpleShape::OrientedBox, BoxExtent: (61.5, 102.3, 49.3)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (7612.01, 1960.8911, 743.0976), (0.0, 0.0, -0.0), (1.2291, 2.0450, 0.9852), "BP_Ruin_Wall_Thick_1x2m_B_Breakable6", _folder)
if a: placed += 1
else: skipped += 1

# Construction: BP_Ruin_Wall_Thick_1x2m_B_Breakable7
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Stone
#   Volume: EMorSimpleShape::OrientedBox, BoxExtent: (110.3, 83.4, 49.3)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (8275.272, 3005.666, 723.0976), (0.0, 0.0, -0.0), (2.2050, 1.6686, 0.9852), "BP_Ruin_Wall_Thick_1x2m_B_Breakable7", _folder)
if a: placed += 1
else: skipped += 1

# Construction: BP_Ruin_Wall_Thick_1x2m_B_Breakable8
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Stone
#   Volume: EMorSimpleShape::OrientedBox, BoxExtent: (102.3, 61.5, 49.3)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (7672.7046, 1832.8429, 743.0976), (0.0, 0.0, -0.0), (2.0450, 1.2291, 0.9852), "BP_Ruin_Wall_Thick_1x2m_B_Breakable8", _folder)
if a: placed += 1
else: skipped += 1

# Construction: BP_Ruin_Wall_Thick_1x2m_C_Breakable_2
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Stone
#   Volume: EMorSimpleShape::OrientedBox, BoxExtent: (65.6, 114.5, 47.0)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (2490.8145, 10482.25, 805.79865), (0.0, 0.0, -0.0), (1.3118, 2.2896, 0.9394), "BP_Ruin_Wall_Thick_1x2m_C_Breakable_2", _folder)
if a: placed += 1
else: skipped += 1

# Construction: BP_Ruin_Wall_Thick_1x2m_C_Breakable2
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Stone
#   Volume: EMorSimpleShape::OrientedBox, BoxExtent: (73.9, 116.5, 47.0)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (8440.832, 3032.4666, 705.79865), (0.0, 0.0, -0.0), (1.4775, 2.3299, 0.9394), "BP_Ruin_Wall_Thick_1x2m_C_Breakable2", _folder)
if a: placed += 1
else: skipped += 1

# Construction: BP_Ruin_Wall_Thick_1x2m_C_Breakable6
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Stone
#   Volume: EMorSimpleShape::OrientedBox, BoxExtent: (99.6, 116.1, 47.0)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (8704.619, 5924.444, 742.95984), (0.0, 0.0, -0.0), (1.9917, 2.3216, 0.9394), "BP_Ruin_Wall_Thick_1x2m_C_Breakable6", _folder)
if a: placed += 1
else: skipped += 1

# Construction: BP_Ruin_Wall_Thick_1x2m_C_Breakable7_14
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Stone
#   Volume: EMorSimpleShape::OrientedBox, BoxExtent: (107.9, 47.6, 47.0)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (11099.266, 3797.625, 1345.5071), (0.0, 0.0, -0.0), (2.1571, 0.9517, 0.9394), "BP_Ruin_Wall_Thick_1x2m_C_Breakable7_14", _folder)
if a: placed += 1
else: skipped += 1

# Construction: BP_Ruin_Wall_Thick_1x2m_D_Breakable_5
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Stone
#   Volume: EMorSimpleShape::OrientedBox, BoxExtent: (150.7, 133.6, 53.7)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (6072.372, 2657.8838, 741.65686), (0.0, 0.0, -0.0), (3.0136, 2.6714, 1.0739), "BP_Ruin_Wall_Thick_1x2m_D_Breakable_5", _folder)
if a: placed += 1
else: skipped += 1

# Construction: BP_Ruin_Wall_Thick_1x3m_B_Breakable_2
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Stone
#   Volume: EMorSimpleShape::OrientedBox, BoxExtent: (64.1, 154.0, 53.6)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (11198.524, 4845.7544, 1597.103), (0.0, 0.0, -0.0), (1.2827, 3.0798, 1.0725), "BP_Ruin_Wall_Thick_1x3m_B_Breakable_2", _folder)
if a: placed += 1
else: skipped += 1

# Construction: BP_Ruin_Wall_Thick_1x3m_B_Breakable2
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Stone
#   Volume: EMorSimpleShape::OrientedBox, BoxExtent: (109.9, 157.7, 53.6)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (10294.523, 6650.174, 717.10297), (0.0, 0.0, -0.0), (2.1976, 3.1538, 1.0725), "BP_Ruin_Wall_Thick_1x3m_B_Breakable2", _folder)
if a: placed += 1
else: skipped += 1

# Construction: BP_Ruin_Wall_Thick_1x3m_B_Breakable3
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Stone
#   Volume: EMorSimpleShape::OrientedBox, BoxExtent: (158.6, 99.5, 53.6)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (10052.932, 6748.6475, 717.10297), (0.0, 0.0, -0.0), (3.1714, 1.9899, 1.0725), "BP_Ruin_Wall_Thick_1x3m_B_Breakable3", _folder)
if a: placed += 1
else: skipped += 1

# Construction: BP_Ruin_Wall_Thick_1x3m_C_Breakable_2
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Stone
#   Volume: EMorSimpleShape::OrientedBox, BoxExtent: (156.7, 76.5, 50.0)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (2091.2, 10604.153, 808.78284), (0.0, 0.0, -0.0), (3.1342, 1.5307, 0.9991), "BP_Ruin_Wall_Thick_1x3m_C_Breakable_2", _folder)
if a: placed += 1
else: skipped += 1

# Construction: BP_Ruin_Wall_Thick_1x3m_C_Breakable2
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Stone
#   Volume: EMorSimpleShape::OrientedBox, BoxExtent: (126.2, 153.2, 50.0)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (9393.986, 5509.4883, 745.94434), (0.0, 0.0, -0.0), (2.5230, 3.0641, 0.9991), "BP_Ruin_Wall_Thick_1x3m_C_Breakable2", _folder)
if a: placed += 1
else: skipped += 1

# Construction: BP_Ruin_Wall_Thick_1x3m_C_Breakable3_8
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Stone
#   Volume: EMorSimpleShape::OrientedBox, BoxExtent: (158.2, 88.3, 50.0)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (6151.4087, 10239.197, 943.4293), (0.0, 0.0, -0.0), (3.1648, 1.7670, 0.9991), "BP_Ruin_Wall_Thick_1x3m_C_Breakable3_8", _folder)
if a: placed += 1
else: skipped += 1

# Construction: BP_Ruin_Wall_Thick_1x3m_C_Breakable4_5
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Stone
#   Volume: EMorSimpleShape::OrientedBox, BoxExtent: (156.7, 76.5, 50.0)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (2473.0193, 10166.386, 808.78284), (0.0, 0.0, -0.0), (3.1342, 1.5307, 0.9991), "BP_Ruin_Wall_Thick_1x3m_C_Breakable4_5", _folder)
if a: placed += 1
else: skipped += 1

# Construction: BP_Ruin_Wall_Thick_1x3m_C_Breakable6_2
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Stone
#   Volume: EMorSimpleShape::OrientedBox, BoxExtent: (150.1, 51.2, 50.0)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (6460.0, 9711.29, 893.4293), (0.0, 0.0, -0.0), (3.0018, 1.0250, 0.9991), "BP_Ruin_Wall_Thick_1x3m_C_Breakable6_2", _folder)
if a: placed += 1
else: skipped += 1

# Construction: BP_Ruin_Wall_Thick_3x1m_B_Breakable15_25
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Stone
#   Volume: EMorSimpleShape::OrientedBox, BoxExtent: (70.2, 69.9, 150.2)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (11352.568, 4575.7095, 1148.4019), (0.0, 0.0, -0.0), (1.4043, 1.3984, 3.0047), "BP_Ruin_Wall_Thick_3x1m_B_Breakable15_25", _folder)
if a: placed += 1
else: skipped += 1

# Construction: BP_Ruin_Wall_Thick_3x1m_B_Breakable2_8
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Stone
#   Volume: EMorSimpleShape::OrientedBox, BoxExtent: (51.7, 50.9, 150.2)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (11147.759, 4650.0, 1648.4019), (0.0, 0.0, -0.0), (1.0339, 1.0178, 3.0047), "BP_Ruin_Wall_Thick_3x1m_B_Breakable2_8", _folder)
if a: placed += 1
else: skipped += 1

# Construction: BP_Ruin_Wall_Thick_3x1m_B_Breakable3
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Stone
#   Volume: EMorSimpleShape::OrientedBox, BoxExtent: (66.0, 65.5, 150.2)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (10217.894, 6829.2334, 838.4018), (0.0, 0.0, -0.0), (1.3197, 1.3100, 3.0047), "BP_Ruin_Wall_Thick_3x1m_B_Breakable3", _folder)
if a: placed += 1
else: skipped += 1

# Construction: BP_Ruin_Wall_Thick_3x1m_B_Breakable8
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Stone
#   Volume: EMorSimpleShape::OrientedBox, BoxExtent: (71.3, 71.1, 150.2)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (8727.993, 5600.868, 855.92194), (0.0, 0.0, -0.0), (1.4256, 1.4212, 3.0047), "BP_Ruin_Wall_Thick_3x1m_B_Breakable8", _folder)
if a: placed += 1
else: skipped += 1

# Construction: BP_Ruin_Wall_Thick_3x1m_C_Breakable_2
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Stone
#   Volume: EMorSimpleShape::OrientedBox, BoxExtent: (59.0, 56.9, 95.8)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (2782.3877, 10216.348, 795.2973), (0.0, 0.0, -0.0), (1.1796, 1.1384, 1.9157), "BP_Ruin_Wall_Thick_3x1m_C_Breakable_2", _folder)
if a: placed += 1
else: skipped += 1

# Construction: BP_Ruin_Wall_Thick_3x1m_C_Breakable5_18
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Stone
#   Volume: EMorSimpleShape::OrientedBox, BoxExtent: (63.4, 65.0, 95.8)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (5953.4995, 10581.487, 1593.9526), (0.0, 0.0, -0.0), (1.2686, 1.2994, 1.9157), "BP_Ruin_Wall_Thick_3x1m_C_Breakable5_18", _folder)
if a: placed += 1
else: skipped += 1

# Construction: BP_Ruin_Wall_Thick_3x1m_C_Breakable6_33
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Stone
#   Volume: EMorSimpleShape::OrientedBox, BoxExtent: (53.5, 55.8, 95.8)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (10700.195, 6597.767, 1093.9526), (0.0, 0.0, -0.0), (1.0704, 1.1158, 1.9157), "BP_Ruin_Wall_Thick_3x1m_C_Breakable6_33", _folder)
if a: placed += 1
else: skipped += 1

# Construction: BP_Ruin_Wall_Thick_3x1m_C_Breakable8
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Stone
#   Volume: EMorSimpleShape::OrientedBox, BoxExtent: (70.6, 71.0, 95.8)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (6358.0024, 4204.672, 857.69946), (0.0, 0.0, -0.0), (1.4112, 1.4200, 1.9157), "BP_Ruin_Wall_Thick_3x1m_C_Breakable8", _folder)
if a: placed += 1
else: skipped += 1

# Construction: BP_Ruin_Wall_Thick_3x3m_B_Breakable_2
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Stone
#   Volume: EMorSimpleShape::OrientedBox, BoxExtent: (77.1, 156.7, 150.0)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (1534.9541, 10304.297, 914.88074), (0.0, 0.0, -0.0), (1.5412, 3.1338, 3.0008), "BP_Ruin_Wall_Thick_3x3m_B_Breakable_2", _folder)
if a: placed += 1
else: skipped += 1

# Construction: BP_Ruin_Wall_Thick_3x3m_B_Breakable5_2
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Stone
#   Volume: EMorSimpleShape::OrientedBox, BoxExtent: (101.9, 166.4, 159.3)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (9163.295, 6225.274, 845.13086), (0.0, 0.0, -0.0), (2.0378, 3.3286, 3.1863), "BP_Ruin_Wall_Thick_3x3m_B_Breakable5_2", _folder)
if a: placed += 1
else: skipped += 1

# Construction: BP_Ruin_Wall_Thick_3x3m_C_Breakable_2
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Stone
#   Volume: EMorSimpleShape::OrientedBox, BoxExtent: (159.7, 77.9, 150.2)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (1597.4553, 10518.401, 913.1063), (0.0, 0.0, -0.0), (3.1936, 1.5578, 3.0045), "BP_Ruin_Wall_Thick_3x3m_C_Breakable_2", _folder)
if a: placed += 1
else: skipped += 1

# Construction: BP_Ruin_Wall_Thick_3x3m_C_Breakable8
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Stone
#   Volume: EMorSimpleShape::OrientedBox, BoxExtent: (152.8, 134.9, 150.2)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (6102.7363, 4526.369, 1011.49963), (0.0, 0.0, -0.0), (3.0561, 2.6985, 3.0045), "BP_Ruin_Wall_Thick_3x3m_C_Breakable8", _folder)
if a: placed += 1
else: skipped += 1

# Construction: BP_Ruin_Wall_Thick_3x3m_D_Breakable4_7
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Stone
#   Volume: EMorSimpleShape::OrientedBox, BoxExtent: (149.7, 51.2, 146.8)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (5450.0, 2049.366, 1686.272), (0.0, 0.0, -0.0), (2.9947, 1.0242, 2.9363), "BP_Ruin_Wall_Thick_3x3m_D_Breakable4_7", _folder)
if a: placed += 1
else: skipped += 1

# Construction: BP_Ruin_Wall_Thick_3x3m_D_Breakable5_15
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Stone
#   Volume: EMorSimpleShape::OrientedBox, BoxExtent: (149.7, 51.2, 146.8)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (11350.0, 3799.366, 1446.272), (0.0, 0.0, -0.0), (2.9947, 1.0242, 2.9363), "BP_Ruin_Wall_Thick_3x3m_D_Breakable5_15", _folder)
if a: placed += 1
else: skipped += 1

# Construction: BP_Ruin_Wall_Thick_3x3m_D_Breakable6
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Stone
#   Volume: EMorSimpleShape::OrientedBox, BoxExtent: (157.9, 88.2, 146.8)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (5779.836, 2049.3877, 1686.272), (0.0, 0.0, -0.0), (3.1578, 1.7644, 2.9363), "BP_Ruin_Wall_Thick_3x3m_D_Breakable6", _folder)
if a: placed += 1
else: skipped += 1

# Construction: BP_Ruin_Wall_Thick_Corner_A_1_Breakable1
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Stone
#   Volume: EMorSimpleShape::OrientedBox, BoxExtent: (141.6, 141.6, 149.5)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (6266.514, 4329.928, 1012.53955), (0.0, 0.0, -0.0), (2.8319, 2.8320, 2.9908), "BP_Ruin_Wall_Thick_Corner_A_1_Breakable1", _folder)
if a: placed += 1
else: skipped += 1

# Construction: BP_Ruin_Wall_Thick_Corner_A_1_Breakable2_4
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Stone
#   Volume: EMorSimpleShape::OrientedBox, BoxExtent: (132.5, 136.0, 156.4)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (9295.727, 6007.8926, 828.8711), (0.0, 0.0, -0.0), (2.6500, 2.7198, 3.1281), "BP_Ruin_Wall_Thick_Corner_A_1_Breakable2_4", _folder)
if a: placed += 1
else: skipped += 1

# Construction: BP_Ruin_Wall_Thick_Corner_A_1_Breakable5_12
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Stone
#   Volume: EMorSimpleShape::OrientedBox, BoxExtent: (124.6, 124.6, 149.5)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (5978.433, 10184.369, 1148.7927), (0.0, 0.0, -0.0), (2.4924, 2.4927, 2.9908), "BP_Ruin_Wall_Thick_Corner_A_1_Breakable5_12", _folder)
if a: placed += 1
else: skipped += 1

# Construction: BP_Ruin_Wall_Thick_Corner_A_3_Breakable15_48
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Stone
#   Volume: EMorSimpleShape::OrientedBox, BoxExtent: (152.3, 153.3, 52.7)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (5327.737, 10903.548, 1300.881), (0.0, 0.0, -0.0), (3.0458, 3.0665, 1.0548), "BP_Ruin_Wall_Thick_Corner_A_3_Breakable15_48", _folder)
if a: placed += 1
else: skipped += 1

# Construction: BP_Ruin_Wall_Thick_Corner_A_3_Breakable2
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Stone
#   Volume: EMorSimpleShape::OrientedBox, BoxExtent: (154.8, 155.6, 52.7)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (9216.99, 5351.539, 753.40106), (0.0, 0.0, -0.0), (3.0964, 3.1119, 1.0548), "BP_Ruin_Wall_Thick_Corner_A_3_Breakable2", _folder)
if a: placed += 1
else: skipped += 1

# Construction: BP_Ruin_Wall_Thick_Corner_A_3_Breakable3_8
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Stone
#   Volume: EMorSimpleShape::OrientedBox, BoxExtent: (113.3, 110.5, 52.7)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (5510.2417, 2502.753, 800.881), (0.0, 0.0, -0.0), (2.2654, 2.2091, 1.0548), "BP_Ruin_Wall_Thick_Corner_A_3_Breakable3_8", _folder)
if a: placed += 1
else: skipped += 1

# Construction: BP_Ruin_Wall_Thin_1x2m_B_Breakable_0
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Stone
#   Volume: EMorSimpleShape::OrientedBox, BoxExtent: (92.9, 29.5, 50.7)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (3502.5586, 7479.5845, 929.48364), (0.0, 0.0, -0.0), (1.8575, 0.5900, 1.0141), "BP_Ruin_Wall_Thin_1x2m_B_Breakable_0", _folder)
if a: placed += 1
else: skipped += 1

# Construction: BP_Ruin_Wall_Thin_1x3m_B_Breakable2_0
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Stone
#   Volume: EMorSimpleShape::OrientedBox, BoxExtent: (26.6, 147.3, 52.4)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (3003.9053, 7432.387, 1331.9257), (0.0, 0.0, -0.0), (0.5325, 2.9467, 1.0488), "BP_Ruin_Wall_Thin_1x3m_B_Breakable2_0", _folder)
if a: placed += 1
else: skipped += 1

# Construction: BP_Ruin_Wall_Thin_1x3m_B_Breakable3_1
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Stone
#   Volume: EMorSimpleShape::OrientedBox, BoxExtent: (147.3, 26.6, 52.4)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (3153.2979, 7481.78, 1228.0745), (0.0, 0.0, -0.0), (2.9467, 0.5325, 1.0488), "BP_Ruin_Wall_Thin_1x3m_B_Breakable3_1", _folder)
if a: placed += 1
else: skipped += 1

# Construction: BP_Ruin_Wall_Thin_1x3m_C_Breakable_0
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Stone
#   Volume: EMorSimpleShape::OrientedBox, BoxExtent: (147.0, 27.4, 36.5)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (2553.2979, 7882.3867, 1915.9879), (0.0, 0.0, -0.0), (2.9393, 0.5484, 0.7300), "BP_Ruin_Wall_Thin_1x3m_C_Breakable_0", _folder)
if a: placed += 1
else: skipped += 1

# Construction: BP_Ruin_Wall_Thin_1x3m_C_Breakable2_2
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Stone
#   Volume: EMorSimpleShape::OrientedBox, BoxExtent: (147.0, 27.4, 36.5)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (3153.2979, 6682.388, 2115.9878), (0.0, 0.0, -0.0), (2.9393, 0.5484, 0.7300), "BP_Ruin_Wall_Thin_1x3m_C_Breakable2_2", _folder)
if a: placed += 1
else: skipped += 1

# Construction: BP_Ruin_Wall_Thin_1x3m_C_Breakable3_1
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Stone
#   Volume: EMorSimpleShape::OrientedBox, BoxExtent: (147.0, 27.4, 36.5)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (3163.2979, 7482.3867, 1315.9879), (0.0, 0.0, -0.0), (2.9393, 0.5484, 0.7300), "BP_Ruin_Wall_Thin_1x3m_C_Breakable3_1", _folder)
if a: placed += 1
else: skipped += 1

# Construction: BP_Ruin_Wall_Thin_1x3m_C_Breakable4
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Stone
#   Volume: EMorSimpleShape::OrientedBox, BoxExtent: (131.9, 119.2, 65.3)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (9033.24, 5426.657, 816.6648), (0.0, 0.0, -0.0), (2.6385, 2.3835, 1.3059), "BP_Ruin_Wall_Thin_1x3m_C_Breakable4", _folder)
if a: placed += 1
else: skipped += 1

# Construction: BP_Ruin_Wall_Thin_1x3m_C_Breakable4_3
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Stone
#   Volume: EMorSimpleShape::OrientedBox, BoxExtent: (27.4, 147.0, 36.5)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (3603.2954, 7632.3867, 915.9879), (0.0, 0.0, -0.0), (0.5484, 2.9393, 0.7300), "BP_Ruin_Wall_Thin_1x3m_C_Breakable4_3", _folder)
if a: placed += 1
else: skipped += 1

# Construction: BP_Ruin_Wall_Thin_1x3m_C_Breakable5_4
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Stone
#   Volume: EMorSimpleShape::OrientedBox, BoxExtent: (147.0, 27.4, 36.5)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (3463.297, 7482.3867, 1315.9879), (0.0, 0.0, -0.0), (2.9393, 0.5484, 0.7300), "BP_Ruin_Wall_Thin_1x3m_C_Breakable5_4", _folder)
if a: placed += 1
else: skipped += 1

# Construction: BP_Ruin_Wall_Thin_1x3m_C_Breakable7
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Stone
#   Volume: EMorSimpleShape::OrientedBox, BoxExtent: (104.6, 137.3, 36.5)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (8610.432, 6372.2686, 738.4952), (0.0, 0.0, -0.0), (2.0924, 2.7468, 0.7301), "BP_Ruin_Wall_Thin_1x3m_C_Breakable7", _folder)
if a: placed += 1
else: skipped += 1

# Construction: BP_Ruin_Wall_Thin_3x1m_D_Breakable_0
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Stone
#   Volume: EMorSimpleShape::OrientedBox, BoxExtent: (26.5, 50.4, 29.3)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (3603.2559, 7332.6577, 1609.7819), (0.0, 0.0, -0.0), (0.5308, 1.0081, 0.5861), "BP_Ruin_Wall_Thin_3x1m_D_Breakable_0", _folder)
if a: placed += 1
else: skipped += 1

# Construction: BP_Ruin_Wall_Thin_3x1m_D_Breakable2_1
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Stone
#   Volume: EMorSimpleShape::OrientedBox, BoxExtent: (50.4, 26.5, 29.3)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (3340.2708, 6690.04, 2109.782), (0.0, 0.0, -0.0), (1.0081, 0.5308, 0.5861), "BP_Ruin_Wall_Thin_3x1m_D_Breakable2_1", _folder)
if a: placed += 1
else: skipped += 1

# Construction: BP_Ruin_Wall_Thin_3x3m_A_Breakable_0
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Stone
#   Volume: EMorSimpleShape::OrientedBox, BoxExtent: (30.7, 149.9, 150.0)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (2403.6184, 7432.387, 1929.498), (0.0, 0.0, -0.0), (0.6137, 2.9982, 3.0002), "BP_Ruin_Wall_Thin_3x3m_A_Breakable_0", _folder)
if a: placed += 1
else: skipped += 1

# Construction: BP_Ruin_Wall_Thin_3x3m_A_Breakable2_3
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Stone
#   Volume: EMorSimpleShape::OrientedBox, BoxExtent: (149.9, 30.7, 150.0)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (2553.2983, 6682.709, 2229.4978), (0.0, 0.0, -0.0), (2.9982, 0.6137, 3.0002), "BP_Ruin_Wall_Thin_3x3m_A_Breakable2_3", _folder)
if a: placed += 1
else: skipped += 1

# Construction: BP_Ruin_Wall_Thin_3x3m_A_Breakable3_1
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Stone
#   Volume: EMorSimpleShape::OrientedBox, BoxExtent: (30.7, 149.9, 150.0)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (3602.9763, 6842.388, 1829.4979), (0.0, 0.0, -0.0), (0.6137, 2.9982, 3.0002), "BP_Ruin_Wall_Thin_3x3m_A_Breakable3_1", _folder)
if a: placed += 1
else: skipped += 1

# Construction: BP_Ruin_Wall_Thin_3x3m_A_Breakable5_4
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Stone
#   Volume: EMorSimpleShape::OrientedBox, BoxExtent: (30.7, 149.9, 150.0)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (2403.6187, 6842.3877, 2229.4978), (0.0, 0.0, -0.0), (0.6137, 2.9982, 3.0002), "BP_Ruin_Wall_Thin_3x3m_A_Breakable5_4", _folder)
if a: placed += 1
else: skipped += 1

# Construction: BP_Ruin_Wall_Thin_3x3m_B_Breakable_2
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Stone
#   Volume: EMorSimpleShape::OrientedBox, BoxExtent: (153.6, 72.1, 150.0)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (5290.3774, 2348.5908, 1309.4644), (0.0, 0.0, -0.0), (3.0725, 1.4412, 2.9996), "BP_Ruin_Wall_Thin_3x3m_B_Breakable_2", _folder)
if a: placed += 1
else: skipped += 1

# Construction: BP_Ruin_Wall_Thin_3x3m_B_Breakable10_7
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Stone
#   Volume: EMorSimpleShape::OrientedBox, BoxExtent: (149.8, 34.5, 150.0)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (3153.2979, 7480.9277, 1029.4644), (0.0, 0.0, -0.0), (2.9962, 0.6892, 2.9996), "BP_Ruin_Wall_Thin_3x3m_B_Breakable10_7", _folder)
if a: placed += 1
else: skipped += 1

# Construction: BP_Ruin_Wall_Thin_3x3m_B_Breakable11_8
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Stone
#   Volume: EMorSimpleShape::OrientedBox, BoxExtent: (149.8, 34.5, 150.0)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (3453.297, 7480.928, 1130.5356), (0.0, 0.0, -0.0), (2.9962, 0.6892, 2.9996), "BP_Ruin_Wall_Thin_3x3m_B_Breakable11_8", _folder)
if a: placed += 1
else: skipped += 1

# Construction: BP_Ruin_Wall_Thin_3x3m_B_Breakable12_9
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Stone
#   Volume: EMorSimpleShape::OrientedBox, BoxExtent: (149.8, 150.0, 34.5)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (3153.297, 7032.9233, 1268.5411), (0.0, 0.0, -0.0), (2.9962, 2.9996, 0.6892), "BP_Ruin_Wall_Thin_3x3m_B_Breakable12_9", _folder)
if a: placed += 1
else: skipped += 1

# Construction: BP_Ruin_Wall_Thin_3x3m_B_Breakable2_0
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Stone
#   Volume: EMorSimpleShape::OrientedBox, BoxExtent: (149.8, 34.5, 150.0)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (2853.2983, 7880.9277, 1729.4644), (0.0, 0.0, -0.0), (2.9962, 0.6892, 2.9996), "BP_Ruin_Wall_Thin_3x3m_B_Breakable2_0", _folder)
if a: placed += 1
else: skipped += 1

# Construction: BP_Ruin_Wall_Thin_3x3m_B_Breakable3_2
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Stone
#   Volume: EMorSimpleShape::OrientedBox, BoxExtent: (34.5, 149.8, 150.0)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (3001.8384, 7732.3867, 1429.4644), (0.0, 0.0, -0.0), (0.6892, 2.9962, 2.9996), "BP_Ruin_Wall_Thin_3x3m_B_Breakable3_2", _folder)
if a: placed += 1
else: skipped += 1

# Construction: BP_Ruin_Wall_Thin_3x3m_B_Breakable4_1
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Stone
#   Volume: EMorSimpleShape::OrientedBox, BoxExtent: (149.8, 150.0, 34.5)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (2553.2983, 7432.9224, 1578.541), (0.0, 0.0, -0.0), (2.9962, 2.9996, 0.6892), "BP_Ruin_Wall_Thin_3x3m_B_Breakable4_1", _folder)
if a: placed += 1
else: skipped += 1

# Construction: BP_Ruin_Wall_Thin_3x3m_B_Breakable5_5
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Stone
#   Volume: EMorSimpleShape::OrientedBox, BoxExtent: (34.5, 149.8, 150.0)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (3604.7556, 7132.3877, 1829.4644), (0.0, 0.0, -0.0), (0.6892, 2.9962, 2.9996), "BP_Ruin_Wall_Thin_3x3m_B_Breakable5_5", _folder)
if a: placed += 1
else: skipped += 1

# Construction: BP_Ruin_Wall_Thin_3x3m_B_Breakable7_4
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Stone
#   Volume: EMorSimpleShape::OrientedBox, BoxExtent: (149.8, 34.5, 150.0)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (2553.2986, 7480.9277, 1029.4644), (0.0, 0.0, -0.0), (2.9962, 0.6892, 2.9996), "BP_Ruin_Wall_Thin_3x3m_B_Breakable7_4", _folder)
if a: placed += 1
else: skipped += 1

# Construction: BP_Ruin_Wall_Thin_3x3m_B_Breakable9_6
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Stone
#   Volume: EMorSimpleShape::OrientedBox, BoxExtent: (149.8, 34.5, 150.0)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (2853.2976, 6680.929, 2229.4644), (0.0, 0.0, -0.0), (2.9962, 0.6892, 2.9996), "BP_Ruin_Wall_Thin_3x3m_B_Breakable9_6", _folder)
if a: placed += 1
else: skipped += 1

# Construction: BP_Ruin_Wall_Thin_3x3m_C_Breakable_1
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Stone
#   Volume: EMorSimpleShape::OrientedBox, BoxExtent: (30.7, 149.7, 136.1)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (2390.0002, 7139.9995, 2215.6296), (0.0, 0.0, -0.0), (0.6137, 2.9947, 2.7229), "BP_Ruin_Wall_Thin_3x3m_C_Breakable_1", _folder)
if a: placed += 1
else: skipped += 1

# Construction: BP_Ruin_Wall_Thin_3x3m_C_Breakable3_0
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Stone
#   Volume: EMorSimpleShape::OrientedBox, BoxExtent: (30.7, 149.7, 136.1)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (2403.298, 7722.3867, 1915.6296), (0.0, 0.0, -0.0), (0.6137, 2.9947, 2.7229), "BP_Ruin_Wall_Thin_3x3m_C_Breakable3_0", _folder)
if a: placed += 1
else: skipped += 1

# Construction: BP_Ruin_Wall_Thin_3x3m_D_Breakable_1
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Stone
#   Volume: EMorSimpleShape::OrientedBox, BoxExtent: (28.1, 147.3, 89.2)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (3603.2969, 6832.388, 2068.7258), (0.0, 0.0, -0.0), (0.5628, 2.9467, 1.7848), "BP_Ruin_Wall_Thin_3x3m_D_Breakable_1", _folder)
if a: placed += 1
else: skipped += 1

# Construction: BP_Ruin_Wall_Thin_3x3m_D_Breakable_6
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Stone
#   Volume: EMorSimpleShape::OrientedBox, BoxExtent: (149.9, 49.2, 89.2)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (5688.9404, 10767.773, 1658.726), (0.0, 0.0, -0.0), (2.9971, 0.9836, 1.7848), "BP_Ruin_Wall_Thin_3x3m_D_Breakable_6", _folder)
if a: placed += 1
else: skipped += 1

# Construction: BP_Ruin_Wall_Thin_3x3m_D_Breakable2_0
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Stone
#   Volume: EMorSimpleShape::OrientedBox, BoxExtent: (147.3, 89.2, 28.1)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (2853.2976, 7493.6606, 1580.0001), (0.0, 0.0, -0.0), (2.9467, 1.7848, 0.5628), "BP_Ruin_Wall_Thin_3x3m_D_Breakable2_0", _folder)
if a: placed += 1
else: skipped += 1

# Construction: BP_Ruin_Wall_Thin_3x3m_D_Breakable3_3
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Stone
#   Volume: EMorSimpleShape::OrientedBox, BoxExtent: (28.1, 147.3, 89.2)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (2390.0005, 7439.999, 2168.7258), (0.0, 0.0, -0.0), (0.5628, 2.9467, 1.7848), "BP_Ruin_Wall_Thin_3x3m_D_Breakable3_3", _folder)
if a: placed += 1
else: skipped += 1

# Construction: BP_Ruins_Stairs_Medium_B_Breakable3
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Stone
#   Volume: EMorSimpleShape::OrientedBox, BoxExtent: (117.4, 158.7, 101.7)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (2504.2153, 8104.0293, 778.64764), (0.0, 0.0, -0.0), (2.3487, 3.1742, 2.0340), "BP_Ruins_Stairs_Medium_B_Breakable3", _folder)
if a: placed += 1
else: skipped += 1

# Construction: BP_Ruins_Stairs_Medium_B_Breakable4
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Stone
#   Volume: EMorSimpleShape::OrientedBox, BoxExtent: (117.4, 158.7, 101.7)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (2934.2153, 8104.0293, 778.64764), (0.0, 0.0, -0.0), (2.3487, 3.1742, 2.0340), "BP_Ruins_Stairs_Medium_B_Breakable4", _folder)
if a: placed += 1
else: skipped += 1

# Construction: BP_Ruins_Stairs_Medium_B_Breakable5
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Stone
#   Volume: EMorSimpleShape::OrientedBox, BoxExtent: (117.4, 158.7, 101.7)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (3394.2153, 8104.0293, 778.64764), (0.0, 0.0, -0.0), (2.3487, 3.1742, 2.0340), "BP_Ruins_Stairs_Medium_B_Breakable5", _folder)
if a: placed += 1
else: skipped += 1

# Construction: BP_Ruins_Stairs_Medium_C_Breakable_5
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Stone
#   Volume: EMorSimpleShape::OrientedBox, BoxExtent: (159.4, 157.8, 102.5)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (3153.7007, 8103.0146, 779.25073), (0.0, 0.0, -0.0), (3.1881, 3.1566, 2.0509), "BP_Ruins_Stairs_Medium_C_Breakable_5", _folder)
if a: placed += 1
else: skipped += 1

# Construction: BP_Ruins_Stairs_Medium_C_Breakable2
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Stone
#   Volume: EMorSimpleShape::OrientedBox, BoxExtent: (159.4, 157.8, 102.5)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (2713.7007, 8103.0146, 779.25073), (0.0, 0.0, -0.0), (3.1881, 3.1566, 2.0509), "BP_Ruins_Stairs_Medium_C_Breakable2", _folder)
if a: placed += 1
else: skipped += 1

# Construction: BP_Suburbs_Balustrade_3m_A13_0
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Advanced
#   Volume: EMorSimpleShape::OrientedBox, BoxExtent: (16.1, 150.0, 40.2)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (2988.298, 7132.288, 1334.9382), (0.0, 0.0, -0.0), (0.3221, 3.0000, 0.8049), "BP_Suburbs_Balustrade_3m_A13_0", _folder)
if a: placed += 1
else: skipped += 1

# Construction: BP_Suburbs_Stairs_Medium_B_0
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Advanced
#   Volume: EMorSimpleShape::Empty, BoxExtent: (100.0, 100.0, 100.0)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (3253.2979, 6782.3887, 1180.0), (-0.0, -90.00005166594045, -0.0), (2.0000, 2.0000, 2.0000), "BP_Suburbs_Stairs_Medium_B_0", _folder)
if a: placed += 1
else: skipped += 1

# Construction: BP_Suburbs_Stairs_Medium_B2
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Advanced
#   Volume: EMorSimpleShape::Empty, BoxExtent: (100.0, 100.0, 100.0)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (3493.2976, 7022.3887, 980.0), (0.0, 6.484984988975128e-05, -0.0), (2.0000, 2.0000, 2.0000), "BP_Suburbs_Stairs_Medium_B2", _folder)
if a: placed += 1
else: skipped += 1

# Construction: BP_Suburbs_Wall_Thick_1x2m_A_Breakable10
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Stone
#   Volume: EMorSimpleShape::OrientedBox, BoxExtent: (50.0, 100.0, 50.0)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (3053.2993, 6782.3877, 1129.4686), (0.0, 0.0, -0.0), (1.0000, 2.0000, 1.0000), "BP_Suburbs_Wall_Thick_1x2m_A_Breakable10", _folder)
if a: placed += 1
else: skipped += 1

# Construction: BP_Suburbs_Wall_Thick_1x2m_A_Breakable11
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Stone
#   Volume: EMorSimpleShape::OrientedBox, BoxExtent: (50.0, 100.0, 50.0)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (3053.2993, 6782.3877, 1229.4686), (0.0, 0.0, -0.0), (1.0000, 2.0000, 1.0000), "BP_Suburbs_Wall_Thick_1x2m_A_Breakable11", _folder)
if a: placed += 1
else: skipped += 1

# Construction: BP_Suburbs_Wall_Thick_1x2m_A_Breakable15
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Stone
#   Volume: EMorSimpleShape::OrientedBox, BoxExtent: (50.0, 100.0, 50.0)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (3153.2993, 6782.3877, 929.4687), (0.0, 0.0, -0.0), (1.0000, 2.0000, 1.0000), "BP_Suburbs_Wall_Thick_1x2m_A_Breakable15", _folder)
if a: placed += 1
else: skipped += 1

# Construction: BP_Suburbs_Wall_Thick_1x2m_A_Breakable16
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Stone
#   Volume: EMorSimpleShape::OrientedBox, BoxExtent: (100.0, 50.0, 50.0)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (3303.2993, 6832.3877, 929.4687), (0.0, 0.0, -0.0), (2.0000, 1.0000, 1.0000), "BP_Suburbs_Wall_Thick_1x2m_A_Breakable16", _folder)
if a: placed += 1
else: skipped += 1

# Construction: BP_Suburbs_Wall_Thick_1x2m_A_Breakable17
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Stone
#   Volume: EMorSimpleShape::OrientedBox, BoxExtent: (100.0, 50.0, 50.0)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (3303.2993, 6732.3877, 929.4687), (0.0, 0.0, -0.0), (2.0000, 1.0000, 1.0000), "BP_Suburbs_Wall_Thick_1x2m_A_Breakable17", _folder)
if a: placed += 1
else: skipped += 1

# Construction: BP_Suburbs_Wall_Thick_1x2m_A_Breakable18
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Stone
#   Volume: EMorSimpleShape::OrientedBox, BoxExtent: (50.0, 100.0, 50.0)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (3153.2993, 6782.3877, 1029.4686), (0.0, 0.0, -0.0), (1.0000, 2.0000, 1.0000), "BP_Suburbs_Wall_Thick_1x2m_A_Breakable18", _folder)
if a: placed += 1
else: skipped += 1

# Construction: BP_Suburbs_Wall_Thick_1x2m_A_Breakable19
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Stone
#   Volume: EMorSimpleShape::OrientedBox, BoxExtent: (100.0, 50.0, 50.0)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (3303.2993, 6832.3877, 1029.4686), (0.0, 0.0, -0.0), (2.0000, 1.0000, 1.0000), "BP_Suburbs_Wall_Thick_1x2m_A_Breakable19", _folder)
if a: placed += 1
else: skipped += 1

# Construction: BP_Suburbs_Wall_Thick_1x2m_A_Breakable20
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Stone
#   Volume: EMorSimpleShape::OrientedBox, BoxExtent: (100.0, 50.0, 50.0)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (3303.2993, 6732.3877, 1029.4686), (0.0, 0.0, -0.0), (2.0000, 1.0000, 1.0000), "BP_Suburbs_Wall_Thick_1x2m_A_Breakable20", _folder)
if a: placed += 1
else: skipped += 1

# Construction: BP_Suburbs_Wall_Thick_1x2m_A_Breakable21
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Stone
#   Volume: EMorSimpleShape::OrientedBox, BoxExtent: (50.0, 100.0, 50.0)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (3453.2993, 6782.3877, 929.4687), (0.0, 0.0, -0.0), (1.0000, 2.0000, 1.0000), "BP_Suburbs_Wall_Thick_1x2m_A_Breakable21", _folder)
if a: placed += 1
else: skipped += 1

# Construction: BP_Suburbs_Wall_Thick_1x2m_A_Breakable22
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Stone
#   Volume: EMorSimpleShape::OrientedBox, BoxExtent: (50.0, 100.0, 50.0)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (3453.2993, 6782.3877, 1029.4686), (0.0, 0.0, -0.0), (1.0000, 2.0000, 1.0000), "BP_Suburbs_Wall_Thick_1x2m_A_Breakable22", _folder)
if a: placed += 1
else: skipped += 1

# Construction: BP_Suburbs_Wall_Thick_1x2m_A_Breakable23
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Stone
#   Volume: EMorSimpleShape::OrientedBox, BoxExtent: (50.0, 100.0, 50.0)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (3553.2993, 6782.3877, 929.4687), (0.0, 0.0, -0.0), (1.0000, 2.0000, 1.0000), "BP_Suburbs_Wall_Thick_1x2m_A_Breakable23", _folder)
if a: placed += 1
else: skipped += 1

# Construction: BP_Suburbs_Wall_Thick_1x2m_A_Breakable24
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Stone
#   Volume: EMorSimpleShape::OrientedBox, BoxExtent: (50.0, 100.0, 50.0)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (3553.2993, 6782.3877, 1029.4686), (0.0, 0.0, -0.0), (1.0000, 2.0000, 1.0000), "BP_Suburbs_Wall_Thick_1x2m_A_Breakable24", _folder)
if a: placed += 1
else: skipped += 1

# Construction: BP_Suburbs_Wall_Thick_1x2m_A_Breakable6_6
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Stone
#   Volume: EMorSimpleShape::OrientedBox, BoxExtent: (50.0, 100.0, 50.0)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (3053.2993, 6782.3877, 929.4687), (0.0, 0.0, -0.0), (1.0000, 2.0000, 1.0000), "BP_Suburbs_Wall_Thick_1x2m_A_Breakable6_6", _folder)
if a: placed += 1
else: skipped += 1

# Construction: BP_Suburbs_Wall_Thick_1x2m_A_Breakable9
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Stone
#   Volume: EMorSimpleShape::OrientedBox, BoxExtent: (50.0, 100.0, 50.0)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (3053.2993, 6782.3877, 1029.4686), (0.0, 0.0, -0.0), (1.0000, 2.0000, 1.0000), "BP_Suburbs_Wall_Thick_1x2m_A_Breakable9", _folder)
if a: placed += 1
else: skipped += 1

# Construction: BP_Suburbs_Wall_Thin_1x2m_A20_3
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Stone
#   Volume: EMorSimpleShape::OrientedBox, BoxExtent: (25.0, 100.0, 50.0)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (3613.2957, 7382.389, 1329.4686), (0.0, 0.0, -0.0), (0.5000, 2.0000, 1.0000), "BP_Suburbs_Wall_Thin_1x2m_A20_3", _folder)
if a: placed += 1
else: skipped += 1

# Construction: BP_Suburbs_Wall_Thin_1x2m_A21
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Stone
#   Volume: EMorSimpleShape::OrientedBox, BoxExtent: (25.0, 100.0, 50.0)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (3613.2957, 7382.389, 1429.4686), (0.0, 0.0, -0.0), (0.5000, 2.0000, 1.0000), "BP_Suburbs_Wall_Thin_1x2m_A21", _folder)
if a: placed += 1
else: skipped += 1

# Construction: BP_Suburbs_Wall_Thin_1x2m_A22
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Stone
#   Volume: EMorSimpleShape::OrientedBox, BoxExtent: (25.0, 100.0, 50.0)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (3613.2957, 7382.389, 929.4687), (0.0, 0.0, -0.0), (0.5000, 2.0000, 1.0000), "BP_Suburbs_Wall_Thin_1x2m_A22", _folder)
if a: placed += 1
else: skipped += 1

# Construction: BP_Suburbs_Wall_Thin_1x2m_A23
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Stone
#   Volume: EMorSimpleShape::OrientedBox, BoxExtent: (25.0, 100.0, 50.0)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (3613.2957, 7382.389, 1529.4686), (0.0, 0.0, -0.0), (0.5000, 2.0000, 1.0000), "BP_Suburbs_Wall_Thin_1x2m_A23", _folder)
if a: placed += 1
else: skipped += 1

# Construction: BP_Suburbs_Wall_Thin_1x2m_A24
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Stone
#   Volume: EMorSimpleShape::OrientedBox, BoxExtent: (25.0, 100.0, 50.0)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (3613.2957, 7382.389, 1029.4686), (0.0, 0.0, -0.0), (0.5000, 2.0000, 1.0000), "BP_Suburbs_Wall_Thin_1x2m_A24", _folder)
if a: placed += 1
else: skipped += 1

# Construction: BP_Suburbs_Wall_Thin_1x2m_A25
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Stone
#   Volume: EMorSimpleShape::OrientedBox, BoxExtent: (25.0, 100.0, 50.0)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (3613.2957, 7382.389, 1129.4686), (0.0, 0.0, -0.0), (0.5000, 2.0000, 1.0000), "BP_Suburbs_Wall_Thin_1x2m_A25", _folder)
if a: placed += 1
else: skipped += 1

# Construction: BP_Suburbs_Wall_Thin_1x2m_A26
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Stone
#   Volume: EMorSimpleShape::OrientedBox, BoxExtent: (25.0, 100.0, 50.0)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (3613.2957, 7382.389, 1229.4686), (0.0, 0.0, -0.0), (0.5000, 2.0000, 1.0000), "BP_Suburbs_Wall_Thin_1x2m_A26", _folder)
if a: placed += 1
else: skipped += 1

# Construction: BP_Suburbs_Wall_Thin_1x3m_A123_0
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Advanced
#   Volume: EMorSimpleShape::Empty, BoxExtent: (100.0, 100.0, 100.0)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (2403.298, 7732.3867, 1730.0), (0.0, 90.0000030488508, -0.0), (2.0000, 2.0000, 2.0000), "BP_Suburbs_Wall_Thin_1x3m_A123_0", _folder)
if a: placed += 1
else: skipped += 1

# Construction: BP_Suburbs_Wall_Thin_1x3m_A124
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Advanced
#   Volume: EMorSimpleShape::Empty, BoxExtent: (100.0, 100.0, 100.0)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (2403.298, 7432.3867, 1730.0), (0.0, 90.0000030488508, -0.0), (2.0000, 2.0000, 2.0000), "BP_Suburbs_Wall_Thin_1x3m_A124", _folder)
if a: placed += 1
else: skipped += 1

# Construction: BP_Suburbs_Wall_Thin_1x3m_A125
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Advanced
#   Volume: EMorSimpleShape::Empty, BoxExtent: (100.0, 100.0, 100.0)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (2403.298, 7132.3867, 1730.0), (0.0, 90.0000030488508, -0.0), (2.0000, 2.0000, 2.0000), "BP_Suburbs_Wall_Thin_1x3m_A125", _folder)
if a: placed += 1
else: skipped += 1

# Construction: BP_Suburbs_Wall_Thin_1x3m_A126
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Advanced
#   Volume: EMorSimpleShape::Empty, BoxExtent: (100.0, 100.0, 100.0)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (2403.298, 6832.3867, 1730.0), (0.0, 90.0000030488508, -0.0), (2.0000, 2.0000, 2.0000), "BP_Suburbs_Wall_Thin_1x3m_A126", _folder)
if a: placed += 1
else: skipped += 1

# Construction: BP_Suburbs_Wall_Thin_1x3m_A129
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Advanced
#   Volume: EMorSimpleShape::Empty, BoxExtent: (100.0, 100.0, 100.0)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (2553.298, 6672.3867, 2030.0), (-0.0, -0.00012207030837116422, -0.0), (2.0000, 2.0000, 2.0000), "BP_Suburbs_Wall_Thin_1x3m_A129", _folder)
if a: placed += 1
else: skipped += 1

# Construction: BP_Suburbs_Wall_Thin_1x3m_A130
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Advanced
#   Volume: EMorSimpleShape::Empty, BoxExtent: (100.0, 100.0, 100.0)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (2853.298, 6672.3867, 2030.0), (-0.0, -0.00012207030837116422, -0.0), (2.0000, 2.0000, 2.0000), "BP_Suburbs_Wall_Thin_1x3m_A130", _folder)
if a: placed += 1
else: skipped += 1

# Construction: BP_Suburbs_Wall_Thin_1x3m_A131
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Advanced
#   Volume: EMorSimpleShape::Empty, BoxExtent: (100.0, 100.0, 100.0)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (3153.298, 6672.3867, 2030.0), (-0.0, -0.00012207030837116422, -0.0), (2.0000, 2.0000, 2.0000), "BP_Suburbs_Wall_Thin_1x3m_A131", _folder)
if a: placed += 1
else: skipped += 1

# Construction: BP_Suburbs_Wall_Thin_1x3m_A132
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Advanced
#   Volume: EMorSimpleShape::Empty, BoxExtent: (100.0, 100.0, 100.0)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (3453.298, 6672.3867, 2030.0), (-0.0, -0.00012207030837116422, -0.0), (2.0000, 2.0000, 2.0000), "BP_Suburbs_Wall_Thin_1x3m_A132", _folder)
if a: placed += 1
else: skipped += 1

# Construction: BP_Suburbs_Wall_Thin_1x3m_A133
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Advanced
#   Volume: EMorSimpleShape::Empty, BoxExtent: (100.0, 100.0, 100.0)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (2403.298, 7732.3867, 1230.0), (0.0, 90.0000030488508, -0.0), (2.0000, 2.0000, 2.0000), "BP_Suburbs_Wall_Thin_1x3m_A133", _folder)
if a: placed += 1
else: skipped += 1

# Construction: BP_Suburbs_Wall_Thin_1x3m_A134
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Advanced
#   Volume: EMorSimpleShape::Empty, BoxExtent: (100.0, 100.0, 100.0)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (2403.298, 7432.3867, 1230.0), (0.0, 90.0000030488508, -0.0), (2.0000, 2.0000, 2.0000), "BP_Suburbs_Wall_Thin_1x3m_A134", _folder)
if a: placed += 1
else: skipped += 1

# Construction: BP_Suburbs_Wall_Thin_1x3m_A135
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Advanced
#   Volume: EMorSimpleShape::Empty, BoxExtent: (100.0, 100.0, 100.0)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (2403.298, 7132.3867, 1230.0), (0.0, 90.0000030488508, -0.0), (2.0000, 2.0000, 2.0000), "BP_Suburbs_Wall_Thin_1x3m_A135", _folder)
if a: placed += 1
else: skipped += 1

# Construction: BP_Suburbs_Wall_Thin_1x3m_A136
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Advanced
#   Volume: EMorSimpleShape::Empty, BoxExtent: (100.0, 100.0, 100.0)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (2403.298, 6832.3867, 1230.0), (0.0, 90.0000030488508, -0.0), (2.0000, 2.0000, 2.0000), "BP_Suburbs_Wall_Thin_1x3m_A136", _folder)
if a: placed += 1
else: skipped += 1

# Construction: BP_Suburbs_Wall_Thin_1x3m_A137
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Advanced
#   Volume: EMorSimpleShape::Empty, BoxExtent: (100.0, 100.0, 100.0)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (2553.299, 6672.388, 1230.0), (-0.0, -179.99988388675877, -0.0), (2.0000, 2.0000, 2.0000), "BP_Suburbs_Wall_Thin_1x3m_A137", _folder)
if a: placed += 1
else: skipped += 1

# Construction: BP_Suburbs_Wall_Thin_1x3m_A138
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Advanced
#   Volume: EMorSimpleShape::Empty, BoxExtent: (100.0, 100.0, 100.0)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (2853.299, 6672.388, 1230.0), (-0.0, -179.99988388675877, -0.0), (2.0000, 2.0000, 2.0000), "BP_Suburbs_Wall_Thin_1x3m_A138", _folder)
if a: placed += 1
else: skipped += 1

# Construction: BP_Suburbs_Wall_Thin_1x3m_A139
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Advanced
#   Volume: EMorSimpleShape::Empty, BoxExtent: (100.0, 100.0, 100.0)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (3153.299, 6672.388, 1230.0), (-0.0, -179.99988388675877, -0.0), (2.0000, 2.0000, 2.0000), "BP_Suburbs_Wall_Thin_1x3m_A139", _folder)
if a: placed += 1
else: skipped += 1

# Construction: BP_Suburbs_Wall_Thin_1x3m_A140
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Advanced
#   Volume: EMorSimpleShape::Empty, BoxExtent: (100.0, 100.0, 100.0)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (3453.299, 6672.388, 1230.0), (-0.0, -179.99988388675877, -0.0), (2.0000, 2.0000, 2.0000), "BP_Suburbs_Wall_Thin_1x3m_A140", _folder)
if a: placed += 1
else: skipped += 1

# Construction: BP_Suburbs_Wall_Thin_1x3m_A141
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Advanced
#   Volume: EMorSimpleShape::Empty, BoxExtent: (100.0, 100.0, 100.0)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (3613.299, 6832.388, 1230.0), (-0.0, -89.99971782898, -0.0), (2.0000, 2.0000, 2.0000), "BP_Suburbs_Wall_Thin_1x3m_A141", _folder)
if a: placed += 1
else: skipped += 1

# Construction: BP_Suburbs_Wall_Thin_1x3m_A142
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Advanced
#   Volume: EMorSimpleShape::Empty, BoxExtent: (100.0, 100.0, 100.0)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (3613.299, 7132.388, 1230.0), (-0.0, -89.99971782898, -0.0), (2.0000, 2.0000, 2.0000), "BP_Suburbs_Wall_Thin_1x3m_A142", _folder)
if a: placed += 1
else: skipped += 1

# Construction: BP_Suburbs_Wall_Thin_1x3m_G10
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Stone
#   Volume: EMorSimpleShape::OrientedBox, BoxExtent: (150.0, 32.0, 50.0)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (3453.2676, 6679.383, 1629.505), (0.0, 0.0, -0.0), (3.0006, 0.6400, 1.0000), "BP_Suburbs_Wall_Thin_1x3m_G10", _folder)
if a: placed += 1
else: skipped += 1

# Construction: BP_Suburbs_Wall_Thin_1x3m_G11
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Stone
#   Volume: EMorSimpleShape::OrientedBox, BoxExtent: (32.0, 150.0, 50.0)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (3596.2966, 6832.3555, 1629.505), (0.0, 0.0, -0.0), (0.6400, 3.0006, 1.0000), "BP_Suburbs_Wall_Thin_1x3m_G11", _folder)
if a: placed += 1
else: skipped += 1

# Construction: BP_Suburbs_Wall_Thin_1x3m_G12
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Stone
#   Volume: EMorSimpleShape::OrientedBox, BoxExtent: (32.0, 150.0, 50.0)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (3596.2966, 7132.3555, 1629.505), (0.0, 0.0, -0.0), (0.6400, 3.0006, 1.0000), "BP_Suburbs_Wall_Thin_1x3m_G12", _folder)
if a: placed += 1
else: skipped += 1

# Construction: BP_Suburbs_Wall_Thin_1x3m_G3_6
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Stone
#   Volume: EMorSimpleShape::OrientedBox, BoxExtent: (32.0, 150.0, 50.0)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (2410.295, 7732.412, 1629.505), (0.0, 0.0, -0.0), (0.6400, 3.0006, 1.0000), "BP_Suburbs_Wall_Thin_1x3m_G3_6", _folder)
if a: placed += 1
else: skipped += 1

# Construction: BP_Suburbs_Wall_Thin_1x3m_G4
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Stone
#   Volume: EMorSimpleShape::OrientedBox, BoxExtent: (32.0, 150.0, 50.0)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (2410.295, 7432.412, 1629.505), (0.0, 0.0, -0.0), (0.6400, 3.0006, 1.0000), "BP_Suburbs_Wall_Thin_1x3m_G4", _folder)
if a: placed += 1
else: skipped += 1

# Construction: BP_Suburbs_Wall_Thin_1x3m_G5
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Stone
#   Volume: EMorSimpleShape::OrientedBox, BoxExtent: (32.0, 150.0, 50.0)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (2410.295, 7132.412, 1629.505), (0.0, 0.0, -0.0), (0.6400, 3.0006, 1.0000), "BP_Suburbs_Wall_Thin_1x3m_G5", _folder)
if a: placed += 1
else: skipped += 1

# Construction: BP_Suburbs_Wall_Thin_1x3m_G6
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Stone
#   Volume: EMorSimpleShape::OrientedBox, BoxExtent: (32.0, 150.0, 50.0)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (2410.295, 6832.412, 1629.505), (0.0, 0.0, -0.0), (0.6400, 3.0006, 1.0000), "BP_Suburbs_Wall_Thin_1x3m_G6", _folder)
if a: placed += 1
else: skipped += 1

# Construction: BP_Suburbs_Wall_Thin_1x3m_G7
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Stone
#   Volume: EMorSimpleShape::OrientedBox, BoxExtent: (150.0, 32.0, 50.0)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (2553.2676, 6679.383, 1629.505), (0.0, 0.0, -0.0), (3.0006, 0.6400, 1.0000), "BP_Suburbs_Wall_Thin_1x3m_G7", _folder)
if a: placed += 1
else: skipped += 1

# Construction: BP_Suburbs_Wall_Thin_1x3m_G8
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Stone
#   Volume: EMorSimpleShape::OrientedBox, BoxExtent: (150.0, 32.0, 50.0)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (2853.2676, 6679.383, 1629.505), (0.0, 0.0, -0.0), (3.0006, 0.6400, 1.0000), "BP_Suburbs_Wall_Thin_1x3m_G8", _folder)
if a: placed += 1
else: skipped += 1

# Construction: BP_Suburbs_Wall_Thin_1x3m_G9
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Stone
#   Volume: EMorSimpleShape::OrientedBox, BoxExtent: (150.0, 32.0, 50.0)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (3153.2676, 6679.383, 1629.505), (0.0, 0.0, -0.0), (3.0006, 0.6400, 1.0000), "BP_Suburbs_Wall_Thin_1x3m_G9", _folder)
if a: placed += 1
else: skipped += 1

# Construction: BP_Suburbs_Wall_Thin_3x3m_A35_0
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Stone
#   Volume: EMorSimpleShape::Empty, BoxExtent: (100.0, 100.0, 100.0)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (2403.2979, 7132.3877, 1930.0), (0.0, 90.0000030488508, -0.0), (2.0000, 2.0000, 2.0000), "BP_Suburbs_Wall_Thin_3x3m_A35_0", _folder)
if a: placed += 1
else: skipped += 1

# Construction: BP_Suburbs_Wall_Thin_3x3m_A36
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Stone
#   Volume: EMorSimpleShape::Empty, BoxExtent: (100.0, 100.0, 100.0)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (2403.2979, 6832.3877, 1930.0), (0.0, 90.0000030488508, -0.0), (2.0000, 2.0000, 2.0000), "BP_Suburbs_Wall_Thin_3x3m_A36", _folder)
if a: placed += 1
else: skipped += 1

# Construction: BP_Suburbs_Wall_Thin_3x3m_A37
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Stone
#   Volume: EMorSimpleShape::Empty, BoxExtent: (100.0, 100.0, 100.0)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (2553.2979, 6672.3877, 1830.0), (-0.0, -179.99988388675877, -0.0), (2.0000, 2.0000, 2.0000), "BP_Suburbs_Wall_Thin_3x3m_A37", _folder)
if a: placed += 1
else: skipped += 1

# Construction: BP_Suburbs_Wall_Thin_3x3m_A38
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Stone
#   Volume: EMorSimpleShape::Empty, BoxExtent: (100.0, 100.0, 100.0)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (2853.2979, 6672.3877, 1830.0), (-0.0, -179.99988388675877, -0.0), (2.0000, 2.0000, 2.0000), "BP_Suburbs_Wall_Thin_3x3m_A38", _folder)
if a: placed += 1
else: skipped += 1

# Construction: BP_Suburbs_Wall_Thin_3x3m_A39
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Stone
#   Volume: EMorSimpleShape::Empty, BoxExtent: (100.0, 100.0, 100.0)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (3153.2979, 6672.3877, 1830.0), (-0.0, -179.99988388675877, -0.0), (2.0000, 2.0000, 2.0000), "BP_Suburbs_Wall_Thin_3x3m_A39", _folder)
if a: placed += 1
else: skipped += 1

# Construction: BP_Suburbs_Wall_Thin_3x3m_A40
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Stone
#   Volume: EMorSimpleShape::Empty, BoxExtent: (100.0, 100.0, 100.0)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (3453.2979, 6672.3877, 1830.0), (-0.0, -179.99988388675877, -0.0), (2.0000, 2.0000, 2.0000), "BP_Suburbs_Wall_Thin_3x3m_A40", _folder)
if a: placed += 1
else: skipped += 1

# Construction: BP_Suburbs_Wall_Thin_3x3m_A41
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Stone
#   Volume: EMorSimpleShape::Empty, BoxExtent: (100.0, 100.0, 100.0)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (2553.2979, 6672.3877, 1430.0), (-0.0, -179.99988388675877, -0.0), (2.0000, 2.0000, 2.0000), "BP_Suburbs_Wall_Thin_3x3m_A41", _folder)
if a: placed += 1
else: skipped += 1

# Construction: BP_Suburbs_Wall_Thin_3x3m_A42
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Stone
#   Volume: EMorSimpleShape::Empty, BoxExtent: (100.0, 100.0, 100.0)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (2853.2979, 6672.3877, 1430.0), (-0.0, -179.99988388675877, -0.0), (2.0000, 2.0000, 2.0000), "BP_Suburbs_Wall_Thin_3x3m_A42", _folder)
if a: placed += 1
else: skipped += 1

# Construction: BP_Suburbs_Wall_Thin_3x3m_A43
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Stone
#   Volume: EMorSimpleShape::Empty, BoxExtent: (100.0, 100.0, 100.0)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (2403.2979, 7132.3877, 1430.0), (0.0, 90.0000030488508, -0.0), (2.0000, 2.0000, 2.0000), "BP_Suburbs_Wall_Thin_3x3m_A43", _folder)
if a: placed += 1
else: skipped += 1

# Construction: BP_Suburbs_Wall_Thin_3x3m_A44
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Stone
#   Volume: EMorSimpleShape::Empty, BoxExtent: (100.0, 100.0, 100.0)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (2403.2979, 6832.3877, 1430.0), (0.0, 90.0000030488508, -0.0), (2.0000, 2.0000, 2.0000), "BP_Suburbs_Wall_Thin_3x3m_A44", _folder)
if a: placed += 1
else: skipped += 1

# Construction: BP_Suburbs_Wall_Thin_3x3m_A45
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Stone
#   Volume: EMorSimpleShape::Empty, BoxExtent: (100.0, 100.0, 100.0)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (2403.2979, 7732.3877, 1430.0), (0.0, 90.0000030488508, -0.0), (2.0000, 2.0000, 2.0000), "BP_Suburbs_Wall_Thin_3x3m_A45", _folder)
if a: placed += 1
else: skipped += 1

# Construction: BP_Suburbs_Wall_Thin_3x3m_A46
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Stone
#   Volume: EMorSimpleShape::Empty, BoxExtent: (100.0, 100.0, 100.0)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (2403.2979, 7432.3877, 1430.0), (0.0, 90.0000030488508, -0.0), (2.0000, 2.0000, 2.0000), "BP_Suburbs_Wall_Thin_3x3m_A46", _folder)
if a: placed += 1
else: skipped += 1

# Construction: BP_Suburbs_Wall_Thin_3x3m_A47
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Stone
#   Volume: EMorSimpleShape::Empty, BoxExtent: (100.0, 100.0, 100.0)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (3153.2979, 6672.3877, 1430.0), (-0.0, -179.99988388675877, -0.0), (2.0000, 2.0000, 2.0000), "BP_Suburbs_Wall_Thin_3x3m_A47", _folder)
if a: placed += 1
else: skipped += 1

# Construction: BP_Suburbs_Wall_Thin_3x3m_A48
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Stone
#   Volume: EMorSimpleShape::Empty, BoxExtent: (100.0, 100.0, 100.0)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (3453.2979, 6672.3877, 1430.0), (-0.0, -179.99988388675877, -0.0), (2.0000, 2.0000, 2.0000), "BP_Suburbs_Wall_Thin_3x3m_A48", _folder)
if a: placed += 1
else: skipped += 1

# Construction: BP_Suburbs_Wall_Thin_3x3m_A49
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Stone
#   Volume: EMorSimpleShape::Empty, BoxExtent: (100.0, 100.0, 100.0)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (3613.2988, 6832.3867, 1430.0), (-0.0, -89.99975996369572, -0.0), (2.0000, 2.0000, 2.0000), "BP_Suburbs_Wall_Thin_3x3m_A49", _folder)
if a: placed += 1
else: skipped += 1

# Construction: BP_Suburbs_Wall_Thin_3x3m_A50
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Stone
#   Volume: EMorSimpleShape::Empty, BoxExtent: (100.0, 100.0, 100.0)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (3613.2979, 7132.3877, 1430.0), (-0.0, -89.99975996369572, -0.0), (2.0000, 2.0000, 2.0000), "BP_Suburbs_Wall_Thin_3x3m_A50", _folder)
if a: placed += 1
else: skipped += 1

# Construction: BP_Suburbs_Wall_Thin_3x3m_A51
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Stone
#   Volume: EMorSimpleShape::Empty, BoxExtent: (100.0, 100.0, 100.0)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (3613.2988, 6832.3867, 1030.0), (-0.0, -89.99975996369572, -0.0), (2.0000, 2.0000, 2.0000), "BP_Suburbs_Wall_Thin_3x3m_A51", _folder)
if a: placed += 1
else: skipped += 1

# Construction: BP_Suburbs_Wall_Thin_3x3m_A52
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Stone
#   Volume: EMorSimpleShape::Empty, BoxExtent: (100.0, 100.0, 100.0)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (3613.2979, 7132.3877, 1030.0), (-0.0, -89.99975996369572, -0.0), (2.0000, 2.0000, 2.0000), "BP_Suburbs_Wall_Thin_3x3m_A52", _folder)
if a: placed += 1
else: skipped += 1

# Construction: BP_Suburbs_Wall_Thin_3x3m_A53
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Stone
#   Volume: EMorSimpleShape::Empty, BoxExtent: (100.0, 100.0, 100.0)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (2403.2979, 7132.3877, 1030.0), (0.0, 90.0000030488508, -0.0), (2.0000, 2.0000, 2.0000), "BP_Suburbs_Wall_Thin_3x3m_A53", _folder)
if a: placed += 1
else: skipped += 1

# Construction: BP_Suburbs_Wall_Thin_3x3m_A54
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Stone
#   Volume: EMorSimpleShape::Empty, BoxExtent: (100.0, 100.0, 100.0)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (2403.2979, 6832.3877, 1030.0), (0.0, 90.0000030488508, -0.0), (2.0000, 2.0000, 2.0000), "BP_Suburbs_Wall_Thin_3x3m_A54", _folder)
if a: placed += 1
else: skipped += 1

# Construction: BP_Suburbs_Wall_Thin_3x3m_A55
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Stone
#   Volume: EMorSimpleShape::Empty, BoxExtent: (100.0, 100.0, 100.0)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (2403.2979, 7732.3877, 1030.0), (0.0, 90.0000030488508, -0.0), (2.0000, 2.0000, 2.0000), "BP_Suburbs_Wall_Thin_3x3m_A55", _folder)
if a: placed += 1
else: skipped += 1

# Construction: BP_Suburbs_Wall_Thin_3x3m_A56
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Stone
#   Volume: EMorSimpleShape::Empty, BoxExtent: (100.0, 100.0, 100.0)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (2403.2979, 7432.3877, 1030.0), (0.0, 90.0000030488508, -0.0), (2.0000, 2.0000, 2.0000), "BP_Suburbs_Wall_Thin_3x3m_A56", _folder)
if a: placed += 1
else: skipped += 1

# Construction: BP_Suburbs_Wall_Thin_3x3m_A57
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Stone
#   Volume: EMorSimpleShape::Empty, BoxExtent: (100.0, 100.0, 100.0)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (2553.2979, 6672.3877, 1030.0), (-0.0, -179.99988388675877, -0.0), (2.0000, 2.0000, 2.0000), "BP_Suburbs_Wall_Thin_3x3m_A57", _folder)
if a: placed += 1
else: skipped += 1

# Construction: BP_Suburbs_Wall_Thin_3x3m_A58
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Stone
#   Volume: EMorSimpleShape::Empty, BoxExtent: (100.0, 100.0, 100.0)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (2853.2979, 6672.3877, 1030.0), (-0.0, -179.99988388675877, -0.0), (2.0000, 2.0000, 2.0000), "BP_Suburbs_Wall_Thin_3x3m_A58", _folder)
if a: placed += 1
else: skipped += 1

# Construction: BP_Suburbs_Wall_Thin_3x3m_A59
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Stone
#   Volume: EMorSimpleShape::Empty, BoxExtent: (100.0, 100.0, 100.0)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (3153.2979, 6672.3877, 1030.0), (-0.0, -179.99988388675877, -0.0), (2.0000, 2.0000, 2.0000), "BP_Suburbs_Wall_Thin_3x3m_A59", _folder)
if a: placed += 1
else: skipped += 1

# Construction: BP_Suburbs_Wall_Thin_3x3m_A60
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Stone
#   Volume: EMorSimpleShape::Empty, BoxExtent: (100.0, 100.0, 100.0)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (3453.2979, 6672.3877, 1030.0), (-0.0, -179.99988388675877, -0.0), (2.0000, 2.0000, 2.0000), "BP_Suburbs_Wall_Thin_3x3m_A60", _folder)
if a: placed += 1
else: skipped += 1

# Construction: BP_Suburbs_Wall_Thin_Arch_Half_E_3m10
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Advanced
#   Volume: EMorSimpleShape::OrientedBox, BoxExtent: (25.0, 149.7, 49.7)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (3003.2979, 6832.3867, 1230.0), (0.0, 0.0, -0.0), (0.5000, 2.9945, 0.9936), "BP_Suburbs_Wall_Thin_Arch_Half_E_3m10", _folder)
if a: placed += 1
else: skipped += 1

# Construction: BP_Suburbs_Wall_Thin_Arch_Half_E_3m2_1
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Advanced
#   Volume: EMorSimpleShape::OrientedBox, BoxExtent: (149.7, 25.0, 49.7)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (2553.2979, 7882.3867, 1230.0), (0.0, 0.0, -0.0), (2.9945, 0.5000, 0.9936), "BP_Suburbs_Wall_Thin_Arch_Half_E_3m2_1", _folder)
if a: placed += 1
else: skipped += 1

# Construction: BP_Suburbs_Wall_Thin_Arch_Half_E_3m6
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Advanced
#   Volume: EMorSimpleShape::OrientedBox, BoxExtent: (149.7, 25.0, 49.7)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (2853.2979, 7882.3867, 1230.0), (0.0, 0.0, -0.0), (2.9945, 0.5000, 0.9936), "BP_Suburbs_Wall_Thin_Arch_Half_E_3m6", _folder)
if a: placed += 1
else: skipped += 1

# Construction: BP_Suburbs_Wall_Thin_Arch_Half_E_3m7
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Advanced
#   Volume: EMorSimpleShape::OrientedBox, BoxExtent: (25.0, 149.7, 49.7)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (3003.2979, 7732.3867, 1230.0), (0.0, 0.0, -0.0), (0.5000, 2.9945, 0.9936), "BP_Suburbs_Wall_Thin_Arch_Half_E_3m7", _folder)
if a: placed += 1
else: skipped += 1

# Construction: BP_Suburbs_Wall_Thin_Arch_Half_E_3m8
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Advanced
#   Volume: EMorSimpleShape::OrientedBox, BoxExtent: (25.0, 149.7, 49.7)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (3003.2979, 7432.3867, 1230.0), (0.0, 0.0, -0.0), (0.5000, 2.9945, 0.9936), "BP_Suburbs_Wall_Thin_Arch_Half_E_3m8", _folder)
if a: placed += 1
else: skipped += 1

# Construction: BP_Suburbs_Wall_Thin_Arch_Half_E_3m9
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Advanced
#   Volume: EMorSimpleShape::OrientedBox, BoxExtent: (25.0, 149.7, 49.7)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (3003.2979, 7132.3867, 1230.0), (0.0, 0.0, -0.0), (0.5000, 2.9945, 0.9936), "BP_Suburbs_Wall_Thin_Arch_Half_E_3m9", _folder)
if a: placed += 1
else: skipped += 1

# Construction: BP_Suburbs_Wall_Thin_Window_Small_B14_0
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Stone
#   Volume: EMorSimpleShape::OrientedBox, BoxExtent: (150.0, 25.7, 153.0)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (2853.2983, 7882.962, 1426.4218), (0.0, 0.0, -0.0), (3.0000, 0.5135, 3.0606), "BP_Suburbs_Wall_Thin_Window_Small_B14_0", _folder)
if a: placed += 1
else: skipped += 1

# Construction: BP_Suburbs_Wall_Thin_Window_Small_B15
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Stone
#   Volume: EMorSimpleShape::OrientedBox, BoxExtent: (150.0, 25.7, 153.0)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (2553.2983, 7882.962, 1426.4218), (0.0, 0.0, -0.0), (3.0000, 0.5135, 3.0606), "BP_Suburbs_Wall_Thin_Window_Small_B15", _folder)
if a: placed += 1
else: skipped += 1

# Construction: BP_Suburbs_Wall_Thin_Window_Small_B16
#   Snap: ESnapPointPlacement::Odd, Grid: Default, Stability: Stone
#   Volume: EMorSimpleShape::OrientedBox, BoxExtent: (150.0, 25.7, 153.0)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (2553.2983, 7882.962, 1726.4218), (0.0, 0.0, -0.0), (3.0000, 0.5135, 3.0606), "BP_Suburbs_Wall_Thin_Window_Small_B16", _folder)
if a: placed += 1
else: skipped += 1

# ======================================================================
# PHASE 3: Breakables + DecoVolumes
# ======================================================================
unreal.log(f"[{BUBBLE_NAME}] Phase 3: Placing breakables and deco volumes...")

_folder = "Reconstruction/BD_BB_Chapter3_HeadwaterNexus/Breakables"

# Breakable Batch 0: BP_Flora_Fungal_Tree_Large_Stump (1 instances)
#   BP Class: /Game/LevelDesign/Deco/Foliage/BP_Flora_Fungal_Tree_Large_Stump
_brk_mesh = "/Game/Art/Assets/Kits/Deco/Flora/Flora_Fungal_Tree_Large_Stump"
_brk_mats = ['/Game/Art/Assets/Kits/Deco/Flora/Materials/Fungal_Trees/MI_Fungal_Tree_Tileable', '/Game/Art/Assets/Kits/Deco/Flora/Materials/Fungal_Trees/MI_Fungal_Tree_Dest', '/Game/Art/Assets/Kits/Deco/Flora/Materials/Fungal_Trees/MI_Fungal_Tree_Head']
a = spawn_static_mesh(_brk_mesh, _brk_mats, (6492.453, 10205.116, 966.4143), (-1.5779416838250766, -71.23838825247121, -2.3153991940954306), (1.0, 1.0, 1.0), "BP_Flora_Fungal_Tree_Large_Stump_2", _folder)
if a: placed += 1
else: skipped += 1

# Breakable Batch 1: BP_Flora_Fungal_Tree_Medium_Stump (1 instances)
#   BP Class: /Game/LevelDesign/Deco/Foliage/BP_Flora_Fungal_Tree_Medium_Stump
_brk_mesh = "/Game/Art/Assets/Kits/Deco/Flora/Flora_Fungal_Tree_Medium_Stump"
_brk_mats = ['/Game/Art/Assets/Kits/Deco/Flora/Materials/Fungal_Trees/MI_Fungal_Tree_Tileable', '/Game/Art/Assets/Kits/Deco/Flora/Materials/Fungal_Trees/MI_Fungal_Tree_Dest', '/Game/Art/Assets/Kits/Deco/Flora/Materials/Fungal_Trees/MI_Fungal_Tree_Head']
a = spawn_static_mesh(_brk_mesh, _brk_mats, (10703.029, 4127.48, 1157.0208), (0.0, 65.2951062673315, -0.0), (1.0, 1.0, 1.0), "BP_Flora_Fungal_Tree_Medium_Stump_2", _folder)
if a: placed += 1
else: skipped += 1

# Breakable Batch 2: BP_Flora_Fungal_Tree_Small_Chopped (1 instances)
#   BP Class: /Game/LevelDesign/Deco/Foliage/BP_Flora_Fungal_Tree_Small_Chopped
_brk_mesh = "/Game/Art/Assets/Kits/Deco/Flora/Flora_Fungal_Tree_Small_Chopped"
_brk_mats = ['/Game/Art/Assets/Kits/Deco/Flora/Materials/Fungal_Trees/MI_Fungal_Tree_Tileable', '/Game/Art/Assets/Kits/Deco/Flora/Materials/Fungal_Trees/MI_Fungal_Tree_Dest', '/Game/Art/Assets/Kits/Deco/Flora/Materials/Fungal_Trees/MI_Fungal_Tree_Head']
a = spawn_static_mesh(_brk_mesh, _brk_mats, (10439.9375, 4155.349, 1070.7242), (-23.717189406965797, 136.22998631955315, -1.3472579549006696), (1.0, 1.0, 1.0), "BP_Flora_Fungal_Tree_Small_Chopped_2", _folder)
if a: placed += 1
else: skipped += 1

# Breakable Batch 3: BP_Fungal_Foliage_AD (2 instances)
#   BP Class: /Game/LevelDesign/Deco/Foliage/BP_Fungal_Foliage_AD
_brk_mesh = "/Game/Art/Assets/Kits/Deco/Flora/Fungal_Foliage_AD"
_brk_mats = ['/Game/Art/Assets/Kits/Deco/Flora/Materials/Fungal_Foliage/MI_Fungal_Foliage_A']
a = spawn_static_mesh(_brk_mesh, _brk_mats, (3540.0, 7729.999, 880.0), (0.0, 74.42147453787975, -0.0), (1.0, 1.0, 1.0), "BP_Fungal_Foliage_AD_0", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_brk_mesh, _brk_mats, (2930.0, 7739.999, 880.0), (0.0, 90.0000030488508, -0.0), (1.0, 1.0, 1.0), "BP_Fungal_Foliage_AD2_1", _folder)
if a: placed += 1
else: skipped += 1

# Breakable Batch 4: BP_DM_Rubble_Masonry_large_A_Breakable (1 instances)
#   BP Class: /Game/LevelDesign/Deco/Rubble/BP_DM_Rubble_Masonry_large_A_Breakable
_brk_mesh = "/Game/Art/Assets/Kits/Deco/Rubble/Rubble_Masonry_large_A"
_brk_mats = ['/Game/Art/Assets/Kits/Deco_Architecture/Ruins/Materials/Ruin_Wall_Thick/MI_Ruin_Wall_Ind_Stone_2_Cavern', '/Game/Art/Assets/Kits/Deco_Architecture/Ruins/Materials/Ruin_Wall_Thick/MI_Ruin_Wall_Ind_Stone_3_Cavern', '/Game/Art/Assets/Kits/Deco_Architecture/Ruins/Materials/Ruin_Wall_Thick/MI_Ruin_Wall_Ind_Stone_1_Cavern', '/Game/Art/Assets/Kits/Deco/Rubble/Materials/Rubble_Masonry_Pile/MI_Rubble_Masonry_Pile_06_Cavern']
a = spawn_static_mesh(_brk_mesh, _brk_mats, (2935.0002, 7189.9995, 1300.0), (0.0, 90.0000030488508, -0.0), (1.0, 1.0, 1.0), "BP_DM_Rubble_Masonry_large_A_Breakable_3", _folder)
if a: placed += 1
else: skipped += 1

# Breakable Batch 5: BP_DM_Rubble_Masonry_large_B_Breakable (1 instances)
#   BP Class: /Game/LevelDesign/Deco/Rubble/BP_DM_Rubble_Masonry_large_B_Breakable
_brk_mesh = "/Game/Art/Assets/Kits/Deco/Rubble/Rubble_Masonry_large_B"
_brk_mats = ['/Game/Art/Assets/Kits/Deco_Architecture/Ruins/Materials/Ruin_Wall_Thick/MI_Ruin_Wall_Ind_Stone_Cavern', '/Game/Art/Assets/Kits/Deco_Architecture/Ruins/Materials/Ruin_Wall_Thick/MI_Ruin_Wall_Ind_Stone_2_Cavern', '/Game/Art/Assets/Kits/Deco_Architecture/Ruins/Materials/Ruin_Wall_Thick/MI_Ruin_Wall_Ind_Stone_2_Cavern']
a = spawn_static_mesh(_brk_mesh, _brk_mats, (3499.9985, 7519.999, 880.0), (0.0, 3.415093967621972e-06, -0.0), (1.0, 1.0, 1.0), "BP_DM_Rubble_Masonry_large_B_Breakable_0", _folder)
if a: placed += 1
else: skipped += 1

# Breakable Batch 6: BP_DM_Rubble_Masonry_large_E_Breakable (2 instances)
#   BP Class: /Game/LevelDesign/Deco/Rubble/BP_DM_Rubble_Masonry_large_E_Breakable
_brk_mesh = "/Game/Art/Assets/Kits/Deco/Rubble/Rubble_Masonry_large_E"
_brk_mats = ['/Game/Art/Assets/Kits/Deco_Architecture/Ruins/Materials/Ruin_Wall_Thick/MI_Ruin_Wall_Ind_Stone_1_Cavern', '/Game/Art/Assets/Kits/Deco_Architecture/Ruins/Materials/Ruin_Wall_Thick/MI_Ruin_Wall_Ind_Stone_Cavern', '/Game/Art/Assets/Kits/Deco_Architecture/Ruins/Materials/Ruin_Wall_Thick/MI_Ruin_Wall_Ind_Stone_2_Cavern', '/Game/Art/Assets/Kits/Deco/Rubble/Materials/Rubble_Masonry_Pile/MI_Rubble_Masonry_Pile_06_Cavern']
a = spawn_static_mesh(_brk_mesh, _brk_mats, (2913.2979, 7632.3867, 1290.0), (0.0, 90.0000030488508, -0.0), (1.0, 1.0, 1.0), "BP_DM_Rubble_Masonry_large_E_Breakable4_0", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_brk_mesh, _brk_mats, (2823.2979, 7782.3867, 1290.0), (0.0, 165.00006780117724, -0.0), (1.0, 1.0, 1.0), "BP_DM_Rubble_Masonry_large_E_Breakable5", _folder)
if a: placed += 1
else: skipped += 1

# Breakable Batch 7: BP_DM_Rubble_Masonry_large_F_Breakable (1 instances)
#   BP Class: /Game/LevelDesign/Deco/Rubble/BP_DM_Rubble_Masonry_large_F_Breakable
_brk_mesh = "/Game/Art/Assets/Kits/Deco/Rubble/Rubble_Masonry_large_F"
_brk_mats = ['/Game/Art/Assets/Kits/Deco_Architecture/Ruins/Materials/Ruin_Wall_Thick/MI_Ruin_Wall_Ind_Stone_1_Cavern', '/Game/Art/Assets/Kits/Deco_Architecture/Ruins/Materials/Ruin_Wall_Thick/MI_Ruin_Wall_Ind_Stone_3_Cavern', '/Game/Art/Assets/Kits/Deco_Architecture/Ruins/Materials/Ruin_Wall_Thick/MI_Ruin_Wall_Ind_Stone_2_Cavern', '/Game/Art/Assets/Kits/Deco/Rubble/Materials/Rubble_Masonry_Pile/MI_Rubble_Masonry_Pile_06_Cavern']
a = spawn_static_mesh(_brk_mesh, _brk_mats, (2490.0005, 7079.9995, 1300.0), (0.0, 90.0000030488508, -0.0), (1.0, 1.0, 1.0), "BP_DM_Rubble_Masonry_large_F_Breakable_1", _folder)
if a: placed += 1
else: skipped += 1

# Breakable Batch 8: BP_DM_Rubble_Masonry_Pile_B_Breakable (2 instances)
#   BP Class: /Game/LevelDesign/Deco/Rubble/BP_DM_Rubble_Masonry_Pile_B_Breakable
_brk_mesh = "/Game/Art/Assets/Kits/Deco/Rubble/Rubble_Masonry_Pile_B"
_brk_mats = ['/Game/Art/Assets/Kits/Deco/Rubble/Materials/Rubble_Masonry_Pile/MI_Rubble_Masonry_Pile_Atlas_Inst_B_Cavern', '/Game/Art/Assets/Kits/Deco/Rubble/Materials/Rubble_Masonry_Pile/MI_Rubble_Masonry_Pile_Atlas_Inst_A_Cavern']
a = spawn_static_mesh(_brk_mesh, _brk_mats, (1632.5631, 9275.35, 687.6915), (0.0, -55.29010087956054, 0.0), (1.0, 1.0, 1.0), "BP_DM_Rubble_Masonry_Pile_B_Breakable_2", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_brk_mesh, _brk_mats, (3033.2979, 7712.387, 880.0), (0.0, 90.0000030488508, -0.0), (1.0, 1.0, 1.0), "BP_DM_Rubble_Masonry_Pile_B_Breakable2_0", _folder)
if a: placed += 1
else: skipped += 1

# Breakable Batch 9: BP_DM_Rubble_Masonry_Pile_C_Breakable (3 instances)
#   BP Class: /Game/LevelDesign/Deco/Rubble/BP_DM_Rubble_Masonry_Pile_C_Breakable
_brk_mesh = "/Game/Art/Assets/Kits/Deco/Rubble/Rubble_Masonry_Pile_C"
_brk_mats = ['/Game/Art/Assets/Kits/Deco/Rubble/Materials/Rubble_Masonry_Pile/MI_Rubble_Masonry_Pile_Atlas_Inst_B_Cavern', '/Game/Art/Assets/Kits/Deco/Rubble/Materials/Rubble_Masonry_Pile/MI_Rubble_Masonry_Pile_Atlas_Inst_A_Cavern']
a = spawn_static_mesh(_brk_mesh, _brk_mats, (2588.669, 10085.254, 690.909), (0.0, 0.0, -0.0), (1.0, 1.0, 1.0), "BP_DM_Rubble_Masonry_Pile_C_Breakable_2", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_brk_mesh, _brk_mats, (3502.98, 7399.623, 880.0), (0.0, 90.00007597449323, -0.0), (1.0, 1.0, 1.0), "BP_DM_Rubble_Masonry_Pile_C_Breakable2_0", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_brk_mesh, _brk_mats, (2593.298, 7782.3867, 1590.0), (0.0, -179.9998975471592, 0.0), (1.0, 1.0, 1.0), "BP_DM_Rubble_Masonry_Pile_C_Breakable3_1", _folder)
if a: placed += 1
else: skipped += 1

# Breakable Batch 10: BP_DM_Rubble_Masonry_Pile_D_Breakable (2 instances)
#   BP Class: /Game/LevelDesign/Deco/Rubble/BP_DM_Rubble_Masonry_Pile_D_Breakable
_brk_mesh = "/Game/Art/Assets/Kits/Deco/Rubble/Rubble_Masonry_Pile_D"
_brk_mats = ['/Game/Art/Assets/Kits/Deco/Rubble/Materials/Rubble_Masonry_Pile/MI_Rubble_Masonry_Pile_Atlas_Inst_A_Cavern', '/Game/Art/Assets/Kits/Deco/Rubble/Materials/Rubble_Masonry_Pile/MI_Rubble_Masonry_Pile_Atlas_Inst_B_Cavern']
a = spawn_static_mesh(_brk_mesh, _brk_mats, (2108.3408, 10506.943, 765.3535), (0.0, 100.00002831399844, -0.0), (1.0, 1.0, 1.0), "BP_DM_Rubble_Masonry_Pile_D_Breakable_2", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_brk_mesh, _brk_mats, (2463.2979, 7352.3867, 880.0), (0.0, -89.99993822608693, 0.0), (1.0, 1.0, 1.0), "BP_DM_Rubble_Masonry_Pile_D_Breakable2_0", _folder)
if a: placed += 1
else: skipped += 1

# Breakable Batch 11: BP_DM_Rubble_Masonry_Pile_E_Breakable (1 instances)
#   BP Class: /Game/LevelDesign/Deco/Rubble/BP_DM_Rubble_Masonry_Pile_E_Breakable
_brk_mesh = "/Game/Art/Assets/Kits/Deco/Rubble/Rubble_Masonry_Pile_E_Optimized"
_brk_mats = ['/Game/Art/Assets/Kits/Deco/Rubble/Materials/Rubble_Masonry_Pile/MI_Rubble_Masonry_Pile_Atlas_Inst_A_Cavern', '/Game/Art/Assets/Kits/Deco/Rubble/Materials/Rubble_Masonry_Pile/MI_Rubble_Masonry_Pile_Atlas_Inst_B_Cavern']
a = spawn_static_mesh(_brk_mesh, _brk_mats, (2554.3584, 10280.961, 765.3535), (0.0, 100.00002831399844, -0.0), (1.0, 1.0, 1.0), "BP_DM_Rubble_Masonry_Pile_E_Breakable_2", _folder)
if a: placed += 1
else: skipped += 1

# Breakable Batch 12: BP_DM_Rubble_Masonry_Pile_E_Breakable (1 instances)
#   BP Class: /Game/LevelDesign/Deco/Rubble/BP_DM_Rubble_Masonry_Pile_E_Breakable
_brk_mesh = "/Game/Art/Assets/Kits/Deco/Rubble/Rubble_Masonry_Pile_E_Optimized"
_brk_mats = ['/Game/Art/Assets/Kits/Deco/Rubble/Materials/Rubble_Masonry_Pile/MI_Rubble_Masonry_Pile_Atlas_Inst_A_Cavern', '/Game/Art/Assets/Kits/Deco/Rubble/Materials/Rubble_Masonry_Pile/MI_Rubble_Masonry_Pile_Atlas_Inst_B_Cavern']
a = spawn_static_mesh(_brk_mesh, _brk_mats, (7764.3584, 1980.9609, 705.3535), (0.0, 29.999939265282134, -0.0), (1.0, 1.0, 1.0), "BP_DM_Rubble_Masonry_Pile_E_Breakable2", _folder)
if a: placed += 1
else: skipped += 1

# Breakable Batch 13: BP_DM_Rubble_Masonry_Pile_F_Breakable (4 instances)
#   BP Class: /Game/LevelDesign/Deco/Rubble/BP_DM_Rubble_Masonry_Pile_F_Breakable
_brk_mesh = "/Game/Art/Assets/Kits/Deco/Rubble/Rubble_Masonry_Pile_F_Optimized"
_brk_mats = ['/Game/Art/Assets/Kits/Deco/Rubble/Materials/Rubble_Masonry_Pile/MI_Rubble_Masonry_Pile_Atlas_Inst_B_Cavern', '/Game/Art/Assets/Kits/Deco/Rubble/Materials/Rubble_Masonry_Pile/MI_Rubble_Masonry_Pile_Atlas_Inst_A_Cavern']
a = spawn_static_mesh(_brk_mesh, _brk_mats, (1673.8602, 10379.56, 765.3535), (0.0, 100.00002831399844, -0.0), (1.0, 1.0, 1.0), "BP_DM_Rubble_Masonry_Pile_F_Breakable_5", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_brk_mesh, _brk_mats, (2584.9883, 6804.391, 873.5027), (0.0, 100.00002831399844, -0.0), (1.0, 1.0, 1.0), "BP_DM_Rubble_Masonry_Pile_F_Breakable2", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_brk_mesh, _brk_mats, (2762.6143, 6835.717, 873.5027), (0.0, 12.968768237947627, -0.0), (1.0, 1.0, 1.0), "BP_DM_Rubble_Masonry_Pile_F_Breakable3", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_brk_mesh, _brk_mats, (3299.6047, 6959.3945, 873.5027), (0.0, 12.968768237947627, -0.0), (1.0, 1.0, 1.0), "BP_DM_Rubble_Masonry_Pile_F_Breakable4", _folder)
if a: placed += 1
else: skipped += 1

# Breakable Batch 14: BP_DM_Rubble_Masonry_Pile_H_Breakable (1 instances)
#   BP Class: /Game/LevelDesign/Deco/Rubble/BP_DM_Rubble_Masonry_Pile_H_Breakable
_brk_mesh = "/Game/Art/Assets/Kits/Deco/Rubble/Rubble_Masonry_Pile_H_Optimized"
_brk_mats = ['/Game/Art/Assets/Kits/Deco/Rubble/Materials/Rubble_Masonry_Pile/MI_Rubble_Masonry_Pile_Atlas_Inst_B_Cavern', '/Game/Art/Assets/Kits/Deco/Rubble/Materials/Rubble_Masonry_Pile/MI_Rubble_Masonry_Pile_Atlas_Inst_A_Cavern']
a = spawn_static_mesh(_brk_mesh, _brk_mats, (4249.5796, 8419.319, 715.0), (0.0, -26.84774632324737, 0.0), (1.0, 1.0, 1.0), "BP_DM_Rubble_Masonry_Pile_H_Breakable_2", _folder)
if a: placed += 1
else: skipped += 1

# Breakable Batch 15: BP_DM_Rubble_Masonry_Pile_H_Breakable (4 instances)
#   BP Class: /Game/LevelDesign/Deco/Rubble/BP_DM_Rubble_Masonry_Pile_H_Breakable
_brk_mesh = "/Game/Art/Assets/Kits/Deco/Rubble/Rubble_Masonry_Pile_H_Optimized"
_brk_mats = ['/Game/Art/Assets/Kits/Deco/Rubble/Materials/Rubble_Masonry_Pile/MI_Rubble_Masonry_Pile_Atlas_Inst_B_Cavern', '/Game/Art/Assets/Kits/Deco/Rubble/Materials/Rubble_Masonry_Pile/MI_Rubble_Masonry_Pile_Atlas_Inst_A_Cavern']
a = spawn_static_mesh(_brk_mesh, _brk_mats, (2560.0, 6849.9995, 1290.0), (0.0, 105.00004236159195, -0.0), (1.0, 1.0, 1.0), "BP_DM_Rubble_Masonry_Pile_H_Breakable_3", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_brk_mesh, _brk_mats, (3460.0, 7339.9995, 1290.0), (0.0, -15.000120764283075, 0.0), (1.0, 1.0, 1.0), "BP_DM_Rubble_Masonry_Pile_H_Breakable2", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_brk_mesh, _brk_mats, (2470.5977, 7053.834, 875.2323), (0.0, 105.00004236159195, -0.0), (1.0, 1.0, 1.0), "BP_DM_Rubble_Masonry_Pile_H_Breakable3", _folder)
if a: placed += 1
else: skipped += 1
a = spawn_static_mesh(_brk_mesh, _brk_mats, (2554.6633, 7569.4443, 875.2323), (0.0, -67.55248301281983, 0.0), (1.0, 1.0, 1.0), "BP_DM_Rubble_Masonry_Pile_H_Breakable4", _folder)
if a: placed += 1
else: skipped += 1

# Breakable Batch 16: BP_DM_Rubble_Masonry_Pile_I_Breakable (1 instances)
#   BP Class: /Game/LevelDesign/Deco/Rubble/BP_DM_Rubble_Masonry_Pile_I_Breakable
_brk_mesh = "/Game/Art/Assets/Kits/Deco/Rubble/Rubble_Masonry_Pile_I"
_brk_mats = ['/Game/Art/Assets/Kits/Deco/Rubble/Materials/Rubble_Masonry_Pile/MI_Rubble_Masonry_Pile_Atlas_Inst_B_Cavern', '/Game/Art/Assets/Kits/Deco/Rubble/Materials/Rubble_Masonry_Pile/MI_Rubble_Masonry_Pile_Atlas_Inst_A_Cavern']
a = spawn_static_mesh(_brk_mesh, _brk_mats, (3777.8582, 8808.0, 722.8014), (0.0, -44.99999866815529, 0.0), (1.0, 1.0, 1.0), "BP_DM_Rubble_Masonry_Pile_I_Breakable_2", _folder)
if a: placed += 1
else: skipped += 1

# Breakable Batch 17: BP_DM_Rubble_Masonry_Pile_I_Breakable (1 instances)
#   BP Class: /Game/LevelDesign/Deco/Rubble/BP_DM_Rubble_Masonry_Pile_I_Breakable
_brk_mesh = "/Game/Art/Assets/Kits/Deco/Rubble/Rubble_Masonry_Pile_I"
_brk_mats = ['/Game/Art/Assets/Kits/Deco/Rubble/Materials/Rubble_Masonry_Pile/MI_Rubble_Masonry_Pile_Atlas_Inst_B_Cavern', '/Game/Art/Assets/Kits/Deco/Rubble/Materials/Rubble_Masonry_Pile/MI_Rubble_Masonry_Pile_Atlas_Inst_A_Cavern']
a = spawn_static_mesh(_brk_mesh, _brk_mats, (2503.2976, 7682.3867, 1590.0), (0.0, 90.0000030488508, -0.0), (1.0, 1.0, 1.0), "BP_DM_Rubble_Masonry_Pile_I_Breakable2_1", _folder)
if a: placed += 1
else: skipped += 1

# Breakable Batch 18: BP_DM_Rubble_Masonry_Pile_I_Breakable (1 instances)
#   BP Class: /Game/LevelDesign/Deco/Rubble/BP_DM_Rubble_Masonry_Pile_I_Breakable
_brk_mesh = "/Game/Art/Assets/Kits/Deco/Rubble/Rubble_Masonry_Pile_I"
_brk_mats = ['/Game/Art/Assets/Kits/Deco/Rubble/Materials/Rubble_Masonry_Pile/MI_Rubble_Masonry_Pile_Atlas_Inst_B_Cavern', '/Game/Art/Assets/Kits/Deco/Rubble/Materials/Rubble_Masonry_Pile/MI_Rubble_Masonry_Pile_Atlas_Inst_A_Cavern']
a = spawn_static_mesh(_brk_mesh, _brk_mats, (1726.7924, 10033.506, 765.3507), (0.0, 10.000151227758034, -0.0), (1.0, 1.0, 1.0), "BP_DM_Rubble_Masonry_Pile_I_Breakable2_5", _folder)
if a: placed += 1
else: skipped += 1

# Breakable Batch 19: Mining_Dirt_Mound_A_Blueprint (1 instances)
#   BP Class: /Game/LevelDesign/Deco_Architecture/Mounds/Mining_Dirt_Mound_A_Blueprint
_brk_mesh = "/Game/Art/Assets/Kits/Misc/Dirt_Mounds/Mining_Dirt_Mound_A"
_brk_mats = ['/Game/Art/Assets/Kits/Misc/Dirt_Mounds/Materials/Suburbs_Dirt_Inst']
a = spawn_static_mesh(_brk_mesh, _brk_mats, (2503.2979, 7382.3867, 880.0), (0.0, 3.415093967621972e-06, -0.0), (1.0, 1.0, 1.0), "Mining_Dirt_Mound_A5_3", _folder)
if a: placed += 1
else: skipped += 1

# Breakable Batch 20: Mining_Dirt_Mound_B2_Blueprint (1 instances)
#   BP Class: /Game/LevelDesign/Deco_Architecture/Mounds/Mining_Dirt_Mound_B2_Blueprint
_brk_mesh = "/Game/Art/Assets/Kits/Misc/Dirt_Mounds/Mining_Dirt_Mound_B"
_brk_mats = ['/Game/Art/Assets/Kits/Misc/Dirt_Mounds/Materials/Suburbs_Dirt_Inst']
a = spawn_static_mesh(_brk_mesh, _brk_mats, (2503.2979, 7302.3877, 870.0), (0.0, 90.0000030488508, -0.0), (1.0, 1.0, 1.0), "Mining_Dirt_Mound_B2_4", _folder)
if a: placed += 1
else: skipped += 1

# --- Extra DecoVolumes (not construction blocks) ---
_folder = "Reconstruction/BD_BB_Chapter3_HeadwaterNexus/DecoVolumes"

# DecoVolume: BP_DM_Rubble_Masonry_large_A_Breakable_3 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (2918.9797, 7189.68, 1329.3792), (0.0, 0.0, -0.0), (1.5925, 2.5568, 0.6509), "DV_BP_DM_Rubble_Masonry_large_A_Breakable_3_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_DM_Rubble_Masonry_large_B_Breakable_0 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (3503.1128, 7530.408, 944.49255), (0.0, 0.0, -0.0), (2.0936, 0.9710, 1.1261), "DV_BP_DM_Rubble_Masonry_large_B_Breakable_0_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_DM_Rubble_Masonry_large_E_Breakable4_0 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (2901.1643, 7619.9707, 1322.203), (0.0, 0.0, -0.0), (1.5134, 2.5069, 0.7478), "DV_BP_DM_Rubble_Masonry_large_E_Breakable4_0_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_DM_Rubble_Masonry_large_E_Breakable5 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (2832.1504, 7767.453, 1322.203), (0.0, 0.0, -0.0), (2.8132, 2.1107, 0.7478), "DV_BP_DM_Rubble_Masonry_large_E_Breakable5_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_DM_Rubble_Masonry_large_F_Breakable_1 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (2505.4602, 7064.3936, 1352.1968), (0.0, 0.0, -0.0), (1.4717, 2.1632, 1.1332), "DV_BP_DM_Rubble_Masonry_large_F_Breakable_1_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_DM_Rubble_Masonry_Pile_B_Breakable_2 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (1650.0726, 9268.492, 741.7768), (0.0, 0.0, -0.0), (3.4173, 3.7961, 1.1191), "DV_BP_DM_Rubble_Masonry_Pile_B_Breakable_2_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_DM_Rubble_Masonry_Pile_B_Breakable2_0 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (3022.809, 7727.9946, 934.08527), (0.0, 0.0, -0.0), (1.8422, 3.3418, 1.1191), "DV_BP_DM_Rubble_Masonry_Pile_B_Breakable2_0_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_DM_Rubble_Masonry_Pile_C_Breakable_2 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (2573.7285, 10089.985, 734.7998), (0.0, 0.0, -0.0), (1.9384, 1.8593, 0.9351), "DV_BP_DM_Rubble_Masonry_Pile_C_Breakable_2_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_DM_Rubble_Masonry_Pile_C_Breakable2_0 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (3498.248, 7384.6826, 923.89075), (0.0, 0.0, -0.0), (1.8593, 1.9384, 0.9351), "DV_BP_DM_Rubble_Masonry_Pile_C_Breakable2_0_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_DM_Rubble_Masonry_Pile_C_Breakable3_1 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (2608.2385, 7777.655, 1633.8907), (0.0, 0.0, -0.0), (1.9384, 1.8593, 0.9351), "DV_BP_DM_Rubble_Masonry_Pile_C_Breakable3_1_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_DM_Rubble_Masonry_Pile_D_Breakable_2 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (2076.1868, 10473.183, 855.80865), (0.0, 0.0, -0.0), (2.4883, 2.2850, 1.8381), "DV_BP_DM_Rubble_Masonry_Pile_D_Breakable_2_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_DM_Rubble_Masonry_Pile_D_Breakable2_0 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (2500.8257, 7380.051, 970.45514), (0.0, 0.0, -0.0), (2.1855, 1.9349, 1.8381), "DV_BP_DM_Rubble_Masonry_Pile_D_Breakable2_0_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_DM_Rubble_Masonry_Pile_E_Breakable_2 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (2544.9866, 10264.705, 788.6942), (0.0, 0.0, -0.0), (2.6471, 2.8602, 1.3025), "DV_BP_DM_Rubble_Masonry_Pile_E_Breakable_2_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_DM_Rubble_Masonry_Pile_E_Breakable2 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (7745.8774, 1984.2079, 728.6942), (0.0, 0.0, -0.0), (3.2951, 3.1990, 1.3025), "DV_BP_DM_Rubble_Masonry_Pile_E_Breakable2_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_DM_Rubble_Masonry_Pile_F_Breakable_5 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (1650.2705, 10375.9795, 818.2045), (0.0, 0.0, -0.0), (4.7515, 5.0650, 1.3764), "DV_BP_DM_Rubble_Masonry_Pile_F_Breakable_5_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_DM_Rubble_Masonry_Pile_F_Breakable2 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (2561.3987, 6800.811, 926.3537), (0.0, 0.0, -0.0), (4.7515, 5.0650, 1.3764), "DV_BP_DM_Rubble_Masonry_Pile_F_Breakable2_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_DM_Rubble_Masonry_Pile_F_Breakable3 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (2757.8174, 6859.0894, 926.3537), (0.0, 0.0, -0.0), (5.2246, 4.9347, 1.3764), "DV_BP_DM_Rubble_Masonry_Pile_F_Breakable3_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_DM_Rubble_Masonry_Pile_F_Breakable4 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (3294.8079, 6982.767, 926.3537), (0.0, 0.0, -0.0), (5.2246, 4.9347, 1.3764), "DV_BP_DM_Rubble_Masonry_Pile_F_Breakable4_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_DM_Rubble_Masonry_Pile_H_Breakable_2 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (4252.978, 8451.452, 778.0759), (0.0, 0.0, -0.0), (3.9362, 3.7085, 1.3071), "DV_BP_DM_Rubble_Masonry_Pile_H_Breakable_2_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_DM_Rubble_Masonry_Pile_H_Breakable_3 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (2582.0964, 6844.0366, 1331.5479), (0.0, 0.0, -0.0), (3.3009, 3.6663, 1.3071), "DV_BP_DM_Rubble_Masonry_Pile_H_Breakable_3_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_DM_Rubble_Masonry_Pile_H_Breakable2 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (3443.7876, 7323.845, 1331.5479), (0.0, 0.0, -0.0), (3.6663, 3.3009, 1.3071), "DV_BP_DM_Rubble_Masonry_Pile_H_Breakable2_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_DM_Rubble_Masonry_Pile_H_Breakable3 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (2492.694, 7047.871, 916.7802), (0.0, 0.0, -0.0), (3.3009, 3.6663, 1.3071), "DV_BP_DM_Rubble_Masonry_Pile_H_Breakable3_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_DM_Rubble_Masonry_Pile_H_Breakable4 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (2531.9807, 7572.493, 916.7802), (0.0, 0.0, -0.0), (3.5747, 3.8551, 1.3071), "DV_BP_DM_Rubble_Masonry_Pile_H_Breakable4_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_DM_Rubble_Masonry_Pile_I_Breakable_2 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (3770.3167, 8824.633, 801.8911), (0.0, 0.0, -0.0), (4.3352, 3.5608, 1.1909), "DV_BP_DM_Rubble_Masonry_Pile_I_Breakable_2_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_DM_Rubble_Masonry_Pile_I_Breakable2_1 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (2492.6362, 7667.56, 1641.5137), (0.0, 0.0, -0.0), (1.8409, 3.9423, 1.1909), "DV_BP_DM_Rubble_Masonry_Pile_I_Breakable2_1_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_DM_Rubble_Masonry_Pile_I_Breakable2_5 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (1720.8418, 10061.528, 816.8643), (0.0, 0.0, -0.0), (4.2020, 2.4975, 1.1909), "DV_BP_DM_Rubble_Masonry_Pile_I_Breakable2_5_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_DM_Warren_Lighting_Torch_Breakable_2 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (3584.3704, 7828.2217, 941.8457), (0.0, 0.0, -0.0), (1.6296, 1.4541, 2.0624), "DV_BP_DM_Warren_Lighting_Torch_Breakable_2_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_DM_Warren_Lighting_Torch_Breakable2 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (8759.042, 9591.418, 854.8237), (0.0, 0.0, -0.0), (1.0112, 1.0765, 1.9128), "DV_BP_DM_Warren_Lighting_Torch_Breakable2_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_DM_Warren_Lighting_Torch_Breakable3 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (10095.968, 5425.9927, 929.16077), (0.0, 0.0, -0.0), (1.4057, 1.4313, 1.9128), "DV_BP_DM_Warren_Lighting_Torch_Breakable3_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_DM_Warren_Lighting_Torch_Breakable4 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (3557.5432, 2181.4248, 869.8237), (0.0, 0.0, -0.0), (1.0112, 1.0765, 1.9128), "DV_BP_DM_Warren_Lighting_Torch_Breakable4_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_DM_Warren_Lighting_Torch_Breakable5 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (6540.16, 1878.4465, 1262.697), (0.0, 0.0, -0.0), (1.2210, 1.1666, 1.9128), "DV_BP_DM_Warren_Lighting_Torch_Breakable5_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_DM_Warren_Lighting_Torch_Breakable6 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (5886.668, 7151.0186, 932.2654), (0.0, 0.0, -0.0), (1.4350, 1.3236, 1.9707), "DV_BP_DM_Warren_Lighting_Torch_Breakable6_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_DM_Warren_Lighting_Torch_Breakable7 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (9643.272, 5396.577, 929.16077), (0.0, 0.0, -0.0), (1.4581, 1.4405, 1.9128), "DV_BP_DM_Warren_Lighting_Torch_Breakable7_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_Flora_Fungal_Tree_Large_Stump_2 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (6494.337, 10178.246, 1237.462), (0.0, 0.0, -0.0), (4.2923, 4.6967, 5.8382), "DV_BP_Flora_Fungal_Tree_Large_Stump_2_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_Flora_Fungal_Tree_Medium_5 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (10113.459, 7959.9956, 854.21497), (0.0, 0.0, -0.0), (4.1604, 4.1671, 2.6621), "DV_BP_Flora_Fungal_Tree_Medium_5_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_Flora_Fungal_Tree_Medium2_8 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (6809.9277, 2160.5977, 785.9472), (0.0, 0.0, -0.0), (3.4264, 3.4110, 2.6621), "DV_BP_Flora_Fungal_Tree_Medium2_8_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_Flora_Fungal_Tree_Medium3_11 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (6867.125, 10189.672, 1164.6816), (0.0, 0.0, -0.0), (4.2618, 4.4582, 2.9974), "DV_BP_Flora_Fungal_Tree_Medium3_11_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_Flora_Fungal_Tree_Medium4_2 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (5254.522, 9869.298, 877.1836), (0.0, 0.0, -0.0), (3.9726, 3.9824, 2.6621), "DV_BP_Flora_Fungal_Tree_Medium4_2_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_Flora_Fungal_Tree_Medium5_5 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (4119.1045, 10867.137, 1051.1958), (0.0, 0.0, -0.0), (4.1793, 4.3098, 2.8913), "DV_BP_Flora_Fungal_Tree_Medium5_5_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_Flora_Fungal_Tree_Medium6_11 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (3181.3196, 2997.4675, 1236.3102), (0.0, 0.0, -0.0), (4.7818, 4.6405, 8.3330), "DV_BP_Flora_Fungal_Tree_Medium6_11_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_Flora_Fungal_Tree_Medium_Stump_2 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (10695.268, 4136.866, 1276.4292), (0.0, 0.0, -0.0), (2.9285, 3.1148, 2.5171), "DV_BP_Flora_Fungal_Tree_Medium_Stump_2_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_Flora_Fungal_Tree_Small_2 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (10197.491, 10032.019, 923.57153), (0.0, 0.0, -0.0), (3.6913, 3.6756, 2.5250), "DV_BP_Flora_Fungal_Tree_Small_2_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_Flora_Fungal_Tree_Small2_5 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (11475.559, 9134.944, 756.7938), (0.0, 0.0, -0.0), (3.5277, 3.5446, 2.5250), "DV_BP_Flora_Fungal_Tree_Small2_5_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_Flora_Fungal_Tree_Small_Chopped_2 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (10408.459, 4143.5464, 1127.0018), (0.0, 0.0, -0.0), (5.1786, 5.1325, 2.9216), "DV_BP_Flora_Fungal_Tree_Small_Chopped_2_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_Flora_Fungal_Tree_X_Small_2 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (10091.9375, 9673.638, 772.4), (0.0, 0.0, -0.0), (4.4009, 4.4082, 2.5250), "DV_BP_Flora_Fungal_Tree_X_Small_2_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_Flora_Fungal_Tree_X_Small2_2 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (4018.6694, 11036.979, 1075.5363), (0.0, 0.0, -0.0), (3.3910, 3.3731, 2.5250), "DV_BP_Flora_Fungal_Tree_X_Small2_2_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_Flora_FungalTree_Young_5 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (9938.486, 8014.5312, 876.721), (0.0, 0.0, -0.0), (4.5603, 4.5627, 2.5250), "DV_BP_Flora_FungalTree_Young_5_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_Fungal_Foliage_AA_0 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (2693.799, 6768.391, 1418.4441), (0.0, 0.0, -0.0), (1.9151, 1.7476, 2.4317), "DV_BP_Fungal_Foliage_AA_0_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_Fungal_Foliage_AA10_10 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (3461.1504, 11806.63, 899.97064), (0.0, 0.0, -0.0), (2.7615, 2.6262, 2.3972), "DV_BP_Fungal_Foliage_AA10_10_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_Fungal_Foliage_AA11 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (7158.4233, 1294.6423, 984.8833), (0.0, 0.0, -0.0), (2.3576, 2.3520, 2.1270), "DV_BP_Fungal_Foliage_AA11_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_Fungal_Foliage_AA12_35 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (5605.063, 2434.8845, 1108.1848), (0.0, 0.0, -0.0), (2.6163, 2.7138, 2.4318), "DV_BP_Fungal_Foliage_AA12_35_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_Fungal_Foliage_AA13_38 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (6715.244, 2368.707, 712.7278), (0.0, 0.0, -0.0), (2.2913, 2.2848, 2.1270), "DV_BP_Fungal_Foliage_AA13_38_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_Fungal_Foliage_AA14_41 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (5809.279, 2602.4937, 724.3273), (0.0, 0.0, -0.0), (2.1009, 2.3874, 2.3886), "DV_BP_Fungal_Foliage_AA14_41_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_Fungal_Foliage_AA15_47 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (5450.215, 3928.4287, 753.61487), (0.0, 0.0, -0.0), (1.7919, 1.8023, 2.1270), "DV_BP_Fungal_Foliage_AA15_47_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_Fungal_Foliage_AA16_50 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (5962.023, 5534.844, 926.97437), (0.0, 0.0, -0.0), (2.5370, 2.5360, 2.1270), "DV_BP_Fungal_Foliage_AA16_50_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_Fungal_Foliage_AA17_53 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (1771.817, 8124.6436, 866.615), (0.0, 0.0, -0.0), (2.1912, 2.2797, 2.5580), "DV_BP_Fungal_Foliage_AA17_53_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_Fungal_Foliage_AA18_56 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (1352.0911, 11241.45, 1110.0117), (0.0, 0.0, -0.0), (2.8054, 2.7600, 2.2927), "DV_BP_Fungal_Foliage_AA18_56_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_Fungal_Foliage_AA19_2 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (10484.713, 7834.054, 968.8385), (0.0, 0.0, -0.0), (2.7561, 2.6508, 2.3463), "DV_BP_Fungal_Foliage_AA19_2_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_Fungal_Foliage_AA2_2 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (10769.304, 6397.303, 1126.1726), (0.0, 0.0, -0.0), (2.8576, 2.5478, 2.5346), "DV_BP_Fungal_Foliage_AA2_2_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_Fungal_Foliage_AA20_5 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (7952.7344, 7895.7275, 1014.968), (0.0, 0.0, -0.0), (2.5849, 2.5505, 2.3037), "DV_BP_Fungal_Foliage_AA20_5_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_Fungal_Foliage_AA21_11 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (11063.384, 5524.1895, 1271.5254), (0.0, 0.0, -0.0), (2.8605, 2.7366, 2.4677), "DV_BP_Fungal_Foliage_AA21_11_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_Fungal_Foliage_AA22_23 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (6245.553, 10333.268, 1138.4586), (0.0, 0.0, -0.0), (1.8737, 2.3506, 2.5405), "DV_BP_Fungal_Foliage_AA22_23_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_Fungal_Foliage_AA23_26 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (6959.9585, 8625.02, 1081.4667), (0.0, 0.0, -0.0), (2.7998, 2.5594, 2.4393), "DV_BP_Fungal_Foliage_AA23_26_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_Fungal_Foliage_AA24_2 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (6255.8535, 8757.78, 885.12085), (0.0, 0.0, -0.0), (2.5296, 2.1834, 2.4477), "DV_BP_Fungal_Foliage_AA24_2_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_Fungal_Foliage_AA25_13 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (3951.4502, 10682.41, 920.6645), (0.0, 0.0, -0.0), (2.6663, 2.6696, 2.2395), "DV_BP_Fungal_Foliage_AA25_13_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_Fungal_Foliage_AA3_5 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (9512.742, 8028.4404, 748.7366), (0.0, 0.0, -0.0), (2.5332, 2.5344, 2.1270), "DV_BP_Fungal_Foliage_AA3_5_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_Fungal_Foliage_AA4_8 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (10217.889, 7112.1084, 741.56824), (0.0, 0.0, -0.0), (1.9573, 1.9667, 2.1270), "DV_BP_Fungal_Foliage_AA4_8_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_Fungal_Foliage_AA5_11 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (8397.338, 8013.134, 686.7178), (0.0, 0.0, -0.0), (2.0891, 2.2867, 2.2792), "DV_BP_Fungal_Foliage_AA5_11_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_Fungal_Foliage_AA6_14 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (10281.892, 10018.98, 944.00793), (0.0, 0.0, -0.0), (2.5986, 2.7361, 2.4305), "DV_BP_Fungal_Foliage_AA6_14_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_Fungal_Foliage_AA7_17 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (9860.85, 9855.974, 818.0343), (0.0, 0.0, -0.0), (2.4882, 2.4487, 2.3262), "DV_BP_Fungal_Foliage_AA7_17_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_Fungal_Foliage_AA8_23 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (6534.6533, 10492.93, 1276.8188), (0.0, 0.0, -0.0), (2.5355, 2.5879, 2.2881), "DV_BP_Fungal_Foliage_AA8_23_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_Fungal_Foliage_AA9_29 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (10933.593, 878.334, 815.3943), (0.0, 0.0, -0.0), (2.2295, 2.2365, 2.1270), "DV_BP_Fungal_Foliage_AA9_29_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_Fungal_Foliage_AB_8 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (8523.321, 9534.102, 823.07764), (0.0, 0.0, -0.0), (2.8332, 2.6511, 2.6256), "DV_BP_Fungal_Foliage_AB_8_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_Fungal_Foliage_AB10_20 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (9351.519, 1245.903, 826.3234), (0.0, 0.0, -0.0), (2.3878, 2.1122, 2.2805), "DV_BP_Fungal_Foliage_AB10_20_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_Fungal_Foliage_AB11_26 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (7142.5205, 10078.088, 1151.544), (0.0, 0.0, -0.0), (2.3324, 2.6668, 2.5289), "DV_BP_Fungal_Foliage_AB11_26_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_Fungal_Foliage_AB12_2 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (4710.5356, 10028.679, 926.7674), (0.0, 0.0, -0.0), (2.3148, 2.5376, 2.4824), "DV_BP_Fungal_Foliage_AB12_2_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_Fungal_Foliage_AB13_5 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (5646.1587, 9843.438, 858.76465), (0.0, 0.0, -0.0), (2.7085, 2.7852, 2.3556), "DV_BP_Fungal_Foliage_AB13_5_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_Fungal_Foliage_AB14_8 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (4962.265, 10190.244, 1112.2051), (0.0, 0.0, -0.0), (2.6940, 2.7742, 2.3442), "DV_BP_Fungal_Foliage_AB14_8_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_Fungal_Foliage_AB15_14 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (1476.0156, 11032.492, 945.92944), (0.0, 0.0, -0.0), (2.7532, 2.4979, 2.3441), "DV_BP_Fungal_Foliage_AB15_14_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_Fungal_Foliage_AB2_17 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (10784.894, 1863.1359, 1051.824), (0.0, 0.0, -0.0), (2.5414, 2.7879, 2.3640), "DV_BP_Fungal_Foliage_AB2_17_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_Fungal_Foliage_AB3_20 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (10997.579, 2292.1633, 974.527), (0.0, 0.0, -0.0), (2.4355, 2.4510, 2.1571), "DV_BP_Fungal_Foliage_AB3_20_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_Fungal_Foliage_AB4_26 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (4849.087, 3282.4792, 955.80444), (0.0, 0.0, -0.0), (2.0085, 1.9994, 2.1270), "DV_BP_Fungal_Foliage_AB4_26_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_Fungal_Foliage_AB5_2 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (10354.812, 7857.641, 880.8052), (0.0, 0.0, -0.0), (2.4992, 2.2917, 2.5730), "DV_BP_Fungal_Foliage_AB5_2_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_Fungal_Foliage_AB6_8 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (8396.759, 6545.916, 850.22595), (0.0, 0.0, -0.0), (2.6842, 2.7377, 2.3215), "DV_BP_Fungal_Foliage_AB6_8_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_Fungal_Foliage_AB7_11 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (10996.973, 5622.0044, 1225.9521), (0.0, 0.0, -0.0), (2.5787, 2.2260, 2.4647), "DV_BP_Fungal_Foliage_AB7_11_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_Fungal_Foliage_AB8_14 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (9156.57, 3902.1738, 907.96185), (0.0, 0.0, -0.0), (2.1910, 2.3216, 2.3283), "DV_BP_Fungal_Foliage_AB8_14_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_Fungal_Foliage_AB9_17 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (8277.958, 3840.6284, 799.5816), (0.0, 0.0, -0.0), (2.8765, 2.5980, 2.5517), "DV_BP_Fungal_Foliage_AB9_17_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_Fungal_Foliage_AC_0 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (3110.2812, 7745.28, 939.2704), (0.0, 0.0, -0.0), (1.4443, 1.3071, 1.3911), "DV_BP_Fungal_Foliage_AC_0_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_Fungal_Foliage_AC10_11 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (8459.717, 7396.1426, 732.1935), (0.0, 0.0, -0.0), (2.2416, 2.2948, 2.3329), "DV_BP_Fungal_Foliage_AC10_11_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_Fungal_Foliage_AC11_14 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (8022.455, 7892.0415, 1007.1161), (0.0, 0.0, -0.0), (2.4732, 2.2231, 2.3430), "DV_BP_Fungal_Foliage_AC11_14_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_Fungal_Foliage_AC12_17 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (9010.1455, 6505.9624, 724.1288), (0.0, 0.0, -0.0), (2.3022, 2.4120, 2.2121), "DV_BP_Fungal_Foliage_AC12_17_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_Fungal_Foliage_AC13_20 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (8378.885, 6502.497, 937.8678), (0.0, 0.0, -0.0), (2.3688, 2.4726, 2.2084), "DV_BP_Fungal_Foliage_AC13_20_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_Fungal_Foliage_AC14_23 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (8619.267, 5920.1494, 1011.365), (0.0, 0.0, -0.0), (2.0577, 1.8023, 2.2451), "DV_BP_Fungal_Foliage_AC14_23_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_Fungal_Foliage_AC15_26 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (10617.5205, 6287.545, 1069.9387), (0.0, 0.0, -0.0), (2.5999, 2.7217, 2.3648), "DV_BP_Fungal_Foliage_AC15_26_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_Fungal_Foliage_AC16_32 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (10941.556, 5430.5728, 1218.8577), (0.0, 0.0, -0.0), (1.7919, 1.8023, 2.1270), "DV_BP_Fungal_Foliage_AC16_32_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_Fungal_Foliage_AC17_38 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (9528.61, 4606.1836, 1049.9778), (0.0, 0.0, -0.0), (2.4228, 2.2701, 2.4546), "DV_BP_Fungal_Foliage_AC17_38_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_Fungal_Foliage_AC18_41 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (10513.2295, 2197.7366, 816.7394), (0.0, 0.0, -0.0), (1.7919, 2.0091, 2.2634), "DV_BP_Fungal_Foliage_AC18_41_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_Fungal_Foliage_AC19_44 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (9035.816, 4018.3074, 926.1826), (0.0, 0.0, -0.0), (2.5415, 2.5415, 2.1270), "DV_BP_Fungal_Foliage_AC19_44_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_Fungal_Foliage_AC2_5 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (10567.613, 8003.314, 1073.2998), (0.0, 0.0, -0.0), (2.0679, 1.8023, 2.2912), "DV_BP_Fungal_Foliage_AC2_5_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_Fungal_Foliage_AC20_47 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (9305.731, 1298.3671, 867.98145), (0.0, 0.0, -0.0), (2.1339, 1.8023, 2.2646), "DV_BP_Fungal_Foliage_AC20_47_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_Fungal_Foliage_AC21_53 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (6740.788, 1986.0029, 933.4115), (0.0, 0.0, -0.0), (2.1229, 2.1114, 2.4250), "DV_BP_Fungal_Foliage_AC21_53_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_Fungal_Foliage_AC22_59 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (6578.922, 9990.036, 954.3867), (0.0, 0.0, -0.0), (2.4540, 2.6080, 2.2863), "DV_BP_Fungal_Foliage_AC22_59_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_Fungal_Foliage_AC23_62 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (6766.3535, 8781.367, 985.34155), (0.0, 0.0, -0.0), (2.2030, 2.1854, 2.4312), "DV_BP_Fungal_Foliage_AC23_62_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_Fungal_Foliage_AC24_65 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (6928.275, 8754.569, 1063.312), (0.0, 0.0, -0.0), (1.9971, 1.9841, 2.3413), "DV_BP_Fungal_Foliage_AC24_65_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_Fungal_Foliage_AC25_2 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (6368.018, 8772.42, 945.6919), (0.0, 0.0, -0.0), (2.0703, 2.0617, 2.1270), "DV_BP_Fungal_Foliage_AC25_2_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_Fungal_Foliage_AC26_5 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (3753.255, 8629.746, 805.70233), (0.0, 0.0, -0.0), (2.3744, 2.4170, 2.4378), "DV_BP_Fungal_Foliage_AC26_5_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_Fungal_Foliage_AC27_8 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (3631.52, 11016.111, 886.44836), (0.0, 0.0, -0.0), (1.7919, 1.8023, 2.1270), "DV_BP_Fungal_Foliage_AC27_8_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_Fungal_Foliage_AC28_11 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (3898.1226, 10885.149, 926.7747), (0.0, 0.0, -0.0), (2.0363, 2.0456, 2.3935), "DV_BP_Fungal_Foliage_AC28_11_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_Fungal_Foliage_AC29_14 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (1284.8486, 9049.97, 773.159), (0.0, 0.0, -0.0), (1.9502, 1.8023, 2.2043), "DV_BP_Fungal_Foliage_AC29_14_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_Fungal_Foliage_AC3_8 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (8253.37, 7915.5444, 802.2047), (0.0, 0.0, -0.0), (2.7916, 2.7625, 2.2643), "DV_BP_Fungal_Foliage_AC3_8_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_Fungal_Foliage_AC30_17 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (1854.2252, 8944.931, 781.5945), (0.0, 0.0, -0.0), (2.2949, 2.3012, 2.1270), "DV_BP_Fungal_Foliage_AC30_17_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_Fungal_Foliage_AC31_20 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (858.2947, 8141.499, 836.37), (0.0, 0.0, -0.0), (2.1823, 2.4611, 2.4092), "DV_BP_Fungal_Foliage_AC31_20_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_Fungal_Foliage_AC32_23 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (1337.3417, 10955.003, 886.25726), (0.0, 0.0, -0.0), (1.9992, 1.8023, 2.2554), "DV_BP_Fungal_Foliage_AC32_23_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_Fungal_Foliage_AC4_27 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (7525.1797, 1682.66, 714.51733), (0.0, 0.0, -0.0), (1.7919, 1.8023, 2.1270), "DV_BP_Fungal_Foliage_AC4_27_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_Fungal_Foliage_AC5_2 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (9713.245, 7850.4243, 781.79956), (0.0, 0.0, -0.0), (1.7919, 1.8023, 2.1270), "DV_BP_Fungal_Foliage_AC5_2_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_Fungal_Foliage_AC6_8 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (10904.571, 8931.982, 916.1897), (0.0, 0.0, -0.0), (1.7919, 1.8023, 2.1270), "DV_BP_Fungal_Foliage_AC6_8_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_Fungal_Foliage_AC7_30 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (6036.7695, 2511.6807, 810.136), (0.0, 0.0, -0.0), (1.7919, 1.8023, 2.1270), "DV_BP_Fungal_Foliage_AC7_30_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_Fungal_Foliage_AC8_36 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (5103.0215, 3304.6304, 850.63684), (0.0, 0.0, -0.0), (2.1579, 2.1501, 2.1270), "DV_BP_Fungal_Foliage_AC8_36_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_Fungal_Foliage_AC9_39 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (3655.6143, 1846.2456, 902.6295), (0.0, 0.0, -0.0), (1.7919, 1.8023, 2.1270), "DV_BP_Fungal_Foliage_AC9_39_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_Fungal_Foliage_AD_0 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (3538.31, 7715.9805, 931.9479), (0.0, 0.0, -0.0), (1.1462, 1.2705, 1.0388), "DV_BP_Fungal_Foliage_AD_0_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_Fungal_Foliage_AD10_44 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (7311.431, 1751.1696, 860.3734), (0.0, 0.0, -0.0), (1.8662, 1.8023, 2.1654), "DV_BP_Fungal_Foliage_AD10_44_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_Fungal_Foliage_AD11_59 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (1761.2595, 8697.055, 767.0072), (0.0, 0.0, -0.0), (1.7919, 1.8023, 2.1270), "DV_BP_Fungal_Foliage_AD11_59_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_Fungal_Foliage_AD12_62 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (1503.2295, 8914.211, 779.7875), (0.0, 0.0, -0.0), (1.7919, 1.8023, 2.1270), "DV_BP_Fungal_Foliage_AD12_62_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_Fungal_Foliage_AD13_65 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (1629.4233, 11008.442, 1093.4631), (0.0, 0.0, -0.0), (2.5411, 2.5413, 2.1270), "DV_BP_Fungal_Foliage_AD13_65_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_Fungal_Foliage_AD14_2 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (10265.566, 9634.901, 833.1876), (0.0, 0.0, -0.0), (2.1257, 2.2699, 2.2315), "DV_BP_Fungal_Foliage_AD14_2_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_Fungal_Foliage_AD15_8 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (10482.553, 7964.9097, 943.0043), (0.0, 0.0, -0.0), (2.1119, 1.8023, 2.3313), "DV_BP_Fungal_Foliage_AD15_8_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_Fungal_Foliage_AD16_14 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (6829.2056, 1814.9727, 1028.532), (0.0, 0.0, -0.0), (2.0554, 1.8570, 2.2548), "DV_BP_Fungal_Foliage_AD16_14_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_Fungal_Foliage_AD17_2 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (4537.007, 9935.155, 890.46423), (0.0, 0.0, -0.0), (1.7919, 2.2266, 2.3366), "DV_BP_Fungal_Foliage_AD17_2_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_Fungal_Foliage_AD18_5 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (4018.313, 8371.177, 795.3323), (0.0, 0.0, -0.0), (2.7626, 2.5579, 2.3026), "DV_BP_Fungal_Foliage_AD18_5_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_Fungal_Foliage_AD2_1 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (2932.137, 7726.0415, 931.9479), (0.0, 0.0, -0.0), (0.8914, 1.0705, 1.0388), "DV_BP_Fungal_Foliage_AD2_1_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_Fungal_Foliage_AD3_2 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (10687.417, 6480.1274, 1045.7124), (0.0, 0.0, -0.0), (2.4873, 2.4903, 2.1270), "DV_BP_Fungal_Foliage_AD3_2_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_Fungal_Foliage_AD4_11 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (8459.593, 6982.5586, 825.10114), (0.0, 0.0, -0.0), (2.1857, 1.8023, 2.2816), "DV_BP_Fungal_Foliage_AD4_11_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_Fungal_Foliage_AD5_14 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (8116.203, 7457.549, 1057.9792), (0.0, 0.0, -0.0), (1.7919, 1.8023, 2.1270), "DV_BP_Fungal_Foliage_AD5_14_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_Fungal_Foliage_AD6_23 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (6864.6895, 9737.5625, 886.78955), (0.0, 0.0, -0.0), (1.7919, 1.8023, 2.1270), "DV_BP_Fungal_Foliage_AD6_23_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_Fungal_Foliage_AD7_29 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (6438.6436, 9123.982, 861.57825), (0.0, 0.0, -0.0), (1.7919, 1.8023, 2.1270), "DV_BP_Fungal_Foliage_AD7_29_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_Fungal_Foliage_AD8_32 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (9812.648, 3302.665, 861.7993), (0.0, 0.0, -0.0), (1.7919, 1.8023, 2.1270), "DV_BP_Fungal_Foliage_AD8_32_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_Fungal_Foliage_AD9_41 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (7476.6104, 1510.0814, 819.18494), (0.0, 0.0, -0.0), (2.0958, 1.8023, 2.2560), "DV_BP_Fungal_Foliage_AD9_41_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_Fungal_Foliage_AE_5 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (8354.268, 7277.501, 1038.342), (0.0, 0.0, -0.0), (1.7919, 1.8023, 2.1270), "DV_BP_Fungal_Foliage_AE_5_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_Fungal_Foliage_AE2_5 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (10562.112, 8681.917, 896.9723), (0.0, 0.0, -0.0), (2.7105, 2.6263, 2.2917), "DV_BP_Fungal_Foliage_AE2_5_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_Fungal_Foliage_AE3_8 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (8922.302, 6090.501, 884.60974), (0.0, 0.0, -0.0), (2.5173, 2.5193, 2.1270), "DV_BP_Fungal_Foliage_AE3_8_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_Fungal_Foliage_AF_2 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (10655.387, 10081.492, 1073.3456), (0.0, 0.0, -0.0), (2.8245, 2.8729, 2.4573), "DV_BP_Fungal_Foliage_AF_2_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_Fungal_Foliage_AF2_8 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (9180.739, 3622.9248, 782.918), (0.0, 0.0, -0.0), (2.0716, 1.9823, 2.4029), "DV_BP_Fungal_Foliage_AF2_8_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_Fungal_Foliage_AF3_11 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (6186.39, 10075.606, 935.58484), (0.0, 0.0, -0.0), (2.4147, 2.5901, 2.4061), "DV_BP_Fungal_Foliage_AF3_11_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_Fungal_Foliage_AF4_8 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (1126.2001, 8876.514, 759.328), (0.0, 0.0, -0.0), (1.7919, 1.8023, 2.1270), "DV_BP_Fungal_Foliage_AF4_8_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_Fungal_Foliage_AF5_11 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (1088.3766, 8150.376, 886.09), (0.0, 0.0, -0.0), (2.0256, 1.9157, 2.3004), "DV_BP_Fungal_Foliage_AF5_11_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_Fungal_Foliage_AG_2 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (10830.191, 9712.926, 926.6035), (0.0, 0.0, -0.0), (1.9848, 2.1320, 2.2242), "DV_BP_Fungal_Foliage_AG_2_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_Fungal_Foliage_AG10_26 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (2307.3372, 10691.711, 831.3203), (0.0, 0.0, -0.0), (2.3410, 2.3467, 2.1270), "DV_BP_Fungal_Foliage_AG10_26_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_Fungal_Foliage_AG11_29 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (1486.6317, 7938.6636, 985.14166), (0.0, 0.0, -0.0), (2.5388, 2.5380, 2.1270), "DV_BP_Fungal_Foliage_AG11_29_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_Fungal_Foliage_AG2_5 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (10454.305, 8485.421, 909.1974), (0.0, 0.0, -0.0), (2.4869, 2.4899, 2.1270), "DV_BP_Fungal_Foliage_AG2_5_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_Fungal_Foliage_AG3_11 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (8153.063, 8080.089, 826.459), (0.0, 0.0, -0.0), (2.5114, 2.4277, 2.3190), "DV_BP_Fungal_Foliage_AG3_11_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_Fungal_Foliage_AG4_23 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (10707.61, 3983.7498, 1150.6672), (0.0, 0.0, -0.0), (2.4984, 2.4006, 2.2217), "DV_BP_Fungal_Foliage_AG4_23_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_Fungal_Foliage_AG5_26 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (8551.223, 3786.9473, 744.40076), (0.0, 0.0, -0.0), (2.2238, 2.3577, 2.3278), "DV_BP_Fungal_Foliage_AG5_26_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_Fungal_Foliage_AG6_8 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (4820.9985, 9793.102, 867.03723), (0.0, 0.0, -0.0), (2.1504, 2.4436, 2.3677), "DV_BP_Fungal_Foliage_AG6_8_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_Fungal_Foliage_AG7_14 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (4948.7603, 10413.466, 1226.3105), (0.0, 0.0, -0.0), (2.2983, 2.2920, 2.1270), "DV_BP_Fungal_Foliage_AG7_14_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_Fungal_Foliage_AG8_17 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (3545.4583, 8415.856, 723.85956), (0.0, 0.0, -0.0), (2.7492, 2.5768, 2.3140), "DV_BP_Fungal_Foliage_AG8_17_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_Fungal_Foliage_AG9_23 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (3563.516, 10559.572, 676.77673), (0.0, 0.0, -0.0), (2.4843, 2.3255, 2.2487), "DV_BP_Fungal_Foliage_AG9_23_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_Fungal_Foliage_AH_5 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (10543.479, 8204.955, 987.5969), (0.0, 0.0, -0.0), (2.3477, 2.1089, 2.3103), "DV_BP_Fungal_Foliage_AH_5_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_Fungal_Foliage_AH2_8 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (8767.493, 5916.78, 1006.03076), (0.0, 0.0, -0.0), (1.7919, 1.8745, 2.1660), "DV_BP_Fungal_Foliage_AH2_8_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_Fungal_Foliage_AH3_11 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (8556.748, 6727.315, 819.22156), (0.0, 0.0, -0.0), (2.4325, 2.4367, 2.1270), "DV_BP_Fungal_Foliage_AH3_11_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_Fungal_Foliage_AH4_14 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (10846.278, 4543.809, 1250.1621), (0.0, 0.0, -0.0), (1.9067, 1.9194, 2.2242), "DV_BP_Fungal_Foliage_AH4_14_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_Fungal_Foliage_AH5_20 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (10952.465, 2069.5393, 1067.8193), (0.0, 0.0, -0.0), (2.2887, 2.1781, 2.1983), "DV_BP_Fungal_Foliage_AH5_20_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_Fungal_Foliage_AH6_26 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (7917.227, 809.857, 827.09753), (0.0, 0.0, -0.0), (2.4259, 2.2248, 2.2954), "DV_BP_Fungal_Foliage_AH6_26_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_Fungal_Foliage_AH7_2 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (3415.4102, 11355.256, 793.3861), (0.0, 0.0, -0.0), (2.5077, 2.4695, 2.1587), "DV_BP_Fungal_Foliage_AH7_2_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_Fungal_Foliage_AH8_5 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (1341.6793, 8759.435, 760.01636), (0.0, 0.0, -0.0), (2.6011, 2.5969, 2.1885), "DV_BP_Fungal_Foliage_AH8_5_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_Fungal_Foliage_BA_4 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (9735.865, 3776.0007, 1075.8901), (0.0, 0.0, -0.0), (2.5404, 2.5400, 2.0620), "DV_BP_Fungal_Foliage_BA_4_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_Fungal_Foliage_BA10_86 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (7043.67, 3272.6619, 786.53394), (0.0, 0.0, -0.0), (2.4589, 2.4551, 2.0620), "DV_BP_Fungal_Foliage_BA10_86_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_Fungal_Foliage_BA2_16 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (8141.603, 7535.9395, 902.3867), (0.0, 0.0, -0.0), (1.7919, 2.0719, 2.2089), "DV_BP_Fungal_Foliage_BA2_16_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_Fungal_Foliage_BA3_5 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (7735.2573, 1293.9354, 701.1686), (0.0, 0.0, -0.0), (1.7919, 1.8023, 2.0620), "DV_BP_Fungal_Foliage_BA3_5_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_Fungal_Foliage_BA4_34 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (11111.931, 8954.723, 891.57263), (0.0, 0.0, -0.0), (2.0188, 2.0098, 2.0620), "DV_BP_Fungal_Foliage_BA4_34_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_Fungal_Foliage_BA6_63 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (4369.5713, 8227.312, 825.3905), (0.0, 0.0, -0.0), (2.2327, 2.2397, 2.0620), "DV_BP_Fungal_Foliage_BA6_63_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_Fungal_Foliage_BA7_67 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (12073.375, 2972.4907, 835.7555), (0.0, 0.0, -0.0), (1.7919, 1.8023, 2.0620), "DV_BP_Fungal_Foliage_BA7_67_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_Fungal_Foliage_BA8_71 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (7419.453, 1531.723, 846.2018), (0.0, 0.0, -0.0), (2.5459, 2.6316, 2.1486), "DV_BP_Fungal_Foliage_BA8_71_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_Fungal_Foliage_BA9_82 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (5085.4375, 3145.403, 716.9457), (0.0, 0.0, -0.0), (1.9672, 1.9765, 2.0620), "DV_BP_Fungal_Foliage_BA9_82_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_Fungal_Foliage_BB_2 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (2489.2937, 7263.3564, 948.818), (0.0, 0.0, -0.0), (0.8488, 1.1064, 1.3789), "DV_BP_Fungal_Foliage_BB_2_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_Fungal_Foliage_BB10 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (10228.755, 8235.967, 905.8086), (0.0, 0.0, -0.0), (2.2429, 2.1898, 2.2541), "DV_BP_Fungal_Foliage_BB10_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_Fungal_Foliage_BB11 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (7030.635, 9754.468, 889.885), (0.0, 0.0, -0.0), (2.3191, 2.3912, 2.2430), "DV_BP_Fungal_Foliage_BB11_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_Fungal_Foliage_BB12 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (10419.643, 7531.0225, 1021.0985), (0.0, 0.0, -0.0), (2.4702, 2.5894, 2.2259), "DV_BP_Fungal_Foliage_BB12_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_Fungal_Foliage_BB13 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (9904.35, 7436.5786, 672.603), (0.0, 0.0, -0.0), (2.1374, 2.0329, 2.1817), "DV_BP_Fungal_Foliage_BB13_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_Fungal_Foliage_BB14 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (10089.345, 5222.0957, 887.9574), (0.0, 0.0, -0.0), (2.3687, 2.4886, 2.2175), "DV_BP_Fungal_Foliage_BB14_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_Fungal_Foliage_BB15_5 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (11028.7, 4806.698, 1349.1335), (0.0, 0.0, -0.0), (2.4508, 2.4469, 2.0620), "DV_BP_Fungal_Foliage_BB15_5_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_Fungal_Foliage_BB17 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (9129.26, 6425.3594, 692.67053), (0.0, 0.0, -0.0), (2.7976, 2.6029, 2.2718), "DV_BP_Fungal_Foliage_BB17_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_Fungal_Foliage_BB18 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (8316.407, 7544.158, 828.6113), (0.0, 0.0, -0.0), (2.7368, 2.6218, 2.2718), "DV_BP_Fungal_Foliage_BB18_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_Fungal_Foliage_BB19 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (8313.863, 8773.893, 765.2954), (0.0, 0.0, -0.0), (2.5097, 2.5795, 2.1285), "DV_BP_Fungal_Foliage_BB19_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_Fungal_Foliage_BB2 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (8074.004, 640.7363, 729.6085), (0.0, 0.0, -0.0), (2.5638, 2.4450, 2.1651), "DV_BP_Fungal_Foliage_BB2_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_Fungal_Foliage_BB20 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (7762.081, 8445.925, 1246.9421), (0.0, 0.0, -0.0), (2.7041, 2.5366, 2.3215), "DV_BP_Fungal_Foliage_BB20_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_Fungal_Foliage_BB21 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (8551.774, 9906.228, 1058.0242), (0.0, 0.0, -0.0), (2.5392, 2.5620, 2.1517), "DV_BP_Fungal_Foliage_BB21_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_Fungal_Foliage_BB22 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (9708.552, 9993.066, 872.695), (0.0, 0.0, -0.0), (2.4233, 2.4099, 2.1558), "DV_BP_Fungal_Foliage_BB22_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_Fungal_Foliage_BB23 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (9506.608, 10500.755, 1246.6713), (0.0, 0.0, -0.0), (2.5145, 2.3370, 2.2334), "DV_BP_Fungal_Foliage_BB23_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_Fungal_Foliage_BB24 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (10482.771, 9759.515, 901.00354), (0.0, 0.0, -0.0), (2.2348, 2.1331, 2.1483), "DV_BP_Fungal_Foliage_BB24_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_Fungal_Foliage_BB25_31 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (10008.737, 9839.179, 897.301), (0.0, 0.0, -0.0), (2.5314, 2.5327, 2.0620), "DV_BP_Fungal_Foliage_BB25_31_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_Fungal_Foliage_BB26 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (10576.147, 8999.539, 818.9437), (0.0, 0.0, -0.0), (2.5430, 2.6458, 2.1677), "DV_BP_Fungal_Foliage_BB26_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_Fungal_Foliage_BB27 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (11016.756, 9128.654, 805.07446), (0.0, 0.0, -0.0), (2.5441, 2.7104, 2.2210), "DV_BP_Fungal_Foliage_BB27_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_Fungal_Foliage_BB28 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (8754.142, 9754.013, 827.1261), (0.0, 0.0, -0.0), (2.8567, 2.7370, 2.3573), "DV_BP_Fungal_Foliage_BB28_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_Fungal_Foliage_BB29 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (10061.397, 9754.0205, 810.6385), (0.0, 0.0, -0.0), (2.4675, 2.4664, 2.1879), "DV_BP_Fungal_Foliage_BB29_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_Fungal_Foliage_BB3 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (9882.594, 3411.739, 890.7663), (0.0, 0.0, -0.0), (2.4431, 2.6181, 2.2018), "DV_BP_Fungal_Foliage_BB3_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_Fungal_Foliage_BB30 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (11553.238, 9921.938, 837.1335), (0.0, 0.0, -0.0), (2.3499, 2.6979, 2.3426), "DV_BP_Fungal_Foliage_BB30_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_Fungal_Foliage_BB31 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (11141.034, 9853.032, 918.61914), (0.0, 0.0, -0.0), (2.3547, 2.5444, 2.4516), "DV_BP_Fungal_Foliage_BB31_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_Fungal_Foliage_BB32_40 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (11648.11, 9142.463, 799.6389), (0.0, 0.0, -0.0), (2.6078, 2.5829, 2.1161), "DV_BP_Fungal_Foliage_BB32_40_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_Fungal_Foliage_BB33 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (12036.493, 9113.187, 812.9208), (0.0, 0.0, -0.0), (2.6097, 2.5911, 2.1161), "DV_BP_Fungal_Foliage_BB33_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_Fungal_Foliage_BB34_44 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (11926.637, 9156.115, 796.4253), (0.0, 0.0, -0.0), (1.7919, 1.8023, 2.0620), "DV_BP_Fungal_Foliage_BB34_44_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_Fungal_Foliage_BB35_2 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (10617.013, 8288.095, 1058.78), (0.0, 0.0, -0.0), (2.6612, 2.5612, 2.3369), "DV_BP_Fungal_Foliage_BB35_2_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_Fungal_Foliage_BB36 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (7438.3647, 8846.741, 1018.6083), (0.0, 0.0, -0.0), (2.6429, 2.8662, 2.3576), "DV_BP_Fungal_Foliage_BB36_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_Fungal_Foliage_BB37 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (7072.173, 10181.649, 1220.3369), (0.0, 0.0, -0.0), (2.4505, 2.7661, 2.4711), "DV_BP_Fungal_Foliage_BB37_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_Fungal_Foliage_BB38 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (6704.899, 10374.869, 1255.4465), (0.0, 0.0, -0.0), (2.0013, 2.1886, 2.1961), "DV_BP_Fungal_Foliage_BB38_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_Fungal_Foliage_BB39 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (5644.9775, 10203.916, 1206.3389), (0.0, 0.0, -0.0), (2.2684, 2.3912, 2.2280), "DV_BP_Fungal_Foliage_BB39_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_Fungal_Foliage_BB4 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (8247.496, 1417.6206, 785.6341), (0.0, 0.0, -0.0), (2.2751, 2.2199, 2.1859), "DV_BP_Fungal_Foliage_BB4_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_Fungal_Foliage_BB41 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (5022.5903, 9822.579, 907.8186), (0.0, 0.0, -0.0), (2.6100, 2.5647, 2.3061), "DV_BP_Fungal_Foliage_BB41_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_Fungal_Foliage_BB44 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (4704.663, 10487.83, 1125.0288), (0.0, 0.0, -0.0), (2.7248, 2.5542, 2.2261), "DV_BP_Fungal_Foliage_BB44_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_Fungal_Foliage_BB46 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (4273.2725, 11220.061, 1349.0792), (0.0, 0.0, -0.0), (2.1676, 2.1361, 2.2462), "DV_BP_Fungal_Foliage_BB46_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_Fungal_Foliage_BB47 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (2132.8513, 11040.906, 1098.955), (0.0, 0.0, -0.0), (2.5389, 2.5614, 2.0966), "DV_BP_Fungal_Foliage_BB47_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_Fungal_Foliage_BB5 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (9561.631, 4790.6465, 1046.6849), (0.0, 0.0, -0.0), (2.5141, 2.5307, 2.1415), "DV_BP_Fungal_Foliage_BB5_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_Fungal_Foliage_BB50 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (2839.0613, 11697.033, 810.2472), (0.0, 0.0, -0.0), (2.7616, 2.7797, 2.2614), "DV_BP_Fungal_Foliage_BB50_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_Fungal_Foliage_BB51 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (2623.6965, 11305.21, 832.89056), (0.0, 0.0, -0.0), (2.0013, 2.0631, 2.1270), "DV_BP_Fungal_Foliage_BB51_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_Fungal_Foliage_BB52 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (6704.034, 8602.992, 1115.8118), (0.0, 0.0, -0.0), (2.0178, 2.4251, 2.2704), "DV_BP_Fungal_Foliage_BB52_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_Fungal_Foliage_BB53 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (6333.1055, 8403.224, 1142.8126), (0.0, 0.0, -0.0), (2.0178, 2.2514, 2.2147), "DV_BP_Fungal_Foliage_BB53_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_Fungal_Foliage_BB54_69 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (4276.4546, 9664.312, 794.20105), (0.0, 0.0, -0.0), (2.4364, 2.4322, 2.0620), "DV_BP_Fungal_Foliage_BB54_69_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_Fungal_Foliage_BB55 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (3811.5554, 8401.742, 883.53516), (0.0, 0.0, -0.0), (2.6640, 2.5551, 2.3429), "DV_BP_Fungal_Foliage_BB55_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_Fungal_Foliage_BB56 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (4135.8276, 8503.709, 741.4232), (0.0, 0.0, -0.0), (2.6505, 2.6517, 2.1452), "DV_BP_Fungal_Foliage_BB56_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_Fungal_Foliage_BB58 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (5354.4067, 4468.884, 921.80115), (0.0, 0.0, -0.0), (2.4219, 2.0149, 2.2683), "DV_BP_Fungal_Foliage_BB58_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_Fungal_Foliage_BB59 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (10629.1875, 3751.7444, 1143.4241), (0.0, 0.0, -0.0), (2.5031, 2.4235, 2.3151), "DV_BP_Fungal_Foliage_BB59_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_Fungal_Foliage_BB6_5 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (9804.59, 3754.7861, 1076.4843), (0.0, 0.0, -0.0), (2.2858, 2.3444, 2.1089), "DV_BP_Fungal_Foliage_BB6_5_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_Fungal_Foliage_BB60 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (11038.079, 3969.691, 1321.5231), (0.0, 0.0, -0.0), (2.5725, 2.6792, 2.2048), "DV_BP_Fungal_Foliage_BB60_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_Fungal_Foliage_BB62 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (9554.96, 3825.816, 1046.5571), (0.0, 0.0, -0.0), (2.5824, 2.4423, 2.1817), "DV_BP_Fungal_Foliage_BB62_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_Fungal_Foliage_BB63_80 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (8183.046, 3656.8137, 838.7429), (0.0, 0.0, -0.0), (2.5264, 2.5248, 2.0620), "DV_BP_Fungal_Foliage_BB63_80_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_Fungal_Foliage_BB64 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (11126.073, 3293.8088, 833.0972), (0.0, 0.0, -0.0), (2.7320, 2.5533, 2.2444), "DV_BP_Fungal_Foliage_BB64_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_Fungal_Foliage_BB65_84 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (11040.865, 3221.7268, 833.69543), (0.0, 0.0, -0.0), (1.7919, 1.8023, 2.0620), "DV_BP_Fungal_Foliage_BB65_84_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_Fungal_Foliage_BB67 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (10996.24, 2593.068, 828.1703), (0.0, 0.0, -0.0), (2.9054, 2.5906, 2.3920), "DV_BP_Fungal_Foliage_BB67_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_Fungal_Foliage_BB68_93 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (11207.662, 2727.5881, 852.0259), (0.0, 0.0, -0.0), (1.7919, 1.8023, 2.0620), "DV_BP_Fungal_Foliage_BB68_93_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_Fungal_Foliage_BB69 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (10635.889, 1622.0182, 894.7454), (0.0, 0.0, -0.0), (2.7197, 2.4637, 2.2997), "DV_BP_Fungal_Foliage_BB69_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_Fungal_Foliage_BB7 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (10386.174, 3854.916, 1027.1055), (0.0, 0.0, -0.0), (2.6185, 2.4066, 2.2474), "DV_BP_Fungal_Foliage_BB7_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_Fungal_Foliage_BB70 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (10898.609, 1025.6849, 835.17365), (0.0, 0.0, -0.0), (2.1514, 2.3151, 2.2723), "DV_BP_Fungal_Foliage_BB70_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_Fungal_Foliage_BB71 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (10924.495, 502.9667, 805.1195), (0.0, 0.0, -0.0), (2.2803, 2.4137, 2.2723), "DV_BP_Fungal_Foliage_BB71_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_Fungal_Foliage_BB72 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (8025.0234, 3288.3958, 879.4734), (0.0, 0.0, -0.0), (2.6682, 2.4991, 2.2488), "DV_BP_Fungal_Foliage_BB72_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_Fungal_Foliage_BB73 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (7634.519, 3460.0793, 967.66895), (0.0, 0.0, -0.0), (2.6230, 2.5180, 2.1487), "DV_BP_Fungal_Foliage_BB73_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_Fungal_Foliage_BB74 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (9073.768, 3760.068, 825.7158), (0.0, 0.0, -0.0), (2.4924, 2.5094, 2.1389), "DV_BP_Fungal_Foliage_BB74_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_Fungal_Foliage_BB75_102 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (7760.8687, 660.6645, 987.9488), (0.0, 0.0, -0.0), (1.9034, 1.8936, 2.0620), "DV_BP_Fungal_Foliage_BB75_102_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_Fungal_Foliage_BB76_105 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (7433.4116, 1808.9114, 763.92346), (0.0, 0.0, -0.0), (1.8588, 1.8487, 2.0620), "DV_BP_Fungal_Foliage_BB76_105_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_Fungal_Foliage_BB78 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (5162.9136, 3558.0283, 850.2296), (0.0, 0.0, -0.0), (2.6330, 2.5720, 2.2501), "DV_BP_Fungal_Foliage_BB78_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_Fungal_Foliage_BB79 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (6142.278, 4282.331, 788.9369), (0.0, 0.0, -0.0), (2.6198, 2.8821, 2.3621), "DV_BP_Fungal_Foliage_BB79_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_Fungal_Foliage_BB8 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (10363.471, 4887.681, 1219.8467), (0.0, 0.0, -0.0), (2.2487, 2.2300, 2.2259), "DV_BP_Fungal_Foliage_BB8_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_Fungal_Foliage_BB80 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (5357.5303, 5361.664, 879.4948), (0.0, 0.0, -0.0), (2.7643, 2.6975, 2.2294), "DV_BP_Fungal_Foliage_BB80_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_Fungal_Foliage_BB81 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (5359.175, 6502.9336, 879.4948), (0.0, 0.0, -0.0), (2.6274, 2.7603, 2.2294), "DV_BP_Fungal_Foliage_BB81_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_Fungal_Foliage_BB82 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (5837.193, 5602.658, 863.58374), (0.0, 0.0, -0.0), (2.2121, 2.0242, 2.2106), "DV_BP_Fungal_Foliage_BB82_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_Fungal_Foliage_BB83 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (3404.4097, 2895.786, 856.5669), (0.0, 0.0, -0.0), (2.6506, 2.7987, 2.4355), "DV_BP_Fungal_Foliage_BB83_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_Fungal_Foliage_BB84 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (3651.406, 2044.238, 814.5536), (0.0, 0.0, -0.0), (2.4743, 2.4551, 2.3559), "DV_BP_Fungal_Foliage_BB84_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_Fungal_Foliage_BB85 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (2707.0679, 1708.7395, 802.1753), (0.0, 0.0, -0.0), (2.5276, 2.4203, 2.1699), "DV_BP_Fungal_Foliage_BB85_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_Fungal_Foliage_BB86 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (3810.3499, 2241.7205, 831.0387), (0.0, 0.0, -0.0), (2.4306, 2.7322, 2.4727), "DV_BP_Fungal_Foliage_BB86_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_Fungal_Foliage_BB87 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (3017.4648, 3076.3384, 896.8097), (0.0, 0.0, -0.0), (2.3031, 2.1098, 2.2530), "DV_BP_Fungal_Foliage_BB87_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_Fungal_Foliage_BB88 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (2570.9863, 2830.5103, 790.4672), (0.0, 0.0, -0.0), (2.1134, 2.1098, 2.1104), "DV_BP_Fungal_Foliage_BB88_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_Fungal_Foliage_BB89_123 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (2999.4763, 2841.5442, 773.5884), (0.0, 0.0, -0.0), (1.7919, 1.8023, 2.0620), "DV_BP_Fungal_Foliage_BB89_123_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_Fungal_Foliage_BB9 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (9868.838, 8104.2285, 922.04675), (0.0, 0.0, -0.0), (2.0797, 2.0665, 2.2259), "DV_BP_Fungal_Foliage_BB9_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_Fungal_Foliage_BB90 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (3673.2725, 1421.4111, 913.91736), (0.0, 0.0, -0.0), (2.2069, 2.3611, 2.2946), "DV_BP_Fungal_Foliage_BB90_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_Fungal_Foliage_BB91 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (1205.7341, 2601.9756, 783.92615), (0.0, 0.0, -0.0), (2.5276, 2.4203, 2.1699), "DV_BP_Fungal_Foliage_BB91_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_Fungal_Foliage_BB92_128 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (1790.739, 2779.2056, 801.34875), (0.0, 0.0, -0.0), (2.1751, 2.1827, 2.0620), "DV_BP_Fungal_Foliage_BB92_128_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_Fungal_Foliage_BB93 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (1373.9678, 2222.9565, 1144.8629), (0.0, 0.0, -0.0), (2.0916, 2.2067, 2.4005), "DV_BP_Fungal_Foliage_BB93_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_Fungal_Foliage_BB94 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (2916.4094, 700.9495, 785.93774), (0.0, 0.0, -0.0), (2.2242, 2.2215, 2.1699), "DV_BP_Fungal_Foliage_BB94_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_Fungal_Foliage_BB95 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (1599.8314, 8661.62, 784.6138), (0.0, 0.0, -0.0), (2.2705, 2.3658, 2.1450), "DV_BP_Fungal_Foliage_BB95_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_Fungal_Foliage_BB96 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (1062.3239, 9100.318, 737.501), (0.0, 0.0, -0.0), (2.6287, 2.5982, 2.1849), "DV_BP_Fungal_Foliage_BB96_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_Fungal_Foliage_BB97 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (1071.4932, 8518.857, 869.1896), (0.0, 0.0, -0.0), (2.6241, 2.5850, 2.1429), "DV_BP_Fungal_Foliage_BB97_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_Fungal_Foliage_BB98 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (1293.6637, 8151.8486, 989.42596), (0.0, 0.0, -0.0), (2.6189, 2.5837, 2.1420), "DV_BP_Fungal_Foliage_BB98_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_Fungal_Foliage_BB99 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (726.3613, 11342.029, 840.6884), (0.0, 0.0, -0.0), (2.3714, 2.4376, 2.1534), "DV_BP_Fungal_Foliage_BB99_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_Fungal_Foliage_BC_0 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (3226.974, 7414.5146, 1313.693), (0.0, 0.0, -0.0), (0.5468, 0.7340, 0.5410), "DV_BP_Fungal_Foliage_BC_0_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_Fungal_Foliage_BC2_2 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (2602.691, 7660.2695, 903.693), (0.0, 0.0, -0.0), (0.6008, 0.8116, 0.5410), "DV_BP_Fungal_Foliage_BC2_2_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_Fungal_Foliage_BC3_3 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (2883.3699, 7698.9395, 903.693), (0.0, 0.0, -0.0), (0.6064, 0.7779, 0.5410), "DV_BP_Fungal_Foliage_BC3_3_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_Fungal_Foliage_BC4_4 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (2930.4956, 7819.207, 903.693), (0.0, 0.0, -0.0), (0.6490, 0.7313, 0.5410), "DV_BP_Fungal_Foliage_BC4_4_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_Fungal_Foliage_BC5_5 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (2604.123, 7392.77, 903.693), (0.0, 0.0, -0.0), (0.7270, 0.5767, 0.5410), "DV_BP_Fungal_Foliage_BC5_5_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_Fungal_Foliage_BC8_9 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (6876.2197, 9666.305, 901.57886), (0.0, 0.0, -0.0), (1.7919, 1.8023, 2.0620), "DV_BP_Fungal_Foliage_BC8_9_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_Fungal_Foliage_BD_2 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (9500.25, 5836.45, 723.9706), (0.0, 0.0, -0.0), (1.7919, 1.8023, 2.0620), "DV_BP_Fungal_Foliage_BD_2_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_Fungal_Foliage_BD14_41 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (4262.826, 9927.6875, 761.6126), (0.0, 0.0, -0.0), (2.4615, 2.4884, 2.0883), "DV_BP_Fungal_Foliage_BD14_41_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_Fungal_Foliage_BD17_53 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (9655.8545, 3663.1135, 1021.2876), (0.0, 0.0, -0.0), (2.6670, 2.6613, 2.1530), "DV_BP_Fungal_Foliage_BD17_53_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_Fungal_Foliage_BD18_56 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (8119.8936, 3739.3105, 843.3943), (0.0, 0.0, -0.0), (2.6856, 2.4995, 2.2285), "DV_BP_Fungal_Foliage_BD18_56_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_Fungal_Foliage_BD19_59 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (11284.497, 3357.5789, 783.8512), (0.0, 0.0, -0.0), (2.2550, 1.8954, 2.2756), "DV_BP_Fungal_Foliage_BD19_59_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_Fungal_Foliage_BD2 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (10149.954, 5305.4517, 873.31775), (0.0, 0.0, -0.0), (2.4954, 2.3945, 2.1763), "DV_BP_Fungal_Foliage_BD2_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_Fungal_Foliage_BD20_62 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (10563.276, 1995.9072, 910.4621), (0.0, 0.0, -0.0), (2.6888, 2.7385, 2.2367), "DV_BP_Fungal_Foliage_BD20_62_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_Fungal_Foliage_BD21_65 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (7804.1274, 595.939, 1006.8086), (0.0, 0.0, -0.0), (2.5180, 2.5160, 2.0620), "DV_BP_Fungal_Foliage_BD21_65_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_Fungal_Foliage_BD22_77 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (5360.5464, 4618.012, 905.30615), (0.0, 0.0, -0.0), (2.2458, 2.1092, 2.1715), "DV_BP_Fungal_Foliage_BD22_77_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_Fungal_Foliage_BD23_71 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (4881.956, 3543.7642, 943.76245), (0.0, 0.0, -0.0), (2.1217, 2.2290, 2.1771), "DV_BP_Fungal_Foliage_BD23_71_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_Fungal_Foliage_BD24_74 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (5447.591, 2652.5554, 771.5015), (0.0, 0.0, -0.0), (1.9714, 2.0874, 2.1652), "DV_BP_Fungal_Foliage_BD24_74_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_Fungal_Foliage_BD25_80 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (2860.3186, 3080.4858, 912.01697), (0.0, 0.0, -0.0), (2.4505, 2.6001, 2.2014), "DV_BP_Fungal_Foliage_BD25_80_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_Fungal_Foliage_BD26_83 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (3447.7576, 1375.5773, 783.1111), (0.0, 0.0, -0.0), (2.6442, 2.5665, 2.1952), "DV_BP_Fungal_Foliage_BD26_83_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_Fungal_Foliage_BD27_86 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (1346.1826, 3186.7708, 996.4339), (0.0, 0.0, -0.0), (2.3940, 2.3989, 2.0620), "DV_BP_Fungal_Foliage_BD27_86_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_Fungal_Foliage_BD28_89 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (2321.9526, 3160.6555, 1026.6919), (0.0, 0.0, -0.0), (1.9605, 1.8023, 2.1661), "DV_BP_Fungal_Foliage_BD28_89_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_Fungal_Foliage_BD29_92 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (2931.8918, 980.1134, 793.4586), (0.0, 0.0, -0.0), (2.0049, 1.9958, 2.0620), "DV_BP_Fungal_Foliage_BD29_92_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_Fungal_Foliage_BD31_98 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (1055.7985, 11108.021, 852.10236), (0.0, 0.0, -0.0), (1.7919, 1.8767, 2.1104), "DV_BP_Fungal_Foliage_BD31_98_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_Fungal_Foliage_BD4_14 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (9548.522, 10477.975, 1230.1118), (0.0, 0.0, -0.0), (1.7919, 1.8023, 2.0620), "DV_BP_Fungal_Foliage_BD4_14_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_Fungal_Foliage_BD5_18 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (8472.861, 9912.283, 1039.6035), (0.0, 0.0, -0.0), (2.5191, 2.7630, 2.3664), "DV_BP_Fungal_Foliage_BD5_18_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_Fungal_Foliage_BD6_21 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (11626.672, 9957.356, 869.2571), (0.0, 0.0, -0.0), (2.4484, 2.7278, 2.3159), "DV_BP_Fungal_Foliage_BD6_21_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_Fungal_Foliage_BD8_27 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (6975.6104, 9076.77, 854.4574), (0.0, 0.0, -0.0), (1.7919, 1.8023, 2.0620), "DV_BP_Fungal_Foliage_BD8_27_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_Fungal_Foliage_BD9_30 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (7259.803, 9506.026, 880.755), (0.0, 0.0, -0.0), (2.2524, 2.4011, 2.1844), "DV_BP_Fungal_Foliage_BD9_30_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_Fungal_Foliage_BE_2 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (10143.283, 7470.7847, 822.937), (0.0, 0.0, -0.0), (2.3996, 2.6608, 2.2942), "DV_BP_Fungal_Foliage_BE_2_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_Fungal_Foliage_BE2_13 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (10789.048, 2527.605, 808.4121), (0.0, 0.0, -0.0), (2.4417, 2.4457, 2.0620), "DV_BP_Fungal_Foliage_BE2_13_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_Fungal_Foliage_BE3_2 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (3327.1514, 10998.634, 799.58496), (0.0, 0.0, -0.0), (1.8587, 1.8902, 2.1587), "DV_BP_Fungal_Foliage_BE3_2_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_Fungal_Foliage_BE4_8 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (2128.5154, 11264.481, 1127.7905), (0.0, 0.0, -0.0), (2.1713, 2.0102, 2.3077), "DV_BP_Fungal_Foliage_BE4_8_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: BP_Fungal_Foliage_Cluster_A_2 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (5264.6885, 10559.784, 1562.1421), (0.0, 0.0, -0.0), (2.4313, 2.8681, 2.7629), "DV_BP_Fungal_Foliage_Cluster_A_2_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: CBP_StoryStone_TheLowerDeeps_2 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (786.0026, 9881.297, 955.7575), (-0.0, -60.000092633621556, -0.0), (2.0000, 2.0000, 3.4389), "DV_CBP_StoryStone_TheLowerDeeps_2", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: DecorationBlockingVolume_1 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (8753.946, 11335.635, 1807.6929), (0.0, 13.614755872881249, -0.0), (12.9852, 9.2581, 7.2914), "DV_DecorationBlockingVolume_1", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: DecorationBlockingVolume_2 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (12200.0, 9600.0, 900.0), (0.0, 0.0, -0.0), (12.0000, 4.0000, 2.0000), "DV_DecorationBlockingVolume_2", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: DecorationBlockingVolume_3 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (5359.381, 11734.09, 1951.4832), (-0.0, -27.72448487127817, -0.0), (20.8982, 9.3507, 9.6340), "DV_DecorationBlockingVolume_3", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: DecorationBlockingVolume_4 (EMorSimpleShape::Empty)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (11250.0, 3900.0, 1250.0), (0.0, 0.0, -0.0), (2.0000, 2.0000, 2.0000), "DV_DecorationBlockingVolume_4", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: DecorationBlockingVolume_5 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (11927.117, 6365.63, 1821.729), (0.0, 5.278794225679529, -0.0), (13.5111, 14.6291, 8.4650), "DV_DecorationBlockingVolume_5", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: DecorationBlockingVolume_6 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (10160.768, 3614.4304, 942.0863), (0.0, 4.112010301950224, -0.0), (2.0000, 2.0000, 2.0000), "DV_DecorationBlockingVolume_6", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: DecorationBlockingVolume_7 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (6062.527, 852.7739, 1944.6743), (-0.0, -43.48126168205142, -0.0), (14.4843, 9.6340, 9.7303), "DV_DecorationBlockingVolume_7", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: DecorationBlockingVolume_9 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (1157.7571, 1849.1835, 1534.807), (-0.0, -22.199158903256752, -0.0), (11.1848, 11.1781, 9.7303), "DV_DecorationBlockingVolume_9", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: DecorationBlockingVolume_12 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (1278.8287, 3799.9194, 1665.3047), (-0.0, -0.0769958493740782, -0.0), (10.7473, 7.8955, 8.4650), "DV_DecorationBlockingVolume_12", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: DecorationBlockingVolume_20 (EMorSimpleShape::Empty)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (6016.575, 2138.752, 800.0), (-0.0, -15.000058335092751, -0.0), (2.0000, 2.0000, 2.0000), "DV_DecorationBlockingVolume_20", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: DecorationBlockingVolume10 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (1331.4673, 1506.7448, 1534.807), (-0.0, -39.420226717708495, -0.0), (11.1848, 11.1781, 9.7303), "DV_DecorationBlockingVolume10", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: DecorationBlockingVolume11 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (9600.0, 600.0, 900.0), (0.0, 0.0, -0.0), (4.0000, 12.0000, 2.0000), "DV_DecorationBlockingVolume11", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: DecorationBlockingVolume13 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (12200.0, 3200.0, 900.0), (0.0, 0.0, -0.0), (12.0000, 4.0000, 2.0000), "DV_DecorationBlockingVolume13", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: DecorationBlockingVolume14 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (600.0, 3200.0, 900.0), (0.0, 0.0, -0.0), (12.0000, 4.0000, 2.0000), "DV_DecorationBlockingVolume14", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: DecorationBlockingVolume15 (EMorSimpleShape::Empty)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (9332.584, 4129.631, 1250.0), (0.0, 25.00005828883052, -0.0), (2.0000, 2.0000, 2.0000), "DV_DecorationBlockingVolume15", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: DecorationBlockingVolume16 (EMorSimpleShape::Empty)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (7763.762, 3829.4482, 1250.0), (0.0, 5.000134649533364, -0.0), (2.0000, 2.0000, 2.0000), "DV_DecorationBlockingVolume16", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: DecorationBlockingVolume17 (EMorSimpleShape::Empty)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (11554.902, 2171.891, 1250.0), (0.0, 30.000056363592833, -0.0), (2.0000, 2.0000, 2.0000), "DV_DecorationBlockingVolume17", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: DecorationBlockingVolume18 (EMorSimpleShape::Empty)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (11082.186, 1090.6732, 1250.0), (0.0, 30.000056363592833, -0.0), (2.0000, 2.0000, 2.0000), "DV_DecorationBlockingVolume18", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: DecorationBlockingVolume19 (EMorSimpleShape::Empty)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (11271.787, 4799.048, 1600.0), (0.0, 84.99997401305096, -0.0), (2.0000, 2.0000, 2.0000), "DV_DecorationBlockingVolume19", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: DecorationBlockingVolume20 (EMorSimpleShape::Empty)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (10541.661, 6014.383, 900.0), (0.0, 70.00006109847311, -0.0), (2.0000, 2.0000, 2.0000), "DV_DecorationBlockingVolume20", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: DecorationBlockingVolume21 (EMorSimpleShape::Empty)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (11110.136, 7137.6978, 900.0), (0.0, 70.00006109847311, -0.0), (2.0000, 2.0000, 2.0000), "DV_DecorationBlockingVolume21", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: DecorationBlockingVolume22 (EMorSimpleShape::Empty)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (10678.811, 7560.734, 900.0), (0.0, 70.00006109847311, -0.0), (2.0000, 2.0000, 2.0000), "DV_DecorationBlockingVolume22", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: DecorationBlockingVolume23 (EMorSimpleShape::Empty)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (7935.6133, 7849.9814, 900.0), (0.0, 90.00001925454748, -0.0), (2.0000, 2.0000, 2.0000), "DV_DecorationBlockingVolume23", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: DecorationBlockingVolume24 (EMorSimpleShape::Empty)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (8035.6133, 10049.981, 900.0), (0.0, 90.00001925454748, -0.0), (2.0000, 2.0000, 2.0000), "DV_DecorationBlockingVolume24", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: DecorationBlockingVolume25 (EMorSimpleShape::Empty)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (6721.5854, 10449.981, 900.0), (0.0, 90.00001925454748, -0.0), (2.0000, 2.0000, 2.0000), "DV_DecorationBlockingVolume25", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: DecorationBlockingVolume26 (EMorSimpleShape::Empty)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (5559.009, 10385.702, 900.0), (0.0, 39.99996194656455, -0.0), (2.0000, 2.0000, 2.0000), "DV_DecorationBlockingVolume26", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: DecorationBlockingVolume27 (EMorSimpleShape::Empty)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (4213.8975, 7789.9453, 900.0), (0.0, 120.00000959706765, -0.0), (2.0000, 2.0000, 2.0000), "DV_DecorationBlockingVolume27", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: DecorationBlockingVolume28 (EMorSimpleShape::Empty)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (4807.7295, 3644.9697, 800.0), (0.0, 59.99997596179053, -0.0), (2.0000, 2.0000, 2.0000), "DV_DecorationBlockingVolume28", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: DecorationBlockingVolume29 (EMorSimpleShape::Empty)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (3914.6372, 1507.2043, 800.0), (0.0, 74.99998137898993, -0.0), (2.0000, 2.0000, 2.0000), "DV_DecorationBlockingVolume29", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: DecorationBlockingVolume30 (EMorSimpleShape::Empty)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (2453.821, 1301.3185, 1250.0), (0.0, 105.00001874691905, -0.0), (2.0000, 2.0000, 2.0000), "DV_DecorationBlockingVolume30", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: DecorationBlockingVolume31 (EMorSimpleShape::Empty)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (3155.178, 3156.7886, 1250.0), (0.0, 174.9999157649341, -0.0), (2.0000, 2.0000, 2.0000), "DV_DecorationBlockingVolume31", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: DecorationBlockingVolume32 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (10497.305, 10492.803, 1050.0), (-0.0, -63.283693848418935, -0.0), (12.0000, 4.0000, 2.0000), "DV_DecorationBlockingVolume32", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: DecorationBlockingVolume33 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (6605.386, 8282.4375, 1334.807), (0.0, 22.800852668673006, -0.0), (11.1848, 11.1781, 9.7303), "DV_DecorationBlockingVolume33", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: DecorationBlockingVolume34 (EMorSimpleShape::Empty)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (3780.758, 11167.089, 900.0), (0.0, 65.00000013753403, -0.0), (2.0000, 2.0000, 2.0000), "DV_DecorationBlockingVolume34", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: DecorationBlockingVolume35 (EMorSimpleShape::Empty)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (1787.1001, 11304.931, 900.0), (0.0, 85.21603193428855, -0.0), (2.0000, 2.0000, 2.0000), "DV_DecorationBlockingVolume35", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: DecorationBlockingVolume36 (EMorSimpleShape::Empty)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (1444.207, 8562.188, 900.0), (0.0, 85.21603193428855, -0.0), (2.0000, 2.0000, 2.0000), "DV_DecorationBlockingVolume36", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: DecorationBlockingVolume37 (EMorSimpleShape::Empty)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (3974.0088, 8284.773, 900.0), (0.0, 128.14721107530252, -0.0), (2.0000, 2.0000, 2.0000), "DV_DecorationBlockingVolume37", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: DecorationBlockingVolume38 (EMorSimpleShape::Empty)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (9804.4, 8037.9336, 900.0), (0.0, 111.1545171065685, -0.0), (2.0000, 2.0000, 2.0000), "DV_DecorationBlockingVolume38", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: DecorationBlockingVolume39 (EMorSimpleShape::Empty)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (10621.0, 8543.073, 900.0), (0.0, 111.1545171065685, -0.0), (2.0000, 2.0000, 2.0000), "DV_DecorationBlockingVolume39", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: DecorationBlockingVolume4 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (600.0, 9600.0, 900.0), (0.0, 0.0, -0.0), (12.0000, 4.0000, 2.0000), "DV_DecorationBlockingVolume4", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: DecorationBlockingVolume40 (EMorSimpleShape::Empty)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (8591.3955, 6003.615, 900.0), (0.0, 132.49983071246024, -0.0), (2.0000, 2.0000, 2.0000), "DV_DecorationBlockingVolume40", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: DecorationBlockingVolume41 (EMorSimpleShape::Empty)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (8241.09, 1457.7721, 1271.7172), (0.0, 5.000134304778899, -0.0), (2.0000, 2.0000, 2.0000), "DV_DecorationBlockingVolume41", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: DecorationBlockingVolume42 (EMorSimpleShape::Empty)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (9273.647, 1359.6127, 1271.7172), (-0.0, -25.736724039260537, -0.0), (2.0000, 2.0000, 2.0000), "DV_DecorationBlockingVolume42", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: DecorationBlockingVolume43 (EMorSimpleShape::Empty)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (7417.731, 1457.7856, 1271.7172), (0.0, 2.162550092755297, -0.0), (2.0000, 2.0000, 2.0000), "DV_DecorationBlockingVolume43", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: DecorationBlockingVolume44 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (10405.819, 4567.447, 1141.9152), (-0.0, -56.05627338180219, -0.0), (2.0000, 2.0000, 2.0000), "DV_DecorationBlockingVolume44", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: DecorationBlockingVolume45 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (10959.904, 6211.898, 1271.8672), (-0.0, -40.110106256410006, -0.0), (2.0000, 2.0000, 2.0000), "DV_DecorationBlockingVolume45", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: DecorationBlockingVolume46 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (9873.327, 5086.683, 990.4065), (-0.0, -0.23330687301984113, -0.0), (2.0000, 2.0000, 2.0000), "DV_DecorationBlockingVolume46", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: DecorationBlockingVolume47 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (9873.669, 5590.1045, 809.3411), (0.0, 1.970841525482234, -0.0), (2.0000, 2.0000, 2.0000), "DV_DecorationBlockingVolume47", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: DecorationBlockingVolume48 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (7128.046, 2174.4236, 770.7824), (-0.0, -19.856933889735497, -0.0), (2.0000, 2.0000, 2.0000), "DV_DecorationBlockingVolume48", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: DecorationBlockingVolume49 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (7064.8096, 1739.5588, 913.08075), (0.0, 4.3566309691475364, -0.0), (2.0000, 2.0000, 2.0000), "DV_DecorationBlockingVolume49", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: DecorationBlockingVolume50 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (6809.929, 1490.7559, 1132.8677), (0.0, 1.086537704195144, -0.0), (2.0000, 2.0000, 2.0000), "DV_DecorationBlockingVolume50", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: DecorationBlockingVolume51 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (5770.9727, 4236.046, 822.85535), (-0.0, -74.18103932250722, -0.0), (2.0000, 2.0000, 2.0000), "DV_DecorationBlockingVolume51", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: DecorationBlockingVolume52 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (5486.0547, 7291.582, 827.7008), (-0.0, -74.18103932250722, -0.0), (2.0000, 2.0000, 2.0000), "DV_DecorationBlockingVolume52", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: DecorationBlockingVolume53 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (4047.429, 10213.196, 827.7021), (-0.0, -129.36857108791824, -0.0), (2.0000, 2.0000, 2.0000), "DV_DecorationBlockingVolume53", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: DecorationBlockingVolume54 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (4452.9873, 10661.576, 1183.0825), (-0.0, -129.36857108791824, -0.0), (2.0000, 2.0000, 2.0000), "DV_DecorationBlockingVolume54", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: DecorationBlockingVolume6 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (3200.0, 12200.0, 900.0), (0.0, 0.0, -0.0), (4.0000, 12.0000, 2.0000), "DV_DecorationBlockingVolume6", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: DecorationBlockingVolume8 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (3200.0, 600.0, 900.0), (0.0, 0.0, -0.0), (4.0000, 12.0000, 2.0000), "DV_DecorationBlockingVolume8", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: Flora_Fungal_Tree_Large3_503 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (8766.281, 3744.5452, 738.1641), (0.0, 0.0, -0.0), (4.2168, 4.4194, 3.1480), "DV_Flora_Fungal_Tree_Large3_503_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: Flora_Fungal_Tree_Large4 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (7716.1963, 940.53546, 836.1916), (0.0, 0.0, -0.0), (3.9821, 3.8839, 3.5275), "DV_Flora_Fungal_Tree_Large4_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: Flora_Fungal_Tree_Large5 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (8126.6504, 8711.967, 759.98566), (0.0, 0.0, -0.0), (4.6411, 4.4604, 3.6867), "DV_Flora_Fungal_Tree_Large5_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: Flora_Fungal_Tree_Large6 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (6751.6396, 3491.4548, 663.7075), (0.0, 0.0, -0.0), (3.4573, 3.4396, 2.8237), "DV_Flora_Fungal_Tree_Large6_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: Flora_Fungal_Tree_Large7 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (8418.816, 9554.92, 876.8188), (0.0, 0.0, -0.0), (4.8961, 4.7360, 3.3362), "DV_Flora_Fungal_Tree_Large7_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: Flora_Fungal_Tree_Large8 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (7236.351, 9705.437, 832.1843), (0.0, 0.0, -0.0), (4.4746, 4.6229, 3.4065), "DV_Flora_Fungal_Tree_Large8_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: Flora_Fungal_Tree_Large9 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (10995.123, 673.6984, 769.4911), (0.0, 0.0, -0.0), (3.7957, 3.5963, 3.1569), "DV_Flora_Fungal_Tree_Large9_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: Flora_Fungal_Tree_Medium11 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (3919.7124, 8090.6904, 815.74304), (0.0, 0.0, -0.0), (4.5855, 4.7949, 3.1567), "DV_Flora_Fungal_Tree_Medium11_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: Flora_Fungal_Tree_Medium2 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (6598.9595, 8479.16, 1065.1715), (0.0, 0.0, -0.0), (4.4061, 4.4909, 2.9426), "DV_Flora_Fungal_Tree_Medium2_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: Flora_Fungal_Tree_Medium3_420 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (11182.741, 3494.379, 765.7103), (0.0, 0.0, -0.0), (4.2516, 4.3515, 3.1063), "DV_Flora_Fungal_Tree_Medium3_420_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: Flora_Fungal_Tree_Medium4 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (1542.4164, 8174.784, 938.4534), (0.0, 0.0, -0.0), (4.4303, 4.4374, 2.8237), "DV_Flora_Fungal_Tree_Medium4_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: Flora_Fungal_Tree_Medium6 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (8046.6025, 7756.584, 839.13135), (0.0, 0.0, -0.0), (3.4796, 3.4621, 2.8237), "DV_Flora_Fungal_Tree_Medium6_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: Flora_Fungal_Tree_Medium7 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (3563.13, 11154.099, 767.5929), (0.0, 0.0, -0.0), (4.5078, 4.5023, 2.8237), "DV_Flora_Fungal_Tree_Medium7_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: Flora_Fungal_Tree_Medium8 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (10384.017, 9861.991, 864.1786), (0.0, 0.0, -0.0), (4.5831, 4.5226, 3.0404), "DV_Flora_Fungal_Tree_Medium8_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: Flora_Fungal_Tree_Medium9 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (2718.0376, 11550.749, 799.4944), (0.0, 0.0, -0.0), (4.5506, 4.5545, 2.8237), "DV_Flora_Fungal_Tree_Medium9_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: Flora_Fungal_Tree_Small4_32 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (10060.043, 8144.995, 905.2335), (0.0, 0.0, -0.0), (4.3896, 4.3732, 2.7080), "DV_Flora_Fungal_Tree_Small4_32_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: Flora_Fungal_Tree_X_Small_65 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (4547.389, 8151.2393, 809.7007), (0.0, 0.0, -0.0), (4.2209, 4.2394, 2.7791), "DV_Flora_Fungal_Tree_X_Small_65_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: Flora_Fungal_Tree_X_Small2_253 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (7689.7085, 8847.34, 925.3489), (0.0, 0.0, -0.0), (4.6500, 4.9471, 3.4544), "DV_Flora_Fungal_Tree_X_Small2_253_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: Flora_Fungal_Tree_X_Small4 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (5700.9214, 8379.683, 871.9182), (0.0, 0.0, -0.0), (4.0669, 4.1735, 2.7452), "DV_Flora_Fungal_Tree_X_Small4_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: Flora_Fungal_Tree_X_Small5_910 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (3653.054, 1660.2104, 884.3538), (0.0, 0.0, -0.0), (4.1792, 4.1683, 2.5250), "DV_Flora_Fungal_Tree_X_Small5_910_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: Fungal_Foliage_BA14 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (8209.169, 1419.0005, 773.2089), (0.0, 0.0, -0.0), (2.2116, 2.0892, 2.2746), "DV_Fungal_Foliage_BA14_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: Fungal_Foliage_BA15 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (9533.602, 4817.1997, 1038.8682), (0.0, 0.0, -0.0), (2.5817, 2.7667, 2.2651), "DV_Fungal_Foliage_BA15_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: Fungal_Foliage_BA16 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (7069.154, 9754.025, 894.22314), (0.0, 0.0, -0.0), (1.8938, 2.1575, 2.2482), "DV_Fungal_Foliage_BA16_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: Fungal_Foliage_BA17 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (9853.753, 7541.6616, 675.54736), (0.0, 0.0, -0.0), (2.1824, 1.9997, 2.1838), "DV_Fungal_Foliage_BA17_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: Fungal_Foliage_BA19 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (9110.761, 6459.2056, 694.8392), (0.0, 0.0, -0.0), (2.6974, 2.6074, 2.2875), "DV_Fungal_Foliage_BA19_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: Fungal_Foliage_BA20 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (8291.388, 7573.518, 830.7799), (0.0, 0.0, -0.0), (2.7579, 2.7684, 2.2875), "DV_Fungal_Foliage_BA20_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: Fungal_Foliage_BA21 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (8316.795, 8723.172, 750.3969), (0.0, 0.0, -0.0), (2.7289, 2.6117, 2.3077), "DV_Fungal_Foliage_BA21_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: Fungal_Foliage_BA22 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (8575.298, 9987.917, 1064.0066), (0.0, 0.0, -0.0), (2.4206, 2.4368, 2.0734), "DV_Fungal_Foliage_BA22_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: Fungal_Foliage_BA23 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (9721.267, 9991.633, 863.27185), (0.0, 0.0, -0.0), (2.6473, 2.5292, 2.2255), "DV_Fungal_Foliage_BA23_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: Fungal_Foliage_BA24_31 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (10559.468, 9758.502, 900.89685), (0.0, 0.0, -0.0), (2.5917, 2.6522, 2.2329), "DV_Fungal_Foliage_BA24_31_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: Fungal_Foliage_BA25 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (8710.757, 9783.833, 847.6279), (0.0, 0.0, -0.0), (2.0149, 2.1715, 2.2382), "DV_Fungal_Foliage_BA25_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: Fungal_Foliage_BA26 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (11175.852, 9915.35, 953.6981), (0.0, 0.0, -0.0), (2.5430, 2.8405, 2.3626), "DV_Fungal_Foliage_BA26_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: Fungal_Foliage_BA28 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (7457.528, 8814.277, 1034.4764), (0.0, 0.0, -0.0), (2.5071, 2.6317, 2.2743), "DV_Fungal_Foliage_BA28_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: Fungal_Foliage_BA30 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (5683.569, 10203.475, 1206.5283), (0.0, 0.0, -0.0), (1.9535, 2.1575, 2.2728), "DV_Fungal_Foliage_BA30_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: Fungal_Foliage_BA31 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (4727.56, 10456.824, 1128.1104), (0.0, 0.0, -0.0), (2.6972, 2.6751, 2.2440), "DV_Fungal_Foliage_BA31_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: Fungal_Foliage_BA33 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (4309.0464, 11205.962, 1356.043), (0.0, 0.0, -0.0), (2.4644, 2.6173, 2.2265), "DV_Fungal_Foliage_BA33_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: Fungal_Foliage_BA35 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (9583.405, 3799.915, 1051.5061), (0.0, 0.0, -0.0), (2.6668, 2.6807, 2.1838), "DV_Fungal_Foliage_BA35_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: Fungal_Foliage_BA36 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (8016.5293, 3326.0652, 878.5804), (0.0, 0.0, -0.0), (2.2598, 2.1572, 2.2196), "DV_Fungal_Foliage_BA36_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: Fungal_Foliage_BA38 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (5154.897, 3595.4934, 858.2428), (0.0, 0.0, -0.0), (2.3626, 2.1018, 2.2486), "DV_Fungal_Foliage_BA38_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: Fungal_Foliage_BA39 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (6176.179, 4299.254, 800.1133), (0.0, 0.0, -0.0), (2.4893, 2.7771, 2.3507), "DV_Fungal_Foliage_BA39_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: Fungal_Foliage_BA40 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (3432.0676, 2922.1177, 865.14624), (0.0, 0.0, -0.0), (2.8245, 2.8842, 2.3230), "DV_Fungal_Foliage_BA40_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: Fungal_Foliage_BA41 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (3650.424, 2006.1824, 824.84094), (0.0, 0.0, -0.0), (2.2615, 1.9355, 2.3292), "DV_Fungal_Foliage_BA41_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: Fungal_Foliage_BA42 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (2677.7686, 1733.8158, 802.75244), (0.0, 0.0, -0.0), (2.6290, 2.7128, 2.2137), "DV_Fungal_Foliage_BA42_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: Fungal_Foliage_BA43 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (1176.4352, 2627.0522, 784.5032), (0.0, 0.0, -0.0), (2.6290, 2.7128, 2.2137), "DV_Fungal_Foliage_BA43_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: Fungal_Foliage_BA44 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (1337.152, 2233.8232, 1152.3518), (0.0, 0.0, -0.0), (2.3747, 2.6548, 2.2853), "DV_Fungal_Foliage_BA44_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: Fungal_Foliage_BA45 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (2918.7249, 739.4451, 786.5149), (0.0, 0.0, -0.0), (2.1619, 2.0084, 2.2137), "DV_Fungal_Foliage_BA45_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: Fungal_Foliage_BA46 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (1316.5072, 8120.9136, 979.44415), (0.0, 0.0, -0.0), (2.5924, 2.6988, 2.2046), "DV_Fungal_Foliage_BA46_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: Fungal_Foliage_BB_0 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (2637.9841, 7596.0786, 948.818), (0.0, 0.0, -0.0), (1.3825, 1.2882, 1.3789), "DV_Fungal_Foliage_BB_0_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: Fungal_Foliage_BB2_1 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (3103.0645, 7288.7573, 1358.818), (0.0, 0.0, -0.0), (1.3825, 1.2882, 1.3789), "DV_Fungal_Foliage_BB2_1_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: Fungal_Foliage_BC_1 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (3537.813, 7605.412, 903.693), (0.0, 0.0, -0.0), (0.7340, 0.5468, 0.5410), "DV_Fungal_Foliage_BC_1_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: Mining_Dirt_Mound_A5_3 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (2494.515, 7390.098, 891.4355), (0.0, 0.0, -0.0), (1.8850, 1.9447, 0.2310), "DV_Mining_Dirt_Mound_A5_3_BRK", _folder)
if a: placed += 1
else: skipped += 1
# DecoVolume: Mining_Dirt_Mound_B2_4 (EMorSimpleShape::OrientedBox)
a = spawn_static_mesh("/Engine/BasicShapes/Cube", [], (2478.0051, 7302.3877, 890.16986), (0.0, 0.0, -0.0), (1.8594, 1.9500, 0.4034), "DV_Mining_Dirt_Mound_B2_4_BRK", _folder)
if a: placed += 1
else: skipped += 1

# ======================================================================
# SUMMARY
# ======================================================================
unreal.log(f"[{BUBBLE_NAME}] Reconstruction complete: {placed} placed, {skipped} skipped, {errors} errors")
