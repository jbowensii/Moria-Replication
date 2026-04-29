# Milestone: 8 Levels Working, 14-Level Z Space

**Saved:** 2026-04-29
**Closest tag:** v2.5.0 (Moria WorldGen Editor: row CRUD + humanized validator UX)

## State Summary

This is a known-good baseline where the in-game map renders all 8 vanilla SandboxSmall levels correctly, on a Z layout that has been pre-expanded to support up to 14 levels.

## What works

- **All 8 vanilla levels visible on map**: Lv-1, Lv-2, Lv-3, Lv-4, D-1, D-2, D-3, D-4
- **No crashes** during world generation
- **Lv-4 fully populated** (was empty in prior states — fixed by expanding chapter-4 to a 4-cell band + reverting 4 zones to vanilla auto-place + manual X/Y spread)
- **Stairs traversable** between all visible levels via the 5-stair architecture

## What doesn't (yet)

- **Lv-5, Lv-6, Lv-7, D-5, D-6, D-7 not visible on map.** Strongly suspected to be a hardcoded engine UI clamp on Layer range [-4..+3]. Data is structurally correct (verified 3 ways) but the compiled UI may ignore Layers outside that range. Investigation deferred.

## Z layout

| Lv | Chapter | Layer | MinZ | MaxZ | PrimeZ | Notes |
|---|---|---|---|---|---|---|
| Lv-7 | chapter-11 | +6 | 28 | 28 | 28 | Hosts TopStair |
| Lv-6 | chapter-10 | +5 | 27 | 27 | 27 | TopStair listed in addl |
| Lv-5 | chapter-9 | +4 | 26 | 26 | 26 | TopStair listed in addl |
| Lv-4 | chapter-4 | +3 | 22 | **25** | 22 | **4-cell band** for tall zones |
| Lv-3 | chapter-3 | +2 | 21 | 21 | 21 | UpperStair primary here |
| Lv-2 | chapter-2 | +1 | 20 | 20 | 20 | |
| Lv-1 | chapter-1 | 0 | 18 | 18 | 18 | GroundStair primary here |
| D-1 | chapter-5 | -1 | 17 | 17 | 17 | GroundStair listed in addl |
| D-2 | chapter-6 | -2 | 13 | 13 | 13 | |
| D-3 | chapter-7 | -3 | 9 | 9 | 9 | MidDeepStair primary here |
| D-4 | chapter-8 | -4 | 8 | 8 | 8 | MidDeepStair listed in addl |
| D-5 | chapter-12 | -5 | 4 | 4 | 4 | BottomStair listed in addl |
| D-6 | chapter-13 | -6 | 1 | 1 | 1 | BottomStair listed in addl |
| D-7 | chapter-14 | -7 | 0 | 0 | 0 | BottomStair primary here |

## Key fixes baked in

1. **Z-shift**: Vanilla SandboxSmall shifted +7 cells (Lv-1 MinZ now 18) — preserves vanilla relative geometry.
2. **5-short-stairs architecture**: replaced 8 over-aggressive stairs (`Size.Z=4 + bExtendFootprint=true`) that crushed neighbor-floor content. Now 5 stairs with `Size.Z=1` or `2` and `bExtendFootprint=false`.
3. **Chapter-4 expanded to 4-cell band**: Z=22..25, PrimeZ=22 — gives 4-tall zones (DestroyedCity_B, DarkestDeeps_E, AngryCaverns_C) room to fit.
4. **Chapter-9 (Lv-5) shifted up to Z=26** to avoid overlap with expanded Lv-4 band.
5. **4 unanchored ch-4 zones reverted to vanilla pattern**: Pos=(0,0,0), bPosFromLandmarks=true. Runtime auto-places them inside the 4-cell band.
6. **OrcTown_D_Redeye** kept at explicit Pos=(15,15,22) — has real X/Y so no sentinel issue.
7. **6 chapter rows added** (chapter-9..14) for Lv-5/6/7 + D-5/6/7 with proper StringTable display names.
8. **All NameMap counters synced** across 4 modified DTs.

## Files

- `DT_Moria_Zones.json`
- `DT_Moria_Chapters.json`
- `DT_Moria_Landmarks.json`
- `DT_Moria_LayoutConnections.json`
- `World.json` (StringTable)

## Roll-back

```
cp "experiments/worldgen_research/backups/8 levels working - 14 level space/"*.json experiments/worldgen_research/
```

## Validator state at save

- 0 errors
- 23 warnings (all pre-existing vanilla-tolerated patterns: 16 null-endpoint connections, 9 unanchored zones, 1 namemap_completeness, 1 landmark_zband_misalign, 1 live_landmark_has_host on `Sandbox.CrystalDescent`)
- Deep verify: 11/11 pass
