"""Disable orphan landmark rows.

Orphan = Live landmark row with:
  - No host zone via any Live SS zone's LandmarkHandles, AND
  - No reference from any Live LayoutConnection's OriginLandmark/DestinationLandmark, AND
  - No reference from any landmark's GuaranteedConnections TagName (e.g. "World.Landmark.<RowName>").

Action: set EnabledState to ERowEnabledState::Disabled.
Then sync NameMap counters (NameMap len == NamesReferencedFromExportDataCount == Generations[0].NameCount).
"""
import json, shutil, os
from pathlib import Path

WGR = Path(__file__).resolve().parent
LM_PATH = WGR / 'DT_Moria_Landmarks.json'
Z_PATH = WGR / 'DT_Moria_Zones.json'
LC_PATH = WGR / 'DT_Moria_LayoutConnections.json'

NULL_FNAMES = {'None', 'Null', '', None}

def fp(v, n):
    for p in v or []:
        if isinstance(p, dict) and p.get('Name') == n:
            return p
    return None

def zstate(r):
    p = fp(r.get('Value', []), 'EnabledState')
    return str(p.get('Value', '')).split('::')[-1] if p else None

def get_rowname(prop):
    """Extract RowName from a struct prop value list."""
    if not prop:
        return None
    v = prop.get('Value')
    if isinstance(v, list):
        for s in v:
            if isinstance(s, dict) and s.get('Name') == 'RowName':
                return s.get('Value')
    return None


# --- Backup ---
backup_dir = WGR / 'backups' / 'before_orphan_disable'
backup_dir.mkdir(parents=True, exist_ok=True)
shutil.copy2(LM_PATH, backup_dir / 'DT_Moria_Landmarks.json')
print(f'[backup] {LM_PATH} -> {backup_dir / "DT_Moria_Landmarks.json"}')

# --- Load ---
lm = json.load(open(LM_PATH, encoding='utf-8'))
zd = json.load(open(Z_PATH, encoding='utf-8'))
lc = json.load(open(LC_PATH, encoding='utf-8'))

lm_rows = lm['Exports'][0]['Table']['Data']
z_rows = zd['Exports'][0]['Table']['Data']
lc_rows = lc['Exports'][0]['Table']['Data']

# Live Sandbox.* landmarks (mirrors validator scope)
live_sandbox_lm = set()
for r in lm_rows:
    n = r.get('Name', '')
    if not n.startswith('Sandbox.'):
        continue
    if zstate(r) == 'Disabled':
        continue
    live_sandbox_lm.add(n)

print(f'Live Sandbox.* landmarks: {len(live_sandbox_lm)}')

# Referenced by LandmarkHandles in Live SS zones
referenced_by_zone = set()
for r in z_rows:
    if zstate(r) == 'Disabled':
        continue
    zs_p = fp(r.get('Value', []), 'ZoneSet')
    if not zs_p or str(zs_p.get('Value', '')).split('::')[-1] != 'SandboxSmall':
        continue
    lh = fp(r.get('Value', []), 'LandmarkHandles')
    if not lh:
        continue
    for e in (lh.get('Value') or []):
        inner = e.get('Value') if isinstance(e, dict) else None
        if not isinstance(inner, list):
            continue
        lm_p = fp(inner, 'Landmark')
        v = get_rowname(lm_p)
        if v and v not in NULL_FNAMES:
            referenced_by_zone.add(v)

# Referenced by Live LayoutConnections (Origin/Destination Landmark)
referenced_by_lc = set()
for r in lc_rows:
    if zstate(r) == 'Disabled':
        continue
    for fname in ('OriginLandmark', 'DestinationLandmark'):
        p = fp(r.get('Value', []), fname)
        v = get_rowname(p)
        if v and v not in NULL_FNAMES:
            referenced_by_lc.add(v)

# Referenced by GuaranteedConnections TagName (any landmark, including disabled host).
# Tag form: "World.Landmark.<RowName>" - we extract the trailing path after "World.Landmark."
referenced_by_gc = set()
GC_PREFIX = 'World.Landmark.'
for r in lm_rows:
    gc = fp(r.get('Value', []), 'GuaranteedConnections')
    if not gc:
        continue
    for entry in (gc.get('Value') or []):
        inner = entry.get('Value') if isinstance(entry, dict) else None
        if not isinstance(inner, list):
            continue
        tn = fp(inner, 'TagName')
        if not tn:
            continue
        tag = tn.get('Value')
        if isinstance(tag, str) and tag.startswith(GC_PREFIX):
            target = tag[len(GC_PREFIX):]
            if target:
                referenced_by_gc.add(target)

print(f'Referenced by zones (LandmarkHandles): {len(referenced_by_zone)}')
print(f'Referenced by LayoutConnections (Origin/DestinationLandmark): {len(referenced_by_lc)}')
print(f'Referenced by GuaranteedConnections TagName: {len(referenced_by_gc)}')

all_referenced = referenced_by_zone | referenced_by_lc | referenced_by_gc
orphans = sorted(live_sandbox_lm - all_referenced)

print()
print(f'ORPHANS: {len(orphans)}')
for n in orphans:
    print(f'  - {n}')
print()

# --- Disable each orphan ---
disabled_now = []
for r in lm_rows:
    name = r.get('Name', '')
    if name not in orphans:
        continue
    p = fp(r.get('Value', []), 'EnabledState')
    if not p:
        print(f'[WARN] {name}: no EnabledState property, skipping')
        continue
    old = p.get('Value')
    p['Value'] = 'ERowEnabledState::Disabled'
    disabled_now.append((name, old, p['Value']))

print(f'Disabled {len(disabled_now)} landmark rows:')
for name, old, new in disabled_now:
    print(f'  {name}: {old} -> {new}')
print()

# --- Sync NameMap counters ---
nm_len = len(lm.get('NameMap', []))
old_ref = lm.get('NamesReferencedFromExportDataCount')
gens = lm.get('Generations') or []
old_gen = gens[0].get('NameCount') if gens and isinstance(gens[0], dict) else None

# Ensure ERowEnabledState::Disabled is in NameMap (it already is per our audit)
need_name = 'ERowEnabledState::Disabled'
if need_name not in lm['NameMap']:
    lm['NameMap'].append(need_name)
    print(f'[NameMap] Added missing entry: {need_name}')

nm_len = len(lm['NameMap'])
lm['NamesReferencedFromExportDataCount'] = nm_len
if gens and isinstance(gens[0], dict):
    gens[0]['NameCount'] = nm_len

print(f'NameMap len: {nm_len}')
print(f'NamesReferencedFromExportDataCount: {old_ref} -> {lm["NamesReferencedFromExportDataCount"]}')
print(f'Generations[0].NameCount: {old_gen} -> {gens[0]["NameCount"] if gens else "N/A"}')

# --- Write ---
with open(LM_PATH, 'w', encoding='utf-8') as f:
    json.dump(lm, f, indent=2, ensure_ascii=False)
print(f'[write] {LM_PATH}')
