# DestroyedCity_A_Desolation Crash Analysis

**Crash:** `EXCEPTION_ACCESS_VIOLATION` at `FMorLayoutConnectionInstance::GetZone()` 0x1a1, fired from `UWorldRoute::AStarSearch` -> `L2_RouteConnection` -> `L2_RouteInterzoneConnections` when the zone `Sandbox_Small_DestroyedCity_A_Desolation` is Live.

**Working theory:** The crash is NOT about the zone's footprint, Z-band, world ceiling, or bubble cell shape. It is a **dangling Live LayoutConnection that requires a landmark no Live zone hosts anymore.**

---

## Top hypothesis (very high confidence): orphaned `Sandbox_Small_21stHallToBridge` LayoutConnection

**Evidence:**

- `DT_Moria_LayoutConnections.json` row **`Sandbox_Small_21stHallToBridge`** is `EnabledState=Live`, `bRequired=True`, `bExclusive=True`, `ZoneRule=Chapter`, `ZoneSet=SandboxSmall`. (grep hit at the connection-table dump above.)
- Its endpoints are landmark-typed: `OriginLandmark=Sandbox.21stHall`, `DestinationLandmark=Sandbox.Bridge`.
- In `DT_Moria_Zones.json`, **zero zones** (Live or Disabled) hold `Sandbox.21stHall` in their `LandmarkHandles[]`. We removed it from `Sandbox_Small_DestroyedCity_A_Desolation` row 49, and no other zone ever held it.
- `Sandbox.Bridge` is held by `Sandbox_Small_City_A_EasternBastion` (chap-1, Z=15..16). `Sandbox.21stHall` landmark itself still has `BasePosition.Z=26, Placement=Free, EnabledState=Live` in `DT_Moria_Landmarks.json`.

When `L2_RouteInterzoneConnections` walks every Live SandboxSmall connection and tries to resolve the **host zone** of `Sandbox.21stHall`, the lookup returns null. `FMorLayoutConnectionInstance::GetZone()` then dereferences a null `FZoneDefinition*` at offset 0x1a1 — exactly the observed signature. This matches the existing rule 6.5 ("dangling FName references") but at the *connection-endpoint* level rather than the NameMap level.

The reason re-enabling the zone "triggers" the crash isn't that the zone is broken — it's that disabling the zone **also** disables the chapter-7 connection graph the router walks. Once the zone is Live, chap-7 is in the graph, the A* run starts, and the orphaned `21stHallToBridge` row gets visited.

This is also consistent with the user already disabling `Sandbox_Small_GhashOrcTown_To_Descent` (a sibling orphan) — there's a class of orphan connection rows in this table; we caught one but missed `21stHallToBridge`.

## Hypothesis 2 (medium): bubble footprint / zone footprint mismatch with `bExtendFootprint=True`

**Evidence:**

- `BF_BB_Chapter4_21stHall.json` `SupportedInterfaces` enumerates 36 entries but only **6 unique subcells**: (0,0,0), (1,0,0), (0,1,0), (1,1,0), (0,1,1), (1,1,1). This is **not** a uniform 2x2x2 cube — Y=0 row only exists at Z=0; the bubble is L-shaped on Z. Every face direction (East/West/N/S/Up/Down) has an interface entry on every present subcell, including Up on (0,1,1)/(1,1,1) — meaning the bubble actively advertises a +Z hookup at its top.
- Zone `TargetSize=(10,10,2)` is far larger than the bubble's 2x2x2 envelope, with `bExtendFootprint=True`. With AutoConnections=All and chap-7 sitting at the top of the world (no chap above), an interface on the bubble's +Z face has nowhere to route.
- Counter-evidence: `Sandbox_Small_DestroyedCity_E` (chap-6, Pos=(0,0,24), Size=(12,14,2), bExtendFootprint=True) is also a non-trivial bubble at the top of its band and loads fine. So large-footprint + bExtend alone is not the trigger.

If hypothesis 1 is wrong, this is the next thing to test.

## Hypothesis 3 (lower): chapter-graph reachability gap for the required `ZoneRule=Chapter` connection

**Evidence:**

- `21stHallToBridge` is `ZoneRule=Chapter` (must traverse the chapter graph). It would need a path chap-7 -> chap-6 -> ... -> chap-1.
- chap-7 has only one Live zone (the suspect). chap-5 and chap-6 are sparsely populated. The A* graph between Z=26 (origin landmark BasePosition) and Z=15 (Sandbox.Bridge BasePosition) may have an unwalkable Z-cell band.
- Even if the landmark host resolved, the routing buffer would still face an 11-cell vertical climb across 6 chapters with thin zones — a long-shot for A* under `bRequired=True`.

This collapses into hypothesis 1 if the connection is the proximate cause: fixing the orphan kills the routing entirely.

---

## Three test interventions (in order)

1. **Disable `Sandbox_Small_21stHallToBridge` in `DT_Moria_LayoutConnections.json`** (set `EnabledState=Disabled`). Rebuild. **If the world loads, hypothesis 1 is confirmed.** This is the safest, smallest change and addresses the root cause directly.

2. **Re-attach the `Sandbox.21stHall` landmark** to a Live zone (the natural home is `Sandbox_Small_DestroyedCity_A_Desolation` — restore `LandmarkHandles[]` with `Landmark=Sandbox.21stHall`, `bExtendedConnectivityLandmark=false`), and re-clamp `Sandbox.21stHall.BasePosition.Z` to chap-7 MinZ=26 (already the case). Rebuild with the LayoutConnection still Live. **If the world loads, hypothesis 1 is confirmed via the other side** (the connection itself is fine; only the orphan was lethal).

3. **If 1 and 2 both still crash:** set `bExtendFootprint=False` on the zone and rebuild. **If the world then loads, hypothesis 2 is the cause** (footprint extension off the world edge / off the chapter band). If still crashing, hypothesis 3 — drop `AutoConnections` from `All` to `None` and retest, which proves chapter-graph reachability is the blocker.

Run them in order; stop at the first that loads.

## Things not yet captured in `Worldgen Rules and Constraints.md`

- **Orphan LayoutConnection rule.** Every Live `DT_Moria_LayoutConnections` row whose `OriginLandmark`/`DestinationLandmark` references a landmark that **no Live zone holds in `LandmarkHandles[]`** is a 0x1a1 crash waiting to happen. This is distinct from the "Live -> Disabled chapter/deck/landmark" check the validator already runs. Suggested validator: `_check_orphan_layout_connections` — for every Live connection, verify each Origin/Destination Landmark RowName is referenced by at least one Live zone's LandmarkHandles. Auto-fix: set the connection EnabledState to Disabled (the route was vanilla campaign infrastructure that no longer applies once the SandboxSmall zone topology changes).
- **Detaching a landmark from a zone is not a complete operation.** The validator must follow up by scanning LayoutConnections for any row that uses that landmark name and either disable those rows or reattach the landmark elsewhere.
- **`bExtendFootprint=True` interaction with chapter-top zones.** Worth a callout in the rules doc that the topmost-layer chapter (no Live chapter above) should avoid `bExtendFootprint=True` on bubbles whose `SupportedInterfaces` advertise `ECellDirection::Up` faces. Bubble `BB_Chapter4_21stHall` advertises Up on subcells (0,1,1) and (1,1,1).
- **Bubble subcell footprint asymmetry.** `BB_Chapter4_21stHall` is **not a regular 2x2x2 cube**; it's L-shaped (Y=0 layer present only at Z=0). When sizing a host zone's `TargetSize`, the asymmetric footprint can cause the placer to leave gaps that the A* router treats as required-but-empty cells. Worth documenting per-bubble-footprint shapes in the project for any bubble used as a fixed-placement landmark anchor.
