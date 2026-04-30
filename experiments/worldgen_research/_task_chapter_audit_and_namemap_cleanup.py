"""Task 1: List all Chapter[1-6].* landmarks and classify HOSTED vs ORPHAN.
Task 2: Clean up orphan NameMap strings in 4 DataTable files.
"""
from __future__ import annotations
import json, re, copy
from pathlib import Path

ROOT = Path(r"C:\Users\johnb\OneDrive\Documents\Projects\Moria-Replication\experiments\worldgen_research")

CHAPTER_RE = re.compile(r"^Chapter[1-6]\.")

def load(name):
    with open(ROOT / name, "r", encoding="utf-8") as f:
        return json.load(f)

def save(name, data):
    with open(ROOT / name, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2)

def get_field(row, name):
    for v in row.get("Value", []):
        if v.get("Name") == name:
            return v
    return None

def get_struct_rowname(field):
    """Extract RowName string from a struct property like OriginLandmark."""
    if not field: return None
    inner = field.get("Value")
    if not isinstance(inner, list): return None
    for item in inner:
        if isinstance(item, dict) and item.get("Name") == "RowName":
            return item.get("Value")
        # Sometimes nested deeper
        if isinstance(item, dict) and "Value" in item:
            iv = item.get("Value")
            if isinstance(iv, list):
                for sub in iv:
                    if isinstance(sub, dict) and sub.get("Name") == "RowName":
                        return sub.get("Value")
    return None

def get_enum_value(field):
    if not field: return None
    return field.get("Value")

# =====================================================
# TASK 1: Chapter[1-6].* landmark hosting analysis
# =====================================================
def task1():
    print("="*70)
    print("TASK 1: Chapter[1-6].* landmark hosting audit")
    print("="*70)
    landmarks = load("DT_Moria_Landmarks.json")
    zones = load("DT_Moria_Zones.json")
    lcs = load("DT_Moria_LayoutConnections.json")

    lm_rows = landmarks["Exports"][0]["Table"]["Data"]
    z_rows = zones["Exports"][0]["Table"]["Data"]
    lc_rows = lcs["Exports"][0]["Table"]["Data"]

    # Collect SS Live zones and their landmark refs
    ss_live_zone_landmarks = {}  # landmark_rowname -> [zone_names]
    for zr in z_rows:
        zname = zr.get("Name")
        zs_field = get_field(zr, "ZoneSet")
        en_field = get_field(zr, "EnabledState")
        if get_enum_value(zs_field) != "EZoneSet::SandboxSmall":
            continue
        if get_enum_value(en_field) != "ERowEnabledState::Live":
            continue
        lh = get_field(zr, "LandmarkHandles")
        if not lh: continue
        for entry in lh.get("Value", []) or []:
            if not isinstance(entry, dict): continue
            # entry is MorZoneLandmarkEntry struct - find Landmark sub-struct
            inner = entry.get("Value", [])
            if not isinstance(inner, list): continue
            for sub in inner:
                if isinstance(sub, dict) and sub.get("Name") == "Landmark":
                    rn = get_struct_rowname(sub)
                    if rn:
                        ss_live_zone_landmarks.setdefault(rn, []).append(zname)

    # Collect Live LC origin/dest landmark refs
    live_lc_landmarks = {}  # landmark_rowname -> [lc_names]
    for lcr in lc_rows:
        lcname = lcr.get("Name")
        en_field = get_field(lcr, "EnabledState")
        if get_enum_value(en_field) != "ERowEnabledState::Live":
            continue
        for fname in ("OriginLandmark", "DestinationLandmark"):
            field = get_field(lcr, fname)
            rn = get_struct_rowname(field)
            if rn:
                live_lc_landmarks.setdefault(rn, []).append(f"{lcname}.{fname}")

    # Build report for Chapter[1-6].*
    rows_data = []
    for lr in lm_rows:
        nm = lr.get("Name") or ""
        if not CHAPTER_RE.match(nm): continue
        en_field = get_field(lr, "EnabledState")
        en_val = get_enum_value(en_field) or "?"
        hosts = ss_live_zone_landmarks.get(nm, [])
        lc_refs = live_lc_landmarks.get(nm, [])
        if hosts or lc_refs:
            status = "HOSTED"
        else:
            status = "ORPHAN"
        rows_data.append((nm, en_val, hosts, lc_refs, status))

    # Sort: HOSTED first, then ORPHAN; within each, alphabetical by name
    rows_data.sort(key=lambda r: (0 if r[4]=="HOSTED" else 1, r[0]))

    print(f"\nFound {len(rows_data)} Chapter[1-6].* landmarks\n")
    print("| Landmark | EnabledState | Hosted by Live SS zone? | Referenced by Live LC? | Status |")
    print("|---|---|---|---|---|")
    for nm, en, hosts, lcs_, st in rows_data:
        h = "yes ("+", ".join(hosts)+")" if hosts else "no"
        l = "yes ("+", ".join(lcs_)+")" if lcs_ else "no"
        en_short = en.replace("ERowEnabledState::","")
        print(f"| {nm} | {en_short} | {h} | {l} | {st} |")
    print()
    return rows_data

# =====================================================
# TASK 2: NameMap orphan cleanup
# =====================================================
def collect_all_strings(node, found):
    """Walk JSON tree, collect every string value AND derive bare UE type names from $type."""
    if isinstance(node, dict):
        for k, v in node.items():
            if isinstance(k, str):
                found.add(k)
            # Derive bare type names from $type values (e.g. "...EnumPropertyData, UAssetAPI" -> "EnumProperty")
            if k == "$type" and isinstance(v, str):
                head = v.split(",")[0].strip().rsplit(".", 1)[-1]
                found.add(head)
                # Strip "Data" suffix that UAssetAPI uses internally
                if head.endswith("Data"):
                    found.add(head[:-4])
                # Also strip "Property" suffix variants if applicable
            collect_all_strings(v, found)
    elif isinstance(node, list):
        for v in node:
            collect_all_strings(v, found)
    elif isinstance(node, str):
        found.add(node)

# Built-in UE FName types that are commonly required by the binary asset format
# even when not visible as JSON strings. Conservative whitelist.
UE_BUILTIN_TYPES = {
    "ArrayProperty", "BoolProperty", "ByteProperty", "EnumProperty",
    "FloatProperty", "DoubleProperty", "IntProperty", "Int8Property",
    "Int16Property", "Int64Property", "UInt16Property", "UInt32Property",
    "UInt64Property", "NameProperty", "ObjectProperty", "SetProperty",
    "MapProperty", "StrProperty", "StructProperty", "TextProperty",
    "SoftObjectProperty", "SoftClassProperty", "ClassProperty",
    "DelegateProperty", "MulticastDelegateProperty",
    "MulticastInlineDelegateProperty", "MulticastSparseDelegateProperty",
    "InterfaceProperty", "FieldPathProperty", "LazyObjectProperty",
    "WeakObjectProperty", "ScriptStruct", "Function", "Class", "Package",
    "Enum",
}

def split_fname_base(s):
    """Strip _N numeric suffix used by FName instance numbers."""
    if not isinstance(s, str): return s
    if "_" in s:
        base, _, tail = s.rpartition("_")
        if tail.isdigit() and base:
            return base
    return s

def cleanup_namemap(filename):
    print(f"\n--- {filename} ---")
    data = load(filename)
    nm = data.get("NameMap", [])
    old_len = len(nm)

    # Build set of referenced strings: walk EVERYTHING except top-level NameMap list
    referenced = set(UE_BUILTIN_TYPES)
    for k, v in data.items():
        if k == "NameMap":
            continue
        # walk this branch but include the key itself
        referenced.add(k)
        collect_all_strings(v, referenced)

    # Also include base form (without _N suffix) match: an FName entry
    # might appear in data as "Foo_3" while NameMap has "Foo"
    # So we expand referenced with base forms.
    expanded = set(referenced)
    for s in list(referenced):
        if isinstance(s, str):
            expanded.add(split_fname_base(s))
            # Decompose enum-prefixed values like "ECellDirection::West" -> "West", "ECellDirection"
            if "::" in s:
                for part in s.split("::"):
                    if part:
                        expanded.add(part)
                        expanded.add(split_fname_base(part))
            # Segment any /Game/ asset paths or dotted paths
            if "/" in s or "." in s:
                for seg in s.replace(".", "/").split("/"):
                    if seg:
                        expanded.add(seg)
                        expanded.add(split_fname_base(seg))

    # Identify orphans
    orphans = []
    kept = []
    for entry in nm:
        # Conservative: skip anything that looks like a UE asset path or None or empty
        if entry == "None" or entry == "":
            kept.append(entry)
            continue
        if entry.startswith("/Game/") or entry.startswith("/Script/") or entry.startswith("/Engine/"):
            # asset path - check if referenced; if not... still keep conservatively
            if entry in expanded:
                kept.append(entry)
            else:
                orphans.append(entry)
            continue
        # General check
        if entry in expanded:
            kept.append(entry)
        else:
            # Also check base form
            base = split_fname_base(entry)
            if base in expanded:
                kept.append(entry)
            else:
                orphans.append(entry)

    print(f"  NameMap: old={old_len}  kept={len(kept)}  orphans={len(orphans)}")
    print(f"  First 10 orphans: {orphans[:10]}")

    if not orphans:
        print(f"  No orphans to remove.")
        return {"file": filename, "old": old_len, "new": old_len, "removed": 0, "samples": []}

    # Apply removal: preserve order of kept
    data["NameMap"] = kept
    new_len = len(kept)
    data["NamesReferencedFromExportDataCount"] = new_len
    if "Generations" in data and data["Generations"]:
        data["Generations"][0]["NameCount"] = new_len

    save(filename, data)

    # Verify reload
    data2 = load(filename)
    assert len(data2["NameMap"]) == new_len
    assert data2["NamesReferencedFromExportDataCount"] == new_len
    assert data2["Generations"][0]["NameCount"] == new_len
    print(f"  WROTE: NameMap={new_len}, NRefED={new_len}, Gen[0].NameCount={new_len}  (sync OK)")
    return {"file": filename, "old": old_len, "new": new_len, "removed": len(orphans), "samples": orphans[:10]}

def task2():
    print("\n" + "="*70)
    print("TASK 2: NameMap orphan cleanup")
    print("="*70)
    results = []
    for fn in ["DT_Moria_Zones.json", "DT_Moria_Chapters.json",
               "DT_Moria_Landmarks.json", "DT_Moria_LayoutConnections.json"]:
        results.append(cleanup_namemap(fn))
    print("\nSUMMARY:")
    for r in results:
        print(f"  {r['file']}: {r['old']} -> {r['new']}  (removed {r['removed']})")
    return results

if __name__ == "__main__":
    task1()
    task2()
