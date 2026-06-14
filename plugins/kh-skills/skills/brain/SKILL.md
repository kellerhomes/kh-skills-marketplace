---
name: brain
description: Read and update the KH Shared Brain — the shared page that keeps Cowork, Claude Code, and Gary in sync across machines. Use at the START of a work session to get caught up, when the user asks "what's the latest", "what's everyone working on", "sync the brain", "catch me up", "check the brain", or after finishing meaningful work to "log this" / "update the brain". Also use to leave a handoff message for Claude Code.
---

# KH Shared Brain

The Shared Brain is a set of markdown files all KH Claudes read and write so
parallel work across machines stays on the same page. It lives in the Obsidian
vault, inside the user's connected OneDrive folder:

```
Keller Homes Cowork/Keller Homes/_Shared Brain/
  STATE.md      (current picture)
  LOG.md        (history, newest at top)
  MESSAGES.md   (handoffs between surfaces)
  00 - README…  (the protocol)
```

If you can't find it, tell the user the path above and that the brain may not be
synced yet on this machine.

## At the start of work (catch up)
1. Read `STATE.md` — the current projects, focus, decisions, open questions.
2. Skim the top few entries of `LOG.md` — recent activity from other surfaces.
3. Check `MESSAGES.md` for anything addressed **to Cowork** that's unticked;
   surface it to the user.
Then briefly tell the user where things stand before doing the task.

## As you work (keep it current)
- When a real decision is made or meaningful progress happens, **prepend** a new
  entry to `LOG.md`:
  `## [YYYY-MM-DD HH:MM] Cowork @ <machine>` followed by bullets.
- Update `STATE.md` in place so it stays accurate (don't let it grow stale).
- Identify the machine (laptop / desktop / server) in your entries.

## To hand off to Claude Code
Add an entry at the top of `MESSAGES.md`:
`### [ ] <date> — from Cowork @ <machine> → to Claude Code` + the message.

## Rules
- **No secrets** in any brain file (it syncs via OneDrive and is embedded into
  Gary). Coordination and status only.
- Keep `STATE.md` short; put history in `LOG.md`.
- Only record what's true — don't invent status for other surfaces.
