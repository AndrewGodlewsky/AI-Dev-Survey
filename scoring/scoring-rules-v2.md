# Scoring rules v2

Decided in [#28](https://github.com/AndrewGodlewsky/AI-Dev-Survey/issues/28); grilling record
[`docs/grilling/issue-28-scoring-rules.md`](../docs/grilling/issue-28-scoring-rules.md).
This is the spec `app/serve.py`'s `score()` implements. It **replaces**
[`scoring-rules.md`](scoring-rules.md) (v1); v1's reasoning is carried by reference where a rule
is unchanged, and v1's file is a reference until the app scores.

**What died with v1's survey shape:** the Stance gap, the norm gap, the stance-identical test,
the Safeguard inconsistency flag, the Internal/Exported split, and the 293-column Scored CSV
contract. None of them has a v2 replacement, on purpose.

---

## 1. The computational core (v1 §1, §2.1–§2.5, §4 — carried verbatim)

1. **Reverse-key first**: `value = 6 − answer`, before anything else.
2. **Score = mean of facets, facets averaged first.** A facet with more than one item is
   averaged before the Dimension mean.
3. **All arithmetic unrounded.** Display one decimal. The nearest integer (halves up) is a
   *rubric landmark*, never the score. Nothing is rounded before a subtraction.
4. **A blank scored answer is a malformed export, not data.** The affected score reads `#N/A`
   visibly; nothing is averaged around. A Respondent who never submitted is *absent*; every
   team number carries its own `n`.
5. **Team score = mean + range (max − min) + every Respondent's value. No standard deviation.**
   Dimension scores are interval (means); Involvement levels are ordinal (medians and
   distributions) — v1 §1's two-scales rule stands.

## 2. Personal Dimension scores

### 2.1 Current (frozen with its section)

The v1 map verbatim: reverse-keys **C3 T2 F3 G6 N4 A2 V2**; facets per v1 §2.3, including
Guardrails' disclosure collapse **mean(G2, G3)** as one facet.

### 2.2 Direction

One item per facet — the Direction score is the mean of the Dimension's items after
reverse-keying. Reverse-keys: **D-C2 D-T2 D-F2 D-G5 D-N4 D-A2 D-V2**.

| Dimension | Items (facets) |
|---|---|
| Comfort | D-C1 · D-C2 |
| Trust | D-T1 · D-T2 |
| Fluency | D-F1 · D-F2 |
| Guardrails | D-G1 · D-G2 · D-G3 · D-G4 · D-G5 |
| Concern | D-N1 · D-N2 · D-N3 · D-N4 · D-N5 |
| Autonomy | D-A1 · D-A2 |
| Craft values | D-V1 · D-V2 |

The five **probes are never scored and never reverse-keyed** (v1 §6 rule, single pass now).

### 2.3 Gap

**Gap = Direction − Current, per Dimension, per Respondent.** Team Gap = team Direction mean −
team Current mean (equal to the mean of personal Gaps, by linearity). Appetite minus practice,
never a forecast. It is deliberately cross-scale (Desirability against Behaviour/Attitude) —
every Gap is the "softer" kind, and **three read softer still** (facet-matched, not
word-matched): **Fluency, Autonomy, and Concern's job-impact facet**. HOW-TO-READ v2 says so.

No other subtraction between blocks is a quantity. Nothing pairs a personal answer with a
team-voice answer.

## 3. Team Dimensions

### 3.1 Norm score (per Respondent)

Mean of facets, facets averaged first, after reverse-keying
(**TR3 TR6 VE3 AL3 AL4 AL6 PA2 SP3 SP6**):

| Team Dimension | Facets |
|---|---|
| Transparency | Disclosure & provenance (TR1 TR2 TR3) · Ownership & accountability (TR4 TR5 TR6) |
| Verification | Reviewing AI-assisted work (VE1 VE2 VE3) |
| Agent latitude | Parallel development (AL1 AL2 AL3) · Limits (AL4 AL5 AL6) |
| Pace | Pace & risk appetite (PA1 PA2 PA3) |
| Shared practice | Shared conventions & tooling (SP1 SP2 SP3) · Learning & skill (SP4 SP5 SP6) |

### 3.2 Team level — compute both families (Q3)

- **Norm scores**: mean + range + every Respondent's value, like any Dimension. Spread is the
  finding; range is the ordering scalar.
- **Raw answer counts per Agreement level, per item and per facet** (raw answers, before
  reverse-keying) — what a diverging stacked bar honestly plots. Binning rounded Norm scores is
  forbidden (§1.3's landmark rule).
- **Agent latitude's facet view is its primary read** (#31): a flat 3 nets *Parallel* against
  *Limits* by construction, so the two facet values ship beside the Dimension score wherever it
  goes.

## 4. Coverage (v1 §5 — carried, one pass renamed)

Two passes now: **today** and **Direction** (no team pass, no horizon in the grid).

- Per Respondent the profile is the **raw Involvement level per area** — never averaged.
- Team profile = **distribution** (count per level, per area). Median only where one number is
  unavoidable; even `n` → the **lower** middle value.
- **Coverage Gap = median of within-person moves** per area, signed steps, never averaged
  across areas. Personal Coverage Gap = Direction level − Current level where both are numeric.
- **N/A pairing** (v1 §5.3 verbatim): both N/A → excluded; one side N/A → **no Gap**, counted
  and flagged as a work-distribution signal, never an adoption signal. N/A counts are reported
  per area.
- **Edge markers**: Involvement level **6** on the six high-stakes areas (Security review,
  Incident response, Code review, SQL/data migrations, IaC, CI/CD), raised **per pass and
  labelled with it**.

## 5. Non-scoring outputs

| Output | Rule |
|---|---|
| **Probe Edge marker** | Probe answered 4–5 → one marker per Respondent per probe. Direction pass only (the only pass probes exist in). |
| **Safeguard askings** | Three (today · willingness · team norm), identical eight-option symmetric list. Never scored. |
| **Lever** | Ticked in *willingness*, not in *today*. Derived by subtraction, never asked. |
| **Hold** | A reading position ticked in both *today* and *willingness* — the line does not move. |
| **Dropped** | Ticked in *today*, not in *willingness* — a pull-back; shown, not scored. |
| **Inconsistency flag** | **Retired** (Q4). On the symmetric "which count as enough" list, every tick combination is a position; Levers/Holds compute for everyone. |
| **Context items** | Unscored; a Slice and a lens only. |

## 6. Pattern flags (Q2 — v1 §6.1 machinery on the v2 blocks)

Non-scoring, per-Respondent, *go and ask*. The numbers are untouched; never "straight-lined".
The **stance-identical test is retired** with the stance blocks.

**Blocks read** — raw answers, before reverse-keying; blank rows excluded:

| Block | Rows | Reverse-keyed rows |
|---|---|---|
| `current` | the 17 Attitude-scale items (v1 list, frozen) | 5 — C3 F3 G6 N4 V2 |
| `direction` | 20 items + 5 probes = 25 | 7 — D-C2 D-T2 D-F2 D-G5 D-N4 D-A2 D-V2 |
| `team` | the 24 team items | 9 — TR3 TR6 VE3 AL3 AL4 AL6 PA2 SP3 SP6 |

Not read: the 9 Behaviour items, the Coverage grids, the Safeguard checklists — v1's reasons
stand (weak evidence, no reverse-keys, a flat profile is a real position).

**Statistics per block** (v1 definitions verbatim): **mode** (most frequent raw answer among
non-reversed rows), **modal share** (block's most frequent answer ÷ rows answered, whole
block), **reverse-key agreement** (reversed rows answered at the mode; not evidence when the
mode is 3; tie rule: drop 3, then smaller agreement).

**Flag per block**: `mode ≠ 3 AND agreement ≥ (reversed rows − 1)` **or** `modal share ≥ 0.90`.
Thresholds are **named constants in Python**, tunable after the pilot.

## 7. The CSV export (Q5 — computed values, no raw answers)

An on-demand dashboard download, one row per Respondent, **named**, never a contract. It
contains what the dashboard knows and nothing it doesn't:

- `respondent`, `n` (roster size);
- 7 Current + 7 Direction scores, 7 Gaps; the Agent-latitude facet pair; 5 Norm scores;
- 19 × 2 Involvement levels, 19 personal Coverage Gaps (blank where N/A-paired) + the pairing
  flags;
- Edge markers (probe and Coverage, labelled), Safeguard ticks per asking, Levers, Holds,
  Dropped;
- Pattern flags **with their statistics** (mode, share, agreement, per block) — a flag travels
  with its evidence; and the malformed-export flag.

**Raw answers are not duplicated into it** — they live in the input export in `data/`. Team
statistics are never in it; they are computed from it.

## 8. Handed downstream

- **[#29](https://github.com/AndrewGodlewsky/AI-Dev-Survey/issues/29) Assemble**: every scored
  item Required; the item-text → ID map this spec keys on is #29's output.
- **[#34](https://github.com/AndrewGodlewsky/AI-Dev-Survey/issues/34) Dashboard build**:
  implements `score()` against this file; the norms chart plots §3.2's counts, never binned
  scores; unblocked by this ticket.
- **Rubric tickets [#33](https://github.com/AndrewGodlewsky/AI-Dev-Survey/issues/33) /
  [#30](https://github.com/AndrewGodlewsky/AI-Dev-Survey/issues/30)**: the integer level is a
  landmark, not the score (§1.3).
- **HOW-TO-READ v2** (map fog): a 0.3 Gap is real; the three facet-matched Gaps read softer;
  initials are display, not anonymity.
