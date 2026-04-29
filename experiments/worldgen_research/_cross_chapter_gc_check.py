"""Flag any GuaranteedConnection that crosses a chapter-Layer boundary —
the exact failure mode that's crashed the pathfinder (L2_RouteInterzoneConnections
null-deref) repeatedly.

A GC is "risky" if:
  - source landmark is attached to a zone whose chapter has Layer L_src
  - target landmark is attached to a zone whose chapter has Layer L_dst
  - L_src != L_dst  (the GC tries to route across chapter boundaries)

Clean output = safe to build. Risky lines = will likely crash at runtime."""
import json
from pathlib import Path

HERE = Path(__file__).parent
z = json.loads((HERE / 'DT_Moria_Zones.json').read_text(encoding='utf-8'))
lm = json.loads((HERE / 'DT_Moria_Landmarks.json').read_text(encoding='utf-8'))
ch = json.loads((HERE / 'DT_Moria_Chapters.json').read_text(encoding='utf-8'))


def fp(v, n):
    for p in v or []:
        if isinstance(p, dict) and p.get('Name') == n:
            return p
    return None


def get(r, k):
    p = fp(r['Value'], k)
    if not p: return None
    v = p.get('Value')
    if isinstance(v, list):
        for it in v:
            if isinstance(it, dict) and it.get('Name') == 'RowName':
                return it.get('Value', '')
    return v


# Build chapter Layer lookup
chap_layer = {}
for r in ch['Exports'][0]['Table']['Data']:
    L = get(r, 'Layer')
    if L is not None:
        chap_layer[r['Name']] = L

# Build landmark-to-host-chapter lookup
# (a landmark may be attached to multiple zones — collect all)
def chap_of(zr):
    c = fp(zr['Value'], 'Chapter')
    if c:
        for it in (c.get('Value') or []):
            if isinstance(it, dict) and it.get('Name') == 'RowName':
                return it.get('Value', '')
    return ''


def zone_state(zr):
    es = fp(zr['Value'], 'EnabledState')
    return str(es.get('Value', '')).split('::')[-1] if es else '?'


# Only look at LIVE zones — disabled zones don't participate in generation
live_zones = [r for r in z['Exports'][0]['Table']['Data']
              if zone_state(r) == 'Live']

lm_to_hosts = {}  # landmark name -> list of (host_zone, host_chapter, host_layer)
for zr in live_zones:
    lh = fp(zr['Value'], 'LandmarkHandles')
    if not lh: continue
    for e in (lh.get('Value') or []):
        for sub in (e.get('Value') or []):
            if isinstance(sub, dict) and sub.get('Name') == 'Landmark':
                for it in (sub.get('Value') or []):
                    if isinstance(it, dict) and it.get('Name') == 'RowName':
                        lname = it.get('Value', '')
                        if lname:
                            c = chap_of(zr)
                            layer = chap_layer.get(c)
                            lm_to_hosts.setdefault(lname, []).append((zr['Name'], c, layer))


# For each landmark row with non-empty GC, check each target's host layer
print('=== CROSS-CHAPTER GC RISK AUDIT ===')
print()

risky = []
ok_crossings_via_stair = []
same_chapter = 0
for r in lm['Exports'][0]['Table']['Data']:
    gc = fp(r['Value'], 'GuaranteedConnections')
    if not gc: continue
    tags = []
    for it in (gc.get('Value') or []):
        for sub in (it.get('Value') or []):
            if isinstance(sub, dict) and sub.get('Name') == 'TagName':
                v = sub.get('Value', '')
                if v.startswith('World.Landmark.'):
                    tags.append(v[len('World.Landmark.'):])
    if not tags: continue

    src_name = r['Name']
    if src_name not in lm_to_hosts: continue  # not attached to any live zone
    src_hosts = lm_to_hosts[src_name]

    # Check extended-connectivity flag for context
    # (bExtendedConnectivityLandmark is on the LH ENTRY in the zone, not on the
    # landmark row itself, so we need to check each host zone's LH for this src)
    def is_stair_in_zone(zone_row, lname):
        lh = fp(zone_row['Value'], 'LandmarkHandles')
        if not lh: return False
        for e in (lh.get('Value') or []):
            row_name = ''; ext = False
            for sub in (e.get('Value') or []):
                if isinstance(sub, dict):
                    if sub.get('Name') == 'Landmark':
                        for it in (sub.get('Value') or []):
                            if isinstance(it, dict) and it.get('Name') == 'RowName':
                                row_name = it.get('Value', '')
                    elif sub.get('Name') == 'bExtendedConnectivityLandmark':
                        ext = sub.get('Value') is True
            if row_name == lname and ext: return True
        return False

    for src_zone, src_chap, src_layer in src_hosts:
        src_is_stair = any(is_stair_in_zone(zr, src_name) for zr in live_zones
                            if zr['Name'] == src_zone)
        for target in tags:
            # Does target exist as a landmark row?
            if target not in lm_to_hosts:
                risky.append({
                    'kind': 'TARGET NOT ATTACHED',
                    'src': src_name, 'src_zone': src_zone, 'src_layer': src_layer,
                    'tgt': target, 'tgt_zone': '(unattached)', 'tgt_layer': None,
                })
                continue
            for tgt_zone, tgt_chap, tgt_layer in lm_to_hosts[target]:
                tgt_is_stair = any(is_stair_in_zone(zr, target) for zr in live_zones
                                    if zr['Name'] == tgt_zone)
                if src_layer == tgt_layer:
                    same_chapter += 1
                    continue
                entry = {
                    'src': src_name, 'src_zone': src_zone, 'src_chap': src_chap, 'src_layer': src_layer,
                    'tgt': target, 'tgt_zone': tgt_zone, 'tgt_chap': tgt_chap, 'tgt_layer': tgt_layer,
                    'delta': abs((src_layer or 0) - (tgt_layer or 0)),
                    'src_stair': src_is_stair, 'tgt_stair': tgt_is_stair,
                }
                # Cross-chapter GC between stairs is the intended pattern for
                # stair-to-stair forced links and sometimes works. Still risky.
                if src_is_stair or tgt_is_stair:
                    ok_crossings_via_stair.append(entry)
                else:
                    risky.append(entry)

print(f'  Same-chapter GCs (safe):       {same_chapter}')
print(f'  Cross-chapter via stair:       {len(ok_crossings_via_stair)}  (tolerated but still risky)')
print(f'  Cross-chapter NON-stair GCs:   {len(risky)}  <-- LIKELY CRASH IF > 0')

if risky:
    print()
    print('  === RISKY (likely crash the pathfinder) ===')
    for e in risky:
        if 'kind' in e and e['kind'] == 'TARGET NOT ATTACHED':
            print(f'    {e["src"]:<32}  in ch-Layer{e["src_layer"]:+d}  GC -> {e["tgt"]}   (target NOT ATTACHED to any Live zone)')
        else:
            print(f'    {e["src"]:<32}  Layer{e["src_layer"]:+d}  ->  {e["tgt"]}  Layer{e["tgt_layer"]:+d}   (delta {e["delta"]})')
            print(f'        src zone: {e["src_zone"]} in {e["src_chap"]}')
            print(f'        tgt zone: {e["tgt_zone"]} in {e["tgt_chap"]}')
else:
    print()
    print('  ==> No non-stair cross-chapter GCs detected. Safe from this failure mode.')

if ok_crossings_via_stair:
    print()
    print('  === Stair-mediated cross-chapter GCs (proceed with caution) ===')
    for e in ok_crossings_via_stair:
        stair_marker = []
        if e['src_stair']: stair_marker.append('src=stair')
        if e['tgt_stair']: stair_marker.append('tgt=stair')
        print(f'    {e["src"]:<32}  Layer{e["src_layer"]:+d}  ->  {e["tgt"]:<32}  Layer{e["tgt_layer"]:+d}   [{"/".join(stair_marker)}]')
