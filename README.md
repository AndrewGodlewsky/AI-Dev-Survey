# AI-Dev-Survey

A survey and scoring rubric that helps a professional software team find out where it
stands on AI-assisted development — today and where it wants to be in six months — both
as individuals and as a team.

## The problem it solves

People on the same team sit at very different points between "no AI for anything" and
"let agents write everything." Without numbers, that gap turns into unspoken friction.
This survey gives every team member a position on a set of independent scales, and gives
the team a way to see its spread, its average, and its desired direction — per topic —
so the conversation about "how much AI, where" is grounded in data.

## How it works

1. **Take the survey** — each team member answers it in Microsoft Forms (responses are
   named and shared openly within the team). It has a *Current-state* section, a
   *Future-state* section (answered twice: "for me" and "the team should"), and a
   *Coverage grid* rating AI involvement across 19 development areas.
2. **Score it** — export the Forms responses into the Excel scoring sheet, which turns raw
   answers into 1–5 scores per **Dimension** (Comfort, Trust, Fluency, Guardrails,
   Concern, Autonomy, Craft values) and a per-area **Coverage profile**, for each person
   and for the team.
3. **Read it** — open the HTML dashboard on the scored CSV to see every slice: per
   dimension, per development area, current vs. future, personal vs. team, and per person.

> **v2 is being designed** and replaces v1 in place. What the author's pilot kept: the
> Current-state section and the "today" Coverage grid, verbatim. What changes: the
> future block asks about *direction* rather than predicting a six-month state; the
> mirrored "the team should" pass is replaced by a **Team section** — asked once, in team
> voice, scored on five new Team Dimensions (Transparency, Verification, Agent latitude,
> Pace, Shared practice; `survey/team-section.md`); every item is written to the
> **Framing rule** (`survey/item-framing-rule.md`); and scoring moves from the Excel
> sheet into a local Python app that reads the raw Forms export and serves the dashboard.
   The one-page *How to read the results* explains what a big gap or a wide spread means.

There is no single "AI adoption level." Each dimension stands on its own, and the
Coverage grid uses its own 1–6 *Involvement level* scale (None → Advisor → Drafter →
Doer, reviewed → Doer, spot-checked → System-verified).

**Getting started:** open [`docs/SETUP.html`](docs/SETUP.html) in a browser. It is the
step-by-step runbook — building the form in Microsoft Forms, piloting it, exporting the
responses, loading them into the scoring sheet, saving the scored CSV, and opening it in
the dashboard — with a troubleshooting table and a file map.

## Repository layout

| Path | What it is |
|---|---|
| `CONTEXT.md` | Domain glossary — the vocabulary everything else uses. Read it first. |
| `survey/` | The survey text (sections, items, Coverage grid). |
| `rubric/` | The rubric: what each score means and how answers become scores. |
| `scoring/` | Excel scoring sheet (formulas only, no macros). |
| `dashboard/` | Single-file HTML dashboard; opens from disk, loads the scored CSV. |
| `docs/` | `SETUP.html` (the setup and results runbook), `HOW-TO-READ.md` (the results guide), agent configuration (`docs/agents/`), grilling records and research. |
| `scripts/` | Repo upkeep, e.g. `update-readme.py`. |

## How the project is being built

Design decisions are worked through one at a time as GitHub issues under a wayfinder
map — [Map v2](https://github.com/AndrewGodlewsky/AI-Dev-Survey/issues/21) is live;
[the v1 map](https://github.com/AndrewGodlewsky/AI-Dev-Survey/issues/1) is complete. Each ticket
resolves one question (a decision, a draft to react to, or a piece of research); its
answer lives in the issue's resolution comment and is indexed on the map. The block below
is regenerated from GitHub whenever a ticket is closed — run
`python scripts/update-readme.py --force` to refresh it by hand.

<!-- progress:start -->

**Map progress:** 23 of 31 tickets resolved.

### Deliverables

- [x] Survey document — `survey/SURVEY.md`
- [x] Coverage grid — `survey/coverage-grid.md`
- [x] Rubric — `rubric/RUBRIC.md`
- [x] Scoring sheet (Excel) — `scoring/scoring.xlsx`
- [x] Dashboard (HTML) — `dashboard/index.html`
- [x] How to read the results — `docs/HOW-TO-READ.md`

### Decided

- [Item scale semantics for Dimension items](https://github.com/AndrewGodlewsky/AI-Dev-Survey/issues/2)
- [Coverage grid: Involvement level anchor text per Development area](https://github.com/AndrewGodlewsky/AI-Dev-Survey/issues/3)
- [Rubric: what 1–5 means in words for each Dimension](https://github.com/AndrewGodlewsky/AI-Dev-Survey/issues/4)
- [Item bank: Current-state section](https://github.com/AndrewGodlewsky/AI-Dev-Survey/issues/5)
- [Item bank: Future-state section (Personal + Team stance)](https://github.com/AndrewGodlewsky/AI-Dev-Survey/issues/6)
- [Context items: which Respondent attributes to collect](https://github.com/AndrewGodlewsky/AI-Dev-Survey/issues/7)
- [Probe items: definition, count and scoring rule](https://github.com/AndrewGodlewsky/AI-Dev-Survey/issues/8)
- [Scoring rules: items → Dimension scores, grid → Coverage profile, gaps](https://github.com/AndrewGodlewsky/AI-Dev-Survey/issues/9)
- [Microsoft Forms export: column layout for Likert and grid questions](https://github.com/AndrewGodlewsky/AI-Dev-Survey/issues/10)
- [Dashboard prototype: the Slices and the Layered view with fake data](https://github.com/AndrewGodlewsky/AI-Dev-Survey/issues/11)
- [Scored CSV schema: the contract between the Scoring sheet and the dashboard](https://github.com/AndrewGodlewsky/AI-Dev-Survey/issues/12)
- [Assemble the Survey document](https://github.com/AndrewGodlewsky/AI-Dev-Survey/issues/13)
- [Assemble the Rubric document](https://github.com/AndrewGodlewsky/AI-Dev-Survey/issues/14)
- [Build the Excel Scoring sheet](https://github.com/AndrewGodlewsky/AI-Dev-Survey/issues/15)
- [Build the HTML dashboard](https://github.com/AndrewGodlewsky/AI-Dev-Survey/issues/16)
- [Write the one-page 'How to read the results'](https://github.com/AndrewGodlewsky/AI-Dev-Survey/issues/17)
- [Pilot the survey with 1–2 people](https://github.com/AndrewGodlewsky/AI-Dev-Survey/issues/18)
- [Conditional items: locating where a Respondent's line moves](https://github.com/AndrewGodlewsky/AI-Dev-Survey/issues/19)
- [Straight-lining: does the survey need attention checks, and where?](https://github.com/AndrewGodlewsky/AI-Dev-Survey/issues/20)
- [Item framing rule: what replaces the non-leading rule](https://github.com/AndrewGodlewsky/AI-Dev-Survey/issues/22)
- [Team section: what it measures, and is it scored](https://github.com/AndrewGodlewsky/AI-Dev-Survey/issues/23)
- [Forward personal block: from prediction to direction](https://github.com/AndrewGodlewsky/AI-Dev-Survey/issues/24)
- [Coverage grid: what replaces the six-month pass](https://github.com/AndrewGodlewsky/AI-Dev-Survey/issues/25)

### Still open

- [Local app: architecture, launch, and how index.html is fed](https://github.com/AndrewGodlewsky/AI-Dev-Survey/issues/26) _(prototype)_
- [Report identity, and where real exports live](https://github.com/AndrewGodlewsky/AI-Dev-Survey/issues/27) _(grilling)_
- [Scoring rules v2: what survives the Stance gap](https://github.com/AndrewGodlewsky/AI-Dev-Survey/issues/28) _(grilling)_
- [Assemble the v2 survey document](https://github.com/AndrewGodlewsky/AI-Dev-Survey/issues/29) _(task)_
- [Team Dimension rubric levels](https://github.com/AndrewGodlewsky/AI-Dev-Survey/issues/30) _(task)_
- [Team item bank](https://github.com/AndrewGodlewsky/AI-Dev-Survey/issues/31) _(prototype)_
- [Direction item bank](https://github.com/AndrewGodlewsky/AI-Dev-Survey/issues/32) _(prototype)_
- [Rubric v2: personal side](https://github.com/AndrewGodlewsky/AI-Dev-Survey/issues/33) _(task)_

<!-- progress:end -->

## Status

v1 is built end to end and was piloted by the author (one response). It is not being run
on the team; v2 — the survey overhaul and the local Python app — is being designed on
Map v2 and replaces it.
