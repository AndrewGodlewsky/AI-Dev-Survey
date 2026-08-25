---
label: wayfinder:map
title: Team AI-Adoption Survey & Rubric
---

## Destination

A runnable v1 of the team AI-adoption survey and its interpretation, in this repo: (1) the **Survey** document (Current-state + Future-state sections, Coverage grid, Context items, Probe items) ready to paste into Microsoft Forms; (2) the **Rubric** document; (3) the **Scoring sheet** (Excel, no VBA) that turns the Forms export into individual and Team scores and a scored CSV; (4) a self-contained **HTML dashboard** that loads the scored CSV and shows every Slice; (5) a one-page **How to read the results**. Piloted once on 1–2 people.

## Notes

- Domain glossary is `CONTEXT.md` at the repo root — read it first; challenge and update it via `/domain-modeling`.
- **Execution is in scope for this map**: `task` tickets build the artifacts, not just decide them. The user asked to "plan out and then build".
- Skills: `/grilling` for decisions, `/prototype` for item drafts and dashboard mock-ups, `/research` for the Forms export shape.
- Standing preferences: ponytail mode (lazy, fewest files); the user commits manually — never run git writes; Excel formulas only, no macros; dashboard is one HTML file, no external CDNs, runs from disk.
- Team size 5–9, named responses shared openly. Horizon = 6 months. Dimension scales keep their natural direction (Concern 5 = very concerned).
- Length: all 19 Development areas kept; accept ~35–40 minutes; 2–3 items per Dimension per section. No free-text questions; Probe items instead.
- Artifact locations (when built): `survey/`, `rubric/`, `scoring/`, `dashboard/`, `docs/`.

## Decisions so far

<!-- one line per closed ticket: [title](tickets/NNN-slug.md) — gist -->

## Not yet specified

- Whether Craft values needs a cross-view in the dashboard (e.g. Craft values vs Comfort per person) — depends on what the dashboard prototype reveals.
- Reliability checks: whether the item bank needs paired/consistency items or attention checks — depends on final length after item banks are drafted.
- Whether per-area custom anchors are needed for many areas or only a few — decided per area while drafting the grid.
- How Probe items influence a Dimension score vs. just flagging a Respondent's edge position — sharpens once Probe items are drafted (ticket 007 decides the rule; drafting may revise it).

## Out of scope

- Full workshop facilitation guide — only the one-page "how to read the results" is in scope.
- Anonymous administration — responses are named by decision.
- Hosting or collecting responses in a custom web app — Microsoft Forms is the collector.
- Longitudinal comparison (re-running the survey later and diffing) — a follow-on effort once v1 has run.
