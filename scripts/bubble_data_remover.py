#!/usr/bin/env python3
"""
Bubble Data Object Remover
Removes specific objects or entire object types from a BubbleData JSON file
based on a removal specification file.

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
from datetime import datetime

# Paths relative to project root
SCRIPT_DIR = Path(__file__).resolve().parent
PROJECT_ROOT = SCRIPT_DIR.parent
INI_PATH = SCRIPT_DIR / 'bubble_data_remover.ini'
MODIFIED_BUBBLES_DIR = PROJECT_ROOT / 'Modified_Bubbles'
LEGACY_ASSETS_DIR = PROJECT_ROOT / 'tools' / 'legacy-assets'
RETOC_EXE = PROJECT_ROOT / 'tools' / 'retoc' / 'bin' / 'retoc.exe'
DOWNLOADS_DIR = Path(os.path.expanduser('~/Downloads'))

COORD_EPSILON = 0.5  # coordinate matching tolerance in UE units


# ---------------------------------------------------------------------------
# Parsing helpers
# ---------------------------------------------------------------------------

def extract_mesh_name(mesh_string):
    """Extract mesh name from 'MeshName-Material-Collision-flags' format."""
    return mesh_string.split('-')[0]


def mesh_name_from_object_name(obj_name):
    """Extract mesh name from UE ObjectName like StaticMesh'MeshName'."""
    if "'" in obj_name:
        return obj_name.split("'")[1]
    return obj_name


def mesh_name_from_asset_path(asset_path):
    """Extract class name from asset path like /Game/.../BP_Name.BP_Name_C."""
    return asset_path.split('/')[-1].split('.')[0]


def coords_match(x1, y1, z1, x2, y2, z2, epsilon=COORD_EPSILON):
    """Check if two 3D coordinates are within epsilon on each axis."""
    return (abs(x1 - x2) < epsilon and
            abs(y1 - y2) < epsilon and
            abs(z1 - z2) < epsilon)


def get_translation(transform):
    """Extract (x, y, z) from a Transform dict."""
    t = transform.get('Translation', {})
    return t.get('X', 0.0), t.get('Y', 0.0), t.get('Z', 0.0)


# ---------------------------------------------------------------------------
# Removal spec parser
# ---------------------------------------------------------------------------

def parse_removal_file(filepath):
    """Parse the removal specification file.

    Returns:
        type_rules:      list of {'mesh_name': str, 'bubble': str|None, 'raw': str}
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
                    # mesh entry without coordinates — treat as type rule
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
# Mesh matching helpers
# ---------------------------------------------------------------------------

def instanced_mesh_matches(batch_definition, mesh_name):
    """Check if an InstancedMeshCatalog batch matches a mesh name."""
    obj_name = batch_definition.get('Mesh', {}).get('ObjectName', '')
    batch_mesh = mesh_name_from_object_name(obj_name)
    return batch_mesh == mesh_name


def breakable_matches(batch_definition, mesh_name):
    """Check if an InstancedBreakableCatalog batch matches a mesh name.

    Breakable classes are named like BP_<MeshName>_Breakable, so we check
    if the mesh name is contained within the class name.
    """
    asset_path = batch_definition.get('BreakableClass', {}).get('AssetPathName', '')
    class_name = mesh_name_from_asset_path(asset_path)
    # Direct substring match: 'Ruin_Column_Medium_A_2_Shaft' in
    # 'BP_Ruin_Column_Medium_A_2_Shaft_Breakable'
    return mesh_name in class_name


def construction_name_matches(block_name, mesh_name):
    """Check if a ConstructionCatalog block name matches a mesh name.

    Block names have instance suffixes like 'AB_Mines_Scaffolding_Broken_Segment_A_4'.
    We check if the mesh name is a prefix/substring of the block name.
    """
    return mesh_name in block_name


# ---------------------------------------------------------------------------
# Removal engine
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


def apply_removals(bubble_data, type_rules, position_entries, log_fn=None):
    """Apply removal operations to the bubble data (mutates in place).

    Args:
        bubble_data: The parsed BubbleData JSON (the Properties dict).
        type_rules: List of type rule dicts (remove all of mesh type).
        position_entries: List of position entry dicts (remove specific objects).
        log_fn: Optional callable for logging messages.

    Returns:
        RemovalStats with counts of removed items.
    """
    if log_fn is None:
        log_fn = lambda msg: None

    stats = RemovalStats()

    # --- InstancedMeshCatalog ---
    imc = bubble_data.get('InstancedMeshCatalog', {})
    batches = imc.get('Batches', [])
    new_batches = []

    for batch in batches:
        defn = batch.get('Definition', {})
        obj_name = defn.get('Mesh', {}).get('ObjectName', '')
        batch_mesh = mesh_name_from_object_name(obj_name)
        instances = batch.get('Instances', [])

        # Check type rules — remove entire batch if mesh matches
        type_match = any(tr['mesh_name'] == batch_mesh for tr in type_rules)
        if type_match:
            count = len(instances)
            stats.instanced_mesh += count
            log_fn(f"  [TypeRule] Removed {count}x {batch_mesh} (InstancedMesh)")
            continue  # skip this batch entirely

        # Check position entries — remove specific instances
        surviving_instances = []
        for inst in instances:
            transform = inst.get('Transform', {})
            ix, iy, iz = get_translation(transform)

            removed = False
            for pe in position_entries:
                if pe['mesh_name'] == batch_mesh:
                    px, py, pz = pe['local']
                    if coords_match(ix, iy, iz, px, py, pz):
                        stats.instanced_mesh += 1
                        name = inst.get('Name', '?')
                        log_fn(f"  [Position] Removed {name} at "
                               f"({ix:.1f}, {iy:.1f}, {iz:.1f}) (InstancedMesh)")
                        removed = True
                        break
            if not removed:
                surviving_instances.append(inst)

        if surviving_instances:
            batch['Instances'] = surviving_instances
            new_batches.append(batch)
        elif instances:
            # All instances removed
            log_fn(f"  [Cleanup] Dropped empty batch for {batch_mesh}")

    imc['Batches'] = new_batches

    # --- InstancedBreakableCatalog ---
    ibc = bubble_data.get('InstancedBreakableCatalog', {})
    b_batches = ibc.get('Batches', [])
    new_b_batches = []

    for batch in b_batches:
        defn = batch.get('Definition', {})
        asset_path = defn.get('BreakableClass', {}).get('AssetPathName', '')
        class_name = mesh_name_from_asset_path(asset_path)
        instances = batch.get('Instances', [])

        # Check type rules
        type_match = any(tr['mesh_name'] in class_name for tr in type_rules)
        if type_match:
            count = len(instances)
            stats.instanced_breakable += count
            log_fn(f"  [TypeRule] Removed {count}x {class_name} (Breakable)")
            continue

        # Check position entries
        surviving_instances = []
        for inst in instances:
            transform = inst.get('Transform', {})
            ix, iy, iz = get_translation(transform)

            removed = False
            for pe in position_entries:
                if pe['mesh_name'] in class_name:
                    px, py, pz = pe['local']
                    if coords_match(ix, iy, iz, px, py, pz):
                        stats.instanced_breakable += 1
                        name = inst.get('Name', class_name)
                        log_fn(f"  [Position] Removed {name} at "
                               f"({ix:.1f}, {iy:.1f}, {iz:.1f}) (Breakable)")
                        removed = True
                        break
            if not removed:
                surviving_instances.append(inst)

        if surviving_instances:
            batch['Instances'] = surviving_instances
            new_b_batches.append(batch)
        elif instances:
            log_fn(f"  [Cleanup] Dropped empty batch for {class_name}")

    ibc['Batches'] = new_b_batches

    # --- ConstructionCatalog + DecoVolumes + BreakableAttachmentDefinition ---
    cc = bubble_data.get('ConstructionCatalog', {})
    blocks = cc.get('Blocks', [])
    dv = bubble_data.get('DecoVolumes', {})
    volumes = dv.get('Volumes', [])
    bad = bubble_data.get('BreakableAttachmentDefinition', {})
    attachments = bad.get('Attachments', [])

    # Build DecoVolume lookup by name for coordinate matching
    dv_by_name = {}
    for vol in volumes:
        dv_by_name[vol['Name']] = vol

    # Determine which block names to remove
    blocks_to_remove = set()

    for block in blocks:
        block_name = block.get('Name', '')

        # Type rules — check if any mesh name matches the block name
        for tr in type_rules:
            if construction_name_matches(block_name, tr['mesh_name']):
                blocks_to_remove.add(block_name)
                log_fn(f"  [TypeRule] Marked construction block {block_name} for removal")
                break

        # Position entries — match via DecoVolume coordinates
        if block_name not in blocks_to_remove and block_name in dv_by_name:
            vol = dv_by_name[block_name]
            transform = vol.get('Volume', {}).get('BaseTransform', {})
            vx, vy, vz = get_translation(transform)

            for pe in position_entries:
                if construction_name_matches(block_name, pe['mesh_name']):
                    px, py, pz = pe['local']
                    if coords_match(vx, vy, vz, px, py, pz):
                        blocks_to_remove.add(block_name)
                        log_fn(f"  [Position] Marked construction block {block_name} "
                               f"at ({vx:.1f}, {vy:.1f}, {vz:.1f}) for removal")
                        break

    # Remove blocks
    new_blocks = [b for b in blocks if b.get('Name', '') not in blocks_to_remove]
    removed_blocks = len(blocks) - len(new_blocks)
    stats.construction += removed_blocks
    cc['Blocks'] = new_blocks

    # Remove matching DecoVolumes
    new_volumes = [v for v in volumes if v.get('Name', '') not in blocks_to_remove]
    removed_vols = len(volumes) - len(new_volumes)
    stats.deco_volume += removed_vols
    dv['Volumes'] = new_volumes
    if removed_vols:
        log_fn(f"  [Cleanup] Removed {removed_vols} DecoVolumes for removed blocks")

    # Remove matching BreakableAttachmentDefinition entries
    new_attachments = [a for a in attachments
                       if a.get('Key', '') not in blocks_to_remove]
    removed_att = len(attachments) - len(new_attachments)
    stats.attachment += removed_att
    bad['Attachments'] = new_attachments
    if removed_att:
        log_fn(f"  [Cleanup] Removed {removed_att} BreakableAttachmentDefinition entries")

    return stats


# ---------------------------------------------------------------------------
# Tkinter UI
# ---------------------------------------------------------------------------

class BubbleDataRemoverApp:
    def __init__(self, root):
        self.root = root
        root.title("Bubble Data Object Remover")
        root.geometry("900x650")
        root.resizable(True, True)

        # State
        self.bubble_data_path = tk.StringVar()
        self.removal_spec_path = tk.StringVar()
        self.selected_bubble = tk.StringVar()
        self.bubble_names = []
        self.last_output_dir = None   # set after successful Process
        self.last_bd_name = None      # e.g. 'BD_BB_Chapter2_GameStart'
        self.last_bubble_name = None  # e.g. 'Aftermath'

        self._build_ui()
        self._load_settings()

        # Auto-populate bubble dropdown when removal spec path changes
        self.removal_spec_path.trace_add('write', self._on_spec_path_changed)

    def _build_ui(self):
        # --- File selection frame ---
        file_frame = ttk.LabelFrame(self.root, text="Input Files", padding=10)
        file_frame.pack(fill='x', padx=10, pady=(10, 5))

        # BubbleData file
        ttk.Label(file_frame, text="Bubble Data JSON (BD_):").grid(
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
            # Re-populate bubble dropdown from saved spec file
            if os.path.isfile(sp):
                self._load_bubble_names(sp)
        if bubble:
            self.selected_bubble.set(bubble)

    def _save_settings(self):
        """Save current paths and bubble name to INI file."""
        cfg = configparser.ConfigParser()
        cfg['settings'] = {
            'bubble_data_path': self.bubble_data_path.get(),
            'removal_spec_path': self.removal_spec_path.get(),
            'selected_bubble': self.selected_bubble.get(),
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
        """Callback when removal spec path changes — re-populate bubble dropdown."""
        path = self.removal_spec_path.get()
        if path and os.path.isfile(path):
            self._load_bubble_names(path)

    def _browse_bubble_data(self):
        path = filedialog.askopenfilename(
            title="Select BubbleData JSON file",
            filetypes=[("All files", "*.*"), ("JSON files", "*.json"),
                       ("Text files", "*.txt")])
        if path:
            self.bubble_data_path.set(path)

    def _browse_removal_spec(self):
        path = filedialog.askopenfilename(
            title="Select Removal Spec file",
            filetypes=[("All files", "*.*"), ("JSON files", "*.json"),
                       ("Text files", "*.txt")])
        if path:
            self.removal_spec_path.set(path)
            self._load_bubble_names(path)

    def _load_bubble_names(self, spec_path):
        """Parse removal spec and populate bubble name dropdown."""
        try:
            type_rules, position_entries = parse_removal_file(spec_path)
            names = get_bubble_names(type_rules, position_entries)

            if names:
                self.bubble_names = names
                self.bubble_combo['values'] = names
                self.selected_bubble.set(names[0])
                self._log(f"Found bubble names: {', '.join(names)}")
            else:
                # No bubble names — type rules apply to any bubble
                self.bubble_names = ['(all)']
                self.bubble_combo['values'] = ['(all)']
                self.selected_bubble.set('(all)')
                self._log("No bubble names in spec — rules apply to all bubbles")

            self._log(f"Loaded {len(type_rules)} type rules, "
                      f"{len(position_entries)} position entries")
        except Exception as e:
            self._log(f"ERROR loading removal spec: {e}")

    def _package(self):
        """Package the modified BubbleData as an IoStore mod pak."""
        if not self.last_output_dir or not self.last_bd_name:
            messagebox.showerror("Error",
                "No processed data to package.\n\n"
                "Run 'Process Removals' first, then package.")
            return

        bd_name = self.last_bd_name
        bubble_name = self.last_bubble_name or bd_name
        pak_name = f"Bubble_{bubble_name}_P"

        self._log("")
        self._log(f"{'=' * 60}")
        self._log(f"Packaging IoStore Mod: {pak_name}")
        self._log(f"{'=' * 60}")

        # Verify retoc exists
        if not RETOC_EXE.exists():
            self._log(f"ERROR: retoc not found at {RETOC_EXE}")
            messagebox.showerror("Error",
                f"retoc.exe not found at:\n{RETOC_EXE}\n\n"
                "Install retoc to tools/retoc/bin/retoc.exe")
            return

        # Locate legacy .uasset/.uexp
        legacy_subpath = Path('Moria/Content/Tech/Data/Bubbles/GameWorldCatalog')
        legacy_dir = LEGACY_ASSETS_DIR / legacy_subpath
        uasset_path = legacy_dir / f"{bd_name}.uasset"
        uexp_path = legacy_dir / f"{bd_name}.uexp"

        if not uasset_path.exists():
            self._log(f"ERROR: Legacy .uasset not found: {uasset_path}")
            messagebox.showerror("Error",
                f"Legacy asset not found:\n{uasset_path}\n\n"
                "Run retoc to convert IoStore assets first.")
            return

        self._log(f"Legacy .uasset: {uasset_path}")
        self._log(f"Legacy .uexp:   {uexp_path}")

        # Create staging directory with UE4 content path structure
        staging_dir = self.last_output_dir / 'staging'
        staging_content = staging_dir / legacy_subpath
        staging_content.mkdir(parents=True, exist_ok=True)

        # Copy legacy assets to staging
        self._log("Staging legacy assets...")
        try:
            shutil.copy2(uasset_path, staging_content / uasset_path.name)
            if uexp_path.exists():
                shutil.copy2(uexp_path, staging_content / uexp_path.name)
            # Also copy .ubulk if it exists
            ubulk_path = legacy_dir / f"{bd_name}.ubulk"
            if ubulk_path.exists():
                shutil.copy2(ubulk_path, staging_content / ubulk_path.name)
                self._log(f"  Copied .ubulk")
        except Exception as e:
            self._log(f"ERROR copying legacy assets: {e}")
            return

        self._log("  Staged .uasset and .uexp")

        # Run retoc to-zen to create IoStore pak
        output_utoc = self.last_output_dir / f"{pak_name}.utoc"
        cmd = [
            str(RETOC_EXE),
            '--override-container-header-version', 'PreInitial',
            'to-zen', '-v',
            '--version', 'UE4_27',
            str(staging_dir),
            str(output_utoc),
        ]

        self._log(f"Running retoc...")
        self._log(f"  Command: {' '.join(cmd)}")
        self._log("")

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
                self._log(f"ERROR: retoc exited with code {result.returncode}")
                return
        except subprocess.TimeoutExpired:
            self._log("ERROR: retoc timed out after 120 seconds")
            return
        except Exception as e:
            self._log(f"ERROR running retoc: {e}")
            return

        # Verify output files exist
        pak_path = self.last_output_dir / f"{pak_name}.pak"
        ucas_path = self.last_output_dir / f"{pak_name}.ucas"
        utoc_path = output_utoc

        if not pak_path.exists() or not ucas_path.exists() or not utoc_path.exists():
            self._log("ERROR: Expected IoStore output files not found:")
            self._log(f"  .pak:  {pak_path} {'OK' if pak_path.exists() else 'MISSING'}")
            self._log(f"  .ucas: {ucas_path} {'OK' if ucas_path.exists() else 'MISSING'}")
            self._log(f"  .utoc: {utoc_path} {'OK' if utoc_path.exists() else 'MISSING'}")
            return

        self._log("")
        self._log("IoStore files created:")
        self._log(f"  {pak_path.name}")
        self._log(f"  {ucas_path.name}")
        self._log(f"  {utoc_path.name}")

        # Zip the 3 IoStore files to Downloads
        zip_name = f"{pak_name}.zip"
        zip_path = DOWNLOADS_DIR / zip_name

        self._log(f"Creating zip: {zip_path}")
        try:
            with zipfile.ZipFile(zip_path, 'w', zipfile.ZIP_DEFLATED) as zf:
                zf.write(pak_path, pak_path.name)
                zf.write(ucas_path, ucas_path.name)
                zf.write(utoc_path, utoc_path.name)
            zip_size = os.path.getsize(zip_path) / (1024 * 1024)
            self._log(f"Zip saved ({zip_size:.1f} MB)")
        except Exception as e:
            self._log(f"ERROR creating zip: {e}")
            return

        # Clean up staging directory
        try:
            shutil.rmtree(staging_dir)
            self._log("Cleaned up staging directory")
        except Exception:
            pass

        self._log("")
        self._log(f"Done! Mod package ready at:")
        self._log(f"  {zip_path}")
        self._log("")
        self._log("NOTE: This pak contains the ORIGINAL (unmodified) binary data.")
        self._log("Modified JSON is saved alongside for reference.")
        self._log("Binary modification support is a future enhancement.")

    def _process(self):
        """Main processing: load files, apply removals, save result."""
        bd_path = self.bubble_data_path.get()
        spec_path = self.removal_spec_path.get()
        bubble_name = self.selected_bubble.get()

        if not bd_path or not os.path.isfile(bd_path):
            messagebox.showerror("Error",
                "Please select a valid Game Bubble JSON file.\n\n"
                "This should be a BD_*.json file from:\n"
                "tools/cloud-exports/Tech/Data/Bubbles/GameWorldCatalog/")
            return
        if not spec_path or not os.path.isfile(spec_path):
            messagebox.showerror("Error",
                "Please select a valid Removed Instances file.\n\n"
                "This is the removed_instances.txt from your mod.")
            return

        # Detect swapped files — check if BubbleData path looks like a removal spec
        try:
            with open(bd_path, 'r', encoding='utf-8') as f:
                first_line = f.readline().strip()
            if first_line.startswith('#') or '"typeRule"' in first_line:
                messagebox.showerror("Files Swapped?",
                    "The Game Bubble JSON file looks like a removal spec "
                    "(starts with # comments or typeRule entries).\n\n"
                    "Swap the files:\n"
                    "- Game Bubble JSON = BD_*.json (from cloud-exports)\n"
                    "- Removed Instances = removed_instances.txt (from your mod)")
                return
        except Exception:
            pass

        # Detect BF_ (BubbleDef) instead of BD_ (BubbleData)
        bd_basename = os.path.basename(bd_path)
        if bd_basename.startswith('BF_'):
            messagebox.showerror("Wrong File Type",
                f"You selected a BubbleDef file (BF_):\n{bd_basename}\n\n"
                "You need the BubbleData file (BD_) instead.\n\n"
                "Look in:\n"
                "tools/cloud-exports/Tech/Data/Bubbles/GameWorldCatalog/\n"
                f"for: BD_{bd_basename[3:]}")
            return

        # Ensure bubble dropdown is populated
        if not self.bubble_names or self.bubble_names == ['(all)']:
            self._load_bubble_names(spec_path)

        self._clear_log()
        self._log(f"{'=' * 60}")
        self._log(f"Bubble Data Object Remover")
        self._log(f"{'=' * 60}")
        self._log(f"BubbleData: {bd_path}")
        self._log(f"Removal Spec: {spec_path}")
        self._log(f"Bubble Filter: {bubble_name}")
        self._log("")

        # --- Load BubbleData ---
        self._log("Loading BubbleData...")
        try:
            with open(bd_path, 'r', encoding='utf-8') as f:
                raw_data = json.load(f)
        except Exception as e:
            self._log(f"ERROR loading BubbleData: {e}")
            return

        # BubbleData is a list with one object; work on the Properties dict
        if isinstance(raw_data, list) and len(raw_data) > 0:
            bd_obj = raw_data[0]
            props = bd_obj.get('Properties', {})
        else:
            self._log("ERROR: Unexpected BubbleData format (expected JSON array)")
            return

        bd_name = bd_obj.get('Name', 'unknown')
        self._log(f"Loaded: {bd_name}")

        # Count originals
        orig_im = sum(len(b.get('Instances', []))
                      for b in props.get('InstancedMeshCatalog', {}).get('Batches', []))
        orig_ib = sum(len(b.get('Instances', []))
                      for b in props.get('InstancedBreakableCatalog', {}).get('Batches', []))
        orig_cc = len(props.get('ConstructionCatalog', {}).get('Blocks', []))
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

        self._log(f"  Type rules to apply:     {len(type_rules_filtered)}")
        self._log(f"  Position entries to apply:{len(position_entries)}")
        self._log("")

        if not type_rules_filtered and not position_entries:
            self._log("Nothing to remove! Check bubble name filter.")
            return

        # --- Apply removals ---
        self._log("Applying removals...")
        self._log("-" * 40)

        # Deep copy so we can report before/after
        working_data = copy.deepcopy(raw_data)
        working_props = working_data[0]['Properties']

        stats = apply_removals(
            working_props, type_rules_filtered, position_entries,
            log_fn=self._log)

        self._log("-" * 40)
        self._log("")

        # Count remaining
        rem_im = sum(len(b.get('Instances', []))
                     for b in working_props.get('InstancedMeshCatalog', {}).get('Batches', []))
        rem_ib = sum(len(b.get('Instances', []))
                     for b in working_props.get('InstancedBreakableCatalog', {}).get('Batches', []))
        rem_cc = len(working_props.get('ConstructionCatalog', {}).get('Blocks', []))
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

        # --- Save result to Modified_Bubbles/<bd_name>/ ---
        out_dir = MODIFIED_BUBBLES_DIR / bd_name
        out_dir.mkdir(parents=True, exist_ok=True)
        out_name = f"{bd_name}_modified.json"
        out_path = out_dir / out_name

        self._log(f"Saving to: {out_path}")
        try:
            with open(out_path, 'w', encoding='utf-8') as f:
                json.dump(working_data, f, indent=2, ensure_ascii=False)
            size_mb = os.path.getsize(out_path) / (1024 * 1024)
            self._log(f"Saved successfully ({size_mb:.1f} MB)")
        except Exception as e:
            self._log(f"ERROR saving: {e}")
            return

        # Store state for packaging
        self.last_output_dir = out_dir
        self.last_bd_name = bd_name
        self.last_bubble_name = bubble_name if bubble_name != '(all)' else bd_name

        self._log("")
        self._log("Done! Use 'Package as IoStore Mod' to create a mod pak.")

        # Save settings for next run
        self._save_settings()


# ---------------------------------------------------------------------------
# Entry point
# ---------------------------------------------------------------------------

def main():
    root = tk.Tk()
    app = BubbleDataRemoverApp(root)
    root.mainloop()


if __name__ == '__main__':
    main()
