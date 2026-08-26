# Current-state item bank

**DRAFT for reaction** — wayfinder ticket [#5](https://github.com/AndrewGodlewsky/AI-Dev-Survey/issues/5).

The scored Dimension items for the Current-state section. Scales and conventions are fixed
by [#2](https://github.com/AndrewGodlewsky/AI-Dev-Survey/issues/2); this file is the wording.

**26 items.** 3 per Dimension, except the two Dimensions the glossary defines as *bundles*:
**Concern gets 5** (one per named risk) and **Guardrails gets 6** (two axes, not one).
Coverage has none: it is a profile scored by the grid, not by items.

## What else lives in this section (already decided, not re-drafted here)

| Element | Decided in | Text |
|---|---|---|
| Context item — tools matrix | [#7](https://github.com/AndrewGodlewsky/AI-Dev-Survey/issues/7) | [`context-items.md`](context-items.md) |
| Coverage grid — current column | [#3](https://github.com/AndrewGodlewsky/AI-Dev-Survey/issues/3) | [`coverage-grid.md`](coverage-grid.md) |
| Safeguard item 1 — "accept today instead of reading it yourself" | [#19](https://github.com/AndrewGodlewsky/AI-Dev-Survey/issues/19) | [`safeguard-items.md`](safeguard-items.md) |
| Probe items | [#8](https://github.com/AndrewGodlewsky/AI-Dev-Survey/issues/8) | **None.** Future-state only. |

---

## The two scales

| Kind | Prompt | 1 | 2 | 3 | 4 | 5 |
|---|---|---|---|---|---|---|
| **B** — Behaviour | "How often…" | Never | Rarely | Sometimes | Often | Always |
| **A** — Attitude | "How well does this describe you today?" | Not at all | Slightly | Moderately | Mostly | Completely |

No N/A. **R** = reverse-keyed, scored `6 − answer`.

---

## Comfort — willingness to use AI in my own development work

| ID | Kind | R | Item |
|---|---|---|---|
| C1 | B | | How often do you use an AI tool in your development work? |
| C2 | B | | How often do you use AI on work that ends up in production? |
| C3 | A | **R** | I'd rather work through something myself than hand any of it to AI. |

C1 is the **overall-frequency** item [#7](https://github.com/AndrewGodlewsky/AI-Dev-Survey/issues/7)
cut from the Context section and required here. C2 separates "uses it for lookups" from
"uses it on work that matters" — the 2/3 boundary in the rubric.

## Trust — confidence that AI output is correct without line-by-line scrutiny

| ID | Kind | R | Item |
|---|---|---|---|
| T1 | A | | I expect code an AI writes for me to be correct. |
| T2 | B | **R** | How often do you read AI-written code line by line before you use it? |
| T3 | A | | I trust AI's output about as much as I'd trust a colleague's. |

T3 is rubric level 4 stated plainly. T2 is the behavioural counter-check on T1 — someone who
says they expect correctness but reads every line is telling you something useful.

## Fluency — practical skill with AI tools

| ID | Kind | R | Item |
|---|---|---|---|
| F1 | B | | How often do you get a usable result from an AI tool within a try or two? |
| F2 | B | | How often do you deliberately give an AI tool context — pointing it at the right files, rules, or docs? |
| F3 | A | **R** | When an AI tool doesn't give me what I need, I'm not sure what to change. |

Fluency is measured by *outcomes and habits*, not by self-rated skill: nobody's gut answer to
"how good are you at prompting?" is worth much.

## Guardrails — how much review, disclosure, testing and policy I want

*High is not "good" — this is how much process the Respondent wants.*

**Six items, because Guardrails is a bundle of a different shape from Concern.** Concern is a
flat list of five risks. Guardrails tangles **two axes**:

- **What is covered** — review · disclosure · testing · where AI may be used at all
- **How hard it is held** — nothing special → informal norm → agreed expectation → written
  rule → enforced in tooling

Rubric levels 1–5 barely move along the first axis; they almost entirely move along the
second. So one-item-per-named-facet — the right fix for Concern — would have left the score
unable to separate rubric 2 from rubric 5. The enforcement axis needs its own item.

| ID | Kind | R | Covers | Item |
|---|---|---|---|---|
| G1 | A | | Review + testing | AI-assisted work needs more review and testing than work someone wrote by hand. |
| G2 | A | | Disclosure — endorsed | People should say when a change was mostly written by AI. |
| G3 | B | | Disclosure — practised | How often do you tell people a change was mostly written by AI? |
| G4 | A | | Off-limits areas | There should be parts of our work where AI isn't used at all. |
| G5 | A | | Enforcement strength | Whatever we agree about AI use should be enforced by our tooling, not left to judgement. |
| G6 | A | **R** | The "nothing extra" pole | Our current process already covers AI-assisted work; it needs nothing extra. |

**G5 carries both poles inside the sentence** — *enforced by tooling* against *left to
judgement* — so it describes a position rather than pushing toward one.

**G2 and G3 are a deliberate pair**: what the Respondent endorses against what they actually
do. People endorse disclosure more than they practise it, and that gap is one of the more
useful readings in the bank. It is also the only Guardrails item on the behaviour scale.

**Review and testing stay together in G1.** On this team's process they ride the same pull
request; the rubric only separates them at level 4, and one item carries both.

**G4 overlaps the Concern probe** ("…want there to be work here that AI is not allowed to
touch at all", [#8](https://github.com/AndrewGodlewsky/AI-Dev-Survey/issues/8)). Kept
knowingly: G4 is a scored Current-state position, the probe is an unscored Future-state
marker, and #8's decision that Guardrails carries no probes stands. Flagged to
[#6](https://github.com/AndrewGodlewsky/AI-Dev-Survey/issues/6) so a third near-identical
sentence doesn't appear.

## Concern — perceived risk from AI-assisted development

*5 = most concerned.*

**Five items, one per risk.** Concern is the only Dimension the glossary defines as a *bundle*
rather than a single idea — "security, IP/licensing, skill atrophy, job impact,
maintainability". Those five worries do not move together: someone can fear deskilling and
shrug at licensing. Sampling two of them would quietly redefine Concern as whichever two got
items, while the rubric kept promising all five. So each named risk gets its own item.

| ID | Kind | R | Risk | Item |
|---|---|---|---|---|
| N1 | A | | Skill atrophy | I worry that leaning on AI will erode my own skills. |
| N2 | A | | Security | AI-written code could introduce security problems we wouldn't catch. |
| N3 | A | | IP / licensing | Using AI-generated code could create licensing or IP problems for us. |
| N4 | A | **R** | Maintainability | Code we write with AI will be just as maintainable as anything else we write. |
| N5 | A | | Job impact | I expect AI to change what my job is within a few years. |

**N4 carries the reverse-key** for this Dimension. It reads naturally in the low-concern
direction, so it doubles as the attention check the old catch-all item was providing.

**N5 is the one to watch.** Responses are named and shared openly, and the team view goes to
your manager — which makes job impact the item most exposed to a guarded answer. It is worded
as *change*, not *threat*, deliberately. If it reads wrong in the pilot
([#18](https://github.com/AndrewGodlewsky/AI-Dev-Survey/issues/18)), dropping it is a one-line
edit and Concern still covers four risks.

**Read the five separately as well as as a mean.** A Concern of 3 can be "mildly worried about
everything" or "alarmed about security, relaxed about the rest", and those need different
responses from the team. The mean is the Dimension score; the five values are the diagnosis.

## Autonomy — how unsupervised AI may act on my behalf

| ID | Kind | R | Item |
|---|---|---|---|
| A1 | B | | How often do you let an AI tool edit files or run commands in your project? |
| A2 | B | **R** | How often do you approve an agent's steps as it goes, rather than letting it run on? |
| A3 | B | | How often do you hand AI a whole task and come back to a finished change? |

A1 = does it act at all (rubric 2→3). A3 = does it act unattended (rubric 4). A2 is the leash,
reversed.

## Craft values — weight placed on general development principles

*Not AI-specific; a lens for reading the other Dimensions.*

| ID | Kind | R | Item |
|---|---|---|---|
| V1 | A | | Code I ship should be something I could walk someone else through. |
| V2 | A | **R** | When a deadline is tight, tests and review are the first things I drop. |
| V3 | A | | I'd hold up my own change to fix something only I would notice. |

V1 is worded to stay clear of the Craft probe ("explain every line that ships under my name") —
see the note to [#6](https://github.com/AndrewGodlewsky/AI-Dev-Survey/issues/6) below.

---

## The bench — drafted, not in the 21

Spares, if a Dimension turns out thin or an item dies in the pilot.

| For | Kind | R | Item | Why it's on the bench |
|---|---|---|---|---|
| Comfort | A | | Reaching for AI is my default starting point on new work. | Overlaps C1/C2 on the same axis. |
| Fluency | B | | How often do you use AI features beyond chat and autocomplete — agents, custom rules, MCP? | Overlaps Autonomy A1. |

## Open questions for the assembly ticket

1. **Block structure.** Forms wants one Likert block per scale, which makes this section two
   blocks: 9 behaviour rows, 17 attitude rows. That is two long grids, against the map's
   "vary question types so Respondents do not stall". Alternatives: split each scale into
   two shorter blocks, or interleave the Coverage grid and Safeguard item between them.
   Belongs to [#13](https://github.com/AndrewGodlewsky/AI-Dev-Survey/issues/13).
2. **Item order within a block.** Not decided here. Grouping by Dimension makes the intent
   obvious and invites consistent answering; shuffling costs nothing to do.

## What this hands downstream

- **[#6](https://github.com/AndrewGodlewsky/AI-Dev-Survey/issues/6) Future-state bank** — every item here needs a Future counterpart *except* where a probe already occupies that ground. Three carries: Craft's ordinary future item must **not** be the probe sentence (V1 is worded to leave it room); **Concern must mirror the same five risks** and **Guardrails the same six items**, because a Gap between means built from different item sets subtracts two different things; and Guardrails' future items must not restate the Concern probe (see G4 above).
- **[#9](https://github.com/AndrewGodlewsky/AI-Dev-Survey/issues/9) Scoring rules** — five Dimension means over 3 items each, plus Concern over 5 and Guardrails over 6; the 7 reverse-keyed items (C3, T2, F3, **G6**, **N4**, A2, V2) flip as `6 − answer` before the mean. **One open call**: G2 and G3 are the same facet (disclosure) asked two ways, so a flat mean gives disclosure ⅓ of the Guardrails score. Averaging G2+G3 into one disclosure value first, then taking the mean of five facets, is the alternative. Decide there, not here.
- **[#12](https://github.com/AndrewGodlewsky/AI-Dev-Survey/issues/12) Scored CSV** — the per-facet values for Concern (5) and Guardrails (6) need to survive into the CSV, not just the two means.
- **[#13](https://github.com/AndrewGodlewsky/AI-Dev-Survey/issues/13) Survey document** — the two open questions above.
- **[#16](https://github.com/AndrewGodlewsky/AI-Dev-Survey/issues/16) Dashboard** — Concern needs a per-risk breakdown alongside its score, and Guardrails a per-facet one; both means hide which facet is driving them. The **G2-vs-G3 gap** (disclosure endorsed vs practised) is worth showing on its own.
- **[#18](https://github.com/AndrewGodlewsky/AI-Dev-Survey/issues/18) Pilot** — watch C1/C2, T1/T3 and A1/A3 for pairs that always get the same answer; one of each pair can go. Watch **N5** (job impact) for guarded answers, and **G1/G6** for whether the reverse-key is reading as a trick.
