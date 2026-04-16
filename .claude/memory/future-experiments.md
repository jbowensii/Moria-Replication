---
name: future-experiments
description: Research findings from April 2026 — pak auto-mount, FGK cache bypass, GAS manipulation, IoStoreLoaderMod, DiscoveryManager injection, new capabilities
type: project
originSessionId: faf77fec-764b-499b-8ea8-e24075baf1b0
---
## Build Menu Injection — The Answer Exists

**Existing Moria mods (Secrets of Khazad-dum, TobiModsAddons) already add new constructions** using the engine's auto-mount system. Place IoStore triplets (`*_P.pak` + `.ucas` + `.utoc`) in `Moria/Content/Paks/` — engine loads them before FGK init, cache naturally includes new rows.

**Why:** FGK wrappers initialize AFTER pak mounting. Our previous approach failed because we injected rows AFTER the cache was built. The fix is to get rows in BEFORE, via pak.

## THE HOLY GRAIL — Editor Project Reconstruction (PROVEN)

**25+ game communities use this pattern.** Create a template UE4.27 project from UHT dumps, populate with imported assets, create new content in the editor, cook, pack as IoStore, deploy to Content/Paks/.

**We already have the hardest prerequisite**: 151 UHT modules + 3,028 CXX headers in dumps/.

**Key tools**: UE4GameProjectGenerator (github.com/Archengius/UE4GameProjectGenerator), JsonAsAsset (with Local Fetch for bulk import), retoc (IoStore packaging).

**What this SOLVES**: New DataTable rows cooked into paks load BEFORE FGK init → cache naturally includes them → **new constructions appear in the build menu**. Also unlocks new Blueprints, meshes, textures, materials, widget BPs.

**Closest reference**: Deep Rock Galactic (FSD-Template) — same UE4.27 engine, proven template + cooking workflow.

**Roadmap**: Phase 1 (1-2 days) generate template, Phase 2 (2-5 days) import assets, Phase 3 create content, Phase 4 cook + deploy.

**Detailed step-by-step plan**: `docs/Moria Replication Plan - Editor Project Reconstruction.md` — 7 phases, milestones, risk assessment, tool installation, cooking/packaging commands, installer integration.

**Current tool status** (as of April 2026): UE4.27 editor installed. FModel and retoc NOT yet installed (easy: fmodel.app download + cargo install retoc). Rust toolchain ready. 151 UHT modules + 3,028 CXX headers already extracted.

**Unique room editing**: User knows where the .umap sublevel files are for landmark rooms. Plan: extract via FModel/retoc → edit with UAssetGUI (remove misplaced actor entries) → pack as _P.pak override. Permanently removes offending rocks/dirt piles from hand-crafted rooms.

## Top Approaches (Prioritized)

1. **DiscoveryManager.Recipes injection** — Append recipe structs directly to AMorDiscoveryManager.Recipes TArray at offset 0x0220. Bypasses FGK entirely. UNTESTED but low effort to validate.

2. **Auto-mount pak pipeline** — Create UE4.27 project → cook → retoc to-zen → place in Content/Paks/. PROVEN working in other Moria mods.

3. **HandleDataTableChanged delegate test** — Check if FGK wrappers subscribe to UDataTable::OnDataTableChanged(). If yes, sig-scan HandleDataTableChanged (ENGINE_API exported) and call it after addRow(). 30-minute test.

4. **Hook FGK PostLoad** — vtable-hook MorConstructionRecipesTable::PostLoad, inject rows into underlying UDataTable (at wrapper + 0x28) BEFORE original PostLoad builds the cache.

5. **IoStoreLoaderMod port** — Runtime IoStore mounting from C++ via MinHook + AOB sigscanning. Proven on Hi-Fi RUSH (UE4.27). github.com/akmubi/IoStoreLoaderMod.

## New Capabilities Discovered

- **GAS manipulation** — Apply/remove GameplayEffects via ProcessEvent on UAbilitySystemComponent. Hundreds of existing effects (GE_DEV_RingOfPower, GE_BootsOfDebugSpeed, buffs, debuffs). HIGH feasibility.
- **Custom UFunction registration** — Register native C++ as UFunction on any UClass at runtime via UE4SS's NewObject<UFunction>, SetFuncPtr, GetFuncMap().Add(). Could add cache-rebuild function to FGK wrapper.
- **Texture/material replacement** — CreateDynamicMaterialInstance + Set*ParameterValue via ProcessEvent. Also UE4-DDS-Tools for offline .uasset texture injection.
- **Audio** — PlaySound2D/PlaySoundAtLocation via UGameplayStatics. Limited to existing game sounds without pak mounting.
- **Blueprint function hooking** — spaghetti (github.com/bananaturtlesandwich/spaghetti) + KismetKompiler for modifying cooked Blueprint bytecode offline.
- **CDO modification** — Modify Default__<ClassName> objects to change all future instances. GameInstance.ReferencedObjects prevents GC across level loads.

## FGK Wrapper Internals (For Cache Work)

```
UFGKDataTableBase: 0x28=TableAsset, 0x38=DynamicTableAsset, 0x40-0x10F=hidden cache
UMorConstructionRecipesTable: 0x110=TMap<FMorConstructionRowHandle,FName> ConstructionRecipeLookup
UMorConstructionsTable: 0x110=TMap<TSoftClassPtr<AActor>,FName> ActorRowNameLookup
```

Data flow: UDataTable → FGK wrapper cache → AMorDiscoveryManager.Recipes (0x0220) → BuildHUD.GetRecipeBlocks()

## Key Tool URLs

- retoc (IoStore conversion): github.com/trumank/retoc
- IoStoreLoaderMod (runtime mount): github.com/akmubi/IoStoreLoaderMod
- KismetKompiler (BP bytecode): github.com/tge-was-taken/KismetKompiler
- spaghetti (BP function hook): github.com/bananaturtlesandwich/spaghetti
- UE4-DDS-Tools (texture inject): github.com/matyalatte/UE4-DDS-Tools
- UE.Toolkit (XML runtime editing): github.com/RyoTune/UE.Toolkit
- Full research doc: docs/Future Research - Build Menu Injection and New Capabilities.md

## Deep Dive Findings (April 2026)

### Blueprint Behavior Injection
- **spaghetti** (github.com/bananaturtlesandwich/spaghetti) — hooks cooked Blueprint functions by redirecting function map. UE4.27 compatible. Single-asset-per-pak limitation. Replacement only, not addition.
- **KismetKompiler** (github.com/tge-was-taken/KismetKompiler) — decompile/recompile Blueprint bytecode. Tested on UE4.23, 4.27 uncertain but plausible. Can compile into existing .uasset.
- Combined workflow: retoc extract → KismetKompiler decompile → edit .kms → recompile → pack _P.pak
- Safe targets: UI_WBP_BuildHUDv2 (UI-only). Risky: recipe/crafting BPs (MP desync if server/client mismatch).

### 3dmigoto Mesh/Texture Replacement
- D3D11 proxy DLL interception, hash-based mesh/texture identification
- Fully compatible with UE4.27 + GPU skinning. Proven on Genshin Impact, Honkai Star Rail.
- Coexists with UE4SS via separate proxy DLLs (3dmigoto=d3d11.dll, UE4SS=dwmapi.dll)
- Purely client-side cosmetic, no MP desync. 0-5% FPS impact for typical mods.
- Moria uses: building retextures (easy), weapon/armor skins (easy), custom models (medium)

### Weather/Environment/Spawn Control
- **AMorWorldLighting**: DirectionalLight, SkyLight, HeightFog, PostProcess for each debuff (Cold, Shadow, Poison, Despair, Singing)
- **AMorLocalLightingInfo**: Per-zone overrides with FMorBakedLocalLighting (60+ properties including fog density, sun color/temperature, skylight color/intensity)
- **Temperature**: GAS attributes (Temperature, TemperatureModifier, ColdBuildupRate, ColdRecoverRate) on AbilitySystemComponent. Zone-level ZoneTemperature. Effects: GE_Warm, GE_ColdDebuff, GE_Freezing.
- **Spawn**: AMorAISpawnManager.BP_RequestSpawn is a UFUNCTION! MaxSpawnLimit property. Contexts: AIPopulation/AIPatrol/AIChallenge/AILair/AIWaveEncounter.
- **Debug menus**: BP_DebugMenu_WorldLayout (Unlock All Chapters, Toggle Fog of War), BP_DebugMenu_AI, BP_DebugMenu_Hordes, BP_DebugMenu_Scene, BP_DebugMenu_Recipes (All Recipes).
- **Dev items**: DEV_Pick_GodPick, DEV_SwordOfSlaying, GE_DEV_RingOfPower.
- **Day/Night**: EGameplayTodLightMode enum (None/Both/Day/Night).

### Enhancement Ideas (8 items)
1. GAS buff/debuff system — Apply existing GE_ effects via ProcessEvent. LOW effort.
2. Custom building appearances — CreateDynamicMaterialInstance + SetVectorParameterValue. MEDIUM effort.
3. Sound feedback — PlaySound2D/PlaySoundAtLocation from existing USoundCue objects. LOW effort.
4. CDO modification — Modify Default__<ClassName> objects for game balance. GameInstance.ReferencedObjects prevents GC.
5. New constructions via pak — UE4.27 project → cook → retoc → Content/Paks/. PROVEN.
6. Blueprint behavior injection — spaghetti + KismetKompiler. See deep dive above.
7. 3dmigoto mesh/texture replacement — D3D11 interception. See deep dive above.
8. Weather/environment control — GAS + lighting system. See deep dive above.

### Game Menu and Controller/Input Access
- **UFGKUIManager** — central screen stack manager. Get via `UMorUIManager::BPGetManager(WorldContext)` UFUNCTION.
- Key UFUNCTIONs: `ShowScreen`, `HideScreen`, `GetScreen`, `GetHUD`, `SetUiInputMode`/`SetGameInputMode`, `ShowTwoButtonPopup`
- Screen lifecycle hooks: `OnBeforeShow`/`OnAfterShow`/`OnBeforeHide`/`OnAfterHide` on every `UFGKUIScreen`
- Widget injection: `GetScreen(Class)` → `GetWidgetFromName(FName)` → `PanelWidget->AddChild(NewWidget)` — works at runtime
- Three input layers: Legacy (ActionMappings), Enhanced (UInputAction/UInputMappingContext), CommonInput (KB/gamepad detection)
- `UCommonInputSubsystem.OnInputMethodChanged` delegate fires on KB↔gamepad switch. `GetCurrentInputType()` returns MouseAndKeyboard=0, Gamepad=1, Touch=2.
- Controller data classes: UKBMBaseControllerData_C, UGenericBaseControllerData_C, UPS5BaseControllerData_C (with InputBrushDataMap for icons)
- Can add/remove input actions at runtime via `UPlayerInput::AddActionMapping` or Enhanced Input `AddMappingContext`
- Complete screen catalog: 30+ screen classes, 10+ HUD overlays, 9 settings tabs — all documented in future research doc
- **KEY TAKEAWAY**: v6.2.0 XInput/DirectInput polling was the wrong approach. Hook CommonInput's OnInputMethodChanged + register input actions via AddActionMapping/AddMappingContext instead. Integrates natively with game's KB/gamepad switching. Replaces ~600 lines of raw HID polling.

## QuickBuild Timing Reductions (From Earlier Research)

Game state logging (v2.7.7) confirmed all pointers remain stable during F-key cycling. Some delays may be reducible:

- **500ms post-completion cooldown** — try 300ms. Protects against ghost flicker / UI cascade. Not a crash risk, cosmetic only.
- **150ms DIRECT path cooldown** — try 100ms. Prevents duplicate SelectRecipe queueing.
- **350ms Show/Hide cooldown** — do NOT reduce. Protects against MovieScene re-entrancy crash (engine-level).
- **5000ms SM timeout** — do NOT change. Watchdog for stuck state machine.
