# The Team section

**Decided** — wayfinder ticket [#23](https://github.com/AndrewGodlewsky/AI-Dev-Survey/issues/23).
Grilling record: [`docs/grilling/issue-23-team-section.md`](../docs/grilling/issue-23-team-section.md).
Governed by the [Framing rule](item-framing-rule.md).

The **Team section** replaces v1's mirrored team block — the seven personal Dimensions re-asked
as *"the team should…"*, which the pilot called *"re-answering all the questions just in a
slightly different frame of mind."* It asks **different questions at the team level**, once,
in team voice, and scores them on **five new Team Dimensions**.

Purpose, in the author's words: *"how, as an individual, they want to work with other
individuals who are using AI … as a group, what are acceptable and unacceptable patterns and
principles for us as a team."*

---

## The rules

1. **Single pass, team voice.** Every item is a norm — *"On this team…"* / *"the team
   should…"*. There is no now/future pair and no personal row. *"It's not about what you want
   others to do. It's about what we should require."*
2. **The Agreement scale**, five points, one scale for the whole section:
   *Strongly disagree · Disagree · Neither agree nor disagree · Agree · Strongly agree* → 1–5.
   Both end labels are equally sayable (the Framing rule's scale check).
3. **Scored.** Each Respondent gets a **Norm score** per Team Dimension — the norm they would
   set — computed exactly as any Dimension: the mean of its facets, each facet the mean of its
   items, reverse-keyed items flipped first. The Team score on a Team Dimension is the
   aggregate plus spread; **spread is the finding**.
4. **Three items per facet** — 8 facets × 3 = **24 scored items**. At least one
   **Reverse-keyed item per Team Dimension**, so the Pattern flag's flat-block check works on
   this block too.
5. **No Probe items and no Edge markers** in this section. On a named, scored Team Dimension a
   *Strongly agree* on the highest-pole item is already the visible sentence somebody owns. A
   probe can be added as one row later if results show the team wants a named edge.
6. **The Safeguard checklist is re-homed here**, once, under *Verification*:
   *"For AI-written output, which of these should count, for this team, as enough?"* — the
   **symmetric eight-option list** shared by all four askings, in the same interleaved order,
   **never scored**. It is a standalone team norm, not the cut third pass of the personal item.

   > **Corrected three ways by the item banks' joint resolution, 2026-08-30**
   > ([#31](https://github.com/AndrewGodlewsky/AI-Dev-Survey/issues/31) Q4;
   > [`issue-31-32-item-banks-resolution.md`](../docs/grilling/issue-31-32-item-banks-resolution.md)).
   > This rule was written before [#24](https://github.com/AndrewGodlewsky/AI-Dev-Survey/issues/24)
   > landed and said *seven* options, *principle answer first*, and the stem *"…as enough,
   > **without an individual reading the output**?"*. All three are superseded: #24 replaced the
   > leaning seven with the symmetric eight; with a symmetric list reading is an option like any
   > other rather than a special first slot; and the old stem excluded reading from a question
   > whose list now offers three ways of reading. All four askings must be identical or the team
   > norm is not comparable with the personal ones. The list lives in
   > [`direction-section.md`](direction-section.md), the wording in [`team-items.md`](team-items.md).

7. **The Framing rule applies in full**, and this is the **only** block where a **Value item** —
   a principle stated flat as a proposed norm — is legal. **Two forms are usable here: Direction
   items and Value items**, plus the one Checklist. The balance floor is met by the low-pole
   items on *Agent latitude* and *Pace*.

   > **Narrowed by the item banks' joint resolution, 2026-08-30**
   > ([#31](https://github.com/AndrewGodlewsky/AI-Dev-Survey/issues/31) Q1). This rule originally
   > read *"All five forms are legal here."* They remain legal under the
   > [Framing rule](item-framing-rule.md) — but the **Agreement scale removes two of them in
   > practice**. A **Scenario item** is a present-tense world answered on the *Desirability*
   > scale (*would you want to work this way*); put the same sentence on an Agreement scale and
   > agreeing means *this is already how things are* — a current-state question, which breaks
   > rule 1's single-norm pass. **Probe items** are excluded outright by rule 5. Nothing in the
   > bank moved either way: this states what the scale already forced, so a future drafter does
   > not reach for a form this block cannot carry.

## The five Team Dimensions

Each is a **bundle**: its facets are the eight topics the section covers. Both poles are
positions a team can hold; the direction is a direction, not the good direction — 5 on
*Verification* and 5 on *Agent latitude* pull opposite ways on purpose.

| Team Dimension | Facets | 1 — low pole | 5 — high pole | Direction reads as |
|---|---|---|---|---|
| **Transparency** | Disclosure & provenance · Ownership & accountability | AI's role in the work is invisible; ownership of AI-written code is diffuse or by the system | Every AI contribution is labelled and personally owned by whoever merges it | more required visibility and personal ownership |
| **Verification** | Reviewing AI-assisted work *(+ the Safeguard checklist, unscored)* | Automated checks are enough; nobody has to read AI output | A human reads every line of AI output, with the same review as human work or more | more required human review |
| **Agent latitude** | Parallel development with agents · Limits | Agents work only in personal sandboxes and broad areas are written off-limits | Agents act on shared code anywhere, including against `main`, with no no-go zones | more freedom for agents in the shared codebase |
| **Pace** | Pace & risk appetite | The team moves at the pace of its most cautious member and waits for evidence | The team moves at the pace of its keenest member and tries things first | faster adoption as a team |
| **Shared practice** | Shared conventions & tooling · Learning & skill | Everyone picks their own tools and instructions; skill without AI is each person's own business | One shared, maintained setup; the team deliberately keeps everyone able to work without AI | more investment in shared capability |

> **Agent latitude nets two facets that run opposite ways**, and the **facet view is its primary
> read** — decided in the item banks' joint resolution, 2026-08-30
> ([#31](https://github.com/AndrewGodlewsky/AI-Dev-Survey/issues/31) Q2). *Parallel development
> with agents* runs with the Dimension (more of it, more latitude); *Limits* runs against it
> (more of it, less latitude), which is why three of that Dimension's six items are
> reverse-keyed. A **flat 3 is therefore ambiguous by construction** — it cannot be told apart
> from *"agents everywhere in the day-to-day code, and absolutely nowhere near production
> data"*, which is a coherent and common position. Concern is the precedent: five risks under
> one mean, read separately as well as as a mean. Splitting this into two Team Dimensions was
> considered and rejected as the more expensive fix; it stays revisitable after the pilot.

### What each facet covers

| Facet | Covers |
|---|---|
| **Disclosure & provenance** | Whether and how people tell each other what AI wrote — PR descriptions, commit trailers, "an agent did this part". |
| **Ownership & accountability** | Who owns AI-written code once merged; "explain every line under your name" at team level. |
| **Reviewing AI-assisted work** | How a reviewer treats an AI-heavy PR; what the author owes the reviewer; reviewer load. |
| **Parallel development with agents** | Several people running agents in one codebase — conflicts, churn, branch hygiene, agents touching shared code. |
| **Limits** | Work AI must not touch as a matter of team policy — secrets, production data, named areas. |
| **Pace & risk appetite** | How fast the team adopts; who decides; whether the cautious or the keen set the pace. |
| **Shared conventions & tooling** | Shared instruction files in the repo, agreed tools, who maintains them. |
| **Learning & skill** | Keeping the team's skills sharp, pairing, teaching each other tools; skill atrophy as a *team* risk. |

## Shape

| | |
|---|---|
| Scored items | 24 (8 facets × 3), one Likert block per Team Dimension or one for the section — the assembly ticket decides |
| Checklist | 1 (Safeguard, under Verification) |
| Answers per Respondent | 25 — against ~49 in v1's team block |
| Scale | Agreement, 1–5 |
| Passes | 1 |

## Reading it

| Signal | How it's read |
|---|---|
| **Norm score** (per Respondent, per Team Dimension) | The norm this person would set. Shown by initials, like everything else. |
| **Team score** (per Team Dimension) | Mean **and spread**. A tight cluster is a norm the team already holds; a wide spread is the conversation to have. |
| **Facet view** | The same, per facet — where a Dimension's spread comes from. |
| **Safeguard team norm** | Options at least half the team ticks are a draft norm the team can write down. |
| **Pattern flag** | A flat team block (same answer down it, reverse-keyed items included) is flagged, never scored out. |

## What dies with this

- The mirrored team block, the **Stance gap** and the **norm gap** — the `Future-Team − Future-Personal` quantity no longer exists.
- The **team Coverage pass** (v1 section 10) and the **team Safeguard pass** *as a pass* — the checklist survives as an item, above.
- *Future score* no longer applies to anything team-level; the team block's per-Respondent value is the Norm score.

## What this hands downstream

- **Team Dimension rubric levels** *(new ticket)* — 1–5 level text for each of the five, written in team voice between the poles above, in `rubric/RUBRIC.md`'s format.
- **Team item bank** *(new ticket)* — 24 items + the checklist, drafted to the Framing rule: 3 per facet, ≥1 reverse-keyed per Dimension, all in team voice on the Agreement scale.
- **[#28](https://github.com/AndrewGodlewsky/AI-Dev-Survey/issues/28) Scoring rules v2** — Norm score = mean of facets, facets averaged first; reverse-keys; Pattern flag on the block; the Safeguard checklist's team norm read; nothing here is a Gap.
- **[#26](https://github.com/AndrewGodlewsky/AI-Dev-Survey/issues/26) Local app** — a team panel: five Team Dimensions, mean + spread + per-person by initials, with a facet drill-down.
- **[#29](https://github.com/AndrewGodlewsky/AI-Dev-Survey/issues/29) Assemble the v2 survey document** — one section, one scale, 25 answers; every statement unique.
- **How to read the results** — spread on a Team Dimension is the headline, not the mean; a Norm score is a position someone holds, not a rating of the team.
