# Scoring rules

Decided in wayfinder ticket [#9](https://github.com/AndrewGodlewsky/AI-Dev-Survey/issues/9).
Grilling record: [`docs/grilling/issue-9-scoring-rules.md`](../docs/grilling/issue-9-scoring-rules.md).

How raw Microsoft Forms answers become scores. The **Rubric**, the **Scoring sheet**
([#15](https://github.com/AndrewGodlewsky/AI-Dev-Survey/issues/15)) and the **dashboard**
([#16](https://github.com/AndrewGodlewsky/AI-Dev-Survey/issues/16)) all follow this document.

> **The shape of this spec is mostly refusals.** No standard deviation, no cross-area Coverage
> mean, no averaging around blanks, no per-Respondent team-stance Gap. At n=5–9 with named
> responses the honest move is nearly always to show the points and let people look, rather
> than to summarise. Every statistic omitted is one nobody can over-read in a meeting.

---

## 1. Two kinds of scale, two kinds of statistic

The spec treats Dimension scores as **interval** (means) and Coverage as **ordinal** (medians
and distributions). That is deliberate, not an inconsistency to tidy up later:

| | Anchors | Why |
|---|---|---|
| **Dimension items** | Never · Rarely · Sometimes · Often · Always | A graded intensity. Equal spacing is a defensible approximation and the standard one. |
| **Involvement levels** | None · Advisor · Drafter · Doer-reviewed · Doer-spot-checked · System-verified | **Qualitatively distinct states.** Drafter → Doer-reviewed is a human ceasing to write and starting to check. Nothing claims that step equals 5 → 6. |

Same-looking numbers, different kinds of scale, so different statistics.

## 2. Dimension score

### 2.1 Reverse-keying comes first

`value = 6 − answer`, applied before anything else, to:

| Section | Reverse-keyed items |
|---|---|
| Current | C3 · T2 · F3 · G6 · N4 · A2 · V2 |
| Future (both stances) | FC3 · FT2 · FF3 · FG5 · FN4 · FA2 · FV2 |

### 2.2 Score = mean of **facets**, not of items

A facet with more than one item is averaged first; the Dimension score is the mean of its
facet values. Every facet weighs the same regardless of how many items happen to ask about it.

**Guardrails is the only place this differs from a flat item mean.** Current G2 (disclosure
endorsed) and G3 (disclosure practised) are one facet asked two ways; a flat mean would give
disclosure ⅓ of the Guardrails score as an artefact of item count. It would also make the
current mean (6 items) and the future mean (5 items) structurally different, so any Guardrails
Gap would partly measure the reweighting rather than a change of position.

### 2.3 The facet map

| Dimension | Current facets | Future facets |
|---|---|---|
| Comfort | C1 · C2 · C3 | FC1 · FC2 · FC3 |
| Trust | T1 · T2 · T3 | FT1 · FT2 · FT3 |
| Fluency | F1 · F2 · F3 | FF1 · FF2 · FF3 |
| **Guardrails** | G1 · **mean(G2, G3)** · G4 · G5 · G6 | FG1 · FG2 · FG3 · FG4 · FG5 |
| Concern | N1 · N2 · N3 · N4 · N5 | FN1 · FN2 · FN3 · FN4 · FN5 |
| Autonomy | A1 · A2 · A3 | FA1 · FA2 · FA3 |
| Craft values | V1 · V2 · V3 | FV1 · FV2 · FV3 |

Every **future** facet has two values, one per Stance.

**Worked example — Guardrails, current, one Respondent.** Answers G1=4, G2=5, G3=2, G4=3,
G5=4, G6=2. Reverse G6: `6 − 2 = 4`. Collapse disclosure: `mean(5, 2) = 3.5`. Facets are
`4, 3.5, 3, 4, 4` → score **3.7**. A flat item mean would have given 3.67 — close here, but it
drifts as the disclosure pair diverges, which is exactly when the number matters.

### 2.4 Decimals are the score; integers are a label

- **All arithmetic runs unrounded.** Nothing is rounded before a subtraction.
- **Display to one decimal place.**
- The **nearest integer** (halves up) is a *label* pointing at the rubric prose, presented as a
  landmark and never as the score: *"3.4 — closest to level 3: comfortable using AI on
  everyday work, but switches it off for anything important."*

Rounding before subtracting would manufacture movement nobody reported: a Current of 3.4 and a
Future of 3.6 round to 3 and 4, showing a Gap of 1 where the real movement is 0.2. Gap is the
number this survey exists to produce, so it never touches a rounded input.

**Consequence for [#17](https://github.com/AndrewGodlewsky/AI-Dev-Survey/issues/17):** a Gap of
0.3 is real and reportable. On a three-facet mean it is one person moving one facet a full
point.

### 2.5 Blank answers are a malformed export, not data

Every Dimension item and both stance rows are **Required** in Forms
([#13](https://github.com/AndrewGodlewsky/AI-Dev-Survey/issues/13) builds it that way), and #2
gave Dimension items no N/A. A blank therefore cannot be a Respondent expressing something —
it is a defect in the form or the export.

- The cell is **flagged** and the Dimension score reads `#N/A`. Visibly.
- Nothing is averaged around. No `AVERAGEIF`, no varying divisor.
- Recovery is a conversation, not a formula — the same principle #19 already applies to
  inconsistent Safeguard responses.
- A Respondent who never submits is **absent**, not blank. Every team number carries its own
  `n`, so five of nine is visible on the face of the result.

## 3. Gap

Each Respondent has three values per Dimension: **Current**, **Future-Personal**,
**Future-Team**. Not every subtraction between them is a quantity.

| Level | Gap | Meaning |
|---|---|---|
| Respondent | `Future-Personal − Current` | How far I want to move. **The only per-Respondent Gap.** |
| Respondent | **Stance gap** = `Future-Team − Future-Personal` | Negative: *"I'd go further than the team should."* Positive: *"the team should go further than I would."* |
| Team | `Team Future-Personal − Team Current` | Where people individually intend to get to. |
| Team | **Norm gap** = `Team Future-Team − Team Current` | Where people think the team should get to. |

**`Future-Team − Current` is not computed per Respondent.** It subtracts a statement about the
team from a statement about oneself. Someone at Current 2 who thinks the team should be at 4
does not have "a gap of 2"; those are answers to different questions.

**Mean-of-Gaps equals Gap-of-means** (both linear), so the sheet may compute team Gaps either
way without the two views disagreeing. This identity does **not** hold for the Coverage medians
in §5 — which is why Coverage has its own rule rather than inheriting this one.

## 4. Team score

**Mean + range (max − min) + every Respondent's value. No standard deviation.**

At n=5–9 a standard deviation is unstable and authoritative-looking: the difference between 0.8
and 1.1 is not interpretable at this n but will be quoted as though it were. The Layered view
already plots every Respondent against the team mean and the team-stance target, so compressing
seven *named* people into one statistic subtracts information the team already has. Range earns
its place only as the scalar for ordering — "which Dimension do we disagree most about".

### 4.1 The export split

The map carries a hard rule: the combined team view may reach the user's manager; individual
results never do. "Every Respondent's value" is an individual result.

| View | Contents |
|---|---|
| **Internal** — everyone who took the survey | Mean, range, `n`, every **named** Respondent's value. |
| **Exported team view** — may reach the manager | Mean, range, `n`, distribution as **unnamed counts per value**. |

A count is a team fact, not an individual result: "three people at 2, four at 4" is the
disagreement the team wants to show upward without exposing who.

**Stated, not engineered away:** at n=5–9 an unnamed distribution is partially re-identifiable
by anyone who knows the team well. #16 and #17 say so plainly. Dropping the distribution from
the export is the fallback if that is judged too close.

## 5. Coverage

### 5.1 Profile

Per Respondent, the profile is the **raw Involvement level per area** — no averaging, ever.

The team profile is **the distribution**: how many people at each level, per area. "Four at
Drafter, one at System-verified" on Security review is a conversation; "3.2" is a shrug.

The **median** is computed only where one number is unavoidable (sorting 19 areas, the Gap in
§5.2). Never a mean — the levels are named states, and because N/A is excluded, different areas
have different `n`, so two area means would not even be comparable to each other.

- **Even `n` → the lower of the two middle values.** A median of 4.5 names no level; rounding
  down is the conservative read.
- **N/A is excluded from the area's profile but its count is reported.** "Four of nine don't do
  infrastructure-as-code" is a finding about the team, and it tells you whether that area's
  profile is worth reading at all.

### 5.2 Coverage Gap

**Median of within-person differences**, reported as **signed steps** (`+2 levels`).

Compute each Respondent's own movement first, then take the typical movement. Difference-of-
medians would pair a typical Current from one person with a typical Future from another and
describe a movement nobody made. For Dimension means the two orders agree by linearity; for
medians they do not, and both should follow the same rule so the spec has one story.

**Never averaged across areas.** A mean movement over 19 heterogeneous areas is meaningless —
Meeting notes and Security review do not share a number. That is the point of Coverage being a
profile.

**Coverage Stance gap** = `Future-Team − Future-Personal` per area, same pairing rule below.

### 5.3 N/A pairing

A Coverage Gap exists **only where the same Respondent gave a numeric level in both passes.**

| Today | Future | Reading | Rule |
|---|---|---|---|
| N/A | N/A | Doesn't do this work, doesn't expect to. | Excluded from the area entirely. |
| level | level | Normal. | Gap = Future − Current, in steps. |
| **N/A** | **level** | "I don't do this work now, but I expect to." | **No Gap** — no baseline. Counted and flagged. |
| **level** | **N/A** | "I won't be doing this work in six months." | **No Gap.** Counted and flagged. |

The two mixed cases are excluded but **never silently**. They are a signal about how the team
expects its work to be distributed — a staffing signal, not an adoption signal — and folding
them into the AI numbers would mislabel one as the other.

## 6. Non-scoring outputs

Recorded here so the Scoring sheet knows what to compute; all decided elsewhere.

| Output | Rule | Decided in |
|---|---|---|
| **Probe items** | Excluded from every Dimension mean, current and future. Never reverse-keyed. | [#8](https://github.com/AndrewGodlewsky/AI-Dev-Survey/issues/8) |
| **Edge marker** — probe | Raised when a probe is answered 4 or 5, tracked **separately per Stance**. | [#8](https://github.com/AndrewGodlewsky/AI-Dev-Survey/issues/8) |
| **Edge marker** — Coverage | Involvement level **6** on the six high-stakes areas (Security review, Incident response, Code review, SQL/data migrations, IaC, CI/CD). Raised **per pass and labelled with it** — a 6 today is a different statement from wanting one in six months. | [#8](https://github.com/AndrewGodlewsky/AI-Dev-Survey/issues/8) |
| **Safeguard items** | Excluded from every Dimension mean. Respondent-level attribute. | [#19](https://github.com/AndrewGodlewsky/AI-Dev-Survey/issues/19) |
| **Lever** | Ticked in the future-personal safeguard item, not in the current one. Derived by subtraction, never asked. | [#19](https://github.com/AndrewGodlewsky/AI-Dev-Survey/issues/19) |
| **Inconsistency flag** | "I'd read it myself" ticked **alongside** another safeguard. Flagged, excluded from the Lever calculation, never resolved by rule. | [#19](https://github.com/AndrewGodlewsky/AI-Dev-Survey/issues/19) |
| **Context tools matrix** | Unscored. A Slice and a lens only. | [#7](https://github.com/AndrewGodlewsky/AI-Dev-Survey/issues/7) |

### 6.1 Pattern flags

Decided in [#20](https://github.com/AndrewGodlewsky/AI-Dev-Survey/issues/20); grilling record
[`docs/grilling/issue-20-straight-lining.md`](../docs/grilling/issue-20-straight-lining.md).

A **Pattern flag** is raised when a block of answers follows a pattern its reverse-keyed items
do not support. Non-scoring, per-Respondent, *go and ask*. **The numbers are untouched**: a
formula never decides that a named colleague was not paying attention. If the conversation
confirms it, the person re-takes the block or a human leaves them out — the malformed path.

**Why a rule and not an item.** The reverse-keys *dampen* a flat-liner but *detect* nothing: a
flat *Probably* down a 30-row Future block scores 3.3 on every three-facet Dimension, a flat
*Unsure* scores 3.0 and — since `6 − 3 = 3` — is invisible to reverse-keying altogether. And
because Forms forces the Future section into two 30-row stance blocks ([#10](https://github.com/AndrewGodlewsky/AI-Dev-Survey/issues/10)),
answering the `[Team]` block as a copy of the `[Me]` block yields a Stance gap of exactly 0 on
every Dimension — the headline reading, faked, with no visible defect. A planted or repeated
item was rejected: it leads (the non-leading rule), cannot be a true repeat (#10's uniqueness
rule), costs rows at the 152-of-200 ceiling, and reads as distrust on a named survey. The
contradiction already exists at raw-item level; this rule is the reader.

**Blocks read** — raw answers, *before* reverse-keying; blank rows excluded:

| Block | Rows | Reverse-keyed rows |
|---|---|---|
| `current` | the 17 Attitude-scale items: C3 T1 T3 F3 G1 G2 G4 G5 G6 N1 N2 N3 N4 N5 V1 V2 V3 | 5 — C3 F3 G6 N4 V2 |
| `future-personal` | the 25 `[Me]` items + 5 probes = 30 | 7 — FC3 FT2 FF3 FG5 FN4 FA2 FV2 |
| `future-team` | the 25 `[Team]` items + 5 probes = 30 | 7 — same stems |

Not read: the 9 Behaviour-scale items (a different scale, two reverse-keys — weak evidence) and
the Coverage grids (no reverse-keys, and a flat Involvement profile is a real position).

**Statistics per block** (exported, so the flag travels with its evidence):

| Statistic | Rule |
|---|---|
| **modal share** | the block's most frequent raw answer ÷ rows answered, over the **whole** block. The only statistic that sees the midpoint case. |
| **mode** | the most frequent raw answer among the block's **non-reversed** rows — what the person says when not reversed. (Taken over the whole block, a genuine "mostly 4" person's reversed rows at 2 can *become* the mode and then trivially agree with it.) |
| **reverse-key agreement** | reverse-keyed rows answered *at that mode*. A person who genuinely holds the block's modal position answers the reversed rows away from it (a *Probably* adopter answers "…keep doing things by hand" with *Probably not*); agreement means they were not read. **Not evidence at the midpoint**: when the mode is 3, a genuine moderate answers the reversed rows at 3 too, so the criterion is skipped. Tied modes: drop 3 if another value ties with it, then take the tied value with the **smaller** agreement — conservative, because a flag on a named colleague should need every reading to point the same way. |
| **stance-identical** | of the 30 Future stems, how many received the same answer in both stance blocks (pairs with a blank side excluded) |

**Flags.** The three thresholds are **named input cells** on the Scoring sheet, tunable after
the pilot without touching formulas; defaults below.

| Flag | Raised when |
|---|---|
| `flag.flat-<pass>` | mode ≠ 3 **and** reverse-key agreement ≥ (reverse-keyed rows − **1**) — i.e. ≥ 6 of 7, ≥ 4 of 5 — **or** modal share ≥ **0.90** |
| `flag.stance-identical` | stance-identical ≥ **28** of 30 |

Worked cases, 30-row block: flat *Probably* → share 1.00, agreement 7/7, flagged. Flat *Unsure*
→ share 1.00, mode 3, flagged on share alone. A genuine strong adopter — 23 rows *Definitely*, 7
reversed rows *Definitely not* — share 0.77, agreement 0/7, **not** flagged. A moderate whose
block modes at 3 with 4 of 5 reversed rows also at 3 — **not** flagged (midpoint).

**Where it shows.** Internal view only: the People page with the statistics, a marker beside
the person in the Layered view and on the Stance page, and a banner while any flag is unresolved
— *resolve before exporting*. Nothing on the Team overview or in the exported view. Wording
follows [#17](https://github.com/AndrewGodlewsky/AI-Dev-Survey/issues/17): *answers follow a
pattern the reverse-keyed items don't support — worth a conversation before the results go
upward.* Never "straight-lined".

## 7. Two Gaps are softer than the rest

Current **F3** and **V2** could not be mirrored into the Future section — on a Desirability
scale they name states nobody wants, so everyone floors at 1 and the reverse-key hands the
Dimension a constant. Their future counterparts **FF3** and **FV2** are *facet-matched, not
word-matched* ([#6](https://github.com/AndrewGodlewsky/AI-Dev-Survey/issues/6)).

No special scoring treatment — they score exactly like every other facet. But the **Fluency and
Craft values Gaps are less precise than the other five**, and
[#17](https://github.com/AndrewGodlewsky/AI-Dev-Survey/issues/17) must say so rather than let
them be read to one decimal place with the same confidence.

## 8. What this hands downstream

- **[#12](https://github.com/AndrewGodlewsky/AI-Dev-Survey/issues/12) Scored CSV** — must carry, per Respondent: 7 Current scores, 7 Future-Personal, 7 Future-Team, their facet values, 19×3 Involvement levels, and the non-scoring column family (probe answers per Stance, Edge markers per Stance and per pass, safeguards, Levers, inconsistency flag). Plus the malformed-export flag.
- **[#14](https://github.com/AndrewGodlewsky/AI-Dev-Survey/issues/14) Rubric document** — carries §2.4: the integer level is a landmark, not the score.
- **[#15](https://github.com/AndrewGodlewsky/AI-Dev-Survey/issues/15) Scoring sheet** — formulas only, no macros. The facet map in §2.3 is the one place the sheet cannot just point at a column range.
- **[#13](https://github.com/AndrewGodlewsky/AI-Dev-Survey/issues/13) Survey document** — every Dimension item and both stance rows marked **Required**.
- **[#16](https://github.com/AndrewGodlewsky/AI-Dev-Survey/issues/16) Dashboard** — the export split in §4.1 is a hard requirement, not a display preference.
- **[#17](https://github.com/AndrewGodlewsky/AI-Dev-Survey/issues/17) How to read the results** — a 0.3 Gap is real (§2.4); the Fluency and Craft Gaps are softer (§7); the re-identification residual is stated, not hidden (§4.1).
