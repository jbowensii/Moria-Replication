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

MOD_VERSION = '1.2.11'
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
    # v1.2.7: BP_MoriaGameMode_MainMenu RESTORED. v1.2.6 dropped BP_NpcGoat_C
    # from BP_NPCManager.ValidNpcClasses to kill the random-dwarf-at-camp bug,
    # but ValidNpcClasses was ALSO acting as the eager class-load anchor for
    # BP_NpcGoat_C. Without it, the SurvivorRescue2 challenge fails to spawn
    # the goat (class isn't loaded) and falls back to a default dwarf.
    # MainMenu DefaultPawnClass override is a pure load anchor with no
    # tracked-companion side effects, exactly what we need.
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
    # v1.2.10 — bytecode constant-replacement patch on the rescue-dispatcher
    # whitelist gate. HandleOnNpcRescued (and SandboxHandleOnNpcRescued) check
    # GetObjectClass(npcChar) against BP_NpcDwarf_Wanderer_RecruitAndSettlement_C
    # and BP_NpcDwarf_Recruit_C; if neither matches, the goat takes a silent
    # fallthrough path and DespawnRecruitedWanderer never fires. We swap the
    # -34 (BP_NpcDwarf_Recruit_C) references for BP_NpcGoat_C.
    ('Tech/Managers/BP_StoryManager',
     'Tech/Managers/BP_StoryManager',
     'BP_StoryManager'),
    # v1.2.11 — patch the camp recruit spawner's hardcoded class from
    # BP_NpcDwarf_Wanderer_RecruitAndSettlement_C to BP_NpcGoat_C. Empirical
    # test of Model alpha (data-record save with class-flexible-apply).
    # When player rescues first wanderer at Dimrill Dale, this spawner fires
    # and creates a permanent actor at camp. Swapping the soft class ref
    # changes WHAT class spawns -- if Model alpha is correct, the C++ side
    # then writes the resident record applying its data to whichever class
    # the spawner creates.
    ('LevelDesign/Challenges/DwarfStorySpawners/BP_StoryNpcSpawner_Wanderer_RecruitCamp',
     'LevelDesign/Challenges/DwarfStorySpawners/BP_StoryNpcSpawner_Wanderer_RecruitCamp',
     'BP_StoryNpcSpawner_Wanderer_RecruitCamp'),
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
    return name in ('BP_NPCManager', 'BP_StoryManager')


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


def _find_existing_import(imports, object_name, class_name=None, class_package=None):
    """Return negative-1-based index of import matching name+optionally class. None if absent."""
    for i, imp in enumerate(imports):
        if imp.get('ObjectName') != object_name:
            continue
        if class_name is not None and imp.get('ClassName') != class_name:
            continue
        if class_package is not None and imp.get('ClassPackage') != class_package:
            continue
        return -(i + 1)
    return None


def _add_morwanderer_scs(data):
    """v1.2.8: SCS surgery — add MorWandererComponent to BP_NpcGoat's component
    tree as a fresh (non-inherited) SCS_Node.

    HIGH RISK. Adds 2 imports + 2 exports + 2 array entries + dependency wiring
    on SimpleConstructionScript_0. Round-trip validation required.

    Returns True on success, False if any required precondition isn't met.

    Inert-by-design: this surgery only registers the component on the goat
    actor. Wiring its events (BeginPlay subscription, OnInteract → recruit
    dialogue, despawn) requires Blueprint event-graph editing which UAssetGUI
    cannot do. Per VS-Claude's Path B: runtime mod is responsible for the
    actual rescue logic. This addition gives runtime a real
    MorWandererComponent to bind handlers onto.
    """
    log("    --- SCS surgery: add MorWandererComponent ---")

    imports = data['Imports']
    exports = data['Exports']

    # ---- Idempotency guard ----------------------------------------------
    existing = _find_existing_import(imports, 'MorWandererComponent',
                                     class_name='Class',
                                     class_package='/Script/CoreUObject')
    if existing is not None:
        log(f"    NOTE: MorWandererComponent class import already at {existing} (idempotent skip)")
        return True

    # ---- Step 1: locate /Script/Moria package import --------------------
    moria_pkg_idx = _find_existing_import(imports, '/Script/Moria',
                                          class_name='Package',
                                          class_package='/Script/CoreUObject')
    if moria_pkg_idx is None:
        log("    ERROR: /Script/Moria package import not found")
        return False
    log(f"    /Script/Moria pkg import at {moria_pkg_idx}")

    # ---- Step 2: locate SCS_Node import + Default__SCS_Node template ----
    scs_node_class_idx = _find_existing_import(imports, 'SCS_Node',
                                               class_name='Class',
                                               class_package='/Script/CoreUObject')
    scs_node_template_idx = _find_existing_import(imports, 'Default__SCS_Node',
                                                  class_name='SCS_Node')
    if scs_node_class_idx is None or scs_node_template_idx is None:
        log(f"    ERROR: SCS_Node imports missing (class={scs_node_class_idx} tmpl={scs_node_template_idx})")
        return False
    log(f"    SCS_Node imports: class={scs_node_class_idx} template={scs_node_template_idx}")

    # ---- Step 3: locate BP class export + SimpleConstructionScript_0 ----
    bp_class_export_idx = None  # 1-based positive
    scs_export_idx = None
    for i, exp in enumerate(exports):
        on = exp.get('ObjectName', '')
        if on == 'BP_NpcGoat_C':
            bp_class_export_idx = i + 1
        elif on == 'SimpleConstructionScript_0':
            scs_export_idx = i + 1
    if bp_class_export_idx is None or scs_export_idx is None:
        log(f"    ERROR: BP class or SCS export missing (bp={bp_class_export_idx} scs={scs_export_idx})")
        return False
    log(f"    BP class export at {bp_class_export_idx}, SCS at {scs_export_idx}")

    # ---- Step 4: add MorWandererComponent class import ------------------
    cls_import = {
        '$type': 'UAssetAPI.Import, UAssetAPI',
        'ObjectName': 'MorWandererComponent',
        'OuterIndex': moria_pkg_idx,
        'ClassPackage': '/Script/CoreUObject',
        'ClassName': 'Class',
        'PackageName': None,
        'bImportOptional': False,
    }
    imports.append(cls_import)
    morwanderer_cls_idx = -len(imports)
    log(f"    + Class import at {morwanderer_cls_idx}: MorWandererComponent")

    # ---- Step 5: add Default__MorWandererComponent template import ------
    tmpl_import = {
        '$type': 'UAssetAPI.Import, UAssetAPI',
        'ObjectName': 'Default__MorWandererComponent',
        'OuterIndex': moria_pkg_idx,
        'ClassPackage': '/Script/Moria',
        'ClassName': 'MorWandererComponent',
        'PackageName': None,
        'bImportOptional': False,
    }
    imports.append(tmpl_import)
    morwanderer_tmpl_idx = -len(imports)
    log(f"    + Template import at {morwanderer_tmpl_idx}: Default__MorWandererComponent")

    # ---- Step 6: add MorWanderer_GEN_VARIABLE export --------------------
    # Cloned shape from MorNPC_GEN_VARIABLE; OuterIndex points at BP class.
    # Empty Data array — component uses C++ defaults. (BP authors set fields
    # like RecruitInteraction here, but we want minimum surface area to keep
    # round-trip validation tight.)
    gen_var_export = {
        '$type': 'UAssetAPI.ExportTypes.NormalExport, UAssetAPI',
        'Data': [],
        'ObjectGuid': None,
        'SerializationControl': 'NoExtension',
        'Operation': 'None',
        'HasLeadingFourNullBytes': False,
        'ObjectName': 'MorWanderer_GEN_VARIABLE',
        'OuterIndex': bp_class_export_idx,
        'ClassIndex': morwanderer_cls_idx,
        'SuperIndex': 0,
        'TemplateIndex': morwanderer_tmpl_idx,
        'ObjectFlags': 'RF_Public, RF_Transactional, RF_ArchetypeObject',
        'SerialSize': 0,           # serializer recomputes
        'SerialOffset': 0,         # serializer recomputes
        'ScriptSerializationStartOffset': 0,
        'ScriptSerializationEndOffset': 0,
        'bForcedExport': False,
        'bNotForClient': False,
        'bNotForServer': False,
        'PackageGuid': '{00000000-0000-0000-0000-000000000000}',
        'IsInheritedInstance': False,
        'PackageFlags': 'PKG_None',
        'bNotAlwaysLoadedForEditorGame': False,
        'bIsAsset': False,
        'GeneratePublicHash': False,
        'SerializationBeforeSerializationDependencies': [],
        'CreateBeforeSerializationDependencies': [],
        'SerializationBeforeCreateDependencies': [
            morwanderer_cls_idx,
            morwanderer_tmpl_idx,
        ],
        'CreateBeforeCreateDependencies': [
            bp_class_export_idx,
        ],
        'Extras': '',
    }
    exports.append(gen_var_export)
    gen_var_idx = len(exports)  # 1-based positive
    log(f"    + Export at {gen_var_idx}: MorWanderer_GEN_VARIABLE (outer={bp_class_export_idx})")

    # ---- Step 7: add new SCS_Node export --------------------------------
    # Use SCS_Node_29 (next after existing 28).
    # Determine current max SCS_Node index by scanning exports.
    max_scs_idx = -1
    for exp in exports:
        on = exp.get('ObjectName', '')
        if on.startswith('SCS_Node_'):
            try:
                n = int(on.split('_')[-1])
                if n > max_scs_idx:
                    max_scs_idx = n
            except ValueError:
                continue
    new_scs_idx = max_scs_idx + 1
    new_scs_name = f'SCS_Node_{new_scs_idx}'

    # Generate a stable VariableGuid (deterministic, not random — round-trip
    # friendly). UE5 GUID format is brace-delimited uppercase hex with dashes.
    # Pattern: ABCDEF01-2345-6789-ABCD-EF0123456789
    variable_guid = '{12345678-9ABC-DEF0-1234-56789ABCDEF0}'

    scs_node_export = {
        '$type': 'UAssetAPI.ExportTypes.NormalExport, UAssetAPI',
        'Data': [
            {
                '$type': 'UAssetAPI.PropertyTypes.Objects.ObjectPropertyData, UAssetAPI',
                'Name': 'ComponentClass',
                'ArrayIndex': 0,
                'PropertyGuid': None,
                'IsZero': False,
                'PropertyTagFlags': 'None',
                'PropertyTypeName': None,
                'PropertyTagExtensions': 'NoExtension',
                'Value': morwanderer_cls_idx,
            },
            {
                '$type': 'UAssetAPI.PropertyTypes.Objects.ObjectPropertyData, UAssetAPI',
                'Name': 'ComponentTemplate',
                'ArrayIndex': 0,
                'PropertyGuid': None,
                'IsZero': False,
                'PropertyTagFlags': 'None',
                'PropertyTypeName': None,
                'PropertyTagExtensions': 'NoExtension',
                'Value': gen_var_idx,
            },
            {
                '$type': 'UAssetAPI.PropertyTypes.Structs.StructPropertyData, UAssetAPI',
                'StructType': 'Guid',
                'SerializeNone': True,
                'StructGUID': '{00000000-0000-0000-0000-000000000000}',
                'SerializationControl': 'NoExtension',
                'Operation': 'None',
                'Name': 'VariableGuid',
                'ArrayIndex': 0,
                'PropertyGuid': None,
                'IsZero': False,
                'PropertyTagFlags': 'None',
                'PropertyTypeName': None,
                'PropertyTagExtensions': 'NoExtension',
                'Value': [
                    {
                        '$type': 'UAssetAPI.PropertyTypes.Structs.GuidPropertyData, UAssetAPI',
                        'Name': 'VariableGuid',
                        'ArrayIndex': 0,
                        'PropertyGuid': None,
                        'IsZero': False,
                        'PropertyTagFlags': 'None',
                        'PropertyTypeName': None,
                        'PropertyTagExtensions': 'NoExtension',
                        'Value': variable_guid,
                    }
                ],
            },
            {
                '$type': 'UAssetAPI.PropertyTypes.Objects.NamePropertyData, UAssetAPI',
                'Name': 'InternalVariableName',
                'ArrayIndex': 0,
                'PropertyGuid': None,
                'IsZero': False,
                'PropertyTagFlags': 'None',
                'PropertyTypeName': None,
                'PropertyTagExtensions': 'NoExtension',
                'Value': 'MorWanderer',
            },
        ],
        'ObjectGuid': None,
        'SerializationControl': 'NoExtension',
        'Operation': 'None',
        'HasLeadingFourNullBytes': False,
        'ObjectName': new_scs_name,
        'OuterIndex': scs_export_idx,
        'ClassIndex': scs_node_class_idx,
        'SuperIndex': 0,
        'TemplateIndex': scs_node_template_idx,
        'ObjectFlags': 'RF_Transactional',
        'SerialSize': 0,
        'SerialOffset': 0,
        'ScriptSerializationStartOffset': 0,
        'ScriptSerializationEndOffset': 0,
        'bForcedExport': False,
        'bNotForClient': False,
        'bNotForServer': False,
        'PackageGuid': '{00000000-0000-0000-0000-000000000000}',
        'IsInheritedInstance': False,
        'PackageFlags': 'PKG_None',
        'bNotAlwaysLoadedForEditorGame': False,
        'bIsAsset': False,
        'GeneratePublicHash': False,
        'SerializationBeforeSerializationDependencies': [],
        'CreateBeforeSerializationDependencies': [
            gen_var_idx,
        ],
        'SerializationBeforeCreateDependencies': [
            scs_node_class_idx,
            scs_node_template_idx,
        ],
        'CreateBeforeCreateDependencies': [
            scs_export_idx,
        ],
        'Extras': '',
    }
    exports.append(scs_node_export)
    new_scs_node_idx = len(exports)  # 1-based positive
    log(f"    + Export at {new_scs_node_idx}: {new_scs_name}")

    # ---- Step 8: append to SimpleConstructionScript_0.RootNodes + AllNodes
    scs_export = exports[scs_export_idx - 1]
    scs_data = scs_export.get('Data', [])

    def _append_to_array_prop(prop_name, ref_export_idx):
        prop = next((p for p in scs_data
                     if isinstance(p, dict) and p.get('Name') == prop_name), None)
        if prop is None:
            log(f"    ERROR: {prop_name} property not found on SimpleConstructionScript_0")
            return False
        arr = prop.get('Value', [])
        next_name = str(len(arr))
        arr.append({
            '$type': 'UAssetAPI.PropertyTypes.Objects.ObjectPropertyData, UAssetAPI',
            'Name': next_name,
            'ArrayIndex': 0,
            'PropertyGuid': None,
            'IsZero': False,
            'PropertyTagFlags': 'None',
            'PropertyTypeName': None,
            'PropertyTagExtensions': 'NoExtension',
            'Value': ref_export_idx,
        })
        log(f"    SimpleConstructionScript_0.{prop_name}[{next_name}] = {ref_export_idx}")
        return True

    if not _append_to_array_prop('RootNodes', new_scs_node_idx):
        return False
    if not _append_to_array_prop('AllNodes', new_scs_node_idx):
        return False

    # ---- Step 9: SimpleConstructionScript_0 must serialize the new SCS_Node
    # before itself; add to CreateBeforeSerializationDependencies.
    cbsd = scs_export.get('CreateBeforeSerializationDependencies', [])
    if new_scs_node_idx not in cbsd:
        cbsd.append(new_scs_node_idx)
    scs_export['CreateBeforeSerializationDependencies'] = cbsd

    # ---- Step 10: NameMap entries ---------------------------------------
    namemap_adds = [
        'MorWandererComponent',
        'Default__MorWandererComponent',
        'MorWanderer_GEN_VARIABLE',
        'MorWanderer',
        new_scs_name,
        'ComponentClass',
        'ComponentTemplate',
        'VariableGuid',
        'InternalVariableName',
    ]
    for n in namemap_adds:
        ensure_namemap_entry(data, n)

    log(f"    SCS surgery complete: +2 imports, +2 exports, +2 array entries")
    return True


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
    """Single BP_NpcGoat CDO edit (v1.2.0):

    InventoryComp.DefaultContainers -> [BP_ContainerItem_Goat_BodyInventory_C]
       (gives the goat its 8x8 BodyInventory grid via the wrapper BP)

    Dropped vs prior versions:
      - v1.0.5 EquipComp.DummyEquipment override (always dormant; never fired
        the auto-attach we hoped for)
      - v1.1.3 MorNPC bool flags (bRescueInteractionEnabled etc.) — VS-Claude
        runtime trace showed the bools alone don't surface a working rescue;
        the per-instance Blueprint event handler OnNpcRescued_Event_2 is what
        actually flips state, and bytecode injection is beyond UAssetGUI.
    """
    # InventoryComp.DefaultContainers override
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
    # v1.2.3: dead-code cleanup. v1.2.1 attempted CDO overrides on
    # bIsRescued=false and bRescueInteractionEnabled=true. Per VS-Claude
    # runtime probe (2026-05-10):
    #   - bIsRescued is NOT a UPROPERTY (native-only field) → CDO edit
    #     was silently ignored
    #   - bRescueInteractionEnabled = true at runtime by default already
    # Both overrides removed. The Rescue prompt gate is OnNpcRescued
    # delegate subscription on AMorSettlementManager (off=0x2F8), which
    # cannot be replicated via CDO — runtime mod handles it via raw
    # FScriptDelegate append at goat spawn.
    morpc_export = next((e for e in data.get('Exports', [])
                         if e.get('ObjectName') == 'MorNPC_GEN_VARIABLE'), None)
    if morpc_export is None:
        morpc_export = next((e for e in data.get('Exports', [])
                             if e.get('ObjectName') == 'MorNPC'), None)
    if morpc_export is None:
        log("    WARN: MorNPC component export not found — skipping field clone")
        return True
    morpc_data = morpc_export.setdefault('Data', [])

    # ---------------------------------------------------------------- (4)
    # v1.2.2: clone the 8 MorNPC fields that BP_NpcDwarf has but BP_NpcGoat
    # lacks. Goat MorNPC override has only 3 interaction structs (Manage,
    # Revive, Rescue). Dwarf has 7 interaction structs + 4 non-struct fields.
    # Hypothesis: prompt arbitration on MorNPCComponent picks among
    # registered MorInteraction structs by SortPriority; without
    # DetailsInteraction (SortPriority=1) and TalkInteraction (SortPriority=4)
    # registered, Manage (no SortPriority -> 0) wins over Rescue when both
    # are eligible. Cloning dwarf's full set normalizes the priority space.
    #
    # Source-of-truth values transcribed from
    # experiments/portergoat/preflight/BP_NpcDwarf_with_usmap.json (lines
    # 15546-15915). All 4 interaction structs reference StringTable
    # /Game/Tech/Data/StringTables/UI.UI which is already loaded by the goat
    # asset (it lives in NameMap), so no new imports are required.
    #
    # NameMap entries needed:
    UI_TABLE = '/Game/Tech/Data/StringTables/UI.UI'
    namemap_adds = [
        UI_TABLE,
        'RecruitInteraction', 'DeliverResearchInteraction',
        'DetailsInteraction', 'TalkInteraction',
        'RecruitNPCWorldCapReachedText', 'ActivityPointGainedEffect',
        'SoftMugAsset', 'BarkWhitelistTag',
        'SortPriority', 'EnabledTextFormat', 'DisabledTextFormat',
        'HUD.NPC.RecruitCoins', 'HUD.NPC.Collect',
        'HUD.NPC.Details', 'HUD.NPC.Talk',
        'HUD.NPC.RecruitCapReached',
        '/Game/FX/HonorRemains/Niagara/NS_HonorRemains_NPC.NS_HonorRemains_NPC',
        '/Game/Items/BP_MorContainerItem_Mug.BP_MorContainerItem_Mug_C',
        'GameplayTagContainer',
        'AI.Behavior.RecTime', 'AI.Behavior.WorkTime',
        'MorInteraction', 'IntProperty', 'TextProperty',
        'SoftObjectProperty',
    ]
    for n in namemap_adds:
        ensure_namemap_entry(data, n)

    def _text_prop(name, value):
        return {
            '$type': 'UAssetAPI.PropertyTypes.Objects.TextPropertyData, UAssetAPI',
            'Flags': 0,
            'HistoryType': 'StringTableEntry',
            'TableId': UI_TABLE,
            'Namespace': None,
            'CultureInvariantString': None,
            'SourceFmt': None,
            'Arguments': None,
            'ArgumentsData': None,
            'TransformType': 'ToLower',
            'SourceValue': None,
            'FormatOptions': None,
            'TargetCulture': None,
            'Name': name,
            'ArrayIndex': 0,
            'PropertyGuid': None,
            'IsZero': False,
            'PropertyTagFlags': 'None',
            'PropertyTypeName': None,
            'PropertyTagExtensions': 'NoExtension',
            'Value': value,
        }

    def _int_prop(name, value):
        return {
            '$type': 'UAssetAPI.PropertyTypes.Objects.IntPropertyData, UAssetAPI',
            'Name': name,
            'ArrayIndex': 0,
            'PropertyGuid': None,
            'IsZero': False,
            'PropertyTagFlags': 'None',
            'PropertyTypeName': None,
            'PropertyTagExtensions': 'NoExtension',
            'Value': value,
        }

    def _interaction(name, sort_priority, enabled, disabled):
        inner = []
        if sort_priority is not None:
            inner.append(_int_prop('SortPriority', sort_priority))
        inner.append(_text_prop('EnabledTextFormat', enabled))
        inner.append(_text_prop('DisabledTextFormat', disabled))
        return {
            '$type': 'UAssetAPI.PropertyTypes.Structs.StructPropertyData, UAssetAPI',
            'StructType': 'MorInteraction',
            'SerializeNone': True,
            'StructGUID': '{00000000-0000-0000-0000-000000000000}',
            'SerializationControl': 'NoExtension',
            'Operation': 'None',
            'Name': name,
            'ArrayIndex': 0,
            'PropertyGuid': None,
            'IsZero': False,
            'PropertyTagFlags': 'None',
            'PropertyTypeName': None,
            'PropertyTagExtensions': 'NoExtension',
            'Value': inner,
        }

    def _soft_obj(name, asset_path):
        return {
            '$type': 'UAssetAPI.PropertyTypes.Objects.SoftObjectPropertyData, UAssetAPI',
            'Name': name,
            'ArrayIndex': 0,
            'PropertyGuid': None,
            'IsZero': False,
            'PropertyTagFlags': 'None',
            'PropertyTypeName': None,
            'PropertyTagExtensions': 'NoExtension',
            'Value': {
                '$type': 'UAssetAPI.PropertyTypes.Objects.FSoftObjectPath, UAssetAPI',
                'AssetPath': {
                    '$type': 'UAssetAPI.PropertyTypes.Objects.FTopLevelAssetPath, UAssetAPI',
                    'PackageName': None,
                    'AssetName': asset_path,
                },
                'SubPathString': None,
            },
        }

    def _bark_whitelist():
        return {
            '$type': 'UAssetAPI.PropertyTypes.Structs.StructPropertyData, UAssetAPI',
            'StructType': 'GameplayTagContainer',
            'SerializeNone': True,
            'StructGUID': '{00000000-0000-0000-0000-000000000000}',
            'SerializationControl': 'NoExtension',
            'Operation': 'None',
            'Name': 'BarkWhitelistTag',
            'ArrayIndex': 0,
            'PropertyGuid': None,
            'IsZero': False,
            'PropertyTagFlags': 'None',
            'PropertyTypeName': None,
            'PropertyTagExtensions': 'NoExtension',
            'Value': [
                {
                    '$type': 'UAssetAPI.PropertyTypes.Structs.GameplayTagContainerPropertyData, UAssetAPI',
                    'Name': 'BarkWhitelistTag',
                    'ArrayIndex': 0,
                    'PropertyGuid': None,
                    'IsZero': False,
                    'PropertyTagFlags': 'None',
                    'PropertyTypeName': None,
                    'PropertyTagExtensions': 'NoExtension',
                    'Value': [
                        'AI.Behavior.RecTime',
                        'AI.Behavior.WorkTime',
                    ],
                }
            ],
        }

    new_fields = [
        _interaction('RecruitInteraction',         None, 'HUD.NPC.RecruitCoins', 'HUD.NPC.RecruitCoins'),
        _interaction('DeliverResearchInteraction', 2,    'HUD.NPC.Collect',      'HUD.NPC.Collect'),
        _interaction('DetailsInteraction',         1,    'HUD.NPC.Details',      'HUD.NPC.Details'),
        _interaction('TalkInteraction',            4,    'HUD.NPC.Talk',         'HUD.NPC.Talk'),
        _text_prop('RecruitNPCWorldCapReachedText', 'HUD.NPC.RecruitCapReached'),
        _soft_obj('ActivityPointGainedEffect',
                  '/Game/FX/HonorRemains/Niagara/NS_HonorRemains_NPC.NS_HonorRemains_NPC'),
        _soft_obj('SoftMugAsset',
                  '/Game/Items/BP_MorContainerItem_Mug.BP_MorContainerItem_Mug_C'),
        _bark_whitelist(),
    ]

    for prop in new_fields:
        fname = prop['Name']
        if any(isinstance(p, dict) and p.get('Name') == fname for p in morpc_data):
            log(f"    NOTE: MorNPC.{fname} already present (skip)")
            continue
        morpc_data.append(prop)
        log(f"    MorNPC.{fname}  (cloned from BP_NpcDwarf)")

    # ---------------------------------------------------------------- (5)
    # v1.2.8: SCS surgery — add MorWandererComponent to BP_NpcGoat's tree.
    # v1.2.10: TEMPORARILY DISABLED. The SCS surgery added cross-package
    # IoStore dependencies that conflict with v1.2.10's BP_StoryManager
    # bytecode patch (retoc to-zen fails with "Failed to find export ...
    # SimpleConstructionScript_0 dependency Serialize in BP_NpcGoat").
    # The dispatcher whitelist patch in BP_StoryManager is the actual fix
    # for the rescue-routing bug; the SCS surgery was inert (per VS-Claude
    # probe — the component has no event-graph wiring). Disabling here to
    # unblock the v1.2.10 ship; revisit if a cleaner co-existence is
    # possible.
    # if not _add_morwanderer_scs(data):
    #     log("    WARN: SCS surgery failed; v1.2.8 will lack MorWandererComponent")
    log("    NOTE: SCS surgery DISABLED in v1.2.10 (conflicts with BP_StoryManager patch)")

    return True


def edit_bp_npcmanager(data):
    """v1.2.9: RESTORED. Append BP_NpcGoat_C to ValidNpcClasses CDO array.

    Per VS-Claude runtime probe 2026-05-10: ServerSendNpcToSettlement(goatGuid)
    misroutes to a dwarf because the server-side roster doesn't recognize
    BP_NpcGoat_C as a valid NPC class. The whitelist needs the goat back.

    The original v1.1.x side effect (random dwarf at camp / "(E) Manage Goat"
    prompt) was caused by ValidNpcClasses being whitelisted WITHOUT a real
    MorWandererComponent on the goat — server tried to resolve the
    whitelisted class to a wanderer instance, couldn't find one, fell back
    to a generic dwarf. v1.2.8 added MorWandererComponent via SCS surgery,
    so the resolver should now find the actual goat actor.

    If the regression returns, fallback is Option B (Dumper-7 + UE editor
    for BP graph node injection) or Option C (alternate registration API
    from runtime side).

    The 'Manager' class uses UnversionedProperties — without the Moria usmap,
    the CDO is a RawExport blob and unmodifiable. With the usmap loaded,
    ValidNpcClasses surfaces as `TArray<TSoftClassPath>` (12 dwarf entries).
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


DWARF_SURVIVOR_2_CLASS_PATH = '/Game/Character/NpcDwarf/BP_NpcDwarf_Survivor_2.BP_NpcDwarf_Survivor_2_C'
MONSTER_WOLF_CLASS_PATH     = '/Game/Character/Creatures/Wolf/BP_Monster_Wolf.BP_Monster_Wolf_C'


def edit_ai_challenge_spawns(data):
    """Replace dwarf survivor with goat in SurvivorRescue2.CharactersToSpawn.

    v1.2.4: Per user direction, remove BP_NpcDwarf_Survivor_2_C from the
    encounter so only the goat (and the wolf threat) spawn. The dwarf
    survivor's per-instance OnNpcRescued_Event_2 handler was catching the
    goat's rescue broadcast and (mis-)completing his own rescue goal in
    v1.2.3. Removing the dwarf eliminates the cross-talk subscriber
    entirely; the goat is the only NPC in the encounter that responds to
    the rescue interaction.

    Net change to CharactersToSpawn map:
      BEFORE (v1.2.3): {Dwarf_Survivor_2: 1, Monster_Wolf: 1, NpcGoat: 1}
      v1.2.4         : {Monster_Wolf: 1, NpcGoat: 1}      (dwarf removed)
      AFTER  (v1.2.5): {NpcGoat: 1}                       (wolf removed too)

    Wolf removed in v1.2.5 — was attacking the goat (non-combatant).
    Goat now stands alone in 3-2 LowerDeeps, peaceful encounter.

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

    def _entry_class_path(pair):
        if not isinstance(pair, list) or len(pair) != 2:
            return None
        k = pair[0]
        kv = k.get('Value', {}) if isinstance(k, dict) else {}
        ap = kv.get('AssetPath', {}) if isinstance(kv, dict) else {}
        return ap.get('AssetName') if isinstance(ap, dict) else None

    before = len(entries)

    # Save a template pair BEFORE any removals (in case we strip the map empty)
    template_seed = copy.deepcopy(entries[0]) if entries else None

    # ---- (1) Remove the dwarf survivor and wolf entries ---------------
    REMOVE_PATHS = [DWARF_SURVIVOR_2_CLASS_PATH, MONSTER_WOLF_CLASS_PATH]
    for rm_path in REMOVE_PATHS:
        rm_idxs = [i for i, p in enumerate(entries)
                   if _entry_class_path(p) == rm_path]
        if rm_idxs:
            for i in reversed(rm_idxs):  # delete back-to-front
                del entries[i]
            log(f"    SurvivorRescue2.CharactersToSpawn -- {rm_path} (removed {len(rm_idxs)} entry)")
        else:
            log(f"    NOTE: {rm_path} not found in map (already removed?)")

    # ---- (2) Ensure goat is in the map (idempotent) -------------------
    has_goat = any(_entry_class_path(p) == NPCGOAT_CLASS_PATH for p in entries)
    if has_goat:
        log("    NOTE: BP_NpcGoat_C already in SurvivorRescue2.CharactersToSpawn (idempotent skip)")
    else:
        if template_seed is None:
            log("    ERROR: CharactersToSpawn map empty and no template available")
            return False
        template = copy.deepcopy(template_seed)
        if isinstance(template, list) and len(template) == 2:
            k = template[0]
            kv = k.get('Value', {})
            ap = kv.get('AssetPath', {})
            ap['AssetName'] = NPCGOAT_CLASS_PATH
            v = template[1]
            v['Value'] = 1
        entries.append(template)
        log(f"    SurvivorRescue2.CharactersToSpawn += {NPCGOAT_CLASS_PATH} (count=1)")

    after = len(entries)
    log(f"    Entry count: {after} (was {before})")

    # NameMap entries — soft path strings get FName-serialised
    for n in [NPCGOAT_PACKAGE_PATH, NPCGOAT_CLASS_PATH]:
        ensure_namemap_entry(data, n)
    return True


BP_NPC_DWARF_RECRUIT_IMPORT_NAME = 'BP_NpcDwarf_Recruit_C'


def _find_import_index_by_name(imports, object_name):
    """Return negative-1-based index of import whose ObjectName matches, or None."""
    for i, imp in enumerate(imports):
        if imp.get('ObjectName') == object_name:
            return -(i + 1)
    return None


def _walk_and_swap_objectconst(node, old_value, new_value, path=None, hits=None):
    """Recursively walk a dict/list tree, find any
    {"$type": "...EX_ObjectConst...", "Value": old_value} dicts
    and replace Value with new_value. Returns count of swaps.
    """
    if hits is None:
        hits = [0]
    if isinstance(node, dict):
        t = node.get('$type', '')
        if 'EX_ObjectConst' in t and node.get('Value') == old_value:
            node['Value'] = new_value
            hits[0] += 1
        for v in node.values():
            _walk_and_swap_objectconst(v, old_value, new_value, path, hits)
    elif isinstance(node, list):
        for v in node:
            _walk_and_swap_objectconst(v, old_value, new_value, path, hits)
    return hits[0]


def edit_bp_storymanager(data):
    """v1.2.10: Bytecode constant-replacement on the rescue-dispatcher
    whitelist gate.

    Per VS-Claude runtime probe 2026-05-10 (post v1.2.9):
      vanilla E-press fires `ServerRescueNpc(NpcGuid, SettlementId)` →
      `HandleOnNpcRescued(NpcId)` runs. Recipes unlock (proves the handler
      ran), but `DespawnRecruitedWanderer` and all settlement-roster update
      calls NEVER fire for the goat. PE-pre log grep confirms zero matches
      on `Despawn|RecruitedWanderer|AddSurvivor|SpawnNext|AddRescued`.
    Editor-side recon (this script's preflight) found the gate in the
      HandleOnNpcRescued ubergraph:

          npcChar  = MorNpcUtils::GetNpcCharacter(self, NpcId)
          objClass = npcChar.GetObjectClass()
          bNotEq1  = (objClass != BP_NpcDwarf_Wanderer_RecruitAndSettlement_C)
          bNotEq2  = (objClass != BP_NpcDwarf_Recruit_C)
          bAND     = bNotEq1 AND bNotEq2
          JumpIfNot bAND -> dispatcher path B (despawn + settlement update)
                            // dwarf classes land here
          // goat (class not in whitelist) falls through path A:
          //   GetGameState / IsInExpedition / generic non-dispatch handling
          //   -> recipes unlock side-effect runs but no despawn / no
          //      settlement update -> later iterator picks "nearest dwarf"
          //      and that's the random-dwarf-at-camp bug.

    Fix: rewrite the EX_ObjectConst.Value references from -34
    (BP_NpcDwarf_Recruit_C) to a new import for BP_NpcGoat_C. Keeps the
    bytecode topology identical (no inserted ops, no offset renumbering)
    -- just changes which class one side of the NotEqual comparison
    points at. Tradeoff: we lose dispatcher-path-B routing for
    BP_NpcDwarf_Recruit_C. Per VS-Claude: that's a niche late-game case,
    accept it; iterate later if needed.

    Both HandleOnNpcRescued (campaign) and SandboxHandleOnNpcRescued
    (sandbox) use the same `-34` constant -- there are two callsites total.
    Both get patched in one pass via the recursive walker.
    """
    imports = data['Imports']

    # ---- Step 1: locate existing BP_NpcDwarf_Recruit_C import ----------
    dwarf_recruit_idx = _find_import_index_by_name(imports, BP_NPC_DWARF_RECRUIT_IMPORT_NAME)
    if dwarf_recruit_idx is None:
        log(f"    ERROR: {BP_NPC_DWARF_RECRUIT_IMPORT_NAME} import not found")
        return False
    log(f"    Found BP_NpcDwarf_Recruit_C import at {dwarf_recruit_idx}")

    # ---- Step 2: add BP_NpcGoat_C import (idempotent) ------------------
    # _add_npcgoat_imports_to_asset adds /Game/Character/NpcGoat/BP_NpcGoat
    # package + BP_NpcGoat_C class imports, returns the negative class idx.
    goat_class_idx = _add_npcgoat_imports_to_asset(data, 'BP_StoryManager')
    log(f"    BP_NpcGoat_C class import at {goat_class_idx}")

    # ---- Step 3: walk bytecode + swap EX_ObjectConst.Value -------------
    # Goes through every export's ScriptBytecode array and any nested
    # KismetPropertyPointer / FFieldPath structures looking for
    # EX_ObjectConst{Value=dwarf_recruit_idx}.
    swaps = _walk_and_swap_objectconst(
        data.get('Exports', []),
        old_value=dwarf_recruit_idx,
        new_value=goat_class_idx,
    )
    log(f"    Bytecode constant-replacement: {swaps} EX_ObjectConst sites swapped")
    log(f"      ({dwarf_recruit_idx} BP_NpcDwarf_Recruit_C -> {goat_class_idx} BP_NpcGoat_C)")

    if swaps == 0:
        log("    ERROR: expected at least 2 swap sites (HandleOnNpcRescued + Sandbox variant)")
        log("           but found 0 -- recon may have been wrong, abort patch")
        return False
    if swaps < 2:
        log(f"    WARN: only {swaps} swap site(s) found, expected 2")
        log("          (one for HandleOnNpcRescued, one for SandboxHandleOnNpcRescued)")
        # Don't fail -- 1 may be enough for campaign-only test.

    # NameMap additions for path strings (FName-serialized)
    for n in [NPCGOAT_PACKAGE_PATH, NPCGOAT_CLASS_PATH, 'BP_NpcGoat_C']:
        ensure_namemap_entry(data, n)
    return True


DWARF_WANDERER_REC_AND_SETTLE_CLASS_PATH = (
    '/Game/Character/NpcDwarf/BP_NpcDwarf_Wanderer_RecruitAndSettlement.'
    'BP_NpcDwarf_Wanderer_RecruitAndSettlement_C'
)


def edit_bp_recruit_camp_spawner(data):
    """v1.2.11: Patch the camp recruit spawner's SpawnCharacter soft class ref
    from BP_NpcDwarf_Wanderer_RecruitAndSettlement_C to BP_NpcGoat_C.

    The spawner has ONE SoftObjectPropertyData (Name=SpawnCharacter) on its
    MorNPCStorySpawner_GEN_VARIABLE component with AssetName pointing at the
    dwarf class. No hard imports for the dwarf class -- it's purely a soft
    reference -- so the patch is a single string swap.

    Effect: when the player's first wanderer rescue at Dimrill Dale Recruit
    Camp triggers this spawner, it now creates BP_NpcGoat_C at the camp
    location instead of the dwarf class.

    Empirical test of Model alpha (data-record save with class-flexible-apply
    vs class-strict-apply -- see deep dive brief 2026-05-10). On reload:
      - If Outcome A (record applies cross-class): goat at camp with full
        inventory data persisted
      - If Outcome B (class-strict apply): goat at camp but empty inventory
      - If Outcome C (spawner-class override ignored): random dwarf at camp
        anyway (record forces actor class)
    """
    log("    --- edit BP_StoryNpcSpawner_Wanderer_RecruitCamp ---")

    # Walk all exports' Data arrays looking for SoftObjectPropertyData with
    # AssetName matching the dwarf class. Replace with goat class.
    swaps = 0

    def _walk(node):
        nonlocal swaps
        if isinstance(node, dict):
            t = node.get('$type', '')
            if 'FTopLevelAssetPath' in t:
                if node.get('AssetName') == DWARF_WANDERER_REC_AND_SETTLE_CLASS_PATH:
                    node['AssetName'] = NPCGOAT_CLASS_PATH
                    swaps += 1
                    log(f"    Swapped FTopLevelAssetPath.AssetName:")
                    log(f"      {DWARF_WANDERER_REC_AND_SETTLE_CLASS_PATH}")
                    log(f"      -> {NPCGOAT_CLASS_PATH}")
            for v in node.values():
                _walk(v)
        elif isinstance(node, list):
            for v in node:
                _walk(v)

    _walk(data)

    if swaps == 0:
        log("    ERROR: dwarf class path not found -- recon was wrong, abort")
        return False
    if swaps > 1:
        log(f"    NOTE: {swaps} swap sites (expected 1) -- proceeding")

    # NameMap additions: the soft-ref path needs the goat strings present
    # for serialization. Add both package + full class path. (Existing dwarf
    # NameMap entries can stay; they're now unused but harmless.)
    for n in [NPCGOAT_PACKAGE_PATH, NPCGOAT_CLASS_PATH]:
        ensure_namemap_entry(data, n)

    log(f"    Total swaps: {swaps}")
    return True


EDIT_FUNCS = {
    'DT_NPCRoles': edit_npcroles,
    'DT_Moria_AI_Population': edit_ai_population,
    'DT_AICharacterSettings': edit_aicharsettings,
    # v1.2.7: restored as eager class-load anchor for BP_NpcGoat_C
    'BP_MoriaGameMode_MainMenu': edit_mainmenu_gamemode,
    'BP_NpcGoat': edit_bp_npcgoat,
    'DT_NPCInventoryPresets': edit_npcinventorypresets,
    'DT_NPCUniqueCharacters': edit_npcuniquecharacters,
    'DT_Storage': edit_dt_storage,
    'DT_ContainerItems': edit_dt_containeritems,
    'BP_NPCManager': edit_bp_npcmanager,
    'DT_Moria_AIChallengeSpawns': edit_ai_challenge_spawns,
    'BP_StoryManager': edit_bp_storymanager,
    'BP_StoryNpcSpawner_Wanderer_RecruitCamp': lambda d: edit_bp_recruit_camp_spawner(d),
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
    # v1.2.10: SKIP BP_NpcGoat from staging — its modded form conflicts with
    # modded BP_StoryManager during retoc to-zen cross-package validation
    # (Failed to find export ...SimpleConstructionScript_0... dependency
    # Serialize). The BP_NpcGoat edits (DefaultContainers wiring, MorNPC
    # interaction fields, optional SCS surgery) are post-rescue UX polish;
    # the actual rescue-routing fix is the BP_StoryManager whitelist patch.
    # Future v1.2.11+ may find a way to coexist.
    SKIP_FROM_STAGING = {'BP_NpcGoat'}
    for out_uasset, out_uexp, dst_rel, name in edited_outputs:
        if name in SKIP_FROM_STAGING:
            log(f"  SKIPPED (retoc conflict): {name}")
            continue
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
        # v1.2.0: dropped MainMenu (was 12) → 11 total
        log(f"  ExportBundleData entries: {export_count} (expected 14 for v1.2.11)")
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
    log(f"  v1.2.0: scoped to wanderer-spawn pivot (per VS-Claude PE trace)")
    log(f"  ")
    log(f"  Editor-side edits:")
    log(f"    DT edits:")
    log(f"    - DT_NPCRoles: Porter Disabled -> Live  (+ label cleanup)")
    log(f"    - DT_NPCInventoryPresets: +1 row 'Porter'")
    log(f"    - DT_NPCUniqueCharacters: +1 row 'PorterGoat'")
    log(f"    - DT_Storage: +1 row 'Goat.BodyInventory' (8x8)")
    log(f"    - DT_ContainerItems: +1 row 'Goat.BodyInventory'")
    log(f"    - DT_Moria_AI_Population: +1 row 'NpcGoat'")
    log(f"    - DT_AICharacterSettings: +1 row 'NpcGoat'")
    log(f"    - DT_Moria_AIChallengeSpawns.SurvivorRescue2: -Dwarf_Survivor_2 -Monster_Wolf +NpcGoat")
    log(f"      (v1.2.4: removed dwarf -> eliminates OnNpcRescued cross-talk)")
    log(f"      (v1.2.5: removed wolf -> peaceful goat-only encounter)")
    log(f"    BP / Manager edits:")
    log(f"    - BP_NPCManager.ValidNpcClasses += BP_NpcGoat_C  (v1.2.9 RESTORED)")
    log(f"      Per VS-Claude probe: needed for server-side roster resolution")
    log(f"    - BP_NpcGoat.InventoryComp.DefaultContainers += Goat.BodyInventory wrapper")
    log(f"    - NEW: BP_ContainerItem_Goat_BodyInventory at /Game/Mods/PorterGoat/Items/")
    log(f"  ")
    log(f"  DROPPED vs v1.1.3:")
    log(f"    - BP_MoriaGameMode_MainMenu load anchor (was for keybind only)")
    log(f"    - BP_NpcGoat.EquipComp.DummyEquipment (always dormant)")
    log(f"    - v1.1.3 full bool-set (bManageInteractionEnabled, bInteractionEnabled)")
    log(f"  ")
    log(f"  v1.2.2: cloned 8 missing MorNPC fields from BP_NpcDwarf into BP_NpcGoat")
    log(f"    - 4 interaction structs: Recruit, DeliverResearch (SP=2), Details (SP=1), Talk (SP=4)")
    log(f"    - 4 non-struct: RecruitNPCWorldCapReachedText, ActivityPointGainedEffect,")
    log(f"      SoftMugAsset, BarkWhitelistTag")
    log(f"  ")
    log(f"  v1.2.3 cleanup (per VS-Claude runtime probe 2026-05-10):")
    log(f"    - DROPPED bIsRescued CDO override -- non-UPROPERTY, edit silently ignored")
    log(f"    - DROPPED bRescueInteractionEnabled CDO override -- already true at runtime")
    log(f"  ")
    log(f"  Rescue prompt gate is OnNpcRescued multicast subscription on")
    log(f"  AMorSettlementManager (signature: void(FGuid NpcId)). Cannot be")
    log(f"  replicated via CDO -- bytecode injection beyond UAssetGUI.")
    log(f"  Runtime mod handles it via raw FScriptDelegate append at goat spawn.")
    log(f"  Pak: {PAK_NAME}")
    log(f"  Zip: {zip_path}")
    log(f"  Install: extract zip to <game>/Moria/Content/Paks/~mods/")
    log(f"{'='*60}")


if __name__ == '__main__':
    main()
