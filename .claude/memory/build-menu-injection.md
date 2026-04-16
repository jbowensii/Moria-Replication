---
name: Build Menu Injection (ABANDONED)
description: Adding new constructions to the build menu is blocked by FGK wrapper cache layer — both IoStore and JSON AddRow approaches hit dead ends
type: project
---

## Build Menu Injection — Two Approaches, Both Blocked

### Approach 1: IoStore pak mounting (ABANDONED earlier)
- IoStore containers (.pak/.ucas/.utoc) cannot be mounted from UE4SS at runtime
- Would require engine-level IoStore dispatcher access

### Approach 2: JSON AddRow + FGK cache refresh (ABANDONED 2026-03-14)
- DataTable row injection works perfectly (rows verified in DT_Constructions and DT_ConstructionRecipes)
- FGK wrapper layer (MorConstructionsTable, MorConstructionRecipesTable) caches rows at load time
- No public API exists to refresh FGK wrapper caches
- Tried: PostLoad(), DiscoverRecipe(), LearnRecipe() — all failed
- See [json-addrow-research.md](json-addrow-research.md) for full details

**Why:** FGK framework has no cache invalidation mechanism. Wrappers are UFGKDataTableBase subclasses with internal TMap/TArray caches at fixed byte offsets, populated once during initialization.

**How to apply:** Do not attempt build menu injection for new constructions. The definition system (.def files) can modify EXISTING construction/recipe rows (change properties, enable/disable) but cannot add NEW ones that appear in the build menu. JSON AddRow is useful for non-FGK DataTables only.
