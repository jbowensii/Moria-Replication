---
name: multiplayer-fly-fix
description: v6.3.5 fix for MP fly — findPlayerController filters by bIsLocalPlayerController, server-fly sweep sets auth flags on all dwarves
type: project
originSessionId: faf77fec-764b-499b-8ea8-e24075baf1b0
---
## findPlayerController() rewrite (v6.3.5)

In multiplayer, `FindAllOf("PlayerController")` returns local + replicated proxies.
Previous code returned `pcs[0]` which was typically the host's proxy on non-host clients.

**Fix:** Walk all PCs, filter by `bIsLocalPlayerController` UPROPERTY (set by engine in
`PostInitializeComponents` → `IsLocalController()`). Returns the locally-owned PC reliably.
Falls back to nullptr on dedicated server.

All callers (`getPawn()`, `m_localPC`/`m_localPawn` caching, hook guards, char-load detection)
inherit the fix automatically.

## Server-fly sweep (v6.3.5)

Listen-server host sweeps `FindAllOf("BP_FGKDwarf_C")` every 2s and sets
`bIgnoreClientMovementErrorChecksAndCorrection` + `bServerAcceptClientAuthoritativePosition`
on each pawn whose `Role == ROLE_Authority`. Remote clients skip (their pawn is AutonomousProxy).

**Why:** v6.1.0 restricted these flags to local pawn only, which blocked remote clients from flying.

## Key API facts
- `bIsLocalPlayerController` — UPROPERTY on APlayerController, set at spawn, safe to read via reflection
- `Role` property — ENetRole, ROLE_Authority=3, read as uint8_t at property offset
- `ServerDebugSetItem(Item, Count)` — Server RPC on InventoryComponent, sets absolute count
- `RequestAddItem(Class, Count, Method)` — local-only, does NOT replicate to server on non-host clients
