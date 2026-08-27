# Grilling — Issue #22: Item framing rule

**Ticket:** [Item framing rule: what replaces the non-leading rule](https://github.com/AndrewGodlewsky/AI-Dev-Survey/issues/22)
**Map:** [Map v2: Survey overhaul & local dashboard app](https://github.com/AndrewGodlewsky/AI-Dev-Survey/issues/21)
**Round:** 1 of ~2 — four questions
**How to use:** answer inline under each `### Your answer` heading. Free text is fine; you don't have to pick one of the listed options. Then tell me it's ready and I'll read it back and compute the next round.

---

## What is already settled coming in

- **The old rule is gutted, not softened.** Round 3, Q1: *"this is going to be changed in version 2, so we're going to have to gut the old stuff and replace it with a new version that is going to be the truth and can't be overturned."* So the question below is never *whether* to replace it — only what the replacement says.
- **The replacement is binding and not re-litigated per item.** Same answer. Any option that needs an argument per draft item is disqualified on that ground alone.
- **This ticket blocks every item ticket in v2.** Nothing gets drafted until it closes.

## What this round deliberately holds back

These are real questions, but each one needs an answer from below before it can be asked honestly, so they are round 2:

- The **concrete form catalogue** — what a scenario item, a preference item, a direction item actually look like on the page.
- **The test** — the pass/fail check a draft item runs through, and who runs it.
- **Probe items and Levers**, both of which exist because of the old rule.
- **Where the rule is written down** — `CONTEXT.md`, a `survey/` doc, or an ADR.

---

## Q1 — What harm does the rule name?

### What this is

v1's rule banned a **sentence shape**: *"Never ask 'what would have to be true for you to accept X'."*

A shape-ban is brittle. It is easy to write a thoroughly leading item that never once uses those words, and a shape-ban gives you no grounds to reject it. The replacement should name the **harm**, and let the specific bans fall out of it as consequences.

### Why it matters

This is the root of the whole rule. Everything in round 2 — which forms are legal, what the test checks, whether Probes survive — is derived from whichever harm you name here. Name it too narrowly and the rule has holes; too broadly and it bans items you want.

### Options

| Option | The rule says | Pros | Cons |
|---|---|---|---|
| **A. No implied destination** | An item may not contain or presuppose a position the Respondent is supposed to be moving toward. | Catches ramps, thresholds, "what would it take", and anything positioning the Respondent as short of somewhere — including phrasings that use none of v1's banned words. | Strict. Some genuinely useful items will fail it and need rewriting. |
| **B. No advocacy** | An item may not state or imply that a position is good. Asking what would change someone's mind is fair, because asking is not endorsing. | Maximum freedom; the "what would AI have to do" items can be written literally. | This is the loophole, not the rule. See below. |
| **C. No socially costly answer** | The test is exposure-shaped: no point on the scale should embarrass the person who picks it, on a survey their team reads by name. | Directly targets the validity problem — guarded answers you cannot distinguish from honest ones. | Bans items that are uncomfortable *by design*, including the Concern and Craft probes. Wrong instrument for this job. |

### My recommendation

**A.** It is the only one that survives being made binding.

**B** is exactly the loophole your own round-3 phrasing walked into. *"What AI would have to do for them to change and use it more"* advocates nothing explicitly — and still tells the reader precisely where the finish line is, and that they are currently behind it. A rule that permits that has not replaced anything.

**C** describes a real failure mode, but it is mostly a **consequence** of A plus mechanics `safeguard-items.md` already uses (the principle answer comes first; the list is not ordered as a ramp). Promoted to headline rule it would kill the Concern probe — *"…slow down how fast I adopt AI, because the risks outweigh what I'd gain"* — which is supposed to be a costly thing to say. That is the item doing its job.

### Your answer

:

---

## Q2 — Symmetric, or does it single out more-AI?

### What this is

Given a rule against implied destinations: does it forbid **any** destination, or specifically the *more-AI-is-where-you're-heading* framing that a manager-visible team view makes dangerous?

### Why it matters

One input changed since v1. v1's strictness leaned hard on the manager reading the team view. v2 simplifies that boundary — reports label people by **initials**, nothing travels as a file, you screenshot what you want to show. That materially weakens the manager argument.

It does **not** weaken the peer argument. Responses stay **named and shared openly within the team**, the team reads them, and peers are the audience most social pressure actually answers to. So the exposure that justifies a strict rule is still there; it just isn't upward any more.

### Options

| Option | Pros | Cons |
|---|---|---|
| **A. Symmetric** — no implied destination in either direction, pro-AI or pro-craft | One rule, no direction lookup. Enforceable by someone who does not know which way the team leans. | Bans some anti-AI framings nobody was going to write anyway. |
| **B. Directional** — only pro-AI framing is banned; framing that nudges toward caution is fine, because that is not the pressure that exists here | Honest about where the real risk is. Slightly more freedom. | Every borderline item becomes an argument about which way it leans. |

### My recommendation

**A, symmetric.** **B** fails your own *"binding and not re-litigated per item"* requirement directly: a directional rule cannot be applied without first arguing the direction of the item in front of you, which is per-item litigation by definition.

There is also a substantive reason. A survey that leads toward caution produces a team that reads as more cautious than it is — the same broken instrument, pointed the other way, and just as useless for deciding what to do next. The point of the survey is to find out where people actually are.

### Your answer

:

---

## Q3 — Must every item be concrete? *(the sharpest edge in this round)*

### What this is

From the pilot, Q2: you want to *"understand each person's core values and principles **without directly asking them for it**."*

Does that become **part of the binding rule**, or stay a stylistic preference?

### Why it matters

This is a second constraint, orthogonal to Q1. Q1 governs whether an item points somewhere. This governs whether an item is allowed to be **abstract** — to ask about a principle in the open rather than put a concrete situation in front of someone and read the principle off their reaction.

It is not a new idea in this repo. Probe rule 7 already says it, for probes only:

> **Concrete scenario**: a named action with a named condition, drawn from work this team actually does. Never an abstract maximal statement ("I completely trust AI").

The question is whether that gets promoted from a probe rule to a rule for the whole bank.

### Options

| Option | Pros | Cons |
|---|---|---|
| **A. Binding** — every item names something concrete: a situation, an action, an artifact. No abstract principle items. | Nothing new to learn; it is Probe rule 7 promoted. Concreteness is also what makes items answerable on gut reaction — which the pilot confirmed was working ("nothing I had to reread"). Delivers the "without directly asking" requirement literally. | Costs more to write. Some Dimensions (Craft values, Concern) are natively abstract and will fight it. |
| **B. Preference** — direct value items allowed where a concrete phrasing would be tortured | Escape hatch for the hard Dimensions. | An escape hatch judged per item is per-item litigation. Same disqualifier as Q2/B. |
| **C. Split** — direct allowed for *direction* items, banned for *value* items | Matches the two things you asked for separately. | Requires classifying each item as value-or-direction before you can check it, and that classification is itself arguable. |

### My recommendation

**A** — with one consequence stated plainly, because it is the sharpest thing in this round.

Under A, *"In what ways do I want to be able to do that development in the future?"* — your own words from round 3 — is an **illegal item as written**. It is an open question about direction with nothing concrete in it. It has to become a set of concrete directions the Respondent reacts to, rather than an open question about direction.

I think that is the right trade: an open question like that gets you prose you cannot score, from a survey with no free-text questions by design, and it re-runs the pilot's original problem — *"I don't know what I'll think in six months."* Someone who cannot forecast their own state also cannot narrate their own direction on demand; they *can* tell you how they feel about a world you describe to them. But it is a real cost and I would rather you agree to it explicitly than discover it in #24.

### Your answer

:

---

## Q4 — Does the rule govern only item text?

### What this is

The Respondent reads more than items: a survey description, section intros, block headings, scale labels, the Coverage grid's level definitions.

### Why it matters

v1 wrote the non-leading rule as an **item** rule, and the section descriptions were never checked against it. A perfectly neutral item sitting under a heading like *"Where we're growing"* is a led item — the heading did the leading and the rule never looked at it.

### Options

| Option | Pros | Cons |
|---|---|---|
| **A. Everything the Respondent reads** | Closes the largest hole in v1's version. Costs one extra check on maybe six pieces of section copy. | Slightly more surface to review. |
| **B. Item text only** — surrounding copy is framing, and framing is allowed to set context | Less to check. | The rule can be routed around in the paragraph above the question. |

### My recommendation

**A.** This is the difference between a rule with teeth and one with a documented bypass. The cost is small and one-off: the section copy is written once and checked once.

### Your answer

:

---

## Anything else

Anything the four questions above didn't leave room for — a form you already know you want, one you already know you hate, or a place you think the rule as sketched will strangle the items when we get to writing them.

### Your answer

:
