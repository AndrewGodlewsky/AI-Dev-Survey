# AI-Dev-Survey

A survey + rubric for a professional-dev team to locate where it is on
AI-assisted development, and which way it wants to go. Deliverables: survey doc
for Microsoft Forms, rubric, a local Python app that reads the raw Forms export
and serves the dashboard, one-page "how to read the results".

v1 is built and piloted, and is being replaced by v2 — it is a reference, not a
base to extend. See the map below.

## Start here

- Read `CONTEXT.md` first — the domain glossary. Use its terms; don't invent synonyms.
- The live wayfinder map is GitHub issue #21: https://github.com/AndrewGodlewsky/AI-Dev-Survey/issues/21.
  Work it with `/wayfinder <map url>`; one ticket per session.
  Issue #1 is the **completed** v1 map — read it for why things are the way they
  are, but never take tickets from it.
- Artifact locations: `survey/`, `rubric/`, `scoring/`, `dashboard/`, `app/`
  (the Python app, once #26 lands), `docs/`.

## Constraints

- Scoring lives in the local Python app (map v2). The v1 Excel sheet
  (`scoring/scoring.xlsx`, formulas only, no macros/VBA) is retired once Python
  scores — read it as a reference, don't extend it.
- Dashboard: served by the local Python app on localhost; `dashboard/index.html`
  is the template. v1's "one self-contained HTML file, opened from disk" rule no
  longer applies. Still no external CDNs — it runs locally and offline.
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
