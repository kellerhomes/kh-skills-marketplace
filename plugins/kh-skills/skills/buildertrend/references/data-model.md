# KH Job Hub data model

The record types, fields, and status lifecycles for KH's file-based job
system, mirroring Buildertrend's data model. Use these field lists when
creating or updating job files. `TBD` is always a legal value — never invent
data to fill a field.

## Job (`job.md`)

Fields: job name, client (name, phone, email), job address, contract type
(**Fixed Price** or **Cost Plus**), contract amount, projected start / actual
start, projected completion / actual completion, square footage, permit
numbers, PM/super, notes.

Status lifecycle: `Presale → Open → Warranty → Closed` (Buildertrend's exact
statuses). Presale = sold but not started; Open = under construction;
Warranty = closed but inside the warranty window; Closed = archived.

Also track the **Job Running Total**: contract amount + approved change
orders + selection overages (– credits). This is the live contract value and
belongs in `job.md` so it's never recomputed inconsistently.

## Lead (`_pipeline.md`, one `##` section per lead)

Fields: contact info, source (referral, website, Houzz…), project type,
estimated value, confidence %, stage, next action + date, activity log
(dated bullets of calls/emails/meetings).

Stages: `New → Contacted → Qualified → Proposal Sent → Sold / Lost`.
Sold converts to a job (Presale); keep the lead section with a pointer to
the job folder.

## Schedule item (`schedule.md`, table rows)

Columns: ID, task, phase, duration (workdays), predecessors (IDs, optional
lag like `24 FS+2` or `27 SS`), baseline start/end, current start/end,
assigned sub, status, % complete.

Status: `Scheduled → In Progress → Complete`. Milestones have zero duration.
Rules: durations count workdays only; when a task moves, shift all downstream
successors the same amount and note the reason and date in a "Shift log"
section at the bottom of the file (Buildertrend tracks who/when/why per
shift); **never edit baseline columns after the schedule is locked**.

## Daily log (`daily-logs/YYYY-MM-DD.md`)

Fields: date, weather + weather impact, crews on site (headcount per trade),
work performed, deliveries, visitors/inspections, delays (cause + time
lost), safety notes, photos (paths), share note (internal / client-shared).
Append-only — never rewrite history. One per active day; same-day entry is
the discipline that makes them count as evidence.

## To-do / punch item (`todos.md`)

Fields: task, assignee (staff or sub), priority, due date **or** linked
schedule task ± offset ("3 days before task 37"), checklist sub-items,
photos. Status: `Open → Done` (with date). Punch list = a dedicated section;
each item carries location/room, trade responsible, defect description,
photo. Punch lifecycle: `Open → Fixed → Verified`.

## Change order (`change-orders/CO-###-<slug>.md`)

Fields: CO number (sequential per job), title, scope description, line items
(cost code, description, qty, unit cost, **builder cost**, markup → **client
price**), total, schedule impact (days), approval deadline, how approved
(e-sign / email / text / verbal-confirmed-in-writing), approval date.

Status: `Draft → Sent → Approved / Declined / Expired`. On approval: add to
Job Running Total in `job.md`, add a budget line (or adjust the cost code
row) in `budget.md`, and add to the amount invoiceable in `invoices.md`.
Client price and builder cost both live in the file; only client price goes
in anything client-facing.

## Selection (`selections.md`, table rows)

Columns: item (e.g. Kitchen Countertops), category/room, allowance, deadline
(linked schedule task – lead-time days), choice made, vendor, client price,
over/(under) allowance, status, decided date.

Status: `Pending → Decided / Overdue`. Deadline = the schedule task that
consumes the selection minus procurement lead time; deadlines float when the
schedule shifts. Overages post to the budget and roll into the next invoice
(or a CO if large). Long-lead items (windows, trusses, cabinets, plumbing
fixtures) must be decided before rough-ins start.

## Purchase order / bid (`purchase-orders.md`)

PO fields: PO number, sub/vendor, scope, cost code(s), amount, status.
Status: `Draft → Sent → Accepted → Work Complete → Paid`. A sent+accepted PO
is **committed cost** in the budget; a paid PO is **actual cost**.
Bids: a section per trade package — scope, subs invited, quotes received,
awarded to whom; awarding converts to a PO row.

## Budget (`budget.md`, table rows per cost code)

Columns: cost code, description, **estimate**, **revised** (estimate ±
approved COs and selection overages), **committed** (accepted POs/bids),
**actual** (paid), **variance** (revised – actual), notes.
No lifecycle — it's a live rollup. Footer rows: totals, contract amount, Job
Running Total, projected margin. When recording a variance, note the reason
(estimating error, plan change, client change, weather, price increase —
NAHB's standard variance reasons).

## Owner invoice / draw (`invoices.md`)

Draw schedule table (Fixed Price jobs): milestone, % or amount, trigger
(e.g. "Foundation complete", "Dried-in", "Drywall complete", CO), status.
Invoice entries: number, date, amount, what it covers, status
(`Draft → Sent → Paid / Overdue`), payment date. Typical custom-build draws:
deposit at contract, foundation, dried-in/framing, drywall, trim/cabinets,
final at closing.

## Warranty claim (`warranty.md`, one `##` section per claim)

Fields: date received, category (plumbing, drywall…), description, photos,
responsible sub, service appointment (date, confirmed by client and sub),
resolution, owner sign-off date.
Status: `Submitted → Scheduled → Work Complete → Verified/Closed` (or
`Declined – not warrantable`, with the reason). Standard rhythm: 30-day and
11-month service visits.

## Cross-cutting conventions

- Every dollar and labor hour carries a cost code so estimate → PO → bill →
  budget reconcile automatically.
- Approvals always record **how** and **when** (a verbal OK gets confirmed in
  writing before it counts).
- Photos are referenced from the record they belong to (daily log, punch
  item, warranty claim) — not loose.
- Three walkthroughs: pre-drywall, blue-tape, final orientation. Photograph
  every wall/ceiling before drywall covers the MEP.
