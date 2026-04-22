#!/usr/bin/env python3
"""
Build an empty CPF_BearNest.umap that replaces the bear nest prefab.
Strips all bear-specific actors, keeps only the minimal level skeleton.
"""

import json
from pathlib import Path

src = Path(__file__).parent / 'CPF_BearNest.json'
dst = Path(__file__).parent / 'CPF_BearNest_empty.json'

with open(src, 'r', encoding='utf-8') as f:
    data = json.load(f)

# Current exports (0-indexed in the array, 1-indexed in references):
#  0: Ak (AkComponent)              - bear component
#  1: BP_BearNest_Spawner_10        - bear actor
#  2: BP_BearNestCenter_11          - bear actor
#  3: PersistentLevel               - KEEP
#  4: Model_0                       - KEEP
#  5: SpawnerComponent              - bear component
#  6: MorNavigationSystemConfig_0   - KEEP (WorldSettings child)
#  7: MorViewTrigger                - bear component
#  8: ParticleSystem                - bear component
#  9: SceneComponent                - bear component
# 10: BearNest_Deco_PH_Collision    - bear actor
# 11: StaticMeshComponent0          - bear component
# 12: CPF_BearNest (World)          - KEEP
# 13: WorldSettings                 - KEEP

# Strategy: keep exports 3,4,6,12,13 (PersistentLevel, Model, NavConfig, World, WorldSettings)
# Remove exports 0,1,2,5,7,8,9,10,11 (all bear stuff)

keep_indices = {3, 4, 6, 12, 13}  # 0-based
old_exports = data['Exports']

# Build old-to-new export index mapping (1-based references)
new_idx = 0
old_to_new = {}  # old 1-based -> new 1-based
for i in range(len(old_exports)):
    if i in keep_indices:
        new_idx += 1
        old_to_new[i + 1] = new_idx

print(f"Keeping {len(keep_indices)} of {len(old_exports)} exports")
print(f"Index mapping (1-based): {old_to_new}")

def remap_export_ref(ref):
    """Remap an export reference. Export refs are positive 1-based.
    Import refs are negative. 0 = null."""
    if ref > 0:
        return old_to_new.get(ref, 0)  # 0 = null if removed
    return ref  # imports and null unchanged

# Filter exports
new_exports = []
for i in range(len(old_exports)):
    if i in keep_indices:
        exp = old_exports[i]
        # Remap OuterIndex
        if exp.get('OuterIndex', 0) > 0:
            exp['OuterIndex'] = remap_export_ref(exp['OuterIndex'])
        # Remap dependency arrays
        for dep_key in ['SerializationBeforeSerializationDependencies',
                        'CreateBeforeSerializationDependencies',
                        'SerializationBeforeCreateDependencies',
                        'CreateBeforeCreateDependencies']:
            if dep_key in exp:
                exp[dep_key] = [remap_export_ref(r) if r > 0 else r
                                for r in exp[dep_key]
                                if r <= 0 or r in old_to_new]  # keep imports, remap or drop exports

        # Remap data references
        for prop in exp.get('Data', []):
            if prop.get('$type', '').endswith('ObjectPropertyData, UAssetAPI'):
                val = prop.get('Value', 0)
                if val > 0:
                    prop['Value'] = remap_export_ref(val)
            # Handle arrays of object properties
            if prop.get('$type', '').endswith('ArrayPropertyData, UAssetAPI'):
                for item in prop.get('Value', []):
                    if item.get('$type', '').endswith('ObjectPropertyData, UAssetAPI'):
                        val = item.get('Value', 0)
                        if val > 0:
                            item['Value'] = remap_export_ref(val)

        # Special handling for LevelExport — empty the Actors list
        if exp.get('$type', '') == 'UAssetAPI.ExportTypes.LevelExport, UAssetAPI':
            # Keep only WorldSettings actor
            ws_new = old_to_new.get(14, 0)  # export 14 (1-based) = WorldSettings
            exp['Actors'] = [ws_new]
            # Remap Model reference
            if 'Model' in exp:
                exp['Model'] = remap_export_ref(exp['Model'])

        new_exports.append(exp)

data['Exports'] = new_exports

# Clean up NameMap — remove bear-specific names (optional, not strictly needed)
# Keep all names to be safe — UAssetGUI handles this

# Clean up imports — remove bear-specific ones
# Keep all imports to be safe — orphan imports don't cause crashes

# Update DependsMap to match new export count
data['DependsMap'] = [[] for _ in range(len(new_exports))]

# Update Generations
if data.get('Generations'):
    data['Generations'][0]['ExportCount'] = len(new_exports)

print(f"New export count: {len(new_exports)}")
for i, exp in enumerate(new_exports):
    print(f"  {i+1}: {exp.get('ObjectName', '?')}")

with open(dst, 'w', encoding='utf-8') as f:
    json.dump(data, f, indent=2)

print(f"\nWrote: {dst}")
