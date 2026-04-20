#!/usr/bin/env python3
"""
Bubble Data Object Remover
Removes specific objects or entire object types from a BubbleData .uasset file
based on a removal specification file.

Pipeline:
  1. UAssetGUI tojson: legacy .uasset -> UAssetAPI JSON
  2. Apply removals to UAssetAPI JSON (this script)
  3. UAssetGUI fromjson: modified JSON -> .uasset/.uexp
  4. retoc to-zen: .uasset/.uexp -> IoStore .pak/.ucas/.utoc

Removal spec format (one entry per line):
  # Comment lines are ignored
  # Position entry - removes a specific object by mesh type + local coordinates:
  {"mesh":"MeshName-Material-Collision-flags","bubble":"BubbleName","local":[x,y,z],...}
  # Type rule - removes ALL objects of a mesh type:
  {"typeRule":"MeshName-Material-Collision-flags"}
  # @ prefix - also treated as a type rule:
  @MeshName-Material-Collision-flags

Searches across InstancedMeshCatalog, InstancedBreakableCatalog,
ConstructionCatalog, DecoVolumes, and BreakableAttachmentDefinition.

Usage: python bubble_data_remover.py
"""

import json
import configparser
import subprocess
import shutil
import zipfile
import tkinter as tk
from tkinter import ttk, filedialog, messagebox, scrolledtext
import os
import copy
from pathlib import Path

# Paths relative to project root
SCRIPT_DIR = Path(__file__).resolve().parent
PROJECT_ROOT = SCRIPT_DIR.parent
INI_PATH = SCRIPT_DIR / 'bubble_data_remover.ini'
MODIFIED_BUBBLES_DIR = PROJECT_ROOT / 'Modified_Bubbles'
LEGACY_ASSETS_DIR = PROJECT_ROOT / 'tools' / 'legacy-assets'
RETOC_EXE = PROJECT_ROOT / 'tools' / 'retoc' / 'bin' / 'retoc.exe'
UASSETGUI_EXE = PROJECT_ROOT / 'tools' / 'UAssetGUI' / 'UAssetGUI.exe'
DOWNLOADS_DIR = Path(os.path.expanduser('~/Downloads'))

UE_VERSION = 'VER_UE4_27'       # for UAssetGUI tojson/fromjson
RETOC_VERSION = 'UE4_27'        # for retoc to-zen (no VER_ prefix)
COORD_EPSILON = 50.0             # coordinate matching tolerance in UE units (~50cm)


# ---------------------------------------------------------------------------
# Removal spec parser
# ---------------------------------------------------------------------------

def extract_mesh_name(mesh_string):
    """Extract mesh name from 'MeshName-Material-Collision-flags' format."""
    return mesh_string.split('-')[0]


def coords_match(x1, y1, z1, x2, y2, z2, epsilon=COORD_EPSILON):
    """Check if two 3D coordinates are within epsilon on each axis."""
    return (abs(x1 - x2) < epsilon and
            abs(y1 - y2) < epsilon and
            abs(z1 - z2) < epsilon)


def parse_removal_file(filepath):
    """Parse the removal specification file.

    Returns:
        type_rules:       list of {'mesh_name': str, 'bubble': str|None, 'raw': str}
        position_entries: list of {'mesh_name': str, 'bubble': str|None,
                                   'local': [x,y,z], 'raw': str}
    """
    type_rules = []
    position_entries = []

    with open(filepath, 'r', encoding='utf-8') as f:
        for line_no, line in enumerate(f, 1):
            line = line.strip()
            if not line or line.startswith('#'):
                continue

            # Handle @ prefix lines as type rules
            if line.startswith('@'):
                mesh_full = line[1:]
                mesh_name = extract_mesh_name(mesh_full)
                type_rules.append({
                    'mesh_name': mesh_name,
                    'bubble': None,
                    'raw': mesh_full,
                    'line': line_no,
                })
                continue

            # Try to parse as JSON
            try:
                data = json.loads(line)
            except json.JSONDecodeError:
                continue

            if 'typeRule' in data:
                mesh_name = extract_mesh_name(data['typeRule'])
                type_rules.append({
                    'mesh_name': mesh_name,
                    'bubble': None,
                    'raw': data['typeRule'],
                    'line': line_no,
                })
            elif 'mesh' in data:
                mesh_name = extract_mesh_name(data['mesh'])
                bubble = data.get('bubble') or data.get('bubbleName')
                if 'local' in data:
                    position_entries.append({
                        'mesh_name': mesh_name,
                        'bubble': bubble,
                        'local': data['local'],  # [x, y, z]
                        'raw': data['mesh'],
                        'line': line_no,
                    })
                else:
                    type_rules.append({
                        'mesh_name': mesh_name,
                        'bubble': bubble,
                        'raw': data['mesh'],
                        'line': line_no,
                    })

    return type_rules, position_entries


def get_bubble_names(type_rules, position_entries):
    """Return sorted list of unique bubble names from removal entries."""
    names = set()
    for entry in type_rules + position_entries:
        b = entry.get('bubble')
        if b:
            names.add(b)
    return sorted(names)


# ---------------------------------------------------------------------------
# UAssetAPI JSON navigation helpers
# ---------------------------------------------------------------------------

def find_property_by_name(value_list, name):
    """Find a property dict by Name in a UAssetAPI Value list."""
    if not isinstance(value_list, list):
        return None
    for item in value_list:
        if isinstance(item, dict) and item.get('Name') == name:
            return item
    return None


def get_uasset_translation(transform_prop):
    """Extract (x, y, z) from a UAssetAPI Transform struct property.

    UAssetAPI Transform has nested structs:
      Transform.Value -> [Rotation, Translation, Scale3D]
      Translation.Value -> [VectorPropertyData with Value: {X, Y, Z}]
    """
    if not transform_prop or 'Value' not in transform_prop:
        return 0.0, 0.0, 0.0

    translation = find_property_by_name(transform_prop['Value'], 'Translation')
    if not translation or 'Value' not in translation:
        return 0.0, 0.0, 0.0

    # Translation.Value is a list with one VectorPropertyData
    vec_list = translation['Value']
    if isinstance(vec_list, list) and len(vec_list) > 0:
        vec = vec_list[0].get('Value', {})
        return float(vec.get('X', 0)), float(vec.get('Y', 0)), float(vec.get('Z', 0))
    return 0.0, 0.0, 0.0


def resolve_import_name(uasset_data, import_index):
    """Resolve a negative import index to an ObjectName.

    UAssetAPI uses 1-based negative indices: -1 = Imports[0], -215 = Imports[214].
    """
    if import_index >= 0:
        return None
    idx = abs(import_index) - 1
    imports = uasset_data.get('Imports', [])
    if 0 <= idx < len(imports):
        return imports[idx].get('ObjectName', '')
    return None


def build_import_lookup(uasset_data):
    """Build a dict mapping negative import index -> ObjectName."""
    lookup = {}
    for i, imp in enumerate(uasset_data.get('Imports', [])):
        lookup[-(i + 1)] = imp.get('ObjectName', '')
    return lookup


# ---------------------------------------------------------------------------
# UAssetAPI JSON removal engine
# ---------------------------------------------------------------------------

class RemovalStats:
    """Tracks removal counts for logging."""

    def __init__(self):
        self.instanced_mesh = 0
        self.instanced_breakable = 0
        self.construction = 0
        self.deco_volume = 0
        self.attachment = 0

    @property
    def total(self):
        return (self.instanced_mesh + self.instanced_breakable +
                self.construction + self.deco_volume + self.attachment)


def apply_removals_uasset(uasset_data, type_rules, position_entries, log_fn=None):
    """Apply removal operations to a UAssetAPI JSON structure (mutates in place).

    Args:
        uasset_data: The full parsed UAssetAPI JSON dict.
        type_rules: List of type rule dicts (remove all of mesh type).
        position_entries: List of position entry dicts (remove specific objects).
        log_fn: Optional callable for logging messages.

    Returns:
        RemovalStats with counts of removed items.
    """
    if log_fn is None:
        log_fn = lambda msg: None

    stats = RemovalStats()
    import_lookup = build_import_lookup(uasset_data)

    # Navigate to the export data — BubbleData has one export
    exports = uasset_data.get('Exports', [])
    if not exports:
        log_fn("ERROR: No exports found in UAssetAPI JSON")
        return stats

    export_data = exports[0].get('Data', [])
    if not export_data:
        log_fn("ERROR: Export has no Data")
        return stats

    # Find the catalog properties
    imc_prop = find_property_by_name(export_data, 'InstancedMeshCatalog')
    ibc_prop = find_property_by_name(export_data, 'InstancedBreakableCatalog')
    cc_prop = find_property_by_name(export_data, 'ConstructionCatalog')
    dv_prop = find_property_by_name(export_data, 'DecoVolumes')
    bad_prop = find_property_by_name(export_data, 'BreakableAttachmentDefinition')

    # --- InstancedMeshCatalog ---
    if imc_prop and 'Value' in imc_prop:
        batches_prop = find_property_by_name(imc_prop['Value'], 'Batches')
        if batches_prop and 'Value' in batches_prop:
            batches = batches_prop['Value']
            new_batches = []

            for batch in batches:
                batch_value = batch.get('Value', [])
                defn_prop = find_property_by_name(batch_value, 'Definition')
                instances_prop = find_property_by_name(batch_value, 'Instances')

                # Get mesh name from Definition.Mesh import reference
                batch_mesh = '?'
                if defn_prop and 'Value' in defn_prop:
                    mesh_prop = find_property_by_name(defn_prop['Value'], 'Mesh')
                    if mesh_prop:
                        mesh_ref = mesh_prop.get('Value', 0)
                        batch_mesh = import_lookup.get(mesh_ref, '?')

                instances = instances_prop.get('Value', []) if instances_prop else []

                # Check type rules — remove entire batch if mesh matches
                type_match = any(tr['mesh_name'] in batch_mesh for tr in type_rules)
                if type_match:
                    count = len(instances)
                    stats.instanced_mesh += count
                    log_fn(f"  [TypeRule] Removed {count}x {batch_mesh} (InstancedMesh)")
                    continue  # skip this batch

                # Check position entries — remove specific instances
                surviving = []
                for inst in instances:
                    inst_value = inst.get('Value', [])
                    name_prop = find_property_by_name(inst_value, 'Name')
                    transform_prop = find_property_by_name(inst_value, 'Transform')
                    ix, iy, iz = get_uasset_translation(transform_prop)
                    inst_name = name_prop.get('Value', '?') if name_prop else '?'

                    removed = False
                    for pe in position_entries:
                        if pe['mesh_name'] == batch_mesh:
                            px, py, pz = pe['local']
                            if coords_match(ix, iy, iz, px, py, pz):
                                stats.instanced_mesh += 1
                                log_fn(f"  [Position] Removed {inst_name} at "
                                       f"({ix:.1f}, {iy:.1f}, {iz:.1f}) (InstancedMesh)")
                                removed = True
                                break
                    if not removed:
                        surviving.append(inst)

                if surviving:
                    instances_prop['Value'] = surviving
                    new_batches.append(batch)
                elif instances:
                    log_fn(f"  [Cleanup] Dropped empty batch for {batch_mesh}")

            batches_prop['Value'] = new_batches

    # --- InstancedBreakableCatalog ---
    if ibc_prop and 'Value' in ibc_prop:
        batches_prop = find_property_by_name(ibc_prop['Value'], 'Batches')
        if batches_prop and 'Value' in batches_prop:
            batches = batches_prop['Value']
            new_batches = []

            for batch in batches:
                batch_value = batch.get('Value', [])
                defn_prop = find_property_by_name(batch_value, 'Definition')
                instances_prop = find_property_by_name(batch_value, 'Instances')

                # Get class name from Definition.BreakableClass
                class_name = '?'
                if defn_prop and 'Value' in defn_prop:
                    bc_prop = find_property_by_name(defn_prop['Value'], 'BreakableClass')
                    if bc_prop and 'Value' in bc_prop:
                        # SoftObjectProperty — Value is a dict with AssetPath.AssetPathName
                        val = bc_prop['Value']
                        if isinstance(val, dict):
                            asset_path = val.get('AssetPath', {}).get('AssetPathName', '')
                            if not asset_path:
                                asset_path = val.get('AssetPathName', '')
                            class_name = asset_path.split('/')[-1].split('.')[0]
                        elif isinstance(val, list):
                            # May be wrapped differently
                            for item in val:
                                if isinstance(item, dict) and 'AssetPathName' in item:
                                    asset_path = item['AssetPathName']
                                    class_name = asset_path.split('/')[-1].split('.')[0]
                                    break

                instances = instances_prop.get('Value', []) if instances_prop else []

                # Check type rules
                type_match = any(tr['mesh_name'] in class_name for tr in type_rules)
                if type_match:
                    count = len(instances)
                    stats.instanced_breakable += count
                    log_fn(f"  [TypeRule] Removed {count}x {class_name} (Breakable)")
                    continue

                # Check position entries
                surviving = []
                for inst in instances:
                    inst_value = inst.get('Value', [])
                    transform_prop = find_property_by_name(inst_value, 'Transform')
                    ix, iy, iz = get_uasset_translation(transform_prop)

                    removed = False
                    for pe in position_entries:
                        if pe['mesh_name'] in class_name:
                            px, py, pz = pe['local']
                            if coords_match(ix, iy, iz, px, py, pz):
                                stats.instanced_breakable += 1
                                log_fn(f"  [Position] Removed {class_name} at "
                                       f"({ix:.1f}, {iy:.1f}, {iz:.1f}) (Breakable)")
                                removed = True
                                break
                    if not removed:
                        surviving.append(inst)

                if surviving:
                    instances_prop['Value'] = surviving
                    new_batches.append(batch)
                elif instances:
                    log_fn(f"  [Cleanup] Dropped empty batch for {class_name}")

            batches_prop['Value'] = new_batches

    # --- ConstructionCatalog + DecoVolumes ---
    blocks_to_remove = set()  # shared with BreakableAttachmentDefinition below

    if cc_prop and 'Value' in cc_prop:
        blocks_prop = find_property_by_name(cc_prop['Value'], 'Blocks')
        volumes_prop = None
        if dv_prop and 'Value' in dv_prop:
            volumes_prop = find_property_by_name(dv_prop['Value'], 'Volumes')

        if blocks_prop and 'Value' in blocks_prop:
            blocks = blocks_prop['Value']
            volumes = volumes_prop.get('Value', []) if volumes_prop else []

            # Build volume lookup by name
            dv_by_name = {}
            for vol in volumes:
                vol_value = vol.get('Value', [])
                name_prop = find_property_by_name(vol_value, 'Name')
                if name_prop:
                    dv_by_name[name_prop.get('Value', '')] = vol

            for block in blocks:
                block_value = block.get('Value', [])
                name_prop = find_property_by_name(block_value, 'Name')
                block_name = name_prop.get('Value', '') if name_prop else ''

                # Type rules
                for tr in type_rules:
                    if tr['mesh_name'] in block_name:
                        blocks_to_remove.add(block_name)
                        log_fn(f"  [TypeRule] Marked {block_name} (Construction)")
                        break

                # Position entries via DecoVolume coordinates
                if block_name not in blocks_to_remove and block_name in dv_by_name:
                    vol = dv_by_name[block_name]
                    vol_value = vol.get('Value', [])
                    volume_struct = find_property_by_name(vol_value, 'Volume')
                    if volume_struct and 'Value' in volume_struct:
                        base_transform = find_property_by_name(
                            volume_struct['Value'], 'BaseTransform')
                        vx, vy, vz = get_uasset_translation(base_transform)

                        for pe in position_entries:
                            if pe['mesh_name'] in block_name:
                                px, py, pz = pe['local']
                                if coords_match(vx, vy, vz, px, py, pz):
                                    blocks_to_remove.add(block_name)
                                    log_fn(f"  [Position] Marked {block_name} at "
                                           f"({vx:.1f}, {vy:.1f}, {vz:.1f}) (Construction)")
                                    break

            # Remove blocks
            new_blocks = []
            for block in blocks:
                block_value = block.get('Value', [])
                name_prop = find_property_by_name(block_value, 'Name')
                block_name = name_prop.get('Value', '') if name_prop else ''
                if block_name not in blocks_to_remove:
                    new_blocks.append(block)
            removed_blocks = len(blocks) - len(new_blocks)
            stats.construction += removed_blocks
            blocks_prop['Value'] = new_blocks

            # Remove matching DecoVolumes
            if volumes_prop:
                new_volumes = []
                for vol in volumes:
                    vol_value = vol.get('Value', [])
                    name_prop = find_property_by_name(vol_value, 'Name')
                    vol_name = name_prop.get('Value', '') if name_prop else ''
                    if vol_name not in blocks_to_remove:
                        new_volumes.append(vol)
                removed_vols = len(volumes) - len(new_volumes)
                stats.deco_volume += removed_vols
                volumes_prop['Value'] = new_volumes
                if removed_vols:
                    log_fn(f"  [Cleanup] Removed {removed_vols} DecoVolumes")

    # --- Standalone DecoVolumes (not tied to ConstructionCatalog blocks) ---
    # Spider webs and other standalone DecoVolumes have no matching CC block,
    # so the CC-based pass above never checks them.  This pass catches them.
    if dv_prop and 'Value' in dv_prop:
        volumes_prop = find_property_by_name(dv_prop['Value'], 'Volumes')
        if volumes_prop and 'Value' in volumes_prop:
            volumes = volumes_prop['Value']
            new_volumes = []
            standalone_removed = 0
            for vol in volumes:
                vol_value = vol.get('Value', [])
                name_prop = find_property_by_name(vol_value, 'Name')
                vol_name = name_prop.get('Value', '') if name_prop else ''

                # Skip volumes already removed by CC pass
                if vol_name in blocks_to_remove:
                    continue

                # Check type rules against volume name
                matched = False
                for tr in type_rules:
                    if tr['mesh_name'] in vol_name:
                        log_fn(f"  [TypeRule] Removed standalone DecoVolume: {vol_name}")
                        standalone_removed += 1
                        matched = True
                        break

                # Check position entries against volume coordinates
                if not matched:
                    volume_struct = find_property_by_name(vol_value, 'Volume')
                    if volume_struct and 'Value' in volume_struct:
                        base_transform = find_property_by_name(
                            volume_struct['Value'], 'BaseTransform')
                        vx, vy, vz = get_uasset_translation(base_transform)
                        for pe in position_entries:
                            if pe['mesh_name'] in vol_name:
                                px, py, pz = pe['local']
                                if coords_match(vx, vy, vz, px, py, pz):
                                    log_fn(f"  [Position] Removed standalone DecoVolume: "
                                           f"{vol_name} at ({vx:.1f}, {vy:.1f}, {vz:.1f})")
                                    standalone_removed += 1
                                    matched = True
                                    break

                if not matched:
                    new_volumes.append(vol)

            if standalone_removed:
                stats.deco_volume += standalone_removed
                volumes_prop['Value'] = new_volumes

    # --- BreakableAttachmentDefinition ---
    if bad_prop and 'Value' in bad_prop and blocks_to_remove:
        attach_prop = find_property_by_name(bad_prop['Value'], 'Attachments')
        if attach_prop and 'Value' in attach_prop:
            attachments = attach_prop['Value']
            # Each entry is a list (MapPropertyData key-value pair):
            #   [0] = NamePropertyData with Value = block name (the key)
            #   [1] = StructPropertyData (the value)
            new_attachments = []
            for att in attachments:
                key_name = ''
                if isinstance(att, list) and len(att) > 0:
                    key_name = att[0].get('Value', '')
                elif isinstance(att, dict):
                    key_name = att.get('Value', '')
                if key_name not in blocks_to_remove:
                    new_attachments.append(att)
            removed_att = len(attachments) - len(new_attachments)
            stats.attachment += removed_att
            attach_prop['Value'] = new_attachments
            if removed_att:
                log_fn(f"  [Cleanup] Removed {removed_att} BreakableAttachmentDefinition")

    return stats


def count_uasset_objects(uasset_data):
    """Count objects across all catalogs in UAssetAPI JSON."""
    exports = uasset_data.get('Exports', [])
    if not exports:
        return 0, 0, 0

    export_data = exports[0].get('Data', [])
    im_count = ib_count = cc_count = 0

    imc_prop = find_property_by_name(export_data, 'InstancedMeshCatalog')
    if imc_prop and 'Value' in imc_prop:
        batches_prop = find_property_by_name(imc_prop['Value'], 'Batches')
        if batches_prop and 'Value' in batches_prop:
            for batch in batches_prop['Value']:
                inst_prop = find_property_by_name(batch.get('Value', []), 'Instances')
                if inst_prop and 'Value' in inst_prop:
                    im_count += len(inst_prop['Value'])

    ibc_prop = find_property_by_name(export_data, 'InstancedBreakableCatalog')
    if ibc_prop and 'Value' in ibc_prop:
        batches_prop = find_property_by_name(ibc_prop['Value'], 'Batches')
        if batches_prop and 'Value' in batches_prop:
            for batch in batches_prop['Value']:
                inst_prop = find_property_by_name(batch.get('Value', []), 'Instances')
                if inst_prop and 'Value' in inst_prop:
                    ib_count += len(inst_prop['Value'])

    cc_prop = find_property_by_name(export_data, 'ConstructionCatalog')
    if cc_prop and 'Value' in cc_prop:
        blocks_prop = find_property_by_name(cc_prop['Value'], 'Blocks')
        if blocks_prop and 'Value' in blocks_prop:
            cc_count = len(blocks_prop['Value'])

    return im_count, ib_count, cc_count


# ---------------------------------------------------------------------------
# Tkinter UI
# ---------------------------------------------------------------------------

class BubbleDataRemoverApp:
    def __init__(self, root):
        self.root = root
        root.title("Bubble Data Object Remover")
        root.geometry("900x700")
        root.resizable(True, True)

        # State
        self.bubble_data_path = tk.StringVar()   # legacy .uasset path
        self.removal_spec_path = tk.StringVar()
        self.selected_bubble = tk.StringVar()
        self.bubble_names = []
        self.last_output_dir = None
        self.last_bd_name = None
        self.last_bubble_name = None
        self.last_modified_json = None  # path to modified UAssetAPI JSON

        self._build_ui()
        self._load_settings()

        # Auto-populate bubble dropdown when removal spec path changes
        self.removal_spec_path.trace_add('write', self._on_spec_path_changed)

    def _build_ui(self):
        # --- File selection frame ---
        file_frame = ttk.LabelFrame(self.root, text="Input Files", padding=10)
        file_frame.pack(fill='x', padx=10, pady=(10, 5))

        # BubbleData .uasset file
        ttk.Label(file_frame, text="Bubble Data (.uasset):").grid(
            row=0, column=0, sticky='w', pady=2)
        ttk.Entry(file_frame, textvariable=self.bubble_data_path, width=70).grid(
            row=0, column=1, padx=5, pady=2)
        ttk.Button(file_frame, text="Browse...",
                    command=self._browse_bubble_data).grid(
            row=0, column=2, pady=2)

        # Removal spec file
        ttk.Label(file_frame, text="Removed Instances:").grid(
            row=1, column=0, sticky='w', pady=2)
        ttk.Entry(file_frame, textvariable=self.removal_spec_path, width=70).grid(
            row=1, column=1, padx=5, pady=2)
        ttk.Button(file_frame, text="Browse...",
                    command=self._browse_removal_spec).grid(
            row=1, column=2, pady=2)

        # Bubble name selector
        ttk.Label(file_frame, text="Bubble Name:").grid(
            row=2, column=0, sticky='w', pady=2)
        self.bubble_combo = ttk.Combobox(
            file_frame, textvariable=self.selected_bubble,
            state='readonly', width=40)
        self.bubble_combo.grid(row=2, column=1, sticky='w', padx=5, pady=2)

        file_frame.columnconfigure(1, weight=1)

        # --- Action buttons ---
        btn_frame = ttk.Frame(self.root)
        btn_frame.pack(fill='x', padx=10, pady=5)

        self.process_btn = ttk.Button(
            btn_frame, text="Process Removals", command=self._process)
        self.process_btn.pack(side='left', padx=5)

        self.package_btn = ttk.Button(
            btn_frame, text="Package as IoStore Mod", command=self._package)
        self.package_btn.pack(side='left', padx=5)

        ttk.Button(btn_frame, text="Clear Log",
                    command=self._clear_log).pack(side='left', padx=5)

        # --- Log area ---
        log_frame = ttk.LabelFrame(self.root, text="Log", padding=5)
        log_frame.pack(fill='both', expand=True, padx=10, pady=(5, 10))

        self.log_text = scrolledtext.ScrolledText(
            log_frame, wrap='word', font=('Consolas', 9))
        self.log_text.pack(fill='both', expand=True)

    # --- Settings persistence ---

    def _load_settings(self):
        """Load last-used paths and bubble name from INI file."""
        if not INI_PATH.exists():
            return
        cfg = configparser.ConfigParser()
        cfg.read(INI_PATH, encoding='utf-8')
        if 'settings' not in cfg:
            return
        s = cfg['settings']

        bd = s.get('bubble_data_path', '')
        sp = s.get('removal_spec_path', '')
        bubble = s.get('selected_bubble', '')

        if bd:
            self.bubble_data_path.set(bd)
        if sp:
            self.removal_spec_path.set(sp)
            # Silently populate bubble dropdown without logging
            if os.path.isfile(sp):
                self._load_bubble_names(sp, silent=True)
        if bubble:
            self.selected_bubble.set(bubble)

        # Restore last build state for Package button
        if 'last_build' in cfg:
            lb = cfg['last_build']
            bd_name = lb.get('bd_name', '')
            bubble_name = lb.get('bubble_name', '')
            modified_json = lb.get('modified_json', '')
            output_dir = lb.get('output_dir', '')
            if bd_name and modified_json and os.path.isfile(modified_json):
                self.last_bd_name = bd_name
                self.last_bubble_name = bubble_name
                self.last_modified_json = Path(modified_json)
                self.last_output_dir = Path(output_dir) if output_dir else None

    def _save_settings(self):
        """Save current paths, bubble name, and last build state to INI file."""
        cfg = configparser.ConfigParser()
        cfg['settings'] = {
            'bubble_data_path': self.bubble_data_path.get(),
            'removal_spec_path': self.removal_spec_path.get(),
            'selected_bubble': self.selected_bubble.get(),
        }
        cfg['last_build'] = {
            'bd_name': self.last_bd_name or '',
            'bubble_name': self.last_bubble_name or '',
            'modified_json': str(self.last_modified_json) if self.last_modified_json else '',
            'output_dir': str(self.last_output_dir) if self.last_output_dir else '',
        }
        with open(INI_PATH, 'w', encoding='utf-8') as f:
            cfg.write(f)

    def _log(self, message):
        self.log_text.insert('end', message + '\n')
        self.log_text.see('end')
        self.root.update_idletasks()

    def _clear_log(self):
        self.log_text.delete('1.0', 'end')

    def _on_spec_path_changed(self, *args):
        """Callback when removal spec path changes."""
        path = self.removal_spec_path.get()
        if path and os.path.isfile(path):
            self._load_bubble_names(path)

    def _initial_dir(self, path_var):
        """Get the directory from a path StringVar, or empty string."""
        current = path_var.get()
        if current:
            d = os.path.dirname(current)
            if os.path.isdir(d):
                return d
        return ''

    def _browse_bubble_data(self):
        path = filedialog.askopenfilename(
            title="Select BubbleData .uasset file (BD_*)",
            initialdir=self._initial_dir(self.bubble_data_path),
            filetypes=[("UAsset files", "*.uasset"), ("All files", "*.*")])
        if path:
            self.bubble_data_path.set(path)

    def _browse_removal_spec(self):
        path = filedialog.askopenfilename(
            title="Select Removal Spec file",
            initialdir=self._initial_dir(self.removal_spec_path),
            filetypes=[("All files", "*.*"), ("Text files", "*.txt"),
                       ("JSON files", "*.json")])
        if path:
            self.removal_spec_path.set(path)
            self._load_bubble_names(path)

    def _load_bubble_names(self, spec_path, silent=False):
        """Parse removal spec and populate bubble name dropdown."""
        try:
            type_rules, position_entries = parse_removal_file(spec_path)
            names = get_bubble_names(type_rules, position_entries)

            if names:
                self.bubble_names = names
                self.bubble_combo['values'] = names
                if not silent:
                    self.selected_bubble.set(names[0])
                    self._log(f"Found bubble names: {', '.join(names)}")
            else:
                self.bubble_names = ['(all)']
                self.bubble_combo['values'] = ['(all)']
                if not silent:
                    self.selected_bubble.set('(all)')
                    self._log("No bubble names in spec — rules apply to all bubbles")

            if not silent:
                self._log(f"Loaded {len(type_rules)} type rules, "
                          f"{len(position_entries)} position entries")
        except Exception as e:
            if not silent:
                self._log(f"ERROR loading removal spec: {e}")

    def _run_uassetgui_tojson(self, uasset_path, json_path):
        """Convert .uasset to UAssetAPI JSON using UAssetGUI tojson."""
        if not UASSETGUI_EXE.exists():
            self._log(f"ERROR: UAssetGUI not found at {UASSETGUI_EXE}")
            messagebox.showerror("Error",
                f"UAssetGUI.exe not found at:\n{UASSETGUI_EXE}\n\n"
                "Copy UAssetGUI.exe to tools/UAssetGUI/UAssetGUI.exe")
            return False

        cmd = [str(UASSETGUI_EXE), 'tojson',
               str(uasset_path), str(json_path), UE_VERSION]
        self._log(f"  UAssetGUI tojson: {Path(uasset_path).name}")
        try:
            result = subprocess.run(
                cmd, capture_output=True, text=True, timeout=120)
            if result.returncode != 0:
                self._log(f"  ERROR: UAssetGUI tojson failed (exit {result.returncode})")
                if result.stderr:
                    self._log(f"  {result.stderr.strip()}")
                if result.stdout:
                    self._log(f"  {result.stdout.strip()}")
                return False
            return True
        except Exception as e:
            self._log(f"  ERROR: {e}")
            return False

    def _run_uassetgui_fromjson(self, json_path, uasset_path):
        """Convert UAssetAPI JSON back to .uasset/.uexp using UAssetGUI fromjson."""
        cmd = [str(UASSETGUI_EXE), 'fromjson',
               str(json_path), str(uasset_path), UE_VERSION]
        self._log(f"  UAssetGUI fromjson: {Path(json_path).name}")
        try:
            result = subprocess.run(
                cmd, capture_output=True, text=True, timeout=120)
            if result.returncode != 0:
                self._log(f"  ERROR: UAssetGUI fromjson failed (exit {result.returncode})")
                if result.stderr:
                    self._log(f"  {result.stderr.strip()}")
                if result.stdout:
                    self._log(f"  {result.stdout.strip()}")
                return False
            return True
        except Exception as e:
            self._log(f"  ERROR: {e}")
            return False

    def _process(self):
        """Main processing: convert .uasset to JSON, apply removals, save."""
        bd_path = self.bubble_data_path.get()
        spec_path = self.removal_spec_path.get()
        bubble_name = self.selected_bubble.get()

        if not bd_path or not os.path.isfile(bd_path):
            messagebox.showerror("Error",
                "Please select a valid BubbleData .uasset file.\n\n"
                "This should be a BD_*.uasset file from:\n"
                "tools/legacy-assets/Moria/Content/Tech/Data/Bubbles/GameWorldCatalog/")
            return
        if not spec_path or not os.path.isfile(spec_path):
            messagebox.showerror("Error",
                "Please select a valid Removed Instances file.\n\n"
                "This is the removed_instances.txt from your mod.")
            return

        # Validate it's a .uasset, not a .json or .txt
        bd_basename = os.path.basename(bd_path)
        if bd_basename.endswith('.json') or bd_basename.endswith('.txt'):
            messagebox.showerror("Wrong File Type",
                f"You selected: {bd_basename}\n\n"
                "This tool now works with .uasset files directly.\n\n"
                "Select the BD_*.uasset from:\n"
                "tools/legacy-assets/Moria/Content/Tech/Data/Bubbles/GameWorldCatalog/")
            return

        # Detect BF_ (BubbleDef) instead of BD_ (BubbleData)
        if bd_basename.startswith('BF_'):
            messagebox.showerror("Wrong File Type",
                f"You selected a BubbleDef file (BF_):\n{bd_basename}\n\n"
                "You need the BubbleData file (BD_) instead.\n"
                f"Look for: BD_{bd_basename[3:]}")
            return

        # Detect swapped files
        try:
            with open(bd_path, 'rb') as f:
                header = f.read(4)
            # .uasset files start with the magic bytes C1 83 2A 9E
            # If it starts with text characters, it's not a .uasset
            if header[:1] in (b'#', b'{', b'@'):
                messagebox.showerror("Files Swapped?",
                    "The BubbleData file appears to be a text file, not a .uasset.\n\n"
                    "Swap the files:\n"
                    "- Bubble Data = BD_*.uasset\n"
                    "- Removed Instances = removed_instances.txt")
                return
        except Exception:
            pass

        # Ensure bubble dropdown is populated
        if not self.bubble_names or self.bubble_names == ['(all)']:
            self._load_bubble_names(spec_path)

        bd_name = Path(bd_path).stem  # e.g. 'BD_BB_Chapter2_GameStart'

        self._clear_log()
        self._log(f"{'=' * 60}")
        self._log(f"Bubble Data Object Remover")
        self._log(f"{'=' * 60}")
        self._log(f"BubbleData: {bd_path}")
        self._log(f"Removal Spec: {spec_path}")
        self._log(f"Bubble Filter: {bubble_name}")
        self._log("")

        # --- Step 1: Convert .uasset to UAssetAPI JSON ---
        self._log("Step 1: Converting .uasset to UAssetAPI JSON...")
        out_dir = MODIFIED_BUBBLES_DIR / bd_name
        out_dir.mkdir(parents=True, exist_ok=True)

        source_json = out_dir / f"{bd_name}_source.json"
        if not self._run_uassetgui_tojson(bd_path, source_json):
            return

        size_mb = os.path.getsize(source_json) / (1024 * 1024)
        self._log(f"  Converted: {source_json.name} ({size_mb:.1f} MB)")
        self._log("")

        # --- Load UAssetAPI JSON ---
        self._log("Loading UAssetAPI JSON...")
        try:
            with open(source_json, 'r', encoding='utf-8') as f:
                uasset_data = json.load(f)
        except Exception as e:
            self._log(f"ERROR loading JSON: {e}")
            return

        # Count originals
        orig_im, orig_ib, orig_cc = count_uasset_objects(uasset_data)
        orig_total = orig_im + orig_ib + orig_cc
        self._log(f"  InstancedMesh instances: {orig_im}")
        self._log(f"  Breakable instances:     {orig_ib}")
        self._log(f"  Construction blocks:     {orig_cc}")
        self._log(f"  Total objects:           {orig_total}")
        self._log("")

        # --- Load and filter removal spec ---
        self._log("Loading removal spec...")
        try:
            type_rules, position_entries = parse_removal_file(spec_path)
        except Exception as e:
            self._log(f"ERROR loading removal spec: {e}")
            return

        # Filter by selected bubble name
        if bubble_name and bubble_name != '(all)':
            position_entries = [pe for pe in position_entries
                                if pe.get('bubble') == bubble_name
                                or pe.get('bubble') is None]
            type_rules_filtered = [tr for tr in type_rules
                                   if tr.get('bubble') == bubble_name
                                   or tr.get('bubble') is None]
        else:
            type_rules_filtered = type_rules

        self._log(f"  Type rules to apply:      {len(type_rules_filtered)}")
        self._log(f"  Position entries to apply: {len(position_entries)}")
        self._log("")

        if not type_rules_filtered and not position_entries:
            self._log("Nothing to remove! Check bubble name filter.")
            return

        # --- Step 2: Apply removals ---
        self._log("Step 2: Applying removals...")
        self._log("-" * 40)

        working_data = copy.deepcopy(uasset_data)
        stats = apply_removals_uasset(
            working_data, type_rules_filtered, position_entries,
            log_fn=self._log)

        self._log("-" * 40)
        self._log("")

        # Count remaining
        rem_im, rem_ib, rem_cc = count_uasset_objects(working_data)
        rem_total = rem_im + rem_ib + rem_cc

        self._log("=== Summary ===")
        self._log(f"  InstancedMesh:   {orig_im:5d} -> {rem_im:5d}  "
                  f"(removed {stats.instanced_mesh})")
        self._log(f"  Breakable:       {orig_ib:5d} -> {rem_ib:5d}  "
                  f"(removed {stats.instanced_breakable})")
        self._log(f"  Construction:    {orig_cc:5d} -> {rem_cc:5d}  "
                  f"(removed {stats.construction})")
        self._log(f"  DecoVolumes:     removed {stats.deco_volume}")
        self._log(f"  Attachments:     removed {stats.attachment}")
        self._log(f"  TOTAL:           {orig_total:5d} -> {rem_total:5d}  "
                  f"(removed {stats.total})")
        self._log("")

        if stats.total == 0:
            self._log("No objects matched the removal criteria.")
            self._log("Check that mesh names and coordinates are correct.")
            return

        # --- Save modified UAssetAPI JSON ---
        modified_json = out_dir / f"{bd_name}.json"
        self._log(f"Saving modified JSON: {modified_json}")
        try:
            with open(modified_json, 'w', encoding='utf-8') as f:
                json.dump(working_data, f, indent=2, ensure_ascii=False)
            size_mb = os.path.getsize(modified_json) / (1024 * 1024)
            self._log(f"  Saved ({size_mb:.1f} MB)")
        except Exception as e:
            self._log(f"ERROR saving: {e}")
            return

        # Store state for packaging
        self.last_output_dir = out_dir
        self.last_bd_name = bd_name
        self.last_bubble_name = bubble_name if bubble_name != '(all)' else bd_name
        self.last_modified_json = modified_json

        self._log("")
        self._log("Done! Click 'Package as IoStore Mod' to build the mod pak.")

        # Save settings
        self._save_settings()

    def _package(self):
        """Package: JSON -> .uasset/.uexp (UAssetGUI) -> IoStore (retoc) -> zip."""
        if not self.last_output_dir or not self.last_modified_json:
            messagebox.showerror("Error",
                "No processed data to package.\n\n"
                "Run 'Process Removals' first, then package.")
            return

        bd_name = self.last_bd_name
        bubble_name = self.last_bubble_name or bd_name
        pak_name = f"Bubble_{bubble_name}_P"
        out_dir = self.last_output_dir
        modified_json = self.last_modified_json

        self._log("")
        self._log(f"{'=' * 60}")
        self._log(f"Packaging IoStore Mod: {pak_name}")
        self._log(f"{'=' * 60}")

        # Verify tools exist
        if not UASSETGUI_EXE.exists():
            self._log(f"ERROR: UAssetGUI not found at {UASSETGUI_EXE}")
            messagebox.showerror("Error",
                f"UAssetGUI.exe not found at:\n{UASSETGUI_EXE}\n\n"
                "Copy UAssetGUI.exe to tools/UAssetGUI/UAssetGUI.exe")
            return
        if not RETOC_EXE.exists():
            self._log(f"ERROR: retoc not found at {RETOC_EXE}")
            messagebox.showerror("Error",
                f"retoc.exe not found at:\n{RETOC_EXE}\n\n"
                "Install retoc to tools/retoc/bin/retoc.exe")
            return

        # --- Step 3: Convert modified JSON -> .uasset/.uexp ---
        self._log("Step 3: Converting modified JSON to .uasset/.uexp...")

        # Create staging with UE4 content path structure
        staging_dir = out_dir / 'staging'
        content_subpath = Path('Moria/Content/Tech/Data/Bubbles/GameWorldCatalog')
        staging_content = staging_dir / content_subpath
        staging_content.mkdir(parents=True, exist_ok=True)

        output_uasset = staging_content / f"{bd_name}.uasset"
        if not self._run_uassetgui_fromjson(modified_json, output_uasset):
            return

        # Verify output
        output_uexp = staging_content / f"{bd_name}.uexp"
        if not output_uasset.exists():
            self._log(f"  ERROR: .uasset not created at {output_uasset}")
            return

        uasset_size = os.path.getsize(output_uasset) / 1024
        uexp_size = os.path.getsize(output_uexp) / 1024 if output_uexp.exists() else 0
        self._log(f"  Created: {bd_name}.uasset ({uasset_size:.0f} KB)")
        self._log(f"  Created: {bd_name}.uexp ({uexp_size:.0f} KB)")
        self._log("")

        # --- Step 4: Pack into IoStore format ---
        self._log("Step 4: Packing into IoStore format...")

        output_utoc = out_dir / f"{pak_name}.utoc"
        cmd = [
            str(RETOC_EXE),
            'to-zen', '-v',
            '--version', RETOC_VERSION,
            str(staging_dir),
            str(output_utoc),
        ]

        self._log(f"  retoc to-zen...")
        try:
            result = subprocess.run(
                cmd, capture_output=True, text=True, timeout=120)
            if result.stdout:
                for line in result.stdout.strip().split('\n'):
                    self._log(f"  [retoc] {line}")
            if result.stderr:
                for line in result.stderr.strip().split('\n'):
                    self._log(f"  [retoc] {line}")
            if result.returncode != 0:
                self._log(f"  ERROR: retoc exited with code {result.returncode}")
                return
        except subprocess.TimeoutExpired:
            self._log("  ERROR: retoc timed out after 120 seconds")
            return
        except Exception as e:
            self._log(f"  ERROR: {e}")
            return

        # Verify output files
        pak_path = out_dir / f"{pak_name}.pak"
        ucas_path = out_dir / f"{pak_name}.ucas"
        utoc_path = output_utoc

        missing = []
        for p in [pak_path, ucas_path, utoc_path]:
            if not p.exists():
                missing.append(p.name)
        if missing:
            self._log(f"  ERROR: Missing output files: {', '.join(missing)}")
            return

        self._log("")
        self._log("IoStore files created:")
        for p in [pak_path, ucas_path, utoc_path]:
            sz = os.path.getsize(p) / 1024
            self._log(f"  {p.name} ({sz:.0f} KB)")

        # --- Step 5: Zip to Downloads ---
        zip_name = f"{pak_name}.zip"
        zip_path = DOWNLOADS_DIR / zip_name

        self._log(f"Creating zip: {zip_path}")
        try:
            with zipfile.ZipFile(zip_path, 'w', zipfile.ZIP_DEFLATED) as zf:
                zf.write(pak_path, pak_path.name)
                zf.write(ucas_path, ucas_path.name)
                zf.write(utoc_path, utoc_path.name)
            zip_size = os.path.getsize(zip_path) / (1024 * 1024)
            self._log(f"  Zip saved ({zip_size:.1f} MB)")
        except Exception as e:
            self._log(f"  ERROR creating zip: {e}")
            return

        # Clean up staging
        try:
            shutil.rmtree(staging_dir)
            self._log("  Cleaned up staging directory")
        except Exception:
            pass

        self._log("")
        self._log(f"Done! Mod package ready:")
        self._log(f"  {zip_path}")


# ---------------------------------------------------------------------------
# Entry point
# ---------------------------------------------------------------------------

def main():
    root = tk.Tk()
    app = BubbleDataRemoverApp(root)
    root.mainloop()


if __name__ == '__main__':
    main()
