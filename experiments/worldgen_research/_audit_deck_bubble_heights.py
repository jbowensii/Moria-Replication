"""For each of the 4 new ZoneDeck rows, list every bubble it references
and report the bubble's Z height in zone cells. Z height is derived from
the BubbleDefinition (BF_BB_*.json) SupportedInterfaces field — each
entry's Subcell.Z gives the cell coordinates the bubble occupies; size_Z
is max-min+1 across them.
"""
import json, os, glob

PROJ = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..'))
BF_ROOTS = [
    os.path.join(PROJ, 'tools', 'cloud-exports-by-type', 'MorBubbleDefinition'),
    os.path.join(PROJ, 'tools', 'cloud-exports', 'Tech', 'Data', 'BubbleDefs'),
    os.path.join(PROJ, 'tools', 'fmodel-export', 'Exports', 'Moria', 'Content', 'Tech', 'Data', 'BubbleDefs'),
]

# Build BF index: bubble name -> filepath
bf_index = {}
for root in BF_ROOTS:
    if not os.path.isdir(root): continue
    for fp in glob.glob(os.path.join(root, '**', 'BF_BB_*.json'), recursive=True):
        stem = os.path.splitext(os.path.basename(fp))[0]  # BF_BB_xxx
        bb_name = stem[3:]  # drop "BF_" -> "BB_xxx"
        if bb_name not in bf_index:
            bf_index[bb_name] = fp

def bubble_size_z(bubble_name):
    fp = bf_index.get(bubble_name)
    if not fp: return None, None  # (size_z, source)
    try:
        d = json.load(open(fp, encoding='utf-8'))
    except Exception:
        return None, fp
    for item in d:
        if not isinstance(item, dict): continue
        props = item.get('Properties', {})
        si = props.get('SupportedInterfaces', [])
        if not isinstance(si, list) or not si: continue
        zs = []; xs = []; ys = []
        for entry in si:
            if not isinstance(entry, dict): continue
            k = entry.get('Key', {})
            if isinstance(k, dict):
                sc = k.get('Subcell', {})
                if isinstance(sc, dict):
                    zs.append(sc.get('Z', 0))
                    xs.append(sc.get('X', 0))
                    ys.append(sc.get('Y', 0))
        if zs:
            sx = max(xs) - min(xs) + 1
            sy = max(ys) - min(ys) + 1
            sz = max(zs) - min(zs) + 1
            return (sx, sy, sz), fp
    return (1, 1, 1), fp  # default if no SupportedInterfaces

def fp(v, n):
    for p in v or []:
        if isinstance(p, dict) and p.get('Name') == n: return p
    return None

dk = json.load(open(os.path.join(PROJ, 'experiments', 'worldgen_research', 'DT_Moria_ZoneDeck.json'), encoding='utf-8'))
TARGETS = ['Sandbox_AngryCavernsBubbles1','Sandbox_AngryCavernsPassages1',
           'Sandbox_DesolationBubbles1','Sandbox_DesolationPassages1']

for tgt in TARGETS:
    print('\n=' * 1 + ' ' + tgt + ' ' + '=' * (78 - len(tgt) - 4))
    for r in dk['Exports'][0]['Table']['Data']:
        if r['Name'] != tgt: continue
        de = fp(r['Value'], 'DeckEntries')
        entries = de.get('Value', []) if de else []
        print(f'  Entries: {len(entries)}')
        print(f'  {"Bubble":<46s}  {"X":>3s} {"Y":>3s} {"Z":>3s}  Status')
        print('  ' + '-' * 76)
        for e in entries:
            if not isinstance(e, dict): continue
            inner = e.get('Value', [])
            bb = None
            for sub in inner:
                if isinstance(sub, dict) and sub.get('Name') == 'Bubble':
                    bb = sub.get('Value')
                    break
            if not bb: continue
            size, src = bubble_size_z(bb)
            if size is None:
                print(f'  {bb:<46s}  {"?":>3s} {"?":>3s} {"?":>3s}  no BF file')
            else:
                sx, sy, sz = size
                flag = '  <-- TALLER THAN 1' if sz > 1 else ''
                print(f'  {bb:<46s}  {sx:>3d} {sy:>3d} {sz:>3d}{flag}')
