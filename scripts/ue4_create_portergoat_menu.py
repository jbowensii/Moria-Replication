"""UE4 Editor Python script — author WBP_PorterGoatMenu from scratch.

Creates:
  /Game/Mods/PorterGoat/UI/WBP_PorterGoatMenu

Layout:
  CanvasPanel (root)
    Overlay (centered, anchored center)
      Image (BG_Dark, dark translucent fill)
      VerticalBox
        TextBlock "NameHeader"            <- UE4SS SetText("Porter Goat")
        Spacer
        Button "Btn_Follow"      + TextBlock
        Button "Btn_Stay"        + TextBlock
        Button "Btn_Wander"      + TextBlock
        Button "Btn_Saddlebags"  + TextBlock
        Button "Btn_Feed"        + TextBlock
        Button "Btn_Rename"      + TextBlock
        Button "Btn_Manage"      + TextBlock
        Button "Btn_Dismiss"     + TextBlock

Each button is named for UE4SS reflection lookup via
GetWidgetFromName(). The user wires Button.OnClicked -> Custom Event
in the editor manually (one of two click types per button: Pressed
or Released; UMG event-graph wiring is not reachable from Python
in UE4.27 in any robust way).

Run via:
    UE4Editor-Cmd.exe project/Moria.uproject \
      -ExecutePythonScript=scripts/ue4_create_portergoat_menu.py \
      -nullrhi -unattended -nopause -nosplash
"""
import unreal
import os
import json

ASSET_NAME    = "WBP_PorterGoatMenu"
ASSET_DIR     = "/Game/Mods/PorterGoat/UI"
ASSET_FULL    = ASSET_DIR + "/" + ASSET_NAME

LOG_PATH = r"C:\Users\johnb\OneDrive\Documents\Projects\Moria-Replication\tools\portergoat-menu-create-results.json"

BUTTONS = [
    ("Btn_Follow",     "Follow"),
    ("Btn_Stay",       "Stay"),
    ("Btn_Wander",     "Wander"),
    ("Btn_Saddlebags", "Access Saddlebags"),
    ("Btn_Feed",       "Feed"),
    ("Btn_Rename",     "Rename"),
    ("Btn_Manage",     "Manage"),
    ("Btn_Dismiss",    "Dismiss"),
]


def run():
    results = {"created": None, "widgets_added": [], "errors": []}

    # Ensure dest directory exists
    if not unreal.EditorAssetLibrary.does_directory_exist(ASSET_DIR):
        unreal.EditorAssetLibrary.make_directory(ASSET_DIR)
        unreal.log("Created directory: " + ASSET_DIR)

    # Delete existing if present (idempotent rerun)
    if unreal.EditorAssetLibrary.does_asset_exist(ASSET_FULL):
        unreal.EditorAssetLibrary.delete_asset(ASSET_FULL)
        unreal.log("Deleted existing: " + ASSET_FULL)

    # Create the Widget Blueprint asset
    asset_tools = unreal.AssetToolsHelpers.get_asset_tools()
    factory = unreal.WidgetBlueprintFactory()
    factory.set_editor_property("parent_class", unreal.UserWidget)
    wbp = asset_tools.create_asset(ASSET_NAME, ASSET_DIR, None, factory)
    if wbp is None:
        results["errors"].append("create_asset returned None")
        _save(results)
        return
    results["created"] = ASSET_FULL
    unreal.log("Created WBP: " + ASSET_FULL)

    # Access the widget tree -- UE4.27 Python doesn't expose `widget_tree` as
    # a Pythonic attribute. Try several known patterns.
    wt = None
    last_err = None
    for accessor in ("WidgetTree", "widget_tree"):
        try:
            wt = wbp.get_editor_property(accessor)
            if wt:
                results["widget_tree_accessor"] = "get_editor_property('" + accessor + "')"
                break
        except Exception as e:
            last_err = str(e)
    if wt is None:
        # Try compiling first
        try:
            unreal.BlueprintEditorLibrary.compile_blueprint(wbp)
            wt = wbp.get_editor_property("WidgetTree")
            results["widget_tree_accessor"] = "post-compile WidgetTree"
        except Exception as e:
            last_err = str(e)
    if wt is None:
        # Last resort: list all editor properties + attrs
        try:
            attrs = [a for a in dir(wbp) if not a.startswith('_')]
            results["wbp_attrs"] = attrs
        except Exception:
            pass
        results["errors"].append("widget_tree unreachable; last_err=" + str(last_err))
        _save(results)
        return

    # Build the layout via widget_tree.construct_widget API
    # Root: CanvasPanel
    try:
        canvas = wt.construct_widget(unreal.CanvasPanel, "RootCanvas")
        wt.set_editor_property("root_widget", canvas)
        results["widgets_added"].append("RootCanvas")
    except Exception as e:
        results["errors"].append("CanvasPanel construct: " + str(e))
        _save(results)
        return

    # Overlay (centered container)
    overlay = wt.construct_widget(unreal.Overlay, "CenteredOverlay")
    canvas_slot = canvas.add_child_to_canvas(overlay)
    # Center anchors
    canvas_slot.set_anchors(unreal.Anchors(0.5, 0.5, 0.5, 0.5))
    canvas_slot.set_alignment(unreal.Vector2D(0.5, 0.5))
    canvas_slot.set_size(unreal.Vector2D(420.0, 520.0))
    canvas_slot.set_position(unreal.Vector2D(0.0, 0.0))
    results["widgets_added"].append("CenteredOverlay")

    # BG_Dark (Image background)
    bg = wt.construct_widget(unreal.Image, "BG_Dark")
    bg.set_editor_property("color_and_opacity",
                           unreal.LinearColor(0.05, 0.05, 0.08, 0.85))
    overlay.add_child_to_overlay(bg)
    results["widgets_added"].append("BG_Dark")

    # VerticalBox (button stack)
    vbox = wt.construct_widget(unreal.VerticalBox, "MainVBox")
    vbox_slot = overlay.add_child_to_overlay(vbox)
    vbox_slot.set_padding(unreal.Margin(20.0, 20.0, 20.0, 20.0))
    vbox_slot.set_horizontal_alignment(unreal.HorizontalAlignment.H_ALIGN_FILL)
    vbox_slot.set_vertical_alignment(unreal.VerticalAlignment.V_ALIGN_FILL)
    results["widgets_added"].append("MainVBox")

    # NameHeader TextBlock
    header = wt.construct_widget(unreal.TextBlock, "NameHeader")
    header.set_text(unreal.Text("Porter Goat"))
    header.set_editor_property("color_and_opacity",
        unreal.SlateColor(unreal.LinearColor(1.0, 0.95, 0.85, 1.0)))
    header_slot = vbox.add_child_to_vertical_box(header)
    header_slot.set_padding(unreal.Margin(0.0, 0.0, 0.0, 8.0))
    header_slot.set_horizontal_alignment(unreal.HorizontalAlignment.H_ALIGN_CENTER)
    results["widgets_added"].append("NameHeader")

    # Buttons
    for btn_name, label_text in BUTTONS:
        btn = wt.construct_widget(unreal.Button, btn_name)
        # Inner TextBlock for the button label
        txt = wt.construct_widget(unreal.TextBlock, btn_name + "_Text")
        txt.set_text(unreal.Text(label_text))
        txt.set_editor_property("color_and_opacity",
            unreal.SlateColor(unreal.LinearColor(0.95, 0.92, 0.88, 1.0)))
        btn.add_child(txt)
        btn_slot = vbox.add_child_to_vertical_box(btn)
        btn_slot.set_padding(unreal.Margin(0.0, 4.0, 0.0, 4.0))
        btn_slot.set_horizontal_alignment(unreal.HorizontalAlignment.H_ALIGN_FILL)
        results["widgets_added"].append(btn_name)

    # Compile + save
    try:
        unreal.EditorAssetLibrary.save_asset(ASSET_FULL)
        results["saved"] = True
    except Exception as e:
        results["errors"].append("save_asset: " + str(e))

    _save(results)
    unreal.log("WBP_PorterGoatMenu construction complete.")
    unreal.log("Results written to: " + LOG_PATH)


def _save(results):
    with open(LOG_PATH, "w") as f:
        json.dump(results, f, indent=2)


run()
