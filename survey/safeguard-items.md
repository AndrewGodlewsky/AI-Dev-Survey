# Safeguard items and Levers

**DRAFT for reaction** — wayfinder ticket [#19](https://github.com/AndrewGodlewsky/AI-Dev-Survey/issues/19).
Grilling record: [`docs/grilling/issue-19-conditional-items.md`](../docs/grilling/issue-19-conditional-items.md).

A **Safeguard item** asks which positions a Respondent counts as **enough** for AI-written
output — reading it and automated checks alike, as equal options. It is a plain description of a
position — not a hypothetical, not a condition, and never a question about what would change
their mind.

*(v1 defined it as which checks are accepted **in place of reading the output yourself**. That
framing is the lean [#24](https://github.com/AndrewGodlewsky/AI-Dev-Survey/issues/24) removed —
see the banner below.)*

A **Lever** is a safeguard someone accepts in six months but not today. Levers are
**derived by subtraction**, never asked. That is the whole design: the survey gets the
conditional answer without ever putting a conditional question in front of anyone.

> The ticket that produced this was called *"Conditional items"*. Nothing conditional
> survived the design, so the name did not either.

---

## Framing

> **v2:** the non-leading rule that used to live here is replaced by the
> [**Framing rule**](item-framing-rule.md) ([#22](https://github.com/AndrewGodlewsky/AI-Dev-Survey/issues/22)).
> This is a **Checklist item** under that rule; *"what would have to be true for you to accept
> AI doing X?"* is a threshold item and stays banned. The three mechanics below were written
> for this item and are now general rules for every option list in the survey.

> **v2, [#24](https://github.com/AndrewGodlewsky/AI-Dev-Survey/issues/24):** the seven-option list below leaned — one way to read, six ways not to — and is replaced by a **symmetric list** used by all three askings, with **Holds** as the twin of Levers and a narrower inconsistency rule. See [`direction-section.md`](direction-section.md). The item texts and the reading table below are v1's.

> **⚠️ v2, applied 2026-08-30 — this page's item text is superseded.** The item banks' joint
> resolution ([#32](https://github.com/AndrewGodlewsky/AI-Dev-Survey/issues/32) Q6;
> [`issue-31-32-item-banks-resolution.md`](../docs/grilling/issue-31-32-item-banks-resolution.md))
> settled **all four askings, their stems and their shared list**. The live text is in
> [`direction-items.md`](direction-items.md) (askings 1–3) and [`team-items.md`](team-items.md)
> (asking 4). Three things on this page are dead:
>
> 1. **Asking 1's stem.** *"Which of these, if any, do you accept today **instead of reading AI's
>    output yourself**?"* is the lean #24 removed, and it contradicts its own list now that three
>    of the eight options **are** reading positions. Replaced by *"For AI-written output, which of
>    these count, for you, as enough **today**?"* **This edits the Current-state section** — ruled
>    in scope, because the freeze covers the 26 scored items and the Coverage grid's today pass,
>    and Safeguard asking 1 is neither. Leaving it alone was the one option disqualified outright:
>    Levers and Holds are **subtractions**, and a subtraction needs identical lists on both sides.
> 2. **The seven options.** Replaced by the symmetric eight, interleaved so the three reading
>    positions land at 2, 4 and 6 and neither group is a bloc.
> 3. **Mechanic 2, *the principle answer comes first*.** Retired — with a symmetric list, reading
>    is an option like any other and does not need the front. Mechanics 1 and 3 below (ramp ban,
>    ticking the same boxes is valid) stand, and #24 added a fourth: **the list is symmetric**.
>
> Everything else on this page is untouched: Levers stay derived by subtraction and are never
> asked, and Safeguard items are still never scored into any Dimension mean.

Three mechanics keep the Safeguard item neutral:

1. **Ask twice, subtract.** Current and Future are both plain descriptions. The difference
   between them is the lever. Nobody is ever asked what would move them.
2. ~~**The principle answer comes first**, not last. Trailing a list of six alternatives with
   *"Nothing — I'd read it myself"* makes it the odd one out, and people avoid being the odd
   one out in a survey their team reads. First position makes it a normal answer.~~
   **Retired in v2** — the symmetric list makes reading an ordinary option, so it needs no
   special slot. See the banner above.
3. **The list is not ordered as a ramp.** An escalation from weakest to strongest safeguard
   is a ladder, and a ladder implies a direction to climb.

**Ticking the same boxes in both sections is a valid answer**, not a failure. It says the
line doesn't move.

## The item

One multi-select list, asked **four times in v2** (three in v1 — the team asking moved into the
[Team section](team-section.md)). It is a **Respondent-level** attribute — it belongs to no
single Dimension, because the same safeguards answer Trust ("is the output right?") and Autonomy
("how long is the leash?") simultaneously. Read it against both.

**v2 — the four askings, live text.** Same list every time; the stems read as four different
questions.

| # | Section | Question text |
|---|---|---|
| 1 | Current-state | For AI-written output, which of these count, for you, as enough **today**? |
| 2 | Direction | For AI-written output, which of these **would you be willing** to count as enough? |
| 3 | Direction, immediately after | Which of these would you **want to know more about**? |
| 4 | Team, under *Verification* | For AI-written output, which of these should count, **for this team**, as enough? |

**The same eight options every time**, interleaved so the three reading positions land at 2, 4
and 6 and neither reading nor checks form a bloc:

- The test suite passes
- A person reads all of it
- It's easy to roll back if it's wrong
- Another person reviews it
- A type check or schema validation covers it
- A person reads the risky parts
- The blast radius is small (docs, internal tooling, non-production)
- An automated security or lint scan covers it

<details>
<summary><strong>v1's askings and seven-option list — superseded, kept as the record</strong></summary>

| # | When | Question text |
|---|---|---|
| 1 | Current section | Which of these, if any, do you accept today instead of reading AI's output yourself? |
| 2 | Future section | In six months, which of these would you accept instead of reading AI's output yourself? |
| 3 | Future section | In six months, which of these should the team accept as enough, without an individual reading the output? |
| 4 | Future section, immediately after | Which of these would you want to know more about? |

Same seven options every time:

- **I'd read it myself — nothing on this list changes that**
- Another person reviews it
- The test suite passes
- It's easy to roll back if it's wrong
- A type check or schema validation covers it
- The blast radius is small (docs, internal tooling, non-production)
- An automated security or lint scan covers it

One escape and six alternatives: the count itself said which side was normal. That is the lean
[#24](https://github.com/AndrewGodlewsky/AI-Dev-Survey/issues/24) removed by splitting *read it
myself* into two real reading positions and dropping the special first slot.

</details>

Three of these — schema validation, reversibility, blast radius — are there because a
developer may not know they can stand in for their own reading. That is the gap this item
exists to find.

**Forms mechanics, unverified.** Microsoft Forms' Likert grid appears to be single-select
per row, so a multi-select cannot be a two-row grid and items 1–3 are three separate
checkbox questions. [#10](https://github.com/AndrewGodlewsky/AI-Dev-Survey/issues/10)
confirms this. If it's wrong, this gets cheaper, not more expensive.

## Reading it

| Signal | How it's read |
|---|---|
| **Lever** | Ticked in item 2, not in item 1. What would move this person — derived, never asked. |
| **Principle hold** | *"I'd read it myself"* in item 2. The line does not move; a real constraint on the six-month plan. |
| **Team norm** | Item 3 across all Respondents. Where they agree, that is a draft six-month norm the team can write down. |
| **Learning interest** | Ticked in item 4 but not item 2. Self-reported, actionable, and free of any admission of ignorance. |
| **Inconsistent** | *"I'd read it myself"* ticked **alongside** another safeguard. |

**Inconsistent responses are flagged, never resolved by rule.** Both readings are plausible
and guessing wrong invents or erases exactly the distinction this item exists to make. With
5–9 named Respondents you can go and ask — so the response is marked inconsistent, excluded
from the lever calculation, and raised for a conversation. No silent tiebreak in a formula.

Safeguard items are **never scored** into any Dimension mean, current or future — the same
rule as Probe items ([#8](https://github.com/AndrewGodlewsky/AI-Dev-Survey/issues/8)).

## What this hands downstream

- **[#5](https://github.com/AndrewGodlewsky/AI-Dev-Survey/issues/5) / [#6](https://github.com/AndrewGodlewsky/AI-Dev-Survey/issues/6) item banks** — items 1 and 2–4 respectively. Wording above is a draft; the rules are the decision.
- **[#9](https://github.com/AndrewGodlewsky/AI-Dev-Survey/issues/9) Scoring rules** — Safeguard items are excluded from every Dimension mean. Lever and inconsistency are computed, not scored.
- **[#10](https://github.com/AndrewGodlewsky/AI-Dev-Survey/issues/10) Forms export** — confirm the multi-select assumption above, and how a checkbox question's selections come back in the export.
- **[#12](https://github.com/AndrewGodlewsky/AI-Dev-Survey/issues/12) Scored CSV** — a **per-Respondent** attribute slot (not per-Dimension), carrying accepted safeguards, levers, learning interest and the inconsistency flag. Shares the column family with Edge markers.
- **[#16](https://github.com/AndrewGodlewsky/AI-Dev-Survey/issues/16) Dashboard** — safeguards read against both Trust and Autonomy; the team-norm view across Respondents is the actionable one.
- **[#17](https://github.com/AndrewGodlewsky/AI-Dev-Survey/issues/17) How to read the results** — a Lever is what someone *would* accept, not a promise; a principle hold is a position, not an obstacle.
