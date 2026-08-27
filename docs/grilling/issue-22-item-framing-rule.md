# Grilling — Issue #22: Item framing rule

**Ticket:** [Item framing rule: what replaces the non-leading rule](https://github.com/AndrewGodlewsky/AI-Dev-Survey/issues/22)
**Map:** [Map v2: Survey overhaul & local dashboard app](https://github.com/AndrewGodlewsky/AI-Dev-Survey/issues/21)
**Round:** 1 of ~3 — four questions *(round 2 appended below)*
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

: Let's go with rule A then. 

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

: I don't really want to have an implied direction, either pro or anti-AI. I just want to have a spectrum of questions that will reveal where someone wants to be both now and in the future, and where they think the team should be or how the team should be working going forward. 

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

: I think ultimately, particularly for the team level, things are gonna have to end up being a little bit split because we're gonna need to see both the value and direction items. At a team level, those are really important, but at an individual level, particularly for the now section, the me today, I think everything we have is fine. 

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

: Let's go with your recommendation here. 

---

## Anything else

Anything the four questions above didn't leave room for — a form you already know you want, one you already know you hate, or a place you think the rule as sketched will strangle the items when we get to writing them.

### Your answer

:

---

# Round 2 — the forms, the test, and what the rule keeps

**Round:** 2 of 3 — eight questions. This is the last *question* round; round 3 is you reacting to the written rule.
**How to use:** same as before — answer inline under each `### Your answer`, then tell me it's ready.

**What round 1 settled**

- **Q1 → A. The rule names the harm: no implied destination.** An item may not contain or presuppose a position the Respondent is supposed to be moving toward. Every specific ban falls out of that.
- **Q2 → symmetric.** No implied destination in *either* direction. Your words: *"a spectrum of questions that will reveal where someone wants to be both now and in the future, and where they think the team should be."* The survey locates; it never points.
- **Q3 → split, by block.** Read back in Q5 below, because your answer settled the principle and left one block unassigned.
- **Q4 → A. The rule governs everything the Respondent reads** — form description, section intros, headings, scale labels, option lists — not just item text.

**One thing your Q3 answer surfaced.** You said *"at a team level, those are really important"* — value items and direction items both. That means the rule has to define what a *value item* and a *direction item* actually are, because until now the repo has only had Behaviour items, Attitude items and Probe items. Q6 names them.

**What this round holds back**

- **The rule document itself.** Everything below settles what it says; round 3 is you reading the draft and marking what's wrong.
- **Glossary edits.** *Framing rule*, *Scenario item*, *Direction item*, *Value item* go into `CONTEXT.md` once Q6 and Q12 fix the names and the home — not before.

---

## Q5 — Read-back: which blocks must be concrete?

### What this is

Your Q3 answer:

> *"particularly for the team level, things are gonna have to end up being a little bit split because we're gonna need to see both the value and direction items. At a team level, those are really important, but at an individual level, particularly for the now section, the me today, I think everything we have is fine."*

Two blocks are clear from that. One is not.

| Block | Concreteness | Source |
|---|---|---|
| **Current-state section** (me today) | Frozen — untouched by this rule beyond the Q4 copy check | "everything we have is fine" |
| **Team section** | **Split**: concrete direction items *and* directly-stated value items are both legal | "we're gonna need to see both" |
| **Forward personal block** (me, six months as direction) | **Not said** | — |

### Why it matters

The forward personal block is the one the pilot found repetitive and the one [Forward personal block: from prediction to direction](https://github.com/AndrewGodlewsky/AI-Dev-Survey/issues/24) rewrites next. It inherits whatever this says. Leaving it unassigned means #24 has to re-open this ticket on its first item.

### Options

| Option | Pros | Cons |
|---|---|---|
| **A. Forward personal = concrete only** — scenario and direction items; no directly-stated value items | The block where "I don't know what I'll think in six months" bit hardest is exactly the block where reacting to a described world beats being asked a principle. Keeps the personal side gut-answerable, which the pilot said was working. Value items live in the team section only. | Personal values are read *off* reactions, never asked. If you want "what do *I* believe" stated flat, it isn't here. |
| **B. Forward personal = split too** — same as team | Symmetric with the team section; one rule for both forward blocks. | Puts abstract principle items back into the block the pilot said felt like re-answering. An abstract value item and its Current-state attitude twin are the same sentence in a different tense. |

### My recommendation

**A.** Your pilot answer was *"understand each person's core values and principles **without directly asking them for it**"* — that is a description of A. The team section is different because a team-level value (*"every line that ships should be understood by someone"*) is a **norm** being proposed, not a self-report, so stating it flat doesn't collapse into the Current-state item. The personal one does.

### Your answer

: So for me, the forward personal section is really about trying to figure out How the person, as an individual developer, thinks AI can help them, or how they want to integrate with AI. It's more about looking forward, trying to get down to the principles of what they'd be willing to accept and what they're interested in doing by asking them questions that will reveal those types of answers. As far as the team section, this is more about how, as an individual, they want to work with other individuals who are using AI. It's about, as a group, what are acceptable and unacceptable patterns and principles for us as a team. 

---

## Q6 — The form catalogue: which item forms exist, and is the list closed?

### What this is

The rule needs to say what a legal item *looks like*, by form, with the illegal twin beside each so nobody has to argue from the principle every time. Proposed catalogue — the forms, not the final wording:

| Form | What it is | Legal example | Its illegal twin (and why) |
|---|---|---|---|
| **Scenario item** | A concrete way of working, stated in the present tense as if it were already how things are, followed by a reaction on the Desirability scale. Says nothing about whether that world is coming or good. | *"AI writes the first draft of every PR on this team."* → Definitely not … Definitely | *"AI is ready to write the first draft of every PR — how far would you let it go?"* — "ready" and "how far" both place a destination. |
| **Direction item** | A concrete practice, asked as *want* (personal: "I want to…") or *should* (team: "the team should…"). The practice is named; the scale carries the direction. | *"The team should run agents unsupervised on migrations, with rollback as the only gate."* | *"In what ways do you want to be able to develop with AI?"* — open, not concrete, asks the Respondent to narrate a direction. |
| **Value item** *(team section only, per Q5)* | A principle stated flat, as a proposed team norm. Abstract by nature — the one place the rule permits it. | *"Every line that ships should be understood by someone on the team."* | *"How important is it that we don't lose the ability to understand our own code?"* — presupposes the loss is coming. |
| **Probe item** | A scenario item at a pole, unscored, raising an Edge marker. Unchanged from `probe-items.md` rules 1–7. | *"…merge AI-written code I had not read line by line, as long as the tests pass."* | *"…would you eventually merge AI code unread?"* — "eventually" is a ramp. |
| **Checklist item** | A multi-select plain description of a position (the Safeguard item is the only one today). | *"Which of these do you accept in place of reading the output yourself?"* | *"Which of these would it take for you to stop reading the output?"* — a threshold. |

Banned outright, as consequences of *no implied destination*: **threshold** items (*"what would AI have to do / prove before…"*), **ramp** wording (*yet, still, ready, eventually, further, more than today, go as far as*), **open direction** questions (*"in what ways…"*), and any item whose honest answer *"no, and I don't want that"* has to argue with the question before it can be given.

### Why it matters

A catalogue is what makes the rule checkable without litigation: a draft is one of these forms or it is not an item. The question is whether the list is **closed**.

### Options

| Option | Pros | Cons |
|---|---|---|
| **A. Closed** — these five forms; adding a form means reopening this rule, not arguing an item | Enforceable by someone who wasn't in the room. Matches *"the truth and can't be overturned."* | If #23 or #24 needs a sixth form, it comes back here. That's a feature. |
| **B. Open** — the five are examples; any item passing the Q7 test is legal | Flexibility for the item tickets. | "Passes the test" for an unnamed form is exactly the per-item argument you disqualified in round 1. |

### My recommendation

**A, closed.** And I'd take corrections to the catalogue *now* — a form you know you want that isn't here, or one you'd cut — rather than in #24.

### Your answer

: Yeah, let's go with your recommendation here. 

---

## Q7 — The test: what does a draft item pass or fail, and who runs it?

### What this is

*"A test a draft item passes or fails, not a feeling."* Proposed, in order — an item stops at the first failure and is rewritten or dropped, never argued:

1. **Form** — it is one of the Q6 forms, and the form is legal in its block (Q5).
2. **The flip** — write the opposite position. *"AI writes the first draft of every PR"* ↔ *"No PR here starts from an AI draft."* If the opposite reads as a normal thing to want, the item is symmetric. If the opposite reads like a confession or a refusal, the original was pointing.
3. **The refusal** — someone whose honest answer is *"no, and I don't want that"* can give it by picking the bottom of the scale, without contradicting anything in the sentence.
4. **The vocabulary** — none of the ramp words (Q6), no "would have to", no comparative against today (*more, further, beyond what I do now*).
5. **Concrete** *(where Q5 requires it)* — names an action, artifact or situation drawn from this team's work.

Tests 2 and 3 are the ones with teeth; 1, 4 and 5 are the cheap screens that catch most failures before you need them.

### Why it matters

Without a fixed sequence, "does it lead?" is a taste question, and taste is re-litigated per item. With one, a rejected item has a numbered reason.

### Options

| Option | Pros | Cons |
|---|---|---|
| **A. Drafter runs it; the result is not recorded per item** — the item bank file states once that every item passed, and a failed draft never appears | Fewest files, no annotation noise. Rejections show up in the ticket's grilling record when they're interesting. | You have to trust the statement. |
| **B. Drafter runs it; each item carries its flip** — the bank lists every item with its opposite beside it | The flip is visible, so you can check the symmetry at a glance while reacting to drafts. | Doubles the bank's length. |
| **C. You run it** — the agent drafts, you apply the five checks | Human judgement on every item. | ~50 items × 5 checks, by hand, on a ticket you already found repetitive to answer. |

### My recommendation

**A**, with one addition from B: the drafter shows the flip **only for items it was unsure about**, in the ticket's grilling record, so you see the judgement calls and nothing else. Ponytail mode.

### Your answer

: Yeah, I think these are fine. Let's go with your recommendation. 

---

## Q8 — Probe items: do they survive as a form?

### What this is

Probes exist because of the *old* rule — they replaced the free-text questions the survey has none of, and they were designed so the edge is a sentence somebody owns in the room. All five sit in the Future-state section, which #24 is rewriting.

Under the new rule a probe is a **scenario item at a pole**: it states an extreme concrete world and asks for a reaction. It passes every check in Q7 as written — the Trust probe's flip (*"I would not merge AI code I hadn't read, even with tests green"*) is a normal thing to want.

### Why it matters

If probes stay a form, #24 and #23 decide *how many* and *where*. If they don't, the Edge marker machinery in the Rubric and the dashboard goes with them.

### Options

| Option | Pros | Cons |
|---|---|---|
| **A. Probes survive as a form**; count and placement are #24's and #23's call | Nothing to rebuild; the Edge marker is the one output that names a person at a position rather than averaging them. Rules 1–7 already satisfy the new rule. | The five current probes are worded for a *prediction* block ("in six months, I would…") and need re-tensing to present-tense scenarios. |
| **B. Retire the form** — every scenario item can be extreme; the Edge marker fires on any item you designate | Simpler catalogue. | Loses the design property that a probe is *never scored*. A scored item at 5 is a data point; a probe at 5 is a conversation. |

### My recommendation

**A.** Re-tensing is #24's job; the form stands.

### Your answer

: Yeah, let's go with your recommendation.

---

## Q9 — Levers, and the Safeguard mechanics: consequence or casualty?

### What this is

Two things in `safeguard-items.md` were built *from* the old rule:

- **Levers are derived by subtraction, never asked.** The direct question — *"what would have to be true for you to stop reading it yourself?"* — is the archetypal threshold item, and under *no implied destination* it stays banned. So if Levers exist in v2 at all, they stay derived. Whether the future-personal Safeguard asking survives is #24's decision; this ticket only fixes that it can't be replaced by asking.
- **Three neutrality mechanics for the checklist**: the principle answer (*"I'd read it myself"*) comes first; the list is not ordered as a ramp; ticking the same boxes twice is a valid answer.

### Why it matters

The mechanics were written for one item. Q4 (everything the Respondent reads) means option order and option lists are now in scope everywhere — so they either become general rules of the Framing rule or stay a local note on one item.

### Options

| Option | Pros | Cons |
|---|---|---|
| **A. Both survive as consequences of the new rule** — "derived, never asked" stands; the three mechanics become general rules for every checklist and option list | The old rule's two best ideas are kept *because* they follow from the new one, not out of loyalty. One place to look. | None real. |
| **B. Levers may be asked directly now that the rule changed** | Fewer items. | It's the exact item the new rule bans. Disqualified by Q1. |

### My recommendation

**A.** This is close to a formality, but the ticket body asks it by name and #24 needs to know it cannot cut the future Safeguard asking and replace it with a question.

### Your answer

: Yeah, I like your recommendation. 

---

## Q10 — Scales versus ramps: does the frozen Coverage grid pass its own rule?

### What this is

A conflict the rule has to resolve explicitly, because you froze one side of it.

The Safeguard mechanic says *"the list is not ordered as a ramp — an escalation is a ladder, and a ladder implies a direction to climb."* The Involvement level scale is, literally, a ladder: 1 None → 6 System-verified, in order, with numbers. So is every Likert scale. Under Q4 the Respondent reads all of it.

### Why it matters

Read strictly, the new rule fails the frozen "today" Coverage grid. That can't be the outcome — but the rule has to say *why* it isn't, or the first person to draft a team-section ordinal item will hit the same wall.

### Options

| Option | Pros | Cons |
|---|---|---|
| **A. Ordinal scales are instruments, not options.** The ramp ban applies to *unordered* choice lists presented as an escalation, and to copy that names one end of a scale as the good end. A numbered scale whose ends are both stated neutrally is a measurement, and measurements are allowed. | Keeps the grid and every Likert scale, on a stated principle. The ban still catches *"1 Skeptic … 5 Early adopter"* — a scale whose *labels* point. | Someone could argue a 1–6 scale points at 6 by existing. Answer: the intro already says a cautious answer is as useful as a keen one, and that copy is now covered by Q4. |
| **B. No carve-out — the grid is frozen by fiat and the rule is silent** | Nothing to write. | The rule has an undocumented exception on day one. |

### My recommendation

**A.** It also gives the rule its check for scale labels: **both ends of a scale must be equally sayable.** *None* and *System-verified* pass. *Reluctant* and *Confident* would not.

### Your answer

: Let's go with your recommendation. 

---

## Q11 — Does the rule bind the bank, not just the item?

### What this is

Every item can pass Q7 individually while the *bank* still leans: if all twelve scenario items describe a world with more AI than today, the section as a whole says where things are going, and no single item is at fault.

v1 handled the analogue with a rule on the bank — *every Dimension has at least one Reverse-keyed item*. This is the same idea for direction.

### Why it matters

Symmetry (Q2) was the point. A symmetric rule applied only per item does not produce a symmetric survey.

### Options

| Option | Pros | Cons |
|---|---|---|
| **A. Bank-level balance rule** — every scenario/direction block contains at least one item describing *less* AI than today, or the status quo held deliberately | The spectrum you asked for actually appears on the page. Cheap: one or two items per block. Same shape as the reverse-key rule, which already exists and worked. | Someone has to write the less-AI scenarios well — a strawman less-AI item is itself a pointer. That's what the Q7 flip catches. |
| **B. Per-item only** | Nothing extra to write. | The lean creeps in through selection, and the rule can't see it. |

### My recommendation

**A.** Word it as a floor, not a ratio: *at least one* per block, so it can't be gamed into a quota argument.

### Your answer

: Let's go with your recommendation here. 

---

## Q12 — Where is the rule written, and what is it called?

### What this is

Today the old rule lives as a section inside `survey/safeguard-items.md`, a line in the map's Notes, and two glossary entries (*Safeguard item*, *Lever*) that restate it. The new one is binding across every block, so it needs one home everything else points at.

The name matters too. *Non-leading rule* is the thing being gutted; reusing the name invites someone to read the old text.

### Why it matters

Drafters look in `survey/` when writing items. Readers wondering *why* the v1 rule vanished look in `docs/`. The glossary is where the term has to resolve. Ponytail mode says the fewest files that satisfy all three.

### Options

| Option | Pros | Cons |
|---|---|---|
| **A. `survey/item-framing-rule.md`** holds the rule, catalogue and test; `CONTEXT.md` gains a one-line **Framing rule** term pointing at it; `safeguard-items.md`'s rule section becomes a pointer; **plus a short ADR** (`docs/adr/0001-item-framing-rule.md`) recording that v1's rule was overturned and why | Rule sits beside the items it governs; the ADR carries the *why* so nobody re-derives v1's rule from `issue-19`; glossary resolves the term. All three ADR criteria hold: hard to reverse, surprising without context, a real trade-off. | Two new files. `docs/adr/` doesn't exist yet — this would be the first. |
| **B. Rule doc + glossary, no ADR** | One new file. | The reversal of a rule three v1 tickets were built on is exactly the decision a future reader will ask about. The grilling records hold the answer, but nobody reads those cold. |
| **C. ADR only** — the rule *is* the ADR's Decision section | One file, and it's the binding one. | Drafters don't look in `docs/adr/` for a form catalogue, and ADRs aren't meant to be edited as the catalogue grows. |

### My recommendation

**A** — it's a close call against B on ponytail grounds, but the ADR is fifteen lines and it's the one this repo actually needs. Name: **Framing rule**. The glossary entry names the harm in one sentence and points at the doc; the doc holds everything from Q6–Q11.

### Your answer

: Let's go with your recommendation here. 

---

## Anything else

A form you want that Q6 doesn't list, an item you already know you want to write that you suspect Q7 would fail, or a place where the rule as sketched will strangle #23 or #24.

### Your answer

:

---

# Round 3 — the written rule

**Round:** 3 of 3 — one question. React to the draft; the ticket closes on your word.
**How to use:** read [`survey/item-framing-rule.md`](../../survey/item-framing-rule.md). Mark anything wrong inline under Q13, or say it's ready.

**What round 2 settled**

- **Q5 → A.** Forward personal block is **concrete only** — Scenario and Direction items, no Value items — because its job is to reveal *"what they'd be willing to accept and what they're interested in doing"* without asking for it flat. The team section is **split**: all five forms, Value items legal there and nowhere else, because its job is *"how, as an individual, they want to work with other individuals who are using AI … as a group, what are acceptable and unacceptable patterns and principles."* Both purpose statements are handed to #24 and #23 verbatim in the rule doc.
- **Q6 → A, closed catalogue** of five forms: Scenario, Direction, Value, Probe, Checklist.
- **Q7 → A.** Five checks in order — form, flip, refusal, vocabulary, concrete. The drafter runs it; the bank states once that everything passed; the flip is shown only for judgement calls, in the ticket's grilling record.
- **Q8 → A.** Probes survive as a form; count, placement and re-tensing are #24's and #23's.
- **Q9 → A.** Levers stay derived-never-asked; the three option-list mechanics become general.
- **Q10 → A.** Ordinal scales are instruments, not option lists; *both end labels equally sayable* is the scale check. The frozen grid passes.
- **Q11 → A.** Balance floor: at least one less-AI-or-status-quo item per Scenario/Direction block.
- **Q12 → A.** Named the **Framing rule**. Home: `survey/item-framing-rule.md`; glossary term in `CONTEXT.md`; `safeguard-items.md`'s old rule section is now a pointer; first ADR at `docs/adr/0001-item-framing-rule.md`.

**What was written** (all on the working tree, uncommitted — your commit):

- `survey/item-framing-rule.md` — the rule, the per-block table, the catalogue with illegal twins, the banned list, the test, scales, option lists, the bank floor, what survives from v1, and what each downstream ticket inherits.
- `docs/adr/0001-item-framing-rule.md` — why v1's rule was overturned and what was rejected.
- `CONTEXT.md` — new terms **Framing rule**, **Scenario item**, **Direction item**, **Value item**, **Checklist item**; *Probe item*, *Safeguard item* and *Lever* re-pointed at the rule.
- `survey/safeguard-items.md` — "The non-leading rule" section replaced by a pointer; the three mechanics kept.

---

## Q13 — Is the written rule the rule?

### What this is

The doc is the decision now; this record is only how it was reached. Two things worth a second look while reading:

1. **The illegal-twin column.** Each is my best example of the failure mode. If one reads as *legal* to you, the rule has a hole and the example should change, not your reading.
2. **The ramp vocabulary list** (*yet, still, ready, eventually, further, more than today, go as far as, beyond what I do now*). It is a screen, not the test — a word on the list fails an item; a word off the list does not pass it. Add any you already know you'd reach for.

### My recommendation

Ship it as written. Anything you change in the doc is the rule; I'll mirror it into the ADR and glossary if it moves a definition.

### Your answer

: Ship it — close #22 and update the map. *(answered in chat, 2026-08-27)*
