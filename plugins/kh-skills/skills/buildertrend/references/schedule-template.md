# KH new-construction schedule template

Standard custom single-family build: ~155–185 working days (~8–9 months)
permit-to-closing. Durations are **working days**; predecessors are task IDs
(finish-to-start unless noted: `SS` = start-to-start, `+n` = lag days).
Milestones have zero duration and mark the draw schedule.

To seed a job's `schedule.md`: copy this table, compute dates from the job's
start date (skip weekends/holidays), copy baseline = current dates, and lock
the baseline. Adjust durations to the job — this is a starting point, not
gospel.

| ID | Task | Dur | Pred |
|---|---|---|---|
| **Phase 0 — Pre-Construction** | | | |
| 1 | Final plans, specs, engineering | 15 | — |
| 2 | Contract signed / estimate approved | 0 | 1 |
| 3 | Permit application and review | 20 | 2 |
| 4 | Survey and stake lot | 2 | 2 |
| 5 | Order long-lead items (windows, trusses, cabinets) | 1 | 2 |
| 6 | **MILESTONE: Building permit issued** | 0 | 3 |
| **Phase 1 — Sitework & Foundation** | | | |
| 7 | Temp utilities, erosion control, portable toilet | 2 | 6 |
| 8 | Clear and rough-grade lot | 3 | 6,4 |
| 9 | Excavate foundation | 3 | 8,7 |
| 10 | Form and pour footings | 3 | 9 |
| 11 | Footing inspection | 1 | 10 |
| 12 | Foundation walls | 5 | 11 |
| 13 | Waterproofing, foundation drains, termite treat | 2 | 12 |
| 14 | Foundation inspection; backfill | 2 | 13 |
| 15 | Underslab plumbing rough + inspection | 3 | 12 |
| 16 | Pour basement/garage slabs | 2 | 15,14 |
| 17 | **MILESTONE: Foundation complete (draw)** | 0 | 16 |
| **Phase 2 — Framing & Dry-In** | | | |
| 18 | Frame floor system | 4 | 17 |
| 19 | Frame walls | 8 | 18 |
| 20 | Set roof trusses / frame roof | 5 | 19 |
| 21 | Sheathing, house wrap | 3 | 20 |
| 22 | Install windows and exterior doors | 3 | 21 |
| 23 | Roofing | 5 | 21 |
| 24 | Framing inspection | 1 | 22,23 |
| 25 | **MILESTONE: Dried-in (draw)** | 0 | 24 |
| **Phase 3 — Rough-Ins** | | | |
| 26 | HVAC rough-in (ducts first — largest runs) | 5 | 25 |
| 27 | Plumbing top-out rough-in | 5 | 26 SS+2 |
| 28 | Electrical rough-in | 5 | 27 |
| 29 | Low-voltage / security / AV rough | 2 | 28 SS |
| 30 | Fireplace, tubs/showers set | 2 | 27 |
| 31 | Rough inspections (plumb, mech, elec, framing) | 2 | 26,27,28,29,30 |
| 32 | Exterior siding / masonry / exterior trim | 10 | 23 |
| 33 | Exterior paint | 4 | 32 |
| 34 | **MILESTONE: Rough inspections passed** | 0 | 31 |
| **Phase 4 — Insulation & Drywall** | | | |
| 35 | Insulation + air-seal | 3 | 34 |
| 36 | Insulation inspection | 1 | 35 |
| 37 | Hang drywall | 4 | 36 |
| 38 | Tape, mud, sand | 7 | 37 |
| 39 | Texture / prime | 2 | 38 |
| 40 | **MILESTONE: Drywall complete (draw)** | 0 | 39 |
| **Phase 5 — Interior Finishes** | | | |
| 41 | Interior trim: doors, base, casing, stairs | 7 | 40 |
| 42 | Paint interior (1st pass) | 5 | 41 |
| 43 | Install cabinets and vanities | 4 | 42 |
| 44 | Template, fabricate, install countertops | 8 | 43 |
| 45 | Tile (baths, backsplash) | 6 | 42 |
| 46 | Hardwood flooring | 4 | 42 |
| 47 | Finish plumbing | 3 | 44,45 |
| 48 | Finish electrical | 3 | 44 |
| 49 | Finish HVAC + startup | 2 | 48 SS |
| 50 | Appliances | 1 | 44,48 |
| 51 | Carpet | 2 | 42,41 |
| 52 | Paint touch-up / final coat | 3 | 47,48,50,51 |
| 53 | Mirrors, shower doors, accessories, hardware | 2 | 52 |
| **Phase 6 — Exterior Completion** (parallel with Phase 5) | | | |
| 54 | Garage doors | 1 | 33 |
| 55 | Driveway, walks, patios | 4 | 33 |
| 56 | Final grade, landscaping, irrigation | 6 | 55 |
| 57 | Deck / porch finish | 4 | 33 |
| **Phase 7 — Completion & Closing** | | | |
| 58 | Final cleaning | 2 | 53 |
| 59 | Final MEP + building inspections | 2 | 53,56 |
| 60 | **MILESTONE: Certificate of Occupancy** | 0 | 59 |
| 61 | Builder punch walk; punch work | 5 | 58,60 |
| 62 | Client blue-tape walkthrough | 1 | 61 |
| 63 | Punch completion and verification | 4 | 62 |
| 64 | **MILESTONE: Closing / handover (final draw)** | 0 | 63 |
| 65 | Warranty period begins (30-day + 11-month visits) | 0 | 64 |

## Selection deadlines to derive from this schedule

| Selection | Must be decided by | Why |
|---|---|---|
| Windows, exterior doors, trusses | Task 5 (contract) | Long lead — ordered at contract |
| Plumbing fixtures (rough-valve models) | Before task 27 | Valves set at top-out |
| Lighting/electrical layout, appliances (specs) | Before task 28 | Boxes and circuits placed at rough |
| HVAC equipment | Before task 26 | Duct design |
| Cabinets | Before task 34 | 6–10 week lead; installed task 43 |
| Tile, hardwood, carpet | Before task 40 | Ordered before drywall completes |
| Countertops (material) | Before task 43 | Templated right after cabinets |
| Paint colors | Before task 41 | First coat follows trim |
| Plumbing/electrical finish fixtures | Before task 40 | On hand for finish trades |

## Notes

- Weather-sensitive: tasks 8–16, 23, 32–33, 55–56. Inspections (11, 14, 24,
  31, 36, 59) depend on the jurisdiction — pad 1–5 days.
- When a task slips, shift all successors and re-check the selection table —
  a schedule shift moves selection deadlines with it.
- Three walkthroughs: pre-drywall (before task 35 — photograph every
  wall/ceiling), blue-tape (task 62), final orientation at closing.
