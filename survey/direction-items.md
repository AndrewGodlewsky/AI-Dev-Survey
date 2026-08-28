# Direction item bank

**DRAFT for reaction** — wayfinder ticket [#32](https://github.com/AndrewGodlewsky/AI-Dev-Survey/issues/32).
Grilling record: [`docs/grilling/issue-32-direction-item-bank.md`](../docs/grilling/issue-32-direction-item-bank.md).

The items for the **Direction section**, specified by
[`direction-section.md`](direction-section.md) ([#24](https://github.com/AndrewGodlewsky/AI-Dev-Survey/issues/24))
and governed by the [Framing rule](item-framing-rule.md)
([#22](https://github.com/AndrewGodlewsky/AI-Dev-Survey/issues/22)). Facets are the frozen
[`current-state-items.md`](current-state-items.md).

**20 scored items + 5 probes + 2 Safeguard askings = 27 answers.**

> **Every item in this bank ran the Framing rule's five-check test and passed.** A failed draft
> was rewritten or dropped and does not appear here. The working — the flip — is shown only for
> the items the drafter was unsure about, in the grilling record linked above.

---

## The scale

One block, one scale, **one row** — Stance is dead, so nothing is asked twice.

| | 1 | 2 | 3 | 4 | 5 |
|---|---|---|---|---|---|
| **Desirability** | Definitely not | Probably not | Unsure | Probably | Definitely |

Both ends are equally sayable, so the scale passes as an instrument rather than a pointer.

**R** = reverse-keyed, scored `6 − answer`. **Form** = `S` Scenario · `D` Direction. No Value
items: this block is concrete-only.

Items are written as **whole present-tense sentences**, not stems. v1's `[Me]` / `[Team]`
prefix hack is gone with the second row — each statement is already unique on its own text,
which is all the Forms export needs.

## The section description

Draft. Checked against the Framing rule's point 2 (*everything the Respondent reads*).

> ### Direction
>
> This section describes concrete ways of working. Each one is written as if it were already
> how things are.
>
> For each, answer one question: **if this were true, how would you feel about working this
> way?**
>
> None of these is a prediction and none is a recommendation. Some describe a great deal of AI
> in the work, some describe very little, and both are real answers. There is no right column.
>
> We use the answers to plan the next six months.

The horizon is named **once**, here, and appears in no item.

---

## Comfort — willingness to use AI in my own development work

| ID | Form | R | Twin | Item |
|---|---|---|---|---|
| D-C1 | S | | C1 + C2 | AI is involved in most of the code I write, including the code that ships to production. |
| D-C2 | S | **R** | C3 | I work without AI for stretches at a time, by choice. |

Two slots and a mandatory reverse-key mean the forward item carries both of C1's frequency and
C2's stakes. **D-C2 is deliberately not C3's sentence** (*"I'd rather work through something
myself…"*), which is a stated preference; D-C2 is a described working pattern, and preference
is what the scale is already asking for.

## Trust — confidence that AI output is correct without line-by-line scrutiny

| ID | Form | R | Twin | Item |
|---|---|---|---|---|
| D-T1 | S | | T1 | AI's answers go straight into my work; I look closely only when something seems off. |
| D-T2 | S | **R** | T2 | I check AI's work against the source — the docs, the code, the data — before I act on it. |

**D-T2 is deliberately off the line-by-line ground.** The Trust probe (P2) already occupies
*"code I have not read line by line, as long as the tests pass"*, and in a single 25-row block
a scored item and an unscored probe on the same sentence waste one of the two Trust slots — the
mistake [#6](https://github.com/AndrewGodlewsky/AI-Dev-Survey/issues/6) caught between FG3 and
the Concern probe. Source-checking is the same facet (verification before acting) on different
words. **Q1 in the grilling record.**

## Fluency — practical skill with AI tools

Direction form throughout: the facet is the Respondent's own skill, and a world-sentence about
someone's competence comes out contrived.

| ID | Form | R | Twin | Item |
|---|---|---|---|---|
| D-F1 | D | | F2 | I want to point AI at the right files and examples before I ask it anything. |
| D-F2 | D | **R** | F3 → FF3 | I want to use AI tools as they come, without configuring or tuning them. |

**F3 does not mirror.** *"When an AI tool doesn't give me what I need, I'm not sure what to
change"* floors out on a Desirability scale — nobody answers *Definitely* to wanting to stay
confused, so the reverse-key would hand Fluency a constant. v1 found this and replaced it with
FF3; that replacement carries into D-F2 unchanged in substance. The two items sit on adjacent
axes — per-task context against tool setup — which is a real overlap. **Q2.**

## Guardrails — how much review, disclosure, testing and policy I want

Five items, one per facet, matching the Current bank's **five** facets with G2 and G3 collapsed
into one disclosure value. One fewer and the Gap subtracts two different things.

| ID | Form | R | Facet | Twin | Item |
|---|---|---|---|---|---|
| D-G1 | S | | Review + testing | G1 | Anything AI helped write goes through an extra pair of eyes and an extra test before it ships. |
| D-G2 | D | | Disclosure | G2 + G3 | I want the commit or PR to say when AI wrote most of it. |
| D-G3 | S | | Off-limits areas | G4 | There are parts of my work I keep AI out of, deliberately. |
| D-G4 | S | | Enforcement strength | G5 | Our AI rules live in the tooling — lint, CI, hooks — not in people's heads. |
| D-G5 | S | **R** | The "nothing extra" pole | G6 | AI-assisted work moves through the same pipeline as everything else, with nothing added for it. |

**D-G4 carries both poles inside the sentence** — *in the tooling* against *in people's heads* —
so it describes a position rather than pushing toward one, the same trick G5 uses.

**D-G4 and D-G5 are collectively voiced** where the rest of the section is personal. Enforcement
and pipeline are properties of a shared environment; their Current twins (G5, G6) are voiced the
same way. They are Scenario items about a world, not *"the team should"* Direction items, so
they do not trespass on the Team section. **Q5.**

**D-G1 and D-G5 are near-inverses**, inherited from G1/G6 — a known v1 shape the pilot ticket
already flagged to watch. It cannot be fixed by dropping one: both are named facets the Gap
needs. **Q4.**

## Concern — perceived risk from AI-assisted development

Five items, one per named risk. Worded as **the vigilance in force**, never as a feeling —
nobody sets a target for how worried they want to be, and a Desirability scale asked against a
feeling produces nothing.

| ID | Form | R | Risk | Twin | Item |
|---|---|---|---|---|---|
| D-N1 | D | | Skill atrophy | N1 | I want to keep doing enough work without AI to keep my own skills sharp. |
| D-N2 | S | | Security | N2 | Anything AI wrote for me gets a security look before it ships. |
| D-N3 | S | | IP / licensing | N3 | I check AI-generated code for licensing and IP exposure before it goes in. |
| D-N4 | S | **R** | Maintainability | N4 | AI-written code goes into my codebase on the same terms as anything else — I give its maintainability no extra thought. |
| D-N5 | D | | Job impact | N5 | I want to plan around AI changing what my job is. |

**D-N5 is facet-matched, not word-matched.** N5 is an expectation (*"I expect AI to change what
my job is within a few years"*); a Desirability scale cannot ask whether you want an expectation,
so the forward item asks about planning instead. That Gap is softer than the other four and the
one-pager should say so — the same caveat v1 attached to FF3 and FV2.

**D-N2 sits beside D-G1** (extra review and testing). They are distinguishable — a named security
gate against general added rigour — but they are neighbours. Noted, kept.

## Autonomy — how unsupervised AI may act on my behalf

| ID | Form | R | Twin | Item |
|---|---|---|---|---|
| D-A1 | S | | A1 | Agents change files and run commands across my project, not just in the file I have open. |
| D-A2 | S | **R** | A2 | AI suggests and explains; I make the actual edits myself. |

Two anchors on one axis — how far AI's hand reaches — which leaves the Autonomy probe (P3) its
own ground in *duration* (*"unsupervised for an hour"*). **D-A2 changes facet**: A2 is
step-approval (*"approve an agent's steps as it goes"*), D-A2 is the Advisor position. Same
Dimension, different point on it, so Autonomy's Gap is softer than a word-matched pair. **Q3.**

## Craft values — weight placed on general development principles

*Not AI-specific; a lens for reading the other Dimensions.* Direction form: the facet is the
Respondent's own values.

| ID | Form | R | Twin | Item |
|---|---|---|---|---|
| D-V1 | D | | V1 | I want to leave code the next person can work on without asking me. |
| D-V2 | D | **R** | V2 → FV2 | I want to ship when it works, rather than spend more time on tests and tidying. |

**D-V1 stays clear of the Craft probe.** P5 is *"explain every line of code that ships under my
name"* — personal explainability. D-V1 is handover to someone else. V1 was worded to leave this
room and it still does.

**V2 does not mirror, and v1's replacement is now illegal.** *"When a deadline is tight, tests
and review are the first things I drop"* is a confession nobody signs on a named survey. v1
replaced it with FV2, *"…let speed win over polish **more often than it does today**"* — a
**comparative against the Respondent's present position**, banned outright by the Framing rule's
ramp vocabulary. D-V2 states the position with no reference to today.

---

## The five Probe items

Re-tensed from `probe-items.md`'s forecasts to **present-tense worlds**. Rules 1–7 otherwise
unchanged: never scored, never reverse-keyed, one pole each, direction-normalised so
**"Definitely" is always the edge**, indistinguishable from their neighbours in the block. An
**Edge marker** fires at 4–5 — **one per Respondent per probe**, no stance split.

| ID | Dimension | Pole | Item |
|---|---|---|---|
| P1 | Comfort | low | I work with no AI tooling at all, the way I worked before it existed. |
| P2 | Trust | high | I merge AI-written code I have not read line by line, as long as the tests pass. |
| P3 | Autonomy | high | I let an agent work unsupervised for an hour and only look at the final result. |
| P4 | Concern | high | I hold back on AI, because the risks outweigh what I'd gain. |
| P5 | Craft values | high | I expect to be able to explain every line of code that ships under my name. |

> **P4 is amended again.** `probe-items.md` reads *"…**slow down** how fast I adopt AI"* — a
> comparative against the Respondent's present pace, which is exactly what the Framing rule's
> ramp ban forbids. *Hold back* states the position without measuring it against today. The
> rules on that page are untouched: still five probes, one pole each, Concern still high.
> **Q7** — this amends a closed ticket's wording for the second time.

P1's flip is the whole reason it is the one low-pole probe: refusing AI outright is rare enough
to be worth locating, and common enough to be a real constraint.

## The Safeguard askings

Two live in this section; the third is today's, in the Current-state section. All three share
one list, because Levers and Holds are subtractions and a subtraction needs identical sides.

| # | Section | Stem |
|---|---|---|
| 1 | Current-state | For AI-written output, which of these count, for you, as enough **today**? |
| 2 | Direction | For AI-written output, which of these **would you be willing** to count as enough? |
| 3 | Direction, immediately after | Which of these would you **want to know more about**? |

Asking 1's stem is drafted here because all three share the list and the three stems have to
read as three different questions. It **replaces** the Current-state section's existing Safeguard
item 1 — *"Which of these, if any, do you accept today instead of reading AI's output yourself?"*
— whose *instead of reading it yourself* framing is the lean [#24](https://github.com/AndrewGodlewsky/AI-Dev-Survey/issues/24)
removed. Safeguard item 1 is **not** one of the 26 frozen scored items, but it does sit in that
section. **Q6.**

### The list — same eight options, all three askings

- The test suite passes
- A person reads all of it
- It's easy to roll back if it's wrong
- Another person reviews it
- A type check or schema validation covers it
- A person reads the risky parts
- The blast radius is small (docs, internal tooling, non-production)
- An automated security or lint scan covers it

**The order is interleaved on purpose.** The spec lists the three reading positions first and
the five checks after, which reads as an escalation from human to automated — a ramp, banned by
option-list mechanic 2. Interleaving puts the reading positions at 2, 4 and 6 so neither group is
a bloc and neither leads. With a symmetric list, mechanic 1's *principle answer first* slot
stops being special: reading is an option like any other, so it does not need the front. **Q6.**

### Reading it

| Signal | How it's read |
|---|---|
| **Lever** | A check ticked in asking 2, not in asking 1. Derived, never asked. |
| **Hold** | A reading position ticked in both. The line does not move — a position, not an obstacle. |
| **Learning interest** | Ticked in asking 3, not in asking 2. |
| **Inconsistent** | *A person reads all of it* alongside **any** check, in the same asking. *Reads the risky parts* + a check is coherent and is **not** flagged. Levers and Holds are not computed for that person. |

---

## Uniqueness — checked

Forms exports statement text as the only identifier, so **every statement in the whole form must
be unique**, and no Direction item may be a Current-state item's sentence in another tense. Every
item above was checked against its twin and against the probes. Five drafts were rewritten for
being too close to their Current twin rather than for failing the test:

| Draft | Collided with | Rewritten to |
|---|---|---|
| *"I rely on AI's output about as much as I'd rely on a colleague's."* | T3, near word-identical | D-T1, moved onto T1's ground |
| *"AI-assisted changes I make get more review and testing than the ones I write by hand."* | G1, same sentence re-voiced | D-G1 |
| *"Whatever we agree about AI use is enforced by our tooling rather than left to judgement."* | G5, same sentence, different mood | D-G4 |
| *"Our normal process covers AI-assisted work; nothing extra applies to it."* | G6 | D-G5 |
| *"I want to be deliberate about the context I give an AI tool."* | F2 | D-F1 |

## The balance floor — met

Seven of the twenty describe **less AI, or the status quo held deliberately**: D-C2, D-T2, D-F2,
D-G1, D-G3, D-N1, D-A2. The floor asks for one. None is a strawman — each one's flip reads as a
normal thing to want, which is the check that catches a strawman less-AI item.

## What this does *not* settle

- **Block structure and item order.** 25 Likert rows on one scale is the largest single block in
  v2 and the straight-lining risk moves with it. Interleaving the Coverage grid's Direction pass
  and the Safeguard askings between Dimension groups is the cheapest mitigation.
  [#29](https://github.com/AndrewGodlewsky/AI-Dev-Survey/issues/29) owns it.
- **Where the probes sit.** Rule 4 requires them inside the ordinary blocks, indistinguishable
  from their neighbours — not gathered into a probe section. Placement is #29's.

## What this hands downstream

- **[#29](https://github.com/AndrewGodlewsky/AI-Dev-Survey/issues/29) Assemble** — 25 Likert rows plus 2 checkbox questions; the section description above; block structure and probe placement; **and the Current-state section's Safeguard item 1 stem and option list change**, per the table above.
- **[#28](https://github.com/AndrewGodlewsky/AI-Dev-Survey/issues/28) Scoring rules** — Direction score over the facets above: Comfort/Trust/Fluency/Autonomy/Craft **2 items** each against Current's **3**, Concern 5, Guardrails 5 with G2+G3 collapsed first. Reverse-keys: D-C2, D-T2, D-F2, D-G5, D-N4, D-A2, D-V2. **Three Gaps are facet-matched rather than word-matched and read softer than the rest — Fluency (F3→D-F2), Autonomy (A2→D-A2), Concern's job-impact facet (N5→D-N5)** — on top of #24's ruling that *every* Gap is now the softer kind.
- **[#33](https://github.com/AndrewGodlewsky/AI-Dev-Survey/issues/33) Rubric v2** — §6.2's symmetric list and its ordering are fixed here; the three stems above are the ones the Lever/Hold subtraction runs on.
- **[`probe-items.md`](probe-items.md)** — P4's wording amended a second time (ramp vocabulary); all five re-tensed to the present. Apply once **Q7** is answered.
- **[`safeguard-items.md`](safeguard-items.md)** — asking 1's stem and the option list are superseded by this file. Apply once **Q6** is answered.
- **[#26](https://github.com/AndrewGodlewsky/AI-Dev-Survey/issues/26) Local app** — the Safeguard panel needs Holds beside Levers, and the probe table loses its per-stance split.
