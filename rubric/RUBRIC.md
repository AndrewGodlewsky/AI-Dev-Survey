# Rubric — scoring the AI-Dev-Survey by hand

Assembled in v1 by wayfinder ticket [#14](https://github.com/AndrewGodlewsky/AI-Dev-Survey/issues/14) (the decision trail is in the issues it
links); updated to **v2** by [#30](https://github.com/AndrewGodlewsky/AI-Dev-Survey/issues/30) (Team Dimension level text, §4.8) and
[#33](https://github.com/AndrewGodlewsky/AI-Dev-Survey/issues/33) (the personal side: the Direction section replaces Future-state, the Gap is
appetite minus practice, the symmetric Safeguard list). The machine spec the local app implements is
[`scoring/scoring-rules-v2.md`](../scoring/scoring-rules-v2.md); this document agrees with it and adds the words — everything needed to score
one person's response by hand, and to say what the numbers mean.

**Every Dimension is scored in its natural direction.** Concern 5 = most concerned; Guardrails 5 = wants the most process. Neither
is "good" or "bad". Nothing in this rubric ranks a person.

---

## 1. What gets scored, and what doesn't

| Instrument | Output | Scored? |
|---|---|---|
| **Seven personal Dimensions** — Comfort · Trust · Fluency · Guardrails · Concern · Autonomy · Craft values | Two scores each, 1–5 with decimals: **Current** and **Direction** — plus the **Gap** (Direction − Current, appetite minus practice) | Yes — §3, §4 |
| **Five Team Dimensions** — Transparency · Verification · Agent latitude · Pace · Shared practice | One **Norm score** each, 1–5 with decimals, from the single team-voice pass | Yes — §3, §4.8 |
| **Coverage** — 19 Development areas | A **profile**: one Involvement level (1–6, or N/A) per area, per pass (today · Direction). Never a single number. | Profile, not score — §5 |
| **Probe items** (5, Direction section) | **Edge markers** — a person endorsed an extreme; one per probe | Never scored — §6.1 |
| **Safeguard askings** (today · willingness · team norm, + learning) | Accepted safeguards, **Levers**, **Holds**, **Dropped**, learning interest | Never scored — §6.2 |
| **Context item** (tools matrix) | A lens for reading the rest | Never scored — §6.3 |
| **Answer patterns** (three item blocks) | **Pattern flags** — a block answered flat | Never scored — §6.4 |

## 2. The answer scales and their numbers

Microsoft Forms exports the **label**; scoring uses the **number**. These are the only six conversions.

| Scale | Used by | 1 | 2 | 3 | 4 | 5 | 6 |
|---|---|---|---|---|---|---|---|
| **Behaviour** — "How often…" | Current-state items marked **B** | Never | Rarely | Sometimes | Often | Always | — |
| **Attitude** — "How well does this describe you today?" | Current-state items marked **A** | Not at all | Slightly | Moderately | Mostly | Completely | — |
| **Desirability** — "would you want to work this way?" | Every Direction item and probe | Definitely not | Probably not | Unsure | Probably | Definitely | — |
| **Agreement** | The Team section's 24 items | Strongly disagree | Disagree | Neither agree nor disagree | Agree | Strongly agree | — |
| **Involvement level** | Coverage grid, both passes | None | Advisor | Drafter | Doer, reviewed | Doer, spot-checked | System-verified |
| **Tool use** | Context item | Never used | Tried it, not using it now | Use it occasionally | Use it regularly | — | — |

In the form itself ([#29](https://github.com/AndrewGodlewsky/AI-Dev-Survey/issues/29), `survey/SURVEY.md`) every option label is prefixed with its
number — `4 – Often`, `3 – Unsure`, `N/A – I don't do this work` — so an exported cell already shows the value to use; the words are the same.
The Involvement scale also has **N/A — I don't do this work**, which is not a number (§5.3). Dimension items have no N/A: every one is
required, and a blank is a defect, not an answer (§3, step 0).

## 3. Scoring a Dimension by hand

Do this once per Dimension, twice — for the Current answers and the Direction answers. A Team Dimension is scored the same way, once, on its Team-section answers.

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
6. **Gap.** Per person, one subtraction per Dimension, unrounded: **Gap = Direction − Current.** Appetite minus practice — positive = would
   want more of the Dimension than is practised today; negative = would pull back. Never a forecast. No other subtraction between blocks is a
   quantity: nothing pairs a personal answer with a team-voice one (the Stance gap and the norm gap died with the mirrored team block).

**Why decimals.** Rounding before subtracting manufactures movement: Current 3.4 and Direction 3.6 would round to 3 and 4, a Gap of 1 for a real
move of 0.2. Gap is the number this survey exists to produce. On a three-facet Dimension, a Gap of **0.3 is one person moving one facet a full
point — real and reportable.** Display to one decimal.

## 4. The Dimensions

Each personal Dimension below lists: its definition; the Current-state items (kind **B**/**A**, **R** = reverse-keyed) — frozen with their
section; the Direction items ([`survey/direction-items.md`](../survey/direction-items.md), **R** as marked), concrete ways of working answered
once as *would you want to work this way*; the facet map; and the level text 1–5. Level text is worded as a **position**, not an action, so the
same words read correctly as a Current score ("where I am today") and as a Direction score ("how much I'd want to work this way").

### 4.1 Comfort — willingness to use AI in my own development work

| Current | Kind | R | Item |
|---|---|---|---|
| C1 | B | | How often do you use an AI tool in your development work? |
| C2 | B | | How often do you use AI on work that ends up in production? |
| C3 | A | **R** | I'd rather work through something myself than hand any of it to AI. |

| Direction | R | Item |
|---|---|---|
| D-C1 | | AI is involved in most of the code I write, including the code that ships to production. |
| D-C2 | **R** | I work without AI for stretches at a time, by choice. |

**Facets:** C1 · C2 · C3. **Direction score** = mean(D-C1, D-C2); D-C1 covers the C1 + C2 ground, D-C2 answers C3.

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

| Direction | R | Item |
|---|---|---|
| D-T1 | | AI's answers go straight into my work; I look closely only when something seems off. |
| D-T2 | **R** | I check AI's work against the source — the docs, the code, the data — before I act on it. |

**Facets:** T1 · T2 · T3. **Direction score** = mean(D-T1, D-T2). Read T1 against T2: someone who *expects* correctness but reads every line is
saying something useful.

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

| Direction | R | Item |
|---|---|---|
| D-F1 | | I want to point AI at the right files and examples before I ask it anything. |
| D-F2 | **R** | I want to use AI tools as they come, without configuring or tuning them. |

**Facets:** F1 · F2 · F3. **Direction score** = mean(D-F1, D-F2). **F3 → D-F2 is facet-matched, not word-matched** (nobody can *want* to stay
confused, so the Direction item names a low-Fluency position someone could prefer). The Fluency Gap is one of the three that read **softer
still** (§3) — do not read it to one decimal with the same confidence.

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

| Direction | R | Facet | Item |
|---|---|---|---|
| D-G1 | | Review + testing | Anything AI helped write goes through an extra pair of eyes and an extra test before it ships. |
| D-G2 | | Disclosure | I want the commit or PR to say when AI wrote most of it. |
| D-G3 | | Off-limits areas | There are parts of my work I keep AI out of, deliberately. |
| D-G4 | | Enforcement strength | Our AI rules live in the tooling — lint, CI, hooks — not in people's heads. |
| D-G5 | **R** | The "nothing extra" pole | AI-assisted work moves through the same pipeline as everything else, with nothing added for it. |

**Facets (five):** G1 · **mean(G2, G3)** · G4 · G5 · G6; Direction D-G1 – D-G5, one item per facet. The disclosure pair collapses because
"endorsed" and "practised" are one facet that only splits in the present tense — forward it is a single item — and a flat mean over six Current
items would give disclosure a third of the score and make the Current and Direction means structurally different. The **G2 − G3 difference**
(endorsed minus practised) is worth reading on its own.

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

| Direction | R | Risk | Item |
|---|---|---|---|
| D-N1 | | Skill atrophy | I want to keep doing enough work without AI to keep my own skills sharp. |
| D-N2 | | Security | Anything AI wrote for me gets a security look before it ships. |
| D-N3 | | IP / licensing | I check AI-generated code for licensing and IP exposure before it goes in. |
| D-N4 | **R** | Maintainability | AI-written code goes into my codebase on the same terms as anything else — I give its maintainability no extra thought. |
| D-N5 | | Job impact | I want to plan around AI changing what my job is. |

**Facets (five):** one per risk, N1–N5 → D-N1–D-N5. **Read the five separately as well as the mean:** a Concern of 3 can be "mildly worried about
everything" or "alarmed about security, relaxed about the rest", and those need different responses. The Direction items are worded as *the
vigilance someone would want in force* — nobody sets a target for how worried they want to be. **N5 → D-N5 is facet-matched, not word-matched**
(an expectation has no direction form, so the item asks about planning instead); the job-impact part of Concern's Gap reads **softer still**.

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

| Direction | R | Item |
|---|---|---|
| D-A1 | | Agents change files and run commands across my project, not just in the file I have open. |
| D-A2 | **R** | AI suggests and explains; I make the actual edits myself. |

**Facets:** A1 · A2 · A3. **Direction score** = mean(D-A1, D-A2). **A2 → D-A2 is facet-matched, not word-matched** — D-A2 names the Advisor
position outright, a different point on the same leash — so Autonomy's Gap is one of the three that read **softer still**.

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

| Direction | R | Item |
|---|---|---|
| D-V1 | | I want to leave code the next person can work on without asking me. |
| D-V2 | **R** | I want to ship when it works, rather than spend more time on tests and tidying. |

**Facets:** V1 · V2 · V3. **Direction score** = mean(D-V1, D-V2). D-V2 names the speed-over-polish position outright — wantable, so this pair is
word-matched and Craft values is **not** on v2's softer-still list; like every Gap it is still the cross-scale, softer kind.

| Level | Position |
|---|---|
| 1 | Working software is what counts; understanding, tests, and review are overhead to be skipped when they slow delivery. |
| 2 | Worth having in principle, but the first thing to drop under pressure. |
| 3 | A working baseline holds — code is reviewed, reasonably tested, and understood by whoever ships it — and is traded away deliberately when the cost is high. |
| 4 | Understanding, tests, review, and ownership are non-negotiable for anything that reaches production. |
| 5 | Craft is the point: nothing ships that its author cannot explain line by line, and depth of understanding is defended even at real cost to speed. |

### 4.8 The Team Dimensions (v2)

Added by wayfinder ticket [#30](https://github.com/AndrewGodlewsky/AI-Dev-Survey/issues/30); construct decided in
[#23](https://github.com/AndrewGodlewsky/AI-Dev-Survey/issues/23) ([`survey/team-section.md`](../survey/team-section.md), items in
[`survey/team-items.md`](../survey/team-items.md)). Five Team Dimensions, measured **once**, in team voice, on the Agreement scale.
Unlike §§4.1–4.7 there is no Current/Future pair: each Respondent gets one **Norm score** per Team Dimension — the norm they would
set — and the Team score is the aggregate plus spread; spread is the finding.

**Level text is worded as the norm in force** — the way of working the team requires at that level — so the same words read
correctly as one person's Norm score (*the norm I'd set*) and as the Team score (*the norm we'd collectively set*). As everywhere
in this rubric, both ends are positions a team can hold; level 1 is never a deficiency, and the direction is a direction, not the
good direction. A two-facet Dimension gets **one level text spanning both facets**, because the number being located is the
Dimension mean; where the facets pull apart, the facet view (scoring rules v2 §facets) is the read, not the mean.

#### Transparency — how much the team requires AI's role in work to be visible and personally owned

*Facets: Disclosure & provenance · Ownership & accountability.*

| Level | Norm in force |
|---|---|
| 1 | Work is judged as work: nobody is asked to say what AI wrote, and merged code is owned the way the team owns anything — collectively, through the system that shipped it. |
| 2 | Disclosure is a courtesy, not a rule: people mention AI involvement when it seems relevant, and ownership follows the ordinary review trail. |
| 3 | AI involvement is visible at the level of the change — a PR says AI played a part — and whoever merges it answers for it; saying *which parts* is not required. |
| 4 | AI-written parts are identified within a change, and whoever merges is expected to be able to explain them. |
| 5 | Every AI contribution is labelled — which parts, produced how — and recorded beyond the PR; whoever merges owns it personally, line by line. |

#### Verification — how much human review the team requires of AI output

*Facet: Reviewing AI-assisted work (the Safeguard checklist sits here, unscored).*

| Level | Norm in force |
|---|---|
| 1 | Automated checks are the gate: when tests and CI pass, AI output can merge without any person reading it. |
| 2 | AI output gets a human glance — a skim, a spot-check of the risky parts — but the checks carry the weight; full reading is not required. |
| 3 | AI-assisted work goes through the team's normal review: a person reads it and judges it as they would any change, with no extra ceremony for its origin. |
| 4 | AI-heavy changes get deliberate extra care: the author reads the AI-written parts before asking for review, and a reviewer who didn't run the agent reads them again. |
| 5 | A human reads every line of AI output before it ships, under review at least as demanding as for human-written work; no check stands in for reading. |

#### Agent latitude — how freely agents may act in the shared codebase

*Facets: Parallel development with agents · Limits — and they run **opposite ways**: more parallel agent work is more latitude,
more limits is less. The level text spans both, so the* Limits *half runs backwards down the table (broad no-go zones at 1, none
at 5). A **flat 3 is ambiguous by construction** — indistinguishable from "agents everywhere in the day-to-day code, and nowhere
near production data", a coherent position — so the facet view is this Dimension's primary read; the mean locates nobody on its
own.*

| Level | Norm in force |
|---|---|
| 1 | Agents work in personal sandboxes only, and whole kinds of work — production data, secrets, releases, named areas — are off-limits to AI as team policy. |
| 2 | Agents may touch shared code, but only on a personal branch a person cleans up before it goes anywhere, and the off-limits list stays broad. |
| 3 | Several agents working in the shared codebase at once is normal, on branches, with a short explicit list of no-go areas still standing. |
| 4 | Agents act on shared code freely and may run against `main`; limits are a few named exclusions, not a posture of restraint. |
| 5 | Agents act anywhere in the shared codebase, including against `main`, with no standing no-go zones: what contains them is verification, not territory. |

#### Pace — how fast the team adopts, and who sets that pace

*Facet: Pace & risk appetite.*

| Level | Norm in force |
|---|---|
| 1 | The team moves at the pace of its most cautious member: nothing is adopted until everyone is ready, and evidence from elsewhere comes first. |
| 2 | Adoption is collective and deliberate: the team follows once a practice has proved itself elsewhere, and the hesitant set the schedule. |
| 3 | Individuals adopt tools for their own work as they see fit; anything team-wide waits for team agreement. |
| 4 | The keen run ahead by default: new tools are tried as they appear, and caution has to make its case tool by tool. |
| 5 | The team moves at the pace of its keenest member: it tries things first, budgets for failures, and treats waiting as the cost rather than the safety. |

#### Shared practice — how much the team invests in shared AI setup and in keeping everyone able to work without AI

*Facets: Shared conventions & tooling · Learning & skill.*

| Level | Norm in force |
|---|---|
| 1 | AI setup is personal: each person picks their own tools and instructions, and staying able to work without AI is each person's own business. |
| 2 | Conventions spread informally — a shared config here, tips at standup — but nothing is maintained on purpose, and skills look after themselves. |
| 3 | A shared baseline exists — common instruction files in the repo, agreed core tools — with personal variation on top; skill-sharing happens, unscheduled. |
| 4 | The shared setup is maintained like code and has an owner; the team deliberately teaches each other and keeps an eye on skill atrophy. |
| 5 | One shared, maintained setup is how the team works, and keeping everyone able to work without AI is an explicit, practised team investment. |

## 5. Coverage — the Involvement profile

Coverage is not a score. Per person it is **the raw Involvement level per Development area**, for each of two passes — the **today pass**
(*Current level*) and the **Direction pass** (*Direction level*: the same 19 rows asked as *where do you want AI*, with no horizon in them).
Nothing is averaged, ever: the levels are named, qualitatively different states, and
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

- **Coverage Gap** per area = Direction level − Current level, in **signed levels** (`+2`) — appetite minus practice, never a forecast.
- **A Gap exists only where both passes are numeric.** The two mixed cases are positions, not gaps, and are never silently dropped:

| Today | Direction | Reading | Rule |
|---|---|---|---|
| N/A | N/A | Not this person's work. | Excluded from the area entirely; counted. |
| level | level | Normal. | Gap = Direction − Current. |
| **N/A** | **level** | "Not my work today — but if it were, here's where AI would sit." | **No Gap** — no baseline. Counted and flagged. |
| **level** | **N/A** | "I do this today and would rather it weren't my work." | **No Gap.** Counted and flagged. |

  These are signals about how this person would have the team's work *distributed* — a wish about the work, never an adoption signal.
- **Never average across areas.** Meeting notes and Security review do not share a number; a "mean Coverage" is meaningless. That is the point of a profile.
- At team level the profile is the **distribution** (how many people at each level, per area); a median (lower middle at even n) only where one number is unavoidable, e.g. to sort areas. Team rules live in [`scoring/scoring-rules-v2.md`](../scoring/scoring-rules-v2.md) §4 and are the app's and dashboard's job, not the hand-scorer's.

## 6. The non-scoring attributes

Each sits *beside* a person's scores, never inside one. **A marker locates a position; it does not report a fault.**

### 6.1 Probe items → Edge markers

Five Direction items, indistinguishable from their neighbours, each a **present-tense world** at one **pole** of a Dimension, worded so that
**"Definitely" is always the edge**. Answered once, on the Desirability scale, like everything else in the section.

| Probe | Dimension | Pole | Item |
|---|---|---|---|
| P1 | Comfort | low | I work with no AI tooling at all, the way I worked before it existed. |
| P2 | Trust | high | I merge AI-written code I have not read line by line, as long as the tests pass. |
| P3 | Autonomy | high | I let an agent work unsupervised for an hour and only look at the final result. |
| P4 | Concern | high | I hold back on AI, because the risks outweigh what I'd gain. |
| P5 | Craft values | high | I expect to be able to explain every line of code that ships under my name. |

Rules: **never enters a Dimension mean; never reverse-keyed.** An **Edge marker** is raised when the answer is **4 or 5** — **one per
Respondent per probe**, with no per-stance states (Stance is dead). A marker locates a position at a pole; on P1 and P4 the pole is a brake
rather than an accelerator. Fluency and Guardrails carry no probe.

**Edge markers from the grid.** Involvement level **6** on one of the six high-stakes areas ◆ — Code review, CI/CD, Infrastructure-as-code,
Incident response, SQL & data migrations, Security review — also raises an Edge marker, **per pass and labelled with it**: a 6 in the today
pass is a different statement from a 6 in the Direction pass. A 6 on any other area raises nothing.

### 6.2 Safeguard askings → Levers, Holds and Dropped

One multi-select — **"For AI-written output, which of these count, for you, as enough?"** — asked three times on the identical eight-option
**symmetric list**: **today** (Current-state section), **willingness** (*would you be willing to count as enough*, Direction section) and the
**team norm** (Team section, under Verification), plus a fourth asking, **"Which of these would you want to know more about?"** (Direction
section). The options, in the form's interleaved order:

1. The test suite passes
2. A person reads all of it
3. It's easy to roll back if it's wrong
4. Another person reviews it
5. A type check or schema validation covers it
6. A person reads the risky parts
7. The blast radius is small (docs, internal tooling, non-production)
8. An automated security or lint scan covers it

Three **reading positions** (2, 4, 6) and five **checks**, equal options in no escalating order — both sides of the position are real answers,
never one escape and six alternatives. It is a **Respondent-level** attribute, not a Dimension item: the same ticks answer Trust ("is the output
right?") and Autonomy ("how long is the leash?") at once. Derived readings, all per person:

| Reading | Rule |
|---|---|
| **Lever** | A check ticked in *willingness* but **not** in *today*. What would move this person — derived by subtraction, **never asked**, because "what would have to be true?" is a threshold question the Framing rule bans. |
| **Hold** | A reading position ticked in **both** *today* and *willingness*. The line does not move — a position, not an obstacle; the symmetric twin of a Lever. |
| **Dropped** | Ticked in *today* but not in *willingness* — a pull-back. Shown, never scored. |
| **Team norm** | An option ticked in the *team* asking by at least half the team — a draft norm the team can write down. Display only; it enters no per-person reading. |
| **Learning interest** | Ticked in *know more about* but not in *willingness*. Forward-looking, free of any admission. |

**v1's inconsistency flag is retired** ([#28](https://github.com/AndrewGodlewsky/AI-Dev-Survey/issues/28)): under the symmetric *which count as
enough* stem, every tick combination is a position — *a person reads all of it* alongside *the test suite passes* says either suffices. Levers
and Holds are computed for everyone. Ticking the same boxes in today and willingness is a valid answer: the line doesn't move. Never scored into
any Dimension.

### 6.3 Context item — the tools lens

One required matrix, first in the survey: *Which of these AI tools do you use in your development work?* Rows: GitHub Copilot · Copilot Studio ·
Microsoft 365 Copilot · Azure AI Foundry · Another AI tool not on this list. Columns: the Tool-use scale (§2). **A lens, never a metric** — a
cautious Autonomy score reads differently from someone whose only exposure is inline completion than from someone running agents in Foundry.
The "another tool" row is a signal about the estate, not the person, and has no follow-up.

### 6.4 Answer patterns → Pattern flags

The reverse-keyed items only *dampen* an unread block — a flat *Probably* down a block still scores a plausible number everywhere, and a flat
*Unsure* scores 3.0 and is invisible, because `6 − 3 = 3`. So three blocks are read for a pattern, on the **raw answers, before
reverse-keying**, blanks left out:

| Block | Rows | Reverse-keyed rows |
|---|---|---|
| `current` — the 17 Attitude-scale items | C3 T1 T3 F3 G1 G2 G4 G5 G6 N1–N5 V1 V2 V3 | C3 F3 G6 N4 V2 (5) |
| `direction` — the 20 items + 5 probes | 25 rows | D-C2 D-T2 D-F2 D-G5 D-N4 D-A2 D-V2 (7) |
| `team` — the 24 team items | 24 rows | TR3 TR6 VE3 AL3 AL4 AL6 PA2 SP3 SP6 (9) |

Not read: the 9 Behaviour items, the Coverage grids, the Safeguard checklists — weak evidence, no reverse-keys, and a flat profile is a real
position. For each block find the **modal share** (the most frequent answer's share of all answered rows), then the **mode of the
non-reversed rows only** (what the person says when not reversed — if two values tie, drop 3 and take the one fewer reversed rows
sit at), and count the reverse-keyed rows answered **at that mode**. Then:

- **Flat** — raise the flag if the mode is not 3 *and* all but at most one of the reverse-keyed rows sit at the mode,
  **or** if the modal share is ≥ 0.90 whatever the mode. (At a mode of 3 the reversed rows *belong* at the mode, so that count is not evidence.)
- The **stance-identical check is retired** — no item is answered twice in v2, so there is nothing to copy.

A Pattern flag **changes no number**. It is a conversation to have before the results go upward: *"your answers follow a pattern the
reverse-keyed items don't support"* — never "you straight-lined". If the person confirms it, they re-take the block, or a human leaves
them out the way a blank would (§3 step 0). The thresholds are named constants in the app, tunable after the pilot.
Rules and rationale: [`scoring/scoring-rules-v2.md`](../scoring/scoring-rules-v2.md) §6.

## 7. Reading one person's numbers

- **The decimal is the score; the integer is a landmark.** Say "Trust 3.4 — closest to level 3: *trusts AI output on familiar, well-specified work…*",
  never "Level 3". The prose is a translation; the number is the finding.
- **A Gap of 0.3 is real** — one facet moving one point on a three-facet Dimension — and its **direction matters more than its size**. Every Gap
  is cross-scale (a Desirability answer against a Behaviour/Attitude one), so all seven are the "softer" kind, and **Fluency, Autonomy and
  Concern's job-impact facet read softer still** (§4.3, §4.5, §4.6). Appetite minus practice, never a forecast.
- **Guardrails high ≠ responsible; Concern high ≠ negative.** Both are positions. Concern's five facets are the diagnosis; the mean is the summary.
- **A Norm score is the norm that person would set** (§4.8) — a position someone holds, never a rating of the team; on a Team Dimension the
  **spread is the finding**, not the mean.
- **`#N/A` is a defect, not a result.** Recovery is a conversation, not a formula.
- **Edge markers, Levers, Holds and flags describe positions.** None of them is a fault, and none enters a score.

## 8. Worked example — Sofia Marchetti (fictional)

Sofia is invented, and the example is self-contained: every number below can be recomputed from her answers with §3's steps. (v1 kept her row
in `scoring/scored-sample.csv`; that file retires with the Excel path, and the app's tests can re-adopt her as a fixture when
[#34](https://github.com/AndrewGodlewsky/AI-Dev-Survey/issues/34) builds `score()`.) She was chosen because her response has the awkward cases:
an N/A that becomes a level, and a safeguard answer v1 would have flagged.

### 8.1 Her answers (already converted to numbers)

**Context:** GitHub Copilot 3 (occasionally) · Copilot Studio 1 (never) · M365 Copilot 4 (regularly) · Azure AI Foundry 2 (tried, stopped) · Other 1.

**Current-state items** (unchanged from v1 — the section is frozen; R = reverse-keyed; the arrow shows `6 − answer`):

| Dimension | Answers |
|---|---|
| Comfort | C1 = 3 · C2 = 2 · C3 (R) = 4 → **2** |
| Trust | T1 = 2 · T2 (R) = 3 → **3** · T3 = 2 |
| Fluency | F1 = 2 · F2 = 3 · F3 (R) = 4 → **2** |
| Guardrails | G1 = 3 · G2 = 3 · G3 = 3 · G4 = 3 · G5 = 4 · G6 (R) = 2 → **4** |
| Concern | N1 = 3 · N2 = 3 · N3 = 4 · N4 (R) = 3 → **3** · N5 = 4 |
| Autonomy | A1 = 2 · A2 (R) = 4 → **2** · A3 = 2 |
| Craft values | V1 = 3 · V2 (R) = 3 → **3** · V3 = 4 |

**Direction items** (R = reverse-keyed):

| Dimension | Answers |
|---|---|
| Comfort | D-C1 = 4 · D-C2 (R) = 2 → **4** |
| Trust | D-T1 = 4 · D-T2 (R) = 2 → **4** |
| Fluency | D-F1 = 4 · D-F2 (R) = 1 → **5** |
| Guardrails | D-G1 = 3 · D-G2 = 3 · D-G3 = 3 · D-G4 = 3 · D-G5 (R) = 3 → **3** |
| Concern | D-N1 = 2 · D-N2 = 3 · D-N3 = 3 · D-N4 (R) = 3 → **3** · D-N5 = 3 |
| Autonomy | D-A1 = 4 · D-A2 (R) = 2 → **4** |
| Craft values | D-V1 = 3 · D-V2 (R) = 3 → **3** |

**Probes:** P1 = 2 · P2 = 3 · P3 = 3 · P4 = 2 · P5 = 3.

**Coverage** (today pass / Direction pass) — the rows that matter for the example:
Requirements 4 / 6 · Writing tests 2 / 3 · Code review 2 / 3 · **Infrastructure-as-code N/A / N/A** ·
**Security review N/A / 3** · Estimates 3 / 5 · Meeting notes 3 / 5.

**Safeguards** (the symmetric eight-option list): today — *another person reviews it*. Willingness — **"a person reads all of it" and "the test
suite passes"**. Know more about — *a type check or schema validation covers it*, *the blast radius is small*.

### 8.2 Scoring

**Comfort, current.** No blanks. Reverse C3: 6 − 4 = 2. Facets 3 · 2 · 2 → mean **2.33**. Landmark 2: *"uses AI for peripheral, low-stakes
things… and keeps it away from real work."* **Direction:** reverse D-C2: 6 − 2 = 4; mean(4, 4) = **4.00**, landmark 4.
**Gap = 4.00 − 2.33 = +1.67** — a large appetite for more AI in her own work than she practises today. A direction, not a forecast.

**Guardrails, current** — the one with a collapsed facet. Reverse G6: 6 − 2 = 4. Collapse disclosure: mean(G2, G3) = mean(3, 3) = 3. Facets
3 · 3 · 3 · 4 · 4 → **3.40**. Landmark 3: *"a few explicit expectations… held by agreement."* **Direction:** one item per facet, D-G5
reversed: 6 − 3 = 3; 3 · 3 · 3 · 3 · 3 → **3.00**. **Gap = −0.40** — she'd want slightly *less* process than she has today.

**Concern, current.** Reverse N4: 6 − 3 = 3. Facets 3 · 3 · 4 · 3 · 4 → 17 / 5 = **3.40**; landmark 3. Read the five: IP/licensing and job
impact at 4 are what lift it. **Direction:** 2 · 3 · 3 · 3 · 3 → **2.80**. **Gap = −0.60**, and its job-impact facet (N5 → D-N5) is one of the
three facet-matched pairs — read that part of the move softer.

The remaining four, same procedure:

| Dimension | Current | Direction | Gap |
|---|---|---|---|
| Trust | 2 · 3 · 2 → **2.33** | 4 · 4 → **4.00** | **+1.67** |
| Fluency | 2 · 3 · 2 → **2.33** | 4 · 5 → **4.50** | **+2.17** *(softer)* |
| Autonomy | 2 · 2 · 2 → **2.00** | 4 · 4 → **4.00** | **+2.00** *(softer)* |
| Craft values | 3 · 3 · 4 → **3.33** | 3 · 3 → **3.00** | **−0.33** |

**Coverage.** Requirements 4 → 6: Coverage Gap **+2 levels** — and the 6 in the Direction pass raises **no** Edge marker, because Requirements
is not a high-stakes area. Infrastructure-as-code is N/A in both passes: excluded, counted. **Security review is N/A today and 3 in the
Direction pass: no Gap, flagged** — *"not my work today — but if it were, here's where AI would sit"* — a work-distribution wish, never an
adoption signal.

**Edge markers.** No probe answered 4 or 5; no level 6 on a high-stakes area in either pass. None.

**Safeguards.** *The test suite passes* is ticked in willingness but not today → a **Lever**. *Another person reviews it* is ticked today but
not in willingness → **Dropped**. No reading position is ticked in both askings, so there is no **Hold**. And *a person reads all of it*
alongside *the test suite passes* — the very combination v1 flagged as inconsistent — is now simply her position: either suffices
([#28](https://github.com/AndrewGodlewsky/AI-Dev-Survey/issues/28) retired the flag). Learning interest: *type/schema check* and *small blast
radius* — ticked in "know more about" and not in willingness.

### 8.3 What her scored row says

Current: Comfort 2.3 · Trust 2.3 · Fluency 2.3 · Guardrails 3.4 · Concern 3.4 · Autonomy 2.0 · Craft 3.3. A cautious current position with a
large appetite on Comfort, Trust, Fluency and Autonomy (Gaps +1.7 to +2.2, the last two softer), a slight pull-back on Guardrails, Concern and
Craft values, nothing at an edge, one staffing flag (Security review), one Lever (tests) and one Dropped safeguard (another person's review).
The Gaps say which way she'd move, not where she will be in six months.

## 9. What this hands downstream

- **[#34](https://github.com/AndrewGodlewsky/AI-Dev-Survey/issues/34) Dashboard build** — `app/serve.py`'s `score()` implements
  [`scoring/scoring-rules-v2.md`](../scoring/scoring-rules-v2.md), which this rubric agrees with; the rubric owns the level text (§4, §4.8,
  §5.1) the dashboard shows beside the numbers, and Sofia (§8) is a ready-made test case for `score()`.
- **HOW-TO-READ v2** (map fog) — §7 is its source: decimals vs landmarks, the 0.3 rule, every Gap softer and three softer still, "high is not
  good", markers are positions, spread is the finding.
- **[#29](https://github.com/AndrewGodlewsky/AI-Dev-Survey/issues/29) `survey/SURVEY.md`** — the item and anchor text here must match the form
  verbatim; item text is the join key in the Forms export.
