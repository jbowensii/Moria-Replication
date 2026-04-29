"""_crash_diag.py — Diagnose null-Zone routing crash in SandboxSmall.

Walks all 7 hypotheses for the EXCEPTION_ACCESS_VIOLATION at
FMorLayoutConnectionInstance::GetZone() (offset 0x1a1).

Reads the live JSONs in worldgen_research/. Prints evidence per hypothesis
and a ranked suspect list. Does NOT modify anything.
"""
from __future__ import annotations
import json
from collections import defaultdict
from pathlib import Path

WGR = Path(__file__).resolve().parent

# ----------------------------------------------------------------------------
# Mini DT readers — same shape helpers BuildValidator uses, copied so this
# script runs without importing the editor.
# ----------------------------------------------------------------------------

def load(name):
    with open(WGR / name, 'r', encoding='utf-8') as f:
        d = json.load(f)
    table = d['Exports'][0].get('Table', {})
    rows = table.get('Data', []) if 'Data' in table else (table.get('Value', []) or [])
    return d, rows

def fp(values, n):
    for p in values or []:
        if isinstance(p, dict) and p.get('Name') == n:
            return p
    return None

def get(r, k):
    p = fp(r.get('Value', []), k)
    if not p: return None
    v = p.get('Value')
    if isinstance(v, list):
        for it in v:
            if isinstance(it, dict) and it.get('Name') == 'RowName':
                return it.get('Value', '')
    return v

def zstate(r):
    p = fp(r.get('Value', []), 'EnabledState')
    return str(p.get('Value', '')).split('::')[-1] if p else None

def is_live(r):
    return zstate(r) != 'Disabled'

# ----------------------------------------------------------------------------
# Loaders
# ----------------------------------------------------------------------------

print('Loading DTs ...')
_, zones_rows      = load('DT_Moria_Zones.json')
_, chapters_rows   = load('DT_Moria_Chapters.json')
_, landmarks_rows  = load('DT_Moria_Landmarks.json')
_, conns_rows      = load('DT_Moria_LayoutConnections.json')

# Live SS zones
def is_ss_zone(r):
    zs = fp(r.get('Value', []), 'ZoneSet')
    zsv = str(zs.get('Value', '')).split('::')[-1] if zs else 'None'
    return zsv == 'SandboxSmall'

ss_zones = {r['Name']: r for r in zones_rows if is_live(r) and is_ss_zone(r)}
all_zones = {r['Name']: r for r in zones_rows}

# chapters
ss_chapters = {r['Name']: r for r in chapters_rows
               if r.get('Name', '').startswith('SandboxSmall-chapter-') and is_live(r)}
chap_band = {}
for n, r in ss_chapters.items():
    mn, mx = get(r, 'MinZ'), get(r, 'MaxZ')
    chap_band[n] = (mn, mx)

# landmarks
all_landmarks = {r['Name']: r for r in landmarks_rows}
def landmark_bp_z(name):
    r = all_landmarks.get(name)
    if not r: return None
    p = fp(r.get('Value', []), 'BasePosition')
    if not p: return None
    v = p.get('Value')
    if isinstance(v, list) and v and isinstance(v[0], dict):
        inner = v[0].get('Value')
        if isinstance(inner, dict):
            return inner.get('Z')
    return None

# Build landmark -> hosting Live SS zones map (via LandmarkHandles)
landmark_hosts = defaultdict(list)   # landmark_name -> [zone_name,...]
zone_landmarks = defaultdict(list)   # zone_name -> [landmark_name,...]
for zn, zr in ss_zones.items():
    lh = fp(zr.get('Value', []), 'LandmarkHandles')
    if not lh: continue
    for e in (lh.get('Value') or []):
        if not isinstance(e, dict): continue
        inner = e.get('Value')
        if not isinstance(inner, list): continue
        lhprop = fp(inner, 'Landmark')
        if not lhprop: continue
        lv = lhprop.get('Value')
        if isinstance(lv, list):
            for it in lv:
                if isinstance(it, dict) and it.get('Name') == 'RowName':
                    lname = it.get('Value', '')
                    if lname and lname != 'None':
                        landmark_hosts[lname].append(zn)
                        zone_landmarks[zn].append(lname)

# zone_chapter map
def zone_chapter(zr):
    return get(zr, 'Chapter')

# ----------------------------------------------------------------------------
# Identify the new rows by name pattern
# ----------------------------------------------------------------------------

NEW_LC_HANDOFF = {
    'Sandbox_E_LowerDescent_to_F_CrystalDescent',
    'Sandbox_F_CrystalDescent_to_G_SeventhStair',
    'Sandbox_G_SeventhStair_to_C_SecondStair',
    'Sandbox_C_SecondStair_to_H_NinthStair',
    'Sandbox_H_TenthStair_to_B_FirstStair',
    'Sandbox_B_FourthStair_to_D_ThirdStair',
}

# Floor-internal LCs — try common patterns
floor_internal_lcs = [r for r in conns_rows
                      if isinstance(r.get('Name'), str)
                      and ('Sandbox_Floor' in r['Name'] or '_Internal' in r['Name'])
                      and r['Name'] not in NEW_LC_HANDOFF]

new_handoff_rows = [r for r in conns_rows if r.get('Name') in NEW_LC_HANDOFF]
print(f'Found {len(new_handoff_rows)}/6 handoff LCs, {len(floor_internal_lcs)} floor-internal LCs')

# ----------------------------------------------------------------------------
# H1: GuaranteedConnections referencing landmarks without a Live SS host zone
# ----------------------------------------------------------------------------

print('\n' + '='*72)
print('H1 — GC -> unhosted landmark check')
print('='*72)

h1_bad = []
for lname, lr in all_landmarks.items():
    if not is_live(lr): continue
    gc = fp(lr.get('Value', []), 'GuaranteedConnections')
    if not gc: continue
    gc_v = gc.get('Value') or []
    for e in gc_v:
        if not isinstance(e, dict): continue
        # Each entry has TagName
        inner = e.get('Value')
        if isinstance(inner, list):
            tn = fp(inner, 'TagName')
            if tn:
                tag = tn.get('Value')
                # tag like 'World.Landmark.NinthStair' — strip prefix
                if isinstance(tag, str) and tag.startswith('World.Landmark.'):
                    target_lm_short = tag.split('.')[-1]
                    # Match by suffix: real landmark names end with .ShortName or include it
                    matches = [n for n in all_landmarks
                               if n.endswith('.' + target_lm_short) or n == target_lm_short]
                    # Filter to Live SS-hosted
                    live_hosted = [n for n in matches if landmark_hosts.get(n)]
                    if not live_hosted:
                        h1_bad.append((lname, tag, matches))

print(f'  {len(h1_bad)} GC entries point to landmarks with no Live SS host')
for src, tag, matches in h1_bad[:10]:
    print(f'    {src} -> {tag}  (matches in DT: {len(matches)}, live-hosted: 0)')
if len(h1_bad) > 10: print(f'    ... +{len(h1_bad)-10} more')

# ----------------------------------------------------------------------------
# H2: LC endpoints referencing landmarks not hosted by a Live SS zone
# ----------------------------------------------------------------------------

print('\n' + '='*72)
print('H2 — new LC OriginLandmark/DestinationLandmark hosted?')
print('='*72)

def lc_endpoint(r, key):
    """Read OriginLandmark/DestinationLandmark.RowName."""
    p = fp(r.get('Value', []), key)
    if not p: return None
    v = p.get('Value')
    if isinstance(v, list):
        # struct-of-RowName
        for it in v:
            if isinstance(it, dict) and it.get('Name') == 'RowName':
                return it.get('Value', '')
        # nested (one-element list of dicts containing more lists)
        if v and isinstance(v[0], dict):
            inner = v[0].get('Value')
            if isinstance(inner, list):
                for it in inner:
                    if isinstance(it, dict) and it.get('Name') == 'RowName':
                        return it.get('Value', '')
    return None

h2_bad = []
new_lc_check = list(new_handoff_rows) + floor_internal_lcs
for r in new_lc_check:
    name = r.get('Name')
    o_lm = lc_endpoint(r, 'OriginLandmark')
    d_lm = lc_endpoint(r, 'DestinationLandmark')
    o_zone = get(r, 'OriginZone')
    d_zone = get(r, 'DestinationZone')
    o_hosted = bool(landmark_hosts.get(o_lm)) if o_lm else None
    d_hosted = bool(landmark_hosts.get(d_lm)) if d_lm else None
    o_zone_live = (o_zone in ss_zones) if o_zone else None
    d_zone_live = (d_zone in ss_zones) if d_zone else None
    enabled = zstate(r)
    issue = []
    if o_lm and not o_hosted: issue.append(f'OriginLM={o_lm} NOT HOSTED')
    if d_lm and not d_hosted: issue.append(f'DestLM={d_lm} NOT HOSTED')
    if o_zone and o_zone != 'None' and not o_zone_live:
        issue.append(f'OriginZone={o_zone} not Live-SS')
    if d_zone and d_zone != 'None' and not d_zone_live:
        issue.append(f'DestZone={d_zone} not Live-SS')
    if issue:
        h2_bad.append((name, enabled, o_lm, d_lm, o_zone, d_zone, issue))
    print(f'  {name} [{enabled}]')
    print(f'    OL={o_lm}  hosted={o_hosted}  OZ={o_zone}  liveSS={o_zone_live}')
    print(f'    DL={d_lm}  hosted={d_hosted}  DZ={d_zone}  liveSS={d_zone_live}')
    if issue:
        print(f'    !! {"; ".join(issue)}')

# ----------------------------------------------------------------------------
# H3: bidirectional GCs without matching reverse LCs
# ----------------------------------------------------------------------------

print('\n' + '='*72)
print('H3 — Reverse LC for each direction in chained GCs')
print('='*72)

# Build LC pair set keyed by (OriginLandmark, DestinationLandmark) for ALL Live SS-relevant LCs
SS_REL = ('SandboxSmall', 'All')
lc_pairs = set()
for r in conns_rows:
    if not is_live(r): continue
    zs = fp(r.get('Value', []), 'ZoneSet')
    zsv = str(zs.get('Value', '')).split('::')[-1] if zs else 'None'
    if zsv not in SS_REL: continue
    o = lc_endpoint(r, 'OriginLandmark')
    d = lc_endpoint(r, 'DestinationLandmark')
    if o and d:
        lc_pairs.add((o, d))

# Build the GC chain-implied required pairs from new handoffs
chain_pairs = set()
for r in new_handoff_rows:
    o = lc_endpoint(r, 'OriginLandmark')
    d = lc_endpoint(r, 'DestinationLandmark')
    if o and d:
        chain_pairs.add((o, d))

missing_reverse = []
for (a, b) in chain_pairs:
    if (b, a) not in lc_pairs:
        missing_reverse.append((a, b))

print(f'  {len(chain_pairs)} new handoff LC pairs')
print(f'  {len(missing_reverse)} missing reverse direction:')
for a, b in missing_reverse:
    print(f'    NO REVERSE: ({b} -> {a})')

# ----------------------------------------------------------------------------
# H4: Cloned LC template field comparison vs vanilla stair-related LC
# ----------------------------------------------------------------------------

print('\n' + '='*72)
print('H4 — Field comparison vs Sandbox_ElvenEntranceToPromenade template')
print('='*72)

def row_fields_summary(r):
    out = {}
    for p in r.get('Value', []) or []:
        if isinstance(p, dict):
            n = p.get('Name')
            v = p.get('Value')
            if isinstance(v, (str, int, float, bool)) or v is None:
                out[n] = v
            elif isinstance(v, list) and len(v) <= 1 and v and isinstance(v[0], dict):
                inner = v[0].get('Value')
                if isinstance(inner, dict):
                    out[n] = '<struct>'
                elif isinstance(inner, list):
                    out[n] = f'<list len={len(inner)}>'
                else:
                    out[n] = inner
            else:
                out[n] = f'<list len={len(v) if isinstance(v,list) else "?"}>'
    return out

template_row = next((r for r in conns_rows if r.get('Name') == 'Sandbox_ElvenEntranceToPromenade'), None)
if template_row:
    tpl = row_fields_summary(template_row)
    print(f'  Template "Sandbox_ElvenEntranceToPromenade" fields: {sorted(tpl.keys())}')
    for r in new_handoff_rows[:1]:
        rf = row_fields_summary(r)
        keys_only_in_tpl = set(tpl) - set(rf)
        keys_only_in_new = set(rf) - set(tpl)
        diffs = {k: (tpl[k], rf[k]) for k in (set(tpl) & set(rf))
                 if str(tpl[k]) != str(rf[k])}
        print(f'  Sample new "{r.get("Name")}":')
        print(f'    keys missing from new: {sorted(keys_only_in_tpl)}')
        print(f'    keys only in new:     {sorted(keys_only_in_new)}')
        print(f'    value diffs:          {len(diffs)}')
        for k, (a, b) in list(diffs.items())[:8]:
            print(f'      {k}: tpl={a!r}  new={b!r}')
else:
    print('  Template row not found')

# ----------------------------------------------------------------------------
# H5: Elevator_G ext flag — neighbour chapter Z bands and anchored landmarks
# ----------------------------------------------------------------------------

print('\n' + '='*72)
print('H5 — Elevator_G SeventhStair ext-flag flip neighbour evidence')
print('='*72)

# Find SeventhStair landmark
seventh = [n for n in all_landmarks if n.endswith('.SeventhStair')]
print(f'  SeventhStair landmark candidates: {seventh}')
for n in seventh:
    r = all_landmarks[n]
    bp_z = landmark_bp_z(n)
    hosts = landmark_hosts.get(n, [])
    print(f'    {n}  BP.Z={bp_z}  Live-SS hosts={hosts}')
    # ext flag
    ext = fp(r.get('Value', []), 'bExtendedConnectivityLandmark')
    print(f'      bExtendedConnectivityLandmark={ext.get("Value") if ext else None}')

# Find host zone's chapter and check Layer +/- 1 chapters
for n in seventh:
    hosts = landmark_hosts.get(n, [])
    for hz in hosts:
        zr = ss_zones[hz]
        chap = zone_chapter(zr)
        cb = chap_band.get(chap)
        print(f'    Host {hz} chapter={chap} Z-band={cb}')

# ----------------------------------------------------------------------------
# H6: connection endpoint zone Z-band vs landmark BP.Z
# ----------------------------------------------------------------------------

print('\n' + '='*72)
print('H6 — Endpoint zone Z-band contains landmark BP.Z?')
print('='*72)

h6_bad = []
for r in new_lc_check:
    name = r.get('Name')
    for side, lm_key, zn_key in (('O', 'OriginLandmark', 'OriginZone'),
                                 ('D', 'DestinationLandmark', 'DestinationZone')):
        lm = lc_endpoint(r, lm_key)
        zn = get(r, zn_key)
        if not lm: continue
        bz = landmark_bp_z(lm)
        # Use endpoint zone's host chapter if zn is None
        host_zone = zn if zn and zn in ss_zones else (landmark_hosts.get(lm, [None])[0])
        if not host_zone: continue
        zr = ss_zones.get(host_zone)
        if not zr: continue
        chap = zone_chapter(zr)
        cb = chap_band.get(chap)
        if cb and bz is not None:
            mn, mx = cb
            in_band = mn <= bz <= mx
            if not in_band:
                h6_bad.append((name, side, lm, bz, host_zone, chap, mn, mx))
            print(f'  {name} [{side}] lm={lm} BP.Z={bz} hostZone={host_zone} chap={chap} band={cb} -> {"OK" if in_band else "OUT OF BAND"}')

print(f'  {len(h6_bad)} out-of-band endpoints')

# ----------------------------------------------------------------------------
# H7: bDisabled / EnabledState consistency on new rows
# ----------------------------------------------------------------------------

print('\n' + '='*72)
print('H7 — EnabledState on new rows')
print('='*72)

for r in new_lc_check:
    print(f'  {r.get("Name")}: EnabledState={zstate(r)}')

# ----------------------------------------------------------------------------
# Bonus: verify new handoff LCs reference landmarks/zones in sane chapters and
# that cross-chapter routing connects valid Live SS zones each side.
# ----------------------------------------------------------------------------

print('\n' + '='*72)
print('Suspect ranking')
print('='*72)
print(f'  H1 GC->unhosted-landmark   evidence count: {len(h1_bad)}')
print(f'  H2 LC endpoint unhosted    evidence count: {len(h2_bad)}')
print(f'  H3 missing-reverse-LC      evidence count: {len(missing_reverse)}')
print(f'  H6 OOB endpoint Z-band     evidence count: {len(h6_bad)}')

print('\nDone.')
