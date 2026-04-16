# Moria Replication Plan — Editor Project Reconstruction

**Goal:** Create a baseline UE4.27 editor project reconstructed from Return to Moria's shipped game content. This project serves as the foundation for creating new constructions, items, Blueprints, meshes, textures, and modifying existing game data — all cooked and packed as IoStore mod paks. Combined with the existing UE4SS C++ mod, this unlocks the full modding surface.

**Author:** Mereak Firmaxe  
**Date:** April 2026  
**Last Updated:** April 16, 2026  
**Game:** The Lord of the Rings: Return to Moria (UE4.27, IoStore packaging)  
**Reference:** Deep Rock Galactic FSD-Template (same engine version, proven pattern)

---

## Use Cases This Enables

1. **Build menu injection** — Add new construction recipes that appear in the build menu (solves the FGK cache problem)
2. **Unique room fixes** — Remove misplaced unbreakable rocks/dirt piles from hand-crafted landmark rooms via cooked level overrides
3. **Biome customization** — Change decoration density, ore types, enemy spawns, lighting per biome via DataTable modifications
4. **New building pieces** — Custom meshes, textures, materials cooked and deployed
5. **New items/weapons/tools** — DataTable rows with proper asset references
6. **Widget Blueprints** — Custom UI screens created in the UMG visual designer

---

## Current State Assessment

### What We Have
| Resource | Location | Status |
|----------|----------|--------|
| UE4.27 Editor | `C:\Program Files\Epic Games\UE_4.27\` | Installed — UE4Editor.exe + UE4Editor-Cmd.exe present |
| UE4.27 Engine Source | `UE_4.27\Engine\Source\` | Full source available |
| Game Paks (IoStore) | `ReturnToMoria\Moria\Content\Paks\` | Main pak 15.6 GB .ucas + global + DLC |
| UHT Header Dump | `<workspace>/dumps/UHTHeaderDump/` | 151 modules, 8,881 .h files |
| CXX Header Dump | `<workspace>/dumps/CXXHeaderDump/` | 3,028 .hpp files |
| Rust Toolchain | `C:\Users\johnb\.cargo\` | Cargo 1.93.1 |
| Python | System PATH | 3.14.2 with pip |
| Proof it works | `Content/Paks/Secrets of Khazad-dum/` | TobiModsAddons already uses cooked paks |

### What We Need to Install
| Tool | Purpose | Install Method |
|------|---------|----------------|
| FModel | Extract game assets from paks | Download from fmodel.app |
| retoc | Convert between legacy and IoStore | `cargo install retoc` |
| UE4GameProjectGenerator | Generate template project from UHT dumps | Clone github.com/Buckminsterfullerene02/UE4GameProjectGenerator, compile as UE4 commandlet |
| JsonAsAsset | Import FModel JSON into editor | Clone github.com/JsonAsAsset/JsonAsAsset, install as editor plugin |
| JsonAsAsset Cloud Server | Auto-resolve dependencies during import | Download from JsonAsAsset releases (requires ASP.NET 8.0) |
| Blender (optional) | Convert PSK meshes to FBX | Download from blender.org |

---

## Phase 1: Tool Installation and Game Extraction (Day 1)

### Step 1.1: Install FModel

1. Download FModel from https://fmodel.app (Windows x64)
2. Install/extract to `C:\Users\johnb\Tools\FModel\`
3. Launch FModel
4. First-time setup:
   - If Return to Moria is not auto-detected: click the expand arrow → **Add Undetected Game**
   - Game name: `ReturnToMoria`
   - Game directory: `C:\Program Files\Epic Games\ReturnToMoria\`
5. Settings → General:
   - **UE Versions**: Set to `GAME_UE4_27` (critical — wrong version = archive errors)
   - **Output Directory**: `C:\Users\johnb\OneDrive\Documents\Projects\UE4SS Testing\fmodel-export\`
   - **Keep Directory Structure**: ENABLED
6. **Loading Archives**:
   - Archives panel → set Loading Mode to **All** → click **Load**
   - Wait for the full directory tree to populate
   - Verify: you can browse `Moria/Content/` and see assets

If paks appear greyed out with red icons, you need an AES encryption key. Check https://github.com/FModel/Unreal-Game-Keys or the Moria modding community.

### Step 1.2: Extract Project Metadata

In FModel, locate and export (right-click → **Export Raw Data**):

1. **The .uproject file** — search the root of the content tree for `Moria.uproject` or similar
2. **The .upluginmanifest file** — search for `.upluginmanifest`
3. **Any .uplugin files** for game-specific plugins (FGK, Moria plugins)

Save these to `<workspace>/fmodel-export/metadata/`

If the .uproject is not found in paks (some games don't include it), create one manually based on the DRG FSD-Template structure:

```json
{
    "FileVersion": 3,
    "EngineAssociation": "4.27",
    "Category": "",
    "Description": "",
    "Modules": [
        {
            "Name": "Moria",
            "Type": "Runtime",
            "LoadingPhase": "Default"
        }
    ]
}
```

### Step 1.3: Extract Key Game Assets

**Priority 1 — All DataTables:**
1. In FModel, press Ctrl+Shift+F to search
2. Search for `DT_` 
3. Select all DataTable assets
4. Right-click → **Save Properties (.json)**
5. Critical tables to verify export:
   - `DT_Constructions`, `DT_ConstructionRecipes` (build menu — the main prize)
   - `DT_Items`, `DT_Weapons`, `DT_Tools`, `DT_Armor`, `DT_Consumables`, `DT_Ores`, `DT_ContainerItems`
   - `DT_Storage`, `DT_SettlementLevelData`, `DT_WorldLevelData`
   - Zone/biome tables: `DT_Zone*`, `DT_Biome*` (if they exist as separate assets)

**Priority 2 — Unique Room / Landmark Assets:**
1. Search for `Landmark`, `Nexus`, `Boss`, or specific room names you recognize
2. These may be `.umap` sublevel files or Blueprint actors
3. Right-click → **Export Raw Data** (gets the cooked .uasset/.uexp)
4. Also **Save Properties (.json)** for reference

**Priority 3 — Bubble/Biome Definitions:**
1. Search for `BubbleDefinition`, `BubbleCatalog`, `BiomeDefinition`
2. Search for `DecoConfig`, `RockConfig`, `AtmosphericsConfig`
3. Export as JSON — these control what spawns in each room type

**Priority 4 — Enums, Structs, DataAssets:**
1. Search for enum and struct assets
2. Export as JSON — needed for DataTable row type definitions

**Priority 5 — Textures and Icons:**
1. Search for `T_Icon_*`, `T_UI_*`
2. Right-click → **Save Texture** (exports as PNG)

**Priority 6 — Static Meshes (for new building pieces):**
1. Search for `SM_*` — building piece meshes
2. Right-click → **Save Model** (exports as PSK)
3. Will need Blender to convert PSK → FBX for editor import

### Step 1.4: Install retoc

```bash
# Option A: Pre-built installer (recommended)
powershell -ExecutionPolicy Bypass -c "irm https://github.com/trumank/retoc/releases/download/v0.1.5/retoc_cli-installer.ps1 | iex"

# Option B: Build from source
cargo install --git https://github.com/trumank/retoc
```

Verify: `retoc --help`

### Step 1.5: Study Existing Mod Pak Structure

Before building our own, study how TobiModsAddons works:

```bash
retoc to-legacy "C:\Program Files\Epic Games\ReturnToMoria\Moria\Content\Paks\Secrets of Khazad-dum\TobiModsAddons_P.utoc" --output ./tobi-extracted/
```

Examine:
- What folder structure does the extracted content follow? (should mirror `Moria/Content/...`)
- What asset types are included?
- How is the stub `.pak` structured?
- Document findings — this is our blueprint for packaging

### Step 1.6: Study Unique Room Assets

For the specific use case of removing misplaced objects from hand-crafted rooms:

1. In FModel, search for landmark/unique room assets
2. Double-click to view properties — look for `StaticMeshComponent` entries, actor references
3. Note the asset paths of rooms with problematic objects
4. Export these as raw .uasset/.uexp for later modification

**Key insight:** The unique/landmark rooms are **.umap sublevel files** — the user has already identified their locations in the game paks. These are streamed levels with explicitly placed actors (rocks, dirt piles, furniture, etc.). The editing approach is:

1. Extract the .umap + companion .uexp via FModel or retoc
2. Edit with UAssetGUI (binary level editing — find actor entries by class/name, delete or modify)
3. Or: import into editor project if the template supports sublevel loading
4. Pack the modified .umap into a `_P.pak` that overrides the original
5. The game loads YOUR version of the room — offending objects are permanently gone

---

## Phase 2: Generate the Template Project (Day 1-2)

### Step 2.1: Clone UE4GameProjectGenerator

```bash
cd "C:\Users\johnb\OneDrive\Documents\Projects\"
git clone https://github.com/Buckminsterfullerene02/UE4GameProjectGenerator.git
```

Use Buckminsterfullerene's fork (recommended over Archengius's original — has more fixes).

### Step 2.2: Set Up the Generator Project

1. Open `GameProjectGenerator.uproject` in UE4.27 Editor
2. Open the extracted `.upluginmanifest` from Phase 1
3. Add every engine plugin the game uses to the generator's `.uproject`
4. Exclude any licensed plugins you can't redistribute
5. Build the project (Development Editor | Win64)

**Alternative (if the commandlet approach is complex):** Create the project manually:
1. In UE4.27: File → New Project → C++ → Basic Code → name it `Moria` (must match game's internal project name)
2. Create modules matching the game's structure: `Moria`, `FGK`, `FGKStaticData`, `FGKUIToolkit`, etc.
3. Copy UHT headers into each module's `Source/<Module>/Public/` directory
4. Set up `.Build.cs` files with correct PublicDependencyModuleNames

### Step 2.3: Run the Commandlet

```batch
"C:\Program Files\Epic Games\UE_4.27\Engine\Binaries\Win64\UE4Editor-Cmd.exe" ^
  "C:\Users\johnb\OneDrive\Documents\Projects\UE4GameProjectGenerator\GameProjectGenerator.uproject" ^
  -run=ProjectGenerator ^
  -HeaderRoot="C:\Users\johnb\OneDrive\Documents\Projects\UE4SS Testing\dumps\UHTHeaderDump" ^
  -ProjectFile="C:\Users\johnb\OneDrive\Documents\Projects\UE4SS Testing\fmodel-export\metadata\Moria.uproject" ^
  -OutputDir="C:\Users\johnb\OneDrive\Documents\Projects\MoriaModKit" ^
  -stdout -unattended -NoLogTimes
```

### Step 2.4: Fix Compilation Errors

Expect 50-200+ errors on first try. Fix in this order:

**Round 1 — Missing includes and modules:**
| Error | Fix |
|-------|-----|
| `#include "X.h" not found` | Add `#include "CoreMinimal.h"` at top of header |
| `LNK2001 unresolved external` | Add missing module to `.Build.cs` PublicDependencyModuleNames |
| `undefined type` | Add forward declaration or include the module |

**Round 2 — Type and signature issues:**
| Error | Fix |
|-------|-----|
| Pure virtual without implementation | Add empty body: `{ return {}; }` or `{ }` |
| Delegate signature mismatch | Comment out or add `DECLARE_DYNAMIC_MULTICAST_DELEGATE(Name);` |
| `const` conversion error (C2664) | Remove `const` from function argument |
| Constructor mismatch | Change to: `ClassName(const FObjectInitializer& ObjectInitializer);` |
| Enum missing zero value | Add `None = 0` as first entry |
| Bitfield size mismatch | Change `uint8` to `uint32` (check CXX dump for correct size) |

**Round 3 — Blueprint/property metadata:**
| Error | Fix |
|-------|-----|
| `BlueprintReadWrite` on incompatible type | Remove the specifier |
| `SoftObjectProperty` not found (pre-4.17) | Replace with `AssetObjectProperty` |
| Circular dependency | Add forward declarations, reorder includes |

**Key principle:** None of these functions need to WORK. They only need to COMPILE so the editor can create assets referencing these types. Every function body can be `{ return {}; }`.

### Step 2.5: Create Game Target Files

1. Find `MoriaEditor.Target.cs` in the generated output
2. Duplicate it to `Moria.Target.cs`
3. Remove all "Editor" references inside the file
4. Both files must exist for the project to compile

### Step 2.6: Verify Compilation

```batch
"C:\Program Files\Epic Games\UE_4.27\Engine\Binaries\Win64\UE4Editor-Cmd.exe" ^
  "C:\Users\johnb\OneDrive\Documents\Projects\MoriaModKit\Moria.uproject" ^
  -build
```

Or open in Visual Studio: Build → Build Solution (Development Editor | Win64).

**Success criteria:** Zero errors. The editor opens and shows the Content Browser.

---

## Phase 3: Asset Population (Day 2-4)

### Step 3.1: Install JsonAsAsset Plugin

1. Download the UE4.27.2 release from https://github.com/JsonAsAsset/JsonAsAsset/releases
2. Extract to `MoriaModKit/Plugins/JsonAsAsset/`
3. Rebuild the project
4. Verify: JsonAsAsset toolbar button appears in editor

### Step 3.2: Configure Cloud Server (Auto-Dependency Resolution)

1. Download the Cloud Server (Core releases) from JsonAsAsset releases
2. Install ASP.NET 8.0 runtime if not present
3. Launch the Cloud Server application
4. Configure it to point at Moria's paks:
   - Paks Directory: `C:\Program Files\Epic Games\ReturnToMoria\Moria\Content\Paks\`
   - UE Version: 4.27
5. Wait until console shows `[CORE] Running API`
6. In UE4 Editor: JsonAsAsset dropdown → Open Plugin Settings
7. Enable **"Cloud"** and point to `http://localhost:<port>`
8. Enable **"Save Assets"** and **"Disconnect Root"** (prevents assertion errors)
9. Test: import a single DataTable JSON and verify it appears in Content Browser with correct data

### Step 3.3: Import DataTables (Critical)

1. JsonAsAsset toolbar → Import
2. Navigate to the FModel JSON export directory
3. Select all `DT_*.json` files
4. Import — each creates a UDataTable in the Content Browser

**Verify these critical tables:**
- Open `DT_Constructions` — confirm building definitions have rows
- Open `DT_ConstructionRecipes` — confirm recipes are populated
- Open `DT_Items`, `DT_Weapons`, etc. — confirm item data is present

**If import fails** with "row struct not found": The C++ stub for that struct type is missing or incorrectly defined. Check the UHT headers and fix the struct definition.

### Step 3.4: Import Biome and Zone Definitions

Import these configuration assets:
- `FBiomeDefinition` DataTable rows (biome audio, deco, rock, atmospherics configs)
- `FZoneDefinition` DataTable rows (temperature, resources, enemy populations, lighting)
- `UMorBubbleDefinition` data assets (per-room-type templates)
- `UBiomeDecoConfig`, `UBiomeRockConfig`, `UBiomeAtmosphericsConfig` data assets

These control what spawns in each room type and biome.

### Step 3.5: Import Materials and Textures

1. JsonAsAsset imports `MaterialInstanceConstant` assets (parameter values only — node graphs are stripped)
2. Import textures as PNG → UTexture2D via standard editor drag-and-drop import
3. Focus on building piece textures and icon textures first

**Material limitation:** Full material node graphs are stripped during cooking. You get parameter values (scalar, vector, texture references) but not the shader graph. New materials must be created from scratch or by copying/modifying existing MaterialInstanceConstants.

### Step 3.6: Import Landmark/Unique Room Assets

For rooms you want to modify (remove misplaced objects):

1. The exported `.uasset`/`.uexp` files from Phase 1.6 can be placed directly in the project's Content folder at the matching path
2. If they're Blueprint actors: the editor will show their component hierarchy (meshes, colliders, etc.) in the Details panel — though not the node graph logic
3. If they're sublevel `.umap` files: these are harder to edit in the editor but CAN be modified with UAssetGUI (binary editing)

### Step 3.7: Create Dummy Assets

For every game asset your mod content REFERENCES but does NOT modify:

1. Create folder: `Content/Dummies/` 
2. For each referenced Blueprint:
   - Create a new Blueprint at the same content path as the game version
   - Set parent class to match (e.g., `AMorConstructionActor`)
   - Leave empty — no logic, no components
3. For each referenced mesh/texture: create a placeholder at the matching path

**CRITICAL:** Add `Dummies/` to Project Settings → Packaging → **Directories to Never Cook**. Including dummies in your pak would override the real game assets.

---

## Phase 4: Modify Content (Ongoing)

### Step 4.1: Validation Test — Simple DataTable Change

Before anything ambitious, verify the pipeline works end-to-end:

1. Open `DT_Items` → find `Coal` row → change `MaxStackSize` to 999
2. Save
3. Proceed to Phase 5 (Cook, Package, Deploy)
4. Launch game → verify Coal stacks to 999

If this works, the entire pipeline is validated.

### Step 4.2: The Big Test — New Build Menu Entry

This is the test that proves the FGK cache problem is solved:

1. Open `DT_ConstructionRecipes`
2. Duplicate an existing row (e.g., copy `TimberWall` to `TimberWall_Custom`)
3. Modify display name and/or recipe requirements
4. Save → Cook → Deploy
5. Launch game → open build menu → **the new recipe should appear**

### Step 4.3: Fix Unique Room Objects

For removing misplaced rocks/dirt from hand-crafted landmark rooms:

**If the room is a Blueprint actor:**
1. Open the Blueprint in the editor
2. In the Components panel, find the offending StaticMeshComponent
3. Delete it or move it to a valid position
4. Save → Cook → Deploy as a `_P.pak` override

**If the room is a sublevel (.umap):**
1. Open the `.uasset` in UAssetGUI (binary editor)
2. Find the actor entry for the offending object by class name and position
3. Delete the entry or set its scale to (0,0,0)
4. Save → Pack with retoc → Deploy

**If the room's objects are defined in a UMorBubbleDefinition data asset:**
1. Open the bubble definition in the editor
2. Find the content proxy or decoration config entry for the offending object
3. Remove it from the array or set its weight to 0
4. Save → Cook → Deploy

### Step 4.4: Modify Biome Properties

Change what spawns in room types:

1. Open the `UBiomeDecoConfig` for the target biome
2. Remove unwanted mesh entries (e.g., giant mushrooms)
3. Add new mesh entries or change density weights
4. Modify `UBiomeRockConfig` to change rock formations
5. Modify `FZoneDefinition` rows for temperature, ore types, enemy spawns
6. Save → Cook → Deploy

### Step 4.5: Create New Building Pieces (Advanced)

1. Create or import a static mesh (FBX format)
2. Create a new Blueprint actor extending `AMorConstructionActor`
3. Add the mesh, collision, snap points as components
4. Add a row to `DT_Constructions` referencing the new actor
5. Add a row to `DT_ConstructionRecipes` with the recipe
6. Save → Cook → Deploy

### Step 4.6: Create New Widget Blueprints (Advanced)

1. Create a Widget Blueprint extending `UFGKUIScreen` (or a Moria subclass)
2. Design layout in UE4's UMG visual designer (full drag-and-drop UI editor)
3. Add buttons, text, images, scroll boxes — all in the visual editor
4. Cook → Deploy
5. The UE4SS C++ mod shows the widget via `UFGKUIManager::ShowScreen()`

---

## Phase 5: Cook, Package, and Deploy

### Step 5.1: Configure Cooking Settings

Editor → Edit → Project Settings → Packaging:

| Setting | Value | Why |
|---------|-------|-----|
| Use Io Store | ENABLED | Return to Moria uses IoStore |
| Directories to Never Cook | `Dummies/` | Prevents dummies from overriding real game assets |
| Generate Chunks | ENABLED | For selective asset packaging |
| Use Pak File | ON | Required for IoStore |

### Step 5.2: Assign Mod Content to Chunks

For each modified or new asset:
1. Select in Content Browser
2. Right-click → Asset Actions → Assign to Chunk
3. Set Chunk ID to **111** (or any unused ID)

**Bulk assignment:** Create a `PrimaryAssetLabel` data asset in your mod content folder:
- Priority: 1
- Chunk ID: 111
- Apply Recursively: enabled
- Label Assets in My Directory: enabled
- Cook Rule: Always Cook

### Step 5.3: Cook

**Option A — Editor:**
```
File → Cook Content for Windows
```

**Option B — Command line:**
```batch
"C:\Program Files\Epic Games\UE_4.27\Engine\Binaries\Win64\UE4Editor-Cmd.exe" ^
  "C:\Users\johnb\OneDrive\Documents\Projects\MoriaModKit\Moria.uproject" ^
  -run=Cook -TargetPlatform=WindowsNoEditor -unattended
```

Cooked output: `MoriaModKit\Saved\Cooked\WindowsNoEditor\Moria\Content\`

### Step 5.4: Package as IoStore

**Option A — Full editor packaging (simplest):**
```
File → Package Project → Windows (64-bit)
```
With "Use Io Store" enabled, this directly produces `.pak` + `.ucas` + `.utoc`.

**Option B — Manual with retoc (more control):**
1. Collect your cooked `.uasset`/`.uexp` files from `Saved/Cooked/`
2. Create a staging directory matching the game's content path:
   ```
   staging/
     Moria/
       Content/
         (your modified DataTables, Blueprints, etc.)
   ```
3. Run retoc:
   ```bash
   retoc --override-container-header-version PreInitial to-zen -v ^
     --version UE4_27 ^
     "staging" ^
     "output/z_MoriaAdvancedBuilder_Content_P.utoc"
   ```
4. Create a stub .pak file if retoc doesn't generate one (copy any small existing .pak and rename)

**Option C — UnrealPak for legacy .pak then convert:**
1. Create `filelist.txt`:
   ```
   "C:\Path\To\Cooked\Moria\Content\*.*" "..\..\..\*.*"
   ```
2. Run UnrealPak:
   ```bash
   "C:\Program Files\Epic Games\UE_4.27\Engine\Binaries\Win64\UnrealPak.exe" ^
     "z_MoriaAdvancedBuilder_Content_P.pak" ^
     -Create="filelist.txt" -compress
   ```
3. Convert to IoStore with retoc if needed

### Step 5.5: Handle Signature Files

If the game's Paks folder contains `.sig` files:
1. Copy any existing `.sig` file
2. Rename to match your pak: `z_MoriaAdvancedBuilder_Content_P.sig`

Or use UniversalSigBypasser (drop-in DLL) from https://github.com/rm-NoobInCoding/UniversalSigBypasser

### Step 5.6: Deploy

1. Rename the output triplet:
   - `z_MoriaAdvancedBuilder_Content_P.pak`
   - `z_MoriaAdvancedBuilder_Content_P.ucas`
   - `z_MoriaAdvancedBuilder_Content_P.utoc`
2. The `z_` prefix = alphabetical-last = highest priority among `_P` paks
3. The `_P` suffix = mount priority over base game content
4. Copy to: `ReturnToMoria\Moria\Content\Paks\MoriaAdvancedBuilder\`

### Step 5.7: Test In-Game

1. Launch Return to Moria
2. Verify modified DataTable values take effect
3. Check build menu for new construction recipes
4. Enter landmark rooms to verify object removals
5. Check biome changes in relevant zones
6. **Multiplayer test:** Both server and client need the same pak for consistency

---

## Phase 6: Integration with the C++ Mod

### How the Two Halves Work Together

| Layer | Handles | Deployment |
|-------|---------|-----------|
| **Pak content** (editor project) | DataTable rows, Blueprints, meshes, textures, materials, level overrides, biome configs | `Content/Paks/MoriaAdvancedBuilder/z_*.pak/.ucas/.utoc` |
| **UE4SS C++ mod** (MoriaCppMod) | Runtime hooks, ProcessEvent, fly mode, quick-build, HISM removal, UI overlays, definition processing, controller input | `Win64/ue4ss/Mods/MoriaCppMod/dlls/main.dll` |

### Installer Updates

Add to `KhazadDumAdvancedBuilderPack.iss`:

```ini
; ── Cooked Content Pak ──────────────────────────────────────────────────
Source: "staging\Paks\z_MoriaAdvancedBuilder_Content_P.pak";  DestDir: "{app}\..\..\..\Content\Paks\MoriaAdvancedBuilder"; Flags: ignoreversion
Source: "staging\Paks\z_MoriaAdvancedBuilder_Content_P.ucas"; DestDir: "{app}\..\..\..\Content\Paks\MoriaAdvancedBuilder"; Flags: ignoreversion
Source: "staging\Paks\z_MoriaAdvancedBuilder_Content_P.utoc"; DestDir: "{app}\..\..\..\Content\Paks\MoriaAdvancedBuilder"; Flags: ignoreversion
```

### Version Coordination

Both the C++ mod and pak content must be versioned together. A pak that adds a DataTable row AND a C++ hook that references it must deploy in sync. The installer handles this naturally.

---

## Phase 7: Automation and Iteration

### Build Script (build_pak.ps1)

```powershell
# Cook content
& "$env:UE4_27\Engine\Binaries\Win64\UE4Editor-Cmd.exe" `
  "$PSScriptRoot\..\MoriaModKit\Moria.uproject" `
  -run=Cook -TargetPlatform=WindowsNoEditor -unattended

# Package with retoc
retoc --override-container-header-version PreInitial to-zen -v `
  --version UE4_27 `
  "$PSScriptRoot\..\MoriaModKit\Saved\Cooked\WindowsNoEditor\Moria\Content" `
  "$PSScriptRoot\staging\Paks\z_MoriaAdvancedBuilder_Content_P.utoc"

# Deploy to game for testing
Copy-Item "$PSScriptRoot\staging\Paks\z_*" `
  "C:\Program Files\Epic Games\ReturnToMoria\Moria\Content\Paks\MoriaAdvancedBuilder\" -Force
```

### CI/CD Integration

Add to existing `installer/build.ps1`:
1. Build C++ mod (CMake)
2. Cook pak content (UE4Editor-Cmd)
3. Package IoStore (retoc)
4. Compile installer (Inno Setup)
5. Sign (SSL.com eSigner)
6. Deploy to GitHub release

---

## Biome and Zone System — What's Data-Driven

The research confirmed Moria's biome system is **heavily data-driven**:

### Key Structures

**FBiomeDefinition** (DataTable row, 0xA8 bytes):
- `BiomeId` (GameplayTag), `DisplayName` (FText)
- `AudioConfig`, `DecoConfig`, `RockConfig`, `AtmosphericsConfig` (all data asset references)
- `DefaultCellData` (TMap<GameplayTag, float> — per-biome overrides)

**FZoneDefinition** (DataTable row, 0x278 bytes):
- Environment: `ZoneTemperature`, `WaterPrevalence`, `LightPrevalence`, `LightingCurve`
- Content: `BubbleDeck`, `PassageDeck`, `TargetBubbles`, `NewBubbleChance`
- Resources: `ZoneResources` array, `OrePlugDensity`, `OrePlugMineral`
- Enemies: `AiPopulationDistribution`, `AiZoneEncounter`, `AiPatrols`
- Music: `RoamingMusicPlaylist`
- Terrain: `RandomDirtPlugDensity`, `RandomDirtPlugType`, tier chances

**UMorBubbleDefinition** (data asset):
- `bEnable`, `BubbleName`, `BubbleType` (ECellContents)
- `bCanBuildInBubble`, `bCanSpawnAI`
- `VoxelMinerals` (ore types per room)
- `ProxyCatalog` (content spawn configuration)
- `VoxelDistanceField` (room shape — complex, not casually editable)

### What You CAN Change via Cooked Paks

| Change | DataTable/Asset | Impact |
|--------|----------------|--------|
| Remove a decoration type from a biome | UBiomeDecoConfig | All rooms of that biome lose that mesh |
| Change rock formations | UBiomeRockConfig | Different rocks spawn in that biome |
| Modify zone temperature | FZoneDefinition.ZoneTemperature | All rooms in that zone feel warmer/colder |
| Change ore types in a zone | FZoneDefinition.OrePlugMineral | Different ores appear in walls |
| Modify enemy types/density | FZoneDefinition.AiPopulationDistribution | Different enemies spawn |
| Change zone lighting | FZoneDefinition.LightingCurve + LightPrevalence | Brighter/darker zones |
| Enable/disable building in a room type | UMorBubbleDefinition.bCanBuildInBubble | Allow/prevent construction |
| Enable/disable enemy spawns | UMorBubbleDefinition.bCanSpawnAI | Peaceful rooms |

---

## What You CAN vs CANNOT See in the Editor

| Asset Type | See in Editor? | Edit in Editor? | Notes |
|-----------|---------------|----------------|-------|
| DataTable rows | YES — full table viewer | YES — add/modify/delete rows | The core modding surface |
| Blueprint default properties | YES — Details panel | YES — change values | Variables, component references |
| Blueprint component hierarchy | YES — Components panel | YES — add/remove/reposition | Meshes, colliders, etc. |
| Blueprint node graphs (logic) | **NO** | **NO** (use KismetKompiler for text-based editing) | Stripped during cooking |
| Static meshes | YES — 3D preview | YES — if imported as FBX | Can create/modify in Blender |
| Textures | YES — 2D preview | YES — if imported as PNG | Can create in any image editor |
| Materials (node graphs) | **NO** | **NO** — create new from scratch | Stripped during cooking |
| Material parameters | YES — parameter list | YES — modify scalars/vectors/textures | Via MaterialInstanceConstant |
| Data assets (configs) | YES — property editor | YES — modify any property | Biome configs, bubble defs |
| Level/sublevel content | PARTIAL — actor list | LIMITED — via UAssetGUI binary editing | Cooked levels lose editor data |
| Sound assets | YES — playback | YES — if reimported | Existing game sounds accessible |

---

## Risk Assessment

| Risk | Likelihood | Impact | Mitigation |
|------|-----------|--------|------------|
| UE4GameProjectGenerator fails on Moria's headers | MEDIUM | HIGH | Manual project creation using DRG FSD-Template as reference |
| DataTable row struct types not recognized | MEDIUM | HIGH | Verify all USTRUCT definitions compile before importing |
| IoStore cooking produces incompatible format | LOW | HIGH | Use retoc with `--override-container-header-version PreInitial` |
| FGK still doesn't see cooked DataTable rows | LOW | CRITICAL | Study TobiModsAddons pak — it already works |
| Material node graphs can't be reconstructed | CERTAIN | MEDIUM | Accept; create new materials from scratch |
| Blueprint logic can't be edited visually | CERTAIN | MEDIUM | Accept; use KismetKompiler for text-based edits |
| Game update changes asset format | MEDIUM | MEDIUM | Version-lock editor project to match game's UE4.27 |
| retoc offset issue (GitHub #51) | LOW | MEDIUM | Use UnrealReZen as alternative, or validate output |

---

## Milestones

**Milestone 1 (Day 2):** Template project compiles. Editor opens without crashing.

**Milestone 2 (Day 3):** At least one DataTable imported into editor, browsable with correct data.

**Milestone 3 (Day 4):** Modified DataTable (Coal MaxStackSize → 999) cooked, packed, deployed. Change visible in-game.

**Milestone 4 (Day 5):** NEW row added to DT_ConstructionRecipes appears in the game's build menu. **This is the moment the FGK cache problem is solved.**

**Milestone 5 (Week 2):** Landmark room object removed via cooked pak override. Verified in-game.

**Milestone 6 (Week 2+):** New building piece with custom mesh and recipe playable in-game.

---

## Reference Projects and Documentation

| Resource | URL | Relevance |
|----------|-----|-----------|
| DRG FSD-Template (UE4.27) | https://github.com/DRG-Modding/FSD-Template | Closest reference — same engine |
| DRG Blueprint Modding Guide | https://drg-modding.github.io/docs/guides/blueprint-modding-guide.html | Step-by-step UE4.27 workflow |
| UE4GameProjectGenerator | https://github.com/Buckminsterfullerene02/UE4GameProjectGenerator | Template generation |
| JsonAsAsset (4.27.2 supported) | https://github.com/JsonAsAsset/JsonAsAsset | Asset import |
| UEAssetToolkit-Fixes | https://github.com/Buckminsterfullerene02/UEAssetToolkit-Fixes | Bulk import commandlet |
| Comprehensive UE Modding Guide | https://buckminsterfullerene02.github.io/dev-guide/ | Dummying, cooking, paks |
| Dmgvol UE Modding Guides | https://github.com/Dmgvol/UE_Modding | CDOs, BP replication, IoStore |
| Hogwarts Legacy Modding Wiki | https://modding.wiki/en/hogwartslegacy/developers | IoStore cooking reference |
| retoc | https://github.com/trumank/retoc | IoStore conversion |
| UnrealReZen | https://github.com/rm-NoobInCoding/UnrealReZen | Alternative IoStore packer |
| FModel | https://fmodel.app | Game asset extraction |
| UAssetGUI | https://github.com/atenfyr/UAssetGUI | Binary .uasset editing |
| KismetKompiler | https://github.com/tge-was-taken/KismetKompiler | Blueprint bytecode editing |
| IoStore Packing Guide | https://github.com/Dmgvol/UE_Modding/blob/main/BasicModding/IoStorePacking.md | Step-by-step IoStore |
| UE4SS UHT Generation | https://docs.ue4ss.com/guides/generating-uht-compatible-headers.html | Header dump docs |
| UniversalSigBypasser | https://github.com/rm-NoobInCoding/UniversalSigBypasser | Pak signature bypass |

---

## Appendix A: FGK Cache Bypass Research (Alternative Runtime Approaches)

If the cooked pak approach (the primary plan above) is insufficient for some use case, these alternative runtime approaches were researched for bypassing the FGK wrapper cache without paks. They are ordered by feasibility.

### A.1 DiscoveryManager.Recipes Direct Injection

**Status:** UNTESTED — bypasses FGK entirely.

`AMorDiscoveryManager` holds:
- `Recipes` TArray at offset `0x0220` (TArray<FMorConstructionRecipeDefinition>)
- `Categories` TArray at offset `0x0230` (TArray<FMorCategoryTagDefinition>)
- `GetRecipeBlocks(CategoryTagDefinition)` is a UFUNCTION the BuildHUD calls

If the BuildHUD reads from this array, appending a properly constructed recipe definition struct would make new items appear in the build menu without touching the FGK cache at all.

**Test plan:** Duplicate an existing recipe, modify the name, append to the Recipes TArray, check the build menu.

### A.2 Custom UFunction Registration on FGK Wrapper

**Status:** FEASIBLE — UE4SS API exposes all primitives.

Register a native C++ function as a UFunction on any UClass at runtime:
```
NewObject<UFunction>(targetClass, UFunction::StaticClass(), FName("ModRefreshCache"))
→ SetFuncPtr(yourNativeFunction)
→ Set FUNC_Native | FUNC_Public | FUNC_BlueprintCallable flags
→ targetClass->GetFuncMap().Add(FName("ModRefreshCache"), newFunc)
→ targetClass->GetNativeFunctionLookupTable().Add(...)
```

Could register a cache-rebuild function on the FGK wrapper class that manually repopulates the TMap at offset 0x110.

### A.3 Hook FGK Wrapper PostLoad (Earliest Injection)

**Status:** FEASIBLE — requires vtable hooking.

Hook `PostLoad` on `MorConstructionRecipesTable` via vtable:
1. Our hook adds custom rows to the underlying UDataTable (at wrapper + 0x28)
2. Then calls the original PostLoad
3. The wrapper builds its cache with our rows already present

### A.4 HandleDataTableChanged Delegate Check

**Status:** QUICK TEST — worth 30 minutes.

`UDataTable::HandleDataTableChanged()` broadcasts an `OnDataTableChanged` multicast delegate. If FGK wrappers subscribe, calling it after `addRow()` would trigger a cache rebuild.

**Quick test:** Read the delegate's invocation list count on the FGK wrapper's TableAsset. If > 0, something is listening.

`HandleDataTableChanged` is `ENGINE_API` (exported symbol) — findable via `GetProcAddress` or AOB sigscan.

### A.5 Direct TMap Manipulation at Offset 0x0110

**Status:** VIABLE BUT COMPLEX — last resort.

FGK wrapper TMap layout (from UE4.27 engine source):
```
TMap<K,V> → TSet<TPair<K,V>>
  → TSparseArray<TSetElement<TPair<K,V>>>
    → TArray<TSetElement<...>> Data (pointer + Num + Max)
    → TBitArray AllocationFlags (pointer + NumBits + MaxBits)
    → int32 FirstFreeIndex, NumFreeIndices
  → HashType Hash (pointer + allocation count)
  → int32 HashSize
```

For `ConstructionRecipeLookup` (TMap<FMorConstructionRowHandle, FName>):
- Key: FMorConstructionRowHandle = 0x10 bytes (padding + FName)
- Value: FName = 0x08 bytes
- Each element: ~0x20 bytes with hash chain pointers

### A.6 IoStoreLoaderMod Pattern (Runtime Pak Mounting from C++)

**Status:** PROVEN on UE4.27 (Hi-Fi RUSH).

IoStoreLoaderMod (https://github.com/akmubi/IoStoreLoaderMod) demonstrates runtime IoStore mounting from a UE4SS C++ mod:
- MinHook + AOB sigscanning finds `FIoDispatcherImpl::Mount`, `FPakPlatformFile::Mount`, `StaticLoadClass`
- Patches `GetPakSigningKeysHelper` to bypass signature verification
- Hooks `MountAllPakFiles` to capture the FPakPlatformFile singleton
- ~650 lines of self-contained C++ in a UE4SS mod format

Useful for hot-reload or conditional content loading (not needed if auto-mount works).

---

## Appendix B: FGK Wrapper Internal Layout

```
UFGKDataTableBase (base, reflected size 0x40, actual to 0x110):
  0x0028  UDataTable* TableAsset
  0x0030  UDataTable* TestTableAsset
  0x0038  UFGKAdditiveDataTable* DynamicTableAsset
  0x0040–0x010F  0xD0 bytes of hidden non-reflected cache infrastructure

UMorConstructionRecipesTable (size 0x160):
  0x0110  TMap<FMorConstructionRowHandle, FName> ConstructionRecipeLookup (0x50 bytes)

UMorConstructionsTable (size 0x160):
  0x0110  TMap<TSoftClassPtr<AActor>, FName> ActorRowNameLookup (0x50 bytes)
```

Build menu data flow:
```
UDataTable (DT_Constructions, DT_ConstructionRecipes)
  → UFGKDataTableBase wrapper (caches rows at init)
    → AMorDiscoveryManager.Recipes array (0x0220)
      → Build HUD calls GetRecipeBlocks()
```
