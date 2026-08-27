# Coverage grid

Rows, scale and anchors decided in wayfinder ticket [#3](https://github.com/AndrewGodlewsky/AI-Dev-Survey/issues/3) (v1).
The second pass decided in [#25](https://github.com/AndrewGodlewsky/AI-Dev-Survey/issues/25) (v2) —
grilling record [`docs/grilling/issue-25-coverage-grid.md`](../docs/grilling/issue-25-coverage-grid.md).
Governed by the [Framing rule](item-framing-rule.md), which checks this grid **as a scale** (both ends equally sayable), not as an option list.

The grid appears **twice** in the v2 survey — same 19 rows, same scale each time:

1. **The today pass** — *frozen.* Section 3 of the v1 form, verbatim. *"All of that was perfect. I don't want to change any of those questions."*
2. **The Direction pass** — replaces v1's *"In 6 months — for me"* pass. Same instrument, different question: **where do you want AI**, not where you predict you'll be. Rules in [The Direction pass](#the-direction-pass) below.

v1's third pass, *"In 6 months — the team should"*, is **cut** — the [Team section](team-section.md) is its own construct and does not mirror the grid.

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

---

## The Direction pass

**Decided** — wayfinder ticket [#25](https://github.com/AndrewGodlewsky/AI-Dev-Survey/issues/25).

v1's second pass prefixed every row with `Me in 6 months:` and asked for *"the level you would want
to be working at in six months … Pick N/A if you won't be doing that work."* The pilot answered it
from the present: *"I don't know what I'll think in six months, because if I knew, I would be
thinking that now."* It was a want-question dressed as a forecast — the same defect the
[Direction section](direction-section.md) diagnosed in the Dimension block, and it gets the same
fix: **keep the instrument, take the forecast out of the question.**

### The rules

1. **Same rows, same scale.** All 19 Development areas, the 1–6 Involvement level scale plus N/A,
   the same "AI does it" help text and the same four custom anchors — verbatim from the today
   pass. The section description is the **same block as the today pass** (*The levels*, *What
   "AI does it" means per area*, *Four areas read the levels differently*) with only the first
   line replaced.
2. **Single row, for me.** No team pass. A Respondent answers each area once.
3. **The question is *where do you want AI*.** A **Direction item** in grid form: the practice is
   the named area, the Involvement scale carries the position. Not a prediction, not a comparison
   against today.

   | Copy | Text |
   |---|---|
   | Section title | `Where do you want AI on each of these?` |
   | Description, first line | `For each area of work, pick the level you want AI at. Pick N/A if this isn't your work.` |
   | Row prefix | `Where I want AI:` — e.g. *Where I want AI: Code review* |

   The prefix exists because Forms requires every statement in the form to be unique and the today
   rows own the bare area names. It must never be `Me in 6 months:` again.
4. **No horizon in the pass.** *Six months* appears nowhere in the title, description or rows. The
   planning window is named once in the Direction section's description and nowhere else; if this
   grid is its own Forms section, it does not restate it.
5. **Framing rule check, as a scale.** *None* and *System-verified* are both equally sayable, so the
   scale is a measurement and passes. The flip — *"Where I want AI: None"* — is a normal thing to
   say. No ramp words, no *would have to*, no comparative against today. Because the scale itself
   carries both directions, the pass satisfies the Framing rule's balance floor without any row
   pointing either way.
6. **Output: a Direction level per area** — the Respondent's Involvement level on that area in
   the Direction pass, beside their **Current level** from the today pass. Together they are the
   Respondent's **Coverage** profile.

### Coverage Gap

**`Direction level − Current level`**, per area, in **signed levels** (`+2`). Read as **appetite
minus practice** — where this person would put AI on this work, against where it is — never as a
forecast. The v1 definition carries over unchanged: for a team, the **median of within-person
moves**, never averaged across areas (Meeting notes and Security review do not share a number).

A Coverage Gap exists **only where the same Respondent gave a numeric level in both passes.** The
v1 pairing table stands; its readings change from expectations to positions:

| Today | Direction | Reading | Rule |
|---|---|---|---|
| N/A | N/A | Not this person's work. | Excluded from the area entirely; counted. |
| level | level | Normal. | Gap = Direction − Current, in levels. |
| **N/A** | **level** | *"Not my work today — but if it were, here's where AI would sit."* | **No Gap** — no baseline. Counted and flagged. |
| **level** | **N/A** | *"I do this today and would rather it weren't my work."* | **No Gap.** Counted and flagged. |

The two mixed cases stay a **work-distribution signal** — now a wish rather than an expectation —
and are never folded into the AI numbers. *Coverage Stance gap* is dead with the team pass.

### Edge markers

An Involvement level of **6** on one of the six **high-stakes areas** — Code review, CI/CD & build
configuration, Infrastructure-as-code, Incident response & on-call, SQL & data migrations, Security
review & threat modeling — raises an **Edge marker** in **either pass, labelled with the pass**. A
6 today says *AI already runs this end-to-end and nobody looks*; a 6 in the Direction pass says
*I'd want it that way*. Different statements, kept apart. Non-scoring, as every Edge marker is.

### Shape

| | v1 | v2 |
|---|---|---|
| Passes | 3 (today · me in 6 months · team should) | **2** (today · Direction) |
| Grid answers | 57 | **38** |
| Coverage Gap | Future-Personal − Current | **Direction − Current** — same definition, read as appetite minus practice |
| Coverage Stance gap | Future-Team − Future-Personal | dead |
| Edge markers from the grid | per pass, three passes | per pass, **two** passes |

With the Direction section's 27 answers this puts the whole survey at **122** answers — the top of
the range [#24](https://github.com/AndrewGodlewsky/AI-Dev-Survey/issues/24) accepted. If that has
to give, the fallback is a **symmetric Checklist pair** (two multi-selects over the 19 areas —
*areas where I'd want AI doing the work* / *areas where I'd want to do the work myself*, two
answers), which is legal and directional but stops Coverage being a profile. Rejected in #25 for
that reason; recorded so the trade is visible.

### What dies with this

- The `Me in 6 months:` prefix and the *"in six months … if you won't be doing that work"*
  description — forecasting anywhere in the grid.
- The team pass, and **Coverage Stance gap** with it.
- *Future-Personal level* as a term — replaced by **Direction level**.

### What this hands downstream

- **[#29](https://github.com/AndrewGodlewsky/AI-Dev-Survey/issues/29) Assemble** — the copy in
  rule 3 goes into the form; where the pass sits and whether it is its own section is #29's call
  under the alternating-type rule. The prefix may shrink if it wraps badly in Forms, but stays a
  *want*, never a horizon.
- **[#28](https://github.com/AndrewGodlewsky/AI-Dev-Survey/issues/28) Scoring rules v2** — §5.2
  and §5.3 carry over with *Future* → *Direction* and the readings above; Coverage Stance gap
  removed; Edge markers per pass, two passes.
- **[#33](https://github.com/AndrewGodlewsky/AI-Dev-Survey/issues/33) Rubric v2, personal side** —
  §5.3 / §6.1 rewritten to the same; the worked example loses its team column.
- **[#26](https://github.com/AndrewGodlewsky/AI-Dev-Survey/issues/26) Local app** — the Coverage
  panels lose the *Team should* series and the Stance-gap column; *6 mo — me* becomes *Direction*;
  the mixed-case flags are reworded to the readings above.
