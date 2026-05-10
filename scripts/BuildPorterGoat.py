#!/usr/bin/env python3
"""
BuildPorterGoat.py - Build the PorterGoat mod pak.

Two paths combined into one tiny IoStore mod:

  Path A: Re-enable the Porter NPC role
    DT_NPCRoles -> row "Porter" -> EnabledState: Disabled -> Live
    The dev team built the porter goat system but shipped it Disabled.
    Flipping it makes the role assignable. (Required tag: Fauna.Goat,
    which BP_NpcGoat already carries.)

  Path B: Register BP_NpcGoat in the AI spawn vocabulary
    DT_Moria_AI_Population -> add row "NpcGoat" -> BP_NpcGoat_C
    DT_AICharacterSettings -> add row "NpcGoat" cloned from "Goat"
    Does NOT add a distribution row, so the wildlife director will
    not randomly spawn it. UE4SS keypress remains the only trigger.

Pipeline (same as CleanSweep):
  1. UAssetGUI tojson on three source DTs
  2. Edit JSON in-place: flip Porter, add NpcGoat row x2
  3. UAssetGUI fromjson back to .uasset/.uexp
  4. Validate round-trip with another tojson
  5. Stage under correct content paths
  6. retoc to-zen -> IoStore .pak/.utoc/.ucas
  7. Zip to ~/Downloads/PorterGoat_v{VERSION}.zip

Usage:
    python scripts/BuildPorterGoat.py
"""

import copy
import json
import os
import shutil
import stat
import subprocess
import sys
import time
import zipfile
from pathlib import Path

# ---------------------------------------------------------------------------
# Config
# ---------------------------------------------------------------------------
SCRIPT_DIR = Path(__file__).resolve().parent
PROJECT_ROOT = SCRIPT_DIR.parent

EXPERIMENT_DIR = PROJECT_ROOT / 'experiments' / 'portergoat'
WORK_DIR = EXPERIMENT_DIR / 'work'
STAGING_DIR = EXPERIMENT_DIR / 'staging'
OUTPUT_DIR = EXPERIMENT_DIR / 'output'
DOWNLOADS_DIR = Path(os.path.expanduser('~/Downloads'))

LEGACY_ROOT = PROJECT_ROOT / 'tools' / 'legacy-assets' / 'Moria' / 'Content'

RETOC_EXE = PROJECT_ROOT / 'tools' / 'retoc' / 'bin' / 'retoc.exe'
UASSETGUI_EXE = PROJECT_ROOT / 'tools' / 'UAssetGUI' / 'UAssetGUI.exe'

# v1.1.1 — newer UAssetGUI for files requiring usmap parsing of UnversionedProperties.
# v1.0.2 (the legacy binary) crashes when given a [mappings name] argument
# because of a UI-thread invocation bug. v1.1.0 fixes this.
UASSETGUI_EXE_V110 = PROJECT_ROOT / 'tools' / 'UAssetGUI-v1.1.0' / 'UAssetGUI.exe'

# Mapping file basename (no extension) — UAssetGUI reads from
# %LOCALAPPDATA%/UAssetGUI/Mappings/<name>.usmap
USMAP_NAME = 'Moria'

UE_VERSION = 'VER_UE4_27'
RETOC_VERSION = 'UE4_27'

MOD_VERSION = '1.1.3'
PAK_NAME = 'PorterGoat_P'
NPCGOAT_CLASS_PATH = '/Game/Character/NpcGoat/BP_NpcGoat.BP_NpcGoat_C'
NPCGOAT_PACKAGE_PATH = '/Game/Character/NpcGoat/BP_NpcGoat'

# v1.0.2 — drops the brand-new BP_PorterGoatLoader asset entirely.
# Theory A (IoStore rejecting brand-new mod-pak paths) was confirmed at
# runtime: the loader package returned 0x0 from every load API. Override
# paths (DT_NPCRoles, etc.) work fine.
#
# Replacement: embed a hard UClass* reference inside DT_NPCRoles by
# adding a dummy "_PorterGoatLoader" row whose WorkBehavior field
# (which is hard ObjectPropertyData, not soft) points at BP_NpcGoat_C.
# When the modified DT_NPCRoles loads at boot, that import is resolved,
# pulling /Game/Character/NpcGoat/BP_NpcGoat into memory.
# Type validation against TSubclassOf<UMorBehaviorState> happens AFTER
# import resolution, so the load fires regardless of type mismatch.
# v1.0.3: row is Live (was Disabled in v1.0.2). Theory was that Disabled
# rows skip eager import resolution; runtime probe confirmed v1.0.2 didn't
# trigger BP_NpcGoat load. To keep the role un-assignable while Live, we
# set RequiredTags to an impossible tag no entity carries.
LOADER_ROW_NAME = '_PorterGoatLoader'
LOADER_IMPOSSIBLE_TAG = '_DoesNotExist_PorterGoatLoader'

# All FName strings introduced by the NpcGoat row addition.
# UAssetGUI serialises FSoftObjectPath.AssetName as an FName, so the full
# class path AND the package path must exist in NameMap before fromjson.
NPCGOAT_NAMEMAP_ADDITIONS = [
    'NpcGoat',
    NPCGOAT_PACKAGE_PATH,
    NPCGOAT_CLASS_PATH,
]

# (legacy-assets relpath, staging relpath, friendly name)
# NOTE: in v1.0.4 the list includes a Blueprint asset (BP_MoriaGameMode_MainMenu)
# alongside the three DTs. The build pipeline is generic — it just round-trips
# each entry through tojson/edit/fromjson per its registered editor function.
DTS = [
    ('Character/NpcDwarf/DT_NPCRoles',
     'Character/NpcDwarf/DT_NPCRoles',
     'DT_NPCRoles'),
    ('Character/AI/Spawning/DT_Moria_AI_Population',
     'Character/AI/Spawning/DT_Moria_AI_Population',
     'DT_Moria_AI_Population'),
    ('Character/AI/Spawning/DT_AICharacterSettings',
     'Character/AI/Spawning/DT_AICharacterSettings',
     'DT_AICharacterSettings'),
    ('Tech/GameModes/BP_MoriaGameMode_MainMenu',
     'Tech/GameModes/BP_MoriaGameMode_MainMenu',
     'BP_MoriaGameMode_MainMenu'),
    ('Character/NpcGoat/BP_NpcGoat',
     'Character/NpcGoat/BP_NpcGoat',
     'BP_NpcGoat'),
    # v1.1.0 Phase 1 — register the goat as a proper NPC by mirroring dwarf NPC plumbing
    ('Character/NpcDwarf/DT_NPCInventoryPresets',
     'Character/NpcDwarf/DT_NPCInventoryPresets',
     'DT_NPCInventoryPresets'),
    ('Character/NpcDwarf/DT_NPCUniqueCharacters',
     'Character/NpcDwarf/DT_NPCUniqueCharacters',
     'DT_NPCUniqueCharacters'),
    ('Tech/Data/Items/DT_Storage',
     'Tech/Data/Items/DT_Storage',
     'DT_Storage'),
    ('Tech/Data/Items/DT_ContainerItems',
     'Tech/Data/Items/DT_ContainerItems',
     'DT_ContainerItems'),
    # v1.1.1 — requires Moria.usmap (CDO is UnversionedProperties RawExport
    # without it). asset_needs_usmap('BP_NPCManager') routes this through
    # UAssetGUI v1.1.0 + Moria mapping.
    ('Tech/Managers/BP_NPCManager',
     'Tech/Managers/BP_NPCManager',
     'BP_NPCManager'),
    # v1.1.2 — co-locate goat with Survivor_2 in 3-2 LowerDeeps via
    # SurvivorRescue2 challenge spawn group.
    ('Tech/Data/GameWorld/DT_Moria_AIChallengeSpawns',
     'Tech/Data/GameWorld/DT_Moria_AIChallengeSpawns',
     'DT_Moria_AIChallengeSpawns'),
]

# Pack class for v1.0.5 DummyEquipment override
PACK_CLASS_PATH    = '/Game/Items/EpicPacks/BP_EpicPack_AdventurersPack_Large.BP_EpicPack_AdventurersPack_Large_C'
PACK_PACKAGE_PATH  = '/Game/Items/EpicPacks/BP_EpicPack_AdventurersPack_Large'
PACK_CLASS_NAME    = 'BP_EpicPack_AdventurersPack_Large_C'

# Goat BodyInventory wrapper BP — authored in Phase 2 (v1.2.0). DT_ContainerItems
# carries a soft reference to this path; the actual BP ships in Phase 2.
GOAT_BODY_INVENTORY_PACKAGE_PATH = '/Game/Mods/PorterGoat/Items/BP_ContainerItem_Goat_BodyInventory'
GOAT_BODY_INVENTORY_CLASS_PATH   = '/Game/Mods/PorterGoat/Items/BP_ContainerItem_Goat_BodyInventory.BP_ContainerItem_Goat_BodyInventory_C'


# ---------------------------------------------------------------------------
# Helpers (lifted from BuildBearNestRemoval / BuildCleanSweep style)
# ---------------------------------------------------------------------------

def log(msg=''):
    print(msg)


def _rmtree_onerror(func, path, exc_info):
    os.chmod(path, stat.S_IWRITE)
    time.sleep(0.2)
    func(path)


def rmtree_safe(d):
    if not d.exists():
        return
    for _ in range(3):
        try:
            shutil.rmtree(d, onerror=_rmtree_onerror)
            return
        except PermissionError:
            time.sleep(1)
    log(f"  WARN: Could not fully remove {d}")


def run_uassetgui_tojson(uasset_path, json_output, use_usmap=False):
    """Convert .uasset to JSON. If use_usmap=True, use UAssetGUI v1.1.0
    with the Moria usmap (needed for assets that store UnversionedProperties
    such as BP_NPCManager)."""
    exe = UASSETGUI_EXE_V110 if use_usmap else UASSETGUI_EXE
    cmd = [str(exe), 'tojson', str(uasset_path), str(json_output), UE_VERSION]
    if use_usmap:
        cmd.append(USMAP_NAME)
    r = subprocess.run(cmd, capture_output=True, text=True, timeout=60)
    if r.returncode != 0:
        log(f"    FAIL tojson exit={r.returncode}\n    {r.stderr[:500]}")
        return False
    return True


def run_uassetgui_fromjson(json_path, uasset_output, use_usmap=False):
    """Convert JSON back to .uasset. Mirror of tojson — pass use_usmap=True
    for assets parsed with the usmap so the inverse uses the same binary."""
    exe = UASSETGUI_EXE_V110 if use_usmap else UASSETGUI_EXE
    cmd = [str(exe), 'fromjson', str(json_path), str(uasset_output), UE_VERSION]
    if use_usmap:
        cmd.append(USMAP_NAME)
    r = subprocess.run(cmd, capture_output=True, text=True, timeout=60)
    if r.returncode != 0:
        log(f"    FAIL fromjson exit={r.returncode}\n    {r.stderr[:500]}")
        return False
    return True


def asset_needs_usmap(name):
    """Returns True for assets whose CDO uses UnversionedProperties (RawExport
    without a mapping). v1.1.1 added BP_NPCManager.
    """
    return name in ('BP_NPCManager',)


def run_retoc_tozen(staging_dir, output_dir, pak_name):
    output_utoc = output_dir / f'{pak_name}.utoc'
    cmd = [str(RETOC_EXE), 'to-zen', '-v', '--version', RETOC_VERSION,
           str(staging_dir), str(output_utoc)]
    log(f"  retoc to-zen -> {pak_name}")
    r = subprocess.run(cmd, capture_output=True, text=True, timeout=300)
    if r.stdout:
        for ln in r.stdout.strip().split('\n')[-5:]:
            log(f"  [retoc] {ln}")
    if r.stderr:
        for ln in r.stderr.strip().split('\n')[-5:]:
            log(f"  [retoc] {ln}")
    return r.returncode == 0


# ---------------------------------------------------------------------------
# Edits
# ---------------------------------------------------------------------------

def ensure_namemap_entry(data, name):
    """Add `name` to NameMap if it isn't already present.

    UAssetGUI usually handles new FNames automatically on fromjson, but we add
    explicitly to be safe. NameMap is a simple list of strings.
    """
    nm = data.get('NameMap', [])
    if name not in nm:
        nm.append(name)
        data['NameMap'] = nm
        return True
    return False


def _add_npcgoat_imports_to_asset(data, label='asset'):
    """Append package + class imports for /Game/Character/NpcGoat/BP_NpcGoat
    and BP_NpcGoat_C.  Returns the negative import index of BP_NpcGoat_C
    (i.e. the value to assign to the WorkBehavior field).

    Idempotent: if the imports already exist, returns the existing index.
    """
    imports = data['Imports']

    # Check if BP_NpcGoat_C class import already exists
    for i, imp in enumerate(imports):
        if (imp.get('ObjectName') == 'BP_NpcGoat_C'
                and imp.get('ClassPackage') == '/Script/Engine'
                and imp.get('ClassName') == 'BlueprintGeneratedClass'):
            log(f"    NOTE: BP_NpcGoat_C class import already at -{i+1}")
            return -(i + 1)

    # Add package import
    pkg_import = {
        '$type': 'UAssetAPI.Import, UAssetAPI',
        'ObjectName': NPCGOAT_PACKAGE_PATH,
        'OuterIndex': 0,
        'ClassPackage': '/Script/CoreUObject',
        'ClassName': 'Package',
        'PackageName': None,
        'bImportOptional': False,
    }
    imports.append(pkg_import)
    pkg_idx_neg = -len(imports)
    log(f"    + Package import at {pkg_idx_neg}: {NPCGOAT_PACKAGE_PATH}")

    # Add class import
    cls_import = {
        '$type': 'UAssetAPI.Import, UAssetAPI',
        'ObjectName': 'BP_NpcGoat_C',
        'OuterIndex': pkg_idx_neg,
        'ClassPackage': '/Script/Engine',
        'ClassName': 'BlueprintGeneratedClass',
        'PackageName': None,
        'bImportOptional': False,
    }
    imports.append(cls_import)
    cls_idx_neg = -len(imports)
    log(f"    + Class   import at {cls_idx_neg}: BP_NpcGoat_C (outer={pkg_idx_neg})")

    return cls_idx_neg


def edit_npcroles(data):
    """Two edits to the Porter row:
       1. Flip EnabledState Disabled -> Live.
       2. Clean up the FRG annotations on DisplayName and Description
          (drop the leading "*" and "[Bug this]" marker so the role
          shows up cleanly in the player's role-assignment UI).

    v1.0.4: removed the _PorterGoatLoader sentinel row. v1.0.3 confirmed DT
    row hard imports don't fire eagerly regardless of EnabledState.
    """
    rows = data['Exports'][0]['Table']['Data']
    porter = next((r for r in rows if r.get('Name') == 'Porter'), None)
    if porter is None:
        log("    ERROR: Porter row not found")
        return False

    flipped = False
    cleaned_display = False
    cleaned_desc = False
    for prop in porter['Value']:
        pname = prop.get('Name')
        if pname == 'EnabledState':
            old = prop.get('Value')
            prop['Value'] = 'ERowEnabledState::Live'
            log(f"    Porter.EnabledState: {old} -> {prop['Value']}")
            flipped = True
        elif pname == 'DisplayName':
            # TextPropertyData carries SourceString and LocalizedString that
            # render in the UI when the StringTable lookup fires. Strip
            # the dev annotations from both.
            for k in ('SourceString', 'LocalizedString'):
                v = prop.get(k)
                if isinstance(v, str) and v == '*Porter [Bug this]':
                    prop[k] = 'Porter'
                    cleaned_display = True
            if cleaned_display:
                log(f"    Porter.DisplayName: '*Porter [Bug this]' -> 'Porter'")
        elif pname == 'Description':
            for k in ('SourceString', 'LocalizedString'):
                v = prop.get(k)
                if isinstance(v, str) and v == '*Carries items for a player.':
                    prop[k] = 'Carries items for a player.'
                    cleaned_desc = True
            if cleaned_desc:
                log(f"    Porter.Description: '*Carries items...' -> 'Carries items...'")

    if not flipped:
        log("    ERROR: Porter row has no EnabledState property")
        return False
    return True


def _clone_row(rows, template_name, new_name):
    """Clone an existing row (deep copy) and rename it. Returns the new row.
       Idempotent: if the row already exists, returns it unchanged.
    """
    if any(r.get('Name') == new_name for r in rows):
        log(f"    NOTE: row '{new_name}' already exists (idempotent skip)")
        return None
    template = next((r for r in rows if r.get('Name') == template_name), None)
    if template is None:
        log(f"    ERROR: template row '{template_name}' not found")
        return None
    new_row = copy.deepcopy(template)
    new_row['Name'] = new_name
    return new_row


def edit_npcinventorypresets(data):
    """Add a 'Porter' row to DT_NPCInventoryPresets.

    Cloned from 'EmptyLoadout' so the InventoryLoadout import index (hard
    ObjectProperty pointing at DA_NpcDwarf_EmptyLoadout) stays valid. Porter
    starts with no items in inventory; future passes can swap in a goat-specific
    DA when one ships.
    """
    rows = data['Exports'][0]['Table']['Data']
    new_row = _clone_row(rows, 'EmptyLoadout', 'Porter')
    if new_row is None:
        return True  # idempotent skip / template missing already logged
    # No field changes — Porter inherits EmptyLoadout's hard import
    rows.append(new_row)
    ensure_namemap_entry(data, 'Porter')
    log(f"    Added row 'Porter' (cloned from EmptyLoadout, hard ref to DA_NpcDwarf_EmptyLoadout)")
    log(f"    DT_NPCInventoryPresets row count: {len(rows)}")
    return True


def edit_npcuniquecharacters(data):
    """Add a 'PorterGoat' row to DT_NPCUniqueCharacters.

    Cloned from 'Wanderer' (Vror) and retargeted:
      - CharacterClass (soft) -> /Game/Character/NpcGoat/BP_NpcGoat.BP_NpcGoat_C
      - AppearancePreset.RowName -> "None" (no character customization for goat)
      - CharacterName.Value -> "PorterGoat" (string table key fallback)
    """
    rows = data['Exports'][0]['Table']['Data']
    new_row = _clone_row(rows, 'Wanderer', 'PorterGoat')
    if new_row is None:
        return True

    for prop in new_row['Value']:
        pname = prop.get('Name')
        if pname == 'CharacterClass':
            # SoftObjectPropertyData: change the AssetPath.AssetName
            v = prop.get('Value', {})
            ap = v.get('AssetPath', {})
            ap['AssetName'] = NPCGOAT_CLASS_PATH
            log(f"    PorterGoat.CharacterClass -> {NPCGOAT_CLASS_PATH}")
        elif pname == 'AppearancePreset':
            # struct DataTableRowHandle — set RowName to "None"
            for sub in prop.get('Value', []):
                if sub.get('Name') == 'RowName':
                    sub['Value'] = 'None'
                    log(f"    PorterGoat.AppearancePreset.RowName -> 'None'")
        elif pname == 'CharacterName':
            # TextProperty with string-table reference; just change the Value
            # (the engine falls back to displaying the key when the string
            # table doesn't have an entry, which is fine for a debug label).
            prop['Value'] = 'PorterGoat'
            log(f"    PorterGoat.CharacterName.Value -> 'PorterGoat'")

    rows.append(new_row)
    ensure_namemap_entry(data, 'PorterGoat')
    # The new SoftObjectPath AssetName needs to be in NameMap (FName-serialized)
    ensure_namemap_entry(data, NPCGOAT_PACKAGE_PATH)
    ensure_namemap_entry(data, NPCGOAT_CLASS_PATH)
    log(f"    DT_NPCUniqueCharacters row count: {len(rows)}")
    return True


def edit_dt_storage(data):
    """Add a 'Goat.BodyInventory' row to DT_Storage.

    Cloned from 'Dwarf.BodyInventory' and retargeted:
      - InventoryWidth: 8 (unchanged from dwarf)
      - InventoryHeight: 1 -> 8 (8x8 grid)
      - AllowedEquip: drop weapon slots (no MainHand/OffHand/BothHands/Ammo)
      - ExcludeItems: keep dwarf's exclusions (no EpicPack/EpicItem/Brew/HandsOnly)

    User noted weapons/armor are not goat things; this excludes them from
    the goat's inventory grid. Future pass may relax these constraints.
    """
    rows = data['Exports'][0]['Table']['Data']
    new_row = _clone_row(rows, 'Dwarf.BodyInventory', 'Goat.BodyInventory')
    if new_row is None:
        return True

    for prop in new_row['Value']:
        pname = prop.get('Name')
        if pname == 'InventoryHeight':
            old = prop.get('Value')
            prop['Value'] = 8
            log(f"    Goat.BodyInventory.InventoryHeight: {old} -> 8 (8x8 grid)")
        elif pname == 'AllowedEquip':
            # SetPropertyData of EnumProperty — clear the equipment-slot list
            # (goat has no weapon slots; nothing equippable belongs in its body grid).
            old_count = len(prop.get('Value', []))
            prop['Value'] = []
            log(f"    Goat.BodyInventory.AllowedEquip: {old_count} entries -> []")

    rows.append(new_row)
    ensure_namemap_entry(data, 'Goat.BodyInventory')
    log(f"    DT_Storage row count: {len(rows)}")
    return True


def edit_dt_containeritems(data):
    """Add a 'Goat.BodyInventory' row to DT_ContainerItems.

    Cloned from 'Dwarf.BodyInventory' and retargeted:
      - StorageRowHandle.RowName -> "Goat.BodyInventory"
      - Actor.AssetPath.AssetName -> /Game/Mods/PorterGoat/Items/BP_ContainerItem_Goat_BodyInventory.BP_ContainerItem_Goat_BodyInventory_C
        (Phase 2 will ship that BP; the soft ref allows the row to load now and resolve later.)
      - Tags retain "Item.ContainerItem" + "Inventory.BodyInventory"

    DisplayName/Description TextProperty values are left pointing at the dwarf
    string table keys; engine falls back to displaying the key string itself
    if no localized entry matches our new keys. Cosmetic only.
    """
    rows = data['Exports'][0]['Table']['Data']
    new_row = _clone_row(rows, 'Dwarf.BodyInventory', 'Goat.BodyInventory')
    if new_row is None:
        return True

    for prop in new_row['Value']:
        pname = prop.get('Name')
        if pname == 'StorageRowHandle':
            for sub in prop.get('Value', []):
                if sub.get('Name') == 'RowName':
                    sub['Value'] = 'Goat.BodyInventory'
                    log(f"    Goat.BodyInventory.StorageRowHandle.RowName -> 'Goat.BodyInventory'")
        elif pname == 'Actor':
            # SoftObjectPropertyData
            v = prop.get('Value', {})
            ap = v.get('AssetPath', {})
            ap['AssetName'] = GOAT_BODY_INVENTORY_CLASS_PATH
            log(f"    Goat.BodyInventory.Actor -> {GOAT_BODY_INVENTORY_CLASS_PATH}")

    rows.append(new_row)
    ensure_namemap_entry(data, 'Goat.BodyInventory')
    ensure_namemap_entry(data, GOAT_BODY_INVENTORY_PACKAGE_PATH)
    ensure_namemap_entry(data, GOAT_BODY_INVENTORY_CLASS_PATH)
    log(f"    DT_ContainerItems row count: {len(rows)}")
    return True


def edit_mainmenu_gamemode(data):
    """Override BP_MoriaGameMode_MainMenu's DefaultPawnClass CDO default
    from BP_CharSelectionPawn_C to BP_NpcGoat_C.

    Both classes are Pawn-derived, so the engine's TSubclassOf<APawn> type
    check accepts the override at validation time. The hard import is
    resolved eagerly during CDO deserialization at title-screen load,
    pulling /Game/Character/NpcGoat/BP_NpcGoat permanently into memory.

    Side effect: at the character-selection screen, the menu pawn appears
    as a goat instead of a dwarf. Acceptable tradeoff for the load anchor.
    """
    # Find the CDO export
    cdo = None
    for exp in data.get('Exports', []):
        on = exp.get('ObjectName', '')
        if on.startswith('Default__BP_MoriaGameMode_MainMenu'):
            cdo = exp
            break
    if cdo is None:
        log("    ERROR: Default__BP_MoriaGameMode_MainMenu CDO not found")
        return False

    # Find DefaultPawnClass property in CDO Data
    target_prop = None
    for prop in cdo.get('Data', []):
        if prop.get('Name') == 'DefaultPawnClass':
            target_prop = prop
            break
    if target_prop is None:
        log("    ERROR: DefaultPawnClass property not found on CDO")
        log("    (it may inherit the parent's value without an override entry)")
        return False

    # Add NameMap entries (FName strings the new imports will reference)
    for n in [NPCGOAT_PACKAGE_PATH, 'BP_NpcGoat_C']:
        ensure_namemap_entry(data, n)

    # Add hard imports for BP_NpcGoat_C (returns negative class import idx)
    bpgoat_class_idx = _add_npcgoat_imports_to_asset(data, 'MainMenuGameMode')

    # Retarget DefaultPawnClass value
    old = target_prop.get('Value')
    target_prop['Value'] = bpgoat_class_idx
    log(f"    Default__BP_MoriaGameMode_MainMenu.DefaultPawnClass: {old} -> {bpgoat_class_idx} (BP_NpcGoat_C)")

    # Update CDO's CreateBeforeSerializationDependencies to include our class
    deps = cdo.get('CreateBeforeSerializationDependencies', [])
    if isinstance(old, int) and old < 0 and old in deps:
        deps[deps.index(old)] = bpgoat_class_idx
    elif bpgoat_class_idx not in deps:
        deps.append(bpgoat_class_idx)
    cdo['CreateBeforeSerializationDependencies'] = deps
    log(f"    CDO.CreateBeforeSerializationDependencies updated: {deps}")
    return True


def edit_ai_population(data):
    """Add new row 'NpcGoat' cloned from 'Goat', repointed at BP_NpcGoat_C."""
    rows = data['Exports'][0]['Table']['Data']

    # Guard against double-add
    if any(r.get('Name') == 'NpcGoat' for r in rows):
        log("    NOTE: NpcGoat row already present (idempotent skip)")
        return True

    template = next((r for r in rows if r.get('Name') == 'Goat'), None)
    if template is None:
        log("    ERROR: Template row 'Goat' not found")
        return False

    new_row = copy.deepcopy(template)
    new_row['Name'] = 'NpcGoat'
    # Re-point CharacterClass
    for prop in new_row['Value']:
        if prop.get('Name') == 'CharacterClass':
            prop['Value']['AssetPath']['AssetName'] = NPCGOAT_CLASS_PATH

    rows.append(new_row)
    for n in NPCGOAT_NAMEMAP_ADDITIONS:
        ensure_namemap_entry(data, n)
    log(f"    Added row 'NpcGoat' -> {NPCGOAT_CLASS_PATH}")
    log(f"    Population row count: {len(rows)}")
    return True


def edit_aicharsettings(data):
    """Add new row 'NpcGoat' cloned from 'Goat', repointed at BP_NpcGoat_C."""
    rows = data['Exports'][0]['Table']['Data']

    if any(r.get('Name') == 'NpcGoat' for r in rows):
        log("    NOTE: NpcGoat row already present (idempotent skip)")
        return True

    template = next((r for r in rows if r.get('Name') == 'Goat'), None)
    if template is None:
        log("    ERROR: Template row 'Goat' not found")
        return False

    new_row = copy.deepcopy(template)
    new_row['Name'] = 'NpcGoat'
    for prop in new_row['Value']:
        if prop.get('Name') == 'CharacterClass':
            prop['Value']['AssetPath']['AssetName'] = NPCGOAT_CLASS_PATH

    rows.append(new_row)
    for n in NPCGOAT_NAMEMAP_ADDITIONS:
        ensure_namemap_entry(data, n)
    log(f"    Added row 'NpcGoat' -> {NPCGOAT_CLASS_PATH}")
    log(f"    AICharacterSettings row count: {len(rows)}")
    return True


def _add_bp_class_imports(data, pkg_path, class_name, label):
    """Append package + BlueprintGeneratedClass imports for a BP class.
       Returns the negative import index of the class (or existing one).
       Idempotent.
    """
    imports = data['Imports']
    for i, imp in enumerate(imports):
        if (imp.get('ObjectName') == class_name
                and imp.get('ClassPackage') == '/Script/Engine'
                and imp.get('ClassName') == 'BlueprintGeneratedClass'):
            existing = -(i + 1)
            log(f"    NOTE: [{label}] class import {class_name} already at {existing}")
            return existing
    pkg_import = {
        '$type': 'UAssetAPI.Import, UAssetAPI',
        'ObjectName': pkg_path,
        'OuterIndex': 0,
        'ClassPackage': '/Script/CoreUObject',
        'ClassName': 'Package',
        'PackageName': None,
        'bImportOptional': False,
    }
    imports.append(pkg_import)
    pkg_idx = -len(imports)
    log(f"    + [{label}] Package import at {pkg_idx}: {pkg_path}")
    cls_import = {
        '$type': 'UAssetAPI.Import, UAssetAPI',
        'ObjectName': class_name,
        'OuterIndex': pkg_idx,
        'ClassPackage': '/Script/Engine',
        'ClassName': 'BlueprintGeneratedClass',
        'PackageName': None,
        'bImportOptional': False,
    }
    imports.append(cls_import)
    cls_idx = -len(imports)
    log(f"    + [{label}] Class   import at {cls_idx}: {class_name} (outer={pkg_idx})")
    return cls_idx


def edit_bp_npcgoat(data):
    """Two BP_NpcGoat CDO edits:

    1. v1.0.5 carry-forward: EquipComp.DummyEquipment ->
       BP_EpicPack_AdventurersPack_Large_C  (dormant; auto-attach didn't fire,
       but harmless to leave in place).

    2. v1.1.0 Phase 2: InventoryComp.DefaultContainers ->
       [BP_ContainerItem_Goat_BodyInventory_C]  (gives the goat its 8x8
       BodyInventory grid via the new wrapper BP we ship in this pak).
    """
    # ---------------------------------------------------------------- (1)
    # EquipComp.DummyEquipment override (carry-forward from v1.0.5)
    equipcomp_export = next((e for e in data.get('Exports', [])
                             if e.get('ObjectName') == 'EquipComp'), None)
    if equipcomp_export is None:
        log("    ERROR: EquipComp export not found")
        return False

    has_dummy = any(p.get('Name') == 'DummyEquipment'
                    for p in equipcomp_export.get('Data', []))
    if has_dummy:
        log("    NOTE: EquipComp.DummyEquipment already set (idempotent skip)")
    else:
        for n in ['DummyEquipment', PACK_PACKAGE_PATH, PACK_CLASS_NAME]:
            ensure_namemap_entry(data, n)
        pack_class_idx = _add_bp_class_imports(
            data, PACK_PACKAGE_PATH, PACK_CLASS_NAME, 'AdventurersPack')
        new_prop = {
            '$type': 'UAssetAPI.PropertyTypes.Objects.ObjectPropertyData, UAssetAPI',
            'Name': 'DummyEquipment',
            'ArrayIndex': 0,
            'IsZero': False,
            'PropertyTagFlags': 'None',
            'PropertyTagExtensions': 'NoExtension',
            'Value': pack_class_idx,
        }
        equipcomp_export.setdefault('Data', []).append(new_prop)
        log(f"    EquipComp.DummyEquipment = {pack_class_idx} ({PACK_CLASS_NAME})")
        deps = equipcomp_export.get('CreateBeforeSerializationDependencies', [])
        if pack_class_idx not in deps:
            deps.append(pack_class_idx)
        equipcomp_export['CreateBeforeSerializationDependencies'] = deps
        log(f"    EquipComp.CreateBeforeSerializationDependencies updated: {deps}")

    # ---------------------------------------------------------------- (2)
    # InventoryComp.DefaultContainers override (v1.1.0 Phase 2)
    invcomp_export = next((e for e in data.get('Exports', [])
                           if e.get('ObjectName') == 'InventoryComp'), None)
    if invcomp_export is None:
        log("    ERROR: InventoryComp export not found")
        return False

    has_dc = any(p.get('Name') == 'DefaultContainers'
                 for p in invcomp_export.get('Data', []))
    if has_dc:
        log("    NOTE: InventoryComp.DefaultContainers already set (idempotent skip)")
        return True

    # NameMap entries needed for the new field + import
    for n in ['DefaultContainers',
              GOAT_BODY_INVENTORY_PACKAGE_PATH,
              'BP_ContainerItem_Goat_BodyInventory_C']:
        ensure_namemap_entry(data, n)

    # Hard import of the goat BodyInventory wrapper class
    goat_bi_idx = _add_bp_class_imports(
        data,
        GOAT_BODY_INVENTORY_PACKAGE_PATH,
        'BP_ContainerItem_Goat_BodyInventory_C',
        'GoatBodyInventory')

    # Construct the DefaultContainers ArrayPropertyData (mirrors dwarf shape)
    dc_prop = {
        '$type': 'UAssetAPI.PropertyTypes.Objects.ArrayPropertyData, UAssetAPI',
        'ArrayType': 'ObjectProperty',
        'DummyStruct': None,
        'Name': 'DefaultContainers',
        'ArrayIndex': 0,
        'IsZero': False,
        'PropertyTagFlags': 'None',
        'PropertyTagExtensions': 'NoExtension',
        'Value': [
            {
                '$type': 'UAssetAPI.PropertyTypes.Objects.ObjectPropertyData, UAssetAPI',
                'Name': '0',
                'ArrayIndex': 0,
                'IsZero': False,
                'PropertyTagFlags': 'None',
                'PropertyTagExtensions': 'NoExtension',
                'Value': goat_bi_idx,
            },
        ],
    }
    invcomp_export.setdefault('Data', []).append(dc_prop)
    log(f"    InventoryComp.DefaultContainers = [{goat_bi_idx} (Goat.BodyInventory wrapper)]")

    # Update CreateBeforeSerializationDependencies on InventoryComp
    inv_deps = invcomp_export.get('CreateBeforeSerializationDependencies', [])
    if goat_bi_idx not in inv_deps:
        inv_deps.append(goat_bi_idx)
    invcomp_export['CreateBeforeSerializationDependencies'] = inv_deps
    log(f"    InventoryComp.CreateBeforeSerializationDependencies updated: {inv_deps}")

    # ---------------------------------------------------------------- (3)
    # MorNPC component bool overrides (v1.1.3) — make Rescue prompt surface
    # on E-press AND Manage prompt show post-rescue.
    #
    # The 7 MorInteraction structs are configured (Rescue/Manage/Revive on
    # the goat — minus Talk/Details/Recruit which are missing structs).
    # The bRescueInteractionEnabled / bManageInteractionEnabled bools are
    # NOT overridden by default on BP_NpcGoat — they inherit from C++.
    # Per usmap dump, these bools exist on MorNPCComponent.
    # Adding them as CDO overrides forces the prompts to surface.
    morpc_export = next((e for e in data.get('Exports', [])
                         if e.get('ObjectName') == 'MorNPC_GEN_VARIABLE'), None)
    if morpc_export is None:
        # Fall back: some BPs name it 'MorNPC' without the GEN_VARIABLE suffix
        morpc_export = next((e for e in data.get('Exports', [])
                             if e.get('ObjectName') == 'MorNPC'), None)
    if morpc_export is None:
        log("    WARN: MorNPC component export not found — skipping interaction-bool overrides")
        return True

    bool_flags = {
        'bRescueInteractionEnabled': True,
        'bManageInteractionEnabled': True,
        'bInteractionEnabled': True,
    }
    morpc_data = morpc_export.setdefault('Data', [])
    for fname, fval in bool_flags.items():
        existing = next((p for p in morpc_data
                         if isinstance(p, dict) and p.get('Name') == fname), None)
        if existing:
            log(f"    NOTE: MorNPC.{fname} already overridden (skip)")
            continue
        ensure_namemap_entry(data, fname)
        new_prop = {
            '$type': 'UAssetAPI.PropertyTypes.Objects.BoolPropertyData, UAssetAPI',
            'Name': fname,
            'ArrayIndex': 0,
            'PropertyGuid': None,
            'IsZero': False,
            'PropertyTagFlags': 'None',
            'PropertyTypeName': None,
            'PropertyTagExtensions': 'NoExtension',
            'Value': fval,
        }
        morpc_data.append(new_prop)
        log(f"    MorNPC.{fname} = {fval}")

    return True


def edit_bp_npcmanager(data):
    """Append BP_NpcGoat_C to BP_NPCManager.ValidNpcClasses CDO array.

    The 'Manager' class uses UnversionedProperties — without the Moria usmap,
    the CDO is a RawExport blob and unmodifiable. With the usmap loaded,
    ValidNpcClasses surfaces as `TArray<TSoftClassPath>` (12 dwarf entries).

    Persistence requirement (per VS-Claude runtime testing of v1.1.0):
    save iteration filters by ValidNpcClasses, dropping unregistered classes.
    Adding BP_NpcGoat_C here lets the goat persist across save/reload like a
    recruited dwarf NPC.
    """
    cdo = next((e for e in data.get('Exports', [])
                if e.get('ObjectName', '').startswith('Default__BP_NPCManager')), None)
    if cdo is None:
        log("    ERROR: Default__BP_NPCManager_C CDO not found")
        return False

    target_prop = next((p for p in cdo.get('Data', [])
                        if isinstance(p, dict) and p.get('Name') == 'ValidNpcClasses'), None)
    if target_prop is None:
        log("    ERROR: ValidNpcClasses property not found on CDO")
        log("    (CDO is likely RawExport; verify usmap=Moria was applied)")
        return False

    entries = target_prop.get('Value', [])
    # Idempotency: walk the array, look for our class path
    for el in entries:
        if not isinstance(el, dict):
            continue
        inner_list = el.get('Value', [])
        if not isinstance(inner_list, list):
            continue
        for sub in inner_list:
            if not isinstance(sub, dict):
                continue
            v = sub.get('Value', {})
            if isinstance(v, dict):
                ap = v.get('AssetPath', {})
                if isinstance(ap, dict) and ap.get('AssetName') == NPCGOAT_CLASS_PATH:
                    log(f"    NOTE: ValidNpcClasses already contains {NPCGOAT_CLASS_PATH} (idempotent skip)")
                    return True

    if not entries:
        log("    ERROR: ValidNpcClasses array is empty; cannot use first entry as template")
        return False

    template = copy.deepcopy(entries[0])
    # The struct is StructPropertyData{StructType:'SoftClassPath'} containing
    # a list with one SoftClassPathPropertyData. Set its AssetName to BP_NpcGoat_C.
    inner = template.get('Value', [])
    if isinstance(inner, list) and inner and isinstance(inner[0], dict):
        sub = inner[0]
        sub_val = sub.get('Value', {})
        if isinstance(sub_val, dict):
            ap = sub_val.get('AssetPath', {})
            if isinstance(ap, dict):
                ap['AssetName'] = NPCGOAT_CLASS_PATH

    entries.append(template)
    log(f"    ValidNpcClasses += {NPCGOAT_CLASS_PATH}")
    log(f"    ValidNpcClasses count: {len(entries)}")

    # NameMap entries — soft path strings get FName-serialised
    for n in [NPCGOAT_PACKAGE_PATH, NPCGOAT_CLASS_PATH]:
        ensure_namemap_entry(data, n)
    return True


def edit_ai_challenge_spawns(data):
    """Append BP_NpcGoat_C to SurvivorRescue2.CharactersToSpawn map.

    SurvivorRescue2 already spawns BP_NpcDwarf_Survivor_2 + BP_Monster_Wolf
    (wolf attacks survivor, player rescues). Adding the goat as a third
    entry places it at the same world-gen-distributed location in
    3-2 LowerDeeps (per DT_Moria_ZoneChallenges.3-2_LowerDeeps).

    Schema: MapPropertyData with array-of-[Key,Value] pairs.
      Key: SoftObjectPropertyData (TSoftClassPtr<>) carrying AssetName
      Value: UInt32PropertyData (count)
    """
    rows = data['Exports'][0]['Table']['Data']
    target_row = next((r for r in rows if r.get('Name') == 'SurvivorRescue2'), None)
    if target_row is None:
        log("    ERROR: SurvivorRescue2 row not found")
        return False

    map_prop = next((p for p in target_row['Value']
                     if isinstance(p, dict) and p.get('Name') == 'CharactersToSpawn'), None)
    if map_prop is None:
        log("    ERROR: CharactersToSpawn map not found on SurvivorRescue2")
        return False

    entries = map_prop.get('Value', [])
    # Idempotency: check if BP_NpcGoat_C is already in the map
    for pair in entries:
        if isinstance(pair, list) and len(pair) == 2:
            k = pair[0]
            kv = k.get('Value', {}) if isinstance(k, dict) else {}
            ap = kv.get('AssetPath', {}) if isinstance(kv, dict) else {}
            if isinstance(ap, dict) and ap.get('AssetName') == NPCGOAT_CLASS_PATH:
                log("    NOTE: BP_NpcGoat_C already in SurvivorRescue2.CharactersToSpawn (idempotent skip)")
                return True

    if not entries:
        log("    ERROR: CharactersToSpawn map empty; cannot use template")
        return False

    # Clone the first pair as a template and retarget the AssetName
    template = copy.deepcopy(entries[0])
    if isinstance(template, list) and len(template) == 2:
        k = template[0]
        kv = k.get('Value', {})
        ap = kv.get('AssetPath', {})
        ap['AssetName'] = NPCGOAT_CLASS_PATH
        # Set count to 1
        v = template[1]
        v['Value'] = 1

    entries.append(template)
    log(f"    SurvivorRescue2.CharactersToSpawn += {NPCGOAT_CLASS_PATH} (count=1)")
    log(f"    Entry count: {len(entries)} (was {len(entries)-1})")

    # NameMap entries — soft path strings get FName-serialised
    for n in [NPCGOAT_PACKAGE_PATH, NPCGOAT_CLASS_PATH]:
        ensure_namemap_entry(data, n)
    return True


EDIT_FUNCS = {
    'DT_NPCRoles': edit_npcroles,
    'DT_Moria_AI_Population': edit_ai_population,
    'DT_AICharacterSettings': edit_aicharsettings,
    'BP_MoriaGameMode_MainMenu': edit_mainmenu_gamemode,
    'BP_NpcGoat': edit_bp_npcgoat,
    # v1.1.0 Phase 1
    'DT_NPCInventoryPresets': edit_npcinventorypresets,
    'DT_NPCUniqueCharacters': edit_npcuniquecharacters,
    'DT_Storage': edit_dt_storage,
    'DT_ContainerItems': edit_dt_containeritems,
    # v1.1.1 — unblocked by usmap; appends BP_NpcGoat_C to NPCManager whitelist
    'BP_NPCManager': edit_bp_npcmanager,
    # v1.1.2 — co-locate goat with Survivor_2 in 3-2 LowerDeeps
    'DT_Moria_AIChallengeSpawns': edit_ai_challenge_spawns,
}


# ---------------------------------------------------------------------------
# Main build
# ---------------------------------------------------------------------------

def main():
    log(f"=== BuildPorterGoat v{MOD_VERSION} ===\n")

    # ----------------------------------------------------------------- 1
    log("[1/7] Pre-flight checks...")
    errors = []
    for tool_name, tool_path in [('retoc.exe', RETOC_EXE),
                                 ('UAssetGUI.exe', UASSETGUI_EXE)]:
        if not tool_path.exists():
            errors.append(f"  Missing {tool_name}: {tool_path}")
    for src_rel, _, name in DTS:
        src_uasset = LEGACY_ROOT / f'{src_rel}.uasset'
        src_uexp = LEGACY_ROOT / f'{src_rel}.uexp'
        if not src_uasset.exists():
            errors.append(f"  Missing {src_uasset}")
        if not src_uexp.exists():
            errors.append(f"  Missing {src_uexp}")
    if errors:
        for e in errors:
            log(e)
        sys.exit(1)
    log(f"  Sources: {len(DTS)} DataTables\n")

    # ----------------------------------------------------------------- 2
    log("[2/7] Cleaning work dirs...")
    for d in [WORK_DIR, STAGING_DIR, OUTPUT_DIR]:
        rmtree_safe(d)
        d.mkdir(parents=True, exist_ok=True)
    log("  Done.\n")

    # ----------------------------------------------------------------- 3
    log("[3/7] tojson + edit + fromjson...")
    edited_outputs = []  # (modified_uasset, modified_uexp, staging_relpath)

    for src_rel, dst_rel, name in DTS:
        log(f"  --- {name} ---")
        use_usmap = asset_needs_usmap(name)
        if use_usmap:
            log(f"    [usmap=Moria, UAssetGUI=v1.1.0]")

        src_uasset = LEGACY_ROOT / f'{src_rel}.uasset'
        src_uexp = LEGACY_ROOT / f'{src_rel}.uexp'

        work_uasset = WORK_DIR / f'{name}.uasset'
        work_uexp = WORK_DIR / f'{name}.uexp'
        shutil.copy2(src_uasset, work_uasset)
        shutil.copy2(src_uexp, work_uexp)

        work_json = WORK_DIR / f'{name}.json'
        if not run_uassetgui_tojson(work_uasset, work_json, use_usmap=use_usmap):
            log(f"  ERROR: tojson failed for {name}"); sys.exit(1)

        with open(work_json, 'r', encoding='utf-8') as f:
            data = json.load(f)

        edit_fn = EDIT_FUNCS[name]
        if not edit_fn(data):
            log(f"  ERROR: edit failed for {name}"); sys.exit(1)

        modified_json = WORK_DIR / f'{name}_modified.json'
        with open(modified_json, 'w', encoding='utf-8') as f:
            json.dump(data, f, indent=2)

        out_uasset = WORK_DIR / f'{name}_out.uasset'
        if not run_uassetgui_fromjson(modified_json, out_uasset, use_usmap=use_usmap):
            log(f"  ERROR: fromjson failed for {name}"); sys.exit(1)

        out_uexp = out_uasset.with_suffix('.uexp')
        if not (out_uasset.exists() and out_uexp.exists()):
            log(f"  ERROR: fromjson missing output for {name}"); sys.exit(1)

        log(f"    Output: {out_uasset.stat().st_size} + {out_uexp.stat().st_size} bytes")
        edited_outputs.append((out_uasset, out_uexp, dst_rel, name))

    log()

    # ----------------------------------------------------------------- 4
    log("[4/7] Validating round-trip (tojson on the modified output)...")
    for out_uasset, _, _, name in edited_outputs:
        validate_json = WORK_DIR / f'{name}_validate.json'
        if not run_uassetgui_tojson(out_uasset, validate_json, use_usmap=asset_needs_usmap(name)):
            log(f"  ERROR: round-trip validation failed for {name}"); sys.exit(1)
        log(f"  OK: {name}")
    log()

    # ----------------------------------------------------------------- 5
    log("[5/7] Staging modified uassets...")
    for out_uasset, out_uexp, dst_rel, name in edited_outputs:
        dst_dir = STAGING_DIR / 'Moria' / 'Content' / Path(dst_rel).parent
        dst_dir.mkdir(parents=True, exist_ok=True)
        final_uasset = dst_dir / f'{Path(dst_rel).name}.uasset'
        final_uexp = dst_dir / f'{Path(dst_rel).name}.uexp'
        shutil.copy2(out_uasset, final_uasset)
        shutil.copy2(out_uexp, final_uexp)
        log(f"  Staged: Moria/Content/{dst_rel}")

    # v1.1.0 Phase 2 — stage the brand-new BP_ContainerItem_Goat_BodyInventory.
    # This BP is pre-cooked by scripts/CloneGoatBodyInventoryBP.py (one-time
    # authoring) into experiments/portergoat/v110_build/. We just copy it into
    # the pak's staging tree at /Game/Mods/PorterGoat/Items/.
    goat_bi_src_uasset = PROJECT_ROOT / 'experiments' / 'portergoat' / 'v110_build' / 'BP_ContainerItem_Goat_BodyInventory.uasset'
    goat_bi_src_uexp   = goat_bi_src_uasset.with_suffix('.uexp')
    if not (goat_bi_src_uasset.exists() and goat_bi_src_uexp.exists()):
        log(f"  ERROR: missing pre-cooked BP at {goat_bi_src_uasset}")
        log(f"         run scripts/CloneGoatBodyInventoryBP.py first")
        sys.exit(1)
    goat_bi_dst_dir = STAGING_DIR / 'Moria' / 'Content' / 'Mods' / 'PorterGoat' / 'Items'
    goat_bi_dst_dir.mkdir(parents=True, exist_ok=True)
    shutil.copy2(goat_bi_src_uasset, goat_bi_dst_dir / 'BP_ContainerItem_Goat_BodyInventory.uasset')
    shutil.copy2(goat_bi_src_uexp,   goat_bi_dst_dir / 'BP_ContainerItem_Goat_BodyInventory.uexp')
    log(f"  Staged: Moria/Content/Mods/PorterGoat/Items/BP_ContainerItem_Goat_BodyInventory")
    log()

    # ----------------------------------------------------------------- 6
    log("[6/7] Building IoStore pak with retoc to-zen...")
    if not run_retoc_tozen(STAGING_DIR, OUTPUT_DIR, PAK_NAME):
        log("  ERROR: retoc to-zen failed"); sys.exit(1)

    triplet = [
        OUTPUT_DIR / f'{PAK_NAME}.pak',
        OUTPUT_DIR / f'{PAK_NAME}.ucas',
        OUTPUT_DIR / f'{PAK_NAME}.utoc',
    ]
    for f in triplet:
        if not f.exists():
            log(f"  ERROR: missing {f.name}"); sys.exit(1)
        log(f"  {f.name}: {f.stat().st_size:,} bytes")

    # retoc list sanity check
    list_cmd = [str(RETOC_EXE), 'list', str(triplet[2])]
    r = subprocess.run(list_cmd, capture_output=True, text=True, timeout=60)
    if r.returncode == 0:
        lines = [l for l in r.stdout.strip().split('\n') if l.strip()]
        export_count = sum(1 for l in lines if 'ExportBundleData' in l)
        # v1.1.1 had 11; v1.1.2 adds DT_Moria_AIChallengeSpawns override = 12 total
        log(f"  ExportBundleData entries: {export_count} (expected 12 for v1.1.2)")
    log()

    # ----------------------------------------------------------------- 7
    log("[7/7] Creating distribution zip...")
    DOWNLOADS_DIR.mkdir(parents=True, exist_ok=True)
    zip_path = DOWNLOADS_DIR / f'PorterGoat_v{MOD_VERSION}.zip'
    with zipfile.ZipFile(zip_path, 'w', zipfile.ZIP_DEFLATED) as zf:
        for f in triplet:
            zf.write(f, f.name)
            log(f"  Added: {f.name}")
    log(f"\n  Output: {zip_path} ({zip_path.stat().st_size:,} bytes)")

    # ------------------------------------------------------------- summary
    log(f"\n{'='*60}")
    log(f"  PorterGoat v{MOD_VERSION} -- BUILD SUCCESSFUL")
    log(f"  Carried-forward edits from v1.0.5:")
    log(f"    - DT_NPCRoles: Porter Disabled -> Live  (+ label cleanup in v1.1.0)")
    log(f"    - DT_Moria_AI_Population: +1 row 'NpcGoat'")
    log(f"    - DT_AICharacterSettings: +1 row 'NpcGoat'")
    log(f"    - BP_MoriaGameMode_MainMenu: DefaultPawnClass -> BP_NpcGoat_C (load anchor)")
    log(f"    - BP_NpcGoat: EquipComp.DummyEquipment = AdventurersPack_Large (dormant)")
    log(f"  v1.1.0 Phase 1 — proper-NPC registration:")
    log(f"    - DT_NPCRoles: Porter labels cleaned ('*[Bug this]' removed)")
    log(f"    - DT_NPCInventoryPresets: +1 row 'Porter' (cloned from EmptyLoadout)")
    log(f"    - DT_NPCUniqueCharacters: +1 row 'PorterGoat' -> BP_NpcGoat_C")
    log(f"    - DT_Storage: +1 row 'Goat.BodyInventory' (8x8, no weapon slots)")
    log(f"    - DT_ContainerItems: +1 row 'Goat.BodyInventory'")
    log(f"  v1.1.0 Phase 2 — goat 8x8 inventory wrapper:")
    log(f"    - NEW: BP_ContainerItem_Goat_BodyInventory at /Game/Mods/PorterGoat/Items/")
    log(f"    - BP_NpcGoat: InventoryComp.DefaultContainers += [Goat.BodyInventory wrapper]")
    log(f"  v1.1.1 — UNBLOCKED via Moria usmap:")
    log(f"    - BP_NPCManager.ValidNpcClasses += BP_NpcGoat_C")
    log(f"      (uses UAssetGUI v1.1.0 + Moria.usmap from UE4SS dumper)")
    log(f"      Save persistence: goat now passes ValidNpcClasses filter on save loop.")
    log(f"  v1.1.2 — world-placed goat in Lower Deeps:")
    log(f"    - DT_Moria_AIChallengeSpawns.SurvivorRescue2.CharactersToSpawn")
    log(f"      += BP_NpcGoat_C  (spawns alongside Survivor_2 + Wolf in 3-2 LowerDeeps)")
    log(f"  v1.1.3 — interaction prompts on goat:")
    log(f"    - BP_NpcGoat.MorNPC.bRescueInteractionEnabled = true")
    log(f"    - BP_NpcGoat.MorNPC.bManageInteractionEnabled = true")
    log(f"    - BP_NpcGoat.MorNPC.bInteractionEnabled = true (master)")
    log(f"      Pre-rescue: E shows 'Rescue' prompt")
    log(f"      Post-rescue: E shows 'Manage Goat' prompt")
    log(f"  Pak: {PAK_NAME}")
    log(f"  Zip: {zip_path}")
    log(f"  Install: extract zip to <game>/Moria/Content/Paks/~mods/")
    log(f"{'='*60}")


if __name__ == '__main__':
    main()
