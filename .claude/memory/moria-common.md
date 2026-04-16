# moria_common.inl — Centralized Utilities

**File**: `<workspace>/cpp-mod/MyCPPMods/MoriaCppMod/src/moria_common.inl`
**Included**: Inside the main mod class body, before other .inl files.

## Functions Available for Reuse

### ScreenCoords (struct)
- `m_screen.refresh(playerController)` — caches viewW/viewH/uiScale from GetViewportSize
- `m_screen.getCursorFraction(fx, fy)` — Win32 cursor as 0.0-1.0 viewport fraction
- `m_screen.getCursorClientPixels(x, y, w, h)` — raw pixel cursor + client dimensions
- `m_screen.fracToPixelX/Y(frac)` — fraction to raw pixels
- `m_screen.pixelToFracX/Y(px)` — raw pixels to fraction
- `m_screen.pixelToSlateX/Y(px)` — raw pixels to slate units (/ dpiScale)
- Fields: viewW, viewH, dpiScale, uiScale (viewH/2160, min 0.5)

### Object Introspection
- `safeClassName(UObject* obj)` — returns class name as std::wstring, empty if null
- `isWidgetAlive(UObject* obj)` — GC-safe: not null, not pending destroy, not unreachable

### Player & World Lookup
- `findPlayerController()` — FindAllOf("PlayerController"), returns first
- `getPawn()` — K2_GetPawn via ProcessEvent
- `getPawnLocation()` — K2_GetActorLocation via ProcessEvent, returns FVec3f

### Widget Visibility
- `setWidgetVisibility(UObject* widget, uint8_t vis)` — SetVisibility via ProcessEvent
  - 0=Visible, 1=Collapsed, 2=Hidden

### Panel Child Management
- `addChildToPanel(UObject* parent, const wchar_t* fnName, UObject* child)` — generic AddChild via named UFunction, returns slot UObject*
- `addToVBox(parent, child)` — AddChildToVerticalBox wrapper
- `addToHBox(parent, child)` — AddChildToHorizontalBox wrapper
- `addToOverlay(parent, child)` — AddChildToOverlay wrapper

### Widget Discovery
- `findWidgetByClass(const wchar_t* className, bool requireVisible = false)` — finds first UserWidget matching class name

## C++ Include Order Note
All .inl files are #included inside a single class body. C++ defers name lookup in inline member function bodies until the class is complete, so **include order does not affect cross-file visibility** of member functions.
