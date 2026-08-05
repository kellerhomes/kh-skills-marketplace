# KH Job Hub — server

Hosts the Job Hub on the KH server so schedule edits are **shared** — a trade
dragged on one phone is what everyone sees — and job data updates without any
redeploy.

## What's in here

```
server/
  run-jobhub.bat     ← double-click this on the server (Windows)
  server.js          ← the server (plain Node, no npm install)
  server.py          ← fallback if Node isn't installed (plain Python)
  jobs.json          ← the job data the app shows (edit this to update jobs)
  edits.json         ← created automatically; shared drag/drop schedule edits
  public/index.html  ← the app
```

## Set up (once, on the server)

1. Copy this whole `server` folder somewhere permanent on the server.
   **Best spot: inside the OneDrive KH folder** (e.g. `KH\jobhub\`) — then
   `jobs.json` syncs to every machine and any Claude (Cowork, Code, this
   phone app) reads and writes the same data.
2. Double-click **run-jobhub.bat**. It uses Node if installed, else Python.
   (Neither installed? Install Node LTS from nodejs.org — one click, defaults.)
3. The window prints two addresses. On your phone (same Wi-Fi), open the
   `http://<network-ip>:8787` one → Share → **Add to Home Screen**.

## Keep it running

- Leave the window open, or set it to start automatically:
  Task Scheduler → Create Basic Task → At startup →
  Start a program → `run-jobhub.bat` (in its folder).
- Away from the office/home Wi-Fi the app won't load (it's LAN-only).
  Two options: install **Tailscale** on the server + phones (free, ~5 min,
  gives you a private address that works anywhere), or keep using the
  Claude artifact URL as the away-from-network fallback.

## Updating job data

`jobs.json` is the single source of truth the server reads **live** — save the
file and reload the app; no restart needed. Ask Claude (Cowork or Claude Code
on any synced machine) to update it: new jobs, schedule changes, budgets,
selections. The format is the same `JOBS` array documented in
`references/jobhub-template.html`.

`edits.json` holds field drag/drop edits from the app. To make them permanent,
ask Claude to fold `edits.json` into `jobs.json` and clear it.

## Notes

- No login: anyone on your network (or tailnet) can open it. Fine for
  schedules; think before adding client financials if the Wi-Fi is shared.
- Change the port by setting the `PORT` environment variable.
