# Rubric — scoring the AI-Dev-Survey by hand

Assembled in wayfinder ticket [#14](https://github.com/AndrewGodlewsky/AI-Dev-Survey/issues/14) from the decisions in
[#2](https://github.com/AndrewGodlewsky/AI-Dev-Survey/issues/2) (scales), [#3](https://github.com/AndrewGodlewsky/AI-Dev-Survey/issues/3) (Coverage grid),
[#4](https://github.com/AndrewGodlewsky/AI-Dev-Survey/issues/4) (level text), [#5](https://github.com/AndrewGodlewsky/AI-Dev-Survey/issues/5) / [#6](https://github.com/AndrewGodlewsky/AI-Dev-Survey/issues/6) (item banks),
[#7](https://github.com/AndrewGodlewsky/AI-Dev-Survey/issues/7) (Context item), [#8](https://github.com/AndrewGodlewsky/AI-Dev-Survey/issues/8) (Probe items),
[#9](https://github.com/AndrewGodlewsky/AI-Dev-Survey/issues/9) (scoring rules), [#12](https://github.com/AndrewGodlewsky/AI-Dev-Survey/issues/12) (Scored CSV) and
[#19](https://github.com/AndrewGodlewsky/AI-Dev-Survey/issues/19) (Safeguard items). Those files remain the decision records; **this document is what the
Scoring sheet implements**, and it is complete on its own: everything needed to score one person's response by hand is here.

**Every Dimension is scored in its natural direction.** Concern 5 = most concerned; Guardrails 5 = wants the most process. Neither
is "good" or "bad". Nothing in this rubric ranks a person.

---

## 1. What gets scored, and what doesn't

| Instrument | Output | Scored? |
|---|---|---|
| **Seven Dimensions** — Comfort · Trust · Fluency · Guardrails · Concern · Autonomy · Craft values | Three scores each, 1–5 with decimals: **Current**, **Future-Personal** ("what I would do"), **Future-Team** ("what the team should adopt") — plus a **Gap** and a **Stance gap** | Yes — §3, §4 |
| **Coverage** — 19 Development areas | A **profile**: one Involvement level (1–6, or N/A) per area, per pass. Never a single number. | Profile, not score — §5 |
| **Probe items** (5, Future-state only) | **Edge markers** — a person endorsed an extreme, per stance | Never scored — §6.1 |
| **Safeguard items** (asked three times + learning interest) | Accepted safeguards, **Levers**, principle hold, inconsistency flag | Never scored — §6.2 |
| **Context item** (tools matrix) | A lens for reading the rest | Never scored — §6.3 |
| **Answer patterns** (three item blocks) | **Pattern flags** — a block answered flat, or the Team block copied from the Me block | Never scored — §6.4 |

## 2. The answer scales and their numbers

Microsoft Forms exports the **label**; scoring uses the **number**. These are the only five conversions.

| Scale | Used by | 1 | 2 | 3 | 4 | 5 | 6 |
|---|---|---|---|---|---|---|---|
| **Behaviour** — "How often…" | Current-state items marked **B** | Never | Rarely | Sometimes | Often | Always | — |
| **Attitude** — "How well does this describe you today?" | Current-state items marked **A** | Not at all | Slightly | Moderately | Mostly | Completely | — |
| **Desirability** — "In six months, I would… / the team should…" | Every Future-state item and probe, both stances | Definitely not | Probably not | Unsure | Probably | Definitely | — |
| **Involvement level** | Coverage grid, all three passes | None | Advisor | Drafter | Doer, reviewed | Doer, spot-checked | System-verified |
| **Tool use** | Context item | Never used | Tried it, not using it now | Use it occasionally | Use it regularly | — | — |

The Involvement scale also has **N/A — I don't do this work**, which is not a number (§5.3). Dimension items have no N/A: every one is
required, and a blank is a defect, not an answer (§3, step 0).

## 3. Scoring a Dimension by hand

Do this once per Dimension, three times — for the Current answers, the Future-Personal answers and the Future-Team answers.

0. **Check for blanks.** If any item of the Dimension is blank, stop: that Dimension's score is **`#N/A`** and the blank item is recorded in the
   malformed flag. Never average the items that are present — a Respondent scored on two of five Concern facets would look like everyone else
   on a dashboard built entirely of comparisons. Go and ask the person.
1. **Convert labels to numbers** with the scale table above.
2. **Reverse-key.** For every item marked **R**, replace the answer with `6 − answer`. A 1 becomes 5, a 4 becomes 2. Do this before anything else.
3. **Collapse multi-item facets.** Only one exists: Current-state Guardrails G2 and G3 are one facet (disclosure) asked two ways — take their mean
   first. Every other facet is a single item.
4. **Score = mean of the facets.** Keep the decimals; do not round.
5. **Landmark.** The nearest integer (halves round up) points at the level text in §4. It is a label for reading, never the score, and it never
   enters any arithmetic.
6. **Gaps.** Per person, exactly two subtractions per Dimension, both unrounded:
   - **Gap** = Future-Personal − Current. *How far I want to move.* Positive = wants more of the Dimension.
   - **Stance gap** = Future-Team − Future-Personal. Negative = *"I'd go further than the team should"*; positive = *"the team should go further than I would"*.
   - **Never** Future-Team − Current per person: it subtracts a statement about the team from a statement about oneself. That subtraction exists only
     at team level, as the *norm gap* (team mean Future-Team − team mean Current).

**Why decimals.** Rounding before subtracting manufactures movement: Current 3.4 and Future 3.6 would round to 3 and 4, a Gap of 1 for a real
move of 0.2. Gap is the number this survey exists to produce. On a three-facet Dimension, a Gap of **0.3 is one person moving one facet a full
point — real and reportable.** Display to one decimal.

## 4. The Dimensions

Each Dimension below lists: its definition; the Current-state items (kind **B**/**A**, **R** = reverse-keyed); the Future-state stems (each
completes both *"In six months, I would…"* and *"In six months, the team should…"*; **R** as marked); the facet map; and the level text 1–5.
Level text is worded as a **position**, not an action, so the same words read correctly as a Current score ("where I am today") and as a Future
score ("where I want to be / where the team should be in six months").

### 4.1 Comfort — willingness to use AI in my own development work

| Current | Kind | R | Item |
|---|---|---|---|
| C1 | B | | How often do you use an AI tool in your development work? |
| C2 | B | | How often do you use AI on work that ends up in production? |
| C3 | A | **R** | I'd rather work through something myself than hand any of it to AI. |

| Future | R | Stem |
|---|---|---|
| FC1 | | …use AI in most development work. |
| FC2 | | …use AI on work that ends up in production. |
| FC3 | **R** | …keep doing things by hand rather than hand them to AI. |

**Facets:** C1 · C2 · C3 → FC1 · FC2 · FC3.

| Level | Position |
|---|---|
| 1 | Would rather not use AI for development work at all; uses it only when there is no alternative. |
| 2 | Uses AI for peripheral, low-stakes things — lookups, explanations, boilerplate — and keeps it away from real work. |
| 3 | Comfortable using AI on everyday work, but switches it off for anything important, unfamiliar, or high-blast-radius. |
| 4 | Reaches for AI by default on most work, including work that matters; only a few areas are deliberately held back. |
| 5 | AI is the default starting point for essentially all development work; working without it is the exception that needs a reason. |

### 4.2 Trust — confidence that AI output is correct and safe without line-by-line scrutiny

| Current | Kind | R | Item |
|---|---|---|---|
| T1 | A | | I expect code an AI writes for me to be correct. |
| T2 | B | **R** | How often do you read AI-written code line by line before you use it? |
| T3 | A | | I trust AI's output about as much as I'd trust a colleague's. |

| Future | R | Stem |
|---|---|---|
| FT1 | | …treat AI output as correct by default, checking only when something looks off. |
| FT2 | **R** | …read AI-written code line by line before it is used. |
| FT3 | | …trust AI's output about as much as a colleague's. |

**Facets:** T1 · T2 · T3 → FT1 · FT2 · FT3. Read T1 against T2: someone who *expects* correctness but reads every line is saying something useful.

| Level | Position |
|---|---|
| 1 | Assumes AI output is wrong until proven otherwise; nothing is believed before it has been read in full. |
| 2 | Expects frequent errors; output is usable only after being checked end to end. |
| 3 | Trusts AI output on familiar, well-specified work; anything else gets full scrutiny. |
| 4 | Generally trusts AI output and reviews it the way a competent colleague's work is reviewed — read and judged, not re-derived. |
| 5 | Treats AI output as correct unless a test, check, or reviewer says otherwise; line-by-line reading is reserved for when something fails. |

### 4.3 Fluency — practical skill with AI tools

| Current | Kind | R | Item |
|---|---|---|---|
| F1 | B | | How often do you get a usable result from an AI tool within a try or two? |
| F2 | B | | How often do you deliberately give an AI tool context — pointing it at the right files, rules, or docs? |
| F3 | A | **R** | When an AI tool doesn't give me what I need, I'm not sure what to change. |

| Future | R | Stem |
|---|---|---|
| FF1 | | …be able to get what's needed out of an AI tool in a try or two. |
| FF2 | | …routinely give AI tools proper context — the right files, rules and docs. |
| FF3 | **R** | …use AI tools as they come out of the box, without configuring or tuning them. |

**Facets:** F1 · F2 · F3 → FF1 · FF2 · FF3. **F3 → FF3 is facet-matched, not word-matched** (nobody can *want* to stay confused, so the future
item names a low-Fluency position someone could prefer). The Fluency Gap is therefore **softer** than the other five — do not read it to one decimal
with the same confidence.

| Level | Position |
|---|---|
| 1 | Little or no hands-on use; unclear what the tools can do or how to drive them. |
| 2 | Uses a chat or autocomplete tool as it comes out of the box; prompting is ad-hoc and results are hit-or-miss. |
| 3 | Gets reliable results on ordinary tasks — knows how to supply context, iterate on a prompt, and recognise a bad answer. |
| 4 | Works fluently with agents and multi-step workflows; configures the tooling (rules, context files, MCP, permissions) and knows the common failure modes. |
| 5 | Builds and tunes AI workflows that others use; treats setup, evaluation, and failure modes as part of the craft. |

### 4.4 Guardrails — how much review, disclosure, testing and policy I want around AI-assisted work

*High is not "good" — this is how much process the Respondent wants, not how responsible they are.*

| Current | Kind | R | Facet | Item |
|---|---|---|---|---|
| G1 | A | | Review + testing | AI-assisted work needs more review and testing than work someone wrote by hand. |
| G2 | A | | Disclosure — endorsed | People should say when a change was mostly written by AI. |
| G3 | B | | Disclosure — practised | How often do you tell people a change was mostly written by AI? |
| G4 | A | | Off-limits areas | There should be parts of our work where AI isn't used at all. |
| G5 | A | | Enforcement strength | Whatever we agree about AI use should be enforced by our tooling, not left to judgement. |
| G6 | A | **R** | The "nothing extra" pole | Our current process already covers AI-assisted work; it needs nothing extra. |

| Future | R | Facet | Stem |
|---|---|---|---|
| FG1 | | Review + testing | …give AI-assisted work more review and testing than hand-written work. |
| FG2 | | Disclosure | …say when a change was mostly written by AI. |
| FG3 | | Off-limits areas | …keep parts of our work where AI isn't used at all. |
| FG4 | | Enforcement strength | …have whatever we agree about AI enforced by our tooling rather than left to judgement. |
| FG5 | **R** | The "nothing extra" pole | …need nothing beyond our current process for AI-assisted work. |

**Facets (five):** G1 · **mean(G2, G3)** · G4 · G5 · G6 → FG1 · FG2 · FG3 · FG4 · FG5. The disclosure pair collapses because "endorsed" and
"practised" are one facet that only splits in the present tense; a flat mean over six items would give disclosure a third of the score and make
the Current and Future means structurally different. The **G2 − G3 difference** (endorsed minus practised) is worth reading on its own.

| Level | Position |
|---|---|
| 1 | AI-assisted work needs no special treatment; the team's existing rules are already enough. |
| 2 | Norms rather than rules: people are expected to use judgement, with maybe a convention or two and nothing enforced. |
| 3 | A few explicit expectations for AI-assisted work — e.g. tests required, author reads it before opening a PR — held by agreement. |
| 4 | Written team rules covering what must be reviewed, disclosed, and tested, plus agreed limits on where AI may be used at all. |
| 5 | Controls enforced in the tooling: mandatory disclosure, required human review, gates in CI, and named areas AI may not touch. |

### 4.5 Concern — perceived risk from AI-assisted development

*Security, IP/licensing, skill atrophy, job impact, maintainability. 5 = most concerned. High is not "bad".*

| Current | Kind | R | Risk | Item |
|---|---|---|---|---|
| N1 | A | | Skill atrophy | I worry that leaning on AI will erode my own skills. |
| N2 | A | | Security | AI-written code could introduce security problems we wouldn't catch. |
| N3 | A | | IP / licensing | Using AI-generated code could create licensing or IP problems for us. |
| N4 | A | **R** | Maintainability | Code we write with AI will be just as maintainable as anything else we write. |
| N5 | A | | Job impact | I expect AI to change what my job is within a few years. |

| Future | R | Risk | Stem |
|---|---|---|---|
| FN1 | | Skill atrophy | …treat skill erosion as a real risk to watch for. |
| FN2 | | Security | …treat security problems in AI-written code as a live risk to guard against. |
| FN3 | | IP / licensing | …treat licensing and IP exposure from AI-generated code as a live risk. |
| FN4 | **R** | Maintainability | …be relaxed about how maintainable AI-written code is. |
| FN5 | | Job impact | …plan for AI changing what our jobs are. |

**Facets (five):** one per risk, N1–N5 → FN1–FN5. **Read the five separately as well as the mean:** a Concern of 3 can be "mildly worried about
everything" or "alarmed about security, relaxed about the rest", and those need different responses. The Future scores are worded as *the vigilance
in force* — nobody sets a target for how worried they want to be.

| Level | Position |
|---|---|
| 1 | No meaningful risk beyond the ordinary risks of writing software; nothing here needs watching. |
| 2 | The risks are real in principle but not live for this team on this work; awareness is enough. |
| 3 | One or two risk areas warrant active attention; the rest can be left alone. |
| 4 | Several risk areas warrant active attention at once, and real damage — to code quality, skills, or the team — is expected if adoption continues unchanged. |
| 5 | Risk is the dominant fact about AI-assisted development; serious harm is expected unless something changes. |

### 4.6 Autonomy — how unsupervised AI may act on my behalf

| Current | Kind | R | Item |
|---|---|---|---|
| A1 | B | | How often do you let an AI tool edit files or run commands in your project? |
| A2 | B | **R** | How often do you approve an agent's steps as it goes, rather than letting it run on? |
| A3 | B | | How often do you hand AI a whole task and come back to a finished change? |

| Future | R | Stem |
|---|---|---|
| FA1 | | …let AI tools edit files and run commands directly. |
| FA2 | **R** | …approve an agent's steps as it goes rather than letting it run on. |
| FA3 | | …hand AI a whole task and come back to a finished change. |

**Facets:** A1 · A2 · A3 → FA1 · FA2 · FA3. A1 = does it act at all; A3 = does it act unattended; A2 is the leash, reversed.

| Level | Position |
|---|---|
| 1 | Inline assistance only: completions and suggestions in the editor, accepted or rejected one at a time. |
| 2 | Chat: AI answers questions and produces snippets; a human carries every change into the codebase. |
| 3 | Supervised agent: AI edits files and runs commands while a human watches each step and approves the risky ones. |
| 4 | Delegated agent: AI is handed a task and works unattended, then hands back a finished change a human reviews before it lands. |
| 5 | Autonomous agent: AI takes a task all the way to landed work, with automated checks — not a person — as the gate. |

### 4.7 Craft values — weight placed on general development principles

*Understanding every line, tests, review, ownership. Not AI-specific; a lens for reading the other Dimensions, not an adoption metric.*

| Current | Kind | R | Item |
|---|---|---|---|
| V1 | A | | Code I ship should be something I could walk someone else through. |
| V2 | A | **R** | When a deadline is tight, tests and review are the first things I drop. |
| V3 | A | | I'd hold up my own change to fix something only I would notice. |

| Future | R | Stem |
|---|---|---|
| FV1 | | …ship only code someone could walk another person through. |
| FV2 | **R** | …let speed win over polish more often than it does today. |
| FV3 | | …hold up a change to fix something only its author would notice. |

**Facets:** V1 · V2 · V3 → FV1 · FV2 · FV3. **V2 → FV2 is facet-matched, not word-matched** (nobody volunteers "Definitely, I'd drop tests" in a
named survey). The Craft values Gap is **softer**, like Fluency's. The Future scores read as *the standard that should be in force*.

| Level | Position |
|---|---|
| 1 | Working software is what counts; understanding, tests, and review are overhead to be skipped when they slow delivery. |
| 2 | Worth having in principle, but the first thing to drop under pressure. |
| 3 | A working baseline holds — code is reviewed, reasonably tested, and understood by whoever ships it — and is traded away deliberately when the cost is high. |
| 4 | Understanding, tests, review, and ownership are non-negotiable for anything that reaches production. |
| 5 | Craft is the point: nothing ships that its author cannot explain line by line, and depth of understanding is defended even at real cost to speed. |

## 5. Coverage — the Involvement profile

Coverage is not a score. Per person it is **the raw Involvement level per Development area**, for each of three passes — *Today*,
*In 6 months — for me*, *In 6 months — the team should*. Nothing is averaged, ever: the levels are named, qualitatively different states, and
Drafter → Doer-reviewed (a human ceasing to write and starting to check) is not the same step as Doer-spot-checked → System-verified.

### 5.1 The Involvement level scale

| # | Column header (what Respondents see) | Definition |
|---|---|---|
| 1 | **None** — no AI | I do this without AI. |
| 2 | **Advisor** — AI explains, I do the work | I ask AI to explain, look up, or suggest; every artifact is written by me. |
| 3 | **Drafter** — AI drafts, I rework every line | AI produces a first draft; I read and edit all of it before it counts. |
| 4 | **Doer, reviewed** — AI does it, I review the result | AI produces the finished artifact; I review it as I would a colleague's work. |
| 5 | **Doer, spot-checked** — AI does it, I spot-check | AI produces it; I sample or skim rather than review fully. |
| 6 | **System-verified** — AI does it, checks catch errors | AI produces it end-to-end; no individual looks unless automated checks (tests, CI, policy gates, monitors) fail. |
| — | **N/A** — I don't do this work | Excluded from this person's profile; counted. |

### 5.2 The 19 Development areas

Each row carries a one-line "AI does it" example so levels 4–6 are concrete. Four rows (**custom**) have their own anchor wording because
"AI does it" is ambiguous there. ◆ marks the six **high-stakes** areas (§6.1).

| Group | Area | "AI does it" means… | Anchors |
|---|---|---|---|
| Core SDLC | Requirements & ideation | AI turns a rough ask into user stories / acceptance criteria | shared |
| Core SDLC | Architecture & design | AI proposes the design, component boundaries, and trade-offs | shared |
| Core SDLC | Writing production code | AI writes the feature code | shared |
| Core SDLC | Writing tests | AI writes the unit/integration tests | shared |
| Core SDLC | Code review ◆ | AI reviews someone else's PR | **custom** |
| Core SDLC | Debugging | AI finds the root cause and writes the fix | shared |
| Core SDLC | Documentation | AI writes READMEs, ADRs, API docs, comments | shared |
| Core SDLC | Refactoring & legacy migration | AI performs the refactor / migration across the codebase | shared |
| Ops & delivery | CI/CD & build configuration ◆ | AI writes/changes pipelines and build files | shared |
| Ops & delivery | Infrastructure-as-code ◆ | AI writes Terraform/Bicep/etc. and applies changes | shared |
| Ops & delivery | Incident response & on-call ◆ | AI diagnoses and remediates a live incident | **custom** |
| Ops & delivery | Monitoring & alerting | AI defines dashboards/alerts and triages alerts | shared |
| Data & security | SQL & data migrations ◆ | AI writes the migration and the data backfill | shared |
| Data & security | Security review & threat modeling ◆ | AI performs the review and produces findings | **custom** |
| Data & security | Dependency upgrades | AI bumps versions and resolves breaking changes | shared |
| Non-code | Estimates & planning | AI breaks work down and sizes it | shared |
| Non-code | Stakeholder comms & PR descriptions | AI writes the update / PR description | shared |
| Non-code | Learning new tech | AI is the tutor / produces the learning material | **custom** |
| Non-code | Meeting notes & summaries | AI transcribes and summarizes | shared |

**Custom anchors**

| # | Code review — the "work" is reviewing | Incident response — acting in production | Security review & threat modeling | Learning new tech — the "work" is my understanding |
|---|---|---|---|---|
| 1 | I review PRs without AI. | I handle incidents without AI. | I do security review without AI. | I learn from docs, books, and people; no AI. |
| 2 | AI explains the diff or answers my questions; I write every review comment. | AI helps me read logs/errors and suggests hypotheses; I do everything. | AI explains vulnerability classes or a specific finding; I do the review. | AI answers questions while I work through the material myself. |
| 3 | AI drafts review comments; I rewrite them before posting. | AI proposes a diagnosis and a fix; I verify the diagnosis and rewrite the fix myself. | AI drafts a threat model / findings list; I re-derive and rewrite it. | AI builds me a tailored tutorial or example; I work through and verify all of it. |
| 4 | AI posts its review; I still read the whole diff and add or veto comments. | AI diagnoses and prepares the remediation; I review and execute it. | AI produces the findings; I review each finding and the code it points at. | AI summarizes the tech and I rely on the summary after checking key claims. |
| 5 | AI posts its review; I skim the diff and its findings. | AI executes the remediation; I spot-check afterwards. | AI produces the findings; I spot-check the high-severity ones. | AI summarizes; I skim and trust it. |
| 6 | AI review is the merge gate; no human reviewer unless it flags something. | AI auto-remediates; monitors and rollback guards catch mistakes, no human in the loop. | AI security gates in CI decide; no human security review unless a gate fails. | I don't learn it — AI applies the tech for me and checks catch errors. |

### 5.3 Rules for one person's Coverage

- **Coverage Gap** per area = Future-Personal level − Current level, in **signed levels** (`+2`). **Coverage Stance gap** = Future-Team − Future-Personal.
- **A Gap exists only where both sides are numeric.** The two mixed cases are not gaps and are never silently dropped:

| Today | Future | Reading | Rule |
|---|---|---|---|
| N/A | N/A | Doesn't do this work, doesn't expect to. | Excluded from the area entirely. |
| level | level | Normal. | Gap = Future − Current. |
| **N/A** | **level** | "I don't do this work now, but I expect to." | **No Gap** — no baseline. Counted and flagged. |
| **level** | **N/A** | "I won't be doing this work in six months." | **No Gap.** Counted and flagged. |

  These are signals about how the team expects its work to be *distributed* — a staffing signal, not an adoption signal.
- **Never average across areas.** Meeting notes and Security review do not share a number; a "mean Coverage" is meaningless. That is the point of a profile.
- At team level the profile is the **distribution** (how many people at each level, per area); a median (lower middle at even n) only where one number is unavoidable, e.g. to sort areas. Team rules live in `scoring/scoring-rules.md` §5 and are the Scoring sheet's and dashboard's job, not the hand-scorer's.

## 6. The non-scoring attributes

Each sits *beside* a person's scores, never inside one. **A marker locates a position; it does not report a fault.**

### 6.1 Probe items → Edge markers

Five Future-state items, indistinguishable from their neighbours, each a concrete scenario at one **pole** of a Dimension, worded so that
**"Definitely" is always the edge**. Answered on the Desirability scale for both stances like everything else.

| Probe | Dimension | Pole | *For me* — "In six months, I would…" | *For the team* — "…the team should…" |
|---|---|---|---|---|
| P1 | Comfort | low | …be happy working with no AI tooling at all, the way I worked before it existed. | …be fine going back to no AI tooling at all. |
| P2 | Trust | high | …merge AI-written code I had not read line by line, as long as the tests pass. | …merge AI-written code nobody has read line by line, as long as the tests pass. |
| P3 | Autonomy | high | …let an agent work unsupervised for an hour and only look at the final result. | …let agents work unsupervised for an hour and only review the final result. |
| P4 | Concern | high | …slow down how fast I adopt AI, because the risks outweigh what I'd gain. | …slow down how fast we adopt AI, because the risks outweigh what we'd gain. |
| P5 | Craft values | high | …expect to be able to explain every line of code that ships under my name. | …expect everyone to be able to explain every line that ships under their name. |

Rules: **never enters a Dimension mean; never reverse-keyed.** An **Edge marker** is raised when the answer is **4 or 5**, separately per
stance, giving three states — *both* (an accelerator, or on P1/P4 a brake), *personal only* ("I'd go, but we shouldn't"), *team only*
("the team should, but not me"). Fluency and Guardrails carry no probe.

**Edge markers from the grid.** Involvement level **6** on one of the six high-stakes areas ◆ — Code review, CI/CD, Infrastructure-as-code,
Incident response, SQL & data migrations, Security review — also raises an Edge marker, **per pass and labelled with it**: a 6 today is a different
statement from wanting one in six months. A 6 on any other area raises nothing.

### 6.2 Safeguard items → Levers, holds and flags

One multi-select, **"which of these do you accept instead of reading AI's output yourself?"**, asked three times (today · in six months, for me ·
in six months, the team should) plus once as **"which would you want to know more about?"**. Same seven options every time, in this order:

1. **I'd read it myself — nothing on this list changes that**
2. Another person reviews it
3. The test suite passes
4. It's easy to roll back if it's wrong
5. A type check or schema validation covers it
6. The blast radius is small (docs, internal tooling, non-production)
7. An automated security or lint scan covers it

It is a **Respondent-level** attribute, not a Dimension item: the same list answers Trust ("is the output right?") and Autonomy ("how long is the
leash?") at once, and is read against both. Derived readings, all per person:

| Reading | Rule |
|---|---|
| **Lever** | Ticked in *future-me* but **not** in *today*. What would move this person — derived by subtraction, **never asked**, because asking "what would have to be true?" pushes people toward a position. |
| **Principle hold** | "I'd read it myself" ticked in *future-me* (and the answer is consistent). The line does not move; a real constraint on the plan, not an obstacle. |
| **Team norm** | Option ticked in *team should* by a majority — a draft six-month norm the team can write down. |
| **Learning interest** | Ticked in *know more about* but not in *future-me*. Forward-looking, free of any admission. |
| **Inconsistent** | "I'd read it myself" ticked **alongside** another safeguard in the same asking. **Flagged, never resolved by rule**; that person's Levers are not computed (they read `NA`). With 5–9 named people, go and ask. |

Ticking the same boxes today and in six months is a valid answer: it says the line doesn't move. Never scored into any Dimension.

### 6.3 Context item — the tools lens

One required matrix, first in the survey: *Which of these AI tools do you use in your development work?* Rows: GitHub Copilot · Copilot Studio ·
Microsoft 365 Copilot · Azure AI Foundry · Another AI tool not on this list. Columns: the Tool-use scale (§2). **A lens, never a metric** — a
cautious Autonomy score reads differently from someone whose only exposure is inline completion than from someone running agents in Foundry.
The "another tool" row is a signal about the estate, not the person, and has no follow-up.

### 6.4 Answer patterns → Pattern flags

The reverse-keyed items only *dampen* an unread block — a flat *Probably* down the 30-row `[Me]` block still scores a plausible 3.3
everywhere, and a flat *Unsure* scores 3.0 and is invisible, because `6 − 3 = 3`. And a `[Team]` block copied from the `[Me]` block
produces a Stance gap of 0 on every Dimension. So the hand-scorer reads three blocks for a pattern, on the **raw answers, before
reverse-keying**, blanks left out:

| Block | Rows | Reverse-keyed rows |
|---|---|---|
| Current — the 17 Attitude-scale items | C3 T1 T3 F3 G1 G2 G4 G5 G6 N1–N5 V1 V2 V3 | C3 F3 G6 N4 V2 (5) |
| Future `[Me]` | 25 items + 5 probes | FC3 FT2 FF3 FG5 FN4 FA2 FV2 (7) |
| Future `[Team]` | 25 items + 5 probes | same stems (7) |

For each block find the **modal share** (the most frequent answer's share of all answered rows), then the **mode of the
non-reversed rows only** (what the person says when not reversed — if two values tie, drop 3 and take the one fewer reversed rows
sit at), and count the reverse-keyed rows answered **at that mode**. Then:

- **Flat** — raise the flag if the mode is not 3 *and* all but at most one of the reverse-keyed rows sit at the mode (≥ 6 of 7; ≥ 4 of 5),
  **or** if the modal share is ≥ 0.90 whatever the mode. (At a mode of 3 the reversed rows *belong* at the mode, so that count is not evidence.)
- **Stance-identical** — count the 30 Future stems answered the same in both blocks; raise the flag at ≥ 28.

A Pattern flag **changes no number**. It is a conversation to have before the results go upward: *"your answers follow a pattern the
reverse-keyed items don't support"* — never "you straight-lined". If the person confirms it, they re-take the block, or a human leaves
them out the way a blank would (§3 step 0). The Scoring sheet keeps the three thresholds in input cells; these are the defaults.
Rules and rationale: `scoring/scoring-rules.md` §6.1.

## 7. Reading one person's numbers

- **The decimal is the score; the integer is a landmark.** Say "Trust 3.4 — closest to level 3: *trusts AI output on familiar, well-specified work…*",
  never "Level 3". The prose is a translation; the number is the finding.
- **A Gap of 0.3 is real** — one facet moving one point on a three-facet Dimension. The **Fluency and Craft values Gaps are softer** than the other
  five (§4.3, §4.7) and should not be quoted to the same precision.
- **Guardrails high ≠ responsible; Concern high ≠ negative.** Both are positions. Concern's five facets are the diagnosis; the mean is the summary.
- **Stance gap sign:** negative = *I'd go further than the team should*; positive = *the team should go further than I would*. Both ends are that
  person's own answers, so — unlike Future-Team − Current — it is a real quantity.
- **`#N/A` is a defect, not a result.** Recovery is a conversation, not a formula.
- **Edge markers, holds and flags describe positions.** None of them is a fault, and none enters a score.

## 8. Worked example — Sofia Marchetti (fictional)

Sofia is one of the seven invented Respondents in [`scoring/scored-sample.csv`](../scoring/scored-sample.csv); every number below can be checked
against her row there. She was chosen because her response has the awkward cases: an N/A that becomes a level, and an inconsistent safeguard answer.

### 8.1 Her answers (already converted to numbers)

**Context:** GitHub Copilot 3 (occasionally) · Copilot Studio 1 (never) · M365 Copilot 4 (regularly) · Azure AI Foundry 2 (tried, stopped) · Other 1.

**Current-state items** (R = reverse-keyed; the arrow shows `6 − answer`):

| Dimension | Answers |
|---|---|
| Comfort | C1 = 3 · C2 = 2 · C3 (R) = 4 → **2** |
| Trust | T1 = 2 · T2 (R) = 3 → **3** · T3 = 2 |
| Fluency | F1 = 2 · F2 = 3 · F3 (R) = 4 → **2** |
| Guardrails | G1 = 3 · G2 = 3 · G3 = 3 · G4 = 3 · G5 = 4 · G6 (R) = 2 → **4** |
| Concern | N1 = 3 · N2 = 3 · N3 = 4 · N4 (R) = 3 → **3** · N5 = 4 |
| Autonomy | A1 = 2 · A2 (R) = 4 → **2** · A3 = 2 |
| Craft values | V1 = 3 · V2 (R) = 3 → **3** · V3 = 4 |

**Future-state items**, *for me* / *the team should*:

| Dimension | For me | The team should |
|---|---|---|
| Comfort | FC1 = 4 · FC2 = 4 · FC3 (R) = 2 → **4** | 4 · 4 · FC3 = 1 → **5** |
| Trust | FT1 = 4 · FT2 (R) = 2 → **4** · FT3 = 4 | 4 · 2 → **4** · 3 |
| Fluency | FF1 = 4 · FF2 = 4 · FF3 (R) = 1 → **5** | 4 · 4 · 2 → **4** |
| Guardrails | FG1–FG4 = 3 · FG5 (R) = 3 → **3** | all 3 → **3** |
| Concern | FN1 = 2 · FN2 = 3 · FN3 = 3 · FN4 (R) = 3 → **3** · FN5 = 3 | 3 · 4 · 3 · 3 → **3** · 3 |
| Autonomy | FA1 = 4 · FA2 (R) = 2 → **4** · FA3 = 4 | 4 · 2 → **4** · 4 |
| Craft values | FV1 = 3 · FV2 (R) = 3 → **3** · FV3 = 3 | 4 · 2 → **4** · 4 |

**Probes** (me / team): P1 2/1 · P2 3/3 · P3 3/3 · P4 2/2 · P5 3/3.

**Coverage** (Today / 6 months me / team should) — the rows that matter for the example; the full profile is in the CSV:
Requirements 4 / 6 / 5 · Writing tests 2 / 3 / 3 · Code review 2 / 3 / 3 · **Infrastructure-as-code N/A / N/A / N/A** ·
**Security review N/A / 3 / 3** · Estimates 3 / 5 / 4 · Meeting notes 3 / 5 / 5.

**Safeguards:** today — *another person reviews it*. In six months, for me — **"I'd read it myself" and "the test suite passes"**. The team should
— *tests*, *rollback*. Know more about — *schema check*, *small blast radius*.

### 8.2 Scoring

**Comfort, current.** No blanks. Reverse C3: 6 − 4 = 2. Facets 3 · 2 · 2 → mean **2.33**. Landmark 2: *"uses AI for peripheral, low-stakes
things… and keeps it away from real work."* Future-Personal: 4 · 4 · 4 → **4.00**. Future-Team: 4 · 4 · 5 → **4.33**.
**Gap = 4.00 − 2.33 = +1.67. Stance gap = 4.33 − 4.00 = +0.33** (the team should go slightly further than she would).

**Guardrails, current** — the one with a collapsed facet. Reverse G6: 6 − 2 = 4. Collapse disclosure: mean(G2, G3) = mean(3, 3) = 3. Facets
3 · 3 · 3 · 4 · 4 → **3.40**. Landmark 3: *"a few explicit expectations… held by agreement."* Future-Personal: 3 · 3 · 3 · 3 · 3 → **3.00**;
Future-Team **3.00**. **Gap = −0.40** (she'd want slightly *less* process in six months than she has today); **Stance gap = 0.00**.

**Concern, current.** Reverse N4: 6 − 3 = 3. Facets 3 · 3 · 4 · 3 · 4 → 17 / 5 = **3.40**; landmark 3. Read the five: IP/licensing and job
impact at 4 are what lift it. Future-Personal 2 · 3 · 3 · 3 · 3 → **2.80**; Future-Team 3 · 4 · 3 · 3 · 3 → **3.20**. **Gap = −0.60;
Stance gap = +0.40.**

The remaining four, same procedure:

| Dimension | Current | Future-Personal | Future-Team | Gap | Stance gap |
|---|---|---|---|---|---|
| Trust | 2 · 3 · 2 → **2.33** | 4 · 4 · 4 → **4.00** | 4 · 4 · 3 → **3.67** | **+1.67** | **−0.33** |
| Fluency | 2 · 3 · 2 → **2.33** | 4 · 4 · 5 → **4.33** | 4 · 4 · 4 → **4.00** | **+2.00** *(softer)* | **−0.33** |
| Autonomy | 2 · 2 · 2 → **2.00** | 4 · 4 · 4 → **4.00** | **4.00** | **+2.00** | **0.00** |
| Craft values | 3 · 3 · 4 → **3.33** | 3 · 3 · 3 → **3.00** | 4 · 4 · 4 → **4.00** | **−0.33** *(softer)* | **+1.00** |

**Coverage.** Requirements 4 → 6: Gap **+2 levels**; Stance gap 5 − 6 = **−1**. Level 6 on Requirements raises **no** Edge marker — it is
not a high-stakes area. Infrastructure-as-code is N/A in all three passes: excluded, counted. **Security review is N/A today and 3 in six
months: no Gap, flagged** — "I don't do this work now, but I expect to"; its Stance gap (3 − 3 = 0) *does* exist because both future passes are
numeric.

**Edge markers.** No probe answered 4 or 5 on either stance; no level 6 on a high-stakes area. None.

**Safeguards.** The six-months-for-me answer ticks **"I'd read it myself" alongside "the test suite passes"** → **inconsistent (future-personal)**.
Flagged; her **Levers are not computed** (`NA`); and because the answer is inconsistent it is **not** a principle hold either. The team-should
answer (tests, rollback) counts toward the team norms. Learning interest: *schema check* and *small blast radius* — both ticked in "know more
about" and neither in her six-months list. The right next step is a two-minute conversation, not a rule.

### 8.3 What her scored row says

Current: Comfort 2.3 · Trust 2.3 · Fluency 2.3 · Guardrails 3.4 · Concern 3.4 · Autonomy 2.0 · Craft 3.3. A cautious current position with
large personal Gaps on Comfort, Trust, Fluency and Autonomy (+1.7 to +2.0), a slight pull-back on Guardrails and Concern, and a Stance gap on
Craft values of +1.0 — she thinks the team should hold a higher craft standard than she would set for herself. Nothing at an edge. One flag to
ask her about.

## 9. What this hands downstream

- **[#15](https://github.com/AndrewGodlewsky/AI-Dev-Survey/issues/15) Scoring sheet** — implements §3, §5.3 and §6 exactly; the scale table in §2 is
  the five lookup tables; Sofia's row in `scoring/scored-sample.csv` is the acceptance test.
- **[#16](https://github.com/AndrewGodlewsky/AI-Dev-Survey/issues/16) Dashboard** — owns the label tables in §2 and the level text in §4/§5 for tooltips;
  shows Concern's five facets and the G2 − G3 difference beside the means.
- **[#17](https://github.com/AndrewGodlewsky/AI-Dev-Survey/issues/17) How to read the results** — §7 is its source: decimals vs landmarks, the 0.3 rule,
  the two softer Gaps, "high is not good", markers are positions.
- **[#13](https://github.com/AndrewGodlewsky/AI-Dev-Survey/issues/13) Survey document** — the item and anchor text here must match the form verbatim;
  item text is the join key in the Forms export.
