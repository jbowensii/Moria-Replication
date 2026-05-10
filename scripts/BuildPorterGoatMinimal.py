#!/usr/bin/env python3
"""
BuildPorterGoatMinimal.py — minimum-viable goat-rescue mod (v2.0.0).

Single DataTable edit:
  DT_Moria_AIChallengeSpawns.SurvivorRescue2.CharactersToSpawn += BP_NpcGoat_C

Nothing else.  No modifications to BP_NpcGoat, BP_NPCManager, BP_FGKDwarf,
BP_MoriaGameMode_MainMenu, DT_NPCRoles, or any other asset.

This is a baseline test:
  - Does the goat spawn at the SurvivorRescue2 location?
  - Does the standard rescue prompt fire on the goat?
  - Does the rescue confirm complete the recruitment?
  - Does the goat persist across save/reload?

If shipping content alone covers all these, we ship v2.0.0 and call it done.
If something fails, the v1.x.x edit list (in BuildPorterGoat.py) provides
the remediation menu.

Pipeline (same as CleanSweep):
  1. UAssetGUI tojson on DT_Moria_AIChallengeSpawns.uasset
  2. Append BP_NpcGoat_C entry to SurvivorRescue2.CharactersToSpawn map
  3. UAssetGUI fromjson back
  4. retoc to-zen -> IoStore .pak/.utoc/.ucas
  5. Zip to ~/Downloads/PorterGoat_v2.0.0.zip

Usage:
    python scripts/BuildPorterGoatMinimal.py
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
SCRIPT_DIR   = Path(__file__).resolve().parent
PROJECT_ROOT = SCRIPT_DIR.parent

EXPERIMENT_DIR = PROJECT_ROOT / 'experiments' / 'portergoat_minimal'
WORK_DIR       = EXPERIMENT_DIR / 'work'
STAGING_DIR    = EXPERIMENT_DIR / 'staging'
OUTPUT_DIR     = EXPERIMENT_DIR / 'output'
DOWNLOADS_DIR  = Path(os.path.expanduser('~/Downloads'))

LEGACY_ROOT = PROJECT_ROOT / 'tools' / 'legacy-assets' / 'Moria' / 'Content'

RETOC_EXE     = PROJECT_ROOT / 'tools' / 'retoc' / 'bin' / 'retoc.exe'
UASSETGUI_EXE = PROJECT_ROOT / 'tools' / 'UAssetGUI' / 'UAssetGUI.exe'

UE_VERSION    = 'VER_UE4_27'
RETOC_VERSION = 'UE4_27'

MOD_VERSION = '2.0.0'
PAK_NAME    = 'PorterGoat_P'

NPCGOAT_CLASS_PATH    = '/Game/Character/NpcGoat/BP_NpcGoat.BP_NpcGoat_C'
NPCGOAT_PACKAGE_PATH  = '/Game/Character/NpcGoat/BP_NpcGoat'

# Single asset to modify
ASSET_REL = 'Tech/Data/GameWorld/DT_Moria_AIChallengeSpawns'
ASSET_NAME = 'DT_Moria_AIChallengeSpawns'


# ---------------------------------------------------------------------------
# Helpers
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


def run_uassetgui_tojson(uasset_path, json_output):
    cmd = [str(UASSETGUI_EXE), 'tojson', str(uasset_path), str(json_output), UE_VERSION]
    r = subprocess.run(cmd, capture_output=True, text=True, timeout=60)
    if r.returncode != 0:
        log(f"    FAIL tojson exit={r.returncode}\n    {r.stderr[:500]}")
        return False
    return True


def run_uassetgui_fromjson(json_path, uasset_output):
    cmd = [str(UASSETGUI_EXE), 'fromjson', str(json_path), str(uasset_output), UE_VERSION]
    r = subprocess.run(cmd, capture_output=True, text=True, timeout=60)
    if r.returncode != 0:
        log(f"    FAIL fromjson exit={r.returncode}\n    {r.stderr[:500]}")
        return False
    return True


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


def ensure_namemap_entry(data, name):
    nm = data.get('NameMap', [])
    if name not in nm:
        nm.append(name)
        data['NameMap'] = nm


def edit_ai_challenge_spawns(data):
    """Append BP_NpcGoat_C entry to SurvivorRescue2.CharactersToSpawn map.

    The CharactersToSpawn map is a TMap<TSoftClassPtr<>, uint32>.  It already
    contains:
      [BP_NpcDwarf_Survivor_2_C, 1]
      [BP_Monster_Wolf_C, 1]
    We add a third entry:
      [BP_NpcGoat_C, 1]
    """
    rows = data['Exports'][0]['Table']['Data']
    target_row = next((r for r in rows if r.get('Name') == 'SurvivorRescue2'), None)
    if target_row is None:
        log("    ERROR: SurvivorRescue2 row not found"); return False

    map_prop = next((p for p in target_row['Value']
                     if isinstance(p, dict) and p.get('Name') == 'CharactersToSpawn'), None)
    if map_prop is None:
        log("    ERROR: CharactersToSpawn map not found"); return False

    entries = map_prop.get('Value', [])
    for pair in entries:
        if isinstance(pair, list) and len(pair) == 2:
            kv = pair[0].get('Value', {}) if isinstance(pair[0], dict) else {}
            ap = kv.get('AssetPath', {}) if isinstance(kv, dict) else {}
            if isinstance(ap, dict) and ap.get('AssetName') == NPCGOAT_CLASS_PATH:
                log("    NOTE: BP_NpcGoat_C already in map (idempotent skip)")
                return True

    if not entries:
        log("    ERROR: CharactersToSpawn map empty"); return False

    template = copy.deepcopy(entries[0])
    if isinstance(template, list) and len(template) == 2:
        ap = template[0]['Value']['AssetPath']
        ap['AssetName'] = NPCGOAT_CLASS_PATH
        template[1]['Value'] = 1

    entries.append(template)
    log(f"    SurvivorRescue2.CharactersToSpawn += {NPCGOAT_CLASS_PATH}")
    log(f"    Map entries: {len(entries)}")

    for n in [NPCGOAT_PACKAGE_PATH, NPCGOAT_CLASS_PATH]:
        ensure_namemap_entry(data, n)
    return True


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

def main():
    log(f"=== BuildPorterGoatMinimal v{MOD_VERSION} ===\n")
    log("Single edit:")
    log("  DT_Moria_AIChallengeSpawns.SurvivorRescue2.CharactersToSpawn")
    log(f"    += {NPCGOAT_CLASS_PATH}")
    log("Nothing else modified.\n")

    # ------------------------------------------------------------------ 1
    log("[1/6] Pre-flight checks...")
    src_uasset = LEGACY_ROOT / f'{ASSET_REL}.uasset'
    src_uexp   = LEGACY_ROOT / f'{ASSET_REL}.uexp'
    for p in (src_uasset, src_uexp, RETOC_EXE, UASSETGUI_EXE):
        if not p.exists():
            log(f"  ERROR: missing {p}"); sys.exit(1)
    log("  OK\n")

    # ------------------------------------------------------------------ 2
    log("[2/6] Cleaning work dirs...")
    for d in (WORK_DIR, STAGING_DIR, OUTPUT_DIR):
        rmtree_safe(d); d.mkdir(parents=True, exist_ok=True)
    log("  OK\n")

    # ------------------------------------------------------------------ 3
    log(f"[3/6] tojson + edit + fromjson on {ASSET_NAME}...")
    work_uasset = WORK_DIR / f'{ASSET_NAME}.uasset'
    work_uexp   = WORK_DIR / f'{ASSET_NAME}.uexp'
    shutil.copy2(src_uasset, work_uasset)
    shutil.copy2(src_uexp, work_uexp)

    work_json = WORK_DIR / f'{ASSET_NAME}.json'
    if not run_uassetgui_tojson(work_uasset, work_json):
        sys.exit(1)

    with open(work_json, 'r', encoding='utf-8') as f:
        data = json.load(f)
    if not edit_ai_challenge_spawns(data):
        sys.exit(1)

    modified_json = WORK_DIR / f'{ASSET_NAME}_modified.json'
    with open(modified_json, 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=2)

    out_uasset = WORK_DIR / f'{ASSET_NAME}_out.uasset'
    if not run_uassetgui_fromjson(modified_json, out_uasset):
        sys.exit(1)
    out_uexp = out_uasset.with_suffix('.uexp')
    log(f"  Output: {out_uasset.stat().st_size} + {out_uexp.stat().st_size} bytes\n")

    # ------------------------------------------------------------------ 4
    log("[4/6] Round-trip validation...")
    validate_json = WORK_DIR / f'{ASSET_NAME}_validate.json'
    if not run_uassetgui_tojson(out_uasset, validate_json):
        log("  ERROR: round-trip failed"); sys.exit(1)
    log("  OK\n")

    # ------------------------------------------------------------------ 5
    log("[5/6] Staging + retoc to-zen...")
    dst_dir = STAGING_DIR / 'Moria' / 'Content' / Path(ASSET_REL).parent
    dst_dir.mkdir(parents=True, exist_ok=True)
    shutil.copy2(out_uasset, dst_dir / f'{ASSET_NAME}.uasset')
    shutil.copy2(out_uexp,   dst_dir / f'{ASSET_NAME}.uexp')
    log(f"  Staged: Moria/Content/{ASSET_REL}")

    if not run_retoc_tozen(STAGING_DIR, OUTPUT_DIR, PAK_NAME):
        log("  ERROR: retoc failed"); sys.exit(1)

    triplet = [OUTPUT_DIR / f'{PAK_NAME}.{ext}' for ext in ('pak', 'ucas', 'utoc')]
    for f in triplet:
        if not f.exists():
            log(f"  ERROR: missing {f.name}"); sys.exit(1)
        log(f"  {f.name}: {f.stat().st_size:,} bytes")

    list_cmd = [str(RETOC_EXE), 'list', str(triplet[2])]
    r = subprocess.run(list_cmd, capture_output=True, text=True, timeout=60)
    if r.returncode == 0:
        export_count = sum(1 for ln in r.stdout.strip().split('\n')
                           if 'ExportBundleData' in ln)
        log(f"  ExportBundleData entries: {export_count} (expected 1 for v{MOD_VERSION})")
    log()

    # ------------------------------------------------------------------ 6
    log("[6/6] Creating distribution zip...")
    DOWNLOADS_DIR.mkdir(parents=True, exist_ok=True)
    zip_path = DOWNLOADS_DIR / f'PorterGoat_v{MOD_VERSION}.zip'
    with zipfile.ZipFile(zip_path, 'w', zipfile.ZIP_DEFLATED) as zf:
        for f in triplet:
            zf.write(f, f.name)
            log(f"  Added: {f.name}")
    log(f"\n  Output: {zip_path} ({zip_path.stat().st_size:,} bytes)")

    log(f"\n{'='*60}")
    log(f"  PorterGoat v{MOD_VERSION} (minimal) -- BUILD SUCCESSFUL")
    log(f"  Single edit:")
    log(f"    DT_Moria_AIChallengeSpawns.SurvivorRescue2.CharactersToSpawn")
    log(f"      += BP_NpcGoat_C  (count=1)")
    log(f"  Pak: {PAK_NAME}  (1 ExportBundleData entry)")
    log(f"  Zip: {zip_path}")
    log(f"  Install: extract zip to <game>/Moria/Content/Paks/<your-versioned-folder>/")
    log(f"{'='*60}")


if __name__ == '__main__':
    main()
