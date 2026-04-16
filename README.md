# Moria Replication — UE4.27 Editor Project Reconstruction

Reconstruct a baseline Unreal Engine 4.27 editor project from **The Lord of the Rings: Return to Moria** shipped game content, enabling full-spectrum modding: new building pieces, DataTable modifications, biome customization, unique room fixes, and custom Blueprints — all cooked and packed as IoStore mod paks.

## Current Status

| Phase | Status | Description |
|-------|--------|-------------|
| Phase 1: Tool Installation & Extraction | Complete | FModel, retoc, UE4GameProjectGenerator installed; game assets extracted |
| Phase 2: Template Project Generation | **Complete** | UE4.27 project compiles cleanly, editor opens successfully |
| Phase 3: Asset Population | Not started | Import DataTables, configs, textures via JsonAsAsset |
| Phase 4: Content Modification | Not started | Modify DataTables, create new assets |
| Phase 5: Cook, Package, Deploy | Not started | Cook to IoStore paks, deploy to game |

## Quick Start

### Prerequisites
- **UE4.27 Editor** installed at `C:\Program Files\Epic Games\UE_4.27\`
- **Visual Studio 2022** with C++ game development workload
- **Windows 10/11 x64**

### Open the Editor
1. Double-click `scripts/Moria Editor.lnk` (or copy to your Desktop)
2. If prompted "Missing modules — rebuild?", click **Yes**
3. If prompted about new plugins, click **Dismiss**
4. Expected warning: `DefaultMediaTexture` missing — harmless, resolves in Phase 3

### Build from Command Line
```batch
"C:\Program Files\Epic Games\UE_4.27\Engine\Binaries\DotNET\UnrealBuildTool.exe" ^
  MoriaEditor Win64 Development ^
  -Project="<repo>\project\Moria.uproject"
```

## Repository Structure

```
Moria-Replication/
  project/                    — UE4.27 editor project (the main deliverable)
    Moria.uproject            — Project file (9 game modules, 16 plugins)
    Source/                   — 8,700+ source files across 30 module directories
      Moria/                  — Main game module (5,100+ files)
      FGK/                    — Free-range Games Kit (1,700+ files)
      FGK*/                   — FGK sub-modules (Analytics, DebugMenu, etc.)
      [other modules]         — Reference-only (not compiled, kept for lookup)
    Config/                   — Editor-generated config files
    Binaries/                 — Build output (gitignored)
    Intermediate/             — Build intermediates (gitignored)
  docs/                       — Design documents and research
  scripts/                    — Automation scripts and shortcuts
    phase2_fix_compilation.md — Step-by-step guide to reproduce Phase 2
    extract_game_assets.py    — Phase 1 asset extraction automation
    Moria Editor.lnk          — Desktop shortcut for the editor
  tools/                      — Third-party tools (gitignored, install locally)
  CLAUDE.md                   — AI assistant context
  README.md                   — This file
```

### Compiled Modules (9 game modules)
| Module | Files | Description |
|--------|-------|-------------|
| Moria | 5,114 | Main game module — characters, building, inventory, AI, world |
| FGK | 1,713 | Free-range Games Kit framework |
| FGKAnalytics | 8 | Analytics integration |
| FGKDebugMenu | 16 | Debug menu system |
| FGKLoadingScreen | 6 | Loading screen |
| FGKNavPowerPlaceholder | 8 | Navigation placeholder |
| FGKStaticData | 20 | Static data tables wrapper |
| FGKUE5Stubs | 17 | UE5 API stubs for UE4 compatibility |
| FGKUIToolkit | 38 | UI toolkit |

## Why

Return to Moria uses the FGK (Free-range Games Kit) framework, which caches DataTable contents at initialization and never refreshes. Runtime DataTable injection (via the [C++ mod](https://github.com/jbowensii/MoriaAdvancedBuilder)) can modify existing rows but cannot add new constructions to the build menu — the FGK cache blocks them.

**The solution:** Cooked paks load BEFORE FGK initialization. New DataTable rows baked into a pak are naturally included in the cache. This is already proven by existing Moria mods (Secrets of Khazad-dum, TobiModsAddons).

## What This Enables

| Capability | How |
|-----------|-----|
| New constructions in the build menu | DataTable rows in cooked pak, loaded before FGK cache |
| New items, weapons, tools | DataTable rows with asset references |
| Custom building piece meshes | Import/create in editor, cook |
| Biome customization | Modify FZoneDefinition, UBiomeDecoConfig, lighting configs |
| Unique room fixes | Override .umap sublevel files to remove misplaced objects |
| Custom UI widgets | Create Widget Blueprints in the UMG visual designer |
| New Blueprint actors | Full Blueprint creation referencing game classes |

## Reproducing Phase 2

If you need to regenerate the project from scratch (e.g., after a game update changes headers):

1. **Run UE4GameProjectGenerator** against fresh UHT header dumps (see `docs/Moria Replication Plan`)
2. **Follow `scripts/phase2_fix_compilation.md`** — documents every fix applied:
   - Remove 35+ engine plugin modules from Source compilation
   - Create ~21 GAS header redirects for Moria's custom engine fork
   - Create stub classes for missing UE4.27 types (ACullVolume, ANavMeshLockVolume, etc.)
   - Fix TEnumAsByte mismatches, abstract class instantiation, constructor patterns
   - Reparent classes with unexported symbols (UModelComponent, UEnvQueryTest_Distance)
   - Fix GC crash from unsafe SetupAttachment calls in generated constructors
3. **Verify**: `MoriaEditor Win64 Development` builds with 0 errors

## Documentation

- **[Replication Plan](docs/Moria%20Replication%20Plan%20-%20Editor%20Project%20Reconstruction.md)** — 7-phase step-by-step plan with commands, milestones, and risk assessment
- **[Phase 2 Fix Guide](scripts/phase2_fix_compilation.md)** — Every compilation fix documented for reproducibility
- **[Enhancement Research](docs/Future%20Research%20-%20Build%20Menu%20Injection%20and%20New%20Capabilities.md)** — GAS manipulation, Blueprint injection, weather/spawn control research

## Companion Project

The runtime C++ mod (UE4SS): **[MoriaAdvancedBuilder](https://github.com/jbowensii/MoriaAdvancedBuilder)** (v6.3.9)

The two projects work together:
- **This project**: Persistent content cooked into IoStore paks
- **MoriaAdvancedBuilder**: Runtime behavior via UE4SS DLL injection

## Tools Directory (Not Tracked)

The `tools/` directory is gitignored. Install these locally:

| Tool | Version | Install Method | Purpose |
|------|---------|---------------|---------|
| **FModel** | Latest | Download from [fmodel.app](https://fmodel.app) → `tools/FModel/` | Extract game assets |
| **retoc** | Latest | `cargo install retoc --root tools/retoc` | IoStore conversion |
| **UE4GameProjectGenerator** | Latest | `git clone` → `tools/UE4GameProjectGenerator` | Generate template from UHT dumps |
| **JsonAsAsset** | UE4.27.2 | [Releases](https://github.com/JsonAsAsset/JsonAsAsset/releases) → `tools/JsonAsAsset/` | Import JSON into editor |
| **JsonAsAsset Cloud Server** | Latest | [Core releases](https://github.com/Tectors/Core/releases) → `tools/JsonAsAssetServer/` | Auto-resolve dependencies |

## Reference

- **Engine**: Unreal Engine 4.27
- **Game**: The Lord of the Rings: Return to Moria (Free Range Games / North Beach Games)
- **Closest reference**: [DRG FSD-Template](https://github.com/DRG-Modding/FSD-Template) (same UE4.27)
- **Key guides**: [Buckminsterfullerene Modding Guide](https://buckminsterfullerene02.github.io/dev-guide/), [Dmgvol UE Modding](https://github.com/Dmgvol/UE_Modding)

## License

MIT
