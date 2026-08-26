# Coverage grid

Decided in wayfinder ticket [#3](https://github.com/AndrewGodlewsky/AI-Dev-Survey/issues/3).

The grid appears three times in the survey: **Today**, **In 6 months — for me**, **In 6 months — the team should**. Same rows, same scale each time.

## Involvement level scale (shared by every row)

Column header wording is what Respondents see in Microsoft Forms; the long form is the rubric definition.

| # | Column header | Rubric definition |
|---|---|---|
| 1 | **None** — no AI | I do this without AI. |
| 2 | **Advisor** — AI explains, I do the work | I ask AI to explain, look up, or suggest; every artifact is written by me. |
| 3 | **Drafter** — AI drafts, I rework every line | AI produces a first draft; I read and edit all of it before it counts. |
| 4 | **Doer, reviewed** — AI does it, I review the result | AI produces the finished artifact; I review it as I would a colleague's work. |
| 5 | **Doer, spot-checked** — AI does it, I spot-check | AI produces it; I sample or skim rather than review fully. |
| 6 | **System-verified** — AI does it, checks catch errors | AI produces it end-to-end; no individual looks unless automated checks (tests, CI, policy gates, monitors) fail. |
| — | **N/A** — I don't do this work | Excluded from this Respondent's profile. |

## Rows (19 Development areas)

Each row shows the area as it will read in the survey, plus a one-line **"AI does it" example** — shown as help text under the row so levels 4–6 are concrete for that area. Rows marked **custom** get their own anchor wording (next section) because "AI does it" is ambiguous there.

| # | Group | Row text | "AI does it" means… | Anchors |
|---|---|---|---|---|
| 1 | Core SDLC | Requirements & ideation | AI turns a rough ask into user stories / acceptance criteria | shared |
| 2 | Core SDLC | Architecture & design | AI proposes the design, component boundaries, and trade-offs | shared |
| 3 | Core SDLC | Writing production code | AI writes the feature code | shared |
| 4 | Core SDLC | Writing tests | AI writes the unit/integration tests | shared |
| 5 | Core SDLC | Code review | AI reviews someone else's PR | **custom** |
| 6 | Core SDLC | Debugging | AI finds the root cause and writes the fix | shared |
| 7 | Core SDLC | Documentation | AI writes READMEs, ADRs, API docs, comments | shared |
| 8 | Core SDLC | Refactoring & legacy migration | AI performs the refactor / migration across the codebase | shared |
| 9 | Ops & delivery | CI/CD & build configuration | AI writes/changes pipelines and build files | shared |
| 10 | Ops & delivery | Infrastructure-as-code | AI writes Terraform/Bicep/etc. and applies changes | shared |
| 11 | Ops & delivery | Incident response & on-call | AI diagnoses and remediates a live incident | **custom** |
| 12 | Ops & delivery | Monitoring & alerting | AI defines dashboards/alerts and triages alerts | shared |
| 13 | Data & security | SQL & data migrations | AI writes the migration and the data backfill | shared |
| 14 | Data & security | Security review & threat modeling | AI performs the review and produces findings | **custom** |
| 15 | Data & security | Dependency upgrades | AI bumps versions and resolves breaking changes | shared |
| 16 | Non-code | Estimates & planning | AI breaks work down and sizes it | shared |
| 17 | Non-code | Stakeholder comms & PR descriptions | AI writes the update / PR description | shared |
| 18 | Non-code | Learning new tech | AI is the tutor / produces the learning material | **custom** |
| 19 | Non-code | Meeting notes & summaries | AI transcribes and summarizes | shared |

## Custom anchors

Only where the shared wording would be read two different ways.

### Code review (row 5) — the "work" is reviewing, not writing

| # | Anchor |
|---|---|
| 1 | I review PRs without AI. |
| 2 | AI explains the diff or answers my questions; I write every review comment. |
| 3 | AI drafts review comments; I rewrite them before posting. |
| 4 | AI posts its review; I still read the whole diff and add or veto comments. |
| 5 | AI posts its review; I skim the diff and its findings. |
| 6 | AI review is the merge gate; no human reviewer unless it flags something. |

### Incident response & on-call (row 11) — acting in production

| # | Anchor |
|---|---|
| 1 | I handle incidents without AI. |
| 2 | AI helps me read logs/errors and suggests hypotheses; I do everything. |
| 3 | AI proposes a diagnosis and a fix; I verify the diagnosis and rewrite the fix myself. |
| 4 | AI diagnoses and prepares the remediation; I review and execute it. |
| 5 | AI executes the remediation; I spot-check afterwards. |
| 6 | AI auto-remediates; monitors and rollback guards catch mistakes, no human in the loop. |

### Security review & threat modeling (row 14)

| # | Anchor |
|---|---|
| 1 | I do security review without AI. |
| 2 | AI explains vulnerability classes or a specific finding; I do the review. |
| 3 | AI drafts a threat model / findings list; I re-derive and rewrite it. |
| 4 | AI produces the findings; I review each finding and the code it points at. |
| 5 | AI produces the findings; I spot-check the high-severity ones. |
| 6 | AI security gates in CI decide; no human security review unless a gate fails. |

### Learning new tech (row 18) — "the work" is my understanding

| # | Anchor |
|---|---|
| 1 | I learn from docs, books, and people; no AI. |
| 2 | AI answers questions while I work through the material myself. |
| 3 | AI builds me a tailored tutorial or example; I work through and verify all of it. |
| 4 | AI summarizes the tech and I rely on the summary after checking key claims. |
| 5 | AI summarizes; I skim and trust it. |
| 6 | I don't learn it — AI applies the tech for me and checks catch errors. |
