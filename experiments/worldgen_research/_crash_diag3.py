"""_crash_diag3.py — diff GuaranteedConnections + LCs vs the pre-routing-fix snapshot."""
import json
from pathlib import Path

WGR = Path(__file__).resolve().parent

def load(name):
    with open(WGR / name, 'r', encoding='utf-8') as f:
        d = json.load(f)
    table = d['Exports'][0].get('Table', {})
    rows = table.get('Data', []) if 'Data' in table else (table.get('Value', []) or [])
    return d, rows

# Compare current vs before_lvfix landmarks
def lm_summary(rows):
    """Return {row_name: (BasePosition.Z, [GC TagNames], bExtFlag, EnabledState)} for live."""
    out = {}
    for r in rows:
        n = r.get('Name')
        if not n: continue
        bz = None
        gcs = []
        ext = None
        state = None
        for p in r.get('Value', []) or []:
            if not isinstance(p, dict): continue
            nm = p.get('Name')
            v = p.get('Value')
            if nm == 'BasePosition' and isinstance(v, list) and v and isinstance(v[0], dict):
                inner = v[0].get('Value')
                if isinstance(inner, dict):
                    bz = inner.get('Z')
            elif nm == 'GuaranteedConnections' and isinstance(v, list):
                for e in v:
                    if isinstance(e, dict):
                        ev = e.get('Value')
                        if isinstance(ev, list):
                            for it in ev:
                                if isinstance(it, dict) and it.get('Name') == 'TagName':
                                    gcs.append(it.get('Value'))
            elif nm == 'bExtendedConnectivityLandmark':
                ext = v
            elif nm == 'EnabledState':
                state = str(v).split('::')[-1]
        out[n] = (bz, sorted(gcs), ext, state)
    return out

print('Loading current and pre-routing-fix landmark snapshots...')
_, cur_rows = load('DT_Moria_Landmarks.json')
_, pre_rows = load('DT_Moria_Landmarks.before_lvfix.json')

cur = lm_summary(cur_rows)
pre = lm_summary(pre_rows)

print(f'  current: {len(cur)} rows  /  before_lvfix: {len(pre)} rows')

# Diff GuaranteedConnections per landmark — list new GCs added since pre
print('\n=== Landmarks with new GCs (added since before_lvfix) ===')
all_gc_diffs = []
for n, (bz, gcs, ext, st) in cur.items():
    p = pre.get(n)
    if not p:
        if gcs:
            all_gc_diffs.append((n, set(gcs), set(), 'NEW LANDMARK'))
        continue
    pgcs = set(p[1])
    cgcs = set(gcs)
    added = cgcs - pgcs
    removed = pgcs - cgcs
    if added or removed:
        all_gc_diffs.append((n, added, removed, ''))

for n, added, removed, note in all_gc_diffs:
    if added or removed:
        print(f'  {n} {note}')
        for a in sorted(added):    print(f'      + {a}')
        for r in sorted(removed):  print(f'      - {r}')

# Diff LayoutConnections rows by name
print('\n=== LayoutConnections row name diff ===')
_, cur_lc = load('DT_Moria_LayoutConnections.json')
# Best available pre-routing-fix backup is before_fix5 (before any routing fix)
try:
    _, pre_lc = load('DT_Moria_LayoutConnections.before_fix5.json')
except Exception:
    pre_lc = None

cur_names = {r.get('Name') for r in cur_lc}
if pre_lc is not None:
    pre_names = {r.get('Name') for r in pre_lc}
    added_lc = cur_names - pre_names
    print(f'  LC rows added since before_fix5: {len(added_lc)}')
    for n in sorted(added_lc):
        print(f'    + {n}')
    print(f'  LC rows removed since before_fix5: {len(pre_names - cur_names)}')
    for n in sorted(pre_names - cur_names):
        print(f'    - {n}')

# Now the meaty one: for any NEW GC added, check whether the target landmark
# is hosted in any Live SS zone — these would be the H1 candidates that are
# CAUSED by the routing fix.
print('\n=== Newly-added GC entries pointing to unhosted landmarks ===')
# Reload landmark hosting info (Live SS only)
_, zones_rows = load('DT_Moria_Zones.json')
def is_live(r):
    p = next((p for p in r.get('Value', []) if isinstance(p, dict) and p.get('Name') == 'EnabledState'), None)
    return (str(p.get('Value', '')).split('::')[-1] != 'Disabled') if p else True

ss_zones_rows = [r for r in zones_rows if is_live(r)
                 and any(p.get('Name') == 'ZoneSet' and str(p.get('Value','')).endswith('SandboxSmall')
                         for p in r.get('Value', []) if isinstance(p, dict))]
landmark_hosts = {}
for zr in ss_zones_rows:
    for p in zr.get('Value', []):
        if isinstance(p, dict) and p.get('Name') == 'LandmarkHandles':
            for e in (p.get('Value') or []):
                if not isinstance(e, dict): continue
                inner = e.get('Value')
                if isinstance(inner, list):
                    for ip in inner:
                        if isinstance(ip, dict) and ip.get('Name') == 'Landmark':
                            iv = ip.get('Value')
                            if isinstance(iv, list):
                                for it in iv:
                                    if isinstance(it, dict) and it.get('Name') == 'RowName':
                                        ln = it.get('Value', '')
                                        if ln and ln != 'None':
                                            landmark_hosts.setdefault(ln, []).append(zr.get('Name'))

unhosted_new_gcs = []
for n, added, _, _ in all_gc_diffs:
    for tag in added:
        if not isinstance(tag, str) or not tag.startswith('World.Landmark.'):
            continue
        short = tag[len('World.Landmark.'):]
        # Match: any landmark whose full name == short or ends with short
        cands = [k for k in cur if k == short or k.endswith('.' + short)]
        live_hosted = [c for c in cands if landmark_hosts.get(c)]
        if not live_hosted:
            unhosted_new_gcs.append((n, tag, cands))

print(f'  {len(unhosted_new_gcs)} newly-added GC entries point to unhosted landmarks:')
for src, tag, cands in unhosted_new_gcs:
    print(f'    SRC={src}  TAG={tag}  candidates={cands}')

# Same for new LC endpoints
print('\n=== New LC rows whose endpoints reference unhosted landmarks ===')
if pre_lc is not None:
    new_lc_rows = [r for r in cur_lc if r.get('Name') in (cur_names - pre_names)]
    bad = []
    for r in new_lc_rows:
        for key in ('OriginLandmark', 'DestinationLandmark'):
            for p in r.get('Value', []):
                if isinstance(p, dict) and p.get('Name') == key:
                    v = p.get('Value')
                    rn = None
                    if isinstance(v, list):
                        for it in v:
                            if isinstance(it, dict) and it.get('Name') == 'RowName':
                                rn = it.get('Value', '')
                            elif isinstance(it, dict) and isinstance(it.get('Value'), list):
                                for sub in it['Value']:
                                    if isinstance(sub, dict) and sub.get('Name') == 'RowName':
                                        rn = sub.get('Value', '')
                    if rn and rn != 'None':
                        if not landmark_hosts.get(rn):
                            bad.append((r.get('Name'), key, rn))
    for nm, key, rn in bad:
        print(f'    {nm} {key}={rn}  NOT HOSTED')
    if not bad:
        print('    none')
