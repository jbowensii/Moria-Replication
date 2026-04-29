"""Audit landmark BasePositions vs host Live SS zone Positions.

Rule A: zones with bPositionFromLandmarks=true => landmark BP must EQUAL zone Position.
Rule B: zones with bPositionFromLandmarks=false => landmark BP must be inside zone footprint.
"""
import json
from pathlib import Path

WGR = Path(__file__).resolve().parent

def load(name):
    with open(WGR / name, 'r', encoding='utf-8') as f:
        return json.load(f)

def fp(v, n):
    for p in v or []:
        if isinstance(p, dict) and p.get('Name') == n:
            return p
    return None

def pv(v, n):
    p = fp(v, n)
    return p.get('Value') if p else None

def gv(p):
    """Read IntVector struct as (X,Y,Z)."""
    v = p.get('Value') if p else None
    if isinstance(v, list) and v:
        d = v[0].get('Value') if isinstance(v[0], dict) else None
        if isinstance(d, dict):
            return (d.get('X'), d.get('Y'), d.get('Z'))
    return None

def gv_named(props, name):
    return gv(fp(props, name))

def find_rows(uasset):
    for exp in uasset.get('Exports', []):
        t = exp.get('Table')
        if t and 'Data' in t:
            return t['Data']
    return []

def landmark_handles(rd):
    """Return list of landmark RowNames referenced by the zone."""
    out = []
    p = fp(rd, 'LandmarkHandles')
    if not p:
        return out
    for entry in p.get('Value', []) or []:
        ep = entry.get('Value', []) or []
        lh = fp(ep, 'Landmark')
        if lh:
            inner = lh.get('Value', []) or []
            rn = fp(inner, 'RowName')
            if rn:
                out.append(rn.get('Value'))
    return out

def main():
    zones = load('DT_Moria_Zones.json')
    lms = load('DT_Moria_Landmarks.json')

    zdata = find_rows(zones)
    ldata = find_rows(lms)

    # Build landmark dict: name -> (row, BP, state)
    lm_map = {}
    for r in ldata:
        nm = r.get('Name','')
        rd = r.get('Value', []) or []
        bp = gv_named(rd, 'BasePosition')
        state = pv(rd, 'EnabledState')
        lm_map[nm] = {'row': r, 'bp': bp, 'state': state}

    # Iterate Live SS zones
    rule_a = []  # (zone_name, zone_pos, lm_name, lm_bp, proposed_bp, delta)
    rule_b = []  # (zone_name, zone_pos, ts, lm_name, lm_bp, in_range, proposed_bp_or_None)
    referenced_lms = set()

    for r in zdata:
        zname = r.get('Name','')
        v = r.get('Value', []) or []
        zs = pv(v, 'ZoneSet')
        state = pv(v, 'EnabledState')
        if zs != 'EZoneSet::SandboxSmall' or state != 'ERowEnabledState::Live':
            continue
        pos = gv_named(v, 'Position')
        ts = gv_named(v, 'TargetSize')
        bpfl = pv(v, 'bPositionFromLandmarks')
        lhs = landmark_handles(v)
        for lm_name in lhs:
            if lm_name is None:
                continue
            referenced_lms.add(lm_name)
            # resolve landmark — try direct then 'Sandbox.' prefix variants
            lm = lm_map.get(lm_name)
            resolved_key = lm_name
            if lm is None:
                # try matching by suffix
                for k in lm_map:
                    if k == lm_name or k.endswith('.' + lm_name):
                        lm = lm_map[k]; resolved_key = k; break
            if lm is None:
                rule_b.append((zname, pos, ts, f'{lm_name} (NOT FOUND)', None, False, None))
                continue
            # Only consider Live landmarks
            if lm['state'] != 'ERowEnabledState::Live':
                continue
            bp = lm['bp']
            if bpfl:
                proposed = pos
                delta = None
                if bp and pos:
                    delta = (bp[0]-pos[0], bp[1]-pos[1], bp[2]-pos[2])
                rule_a.append((zname, pos, resolved_key, bp, proposed, delta))
            else:
                # Rule B: check footprint
                if not (pos and ts and bp):
                    rule_b.append((zname, pos, ts, resolved_key, bp, False, None))
                    continue
                in_range = (pos[0] <= bp[0] <= pos[0]+ts[0]-1 and
                            pos[1] <= bp[1] <= pos[1]+ts[1]-1 and
                            pos[2] <= bp[2] <= pos[2]+ts[2]-1)
                proposed = None
                if not in_range:
                    proposed = (pos[0]+ts[0]//2, pos[1]+ts[1]//2, pos[2])
                rule_b.append((zname, pos, ts, resolved_key, bp, in_range, proposed))

    # Orphans
    orphans = []
    for k, info in lm_map.items():
        if info['state'] != 'ERowEnabledState::Live':
            continue
        # was it referenced?
        # account for short-name lookup: a zone may have referenced a short name k.split('.')[-1]
        short = k.split('.')[-1] if '.' in k else k
        if k in referenced_lms or short in referenced_lms:
            continue
        orphans.append((k, info['bp']))

    # === Print A1 ===
    print('=== TABLE A1: Rule A (bPositionFromLandmarks=true) ===')
    print(f'{"Zone":35s} {"ZonePos":20s} {"Landmark":30s} {"CurrentBP":20s} {"ProposedBP":20s} {"Delta"}')
    for z, pos, lm, bp, prop, delta in rule_a:
        print(f'  {z:35s} {str(pos):20s} {lm:30s} {str(bp):20s} {str(prop):20s} {delta}')
    print(f'  count={len(rule_a)}')

    print()
    print('=== TABLE B1: Rule B (bPositionFromLandmarks=false) ===')
    print(f'{"Zone":35s} {"ZonePos":18s} {"TS":12s} {"Landmark":30s} {"CurrentBP":20s} {"InRange":8s} {"ProposedBP"}')
    out_of_range = 0
    for z, pos, ts, lm, bp, ir, prop in rule_b:
        flag = 'YES' if ir else 'NO'
        if not ir:
            out_of_range += 1
        print(f'  {z:35s} {str(pos):18s} {str(ts):12s} {lm:30s} {str(bp):20s} {flag:8s} {prop if prop else ""}')
    print(f'  total={len(rule_b)}  out_of_range={out_of_range}')

    print()
    print('=== ORPHAN LIVE LANDMARKS (informational) ===')
    for k, bp in orphans:
        print(f'  {k:50s} BP={bp}')
    print(f'  count={len(orphans)}')

    return {'rule_a': rule_a, 'rule_b': rule_b, 'orphans': orphans}

if __name__ == '__main__':
    main()
