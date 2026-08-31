# Grilling — Issue #28: Scoring rules v2

**Ticket:** [Scoring rules v2: what survives the Stance gap](https://github.com/AndrewGodlewsky/AI-Dev-Survey/issues/28)
**Map:** [Map v2: Survey overhaul & local dashboard app](https://github.com/AndrewGodlewsky/AI-Dev-Survey/issues/21)
**Round:** 1 of 2 — five questions. **Answered 2026-08-31; resolved in Round 2 below.**
**How to use:** answer inline under each `### Your answer` heading. Free text is fine; you don't have to pick a listed option. Tell me when it's ready and I'll read it back and write the v2 spec (`scoring/scoring-rules-v2.md`) that `app/serve.py`'s `score()` implements.

---

## What is already settled coming in

Most of v1's spec survives by freeze or was re-decided by closed tickets; none of it is re-asked below.

- **Current-state scoring is frozen with its section**: reverse-keys (C3 T2 F3 G6 N4 A2 V2), facet means with Guardrails' `mean(G2,G3)` disclosure collapse, facets-averaged-first.
- **Gap = Direction − Current per Dimension** (#24) — appetite minus practice, cross-scale on purpose, always the "softer" kind. Stance gap and norm gap are dead; nothing resurrects them.
- **Direction section** (#32): 20 items, 7 reverse-keyed (D-C2 D-T2 D-F2 D-G5 D-N4 D-A2 D-V2); 5 probes **never scored, never reverse-keyed**; three Gaps read softer (facet-matched: Fluency, Autonomy, Concern's job-impact).
- **Team section** (#31): 24 items, 9 reverse-keyed (TR3 TR6 VE3 AL3 AL4 AL6 PA2 SP3 SP6); **Norm score** per Respondent = mean of facets, same arithmetic as any Dimension; **spread is the finding**; Agent latitude's facet view is its primary read.
- **Coverage** (#25): profile of raw levels, no averaging; team profile = distribution; median only where one number is unavoidable (even *n* → lower); **Coverage Gap = median of within-person moves, signed steps, never averaged across areas**; the N/A-pairing table carries verbatim; level-6 Edge markers on the six high-stakes areas, both passes, labelled.
- **Edge markers from probes**: answered 4–5, one per Respondent per probe, single pass now (Direction only).
- **Levers and Holds** (glossary): derived by subtracting the *today* Safeguard asking from the *willingness* asking; Hold = a reading position ticked in both. The team asking is display, never scored.
- **The export split is dead** (#27): no Internal/Exported views, no unnamed-counts export. Screenshots are the only export. The CSV is an on-demand dashboard feature (#26), not a contract — its *columns* are Q5 below.
- **Blanks**: v1's "blank = malformed export, `#N/A`, nothing averaged around" — kept unless you object in Q1; #29 will again mark every scored item Required.
- **Item text is the key**: Python resolves columns by header text. The concrete text→ID map is #29's output and the build's input, not a decision here.

## What this round holds back

- **The spec's wording** — written after this round, as the resolution.
- **Pattern-flag threshold *values*** — Q2 decides the machinery; defaults are proposed there and stay tunable constants in Python, revisited after the pilot.
- **Dashboard chart choices** feeding on these numbers — #34's business; Q3 only fixes what Python must *compute*.

---

## Q1 — Carry the v1 computational core verbatim?

### What this is

The arithmetic backbone, applied unchanged to the v2 shape:

1. Reverse-key first: `value = 6 − answer`.
2. Score = mean of **facets**, facets averaged first.
3. **All arithmetic unrounded**; display one decimal; nearest integer is a rubric *landmark*, never the score.
4. Blank scored answer = malformed export → the score reads `#N/A` visibly; nothing averaged around; a never-submitted Respondent is *absent*, and every team number carries its `n`.
5. Team score = **mean + range + every Respondent's value. No standard deviation** — at n=5–9 show the points instead.

### Why it matters

This is the whole "what survives untouched" half of the ticket. Saying yes once here lets the spec be short and lets `score()` be written without re-litigating v1.

### Options

| Option | Pros | Cons |
|---|---|---|
| **A. Carry all five verbatim** | v1's reasoning still holds; every rule was argued once already (#9). | None visible — the v2 shape changes none of the premises. |
| **B. Carry, but revisit one** (name it in your answer) | Targeted change. | Reopens settled ground. |

### My recommendation

**A.** Nothing in v2 disturbs any of the five premises; the pilot complained about the pipeline and the dashboard, never the arithmetic.

### Your answer

: Let's go with your recommendation. 

---

## Q2 — Pattern flags: rebuild on the v2 blocks, or simplify?

### What this is

v1's straight-lining detector read three blocks and had a *stance-identical* test for the copied-block cheat. The stance blocks are gone, so that test dies with them — but the flat-block risk is unchanged, and the glossary already defines the v2 Pattern flag (a flat block whose reverse-keyed rows follow along, except at the scale midpoint).

The v2 blocks that *could* be read: **Current-attitude** (17 rows, 5 reverse — unchanged from v1), **Direction** (25 rows incl. probes, 7 reverse), **Team** (24 rows, 9 reverse). v1's exclusions (Behaviour items, Coverage grids) still apply for the same reasons.

### Why it matters

A flag accuses a named colleague of not reading; the machinery has to be strong enough to be fair and simple enough to explain in the conversation it triggers. And the thresholds' *shape* decides how much of v1's statistics Python reimplements.

### Options

| Option | Pros | Cons |
|---|---|---|
| **A. Keep v1's machinery per block** — mode, modal share, reverse-key agreement; flag when (mode ≠ 3 **and** agreement ≥ reversed-rows − 1) **or** share ≥ 0.90; stance-identical retired | Proven logic; midpoint case handled; thresholds already argued in #20. Defaults: unchanged. | Three statistics to carry into Python and explain. |
| **B. Modal share only** (flag at ≥ 0.90) | One number, trivially explainable. | Misses the flat-*Probably* faker at share just under 0.9 whose reversed rows agree — the case reverse-agreement exists for. |
| **C. No flags in v2** | Least machinery. | The risk didn't go away; the reverse-keys dampen but detect nothing, as #20 showed. |

### My recommendation

**A.** The machinery ports in ~30 lines of Python, the thresholds become named constants, and the fairness argument (every reading must point the same way before a named flag is raised) was the hard-won part — keep it.

### Your answer

: Let's go with your recommendation. 

---

## Q3 — What does the Team section produce, numerically?

### What this is

Per Respondent, the **Norm score** per Team Dimension (mean of facets) is settled. The open half is what Python computes at *team* level for the norms view, because Norm scores are decimals — a person's Verification norm might be 3.7 — and the prototype's diverging stacked bars binned people into the five Agreement levels, which real decimals don't naturally do.

### Why it matters

This is the seam between scoring and the "What norms would we set?" chart: whether the dashboard bins rounded Norm scores (quietly violating "the integer is a label, not the score") or plots something computed honestly.

### Options

| Option | Pros | Cons |
|---|---|---|
| **A. Compute both**: Norm scores (mean + range + every value, like any Dimension) **and** raw answer counts per Agreement level *per item and per facet* — the stacked bars plot real counts, the spread plot uses real decimals | Both honest; the Agent-latitude facet view falls out for free; the dashboard picks per chart. | Slightly more to compute (trivial in Python). |
| **B. Norm scores only; the chart bins rounded scores** | One family of numbers. | The bars would show a binned artefact of rounding — the exact thing §2.4 exists to prevent. |
| **C. Counts only, no Norm scores** | Simplest display story. | Loses the per-person position and the spread scalar; contradicts #23's "scored". |

### My recommendation

**A.** Counts are what a diverging stacked bar honestly plots; Norm scores are what "scored, spread is the finding" promised. Computing both keeps every chart honest and costs a few lines.

### Your answer

: Let's go with your recommendation. 

---

## Q4 — Does the Safeguard inconsistency flag survive the symmetric list?

### What this is

v1 flagged a Respondent who ticked *"I'd read all of it myself"* **alongside** another safeguard, and excluded them from Lever computation — coherent when the list leaned and reading was the "real" answer. The v2 list is **symmetric**: eight equal options under a *"which of these count as enough"* stem, where ticking several means *any of these suffices*. Reading + tests is now a coherent position, not a contradiction.

### Why it matters

The flag either blocks Lever computation for people whose answers are now perfectly sensible, or it quietly disappears and the spec should say so out loud.

### Options

| Option | Pros | Cons |
|---|---|---|
| **A. Retire the flag** — any tick combination is a position; Levers/Holds compute for everyone | Matches the symmetric list's semantics; one less rule. | If someone ticks all eight without reading, nothing notices (Q2's flags don't read checklists). |
| **B. Keep a narrowed version** — flag only all-eight-ticked as "says everything suffices" | Catches the checklist straight-liner. | Ticking all eight *is* arguably a position ("I'm easy to satisfy"); flagging it contradicts the symmetric framing. |

### My recommendation

**A**, and it follows from #24's own logic: the list was made symmetric precisely so every combination reads as a position. B polices an answer the design just legitimized. Close call only if you expect checklist straight-lining to be common.

### Your answer

: Let's go with your recommendation. 

---

## Q5 — What does the on-demand CSV export contain?

### What this is

The dashboard offers a CSV download (#26's `/scored.csv`); with the 293-column contract dead, its columns are whatever we say. One row per Respondent, and the candidates: computed values (7 Current + 7 Direction scores + 7 Gaps, 5 Norm scores, 19×2 Involvement levels + Coverage Gaps), non-scoring outputs (Edge markers, Levers, Holds, Pattern flags, Safeguard ticks), and the raw answers themselves.

### Why it matters

It's the only file the app ever produces. Its columns decide what you can do in Excel later without re-running anything — and it's named data, living wherever your Downloads folder puts it.

### Options

| Option | Pros | Cons |
|---|---|---|
| **A. Everything computed + raw answers** | One file re-creates any analysis; nothing hidden in the app. | Widest file (~200 cols); another full named copy of the raw data on disk. |
| **B. Computed values + markers/flags only, no raw answers** | Everything the dashboard shows, nothing more; the raw export already exists in `data/` if needed. | Cross-checking a score against its answers needs both files side by side. |
| **C. Scores and Gaps only** | Smallest, cleanest. | Loses Coverage levels and every non-scoring output — the parts meetings actually point at. |

### My recommendation

**B.** The raw answers already live in the input file one folder over; duplicating them into every export just multiplies named copies. B is exactly "what the dashboard knows," which is what an export of the dashboard should mean.

### Your answer

: Let's go with your recommendation. 

---

## Anything else

Anything these five didn't cover — statistics you want that v1 refused (stdev?), anything about how scores meet the rubric levels, anything you'd rather I stop assuming.

### Your answer

:

---

# Round 2 — the read-back and resolution

**Answered:** 2026-08-31 — all five recommendations accepted; *Anything else* returned empty.
The spec is written: **[`scoring/scoring-rules-v2.md`](../../scoring/scoring-rules-v2.md)** —
the file `score()` in `app/serve.py` is implemented against (#34).

## The decisions

1. **Q1 — the v1 computational core carries verbatim**: reverse-key first, facet-first means,
   unrounded arithmetic with the integer-as-landmark rule, blank = malformed `#N/A`,
   team = mean + range + every value, no standard deviation.
2. **Q2 — Pattern flags keep v1's three-statistic machinery**, re-based on the three v2 blocks
   (current-attitude 17/5R · direction 25/7R · team 24/9R); the stance-identical test is
   retired with the stance blocks; thresholds are named Python constants, tunable after the
   pilot.
3. **Q3 — the Team section computes both families**: Norm scores (decimals, spread is the
   finding) *and* raw answer counts per Agreement level per item and facet — so the norms
   chart plots real counts, never binned rounded scores.
4. **Q4 — the Safeguard inconsistency flag is retired.** On the symmetric list every tick
   combination is a position; Levers, Holds and Dropped compute for everyone.
5. **Q5 — the CSV export carries computed values, markers and flags (with their statistics),
   and no raw answers** — the raw export already lives in `data/`.

## Handed downstream

- **#34** implements the spec and is unblocked by this ticket closing.
- **#29** owes every scored item Required and the item-text → ID map.
- **#33/#30** inherit the landmark rule; **HOW-TO-READ v2** inherits the softness caveats.
