"""Export remaining textures via UModel."""
import subprocess
import os
from pathlib import Path

UMODEL = str(Path("tools/umodel/umodel_64.exe").resolve())
PAKS = r"C:\Program Files\Epic Games\ReturnToMoria\Moria\Content\Paks"
OUT_DIR = str(Path("tools/umodel-textures-remaining").resolve())

with open("tools/texture-export-list.txt") as f:
    textures = [l.strip() for l in f if l.strip()]

print(f"Exporting {len(textures)} textures via UModel...")

for i, t in enumerate(textures):
    name = Path(t).name
    cmd = [UMODEL, "-export", "-png", "-out=" + OUT_DIR, "-path=" + PAKS, "-game=ue4.27", t]
    print(f"[{i+1}/{len(textures)}] {name}...", end=" ", flush=True)
    try:
        result = subprocess.run(cmd, capture_output=True, text=True, timeout=30)
        combined = result.stdout + result.stderr
        if "ERROR" in combined.upper() or result.returncode != 0:
            print(f"FAIL (rc={result.returncode})")
            print(f"  {combined[-150:].strip()}")
        else:
            print("OK")
    except Exception as e:
        print(f"ERROR: {e}")

print("Done.")
