# Worldgen Bisection Plan — 14-chapter SS crash hunt

**Status:** working baseline confirmed, re-enabling zones one chapter at a time.

## Working baseline (saved to `backups/working 8-chapter (chap5-10 zones disabled)/`)

**Loads cleanly in-game.** This is the known-good rollback target if any re-enable step crashes.

### What's Live

- **All 14 SS chapter rows** (chap-1 through chap-14) — chapter scaffolding intact
- **3 outdoor bridge chapters** (Moria-DurinTower / -DimrillDale / -TradingPost) — ChapIDs 15/16/17
- **33 Live SS zones** — every zone hosted in chap-1, 2, 3, 4 (above) and chap-11, 12, 13, 14 (deep), plus the 3 outdoor bridges
- All Phase 1 landmark BasePos.Z clamps
- Sequential ChapterIDs 1–14 in SS scope
- BuildValidator: 0 issues

### What's Disabled (the 17 zones in chap-5..10)

| # | Zone | Originally hosted | Layer / Lv |
|---|---|---|---|
| 1 | `Sandbox_Small_City_B_Dwarrowdelf` | chap-5 | Lv-5 (+4) |
| 2 | `Sandbox_Small_OrcTown_D_Redeye` | chap-5 | Lv-5 (+4) |
| 3 | `Sandbox_Small_Elevator_G` | chap-5 | Lv-5 (+4) |
| 4 | `Sandbox_Small_OrcTown_C_Gundabad` | chap-6 | Lv-6 (+5) |
| 5 | `Sandbox_Small_DestroyedCity_E` | chap-6 | Lv-6 (+5) |
| 6 | `Sandbox_Small_Elevator_H` | chap-6 | Lv-6 (+5) |
| 7 | `Sandbox_Small_DestroyedCity_A_Desolation` | chap-7 | Lv-7 (+6) |
| 8 | `Sandbox_Small_AngryCaverns_B` | chap-8 | D-7 (-7) |
| 9 | `Sandbox_Small_DarkestDeeps_D` | chap-8 | D-7 (-7) |
| 10 | `Sandbox_Small_AngryCaverns_C` | chap-9 | D-6 (-6) |
| 11 | `Sandbox_Small_Dragon_A` | chap-9 | D-6 (-6) |
| 12 | `Sandbox_Small_Elevator_F` | chap-9 | D-6 (-6) |
| 13 | `Sandbox_Small_DestroyedCity_C` | chap-10 | D-5 (-5) |
| 14 | `Sandbox_Small_OrcTown_E_Ghash` | chap-10 | D-5 (-5) |
| 15 | `Sandbox_Small_DarkestDeeps_C` | chap-10 | D-5 (-5) |
| 16 | `Sandbox_Small_Elevator_E` | chap-10 | D-5 (-5) |
| 17 | `Sandbox_Small_Elevator_I` | chap-10 | D-5 (-5) |

### Other refs cleared (parcelizer-crash mitigation)

| Live zone | Field | Was → Now |
|---|---|---|
| `Sandbox_Small_OrcTown_B_Deep` | `SlideToZone` | `Sandbox_Small_DestroyedCity_C` → `None` |
| `Sandbox_Small_DarkestDeeps_E` | `ParentZone` | `Sandbox_Small_AngryCaverns_C` → `None` |

When re-enabling the disabled targets, optionally restore these.

## Re-enable order (one chapter per build)

| Step | Chapter | Zones | Add a stair? |
|---|---|---|---|
| 1 | **chap-5** (Lv-5) | City_B_Dwarrowdelf, OrcTown_D_Redeye, Elevator_G | yes — stair Elevator_G |
| 2 | chap-6 (Lv-6) | OrcTown_C_Gundabad, DestroyedCity_E, Elevator_H | yes — stair Elevator_H |
| 3 | chap-7 (Lv-7) | DestroyedCity_A_Desolation | no stair (top cap) |
| 4 | chap-10 (D-5) | DestroyedCity_C, OrcTown_E_Ghash, DarkestDeeps_C, Elevator_E, Elevator_I | yes — 2 stairs |
| 5 | chap-9 (D-6) | AngryCaverns_C, Dragon_A, Elevator_F | yes — stair Elevator_F |
| 6 | chap-8 (D-7) | AngryCaverns_B, DarkestDeeps_D | no stair (bottom cap) |

## After each step

1. Validator clean (0 issues)
2. Build mod pak
3. Test in-game
4. If it crashes — note the exception address + signature; the failing chapter's zones are the suspect set. Sub-bisect (re-enable individual zones in that chapter) to find the specific zone.
5. If it loads — proceed to the next step.

## Validator rules confirmed by this bisection

The 14 BuildValidator checks now include:

- `unanchored_zone` — bPositionFromLandmarks=true + no landmark + Pos=(0,0,0) → null deref in router
- `landmark_zband_misalign` — landmark BasePos.Z outside host chapter band → null deref in router
- `extended_connectivity_no_neighbour` — stair has no Layer±1 Live chapter → null deref in router
- `live_to_disabled` — now also covers zone→zone refs (ParentZone, SlideToZone). Live→Disabled zone ref → null `FZoneDefinition*` in parcelizer merge-sort comparator (`MorLayoutParcelizer.cpp:213`, exception 0x8 deref). Auto-fix clears the ref to `None`.
- `chapterid_duplicates` — duplicate ChapID across Live SS chapters
- `chapter_displayname_missing` — chapter DisplayName key not in World StringTable
