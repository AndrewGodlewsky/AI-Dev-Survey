# PROTOTYPE — wayfinder #26: local app architecture

**Question:** how is the v2 app built, how does the raw Forms `.xlsx` feed it,
how does it launch, and where does the Python/browser seam go?

**Run it:** `python app/serve.py` — finds the newest `.xlsx` in `data/`
(falls back to the v1 fixture in `Excel Example/`), prints a parse summary,
serves the dashboard at `http://localhost:8737/`, opens the browser. Ctrl+C stops.

## Proposed answer (react, then fill the verdict)

1. **Project shape** — one file, `app/serve.py`; drop folder is `data/` at the
   repo root (`.gitignore` line 8, `*.xlsx`, already keeps real exports out of
   the public repo). One command, browser opens itself.
2. **Python side** — **stdlib only**: `zipfile` + `ElementTree` read the export
   (~30 lines — an `.xlsx` is a zip of XML), `http.server` serves it. No pip
   install, no venv, no framework; any Python 3 runs it. Labels resolve to
   numbers by their leading digit (`"5 – Always"`); columns resolve by header
   text, never position.
3. **The seam** — Python computes, the browser draws, and data crosses as a
   **fetch, not embedding**: the template is served *unmodified* at `/` and fed
   through its own existing `?csv=` path via a 302 to `/?csv=/scored.csv`.
   `/scored.csv` is computed in memory (doubling as the on-demand CSV export);
   `/parsed.json` exposes the parsed raw export.
4. **Frontend** — the existing vanilla-JS template, untouched. When v2 data
   changes shape, its *loader* changes; the rendering stays.
5. **Errors** — no file → message saying where to drop one; two files → newest
   by mtime, says which it ignored; not-a-zip / missing sheet → one-line
   failure naming the file; blank or duplicate headers → warned at startup.

## Stubbed, deliberately

`score()` returns the v1 **sample** CSV (`scoring/scored-sample.csv`) so the
render path is visible end to end. Real scoring is ticket #28 + the
"Scoring in Python" fog — it drops into the `score(header, rows)` slot.

## Verdict

Accepted (2026-08-31), with one redirect. The pipeline stands as prototyped —
drop the `.xlsx` in `data/`, `python app/serve.py`, dashboard on localhost,
stdlib only, fetch seam — and `serve.py` is the seed of the real app.

The redirect: the *dashboard itself* is redesigned after all. v1's layout was
"far too busy"; of three prototyped structures the user picked **B — Five
questions** (`dashboard/prototype-simple.html`, now trimmed to just B), and the
dashboard is **light-themed only** — no dark variant. So `dashboard/index.html`
stops being the v2 template; the five-questions page replaces it as the design
reference, and `serve.py` will serve that structure once real scoring (#28)
exists.
