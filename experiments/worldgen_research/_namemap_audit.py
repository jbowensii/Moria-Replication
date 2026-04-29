"""NameMap audit for UAssetGUI-exported DataTables.

Compares modified vs pristine .json pairs and verifies that every FName
referenced anywhere in the export blob exists in the top-level NameMap.
Also flags missing/duplicate/order-shifted entries and any sibling
indexes (NameMapLookup, NameMapIndexList, NameCount, etc.).
"""
from __future__ import annotations
import json, os, sys
from pathlib import Path

ROOT = Path(r"C:\Users\johnb\OneDrive\Documents\Projects\Moria-Replication\experiments\worldgen_research")

PAIRS = [
    "DT_Moria_Zones",
    "DT_Moria_Landmarks",
    "DT_Moria_Chapters",
    "DT_Moria_LayoutConnections",
    "DT_Moria_ZoneDeck",
    "DT_Moria_ZoneBubbleFilters",
    "DT_Moria_Biomes",
    "World",
]

# Property type fields that hold an FName-like string we should check
FNAME_KEY_HINTS = {
    "Name", "RowName", "EnumValue", "EnumType", "ParentName",
    "PackageGuid", "ObjectName", "AssetPathName", "SubPathString",
    "PackageName", "OuterName",
}

def collect_fnames(node, hits, path="$"):
    """Walk JSON and collect (path, value) for any string that *looks* like an FName.

    UAssetGUI emits FNames as plain strings inside fields like Name/RowName.
    SoftObjectPaths embed them in AssetPathName. We collect every string under
    a known FName-bearing key, plus any string in 'Value' fields whose sibling
    'Type' is 'NameProperty' / 'EnumProperty' / 'ObjectProperty' / 'SoftObjectProperty'.
    """
    if isinstance(node, dict):
        node_type = node.get("$type") or node.get("Type")
        # Handle property-like dicts
        for k, v in node.items():
            kp = f"{path}.{k}"
            if isinstance(v, str):
                if k in FNAME_KEY_HINTS:
                    hits.append((kp, v))
                elif k == "Value" and node_type in {
                    "NameProperty", "NamePropertyData",
                    "EnumProperty", "EnumPropertyData",
                    "ObjectProperty", "ObjectPropertyData",
                    "SoftObjectProperty", "SoftObjectPropertyData",
                    "ByteProperty", "BytePropertyData",
                }:
                    hits.append((kp, v))
            else:
                collect_fnames(v, hits, kp)
    elif isinstance(node, list):
        for i, v in enumerate(node):
            collect_fnames(v, hits, f"{path}[{i}]")

def split_fname(s):
    """Strip _N suffix that UAssetGUI sometimes appends for FName instance numbers."""
    # FNames may appear as "Foo" or "Foo_42" where 42 is the instance number.
    # The base name (before the trailing _<digits>) is what's stored in NameMap.
    if "_" in s:
        base, _, tail = s.rpartition("_")
        if tail.isdigit() and base:
            return base
    return s

def audit(stem):
    mod = ROOT / f"{stem}.json"
    pri = ROOT / f"{stem}.original.json"
    print(f"\n=== {stem} ===")
    if not mod.exists():
        print(f"  MISSING modified: {mod.name}")
        return
    if not pri.exists():
        print(f"  MISSING pristine: {pri.name}")
        return
    with open(mod, encoding="utf-8") as f: M = json.load(f)
    with open(pri, encoding="utf-8") as f: P = json.load(f)

    # Top-level keys
    print(f"  top-level keys (mod): {sorted(M.keys())[:20]}")
    name_keys = [k for k in M.keys() if "name" in k.lower() or "Name" in k]
    print(f"  name-related keys: {name_keys}")

    nm_m = M.get("NameMap") or []
    nm_p = P.get("NameMap") or []
    print(f"  NameMap len: mod={len(nm_m)} pri={len(nm_p)}")

    # NameCount field?
    for k in ("NameCount", "NameMapCount"):
        if k in M:
            print(f"  {k} (mod) = {M[k]}  (NameMap len = {len(nm_m)})  match={M[k]==len(nm_m)}")
        if k in P:
            print(f"  {k} (pri) = {P[k]}  (NameMap len = {len(nm_p)})  match={P[k]==len(nm_p)}")

    # Sibling indexes?
    for k in ("NameMapLookup", "NameMapIndexList", "NameMapHashes"):
        if k in M:
            print(f"  HAS sibling {k} (mod): len={len(M[k]) if hasattr(M[k],'__len__') else '?'}")

    # Duplicates inside NameMap?
    seen = {}
    dups = []
    for i, n in enumerate(nm_m):
        if n in seen:
            dups.append((n, seen[n], i))
        else:
            seen[n] = i
    if dups:
        print(f"  DUPLICATES in NameMap: {dups[:10]}{'...' if len(dups)>10 else ''}")

    # Order check for shared names
    set_p = set(nm_p)
    set_m = set(nm_m)
    only_m = [n for n in nm_m if n not in set_p]
    only_p = [n for n in nm_p if n not in set_m]
    print(f"  NameMap only in mod ({len(only_m)}): {only_m[:30]}")
    print(f"  NameMap only in pri ({len(only_p)}): {only_p[:10]}")

    # Order: are pristine names still at same indices?
    order_shifts = []
    for i, n in enumerate(nm_p):
        if i < len(nm_m) and nm_m[i] != n:
            order_shifts.append((i, n, nm_m[i]))
    if order_shifts:
        print(f"  ORDER SHIFTED at first {min(5,len(order_shifts))} positions: {order_shifts[:5]}")
        print(f"  total shifted indices: {len(order_shifts)}")
    else:
        print(f"  NameMap order: pristine prefix preserved ({len(nm_p)} entries match in-place)")

    # Collect all FName-ish references in modified Exports
    hits = []
    collect_fnames(M.get("Exports", []), hits, "$.Exports")
    # Also check Imports
    collect_fnames(M.get("Imports", []), hits, "$.Imports")
    # And the table_data row names if exposed at top-level
    collect_fnames(M.get("TableData") or {}, hits, "$.TableData")

    nm_set = set(nm_m)
    missing = []
    for p, v in hits:
        if not v: continue
        # SoftObjectPaths often contain full paths; split into segments
        candidates = {v, split_fname(v)}
        if "/" in v or "." in v:
            for seg in v.replace(".", "/").split("/"):
                if seg:
                    candidates.add(seg)
                    candidates.add(split_fname(seg))
        if not any(c in nm_set for c in candidates):
            missing.append((p, v))
    print(f"  FName refs collected: {len(hits)}; not-found-in-NameMap: {len(missing)}")
    for m in missing[:25]:
        print(f"    MISSING: {m[1]}  @ {m[0]}")
    if len(missing) > 25:
        print(f"    ... +{len(missing)-25} more")

    # Find new chapter/zone row names (entries in mod that aren't in pristine row set)
    # Heuristic: Exports[0] DataTable rows — look for "Name" entries on first level
    try:
        rows_m = M["Exports"][0]["Table"]["Data"]
        rows_p = P["Exports"][0]["Table"]["Data"]
        names_m = [r.get("Name") for r in rows_m]
        names_p = [r.get("Name") for r in rows_p]
        new_rows = [n for n in names_m if n not in set(names_p)]
        if new_rows:
            print(f"  NEW rows ({len(new_rows)}): {new_rows}")
            for nr in new_rows:
                # is row name itself in NameMap?
                base = split_fname(nr) if nr else nr
                if nr not in nm_set and base not in nm_set:
                    print(f"    !! row name {nr!r} NOT in NameMap")
    except (KeyError, IndexError, TypeError):
        pass

for stem in PAIRS:
    audit(stem)
