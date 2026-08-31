# The v2 item banks, explained

**What this is.** A plain-language account of what
[Team item bank](https://github.com/AndrewGodlewsky/AI-Dev-Survey/issues/31) and
[Direction item bank](https://github.com/AndrewGodlewsky/AI-Dev-Survey/issues/32) settled on
2026-08-30, and what those decisions mean for the rest of the project.

**Who it is for.** Anyone picking up this repo who needs to know what the survey now *is* and
why it is shaped that way — without reading thirteen pros/cons tables.

**Where the detail lives.** The decision record with the full working is
[`grilling/issue-31-32-item-banks-resolution.md`](grilling/issue-31-32-item-banks-resolution.md).
The rejected alternatives are in the two round-1 records,
[`grilling/issue-31-team-item-bank.md`](grilling/issue-31-team-item-bank.md) and
[`grilling/issue-32-direction-item-bank.md`](grilling/issue-32-direction-item-bank.md). The item
text itself is [`../survey/team-items.md`](../survey/team-items.md) and
[`../survey/direction-items.md`](../survey/direction-items.md).

---

## The short version

These two tickets wrote **every remaining sentence a Respondent will read** in v2. Thirteen
judgement calls were put to the author; **all thirteen were accepted as drafted**, so no item
text moved. What did move was four spec files that had fallen behind the decisions above them,
and three constraints that previously had nowhere to live.

**The practical upshot: the survey is now fully written.** Assembling it is a matter of ordering
and layout, not of deciding what to ask.

---

## What the survey now looks like

v2 has four things a Respondent answers. Two of them were frozen by the pilot; two were written
by these tickets.

| Part | Status | Size | Scale |
|---|---|---|---|
| **Current-state section** — me, today | **Frozen** by the pilot (*"the part that worked"*) | 26 scored items | Behaviour / Attitude |
| **Coverage grid** — where AI is involved | Today's pass frozen; a **Direction pass** added by [#25](https://github.com/AndrewGodlewsky/AI-Dev-Survey/issues/25) | 19 rows × 2 passes | Involvement level 1–6 |
| **Direction section** — where I want to go | **Written by [#32](https://github.com/AndrewGodlewsky/AI-Dev-Survey/issues/32)** | 20 scored + 5 probes + 2 checklists = **27** | Desirability |
| **Team section** — what we should require | **Written by [#31](https://github.com/AndrewGodlewsky/AI-Dev-Survey/issues/31)** | 24 scored + 1 checklist = **25** | Agreement |

The whole form lands at roughly **122 answers**, against v1's 152 — and v1's count was inflated
by asking almost everything twice.

**The two new sections are deliberately different questions, not two voices on one question.**
That is the single biggest structural change in v2, and it is a direct response to the pilot's
verdict on v1's team block: *"re-answering all the questions just in a slightly different frame
of mind."*

- The **Direction section** asks *would I want to work this way* — concrete worlds, stated in the
  present tense, answered on a Desirability scale. It scores the same seven personal Dimensions
  as the Current-state section, so **Gap = Direction − Current** still subtracts like for like.
- The **Team section** asks *should this be our rule* — norms, answered on an Agreement scale. It
  scores five **new** Team Dimensions (Transparency, Verification, Agent latitude, Pace, Shared
  practice) that have no personal counterpart at all.

---

## The thirteen decisions, grouped by what they were really about

The questions arrived as thirteen separate item-level calls. They resolve into four themes.

### 1. Where the survey deliberately asks the same idea twice

Four of the thirteen were versions of *"these two sentences are close — is that a bug?"* In every
case the answer was **keep both**, because the near-collision is the instrument working.

| Pair | Why both survive |
|---|---|
| **VE3** (team: *"if the checks pass, a change is good enough to merge without anyone reading it"*) vs **P2** (personal probe: *"I merge AI-written code I have not read line by line, as long as the tests pass"*) | This is the most valuable disagreement the survey can produce. *"I'd merge unread, but the team shouldn't"* is a real and common position, and it is invisible unless you ask both. |
| **TR5 / P5**, **SP5 / D-N1**, **VE2 / D-T2** | Three subjects out of twenty-four appear in both halves. v1's failure was twenty-five out of twenty-five. Personal-vs-team divergence on these three is a finding. |
| **D-T2** moved *off* the line-by-line sentence | Here the answer went the other way: the Trust **probe** already owns that exact sentence, and a scored item sitting a few rows from it would have wasted one of Trust's two slots. The scored item moved; the probe kept the ground. |
| **D-A2** moved *off* step-approval | Same reasoning. The Autonomy probe owns *duration* (*"unsupervised for an hour"*), so the scored item took the Advisor position instead. |

**The rule that emerged:** an unscored **probe** outranks a scored item when they collide, because
a probe produces a sentence somebody has to own in the room, and a scored item can move to
adjacent ground without losing its Dimension.

### 2. Where the specs had simply fallen behind

Four decisions were bookkeeping between tickets that closed in the wrong order — but bookkeeping
with teeth, because each stale line contradicted something a Respondent would read.

- **`team-section.md` rule 7 said all five item forms were legal in the Team section.** They are
  legal, but the Agreement scale makes two of them unusable: agreeing with a present-tense world
  means *this is already true*, which is a current-state question, not a norm. Narrowed to
  **Direction + Value items, plus the Checklist**.
- **`team-section.md` rule 6 described the old seven-option Safeguard list**, a *principle answer
  first* slot, and a stem that excluded reading — in a question whose list now offers three ways
  of reading. All three corrected.
- **`safeguard-items.md` still carried the leaning v1 list** and the definition that framed
  safeguards as things accepted *instead of reading the output yourself*. Superseded.
- **The Concern probe still said *"slow down how fast I adopt AI"*** — a comparative against the
  Respondent's present pace, which the Framing rule bans outright. Now **"I hold back on AI,
  because the risks outweigh what I'd gain."**

### 3. Where a known cost was accepted rather than engineered away

Three decisions took a real weakness over a fix that would have cost more. **These are the ones
worth remembering**, because each is a caveat the results have to be read with.

| Weakness | Why it was accepted | What it costs |
|---|---|---|
| **Fluency's two items sit on adjacent axes** (per-task context, tool setup) | The alternatives were worse: a tool-breadth item collides with Autonomy, a failure-mode item re-runs a floor v1 already hit. | If the two never diverge, Fluency's Direction score is one item doubled. **Flagged as the Dimension most likely to need a third item.** |
| **Agent latitude nets two facets that run opposite ways** — *Parallel development* (more = more latitude) and *Limits* (more = less) | Splitting it would mean six Team Dimensions and reopening the section's construct. Concern already works this way: five risks under one mean, read separately too. | **A flat 3 is ambiguous by construction** — indistinguishable from *"agents everywhere in day-to-day code, nowhere near production data"*. The facet view is the primary read. |
| **D-G1 and D-G5 are near-inverses** — extra review vs. nothing extra | Both are named Guardrails facets. Dropping either would make Guardrails' Gap subtract two different things from its frozen twin. | A Respondent who spots the pair may answer the second from the first. Mitigated by wording, and by keeping them apart in the form. |

### 4. Two calls about copy, not items

- **The Direction section gains one line**: *"Some of these describe how a team works rather than
  something you do alone. Answer those the same way: as a world you would or would not want to
  work in."* Two Guardrails items are unavoidably collective — you cannot have a personal CI
  policy — and re-voicing them would have softened the Gap on two facets. Cheaper to explain than
  to rewrite.
- **The Team section keeps** *"We are looking for where we already agree and where we don't."* On
  a named survey the whole team reads, the strongest bias is toward converging on what you think
  the team wants to hear. Saying disagreement is useful is the cheapest counter — and it is true.
  Noted as a close call: it is still a nudge, just pointed at the larger risk.

---

## How this changes the project

### 1. The survey is written. Assembly is now the critical path.

[Assemble the v2 survey document](https://github.com/AndrewGodlewsky/AI-Dev-Survey/issues/29)
became unblocked the moment these two closed — it was waiting on nothing else. Every item text,
every section description, every checklist stem now exists.

But assembly inherited **three hard constraints**, which is new. Ordering used to be cosmetic;
it is now load-bearing:

1. **D-G1 and D-G5 must be far apart** — they are logical inverses on one scale.
2. **VE3 and probe P2 must be in different sections, far apart** — same proposition, two framings.
3. **The Current-state section's Safeguard asking changes** — new stem, new eight-option list.
   This edits the otherwise-frozen section, ruled in scope because the freeze covers the 26 scored
   items and the Coverage grid's today pass, and that asking is neither.

There is also a **straight-lining exposure** to manage: the Direction section is 25 Likert rows on
one scale, the largest single block in v2. Interleaving the Coverage grid's Direction pass and the
Safeguard askings between Dimension groups is the cheapest mitigation.

### 2. Every Gap now reads softer — and three read softer still

`Gap = Direction − Current` survives, but it changed meaning: it is **appetite minus practice,
never a forecast**. Because a Desirability answer is being subtracted from a Behaviour or Attitude
one, [#24](https://github.com/AndrewGodlewsky/AI-Dev-Survey/issues/24) already ruled *every* Gap is
the softer kind.

These tickets added a second tier. **Three Gaps are facet-matched rather than word-matched** —
Fluency, Autonomy, and Concern's job-impact facet — meaning the forward item measures the same
facet as its Current twin, but not the same sentence. Two of those three were chosen deliberately
here, to protect the probes.

**Consequence:** the one-page *How to read the results* has to say plainly which Gaps are soft and
which are not, or someone will read a 0.4 on Autonomy as if it meant what a 0.4 on Guardrails
means. Guardrails is the only fully word-matched Dimension, and that is precisely why D-G1 and
D-G5 were kept despite being awkward.

### 3. The Safeguard checklist became one instrument in four places

This is quietly the most structural outcome. The same eight options are now asked **four times** —
today (Current-state), willingness and learning interest (Direction), and the team norm (Team
section) — with four different stems and **one identical list**.

That identity is not tidiness. **Levers** (a check you would accept but do not today) and
**Holds** (a reading position you keep in both) are computed by *subtraction*, and a subtraction
needs identical sides. Any drift between the four askings silently breaks two of the survey's
most actionable signals.

It also means the list is now symmetric: three reading positions and five checks, interleaved so
neither forms a bloc. v1's list had one way to read and six ways not to — the count itself said
which side was normal.

### 4. Two Dimensions carry a caveat only the pilot can settle

**Fluency** (personal) and **Agent latitude** (team) both shipped with a known, documented
weakness rather than a fix. Both are cheapest to revisit *after* the pilot, and neither reopens a
closed ticket if it changes:

- Fluency may need a third item, if D-F1 and D-F2 turn out to move together.
- Agent latitude may want to be two Team Dimensions, if flat 3s turn out to be common.

Alongside these sit seven smaller **watch items** — individual sentences that passed the framing
test but may still read wrong to a real Respondent (whether AL1 and AL5 describe practices this
team has never done; whether SP3 reads as a position or a grumble; whether D-V1 reads as a craft
value or a documentation habit). None is a defect today. All are listed in the resolution record.

### 5. Downstream tickets now have their inputs

| Ticket | What it received |
|---|---|
| [Team Dimension rubric levels](https://github.com/AndrewGodlewsky/AI-Dev-Survey/issues/30) | The facet content each level must span — **and an instruction that Agent latitude's level text runs opposite for *Limits***, and must not claim the mean says more than it does. |
| [Scoring rules v2](https://github.com/AndrewGodlewsky/AI-Dev-Survey/issues/28) | Both reverse-key lists; the Norm score's 8 facets in 5 unequal bundles; which Gaps are soft; that the team Safeguard asking is counted but never scored and never part of Lever/Hold. |
| [Rubric v2: personal side](https://github.com/AndrewGodlewsky/AI-Dev-Survey/issues/33) | The symmetric list, its interleaved order, and the four stems the Lever/Hold subtraction runs on. |
| [Local app](https://github.com/AndrewGodlewsky/AI-Dev-Survey/issues/26) | The Safeguard panel needs **Holds** beside Levers; the probe table loses its per-stance split; the team panel needs a facet drill-down, which Agent latitude makes mandatory rather than nice-to-have. |

---

## What these tickets did *not* settle

- **Item order, block structure and placement** — [#29](https://github.com/AndrewGodlewsky/AI-Dev-Survey/issues/29), now carrying the three constraints above.
- **What 1–5 means in words** for the five Team Dimensions — [#30](https://github.com/AndrewGodlewsky/AI-Dev-Survey/issues/30) — or the rewritten personal rubric — [#33](https://github.com/AndrewGodlewsky/AI-Dev-Survey/issues/33).
- **The arithmetic** that turns answers into scores — [#28](https://github.com/AndrewGodlewsky/AI-Dev-Survey/issues/28).
- **Anything about the app, the export, or where real data lives** — [#26](https://github.com/AndrewGodlewsky/AI-Dev-Survey/issues/26) and [#27](https://github.com/AndrewGodlewsky/AI-Dev-Survey/issues/27). These tickets never touched the pipeline.

---

## One thing worth knowing if you are new here

Two ideas govern every sentence in both banks, and neither is obvious from the item text alone.

**The Framing rule** ([`../survey/item-framing-rule.md`](../survey/item-framing-rule.md)) says
*nothing the Respondent reads may contain or presuppose a position they are supposed to be moving
toward* — in either direction. Not pro-AI, not pro-craft. It is why there is no *"how far would
you go"*, no *"more than today"*, no *"are you ready to"*. It also governs section copy, headings
and option lists, not just items — which is why two of the thirteen decisions were about a single
sentence of description.

**The survey locates; it never points.** On a named survey read by the whole team and screenshot
for a manager, an item that reveals where the finish line is produces a guarded answer you cannot
tell from an honest one. Every awkward-looking call in these two tickets — the moved items, the
kept near-duplicates, the accepted flat-3 ambiguity — is that principle costing something and
being paid anyway.
