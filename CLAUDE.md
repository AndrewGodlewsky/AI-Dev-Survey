# AI-Dev-Survey

A survey + rubric for a professional-dev team to locate its current and desired
(6-month) stance on AI-assisted development. Deliverables: survey doc for
Microsoft Forms, rubric, Excel scoring sheet, single-file HTML dashboard,
one-page "how to read the results".

## Start here

- Read `CONTEXT.md` first — the domain glossary. Use its terms; don't invent synonyms.
- The wayfinder map is GitHub issue #1: https://github.com/AndrewGodlewsky/AI-Dev-Survey/issues/1.
  Work it with `/wayfinder <map url>`; one ticket per session.
- Artifact locations: `survey/`, `rubric/`, `scoring/`, `dashboard/`, `docs/`.

## Constraints

- Excel: formulas only, no macros/VBA.
- Dashboard: one self-contained HTML file, opened from disk, no external CDNs.
- Responses are named and shared openly; horizon is 6 months; Dimension
  scales keep their natural direction.
- Git writes (commit/push/etc.) are the user's — never run them.

## Agent skills

### Issue tracker

Issues live in this repo's GitHub Issues via the `gh` CLI; external PRs are
not a triage surface. See `docs/agents/issue-tracker.md`.

### Triage labels

Canonical names: `needs-triage`, `needs-info`, `ready-for-agent`,
`ready-for-human`, `wontfix`. See `docs/agents/triage-labels.md`.

### Domain docs

Single-context: `CONTEXT.md` + `docs/adr/` at the repo root.
See `docs/agents/domain.md`.
