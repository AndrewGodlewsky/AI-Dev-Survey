# Grilling — Issue #18: Pilot

**Ticket:** [Pilot the survey with 1–2 people](https://github.com/AndrewGodlewsky/AI-Dev-Survey/issues/18)
**Round:** 1 of ? — what the pilot actually showed, how it felt to answer, and what you want to change before the team sees it
**How to use:** answer inline under each `### Your answer` heading. Free text is fine; you don't have to pick one of the listed options. This is a *quick* round — short answers are enough; I'll read them back and only go deeper where something needs it.

---

## What is already settled, and what I looked up

**Settled elsewhere and not re-asked here:**

- The pilot recipe is the comment on #18: build the form from `survey/SURVEY.md` Appendix A → four pre-flight checks on a throwaway form → 1–2 people take it and time each section → Responses → Excel → paste over `scoring/scoring.xlsx` Responses → Export → CSV UTF-8 → drop on `dashboard/index.html`.
- **Item text is the database key.** Wording changes go in `survey/SURVEY.md` first and only there; the Scoring sheet's `Items!F` column must match it. A wording fix is cheap; a *structural* change (dropping or adding items, changing a scale) reopens the bank decisions (#5, #6) and the sheet generator (`scripts/make-scoring-xlsx.mjs`).
- #6 left a **10-row reduction** available and *deliberately declined* it "until the pilot shows which item pairs never diverge". That decision comes due here.
- The watch-list from the banks: **C1/C2, T1/T3, A1/A3** for pairs that never diverge; **N5** (job impact) for guarded answers; **FF3/FV2** for flooring; whether the **section-3 grid description** gets read.
- One patch of fog waits on this ticket: whether the Safeguard team-stance row is enough on its own to draft a written team norm, or whether that needs a session after the results land.

**What I could not look up:** anything about the pilot itself. There is no export in the working tree (`.gitignore` excludes real exports by design), so everything below starts from what you tell me.

---

## Q1 — What actually ran? *(prerequisite — the rest of the round hangs on this)*

### What this is

Which steps of the recipe happened, by whom, and how far the round-trip got. Be concrete: "I built the form and took it myself, no export yet" is a perfectly good answer.

### Why it matters

The ticket closes when the pilot **round-trips cleanly** — form → export → sheet → CSV → dashboard. If only the *taking* has happened, the remaining steps are the next concrete work, not a decision; if the export happened and something failed to match, that is the most valuable finding this ticket can produce and I want to see the exact header or cell.

### Options

| Option | Pros | Cons |
|---|---|---|
| **A. Full round-trip** — form built, pre-flight done, taken, exported, scored, dashboard loaded | Ticket is essentially done; the round is about findings. | — |
| **B. Form built and taken, no export/scoring yet** | The experience findings are real; the mechanics are still untested. | Round-trip risk (header matching, Required-per-statement) still open. |
| **C. Read through / answered on paper or in the Markdown, no Forms form** | Cheapest possible read of the *items*. | Says nothing about Forms length, timing, or export. |

### My recommendation

Tell me which, plus: who took it (you alone / you + one other), whether the **Required-per-statement** pre-flight check was run and what it showed, and — if the export happened — whether the sheet produced any `#N/A` or any Pattern flag.

### Your answer

: I ended up doing the full round trip. I did it all, and it worked totally fine. 

<!-- If the export exists, paste the headers that failed to match (if any) and the dashboard's "n of roster_n" line. -->

---

## Q2 — Time and fatigue: where did it drag?

### What this is

Elapsed time overall and per section if you have it, and *where* you noticed yourself stalling or switching to autopilot. The survey is 152 answers in 11 sections; the estimate was 35–40 minutes.

### Why it matters

Two decisions come due on this answer. (1) #6's declined **10-row reduction**: if a block visibly dragged, that's the case for taking it now. (2) #20's Pattern flags exist because of fatigue — if you caught *yourself* block-copying the Team block from the Me block, that's a design signal, not a personal failing, and it argues for reordering or cutting more than for detecting.

### Options

| Option | Pros | Cons |
|---|---|---|
| **A. Within estimate, no real drag** — keep 152 rows | Nothing to change; keeps every facet. | — |
| **B. A specific block dragged** — take the 10-row cut *in that block* | Targeted; the cut was already designed. | Needs the never-diverging pairs (Q4) to pick which rows. |
| **C. Whole thing too long** — cut deeper than 10 rows | Team will actually finish it. | Reopens the bank decisions; Dimension bundles (Concern, Guardrails) resist sampling by design. |

### My recommendation

Answer with numbers where you have them and the *one* place it dragged most. My prior is **B** — the two 30-row Future blocks are the obvious candidates — but I don't want to lead you on that.

### Your answer

: Ultimately, here's how I felt taking the survey. The team part of the survey didn't really make sense because we were basically re-answering all the questions just in a slightly different frame of mind. I'm really hoping we can revamp that section to have fewer questions and have those questions be different and more team-oriented, maybe a little bit broader and wider in scope. They should be more about development practices as a team and the future of multiple developers developing in parallel or developing as a team using AI. 
I really loved the self-reflective session that was about the now. I thought that was perfect, and we probably shouldn't change any of that, but the session that was about me within six months did feel a little repetitive to fill out. I'm hoping we can put a spin on that, maybe shorten some of the questions, as in, not have quite as many, but have them be more perceptive, trying to glean insights about how personal development might change and how you would be comfortable with it changing in the future The idea here would be to be able to understand each person's core values and principles without directly asking them for it. 

<!-- Did you time sections, or only the whole? Did the Coverage grids (19 rows × 3 passes) feel like one long thing or three short ones? -->

---

## Q3 — How did it *feel* to answer — named, gut-reaction, and the two stances?

### What this is

Three deliberate design bets that only a real answerer can test: (a) responses are **named and shared openly**, with the Team view going to your manager; (b) every item must be answerable on **gut reaction**; (c) the Future section asks everything twice, **"I would…"** then **"The team should…"**.

### Why it matters

- If any item made you **guard** your answer because of who reads it — N5 (job impact) is the one we flagged — that's a validity problem the numbers won't show.
- If any item made you **stop and think**, it broke the gut-reaction rule and either the wording or the item goes.
- If the Team block felt like **"the same questions again"** rather than a genuinely different question, the Stance gap — the design's headline — is at risk before the team ever sees it.

### Options

| Option | Pros | Cons |
|---|---|---|
| **A. Felt fine on all three** | Design holds. | — |
| **B. Guarded on specific items** — name them | Fixable by wording, or by cutting N5. | Cutting N5 leaves Concern with 4 of 5 named risks. |
| **C. The Team block felt redundant** | Honest signal; better now than at n=9. | Fix is framing (section description), not items — or a real restructuring. |

### My recommendation

Answer all three parts separately, naming items where you can. If (c) felt redundant, say whether it was *the questions* or *the fact of answering 30 rows again* — those have different fixes.

### Your answer

: This felt really, really good. I liked this a lot. I definitely want to keep this part, especially for the now section for me. 

<!-- Also: did you notice the reverse-keyed items (C3, T2, F3, G6, N4, A2, V2 / FC3, FT2, FF3, FG5, FN4, FA2, FV2) as "trick" items, or did they read naturally? -->

---

## Q4 — Ambiguous items and the watch-list

### What this is

Any item you had to re-read, answered "Unsure" because the *question* was unclear rather than your view, or would word differently. Plus the specific things the banks asked the pilot to check:

- **C1/C2, T1/T3, A1/A3** — did those pairs feel like the same question? Did you answer them the same?
- **FF3 / FV2** — did they floor out (everyone would answer 1)?
- **Section-3 grid description** (level meanings for None → System-verified) — did you actually read it, or answer the grid from the row text?
- **Safeguard items** (asked three times) — did the "I'd read it myself" option make sense alongside the safeguards?

### Why it matters

This is the input to the wording fixes (SURVEY.md → Items!F) and to the 10-row cut in Q2. A pair that never diverges is the cheapest row to drop; an item nobody reads the description for needs its meaning moved into the row text.

### Options

None — this one is a list. Item IDs (or the statement text) plus one line each is ideal.

### My recommendation

Don't polish; a rough list now beats a complete one later. If nothing was ambiguous, say so explicitly — that is itself a finding.

### Your answer

: I don't think there was anything I had to reread. All the questions were very clear and to the point, so I was very happy with that. They were easy to read, easy to follow, so that was very nice. 

<!-- If you didn't read the grid description: would a one-line reminder in each row ("Drafter = AI writes, I rework") have helped, or is the scale self-explanatory? -->

---

## Q5 — What next, and what changes going forward?

### What this is

Two things. **(a) The survey:** run it on the team as-is, fix then run, or pilot again with a second person first. **(b) The way of working:** this map is nearly done — what, if anything, do you want to do differently on the next effort (the wayfinder/grilling process, the round-file format, the pace, what got over-built or under-built)?

### Why it matters

(a) decides whether #18 closes on this round or waits for fixes. (b) is the retrospective the map won't otherwise get — and you asked for it. Anything here about the *process* I'll save as feedback for future sessions rather than put on the map.

### Options (for part a)

| Option | Pros | Cons |
|---|---|---|
| **A. Run on the team as-is** | Fastest to real data; fixes can follow v1. | Wording bugs get baked into the first run's keys. |
| **B. Fix the Q3/Q4 items, then run** | One cheap pass; item text is the key, so fix before the team answers. | A few days. |
| **C. Second pilot with another person first** | Catches things only a non-author sees. | Another cycle; the team is 5–9, so the pilot eats a respondent. |

### My recommendation

**B** unless Q4 came back empty, in which case **A**. For (b), I'd like to hear specifically whether the grilling rounds were the right size, and whether any built artifact (rubric / sheet / dashboard / one-pager) is more than you'll actually use.

### Your answer

: I think, going forward, other than some of the other things I mentioned in previous questions, one of the major changes that I want to completely overhaul about this project is the dashboard itself. I really hated the process of having to take that data and paste it in, and it was very, very clunky.

What my ideal scenario will be and what I want to create for this project is that I will export the Excel file from the Microsoft Teams forms. That Excel file will be an input for a local host dashboard that I can just spin up. It uses Python on the backend and some sort of JavaScript or something simple, easy, and maintainable on the frontend. But to be clear, I don't really want to change how the dashboard looks. I was very happy with the prototyping we did. Just how it actually works and how I can spin it up is what I'm looking to change. 

<!-- Part (b) is the "changes I want to make going forward" you asked for — be blunt; it becomes memory, not a ticket. -->

---

## Anything else

Anything the questions above didn't give you room for — how the whole thing felt, what surprised you, what you'd tell someone else about to take it.

### Your answer

: 
