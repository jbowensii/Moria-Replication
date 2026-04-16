# Item DataTable Row Struct Schemas

Reference for all 7 item DataTable row structs used by MoriaCppMod. All access via `DataTableUtil` (runtime reflection, no hardcoded offsets).

## Inheritance Hierarchy

```
FTableRowBase (UE4 engine)
  └─ FFGKTableRowBase (+EnabledState: ERowEnabledState)
       └─ FMorItemDefinition (base for all 7 item tables)
            ├─ FMorWeaponDefinition       → m_dtWeapons ("DT_Weapons")
            ├─ FMorToolDefinition         → m_dtTools ("DT_Tools")
            ├─ FMorArmorDefinition        → m_dtArmor ("DT_Armor")
            ├─ FMorConsumableDefinition   → m_dtConsumables ("DT_Consumables")
            ├─ FMorOreDefinition          → m_dtOres ("DT_Ores")
            └─ FMorContainerItemDefinition → m_dtContainerItems ("DT_ContainerItems")
       (FMorItemDefinition itself)        → m_dtItems ("DT_Items")
```

## Table Binding (moria_datatable.inl lines 574-597)

| Member | Table Name | Row Struct |
|--------|-----------|------------|
| m_dtItems | DT_Items | FMorItemDefinition |
| m_dtWeapons | DT_Weapons | FMorWeaponDefinition |
| m_dtTools | DT_Tools | FMorToolDefinition |
| m_dtArmor | DT_Armor | FMorArmorDefinition |
| m_dtConsumables | DT_Consumables | FMorConsumableDefinition |
| m_dtOres | DT_Ores | FMorOreDefinition |
| m_dtContainerItems | DT_ContainerItems | FMorContainerItemDefinition |

## FMorItemDefinition (base — 20 properties)

All 7 specialized structs inherit these properties.

| Property | Type | DataTableUtil Method |
|----------|------|---------------------|
| DisplayName | FText | readFText |
| Description | FText | readFText |
| Icon | TSoftObjectPtr\<UTexture2D\> | readObjectPtr |
| Actor | TSoftClassPtr\<AMorItemBase\> | readObjectPtr |
| DroppedItemMeshOverride | UStaticMesh* | readObjectPtr |
| Tags | FGameplayTagContainer | readRaw |
| SkillsRequired | FGameplayTagContainer | readRaw |
| SkillsGranted | FGameplayTagContainer | readRaw |
| VisibleEffects | TArray\<TSubclassOf\<UGameplayEffect\>\> | readTArrayRaw |
| VisibleEffectTagMagnitudes | TMap\<FGameplayTag, float\> | readRaw |
| EquipEffects | TArray\<TSubclassOf\<UGameplayEffect\>\> | readTArrayRaw |
| EquipEffectTagMagnitudes | TMap\<FGameplayTag, float\> | readRaw |
| HolsterEffects | TArray\<TSubclassOf\<UGameplayEffect\>\> | readTArrayRaw |
| HolsterEffectTagMagnitudes | TMap\<FGameplayTag, float\> | readRaw |
| CosmeticConvertCost | FMorCosmeticConvertRowHandle | readFName (inner RowName) |
| ItemSetRowHandle | FMorItemSetRowHandle | readFName (inner RowName) |
| Portability | EItemPortability (uint8) | readUInt8 |
| MaxStackSize | int32 | readInt32 |
| SlotSize | int32 | readInt32 |
| BaseTradeValue | float | readFloat |

## FMorWeaponDefinition (+13 properties)

| Property | Type | Method |
|----------|------|--------|
| DamageType | FGameplayTag | readRaw |
| Durability | int32 | readInt32 |
| Tier | uint8 | readUInt8 |
| Damage | int32 | readInt32 |
| Speed | float | readFloat |
| ArmorPenetration | float | readFloat |
| StaminaCost | float | readFloat |
| EnergyCost | float | readFloat |
| BlockDamageReduction | float | readFloat |
| UseEffects | TArray\<TSubclassOf\<UGameplayEffect\>\> | readTArrayRaw |
| UseEffectTagMagnitudes | TMap\<FGameplayTag, float\> | readRaw |
| InitialRepairCost | TArray\<FMorRequiredRecipeMaterial\> | readTArrayRaw |
| RepairCostCurve | UCurveFloat* | readObjectPtr |

## FMorToolDefinition (+11 properties)

| Property | Type | Method |
|----------|------|--------|
| Durability | int32 | readInt32 |
| DurabilityDecayWhileEquipped | float | readFloat |
| StaminaCost | float | readFloat |
| EnergyCost | float | readFloat |
| CompatibleToolTags | FGameplayTagContainer | readRaw |
| UseEffects | TArray\<TSubclassOf\<UGameplayEffect\>\> | readTArrayRaw |
| UseEffectTagMagnitudes | TMap\<FGameplayTag, float\> | readRaw |
| InitialRepairCost | TArray\<FMorRequiredRecipeMaterial\> | readTArrayRaw |
| RepairCostCurve | UCurveFloat* | readObjectPtr |
| CarveHits | int32 | readInt32 |
| NpcMiningRate | float | readFloat |

## FMorArmorDefinition (+7 properties)

| Property | Type | Method |
|----------|------|--------|
| Durability | int32 | readInt32 |
| DamageReduction | float | readFloat |
| DamageProtection | float | readFloat |
| DamageModifiers | TArray\<FMorDamageModifierRowHandle\> | readTArrayRaw |
| InitialRepairCost | TArray\<FMorRequiredRecipeMaterial\> | readTArrayRaw |
| RepairCostCurve | UCurveFloat* | readObjectPtr |
| CosmeticOwner | FMorArmorRowHandle | readFName |
| CosmeticAchievement | FMorAchievementRowHandle | readFName |

## FMorConsumableDefinition (+9 properties)

| Property | Type | Method |
|----------|------|--------|
| SpoilageSeconds | int32 | readInt32 |
| HungerRestore | int32 | readInt32 |
| HealthRestore | int32 | readInt32 |
| EnergyRestore | int32 | readInt32 |
| UseEffects | TArray\<TSubclassOf\<UGameplayEffect\>\> | readTArrayRaw |
| MealTime | EMealTime (uint8) | readUInt8 |
| MealTimeUseEffects | TArray\<TSubclassOf\<UGameplayEffect\>\> | readTArrayRaw |
| UseEffectTagMagnitudes | TMap\<FGameplayTag, float\> | readRaw |
| ItemHotbarBehavior | EMorItemHotbarBehavior (uint8) | readUInt8 |

## FMorOreDefinition (+1 property)

| Property | Type | Method |
|----------|------|--------|
| Mineral | TSoftObjectPtr\<UMoriaMineralPropertyAsset\> | readObjectPtr |

## FMorContainerItemDefinition (+1 property)

| Property | Type | Method |
|----------|------|--------|
| StorageRowHandle | FMorStorageRowHandle | readFName |

## Enums

| Enum | Values |
|------|--------|
| ERowEnabledState | Live, Test, Disabled |
| EItemPortability | Storable, HeavyCarry, AutoConsume |
| EMorItemHotbarBehavior | None, Equip, Use |
| EMealTime | None, Breakfast, Lunch, Dinner |

## Row Handle Types

All extend `FFGKDataTableRowHandle` → stores single `FName RowName`.

Moria variants: FMorAnyItemRowHandle, FMorItemRowHandle, FMorItemSetRowHandle, FMorContainerItemRowHandle, FMorCosmeticConvertRowHandle, FMorStorageRowHandle, FMorArmorRowHandle, FMorAchievementRowHandle, FMorDamageModifierRowHandle.

## DataTableUtil Capabilities (moria_datatable.inl)

- **Scalar read/write**: readInt32, readFloat, readBool, readUInt8, readFName, readFText, readObjectPtr + write variants (writeInt32, writeFloat, writeBool, writeUInt8, writeFName)
- **Array**: readTArrayRaw, readTArrayCount, writeTArrayRaw, clearTArray
- **Row management**: addRow (copies from template row), duplicateRow, removeRow
- **Lookup**: findRowData, getRowNames, getRowCount, resolvePropertyOffset
- **Cross-table**: construction recipe helpers

## Header Source Paths

| Struct | Path (relative to workspace dumps/) |
|--------|------|
| FMorItemDefinition | UHTHeaderDump/Moria/Public/MorItemDefinition.h |
| FMorWeaponDefinition | UHTHeaderDump/Moria/Public/MorWeaponDefinition.h |
| FMorToolDefinition | UHTHeaderDump/Moria/Public/MorToolDefinition.h |
| FMorArmorDefinition | UHTHeaderDump/Moria/Public/MorArmorDefinition.h |
| FMorConsumableDefinition | UHTHeaderDump/Moria/Public/MorConsumableDefinition.h |
| FMorOreDefinition | UHTHeaderDump/Moria/Public/MorOreDefinition.h |
| FMorContainerItemDefinition | UHTHeaderDump/Moria/Public/MorContainerItemDefinition.h |
| FFGKTableRowBase | UHTHeaderDump/FGKStaticData/Public/FGKTableRowBase.h |
