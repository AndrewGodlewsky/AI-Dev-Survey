# The Framing rule

**Binding for v2** — wayfinder ticket [#22](https://github.com/AndrewGodlewsky/AI-Dev-Survey/issues/22).
Grilling record: [`docs/grilling/issue-22-item-framing-rule.md`](../docs/grilling/issue-22-item-framing-rule.md).
Decision record: [ADR-0001](../docs/adr/0001-item-framing-rule.md).

This replaces v1's **non-leading rule** (a ban on one sentence shape — *"never ask what would
have to be true for you to accept X"*). It is not re-litigated per item: a draft is one of the
forms below and passes the test below, or it is not an item. Adding a form or changing a check
means reopening [#22](https://github.com/AndrewGodlewsky/AI-Dev-Survey/issues/22), not arguing
a draft.

---

## The rule

> **No implied destination.** Nothing the Respondent reads may contain or presuppose a
> position they are supposed to be moving toward — in either direction, pro-AI or pro-craft.

The survey **locates**; it never **points**. On a named survey read by the whole team, an item
that tells someone where the finish line is produces a guarded answer you cannot tell from an
honest one, and the instrument is broken either way it leans.

Three things follow directly and are part of the rule, not commentary on it:

1. **Symmetric.** An item that nudges toward caution is as illegal as one that nudges toward
   adoption. A survey led toward caution reports a team more cautious than it is — the same
   broken instrument pointed the other way.
2. **Everything the Respondent reads.** Form description, section intros, headings, subtitles,
   scale labels, option lists, level definitions — not only item text. A neutral item under the
   heading *"Where we're growing"* is a led item.
3. **Not concrete ≠ illegal, but abstract is only legal in one block.** See *Where it applies*.

## Where it applies

| Block | What the rule permits | Note |
|---|---|---|
| **Current-state section** (me, today) | Frozen — 26 items and the 19-row Coverage grid stand verbatim. | Only the surrounding copy is checked (point 2 above). |
| **Forward personal block** (me, six months as a direction) | **Concrete only**: Scenario, Direction, Probe and Checklist items. **No Value items.** | Personal values are read *off* reactions to concrete situations, never asked flat. *"Understand each person's core values and principles without directly asking them for it."* |
| **Team section** | **All five forms**, including Value items stated flat as proposed team norms. | A team-level value is a norm being proposed, not a self-report, so it does not collapse into its Current-state twin. |

## The forms — a closed catalogue

| Form | What it is | Legal | Illegal twin — and why |
|---|---|---|---|
| **Scenario item** | A concrete way of working, stated in the **present tense** as if it were already how things are, answered on the Desirability scale. It says nothing about whether that world is coming or good. | *"AI writes the first draft of every PR on this team."* | *"AI is ready to write the first draft of every PR — how far would you let it go?"* — *ready* and *how far* both place a destination. |
| **Direction item** | A concrete practice, asked as **want** (personal: *"I want to…"*) or **should** (team: *"the team should…"*). The practice is named; the scale carries the direction. | *"The team should run agents unsupervised on migrations, with rollback as the only gate."* | *"In what ways do you want to be able to develop with AI?"* — open, not concrete; asks the Respondent to narrate a direction. |
| **Value item** *(team section only)* | A principle stated flat, as a proposed team norm. Abstract by nature — the one place abstraction is legal. | *"Every line that ships should be understood by someone on the team."* | *"How important is it that we don't lose the ability to understand our own code?"* — presupposes the loss is coming. |
| **Probe item** | A Scenario item at a **pole**: extreme, concrete, **never scored**, raising an Edge marker at 4–5. Rules 1–7 in [`probe-items.md`](probe-items.md) stand unchanged. | *"…merge AI-written code I had not read line by line, as long as the tests pass."* | *"…would you eventually merge AI code unread?"* — *eventually* is a ramp. |
| **Checklist item** | A multi-select plain description of a position. The Safeguard item is the only one today. | *"Which of these do you accept in place of reading the output yourself?"* | *"Which of these would it take for you to stop reading the output?"* — a threshold. |

Every form is answered on gut reaction. An item that needs thinking through has failed before
the test starts.

## Banned outright

All consequences of *no implied destination*:

- **Threshold items** — *"what would AI have to do / prove before you'd…"*, *"what would have to be true for you to…"*. This is the archetype the v1 rule banned, and it stays banned.
- **Ramp vocabulary** — *yet, still, ready, eventually, further, more than today, go as far as, beyond what I do now*, and any comparative against the Respondent's present position.
- **Open direction questions** — *"in what ways…"*, *"how would you like to…"*. They ask for prose a survey with no free text cannot score, and they re-run the pilot's finding: someone who cannot forecast their own state cannot narrate their own direction on demand either.
- **Option lists ordered as a ramp** — an escalation from weakest to strongest is a ladder, and a ladder implies a direction to climb.
- **Scale labels that point** — a scale whose end labels carry a judgement (*Reluctant … Confident*, *Skeptic … Early adopter*).
- **Any item whose honest answer *"no, and I don't want that"* has to argue with the sentence before it can be given.**

## The test

Every draft item runs these **in order** and stops at the first failure. A failed item is
**rewritten or dropped — never argued**. The drafter runs it; the item bank states once that
every item in it passed, and a failed draft never appears there. The drafter shows its
working (the flip) only for items it was unsure about, in the ticket's grilling record, so the
judgement calls are visible and nothing else is.

1. **Form** — it is one of the five forms, and that form is legal in its block.
2. **The flip** — write the opposite position. *"AI writes the first draft of every PR"* ↔ *"No PR here starts from an AI draft."* If the opposite reads as a normal thing to want, the item is symmetric. If the opposite reads like a confession or a refusal, the original was pointing.
3. **The refusal** — someone whose honest answer is *"no, and I don't want that"* can give it by picking the bottom of the scale, without contradicting anything in the sentence.
4. **The vocabulary** — none of the ramp words, no *would have to*, no comparative against today.
5. **Concrete** *(where the block requires it)* — names an action, artifact or situation drawn from work this team actually does.

Checks 2 and 3 have the teeth; 1, 4 and 5 are the cheap screens that catch most failures first.

## Scales are instruments, not options

The ramp ban applies to **unordered choice lists** presented as an escalation, and to copy
that names one end of a scale as the good end. A numbered ordinal scale whose ends are both
stated neutrally is a **measurement**, and measurements are allowed — the Involvement level
scale (1 *None* → 6 *System-verified*) and every Likert scale pass. The check for a scale is:
**both end labels must be equally sayable.** *None* and *System-verified* are. *Reluctant* and
*Confident* are not.

## Option lists

Three mechanics, originally written for the Safeguard item, now general for every Checklist
item and option list in the survey:

1. **The principle answer comes first**, not last. Trailing six alternatives with *"Nothing — I'd read it myself"* makes it the odd one out, and people avoid being the odd one out in a survey their team reads.
2. **The list is not ordered as a ramp.**
3. **Ticking the same boxes in two askings is a valid answer.** It says the line doesn't move.

## The bank

The rule binds the **bank**, not only the item. Every item can pass the test individually while
the section as a whole still leans: twelve scenarios that all describe more AI than today say
where things are going, and no single item is at fault.

**Balance floor:** every block of Scenario or Direction items contains **at least one** item
describing *less* AI than today, or the status quo held deliberately. A floor, not a ratio —
it is the direction-analogue of v1's *"at least one Reverse-keyed item per Dimension"*, which
exists for the same reason. A strawman less-AI item is itself a pointer; the flip catches it.

## What survives from v1, and why

- **Probe items** survive as a form because they already satisfy the rule — an extreme concrete world, answered on the same scale as its neighbours, whose flip is a normal thing to want. Their **count, placement and tense** are decided by the block tickets; the five in `probe-items.md` are worded for a *prediction* block and need re-tensing to present-tense scenarios.
- **Levers stay derived by subtraction, never asked.** The direct question is a Threshold item. Whether the future-personal Safeguard asking survives is [#24](https://github.com/AndrewGodlewsky/AI-Dev-Survey/issues/24)'s decision; if it does not, Levers go with it — they cannot be replaced by a question.
- **The three option-list mechanics** survive because they follow from the rule, not out of loyalty to the old one.

## What this hands downstream

- **[#24](https://github.com/AndrewGodlewsky/AI-Dev-Survey/issues/24) Forward personal block** — Scenario and Direction items only, present tense, balance floor per block; re-tense the probes; decide whether the future-personal Safeguard asking (and so Levers) survives. Purpose, in the author's words: *"how the person, as an individual developer, thinks AI can help them, or how they want to integrate with AI … the principles of what they'd be willing to accept and what they're interested in doing, by asking them questions that will reveal those types of answers."*
- **[#23](https://github.com/AndrewGodlewsky/AI-Dev-Survey/issues/23) Team section** — all five forms; Value items legal here and nowhere else. Purpose, same source: *"how, as an individual, they want to work with other individuals who are using AI … as a group, what are acceptable and unacceptable patterns and principles for us as a team."*
- **[#25](https://github.com/AndrewGodlewsky/AI-Dev-Survey/issues/25) Coverage grid** — the frozen "today" pass is untouched; anything replacing the six-month pass is checked as a scale (*both ends equally sayable*), not as an option list.
- **Assembling the v2 survey document** — every piece of section copy in `SURVEY.md` is checked against point 2 of the rule; the current intro (*"where we would each like to be … six months from now"*, *"asks each thing twice"*) is stale on other grounds and is rewritten anyway.
- **Rubric v2** — nothing to score changes here; the Edge marker and Lever definitions stand where their items survive.
