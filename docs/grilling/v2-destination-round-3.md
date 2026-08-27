# Grilling — v2: naming the destination, round 3 (last one before charting)

**Effort:** v2 of the AI-Dev-Survey.
**Previous rounds:** `docs/grilling/v2-destination.md`, `docs/grilling/v2-destination-round-2.md`.
**Round:** 3 of 3 — **three questions**. One of them is important; the other two are small. After this I chart the map and cut tickets.
**How to use:** answer inline under each `### Your answer` heading.

---

## What round 2 settled

- **The Scored CSV contract dies.** No 293-column spec; `scoring/scored-csv-schema.md` retires. Python computes in memory and the **dashboard offers a CSV export** when you want one.
- **Dashboard = option C.** `dashboard/index.html` is the template; Python is the backend; I pick the frontend approach. Runs on localhost, launched by a script. Not-perfect-is-fine.
- **The Current-state section is confirmed untouched** — "all the questions about how they're using AI now will remain the same."
- **New team Dimensions are a ticket, not this round.** You want different question *types* at the team level; designing them is its own grilling session.
- **The personal six-month block gets reframed**, not deleted — you still want six-month answers, but re-asking the same items just returns the same answers, so the items have to change shape.
- **Dashboard visuals may change** as a consequence, and that's accepted.

## What I still assume

- The **manager boundary** is unchanged: named and internal for individuals, unnamed rendering upward for the team view.
- **Coverage survives** for the personal side. Q2 below checks that, because it's the one thing your Q1 answer might have quietly undercut.

---

## Q1 — The non-leading rule: overturned, softened, or does the conditional framing need a non-leading form? *(the important one)*

### What this is

You wrote: *"We need to reframe many of these questions to figure out their principles and values and what AI would have to do, or what development with AI would mean for them to change and use it more. I'm looking for a larger variety of questions around 'If this were true, how would you feel about this?'"*

That is a direct reversal of a rule v1 treated as inviolable. It sits in the map's Notes as the **non-leading rule**:

> No item may push a Respondent toward a position. **Never ask "what would have to be true for you to accept X" — it presupposes X is a destination.** Where a conditional answer is wanted, ask a plain description twice (current, future) and **derive it by subtraction**. Applies to every item bank.

It's not a stylistic preference. It's the reason [Conditional items](https://github.com/AndrewGodlewsky/AI-Dev-Survey/issues/19) got **renamed to Safeguard items** — the ticket's own conclusion was *"nothing conditional survived"* — and the reason **Levers** are derived by subtracting current safeguards from future ones rather than asked about directly.

### Why it matters

Two things, and I want to separate them because they have different answers.

**The mechanism you want is real and good.** "If this were true, how would you feel?" is a well-established way to surface values without interrogating them, and your instinct that re-asking the same items returns the same answers is correct.

**But the specific framing you wrote is leading**, in exactly the way the rule names. *"What AI would have to do for them to change and use it more"* presupposes that using it more is the destination and positions the Respondent as someone currently short of it. On a named survey whose team view reaches a manager, that pressure is not hypothetical — it's the same exposure that made N5 (job impact) the flagged item in v1.

There's a version that keeps your mechanism and drops the pressure: **describe a world and ask for a reaction, without implying the world is coming or desirable.** *"AI writes the first draft of every PR on this team. How do you feel about working that way?"* is a scenario. *"What would AI have to prove before you'd let it write your PRs?"* is a ramp. Same topic; only one of them tells the Respondent where they're supposed to end up.

### Options

| Option | Pros | Cons |
|---|---|---|
| **A. Overturn it** — conditional and "what would it take" items are allowed in v2 | Maximum freedom; the questions you described can be written literally. | The survey starts nudging. On named responses reaching a manager, answers drift toward what people think they should say — and you lose the ability to tell the drift from the truth. |
| **B. Keep the rule, add a sanctioned scenario form** — hypotheticals allowed as *neutral world descriptions* with no implied direction; "what would have to be true" still banned | Keeps your mechanism and the variety you want. Non-leading guarantee survives. Extends the pattern [Probe items](https://github.com/AndrewGodlewsky/AI-Dev-Survey/issues/8) already proved. | Harder to write. Every scenario needs checking for a hidden direction. |
| **C. Keep the rule as-is** — no hypotheticals; solve monotony by cutting and rewording only | Nothing to re-argue. | Doesn't give you what you asked for. The future block stays a second pass over the same ideas. |

### My recommendation

**B.** You've identified a genuine weakness — the future block returns the present because it asks the same thing twice — and scenarios are the right cure. But the cure shouldn't come with a direction attached, and it doesn't have to: a scenario item can be perfectly neutral about whether the world it describes is good, and the reaction is still the signal you want.

The practical shape: **a scenario item states a world in the present tense and asks for a position on it.** It never contains "would have to", never implies a threshold to clear, and never treats more-AI as the endpoint. If that constraint turns out to strangle the items when we actually write them, we revisit — but I'd rather find that out with drafts in hand than delete the guarantee up front.

### Your answer

: Yes, this is going to be changed in version 2, so we're going to have to gut the old stuff and replace it with a new version that is going to be the truth and can't be overturned. 

<!-- If B: are you OK with me rejecting a scenario you like on the grounds that it leads, when we get to writing them? That's the rule having teeth. -->

---

## Q2 — Does the Coverage grid survive, and with how many passes?

### What this is

The 19-row Development-area grid. Round 1 cut the team pass, leaving two: **today**, and **me in six months**.

### Why it matters

Your Q1 answer said the six-month Dimension items return the present because they ask the same thing twice — and the Coverage future pass has *exactly* that shape, 19 rows of it. If the reasoning applies there too, Coverage is one pass and the Coverage Gap dies with it. If it doesn't — because "where should AI sit on incident response in six months" is a concrete judgement rather than a restated attitude — it stays at two.

I lean towards it staying, but the argument you made against the Dimension items applies here almost word for word, so I'd rather ask than assume.

### Options

| Option | Pros | Cons |
|---|---|---|
| **A. Two passes — today + me in six months** | Keeps the Coverage Gap, the most concrete "here's where you want to move" output in the survey. | 38 grid answers. The second pass is where the pilot's fatigue was worst. |
| **B. One pass — today only** | Cheapest. 19 answers. No repetition anywhere in the survey. | No Coverage Gap. You'd know where AI sits today and nothing about where anyone wants it. |
| **C. Two passes, but the second is a scenario** — today, then "in a version of this team where AI does X, which areas would you be comfortable with?" | Consistent with the Q1 direction. | Harder to score; the Coverage Gap becomes a different quantity than v1's. |

### My recommendation

**A.** The grid is the only place the survey gets *concrete* — named areas of real work rather than attitudes — and the future pass asks for a judgement about 19 specific jobs, not a restatement of a feeling. It's also the output most likely to drive an actual conversation ("nobody wants AI near incident response" is a finding you can act on Monday).

### Your answer

: So all of the coverage grid should survive with respect to the individual "like me today." All of that was perfect. I don't want to change any of those questions. I do want to change many of the "me in six months" questions because I just felt like it was repetitive, re-answering the same questions over again, just where you think you'd be in six months. The problem I had when I was trying to do this in reality was that I don't know what I'll think in six months, because if I knew, I would be thinking that now. So it's more about trying to figure out: instead of asking hard questions about the state of where I think I'll be in six months, I need to ask more soft directional questions to understand principles and development going forward towards the future. In what ways do I want to be able to do that development in the future? 

---

## Q3 — Where do real exports and outputs live?

### What this is

Practical, and a privacy decision. Your workflow puts a **named Forms export** in a folder every time you run the app. Right now that folder is `Excel Example/` inside a **public** repository — I've added it to `.gitignore`, but an ignore rule is one `git add -f` or one misconfigured hook away from not helping.

### Why it matters

The repo is public and the file has `Name` and `Email` columns for every Respondent. The safest arrangement is that real data never sits inside the repo at all.

### Options

| Option | Pros | Cons |
|---|---|---|
| **A. A folder outside the repo** — e.g. `~/ai-dev-survey-data/`, path configurable, app defaults to it | Real data cannot be committed by accident, ever. | One path to configure the first time. |
| **B. A gitignored folder inside the repo** — `data/`, ignored, app reads from it | Everything in one place; nothing to configure. | One `-f`, one hook, one fresh clone with a stale ignore file, and it's public. |
| **C. Wherever you drop it** — app takes a path argument or a file picker | Most flexible. | Nothing stops it being dropped in the repo. |

### My recommendation

**A**, with the app defaulting to a folder outside the repo and accepting a path argument to override. The repository is public and the data is named — that's the one place where "simple and clean" should lose to "cannot go wrong."

### Your answer

: So I think we can use the initials for people inside the report, and it's totally fine because I don't intend to send this to my manager. I will just take a screenshot of the pieces that I need my manager to be able to see. 

---

## Anything else

Last chance before I chart the map — sequencing, anything you want built first, anything you'd rather I stop assuming.

### Your answer

:
