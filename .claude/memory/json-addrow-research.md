---
name: JSON AddRow Research (ABANDONED for build menu)
description: Runtime JSON-based DataTable row injection works but FGK wrapper cache prevents build menu visibility for constructions/recipes
type: project
---

## JSON AddRow Test Results (2026-03-14)

**Goal**: Read UAssetAPI-format JSON files and inject rows into DT_Constructions / DT_ConstructionRecipes at runtime.

**What WORKS**:
- JSON file reading from `Mods/MoriaCppMod/json/` directory
- Row injection via existing `applyAddRow()` pipeline — rows added successfully (854→855, 814→815)
- `findRowData()` confirms rows exist after injection
- `DoesDataTableRowExist` (hash-based) confirms YES
- TextPropertyData handled via `UKismetTextLibrary::TextFromStringTable` ProcessEvent — LOCTABLE references created correctly
- All field types written: FText, SoftObjectPath, GameplayTagContainer, enums, nested structs, arrays

**What DOESN'T WORK — Build menu visibility**:
The FGK wrapper layer (MorConstructionsTable, MorConstructionRecipesTable) caches DataTable rows internally at initialization. Adding rows to the raw UDataTable after FGK initialization means the wrapper never sees them.

**Approaches tried (all failed)**:
1. `PostLoad()` on FGK wrapper → returned OK but DynamicTable remained NULL, no cache refresh
2. `AMorDiscoveryManager::DiscoverRecipe(FName)` → returned OK but recipe not in FGK cache so discovery system can't match it
3. `UFGKRecipeRepository::LearnRecipe(FName)` → 0 instances found in game world
4. `GetDiscoveredConstructionRecipesCount` → returns 775 (of 815), confirms discovery system is separate from DataTable

**Why it fails — Root cause**:
- FGK wrappers (UFGKDataTableBase subclasses) have NO public refresh/rebuild/invalidate methods
- Internal TMap caches at offset 0x110 (ConstructionRecipeLookup, ActorRowNameLookup) populated once at load
- `HandleDataTableChanged()` is ENGINE_API (not UFUNCTION, not virtual) — can't call via ProcessEvent or vtable
- No delegate listeners on the FGK wrappers to notify of DataTable changes

**Remaining theoretical options** (not attempted):
- Direct memory write into FGK wrapper TMap at offset 0x110 (risky, struct layout unknown)
- Signature scan for HandleDataTableChanged address
- Hook earlier in load sequence before FGK wrapper initialization

**How to apply**: JSON AddRow is validated for non-FGK DataTables (items, weapons, ores, etc. where the game reads directly from the DataTable). For construction/recipe build menu visibility, the pak/IoStore approach would be needed. The `add_row` directive in .def files works for DataTable modifications but new constructions won't appear in the build menu.

## JSON files used for testing
- `Mods/MoriaCppMod/json/NotchedArchway.json` — MorConstructionDefinition row
- `Mods/MoriaCppMod/json/NotchedArchwayRecipe.json` — MorConstructionRecipeDefinition row
- Row name: `MereakPack_NotchedArchway_A`
