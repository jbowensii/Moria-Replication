# UE4SS Return to Moria - Project Memory

## Project Overview
- **Game**: Return to Moria (Lord of the Rings) by Free Range Games
- **Engine**: Unreal Engine 4.27
- **UE4SS Version**: Custom-built from source (main branch, 0bfec09e — v4.0.0-rc1)
- **Game Path**: `C:\Program Files\Epic Games\ReturnToMoria\Moria\Binaries\Win64`
- **UE4SS Dir**: `<game>/ue4ss/` (SUBFOLDER structure — dwmapi.dll in Win64/, UE4SS.dll+settings+Mods/ in Win64/ue4ss/)
- **Workspace**: `c:\Users\johnb\OneDrive\Documents\Projects\UE4SS Testing`
- **GitHub**: `https://github.com/jbowensii/MoriaAdvancedBuilder`
- **UE4 Engine Headers**: `C:\Program Files\Epic Games\UE_4.27\Engine\Source\Runtime\Engine\Classes`
- **Player Character Class**: `BP_FGKDwarf_C`

## C++ Mod: MoriaCppMod
- **Source**: `<workspace>/cpp-mod/MyCPPMods/MoriaCppMod/src/dllmain.cpp` (~11,000 lines)
- **Inlined files**: moria_common.inl, moria_inventory.inl, moria_datatable.inl, moria_DefinitionProcessing.inl
- **New header**: `moria_dualsense.h` — DualSense raw HID reader + DirectInput gamepad reader
- **Testable header**: `<workspace>/cpp-mod/MyCPPMods/MoriaCppMod/src/moria_testable.h`
- **Deploy to**: `<game>/ue4ss/Mods/MoriaCppMod/dlls/main.dll` + `enabled.txt` + `definitions/`
- **STATUS**: v6.3.9 on GitHub
- **GitHub Tags**: v2.7-v2.7.7, v3.0.0, v3.1.0, v3.1.5, v4.0.0, v4.1.0, v4.3, v5.0.0-v5.5.2, v6.0.0, v6.1.0, v6.2.0, v6.3.0, v6.3.5, v6.3.6, v6.3.7, v6.3.8, v6.3.9

## Key Technical Rules
- **ALL file I/O must use `modPath("Mods/...")`** — process CWD is Win64/ but files live in Win64/ue4ss/
- **NEVER call FName::ToString() on raw memory offsets.** Only safe on UE4SS API FNames, FText::ToString, ForEachProperty names
- **Max 3 UpdateInstanceTransform calls per frame** (render thread crash)
- **bLock is THE recipe identifier** — resolved via reflection, cached in `s_off_bLock`
- **Post-hook contamination**: `m_isAutoSelecting` + `AutoSelectGuard` RAII suppresses capture during quickbuild
- **Property offsets**: ALL resolved via runtime reflection (v2.0+), no hardcoded Blueprint offsets
- **Inventory modification**: Use `ServerDebugSetItem` (Server RPC, works in MP) — NOT `RequestAddItem` (local-only, fails on non-host clients). NEVER raw memory writes
- **DataTable lazy binding**: Must be explicitly bound before use; `bindAllDataTables()` exists but never auto-called
- **Definition processing**: Zero hardcoded offsets — all via `ForEachProperty` → `GetOffset_Internal` → `std::memcpy`
- **GameMods.ini**: `Mods/GameMods.ini` (root Mods dir, NOT inside MoriaCppMod)
- **F12 config tabs**: Key Bindings, Game Options, Environment, Game Mods (CONFIG_TAB_COUNT=4)

## Header Sources (3 places)
1. **UE4 Engine Source**: `C:\Program Files\Epic Games\UE_4.27\Engine\Source\Runtime\Engine\Classes`
2. **CXXHeaderDump**: `<workspace>/dumps/CXXHeaderDump/` — 3,028 `.hpp` files (reflected properties + byte offsets)
3. **UHTHeaderDump**: `<workspace>/dumps/UHTHeaderDump/` — 151 module directories (clean function signatures)

## Build Commands & Environment
- **VS2026** (v18), MSVC v14.50, CMake 4.1.2, Rust 1.93.1
- **Config**: `Game__Shipping__Win64` (NOT Release/Debug)
- **Tests**: 5 test files (file_io, key_helpers, loc, memory, string_helpers), 286 tests
```bash
# Build mod only (~5s):
cd "<workspace>/cpp-mod" && PATH="$PATH:/c/Users/johnb/.cargo/bin" && "/c/Program Files/Microsoft Visual Studio/18/Community/Common7/IDE/CommonExtensions/Microsoft/CMake/CMake/bin/cmake.exe" --build build --config "Game__Shipping__Win64" --target MoriaCppMod
# Deploy mod:
cp build/MyCPPMods/MoriaCppMod/Game__Shipping__Win64/MoriaCppMod.dll "<game>/ue4ss/Mods/MoriaCppMod/dlls/main.dll"
```

## Git Notes
- **Repo root**: `<workspace>/cpp-mod/` (NOT workspace root)
- **Push remote**: `moria` (NOT `origin` — origin points to UE4SS template repo)
- `git push moria main --tags`

## UE4SS Settings
- **Settings file**: `<game>/ue4ss/UE4SS-settings.ini` | **Log**: `<game>/ue4ss/UE4SS.log`
- GraphicsAPI: `dx11` (opengl crashes game!), RenderMode: ExternalThread
- **Currently deployed**: Debug config (ConsoleEnabled=1, GuiConsoleEnabled=0, Verbose=true, s_verbose=true)
- **GuiConsoleEnabled CRASHES this game** (DXGI_ERROR_DEVICE_REMOVED) — never enable
- **DO NOT downgrade to v3.0.1**: removes `register_keydown_event`, flips FName defaults

## Installer
- **Script**: `<workspace>/installer/KhazadDumAdvancedBuilderPack.iss` (outside git repo)
- **Build**: `<workspace>/installer/build.ps1` (-SkipBuild -SkipSign for quick rebuilds)
- **Output**: `<workspace>/installer/output/KhazadDumAdvancedBuilderPack_v{Version}_Setup.exe`
- **Signing**: SSL.com eSigner via `C:\Users\johnb\Tools\CodeSignTool\sign.bat`
- Proxy DLL from `build/Game__Shipping__Win64/bin/dwmapi.dll` (not zDEV/)

## Version Tracking (all must update together)
1. `dllmain.cpp` line 2 header comment
2. `dllmain.cpp` ModVersion = STR("x.y")
3. `dllmain.cpp` VLOG "Loaded vX.Y"
4. `dllmain.cpp` help text "vX.Y: F1-F8=..."
5. `installer/KhazadDumAdvancedBuilderPack.iss` — `#define MyAppVersion`
6. `installer/build.ps1` — `$Version`
7. `installer/staging/Win64/ue4ss/UE4SS-settings.ini` — comment header
7b. `installer/staging-server/Win64/ue4ss/UE4SS-settings.ini` — comment header
8. Git tag in `<workspace>/cpp-mod/`
- **Do NOT touch** GoogleTest `GIT_TAG v1.15.2` in tests/CMakeLists.txt

## Code Review — Intentionally Skipped Items
- **#9 stopOverlay race**: 3s timeout; only at shutdown
- **#11 TSet iteration**: Static/read-only DataTable RowMaps
- **#18 removeAimed throttle**: Keypress-only; throttle risks corrupting undo
- **W6 callDebugFunc IsValid**: null check from fresh `FindAllOf` is sufficient

## Custom Skills
- `/ue4-api` — UE4.27 API reference (engine, gameplay, UI, rendering, FGK, Moria, UE4SS patterns)
- `/ue4ss-stability` — stability rules, patterns, and code review for UE4SS C++ mods

## Workspace Structure
- `cpp-mod/` — Git repo root, C++ mod build tree + RE-UE4SS submodule
- `definitions/` — Item/recipe definition files
- `dumps/` — CXXHeaderDump (3,028 files) + UHTHeaderDump (151 modules)
- `installer/` — Inno Setup script, build.ps1, staging, output
- `mods/` — Workspace backups

## Topic Files
- [api-index.md](api-index.md) — all mod functions index
- [build-menu-injection.md](build-menu-injection.md) — ABANDONED (IoStore + JSON AddRow)
- [code-stability-audit.md](code-stability-audit.md) — full /ue4ss-stability rules audit
- [datatable-schemas.md](datatable-schemas.md) — DataTable row struct schemas
- [definition-processing.md](definition-processing.md) — Game Mods system
- [desktop-path.md](desktop-path.md) — user desktop path
- [feedback_both_desktops.md](feedback_both_desktops.md) — copy to both desktops
- [feedback_installer_banner.md](feedback_installer_banner.md) — installer banner preference
- [feedback_ue4_quaternions.md](feedback_ue4_quaternions.md) — UE4 quaternion convention (CRITICAL)
- [hism-permanent-removal.md](hism-permanent-removal.md) — ABANDONED
- [hism-removal-guide.md](hism-removal-guide.md) — remove/undo/type-rules/replay
- [icon-extraction.md](icon-extraction.md) — Canvas RT pipeline
- [inventory-features.md](inventory-features.md) — trash, remove attrs, effects
- [inventory-system.md](inventory-system.md) — FItemHandle, FItemInstance, containers
- [json-addrow-research.md](json-addrow-research.md) — FGK cache blocks build menu
- [feedback_gui_console_crash.md](feedback_gui_console_crash.md) — NEVER enable GuiConsoleEnabled (GPU crash)
- [feedback_ps5_controller_input.md](feedback_ps5_controller_input.md) — PS5 DualSense: only DirectInput works on Epic Games Store
- [feedback_validate_before_documenting.md](feedback_validate_before_documenting.md) — always verify features against source before docs
- [gamepad-support.md](gamepad-support.md) — D-pad Left toggle, XInput/DirectInput, bBlockInput, callout handling
- [mc-toolbar.md](mc-toolbar.md) — 9-slot UMG toolbar, slot dispatch
- [multiplayer-fixes.md](multiplayer-fixes.md) — isLocalContext, hook guards, FindAllOf elimination
- [mod-keybinds.md](mod-keybinds.md) — all keybinds + fixed keys
- [moria-common.md](moria-common.md) — moria_common.inl utilities
- [moria-datatable.md](moria-datatable.md) — DataTable CRUD utility
- [multipart-ghost-research.md](multipart-ghost-research.md) — multipart ghost research
- [pitch-roll-research.md](pitch-roll-research.md) — SOLVED v5.5.2
- [quick-build-system.md](quick-build-system.md) — reactive state machine
- [quickbuild-workflow.md](quickbuild-workflow.md) — full workflow
- [stability-audit.md](stability-audit.md) — PointLight spawning, VFX, tuning
- [ue4-struct-index.md](ue4-struct-index.md) — UE4 struct/widget byte-offset index
- [ue4ss-upgrade-plan.md](ue4ss-upgrade-plan.md) — upgrade plan (completed in v5.0.0)
- [ufunction-index.md](ufunction-index.md) — UFUNCTION signatures for ProcessEvent
- [ui-scaling-repositioning.md](ui-scaling-repositioning.md) — uiScale + drag positioning
- [v4-release-status.md](v4-release-status.md) — v4.0.0 release pipeline
- [v6-release-status.md](v6-release-status.md) — v6.0.0 release status
- [multiplayer-fly-fix.md](multiplayer-fly-fix.md) — v6.3.5 bIsLocalPlayerController, server-fly sweep, ServerDebugSetItem
- [controller-ui-removal.md](controller-ui-removal.md) — v6.3.5 removed F12 controller UI
- [installer-drive-handling.md](installer-drive-handling.md) — v6.3.9 non-C: drive fix, modPath() pattern, constants rationale
