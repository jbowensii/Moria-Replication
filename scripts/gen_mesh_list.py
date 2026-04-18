"""Generate list of mesh asset paths for UModel export."""
import subprocess
import os

BASE = r"C:\Users\johnb\OneDrive\Documents\Projects\Moria-Replication\tools\extracted-assets\Moria\Content"
OUT = r"C:\Users\johnb\OneDrive\Documents\Projects\Moria-Replication\tools\mesh-asset-list.txt"

ps = (
    f"Get-ChildItem -Path '{BASE}' -Include 'SM_*.uasset','SK_*.uasset' "
    f"-Recurse -File | ForEach-Object {{ $_.FullName }}"
)
r = subprocess.run(
    ["powershell", "-NoProfile", "-Command", ps],
    capture_output=True, text=True, errors="replace", timeout=120
)
lines = [l.strip() for l in r.stdout.strip().splitlines() if l.strip()]

paths = []
prefix = BASE + os.sep
for l in lines:
    if l.startswith(prefix):
        rel = l[len(prefix):]
    else:
        rel = l
    rel = rel.replace(os.sep, "/").replace(".uasset", "")
    paths.append(rel)

print(f"Total mesh assets: {len(paths)}")
for p in paths[:5]:
    print(f"  {p}")

with open(OUT, "w") as f:
    for p in paths:
        f.write(p + "\n")
print(f"Written to {OUT}")
