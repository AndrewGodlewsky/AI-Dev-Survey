# The Survey (v2) — paste-ready for Microsoft Forms

Assembled in wayfinder ticket [#29](https://github.com/AndrewGodlewsky/AI-Dev-Survey/issues/29) from the frozen
[`current-state-items.md`](current-state-items.md) and [`coverage-grid.md`](coverage-grid.md) today pass,
the [`direction-items.md`](direction-items.md) bank ([#32](https://github.com/AndrewGodlewsky/AI-Dev-Survey/issues/32)),
the [`team-items.md`](team-items.md) bank ([#31](https://github.com/AndrewGodlewsky/AI-Dev-Survey/issues/31)),
and the [Direction pass](coverage-grid.md#the-direction-pass) ([#25](https://github.com/AndrewGodlewsky/AI-Dev-Survey/issues/25)).
Every piece of copy below is checked against the [Framing rule](item-framing-rule.md)'s point 2
(*everything the Respondent reads*). Those files stay the decision records; **this file is the
verbatim text of the form.** Every statement and option label below is the exact string Forms
will export as a column header or cell value, and the app
([#34](https://github.com/AndrewGodlewsky/AI-Dev-Survey/issues/34)) keys on it —
**edit wording here first, and only here.** It replaces v1's assembled document
([#13](https://github.com/AndrewGodlewsky/AI-Dev-Survey/issues/13)); v1's text survives inside
this file wherever a section is marked *frozen*.

**Shape:** 9 sections, 14 Forms questions, **122 of the 200 question slots** (each Likert
statement counts as one; each Choice question counts as one), **about 30 minutes**.
The **ID** column in every table is for the app's items map; it is **not** pasted into Forms.

## How to read this file

| Marker | Means |
|---|---|
| **Section** | A Forms *section* (Add new → Section). Its title and description are pasted as given; the description is the only preamble Respondents see for that block. |
| **Q** | One Forms question. Type, title, subtitle, Required and options are given; paste them exactly. |
| *Statements* / *Options* | The rows of a Likert, or the choices of a Choice question — in the order listed. Order matters for fatigue and for the two placement constraints below, not for scoring (the app resolves columns by header text). |

Placement is deliberate in three places ([#31](https://github.com/AndrewGodlewsky/AI-Dev-Survey/issues/31)/[#32](https://github.com/AndrewGodlewsky/AI-Dev-Survey/issues/32) resolution):
**D-G1 and D-G5** (near-inverse wordings) sit in different Direction blocks; **P2 and VE3**
(the same proposition as a personal edge and a team norm) sit four sections apart; and the five
probes are interleaved among ordinary rows, never adjacent to their own Dimension's items.

Five scales are used in the whole form. Option labels carry their number so the app can read
the value off the front of the string and never depends on exact wording:

| Scale | Options, verbatim |
|---|---|
| **Tool use** | `1 – Never used` · `2 – Tried it, not using it now` · `3 – Use it occasionally` · `4 – Use it regularly` |
| **Behaviour** | `1 – Never` · `2 – Rarely` · `3 – Sometimes` · `4 – Often` · `5 – Always` |
| **Attitude** | `1 – Not at all` · `2 – Slightly` · `3 – Moderately` · `4 – Mostly` · `5 – Completely` |
| **Desirability** | `1 – Definitely not` · `2 – Probably not` · `3 – Unsure` · `4 – Probably` · `5 – Definitely` |
| **Agreement** | `1 – Strongly disagree` · `2 – Disagree` · `3 – Neither agree nor disagree` · `4 – Agree` · `5 – Strongly agree` |
| **Involvement** | `1 – None: no AI` · `2 – Advisor: AI explains, I do the work` · `3 – Drafter: AI drafts, I rework every line` · `4 – Doer, reviewed: AI does it, I review the result` · `5 – Doer, spot-checked: AI does it, I spot-check` · `6 – System-verified: AI does it, checks catch errors` · `N/A – I don't do this work` |

---

## Form title and description

**Title:** `AI-assisted development — where we are, and where we want to be`

**Description** (the intro; Forms shows it above section 1):

> This survey maps where each of us stands on AI-assisted development today, which ways of
> working each of us would want, and what we should require of ourselves as a team. It is not
> an assessment and there are no right answers: a cautious answer is as useful as a keen one,
> because the point is to see where we actually are before deciding anything.
>
> **It takes about 30 minutes.** Most questions are rows on a scale. Answer on gut reaction —
> the first answer that fits is the right one; nothing here needs thinking through. Do it in
> one sitting if you can.
>
> **Your name is recorded.** Results are shared openly within the team: everyone who takes the
> survey will see everyone's answers, by name. Nothing leaves the team as a file — anything
> shared beyond the team is a screenshot of the team-level picture we choose together.
>
> The survey asks about today first, then about ways of working you would or wouldn't want,
> then about the team. Personal answers and team answers can differ — that difference is one of
> the things we want to see.

---

## Section 1 — Your tools today *(frozen, v1 §1)*

**Section description:** `A warm-up. This is about enablement, not compliance — we're mapping what the team actually reaches for so we know what to support. There is no wrong answer, including "never used".`

### Q1 · Likert · Required

**Title:** `Which of these AI tools do you use in your development work?`
**Scale:** Tool use (4 options)

| # | ID | Statement |
|---|---|---|
| 1 | tool.copilot | GitHub Copilot |
| 2 | tool.copilot-studio | Copilot Studio |
| 3 | tool.m365-copilot | Microsoft 365 Copilot |
| 4 | tool.azure-ai-foundry | Azure AI Foundry |
| 5 | tool.other-tool | Another AI tool not on this list |

---

## Section 2 — Today: what you do *(frozen, v1 §2)*

**Section description:** `How you actually work today. Answer with what happens, not what you think should happen.`

### Q2 · Likert · Required

**Title:** `How often do you…`
**Subtitle:** `Think about a typical few weeks of your own development work.`
**Scale:** Behaviour (5 options)

| # | ID | Statement |
|---|---|---|
| 1 | C1 | How often do you use an AI tool in your development work? |
| 2 | F1 | How often do you get a usable result from an AI tool within a try or two? |
| 3 | A1 | How often do you let an AI tool edit files or run commands in your project? |
| 4 | T2 | How often do you read AI-written code line by line before you use it? |
| 5 | G3 | How often do you tell people a change was mostly written by AI? |
| 6 | C2 | How often do you use AI on work that ends up in production? |
| 7 | A3 | How often do you hand AI a whole task and come back to a finished change? |
| 8 | F2 | How often do you deliberately give an AI tool context — pointing it at the right files, rules, or docs? |
| 9 | A2 | How often do you approve an agent's steps as it goes, rather than letting it run on? |

---

## Section 3 — Today: your work, area by area *(frozen, v1 §3)*

**Section description** (paste as one block — it is the only place the level meanings and the area examples appear, so it is repeated verbatim in section 7 with only the first line changed):

> For each area of work, pick the level that best describes **how you do it today**. Pick **N/A** if you don't do that work.
>
> **The levels.** 1 None — I do this without AI. 2 Advisor — AI explains, looks things up or suggests; every artifact is mine.
> 3 Drafter — AI produces a first draft; I read and edit all of it. 4 Doer, reviewed — AI produces the finished artifact; I review it
> as I would a colleague's work. 5 Doer, spot-checked — AI produces it; I sample or skim rather than review fully.
> 6 System-verified — AI produces it end-to-end; nobody looks unless automated checks (tests, CI, policy gates, monitors) fail.
>
> **What "AI does it" means per area.** Requirements & ideation — turns a rough ask into user stories / acceptance criteria.
> Architecture & design — proposes the design, component boundaries and trade-offs. Writing production code — writes the feature
> code. Writing tests — writes the unit/integration tests. Debugging — finds the root cause and writes the fix. Documentation —
> writes READMEs, ADRs, API docs, comments. Refactoring & legacy migration — performs the refactor / migration across the codebase.
> CI/CD & build configuration — writes/changes pipelines and build files. Infrastructure-as-code — writes Terraform/Bicep/etc. and
> applies changes. Monitoring & alerting — defines dashboards/alerts and triages alerts. SQL & data migrations — writes the
> migration and the data backfill. Dependency upgrades — bumps versions and resolves breaking changes. Estimates & planning —
> breaks work down and sizes it. Stakeholder comms & PR descriptions — writes the update / PR description. Meeting notes &
> summaries — transcribes and summarizes.
>
> **Four areas read the levels differently:**
> **Code review** (the work is reviewing): 1 I review PRs without AI · 2 AI explains the diff or answers my questions; I write every
> review comment · 3 AI drafts review comments; I rewrite them before posting · 4 AI posts its review; I still read the whole diff
> and add or veto comments · 5 AI posts its review; I skim the diff and its findings · 6 AI review is the merge gate; no human
> reviewer unless it flags something.
> **Incident response & on-call** (acting in production): 1 I handle incidents without AI · 2 AI helps me read logs/errors and
> suggests hypotheses; I do everything · 3 AI proposes a diagnosis and a fix; I verify the diagnosis and rewrite the fix myself ·
> 4 AI diagnoses and prepares the remediation; I review and execute it · 5 AI executes the remediation; I spot-check afterwards ·
> 6 AI auto-remediates; monitors and rollback guards catch mistakes, no human in the loop.
> **Security review & threat modeling:** 1 I do security review without AI · 2 AI explains vulnerability classes or a specific
> finding; I do the review · 3 AI drafts a threat model / findings list; I re-derive and rewrite it · 4 AI produces the findings;
> I review each finding and the code it points at · 5 AI produces the findings; I spot-check the high-severity ones · 6 AI security
> gates in CI decide; no human security review unless a gate fails.
> **Learning new tech** (the work is my understanding): 1 I learn from docs, books and people; no AI · 2 AI answers questions while
> I work through the material myself · 3 AI builds me a tailored tutorial or example; I work through and verify all of it ·
> 4 AI summarizes the tech and I rely on the summary after checking key claims · 5 AI summarizes; I skim and trust it ·
> 6 I don't learn it — AI applies the tech for me and checks catch errors.

### Q3 · Likert · Required

**Title:** `Today — how do you do each of these?`
**Scale:** Involvement (7 options, N/A last)

| # | ID | Statement |
|---|---|---|
| 1 | area.requirements.current | Today: Requirements & ideation |
| 2 | area.architecture.current | Today: Architecture & design |
| 3 | area.production-code.current | Today: Writing production code |
| 4 | area.tests.current | Today: Writing tests |
| 5 | area.code-review.current | Today: Code review |
| 6 | area.debugging.current | Today: Debugging |
| 7 | area.documentation.current | Today: Documentation |
| 8 | area.refactoring.current | Today: Refactoring & legacy migration |
| 9 | area.ci-cd.current | Today: CI/CD & build configuration |
| 10 | area.infrastructure.current | Today: Infrastructure-as-code |
| 11 | area.incident-response.current | Today: Incident response & on-call |
| 12 | area.monitoring.current | Today: Monitoring & alerting |
| 13 | area.data-migrations.current | Today: SQL & data migrations |
| 14 | area.security-review.current | Today: Security review & threat modeling |
| 15 | area.dependency-upgrades.current | Today: Dependency upgrades |
| 16 | area.estimates.current | Today: Estimates & planning |
| 17 | area.stakeholder-comms.current | Today: Stakeholder comms & PR descriptions |
| 18 | area.learning.current | Today: Learning new tech |
| 19 | area.meeting-notes.current | Today: Meeting notes & summaries |

---

## Section 4 — Today: how you see it *(frozen, v1 §4)*

**Section description:** `Now how you think and feel about it — today, not in principle. "Describes me" means describes you as you are now.`

### Q4 · Likert · Required

**Title:** `How well does each of these describe you today?`
**Scale:** Attitude (5 options)

| # | ID | Statement |
|---|---|---|
| 1 | T1 | I expect code an AI writes for me to be correct. |
| 2 | N1 | I worry that leaning on AI will erode my own skills. |
| 3 | G1 | AI-assisted work needs more review and testing than work someone wrote by hand. |
| 4 | V1 | Code I ship should be something I could walk someone else through. |
| 5 | C3 | I'd rather work through something myself than hand any of it to AI. |
| 6 | N2 | AI-written code could introduce security problems we wouldn't catch. |
| 7 | G2 | People should say when a change was mostly written by AI. |
| 8 | F3 | When an AI tool doesn't give me what I need, I'm not sure what to change. |
| 9 | N3 | Using AI-generated code could create licensing or IP problems for us. |

### Q5 · Likert · Required

**Title:** `And these — how well do they describe you today?`
**Scale:** Attitude (5 options)

| # | ID | Statement |
|---|---|---|
| 1 | V2 | When a deadline is tight, tests and review are the first things I drop. |
| 2 | G4 | There should be parts of our work where AI isn't used at all. |
| 3 | N4 | Code we write with AI will be just as maintainable as anything else we write. |
| 4 | T3 | I trust AI's output about as much as I'd trust a colleague's. |
| 5 | G5 | Whatever we agree about AI use should be enforced by our tooling, not left to judgement. |
| 6 | N5 | I expect AI to change what my job is within a few years. |
| 7 | V3 | I'd hold up my own change to fix something only I would notice. |
| 8 | G6 | Our current process already covers AI-assisted work; it needs nothing extra. |

---

## Section 5 — Today: what counts as enough

**Section description:** `One question about AI-written output. Tick everything that applies to how you work today — any combination is a complete answer.`

> The stem and the eight-option symmetric list replace v1's Safeguard asking, per
> [#32](https://github.com/AndrewGodlewsky/AI-Dev-Survey/issues/32) Q6 — ruled on record: the
> freeze covers the 26 scored items and the Coverage today pass, and this asking is neither.
> The order is interleaved on purpose (reading positions at 2, 4 and 6) and is identical in all
> three askings, because Levers and Holds are subtractions and need identical sides.

### Q6 · Choice · Multiple answers · Required

**Title:** `For AI-written output, which of these count, for you, as enough today?`

| # | ID | Option |
|---|---|---|
| 1 | safeguard.tests.current | The test suite passes |
| 2 | safeguard.read-all.current | A person reads all of it |
| 3 | safeguard.rollback.current | It's easy to roll back if it's wrong |
| 4 | safeguard.another-person.current | Another person reviews it |
| 5 | safeguard.schema-check.current | A type check or schema validation covers it |
| 6 | safeguard.read-risky.current | A person reads the risky parts |
| 7 | safeguard.small-blast-radius.current | The blast radius is small (docs, internal tooling, non-production) |
| 8 | safeguard.security-scan.current | An automated security or lint scan covers it |

---

## Section 6 — Ways of working: would you want them?

**Section description** (the Direction section description, [#32](https://github.com/AndrewGodlewsky/AI-Dev-Survey/issues/32); the horizon is named here, once, and appears in no item):

> This section describes concrete ways of working. Each one is written as if it were already
> how things are.
>
> For each, answer one question: **if this were true, how would you feel about working this
> way?**
>
> None of these is a prediction and none is a recommendation. Some describe a great deal of AI
> in the work, some describe very little, and both are real answers. There is no right column.
>
> Some of these describe how a team works rather than something you do alone. Answer those the
> same way: as a world you would or would not want to work in.
>
> We use the answers to plan the next six months.

### Q7 · Likert · Required

**Title:** `Would you want to work this way?`
**Scale:** Desirability (5 options)

| # | ID | Statement |
|---|---|---|
| 1 | D-C1 | AI is involved in most of the code I write, including the code that ships to production. |
| 2 | D-T1 | AI's answers go straight into my work; I look closely only when something seems off. |
| 3 | D-N1 | I want to keep doing enough work without AI to keep my own skills sharp. |
| 4 | D-G1 | Anything AI helped write goes through an extra pair of eyes and an extra test before it ships. |
| 5 | D-A2 | AI suggests and explains; I make the actual edits myself. |
| 6 | D-V1 | I want to leave code the next person can work on without asking me. |
| 7 | P1 | I work with no AI tooling at all, the way I worked before it existed. |
| 8 | D-F1 | I want to point AI at the right files and examples before I ask it anything. |
| 9 | D-N4 | AI-written code goes into my codebase on the same terms as anything else — I give its maintainability no extra thought. |
| 10 | D-G2 | I want the commit or PR to say when AI wrote most of it. |
| 11 | P2 | I merge AI-written code I have not read line by line, as long as the tests pass. |
| 12 | D-C2 | I work without AI for stretches at a time, by choice. |
| 13 | D-N3 | I check AI-generated code for licensing and IP exposure before it goes in. |

---

## Section 7 — Where do you want AI on each of these?

**Section description:** the **same block as section 3**, with the first line replaced by:
`For each area of work, pick the level you want AI at. Pick N/A if this isn't your work.`
(then *The levels*, *What "AI does it" means per area* and *Four areas read the levels differently*, verbatim. Per [#25](https://github.com/AndrewGodlewsky/AI-Dev-Survey/issues/25), no horizon appears anywhere in this section.)

### Q8 · Likert · Required

**Title:** `Where do you want AI on each of these?`
**Scale:** Involvement (7 options, N/A last)

| # | ID | Statement |
|---|---|---|
| 1 | area.requirements.direction | Where I want AI: Requirements & ideation |
| 2 | area.architecture.direction | Where I want AI: Architecture & design |
| 3 | area.production-code.direction | Where I want AI: Writing production code |
| 4 | area.tests.direction | Where I want AI: Writing tests |
| 5 | area.code-review.direction | Where I want AI: Code review |
| 6 | area.debugging.direction | Where I want AI: Debugging |
| 7 | area.documentation.direction | Where I want AI: Documentation |
| 8 | area.refactoring.direction | Where I want AI: Refactoring & legacy migration |
| 9 | area.ci-cd.direction | Where I want AI: CI/CD & build configuration |
| 10 | area.infrastructure.direction | Where I want AI: Infrastructure-as-code |
| 11 | area.incident-response.direction | Where I want AI: Incident response & on-call |
| 12 | area.monitoring.direction | Where I want AI: Monitoring & alerting |
| 13 | area.data-migrations.direction | Where I want AI: SQL & data migrations |
| 14 | area.security-review.direction | Where I want AI: Security review & threat modeling |
| 15 | area.dependency-upgrades.direction | Where I want AI: Dependency upgrades |
| 16 | area.estimates.direction | Where I want AI: Estimates & planning |
| 17 | area.stakeholder-comms.direction | Where I want AI: Stakeholder comms & PR descriptions |
| 18 | area.learning.direction | Where I want AI: Learning new tech |
| 19 | area.meeting-notes.direction | Where I want AI: Meeting notes & summaries |

---

## Section 8 — Ways of working, continued

**Section description:** `More ways of working, answered the same way. Then two quick tick-lists — ticking the same boxes as earlier is a complete answer.`

### Q9 · Likert · Required

**Title:** `And these — would you want to work this way?`
**Scale:** Desirability (5 options)

| # | ID | Statement |
|---|---|---|
| 1 | D-F2 | I want to use AI tools as they come, without configuring or tuning them. |
| 2 | D-A1 | Agents change files and run commands across my project, not just in the file I have open. |
| 3 | D-G3 | There are parts of my work I keep AI out of, deliberately. |
| 4 | D-N2 | Anything AI wrote for me gets a security look before it ships. |
| 5 | P3 | I let an agent work unsupervised for an hour and only look at the final result. |
| 6 | D-T2 | I check AI's work against the source — the docs, the code, the data — before I act on it. |
| 7 | D-G4 | Our AI rules live in the tooling — lint, CI, hooks — not in people's heads. |
| 8 | P4 | I hold back on AI, because the risks outweigh what I'd gain. |
| 9 | D-V2 | I want to ship when it works, rather than spend more time on tests and tidying. |
| 10 | D-N5 | I want to plan around AI changing what my job is. |
| 11 | D-G5 | AI-assisted work moves through the same pipeline as everything else, with nothing added for it. |
| 12 | P5 | I expect to be able to explain every line of code that ships under my name. |

### Q10 · Choice · Multiple answers · Required

**Title:** `For AI-written output, which of these would you be willing to count as enough?`

| # | ID | Option |
|---|---|---|
| 1 | safeguard.tests.direction | The test suite passes |
| 2 | safeguard.read-all.direction | A person reads all of it |
| 3 | safeguard.rollback.direction | It's easy to roll back if it's wrong |
| 4 | safeguard.another-person.direction | Another person reviews it |
| 5 | safeguard.schema-check.direction | A type check or schema validation covers it |
| 6 | safeguard.read-risky.direction | A person reads the risky parts |
| 7 | safeguard.small-blast-radius.direction | The blast radius is small (docs, internal tooling, non-production) |
| 8 | safeguard.security-scan.direction | An automated security or lint scan covers it |

### Q11 · Choice · Multiple answers · **Not** required

**Title:** `Which of these would you want to know more about?`
**Subtitle:** `Leave it blank if none.`

| # | ID | Option |
|---|---|---|
| 1 | learn.tests | The test suite passes |
| 2 | learn.read-all | A person reads all of it |
| 3 | learn.rollback | It's easy to roll back if it's wrong |
| 4 | learn.another-person | Another person reviews it |
| 5 | learn.schema-check | A type check or schema validation covers it |
| 6 | learn.read-risky | A person reads the risky parts |
| 7 | learn.small-blast-radius | The blast radius is small (docs, internal tooling, non-production) |
| 8 | learn.security-scan | An automated security or lint scan covers it |

---

## Section 9 — The team

**Section description** (the Team section description, [#31](https://github.com/AndrewGodlewsky/AI-Dev-Survey/issues/31)):

> This section is about how we work as a team — not about you.
>
> Each statement is a norm somebody could propose for this team. Say how much you agree with it.
>
> There is no house position. Some statements ask for more process, some for less, and both are
> real answers. We are looking for where we already agree and where we don't.

### Q12 · Likert · Required

**Title:** `How much do you agree?`
**Scale:** Agreement (5 options)

| # | ID | Statement |
|---|---|---|
| 1 | TR1 | It should be clear which *parts* of a change AI wrote, not just that AI was involved. |
| 2 | PA1 | The team should try new AI tools as they come out, rather than waiting to see how they land elsewhere. |
| 3 | AL3 | Agent work should stay on a personal branch until a person has cleaned it up. |
| 4 | SP1 | The team should keep one shared set of AI instruction files in the repo, maintained like any other code. |
| 5 | VE1 | A pull request that AI mostly wrote should be reviewed by someone who didn't run the agent. |
| 6 | TR6 | When AI-written code causes a problem, that is a tooling failure rather than anyone's mistake. |
| 7 | AL4 | Some kinds of work here — production data, secrets, releases — should be off-limits to AI as a matter of policy. |
| 8 | SP4 | The team should make time to teach each other how we use AI tools. |
| 9 | PA2 | The team should move at the pace of whoever is most cautious about AI. |
| 10 | TR4 | Whoever merges a change owns it, whatever wrote it. |
| 11 | AL2 | Agents should be free to touch shared code, not only the files one person is working in. |
| 12 | VE2 | Before asking for review, the author should have read the AI-written parts themselves. |

### Q13 · Likert · Required

**Title:** `And these — how much do you agree?`
**Scale:** Agreement (5 options)

| # | ID | Statement |
|---|---|---|
| 1 | SP2 | The team should agree on which AI tools we use, rather than each person choosing. |
| 2 | AL1 | It should be normal here for several people to have agents working in the codebase at the same time. |
| 3 | TR2 | The team should keep a record of which changes were AI-assisted, beyond the pull request itself. |
| 4 | PA3 | Anyone here should be able to adopt an AI tool for their own work without the team agreeing to it first. |
| 5 | VE3 | If the automated checks pass, a change is good enough to merge without anyone reading it. |
| 6 | SP5 | The team should deliberately keep everyone able to do the work without AI. |
| 7 | AL5 | Agents should be able to run against `main`, not only against a branch. |
| 8 | TR3 | What matters is whether a change is right, not how it was produced. |
| 9 | SP3 | Time spent maintaining shared AI setup is time not spent shipping. |
| 10 | AL6 | An agent should need a person's approval before it changes anything outside the task it was given. |
| 11 | TR5 | Someone on the team should be able to explain any AI-written change that ships. |
| 12 | SP6 | Keeping your own skills current is each person's responsibility, not the team's. |

### Q14 · Choice · Multiple answers · Required

**Title:** `For AI-written output, which of these should count, for this team, as enough?`

| # | ID | Option |
|---|---|---|
| 1 | safeguard.tests.team | The test suite passes |
| 2 | safeguard.read-all.team | A person reads all of it |
| 3 | safeguard.rollback.team | It's easy to roll back if it's wrong |
| 4 | safeguard.another-person.team | Another person reviews it |
| 5 | safeguard.schema-check.team | A type check or schema validation covers it |
| 6 | safeguard.read-risky.team | A person reads the risky parts |
| 7 | safeguard.small-blast-radius.team | The blast radius is small (docs, internal tooling, non-production) |
| 8 | safeguard.security-scan.team | An automated security or lint scan covers it |

## Thank-you message

Settings → *Customize thank you message*: `Thanks — that's everything. Results are shared with the whole team, by name, once everyone has answered.`

---

## Appendix A — Forms setup checklist

Build order is section order. Nothing below requires a decision; where Forms offers a choice, the answer is given.

**Settings (⋯ → Settings)**

- [ ] *Who can fill out this form*: **Only people in my organization can respond** → tick **Record name**, tick **One response per person**. (Anonymous mode empties the name column, which is the join key.)
- [ ] *Shuffle questions*: **off**. Section order is the fatigue design and carries the placement constraints; shuffling would also separate a grid from its description.
- [ ] *Show progress bar*: **on**.
- [ ] *Customize thank you message*: the text above.
- [ ] *Start/end date*: set an end date two weeks out; leave start open.
- [ ] No branching anywhere.

**Per question**

| Q | Forms type | Settings |
|---|---|---|
| Q1, Q2, Q4, Q5, Q7, Q9 | **Likert** | Required. Options = the scale's labels, verbatim, in order. Statements = the table, in order. One statement per row; no blank statements left over (Forms starts with three placeholder rows — replace or delete them). |
| Q12, Q13 | **Likert** | As above with the **Agreement** scale. |
| Q3, Q8 | **Likert** | As above with the **Involvement** scale — 7 options, `N/A – I don't do this work` last. |
| Q6, Q10, Q14 | **Choice** | ⋯ → **Multiple answers** on. Required. No "Other" option. Options verbatim, in the interleaved order given — identical across the three askings. |
| Q11 | **Choice** | Multiple answers on. **Required off.** No "Other". |

**Text rules — these are what the app keys on**

- [ ] Every statement and option is pasted **verbatim from this file**, including the leading `1 – ` numbers and the en dash. Forms may convert straight quotes to curly ones — it does so consistently, so this is harmless.
- [ ] **No two statements anywhere in the form share the same text.** (Checked in this file: 118 Likert statements, all unique. The two Coverage passes differ by their `Today:` / `Where I want AI:` prefix.)
- [ ] Section 7's description is the section-3 block with only the first line changed.
- [ ] The three Safeguard askings and the know-more list use the **same eight option texts in the same order**.

**Pre-flight, before the real form goes out** (a throwaway form with two answered rows of Q2, Q3 and Q6, two submissions, then *Open in Excel*):

- [ ] **Required is enforced per statement** on a Likert — a submission with one grid row blank is refused. This is what "a blank is a malformed export" (scoring-rules-v2 §1.4) rests on. If it is *not* enforced per statement, tell [#34](https://github.com/AndrewGodlewsky/AI-Dev-Survey/issues/34): blanks become reachable and the malformed flag does real work.
- [ ] The Likert cells export the **full option label** (`4 – Often`, `N/A – I don't do this work`) so the app can read the leading number.
- [ ] The multi-select cell's delimiter (comma-space or semicolon) — the app presence-tests per option text, so either works; confirm nothing truncates.

**Exporting responses**

- [ ] Responses → **Open in Excel** (or ⋯ → *Sync all responses to a new workbook* if the columns look out of order — a known Forms issue; the app resolves by header text either way).
- [ ] Save the workbook into the repo's **`data/` folder** — it is gitignored and the pre-commit guard blocks it from ever being committed ([#27](https://github.com/AndrewGodlewsky/AI-Dev-Survey/issues/27)). Then `python app/serve.py`.

## Appendix B — Count

| Block | Forms questions | Question slots |
|---|---|---|
| Section 1 — tools matrix | 1 | 5 |
| Section 2 — behaviour items | 1 | 9 |
| Section 3 — Coverage, today | 1 | 19 |
| Section 4 — attitude items | 2 | 17 |
| Section 5 — Safeguard, today | 1 | 1 |
| Section 6 — Direction, part 1 | 1 | 13 |
| Section 7 — Coverage, Direction pass | 1 | 19 |
| Section 8 — Direction, part 2 + Safeguard + know-more | 3 | 12 + 1 + 1 |
| Section 9 — Team + Safeguard norm | 3 | 24 + 1 |
| **Total** | **14** | **122 of 200** |

Down from v1's 152: the mirrored team block (−30 −19 −1), plus the Team section's own +24 +1,
and one Coverage pass fewer. The type still alternates — matrix, scale, grid, scale, tick-list,
scale, grid, scale, tick-lists, scale, tick-list — no Likert exceeds 19 rows, and the largest
new block (25 Direction rows) is split 13 + 12 around the Coverage Direction pass, which also
puts the required distance between **D-G1** (Q7 row 4) and **D-G5** (Q9 row 11). **P2** (Q7
row 11) and **VE3** (Q13 row 5) sit four sections apart. Straight-lining is not guarded by any
item: the app reads the pattern instead (scoring-rules-v2 §6).

## What this hands downstream

- **[#34](https://github.com/AndrewGodlewsky/AI-Dev-Survey/issues/34) App** — the ID ↔ Statement tables above are the items map `score()` keys on, verbatim; option labels start with their number; multi-selects are presence-tested per option text; Q11 blank = no interest, not malformed.
- **Pilot v2** (map fog) — run the pre-flight checks first; time the pilot per section; the watch list from [#31](https://github.com/AndrewGodlewsky/AI-Dev-Survey/issues/31)/[#32](https://github.com/AndrewGodlewsky/AI-Dev-Survey/issues/32): Fluency (thinnest Dimension), D-G1/D-G5 answered as a pair, VE3 vs P2 divergence, and whether the section-6 description is read or skipped.
- **[`docs/SETUP.html`](../docs/SETUP.html)** — updated for the v2 pipeline alongside this file.
