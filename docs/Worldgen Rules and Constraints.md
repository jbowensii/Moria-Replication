# Return to Moria — Worldgen Rules and Constraints

**Audience:** modders editing the worldgen DataTable JSONs (`DT_Moria_Zones`, `DT_Moria_Chapters`, `DT_Moria_Landmarks`, etc.) and packaging into IoStore mods.

**Status:** all rules below are derived from auditing pristine vanilla data plus empirical build/test evidence. Treat them as project-wide invariants.

---

## 1. World grid dimensions

The Moria worldgen grid is a fixed-size cube. All three axes have the same valid range.

| Axis | Range | Cells | Notes |
|---|---|---|---|
| X | 0..29 | 30 | Vanilla campaign reaches X=29 |
| Y | 0..29 | 30 | Vanilla campaign reaches Y=29; one Expedition landmark at Y=30 is special-cased |
| Z | 0..29 | 30 | Confirmed by build/test crash at Z=30 (`FMorLayoutConnectionInstance::GetZone` null deref) |

**Z=0 is a valid coordinate** — it is NOT the unplaced sentinel. The unplaced sentinel is the *full vector* `Position=(0,0,0)`. A pinned zone at e.g. `Position=(5,8,0)` is valid and pinned to Z=0.

## 2. Zone TargetSize ceiling

| Limit | Value |
|---|---|
| Max TargetSize.X | 14 |
| Max TargetSize.Y | 14 |
| Max TargetSize.Z | 4 |

Vanilla SandboxSmall used max TargetSize=8 (Suburban_A_Westgate). Vanilla campaign max=5. The 14×14×4 ceiling is a project-set headroom for modded variants.

## 3. Chapter Z-band rules

The 14-chapter SandboxSmall stack must fit in Z=0..29 (30 cells total).

| Constraint | Rule |
|---|---|
| Each chapter | `MinZ ≥ 0` AND `MaxZ ≤ 29` |
| Each chapter | `MinZ ≤ MaxZ`, `Height = MaxZ - MinZ + 1 ≥ 1` |
| Stack budget | sum of heights of all Live SandboxSmall chapters ≤ 30 |
| PrimeZ | typically `floor((MinZ + MaxZ) / 2)`, used as the player spawn / mapstone reference Z |

Chapter Z bands are **generation-time hints**, not hard runtime constraints on zone Position.Z. Vanilla has many zones with Position.Z outside their chapter's band — the engine tolerates it.

## 4. Zone overlap rules

Two pinned zones overlap if their `Position + TargetSize` cuboids share any cell. Coverage = (overlap volume) / (zone volume) — computed for both zones independently.

### Same-chapter overlap

**Allowed: 0% to 100%.**

Vanilla heavily uses the **variant pattern**: 2-3 zones share identical `Position + TargetSize` (100% mutual overlap). The generator picks ONE per game seed. Examples in vanilla SandboxSmall:

```
Mines_B / Mines_C / Mines_D       all at Pos=(14,15,9) Size=(6,6,3)
ElvenQuarter_B / ElvenQuarter_C   at Pos=(5,12,12) Size=(6,6,1)
Suburban_B_Highway / Suburban_C   at Pos=(10,10,12) Size=(4,4,1)
```

Same-chapter partial overlap is also fine (vanilla has 5 such pairs; the generator resolves them).

### Cross-chapter overlap

**Allowed: ≤ 20% coverage on either zone.**

Vanilla SandboxSmall had 4 cross-layer partial overlap pairs, max 12% coverage. The 20% threshold gives modders some headroom while staying within engine tolerance.

Single-axis overlap should be **≤ 4 cells** in any direction (vanilla max).

### Cross-zoneset overlap (e.g., SandboxSmall × Moria)

**No constraint.** Different zone sets are never generated together at runtime — only one zoneset is selected per game (Sandbox vs Campaign vs Expedition). Cross-zoneset overlap is informational.

## 5. Landmarks

| Property | Notes |
|---|---|
| `BasePosition` | IntVector — landmark anchor cell |
| **No size fields** | Landmarks have NO TargetSize. Size flows through the host zone's TargetSize. |
| `bPositionFromLandmarks` (on the Zone) | When TRUE, the zone derives its position from the attached landmark's BasePosition. 42 of 44 vanilla SandboxSmall zones have this TRUE — it's the normal pattern, NOT an accidental flip. |
| Landmark BasePosition.Z bounds | Same as world Z: 0..29 |
| Landmark vs zone alignment | When `bPositionFromLandmarks=true`, ensure landmark BasePosition aligns with the host zone's chapter Z band. Mismatch can cause routing crashes. |

## 6. The L2_RouteInterzoneConnections crash signature

The most common crash signature for malformed worldgen:

```
EXCEPTION_ACCESS_VIOLATION reading address 0x00000000000001a1
FMorLayoutConnectionInstance::GetZone()
UWorldRoute::AStarSearch()
L2_RouteInterzoneConnections
```

**This is a null pointer deref at offset 0x1a1 inside the connection routing system.** Known triggers:

1. **Z values out of [0,29]** — a chapter MinZ < 0 or MaxZ > 29
2. **NameMap counter mismatch** — `NamesReferencedFromExportDataCount` or `Generations[0].NameCount` ≠ `len(NameMap)`
3. **Dangling FName references** — RowName values not present in NameMap
4. **Stale staging uassets** — `experiments/sandbox_zone_mod/staging/` has uassets from a prior build that conflict with current JSONs (auto-fixed by SandboxZoneEditor's wipe-staging step)
5. **bPositionFromLandmarks misalignment** — a Live zone has bPositionFromLandmarks=true but the attached landmark's BasePosition is far from the zone's chapter band

## 6-stairs. Stairs and Crystal Descents grow UP from an origin in their host chapter band (LOCKED 2026-04-26)

Stair zones (`Sandbox_Small_Elevator_*`) and Crystal Descent zones are **deliberately multi-level**. The mental model:

> A stair has an **origin** at the bottom of the zone. The origin must sit in the host chapter's Z-band. The zone then **grows upward** (Z increases) by `TargetSize.Z` cells, bleeding through one or more adjacent chapters above.

**The rule:**
- **Origin Z** (= `Position.Z` if pinned, or `bPositionFromLandmarks=true` landmark's `BasePosition.Z`) MUST lie inside the host chapter's `[MinZ, MaxZ]`. Typically `MinZ`.
- The zone's **top** (`origin_z + TargetSize.Z - 1`) MAY extend past `MaxZ` into chapters above — that's the routing intent.
- The top still must satisfy **≤ 29** (world Z ceiling).
- Stairs extend **upward only** (positive Z direction). They never extend downward from their origin.

**Current state (verified):** all 8 SS elevator zones have origins inside their host chapter Z-band, and tops within the world ceiling:

| Stair | Host chap | Band | Origin | Top | Bleeds into |
|---|---|---|---|---|---|
| Elevator_B | chap-1 (Lv-1) | 15..16 | 15 | 18 | chap-2, chap-3 |
| Elevator_C | chap-13 (D-2) | 12..13 | 12 | 15 | D-1, ground |
| Elevator_D | chap-3 (Lv-3) | 18..19 | 18 | 21 | chap-4 |
| Elevator_E | chap-10 (D-5) | 6..7 | 7 | 10 | D-4, D-3 |
| Elevator_F | chap-9 (D-6) | 3..5 | 5 | 8 | D-5, D-4 |
| Elevator_G | chap-5 (Lv-5) | 22..23 | 22 | 25 | chap-6 |
| Elevator_H | chap-6 (Lv-6) | 24..25 | 24 | 27 | chap-7 |
| Elevator_I | chap-10 (D-5) | 6..7 | 6 | 9 | D-4, D-3 |

**Practical effect on Phase 1 landmark Z clamping:** when we clamp a stair landmark's `BasePosition.Z` to the host chapter `MinZ`, the stair correctly starts at the chapter floor and extends into the chapter above — exactly the vanilla pattern. No additional fix needed.

**Vanilla examples:**
- `Elevator_B` `Size=(6,6,4)` in chap-1 (Z=15..16) → occupies Z=15..18, bleeds into chap-2 (Z=17..17) and chap-3 (Z=18..19)
- `Elevator_C` `Size=(6,6,4)` in chap-13 (D-2, Z=12..13) → occupies Z=12..15, bleeds up into D-1 and ground
- `CrystalDescent (Ch3)` is 193m vertical → ~6 Z cells tall in stored units, anchored at the top of its chapter, descending

**Validator interaction:** the existing `_check_z_bounds` only flags `Pos.Z + Size.Z - 1 > 29` (true world-edge violation). It does NOT flag stair zones for bleeding into adjacent chapters — that's the design. Cross-chapter overlap rules also explicitly tolerate stairs (single-axis ≤4 cells matches Elevator zone Size.Z=4).

## 6-bundle. The DATATABLES registry must include every modified DT (LOCKED 2026-04-26)

The editor's build pipeline only bundles tables registered in the `DATATABLES` dict at the top of `scripts/SandboxZoneEditor.py`. If a DataTable's `.json` is edited but the table isn't in `DATATABLES`, the registry never sees the file — the diff against `.original.json` is never run, the modified uasset is never regenerated, and the build pak silently ships the **pristine** version of that table alongside our modified zones / chapters.

This produces an instantly-broken mod: the modified `DT_Moria_Zones` references new chapters, but the unbundled `DT_Moria_LayoutConnections` and `DT_Moria_ZoneTemplates` come from the pristine pak (which doesn't know about chapters 5-7 or 8-10). A* routing crashes the moment it walks a connection that points to a row that exists only in the modified-but-not-bundled side.

**Required registry entries (current):**

```python
DATATABLES = {
    'zones':       (...),   # DT_Moria_Zones
    'chapters':    (...),   # DT_Moria_Chapters
    'biomes':      (...),   # DT_Moria_Biomes
    'decks':       (...),   # DT_Moria_ZoneDeck
    'filters':     (...),   # DT_Moria_ZoneBubbleFilters
    'landmarks':   (...),   # DT_Moria_Landmarks
    'strings':     (...),   # World StringTable
    'connections': (...),   # DT_Moria_LayoutConnections   ← REQUIRED
    'templates':   (...),   # DT_Moria_ZoneTemplates       ← REQUIRED
}
```

If you add new modifiable DataTables to the project, add them here BEFORE editing the JSONs. Otherwise the editor will load and validate them but never bundle the resulting uasset.

## 6-parcel. Live zone references to Disabled zones crash the parcelizer (LOCKED 2026-04-26)

A Live SandboxSmall zone with `ParentZone` or `SlideToZone` pointing at a **Disabled** zone makes the world generator crash in **parcelization** — BEFORE routing.

**Crash signature (different from the GetZone routing class):**

```
EXCEPTION_ACCESS_VIOLATION reading address 0x0000000000000008
MorLayoutParcelizer.cpp:213  (lambda comparator)
TMergeSort<...>::Sort<FZoneDefinition const *, ...>
UMorLayoutParcelizer::OrderParcelization()
UMorLayoutParcelizer::ParcelizeBetter()
```

The merge-sort comparator dereferences a `FZoneDefinition const *` at offset 0x8; when the target zone is Disabled the resolution returns null.

**Fix:** clear the ref to `None`, OR re-enable the target zone. The validator's `_check_live_to_disabled` covers `Chapter`, `BubbleDeck`, `PassageDeck`, `Landmark`, **AND** `ParentZone` / `SlideToZone`. Auto-fix prefers clearing zone-refs to `None` (safer than re-enabling a row that may have been disabled intentionally) and re-enabling chapters / decks / landmarks.

**Bisection takeaway:** the original `0x1a1` GetZone routing crash and this `0x8` parcelizer crash are two distinct defects. After fixing the routing class, the parcelizer class became visible. Always check both.

## 6-trifecta. Unanchored zone trifecta = crash (LOCKED 2026-04-26)

A Live SandboxSmall zone is **unanchored** (and will crash A* routing) when ALL THREE conditions hold:

1. `bPositionFromLandmarks = true`
2. `LandmarkHandles[]` is empty (or all entries have `Landmark.RowName = "None"`)
3. `Position = (0, 0, 0)` (the sentinel)

The runtime cannot derive a placement → null at `FMorLayoutConnectionInstance::GetZone` (offset 0x1a1).

**Fix options:**
- Set `bPositionFromLandmarks = false` (zone falls back to `bPositionFromZoneTable` + Position sentinel = generator picks freely in chapter — vanilla pattern for unpinned zones)
- Or attach a landmark in `LandmarkHandles[]` whose `BasePosition.Z` lies inside the host chapter's `[MinZ, MaxZ]`

**Common cause:** duplicating a zone (e.g. `Sandbox_Small_DestroyedCity_B → _B1`) copies the `bPositionFromLandmarks=true` flag from the parent but doesn't carry over the landmark — leaving the duplicate with the lethal trifecta.

Validator: `unanchored_zone` (auto-fix clears the flag).

## 6a. Landmark BasePosition.Z must align with host chapter Z band (LOCKED 2026-04-26)

When a zone has `bPositionFromLandmarks=true` (the vanilla pattern — 42/44 SandboxSmall zones), the runtime derives the zone's position from each attached landmark's `BasePosition`. **For each such landmark, `BasePosition.Z` MUST lie within the host zone's chapter `[MinZ, MaxZ]`.**

If `BasePosition.Z` is outside the band, the routing graph builds an edge into a Z-cell that does not exist in that chapter → null deref at `FMorLayoutConnectionInstance::GetZone` (offset 0x1a1).

**Whenever a zone is moved between chapters, every attached landmark's `BasePosition.Z` MUST be re-clamped to the new chapter's band.** This was the silent-defect class that survived multiple debugging passes earlier in this project — the validator now flags it as `landmark_zband_misalign` (auto-fix: clamp to chapter MinZ).

## 6b. ChapterID uniqueness (LOCKED 2026-04-26)

Each Live SandboxSmall chapter MUST have a unique `ChapterID`. Duplicates collapse the in-game travel-stone / map UI into a single bucket, and may break any routing that keys off ChapterID.

When adding new chapters or renumbering, ensure `ChapterID` is unique across all Live SS chapter rows. Validator check: `chapterid_duplicates` (no auto-fix — renumbering is design-level).

## 6c-bridge. Outdoor DLC bridge zones (vanilla pattern, intentional)

Three SandboxSmall zones bridge into the DLC outdoor chapters. They have **`ZoneSet=SandboxSmall`** but their **`Chapter`** points at a Moria-* chapter row:

| Zone | Chapter (Moria ZoneSet) | Outdoor area |
|---|---|---|
| `Sandbox_DurinsTower` | `Moria-DurinTower` (ChapID 6) | Durin's Tower |
| `Sandbox_TradingPost` | `Moria-TradingPost` (ChapID 8) | Trading Post |
| `Sandbox_DimrillDale` | `Moria-DimrillDale` (ChapID 7) | Dimrill Dale |

**This is the vanilla design** — never "fix" these to point at SandboxSmall-* chapters. The runtime resolves chapter by FName row name, so cross-ZoneSet refs work.

Side effect: ChapterID is **scoped per ZoneSet, not globally unique**. Vanilla shipped collisions across ZoneSets (e.g., `ChapterID=2` is used by `Moria-chapter-2`, `SandboxSmall-chapter-2`, and `SandboxMedium-chapter-2`). The validator only enforces uniqueness within Live SS chapters.

The level chart prints these rows under an `OUTDOOR / BRIDGE` section.

## 6c. Chapter DisplayName must reference an existing StringTable key

Each Live SS chapter's `DisplayName` field is a soft reference to a key in `World.uasset` StringTable (namespace `World`). If you change DisplayName, the new key MUST be added to the StringTable, or the in-game UI will show the raw key string. Validator check: `chapter_displayname_missing` (warning, no auto-fix — user picks the display text).

## 7. The validation pipeline

The `BuildValidator` class in `scripts/SandboxZoneEditor.py` runs 9 checks before every Build Mod Pak. Auto-fixes apply where safe; user is prompted otherwise.

| Check | Auto-fix |
|---|---|
| NameMap completeness | yes (append missing FNames) |
| NameMap dedup | yes |
| Empty StructProperty arrays without DummyStruct | yes (inject template) |
| Duplicate row names | manual |
| EnabledState enum values | manual |
| Cross-DT row reference resolution | manual |
| Z bounds [0..29] for chapters / zones / landmarks | yes (clamp) |
| Landmark BasePosition.Z within host chapter band | yes (clamp to chapter MinZ) |
| Extended-connectivity stair has Layer±1 neighbours | manual |
| Unique ChapterID across Live SS chapters | manual |
| Chapter DisplayName resolves in World StringTable | manual |
| Live zone → Disabled chapter | yes (re-enable referenced chapters) |
| `NamesReferencedFromExportDataCount` + `Generations[0].NameCount` sync | yes |

## 8. Backups and the staging-wipe rule

Before any chapter-level edit, snapshot to `experiments/worldgen_research/backups/<descriptive-name>/`. Recommended naming: `before <change-name>`.

The Build Mod Pak in `SandboxZoneEditor.py` automatically wipes `experiments/sandbox_zone_mod/staging/` and `out/` before each build. This prevents stale-uasset ghost edits.

If building outside the editor, manually `rm -rf experiments/sandbox_zone_mod/staging/* experiments/sandbox_zone_mod/out/*` first.

## 9. Bubble field reference (in-game Num0 inspector)

| Inspector field | Meaning | Where to use in JSON |
|---|---|---|
| Definition (`BD_...`) | Bubble Data UAsset name | NOT directly used; ZoneDeck uses `BB_*` short names |
| Definition Path | `/Game/Tech/Data/Bubbles/.../BD_X.BD_X` SoftObjectPath | rare — most refs are FName-based |
| Root Cell | bubble's root cell coordinate | `Zone.Position` or `Landmark.BasePosition` for fixed placement |
| Display Name | StringTable key | look up in `World.uasset` for name |
| Landmark Row | DT_Moria_Landmarks row name | `Zone.LandmarkHandles[].Landmark.RowName` |

Runtime-only fields (Instance Name, World Transform, Full Path, Class) are diagnostics only — never put them in JSON.

## 10. Travel-stone / map debug procedure

The UE4SS C++ debug mod hotkeys:

| Key | Action |
|---|---|
| `Num*` | Reveal map (populates landmark mapstones) |
| `Num-` | Cycle target landmark (`Shift+Num-` reverses) |
| `Num.` | Teleport to current target landmark |

**Always enable fly mode before teleporting** — bubble streaming can take a few seconds and the player can fall into the void otherwise.

## 11. References

- `~/.claude/skills/moria-worldgen-construction/SKILL.md` — full editing skill
- `~/.claude/skills/level-list/SKILL.md` — chapter chart printer
- `~/.claude/projects/C--Unreal-Projects-Delving/memory/moria-worldgen.md` — session memory
- `experiments/worldgen_research/_full_z_audit.py` — Z bounds + chapter audit
- `experiments/worldgen_research/_overlap_audit.py` — overlap rule validator
- `experiments/worldgen_research/_post_surgical_audit.py` — comprehensive post-edit audit
- `scripts/SandboxZoneEditor.py` `BuildValidator` class — pre-build validation pipeline
