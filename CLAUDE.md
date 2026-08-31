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
  (the Python app — `app/serve.py`, decided in #26), `docs/`.

## Constraints

- Scoring lives in the local Python app (map v2). The v1 Excel sheet
  (`scoring/scoring.xlsx`, formulas only, no macros/VBA) is retired once Python
  scores — read it as a reference, don't extend it.
- Dashboard: served by the local Python app on localhost. The v2 template is the
  **five-questions** page, `dashboard/prototype-simple.html` (decided in #26);
  it is **light-themed only — never add a dark variant**. `dashboard/index.html`
  is v1's dashboard, kept as a reference only — its layout is retired ("far too
  busy"). v1's "one self-contained HTML file, opened from disk" rule no longer
  applies. Still no external CDNs — it runs locally and offline.
- Responses are named and shared openly; horizon is 6 months; Dimension
  scales keep their natural direction.
- **Real survey data lives only in `data/` (gitignored) and is never committed**
  (#27). Dev and tests use the fake fixture `app/sample-export.xlsx`
  (regenerate: `python app/make_fixture.py`). A pre-commit guard blocks `.xlsx`,
  `data/*`, and Email-headed CSVs — after a fresh clone, re-arm it with
  `git config core.hooksPath .githooks`.
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

### Grilling records

**Never grill in chat.** Every `/grilling` round is written to a file the user
answers inline — don't wait to be asked. Existing records in `docs/grilling/`
are the reference; match them.

- **One file per ticket or effort**, reused across rounds:
  `docs/grilling/issue-<n>-<slug>.md` for a wayfinder ticket,
  `docs/grilling/<effort>-round-<n>.md` for a charting round.
- **Header:** ticket link, map link, `**Round:** N of ~M`, and a `How to use`
  line telling the user to answer inline and say when it's ready.
- **Then** a *What is already settled coming in* section, and a *What this round
  holds back* section naming the questions deferred to the next round and why.
- **Each question** is `## Qn — <title>` with, in order: `### What this is`,
  `### Why it matters`, `### Options` (a pros/cons table), `### My
  recommendation` (always give one, and say when it's a close call), and an
  empty `### Your answer` ending in `:`.
- Close with an `## Anything else` question, same empty `### Your answer`.
- Ask the **whole frontier** in one round — every question whose prerequisites
  are settled. A question that depends on another still open in this round
  belongs to the next round, not this one.
- After the user answers: read it back, append the next round to the **same
  file**, and link the record from the ticket's resolution comment.
