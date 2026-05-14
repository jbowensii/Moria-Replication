"""
BuildPorterGoatBell.py — Standalone bell pak builder.

Ships:
  1. BP_BellOfTheGoat (pre-cooked by scripts/CloneBellOfTheGoatBP.py)
  2. DT_Storage with new row 'BellOfTheGoat' (8x8 grid)

Architecture C: bell inherits from BP_EpicPack_AdventurersPack_Small.  When
player equips bell into the pack slot, vanilla engine grants the player an
8x8 grid (read from DT_Storage.BellOfTheGoat).  VS-Claude's runtime mod
hooks the equip event to spawn the goat.  Bell + contents persist with
player inventory natively via UE's pack save mechanism.

Cross-pak compatibility:
  - Does NOT modify BP_NpcGoat, BP_StoryManager, BP_NPCManager, or any other
    asset that v1.2.x touched. Fully standalone.
  - Adds Mods/PorterGoat/Items/BP_BellOfTheGoat at a brand-new mod path.
  - Adds one row to DT_Storage (BellOfTheGoat).

Out of scope (deferred to v1.1.0):
  - Crafting recipe (DT_ItemRecipes row) - complex schema with 15+ subfields
  - Recipe discovery (DT_AllRecipes row)
  - Custom bell icon / mesh (uses Adventurer's Pack Small visuals as
    placeholders; user swaps via UE editor texture import later)

Usage:
  python scripts/CloneBellOfTheGoatBP.py   # one-time: clone the BP
  python scripts/BuildPorterGoatBell.py    # build the pak
"""
from pathlib import Path
import sys
import shutil
import zipfile
import json
import copy

# Reuse infrastructure from BuildPorterGoat
SCRIPT_DIR = Path(__file__).resolve().parent
sys.path.insert(0, str(SCRIPT_DIR))
import BuildPorterGoat as bpg


BELL_VERSION  = '1.0.0'
BELL_PAK_NAME = 'PorterGoatBell_P'
BELL_WORK_DIR    = bpg.PROJECT_ROOT / 'experiments' / 'portergoat' / 'bell_work'
BELL_STAGING_DIR = bpg.PROJECT_ROOT / 'experiments' / 'portergoat' / 'bell_staging'
BELL_OUTPUT_DIR  = bpg.PROJECT_ROOT / 'experiments' / 'portergoat' / 'bell_output'

# Pre-cooked bell BP (produced by CloneBellOfTheGoatBP.py)
BELL_BP_DIR = bpg.PROJECT_ROOT / 'experiments' / 'portergoat' / 'bell_build'
BELL_BP_NAME = 'BP_BellOfTheGoat'

# The bell BP ships to this path in the pak
BELL_STAGING_PATH = 'Mods/PorterGoat/Items/BP_BellOfTheGoat'


def log(m=''):
    print(m)


def edit_dt_storage_for_bell(data):
    """Add a 'BellOfTheGoat' row to DT_Storage (8x8 grid).

    Cloned from AdventurersPack_Small row template (5x2 by default). We
    retarget:
      - Row name -> 'BellOfTheGoat'
      - InventoryWidth -> 8
      - InventoryHeight -> 8
      - Name (display text) -> 'EpicPacks.AdventurersPack.BellOfTheGoat.Name'
        (string-table key; falls back to row name if not localized)
      - Durability stays -1 (no decay)
    """
    log("    --- DT_Storage: add BellOfTheGoat row ---")
    rows = data['Exports'][0]['Table']['Data']

    # Idempotency
    if any(r.get('Name') == 'BellOfTheGoat' for r in rows):
        log("    NOTE: BellOfTheGoat row already present (idempotent skip)")
        return True

    # Find the AdventurersPack_Small row as the template
    tmpl = next((r for r in rows
                 if r.get('Name') == 'AdventurersPack_Small'), None)
    if tmpl is None:
        log("    ERROR: AdventurersPack_Small template row not found")
        return False

    new_row = copy.deepcopy(tmpl)
    new_row['Name'] = 'BellOfTheGoat'

    # Retarget InventoryWidth and InventoryHeight to 8
    for prop in new_row.get('Value', []):
        pname = prop.get('Name')
        if pname == 'InventoryWidth':
            prop['Value'] = 8
            log(f"    BellOfTheGoat.InventoryWidth = 8")
        elif pname == 'InventoryHeight':
            prop['Value'] = 8
            log(f"    BellOfTheGoat.InventoryHeight = 8")
        elif pname == 'Name':
            # Update display-name string-table key. Game will fall back to row
            # name 'BellOfTheGoat' if the localized string doesn't resolve.
            prop['Value'] = 'EpicPacks.AdventurersPack.BellOfTheGoat.Name'
            log(f"    BellOfTheGoat.Name (display key) -> "
                f"'EpicPacks.AdventurersPack.BellOfTheGoat.Name'")
        elif pname == 'EnabledState':
            prop['Value'] = 'ERowEnabledState::Live'

    rows.append(new_row)
    bpg.ensure_namemap_entry(data, 'BellOfTheGoat')
    bpg.ensure_namemap_entry(data, 'EpicPacks.AdventurersPack.BellOfTheGoat.Name')
    log(f"    DT_Storage row count: {len(rows)}")
    return True


def main():
    log(f"=== BuildPorterGoatBell v{BELL_VERSION} ===")
    log(f"Standalone bell pak - Architecture C (EpicPack-style equipable).")
    log()

    # Sanity: pre-cooked BP must exist
    pre_uasset = BELL_BP_DIR / f'{BELL_BP_NAME}.uasset'
    pre_uexp = pre_uasset.with_suffix('.uexp')
    if not (pre_uasset.exists() and pre_uexp.exists()):
        log(f"ERROR: pre-cooked bell BP missing at {pre_uasset}")
        log(f"  run scripts/CloneBellOfTheGoatBP.py first")
        sys.exit(1)
    log(f"[0/7] Pre-cooked bell BP found: "
        f"{pre_uasset.stat().st_size} + {pre_uexp.stat().st_size} bytes")
    log()

    log("[1/7] Cleaning bell dirs...")
    for d in [BELL_WORK_DIR, BELL_STAGING_DIR, BELL_OUTPUT_DIR]:
        bpg.rmtree_safe(d)
        d.mkdir(parents=True, exist_ok=True)
    log("  Done.")
    log()

    # DT_Storage round-trip + add BellOfTheGoat row
    log("[2/7] Round-tripping DT_Storage with BellOfTheGoat row...")
    src_uasset = bpg.LEGACY_ROOT / 'Tech' / 'Data' / 'Items' / 'DT_Storage.uasset'
    src_uexp = src_uasset.with_suffix('.uexp')
    if not (src_uasset.exists() and src_uexp.exists()):
        log(f"ERROR: legacy DT_Storage missing at {src_uasset}")
        sys.exit(1)

    work_uasset = BELL_WORK_DIR / 'DT_Storage.uasset'
    work_uexp = BELL_WORK_DIR / 'DT_Storage.uexp'
    shutil.copy2(src_uasset, work_uasset)
    shutil.copy2(src_uexp, work_uexp)

    work_json = BELL_WORK_DIR / 'DT_Storage.json'
    if not bpg.run_uassetgui_tojson(work_uasset, work_json):
        log("ERROR: tojson DT_Storage failed")
        sys.exit(1)

    log("[3/7] Editing DT_Storage...")
    with open(work_json, 'r', encoding='utf-8') as f:
        data = json.load(f)
    if not edit_dt_storage_for_bell(data):
        log("ERROR: edit_dt_storage_for_bell failed")
        sys.exit(1)
    modified_json = BELL_WORK_DIR / 'DT_Storage_modified.json'
    with open(modified_json, 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=2)

    log("[4/7] fromjson DT_Storage...")
    out_uasset = BELL_WORK_DIR / 'DT_Storage_out.uasset'
    if not bpg.run_uassetgui_fromjson(modified_json, out_uasset):
        log("ERROR: fromjson DT_Storage failed")
        sys.exit(1)
    out_uexp = out_uasset.with_suffix('.uexp')
    if not (out_uasset.exists() and out_uexp.exists()):
        log("ERROR: fromjson output missing")
        sys.exit(1)
    log(f"  DT_Storage: {out_uasset.stat().st_size} + {out_uexp.stat().st_size} bytes")

    log("[5/7] Round-trip validation (tojson on modified DT_Storage)...")
    validate_json = BELL_WORK_DIR / 'DT_Storage_validate.json'
    if not bpg.run_uassetgui_tojson(out_uasset, validate_json):
        log("ERROR: round-trip validation failed")
        sys.exit(1)
    with open(validate_json, 'r', encoding='utf-8') as f:
        v = json.load(f)
    bell_row = next((r for r in v['Exports'][0]['Table']['Data']
                     if r.get('Name') == 'BellOfTheGoat'), None)
    if bell_row is None:
        log("ERROR: BellOfTheGoat row missing after round-trip")
        sys.exit(1)
    w_prop = next((p for p in bell_row['Value']
                   if p.get('Name') == 'InventoryWidth'), None)
    h_prop = next((p for p in bell_row['Value']
                   if p.get('Name') == 'InventoryHeight'), None)
    if not (w_prop and h_prop):
        log("ERROR: InventoryWidth/Height missing after round-trip")
        sys.exit(1)
    if w_prop['Value'] != 8 or h_prop['Value'] != 8:
        log(f"ERROR: grid size drift after round-trip: "
            f"{w_prop['Value']}x{h_prop['Value']} (expected 8x8)")
        sys.exit(1)
    log(f"  Round-trip OK: BellOfTheGoat row present with 8x8 grid")
    log()

    log("[6/7] Staging assets...")
    # Stage modified DT_Storage
    dt_dst_dir = (BELL_STAGING_DIR / 'Moria' / 'Content'
                  / 'Tech' / 'Data' / 'Items')
    dt_dst_dir.mkdir(parents=True, exist_ok=True)
    shutil.copy2(out_uasset, dt_dst_dir / 'DT_Storage.uasset')
    shutil.copy2(out_uexp, dt_dst_dir / 'DT_Storage.uexp')
    log("  Staged: Moria/Content/Tech/Data/Items/DT_Storage")

    # Stage pre-cooked bell BP
    bp_dst_dir = (BELL_STAGING_DIR / 'Moria' / 'Content'
                  / Path(BELL_STAGING_PATH).parent)
    bp_dst_dir.mkdir(parents=True, exist_ok=True)
    bp_name = Path(BELL_STAGING_PATH).name
    shutil.copy2(pre_uasset, bp_dst_dir / f'{bp_name}.uasset')
    shutil.copy2(pre_uexp, bp_dst_dir / f'{bp_name}.uexp')
    log(f"  Staged: Moria/Content/{BELL_STAGING_PATH}")
    log()

    log("[7/7] retoc to-zen ...")
    if not bpg.run_retoc_tozen(BELL_STAGING_DIR, BELL_OUTPUT_DIR, BELL_PAK_NAME):
        log("ERROR: retoc to-zen failed")
        log("       Cross-package validation may have caught an issue.")
        sys.exit(1)

    pak = BELL_OUTPUT_DIR / f'{BELL_PAK_NAME}.pak'
    ucas = BELL_OUTPUT_DIR / f'{BELL_PAK_NAME}.ucas'
    utoc = BELL_OUTPUT_DIR / f'{BELL_PAK_NAME}.utoc'
    for f in [pak, ucas, utoc]:
        if f.exists():
            log(f"  {f.name}: {f.stat().st_size} bytes")
    log()

    zip_path = bpg.DOWNLOADS_DIR / f'PorterGoatBell_v{BELL_VERSION}.zip'
    with zipfile.ZipFile(zip_path, 'w', zipfile.ZIP_DEFLATED) as z:
        for f in [pak, ucas, utoc]:
            if f.exists():
                z.write(f, arcname=f.name)
                log(f"  Added: {f.name}")
    log()
    log(f"  Output: {zip_path} ({zip_path.stat().st_size} bytes)")
    log()
    log('=' * 60)
    log(f"  PorterGoatBell v{BELL_VERSION} -- BUILD SUCCESSFUL")
    log()
    log(f"  Ships:")
    log(f"    - BP_BellOfTheGoat at {BELL_STAGING_PATH}")
    log(f"      (cloned from BP_EpicPack_AdventurersPack_Small)")
    log(f"    - DT_Storage with new row 'BellOfTheGoat' (8x8 grid)")
    log()
    log(f"  Architecture C: bell occupies pack slot, equipping grants 8x8 grid.")
    log(f"  Standalone pak. Cross-pak compatible (no BP_NpcGoat or")
    log(f"  BP_StoryManager modifications).")
    log()
    log(f"  Runtime side (VS-Claude):")
    log(f"    - Hook OnItemEquipped on player, filter by class=BP_BellOfTheGoat_C")
    log(f"    - On equip: SpawnActor<BP_NpcGoat_C>(player.location)")
    log(f"    - Hook E-interact on goat: draw custom Stay/Follow/Dismiss/Inventory")
    log(f"      overlay via UE4SS UI")
    log()
    log(f"  Deferred to v1.1.0:")
    log(f"    - Crafting recipe (1 Ironwood + 1 Bronze Bar)")
    log(f"    - Custom bell icon/mesh (currently uses pack visuals)")
    log()
    log(f"  Pak: {BELL_PAK_NAME}")
    log(f"  Zip: {zip_path}")
    log(f"  Install: extract zip to <game>/Moria/Content/Paks/~mods/")
    log('=' * 60)


if __name__ == '__main__':
    main()
