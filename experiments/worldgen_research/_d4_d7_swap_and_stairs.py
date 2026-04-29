"""Multi-step transaction:

1. Swap heights of D-4 (chap-11) and D-7 (chap-8): h=3 <-> h=1.
   D-7 takes the bottom 3 cells (Z=0..2). D-6/D-5 shift up 2. D-4 becomes
   1 cell at Z=7. D-3 and above unchanged.

2. Move Crystal Descents:
     Elevator_E:  chap-11 (D-4) -> chap-10 (D-5)
     Elevator_F:  chap-11 (D-4) -> chap-9  (D-6)
   Now Crystal Descents form chain D-5 <-> D-6 <-> D-7 via extended
   connectivity.

3. Duplicate DestroyedCity_D -> DestroyedCity_E. Both move to chap-11
   (D-4). D keeps UpperArmoury (loses NogrodForge); E keeps NogrodForge
   (loses UpperArmoury). Position set to (0,0,0) so generator places
   within the new 1-cell band.

4. Add 3 new stair zones:
     Elevator_G  at chap-5 (Lv-5) with new landmark Sandbox.SeventhStair
     Elevator_H  at chap-7 (Lv-7) with new landmark Sandbox.NinthStair
     Elevator_I  at chap-10 (D-5) with new landmark Sandbox.SixthStair
   Each has bExtendedConnectivityLandmark=true so they auto-route Layer +/-1.

5. Add 3 new landmark rows for the new stairs.
"""
import json, copy, shutil
from pathlib import Path

HERE = Path(__file__).parent

# ----- helpers -----
def fp(v, n):
    for p in v or []:
        if isinstance(p, dict) and p.get('Name') == n: return p
    return None
def get_rowname(prop):
    if not prop: return None
    v = prop.get('Value')
    if isinstance(v, list):
        for it in v:
            if isinstance(it, dict) and it.get('Name') == 'RowName':
                return it.get('Value', '')
    return None
def set_rowname(prop, new):
    v = prop.get('Value')
    if isinstance(v, list):
        for it in v:
            if isinstance(it, dict) and it.get('Name') == 'RowName':
                it['Value'] = new; return True
    return False
def get_intvec(prop):
    if not prop: return (None,None,None)
    v = prop.get('Value')
    if isinstance(v, list) and v:
        inner = v[0]
        if isinstance(inner, dict) and isinstance(inner.get('Value'), dict):
            d = inner['Value']
            return (d.get('X'), d.get('Y'), d.get('Z'))
    return (None,None,None)
def set_intvec(prop, x, y, z):
    v = prop.get('Value')
    if isinstance(v, list) and v:
        inner = v[0]
        if isinstance(inner, dict) and isinstance(inner.get('Value'), dict):
            inner['Value']['X'] = x
            inner['Value']['Y'] = y
            inner['Value']['Z'] = z
            return True
    return False
def add_intvec_z(prop, delta):
    v = prop.get('Value')
    if isinstance(v, list) and v:
        inner = v[0]
        if isinstance(inner, dict) and isinstance(inner.get('Value'), dict):
            d = inner['Value']
            d['Z'] = (d.get('Z', 0) or 0) + delta
            return True
    return False
def set_scalar(r, key, val):
    p = fp(r['Value'], key)
    if p is not None: p['Value'] = val
def zoneset(r):
    p = fp(r.get('Value', []), 'ZoneSet')
    if not p: return None
    return str(p.get('Value','')).split('::')[-1]
def add_to_namemap(d, names):
    nm = d.setdefault('NameMap', [])
    present = set(nm); added = []
    for n in names:
        if isinstance(n, str) and n and n not in present:
            nm.append(n); present.add(n); added.append(n)
    n = len(nm)
    d['NamesReferencedFromExportDataCount'] = n
    gens = d.get('Generations') or []
    if gens and isinstance(gens[0], dict): gens[0]['NameCount'] = n
    return added


def main():
    # === Snapshot ===
    BAK = HERE / 'backups' / 'before D4-D7 swap and stairs'
    BAK.mkdir(parents=True, exist_ok=True)
    for src in sorted(HERE.glob('*.json')):
        if src.name.endswith('.original.json'): continue
        if not src.name.startswith(('DT_','BC_','World')): continue
        shutil.copy2(src, BAK / src.name)
    print('Snapshot saved to backups/before D4-D7 swap and stairs/\n')

    # === Phase 1: Chapter height swap ===
    print('=== Phase 1: D-4 / D-7 height swap ===')
    ch_path = HERE / 'DT_Moria_Chapters.json'
    ch = json.loads(ch_path.read_text(encoding='utf-8'))

    # New chapter Z bands (only 4 chapters change: 8, 9, 10, 11)
    UPDATES = {
        # name: (Layer, MinZ, MaxZ, PrimeZ)
        'SandboxSmall-chapter-8':  (-7, 0, 2, 1),  # D-7  h=1->3 (was 0..0)
        'SandboxSmall-chapter-9':  (-6, 3, 4, 3),  # D-6  unchanged h=2 (was 1..2 -> 3..4 shift+2)
        'SandboxSmall-chapter-10': (-5, 5, 6, 5),  # D-5  unchanged h=2 (was 3..4 -> 5..6 shift+2)
        'SandboxSmall-chapter-11': (-4, 7, 7, 7),  # D-4  h=3->1 (was 5..7 -> 7..7)
    }
    for r in ch['Exports'][0]['Table']['Data']:
        if r['Name'] in UPDATES:
            L, mn, mx, pz = UPDATES[r['Name']]
            old_mn = fp(r['Value'],'MinZ').get('Value')
            old_mx = fp(r['Value'],'MaxZ').get('Value')
            set_scalar(r, 'Layer', L)
            set_scalar(r, 'MinZ', mn)
            set_scalar(r, 'MaxZ', mx)
            set_scalar(r, 'PrimeZ', pz)
            print(f'  {r["Name"]:<32s}  Z={old_mn}..{old_mx} -> {mn}..{mx}  h={mx-mn+1}')
    ch_path.write_text(json.dumps(ch, indent=2), encoding='utf-8')

    # === Phase 2: Move existing zones ===
    print('\n=== Phase 2: Zone moves + DestroyedCity duplicate ===')
    z_path = HERE / 'DT_Moria_Zones.json'
    z = json.loads(z_path.read_text(encoding='utf-8'))
    rows = z['Exports'][0]['Table']['Data']
    by_name = {r['Name']: r for r in rows}

    # 2a. Move Elevator_E from chap-11 to chap-10 (D-4 -> D-5)
    if 'Sandbox_Small_Elevator_E' in by_name:
        cp = fp(by_name['Sandbox_Small_Elevator_E']['Value'], 'Chapter')
        old = get_rowname(cp)
        set_rowname(cp, 'SandboxSmall-chapter-10')
        print(f'  Sandbox_Small_Elevator_E:  Chapter {old} -> SandboxSmall-chapter-10  (D-5, Crystal Descent)')

    # 2b. Move Elevator_F from chap-11 to chap-9 (D-4 -> D-6)
    if 'Sandbox_Small_Elevator_F' in by_name:
        cp = fp(by_name['Sandbox_Small_Elevator_F']['Value'], 'Chapter')
        old = get_rowname(cp)
        set_rowname(cp, 'SandboxSmall-chapter-9')
        print(f'  Sandbox_Small_Elevator_F:  Chapter {old} -> SandboxSmall-chapter-9   (D-6, Crystal Descent)')

    # 2c. Duplicate DestroyedCity_D -> DestroyedCity_E
    if 'Sandbox_Small_DestroyedCity_D' in by_name:
        d_row = by_name['Sandbox_Small_DestroyedCity_D']
        if 'Sandbox_Small_DestroyedCity_E' not in by_name:
            e_row = copy.deepcopy(d_row)
            e_row['Name'] = 'Sandbox_Small_DestroyedCity_E'
            rows.append(e_row); by_name['Sandbox_Small_DestroyedCity_E'] = e_row
            print(f'  DestroyedCity_E created as copy of DestroyedCity_D')
        else:
            e_row = by_name['Sandbox_Small_DestroyedCity_E']
            print(f'  DestroyedCity_E already exists, reusing')

        # Move both to chap-11
        for nm in ('Sandbox_Small_DestroyedCity_D', 'Sandbox_Small_DestroyedCity_E'):
            r = by_name[nm]
            cp = fp(r['Value'], 'Chapter')
            old = get_rowname(cp)
            set_rowname(cp, 'SandboxSmall-chapter-11')
            print(f'  {nm}:  Chapter {old} -> SandboxSmall-chapter-11  (D-4)')
            # Set Position to (0,0,0) so generator places in 1-cell band
            pos = fp(r['Value'], 'Position')
            old_pos = get_intvec(pos)
            set_intvec(pos, 0, 0, 0)
            if old_pos != (0,0,0):
                print(f'    Position {old_pos} -> (0,0,0)  (unpinned for generator)')

        # 2d. D landmark surgery: keep UpperArmoury, remove NogrodForge
        # 2e. E landmark surgery: keep NogrodForge, remove UpperArmoury
        def filter_landmarks(row, keep_set, remove_set):
            lh = fp(row['Value'], 'LandmarkHandles')
            if not lh: return
            new_entries = []
            for e in (lh.get('Value') or []):
                inner = e.get('Value') if isinstance(e, dict) else None
                rn = ''
                if isinstance(inner, list):
                    for sub in inner:
                        if isinstance(sub, dict) and sub.get('Name') == 'Landmark':
                            for it in (sub.get('Value') or []):
                                if isinstance(it, dict) and it.get('Name') == 'RowName':
                                    rn = it.get('Value', '')
                if rn in remove_set:
                    continue  # drop
                new_entries.append(e)
            lh['Value'] = new_entries
            # Preserve DummyStruct on empty arrays
            if not new_entries and 'DummyStruct' not in lh and lh.get('Value') is not None:
                # No template available — but vanilla has one already if it had entries.
                pass

        filter_landmarks(by_name['Sandbox_Small_DestroyedCity_D'],
                         {'Sandbox.UpperArmoury'}, {'Sandbox.NogrodForge'})
        print(f'  DestroyedCity_D landmarks: removed Sandbox.NogrodForge, kept Sandbox.UpperArmoury')
        filter_landmarks(by_name['Sandbox_Small_DestroyedCity_E'],
                         {'Sandbox.NogrodForge'}, {'Sandbox.UpperArmoury'})
        print(f'  DestroyedCity_E landmarks: removed Sandbox.UpperArmoury, kept Sandbox.NogrodForge')

    # === Phase 3: Add 3 new stair zones ===
    print('\n=== Phase 3: New stair zones ===')

    # Use Elevator_E as template (same Crystal Descent structure but we'll
    # tweak biome later if desired; for now it inherits whatever Elevator_E
    # has, and the user can re-biome via the editor)
    # Better: use Elevator_B (the FirstStair, basic stair) as a cleaner template
    template = copy.deepcopy(by_name['Sandbox_Small_Elevator_B'])

    NEW_STAIRS = [
        # (zone_name, chapter, landmark_name)
        ('Sandbox_Small_Elevator_G', 'SandboxSmall-chapter-5',  'Sandbox.SeventhStair'),  # Lv-5
        ('Sandbox_Small_Elevator_H', 'SandboxSmall-chapter-7',  'Sandbox.NinthStair'),    # Lv-7
        ('Sandbox_Small_Elevator_I', 'SandboxSmall-chapter-10', 'Sandbox.SixthStair'),    # D-5
    ]

    for zone_name, chap_name, landmark_name in NEW_STAIRS:
        if zone_name in by_name:
            print(f'  {zone_name} already exists, skipping'); continue
        new_row = copy.deepcopy(template)
        new_row['Name'] = zone_name

        # Set Chapter
        cp = fp(new_row['Value'], 'Chapter')
        set_rowname(cp, chap_name)

        # Set EnabledState Live
        es = fp(new_row['Value'], 'EnabledState')
        if es is not None: es['Value'] = 'ERowEnabledState::Live'

        # Replace LandmarkHandles[0].Landmark with the new landmark
        lh = fp(new_row['Value'], 'LandmarkHandles')
        if lh and lh.get('Value'):
            entry = lh['Value'][0]
            inner = entry.get('Value', [])
            for sub in inner:
                if isinstance(sub, dict) and sub.get('Name') == 'Landmark':
                    for it in (sub.get('Value') or []):
                        if isinstance(it, dict) and it.get('Name') == 'RowName':
                            it['Value'] = landmark_name
                # Ensure bExtendedConnectivityLandmark = True
                if isinstance(sub, dict) and sub.get('Name') == 'bExtendedConnectivityLandmark':
                    sub['Value'] = True

        # Position: leave as (0,0,0) so generator places it in band
        pos = fp(new_row['Value'], 'Position')
        if pos: set_intvec(pos, 0, 0, 0)

        rows.append(new_row); by_name[zone_name] = new_row
        print(f'  {zone_name}  -> chapter={chap_name}  landmark={landmark_name} (ext-conn)')

    # NameMap additions for Zones
    new_zone_namemap = [n for n,_,_ in NEW_STAIRS] + [l for _,_,l in NEW_STAIRS] \
                      + ['SandboxSmall-chapter-10','SandboxSmall-chapter-9','SandboxSmall-chapter-11',
                         'Sandbox_Small_DestroyedCity_E']
    add_to_namemap(z, new_zone_namemap)
    z_path.write_text(json.dumps(z, indent=2), encoding='utf-8')

    # === Phase 4: Add new landmark rows ===
    print('\n=== Phase 4: New landmark rows ===')
    lm_path = HERE / 'DT_Moria_Landmarks.json'
    lm = json.loads(lm_path.read_text(encoding='utf-8'))
    lm_rows = lm['Exports'][0]['Table']['Data']
    lm_by_name = {r['Name']: r for r in lm_rows}

    # Use Sandbox.FirstStair as template
    if 'Sandbox.FirstStair' not in lm_by_name:
        print('  ! Sandbox.FirstStair template not found, skipping landmark creation')
    else:
        template_lm = lm_by_name['Sandbox.FirstStair']
        for _, _, lname in NEW_STAIRS:
            if lname in lm_by_name:
                print(f'  {lname} already exists'); continue
            new_lm = copy.deepcopy(template_lm)
            new_lm['Name'] = lname
            # Clear BasePosition (leave at original or zero — a stair doesn't
            # need a fixed BasePos when its host zone is unpinned)
            bp = fp(new_lm['Value'], 'BasePosition')
            if bp: set_intvec(bp, 0, 0, 0)
            es = fp(new_lm['Value'], 'EnabledState')
            if es is not None: es['Value'] = 'ERowEnabledState::Live'
            lm_rows.append(new_lm); lm_by_name[lname] = new_lm
            print(f'  Added landmark: {lname}  (BasePos=0,0,0 unpinned)')

    add_to_namemap(lm, [l for _,_,l in NEW_STAIRS])
    lm_path.write_text(json.dumps(lm, indent=2), encoding='utf-8')

    print('\n=== DONE ===')


if __name__ == '__main__':
    main()
