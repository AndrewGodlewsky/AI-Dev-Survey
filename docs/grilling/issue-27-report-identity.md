# Grilling — Issue #27: Report identity, and where real exports live

**Ticket:** [Report identity, and where real exports live](https://github.com/AndrewGodlewsky/AI-Dev-Survey/issues/27)
**Map:** [Map v2: Survey overhaul & local dashboard app](https://github.com/AndrewGodlewsky/AI-Dev-Survey/issues/21)
**Round:** 1 of ~2 — four questions.
**How to use:** answer inline under each `### Your answer` heading. Free text is fine; you don't have to pick a listed option. Tell me when it's ready and I'll read it back.

---

## What is already settled coming in

- **Initials in the report, screenshots to the manager.** Your charting answer
  (`v2-destination-round-3.md` Q3): *"use the initials for people inside the
  report … take a screenshot of the pieces I need my manager to be able to
  see."* Nothing travels upward as a file. The map records the manager boundary
  as simplified.
- **Responses are named and shared openly within the team.** Initials are a
  display choice, not anonymity — at 5–9 people they identify everyone, and
  that is fine and should be *stated*, not implied as protection.
- **The v2 dashboard is the five-questions page** (decided in #26): initials
  appear as dots in Q1, range-end labels in Q4, and hover tooltips. The v1
  Internal/Exported toggle does not exist in it today.
- **The pipeline** (#26): drop the `.xlsx` in a folder, `python app/serve.py`,
  dashboard on localhost. The prototype currently defaults to a gitignored
  `data/` folder **inside** the repo, falling back to `Excel Example/`.
- **Facts about the risk, verified:** this repository is public. The real pilot
  export sits untracked in `Excel Example/` — its `Name` column is a pseudonym,
  but its `Email` column is your real work address. It has never been committed
  (checked against all history). `.gitignore` now covers `Excel Example/` and
  `*.xlsx`, with one exception (`scoring/scoring.xlsx`).

## What this round holds back

- **The exact wording of the HOW-TO-READ v2 section** on identity and
  screenshots — that is execution once Q1/Q2 are decided, not a decision.
- **The default folder's exact name/path** if Q3 lands outside the repo — I'll
  propose one in the read-back; it changes nothing structural.

---

## Q1 — What does the report show for a person?

### What this is

The app knows full names (the export's `Name` column). The five-questions page
shows people as dots and range-end labels. What identity does it render — and
what happens on hover, where there is more room?

Mechanical sub-point either way: two people can share initials in a team of
5–9. Whatever you pick, I'd disambiguate collisions by extending from the
surname (`AG` → `AGo` / `AGr`), which needs no decision unless you object.

### Why it matters

This is the last identity decision the app needs; every view inherits it. It
also decides what a manager sees *incidentally* when you screenshot: initials
survive a screenshot, hover tooltips don't.

### Options

| Option | Pros | Cons |
|---|---|---|
| **A. Initials everywhere, full name on hover** | Compact marks; screenshots carry only initials; the team (who can decode initials anyway) gets names where there's room. | Name still renderable — a screenshot taken mid-hover leaks it, if you care. |
| **B. Initials everywhere, hover shows initials too** | Nothing but initials can ever appear in any pixel. | Costs the team legibility for no real gain — initials aren't protection at n=7 anyway. |
| **C. Full names in wide spots (tables, tooltips), initials only where compact** | Most readable for the team. | Screenshots need cropping care; you said initials *inside the report*. |

### My recommendation

**A.** It matches your charting answer, keeps screenshots initials-only by
default, and spends hover space on legibility. B protects against nothing the
open-within-team rule doesn't already accept.

### Your answer

: Yeah, I think your recommendation is fine: initials everywhere, then full name on hover is good. 

---

## Q2 — What happens to v1's Internal/Exported machinery?

### What this is

v1 built a hard export boundary: an **Internal (named)** view, an **Exported
team view** (no names, counts/means/ranges only), a *Print / save as PDF*
button, "the CSV never travels upward," and a HOW-TO-READ section explaining
all of it (including the honest note that the exported view isn't anonymous at
5–9 people). Your screenshot workflow replaces the whole apparatus. Does any of
it survive into v2?

### Why it matters

Whatever survives has to be *built* in the five-questions page and *explained*
in HOW-TO-READ v2. Whatever dies should die explicitly, so the rubric/scoring
docs and HOW-TO-READ stop describing machinery that no longer exists.

### Options

| Option | Pros | Cons |
|---|---|---|
| **A. Delete it all** — one view, initials, you screenshot what the manager sees; HOW-TO-READ v2 states in two lines that initials are display, not anonymity, and screenshots are the only export | Honest about the real workflow; nothing to build; kills a whole page of explanation. | If you ever *do* want a names-stripped view to present from, it won't exist. |
| **B. Keep a "presentation mode" toggle** — one button that hides tooltips/hover during screen-shares | Guards against the mid-hover leak in Q1-A; tiny to build. | Machinery for a risk you may not care about; one more thing on screen. |
| **C. Keep the exported team view as a page** | Closest to v1; a ready-made manager artifact. | Rebuilds exactly the complexity you just asked me to strip. |

### My recommendation

**A**, and it isn't close. The five-questions redesign was a vote for less
machinery; the screenshot workflow makes the export split dead code. If the
mid-hover concern ever materializes, B is an afternoon retrofit.

### Your answer

: Let's go with your recommendation here. 

---

## Q3 — Where does real survey data permanently live?

### What this is

The core of the ticket, dodged once in charting. A named export lands somewhere
every time you run the app. Today the prototype reads gitignored `data/` inside
the public repo (and falls back to `Excel Example/`, where the real pilot
export currently sits). An ignore rule is one `git add -f`, one hook, or one
stale clone away from not helping — and your own close-hook **auto-commits and
pushes the working tree**, which raises the stakes of "inside the repo" beyond
the usual.

### Why it matters

This is the one decision where an accident is public, named, and permanent.
Everything else in the ticket is display preference; this is the privacy floor.

### Options

| Option | Pros | Cons |
|---|---|---|
| **A. A folder outside the repo** — e.g. under your user profile; the app defaults to it, path argument overrides | Real data structurally cannot be committed, by any hook, force-add, or stale ignore file. | One folder to know about; the drop-and-run flow gains one step the first time. |
| **B. Gitignored `data/` inside the repo** (what the prototype does) | Everything in one place; already built. | Public repo + named data + an auto-committing hook; protection is one ignore file. |
| **C. Path argument every run** | No standing location at all. | Friction every run; nothing stops the path being inside the repo. |

### My recommendation

**A.** The charting recommendation was A and the reasons have only strengthened
since: the close-hook now commits and pushes the tree *automatically*. Default
the app to a fixed folder outside the repo (creating it on first run, printing
where it looked), keep the path argument as the override, and delete the
in-repo `data/` folder so there is no inviting place to drop the wrong thing.

### Your answer

: Let's go with option B here. 

---

## Q4 — The real export in `Excel Example/`, and what the repo keeps as a fixture

### What this is

Housekeeping with teeth. The real pilot export (real email address) sits
untracked inside the public repo's working tree, and the app needs *some*
`.xlsx` to develop and test against. Two sub-decisions: what happens to the
real file, and does the repo get a committed, fully fake fixture?

### Why it matters

Wherever Q3 lands, a named file inside the tree is the standing hazard — and
without a fake fixture, every future session tests the parser against real
personal data, which is exactly the habit to break.

### Options

| Option | Pros | Cons |
|---|---|---|
| **A. Move the real export to the Q3 home and delete `Excel Example/`; generate a committed fake-persona `.xlsx` fixture** (invented names/emails, same 157-column shape) for dev and tests | Repo tree holds zero real data; the app is developable from a fresh clone; matches the fake-persona precedent of `scored-sample.csv`. | Someone must generate the fixture (a small script; the v1 OOXML writer shows how). |
| **B. Move the real export out; no fixture** | Simplest; zero new files. | Every dev session needs your real export again — the habit this ticket exists to end. |
| **C. Leave the real file where it is** (it's gitignored) | Nothing to do. | The hazard this whole ticket names, left in place. |

### My recommendation

**A.** And one addition worth a yes/no inside this answer: a tiny **pre-commit
guard** that blocks any staged file whose header row contains `Email` or whose
extension is `.xlsx` (except the allowed fixtures) — cheap insurance given the
auto-committing hook. Recommendation: yes, add it.

### Your answer

: Let's go with your recommendation. 

---

## Anything else

Anything these four didn't give you room for — other places real data could
leak (Forms itself, screenshots folder, backups), or anything you'd rather I
stop assuming.

### Your answer

:
