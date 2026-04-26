# Editor dialog regression — forensic analysis

Source of truth: `C:/Users/johnb/OneDrive/Documents/Projects/Moria-Replication/scripts/SandboxZoneEditor.py`
(file is **untracked in git** — no version-control bisect available; analysis is by code reading.)

---

## 1. Code chunks vs. the known-working state

### 1a. `_show_validation_dialog` — REVERTED CORRECTLY
File:6515-6577. Uses `messagebox.askyesnocancel` / `askyesno` exactly as the original. No Toplevel, no `withdraw`/`deiconify`, no orphan `update_idletasks()`. **Matches the working baseline.**

### 1b. `_show_manifest_dialog` — REVERTED CORRECTLY (visible in code)
File:6804-6890. The dialog uses the original early-grab pattern:

```py
6808  dlg = tk.Toplevel(self)
6809  dlg.title('Build manifest — what will be packaged')
6810  dlg.transient(self); dlg.grab_set()      # immediate grab — original pattern
6811  dlg.geometry('780x620')
```

No `withdraw`/`deiconify`/`update_idletasks`. **Matches the working baseline as the user described it.**

### 1c. `_run_pre_build_validation` — DIVERGES from baseline (still has the new instrumentation)
File:6579-6635. The user said the original had **no console prints** and **no progress callback**. Current code still has:

```py
6582  validator = BuildValidator(self.docs)
6587  import time as _t
6588  print('Pre-build validation: starting…', flush=True)
6589  _t0 = _t.perf_counter()
6590  issues = validator.run()
6591  print(f'Pre-build validation: completed in '
6592        f'{(_t.perf_counter()-_t0)*1000:.0f}ms with '
6593        f'{len(issues)} issue(s)', flush=True)
```

These prints are harmless on their own. The cursor='watch' toggle is gone (also as user described).

### 1d. `BuildValidator.run` — has `progress` parameter (user added)
File:2135-2158. `progress` defaults to `None`; `_run_pre_build_validation` calls `validator.run()` with no args, so the callback path is dead. **Benign, but a divergence from baseline.**

### 1e. `_check_namemap_completeness` — iterative walk in place
File:1096-1163. The stack-based version is correct; FName props (`RowName`, `TagName`, `Bubble`, `BaseBubbleName`), Imports, and the Exports[0].Table.Data row-name fallback are all visited. `EnumPropertyData` handling is preserved. **No logic regression vs. recursive original; should be strictly faster.**

### 1f. No leftover-from-broken-state code found
Checked entire file for `withdraw`, `deiconify`, `update_idletasks`, `progress_cb`, BuildValidator instantiations outside `_run_pre_build_validation`. Only one `BuildValidator(self.docs)` exists (line 6582). `CHECKS` is accessed only inside `run()` (line 2143). **No orphan calls.**

---

## 2. Root-cause hypothesis

**Confidence: medium-high — cause A (stale process / unsaved revert), not C (Tk poisoning).**

The current source code on disk is **already in the state the user calls "working"**:
- `_show_validation_dialog` uses `messagebox.*`
- `_show_manifest_dialog` uses early `transient + grab_set` (its original pattern)
- No orphan custom-Toplevel scaffolding remains

For the symptom ("Pre-build validation" or "Build manifest" titled grey window, app hung) to STILL occur with this code, one of the following must be true:

1. **A1 — The running Python process is an old instance** that loaded the editor before the revert, so it still has the broken `_show_*_dialog` bytecode in memory. Tkinter apps don't hot-reload on file change. Most-likely cause given that the source matches the "working" description but the user reports "still broken."
2. **A2 — A Python `__pycache__/SandboxZoneEditor.cpython-314.pyc` is being executed instead of the .py.** (Less likely but possible if the file is launched via a wrapper.)
3. **C — A residual run-time state in the live Tk root** from the earlier broken intermediate (during the same process lifetime) left the root in a bad grab/transient chain. Once an empty grab_set Toplevel was created and not properly destroyed (because the user force-killed it), subsequent Toplevels can inherit a poisoned grab on Windows.

Hypothesis B (different code culprit) is **rejected** — the source file as-read does not contain a culprit.

---

## 3. Specific actions to restore working state

The .py source itself does **not** need a code revert — it already matches baseline for the two dialog functions. The user's reported symptom is most likely a stale process. Recommended actions, in order:

1. **Hard-restart the editor process.** Close every Python window, kill any `pythonw.exe` / `python.exe` referencing `SandboxZoneEditor.py` in Task Manager, delete `scripts/__pycache__/SandboxZoneEditor.cpython-314.pyc` if present, then re-launch.
2. If still broken after a clean relaunch — diff against the symptom: the only remaining behavioural divergence from baseline is the print + `time.perf_counter` block at lines 6587-6593 plus the `progress` kwarg on `BuildValidator.run` (line 2135). Neither is a Tk hazard. To return to the literal pre-change baseline:
   - Lines 6587-6593: remove the `import time as _t` / two `print(...)` calls and the `_t0 = _t.perf_counter()` line. Keep `issues = validator.run()`.
   - Line 2135 signature: change `def run(self, progress=None):` back to `def run(self):` and delete the `if progress: ...` blocks at 2146-2148 and 2155-2157.
3. If the iterative walk is suspected of skipping a corner case (it shouldn't), revert lines 1110-1141 to the recursive `walk(obj)` form used by `_check_empty_struct_arrays` (file:1202-1213) — slow but provably equivalent to the original.

None of (2)/(3) are expected to fix the empty-dialog symptom; they are listed for completeness because the user asked for "exact line ranges to change to restore working state."

---

## 4. Tkinter principle

`tk.Toplevel.grab_set()` registers a global pointer/keyboard grab against a window that may not yet be **mapped** (drawn) by the window manager. On Windows in particular, grabbing an unmapped Toplevel can result in a window that is shown but never receives a paint event — hence the "grey rectangle, can't close" symptom. The standard mitigation is `dlg.wait_visibility()` (or `dlg.update_idletasks()` after packing widgets) **before** `grab_set()`. The original `_show_manifest_dialog` works in practice because Tk eventually flushes idle tasks on the next event-loop tick after the function returns to `mainloop` via `dlg.wait_window()`, and the small window is fast enough to map before the user notices. Once a process has had a Toplevel grab abandoned (e.g., user force-closed an empty dialog from an earlier broken iteration), the Tk root's grab stack can stay corrupted for the lifetime of the process — a fresh interpreter is the only reliable cure. This is why a process restart is the recommended first step regardless of source-code state.
