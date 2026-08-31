# Grilling — Issue #30: Team Dimension rubric levels

**Ticket:** [Team Dimension rubric levels](https://github.com/AndrewGodlewsky/AI-Dev-Survey/issues/30)
**Map:** [Map v2: Survey overhaul & local dashboard app](https://github.com/AndrewGodlewsky/AI-Dev-Survey/issues/21)
**Round:** 1 of ~1 — the draft is already written into `rubric/RUBRIC.md` §4.8; three questions settle how it's built, one collects wording reactions. **Answered 2026-08-31: all four recommendations accepted (answered in chat); ticket resolved.**
**How to use:** answer inline under each `### Your answer` heading. Free text is fine; you don't have to pick a listed option. For Q4, editing §4.8 directly and saying "see the file" is a perfectly good answer. Tell me when it's ready and I'll read it back, apply any changes, and resolve the ticket.

---

## What is already settled coming in

- **The construct** (#23): five Team Dimensions — Transparency · Verification · Agent latitude · Pace · Shared practice — each a bundle of the eight facets in `survey/team-section.md`, with stated low and high poles; a **Norm score** per Respondent, spread is the finding.
- **The instruction from the item-banks resolution** (#31 Q2): Agent latitude's level text **must run opposite for *Limits***, and a flat 3 on that Dimension is ambiguous by construction — the facet view is its primary read. The draft obeys both; Q3 checks the *how*.
- **The Framing rule's scale check applies to level prose** (from the ticket itself): both ends equally sayable, level 1 a position, never a deficiency.
- **Where it lives**: in `rubric/RUBRIC.md` alongside the seven personal Dimensions, not a second rubric — from the ticket. The draft sits as §4.8, after Craft values, before Coverage.
- **Item wording is not this ticket** — `survey/team-items.md` stands as resolved in #31.

## What this round holds back

- **Nothing is deferred to a second round.** The three settle-on-the-way decisions and the wording reaction are all askable at once; a Round 2 happens only if your answers here reshape the draft enough to need a re-read.
- **Rubric v2's overall restructure** is [Rubric v2: personal side](https://github.com/AndrewGodlewsky/AI-Dev-Survey/issues/33)'s business — v1's §§1–4 intro text still describes dead machinery (Future-Team, Stance gap); §4.8 doesn't try to fix that.

---

## Q1 — Whose norm does a level describe: the team's, or the Respondent's?

### What this is

The score is **per Respondent** (the norm they would set), but the text will also be read against the **Team score** (where the team's aggregate sits). The level text has to serve both readings with one set of words.

### Why it matters

Written as a Respondent's position (*"would require every line read"*), the text reads wrong at team level; written as an opinion (*"thinks the team should…"*), it double-wraps — the Agreement scale already carries the opinion. Whatever is chosen here is 25 paragraphs of prose the team will quote at each other in the results meeting.

### Options

| Option | Pros | Cons |
|---|---|---|
| **A — The norm in force**: describe the way of working itself (*"A human reads every line of AI output before it ships"*) | One text reads correctly as "the norm I'd set" **and** "the norm we'd collectively set"; mirrors §4's proven "position, not action" trick; shortest prose | Slightly abstract — no actor named at some levels |
| **B — The Respondent's stance**: (*"Would hold the team to reading every line"*) | Directly matches what the number is (a per-person Norm score) | Reads wrongly for the Team score; every line starts "Would…"; drifts toward rating people |
| **C — The team as actor**: (*"At 3 the team requires…"*) every line | Concrete team voice, matches the ticket's example phrasing | Reads as a description of the *actual* team, which no score measures; awkward for a Respondent's own Norm score |

### My recommendation

**A**, and it's what the draft does — with the team as implicit actor so it still sounds like team voice (the §4.8 intro states the convention once: *level text is worded as the norm in force*). C was a close second; A won because the same sentence has to sit under both a person's initials and the team mean without changing meaning.

### Your answer

Accepted the recommendation — **A, the norm in force**, as drafted. (Answered in chat, 2026-08-31.)

## Q2 — Two-facet Dimensions: one level text, or a line per facet?

### What this is

Transparency, Agent latitude and Shared practice bundle two facets each. Their five levels can each be one paragraph spanning both facets (the draft), or a labelled line per facet per level (10 lines per Dimension).

### Why it matters

The level text is the landmark for the **Dimension mean** — that's the number it locates. Per-facet lines would double the prose and invite reading the rubric at a resolution the score doesn't have; but one spanning paragraph asserts the facets move together, which for Agent latitude is exactly what #31 said *not* to assume.

### Options

| Option | Pros | Cons |
|---|---|---|
| **One text per level** (the draft) | Matches what a mean can say; same shape as the seven personal Dimensions; half the prose | A person split across facets (high parallel-work, high limits) sits *between* texts that each assert both halves |
| **A line per facet per level** | Honest about bundles; supports the facet view #31 made primary for Agent latitude | 80 lines of rubric for 5 numbers; implies facet-level landmarks the scoring spec doesn't produce; no personal Dimension does this (Concern bundles five risks under one text) |

### My recommendation

**One text per level** — Concern is the precedent: five risks, one level text, facet view for the split read. The Agent latitude ambiguity is handled where #31 put it: a warning paragraph above that table saying the mean locates nobody on its own. Not a close call.

### Your answer

Accepted the recommendation — **one text per level**, facet view for the split read. (Answered in chat, 2026-08-31.)

## Q3 — Agent latitude: is the opposite-running Limits handled right?

### What this is

The instruction: *Limits* level text runs opposite (broad no-go zones at level 1, none at level 5). The draft welds the two facets into one arc per level — e.g. level 1 *"personal sandboxes only, and whole kinds of work off-limits as policy"*, level 5 *"anywhere including `main`, no standing no-go zones: what contains them is verification, not territory"* — plus the italic warning paragraph above the table naming the flat-3 ambiguity.

### Why it matters

This is the one Dimension where the level text can quietly lie: prose that reads as a single "more freedom" ramp would pretend the facets agree. It's also the text most likely to be quoted when the team argues about agents on `main`.

### Options

| Option | Pros | Cons |
|---|---|---|
| **As drafted** — welded arc + warning paragraph above the table | Each level is a coherent, real-world team posture; Limits visibly recedes as you read down | A reader skimming only level texts might still miss that a mid split is common |
| **Welded arc, warning moved into the level-3 row itself** | The caveat sits exactly where the ambiguous number lands | Breaks the table's rhythm; the warning applies to the whole Dimension, not one row |

### My recommendation

**As drafted.** The warning belongs to the Dimension (any mean there under-reports a split, not just 3.0), and an intro caveat is how §4 handles its other warnings (Fluency's softer Gap, Craft values'). Close to a formality — but this is the handed constraint, so it gets its own check rather than riding inside Q4.

### Your answer

Accepted the recommendation — **as drafted**: welded arc, warning paragraph above the table. (Answered in chat, 2026-08-31.)

## Q4 — The 25 level texts themselves

### What this is

The wording pass: read `rubric/RUBRIC.md` §4.8 — five tables, 25 rows. The scale check was applied throughout: every level 1 is written as a position someone at the results meeting could defend out loud (*"Automated checks are the gate"*, *"The team moves at the pace of its most cautious member"*), never as a lack.

### Why it matters

These paragraphs are what a Norm score of 2.3 or 4.1 *means* when the dashboard shows it. A level text nobody would own to is a leading item by the back door — the same failure the Framing rule exists to block.

### Options

| Option | Pros | Cons |
|---|---|---|
| **Accept as drafted** | Done | Any wording that grates stays |
| **Edit specific rows** — inline here, or directly in §4.8 | Surgical; the structure survives | None |
| **Redraft a whole Dimension** | For a table whose arc feels wrong end to end | Likely triggers a Round 2 |

### My recommendation

Read Verification and Pace hardest — Verification level 3 (*"the team's normal review… no extra ceremony for its origin"*) is the row doing the most work, since it defines origin-blind review as the midpoint; and Pace level 3 makes *individual freedom + team consensus* the middle, which is a real stance but not the only possible one.

### Your answer

Accepted the recommendation — **the 25 rows stand as drafted**, Verification 3 and Pace 3 included. (Answered in chat, 2026-08-31.)

## Anything else

Anything this round missed — a sixth thing the level text should carry, a placement objection to §4.8, a term the glossary should pick up?

### Your answer

Nothing raised. (Answered in chat, 2026-08-31.)
