# Phase 2: Fix Compilation Errors — Replication Guide

**Purpose:** After running UE4GameProjectGenerator against Return to Moria's UHT header dumps, the generated UE4.27 project has hundreds of errors. This document records every fix applied to achieve clean compilation.

**Starting point:** Raw output from UE4GameProjectGenerator commandlet  
**End state:** `MoriaEditor Win64 Development` builds with 0 errors  
**Engine:** UE4.27 (`C:\Program Files\Epic Games\UE_4.27\`)

---

## Step 1: Remove Engine Plugin Modules from Source/

The generator creates Source/ directories for ALL 77 modules in the UHT dump, but 35+ of these are engine plugins that already exist in UE4.27. Having them as game Source modules causes conflicts.

**Keep only these 9 game modules:**
- `Moria`, `FGK`, `FGKAnalytics`, `FGKDebugMenu`, `FGKLoadingScreen`
- `FGKNavPowerPlaceholder`, `FGKStaticData`, `FGKUE5Stubs`, `FGKUIToolkit`

**The remaining Source/ directories are NOT compiled** (not listed in .uproject Modules), but are kept as reference material. The critical change is updating `.uproject` and `*Target.cs` to only reference the 9 game modules.

### Engine modules that were removed from compilation (partial list):
ACLPlugin, AkAudio, ApexDestruction, CommonInput, CommonUI, ControlRig, DLSS, DLSSBlueprint, DebugPlotter, DragonIKPlugin, EasySkyV2, EnhancedInput, FSR2TemporalUpscaling, FlyingNavSystem, Foliage, FullBodyIK, GenericGraphRuntime, GeometryCache, Gridly, LevelSequence, MediaAssets, MediaUtils, MovieRenderPipeline, NavigationSystem, Niagara, NiagaraCore, OnlineSubsystemUtils, PhysicsCore, PowerIKRuntime, PrefabAsset, RopeCutting, SignificanceManager, Voxel, VoxelExamples, VoxelFoliage, VoxelGraph, VoxelHelpers, VoxelNiagara, Water, WebBrowserWidget

---

## Step 2: Fix .uproject

Update `Moria.uproject`:
- Set `"EngineAssociation": "4.27"`
- List only 9 game modules (see Step 1)
- List only plugins that exist in UE4.27:
  ```
  GameplayAbilities, CommonUI, EnhancedInput, Niagara, ApexDestruction,
  OnlineSubsystemEOS, OnlineSubsystemSteam, OnlineSubsystemUtils,
  OnlineFramework, Water, ControlRig, FullBodyIK, GeometryCache,
  MovieRenderPipeline, DataRegistry, SignificanceManager
  ```
- Remove: CommonInput (part of CommonUI in UE4.27), Voxel, NavigationSystem, LevelSequence (these don't exist as standalone plugins)

---

## Step 3: Fix Target.cs Files

Rename generated files:
- `Moria-input.Target.cs` -> `MoriaGame.Target.cs` (class: `MoriaGameTarget`, Type: Game)
- `Moria-inputEditor.Target.cs` -> `MoriaEditor.Target.cs` (class: `MoriaEditorTarget`, Type: Editor)

Fix invalid C# class names (hyphens not allowed). Set `ExtraModuleNames` to only the 9 game modules.

---

## Step 4: Fix Build.cs Dependencies

### Moria.Build.cs
Add these dependencies beyond what was generated:
```
"GameplayTasks"   — IGameplayTaskOwnerInterface linker errors
"AudioMixer"      — USynthComponent virtual function linker errors (UMediaSoundComponent chain)
```

**Note:** Do NOT use "Synthesis" for USynthComponent — USynthComponent is in AudioMixer, not Synthesis.

### FGK.Build.cs
Add:
```
"GameplayTasks"   — IGameplayTaskOwnerInterface linker errors
```

---

## Step 5: GAS Header Redirects (Gameplay Ability System)

Moria's custom engine fork split GAS headers into standalone files that don't exist in stock UE4.27. Create redirect headers in `Source/Moria/Public/` and `Source/FGK/Public/`:

| Missing Header | Redirect To |
|---|---|
| `GameplayAbilityTargetDataHandle.h` | `Abilities/GameplayAbilityTargetTypes.h` |
| `ActiveGameplayEffectHandle.h` | `GameplayEffectTypes.h` |
| `GameplayAbilitySpecHandle.h` | `Abilities/GameplayAbilityTypes.h` |
| `GameplayAbility.h` | `Abilities/GameplayAbility.h` |
| `GameplayAttribute.h` | `AttributeSet.h` |
| `GameplayAbilityTargetActor.h` | `Abilities/GameplayAbilityTargetActor.h` |
| `GameplayAbilityWorldReticle.h` | `Abilities/GameplayAbilityWorldReticle.h` |
| `GameplayCueParameters.h` | `GameplayCueInterface.h` |
| `GameplayEventData.h` | `Abilities/GameplayAbilityTypes.h` |
| `GameplayTargetDataFilter.h` | `Abilities/GameplayAbilityTargetDataFilter.h` |
| `AbilityTask.h` | `Abilities/Tasks/AbilityTask.h` |
| `GameplayAbilityTargetData.h` | `Abilities/GameplayAbilityTargetTypes.h` |
| `GameplayAttributeData.h` | `AttributeSet.h` |
| `GameplayAbilityTargetActor_SingleLineTrace.h` | `Abilities/GameplayAbilityTargetActor_SingleLineTrace.h` |
| `GameplayAbilityTargetActor_Trace.h` | `Abilities/GameplayAbilityTargetActor_Trace.h` |
| `EGameplayEffectDurationType.h` | `GameplayEffect.h` |

### Other Engine Header Redirects

| Missing Header | Redirect To |
|---|---|
| `ENCPoolMethod.h` | `NiagaraCommon.h` |
| `ECommonInputType.h` | `CommonInputBaseTypes.h` |
| `InputModifier.h` | `InputModifiers.h` |
| `InputTrigger.h` | `InputTriggers.h` |
| `CommonUIActionRouterBase.h` | `Input/CommonUIActionRouterBase.h` |

Each redirect header follows this pattern:
```cpp
#pragma once
#include "ActualEngineHeader.h"
```

---

## Step 6: Stub Classes for Missing Types

These types exist in Moria's custom engine but not in stock UE4.27. Create stub UCLASSes/USTRUCTs:

### ACullVolume (Source/Moria/Public/CullVolume.h + Private/CullVolume.cpp)
```cpp
// .h
#pragma once
#include "CoreMinimal.h"
#include "GameFramework/Volume.h"
#include "CullVolume.generated.h"

UCLASS(Blueprintable)
class MORIA_API ACullVolume : public AVolume {
    GENERATED_BODY()
public:
    ACullVolume(const FObjectInitializer& ObjectInitializer);
};

// .cpp
#include "CullVolume.h"
ACullVolume::ACullVolume(const FObjectInitializer& ObjectInitializer) : Super(ObjectInitializer) {}
```

### ANavMeshLockVolume (same pattern, parent: AVolume)
Referenced by WorldLayoutBubble.h.

### FPrefabLevelStreamData (Source/Moria/Public/PrefabLevelStreamData.h)
```cpp
USTRUCT(BlueprintType)
struct MORIA_API FPrefabLevelStreamData {
    GENERATED_BODY()
};
```

---

## Step 7: TEnumAsByte Mismatches

The generated code uses `TEnumAsByte<EnumType>` wrappers in UFUNCTION parameters, but UE4.27 expects the raw enum. Fix these:

| File | Change |
|---|---|
| `FGKBaseCharacter.h/.cpp` | `TEnumAsByte<ERelativeTransformSpace>` -> `ERelativeTransformSpace` (GetSocketTransform params) |
| `AgenticTrainingConfig.h/.cpp` | `TEnumAsByte<EpisodeState>` -> `EpisodeState` |

---

## Step 8: Abstract Class Fixes

### MorCharacter.h — GetAbilitySystemComponent()
MorCharacter inherits IAbilitySystemInterface but doesn't implement its pure virtual. Add:
```cpp
// .h — inside class declaration
virtual UAbilitySystemComponent* GetAbilitySystemComponent() const override;

// .cpp
#include "MoriaAbilitySystemComponent.h"
UAbilitySystemComponent* AMorCharacter::GetAbilitySystemComponent() const { return MoriaAbSystem; }
```

### MorFarmingReceptacle.h — same interface
```cpp
virtual UAbilitySystemComponent* GetAbilitySystemComponent() const override { return nullptr; }
```

### MovieScene Track Classes (4 files)
MovieSceneAkAudioEventTrack, MovieSceneAkAudioRTPCTrack, FGKMovieSceneLabelTrack, FGKMovieSceneStateTrack — all need `CreateTemplateForSection` override:
```cpp
virtual FMovieSceneEvalTemplatePtr CreateTemplateForSection(const UMovieSceneSection& InSection) const override;
// .cpp: return FMovieSceneEvalTemplatePtr();
```

---

## Step 9: Constructor Fixes (Linker Errors)

Several parent classes don't export their default constructor. Change to FObjectInitializer pattern:

| Class | Parent | Issue |
|---|---|---|
| `MorControlRig_FeetIK` | `UControlRig` | Default ctor not exported |
| `MorEnvQueryTest_BreakableDistance` | `UEnvQueryTest_Distance` | Entire class not exported (no AIMODULE_API) — **reparent to `UEnvQueryTest`** |
| `FGKLevelSequencePlayerFSM` | `ULevelSequencePlayer` | Requires FObjectInitializer |
| `MorBlockedPlayersListView` | `UListViewBase` | Requires FObjectInitializer |

Pattern:
```cpp
// .h
ClassName(const FObjectInitializer& ObjectInitializer);

// .cpp
ClassName::ClassName(const FObjectInitializer& ObjectInitializer) : Super(ObjectInitializer) {}
```

---

## Step 10: Reparenting for Unexported Classes

| Class | Original Parent | New Parent | Reason |
|---|---|---|---|
| `UVoxelProceduralMeshComponent` | `UModelComponent` | `UPrimitiveComponent` | UModelComponent virtuals not exported |
| `UMorEnvQueryTest_BreakableDistance` | `UEnvQueryTest_Distance` | `UEnvQueryTest` | UEnvQueryTest_Distance has no AIMODULE_API |

---

## Step 11: UHT Metadata Fixes

### Reserved parameter names
Rename `Self` to `InSelf` in delegate declarations:
- `OnCanBeDamagedChangedDelegate.h`
- `OnTeleportFinishedDelegate.h`
- `MorHeavyCarryWrapperItem.h`

### Enums missing zero value
Add `None = 0` to:
- `EMorBubblePriority`
- `EWaterColliderPlayMode`

### Missing delegate declarations
Add `DECLARE_DYNAMIC_MULTICAST_DELEGATE` stubs for:
- `FBlueprintOnUse` (FGKSimplePickupComponent.h)
- `FConfigureVoxelWorld` (VoxelPhysicsPartSpawner_VoxelWorlds.h)
- `FOnSpawnedPassageActor` (BubbleInterface.h)

### BlueprintReadWrite on incompatible types
Remove `BlueprintReadWrite` from:
- `FAIMoveRequest` properties (3 files)
- `FInputBlendPose` in MorAnimNode_LipSync.h
- `TSet<TWeakObjectPtr>` in MorSpawnPrefabInCellAsyncOperation.h

### Malformed sparse delegate
Fix `MorFXLocalPlayerProximityDelegateDelegate.h` — malformed sparse delegate macro.

### Include ordering
In `WorldLayoutBubble.h`: move `#include` before `.generated.h`.

---

## Step 12: Interface Removal

Remove `ICustomAnimInstanceEvaluationDispatcher` interface from `FGKCharacterAnimInstance.h` — doesn't exist in UE4.27.

---

## Step 13: Copy Prevention

Add `TStructOpsTypeTraits` with `WithCopy = false` to `FMorBubbleStateHandler` — contains `FBroadphaseRegionTickFunction` member which has a deleted copy operator.

---

## Step 14: Delegate Signature Fix

In `MorProfanityFilter.cpp`: change `FMorProfanityFilterReturnValue()` to `UMorProfanityFilter::FOnTextUpdatedDynamic()`.

---

## Build Command

```batch
"C:\Program Files\Epic Games\UE_4.27\Engine\Binaries\DotNET\UnrealBuildTool.exe" ^
  MoriaEditor Win64 Development ^
  -Project="C:\Users\johnb\OneDrive\Documents\Projects\Moria-Replication\project\Moria.uproject"
```

**Expected result:** 94/94 actions, 0 errors, only APEX deprecation warnings (cosmetic).
