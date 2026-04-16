---
name: moria-datatable
description: DataTable CRUD utility — bind/read/write/add rows, vtable dispatch, cached instances
type: project
---

# moria_datatable.inl — DataTable CRUD Utility

**File**: `<workspace>/cpp-mod/MyCPPMods/MoriaCppMod/src/moria_datatable.inl`
**Included**: Inside the main mod class body, after `moria_common.inl`.

## Overview
Runtime-only DataTable read/write/add utility. Changes reset on game restart. All operations use raw memory access with `isReadableMemory()` guards.

## DataTableUtil Struct

### Lifecycle
- `bind(L"DT_Constructions")` — FindAllOf("DataTable") + name match, resolves RowStruct + rowSize
- `unbind()` — clear all cached state
- `isBound()` — check if table is bound

### Row Enumeration
- `getRowCount()` — number of rows via RowMap header
- `getRowNames()` — all FName row names as `vector<wstring>`
- `findRowData(L"RowName")` — raw `uint8_t*` to row data by FName match

### Property Resolution
- `resolvePropertyOffset(L"PropName")` — ForEachProperty + cache (sentinels: -2=unresolved, -1=not found)

### Typed Reads
- `readInt32` — int32 read
- `readFText` — FText → wstring via ToString() (ref-counted, read-only safe)
- `readObjectPtr` — UObject* pointer read

### Typed Writes (in-place)
- `writeInt32` — int32 write
- `writeFloat` — float write
- **FText writes**: NOT supported (ref-counted internal structure)

### Add Row (via Engine VTable Dispatch)
- `addRow(L"NewRow")` — FMemory::Malloc + zero-fill + InitializeStruct + `callAddRowInternal()` via vtable
  - Uses engine's `AddRowInternal` at vtable offset 0x278 (UE 4.27)
  - Properly maintains TMap hash buckets (confirmed: engine source is just `RowMap.Add(name, data)`)
  - No manual TMap/TSet manipulation needed
- `callAddRowInternal(rowName, rowData)` — vtable dispatch helper using `std::bit_cast<MFP>(rawFunc)` pattern
- **IMPORTANT**: Adding rows to the raw UDataTable does NOT update FGK wrapper caches (see build-menu-injection.md)

### Diagnostics
- `dumpRowNames()` — VLOG all row names
- `dumpRowStructFields()` — VLOG all property names, offsets, sizes

## Cached Instances (class members)
6 pre-defined DataTableUtil instances:
- `m_dtConstructions`, `m_dtConstructionRecipes`
- `m_dtItems`, `m_dtWeapons`, `m_dtTools`, `m_dtArmor`

## Cross-Table Lookups (class methods, not DataTableUtil methods)
- `resolveConstructionRowName(L"RecipeRow")` — reads ResultConstructionHandle.RowName (+0x08) from DT_ConstructionRecipes → returns DT_Constructions row name
- `lookupRecipeIcon(L"RecipeRow")` — cross-ref recipe → construction → `readObjectPtr(L"Icon")` → UTexture2D*

## Technical Notes
- RowMap at offset 0x30 (`DT_ROWMAP_OFFSET`): TSet with 24-byte element stride (FName 8B + ptr 8B + hash 8B)
- UE4SS TMap devlog warns about mutation — add uses raw memory instead
- AddRowInternal is ENGINE_API virtual (not UFUNCTION) — cannot use ProcessEvent
- FText is reference-counted — reads OK, writes unsafe
- TArray layout: `{ T* Data; int32 Num; int32 Max; }` = 16 bytes
