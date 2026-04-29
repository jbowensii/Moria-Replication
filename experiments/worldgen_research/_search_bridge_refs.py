"""Search for bridge chapter references."""
import os
from collections import Counter

TARGETS = ['Moria-DurinTower', 'Moria-DimrillDale', 'Moria-TradingPost']
SCAN_ROOTS = [
    '../../experiments/worldgen_research',
    '../../tools/cloud-exports',
    '../../tools/cloud-exports-by-type',
    '../../tools/extracted-assets',
    '../../tools/cloud-exports-fmodel',
]
SKIP_SUBSTR = ['/backups/', '\\backups\\', '.original.', '.git', '__pycache__']

hits = {t: [] for t in TARGETS}
scanned = 0
for root in SCAN_ROOTS:
    if not os.path.isdir(root):
        continue
    for dirpath, dirs, files in os.walk(root):
        norm = dirpath.replace('\\', '/')
        if any(s in norm for s in SKIP_SUBSTR):
            continue
        for f in files:
            if not f.endswith('.json'):
                continue
            p = os.path.join(dirpath, f)
            try:
                with open(p, encoding='utf-8', errors='ignore') as fh:
                    data = fh.read()
                scanned += 1
                for t in TARGETS:
                    if t in data:
                        hits[t].append(p)
            except Exception:
                pass

print(f'Scanned {scanned} JSON files\n')
for t in TARGETS:
    print(f'=== {t} ===')
    if not hits[t]:
        print('  (no references found)')
    else:
        dirs = Counter(os.path.dirname(p) for p in hits[t])
        for d, ct in dirs.most_common(15):
            print(f'  {ct:>4} files in {d}')
        print(f'  Total: {len(hits[t])} files')
        print('  Sample paths:')
        for p in hits[t][:8]:
            print(f'    {p}')
    print()
