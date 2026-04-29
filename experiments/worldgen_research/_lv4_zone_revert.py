"""Revert 4 ch-4 zones to vanilla auto-place pattern."""
import json
from pathlib import Path

ROOT = Path(__file__).parent
WORK = ROOT / "DT_Moria_Zones.json"
ORIG = ROOT / "DT_Moria_Zones.original.json"

TARGETS = [
    "Sandbox_Small_AngryCaverns_C",
    "Sandbox_Small_City_D",
    "Sandbox_Small_DarkestDeeps_E",
    "Sandbox_Small_DestroyedCity_B",
]


def load(p):
    with open(p, "r", encoding="utf-8") as f:
        return json.load(f)


def save(p, data):
    with open(p, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2)


def find_rows(doc):
    out = {}
    for exp in doc.get("Exports", []):
        tbl = exp.get("Table")
        if not tbl:
            continue
        for row in tbl.get("Data", []):
            n = row.get("Name")
            if n:
                out[n] = row
    return out


def get_intvec(struct, name):
    """Returns dict {X,Y,Z} for an IntVector property by name, or None."""
    f = get_field(struct, name)
    if not f:
        return None
    inner = f.get("Value")
    if isinstance(inner, list) and inner:
        v = inner[0].get("Value")
        if isinstance(v, dict):
            return {"X": v.get("X"), "Y": v.get("Y"), "Z": v.get("Z")}
    return None


def get_chapter(struct):
    f = get_field(struct, "Chapter")
    if not f:
        return None
    inner = f.get("Value")
    if isinstance(inner, list):
        for sub in inner:
            if sub.get("Name") == "RowName":
                return sub.get("Value")
    return None


def get_landmark_handles(struct):
    f = get_field(struct, "LandmarkHandles")
    if not f:
        return []
    out = []
    for entry in f.get("Value", []):
        # entry is a struct; find RowName inside
        inner = entry.get("Value")
        if isinstance(inner, list):
            for sub in inner:
                if sub.get("Name") == "RowName":
                    out.append(sub.get("Value"))
                    break
    return out


def get_field(struct, name):
    for v in struct.get("Value", []):
        if v.get("Name") == name:
            return v
    return None


def summarize(row):
    bpFromLM = get_field(row, "bPositionFromLandmarks")
    bpFromZT = get_field(row, "bPositionFromZoneTable")
    return {
        "Position": get_intvec(row, "Position"),
        "bPositionFromLandmarks": bpFromLM.get("Value") if bpFromLM else None,
        "bPositionFromZoneTable": bpFromZT.get("Value") if bpFromZT else None,
        "TargetSize": get_intvec(row, "TargetSize"),
        "Chapter": get_chapter(row),
        "LandmarkHandles": get_landmark_handles(row),
    }


def set_position_zero(row):
    f = get_field(row, "Position")
    if not f:
        return False
    inner = f.get("Value")
    if isinstance(inner, list) and inner:
        v = inner[0].get("Value")
        if isinstance(v, dict):
            v["X"] = 0
            v["Y"] = 0
            v["Z"] = 0
            return True
    return False


def set_bool(row, name, value):
    f = get_field(row, name)
    if not f:
        return False
    f["Value"] = value
    return True


def main():
    orig_doc = load(ORIG)
    work_doc = load(WORK)
    orig_rows = find_rows(orig_doc)
    work_rows = find_rows(work_doc)

    print("=== VANILLA BASELINE (.original.json) ===")
    baselines = {}
    for name in TARGETS:
        if name not in orig_rows:
            print(f"  MISSING in original: {name}")
            continue
        b = summarize(orig_rows[name])
        baselines[name] = b
        print(f"  {name}: {b}")

    print("\n=== WORKING BEFORE ===")
    befores = {}
    for name in TARGETS:
        if name not in work_rows:
            print(f"  MISSING in working: {name}")
            continue
        b = summarize(work_rows[name])
        befores[name] = b
        print(f"  {name}: {b}")

    print("\n=== APPLYING CHANGES ===")
    changes = []
    for name in TARGETS:
        row = work_rows.get(name)
        if not row:
            continue
        before = befores[name]
        # Set Position to (0,0,0)
        set_position_zero(row)
        # Set bPositionFromLandmarks = true
        set_bool(row, "bPositionFromLandmarks", True)
        after = summarize(row)
        for k in ("Position", "bPositionFromLandmarks", "bPositionFromZoneTable",
                  "TargetSize", "Chapter"):
            if before.get(k) != after.get(k):
                changes.append((name, k, before.get(k), after.get(k)))

    save(WORK, work_doc)

    print("\n=== CHANGES ===")
    for c in changes:
        print(f"  {c[0]} | {c[1]} | {c[2]} -> {c[3]}")

    print("\n=== AFTER (working) ===")
    work_doc2 = load(WORK)
    work_rows2 = find_rows(work_doc2)
    for name in TARGETS:
        a = summarize(work_rows2[name])
        print(f"  {name}: {a}")


if __name__ == "__main__":
    main()
