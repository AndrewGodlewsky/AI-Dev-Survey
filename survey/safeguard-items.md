# Safeguard items and Levers

**DRAFT for reaction** — wayfinder ticket [#19](https://github.com/AndrewGodlewsky/AI-Dev-Survey/issues/19).
Grilling record: [`docs/grilling/issue-19-conditional-items.md`](../docs/grilling/issue-19-conditional-items.md).

A **Safeguard item** asks which checks a Respondent accepts **in place of reading AI's
output themselves**. It is a plain description of a position — not a hypothetical, not a
condition, and never a question about what would change their mind.

A **Lever** is a safeguard someone accepts in six months but not today. Levers are
**derived by subtraction**, never asked. That is the whole design: the survey gets the
conditional answer without ever putting a conditional question in front of anyone.

> The ticket that produced this was called *"Conditional items"*. Nothing conditional
> survived the design, so the name did not either.

---

## The non-leading rule

The survey must not push anyone toward a position. *"What would have to be true for you to
accept AI doing X?"* presupposes that accepting X is a destination and invites the
Respondent to negotiate themselves toward yes — someone whose honest answer is *"nothing,
and I don't want there to be"* has to argue with the question before they can answer it.

Three mechanics keep the Safeguard item neutral:

1. **Ask twice, subtract.** Current and Future are both plain descriptions. The difference
   between them is the lever. Nobody is ever asked what would move them.
2. **The principle answer comes first**, not last. Trailing a list of six alternatives with
   *"Nothing — I'd read it myself"* makes it the odd one out, and people avoid being the odd
   one out in a survey their team reads. First position makes it a normal answer.
3. **The list is not ordered as a ramp.** An escalation from weakest to strongest safeguard
   is a ladder, and a ladder implies a direction to climb.

**Ticking the same boxes in both sections is a valid answer**, not a failure. It says the
line doesn't move.

## The item

One multi-select list, asked three times. It is a **Respondent-level** attribute — it
belongs to no single Dimension, because the same six safeguards answer Trust ("is the
output right?") and Autonomy ("how long is the leash?") simultaneously. Read it against
both.

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
