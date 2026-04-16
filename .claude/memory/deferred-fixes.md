---
name: Deferred Stability Fixes
description: Deferred code review items — server-fly polling, replenish handle, dedi nullptr, widget pointers, TArray risk
type: project
originSessionId: faf77fec-764b-499b-8ea8-e24075baf1b0
---
## W1: Server-fly sweep polling → event-driven (DEFERRED from v6.3.7 review)

**Current**: Sweep runs every 2s, sets bIgnoreClientMovementErrorChecksAndCorrection + bServerAcceptClientAuthoritativePosition on ALL authority dwarves unconditionally. Permanently disables server movement correction for all players regardless of fly state.

**Goal**: Instead of polling every 2s, hook player login/spawn on the server and set the flags once when a player joins. No continuous polling needed.

**Approach**: Hook `APlayerController::BeginPlay` or pawn `PossessedBy` on the server side. When a new dwarf spawns with Role=Authority, set the two flags on its CharacterMovement once.

**Why deferred**: Works now, just inefficient and overly permissive. User OK with arbitrary position acceptance for this co-op mod.

## W2: Replenish ServerDebugSetItem — verify handle/stack semantics (DEFERRED)

**Current**: `ServerDebugSetItem(Class, Count)` takes a TSubclassOf and int32 Count. Passes maxStack as Count.

**Concern**: This operates by item CLASS, not by ItemHandle. If a player has multiple stacks of the same item in different containers, ServerDebugSetItem may set the TOTAL count across all containers rather than a specific stack. User wants handle-specific stack fill.

**Action needed**: Test in-game with multi-container scenario. If it over-fills, find a handle-based Server RPC or use a different approach.

## W3: findPlayerController returns nullptr on dedicated server (DEFERRED)

**Current**: Returns nullptr when no PC has bIsLocalPlayerController=true. Old code returned pcs[0].

**Risk**: Low — dedi server detection at dllmain.cpp:1074 already handles nullptr PC. Most callers null-check. Verify no dedi crash logs.

**Action needed**: Check UE4SS.log on a dedicated server for nullptr-related warnings.

## W3: Widget Pointers — Convert ~30 raw UObject* to FWeakObjectPtr (DEFERRED)

**Risk**: LOW in practice — widgets are viewport-rooted so GC won't collect them during normal play. World transitions clear all widget members.

**Plan**: Phase over multiple releases:
1. Start with crash-prone ones: m_fontTestWidget, m_ftScrollBox, m_ftRemovalVBox
2. Then toolbars: m_umgBarWidget, m_mcBarWidget, m_abBarWidget
3. Then remaining: error box, crosshair, trash dialog, label pointers

**Files**: dllmain.cpp (declarations), moria_widgets.inl (usage), moria_debug.inl (usage)

## W4: TArray Direct Manipulation — Cannot Fix, Documented Risk

**Location**: moria_inventory.inl:57-92, removeItemEffectFromList()

**What it does**: Directly modifies TArray `Num` field and swaps elements via memcpy to remove item effects (tint/rune). No UFUNCTION exists for this operation.

**Risk**: Bypasses replication and internal UE4 bookkeeping. Could cause desync in multiplayer. Bounds-checked before memmove.

**Why we can't fix it**: The game doesn't expose item effect removal as a UFUNCTION. The only alternative would be calling the full ServerTintItem pipeline which requires crafting material handles.

**Mitigation**: Comment documents the risk. Bounds checking verified. Single-player only context (mod feature).
