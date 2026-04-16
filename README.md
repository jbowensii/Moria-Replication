# Moria Replication — UE4.27 Editor Project Reconstruction

Reconstruct a baseline Unreal Engine 4.27 editor project from **The Lord of the Rings: Return to Moria** shipped game content, enabling full-spectrum modding: new building pieces, DataTable modifications, biome customization, unique room fixes, and custom Blueprints — all cooked and packed as IoStore mod paks.

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

## Documentation

- **[Replication Plan](docs/Moria%20Replication%20Plan%20-%20Editor%20Project%20Reconstruction.md)** — 7-phase step-by-step plan with copy-paste commands, milestones, and risk assessment
- **[Enhancement Research](docs/Future%20Research%20-%20Build%20Menu%20Injection%20and%20New%20Capabilities.md)** — Deep dives into GAS manipulation, 3dmigoto, Blueprint injection, weather/spawn control, menu/controller access

## Companion Project

The runtime C++ mod (UE4SS): **[MoriaAdvancedBuilder](https://github.com/jbowensii/MoriaAdvancedBuilder)** (v6.3.9)

The two projects work together:
- **This project**: Persistent content cooked into IoStore paks
- **MoriaAdvancedBuilder**: Runtime behavior via UE4SS DLL injection

## Reference

- **Engine**: Unreal Engine 4.27
- **Closest reference**: [DRG FSD-Template](https://github.com/DRG-Modding/FSD-Template) (same UE4.27 engine)
- **Key tools**: [FModel](https://fmodel.app), [retoc](https://github.com/trumank/retoc), [JsonAsAsset](https://github.com/JsonAsAsset/JsonAsAsset), [UE4GameProjectGenerator](https://github.com/Buckminsterfullerene02/UE4GameProjectGenerator)

## Tools Directory (Not Tracked)

The `tools/` directory is gitignored and contains third-party tools needed for the modding pipeline. To replicate this setup, install the following:

| Tool | Version | Install Method | Purpose |
|------|---------|---------------|---------|
| **FModel** | Latest | Download from [fmodel.app](https://fmodel.app) → extract to `tools/FModel/` | Extract game assets from IoStore paks |
| **retoc** | Latest | `cargo install retoc --root tools/retoc` | Convert between legacy .pak and IoStore (.pak/.ucas/.utoc) |
| **UE4GameProjectGenerator** | Latest | `git clone https://github.com/Buckminsterfullerene02/UE4GameProjectGenerator tools/UE4GameProjectGenerator` | Generate UE4 template project from UHT header dumps |
| **JsonAsAsset** | UE4.27.2 | Download from [JsonAsAsset releases](https://github.com/JsonAsAsset/JsonAsAsset/releases) → extract to `tools/JsonAsAsset/` | Import FModel JSON exports into UE4 editor |
| **JsonAsAsset Cloud Server** | Latest | Download from [Tectors/Core releases](https://github.com/Tectors/Core/releases) → extract to `tools/JsonAsAssetServer/` | Auto-resolve asset dependencies during import (requires ASP.NET 8.0+) |

### Prerequisites

- **Rust/Cargo** (for retoc): [rustup.rs](https://rustup.rs)
- **UE4.27 Editor**: Required for UE4GameProjectGenerator and JsonAsAsset
- **ASP.NET Runtime 8.0+**: Required for JsonAsAsset Cloud Server
- **Git**: Required for cloning UE4GameProjectGenerator

## License

MIT
