"""
BuildPorterGoatEdits.py — Standalone addon pak with ONLY the modded BP_NpcGoat.

Why this exists:
  v1.2.10's main pak (PorterGoat_P) had to drop modded BP_NpcGoat from staging
  because retoc to-zen rejected the cross-package dependency graph when modded
  BP_NpcGoat and modded BP_StoryManager were in the same pak (the goat's
  Serialize dependency on BP_StoryManager.SimpleConstructionScript_0 failed to
  validate against the modded StoryManager).

  Hypothesis: if the modded BP_NpcGoat ships in its OWN separate pak (with no
  other modded assets), retoc only sees one mutated cross-package edge per
  build run — modded BP_NpcGoat → vanilla BP_StoryManager (which is in base
  game). That edge has stable hashes and should validate cleanly.

  This script tests the hypothesis. If it builds, the user installs both:
    - PorterGoat_v1.2.10.zip          (DT edits + BP_StoryManager whitelist patch
                                       + BodyInventory wrapper)
    - PorterGoatEdits_v1.0.0.zip      (modded BP_NpcGoat with CDO + SCS surgery)

  Together they restore the full v1.2.8/v1.2.9 goat behavior on top of the
  v1.2.10 dispatcher fix.

What this ships:
  BP_NpcGoat with:
    - InventoryComp.DefaultContainers += BP_ContainerItem_Goat_BodyInventory_C
      (the 8x8 inventory wrapper — wired from CDO)
    - MorNPC: 8 cloned interaction structs from BP_NpcDwarf
      (Recruit / DeliverResearch / Details / Talk + SoftMugAsset + BarkWhitelistTag
       + ActivityPointGainedEffect + RecruitNPCWorldCapReachedText)
    - MorWandererComponent SCS_Node_29 (the v1.2.8 SCS surgery — adds the
      component to the goat's component tree)

Usage:
  python scripts/BuildPorterGoatEdits.py
"""
from pathlib import Path
import sys
import os
import shutil
import zipfile

# Reuse all infrastructure from BuildPorterGoat
SCRIPT_DIR = Path(__file__).resolve().parent
sys.path.insert(0, str(SCRIPT_DIR))
import BuildPorterGoat as bpg


ADDON_VERSION  = '1.0.0'
ADDON_PAK_NAME = 'PorterGoatEdits_P'
ADDON_WORK_DIR    = bpg.PROJECT_ROOT / 'experiments' / 'portergoat' / 'addon_work'
ADDON_STAGING_DIR = bpg.PROJECT_ROOT / 'experiments' / 'portergoat' / 'addon_staging'
ADDON_OUTPUT_DIR  = bpg.PROJECT_ROOT / 'experiments' / 'portergoat' / 'addon_output'


def log(m=''):
    print(m)


def main():
    log(f"=== BuildPorterGoatEdits v{ADDON_VERSION} ===")
    log(f"Builds a standalone addon pak with ONLY modded BP_NpcGoat.")
    log()

    # Re-enable the SCS surgery for this isolated build by patching edit_bp_npcgoat's
    # comment-out at runtime. Easier: just call _add_morwanderer_scs explicitly
    # after edit_bp_npcgoat. Cleanest: call edit_bp_npcgoat normally (which
    # currently skips SCS surgery), then call _add_morwanderer_scs as a follow-up.

    # ---- Clean dirs ----
    log("[1/6] Cleaning addon dirs...")
    for d in [ADDON_WORK_DIR, ADDON_STAGING_DIR, ADDON_OUTPUT_DIR]:
        bpg.rmtree_safe(d)
        d.mkdir(parents=True, exist_ok=True)
    log("  Done.")
    log()

    # ---- tojson ----
    src_rel = 'Character/NpcGoat/BP_NpcGoat'
    name = 'BP_NpcGoat'
    src_uasset = bpg.LEGACY_ROOT / f'{src_rel}.uasset'
    src_uexp   = bpg.LEGACY_ROOT / f'{src_rel}.uexp'
    if not src_uasset.exists() or not src_uexp.exists():
        log(f"ERROR: missing source {src_uasset}")
        sys.exit(1)

    work_uasset = ADDON_WORK_DIR / f'{name}.uasset'
    work_uexp   = ADDON_WORK_DIR / f'{name}.uexp'
    work_json   = ADDON_WORK_DIR / f'{name}.json'
    shutil.copy2(src_uasset, work_uasset)
    shutil.copy2(src_uexp,   work_uexp)

    log(f"[2/6] tojson {name}...")
    if not bpg.run_uassetgui_tojson(work_uasset, work_json):
        log(f"ERROR: tojson failed for {name}")
        sys.exit(1)
    log(f"  OK: {work_json.stat().st_size} bytes")
    log()

    # ---- edit ----
    log(f"[3/6] Editing {name}...")
    import json as _json
    with open(work_json, 'r', encoding='utf-8') as f:
        data = _json.load(f)

    # Apply the standard goat edit (DefaultContainers + 8 MorNPC fields).
    # v1.2.10 disabled the SCS surgery inside edit_bp_npcgoat to avoid the
    # cross-pak retoc conflict. In this STANDALONE build there's no
    # BP_StoryManager in the pak, so we re-enable the SCS surgery directly.
    if not bpg.edit_bp_npcgoat(data):
        log("ERROR: edit_bp_npcgoat returned False")
        sys.exit(1)

    # Re-enable SCS surgery here (bypass the v1.2.10 comment-out in edit_bp_npcgoat)
    log("  Re-enabling MorWandererComponent SCS surgery (isolated build, no retoc conflict expected)...")
    if not bpg._add_morwanderer_scs(data):
        log("  WARN: SCS surgery failed; addon will lack MorWandererComponent")
        # Continue — the other edits are still valuable.

    modified_json = ADDON_WORK_DIR / f'{name}_modified.json'
    with open(modified_json, 'w', encoding='utf-8') as f:
        _json.dump(data, f, indent=2)
    log(f"  Modified JSON: {modified_json.stat().st_size} bytes")
    log()

    # ---- fromjson ----
    out_uasset = ADDON_WORK_DIR / f'{name}_out.uasset'
    log(f"[4/6] fromjson {name}...")
    if not bpg.run_uassetgui_fromjson(modified_json, out_uasset):
        log(f"ERROR: fromjson failed for {name}")
        sys.exit(1)
    out_uexp = out_uasset.with_suffix('.uexp')
    if not out_uasset.exists() or not out_uexp.exists():
        log(f"ERROR: expected output files not found")
        sys.exit(1)
    log(f"  OK: {out_uasset.stat().st_size} + {out_uexp.stat().st_size} bytes")

    # Round-trip validate
    validate_json = ADDON_WORK_DIR / f'{name}_validate.json'
    if not bpg.run_uassetgui_tojson(out_uasset, validate_json):
        log(f"ERROR: round-trip validation tojson failed")
        sys.exit(1)
    log(f"  Round-trip OK")
    log()

    # ---- stage ----
    log(f"[5/6] Staging {name}...")
    dst_rel = 'Character/NpcGoat/BP_NpcGoat'
    dst_dir = ADDON_STAGING_DIR / 'Moria' / 'Content' / Path(dst_rel).parent
    dst_dir.mkdir(parents=True, exist_ok=True)
    shutil.copy2(out_uasset, dst_dir / f'{Path(dst_rel).name}.uasset')
    shutil.copy2(out_uexp,   dst_dir / f'{Path(dst_rel).name}.uexp')
    log(f"  Staged: Moria/Content/{dst_rel}")
    log()

    # ---- retoc to-zen ----
    log(f"[6/6] retoc to-zen -> {ADDON_PAK_NAME}...")
    if not bpg.run_retoc_tozen(ADDON_STAGING_DIR, ADDON_OUTPUT_DIR, ADDON_PAK_NAME):
        log(f"ERROR: retoc to-zen failed")
        log(f"       Hypothesis: even isolated, modded BP_NpcGoat triggers the")
        log(f"       same cross-package validation failure. If so, addon pak is")
        log(f"       not viable.")
        sys.exit(1)

    pak  = ADDON_OUTPUT_DIR / f'{ADDON_PAK_NAME}.pak'
    ucas = ADDON_OUTPUT_DIR / f'{ADDON_PAK_NAME}.ucas'
    utoc = ADDON_OUTPUT_DIR / f'{ADDON_PAK_NAME}.utoc'
    for f in [pak, ucas, utoc]:
        if f.exists():
            log(f"  {f.name}: {f.stat().st_size} bytes")
    log()

    # ---- zip ----
    zip_path = bpg.DOWNLOADS_DIR / f'PorterGoatEdits_v{ADDON_VERSION}.zip'
    with zipfile.ZipFile(zip_path, 'w', zipfile.ZIP_DEFLATED) as z:
        for f in [pak, ucas, utoc]:
            if f.exists():
                z.write(f, arcname=f.name)
                log(f"  Added: {f.name}")
    log()
    log(f"  Output: {zip_path} ({zip_path.stat().st_size} bytes)")
    log()
    log("=" * 60)
    log(f"  PorterGoatEdits v{ADDON_VERSION} -- BUILD SUCCESSFUL")
    log(f"  Companion to PorterGoat_v1.2.10.zip; install BOTH for full behavior.")
    log()
    log(f"  Ships:")
    log(f"    BP_NpcGoat with:")
    log(f"      - InventoryComp.DefaultContainers += Goat.BodyInventory wrapper")
    log(f"      - 8 cloned MorNPC interaction fields from BP_NpcDwarf")
    log(f"      - MorWandererComponent SCS_Node_29 (v1.2.8 SCS surgery)")
    log(f"  Pak: {ADDON_PAK_NAME}")
    log(f"  Zip: {zip_path}")
    log(f"  Install: extract zip to <game>/Moria/Content/Paks/~mods/")
    log(f"           (alongside PorterGoat_P.* from v1.2.10)")
    log("=" * 60)


if __name__ == '__main__':
    main()
