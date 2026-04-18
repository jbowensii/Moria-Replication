# Moria Replication

## What Is This?

**The Lord of the Rings: Return to Moria** is a survival and building game set inside the Mines of Moria. Players explore procedurally generated caves, gather resources, build structures, and fight orcs and trolls while reclaiming the lost Dwarven kingdom.

This project takes the shipped game and works backward to recreate a working copy of the game's development environment. Think of it like taking a finished book and reconstructing the author's notebook — not to copy the book, but to write new chapters that fit seamlessly into the story.

**Why does this matter?** The game's modding scene is limited because of how the game loads its data. The game reads all its configuration files (what items exist, what can be built, what enemies do) at startup and locks them into memory. Mods that try to add new content *after* the game starts are blocked by this lock. But if new content is packaged the same way the original game content is packaged, it gets loaded *before* the lock happens, and the game treats it as if it was always there.

This project builds the tools and environment needed to create those properly packaged mods — new building pieces in the build menu, new items, new weapons, custom rooms, and more.

## Project Status — v0.2.0

### What's Done

| Phase | Status | Description |
|-------|--------|-------------|
| 1. Tool Setup & Extraction | Done | FModel, retoc, KismetKompiler installed; 56,797 game assets extracted |
| 2. Editor Project Generation | Done | UE4.27 project compiles cleanly, editor opens successfully |
| 3. Asset Import | Done | 26,139 assets imported into the editor project (see breakdown below) |
| 4. Blueprint Decompilation | Done | 4,406 Blueprints decompiled to readable pseudocode |
| 5. Level Reconstruction | Done | 86 room layouts reconstructed from game data (292,543 actors total) |

### What's Not Done

| Item | Status | Notes |
|------|--------|-------|
| Materials / Textures on meshes | Not working | Materials were imported but parent shaders can't compile in the editor — meshes show as gray/white |
| Procedural cave geometry | Not possible | Cave walls and ceilings are generated at runtime by the game engine, not stored as files |
| Blueprint functionality | View only | Blueprints are decompiled to pseudocode for reading, but can't be edited or run in the editor |
| Level testing (play in editor) | Not working | No player character, no game mode — levels are view-only in the editor viewport |
| Cook and package mods | Not tested | The editor compiles but cooking to IoStore paks has not been attempted yet |
| 7 bow/crossbow animations | Skipped | Extra bones not present in the base skeleton (see Known Issues) |
| 12 Troll AnimMontages | Skipped | JsonAsAsset can't resolve skeleton references with `.6` object indices |

### Asset Import Breakdown

| Asset Type | Count | Method |
|-----------|-------|--------|
| Textures | 2,806 | JsonAsAsset + Cloud Server |
| Materials & Material Instances | ~3,000+ | JsonAsAsset + Cloud Server |
| Data Tables, Curves, Sound Data | ~5,500+ | JsonAsAsset + Cloud Server |
| Static Meshes | 2,027 | UModel FBX export + UE4 import script |
| Skeletal Meshes + Destructible Meshes | 1,322 | Copied from cooked game files |
| Animations (FBX) | 4,018 | Blender PSA-to-FBX conversion + UE4 import script |
| Animations (cooked) | 4 | Troll AnimSequences copied from cooked files |
| Blueprints (cooked, view-only) | 4,406 | retoc IoStore-to-legacy conversion |
| Level maps (.umap) | ~200+ | retoc IoStore-to-legacy conversion |
| **Total** | **26,139** | |

## Quick Start

### Prerequisites
- **UE4.27 Editor** installed at `C:\Program Files\Epic Games\UE_4.27\`
- **Visual Studio 2022** with C++ game development workload
- **Python 3.10+** for running scripts
- **Blender 3.x+** for mesh and animation conversion scripts
- **Windows 10/11 x64**

### Open the Editor
1. Double-click `scripts/Moria Editor.lnk` (or copy to your Desktop)
2. If prompted "Missing modules -- rebuild?", click **Yes**
3. If prompted about new plugins, click **Dismiss**
4. Expected warning: `DefaultMediaTexture` missing -- harmless

### Build from Command Line
```batch
"C:\Program Files\Epic Games\UE_4.27\Engine\Binaries\DotNET\UnrealBuildTool.exe" ^
  MoriaEditor Win64 Development ^
  -Project="<repo>\project\Moria.uproject"
```

## Scripts Guide

All scripts live in the `scripts/` folder and are run from a terminal. Most have a `--run` flag — without it, they do a dry run so you can see what would happen before committing.

### Phase 1 — Extraction

| Script | What It Does | When To Use |
|--------|-------------|-------------|
| `extract_game_assets.py` | Extracts raw .uasset files from the game's pak archives | Once, at the start of the project or after a game update |

### Phase 3 — Asset Import

These scripts import extracted game assets into the UE4.27 editor project.

| Script | What It Does | When To Use |
|--------|-------------|-------------|
| `batch_import.py` | Runs the JsonAsAsset plugin in batch mode to import textures, materials, data tables, curves, and other JSON-exportable assets | After extracting assets and setting up the Cloud Server |
| `bulk_fetch_cloud.py` | Fetches asset metadata from the JsonAsAsset Cloud Server | Before batch_import, to prepare the dependency list |
| `run_cloud_metadata_pass.py` | Runs a metadata-only pass through the Cloud Server | To gather asset info without importing |
| `run_tier12_import.py` | Imports tier 1-2 assets (textures, simple materials) | First import pass |
| `run_tier4_import.py` | Imports tier 4 assets (complex materials, montages) | After tier 1-2 is done |
| `prep_batch_tiers.py` | Sorts assets into import tiers by dependency order | Before running tiered imports |
| `prep_tier4_montage_batch.py` | Prepares AnimMontage batch for tier 4 import | Before tier 4 import |
| `phase3_import.py` | Earlier version of the import pipeline | Superseded by batch_import.py |
| `export_textures.py` | Exports texture assets for import preparation | Before texture import |
| `ue4_texture_import.py` | Imports textures into the UE4 project via commandlet | After export_textures.py |

### Mesh & Animation Import

| Script | What It Does | When To Use |
|--------|-------------|-------------|
| `gen_mesh_list.py` | Builds a list of all meshes to import | Before mesh import |
| `gen_fbx_manifest.py` | Generates the FBX import manifest | Before mesh import |
| `mesh_import.py` | Imports static meshes into UE4 from FBX files | After FBX conversion |
| `ue4_fbx_import.py` | UE4 commandlet wrapper for FBX mesh import | Called by mesh_import.py |
| `build_anim_fbx_manifest.py` | Builds the animation FBX manifest | Before animation import |
| `ue4_anim_fbx_import.py` | Imports animation FBX files into UE4 | After Blender conversion |
| `ue4_fix_bow_anims.py` | Attempts to fix the 7 failed bow animations | After animation import (currently fails) |
| `blender_psk_to_fbx.py` | Converts a single PSK mesh to FBX using Blender | Mesh conversion |
| `blender_batch_psk_to_fbx.py` | Batch converts all PSK meshes to FBX | Before mesh import |
| `blender_gltf_to_fbx.py` | Converts a single glTF mesh to FBX using Blender | Mesh conversion |
| `blender_batch_gltf_to_fbx.py` | Batch converts all glTF meshes to FBX | Before mesh import |
| `blender_psa_to_fbx.py` | Converts PSA animation files to FBX using Blender | Animation conversion |

### Blueprint & Level Data

| Script | What It Does | When To Use |
|--------|-------------|-------------|
| `batch_decompile_blueprints.py` | Converts Blueprints from IoStore to legacy format, then decompiles to .kms pseudocode | After extraction, to read Blueprint logic |
| `copy_legacy_blueprints_to_project.py` | Copies legacy-format Blueprint .uasset/.uexp into the editor project | After decompilation, to browse BPs in the editor |
| `copy_legacy_umaps_to_project.py` | Copies legacy-format .umap level files into the editor project | To load game levels in the editor |
| `reconstruct_level.py` | Reads BubbleData JSON and generates a UE4 Python script that rebuilds a room's layout | To reconstruct game rooms in the editor |
| `gap_analysis.py` | Compares extracted assets against imported assets to find what's missing | Anytime, to check import coverage |

### Generated Level Scripts

The `scripts/reconstructed/` folder contains **86 generated Python scripts**, one per game room ("bubble"). These are meant to be run inside the UE4 editor via **Edit > Execute Python Script**. Each one places all the static meshes, construction blocks, and breakable objects for that room.

Examples:
- `reconstruct_BD_BB_Chapter4_DurinsForge.py` — Durin's Forge (the large forge area)
- `reconstruct_BD_BB_Passage_CrampedRavine.py` — A small connecting passage (good for testing)
- `reconstruct_BD_BB_Chapter5_MithrilDeep.py` — The Mithril Deep mines

**Note:** These scripts place geometry only. Materials appear as gray/white because the parent shaders can't compile in the editor. Cave walls and procedural terrain are not included — those are generated at runtime by the game.

## Repository Structure

```
Moria-Replication/
  project/                         UE4.27 editor project (the main deliverable)
    Moria.uproject                 Project file (9 game modules, 16 plugins)
    Source/                        8,700+ source files across 30 module directories
    Content/                       26,139 imported assets
    Config/                        Editor-generated config files
  scripts/                         All automation scripts (see Scripts Guide above)
    reconstructed/                 86 generated room reconstruction scripts
    phase2_fix_compilation.md      Step-by-step guide to reproduce Phase 2
    Moria Editor.lnk               Desktop shortcut for the editor
  decompiled/                      4,406 decompiled Blueprint .kms files
  docs/                            Design documents and research
  tools/                           Third-party tools (gitignored, install locally)
  CLAUDE.md                        AI assistant context
  README.md                        This file
```

### Compiled Modules (9 game modules)

| Module | Files | Description |
|--------|-------|-------------|
| Moria | 5,114 | Main game module -- characters, building, inventory, AI, world |
| FGK | 1,713 | Free-range Games Kit framework |
| FGKAnalytics | 8 | Analytics integration |
| FGKDebugMenu | 16 | Debug menu system |
| FGKLoadingScreen | 6 | Loading screen |
| FGKNavPowerPlaceholder | 8 | Navigation placeholder |
| FGKStaticData | 20 | Static data tables wrapper |
| FGKUE5Stubs | 17 | UE5 API stubs for UE4 compatibility |
| FGKUIToolkit | 38 | UI toolkit |

## Why This Project Exists

Return to Moria uses the FGK (Free-range Games Kit) framework, which reads all game data tables at startup and locks them into a cache. Runtime mods (like the companion [MoriaAdvancedBuilder](https://github.com/jbowensii/MoriaAdvancedBuilder)) can modify existing data but cannot add entirely new items to the build menu — the cache blocks them.

**The solution:** If new content is packaged the same way the game packages its own content (as cooked IoStore pak files), it gets loaded before the cache locks. The game treats it as original content. This is already proven by existing Moria mods (Secrets of Khazad-dum, TobiModsAddons).

This project builds the editor environment needed to create, cook, and package that content.

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

## Known Issues

- **Materials are non-functional** — Material Instances were imported with correct parameters and texture references, but the parent master materials (shader graphs) can't be reconstructed from cooked data. All meshes render as gray/white in the editor.
- **7 bow/crossbow animations failed to import** — Extra prop bones (bow mesh bone) not present in the base Dwarf skeleton. Affects: Dwa_Bow_Combat_Aim_Fire_Bow, Dwa_Bow_Combat_Aim_Loop_Bow, Dwa_Bow_Combat_HipAim_Fire_Bow, Dwa_Bow_Draw_Aim_Bow, Dwa_Bow_Draw_HipAim_Bow, Dwa_Xbow_Combat_Atk_Fire_BOW, Dwa_Xbow_Combat_Atk_Reload_Bow.
- **12 Troll AnimMontages skipped** — JsonAsAsset can't resolve skeleton references with `.6` object indices (all reference `Troll_Parent_Skeleton.6`).
- **Lightmap UV overlaps** — Imported meshes have overlapping lightmap UVs, causing baked lighting to fail. Use movable (dynamic) lights instead.
- **OneDrive performance** — Never use `os.walk` on the project directory; use PowerShell `Get-ChildItem` instead (minutes vs seconds).

## Reproducing From Scratch

If you need to regenerate the project (e.g., after a game update):

1. **Phase 1:** Run `extract_game_assets.py` to extract game paks
2. **Phase 2:** Run UE4GameProjectGenerator against UHT header dumps, then follow `scripts/phase2_fix_compilation.md` for all compilation fixes
3. **Phase 3:** Run the import pipeline (`batch_import.py` with Cloud Server running, then mesh and animation scripts)
4. **Blueprints:** Run `batch_decompile_blueprints.py`, then `copy_legacy_blueprints_to_project.py`
5. **Levels:** Run `copy_legacy_umaps_to_project.py`, then use `reconstruct_level.py` to generate room scripts

Detailed steps are in `scripts/phase2_fix_compilation.md` and `docs/Moria Replication Plan`.

## Companion Project

The runtime C++ mod (UE4SS): **[MoriaAdvancedBuilder](https://github.com/jbowensii/MoriaAdvancedBuilder)**

The two projects work together:
- **This project**: Persistent content cooked into IoStore paks (loaded at startup)
- **MoriaAdvancedBuilder**: Runtime behavior via UE4SS DLL injection (runs while game is playing)

## Tools Directory (Not Tracked)

The `tools/` directory is gitignored. Install these locally:

| Tool | Purpose |
|------|---------|
| **FModel** | Extract and export game assets to JSON |
| **retoc** | Convert IoStore format to legacy .uasset/.uexp |
| **KismetKompiler** | Decompile Blueprint bytecode to readable pseudocode |
| **UE4GameProjectGenerator** | Generate editor project from UHT header dumps |
| **JsonAsAsset** (UE4.27 plugin) | Import JSON-exported assets into the editor |
| **JsonAsAsset Cloud Server** | Auto-resolve asset dependencies during import |
| **UModel** | Export meshes and animations from cooked assets |
| **Blender 3.x+** | Convert PSK/PSA/glTF to FBX for UE4 import |
| **Stove** (patched) | Edit .umap level files outside the editor |

## Reference

- **Engine**: Unreal Engine 4.27
- **Game**: The Lord of the Rings: Return to Moria (Free Range Games / North Beach Games)
- **Closest reference**: [DRG FSD-Template](https://github.com/DRG-Modding/FSD-Template) (same UE4.27 approach)
- **Key guides**: [Buckminsterfullerene Modding Guide](https://buckminsterfullerene02.github.io/dev-guide/), [Dmgvol UE Modding](https://github.com/Dmgvol/UE_Modding)

## License

MIT
