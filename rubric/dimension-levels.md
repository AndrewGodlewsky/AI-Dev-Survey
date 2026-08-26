# Rubric — what 1–5 means for each Dimension

**DRAFT for reaction** — wayfinder ticket [#4](https://github.com/AndrewGodlewsky/AI-Dev-Survey/issues/4).

Each Dimension is scored 1–5 in its **natural direction** (Concern 5 = very concerned;
Guardrails 5 = wants the most guardrails). Levels describe a *position*, not an action, so
the same words read correctly as a **Current score** ("where I am today") and as a
**Future score** ("where I want to be / where the team should be in six months").

**Concern** and **Craft values** are worded as the *posture in force* rather than as a feeling,
because nobody sets a target for how worried they want to be. Their Future reading is
"the level of vigilance / the standard that should be in force in six months".

Coverage is not here — it is a profile, not a 1–5 score. Its scale lives in
[`survey/coverage-grid.md`](../survey/coverage-grid.md).

---

## Comfort — willingness to use AI in my own development work

| # | Level |
|---|---|
| 1 | Would rather not use AI for development work at all; uses it only when there is no alternative. |
| 2 | Uses AI for peripheral, low-stakes things — lookups, explanations, boilerplate — and keeps it away from real work. |
| 3 | Comfortable using AI on everyday work, but switches it off for anything important, unfamiliar, or high-blast-radius. |
| 4 | Reaches for AI by default on most work, including work that matters; only a few areas are deliberately held back. |
| 5 | AI is the default starting point for essentially all development work; working without it is the exception that needs a reason. |

## Trust — confidence that AI output is correct and safe without line-by-line scrutiny

| # | Level |
|---|---|
| 1 | Assumes AI output is wrong until proven otherwise; nothing is believed before it has been read in full. |
| 2 | Expects frequent errors; output is usable only after being checked end to end. |
| 3 | Trusts AI output on familiar, well-specified work; anything else gets full scrutiny. |
| 4 | Generally trusts AI output and reviews it the way a competent colleague's work is reviewed — read and judged, not re-derived. |
| 5 | Treats AI output as correct unless a test, check, or reviewer says otherwise; line-by-line reading is reserved for when something fails. |

## Fluency — practical skill with AI tools

| # | Level |
|---|---|
| 1 | Little or no hands-on use; unclear what the tools can do or how to drive them. |
| 2 | Uses a chat or autocomplete tool as it comes out of the box; prompting is ad-hoc and results are hit-or-miss. |
| 3 | Gets reliable results on ordinary tasks — knows how to supply context, iterate on a prompt, and recognise a bad answer. |
| 4 | Works fluently with agents and multi-step workflows; configures the tooling (rules, context files, MCP, permissions) and knows the common failure modes. |
| 5 | Builds and tunes AI workflows that others use; treats setup, evaluation, and failure modes as part of the craft. |

## Guardrails — how much review, disclosure, testing and policy I want around AI-assisted work

*High is not "good" — this is how much process the Respondent wants, not how responsible they are.*

| # | Level |
|---|---|
| 1 | AI-assisted work needs no special treatment; the team's existing rules are already enough. |
| 2 | Norms rather than rules: people are expected to use judgement, with maybe a convention or two and nothing enforced. |
| 3 | A few explicit expectations for AI-assisted work — e.g. tests required, author reads it before opening a PR — held by agreement. |
| 4 | Written team rules covering what must be reviewed, disclosed, and tested, plus agreed limits on where AI may be used at all. |
| 5 | Controls enforced in the tooling: mandatory disclosure, required human review, gates in CI, and named areas AI may not touch. |

## Concern — perceived risk from AI-assisted development

*Security, IP/licensing, skill atrophy, job impact, maintainability. 5 = most concerned.*

| # | Level |
|---|---|
| 1 | No meaningful risk beyond the ordinary risks of writing software; nothing here needs watching. |
| 2 | The risks are real in principle but not live for this team on this work; awareness is enough. |
| 3 | One or two risk areas warrant active attention; the rest can be left alone. |
| 4 | Several risk areas warrant active attention at once, and real damage — to code quality, skills, or the team — is expected if adoption continues unchanged. |
| 5 | Risk is the dominant fact about AI-assisted development; serious harm is expected unless something changes. |

## Autonomy — how unsupervised AI may act on my behalf

| # | Level |
|---|---|
| 1 | Inline assistance only: completions and suggestions in the editor, accepted or rejected one at a time. |
| 2 | Chat: AI answers questions and produces snippets; a human carries every change into the codebase. |
| 3 | Supervised agent: AI edits files and runs commands while a human watches each step and approves the risky ones. |
| 4 | Delegated agent: AI is handed a task and works unattended, then hands back a finished change a human reviews before it lands. |
| 5 | Autonomous agent: AI takes a task all the way to landed work, with automated checks — not a person — as the gate. |

## Craft values — weight placed on general development principles

*Understanding every line, tests, review, ownership. Not AI-specific; a lens for reading the other Dimensions.*

| # | Level |
|---|---|
| 1 | Working software is what counts; understanding, tests, and review are overhead to be skipped when they slow delivery. |
| 2 | Worth having in principle, but the first thing to drop under pressure. |
| 3 | A working baseline holds — code is reviewed, reasonably tested, and understood by whoever ships it — and is traded away deliberately when the cost is high. |
| 4 | Understanding, tests, review, and ownership are non-negotiable for anything that reaches production. |
| 5 | Craft is the point: nothing ships that its author cannot explain line by line, and depth of understanding is defended even at real cost to speed. |
