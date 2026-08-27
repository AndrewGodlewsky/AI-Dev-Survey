# Grilling — Issue #25: Coverage grid, the second pass

**Ticket:** [Coverage grid: what replaces the six-month pass](https://github.com/AndrewGodlewsky/AI-Dev-Survey/issues/25)
**Map:** [Map v2: Survey overhaul & local dashboard app](https://github.com/AndrewGodlewsky/AI-Dev-Survey/issues/21)
**Round:** 1 of 2 — six questions *(round 2 appended below)*
**How to use:** answer inline under each `### Your answer` heading. Free text is fine; you don't have to pick one of the listed options. Then tell me it's ready and I'll read it back and compute the next round.

---

## What is already settled coming in

- **The "today" pass is frozen.** 19 Development areas, the 1–6 Involvement level scale plus N/A, custom anchors on Code review, Incident response, Security review, Learning new tech. *"All of that was perfect. I don't want to change any of those questions."* Nothing in this ticket touches it.
- **The team pass is already cut** — decided in charting ([Team section](https://github.com/AndrewGodlewsky/AI-Dev-Survey/issues/23) is its own construct; no mirrored grid). So the most a second pass can be is **one** pass, for me. *Coverage Stance gap* is already dead.
- **The problem with the six-month pass, in your words:** *"I do want to change many of the 'me in six months' questions because I just felt like it was repetitive, re-answering the same questions over again, just where you think you'd be in six months … I don't know what I'll think in six months, because if I knew, I would be thinking that now."* And the v1 rows literally said it: every statement began `Me in 6 months:`, and the description said *"the level you would want to be working at in six months … Pick N/A if you won't be doing that work"* — a want-question dressed as a forecast.
- **How the Dimension block solved the same problem** ([Forward personal block](https://github.com/AndrewGodlewsky/AI-Dev-Survey/issues/24)): same target, different question. Single row; present-tense worlds or *I want to…*; *would you want to work this way*; the six-month window named **once** in the section description and **never in an item**; Gap survives as **Direction − Current = appetite minus practice**. The ticket says two different answers to one problem would be a design smell, and I agree — so every option below is measured against that pattern.
- **The Framing rule already told this ticket how it will be checked:** *"anything replacing the six-month pass is checked as a scale (both ends equally sayable), not as an option list."* The Involvement scale passes that check — *None* and *System-verified* are both sayable. What is **banned** for this pass: any *six months* in a row, ramp words, and a comparative against today (*more AI than now*).
- **The v1 rules that hang on this pass** (`scoring/scoring-rules.md` §5.2–5.3, `rubric/RUBRIC.md` §6.1): **Coverage Gap** = median of within-person differences in signed levels, computed only where both passes are numeric, never averaged across areas; the two **N/A↔level** mixed cases are excluded but counted and flagged as a *work-distribution* signal; **Edge marker** at level 6 on the six high-stakes areas (Code review, CI/CD, IaC, Incident response, SQL/data migrations, Security review), raised **per pass and labelled with it**.
- **Length budget.** #24 landed the Direction section at 27 answers and the whole survey at **103–122** — the 19 is this ticket. *"The team shrinkage is enough … If we do [need more], I'll come back and we'll address it later."*

## What this round holds back

- **Where the pass sits in the form** — section order and the alternating-type rule are [Assemble the v2 survey document](https://github.com/AndrewGodlewsky/AI-Dev-Survey/issues/29)'s.
- **Exact row prefix and description copy** — the stem is decided here (Q2); the final words are checked against the Framing rule's point 2 in the written spec (round 2) and assembled in #29.
- **How the Coverage panels change on the dashboard** — [Local app](https://github.com/AndrewGodlewsky/AI-Dev-Survey/issues/26), once Q1/Q4 fix what a person's forward Coverage value *is*.
- **Rubric and scoring text** — [Rubric v2: personal side](https://github.com/AndrewGodlewsky/AI-Dev-Survey/issues/33) and [Scoring rules v2](https://github.com/AndrewGodlewsky/AI-Dev-Survey/issues/28) rewrite §6.1 / §5.2 to whatever survives here.
- **The written spec** — the update to `survey/coverage-grid.md`, round 2, as #24 did with `direction-section.md`.

---

## Q1 — Does a second pass exist, and as what instrument? *(the root)*

### What this is

Four things "the second pass" could be in v2, from nothing to the same grid again:

- **Nothing** — Coverage is one pass. Direction on the areas is read off the Direction section's Autonomy and Trust items instead.
- **A Direction pass on the same scale** — the same 19 rows and the same 1–6 + N/A scale, single row, but the question is *if it were your call, where would AI sit for you on each of these* — no *six months* anywhere in it. A **Direction item** in grid form; the scale carries the position, exactly as the Framing rule says a scale may. Output: a **Direction level** per area, so Coverage Gap keeps its v1 definition in levels.
- **A Scenario pass** — 19 present-tense worlds, one per area, at the grid's own "AI does it" pivot (*"AI writes the feature code; I review the result"* … Definitely not … Definitely). The exact grammar of the Direction section. Output: a Desirability answer per area, not a level.
- **A symmetric Checklist pair** — two multi-selects over the 19 areas: *areas where I'd want AI doing the work* and *areas where I'd want to be doing the work myself*. **Two answers** instead of nineteen. Output: a per-area tick, not a level.

### Why it matters

This is the whole ticket. It decides whether Coverage Gap lives, in what unit, and whether the survey lands at 103 or 122 answers. It also decides whether the pilot's "re-answering the same questions" objection is met by asking a *different* question (Scenario, Checklist) or by asking the *same* scale with the forecast taken out of it (Direction pass).

The case that the forecast was the problem, not the scale: v1's rows carried `Me in 6 months:` and the description said *"in six months … if you won't be doing that work"*. That is the same defect #24 diagnosed in the Dimension block, and the fix there was to remove the horizon from the item, not to change the scale. The Involvement scale is the survey's one *concrete* instrument — named jobs, named levels — and a pick on it is a gut position, not a prediction, once nothing in the sentence asks you to predict.

The case against the Direction pass is the one you made: 19 rows on the same scale, sections apart, *feels* like the same questions. The Scenario pass avoids that by feel — but it has a structural problem: the Framing rule's **balance floor** requires every block of Scenario items to contain at least one less-AI item, and a grid of 19 *"AI does it"* worlds is 19 items pointing the same way. Meeting the floor means either a lopsided grid (some rows phrased as *I do this without AI*) or reopening #22. The Direction pass has no such problem — a scale with *None* at one end **is** the balance.

### Options

| Option | Pros | Cons |
|---|---|---|
| **A. Direction pass on the same scale** — same 19 rows, same 1–6 + N/A, single row, *where would you want AI to sit*, no horizon in any row | The pattern #24 chose, applied here: same target, forecast removed. Coverage Gap survives **unchanged in definition** — Direction level − Current level, in signed steps; the N/A pairing table and the level-6 Edge markers carry over. Passes the Framing rule as a scale, and the scale itself satisfies the balance floor. The output is the survey's most actionable finding: *"nobody wants AI past Advisor on incident response"*. | 19 answers — the survey lands at **122**, the top of #24's range. It is the same scale twice, and the pilot felt that. Whether it stops feeling like a forecast depends on the stem (Q2). |
| **B. Scenario pass** — 19 worlds at the "AI does it" pivot, on Desirability | Exactly the Direction section's grammar; reads as a fresh question, not the grid again. The "AI does it" example per row is already written. | Fixed level per row: you learn *would you want AI doing this work*, not *where*. Coverage Gap in levels dies; the read becomes categorical (today ≤3 + Definitely = wants to move). **Fails the balance floor** as a uniform grid — needs a lopsided grid or reopens #22. Still 19 answers. |
| **C. Symmetric Checklist pair** — two multi-selects over the 19 areas | **Two answers**, survey lands at ~105. Legal Checklist form, symmetric by construction. Direct and gut: tick where you'd want AI doing the work; tick where you'd want to do it yourself. | No levels, so no Coverage Gap — a tick against a 1–6 level is a categorical read at best. Sparse: people tick a few boxes, and an unticked area says nothing. Two 19-option multi-selects are a scroll in Forms; Python parses semicolon-joined labels (fine, but a new answer shape). The six-month Edge marker on the grid dies. |
| **D. One pass — today only** | Cheapest, 103 answers. No repetition anywhere in the survey. | You know where AI sits today and nothing about where anyone would want it, per area. Coverage Gap and the direction Edge markers die. The Direction section's Autonomy items are two rows on a Dimension — they cannot say *which areas*. |

### My recommendation

**A.** It is the same fix #24 applied to the same problem, the ticket's own reasoning says one problem should get one answer, and it is the only option where Coverage Gap keeps meaning what it meant — the read becomes *appetite minus practice* in levels, which is the read every other Gap now has. The cost is 19 gut clicks, and #24 budgeted for exactly that.

It is **not a close call against D** — the per-area direction is the finding you said you'd act on Monday. It **is closer against C** than the table suggests: if round 2 or the assembled form shows 122 is too long, C is the fallback I'd reach for, because it is legal, cheap, and directional — it just stops being a *profile*.

### Your answer

: Let's go with your recommendation here. I think a direction pass at the same scale is fine. I want to make sure, though, that we ask these questions in such a way that they are not leading. I need them to be generally neutral and allow people's answers to reveal how they feel about them, not have a leading question that pushes someone in one direction or another, particularly at the team level when we're trying to ask those questions. 

---

## Q2 — The stem: what the Respondent reads *(assumes Q1 = A)*

### What this is

Under A the rows are the 19 area names and the scale is unchanged, so the *entire* difference from the frozen pass — and the entire fix for "it felt like a forecast" — is in the words around the grid: the section title, the first line of the description, and the prefix each row has to carry (Forms requires every statement in the form to be unique, and the today rows already own the bare area names).

The section description otherwise stays the **same block as the today pass** — *The levels*, *What "AI does it" means per area*, *Four areas read the levels differently*, verbatim — because the scale is the same instrument and the Framing rule says the level definitions are part of what's checked, and they already pass.

Candidate stems, all present-tense, none with *six months*, none comparative against today:

- **(i)** Title: *If it were your call — where would AI sit on each of these?* Description first line: *For each area of work, pick the level you would want to be working at. Pick N/A if this isn't your work.* Row prefix: `If it were my call:`
- **(ii)** Title: *Where would you want AI on each of these?* First line: *For each area, pick the level you would want AI at. N/A if this isn't your work.* Row prefix: `Where I'd want it:`
- **(iii)** Title: *Your direction, by area.* First line: *For each area of work, pick the level you'd want to work at.* Row prefix: `Direction:`

### Why it matters

The Framing rule's point 2 makes this copy part of the instrument. The one **six-month** sentence the Direction section allows lives in *that* section's description; if this grid is its own Forms section (which the alternating-type rule will probably force — #29's call), the horizon should **not** be restated here. The stem has to make one thing plain without any ramp word: this is a *want*, not a forecast, and *None* is as ordinary an answer as *System-verified*.

### Options

| Option | Pros | Cons |
|---|---|---|
| **A. Stem (i)** — *if it were your call* | Says *want* without saying *want*; makes it a choice, not a prediction; the row prefix reads naturally in a Forms grid and clearly isn't `Today:`. Passes the flip (*if it were my call, None* is a normal thing to say). | Slightly long as a row prefix × 19. |
| **B. Stem (ii)** — *where would you want AI* | Shortest. Directly the Direction section's verb. | *Where I'd want it:* as a row prefix is ambiguous (*it* = AI? the work?). |
| **C. Stem (iii)** — *Direction:* | Uses the glossary term; shortest prefix. | *Direction* means nothing to a Respondent; a heading that names the construct instead of the question is exactly the kind of copy the Framing rule wants checked. |

### My recommendation

**A — stem (i)**, with the prefix free to shrink in assembly if it wraps badly in Forms (`If my call:` would do). The phrase does the work the six-month sentence used to do — sets the frame — without a horizon or a ramp. Final words get the five-check test in the round-2 spec.

### Your answer

: I think I actually like the "Where do you want AI?" probably more towards option B. 

---

## Q3 — All 19 rows, or a subset? *(assumes Q1 = A)*

### What this is

Whether the Direction pass repeats every row of the today pass, or only the rows where direction is most informative — say the six high-stakes areas plus the Core SDLC eight (14 rows), or the six high-stakes alone.

### Why it matters

This is the one length lever inside option A. But Coverage Gap exists per area and needs both passes numeric; every row dropped from the Direction pass is an area with a *today* and no *direction* — a profile with holes. And which rows are "most informative" is itself a leaning: choosing the high-stakes areas says the survey thinks direction matters where AI is risky, which is a pointer.

### Options

| Option | Pros | Cons |
|---|---|---|
| **A. All 19** | Same rows, same scale — one Coverage profile with two values per area; Gap everywhere; no row selection to defend. | 19 answers. |
| **B. High-stakes six + Core SDLC eight** (14) | Saves five answers; keeps the areas most people do. | Five areas with today and no direction; the selection is a judgement about which work matters, visible to the team. |
| **C. High-stakes six only** | Saves 13 answers; the Edge-marker areas stay. | Direction on Writing code, Tests, Debugging, Docs — the areas *everyone* does — is lost. Selection leans toward risk. |

### My recommendation

**A.** Five answers is not a real saving, and a subset makes the drafter choose which work counts. If length has to give, it gives at Q1 (option C there), not here.

### Your answer

: Yeah, let's go with your recommendation. All nineteen rows are good. 

---

## Q4 — Coverage Gap and the N/A pairing under a direction pass *(assumes Q1 = A)*

### What this is

The v1 definition is sound and carries over with one word changed — **Direction level − Current level**, median of within-person moves in signed steps, never averaged across areas, computed only where both are numeric. What has to change is the *reading* of the two mixed cases, because v1 read them as forecasts:

| Today | Direction | v1 read (forecast) | v2 read (position) |
|---|---|---|---|
| N/A | N/A | Doesn't do it, doesn't expect to | Not this person's work — excluded, counted |
| level | level | Gap | Gap = appetite minus practice, in levels |
| **N/A** | **level** | *"I don't do this now, but I expect to"* | *"Not my work today — but if it were, here's where AI would sit."* **No Gap** (no baseline); counted and flagged, as before |
| **level** | **N/A** | *"I won't be doing this in six months"* | *"I do this today and would rather it weren't my work."* **No Gap**; counted and flagged — still a work-distribution signal, now a *wish* rather than an expectation |

There is a second route: **drop N/A from the Direction pass**. *If it were your call* is answerable by anyone — you can have a view on where AI should sit on IaC without doing IaC — so the pass could be six options, no escape. The level→N/A case vanishes; the N/A→level case still has no Gap.

### Why it matters

The pairing rule is what stops a staffing signal being mislabelled an adoption signal, and it is one of the few v1 scoring rules that survives into Python unchanged if the reading is fixed. Dropping N/A makes scoring simpler and every row answerable, but breaks *same rows, same scale* — the two passes would no longer be the same instrument, and a forced level from someone who has never done the work is a weak number that the Gap would then treat as strong.

### Options

| Option | Pros | Cons |
|---|---|---|
| **A. Keep the definition and the pairing table; rewrite the two mixed readings as positions** | Same instrument both passes; the scoring rule carries over with a rename; the two flags stay meaningful (now wishes, not forecasts). | The level→N/A reading — *"would rather this weren't my work"* — is the one place the pass still asks a person to imagine a different job. Rare, flagged, never scored. |
| **B. Drop N/A from the Direction pass** | Every row answerable; one mixed case fewer; simpler Python. | The passes are no longer the same scale; a level from someone who doesn't do the work enters the profile as if it were a real position; changes the frozen scale's twin. |
| **C. Keep N/A but exclude both mixed cases silently** | Simplest read. | Loses the work-distribution signal v1 valued — *"four of nine don't do IaC and one wishes they didn't"* is a finding. |

### My recommendation

**A.** The rule was right; only its English was a forecast. Same instrument, same pairing, positions instead of predictions.

### Your answer

: Yeah, I think this is fine. Let's go with the recommendation here. 

---

## Q5 — Edge markers at level 6: both passes, labelled? *(assumes Q1 = A)*

### What this is

v1 raises an Edge marker for a **6** on any of the six high-stakes areas, per pass and labelled with the pass. A 6 in the today pass says *AI already runs this end-to-end and nobody looks*; a 6 in the Direction pass says *I'd want it that way*. Those are different statements and v1 labelled them apart. The Direction section kept probe Edge markers as one per person per probe.

### Why it matters

A 6 on *if it were my call, Incident response* is precisely the position an Edge marker exists to locate — the same job the five probes do for the Dimensions, but per area. Dropping it from the Direction pass would leave the probes as the only edge-finders on the forward side; raising it unlabelled would blur *does* and *would want*.

### Options

| Option | Pros | Cons |
|---|---|---|
| **A. Both passes, labelled by pass** (today / direction) — v1's rule, renamed | Keeps the only per-area edge-finder on the forward side; nothing to relearn. | Two marker kinds per area in the dashboard's probe table, as before. |
| **B. Today pass only** | Fewer markers; a marker only ever reports something that *is*. | Loses the one place someone can say *I'd hand this to the system* about a named risky area. |
| **C. Direction pass only** | A marker about appetite matches the forward block's purpose. | A 6 today on security review with no marker is the odder omission. |

### My recommendation

**A.** Same six areas, both passes, labelled. Nothing about the rule was a forecast; only the pass name was.

### Your answer

: Yeah, let's go with the recommendation. Both passes labeled are fine. 

---

## Q6 — The names *(assumes Q1 = A)*

### What this is

The glossary and the specs still carry the v1 words. Proposed:

- **Direction pass** — the second Coverage grid (the today pass keeps its name). *Avoid:* six-month pass, Future-Personal pass.
- **Direction level** — a Respondent's Involvement level on an area in the Direction pass; the today value stays *Involvement level* (or *Current level* where the contrast matters).
- **Coverage Gap** — kept, now `Direction level − Current level`. It already reads as appetite minus practice, so the name needs no change.
- **Coverage** (glossary) — *"an Involvement level per Development area, current and future, personal and team"* becomes *"…today and direction, for the Respondent"*. Team drops out; it was cut in charting.
- **Slice** (glossary) — *"Current vs Future, Personal vs Team stance"* is stale on the same grounds and gets corrected in the same edit.

### Why it matters

Item text is the database key and the glossary is the ubiquitous language; every downstream ticket (#26, #28, #29, #33) will use whatever these are called. Naming it once here means the Python app, the rubric and the how-to-read all say the same word.

### Options

| Option | Pros | Cons |
|---|---|---|
| **A. As proposed** — *Direction pass*, *Direction level*, *Coverage Gap* kept | Parallel to *Direction section* / *Direction score*; one word for the forward side everywhere. | *Direction level* and *Direction score* are one word apart for two different scales (1–6 vs 1–5) — but so were *Involvement level* and *Future score* in v1. |
| **B. Keep *Coverage Gap* but call the pass the *want pass* / *want level*** | Says what the question is. | A second forward word alongside *Direction*; the glossary gains a synonym for the thing #24 just named. |

### My recommendation

**A.** One forward word. I'll make the glossary edits when you confirm.

### Your answer

: Yeah, that's fine. Go with your recommendation. 

---

## Anything else

Anything you'd rather I stop assuming — in particular whether 122 answers is a number you're prepared to pilot, since that is what A at Q1 commits you to.

### Your answer

:

---

# Round 2 — the written spec

**Round:** 2 of 2 — one question. React to the draft; the ticket closes on your word.
**How to use:** read [`survey/coverage-grid.md`](../../survey/coverage-grid.md), the new *The Direction pass* section at the bottom. Mark anything wrong inline under Q7, or say it's ready.

**What round 1 settled**

- **Q1 → A.** A single **Direction pass** on the same 19 rows and the same Involvement scale. Your rider — *"not leading … generally neutral and allow people's answers to reveal how they feel"* — is exactly what the Framing rule does for this grid: it is checked as a scale (*None* and *System-verified* both equally sayable), the flip *"Where I want AI: None"* is an ordinary thing to say, no horizon and no comparative against today appear anywhere in the pass. The *"particularly at the team level"* part lands on the **Team item bank** ([#31](https://github.com/AndrewGodlewsky/AI-Dev-Survey/issues/31)) — there is no team grid any more, and every team item is drafted to the same rule.
- **Q2 → B, stem (ii).** *"Where do you want AI?"* I resolved the row-prefix ambiguity I flagged by making the prefix say the noun: **`Where I want AI:`** — *Where I want AI: Code review*. Title `Where do you want AI on each of these?`; first line `For each area of work, pick the level you want AI at. Pick N/A if this isn't your work.`
- **Q3 → A.** All 19 rows.
- **Q4 → A.** Coverage Gap = `Direction level − Current level`, in signed levels, median of within-person moves; the N/A pairing table kept, its two mixed readings rewritten as positions.
- **Q5 → A.** Level-6 Edge markers on the six high-stakes areas, both passes, labelled by pass.
- **Q6 → A.** *Direction pass*, *Direction level*, *Coverage Gap* kept; glossary corrected.
- **Anything else → blank.** Read as: 122 answers is a number you are prepared to pilot.

**What was written** (working tree, uncommitted — your commit):

- `survey/coverage-grid.md` — header now says two passes (today frozen, Direction, team cut); new **The Direction pass** section: six rules including the exact copy, Coverage Gap and the re-read pairing table, Edge markers, shape (57 → 38 grid answers; survey at 122), the recorded Checklist-pair fallback, what dies, what each downstream ticket inherits. Scale, rows and anchors untouched.
- `CONTEXT.md` — **Coverage** rewritten (today pass + Direction pass, Respondent only); **Direction pass**, **Direction level**, **Coverage Gap** added; **Edge marker** notes *either pass, labelled*; **Slice** loses *Future* and *Team stance*.
- `survey/direction-section.md` — the two Shape cells that deferred to #25 now say 19 / 46.

**What closing does:** [Scoring rules v2](https://github.com/AndrewGodlewsky/AI-Dev-Survey/issues/28) and [Rubric v2: personal side](https://github.com/AndrewGodlewsky/AI-Dev-Survey/issues/33) unblock; [Assemble the v2 survey document](https://github.com/AndrewGodlewsky/AI-Dev-Survey/issues/29) waits only on the two item banks. No new ticket — the Direction pass has no bank to draft; its rows are the frozen ones and its copy is in the spec. Nothing graduates from the fog (all three patches there are downstream of scoring).

---

## Q7 — Is the written spec the pass?

### What this is

The doc is the decision now. Three things worth a second look:

1. **The copy in rule 3** — title, first line, prefix. It goes into the form as written unless #29 has to shorten the prefix for Forms layout. Does *"pick the level you want AI at"* read as a want to you, or does it still smell of a forecast?
2. **The level→N/A reading** — *"I do this today and would rather it weren't my work."* It is the one place the pass asks someone to imagine a different job. Flagged, never scored, and rare — but say so if you would rather it read simply *"no view"*.
3. **The recorded fallback** — the Checklist pair is written into the spec as the rejected trade so it is findable if 122 turns out too long. Fine to leave there, or cut it if you would rather the spec carry only the decision.

### My recommendation

Ship it as written.

### Your answer

: Ship it and close #25. *(answered in chat, 2026-08-27)*
