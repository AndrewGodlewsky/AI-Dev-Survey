# The Survey — paste-ready for Microsoft Forms

Assembled in wayfinder ticket [#13](https://github.com/AndrewGodlewsky/AI-Dev-Survey/issues/13) from
[#7](https://github.com/AndrewGodlewsky/AI-Dev-Survey/issues/7) (Context item), [#5](https://github.com/AndrewGodlewsky/AI-Dev-Survey/issues/5) / [#6](https://github.com/AndrewGodlewsky/AI-Dev-Survey/issues/6) (item banks),
[#3](https://github.com/AndrewGodlewsky/AI-Dev-Survey/issues/3) (Coverage grid), [#8](https://github.com/AndrewGodlewsky/AI-Dev-Survey/issues/8) (Probe items), [#19](https://github.com/AndrewGodlewsky/AI-Dev-Survey/issues/19) (Safeguard items),
[#10](https://github.com/AndrewGodlewsky/AI-Dev-Survey/issues/10) (Forms constraints) and [#20](https://github.com/AndrewGodlewsky/AI-Dev-Survey/issues/20) (no attention-check items). Those files stay the decision records;
**this file is the verbatim text of the form.** Every statement and option label below is the exact string Forms will export as a
column header or cell value, and the Scoring sheet ([#15](https://github.com/AndrewGodlewsky/AI-Dev-Survey/issues/15)) keys on it —
**edit wording here first, and only here.**

**Shape:** 11 sections, 15 Forms questions, **152 of the 200 question slots** (each Likert statement counts as one), ~35–40 minutes.
The **ID** column in every table is for the Scoring sheet's Items tab; it is **not** pasted into Forms.

## How to read this file

| Marker | Means |
|---|---|
| **Section** | A Forms *section* (Add new → Section). Its title and description are pasted as given; the description is the only preamble Respondents see for that block. |
| **Q** | One Forms question. Type, title, subtitle, Required and options are given; paste them exactly. |
| *Statements* / *Options* | The rows of a Likert, or the choices of a Choice question — in the order listed. Order matters for fatigue, not for scoring (the sheet resolves columns by header text). |

Five scales are used in the whole form. Option labels carry their number so the sheet can read the value off the front of the string
and never depends on exact wording ([#10](https://github.com/AndrewGodlewsky/AI-Dev-Survey/issues/10) §4):

| Scale | Options, verbatim |
|---|---|
| **Tool use** | `1 – Never used` · `2 – Tried it, not using it now` · `3 – Use it occasionally` · `4 – Use it regularly` |
| **Behaviour** | `1 – Never` · `2 – Rarely` · `3 – Sometimes` · `4 – Often` · `5 – Always` |
| **Attitude** | `1 – Not at all` · `2 – Slightly` · `3 – Moderately` · `4 – Mostly` · `5 – Completely` |
| **Desirability** | `1 – Definitely not` · `2 – Probably not` · `3 – Unsure` · `4 – Probably` · `5 – Definitely` |
| **Involvement** | `1 – None: no AI` · `2 – Advisor: AI explains, I do the work` · `3 – Drafter: AI drafts, I rework every line` · `4 – Doer, reviewed: AI does it, I review the result` · `5 – Doer, spot-checked: AI does it, I spot-check` · `6 – System-verified: AI does it, checks catch errors` · `N/A – I don't do this work` |

---

## Form title and description

**Title:** `AI-assisted development — where we are, and where we want to be`

**Description** (the intro; Forms shows it above section 1):

> This survey maps where each of us stands on AI-assisted development today, and where we would each like to be — for ourselves,
> and as a team norm — **six months from now**. It is not an assessment and there are no right answers: a cautious answer is
> as useful as a keen one, because the point is to see where we actually are before deciding where we want to go.
>
> **It takes about 35–40 minutes.** Most questions are rows on a scale. Answer on gut reaction — the first answer that fits is the
> right one; nothing here needs thinking through. Do it in one sitting if you can.
>
> **Your name is recorded.** Results are shared openly within the team: everyone who takes the survey will see everyone's
> individual answers, by name. Our manager will see the **combined team picture only** — counts, averages, ranges — never
> individual answers.
>
> The survey asks about today first, then about six months from now. For the future it asks each thing twice: what **you**
> would do, and what **the team** should adopt as a norm. Those can differ — that difference is one of the things we want to see.

---

## Section 1 — Your tools today

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

## Section 2 — Today: what you do

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

## Section 3 — Today: your work, area by area

**Section description** (paste as one block — it is the only place the level meanings and the area examples appear, so it is repeated verbatim in sections 7 and 10):

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

## Section 4 — Today: how you see it

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

## Section 5 — Today: what stands in for reading it yourself

**Section description:** `One question. Tick everything that applies to how you work today. Ticking only the first option is a complete answer.`

### Q6 · Choice · Multiple answers · Required

**Title:** `Which of these, if any, do you accept today instead of reading AI's output yourself?`

| # | ID | Option |
|---|---|---|
| 1 | safeguard.read-myself.current | I'd read it myself — nothing on this list changes that |
| 2 | safeguard.another-person.current | Another person reviews it |
| 3 | safeguard.tests.current | The test suite passes |
| 4 | safeguard.rollback.current | It's easy to roll back if it's wrong |
| 5 | safeguard.schema-check.current | A type check or schema validation covers it |
| 6 | safeguard.small-blast-radius.current | The blast radius is small (docs, internal tooling, non-production) |
| 7 | safeguard.security-scan.current | An automated security or lint scan covers it |

---

## Section 6 — In six months: for you

**Section description:** `Now six months from now, and just you. Each statement starts "In six months, I would…" — would you? Answer for yourself; the team comes later.`

### Q7 · Likert · Required

**Title:** `In six months, would you…`
**Scale:** Desirability (5 options)

| # | ID | Statement |
|---|---|---|
| 1 | FC1 | I would use AI in most development work. |
| 2 | FT1 | I would treat AI output as correct by default, checking only when something looks off. |
| 3 | FN1 | I would treat skill erosion as a real risk to watch for. |
| 4 | FG1 | I would give AI-assisted work more review and testing than hand-written work. |
| 5 | FA1 | I would let AI tools edit files and run commands directly. |
| 6 | FV1 | I would ship only code someone could walk another person through. |
| 7 | FF1 | I would be able to get what's needed out of an AI tool in a try or two. |
| 8 | P2 | I would merge AI-written code I had not read line by line, as long as the tests pass. |
| 9 | FC2 | I would use AI on work that ends up in production. |
| 10 | FN2 | I would treat security problems in AI-written code as a live risk to guard against. |
| 11 | FG2 | I would say when a change was mostly written by AI. |
| 12 | FA2 | I would approve an agent's steps as it goes rather than letting it run on. |
| 13 | FT2 | I would read AI-written code line by line before it is used. |
| 14 | FV2 | I would let speed win over polish more often than it does today. |
| 15 | P1 | I would be happy working with no AI tooling at all, the way I worked before it existed. |

### Q8 · Likert · Required

**Title:** `And in six months, would you…`
**Scale:** Desirability (5 options)

| # | ID | Statement |
|---|---|---|
| 1 | FF2 | I would routinely give AI tools proper context — the right files, rules and docs. |
| 2 | FN3 | I would treat licensing and IP exposure from AI-generated code as a live risk. |
| 3 | FG3 | I would keep parts of our work where AI isn't used at all. |
| 4 | FA3 | I would hand AI a whole task and come back to a finished change. |
| 5 | FV3 | I would hold up a change to fix something only its author would notice. |
| 6 | FT3 | I would trust AI's output about as much as a colleague's. |
| 7 | FC3 | I would keep doing things by hand rather than hand them to AI. |
| 8 | P3 | I would let an agent work unsupervised for an hour and only look at the final result. |
| 9 | FN4 | I would be relaxed about how maintainable AI-written code is. |
| 10 | FG4 | I would have whatever we agree about AI enforced by our tooling rather than left to judgement. |
| 11 | FF3 | I would use AI tools as they come out of the box, without configuring or tuning them. |
| 12 | P5 | I would expect to be able to explain every line of code that ships under my name. |
| 13 | FN5 | I would plan for AI changing what our jobs are. |
| 14 | FG5 | I would need nothing beyond our current process for AI-assisted work. |
| 15 | P4 | I would slow down how fast I adopt AI, because the risks outweigh what I'd gain. |

---

## Section 7 — In six months: your work, area by area (for you)

**Section description:** the **same block as section 3**, with the first line replaced by:
`For each area of work, pick the level you would want to be working at in six months. Pick N/A if you won't be doing that work.`
(then *The levels*, *What "AI does it" means per area* and *Four areas read the levels differently*, verbatim.)

### Q9 · Likert · Required

**Title:** `In six months — how would you want to do each of these?`
**Scale:** Involvement (7 options, N/A last)

| # | ID | Statement |
|---|---|---|
| 1 | area.requirements.future-personal | Me in 6 months: Requirements & ideation |
| 2 | area.architecture.future-personal | Me in 6 months: Architecture & design |
| 3 | area.production-code.future-personal | Me in 6 months: Writing production code |
| 4 | area.tests.future-personal | Me in 6 months: Writing tests |
| 5 | area.code-review.future-personal | Me in 6 months: Code review |
| 6 | area.debugging.future-personal | Me in 6 months: Debugging |
| 7 | area.documentation.future-personal | Me in 6 months: Documentation |
| 8 | area.refactoring.future-personal | Me in 6 months: Refactoring & legacy migration |
| 9 | area.ci-cd.future-personal | Me in 6 months: CI/CD & build configuration |
| 10 | area.infrastructure.future-personal | Me in 6 months: Infrastructure-as-code |
| 11 | area.incident-response.future-personal | Me in 6 months: Incident response & on-call |
| 12 | area.monitoring.future-personal | Me in 6 months: Monitoring & alerting |
| 13 | area.data-migrations.future-personal | Me in 6 months: SQL & data migrations |
| 14 | area.security-review.future-personal | Me in 6 months: Security review & threat modeling |
| 15 | area.dependency-upgrades.future-personal | Me in 6 months: Dependency upgrades |
| 16 | area.estimates.future-personal | Me in 6 months: Estimates & planning |
| 17 | area.stakeholder-comms.future-personal | Me in 6 months: Stakeholder comms & PR descriptions |
| 18 | area.learning.future-personal | Me in 6 months: Learning new tech |
| 19 | area.meeting-notes.future-personal | Me in 6 months: Meeting notes & summaries |

---

## Section 8 — In six months: what you would accept

**Section description:** `Same list as before, six months out, still just you. Ticking the same boxes as before is a complete answer — it says your line doesn't move.`

### Q10 · Choice · Multiple answers · Required

**Title:** `In six months, which of these would you accept instead of reading AI's output yourself?`

| # | ID | Option |
|---|---|---|
| 1 | safeguard.read-myself.future-personal | I'd read it myself — nothing on this list changes that |
| 2 | safeguard.another-person.future-personal | Another person reviews it |
| 3 | safeguard.tests.future-personal | The test suite passes |
| 4 | safeguard.rollback.future-personal | It's easy to roll back if it's wrong |
| 5 | safeguard.schema-check.future-personal | A type check or schema validation covers it |
| 6 | safeguard.small-blast-radius.future-personal | The blast radius is small (docs, internal tooling, non-production) |
| 7 | safeguard.security-scan.future-personal | An automated security or lint scan covers it |

---

## Section 9 — In six months: for the team

**Section description:** `The same statements, but now as a team norm: what should the team adopt six months from now? It is fine — and useful — for these answers to differ from your own.`

### Q11 · Likert · Required

**Title:** `In six months, should the team…`
**Scale:** Desirability (5 options)

| # | ID | Statement |
|---|---|---|
| 1 | FC1 | The team should use AI in most development work. |
| 2 | FT1 | The team should treat AI output as correct by default, checking only when something looks off. |
| 3 | FN1 | The team should treat skill erosion as a real risk to watch for. |
| 4 | FG1 | The team should give AI-assisted work more review and testing than hand-written work. |
| 5 | FA1 | The team should let AI tools edit files and run commands directly. |
| 6 | FV1 | The team should ship only code someone could walk another person through. |
| 7 | FF1 | The team should be able to get what's needed out of an AI tool in a try or two. |
| 8 | P2 | The team should merge AI-written code nobody has read line by line, as long as the tests pass. |
| 9 | FC2 | The team should use AI on work that ends up in production. |
| 10 | FN2 | The team should treat security problems in AI-written code as a live risk to guard against. |
| 11 | FG2 | The team should say when a change was mostly written by AI. |
| 12 | FA2 | The team should approve an agent's steps as it goes rather than letting it run on. |
| 13 | FT2 | The team should read AI-written code line by line before it is used. |
| 14 | FV2 | The team should let speed win over polish more often than it does today. |
| 15 | P1 | The team should be fine going back to no AI tooling at all. |

### Q12 · Likert · Required

**Title:** `And in six months, should the team…`
**Scale:** Desirability (5 options)

| # | ID | Statement |
|---|---|---|
| 1 | FF2 | The team should routinely give AI tools proper context — the right files, rules and docs. |
| 2 | FN3 | The team should treat licensing and IP exposure from AI-generated code as a live risk. |
| 3 | FG3 | The team should keep parts of our work where AI isn't used at all. |
| 4 | FA3 | The team should hand AI a whole task and come back to a finished change. |
| 5 | FV3 | The team should hold up a change to fix something only its author would notice. |
| 6 | FT3 | The team should trust AI's output about as much as a colleague's. |
| 7 | FC3 | The team should keep doing things by hand rather than hand them to AI. |
| 8 | P3 | The team should let agents work unsupervised for an hour and only review the final result. |
| 9 | FN4 | The team should be relaxed about how maintainable AI-written code is. |
| 10 | FG4 | The team should have whatever we agree about AI enforced by our tooling rather than left to judgement. |
| 11 | FF3 | The team should use AI tools as they come out of the box, without configuring or tuning them. |
| 12 | P5 | The team should expect everyone to be able to explain every line that ships under their name. |
| 13 | FN5 | The team should plan for AI changing what our jobs are. |
| 14 | FG5 | The team should need nothing beyond our current process for AI-assisted work. |
| 15 | P4 | The team should slow down how fast we adopt AI, because the risks outweigh what we'd gain. |

---

## Section 10 — In six months: the team's work, area by area

**Section description:** the **same block as section 3**, with the first line replaced by:
`For each area of work, pick the level the team should be working at in six months. Pick N/A if the team doesn't do that work.`
(then *The levels*, *What "AI does it" means per area* and *Four areas read the levels differently*, verbatim.)

### Q13 · Likert · Required

**Title:** `In six months — how should the team do each of these?`
**Scale:** Involvement (7 options, N/A last)

| # | ID | Statement |
|---|---|---|
| 1 | area.requirements.future-team | Team in 6 months: Requirements & ideation |
| 2 | area.architecture.future-team | Team in 6 months: Architecture & design |
| 3 | area.production-code.future-team | Team in 6 months: Writing production code |
| 4 | area.tests.future-team | Team in 6 months: Writing tests |
| 5 | area.code-review.future-team | Team in 6 months: Code review |
| 6 | area.debugging.future-team | Team in 6 months: Debugging |
| 7 | area.documentation.future-team | Team in 6 months: Documentation |
| 8 | area.refactoring.future-team | Team in 6 months: Refactoring & legacy migration |
| 9 | area.ci-cd.future-team | Team in 6 months: CI/CD & build configuration |
| 10 | area.infrastructure.future-team | Team in 6 months: Infrastructure-as-code |
| 11 | area.incident-response.future-team | Team in 6 months: Incident response & on-call |
| 12 | area.monitoring.future-team | Team in 6 months: Monitoring & alerting |
| 13 | area.data-migrations.future-team | Team in 6 months: SQL & data migrations |
| 14 | area.security-review.future-team | Team in 6 months: Security review & threat modeling |
| 15 | area.dependency-upgrades.future-team | Team in 6 months: Dependency upgrades |
| 16 | area.estimates.future-team | Team in 6 months: Estimates & planning |
| 17 | area.stakeholder-comms.future-team | Team in 6 months: Stakeholder comms & PR descriptions |
| 18 | area.learning.future-team | Team in 6 months: Learning new tech |
| 19 | area.meeting-notes.future-team | Team in 6 months: Meeting notes & summaries |

---

## Section 11 — In six months: what the team should accept

**Section description:** `Last two questions. The first is a team norm; the second is just curiosity — nothing on it is scored.`

### Q14 · Choice · Multiple answers · Required

**Title:** `In six months, which of these should the team accept as enough, without an individual reading the output?`

| # | ID | Option |
|---|---|---|
| 1 | safeguard.read-myself.future-team | I'd read it myself — nothing on this list changes that |
| 2 | safeguard.another-person.future-team | Another person reviews it |
| 3 | safeguard.tests.future-team | The test suite passes |
| 4 | safeguard.rollback.future-team | It's easy to roll back if it's wrong |
| 5 | safeguard.schema-check.future-team | A type check or schema validation covers it |
| 6 | safeguard.small-blast-radius.future-team | The blast radius is small (docs, internal tooling, non-production) |
| 7 | safeguard.security-scan.future-team | An automated security or lint scan covers it |

### Q15 · Choice · Multiple answers · **Not** required

**Title:** `Which of these would you want to know more about?`
**Subtitle:** `Leave it blank if none.`

| # | ID | Option |
|---|---|---|
| 1 | learn.read-myself | I'd read it myself — nothing on this list changes that |
| 2 | learn.another-person | Another person reviews it |
| 3 | learn.tests | The test suite passes |
| 4 | learn.rollback | It's easy to roll back if it's wrong |
| 5 | learn.schema-check | A type check or schema validation covers it |
| 6 | learn.small-blast-radius | The blast radius is small (docs, internal tooling, non-production) |
| 7 | learn.security-scan | An automated security or lint scan covers it |

## Thank-you message

Settings → *Customize thank you message*: `Thanks — that's everything. Results will be shared with the whole team, by name, once everyone has answered; the combined team picture goes to our manager.`

---

## Appendix A — Forms setup checklist

Build order is section order. Nothing below requires a decision; where Forms offers a choice, the answer is given.

**Settings (⋯ → Settings)**

- [ ] *Who can fill out this form*: **Only people in my organization can respond** → tick **Record name**, tick **One response per person**. (Anonymous mode empties the name column, which is the join key — [#10](https://github.com/AndrewGodlewsky/AI-Dev-Survey/issues/10) §1.)
- [ ] *Shuffle questions*: **off**. Section order is the fatigue design; shuffling would also separate a grid from its description.
- [ ] *Show progress bar*: **on**.
- [ ] *Customize thank you message*: the text above.
- [ ] *Start/end date*: set an end date two weeks out; leave start open.
- [ ] No branching anywhere.

**Per question**

| Q | Forms type | Settings |
|---|---|---|
| Q1, Q2, Q4, Q5, Q7, Q8, Q11, Q12 | **Likert** | Required. Options = the scale's labels, verbatim, in order. Statements = the table, in order. One statement per row; no blank statements left over (Forms starts with three placeholder rows — replace or delete them). |
| Q3, Q9, Q13 | **Likert** | As above with the **Involvement** scale — 7 options, `N/A – I don't do this work` last. |
| Q6, Q10, Q14 | **Choice** | ⋯ → **Multiple answers** on. Required. No "Other" option. Options verbatim. |
| Q15 | **Choice** | Multiple answers on. **Required off.** No "Other". |

**Text rules — these are what the Scoring sheet keys on**

- [ ] Every statement and option is pasted **verbatim from this file**, including the leading `1 – ` numbers and the en dash. Forms may convert straight quotes to curly ones — it does so consistently, so this is harmless.
- [ ] **No two statements anywhere in the form share the same text.** (Checked in this file: 148 statements, all unique. The three Coverage grids differ by their `Today:` / `Me in 6 months:` / `Team in 6 months:` prefix; the two Future blocks by their `I would` / `The team should` subject.)
- [ ] Section descriptions for sections 7 and 10 are the section-3 block with only the first line changed.

**Pre-flight, before the real form goes out** (the four checks [#10](https://github.com/AndrewGodlewsky/AI-Dev-Survey/issues/10) §9 could not settle by reading — a throwaway form with two answered rows of Q2, Q3 and Q6, two submissions, then *Open in Excel*):

- [ ] **Required is enforced per statement** on a Likert — a submission with one grid row blank is refused. This is what "a blank is a malformed export" ([#9](https://github.com/AndrewGodlewsky/AI-Dev-Survey/issues/9)) rests on. If it is *not* enforced per statement, tell [#15](https://github.com/AndrewGodlewsky/AI-Dev-Survey/issues/15): blanks become reachable and the malformed flag does real work.
- [ ] The Likert cells export the **full option label** (`4 – Often`, `N/A – I don't do this work`) so the sheet can read the leading number.
- [ ] Two Likert statements with identical text in different blocks are **not** merged — moot for this form (no duplicates), but confirms the uniqueness rule is the right one.
- [ ] The multi-select cell's delimiter (comma-space or semicolon) — moot if the sheet presence-tests as [#10](https://github.com/AndrewGodlewsky/AI-Dev-Survey/issues/10) §6 recommends.

**Exporting responses**

- [ ] Responses → **Open in Excel** (or ⋯ → *Sync all responses to a new workbook* if the columns look out of order — a known Forms issue, [#10](https://github.com/AndrewGodlewsky/AI-Dev-Survey/issues/10) §5).
- [ ] Save the workbook **outside this repository** — it is named data. `.gitignore` blocks `scoring/*.csv`, but the Forms export is an `.xlsx`; keep it in the team's SharePoint, not the clone.

## Appendix B — Count

| Block | Forms questions | Question slots |
|---|---|---|
| Section 1 — tools matrix | 1 | 5 |
| Section 2 — behaviour items | 1 | 9 |
| Section 3 — Coverage, today | 1 | 19 |
| Section 4 — attitude items | 2 | 17 |
| Section 5 — Safeguard, today | 1 | 1 |
| Section 6 — Future, for me | 2 | 30 |
| Section 7 — Coverage, me in 6 months | 1 | 19 |
| Section 8 — Safeguard, me in 6 months | 1 | 1 |
| Section 9 — Future, the team | 2 | 30 |
| Section 10 — Coverage, team in 6 months | 1 | 19 |
| Section 11 — Safeguards, team + know more | 2 | 2 |
| **Total** | **15** | **152 of 200** |

The type alternates all the way down — matrix, scale, grid, scale, tick-list, scale, grid, tick-list, scale, grid, tick-list — so no two consecutive sections ask the same kind of question, and no Likert exceeds 19 rows. Straight-lining is not guarded by any item ([#20](https://github.com/AndrewGodlewsky/AI-Dev-Survey/issues/20)): the Scoring sheet reads the pattern instead.

## What this hands downstream

- **[#15](https://github.com/AndrewGodlewsky/AI-Dev-Survey/issues/15) Scoring sheet** — the Items tab is the ID ↔ Statement tables above, verbatim; option labels start with their number, so `VALUE(LEFT(cell, 1))` reads the value and `N/A` reads as `NA`; multi-selects are presence-tested per option text; Q15 blank = no interest, not malformed.
- **[#18](https://github.com/AndrewGodlewsky/AI-Dev-Survey/issues/18) Pilot** — run the pre-flight checks first; time the two pilot Respondents per section; watch C1/C2, T1/T3, A1/A3 for pairs that never diverge, N5 for guarded answers, FF3/FV2 for flooring, and whether the section-3 description is read or skipped.
