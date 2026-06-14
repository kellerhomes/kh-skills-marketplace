---
name: ask-gary
description: Send a question or task to Gary (the AnythingLLM AI on the KH server) and get the answer back, via the Gary Bridge shared folder. Use when the user says things like "ask Gary", "send this to Gary", "what does Gary think", "have Gary look at this", "check with Gary", or wants to hand a question to the server-side AI. Also use to read or update the shared context both Cowork and Gary see.
---

# Ask Gary (Cowork ⇄ Gary bridge)

Gary is the AnythingLLM AI on the KH server. Cowork and Gary can't talk
directly, so they communicate through a shared folder that the Gary Bridge
service watches. This skill drives that folder.

## Where the folder is

Inside the user's connected OneDrive folder: `KH/gary-bridge/`. It contains
`inbox/`, `outbox/`, `memory/context.md`, and `status.md`. Find it under the
connected folder root; if you can't locate it, tell the user the bridge may
not be set up yet and point them to `KH/gary-bridge/README.md`.

## To ask Gary something

1. Make a short request id, e.g. `req-YYYYMMDD-HHMMSS` (use the real date/time).
2. Write the question to `KH/gary-bridge/inbox/<id>.md` — the file's entire
   contents are the message to Gary. Plain text/markdown.
3. The bridge (running on the server) picks it up, asks Gary, and writes
   `KH/gary-bridge/outbox/<id>.response.md`. This takes a few seconds to ~a
   minute (OneDrive sync + Gary thinking).
4. Poll for the response: check for `outbox/<id>.response.md`. If it's not
   there yet, wait ~10 seconds and check again, up to ~6 times. Read it when
   it appears and relay Gary's answer to the user.
5. If after several tries there's no response, read `status.md` — if its
   heartbeat is stale, the bridge service likely isn't running on the server;
   tell the user to start `run-bridge.bat` on the server.
6. **Flow it back into the brain:** after you relay Gary's answer, append it to
   the Shared Brain so other surfaces see it next session. Prepend to
   `Keller Homes Cowork/Keller Homes/_Shared Brain/from-gary.md` (just under the
   `<!-- ... -->` marker):
   `### [YYYY-MM-DD HH:MM] Q: <the question>` then `**Gary:** <his answer>`.
   Keep it to the substance; no secrets.

## Shared memory

`memory/context.md` is sent to Gary with every request and is the common
ground both sides see. When the user wants Gary to "remember" something or
wants to update what both sides know, edit that file. Keep it concise.

## Notes

- Don't invent a response — only relay what's actually in the outbox file.
- One request file per question. Use a fresh id each time.
- This works from any machine's Cowork because the folder rides OneDrive; the
  bridge itself must be running on the server for anything to be answered.
