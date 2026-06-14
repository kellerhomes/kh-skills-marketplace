---
name: resume
description: Pick up KH work where it left off on any machine. Reads the Shared Brain (STATE/LOG/MESSAGES), identifies the active project, loads any referenced deliverables, summarizes where things stand, then continues the actual work — not just a status read. Use when the user says "continue this conversation", "pick up where I left off", "resume", "continue on this machine", "where was I", "keep going on <project>", "what was I doing", or switches machines mid-task. Sibling to the `brain` skill — `brain` syncs the shared page; `resume` gets back to work.
---

# KH Resume

Lets any KH Claude — on any machine — pick up an in-flight project and keep
going, using the Shared Brain as the source of truth. The brain syncs via
OneDrive, so this works cross-machine as long as the vault is synced locally.

Brain location (Obsidian vault inside the connected OneDrive folder):

```
Keller Homes Cowork/Keller Homes/_Shared Brain/
  STATE.md      (current picture — active projects, focus, decisions, open questions)
  LOG.md        (history, newest at top)
  MESSAGES.md   (handoffs between Cowork / Claude Code / Gary)
```

If the vault isn't found, tell the user the path above and that the brain may
not be synced on this machine yet, then offer to connect the `Keller Homes
Cowork` folder.

## What to do when invoked

1. **Read `STATE.md` in full.** This is the current picture across projects.
2. **Read the top 3–5 entries of `LOG.md`** for the most recent activity and decisions.
3. **Check `MESSAGES.md`** for anything addressed **to Cowork** (or to this surface)
   that's unticked `[ ]` — surface it first.
4. **Identify the active project.** If the user named one ("keep going on Boulder
   Creek"), use it. Otherwise infer from the newest LOG entry / STATE focus. If it's
   genuinely ambiguous between two active projects, ask which one.
5. **Load referenced deliverables.** If STATE/LOG point to a playbook, doc, or file
   (e.g. a `*_responses.md` playbook, a CO batch, a cost summary), read it so you have
   the working context, not just the headline.
6. **Give a tight "here's where things stand" recap** (5–8 lines max): the project,
   the last decision, what's blocked, and the open follow-ups — then state the
   single most useful next action.
7. **Continue the work.** Don't stop at the recap — proceed on the next action (draft
   the message, build the CO, prep the agenda), confirming scope only if a real
   decision is the user's to make.

## As you work
- When a real decision is made or meaningful progress happens, **prepend** a LOG entry
  (`## [YYYY-MM-DD HH:MM] Cowork @ <machine>`) and update `STATE.md` in place — same
  protocol as the `brain` skill. Keep `STATE.md` short; history goes in `LOG.md`.
- Identify the machine (laptop / desktop / server) in entries.

## Rules
- **No secrets** in any brain file (it syncs via OneDrive and is embedded into Gary).
  Coordination and status only — never dollar-account numbers, passwords, or lender
  account IDs.
- Only record what's true. Don't invent status for other surfaces or other machines.
- Honor the project's "caution zones" if STATE lists any (e.g. don't guarantee buyer
  fund credits / interest credits before Title + lender confirm).
