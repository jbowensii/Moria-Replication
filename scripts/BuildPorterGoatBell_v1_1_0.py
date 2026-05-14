"""
BuildPorterGoatBell_v1_1_0.py — Consolidated v1.1.0-rc1 bell pak builder.

Supersedes ALL prior PorterGoat paks (v1.2.x rescue chain, PorterGoatEdits,
PorterGoatBell v1.0.0).  Architecture is bell-summon based, vanilla goat,
runtime menu via UE4SS.

Ships:
  1. BP_PorterGoatBell_C       — trigger item (right-clicked -> spawn goat)
  2. BP_PorterGoatSaddlebags_C — container item with 8x8 backing
  3. DT_Storage row: PorterGoatSaddlebags (8x8 grid)
     DT_Storage row: PorterGoatBell (1x1 nominal grid, no real storage)
  4. DT_ContainerItems rows for both (BP <-> storage wiring)

NOT in v1.1.0-rc1 (deferred to v1.1.0 final, pending user vendor pick):
  - DT_Merchants edits (vendor sells recipes)
  - DT_ItemRecipes rows (1 Ironwood + 1 Bronze for bell;
                         2 Bronze + 6 FineLeather for saddlebags)

Runtime side (VS-Claude rc.40+):
  - Filter by class BP_PorterGoatBell_C on right-click event -> toggle goat
  - Filter by class BP_PorterGoatSaddlebags_C on click -> suppress
  - Goat E-menu overlay: Stay / Follow / Dismiss / Access Saddlebags

Standalone — zero dependencies on v1.2.x. Cross-pak compatible with the
user's "Epic Items in Every Slot" mod (no slot-system modification here).

Usage:
  python scripts/CloneBellAndSaddlebagsBPs.py     # one-time: clone both BPs
  python scripts/BuildPorterGoatBell_v1_1_0.py    # build the pak
"""
from pathlib import Path
import sys
import shutil
import zipfile
import json
import copy

SCRIPT_DIR = Path(__file__).resolve().parent
sys.path.insert(0, str(SCRIPT_DIR))
import BuildPorterGoat as bpg


VERSION    = '1.3.11'
PAK_NAME   = 'PorterGoatBell_P'
WORK_DIR    = bpg.PROJECT_ROOT / 'experiments' / 'portergoat' / 'v110_work'
STAGING_DIR = bpg.PROJECT_ROOT / 'experiments' / 'portergoat' / 'v110_staging'
OUTPUT_DIR  = bpg.PROJECT_ROOT / 'experiments' / 'portergoat' / 'v110_output'

# Pre-cooked BPs from CloneBellAndSaddlebagsBPs.py
BP_BUILD_DIR = bpg.PROJECT_ROOT / 'experiments' / 'portergoat' / 'v110_build'

# v1.1.7: cooked custom icon Texture2D pairs
# Produced by: UE4Editor-Cmd.exe project/Moria.uproject \
#   -ExecutePythonScript=scripts/ue4_import_portergoat_icons.py -nullrhi
# Then: UE4Editor-Cmd.exe project/Moria.uproject -run=Cook \
#   -TargetPlatform=WindowsNoEditor -CookDir=<icons_dir> -nullrhi -unattended
TEX_BUILD_DIR = (bpg.PROJECT_ROOT / 'project' / 'Saved' / 'Cooked'
                 / 'WindowsNoEditor' / 'Moria' / 'Content' / 'Mods'
                 / 'PorterGoat' / 'Icons')

BPS_TO_STAGE = [
    # (basename, in-pak path relative to Moria/Content)
    ('BP_PorterGoatBell',
     'Mods/PorterGoat/Items/BP_PorterGoatBell'),
    # v1.4.0: saddlebag is now an EpicPack-class BP (cloned from
    # BP_EpicPack_AdventurersPack_Large via CloneSaddlebagsAsEpicPack.py).
    # Equippable to player's back slot, surfaces 8x8 grid when worn.
    ('BP_PorterGoatSaddlebags',
     'Mods/PorterGoat/Items/BP_PorterGoatSaddlebags'),
    # v1.1.5: custom StringTable for our localization keys
    ('ST_PorterGoatStrings',
     'Mods/PorterGoat/Strings/ST_PorterGoatStrings'),
    # v1.4.0: kept in pak as dormant foundation for future v1.5+ goat-attached
    # storage. Player carries the saddlebag via EpicPack equip slot now; the
    # goat's DefaultContainers references this wrapper class but the player
    # doesn't interact with it directly until we wire the goat-slot UX.
    ('BP_ContainerItem_Goat_BodyInventory',
     'Mods/PorterGoat/Items/BP_ContainerItem_Goat_BodyInventory'),
]

# v1.1.7: cooked Texture2D pairs from UE4 editor cook (read from TEX_BUILD_DIR)
TEX_TO_STAGE = [
    ('T_PorterGoatBell',
     'Mods/PorterGoat/Icons/T_PorterGoatBell'),
    ('T_PorterGoatSaddlebags',
     'Mods/PorterGoat/Icons/T_PorterGoatSaddlebags'),
]


def log(m=''):
    print(m)


# ---------------------------------------------------------------------------
# Shared helpers (used across multiple DT edits in v1.1.4)
# ---------------------------------------------------------------------------

ITEMS_STRING_TABLE = '/Game/Tech/Data/StringTables/Items.Items'
PORTERGOAT_STRING_TABLE = '/Game/Mods/PorterGoat/Strings/ST_PorterGoatStrings.ST_PorterGoatStrings'


def _make_strtable_text_prop(field_name, key,
                              table_id=PORTERGOAT_STRING_TABLE):
    """Build a TextPropertyData with HistoryType=StringTableEntry.

    Used for DisplayName / Description / Name fields in the same shape that
    Brewskin and other vanilla items use. The key won't necessarily resolve
    in the actual string table (we're using our own custom keys), but the
    serialization round-trips cleanly through UAssetGUI. In-game UI falls
    back to displaying the key when no localized string is found.
    """
    return {
        '$type': 'UAssetAPI.PropertyTypes.Objects.TextPropertyData, UAssetAPI',
        'Flags': 0,
        'HistoryType': 'StringTableEntry',
        'TableId': table_id,
        'Namespace': None,
        'CultureInvariantString': None,
        'SourceFmt': None,
        'Arguments': None,
        'ArgumentsData': None,
        'TransformType': 'ToLower',
        'SourceValue': None,
        'FormatOptions': None,
        'TargetCulture': None,
        'Name': field_name,
        'ArrayIndex': 0,
        'PropertyGuid': None,
        'IsZero': False,
        'PropertyTagFlags': 'None',
        'PropertyTypeName': None,
        'PropertyTagExtensions': 'NoExtension',
        'Value': key,
    }


def _make_tags_prop(tag_list, field_name='Tags'):
    """Build a GameplayTagContainer StructProperty wrapping a list of tag names."""
    return {
        '$type': 'UAssetAPI.PropertyTypes.Structs.StructPropertyData, UAssetAPI',
        'StructType': 'GameplayTagContainer',
        'SerializeNone': True,
        'StructGUID': '{00000000-0000-0000-0000-000000000000}',
        'SerializationControl': 'NoExtension',
        'Operation': 'None',
        'Name': field_name,
        'ArrayIndex': 0,
        'PropertyGuid': None,
        'IsZero': False,
        'PropertyTagFlags': 'None',
        'PropertyTypeName': None,
        'PropertyTagExtensions': 'NoExtension',
        'Value': [
            {
                '$type': 'UAssetAPI.PropertyTypes.Structs.GameplayTagContainerPropertyData, UAssetAPI',
                'Name': field_name,
                'ArrayIndex': 0,
                'PropertyGuid': None,
                'IsZero': False,
                'PropertyTagFlags': 'None',
                'PropertyTypeName': None,
                'PropertyTagExtensions': 'NoExtension',
                'Value': list(tag_list),
            }
        ],
    }


def edit_dt_storage_for_bell_v11(data):
    """Add two new rows to DT_Storage:

      PorterGoatBell        - 1x1 nominal (trigger only, no real storage)
      PorterGoatSaddlebags  - 8x8 storage grid (the bell-architecture cargo)
    """
    log("    --- DT_Storage: add PorterGoatBell + PorterGoatSaddlebags rows ---")
    rows = data['Exports'][0]['Table']['Data']

    tmpl = next((r for r in rows
                 if r.get('Name') == 'Dwarf.BodyInventory'), None)
    if tmpl is None:
        log("    ERROR: Dwarf.BodyInventory template row not found")
        return False

    def _add_row(new_name, w, h):
        if any(r.get('Name') == new_name for r in rows):
            log(f"    NOTE: {new_name} already present (idempotent skip)")
            return
        nr = copy.deepcopy(tmpl)
        nr['Name'] = new_name
        # v1.1.4: set Name/Description string-table keys (were null -> readable)
        display_key = f'Storage.{new_name}.Name'
        desc_key = f'Storage.{new_name}.Description'
        for prop in nr.get('Value', []):
            pname = prop.get('Name')
            if pname == 'InventoryWidth':
                prop['Value'] = w
            elif pname == 'InventoryHeight':
                prop['Value'] = h
            elif pname == 'Name':
                # v1.1.5: retarget TableId to our StringTable
                prop['Value'] = display_key
                prop['TableId'] = PORTERGOAT_STRING_TABLE
            elif pname == 'Description':
                prop['Value'] = desc_key
                prop['TableId'] = PORTERGOAT_STRING_TABLE
            elif pname == 'EnabledState':
                prop['Value'] = 'ERowEnabledState::Live'
        rows.append(nr)
        for n in [new_name, display_key, desc_key,
                  PORTERGOAT_STRING_TABLE,
                  PORTERGOAT_STRING_TABLE.split('.')[0]]:
            bpg.ensure_namemap_entry(data, n)
        log(f"    + Row {new_name}: {w}x{h}, Name={display_key}")

    # v1.3.5: bell row restored to DT_Storage as a 0x0 stub so the
    # BP_PorterGoatBell.RowHandle (typed MorContainerItemRowHandle) routes
    # cleanly through DT_ContainerItems -> DT_Storage chain. The bar is
    # suppressed at the DT_ContainerItems layer via StorageRowHandle.RowName
    # = "None" -- see edit_dt_containeritems_for_bell_v11.
    _add_row('PorterGoatBell', 0, 0)  # stub: row exists but contains no grid
    _add_row('PorterGoatSaddlebags', 8, 8)  # the actual cargo
    log(f"    DT_Storage row count: {len(rows)}")
    return True


def _make_required_material(material_handle_rowname, count):
    """Build one MorRequiredRecipeMaterial struct entry for DefaultRequiredMaterials."""
    return {
        '$type': 'UAssetAPI.PropertyTypes.Structs.StructPropertyData, UAssetAPI',
        'StructType': 'MorRequiredRecipeMaterial',
        'SerializeNone': True,
        'StructGUID': '{00000000-0000-0000-0000-000000000000}',
        'SerializationControl': 'NoExtension',
        'Operation': 'None',
        'Name': 'DefaultRequiredMaterials',
        'ArrayIndex': 0,
        'PropertyGuid': None,
        'IsZero': False,
        'PropertyTagFlags': 'None',
        'PropertyTypeName': None,
        'PropertyTagExtensions': 'NoExtension',
        'Value': [
            {
                '$type': 'UAssetAPI.PropertyTypes.Structs.StructPropertyData, UAssetAPI',
                'StructType': 'MorAnyItemRowHandle',
                'SerializeNone': True,
                'StructGUID': '{00000000-0000-0000-0000-000000000000}',
                'SerializationControl': 'NoExtension',
                'Operation': 'None',
                'Name': 'MaterialHandle',
                'ArrayIndex': 0,
                'PropertyGuid': None,
                'IsZero': False,
                'PropertyTagFlags': 'None',
                'PropertyTypeName': None,
                'PropertyTagExtensions': 'NoExtension',
                'Value': [
                    {
                        '$type': 'UAssetAPI.PropertyTypes.Objects.NamePropertyData, UAssetAPI',
                        'Name': 'RowName',
                        'ArrayIndex': 0,
                        'PropertyGuid': None,
                        'IsZero': False,
                        'PropertyTagFlags': 'None',
                        'PropertyTypeName': None,
                        'PropertyTagExtensions': 'NoExtension',
                        'Value': material_handle_rowname,
                    }
                ],
            },
            {
                '$type': 'UAssetAPI.PropertyTypes.Structs.StructPropertyData, UAssetAPI',
                'StructType': 'MorCategoryTagRowHandle',
                'SerializeNone': True,
                'StructGUID': '{00000000-0000-0000-0000-000000000000}',
                'SerializationControl': 'NoExtension',
                'Operation': 'None',
                'Name': 'WildcardHandle',
                'ArrayIndex': 0,
                'PropertyGuid': None,
                'IsZero': False,
                'PropertyTagFlags': 'None',
                'PropertyTypeName': None,
                'PropertyTagExtensions': 'NoExtension',
                'Value': [
                    {
                        '$type': 'UAssetAPI.PropertyTypes.Objects.NamePropertyData, UAssetAPI',
                        'Name': 'RowName',
                        'ArrayIndex': 0,
                        'PropertyGuid': None,
                        'IsZero': False,
                        'PropertyTagFlags': 'None',
                        'PropertyTypeName': None,
                        'PropertyTagExtensions': 'NoExtension',
                        'Value': 'None',
                    }
                ],
            },
            {
                '$type': 'UAssetAPI.PropertyTypes.Objects.IntPropertyData, UAssetAPI',
                'Name': 'Count',
                'ArrayIndex': 0,
                'PropertyGuid': None,
                'IsZero': False,
                'PropertyTagFlags': 'None',
                'PropertyTypeName': None,
                'PropertyTagExtensions': 'NoExtension',
                'Value': count,
            },
        ],
    }


def edit_dt_itemrecipes_for_bell_v11(data):
    """Add two new rows to DT_ItemRecipes — the actual crafting recipes for
    Bell and Saddlebags.

      PorterGoatBell:        1 Ironwood + 1 Bronze Ingot -> 1 BP_PorterGoatBell
      PorterGoatSaddlebags:  2 Bronze Ingot + 6 Fine Leather -> 1 BP_PorterGoatSaddlebags

    Cloned from AdventurersPack_Small recipe template (closest pattern for
    "single-output, multi-material, no specific crafting station").  Retargets:
      ResultItemHandle.RowName -> our DT_ContainerItems row name
      DefaultRequiredMaterials -> the user-specified ingredients
    """
    log("    --- DT_ItemRecipes: add PorterGoatBell + Saddlebags recipes ---")
    rows = data['Exports'][0]['Table']['Data']

    tmpl = next((r for r in rows
                 if r.get('Name') == 'AdventurersPack_Small'), None)
    if tmpl is None:
        log("    ERROR: AdventurersPack_Small template row not found")
        return False

    def _make_station_handle(station_rowname):
        """Build one MorConstructionRowHandle entry for CraftingStations array."""
        return {
            '$type': 'UAssetAPI.PropertyTypes.Structs.StructPropertyData, UAssetAPI',
            'StructType': 'MorConstructionRowHandle',
            'SerializeNone': True,
            'StructGUID': '{00000000-0000-0000-0000-000000000000}',
            'SerializationControl': 'NoExtension',
            'Operation': 'None',
            'Name': 'CraftingStations',
            'ArrayIndex': 0,
            'PropertyGuid': None,
            'IsZero': False,
            'PropertyTagFlags': 'None',
            'PropertyTypeName': None,
            'PropertyTagExtensions': 'NoExtension',
            'Value': [
                {
                    '$type': 'UAssetAPI.PropertyTypes.Objects.NamePropertyData, UAssetAPI',
                    'Name': 'RowName',
                    'ArrayIndex': 0,
                    'PropertyGuid': None,
                    'IsZero': False,
                    'PropertyTagFlags': 'None',
                    'PropertyTypeName': None,
                    'PropertyTagExtensions': 'NoExtension',
                    'Value': station_rowname,
                }
            ],
        }

    def _add_recipe(new_name, result_rowname, materials, stations, craft_time=15.0):
        if any(r.get('Name') == new_name for r in rows):
            log(f"    NOTE: {new_name} already present (idempotent skip)")
            return
        nr = copy.deepcopy(tmpl)
        nr['Name'] = new_name
        for prop in nr.get('Value', []):
            pname = prop.get('Name')
            if pname == 'ResultItemHandle':
                for sub in prop.get('Value', []):
                    if sub.get('Name') == 'RowName':
                        sub['Value'] = result_rowname
            elif pname == 'ResultItemCount':
                prop['Value'] = 1
            elif pname == 'CraftTimeSeconds':
                prop['Value'] = craft_time
            elif pname == 'bCanBePinned':
                # v1.1.4: allow players to pin in crafting UI
                prop['Value'] = True
            elif pname == 'CraftingStations':
                # CRITICAL: empty CraftingStations means recipe HIDDEN from
                # all UIs. v1.1.3 fix: list workbench + workbench upgrade so
                # recipe shows up in workbench crafting menu.
                prop['Value'] = [_make_station_handle(s) for s in stations]
            elif pname == 'DefaultRequiredMaterials':
                # Replace the materials array with our new ingredients
                prop['Value'] = [
                    _make_required_material(mh, cnt) for (mh, cnt) in materials
                ]
            elif pname == 'EnabledState':
                prop['Value'] = 'ERowEnabledState::Live'
        rows.append(nr)
        bpg.ensure_namemap_entry(data, new_name)
        bpg.ensure_namemap_entry(data, result_rowname)
        for (mh, _) in materials:
            bpg.ensure_namemap_entry(data, mh)
        for s in stations:
            bpg.ensure_namemap_entry(data, s)
        log(f"    + Recipe {new_name}: result={result_rowname}, "
            f"materials={[(m,c) for (m,c) in materials]}, "
            f"stations={stations}")

    WORKBENCH_STATIONS = ['CraftingStation_Workbench',
                          'CraftingStation_WorkbenchUpgrade']

    _add_recipe(
        'PorterGoatBell',
        result_rowname='ContainerItem.PorterGoatBell',
        materials=[('Item.Ironwood', 1), ('Item.BronzeIngot', 1)],
        stations=WORKBENCH_STATIONS,
        craft_time=10.0,
    )
    _add_recipe(
        'PorterGoatSaddlebags',
        result_rowname='ContainerItem.PorterGoatSaddlebags',
        materials=[('Item.BronzeIngot', 2), ('Item.FineLeather', 6)],
        stations=WORKBENCH_STATIONS,
        craft_time=20.0,
    )
    log(f"    DT_ItemRecipes row count: {len(rows)}")
    return True


def edit_dt_recipebundles_for_bell_v11(data):
    """Add two new rows to DT_RecipeBundles wrapping each recipe as a
    purchasable bundle from a vendor.

      PorterGoatBell_Bundle       -> Recipes: ["Item.PorterGoatBell"]      BaseTradeValue: 60
      PorterGoatSaddlebags_Bundle -> Recipes: ["Item.PorterGoatSaddlebags"] BaseTradeValue: 120
    """
    log("    --- DT_RecipeBundles: add Bell + Saddlebags bundles ---")
    rows = data['Exports'][0]['Table']['Data']

    tmpl = next((r for r in rows if r.get('Name') == 'MeatHat'), None)
    if tmpl is None:
        log("    ERROR: MeatHat template row not found")
        return False

    def _make_recipe_handle(recipe_rowname):
        return {
            '$type': 'UAssetAPI.PropertyTypes.Structs.StructPropertyData, UAssetAPI',
            'StructType': 'MorAnyRecipeRowHandle',
            'SerializeNone': True,
            'StructGUID': '{00000000-0000-0000-0000-000000000000}',
            'SerializationControl': 'NoExtension',
            'Operation': 'None',
            'Name': 'Recipes',
            'ArrayIndex': 0,
            'PropertyGuid': None,
            'IsZero': False,
            'PropertyTagFlags': 'None',
            'PropertyTypeName': None,
            'PropertyTagExtensions': 'NoExtension',
            'Value': [
                {
                    '$type': 'UAssetAPI.PropertyTypes.Objects.NamePropertyData, UAssetAPI',
                    'Name': 'RowName',
                    'ArrayIndex': 0,
                    'PropertyGuid': None,
                    'IsZero': False,
                    'PropertyTagFlags': 'None',
                    'PropertyTypeName': None,
                    'PropertyTagExtensions': 'NoExtension',
                    'Value': recipe_rowname,
                }
            ],
        }

    def _add_bundle(new_name, recipe_rowname, base_trade_value,
                    display_key, description_key, icon_asset_path):
        if any(r.get('Name') == new_name for r in rows):
            log(f"    NOTE: {new_name} already present (idempotent skip)")
            return
        nr = copy.deepcopy(tmpl)
        nr['Name'] = new_name
        for prop in nr.get('Value', []):
            pname = prop.get('Name')
            if pname == 'Recipes':
                prop['Value'] = [_make_recipe_handle(recipe_rowname)]
            elif pname == 'BaseTradeValue':
                prop['Value'] = base_trade_value
            elif pname == 'DisplayName':
                # v1.1.4: override Meathat key -> our own
                # v1.1.5: also retarget TableId -> our StringTable
                prop['Value'] = display_key
                prop['TableId'] = PORTERGOAT_STRING_TABLE
            elif pname == 'Description':
                prop['Value'] = description_key
                prop['TableId'] = PORTERGOAT_STRING_TABLE
            elif pname == 'Icon':
                v = prop.get('Value', {})
                ap = v.get('AssetPath', {})
                ap['AssetName'] = icon_asset_path
            elif pname == 'EnabledState':
                prop['Value'] = 'ERowEnabledState::Live'
        rows.append(nr)
        for n in [new_name, recipe_rowname, display_key, description_key,
                  icon_asset_path, icon_asset_path.split('.')[0],
                  PORTERGOAT_STRING_TABLE,
                  PORTERGOAT_STRING_TABLE.split('.')[0]]:
            bpg.ensure_namemap_entry(data, n)
        log(f"    + Bundle {new_name}: Recipes=[{recipe_rowname}], "
            f"BaseTradeValue={base_trade_value}, "
            f"DisplayName={display_key}, Icon={icon_asset_path}")

    _add_bundle('PorterGoatBell_Bundle',
                recipe_rowname='Item.PorterGoatBell',
                base_trade_value=60.0,
                display_key='Economy.Recipe.Bundle.PorterGoatBell.Name',
                description_key='Economy.Recipe.Bundle.PorterGoatBell.Description',
                icon_asset_path='/Game/Mods/PorterGoat/Icons/T_PorterGoatBell.T_PorterGoatBell')
    _add_bundle('PorterGoatSaddlebags_Bundle',
                recipe_rowname='Item.PorterGoatSaddlebags',
                base_trade_value=120.0,
                display_key='Economy.Recipe.Bundle.PorterGoatSaddlebags.Name',
                description_key='Economy.Recipe.Bundle.PorterGoatSaddlebags.Description',
                icon_asset_path='/Game/Mods/PorterGoat/Icons/T_PorterGoatSaddlebags.T_PorterGoatSaddlebags')
    log(f"    DT_RecipeBundles row count: {len(rows)}")
    return True


def edit_dt_offertemplates_for_bell_v11(data):
    """Add two new rows to DT_OfferTemplates wrapping the bell + saddlebags
    as RECIPE-BUNDLE offers (vendor sells the recipe; player crafts).

    Cloned from MeatHatRecipe_Offer_Default template (recipe-bundle style):
      RecipeBundle.RowName = our DT_RecipeBundles row name
      ItemHandle.RowName   = "None" (recipe-bundle path, not direct-item)
      OfferSize / Limits   = 1 / 1 / 1 (recipes are 1-shot purchase)
    """
    log("    --- DT_OfferTemplates: add PorterGoatBell + Saddlebags RECIPE offers ---")
    rows = data['Exports'][0]['Table']['Data']

    tmpl = next((r for r in rows
                 if r.get('Name') == 'MeatHatRecipe_Offer_Default'), None)
    if tmpl is None:
        log("    ERROR: MeatHatRecipe_Offer_Default template row not found")
        return False

    def _add_offer(new_name, recipe_bundle_rowname):
        if any(r.get('Name') == new_name for r in rows):
            log(f"    NOTE: {new_name} already present (idempotent skip)")
            return
        nr = copy.deepcopy(tmpl)
        nr['Name'] = new_name
        for prop in nr.get('Value', []):
            pname = prop.get('Name')
            if pname == 'RecipeBundle':
                for sub in prop.get('Value', []):
                    if sub.get('Name') == 'RowName':
                        sub['Value'] = recipe_bundle_rowname
            elif pname == 'ItemHandle':
                for sub in prop.get('Value', []):
                    if sub.get('Name') == 'RowName':
                        sub['Value'] = 'None'
            elif pname == 'OfferSize':
                prop['Value'] = 1
            elif pname == 'OfferMinLimit':
                prop['Value'] = 1
            elif pname == 'OfferMaxLimit':
                prop['Value'] = 1
            elif pname == 'EnabledState':
                prop['Value'] = 'ERowEnabledState::Live'
        rows.append(nr)
        bpg.ensure_namemap_entry(data, new_name)
        bpg.ensure_namemap_entry(data, recipe_bundle_rowname)
        log(f"    + Offer {new_name}: RecipeBundle={recipe_bundle_rowname}, Size=1")

    _add_offer('PorterGoatBell_Offer_Default',       'PorterGoatBell_Bundle')
    _add_offer('PorterGoatSaddlebags_Offer_Default', 'PorterGoatSaddlebags_Bundle')
    log(f"    DT_OfferTemplates row count: {len(rows)}")
    return True


def edit_dt_offerdecks_for_shire_v11(data):
    """Append our two new offers to ShireOffers_Default.Offers array so the
    Shire merchant offers the bell + saddlebags on rotation.
    """
    log("    --- DT_OfferDecks: extend ShireOffers_Default with new offers ---")
    rows = data['Exports'][0]['Table']['Data']

    deck_row = next((r for r in rows
                     if r.get('Name') == 'ShireOffers_Default'), None)
    if deck_row is None:
        log("    ERROR: ShireOffers_Default row not found")
        return False

    offers_prop = next((p for p in deck_row.get('Value', [])
                        if isinstance(p, dict) and p.get('Name') == 'Offers'), None)
    if offers_prop is None:
        log("    ERROR: Offers array missing on ShireOffers_Default")
        return False

    entries = offers_prop.get('Value', [])
    if not entries:
        log("    ERROR: Offers array empty (no template to clone)")
        return False

    def _entry_rowname(e):
        if not isinstance(e, dict):
            return None
        val = e.get('Value', [])
        if not isinstance(val, list):
            return None
        for sub in val:
            if isinstance(sub, dict) and sub.get('Name') == 'RowName':
                return sub.get('Value')
        return None

    def _append_offer(offer_row_name):
        # Idempotency
        if any(_entry_rowname(e) == offer_row_name for e in entries):
            log(f"    NOTE: {offer_row_name} already in Offers (idempotent skip)")
            return
        tmpl = copy.deepcopy(entries[0])
        # Update RowName
        for sub in tmpl.get('Value', []):
            if isinstance(sub, dict) and sub.get('Name') == 'RowName':
                sub['Value'] = offer_row_name
        entries.append(tmpl)
        bpg.ensure_namemap_entry(data, offer_row_name)
        log(f"    + ShireOffers_Default.Offers += {offer_row_name}")

    _append_offer('PorterGoatBell_Offer_Default')
    _append_offer('PorterGoatSaddlebags_Offer_Default')
    log(f"    ShireOffers_Default.Offers count: {len(entries)}")
    return True


def _ensure_mesh_import(data, mesh_pkg_path, mesh_class_name):
    """Add hard imports for a StaticMesh asset (Package + StaticMesh).
    Returns the negative import index of the StaticMesh asset reference.
    Idempotent: skips if package + class already imported.

    For SM_Tankard_01a -> two imports added:
      Package import: /Game/Unshippable/.../SM_Tankard_01a, ClassName=Package
      Asset import:   SM_Tankard_01a, ClassName=StaticMesh, OuterIndex=package
    """
    imports = data['Imports']
    # Check for existing mesh asset import
    for i, imp in enumerate(imports):
        if (imp.get('ObjectName') == mesh_class_name
                and imp.get('ClassName') == 'StaticMesh'):
            return -(i + 1)

    # Add the package import
    pkg_import = {
        '$type': 'UAssetAPI.Import, UAssetAPI',
        'ObjectName': mesh_pkg_path,
        'OuterIndex': 0,
        'ClassPackage': '/Script/CoreUObject',
        'ClassName': 'Package',
        'PackageName': None,
        'bImportOptional': False,
    }
    imports.append(pkg_import)
    pkg_neg = -len(imports)

    # Add the StaticMesh asset import
    mesh_import = {
        '$type': 'UAssetAPI.Import, UAssetAPI',
        'ObjectName': mesh_class_name,
        'OuterIndex': pkg_neg,
        'ClassPackage': '/Script/Engine',
        'ClassName': 'StaticMesh',
        'PackageName': None,
        'bImportOptional': False,
    }
    imports.append(mesh_import)
    mesh_neg = -len(imports)

    # Critical: ensure all FNames referenced by these imports are in NameMap.
    # /Script/CoreUObject, /Script/Engine, Package are usually already there;
    # 'StaticMesh' often is NOT in vanilla DT_ContainerItems and would trip
    # the "dummy FName" exception on fromjson.
    for n in [mesh_pkg_path, mesh_class_name,
              '/Script/CoreUObject', '/Script/Engine',
              'Package', 'StaticMesh']:
        bpg.ensure_namemap_entry(data, n)

    return mesh_neg


def edit_dt_epicpacks_for_saddlebag_v140(data):
    """v1.4.0: add PorterGoatSaddlebags row to DT_EpicPacks (player-equippable
    back-slot pack, 8x8 grid).

    Cloned from AdventurersPack_Large template row. Retargets:
      - Actor      -> /Game/Mods/PorterGoat/Items/BP_PorterGoatSaddlebags
      - Icon       -> /Game/Mods/PorterGoat/Icons/T_PorterGoatSaddlebags
      - StorageRowHandle.RowName -> 'PorterGoatSaddlebags'
      - DisplayName + Description -> ST_PorterGoatStrings keys
      - Tags retain vanilla EpicPack tags so the bag-slot equip logic
        recognizes it as an EpicPack

    The DT_Storage.PorterGoatSaddlebags row (8x8) already exists from
    edit_dt_storage_for_bell_v11 -- the EpicPack's StorageRowHandle points
    at it just like the ContainerItem version did.
    """
    log("    --- DT_EpicPacks: add PorterGoatSaddlebags row (player-equippable, 8x8) ---")
    rows = data['Exports'][-1]['Table']['Data']

    tmpl = next((r for r in rows if r.get('Name') == 'AdventurersPack_Large'), None)
    if tmpl is None:
        log("    ERROR: AdventurersPack_Large template row not found in DT_EpicPacks")
        return False

    if any(r.get('Name') == 'PorterGoatSaddlebags' for r in rows):
        log("    NOTE: PorterGoatSaddlebags row already exists in DT_EpicPacks (idempotent skip)")
        return True

    BP_PKG_PATH    = '/Game/Mods/PorterGoat/Items/BP_PorterGoatSaddlebags'
    BP_CLASS_PATH  = '/Game/Mods/PorterGoat/Items/BP_PorterGoatSaddlebags.BP_PorterGoatSaddlebags_C'
    ICON_PATH      = '/Game/Mods/PorterGoat/Icons/T_PorterGoatSaddlebags.T_PorterGoatSaddlebags'
    DISPLAY_KEY    = 'Container.PorterGoatSaddlebags.Name'
    DESCRIPTION_KEY = 'Container.PorterGoatSaddlebags.Description'

    nr = copy.deepcopy(tmpl)
    nr['Name'] = 'PorterGoatSaddlebags'

    for prop in nr.get('Value', []):
        pname = prop.get('Name')
        if pname == 'StorageRowHandle':
            # Update inner RowName
            inner = prop.get('Value', [])
            for sub in inner:
                if sub.get('Name') == 'RowName':
                    sub['Value'] = 'PorterGoatSaddlebags'
        elif pname == 'DisplayName':
            prop['HistoryType']  = 'StringTableEntry'
            prop['TableId']      = PORTERGOAT_STRING_TABLE
            prop['Value']        = DISPLAY_KEY
            prop['Namespace']    = None
            prop['CultureInvariantString'] = None
            prop['SourceFmt']    = None
            prop['Arguments']    = None
            prop['ArgumentsData'] = None
            prop['SourceValue']  = None
            prop['FormatOptions'] = None
            prop['TargetCulture'] = None
        elif pname == 'Description':
            prop['HistoryType']  = 'StringTableEntry'
            prop['TableId']      = PORTERGOAT_STRING_TABLE
            prop['Value']        = DESCRIPTION_KEY
            prop['Namespace']    = None
            prop['CultureInvariantString'] = None
            prop['SourceFmt']    = None
            prop['Arguments']    = None
            prop['ArgumentsData'] = None
            prop['SourceValue']  = None
            prop['FormatOptions'] = None
            prop['TargetCulture'] = None
        elif pname == 'Icon':
            ap = prop['Value']['AssetPath']
            ap['PackageName'] = None
            ap['AssetName']   = ICON_PATH
        elif pname == 'Actor':
            ap = prop['Value']['AssetPath']
            ap['PackageName'] = None
            ap['AssetName']   = BP_CLASS_PATH
        elif pname == 'BaseTradeValue':
            prop['Value'] = 120.0
        elif pname == 'EnabledState':
            prop['Value'] = 'ERowEnabledState::Live'

    rows.append(nr)

    # NameMap entries: row name, BP pkg/class, icon path + base, localization keys
    for n in ['PorterGoatSaddlebags',
              BP_PKG_PATH, BP_CLASS_PATH,
              ICON_PATH, ICON_PATH.split('.')[0],
              DISPLAY_KEY, DESCRIPTION_KEY,
              PORTERGOAT_STRING_TABLE,
              PORTERGOAT_STRING_TABLE.split('.')[0]]:
        bpg.ensure_namemap_entry(data, n)

    log(f"    + Row PorterGoatSaddlebags: Actor={BP_CLASS_PATH}, "
        f"Storage=PorterGoatSaddlebags (8x8 grid), Tags=vanilla EpicPack set")
    log(f"    DT_EpicPacks row count: {len(rows)}")
    return True


def edit_dt_containeritems_for_bell_v11(data):
    """v1.1.2: Add two new rows to DT_ContainerItems with Icon + DroppedMesh
    overrides INJECTED into the Dwarf.BodyInventory template (proven clean
    round-trip from v1.1.1). Skip DisplayName/Description text overrides —
    UAssetGUI's TextPropertyData round-trip is finicky on inline text;
    in-game UI falls back to row name (PorterGoatBell / PorterGoatSaddlebags)
    until proper localization is authored.

    Visual overrides added:
      Icon (SoftObjectPropertyData)        - inventory icon
      DroppedItemMeshOverride (ObjectProperty) - world mesh when dropped

    Bell:        Icon=Heavy_Ram_Icon,         DroppedMesh=SM_Tankard_01a
    Saddlebags:  Icon=T_UI_Icon_Container,    DroppedMesh=SM_Tankard_01a
    """
    log("    --- DT_ContainerItems: add PorterGoatBell + Saddlebags (icon+mesh) ---")
    rows = data['Exports'][0]['Table']['Data']

    tmpl = next((r for r in rows
                 if r.get('Name') == 'Dwarf.BodyInventory'), None)
    if tmpl is None:
        log("    ERROR: Dwarf.BodyInventory template row not found")
        return False

    # Get the SM_Tankard_01a import index (or add if missing)
    tankard_mesh_idx = _ensure_mesh_import(
        data,
        '/Game/Unshippable/ThirdParty/MedievalVOL6/Meshes/SM_Tankard_01a',
        'SM_Tankard_01a',
    )
    log(f"    SM_Tankard_01a import at {tankard_mesh_idx}")

    def _make_icon_prop(asset_name):
        """Build a SoftObjectPropertyData for the 'Icon' field."""
        return {
            '$type': 'UAssetAPI.PropertyTypes.Objects.SoftObjectPropertyData, UAssetAPI',
            'Name': 'Icon',
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
                    'AssetName': asset_name,
                },
                'SubPathString': None,
            },
        }

    def _make_dropmesh_prop(mesh_import_idx):
        """Build an ObjectPropertyData for the 'DroppedItemMeshOverride' field."""
        return {
            '$type': 'UAssetAPI.PropertyTypes.Objects.ObjectPropertyData, UAssetAPI',
            'Name': 'DroppedItemMeshOverride',
            'ArrayIndex': 0,
            'PropertyGuid': None,
            'IsZero': False,
            'PropertyTagFlags': 'None',
            'PropertyTypeName': None,
            'PropertyTagExtensions': 'NoExtension',
            'Value': mesh_import_idx,
        }

    def _add_row(new_name, bp_pkg, bp_class_path, icon_asset_path,
                 display_key, description_key, tags):
        if any(r.get('Name') == new_name for r in rows):
            log(f"    NOTE: {new_name} already present (idempotent skip)")
            return
        nr = copy.deepcopy(tmpl)
        nr['Name'] = new_name
        # Modify existing fields
        for prop in nr.get('Value', []):
            pname = prop.get('Name')
            if pname == 'Actor':
                v = prop.get('Value', {})
                ap = v.get('AssetPath', {})
                ap['AssetName'] = bp_class_path
                log(f"      Actor -> {bp_class_path}")
            elif pname == 'StorageRowHandle':
                for sub in prop.get('Value', []):
                    if sub.get('Name') == 'RowName':
                        sub['Value'] = new_name
            elif pname == 'EnabledState':
                prop['Value'] = 'ERowEnabledState::Live'

        prop_names = {p.get('Name') for p in nr.get('Value', [])}

        # Inject Icon (or update existing)
        if 'Icon' not in prop_names:
            nr['Value'].append(_make_icon_prop(icon_asset_path))
            log(f"      Icon (injected) -> {icon_asset_path}")
        else:
            for prop in nr['Value']:
                if prop.get('Name') == 'Icon':
                    v = prop.get('Value', {})
                    ap = v.get('AssetPath', {})
                    ap['AssetName'] = icon_asset_path

        # Inject DroppedItemMeshOverride
        if 'DroppedItemMeshOverride' not in prop_names:
            nr['Value'].append(_make_dropmesh_prop(tankard_mesh_idx))
            log(f"      DroppedItemMeshOverride (injected) -> SM_Tankard_01a")
        else:
            for prop in nr['Value']:
                if prop.get('Name') == 'DroppedItemMeshOverride':
                    prop['Value'] = tankard_mesh_idx

        # v1.1.4: Inject DisplayName (v1.1.5: also retarget TableId)
        if 'DisplayName' not in prop_names:
            nr['Value'].append(_make_strtable_text_prop('DisplayName', display_key))
            log(f"      DisplayName (injected) -> {display_key}")
        else:
            for prop in nr['Value']:
                if prop.get('Name') == 'DisplayName':
                    prop['Value'] = display_key
                    prop['TableId'] = PORTERGOAT_STRING_TABLE

        # v1.1.4: Inject Description (v1.1.5: also retarget TableId)
        if 'Description' not in prop_names:
            nr['Value'].append(_make_strtable_text_prop('Description', description_key))
            log(f"      Description (injected) -> {description_key}")
        else:
            for prop in nr['Value']:
                if prop.get('Name') == 'Description':
                    prop['Value'] = description_key
                    prop['TableId'] = PORTERGOAT_STRING_TABLE

        # v1.1.4: Inject Tags (CRITICAL — controls Tools-section categorization)
        if 'Tags' not in prop_names:
            nr['Value'].append(_make_tags_prop(tags))
            log(f"      Tags (injected) -> {tags}")
        else:
            for prop in nr['Value']:
                if prop.get('Name') == 'Tags':
                    inner = prop.get('Value', [])
                    if isinstance(inner, list) and inner and isinstance(inner[0], dict):
                        inner[0]['Value'] = list(tags)
                        log(f"      Tags (updated) -> {tags}")

        rows.append(nr)
        # NameMap entries
        for n in [new_name, bp_pkg, bp_class_path,
                  icon_asset_path, icon_asset_path.split('.')[0],
                  '/Game/Unshippable/ThirdParty/MedievalVOL6/Meshes/SM_Tankard_01a',
                  'SM_Tankard_01a', 'Icon', 'DroppedItemMeshOverride',
                  'DisplayName', 'Description', 'Tags',
                  display_key, description_key,
                  # v1.1.5: ST_PorterGoatStrings TableId references
                  PORTERGOAT_STRING_TABLE,
                  PORTERGOAT_STRING_TABLE.split('.')[0]]:
            bpg.ensure_namemap_entry(data, n)
        for t in tags:
            bpg.ensure_namemap_entry(data, t)

    # v1.3.5: bell row restored to DT_ContainerItems. The BP's RowHandle
    # (typed MorContainerItemRowHandle) routes here -- removing the row in
    # v1.3.3 caused stale-neighbor lookup ("axe" icon). The bar is suppressed
    # by setting StorageRowHandle.RowName="None" after _add_row.
    _add_row(
        'PorterGoatBell',
        bp_pkg='/Game/Mods/PorterGoat/Items/BP_PorterGoatBell',
        bp_class_path='/Game/Mods/PorterGoat/Items/BP_PorterGoatBell.BP_PorterGoatBell_C',
        icon_asset_path='/Game/Mods/PorterGoat/Icons/T_PorterGoatBell.T_PorterGoatBell',
        display_key='Container.PorterGoatBell.Name',
        description_key='Container.PorterGoatBell.Description',
        tags=['UI.Tool'],
    )
    # v1.3.5: null out StorageRowHandle on the bell row so the container UI
    # has no grid backing and renders no fullness bar.
    for r in rows:
        if r.get('Name') == 'PorterGoatBell':
            for prop in r.get('Value', []):
                if prop.get('Name') == 'StorageRowHandle':
                    inner = prop.get('Value', [])
                    for sub in inner:
                        if sub.get('Name') == 'RowName':
                            sub['Value'] = 'None'
                            log(f"      StorageRowHandle.RowName -> None (suppress bar)")
                            break
                    break
            break
    # v1.3.11: saddlebag restored to DT_ContainerItems. v1.4.0's EpicPack
    # pivot caused player inventory corruption (replaced vanilla 8x1 body
    # inventory with 8x8 even without crafting). Reverted.
    _add_row(
        'PorterGoatSaddlebags',
        bp_pkg='/Game/Mods/PorterGoat/Items/BP_PorterGoatSaddlebags',
        bp_class_path='/Game/Mods/PorterGoat/Items/BP_PorterGoatSaddlebags.BP_PorterGoatSaddlebags_C',
        icon_asset_path='/Game/Mods/PorterGoat/Icons/T_PorterGoatSaddlebags.T_PorterGoatSaddlebags',
        display_key='Container.PorterGoatSaddlebags.Name',
        description_key='Container.PorterGoatSaddlebags.Description',
        tags=['UI.Tool'],
    )
    log(f"    DT_ContainerItems row count: {len(rows)}")
    return True


def edit_dt_npcroles_for_v138(data):
    """v1.3.8: enable Porter role in DT_NPCRoles + retarget DisplayName.

    Vanilla DT_NPCRoles.Porter row has:
      - EnabledState = Disabled  (UMorNpcUtils::GetAvialableRoles filters this out)
      - DisplayName  = '*Porter [Bug this]'  (FRG dev annotation)
      - Description  = '*Carries items for a player.'

    v1.3.8 flips:
      - EnabledState -> Live
      - DisplayName  -> 'Porter Goat' (inline Base text, both SourceString
                                       and LocalizedString)
      - Description  -> 'Carries items for the player.' (drop FRG asterisk)

    Result: UMorNPCComponent::SetRole(Porter) works, and the interaction
    menu's NameText (which reads from GetCurrentRole().DisplayName) shows
    'Porter Goat' once VS-Claude's runtime BeginPlay hook calls
    SetRole(Porter) at goat spawn time.
    """
    log("    --- DT_NPCRoles: enable Porter + retarget DisplayName -> 'Porter Goat' ---")
    rows = data['Exports'][0]['Table']['Data']
    porter = next((r for r in rows if r.get('Name') == 'Porter'), None)
    if porter is None:
        log("    ERROR: Porter row not found in DT_NPCRoles")
        return False

    flipped = False
    display_set = False
    desc_cleaned = False
    for prop in porter['Value']:
        pname = prop.get('Name')
        if pname == 'EnabledState':
            old = prop.get('Value')
            prop['Value'] = 'ERowEnabledState::Live'
            log(f"    Porter.EnabledState: {old} -> {prop['Value']}")
            flipped = True
        elif pname == 'DisplayName':
            # v1.3.9: retarget to StringTable entry instead of inline Base text.
            # v1.3.8 attempted inline Base with a placeholder hash but the
            # in-game menu still resolved to "Citizen" -- the hash mismatch
            # caused fallback to the role-display chain. StringTable refs are
            # the proven path in this pak (used for all other text fields).
            prop['HistoryType'] = 'StringTableEntry'
            prop['TableId']     = PORTERGOAT_STRING_TABLE
            prop['Value']       = 'Goat.Role.Porter'
            prop['Namespace']   = None
            prop['CultureInvariantString'] = None
            prop['SourceFmt']   = None
            prop['Arguments']   = None
            prop['ArgumentsData'] = None
            prop['SourceValue'] = None
            prop['FormatOptions'] = None
            prop['TargetCulture'] = None
            log(f"    Porter.DisplayName: StringTable ref -> Goat.Role.Porter")
            display_set = True
        elif pname == 'Description':
            for k in ('SourceString', 'LocalizedString'):
                v = prop.get(k)
                if isinstance(v, str) and v.startswith('*'):
                    prop[k] = v.lstrip('*').strip()
                    desc_cleaned = True
            if desc_cleaned:
                log(f"    Porter.Description: dropped FRG asterisk")

    if not flipped:
        log("    ERROR: Porter row has no EnabledState property")
        return False
    if not display_set:
        log("    WARN: Porter DisplayName not modified (property not found?)")

    # v1.3.9: NameMap entries for the new StringTable retarget
    for n in (PORTERGOAT_STRING_TABLE,
              PORTERGOAT_STRING_TABLE.split('.')[0],
              'Goat.Role.Porter',
              'Porter Goat'):
        bpg.ensure_namemap_entry(data, n)
    return True


def edit_dt_items_for_bell_v133(data):
    """v1.3.3: add PorterGoatBell row to DT_Items (non-container regular item).

    Bell is no longer a container -- moved out of DT_ContainerItems / DT_Storage
    so the inventory UI doesn't render the storage-fullness bar that container
    items get. This DT_Items row gives the bell a clean tile with icon + name +
    tooltip and nothing else.

    Schema mirrors vanilla DT_Items rows (e.g., Scrap, Wood, Ironwood) which
    have no storage backing and no durability. Tags=["UI.Tool"] keeps it in
    the Tools section of the crafting menu.
    """
    log("    --- DT_Items: add PorterGoatBell row (non-container regular item) ---")
    rows = data['Exports'][-1]['Table']['Data']

    # Use Ironwood as the template (single-stack, plain item, no special effects)
    tmpl = next((r for r in rows if r.get('Name') == 'Ironwood'), None)
    if tmpl is None:
        tmpl = rows[0] if rows else None
    if tmpl is None:
        log("    ERROR: DT_Items has no rows to use as template")
        return False

    BP_PKG_PATH    = '/Game/Mods/PorterGoat/Items/BP_PorterGoatBell'
    BP_CLASS_PATH  = '/Game/Mods/PorterGoat/Items/BP_PorterGoatBell.BP_PorterGoatBell_C'
    ICON_PATH      = '/Game/Mods/PorterGoat/Icons/T_PorterGoatBell.T_PorterGoatBell'
    DISPLAY_KEY    = 'Container.PorterGoatBell.Name'
    DESCRIPTION_KEY = 'Container.PorterGoatBell.Description'
    TAGS           = ['UI.Tool']

    if any(r.get('Name') == 'PorterGoatBell' for r in rows):
        log("    NOTE: PorterGoatBell already in DT_Items (idempotent skip)")
        return True

    nr = copy.deepcopy(tmpl)
    nr['Name'] = 'PorterGoatBell'

    for prop in nr.get('Value', []):
        pname = prop.get('Name')
        if pname == 'DisplayName':
            prop['HistoryType']  = 'StringTableEntry'
            prop['TableId']      = PORTERGOAT_STRING_TABLE
            prop['Value']        = DISPLAY_KEY
            prop['Namespace']    = None
            prop['CultureInvariantString'] = None
            prop['SourceFmt']    = None
            prop['Arguments']    = None
            prop['ArgumentsData'] = None
            prop['SourceValue']  = None
            prop['FormatOptions'] = None
            prop['TargetCulture'] = None
        elif pname == 'Description':
            prop['HistoryType']  = 'StringTableEntry'
            prop['TableId']      = PORTERGOAT_STRING_TABLE
            prop['Value']        = DESCRIPTION_KEY
            prop['Namespace']    = None
            prop['CultureInvariantString'] = None
            prop['SourceFmt']    = None
            prop['Arguments']    = None
            prop['ArgumentsData'] = None
            prop['SourceValue']  = None
            prop['FormatOptions'] = None
            prop['TargetCulture'] = None
        elif pname == 'Icon':
            ap = prop['Value']['AssetPath']
            ap['PackageName'] = None
            ap['AssetName']   = ICON_PATH
        elif pname == 'Actor':
            ap = prop['Value']['AssetPath']
            ap['PackageName'] = None
            ap['AssetName']   = BP_CLASS_PATH
        elif pname == 'Tags':
            inner = prop.get('Value', [])
            if isinstance(inner, list) and inner and isinstance(inner[0], dict):
                inner[0]['Value'] = list(TAGS)
        elif pname == 'MaxStackSize':
            prop['Value'] = 1
        elif pname == 'SlotSize':
            prop['Value'] = 1
        elif pname == 'BaseTradeValue':
            prop['Value'] = 60.0
        elif pname == 'Portability':
            prop['Value'] = 'EItemPortability::Storable'
        elif pname == 'EnabledState':
            prop['Value'] = 'ERowEnabledState::Live'

    rows.append(nr)

    # NameMap entries: row name, BP pkg/class, icon path + base, tags,
    # localization keys + the StringTable references.
    for n in ['PorterGoatBell',
              BP_PKG_PATH, BP_CLASS_PATH,
              ICON_PATH, ICON_PATH.split('.')[0],
              DISPLAY_KEY, DESCRIPTION_KEY,
              PORTERGOAT_STRING_TABLE,
              PORTERGOAT_STRING_TABLE.split('.')[0]]:
        bpg.ensure_namemap_entry(data, n)
    for t in TAGS:
        bpg.ensure_namemap_entry(data, t)

    log(f"    + Row PorterGoatBell: Actor={BP_CLASS_PATH}, Icon={ICON_PATH}, "
        f"Tags={TAGS}")
    log(f"    DT_Items row count: {len(rows)}")
    return True


def main():
    log(f"=== BuildPorterGoatBell v{VERSION} ===")
    log(f"Consolidated bell architecture: 1 pak supersedes all prior PorterGoat paks.")
    log()

    # Sanity: pre-cooked BPs must exist
    for basename, _ in BPS_TO_STAGE:
        ua = BP_BUILD_DIR / f'{basename}.uasset'
        ue = ua.with_suffix('.uexp')
        if not (ua.exists() and ue.exists()):
            log(f"ERROR: pre-cooked BP missing at {ua}")
            log(f"  run scripts/CloneBellAndSaddlebagsBPs.py first")
            sys.exit(1)
    log(f"[0/8] Pre-cooked BPs found for: "
        f"{', '.join(b for b, _ in BPS_TO_STAGE)}")
    log()

    log("[1/8] Cleaning dirs...")
    for d in [WORK_DIR, STAGING_DIR, OUTPUT_DIR]:
        bpg.rmtree_safe(d)
        d.mkdir(parents=True, exist_ok=True)
    log("  Done.")
    log()

    # Process DT_Storage
    log("[2/8] DT_Storage: round-trip + add new rows...")
    src_uasset = bpg.LEGACY_ROOT / 'Tech' / 'Data' / 'Items' / 'DT_Storage.uasset'
    src_uexp = src_uasset.with_suffix('.uexp')
    work_uasset = WORK_DIR / 'DT_Storage.uasset'
    work_uexp = WORK_DIR / 'DT_Storage.uexp'
    shutil.copy2(src_uasset, work_uasset)
    shutil.copy2(src_uexp, work_uexp)
    work_json = WORK_DIR / 'DT_Storage.json'
    if not bpg.run_uassetgui_tojson(work_uasset, work_json):
        sys.exit(1)
    with open(work_json, 'r', encoding='utf-8') as f:
        data = json.load(f)
    if not edit_dt_storage_for_bell_v11(data):
        sys.exit(1)
    modified_json = WORK_DIR / 'DT_Storage_modified.json'
    with open(modified_json, 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=2)
    out_uasset = WORK_DIR / 'DT_Storage_out.uasset'
    if not bpg.run_uassetgui_fromjson(modified_json, out_uasset):
        sys.exit(1)
    out_uexp = out_uasset.with_suffix('.uexp')
    validate_json = WORK_DIR / 'DT_Storage_validate.json'
    if not bpg.run_uassetgui_tojson(out_uasset, validate_json):
        sys.exit(1)
    # Sanity check
    with open(validate_json, 'r', encoding='utf-8') as f:
        v = json.load(f)
    # v1.3.5: both rows restored to DT_Storage (bell as 0x0 stub, saddlebags as 8x8)
    found_bell = any(r.get('Name') == 'PorterGoatBell'
                     for r in v['Exports'][0]['Table']['Data'])
    found_sad = any(r.get('Name') == 'PorterGoatSaddlebags'
                    for r in v['Exports'][0]['Table']['Data'])
    if not (found_bell and found_sad):
        log(f"ERROR: round-trip lost rows (bell={found_bell} sad={found_sad})")
        sys.exit(1)
    log(f"  DT_Storage round-trip OK")
    stage_dt_storage_uasset = out_uasset
    stage_dt_storage_uexp = out_uexp
    log()

    # Process DT_ContainerItems
    log("[3/8] DT_ContainerItems: round-trip + add new rows...")
    src_uasset = bpg.LEGACY_ROOT / 'Tech' / 'Data' / 'Items' / 'DT_ContainerItems.uasset'
    src_uexp = src_uasset.with_suffix('.uexp')
    work_uasset = WORK_DIR / 'DT_ContainerItems.uasset'
    work_uexp = WORK_DIR / 'DT_ContainerItems.uexp'
    shutil.copy2(src_uasset, work_uasset)
    shutil.copy2(src_uexp, work_uexp)
    work_json = WORK_DIR / 'DT_ContainerItems.json'
    if not bpg.run_uassetgui_tojson(work_uasset, work_json):
        sys.exit(1)
    with open(work_json, 'r', encoding='utf-8') as f:
        data = json.load(f)
    if not edit_dt_containeritems_for_bell_v11(data):
        sys.exit(1)
    modified_json = WORK_DIR / 'DT_ContainerItems_modified.json'
    with open(modified_json, 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=2)
    out_uasset = WORK_DIR / 'DT_ContainerItems_out.uasset'
    if not bpg.run_uassetgui_fromjson(modified_json, out_uasset):
        sys.exit(1)
    out_uexp = out_uasset.with_suffix('.uexp')
    validate_json = WORK_DIR / 'DT_ContainerItems_validate.json'
    if not bpg.run_uassetgui_tojson(out_uasset, validate_json):
        sys.exit(1)
    with open(validate_json, 'r', encoding='utf-8') as f:
        v = json.load(f)
    # v1.3.11: both bell and saddlebag back in DT_ContainerItems (saddlebag
    # restored after v1.4.0 EpicPack pivot was reverted).
    found_bell = any(r.get('Name') == 'PorterGoatBell'
                     for r in v['Exports'][0]['Table']['Data'])
    found_sad = any(r.get('Name') == 'PorterGoatSaddlebags'
                    for r in v['Exports'][0]['Table']['Data'])
    if not (found_bell and found_sad):
        log(f"ERROR: round-trip lost rows (bell={found_bell} sad={found_sad})")
        sys.exit(1)
    log(f"  DT_ContainerItems round-trip OK")
    stage_dt_ci_uasset = out_uasset
    stage_dt_ci_uexp = out_uexp
    log()

    # v1.4.0 DT_EpicPacks staging REMOVED -- shipping DT_EpicPacks override
    # caused player inventory corruption (8x8 default for new characters
    # without crafting). DO NOT re-add without testing player inventory
    # impact on fresh characters first.

    # v1.3.8: Process DT_NPCRoles (enable Porter + retarget DisplayName)
    log("[3a-r/8] DT_NPCRoles: round-trip + Porter Live + DisplayName 'Porter Goat'...")
    src_uasset = bpg.LEGACY_ROOT / 'Character' / 'NpcDwarf' / 'DT_NPCRoles.uasset'
    src_uexp = src_uasset.with_suffix('.uexp')
    work_uasset = WORK_DIR / 'DT_NPCRoles.uasset'
    work_uexp = WORK_DIR / 'DT_NPCRoles.uexp'
    shutil.copy2(src_uasset, work_uasset)
    shutil.copy2(src_uexp, work_uexp)
    work_json = WORK_DIR / 'DT_NPCRoles.json'
    if not bpg.run_uassetgui_tojson(work_uasset, work_json):
        sys.exit(1)
    with open(work_json, 'r', encoding='utf-8') as f:
        data = json.load(f)
    if not edit_dt_npcroles_for_v138(data):
        sys.exit(1)
    modified_json = WORK_DIR / 'DT_NPCRoles_modified.json'
    with open(modified_json, 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=2)
    out_uasset = WORK_DIR / 'DT_NPCRoles_out.uasset'
    if not bpg.run_uassetgui_fromjson(modified_json, out_uasset):
        sys.exit(1)
    out_uexp = out_uasset.with_suffix('.uexp')
    validate_json = WORK_DIR / 'DT_NPCRoles_validate.json'
    if not bpg.run_uassetgui_tojson(out_uasset, validate_json):
        sys.exit(1)
    with open(validate_json, 'r', encoding='utf-8') as f:
        v = json.load(f)
    porter_row = next((r for r in v['Exports'][0]['Table']['Data']
                       if r.get('Name') == 'Porter'), None)
    if porter_row is None:
        log("ERROR: round-trip lost Porter row in DT_NPCRoles")
        sys.exit(1)
    porter_state = next((p['Value'] for p in porter_row.get('Value', [])
                         if p.get('Name') == 'EnabledState'), None)
    if porter_state != 'ERowEnabledState::Live':
        log(f"ERROR: Porter.EnabledState round-trip drift: {porter_state}")
        sys.exit(1)
    log(f"  DT_NPCRoles round-trip OK (Porter Live)")
    stage_dt_npcroles_uasset = out_uasset
    stage_dt_npcroles_uexp = out_uexp
    log()

    # v1.3.5: DT_Items stage REMOVED -- bell reverted to DT_ContainerItems route
    # with StorageRowHandle.RowName="None" suppressing the bar. v1.3.3's DT_Items
    # approach failed because BP_PorterGoatBell's RowHandle is typed
    # MorContainerItemRowHandle (hardwired to DT_ContainerItems lookup), so
    # removing the bell row from DT_ContainerItems caused stale-neighbor lookup
    # (axe icon shown).

    # Process DT_ItemRecipes (this is HUGE — ~14MB — but only one row addition per ingredient set)
    log("[3a-i/8] DT_ItemRecipes: round-trip + add bell + saddlebags recipes...")
    src_uasset = bpg.LEGACY_ROOT / 'Tech' / 'Data' / 'Items' / 'DT_ItemRecipes.uasset'
    src_uexp = src_uasset.with_suffix('.uexp')
    work_uasset = WORK_DIR / 'DT_ItemRecipes.uasset'
    work_uexp = WORK_DIR / 'DT_ItemRecipes.uexp'
    shutil.copy2(src_uasset, work_uasset)
    shutil.copy2(src_uexp, work_uexp)
    work_json = WORK_DIR / 'DT_ItemRecipes.json'
    if not bpg.run_uassetgui_tojson(work_uasset, work_json):
        sys.exit(1)
    with open(work_json, 'r', encoding='utf-8') as f:
        data = json.load(f)
    if not edit_dt_itemrecipes_for_bell_v11(data):
        sys.exit(1)
    modified_json = WORK_DIR / 'DT_ItemRecipes_modified.json'
    with open(modified_json, 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=2)
    out_uasset = WORK_DIR / 'DT_ItemRecipes_out.uasset'
    if not bpg.run_uassetgui_fromjson(modified_json, out_uasset):
        sys.exit(1)
    out_uexp = out_uasset.with_suffix('.uexp')
    validate_json = WORK_DIR / 'DT_ItemRecipes_validate.json'
    if not bpg.run_uassetgui_tojson(out_uasset, validate_json):
        sys.exit(1)
    with open(validate_json, 'r', encoding='utf-8') as f:
        v = json.load(f)
    found_bell_recipe = any(r.get('Name') == 'PorterGoatBell'
                             for r in v['Exports'][0]['Table']['Data'])
    found_sad_recipe = any(r.get('Name') == 'PorterGoatSaddlebags'
                            for r in v['Exports'][0]['Table']['Data'])
    if not (found_bell_recipe and found_sad_recipe):
        log(f"ERROR: round-trip lost recipe rows (bell={found_bell_recipe} sad={found_sad_recipe})")
        sys.exit(1)
    log(f"  DT_ItemRecipes round-trip OK")
    stage_dt_ir_uasset = out_uasset
    stage_dt_ir_uexp = out_uexp
    log()

    # Process DT_RecipeBundles
    log("[3a-ii/8] DT_RecipeBundles: round-trip + add bell + saddlebags bundles...")
    src_uasset = bpg.LEGACY_ROOT / 'Tech' / 'Data' / 'Economy' / 'DT_RecipeBundles.uasset'
    src_uexp = src_uasset.with_suffix('.uexp')
    work_uasset = WORK_DIR / 'DT_RecipeBundles.uasset'
    work_uexp = WORK_DIR / 'DT_RecipeBundles.uexp'
    shutil.copy2(src_uasset, work_uasset)
    shutil.copy2(src_uexp, work_uexp)
    work_json = WORK_DIR / 'DT_RecipeBundles.json'
    if not bpg.run_uassetgui_tojson(work_uasset, work_json):
        sys.exit(1)
    with open(work_json, 'r', encoding='utf-8') as f:
        data = json.load(f)
    if not edit_dt_recipebundles_for_bell_v11(data):
        sys.exit(1)
    modified_json = WORK_DIR / 'DT_RecipeBundles_modified.json'
    with open(modified_json, 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=2)
    out_uasset = WORK_DIR / 'DT_RecipeBundles_out.uasset'
    if not bpg.run_uassetgui_fromjson(modified_json, out_uasset):
        sys.exit(1)
    out_uexp = out_uasset.with_suffix('.uexp')
    validate_json = WORK_DIR / 'DT_RecipeBundles_validate.json'
    if not bpg.run_uassetgui_tojson(out_uasset, validate_json):
        sys.exit(1)
    log(f"  DT_RecipeBundles round-trip OK")
    stage_dt_rb_uasset = out_uasset
    stage_dt_rb_uexp = out_uexp
    log()

    # Process DT_OfferTemplates
    log("[3b/8] DT_OfferTemplates: round-trip + add new offer rows...")
    src_uasset = bpg.LEGACY_ROOT / 'Tech' / 'Data' / 'Economy' / 'DT_OfferTemplates.uasset'
    src_uexp = src_uasset.with_suffix('.uexp')
    work_uasset = WORK_DIR / 'DT_OfferTemplates.uasset'
    work_uexp = WORK_DIR / 'DT_OfferTemplates.uexp'
    shutil.copy2(src_uasset, work_uasset)
    shutil.copy2(src_uexp, work_uexp)
    work_json = WORK_DIR / 'DT_OfferTemplates.json'
    if not bpg.run_uassetgui_tojson(work_uasset, work_json):
        sys.exit(1)
    with open(work_json, 'r', encoding='utf-8') as f:
        data = json.load(f)
    if not edit_dt_offertemplates_for_bell_v11(data):
        sys.exit(1)
    modified_json = WORK_DIR / 'DT_OfferTemplates_modified.json'
    with open(modified_json, 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=2)
    out_uasset = WORK_DIR / 'DT_OfferTemplates_out.uasset'
    if not bpg.run_uassetgui_fromjson(modified_json, out_uasset):
        sys.exit(1)
    out_uexp = out_uasset.with_suffix('.uexp')
    validate_json = WORK_DIR / 'DT_OfferTemplates_validate.json'
    if not bpg.run_uassetgui_tojson(out_uasset, validate_json):
        sys.exit(1)
    with open(validate_json, 'r', encoding='utf-8') as f:
        v = json.load(f)
    found_bell_offer = any(r.get('Name') == 'PorterGoatBell_Offer_Default'
                           for r in v['Exports'][0]['Table']['Data'])
    found_sad_offer = any(r.get('Name') == 'PorterGoatSaddlebags_Offer_Default'
                          for r in v['Exports'][0]['Table']['Data'])
    if not (found_bell_offer and found_sad_offer):
        log(f"ERROR: round-trip lost offer rows (bell={found_bell_offer} sad={found_sad_offer})")
        sys.exit(1)
    log(f"  DT_OfferTemplates round-trip OK")
    stage_dt_ot_uasset = out_uasset
    stage_dt_ot_uexp = out_uexp
    log()

    # Process DT_OfferDecks
    log("[3c/8] DT_OfferDecks: round-trip + extend ShireOffers_Default...")
    src_uasset = bpg.LEGACY_ROOT / 'Tech' / 'Data' / 'Economy' / 'DT_OfferDecks.uasset'
    src_uexp = src_uasset.with_suffix('.uexp')
    work_uasset = WORK_DIR / 'DT_OfferDecks.uasset'
    work_uexp = WORK_DIR / 'DT_OfferDecks.uexp'
    shutil.copy2(src_uasset, work_uasset)
    shutil.copy2(src_uexp, work_uexp)
    work_json = WORK_DIR / 'DT_OfferDecks.json'
    if not bpg.run_uassetgui_tojson(work_uasset, work_json):
        sys.exit(1)
    with open(work_json, 'r', encoding='utf-8') as f:
        data = json.load(f)
    if not edit_dt_offerdecks_for_shire_v11(data):
        sys.exit(1)
    modified_json = WORK_DIR / 'DT_OfferDecks_modified.json'
    with open(modified_json, 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=2)
    out_uasset = WORK_DIR / 'DT_OfferDecks_out.uasset'
    if not bpg.run_uassetgui_fromjson(modified_json, out_uasset):
        sys.exit(1)
    out_uexp = out_uasset.with_suffix('.uexp')
    validate_json = WORK_DIR / 'DT_OfferDecks_validate.json'
    if not bpg.run_uassetgui_tojson(out_uasset, validate_json):
        sys.exit(1)
    log(f"  DT_OfferDecks round-trip OK")
    stage_dt_od_uasset = out_uasset
    stage_dt_od_uexp = out_uexp
    log()

    log("[4/8] Staging DTs...")
    dt_dst_dir = STAGING_DIR / 'Moria' / 'Content' / 'Tech' / 'Data' / 'Items'
    dt_dst_dir.mkdir(parents=True, exist_ok=True)
    shutil.copy2(stage_dt_storage_uasset, dt_dst_dir / 'DT_Storage.uasset')
    shutil.copy2(stage_dt_storage_uexp, dt_dst_dir / 'DT_Storage.uexp')
    shutil.copy2(stage_dt_ci_uasset, dt_dst_dir / 'DT_ContainerItems.uasset')
    shutil.copy2(stage_dt_ci_uexp, dt_dst_dir / 'DT_ContainerItems.uexp')
    # v1.3.11: DT_EpicPacks staging REMOVED (v1.4.0 caused inventory corruption)
    # v1.3.8: DT_NPCRoles ships in Character/NpcDwarf path (different from Items)
    npc_dst_dir = STAGING_DIR / 'Moria' / 'Content' / 'Character' / 'NpcDwarf'
    npc_dst_dir.mkdir(parents=True, exist_ok=True)
    shutil.copy2(stage_dt_npcroles_uasset, npc_dst_dir / 'DT_NPCRoles.uasset')
    shutil.copy2(stage_dt_npcroles_uexp, npc_dst_dir / 'DT_NPCRoles.uexp')
    log(f"  Staged: DT_Storage, DT_ContainerItems, DT_NPCRoles")
    # DT_ItemRecipes (Items dir)
    shutil.copy2(stage_dt_ir_uasset, dt_dst_dir / 'DT_ItemRecipes.uasset')
    shutil.copy2(stage_dt_ir_uexp, dt_dst_dir / 'DT_ItemRecipes.uexp')
    log(f"  Staged: DT_ItemRecipes")
    # Economy DTs
    eco_dst_dir = STAGING_DIR / 'Moria' / 'Content' / 'Tech' / 'Data' / 'Economy'
    eco_dst_dir.mkdir(parents=True, exist_ok=True)
    shutil.copy2(stage_dt_rb_uasset, eco_dst_dir / 'DT_RecipeBundles.uasset')
    shutil.copy2(stage_dt_rb_uexp, eco_dst_dir / 'DT_RecipeBundles.uexp')
    shutil.copy2(stage_dt_ot_uasset, eco_dst_dir / 'DT_OfferTemplates.uasset')
    shutil.copy2(stage_dt_ot_uexp, eco_dst_dir / 'DT_OfferTemplates.uexp')
    shutil.copy2(stage_dt_od_uasset, eco_dst_dir / 'DT_OfferDecks.uasset')
    shutil.copy2(stage_dt_od_uexp, eco_dst_dir / 'DT_OfferDecks.uexp')
    log(f"  Staged: DT_RecipeBundles, DT_OfferTemplates, DT_OfferDecks")
    log()

    log("[5/8] Staging BPs...")
    for basename, dst_rel in BPS_TO_STAGE:
        src_ua = BP_BUILD_DIR / f'{basename}.uasset'
        src_ue = src_ua.with_suffix('.uexp')
        dst_dir = STAGING_DIR / 'Moria' / 'Content' / Path(dst_rel).parent
        dst_dir.mkdir(parents=True, exist_ok=True)
        dst_name = Path(dst_rel).name
        shutil.copy2(src_ua, dst_dir / f'{dst_name}.uasset')
        shutil.copy2(src_ue, dst_dir / f'{dst_name}.uexp')
        log(f"  Staged: Moria/Content/{dst_rel}")

    # v1.1.7: stage cooked custom icon textures
    log("  --- Custom icon Texture2D pairs ---")
    for basename, dst_rel in TEX_TO_STAGE:
        src_ua = TEX_BUILD_DIR / f'{basename}.uasset'
        src_ue = src_ua.with_suffix('.uexp')
        if not (src_ua.exists() and src_ue.exists()):
            log(f"  ERROR: cooked texture missing: {src_ua}")
            log(f"  Run scripts/ue4_import_portergoat_icons.py then cook commandlet")
            sys.exit(1)
        dst_dir = STAGING_DIR / 'Moria' / 'Content' / Path(dst_rel).parent
        dst_dir.mkdir(parents=True, exist_ok=True)
        dst_name = Path(dst_rel).name
        shutil.copy2(src_ua, dst_dir / f'{dst_name}.uasset')
        shutil.copy2(src_ue, dst_dir / f'{dst_name}.uexp')
        log(f"  Staged: Moria/Content/{dst_rel}  "
            f"({src_ua.stat().st_size + src_ue.stat().st_size} bytes)")
    log()

    # v1.3.0: modded BP_NpcGoat override
    # Restores the v1.2.0-v1.2.2 BP modifications dropped in v1.2.10 due to the
    # cross-package retoc conflict with modded BP_StoryManager. v1.1.x+
    # does NOT touch BP_StoryManager, so the conflict should not recur.
    log("[5b/8] BP_NpcGoat override (porter behavior native to the BP)...")
    npcgoat_src_rel = 'Character/NpcGoat/BP_NpcGoat'
    npcgoat_src_uasset = bpg.LEGACY_ROOT / f'{npcgoat_src_rel}.uasset'
    npcgoat_src_uexp   = bpg.LEGACY_ROOT / f'{npcgoat_src_rel}.uexp'
    if not (npcgoat_src_uasset.exists() and npcgoat_src_uexp.exists()):
        log(f"  ERROR: vanilla BP_NpcGoat missing at {npcgoat_src_uasset}")
        sys.exit(1)

    ng_work_uasset = WORK_DIR / 'BP_NpcGoat.uasset'
    ng_work_uexp   = WORK_DIR / 'BP_NpcGoat.uexp'
    ng_work_json   = WORK_DIR / 'BP_NpcGoat.json'
    shutil.copy2(npcgoat_src_uasset, ng_work_uasset)
    shutil.copy2(npcgoat_src_uexp,   ng_work_uexp)

    if not bpg.run_uassetgui_tojson(ng_work_uasset, ng_work_json):
        log("  ERROR: tojson BP_NpcGoat failed")
        sys.exit(1)

    with open(ng_work_json, 'r', encoding='utf-8') as f:
        ng_data = json.load(f)

    # Apply the v1.2.x CDO edits: DefaultContainers += GoatBodyInventory_C
    # + 8 cloned MorNPC interaction structs from BP_NpcDwarf.
    if not bpg.edit_bp_npcgoat(ng_data):
        log("  ERROR: edit_bp_npcgoat failed")
        sys.exit(1)

    # SCS surgery — add MorWandererComponent (v1.2.8 pattern).
    # The v1.2.10 cross-pak retoc conflict involved modded BP_StoryManager
    # being in the same pak. We do NOT modify BP_StoryManager here, so this
    # surgery should re-enable cleanly.
    log("  Adding MorWandererComponent SCS node...")
    if not bpg._add_morwanderer_scs(ng_data):
        log("  WARN: SCS surgery failed; goat will lack MorWandererComponent")

    # v1.3.1 — disable 4 of 5 vanilla interaction prompts on the MorNPC
    # component CDO. v1.3.4: KEEP bManageInteractionEnabled=true so the goat
    # surfaces "[E] Manage Goat" as the proximity cue. Runtime mod intercepts
    # E and opens its custom modal (Stay / Follow / Manage / Dismiss /
    # Access Saddlebags) before vanilla Manage UI can spawn.
    log("  v1.3.7: setting bDetails=true (vanilla-rendered cue), Rescue/Recruit/Talk/Manage=false...")
    morpnc_export = next((e for e in ng_data.get('Exports', [])
                          if e.get('ObjectName') == 'MorNPC_GEN_VARIABLE'), None)
    if morpnc_export is None:
        log("    ERROR: MorNPC_GEN_VARIABLE not found")
        sys.exit(1)
    INTERACTION_BOOL_STATES = [
        ('bRescueInteractionEnabled',   False),   # v1.3.6 worked but user can't use Rescue
        ('bRecruitInteractionEnabled',  False),
        ('bDetailsInteractionEnabled',  True),    # v1.3.7: also vanilla-rendered per v1.3.0 evidence (E-menu showed Rescue+Details)
        ('bTalkInteractionEnabled',     False),
        ('bManageInteractionEnabled',   False),
    ]
    existing_props = {p.get('Name') for p in morpnc_export.get('Data', [])}
    for bool_name, target in INTERACTION_BOOL_STATES:
        bpg.ensure_namemap_entry(ng_data, bool_name)
        if bool_name in existing_props:
            for p in morpnc_export['Data']:
                if p.get('Name') == bool_name:
                    p['Value'] = target
                    log(f"    {bool_name}: updated -> {target}")
                    break
        else:
            morpnc_export['Data'].append({
                '$type': 'UAssetAPI.PropertyTypes.Objects.BoolPropertyData, UAssetAPI',
                'Name': bool_name,
                'ArrayIndex': 0,
                'IsZero': False,
                'PropertyTagFlags': 'None',
                'PropertyTagExtensions': 'NoExtension',
                'Value': target,
            })
            log(f"    {bool_name}: appended -> {target}")

    # v1.3.1 — override actor DisplayName from soft-ref-into-ST_AiCharacters
    # (which routes through dwarf name lookup and falls back to "Citizen")
    # to an inline literal "Porter Goat".
    log("  v1.3.1: overriding Default__BP_NpcGoat_C.DisplayName -> 'Porter Goat'...")
    cdo_export = next((e for e in ng_data.get('Exports', [])
                       if e.get('ObjectName') == 'Default__BP_NpcGoat_C'), None)
    if cdo_export is None:
        log("    ERROR: Default__BP_NpcGoat_C not found")
        sys.exit(1)
    for p in cdo_export.get('Data', []):
        if p.get('Name') == 'DisplayName':
            # Rewrite to inline Base text with a stable hash key.
            p['HistoryType'] = 'Base'
            p['TableId'] = None
            p['Namespace'] = ''
            p['CultureInvariantString'] = 'Porter Goat'
            p['SourceFmt'] = None
            p['Arguments'] = None
            p['ArgumentsData'] = None
            p['SourceValue'] = None
            p['FormatOptions'] = None
            p['TargetCulture'] = None
            # The Value field on a Base-history TextPropertyData is the
            # source-string hash key. Use a deterministic 32-hex hash so
            # round-trip is stable.
            p['Value'] = 'B3F1D27E4A89C45EAB12569D3F87C0E1'
            log("    DisplayName rewritten to inline Base text 'Porter Goat'")
            break
    else:
        log("    WARN: DisplayName property not found on CDO")

    ng_modified_json = WORK_DIR / 'BP_NpcGoat_modified.json'
    with open(ng_modified_json, 'w', encoding='utf-8') as f:
        json.dump(ng_data, f, indent=2)

    ng_out_uasset = WORK_DIR / 'BP_NpcGoat_out.uasset'
    if not bpg.run_uassetgui_fromjson(ng_modified_json, ng_out_uasset):
        log("  ERROR: fromjson BP_NpcGoat failed")
        sys.exit(1)
    ng_out_uexp = ng_out_uasset.with_suffix('.uexp')
    if not (ng_out_uasset.exists() and ng_out_uexp.exists()):
        log("  ERROR: BP_NpcGoat round-trip outputs missing")
        sys.exit(1)

    # Round-trip validate
    ng_validate_json = WORK_DIR / 'BP_NpcGoat_validate.json'
    if not bpg.run_uassetgui_tojson(ng_out_uasset, ng_validate_json):
        log("  ERROR: BP_NpcGoat round-trip validation tojson failed")
        sys.exit(1)
    log("  Round-trip OK")

    # Stage at vanilla path -- this is an override
    ng_dst_dir = STAGING_DIR / 'Moria' / 'Content' / 'Character' / 'NpcGoat'
    ng_dst_dir.mkdir(parents=True, exist_ok=True)
    shutil.copy2(ng_out_uasset, ng_dst_dir / 'BP_NpcGoat.uasset')
    shutil.copy2(ng_out_uexp,   ng_dst_dir / 'BP_NpcGoat.uexp')
    log(f"  Staged: Moria/Content/Character/NpcGoat/BP_NpcGoat  "
        f"({ng_out_uasset.stat().st_size + ng_out_uexp.stat().st_size} bytes)")
    log()

    log("[6/8] retoc to-zen ...")
    if not bpg.run_retoc_tozen(STAGING_DIR, OUTPUT_DIR, PAK_NAME):
        log("ERROR: retoc to-zen failed")
        sys.exit(1)
    pak = OUTPUT_DIR / f'{PAK_NAME}.pak'
    ucas = OUTPUT_DIR / f'{PAK_NAME}.ucas'
    utoc = OUTPUT_DIR / f'{PAK_NAME}.utoc'
    for f in [pak, ucas, utoc]:
        if f.exists():
            log(f"  {f.name}: {f.stat().st_size} bytes")
    log()

    log("[7/8] Creating distribution zip...")
    zip_path = bpg.DOWNLOADS_DIR / f'PorterGoatBell_v{VERSION}.zip'
    with zipfile.ZipFile(zip_path, 'w', zipfile.ZIP_DEFLATED) as z:
        for f in [pak, ucas, utoc]:
            if f.exists():
                z.write(f, arcname=f.name)
                log(f"  Added: {f.name}")
    log(f"  Output: {zip_path} ({zip_path.stat().st_size} bytes)")
    log()

    log("[8/8] Summary")
    log('=' * 60)
    log(f"  PorterGoatBell v{VERSION} -- BUILD SUCCESSFUL")
    log()
    log(f"  Ships:")
    log(f"    - BP_PorterGoatBell at Mods/PorterGoat/Items/BP_PorterGoatBell")
    log(f"    - BP_PorterGoatSaddlebags at Mods/PorterGoat/Items/BP_PorterGoatSaddlebags")
    log(f"    - DT_Storage rows: PorterGoatBell (1x1), PorterGoatSaddlebags (8x8)")
    log(f"    - DT_ContainerItems rows wiring both BPs to their storage")
    log(f"    - DT_ItemRecipes: PorterGoatBell (1 Ironwood + 1 Bronze),")
    log(f"                       PorterGoatSaddlebags (2 Bronze + 6 FineLeather)")
    log(f"    - DT_RecipeBundles: PorterGoatBell_Bundle (60 trade),")
    log(f"                         PorterGoatSaddlebags_Bundle (120 trade)")
    log(f"    - DT_OfferTemplates: Bell + Saddlebags RECIPE offers")
    log(f"    - DT_OfferDecks.ShireOffers_Default: extended with both offers")
    log(f"  Shire merchant sells the RECIPES; player crafts with ingredients.")
    log()
    log(f"  Class paths for VS-Claude runtime hooks:")
    log(f"    Bell:       /Game/Mods/PorterGoat/Items/BP_PorterGoatBell.BP_PorterGoatBell_C")
    log(f"    Saddlebags: /Game/Mods/PorterGoat/Items/BP_PorterGoatSaddlebags.BP_PorterGoatSaddlebags_C")
    log()
    log(f"  Standalone pak. Supersedes ALL prior PorterGoat releases.")
    log(f"  Cross-pak compatible with 'Epic Items in Every Slot' user mod.")
    log()
    log(f"  Deferred to v1.1.0 final (pending vendor pick):")
    log(f"    - DT_Merchants edit: add bell + saddlebags recipe to chosen vendor's offers")
    log(f"    - Or DT_ItemRecipes rows if user picks craft-instead-of-buy")
    log()
    log(f"  Pak: {PAK_NAME}")
    log(f"  Zip: {zip_path}")
    log(f"  Install: extract zip to <game>/Moria/Content/Paks/~mods/")
    log('=' * 60)


if __name__ == '__main__':
    main()
