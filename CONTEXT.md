# AI-Dev-Survey — Domain Glossary

Ubiquitous language for the team AI-adoption survey and its rubric. Glossary only; no implementation detail.

## Core terms

- **Survey** — The questionnaire each team member completes. Split into a *Current-state section* and a *Future-state section*, which ask different questions but score the same Dimensions.
- **Respondent** — A named team member answering the Survey. Responses are not anonymous; results are shared openly within the team.
- **Dimension** — One independently scored 1–5 scale. There is deliberately no single master "autonomy level"; each Dimension stands alone. Every Dimension yields a *Current score* and a *Future score* per Respondent and per Team.
- **Current score** — Where a Respondent (or the Team) is today on a Dimension, derived from the Current-state section (behaviour- and experience-phrased items).
- **Future score** — Where a Respondent (or the Team) wants to be on a Dimension in six months (the **Horizon**), derived from the Future-state section (aspiration-phrased items).
- **Horizon** — The future the survey asks about: six months from the survey date.
- **Gap** — Future score minus Current score, per Dimension. Positive = wants to adopt more; negative = wants to pull back.
- **Stance** — Whose position a Future-state item captures. Every Future-state item is answered twice, once per stance: **Personal stance** ("what I would do") or **Team stance** ("what the team should adopt as a norm"). Distinguishing them surfaces "I'd go further, but I don't think we should" and the reverse.
- **Team score** — Aggregate of Respondent scores on a Dimension (current or future). Includes a spread measure so disagreement is visible, not averaged away.
- **Behaviour item** — A Current-state Dimension item about something the Respondent does; answered on a frequency scale (Never … Always).
- **Attitude item** — A Current-state Dimension item about how the Respondent feels or judges; answered on a "describes me today" scale (Not at all … Completely).
- **Desirability scale** — The single scale for every Future-state item (Definitely not … Definitely), used identically for the Personal and Team stance rows.
- **Reverse-keyed item** — An item worded so that agreeing means *less* of the Dimension; its answer is flipped before scoring. Every Dimension has at least one.
- **Probe item** — A deliberately extreme statement placed at a far end of a Dimension (e.g. "I'd merge an agent's PR unread if CI is green") whose purpose is to locate people at the edges. Used instead of open-text prompts; the survey has no free-text questions.
- **Context item** — An unscored question about the Respondent (role, experience, tools used today) that becomes an extra Slice.
- **Rubric** — The rules that map raw Survey answers to Dimension scores and describe what each score level means in words.
- **Scoring sheet** — The spreadsheet/CSV template that applies the Rubric to exported responses and produces individual and Team scores.

## Dimensions (v1)

- **Comfort** — Willingness to use AI in one's own development work.
- **Trust** — Confidence that AI-produced output (code, tests, docs) is correct and safe without line-by-line scrutiny.
- **Fluency** — Practical skill with AI tools: prompting, agent workflows, setup, knowing failure modes.
- **Guardrails** — How much review, disclosure, testing and policy the Respondent wants around AI-assisted work.
- **Concern** — Perceived risk: security, IP/licensing, skill atrophy, job impact, maintainability. High = more concerned.
- **Autonomy** — How unsupervised AI may act on the Respondent's behalf: autocomplete → chat → supervised agent → autonomous agent.
- **Coverage** — Not a single score but a *profile*: an **Involvement level** per **Development area** (see below), current and future, personal and team.
- **Involvement level** — The 1–6 scale used only by the Coverage grid: 1 No AI · 2 AI explains/looks up, I do the work · 3 AI drafts, I rework every line · 4 AI does it, I review the result · 5 AI does it, I spot-check · 6 **System-verified**: AI does it all, no individual spot-check, automated checks and validation catch errors. Areas may carry custom anchor wording where it makes the question clearer.
- **Craft values** — Weight placed on general development principles (understanding every line, tests, review, ownership). A lens for interpreting the other Dimensions, not an adoption metric in itself.

## Development areas

The parts of the development lifecycle a Coverage profile is scored against. Grouped for readability; each area is scored individually.

- **Core SDLC** — Requirements/ideation · Architecture/design · Writing production code · Writing tests · Code review · Debugging · Documentation · Refactoring/legacy migration
- **Ops & delivery** — CI/CD & build config · Infrastructure-as-code · Incident response/on-call · Monitoring
- **Data & security** — SQL/data migrations · Security review/threat modeling · Dependency upgrades
- **Non-code work** — Estimates & planning · Stakeholder comms/PR descriptions · Learning new tech · Meeting notes

## Views

- **Slice** — One way of cutting the scored results: by Dimension, by Development area, by Respondent, Current vs Future, Personal vs Team stance. The Team score is never a single number; it is whichever Slice the team is looking at, each showing mean, spread and distribution.
- **Layered view** — A Slice for one topic (a Dimension or a Development area) showing every Respondent's position overlaid with the Team mean and the Team-stance target, so the team can see where it actually sits before deciding where it wants to be.
