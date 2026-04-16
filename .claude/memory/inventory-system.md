# Inventory System - Return to Moria

## Key Classes (from CXXHeaderDump/FGK.hpp and Moria.hpp)

### FItemHandle (FGK.hpp:1715) — 0x14 = 20 bytes
The runtime handle for referencing items in inventory. NOT FNames!
```cpp
struct FItemHandle {
    int32 ID;                                    // @0x00 — matches FItemInstance.ID
    int32 Payload;                               // @0x04
    TWeakObjectPtr<UInventoryComponent> Owner;   // @0x08 (8B)
}; // Size: 0x14 (20 bytes)
```

### FItemInstance (FGK.hpp:1723) — 0x30 = 48 bytes
The actual item data stored in inventory arrays.
```cpp
struct FItemInstance : public FFastArraySerializerItem {
    // FFastArraySerializerItem base: 0x10 bytes (ReplicationID, Key, etc.)
    TSubclassOf<AInventoryItem> Item;  // @0x10 (UClass*, 8B) — THE ITEM TYPE
    int32 Count;                       // @0x18
    int32 Slot;                        // @0x1C
    int32 ID;                          // @0x20 — matches FItemHandle.ID
    float Durability;                  // @0x24
    int32 RepairCount;                 // @0x28
    int32 ContainerStartSlot;          // @0x2C
}; // Size: 0x30
```

### FItemInstanceArray (FGK.hpp:1735) — 0x120 bytes
Container for item instances.
```cpp
struct FItemInstanceArray : public FFastArraySerializer {
    UInventoryComponent* Inventory;     // @0x0108
    TArray<FItemInstance> List;          // @0x0110 (16B = Data*+Num+Max)
}; // Size: 0x120
```

## UInventoryComponent (FGK.hpp:7308) — base class
```
@0x00B8: TArray<FItemInstance> ClientItems  — CLIENT-SIDE item list (readable!)
@0x0208: TArray<int32> Hotbar               — hotbar slot indices (may be empty!)
@0x0220: FItemInstanceArray Items            — server-replicated items (0x120 bytes)
  Items.List at component+0x0330          — TArray<FItemInstance>
@0x0340: FActiveItemEffectArray Effects
@0x0470: UInventoryLoadout* OverrideStartingLoadout
@0x0478: UEquipComponent* Equip
```
Key functions:
- `GetItemForSlot(int32 Slot)` → FItemHandle
- `GetAllItems(TArray<FItemHandle>& OutItems)` — out param (16B)
- `GetItemListForUI()` → TArray<UObject*>
- `GetItemCount(TSubclassOf<AInventoryItem>, EInventoryQuery)` → int32
- `GetItemCountById(const FName& ID, EInventoryQuery)` → int32

## UMorInventoryComponent (Moria.hpp:17994) — game subclass extends UInventoryComponent
```
@0x04B8: FMorStorageRowHandle StorageHandle
@0x0530: int32 HotbarSize                   — returns 8
@0x0534: int32 HotbarEpicItemIndex           — returns 9
```
Key functions:
- `GetItemForHotbarSlot(int32 HotbarIndex)` → FItemHandle (24B params: Index@0, ReturnValue@4)
- `GetHotbarSize()` → int32 (4B)
- `GetHotbarEpicItemIndex()` → int32 (4B)
- `ProcessHotbarAction(int32 HotbarIndex)` — trigger hotbar action
- `GetItemHotbarBehavior(int32 HotbarIndex)` → EMorItemHotbarBehavior
- `UseFromItemHandle(const FItemHandle& Item)` — use an item
- `GetContainers()` → TArray<FItemHandle>

## UItemHandleFunctions (FGK.hpp:7427) — BlueprintFunctionLibrary
Static utility functions for FItemHandle (call on CDO):
- `ToString(FItemHandle)` → FString
- `ToDebugString(FItemHandle)` → FString
- `GetClass(FItemHandle)` → TSubclassOf<AInventoryItem> (UClass*)
- `GetClassDefault(FItemHandle)` → AInventoryItem* (CDO)
- `GetCount(FItemHandle)` → int32
- `GetDurability(FItemHandle)` → float
- `GetSlot(FItemHandle)` → int32
- `IsValidItem(FItemHandle)` → bool
- `IsContainer(FItemHandle)` → bool
- `GetContents(FItemHandle, TArray<FItemHandle>&)` — out param
- `GetStorageName(FItemHandle)` → FText

## AInventoryItem (FGK.hpp:2851) — base item actor
```
@0x0230: TSubclassOf<AInventoryItem> DecomposesInto
@0x0238: TSubclassOf<AInventoryItem> RestoresBackTo
@0x0240: TArray<UItemEffect*> StartingItemEffects
@0x0258: TArray<TSubclassOf<UGameplayEffect>> VisibleEffects
```
Key functions:
- `GetDisplayName()` → FText
- `GetIcon()` → UTexture2D*
- `GetMaxDurability()` → float

## AFGKDropItemManager (FGK.hpp:2471)
- `GetNameForItemHandle(const FItemHandle& Item)` → FName — item's FName row identifier

## Hotbar Layout
- 8 normal slots: keys 1-8 (HotbarIndex 0-7)
- 1 epic slot: key 0 (HotbarIndex 9, HotbarEpicItemIndex)
- Key 9: skipped
- Associated with DT_Storage.uasset → Dwarf.BodyInventory (8x1 grid)

## Probe Approach (WORKING — confirmed 2026-02-21)
1. Find MorInventoryComponent via findPlayerInventoryComponent()
2. Read **Items.List** TArray at component+**0x0330** (NOT ClientItems@0xB8 — empty when host/server)
   - Items.List = UInventoryComponent+0x0220 (FItemInstanceArray) + 0x0110 (List offset within it)
3. For each FItemInstance (0x30 bytes each), read UClass* at entry+0x10, call GetName()
4. Build ID→name map (FItemInstance.ID @0x20 matches FItemHandle.ID @0x00)
5. Call GetItemForHotbarSlot for each slot → FItemHandle (20 bytes, ReturnValue@4)
6. Extract FItemHandle.ID (bytes 4-7 of ProcessEvent buffer), look up in map

**ClientItems @0xB8 is EMPTY when host/server** — only populated for client confirmation.
Server-side Items.List @0x0330 is the authoritative source.

## Action Bar Widgets
- `UI_WBP_Inventory_ActionBar_Item_C` (0x300 bytes)
  - @0x02A0: nestedInventoryItem (UI_WBP_Inventory_Item_AB_C*)
  - @0x02C8: isEpicItem (bool)
  - @0x02D0: nestedEpicItem (UI_WBP_Inventory_Item_ABEpic_C*)
  - @0x02E8: slotID (int32)
  - @0x02F8: CurrentAction (FName, 8B)
  - Named instances: _1 through _8, _EPIC, _MainHand, _Offhand, _HeavyCarry

## Modifying Inventory Items via ProcessEvent (CORRECT APPROACH)

**DO NOT write directly to FItemInstance memory** — it bypasses replication, UI updates, and events.

### Architecture: 3-Layer Item System
1. **AInventoryItem (AActor)** — Item CLASS definition (Blueprint template like `BP_Granite_C`). NOT stored in inventory — only the class reference is stored.
2. **FItemInstance (USTRUCT, 0x30)** — Inventory slot record. Stores `Item` (UClass*), `Count`, `Durability`, `ID`, `Slot`. Lives in `FItemInstanceArray::List` TArray. NOT a UObject — cannot use FindObject().
3. **FItemHandle** — Lightweight reference `{ID, Payload, Owner}` to find an FItemInstance by ID.

### Proper APIs (ProcessEvent on UInventoryComponent)

**Adding items:**
```cpp
// RequestAddItem — Server, Reliable RPC. Adds items through proper channels.
auto* fn = invComp->GetFunctionByNameInChain(STR("RequestAddItem"));
int sz = fn->GetParmsSize();
std::vector<uint8_t> p(sz, 0);
auto* pClass  = findParam(fn, STR("Class"));
auto* pCount  = findParam(fn, STR("Count"));
auto* pMethod = findParam(fn, STR("Method"));
if (pClass)  *reinterpret_cast<UClass**>(p.data() + pClass->GetOffset_Internal()) = itemClass;
if (pCount)  *reinterpret_cast<int32_t*>(p.data() + pCount->GetOffset_Internal()) = count;
if (pMethod) *reinterpret_cast<uint8_t*>(p.data() + pMethod->GetOffset_Internal()) = 0; // EAddItem::Normal
invComp->ProcessEvent(fn, p.data());
```

**Getting current count:**
```cpp
auto* fn = invComp->GetFunctionByNameInChain(STR("GetItemCount"));
int sz = fn->GetParmsSize();
std::vector<uint8_t> p(sz, 0);
auto* pItem = findParam(fn, STR("Item"));
auto* pFrom = findParam(fn, STR("From"));
auto* pRet  = findParam(fn, STR("ReturnValue"));
if (pItem) *reinterpret_cast<UClass**>(p.data() + pItem->GetOffset_Internal()) = itemClass;
if (pFrom) *reinterpret_cast<uint8_t*>(p.data() + pFrom->GetOffset_Internal()) = 0;
invComp->ProcessEvent(fn, p.data());
int32_t count = pRet ? *reinterpret_cast<int32_t*>(p.data() + pRet->GetOffset_Internal()) : 0;
```

**Setting count (debug):**
```cpp
// ServerDebugSetItem — sets TOTAL count for an item type across inventory
auto* fn = invComp->GetFunctionByNameInChain(STR("ServerDebugSetItem"));
// Params: TSubclassOf<AInventoryItem> Item, int32 Count
```

### EAddItem Enum (uint8)
| Value | Name | Purpose |
|-------|------|---------|
| 0 | Normal | Standard add with stacking |
| 1 | Create | Force create new slot |
| 2 | Silent | No UI notification |
| 4 | Equip | Add and equip |
| 8 | ReplaceContainer | Replace container contents |

### All Inventory Modification UFUNCTIONs (Server, Reliable RPCs)
| Function | Params | Notes |
|----------|--------|-------|
| `RequestAddItem` | `(Class, Count, Method)` | Add items |
| `ServerRemoveItem` | `(Item, Count, From)` | Remove by class |
| `ServerDebugSetItem` | `(Item, Count)` | Set total count |
| `ServerDropItem` | `(Item, Count, Direction)` | Drop from inventory |
| `ServerSplitStack` | `(Source, Destination, MoveCount)` | Split stack |
| `ServerMoveItem` | `(Item, Destination, AddType)` | Move between slots |
| `ServerChangeDurability` | `(Item, RatioChange)` | Change durability |
| `ServerDebugDamageItems` | `(Percentage)` | Damage all items |
| `ServerDebugBreakItems` | `()` | Break all items |

### Replenish Item Flow (moria_inventory.inl)
1. **Capture**: `ServerMoveItem`/`MoveSwapItem`/`BroadcastToContainers_OnChanged` ProcessEvent hooks capture FItemHandle.ID → scan Items.List → store UClass*
2. **CDO → RowName**: `m_lastPickedUpItemClass->GetClassDefaultObject()` → resolve `RowHandle` property → extract FName RowName
3. **DataTable MaxStackSize**: Lazy-bind 7 item DataTables → `findRowData(rowName)` → `readInt32("MaxStackSize")`
4. **GetItemCount**: ProcessEvent to get current total
5. **RequestAddItem**: ProcessEvent with deficit (maxStack - currentCount)

### DataTable Lazy Binding (CRITICAL)
Item DataTables must be explicitly bound before use. They are NOT auto-bound on mod load.
```cpp
if (!m_dtItems.isBound()) m_dtItems.bind(L"DT_Items");
// ... same for m_dtWeapons, m_dtTools, m_dtArmor, m_dtConsumables, m_dtOres, m_dtContainerItems
```
`bindAllDataTables()` exists but is never called from dllmain.cpp. Construction tables are lazily bound by quickbuild/hism code.

### ProcessEvent Gotchas for Inventory
- **Client, Reliable RPCs** (e.g. `ClientAddItemFX`) bypass ProcessEvent on listen servers
- **BlueprintCallable non-RPCs** (e.g. `AddItem`) are called directly by game code, NOT through ProcessEvent
- **Server, Reliable RPCs** (e.g. `ServerMoveItem`, `RequestAddItem`) DO go through ProcessEvent on listen servers
- Only 3 functions confirmed firing via ProcessEvent on MorInventoryComponent: `BroadcastToContainers_OnChanged`, `OnItemEquipped`, `ServerMoveItem`

## Handle-Specific Item Removal (Trash Item Pattern)
There is **NO reflected RemoveItem that takes FItemHandle**. `RemoveItem`/`ServerRemoveItem` only take `TSubclassOf<AInventoryItem>` (class+count) — they remove from any stack, not a specific instance.

**To remove a specific item by handle**: use `DropItem(FItemHandle, int32 Count)` which targets the exact handle, then destroy the spawned `MorDroppedItem` actor:
```cpp
// 1. Get item count via UItemHandleFunctions::GetCount(handle)
auto* ihfClass = StaticFindObject<UClass*>(nullptr, nullptr, STR("/Script/FGK.ItemHandleFunctions"));
auto* getCountFn = ihfClass->GetFunctionByNameInChain(STR("GetCount"));
// Call on CDO with FItemHandle param → returns int32

// 2. Snapshot existing drop actors
std::vector<UObject*> preDropActors;
FindAllOf(STR("MorDroppedItem"), preDropActors);
std::unordered_set<UObject*> preDropSet(preDropActors.begin(), preDropActors.end());

// 3. DropItem(handle, count) on inventory component
auto* dropFn = invComp->GetFunctionByNameInChain(STR("DropItem"));
// Params: Item (FItemHandle, 20 bytes), Count (int32)

// 4. Find and destroy the new MorDroppedItem actor
std::vector<UObject*> postDropActors;
FindAllOf(STR("MorDroppedItem"), postDropActors);
for (auto* actor : postDropActors) {
    if (preDropSet.count(actor)) continue;
    auto* destroyFn = actor->GetFunctionByNameInChain(STR("K2_DestroyActor"));
    safeProcessEvent(actor, destroyFn, nullptr);
}
```

**Key class**: `AMorDroppedItem` (NOT `FGKDropItem`) — spawned by `DropItem`/`ServerDropItem`. Extends `AMorPickup`, has `Inventory` (UMorInventoryComponent*), `DroppedItem` (FItemCount).

## Per-Instance Item Effects (Effects.List)
- **FActiveItemEffectArray**: at `UInventoryComponent+0x0340`, List TArray at +0x0110 within it
- **FActiveItemEffect**: stride 0x30, OnItem (int32) at +0x0C, Effect (UItemEffect*) at +0x10
- Tints stored as `MorItemTintEffect`, runes as `MorRuneEffect`
- Matched by `OnItem == FItemHandle.ID`
- Clear tint: `ServerTintItem(handle, nullptr, pawn)` on CraftingComponent — works
- Clear rune: `ServerInscribeRune(handle, nullptr, pawn)` does NOT work (validation rejects null)
- Rune removal: direct swap-remove from Effects.List TArray (see `removeItemEffectFromList()`)

## Display Names
- `AInventoryItem::GetDisplayName()` → FText (human-readable, e.g. "Iron Pickaxe")
- Call on CDO: `itemClass->GetClassDefaultObject()` → `GetFunctionByNameInChain("GetDisplayName")`
- `AInventoryItem::GetIcon()` → UTexture2D* (item icon texture)
- Class name (e.g. "EQ_Pick_Iron_C") is NOT the display name

## LESSONS LEARNED
- FItemHandle is {ID, Payload, TWeakObjectPtr} — NOT two FNames. The FName constructor doesn't just set raw values.
- FItemInstance is a USTRUCT, NOT a UObject — cannot use FindObject() on it.
- AInventoryItem is the class definition, NOT an instance in inventory. Inventory only stores UClass* references.
- Always use ProcessEvent with proper UFUNCTIONs instead of raw memory writes for inventory modification.
- DataTables must be lazily bound before first use — they are not auto-bound.
- **RemoveItem/ServerRemoveItem are CLASS-based, not handle-based** — they remove from any matching stack. Use DropItem+DestroyActor for handle-specific removal.
- **Dropped item actor class is `MorDroppedItem`** (NOT `FGKDropItem` — that class doesn't exist)
- **ServerInscribeRune(nullptr) fails silently** — validation rejects null Rune param. Must manipulate Effects.List directly.
- **UItemHandleFunctions::GetCount(handle) returns 1 for stacks** — unreliable during/after moves. Read `FItemInstance.Count` at offset 0x18 directly from Items.List at capture time instead.
