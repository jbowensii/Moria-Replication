"""Batch add position entries to bubble files."""
import json
from pathlib import Path

BUBBLES_DIR = Path(__file__).resolve().parent.parent / 'bubbles'
COORD_EPSILON = 50.0

def position_exists(existing, new_entry):
    new_mesh = new_entry['mesh'].split('-')[0]
    new_local = new_entry.get('local', [0,0,0])
    for pe in existing:
        ex_mesh = pe.get('mesh', '').split('-')[0]
        if new_mesh != ex_mesh:
            continue
        ex_local = pe.get('local', [0,0,0])
        if (abs(new_local[0]-ex_local[0]) < COORD_EPSILON and
            abs(new_local[1]-ex_local[1]) < COORD_EPSILON and
            abs(new_local[2]-ex_local[2]) < COORD_EPSILON):
            return True
    return False

def add_to_bubble(filename, entries):
    bf = BUBBLES_DIR / filename
    with open(bf, 'r', encoding='utf-8') as f:
        data = json.load(f)
    if 'position_entries' not in data:
        data['position_entries'] = []
    added = 0
    for entry in entries:
        if not position_exists(data['position_entries'], entry):
            data['position_entries'].append(entry)
            added += 1
    with open(bf, 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=2, ensure_ascii=False)
    print(f"  {filename}: +{added} position entries (total: {len(data['position_entries'])})")

# --- Western_Mines ---
western_entries = [
    {"mesh":"Ruin_Column_Medium_A_2_Shaft-MI_Ruin_Column_Mat_A-BlockAll-dcl-L100","bubble":"Western_Mines","world":[45784.37,113974.80,2474.37],"local":[10734.37,2474.80,774.37]},
    {"mesh":"PWM_Quarry_1x1x1_A-ProcMaterial_Quarry_Atlas-BlockAll-dcl-L100","bubble":"Western_Mines","world":[45488.92,113820.53,2539.70],"local":[10438.92,2320.53,839.70]},
    {"mesh":"Suburbs_Floor_3x3m_AA_Broken-M_GuideMeshFloor_Urban_Dirt-BlockAll-dcl-L100","bubble":"Western_Mines","world":[46930.00,114550.00,2520.00],"local":[11880.00,3050.00,820.00]},
    {"mesh":"Suburbs_Floor_3x3m_AA_Broken-M_GuideMeshFloor_Urban_Dirt-BlockAll-dcl-L100","bubble":"Western_Mines","world":[46630.00,114550.00,2520.00],"local":[11580.00,3050.00,820.00]},
    {"mesh":"PWM_Quarry_1x1x1_A-ProcMaterial_Quarry_Atlas-BlockAll-dcl-L100","bubble":"Western_Mines","world":[46672.93,114979.14,2525.00],"local":[11622.93,3479.14,825.00]},
    {"mesh":"PWM_Quarry_1X1x1_C-ProcMaterial_Quarry_Atlas-BlockAll-dcl-L100","bubble":"Western_Mines","world":[47390.00,115180.00,2515.00],"local":[12340.00,3680.00,815.00]},
    {"mesh":"PWM_Quarry_1X1x1_C-ProcMaterial_Quarry_Atlas-BlockAll-dcl-L100","bubble":"Western_Mines","world":[47323.11,116848.31,2600.00],"local":[12273.11,5348.31,900.00]},
    {"mesh":"PWM_Quarry_1X1x1_C-ProcMaterial_Quarry_Atlas-BlockAll-dcl-L100","bubble":"Western_Mines","world":[47140.00,116720.00,2590.00],"local":[12090.00,5220.00,890.00]},
    {"mesh":"PWM_Quarry_1x1x1_A-ProcMaterial_Quarry_Atlas-BlockAll-dcl-L100","bubble":"Western_Mines","world":[47534.34,116552.76,2685.51],"local":[12484.34,5052.76,985.51]},
    {"mesh":"PWM_Quarry_2x2x2_A-ProcMaterial_Quarry_Atlas-BlockAll-dcl-L100","bubble":"Western_Mines","world":[42721.71,117201.72,2530.00],"local":[7671.71,5701.72,830.00]},
    {"mesh":"PWM_Quarry_1x1x1_A-ProcMaterial_Quarry_Atlas-BlockAll-dcl-L100","bubble":"Western_Mines","world":[45270.00,116665.00,2504.00],"local":[10220.00,5165.00,804.00]},
    {"mesh":"PWM_Quarry_2x2x2_A-ProcMaterial_Quarry_Atlas-BlockAll-dcl-L100","bubble":"Western_Mines","world":[45150.00,116430.00,2500.00],"local":[10100.00,4930.00,800.00]},
    {"mesh":"PWM_Quarry_1x1x1_A-ProcMaterial_Quarry_Atlas-BlockAll-dcl-L100","bubble":"Western_Mines","world":[42650.00,116365.00,1785.00],"local":[7600.00,4865.00,85.00]},
    {"mesh":"PWM_Quarry_1X1x1_C-ProcMaterial_Quarry_Atlas-BlockAll-dcl-L100","bubble":"Western_Mines","world":[42802.66,116460.18,1800.60],"local":[7752.66,4960.18,100.60]},
    {"mesh":"PWM_Quarry_1X1x1_C-ProcMaterial_Quarry_Atlas-BlockAll-dcl-L100","bubble":"Western_Mines","world":[42115.00,116210.00,1755.00],"local":[7065.00,4710.00,55.00]},
    {"mesh":"PWM_Quarry_1x1x1_A-ProcMaterial_Quarry_Atlas-BlockAll-dcl-L100","bubble":"Western_Mines","world":[41118.06,113788.99,1780.00],"local":[6068.06,2288.99,80.00]},
    {"mesh":"PWM_Quarry_2x2x2_A-ProcMaterial_Quarry_Atlas-BlockAll-dcl-L100","bubble":"Western_Mines","world":[41218.30,113206.34,1800.00],"local":[6168.30,1706.34,100.00]},
    {"mesh":"PWM_Quarry_1x1x1_A-ProcMaterial_Quarry_Atlas-BlockAll-dcl-L100","bubble":"Western_Mines","world":[39070.00,114200.00,1700.00],"local":[4020.00,2700.00,0.00]},
    {"mesh":"PWM_Quarry_1X1x1_C-ProcMaterial_Quarry_Atlas-BlockAll-dcl-L100","bubble":"Western_Mines","world":[39160.00,114070.00,1740.00],"local":[4110.00,2570.00,40.00]},
    {"mesh":"PWM_Quarry_2x2x2_A-ProcMaterial_Quarry_Atlas-BlockAll-dcl-L100","bubble":"Western_Mines","world":[39190.00,114965.00,1720.00],"local":[4140.00,3465.00,20.00]},
    {"mesh":"PWM_Quarry_1X1x1_C-ProcMaterial_Quarry_Atlas-BlockAll-dcl-L100","bubble":"Western_Mines","world":[38996.98,114170.61,1720.00],"local":[3946.98,2670.61,20.00]},
    {"mesh":"PWM_Quarry_1x1x1_A-ProcMaterial_Quarry_Atlas-BlockAll-dcl-L100","bubble":"Western_Mines","world":[37250.00,116150.00,2950.00],"local":[2200.00,4650.00,1250.00]},
    {"mesh":"PWM_Quarry_1x1x1_A-ProcMaterial_Quarry_Atlas-BlockAll-dcl-L100","bubble":"Western_Mines","world":[36865.93,116312.57,2838.88],"local":[1815.93,4812.57,1138.88]},
    {"mesh":"Ruin_Column_Medium_A_2_Shaft-MI_Ruin_Column_Mat_A-BlockAll-dcl-L100","bubble":"Western_Mines","world":[37824.42,114379.41,3537.73],"local":[2774.42,2879.41,1837.73]},
    {"mesh":"Ruin_Column_Medium_A_2_Shaft-MI_Ruin_Column_Mat_A-BlockAll-dcl-L100","bubble":"Western_Mines","world":[37800.00,114650.00,3679.85],"local":[2750.00,3150.00,1979.85]},
    {"mesh":"Ruin_Column_Medium_A_1_Base-MI_Ruin_Column_Mat_A-BlockAll-dcl-L100","bubble":"Western_Mines","world":[37800.00,114650.00,3479.85],"local":[2750.00,3150.00,1779.85]},
    {"mesh":"PWM_Quarry_2x2x2_A-ProcMaterial_Quarry_Atlas-BlockAll-dcl-L100","bubble":"Western_Mines","world":[37300.00,112500.00,5700.00],"local":[2250.00,1000.00,4000.00]},
    {"mesh":"PWM_Quarry_1x1x1_A-ProcMaterial_Quarry_Atlas-BlockAll-dcl-L100","bubble":"Western_Mines","world":[37288.94,111734.86,5680.00],"local":[2238.94,234.86,3980.00]},
    {"mesh":"PWM_Quarry_1X1x1_C-ProcMaterial_Quarry_Atlas-BlockAll-dcl-L100","bubble":"Western_Mines","world":[37010.00,111880.00,5680.00],"local":[1960.00,380.00,3980.00]},
    {"mesh":"PWM_Quarry_1x1x1_A-ProcMaterial_Quarry_Atlas-BlockAll-dcl-L100","bubble":"Western_Mines","world":[37150.00,112500.00,5690.00],"local":[2100.00,1000.00,3990.00]},
    {"mesh":"PWM_Quarry_1X1x1_C-ProcMaterial_Quarry_Atlas-BlockAll-dcl-L100","bubble":"Western_Mines","world":[35950.00,113550.00,5700.00],"local":[900.00,2050.00,4000.00]},
]

# --- The_Great_Forge_of_Narvi ---
narvi_entries = [
    {"mesh":"PWM_Quarry_2x2x2_A-ProcMaterial_Quarry_Atlas-BlockAll-dcl-L100","bubble":"The_Great_Forge_of_Narvi","world":[28212.28,116227.62,5953.77],"local":[12362.28,17527.62,4253.77]},
    {"mesh":"PWM_Quarry_1X1x1_C-ProcMaterial_Quarry_Atlas-BlockAll-dcl-L100","bubble":"The_Great_Forge_of_Narvi","world":[28368.32,116213.82,5920.00],"local":[12518.32,17513.82,4220.00]},
    {"mesh":"PWM_Quarry_1x1x1_A-ProcMaterial_Quarry_Atlas-BlockAll-dcl-L100","bubble":"The_Great_Forge_of_Narvi","world":[28210.00,116090.00,5920.00],"local":[12360.00,17390.00,4220.00]},
    {"mesh":"PWM_Quarry_1X1x1_C-ProcMaterial_Quarry_Atlas-BlockAll-dcl-L100","bubble":"The_Great_Forge_of_Narvi","world":[28242.55,115728.47,5830.48],"local":[12392.55,17028.47,4130.48]},
    {"mesh":"PWM_Quarry_8x8x8_A-ProcMaterial_Quarry_Atlas-Custom-dcl-L100","bubble":"The_Great_Forge_of_Narvi","world":[28214.24,115373.34,5755.86],"local":[12364.24,16673.34,4055.86]},
    {"mesh":"PWM_Quarry_4x8x3-ProcMaterial_Quarry_Atlas_A-BlockAll-dcl-L100","bubble":"The_Great_Forge_of_Narvi","world":[28207.81,115003.73,5750.44],"local":[12357.81,16303.73,4050.44]},
    {"mesh":"PWM_Quarry_2x2x2_A-ProcMaterial_Quarry_Atlas-BlockAll-dcl-L100","bubble":"The_Great_Forge_of_Narvi","world":[28195.76,115226.75,5735.00],"local":[12345.76,16526.75,4035.00]},
    {"mesh":"PWM_Quarry_2x2x2_A-ProcMaterial_Quarry_Atlas-BlockAll-dcl-L100","bubble":"The_Great_Forge_of_Narvi","world":[28415.09,114732.40,5730.00],"local":[12565.09,16032.40,4030.00]},
    {"mesh":"PWM_Quarry_1X1x1_C-ProcMaterial_Quarry_Atlas-BlockAll-dcl-L100","bubble":"The_Great_Forge_of_Narvi","world":[28590.00,114796.08,5760.00],"local":[12740.00,16096.08,4060.00]},
    {"mesh":"PWM_Quarry_1x1x1_A-ProcMaterial_Quarry_Atlas-BlockAll-dcl-L100","bubble":"The_Great_Forge_of_Narvi","world":[28309.66,114551.20,5720.00],"local":[12459.66,15851.20,4020.00]},
    {"mesh":"PWM_Quarry_2x2x2_A-ProcMaterial_Quarry_Atlas-BlockAll-dcl-L100","bubble":"The_Great_Forge_of_Narvi","world":[28134.95,114518.70,5760.00],"local":[12284.95,15818.70,4060.00]},
    {"mesh":"PWM_Quarry_1X1x1_C-ProcMaterial_Quarry_Atlas-BlockAll-dcl-L100","bubble":"The_Great_Forge_of_Narvi","world":[28096.77,114334.77,5698.82],"local":[12246.77,15634.77,3998.82]},
    {"mesh":"PWM_Quarry_1X1x1_C-ProcMaterial_Quarry_Atlas-BlockAll-dcl-L100","bubble":"The_Great_Forge_of_Narvi","world":[26554.00,113751.64,5367.74],"local":[10704.00,15051.64,3667.74]},
    {"mesh":"PWM_Quarry_8x8x8_A-ProcMaterial_Quarry_Atlas-Custom-dcl-L100","bubble":"The_Great_Forge_of_Narvi","world":[22925.70,117303.47,6433.92],"local":[7075.70,18603.47,4733.92]},
    {"mesh":"PWM_Quarry_5x4x10-ProcMaterial_Quarry_Atlas_A-BlockAll-dcl-L100","bubble":"The_Great_Forge_of_Narvi","world":[22834.99,117120.09,6189.51],"local":[6984.99,18420.09,4489.51]},
    {"mesh":"PWM_Quarry_8x8x8_A-ProcMaterial_Quarry_Atlas-Custom-dcl-L100","bubble":"The_Great_Forge_of_Narvi","world":[23059.19,117327.95,7213.81],"local":[7209.19,18627.95,5513.81]},
    {"mesh":"PWM_Quarry_2x2x2_A-ProcMaterial_Quarry_Atlas-BlockAll-dcl-L100","bubble":"The_Great_Forge_of_Narvi","world":[22645.00,117220.00,7235.00],"local":[6795.00,18520.00,5535.00]},
    {"mesh":"PWM_Quarry_4x5x10-ProcMaterial_Quarry_Atlas_A-BlockAll-dcl-L100","bubble":"The_Great_Forge_of_Narvi","world":[22803.67,117354.17,7693.13],"local":[6953.67,18654.17,5993.13]},
    {"mesh":"PWM_Quarry_8x8x8_A-ProcMaterial_Quarry_Atlas-Custom-dcl-L100","bubble":"The_Great_Forge_of_Narvi","world":[22550.00,117250.00,7250.00],"local":[6700.00,18550.00,5550.00]},
    {"mesh":"PWM_Quarry_8x8x8_A-ProcMaterial_Quarry_Atlas-Custom-dcl-L100","bubble":"The_Great_Forge_of_Narvi","world":[22807.79,117290.48,8043.62],"local":[6957.79,18590.48,6343.62]},
    {"mesh":"PWM_Quarry_4x3x10_A-ProcMaterial_Quarry_Atlas_A-BlockAll-dcl-L100","bubble":"The_Great_Forge_of_Narvi","world":[23906.81,114130.04,5217.74],"local":[8056.81,15430.04,3517.74]},
    {"mesh":"PWM_Quarry_5x4x10-ProcMaterial_Quarry_Atlas_A-BlockAll-dcl-L100","bubble":"The_Great_Forge_of_Narvi","world":[23150.00,114300.00,5485.00],"local":[7300.00,15600.00,3785.00]},
    {"mesh":"PWM_Quarry_4x3x10_A-ProcMaterial_Quarry_Atlas_A-BlockAll-dcl-L100","bubble":"The_Great_Forge_of_Narvi","world":[24653.25,114381.30,5271.80],"local":[8803.25,15681.30,3571.80]},
    {"mesh":"PWM_Quarry_1x1x1_A-ProcMaterial_Quarry_Atlas-BlockAll-dcl-L100","bubble":"The_Great_Forge_of_Narvi","world":[26699.20,114012.78,5385.95],"local":[10849.20,15312.78,3685.95]},
    {"mesh":"PWM_Quarry_4x3x10_A-ProcMaterial_Quarry_Atlas_A-BlockAll-dcl-L100","bubble":"The_Great_Forge_of_Narvi","world":[24588.34,111604.63,4906.02],"local":[8738.34,12904.63,3206.02]},
    {"mesh":"PWM_Quarry_4x3x10_A-ProcMaterial_Quarry_Atlas_A-BlockAll-dcl-L100","bubble":"The_Great_Forge_of_Narvi","world":[24600.00,111450.00,4800.00],"local":[8750.00,12750.00,3100.00]},
    {"mesh":"Defiled_Statues_A_Damaged_E-MI_Defiled_Statues_A-MI_Defiled_Statues_B_Damaged-BlockAll-dcl-L100","bubble":"The_Great_Forge_of_Narvi","world":[20410.00,107661.22,4366.88],"local":[4560.00,8961.22,2666.88]},
    {"mesh":"Defiled_Statues_A_Damaged_C-MI_Defiled_Statues_A-MI_Defiled_Statues_B_Damaged-BlockAll-dcl-L100","bubble":"The_Great_Forge_of_Narvi","world":[19035.36,109485.36,6150.00],"local":[3185.36,10785.36,4450.00]},
    {"mesh":"Defiled_Statues_A_Damaged_B-MI_Defiled_Statues_A-MI_Defiled_Statues_B_Damaged-BlockAll-dcl-L100","bubble":"The_Great_Forge_of_Narvi","world":[19035.36,109485.36,6150.00],"local":[3185.36,10785.36,4450.00]},
    {"mesh":"PWM_Quarry_1X1x1_C-ProcMaterial_Quarry_Atlas-BlockAll-dcl-L100","bubble":"The_Great_Forge_of_Narvi","world":[18000.00,116250.00,6500.00],"local":[2150.00,17550.00,4800.00]},
    {"mesh":"PWM_Quarry_1X1x1_C-ProcMaterial_Quarry_Atlas-BlockAll-dcl-L100","bubble":"The_Great_Forge_of_Narvi","world":[20574.93,115955.91,6345.67],"local":[4724.93,17255.91,4645.67]},
    {"mesh":"PWM_Quarry_1x1x1_A-ProcMaterial_Quarry_Atlas-BlockAll-dcl-L100","bubble":"The_Great_Forge_of_Narvi","world":[20575.00,115870.00,6325.00],"local":[4725.00,17170.00,4625.00]},
    {"mesh":"PWM_Quarry_1x1x1_A-ProcMaterial_Quarry_Atlas-BlockAll-dcl-L100","bubble":"The_Great_Forge_of_Narvi","world":[20606.72,116087.12,6355.00],"local":[4756.72,17387.12,4655.00]},
    {"mesh":"PWM_Quarry_2x2x2_A-ProcMaterial_Quarry_Atlas-BlockAll-dcl-L100","bubble":"The_Great_Forge_of_Narvi","world":[20609.37,116342.27,6400.00],"local":[4759.37,17642.27,4700.00]},
    {"mesh":"PWM_Quarry_1x1x1_A-ProcMaterial_Quarry_Atlas-BlockAll-dcl-L100","bubble":"The_Great_Forge_of_Narvi","world":[20850.00,116385.00,6335.00],"local":[5000.00,17685.00,4635.00]},
    {"mesh":"PWM_Quarry_2x2x2_A-ProcMaterial_Quarry_Atlas-BlockAll-dcl-L100","bubble":"The_Great_Forge_of_Narvi","world":[18151.11,113068.89,6360.00],"local":[2301.11,14368.89,4660.00]},
    {"mesh":"PWM_Quarry_1X1x1_C-ProcMaterial_Quarry_Atlas-BlockAll-dcl-L100","bubble":"The_Great_Forge_of_Narvi","world":[18242.50,113162.99,6340.00],"local":[2392.50,14462.99,4640.00]},
    {"mesh":"PWM_Quarry_1x1x1_A-ProcMaterial_Quarry_Atlas-BlockAll-dcl-L100","bubble":"The_Great_Forge_of_Narvi","world":[18330.75,113667.99,6340.00],"local":[2480.75,14967.99,4640.00]},
    {"mesh":"PWM_Quarry_1x1x1_A-ProcMaterial_Quarry_Atlas-BlockAll-dcl-L100","bubble":"The_Great_Forge_of_Narvi","world":[17403.61,104915.43,6135.00],"local":[1553.61,6215.43,4435.00]},
    {"mesh":"PWM_Quarry_1X1x1_C-ProcMaterial_Quarry_Atlas-BlockAll-dcl-L100","bubble":"The_Great_Forge_of_Narvi","world":[17325.00,104900.00,6105.00],"local":[1475.00,6200.00,4405.00]},
    {"mesh":"PWM_Quarry_2x2x2_A-ProcMaterial_Quarry_Atlas-BlockAll-dcl-L100","bubble":"The_Great_Forge_of_Narvi","world":[17450.00,104665.00,6105.00],"local":[1600.00,5965.00,4405.00]},
    {"mesh":"PWM_Quarry_1x1x1_A-ProcMaterial_Quarry_Atlas-BlockAll-dcl-L100","bubble":"The_Great_Forge_of_Narvi","world":[18000.00,104225.00,6130.00],"local":[2150.00,5525.00,4430.00]},
    {"mesh":"PWM_Quarry_1X1x1_C-ProcMaterial_Quarry_Atlas-BlockAll-dcl-L100","bubble":"The_Great_Forge_of_Narvi","world":[18154.77,104136.05,6145.00],"local":[2304.77,5436.05,4445.00]},
    {"mesh":"PWM_Quarry_2x2x2_A-ProcMaterial_Quarry_Atlas-BlockAll-dcl-L100","bubble":"The_Great_Forge_of_Narvi","world":[17980.00,103970.00,6175.00],"local":[2130.00,5270.00,4475.00]},
    {"mesh":"PWM_Quarry_2x2x2_A-ProcMaterial_Quarry_Atlas-BlockAll-dcl-L100","bubble":"The_Great_Forge_of_Narvi","world":[17804.65,104610.55,6099.00],"local":[1954.65,5910.55,4399.00]},
    {"mesh":"PWM_Quarry_1x1x1_A-ProcMaterial_Quarry_Atlas-BlockAll-dcl-L100","bubble":"The_Great_Forge_of_Narvi","world":[17963.00,104491.00,6073.00],"local":[2113.00,5791.00,4373.00]},
    {"mesh":"PWM_Quarry_1x1x1_A-ProcMaterial_Quarry_Atlas-BlockAll-dcl-L100","bubble":"The_Great_Forge_of_Narvi","world":[18061.11,103772.37,6135.00],"local":[2211.11,5072.37,4435.00]},
    {"mesh":"PWM_Quarry_1x1x1_A-ProcMaterial_Quarry_Atlas-BlockAll-dcl-L100","bubble":"The_Great_Forge_of_Narvi","world":[18865.00,102735.00,6135.00],"local":[3015.00,4035.00,4435.00]},
    {"mesh":"PWM_Quarry_1X1x1_C-ProcMaterial_Quarry_Atlas-BlockAll-dcl-L100","bubble":"The_Great_Forge_of_Narvi","world":[18615.61,102814.39,6150.00],"local":[2765.61,4114.39,4450.00]},
    {"mesh":"PWM_Quarry_2x2x2_A-ProcMaterial_Quarry_Atlas-BlockAll-dcl-L100","bubble":"The_Great_Forge_of_Narvi","world":[18575.00,102605.00,6145.00],"local":[2725.00,3905.00,4445.00]},
    {"mesh":"PWM_Quarry_2x2x2_A-ProcMaterial_Quarry_Atlas-BlockAll-dcl-L100","bubble":"The_Great_Forge_of_Narvi","world":[18770.00,102530.00,6145.00],"local":[2920.00,3830.00,4445.00]},
    {"mesh":"PWM_Quarry_2x2x2_A-ProcMaterial_Quarry_Atlas-BlockAll-dcl-L100","bubble":"The_Great_Forge_of_Narvi","world":[18965.00,102455.00,6135.00],"local":[3115.00,3755.00,4435.00]},
    {"mesh":"PWM_Quarry_1x1x1_A-ProcMaterial_Quarry_Atlas-BlockAll-dcl-L100","bubble":"The_Great_Forge_of_Narvi","world":[18680.00,102515.00,6280.00],"local":[2830.00,3815.00,4580.00]},
    {"mesh":"PWM_Quarry_4x4x4_A-ProcMaterial_Quarry_Atlas-BlockAll-dcl-L100","bubble":"The_Great_Forge_of_Narvi","world":[18625.00,102640.00,6295.00],"local":[2775.00,3940.00,4595.00]},
    {"mesh":"PWM_Quarry_2x2x5_B-ProcMaterial_Quarry_Atlas-BlockAll-dcl-L100","bubble":"The_Great_Forge_of_Narvi","world":[18360.00,102525.00,6405.00],"local":[2510.00,3825.00,4705.00]},
    {"mesh":"PWM_Quarry_1x1x1_A-ProcMaterial_Quarry_Atlas-BlockAll-dcl-L100","bubble":"The_Great_Forge_of_Narvi","world":[18611.21,102456.84,6350.00],"local":[2761.21,3756.84,4650.00]},
    {"mesh":"PWM_Quarry_1X1x1_C-ProcMaterial_Quarry_Atlas-BlockAll-dcl-L100","bubble":"The_Great_Forge_of_Narvi","world":[20240.00,103055.00,6115.00],"local":[4390.00,4355.00,4415.00]},
    {"mesh":"PWM_Quarry_1x1x1_A-ProcMaterial_Quarry_Atlas-BlockAll-dcl-L100","bubble":"The_Great_Forge_of_Narvi","world":[20303.39,102885.07,6120.00],"local":[4453.39,4185.07,4420.00]},
    {"mesh":"PWM_Quarry_1x1x1_A-ProcMaterial_Quarry_Atlas-BlockAll-dcl-L100","bubble":"The_Great_Forge_of_Narvi","world":[20367.50,103003.45,6135.00],"local":[4517.50,4303.45,4435.00]},
    {"mesh":"PWM_Quarry_1x1x1_A-ProcMaterial_Quarry_Atlas-BlockAll-dcl-L100","bubble":"The_Great_Forge_of_Narvi","world":[20685.85,102848.53,6140.00],"local":[4835.85,4148.53,4440.00]},
    {"mesh":"PWM_Quarry_1X1x1_C-ProcMaterial_Quarry_Atlas-BlockAll-dcl-L100","bubble":"The_Great_Forge_of_Narvi","world":[20821.55,102801.88,6125.00],"local":[4971.55,4101.88,4425.00]},
    {"mesh":"PWM_Quarry_1X1x1_C-ProcMaterial_Quarry_Atlas-BlockAll-dcl-L100","bubble":"The_Great_Forge_of_Narvi","world":[21905.00,103255.00,5735.00],"local":[6055.00,4555.00,4035.00]},
    {"mesh":"PWM_Quarry_2x2x2_A-ProcMaterial_Quarry_Atlas-BlockAll-dcl-L100","bubble":"The_Great_Forge_of_Narvi","world":[21900.00,103413.11,5718.42],"local":[6050.00,4713.11,4018.42]},
    {"mesh":"PWM_Quarry_2x2x2_A-ProcMaterial_Quarry_Atlas-BlockAll-dcl-L100","bubble":"The_Great_Forge_of_Narvi","world":[30225.21,110363.19,5507.00],"local":[14375.21,11663.19,3807.00]},
    {"mesh":"PWM_Quarry_1x1x1_A-ProcMaterial_Quarry_Atlas-BlockAll-dcl-L100","bubble":"The_Great_Forge_of_Narvi","world":[30060.00,110350.00,5492.00],"local":[14210.00,11650.00,3792.00]},
    {"mesh":"PWM_Quarry_2x2x2_A-ProcMaterial_Quarry_Atlas-BlockAll-dcl-L100","bubble":"The_Great_Forge_of_Narvi","world":[30215.00,105645.00,5280.00],"local":[14365.00,6945.00,3580.00]},
]

# --- The_Doors_of_Durin ---
durin_entries = [
    {"mesh":"PWM_Quarry_2x2x2_A-ProcMaterial_Quarry_Atlas-BlockAll-dcl-L100","bubble":"The_Doors_of_Durin","world":[6320.00,69000.00,5650.00],"local":[3270.00,2300.00,3950.00]},
]

print("=== Adding position entries ===")
add_to_bubble('Western_Mines.json', western_entries)
add_to_bubble('The_Great_Forge_of_Narvi.json', narvi_entries)
add_to_bubble('The_Doors_of_Durin.json', durin_entries)
print("\nDone!")
