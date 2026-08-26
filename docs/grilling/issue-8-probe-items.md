# Grilling — Issue #8: Probe items

**Ticket:** [Probe items: definition, count and scoring rule](https://github.com/AndrewGodlewsky/AI-Dev-Survey/issues/8)
**Round:** 1 of ? — what a Probe item is *for*
**How to use:** answer inline under each `### Your answer` heading. Free text is fine; you don't have to pick one of the listed options. Then tell me it's ready and I'll read it back and compute the next round.

---

## The arithmetic that makes this a real decision

The ticket carries its own recommendation — *"one at each pole, so 2 per Dimension per section"*. Before anything else, here is what that costs:

| | items |
|---|---|
| Base Dimension items (7 Dimensions × 2–3 × 2 sections) | 28–42 |
| Coverage grid | 19 rows × 2 sections |
| Context item | 1 (a 5-row matrix) |
| **The ticket's recommendation** (2 poles × 7 Dimensions × 2 sections) | **+28** |

The map fixes length at "accept ~35–40 minutes". The ticket's own recommendation roughly **doubles the Dimension half of the survey**. So "how many probes" is not a detail hanging off "what is a probe" — it is most of the ticket, and it is decided entirely by what you think a probe is *for*.

That is why this round is three questions and none of them is "how many". Count, poles, section coverage and scoring rule all fall out of Q1 the moment it is settled; asking them now would be asking you to guess at your own answer.

---

## Q1 — What is a Probe item *for*?

### What this is

`CONTEXT.md` currently defines a Probe item as *"a deliberately extreme statement placed at a far end of a Dimension (e.g. 'I'd merge an agent's PR unread if CI is green') whose purpose is to locate people at the edges. Used instead of open-text prompts."*

Two different jobs are hiding inside that one sentence, and they build opposite instruments.

### Why it matters

**The measurement reading.** With 2–3 items on a 1–5 scale, a small team piles onto 3 and 4 and every Dimension comes back looking the same. On this reading a probe is a **ceiling-stretcher**: an item extreme enough that only genuinely edge-positioned people endorse it, pulling the top of the scale apart so the Dimension mean discriminates. If that is the job, probes *must* count in the mean (a marker that doesn't score can't spread a score), they need **both** poles (a scale is compressed at both ends), and they need to exist in **both** sections. That is the +28.

**The conversation reading.** The map records that results are named, shared openly, and read by 5–9 people who will sit in a room together. It also records that the survey has **no free-text questions** — the probe is what replaces them. On this reading a probe is a **marker**: its output is not a number, it is a sentence somebody has to own. *"Andrew said he'd merge an agent's PR unread if CI is green"* is the thing that starts the argument the survey exists to start. One probe, at the one pole that matters, on the Dimensions where an edge position actually changes the team's six-month plan.

The two readings also differ on damage. `rubric/dimension-levels.md` was written so each 1–5 level reads as a **position** — level 3 Trust is *"trusts AI output on familiar, well-specified work; anything else gets full scrutiny"*. That text is only true if the score means what the rubric says. An extreme item is one nearly everyone answers 1 or 2, so folding it into the mean drags every Current score down by a fraction that has nothing to do with the person's actual position — and quietly detaches the number from the words already written for it.

Against that: a marker-only probe is an item that costs a Respondent's attention and produces no score. It has to earn its place on the strength of the sentence alone.

### Options

| Option | Pros | Cons |
|---|---|---|
| **A. Measurement** — probes stretch the scale and score like any other item | One rule for every item; nothing special in the Scoring sheet or the dashboard. Genuinely does spread a compressed scale. | +28 items. Detaches Dimension scores from the rubric's level text. 5–9 people and 2–3 items is not an instrument that psychometrics can rescue. |
| **B. Marker** — probes never touch the mean; they flag a named person at an edge | Cheap: one per Dimension, one section, one pole. Keeps the rubric honest. Produces the artifact the room actually argues about. Replaces the free-text questions the map ruled out. | Needs its own column in the scored CSV and its own treatment in the dashboard. Items that don't score can feel like wasted questions to a Respondent. |
| **C. Both** — score in the mean *and* flag the edge (the ticket's recommendation) | Nothing is thrown away; the flag is free once the item exists. | Inherits A's costs in full — the +28 and the rubric drift — and adds B's plumbing. "Both" here is not a compromise, it is A plus extra work. |

### My recommendation

**B.**

The *Layered view* is already defined as "every Respondent's position overlaid with the Team mean" — on a team of 5–9 that view is a row of individually visible dots. Discrimination is not the scarce thing when you can see every dot. What's scarce is a reason to talk about a specific dot, and that is exactly what a marker produces.

B is also the only option that is cheap enough to be honest about the 35–40 minute budget: roughly **7 extra items across the whole survey** instead of 28.

### Your answer

:Let's go with your recommendation. B is fine. 

<!-- If neither: what would make a probe worth its question to you? -->


---

## Q2 — Concrete scenario, or abstract extreme?

### What this is

The phrasing rule every probe is written against. Compare:

- **Concrete:** *"I would merge an agent's PR unread if CI is green."*
- **Abstract:** *"I completely trust AI-generated code."*

Both sit at the top of Trust. They do not behave the same way.

### Why it matters

The map sets a hard constraint: items must be answerable on **gut reaction**, and nothing may invite a long, thought-out answer. That constraint cuts both ways here.

An abstract extreme is *cheap to endorse*. "Completely trust" has no consequence attached, so people who would never actually do the thing still tick it — and people who would do it hesitate, because "completely" sounds like a character flaw. The answers cluster in the middle for reasons that have nothing to do with the Dimension.

A concrete scenario has a consequence baked in, so the gut answers it correctly and fast. It is also the phrasing that survives contact with the room: nobody has an argument about a 4.2, and everybody has an argument about merging unread.

The cost is that a concrete scenario is *narrower*. "I'd merge an agent's PR unread if CI is green" doesn't fire for someone who would happily do that on a docs change but not on payment code — and it is meaningless to anyone whose work has no CI. A probe written too specifically measures the scenario rather than the Dimension.

### Options

| Option | Pros | Cons |
|---|---|---|
| **A. Concrete scenario** — a named action with a named condition | Gut-answerable. Consequence attached, so endorsement means something. Produces a quotable sentence. | Narrow; can miss people whose edge is real but sits in a different scenario. Must be picked to fit *this* team's actual work. |
| **B. Abstract extreme** — a maximal statement of the Dimension | Applies to everyone regardless of what they work on. Trivial to write, one per Dimension, no domain knowledge needed. | Cheap to endorse and cheap to refuse; the answer measures self-image. Produces no sentence worth quoting. |
| **C. Concrete, with the condition removed** — *"I would merge an agent's PR without reading it"* | Keeps the action's consequence, drops the CI dependency, so it fires for everyone. | Loses the thing that makes an edge position defensible. Some people's honest answer is "yes, *if* something else checked it" — and with the condition gone they answer no, which is exactly the conflation #19 exists to fix. |

### My recommendation

**A** — concrete scenario, one sentence, a named action with a named condition, and the scenario drawn from work this team actually does.

Note the tension C exposes: the condition is what makes a probe honest, and it is also the seam that ticket **#19 (Conditional items)** is about. Settling A here doesn't pre-empt #19 — it means the probe states *one* condition as a fixed part of the sentence, while #19 decides whether the survey asks separately about *which* conditions move someone. Worth confirming you read it the same way.

### Your answer

: Let's go with your recommendation here. 

<!-- If A: any scenario that is obviously wrong for this team? (e.g. no CI on some work) -->


---

## Q3 — Does the Coverage grid get Probe items?

### What this is

Whether the 19-row Coverage grid carries probes of its own, or is left alone.

### Why it matters

The grid is the largest artifact in the survey — 19 rows, answered current and future. Anything added to it is multiplied by 19, so it is the single most expensive place a probe could land.

It is also the place least in need of one. The Involvement level scale already tops out at **6 — System-verified**: *"AI does it end-to-end; automated checks catch errors, no individual looks."* That is a probe by the definition in `CONTEXT.md`. It is deliberately extreme, it sits at a far end, and it locates people at the edge — and there are already **19 of them**, one per Development area, at zero additional cost. Someone selecting it on *Security review* or *Incident response* has marked themselves more sharply than a purpose-built item would.

The argument on the other side: level 6 is an *anchor on a scale*, not a statement someone endorses. Picking 6 is a low-friction click at the end of a row; agreeing with a written probe is a small act of commitment. If the grid's edges are the ones you most want the team to argue about, an anchor may be too quiet to do it.

### Options

| Option | Pros | Cons |
|---|---|---|
| **A. No probes on the grid** — level 6 already is one | Free. 19 edge markers already exist. Nothing added to the biggest artifact. | Level 6 is a click, not a commitment; some people will pick it casually and the flag misfires. |
| **B. A probe row or two on the grid** — extreme scenarios for the highest-stakes areas | Turns the areas that matter most (security, incident response) into explicit, quotable positions. | Breaks the grid's uniformity — a grid where some rows are areas and some are statements is confusing to answer and to score. Adds items to the ×19 artifact. |
| **C. No probe rows, but treat "6" as a flag in the dashboard** | Zero survey cost, and the edge markers get surfaced rather than averaged into a profile. | Pushes work into the dashboard and the scored CSV. Depends on Q1 landing on B for the concept of a "flag" to exist at all. |

### My recommendation

**A**, with **C** as a free follow-on if Q1 lands on the marker reading — in which case selecting 6 on a high-stakes area shows up in the dashboard the same way a probe endorsement does, and no new items are written.

### Your answer

: I think your recommendation here is fine. 

<!-- Are there Development areas where a 6 would genuinely alarm you? Those are the C candidates. -->


---

## Anything else

<!-- Free space: constraints, objections, things these three questions missed. -->


---
---

# Round 2 — where probes go, and what fires them

**What round 1 settled**

- **Q1 → B, marker.** A Probe item **never enters a Dimension mean**. Its output is not a number, it is a flag on a named Respondent. This is the decision the whole ticket turns on: cost drops from +28 items to a handful, and `rubric/dimension-levels.md` keeps meaning what it says.
- **Q2 → A, concrete scenario** — a named action with a named condition, drawn from work this team does. It also fixes the boundary with **#19**: the probe states *one* condition inside the sentence; #19 decides whether the survey separately asks *which* conditions move someone.
- **Q3 → A + C.** No probe rows on the Coverage grid — level **6 (System-verified)** already is one, 19 times over, free. And because Q1 landed on the marker reading, the C follow-on is live: a level-6 selection surfaces in the dashboard the same way a probe endorsement does. **New constraint on the map** — #12 (scored CSV) and #16 (dashboard) must both carry non-scoring edge flags, not just scores. I'll record that when I close this ticket.

**What that leaves**

Round 1 killed the expensive branch, so the remaining questions are all about placement and plumbing: which Dimensions are worth a marker, which section they sit in, what scale they wear, how loud the grid flag is, and whether Probe and Conditional are one thing or two.

One thing round 1 changed that isn't obvious: a marker-only probe has **no measurement obligation**. It doesn't need to be balanced, it doesn't need a matching item at the other pole, and it doesn't need to exist for every Dimension. That frees Q4 completely — the only test a probe has to pass now is *"does this edge position change what the team can plan for?"*

---

## Q4 — Which Dimensions carry a probe, and at which pole?

### What this is

There are seven Dimensions. A marker earns its place only where an edge position is a **constraint on the six-month plan** — someone whose answer means the team cannot simply decide to move.

### Why it matters

Run each Dimension against that test:

| Dimension | Pole | The edge position | Constrains the plan? |
|---|---|---|---|
| **Comfort** | low | Would rather not use AI at all | **Yes** — a hard floor no plan can vote away |
| **Trust** | high | Would ship code they hadn't read | **Yes** — the ceiling the team is arguing about |
| **Autonomy** | high | Would let an agent run unsupervised | **Yes** — distinct from Trust: about the leash, not the output |
| **Concern** | high | Thinks there is work AI should be banned from | **Yes** — names a boundary the plan must respect |
| **Craft values** | high | Nothing ships under their name they can't explain | **Yes** — the deepest one; it drives the other four |
| **Fluency** | either | Expert, or has never used an agent | **No** — an expert is a *resource*, not a constraint, and the low end is already visible in the Context tools matrix and the grid |
| **Guardrails** | either | Wants nothing / wants CI-enforced gates | **No** — its two edges are literally rubric levels 1 and 5, and "there is work AI should be banned from" is already the Concern probe |

That's five. Note Trust and Autonomy stay **separate** — merging them into one scenario would save an item but produce an ambiguous flag, and the flag is the entire output.

### Options

| Option | Pros | Cons |
|---|---|---|
| **A. Five** — Comfort (low), Trust (high), Autonomy (high), Concern (high), Craft values (high) | Every probe passes the constrains-the-plan test. Five items is a rounding error against 28–42. Covers both the refuseniks and the accelerators. | Fluency and Guardrails get no marker; if someone's edge lives there it won't be visible except through their scores. |
| **B. Three** — only the hard blocks: Comfort (low), Trust (high), Craft values (high) | Leanest. Three quotable sentences is already more than the room can work through in one sitting. | Loses Autonomy, which is the Dimension the six-month plan is most actually *about*. Loses the ban-it boundary. |
| **C. All seven, one each** | Uniform rule, nothing to justify per Dimension, trivially explained in the rubric. | Two of them are markers for edges nobody needs to plan around. A flag that fires on something unremarkable makes every other flag quieter. |
| **D. Five, plus a second pole on Trust and Autonomy** | Catches the accelerator *and* the refusenik on the two most contested Dimensions. | Back to nine items, and the low poles of Trust and Autonomy are the team's status quo — nearly everyone endorses them, so they'd flag most of the team and mark nothing. |

### My recommendation

**A — five probes, one pole each.**

The pattern worth noticing: four of the five sit at the **high** pole and only Comfort sits low. That's not an oversight — the team's current position *is* the low end, so a low-pole probe mostly measures "normal". Comfort is the exception because refusing AI outright is genuinely rare and genuinely blocking.

### Your answer

: I like your recommendation. Let's go with it. 

<!-- If you'd cut one of the five, which? If you'd add Fluency or Guardrails back, what edge are you picturing? -->


---

## Q5 — Which section do probes live in: Current, Future, or both?

### What this is

The survey has a Current-state section (Never…Always / Not at all…Completely) and a Future-state section (Definitely not…Definitely, answered twice — **For me** and **For the team**). A probe has to live in one or both.

### Why it matters

There's an asymmetry here that only shows up once you picture the actual answers.

**A Current probe on this team probably returns all 1s.** "I ship code I haven't read" — on a team that hasn't got there yet, everyone answers Never, no flag fires, and five items produced nothing. The extremity that makes a probe useful is exactly what makes it dead on arrival in the present tense.

**A Future probe discriminates.** "In six months, I would be fine shipping code I hadn't read, if the tests pass" is a live question with real disagreement behind it — which is the definition of a good marker. And it comes with **both stances free**: one item, two rows, and you learn separately whether someone would do it themselves and whether they think the team should. *"I'd go there, but I don't think we should"* is precisely the sentence the map says the stance split exists to surface.

The counter is real though: the shocking present-tense admission is the more powerful artifact in a room, and an all-1s floor is itself a finding — *"nobody here is doing this yet"* is worth knowing before you plan to move.

### Options

| Option | Pros | Cons |
|---|---|---|
| **A. Future only, both stances** | 5 items. Lands where disagreement actually lives. Gets the Personal-vs-Team split for free. Puts the marker where the plan is made. | No present-tense record; if someone *is* already doing the extreme thing, you find out from their Autonomy score rather than from their own words. |
| **B. Current only** | Produces the quotable admission. Cheapest to word — it's a plain statement about today. | Likely all 1s on a team not there yet: five items, zero flags. No stance split. |
| **C. Both** | Full picture — who's already there *and* who's willing to go. The Current→Future move on a probe is itself a strong signal. | 10 items and the Current half is the half likely to return nothing. |

### My recommendation

**A — Future-state only, both stances.**

It's the one option where every item is guaranteed to produce information. Worth flagging: the Craft values probe reads a little awkwardly in future tense (*"in six months I'd be fine shipping code under my name I couldn't explain"*) — that's a wording problem for the item bank (#6), not a reason to reject the rule.

### Your answer

: I like your recommendation. Let's go with it. 

<!-- If you want C, which probes are worth asking in the present tense? -->


---

## Q6 — Does a probe wear the same scale as its neighbours, or a sharper one?

### What this is

Whether a Respondent can *tell* they're answering a probe.

### Why it matters

The map's constraint is gut reaction, and nothing that invites a long, thought-out answer. A visibly special question does the opposite: a lone yes/no in a block of Likert rows announces *this one matters*, and people stop answering and start positioning — which is exactly the self-image problem Q2 rejected abstract phrasing to avoid.

Keeping the same scale also has a payoff beyond camouflage: a 1–5 answer gives the marker a **degree** for free. A 5 is a louder flag than a 4, and "two people at 5, one at 4" is a more useful sentence than "three people said yes".

Against that: a five-point scale on a deliberately extreme statement invites a 3, and "Unsure" on *"I'd ship code I haven't read"* is not really a position. A binary forces the commitment that makes a marker a marker.

### Options

| Option | Pros | Cons |
|---|---|---|
| **A. Same Desirability scale, same block** | Invisible to the Respondent. Zero extra work in Forms. Gives the flag a degree. Nothing to explain in the rubric. | The middle of the scale is a hiding place; some real edges answer 3 and never fire. |
| **B. Binary yes/no** | Forces commitment. A clean, unarguable flag. | Announces itself. Breaks the Likert block layout in Forms. Loses the degree. |
| **C. Same scale, but its own block** | Some separation without changing the scale. | Worst of both — still announces itself, still has a middle. |

### My recommendation

**A**, with the flag firing at **4 or 5**.

The hiding-place objection is real but it fails safe: a 3 on an extreme statement isn't a missed edge, it's someone who genuinely isn't at the edge. A marker that only fires on 4–5 is doing its job.

### Your answer

: Yeah, let's go with the same desirability and Same block. 

<!-- Comfortable with 4–5 as the threshold, or should only a 5 fire it? -->


---

## Q7 — The level-6 grid flag: every Development area, or a named few?

### What this is

Q3's C follow-on. A Respondent choosing **6 — System-verified** on a grid row becomes an edge marker. There are 19 rows and this decides how many of them can fire.

### Why it matters

You didn't answer the prompt on Q3 — *"are there Development areas where a 6 would genuinely alarm you?"* — so here it is properly.

A 6 on **Meeting notes** is unremarkable; that's a sensible place to let a tool run end-to-end. A 6 on **Security review** is a position somebody needs to defend out loud. If every row can fire, the unremarkable sixes drown the alarming ones, and a flag that fires often stops being read — the same failure mode as a noisy CI check.

Against that: a curated list is a judgement you're baking into the instrument, and it will be wrong for someone. It also has to be maintained if the area list ever changes.

### Options

| Option | Pros | Cons |
|---|---|---|
| **A. Every area** | No list to argue about or maintain. Nothing is pre-judged. | Noisy. A 6 on Meeting notes reads the same as a 6 on Incident response. |
| **B. A named subset** — high-stakes areas only | Every flag that fires is worth a conversation. Small list, easy to state in the rubric. | You're deciding in advance which sixes matter. |
| **C. Every area, ranked by stakes in the dashboard** | Nothing hidden, signal still ordered. | Pushes the judgement into #16 instead of removing it, and the ranking is the same list as B with extra steps. |

### My recommendation

**B**, with this starting list — trim it:

- Security review / threat modeling
- Incident response / on-call
- Code review
- SQL / data migrations
- Infrastructure-as-code
- CI/CD & build config

Roughly: the areas where an undetected error is expensive or hard to reverse. **Debugging**, **Writing production code** and **Dependency upgrades** are the borderline ones I left off.

### Your answer

: Yeah, let's go with the named sub-subset. 

<!-- Cut or add freely — this is the list only you can get right. -->


---

## Q8 — Probe and Conditional (#19): two classes, or one mechanism?

### What this is

The ticket asks you to confirm Probe items and Conditional items stay separate. Round 1 made this sharper than the ticket expected: now that a probe **doesn't score**, both classes are non-scoring things that sit beside a Dimension score. They look structurally identical.

### Why it matters

They answer different questions. A **Probe** locates someone at an *extreme* — *"I'd ship code I haven't read."* A **Conditional** locates the *boundary and what moves it* — *"I wouldn't, unless a schema check validated it, and I didn't know that was an option."* Same person, two different facts, and only the second one tells you whether an edge is a principle or a training gap.

But structurally they're the same shape: a non-scoring answer, attached to a Dimension, that produces a per-Respondent attribute rather than a number. That matters because **#12** (scored CSV) and **#16** (dashboard) have to carry them, and building two mechanisms for one shape is the kind of thing that gets regretted at #15.

Worth being explicit: **#19 is blocked by this ticket**, so whatever you answer here is the ground it starts from.

### Options

| Option | Pros | Cons |
|---|---|---|
| **A. Two classes, one mechanism** — distinct names and purposes in `CONTEXT.md`, one shared flag/attribute column family in the scored CSV | Keeps the glossary honest about what each measures. #12 and #16 build one thing. #19 inherits a working mechanism instead of inventing one. | The glossary has to state the distinction clearly enough that item writers don't blur them.
| **B. One class** — collapse both into "Marker item" | Simplest possible glossary and schema. | Loses the distinction that #19 exists to create. Merging the two makes "hard no on principle" and "hard no from not knowing" indistinguishable again — the exact bug #19 was filed against. |
| **C. Two classes, two mechanisms** | Each can evolve independently; #19 is unconstrained by this ticket. | Two schemas and two dashboard treatments for one shape. #19 is blocked by this ticket precisely so it *doesn't* have to start from scratch. |

### My recommendation

**A.** Confirm them as separate classes in `CONTEXT.md`, and note explicitly that they share a mechanism — a per-Respondent, non-scoring attribute — so #12 designs the column family once.

### Your answer

: Let's go with your recommendation here. 

<!-- Does the Probe / Conditional distinction hold for you, or does it feel like one idea split in two? -->


---

## Anything else — round 2

<!-- Free space: constraints, objections, things these five questions missed. -->


---
---

# Round 3 — the last three, then I write it up

**What round 2 settled**

- **Q4 → five probes**, one pole each: **Comfort** (low), **Trust** (high), **Autonomy** (high), **Concern** (high), **Craft values** (high). Fluency and Guardrails carry none.
- **Q5 → Future-state only, both stances.** Five items, each answered twice (*For me* / *For the team*).
- **Q6 → same Desirability scale, same block.** A probe is indistinguishable from its neighbours; the flag fires at **4 or 5**.
- **Q7 → named subset** for the level-6 grid flag, list as drafted: Security review / threat modeling · Incident response / on-call · Code review · SQL / data migrations · Infrastructure-as-code · CI/CD & build config. (Debugging, Writing production code and Dependency upgrades stay off.)
- **Q8 → two classes, one mechanism.** Probe and Conditional stay distinct in `CONTEXT.md` and share one non-scoring per-Respondent attribute in the scored CSV.

**Why there's a round 3 at all**

Q5 and Q6 together produced something neither question asked about. A Future probe has **two rows**, and the flag threshold is a single number — so there are now two places a flag can fire per probe, and nothing has said which one counts. That's Q9, and it's the most interesting thing left.

The other two are the loose ends that stop the item bank (#6) and the CSV (#12) from having to guess: the direction rule every probe is worded against, and what this thing is actually *called* in the deliverables.

After these three I believe the frontier is empty and I'll write the resolution.

---

## Q9 — Which stance row fires the flag?

### What this is

Every Future item is answered twice: **For me** ("in 6 months I would…") and **For the team** ("in 6 months the team should…"). A probe endorsed at 4–5 could fire on either row, and they mean different things.

### Why it matters

Four combinations, and three of them are worth a sentence in the room:

| For me | For the team | What it says |
|---|---|---|
| 4–5 | 4–5 | **Accelerator.** Would go there and thinks the team should. The clearest push signal in the survey. |
| 4–5 | 1–3 | **"I'd go, but we shouldn't."** Someone who trusts their own judgement at the edge and doesn't want it as a norm. The map explicitly says the stance split exists to surface exactly this. |
| 1–3 | 4–5 | **"The team should, but not me."** Rarer and stranger — usually means *"this is where the industry is going and I'm not ready"*. Worth knowing before you plan training. |
| 1–3 | 1–3 | No flag. |

The cost of tracking both is genuinely zero: the two answers already exist in the export, and the Scoring sheet is reading that row anyway. The only real question is whether the *dashboard* has to render three states or one, which is a small amount of work in #16 in exchange for the survey's sharpest output.

The argument for one row: three flag states per probe × five probes is 15 things a reader has to hold, and the one-pager (#17) has to explain it. A single flag is easier to read and harder to misread.

### Options

| Option | Pros | Cons |
|---|---|---|
| **A. Track both rows separately** — a personal flag and a team flag per probe | Free from the data you already have. Surfaces the divergence the map names as a goal. Distinguishes an accelerator from a lone maverick — a real difference for planning. | Three states to render in #16 and explain in #17. |
| **B. Personal row only** | Simplest. "Would *you* do this" is the most honest read of an edge position. | Throws away the divergence for nothing — the team-row answer is already collected either way. |
| **C. Team row only** | Most directly about the six-month plan, which is what the team is deciding. | Loses the person. A probe's whole output is a named individual owning a sentence. |
| **D. Either row fires one combined flag** | One state to render. Any edge shows up. | Merges the accelerator and the maverick into one dot — the exact conflation the stance split was introduced to prevent. |

### My recommendation

**A.**

The data is already there; refusing to look at it is the only expensive option. And the divergence case is the one the map singles out — *"I'd go further, but I don't think we should"* is written into `CONTEXT.md`'s definition of Stance. A probe is the item most likely to produce it.

### Your answer

: I like your recommendation here. We should track both separately. 

<!-- If A feels like too much for the dashboard, D is the honest fallback — say so. -->


---

## Q10 — Is every probe worded so that "Definitely" is the edge?

### What this is

The Desirability scale runs **1 Definitely not → 5 Definitely**. Four of the five probes sit at their Dimension's high pole, so "Definitely" is naturally the edge. **Comfort's probe sits at the low pole** — the refusenik — and that breaks the pattern unless the wording flips it.

Compare the two ways to write the Comfort probe:

- **Pole-faithful:** *"In six months I would be using AI on most of my work"* → the edge fires at **1–2**.
- **Direction-normalised:** *"In six months I would be fine with AI having no place in my work"* → the edge fires at **4–5**, like every other probe.

### Why it matters

This is a one-line rule that either does or doesn't create a lookup table.

If probes point in different directions, the Scoring sheet needs a per-probe direction column, the dashboard needs to know which way each one reads, and #17 has to explain why one flag means agreement and another means refusal. Every one of those is a place to get it wrong silently — and this is Excel, formulas only, so a lookup table is a real cost.

If every probe is normalised so **"Definitely" = the edge**, there is exactly one rule — *fires at 4 or 5* — and nothing to look up anywhere.

The cost of normalising: the Comfort probe reads as a slightly odd sentence, and it's the one probe where endorsing it means *less* AI rather than more. A reader skimming the flag list sees five flags that look alike but one points the other way.

Note this is **not** reverse-keying. Reverse-keying (`6 − answer`) is a scoring operation and probes don't score — so probes are never reverse-keyed, and a probe can't satisfy a Dimension's "at least one reverse-keyed item" requirement. That requirement still falls entirely on the ordinary items, which is a constraint on #6.

### Options

| Option | Pros | Cons |
|---|---|---|
| **A. Normalise — "Definitely" is always the edge** | One threshold rule, no direction column, nothing to look up in Excel or the dashboard. | The Comfort probe is an awkward sentence, and one of five flags means the opposite direction of travel. |
| **B. Pole-faithful — each probe points its natural way** | Every probe reads as the most natural sentence. Comfort's probe stays positively worded. | Needs a per-probe direction column in the Scoring sheet, the dashboard and the one-pager. One lookup table for one item. |
| **C. Normalise, and drop the Comfort probe** | Removes the exception entirely. Four probes, one rule, no awkward sentence. | Loses the refusenik marker — the one edge Q4 identified as a *hard floor no plan can vote away*. |

### My recommendation

**A** — normalise, and accept the awkward sentence. It's one item, and the wording is #6's problem to polish; a direction column is everyone else's problem forever.

### Your answer

: I like your recommendation here. 

<!-- If A: happy for the Comfort probe to be worded as "I'd be fine with AI having no place in my work"? -->


---

## Q11 — What is this flag called?

### What this is

The term that goes in `CONTEXT.md` and then propagates into the Scoring sheet (#15), the dashboard (#16) and the one-page how-to-read (#17). Naming it is the last thing this ticket owes the map.

### Why it matters

The term has to cover **two sources**, because Q3 made them one treatment:

1. A probe endorsed at 4–5 (either stance row).
2. A level-6 selection on one of the six named high-stakes Development areas.

Anything named after probes specifically ("probe endorsement", "probe flag") forces a second term for the grid case and then a third umbrella term to talk about both — three words for one idea.

There's a second pull: Q8 said Probe and Conditional share a *mechanism*. It's tempting to name the mechanism and let both classes use it. But a Conditional answer isn't an edge — it's a **boundary and what moves it** — so an "edge"-flavoured umbrella would fit it badly. Naming and mechanism don't have to be 1:1: #12 can build one column family while the glossary keeps separate words for what lands in it.

### Options

| Option | Pros | Cons |
|---|---|---|
| **A. Edge flag** — source-agnostic; a probe endorsement or a high-stakes level 6 both raise one | One word covers both sources. Says plainly what it does. Leaves #19 free to name its own thing. | Slightly generic; "flag" carries a faint whiff of *something is wrong*, and an edge position isn't wrong. |
| **B. Edge marker** | Same coverage, and "marker" is neutral — it locates rather than warns. Matches the Q1 language this whole design came out of. | Marginally softer; a reader may not register it as something to act on. |
| **C. Probe endorsement** | Precise about the main source. | Doesn't cover the grid case; forces a second and third term. |

### My recommendation

**B — Edge marker.**

"Flag" implies a problem, and the whole point of round 1 was that an edge position is *information for the room*, not a fault. Someone who'd ship unread isn't misbehaving — they're the person the six-month plan has to be built with. **Edge marker** also reads correctly on the grid case, where "flag" would make a level-6 selection sound like an accusation.

### Your answer

: I like your recommendation here. 

<!-- Or give it your own name — this is the one that ends up in front of your manager. -->


---

## Anything else — round 3

<!-- Last call: anything this ticket has silently assumed that you'd want on the record? -->


---
