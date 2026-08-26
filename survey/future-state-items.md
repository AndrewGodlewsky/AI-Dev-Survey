# Future-state item bank

**DRAFT for reaction** — wayfinder ticket [#6](https://github.com/AndrewGodlewsky/AI-Dev-Survey/issues/6).

The Dimension items for the Future-state section, plus the five Probe items specified in
[#8](https://github.com/AndrewGodlewsky/AI-Dev-Survey/issues/8). Mirrors the Current-state
bank ([#5](https://github.com/AndrewGodlewsky/AI-Dev-Survey/issues/5), `current-state-items.md`).

**25 scored items + 5 probes = 30 items, each answered twice = 60 rows.**

## The scale and the two rows

Every item is one Likert block with two rows, both on the Desirability scale fixed by
[#2](https://github.com/AndrewGodlewsky/AI-Dev-Survey/issues/2):

| | 1 | 2 | 3 | 4 | 5 |
|---|---|---|---|---|---|
| **For me** — "In six months, I would…" | Definitely not | Probably not | Unsure | Probably | Definitely |
| **For the team** — "In six months, the team should…" | Definitely not | Probably not | Unsure | Probably | Definitely |

Items below are written as **stems** that complete both rows. Where a stem needs different
wording per stance, both are given.

**R** = reverse-keyed, scored `6 − answer`, same as its Current-state twin.

---

## Three things the mirror does *not* do 1:1

A straight copy of the Current bank onto the Desirability scale breaks in three places. Each
is a decision, not an oversight.

### 1. Reverse-keyed items that name an undesirable *state* floor out

A reverse item works in the Current section by describing a position someone holds. On a
Desirability scale it has to describe a position someone could **want**. Two don't survive:

| Current item | Why it can't be mirrored | Future replacement |
|---|---|---|
| **F3** — "When an AI tool doesn't give me what I need, I'm not sure what to change." | Nobody answers "Definitely" to wanting to stay confused. Every Respondent lands at 1, the reverse-key turns that into a uniform 5, and Fluency's future score gains a constant instead of a signal. | **FF3** — "…use AI tools as they come out of the box, without configuring or tuning them." A real low-Fluency *position* (rubric level 2) somebody can genuinely prefer. |
| **V2** — "When a deadline is tight, tests and review are the first things I drop." | Same floor effect, made worse by the fact that responses are named and the team view reaches a manager. Nobody volunteers "Definitely, I'd drop tests." | **FV2** — "…let speed win over polish more often than it does today." Choosable, and says the same thing about Craft without asking anyone to sign a confession. |

These two pairs are **facet-matched, not word-matched**: both ends measure the low pole of the
same Dimension, but the sentences differ. The Gap on those two items is correspondingly softer
and should not be read as precisely as the others.

### 2. Guardrails mirrors on **five** facets, not six

Current **G2** (disclosure endorsed — "people should say…") and **G3** (disclosure practised —
"how often do you tell people…") are one facet asked two ways. That distinction exists only in
the present tense: the future form of both is the same sentence. There is no honest sixth
future item.

So Guardrails' Gap is computed over **five facets**, with G2 and G3 averaged into a single
current disclosure value first.

That was listed as an open call for [#9](https://github.com/AndrewGodlewsky/AI-Dev-Survey/issues/9)
— flat mean over six items, or collapse G2+G3 then mean five. **This ticket makes the collapse
option effectively forced**, since the alternative leaves the current and future means built
from different facet counts. #9 still owns the decision; it now has one live candidate.

### 3. The Concern probe and Guardrails FG3 land on the same sentence

#8's Concern probe reads *"…want there to be work here that AI is not allowed to touch at
all."* Guardrails FG3 reads *"…keep parts of our work where AI isn't used at all."* In the
Current section those sat in different sections and one was unscored, so the overlap was
tolerable ([#5](https://github.com/AndrewGodlewsky/AI-Dev-Survey/issues/5) flagged it and kept
it knowingly). **In the Future section they are rows apart, on the same scale, in the same
block.** A Respondent will notice, and one of the two slots is wasted.

**Decided:** the Concern probe is reworded onto its own ground —

> ~~…keep areas where AI is not allowed to be used at all.~~
> **…slow down how fast we adopt AI, because the risks outweigh what we'd gain.**

This is a sharper Concern position than a no-go list, it is a genuine constraint on a six-month
plan, and it stops competing with a scored Guardrails item. It **amends the probe wording
decided in closed ticket [#8](https://github.com/AndrewGodlewsky/AI-Dev-Survey/issues/8)** —
signed off in this session, recorded on #8, and applied to
[`probe-items.md`](probe-items.md). #8's *rules* are untouched: still five probes, one pole
each, Concern still holds the high pole.

---

## Comfort

| ID | R | Stem |
|---|---|---|
| FC1 | | …use AI in most development work. |
| FC2 | | …use AI on work that ends up in production. |
| FC3 | **R** | …keep doing things by hand rather than hand them to AI. |

## Trust

| ID | R | Stem |
|---|---|---|
| FT1 | | …treat AI output as correct by default, checking only when something looks off. |
| FT2 | **R** | …read AI-written code line by line before it is used. |
| FT3 | | …trust AI's output about as much as a colleague's. |

## Fluency

| ID | R | Stem |
|---|---|---|
| FF1 | | …be able to get what's needed out of an AI tool in a try or two. |
| FF2 | | …routinely give AI tools proper context — the right files, rules and docs. |
| FF3 | **R** | …use AI tools as they come out of the box, without configuring or tuning them. |

## Guardrails — five facets

| ID | R | Facet | Stem |
|---|---|---|---|
| FG1 | | Review + testing | …give AI-assisted work more review and testing than hand-written work. |
| FG2 | | Disclosure | …say when a change was mostly written by AI. |
| FG3 | | Off-limits areas | …keep parts of our work where AI isn't used at all. |
| FG4 | | Enforcement strength | …have whatever we agree about AI enforced by our tooling rather than left to judgement. |
| FG5 | **R** | The "nothing extra" pole | …need nothing beyond our current process for AI-assisted work. |

Maps to Current G1 · **G2+G3 collapsed** · G4 · G5 · G6.

## Concern — five risks

Worded as the **vigilance in force**, not as a feeling — nobody sets a target for how worried
they want to be. That framing is the one #4 already adopted for Concern's rubric levels.

| ID | R | Risk | Stem |
|---|---|---|---|
| FN1 | | Skill atrophy | …treat skill erosion as a real risk to watch for. |
| FN2 | | Security | …treat security problems in AI-written code as a live risk to guard against. |
| FN3 | | IP / licensing | …treat licensing and IP exposure from AI-generated code as a live risk. |
| FN4 | **R** | Maintainability | …be relaxed about how maintainable AI-written code is. |
| FN5 | | Job impact | …plan for AI changing what our jobs are. |

## Autonomy

| ID | R | Stem |
|---|---|---|
| FA1 | | …let AI tools edit files and run commands directly. |
| FA2 | **R** | …approve an agent's steps as it goes rather than letting it run on. |
| FA3 | | …hand AI a whole task and come back to a finished change. |

## Craft values

| ID | R | Stem |
|---|---|---|
| FV1 | | …ship only code someone could walk another person through. |
| FV2 | **R** | …let speed win over polish more often than it does today. |
| FV3 | | …hold up a change to fix something only its author would notice. |

FV1 stays deliberately softer than the Craft probe below ("explain every line") — the scored
item and the unscored marker must not be the same sentence.

---

## The five Probe items

Rules from [#8](https://github.com/AndrewGodlewsky/AI-Dev-Survey/issues/8), unchanged:
never scored, never reverse-keyed, one pole each, direction-normalised so **"Definitely" is
always the edge**, and indistinguishable from their neighbours in the block. An **Edge marker**
fires at 4–5, tracked separately per stance.

| ID | Dimension | Pole | *For me* | *For the team* |
|---|---|---|---|---|
| P1 | Comfort | low | …be happy working with no AI tooling at all, the way I worked before it existed. | …be fine going back to no AI tooling at all. |
| P2 | Trust | high | …merge AI-written code I had not read line by line, as long as the tests pass. | …merge AI-written code nobody has read line by line, as long as the tests pass. |
| P3 | Autonomy | high | …let an agent work unsupervised for an hour and only look at the final result. | …let agents work unsupervised for an hour and only review the final result. |
| P4 | Concern | high | …slow down how fast I adopt AI, because the risks outweigh what I'd gain. | …slow down how fast we adopt AI, because the risks outweigh what we'd gain. |
| P5 | Craft values | high | …expect to be able to explain every line of code that ships under my name. | …expect everyone to be able to explain every line that ships under their name. |

**P4 is the amended one** — see finding 3 above. P1, P2, P3 and P5 are #8's wording with light
polish only.

**Length stays at 3 items per single-idea Dimension.** The 50-row Future block is at the top of
the budget and the reduction to 40 is available, but which items to drop is a question the
pilot ([#18](https://github.com/AndrewGodlewsky/AI-Dev-Survey/issues/18)) can answer from data
— which pairs never diverge — rather than a guess made against an untested bank.

---

## What else lives in this section (already decided, not re-drafted here)

| Element | Decided in | Text |
|---|---|---|
| Coverage grid — "In 6 months, for me" and "the team should" passes | [#3](https://github.com/AndrewGodlewsky/AI-Dev-Survey/issues/3) | [`coverage-grid.md`](coverage-grid.md) |
| Safeguard items 2, 3, 4 (future-personal, future-team, learning interest) | [#19](https://github.com/AndrewGodlewsky/AI-Dev-Survey/issues/19) | [`safeguard-items.md`](safeguard-items.md) |

## Length — the whole survey, counted

| Block | Answers |
|---|---|
| Context tools matrix | 5 |
| Current-state Dimension items | 26 |
| Coverage grid — Today | 19 |
| Safeguard item 1 | 1 |
| **Future-state Dimension items (25 × 2 stances)** | **50** |
| **Probe items (5 × 2 stances)** | **10** |
| Coverage grid — 6 months, for me | 19 |
| Coverage grid — 6 months, the team | 19 |
| Safeguard items 2–4 | 3 |
| **Total discrete answers** | **152** |

At 8–12 seconds per Likert row plus section preamble, that is roughly **32–45 minutes** —
right at the top of the map's accepted 35–40. The Future section is the single largest block
and the most repetitive, which is exactly the shape that produces straight-lining.

**Reduction available if wanted:** dropping the five single-idea Dimensions (Comfort, Trust,
Fluency, Autonomy, Craft) from 3 future items to 2 takes the section from 50 rows to 40 and the
survey to 142. The two bundle Dimensions cannot be cut — their items *are* the facets, and
cutting one breaks the Gap.

## What this hands downstream

- **[#9](https://github.com/AndrewGodlewsky/AI-Dev-Survey/issues/9) Scoring rules** — Gap = Future − Current per Dimension, over matched facets: Comfort/Trust/Fluency/Autonomy/Craft 3 items each, Concern 5, **Guardrails 5 (G2+G3 collapsed first)**. Reverse-keys mirror their Current twins: FC3, FT2, FF3, FG5, FN4, FA2, FV2. The FF3 and FV2 Gaps are facet-matched rather than word-matched — softer, and the one-pager should say so.
- **[#12](https://github.com/AndrewGodlewsky/AI-Dev-Survey/issues/12) Scored CSV** — every future value exists twice, once per Stance. Probe answers sit in the non-scoring column family with Edge markers, also per Stance.
- **[#13](https://github.com/AndrewGodlewsky/AI-Dev-Survey/issues/13) Survey document** — 60 rows of one scale is the biggest straight-lining risk in the survey. Interleaving the two Coverage grid passes and the Safeguard items between Dimension blocks is the cheapest mitigation.
- **[#16](https://github.com/AndrewGodlewsky/AI-Dev-Survey/issues/16) Dashboard** — the Personal-vs-Team stance split is the headline reading: "I'd go further than the team should" and its reverse.
- **[#17](https://github.com/AndrewGodlewsky/AI-Dev-Survey/issues/17) How to read the results** — must explain why two Gaps (Fluency, Craft) are softer than the rest.
- **[#18](https://github.com/AndrewGodlewsky/AI-Dev-Survey/issues/18) Pilot** — watch for straight-lining down the Future block, and check FF3/FV2 don't floor out the way F3/V2 would have.
