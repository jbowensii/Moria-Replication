# Future Research — Mod Enhancement Experiments and New Capabilities

**Version:** 6.3.9  
**Date:** April 2026  
**Author:** Mereak Firmaxe  
**Last Updated:** April 16, 2026  

**Note:** FGK cache bypass research, pak mounting, IoStore tooling, and the full editor project reconstruction pipeline have been moved to the companion document: **Moria Replication Plan - Editor Project Reconstruction.md**

---

## New Capabilities via UE4SS C++ Mod (No Pak Required)

### H. Gameplay Ability System (GAS) Manipulation

**Status:** HIGHLY FEASIBLE — all via ProcessEvent on existing classes.

The player's `UAbilitySystemComponent` is accessible via property reflection on `BP_FGKDwarf_C`. Key UFUNCTIONs:
- `BP_ApplyGameplayEffectToSelf(geClass, level, context)`
- `MakeOutgoingSpec(geClass, level, context)` — create modifiable spec
- `MakeEffectContext()` — create context handle
- `RemoveActiveGameplayEffect(handle, stacksToRemove)`
- `HasMatchingGameplayTag(tag)` / `GetOwnedGameplayTags(outContainer)`

Hundreds of existing GameplayEffect classes: `GE_DEV_RingOfPower`, `GE_BootsOfDebugSpeed`, `GE_Warm`, `GE_Full`, etc.

**Use cases:** Apply buffs/debuffs, temperature immunity, speed boosts, damage resistance, stat modifications — all through existing game assets without creating new ones.

---

### I. Texture and Material Replacement

**Status:** FEASIBLE — multiple approaches.

**Runtime (via ProcessEvent):**
- `CreateDynamicMaterialInstance(ElementIndex, SourceMaterial, Name)` on `UPrimitiveComponent`
- `SetTextureParameterValue` / `SetVectorParameterValue` / `SetScalarParameterValue` on the MID
- Limited to parameter changes on existing materials

**Offline (via tools):**
- UE4-DDS-Tools: inject textures directly into .uasset files (supports UE4.27, any-size textures, DDS/PNG/TGA/BMP)
- Package modified assets into a priority pak for auto-mount

---

### J. Audio Injection

**Status:** FEASIBLE — limited to existing game sounds.

UFUNCTIONs on `UGameplayStatics`:
- `PlaySound2D(WorldContextObject, USoundBase*, Volume, Pitch, StartTime, ...)`
- `PlaySoundAtLocation(WorldContextObject, USoundBase*, Location, Rotation, ...)`
- `SpawnSoundAtLocation(...)` — returns `UAudioComponent*` for ongoing control

Hundreds of existing game `USoundCue` objects discoverable via `FindAllOf("SoundCue")`.

Cannot load custom WAV/OGG from disk without pak mounting.

---

### K. Blueprint Function Hooking (Offline Asset Modification)

**Status:** EXPERIMENTAL — proven tools exist.

| Tool | Purpose | URL |
|------|---------|-----|
| spaghetti | Hook cooked Blueprint functions by modifying function map in .uasset | https://github.com/bananaturtlesandwich/spaghetti |
| KismetKompiler | Compile/decompile Blueprint bytecode (supports UE4.27) | https://github.com/tge-was-taken/KismetKompiler |

**Combined approach:** Decompile FGK's build-menu initialization Blueprint, add registration calls for new items, recompile, repack into a priority pak.

---

### L. CDO and Template Modification

**Status:** PROVEN in other UE4 games (Dmgvol guides).

Modify `Default__<ClassName>` (Class Default Objects) to change all future instances of a class. Modify `_GEN_VARIABLE` component templates to affect newly spawned actors.

`GameInstance.ReferencedObjects` trick (UE4): add modified CDOs to this array to prevent GC from reclaiming them across level loads.

**Reference:** https://github.com/Dmgvol/UE_Modding

---

### M. UE.Toolkit (XML-Based Runtime Object Editing)

**Status:** PROVEN for UE4.27.2 (Reloaded II framework).

https://github.com/RyoTune/UE.Toolkit — supports:
- Edit any UObject/UDataTable at runtime via XML text files
- Add new properties to class type information
- Register entirely new struct types into UE's reflection system
- Extend object sizes with custom constructors
- Built-in mod merging

Could potentially register new struct types that FGK recognizes.

---

### N. Universal Signature Bypasser

**Status:** PROVEN — drop-in DLL.

https://github.com/rm-NoobInCoding/UniversalSigBypasser — universal .sig file bypass for UE games. Useful if our pak files would otherwise fail signature verification.

---

## Enhancement Ideas — Things Other UE4 Game Mods Do

### 1. GAS Buff/Debuff System
Apply existing GameplayEffects to the player via ProcessEvent on UAbilitySystemComponent. The game ships hundreds of effects: `GE_DEV_RingOfPower`, `GE_BootsOfDebugSpeed`, `GE_Warm`, `GE_Full`, `GE_ColdDebuff`, `GE_Freezing`, `GE_Shadowed`, `GE_AntiDarknessBrewSip`. Could build an F12 "Potions" tab for speed boosts, temperature immunity, damage resistance, stamina regen. All via ProcessEvent — no pak work needed.

### 2. Custom Building Piece Appearances
Swap textures/colors on placed buildings using `CreateDynamicMaterialInstance` + `SetVectorParameterValue` via ProcessEvent. Imagine painting walls different colors or making torches glow different hues. Works at runtime, no paks.

### 3. Sound Feedback
Play existing game sounds when mod actions fire (placement confirmation, removal swoosh, toolbar switch click). Hundreds of `USoundCue` objects already in the game, discoverable via `FindAllOf("SoundCue")`. Pure ProcessEvent on `UGameplayStatics`, trivial to add.

### 4. CDO Modification for Game Balance
Instead of DataTable XML defs, directly modify Class Default Objects to change ALL future instances of a class. For example, change default durability of all iron picks by modifying `Default__BP_IronPick_C`. Persists across level loads with the `GameInstance.ReferencedObjects` trick (add the modified CDO to this array to prevent GC from reclaiming it).

### 5. New Constructions via Pak
Set up a UE4.27 project, create custom building pieces (new wall types, decorative elements, functional structures), cook, convert with retoc, and deploy alongside the C++ mod. The auto-mount system handles everything. This is proven by existing Moria mods (Secrets of Khazad-dum, TobiModsAddons).

### 6. Blueprint Behavior Injection
See deep dive below.

### 7. 3D Model Replacement via 3dmigoto
See deep dive below.

### 8. Weather/Environment Control
See deep dive below.

---

## Deep Dive — Blueprint Behavior Injection

### spaghetti (Blueprint Function Hooker)

**What it does:** Intercepts and redirects calls in compiled (cooked) Blueprint functions. Takes two inputs: your hook-containing Blueprint and the original Blueprint. Redirects the function map to your hook and registers the original under a different name. The hook can still call the original (now renamed) for fallback behavior.

**Workflow:**
```
spaghetti <hook_blueprint.uasset> <original_blueprint.uasset> -v 4.27 -o <output.uasset>
```

**UE4.27 compatibility:** Yes, supports `-v 4.27`.

**Critical limitations:**
- Single asset per pak — only ONE modded asset per pak file
- No hook-on-hook — two mods cannot both modify the same Blueprint
- Primarily function REPLACEMENT, not function ADDITION
- If two mods want the same Blueprint, they must be manually merged

**URL:** https://github.com/bananaturtlesandwich/spaghetti

### KismetKompiler (Blueprint Bytecode Compiler)

**What it does:** Decompiles cooked UE4 Blueprint bytecode into readable `.kms` scripts (C#-like syntax), lets you edit them, and recompiles back into `.uasset` files.

**Key commands:**
```
# Decompile
KismetKompiler decompile -v 4.27 -i Blueprint.uasset -o Blueprint.kms

# Recompile into existing .uasset
KismetKompiler compile -v 4.27 -i Blueprint.kms -o Blueprint_modified.uasset --asset Blueprint.uasset
```

**Capabilities:** Function calls, variable access/assignment, control flow (if/else, loops), local and member variables, Blueprint library function imports.

**Limitations:**
- Primarily tested on UE4.23 (Shin Megami Tensei V) — UE4.27 compatibility uncertain but plausible
- Cannot create Blueprint classes from scratch
- Cannot modify existing variable/function definitions (only add new ones)
- Unsupported constructs appear as `EX_...` intrinsics that cannot be modified

**URL:** https://github.com/tge-was-taken/KismetKompiler

### Combined Workflow for Return to Moria

```
Step 1: Extract game Blueprint .uasset
  retoc --extract -f=/Moria/Content/UI/BuildHUD -o=extracted/

Step 2: Decompile
  KismetKompiler decompile -v 4.27 -i extracted/UI_WBP_BuildHUDv2.uasset -o BuildHUD.kms

Step 3: Edit the .kms script
  Add function calls to register new build menu categories, populate recipe lists, etc.

Step 4: Recompile
  KismetKompiler compile -v 4.27 -i BuildHUD.kms -o BuildHUD_modified.uasset --asset extracted/UI_WBP_BuildHUDv2.uasset

Step 5: Pack into priority pak
  Place in folder structure matching game content path, pack with UnrealPak or retoc
  Name MUST end with _P (e.g., MoriaRecipeMod_P.pak)

Step 6: Deploy
  Place in Moria/Content/Paks/
```

### High-Value Blueprints to Target

| Blueprint | Risk Level | Use Case |
|-----------|-----------|----------|
| UI_WBP_BuildHUDv2 | LOW (UI-only) | Add new category filters, inject custom recipe selection logic |
| BP_DebugMenu_Recipes | LOW | Expose recipe discovery hooks |
| Recipe/Crafting BPs | HIGH (MP desync) | Modify recipe availability — server+client must match |
| FGK init BPs | HIGH | Hook FGK system initialization |

### Risks

- **UE4.27 bytecode compatibility:** KismetKompiler was tested on 4.23. Opcodes may differ for 4.27. Test on a non-critical Blueprint first.
- **Multiplayer desync:** UI-only mods are safe (clients can differ). Recipe/gameplay logic mods require identical files on server AND all clients.
- **Single-asset-per-pak:** Each modified Blueprint is a separate pak file. No mod combinations within one pak.

### Real-World Examples
- Hogwarts Legacy: Blueprint Apparate Modloader + UE4SS for dozens of feature mods
- S.T.A.L.K.E.R. 2: UE4SS loads Blueprint mods from content/mods/ subfolders
- Shin Megami Tensei V: KismetKompiler used extensively for decompile/modify/recompile workflow

---

## Deep Dive — 3dmigoto Mesh and Texture Replacement

### What Is 3dmigoto?

An open-source **DirectX 11 interception framework** that operates at the renderer level. It intercepts D3D11 draw calls via a proxy `d3d11.dll` placed in the game directory, enabling runtime modification of shaders, textures, and meshes without touching game source code or assets.

**Identification:** Hash-based — each draw call, vertex buffer, index buffer, and texture gets a unique hash. Files follow the pattern: `DrawID-BufferType-Hash-ShaderInfo.Extension`.

**URL:** https://github.com/bo3b/3Dmigoto (WARNING: 3dmigoto.com is a phishing site — use only GitHub)

### UE4.27 Compatibility

**Fully compatible.** UE4.27 uses DirectX 11 and 3dmigoto's interception is engine-agnostic. Proven on multiple UE4 games (Genshin Impact, Honkai Star Rail, and others).

**GPU Skinning:** UE4 uses GPU skinning by default for skeletal meshes. 3dmigoto CAN replace these — the replacement must maintain the same bone count, structure, and vertex-to-bone weight mapping.

**UE4 Deferred Rendering:** Objects appear in multiple render passes (G-buffer, lighting, final). You may see the same mesh drawn multiple times with different hashes. Solution: hunt each relevant pass and replace all instances.

### Mesh Replacement Workflow

**Phase 1 — Identify Target:**
1. Place `d3d11.dll` (3dmigoto) in game directory
2. Launch game, press Numpad 0 for hunting mode (green text overlay)
3. Numpad 1/2 cycles through vertex buffers — target object disappears when correct buffer selected
4. Copy Index Buffer hash and shader hashes
5. F8 creates a frame analysis dump (exports all buffers, textures, shaders)

**Phase 2 — Extract and Edit:**
1. Install 3dmigoto Blender plugin (`blender_3dmigoto_gimi.py`)
2. Import dumped `.vb`/`.ib` files into Blender
3. Edit geometry — MUST preserve vertex groups (bone assignments), vertex colors, and stay within vertex limits
4. Export as 3dmigoto vertex buffer

**Phase 3 — Configure Replacement:**
```ini
[TextureOverride]
Hash = <original_texture_hash>
CheckTextureOverride = true

[ResourceReplaceBuffer]
Hash = <original_vb_hash>
Path = Mods\MyMod\replacement.vb
Stride = <vertex_stride_bytes>
```

**Phase 4 — Deploy:**
Place `d3d11.dll` + `d3dx.ini` + `Mods/` folder in game directory. F10 in-game reloads config.

### Texture-Only Replacement (Simpler)

1. Hunt texture in hunting mode (Numpad 3/4 cycles pixel shaders)
2. F8 dumps textures as DDS files
3. Create replacement DDS with **identical dimensions, compression format, and mip levels**
4. Configure in `d3dx.ini` and place in Mods folder

### Performance

| Mod Type | FPS Impact |
|----------|-----------|
| Texture-only | 0–2% |
| Simple model swap | 0–5% |
| Complex shader overrides | 5–15% |
| Heavy geometry edits | 10–20% |

### Coexistence with UE4SS

Both use proxy DLL injection but with **different DLLs**:
- 3dmigoto: `d3d11.dll`
- UE4SS: `dwmapi.dll` (in ue4ss/ subfolder)

They can coexist in the same game directory using separate proxy targets. Modern UE4SS (v3.0+) with the subfolder layout makes this easier.

### Multiplayer Considerations

**Purely cosmetic, client-side only.** Only you see the replaced meshes/textures. The server sends standard geometry data. No data is sent to other players about visual modifications. No collision/physics/position changes. No known ban risk in Return to Moria's cooperative gameplay.

### Return to Moria Applications

| Application | Difficulty | Notes |
|------------|-----------|-------|
| Building piece retextures | EASY | Texture-only, no mesh editing |
| Weapon skins | EASY | Texture swap on weapon models |
| Armor color variations | EASY | Swap metal/cloth textures |
| Environmental recoloring | EASY | Ore, plants, stone surfaces |
| Custom weapon models | MEDIUM | Must maintain skeleton/bone structure |
| Custom armor models | MEDIUM | Skeletal mesh, preserve animations |
| Character appearance | HARD | Complex face/body modifications |
| HUD reskins | MEDIUM | 2D texture swaps on UI elements |

### Tools

| Tool | Purpose | URL |
|------|---------|-----|
| 3dmigoto | D3D11 interception framework | https://github.com/bo3b/3Dmigoto |
| GI-Model-Importer (GIMI) | Blender plugin + frame dump tools | https://github.com/SilentNightSound/GI-Model-Importer |
| UModel | Browse/export UE4 assets from .pak | gildor.org |
| Blender 3.0+ | 3D modeling with 3dmigoto plugin | blender.org |

---

## Deep Dive — Weather, Environment, and Spawn Control

### Lighting System

**AMorWorldLighting** — The master lighting actor containing all global lighting components:

| Component | Purpose |
|-----------|---------|
| `UDirectionalLightComponent* DirectionalLight` | Sun / main directional light |
| `USkyLightComponent* SkyLight` | Sky illumination |
| `UExponentialHeightFogComponent* HeightFog` | Global fog system |
| `UPostProcessComponent* LowHealth` | Low-health visual effect |
| `UPostProcessComponent* HungerDebuff` | Hunger visual effect |
| `UPostProcessComponent* ShadowDebuff` | Darkness visual effect |
| `UPostProcessComponent* Cold` | Cold visual effect |
| `UPostProcessComponent* Poison` | Poison visual effect |
| `UPostProcessComponent* Despair` | Despair visual effect |
| `UPostProcessComponent* Singing` | Singing visual effect |
| `UPostProcessComponent* OrcHunter` | Orc Hunter visual effect |

**AMorLocalLightingInfo** — Per-zone lighting overrides:
- `FMorBakedLocalLighting BakedLightingData` — all baked settings (60+ properties)
- `bool bIncludeDirectionalLightParameters / bIncludeSkylightParameters / bIncludeHeightFogParameters`
- `UCurveLinearColor*` curves for time-of-day sun, skylight, sky crystal, fog
- `UPostProcessComponent* PostProcess` with `UBoxComponent* PostProcessBox`
- `float FalloffRadius`, `float FadeInTime`, `bool bEnabled`, `bool bIsOutdoorScene`

**FMorBakedLocalLighting** — The full lighting parameter set (key properties):

```
Directional Light:
  FLinearColor DirectionalLightLightColor       — Sun color
  float DirectionalLightVolumetricScatteringIntensity
  float DirectionalLightBloomScale / BloomThreshold
  FLinearColor DirectionalLightBloomTint
  float DirectionalLightShadowAmount            — Shadow darkness
  float DirectionalLightSpecularScale           — Reflections
  float DirectionalLightTemperature             — Kelvin color temperature

Height Fog:
  float HeightFogFogDensity                     — Main fog density
  float HeightFogFogHeightFalloff               — Height gradient
  FLinearColor HeightFogFogInscatteringColor    — Fog color
  float HeightFogFogMaxOpacity                  — Maximum opacity
  float HeightFogStartDistance / FogCutoffDistance
  FLinearColor HeightFogDirectionalInscatteringColor
  float HeightFogVolumetricFogScatteringDistribution
  FLinearColor HeightFogVolumetricFogAlbedo / Emissive
  float HeightFogVolumetricFogExtinctionScale / Distance

Sky Light:
  FLinearColor SkylightLightColor               — Sky top color
  FLinearColor SkylightLowerHemisphereColor     — Sky bottom color
  float SkylightIntensity                       — Sky brightness
  FLinearColor SkylightOcclusionTint
  float SkylightMinOcclusion / OcclusionExponent
```

**Day/Night Enum:** `EGameplayTodLightMode` — `None` / `Both` / `Day` / `Night`

**Lighting LOD Groups:** `ELightLodGroup` — `DirectionalLight` / `SkyLight` / `ThrowableLight` / `PlayerPlacedLight` / `LightShaft`

### Temperature System

**Player Attributes (on UAbilitySystemComponent via GAS):**
```
FGameplayAttributeData Temperature           — offset 0x0280
FGameplayAttributeData TemperatureModifier   — offset 0x0290
FGameplayAttributeData ColdBuildupRate       — offset 0x02A0
FGameplayAttributeData ColdRecoverRate       — offset 0x02B0
```

**Temperature Manager:** `AMorTemperatureManager` (extends `AMorReplicatedManager`)
- `TSet<UMorThresholdEffectComponent*> TemperatureComponents`
- `float TemperatureUpdateInterval`

**Zone Temperature:** Each `FZoneDefinition` has `float ZoneTemperature` (base environmental temperature), `float WaterPrevalence`, `float LightPrevalence`, `UCurveFloat* LightingCurve`.

**Temperature Zones (EasySkyV2 Plugin):** `ATemperatureZone` actor with `Temperature`, `Priority`, `Power`, `Hardness` properties.

**Temperature Function Library:** `MorAttributesFunctionLibrary::GetTemperature(const AActor* Character)` — UFUNCTION, callable via ProcessEvent.

**GameplayEffects for Temperature:**
| Effect | Purpose |
|--------|---------|
| `GE_Warm` | Warmth buff |
| `GE_ColdDebuff` | Cold/chilling debuff |
| `GE_Freezing` | Severe cold (freezing) |
| `GE_Shadowed` | Darkness debuff |
| `GE_AntiDarknessBrewSip` | Counteracts darkness |
| `GE_DEV_RingOfPower` | Developer power ring |

### Spawn Control System

**AMorAISpawnManager** — Primary spawn manager:
- `float MaxSpawnLimit` — global spawn cap
- `TMap<EMorAISpawnContext, FActiveSpawners> CurrentActiveSpawners`
- `TArray<FMorAIQueuedSpawn> QueuedSpawns`
- `TMap<uint32, FMorAIDespawn> QueuedDespawns`
- `TArray<FMorAIDespawn> QueuedRespawns`
- `float SpawnAttemptCooldownTime`
- **`void BP_RequestSpawn(TSoftClassPtr<AMorCharacter>, FTransform, UObject*, EMorAISpawnContext)`** — UFUNCTION, callable via ProcessEvent!

**Spawn Context Enum:** `None` / `AIPopulation` / `AIPatrol` / `AIChallenge` / `AILair` / `AIWaveEncounter` / `AISavedSingleSpawner`

**Spawn Type Enum:** `Fallback` / `FromBelow` / `FromAbove`

**AMorAISavedSingleSpawner:**
- `TSoftClassPtr<AMorCharacter> ExplicitCharacterClass`
- `AMorCharacter* SpawnedCharacter`
- `bool bSpawnedCharacterKilled`, `bool bDontAutoSpawn`
- `void SpawnAiCharacter()` — UFUNCTION
- `void SaveCharacterDeath()` — UFUNCTION

**Quick Spawn Manager:** `AMorAIQuickSpawnManager` with `AMorAISpawnManager*` reference and `TArray<AMorCharacter*> CurrentSpawns`.

### Debug Menus and Dev Tools

**Debug Menu Blueprints found in CXX dump:**

| Blueprint | Key Functions |
|-----------|--------------|
| `BP_DebugMenu_WorldLayout` | `Unlock All Chapters()`, `Toggle Fog of War on Map()`, `Show Cell Status()` |
| `BP_DebugMenu_AI` | AI behavior controls |
| `BP_DebugMenu_Hordes` | Horde spawning controls |
| `BP_DebugMenu_Scene` | Scene/lighting controls |
| `BP_DebugMenu_Recipes` | `All Recipes`, `2-1 Recipes`, `Nothing Discovered` |
| `BP_DebugMenu_Character` | Character attribute controls |
| `FGKDebugMenu` | Core debug menu framework |
| `WBP_BlueprintCheatsWidget` | Cheat entry UI |

**Developer Items:**

| Item | Purpose |
|------|---------|
| `DEV_Pick_GodPick` | Indestructible developer pickaxe |
| `DEV_SwordOfSlaying` | Developer sword |
| `BP_DEV_Gloves` | Developer gloves |
| `GE_DEV_RingOfPower` | Developer power ring effect |

### Practical Use Cases

| Feature | Approach | Effort |
|---------|----------|--------|
| Toggle darkness immunity | Apply/remove `GE_Shadowed` / `GE_AntiDarknessBrewSip` | LOW |
| Temperature control | Modify `Temperature` attribute via GAS, apply `GE_Warm`/`GE_ColdDebuff` | LOW |
| Custom fog density | Modify `AMorWorldLighting.HeightFog` properties | MEDIUM |
| Zone lighting override | Modify `AMorLocalLightingInfo.BakedLightingData` | MEDIUM |
| Spawn enemies on demand | Call `BP_RequestSpawn` on `AMorAISpawnManager` | MEDIUM |
| Suppress enemy spawns | Set `MaxSpawnLimit = 0` on spawn manager | LOW |
| Day/night toggle | Set `EGameplayTodLightMode` | LOW |
| Apply dev buffs | Apply `GE_DEV_RingOfPower`, `GE_BootsOfDebugSpeed` | LOW |
| Access debug menus | Instantiate debug menu Blueprint widgets | MEDIUM |

---

## Deep Dive — Game Menus and Controller/Input Access

### FGK UI Framework Architecture

The game uses a custom screen stack system built on top of UMG:

```
UUserWidget
  → UFGKUserWidget              (input listening helpers)
       → UFGKHUD                (HUD overlays: Show/Hide/IsShowing)
       → UFGKUIScreen           (full screens: screen stack lifecycle)
            → UFGKPopup         (modal confirmations)
            → UMorCraftingScreen, UMorInventoryScreen, UMorSettingsScreen
            → UMorUIMainMenuScreen, UMorCalloutHud, UMorFreeCameraHUD
            → UBuildOverlayWidget, UMorGameInteractiveMinimapWidget
```

### UFGKUIManager (Core Screen Manager)

The central UI orchestrator (accessible via `UMorUIManager::BPGetManager(WorldContext)` — a UFUNCTION).

**Key Members:**
- `TArray<UFGKHUD*> UnderlayHuds` (0x0040) — permanent HUD layers below screens
- `TArray<UFGKHUD*> OverlayHuds` (0x0050) — permanent HUD layers above screens
- `TMap<UClass*, UFGKUIScreen*> CachedScreens` (0x0080) — screen instance cache
- `TArray<UFGKUIScreen*> OpenScreensStack` (0x01C0) — the screen stack
- `UInputComponent* InputComponent` (0x0030) — input bindings

**Key UFUNCTIONs (all callable via ProcessEvent):**
- `ShowScreen(TSubclassOf<UFGKUIScreen>)` — push screen onto stack
- `HideScreen(UFGKUIScreen*)` — pop specific screen
- `HideAllScreens()` — clear entire stack
- `IsScreenShowing(TSubclassOf<UFGKUIScreen>)` — query
- `GetScreen(TSubclassOf<UFGKUIScreen>)` — get cached instance
- `GetHUD(TSubclassOf<UFGKHUD>, EFGKUIResult&)` — get HUD instance
- `SetHudVisibility(EFGKHudVisibility)` — control HUD layer visibility
- `SetUiInputMode()` / `SetGameInputMode()` — input mode switching
- `ShowTwoButtonPopup` / `ShowOneButtonPopup` — modal dialogs
- `BindToScreenShownEvent` / `BindToScreenHiddenEvent` — lifecycle listeners

### Screen Lifecycle Hooks (on every UFGKUIScreen)
- `OnBeforeShow()` / `OnAfterShow()` / `OnBeforeHide()` / `OnAfterHide()`
- `OnBindInputs()` / `OnUnbindInputs()` — input action binding when screen gains/loses focus
- `Show()` / `Hide()` / `IsShowing()`
- Tab support: `ShowTabWithName(FName)`, `OnTabShown/OnTabHidden/OnTabAdded`

### Complete Game Screen Catalog

**Main Menu:**
| Class | Purpose |
|-------|---------|
| `UWBP_UI_StartScreen_C` | Title/start screen |
| `UWBP_UI_CharacterSelectScreen_C` | Character selection |
| `UWBP_UI_CreateWorldScreen_C` | World creation |
| `UWBP_UI_LoadWorldScreen_C` | Load saved world |
| `UWBP_UI_JoinWorldScreen_C` | Join multiplayer world |
| `UWBP_UI_CreditsScreen_C` | Credits |
| `UWBP_UI_DLC_Screen_C` | DLC content |

**Pause/Escape:**
| Class | Purpose |
|-------|---------|
| `UUI_WBP_EscapeMenu2_C` | Escape menu (Resume, Settings, Leave, Quit, Player Mgmt, FreeCam, Difficulty) |
| `UUI_WBP_PauseMenu_C` | Tabbed pause menu hosting Goals, Inventory, Map |

**Settings (inside WBP_SettingsScreen_C):**
| Tab Widget | Purpose |
|-----------|---------|
| `WBP_VideoTab` | Graphics settings |
| `WBP_AudioTab` | Audio settings |
| `WBP_ControlsTab` | KB/M controls (sensitivity, invert, toggle sprint) |
| `WBP_ControllerTab` | Gamepad settings (sensitivity, vibration, invert) |
| `WBP_ControllerMappingTab` | Gamepad button layout display |
| `WBP_EditMappingTab` | Key rebinding |
| `WBP_GameplayTab` | Gameplay options |
| `WBP_AccessibilityTab` | Accessibility options |

**Gameplay Screens:**
| Class | Purpose |
|-------|---------|
| `UWBP_UI_Inventory_Screen_C` | Full inventory (~0x750 bytes, drag/drop, gamepad, context menus) |
| `UUI_WBP_Crafting_Screen_C` | Crafting station (queue, recipe list, fuel) |
| `UUI_WBP_Runecrafting_Screen_v2_C` | Rune crafting |
| `UUI_WBP_Repair_Screen_V2_C` | Repair station |
| `UWBP_UI_Trading_Screen_C` | Trading (offers/orders, currency) |
| `UWBP_GameMinimapFull_C` | Full map (dual view, virtual cursor, waypoints) |
| `UWBP_UI_Cosmetics_Screen_C` | Cosmetic customization |
| `UWBP_UI_Expedition_Screen_C` | Expedition management |
| `UWBP_UI_Settlement_Management_Screen_C` | Settlement management |
| `UUI_WBP_Tint_Screen_C` | Tint station |
| `UUI_WBP_FastTravelScreen_C` | Fast travel |
| `UWBP_UI_Conversation_Screen_C` | NPC conversation |

**HUD Overlays:**
| Class | Purpose |
|-------|---------|
| `UWBP_MoriaHUD_C` | Main HUD (BossBar, SleepPrompt, Singing, ActionBar, SystemMessages) |
| `UWBP_UI_ActionBar_C` | Action bar (8 slots + epic + hands) |
| `UUI_WBP_PlayerStatsWidget_Overlay_C` | Player stats |
| `UUI_WBP_StatusEffectsOverlay_C` | Status effects |
| `UUI_WBP_StaminaBar_Overlay_C` | Stamina bar |
| `UUI_WBP_Minimap_Overlay_C` | Minimap |
| `UUI_WBP_SubtitleOverlay_C` | Subtitles |
| `UUI_WBP_NotificationOverlay_C` | Notifications |
| `UUI_WBP_TutorialOverlay_C` | Tutorial prompts |
| `UWBP_AwarenessOverlay_C` | Enemy awareness indicator |

### Controller/Input System

The game uses THREE input layers:

**1. UE4 Legacy Input** (primary) — ActionMappings/AxisMappings on UPlayerInput. Our mod already uses `register_keydown_event` from this system.

**2. Enhanced Input** (present, lightly used) — `UInputAction`, `UInputMappingContext`, `UEnhancedPlayerInput`. Runtime API available:
- `AddMappingContext(UInputMappingContext*, Priority)` — add context
- `RemoveMappingContext(UInputMappingContext*)` — remove
- `QueryKeysMappedToAction(UInputAction*)` — get bound keys
- `RequestRebuildControlMappings(bForceImmediately)` — rebuild

**3. CommonInput** (input type detection) — `UCommonInputSubsystem` per LocalPlayer:
- `CurrentInputType` / `LastInputType` (ECommonInputType: MouseAndKeyboard=0, Gamepad=1, Touch=2)
- `GamepadInputType` (FName: "Generic", "PS5")
- `OnInputMethodChanged` delegate — broadcast when switching KB ↔ gamepad
- Almost every screen widget listens for `OnInputChanged(ECommonInputType)`

**Controller Data Classes:**
- `UKBMBaseControllerData_C` — keyboard/mouse button icons
- `UGenericBaseControllerData_C` — generic gamepad (Xbox) icons
- `UPS5BaseControllerData_C` — PS5/DualSense icons
- Each contains `InputBrushDataMap` (key → image mappings)

**MorPlayerController Input Integration:**
- `TArray<TSubclassOf<UUserWidget>> HudWidgets` (0x09E0) — HUD widget classes
- `TArray<FMorHudInfo> HudToggleWidgets` (0x09F0) — HUDs with toggle keys
- `TMap<FKey, UUserWidget*> ToggleHuds` (0x0A10) — key → toggle HUD map
- `UUserWidget* DebugMenu` (0x0AD0) — debug menu widget

**Key Remapping:**
- `UMorSettingsKeySelector` — key selector widget with `UInputKeySelector`, `FInputChord CurrentSelectedKey`, `ConfirmSelectedKey(FInputChord&)`, `ResetToCurrent()`

### Runtime Modification — What's Possible

**YES — via UE4SS C++ mod (no pak needed):**

| Capability | How |
|-----------|-----|
| Add buttons/panels to existing screens | `UIManager->GetScreen(Class)` → `GetWidgetFromName` → `AddChild(NewWidget)` |
| Intercept input events | Hook `APlayerController::InputKey` or `UPlayerInput::ProcessInputStack` |
| Register new input actions (legacy) | Call `UPlayerInput::AddActionMapping` / `AddAxisMapping` at runtime |
| Register new input actions (Enhanced) | Create `UInputAction` objects, `UInputMappingContext`, call `AddMappingContext` |
| Modify controller button mapping | Modify `UPlayerInput::ActionMappings` / `AxisMappings` at runtime |
| Show/hide screens programmatically | `UMorUIManager::ShowScreen` / `HideScreen` / `ShowScreenWithHandle` |
| React to input mode changes | Bind to `UCommonInputSubsystem::OnInputMethodChanged` delegate |
| Create modal dialogs | `UIManager->ShowTwoButtonPopup` / `ShowOneButtonPopup` |
| Inject widgets into HUD | Get HUD via `UIManager->GetHUD(Class)`, add child widgets |

**REQUIRES pak replacement:**

| Capability | Why |
|-----------|-----|
| Modify Blueprint graphs (ExecuteUbergraph) | Compiled bytecode, not accessible via reflection |
| Change widget layouts/positioning of existing elements | Hardcoded in Blueprint construction (movable via C++ at runtime as workaround) |
| Add new ScreensConfigTable entries | DataTable rows need to exist before FGK init |
| Change visual style/materials of existing widgets | Material references in Blueprint defaults |
| Modify controller mapping display labels | Hardcoded FText arrays in BP construction |

### Key APIs for Runtime UI Work

```
1. Get UI Manager:
   UMorUIManager::BPGetManager(WorldContext)  // static UFUNCTION

2. Get any screen:
   UIManager->GetScreen(ScreenClass)          // returns cached instance

3. Show/hide:
   UIManager->ShowScreen(ScreenClass)
   UIManager->HideScreen(ScreenInstance)

4. Screen lifecycle events:
   UIManager->BindToScreenShownEvent(ScreenClass, Delegate)
   UIManager->BindToScreenHiddenEvent(ScreenClass, Delegate)

5. Input mode:
   UIManager->SetUiInputMode()   // mouse cursor visible
   UIManager->SetGameInputMode() // mouse cursor hidden

6. Widget injection:
   ScreenInstance->GetWidgetFromName(FName)
   PanelWidget->AddChild(NewWidget)

7. Input detection:
   UCommonInputSubsystem->GetCurrentInputType()
   UCommonInputSubsystem->OnInputMethodChanged  // delegate
```

### KEY TAKEAWAY — Controller Support Done Right

The v6.2.0–v6.3.0 approach of polling XInput/DirectInput manually was the wrong path. The game already has a full controller infrastructure:

1. **`WBP_ControllerTab`** — gamepad settings (sensitivity, vibration, invert) already in the Settings screen
2. **`WBP_ControllerMappingTab`** — gamepad button layout display with General Gameplay and Build Mode views
3. **`UCommonInputSubsystem`** fires `OnInputMethodChanged` when switching KB ↔ gamepad — every screen widget already listens for this
4. **Every major screen** (inventory, crafting, trading, map, build HUD) already has full gamepad support with `OnInputChanged(ECommonInputType)` handlers

The correct approach for mod controller support: **hook into CommonInput's `OnInputMethodChanged` delegate** and register mod-specific input actions via `UPlayerInput::AddActionMapping` or Enhanced Input's `AddMappingContext`. This integrates natively with the game's own KB/gamepad switching rather than fighting it with raw HID polling. The mod's toolbar navigation, slot selection, and action buttons should bind to standard UE4 input actions that CommonInput routes to the correct physical button automatically.

This would replace the ~600 lines of XInput/DirectInput/DualSense polling code with a handful of input action registrations that work with ANY controller the game already supports.

### FFGKUIScreenConfig (Screen Definition DataTable Row)
Each screen is configured via a DataTable row containing:
- `TSoftClassPtr<UFGKUIScreen> ScreenClass` — the widget class
- `FName ToggleInputAction` — input action name that toggles this screen
- `bTakesInputControl` — whether screen captures input focus
- `bHideOpenScreens` — whether opening this hides other screens
- `EFGKHudVisibility HudBehavior` — what happens to HUDs when screen opens
- `TArray<TSoftClassPtr<UFGKHUD>> HudsToShow` — specific HUDs to show
- `EFGKScreenUserAccess UserAccess` — Everyone or DevOnly
- `int32 ZOrderOffset` — Z-order layering

---

## Related Document

The full editor project reconstruction pipeline, FGK cache bypass research, pak mounting techniques, IoStore tooling, and step-by-step setup guide are in the companion document:

**→ [Moria Replication Plan - Editor Project Reconstruction.md](Moria%20Replication%20Plan%20-%20Editor%20Project%20Reconstruction.md)**
