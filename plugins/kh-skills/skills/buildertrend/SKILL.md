---
name: buildertrend
description: KH's Buildertrend-style construction job management, run by Claude over files in the KH vault — jobs, schedules, daily logs, change orders, selections & allowances, budgets/draws, punch lists, warranty. Use when the user mentions Buildertrend, starting or managing a job/build, daily logs, schedule shifts or delays, change orders, selections or allowances, budget vs. actual, draws/owner invoices, punch lists, warranty claims, subs/bids/POs, or asks for a job status report or weekly client update. Also use for questions about Buildertrend the product (pricing, features, competitors) — see references/buildertrend-research.md.
---

# KH Buildertrend (Job Hub)

Buildertrend is the construction management SaaS home builders use to run
jobs. It has no open API and costs ~$8–10k/yr, so KH runs the same playbook as
plain markdown files Claude reads and writes. Everything lives in the vault,
syncs via OneDrive, and works from any machine — same model as the Shared
Brain.

Two modes:
1. **Answer questions about Buildertrend the product** (features, pricing,
   competitors, whether KH should buy it) — read
   `references/buildertrend-research.md` and answer from it.
2. **Run KH jobs** (everything below).

## Where jobs live

```
Keller Homes Cowork/Keller Homes/Jobs/
  _pipeline.md              ← leads: one section per prospect, stage + next action
  _templates/               ← job blueprint (copied for each new job)
  <Job Name>/               ← one folder per job, e.g. "Boulder Creek"
    job.md                  ← job info: client, address, contract, dates, status
    schedule.md             ← phase/task table with predecessors + baseline/actual
    budget.md               ← cost-code table: estimate / committed / actual / variance
    selections.md           ← client decisions with allowances + deadlines
    todos.md                ← tasks + punch list
    invoices.md             ← draw schedule / owner invoices / payments received
    change-orders/          ← CO-001-<slug>.md, one file per CO
    daily-logs/             ← YYYY-MM-DD.md, one file per day
    client-updates/         ← drafted weekly updates sent to the owner
    warranty.md             ← post-closing claims
```

If `Jobs/` doesn't exist, offer to create it (with `_templates/` seeded from
`references/`). If the vault isn't found, say so — the OneDrive folder may not
be connected on this machine.

Record formats, field lists, and status lifecycles are in
`references/data-model.md`. Cost codes are in `references/cost-codes.md`.
The standard new-build schedule is in `references/schedule-template.md`.

## Core operations

### Start a job
Ask for (or pull from the lead in `_pipeline.md`): client name/contact,
address, contract type (fixed-price or cost-plus), contract amount, target
start. Create the job folder from the template: seed `schedule.md` from the
schedule template (compute dates from the start date), `budget.md` from the
cost codes with estimate amounts if known, `selections.md` with the standard
selection sheet and deadlines back-computed from schedule phases. Mark the
lead Sold in `_pipeline.md`. Log it to the Shared Brain.

### Daily log
Create `daily-logs/YYYY-MM-DD.md`: what happened, who was on site, weather
(ask or note "not recorded"), photos referenced by path if any, delays or
issues flagged. Never skip a delay — daily logs are the evidentiary record.
If the log reveals a schedule slip, offer to shift the schedule.

### Run the schedule
`schedule.md` tasks have predecessors. When a task slips, cascade: move every
downstream task by the same amount, keep the baseline column untouched so
slippage stays visible, and list which selection deadlines moved with it.
Flag any selection now due within 14 days. Weekly, report: current phase,
days ahead/behind baseline, next 2 weeks of tasks, decisions needed.

### Change orders
Nothing extra gets built without a written, priced, client-approved CO.
Create `change-orders/CO-###-<slug>.md` with scope, line-item pricing (cost
vs. client price), schedule impact, and status **Draft**. Draft the message
sending it to the client. Track status: Draft → Sent → Approved / Declined
(record the date and how approval was given — email, text, signed doc).
On approval, add the amount to `budget.md` and `invoices.md`.

### Selections & allowances
Each selection has an allowance, a deadline tied to a schedule task (e.g.
"tile: 14 days before Tile Install"), and choices. When the client picks,
record the price vs. allowance; overages roll into the budget and next
invoice (or a CO if large). Chase upcoming deadlines in every status report.

### Budget & draws
`budget.md` per cost code: estimate → approved COs → committed (signed
POs/bids) → actual (paid) → variance. Update actuals when the user reports
payments. `invoices.md` holds the draw schedule; when a milestone hits,
draft the owner invoice and the cover message.

### Punch list & warranty
Punch list = checklist in `todos.md` with responsible sub per item; track to
zero before closing. After closing, `warranty.md` records claims (date,
issue, photos, responsible sub, appointment, resolution, owner sign-off).

### Gantt view ("show me the schedule / gantt")
Render the schedule as an interactive chart from
`references/gantt-template.html`: copy the template, replace the DATA block
(TITLE, SUBTITLE_NOTE, PHASES, TASKS) with the job's `schedule.md` rows —
task IDs, names, durations, predecessors, phase index; pin in-progress tasks
to their actual position with the startOverride field. Save it as
`<Job Name>/gantt.html` in the job folder (so it syncs to every device via
OneDrive) and send it to the user rendered. Works on phones — it's a
standalone HTML file, dark-mode aware, tappable rows.

### Job Hub app ("refresh the job hub / update my app")
The KH Job Hub is a phone-installable web app deployed as a private Claude
Artifact at:

`https://claude.ai/code/artifact/dc72da42-256d-4488-b358-7b801dd7a49e`

To refresh it: copy `references/jobhub-template.html`, rebuild the DATA block
(`GENERATED`, `JOBS`) from every active job's files — schedule tasks with
percent-complete and start overrides for in-progress work, budget divisions
(estimate/revised/committed/actual), selections with deadlines in working
days, change orders, the 2–3 latest daily logs, current working day, and
schedule delta vs. baseline — then redeploy with the Artifact tool passing
that same `url` so the user's home-screen icon keeps working (keep favicon
🏗️ and the `<title>` unchanged). Dollar figures come from the job files
only; never estimate them. Refresh after meaningful job events or whenever
asked.

### Status report ("how are my jobs doing")
Read every active job's `job.md`, `schedule.md`, `budget.md`, and latest
daily log. Report per job: phase, schedule vs. baseline, budget variance,
open COs, selections due, blockers. Lead with anything needing a decision.

### Weekly client update
Draft from the week's daily logs + schedule: what happened, what's next,
decisions needed (selections due, COs awaiting approval), one honest note on
schedule. Save to `client-updates/YYYY-MM-DD.md` for the user to send —
never send directly to a client without being asked.

## Rules

- **Money accuracy beats speed.** Never invent amounts, dates, or approval
  status. If a figure is unknown, write `TBD` and ask.
- **COs before work.** If the user describes extra work with no CO, push to
  create one before anything else.
- **Baselines are immutable** — schedule and budget baselines stay put so
  variance is always visible.
- **Client-facing text is drafted, not sent.** The user sends it.
- **No secrets in job files** (they sync via OneDrive and feed Gary): no full
  account numbers, SSNs, or lender credentials. Contract amounts are fine.
- **Log to the Shared Brain** (per the `brain` skill) when a job starts,
  a CO is approved, a draw goes out, or a job closes.
