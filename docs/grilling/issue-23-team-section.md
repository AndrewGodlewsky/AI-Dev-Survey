# Grilling — Issue #23: Team section

**Ticket:** [Team section: what it measures, and is it scored](https://github.com/AndrewGodlewsky/AI-Dev-Survey/issues/23)
**Map:** [Map v2: Survey overhaul & local dashboard app](https://github.com/AndrewGodlewsky/AI-Dev-Survey/issues/21)
**Round:** 1 of ~3 — five questions *(round 2 appended below)*
**How to use:** answer inline under each `### Your answer` heading. Free text is fine; you don't have to pick one of the listed options. Then tell me it's ready and I'll read it back and compute the next round.

---

## What is already settled coming in

- **The mirror is dead.** v1's team block re-asked the seven personal Dimensions in a "the team should…" frame; the pilot called it *"re-answering all the questions just in a slightly different frame of mind."* Charting killed it, and the **Stance gap** and **norm gap** died with it — accepted cost, not reopened here.
- **Single pass, "what it should be."** No now/future pair for the team. *"I just want to have a section about what it should be or what each person wants it to be."*
- **The team Coverage pass and the team Safeguard pass are cut** — as *passes*, i.e. third askings of personal items. Whether the Safeguard question has a *different* home here is Q4.
- **The purpose, in your words** (from the Framing rule round): *"how, as an individual, they want to work with other individuals who are using AI. It's about, as a group, what are acceptable and unacceptable patterns and principles for us as a team."* Two lenses in one sentence — Q3 is about whether they are one pass or two.
- **The Framing rule applies** (`survey/item-framing-rule.md`): all five forms are legal here, and this is the **only** block where a **Value item** — a principle stated flat as a proposed norm — is legal. Balance floor per block. Nothing points.
- **Item wording is not this ticket.** The map's fog holds *"the item banks for the two rewritten blocks"*; this ticket fixes what the bank is *for*, and the bank graduates after it.

## What this round holds back

Each of these needs an answer below before it can be asked honestly, so they are round 2:

- **Probes and Edge markers at team level** — whether an extreme team norm gets a marker depends on whether the section is scored (Q1); on an unscored profile a strong disagreement is already visible.
- **Items per topic and the balance floor per topic** — hangs on which topics survive (Q2).
- **What `CONTEXT.md` gains and loses** — *Stance*, *Team score*, *Future score* all shift depending on Q1 and Q3; the new terms (*Topic*, whatever the norm-agreement reading is called) are named once the shape is fixed.
- **How disagreement is read** — spread thresholds and the "we don't have a norm here" signal are downstream of Q1 and Q5, and mostly belong to the dashboard and how-to-read tickets.

---

## Q1 — Scored Dimensions, or an unscored profile? *(the driver — everything else sizes off this)*

### What this is

You said in charting *"we might have to come up with some alternate dimensions that the team would be scored upon"* and then, when asked directly, deferred: *"that might have to be a grill-me issue later on."* This is that issue.

The word *dimension* is doing two jobs. One is **an area the section covers** — a topic with a name, so results can be read per topic. The other is **a 1–5 construct with rubric level text**, so a team can be "at 3.2" on it. You need the first either way. The question is whether you want the second.

### Why it matters

It is the largest cost driver left on the map. Scored means, per new construct: a glossary definition, 1–5 level prose in the Rubric (v1's `rubric/RUBRIC.md` level text is the single largest piece of writing in the repo), reverse keys, facet rules, and a scored-Dimension view in the dashboard — [Rubric levels](https://github.com/AndrewGodlewsky/AI-Dev-Survey/issues/4), [Current-state bank](https://github.com/AndrewGodlewsky/AI-Dev-Survey/issues/5) and [Scoring rules](https://github.com/AndrewGodlewsky/AI-Dev-Survey/issues/9) re-walked. Unscored means the section works the way Coverage and Safeguard items already do: a profile read for **agreement and spread**, per topic, with no rubric prose behind it.

There is also a validity point. A personal Dimension is a *trait* — Trust 2.4 says something about a person. A team norm is a *proposal* — "the team should require disclosure of agent-written code" is something you vote on, not a level you're at. Averaging a vote to 3.4 hides the one thing you want to see: whether the team agrees.

### Options

| Option | Pros | Cons |
|---|---|---|
| **A. Unscored profile, grouped by named Topic** — each item read for agreement and spread; each Topic is a heading in the survey and a panel in the dashboard, never a number | Cheapest by a wide margin. Matches what the data is. The dashboard already renders distributions (Coverage, Safeguards). "Where do we agree / where are we split" is the actionable output. | No "the team is at 3.2 on handoffs." No level prose to hand someone. Topics can't be ranked against each other. |
| **B. Scored — new team Dimensions with full rubric levels** | Team results sit beside personal ones in the same visual language. Comparable across a future re-run. | Most expensive option on the map. Level text for a brand-new construct is hard to write well, and the construct is a norm, not a trait. |
| **C. Hybrid** — one or two scored Dimensions (e.g. *team risk appetite*), the rest profile | A scale where one genuinely means something. | Two logics to explain to a reader; you pick which is which with no data. |

### My recommendation

**A.** Your own phrasing of the purpose — *acceptable and unacceptable patterns and principles for us as a team* — is a list of proposals to agree or disagree with. That is a profile. If a topic later turns out to want a scale, adding one is a smaller change than removing one. And it keeps v2 from re-walking three of v1's most expensive tickets for a construct nobody has validated.

I'm aware this is the opposite of the *"scored upon"* instinct from charting; if you want B, the map gets a Rubric-levels ticket for the team construct and the Not-yet-specified *Rubric v2* patch roughly doubles.

### Your answer

: I think we need to go with option B and come up with a new team dimension and full rubric levels. Ultimately, this is a rework and a refactor and overhaul of what was originally there, so it's fine if we replace things. 

---

## Q2 — Which Topics, and how many?

### What this is

The candidate list, built from your two lenses. The first four are *developer-to-developer with AI in the mix*; the last four are *group principles*.

| # | Topic | What it covers | Example norm (illustrative, not drafted) |
|---|---|---|---|
| 1 | **Disclosure & provenance** | Whether and how people tell each other what AI wrote — PR descriptions, commit trailers, "an agent did this part" | *"A PR says which parts an agent wrote."* |
| 2 | **Reviewing AI-assisted work** | How a reviewer treats an AI-heavy PR; what the author owes the reviewer; reviewer load | *"An AI-written PR gets the same review as a human one — no more, no less."* |
| 3 | **Parallel development with agents** | Several people running agents in one codebase — conflicts, churn, branch hygiene, agents touching shared code | *"An agent may open a PR against main without a human having read the diff first."* |
| 4 | **Shared conventions & tooling** | Shared prompt files / `CLAUDE.md`-style config in the repo, agreed tools, who maintains them | *"The repo carries one shared set of AI instructions everyone's tools read."* |
| 5 | **Ownership & accountability** | Who owns AI-written code once merged; "explain every line under your name" at team level | *"Whoever merges it can explain it."* |
| 6 | **Pace & risk appetite** | How fast the team adopts; who decides; whether the cautious or the keen set the pace | *"We move at the pace of the most cautious person on the team."* |
| 7 | **Limits** | Work AI must not touch as a matter of team policy — secrets, prod data, certain areas | *"Some parts of this codebase are off-limits to agents, and we write down which."* |
| 8 | **Learning & skill** | Keeping the team's skills sharp, pairing, teaching each other tools, skill atrophy as a *team* risk | *"Everyone on the team can still do the work without AI."* |

Note the illustrative norms are written so the flip reads as a normal thing to want — that is the Framing rule at work, and it is why Topic 6's example is phrased from the cautious end.

### Why it matters

*"Three is a section; ten is a survey of its own."* v1's team block was ~49 answers. At 3–4 items per topic, six topics is ~20 items — under half of v1 — and each topic gets a readable dashboard panel. Eight topics at the same density is ~28 and starts to crowd the forward personal block.

### Options

| Option | Pros | Cons |
|---|---|---|
| **A. Six topics** — 1–5 plus **6+7 merged** as *"Pace & limits"* (how fast, and where we stop) | Covers both lenses. Pace and limits are the same conversation from two ends. Learning (8) is partly a personal Dimension already (Fluency, and the Concern facet on skill atrophy). | Drops Learning as a team topic. |
| **B. All eight** | Nothing dropped. | ~28 items; two topics thin enough to feel like padding. |
| **C. Four topics** — the dev-to-dev lens only (1–4) | Sharpest section; entirely new ground v1 never touched. | Loses the *"acceptable and unacceptable principles"* lens you named explicitly. |

### My recommendation

**A, six.** Strike or add rows in the table above rather than picking a letter, if that's easier — the topic list is the decision, the count follows.

### Your answer

: I think let's go with all eight. I think that's fine. 

---

## Q3 — One voice or two: does the section ask "what I want from others" separately from "what we should require"?

### What this is

Your purpose sentence has two halves: *how, as an individual, I want to work with other individuals who use AI*, and *as a group, what are acceptable patterns for us*. Those could be two rows per item — and that is exactly the shape the mirror had (*"I would"* / *"the team should"*), which the pilot found repetitive and charting killed.

### Why it matters

If the halves are two rows, the Stance concept comes back for one block, with its Forms cost (two Likert blocks, unique statements) and the "re-answering" feel. If they are one row, the individual-interaction lens has to live in the *content* of the items instead — the norms are about what developers owe each other, which is where that lens naturally lands anyway.

### Options

| Option | Pros | Cons |
|---|---|---|
| **A. One row, team voice** — every item is a norm: *"On this team, …"* / *"the team should…"*. The dev-to-dev lens is carried by Topics 1–4's content. | Single pass, as charting settled. Reads as a vote, which is what it is. No Stance, no second Likert block. | "What *I* want from others" is inferred from what someone endorses as a norm, not asked. |
| **B. Two rows** — *"I want this from the people I work with"* / *"we should require this"* | Both halves of your sentence asked literally. | The mirror, re-created. Stance survives for one block; the Forms build doubles; "re-answering" returns. |
| **C. One row, mixed voice** — some items *"I want…"* (Direction, personal form), some *"the team should…"*, chosen per item | Each item in its most natural voice. | Two voices in one block makes the reader switch frames; and a personal-voice item in the team section blurs it with the forward personal block. |

### My recommendation

**A.** A norm someone endorses *is* what they want from the people they work with; asking it twice measures the same thing and re-creates the cost you cut. Keep the personal *"I want…"* form for the forward personal block, where it belongs.

### Your answer

: It should definitely be option A. It should be on this team, or the team should. It's not about what you want others to do. It's about what we should require, so option A is the correct choice here. 

---

## Q4 — The team Safeguard question: gone, or re-homed as the section's Checklist item?

### What this is

v1 asked the Safeguard checklist three times; the third — *"which of these should the team accept as enough, without an individual reading the output?"* — was the team pass, and the map cut it as a pass. But read on its own it is a team norm about reviewing AI output, which is Topic 2 exactly, and it is a **Checklist item** — a legal form.

### Why it matters

It is the one v1 question whose *team* answer was directly actionable (*"where they agree, that is a draft six-month norm the team can write down"* — `safeguard-items.md`). Dropping it loses that; keeping it costs one multi-select question.

### Options

| Option | Pros | Cons |
|---|---|---|
| **A. Re-home it** — one Checklist item under *Reviewing AI-assisted work*, single asking, team voice; same seven options, same mechanics (principle answer first, not ramp-ordered) | Keeps the most actionable team answer v1 had. Fits the Framing rule and Q3-A. One question. | The map's Notes say the pass is "cut" — the wording there needs one clause: cut as a *pass*, re-homed as an *item*. |
| **B. Gone** | Cleanest reading of "the team Safeguard pass is cut." | Loses the draft-norm output for one saved question. The Lever/personal Safeguard story is unaffected either way (that's #24). |

### My recommendation

**A.** It is a different thing from the pass that was cut — a standalone norm, not a third asking of a personal item.

### Your answer

: Yeah, definitely rehome it, I think. So option A is correct. 

---

## Q5 — What scale does the team section answer on?

### What this is

v1's team stance used the **Desirability scale** (*Definitely not … Definitely*) because the items were "the team should…" completions. The team section now also carries **Value items** stated flat — *"Every line that ships should be understood by someone on the team"* — and *Definitely* is an odd answer to a flat principle. An **Agreement scale** (*Strongly disagree … Strongly agree*) reads naturally for both forms.

### Why it matters

One scale per block keeps the reader in one frame and keeps Forms simple. The choice also says what the section *is*: Desirability asks *do you want this*; Agreement asks *do you hold this* — and a vote on a norm is the latter.

### Options

| Option | Pros | Cons |
|---|---|---|
| **A. Agreement scale for the whole team section** — 5 points, midpoint *Neither* | Native language of a vote. Reads well for Value and Direction items alike. The forward personal block keeps Desirability, so each block has one scale and the two blocks read differently on purpose. | A third scale family in the survey (after Behaviour/Attitude in Current-state and Desirability in the forward block). Every statement is still unique, so the Forms export is unaffected. |
| **B. Desirability everywhere forward** — team section shares the forward personal block's scale | One scale for everything after the Current-state section. | Value items have to be contorted into "the team should…" completions to read on it; some will be awkward. |

### My recommendation

**A** — a close call against B. The tie-breaker is that the section is a vote and should read like one; and the scale check in the Framing rule (*both end labels equally sayable*) passes trivially for *Strongly disagree / Strongly agree*.

### Your answer

: Yeah, let's go with your recommendation here. That seems fine. I definitely want there to be a scale for people to be able to express how they feel, because it is a little bit nuanced and it's not as simple as strongly agree, strongly disagree. 

---

## Anything else

A topic you already know the team argues about that isn't in the Q2 table; a norm you already know you want to put to a vote; or a reason the team section should ask about *today* after all.

### Your answer

: I think it has to be a little bit of both agreement and desirability, so I'm wondering if we can work both of those in here. 

---

# Round 2 — eight topics, scored: what the axes are

**Round:** 2 of 3 — four questions. Round 3 is you reacting to the written spec (`survey/team-section.md`), not more questions.
**How to use:** same as before — answer inline under each `### Your answer`, then tell me it's ready.

**What round 1 settled**

- **Q1 → B, scored.** New team Dimensions with full 1–5 rubric level text. *"This is a rework and a refactor and overhaul … it's fine if we replace things."* Against my recommendation, and noted: the map gets a Rubric-levels ticket for the team construct, and *Rubric v2* in the fog roughly doubles.
- **Q2 → all eight topics.** Disclosure & provenance · Reviewing AI-assisted work · Parallel development with agents · Shared conventions & tooling · Ownership & accountability · Pace & risk appetite · Limits · Learning & skill.
- **Q3 → A, one voice.** *"It's not about what you want others to do. It's about what we should require."* Every item is *"On this team…"* / *"the team should…"*.
- **Q4 → A.** The Safeguard checklist is re-homed as one Checklist item under *Reviewing AI-assisted work* — single asking, team voice, never scored. The map's Notes get a clause: cut as a *pass*, re-homed as an *item*.
- **Q5 → Agreement scale.** *"I definitely want there to be a scale for people to be able to express how they feel."* I'm taking that as the **5-point** scale I proposed — *Strongly disagree · Disagree · Neither · Agree · Strongly agree* — because every other scale in the survey is five points and the Rubric's levels are 1–5. Say so if you meant seven.

**What Q1 + Q2 together imply.** A scored Dimension is a **1–5 axis with a natural direction** — Autonomy runs *autocomplete → autonomous agent*, Concern runs *unconcerned → concerned*. Each team Dimension needs the same: a low pole and a high pole that are both normal things to want (the Framing rule's scale check), and level text describing what a team at 1, 2, 3, 4, 5 requires. That is Q6, and it is the whole round; Q7–Q9 are consequences.

**What this round holds back**

- **The level text itself and the items** — two tickets that graduate when this one closes: *Team Dimension rubric levels* and *Team item bank*.
- **Glossary deaths outside this block** — *Stance* and *Future score* only die completely once [Forward personal block](https://github.com/AndrewGodlewsky/AI-Dev-Survey/issues/24) confirms the personal side is single-stance. Q9 handles only what this block adds.
- **Dashboard views for team Dimensions** — [Local app](https://github.com/AndrewGodlewsky/AI-Dev-Survey/issues/26) and [Scoring rules v2](https://github.com/AndrewGodlewsky/AI-Dev-Survey/issues/28) own that; this ticket hands them the shape.

---

## Q6 — Eight Dimensions, or five with the topics as facets — and what is each axis?

### What this is

Two structural choices, and they fold together.

The glossary already has the mechanism for a Dimension that measures more than one thing: a **bundle** with **facets** — Concern is five named risks, a Dimension score is the mean of its facets. So "all eight topics" can be **eight Dimensions** (one per topic) or **fewer Dimensions with the eight topics as facets**. Either way, every Dimension needs its axis stated. Here is my proposal for the grouped version; the ungrouped version uses the same poles, one per topic.

| Team Dimension | Facets (the topics) | Low pole (1) | High pole (5) | Direction reads as |
|---|---|---|---|---|
| **Transparency** | Disclosure & provenance · Ownership & accountability | AI's role in the work is invisible; ownership of AI-written code is diffuse or by the system | Every AI contribution is labelled and personally owned by whoever merges it | *more required visibility and personal ownership* |
| **Verification** | Reviewing AI-assisted work (+ the re-homed Safeguard checklist, unscored, sits here) | Automated checks are enough; nobody has to read AI output | A human reads every line of AI output, with the same review as human work or more | *more required human review* |
| **Agent latitude** | Parallel development with agents · Limits | Agents work only in personal sandboxes and broad areas are written off-limits | Agents act on shared code anywhere, including against `main`, with no no-go zones | *more freedom for agents in the shared codebase* |
| **Pace** | Pace & risk appetite | The team moves at the pace of its most cautious member and waits for evidence | The team moves at the pace of its keenest member and tries things first | *faster adoption as a team* |
| **Shared practice** | Shared conventions & tooling · Learning & skill | Everyone picks their own tools and instructions; skill without AI is each person's own business | One shared, maintained setup; the team deliberately keeps everyone able to work without AI | *more investment in shared capability* |

Two things to check against the Framing rule as you read: **both poles are normal things to want** (a team that says "automated checks are enough" is a position, not a confession), and **the direction is not the good direction** — 5 on *Agent latitude* and 5 on *Verification* pull opposite ways on purpose.

### Why it matters

This table *is* the construct. Level text (the next ticket) is written between these poles, items are written to land on them, and the dashboard's team panel is one row per Dimension. Get an axis wrong here and the rubric is wrong for that Dimension.

### Options

| Option | Pros | Cons |
|---|---|---|
| **A. Five Dimensions, eight facets** — the table above | 25 level descriptions instead of 40. All eight topics survive and are visible per-facet in results (facets already render that way). Five reads beside the seven personal Dimensions without crowding the dashboard. Pairs whose poles genuinely share an axis are paired; *Pace* stays alone because nothing shares its axis. | Two of the pairings are judgement calls — *Limits* under Agent latitude, *Learning* under Shared practice. A facet with only two items is thin. |
| **B. Eight Dimensions, one per topic** | Every topic gets its own score and its own level text. No pairing arguments. | 40 level descriptions to write and read. Eight team rows plus seven personal rows on the dashboard. Some topics (*Limits*, *Learning*) are narrow for a five-level scale. |

### My recommendation

**A** — a close call, and either is workable. The tie-breaker is the level text: five well-separated axes are easier to write five honest levels for than eight, two of which are narrow. **Correct the poles in the table directly** if any read wrong — that matters more than the letter.

### Your answer

: I like these a lot. Let's include all eight here. 

---

## Q7 — Items per facet, and the reverse-key rule

### What this is

A scored mean needs enough items to be one. v1's Current-state bank averages ~3.7 items per Dimension, and every Dimension carries **at least one Reverse-keyed item** — worded so agreeing means *less* of the Dimension — which is also what the Pattern flag uses to catch a flat block.

### Why it matters

Sets the section's length. With five Dimensions and eight facets: **3 items per facet = 24 items** plus the Safeguard checklist — about half of v1's ~49 team answers. 2 per facet = 16, which is short but makes every facet a two-item mean.

### Options

| Option | Pros | Cons |
|---|---|---|
| **A. 3 per facet (24 + checklist); ≥1 reverse-keyed per Dimension** | Every facet mean has three items behind it. Reverse-key rule carries unchanged, so the Pattern flag works on this block too. ~25 answers is a section, not a survey. | — |
| **B. 2 per facet (16 + checklist)** | Shortest. | Two-item facets; one badly-worded item moves a facet a full point. |
| **C. 4 per facet (32 + checklist)** | Most robust means. | Back toward v1's length, on the block the pilot found long. |

### My recommendation

**A.** The Framing rule's balance floor (at least one less-AI-than-today item per block) is met automatically — the low-pole items on *Agent latitude* and *Pace* are exactly that — so no extra rule is needed here.

### Your answer

: Yeah, I think we can go with your recommendation on this one. 

---

## Q8 — Probes and Edge markers at team level?

### What this is

v1 put five Probe items — extreme, unscored, one pole each — in the Future-state block, raising an **Edge marker** when someone endorsed one. The rule was *"the poles where an edge position is a real constraint on the six-month plan."* At team level the candidates would be *Agent latitude* high (*"agents merge to main with nobody reading the diff"*) and *Verification* low.

### Why it matters

A probe costs a row per Dimension it sits on and needs the Edge marker machinery extended to a new block. On a **named, scored** team Dimension, though, a *Strongly agree* on the highest-pole scored item is already visible per person in the distribution — the thing a probe was invented to surface.

### Options

| Option | Pros | Cons |
|---|---|---|
| **A. No team probes** — the scored items' own extremes do the job; Edge markers stay a personal-block concept | Keeps the section at ~25. Nothing new to build in scoring or dashboard. | No unscored "sentence somebody owns" for the team block. |
| **B. Two probes** — Agent latitude high, Verification low | The two edges that most constrain what the team can adopt get an explicit marker. | +2 rows, Edge marker per team Dimension in the Rubric and dashboard; and each probe is a scored item's extreme twin sitting rows away on the same scale — the near-duplicate problem #6 hit. |

### My recommendation

**A.** If reading the results shows the team wants a named edge, a probe is a one-row addition later.

### Your answer

: Yeah, let's go with your recommendation here again. 

---

## Q9 — What `CONTEXT.md` gains

### What this is

The glossary needs the new construct named before the rubric and bank tickets write to it. Proposed:

| Term | Definition (gist) | Replaces / touches |
|---|---|---|
| **Team section** | The single-pass block of team-voice items answered on the Agreement scale; scores the Team Dimensions. | The v1 "Future-state section, Team stance" reading. |
| **Team Dimension** | A scored 1–5 Dimension about how the team should work, measured once, in team voice. Five: Transparency, Verification, Agent latitude, Pace, Shared practice — each a bundle of the facets in Q6. | New subsection beside *Dimensions (v1)*. |
| **Norm score** | A Respondent's score on a Team Dimension — the norm they would set. Aggregated into a Team score like any Dimension; spread is the finding. | *Future score* stops applying to the team block; *Team score* extends to "current, future, or norm". |
| **Agreement scale** | The team section's five-point scale, *Strongly disagree … Strongly agree*. | Third scale family after Behaviour/Attitude and Desirability. |

*Topic* is deliberately **not** a term — the eight are facets, and *Facet* already exists.

### Why it matters

These names go into the rubric level text, the scoring rules and the dashboard labels. Renaming later touches all three.

### Options

Accept, or rename. The only real alternative I considered was calling the per-Respondent value a *Team score*, which collides with the existing aggregate term.

### My recommendation

Accept as written. If a name grates, say which — the definitions are the decision, the labels can move.

### Your answer

: Yeah, I think that's fine. 

---

## Anything else

A pole in the Q6 table that reads as the "wrong" end to you; a topic that landed under the wrong Dimension; or anything the scored choice implies that I haven't priced in.

### Your answer

:

---

# Round 3 — the written spec

**Round:** 3 of 3 — one question. React to the draft; the ticket closes on your word.
**How to use:** read [`survey/team-section.md`](../../survey/team-section.md). Mark anything wrong inline under Q10, or say it's ready.

**What round 2 settled**

- **Q6 → A, read from *"I like these a lot. Let's include all eight here."*** — the five-Dimension table you liked, with **all eight topics as its facets** (they were all in it). If you meant eight Dimensions one-per-topic, say so under Q10 and the spec's table splits; the poles stay.
- **Q7 → A.** 3 items per facet → 24 scored items + the checklist, ≥1 reverse-keyed per Team Dimension.
- **Q8 → A.** No team probes, no Edge markers in this block.
- **Q9 → accepted.** *Team section*, *Team Dimension*, *Norm score*, *Agreement scale*; *Topic* is not a term.

**What was written** (working tree, uncommitted — your commit):

- `survey/team-section.md` — the rules, the five Team Dimensions with poles and facets, facet definitions, shape (25 answers vs ~49), how it's read, what dies, what each downstream ticket inherits.
- `CONTEXT.md` — **Team section**, **Norm score**, **Agreement scale** added; **Team score** extended to *current, future, or norm*; a new **Team Dimensions (v2)** subsection with the five; *Safeguard item* re-pointed to its three v2 homes.

**What closing does** — so you can object now rather than after: two tickets graduate from the fog, both unblocked the moment this closes: **Team Dimension rubric levels** (five × five level texts, team voice, between the poles) and **Team item bank** (24 + checklist, to the Framing rule). The map's Notes get the Safeguard clause. *Rubric v2* stays in the fog for the personal side only.

---

## Q10 — Is the written spec the section?

### What this is

The doc is the decision now. Two things worth a second look:

1. **The poles table.** Each pole is meant to be a position a team could defend out loud. If one reads as a confession rather than a position, the axis is wrong and the level text built on it will be too.
2. **The facet pairings** — *Limits* under Agent latitude, *Learning & skill* under Shared practice. Those were the two judgement calls.

### My recommendation

Ship it as written. Anything you change in the doc is the decision; I'll mirror it into the glossary if it moves a definition.

### Your answer

: Ship it — close #23 and update the map. *(answered in chat, 2026-08-27)*
