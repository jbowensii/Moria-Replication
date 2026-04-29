"""Deep audit for the L2_RouteInterzoneConnections / GetZone() crash class.

The crash signature is `EXCEPTION_ACCESS_VIOLATION reading address 0x1a1`
in `FMorLayoutConnectionInstance::GetZone()` from `UWorldRoute::AStarSearch`.

This crashes when the runtime tries to A* across chapters and dereferences
a null Connection pointer at field offset 0x1a1 (likely the ZoneRow field).
The connection is set up from one of three sources:
  - DT_Moria_LayoutConnections rows
  - Landmark.GuaranteedConnections tags
  - Zone.LandmarkHandles[].bExtendedConnectivityLandmark=true (stairs)

This audit catches:
1. Landmark GC tags pointing at landmarks not attached to any Live zone
2. Cross-layer GC where source landmark is NOT a stair (no extended-connectivity)
3. Live zones whose Chapter is Disabled
4. Extended-connectivity stairs with no Layer±1 neighbours
5. LayoutConnections referencing zones whose chapter is Disabled
"""
import json
from pathlib import Path

HERE = Path(__file__).parent


def fp(v, n):
    for p in v or []:
        if isinstance(p, dict) and p.get('Name') == n:
            return p
    return None


def get(r, k):
    p = fp(r['Value'], k)
    if not p:
        return None
    v = p.get('Value')
    if isinstance(v, list):
        for it in v:
            if isinstance(it, dict) and it.get('Name') == 'RowName':
                return it.get('Value', '')
    return v


def zstate(r):
    p = fp(r['Value'], 'EnabledState')
    return str(p.get('Value', '')).split('::')[-1] if p else None


def main():
    z = json.loads((HERE / 'DT_Moria_Zones.json').read_text(encoding='utf-8'))
    lm = json.loads((HERE / 'DT_Moria_Landmarks.json').read_text(encoding='utf-8'))
    ch = json.loads((HERE / 'DT_Moria_Chapters.json').read_text(encoding='utf-8'))
    lc = json.loads((HERE / 'DT_Moria_LayoutConnections.json').read_text(encoding='utf-8'))

    zone_rows = {r['Name']: r for r in z['Exports'][0]['Table']['Data']}
    lm_rows = {r['Name']: r for r in lm['Exports'][0]['Table']['Data']}
    ch_rows = {r['Name']: r for r in ch['Exports'][0]['Table']['Data']}

    live_zones = {n: r for n, r in zone_rows.items() if zstate(r) != 'Disabled'}
    live_lms = {n: r for n, r in lm_rows.items() if zstate(r) != 'Disabled'}
    live_chapters = {n: r for n, r in ch_rows.items() if zstate(r) != 'Disabled'}

    chap_layer = {n: get(r, 'Layer') for n, r in ch_rows.items()}
    live_layers = {chap_layer[n] for n in live_chapters if chap_layer[n] is not None}
    print(f'Live chapter layers: {sorted(live_layers)}')

    # Build landmark host index — maps each landmark to list of (zone, chap, layer, is_stair)
    lm_hosts = {}
    for zname, zr in live_zones.items():
        chap = get(zr, 'Chapter')
        layer = chap_layer.get(chap)
        lh = fp(zr['Value'], 'LandmarkHandles')
        if not lh:
            continue
        for e in (lh.get('Value') or []):
            inner = e.get('Value') if isinstance(e, dict) else None
            if not isinstance(inner, list):
                continue
            rn = ''
            ext = False
            for sub in inner:
                if isinstance(sub, dict):
                    if sub.get('Name') == 'Landmark':
                        for it in (sub.get('Value') or []):
                            if isinstance(it, dict) and it.get('Name') == 'RowName':
                                rn = it.get('Value', '')
                    elif sub.get('Name') == 'bExtendedConnectivityLandmark':
                        ext = sub.get('Value') is True
            if rn:
                lm_hosts.setdefault(rn, []).append((zname, chap, layer, ext))

    # === 1. Landmark GC audit ===
    print('\n=== 1. Landmark GuaranteedConnections audit ===')
    gc_issues = []
    for lname, lr in live_lms.items():
        gc = fp(lr['Value'], 'GuaranteedConnections')
        if not gc:
            continue
        for it in (gc.get('Value') or []):
            inner = it.get('Value') if isinstance(it, dict) else None
            if not isinstance(inner, list):
                continue
            for sub in inner:
                if isinstance(sub, dict) and sub.get('Name') == 'TagName':
                    tag = sub.get('Value', '')
                    if not tag:
                        continue
                    if not tag.startswith('World.Landmark.'):
                        continue
                    target = tag[len('World.Landmark.'):]
                    if target not in lm_rows:
                        gc_issues.append((lname, target, 'TARGET LANDMARK MISSING'))
                    elif target not in live_lms:
                        gc_issues.append((lname, target, 'TARGET LANDMARK DISABLED'))
                    elif target not in lm_hosts:
                        gc_issues.append((lname, target, 'TARGET NOT ATTACHED to any Live zone'))
                    elif lname not in lm_hosts:
                        gc_issues.append((lname, target, 'SOURCE NOT ATTACHED to any Live zone'))
                    else:
                        src_hosts = lm_hosts[lname]
                        tgt_hosts = lm_hosts[target]
                        src_layers = {h[2] for h in src_hosts if h[2] is not None}
                        tgt_layers = {h[2] for h in tgt_hosts if h[2] is not None}
                        # Cross-chapter check
                        if src_layers and tgt_layers and not (src_layers & tgt_layers):
                            src_is_stair = any(h[3] for h in src_hosts)
                            tgt_is_stair = any(h[3] for h in tgt_hosts)
                            if not (src_is_stair or tgt_is_stair):
                                gc_issues.append((lname, target,
                                    f'CROSS-LAYER non-stair GC: src={sorted(src_layers)} tgt={sorted(tgt_layers)}'))
    print(f'GC issues: {len(gc_issues)}')
    for it in gc_issues[:30]:
        print(f'  {it[0]:<40s} -> {it[1]:<40s}  {it[2]}')

    # === 2. Live zone -> Disabled chapter ===
    print('\n=== 2. Live zone -> Disabled chapter ===')
    disabled_chap = set(ch_rows) - set(live_chapters)
    risky = [(n, get(r, 'Chapter')) for n, r in live_zones.items()
             if get(r, 'Chapter') in disabled_chap]
    print(f'  {len(risky)} risky')
    for r in risky[:10]:
        print(f'    {r}')

    # === 3. Stairs (extended-connectivity) without Layer+/-1 neighbour ===
    print('\n=== 3. Extended-connectivity stairs without neighbour layer ===')
    stair_issues = []
    for zname, zr in live_zones.items():
        chap = get(zr, 'Chapter')
        if chap not in live_chapters:
            continue
        L = chap_layer.get(chap)
        if L is None:
            continue
        lh = fp(zr['Value'], 'LandmarkHandles')
        if not lh:
            continue
        for e in (lh.get('Value') or []):
            inner = e.get('Value') if isinstance(e, dict) else None
            if not isinstance(inner, list):
                continue
            rn = ''
            ext = False
            for sub in inner:
                if isinstance(sub, dict):
                    if sub.get('Name') == 'Landmark':
                        for it in (sub.get('Value') or []):
                            if isinstance(it, dict) and it.get('Name') == 'RowName':
                                rn = it.get('Value', '')
                    elif sub.get('Name') == 'bExtendedConnectivityLandmark':
                        ext = sub.get('Value') is True
            if ext and rn:
                up = (L + 1) in live_layers
                down = (L - 1) in live_layers
                if not (up or down):
                    stair_issues.append((zname, rn, L, 'NO ADJACENT LAYER'))
    print(f'  {len(stair_issues)} stair issues')
    for s in stair_issues[:20]:
        print(f'    {s}')

    # === 4. LayoutConnections referencing zones whose chapter is Disabled ===
    print('\n=== 4. Live LayoutConnections -> zones in Disabled chapter ===')
    lc_issues = []
    for r in lc['Exports'][0]['Table']['Data']:
        n = r['Name']
        st = zstate(r)
        if st in ('Disabled', 'Test'):
            continue
        if n.startswith('Test_'):
            continue
        for fld in ('OriginZone', 'DestinationZone'):
            zr_name = get(r, fld)
            if zr_name and zr_name not in ('None', 'Null'):
                zr = zone_rows.get(zr_name)
                if zr:
                    chap = get(zr, 'Chapter')
                    if chap in disabled_chap:
                        lc_issues.append((n, fld, zr_name, chap, 'CHAPTER DISABLED'))
    print(f'  {len(lc_issues)} issues')
    for x in lc_issues[:20]:
        print(f'    {x}')

    print('\n=== SUMMARY ===')
    total = len(gc_issues) + len(risky) + len(stair_issues) + len(lc_issues)
    print(f'Total potential crash sources: {total}')
    if total == 0:
        print('No structural reason for the GetZone crash detected at this layer.')
        print('Likely next: build pipeline byte corruption, or a vanilla pattern')
        print('we have not yet recognized.')


if __name__ == '__main__':
    main()
