# Grilling — v2: naming the destination, round 2

**Effort:** v2 of the AI-Dev-Survey. **No ticket yet** — this round finishes naming the destination, then the map gets charted.
**Previous round:** `docs/grilling/v2-destination.md` (round 1 — the four scope questions).
**Round:** 2 of ? — four questions, each unblocked by a round-1 answer. Everything still open after this is either a ticket or fog.
**How to use:** answer inline under each `### Your answer` heading. Free text is fine.

---

## What round 1 settled

- **v1 is dead.** Complete replacement, nobody else answers it. **Item keys are free** — v2 can rewrite any wording at no migration cost.
- **`scoring/scoring.xlsx` dies**, and `scripts/make-scoring-xlsx.mjs` with it. The **raw Forms export is the input**: drop the `.xlsx` in the folder, Python picks it up, serves the dashboard. Simple and clean.
- **The team section gets new, genuinely team-oriented Dimensions** — team-level principles, and how developers interact with AI while interacting with *each other*. The seven v1 Dimensions do not carry over to it.
- **The Stance gap is dead**, and the norm gap with it. This is the deliberate cost of the line above, not an oversight.
- **The team Coverage pass is cut.** Coverage is two passes: today, and me in six months.
- **The team section is single-pass** — "what it should be", not a now/future pair.

## What I looked up

- **Your uploaded export is the raw Forms output**, not a scored file: `A1:FA2` — **157 columns × 1 response**, built-ins first (`ID`, `Start time`, `Completion time`, `Email`, `Name`, `Last modified time`), then one column per Likert statement, headed by the statement text. It matches the 157-column Responses sheet the Excel workbook expected. **So Python inherits the whole job**: label→number lookup, `N/A`, reverse keys, facet means, Gaps, Coverage medians, Edge markers, Levers, Pattern flags. Everything in `scoring/scoring-rules.md` becomes code.
- ⚠️ **That file is named personal data in a public repo.** It has never been committed — I checked all history — but `.gitignore` only covered `scoring/*.csv`, so nothing was stopping it. I've added `Excel Example/` and `*.xlsx` to `.gitignore` (uncommitted, like everything else). **Q4 below asks where real exports should live**, because your new workflow puts one in that folder every time you run the app.
- **Everything the team section touches, by count:** dropping the mirrored stance rows (30), the team Coverage pass (19) and the team Safeguard question takes **~49 answers** out of 152, before the new team block adds any back.

## What I'm assuming unless you say otherwise

- The **manager boundary survives unchanged**: individual results stay internal and named; the manager sees a combined, unnamed team view, as a rendering and never as a file.
- The **Current-state section is untouched** — 26 items, exactly as they are.
- The **dashboard's visual design is untouched**. Only how it is fed and launched changes.

---

## Q1 — Does the six-month Horizon survive for the *personal* section? *(prerequisite — three of the next four questions hang on it)*

### What this is

Your Q4 answer said: *"I don't want to have a section that's in six months. I just want to have a section about what it should be or what each person wants it to be, not necessarily where it is now and where it is in six months."*

I read that as scoped to the **team** section. But it can be read wider, and the difference is the whole instrument.

### Why it matters

**Gap** — Future minus Current — is v1's core measurement, and it only exists because the personal side asks the same person twice. Kill the personal six-month pass and there is no Gap, no Coverage Gap, no Lever (which is derived by subtracting current safeguards from future ones). v2 becomes a **snapshot**: where everyone is, plus what they think the team should do. That is a legitimate and much shorter instrument — but it is not the one v1 was.

Against that: in the pilot you said the "me in six months" block *felt repetitive* and you wanted it **shortened and sharpened**, not removed. Those are different asks, and I don't want to guess which one you meant.

### Options

| Option | Pros | Cons |
|---|---|---|
| **A. Keep six months for personal only** — today + me in six months; team section is single-pass | Gap, Coverage Gap and Levers all survive. Matches what you said in the pilot. Cuts only the team's future pass. | The personal future block is still a second pass over the same Dimensions — the repetition you flagged is reduced, not removed. |
| **B. Drop six months everywhere** — one personal pass (today), one team pass (what it should be) | Shortest survey by far. Zero repetition anywhere. Very clean. | **Gap dies entirely.** No movement is measured — you learn where people are and what they want for the team, never the distance they intend to travel. |
| **C. Keep six months, but only on Coverage** — the 19-row grid twice, Dimension items once | Keeps concrete, area-level movement, drops abstract movement. Big row saving. | Two different logics in one survey; the Rubric has to explain why some things have a Gap and others don't. |

### My recommendation

**A.** The pilot said the personal future block was *repetitive*, and the fix you asked for was fewer, sharper items — that is Q3-of-round-3 territory, not a reason to delete the pass. Gap is what turns this from a census into a direction, and B throws it away to solve a problem A already solves.

But if what you actually want is a short, sharp snapshot, say **B** — it makes v2 dramatically smaller and I'd rather build the thing you want than defend v1's design.

### Your answer

: I think I want to phrase this a little differently. Ultimately, I still want the answers, as in, where do they think they'll be in six months? I think re-asking the same questions, they're going to give the same answers because they have the amount of knowledge that they have now. They're probably using AI in the way they want to.

We need to reframe many of these questions to figure out their principles and values and what AI would have to do, or what development with AI would mean for them to change and use it more. I'm looking for a larger variety of questions around "If this were true, how would you feel about this?" So I don't know, maybe something we still need to workshop a little bit. Yes, I acknowledge that this will change the dashboard visualization a little bit, and that's fine. It's okay if the dashboard changes. 

<!-- Concretely: should the survey be able to tell you "Priya is at Trust 2.4 today and wants to be at 3.8"? A keeps that sentence; B removes it. -->

---

## Q2 — Is the new team section *scored*, or is it an unscored profile?

### What this is

You want new team Dimensions — team-level principles, developer-to-developer interaction with AI. The question is what the survey does with those answers.

### Why it matters

This is the largest single driver of how big the v2 map gets.

- **Scored** means each new team Dimension needs: a definition in `CONTEXT.md`, 1–5 **level text** in the rubric (the v1 equivalent, `rubric/dimension-levels.md`, is a substantial document), items, reverse keys, facet rules, and a place in the dashboard's per-topic views. That is roughly what tickets [Rubric: what 1–5 means](https://github.com/AndrewGodlewsky/AI-Dev-Survey/issues/4), [Item bank: Current-state](https://github.com/AndrewGodlewsky/AI-Dev-Survey/issues/5) and [Scoring rules](https://github.com/AndrewGodlewsky/AI-Dev-Survey/issues/9) cost the first time, redone for a new construct.
- **Unscored** means the team section works the way **Safeguard items** and **Coverage** already do: a *profile* you read, showing where people agree and where they split, with no 1–5 score and no rubric prose behind it. Much cheaper, and arguably more honest — "what should our norm be" is a vote, not a measurement.

### Options

| Option | Pros | Cons |
|---|---|---|
| **A. Scored — new Dimensions with full rubric levels** | Team results sit beside personal results in the same visual language. Comparable across future re-runs. | The most expensive option by a wide margin. Level text for a brand-new construct is hard to write well and easy to write badly. |
| **B. Unscored profile — agreement and spread, no score** | Much cheaper. Matches what the data actually is: a norm proposal, not a trait. Dashboard already knows how to render distributions. | Team topics can't be ranked "we're at 3.2 on this". No level prose to hand someone. |
| **C. Hybrid — 2–3 scored Dimensions, the rest as profile** | Scores where a scale genuinely means something; votes elsewhere. | Two logics to explain; you have to pick which is which without data. |

### My recommendation

**B — unscored profile.** "What should the team's norm be" is a position people hold, not a level they're at, and v1 already proved this project can render an unscored profile well (Coverage and Safeguards both do it). It also keeps v2 from re-walking three of v1's most expensive tickets. If a team topic later turns out to want a scale, adding one is a smaller change than removing one.

### Your answer

: I think we're gonna need for you to come up with some new dimensions, and that might have to be a grill-me issue later on in the future when we're trying to build this. Because ultimately I want to ask different types of questions at the team level But for the individual level, all the questions about how they're using AI now will remain the same. We can still use those sorts of metrics, but I do think some of the six-month questions are going to shift to be a little bit more insightful and a little bit less monotonous when answering the questions. 

<!-- Roughly how many team topics do you have in mind? Three feels like a section; ten is a survey of its own. -->

---

## Q3 — Does the Scored CSV survive?

### What this is

Round 1 killed the Excel sheet but left this open. Today `scoring/scored-csv-schema.md` defines a 293-column contract — one row per Respondent — that the sheet writes and the dashboard reads. With Python owning both ends, that seam is now optional.

### Why it matters

It is the boundary where **named data stops**. The CSV is named and internal by design; the manager gets a rendering, never the file. It's also the only durable record of a run — the raw export plus code can always regenerate it, but only if the code hasn't changed since.

### Options

| Option | Pros | Cons |
|---|---|---|
| **A. Keep it as an export** — Python computes in memory, writes the CSV on request | Durable archive; future re-runs comparable; the named/unnamed boundary stays an explicit artifact. | A schema to maintain that nothing strictly requires. |
| **B. Drop it** — Python holds everything in memory, dashboard reads from the app | Simplest possible pipeline: export in, dashboard out, nothing on disk. Matches "super simple and clean". | No archive. Re-running an old export against newer code silently gives different numbers, and you'd never know. |
| **C. Keep it, but as an internal cache** — written automatically, not a published contract | Archive without a spec to maintain. | "Not a contract" tends to become a contract the moment anything else reads it. |

### My recommendation

**A**, at a much smaller size than 293 columns. The schema was that wide because Excel had to precompute everything the dashboard couldn't; Python can compute on demand, so the CSV only needs to carry what you'd want to *read back in a year*. But keep something on disk — B means a run's results exist only as long as the code that produced them.

### Your answer

: I don't think we really need it. Maybe you can keep it as an internal cache or an export, but it's fine if we can export a CSV from the dashboard. That's okay. 

<!-- Also worth deciding: where do real exports and their outputs live? They're named data and the repo is public — a folder outside the repo entirely is the safest answer. -->

---

## Q4 — How does the dashboard get served, and does `dashboard/index.html` survive?

### What this is

You said the look is right and you don't want it changed — only how it's fed and spun up. `dashboard/index.html` is 705 lines: one self-contained file, no dependencies, that reads a CSV and renders every Slice. There are three ways to keep the look.

### Why it matters

This decides whether the dashboard work is a **port** or a **rewrite**, and that's the difference between one ticket and four.

### Options

| Option | Pros | Cons |
|---|---|---|
| **A. Keep `index.html` as-is; Python just feeds it** — the app serves the existing file and hands it data over HTTP instead of a file picker | Smallest possible change. The look is preserved *exactly*, because it's the same file. All existing rendering logic keeps working. | The HTML still contains rendering logic that arguably belongs in Python. One file stays large. |
| **B. Python renders server-side; a thin JS layer for interaction** | Logic lives in one language. HTML gets simpler. | The look has to be **rebuilt**, and "it should look the same" is much harder to hit than it sounds. Highest risk to the thing you said you liked. |
| **C. Keep `index.html` as the template, move computation to Python, leave rendering in JS** | Clean split: Python computes, JS draws. Look preserved because the drawing code is untouched. | Needs a deliberate cut line between "computed" and "drawn" — some of `index.html`'s current logic is genuinely both. |

### My recommendation

**A first, C later if it itches.** You said the pain was the *pipeline*, not the file — so fix the pipeline and leave the renderer alone. A is close to a day's work; B risks weeks and puts the one thing you were happy with back on the table. If Python ends up duplicating computation the HTML already does, that's a follow-up refactor with a working app in hand, not a precondition.

### Your answer

: Yeah, I want to go with your recommendation here. Let's use index.html as the template and create this with Python as the backend and JavaScript or something else that's simple as the frontend. I'll leave that up to you as far as architecturally choosing a frontend. I just want to be able to run it and have it show up as a local host for me, just so it's easy and simple and I can spin it up. I'm technically savvy, so it's fine if it's not perfect and requires me to run a script to start it. 

<!-- Practical: how do you want to launch it? `python app.py` and a browser opens? A `.bat` file you double-click? That shapes the packaging ticket. -->

---

## Anything else

Anything these four didn't cover — how you want the work sequenced, what should be built first, anything you'd rather I stop assuming.

### Your answer

:
