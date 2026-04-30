"""Disable 4 orphan vanilla stair landmarks.

These were vanilla landmarks for Elevator_C/D/E/F which we disabled.
Now hostless, just turning them off too.
"""
import json
from pathlib import Path

WGR = Path(__file__).resolve().parent
LM_PATH = WGR / 'DT_Moria_Landmarks.json'

TARGETS = {
    'Sandbox.SecondStair',
    'Sandbox.ThirdStair',
    'Sandbox.FourthStair',
    'Sandbox.FifthStair',
}

def fp(v, n):
    for p in v or []:
        if isinstance(p, dict) and p.get('Name') == n:
            return p
    return None

lm = json.load(open(LM_PATH, encoding='utf-8'))
rows = lm['Exports'][0]['Table']['Data']

disabled = []
for r in rows:
    if r.get('Name') in TARGETS:
        p = fp(r.get('Value', []), 'EnabledState')
        if p is None:
            print(f'[WARN] {r["Name"]}: no EnabledState property')
            continue
        old = p.get('Value')
        p['Value'] = 'ERowEnabledState::Disabled'
        disabled.append((r['Name'], old, p['Value']))

print(f'Disabled {len(disabled)} landmark rows:')
for name, old, new in disabled:
    print(f'  {name}: {old} -> {new}')

# Ensure Disabled name is present
need_name = 'ERowEnabledState::Disabled'
if need_name not in lm['NameMap']:
    lm['NameMap'].append(need_name)
    print(f'[NameMap] Added: {need_name}')

# Sync counters
nm_len = len(lm['NameMap'])
old_ref = lm.get('NamesReferencedFromExportDataCount')
gens = lm.get('Generations') or []
old_gen = gens[0].get('NameCount') if gens and isinstance(gens[0], dict) else None

lm['NamesReferencedFromExportDataCount'] = nm_len
if gens and isinstance(gens[0], dict):
    gens[0]['NameCount'] = nm_len

print(f'NameMap len: {nm_len}')
print(f'NamesReferencedFromExportDataCount: {old_ref} -> {lm["NamesReferencedFromExportDataCount"]}')
print(f'Generations[0].NameCount: {old_gen} -> {gens[0]["NameCount"] if gens else "N/A"}')

with open(LM_PATH, 'w', encoding='utf-8') as f:
    json.dump(lm, f, indent=2, ensure_ascii=False)
print(f'[write] {LM_PATH}')
