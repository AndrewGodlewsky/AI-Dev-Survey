# Team item bank

**Decided** — wayfinder ticket [#31](https://github.com/AndrewGodlewsky/AI-Dev-Survey/issues/31).
Grilling record: [`docs/grilling/issue-31-team-item-bank.md`](../docs/grilling/issue-31-team-item-bank.md)
(round 1, the working) → [`issue-31-32-item-banks-resolution.md`](../docs/grilling/issue-31-32-item-banks-resolution.md)
(the decision).

> **All six questions resolved 2026-08-30 — every recommendation accepted as drafted.** No item
> text moved. Q1 narrowed `team-section.md` rule 7 to the two usable forms; Q4 corrected rule 6
> three ways; Q2, Q3, Q5 and Q6 confirmed the draft. The `Qn` markers below are kept as pointers
> into the round-1 record, which holds the options and the rejected alternatives.

The items for the **Team section**, specified by [`team-section.md`](team-section.md)
([#23](https://github.com/AndrewGodlewsky/AI-Dev-Survey/issues/23)) and governed by the
[Framing rule](item-framing-rule.md) ([#22](https://github.com/AndrewGodlewsky/AI-Dev-Survey/issues/22)).

**24 scored items + 1 Safeguard checklist = 25 answers.**

> **Every item in this bank ran the Framing rule's five-check test and passed.** A failed draft
> was rewritten or dropped and does not appear here. The working — the flip — is shown only for
> the items the drafter was unsure about, in the grilling record linked above.

---

## The scale

| | 1 | 2 | 3 | 4 | 5 |
|---|---|---|---|---|---|
| **Agreement** | Strongly disagree | Disagree | Neither agree nor disagree | Agree | Strongly agree |

Both end labels are equally sayable. Single pass, team voice, no personal row.

**R** = reverse-keyed, scored `6 − answer`. **Form** = `D` Direction · `V` Value.

### Only two forms are usable here — a finding, not a choice

`team-section.md` rule 7 says all five forms are legal in this block. In practice the
**Agreement scale removes two of them**:

- A **Scenario item** is defined as a present-tense world answered on the **Desirability** scale
  — *would you want to work this way*. Put the same sentence on an Agreement scale and agreeing
  means *this is how things already are*: a current-state question, which breaks rule 1's single
  norm pass.
- **Probe items** are excluded outright by rule 5.

That leaves **Direction items** (*"the team should…"*) and **Value items** (a principle stated
flat as a proposed norm — legal here and nowhere else), plus the one Checklist. **Q1.**

## The section description

Draft. Checked against the Framing rule's point 2 (*everything the Respondent reads*).

> ### The team
>
> This section is about how we work as a team — not about you.
>
> Each statement is a norm somebody could propose for this team. Say how much you agree with it.
>
> There is no house position. Some statements ask for more process, some for less, and both are
> real answers. We are looking for where we already agree and where we don't.

**Q6** covers whether that last sentence changes how people answer.

---

## Transparency

*How much the team requires AI's role in work to be visible and personally owned.*
**1** — AI's role is invisible, ownership diffuse. **5** — every contribution labelled and
personally owned.

### Disclosure & provenance

| ID | Form | R | Item |
|---|---|---|---|
| TR1 | D | | It should be clear which *parts* of a change AI wrote, not just that AI was involved. |
| TR2 | D | | The team should keep a record of which changes were AI-assisted, beyond the pull request itself. |
| TR3 | V | **R** | What matters is whether a change is right, not how it was produced. |

**TR1 is deliberately about granularity, not existence.** *"A pull request should say when AI
wrote most of it"* was the first draft and it collides with the frozen G2 (*"People should say
when a change was mostly written by AI"*) and with the Direction section's D-G2. Granularity is
a genuinely different norm and the sentence is unmistakably its own.

### Ownership & accountability

| ID | Form | R | Item |
|---|---|---|---|
| TR4 | V | | Whoever merges a change owns it, whatever wrote it. |
| TR5 | D | | Someone on the team should be able to explain any AI-written change that ships. |
| TR6 | V | **R** | When AI-written code causes a problem, that is a tooling failure rather than anyone's mistake. |

**TR6 is the low pole stated exactly as the spec describes it** — *"ownership … by the system"*.
It is a real position (a team that treats defects as process failures rather than personal ones
is a recognised and defensible culture), which is what stops it being a strawman.

**TR5 sits beside the personal Craft probe P5** (*"explain every line of code that ships under my
name"*). Personal against team, Desirability against Agreement, different section. **Q5.**

## Verification

*How much human review the team requires of AI output.*
**1** — automated checks are enough. **5** — a human reads every line.

| ID | Form | R | Item |
|---|---|---|---|
| VE1 | D | | A pull request that AI mostly wrote should be reviewed by someone who didn't run the agent. |
| VE2 | D | | Before asking for review, the author should have read the AI-written parts themselves. |
| VE3 | V | **R** | If the automated checks pass, a change is good enough to merge without anyone reading it. |

**VE1 avoids the review-volume sentence.** *"An AI-heavy pull request should get more review than
a hand-written one"* is frozen G1 in team voice. *Who* reviews is a separate norm — it covers the
facet's reviewer-load topic without restating an item that already exists twice in the form.

**VE3 is the closest cross-section echo in the whole survey** — the Trust probe P2 is *"I merge
AI-written code I have not read line by line, as long as the tests pass."* **Q3.**

> **Resolved (Q3, 2026-08-30): both kept, with an instruction to
> [#29](https://github.com/AndrewGodlewsky/AI-Dev-Survey/issues/29) — VE3 and P2 sit in different
> sections, far apart.** Same proposition (*do passing checks stand in for reading?*) asked once
> as a team norm on the Agreement scale and once as a personal edge on the Desirability scale.
> Keeping both is what makes *"I'd merge unread, but the team shouldn't"* visible, and that
> divergence is the single most valuable disagreement the instrument can surface — it cannot be
> surfaced without asking both. Rewording VE3 onto review *depth* was rejected as vaguer than the
> rest of the bank; dropping P2 would reopen
> [#8](https://github.com/AndrewGodlewsky/AI-Dev-Survey/issues/8). Note VE3 is also
> **Verification's only reverse-keyed item**, so removing it would have cost a reword elsewhere.

## Agent latitude

*How freely agents may act in the shared codebase.*
**1** — personal sandboxes, broad no-go areas. **5** — agents act anywhere, including against
`main`.

### Parallel development with agents

| ID | Form | R | Item |
|---|---|---|---|
| AL1 | D | | It should be normal here for several people to have agents working in the codebase at the same time. |
| AL2 | D | | Agents should be free to touch shared code, not only the files one person is working in. |
| AL3 | D | **R** | Agent work should stay on a personal branch until a person has cleaned it up. |

### Limits

| ID | Form | R | Item |
|---|---|---|---|
| AL4 | V | **R** | Some kinds of work here — production data, secrets, releases — should be off-limits to AI as a matter of policy. |
| AL5 | D | | Agents should be able to run against `main`, not only against a branch. |
| AL6 | D | **R** | An agent should need a person's approval before it changes anything outside the task it was given. |

**AL4 names concrete areas on purpose.** *"There should be parts of this codebase AI is not
allowed to touch"* is frozen G4 almost word for word, and the Direction section's D-G3 is on the
same ground personally. Naming the areas makes it a different sentence and a sharper norm.

**Three of six are reverse-keyed**, because the *Limits* facet points against the Dimension by
construction: more limits is less latitude. The block is balanced 3 high / 3 low, which is where
this section's balance floor is met. **Q2** asks whether that makes Agent latitude one Dimension
or two.

> **Resolved (Q2, 2026-08-30): one Dimension, and the facet view is its primary read.** Concern
> is the precedent — five risks under one mean, read separately as well as as a mean — and it
> works. Splitting into *Agent reach* and *Limits* would give six Team Dimensions and reopen
> [#23](https://github.com/AndrewGodlewsky/AI-Dev-Survey/issues/23)'s construct; re-keying the
> *Limits* items to run with the Dimension would be dishonest. **The cost is accepted and must be
> stated, not hidden: a flat 3 on Agent latitude is ambiguous by construction** — it cannot be
> told apart from *"agents everywhere in the day-to-day code, and absolutely nowhere near
> production data"*, a coherent and common position. Two instructions follow: the one-pager says
> to read this Dimension's facets, and
> [#30](https://github.com/AndrewGodlewsky/AI-Dev-Survey/issues/30)'s level text must run
> **opposite** for *Limits*. This was the closest call in either bank and is cheapest to revisit
> after the pilot.

## Pace

*How fast the team adopts, and who sets that pace.*
**1** — the pace of the most cautious member. **5** — the pace of the keenest.

| ID | Form | R | Item |
|---|---|---|---|
| PA1 | D | | The team should try new AI tools as they come out, rather than waiting to see how they land elsewhere. |
| PA2 | V | **R** | The team should move at the pace of whoever is most cautious about AI. |
| PA3 | D | | Anyone here should be able to adopt an AI tool for their own work without the team agreeing to it first. |

**PA1 and PA2 both carry their opposite inside the sentence** — *try as they come out* against
*wait to see how they land*, *most cautious* against its implied twin — so each describes a
position rather than pushing toward one. PA3 covers the facet's *who decides* topic, which is a
different question from *how fast*.

## Shared practice

*How much the team invests in shared AI setup and in staying able to work without AI.*
**1** — everyone picks their own; skill is each person's business. **5** — one shared maintained
setup; the team keeps everyone able to work without AI.

### Shared conventions & tooling

| ID | Form | R | Item |
|---|---|---|---|
| SP1 | D | | The team should keep one shared set of AI instruction files in the repo, maintained like any other code. |
| SP2 | D | | The team should agree on which AI tools we use, rather than each person choosing. |
| SP3 | V | **R** | Time spent maintaining shared AI setup is time not spent shipping. |

### Learning & skill

| ID | Form | R | Item |
|---|---|---|---|
| SP4 | D | | The team should make time to teach each other how we use AI tools. |
| SP5 | V | | The team should deliberately keep everyone able to do the work without AI. |
| SP6 | V | **R** | Keeping your own skills current is each person's responsibility, not the team's. |

**SP3 is the cost position, not a dismissal.** *"How someone sets up their own AI tooling is
their own business"* was the first draft; it is SP2 negated and it duplicates SP6's shape. Cost
against benefit is a separate and honest reason to hold the low pole.

**SP5 is the team-level twin of the personal D-N1** (*"I want to keep doing enough work without
AI to keep my own skills sharp"*). **Q5.**

---

## The Safeguard checklist

One asking, under Verification, **never scored**. The fourth and last asking of the one shared
list — today (Current-state), willingness and learning interest (Direction), and this one.

> **For AI-written output, which of these should count, for this team, as enough?**

Same eight options, same interleaved order as
[`direction-items.md`](direction-items.md):

- The test suite passes
- A person reads all of it
- It's easy to roll back if it's wrong
- Another person reviews it
- A type check or schema validation covers it
- A person reads the risky parts
- The blast radius is small (docs, internal tooling, non-production)
- An automated security or lint scan covers it

**This corrects `team-section.md` rule 6 in three ways**, all of them consequences of
[#24](https://github.com/AndrewGodlewsky/AI-Dev-Survey/issues/24) landing after
[#23](https://github.com/AndrewGodlewsky/AI-Dev-Survey/issues/23):

| Rule 6 says | Corrected to | Why |
|---|---|---|
| *"same **seven** options"* | eight | #24 replaced the leaning seven with the symmetric eight |
| *"principle answer first"* | interleaved, no special slot | With a symmetric list, reading is an option like any other |
| stem: *"…as enough, **without an individual reading the output**?"* | the stem above | *Without reading it* is the exact lean #24 removed — and three of the eight options now **are** reading positions, so the old stem contradicts its own list |

**Q4.**

**Read as:** options at least half the team ticks are a draft norm the team can write down. This
asking does **not** enter Levers or Holds — those are subtractions between the personal today and
willingness askings. It is a standalone team norm.

---

## Checks

| Check | Result |
|---|---|
| Items | 24 — 3 per facet across 8 facets |
| Reverse-keyed per Team Dimension | Transparency 2 · Verification 1 · Agent latitude 3 · Pace 1 · Shared practice 2 — **all five covered** |
| Forms used | Direction 15 · Value 9. No Scenario, no Probe (see above) |
| Balance floor | Met — AL3, AL4, AL6 and PA2 are the low-pole items `team-section.md` rule 7 nominated |
| Statement uniqueness | Every statement unique across the whole form; three drafts rewritten for collision (TR1, VE1, AL4 — noted above) |
| Value items and reverse keys | 7 of the 9 reverse-keyed items are Value items — **Q2** |

## What this does *not* settle

- **Block structure and item order** — one Likert block per Team Dimension or one for the whole
  section, and where the checklist sits.
  [Assemble the v2 survey document](https://github.com/AndrewGodlewsky/AI-Dev-Survey/issues/29) owns it.
- **Rubric level text** for the five Team Dimensions —
  [Team Dimension rubric levels](https://github.com/AndrewGodlewsky/AI-Dev-Survey/issues/30). This bank
  fixes what each facet's items measure; that ticket writes what 1–5 mean in words.

## What this hands downstream

- **[Assemble the v2 survey document](https://github.com/AndrewGodlewsky/AI-Dev-Survey/issues/29)** — 24 Likert rows on the Agreement scale plus 1 checkbox question; the section description above; block structure and checklist placement. **One hard placement constraint from the resolution: VE3 and the personal probe P2 sit in different sections, far apart (Q3).**
- **[Scoring rules v2](https://github.com/AndrewGodlewsky/AI-Dev-Survey/issues/28)** — Norm score = mean of facets, facets averaged first, over **8 facets in 5 bundles** (Transparency 2, Verification 1, Agent latitude 2, Pace 1, Shared practice 2). Reverse-keys: TR3, TR6, VE3, AL3, AL4, AL6, PA2, SP3, SP6. Nothing here is a Gap. The Safeguard team asking is counted, never scored, and is **not** part of Lever/Hold.
- **[Team Dimension rubric levels](https://github.com/AndrewGodlewsky/AI-Dev-Survey/issues/30)** — the facet content each level must span is fixed here. **Two instructions from the resolution (Q2): *Limits* points against Agent latitude, so its level text runs the opposite way from *Parallel development*; and the level text must not claim the Agent latitude mean says more than it does — a flat 3 there is ambiguous by construction, and the facet view is the primary read.**
- **[Local app](https://github.com/AndrewGodlewsky/AI-Dev-Survey/issues/26)** — a team panel: five Team Dimensions, mean + spread + per-person by initials, drilling down to 8 facets; the Safeguard team norm is a separate count, not a score.
- **[`team-section.md`](team-section.md)** — rule 6 corrected (three ways, table above) and rule 7 narrowed (two usable forms, not five). ✅ **Applied 2026-08-30** (Q1, Q4).
