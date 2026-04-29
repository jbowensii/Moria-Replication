"""
Create two new sandbox landmarks that anchor existing deck bubbles:

  Sandbox.DwarfMainHall   ->  BB_DwarfHall1
  Sandbox.ElfMainHall     ->  BB_Sandbox_ElfHall

Both start with zero GuaranteedConnections (safe defaults for sandbox).
Updates DT_Moria_Landmarks.json + its NameMap.
"""
import copy
import json
from pathlib import Path

HERE = Path(__file__).parent
LM_PATH = HERE / 'DT_Moria_Landmarks.json'

LANDMARKS_TO_CREATE = [
    # (new landmark name, target bubble, display label)
    ('Sandbox.DwarfMainHall', 'BB_DwarfHall1',       'Sandbox.DwarfMainHall'),
    ('Sandbox.ElfMainHall',   'BB_Sandbox_ElfHall',  'Sandbox.ElfMainHall'),
]


def clone_as_landmark(template_row, new_name, base_bubble):
    """Clone an existing landmark row and rewrite the fields we want to change.
    Returns the new row dict."""
    new_row = copy.deepcopy(template_row)
    new_row['Name'] = new_name
    for p in new_row.get('Value', []):
        if not isinstance(p, dict):
            continue
        n = p.get('Name')
        if n == 'BaseBubbleName':
            p['Value'] = base_bubble
        elif n == 'GuaranteedConnections':
            # Clear the list; keep DummyStruct so empty array still serializes
            existing = p.get('Value', []) or []
            if existing and 'DummyStruct' not in p:
                p['DummyStruct'] = copy.deepcopy(existing[0])
            p['Value'] = []
        elif n == 'DisplayName':
            # Null out — game falls back to row name if the string key is missing
            p['Value'] = f'Landmarks.{new_name}'
        elif n == 'BasePosition':
            # Keep the template's position (arbitrary anchor — safe default).
            pass
    return new_row


def main():
    data = json.loads(LM_PATH.read_text(encoding='utf-8'))
    rows = data['Exports'][0]['Table']['Data']
    by_name = {r['Name']: r for r in rows}

    # Pick a simple existing landmark as template — one with minimal fields
    # and zero GuaranteedConnections so cloning keeps a clean slate.
    template = by_name.get('Sandbox.ElvenForge') or by_name.get('Sandbox.Aftermath')
    if template is None:
        raise SystemExit('No suitable template landmark found.')
    print(f'Using template row: {template["Name"]}')

    namemap = data.get('NameMap', [])
    namemap_set = set(namemap)
    added_namemap = []

    def nm_add(s):
        if s and s not in namemap_set:
            namemap.append(s)
            namemap_set.add(s)
            added_namemap.append(s)

    for new_name, bubble, display in LANDMARKS_TO_CREATE:
        if new_name in by_name:
            print(f'  {new_name} exists — leaving alone')
            continue
        new_row = clone_as_landmark(template, new_name, bubble)
        rows.append(new_row)
        by_name[new_name] = new_row
        print(f'  created {new_name} -> {bubble}')

        # NameMap additions: row name, bubble name, and the tag form
        # (World.Landmark.X is only needed if anything points at this
        # landmark, but add it pre-emptively so zones can link later.)
        nm_add(new_name)
        nm_add(bubble)
        nm_add(f'World.Landmark.{new_name}')
        nm_add(f'Landmarks.{new_name}')

    data['NameMap'] = namemap
    LM_PATH.write_text(json.dumps(data, indent=2), encoding='utf-8')

    # --- Verify ---
    print('\nNameMap additions:')
    for s in added_namemap:
        print(f'  + {s}')

    print('\n=== Verification ===')
    for new_name, bubble, _ in LANDMARKS_TO_CREATE:
        r = by_name[new_name]
        bb = ''
        pl = ''
        conn_count = 0
        for p in r['Value']:
            if p.get('Name') == 'BaseBubbleName':
                bb = str(p.get('Value', ''))
            elif p.get('Name') == 'Placement':
                v = str(p.get('Value', ''))
                pl = v.split('::')[-1] if '::' in v else v
            elif p.get('Name') == 'GuaranteedConnections':
                conn_count = len(p.get('Value', []) or [])
        print(f'  {new_name:30s}  bubble={bb:30s}  place={pl}  conns={conn_count}')


if __name__ == '__main__':
    main()
