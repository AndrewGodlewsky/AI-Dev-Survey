# AI-Dev-Survey

A survey and scoring rubric that helps a professional software team find out where it
stands on AI-assisted development — how each person works today, how they would *want* to
work, and what the team should require of itself.

## The problem it solves

People on the same team sit at very different points between "no AI for anything" and
"let agents write everything." Without numbers, that gap turns into unspoken friction.
This survey gives every team member a position on a set of independent scales, and gives
the team a way to see its spread, its average, and its appetite — per topic — so the
conversation about "how much AI, where" is grounded in data.

There is no single "AI adoption level." Each Dimension stands on its own, and the
Coverage grid uses its own 1–6 *Involvement level* scale (None → Advisor → Drafter →
Doer, reviewed → Doer, spot-checked → System-verified).

## What the survey asks

Four parts, ~122 answers, roughly 22–33 minutes. Responses are **named and shared openly**
within the team.

| Part | What it asks | Size | Scale |
|---|---|---|---|
| **Current-state** | How I work with AI today | 26 scored items | Behaviour / Attitude |
| **Coverage grid** | How involved AI is across 19 development areas — a *today* pass and a *direction* pass | 19 × 2 | Involvement level 1–6 |
| **Direction** | Concrete ways of working, and whether I would want to work that way | 20 scored + 5 probes + 2 checklists = 27 | Desirability |
| **Team** | What this team should require of itself | 24 scored + 1 checklist = 25 | Agreement |

**The Direction and Team sections ask genuinely different questions** — *would I want this*
against *should this be our rule* — rather than the same question in two voices. That is the
central change from v1, and it came out of the author's pilot.

## What it measures

- **Seven personal Dimensions** — Comfort, Trust, Fluency, Guardrails, Concern, Autonomy,
  Craft values — each scored twice: a **Current score** and a **Direction score**.
- **Gap = Direction − Current**, per Dimension. Read as **appetite minus practice, never a
  forecast**. Positive means someone wants more of it than they do today.
- **Five Team Dimensions** — Transparency, Verification, Agent latitude, Pace, Shared
  practice. Each Respondent gets a **Norm score** (the norm they would set); across the team
  the **spread is the finding**, not the mean.
- **Coverage Gap** — where someone wants AI involved, minus where it is involved today.
- **Edge markers** — five deliberately extreme *probe* items, never scored, that locate a
  position somebody has to own out loud.
- **Levers and Holds** — one eight-option Safeguard checklist asked four times with different
  stems. A **Lever** is a check you would accept but do not today; a **Hold** is a reading
  position you keep either way. Both are derived by *subtraction* — the survey never asks
  anyone what would change their mind.

Everything a Respondent reads — items, section copy, headings, option lists, scale labels — is
written to the **[Framing rule](survey/item-framing-rule.md)**: *no implied destination*, in
either direction. The survey locates; it never points.

## How it runs

1. **Take it** — each team member answers in Microsoft Forms.
2. **Score it** — drop the raw `.xlsx` export in a folder and run the local Python app. *(v2,
   in design — [#26](https://github.com/AndrewGodlewsky/AI-Dev-Survey/issues/26). It replaces
   v1's Excel sheet entirely.)*
3. **Read it** — the app serves the dashboard on `localhost`. The one-page
   [How to read the results](docs/HOW-TO-READ.md) explains what a big Gap or a wide spread
   means, and which readings are softer than they look.

## What v2 changed, and why

v1 was built end to end and piloted by the author. It works, and it is **not** being run on the
team — the pilot found enough structural problems that v2 replaces it in place. v1 is a
reference, not a base to extend.

**What the pilot kept, verbatim:** the Current-state section (*"the part that worked"*) and the
Coverage grid's today pass. Both are frozen.

**What the pilot broke, and what replaced it:**

| v1 | The problem | v2 |
|---|---|---|
| A *Future-state* section asking *"In six months, I would…"* | *"I don't know what I'll think in six months, because if I knew, I would be thinking that now."* People answered a forecast from the present. | The **Direction section** — concrete present-tense worlds, asked as *would you want to work this way*. No item contains the words *six months*; the horizon is named once, in the section description. |
| Every question asked twice — *for me* and *the team should* | *"Re-answering all the questions just in a slightly different frame of mind."* 152 answers, most of them duplicated. | The **Team section** asks different questions entirely, once, on five new Team Dimensions. **Stance, the Stance gap and the norm gap are deleted** — an accepted cost, not an oversight. |
| A *non-leading rule* banning one sentence shape | It banned a shape, not a lean. Items and copy could still point. | The **[Framing rule](survey/item-framing-rule.md)** — no implied destination, symmetric, governing everything the Respondent reads. Five item forms, a five-check test, a balance floor per block. |
| A Safeguard list with one way to read and six ways not to | The option count itself said which side was normal. | A **symmetric eight-option list**, interleaved, identical across all four askings — which is what makes Levers and **Holds** computable. |
| An Excel sheet with 5,224 formulas, feeding a self-contained HTML file from disk | *"Very, very clunky."* Paste, delete surplus rows, save as CSV UTF-8, drop on an HTML file. | A **local Python app** that reads the raw Forms export and serves the dashboard on `localhost`. The dashboard itself is simplified to the **five-questions** page (`dashboard/prototype-simple.html`), light-themed only — v1's `index.html` layout was "far too busy" and is retired with the sheet. |

**The items themselves were settled on 2026-08-30** by
[Team item bank](https://github.com/AndrewGodlewsky/AI-Dev-Survey/issues/31) and
[Direction item bank](https://github.com/AndrewGodlewsky/AI-Dev-Survey/issues/32) — thirteen
judgement calls, all resolved, no item text left open. Three of them accepted a known weakness
rather than engineering it away, and those are caveats the results must be read with:

- **Fluency's two Direction items sit on adjacent axes.** If they never diverge, the Dimension
  is one item doubled. Flagged as the most likely to need a third item after the pilot.
- **Agent latitude nets two facets running opposite ways** (*Parallel development* vs *Limits*),
  so **a flat 3 there is ambiguous by construction**. Its facet view is the primary read.
- **Three Gaps are facet-matched rather than word-matched** — Fluency, Autonomy, and Concern's
  job-impact facet — and read softer than the other four, on top of every Gap already being the
  softer kind.

📄 **[The v2 item banks, explained](docs/v2-item-banks-explained.md)** — what those two tickets
settled, in plain language, and how it changes the rest of the project. Start there if you want
the *why* behind the survey's current shape.

**Getting started:** open [`docs/SETUP.html`](docs/SETUP.html) in a browser — the step-by-step
runbook for building the form, piloting it, exporting responses and reading the results.
⚠️ **It documents the v1 pipeline** (Excel sheet → scored CSV → HTML file) and is rewritten once
the local app lands.

## Repository layout

| Path | What it is |
|---|---|
| `CONTEXT.md` | Domain glossary — the vocabulary everything else uses. **Read it first.** |
| `survey/` | The survey text. See the file map below. |
| `rubric/` | `RUBRIC.md` — what each score means, and how answers become scores. Being rewritten for v2 ([#33](https://github.com/AndrewGodlewsky/AI-Dev-Survey/issues/33), [#30](https://github.com/AndrewGodlewsky/AI-Dev-Survey/issues/30)). |
| `scoring/` | v1's Excel sheet and scoring rules. **Retired once the Python app scores** — a reference, not something to extend. |
| `dashboard/` | `index.html` — v1's self-contained dashboard (reference). `prototype-simple.html` — the **five-questions** page, v2's rendering template (light-only). |
| `app/` | The local Python app. *Does not exist yet* — [#26](https://github.com/AndrewGodlewsky/AI-Dev-Survey/issues/26). |
| `docs/` | `HOW-TO-READ.md` (results guide), `SETUP.html` (v1 runbook), `v2-item-banks-explained.md`, `adr/` (decision records), `agents/` (agent configuration), `grilling/` (the working behind every decision). |
| `scripts/` | Repo upkeep, e.g. `update-readme.py`, which regenerates the progress block below. |

**Inside `survey/` — the v2 files that matter:**

| File | What it holds |
|---|---|
| `item-framing-rule.md` | **The rule every item and every line of copy obeys.** Binding; backed by `docs/adr/0001`. |
| `current-state-items.md` | The 26 frozen items. Not to be reopened. |
| `coverage-grid.md` | 19 development areas, today pass + direction pass. |
| `direction-section.md` / `direction-items.md` | The spec, then the 20 items + 5 probes + 2 checklist askings. |
| `team-section.md` / `team-items.md` | The spec, then the 24 items + the checklist. |
| `probe-items.md` / `safeguard-items.md` | The probe and checklist *rules*; both partly superseded by the two section files above, with banners saying which parts. |
| `SURVEY.md` | v1's assembled document. The v2 assembly is [#29](https://github.com/AndrewGodlewsky/AI-Dev-Survey/issues/29). |

## How the project is being built

Design decisions are worked through one at a time as GitHub issues under a wayfinder
map — [Map v2](https://github.com/AndrewGodlewsky/AI-Dev-Survey/issues/21) is live;
[the v1 map](https://github.com/AndrewGodlewsky/AI-Dev-Survey/issues/1) is complete. Each ticket
resolves one question (a decision, a draft to react to, or a piece of research); its
answer lives in the issue's resolution comment and is indexed on the map. The block below
is regenerated from GitHub whenever a ticket is closed — run
`python scripts/update-readme.py --force` to refresh it by hand.

<!-- progress:start -->

**Map progress:** 27 of 32 tickets resolved.

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
- [Local app: architecture, launch, and how index.html is fed](https://github.com/AndrewGodlewsky/AI-Dev-Survey/issues/26)
- [Report identity, and where real exports live](https://github.com/AndrewGodlewsky/AI-Dev-Survey/issues/27)
- [Team item bank](https://github.com/AndrewGodlewsky/AI-Dev-Survey/issues/31)
- [Direction item bank](https://github.com/AndrewGodlewsky/AI-Dev-Survey/issues/32)

### Still open

- [Scoring rules v2: what survives the Stance gap](https://github.com/AndrewGodlewsky/AI-Dev-Survey/issues/28) _(grilling)_
- [Assemble the v2 survey document](https://github.com/AndrewGodlewsky/AI-Dev-Survey/issues/29) _(task)_
- [Team Dimension rubric levels](https://github.com/AndrewGodlewsky/AI-Dev-Survey/issues/30) _(task)_
- [Rubric v2: personal side](https://github.com/AndrewGodlewsky/AI-Dev-Survey/issues/33) _(task)_
- [Build the five-questions dashboard on real data](https://github.com/AndrewGodlewsky/AI-Dev-Survey/issues/34) _(task)_

<!-- progress:end -->

## Status

v1 is built end to end and was piloted by the author (one response). **It is not being run on
the team** — v2 replaces it, and nobody outside the author ever answers v1.

**v2, as of 2026-08-30:** the survey is **fully written**. Every item, section description and
checklist stem now exists — the Current-state section and Coverage grid today pass frozen from
v1, the Direction and Team sections settled by
[#31](https://github.com/AndrewGodlewsky/AI-Dev-Survey/issues/31) and
[#32](https://github.com/AndrewGodlewsky/AI-Dev-Survey/issues/32).

What remains is everything downstream of the words: assembling the document, writing the rubric
levels, specifying the scoring, and building the local app. Six tickets, all unblocked — see
*Still open* above.
