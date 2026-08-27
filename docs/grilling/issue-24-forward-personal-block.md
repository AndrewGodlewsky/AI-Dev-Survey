# Grilling — Issue #24: Forward personal block

**Ticket:** [Forward personal block: from prediction to direction](https://github.com/AndrewGodlewsky/AI-Dev-Survey/issues/24)
**Map:** [Map v2: Survey overhaul & local dashboard app](https://github.com/AndrewGodlewsky/AI-Dev-Survey/issues/21)
**Round:** 1 of ~3 — seven questions *(round 2 appended below)*
**How to use:** answer inline under each `### Your answer` heading. Free text is fine; you don't have to pick one of the listed options. Then tell me it's ready and I'll read it back and compute the next round.

---

## What is already settled coming in

- **Six months is a direction, not a prediction.** *"I don't know what I'll think in six months, because if I knew, I would be thinking that now."* The block stops asking anyone to forecast a state.
- **But you still want the answer.** Round 2 of charting: *"Ultimately, I still want the answers, as in, where do they think they'll be in six months? … re-asking the same questions, they're going to give the same answers."* The question changes; the thing you want to learn does not.
- **The purpose, in your words** (Framing rule round): *"how the person, as an individual developer, thinks AI can help them, or how they want to integrate with AI … the principles of what they'd be willing to accept and what they're interested in doing, by asking them questions that will reveal those types of answers."*
- **The Framing rule applies, and this block is concrete-only.** Scenario and Direction items (plus Probe and Checklist); **no Value items** — values are read off reactions, never asked flat. Scenarios are present-tense worlds; nothing points; balance floor per block; the five v1 probes need re-tensing if they stay.
- **Single row.** The Team section is its own construct now, so this block has no "the team should" row. *Stance* as a concept dies with that — the glossary edit waits for round 2.
- **The Current-state section is frozen** — 26 items on the seven Dimensions, plus Safeguard item 1 and the "today" Coverage grid. Whatever this block becomes, it sits *next to* that, not instead of it.
- **The dashboard may change.** *"I acknowledge that this will change the dashboard visualization a little bit, and that's fine."*
- **Not this ticket:** the Coverage grid's six-month pass ([#25](https://github.com/AndrewGodlewsky/AI-Dev-Survey/issues/25), blocked on this one) and item wording (the personal item bank, still in the fog).

## What this round holds back

- **Glossary renames** — *Future score*, *Future-state section*, *Stance*, *Desirability scale*'s definition — all depend on Q1 and Q4.
- **How Gap is read** in the how-to-read and the Rubric — depends on Q1.
- **Which facets get which items** — the bank ticket's job, once Q5 sets the count.
- **What the Layered view shows** — [Local app](https://github.com/AndrewGodlewsky/AI-Dev-Survey/issues/26)'s, once Q1 fixes what a person's forward value *is*.

---

## Q1 — What is the block's output: a Direction score on the seven Dimensions, or a profile of preferred worlds? *(the root — everything else hangs on it)*

### What this is

v1's forward block produced a **Future score** per Dimension — the same seven as today — and **Gap = Future − Current** was the survey's core finding. The pilot broke the *question* ("in six months, I would…"), not the *target*: you still want to know where each person would go.

Under the Framing rule, the items become concrete worlds to react to (*"AI writes the first draft of every PR I open"* → Definitely not … Definitely). The question is whether those reactions still **roll up to the seven Dimensions** — so that the Trust scenarios produce a Trust direction, comparable to today's Trust — or whether they are read **one world at a time**, the way Coverage is.

### Why it matters

This decides whether Gap lives. The ticket flags a real objection: Gap needs both ends measuring the same thing. But v1 already subtracted a *Desirability* answer from a *Behaviour/Attitude* answer, and the how-to-read already calls the Fluency and Craft Gaps *softer* for exactly that reason. Scenario items don't make that worse — they replace "would I do X" with "would I want to work in a world where X", which is arguably the more honest end of the subtraction.

### Options

| Option | Pros | Cons |
|---|---|---|
| **A. Direction score on the seven Dimensions** — scenario/direction items written *per facet*, so each Dimension gets a 1–5 **Direction score** ("how much I'd want to work that way"), and **Gap = Direction − Current** survives | Keeps the Layered view (today → direction per person), the Gap rows in the how-to-read, and the Rubric's structure. Sits beside the frozen Current-state on the same axes. *"I still want the answers"* — this is the answer. | Every scenario has to land on a named facet, which constrains the bank. Gap becomes *appetite minus practice* and has to be read that way. |
| **B. Unscored profile of worlds** — each scenario read on its own; no Dimension roll-up; no Gap | Maximum freedom in writing scenarios — any world you want to put in front of people. Nothing to reconcile with today's scales. | Gap dies, the Layered view dies, the Rubric loses its forward half. You learn which worlds people want, but not *where they'd go* on the axes today is measured on. |
| **C. Both** — most items roll up to a Dimension; a few free scenarios are read on their own | The best worlds don't have to fit a facet. | Two reading logics in one block; the free scenarios are the ones most likely to be filler. |

### My recommendation

**A.** It is the only option that gives you what you said you still want, and the cost — writing scenarios that land on facets — is a drafting constraint, not a design compromise. The Current-state bank already lists every facet; the scenarios are written to the same list.

### Your answer

: I think this definitely has to be a directional score based on dimensions because when we're trying to understand grouped values, we need to just understand them on a dimensional access. 

---

## Q2 — Which form leads: Scenario or Direction?

### What this is

Both are legal here. A **Scenario item** states a world and asks for a reaction — *"AI writes the first draft of every PR I open."* A **Direction item** names a practice and asks whether I want it — *"I want to hand whole tickets to an agent and review the result."* Under Q1-A both produce a Desirability answer on a facet; they differ in *who is the subject* — the world, or me.

### Why it matters

The pilot's finding was that "I would…" items get answered from the present. A scenario puts the subject outside the person, which is what makes it answerable on gut without forecasting. But some Dimensions are about the person's own skill or values — Fluency, Craft values — where "a world in which…" gets tortured and "I want to…" is the natural sentence.

### Options

| Option | Pros | Cons |
|---|---|---|
| **A. Scenario by default; Direction where the facet is about my own skill or values** (Fluency, Craft values, parts of Guardrails) | Each Dimension gets its natural form. Worlds for the outward Dimensions (Comfort, Trust, Autonomy, Concern); wants for the inward ones. | Two forms in one block — but they read on the same scale, and the Framing rule test is the same. |
| **B. Scenario only** | One form, purest version of "if this were true, how would you feel." | Fluency and Craft scenarios come out contrived (*"A world in which I tune my tools deeply"*). |
| **C. Direction only** | Closest to v1's grammar. | Closest to v1's failure — "I want to…" is still answered from the present. |

### My recommendation

**A.** The form follows the facet; the bank ticket picks per item, and the test catches the misfits.

### Your answer

: I think we need to go with Selection A here. I think that's fine. 

---

## Q3 — The scale: does Desirability survive, and what is the block's prompt?

### What this is

v1's forward scale is **Desirability** — *Definitely not · Probably not · Unsure · Probably · Definitely* — under the stem *"In six months, I would…"*. With scenarios, the stem changes: the natural prompt is your own phrase, *"If this were true, how would you feel about working this way?"*

### Why it matters

The scale must fit both forms from Q2 and keep 1–5 for the Rubric and for Gap. And the Framing rule's scale check applies: both end labels equally sayable.

### Options

| Option | Pros | Cons |
|---|---|---|
| **A. Keep Desirability; change the prompt** — section prompt *"For each of these: would you want to work this way?"*, answers *Definitely not … Definitely* | Zero change to scale, scoring or Forms. Reads naturally for both a world (*"would you want to work this way"*) and a want (*"I want to…"* — *Definitely*). *Unsure* stays as the honest midpoint. | "Would you want" is a slightly different question from "how would you feel"; the feel is inferred. |
| **B. A feeling scale** — *Very uneasy · Uneasy · Neutral · Keen · Very keen* | Literally "how would you feel." | New scale family; *keen/uneasy* labels carry a whiff of judgement (the scale check is borderline); Direction items don't read on it. |
| **C. Agreement scale, shared with the Team section** | One scale for everything after Current-state. | *Strongly agree* to a described world is a strange answer; loses *Unsure*. |

### My recommendation

**A.** The change is in the prompt, not the scale. Your "how would you feel" line becomes the section description; the rows answer *would you want it*.

### Your answer

: Yeah, let's go with your recommendation here. We need to keep desirability and change the prompt. 

---

## Q4 — How many items?

### What this is

v1: 25 scored forward items (3 per single-idea Dimension; one per facet on the two bundles — Guardrails 5, Concern 5) plus 5 probes, each answered twice = 60 rows. Single row now, and the pilot asked for *"not quite as many … but more perceptive."* Gap on a bundle Dimension needs every facet covered, so the bundles can't shrink; the single-idea Dimensions can.

### Options

| Option | Pros | Cons |
|---|---|---|
| **A. 2 per single-idea Dimension, 1 per bundle facet → 20 items** (Comfort 2 · Trust 2 · Fluency 2 · Autonomy 2 · Craft 2 · Guardrails 5 · Concern 5) | Twenty rows, under half of v1's sixty. Every facet still present, so Gap is intact everywhere. | Two-item means on five Dimensions — one clumsy item moves a Direction score half a point. |
| **B. 3 per single-idea, 1 per facet → 25** (v1's count, single row) | Three-item means; v1's structure kept. | Thirty rows with probes; the pilot's "not quite as many" not delivered. |
| **C. 1 per facet everywhere → 16** | Shortest. | Single-item Dimensions for five of seven; a Gap on one sentence. |

### My recommendation

**A, twenty.** The reverse-key floor (≥1 per Dimension) and the Framing rule's balance floor are both met inside twenty — the reverse-keyed items *are* the less-AI worlds.

### Your answer

: Yeah, I think your recommendation here is fine. Ultimately, as a whole, I would like to shrink the number of questions we are asking down. I think a lot of that shrink is going to come from the team section and also the "me in a future state" section, because I don't think either of those needs quite as many questions. Your recommendation is good, but ultimately I would like the number of total questions in the forum to slightly shrink. 

---

## Q5 — The five Probe items: all, some, or none?

### What this is

Probes survive as a form (Framing rule), and the Team section has none. v1's five sit in this block — Comfort low, Trust high, Autonomy high, Concern high, Craft high — worded as forecasts (*"…merge AI-written code I had not read line by line, as long as the tests pass"*). Re-tensed as present-tense scenarios they pass the test unchanged in substance. Single row now, so an Edge marker is one per person per probe, no stance split.

### Options

| Option | Pros | Cons |
|---|---|---|
| **A. All five, re-tensed, single row** | Edge marker machinery already exists; five rows is cheap; each names a real constraint on a plan. | 25 rows total with Q4-A. |
| **B. Three** — Trust high, Autonomy high, Concern high (the three that constrain what the team can adopt); drop Comfort low and Craft high | Fewer rows; keeps the edges that block a plan. | Comfort-low (*"happy with no AI at all"*) is the one genuinely blocking edge in a team at the low end; dropping it loses the rarest signal. |
| **C. None** — with scenarios, every item is a world; the extreme worlds are just the ends of the scale | Simplest. | Loses the *never scored* property — a probe at 5 is a conversation, a scored item at 5 is a decimal. |

### My recommendation

**A.** Five rows, and the how-to-read's probe table stays.

### Your answer

: I would like to probe for all five. I think that makes sense. 

---

## Q6 — Safeguard items 2 and 4: do Levers survive?

### What this is

Two checklist rows live in this block: **item 2** (*which of these would you accept instead of reading it yourself* — the forward-personal asking, which minus item 1 is the **Lever**) and **item 4** (*which would you want to know more about* — learning interest). The Framing rule fixed that a Lever can only exist by derivation; whether the asking survives is this question.

### Why it matters

The Lever is the one output that says *what would move this person* without ever asking it, and it feeds the how-to-read's most actionable row. Two checklist rows is the cost.

### Options

| Option | Pros | Cons |
|---|---|---|
| **A. Keep both** — re-worded as willingness, not forecast (*"which of these would you accept instead of reading it yourself"*, no "in six months") | Levers, principle holds and learning interest all survive; two rows. | Item 2 must be worded so it isn't a forecast — the bank's job, and the Framing rule test covers it. |
| **B. Keep item 4 only** — Levers die | One row. | Loses the derived "what would move me"; the team Safeguard norm (Team section) is not a substitute — it is about the team, not the person. |
| **C. Drop both** | Zero rows. | Learning interest was the free, non-confessional skills signal. |

### My recommendation

**A.**

### Your answer

: I think that these levers survive, but I would like to maybe restate these so that it is slightly less pointing users towards an acceptable, or what I think is an acceptable, answer. Ultimately, I need these to be net-neutral questions so that users don't tend towards the answers that I would tend towards, being pro-AI. This should be a true neutral way to evaluate. 

---

## Q7 — Where does "six months" live now?

### What this is

*Horizon = six months* is a standing constraint, and v1 wrote it into every forward stem. If the items are present-tense worlds, "six months" leaves the item text. It can still live in the **section description** (*"…the direction you'd want us to take over the next six months"*) and in the how-to-read (*"the Gap is the distance a person would travel in the planning window"*).

### Why it matters

The Framing rule governs the section copy too. A description that says *"where you'll be in six months"* re-introduces the forecast the items just removed. One that says *"the next six months is our planning window — this section asks which ways of working you'd want"* keeps the window without the prediction.

### Options

| Option | Pros | Cons |
|---|---|---|
| **A. Horizon is a planning window, stated once in the section description, never in item text** | Keeps the six-month constraint honest — it is how long the team has to act, not how far people are asked to see. | Someone reading a Gap must be told it is appetite, not a forecast — one line in the how-to-read. |
| **B. Drop six months from the survey entirely** — it lives only in the how-to-read | Simplest survey copy. | The Respondent loses the sense of *why* the direction matters now. |

### My recommendation

**A.**

### Your answer

: Yeah, I think your recommendation is fine, Aaron. 

---

## Anything else

A world you already know you want to put in front of people; a Dimension where you already suspect a scenario will fail the test; or anything the pilot felt that the seven questions above don't reach.

### Your answer

:

---

# Round 2 — length, the neutral checklist, and the names

**Round:** 2 of 3 — three questions. Round 3 is you reacting to the written spec.
**How to use:** same as before — answer inline under each `### Your answer`, then tell me it's ready.

**What round 1 settled**

- **Q1 → A. A Direction score on the seven Dimensions.** *"When we're trying to understand grouped values, we need to understand them on a dimensional axis."* Items are written per facet; **Gap = Direction − Current survives**, read as appetite minus practice.
- **Q2 → A.** Scenario by default; Direction form where the facet is about the person's own skill or values.
- **Q3 → A.** Desirability scale stays; the prompt changes to *would you want to work this way*, with your "if this were true, how would you feel" line as the section description.
- **Q4 → A, twenty items** — 2 per single-idea Dimension, 1 per bundle facet. Plus a standing preference, read back in Q8: *"I would like the number of total questions in the form to slightly shrink."*
- **Q5 → all five probes**, re-tensed, single row.
- **Q6 → Levers survive**, and the Safeguard items must be **net-neutral**: *"slightly less pointing users towards … what I think is an acceptable answer … so that users don't tend towards the answers that I would tend towards, being pro-AI."* Read back in Q9.
- **Q7 → A.** Six months is a planning window, stated once in the section description, never in item text.

**What this round holds back**

- **The spec document** — `survey/<name>.md` (name from Q10), written after this round; round 3 is your reaction.
- **The personal item bank** — graduates from the fog when this closes; it inherits Q1–Q9.
- **The Layered view** — hands to [Local app](https://github.com/AndrewGodlewsky/AI-Dev-Survey/issues/26) as: today → direction per person, team means of both, **no team-stance target line** (that quantity no longer exists).

---

## Q8 — Is the shrink enough, or does the Team section give more?

### What this is

Your Q4 answer: the total should shrink, and you expect the shrink to come from the team section and this block. Here is where v2 stands, counted the way `future-state-items.md` counts v1:

| Block | v1 | v2 | Status |
|---|---|---|---|
| Context tools matrix | 5 | 5 | frozen |
| Current-state Dimension items | 26 | 26 | frozen |
| Coverage grid — today | 19 | 19 | frozen |
| Safeguard item 1 | 1 | 1 | frozen |
| Forward Dimension items | 50 (25 × 2 stances) | **20** | this ticket |
| Probe items | 10 (5 × 2) | **5** | this ticket |
| Coverage grid — forward, personal | 19 | **0–19** | [#25](https://github.com/AndrewGodlewsky/AI-Dev-Survey/issues/25) decides |
| Coverage grid — team | 19 | 0 | cut |
| Safeguard items 2 & 4 (forward personal, learning) | 2 | **2** | this ticket |
| Safeguard item 3 (team) | 1 | 1 | re-homed in the Team section |
| Team Dimension items | — | **24** | decided in [#23](https://github.com/AndrewGodlewsky/AI-Dev-Survey/issues/23) |
| **Total answers** | **152** | **103 – 122** | |

That is a 20–32 % cut before #25 decides the forward Coverage pass. At v1's 8–12 s per row it is roughly **22–33 minutes** against v1's 32–45.

### Why it matters

"Slightly shrink" is met at 122 and comfortably met at 103. The only remaining lever of any size is the Team section's 3-items-per-facet (24), which was your call in #23 three hours ago — going to 2 per facet makes it 16 and reopens one line of that ticket's resolution. This block is already at its floor: twenty is two items per Dimension, and one fewer breaks Gap on the bundles.

### Options

| Option | Pros | Cons |
|---|---|---|
| **A. Enough** — 103–122 is the target; #25 decides the rest | Nothing reopened. Both rewritten blocks are at half or less of their v1 size. | If #25 keeps the full 19-row pass, the form is 122 — "slightly" rather than "a lot". |
| **B. Also cut the Team section to 2 per facet (16 + 1)** → 95–114 | A further 8 rows; the team block becomes the shortest section. | Two-item facet means on eight facets; reopens #23 Q7. |

### My recommendation

**A.** The shrink you asked for is already on the table, and #25 is the right place to decide the last big number — a 19-row grid is the single largest remaining block and the one the pilot didn't complain about.

### Your answer

: I think the team shrinkage is enough. I don't think we need to limit it more. If we do, I'll come back and we'll address it later. 

---

## Q9 — What makes the Safeguard items net-neutral?

### What this is

The current item: *"Which of these, if any, do you accept **instead of reading AI's output yourself**?"* with seven options — *I'd read it myself* first, then six checks (another reviewer · tests pass · easy rollback · schema check · small blast radius · security/lint scan). You said it points toward the pro-AI answer. I think you're right, and it's worth being precise about **where** it points, because the fix differs:

1. **The stem** — *"instead of reading it yourself"* frames not-reading as the thing being asked about; reading is the exception you opt into.
2. **The list** — six ways to skip reading against one way to read. Even unordered and with the principle answer first, the *count* says which side is normal.
3. **The derivation** — *Lever = ticked in future, not today* only counts movement toward accepting checks. Movement the other way (someone who accepts a check today and wouldn't in future) is invisible.

### Why it matters

This is the Framing rule applied to an option list, and it is the one place in the survey where the rule's *symmetric* clause has real work to do. It also fixes what the Framing rule's option-list mechanics say — those three mechanics came from this item, and if the item itself was leaning, the mechanics were incomplete.

### Options

| Option | Pros | Cons |
|---|---|---|
| **A. Re-word the stem only** — *"For AI-written output, which of these count, for you, as enough?"*, list unchanged, *"None of these — a person reads it"* first | Smallest change. Levers derive exactly as before. | The 6-vs-1 list still says which side is normal. |
| **B. Balance the list** — a symmetric option list with reading-side positions as real options, not one escape: *A person reads all of it* · *A person reads the risky parts* · *Another person reviews it* · *Tests pass* · *Schema/type check* · *Security/lint scan* · *Easy rollback* · *Small blast radius* — unordered, no principle-first slot needed because reading is just an option | The list itself is symmetric; nothing is the odd one out. Both directions of movement become visible: a **Lever** is a check accepted in future not today, and a **Hold** is a reading position kept in both. | The "inconsistent" flag (*I'd read it myself* alongside a check) needs redefining — reading the risky parts *and* tests passing is a coherent position now. The Rubric's §6.2 and the how-to-read rows change. |
| **C. A and B** | The stem and the list both neutral. | Same cost as B. |

### My recommendation

**C** — B does the real work and A costs nothing on top. The inconsistency flag becomes narrow and honest: *reads all of it* ticked alongside any check is still a contradiction; anything else is a position. The Framing rule's option-list mechanics gain a fourth line — **the list is symmetric: both sides of the position are real options, not one escape and six alternatives** — and I'll add it to `item-framing-rule.md` as a consequence of this answer, since the rule is closed and this is a consequence of it, not a new form.

### Your answer

: I think your recommendation is fine here. Let's go with that. 

---

## Q10 — The names: what the glossary gains and loses

### What this is

Proposed, so the spec, the bank and the dashboard labels use one vocabulary:

| Term | Proposed | Replaces |
|---|---|---|
| **Direction section** | The forward personal block: single row, Scenario/Direction items on the seven Dimensions, Desirability scale, twenty items + five probes + two checklists. | *Future-state section* |
| **Direction score** | A Respondent's score on a Dimension from the Direction section — how much they would want to work that way. | *Future score* |
| **Gap** | `Direction − Current` per Dimension. Positive = would want more of it than practised today; negative = would pull back. Appetite minus practice — never a forecast. | Same name; the definition loses "within a Stance" and the norm gap. |
| **Horizon** | Six months — the planning window the results are acted on in; stated in the section description, never in item text. | Same name; loses "the future the survey asks about". |
| **Desirability scale** | The Direction section's scale, *Definitely not … Definitely*, answering *would you want to work this way*. | Loses "used identically for the Personal and Team stance rows". |
| **Probe item / Edge marker** | Unchanged in substance; single row, one marker per person per probe. | Loses "answered twice / tracked per Stance". |
| **Hold** *(if Q9-B)* | A reading position kept in both Safeguard askings. | New — the symmetric twin of *Lever*. |
| **Deleted** | **Stance**, **Stance gap**, **norm gap** — no item is answered twice, and no team item shares an axis with a personal one. | — |

### Why it matters

*Stance* is referenced in a dozen places (Rubric, scoring rules, dashboard, how-to-read, the CSV schema that is already retired). Deleting it from the glossary is the signal to every downstream ticket that those references are dead, not dormant.

### Options

Accept, or rename. The one I went back and forth on is *Direction section* vs keeping *Future-state section* — I chose Direction because the word *future* is the forecast the pilot rejected.

### My recommendation

Accept as written.

### Your answer

: Yeah, this is fine. I'm okay with this. 

---

## Anything else

A world you already know you want in front of people; a Safeguard option missing from the balanced list in Q9; or a name in Q10 that grates.

### Your answer

:

---

# Round 3 — the written spec

**Round:** 3 of 3 — one question. React to the draft; the ticket closes on your word.
**How to use:** read [`survey/direction-section.md`](../../survey/direction-section.md). Mark anything wrong inline under Q11, or say it's ready.

**What round 2 settled**

- **Q8 → A.** The shrink is enough: v1 152 → v2 103–122 answers; #25 decides the last big number. *"If we do [need more], I'll come back."*
- **Q9 → C.** Stem re-worded *and* the list balanced — reading positions and checks as equal options; **Hold** as the twin of Lever; inconsistency narrowed to *reads all of it* + any check. The Framing rule gains a fourth option-list mechanic as a consequence.
- **Q10 → accepted.** *Direction section*, *Direction score*, Gap redefined, Horizon as a planning window, Desirability re-scoped, *Hold* added; **Stance, Stance gap, norm gap deleted**.

**What was written** (working tree, uncommitted — your commit):

- `survey/direction-section.md` — eight rules, the per-Dimension item allocation (20), the symmetric Safeguard list with its stem and reading table, shape (27 answers vs 81), how it's read, what dies, what each downstream ticket inherits.
- `CONTEXT.md` — *Survey* now names three blocks; **Direction section**, **Direction score**, **Hold** added; **Gap**, **Horizon**, **Desirability scale**, **Probe item**, **Edge marker**, **Safeguard item**, **Lever**, **Pattern flag** rewritten; **Stance**, **Stance gap** deleted (norm gap with them).
- `survey/item-framing-rule.md` — option-list mechanic 4, *the list is symmetric*; the Levers line updated.
- `survey/safeguard-items.md` — a v2 note pointing at the symmetric list; v1 text left as the reference.

**One thing to notice before you say ship.** The symmetric list has to be used by **all three** Safeguard askings, or Levers and Holds can't be subtracted — and the first asking sits in the **Current-state section**. Safeguard item 1 is not one of the 26 frozen scored items, but it is in the frozen section. I've treated it as in scope for the list change and said so in the spec; if you'd rather the today-asking keep v1's list, Levers die and Holds never exist — say so under Q11.

**What closing does:** two tickets graduate — **Direction item bank** (prototype: 20 items + 5 probes + 2 askings) and **Rubric v2, personal side** (task, blocked on #25); *Coverage grid* (#25) unblocks; the map's fog loses both personal patches.

---

## Q11 — Is the written spec the section?

### What this is

The doc is the decision now. Three things worth a second look:

1. **The symmetric list** — eight options. Is a reading position missing, or a check you'd never accept even in principle (which should still be on the list — the point is that it's *available* to refuse)?
2. **The item allocation** — 2/2/2/5/5/2/2. The bundles can't shrink; the single-idea Dimensions could go to 3 if you'd rather have three-item means.
3. **The Safeguard item 1 question** above.

### My recommendation

Ship it as written, including the Current-state Safeguard list change.

### Your answer

: This looks good — ship it. *(answered in chat, 2026-08-27)*
