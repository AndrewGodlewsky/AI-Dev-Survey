# Grilling — Issue #19: Conditional items

**Ticket:** [Conditional items: locating where a Respondent's line moves](https://github.com/AndrewGodlewsky/AI-Dev-Survey/issues/19)
**Round:** 1 of ? — what job is actually left
**How to use:** answer inline under each `### Your answer` heading. Free text is fine; you don't have to pick one of the listed options. Then tell me it's ready and I'll read it back and compute the next round.

---

## What #8 already settled

This ticket was blocked by [#8](https://github.com/AndrewGodlewsky/AI-Dev-Survey/issues/8), which closed an hour ago. Two of its decisions land directly here:

- **Probe and Conditional stay separate classes over one shared mechanism.** A Probe locates an *extreme*; a Conditional locates the *boundary and what moves it*. Both are **non-scoring per-Respondent attributes** sitting beside a Dimension score, and #12 designs that column family once.
- That means **the ticket's question 4 is already answered**: a Conditional does **not** move a Dimension score. It sits beside it. If you want to reopen that, say so in *Anything else* — otherwise I'm treating it as settled and it doesn't get a question below.

The ticket's remaining questions are shape, which Dimensions, scale, the training-gap escape, and cost. None of them can be asked yet, because of Q1.

---

## Q1 — Does the Coverage grid already do most of this?

### What this is

Before designing a new item class, the same test that saved 28 items on #8: is the instrument already answering this question somewhere?

Look at what the **Involvement level** scale actually is:

> 1 None · 2 Advisor · 3 Drafter · 4 **Doer, reviewed** · 5 **Doer, spot-checked** · 6 **System-verified** *(AI does it end-to-end; automated checks catch errors, no individual looks)*

That is an **escalating-safeguard ladder** — exactly the shape the ticket proposes as option (b). It runs from "I do all the checking" to "a machine does the checking", it is already answered **current and future**, and it is answered **19 times**, once per Development area.

### Why it matters

So the grid already locates the boundary. If someone's future level on *Writing tests* is 5 but on *Security review* is 2, their line is drawn, per area, in the exact currency this ticket cares about.

What the grid does **not** give you is the other two thirds of the ticket's premise:

| | Does the grid answer it? |
|---|---|
| **Where is the line?** | **Yes** — 19 areas × current × future, on a safeguard ladder |
| **What lever moves it?** | **No** — the grid never asks what would make a 2 into a 4 |
| **Is a "no" principle or ignorance?** | **No** — and this is the bug the ticket was actually filed against |

That reframes the ticket. Its opening example is two people who both answer "Never" to *"I let an agent land a change without reading it"* — one on principle, one because they don't know a schema check could stand in for their reading. **The grid does not separate those two either.** Both would put a low number on the same rows. So the ticket's real job survives — but it may be much smaller than "design a new item class", because the *locating* half is already built and paid for.

The argument against: the grid is organised by **Development area**, and Dimensions are not areas. Trust, Comfort and Autonomy have no rows in it. If you want to know where someone's Trust line sits *in general*, the grid only tells you sideways, by inference across 19 rows — and inference is what this survey is trying to avoid.

### Options

| Option | Pros | Cons |
|---|---|---|
| **A. Shrink the ticket to lever + reason** — the grid locates the boundary; Conditional items only ask *what moves it* and *why it's there* | Removes the most expensive half of every shape the ticket proposes. Avoids asking the same person to draw the same line twice in one survey. Keeps the survey's one ladder in one place. | Depends on the grid being read as a safeguard ladder, which is a slightly indirect use of it. Someone who N/As out an area gives you nothing there. |
| **B. Full ticket** — Conditional items locate the boundary *and* the lever, per Dimension, independent of the grid | Dimension-level boundaries stated directly, no inference across 19 rows. Works for Trust and Comfort, which have no grid rows. | Duplicates the ladder. Adds a second, differently-worded escalation scale to a 35–40 minute survey — and two ladders that disagree is a real outcome. |
| **C. Kill the ticket** — the grid is enough | Free. | Leaves the principle-vs-ignorance bug unfixed, which is the thing the ticket was filed for and the thing the grid definitely does not answer. |

### My recommendation

**A.**

The ticket's own framing gives this away: it says the survey "cannot tell them apart", and the *them* is not two positions — it's two **reasons for the same position**. Reasons are what's missing, not coordinates. The grid has 19 coordinates already.

A also keeps the survey honest about the map's length constraint. B is the option that quietly adds a second scale to an instrument that already has three.

### Your answer

: Okay, I think this is fine, just as long as we remember the main point of all these questions is to figure out what people are comfortable with AI-wise right now. Also, as an extension, in a future state, what would they be comfortable with AI doing if some other scenario was true? Or asked another way, what would have to be true for them to be comfortable to a certain point? I don't want to ask the questions that way, but I'm trying to get that answer. If I ask the questions of what would have to be true, it would be hard to frame those questions appropriately, I think, because we'd be asking very toward the edge questions. I don't want to push people's answers in one direction or another. I want them to answer honestly as their true self. 

<!-- If B: is it the Trust/Comfort gap that bothers you, or not trusting the grid to carry this? -->


---

## Q2 — What is the safeguard vocabulary?

### What this is

Whatever shape this lands on, it needs a **closed list of things that could stand in for a human reading the output**. That list is the substance of the item; everything else is packaging.

This is the one question in this ticket only you can answer, because it has to name **things this team actually has or could plausibly have in six months** — a safeguard nobody could adopt is a wasted option, and a safeguard already universal is a wasted option too.

### Why it matters

The list has to do two jobs at once, and they pull apart.

**As a lever**, it should name things that are *actionable*: if four people say "a schema check would move me", that's a piece of six-month plan. Levers must be things the team could go and build.

**As a training-gap detector**, it needs to include things people **might not know are possible**. That's the whole point — the ticket's example is someone who doesn't know a validation script could substitute for their own reading. A list of only obvious safeguards ("tests pass") detects nothing.

Length is the tension. Every option is a thing to read on a gut-reaction instrument. Six is a glance; twelve is a wall, and a wall gets ticked at random or skipped.

### Options

Candidate vocabulary — treat this as a menu to cut, not a proposal:

| Safeguard | Actionable lever? | Might not know it's possible? |
|---|---|---|
| The test suite passes | Yes | No — everyone knows this |
| A type check / schema validation covers it | Yes | **Yes** |
| A linter or static analysis / security scanner covers it | Yes | Partly |
| Another person reviews it | Yes | No |
| It's easy to roll back if it's wrong | Yes | **Yes** — reversibility as a substitute for scrutiny is a genuinely unfamiliar idea |
| The blast radius is small (docs, internal tooling, non-prod) | Yes | Partly |
| A second AI reviews it | Yes | **Yes** |
| It runs behind a flag / staged rollout | Yes | Partly |
| I wrote the spec or the acceptance criteria myself | Partly | Partly |
| Nothing would — I need to read it myself | n/a | n/a — **the principle answer** |

### My recommendation

**Six, plus the principle escape**: test suite · type/schema check · automated security or lint scan · another person reviews · easy to roll back · small blast radius — and *"Nothing would; I need to read it myself."*

That set keeps three genuine might-not-know entries (schema check, rollback, blast radius), drops "a second AI reviews it" as too speculative for a six-month horizon, and drops "I wrote the spec" because it's about authorship rather than verification.

The **principle escape is not optional** — without it, someone whose honest answer is "nothing" has to either leave it blank or falsely tick something, and distinguishing that person is the entire purpose of the ticket.

### Your answer

: Yeah, I think this is fine to go with your recommendation. 

<!-- Cut, add, rename. What does this team actually have, and what would surprise people to learn is possible? -->


---

## Q3 — Is there an explicit "I didn't know that was possible"?

### What this is

The ticket's question 5. The training gap is either **stated** by the Respondent (an explicit option they tick) or **inferred** by you (hard no on the item, yes on the condition).

### Why it matters

This one is not really a measurement question. It's a social question, and the map already decided the thing that makes it hard: **results are named, individual results are visible to everyone who took the survey, and the team view goes to your manager.**

An explicit "I did not know that was possible" is an item that asks a professional developer to **publish an admission of ignorance next to their name**, to their whole team. Two things follow, and they point in opposite directions:

- It will be **under-ticked**. The people most likely to have the gap are the most likely to skip the option, which biases the measurement exactly where it matters.
- If someone *does* tick it, it is enormously valuable — an unambiguous, self-reported, actionable training request, which is the single most useful sentence this survey could produce.

Inference has the mirror problem. "Hard no on the item, yes on the condition" is a clean pattern and costs nothing to collect — but it **cannot tell you which safeguard was the news**. It says the line moved; it doesn't say the person learned something. And an inference presented to a team as fact ("three of you have a training gap") is the kind of finding that starts an argument about the instrument rather than about the work.

There's a third way the phrasing can dodge the whole problem: ask it as a **forward-looking** question rather than a confession. *"Which of these would you want to learn more about?"* collects the same signal with no admission attached — nobody is embarrassed to want to learn something.

### Options

| Option | Pros | Cons |
|---|---|---|
| **A. Explicit confession** — *"I didn't know that was an option"* as a tickable choice | Unambiguous when ticked. Directly actionable. | Named, openly shared results make it costly to tick. Biased against exactly the people it targets. Ticking it in front of your manager's team is a real ask. |
| **B. Inference only** — no such option; you read the pattern | Zero survey cost. No admission required. | Cannot say *which* safeguard was news. Turns a finding into an interpretation, and interpretations get argued with. |
| **C. Forward-looking rephrase** — *"which of these would you want to know more about?"* | Same signal, no confession. Reads as ambition, not ignorance. Actionable as a training list. | Softer: "want to learn more" also gets ticked by people who already know it and are just interested. Measures curiosity as well as gaps. |
| **D. C plus B** — ask the forward-looking version, and read the hard-no/yes-on-condition pattern alongside it | Two independent signals; where they agree you can say something confidently. | One more item, and two signals that disagree need a rule for which one wins. |

### My recommendation

**C.**

A is the right *idea* and the wrong instrument for this survey specifically. The map's visibility decision — individual results shown to the whole team, team view to your manager — was made after this ticket was written, and it makes a confession item structurally unreliable. C gets the same list out of people at no social cost.

Worth noting C changes what you can claim: you get a **training-interest list**, not a proven gap. For planning six months of team development, that's the more useful artifact anyway — you were going to act on it by offering the thing, not by diagnosing anyone.

### Your answer

: Yeah, I think it's fine to have a forward-looking rephrase. 

<!-- Does the visibility argument land? If your team would happily tick A, say so — it's the sharper signal. -->


---

## Anything else

<!-- Free space. Also: if you want to reopen #8's "Conditionals don't score" decision, here's where. -->


---
---

# Round 2 — asking it without asking it

**What round 1 settled**

- **Q1 → A, shrink to lever + reason.** The Coverage grid already locates the boundary, 19 times, current and future. Conditional items only have to supply what the grid can't: the lever and the reason.
- **Q2 → six safeguards plus the principle escape**: test suite · type/schema check · automated security or lint scan · another person reviews · easy to roll back · small blast radius · *"Nothing would; I need to read it myself."*
- **Q3 → C, forward-looking rephrase.** The training signal is collected as *"which of these would you want to know more about?"*, never as a confession.

**And a constraint that changes the shape of this ticket**

Your Q1 answer added something none of the three questions asked about, and it's the most important thing said so far:

> *"what would have to be true for them to be comfortable to a certain point? I don't want to ask the questions that way… we'd be asking very toward the edge questions. I don't want to push people's answers in one direction or another. I want them to answer honestly as their true self."*

That is a hard **non-leading constraint**, and it rules out the ticket's own framing. *"What would have to be true for you to accept AI doing X?"* presupposes that accepting X is a destination — it invites the Respondent to negotiate with themselves toward yes. Someone whose honest answer is *"nothing, and I don't want there to be"* has to argue with the question before they can answer it. That's a push, and a survey read openly by your team and summarised to your manager is the worst possible place for one.

So this round has one real job: **get the conditional answer out without ever asking a conditional question.** Everything else follows.

---

## Q4 — How do we get the lever without a leading question?

### What this is

The framing of the safeguard checklist. The constraint is that no version of it may imply the Respondent ought to move.

### Why it matters

There's a way out, and it comes from the structure the survey already has.

The survey is already **Current + Future**. If the same neutral checklist is asked in both sections — *"which of these do you accept instead of reading AI's output yourself?"* now, and *"which would you accept in six months?"* — then neither question is leading. Both are plain descriptions of a position. But the **difference between the two answers is exactly the conditional answer you wanted**:

> *Today: tests pass. In six months: tests pass, type/schema check, easy rollback.*
> → Schema checks and reversibility are this person's levers.

You never asked "what would have to be true". You derived it. Someone who ticks the same boxes in both sections has told you their line doesn't move — honestly, without ever being nudged, and their "no movement" is a real finding rather than a refusal to engage with a pushy question.

The cost is two items rather than one, and the risk is that a Respondent seeing the same list twice just copies their first answer. Worth naming: on this instrument **copying is a valid answer**, not a failure mode. It means the line is where it is.

There are also two phrasing mechanics that decide whether this stays neutral:

- **"Nothing — I'd read it myself" must sit as a peer**, not as an escape hatch at the bottom of six alternatives. Last-and-alone reads as the odd one out, and people avoid being the odd one out in a named survey.
- **Don't order the list as a ramp** from weakest to strongest safeguard. An escalating order is a ladder, and a ladder implies a direction to climb — the exact push you ruled out.

### Options

| Option | Pros | Cons |
|---|---|---|
| **A. Present tense only** — one checklist in the Current section | Purely descriptive, zero push. Cheapest at one item. | You learn where the line is and nothing about what moves it. Fails the ticket. |
| **B. Future tense only** — *"in six months, which would you accept?"* | One item, matches the Horizon. | Mildly aspirational on its own, and with no baseline you can't tell a lever from the status quo — you can't see what changed if you never asked what was. |
| **C. Both sections, same list; the delta is the lever** | Neither question leads. The conditional answer is derived, never asked. Slots into the Current/Future structure that already exists. "No movement" is a clean, honest result. | Two items. Some Respondents will copy their answers across. |
| **D. Direct conditional** — *"what would have to be true for you to accept…"* | Most direct route to the answer. | The framing you ruled out. Presupposes a destination and pushes toward it. |

### My recommendation

**C.**

It's the only option that satisfies both halves of what you said in Q1 — you want the conditional answer, and you refuse to ask a conditional question. C gets it by subtraction. Two neutral questions, and the arithmetic between them says the thing neither one asked.

### Your answer

: I like your recommendation here. I think that's fine. 

<!-- Does asking the same list twice feel repetitive to you, or fine? -->


---

## Q5 — One checklist, or one per Dimension?

### What this is

The ticket's question 2 — *which Dimensions get a Conditional item*. It proposed Comfort, Trust and Autonomy as candidates.

### Why it matters

The safeguard list has a single subject: **what can stand in for me reading the output**. That is Trust and Autonomy fused — Trust is whether the output is right, Autonomy is how long the leash is, and a safeguard answers both at once. Asking it twice with two framings gets you two versions of one answer, and if they disagree you have no way to say which is true.

Comfort is a different question altogether. Comfort is *willingness to use AI at all*; it isn't about verification, so a safeguard checklist has nothing to say about it. Someone can be entirely uncomfortable with AI and still agree that a passing test suite is meaningful.

That suggests something simpler than the ticket assumed: this isn't a Dimension item at all. It's a **Respondent-level attribute** — one checklist, once per section, attached to the person rather than to any Dimension. That matters downstream: #12 doesn't need a per-Dimension slot for it, just a per-Respondent one.

Against that: if it belongs to no Dimension, the dashboard has to find somewhere to put it that isn't a Dimension view, and the one-pager has to explain a thing that sits outside the structure everything else uses.

### Options

| Option | Pros | Cons |
|---|---|---|
| **A. One checklist, Respondent-level** | Two items total. One vocabulary, asked once. Simplest possible schema — no per-Dimension slot needed. | Sits outside the Dimension structure, so #16 and #17 need a home for it. |
| **B. Three — Comfort, Trust, Autonomy** (the ticket's proposal) | Each Dimension carries its own boundary; every view has one. | Six items. Comfort's version is close to meaningless. Three answers to one question, free to contradict each other. |
| **C. Two — Trust and Autonomy** | Drops the meaningless one; keeps the two that genuinely differ. | Four items, and the two lists would be near-identical — which is the tell that it's really one question. |

### My recommendation

**A**, reported against **both Trust and Autonomy** in the dashboard.

One asking, two readings. The distinction between Trust and Autonomy is real in the *scores*; it isn't real in the *safeguards*, because the same six things answer both.

### Your answer

: I think your recommendation is fine. 

<!-- If A: happy for it to be a Respondent-level attribute rather than belonging to a Dimension? -->


---

## Q6 — What list does the training-interest question use?

### What this is

Q3 landed on the forward-looking rephrase — *"which of these would you want to know more about?"*. This decides what's in it.

### Why it matters

The obvious answer is **the same six safeguards**, and it's obvious for a good reason: the gap this ticket exists to catch is someone who doesn't know a schema check could substitute for their reading. That gap is only visible against the safeguard vocabulary. Reusing the list also means the Respondent reads those six things once and recognises them the second time — one vocabulary, one glance, no new reading.

The pull the other way is that "what would you like to learn" is a broader and genuinely useful question — agents, MCP, custom rules, evals, prompt technique. That's a training list you could act on directly.

But that broader question is **Fluency's job**, and Fluency already has items and a rubric. Widening this item turns it into a second Fluency instrument bolted onto a Trust question, and the two would need reconciling. It also breaks the pairing that makes the signal legible: *didn't tick it as accepted, did tick it as want-to-know* is a clean, self-reported, actionable sentence. Against a broader list, that pairing doesn't exist.

### Options

| Option | Pros | Cons |
|---|---|---|
| **A. The same six safeguards** | One vocabulary. Pairs directly against the accepted-list, so "not accepted + want to know" reads cleanly. No new reading for the Respondent. | Doesn't collect the broader training interest, which someone will want. |
| **B. A broader AI-capability list** | A directly actionable training plan. | Duplicates Fluency. No pairing, so the specific gap this ticket targets becomes invisible again. |
| **C. The six, plus two or three capability entries** | Catches both. | The pairing only works for six of nine entries, so the rule for reading it has an exception — and exceptions are what #17 has to explain. |

### My recommendation

**A**, and let a broader training-interest question be a separate thing if you want one later — it isn't this ticket's job and it isn't blocked by anything here.

### Your answer

: Let's go with your recommendation here. 

<!-- Would you rather have the broader training list, even at the cost of the pairing? -->


---

## Anything else — round 2

<!-- Free space: constraints, objections, anything the non-leading rule should also cover. -->


---
---

# Round 3 — placement, the contradiction, and the name

**What round 2 settled**

- **Q4 → C.** The same neutral checklist in both sections; **the delta is the lever**. The conditional answer is derived, never asked, so nothing pushes anyone. Two phrasing mechanics ride along: *"Nothing — I'd read it myself"* sits as a **peer**, not a trailing escape hatch, and the list is **not ordered as a ramp** from weakest to strongest safeguard.
- **Q5 → A.** One checklist, **Respondent-level**, not a Dimension item — reported against Trust and Autonomy both. #12 needs a per-Respondent slot, not a per-Dimension one.
- **Q6 → A.** The training-interest question reuses **the same six safeguards**, so *"didn't accept it + want to know more about it"* pairs cleanly.

**What's left**

Three loose ends and a naming problem. The naming problem is the interesting one: after round 2, **nothing about this item class is conditional any more**. The ticket named it *"Conditional item — until the glossary says otherwise"*, and the glossary now has to say otherwise.

After this round I believe the frontier is empty and I'll write the resolution.

---

## Q7 — Does the Future checklist get both stance rows?

### What this is

Every Future-state item is answered twice — *For me* and *For the team*. This asks whether the safeguard checklist follows that rule or is exempt.

### Why it matters

The team-stance version is not a formality. *"Which of these should the team accept as enough to skip an individual reading the output?"* is, answered across 5–9 people, **a draft six-month policy** — arguably the single most directly actionable thing this whole survey can produce. "Six of us agree a passing test suite plus a schema check is sufficient; two of us don't" is a norm you can go and write down.

The personal-stance version is what the Q4 delta needs: Current → Future-personal is the lever calculation. The team row is extra, and it answers a different question.

**Cost, with a caveat.** This checklist is a multi-select, and Microsoft Forms' Likert grid is single-select per row — so a two-stance multi-select almost certainly cannot be one grid question. It would be **three separate checkbox questions**: Current, Future-personal, Future-team. That's my reading of Forms, not a verified fact — **#10** is the ticket that confirms it, and if it's wrong this gets cheaper, not more expensive.

Against: three near-identical checkbox questions in a survey the map says must **vary question types so Respondents don't stall**. That's a real cost, and it's the strongest argument for dropping the team row.

### Options

| Option | Pros | Cons |
|---|---|---|
| **A. Both stances** — Current, Future-personal, Future-team | The team row is a draft norm, directly usable. Consistent with every other Future item. The lever still comes from the personal row. | Three checkbox questions, likely consecutive. Most repetitive stretch in the survey. |
| **B. Personal only** — Current, Future-personal | Two questions. Enough for the lever, which is what the ticket was filed for. | Throws away the norm-setting answer — the one output that converts this survey into a decision. |
| **C. Team only** — Current, Future-team | Most directly about the six-month plan. | Breaks the lever: Current is personal and Future is team, so the delta subtracts two different things. Structurally wrong. |

### My recommendation

**A.**

C is a bug, so it's really A vs B, and B discards the norm. The repetition cost is smaller than it looks: the Respondent reads six options once and recognises them twice, so questions two and three are fast even though they look identical. That's cheap repetition — the kind that costs a glance, not a decision.

### Your answer

: Let's go with your recommendation. 

<!-- If the repetition bothers you, B is the honest cut — say so. -->


---

## Q8 — What happens when someone ticks "Nothing" *and* a safeguard?

### What this is

It's a multi-select with a principle escape in it, so a Respondent can tick *"Nothing — I'd read it myself"* alongside *"the test suite passes"*. Microsoft Forms has no native mutually-exclusive option, so this will happen and something has to decide what it means.

### Why it matters

The two readings are opposite and both are plausible. Ticking a specific safeguard is a positive, deliberate act — which argues the specifics are the real answer. But *"Nothing"* is the unusual option; nobody ticks it by accident, which argues it's the considered one.

Guessing wrong matters here, because this is the exact distinction the ticket exists to make. Reading it as principle when it isn't invents a hard constraint on the six-month plan; reading it as a lever when it isn't erases someone's actual position.

And there's a fact that makes this easier than it looks: **there are 5–9 Respondents and their names are on the answers.** You can go and ask. An automated tiebreak here is solving a problem you don't have — and it would be solving it silently, in an Excel formula, where nobody sees the guess being made.

### Options

| Option | Pros | Cons |
|---|---|---|
| **A. Flag it, don't guess** — mark the response inconsistent, exclude it from the derived lever, and ask the person | Never invents a position. Cheap: one formula that raises a flag rather than one that picks a winner. Honest in the dashboard. | Needs an inconsistency state in #12/#16, and someone has to actually go and ask. |
| **B. "Nothing" wins** — treat as principle, ignore the other ticks | Conservative; never overstates willingness. | Discards deliberate positive answers. Manufactures hard constraints that may not exist. |
| **C. Specifics win** — ignore "Nothing" if anything else is ticked | Keeps the richer signal. | Overwrites the one answer nobody ticks by accident. |
| **D. Prevent it** — restructure as single-select "the highest thing you accept" | No contradiction possible. | It's a ladder, and Q4 ruled ladders out — an ordered escalation implies a direction to climb. |

### My recommendation

**A.**

At n=9 with named responses, "go and ask" is a genuinely available option, and it beats every silent rule. The flag also costs almost nothing: #12 already needs a per-Respondent attribute slot from Q5, and an inconsistency marker rides in it.

### Your answer

: Let's go to your recommendation. 

<!-- Would you actually chase someone down over this, or would you rather it just resolve itself? -->


---

## Q9 — Which section does the training-interest question live in?

### What this is

Q3/Q6 settled *what* it asks — the same six safeguards, framed as *"which of these would you want to know more about?"*. This is where it sits.

### Why it matters

It's forward-looking, so the Future section is the natural home. The sharper question is whether it sits **immediately after** the future checklists or somewhere else.

Immediately after means the six options are already read and fresh — the Respondent answers on recognition, which is what the gut-reaction constraint wants. It also puts four checkbox questions in a row, which is the most monotonous stretch in the survey.

Separating it breaks the monotony but forces a cold re-read of six options with no context, which is slower and worse — and it puts distance between the two answers whose *pairing* is the entire signal.

### Options

| Option | Pros | Cons |
|---|---|---|
| **A. Future section, immediately after the checklists** | Options already fresh; answered on recognition. Keeps the paired answers adjacent. | Four checkbox questions in a row. |
| **B. Future section, but separated** | Breaks up the monotony. | Cold re-read of six options. Splits the pairing. |
| **C. End of the survey, on its own** | Reads as a friendly closing question rather than part of the instrument. Ends the survey on ambition rather than assessment. | Furthest from context. Last questions get the least attention — and this is the one meant to catch people who don't know what's possible. |

### My recommendation

**A.**

The monotony objection is real but it's the cheapest kind of repetition — same options, third look, no new reading. C is tempting for tone, but the last question on a 35–40 minute survey is the worst place to put the item designed to catch the least-engaged answer.

### Your answer

: Let's go with your recommendation. 

<!-- C has a real tone argument — take it if you'd rather end on that note. -->


---

## Q10 — What is this class called?

### What this is

The ticket says *"call it a **Conditional item** until the glossary says otherwise"*. Round 2 made it otherwise.

### Why it matters

After Q4, **nothing about the question is conditional**. It doesn't ask "what if", it doesn't state a condition, and its whole design point is that it *refuses* to ask conditionally. What it actually asks is: *which safeguards do you accept in place of reading the output yourself?* — a plain description of a position, asked twice.

Calling that a "Conditional item" would leave the glossary describing the thing the ticket rejected, and the name propagates into #12, #15, #16 and #17. It also collides with `CONTEXT.md`'s existing precision: **Probe item**, **Behaviour item**, **Attitude item** are all named for what they *are*, not for what's inferred from them.

There are really two things needing names — the **question** and the **thing derived from two askings of it** — and conflating them is how "Conditional" got confusing in the first place.

### Options

| Option | Pros | Cons |
|---|---|---|
| **A. Two terms** — a **Safeguard item** (the checklist) and a **Lever** (a safeguard accepted in future but not now) | Names the question for what it is and the derivation for what it is. Matches the existing naming style. "Lever" is the word you'd use in the room anyway. | Two new glossary entries instead of one. |
| **B. Keep "Conditional item"** | Zero churn; #8's resolution already uses it. | Describes a design that was rejected. The item is not conditional and a reader will look for the condition. |
| **C. One term** — **Safeguard item** only; the delta stays unnamed | Leanest. | The delta is the ticket's whole output. An unnamed output gets described three different ways across #16 and #17. |

### My recommendation

**A** — **Safeguard item** and **Lever**, and retire "Conditional item" from the glossary entirely.

The class relationship #8 established still holds; only the name changes. Probe locates an extreme, Safeguard item locates what substitutes for scrutiny, and both are non-scoring per-Respondent attributes over one shared mechanism. I'll note the rename on #8 so its resolution doesn't strand a dead term.

### Your answer

: Let's go with your recommendation. 

<!-- Better names welcome — this one ends up in the one-pager. -->


---

## Anything else — round 3

<!-- Last call. -->


---
