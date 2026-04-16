---
name: controller-ui-removal
description: v6.3.5 removed F12 Controller checkbox and Xbox/PS5 profile selector — controller input permanently disabled
type: project
originSessionId: faf77fec-764b-499b-8ea8-e24075baf1b0
---
## What was removed (v6.3.5)
- F12 > Game Options: Controller enable checkbox + Xbox/PS5 profile toggle
- Click handlers for both (ctY0 row in dllmain.cpp)
- INI save/load of `Controller=` and `ControllerProfile=` in moria_quickbuild.inl

## What remains
- `m_controllerEnabled` field — defaults false, nothing can flip it
- Underlying gamepad/DualSense code compiled in but permanently gated off
- `moria_dualsense.h`, XInput/DirectInput readers still linked
- All guarded paths (`if (m_controllerEnabled ...)` at lines 718, 1683) are dead code

## Why
Controller support was experimental and not ready for release.
Removing the UI prevents users from enabling it accidentally.
