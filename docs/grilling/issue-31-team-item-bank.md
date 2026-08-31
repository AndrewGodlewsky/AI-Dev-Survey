# Grilling — Issue #31: Team item bank

**Ticket:** [Team item bank](https://github.com/AndrewGodlewsky/AI-Dev-Survey/issues/31)
**Map:** [Map v2: Survey overhaul & local dashboard app](https://github.com/AndrewGodlewsky/AI-Dev-Survey/issues/21)
**Round:** 1 of 2 — six questions. **✅ Answered 2026-08-30.**
**How to use:** the draft bank is [`survey/team-items.md`](../../survey/team-items.md) — read that first, it is the thing being reacted to. Then answer inline under each `### Your answer` heading below. Free text is fine; you don't have to pick a listed option. Tell me when it's ready and I'll read it back.

> **✅ Resolved — every recommendation below was accepted as drafted.** The answers, the file
> changes they produced and the constraints handed downstream are in
> **[`issue-31-32-item-banks-resolution.md`](issue-31-32-item-banks-resolution.md)** — a joint
> round 2 covering this record and its sibling, because five of the thirteen questions crossed
> between the two banks. The `### Your answer` headings below are left empty on purpose: this
> record is the *working*, kept for the options and the alternatives that were rejected.

> **Sibling ticket:** [Direction item bank](https://github.com/AndrewGodlewsky/AI-Dev-Survey/issues/32) is drafted and waiting on [`issue-32-direction-item-bank.md`](issue-32-direction-item-bank.md). **Q3 and Q5 below touch both banks** — if you'd rather answer the two records together, that's the cheaper order.

---

## What is already settled coming in

- **The structure is fixed** by [Team section](https://github.com/AndrewGodlewsky/AI-Dev-Survey/issues/23): five Team Dimensions, 8 facets, **3 items per facet = 24**, ≥1 reverse-keyed per Dimension, Agreement scale, single pass, team voice, scored. Not renegotiated here.
- **No probes, no Edge markers** in this section (rule 5). If results later show the team wants a named edge, one row can be added then.
- **The Safeguard checklist is re-homed here**, once, under Verification, never scored.
- **Value items are legal here and nowhere else** — a team-level value is a norm being proposed, not a self-report.
- **The Framing rule is not re-litigated per item.** Every item passed the five-check test; this record shows the working only for the calls I was unsure about. Three drafts were rewritten for **collision** with an existing statement rather than for failing the test (TR1 vs G2, VE1 vs G1, AL4 vs G4) — those were mechanical fixes and are not questions here.
- **The balance floor is met** by the low-pole items on Agent latitude and Pace, exactly as rule 7 predicted.

## What this round holds back

- **Block structure, item order, checklist placement** — [Assemble the v2 survey document](https://github.com/AndrewGodlewsky/AI-Dev-Survey/issues/29)'s.
- **Rubric level text** for the five Team Dimensions — [Team Dimension rubric levels](https://github.com/AndrewGodlewsky/AI-Dev-Survey/issues/30). Q2 below hands it one constraint; it decides the rest.
- **The scoring arithmetic** for 8 facets in 5 unequal bundles — [Scoring rules v2](https://github.com/AndrewGodlewsky/AI-Dev-Survey/issues/28).

---

## Q1 — Only two of the five forms are usable here. Narrow the spec?

### What this is

`team-section.md` rule 7 says *"All five forms are legal here."* Drafting found that the
**Agreement scale rules out two of them**:

- A **Scenario item** is a present-tense world answered on the **Desirability** scale — *would
  you want to work this way*. On an Agreement scale, agreeing with *"On this team, agents run
  against main"* means **this is already true** — a current-state question, which breaks rule 1's
  single-norm pass.
- **Probes** are already excluded by rule 5.

So the bank is **Direction items (15) and Value items (9)**, plus the Checklist. Nothing was lost
— every facet is covered — but the spec promises a catalogue the block cannot use.

### Why it matters

Small, but it's the kind of thing that costs an hour later when someone drafts a replacement item
against rule 7 and produces a Scenario that quietly asks a different question than its neighbours.
It also says something real about the two sections: the personal block asks *would you want this
world*, the team block asks *should this be our rule*. Different scales, different forms, by
construction — which is exactly the separation v2 was built to get.

### Options

| Option | Pros | Cons |
|---|---|---|
| **Narrow rule 7 to Direction + Value + Checklist** *(recommended)* | Says what's true; stops a future drafter reaching for a form that can't work | Amends a "Decided" spec |
| Leave rule 7, add a drafting note | Doesn't touch the decision | The note is the correction, just less findable |
| Keep Scenario legal by adding a second scale to the section | Full catalogue available | Two scales in one section for no gain; rule 2 fixes one scale, and the pilot's complaint was repetition |

### My recommendation

**Narrow rule 7.** It is a clarification of what the scale already forces, not a change of mind —
nothing in the bank moves either way. Not a close call.

### Your answer:

---

## Q2 — Agent latitude: is *Limits* a facet, or its own Dimension?

### What this is

Agent latitude bundles two facets, and they point **opposite ways**:

- *Parallel development with agents* — more of it means more latitude.
- *Limits* — more of it means **less** latitude.

So three of the Dimension's six items are reverse-keyed, and the Dimension score is a net of two
things that a team can genuinely want at once: *"agents everywhere in the day-to-day code, and
absolutely nowhere near production data."* That's a coherent, common position, and it scores as
a flat 3 — indistinguishable from someone with no opinion.

### Why it matters

The same problem the frozen Current-state bank solved for Concern by giving each risk its own
item and telling the reader to *"read the five separately as well as as a mean."* Here the facet
view already exists in the dashboard spec, so the diagnosis is available — the question is
whether the **score** is worth having on top of it, or whether it hides more than it shows.

It also feeds [Team Dimension rubric levels](https://github.com/AndrewGodlewsky/AI-Dev-Survey/issues/30) directly:
if Agent latitude stays one Dimension, its level text has to span two facets running in opposite
directions, which is hard to write honestly.

### Options

| Option | Pros | Cons |
|---|---|---|
| **Keep as one Dimension, flag the facet view as the primary read** *(recommended)* | Five Team Dimensions as decided; the facet drill-down already exists in the app spec; Concern has the same shape and works | A flat 3 is ambiguous; rubric level text has to span both directions |
| Split into two Team Dimensions — *Agent reach* and *Limits* | Each scores cleanly; level text is easy | Six Team Dimensions; reopens [#23](https://github.com/AndrewGodlewsky/AI-Dev-Survey/issues/23)'s construct, and the section's shape is downstream of it |
| Keep one Dimension, re-key so *Limits* items run with it | No reverse-key needed in that facet | Dishonest — it would mean "more limits" scores as "more latitude" |
| Keep one Dimension and drop the mean; report Agent latitude as a facet pair only | No misleading number | An unscored Team Dimension contradicts [#23](https://github.com/AndrewGodlewsky/AI-Dev-Survey/issues/23)'s central decision |

### My recommendation

**Keep one Dimension, and hand [Team Dimension rubric levels](https://github.com/AndrewGodlewsky/AI-Dev-Survey/issues/30) an explicit instruction that its level text runs opposite for *Limits*.** Concern is the precedent and it's a good one. But this is a **genuinely close call** — if you'd rather the number be unambiguous than the Dimension count be five, splitting is defensible and now is the cheapest time to do it.

### Your answer:

---

## Q3 — VE3 and the Trust probe say nearly the same thing

### What this is

> **VE3** (team, Agreement, reverse-keyed) — *If the automated checks pass, a change is good
> enough to merge without anyone reading it.*
>
> **P2** (personal, Desirability, probe) — *I merge AI-written code I have not read line by line,
> as long as the tests pass.*

Same proposition: **do passing checks stand in for reading?** One asked as a team norm, one as a
personal edge.

### Why it matters

This is the sharpest instance of the design v2 chose. The whole point of replacing the mirrored
team block was that team and personal are **different questions** — but on this particular
proposition they land close enough that a Respondent may feel they answered it twice, which is
the pilot's original complaint arriving through a side door.

There is also a real argument the other way: *"I'd merge unread, but the team shouldn't"* is
exactly the finding the survey exists to surface, and you cannot surface it without asking both.
It is the single most valuable disagreement in the instrument.

Note VE3 is also **Verification's only reverse-keyed item** — Verification has one facet and
three items, so removing it means rewording another item to carry the reverse-key.

### Options

| Option | Pros | Cons |
|---|---|---|
| **Keep both** *(recommended)* | Produces the "I would, but we shouldn't" reading, which the dashboard was built to show; different scale and voice make them read as different questions | Two similar sentences in one form |
| Reword VE3 onto review *depth* — *"a reviewer should be able to skim an AI-written change if the checks are green"* | Distinct sentence; still Verification's low pole | Weaker as a norm; "skim" is vague where the survey is otherwise concrete |
| Drop the Trust probe P2 | Personal block gets a slot back | Reopens [#8](https://github.com/AndrewGodlewsky/AI-Dev-Survey/issues/8); P2 is the probe most likely to fire |
| Reword P2 onto a different Trust pole | Team item keeps the cleanest sentence | Third amendment to the probe set this map; there isn't an obvious second high pole for Trust |

### My recommendation

**Keep both, and ask [Assemble the v2 survey document](https://github.com/AndrewGodlewsky/AI-Dev-Survey/issues/29) to put them in different sections far apart** — which the section structure does anyway. The pair is the instrument working, not failing. Fairly confident, but you are the one who felt the repetition in the pilot, so your read beats mine here.

### Your answer:

---

## Q4 — The Safeguard checklist: correcting three things in `team-section.md`

### What this is

`team-section.md` rule 6 was written before
[Forward personal block](https://github.com/AndrewGodlewsky/AI-Dev-Survey/issues/24) landed, and
three parts of it are now stale:

| Rule 6 says | Draft corrects to | Why |
|---|---|---|
| *"same **seven** options"* | eight | #24 replaced the leaning seven with the symmetric eight |
| *"principle answer first"* | interleaved, no special slot | With a symmetric list, reading is an option like any other |
| stem: *"which of these should the team accept as enough, **without an individual reading the output**?"* | *"For AI-written output, which of these should count, for this team, as enough?"* | *Without reading it* is the exact lean #24 removed — and three of the eight options **are** reading positions, so the old stem contradicts its own list |

### Why it matters

The stem is the load-bearing one. Left as written, the team asking would offer *"a person reads
all of it"* as an answer to a question that has already excluded reading — which a Respondent
will notice, and which makes the team norm non-comparable with the personal askings on the same
list.

This is bookkeeping between two closed tickets rather than a new decision, but it edits a spec
marked **Decided**, so it should be your call rather than mine.

### Options

| Option | Pros | Cons |
|---|---|---|
| **Apply all three corrections** *(recommended)* | All four askings identical; the team norm is comparable with the personal ones | Edits a Decided spec |
| Apply the list and order, keep the old stem | Smaller edit | Self-contradictory question |
| Ask the team norm on its own list | Team asking tuned to team voice | Kills comparability across the four askings for no gain |

### My recommendation

**Apply all three.** #24 is the later decision and the glossary already records the eight-option list as shared by every asking; rule 6 simply hasn't caught up. Not a close call.

### Your answer:

---

## Q5 — Cross-section echoes: does the personal/team split hold?

### What this is

Three pairs where a personal item and a team item sit on the same subject. Q3 covers the sharpest;
these are the rest:

| Team item | Personal counterpart |
|---|---|
| **TR5** — *Someone on the team should be able to explain any AI-written change that ships.* | **P5** (probe) — *I expect to be able to explain every line of code that ships under my name.* |
| **SP5** — *The team should deliberately keep everyone able to do the work without AI.* | **D-N1** — *I want to keep doing enough work without AI to keep my own skills sharp.* |
| **VE2** — *Before asking for review, the author should have read the AI-written parts themselves.* | **D-T2** — *I check AI's work against the source before I act on it.* |

None is a duplicate sentence and all three pass the uniqueness rule. The question is whether they
*feel* like repetition to someone answering the form in one sitting.

### Why it matters

v1's team block failed because it re-asked the personal questions in team voice. v2's team block
asks about different **topics** — parallel agents, shared tooling, reviewer load, pace — but three
of its 24 items land on subjects the personal block also covers. Three out of twenty-four is a
long way from v1's twenty-five out of twenty-five, and some overlap is unavoidable when both
sections are about the same activity.

The counter-argument is the same as Q3's: the *difference* between someone's personal answer and
their team answer on the same subject is a finding, and the sections are far apart in the form.

### Options

| Option | Pros | Cons |
|---|---|---|
| **Keep all three** *(recommended)* | Personal-vs-team divergence on these three subjects is genuinely interesting; 3 of 24 is not the v1 failure | Three moments of "haven't I answered this?" |
| Reword the team side of one or two onto adjacent ground | Less echo | Each reword costs the facet some directness; the team-voice sentences are currently the more natural ones |
| Reword the personal side instead | Team block stays clean | The Direction bank is already drafted; two of these are its clearest items |

### My recommendation

**Keep all three.** The pilot's objection was to answering *every* question twice, not to three subjects appearing in both halves of a survey about one activity. But you are the person who felt it — if any of these three reads as a repeat to you, say which and I'll move the team side.

### Your answer:

---

## Q6 — Should the section description say that disagreement is the point?

### What this is

The drafted description ends:

> *There is no house position. Some statements ask for more process, some for less, and both are
> real answers. We are looking for where we already agree and where we don't.*

That last sentence tells Respondents, in effect, that **spread is the finding**. `team-section.md`
says the same thing to whoever reads the results (*"a wide spread is the conversation to have"*),
but this puts it in front of the people answering.

### Why it matters

Two effects, pulling opposite ways.

**For:** on a named survey read by the whole team and screenshotted for a manager, the default
pressure is to converge on what you think the team wants to hear. Saying disagreement is useful is
the cheapest counter to that, and it is true.

**Against:** it is still a nudge, and the Framing rule's point 2 covers section copy. Telling
people you are looking for disagreement could make someone answer *more* distinctively than they
feel, which is the same instrument error pointed a third way.

### Options

| Option | Pros | Cons |
|---|---|---|
| **Keep the sentence** *(recommended)* | Counters the strongest bias on a named survey; states a true fact about how results are read | A nudge toward differentiation |
| Cut it, keep *"There is no house position"* | Neutral about the shape of answers while still disowning a target | Leaves the convergence pressure unopposed |
| Replace with something about privacy of interpretation — *"nothing here is scored as right or wrong"* | Reduces the stakes without steering the shape of answers | Slightly redundant with *no house position* |

### My recommendation

**Keep it.** *No house position* removes the destination; this sentence removes the incentive to
agree with each other, which on a five-to-nine-person named survey is the larger risk. **Close
call**, and reasonable to cut if you'd rather the copy say nothing at all about answer shape.

### Your answer:

---

## Anything else

Anything in the bank that reads wrong, sounds unlike this team, or names a practice this team
doesn't actually have. The five-check test catches structure; it doesn't catch an item about
parallel agents on a team that has never run two at once.

Worth a specific look:

- **AL5** (*agents run against `main`, not only a branch*) and **AL1** (*several people's agents
  in the codebase at once*) describe practices this team may not do at all yet. On an Agreement
  scale that is fine — they're proposed norms, not reports — but if they read as science fiction
  they'll get a shrug at 3.
- **TR2** (*a record of AI-assisted changes beyond the pull request*) is the most speculative item
  in the bank. Is there a real artifact this would live in?
- **SP3** (*time maintaining shared AI setup is time not spent shipping*) is the one item worded
  as a cost complaint. Does it read as a position or as a grumble?
- **PA3** — is *"who decides"* really Pace, or is it Shared practice wearing a different hat?

### Your answer:

