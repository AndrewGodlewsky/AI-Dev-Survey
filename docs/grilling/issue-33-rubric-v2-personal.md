# Grilling — Issue #33: Rubric v2, personal side

**Ticket:** [Rubric v2: personal side](https://github.com/AndrewGodlewsky/AI-Dev-Survey/issues/33)
**Map:** [Map v2: Survey overhaul & local dashboard app](https://github.com/AndrewGodlewsky/AI-Dev-Survey/issues/21)
**Round:** 1 of ~1 — the rewrite is already applied to `rubric/RUBRIC.md`; two questions are places where the ticket text was overtaken by later decisions, one is a judgment call on the worked example, one collects reading reactions. **Answered 2026-08-31: all four recommendations accepted (answered in chat); ticket resolved.**
**How to use:** answer inline under each `### Your answer` heading. Free text is fine; you don't have to pick a listed option. Tell me when it's ready and I'll read it back, apply any changes, and resolve the ticket.

---

## What is already settled coming in

- **The renames and deletions** are mechanical and done: *Future score* → *Direction score* throughout; every Stance-gap and norm-gap passage removed, not reworded; §3 scores a Dimension **twice** (Current, Direction) with one subtraction, **Gap = Direction − Current**, appetite minus practice.
- **The seven level-text tables are untouched** — the ticket says so explicitly: the Direction score lands on the same axes.
- **The Direction item tables** replace the Future-stem tables in §§4.1–4.7, verbatim from `survey/direction-items.md` (#32); §5 Coverage runs two passes with `Direction level − Current level` and #25's re-read N/A pairing table; §6.1 probes are single-pass, one Edge marker per Respondent per probe; §6.4 keeps the flat-block check and drops the stance-identical one (#28).
- **§1, §2, §3 now also carry the team side's arithmetic surface** (Norm score row, Agreement scale row) so the front of the document doesn't contradict §4.8 — the level text itself was #30's and is untouched.
- **The rubric's role**: the machine spec is `scoring/scoring-rules-v2.md`; RUBRIC.md agrees with it and adds the words. The intro says so instead of claiming the Scoring sheet implements it.

## What this round holds back

- Nothing is deferred; a Round 2 happens only if your answers reshape the rewrite enough to need a re-read.
- **Retiring `scoring/scored-sample.csv` and the other v1 scoring artifacts** stays map fog — §8 notes the file retires, but deleting it is the retirement ticket's business, sharp once #34 scores.

---

## Q1 — The inconsistency flag: the ticket says "narrowed", #28 says "retired"

### What this is

Ticket #33's body (written before #28 resolved) asks §6.2 to keep a **narrowed** inconsistency flag — *reads all of it* alongside a check flagged, Levers/Holds withheld. #28 then **retired the flag entirely**: under the symmetric *"which count as enough"* stem, every tick combination is a position (*reads all of it* + *tests* = either suffices), and Levers and Holds compute for everyone. `scoring/scoring-rules-v2.md` §5 and `survey/direction-items.md` both record the retirement.

### Why it matters

The rubric must agree with the scoring spec or the hand-scorer and `score()` diverge on real responses. This is the one place the ticket's own text and the map's later decision give different instructions, so it needs your eyes rather than a silent pick.

### Options

| Option | Pros | Cons |
|---|---|---|
| **Follow #28 — retired** (what the rewrite does) | Agrees with the spec Python implements; the later, deliberate decision; the symmetric-list logic genuinely dissolves the contradiction | Deviates from the ticket body as written |
| **Follow the ticket — narrowed flag** | Honors the ticket text | Contradicts `scoring-rules-v2.md`; would reopen a #28 decision from inside a rubric ticket |

### My recommendation

**Follow #28.** The ticket text is stale, not a competing decision — #24 proposed the narrowing, #28 examined it later with the symmetric list in hand and retired it. Sofia's worked example now demonstrates the retirement on the very answer v1 flagged. Not a close call, but flagged because tickets are instructions.

### Your answer

Accepted the recommendation — **follow #28: the flag is retired**; the rubric agrees with the scoring spec. (Answered in chat, 2026-08-31.)

## Q2 — The "softer Gap" roster: three, and Craft values drops off

### What this is

v1 flagged **Fluency and Craft values** as the softer Gaps. In v2 every Gap is cross-scale (Desirability against Behaviour/Attitude), and the facet-matched — softer-still — roster per `scoring-rules-v2.md` §2.3 and #32's hand-down is **Fluency (F3→D-F2), Autonomy (A2→D-A2), Concern's job-impact facet (N5→D-N5)**. Craft values is off the list: D-V2 names the speed-over-polish position outright, so V2→D-V2 is word-matched now. The rewrite says exactly this in §3, §4.3, §4.5, §4.6, §4.7 and §7.

### Why it matters

These caveats are what HOW-TO-READ v2 will quote; a wrong roster either over-trusts Autonomy's Gap or needlessly discounts Craft's.

### Options

| Option | Pros | Cons |
|---|---|---|
| **The spec's roster** (what the rewrite does): all seven softer, three softer still, Craft not among them | Matches both #32's resolution and #28's spec | Drops a v1 caveat someone may remember |
| **Keep Craft values flagged softer too** | Conservative | Contradicts the two spec files; D-V2's wording removed the reason |

### My recommendation

**The spec's roster.** #32 accepted D-V2 precisely because "ship when it works" is a wantable position — the reason for Craft's softness was cured, not forgotten. Flagged only because a caveat silently disappearing is the kind of change a reader notices later.

### Your answer

Accepted the recommendation — **the spec's roster**: all seven softer, three softer still (Fluency, Autonomy, Concern's job-impact); Craft values off the list. (Answered in chat, 2026-08-31.)

## Q3 — Sofia: self-contained, or keyed to a committed artifact?

### What this is

v1's worked example was checkable against `scoring/scored-sample.csv`. That file is a v1 artifact headed for retirement, and the v2 fixture (`app/sample-export.xlsx`) generates formulaic answers for Ada Fixture & co. — fine for parsing tests, useless as a pedagogical example. The rewrite makes Sofia **self-contained**: her v2 answers are stated in §8.1 (Current side identical — frozen section; Direction side mapped from her v1 forward answers), every number recomputable by hand, with a note that #34's tests can adopt her as a `score()` test case.

### Why it matters

The worked example is the rubric's proof that the rules are followable; whether it must also be machine-checked decides whether #34 inherits an obligation.

### Options

| Option | Pros | Cons |
|---|---|---|
| **Self-contained** (what the rewrite does), offered to #34 as an optional test case | No dead reference; no new artifact; hand-recomputable in minutes | Nothing verifies §8's arithmetic until #34 chooses to |
| **Add a Sofia row to the fixture** and key §8 to it | Machine-checkable | The fixture is a Forms-export parsing fixture, not a scoring oracle; means hand-editing generated XML or complicating `make_fixture.py` — against ponytail mode |

### My recommendation

**Self-contained**, and hand #34 the suggestion (its resolution can turn §8 into a unit test with Sofia's answers as literals). I did recompute every number while rewriting: Direction means 4.00 · 4.00 · 4.50 · 3.00 · 2.80 · 4.00 · 3.00; Gaps +1.67 · +1.67 · +2.17 · −0.40 · −0.60 · +2.00 · −0.33.

### Your answer

Accepted the recommendation — **Sofia stays self-contained**; #34 may adopt her as a `score()` test case. (Answered in chat, 2026-08-31.)

## Q4 — The rewrite itself

### What this is

The reading pass over `rubric/RUBRIC.md`: intro, §1–§3 (scales, two-score procedure, one Gap), §§4.1–4.7 (Direction tables and facet notes), §5 (two passes), §6.1 (single-pass probes), §6.2 (symmetric list; Lever · Hold · Dropped · team norm · learning interest), §6.4 (flat check only), §7, §8 (Sofia on the v2 shape), §9.

### Why it matters

This document is what a hand-scorer and the results meeting actually read; a sentence that still thinks in forecasts is the v1 defect resurfacing.

### Options

| Option | Pros | Cons |
|---|---|---|
| **Accept as rewritten** | Done | Any wording that grates stays |
| **Edit specific passages** — inline here or directly in the file | Surgical | None |

### My recommendation

Read §6.2 and §8's Safeguards paragraph hardest — they carry the most new machinery (Dropped is a new reading; Hold's "reading position in both askings" rule produces *no* Hold for Sofia, which is correct but worth a second look for surprise). Also worth a glance: §2 gained the Agreement scale row and §1 the Norm-score row, which slightly widens this ticket past "personal side" so the document's front matter doesn't contradict its own §4.8.

### Your answer

Accepted the recommendation — **the rewrite stands as applied**, §6.2 and §8 included. (Answered in chat, 2026-08-31.)

## Anything else

Anything this round missed — a passage that still reads v1, a derived reading §6.2 should also name, a glossary term to pick up?

### Your answer

Nothing raised. (Answered in chat, 2026-08-31.)
