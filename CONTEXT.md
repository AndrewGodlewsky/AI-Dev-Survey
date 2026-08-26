# AI-Dev-Survey — Domain Glossary

Ubiquitous language for the team AI-adoption survey and its rubric. Glossary only; no implementation detail.

## Core terms

- **Survey** — The questionnaire each team member completes. Split into a *Current-state section* and a *Future-state section*, which ask different questions but score the same Dimensions.
- **Respondent** — A named team member answering the Survey. Responses are not anonymous; results are shared openly within the team.
- **Dimension** — One independently scored 1–5 scale. There is deliberately no single master "autonomy level"; each Dimension stands alone. Every Dimension yields a *Current score* and a *Future score* per Respondent and per Team.
- **Current score** — Where a Respondent (or the Team) is today on a Dimension, derived from the Current-state section (behaviour- and experience-phrased items).
- **Future score** — Where a Respondent (or the Team) wants to be on a Dimension in six months (the **Horizon**), derived from the Future-state section (aspiration-phrased items).
- **Horizon** — The future the survey asks about: six months from the survey date.
- **Facet** — One distinct thing a Dimension measures. Most Dimensions have one facet per item, but a Dimension the glossary defines as a *bundle* has a facet per named part (Concern: five risks; Guardrails: five, of which disclosure is asked by two items). A **Dimension score is the mean of its facets**, a facet with more than one item being averaged first — so every facet weighs the same regardless of how many items happen to ask about it.
- **Gap** — Future score minus Current score, per Dimension, **always computed within a Stance**. Per Respondent it is always the Personal stance (`Future-Personal − Current`) — the Team stance subtracts a statement about the team from a statement about oneself, which is not a quantity. At Team level there are two: the personal Gap and the **norm gap** (`Team Future-Team − Team Current`). Positive = wants to adopt more; negative = wants to pull back.
- **Stance gap** — A Respondent's `Future-Team − Future-Personal` on a Dimension. Negative = *"I'd go further than the team should"*; positive = *"the team should go further than I would"*. Both ends are that person's own answers, so unlike the Team-stance Gap it is a real quantity.
- **Stance** — Whose position a Future-state item captures. Every Future-state item is answered twice, once per stance: **Personal stance** ("what I would do") or **Team stance** ("what the team should adopt as a norm"). Distinguishing them surfaces "I'd go further, but I don't think we should" and the reverse.
- **Team score** — Aggregate of Respondent scores on a Dimension (current or future). Includes a spread measure so disagreement is visible, not averaged away.
- **Behaviour item** — A Current-state Dimension item about something the Respondent does; answered on a frequency scale (Never … Always).
- **Attitude item** — A Current-state Dimension item about how the Respondent feels or judges; answered on a "describes me today" scale (Not at all … Completely).
- **Desirability scale** — The single scale for every Future-state item (Definitely not … Definitely), used identically for the Personal and Team stance rows.
- **Reverse-keyed item** — An item worded so that agreeing means *less* of the Dimension; its answer is flipped before scoring. Every Dimension has at least one.
- **Probe item** — A deliberately extreme, concrete statement placed at one pole of a Dimension (e.g. "I'd merge an agent's PR unread if CI is green") whose purpose is to locate people at the edges. A **marker, not a measurement**: it is *never scored* into any Dimension mean, and so is never reverse-keyed. Five exist, one pole each — Comfort (low), Trust, Autonomy, Concern, Craft values (high) — all in the Future-state section, worded so that "Definitely" is always the edge. Used instead of open-text prompts; the survey has no free-text questions. Rules and wording in `survey/probe-items.md`.
- **Edge marker** — The output of a probe: raised against a named Respondent when they answer a Probe item at 4–5, tracked separately per Stance. Also raised by an Involvement level of 6 on one of the six high-stakes Development areas. It locates a position; it does not report a fault. Non-scoring — it sits beside a Dimension score, never inside one.
- **Safeguard item** — A multi-select asking which checks a Respondent accepts **in place of reading AI's output themselves** (test suite, schema check, another reviewer, easy rollback, small blast radius, security scan — plus "I'd read it myself"). Asked three times: current, future-personal, future-team. A *Respondent-level* attribute, not a Dimension item — the same safeguards answer Trust and Autonomy at once — and never scored. Deliberately **not** phrased as a condition: the survey never asks what would change someone's mind. Text in `survey/safeguard-items.md`.
- **Lever** — A safeguard a Respondent accepts in six months but not today, **derived by subtracting** their current Safeguard item answer from their future one. Never asked directly; asking "what would have to be true?" would push people toward a position instead of describing the one they hold.
- **Context item** — An unscored question about the Respondent (role, experience, tools used today) that becomes an extra Slice.
- **Rubric** — The rules that map raw Survey answers to Dimension scores and describe what each score level means in words.
- **Scoring sheet** — The spreadsheet/CSV template that applies the Rubric to exported responses and produces individual and Team scores.
- **Scored CSV** — The single file the Scoring sheet exports and the dashboard reads: one row per Respondent, every per-Respondent value (scores, Gaps, Involvement levels, Edge markers, Safeguards, Levers, flags, raw answers) in named columns. Team-level statistics are never in it — they are computed from it. It is named and internal; it never travels to the manager and is never committed to the repository.

## Dimensions (v1)

- **Comfort** — Willingness to use AI in one's own development work.
- **Trust** — Confidence that AI-produced output (code, tests, docs) is correct and safe without line-by-line scrutiny.
- **Fluency** — Practical skill with AI tools: prompting, agent workflows, setup, knowing failure modes.
- **Guardrails** — How much review, disclosure, testing and policy the Respondent wants around AI-assisted work.
- **Concern** — Perceived risk: security, IP/licensing, skill atrophy, job impact, maintainability. High = more concerned.
- **Autonomy** — How unsupervised AI may act on the Respondent's behalf: autocomplete → chat → supervised agent → autonomous agent.
- **Coverage** — Not a single score but a *profile*: an **Involvement level** per **Development area** (see below), current and future, personal and team.
- **Involvement level** — The 1–6 scale used only by the Coverage grid, plus an N/A escape: 1 **None** (no AI) · 2 **Advisor** (AI explains, I do the work) · 3 **Drafter** (AI drafts, I rework every line) · 4 **Doer, reviewed** (AI does it, I review the result) · 5 **Doer, spot-checked** (AI does it, I spot-check) · 6 **System-verified** (AI does it end-to-end; automated checks catch errors, no individual looks) · **N/A** (I don't do this work — excluded from the profile). Four areas carry custom anchor wording: Code review, Incident response, Security review, Learning new tech. Full text in `survey/coverage-grid.md`.
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
