"""Apply landmark BasePosition sync.

Rule A: zones with bPositionFromLandmarks=true => set landmark BP = zone Position.
Rule B: zones with bPositionFromLandmarks=false => if landmark BP outside footprint,
        set BP = (Pos.X+TS.X//2, Pos.Y+TS.Y//2, Pos.Z).
"""
import json
from pathlib import Path

WGR = Path(__file__).resolve().parent
LMS = WGR / 'DT_Moria_Landmarks.json'
ZONES = WGR / 'DT_Moria_Zones.json'

def fp(v, n):
    for p in v or []:
        if isinstance(p, dict) and p.get('Name') == n:
            return p
    return None

def pv(v, n):
    p = fp(v, n)
    return p.get('Value') if p else None

def gv(p):
    v = p.get('Value') if p else None
    if isinstance(v, list) and v:
        d = v[0].get('Value') if isinstance(v[0], dict) else None
        if isinstance(d, dict):
            return (d.get('X'), d.get('Y'), d.get('Z'))
    return None

def gv_named(props, name):
    return gv(fp(props, name))

def set_intvec(p, x, y, z):
    if p is None:
        return False
    v = p.get('Value')
    if isinstance(v, list) and v:
        d = v[0].get('Value')
        if isinstance(d, dict):
            d['X'] = x; d['Y'] = y; d['Z'] = z
            return True
    return False

def find_rows(uasset):
    for exp in uasset.get('Exports', []):
        t = exp.get('Table')
        if t and 'Data' in t:
            return t['Data']
    return []

def landmark_handles(rd):
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
    with open(ZONES, 'r', encoding='utf-8') as f:
        zones = json.load(f)
    with open(LMS, 'r', encoding='utf-8') as f:
        lms = json.load(f)

    zdata = find_rows(zones)
    ldata = find_rows(lms)

    # Build landmark dict by name
    lm_by_name = {r.get('Name',''): r for r in ldata}

    def resolve(lm_name):
        if lm_name in lm_by_name:
            return lm_by_name[lm_name]
        for k, v in lm_by_name.items():
            if k.endswith('.' + lm_name):
                return v
        return None

    a_changes = []
    b_changes = []

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
            lm_row = resolve(lm_name)
            if lm_row is None:
                continue
            lm_props = lm_row.get('Value', []) or []
            lm_state = pv(lm_props, 'EnabledState')
            if lm_state != 'ERowEnabledState::Live':
                continue
            bp_prop = fp(lm_props, 'BasePosition')
            cur_bp = gv(bp_prop)
            if bpfl:
                if pos and cur_bp != pos:
                    if set_intvec(bp_prop, pos[0], pos[1], pos[2]):
                        a_changes.append((zname, lm_row.get('Name'), cur_bp, pos))
            else:
                if not (pos and ts and cur_bp):
                    continue
                in_range = (pos[0] <= cur_bp[0] <= pos[0]+ts[0]-1 and
                            pos[1] <= cur_bp[1] <= pos[1]+ts[1]-1 and
                            pos[2] <= cur_bp[2] <= pos[2]+ts[2]-1)
                if not in_range:
                    new_bp = (pos[0]+ts[0]//2, pos[1]+ts[1]//2, pos[2])
                    footprint = (f'X[{pos[0]}..{pos[0]+ts[0]-1}] '
                                 f'Y[{pos[1]}..{pos[1]+ts[1]-1}] '
                                 f'Z[{pos[2]}..{pos[2]+ts[2]-1}]')
                    if set_intvec(bp_prop, *new_bp):
                        b_changes.append((zname, lm_row.get('Name'), cur_bp, new_bp, footprint))

    with open(LMS, 'w', encoding='utf-8') as f:
        json.dump(lms, f, indent=2)

    print(f'=== APPLIED Rule A: {len(a_changes)} landmark BP rewrites ===')
    for z, ln, old, new in a_changes:
        print(f'  {z:38s} {ln:32s} {old} -> {new}')
    print()
    print(f'=== APPLIED Rule B: {len(b_changes)} out-of-range fixes ===')
    for z, ln, old, new, fp_ in b_changes:
        print(f'  {z:38s} {ln:32s} {old} -> {new}  fp={fp_}')

if __name__ == '__main__':
    main()
