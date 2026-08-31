# Item banks — joint resolution

**Tickets:** [Team item bank](https://github.com/AndrewGodlewsky/AI-Dev-Survey/issues/31) · [Direction item bank](https://github.com/AndrewGodlewsky/AI-Dev-Survey/issues/32)
**Map:** [Map v2: Survey overhaul & local dashboard app](https://github.com/AndrewGodlewsky/AI-Dev-Survey/issues/21)
**Round:** 2 — the resolution. This single file replaces a round 2 in each of the two round-1 records, at the author's request, because the two banks were drafted together and five of the thirteen questions cross between them.
**Answered:** 2026-08-30 — *"For both of the Grill Me sessions I think I want to go with all of your recommendations."*

Round-1 records hold the full options, reasoning and rejected alternatives for every question
below. They are the working; this file is the decision.

- [`issue-31-team-item-bank.md`](issue-31-team-item-bank.md) — Q1–Q6, Team item bank
- [`issue-32-direction-item-bank.md`](issue-32-direction-item-bank.md) — Q1–Q7, Direction item bank

**Outcome: all thirteen recommendations accepted as drafted.** Both *Anything else* questions
returned without changes; the items they flagged are carried to the pilot as watch items rather
than reworded now (below).

---

## What this means for the two banks

Nothing in either bank's **items** moves. Every recommendation was either *keep as drafted* or
*apply the correction the draft already describes*, so `survey/direction-items.md` and
`survey/team-items.md` stand as the item text of v2:

| | Items | Other answers | Total |
|---|---|---|---|
| Direction section | 20 scored + 5 probes | 2 Safeguard askings | **27** |
| Team section | 24 scored | 1 Safeguard checklist | **25** |

What *does* move is four spec files that still describe superseded rules, and three constraints
that had nowhere to live until now.

---

## The decisions

### Direction item bank ([#32](https://github.com/AndrewGodlewsky/AI-Dev-Survey/issues/32))

| Q | Question | Decision | Consequence |
|---|---|---|---|
| **Q1** | Trust: should the reverse item stay off *line by line*? | **D-T2 stays as source-checking.** The Trust probe P2 keeps the line-by-line sentence; a scored item can move without losing the Dimension. | Trust's Gap is facet-matched, not word-matched. |
| **Q2** | Fluency: are two adjacent items one too many? | **Keep D-F1 and D-F2 both.** The tool-breadth alternative picks a fight with Autonomy; the failure-mode alternative re-runs the floor v1 already hit. | **Fluency is flagged to the pilot** as the Dimension most likely to need a third item. |
| **Q3** | Autonomy: the reverse item changed facet — accept the softer Gap? | **D-A2 stays as the Advisor position.** Two clean anchors on *how far AI's hand reaches* beat one hard Gap and a row spent on the probe's ground. | Autonomy's Gap is facet-matched. Probe P3 keeps *duration* to itself. |
| **Q4** | Guardrails: D-G1 and D-G5 are near-inverses — live with it? | **Keep both, separated by wording.** The pair is structural — the frozen bank has it too, so removing it forward would make the Gap subtract different things. | **Constraint handed to [#29](https://github.com/AndrewGodlewsky/AI-Dev-Survey/issues/29): put distance between D-G1 and D-G5 in the form.** |
| **Q5** | Voice: two items say *our*, in a personal section | **Keep both as worlds, and add a one-line clarification to the section description.** Guardrails is the one place the bank is fully word-matched and that Gap is worth protecting; the ambiguity is a copy problem and copy is cheap. | New sentence written and checked against the Framing rule (below). |
| **Q6** | The Safeguard list: interleaved order, and asking 1's stem | **Both as drafted.** Leaving the Current-state asking alone was disqualified — it kills Levers and Holds, which are subtractions and need identical lists on both sides. | `safeguard-items.md` superseded. **Ruled on record: the freeze covers the 26 scored items and the Coverage grid's today pass; Safeguard asking 1 is neither, so it may change.** |
| **Q7** | The Concern probe, amended a second time | **P4 becomes *"I hold back on AI, because the risks outweigh what I'd gain."*** Smallest change that removes the ramp comparative; the residual implication in *hold back* is carried by the scale, not the sentence. | `probe-items.md` amended. Rules on that page untouched — still five probes, one pole each, Concern still high. |

### Team item bank ([#31](https://github.com/AndrewGodlewsky/AI-Dev-Survey/issues/31))

| Q | Question | Decision | Consequence |
|---|---|---|---|
| **Q1** | Only two of the five forms are usable here — narrow the spec? | **Narrow `team-section.md` rule 7 to Direction + Value + Checklist.** A clarification of what the Agreement scale already forces, not a change of mind — nothing in the bank moves either way. | Rule 7 rewritten. See the note on `item-framing-rule.md` below. |
| **Q2** | Agent latitude: is *Limits* a facet, or its own Dimension? | **Keep one Dimension.** Concern is the precedent — five risks under one mean, read separately as well as as a mean — and it works. Five Team Dimensions as decided in [#23](https://github.com/AndrewGodlewsky/AI-Dev-Survey/issues/23). | **The facet view is the primary read for Agent latitude**, and **[#30](https://github.com/AndrewGodlewsky/AI-Dev-Survey/issues/30) is instructed that its level text runs opposite for *Limits*.** A flat 3 on this Dimension is ambiguous by construction and the one-pager must say so. |
| **Q3** | VE3 and the Trust probe say nearly the same thing | **Keep both.** *"I'd merge unread, but the team shouldn't"* is the single most valuable disagreement the instrument can surface, and you cannot surface it without asking both. | **Constraint handed to [#29](https://github.com/AndrewGodlewsky/AI-Dev-Survey/issues/29): VE3 and P2 sit in different sections, far apart.** |
| **Q4** | The Safeguard checklist: three corrections to `team-section.md` rule 6 | **Apply all three** — eight options not seven, interleaved with no special slot, and the new stem. [#24](https://github.com/AndrewGodlewsky/AI-Dev-Survey/issues/24) is the later decision; rule 6 simply hadn't caught up. | Rule 6 rewritten. All four askings now identical, so the team norm is comparable with the personal ones. |
| **Q5** | Cross-section echoes: does the personal/team split hold? | **Keep all three pairs** (TR5/P5, SP5/D-N1, VE2/D-T2). Three subjects out of twenty-four appearing in both halves of a survey about one activity is a long way from v1's twenty-five out of twenty-five. | No change. The personal-vs-team divergence on these three is a finding, not a duplicate. |
| **Q6** | Should the section description say that disagreement is the point? | **Keep the sentence.** *No house position* removes the destination; this removes the incentive to agree with each other, which on a five-to-nine-person named survey is the larger risk. | No change. Noted as a close call — cuttable later if the pilot reads it as a nudge toward differentiation. |

---

## The new copy — Q5's clarification line, checked

Added to the Direction section description, after the *"None of these is a prediction"* paragraph:

> Some of these describe how a team works rather than something you do alone. Answer those the
> same way: as a world you would or would not want to work in.

Checked against the [Framing rule](../../survey/item-framing-rule.md) point 2 — *everything the
Respondent reads* — because section copy is governed even though it is not an item:

| Check | Result |
|---|---|
| **Implied destination** | None. It says nothing about more or less AI, and names no end of the scale as the expected one. |
| **Ramp vocabulary** | None — no *yet, still, ready, eventually, further*, no comparative against today. |
| **Presupposition** | Only that some items are collectively voiced, which is observably true of D-G4 and D-G5. |
| **Consistency with the prompt** | Restates the section's own question (*if this were true, how would you feel about working this way?*) rather than adding a second one. |

It resolves the ambiguity without re-voicing D-G4 and D-G5, which would have softened the Gap on
two of Guardrails' five facets.

---

## Files changed by this resolution

| File | Change | From |
|---|---|---|
| `survey/team-section.md` | **Rule 7 narrowed** — Direction + Value + Checklist are the usable forms; Scenario is legal but unusable on an Agreement scale, Probes excluded by rule 5. | #31 Q1 |
| `survey/team-section.md` | **Rule 6 corrected three ways** — eight options, interleaved with no *principle answer first* slot, and the stem *"For AI-written output, which of these should count, for this team, as enough?"* | #31 Q4 |
| `survey/team-section.md` | **Agent latitude annotated** — facet view is the primary read; the Dimension nets two facets running opposite ways. | #31 Q2 |
| `survey/probe-items.md` | **P4 amended a second time** to *"I hold back on AI, because the risks outweigh what I'd gain."*, with the amendment note; the five probes are re-tensed to present-tense worlds in `direction-items.md`. | #32 Q7 |
| `survey/safeguard-items.md` | **Superseded** — asking 1's stem, the seven-option leaning list and the *principle answer first* mechanic all replaced by the symmetric eight-option list. The v1 reading table is superseded by Lever/Hold/learning-interest/inconsistent in `direction-section.md`. | #32 Q6 |
| `survey/direction-items.md` | Section description gains the Q5 clarification line; Fluency carries the pilot flag; the D-G1/D-G5 separation instruction is recorded for #29. | #32 Q2, Q4, Q5 |
| `survey/team-items.md` | The VE3/P2 separation instruction is recorded for #29; Agent latitude's facet-view read is recorded for #30. | #31 Q2, Q3 |
| `survey/item-framing-rule.md` | One cross-reference added to the *Where it applies* table pointing at `team-section.md` rule 7. **The catalogue is unchanged** — see below. | #31 Q1 |

### Why `item-framing-rule.md` was barely touched

The rule's *Where it applies* table says the Team section permits **all five forms**. That stays
true: *legality* is the rule's claim, *usability* is a property of the Agreement scale the Team
section chose. The two are compatible, and the rule is ADR-backed — changing the catalogue means
reopening [#22](https://github.com/AndrewGodlewsky/AI-Dev-Survey/issues/22), which nothing here
justifies. A drafter reading only the rule would still reach for a Scenario item in the team
block, though, which is the hour Q1 was trying to save, so a cross-reference was added to the
Note column and nothing else.

---

## Constraints handed downstream

These are the decisions that produce no file of their own. They are recorded in the banks and
repeated here so the receiving ticket cannot miss them.

**[Assemble the v2 survey document](https://github.com/AndrewGodlewsky/AI-Dev-Survey/issues/29)**

1. **Put distance between D-G1 and D-G5.** They are logical inverses on the same scale; a
   Respondent who spots the pair may answer the second from the first, which is a soft form of
   the straight-lining [#20](https://github.com/AndrewGodlewsky/AI-Dev-Survey/issues/20) exists
   to catch. Wording separation is done; placement separation is #29's half.
2. **Keep VE3 and P2 far apart.** Same proposition — *do passing checks stand in for reading?* —
   asked once as a team norm and once as a personal edge. The section structure separates them
   anyway; this makes it a requirement rather than a side effect.
3. **The Current-state section's Safeguard asking 1 changes** — new stem, new eight-option list.
   Ruled in scope: the freeze covers the 26 scored items and the Coverage grid's today pass, and
   asking 1 is neither.
4. Block structure, item order, probe placement and checklist placement remain #29's, unchanged.

**[Team Dimension rubric levels](https://github.com/AndrewGodlewsky/AI-Dev-Survey/issues/30)**

1. **Agent latitude's level text must run opposite for *Limits*.** The Dimension bundles
   *Parallel development with agents* (more = more latitude) and *Limits* (more = less latitude).
   Level text has to span both honestly rather than pretending one direction.
2. **A flat 3 on Agent latitude is ambiguous by construction** — it is indistinguishable from
   *"agents everywhere in day-to-day code, and nowhere near production data"*, which is a
   coherent and common position. The facet view is the primary read; the level text should not
   claim the mean says more than it does.

**[Scoring rules v2](https://github.com/AndrewGodlewsky/AI-Dev-Survey/issues/28)**

1. Reverse-keys, Direction section: D-C2, D-T2, D-F2, D-G5, D-N4, D-A2, D-V2.
2. Reverse-keys, Team section: TR3, TR6, VE3, AL3, AL4, AL6, PA2, SP3, SP6.
3. **Three Gaps are facet-matched rather than word-matched and read softer than the other four**
   — Fluency (F3→D-F2), Autonomy (A2→D-A2), Concern's job-impact facet (N5→D-N5) — on top of
   [#24](https://github.com/AndrewGodlewsky/AI-Dev-Survey/issues/24)'s ruling that *every* Gap is
   now the softer kind. Q1 and Q3 above are where two of those three were chosen deliberately.
4. Norm score runs over **8 facets in 5 unequal bundles**: Transparency 2, Verification 1,
   Agent latitude 2, Pace 1, Shared practice 2.
5. The Safeguard team asking is counted, never scored, and is **not** part of Lever/Hold.

**How to read the results**

1. **Fluency is the thinnest personal Dimension** — two items on adjacent axes (per-task context,
   tool setup), and ±0.5 on a two-item Dimension is one item moving a point.
2. **Agent latitude's mean hides a two-directional bundle.** Read its facets.
3. Three Gaps read softer than the rest (list above).

---

## Watch items carried to the pilot

Both *Anything else* questions were returned without changes. These items are structurally sound
and passed the five-check test; the open question is whether they read wrong to a real
Respondent, which only the pilot can answer. **None of them is a defect today.**

**Direction bank**

- **D-C1** carries frequency and stakes in one sentence (*"most of the code I write, including
  the code that ships to production"*). Two ideas, one row.
- **D-N2 beside D-G1** — a named security gate against general added rigour. Distinguishable,
  but neighbours.
- **D-V1** (*"leave code the next person can work on without asking me"*) — does it read as a
  craft value or as a documentation habit?

**Team bank**

- **AL1 and AL5** describe practices this team may not do at all yet (several agents at once;
  agents against `main`). On an Agreement scale they are proposed norms, not reports — but if
  they read as science fiction they collect a shrug at 3.
- **TR2** (*a record of AI-assisted changes beyond the pull request*) is the most speculative
  item in the bank. Is there a real artifact this would live in?
- **SP3** (*time maintaining shared AI setup is time not spent shipping*) is the one item worded
  as a cost complaint. Position, or grumble?
- **PA3** — is *"who decides"* really Pace, or Shared practice wearing a different hat?
- **The Team section's closing line** (*"We are looking for where we already agree and where we
  don't"*) was a close call at #31 Q6. Kept, on the grounds that convergence pressure on a named
  survey is the larger risk — but worth watching for whether it pushes anyone to answer more
  distinctively than they feel.

---

## What is now settled, and what is not

**Settled by these two tickets:** every item text in the Direction and Team sections; the two
section descriptions; the four Safeguard askings and their shared symmetric list; P4's wording;
which forms the Team section can actually use.

**Still open, and deliberately untouched here:**

- Block structure, item order, probe and checklist placement — [#29](https://github.com/AndrewGodlewsky/AI-Dev-Survey/issues/29).
- Rubric level text, both sides — [#30](https://github.com/AndrewGodlewsky/AI-Dev-Survey/issues/30) and [#33](https://github.com/AndrewGodlewsky/AI-Dev-Survey/issues/33).
- The scoring arithmetic — [#28](https://github.com/AndrewGodlewsky/AI-Dev-Survey/issues/28).
- Whether Fluency needs a third item, and whether Agent latitude should have been two Dimensions.
  Both were decided *for now* on the reasoning above; both are cheapest to revisit after the
  pilot, and neither reopens a closed ticket if it changes.
