# Grilling — Issue #9: Scoring rules

**Ticket:** [Scoring rules: items → Dimension scores, grid → Coverage profile, gaps](https://github.com/AndrewGodlewsky/AI-Dev-Survey/issues/9)
**Session:** 2026-08-26, conversational — seven questions, one at a time, each with a recommendation.
**Outcome:** [`scoring/scoring-rules.md`](../../scoring/scoring-rules.md). This record holds the *rejected* alternatives and why; the spec holds the rules.

---

## Q1 — Is a Dimension score the mean of its **items** or of its **facets**?

**Decided: facets.** A facet with more than one item is averaged first.

Rejected: **mean of items**. Guardrails has 6 current items over 5 facets (G2/G3 are disclosure asked twice), so a flat mean gives disclosure ⅓ of the score as an artefact of item count. Worse, it makes the current mean (6 items) and future mean (5 items) structurally different, so the Guardrails Gap would partly measure the reweighting rather than a change of position.

The generalisation argument mattered more than the Guardrails case itself: *"mean of facets"* survives the next item added to any Dimension, where *"mean of items"* silently re-weights the Dimension every time the bank changes — precisely the failure that would arrive unnoticed after the pilot drops an item.

## Q2 — Rounding, against a rubric defined only at integers

**Decided: decimals are the score; the nearest integer is a label only.** All arithmetic unrounded, display 1 dp, integer label presented as a landmark pointing at rubric prose.

Rejected: **round to integer and use it everywhere.** It manufactures movement. Current 3.4 and Future 3.6 round to 3 and 4 — a reported Gap of 1 where the real movement is 0.2. Gap is the survey's output, so it must never take a rounded input.

Rejected: **decimals with no rubric prose.** Arithmetically clean, humanly useless — "your Trust is 3.4" says nothing without the level text.

Framing note that survived into the spec: printing "Level 3" as a heading makes the *prose* the finding and people start arguing about the wording. Printing "3.4 — nearest level 3" keeps the number as the finding and the prose as a translation.

## Q3 — Blank answers: handle or refuse?

**Decided: refuse and flag.** A blank Dimension answer is a malformed export; the score reads `#N/A`.

Rejected: **average over whatever facets have values.** It converts a defect into a plausible-looking number. A Respondent scored on 2 of 5 Concern facets would look identical to everyone else on a dashboard whose entire output is comparisons between named people.

Three supports: given #2 (no N/A on Dimension items) and Required in Forms, a blank cannot legitimately occur; at n=5–9 with named responses the recovery path is asking the person, matching #19's *flagged, never resolved by rule*; and it is less spreadsheet — no `AVERAGEIF`, no varying divisor, in a formulas-only workbook nobody can debug with macros.

Carried out of this question: every Dimension item and both stance rows marked **Required** (→ #13); a non-submitting Respondent is **absent**, not blank, and every team number carries its `n`.

## Q4 — What is a *team* Coverage profile on an ordinal scale?

**Decided: the distribution is the profile; median only where one number is unavoidable; even `n` takes the lower middle; N/A excluded but counted.**

Rejected: **mean per area.** The Involvement levels are named, qualitatively different states — Drafter → Doer-reviewed is a human ceasing to write and starting to check, and nothing claims that equals 5 → 6. A mean asserts spacing the anchors deny, produces values naming no level, and — because N/A is excluded — runs on a different `n` per area, so two area means are not even comparable to each other.

Rejected: **mode.** Ties constantly at n=5–9 and discards spread.
Rejected: **IQR.** Quartiles at this `n` are interpolated fiction.

The distribution is also what `CONTEXT.md` already promises: *"The Team score is never a single number; it is whichever Slice the team is looking at."*

## Q5 — Which stance does a Gap subtract?

**Decided: Gap stays one definition, parameterised by level.** Per Respondent, `Future-Personal − Current` only. Per Team, two — the personal Gap and the **norm gap**. Plus a named **Stance gap** = `Future-Team − Future-Personal` per Respondent.

Rejected: **`Future-Team − Current` per Respondent.** It subtracts a statement about the team from a statement about oneself. Someone at Current 2 who thinks the team should be at 4 has not got "a gap of 2"; those are answers to different questions. The same subtraction is fine at team level, where both ends are aggregates.

Rejected: **three new nouns** (adoption gap / norm gap / stance gap as parallel terms). Parameterising the existing **Gap** by level costs less glossary and keeps the definition already in `CONTEXT.md` true.

Noted and written into the spec: mean-of-Gaps equals Gap-of-means (both linear), so the sheet may compute team Gaps either way — an identity that does **not** hold for the Coverage medians, which is why Q7 needed its own rule.

## Q6 — Which spread measure survives n = 5–9?

**Decided: mean + range + every Respondent's value. No standard deviation.**

Rejected: **standard deviation.** Unstable at this `n` and authoritative-looking — the difference between 0.8 and 1.1 is not interpretable here but will be quoted in a meeting as though it were. It also drags in a `STDEV.S` / `STDEV.P` choice someone will later assume was meaningful. With named responses already shared openly and the Layered view already plotting every point, compressing seven known people into one statistic subtracts information the team has and adds false precision.

Range survives only as the scalar for ordering — "which Dimension do we disagree most about". One outlier drives it; at n=7 that outlier *is* the disagreement.

**Collision surfaced here:** "every Respondent's value" is an individual result, and the map forbids individual results reaching the manager. Resolved by splitting the views — internal keeps names, the exported team view carries mean, range, `n` and **unnamed counts per value**. A count is a team fact, not an individual result.

Residual stated rather than engineered away: at n=5–9 an unnamed distribution is partially re-identifiable by anyone who knows the team. #16 and #17 say so; dropping the distribution from the export is the fallback.

## Q7 — Coverage Gap: aggregation order, and N/A

**Decided: median of within-person differences, in signed steps; a Gap only where the same Respondent gave a numeric level in both passes.**

Rejected: **difference of medians.** It pairs a typical Current from one person with a typical Future from another and describes a movement nobody made. For Dimension means both orders agree by linearity; for medians they diverge, and one rule should govern both so the spec has a single story.

Rejected: **averaging Coverage movement across areas.** Meaningless over 19 heterogeneous areas — Meeting notes and Security review do not share a number. That is the point of Coverage being a profile rather than a score.

The two mixed N/A cases (`N/A → level`, `level → N/A`) are excluded from the Gap but **counted and flagged**: they are a signal about how the team expects its work to be distributed. Folding a staffing signal into the AI numbers would mislabel one as the other.

Folded in without a separate question: **Coverage Stance gap** = `Future-Team − Future-Personal` per area, same pairing rule; and level-6 **Edge markers** are raised **per pass and labelled with it**, because a 6 on Security review today is a different statement from wanting one in six months.

---

## The through-line

Most of this spec is a refusal to compute: no standard deviation, no cross-area Coverage mean, no averaging around blanks, no per-Respondent team-stance Gap, no rounding before subtraction.

At n=5–9 with named responses, the honest move is nearly always to show the points and let people look rather than to summarise. Every statistic omitted is one nobody can over-read in a meeting — and every one kept has to earn its place by answering a question the raw points cannot.
