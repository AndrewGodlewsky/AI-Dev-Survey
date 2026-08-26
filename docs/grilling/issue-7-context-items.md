# Grilling — Issue #7: Context items

**Ticket:** [Context items: which Respondent attributes to collect](https://github.com/AndrewGodlewsky/AI-Dev-Survey/issues/7)
**Round:** 1 of ? — prerequisites
**How to use:** answer inline under each `### Your answer` heading. Free text is fine; you don't have to pick one of the listed options. Then tell me it's ready and I'll read it back and compute the next round.

---

## Why this round is only three questions

The ticket already proposes a list (role, years of experience, AI tools used, hours per week). I'm not asking about that list yet, because two facts decide whether any of it survives:

1. **The roster-join test.** Anything the org already knows — who does what job, how long they've been here — can be attached to the scored CSV *after* the fact, by you, in about 30 seconds. Survey time is the scarce resource on a 35–40 minute instrument. Re-collecting a known fact spends a Respondent's attention to buy something you already own.
2. **The small-n problem.** `CONTEXT.md` defines a Context item as unscored *and* something that "becomes an extra Slice". With 5–9 named Respondents, a Slice by role is a bucket of two people. A two-person bucket has no mean worth reporting and no spread worth reading. If slicing is genuinely the job, most of the recommended list can't do it — so the job may need redefining before the list is picked.

Both tests need facts only you have. Hence: prerequisites first.

---

## Q1 — Team composition

### What this is

Whether the 5–9 people taking the survey all do the same job, or span disciplines (QA, DevOps/platform, data, design, product).

### Why it matters

The Coverage grid has **19 Development areas** and an **N/A** escape meaning "I don't do this work". A non-developer will N/A out large blocks of it. When the dashboard shows a Coverage profile full of holes, the reader needs to know whether that's *"this person doesn't use AI here"* or *"this person doesn't do this at all"* — those are opposite findings, and only role separates them.

So role isn't competing on the "is it interesting?" axis. It's competing on "does it make the Coverage grid legible or not?" On a uniform team it's decoration. On a mixed team it's the key to the largest artifact in the survey.

### Options

| Option | Pros | Cons |
|---|---|---|
| **A. Uniform team** — everyone is a developer | Role adds nothing; drop it, save the question. N/A patterns are directly comparable person-to-person. | If it's *nearly* uniform (one QA), you lose the one distinction that explains the odd profile. |
| **B. Mixed team** — 2+ disciplines | Role becomes the item that makes Coverage readable. Justifies its place on merit, not convention. | Needs a closed list matching *your actual team*, not a generic taxonomy — a generic list invites people to pick a label that doesn't describe them. |
| **C. Mixed, but you'll label the CSV yourself** | Zero survey cost; you know everyone's role anyway. | The dashboard needs the role column to exist somewhere; you're committing to hand-maintaining it. Fine for one run, annoying at the Horizon. |

### My recommendation

**B**, if the team is genuinely mixed — with the answer options written as your real job titles (5 or fewer), not an industry taxonomy.

### Your answer

: Option A

<!-- Roughly who's on the team? e.g. "6 devs + 1 QA + 1 platform" -->


---

## Q2 — Who reads the results, and when

### What this is

The audience for the dashboard and the one-page "how to read the results". Specifically: does every reader already know the team?

### Why it matters

This is what decides whether the roster-join test above is *actually* free. Roster-lookup costs nothing while the reader has the roster in their head. It costs everything when they don't — and "future you" is one of the readers who won't.

Named responses make this sharper than it looks. If the audience is only the room, the survey can lean on shared knowledge and stay short. If it's ever read cold, every unexplained column becomes a question nobody can answer, and the results quietly stop being usable.

### Options

| Option | Pros | Cons |
|---|---|---|
| **A. The room only** — the 5–9 people, at one readout | Shortest possible survey. Any missing context gets supplied out loud on the day. | The artifact has a shelf life measured in hours. Re-reading it in six months, you'll have forgotten who was who. |
| **B. The room + you at the Horizon** | Only needs the roster written down *once*, next to the scored CSV — not asked of nine people. | Requires the discipline to actually write it down. Easy to skip and then regret. |
| **C. Wider** — a manager, a joiner, an archive | Forces the survey to be self-describing, which is genuinely more robust. | Pushes toward collecting demographics in-survey, which costs time and, on a named survey, changes the social feel of the instrument. |

### My recommendation

**B.** It gets durability without spending survey time — the roster becomes one small file you write by hand, not four questions × nine people.

### Your answer
: I want the results to be available to everyone who's taking the survey, but then the combined results to be available to me, which also might mean that I need the individual results as well. This is not something that's going to go to a manager, or at least none of the individual results will go to a manager. Only our combined team view would be something he would be able to see. 
<!-- Who sees this, and do you expect to re-read it at the 6-month Horizon? -->


---

## Q3 — Is current AI tool usage already recorded anywhere?

### What this is

Whether the org already knows which AI tools people use — licence/seat assignments (Copilot, Cursor, Claude), an expenses line, IDE telemetry, an admin console.

### Why it matters

Of the four items the ticket proposes, "which AI tools have you used in the last month" is the only one that plausibly *can't* be looked up. If it can, the entire recommended list fails the roster-join test and the honest answer to this ticket becomes "collect nothing, or nearly nothing".

There's a distinction worth holding onto: **a seat says who is licensed, not who opens the thing.** Those diverge a lot — teams routinely have licences sitting unopened. If that's the situation here, the item survives but should be reworded to ask about *use*, not *access*, because access is the part you can already look up.

### Options

| Option | Pros | Cons |
|---|---|---|
| **A. Nothing is recorded** | The item is clearly justified. Ask it, multi-select, and it becomes the strongest Context item on the list. | Multi-select options need maintaining — a tool list goes stale fast. |
| **B. Seats are visible, real usage isn't** | Keep the item but reword it to *use* ("used at least weekly in the last month"), which is the part that's genuinely unknown. Seat data can be joined separately if wanted. | "Used" is fuzzy. Needs a frequency floor in the wording or people interpret it differently. |
| **C. Usage telemetry exists** | Drop the item entirely — measured data beats self-report, which is biased in a *named* survey where people know their answer is visible to colleagues. | You'd be relying on data that may not be exportable in a form the Scoring sheet can use. |

### My recommendation

**B**, which I'd guess is the reality. Reword the item to ask about use with an explicit frequency floor.

### Your answer
: We currently have a number of tools available to us, including GitHub Copilot and Copilot Studio and M365 and Azure Foundry. 
<!-- Do you have seat/licence visibility? Any actual usage telemetry? -->


---

## Anything else

<!-- Free space: constraints, objections, things these three questions missed. -->


---
---

# Round 2 — the list itself

**What round 1 settled**

- **Q1 → A, uniform team.** Everyone is a developer. *Role* is dropped: it would be decoration, and the Coverage grid's N/A pattern is now directly comparable person-to-person without it. If someone N/As out "Incident response", that's a real signal about them, not an artefact of their job title.
- **Q2 → layered audience.** Individual results are visible to everyone who took the survey. The combined team view additionally goes to your manager; individual results never do. This is a **new constraint on the map** — the dashboard (#16) and the one-page how-to-read (#17) now have a hard "team-only export" requirement. I'll record that when I close this ticket.
- **Q3 → org-provided estate**, listed as GitHub Copilot, Copilot Studio, M365 (Copilot), Azure AI Foundry. You didn't say whether *usage* is measured, so I'm assuming seats are visible and real usage isn't. Q7 below gives you a place to correct that.

**What this does to the ticket's recommended list**

The ticket proposed: role, years of experience, AI tools used, hours per week. Role is now gone. The remaining three are what round 2 decides — plus one candidate the ticket missed, which I think is stronger than anything on it.

There's a new cost to weigh that round 1 didn't have. Because individual results are visible to the whole team, **every Context item is a public statement about that person**. An unscored demographic question stops being neutral when its answer is shown next to your name to the people you work with. That's not a reason to collect nothing — it's a reason each item has to be worth being seen answering.

---

## Q4 — Years of professional experience: keep or drop?

### What this is

The ticket's "years of professional experience" item, on a team where you already know everyone.

### Why it matters

It's the last survivor of the roster-joinable group, and it has a real argument behind it: experience plausibly correlates with **Craft values** and **Concern** — the "understanding every line" instinct and the skill-atrophy worry both tend to track how long someone has been doing this. If that correlation is what you want to look at, you need the number in the data.

But you can supply it yourself, once, in a roster file, at zero cost to nine people's attention. The question is whether it's worth a survey slot given that.

There's also the visibility cost. On a small named team, tenure is a status marker. Publishing "3 years" next to a name, beside that person's Trust and Fluency scores, invites a reading nobody asked for: *of course they scored low, they're junior*. That reading is exactly the kind of thing that makes people answer a survey carefully rather than honestly.

### Options

| Option | Pros | Cons |
|---|---|---|
| **A. Drop it; put it in the roster file instead** | Zero survey cost. You keep the analytical option — the column still exists for the dashboard. Nothing new is published next to anyone's name. | You have to actually write the roster file. One more hand-maintained thing. |
| **B. Keep it as a banded question** (0–2 / 3–5 / 6–10 / 10+) | Self-reported, no maintenance. Bands blunt the status-marker problem a bit. | Still spends a slot on a fact you know. Still visible to the team. |
| **C. Drop it entirely, don't record it anywhere** | Simplest. Removes the "of course they're junior" reading from the room completely. | Loses the Craft-values / Concern correlation permanently. Can't be recovered later. |

### My recommendation

**A.** The analysis stays possible, the survey stays shorter, and nothing is published that wasn't already known. The roster file is one line per person, and it's the same file Q2's answer already implies you need.

### Your answer

: I don't think we need to keep this anywhere. We're not particularly worried about the experience difference because ultimately we are a team and we are going to act as such. 

---

## Q5 — AI tenure: how long they have been using AI tools at all

### What this is

A **new** candidate, not on the ticket's list: *"Roughly how long have you been using AI tools in your development work?"* — never / under 3 months / 3–12 months / 1–2 years / 2+ years.

### Why it matters

This is the one attribute that is genuinely unknown, genuinely varies on a uniform team, and genuinely changes how every other answer reads.

Consider two people who both score **Fluency 2**. One started last month; one has been at it two years. The first is on a normal learning curve. The second has hit a wall, or tried it and disengaged. Those demand opposite responses from the team, and no other item in the survey distinguishes them — Fluency measures skill, not exposure. Without AI tenure, the dashboard shows you a number with two incompatible meanings.

It also does real work on **Gap**. A large positive Gap from someone three months in is enthusiasm. The same Gap from someone two years in is a considered judgment about where they want to get to. Same number, different weight.

Unlike career tenure, it isn't roster-joinable — you would be guessing — and it carries much less social load, because "I started recently" isn't a status claim.

### Options

| Option | Pros | Cons |
|---|---|---|
| **A. Add it, banded** | Cheap (one question), unknown, high interpretive value, low social cost. Makes Fluency and Gap legible. | It's scope the ticket didn't ask for. One more item on a 35–40 minute instrument. |
| **B. Skip it — Fluency already covers this** | Shorter survey. Arguably exposure shows up in the Fluency score anyway. | It doesn't: Fluency is a *skill* Dimension. Conflating skill with exposure is precisely the ambiguity above. |
| **C. Add it as a scored input to Fluency** | Uses the data actively rather than descriptively. | Breaks the glossary — Context items are unscored by definition — and exposure is not skill. Wrong lever. |

### My recommendation

**A.** If only one Context item survives this ticket, I think it should be this one. It's the only candidate that tells you something you can't otherwise get *and* changes how you read the rest of the results.

### Your answer

: I don't think we really need to keep this question at all. I think we can skip it. I think fluency generally covers this, and we're not trying to determine how good someone is by how long they've been doing AI. That's a fundamentally flawed approach. 

---

## Q6 — AI tools used: keep it, and what goes in the option list?

### What this is

The multi-select. Your estate is GitHub Copilot, Copilot Studio, M365 Copilot, Azure AI Foundry. The live question is whether the list stops there.

### Why it matters

A short, fixed, org-provided list is cheap to ask and cheap to maintain — my round-1 worry about staleness doesn't apply here. So the item survives on cost. The question is what it's *for*, and there are two different jobs hiding inside it:

1. **"Which of the things we pay for do people actually open?"** — a licensing and enablement question, answerable with the four options above.
2. **"What is this team actually using to do its work?"** — the truthful picture, which on most teams includes something outside the sanctioned list: a personal ChatGPT, Claude, a local model, a browser extension.

Job 2 is much more useful and much more dangerous. **Results are named and shared openly, and a team view goes to your manager.** Asking people to declare unsanctioned tool use, under their own name, in a document a version of which their manager will see, is asking them to either under-report or expose themselves. Under-reporting does not stay contained — someone who shades one answer is primed to shade the next, and Trust and Autonomy are where you least want that.

The honest resolutions: ask only about sanctioned tools and accept an incomplete picture, or include an "other" option worded so that ticking it isn't a confession.

### Options

| Option | Pros | Cons |
|---|---|---|
| **A. Sanctioned four only** | Zero social hazard. Directly answers the licensing question. Stable list. | You will not learn what people actually use. If shadow usage is significant, the survey describes the wrong tool landscape. |
| **B. Sanctioned four + a neutral "another tool not on this list"** (no free-text naming it) | Measures *whether* there's shadow usage without making anyone name it. Free-text is already ruled out by the map, so this fits. | You learn it exists, not what it is. Some people still won't tick it. |
| **C. Full honest list including named third-party tools** | The truthful picture, if you actually get it. | Highest hazard given named plus manager-visible results. Risks contaminating answers elsewhere in the survey. |
| **D. Drop the item; read seat data instead** | No survey cost. Seat data is objective. | Seats measure access, not use — the exact thing you want to know. |

### My recommendation

**B.** It gets the licensing answer *and* a signal on whether the sanctioned estate is the whole story, without asking anyone to incriminate themselves by name. Worth pairing with a line in the survey preamble saying the tools question is about enablement, not compliance — that sentence does most of the work.

### Your answer

: I think we can go with option B. The main thing that I'm trying to figure out here is not what they've used as a history. It's just which parts of AI are they more comfortable with? To think of it a different way, you use GitHub Co-Pilot and Azure Foundry for completely different tasks, and they're used in different ways. Their perspective might be shaped based on the tools that they're currently using. 

---

## Q7 — Volume of use: keep, and in what shape?

### What this is

The ticket's "hours per week currently using AI tools", and whether it survives in that form.

### Why it matters

This is the one item where the manager-facing team view genuinely needs something the scored Dimensions don't provide. "The team averages 6 hours a week with AI" is a sentence a manager understands immediately; "the team's mean Comfort is 3.4" is not. Q2's answer therefore *strengthens* the case for a volume item — it's the descriptive headline that makes the team view readable to someone outside the team.

The problem is the unit. Self-reported hours-per-week is notoriously bad data: people can't separate "time with the tool open" from "time actively prompting", and the number is inflated by an assistant that is simply always running. Two people doing identical work can report 2 and 20.

A frequency scale sidesteps the estimation entirely, and matches the scale vocabulary already decided in #2 for behaviour items (Never … Always) — one less scale for a Respondent to learn.

The visibility cost is real here too: a low number, published under your name, reads as *not on board*. Banding blunts that; a raw number doesn't.

### Options

| Option | Pros | Cons |
|---|---|---|
| **A. Banded hours/week** (none / under 2 / 2–5 / 5–10 / 10+) | Gives the manager view a concrete headline number. Bands soften the exposure. | Still asks for an estimate people can't make reliably. Ambiguous unit. |
| **B. Frequency instead** — "How often do you use an AI tool in your development work?" on the Never…Always scale from #2 | No estimation required. Reuses a scale already in the survey. Much more reliable data. | No hours headline. "Often" is less legible to a manager than "6 hours". |
| **C. Both** | Covers the headline and the reliable measure. | Two items for one construct, on an instrument you're already trying to keep under 40 minutes. |
| **D. Drop it** | Shortest. Arguably the Coverage grid already shows breadth of use. | Coverage shows *where* AI is used, never *how much*. The team view loses its plain-English headline. |

### My recommendation

**B**, accepting that you would describe the team to your manager in frequencies rather than hours. If that trade doesn't sit right, **A** — but band it, and never publish a raw number.

**Also, briefly:** does Copilot admin give you actual usage telemetry (active users, suggestions accepted)? If it does, that beats any self-report and this item can lean lighter or drop entirely. Round 1's Q3 didn't quite land on this.

### Your answer

: Yeah, I think we can do frequency. Ultimately, what my goal is here is to figure out what their intuition is about when they would choose to use an AI tool versus code it or do it themselves. I'm not really trying to figure out hours spent, because that metric doesn't mean anything useful. It's how often and when they are turning to AI alternatives naturally and natively. I would hope that the questions we ask can give us some of those insights. 

---

## Anything else — round 2


---
---

# Round 3 — two items left, and one of them is in the wrong place

**What round 2 settled**

- **Q4 → C.** Years of professional experience is dropped entirely and recorded nowhere — not in the survey, not in a roster file. Rationale: the team acts as a team; the experience difference isn't a lens you want applied to the results. This also retires the roster file that Q2's answer implied — with role and tenure both gone, there's nothing left for it to hold.
- **Q5 → B.** AI tenure is skipped. Rationale: tenure is a bad proxy for skill, and Fluency measures the thing directly. Fair — my argument was that tenure disambiguates a low Fluency score, and you've decided that disambiguation isn't worth a question. Noting it as a deliberate trade, not an oversight: a Fluency 2 will read the same whether the person started last month or two years ago.
- **Q6 → B.** Sanctioned four plus a neutral "another tool not on this list". **But with a reframe** — see Q8.
- **Q7 → B.** Frequency rather than hours. **But with a reframe that may undo the answer** — see Q9.

**Where the list stands**

Two items survive: **tools used** and **frequency of use**. That's well under the ≤5 the ticket allowed. Both of the remaining questions are about whether those two items actually do the job you described wanting from them — because in both cases your stated purpose and the item you picked are aimed at slightly different targets.

---

## Q8 — Does the tools item need a regularity floor?

### What this is

You reframed the purpose of the tools multi-select. Not *"what have you used"* as history, but:

> which parts of AI are they more comfortable with... you use GitHub Copilot and Azure Foundry for completely different tasks, and they're used in different ways. Their perspective might be shaped based on the tools they're currently using.

That's a better purpose than the one the ticket wrote down. But it changes what the item has to measure, and the plain multi-select doesn't quite measure it.

### Why it matters

"Have you used Azure AI Foundry?" and "has Azure AI Foundry shaped how you think about AI?" are different questions with different answers. Someone who opened Foundry once in a demo six months ago would tick the box, and their perspective is shaped by exactly none of it. Someone using Copilot's inline completion forty times a day has a deeply shaped perspective — and ticks the same kind of box, worth the same amount.

If the item is a lens for reading someone's Trust and Autonomy scores — *"of course they're cautious about agents, their only exposure is autocomplete"* — then a tick that can mean either "tried once" or "live in it daily" is a lens that doesn't focus. The fix is either a regularity floor in the wording, or a per-tool frequency instead of a per-tool tick.

The cost of the second option is real: the survey already carries one large grid (19 Development areas × Involvement level). A second grid, even a small 4–5 row one, adds fatigue at exactly the point where you want people still reading carefully.

### Options

| Option | Pros | Cons |
|---|---|---|
| **A. Plain multi-select, "which have you used"** | Cheapest. One question, four or five ticks. | Conflates "tried once" with "live in it daily" — the two things the lens most needs to separate. Weakest version of your stated purpose. |
| **B. Multi-select with a regularity floor** — "which do you use **at least weekly**" | Still one question, still ticks. The floor does most of the disambiguating work for free. | Loses the "tried it and stopped" signal, which is itself interesting. Weekly is an arbitrary line people will interpret loosely. |
| **C. Small per-tool frequency grid** — each tool on Never / Rarely / Monthly / Weekly / Daily | Directly measures "shaped by", which is what you actually want. Rich enough to read as a genuine profile. | A second grid. Adds 4–5 rows of grid fatigue before the big Coverage grid. Arguably over-precise for a lens you'll eyeball, not compute. |
| **D. Multi-select, but "which do you use most often" (pick up to 2)** | Forces the signal to the tools that actually shape perspective. Very cheap. | Loses breadth — you can't see who has tried everything versus who lives in one tool. |

### My recommendation

**B.** It's a one-word change from the answer you already gave, it costs nothing extra, and it converts the item from "history" to "current practice", which is the reframe you asked for. **C** is genuinely better data, but I don't think a second grid earns its fatigue cost for an item that will be read as a lens rather than computed.

Note that whichever you pick, the option list needs a **"none of these"** so the question can be required in Forms without forcing a false tick.

### Your answer

: I think it's fine to ask people what they've used, what they've tried, and maybe what they want to use going forward, which is based on how they see development working out. Again, just when we're developing these questions, the purpose isn't literally to figure out what they've used. It's just to help get some context and understanding that should show up in the metrics or results afterwards about how they might be trying to use AI within their day-to-day work. 

---

## Q9 — Should the frequency item exist at all, or is it a Dimension item in disguise?

### What this is

You picked frequency over hours, and gave this reason:

> what my goal is here is to figure out what their intuition is about when they would choose to use an AI tool versus code it or do it themselves... It's how often and *when* they are turning to AI alternatives naturally and natively.

I think that reason argues against the item you picked. Two problems, and they point in different directions.

### Why it matters

**Problem 1 — the item can't answer the question you asked of it.** You want to know *when* someone reaches for AI versus doing it themselves. A single "how often do you use AI tools" produces one number for a whole person. It cannot distinguish someone who uses AI constantly for tests and never for architecture from someone who spreads it evenly. But the survey already has an instrument for exactly that: the **Coverage grid** — an Involvement level for each of 19 Development areas, current and future. That grid *is* the "when and where" answer, at far higher resolution than any single frequency item. If the frequency item is meant to serve that purpose, it's a worse duplicate of something already in the survey.

**Problem 2 — it looks exactly like a scored item.** `CONTEXT.md` defines a **Behaviour item** as "a Current-state Dimension item about something the Respondent does; answered on a frequency scale (Never … Always)", and defines **Comfort** as "willingness to use AI in one's own development work". A Context item reading *"How often do you use an AI tool in your development work?"* on the Never…Always scale is a Comfort behaviour item by both definitions. Filing it under Context means an unscored question sitting adjacent to a scored twin, on the same scale, indistinguishable to the person answering — and a real risk that the Comfort item bank (#5) later drafts the same question again without noticing.

The two problems have different fixes. Problem 1 says drop it. Problem 2 says keep it but move it into the Current-state section as a scored Comfort item.

There's one thing that argues for keeping it as Context regardless: Q2's manager-facing team view. "Most of the team uses AI daily" is a sentence that travels outside the room. A mean Comfort of 3.4 doesn't. But a scored Comfort item can still produce that sentence — the score is derived from behaviour answers either way.

### Options

| Option | Pros | Cons |
|---|---|---|
| **A. Keep as an unscored Context item** | Gives the team view a plain-English headline. Simple, one question. | Duplicates a Comfort behaviour item on the same scale while being scored differently — confusing to answer, easy to double-draft in #5. Doesn't answer the "when" question. |
| **B. Drop it; hand the job to the Coverage grid** — and note it as a requirement on #5 that Comfort's behaviour items cover overall frequency | Removes the duplicate. The "when and where" question gets answered at 19× the resolution. Shortest survey. Context section reduces to one item. | The team view loses its single plain headline until the Coverage profile is summarised for it — a job that then falls to the dashboard (#16) or the one-pager (#17). |
| **C. Move it into the Current-state section as a scored Comfort behaviour item** | Resolves the disguise problem honestly — it *is* a behaviour item, so file it as one. Still yields a headline via the Comfort score. | Pushes a decision into #5's territory. Context section reduces to one item, which raises whether a one-item section is still a section. |
| **D. Keep both it and the Coverage grid, accept the overlap** | Belt and braces. Cheap redundancy can be a consistency check between the two. | Overlap without a stated rule for which wins when they disagree. Costs a question for redundancy you didn't ask for. |

### My recommendation

**B**, with the note carried onto #5 so the coverage isn't silently lost. Your actual goal — *when* do they reach for AI naturally — is the Coverage grid's entire job, and the grid answers it properly. Keeping a blunt single-number version alongside it buys a headline sentence you can generate from the results anyway.

If the headline matters more to you than the duplication bothers you, **C** is the honest second choice — but it makes this ticket resolve with a **single** Context item, which is worth saying out loud before you pick it.

### Your answer

: I think it's fine to go with your recommendation here. I think that makes sense. 

---

## Anything else — round 3


---
---

# Round 4 — the shape of the one surviving item

**What round 3 settled**

- **Q9 → B.** The frequency item is dropped. The "when do they reach for AI" job goes to the **Coverage grid**, which answers it across 19 Development areas instead of one number. A requirement gets carried onto the Current-state item bank (#5): Comfort's behaviour items must cover overall frequency of use, so the signal isn't silently lost. I'll record that on the ticket.
- **Q8 → neither A nor B.** You didn't take the regularity floor. You want *"what they've used, what they've tried, and maybe what they want to use going forward"*, with the purpose being context rather than precision — something that shows up when reading the metrics afterwards, not a measurement in its own right.

**Where that leaves things**

**The Context section is now one item: tools.** That's it. Role, career tenure, AI tenure and frequency are all gone. Given the ticket allowed up to five, it's worth registering that as a real outcome rather than an accident — the survey is shorter by four questions, and every one of them was cut for a stated reason.

But my Q8 recommendation was solving the wrong problem. I proposed a **weekly floor** to sharpen a blurry tick. You don't want a sharper cut-off — you want *more states per tool*: tried is not used, and want-to-use is neither. A multi-select tick carries exactly one bit per tool, so it cannot express three states. The item has to become a small grid, or it has to shed one of the states.

That's Q10. And "want to use going forward" raises a separate problem that Q9 just finished correcting in the other direction — that's Q11.

---

## Q10 — How many states per tool, and what are they called?

### What this is

Four or five tools (GitHub Copilot, Copilot Studio, M365 Copilot, Azure AI Foundry, plus the neutral "another tool not on this list" from Q6). The question is what a Respondent says about each one.

### Why it matters

You named three states — **used**, **tried**, **want to use** — and the distinction between the first two is doing real work. "Tried it" is arguably the most informative answer anyone can give: it means they had access, spent the effort, and *stopped*. That's a stronger signal about the tool than either never-touched-it or use-it-daily, and it's invisible in a tick-box.

The cost is grid fatigue. The survey already carries the 19-row Coverage grid, and Microsoft Forms renders a matrix question as a wall of radio buttons. A second grid immediately before or after it is where people start pattern-clicking. Five rows is small enough that I don't think it's fatal, but it isn't free, and every state you add widens the row.

There's also a wording trap. "Used" and "tried" are near-synonyms in ordinary English — a Respondent won't reliably split them unless the labels do it for them. Labels like *"Tried it, don't use it now"* versus *"Use it regularly"* carry their own distinction; labels like *"Used"* versus *"Tried"* do not.

### Options

| Option | Pros | Cons |
|---|---|---|
| **A. Three states** — Never used / Tried it, not using it now / Use it regularly | Captures the abandonment signal, which is the most interesting one. Narrow enough to render cleanly in Forms. Labels are self-distinguishing. | Drops "want to use" from this item (see Q11 — it may not belong here anyway). |
| **B. Four states** — Never used / Tried it, not using it now / Use it occasionally / Use it regularly | Adds intensity on top of abandonment. Closest to a full picture. | Widest row. "Occasionally" versus "regularly" is the fuzzy split my weekly floor was trying to fix, reintroduced. |
| **C. Two states** — Never used / Have used | Cheapest, renders as a plain multi-select, no grid at all. | Throws away the tried-and-stopped signal you explicitly asked for. |
| **D. Three states, plus a separate "would like to use more" multi-select underneath** | Keeps the grid narrow and puts aspiration in its own question where it reads naturally. | Two questions rather than one. Depends on Q11 landing on "keep it". |

### My recommendation

**A**, with the aspiration half decided separately in Q11. Three states is the smallest grid that carries the signal you asked for, the labels distinguish themselves without a frequency rule, and it keeps the row narrow enough to survive next to the Coverage grid.

Whichever you pick: the tool list needs the **"another tool not on this list"** row from Q6, and the question should be **required** in Forms — with "Never used" available on every row, nobody is forced into a false answer.

### Your answer

: Let's go with option B to have a few more states. 

---

## Q11 — Does "what they want to use going forward" belong here?

### What this is

The third state you named. Whether the tools item carries a forward-looking half, and if so, whether it stays an unscored Context item or becomes something else.

### Why it matters

This is the same category boundary Q9 just ruled on, approached from the other side. Q9 moved a *frequency* item out of Context because it was really a scored behaviour item. Aspiration raises the mirror-image question: **Future-state is the scored section**, and it has a fixed shape — every item on the **Desirability scale** (Definitely not … Definitely), every item answered **twice**, once for Personal stance and once for Team stance. That structure exists so the survey can surface *"I'd go further, but I don't think we should"*.

A tools wishlist fits none of that. "Would you like to use Azure AI Foundry more?" isn't a Desirability judgment about a practice, it's a preference about a product, and asking it twice per stance is faintly absurd — there's no meaningful team norm about whether *you personally* would like to open Foundry more often.

So it can't go into Future-state as-is. The remaining choices are: keep it in Context as an unscored extra, or drop it and let the Coverage grid's future column carry the aspiration.

The argument for dropping is that the Coverage grid **already asks the forward-looking question**, and asks a better one. It asks where a person wants AI involved in their *work* six months out. That's the aspiration that matters. Which product they'd like to open is downstream of it — and it's a question you can answer yourself from the work aspiration plus what's in the estate, without spending a Respondent's attention on it.

The argument for keeping is procurement. If four people say they'd like to use Foundry and nobody currently does, that's an enablement gap you can act on directly, and no amount of Coverage-grid inference tells you which licence to go get.

### Options

| Option | Pros | Cons |
|---|---|---|
| **A. Drop it** — Coverage grid's future column carries aspiration | Clean category line: Context describes today, Future-state handles aspiration, and neither leaks. Shortest survey. | Loses the direct procurement signal. You'd infer tool demand rather than read it. |
| **B. Keep it as a second unscored multi-select** — "which of these would you like to use more?" | Direct, actionable enablement signal. One short question. Stays unscored, so no clash with the Future-state structure. | A forward-looking Context item is a slight bend of the glossary's "unscored question about the Respondent". Needs the map's Notes to acknowledge it. |
| **C. Fold it into the Q10 grid as a fourth state** — "Not using it, but would like to" | No extra question. Reads naturally in a status grid. | A person who uses Copilot daily *and* wants Foundry can only say one thing per row — the state is exclusive, so use and desire collide. Fine per-tool, awkward overall. |
| **D. Send it to Future-state properly** — Desirability scale, both stances | Consistent with every other Future item. | The structure doesn't fit the content, and it doubles the question count for a product preference. I'd argue against this one. |

### My recommendation

**B.** It's one short multi-select, it stays unscored so nothing about the scoring rules changes, and it answers a question — *what should we enable next?* — that nothing else in the survey answers. **A** is the purist answer and I'd accept it, but I think you'd end up wanting the procurement signal and not having it.

If **B**, the Context section resolves at **two items**: the tools status grid, and the would-like-to-use multi-select. Both unscored, both about tools, both short.

### Your answer

: I think we can drop it. I think it's fine. 

---

## Anything else — round 4

<!-- If you leave this blank I'll take the frontier as empty after this round and write the resolution. -->

**Two things I intend to decide myself** unless you say otherwise here, because they're low-stakes and I don't want to spend a round on them:

1. **Placement** — Context items go at the **start** of the survey, before the Current-state section. They're easy warm-up questions, and a Respondent who has just enumerated their tools is better primed for the Dimension items than one who arrives cold.
: I think this is fine. We definitely want to vary the questions a little bit so that when the person is taking the survey, it's easier for them and they don't get stuck in their head about trying to think about answers. I don't want anything to take too long. I want everything to be quick and easy to understand and answer with a gut reaction, as opposed to a long, thought-out answer
2. **Preamble wording** — a line stating the tools question is about **enablement, not compliance**, so the "another tool not on this list" option reads as safe to tick rather than as a confession. This matters more than usual because results are named and a team view reaches your manager.
: I think this is fine because as long as it's anonymous at a Team View level, my manager probably already knows all this anyway. 

