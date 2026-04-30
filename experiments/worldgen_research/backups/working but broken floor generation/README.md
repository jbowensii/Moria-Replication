# Milestone: Working but Broken Floor Generation

**Saved:** 2026-04-30
**Status:** 🟡 World loads in-game, but floor generation is broken

## What works

- World loads, no crashes
- Validator: 0 errors, 25 warnings (vanilla noise)
- Deep verify: 11/11 pass
- All 14 chapters present and connected via 9-zone elevator chain
- Sequential ChapterID 1..14 (1..7 going up, 8..14 going down from D-7)
- EnemyScalingLevel matches vanilla 0..4 with new floors capped at 4
- Stair landmarks renamed to FirstStair..FourteenthStair (odd-up/even-down convention)
- Chapter-prefixed landmark renamed (Chapter1.ElvenQuarterEntrance)
- NameMap orphans pruned: 72 stale strings removed across 4 DTs

## What's broken

- **Floor/map generation is visually wrong** — many floors have malformed layouts in-game
- Specifics need diagnosis (next session)
- Possible causes to investigate:
  - Zone Position.Z values inconsistent with new chapter Z bands after the chapter rename
  - Bridge zones (Size.Z=5) may not place correctly
  - DestroyedCity_A_Desolation TargetSize.Z=7 with PreferredZOverride=29 = footprint Z=29..35 (overflows engine ceiling — was just identified, not yet fixed in this snapshot)
  - Chapter band expansions (Lv-2/D-1/D-2/D-4/D-5) may be inconsistent with zone Position.Z values
  - Chain LayoutConnections may be referencing wrong elevators after renames

## Final chapter table at this snapshot

| Lv | Chapter | Layer | CID | ES | Z-band | Live |
|---|---|---|---|---|---|---|
| Lv-7 | chapter-7 | +6 | 7 | 4 | 29..29 | 1 |
| Lv-6 | chapter-6 | +5 | 6 | 4 | 28..28 | 1 |
| Lv-5 | chapter-5 | +4 | 5 | 4 | 27..27 | 1 |
| Lv-4 | chapter-4 | +3 | 4 | 3 | 24..26 | 1 |
| Lv-3 | chapter-3 | +2 | 3 | 2 | 23..23 | 3 |
| Lv-2 | chapter-2 | +1 | 2 | 1 | 21..22 | 4 |
| Lv-1 | chapter-1 | 0 | 1 | 0 | 20..20 | 5 |
| D-1 | chapter-14 | -1 | 14 | 1 | 16..19 | 4 |
| D-2 | chapter-13 | -2 | 13 | 2 | 12..15 | 4 |
| D-3 | chapter-12 | -3 | 12 | 3 | 11..11 | 4 |
| D-4 | chapter-11 | -4 | 11 | 4 | 7..10 | 2 |
| D-5 | chapter-10 | -5 | 10 | 4 | 4..6 | 2 |
| D-6 | chapter-9 | -6 | 9 | 4 | 1..3 | 3 |
| D-7 | chapter-8 | -7 | 8 | 4 | 0..0 | 2 |

## Stair landmark renames (odd-up / even-down)

| Stair # | Anchor | Zone |
|---|---|---|
| 1st | Lv-1 | Elevator_B (vanilla preserved) |
| 5th | Lv-3 | Lv3Lv4Connector |
| 7th | Lv-4 | TopElevator |
| 2nd | D-1 | D1Lv1Connector |
| 4th | D-2 | DeepUpperEl |
| 6th | D-3 | DeepMidEl |
| 8th | D-4 | D4D3Connector |
| 10th | D-5 | DeepBottomEl |
| 12th | D-6 | D7D6Stair |
| 14th | D-7 | CrystalDescent |

## Roll-back

```
cp "experiments/worldgen_research/backups/working but broken floor generation/"*.json experiments/worldgen_research/
```

## Files

- DT_Moria_Zones.json
- DT_Moria_Chapters.json
- DT_Moria_Landmarks.json
- DT_Moria_LayoutConnections.json
- World.json
