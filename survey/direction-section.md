# The Direction section

**Decided** — wayfinder ticket [#24](https://github.com/AndrewGodlewsky/AI-Dev-Survey/issues/24).
Grilling record: [`docs/grilling/issue-24-forward-personal-block.md`](../docs/grilling/issue-24-forward-personal-block.md).
Governed by the [Framing rule](item-framing-rule.md).

The **Direction section** replaces v1's Future-state section — 25 items and 5 probes asked as
*"In six months, I would…"*, twice (for me / for the team). The pilot's objection was not
fatigue: *"I don't know what I'll think in six months, because if I knew, I would be thinking
that now."* The block asked people to forecast a state they have no access to, and they
answered it from the present.

The replacement asks the **same target** — where each person would go on the seven
Dimensions — with a **different question**: concrete ways of working, stated as if they were
already true, and *would you want to work this way*. Purpose, in the author's words: *"how the
person, as an individual developer, thinks AI can help them, or how they want to integrate with
AI … the principles of what they'd be willing to accept and what they're interested in doing,
by asking them questions that will reveal those types of answers."*

---

## The rules

1. **Single row.** Each item is answered once, for the Respondent themself. There is no
   *"the team should"* row — the [Team section](team-section.md) is its own construct — so
   **Stance** no longer exists anywhere in the survey.
2. **The Desirability scale**, unchanged: *Definitely not · Probably not · Unsure · Probably ·
   Definitely* → 1–5. **The prompt changes**: the section description says, in the author's
   words, *"If this were true, how would you feel about working this way?"* and names the
   **six-month planning window once**; each row is answered as *would you want to work this
   way*. The words *six months* never appear in an item.
3. **Scored on the seven Dimensions.** Each item lands on a named facet of Comfort, Trust,
   Fluency, Guardrails, Concern, Autonomy or Craft values — the same facet list as the frozen
   Current-state bank — and produces a **Direction score** per Dimension, computed like any
   Dimension score (facets averaged first, reverse-keys flipped). *"When we're trying to
   understand grouped values, we need to understand them on a dimensional axis."*
4. **Gap survives: `Direction − Current`** per Dimension. Positive = would want more of it
   than practised today; negative = would pull back. It is **appetite minus practice, never a
   forecast**, and every Gap is now the "softer" kind v1 flagged for Fluency and Craft — a
   Desirability answer against a Behaviour/Attitude one. Read to the nearest half point.
5. **Twenty items** — two per single-idea Dimension, one per facet on the two bundles:

   | Dimension | Items | Facets covered |
   |---|---|---|
   | Comfort | 2 | — |
   | Trust | 2 | — |
   | Fluency | 2 | — |
   | Guardrails | 5 | one per facet, as v1's forward bank mapped them: review + testing · disclosure · off-limits areas · enforcement strength · the "nothing extra" pole (reverse-keyed) |
   | Concern | 5 | one per risk (security · IP/licensing · skill atrophy · job impact · maintainability) |
   | Autonomy | 2 | — |
   | Craft values | 2 | — |

   **At least one Reverse-keyed item per Dimension** — the less-AI worlds — which also meets
   the Framing rule's balance floor. One fewer item anywhere breaks Gap on a bundle.
6. **Form follows the facet.** **Scenario item** by default — a present-tense world
   (*"AI writes the first draft of every PR I open"*). **Direction item** (*"I want to…"*)
   where the facet is about the Respondent's own skill or values — Fluency, Craft values, parts
   of Guardrails — where a world-sentence comes out contrived. **No Value items**: this block is
   concrete-only; values are read off reactions, never asked flat. Every item passes the
   Framing rule's five-check test.
7. **Five Probe items**, re-tensed from forecasts to present-tense worlds at the pole, single
   row, rules 1–7 of `probe-items.md` otherwise unchanged. An **Edge marker** fires at 4–5 —
   **one per Respondent per probe**, no stance split.
8. **Two Safeguard askings live here** — *willingness* (which positions would you accept) and
   *learning interest* (which would you want to know more about) — on the **symmetric list**
   below. Together with the Current-state asking they yield **Levers** and **Holds**.

## The symmetric Safeguard list

The v1 list leaned: *"which of these do you accept **instead of reading it yourself**"*, with
one way to read and six ways not to. *"I need these to be net-neutral questions so that users
don't tend towards the answers that I would tend towards, being pro-AI."*

**Stem (draft):** *For AI-written output, which of these count, for you, as enough?*

**Options — reading positions and checks as equal options, in no escalating order:**

- A person reads all of it
- A person reads the risky parts
- Another person reviews it
- The test suite passes
- A type check or schema validation covers it
- An automated security or lint scan covers it
- It's easy to roll back if it's wrong
- The blast radius is small (docs, internal tooling, non-production)

The same list is used by **all three askings** — today (Current-state section), willingness
(this section), and the team norm (Team section, under Verification) — because Levers and
Holds are subtractions and need identical lists on both sides. **This touches the
Current-state section's Safeguard item 1**, which is not one of the 26 frozen scored items but
does sit in that section.

| Signal | How it's read |
|---|---|
| **Lever** | A check ticked in the willingness asking, not in today's. What would move this person — derived, never asked. |
| **Hold** | A reading position ticked in both askings. The line does not move; a position, not an obstacle. The symmetric twin of a Lever. |
| **Learning interest** | Ticked in the learning asking, not in willingness. Self-reported, actionable, no admission of ignorance. |
| **Inconsistent** | *A person reads all of it* ticked **alongside any check** in the same asking — reading everything and a check standing in for reading is a contradiction. *Reads the risky parts* + a check is a coherent position and is **not** flagged. Flagged, never resolved by rule; Levers and Holds are not computed for that person. |

The Framing rule's option-list mechanics gain a fourth line from this: **the list is
symmetric** — both sides of the position are real options, never one escape and six
alternatives.

## Shape

| | v1 (this block) | v2 |
|---|---|---|
| Dimension items | 50 (25 × 2 stances) | **20** |
| Probe items | 10 (5 × 2) | **5** |
| Safeguard askings | 3 | **2** (the team one moved to the Team section) |
| Coverage grid, forward | 19 + 19 | [#25](https://github.com/AndrewGodlewsky/AI-Dev-Survey/issues/25) decides |
| **Answers in this section** | 81 (+19 team grid) | **27** (+ whatever #25 keeps) |

Whole survey: v1 152 → v2 **103–122** answers, ~22–33 minutes. *"The team shrinkage is
enough … If we do [need more], I'll come back and we'll address it later."*

## Reading it

| Signal | How it's read |
|---|---|
| **Direction score** (per Respondent, per Dimension) | How much this person would want to work that way. Shown by initials. |
| **Gap** | `Direction − Current`. The direction matters more than the size; ±0.5 on a two-item Dimension is one item moving a point. |
| **Layered view** | Every person's *today* and *direction* joined by a connector, over the team means of both. **No team-stance target line** — that quantity no longer exists. |
| **Edge marker** | One per person per probe; the probe table stays. |
| **Levers / Holds / learning interest** | Per person, per option, from the two askings plus today's. |
| **Pattern flag** | A flat block (same answer down it, reverse-keyed items included). The *stance-identical* check is gone with Stance. |

## What dies with this

- The *"In six months, I would…"* stem, and forecasting anywhere in the survey.
- **Stance**, **Stance gap**, **norm gap**, and the team-stance target line in the Layered view.
- **Future score** and **Future-state section** as terms — replaced by *Direction score* and *Direction section*.
- The leaning Safeguard list and the "principle answer first" special slot — reading is an option like any other now.

## What this hands downstream

- **Direction item bank** *(new ticket)* — 20 items + 5 re-tensed probes + the two Safeguard askings on the symmetric list, drafted to the Framing rule; per-facet allocation above; Scenario by default, Direction form for skill/values facets.
- **[#25](https://github.com/AndrewGodlewsky/AI-Dev-Survey/issues/25) Coverage grid** — now unblocked. The forward Coverage pass, if kept, is a *direction* pass on the same 19 rows, single row, no team pass; a Coverage Gap would read like Gap above.
- **Rubric v2, personal side** *(new ticket)* — rename Future → Direction throughout; Gap read as appetite minus practice, all "softer"; §6.2 rewritten for the symmetric list, Levers, Holds and the narrowed inconsistency; every Stance-gap section removed.
- **[#28](https://github.com/AndrewGodlewsky/AI-Dev-Survey/issues/28) Scoring rules v2** — Direction score = same rules as Current; Gap; Edge marker per person; Lever/Hold/inconsistent on the symmetric list; no Stance anywhere.
- **[#26](https://github.com/AndrewGodlewsky/AI-Dev-Survey/issues/26) Local app** — the Layered view loses its target line and its stance panel; the Safeguard panel gains Holds.
- **[#29](https://github.com/AndrewGodlewsky/AI-Dev-Survey/issues/29) Assemble** — one section, one scale, 27 answers, the planning-window sentence in the description; Safeguard item 1's option list changes in the Current-state section.
