"""Audit current state of stair zones and landmarks before applying fix4."""
import json, os, sys

BASE = os.path.dirname(os.path.abspath(__file__))
ZF = os.path.join(BASE, "DT_Moria_Zones.json")
CF = os.path.join(BASE, "DT_Moria_Chapters.json")
LF = os.path.join(BASE, "DT_Moria_Landmarks.json")
LCF = os.path.join(BASE, "DT_Moria_LayoutConnections.json")

def load(p):
    with open(p, "r", encoding="utf-8") as f:
        return json.load(f)

def fp(props, name):
    """Find a property by Name in a list of properties."""
    for p in props:
        if p.get("Name") == name:
            return p
    return None

def get_rows(dt):
    """Return list of (RowName, propsList) tuples for a UAssetGUI DataTable."""
    # DataTable export: the rows live in Exports[0].Table.Data, each entry has Name and Value (props list)
    for ex in dt.get("Exports", []):
        tbl = ex.get("Table")
        if tbl and "Data" in tbl:
            rows = []
            for row in tbl["Data"]:
                rows.append((row.get("Name"), row.get("Value", [])))
            return rows
    return []

def main():
    zones = load(ZF)
    chapters = load(CF)
    landmarks = load(LF)
    print("=" * 70)
    print("ZONE AUDIT — Elevators (Sandbox_Small_Elevator_*)")
    print("=" * 70)
    zrows = get_rows(zones)
    elev_zones = {}
    for name, props in zrows:
        if name and "Sandbox_Small_Elevator_" in name:
            elev_zones[name] = props
            tgt_size = fp(props, "TargetSize")
            base_pos = fp(props, "BasePosition")
            lh = fp(props, "LandmarkHandles")
            sz_str = "?"
            bp_str = "?"
            if tgt_size:
                v = tgt_size.get("Value", [])
                xs = {p["Name"]: p.get("Value") for p in v}
                sz_str = f"X={xs.get('X')} Y={xs.get('Y')} Z={xs.get('Z')}"
            if base_pos:
                v = base_pos.get("Value", [])
                bp = {p["Name"]: p.get("Value") for p in v}
                bp_str = f"X={bp.get('X')} Y={bp.get('Y')} Z={bp.get('Z')}"
            print(f"\nZone: {name}")
            print(f"  BasePosition: {bp_str}")
            print(f"  TargetSize:   {sz_str}")
            if lh:
                print(f"  LandmarkHandles ({len(lh.get('Value', []))} entries):")
                for i, entry in enumerate(lh.get("Value", [])):
                    eprops = entry.get("Value", [])
                    lm = fp(eprops, "Landmark")
                    pl = fp(eprops, "Placement")
                    ext = fp(eprops, "bExtendedConnectivityLandmark")
                    lm_v = lm.get("Value") if lm else None
                    pl_v = pl.get("Value") if pl else None
                    ext_v = ext.get("Value") if ext else None
                    print(f"    [{i}] Landmark={lm_v}  Placement={pl_v}  bExt={ext_v}")
    print("\n" + "=" * 70)
    print("LANDMARKS — *Stair*")
    print("=" * 70)
    lrows = get_rows(landmarks)
    stair_lms = {}
    for name, props in lrows:
        if name and "Stair" in name:
            stair_lms[name] = props
            ch = fp(props, "Chapter")
            bp = fp(props, "BasePosition")
            ch_v = ch.get("Value") if ch else None
            bp_str = "?"
            if bp:
                v = bp.get("Value", [])
                bpv = {p["Name"]: p.get("Value") for p in v}
                bp_str = f"X={bpv.get('X')} Y={bpv.get('Y')} Z={bpv.get('Z')}"
            print(f"  {name}: Chapter={ch_v}  BasePosition={bp_str}")
    print("\n" + "=" * 70)
    print("CHAPTERS — Sandbox rows with their Layer/Z info")
    print("=" * 70)
    crows = get_rows(chapters)
    sb_chapters = {}
    for name, props in crows:
        if name and "Sandbox" in name:
            sb_chapters[name] = props
            lay = fp(props, "Layer")
            primez = fp(props, "PrimeZ")
            minz = fp(props, "MinZ")
            maxz = fp(props, "MaxZ")
            lay_v = lay.get("Value") if lay else None
            pz_v = primez.get("Value") if primez else None
            mn_v = minz.get("Value") if minz else None
            mx_v = maxz.get("Value") if maxz else None
            # Only print Lv-4..Lv-7 candidates
            if lay_v in (3, 4, 5, 6) or (pz_v is not None and pz_v in (22, 23, 26, 27, 28)):
                print(f"  {name}: Layer={lay_v}  PrimeZ={pz_v}  MinZ={mn_v}  MaxZ={mx_v}")
    return zones, chapters, landmarks, elev_zones, stair_lms, sb_chapters

if __name__ == "__main__":
    main()
