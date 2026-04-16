---
name: installer-drive-handling
description: Inno Setup installer supports any drive via dynamic DefaultDirName — runtime code is fully relative via modPath()
type: project
originSessionId: faf77fec-764b-499b-8ea8-e24075baf1b0
---
## Installer path handling (v6.3.9+)

**DefaultDirName** in `KhazadDumAdvancedBuilderPack.iss` uses `{code:GetDefaultDir}`
— a Pascal function that dynamically resolves to the first valid game install
at setup startup (Epic → Steam → Epic-placeholder fallback). This avoids the
hardcoded C: path that broke non-C: drive installs prior to v6.3.9.

**Why the fix was needed**: Inno Setup initializes `{app}` from `DefaultDirName`
BEFORE any wizard pages run. Even though the custom PathPage overrides
`WizardForm.DirEdit.Text` in `NextButtonClick`, hardcoded C: caused internal
state problems for users installing on D:/E:/etc.

**Steam/Epic validation pattern**: Both radio buttons call `IsValidGameRoot(Root)`
at init. If false:
- Radio label gets `[not detected]` appended
- Radio is `Enabled := False` (user cannot select it)
- Auto-select falls through to Custom

**Custom path**: accepts any drive (edit field + browse button). Validated on
every change via `UpdatePathStatus` → `IsValidGameRoot(edtPath.Text)`.
`NextButtonClick` re-validates and blocks Next with error dialog if invalid.

## Runtime code — all paths relative

The C++ mod has ZERO hardcoded drive references. All file I/O uses `modPath()`:

```cpp
inline std::string modPath(const char* relativePath) {
    return s_ue4ssWorkDir + relativePath;
}
```

`s_ue4ssWorkDir` is resolved at `on_unreal_init()` in dllmain.cpp from
`UE4SSProgram::get_program().get_working_directory()` — whatever drive UE4SS
reports becomes the base.

All file helpers use modPath: `iniPath()`, `oldKeybindPath()`, `gameModsIniPath()`,
`definitionsDir()`, `m_saveFilePath`, etc.

**Audit verified (2026-04-14)**: No INI, txt, json, def, or Lua file contains
hardcoded drive paths. Server Lua mods (CheatManagerEnabler, ConsoleEnabler)
are drive-agnostic. README_SERVER.txt has a `C:\ReturnToMoria` example for
documentation but it's not executed.

## Constants still hardcoded (by design)

The Pascal constants `STEAM_ROOT` and `EPIC_ROOT` point to the default install
locations of each distribution platform, which ARE on C: drive. This is correct
— they're only used as a shortcut for users who haven't moved their library.
If either isn't present, `IsValidGameRoot` disables the radio and Custom takes over.

```pascal
STEAM_ROOT = 'C:\Program Files (x86)\Steam\steamapps\common\The Lord of the Rings Return to Moria'#$2122;
EPIC_ROOT  = 'C:\Program Files\Epic Games\ReturnToMoria';
```
